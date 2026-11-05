#!/usr/bin/env python3
"""WebTestBench runner + score-vs-price report.

Credentials come from the environment, never from this file:
    OPENROUTER_API_KEY or ANTHROPIC_AUTH_TOKEN   -> API key
    ANTHROPIC_BASE_URL                           -> default https://openrouter.ai/api

Examples:
    python evaluate.py                                    # report only
    python evaluate.py --run                              # all models in models.yml
    python evaluate.py --run --models hy3,glm-5.3 --skip-models gemini-3.8-flash
    python evaluate.py --run --limit 2 --models claude-haiku-5.5   # smoke test
    python evaluate.py --run --only score                 # rescore existing outputs
    python evaluate.py --run --prewarm --limit 20         # install deps first, then evaluate

models.yml is read from this file's directory. The dataset and the web apps both
come from --data-root (default ./data/WebTestBench, what process/download_dataset.py
fills in).

Output:
    report mode (default)
        Rebuilds the tables from artifacts that already exist. Reads nothing else:
            outputs/<version>/<index>/score.json         # coverage/precision/recall/f1
            outputs/<version>/<index>/session_meta.json  # token usage, reported cost
        and emits:
            outputs/benchmark.jsonl       # one line per (version, task)
            outputs/score_vs_price.csv    # one row per model: score vs $/1M tokens
            outputs/score_vs_price.xlsx   # same table as a spreadsheet
            outputs/score_vs_price.png    # scatter plot

Cost comes from models.yml (see the cost_source column):
    price_table_estimate    tokens x price_in/price_cache_read/price_out
    unavailable             models.yml has no prices for this model

Claude Code's own total_cost_usd is deliberately ignored: it prices every model
with Anthropic's first-party rate cards, so keep models.yml prices updated with
`python process/refresh_prices.py`.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import matplotlib
import yaml
from openpyxl import Workbook
from openpyxl.styles import Font

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  (must follow matplotlib.use)

ROOT = Path(__file__).resolve().parent

# Dev servers bind BASE_PORT + int(record_id[-4:]). Override the base only if that
# range is already busy on your machine.
SHARD_RETRIES = 2
try:
    BASE_PORT = int(os.environ.get("WEBTESTBENCH_BASE_PORT", "6000").strip())
except ValueError:
    raise SystemExit("WEBTESTBENCH_BASE_PORT must be an integer, e.g. 6000")

PRINT_LOCK = threading.Lock()
LIVE_PROCS: List[subprocess.Popen] = []
PROC_LOCK = threading.Lock()


def log(message: str = "") -> None:
    with PRINT_LOCK:
        print(message, flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # what to run
    p.add_argument("--run", action="store_true", help="run eval + scoring before reporting (default: report only)")
    p.add_argument("--models", default="all", help="models.yml keys, comma separated, or 'all' (default)")
    p.add_argument("--skip-models", default="", help="models.yml keys to exclude")
    p.add_argument("--only", choices=("all", "eval", "score"), default="all", help="with --run: all = eval+scoring, eval = skip scoring, score = rescore only")
    p.add_argument("--limit", type=int, default=0, help="only the first N tasks (smoke test)")
    p.add_argument("--dry-run", action="store_true", help="print the plan, run nothing")

    # sharding
    p.add_argument("--jobs", type=int, default=10, help="dataset shards per model (default: 10; each shard runs its own dev server, so lower it on a small machine)")
    p.add_argument("--prewarm", action="store_true", help="run npm install once per project, sequentially, before evaluating (makes each task's install a fast no-op)")
    p.add_argument("--judge-model", default=os.environ.get("JUDGE_MODEL", "qwen/qwen3.5-27b"), help="model used by eval/scoring.py to match items to gold")

    # paths (models.yml is expected next to this file)
    p.add_argument("--data-root", default="./data/WebTestBench", help="holds WebTestBench.jsonl and web_applications/")
    p.add_argument("--output-root", default="./outputs", help="artifacts, logs, work dir and reports")
    return p.parse_args()


# ----------------------------------------------------------------------
# models.yml
# ----------------------------------------------------------------------
def load_models(models_yml: Path) -> Dict[str, dict]:
    """{short_name: {key, model_id, price_in, price_out}}, keyed by the model-id basename."""
    if not models_yml.exists():
        return {}

    configs = (yaml.safe_load(models_yml.read_text(encoding="utf-8")) or {}).get("models") or {}
    return {
        str(cfg.get("model_id") or key).split("/")[-1]: {
            "key": key,
            "model_id": str(cfg.get("model_id") or ""),
            "price_in": _as_float(cfg.get("price_in")),
            "price_out": _as_float(cfg.get("price_out")),
            "price_cache_read": _as_float(cfg.get("price_cache_read")),
            "price_cache_write": _as_float(cfg.get("price_cache_write")),
        }
        for key, cfg in configs.items()
        if isinstance(cfg, dict)
    }


def _as_float(value: Any) -> Optional[float]:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# ----------------------------------------------------------------------
# Per-task artifacts
# ----------------------------------------------------------------------
def _read_json(path: Path) -> Optional[dict]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _session_totals(session_meta: dict) -> Dict[str, float]:
    """Sum token counters and turns over every stage of session_meta.json.

    Prefers the CLI's `model_usage` aggregate, which also counts auxiliary calls
    such as session-title generation; older artifacts only have `token_usage`.
    """
    totals = {
        "prompt_tokens": 0.0,
        "output_tokens": 0.0,
        "cache_read_tokens": 0.0,
        "cache_creation_tokens": 0.0,
        "num_turns": 0.0
    }

    stages = session_meta.values() if isinstance(session_meta, dict) else ()
    for entry in stages:
        if not isinstance(entry, dict):
            continue
        totals["num_turns"] += _as_float(entry.get("num_turns")) or 0.0

        models = entry.get("model_usage")
        if isinstance(models, dict) and models:
            for model_usage in models.values():
                if not isinstance(model_usage, dict):
                    continue

                totals["prompt_tokens"] += _as_float(model_usage.get("inputTokens")) or 0.0
                totals["output_tokens"] += _as_float(model_usage.get("outputTokens")) or 0.0
                totals["cache_read_tokens"] += _as_float(model_usage.get("cacheReadInputTokens")) or 0.0
                totals["cache_creation_tokens"] += _as_float(model_usage.get("cacheCreationInputTokens")) or 0.0

            continue  # don't also add token_usage for this stage

        usage = entry.get("token_usage")
        if isinstance(usage, (int, float)):  # a stage that only reports one number
            totals["prompt_tokens"] += float(usage)
            continue

        for name, value in (usage or {}).items() if isinstance(usage, dict) else ():
            if not isinstance(value, (int, float)):
                continue

            low = str(name).lower()
            if "cost" in low:
                continue  # prices come from models.yml, never from the run
            if "cache_read" in low:
                totals["cache_read_tokens"] += float(value)
            elif "cache_creation" in low or "cache_write" in low:
                totals["cache_creation_tokens"] += float(value)
            elif "output" in low:
                totals["output_tokens"] += float(value)
            elif "input" in low or "prompt" in low:
                totals["prompt_tokens"] += float(value)

    return totals

def _result_bytes(task_dir: Path) -> int:
    """Bytes of result_extracted.md, or 0 when absent. The one definition of "has result"."""
    path = task_dir / "result_extracted.md"
    return path.stat().st_size if path.exists() else 0

def collect_task(
    version_dir: Path,
    task_dir: Path,
    model: dict,
    gold_items: Optional[int] = None
) -> Optional[dict]:
    score = _read_json(task_dir / "score.json") or {}
    session = _read_json(task_dir / "session_meta.json") or {}
    if not score and not session:
        return None

    overall = score.get("overall") or {}
    match_info = _read_json(task_dir / "score_match_ids.json") or {}
    checklist_path = task_dir / "checklist.md"

    # binary on purpose: an error, a timeout and a model that could not handle the
    # input all count as "empty"; only produced test output counts as a result
    result_bytes = _result_bytes(task_dir)
    status = "has_result" if result_bytes else "empty"

    checklist_text = checklist_path.read_text(encoding="utf-8") if checklist_path.exists() else ""
    checklist_items = sum(1 for line in checklist_text.splitlines() if line.startswith("- ["))

    totals = _session_totals(session)
    prompt_tokens = int(
        totals["prompt_tokens"] + totals["cache_read_tokens"] + totals["cache_creation_tokens"]
    )
    output_tokens = int(totals["output_tokens"])

    price_in = model.get("price_in")
    price_out = model.get("price_out")
    price_cache = model.get("price_cache_read")
    price_write = model.get("price_cache_write")

    cost = None
    if price_in is not None and price_out is not None:
        # cached tokens bill at their own rates; a model without a published rate
        # is billed at the input price for that bucket
        read_rate = price_in if price_cache is None else price_cache
        write_rate = price_in if price_write is None else price_write
        cost = (
            totals["prompt_tokens"] / 1_000_000 * price_in
            + totals["cache_creation_tokens"] / 1_000_000 * write_rate
            + totals["cache_read_tokens"] / 1_000_000 * read_rate
            + output_tokens / 1_000_000 * price_out
        )

    cost_source = "price_table_estimate" if cost is not None else "unavailable"

    return {
        "version": version_dir.name,
        "model": model.get("model_id"),
        "model_key": model.get("key"),
        "index": task_dir.name,
        "status": status,
        "result_bytes": result_bytes,
        "gold_items": gold_items,
        "checklist_items": checklist_items,
        "scored_from": match_info.get("source"),
        "coverage": overall.get("coverage"),
        "precision": overall.get("precision"),
        "recall": overall.get("recall"),
        "f1": overall.get("f1"),
        "num_pred_item": overall.get("num_pred_item"),
        "prompt_tokens": prompt_tokens,
        "output_tokens": output_tokens,
        "cache_read_tokens": int(totals["cache_read_tokens"]),
        "cache_creation_tokens": int(totals["cache_creation_tokens"]),
        "total_tokens": prompt_tokens + output_tokens,
        "num_turns": int(totals["num_turns"]),
        "cost_usd": None if cost is None else round(cost, 6),
        "cost_source": cost_source,
        "price_in": price_in,
        "price_out": price_out,
    }


# ----------------------------------------------------------------------
# Aggregation
# ----------------------------------------------------------------------
def _mean(values: Iterable[Optional[float]]) -> Optional[float]:
    clean = [v for v in values if isinstance(v, (int, float))]
    return round(sum(clean) / len(clean), 4) if clean else None

def _total(rows: List[dict], key: str) -> int:
    return int(sum(r.get(key) or 0 for r in rows))

def aggregate(version: str, rows: List[dict], model: dict, total_tasks: Optional[int]) -> dict:
    scored = [r for r in rows if r.get("f1") is not None]
    tokens = _total(rows, "total_tokens")
    cost = sum(r["cost_usd"] or 0.0 for r in rows)
    means = {k: _mean(r[k] for r in scored) for k in ("coverage", "precision", "recall", "f1")}
    f1 = means["f1"]
    blended = round(cost / tokens * 1_000_000, 4) if tokens and cost else None

    # reliability: was each score actually derived from test output?
    from_result = sum(1 for r in scored if r["scored_from"] == "result")
    from_checklist = sum(1 for r in scored if r["scored_from"] == "checklist")
    weighted = [
        (r["coverage"], r["gold_items"])
        for r in scored
        if r["coverage"] is not None and r["gold_items"]
    ]
    gold_scored = sum(g for _, g in weighted)
    coverage_weighted = round(sum(c * g for c, g in weighted) / gold_scored, 4) if gold_scored else None

    return {
        "version": version,
        "model": model.get("model_id"),
        "model_key": model.get("key"),
        "tasks_attempted": len(rows),
        "tasks_scored": len(scored),
        "tasks_total": total_tasks,
        "tasks_has_result": sum(1 for r in rows if r["status"] == "has_result"),
        "tasks_empty": sum(1 for r in rows if r["status"] == "empty"),
        "tasks_scored_from_result": from_result,
        "tasks_scored_from_checklist": from_checklist,
        "scored_from_result_ratio": round(from_result / len(scored), 4) if scored else None,
        "gold_items_total": gold_scored,
        "pred_items_total": _total(rows, "num_pred_item"),
        "checklist_items_total": _total(rows, "checklist_items"),
        "coverage_weighted": coverage_weighted,
        **means,
        "avg_num_pred_item": _mean(r["num_pred_item"] for r in scored),
        "prompt_tokens": _total(rows, "prompt_tokens"),
        "output_tokens": _total(rows, "output_tokens"),
        "cache_read_tokens": _total(rows, "cache_read_tokens"),
        "cache_creation_tokens": _total(rows, "cache_creation_tokens"),
        "total_tokens": tokens,
        "avg_tokens_per_task": round(tokens / len(rows), 1) if rows else None,
        "num_turns": _total(rows, "num_turns"),
        "cost_usd": round(cost, 4),
        "cost_source": next((r["cost_source"] for r in rows if (r["cost_usd"] or 0) > 0), "unavailable"),
        "price_in": model.get("price_in"),
        "price_out": model.get("price_out"),
        "usd_per_1m_blended": blended,
        "score_per_usd_f1": round(f1 / cost, 4) if (f1 is not None and cost) else None,
        "usd_per_task": round(cost / len(rows), 6) if rows else None,
        "cost_per_f1_point_usd": round(cost / (f1 * 100), 6) if (f1 and cost) else None,
    }


# ----------------------------------------------------------------------
# Outputs
# ----------------------------------------------------------------------
def write_xlsx(path: Path, agg: List[dict]) -> None:
    """One row per model with real numbers; metrics that do not apply stay empty."""
    workbook = Workbook()
    sheet = workbook.worksheets[0]  # Workbook() always ships one sheet
    sheet.title = "score_vs_price"
    if agg:
        columns = list(agg[0])
        sheet.append(columns)

        for row in agg:
            sheet.append([row.get(col) for col in columns])
        for cell in sheet[1]:
            cell.font = Font(bold=True)

        sheet.column_dimensions["A"].width = 34

    workbook.save(str(path))


def fmt(value: Any, digits: int) -> str:
    return "" if value is None else f"{value:.{digits}f}"


def write_csv(path: Path, rows: List[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def maybe_plot(path: Path, agg: List[dict]) -> Optional[str]:
    pts = [r for r in agg if r["f1"] is not None and r["usd_per_1m_blended"]]
    if not pts:
        return None

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(
        [r["usd_per_1m_blended"] for r in pts],
        [r["f1"] for r in pts],
        s=[max(30.0, (r["total_tokens"] or 1) / 5000.0) for r in pts],  # bubble = tokens used
        alpha=0.75, edgecolors="black", linewidths=0.6,
    )
    for r in pts:
        ax.annotate(r["model"], (r["usd_per_1m_blended"], r["f1"]),
                    textcoords="offset points", xytext=(5, 4), fontsize=8)
    ax.set_xlabel("Observed blended price (USD per 1M tokens)")
    ax.set_ylabel("Mean checklist F1")
    ax.set_title("WebTestBench: score vs cost")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(str(path), dpi=150)
    plt.close(fig)
    return str(path)


# ----------------------------------------------------------------------
# Sweep: models.yml -> eval -> scoring
# ----------------------------------------------------------------------
class Sweep:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        if args.jobs < 1:
            raise SystemExit("--jobs must be >= 1")

        self.data_root = Path(args.data_root).resolve()
        self.dataset = self.data_root / "WebTestBench.jsonl"
        self.project_root = self.data_root / "web_applications"
        self.output_root = Path(args.output_root).resolve()
        self.models_yml = ROOT / "models.yml"
        # Everything the run produces lives under one root:
        #   outputs/<version>/...          artifacts
        #   outputs/logs/{eval,scoring}/   logs
        #   outputs/work/                  shards
        self.log_root = self.output_root / "logs" / "eval"
        self.work_root = self.output_root / "work"
        self.do_eval = args.only in ("all", "eval")
        self.do_score = args.only in ("all", "score")
        # Credentials are only validated when something is actually executed, so
        # `--dry-run` / report mode work without a key in the environment.
        self.base_url, self.api_key = self._env_credentials()

        if not self.models_yml.exists():
            raise SystemExit(f"models file not found: {self.models_yml}")
        if not self.dataset.exists():
            raise SystemExit(
                f"dataset not found: {self.dataset}\n"
                "WebTestBench does not fetch data automatically. Download it once with:\n"
                "  python process/download_dataset.py --unzip    (~23 MB, from Hugging Face)\n"
                "then re-run this command."
            )

        self.records = [
            line
            for line in self.dataset.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if args.limit:
            self.records = self.records[: args.limit]

        # Ports are BASE_PORT + int(record_id[-4:]); fail here rather than per task.
        highest = 0
        for line in self.records:
            try:
                rid = str(json.loads(line).get("index", ""))
            except Exception:
                continue

            highest = max(highest, int(rid[-4:]) if rid[-4:].isdigit() else 0)

        if highest and BASE_PORT + highest > 65535:
            raise SystemExit(
                f"WEBTESTBENCH_BASE_PORT={BASE_PORT} + task offset {highest} exceeds 65535; set it lower."
            )

    # -- environment / dataset ------------------------------------------
    @staticmethod
    def _env_credentials() -> Tuple[str, str]:
        """Provider URL + API key from the environment (never from disk)."""
        key = (os.environ.get("OPENROUTER_API_KEY")
               or os.environ.get("ANTHROPIC_AUTH_TOKEN")
               or os.environ.get("API_KEY")
               or "")
        base = os.environ.get("ANTHROPIC_BASE_URL") or "https://openrouter.ai/api"
        return base, key

    def require_credentials(self) -> None:
        if not self.api_key:
            raise SystemExit(
                "no API key found. Export it in your shell (.bashrc), e.g.\n"
                '  export OPENROUTER_API_KEY="sk-or-v1-..."\n'
                '  export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"\n'
                '  export ANTHROPIC_BASE_URL="https://openrouter.ai/api"'
            )

    def _append_run_log(self, payload: dict) -> None:
        path = self.output_root / "sweep.jsonl"
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False, default=str) + "\n")

    # -- model selection ------------------------------------------------
    def selected(self) -> List[Tuple[str, str]]:
        models = load_models(self.models_yml)  # {short: {key, model_id, ...}}
        if not models:
            raise SystemExit(f"no models found in {self.models_yml}")
        raw = self.args.models.strip()
        only: set[str] = set() if raw.lower() in ("", "all", "*") else {
            m.strip() for m in raw.split(",") if m.strip()
        }
        skip = {m.strip() for m in self.args.skip_models.split(",") if m.strip()}
        if only & {"all", "*"}:
            only = set()
        chosen = []
        for short, cfg in models.items():
            key = cfg.get("key", short)
            model_id = cfg.get("model_id", short)
            if only and not (only & {key, model_id, short}):
                continue
            if key in skip or short in skip:
                continue
            chosen.append((key, model_id))
        if only and not chosen:
            available = ", ".join(cfg.get("key", short) for short, cfg in models.items())
            raise SystemExit(f"no model matched --models {raw}\navailable: {available}")
        return chosen

    # -- one model ------------------------------------------------------
    def run_model(self, key: str, model_id: str) -> dict:
        args = self.args
        version = f"claudecode-{model_id.split('/')[-1]}"
        base_port = BASE_PORT
        started = time.time()
        result = {
            "key": key,
            "model": model_id,
            "version": version,
            "base_port": base_port,
            "status": "ok",
            "shards_failed": 0,
            "scoring_rc": None
        }

        project_dir = self.project_root
        log(f"[{version}] start  model={model_id}  ports={base_port}+  projects={project_dir}")

        if self.do_eval:
            failed = self.run_eval(version, model_id, base_port, project_dir)
            result["shards_failed"] = failed
            if failed:
                result["status"] = "eval_failed"

        if self.do_score:
            rc = self.run_scoring(version)
            result["scoring_rc"] = rc
            if rc != 0 and result["status"] == "ok":
                result["status"] = "score_failed"

        result["duration_s"] = round(time.time() - started, 1)
        log(f"[{version}] {result['status']} in {result['duration_s']}s")
        self._append_run_log(result)
        return result

    # -- eval -----------------------------------------------------------
    def run_eval(self, version: str, model_id: str, base_port: int, project_dir: Path) -> int:
        args = self.args
        shard_dir = self.work_root / "shards"
        shard_dir.mkdir(parents=True, exist_ok=True)
        console_dir = self.log_root / version
        console_dir.mkdir(parents=True, exist_ok=True)

        total = len(self.records)
        per_shard = max(1, (total + args.jobs - 1) // args.jobs)
        shards = []
        for i in range(0, total, per_shard):
            chunk = self.records[i:i + per_shard]
            if not chunk:
                continue
            path = shard_dir / f"{version}.{len(shards):03d}.jsonl"
            path.write_text("\n".join(chunk) + "\n", encoding="utf-8")
            shards.append(path)

        env = os.environ.copy()
        for var in ("ANTHROPIC_DEFAULT_SONNET_MODEL", "ANTHROPIC_DEFAULT_OPUS_MODEL",
                    "ANTHROPIC_DEFAULT_HAIKU_MODEL"):
            env[var] = model_id

        log(f"[{version}] launching {len(shards)} shard(s); logs in {console_dir}")
        remaining = list(shards)
        # eval/run_agent.py aborts a shard on the first task exception, so retry it:
        # finished tasks are skipped, which is equivalent to continue-on-error.
        for attempt in range(1, SHARD_RETRIES + 2):
            if not remaining:
                break
            if attempt > 1:
                log(f"[{version}] retrying {len(remaining)} shard(s), attempt {attempt}")
            with ThreadPoolExecutor(max_workers=max(1, len(remaining))) as pool:
                rcs = list(pool.map(
                    lambda s: self.run_shard(s, version, model_id, base_port, project_dir, env, attempt),
                    remaining,
                ))
            remaining = [s for s, rc in zip(remaining, rcs) if rc != 0]

        for shard in shards:
            shard.unlink(missing_ok=True)
        for shard in remaining:
            log(f"[{version}] shard {shard.name} failed (see {console_dir})")
        return len(remaining)

    def run_shard(self, shard: Path, version: str, model_id: str, base_port: int,
                  project_dir: Path, env: dict, attempt: int) -> int:
        """Run one shard to completion and return its exit code."""
        suffix = "" if attempt == 1 else f"_retry{attempt}"
        console_path = self.log_root / version / f"_shard_{shard.stem}{suffix}.log"
        cmd = [
            sys.executable, "eval/run_agent.py",
            "--agent", "claude_code",
            "--data_jsonl_path", str(shard),
            "--project_root", str(project_dir),
            "--output_root", str(self.output_root),
            "--log_root", str(self.log_root),
            "--version", version,
            "--base_port", str(base_port),
            "--api_base_url", self.base_url,
            "--api_key", self.api_key,
            "--model", model_id,
        ]
        with console_path.open("w", encoding="utf-8") as console:
            proc = subprocess.Popen(cmd, cwd=str(ROOT), env=env,
                                    stdout=console, stderr=subprocess.STDOUT)
            with PROC_LOCK:
                LIVE_PROCS.append(proc)
            try:
                rc = proc.wait()
            finally:
                with PROC_LOCK:
                    if proc in LIVE_PROCS:
                        LIVE_PROCS.remove(proc)
        if rc != 0:
            log(f"[{version}] shard {shard.name} exited {rc} (log: {console_path})")
        return rc

    # -- scoring --------------------------------------------------------
    def run_scoring(self, version: str) -> int:
        args = self.args
        log_dir = self.log_root.parent / "scoring"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / f"log_{time.strftime('%Y_%m_%d_%H_%M')}_{version}.log"
        cmd = [
            sys.executable, "eval/scoring.py",
            "--dataset_path", str(self.dataset if not args.limit else self._limited_dataset()),
            "--output_root", str(self.output_root),
            "--version", version,
            "--use_checklist_fallback", "True",
            "--api_base_url", self.base_url,
            "--api_key", self.api_key,
            "--api_model", args.judge_model,
        ]
        log(f"[{version}] scoring with judge {args.judge_model}")
        with log_path.open("w", encoding="utf-8") as handle:
            rc = subprocess.call(cmd, cwd=str(ROOT), stdout=handle, stderr=subprocess.STDOUT)
        if rc != 0:
            log(f"[{version}] scoring exited {rc} (log: {log_path})")
        return rc

    def _limited_dataset(self) -> Path:
        path = self.work_root / f"dataset.limit{len(self.records)}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(self.records) + "\n", encoding="utf-8")
        return path

    # -- prewarm --------------------------------------------------------
    def prewarm(self) -> int:
        """Run `npm install` once per project, sequentially, before the sweep.

        Every task installs inside its own project directory during server_deploy;
        doing it up front, one project at a time, keeps a cold install out of the
        sharded phase, where several concurrent installs are what fail on a shared
        (and on this machine, near-full) disk. Idempotent: warm projects report
        "already warm" and cost a few milliseconds.
        """
        cmd = [
            sys.executable, "process/prewarm_dependencies.py",
            "--project_root", str(self.project_root),
        ]

        # With --limit, warm only the projects this run will touch.
        if self.args.limit:
            ids = []
            for line in self.records:
                try:
                    rid = str(json.loads(line).get("index") or "")
                except Exception:
                    rid = ""
                if rid:
                    ids.append(rid)
            if ids:
                cmd += ["--only", ",".join(ids)]

        log(f"[prewarm] npm install, one project at a time, under {self.project_root}")
        rc = subprocess.call(cmd, cwd=str(ROOT))
        if rc != 0:
            log(f"[prewarm] exited {rc}; each task will still install on its own")
        return rc

    # -- progress -------------------------------------------------------
    def finished_tasks(self) -> int:
        """Count tasks that actually produced test output, across all model dirs."""
        total = 0
        for version_dir in self.output_root.iterdir():
            if not version_dir.is_dir() or version_dir.name in ("logs", "work"):
                continue
            total += sum(1 for d in version_dir.iterdir() if _result_bytes(d))
        return total

    def heartbeat(self, stop: threading.Event, models_total: int) -> None:
        """Print finished-task count every 2 minutes, so a long sweep is not silent."""
        last = -1
        while not stop.wait(120):
            try:
                count = self.finished_tasks()
            except Exception:
                continue
            if count != last:
                log(f"... {count} task result(s) on disk for {models_total} model(s) in this run")
                last = count


def run_sweep(args: argparse.Namespace) -> int:
    """Execute the eval + scoring sweep; returns a process exit code."""
    sweep = Sweep(args)
    todo = sweep.selected()

    log(
        f"models: {len(todo)}  jobs/model: {args.jobs}  "
        f"tasks: {len(sweep.records)}"
    )
    for key, model_id in todo:
        log(f"  - {key:<24} {model_id}")

    if args.dry_run:
        log("\ndry run: nothing executed")
        return 0

    sweep.require_credentials()
    if not sweep.project_root.exists() and sweep.do_eval:
        raise SystemExit(
            f"project root not found: {sweep.project_root}\n"
            "run `python process/unzip_web_applications.py` first (or pass --project-root)."
        )
    sweep.output_root.mkdir(parents=True, exist_ok=True)

    if args.prewarm and sweep.do_eval:
        sweep.prewarm()

    stop = threading.Event()
    threading.Thread(target=sweep.heartbeat, args=(stop, len(todo)), daemon=True).start()

    results: List[dict] = []
    try:
        for key, model_id in todo:
            try:
                results.append(sweep.run_model(key, model_id))
            except Exception as exc:  # one model failing must not discard the others
                log(f"[{key}] {type(exc).__name__}: {exc}")
                results.append({
                    "key": key, "model": model_id,
                    "version": f"claudecode-{model_id.split('/')[-1]}",
                    "base_port": BASE_PORT, "status": "error",
                    "shards_failed": 0, "scoring_rc": None, "duration_s": "?",
                })
    except KeyboardInterrupt:
        log("\ninterrupted: stopping child processes (finished tasks are kept in outputs/)")
        with PROC_LOCK:
            for proc in LIVE_PROCS:
                proc.terminate()
        return 130
    finally:
        stop.set()

    build_report(
        output_root=sweep.output_root,
        models_yml=sweep.models_yml,
        dataset_path=sweep.dataset if not args.limit else sweep._limited_dataset(),
        verbose=False,
    )

    log("\nsummary")
    for r in sorted(results, key=lambda row: row["version"]):
        log(f"  {r['version']:<32} {r['status']:<14} {r.get('duration_s', '?')}s")
    log(f"\nreports: {sweep.output_root}/score_vs_price.csv + .xlsx  |  per-task: {sweep.output_root}/benchmark.jsonl")
    log(f"run log: {sweep.output_root}/sweep.jsonl  |  shard logs: {sweep.output_root}/logs/eval")

    bad = [r for r in results if r["status"] != "ok"]
    if bad:
        log(f"\n{len(bad)} model(s) need attention; re-run the same command to resume.")
        return 1
    return 0


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def build_report(
    output_root: str | Path = "./outputs",
    models_yml: str | Path = "./models.yml",
    dataset_path: str | Path | None = "./data/WebTestBench/WebTestBench.jsonl",
    plot: bool = True,
    verbose: bool = True,
) -> List[dict]:
    """Build benchmark.jsonl + score-vs-price reports and return the per-model aggregates.

    Importable entry point (also used by `run_sweep`); only reads artifacts, so it is
    safe to call at any time, including mid-sweep.
    """
    output_root = Path(output_root)
    if not output_root.exists():
        raise SystemExit(f"output root not found: {output_root}")

    models = load_models(Path(models_yml))

    # gold item counts come from the dataset; without it, gold_items stays empty
    gold_counts: Dict[str, int] = {}
    total_tasks = None
    if dataset_path is not None and Path(dataset_path).exists():
        records = []
        for line in Path(dataset_path).read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    records.append(json.loads(line))
                except Exception:
                    continue
        total_tasks = len(records)
        gold_counts = {str(r.get("index", "")): len(r.get("checklist") or []) for r in records}

    jsonl_out = output_root / "benchmark.jsonl"
    csv_out = output_root / "score_vs_price.csv"
    xlsx_out = output_root / "score_vs_price.xlsx"
    plot_out = output_root / "score_vs_price.png"

    all_rows: List[dict] = []
    agg: List[dict] = []

    for version_dir in sorted(d for d in output_root.iterdir() if d.is_dir()):
        short = version_dir.name.split("claudecode-")[-1]
        model = models.get(short, {"key": short, "model_id": short})
        rows = []
        for task_dir in sorted(d for d in version_dir.iterdir() if d.is_dir()):
            row = collect_task(
                version_dir, task_dir, model,
                gold_items=gold_counts.get(task_dir.name)
            )
            if row:
                rows.append(row)
        if not rows:
            continue
        all_rows.extend(rows)
        agg.append(aggregate(version_dir.name, rows, model, total_tasks))

    # best F1 first (scored rows before unscored) so CSV, XLSX and console agree
    agg.sort(key=lambda r: (r["f1"] is None, -(r["f1"] or 0)))

    with jsonl_out.open("w", encoding="utf-8") as f:
        for row in all_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    write_csv(csv_out, agg)
    write_xlsx(xlsx_out, agg)

    if verbose:
        print(f"wrote {jsonl_out} ({len(all_rows)} rows), {csv_out}, {xlsx_out}")

    if plot and agg:
        plotted = maybe_plot(plot_out, agg)
        if verbose and plotted:
            print(f"plot: {plotted}")

    if verbose:
        for r in agg:
            print(f"{r['model']:<32} f1={fmt(r['f1'], 4):>7}  $/1M={fmt(r['usd_per_1m_blended'], 4):>8}"
                  f"  total$={fmt(r['cost_usd'], 4):>9}  tasks={r['tasks_scored']}"
                  f"  empty={r['tasks_empty']}  from_ckl={r['tasks_scored_from_checklist']}"
                  f"  items={r['pred_items_total']}/{r['gold_items_total']}")
    return agg


def main() -> int:
    args = parse_args()

    if args.run:
        return run_sweep(args)

    build_report(
        output_root=args.output_root,
        models_yml=ROOT / "models.yml",
        dataset_path=Path(args.data_root) / "WebTestBench.jsonl",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

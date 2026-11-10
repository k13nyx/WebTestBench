#!/usr/bin/env python3
"""Two figures for a finished WebTestBench sweep.

Read-only: consumes outputs/benchmark.jsonl (written by evaluate.py) and writes
two PNGs plus a CSV of the same numbers. It never modifies the benchmark code,
dataset or existing report files.

    python process/visualize_benchmark.py                  # both figures
    python process/visualize_benchmark.py --chart metrics  # overall metrics only
    python process/visualize_benchmark.py --chart effort   # effort and cost only

Figure 1, "Overall metrics per model": grouped bars of Reliability / Coverage /
Precision / Recall / F1, models sorted by F1, ranks 1-3 badged, #1 marked.

Figure 2, "Effort and cost per model": turns per task (min-max, middle 50%,
average) and average cost per task, same model order, three lowest badged.
"""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean, quantiles, stdev
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  (must follow matplotlib.use)
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402
from matplotlib.ticker import FuncFormatter, MaxNLocator  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FONTS = {"title": 13, "subtitle": 8.5, "axis": 9.5, "tick": 8.5, "note": 7, "legend": 9}
INK = {"title": "#111111", "body": "#333333", "note": "#777777"}

COLORS = {
    "reliability": "#8E9BAA",
    "coverage": "#4285F4",
    "precision": "#FF7043",
    "recall": "#2BB673",
    "f1": "#7E57C2",
    "whisker": "#8C9AA8",
    "box_fill": "#A9CBE8",
    "box_edge": "#5B8DB8",
    "turns_dot": "#1F3864",
    "cost_bar": "#D6A419",
    "cost_badge": "#B08207",
}

# (key, legend label, colour) -- the order the paper's Table 2 uses
METRICS: Tuple[Tuple[str, str, str], ...] = (
    ("reliability", "Reliability", COLORS["reliability"]),
    ("coverage", "Coverage (Cov.)", COLORS["coverage"]),
    ("precision", "Precision (P)", COLORS["precision"]),
    ("recall", "Recall (R)", COLORS["recall"]),
    ("f1", "F1", COLORS["f1"]),
)


# ----------------------------------------------------------------- aggregation
@dataclass
class Model:
    name: str
    tasks: int = 0
    failed: int = 0
    unscored: int = 0
    cost: float = 0.0
    scores: Dict[str, List[float]] = field(default_factory=lambda: {k: [] for k, _, _ in METRICS})
    turns: List[float] = field(default_factory=list)

    @property
    def usd_per_task(self) -> float:
        return self.cost / self.tasks if self.tasks else 0.0

    @property
    def turns_box(self) -> Optional[dict]:
        if not self.turns:
            return None
        q = quantiles(self.turns, n=4, method="inclusive") if len(self.turns) > 1 else [self.turns[0]] * 3
        return {
            "min": min(self.turns), "q1": q[0], "q3": q[2],
            "max": max(self.turns), "avg": mean(self.turns)
        }

    def ci95(self, key: str) -> float:
        values = self.scores[key]
        return 1.96 * stdev(values) / len(values) ** 0.5 if len(values) > 1 else 0.0

    def get(self, key: str) -> Optional[float]:
        """Metric mean, or one of the two derived keys: "turns" and "usd_per_task"."""
        if key == "usd_per_task":
            return self.usd_per_task

        if key == "turns":
            box = self.turns_box
            return box["avg"] if box else None

        values = self.scores.get(key) or []
        return mean(values) if values else None

    def label(self) -> str:
        return self.name + ("*" if self.unscored else "")


def load_rows(path: Path) -> List[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def summarize(rows: Iterable[dict], needle: str = "") -> List[Model]:
    """One Model per version, best F1 first."""
    buckets: Dict[str, Model] = {}
    for row in rows:
        version = str(row.get("version") or "")
        model = buckets.setdefault(
            version, Model((row.get("model") or version).split("/")[-1]))

        failed = row.get("status") != "has_result"
        scored = row.get("f1") is not None

        model.tasks += 1
        model.cost += row.get("cost_usd") or 0.0
        if failed:
            model.failed += 1
        elif not scored:
            model.unscored += 1  # produced a result but the scorer failed

        if not failed and row.get("num_turns") is not None:
            model.turns.append(float(row["num_turns"]))

        for key, _, _ in METRICS:
            if key == "reliability":  # derived: did the run return a result at all?
                value: Optional[float] = 0.0 if failed else 1.0
            else:
                value = row.get(key)
                if value is None and failed:
                    value = 0.0  # empty run with no score at all counts as 0

            if value is not None:
                model.scores[key].append(float(value))

    kept = [
        m for m in buckets.values()
        if not needle or needle.lower() in m.name.lower()
    ]
    return sorted(kept, key=lambda m: (m.get("f1") is None, -(m.get("f1") or 0.0)))


# -------------------------------------------------------------------- ranking
def ranked(models: Sequence[Model], key: str, lowest: bool = False) -> List[Tuple[int, Model]]:
    """Competition ranking: equal values share a rank, so a 6-way tie at #1 makes the
    next distinct value #7 (not #2)."""
    present = [m for m in models if m.get(key) is not None]
    ahead = (lambda a, b: a < b) if lowest else (lambda a, b: a > b)
    return [(1 + sum(ahead(o.get(key), m.get(key)) for o in present), m) for m in present]


def leaderboard(
    models: Sequence[Model],
    key: str,
    size: int = 3,
    lowest: bool = False
) -> List[Tuple[int, List[Model], float]]:
    """Ranks 1..size as (rank, tied models, value); ties collapse into one row."""
    ranks = ranked(models, key, lowest)
    board = []

    for rank in range(1, size + 1):
        group = [m for r, m in ranks if r == rank]
        if group:
            board.append((rank, group, group[0].get(key)))
    return board


def badge_ranks(
    models: Sequence[Model],
    key: str,
    size: int = 3,
    lowest: bool = False
) -> Dict[str, int]:
    """{model name: rank} for the models that made the top `size`."""
    return {m.name: r for r, m in ranked(models, key, lowest) if r <= size}


# ------------------------------------------------------------- draw primitives
def badge(ax, x: float, y: float, rank: int, color: str, size: float = 150) -> None:
    """A filled circle with a white rank numeral."""
    ax.scatter([x], [y], s=size, color=color, edgecolors="white", linewidths=0.8, zorder=6)
    ax.annotate(
        str(rank), (x, y),
        ha="center", va="center", fontsize=7.5, color="white", fontweight="bold", zorder=7
    )


def dotted(ax, value: float, color: str, axis: str = "y") -> None:
    drawer = ax.axhline if axis == "y" else ax.axvline
    drawer(value, color=color, linewidth=1.0, linestyle=(0, (2, 2)), zorder=1)


def text_block(fig, x: float, top: float, lines: Sequence[Tuple[str, str, float, str]], step: float = 0.034) -> None:
    """Left-aligned lines of (text, colour, size, weight), flowing downward from `top`."""
    for i, (text, color, size, weight) in enumerate(lines):
        fig.text(x, top - i * step, text, fontsize=size, color=color, weight=weight, va="top")


def header(fig, title: str, subtitle: str) -> None:
    fig.suptitle(title, x=0.035, ha="left", fontsize=FONTS["title"], weight="bold", y=0.965)
    fig.text(0.035, 0.905, subtitle, fontsize=FONTS["subtitle"], color=INK["body"])


def footnote(fig, note: str) -> None:
    fig.text(0.035, 0.015, note, fontsize=FONTS["note"], color=INK["note"])


def common_subtitle(models: Sequence[Model]) -> str:
    return (f"WebTestBench · {len(models)} models × {max(m.tasks for m in models)} tasks")


RELIABILITY = "reliability = (runs − failed runs) / runs"


def unscored_note(models: Sequence[Model]) -> str:
    bad = [m for m in models if m.unscored]
    if not bad:
        return "All runs scored."
    return "; ".join(
        f"*{m.name}: {m.unscored} of {m.tasks} runs unscored (scorer error), "
        f"mean over {m.tasks - m.unscored - m.failed}" for m in bad
    )


# --------------------------------------------- figure 1: overall scores ---------------
def panel_metrics(ax, models: Sequence[Model]) -> None:
    width, slots = 0.16, range(len(models))
    for i, (key, label, color) in enumerate(METRICS):
        heights = [100 * (m.get(key) or 0.0) for m in models]
        ax.bar(
            [x + (i - 2) * width for x in slots], heights, width,
            label=label, color=color, edgecolor="white", linewidth=0.4, zorder=3
        )

    peak = max(100 * (m.get(key) or 0.0) for m in models for key, _, _ in METRICS)
    ax.set_ylim(0, peak * 1.14)
    headroom = peak * 0.022

    for i, (key, _, color) in enumerate(METRICS):
        board = leaderboard(models, key)
        if not board:  # nothing scored on this metric yet
            continue
        top_value = board[0][2] * 100
        dotted(ax, top_value, color)
        ax.annotate(
            f"{top_value:.1f}", (1.0, top_value),
            xycoords=("axes fraction", "data"), xytext=(5, 0), textcoords="offset points",
            va="center", fontsize=8.5, color=color, weight="bold"
        )

        badges = badge_ranks(models, key)
        for x, m in enumerate(models):
            if m.name in badges:
                badge(ax, x + (i - 2) * width, 100 * (m.get(key) or 0.0) + headroom, badges[m.name], color)

    ax.set_xticks(list(slots))
    ax.set_xticklabels([m.label() for m in models], rotation=28, ha="right", fontsize=FONTS["tick"])
    ax.set_xlim(-0.7, len(models) - 0.3)
    ax.set_ylabel("Score (%)", fontsize=FONTS["axis"])
    ax.grid(axis="y", alpha=0.3, zorder=0)
    ax.legend(
        handles=[Patch(facecolor=c, label=label) for _, label, c in METRICS],
        loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=5, frameon=False,
        fontsize=FONTS["legend"]
    )


def metrics_figure(models: Sequence[Model]):
    fig = plt.figure(figsize=(18, 7.6))
    panel_metrics(fig.add_axes([0.05, 0.14, 0.665, 0.62]), models)

    lines = [("Top 3 per metric", INK["title"], 10.5, "bold")]
    for key, label, color in METRICS:
        lines.append(("", INK["body"], 4, "normal"))
        lines.append((label, color, 9, "bold"))
        for rank, group, value in leaderboard(models, key):
            who = f"{len(group)} models tied" if len(group) > 1 else group[0].label()
            lines.append((f"{rank}. {who} ({value * 100:.1f})", INK["body"], 8.5, "normal"))

    if len(lines) == 1:  # nothing scored yet: say so instead of an empty panel
        lines.append(("no scored runs yet", INK["note"], 8.5, "normal"))

    text_block(fig, 0.765, 0.80, lines, step=0.0295)

    header(
        fig, "Overall metrics per model",
        common_subtitle(models) + " · models sorted by F1 (best left) · higher is better · "
        "numbered badge = rank 1-3 on that metric, dotted line = #1 · " + RELIABILITY
    )
    footnote(
        fig, "Failed (empty) runs count as 0 on every metric. Ties share a rank. "
        + unscored_note(models)
    )
    return fig


# --------------------------------------------- figure 2: effort + cost ---------------
def panel_turns(ax, models: Sequence[Model]) -> None:
    badges = badge_ranks(models, "turns", lowest=True)
    best = min((m.turns_box["avg"] for m in models if m.turns_box), default=0.0)
    dotted(ax, best, COLORS["turns_dot"], axis="x")

    for y, m in enumerate(models):
        box = m.turns_box
        if not box:
            continue

        ax.plot(
            [box["min"], box["max"]], [y, y],
            color=COLORS["whisker"], linewidth=1.0, zorder=2
        )

        for edge in (box["min"], box["max"]):
            ax.plot(
                [edge, edge], [y - 0.12, y + 0.12],
                color=COLORS["whisker"], linewidth=1.0, zorder=2
            )

        ax.add_patch(Rectangle(
            (box["q1"], y - 0.2), box["q3"] - box["q1"], 0.4,
            facecolor=COLORS["box_fill"], edgecolor=COLORS["box_edge"], linewidth=0.9, zorder=3
        ))

        if m.name in badges:
            badge(ax, box["avg"], y, badges[m.name], COLORS["turns_dot"], size=130)
        else:
            ax.scatter(box["avg"], y, s=26, color=COLORS["turns_dot"], zorder=4)

        ax.annotate(
            f"avg {box['avg']:.0f}  ({box['min']:.0f}-{box['max']:.0f})", (box["max"], y),
            textcoords="offset points", xytext=(7, -3), fontsize=7
        )

    span = max((m.turns_box["max"] for m in models if m.turns_box), default=100)
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels([m.label() for m in models], fontsize=FONTS["tick"])
    ax.invert_yaxis()
    ax.set_xlim(0, span * 1.28)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=8))
    ax.set_xlabel("Turns per task (completed runs)", fontsize=FONTS["axis"])
    ax.set_title("Turns per task  ·  ← fewer is better", loc="left", fontsize=10.5)
    ax.grid(axis="x", alpha=0.3)


def panel_cost(ax, models: Sequence[Model]) -> None:
    badges = badge_ranks(models, "usd_per_task", lowest=True)
    longest = max(m.usd_per_task for m in models) or 1.0
    pad = longest * 0.018
    dotted(ax, min(m.usd_per_task for m in models), COLORS["cost_bar"], axis="x")

    for y, m in enumerate(models):
        ax.barh(
            y, m.usd_per_task,
            height=0.55, color=COLORS["cost_bar"], edgecolor="white", linewidth=0.4, zorder=3
        )

        shift = pad if m.name in badges else 0.0
        if m.name in badges:
            badge(ax, m.usd_per_task + pad, y, badges[m.name], COLORS["cost_bar"], size=130)

        ax.annotate(
            f"${m.usd_per_task:.3f}", (m.usd_per_task + 2 * shift, y),
            textcoords="offset points", xytext=(7, -3), fontsize=7.5
        )

    ax.set_yticks([])
    ax.invert_yaxis()
    ax.set_xlim(0, longest * 1.2)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:.2f}"))
    ax.set_xlabel("Average cost per task (USD)", fontsize=FONTS["axis"])
    ax.set_title("Average cost per task  ·  ← cheaper is better", loc="left", fontsize=10.5)
    ax.grid(axis="x", alpha=0.3)

    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)


def effort_figure(models: Sequence[Model]):
    fig = plt.figure(figsize=(18, 7.6))
    panel_turns(fig.add_axes([0.115, 0.19, 0.33, 0.60]), models)
    panel_cost(fig.add_axes([0.545, 0.19, 0.245, 0.60]), models)

    lines = [("Top 3 (lowest)", INK["title"], 10.5, "bold")]
    for key, title, color, fmt in (
        ("turns", "Fewest average turns", COLORS["turns_dot"], "{:.0f}"),
        ("usd_per_task", "Cheapest per task", COLORS["cost_badge"], "${:.3f}")
    ):
        lines.append((title, color, 9, "bold"))
        for rank, group, value in leaderboard(models, key, lowest=True):
            who = f"{len(group)} models tied" if len(group) > 1 else group[0].label()
            lines.append((f"{rank}. {who} ({fmt.format(value)})", INK["body"], 8.5, "normal"))
    
    text_block(fig, 0.825, 0.78, lines, step=0.033)

    fig.legend(
        handles=[
            Line2D(
                [], [],
                color=COLORS["whisker"], marker="|", ms=8, lw=1.0, label="min - max"
            ),
            Patch(facecolor=COLORS["box_fill"], edgecolor=COLORS["box_edge"], label="Q1 - Q3 (middle 50% of tasks)"),
            Line2D(
                [], [],
                marker="o", color="none", markerfacecolor=COLORS["turns_dot"], markeredgecolor="none",
                ms=7, label="average (numbered if top 3)"
            ),
            Line2D(
                [], [],
                color=COLORS["cost_bar"], lw=1.0, ls=(0, (2, 2)), label="dotted line = #1 (lowest)"
            ),
        ],
        loc="lower center", bbox_to_anchor=(0.5, 0.045), ncol=4, frameon=False, fontsize=FONTS["legend"]
    )

    header(fig, "Effort and cost per model",
           common_subtitle(models) + " · models in F1 order (best at top), same as the metrics chart · "
           "numbered badge = rank 1–3 · " + RELIABILITY)
    footnote(fig, "Turns: crashed runs (no result) left out, so they don't fake a 0-turn minimum.  "
                  "Cost: average over all runs, from the price table, after cache discounts.")
    return fig


# ------------------------------------------------------------------- csv table
# one row per model; metric means are fractions in [0, 1] (the charts show %)
CSV_COLUMNS: Tuple[str, ...] = (
    "model", "tasks", "failed", "unscored", "reliability", "coverage", "precision",
    "recall", "f1", "f1_ci95", "turns_min", "turns_q1", "turns_avg", "turns_q3",
    "turns_max", "cost_usd", "usd_per_task",
)


def csv_row(model: Model) -> dict:
    """One flat record; missing values stay empty rather than becoming 0."""
    row = {
        "model": model.name,
        "tasks": model.tasks,
        "failed": model.failed,
        "unscored": model.unscored,
        "f1_ci95": round(model.ci95("f1"), 4),
        "cost_usd": round(model.cost, 6),
        "usd_per_task": round(model.usd_per_task, 6),
    }
    for key, _, _ in METRICS:
        value = model.get(key)
        if value is not None:
            row[key] = round(value, 4)
    for name, value in (model.turns_box or {}).items():
        row[f"turns_{name}"] = round(value, 2)
    return row


def write_csv(path: Path, models: Sequence[Model]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(csv_row(m) for m in models)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output-root", default=str(ROOT / "outputs"), help="directory holding benchmark.jsonl")
    parser.add_argument("--out", default=None, help="write the selected figure / the CSV here (ignored with --chart both)")
    parser.add_argument("--filter", default="", help="only models whose name contains this text")
    parser.add_argument("--chart", choices=("both", "metrics", "effort"), default="both")
    return parser.parse_args()


FIGURES: Dict[str, Tuple[str, Callable]] = {
    "metrics": ("overall_scores.png", metrics_figure),
    "effort": ("effort_cost.png", effort_figure),
}
TABLE = "overall_metrics.csv"


def main() -> int:
    args = parse_args()
    source = Path(args.output_root) / "benchmark.jsonl"
    if not source.exists():
        raise SystemExit(f"{source} not found; run `python evaluate.py` first")

    models = summarize(load_rows(source), args.filter)
    if not models:
        raise SystemExit("no rows to plot")

    selected = FIGURES.values() if args.chart == "both" else [FIGURES[args.chart]]
    for name, build in selected:
        path = Path(args.out) if args.out and args.chart != "both" else source.parent / name
        fig = build(models)
        fig.savefig(str(path), dpi=160)
        plt.close(fig)
        print(f"wrote {path}")

    table = Path(args.out).with_suffix(".csv") if args.out and args.chart != "both" else source.parent / TABLE
    write_csv(table, models)
    print(f"wrote {table}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

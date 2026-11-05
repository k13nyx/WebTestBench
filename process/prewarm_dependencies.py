#!/usr/bin/env python3
"""Install dependencies once per project, ahead of a (parallel) eval run.

Each task runs `npm install` inside its own project directory, and a cold install
is the slowest part of `server_deploy`: seconds when one shard runs, tens of
seconds when every shard does it at once on the same drive. Doing it here
sequentially makes the later `npm install` a no-op and only costs anything once.

`--optimize` additionally pre-bundles Vite deps. It is off by default because it
was measured not to help: on Vite 5.4 the dev server ignores that cache and
re-optimizes ("Re-optimizing dependencies because lockfile has changed"), so the
work is simply done twice.

Examples:
    python process/prewarm_dependencies.py
    python process/prewarm_dependencies.py --project_root ./outputs/work/my-version
    python process/prewarm_dependencies.py --only WebTestBench_0001,WebTestBench_0014
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

DEFAULT_PROJECT_ROOT = Path("./data/WebTestBench/web_applications")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--project_root", type=Path, default=DEFAULT_PROJECT_ROOT,
        help=f"Directory holding one sub-directory per project (default: {DEFAULT_PROJECT_ROOT}).",
    )
    parser.add_argument(
        "--only", type=str, default=None,
        help="Comma-separated project directory names to warm (default: all).",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-run npm install even when node_modules already exists.",
    )
    parser.add_argument(
        "--optimize", action="store_true",
        help="Also run `vite optimize` (usually pointless: `vite dev` re-does it, see module docstring).",
    )
    parser.add_argument(
        "--skip_install", action="store_true",
        help="Do not run npm install; only pre-bundle with the existing node_modules.",
    )
    parser.add_argument(
        "--timeout", type=float, default=900.0,
        help="Seconds allowed per command (default: 900).",
    )
    return parser.parse_args()


def dev_script(project_dir: Path) -> str:
    """`scripts.dev` from package.json, or '' when it cannot be read."""
    try:
        package = json.loads((project_dir / "package.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ""
    return str((package.get("scripts") or {}).get("dev", "") or "")


def run(cmd: list[str], cwd: Path, timeout: float) -> tuple[int, float, str]:
    """Run a command, returning (exit_code, seconds, output_tail)."""
    started = time.time()
    try:
        # start_new_session makes the child a process-group leader, so a timeout can
        # take down its children too (npm spawns node, which spawns esbuild/tsc).
        proc = subprocess.Popen(
            cmd, cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors="replace", start_new_session=True,
        )
    except Exception as exc:  # missing executable and friends
        return 127, round(time.time() - started, 1), f"{type(exc).__name__}: {exc}"

    try:
        output, _ = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        try:
            subprocess.run(f"kill -9 -{proc.pid}", shell=True, capture_output=True)
        except Exception:
            proc.kill()
        try:
            proc.communicate(timeout=10)
        except Exception:
            pass
        return 124, round(time.time() - started, 1), f"timed out after {timeout:.0f}s"

    tail = "\n".join((output or "").strip().splitlines()[-5:])
    return proc.returncode, round(time.time() - started, 1), tail


def warm_project(project_dir: Path, args: argparse.Namespace) -> str:
    """Warm one project. Returns 'cached', 'warmed' or 'failed'."""
    has_node_modules = (project_dir / "node_modules").is_dir()
    needs_install = args.force or not has_node_modules
    uses_vite = "vite" in dev_script(project_dir).lower()
    has_cache = (project_dir / "node_modules" / ".vite" / "deps").exists()
    needs_optimize = args.optimize and uses_vite and (args.force or not has_cache)

    if not needs_install and not needs_optimize:
        print("  already warm")
        return "cached"

    if needs_install:
        if args.skip_install:
            print("  node_modules missing and --skip_install was given; nothing to do")
            return "failed"
        code, seconds, tail = run(["npm", "install"], project_dir, args.timeout)
        print(f"  npm install: exit {code} in {seconds}s")
        if code != 0:
            print(f"  {tail}")
            return "failed"

    if needs_optimize:
        if not (project_dir / "node_modules").is_dir():
            print("  node_modules missing; cannot pre-bundle")
            return "failed"
        code, seconds, tail = run(["npx", "--no-install", "vite", "optimize"], project_dir, args.timeout)
        print(f"  vite optimize: exit {code} in {seconds}s")
        if code != 0:
            print(f"  {tail}")
            return "failed"

    return "warmed"


def main() -> None:
    args = parse_args()

    root: Path = args.project_root
    if not root.is_dir():
        raise FileNotFoundError(f"project root not found: {root}")

    wanted = {item.strip() for item in (args.only or "").split(",") if item.strip()}
    projects = sorted(
        p for p in root.iterdir() if p.is_dir() and (p / "package.json").exists()
    )
    if wanted:
        projects = [p for p in projects if p.name in wanted]

    if not projects:
        print(f"No projects found in {root}" + (f" matching {sorted(wanted)}" if wanted else ""))
        if wanted:
            raise SystemExit(1)  # a typo in --only should not look like success
        return

    print(f"Root: {root}")
    print(f"Projects: {len(projects)}")
    print("Running one project at a time on purpose: parallel installs are what saturates the disk.")

    counts = {"cached": 0, "warmed": 0, "failed": 0}
    failures: list[str] = []
    started = time.time()

    for i, project_dir in enumerate(projects, start=1):
        print(f"[{i}/{len(projects)}] {project_dir.name}")
        status = warm_project(project_dir, args)
        counts[status] += 1
        if status == "failed":
            failures.append(project_dir.name)

    print(
        f"Done in {time.time() - started:.0f}s: "
        f"{counts['warmed']} warmed, {counts['cached']} already cached, {counts['failed']} failed"
    )
    if failures:
        print("Failed projects: " + ", ".join(failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Download the WebTestBench dataset from Hugging Face.

Output:
    data/WebTestBench/WebTestBench.jsonl          # 100 task records (gold checklists)
    data/WebTestBench/web_applications_zip/*.zip  # one zip per web application
    data/WebTestBench/web_applications/           # only with --unzip

Usage:
    python process/download_dataset.py                   # jsonl + 100 zips (~23 MB)
    python process/download_dataset.py --unzip           # ... and extract the apps
    python process/download_dataset.py --skip-apps       # jsonl only (quick check)
    HF_TOKEN=hf_... python process/download_dataset.py   # if you hit rate limits

Already-downloaded files are skipped (unless --force), so re-running is cheap.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

REPO = "friedrichor/WebTestBench"
API_URL = f"https://huggingface.co/api/datasets/{REPO}"
RESOLVE_URL = f"https://huggingface.co/datasets/{REPO}/resolve/main/{{path}}"
JSONL_NAME = "WebTestBench.jsonl"
APPS_DIR = "web_applications_zip"
TOKEN = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN") or ""
HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset-dir", default="./data/WebTestBench", help="destination directory (default ./data/WebTestBench)")
    parser.add_argument("--jobs", type=int, default=4, help="parallel downloads (default 4)")
    parser.add_argument("--skip-apps", action="store_true", help="only fetch WebTestBench.jsonl")
    parser.add_argument("--unzip", action="store_true", help="run process/unzip_web_applications.py afterwards")
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    return parser.parse_args()


def repo_zips() -> list[str]:
    """Paths of the app archives inside the dataset repository."""
    resp = requests.get(API_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    names = [item["rfilename"] for item in resp.json().get("siblings") or []]
    return [n for n in names if n.startswith(f"{APPS_DIR}/") and n.endswith(".zip")]


def fetch(repo_path: str, dest: Path, force: bool) -> str:
    """Download one file atomically. Returns 'ok' or 'skip'; raises on HTTP errors."""
    if dest.exists() and dest.stat().st_size and not force:
        return "skip"

    tmp = dest.with_suffix(dest.suffix + ".part")
    tmp.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(RESOLVE_URL.format(path=repo_path), headers=HEADERS, stream=True, timeout=120) as response:
        response.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in response.iter_content(1 << 20):
                fh.write(chunk)

    tmp.replace(dest)
    return "ok"


def main() -> int:
    args = parse_args()
    out_dir = Path(args.dataset_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Only ask the API for the zip list when the apps are actually wanted.
    targets = [(JSONL_NAME, out_dir / JSONL_NAME)]
    if not args.skip_apps:
        try:
            targets += [(p, out_dir / APPS_DIR / Path(p).name) for p in repo_zips()]
        except Exception as exc:
            print(f"failed to list dataset files: {exc}", file=sys.stderr)
            return 1

    print(f"{REPO} -> {out_dir.resolve()}  ({len(targets)} file(s))\n")

    def run(target: tuple[str, Path]) -> tuple[str, str]:
        try:
            return target[0], fetch(target[0], target[1], args.force)
        except Exception as exc:
            return target[0], f"FAILED: {exc}"

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        results = list(pool.map(run, targets))

    failed = [(path, status) for path, status in results if status.startswith("FAILED")]
    downloaded = sum(status == "ok" for _, status in results)

    print(f"downloaded {downloaded}, skipped {len(results) - downloaded - len(failed)}, failed {len(failed)}")

    for path, status in failed:
        print(f"  {path}: {status}", file=sys.stderr)

    if args.unzip:
        script = Path(__file__).resolve().parent / "unzip_web_applications.py"
        print(f"\nunzipping via {script.name} ...")
        rc = subprocess.call([sys.executable, str(script)], cwd=str(script.parent.parent))
        if rc:
            print(f"unzip failed (exit {rc})", file=sys.stderr)
            return rc

    if failed:
        print(f"\n{len(failed)} file(s) failed; re-run to retry", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

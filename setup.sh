#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"
ROOT_DIR="$(pwd)"

DATASET_DIR="$ROOT_DIR/data/WebTestBench"
DATASET_FILE="$DATASET_DIR/WebTestBench.jsonl"
DATASET_ZIPS_DIR="$DATASET_DIR/web_applications_zip"
DATASET_APPS_DIR="$DATASET_DIR/web_applications"

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    PYTHON_BIN="python"
fi
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    echo "error: neither python3 nor python is on PATH" >&2
    exit 1
fi

# Count real archives and app directories instead of listing directory entries,
# so stray dotfiles (.DS_Store) cannot masquerade as a downloaded dataset.
count_zips() {
    local count=0 path
    for path in "$DATASET_ZIPS_DIR"/*.zip; do
        if [ -e "$path" ]; then
            count=$((count + 1))
        fi
    done
    echo "$count"
}

count_apps() {
    local count=0 path
    for path in "$DATASET_APPS_DIR"/*/; do
        if [ -d "$path" ]; then
            count=$((count + 1))
        fi
    done
    echo "$count"
}

zip_count="$(count_zips)"

downloaded=false
if [ ! -f "$DATASET_FILE" ] || [ "$zip_count" -eq 0 ]; then
    echo "Dataset not found; downloading from Hugging Face..."
    "$PYTHON_BIN" process/download_dataset.py
    downloaded=true
    zip_count="$(count_zips)"
fi

# Extract after a fresh download, and also repair an incomplete extraction.
# unzip_web_applications.py skips apps that are already present, so re-running
# it only fills in what is missing.
if [ "$downloaded" = true ] || [ "$(count_apps)" -lt "$zip_count" ]; then
    echo "Unzipping web applications..."
    "$PYTHON_BIN" process/unzip_web_applications.py
else
    echo "Web applications already extracted; skipping unzip."
fi

echo "Refreshing model prices..."
"$PYTHON_BIN" process/refresh_prices.py

#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

# ======================================================================
MODELS=all
JOBS=10            # dataset shards per model (same idea as scripts/run_webtester_cc_parallel.sh JOBS)
# ======================================================================
python evaluate.py \
    --run \
    --models "$MODELS" \
    --jobs "$JOBS" \
    "$@"

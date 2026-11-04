#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

# ======================================================================
MODELS=all
PARALLEL_MODELS=2
# ======================================================================
python evaluate.py \
    --run \
    --models $MODELS \
    --parallel-models $PARALLEL_MODELS \
    "$@"

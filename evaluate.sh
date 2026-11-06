#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

# ======================================================================
MODELS=all
JOBS=10            # dataset shards per model (same idea as scripts/run_webtester_cc_parallel.sh JOBS)

# The dev server listens on 0.0.0.0 (all network interfaces).
# The agent's browser opens localhost.
export WEBTESTBENCH_BIND_HOST=0.0.0.0
export WEBTESTBENCH_CONNECT_HOST=localhost
# export WEBTESTBENCH_CONNECT_HOST=host.docker.internal
# ======================================================================
python evaluate.py \
    --run \
    --models "$MODELS" \
    --jobs "$JOBS" \
    "$@"

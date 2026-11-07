#!/bin/bash
# Run the full sweep: evaluate every model in models.yml, then score the runs.
#
#   ./evaluate.sh [options]             every option is forwarded to evaluate.py
#
# Prerequisites, once per checkout:
#   pip install -r requirements.txt
#   ./setup.sh                          download & unzip dataset + check latest model prices
#
# Options worth knowing first:
#   --limit N       Run only the first N tasks of WebTestBench.jsonl in file order
#                   (not random sample);
#                   Sharding, --prewarm, scoring and the final report all shrink to those N tasks
#
#   --prewarm       Run `npm install` once per project, sequentially, before the
#                   sweep starts. Every task installs inside its own project during
#                   deployment anyway, but doing it up front avoids several cold
#                   installs competing for the disk, which is what fails on a slow
#                   or nearly full machine. It is idempotent, and with --limit it
#                   only warms the projects in scope.
#
#   --models        models.yml keys to run, comma separated (default: 'all').
#   --skip-models   models.yml keys to exclude.
#   --only MODE     'all' = eval + scoring,
#                   'eval' = skip scoring,
#                   'score' = rescore existing outputs without re-running agents.
#   --dry-run       Print the plan (models, tasks, jobs) and run nothing.
set -euo pipefail
cd "$(dirname "$0")"

# ======================================================================
# N shards => N concurrent agent sessions;
# Keeps bursts near OpenRouter's ceiling (max. ~1,000 req/day).
JOBS=4
MODELS=all

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

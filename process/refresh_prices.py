#!/usr/bin/env python3
"""Update the price fields in models.yml from OpenRouter's public model list.

Claude Code's own total_cost_usd cannot be used for this benchmark: it prices
every model with Anthropic's rate cards, so a cheap third-party model gets billed
at Opus rates. These values are the rates OpenRouter actually applies.

    python process/refresh_prices.py            # update models.yml
    python process/refresh_prices.py --dry-run  # show what would change

The file is edited through a ruamel round-trip, so comments, key order, quoting
and CRLF line endings all survive: an up-to-date file produces a zero-byte diff.
"""
import argparse
import json
import urllib.request
from io import StringIO
from pathlib import Path

try:
    from ruamel.yaml import YAML
except ImportError:  # pragma: no cover - dependency hint
    raise SystemExit("requires ruamel.yaml: pip install ruamel.yaml")

YML = Path(__file__).resolve().parent.parent / "models.yml"
API = "https://openrouter.ai/api/v1/models"

# models.yml key -> OpenRouter pricing key (USD per token)
FIELDS = {
    "price_in": "prompt",
    "price_out": "completion",
    "price_cache_read": "input_cache_read",
    "price_cache_write": "input_cache_write",
}


def live_prices() -> dict:
    with urllib.request.urlopen(API, timeout=60) as response:
        return {model["id"]: model["pricing"] for model in json.load(response)["data"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="report changes, write nothing")
    args = parser.parse_args()

    live = live_prices()
    text = YML.read_bytes().decode("utf-8")
    crlf = "\r\n" in text

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    doc = yaml.load(text) or {}

    changed = 0
    missing = []
    models = doc.get("models") or {}
    if not models:
        raise SystemExit(f"no models in {YML}; refusing to rewrite it")

    for key, cfg in models.items():
        pricing = live.get(cfg.get("model_id")) or {}

        for field, source in FIELDS.items():
            if source not in pricing:
                continue  # OpenRouter does not price it; leave the file alone

            value = round(float(pricing[source]) * 1_000_000, 4)
            current = cfg.get(field)
            if current is None:
                # Adding a key would restructure the block, so say so instead.
                missing.append(f"{key}.{field}")
                continue

            if abs(float(current) - value) < 1e-9:
                continue  # unchanged: keep the original formatting

            cfg[field] = value
            changed += 1

            print(f"  {key}.{field}: {current} -> {value}")

    if missing:
        print(
            "note: models.yml has no field for "
            + ", ".join(missing)
            + ". This script only rewrites existing values; add it manually."
        )

    if args.dry_run:
        print(f"dry run: {changed} value(s) would change")
        return

    buffer = StringIO()
    yaml.dump(doc, buffer)
    output = buffer.getvalue()
    if crlf:  # ruamel emits LF; the repo file is CRLF
        output = output.replace("\r\n", "\n").replace("\n", "\r\n")
    YML.write_bytes(output.encode("utf-8"))

    print(f"models.yml updated ({changed} value(s))")


if __name__ == "__main__":
    main()

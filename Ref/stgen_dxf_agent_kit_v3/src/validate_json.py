"""
JSON Schema Validator CLI

Usage:
  python src/validate_json.py --schema schemas/design_input_v3.schema.json --json examples/design_input_demo.json
"""

from __future__ import annotations

import argparse
import json
from jsonschema import Draft202012Validator


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    schema = load_json(args.schema)
    data = load_json(args.json)

    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)

    if errors:
        print("INVALID")
        for e in errors[:50]:
            path = ".".join([str(p) for p in e.path])
            print(f"- {path}: {e.message}")
        return 2

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

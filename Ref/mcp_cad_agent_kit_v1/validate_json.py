"""
validate_json.py
- design_input / drafting_plan JSON schema 검증 도구

사용:
  python validate_json.py --schema schemas/design_input_v1.schema.json --json examples/design_input_demo.json
  python validate_json.py --schema schemas/drafting_plan_v1.schema.json --json examples/drafting_plan_demo_A101_expanded.json
"""

import argparse, json
from pathlib import Path
import jsonschema

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    data = json.loads(Path(args.json).read_text(encoding="utf-8"))

    try:
        jsonschema.validate(instance=data, schema=schema)
        print("OK: schema validation passed")
    except jsonschema.ValidationError as e:
        print("FAIL:", e.message)
        print("PATH:", list(e.absolute_path))
        raise SystemExit(2)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
plan_validator.py

- JSON Schema 검증 + 추가 규칙 점검(휴리스틱)
- 사용: python src/plan_validator.py path/to/plan.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

try:
    import jsonschema
except ImportError:
    jsonschema = None


def load_json(p: str) -> Any:
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_schema(plan: Dict[str, Any], schema_path: str) -> List[str]:
    issues: List[str] = []
    if jsonschema is None:
        issues.append("WARNING: jsonschema not installed; schema validation skipped")
        return issues
    schema = load_json(schema_path)
    try:
        jsonschema.validate(plan, schema)
    except Exception as e:
        issues.append(f"SCHEMA_ERROR: {e}")
    return issues


def validate_rules(plan: Dict[str, Any]) -> List[str]:
    issues: List[str] = []
    steps = plan.get("steps", [])
    ids: Set[str] = set()

    # unique ids
    for st in steps:
        sid = st.get("id")
        if not sid:
            issues.append("RULE_ERROR: step without id")
            continue
        if sid in ids:
            issues.append(f"RULE_ERROR: duplicate step id: {sid}")
        ids.add(sid)

    # layers should be created early
    first_create_idx = None
    first_layer_idx = None
    for i, st in enumerate(steps):
        tool = st.get("tool")
        macro = st.get("macro")
        if first_layer_idx is None and (tool == "create_layer" or macro == "macro:setup_layers"):
            first_layer_idx = i
        if first_create_idx is None and (tool and tool.startswith("create_")):
            first_create_idx = i
    if first_create_idx is not None and (first_layer_idx is None or first_layer_idx > first_create_idx):
        issues.append("RULE_WARN: entities are created before layers are set up (recommend macro:setup_layers at start)")

    # discourage scaling unless explicitly marked
    for st in steps:
        tool = st.get("tool")
        if tool in ("scale_entities", "scale_region"):
            reason = (st.get("args") or {}).get("reason") or ""
            if "sheet" not in str(reason).lower():
                issues.append(f"RULE_WARN: {tool} used without reason='sheet_*' in args (step {st['id']})")

    # save_dxf should be near end
    save_positions = [i for i, st in enumerate(steps) if st.get("tool") == "save_dxf"]
    if save_positions and save_positions[-1] < len(steps) - 3:
        issues.append("RULE_WARN: save_dxf is not near the end of the plan (recommend last 1~2 steps)")

    return issues


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: plan_validator.py plan.json [schema.json]", file=sys.stderr)
        sys.exit(2)

    plan_path = sys.argv[1]
    schema_path = sys.argv[2] if len(sys.argv) >= 3 else str(Path(__file__).resolve().parent.parent / "schemas" / "drafting_plan_stgen_v1.schema.json")
    plan = load_json(plan_path)

    issues = []
    issues += validate_schema(plan, schema_path)
    issues += validate_rules(plan)

    if issues:
        print("\n".join(issues))
        # schema error 있으면 비정상 종료
        if any(x.startswith("SCHEMA_ERROR") for x in issues):
            sys.exit(1)
    else:
        print("OK")


if __name__ == "__main__":
    main()

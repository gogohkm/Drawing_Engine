"""
Plan Validator / Linter (Sample)

- JSON Schema 검증은 별도 CLI(validate_json.py)로 수행하는 것을 권장.
- 여기서는 "빠른 린트" 위주로:
  - scale tool 사용 경고
  - assign 변수명 형식
  - 알려진 tool 목록 외 사용 여부(스키마에서 이미 막지만, 스키마 미사용 시)

"""

from __future__ import annotations

from typing import Any, Dict, List


SCALE_TOOLS = {"scale_entities", "scale_region"}


def lint_plan_quick(plan: Dict[str, Any]) -> None:
    if not isinstance(plan, dict):
        return

    policy = plan.get("policy") or {}
    avoid_scale = policy.get("avoid_scale", True)
    forbid_tools = set(policy.get("forbid_tools") or [])

    seq: List[Dict[str, Any]] = plan.get("sequence") or []
    for step in seq:
        if not isinstance(step, dict):
            continue
        if "tool" in step:
            tool = step.get("tool")
            if avoid_scale and tool in SCALE_TOOLS:
                print(f"[LINT][WARN] scale tool used: step={step.get('id')} tool={tool}")
            if tool in forbid_tools:
                print(f"[LINT][ERROR] forbidden tool used: step={step.get('id')} tool={tool}")

            assign = step.get("assign")
            if assign is not None and not (isinstance(assign, str) and assign.startswith("$")):
                print(f"[LINT][WARN] assign should start with '$': step={step.get('id')} assign={assign}")

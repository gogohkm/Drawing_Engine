"""
stgen-dxf-viewer Drafting Plan Executor (Sample)

- 입력: drafting_plan(JSON)
- 처리:
  1) macro 단계 전개(macro_library)
  2) 변수 치환($var)
  3) args_map에 따라 canonical args -> 실제 MCP args 변환(args_adapter)
  4) MCP tool call 순차 실행

이 파일은 '샘플'입니다.
실제 MCP 호출은 McpClient.call()을 당신 orchestrator에 맞춰 구현하세요.
"""

from __future__ import annotations

import argparse
import json
import copy
import sys
from typing import Any, Dict, List, Optional, Union

from args_adapter import ArgsAdapter
from macro_library import expand_macro
from plan_validator import lint_plan_quick


Json = Union[Dict[str, Any], List[Any], str, int, float, bool, None]


class McpClient:
    """환경별 MCP 클라이언트 연결부(샘플).

    당신 환경에 맞게 다음만 구현하면 됩니다:
        call(tool_name: str, args: dict) -> Any
    """

    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run

    def call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        # TODO: 당신 orchestrator / MCP SDK 호출로 교체
        if self.dry_run:
            print(f"[DRY-RUN] CALL {tool_name} args={json.dumps(args, ensure_ascii=False)}")
            # 실행 결과 형태를 가정(실제 서버 반환과 다를 수 있음)
            if tool_name.startswith("create_"):
                return {"entity_ids": ["E1"]}
            return {"ok": True}
        else:
            raise NotImplementedError("McpClient.call()을 실제 MCP 호출로 구현하세요.")


def deep_replace_vars(obj: Json, vars_store: Dict[str, Any]) -> Json:
    """JSON 구조에서 '$var' 문자열을 vars_store 값으로 치환."""
    if isinstance(obj, str):
        if obj.startswith("$"):
            key = obj[1:]
            if key in vars_store:
                return copy.deepcopy(vars_store[key])
        return obj
    if isinstance(obj, list):
        return [deep_replace_vars(x, vars_store) for x in obj]
    if isinstance(obj, dict):
        return {k: deep_replace_vars(v, vars_store) for k, v in obj.items()}
    return obj


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True, help="drafting_plan json path")
    ap.add_argument("--args-map", default=None, help="args_map json path (optional)")
    ap.add_argument("--dry-run", action="store_true", help="do not call real MCP, print only")
    args = ap.parse_args()

    plan = load_json(args.plan)
    vars_store = plan.get("vars", {}) if isinstance(plan, dict) else {}
    args_map_path = args.args_map or plan.get("args_map")
    args_map = load_json(args_map_path) if args_map_path else None

    # 간단 린트(권장)
    lint_plan_quick(plan)

    adapter = ArgsAdapter(args_map or {})
    client = McpClient(dry_run=args.dry_run)

    seq: List[Dict[str, Any]] = plan["sequence"]

    expanded_steps: List[Dict[str, Any]] = []
    for step in seq:
        if "macro" in step:
            expanded = expand_macro(step["macro"], step.get("args", {}), step_id=step["id"])
            expanded_steps.extend(expanded)
        else:
            expanded_steps.append(step)

    for step in expanded_steps:
        tool = step["tool"]
        raw_args = step.get("args", {})

        # 변수 치환
        substituted = deep_replace_vars(raw_args, vars_store)

        # args 변환(canonical -> 실제 MCP)
        mapped_args = adapter.transform(tool, substituted)

        try:
            result = client.call(tool, mapped_args)
            # store last result/entity helper vars
            vars_store["LAST_RESULT"] = result
            if isinstance(result, dict):
                if "entity_id" in result:
                    vars_store["LAST"] = result.get("entity_id")
                elif "entity_ids" in result and isinstance(result.get("entity_ids"), list) and result.get("entity_ids"):
                    vars_store["LAST_IDS"] = result.get("entity_ids")
                    vars_store["LAST"] = result.get("entity_ids")[0]
        except Exception as e:
            on_error = step.get("on_error", "abort")
            print(f"[ERROR] step={step.get('id')} tool={tool} err={e}", file=sys.stderr)
            if on_error == "undo_last_action":
                try:
                    client.call("undo_last_action", {})
                except Exception:
                    pass
                continue
            if on_error == "continue":
                continue
            return 2

        assign = step.get("assign")
        if isinstance(assign, str) and assign.startswith("$"):
            vars_store[assign[1:]] = result

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

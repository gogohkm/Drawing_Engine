#!/usr/bin/env python3
"""
stgen_plan_executor.py

- 입력: drafting_plan JSON (schemas/drafting_plan_stgen_v1.schema.json)
- 기능:
  1) JSON Schema 검증(선택)
  2) macro 단계 전개(expand)
  3) $var 치환(resolution)
  4) stgen MCP tool 순차 호출

⚠️ 실제 MCP 호출은 환경마다 다르므로, `McpClient.call()`만 연결하면 됩니다.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

try:
    import jsonschema
except ImportError:
    jsonschema = None  # optional

from macro_library import expand_macros


class McpClient:
    """환경에 맞게 구현하세요."""
    def call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        raise NotImplementedError


class DryRunMcpClient(McpClient):
    def call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        print(f"[DRY-RUN] {tool_name}({json.dumps(args, ensure_ascii=False)})")
        # 도구별 결과를 흉내내면 체인 테스트가 쉬움
        if tool_name.startswith("create_"):
            return {"entity_ids": [f"@{tool_name}:dummy"]}
        return {"ok": True}


@dataclass
class ExecContext:
    vars: Dict[str, Any] = field(default_factory=dict)
    step_results: Dict[str, Any] = field(default_factory=dict)


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_vars(obj: Any, ctx: ExecContext) -> Any:
    """
    JSON 내부의 {"$var":"name"} 를 ctx.vars["name"]로 치환.
    문자열 템플릿 방식은 의도적으로 지원하지 않음(결정론/안정성).
    """
    if isinstance(obj, dict):
        if "$var" in obj and len(obj) == 1:
            name = obj["$var"]
            if name not in ctx.vars:
                raise KeyError(f"Variable not found: {name}")
            return ctx.vars[name]
        return {k: resolve_vars(v, ctx) for k, v in obj.items()}
    if isinstance(obj, list):
        return [resolve_vars(v, ctx) for v in obj]
    return obj


def validate_schema(plan: Dict[str, Any], schema_path: str) -> None:
    if jsonschema is None:
        print("WARNING: jsonschema not installed; skip schema validation", file=sys.stderr)
        return
    schema = load_json(schema_path)
    jsonschema.validate(plan, schema)


def execute_plan(plan: Dict[str, Any], client: McpClient, *, schema_path: Optional[str] = None) -> ExecContext:
    plan = copy.deepcopy(plan)

    if schema_path:
        validate_schema(plan, schema_path)

    ctx = ExecContext()
    # variables 초기화
    if isinstance(plan.get("variables"), dict):
        ctx.vars.update(plan["variables"])

    # 1) macro 전개
    expanded_steps = expand_macros(plan.get("steps", []), ctx.vars)
    plan["steps"] = expanded_steps

    # 2) 실행
    for step in plan["steps"]:
        step_id = step["id"]
        on_error = step.get("on_error", "halt")
        if "tool" not in step:
            raise ValueError(f"Expanded step must have tool. step_id={step_id}")

        tool = step["tool"]
        raw_args = step.get("args", {})
        try:
            args = resolve_vars(raw_args, ctx)
            result = client.call(tool, args)
            ctx.step_results[step_id] = result
            if step.get("save_as"):
                ctx.vars[step["save_as"]] = result
        except Exception as e:
            print(f"ERROR at step {step_id}: {e}", file=sys.stderr)
            if on_error == "undo_last_action":
                try:
                    client.call("undo_last_action", {})
                except Exception as e2:
                    print(f"ERROR on undo_last_action: {e2}", file=sys.stderr)
            if on_error == "continue":
                continue
            raise
    return ctx


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan_json", help="drafting_plan json")
    ap.add_argument("--schema", default="../schemas/drafting_plan_stgen_v1.schema.json")
    ap.add_argument("--no-validate", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    plan = load_json(args.plan_json)
    if args.dry_run:
        client: McpClient = DryRunMcpClient()
    else:
        # TODO: 여기에 실제 MCP 클라이언트를 연결하세요.
        # 예: client = YourRealMcpClient(...)
        print('WARNING: no real MCP client configured. Running in DRY-RUN mode.', file=sys.stderr)
        client = DryRunMcpClient()

    schema_path = None if args.no_validate else args.schema
    ctx = execute_plan(plan, client, schema_path=schema_path)
    print("DONE. saved vars:", list(ctx.vars.keys()))


if __name__ == "__main__":
    main()

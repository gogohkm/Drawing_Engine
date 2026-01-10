"""
Args Adapter

- 역할: plan에서 사용하는 "canonical args"를,
  실제 stgen MCP 서버가 요구하는 args 키/형태로 변환한다.

args_map 스펙 (args-map-v1):
{
  "version": "args-map-v1",
  "global": {"rename": {...}, "drop": [...], "add": {...}},
  "tools": {
     "create_text": {"rename": {...}, "drop":[...], "add": {...}}
  }
}

현재 구현은 "top-level key rename" 중심이다.
필요 시 transform 로직을 추가하여 좌표 포맷 변환 등 확장 가능.
"""

from __future__ import annotations

import copy
from typing import Any, Dict


class ArgsAdapter:
    def __init__(self, args_map: Dict[str, Any]):
        self.args_map = args_map or {}
        self.global_rules = (self.args_map.get("global") or {}) if isinstance(self.args_map, dict) else {}
        self.tool_rules = (self.args_map.get("tools") or {}) if isinstance(self.args_map, dict) else {}

    @staticmethod
    def _apply_rules(args: Dict[str, Any], rules: Dict[str, Any]) -> Dict[str, Any]:
        out = copy.deepcopy(args)

        # drop
        for k in rules.get("drop", []) or []:
            if k in out:
                out.pop(k, None)

        # rename
        rename = rules.get("rename") or {}
        for src, dst in rename.items():
            if src in out and dst not in out:
                out[dst] = out.pop(src)

        # add constants
        add = rules.get("add") or {}
        for k, v in add.items():
            if k not in out:
                out[k] = copy.deepcopy(v)

        return out

    def transform(self, tool: str, canonical_args: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(canonical_args, dict):
            return canonical_args

        out = self._apply_rules(canonical_args, self.global_rules)

        rules = self.tool_rules.get(tool) or {}
        out = self._apply_rules(out, rules)

        return out

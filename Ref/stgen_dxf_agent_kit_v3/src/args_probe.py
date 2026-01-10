"""
Args Probe Utility (Sample)

목적:
- 실제 stgen MCP 서버가 어떤 args 키를 요구하는지 빠르게 확인
- 에러 메시지를 수집하여 args_map 작성에 활용

사용:
  python src/args_probe.py --cases examples/args_probe_cases.json --dry-run

주의:
- dry-run이 아닌 경우 실제 도면이 변경될 수 있음.
- 테스트용 DXF 사본에서 실행 권장.
"""

from __future__ import annotations

import argparse
import json
from typing import Any, Dict, List


class McpClient:
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run

    def call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        if self.dry_run:
            print(f"[DRY-RUN] CALL {tool_name} args={json.dumps(args, ensure_ascii=False)}")
            return {"ok": True}
        else:
            raise NotImplementedError("실제 MCP 호출로 교체하세요.")


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", required=True)
    ap.add_argument("--out", default="probe_results.json")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = load_json(args.cases)
    cases: List[Dict[str, Any]] = data.get("cases") or []

    client = McpClient(dry_run=args.dry_run)
    results = []

    for c in cases:
        tool = c["tool"]
        a = c.get("args", {})
        try:
            r = client.call(tool, a)
            results.append({"tool": tool, "ok": True, "response": r})
        except Exception as e:
            results.append({"tool": tool, "ok": False, "error": str(e)})

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump({"results": results}, f, ensure_ascii=False, indent=2)

    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

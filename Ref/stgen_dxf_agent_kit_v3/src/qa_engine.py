"""
QA Engine (Sample)

stgen-dxf-viewer에서 제공하는 분석/추출 tool을 조합해
도면의 기본 품질을 점검하는 리포트를 생성한다.

실제 MCP 호출은 McpClient.call()을 구현해야 한다.
"""

from __future__ import annotations

import argparse
import json
from typing import Any, Dict, List

from qa_rules import (
    rule_required_layers,
    rule_placeholder_texts,
    rule_min_dimension_count,
    rule_no_entities_on_layer,
)


class McpClient:
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run

    def call(self, tool_name: str, args: Dict[str, Any]) -> Any:
        if self.dry_run:
            print(f"[DRY-RUN] CALL {tool_name} args={json.dumps(args, ensure_ascii=False)}")
            # 매우 단순한 더미 응답(실제와 다름)
            if tool_name == "get_dxf_layers":
                return {"layers": [{"name": "0", "visible": True, "entity_count": 0}, {"name": "A-WALL", "visible": True, "entity_count": 10}]}
            if tool_name == "list_all_texts":
                return {"texts": [{"text": "TBD", "insert": [0,0], "layer":"Z-TBD"}]}
            if tool_name == "extract_dimensions":
                return {"dimensions": []}
            if tool_name == "capture_dxf_view":
                return {"png_base64": "BASE64_PLACEHOLDER"}
            return {"ok": True}
        else:
            raise NotImplementedError


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="qa_report.json")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--required-layers", default="A-GRID,A-WALL,A-TEXT,A-DIM,Z-TBD")
    args = ap.parse_args()

    client = McpClient(dry_run=args.dry_run)

    # 기본 데이터 수집
    summary = client.call("get_dxf_summary", {})
    layers = client.call("get_dxf_layers", {})
    texts = client.call("list_all_texts", {})
    dims = client.call("extract_dimensions", {})
    snapshot = client.call("capture_dxf_view", {"format": "png_base64"})

    report: Dict[str, Any] = {
        "version": "qa-report-v1",
        "meta": {"generated_by": "qa_engine.py"},
        "snapshot": snapshot,
        "summary": summary,
        "layers": layers,
        "checks": []
    }

    required_layers = [s.strip() for s in args.required_layers.split(",") if s.strip()]
    report["checks"].extend(rule_required_layers(layers, required_layers))
    report["checks"].extend(rule_no_entities_on_layer(layers, layer_name="0"))
    report["checks"].extend(rule_placeholder_texts(texts))
    report["checks"].extend(rule_min_dimension_count(dims, min_count=1))

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

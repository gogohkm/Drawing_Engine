"""
executor_adapter_sample.py
- Drafting Plan(v1) JSON DSL executor skeleton
- 목적: LLM이 만든 plan_json을 '결정론적으로' CAD 엔진 함수로 변환해 실행

사용:
  python executor_adapter_sample.py path/to/plan.json

필수:
  - 당신의 CAD 엔진에 맞춰 CadAdapter 메서드를 구현하세요.
  - macros (macro:...)를 구현하거나, Planner가 macro를 쓰지 않도록 강제하세요.

주의:
  - 이 코드는 예시입니다. 트랜잭션/undo/redo/성능 최적화는 엔진 구조에 맞게 보강하세요.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import jsonschema


# ---------------------------
# 1) Adapter 인터페이스
# ---------------------------

class CadAdapter:
    """당신의 CAD 엔진 API를 이 인터페이스로 감싸세요.

    아래 메서드들은 '최소 기능'입니다.
    실제 엔진의 함수명/시그니처에 맞춰 구현하면 됩니다.
    """

    # --- Document / Drawing context ---
    def new_document(self, units: str) -> None:
        raise NotImplementedError

    def activate_model_space(self) -> None:
        raise NotImplementedError

    def activate_layout(self, name: str) -> None:
        raise NotImplementedError

    # --- Layers ---
    def create_layer(self, name: str, color: int = 7, linetype: str = "Continuous",
                     lineweight_mm: float = 0.18, plot: bool = True) -> None:
        raise NotImplementedError

    def set_current_layer(self, name: str) -> None:
        raise NotImplementedError

    # --- Linetype scale / variables ---
    def set_sysvars(self, vars: Dict[str, Any]) -> None:
        """예: {"LTSCALE":1.0, "MSLTSCALE":1, "PSLTSCALE":1}"""
        raise NotImplementedError

    # --- Entities: geometry ---
    def line(self, p1: Tuple[float, float], p2: Tuple[float, float]) -> str:
        raise NotImplementedError

    def polyline(self, points: List[Tuple[float, float]], closed: bool) -> str:
        raise NotImplementedError

    def circle(self, center: Tuple[float, float], r: float) -> str:
        raise NotImplementedError

    def offset(self, source_id: str, distance: float, side: str) -> str:
        """side: left|right|both"""
        raise NotImplementedError

    def trim(self, cutters: List[str], targets: List[str]) -> None:
        raise NotImplementedError

    def fillet(self, e1: str, e2: str, radius: float) -> None:
        raise NotImplementedError

    def hatch(self, boundary_ids: List[str], pattern: str, scale: float, angle_deg: float) -> str:
        raise NotImplementedError

    # --- Annotation ---
    def text(self, at: Tuple[float, float], height: float, value: str,
             rotation_deg: float = 0.0, style: str = "STANDARD") -> str:
        raise NotImplementedError

    def mtext(self, at: Tuple[float, float], width: float, height: float, value: str,
              rotation_deg: float = 0.0, style: str = "STANDARD") -> str:
        raise NotImplementedError

    def dim_linear(self, p1: Tuple[float, float], p2: Tuple[float, float], dim_line_at: Tuple[float, float],
                   style: str = "DIM_STD") -> str:
        raise NotImplementedError

    def leader(self, points: List[Tuple[float, float]], text: str, style: str = "LEADER_STD") -> str:
        raise NotImplementedError

    # --- Blocks / Xref ---
    def load_block(self, name: str, source: str, unit: str = "mm") -> None:
        raise NotImplementedError

    def insert_block(self, name: str, at: Tuple[float, float], rotation_deg: float = 0.0,
                     scale: Tuple[float, float] = (1.0, 1.0), attrs: Optional[Dict[str, str]] = None) -> str:
        raise NotImplementedError

    def attach_xref(self, name: str, path: str, attach_type: str = "overlay",
                    at: Tuple[float, float] = (0.0, 0.0),
                    scale: Tuple[float, float] = (1.0, 1.0),
                    rotation_deg: float = 0.0) -> None:
        raise NotImplementedError

    # --- Layout / Viewport / Plot ---
    def create_layout(self, name: str, paper: str, orientation: str, plot_style: Optional[str] = None) -> None:
        raise NotImplementedError

    def create_viewport(self, vp_id: str, center: Tuple[float, float], size: Tuple[float, float],
                        model_window_min: Tuple[float, float], model_window_max: Tuple[float, float],
                        scale: str, lock: bool = True) -> None:
        raise NotImplementedError

    def vp_freeze_layer(self, vp_id: str, layer: str) -> None:
        raise NotImplementedError

    def lock_viewport(self, vp_id: str, lock: bool = True) -> None:
        raise NotImplementedError

    def plot_layout(self, layout_name: str, filename: str, fmt: str = "pdf") -> None:
        raise NotImplementedError

    # --- QA / Query ---
    def qa_check(self, checks: List[str]) -> Dict[str, Any]:
        """엔진이 제공할 수 있는 검사들을 수행하고 결과를 dict로 반환."""
        return {"ok": True, "checks": checks, "warnings": []}


# ---------------------------
# 2) 유틸: placeholder 치환
# ---------------------------

def deep_replace(obj: Any, ctx: Dict[str, Any]) -> Any:
    """문자열 내 ${a.b.c} 형태를 ctx에서 찾아 치환."""
    if isinstance(obj, dict):
        return {k: deep_replace(v, ctx) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep_replace(v, ctx) for v in obj]
    if isinstance(obj, str):
        def repl(m):
            path = m.group(1).strip()
            cur = ctx
            for part in path.split("."):
                if isinstance(cur, dict) and part in cur:
                    cur = cur[part]
                else:
                    return m.group(0)  # 못 찾으면 그대로
            return str(cur)
        return __import__("re").sub(r"\$\{([^}]+)\}", repl, obj)
    return obj


# ---------------------------
# 3) Plan 실행기
# ---------------------------

@dataclass
class ExecContext:
    entities: Dict[str, str]  # plan id -> engine id
    current_layer: str = "0"


class PlanExecutor:
    def __init__(self, adapter: CadAdapter, schema_path: str):
        self.ad = adapter
        self.schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))

    def validate(self, plan: Dict[str, Any]) -> None:
        jsonschema.validate(instance=plan, schema=self.schema)

    def run(self, plan: Dict[str, Any]) -> None:
        # placeholder 치환 context 구성
        ctx = {
            "project": plan.get("project", {}),
            "globals": plan.get("globals", {}),
        }
        plan = deep_replace(plan, ctx)

        self.validate(plan)

        self.ad.new_document(units=plan["project"]["units"])

        for drawing in plan["drawings"]:
            self._run_drawing(drawing, plan)

    def _run_drawing(self, drawing: Dict[str, Any], plan: Dict[str, Any]) -> None:
        ex = ExecContext(entities={})

        # 1) Model space
        self.ad.activate_model_space()

        # 2) layers
        for layer in drawing.get("layers", []) or []:
            self.ad.create_layer(
                name=layer["name"],
                color=layer.get("color", 7),
                linetype=layer.get("linetype", "Continuous"),
                lineweight_mm=layer.get("lineweight_mm", 0.18),
                plot=layer.get("plot", True),
            )

        # 3) blocks
        for blk in drawing.get("blocks", []) or []:
            self.ad.load_block(blk["name"], blk.get("source", ""), unit=blk.get("unit", "mm"))

        # 4) xrefs
        for xr in drawing.get("xrefs", []) or []:
            self.ad.attach_xref(
                name=xr["name"],
                path=xr["path"],
                attach_type=xr.get("attach_type", "overlay"),
                at=tuple(xr.get("at", (0.0, 0.0))),
                scale=tuple(xr.get("scale", (1.0, 1.0))),
                rotation_deg=xr.get("rotation_deg", 0.0),
            )

        # 5) globals/sysvars
        lt = plan.get("globals", {}).get("linetype_scale")
        if isinstance(lt, dict):
            self.ad.set_sysvars(lt)

        # 6) sequence
        for step in drawing["sequence"]:
            self._run_op(step, ex)

        # 7) layout + viewports
        layout = drawing["layout"]
        self.ad.create_layout(layout["name"], layout["paper"], layout["orientation"], plot_style=layout.get("plot_style"))
        self.ad.activate_layout(layout["name"])

        # title block (옵션)
        tb = layout.get("title_block")
        if tb:
            # 사용자 엔진 기준으로 "삽입 위치"를 템플릿에서 잡아야 함
            # 여기서는 (0,0) 임시
            self.ad.insert_block(tb, at=(0.0, 0.0), attrs={"SHEET_ID": drawing["id"], "SHEET_TITLE": drawing["title"]})

        for vp in layout.get("viewports", []) or []:
            self.ad.create_viewport(
                vp_id=vp["id"],
                center=tuple(vp["center"]),
                size=tuple(vp["size"]),
                model_window_min=tuple(vp["model_window"]["min"]),
                model_window_max=tuple(vp["model_window"]["max"]),
                scale=vp["scale"],
                lock=vp.get("lock", True),
            )
            for lyr in vp.get("vp_freeze_layers", []) or []:
                self.ad.vp_freeze_layer(vp_id=vp["id"], layer=lyr)
            self.ad.lock_viewport(vp_id=vp["id"], lock=vp.get("lock", True))

        # 8) exports
        for expt in drawing.get("exports", []) or []:
            self.ad.plot_layout(layout_name=layout["name"], filename=expt["filename"], fmt=expt["format"])

    def _run_op(self, step: Dict[str, Any], ex: ExecContext) -> None:
        op = step["op"]
        args = step.get("args", {}) or {}
        plan_id = step.get("id")

        # macro
        if op.startswith("macro:"):
            self._run_macro(op, args, ex)
            return

        # base ops
        if op == "set_linetype_scale":
            self.ad.set_sysvars(args)
            return

        if op == "set_layer":
            self.ad.set_current_layer(args["layer"])
            ex.current_layer = args["layer"]
            return

        if op == "line":
            eid = self.ad.line(tuple(args["p1"]), tuple(args["p2"]))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "polyline":
            pts = [tuple(p) for p in args["points"]]
            eid = self.ad.polyline(pts, bool(args.get("closed", False)))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "circle":
            eid = self.ad.circle(tuple(args["center"]), float(args["r"]))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "offset":
            source = ex.entities.get(args["source"], args["source"])
            eid = self.ad.offset(source_id=source, distance=float(args["distance"]), side=args.get("side","both"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "trim":
            cutters = [ex.entities.get(i, i) for i in args.get("cutters", [])]
            targets = [ex.entities.get(i, i) for i in args.get("targets", [])]
            self.ad.trim(cutters=cutters, targets=targets)
            return

        if op == "fillet":
            e1 = ex.entities.get(args["e1"], args["e1"])
            e2 = ex.entities.get(args["e2"], args["e2"])
            self.ad.fillet(e1=e1, e2=e2, radius=float(args["radius"]))
            return

        if op == "hatch":
            bnds = [ex.entities.get(i, i) for i in args.get("boundary_ids", [])]
            eid = self.ad.hatch(boundary_ids=bnds, pattern=args.get("pattern","ANSI31"),
                                scale=float(args.get("scale",1.0)), angle_deg=float(args.get("angle_deg",0.0)))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "text":
            eid = self.ad.text(at=tuple(args["at"]), height=float(args["height"]),
                               value=args["value"], rotation_deg=float(args.get("rotation_deg",0.0)),
                               style=args.get("style","STANDARD"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "mtext":
            eid = self.ad.mtext(at=tuple(args["at"]), width=float(args["width"]), height=float(args["height"]),
                                value=args["value"], rotation_deg=float(args.get("rotation_deg",0.0)),
                                style=args.get("style","STANDARD"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "dim_linear":
            eid = self.ad.dim_linear(p1=tuple(args["p1"]), p2=tuple(args["p2"]), dim_line_at=tuple(args["dim_line_at"]),
                                     style=args.get("style","DIM_STD"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "leader":
            pts = [tuple(p) for p in args["points"]]
            eid = self.ad.leader(points=pts, text=args["text"], style=args.get("style","LEADER_STD"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "insert_block":
            eid = self.ad.insert_block(name=args["name"], at=tuple(args["at"]),
                                       rotation_deg=float(args.get("rotation_deg",0.0)),
                                       scale=tuple(args.get("scale",(1.0,1.0))),
                                       attrs=args.get("attrs"))
            if plan_id:
                ex.entities[plan_id] = eid
            return

        if op == "qa_check":
            res = self.ad.qa_check(checks=args.get("checks", []))
            # fail_policy는 여기서 처리 가능
            return

        raise ValueError(f"Unknown op: {op}")

    def _run_macro(self, op: str, args: Dict[str, Any], ex: ExecContext) -> None:
        # TODO: 여기에 macro 구현을 추가하세요.
        # 예: macro:draw_grids, macro:draw_arch_walls ...
        raise NotImplementedError(f"Macro not implemented: {op}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python executor_adapter_sample.py path/to/plan.json")
        sys.exit(1)

    plan_path = sys.argv[1]
    schema_path = str(Path(__file__).parent / "schemas" / "drafting_plan_v1.schema.json")

    plan = json.loads(Path(plan_path).read_text(encoding="utf-8"))

    # TODO: 아래에 당신의 실제 어댑터 구현체를 넣으세요.
    adapter = CadAdapter()  # type: ignore

    ex = PlanExecutor(adapter=adapter, schema_path=schema_path)
    ex.run(plan)
    print("DONE")

if __name__ == "__main__":
    main()

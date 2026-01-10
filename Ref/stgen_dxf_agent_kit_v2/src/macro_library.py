"""
macro_library.py

`macro:*` 단계를 primitive stgen tool-call(step.tool) 목록으로 전개합니다.

설계 철학
- macro는 LLM이 흔들리기 쉬운 반복 작업을 “결정론 템플릿”으로 고정하기 위함
- macro는 가능한 한 단순하게, 86 tools 조합만으로 구현

주의
- stgen MCP 도구의 실제 인자 스키마는 환경마다 다를 수 있습니다.
  이 파일은 "권장 인자 포맷"을 기준으로 작성되어 있으며,
  필요하면 args를 변환하는 어댑터 레이어를 executor에 추가하세요.
"""

from __future__ import annotations

from typing import Any, Dict, List
import math


def _sid(prefix: str, *parts: str) -> str:
    safe = [p.replace(" ", "_") for p in parts if p]
    return prefix + "__" + "__".join(safe) if safe else prefix


def _resolve_vars(obj: Any, variables: Dict[str, Any]) -> Any:
    """
    macro 전개 시점에서도 {"$var":"name"} 치환이 필요함.
    (macro는 primitive step보다 먼저 실행되므로)
    """
    if isinstance(obj, dict):
        if "$var" in obj and len(obj) == 1:
            name = obj["$var"]
            if name not in variables:
                raise KeyError(f"Variable not found for macro expansion: {name}")
            return variables[name]
        return {k: _resolve_vars(v, variables) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_resolve_vars(v, variables) for v in obj]
    return obj


def expand_macros(steps: List[Dict[str, Any]], variables: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for step in steps:
        if "macro" not in step:
            out.append(step)
            continue
        macro_name = step["macro"]
        macro_id = step["id"]
        args = _resolve_vars(step.get("args", {}), variables)
        expanded = expand_one_macro(macro_name, macro_id, args, variables)
        out.extend(expanded)
    return out


def expand_one_macro(macro: str, macro_id: str, args: Dict[str, Any], variables: Dict[str, Any]) -> List[Dict[str, Any]]:
    if macro == "macro:setup_layers":
        return macro_setup_layers(macro_id, args)
    if macro == "macro:draw_grids":
        return macro_draw_grids(macro_id, args)
    if macro == "macro:draw_walls":
        return macro_draw_walls(macro_id, args)
    if macro == "macro:draw_openings":
        return macro_draw_openings(macro_id, args)
    if macro == "macro:draw_columns_beams":
        return macro_draw_columns_beams(macro_id, args)
    if macro == "macro:add_room_labels":
        return macro_add_room_labels(macro_id, args)
    if macro == "macro:add_dimensions_basic":
        return macro_add_dimensions_basic(macro_id, args)
    if macro == "macro:steel_connection_detail":
        return macro_steel_connection_detail(macro_id, args)
    if macro == "macro:rc_rebar_detail":
        return macro_rc_rebar_detail(macro_id, args)
    if macro == "macro:member_schedule_table":
        return macro_member_schedule_table(macro_id, args)
    if macro == "macro:qa_snapshot":
        return macro_qa_snapshot(macro_id, args)
    if macro == "macro:export_png":
        return macro_export_png(macro_id, args)
    if macro == "macro:fit_and_save":
        return macro_fit_and_save(macro_id, args)
    raise ValueError(f"Unknown macro: {macro}")


# -----------------------------
# Macro implementations
# -----------------------------

def macro_setup_layers(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      layers: [{name,color?,linetype?,visible?}]
    """
    layers = args.get("layers", [])
    steps: List[Dict[str, Any]] = []
    for i, lay in enumerate(layers):
        name = lay["name"]
        st = {
            "id": _sid(macro_id, f"layer_{i:03d}", name),
            "tool": "create_layer",
            "args": lay
        }
        steps.append(st)
        if "visible" in lay:
            steps.append({
                "id": _sid(macro_id, f"layerVis_{i:03d}", name),
                "tool": "set_layer_visibility",
                "args": {"layer": name, "visible": lay["visible"]}
            })
    if args.get("set_current"):
        steps.append({
            "id": _sid(macro_id, "setCurrent", args["set_current"]),
            "tool": "set_current_layer",
            "args": {"layer": args["set_current"]}
        })
    return steps


def macro_draw_grids(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      layer: "A-GRID"
      x: [{coord,label}], y: [{coord,label}]
      bounds: [xmin,ymin,xmax,ymax]  (건물 외곽 또는 뷰 범위)
      extend: number (옵션)
      bubble_radius: number
      text_height: number
    """
    layer = args.get("layer", "A-GRID")
    bounds = args.get("bounds", [0, 0, 10000, 10000])
    xmin, ymin, xmax, ymax = bounds
    ext = float(args.get("extend", 1000))
    bubble_r = float(args.get("bubble_radius", 150))
    th = float(args.get("text_height", 150))

    xgr = args.get("x", [])
    ygr = args.get("y", [])

    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})

    # X grids: vertical lines
    for i, g in enumerate(xgr):
        x = g["coord"]
        label = g.get("label", str(i+1))
        steps.append({
            "id": _sid(macro_id, f"xLine_{i:03d}", label),
            "tool": "create_line",
            "args": {"start": [x, ymin-ext], "end": [x, ymax+ext]}
        })
        # bubbles top/bottom
        for pos, y in [("bot", ymin-ext-bubble_r*2), ("top", ymax+ext+bubble_r*2)]:
            c = [x, y]
            steps.append({"id": _sid(macro_id, f"xBubble_{pos}_{i:03d}", label), "tool": "create_circle", "args": {"center": c, "radius": bubble_r}})
            steps.append({"id": _sid(macro_id, f"xText_{pos}_{i:03d}", label), "tool": "create_text", "args": {"insert": [c[0], c[1]], "height": th, "text": label, "align": "CENTER"}})

    # Y grids: horizontal lines
    for i, g in enumerate(ygr):
        y = g["coord"]
        label = g.get("label", chr(ord('A')+i))
        steps.append({
            "id": _sid(macro_id, f"yLine_{i:03d}", label),
            "tool": "create_line",
            "args": {"start": [xmin-ext, y], "end": [xmax+ext, y]}
        })
        for pos, x in [("left", xmin-ext-bubble_r*2), ("right", xmax+ext+bubble_r*2)]:
            c = [x, y]
            steps.append({"id": _sid(macro_id, f"yBubble_{pos}_{i:03d}", label), "tool": "create_circle", "args": {"center": c, "radius": bubble_r}})
            steps.append({"id": _sid(macro_id, f"yText_{pos}_{i:03d}", label), "tool": "create_text", "args": {"insert": [c[0], c[1]], "height": th, "text": label, "align": "CENTER"}})

    return steps


def macro_draw_walls(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      layer: "A-WALL"
      walls: [{id,path:[[x,y]...], thickness, offset_style:"both|inner|outer"}]
      draw_centerline: bool
    """
    layer = args.get("layer", "A-WALL")
    walls = args.get("walls", [])
    draw_centerline = bool(args.get("draw_centerline", False))

    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})

    for i, w in enumerate(walls):
        wid = w.get("id", f"W{i+1}")
        path = w["path"]
        th = float(w.get("thickness", 200))
        off = th / 2.0
        poly_step_id = _sid(macro_id, f"wallPath_{i:03d}", wid)
        steps.append({"id": poly_step_id, "tool": "create_polyline", "args": {"points": path, "closed": False}, "save_as": f"{poly_step_id}_out"})

        if draw_centerline:
            continue

        # offset both sides: 구현마다 다를 수 있어, 기본은 2회 offset 호출
        steps.append({"id": _sid(macro_id, f"wallOffP_{i:03d}", wid), "tool": "offset_entity",
                      "args": {"entity": {"$var": f"{poly_step_id}_out"}, "distance": off, "side": "left", "reason": "wall_thickness"},
                      "save_as": f"{poly_step_id}_offL"})
        steps.append({"id": _sid(macro_id, f"wallOffN_{i:03d}", wid), "tool": "offset_entity",
                      "args": {"entity": {"$var": f"{poly_step_id}_out"}, "distance": off, "side": "right", "reason": "wall_thickness"},
                      "save_as": f"{poly_step_id}_offR"})

    return steps


def macro_draw_openings(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      openings: [{id,kind,insert:[x,y],width,height?,rotation_deg?,block_name?}]
    """
    openings = args.get("openings", [])
    steps: List[Dict[str, Any]] = []

    for i, op in enumerate(openings):
        kind = op.get("kind", "opening")
        layer = op.get("layer") or ("A-DOOR" if kind == "door" else "A-WIND" if kind == "window" else "A-OPEN")
        steps.append({"id": _sid(macro_id, f"setLayer_{i:03d}", layer), "tool": "set_current_layer", "args": {"layer": layer}})

        ins = op["insert"]
        w = float(op.get("width", 900))
        h = float(op.get("height", 2100))
        rot = float(op.get("rotation_deg", 0))

        if op.get("block_name"):
            steps.append({
                "id": _sid(macro_id, f"insBlock_{i:03d}", op.get("id","")),
                "tool": "insert_block",
                "args": {"name": op["block_name"], "insert": ins, "rotation_deg": rot, "scale": 1.0}
            })
            continue

        # 블록이 없으면 단순 기호로 표현 (사각형)
        p1 = [ins[0]-w/2, ins[1]-h/2]
        p2 = [ins[0]+w/2, ins[1]+h/2]
        steps.append({
            "id": _sid(macro_id, f"rect_{i:03d}", op.get("id", f"OP{i+1}")),
            "tool": "create_rectangle",
            "args": {"p1": p1, "p2": p2, "rotation_deg": rot}
        })

    return steps


def macro_draw_columns_beams(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      columns: [{center:[x,y], shape, size{b,h,d}, layer?}]
      beams: [{start:[x,y], end:[x,y], layer?}]
    """
    steps: List[Dict[str, Any]] = []
    cols = args.get("columns", [])
    beams = args.get("beams", [])

    for i, c in enumerate(cols):
        layer = c.get("layer", "S-COL")
        steps.append({"id": _sid(macro_id, f"setLayerC_{i:03d}", layer), "tool": "set_current_layer", "args": {"layer": layer}})
        center = c["center"]
        shape = c.get("shape", "rect")
        if shape == "circle":
            r = float(c.get("size", {}).get("d", 400)) / 2.0
            steps.append({"id": _sid(macro_id, f"colCirc_{i:03d}"), "tool": "create_circle", "args": {"center": center, "radius": r}})
        else:
            b = float(c.get("size", {}).get("b", 400))
            h = float(c.get("size", {}).get("h", 400))
            p1 = [center[0]-b/2, center[1]-h/2]
            p2 = [center[0]+b/2, center[1]+h/2]
            steps.append({"id": _sid(macro_id, f"colRect_{i:03d}"), "tool": "create_rectangle", "args": {"p1": p1, "p2": p2}})

    for i, b in enumerate(beams):
        layer = b.get("layer", "S-BEAM")
        steps.append({"id": _sid(macro_id, f"setLayerB_{i:03d}", layer), "tool": "set_current_layer", "args": {"layer": layer}})
        steps.append({"id": _sid(macro_id, f"beam_{i:03d}"), "tool": "create_line", "args": {"start": b["start"], "end": b["end"]}})

    return steps


def macro_add_room_labels(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      layer: "A-TEXT"
      rooms: [{name,label_point:[x,y], area?}]
      text_height
    """
    layer = args.get("layer", "A-TEXT")
    th = float(args.get("text_height", 200))
    rooms = args.get("rooms", [])
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})
    for i, r in enumerate(rooms):
        name = r["name"]
        if r.get("area") is not None:
            name = f"{name}\\n({r['area']:.2f})"
        steps.append({"id": _sid(macro_id, f"roomTxt_{i:03d}", r.get("id","")), "tool": "create_text",
                      "args": {"insert": r["label_point"], "height": th, "text": name, "align": "CENTER"}})
    return steps


def macro_add_dimensions_basic(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      layer: "A-DIMS"
      dims: [{p1:[x,y], p2:[x,y], dim_line_point:[x,y], kind:"aligned|horizontal|vertical"}]
    """
    layer = args.get("layer", "A-DIMS")
    dims = args.get("dims", [])
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})
    for i, d in enumerate(dims):
        steps.append({"id": _sid(macro_id, f"dim_{i:03d}"), "tool": "create_dimension", "args": d})
    return steps


def macro_steel_connection_detail(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    철골 접합부 상세(샘플)
    args:
      layer: "S-CONN"
      at_point:[x,y]
      bolt_pattern:{rows,cols,pitch_x,pitch_y,origin?}
      bolt_radius
      note_text?
    """
    layer = args.get("layer", "S-CONN")
    at = args.get("at_point", [0,0])
    pat = args.get("bolt_pattern", {"rows":2,"cols":2,"pitch_x":80,"pitch_y":80,"origin": at})
    rows = int(pat.get("rows",2)); cols=int(pat.get("cols",2))
    px=float(pat.get("pitch_x",80)); py=float(pat.get("pitch_y",80))
    origin = pat.get("origin", at)
    bolt_r = float(args.get("bolt_radius", 10))
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})

    for r in range(rows):
        for c in range(cols):
            x = origin[0] + c*px
            y = origin[1] + r*py
            steps.append({"id": _sid(macro_id, f"bolt_{r}_{c}"), "tool": "create_bolt_symbol", "args": {"center":[x,y], "radius": bolt_r}})

    if args.get("note_text"):
        steps.append({"id": _sid(macro_id, "noteLeader"), "tool": "create_leader",
                      "args": {"points":[[origin[0]+cols*px, origin[1]+rows*py],[origin[0]+cols*px+150, origin[1]+rows*py+150]],
                               "text": args["note_text"], "text_height": float(args.get("text_height", 150))}})
    return steps


def macro_rc_rebar_detail(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    RC 배근 상세(샘플)
    args:
      layer: "S-REBAR"
      bars: [{path:[[x,y]...], bar_dia:"D16", note?}]
    """
    layer = args.get("layer", "S-REBAR")
    bars = args.get("bars", [])
    th = float(args.get("text_height", 120))
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})
    for i, b in enumerate(bars):
        path = b["path"]
        steps.append({"id": _sid(macro_id, f"bar_{i:03d}"), "tool": "create_polyline", "args": {"points": path, "closed": False}})
        if b.get("note"):
            p = path[-1]
            steps.append({"id": _sid(macro_id, f"barNote_{i:03d}"), "tool": "create_leader",
                          "args": {"points":[p,[p[0]+200,p[1]+200]], "text": f"{b.get('bar_dia','') } {b['note']}", "text_height": th}})
    return steps


def macro_member_schedule_table(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    부재 리스트/스케줄 표를 DXF에 그리는 단순 테이블(샘플)
    args:
      layer: "S-TABLE"
      insert:[x,y]
      columns:[{title,width}]
      rows:[{cells:[...]}]
      row_height
      text_height
    """
    layer = args.get("layer", "S-TABLE")
    ins = args.get("insert", [0,0])
    cols = args.get("columns", [])
    rows = args.get("rows", [])
    rh = float(args.get("row_height", 250))
    th = float(args.get("text_height", 150))

    # table size
    total_w = sum(float(c.get("width", 1000)) for c in cols)
    total_h = rh * (len(rows)+1)

    x0, y0 = ins
    x1, y1 = x0 + total_w, y0 + total_h

    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "setLayer", layer), "tool": "set_current_layer", "args": {"layer": layer}})

    # outer border
    steps.append({"id": _sid(macro_id, "border"), "tool": "create_rectangle", "args": {"p1":[x0,y0], "p2":[x1,y1]}})

    # vertical lines
    cx = x0
    for i, c in enumerate(cols[:-1]):
        cx += float(c.get("width", 1000))
        steps.append({"id": _sid(macro_id, f"v_{i:03d}"), "tool": "create_line", "args": {"start":[cx,y0], "end":[cx,y1]}})

    # horizontal lines
    for r in range(1, len(rows)+1):
        yy = y0 + rh*r
        steps.append({"id": _sid(macro_id, f"h_{r:03d}"), "tool": "create_line", "args": {"start":[x0,yy], "end":[x1,yy]}})

    # header text
    cx = x0
    for i, c in enumerate(cols):
        w = float(c.get("width", 1000))
        center = [cx + w/2, y1 - rh/2]
        steps.append({"id": _sid(macro_id, f"hdr_{i:03d}"), "tool": "create_text",
                      "args": {"insert": center, "height": th, "text": str(c.get("title","")), "align": "CENTER"}})
        cx += w

    # body text
    for r_i, row in enumerate(rows):
        cy = y1 - rh*(r_i+1) - rh/2
        cells = row.get("cells", [])
        cx = x0
        for c_i, c in enumerate(cols):
            w = float(c.get("width", 1000))
            center = [cx + w/2, cy]
            txt = "" if c_i >= len(cells) else str(cells[c_i])
            steps.append({"id": _sid(macro_id, f"cell_{r_i:03d}_{c_i:03d}"), "tool": "create_text",
                          "args": {"insert": center, "height": th, "text": txt, "align": "CENTER"}})
            cx += w

    return steps


def macro_qa_snapshot(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    args:
      png_name?: str (미지원이면 무시)
    """
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "zoomExtents"), "tool": "zoom_extents", "args": {}})
    steps.append({"id": _sid(macro_id, "capture"), "tool": "capture_dxf_view", "args": {}})
    return steps


def macro_export_png(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    steps: List[Dict[str, Any]] = []
    if "bounds" in args:
        steps.append({"id": _sid(macro_id, "zoomBounds"), "tool": "zoom_to_bounds", "args": {"bounds": args["bounds"]}})
    else:
        steps.append({"id": _sid(macro_id, "zoomExtents"), "tool": "zoom_extents", "args": {}})
    steps.append({"id": _sid(macro_id, "capture"), "tool": "capture_dxf_view", "args": {}})
    return steps


def macro_fit_and_save(macro_id: str, args: Dict[str, Any]) -> List[Dict[str, Any]]:
    save_as = args.get("save_as", "output.dxf")
    steps: List[Dict[str, Any]] = []
    steps.append({"id": _sid(macro_id, "zoomExtents"), "tool": "zoom_extents", "args": {}})
    steps.append({"id": _sid(macro_id, "save"), "tool": "save_dxf", "args": {"path": save_as}})
    return steps

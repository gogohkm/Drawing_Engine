"""
Macro Library

macro step을 tool step 리스트로 전개한다.
매크로는 "반복적이고 규칙적인 작업"을 고정하기 위해 존재한다.

중요:
- create_* tool의 args는 canonical 포맷이다.
- 실제 stgen MCP 서버 args 키가 다르면 args_map으로 변환한다.
- 일부 tool은 엔티티 ID를 요구할 수 있다. 이 경우:
  1) 먼저 create_*로 엔티티를 만들고(assign),
  2) offset_entity 등에서 그 엔티티 ID를 참조하도록 plan/executor를 확장해야 한다.

이 키트는 "경계(boundary) 기반" 입력을 우선 지원하여,
ID 참조가 없어도 작도 가능하도록 설계했다.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List


def _deg_to_rad(a: float) -> float:
    return a * math.pi / 180.0


def _rot(p, ang_rad):
    x, y = p
    c = math.cos(ang_rad)
    s = math.sin(ang_rad)
    return [x * c - y * s, x * s + y * c]


def _add(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def expand_macro(name: str, args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    fn = {
        "macro:setup_layers": macro_setup_layers,
        "macro:draw_grids": macro_draw_grids,
        "macro:draw_walls": macro_draw_walls,
        "macro:draw_openings": macro_draw_openings,
        "macro:add_room_labels": macro_add_room_labels,
        "macro:add_dimensions_basic": macro_add_dimensions_basic,
        "macro:member_schedule_table": macro_member_schedule_table,
        "macro:qa_snapshot": macro_qa_snapshot,
        "macro:fit_and_save": macro_fit_and_save,
        "macro:steel_connection_detail": macro_steel_connection_detail,
        "macro:rc_rebar_detail": macro_rc_rebar_detail,
    }.get(name)

    if fn is None:
        raise ValueError(f"Unknown macro: {name}")

    return fn(args, step_id=step_id)


def macro_setup_layers(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layers = args.get("layers") or []
    steps = []
    for i, layer in enumerate(layers):
        steps.append({
            "id": f"{step_id}.L{i+1}",
            "tool": "create_layer",
            "args": layer,
            "comment": "create_layer(name,color,linetype...)"
        })
    return steps


def macro_draw_grids(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    """args:
    {
      "layer":"A-GRID",
      "extents": {"min":[x,y], "max":[x,y]},
      "x": [{"coord":0,"label":"1"}, ...],
      "y": [{"coord":0,"label":"A"}, ...],
      "bubble_radius": 150,
      "label_height": 250,
      "label_offset": 300
    }
    """
    layer = args.get("layer", "A-GRID")
    ext = args["extents"]
    xmin, ymin = ext["min"]
    xmax, ymax = ext["max"]
    bubble_r = args.get("bubble_radius", 150)
    th = args.get("label_height", 250)
    off = args.get("label_offset", 300)

    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]

    for i, gx in enumerate(args.get("x") or []):
        x = gx["coord"]
        steps.append({"id": f"{step_id}.X{i+1}.L", "tool": "create_line", "args": {"start":[x, ymin], "end":[x, ymax]}})
        steps.append({"id": f"{step_id}.X{i+1}.B", "tool": "create_circle", "args": {"center":[x, ymax+off], "radius": bubble_r}})
        steps.append({"id": f"{step_id}.X{i+1}.T", "tool": "create_text", "args": {"insert":[x, ymax+off], "height": th, "text": gx["label"], "align":"CENTER"}})

    for i, gy in enumerate(args.get("y") or []):
        y = gy["coord"]
        steps.append({"id": f"{step_id}.Y{i+1}.L", "tool": "create_line", "args": {"start":[xmin, y], "end":[xmax, y]}})
        steps.append({"id": f"{step_id}.Y{i+1}.B", "tool": "create_circle", "args": {"center":[xmin-off, y], "radius": bubble_r}})
        steps.append({"id": f"{step_id}.Y{i+1}.T", "tool": "create_text", "args": {"insert":[xmin-off, y], "height": th, "text": gy["label"], "align":"CENTER"}})

    return steps


def macro_draw_walls(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    """벽 생성(우선: boundary 기반).
    args:
    {
      "layer":"A-WALL",
      "walls":[
        {"id":"W1","boundary":[[x,y]...], "closed":true},
        {"id":"W2","centerline":[[x,y]...], "thickness":200}
      ]
    }

    - boundary가 있으면: create_polyline(closed=True)로 바로 생성
    - boundary가 없고 centerline+thickness만 있으면:
        offset_entity 기반 로직을 사용해야 하는데,
        offset_entity가 엔티티 ID를 요구할 수 있으므로 프로젝트 환경에 맞게 보완 필요.
    """
    layer = args.get("layer", "A-WALL")
    walls = args.get("walls") or []
    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]

    for i, w in enumerate(walls):
        if w.get("boundary"):
            pts = w["boundary"]
            steps.append({
                "id": f"{step_id}.W{i+1}.BND",
                "tool": "create_polyline",
                "args": {"points": pts, "closed": True},
                "comment": f"wall {w.get('id')}"
            })
            continue

        # fallback: centerline + thickness (주의: 오프셋은 엔티티 ID 기반일 수 있음)
        pts = w.get("centerline") or []
        t = float(w.get("thickness", 200))
        steps.append({
            "id": f"{step_id}.W{i+1}.CL",
            "tool": "create_polyline",
            "args": {"points": pts, "closed": False},
            "comment": "fallback centerline (for offset workflow)"
        })
        steps.append({
            "id": f"{step_id}.W{i+1}.O1",
            "tool": "offset_entity",
            "args": {"entity_id": "$LAST", "distance": t/2, "side": "LEFT"},
            "comment": "NOTE: '$LAST' requires executor enhancement to reference last created entity id"
        })

    return steps


def macro_draw_openings(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    """문/창 단순 표현.
    args:
    {
      "door_layer":"A-DOOR",
      "window_layer":"A-WINDOW",
      "openings":[{"type":"DOOR","center":[x,y],"width":900,"orientation_deg":0,"hinge":"L"}, ...]
    }
    """
    steps: List[Dict[str, Any]] = []
    openings = args.get("openings") or []

    for i, op in enumerate(openings):
        typ = op["type"]
        cen = op["center"]
        w = float(op.get("width", 900))
        ang = _deg_to_rad(float(op.get("orientation_deg", 0)))
        hinge = op.get("hinge", "L")

        if typ == "DOOR":
            layer = args.get("door_layer", "A-DOOR")
        elif typ == "WINDOW":
            layer = args.get("window_layer", "A-WINDOW")
        else:
            layer = args.get("void_layer", "A-OPENING")

        steps.append({"id": f"{step_id}.OP{i+1}.SCL", "tool": "set_current_layer", "args": {"name": layer}})

        if typ == "DOOR":
            # hinge at left/right along local X
            if hinge.upper() == "L":
                hinge_local = [-w/2, 0]
                free_local = [w/2, 0]
            else:
                hinge_local = [w/2, 0]
                free_local = [-w/2, 0]

            hinge_pt = _add(cen, _rot(hinge_local, ang))
            free_pt = _add(cen, _rot(free_local, ang))

            steps.append({"id": f"{step_id}.OP{i+1}.DL", "tool": "create_line", "args": {"start": hinge_pt, "end": free_pt}})
            steps.append({"id": f"{step_id}.OP{i+1}.DA", "tool": "create_arc", "args": {"center": hinge_pt, "radius": w, "start_angle_deg": float(op.get("swing_start_deg", 0)), "end_angle_deg": float(op.get("swing_end_deg", 90))}})

        elif typ == "WINDOW":
            half = w/2
            p1 = _add(cen, _rot([-half, 0], ang))
            p2 = _add(cen, _rot([half, 0], ang))
            steps.append({"id": f"{step_id}.OP{i+1}.WL", "tool": "create_line", "args": {"start": p1, "end": p2}})

    return steps


def macro_add_room_labels(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layer = args.get("layer", "A-TEXT")
    th = float(args.get("text_height", 250))
    rooms = args.get("rooms") or []
    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]
    for i, r in enumerate(rooms):
        txt = r.get("name", r.get("id", f"ROOM{i+1}"))
        if r.get("area") is not None:
            txt = f"{txt}\\nA={r['area']:.2f}"
        steps.append({"id": f"{step_id}.R{i+1}", "tool": "create_text", "args": {"insert": r["label_point"], "height": th, "text": txt, "align": "CENTER"}})
    return steps


def macro_add_dimensions_basic(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layer = args.get("layer", "A-DIM")
    dims = args.get("dims") or []
    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]
    for i, d in enumerate(dims):
        steps.append({"id": f"{step_id}.D{i+1}", "tool": "create_dimension", "args": d})
    return steps


def macro_member_schedule_table(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layer = args.get("layer", "S-NOTE")
    org = args["origin"]
    row_h = float(args.get("row_h", 300))
    col_w = args.get("col_w") or [800, 1200, 600, 1200]
    th = float(args.get("text_height", 200))

    headers = args.get("headers") or []
    rows = args.get("rows") or []

    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]

    ncols = len(col_w)
    nrows = 1 + len(rows)
    width = sum(col_w)
    height = nrows * row_h

    x0, y0 = org
    steps.append({"id": f"{step_id}.OUT", "tool": "create_rectangle", "args": {"p1":[x0, y0], "p2":[x0+width, y0-height]}})

    x = x0
    for ci in range(ncols-1):
        x += col_w[ci]
        steps.append({"id": f"{step_id}.V{ci+1}", "tool": "create_line", "args": {"start":[x, y0], "end":[x, y0-height]}})

    y = y0
    for ri in range(nrows-1):
        y -= row_h
        steps.append({"id": f"{step_id}.H{ri+1}", "tool": "create_line", "args": {"start":[x0, y], "end":[x0+width, y]}})

    cx = x0
    for ci, htxt in enumerate(headers):
        cw = col_w[ci]
        steps.append({"id": f"{step_id}.HT{ci+1}", "tool": "create_text", "args": {"insert":[cx+cw/2, y0-row_h/2], "height": th, "text": str(htxt), "align":"CENTER"}})
        cx += cw

    for ri, row in enumerate(rows):
        cy = y0 - row_h*(ri+1) - row_h/2
        cx = x0
        for ci in range(ncols):
            cw = col_w[ci]
            cell = row[ci] if ci < len(row) else ""
            steps.append({"id": f"{step_id}.T{ri+1}.{ci+1}", "tool": "create_text", "args": {"insert":[cx+cw/2, cy], "height": th, "text": str(cell), "align":"CENTER"}})
            cx += cw

    return steps


def macro_qa_snapshot(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    return [
        {"id": f"{step_id}.ZE", "tool": "zoom_extents", "args": {}},
        {"id": f"{step_id}.CAP", "tool": "capture_dxf_view", "args": {"format": "png_base64"}, "assign": "$snapshot"}
    ]


def macro_fit_and_save(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    path = args.get("path") or args.get("target_dxf_path") or "out.dxf"
    return [
        {"id": f"{step_id}.ZE", "tool": "zoom_extents", "args": {}},
        {"id": f"{step_id}.SAVE", "tool": "save_dxf", "args": {"path": path}}
    ]


def macro_steel_connection_detail(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layer = args.get("layer", "S-STEEL")
    p = args["at_point"]
    plate_w = float(args.get("plate_w", 200))
    plate_h = float(args.get("plate_h", 300))
    bolt_pitch = float(args.get("bolt_pitch", 80))
    bolt_rows = int(args.get("bolt_rows", 3))
    bolt_cols = int(args.get("bolt_cols", 2))
    bolt_r = float(args.get("bolt_r", 10))

    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]

    p1 = [p[0]-plate_w/2, p[1]+plate_h/2]
    p2 = [p[0]+plate_w/2, p[1]-plate_h/2]
    steps.append({"id": f"{step_id}.PL", "tool": "create_rectangle", "args": {"p1": p1, "p2": p2}})

    start_x = p[0] - (bolt_cols-1)*bolt_pitch/2
    start_y = p[1] + (bolt_rows-1)*bolt_pitch/2
    for r in range(bolt_rows):
        for c in range(bolt_cols):
            cx = start_x + c*bolt_pitch
            cy = start_y - r*bolt_pitch
            steps.append({"id": f"{step_id}.B{r+1}{c+1}", "tool": "create_bolt_symbol", "args": {"center":[cx,cy], "radius": bolt_r}})

    note_layer = args.get("note_layer", "S-NOTE")
    steps.append({"id": f"{step_id}.SCLN", "tool": "set_current_layer", "args": {"name": note_layer}})
    steps.append({"id": f"{step_id}.NOTE", "tool": "create_text", "args": {"insert":[p[0]+plate_w/2+50, p[1]], "height": float(args.get("text_height", 120)), "text": args.get("note","CONN"), "align":"LEFT"}})

    return steps


def macro_rc_rebar_detail(args: Dict[str, Any], step_id: str) -> List[Dict[str, Any]]:
    layer = args.get("layer", "S-REBAR")
    bars = args.get("bars") or []
    steps = [{"id": f"{step_id}.SCL", "tool": "set_current_layer", "args": {"name": layer}}]
    for i, b in enumerate(bars):
        pts = b.get("shape_points") or []
        if len(pts) >= 2:
            steps.append({"id": f"{step_id}.B{i+1}", "tool": "create_polyline", "args": {"points": pts, "closed": False}})
        mark = b.get("mark")
        if mark:
            note_layer = args.get("note_layer", "S-NOTE")
            steps.append({"id": f"{step_id}.SCLN{i+1}", "tool": "set_current_layer", "args": {"name": note_layer}})
            steps.append({"id": f"{step_id}.BT{i+1}", "tool": "create_text", "args": {"insert": b.get("label_point", pts[-1]), "height": float(args.get("text_height", 120)), "text": mark, "align":"LEFT"}})
            steps.append({"id": f"{step_id}.SCLB{i+1}", "tool": "set_current_layer", "args": {"name": layer}})
    return steps

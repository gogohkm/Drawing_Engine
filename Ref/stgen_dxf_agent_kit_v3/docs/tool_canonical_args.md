# stgen Tool Canonical Args (권장 포맷)

이 문서는 Planner가 plan을 만들 때 사용하는 **권장 canonical args** 포맷입니다.

실제 stgen MCP가 다른 키를 요구하면 `args_map`으로 변환하세요.


## 도면 분석/상태

### `get_dxf_status`

권장 args 예:

```json
{}
```

### `get_dxf_summary`

권장 args 예:

```json
{}
```

### `get_dxf_layers`

권장 args 예:

```json
{}
```

### `identify_drawing_type`

권장 args 예:

```json
{}
```

### `analyze_layer_structure`

권장 args 예:

```json
{}
```

### `analyze_region`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `analyze_pattern`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `count_by_type`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `count_blocks`

권장 args 예:

```json
{}
```

### `compare_layers`

권장 args 예:

```json
{
  "layer_a": "A-WALL",
  "layer_b": "A-WALL-OLD"
}
```


## 개체 생성

### `create_line`

권장 args 예:

```json
{
  "start": [
    0,
    0
  ],
  "end": [
    1000,
    0
  ]
}
```

### `create_polyline`

권장 args 예:

```json
{
  "points": [
    [
      0,
      0
    ],
    [
      1000,
      0
    ],
    [
      1000,
      1000
    ]
  ],
  "closed": false
}
```

### `create_circle`

권장 args 예:

```json
{
  "center": [
    0,
    0
  ],
  "radius": 100
}
```

### `create_arc`

권장 args 예:

```json
{
  "center": [
    0,
    0
  ],
  "radius": 100,
  "start_angle_deg": 0,
  "end_angle_deg": 90
}
```

### `create_rectangle`

권장 args 예:

```json
{
  "p1": [
    0,
    0
  ],
  "p2": [
    1000,
    -500
  ]
}
```

### `create_text`

권장 args 예:

```json
{
  "insert": [
    0,
    0
  ],
  "height": 250,
  "text": "TEXT",
  "align": "LEFT"
}
```

### `create_dimension`

권장 args 예:

```json
{
  "p1": [
    0,
    0
  ],
  "p2": [
    1000,
    0
  ],
  "type": "ALIGNED",
  "offset": 300
}
```

### `create_hatch`

권장 args 예:

```json
{
  "boundary": {
    "type": "polyline",
    "points": [
      [
        0,
        0
      ],
      [
        1000,
        0
      ],
      [
        1000,
        1000
      ],
      [
        0,
        1000
      ]
    ],
    "closed": true
  },
  "pattern": "SOLID"
}
```

### `create_leader`

권장 args 예:

```json
{
  "points": [
    [
      0,
      0
    ],
    [
      300,
      200
    ]
  ],
  "text": "NOTE",
  "arrow": true
}
```

### `create_block`

권장 args 예:

```json
{
  "name": "BLK1",
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `create_bolt_symbol`

권장 args 예:

```json
{
  "center": [
    0,
    0
  ],
  "radius": 10
}
```

### `create_center_mark`

권장 args 예:

```json
{
  "center": [
    0,
    0
  ],
  "size": 50
}
```


## 개체 수정/편집

### `move_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "delta": [
    100,
    0
  ]
}
```

### `copy_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "delta": [
    0,
    100
  ]
}
```

### `rotate_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "base": [
    0,
    0
  ],
  "angle_deg": 90
}
```

### `scale_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "base": [
    0,
    0
  ],
  "scale": 2.0
}
```

### `delete_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `erase_by_bounds`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "mode": "CROSSING"
}
```

### `trim_extend`

권장 args 예:

```json
{
  "cutters": [
    "E10"
  ],
  "targets": [
    "E11"
  ],
  "mode": "TRIM"
}
```

### `offset_entity`

권장 args 예:

```json
{
  "entity_id": "E1",
  "distance": 100,
  "side": "LEFT"
}
```

### `mirror_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "axis": {
    "p1": [
      0,
      0
    ],
    "p2": [
      0,
      1000
    ]
  },
  "copy": true
}
```

### `array_copy`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "type": "RECT",
  "rows": 3,
  "cols": 2,
  "dx": 200,
  "dy": 300
}
```

### `break_entity`

권장 args 예:

```json
{
  "entity_id": "E1",
  "at": [
    100,
    0
  ]
}
```

### `divide_entity`

권장 args 예:

```json
{
  "entity_id": "E1",
  "n": 5
}
```

### `join_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `explode_block`

권장 args 예:

```json
{
  "insert_id": "E100"
}
```

### `stretch`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "delta": [
    100,
    0
  ]
}
```

### `lengthen`

권장 args 예:

```json
{
  "entity_id": "E1",
  "delta": 100
}
```

### `fillet_chamfer`

권장 args 예:

```json
{
  "e1": "E1",
  "e2": "E2",
  "mode": "FILLET",
  "radius": 50
}
```

### `edit_text`

권장 args 예:

```json
{
  "entity_id": "E1",
  "text": "NEW"
}
```

### `close_polyline`

권장 args 예:

```json
{
  "entity_id": "E1",
  "closed": true
}
```

### `reverse_polyline`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```


## 속성 변경

### `change_entity_color`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "aci": 1
}
```

### `change_entity_layer`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "layer": "A-WALL"
}
```

### `change_entity_linetype`

권장 args 예:

```json
{
  "entity_ids": [
    "E1"
  ],
  "linetype": "DASHED"
}
```

### `set_current_layer`

권장 args 예:

```json
{
  "name": "A-WALL"
}
```

### `create_layer`

권장 args 예:

```json
{
  "name": "A-WALL",
  "aci": 7,
  "linetype": "CONTINUOUS",
  "visible": true
}
```

### `set_layer_visibility`

권장 args 예:

```json
{
  "name": "A-WALL",
  "visible": true
}
```

### `merge_layers`

권장 args 예:

```json
{
  "sources": [
    "A-WALL-OLD"
  ],
  "target": "A-WALL"
}
```


## 조회/검색

### `find_entities`

권장 args 예:

```json
{
  "layer": "A-WALL",
  "type": "LINE",
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `find_annotations`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `find_connected_entities`

권장 args 예:

```json
{
  "point": [
    0,
    0
  ],
  "tolerance": 1.0
}
```

### `find_intersections`

권장 args 예:

```json
{
  "entity_a": "E1",
  "entity_b": "E2"
}
```

### `find_parallel_lines`

권장 args 예:

```json
{
  "tolerance_deg": 1.0
}
```

### `find_replace_text`

권장 args 예:

```json
{
  "find": "OLD",
  "replace": "NEW"
}
```

### `detect_symbols`

권장 args 예:

```json
{
  "types": [
    "BOLT",
    "CENTER_MARK",
    "WELD"
  ],
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `get_entity_properties`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```

### `get_entity_points`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```

### `get_selected_entities`

권장 args 예:

```json
{}
```

### `list_all_texts`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `list_blocks`

권장 args 예:

```json
{}
```


## 측정/공간

### `measure_distance`

권장 args 예:

```json
{
  "p1": [
    0,
    0
  ],
  "p2": [
    1000,
    0
  ]
}
```

### `measure_angle`

권장 args 예:

```json
{
  "line_a": "E1",
  "line_b": "E2"
}
```

### `measure_arc_length`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```

### `calculate_area`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```

### `calculate_perimeter`

권장 args 예:

```json
{
  "entity_id": "E1"
}
```

### `sum_lengths`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `sum_areas`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `get_region_bounds`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ]
}
```

### `verify_alignment`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ],
  "mode": "HORIZONTAL",
  "tolerance": 1.0
}
```

### `align_to_baseline`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ],
  "baseline": {
    "p1": [
      0,
      0
    ],
    "p2": [
      1000,
      0
    ]
  }
}
```

### `snap_to_grid`

권장 args 예:

```json
{
  "points": [
    [
      10,
      10
    ],
    [
      20,
      20
    ]
  ],
  "grid": 50
}
```

### `generate_bom`

권장 args 예:

```json
{
  "mode": "AUTO",
  "out_path": "bom.csv"
}
```


## 영역 작업/추출

### `extract_region`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "format": "JSON"
}
```

### `extract_dimensions`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `extract_dxf_entities`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `clone_region`

권장 args 예:

```json
{
  "source_bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "target_origin": [
    2000,
    0
  ]
}
```

### `rotate_region`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "base": [
    0,
    0
  ],
  "angle_deg": 90
}
```

### `scale_region`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  },
  "base": [
    0,
    0
  ],
  "scale": 2.0
}
```


## 파일/뷰

### `capture_dxf_view`

권장 args 예:

```json
{
  "format": "png_base64"
}
```

### `zoom_extents`

권장 args 예:

```json
{}
```

### `zoom_to_bounds`

권장 args 예:

```json
{
  "bounds": {
    "min": [
      0,
      0
    ],
    "max": [
      1000,
      1000
    ]
  }
}
```

### `save_dxf`

권장 args 예:

```json
{
  "path": "out.dxf"
}
```

### `export_entities`

권장 args 예:

```json
{
  "entity_ids": [
    "E1",
    "E2"
  ],
  "path": "export.dxf"
}
```

### `insert_block`

권장 args 예:

```json
{
  "name": "BLK1",
  "insert": [
    0,
    0
  ],
  "rotation_deg": 0,
  "scale": 1.0
}
```

### `undo_last_action`

권장 args 예:

```json
{}
```

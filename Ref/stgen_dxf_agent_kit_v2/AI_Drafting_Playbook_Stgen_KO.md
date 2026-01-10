# AI Drafting Playbook (KO) — stgen-dxf-viewer 86 tools 기반

이 문서는 **AI가 실제로 stgen MCP 도구를 호출해 DXF를 작성**한다는 전제에서,
“도면을 그리는 순서/절차”만을 최대한 결정론적으로 정리한 플레이북입니다.

> 목표  
> - AI가 망설이지 않도록 “항상 같은 순서”로 그리게 만든다.  
> - 매 단계마다 **어떤 도구를 왜 쓰는지**를 명확히 한다.  
> - 실패 시 되돌리기(undo_last_action)와 QA 루프를 내장한다.

---

## 1) 공통 원칙(모든 도면)

### 1.1 사전 점검(Pre-flight)
1. `get_dxf_status` : 현재 열린 파일 확인
2. `get_dxf_summary` : 개체 수/레이어/경계 확인
3. `get_dxf_layers` : 레이어 가시성/개체 수 확인
4. (기존 도면이 있다면)  
   - `identify_drawing_type`  
   - `analyze_layer_structure`  
   - `count_by_type`, `count_blocks`

> 목적: “이미 있는 걸 덮어쓰지 않기”, “레이어 규칙 파악”, “도면 범위(스케일 감)” 잡기

### 1.2 레이어/스타일 세팅(반드시 먼저)
1. 표준 레이어 목록을 확정한다.
2. 레이어 생성: `create_layer`
3. 필요한 레이어 ON/OFF: `set_layer_visibility`
4. 그릴 때마다 활성 레이어 지정: `set_current_layer`

> ByLayer를 기본으로 하고, 개체 개별 속성 변경은 최소화  
> (필요 시 `change_entity_color`, `change_entity_linetype`, `change_entity_layer`)

### 1.3 “큰 것 → 작은 것 → 텍스트/치수” 순서
- 큰 기준: **그리드/기준선 → 외곽 → 주요 구조 → 개구부 → 상세 → 주석/치수**
- 마지막에 검증과 저장:
  - `zoom_extents`
  - `capture_dxf_view`
  - `save_dxf`

### 1.4 선택/조회는 “객체 ID” 또는 “조건 검색”으로
- ID 기반: 생성 도구 결과(엔티티 ID)를 `save_as`로 저장하고 재사용
- 조건 검색 기반:
  - `find_entities` (레이어/타입/범위 조건)
  - `get_region_bounds`, `analyze_region`
  - `find_annotations`, `extract_dimensions`

### 1.5 실패 복구(Undo 전략)
- 위험한 편집(삭제/트림/오프셋/조인/분해) 전에 snapshot:
  - `capture_dxf_view`
- 오류 발생 시:
  - `undo_last_action` 1회 수행 후 재시도(다른 파라미터로)

---

## 2) 건축 평면도(A-PLAN) 절차

### 2.1 입력 정규화(좌표/그리드/외곽)
1. 그리드 좌표(X/Y) 리스트 확정  
2. 건물 외곽 Bounds 확정 (없으면 벽/기둥의 min/max로 추정)

### 2.2 그리드 작성
1. `set_current_layer(A-GRID)`
2. X 그리드(수직):
   - `create_line(start=[x, ymin-ext], end=[x, ymax+ext])`
   - 버블: `create_circle(center=[x, ...], radius=r)`
   - 라벨: `create_text(insert=[x, ...], height=h, text="1", align="CENTER")`
3. Y 그리드(수평)도 동일

검증:
- `find_parallel_lines`로 간격 검증(선택)
- `verify_alignment`로 수평/수직 정렬 검증(선택)

### 2.3 외벽/내벽 작성
권장 2안 중 선택:

**안 A(단순/안정): 벽 중심선 또는 한쪽 면만 표현**
- `set_current_layer(A-WALL)`
- `create_polyline(points=[...])` 로 벽 중심선(또는 외벽선) 작성
- 벽 두께 표현이 필요하면:
  - `offset_entity(distance=벽두께/2, side=left/right)` 2회

**안 B(정밀): 폐합 경계 + 해치**
- 외곽/내곽 경계를 폐합 polyline으로 만든 뒤
- `create_hatch(boundary=...)`

> create_hatch의 boundary 인자 형식은 구현마다 다를 수 있으므로,
> 첫 적용 시 작은 영역에서 테스트 후 표준화 권장

### 2.4 문/창호/개구부
1. 표준 블록이 있으면:
   - `insert_block(name="D-SINGLE-900", insert=[...], rotation_deg=...)`
2. 블록이 없으면:
   - 문틀: `create_rectangle`
   - 스윙: `create_arc`
   - 창호: `create_rectangle` 또는 `create_line` 패턴

### 2.5 실명/실면적/마감
- `set_current_layer(A-TEXT)`
- `create_text`로 Room Label
- 면적이 필요하면:
  - 룸 경계를 폐합 polyline으로 만들고 `calculate_area`

### 2.6 치수
- `set_current_layer(A-DIMS)`
- `create_dimension(p1, p2, dim_line_point, kind)`  
  - 외곽 치수 → 내부 치수 → 개구부 치수 순

QA:
- `extract_dimensions`로 치수 값/텍스트 추출 후 누락 여부 확인
- `find_annotations`로 텍스트/리더 존재 확인

### 2.7 저장/출력
- `zoom_extents`
- `capture_dxf_view` (검수 이미지)
- `save_dxf(path=...)`

---

## 3) RC 구조도(철근콘크리트) 절차(요약)

### 3.1 구조 그리드/부재 배치
- 그리드는 건축과 동일(레이어만 S-GRID)
- 기둥/벽/보:
  - 기둥: `create_rectangle` 또는 `create_circle`
  - 보: `create_line` 또는 `create_polyline`
- 부재 라벨: `create_text`

### 3.2 배근(상세/부분)
- 배근선: `create_polyline`
- 리더/주석: `create_leader`
- 동일 패턴 반복: `array_copy`

### 3.3 철근콘크리트 부재 리스트(표)
- 표 틀: `create_rectangle` + `create_line`
- 셀 텍스트: `create_text`
- 필요 시 `generate_bom`로 별도 BOM 생성(도면 밖 문서)

---

## 4) 철골 도면 / 접합부 상세 절차(요약)

### 4.1 부재(부재선/단면 표기)
- 부재선: `create_line`
- 단면 표기 텍스트: `create_text`
- 기준선/중심선: `change_entity_linetype` 또는 레이어 linetype

### 4.2 접합부(볼트/용접/거셋)
- 볼트: `create_bolt_symbol` + `array_copy`
- 거셋/플레이트: `create_polyline` 또는 `create_rectangle`
- 용접 기호/주석: `create_leader` + 텍스트 규칙

---

## 5) QA 루틴(필수)

### 5.1 도면 범위/개체 수
- `get_dxf_summary`
- `count_by_type`
- `count_blocks`

### 5.2 레이어 규칙/정리
- `get_dxf_layers`
- `merge_layers` (잘못 생성된 레이어가 많을 때)

### 5.3 기하학 검증
- `verify_alignment`
- `find_intersections` (벽/보/기둥 충돌)
- `measure_distance` (간격 확인)

### 5.4 결과 캡처
- `zoom_extents` 또는 `zoom_to_bounds`
- `capture_dxf_view`

---

## 6) 권장 표준 레이어 세트(예시)

- A-GRID, A-WALL, A-DOOR, A-WIND, A-TEXT, A-DIMS
- S-GRID, S-COL, S-BEAM, S-WALL, S-REBAR, S-CONN, S-TABLE
- Z-TBD(placeholder), Z-REF(참조)

---

끝.

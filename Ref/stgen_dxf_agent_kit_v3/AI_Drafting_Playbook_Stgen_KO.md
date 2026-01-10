# AI Drafting Playbook (KO) — stgen-dxf-viewer Tool 기준

이 문서는 “AI가 실제로 어떤 순서로 어떤 tool을 호출해 도면을 그릴지”에 초점을 둔 **절차형 플레이북**입니다.  
(Planner가 `drafting_plan`을 만들 때 참조)

---

## 0) 공통 파이프라인(모든 도면 타입)

### 0.1 준비/상태 확인
1. `get_dxf_status`
2. `get_dxf_summary`
3. `get_dxf_layers`
4. (선택) `identify_drawing_type`, `analyze_layer_structure`

### 0.2 레이어/표현 정책 세팅
1. `create_layer`로 표준 레이어 생성 (없는 것만)
2. `set_current_layer`로 활성 레이어 전환
3. (필요 시) `set_layer_visibility`로 참고 레이어 OFF/ON

권장 레이어 예시(프로젝트에 맞게 확정):
- `A-GRID`, `A-WALL`, `A-DOOR`, `A-WINDOW`, `A-TEXT`, `A-DIM`, `A-HATCH`
- `S-GRID`, `S-COL`, `S-BEAM`, `S-SLAB`, `S-REBAR`, `S-STEEL`, `S-NOTE`, `S-DIM`
- `Z-TBD`(불확실 placeholder)
- `X-REF`(참고/임포트)

### 0.3 형상 작성(큰 것 → 작은 것)
- (그리드) → (외곽/주요 벽체·부재) → (내부/개구부) → (상세) → (주석/치수) → (QA/저장)

### 0.4 QA 루프
1. `zoom_extents`
2. `capture_dxf_view` (스냅샷)
3. `count_by_type`, `find_annotations`, `list_all_texts`, `extract_dimensions`
4. 문제 발견 시: `delete_entities` / `edit_text` / `change_entity_layer` / 재치수 등
5. `save_dxf`

---

## 1) 건축 평면도(A-PLAN) 작도 순서(권장)

1. 그리드
   - `set_current_layer(A-GRID)`
   - `create_line`(축선), `create_text`(축명), 필요시 `create_circle`(그리드 버블)
2. 외곽 벽
   - `set_current_layer(A-WALL)`
   - `create_polyline`(외곽), `offset_entity`(벽 두께), `trim_extend`, `join_entities`
3. 내부 벽/코어
   - 외곽과 동일 로직 반복(반복은 macro화 권장)
4. 개구부(문/창)
   - `set_current_layer(A-DOOR/A-WINDOW)`
   - 문틀/창틀: `create_line`/`create_polyline`
   - 문 스윙: `create_arc`
   - 반복 배치는 `array_copy` 활용
5. 해치/재료
   - `set_current_layer(A-HATCH)`
   - `create_hatch`(경계가 닫혀야 함)
6. 실명/치수
   - `set_current_layer(A-TEXT)` : 실명/면적 텍스트 `create_text`
   - `set_current_layer(A-DIM)` : 전체→부분 순서로 `create_dimension`
7. 주석/리더
   - `set_current_layer(A-TEXT)`
   - `create_leader`로 지시선+텍스트
8. QA/저장
   - `capture_dxf_view`, `extract_dimensions`, `list_all_texts`
   - `save_dxf`

---

## 2) 구조 일반도(S-GA) 작도 순서

1. 구조 그리드(S-GRID)
2. 기둥(S-COL)
   - 사각 기둥: `create_rectangle`
   - 원형 기둥: `create_circle`
3. 보(S-BEAM)
   - 중심선→폭 오프셋: `create_line` + `offset_entity`
4. 슬래브/개구부(S-SLAB)
   - 경계 `create_polyline` + 해치 `create_hatch`
5. 부재 표기(S-NOTE/S-TEXT)
   - `create_text`, `create_leader`
6. 치수(S-DIM)
7. QA/저장

---

## 3) 철골 접합부 상세(S-STEEL-CONN) 작도 순서

1. 상세 영역 확보
   - 기존 도면이면 `extract_region`/`clone_region`로 베이스 복제 후 수정
2. 부재 절단/표현
   - `create_polyline`, `trim_extend`, `fillet_chamfer`
3. 플레이트/볼트
   - 플레이트: `create_rectangle`/`create_polyline`
   - 볼트: 반복 `create_circle` 또는 `create_bolt_symbol` + `array_copy`
4. 치수(S-DIM)
5. 용접/주석
   - 전용 tool이 없으면 `create_leader` + 텍스트로 용접기호 표현
6. BOM/표(선택)
   - 간단 BOM은 `generate_bom` 또는 텍스트 테이블 생성
7. QA/저장

---

## 4) RC 배근 상세(S-RC-REBAR) 작도 순서

1. 콘크리트 외곽/피복 기준
   - `create_polyline`(부재), `offset_entity`(피복선)
2. 주근/스터럽 형상
   - 단순 선: `create_line`
   - 굽힘 포함: `create_polyline`(절점), 필요시 `fillet_chamfer`
3. 간격 표기/바마크
   - `create_text`, `create_leader`
4. 치수(S-DIM)
5. 배근표(선택)
   - 텍스트 테이블 또는 `generate_bom` 기반 문서
6. QA/저장

# AI CAD 제도엔진 구현 종합 계획서

**버전**: 1.0
**작성일**: 2026-01-10
**기반**: 엔진개발.md + stgen_dxf_agent_kit_v3 + AI_CAD_Drafting_Note_KO_v3

---

## 1. 프로젝트 개요

### 1.1 목표
AI가 CAD 도면을 **재현 가능한 절차**로 생성할 수 있는 제도 엔진 시스템 구축

### 1.2 핵심 원칙
- **AI는 도면을 "그림"이 아니라 "절차 + 규칙"으로 생성한다**
- **Plan(JSON) 기반 결정론적 실행**: AI가 선 하나씩 즉흥 호출하면 실패율 높음 → Plan만 생성하고 Executor가 실행
- **모델 1:1 원칙**: 스케일링은 뷰포트에서만
- **ByLayer 원칙**: 객체 속성 오버라이드 최소화

### 1.3 현재 보유 자산

| 자산 | 설명 |
|------|------|
| stgen-dxf-viewer MCP | 86개 CAD 함수 제공 (VS Code 확장) |
| stgen_dxf_agent_kit_v3 | Plan 스키마, Executor, Macro Library, QA Engine |
| AI_CAD_Drafting_Note_KO_v3 | 제도 절차/표준 가이드 |

---

## 2. 시스템 아키텍처

### 2.1 전체 파이프라인

```
┌─────────────────────────────────────────────────────────────────┐
│                        AI CAD 제도 파이프라인                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │ Design Input │───▶│  Planner AI  │───▶│ Drafting Plan│       │
│  │   (JSON)     │    │  (LLM)       │    │   (JSON)     │       │
│  └──────────────┘    └──────────────┘    └──────┬───────┘       │
│                                                  │               │
│                      ┌───────────────────────────▼───────────┐   │
│                      │           Plan Validator              │   │
│                      │   (스키마 + 규칙 검증)                 │   │
│                      └───────────────────────────┬───────────┘   │
│                                                  │               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────▼───────┐       │
│  │ Args Adapter │◀───│   Executor   │◀───│ Macro Expand │       │
│  │(키 변환)     │    │(결정론 실행) │    │  (매크로전개)│       │
│  └──────┬───────┘    └──────────────┘    └──────────────┘       │
│         │                                                        │
│         ▼                                                        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │ stgen MCP    │───▶│  DXF 도면    │───▶│  QA Engine   │       │
│  │ Tool Calls   │    │  (결과물)    │    │  (품질검사)  │       │
│  └──────────────┘    └──────────────┘    └──────┬───────┘       │
│                                                  │               │
│                      ┌───────────────────────────▼───────────┐   │
│                      │         QA Report + Patch Plan         │   │
│                      │    (필요시 수정 Plan 생성 후 재실행)   │   │
│                      └───────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 구성 요소 상세

#### A. Design Input (설계 입력)
- **스키마**: `design_input_v3.schema.json`
- **포함 정보**:
  - 프로젝트 메타 (단위, 기준점, 그리드)
  - 층/레벨 정보
  - 부재 리스트 (벽체, 기둥, 보, 슬래브)
  - 개구부 리스트 (문, 창)
  - 철근/철골 정보 (필요시)
  - 도면 축척/시트 크기
  - 표기 규칙

#### B. Planner AI
- **역할**: Design Input → Drafting Plan (JSON only)
- **핵심 규칙**:
  1. 모델은 항상 1:1
  2. 축척은 뷰포트에서만
  3. ByLayer 강제
  4. 누락값은 질문 대신 `assumptions`에 기록 + `Z-TBD` 레이어에 placeholder

#### C. Drafting Plan
- **스키마**: `drafting_plan_stgen_v2.schema.json`
- **구조**:
```json
{
  "version": "stgen-plan-v2",
  "meta": { "drawing_type": "A_FLOOR_PLAN", "units": "mm", ... },
  "assumptions": ["누락/가정 사항 기록"],
  "policy": {
    "avoid_scale": true,
    "layer_policy": "SET_CURRENT_LAYER",
    "forbid_tools": []
  },
  "vars": { "extents": {"min":[0,0], "max":[12000,8000]} },
  "sequence": [
    { "id": "01", "tool": "create_layer", "args": {...} },
    { "id": "02", "macro": "macro:draw_grids", "args": {...} },
    ...
  ]
}
```

#### D. Executor
- **역할**: Plan을 순서대로 실행
- **기능**:
  1. Macro 전개 (macro_library.py)
  2. 변수 치환 (`$var` → 실제값)
  3. Args 변환 (canonical → 실제 MCP args)
  4. MCP Tool Call 순차 실행
  5. `$LAST`, `$LAST_IDS` 변수 자동 갱신

#### E. QA Engine
- **역할**: 도면 품질 자동 검사
- **사용 Tool**:
  - `get_dxf_summary`, `get_dxf_layers`
  - `list_all_texts`, `extract_dimensions`
  - `detect_symbols`, `capture_dxf_view`
- **검사 항목**:
  - 필수 레이어 존재 여부
  - Placeholder 텍스트 잔존 여부 (TBD, TODO)
  - 최소 치수 개수
  - 텍스트/치수 겹침
  - ByLayer 준수

---

## 3. 구현 단계별 계획

### Phase 1: 기반 환경 구축 (즉시 실행 가능)

#### 1.1 Args Map 확정
- **목표**: stgen MCP 실제 args 키 확인 및 변환 맵 완성
- **방법**: `args_probe.py` 활용하여 대표 tool 테스트

```bash
# 실행 예시
python src/args_probe.py --cases examples/args_probe_cases.json
```

- **확인 필요 Tool** (우선순위):
  - `create_line`, `create_polyline`, `create_circle`, `create_arc`
  - `create_text`, `create_dimension`
  - `create_layer`, `set_current_layer`
  - `offset_entity`, `copy_entities`, `move_entities`
  - `save_dxf`, `capture_dxf_view`

#### 1.2 MCP Client 연결
- **위치**: `src/stgen_plan_executor.py` → `McpClient.call()`
- **연결 방식**: VS Code Extension의 MCP 서버와 직접 통신
- **현재 상태**: dry-run 모드로 구현됨

#### 1.3 기본 테스트
```bash
# 스키마 검증
python src/plan_validator.py --schema schemas/drafting_plan_stgen_v2.schema.json \
  --plan examples/drafting_plan_demo_A101_macro.json

# Dry-run 실행
python src/stgen_plan_executor.py \
  --plan examples/drafting_plan_demo_A101_macro.json \
  --args-map args_map/args_map_identity.json \
  --dry-run
```

### Phase 2: 핵심 Macro 구현 강화

#### 2.1 현재 구현된 Macro
| Macro | 기능 | 상태 |
|-------|------|------|
| `macro:setup_layers` | 레이어 일괄 생성 | 완료 |
| `macro:draw_grids` | 그리드 + 버블 + 라벨 | 완료 |
| `macro:draw_walls` | 벽체 (boundary 기반) | 완료 |
| `macro:draw_openings` | 문/창 심볼 | 기본 |
| `macro:add_room_labels` | 실명 + 면적 | 완료 |
| `macro:add_dimensions_basic` | 기본 치수 | 완료 |
| `macro:member_schedule_table` | 부재리스트 표 | 완료 |
| `macro:qa_snapshot` | QA 스냅샷 | 완료 |
| `macro:fit_and_save` | zoom + 저장 | 완료 |
| `macro:steel_connection_detail` | 철골 접합부 | 기본 |
| `macro:rc_rebar_detail` | RC 배근 | 기본 |

#### 2.2 추가 구현 필요 Macro

| Macro | 우선순위 | 설명 |
|-------|---------|------|
| `macro:draw_wall_hatch` | 높음 | 벽체 포쉐/해치 |
| `macro:door_swing` | 높음 | 문 스윙 호 정밀화 |
| `macro:window_symbol` | 중간 | 창호 2중선 표현 |
| `macro:steel_bolt_pattern` | 중간 | 볼트 배열 패턴 |
| `macro:rebar_spacing_mark` | 중간 | 철근 간격 표기 (D10@200) |
| `macro:weld_symbol` | 낮음 | 용접 기호 (AWS/ISO) |
| `macro:section_callout` | 중간 | 단면 콜아웃 기호 |
| `macro:detail_callout` | 중간 | 상세 콜아웃 기호 |

### Phase 3: 도면 타입별 템플릿 완성

#### 3.1 지원 도면 타입

| 타입 코드 | 도면 종류 | 템플릿 상태 |
|----------|---------|-----------|
| A_FLOOR_PLAN | 건축 평면도 | 기본 완료 |
| A_ELEVATION | 건축 입면도 | 미구현 |
| A_SECTION | 건축 단면도 | 미구현 |
| S_GA | 구조 일반도 | 미구현 |
| S_RC_REBAR | RC 배근도 | 기본 |
| S_STEEL_FRAME | 철골 일반도 | 미구현 |
| S_STEEL_CONN | 철골 접합부 상세 | 기본 |
| S_MEMBER_SCHEDULE | 부재리스트/스케줄 | 기본 완료 |

#### 3.2 각 도면별 절차 (AI_CAD_Drafting_Note 기반)

**건축 평면도 (A_FLOOR_PLAN)**:
1. 그리드 선 + 버블 배치
2. 외벽 기준선 → Offset → 벽체 윤곽
3. 내벽 작성 → 코너 Fillet/Trim
4. 기둥/코어 형상
5. 개구부 Trim/Break → 문/창 블록
6. 계단 형상 + 화살표
7. 해치/포쉐 적용
8. 실명/면적 태그
9. 치수 배치 (전체→그리드→개구부→내부)
10. 콜아웃 배치
11. 레이아웃/뷰포트 구성
12. QA 체크

**구조 일반도 (S_GA)**:
1. 구조 그리드 + 축선 번호
2. 기둥 배치 + 부재명 + 규격
3. 보/거더 중심선 + 보명 + 규격
4. 슬래브/개구부 외곽
5. 기초 (해당시)
6. 치수 배치
7. 상세 참조 콜아웃
8. QA

**RC 배근도 (S_RC_REBAR)**:
1. 부재 외곽/피복선
2. 주근 표시 + 표기 (4-D25)
3. 스터럽/후프 패턴
4. 간격 표기 (D10@100)
5. 바 마크 부여 (B1, B2...)
6. 스케줄 자동 집계
7. QA

**철골 접합부 상세 (S_STEEL_CONN)**:
1. 부재 절단/투영 표현
2. 플레이트/스티프너/거셋 작성
3. 볼트 구멍 패턴 + 규격/수량
4. 볼트 치수 체계 (게이지, 피치, 에지)
5. 용접 기호 배치
6. 부품 콜아웃 + BOM
7. QA

### Phase 4: QA 시스템 강화

#### 4.1 현재 QA 규칙
- `rule_required_layers`: 필수 레이어 검사
- `rule_placeholder_texts`: TBD/TODO 텍스트 잔존
- `rule_min_dimension_count`: 최소 치수 개수
- `rule_no_entities_on_layer`: 특정 레이어 엔티티 검사

#### 4.2 추가 QA 규칙 (구현 필요)

| 규칙 | 설명 | 사용 Tool |
|------|------|----------|
| `rule_text_overlap` | 텍스트/치수 겹침 감지 | `find_annotations`, bounds 비교 |
| `rule_dimension_duplicate` | 치수 중복 검사 | `extract_dimensions` |
| `rule_layer_naming` | 레이어 명명 규칙 준수 | `get_dxf_layers` |
| `rule_bylayer_compliance` | ByLayer 속성 검사 | `find_entities` + properties |
| `rule_grid_alignment` | 그리드 정합성 | `analyze_pattern` |
| `rule_symbol_completeness` | 기호 누락 검사 | `detect_symbols` |
| `rule_scale_violation` | 스케일 위반 검사 | 엔티티 bounds 분석 |

### Phase 5: 고급 기능

#### 5.1 블록 시스템 활용
- 표준 블록 라이브러리 구축 (문, 창, 그리드버블, 레벨마크, 용접기호 등)
- 블록 속성(Attributes)으로 메타데이터 관리
- 데이터 추출 → 스케줄 자동화

#### 5.2 레이아웃/뷰포트 지원
현재 stgen MCP에는 레이아웃/뷰포트 직접 생성 기능이 없음
- **대안 1**: DXF 파일 직접 수정 (ezdxf 등)
- **대안 2**: 템플릿 DXF에 뷰포트 미리 설정 후 모델만 수정

#### 5.3 Xref 지원
외부참조 관리 기능 (현재 MCP에 없음)
- 기준도(그리드/코어) 별도 파일 분리
- 상대경로 관리

---

## 4. stgen MCP Tool 활용 전략

### 4.1 Tool 분류별 활용

#### 도면 분석 (Plan 시작 전)
```
get_dxf_status → 파일 상태 확인
get_dxf_summary → 전체 요약 (엔티티 수, 레이어, 범위)
get_dxf_layers → 레이어 목록
identify_drawing_type → 도면 유형 자동 판별
```

#### 개체 생성 (주요)
```
create_layer → 레이어 생성 (ByLayer 운영 필수)
set_current_layer → 현재 레이어 설정
create_line, create_polyline → 선/폴리라인
create_circle, create_arc → 원/호
create_rectangle → 직사각형
create_text → 텍스트
create_dimension → 치수
create_hatch → 해치
create_leader → 지시선
create_bolt_symbol → 볼트 기호
create_center_mark → 중심 마크
```

#### 개체 수정
```
offset_entity → 평행 복사 (벽체 두께 등)
copy_entities, move_entities → 복사/이동
rotate_entities, mirror_entities → 회전/대칭
array_copy → 배열 복사 (볼트 패턴 등)
trim_extend → 트림/연장
fillet_chamfer → 필렛/챔퍼
```

#### QA/검사
```
extract_dimensions → 치수 추출
list_all_texts → 텍스트 목록
detect_symbols → 기호 감지
find_annotations → 주석 검색
capture_dxf_view → 스냅샷
```

### 4.2 주의사항

1. **scale_entities/scale_region 사용 최소화**
   - 심볼/표만 예외
   - 건축/구조 형상은 절대 1:1 유지

2. **offset_entity는 entityRef 필요**
   - position 또는 handle로 참조
   - `$LAST` 변수 활용 (직전 생성 엔티티)

3. **레이어 운영**
   - 개체 생성 전 반드시 `set_current_layer`
   - 색/선종류는 레이어 정책으로 통일

---

## 5. 실행 로드맵

### 단기 (1주)
- [ ] Args Map 확정 (실제 MCP args 키 매핑)
- [ ] McpClient 연결 구현
- [ ] 건축 평면도 Plan 실행 테스트
- [ ] 기본 QA 파이프라인 동작 확인

### 중기 (2-4주)
- [ ] 추가 Macro 구현 (wall_hatch, door_swing, window_symbol)
- [ ] 구조 일반도 템플릿 완성
- [ ] RC 배근도 Macro 강화
- [ ] 철골 접합부 Macro 강화
- [ ] QA 규칙 확장

### 장기 (1-2개월)
- [ ] 모든 도면 타입 템플릿 완성
- [ ] 블록 라이브러리 구축
- [ ] 레이아웃/뷰포트 대안 구현
- [ ] 사용자 피드백 기반 개선
- [ ] 문서화 및 가이드 작성

---

## 6. 파일 구조

```
Drawing_Engine/
├── .mcp.json                    # MCP 서버 설정
├── 531_CAD_Drawing_Moore_Industries.dxf  # 테스트 도면
├── 엔진개발.md                   # 개발 문서 (원본)
├── AI_CAD_Engine_Implementation_Plan.md  # 이 문서
│
├── Ref/                         # 참조 자료
│   ├── AI_CAD_Drafting_Note_KO_v3.pdf
│   ├── mcp_cad_agent_kit_v1/
│   ├── stgen_dxf_agent_kit_v2/
│   └── stgen_dxf_agent_kit_v3/   # 주 사용 키트
│       ├── schemas/
│       │   ├── design_input_v3.schema.json
│       │   └── drafting_plan_stgen_v2.schema.json
│       ├── src/
│       │   ├── stgen_plan_executor.py
│       │   ├── macro_library.py
│       │   ├── args_adapter.py
│       │   ├── qa_engine.py
│       │   └── qa_rules.py
│       ├── templates/
│       ├── examples/
│       ├── args_map/
│       └── docs/
│
└── src/                         # 실제 구현 (향후)
    ├── executor/
    ├── macros/
    ├── qa/
    └── templates/
```

---

## 7. 핵심 성공 요인

1. **Plan 기반 결정론 실행**
   - AI가 즉흥 작도하면 실패
   - Plan(JSON)만 생성, Executor가 결정론적 실행

2. **Macro로 반복 작업 고정**
   - 그리드, 벽, 개구부, 치수, 스케줄 등
   - AI 흔들림 방지

3. **QA 루프 자동화**
   - 실행 후 자동 검사
   - 문제 발견 시 Patch Plan 생성 → 재실행

4. **Args 변환 레이어**
   - canonical args → 실제 MCP args
   - 서버 변경에도 Plan 스키마 유지

5. **점진적 확장**
   - 단순 도면부터 시작 (건축 평면)
   - 검증 후 복잡 도면으로 확장

---

## 8. 다음 단계 (즉시 실행)

### 8.1 Args 프로브 실행
```bash
cd /Users/hi/2026Coding_Prj/Drawing_Engine/Ref/stgen_dxf_agent_kit_v3
python src/args_probe.py --cases examples/args_probe_cases.json
```

### 8.2 McpClient 연결 구현
`src/stgen_plan_executor.py`의 `McpClient.call()` 메서드를
실제 VS Code Extension MCP 통신으로 교체

### 8.3 테스트 Plan 실행
```bash
python src/stgen_plan_executor.py \
  --plan examples/drafting_plan_demo_A101_macro.json \
  --args-map args_map/args_map_identity.json
```

---

**문서 끝**

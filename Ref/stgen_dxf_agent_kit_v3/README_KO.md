# stgen-dxf-viewer MCP 기반 CAD Agent Kit v3 (Plan → Execute → QA)

버전: v3  
생성일: 2026-01-07

이 키트는 **stgen-dxf-viewer MCP 서버(86개 함수)**를 그대로 사용해,
LLM이 “선 하나씩 즉흥적으로” 그리다가 망가지지 않도록 다음 구조로 운영합니다.

- **Planner(LLM)**: 설계/요구사항(JSON 입력) → **drafting_plan(JSON)** 생성 (오직 JSON)
- **Executor(결정론)**: drafting_plan을 순서대로 MCP tool call 실행
- **QA Engine(결정론 +/ LLM)**: 도면 상태를 분석/스냅샷/치수추출 등으로 검사 → 리포트/패치 플랜

---

## 0) 왜 Plan(JSON) 방식이 필요한가

LLM이 직접 `create_line`을 즉흥적으로 수백 번 호출하면,
- 레이어 누락, 반복 실수, 스케일 혼란, 치수 누락, 도면 정합성 붕괴가 자주 발생합니다.

Plan 방식에서는:
- LLM은 **절차(순서)**만 만든다.
- 실제 작도는 **엔진(Executor)이 결정론적으로** 실행한다.
- QA 결과로 **수정 플랜만** 반복한다.

---

## 1) 핵심 파일

### 스키마
- `schemas/design_input_v3.schema.json`  
  설계/요구 데이터를 정규화하기 위한 입력 스키마
- `schemas/drafting_plan_stgen_v2.schema.json`  
  stgen 86개 tool + macro step을 포함하는 실행 계획 스키마

### 실행
- `src/stgen_plan_executor.py`  
  plan 실행기 (dry-run 기본)
- `src/args_adapter.py`  
  **canonical args → 실제 MCP args** 변환기 (args_map 기반)
- `src/plan_validator.py`  
  스키마 + 규칙(금지 tool/레이어 정책/스케일 정책 등) 검증기

### QA
- `src/qa_engine.py`  
  get_dxf_summary, get_dxf_layers, extract_dimensions, list_all_texts, detect_symbols 등을 조합해 QA 리포트 생성
- `src/qa_rules.py`  
  규칙 기반 검사 함수 모음

### 프롬프트
- `prompt_templates_ko.md`  
  Planner/QA/Patch 프롬프트 템플릿(오직 JSON 출력 강제)

### args 매핑
- `args_map/args_map_identity.json`  
  변환 없음(기본)
- `args_map/args_map_example_rename.json`  
  예: insert → position 같은 키 rename 예시

---

## 2) 빠른 시작

### (1) 예제 plan 검증
```bash
python src/plan_validator.py --schema schemas/drafting_plan_stgen_v2.schema.json --plan examples/drafting_plan_demo_A101_macro.json
```

### (2) dry-run 실행(호출 로그 확인)
```bash
python src/stgen_plan_executor.py --plan examples/drafting_plan_demo_A101_macro.json --args-map args_map/args_map_identity.json --dry-run
```

### (3) 실제 MCP 호출 연결
`src/stgen_plan_executor.py`의 `McpClient.call()`만 당신 orchestrator에 맞춰 구현하면 됩니다.

---

## 3) 중요한 운영 원칙 (강제 권장)

1. **스케일(scale_entities/scale_region) 사용 최소화**
   - 심벌/표만 예외. 건축/구조 형상은 1:1 유지.
2. **ByLayer 운영**
   - create 전에 `set_current_layer`로 레이어 지정.
   - 색/선종류는 레이어 정책으로 통일.
3. **반복 작도는 macro로 고정**
   - 그리드, 벽, 개구부, 기본 치수, 스케줄 표, QA 스냅샷 등

---

## 4) 당신 MCP 서버의 “실제 args 키”가 다를 때

이 키트는 tool args를 **권장 canonical 포맷**으로 작성합니다.
만약 stgen MCP가 다른 키를 요구한다면:

- `args_map/*.json`에 rename/constant/transform 규칙을 추가하거나
- `src/args_adapter.py`에 변환 함수를 확장하세요.

---

## 5) 다음에 확장할 때 추천

- 도면 타입별 macro 세분화(문/창 블록, 문 스윙, 해치 규칙, 철근 정착/후크, 볼트 패턴)
- QA 규칙 강화(레이어 위반, 텍스트 겹침, 치수 누락, 반복 패턴 이상)
- 스케줄 자동화(블록 속성/데이터 추출이 없다면 텍스트 테이블 생성 + generate_bom 연계)

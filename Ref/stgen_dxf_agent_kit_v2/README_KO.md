# stgen-dxf-viewer Agent Kit v2 (KO)

이 키트는 **stgen-dxf-viewer MCP 서버(86 tools)** 를 대상으로, LLM이 “직접 선을 하나씩 그리다 실패”하는 문제를 줄이기 위해
**Plan(JSON DSL) → 결정론 실행(Executor) → QA 루프** 형태로 운영할 수 있게 만든 템플릿/스키마/실행기 샘플입니다.

> 핵심 아이디어  
> - LLM은 “도면을 어떻게 그릴지”를 **drafting_plan(JSON)** 으로만 출력 (설명 금지)  
> - 실행은 코드가 **stgen MCP tool을 순서대로 호출** (결정론)  
> - QA는 stgen의 분석/조회 도구로 검증하고, 필요한 경우 plan 패치만 생성

---

## 폴더 구성

- `schemas/design_input_v2.schema.json`  
  설계/요구 입력(JSON) 스키마: 그리드/레벨/벽/개구부/구조/철골접합/철근/시트요구 등

- `schemas/drafting_plan_stgen_v1.schema.json`  
  stgen 86 tools + macro를 포함한 실행 계획(JSON) 스키마

- `src/stgen_plan_executor.py`  
  plan을 읽어 **stgen MCP 도구를 호출**하는 실행기 샘플 (실제 MCP 호출부는 `McpClient`에 연결)

- `src/macro_library.py`  
  `macro:*` 단계를 primitive tool-call로 전개하는 매크로 라이브러리(샘플)

- `src/plan_validator.py`  
  스키마 검증 외에 “현장 규칙(스케일/레이어/ByLayer 등)”을 추가 점검하는 검증기(샘플)

- `prompt_templates_ko.md`  
  Planner / QA 에이전트 프롬프트 템플릿 (stgen tool 기반)

- `templates/`  
  도면 타입별 플랜 스켈레톤(JSON) — macro 중심

- `examples/`  
  최소 입력/플랜/확장 플랜 예시

---

## 추천 운영 파이프라인

1) **design_input 확보**
- 사용자 입력, DB/BIM, CSV 등을 `design_input`으로 정규화
- `design_input_v2.schema.json`으로 1차 검증

2) **Planner LLM → drafting_plan 생성**
- `prompt_templates_ko.md`의 Planner Prompt 사용
- 입력: design_input JSON
- 출력: drafting_plan JSON (오직 JSON)

3) **plan 검증**
- JSON Schema + `src/plan_validator.py` 규칙 검사

4) **실행**
- `src/stgen_plan_executor.py`로 실행 (macro는 실행 전에 전개)

5) **QA 루프**
- `get_dxf_summary`, `count_by_type`, `find_annotations`, `extract_dimensions`, `get_region_bounds`, `capture_dxf_view` 등으로 검사
- QA Agent가 “수정용 plan patch”만 생성 → 재실행

---

## IMPORTANT: stgen은 레이아웃/뷰포트가 없다면?

stgen의 MCP 목록에는 AutoCAD의 PaperSpace(Layout/Viewport) 개념이 직접 노출되어 있지 않습니다.
따라서 이 키트는 2가지 모드를 지원합니다.

- **Mode A (권장/단순): DXF 한 장 = 한 시트**
  - 시트마다 별도의 DXF로 저장 (`save_dxf` 또는 `export_entities`)
  - 스케일은 “복제+축소”가 아니라, **모델 1:1 유지** + 시트 영역에 필요한 표현만 그리는 방식 권장

- **Mode B (대체): 모델 공간 내에 ‘시트 영역’을 만들어 배치**
  - title block / border를 모델에 직접 그리고
  - 필요 시 `clone_region` + `scale_region`으로 뷰를 축소 복제해 배치 (권장하지 않지만 DXF 기반 워크플로에서 사용 가능)

템플릿은 기본적으로 Mode A에 맞춰 작성되어 있습니다.

---

## 빠른 시작

```bash
python -m pip install jsonschema
python src/plan_validator.py examples/drafting_plan_demo_A101_macro.json
```

실행(실제 MCP 연결 필요):

```bash
python src/stgen_plan_executor.py examples/drafting_plan_demo_A101_macro.json --dry-run
```

`--dry-run`은 MCP 호출 대신 호출 내용을 출력합니다.

---

## 당신이 해야 하는 최소 작업

- `src/stgen_plan_executor.py`의 `McpClient.call(tool_name, args)`를
  **당신의 MCP 실행 환경(예: claude-code, 자체 orchestrator)** 에 연결

끝.

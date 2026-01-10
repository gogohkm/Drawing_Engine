# MCP CAD Agent Kit v1 (KO)

이 폴더는 다음을 포함합니다.

- `schemas/design_input_v1.schema.json` : 설계/요구 입력 스키마(그리드/레벨/부재/요청 시트)
- `schemas/drafting_plan_v1.schema.json` : CAD 실행 계획(작업 절차) 스키마
- `templates/` : 도면 타입별 플랜 스켈레톤(JSON)
- `examples/design_input_demo.json` : 최소 예시 입력
- `prompt_templates_ko.md` : Planner/Executor/QA 프롬프트 템플릿
- `executor_adapter_sample.py` : 실행기/어댑터 샘플(당신의 엔진에 맞게 구현 필요)

---

## 추천 파이프라인(실전)

1) **design_input 확보**
- 사용자 입력 또는 BIM/CSV/DB 등에서 `design_input` JSON 생성
- `design_input_v1.schema.json`으로 1차 검증

2) **Planner AI → drafting_plan 생성**
- `prompt_templates_ko.md`의 Planner System Prompt 적용
- 입력: design_input JSON
- 출력: drafting_plan JSON (오직 JSON)

3) **drafting_plan 검증**
- `drafting_plan_v1.schema.json`으로 구조 검증
- 누락 값/모순은 `assumptions`를 보고 후처리(또는 QA Agent로 수정)

4) **결정론 실행기**
- `executor_adapter_sample.py`를 기반으로
  - 당신의 CAD 엔진 API를 `CadAdapter`에 연결
  - macro(op가 `macro:`로 시작하는 것)를 구현하거나
  - Planner가 macro를 쓰지 않도록 제한하여 "완전 전개된 op 리스트"만 생성하도록 운영

5) **QA → 수정 루프**
- 엔진에서 `qa_check`를 구현해 결과를 반환
- 필요시 QA Agent가 수정 op 목록을 생성 → 재실행

---

## macro 구현 순서(추천)

1) `macro:create_sheet_with_viewport` (타이틀블록 + 뷰포트 생성 + 잠금)
2) `macro:draw_grids` (그리드선 + 버블 + 축선 문자)
3) `macro:draw_arch_walls` (벽 중심선/두께 기반 양쪽 offset, 코너 처리)
4) `macro:insert_doors_windows` (개구부 생성 + 문/창 블록 삽입)
5) `macro:build_table_from_block_attributes` (속성 수집 → 정렬/그룹 → 테이블 작성)

이 5개만 구현해도 AI 제도 성공률이 크게 올라갑니다.

---

## 레이어/블록 라이브러리 운영 팁

- 레이어는 “도메인별 최소 세트”를 템플릿으로 고정하세요.
- 블록은 반드시:
  - 기준점(삽입점) 규칙,
  - 축척 단위(mm),
  - 속성(Attribute) 키
  를 표준화해야 스케줄 자동화가 됩니다.

---

## 버전 규칙

- 스키마/DSL은 `version: 1.0.x` 형태로 관리하세요.
- Planner 프롬프트도 버전 문자열을 포함해 “어떤 스키마에 맞춰야 하는지” 항상 명시하세요.

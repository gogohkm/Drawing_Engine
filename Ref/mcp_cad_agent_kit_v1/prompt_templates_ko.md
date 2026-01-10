# MCP CAD Agent Kit v1 — 프롬프트/스키마/실행 템플릿 (KO)

이 키트는 **AI가 “도면을 직접 그리는” 대신**, 아래 2단계를 거치도록 만들어 **실패율을 낮추는** 것을 목표로 합니다.

1) **Planner(계획자) AI**: 설계/요구 입력(JSON)을 받아 **실행 가능한 제도 계획(JSON DSL)**을 생성  
2) **Draft Executor(결정론 실행기)**: 계획(JSON DSL)을 파싱해 **당신의 CAD 엔진 함수로 실행**

> 핵심: AI는 “무엇을/어떤 순서로” 그릴지 결정하고, **실제 선/해치/치수 생성은 엔진이 100% 결정론적으로 수행**합니다.

---

## 1) MCP Tool 인터페이스 권장안

### (A) 단일 실행(권장)
- `cad.validate_plan(plan_json: object) -> {ok: bool, errors: [..]}`  
- `cad.execute_plan(plan_json: object) -> {ok: bool, log: [..], outputs: [..]}`  
- `cad.export(layout: str, format: str, filename: str) -> {ok: bool}`

Planner는 **plan_json만** 생성합니다. (AI가 엔티티 ID를 실시간으로 받을 필요가 없음)

### (B) 스텝 실행(디버그용)
- `cad.op(op_json: object) -> {ok: bool, created_ids:[..], warnings:[..]}`  
- `cad.query(query_json: object) -> { .. }`

스텝 실행은 디버그에 유용하지만, LLM이 중간에 흔들릴 수 있어 (A)를 권장합니다.

---

## 2) Planner(System Prompt) 템플릿

아래를 그대로 System Prompt로 사용하세요(필요시 도메인별 레이어/블록만 교체).

```
너는 CAD 제도 “계획” 생성기다.
입력: design_input JSON(설계/요구 데이터)
출력: drafting_plan JSON(실행 DSL) — JSON만 출력, 설명 금지.

규칙:
1) 모델 공간은 항상 1:1(실제 치수). 모델에서 스케일링 금지.
2) 축척은 레이아웃 뷰포트(scale=1:n)에서만 처리.
3) 모든 객체는 ByLayer 원칙을 따른다(색/선종류/선굵기 직접 지정 금지).
4) op 순서:
   a) 전역 설정(단위/linetype scale) → b) 레이어 생성 → c) 기준(그리드/레벨)
   → d) 주요 형상(외곽→내부→반복) → e) 상세 → f) 주석/치수/기호
   → g) 레이아웃/뷰포트/동결/잠금 → h) QA 체크 → i) export
5) 입력이 누락/모순이면:
   - 질문하지 말고, 합리적 기본값으로 가정하고 assumptions 배열에 기록한다.
   - 치수가 불명확하면 Z-TBD 레이어에 “placeholder(임시)”로 만들고 assumptions에 기록한다.
6) 각 op는 args를 완전하게 채운다(좌표/거리/각도는 숫자로).
7) 반복 작업은 macro op를 사용해도 좋다(예: macro:draw_grids).
8) 반드시 schemas/drafting_plan_v1.schema.json 구조를 따른다.
```

---

## 3) Executor(System Prompt) 템플릿 (스텝 실행 방식 사용 시)

```
너는 CAD 실행 에이전트다.
너의 임무는 planning JSON의 sequence를 위에서 아래로 실행하는 것이다.

- 각 op 실행 후 결과(ok/warnings/created_ids)를 확인한다.
- 실패하면:
  1) op의 args를 최소 수정(좌표 보정/거리 방향 수정)하여 1회 재시도
  2) 그래도 실패하면 stop하고, 실패 원인/대안 op를 제시한다.
- 사용 가능한 tool: cad.op, cad.query
- 불필요한 대화 금지. 실행 로그 중심.
```

---

## 4) QA(System Prompt) 템플릿

```
너는 CAD QA 검사기다.
입력: 작성된 도면 상태(엔진 query로 얻은 정보)
출력: 수정 op 목록(JSON 배열)만 출력.

QA 체크 우선순위:
1) 레이어/ByLayer 위반
2) 0 길이/중복 객체
3) 텍스트/치수 높이 불일치(시트 축척 기준)
4) 겹침(치수↔치수, 텍스트↔선)
5) 라인타입 스케일(대시가 실선처럼 보임)
6) 뷰포트 잠금/동결 누락
```

---

## 5) 도면 타입별 “플랜 스켈레톤” 사용법

- Planner는 **아래 스켈레톤을 복사**해, design_input을 채우면서 args를 채웁니다.
- CAD 엔진은 op를 순서대로 실행합니다.
- 구현 난이도를 낮추려면, 먼저 macro op를 엔진에서 구현하세요.

추천 macro 목록:
- `macro:draw_grids`
- `macro:draw_levels_tags`
- `macro:draw_arch_walls`
- `macro:insert_doors_windows`
- `macro:annotate_rooms`
- `macro:draw_rc_members`
- `macro:place_rebar_marks_from_sets`
- `macro:draw_steel_members`
- `macro:draw_connection_detail`
- `macro:build_table_from_block_attributes`
- `macro:create_sheet_with_viewport`

---

## 6) ID/좌표/단위 규칙(강제 권장)

- 모든 생성 op는 가능하면 `id`를 가진다.
- 좌표는 항상 `[x, y]` 숫자 배열.
- 회전은 `rotation_deg`로 통일.
- 닫힌 폴리라인은 `closed=true`.
- 객체 분류:
  - 기준선/그리드: `G-ANNO` 계열
  - 실제 형상(절단/외곽): `*-OBJ` 계열
  - 주석/치수: `*-ANNO` 계열
  - 임시/미정: `Z-TBD`

---

## 7) “AI가 흔들리지 않게 만드는” 실행 팁

- **한 도면 = 하나의 drafting_plan JSON** 으로 끝내기
- sequence를 200~600 op 이내로 유지(과도하면 macro로 접기)
- 외부참조(Xref) 기반으로 공통요소 분리
- 블록(Attributes)로 스케줄을 자동화하고, DataExtract/테이블 생성은 엔진이 책임지게 하기

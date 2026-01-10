# Integration Checklist (KO)

이 키트를 당신 시스템에 붙이기 위한 체크리스트입니다.

---

## 1) MCP 호출부 연결

- [ ] `src/stgen_plan_executor.py` 의 `McpClient.call(tool,args)`를 실제 MCP 호출로 교체
- [ ] 동일하게 `src/qa_engine.py`, `src/args_probe.py`의 McpClient도 교체 또는 공용 모듈화

---

## 2) Tool args 스키마 확인

- [ ] 테스트 DXF 사본에서 `args_probe.py` 실행
- [ ] 에러 메시지로 실제 필수 키/포맷 파악
- [ ] `args_map/*.json`에 rename/drop/add 규칙 작성
- [ ] (필요 시) `ArgsAdapter`에 변환 로직 추가(좌표 포맷 등)

---

## 3) Plan/Prompt 운영

- [ ] Planner는 **항상 JSON만 출력**(설명 금지)
- [ ] plan은 `src/validate_json.py`로 스키마 통과
- [ ] `policy.avoid_scale = true` 유지(원칙)
- [ ] 반복 작업은 macro로 고정(그리드/벽/스케줄/QA)

---

## 4) QA 루프

- [ ] 실행 후 `qa_engine.py`로 `qa_report` 생성
- [ ] LLM Patch Planner가 patch_plan 생성(JSON만)
- [ ] patch_plan 실행 → 재 QA

---

## 5) 성능/안정성 팁

- 도면이 크면: 범위 기반(find/erase/extract)을 적극 사용
- 반복 심벌은: `create_block` + `insert_block`로 전환
- 치수/텍스트는: 마지막에 몰아서 배치(겹침 최소화)

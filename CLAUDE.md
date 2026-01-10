# Drawing Engine - Claude Code 세션 가이드

## 세션 시작 시 필수 작업

새 대화를 시작할 때 아래 명령을 실행하여 지식을 로드합니다:

```bash
cd /Users/hi/2026Coding_Prj/Drawing_Engine/knowledge/engine && python claude_helper.py session_start
```

이 명령은 다음을 반환합니다:
- 사용 가능한 시퀀스 목록
- 최근 성공/실패 기록
- 주의사항 및 팁
- **활성 작업 목록** (진행 중이던 작업)

## 주요 명령어

### 시퀀스 조회
```bash
python claude_helper.py list_sequences
python claude_helper.py get_sequence simple_room
```

### 요소 패턴 조회
```bash
python claude_helper.py get_pattern grid
python claude_helper.py get_pattern wall
python claude_helper.py get_pattern dimension
```

### 성공 기록
```bash
python claude_helper.py record_success \
  "작업설명" \
  "접근법" \
  "성공요인1,성공요인2" \
  '{"LINE":6,"CIRCLE":3}' \
  "태그1,태그2" \
  "메모"
```

### 실패 기록
```bash
python claude_helper.py record_failure \
  "작업설명" \
  "에러내용" \
  "원인" \
  "해결방법" \
  "예방책" \
  "태그1,태그2"
```

## 맥락 유지 시스템 (Context Manager)

복잡한 작업 중 맥락을 잃어버리는 문제를 방지합니다.

### 🚀 추천 워크플로우 (자동화)

대량의 엔티티를 다룰 때는 `create_task_auto`를 사용하면 모든 설정이 자동으로 됩니다:

```bash
# 1. 엔티티 선택 후 자동 작업 생성
python claude_helper.py create_task_auto \
  "redraw" \
  "선택 영역 다시 그리기" \
  '엔티티_JSON' \
  '0' '-15' \
  '20'  # batch_size
# → task_id, total_entities, total_steps, batches_info 반환

# 2. 실행 전 검증
python claude_helper.py validate <task_id>
# → {valid: true/false, issues: [], suggestions: []}

# 3. 단계별 실행 + 체크포인트
python claude_helper.py checkpoint <task_id> 1 in_progress
# ... MCP 도구 실행 ...
python claude_helper.py checkpoint <task_id> 1 completed

# 4. 맥락 확인 (주기적)
python claude_helper.py auto_check <task_id>
```

### 자동 작업 생성의 장점

`create_task_auto`는 다음을 자동으로 처리합니다:
- 작업 생성
- 좌표 변환 계산 (dx, dy 적용)
- 엔티티 타입별 그룹화
- 배치 분할 (기본 20개씩)
- 실행 계획 등록

### 수동 워크플로우 (필요시)

#### 1. 작업 생성 (시작 전)
```bash
python claude_helper.py create_task copy_region "도면 영역 복사"
# → task_id 반환: copy_region_20260111_014004_3d982e
```

#### 2. 활성 작업 확인
```bash
python claude_helper.py list_tasks
```

#### 3. 맥락 복구 (잊어버렸을 때)
```bash
python claude_helper.py restore <task_id>
```
→ 진행 상황, 남은 작업, 계산된 좌표 등 전체 복구

#### 4. 체크포인트 기록
```bash
python claude_helper.py checkpoint <task_id> <step> <status>
# status: in_progress, completed, failed
```

#### 5. 남은 작업 조회
```bash
python claude_helper.py get_remaining <task_id>
python claude_helper.py get_step_tools <task_id> <step>
```

### 워크플로우 비교

**자동 (추천)**:
```
get_selected_entities
     ↓
create_task_auto (엔티티, dx, dy)
     ↓
validate → 문제없으면 실행
     ↓
[단계별 실행]
  ├── checkpoint(step, "in_progress")
  ├── MCP 도구 호출 (배치 단위)
  └── checkpoint(step, "completed")
```

**수동**:
```
create_task → task_id 획득
     ↓
도면 분석 → 좌표 계산 → save_coords
     ↓
실행 계획 수립 → set_task_plan
     ↓
[단계별 실행]
```

## 맥락 손실 감지 및 자동 복구

복잡한 작업 중 맥락을 잃어버렸는지 자동으로 감지하고 복구합니다.

### 감지 지표 (5가지)

| 지표 | 설명 | 비중 |
|------|------|------|
| `step_mismatch` | 현재 단계와 체크포인트 불일치 | 0.3 |
| `entity_count_mismatch` | 예상 entity 수와 실제 수 불일치 | 0.25 |
| `long_gap` | 마지막 체크포인트로부터 5분 이상 경과 | 0.2 |
| `stuck_step` | 같은 단계에서 10분 이상 정체 | 0.15 |
| `task_paused` | 작업이 일시정지 상태 | 0.1 |

### 사용 명령어

#### 1. 수동 감지
```bash
python claude_helper.py detect_loss <task_id> [현재단계] [entity수]
```
→ loss_confidence 점수와 감지된 지표 반환

#### 2. 자동 감지 + 복구
```bash
python claude_helper.py auto_check <task_id> [현재단계] [entity수]
```
→ confidence ≥ 0.5 이면 자동으로 restore 실행

#### 3. 상태 확인
```bash
python claude_helper.py health <task_id>
```
→ 작업 건강도 점수 (0.0 ~ 1.0)

### 자동 복구 기준

| confidence | 상태 | 액션 |
|------------|------|------|
| 0.0 ~ 0.3 | 정상 | 계속 진행 |
| 0.3 ~ 0.5 | 주의 | 경고 표시, 수동 확인 권장 |
| 0.5 ~ 1.0 | 손실 | **자동 restore 실행** |

### 권장 워크플로우

복잡한 작업 실행 중 주기적으로 auto_check 호출:

```
[각 단계 시작 전]
     ↓
auto_check(task_id, 현재단계, entity수)
     ↓
[자동 복구 여부 확인]
  ├── action: "none" → 정상, 계속 진행
  └── action: "restored" → 복구됨, restored_context로 작업 재개
     ↓
[단계 실행]
```

## 작업 완료 후 체크리스트

1. `get_dxf_summary`로 결과 검증
2. 예상 entity count와 비교
3. 성공/실패 기록 추가
4. 특이사항 있으면 knowledge 파일 업데이트

## 지식 저장소 구조

```
knowledge/
├── engine/                    # 자동화 스크립트
│   ├── drawing_engine.py      # 메인 엔진
│   ├── context_manager.py     # 맥락 관리 (체크포인트, 복구)
│   └── claude_helper.py       # Claude 연동 CLI 헬퍼
├── patterns/                  # 작도 패턴
│   ├── elements.json          # 요소별 작도법
│   ├── drawing_types.json     # 도면 유형
│   └── calculations.json      # 계산 공식
├── references/                # 참조 데이터
│   ├── example_sequences.json # 실행 시퀀스
│   ├── tool_usage.json        # 도구 사용법
│   └── verification_rules.json
├── lessons/                   # 학습 기록
│   ├── successes.json         # 성공 사례
│   └── failures.json          # 실패 사례
└── context/                   # 프로젝트 설정
    └── project_settings.json
```

## 사용 가능한 시퀀스

| 시퀀스 | 설명 |
|--------|------|
| `simple_room` | 12m x 8m 방 평면도 (그리드+벽체+치수) |
| `grid_only` | 2x2 그리드 테스트 |
| `bolt_pattern_4x4` | 16개 볼트 패턴 |

## MCP 도구 사용 원칙

1. **레이어 먼저**: `create_layer` → `set_current_layer` → 도형 생성
2. **병렬 실행**: 독립적인 도구는 동시 호출
3. **ByLayer 원칙**: 색상/선종류는 레이어에서 상속
4. **검증 필수**: 작업 후 `get_dxf_summary`로 확인

## 안정성 등급

- **high**: 바로 사용 (create_line, create_polyline, create_text 등)
- **medium**: 주의 필요 (offset_entity - entityRef 참조 복잡)
- **low**: 피하거나 대안 사용

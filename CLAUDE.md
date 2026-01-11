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

---

## Photo Tracer (사진 따라 그리기) - 권장

사진을 보고 **그대로 따라 그리는** 기능입니다.

### 핵심 원칙

- **3D 투영 계산이 아닌**, 사진에서 보이는 것을 그대로 그린다
- 퍼린은 짧은 마크가 아닌, **깊이 방향 수평선**으로 표현
- 겹쳐 보이는 프레임들을 **offset**으로 표현
- H-beam 단면을 **여러 라인**으로 표현

### 워크플로우

```
[1. 사진 분석]
사진 보기 → trace_checklist 참고 → 보이는 요소 정확히 세기
     ↓
[2. 통합 명령 실행]
python claude_helper.py trace_draw '<분석결과_JSON>'
     ↓
[3. 시퀀스 실행]
생성된 sequence의 tools를 MCP 도구로 실행
```

### 명령어

```bash
# 정보 조회
python claude_helper.py trace_info        # 사용법 및 예시
python claude_helper.py trace_checklist   # 분석 체크리스트
python claude_helper.py trace_prompt      # 분석 프롬프트

# 통합 명령 (권장)
python claude_helper.py trace_draw '<JSON>' [width] [origin_x] [origin_y]

# 단계별 명령 (선택)
python claude_helper.py trace_create '<JSON>'    # 컨텍스트 생성
python claude_helper.py trace_coords <id>        # 좌표 계산
python claude_helper.py trace_sequence <id>      # 시퀀스 생성
python claude_helper.py trace_status <id>        # 상태 조회
```

### 분석 결과 JSON 형식

```json
{
  "visible_column_frames": 4,      // 겹쳐 보이는 기둥 프레임 수
  "visible_truss_frames": 4,       // 보이는 트러스 수
  "frame_spacing_ratio": 0.025,    // 프레임 간격 (도면 폭 대비)
  "columns_per_frame": 2,          // 프레임당 기둥 수
  "column_section_type": "H-beam", // "H-beam" 또는 "simple"
  "visible_purlin_lines": 8,       // 보이는 퍼린 라인 수
  "purlin_as_depth_lines": true,   // 깊이 방향 라인으로 표현
  "truss_type": "pratt",           // "pratt", "warren", "howe"
  "truss_panel_count": 10,
  "bracing_bays": 2,
  "width_height_ratio": 2.5,
  "eave_height_ratio": 0.72,
  "roof_pitch_degrees": 8
}
```

### 분석 시 핵심 체크리스트

| 항목 | 질문 | 필드 |
|------|------|------|
| 깊이/프레임 | 앞뒤로 겹쳐 보이는 기둥 몇 줄? | `visible_column_frames` |
| 퍼린 | 수평 퍼린 라인 몇 개? | `visible_purlin_lines` |
| 기둥 단면 | H-beam 형태 보이는가? | `column_section_type` |
| 트러스 | 타입과 패널 수는? | `truss_type`, `truss_panel_count` |

---

## 이미지 기반 도면 작도 (Image Analyzer) - 레거시

> **Note**: Photo Tracer (`trace_*`)를 권장합니다.

이미지를 분석하여 도면을 자동으로 그리는 기능입니다.

### 통합 명령

```bash
python claude_helper.py image_draw '<분석결과_JSON>' [width] [height] [margin] [level]
```

### 분석 결과 JSON 형식

```json
{
  "structure_type": "portal_frame_truss",
  "width_height_ratio": 2.5,
  "roof_pitch_degrees": 8,
  "eave_height_ratio": 0.7,
  "columns_left": 2,
  "columns_right": 2,
  "columns_middle": 1,
  "truss_panels": 10,
  "vertical_webs": 9,
  "diagonal_webs": 10,
  "purlins_per_slope": 8,
  "bracing_levels": 2,
  "detail_level": "L2_structural"
}
```

### 지원 구조 템플릿

- `portal_frame_truss`: 포털 프레임 + 트러스 지붕 (공장, 창고)
- `simple_gable_frame`: 단순 박공 프레임 (소규모 창고)
- `multi_span_truss`: 다중 스팬 트러스 (대형 공장)
- `warren_truss`: 워렌 트러스
- `pratt_truss`: 프랫 트러스

### 파일 구조

```
knowledge/
├── patterns/
│   ├── image_analysis.json     # 분석 체크리스트, 프롬프트
│   └── structure_templates.json # 구조별 템플릿, 비율
├── engine/
│   └── image_analyzer.py       # 분석/좌표/시퀀스 생성
└── analysis_cache/             # 분석 결과 저장 (자동 생성)
```

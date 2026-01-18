# Drawing Engine - Claude Code 세션 가이드

## 프로젝트 구조

```
Drawing_Engine/
├── src/                          # 핵심 엔진 코드
│   ├── core/                     # 공용 타입 및 핵심 엔진
│   │   ├── common.py             # Point2D, Point3D, TaskStatus, MCPToolGenerator
│   │   ├── drawing_engine.py     # JSON 시퀀스 기반 도면 자동 생성
│   │   └── context_manager.py    # 맥락 관리 (체크포인트, 복구)
│   ├── vectorize/                # 이미지 벡터화
│   │   ├── image_vectorizer.py   # 이미지→벡터 변환 (PNG/JPEG 내장 디코더)
│   │   └── line_cleaner.py       # 벡터화 후처리 (이중선 제거, 병합)
│   ├── measure/                  # 3D 측정
│   │   ├── frame_plane.py        # Homography 기반 평면 캘리브레이션
│   │   └── pnp_solver.py         # PnP 카메라 자세 계산
│   └── render/                   # 렌더링
│       └── isometric_renderer.py # 등각 투영 렌더러 (3D→2D)
├── api/                          # FastAPI 서버
│   └── main.py                   # REST API 엔드포인트
├── cli/                          # CLI 도구
│   ├── main.py                   # CLI 진입점
│   ├── session.py                # 세션 및 지식 관리
│   └── context.py                # 맥락 관리 CLI
├── knowledge/                    # 지식 저장소
│   ├── patterns/                 # 작도 패턴
│   ├── references/               # 시퀀스 예제
│   ├── lessons/                  # 성공/실패 기록
│   └── context/                  # 프로젝트 설정
└── extension/                    # VS Code 확장
```

## 세션 시작 시 필수 작업

새 대화를 시작할 때 아래 명령을 실행하여 지식을 로드합니다:

```bash
cd /Users/hi/2026Coding_Prj/Drawing_Engine && python -m cli.main session_start
```

이 명령은 다음을 반환합니다:
- 사용 가능한 시퀀스 목록
- 최근 성공/실패 기록
- 주의사항 및 팁
- **활성 작업 목록** (진행 중이던 작업)

## 주요 명령어

### 시퀀스 조회
```bash
python -m cli.main list_sequences
python -m cli.main get_sequence simple_room
```

### 요소 패턴 조회
```bash
python -m cli.main get_pattern grid
python -m cli.main get_pattern wall
python -m cli.main get_pattern dimension
```

### 성공 기록
```bash
python -m cli.main record_success \
  "작업설명" \
  "접근법" \
  "성공요인1,성공요인2" \
  '{"LINE":6,"CIRCLE":3}' \
  "태그1,태그2" \
  "메모"
```

### 실패 기록
```bash
python -m cli.main record_failure \
  "작업설명" \
  "에러내용" \
  "원인" \
  "해결방법" \
  "예방책" \
  "태그1,태그2"
```

## 맥락 유지 시스템 (Context Manager)

복잡한 작업 중 맥락을 잃어버리는 문제를 방지합니다.

### 추천 워크플로우 (자동화)

대량의 엔티티를 다룰 때는 `create_task_auto`를 사용하면 모든 설정이 자동으로 됩니다:

```bash
# 1. 엔티티 선택 후 자동 작업 생성
python -m cli.main create_task_auto \
  "redraw" \
  "선택 영역 다시 그리기" \
  '엔티티_JSON' \
  '0' '-15' \
  '20'  # batch_size

# 2. 실행 전 검증
python -m cli.main validate <task_id>

# 3. 단계별 실행 + 체크포인트
python -m cli.main checkpoint <task_id> 1 in_progress
# ... MCP 도구 실행 ...
python -m cli.main checkpoint <task_id> 1 completed

# 4. 맥락 확인 (주기적)
python -m cli.main auto_check <task_id>
```

### 수동 워크플로우

```bash
# 작업 생성
python -m cli.main create_task copy_region "도면 영역 복사"

# 활성 작업 확인
python -m cli.main list_tasks

# 맥락 복구
python -m cli.main restore <task_id>

# 체크포인트 기록
python -m cli.main checkpoint <task_id> <step> <status>

# 남은 작업 조회
python -m cli.main get_remaining <task_id>
```

### 맥락 손실 감지

```bash
# 수동 감지
python -m cli.main detect_loss <task_id> [현재단계] [entity수]

# 자동 감지 + 복구 (confidence >= 0.5 이면 자동 restore)
python -m cli.main auto_check <task_id> [현재단계] [entity수]

# 작업 건강도 점수
python -m cli.main health <task_id>
```

| confidence | 상태 | 액션 |
|------------|------|------|
| 0.0 ~ 0.3 | 정상 | 계속 진행 |
| 0.3 ~ 0.5 | 주의 | 경고 표시, 수동 확인 권장 |
| 0.5 ~ 1.0 | 손실 | **자동 restore 실행** |

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

## 배경 이미지 벡터화 (Image Vectorizer)

**사용자가 "벡터화 해줘"라고 요청하면 자동으로 실행합니다.**

### 자동 워크플로우

```
[1단계] 배경 이미지 정보 조회
MCP: get_background_images
→ 이미지 위치(x, y), 크기(width, height) 획득

[2단계] 이미지 파일 경로 확인

[3단계] 벡터화 실행
cd /Users/hi/2026Coding_Prj/Drawing_Engine && \
  python -c "from src.vectorize.image_vectorizer import cli_vectorize_to_dxf; \
  print(cli_vectorize_to_dxf('<이미지경로>', '<bg_json>', '<dxf경로>', '<options>'))"

[4단계] 결과 안내
```

### 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `mode` | `binary` (이진화) 또는 `edge` (엣지감지) | `binary` |
| `threshold` | 이진화 임계값 (0-255) | `200` |
| `epsilon` | 단순화 허용 오차 | `1.0` |
| `min_length` | 최소 윤곽선 길이 | `5` |
| `layer` | 출력 레이어 이름 | `0` |

### 이미지 유형별 권장 설정

| 이미지 유형 | mode | threshold | epsilon |
|------------|------|-----------|---------|
| 흑백 도면/라인 드로잉 | `binary` | `200` | `1.0` |
| 스캔된 도면 | `binary` | `150` | `1.5` |
| 사진 (선 추출) | `edge` | - | `2.0` |

---

## 선 후처리 (Line Cleaner)

**벡터화 후 "정리해줘"라고 요청하면 자동으로 실행합니다.**

### 기능

1. **중심선 추출**: 평행한 두 선 → 단일 중심선
2. **선 병합**: 같은 직선 위의 분절된 선들 합치기
3. **중복 제거**: 거의 같은 선 제거
4. **노이즈 필터**: 짧은 선 제거
5. **끝점 스냅**: 끝점을 가까운 점에 맞추기

### 일반적인 워크플로우

```
[1] 배경 이미지 벡터화 → 981개 LINE 생성
[2] 선 정리 → 199개 LINE (79.7% 감소)
[3] VS Code에서 output.dxf 열기
```

---

## API 서버

```bash
# 서버 실행 (프로젝트 루트에서)
cd /Users/hi/2026Coding_Prj/Drawing_Engine && python -m api.main
```

### 엔드포인트

| 엔드포인트 | 기능 |
|-----------|------|
| `POST /frame/calibrate` | 4점 Homography 캘리브레이션 |
| `POST /frame/p2p` | 두 점 간 실제 거리 측정 |
| `POST /pnp/solve` | PnP 카메라 자세 계산 |
| `POST /pnp/pixel-to-world` | 픽셀→3D 월드 좌표 변환 |

---

## 주의사항

- DXF 파일 직접 수정 후 **VS Code에서 파일을 다시 열어야** 변경사항이 표시됨
- MCP Viewer는 메모리 캐시를 사용하므로 외부 수정이 즉시 반영되지 않음

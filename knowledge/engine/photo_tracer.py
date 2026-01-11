"""
Photo Tracer Module - 사진을 보고 그대로 따라 그리기
==================================================

이 모듈의 핵심 철학:
- 3D 투영 계산이 아닌, **사진에 보이는 것을 그대로** 2D로 재현
- 시각 요소 카운터: 사진에서 보이는 요소를 정확히 세어서 기록
- 라인별 그리기: 각 선을 개별적으로 추적하여 그리기
- 컨텍스트 유지: 분석 결과를 저장하여 그리기 중 맥락 유지

사용 워크플로우:
1. 사진 분석 → VisualElementCounter로 보이는 요소 카운트
2. TracingContext에 저장 → 맥락 유지
3. ElementDrawer로 요소별 그리기 → 라인 단위 실행
4. 검증 → 사진과 비교

기존 모듈 통합:
- view_renderer_2d.py의 비율 계산 기능
- image_analyzer.py의 분석/시퀀스 생성 기능
→ 단일 photo_tracer.py로 통합
"""

import json
import math
import os
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum

# 경로 설정
KNOWLEDGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# =============================================================================
# 1. 데이터 클래스
# =============================================================================

@dataclass
class Point2D:
    """2D 점"""
    x: float
    y: float

    def to_dict(self) -> Dict[str, float]:
        return {"x": self.x, "y": self.y}

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

    def scale(self, factor: float) -> 'Point2D':
        return Point2D(self.x * factor, self.y * factor)


class ElementType(Enum):
    """도면 요소 타입"""
    COLUMN = "column"
    BEAM = "beam"
    RAFTER = "rafter"
    TRUSS_TOP_CHORD = "truss_top_chord"
    TRUSS_BOTTOM_CHORD = "truss_bottom_chord"
    TRUSS_WEB_VERTICAL = "truss_web_vertical"
    TRUSS_WEB_DIAGONAL = "truss_web_diagonal"
    PURLIN = "purlin"
    BRACING = "bracing"
    FOUNDATION = "foundation"
    H_SECTION = "h_section"


@dataclass
class VisualElement:
    """사진에서 식별된 시각 요소"""
    element_type: ElementType
    element_id: str
    start: Point2D
    end: Point2D
    layer: str = "0"
    properties: Dict = field(default_factory=dict)
    drawn: bool = False

    def to_dict(self) -> Dict:
        return {
            "type": self.element_type.value,
            "id": self.element_id,
            "start": self.start.to_dict(),
            "end": self.end.to_dict(),
            "layer": self.layer,
            "properties": self.properties,
            "drawn": self.drawn
        }


@dataclass
class VisualElementCount:
    """
    사진에서 세어진 시각 요소 개수

    핵심: 사진에서 **보이는 것**을 정확히 센다
    - visible_column_frames: 겹쳐 보이는 기둥 프레임 수 (깊이 표현)
    - visible_purlin_lines: 수평으로 보이는 펄린 라인 수
    - visible_truss_frames: 보이는 트러스 수
    """
    # 프레임/깊이 관련
    visible_column_frames: int = 1  # 겹쳐 보이는 기둥 프레임 수
    visible_truss_frames: int = 1   # 보이는 트러스 수
    frame_spacing_ratio: float = 0.03  # 프레임 간격 (도면 폭 대비 비율)

    # 기둥
    columns_per_frame: int = 2  # 프레임당 기둥 수
    column_section_type: str = "H-beam"  # H-beam, C-channel, etc.

    # 지붕/트러스
    truss_panel_count: int = 8
    truss_type: str = "pratt"  # warren, pratt, howe

    # 퍼린 - 핵심!
    visible_purlin_lines: int = 6  # 사진에서 보이는 수평 퍼린 라인 수
    purlin_as_depth_lines: bool = True  # 퍼린을 깊이 방향 라인으로 표현

    # 가새
    bracing_bays: int = 2  # X-가새가 있는 베이 수

    # 비율 정보
    width_height_ratio: float = 2.5
    eave_height_ratio: float = 0.72
    roof_pitch_degrees: float = 8.0

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'VisualElementCount':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


@dataclass
class TracingContext:
    """
    사진 추적 컨텍스트 - 분석 결과 저장 및 맥락 유지

    이 클래스는 사진 분석부터 그리기 완료까지 전체 컨텍스트를 유지합니다.
    """
    # 식별 정보
    context_id: str = ""
    created_at: str = ""
    photo_description: str = ""

    # 사진 분석 결과
    element_counts: VisualElementCount = field(default_factory=VisualElementCount)

    # 계산된 좌표
    canvas_width: float = 800
    canvas_height: float = 400
    origin_x: float = 50
    origin_y: float = 50
    key_points: Dict[str, Dict] = field(default_factory=dict)

    # 그리기 요소
    elements: List[VisualElement] = field(default_factory=list)
    drawn_elements: List[str] = field(default_factory=list)  # 그려진 요소 ID

    # 상태
    status: str = "created"  # created, analyzing, calculated, drawing, completed
    current_step: int = 0
    total_steps: int = 0

    # 노트
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "context_id": self.context_id,
            "created_at": self.created_at,
            "photo_description": self.photo_description,
            "element_counts": self.element_counts.to_dict(),
            "canvas": {
                "width": self.canvas_width,
                "height": self.canvas_height,
                "origin_x": self.origin_x,
                "origin_y": self.origin_y
            },
            "key_points": self.key_points,
            "elements": [e.to_dict() for e in self.elements],
            "drawn_elements": self.drawn_elements,
            "status": self.status,
            "current_step": self.current_step,
            "total_steps": self.total_steps,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'TracingContext':
        ctx = cls()
        ctx.context_id = data.get("context_id", "")
        ctx.created_at = data.get("created_at", "")
        ctx.photo_description = data.get("photo_description", "")

        if "element_counts" in data:
            ctx.element_counts = VisualElementCount.from_dict(data["element_counts"])

        canvas = data.get("canvas", {})
        ctx.canvas_width = canvas.get("width", 800)
        ctx.canvas_height = canvas.get("height", 400)
        ctx.origin_x = canvas.get("origin_x", 50)
        ctx.origin_y = canvas.get("origin_y", 50)

        ctx.key_points = data.get("key_points", {})
        ctx.drawn_elements = data.get("drawn_elements", [])
        ctx.status = data.get("status", "created")
        ctx.current_step = data.get("current_step", 0)
        ctx.total_steps = data.get("total_steps", 0)
        ctx.notes = data.get("notes", [])

        return ctx


# =============================================================================
# 2. PhotoTracer 메인 클래스
# =============================================================================

class PhotoTracer:
    """
    사진 따라 그리기 통합 클래스

    주요 기능:
    1. 사진 분석 체크리스트 제공
    2. 시각 요소 카운트 저장
    3. 좌표 계산 (비율 기반)
    4. 요소별 MCP 명령 생성
    5. 컨텍스트 저장/복원
    """

    def __init__(self):
        self.context: Optional[TracingContext] = None
        self.cache_dir = os.path.join(KNOWLEDGE_ROOT, "tracing_cache")
        os.makedirs(self.cache_dir, exist_ok=True)

    # =========================================================================
    # 2.1 분석 체크리스트
    # =========================================================================

    def get_analysis_checklist(self) -> Dict:
        """
        사진 분석 시 Claude가 확인할 체크리스트

        이 체크리스트는 사진에서 **보이는 것**을 정확히 세는 데 초점을 맞춥니다.
        """
        return {
            "description": "사진에서 보이는 요소를 정확히 세는 체크리스트",
            "핵심_원칙": "3D 투영 계산이 아닌, 사진에서 보이는 선을 그대로 센다",

            "1_깊이_프레임": {
                "질문": "사진에서 앞뒤로 겹쳐 보이는 기둥/트러스 프레임이 몇 개인가?",
                "확인사항": [
                    "가장 앞 프레임의 기둥 라인",
                    "뒤에 보이는 기둥 라인들 (offset되어 보임)",
                    "전체 몇 줄의 기둥이 보이는가?"
                ],
                "기록": "visible_column_frames, visible_truss_frames"
            },

            "2_기둥": {
                "질문": "각 프레임에 기둥이 몇 개인가?",
                "확인사항": [
                    "좌측 기둥",
                    "우측 기둥",
                    "중간 기둥 (있다면)",
                    "기둥 단면 형태 (H-beam 보이면 기록)"
                ],
                "기록": "columns_per_frame, column_section_type"
            },

            "3_퍼린_중요": {
                "질문": "사진에서 수평으로 보이는 퍼린 라인이 몇 개인가?",
                "확인사항": [
                    "지붕 경사면을 가로지르는 수평선 개수",
                    "이 선들이 건물 깊이 방향으로 연장되어 보이는지",
                    "좌측 경사면과 우측 경사면 각각"
                ],
                "기록": "visible_purlin_lines, purlin_as_depth_lines",
                "주의": "퍼린은 짧은 마크가 아닌, 깊이 방향 수평선으로 표현해야 함"
            },

            "4_트러스": {
                "질문": "트러스 구조의 세부 사항은?",
                "확인사항": [
                    "트러스 유형 (warren/pratt/howe)",
                    "상현재 패널 수",
                    "수직/대각 웹부재 개수"
                ],
                "기록": "truss_type, truss_panel_count"
            },

            "5_가새": {
                "질문": "X-가새가 어디에 보이는가?",
                "확인사항": [
                    "기둥 사이 X-가새",
                    "몇 개의 베이에 가새가 있는가"
                ],
                "기록": "bracing_bays"
            },

            "6_비율": {
                "질문": "전체 비율은?",
                "확인사항": [
                    "건물 가로:세로 비율",
                    "처마 높이가 전체의 몇 %인가",
                    "지붕 경사각"
                ],
                "기록": "width_height_ratio, eave_height_ratio, roof_pitch_degrees"
            }
        }

    def get_analysis_prompt(self) -> str:
        """Claude가 사진 분석 시 사용할 프롬프트"""
        return """사진을 분석하여 다음 정보를 추출하세요:

## 핵심 원칙
- 3D 투영 계산이 아닌, **사진에서 보이는 선을 그대로** 센다
- 퍼린은 짧은 마크가 아닌, 건물 깊이 방향의 수평선으로 표현

## 분석 항목

1. **깊이/프레임** (가장 중요!)
   - visible_column_frames: 앞뒤로 겹쳐 보이는 기둥 프레임 수
   - visible_truss_frames: 보이는 트러스 프레임 수
   - frame_spacing_ratio: 프레임 간 간격 (도면 폭의 비율, 예: 0.03)

2. **기둥**
   - columns_per_frame: 프레임당 기둥 수
   - column_section_type: "H-beam" 또는 "simple"

3. **퍼린** (주의 필요!)
   - visible_purlin_lines: 사진에서 보이는 수평 퍼린 라인 수
   - purlin_as_depth_lines: true (퍼린을 깊이 방향 선으로 표현)

4. **트러스**
   - truss_type: "warren", "pratt", "howe" 중 선택
   - truss_panel_count: 상현재 패널 수

5. **가새**
   - bracing_bays: X-가새가 있는 베이 수

6. **비율**
   - width_height_ratio: 가로:세로 비율 (예: 2.5)
   - eave_height_ratio: 처마높이/전체높이 (예: 0.72)
   - roof_pitch_degrees: 지붕 경사각 (예: 8)

## 출력 형식
JSON으로 출력:
```json
{
  "visible_column_frames": 4,
  "visible_truss_frames": 4,
  "frame_spacing_ratio": 0.025,
  "columns_per_frame": 2,
  "column_section_type": "H-beam",
  "visible_purlin_lines": 8,
  "purlin_as_depth_lines": true,
  "truss_type": "pratt",
  "truss_panel_count": 10,
  "bracing_bays": 2,
  "width_height_ratio": 2.5,
  "eave_height_ratio": 0.72,
  "roof_pitch_degrees": 8
}
```"""

    # =========================================================================
    # 2.2 컨텍스트 생성/저장/로드
    # =========================================================================

    def create_context(self, element_counts: Dict,
                       canvas_width: float = 800,
                       origin_x: float = 50, origin_y: float = 50,
                       description: str = "") -> str:
        """
        새 추적 컨텍스트 생성

        Args:
            element_counts: 사진 분석 결과 (VisualElementCount 필드들)
            canvas_width: 캔버스 너비
            origin_x, origin_y: 원점 좌표
            description: 사진 설명

        Returns:
            context_id
        """
        context_id = f"trace_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        counts = VisualElementCount.from_dict(element_counts)

        # 높이 자동 계산
        canvas_height = canvas_width / counts.width_height_ratio

        self.context = TracingContext(
            context_id=context_id,
            created_at=datetime.now().isoformat(),
            photo_description=description,
            element_counts=counts,
            canvas_width=canvas_width,
            canvas_height=canvas_height,
            origin_x=origin_x,
            origin_y=origin_y,
            status="created"
        )

        self._save_context()
        return context_id

    def load_context(self, context_id: str) -> Optional[TracingContext]:
        """저장된 컨텍스트 로드"""
        filepath = os.path.join(self.cache_dir, f"{context_id}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.context = TracingContext.from_dict(data)
                return self.context
        return None

    def _save_context(self):
        """현재 컨텍스트 저장"""
        if not self.context:
            return
        filepath = os.path.join(self.cache_dir, f"{self.context.context_id}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.context.to_dict(), f, ensure_ascii=False, indent=2)

    def get_context_summary(self) -> Dict:
        """현재 컨텍스트 요약"""
        if not self.context:
            return {"error": "No active context"}

        return {
            "context_id": self.context.context_id,
            "status": self.context.status,
            "progress": f"{self.context.current_step}/{self.context.total_steps}",
            "elements_total": len(self.context.elements),
            "elements_drawn": len(self.context.drawn_elements),
            "remaining": len(self.context.elements) - len(self.context.drawn_elements)
        }

    # =========================================================================
    # 2.3 좌표 계산
    # =========================================================================

    def calculate_coordinates(self) -> Dict:
        """
        분석 결과 기반 좌표 계산

        사진의 비율과 요소 개수를 바탕으로 모든 좌표를 계산합니다.
        """
        if not self.context:
            raise ValueError("No active context. Call create_context() first.")

        ctx = self.context
        c = ctx.element_counts

        # 기본 좌표
        origin = Point2D(ctx.origin_x, ctx.origin_y)
        width = ctx.canvas_width - 2 * ctx.origin_x
        height = width / c.width_height_ratio

        # 처마 높이
        eave_height = height * c.eave_height_ratio

        # 지붕 최고점
        angle_rad = math.radians(c.roof_pitch_degrees)
        ridge_rise = (width / 2) * math.tan(angle_rad)
        ridge_height = eave_height + ridge_rise

        # 프레임 간격 (깊이 표현)
        frame_offset = width * c.frame_spacing_ratio

        key_points = {
            # 기본점
            "bottom_left": Point2D(origin.x, origin.y).to_dict(),
            "bottom_right": Point2D(origin.x + width, origin.y).to_dict(),
            "bottom_center": Point2D(origin.x + width/2, origin.y).to_dict(),
            "eave_left": Point2D(origin.x, origin.y + eave_height).to_dict(),
            "eave_right": Point2D(origin.x + width, origin.y + eave_height).to_dict(),
            "ridge": Point2D(origin.x + width/2, origin.y + ridge_height).to_dict(),

            # 치수
            "_width": width,
            "_height": height,
            "_eave_height": eave_height,
            "_ridge_height": ridge_height,
            "_frame_offset": frame_offset
        }

        ctx.key_points = key_points
        ctx.status = "calculated"

        # 요소 생성
        self._generate_elements()

        self._save_context()

        return key_points

    def _generate_elements(self):
        """모든 도면 요소 생성"""
        if not self.context:
            return

        ctx = self.context
        c = ctx.element_counts
        kp = ctx.key_points

        elements = []
        element_id = 0

        # 프레임 오프셋
        frame_offset = kp["_frame_offset"]

        # 1. 기둥 (모든 프레임)
        for frame_idx in range(c.visible_column_frames):
            offset = frame_idx * frame_offset

            # 좌측 기둥
            element_id += 1
            elements.append(VisualElement(
                element_type=ElementType.COLUMN,
                element_id=f"col_L_f{frame_idx}",
                start=Point2D(kp["bottom_left"]["x"] + offset, kp["bottom_left"]["y"]),
                end=Point2D(kp["eave_left"]["x"] + offset, kp["eave_left"]["y"]),
                layer="COLUMN",
                properties={"frame": frame_idx, "side": "left"}
            ))

            # 우측 기둥
            element_id += 1
            elements.append(VisualElement(
                element_type=ElementType.COLUMN,
                element_id=f"col_R_f{frame_idx}",
                start=Point2D(kp["bottom_right"]["x"] + offset, kp["bottom_right"]["y"]),
                end=Point2D(kp["eave_right"]["x"] + offset, kp["eave_right"]["y"]),
                layer="COLUMN",
                properties={"frame": frame_idx, "side": "right"}
            ))

        # 2. H-beam 단면 (첫 프레임만 상세)
        if c.column_section_type == "H-beam":
            elements.extend(self._generate_h_section_elements(kp))

        # 3. 래프터/상현재 (모든 프레임)
        for frame_idx in range(c.visible_truss_frames):
            offset = frame_idx * frame_offset

            # 좌측 래프터
            element_id += 1
            elements.append(VisualElement(
                element_type=ElementType.RAFTER,
                element_id=f"rafter_L_f{frame_idx}",
                start=Point2D(kp["eave_left"]["x"] + offset, kp["eave_left"]["y"]),
                end=Point2D(kp["ridge"]["x"] + offset, kp["ridge"]["y"]),
                layer="BEAM",
                properties={"frame": frame_idx, "side": "left"}
            ))

            # 우측 래프터
            element_id += 1
            elements.append(VisualElement(
                element_type=ElementType.RAFTER,
                element_id=f"rafter_R_f{frame_idx}",
                start=Point2D(kp["ridge"]["x"] + offset, kp["ridge"]["y"]),
                end=Point2D(kp["eave_right"]["x"] + offset, kp["eave_right"]["y"]),
                layer="BEAM",
                properties={"frame": frame_idx, "side": "right"}
            ))

        # 4. 퍼린 (깊이 방향 수평선) - 핵심!
        if c.purlin_as_depth_lines:
            elements.extend(self._generate_purlin_depth_lines(kp, c))

        # 5. 트러스 웹부재 (첫 프레임만)
        elements.extend(self._generate_truss_web_elements(kp, c))

        # 6. X-가새
        if c.bracing_bays > 0:
            elements.extend(self._generate_bracing_elements(kp, c))

        # 7. 기초선
        elements.append(VisualElement(
            element_type=ElementType.FOUNDATION,
            element_id="foundation",
            start=Point2D(kp["bottom_left"]["x"], kp["bottom_left"]["y"]),
            end=Point2D(kp["bottom_right"]["x"], kp["bottom_right"]["y"]),
            layer="FOUNDATION"
        ))

        ctx.elements = elements
        ctx.total_steps = len(elements)

    def _generate_h_section_elements(self, kp: Dict) -> List[VisualElement]:
        """H-beam 단면 표현 요소 생성"""
        elements = []

        # H-beam 너비 (도면 폭의 약 5%)
        h_width = kp["_width"] * 0.03
        flange_thickness = h_width * 0.15

        # 좌측 기둥 H-section
        col_x = kp["bottom_left"]["x"]
        col_bottom = kp["bottom_left"]["y"]
        col_top = kp["eave_left"]["y"]

        # 플랜지 라인들
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_L_inner",
            start=Point2D(col_x + h_width/2, col_bottom),
            end=Point2D(col_x + h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "inner_flange"}
        ))
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_L_outer",
            start=Point2D(col_x - h_width/2, col_bottom),
            end=Point2D(col_x - h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "outer_flange"}
        ))

        # 상하단 캡
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_L_top_cap",
            start=Point2D(col_x - h_width/2, col_top),
            end=Point2D(col_x + h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "top_cap"}
        ))
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_L_bottom_cap",
            start=Point2D(col_x - h_width/2, col_bottom),
            end=Point2D(col_x + h_width/2, col_bottom),
            layer="COLUMN",
            properties={"part": "bottom_cap"}
        ))

        # 우측 기둥도 동일하게
        col_x = kp["bottom_right"]["x"]
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_R_inner",
            start=Point2D(col_x - h_width/2, col_bottom),
            end=Point2D(col_x - h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "inner_flange"}
        ))
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_R_outer",
            start=Point2D(col_x + h_width/2, col_bottom),
            end=Point2D(col_x + h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "outer_flange"}
        ))
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_R_top_cap",
            start=Point2D(col_x - h_width/2, col_top),
            end=Point2D(col_x + h_width/2, col_top),
            layer="COLUMN",
            properties={"part": "top_cap"}
        ))
        elements.append(VisualElement(
            element_type=ElementType.H_SECTION,
            element_id="h_R_bottom_cap",
            start=Point2D(col_x - h_width/2, col_bottom),
            end=Point2D(col_x + h_width/2, col_bottom),
            layer="COLUMN",
            properties={"part": "bottom_cap"}
        ))

        return elements

    def _generate_purlin_depth_lines(self, kp: Dict, c: VisualElementCount) -> List[VisualElement]:
        """
        퍼린 깊이 방향 라인 생성 - 핵심 기능!

        사진에서 퍼린은 건물 깊이 방향으로 연장된 수평선으로 보입니다.
        짧은 마크가 아닌, 프레임들을 가로지르는 수평선으로 그립니다.
        """
        elements = []

        # 전체 깊이 (프레임 수 * 오프셋)
        total_depth = (c.visible_column_frames - 1) * kp["_frame_offset"]

        # 좌측 경사면 퍼린 위치 계산
        eave_left = Point2D(kp["eave_left"]["x"], kp["eave_left"]["y"])
        ridge = Point2D(kp["ridge"]["x"], kp["ridge"]["y"])

        purlin_count = c.visible_purlin_lines // 2  # 좌우 각각

        for i in range(1, purlin_count + 1):
            t = i / (purlin_count + 1)

            # 좌측 경사면 위치
            x = eave_left.x + (ridge.x - eave_left.x) * t
            y = eave_left.y + (ridge.y - eave_left.y) * t

            # 깊이 방향 라인 (첫 프레임에서 마지막 프레임까지)
            elements.append(VisualElement(
                element_type=ElementType.PURLIN,
                element_id=f"purlin_L_{i}",
                start=Point2D(x, y),
                end=Point2D(x + total_depth, y),  # 깊이 방향으로 연장
                layer="PURLIN",
                properties={"side": "left", "index": i}
            ))

        # 우측 경사면 퍼린
        eave_right = Point2D(kp["eave_right"]["x"], kp["eave_right"]["y"])

        for i in range(1, purlin_count + 1):
            t = i / (purlin_count + 1)

            x = eave_right.x + (ridge.x - eave_right.x) * t
            y = eave_right.y + (ridge.y - eave_right.y) * t

            elements.append(VisualElement(
                element_type=ElementType.PURLIN,
                element_id=f"purlin_R_{i}",
                start=Point2D(x, y),
                end=Point2D(x + total_depth, y),
                layer="PURLIN",
                properties={"side": "right", "index": i}
            ))

        return elements

    def _generate_truss_web_elements(self, kp: Dict, c: VisualElementCount) -> List[VisualElement]:
        """트러스 웹부재 생성"""
        elements = []

        eave_y = kp["eave_left"]["y"]
        ridge_y = kp["ridge"]["y"]

        # 하현재 높이 (트러스 깊이)
        truss_depth = (ridge_y - eave_y) * 0.25
        bottom_chord_y = eave_y

        # 하현재
        elements.append(VisualElement(
            element_type=ElementType.TRUSS_BOTTOM_CHORD,
            element_id="truss_bottom_chord",
            start=Point2D(kp["eave_left"]["x"], bottom_chord_y),
            end=Point2D(kp["eave_right"]["x"], bottom_chord_y),
            layer="TRUSS"
        ))

        # 웹부재 계산
        half_panels = c.truss_panel_count // 2
        left_x = kp["eave_left"]["x"]
        right_x = kp["eave_right"]["x"]
        center_x = kp["ridge"]["x"]
        panel_width = (center_x - left_x) / half_panels

        # 수직 웹부재
        for i in range(1, half_panels):
            x = left_x + panel_width * i
            t = i / half_panels
            top_y = eave_y + (ridge_y - eave_y) * t

            elements.append(VisualElement(
                element_type=ElementType.TRUSS_WEB_VERTICAL,
                element_id=f"web_vert_L_{i}",
                start=Point2D(x, bottom_chord_y),
                end=Point2D(x, top_y),
                layer="TRUSS"
            ))

        # 중앙 수직
        elements.append(VisualElement(
            element_type=ElementType.TRUSS_WEB_VERTICAL,
            element_id="web_vert_center",
            start=Point2D(center_x, bottom_chord_y),
            end=Point2D(center_x, ridge_y),
            layer="TRUSS"
        ))

        # 우측 수직
        for i in range(1, half_panels):
            x = right_x - panel_width * i
            t = i / half_panels
            top_y = eave_y + (ridge_y - eave_y) * t

            elements.append(VisualElement(
                element_type=ElementType.TRUSS_WEB_VERTICAL,
                element_id=f"web_vert_R_{i}",
                start=Point2D(x, bottom_chord_y),
                end=Point2D(x, top_y),
                layer="TRUSS"
            ))

        # 대각 웹부재 (트러스 타입에 따라)
        if c.truss_type == "pratt":
            elements.extend(self._generate_pratt_diagonals(kp, c, bottom_chord_y))
        elif c.truss_type == "warren":
            elements.extend(self._generate_warren_diagonals(kp, c, bottom_chord_y))

        return elements

    def _generate_pratt_diagonals(self, kp: Dict, c: VisualElementCount,
                                   bottom_chord_y: float) -> List[VisualElement]:
        """프랫 트러스 대각 웹부재"""
        elements = []

        half_panels = c.truss_panel_count // 2
        left_x = kp["eave_left"]["x"]
        center_x = kp["ridge"]["x"]
        right_x = kp["eave_right"]["x"]
        panel_width = (center_x - left_x) / half_panels
        eave_y = kp["eave_left"]["y"]
        ridge_y = kp["ridge"]["y"]

        # 좌측: 하현재에서 상현재 중앙 방향
        for i in range(half_panels):
            x1 = left_x + panel_width * i
            x2 = left_x + panel_width * (i + 1)
            t2 = (i + 1) / half_panels
            top_y2 = eave_y + (ridge_y - eave_y) * t2

            elements.append(VisualElement(
                element_type=ElementType.TRUSS_WEB_DIAGONAL,
                element_id=f"web_diag_L_{i}",
                start=Point2D(x1, bottom_chord_y),
                end=Point2D(x2, top_y2),
                layer="TRUSS"
            ))

        # 우측: 대칭
        for i in range(half_panels):
            x1 = right_x - panel_width * i
            x2 = right_x - panel_width * (i + 1)
            t2 = (i + 1) / half_panels
            top_y2 = eave_y + (ridge_y - eave_y) * t2

            elements.append(VisualElement(
                element_type=ElementType.TRUSS_WEB_DIAGONAL,
                element_id=f"web_diag_R_{i}",
                start=Point2D(x1, bottom_chord_y),
                end=Point2D(x2, top_y2),
                layer="TRUSS"
            ))

        return elements

    def _generate_warren_diagonals(self, kp: Dict, c: VisualElementCount,
                                    bottom_chord_y: float) -> List[VisualElement]:
        """워렌 트러스 대각 웹부재 (지그재그)"""
        elements = []

        half_panels = c.truss_panel_count // 2
        left_x = kp["eave_left"]["x"]
        center_x = kp["ridge"]["x"]
        panel_width = (center_x - left_x) / half_panels
        eave_y = kp["eave_left"]["y"]
        ridge_y = kp["ridge"]["y"]

        for i in range(half_panels):
            x1 = left_x + panel_width * i
            x2 = left_x + panel_width * (i + 1)
            t1 = i / half_panels
            t2 = (i + 1) / half_panels
            top_y1 = eave_y + (ridge_y - eave_y) * t1
            top_y2 = eave_y + (ridge_y - eave_y) * t2

            if i % 2 == 0:
                # 아래에서 위로
                elements.append(VisualElement(
                    element_type=ElementType.TRUSS_WEB_DIAGONAL,
                    element_id=f"web_diag_L_{i}",
                    start=Point2D(x1, bottom_chord_y),
                    end=Point2D(x2, top_y2),
                    layer="TRUSS"
                ))
            else:
                # 위에서 아래로
                elements.append(VisualElement(
                    element_type=ElementType.TRUSS_WEB_DIAGONAL,
                    element_id=f"web_diag_L_{i}",
                    start=Point2D(x1, top_y1),
                    end=Point2D(x2, bottom_chord_y),
                    layer="TRUSS"
                ))

        return elements

    def _generate_bracing_elements(self, kp: Dict, c: VisualElementCount) -> List[VisualElement]:
        """X-가새 생성"""
        elements = []

        bottom_y = kp["bottom_left"]["y"]
        top_y = kp["eave_left"]["y"]
        left_x = kp["bottom_left"]["x"]
        right_x = kp["bottom_right"]["x"]

        # 첫 번째 베이
        bay_width = (right_x - left_x) / 3  # 간단히 3등분

        # 좌측 베이 X-가새
        elements.append(VisualElement(
            element_type=ElementType.BRACING,
            element_id="brace_L1",
            start=Point2D(left_x, bottom_y),
            end=Point2D(left_x + bay_width, top_y),
            layer="BRACING"
        ))
        elements.append(VisualElement(
            element_type=ElementType.BRACING,
            element_id="brace_L2",
            start=Point2D(left_x + bay_width, bottom_y),
            end=Point2D(left_x, top_y),
            layer="BRACING"
        ))

        # 우측 베이 X-가새
        if c.bracing_bays >= 2:
            elements.append(VisualElement(
                element_type=ElementType.BRACING,
                element_id="brace_R1",
                start=Point2D(right_x - bay_width, bottom_y),
                end=Point2D(right_x, top_y),
                layer="BRACING"
            ))
            elements.append(VisualElement(
                element_type=ElementType.BRACING,
                element_id="brace_R2",
                start=Point2D(right_x, bottom_y),
                end=Point2D(right_x - bay_width, top_y),
                layer="BRACING"
            ))

        return elements

    # =========================================================================
    # 2.4 MCP 명령 시퀀스 생성
    # =========================================================================

    def generate_mcp_sequence(self) -> List[Dict]:
        """
        MCP 도구 호출 시퀀스 생성

        컨텍스트의 요소들을 MCP 명령으로 변환합니다.
        """
        if not self.context:
            raise ValueError("No active context")
        if not self.context.elements:
            raise ValueError("No elements calculated. Call calculate_coordinates() first.")

        ctx = self.context

        sequence = []

        # Step 1: 레이어 생성
        layers = set(e.layer for e in ctx.elements)
        layer_tools = []
        layer_colors = {
            "COLUMN": 7, "BEAM": 4, "TRUSS": 6,
            "PURLIN": 3, "BRACING": 5, "FOUNDATION": 8
        }

        for layer in layers:
            layer_tools.append({
                "tool": "create_layer",
                "args": {"name": layer, "color": layer_colors.get(layer, 7)}
            })

        sequence.append({
            "step": 1,
            "name": "레이어 생성",
            "parallel": True,
            "tools": layer_tools
        })

        # Step 2~N: 타입별 그리기
        type_groups = {}
        for elem in ctx.elements:
            t = elem.element_type.value
            if t not in type_groups:
                type_groups[t] = []
            type_groups[t].append(elem)

        step_num = 2
        type_names = {
            "column": "기둥",
            "h_section": "H-beam 단면",
            "rafter": "래프터/상현재",
            "truss_bottom_chord": "트러스 하현재",
            "truss_web_vertical": "트러스 수직 웹",
            "truss_web_diagonal": "트러스 대각 웹",
            "purlin": "퍼린 (깊이 방향)",
            "bracing": "X-가새",
            "foundation": "기초"
        }

        for elem_type, elements in type_groups.items():
            tools = []
            for elem in elements:
                tools.append({
                    "tool": "create_line",
                    "args": {
                        "start": elem.start.to_dict(),
                        "end": elem.end.to_dict(),
                        "layer": elem.layer
                    }
                })

            sequence.append({
                "step": step_num,
                "name": type_names.get(elem_type, elem_type),
                "element_type": elem_type,
                "parallel": True,
                "tools": tools,
                "count": len(tools)
            })
            step_num += 1

        ctx.total_steps = step_num - 1
        self._save_context()

        return sequence

    def get_remaining_elements(self) -> List[Dict]:
        """그리지 않은 요소 조회"""
        if not self.context:
            return []

        remaining = []
        for elem in self.context.elements:
            if elem.element_id not in self.context.drawn_elements:
                remaining.append(elem.to_dict())

        return remaining

    def mark_elements_drawn(self, element_ids: List[str]):
        """요소 그리기 완료 표시"""
        if not self.context:
            return

        for eid in element_ids:
            if eid not in self.context.drawn_elements:
                self.context.drawn_elements.append(eid)
                for elem in self.context.elements:
                    if elem.element_id == eid:
                        elem.drawn = True
                        break

        if len(self.context.drawn_elements) == len(self.context.elements):
            self.context.status = "completed"

        self._save_context()

    def mark_step_complete(self, step: int):
        """단계 완료 표시"""
        if not self.context:
            return

        self.context.current_step = step

        if step >= self.context.total_steps:
            self.context.status = "completed"

        self._save_context()


# =============================================================================
# 3. CLI 인터페이스
# =============================================================================

def cli_checklist() -> str:
    """분석 체크리스트 조회"""
    tracer = PhotoTracer()
    return json.dumps(tracer.get_analysis_checklist(), ensure_ascii=False, indent=2)


def cli_prompt() -> str:
    """분석 프롬프트 조회"""
    tracer = PhotoTracer()
    return tracer.get_analysis_prompt()


def cli_create(analysis_json: str, width: str = "800",
               origin_x: str = "50", origin_y: str = "50") -> str:
    """컨텍스트 생성"""
    try:
        tracer = PhotoTracer()
        data = json.loads(analysis_json)
        context_id = tracer.create_context(
            data,
            canvas_width=float(width),
            origin_x=float(origin_x),
            origin_y=float(origin_y)
        )
        return json.dumps({
            "success": True,
            "context_id": context_id,
            "message": "Context created. Call 'coords' to calculate coordinates."
        }, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_coords(context_id: str) -> str:
    """좌표 계산"""
    try:
        tracer = PhotoTracer()
        tracer.load_context(context_id)
        coords = tracer.calculate_coordinates()

        return json.dumps({
            "success": True,
            "context_id": context_id,
            "key_points": {k: v for k, v in coords.items() if not k.startswith("_")},
            "dimensions": {
                "width": coords["_width"],
                "height": coords["_height"],
                "eave_height": coords["_eave_height"],
                "ridge_height": coords["_ridge_height"],
                "frame_offset": coords["_frame_offset"]
            },
            "elements_generated": len(tracer.context.elements),
            "message": "Coordinates calculated. Call 'sequence' to generate MCP commands."
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_sequence(context_id: str) -> str:
    """MCP 시퀀스 생성"""
    try:
        tracer = PhotoTracer()
        tracer.load_context(context_id)

        # 좌표가 없으면 계산
        if not tracer.context.key_points:
            tracer.calculate_coordinates()

        sequence = tracer.generate_mcp_sequence()

        return json.dumps({
            "success": True,
            "context_id": context_id,
            "total_steps": len(sequence),
            "sequence": sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_status(context_id: str) -> str:
    """컨텍스트 상태 조회"""
    try:
        tracer = PhotoTracer()
        ctx = tracer.load_context(context_id)
        if not ctx:
            return json.dumps({"error": f"Context not found: {context_id}"})

        return json.dumps({
            "context_id": ctx.context_id,
            "status": ctx.status,
            "current_step": ctx.current_step,
            "total_steps": ctx.total_steps,
            "elements_total": len(ctx.elements),
            "elements_drawn": len(ctx.drawn_elements),
            "remaining": len(ctx.elements) - len(ctx.drawn_elements)
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_draw(analysis_json: str, width: str = "800",
             origin_x: str = "50", origin_y: str = "50") -> str:
    """
    통합 명령: 분석 → 좌표 계산 → 시퀀스 생성

    한 번의 호출로 전체 파이프라인 실행
    """
    try:
        tracer = PhotoTracer()
        data = json.loads(analysis_json)

        # 1. 컨텍스트 생성
        context_id = tracer.create_context(
            data,
            canvas_width=float(width),
            origin_x=float(origin_x),
            origin_y=float(origin_y)
        )

        # 2. 좌표 계산
        coords = tracer.calculate_coordinates()

        # 3. 시퀀스 생성
        sequence = tracer.generate_mcp_sequence()

        return json.dumps({
            "success": True,
            "context_id": context_id,
            "canvas": {
                "width": tracer.context.canvas_width,
                "height": tracer.context.canvas_height,
                "origin_x": tracer.context.origin_x,
                "origin_y": tracer.context.origin_y
            },
            "counts": tracer.context.element_counts.to_dict(),
            "key_features": {
                "visible_frames": tracer.context.element_counts.visible_column_frames,
                "purlin_as_depth_lines": tracer.context.element_counts.purlin_as_depth_lines,
                "h_beam_section": tracer.context.element_counts.column_section_type == "H-beam"
            },
            "total_elements": len(tracer.context.elements),
            "total_steps": len(sequence),
            "sequence": sequence
        }, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_info() -> str:
    """Photo Tracer 정보"""
    return json.dumps({
        "module": "photo_tracer",
        "description": "사진을 보고 그대로 따라 그리는 모듈",
        "핵심_원칙": [
            "3D 투영 계산이 아닌, 사진에서 보이는 것을 그대로 그린다",
            "퍼린은 짧은 마크가 아닌, 깊이 방향 수평선으로 표현",
            "겹쳐 보이는 프레임들을 offset으로 표현",
            "H-beam 단면을 여러 라인으로 표현"
        ],
        "commands": {
            "trace_checklist": "분석 체크리스트 조회",
            "trace_prompt": "분석 프롬프트 조회",
            "trace_create": "컨텍스트 생성",
            "trace_coords": "좌표 계산",
            "trace_sequence": "MCP 시퀀스 생성",
            "trace_draw": "통합 명령 (분석→좌표→시퀀스)",
            "trace_status": "컨텍스트 상태 조회",
            "trace_info": "이 정보"
        },
        "workflow": [
            "1. 사진 분석: trace_checklist 참고하여 요소 카운트",
            "2. trace_draw '<json>' 실행 (또는 create → coords → sequence)",
            "3. 생성된 sequence의 tools를 MCP로 실행"
        ],
        "example_analysis": {
            "visible_column_frames": 4,
            "visible_truss_frames": 4,
            "frame_spacing_ratio": 0.025,
            "columns_per_frame": 2,
            "column_section_type": "H-beam",
            "visible_purlin_lines": 8,
            "purlin_as_depth_lines": True,
            "truss_type": "pratt",
            "truss_panel_count": 10,
            "bracing_bays": 2,
            "width_height_ratio": 2.5,
            "eave_height_ratio": 0.72,
            "roof_pitch_degrees": 8
        }
    }, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Photo Tracer - 사진을 보고 그대로 따라 그리기")
        print("")
        print("Usage:")
        print("  python photo_tracer.py checklist         - 분석 체크리스트")
        print("  python photo_tracer.py prompt            - 분석 프롬프트")
        print("  python photo_tracer.py create '<json>'   - 컨텍스트 생성")
        print("  python photo_tracer.py coords <id>       - 좌표 계산")
        print("  python photo_tracer.py sequence <id>     - 시퀀스 생성")
        print("  python photo_tracer.py status <id>       - 상태 조회")
        print("  python photo_tracer.py draw '<json>'     - 통합 명령")
        print("  python photo_tracer.py info              - 정보")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "checklist":
        print(cli_checklist())
    elif cmd == "prompt":
        print(cli_prompt())
    elif cmd == "create" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        ox = sys.argv[4] if len(sys.argv) > 4 else "50"
        oy = sys.argv[5] if len(sys.argv) > 5 else "50"
        print(cli_create(sys.argv[2], w, ox, oy))
    elif cmd == "coords" and len(sys.argv) > 2:
        print(cli_coords(sys.argv[2]))
    elif cmd == "sequence" and len(sys.argv) > 2:
        print(cli_sequence(sys.argv[2]))
    elif cmd == "status" and len(sys.argv) > 2:
        print(cli_status(sys.argv[2]))
    elif cmd == "draw" and len(sys.argv) > 2:
        w = sys.argv[3] if len(sys.argv) > 3 else "800"
        ox = sys.argv[4] if len(sys.argv) > 4 else "50"
        oy = sys.argv[5] if len(sys.argv) > 5 else "50"
        print(cli_draw(sys.argv[2], w, ox, oy))
    elif cmd == "info":
        print(cli_info())
    else:
        print(json.dumps({"error": f"Unknown command: {cmd}"}))

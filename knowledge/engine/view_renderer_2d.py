"""
2D View Renderer Module
=======================
사진/이미지를 보고 똑같은 2D 도면을 그리기 위한 모듈.

이 모듈의 핵심 철학:
- 3D 투영 계산이 아닌, 사진에서 "보이는 그대로"를 2D로 재현
- 사진의 비율과 요소 개수를 분석하여 정확한 좌표 계산
- 반복 요소(기둥, 퍼린, 트러스 부재)의 등간격 배치

사용 워크플로우:
1. 사진 분석 → 비율 및 요소 개수 추출
2. 기준 치수 설정 (전체 폭, 높이)
3. 비율 기반 자동 좌표 계산
4. 도면 생성
"""

import math
from typing import List, Tuple, Dict, Optional, Any
from dataclasses import dataclass, field


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


@dataclass
class ProportionAnalysis:
    """
    사진에서 추출한 비율 분석 결과.

    이 클래스는 사진을 분석하여 얻은 비율 정보를 저장합니다.
    모든 값은 비율로 저장되어, 실제 치수는 나중에 계산합니다.
    """
    # 전체 비율
    width_height_ratio: float = 2.0  # 가로:세로 (예: 2.0 = 2:1)

    # 지붕 비율
    roof_pitch_ratio: float = 0.15  # 지붕높이 / 전체폭의 절반 (경사 표현)
    eave_height_ratio: float = 0.7  # 처마높이 / 전체높이

    # 요소 개수
    column_count: int = 3  # 기둥 개수 (한쪽 프레임)
    truss_panel_count: int = 8  # 트러스 패널 수 (상현재 분할)
    purlin_count_per_slope: int = 5  # 퍼린 개수 (한쪽 경사면)
    vertical_web_count: int = 7  # 수직 웹부재 개수
    diagonal_web_count: int = 14  # 대각 웹부재 개수

    # 트러스 유형
    truss_type: str = "warren"  # warren, pratt, howe

    # 추가 요소
    has_bracing: bool = True
    bracing_type: str = "x"  # x, v, k


@dataclass
class DrawingConfig:
    """
    도면 설정.

    실제 치수와 캔버스 설정을 정의합니다.
    """
    # 기준 치수 (mm 또는 선택한 단위)
    total_width: float = 800  # 전체 폭
    total_height: float = 400  # 전체 높이 (width_height_ratio로 자동 계산 가능)

    # 캔버스 위치
    origin_x: float = 50  # 시작 X 좌표
    origin_y: float = 50  # 시작 Y 좌표

    # 레이어 설정
    column_layer: str = "COLUMN"
    beam_layer: str = "BEAM"
    truss_layer: str = "TRUSS"
    purlin_layer: str = "PURLIN"
    bracing_layer: str = "BRACING"
    dimension_layer: str = "DIMENSION"


class View2DRenderer:
    """
    2D 뷰 렌더러.

    사진의 비율 분석 결과를 바탕으로 2D 도면을 생성합니다.
    핵심 기능:
    - 비율 기반 좌표 계산
    - 반복 요소 등간격 배치
    - 트러스 패턴 생성
    """

    def __init__(self, proportions: ProportionAnalysis = None,
                 config: DrawingConfig = None):
        """
        렌더러 초기화.

        Args:
            proportions: 사진 분석 결과 (비율 정보)
            config: 도면 설정 (실제 치수)
        """
        self.proportions = proportions or ProportionAnalysis()
        self.config = config or DrawingConfig()
        self.commands: List[Dict[str, Any]] = []

        # 계산된 좌표 캐시
        self._calculated_points: Dict[str, Point2D] = {}

    def clear_commands(self):
        """저장된 명령 초기화"""
        self.commands = []
        self._calculated_points = {}

    # ===========================================
    # 좌표 계산 메서드
    # ===========================================

    def calculate_key_points(self) -> Dict[str, Point2D]:
        """
        주요 기준점 계산.

        사진의 비율을 바탕으로 도면의 핵심 좌표를 계산합니다.

        Returns:
            주요 점 딕셔너리 (이름: Point2D)
        """
        p = self.proportions
        c = self.config

        # 기본 좌표
        origin = Point2D(c.origin_x, c.origin_y)
        width = c.total_width

        # 높이 계산 (비율 기반)
        height = width / p.width_height_ratio

        # 처마 높이
        eave_height = height * p.eave_height_ratio

        # 지붕 최고점 높이
        ridge_rise = (width / 2) * p.roof_pitch_ratio
        ridge_height = eave_height + ridge_rise

        points = {
            # 바닥 좌표
            "bottom_left": Point2D(origin.x, origin.y),
            "bottom_right": Point2D(origin.x + width, origin.y),
            "bottom_center": Point2D(origin.x + width/2, origin.y),

            # 처마 좌표
            "eave_left": Point2D(origin.x, origin.y + eave_height),
            "eave_right": Point2D(origin.x + width, origin.y + eave_height),

            # 지붕 최고점
            "ridge": Point2D(origin.x + width/2, origin.y + ridge_height),

            # 메타 정보
            "_width": Point2D(width, 0),
            "_height": Point2D(0, height),
            "_eave_height": Point2D(0, eave_height),
            "_ridge_height": Point2D(0, ridge_height),
        }

        self._calculated_points = points
        return points

    def calculate_column_positions(self) -> List[float]:
        """
        기둥 X 좌표 계산.

        기둥을 등간격으로 배치합니다.

        Returns:
            기둥 X 좌표 리스트
        """
        p = self.proportions
        c = self.config

        if p.column_count < 2:
            return [c.origin_x, c.origin_x + c.total_width]

        spacing = c.total_width / (p.column_count - 1)
        return [c.origin_x + spacing * i for i in range(p.column_count)]

    def calculate_purlin_positions(self, start: Point2D, end: Point2D,
                                   count: int) -> List[Point2D]:
        """
        퍼린 위치 계산 (경사면 따라).

        시작점과 끝점 사이에 퍼린을 등간격으로 배치합니다.

        Args:
            start: 시작점 (처마)
            end: 끝점 (용마루)
            count: 퍼린 개수

        Returns:
            퍼린 위치 리스트
        """
        if count < 1:
            return []

        positions = []
        for i in range(1, count + 1):
            t = i / (count + 1)  # 0과 1 사이의 비율
            x = start.x + (end.x - start.x) * t
            y = start.y + (end.y - start.y) * t
            positions.append(Point2D(x, y))

        return positions

    def calculate_truss_nodes(self, start: Point2D, end: Point2D,
                              panel_count: int) -> Tuple[List[Point2D], List[Point2D]]:
        """
        트러스 노드 계산 (상현재, 하현재).

        Args:
            start: 시작점 (처마)
            end: 끝점 (용마루)
            panel_count: 패널 수 (상현재 분할 수)

        Returns:
            (상현재 노드 리스트, 하현재 노드 리스트)
        """
        # 상현재 노드 (경사면 따라)
        top_chord = [start]
        for i in range(1, panel_count):
            t = i / panel_count
            x = start.x + (end.x - start.x) * t
            y = start.y + (end.y - start.y) * t
            top_chord.append(Point2D(x, y))
        top_chord.append(end)

        # 하현재 노드 (수평)
        bottom_y = start.y
        bottom_chord = []
        for i in range(panel_count + 1):
            t = i / panel_count
            x = start.x + (end.x - start.x) * t
            bottom_chord.append(Point2D(x, bottom_y))

        return top_chord, bottom_chord

    # ===========================================
    # 도면 요소 생성 메서드
    # ===========================================

    def add_line(self, start: Point2D, end: Point2D,
                 layer: str = "0", color: int = None):
        """선 추가"""
        cmd = {
            "type": "line",
            "start": start.to_dict(),
            "end": end.to_dict(),
            "layer": layer
        }
        if color:
            cmd["color"] = color
        self.commands.append(cmd)

    def add_polyline(self, vertices: List[Point2D],
                     layer: str = "0", closed: bool = False):
        """폴리라인 추가"""
        cmd = {
            "type": "polyline",
            "vertices": [v.to_dict() for v in vertices],
            "layer": layer,
            "closed": closed
        }
        self.commands.append(cmd)

    # ===========================================
    # 구조 요소 그리기
    # ===========================================

    def draw_portal_frame_elevation(self) -> Dict[str, int]:
        """
        포털 프레임 정면도 그리기.

        사진과 같은 정면도를 그립니다:
        - 기둥 (수직선)
        - 경사 지붕 (좌/우 경사)
        - 기초선

        Returns:
            생성된 요소 개수 딕셔너리
        """
        points = self.calculate_key_points()
        c = self.config

        counts = {"columns": 0, "rafters": 0, "eave_beams": 0}

        # 기둥 그리기
        column_xs = self.calculate_column_positions()
        eave_y = points["eave_left"].y

        for x in column_xs:
            self.add_line(
                Point2D(x, c.origin_y),
                Point2D(x, eave_y),
                c.column_layer
            )
            counts["columns"] += 1

        # 좌측 경사 지붕 (처마 → 용마루)
        self.add_line(points["eave_left"], points["ridge"], c.beam_layer)
        counts["rafters"] += 1

        # 우측 경사 지붕 (용마루 → 처마)
        self.add_line(points["ridge"], points["eave_right"], c.beam_layer)
        counts["rafters"] += 1

        # 처마 수평선 (옵션)
        self.add_line(points["eave_left"], points["eave_right"], c.beam_layer)
        counts["eave_beams"] += 1

        # 기초선
        self.add_line(points["bottom_left"], points["bottom_right"], "FOUNDATION")

        return counts

    def draw_truss_frame(self, side: str = "left") -> Dict[str, int]:
        """
        트러스 프레임 그리기.

        지정된 측면의 트러스 구조를 그립니다:
        - 상현재 (경사)
        - 하현재 (수평 또는 경사)
        - 웹부재 (수직 + 대각선)

        Args:
            side: "left" 또는 "right"

        Returns:
            생성된 요소 개수
        """
        points = self.calculate_key_points()
        p = self.proportions
        c = self.config

        counts = {"top_chord": 0, "bottom_chord": 0, "web_members": 0}

        # 시작점과 끝점 결정
        if side == "left":
            start = points["eave_left"]
            end = points["ridge"]
        else:
            start = points["eave_right"]
            end = points["ridge"]

        # 트러스 노드 계산
        top_nodes, bottom_nodes = self.calculate_truss_nodes(
            start, end, p.truss_panel_count // 2
        )

        # 상현재 그리기
        for i in range(len(top_nodes) - 1):
            self.add_line(top_nodes[i], top_nodes[i+1], c.truss_layer)
            counts["top_chord"] += 1

        # 하현재 그리기
        for i in range(len(bottom_nodes) - 1):
            self.add_line(bottom_nodes[i], bottom_nodes[i+1], c.truss_layer)
            counts["bottom_chord"] += 1

        # 웹부재 그리기 (트러스 유형에 따라)
        if p.truss_type == "warren":
            counts["web_members"] = self._draw_warren_web(
                top_nodes, bottom_nodes, c.truss_layer
            )
        elif p.truss_type == "pratt":
            counts["web_members"] = self._draw_pratt_web(
                top_nodes, bottom_nodes, c.truss_layer
            )
        elif p.truss_type == "howe":
            counts["web_members"] = self._draw_howe_web(
                top_nodes, bottom_nodes, c.truss_layer
            )

        return counts

    def _draw_warren_web(self, top: List[Point2D], bottom: List[Point2D],
                         layer: str) -> int:
        """워렌 트러스 웹부재 (지그재그 대각선만)"""
        count = 0

        for i in range(len(bottom) - 1):
            # 대각선: bottom[i] -> top[i] 또는 top[i+1]
            if i < len(top) - 1:
                if i % 2 == 0:
                    self.add_line(bottom[i], top[i], layer)
                else:
                    self.add_line(bottom[i], top[i], layer)
                count += 1

            if i + 1 < len(top):
                if i % 2 == 0:
                    self.add_line(bottom[i], top[i+1], layer)
                else:
                    self.add_line(top[i], bottom[i+1], layer)
                count += 1

        return count

    def _draw_pratt_web(self, top: List[Point2D], bottom: List[Point2D],
                        layer: str) -> int:
        """프랫 트러스 웹부재 (수직 + 중앙향 대각선)"""
        count = 0

        # 수직 부재
        for i in range(len(bottom)):
            if i < len(top):
                self.add_line(bottom[i], top[i], layer)
                count += 1

        # 대각선 (중앙을 향함)
        mid = len(bottom) // 2
        for i in range(len(bottom) - 1):
            if i < mid and i + 1 < len(top):
                self.add_line(bottom[i+1], top[i], layer)
                count += 1
            elif i >= mid and i + 1 < len(top):
                self.add_line(bottom[i], top[i+1], layer)
                count += 1

        return count

    def _draw_howe_web(self, top: List[Point2D], bottom: List[Point2D],
                       layer: str) -> int:
        """하우 트러스 웹부재 (수직 + 외향 대각선)"""
        count = 0

        # 수직 부재
        for i in range(len(bottom)):
            if i < len(top):
                self.add_line(bottom[i], top[i], layer)
                count += 1

        # 대각선 (외향)
        mid = len(bottom) // 2
        for i in range(len(bottom) - 1):
            if i < mid and i < len(top):
                self.add_line(bottom[i], top[i+1], layer)
                count += 1
            elif i >= mid and i + 1 < len(bottom):
                self.add_line(bottom[i+1], top[i], layer)
                count += 1

        return count

    def draw_purlins(self) -> int:
        """
        퍼린 그리기 (지붕 경사면의 수평 부재).

        양쪽 경사면에 퍼린을 등간격으로 배치합니다.
        퍼린은 짧은 수평선으로 표현됩니다.

        Returns:
            생성된 퍼린 개수
        """
        points = self.calculate_key_points()
        p = self.proportions
        c = self.config

        count = 0
        purlin_mark_length = c.total_width * 0.02  # 퍼린 마크 길이

        # 좌측 경사면 퍼린
        left_purlins = self.calculate_purlin_positions(
            points["eave_left"], points["ridge"],
            p.purlin_count_per_slope
        )

        for pos in left_purlins:
            # 짧은 수평선으로 퍼린 표시
            self.add_line(
                Point2D(pos.x - purlin_mark_length/2, pos.y),
                Point2D(pos.x + purlin_mark_length/2, pos.y),
                c.purlin_layer
            )
            count += 1

        # 우측 경사면 퍼린
        right_purlins = self.calculate_purlin_positions(
            points["eave_right"], points["ridge"],
            p.purlin_count_per_slope
        )

        for pos in right_purlins:
            self.add_line(
                Point2D(pos.x - purlin_mark_length/2, pos.y),
                Point2D(pos.x + purlin_mark_length/2, pos.y),
                c.purlin_layer
            )
            count += 1

        return count

    def draw_x_bracing(self, bay_index: int = 0) -> int:
        """
        X-가새 그리기.

        Args:
            bay_index: 베이 인덱스 (0부터 시작)

        Returns:
            생성된 가새 개수
        """
        column_xs = self.calculate_column_positions()
        points = self.calculate_key_points()
        c = self.config

        if bay_index >= len(column_xs) - 1:
            return 0

        x1 = column_xs[bay_index]
        x2 = column_xs[bay_index + 1]
        y_bottom = c.origin_y
        y_top = points["eave_left"].y

        # X 대각선
        self.add_line(
            Point2D(x1, y_bottom),
            Point2D(x2, y_top),
            c.bracing_layer
        )
        self.add_line(
            Point2D(x2, y_bottom),
            Point2D(x1, y_top),
            c.bracing_layer
        )

        return 2

    # ===========================================
    # 전체 도면 생성
    # ===========================================

    def draw_complete_elevation(self,
                                include_truss: bool = True,
                                include_purlins: bool = True,
                                include_bracing: bool = True) -> Dict[str, Any]:
        """
        완전한 정면도 생성.

        사진과 동일한 모습의 정면도를 생성합니다.

        Args:
            include_truss: 트러스 포함 여부
            include_purlins: 퍼린 포함 여부
            include_bracing: 가새 포함 여부

        Returns:
            생성 결과 요약
        """
        self.clear_commands()

        result = {
            "elements": {},
            "total_entities": 0
        }

        # 1. 기본 프레임 (기둥, 지붕)
        frame_counts = self.draw_portal_frame_elevation()
        result["elements"]["frame"] = frame_counts

        # 2. 트러스 (옵션)
        if include_truss:
            left_truss = self.draw_truss_frame("left")
            right_truss = self.draw_truss_frame("right")
            result["elements"]["truss_left"] = left_truss
            result["elements"]["truss_right"] = right_truss

        # 3. 퍼린 (옵션)
        if include_purlins:
            purlin_count = self.draw_purlins()
            result["elements"]["purlins"] = purlin_count

        # 4. 가새 (옵션)
        if include_bracing and self.proportions.has_bracing:
            bracing_count = 0
            # 첫 번째와 마지막 베이에 가새
            column_xs = self.calculate_column_positions()
            if len(column_xs) >= 2:
                bracing_count += self.draw_x_bracing(0)
            if len(column_xs) >= 3:
                bracing_count += self.draw_x_bracing(len(column_xs) - 2)
            result["elements"]["bracing"] = bracing_count

        result["total_entities"] = len(self.commands)
        return result

    # ===========================================
    # MCP 명령 생성
    # ===========================================

    def get_mcp_commands(self) -> List[Dict[str, Any]]:
        """MCP 도구 명령 리스트 반환"""
        return self.commands

    def generate_mcp_script(self) -> str:
        """사람이 읽을 수 있는 MCP 명령 스크립트 생성"""
        lines = ["# 2D View Drawing Commands", ""]

        for i, cmd in enumerate(self.commands):
            if cmd["type"] == "line":
                s = cmd["start"]
                e = cmd["end"]
                layer = cmd.get("layer", "0")
                lines.append(f"{i+1}. LINE: ({s['x']:.1f}, {s['y']:.1f}) -> ({e['x']:.1f}, {e['y']:.1f}) [{layer}]")
            elif cmd["type"] == "polyline":
                verts = cmd["vertices"]
                layer = cmd.get("layer", "0")
                closed = "CLOSED" if cmd.get("closed") else "OPEN"
                lines.append(f"{i+1}. PLINE: {len(verts)} vertices [{layer}] {closed}")

        lines.append("")
        lines.append(f"Total: {len(self.commands)} entities")

        return "\n".join(lines)


# ===========================================
# 헬퍼 함수
# ===========================================

def analyze_proportions_from_description(description: Dict[str, Any]) -> ProportionAnalysis:
    """
    사진 설명에서 비율 분석 객체 생성.

    Args:
        description: 사진 분석 설명 딕셔너리
        예: {
            "width_height_ratio": 2.5,
            "roof_pitch_degrees": 10,
            "column_count": 4,
            "truss_type": "warren",
            ...
        }

    Returns:
        ProportionAnalysis 객체
    """
    props = ProportionAnalysis()

    if "width_height_ratio" in description:
        props.width_height_ratio = description["width_height_ratio"]

    if "roof_pitch_degrees" in description:
        # 각도를 비율로 변환 (tan)
        angle_rad = math.radians(description["roof_pitch_degrees"])
        props.roof_pitch_ratio = math.tan(angle_rad)
    elif "roof_pitch_ratio" in description:
        props.roof_pitch_ratio = description["roof_pitch_ratio"]

    if "eave_height_ratio" in description:
        props.eave_height_ratio = description["eave_height_ratio"]

    if "column_count" in description:
        props.column_count = description["column_count"]

    if "truss_panel_count" in description:
        props.truss_panel_count = description["truss_panel_count"]

    if "purlin_count_per_slope" in description:
        props.purlin_count_per_slope = description["purlin_count_per_slope"]

    if "truss_type" in description:
        props.truss_type = description["truss_type"]

    if "has_bracing" in description:
        props.has_bracing = description["has_bracing"]

    return props


def create_drawing_from_photo_analysis(
    analysis: Dict[str, Any],
    total_width: float = 800,
    origin_x: float = 50,
    origin_y: float = 50
) -> View2DRenderer:
    """
    사진 분석 결과로부터 도면 생성기 생성.

    편의 함수로, 분석 결과를 받아 바로 그릴 수 있는
    렌더러를 반환합니다.

    Args:
        analysis: 사진 분석 결과 딕셔너리
        total_width: 도면 전체 폭
        origin_x: 시작 X 좌표
        origin_y: 시작 Y 좌표

    Returns:
        설정된 View2DRenderer 인스턴스
    """
    proportions = analyze_proportions_from_description(analysis)

    config = DrawingConfig(
        total_width=total_width,
        origin_x=origin_x,
        origin_y=origin_y
    )

    return View2DRenderer(proportions, config)


# ===========================================
# 예제 사용법
# ===========================================

if __name__ == "__main__":
    # 예제: 산업용 건물 사진 분석 결과
    photo_analysis = {
        "width_height_ratio": 2.5,  # 넓은 산업용 건물
        "roof_pitch_degrees": 8,    # 낮은 경사
        "eave_height_ratio": 0.72,  # 처마 높이 비율
        "column_count": 4,          # 기둥 4개
        "truss_panel_count": 10,    # 트러스 10패널
        "purlin_count_per_slope": 6,# 퍼린 6개/경사면
        "truss_type": "pratt",      # 프랫 트러스
        "has_bracing": True
    }

    # 렌더러 생성
    renderer = create_drawing_from_photo_analysis(
        photo_analysis,
        total_width=600,
        origin_x=100,
        origin_y=50
    )

    # 도면 생성
    result = renderer.draw_complete_elevation()

    print("Generated Drawing Summary:")
    print(f"Total entities: {result['total_entities']}")
    for category, counts in result["elements"].items():
        print(f"  {category}: {counts}")

    print("\nMCP Commands Preview:")
    print(renderer.generate_mcp_script()[:500] + "...")

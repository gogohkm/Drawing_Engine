"""
PositionalLineExtractor: 위치 기반 선 추출기

이 모듈은 사진에서 선을 추출할 때 "기둥", "보", "퍼린" 등으로 분류하지 않고,
순수하게 **위치 기반**으로 좌표화합니다.

핵심 철학:
- 선의 "의미"를 판단하지 않음
- 오직 "위치"만 기록: 사진의 어느 영역에 있는지
- 모든 선을 빠짐없이 추출하는 것이 목표

위치 컨텍스트 예시:
- "upper-left quadrant, near edge"
- "center-right, vertical orientation"
- "bottom region, horizontal line"
"""

import cv2
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from enum import Enum
import json


class Region(Enum):
    """이미지를 9개 영역으로 분할"""
    TOP_LEFT = "top-left"
    TOP_CENTER = "top-center"
    TOP_RIGHT = "top-right"
    MIDDLE_LEFT = "middle-left"
    MIDDLE_CENTER = "middle-center"
    MIDDLE_RIGHT = "middle-right"
    BOTTOM_LEFT = "bottom-left"
    BOTTOM_CENTER = "bottom-center"
    BOTTOM_RIGHT = "bottom-right"


class Orientation(Enum):
    """선의 방향"""
    HORIZONTAL = "horizontal"      # 0° ~ 15° or 165° ~ 180°
    VERTICAL = "vertical"          # 75° ~ 105°
    DIAGONAL_UP = "diagonal-up"    # 15° ~ 75° (오른쪽 위로)
    DIAGONAL_DOWN = "diagonal-down"  # 105° ~ 165° (오른쪽 아래로)


@dataclass
class PositionalLine:
    """위치 기반 선 데이터"""
    id: int                          # 고유 ID

    # 픽셀 좌표 (원본)
    start_px: Tuple[int, int]        # (x, y) 시작점
    end_px: Tuple[int, int]          # (x, y) 끝점

    # 정규화 좌표 (0~1 범위)
    start_norm: Tuple[float, float]  # 정규화된 시작점
    end_norm: Tuple[float, float]    # 정규화된 끝점

    # 위치 컨텍스트
    start_region: str                # 시작점이 속한 영역
    end_region: str                  # 끝점이 속한 영역
    orientation: str                 # 선의 방향

    # 추가 정보
    length_px: float                 # 픽셀 단위 길이
    length_norm: float               # 정규화된 길이
    angle_deg: float                 # 각도 (도)

    # 위치 설명 (사람이 읽을 수 있는)
    position_description: str        # "upper-left to upper-center, horizontal"

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "start_px": self.start_px,
            "end_px": self.end_px,
            "start_norm": self.start_norm,
            "end_norm": self.end_norm,
            "start_region": self.start_region,
            "end_region": self.end_region,
            "orientation": self.orientation,
            "length_px": self.length_px,
            "length_norm": self.length_norm,
            "angle_deg": self.angle_deg,
            "position_description": self.position_description
        }


@dataclass
class ExtractionResult:
    """추출 결과"""
    image_width: int
    image_height: int
    total_lines: int
    lines: List[PositionalLine]

    # 영역별 통계
    lines_by_region: Dict[str, int] = field(default_factory=dict)
    lines_by_orientation: Dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return {
            "image_size": {"width": self.image_width, "height": self.image_height},
            "total_lines": self.total_lines,
            "lines_by_region": self.lines_by_region,
            "lines_by_orientation": self.lines_by_orientation,
            "lines": [line.to_dict() for line in self.lines]
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


class PositionalLineExtractor:
    """
    위치 기반 선 추출기

    사진에서 모든 선을 추출하고, 각 선의 위치를 기록합니다.
    선의 "의미"(기둥, 보 등)는 판단하지 않습니다.
    """

    def __init__(self,
                 min_line_length: int = 30,
                 max_line_gap: int = 10,
                 canny_low: int = 50,
                 canny_high: int = 150,
                 hough_threshold: int = 50):
        """
        Args:
            min_line_length: 최소 선 길이 (픽셀)
            max_line_gap: 선 연결을 위한 최대 갭
            canny_low: Canny 엣지 검출 하한 임계값
            canny_high: Canny 엣지 검출 상한 임계값
            hough_threshold: Hough 변환 임계값
        """
        self.min_line_length = min_line_length
        self.max_line_gap = max_line_gap
        self.canny_low = canny_low
        self.canny_high = canny_high
        self.hough_threshold = hough_threshold

    def extract_lines(self, image_path: str) -> ExtractionResult:
        """
        이미지에서 모든 선을 추출합니다.

        Args:
            image_path: 이미지 파일 경로

        Returns:
            ExtractionResult: 추출된 모든 선의 위치 정보
        """
        # 이미지 로드
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"이미지를 로드할 수 없습니다: {image_path}")

        height, width = image.shape[:2]

        # 그레이스케일 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 노이즈 제거
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 엣지 검출
        edges = cv2.Canny(blurred, self.canny_low, self.canny_high)

        # Hough 변환으로 선 검출
        lines_p = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi / 180,
            threshold=self.hough_threshold,
            minLineLength=self.min_line_length,
            maxLineGap=self.max_line_gap
        )

        # 결과 처리
        positional_lines = []
        lines_by_region = {}
        lines_by_orientation = {}

        if lines_p is not None:
            for idx, line in enumerate(lines_p):
                x1, y1, x2, y2 = line[0]

                # PositionalLine 생성
                pos_line = self._create_positional_line(
                    idx, x1, y1, x2, y2, width, height
                )
                positional_lines.append(pos_line)

                # 통계 업데이트
                for region in [pos_line.start_region, pos_line.end_region]:
                    lines_by_region[region] = lines_by_region.get(region, 0) + 1
                lines_by_orientation[pos_line.orientation] = \
                    lines_by_orientation.get(pos_line.orientation, 0) + 1

        return ExtractionResult(
            image_width=width,
            image_height=height,
            total_lines=len(positional_lines),
            lines=positional_lines,
            lines_by_region=lines_by_region,
            lines_by_orientation=lines_by_orientation
        )

    def extract_lines_lsd(self, image_path: str) -> ExtractionResult:
        """
        LSD (Line Segment Detector) 알고리즘으로 선 추출
        더 정확한 선 검출이 가능합니다.

        Args:
            image_path: 이미지 파일 경로

        Returns:
            ExtractionResult: 추출된 모든 선의 위치 정보
        """
        # 이미지 로드
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"이미지를 로드할 수 없습니다: {image_path}")

        height, width = image.shape[:2]

        # 그레이스케일 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # LSD 선 검출
        lsd = cv2.createLineSegmentDetector(0)
        lines, _, _, _ = lsd.detect(gray)

        # 결과 처리
        positional_lines = []
        lines_by_region = {}
        lines_by_orientation = {}

        if lines is not None:
            for idx, line in enumerate(lines):
                x1, y1, x2, y2 = line[0]

                # 최소 길이 필터링
                length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if length < self.min_line_length:
                    continue

                # PositionalLine 생성
                pos_line = self._create_positional_line(
                    len(positional_lines),
                    int(x1), int(y1), int(x2), int(y2),
                    width, height
                )
                positional_lines.append(pos_line)

                # 통계 업데이트
                for region in [pos_line.start_region, pos_line.end_region]:
                    lines_by_region[region] = lines_by_region.get(region, 0) + 1
                lines_by_orientation[pos_line.orientation] = \
                    lines_by_orientation.get(pos_line.orientation, 0) + 1

        return ExtractionResult(
            image_width=width,
            image_height=height,
            total_lines=len(positional_lines),
            lines=positional_lines,
            lines_by_region=lines_by_region,
            lines_by_orientation=lines_by_orientation
        )

    def _create_positional_line(self, idx: int,
                                 x1: int, y1: int,
                                 x2: int, y2: int,
                                 img_width: int, img_height: int) -> PositionalLine:
        """PositionalLine 객체 생성"""

        # 정규화 좌표 (0~1)
        start_norm = (x1 / img_width, y1 / img_height)
        end_norm = (x2 / img_width, y2 / img_height)

        # 영역 계산
        start_region = self._get_region(x1, y1, img_width, img_height)
        end_region = self._get_region(x2, y2, img_width, img_height)

        # 길이 계산
        length_px = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        length_norm = np.sqrt((end_norm[0] - start_norm[0])**2 +
                              (end_norm[1] - start_norm[1])**2)

        # 각도 계산 (0~180도)
        angle_rad = np.arctan2(y2 - y1, x2 - x1)
        angle_deg = np.degrees(angle_rad) % 180

        # 방향 판단
        orientation = self._get_orientation(angle_deg)

        # 위치 설명 생성
        position_desc = self._create_position_description(
            start_region, end_region, orientation
        )

        return PositionalLine(
            id=idx,
            start_px=(x1, y1),
            end_px=(x2, y2),
            start_norm=start_norm,
            end_norm=end_norm,
            start_region=start_region,
            end_region=end_region,
            orientation=orientation,
            length_px=length_px,
            length_norm=length_norm,
            angle_deg=angle_deg,
            position_description=position_desc
        )

    def _get_region(self, x: int, y: int,
                    img_width: int, img_height: int) -> str:
        """좌표가 속한 영역 반환 (9분할)"""

        # X 위치 (left, center, right)
        if x < img_width / 3:
            x_region = "left"
        elif x < 2 * img_width / 3:
            x_region = "center"
        else:
            x_region = "right"

        # Y 위치 (top, middle, bottom)
        if y < img_height / 3:
            y_region = "top"
        elif y < 2 * img_height / 3:
            y_region = "middle"
        else:
            y_region = "bottom"

        return f"{y_region}-{x_region}"

    def _get_orientation(self, angle_deg: float) -> str:
        """각도에 따른 방향 반환"""

        if angle_deg < 15 or angle_deg > 165:
            return Orientation.HORIZONTAL.value
        elif 75 <= angle_deg <= 105:
            return Orientation.VERTICAL.value
        elif 15 <= angle_deg < 75:
            return Orientation.DIAGONAL_UP.value
        else:  # 105 < angle_deg <= 165
            return Orientation.DIAGONAL_DOWN.value

    def _create_position_description(self, start_region: str,
                                     end_region: str,
                                     orientation: str) -> str:
        """사람이 읽을 수 있는 위치 설명 생성"""

        if start_region == end_region:
            return f"{start_region}, {orientation}"
        else:
            return f"{start_region} to {end_region}, {orientation}"


class MCPSequenceGenerator:
    """
    추출된 선을 MCP 시퀀스로 변환

    DXF 파일 생성을 위한 MCP 명령어 시퀀스를 생성합니다.
    """

    def __init__(self, drawing_width: float = 1000, drawing_height: float = 600):
        """
        Args:
            drawing_width: 도면 너비 (단위: mm 또는 원하는 단위)
            drawing_height: 도면 높이
        """
        self.drawing_width = drawing_width
        self.drawing_height = drawing_height

    def generate_mcp_sequence(self, result: ExtractionResult,
                              layer_name: str = "EXTRACTED_LINES") -> List[Dict]:
        """
        추출 결과를 MCP 시퀀스로 변환

        Args:
            result: 선 추출 결과
            layer_name: 선을 배치할 레이어 이름

        Returns:
            MCP 명령어 시퀀스 (딕셔너리 리스트)
        """
        mcp_sequence = []

        # 1. 레이어 생성
        mcp_sequence.append({
            "tool": "create_layer",
            "params": {"name": layer_name, "color": 7}  # 흰색
        })

        # 2. 현재 레이어 설정
        mcp_sequence.append({
            "tool": "set_current_layer",
            "params": {"name": layer_name}
        })

        # 3. 각 선을 도면 좌표로 변환하여 생성
        for line in result.lines:
            # 정규화 좌표를 도면 좌표로 변환
            # Y축은 반전 (이미지는 위가 0, 도면은 아래가 0)
            start_x = line.start_norm[0] * self.drawing_width
            start_y = (1 - line.start_norm[1]) * self.drawing_height
            end_x = line.end_norm[0] * self.drawing_width
            end_y = (1 - line.end_norm[1]) * self.drawing_height

            mcp_sequence.append({
                "tool": "create_line",
                "params": {
                    "start": {"x": round(start_x, 2), "y": round(start_y, 2)},
                    "end": {"x": round(end_x, 2), "y": round(end_y, 2)}
                },
                "metadata": {
                    "line_id": line.id,
                    "position": line.position_description,
                    "original_px": {
                        "start": line.start_px,
                        "end": line.end_px
                    }
                }
            })

        # 4. 전체 보기
        mcp_sequence.append({
            "tool": "zoom_extents",
            "params": {}
        })

        return mcp_sequence

    def generate_region_based_mcp(self, result: ExtractionResult) -> List[Dict]:
        """
        영역별로 다른 레이어에 선을 배치하는 MCP 시퀀스 생성

        각 영역(top-left, middle-center 등)마다 별도의 레이어를 생성합니다.
        """
        mcp_sequence = []

        # 영역별 색상 매핑
        region_colors = {
            "top-left": 1,      # 빨강
            "top-center": 2,    # 노랑
            "top-right": 3,     # 초록
            "middle-left": 4,   # 청록
            "middle-center": 5, # 파랑
            "middle-right": 6,  # 마젠타
            "bottom-left": 30,  # 주황
            "bottom-center": 40,# 연두
            "bottom-right": 7,  # 흰색
        }

        # 영역별로 선 분류
        lines_by_start_region = {}
        for line in result.lines:
            region = line.start_region
            if region not in lines_by_start_region:
                lines_by_start_region[region] = []
            lines_by_start_region[region].append(line)

        # 각 영역에 대해 레이어 생성 및 선 그리기
        for region, lines in lines_by_start_region.items():
            layer_name = f"LINES_{region.upper().replace('-', '_')}"
            color = region_colors.get(region, 7)

            # 레이어 생성
            mcp_sequence.append({
                "tool": "create_layer",
                "params": {"name": layer_name, "color": color}
            })

            # 레이어 설정
            mcp_sequence.append({
                "tool": "set_current_layer",
                "params": {"name": layer_name}
            })

            # 선 그리기
            for line in lines:
                start_x = line.start_norm[0] * self.drawing_width
                start_y = (1 - line.start_norm[1]) * self.drawing_height
                end_x = line.end_norm[0] * self.drawing_width
                end_y = (1 - line.end_norm[1]) * self.drawing_height

                mcp_sequence.append({
                    "tool": "create_line",
                    "params": {
                        "start": {"x": round(start_x, 2), "y": round(start_y, 2)},
                        "end": {"x": round(end_x, 2), "y": round(end_y, 2)}
                    },
                    "metadata": {
                        "line_id": line.id,
                        "region": region,
                        "orientation": line.orientation
                    }
                })

        # 전체 보기
        mcp_sequence.append({
            "tool": "zoom_extents",
            "params": {}
        })

        return mcp_sequence


def extract_and_draw(image_path: str,
                     output_json: Optional[str] = None,
                     drawing_width: float = 1000,
                     drawing_height: float = 600,
                     use_lsd: bool = True,
                     min_line_length: int = 30) -> Tuple[ExtractionResult, List[Dict]]:
    """
    이미지에서 선을 추출하고 MCP 시퀀스 생성

    Args:
        image_path: 입력 이미지 경로
        output_json: 결과를 저장할 JSON 파일 경로 (선택)
        drawing_width: 도면 너비
        drawing_height: 도면 높이
        use_lsd: LSD 알고리즘 사용 여부 (True: LSD, False: Hough)
        min_line_length: 최소 선 길이

    Returns:
        (ExtractionResult, MCP 시퀀스)
    """
    # 추출기 생성
    extractor = PositionalLineExtractor(min_line_length=min_line_length)

    # 선 추출
    if use_lsd:
        result = extractor.extract_lines_lsd(image_path)
    else:
        result = extractor.extract_lines(image_path)

    # MCP 시퀀스 생성
    generator = MCPSequenceGenerator(drawing_width, drawing_height)
    mcp_sequence = generator.generate_region_based_mcp(result)

    # JSON 저장
    if output_json:
        with open(output_json, 'w', encoding='utf-8') as f:
            output_data = {
                "extraction_result": result.to_dict(),
                "mcp_sequence": mcp_sequence
            }
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"결과 저장됨: {output_json}")

    return result, mcp_sequence


# CLI 인터페이스
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("사용법: python positional_line_extractor.py <이미지경로> [출력JSON경로]")
        print("")
        print("예시:")
        print("  python positional_line_extractor.py photo.jpg")
        print("  python positional_line_extractor.py photo.jpg result.json")
        sys.exit(1)

    image_path = sys.argv[1]
    output_json = sys.argv[2] if len(sys.argv) > 2 else None

    result, mcp_sequence = extract_and_draw(image_path, output_json)

    print(f"\n=== 추출 결과 ===")
    print(f"이미지 크기: {result.image_width} x {result.image_height}")
    print(f"추출된 선: {result.total_lines}개")
    print(f"\n영역별 분포:")
    for region, count in sorted(result.lines_by_region.items()):
        print(f"  {region}: {count}개")
    print(f"\n방향별 분포:")
    for orientation, count in sorted(result.lines_by_orientation.items()):
        print(f"  {orientation}: {count}개")
    print(f"\nMCP 명령어: {len(mcp_sequence)}개 생성됨")

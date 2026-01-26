#!/usr/bin/env python3
"""
Line Extractor - Canny + HoughLinesP 기반 자동 선 추출 모듈

이 모듈은 이미지에서 구조선(기둥, 빔, 래프터 등)을 자동으로 추출합니다.

주요 기능:
1. Canny 엣지 감지
2. HoughLinesP 직선 추출
3. 평행선 그룹화
4. 구조 요소 분류 (수직=기둥, 수평=빔, 대각선=래프터)
5. 선 병합 및 필터링

사용 예:
    extractor = LineExtractor()
    lines = extractor.extract_lines(image)
    structural = extractor.classify_structural_elements(lines)

참조: OpenCV find_obj.py, plane_tracker.py
"""
from __future__ import annotations  # 타입 힌트 지연 평가 (np.ndarray 허용)

import json
import math
from typing import List, Tuple, Optional, Dict, Any, TYPE_CHECKING
from dataclasses import dataclass, field

# TYPE_CHECKING은 타입 체커만 True, 런타임에는 False
if TYPE_CHECKING:
    import numpy as np
from collections import defaultdict

try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False
    np = None  # 타입 힌트용 placeholder


@dataclass
class Line3D:
    """
    3D 선분 (HoughLinesP 출력용)

    STGEN DXF 에디터는 3D 좌표계를 사용합니다.

    __init__.py에서 ExtractedLine3D로 별칭 export됨
    """
    x1: float
    y1: float
    x2: float
    y2: float
    z1: float = 0.0
    z2: float = 0.0
    angle: float = field(default=0.0)  # XY 평면 각도 (도)
    length: float = field(default=0.0)  # XY 평면 길이

    def __post_init__(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        # XY 평면 길이 (2D 호환)
        self.length = math.sqrt(dx * dx + dy * dy)
        self.angle = math.degrees(math.atan2(dy, dx))
        # 각도를 0-180 범위로 정규화
        if self.angle < 0:
            self.angle += 180

    @property
    def length_3d(self) -> float:
        """3D 길이 계산"""
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        dz = self.z2 - self.z1
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'start': [self.x1, self.y1, self.z1],
            'end': [self.x2, self.y2, self.z2],
            'angle': round(self.angle, 2),
            'length': round(self.length, 2)
        }

    def midpoint(self) -> Tuple[float, float, float]:
        return (
            (self.x1 + self.x2) / 2,
            (self.y1 + self.y2) / 2,
            (self.z1 + self.z2) / 2
        )

    @property
    def start(self) -> Tuple[float, float, float]:
        """시작점 (3D)"""
        return (self.x1, self.y1, self.z1)

    @property
    def end(self) -> Tuple[float, float, float]:
        """끝점 (3D)"""
        return (self.x2, self.y2, self.z2)

    @property
    def start_xy(self) -> Tuple[float, float]:
        """시작점 XY 좌표"""
        return (self.x1, self.y1)

    @property
    def end_xy(self) -> Tuple[float, float]:
        """끝점 XY 좌표"""
        return (self.x2, self.y2)


@dataclass
class LineGroup:
    """평행선 그룹"""
    lines: List[Line3D]
    avg_angle: float
    category: str  # 'vertical', 'horizontal', 'diagonal'

    def to_dict(self) -> Dict[str, Any]:
        return {
            'count': len(self.lines),
            'avg_angle': round(self.avg_angle, 2),
            'category': self.category,
            'lines': [l.to_dict() for l in self.lines]
        }


@dataclass
class StructuralElements:
    """구조 요소 분류 결과"""
    columns: List[Line3D]  # 수직선 (기둥)
    beams: List[Line3D]    # 수평선 (빔)
    rafters: List[Line3D]  # 대각선 (래프터)
    other: List[Line3D]    # 기타

    def to_dict(self) -> Dict[str, Any]:
        return {
            'columns': {'count': len(self.columns), 'lines': [l.to_dict() for l in self.columns]},
            'beams': {'count': len(self.beams), 'lines': [l.to_dict() for l in self.beams]},
            'rafters': {'count': len(self.rafters), 'lines': [l.to_dict() for l in self.rafters]},
            'other': {'count': len(self.other), 'lines': [l.to_dict() for l in self.other]}
        }


class LineExtractor:
    """
    Canny + HoughLinesP 기반 자동 선 추출

    파이프라인:
    1. 전처리 (그레이스케일, 블러)
    2. Canny 엣지 감지
    3. HoughLinesP 직선 추출
    4. 선 필터링 (최소 길이, 중복 제거)
    5. 각도 기반 분류
    """

    def __init__(self,
                 canny_low: int = 50,
                 canny_high: int = 150,
                 hough_threshold: int = 50,
                 min_line_length: int = 30,
                 max_line_gap: int = 10):
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required for LineExtractor")

        # 기본 파라미터
        self.canny_low = canny_low
        self.canny_high = canny_high
        self.hough_rho = 1  # 거리 해상도 (픽셀)
        self.hough_theta = math.pi / 180  # 각도 해상도 (라디안) - np 대신 math 사용
        self.hough_threshold = hough_threshold  # 최소 투표 수
        self.min_line_length = min_line_length  # 최소 선 길이
        self.max_line_gap = max_line_gap  # 최대 선 간격
        self.blur_kernel = 5  # 가우시안 블러 커널

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """이미지 전처리"""
        # 그레이스케일 변환
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        # 가우시안 블러 (노이즈 제거)
        if self.blur_kernel > 0:
            gray = cv2.GaussianBlur(gray, (self.blur_kernel, self.blur_kernel), 0)

        return gray

    def detect_edges(self, gray: np.ndarray) -> np.ndarray:
        """Canny 엣지 감지"""
        edges = cv2.Canny(gray, self.canny_low, self.canny_high, apertureSize=3)
        return edges

    def extract_lines(self, image: np.ndarray,
                      min_length: Optional[int] = None,
                      max_gap: Optional[int] = None,
                      canny_low: Optional[int] = None,
                      canny_high: Optional[int] = None) -> List[Line3D]:
        """
        이미지에서 직선 추출

        Args:
            image: 입력 이미지
            min_length: 최소 선 길이 (None이면 기본값)
            max_gap: 최대 선 간격 (None이면 기본값)
            canny_low: Canny 저임계값
            canny_high: Canny 고임계값

        Returns:
            Line3D 객체 리스트
        """
        # 파라미터 설정
        min_len = min_length if min_length is not None else self.min_line_length
        max_g = max_gap if max_gap is not None else self.max_line_gap

        if canny_low is not None:
            self.canny_low = canny_low
        if canny_high is not None:
            self.canny_high = canny_high

        # 전처리
        gray = self.preprocess(image)

        # 엣지 감지
        edges = self.detect_edges(gray)

        # HoughLinesP
        raw_lines = cv2.HoughLinesP(
            edges,
            rho=self.hough_rho,
            theta=self.hough_theta,
            threshold=self.hough_threshold,
            minLineLength=min_len,
            maxLineGap=max_g
        )

        if raw_lines is None:
            return []

        # Line3D 객체로 변환
        lines = []
        for line in raw_lines:
            x1, y1, x2, y2 = line[0]
            lines.append(Line3D(float(x1), float(y1), float(x2), float(y2)))

        return lines

    def extract_lines_adaptive(self, image: np.ndarray,
                               target_line_count: int = 50) -> List[Line3D]:
        """
        적응적 파라미터로 선 추출

        이미지에 따라 Canny 임계값을 자동 조정합니다.

        Args:
            image: 입력 이미지
            target_line_count: 목표 선 개수 (대략적)

        Returns:
            Line3D 리스트
        """
        gray = self.preprocess(image)

        # Otsu 임계값으로 자동 추정
        otsu_thresh, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Canny 임계값 설정 (Otsu 기반)
        canny_low = int(max(0, otsu_thresh * 0.5))
        canny_high = int(min(255, otsu_thresh * 1.5))

        # 여러 threshold로 시도
        best_lines = []
        best_diff = float('inf')

        for threshold in [30, 50, 70, 100, 130]:
            self.hough_threshold = threshold
            lines = self.extract_lines(image, canny_low=canny_low, canny_high=canny_high)

            diff = abs(len(lines) - target_line_count)
            if diff < best_diff:
                best_diff = diff
                best_lines = lines

            if len(lines) >= target_line_count * 0.8:
                break

        return best_lines

    def filter_lines_by_length(self, lines: List[Line3D],
                                min_length: float,
                                max_length: Optional[float] = None) -> List[Line3D]:
        """길이로 선 필터링"""
        filtered = [l for l in lines if l.length >= min_length]
        if max_length is not None:
            filtered = [l for l in filtered if l.length <= max_length]
        return filtered

    def filter_lines_by_angle(self, lines: List[Line3D],
                              target_angle: float,
                              tolerance: float = 10) -> List[Line3D]:
        """
        각도로 선 필터링

        Args:
            lines: 입력 선 리스트
            target_angle: 목표 각도 (0-180)
            tolerance: 허용 오차 (도)
        """
        filtered = []
        for line in lines:
            # 각도 차이 계산 (순환 고려)
            diff = abs(line.angle - target_angle)
            if diff > 90:
                diff = 180 - diff
            if diff <= tolerance:
                filtered.append(line)
        return filtered

    def group_parallel_lines(self, lines: List[Line3D],
                             angle_tolerance: float = 5) -> List[LineGroup]:
        """
        평행선 그룹화

        Args:
            lines: 입력 선 리스트
            angle_tolerance: 각도 허용 오차 (도)

        Returns:
            LineGroup 리스트
        """
        if not lines:
            return []

        # 각도별 그룹화
        groups = defaultdict(list)

        for line in lines:
            # 각도를 tolerance 단위로 반올림
            bucket = round(line.angle / angle_tolerance) * angle_tolerance
            groups[bucket].append(line)

        # LineGroup 생성
        result = []
        for angle, group_lines in groups.items():
            if len(group_lines) >= 2:  # 최소 2개 이상
                avg_angle = sum(l.angle for l in group_lines) / len(group_lines)

                # 카테고리 결정
                if 80 <= avg_angle <= 100:
                    category = 'vertical'
                elif avg_angle <= 10 or avg_angle >= 170:
                    category = 'horizontal'
                else:
                    category = 'diagonal'

                result.append(LineGroup(
                    lines=group_lines,
                    avg_angle=avg_angle,
                    category=category
                ))

        return result

    def classify_structural_elements(self, lines: List[Line3D],
                                     vertical_tolerance: float = 15,
                                     horizontal_tolerance: float = 15) -> StructuralElements:
        """
        구조 요소 분류

        Args:
            lines: 입력 선 리스트
            vertical_tolerance: 수직 판정 허용 오차 (도)
            horizontal_tolerance: 수평 판정 허용 오차 (도)

        Returns:
            StructuralElements 객체
        """
        columns = []   # 수직 (기둥)
        beams = []     # 수평 (빔)
        rafters = []   # 대각선 (래프터)
        other = []

        for line in lines:
            angle = line.angle

            # 수직 판정 (90도 근처)
            if 90 - vertical_tolerance <= angle <= 90 + vertical_tolerance:
                columns.append(line)
            # 수평 판정 (0도 또는 180도 근처)
            elif angle <= horizontal_tolerance or angle >= 180 - horizontal_tolerance:
                beams.append(line)
            # 대각선 (나머지)
            elif 20 <= angle <= 70 or 110 <= angle <= 160:
                rafters.append(line)
            else:
                other.append(line)

        return StructuralElements(
            columns=columns,
            beams=beams,
            rafters=rafters,
            other=other
        )

    def merge_collinear_lines(self, lines: List[Line3D],
                              angle_tolerance: float = 5,
                              distance_tolerance: float = 20) -> List[Line3D]:
        """
        같은 직선 위의 선분들을 병합

        Args:
            lines: 입력 선 리스트
            angle_tolerance: 각도 허용 오차
            distance_tolerance: 거리 허용 오차 (픽셀)

        Returns:
            병합된 Line3D 리스트
        """
        if not lines:
            return []

        # 각도별 그룹화
        angle_groups = defaultdict(list)
        for line in lines:
            bucket = round(line.angle / angle_tolerance) * angle_tolerance
            angle_groups[bucket].append(line)

        merged = []

        for group_lines in angle_groups.values():
            # 그룹 내에서 공선 여부 확인 및 병합
            remaining = list(group_lines)

            while remaining:
                current = remaining.pop(0)
                merged_with_current = [current]

                i = 0
                while i < len(remaining):
                    candidate = remaining[i]

                    # 두 선이 같은 직선 위에 있는지 확인
                    if self._are_collinear(current, candidate, distance_tolerance):
                        merged_with_current.append(candidate)
                        remaining.pop(i)
                    else:
                        i += 1

                # 병합된 선들의 최소/최대 점 찾기
                if len(merged_with_current) > 1:
                    all_points = []
                    for l in merged_with_current:
                        all_points.append((l.x1, l.y1))
                        all_points.append((l.x2, l.y2))

                    # 주 방향에 따라 정렬
                    avg_angle = sum(l.angle for l in merged_with_current) / len(merged_with_current)

                    if 45 <= avg_angle <= 135:  # 수직에 가까움
                        all_points.sort(key=lambda p: p[1])  # Y로 정렬
                    else:  # 수평에 가까움
                        all_points.sort(key=lambda p: p[0])  # X로 정렬

                    merged.append(Line3D(
                        all_points[0][0], all_points[0][1],
                        all_points[-1][0], all_points[-1][1]
                    ))
                else:
                    merged.append(current)

        return merged

    def _are_collinear(self, line1: Line3D, line2: Line3D,
                       distance_threshold: float) -> bool:
        """두 선이 같은 직선 위에 있는지 확인"""
        # line1의 중점에서 line2까지의 거리 계산
        mid = line1.midpoint()

        # line2의 직선 방정식: ax + by + c = 0
        dx = line2.x2 - line2.x1
        dy = line2.y2 - line2.y1
        length = math.sqrt(dx * dx + dy * dy)

        if length < 1e-6:
            return False

        # 정규화된 법선 벡터
        a = -dy / length
        b = dx / length
        c = -(a * line2.x1 + b * line2.y1)

        # 점-직선 거리
        dist = abs(a * mid[0] + b * mid[1] + c)

        return dist < distance_threshold

    def remove_duplicate_lines(self, lines: List[Line3D],
                               distance_threshold: float = 10,
                               angle_threshold: float = 5) -> List[Line3D]:
        """
        중복 선 제거

        Args:
            lines: 입력 선 리스트
            distance_threshold: 거리 임계값 (픽셀)
            angle_threshold: 각도 임계값 (도)

        Returns:
            중복 제거된 Line3D 리스트
        """
        if not lines:
            return []

        unique = []

        for line in lines:
            is_duplicate = False

            for existing in unique:
                # 각도 차이
                angle_diff = abs(line.angle - existing.angle)
                if angle_diff > 90:
                    angle_diff = 180 - angle_diff

                if angle_diff > angle_threshold:
                    continue

                # 중점 거리
                mid1 = line.midpoint()
                mid2 = existing.midpoint()
                dist = math.sqrt((mid1[0] - mid2[0])**2 + (mid1[1] - mid2[1])**2)

                if dist < distance_threshold:
                    is_duplicate = True
                    break

            if not is_duplicate:
                unique.append(line)

        return unique

    def draw_lines(self, image: np.ndarray,
                   lines: List[Line3D],
                   color: Tuple[int, int, int] = (0, 255, 0),
                   thickness: int = 2) -> np.ndarray:
        """
        선을 이미지에 그리기

        Args:
            image: 입력 이미지
            lines: Line3D 리스트
            color: 선 색상 (BGR)
            thickness: 선 두께

        Returns:
            선이 그려진 이미지
        """
        vis = image.copy()

        for line in lines:
            pt1 = (int(line.x1), int(line.y1))
            pt2 = (int(line.x2), int(line.y2))
            cv2.line(vis, pt1, pt2, color, thickness)

        return vis

    def draw_structural_elements(self, image: np.ndarray,
                                 elements: StructuralElements,
                                 thickness: int = 2) -> np.ndarray:
        """
        구조 요소를 색상별로 이미지에 그리기

        Args:
            image: 입력 이미지
            elements: StructuralElements 객체
            thickness: 선 두께

        Returns:
            구조 요소가 그려진 이미지
        """
        vis = image.copy()

        # 기둥 (빨강)
        for line in elements.columns:
            pt1 = (int(line.x1), int(line.y1))
            pt2 = (int(line.x2), int(line.y2))
            cv2.line(vis, pt1, pt2, (0, 0, 255), thickness)

        # 빔 (파랑)
        for line in elements.beams:
            pt1 = (int(line.x1), int(line.y1))
            pt2 = (int(line.x2), int(line.y2))
            cv2.line(vis, pt1, pt2, (255, 0, 0), thickness)

        # 래프터 (초록)
        for line in elements.rafters:
            pt1 = (int(line.x1), int(line.y1))
            pt2 = (int(line.x2), int(line.y2))
            cv2.line(vis, pt1, pt2, (0, 255, 0), thickness)

        # 기타 (노랑)
        for line in elements.other:
            pt1 = (int(line.x1), int(line.y1))
            pt2 = (int(line.x2), int(line.y2))
            cv2.line(vis, pt1, pt2, (0, 255, 255), thickness)

        return vis


class ContourExtractor:
    """
    윤곽선 기반 선 추출기

    닫힌 영역의 외곽선을 추출합니다.
    """

    def __init__(self):
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required")

    def extract_contours(self, image: np.ndarray,
                         threshold: int = 127,
                         min_area: float = 100) -> List[np.ndarray]:
        """
        윤곽선 추출

        Args:
            image: 입력 이미지
            threshold: 이진화 임계값
            min_area: 최소 면적 (픽셀)

        Returns:
            윤곽선 리스트 (각 윤곽선은 점 배열)
        """
        # 그레이스케일 변환
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        # 이진화
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

        # 윤곽선 추출
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 면적 필터링
        filtered = [c for c in contours if cv2.contourArea(c) >= min_area]

        return filtered

    def contour_to_lines(self, contour: np.ndarray,
                        epsilon_ratio: float = 0.02) -> List[Line3D]:
        """
        윤곽선을 선분 리스트로 변환

        Args:
            contour: 윤곽선 (점 배열)
            epsilon_ratio: Douglas-Peucker 단순화 비율

        Returns:
            Line3D 리스트
        """
        # 윤곽선 단순화
        epsilon = epsilon_ratio * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        lines = []
        points = approx.reshape(-1, 2)

        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            lines.append(Line3D(float(p1[0]), float(p1[1]), float(p2[0]), float(p2[1])))

        return lines


# ============ CLI Interface ============

def main():
    """CLI 엔트리포인트"""
    import sys

    if len(sys.argv) < 2:
        print(json.dumps({
            'usage': 'python line_extractor.py <command> [args]',
            'commands': {
                'extract': 'extract <image_path> [min_length] - Extract lines from image',
                'classify': 'classify <image_path> - Classify structural elements',
                'edges': 'edges <image_path> <output_path> - Save edge detection result'
            }
        }, indent=2))
        return

    cmd = sys.argv[1]

    if cmd == 'extract' and len(sys.argv) >= 3:
        image_path = sys.argv[2]
        min_length = int(sys.argv[3]) if len(sys.argv) > 3 else 30

        image = cv2.imread(image_path)
        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        extractor = LineExtractor()
        lines = extractor.extract_lines(image, min_length=min_length)

        # 중복 제거
        lines = extractor.remove_duplicate_lines(lines)

        print(json.dumps({
            'success': True,
            'count': len(lines),
            'lines': [l.to_dict() for l in lines]
        }, indent=2))

    elif cmd == 'classify' and len(sys.argv) >= 3:
        image_path = sys.argv[2]

        image = cv2.imread(image_path)
        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        extractor = LineExtractor()
        lines = extractor.extract_lines(image)
        lines = extractor.remove_duplicate_lines(lines)
        elements = extractor.classify_structural_elements(lines)

        print(json.dumps({
            'success': True,
            'total_lines': len(lines),
            'elements': elements.to_dict()
        }, indent=2))

    elif cmd == 'edges' and len(sys.argv) >= 4:
        image_path = sys.argv[2]
        output_path = sys.argv[3]

        image = cv2.imread(image_path)
        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        extractor = LineExtractor()
        gray = extractor.preprocess(image)
        edges = extractor.detect_edges(gray)

        cv2.imwrite(output_path, edges)
        print(json.dumps({
            'success': True,
            'output': output_path
        }))

    else:
        print(json.dumps({'error': f'Unknown command: {cmd}'}))


if __name__ == '__main__':
    main()

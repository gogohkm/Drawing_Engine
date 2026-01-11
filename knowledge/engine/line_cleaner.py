"""
Line Cleaner - 벡터화된 선 후처리 모듈

벡터화 결과물의 이중선, 노이즈, 분절선을 정리하여 깔끔한 도면으로 변환합니다.

주요 기능:
1. 중심선 추출: 평행한 두 선 → 하나의 중심선
2. 선 병합: 같은 직선 위의 분절된 선들 합치기
3. 중복 제거: 거의 같은 선 제거
4. 노이즈 필터: 짧은 선 제거
5. 끝점 스냅: 끝점을 가까운 점/선에 맞추기

사용법:
    python line_cleaner.py clean <input.dxf> <output.dxf> [options_json]
    python line_cleaner.py info
"""

import json
import math
import os
import sys
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Set, Dict


@dataclass
class Point2D:
    """2D 점"""
    x: float
    y: float

    def distance_to(self, other: 'Point2D') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __hash__(self):
        return hash((round(self.x, 4), round(self.y, 4)))

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return abs(self.x - other.x) < 0.0001 and abs(self.y - other.y) < 0.0001


@dataclass
class Line2D:
    """2D 선분"""
    start: Point2D
    end: Point2D
    layer: str = "0"

    @property
    def length(self) -> float:
        return self.start.distance_to(self.end)

    @property
    def midpoint(self) -> Point2D:
        return Point2D(
            (self.start.x + self.end.x) / 2,
            (self.start.y + self.end.y) / 2
        )

    @property
    def angle(self) -> float:
        """선의 각도 (0 ~ 180도, 방향 무관)"""
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        angle = math.degrees(math.atan2(dy, dx))
        # 0 ~ 180 범위로 정규화
        if angle < 0:
            angle += 180
        if angle >= 180:
            angle -= 180
        return angle

    @property
    def direction(self) -> Tuple[float, float]:
        """정규화된 방향 벡터"""
        length = self.length
        if length < 0.0001:
            return (0, 0)
        return (
            (self.end.x - self.start.x) / length,
            (self.end.y - self.start.y) / length
        )

    def distance_to_point(self, point: Point2D) -> float:
        """점에서 선분까지의 최단 거리"""
        # 선분의 방향 벡터
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        length_sq = dx * dx + dy * dy

        if length_sq < 0.0001:
            return self.start.distance_to(point)

        # 점을 선분에 투영한 파라미터 t
        t = max(0, min(1, (
            (point.x - self.start.x) * dx +
            (point.y - self.start.y) * dy
        ) / length_sq))

        # 가장 가까운 점
        closest = Point2D(
            self.start.x + t * dx,
            self.start.y + t * dy
        )

        return point.distance_to(closest)

    def distance_to_line_infinite(self, point: Point2D) -> float:
        """점에서 무한 직선까지의 거리"""
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        length = math.sqrt(dx * dx + dy * dy)

        if length < 0.0001:
            return self.start.distance_to(point)

        # 직선의 방정식: ax + by + c = 0
        # (y2-y1)x - (x2-x1)y + (x2-x1)y1 - (y2-y1)x1 = 0
        a = dy
        b = -dx
        c = dx * self.start.y - dy * self.start.x

        return abs(a * point.x + b * point.y + c) / length

    def project_point(self, point: Point2D) -> float:
        """점을 선분에 투영한 파라미터 t (0: start, 1: end)"""
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        length_sq = dx * dx + dy * dy

        if length_sq < 0.0001:
            return 0.5

        return (
            (point.x - self.start.x) * dx +
            (point.y - self.start.y) * dy
        ) / length_sq

    def is_parallel_to(self, other: 'Line2D', angle_tolerance: float = 2.0) -> bool:
        """다른 선과 평행한지 확인"""
        angle_diff = abs(self.angle - other.angle)
        if angle_diff > 90:
            angle_diff = 180 - angle_diff
        return angle_diff < angle_tolerance

    def is_collinear_with(self, other: 'Line2D',
                          angle_tolerance: float = 2.0,
                          distance_tolerance: float = 1.0) -> bool:
        """다른 선과 같은 직선 위에 있는지 확인"""
        if not self.is_parallel_to(other, angle_tolerance):
            return False

        # 두 선분의 끝점들이 모두 직선 가까이에 있는지
        dist1 = self.distance_to_line_infinite(other.start)
        dist2 = self.distance_to_line_infinite(other.end)

        return dist1 < distance_tolerance and dist2 < distance_tolerance


@dataclass
class CleanerOptions:
    """정리 옵션"""
    # 중심선 추출
    extract_centerline: bool = True
    parallel_distance_max: float = 5.0  # 평행선으로 인식할 최대 거리
    parallel_angle_tolerance: float = 3.0  # 각도 허용 오차 (도)

    # 선 병합
    merge_collinear: bool = True
    collinear_gap_max: float = 3.0  # 병합할 최대 갭
    collinear_angle_tolerance: float = 2.0
    collinear_distance_tolerance: float = 1.0

    # 중복 제거
    remove_duplicates: bool = True
    duplicate_tolerance: float = 1.0  # 중복으로 인식할 거리

    # 노이즈 필터
    filter_short: bool = True
    min_length: float = 3.0  # 최소 선 길이

    # 끝점 스냅
    snap_endpoints: bool = True
    snap_tolerance: float = 2.0  # 스냅 거리

    # 각도 스냅 (등각 투영 도면용)
    snap_angles: bool = True
    snap_angle_list: List[float] = None  # 스냅할 각도 목록 (기본: 0, 30, 90, 150)
    snap_angle_tolerance: float = 5.0  # 각도 스냅 허용 오차

    # 출력
    output_layer: str = "CLEANED"

    def __post_init__(self):
        if self.snap_angle_list is None:
            # 등각 투영 도면의 주요 각도: 0°, 30°, 90°, 150° (및 반대 방향)
            self.snap_angle_list = [0, 30, 60, 90, 120, 150]

    @classmethod
    def from_json(cls, json_str: str) -> 'CleanerOptions':
        try:
            data = json.loads(json_str)
            return cls(**{k: v for k, v in data.items() if hasattr(cls, k)})
        except:
            return cls()


class LineCleaner:
    """선 정리 엔진"""

    def __init__(self, options: CleanerOptions = None):
        self.options = options or CleanerOptions()
        self.lines: List[Line2D] = []
        self.cleaned_lines: List[Line2D] = []
        self.stats = {
            "input_count": 0,
            "after_centerline": 0,
            "after_merge": 0,
            "after_duplicate": 0,
            "after_filter": 0,
            "after_snap": 0,
            "output_count": 0
        }

    def load_from_dxf(self, dxf_path: str) -> bool:
        """DXF 파일에서 LINE 엔티티 로드"""
        self.lines = []

        try:
            with open(dxf_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading DXF: {e}")
            return False

        # ENTITIES 섹션 찾기
        entities_start = content.find('ENTITIES')
        if entities_start == -1:
            print("No ENTITIES section found")
            return False

        entities_end = content.find('ENDSEC', entities_start)
        entities_section = content[entities_start:entities_end]

        # LINE 엔티티 파싱 - 여러 형식 지원
        # 형식 1: "  0\nLINE" (공백 2개)
        # 형식 2: " 0\nLINE" (공백 1개)
        # 형식 3: "0\nLINE" (공백 없음)
        import re
        lines_data = re.split(r'\n\s*0\nLINE', entities_section)

        for line_block in lines_data[1:]:  # 첫 번째는 ENTITIES 헤더
            try:
                line = self._parse_line_entity(line_block)
                if line:
                    self.lines.append(line)
            except:
                continue

        self.stats["input_count"] = len(self.lines)
        return True

    def _parse_line_entity(self, block: str) -> Optional[Line2D]:
        """LINE 엔티티 블록 파싱"""
        lines = [l.strip() for l in block.split('\n') if l.strip()]

        x1 = y1 = x2 = y2 = None
        layer = "0"

        i = 0
        while i < len(lines) - 1:
            code = lines[i]
            value = lines[i + 1]

            try:
                if code == '8':
                    layer = value
                elif code == '10':
                    x1 = float(value)
                elif code == '20':
                    y1 = float(value)
                elif code == '11':
                    x2 = float(value)
                elif code == '21':
                    y2 = float(value)
            except ValueError:
                pass

            i += 2

        if all(v is not None for v in [x1, y1, x2, y2]):
            return Line2D(Point2D(x1, y1), Point2D(x2, y2), layer)
        return None

    def clean(self) -> List[Line2D]:
        """전체 정리 프로세스 실행"""
        working_lines = list(self.lines)

        # 1. 중심선 추출
        if self.options.extract_centerline:
            working_lines = self._extract_centerlines(working_lines)
            self.stats["after_centerline"] = len(working_lines)

        # 2. 선 병합
        if self.options.merge_collinear:
            working_lines = self._merge_collinear_lines(working_lines)
            self.stats["after_merge"] = len(working_lines)

        # 3. 중복 제거
        if self.options.remove_duplicates:
            working_lines = self._remove_duplicates(working_lines)
            self.stats["after_duplicate"] = len(working_lines)

        # 4. 짧은 선 제거
        if self.options.filter_short:
            working_lines = self._filter_short_lines(working_lines)
            self.stats["after_filter"] = len(working_lines)

        # 5. 끝점 스냅
        if self.options.snap_endpoints:
            working_lines = self._snap_endpoints(working_lines)
            self.stats["after_snap"] = len(working_lines)

        # 6. 각도 스냅
        if self.options.snap_angles:
            working_lines = self._snap_angles(working_lines)
            self.stats["after_angle_snap"] = len(working_lines)

        # 7. 각도 스냅 후 다시 병합 (같은 각도가 된 선들)
        if self.options.snap_angles and self.options.merge_collinear:
            working_lines = self._merge_collinear_lines(working_lines)
            self.stats["after_final_merge"] = len(working_lines)

        # 레이어 설정
        for line in working_lines:
            line.layer = self.options.output_layer

        self.cleaned_lines = working_lines
        self.stats["output_count"] = len(working_lines)

        return self.cleaned_lines

    def _extract_centerlines(self, lines: List[Line2D]) -> List[Line2D]:
        """평행한 선 쌍에서 중심선 추출"""
        result = []
        used = set()

        for i, line1 in enumerate(lines):
            if i in used:
                continue

            # 이 선과 평행한 선들 찾기
            parallel_group = [line1]
            parallel_indices = [i]

            for j, line2 in enumerate(lines):
                if j <= i or j in used:
                    continue

                if not line1.is_parallel_to(line2, self.options.parallel_angle_tolerance):
                    continue

                # 두 선 사이의 거리 계산
                dist1 = line1.distance_to_line_infinite(line2.midpoint)
                dist2 = line2.distance_to_line_infinite(line1.midpoint)
                avg_dist = (dist1 + dist2) / 2

                if avg_dist < self.options.parallel_distance_max:
                    # 겹침 확인 (투영 범위가 겹치는지)
                    t1_start = line1.project_point(line2.start)
                    t1_end = line1.project_point(line2.end)

                    # 투영 범위가 0~1과 겹치는지
                    t_min = min(t1_start, t1_end)
                    t_max = max(t1_start, t1_end)

                    if t_max > -0.5 and t_min < 1.5:  # 약간의 여유
                        parallel_group.append(line2)
                        parallel_indices.append(j)

            if len(parallel_group) >= 2:
                # 중심선 계산
                centerline = self._calculate_centerline(parallel_group)
                if centerline:
                    result.append(centerline)
                    for idx in parallel_indices:
                        used.add(idx)
            else:
                result.append(line1)
                used.add(i)

        return result

    def _calculate_centerline(self, parallel_lines: List[Line2D]) -> Optional[Line2D]:
        """평행선 그룹의 중심선 계산"""
        if len(parallel_lines) < 2:
            return parallel_lines[0] if parallel_lines else None

        # 기준 선 (가장 긴 선)
        base_line = max(parallel_lines, key=lambda l: l.length)

        # 모든 끝점을 기준 선에 투영
        all_t_values = []
        all_midpoints = []

        for line in parallel_lines:
            t_start = base_line.project_point(line.start)
            t_end = base_line.project_point(line.end)
            all_t_values.extend([t_start, t_end])
            all_midpoints.append(line.midpoint)

        # 투영 범위
        t_min = min(all_t_values)
        t_max = max(all_t_values)

        # 중심점 계산 (모든 중점의 평균)
        avg_x = sum(p.x for p in all_midpoints) / len(all_midpoints)
        avg_y = sum(p.y for p in all_midpoints) / len(all_midpoints)
        center = Point2D(avg_x, avg_y)

        # 중심선의 시작점과 끝점
        dx = base_line.end.x - base_line.start.x
        dy = base_line.end.y - base_line.start.y
        length = base_line.length

        if length < 0.0001:
            return None

        # 방향 벡터
        dir_x = dx / length
        dir_y = dy / length

        # 기준선 시작점에서 중심까지의 오프셋
        center_t = base_line.project_point(center)

        # 새로운 시작점과 끝점
        new_start = Point2D(
            center.x + (t_min - center_t) * length * dir_x,
            center.y + (t_min - center_t) * length * dir_y
        )
        new_end = Point2D(
            center.x + (t_max - center_t) * length * dir_x,
            center.y + (t_max - center_t) * length * dir_y
        )

        return Line2D(new_start, new_end, base_line.layer)

    def _merge_collinear_lines(self, lines: List[Line2D]) -> List[Line2D]:
        """같은 직선 위의 선분들 병합"""
        result = []
        used = set()

        for i, line1 in enumerate(lines):
            if i in used:
                continue

            # 이 선과 같은 직선 위의 선들 찾기
            collinear_group = [line1]
            collinear_indices = [i]

            for j, line2 in enumerate(lines):
                if j <= i or j in used:
                    continue

                if line1.is_collinear_with(line2,
                                           self.options.collinear_angle_tolerance,
                                           self.options.collinear_distance_tolerance):
                    # 갭 확인
                    gap = self._calculate_gap(line1, line2)
                    if gap is None or gap < self.options.collinear_gap_max:
                        collinear_group.append(line2)
                        collinear_indices.append(j)

            if len(collinear_group) >= 2:
                # 반복적으로 병합
                merged = self._merge_line_group(collinear_group)
                result.extend(merged)
            else:
                result.append(line1)

            for idx in collinear_indices:
                used.add(idx)

        return result

    def _calculate_gap(self, line1: Line2D, line2: Line2D) -> Optional[float]:
        """두 선분 사이의 갭 계산 (겹치면 None 반환)"""
        # line1을 기준으로 line2의 끝점들 투영
        t1 = line1.project_point(line2.start)
        t2 = line1.project_point(line2.end)

        t_min = min(t1, t2)
        t_max = max(t1, t2)

        # 겹치는지 확인
        if t_min <= 1 and t_max >= 0:
            return None  # 겹침

        # 갭 계산
        if t_min > 1:
            gap_start = Point2D(
                line1.start.x + t_min * (line1.end.x - line1.start.x),
                line1.start.y + t_min * (line1.end.y - line1.start.y)
            )
            return line1.end.distance_to(gap_start)
        else:  # t_max < 0
            gap_end = Point2D(
                line1.start.x + t_max * (line1.end.x - line1.start.x),
                line1.start.y + t_max * (line1.end.y - line1.start.y)
            )
            return line1.start.distance_to(gap_end)

    def _merge_line_group(self, lines: List[Line2D]) -> List[Line2D]:
        """같은 직선 위의 선분들을 하나로 병합"""
        if not lines:
            return []

        if len(lines) == 1:
            return lines

        # 기준 선
        base = max(lines, key=lambda l: l.length)

        # 모든 끝점을 투영
        all_points = []
        for line in lines:
            t_start = base.project_point(line.start)
            t_end = base.project_point(line.end)
            all_points.append((t_start, line.start))
            all_points.append((t_end, line.end))

        # t값으로 정렬
        all_points.sort(key=lambda x: x[0])

        # 연속된 구간 찾기
        result = []
        current_start_t = all_points[0][0]
        current_end_t = all_points[0][0]

        for t, point in all_points[1:]:
            if t - current_end_t > self.options.collinear_gap_max / base.length:
                # 갭 발견 - 이전 구간 저장
                start_pt = Point2D(
                    base.start.x + current_start_t * (base.end.x - base.start.x),
                    base.start.y + current_start_t * (base.end.y - base.start.y)
                )
                end_pt = Point2D(
                    base.start.x + current_end_t * (base.end.x - base.start.x),
                    base.start.y + current_end_t * (base.end.y - base.start.y)
                )
                if start_pt.distance_to(end_pt) > 0.1:
                    result.append(Line2D(start_pt, end_pt, base.layer))

                current_start_t = t

            current_end_t = max(current_end_t, t)

        # 마지막 구간
        start_pt = Point2D(
            base.start.x + current_start_t * (base.end.x - base.start.x),
            base.start.y + current_start_t * (base.end.y - base.start.y)
        )
        end_pt = Point2D(
            base.start.x + current_end_t * (base.end.x - base.start.x),
            base.start.y + current_end_t * (base.end.y - base.start.y)
        )
        if start_pt.distance_to(end_pt) > 0.1:
            result.append(Line2D(start_pt, end_pt, base.layer))

        return result

    def _remove_duplicates(self, lines: List[Line2D]) -> List[Line2D]:
        """중복 선 제거"""
        result = []

        for line in lines:
            is_duplicate = False

            for existing in result:
                # 두 선의 끝점이 모두 가까운지 확인
                dist1 = min(
                    line.start.distance_to(existing.start) + line.end.distance_to(existing.end),
                    line.start.distance_to(existing.end) + line.end.distance_to(existing.start)
                )

                if dist1 < self.options.duplicate_tolerance * 2:
                    is_duplicate = True
                    break

            if not is_duplicate:
                result.append(line)

        return result

    def _filter_short_lines(self, lines: List[Line2D]) -> List[Line2D]:
        """짧은 선 제거"""
        return [line for line in lines if line.length >= self.options.min_length]

    def _snap_endpoints(self, lines: List[Line2D]) -> List[Line2D]:
        """끝점을 가까운 점에 스냅"""
        if not lines:
            return lines

        # 모든 끝점 수집
        all_points = []
        for line in lines:
            all_points.append(line.start)
            all_points.append(line.end)

        # 각 점에 대해 가까운 점들의 평균 위치 계산
        point_clusters: Dict[int, List[Point2D]] = {}
        cluster_id = 0
        point_to_cluster: Dict[int, int] = {}

        for i, pt in enumerate(all_points):
            if i in point_to_cluster:
                continue

            # 이 점과 가까운 점들 찾기
            cluster = [pt]
            indices = [i]

            for j, other in enumerate(all_points):
                if j <= i or j in point_to_cluster:
                    continue

                if pt.distance_to(other) < self.options.snap_tolerance:
                    cluster.append(other)
                    indices.append(j)

            if len(cluster) > 1:
                point_clusters[cluster_id] = cluster
                for idx in indices:
                    point_to_cluster[idx] = cluster_id
                cluster_id += 1

        # 클러스터별 평균 위치 계산
        cluster_centers: Dict[int, Point2D] = {}
        for cid, cluster in point_clusters.items():
            avg_x = sum(p.x for p in cluster) / len(cluster)
            avg_y = sum(p.y for p in cluster) / len(cluster)
            cluster_centers[cid] = Point2D(avg_x, avg_y)

        # 선의 끝점 업데이트
        result = []
        for i, line in enumerate(lines):
            start_idx = i * 2
            end_idx = i * 2 + 1

            new_start = line.start
            new_end = line.end

            if start_idx in point_to_cluster:
                new_start = cluster_centers[point_to_cluster[start_idx]]
            if end_idx in point_to_cluster:
                new_end = cluster_centers[point_to_cluster[end_idx]]

            result.append(Line2D(new_start, new_end, line.layer))

        return result

    def _snap_angles(self, lines: List[Line2D]) -> List[Line2D]:
        """선의 각도를 주요 각도에 스냅"""
        if not lines or not self.options.snap_angle_list:
            return lines

        result = []
        snap_angles = self.options.snap_angle_list
        tolerance = self.options.snap_angle_tolerance

        for line in lines:
            current_angle = line.angle
            best_snap_angle = None
            min_diff = float('inf')

            # 가장 가까운 스냅 각도 찾기
            for snap_angle in snap_angles:
                diff = abs(current_angle - snap_angle)
                if diff > 90:
                    diff = 180 - diff

                if diff < min_diff and diff < tolerance:
                    min_diff = diff
                    best_snap_angle = snap_angle

            if best_snap_angle is not None:
                # 각도 스냅 적용
                new_line = self._rotate_line_to_angle(line, best_snap_angle)
                result.append(new_line)
            else:
                result.append(line)

        return result

    def _rotate_line_to_angle(self, line: Line2D, target_angle: float) -> Line2D:
        """선을 지정된 각도로 회전 (중점 기준)"""
        midpoint = line.midpoint
        half_length = line.length / 2

        # 타겟 각도로 새 끝점 계산
        rad = math.radians(target_angle)
        dx = half_length * math.cos(rad)
        dy = half_length * math.sin(rad)

        new_start = Point2D(midpoint.x - dx, midpoint.y - dy)
        new_end = Point2D(midpoint.x + dx, midpoint.y + dy)

        return Line2D(new_start, new_end, line.layer)

    def save_to_dxf(self, dxf_path: str, template_path: str = None) -> bool:
        """정리된 선을 DXF로 저장"""
        # 템플릿 파일이 있으면 사용, 없으면 최소 DXF 생성
        if template_path and os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # 기존 ENTITIES 내용 제거 후 새 내용 삽입
            entities_start = content.find('ENTITIES')
            endsec_pos = content.find('ENDSEC', entities_start)

            if entities_start != -1 and endsec_pos != -1:
                # ENTITIES 섹션 시작부터 ENDSEC 전까지 찾기
                section_start = content.find('\n', entities_start) + 1

                # 새 LINE 엔티티 생성
                new_entities = self._generate_line_entities()

                # 새 내용으로 교체
                new_content = content[:section_start] + new_entities + content[endsec_pos:]

                with open(dxf_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                return True

        # 최소 DXF 생성
        dxf_content = self._generate_minimal_dxf()

        with open(dxf_path, 'w', encoding='utf-8') as f:
            f.write(dxf_content)

        return True

    def _generate_line_entities(self) -> str:
        """LINE 엔티티 문자열 생성"""
        entities = []

        for line in self.cleaned_lines:
            entity = f"""  0
LINE
  8
{line.layer}
 10
{round(line.start.x, 4)}
 20
{round(line.start.y, 4)}
 30
0.0
 11
{round(line.end.x, 4)}
 21
{round(line.end.y, 4)}
 31
0.0
"""
            entities.append(entity)

        return ''.join(entities)

    def _generate_minimal_dxf(self) -> str:
        """최소 DXF 파일 생성"""
        header = """  0
SECTION
  2
HEADER
  9
$ACADVER
  1
AC1014
  0
ENDSEC
  0
SECTION
  2
TABLES
  0
ENDSEC
  0
SECTION
  2
ENTITIES
"""

        entities = self._generate_line_entities()

        footer = """  0
ENDSEC
  0
EOF
"""

        return header + entities + footer

    def get_stats(self) -> dict:
        """정리 통계 반환"""
        return {
            **self.stats,
            "reduction_ratio": round(
                (1 - self.stats["output_count"] / max(1, self.stats["input_count"])) * 100, 1
            )
        }


# ========== CLI 함수 ==========

def cli_info() -> str:
    """정보 출력"""
    return json.dumps({
        "module": "line_cleaner",
        "version": "1.0",
        "description": "벡터화된 선 후처리 - 이중선 제거, 병합, 정리",
        "features": [
            "중심선 추출: 평행한 두 선 → 단일 중심선",
            "선 병합: 같은 직선 위의 분절된 선 합치기",
            "중복 제거: 거의 같은 선 제거",
            "노이즈 필터: 짧은 선 제거",
            "끝점 스냅: 끝점을 가까운 점에 맞추기"
        ],
        "options": {
            "extract_centerline": "평행선 → 중심선 (기본: true)",
            "parallel_distance_max": "평행선 인식 최대 거리 (기본: 5.0)",
            "merge_collinear": "같은 직선 위 선 병합 (기본: true)",
            "collinear_gap_max": "병합할 최대 갭 (기본: 3.0)",
            "remove_duplicates": "중복 선 제거 (기본: true)",
            "filter_short": "짧은 선 제거 (기본: true)",
            "min_length": "최소 선 길이 (기본: 3.0)",
            "snap_endpoints": "끝점 스냅 (기본: true)",
            "snap_tolerance": "스냅 허용 거리 (기본: 2.0)",
            "output_layer": "출력 레이어 (기본: CLEANED)"
        },
        "usage": {
            "cli": "python line_cleaner.py clean <input.dxf> <output.dxf> [options_json]",
            "example": 'python line_cleaner.py clean in.dxf out.dxf \'{"min_length": 5.0}\''
        }
    }, ensure_ascii=False, indent=2)


def cli_clean(input_path: str, output_path: str, options_json: str = "{}") -> str:
    """DXF 파일 정리"""
    options = CleanerOptions.from_json(options_json)
    cleaner = LineCleaner(options)

    if not cleaner.load_from_dxf(input_path):
        return json.dumps({"error": f"Failed to load DXF: {input_path}"})

    cleaner.clean()

    if not cleaner.save_to_dxf(output_path, input_path):
        return json.dumps({"error": f"Failed to save DXF: {output_path}"})

    return json.dumps({
        "success": True,
        "input": input_path,
        "output": output_path,
        "stats": cleaner.get_stats()
    }, ensure_ascii=False, indent=2)


def cli_analyze(input_path: str) -> str:
    """DXF 파일 분석 (정리 없이)"""
    cleaner = LineCleaner()

    if not cleaner.load_from_dxf(input_path):
        return json.dumps({"error": f"Failed to load DXF: {input_path}"})

    # 통계 수집
    lines = cleaner.lines

    # 각도 분포
    angle_buckets = {}
    for line in lines:
        bucket = round(line.angle / 5) * 5  # 5도 단위
        angle_buckets[bucket] = angle_buckets.get(bucket, 0) + 1

    # 길이 분포
    lengths = [line.length for line in lines]

    return json.dumps({
        "file": input_path,
        "total_lines": len(lines),
        "length_stats": {
            "min": round(min(lengths), 2) if lengths else 0,
            "max": round(max(lengths), 2) if lengths else 0,
            "avg": round(sum(lengths) / len(lengths), 2) if lengths else 0
        },
        "angle_distribution": dict(sorted(angle_buckets.items())),
        "recommendation": {
            "parallel_distance_max": 5.0,
            "min_length": round(sum(lengths) / len(lengths) * 0.1, 1) if lengths else 3.0
        }
    }, ensure_ascii=False, indent=2)


# ========== Main ==========

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python line_cleaner.py info")
        print("  python line_cleaner.py clean <input.dxf> <output.dxf> [options_json]")
        print("  python line_cleaner.py analyze <input.dxf>")
        print("")
        print("Options JSON example:")
        print('  \'{"min_length": 5.0, "parallel_distance_max": 3.0}\'')
        sys.exit(1)

    command = sys.argv[1]

    if command == "info":
        print(cli_info())
    elif command == "clean" and len(sys.argv) >= 4:
        options = sys.argv[4] if len(sys.argv) > 4 else "{}"
        print(cli_clean(sys.argv[2], sys.argv[3], options))
    elif command == "analyze" and len(sys.argv) >= 3:
        print(cli_analyze(sys.argv[2]))
    else:
        print(json.dumps({"error": f"Unknown command: {command}"}))

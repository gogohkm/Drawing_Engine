#!/usr/bin/env python3
"""
3D Transform Module - 픽셀 좌표를 3D 월드 좌표로 변환

이 모듈은 사진의 픽셀 좌표를 실제 3D 공간 좌표(mm)로 변환합니다.

지원 변환 방식:
1. PnP (Perspective-n-Point): 카메라 자세 기반 광선-평면 교차
2. Homography: 단일 평면 변환 (Z=0 고정)
3. Depth Estimation: 이미지 Y좌표 기반 깊이 추정 (간이)

사용 예:
    transformer = Transform3D()
    transformer.setup_pnp(R, t, K)
    point_3d = transformer.pixel_to_world(u, v, plane='floor')
"""

import math
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass

# OpenCV는 선택적 의존성
try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


@dataclass
class Point3D:
    """3D 점"""
    x: float
    y: float
    z: float

    def to_list(self) -> List[float]:
        return [self.x, self.y, self.z]

    def distance_to(self, other: 'Point3D') -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )


@dataclass
class Plane:
    """3D 평면: n · x + d = 0"""
    normal: Tuple[float, float, float]  # (nx, ny, nz)
    d: float  # offset
    name: str = "plane"

    @classmethod
    def floor(cls, z: float = 0.0) -> 'Plane':
        """바닥면 (Z = z)"""
        return cls(normal=(0, 0, 1), d=-z, name="floor")

    @classmethod
    def wall_back(cls, y: float) -> 'Plane':
        """뒷벽 (Y = y)"""
        return cls(normal=(0, 1, 0), d=-y, name="wall_back")

    @classmethod
    def wall_left(cls, x: float) -> 'Plane':
        """왼쪽벽 (X = x)"""
        return cls(normal=(1, 0, 0), d=-x, name="wall_left")

    @classmethod
    def wall_right(cls, x: float) -> 'Plane':
        """오른쪽벽 (X = x)"""
        return cls(normal=(1, 0, 0), d=-x, name="wall_right")


class Transform3D:
    """
    3D 변환 엔진

    픽셀 좌표를 3D 월드 좌표로 변환합니다.
    """

    def __init__(self):
        # PnP 파라미터
        self.R: Optional[np.ndarray] = None  # 회전 행렬 3x3
        self.t: Optional[np.ndarray] = None  # 이동 벡터 3x1
        self.K: Optional[np.ndarray] = None  # 카메라 행렬 3x3
        self.K_inv: Optional[np.ndarray] = None
        self.R_inv: Optional[np.ndarray] = None

        # Homography 파라미터
        self.H: Optional[np.ndarray] = None  # 3x3 homography
        self.H_inv: Optional[np.ndarray] = None

        # 이미지 크기
        self.image_width: int = 0
        self.image_height: int = 0

        # 평면 정의
        self.planes: Dict[str, Plane] = {
            'floor': Plane.floor(0),
        }

        # 깊이 추정 파라미터 (PnP 없을 때 사용)
        self.depth_estimation_enabled: bool = False
        self.horizon_y: float = 0.5  # 소실점 Y (이미지 비율)
        self.camera_height: float = 1600.0  # 카메라 높이 (mm)
        self.floor_depth_at_bottom: float = 2000.0  # 이미지 하단의 바닥 깊이

    # ============ Setup Methods ============

    def setup_pnp(self, R: List[List[float]], t: List[float], K: List[List[float]]):
        """
        PnP 자세 설정

        Args:
            R: 3x3 회전 행렬
            t: 3x1 이동 벡터
            K: 3x3 카메라 내부 행렬
        """
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required for PnP transformation")

        self.R = np.array(R, dtype=np.float64)
        self.t = np.array(t, dtype=np.float64).reshape(3, 1)
        self.K = np.array(K, dtype=np.float64)
        self.K_inv = np.linalg.inv(self.K)
        self.R_inv = np.linalg.inv(self.R)

    def setup_homography(self, H: List[List[float]], plane_z: float = 0.0):
        """
        Homography 행렬 설정 (평면 변환용)

        Args:
            H: 3x3 homography 행렬 (이미지 → 평면)
            plane_z: 변환된 좌표의 Z값 (기본 0)
        """
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required for homography transformation")

        self.H = np.array(H, dtype=np.float64)
        self.H_inv = np.linalg.inv(self.H)
        self.planes['homography'] = Plane.floor(plane_z)

    def setup_depth_estimation(self,
                                image_width: int,
                                image_height: int,
                                horizon_ratio: float = 0.4,
                                camera_height_mm: float = 1600.0,
                                near_depth_mm: float = 1000.0,
                                far_depth_mm: float = 20000.0):
        """
        깊이 추정 설정 (PnP 없이 간이 3D 변환)

        이미지의 Y 좌표를 기반으로 깊이(Z)를 추정합니다.
        - 이미지 하단 = 카메라 가까이 (near_depth)
        - 소실점(horizon) = 멀리 (far_depth)

        Args:
            image_width: 이미지 너비 (픽셀)
            image_height: 이미지 높이 (픽셀)
            horizon_ratio: 소실점 Y 위치 (0=상단, 1=하단)
            camera_height_mm: 카메라 높이 (mm)
            near_depth_mm: 이미지 하단의 깊이 (mm)
            far_depth_mm: 소실점의 깊이 (mm)
        """
        self.image_width = image_width
        self.image_height = image_height
        self.depth_estimation_enabled = True
        self.horizon_y = horizon_ratio
        self.camera_height = camera_height_mm
        self.floor_depth_at_bottom = near_depth_mm
        self.far_depth = far_depth_mm

    def add_plane(self, name: str, plane: Plane):
        """평면 추가"""
        self.planes[name] = plane

    # ============ Core Transformation Methods ============

    def pixel_to_world(self, u: float, v: float, plane: str = 'floor') -> Optional[Point3D]:
        """
        픽셀 좌표를 3D 월드 좌표로 변환

        우선순위:
        1. PnP 자세가 설정되어 있으면 광선-평면 교차 사용
        2. Homography가 설정되어 있으면 평면 변환 사용
        3. 깊이 추정이 활성화되어 있으면 Y 기반 깊이 추정

        Args:
            u: 픽셀 X 좌표
            v: 픽셀 Y 좌표
            plane: 교차할 평면 이름

        Returns:
            Point3D 또는 None
        """
        # 1. PnP 기반 변환
        if self.R is not None and self.K is not None:
            return self._transform_pnp(u, v, plane)

        # 2. Homography 기반 변환
        if self.H is not None:
            return self._transform_homography(u, v)

        # 3. 깊이 추정 기반 변환
        if self.depth_estimation_enabled:
            return self._transform_depth_estimation(u, v)

        # 변환 불가
        return None

    def _transform_pnp(self, u: float, v: float, plane_name: str) -> Optional[Point3D]:
        """PnP 자세 기반 광선-평면 교차로 3D 좌표 계산"""
        if plane_name not in self.planes:
            plane_name = 'floor'

        plane = self.planes[plane_name]

        # 1. 픽셀 → 카메라 좌표계 광선
        p_img = np.array([u, v, 1.0]).reshape(3, 1)
        p_cam_dir = self.K_inv @ p_img  # 정규화된 카메라 좌표

        # 2. 카메라 좌표계 → 월드 좌표계
        # 광선 원점: 카메라 위치 = -R^(-1) * t
        ray_origin = -self.R_inv @ self.t
        # 광선 방향: R^(-1) * 카메라 방향
        ray_direction = self.R_inv @ p_cam_dir
        ray_direction = ray_direction / np.linalg.norm(ray_direction)

        # 3. 광선-평면 교차
        n = np.array(plane.normal).reshape(3)
        d = plane.d

        ray_o = ray_origin.flatten()
        ray_d = ray_direction.flatten()

        dot = np.dot(n, ray_d)
        if abs(dot) < 1e-9:
            return None  # 평면과 평행

        t_param = -(np.dot(n, ray_o) + d) / dot
        if t_param < 0:
            return None  # 카메라 뒤쪽 교차

        intersection = ray_o + t_param * ray_d
        return Point3D(
            x=float(intersection[0]),
            y=float(intersection[1]),
            z=float(intersection[2])
        )

    def _transform_homography(self, u: float, v: float) -> Optional[Point3D]:
        """Homography 기반 평면 변환 (Z=0)"""
        p = np.array([u, v, 1.0])
        p_plane = self.H @ p

        if abs(p_plane[2]) < 1e-9:
            return None

        x = p_plane[0] / p_plane[2]
        y = p_plane[1] / p_plane[2]
        z = self.planes.get('homography', Plane.floor(0)).d * -1  # plane_z

        return Point3D(x=float(x), y=float(y), z=float(z))

    def _transform_depth_estimation(self, u: float, v: float) -> Optional[Point3D]:
        """
        깊이 추정 기반 원근 왜곡 제거 (Perspective Rectification)

        사진의 원근 효과를 제거하여 정면에서 본 것처럼 변환합니다.

        원리:
        - 소실점으로 수렴하는 선들을 평행하게 펴줌
        - 가까운 곳(이미지 하단)은 좁게 보이므로 확대
        - 먼 곳(이미지 상단)은 넓게 보이므로 축소

        결과 좌표계:
        - X: 좌(-) ↔ 우(+)
        - Y: 이미지 하단(0, 가까움) → 이미지 상단(멀리)
        - Z: 바닥(0) ↔ 천장(+)
        """
        if self.image_width == 0 or self.image_height == 0:
            return None

        # 소실점 위치 (이미지 좌표)
        vanishing_x = self.image_width / 2  # 이미지 중앙
        vanishing_y = self.horizon_y * self.image_height  # 소실점 Y

        # 이미지 좌표를 소실점 기준으로 정규화
        # u_rel: -0.5 ~ 0.5 (소실점 기준 상대 X)
        u_rel = (u - vanishing_x) / self.image_width

        # v_rel: 소실점에서의 거리 (양수 = 아래, 음수 = 위)
        v_rel = v - vanishing_y

        # === 바닥 영역 (소실점 아래, v > vanishing_y) ===
        if v > vanishing_y:
            # 소실점에서 이미지 하단까지의 거리
            max_v_dist = self.image_height - vanishing_y

            # t: 0(소실점) ~ 1(이미지 하단)
            t = v_rel / max_v_dist
            t = max(0.001, min(1.0, t))

            # Y 좌표 (깊이): 이미지 하단 = near, 소실점 = far
            # 비선형 매핑으로 원근감 보정
            y_world = self.floor_depth_at_bottom + (self.far_depth - self.floor_depth_at_bottom) * (1 - t)

            # X 좌표: 원근 보정
            # 핵심: 가까울수록(t 클수록) X 범위가 좁아 보이므로 확대해야 함
            # 소실점에서 멀어질수록 실제 X 범위는 넓어짐
            # perspective_scale = 1/t 형태로 보정
            perspective_scale = 1.0 / max(t, 0.1)  # t가 작을수록(멀리) 축소

            # 기준 폭 (이미지 하단에서의 실제 폭)
            base_width = self.far_depth * 0.8  # FOV 기반 추정
            x_world = u_rel * base_width * t  # t가 클수록(가까울수록) X 범위 좁음 → 원본 유지

            # Z 좌표: 바닥
            z_world = 0.0

        # === 벽면/천장 영역 (소실점 위, v <= vanishing_y) ===
        else:
            # 소실점에서 이미지 상단까지의 거리
            max_v_dist_up = vanishing_y

            # t_up: 0(소실점) ~ 1(이미지 상단)
            t_up = abs(v_rel) / max_v_dist_up if max_v_dist_up > 0 else 0
            t_up = max(0.0, min(1.0, t_up))

            # Y 좌표: 벽면이므로 far_depth 고정
            y_world = self.far_depth

            # X 좌표: 벽면에서의 위치
            base_width = self.far_depth * 0.8
            x_world = u_rel * base_width * 0.3  # 멀리 있으므로 좁게

            # Z 좌표 (높이): 소실점 = 카메라 높이, 이미지 상단 = 천장
            z_world = self.camera_height + t_up * self.camera_height * 1.5

        return Point3D(x=float(x_world), y=float(y_world), z=float(z_world))

    # ============ Utility Methods ============

    def world_to_pixel(self, point: Point3D) -> Optional[Tuple[float, float]]:
        """3D 월드 좌표를 픽셀로 역투영"""
        if self.R is None or self.K is None:
            return None

        # 월드 → 카메라 좌표
        p_world = np.array([point.x, point.y, point.z]).reshape(3, 1)
        p_cam = self.R @ p_world + self.t

        if p_cam[2, 0] <= 0:
            return None  # 카메라 뒤

        # 카메라 → 픽셀
        p_img = self.K @ p_cam
        u = p_img[0, 0] / p_img[2, 0]
        v = p_img[1, 0] / p_img[2, 0]

        return (float(u), float(v))

    def distance_3d(self, p1: Point3D, p2: Point3D) -> float:
        """두 3D 점 사이 거리 (mm)"""
        return p1.distance_to(p2)

    def measure_distance_pixels(self, u1: float, v1: float, u2: float, v2: float,
                                 plane: str = 'floor') -> Optional[Dict[str, Any]]:
        """
        두 픽셀 좌표 사이의 실제 3D 거리 측정

        Returns:
            {
                'distance_mm': float,
                'point1_3d': [x, y, z],
                'point2_3d': [x, y, z],
                'plane': str
            }
        """
        p1 = self.pixel_to_world(u1, v1, plane)
        p2 = self.pixel_to_world(u2, v2, plane)

        if p1 is None or p2 is None:
            return None

        return {
            'distance_mm': self.distance_3d(p1, p2),
            'point1_3d': p1.to_list(),
            'point2_3d': p2.to_list(),
            'plane': plane
        }


class PnPCalibrator:
    """
    PnP 캘리브레이션 유틸리티

    2D-3D 점 대응을 수집하고 카메라 자세를 계산합니다.
    """

    def __init__(self, image_width: int, image_height: int):
        self.image_width = image_width
        self.image_height = image_height
        self.points_2d: List[Tuple[float, float]] = []
        self.points_3d: List[Tuple[float, float, float]] = []

    def add_correspondence(self, pixel: Tuple[float, float], world: Tuple[float, float, float]):
        """2D-3D 대응점 추가"""
        self.points_2d.append(pixel)
        self.points_3d.append(world)

    def clear(self):
        """대응점 초기화"""
        self.points_2d.clear()
        self.points_3d.clear()

    def calibrate(self, focal_length: Optional[float] = None) -> Optional[Dict[str, Any]]:
        """
        PnP 캘리브레이션 실행

        Args:
            focal_length: 초점 거리 (픽셀). None이면 이미지 크기 기반 추정

        Returns:
            {
                'R': 회전 행렬,
                't': 이동 벡터,
                'K': 카메라 행렬,
                'rvec': 회전 벡터,
                'success': bool
            }
        """
        if not HAS_CV2:
            return {'success': False, 'error': 'OpenCV required'}

        if len(self.points_2d) < 4:
            return {'success': False, 'error': f'Need at least 4 points, got {len(self.points_2d)}'}

        # 카메라 행렬 추정
        if focal_length is None:
            focal_length = float(max(self.image_width, self.image_height))

        cx = self.image_width / 2
        cy = self.image_height / 2
        K = np.array([
            [focal_length, 0, cx],
            [0, focal_length, cy],
            [0, 0, 1]
        ], dtype=np.float64)

        # numpy 배열 변환
        obj_pts = np.array(self.points_3d, dtype=np.float64)
        img_pts = np.array(self.points_2d, dtype=np.float64)

        # PnP 풀이
        if len(self.points_2d) >= 6:
            # RANSAC 사용 (더 강건)
            success, rvec, tvec, inliers = cv2.solvePnPRansac(
                obj_pts, img_pts, K, None,
                flags=cv2.SOLVEPNP_ITERATIVE
            )
        else:
            # 일반 PnP
            success, rvec, tvec = cv2.solvePnP(
                obj_pts, img_pts, K, None,
                flags=cv2.SOLVEPNP_ITERATIVE
            )

        if not success:
            return {'success': False, 'error': 'PnP solve failed'}

        R, _ = cv2.Rodrigues(rvec)

        return {
            'success': True,
            'R': R.tolist(),
            't': tvec.flatten().tolist(),
            'K': K.tolist(),
            'rvec': rvec.flatten().tolist()
        }


# ============ CLI Interface ============

def main():
    """CLI 엔트리포인트"""
    import sys
    import json

    if len(sys.argv) < 2:
        print(json.dumps({
            'error': 'Usage: python transform_3d.py <command> [args]',
            'commands': [
                'pixel_to_world <u> <v> <R_json> <t_json> <K_json> [plane]',
                'measure <u1> <v1> <u2> <v2> <R_json> <t_json> <K_json>',
                'calibrate <points2d_json> <points3d_json> <width> <height>',
                'depth_estimate <u> <v> <width> <height> [horizon_ratio]'
            ]
        }))
        return

    cmd = sys.argv[1]

    if cmd == 'pixel_to_world' and len(sys.argv) >= 7:
        u, v = float(sys.argv[2]), float(sys.argv[3])
        R = json.loads(sys.argv[4])
        t = json.loads(sys.argv[5])
        K = json.loads(sys.argv[6])
        plane = sys.argv[7] if len(sys.argv) > 7 else 'floor'

        transformer = Transform3D()
        transformer.setup_pnp(R, t, K)
        result = transformer.pixel_to_world(u, v, plane)

        if result:
            print(json.dumps({'success': True, 'point_3d': result.to_list()}))
        else:
            print(json.dumps({'success': False, 'error': 'Transform failed'}))

    elif cmd == 'measure' and len(sys.argv) >= 9:
        u1, v1 = float(sys.argv[2]), float(sys.argv[3])
        u2, v2 = float(sys.argv[4]), float(sys.argv[5])
        R = json.loads(sys.argv[6])
        t = json.loads(sys.argv[7])
        K = json.loads(sys.argv[8])

        transformer = Transform3D()
        transformer.setup_pnp(R, t, K)
        result = transformer.measure_distance_pixels(u1, v1, u2, v2)

        if result:
            print(json.dumps({'success': True, **result}))
        else:
            print(json.dumps({'success': False, 'error': 'Measure failed'}))

    elif cmd == 'calibrate' and len(sys.argv) >= 6:
        points2d = json.loads(sys.argv[2])
        points3d = json.loads(sys.argv[3])
        width = int(sys.argv[4])
        height = int(sys.argv[5])

        calibrator = PnPCalibrator(width, height)
        for p2d, p3d in zip(points2d, points3d):
            calibrator.add_correspondence(tuple(p2d), tuple(p3d))

        result = calibrator.calibrate()
        print(json.dumps(result))

    elif cmd == 'depth_estimate' and len(sys.argv) >= 6:
        u, v = float(sys.argv[2]), float(sys.argv[3])
        width, height = int(sys.argv[4]), int(sys.argv[5])
        horizon = float(sys.argv[6]) if len(sys.argv) > 6 else 0.4

        transformer = Transform3D()
        transformer.setup_depth_estimation(width, height, horizon)
        result = transformer.pixel_to_world(u, v)

        if result:
            print(json.dumps({'success': True, 'point_3d': result.to_list()}))
        else:
            print(json.dumps({'success': False, 'error': 'Estimate failed'}))

    else:
        print(json.dumps({'error': f'Unknown command: {cmd}'}))


if __name__ == '__main__':
    main()

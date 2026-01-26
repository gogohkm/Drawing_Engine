#!/usr/bin/env python3
"""
ArUco Marker Detector - 자동 캘리브레이션을 위한 마커 감지 모듈

이 모듈은 ArUco 마커를 자동으로 감지하여 수동 4점 선택을 대체합니다.

주요 기능:
1. ArUco 마커 감지 (단일/다중)
2. ChArUco 보드 감지 (더 높은 정확도)
3. 마커 기반 Homography 계산
4. 마커 기반 PnP 자세 추정

사용 예:
    detector = MarkerDetector()
    corners, ids = detector.detect_markers(image)
    H = detector.get_homography_from_markers(corners, marker_size_mm=100)
    pose = detector.calibrate_from_markers(image, marker_size_mm=100)

참조: OpenCV aruco_detect_board_charuco.py
"""
from __future__ import annotations  # 타입 힌트 지연 평가

import json
import math
from typing import List, Tuple, Optional, Dict, Any, TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    import numpy as np

try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


@dataclass
class MarkerInfo:
    """감지된 마커 정보"""
    id: int
    corners: np.ndarray  # 4x2 array of corner points
    center: Tuple[float, float]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'corners': self.corners.tolist(),
            'center': list(self.center)
        }


@dataclass
class CalibrationResult:
    """캘리브레이션 결과"""
    success: bool
    R: Optional[np.ndarray] = None  # 3x3 회전 행렬
    t: Optional[np.ndarray] = None  # 3x1 이동 벡터
    rvec: Optional[np.ndarray] = None  # 회전 벡터
    K: Optional[np.ndarray] = None  # 카메라 행렬
    H: Optional[np.ndarray] = None  # Homography 행렬
    marker_ids: Optional[List[int]] = None  # 감지된 마커 ID 목록
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result = {'success': self.success}
        if self.R is not None:
            result['R'] = self.R.tolist()
        if self.t is not None:
            result['t'] = self.t.flatten().tolist()
        if self.rvec is not None:
            result['rvec'] = self.rvec.flatten().tolist()
        if self.K is not None:
            result['K'] = self.K.tolist()
        if self.H is not None:
            result['H'] = self.H.tolist()
        if self.marker_ids is not None:
            result['marker_ids'] = self.marker_ids
        if self.error:
            result['error'] = self.error
        return result


class MarkerDetector:
    """
    ArUco 마커 기반 자동 캘리브레이션

    지원 기능:
    - 단일 ArUco 마커 감지 및 자세 추정
    - 다중 마커 감지
    - ChArUco 보드 감지 (고정밀)
    - 마커 기반 Homography 계산

    ArUco 사전 목록:
    - DICT_4X4_50, DICT_4X4_100, DICT_4X4_250, DICT_4X4_1000
    - DICT_5X5_50, DICT_5X5_100, DICT_5X5_250, DICT_5X5_1000
    - DICT_6X6_50, DICT_6X6_100, DICT_6X6_250, DICT_6X6_1000
    - DICT_7X7_50, DICT_7X7_100, DICT_7X7_250, DICT_7X7_1000
    """

    # ArUco 사전 매핑
    DICT_NAMES = {
        'DICT_4X4_50': cv2.aruco.DICT_4X4_50 if HAS_CV2 else 0,
        'DICT_4X4_100': cv2.aruco.DICT_4X4_100 if HAS_CV2 else 1,
        'DICT_4X4_250': cv2.aruco.DICT_4X4_250 if HAS_CV2 else 2,
        'DICT_4X4_1000': cv2.aruco.DICT_4X4_1000 if HAS_CV2 else 3,
        'DICT_5X5_50': cv2.aruco.DICT_5X5_50 if HAS_CV2 else 4,
        'DICT_5X5_100': cv2.aruco.DICT_5X5_100 if HAS_CV2 else 5,
        'DICT_5X5_250': cv2.aruco.DICT_5X5_250 if HAS_CV2 else 6,
        'DICT_5X5_1000': cv2.aruco.DICT_5X5_1000 if HAS_CV2 else 7,
        'DICT_6X6_50': cv2.aruco.DICT_6X6_50 if HAS_CV2 else 8,
        'DICT_6X6_100': cv2.aruco.DICT_6X6_100 if HAS_CV2 else 9,
        'DICT_6X6_250': cv2.aruco.DICT_6X6_250 if HAS_CV2 else 10,
        'DICT_6X6_1000': cv2.aruco.DICT_6X6_1000 if HAS_CV2 else 11,
        'DICT_7X7_50': cv2.aruco.DICT_7X7_50 if HAS_CV2 else 12,
        'DICT_7X7_100': cv2.aruco.DICT_7X7_100 if HAS_CV2 else 13,
        'DICT_7X7_250': cv2.aruco.DICT_7X7_250 if HAS_CV2 else 14,
        'DICT_7X7_1000': cv2.aruco.DICT_7X7_1000 if HAS_CV2 else 15,
    }

    def __init__(self, dict_type: str = 'DICT_6X6_250'):
        """
        마커 감지기 초기화

        Args:
            dict_type: ArUco 사전 타입 (기본: DICT_6X6_250)
        """
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required for marker detection")

        if dict_type not in self.DICT_NAMES:
            raise ValueError(f"Unknown dictionary type: {dict_type}. "
                           f"Available: {list(self.DICT_NAMES.keys())}")

        self.dict_type = dict_type
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(self.DICT_NAMES[dict_type])
        self.detector = cv2.aruco.ArucoDetector(self.aruco_dict)

        # 감지 파라미터 (필요시 조정 가능)
        self.detector_params = self.detector.getDetectorParameters()

    def detect_markers(self, image: np.ndarray) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        """
        이미지에서 ArUco 마커 감지

        Args:
            image: 입력 이미지 (BGR 또는 Grayscale)

        Returns:
            (corners, ids) 튜플
            - corners: 마커 코너 좌표 리스트 (각 마커는 4x2 배열)
            - ids: 마커 ID 배열
            마커가 없으면 (None, None) 반환
        """
        # 그레이스케일 변환 (필요시)
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        corners, ids, rejected = self.detector.detectMarkers(gray)

        if ids is None or len(ids) == 0:
            return None, None

        return corners, ids

    def detect_markers_info(self, image: np.ndarray) -> List[MarkerInfo]:
        """
        이미지에서 마커 감지 및 상세 정보 반환

        Args:
            image: 입력 이미지

        Returns:
            MarkerInfo 객체 리스트
        """
        corners, ids = self.detect_markers(image)

        if corners is None:
            return []

        markers = []
        for i, (corner, marker_id) in enumerate(zip(corners, ids.flatten())):
            corner_pts = corner.reshape(4, 2)
            center = corner_pts.mean(axis=0)
            markers.append(MarkerInfo(
                id=int(marker_id),
                corners=corner_pts,
                center=(float(center[0]), float(center[1]))
            ))

        return markers

    def get_homography_from_marker(self, corners: np.ndarray,
                                   marker_size_mm: float,
                                   origin_offset: Tuple[float, float] = (0, 0)) -> Optional[np.ndarray]:
        """
        단일 마커 코너에서 Homography 계산

        마커의 4개 코너를 실제 좌표로 매핑합니다.

        Args:
            corners: 마커 코너 좌표 (4x2)
            marker_size_mm: 마커 실제 크기 (mm)
            origin_offset: 원점 오프셋 (mm)

        Returns:
            3x3 Homography 행렬 (이미지 → 평면)
        """
        src = corners.reshape(4, 2).astype(np.float32)

        ox, oy = origin_offset
        dst = np.array([
            [ox, oy],
            [ox + marker_size_mm, oy],
            [ox + marker_size_mm, oy + marker_size_mm],
            [ox, oy + marker_size_mm]
        ], dtype=np.float32)

        H, status = cv2.findHomography(src, dst)

        return H

    def get_homography_from_markers(self, corners: List[np.ndarray],
                                    ids: np.ndarray,
                                    marker_size_mm: float,
                                    marker_positions: Optional[Dict[int, Tuple[float, float]]] = None) -> Optional[np.ndarray]:
        """
        다중 마커에서 Homography 계산

        여러 마커의 코너를 사용하여 더 정확한 Homography를 계산합니다.

        Args:
            corners: 마커 코너 리스트
            ids: 마커 ID 배열
            marker_size_mm: 마커 크기 (mm)
            marker_positions: 마커 ID별 실제 위치 딕셔너리 {id: (x, y)}
                             None이면 첫 번째 마커만 사용

        Returns:
            3x3 Homography 행렬
        """
        if marker_positions is None:
            # 첫 번째 마커만 사용
            return self.get_homography_from_marker(corners[0], marker_size_mm)

        # 다중 마커 사용
        src_points = []
        dst_points = []

        for corner, marker_id in zip(corners, ids.flatten()):
            if marker_id in marker_positions:
                pos = marker_positions[marker_id]
                corner_pts = corner.reshape(4, 2)

                # 4개 코너 각각 매핑
                for i, (dx, dy) in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]):
                    src_points.append(corner_pts[i])
                    dst_points.append([
                        pos[0] + dx * marker_size_mm,
                        pos[1] + dy * marker_size_mm
                    ])

        if len(src_points) < 4:
            return None

        src = np.array(src_points, dtype=np.float32)
        dst = np.array(dst_points, dtype=np.float32)

        H, status = cv2.findHomography(src, dst, cv2.RANSAC, 3.0)

        return H

    def calibrate_from_marker(self, image: np.ndarray,
                              marker_size_mm: float,
                              camera_matrix: Optional[np.ndarray] = None,
                              dist_coeffs: Optional[np.ndarray] = None) -> CalibrationResult:
        """
        단일 마커에서 카메라 자세 추정 (PnP)

        Args:
            image: 입력 이미지
            marker_size_mm: 마커 실제 크기 (mm)
            camera_matrix: 카메라 내부 파라미터 (None이면 추정)
            dist_coeffs: 왜곡 계수 (None이면 0)

        Returns:
            CalibrationResult 객체
        """
        corners, ids = self.detect_markers(image)

        if corners is None or len(corners) == 0:
            return CalibrationResult(success=False, error="No markers detected")

        # 카메라 행렬 추정
        h, w = image.shape[:2]
        if camera_matrix is None:
            focal = max(w, h)
            camera_matrix = np.array([
                [focal, 0, w / 2],
                [0, focal, h / 2],
                [0, 0, 1]
            ], dtype=np.float64)

        if dist_coeffs is None:
            dist_coeffs = np.zeros(5)

        # 3D 좌표 설정 (마커 평면, Z=0)
        half_size = marker_size_mm / 2
        obj_points = np.array([
            [-half_size, -half_size, 0],
            [half_size, -half_size, 0],
            [half_size, half_size, 0],
            [-half_size, half_size, 0]
        ], dtype=np.float64)

        # 첫 번째 마커 사용
        img_points = corners[0].reshape(4, 2).astype(np.float64)

        # PnP 풀이
        success, rvec, tvec = cv2.solvePnP(
            obj_points, img_points, camera_matrix, dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:
            return CalibrationResult(success=False, error="PnP solve failed")

        R, _ = cv2.Rodrigues(rvec)

        # Homography도 계산
        H = self.get_homography_from_marker(corners[0], marker_size_mm)

        return CalibrationResult(
            success=True,
            R=R,
            t=tvec,
            rvec=rvec,
            K=camera_matrix,
            H=H,
            marker_ids=ids.flatten().tolist() if ids is not None else None
        )

    def calibrate_from_markers_multi(self, image: np.ndarray,
                                     marker_size_mm: float,
                                     marker_3d_positions: Dict[int, Tuple[float, float, float]],
                                     camera_matrix: Optional[np.ndarray] = None,
                                     dist_coeffs: Optional[np.ndarray] = None) -> CalibrationResult:
        """
        다중 마커에서 카메라 자세 추정 (더 정확)

        Args:
            image: 입력 이미지
            marker_size_mm: 마커 크기 (mm)
            marker_3d_positions: 마커 ID별 3D 중심 좌표 {id: (x, y, z)}
            camera_matrix: 카메라 내부 파라미터
            dist_coeffs: 왜곡 계수

        Returns:
            CalibrationResult 객체
        """
        corners, ids = self.detect_markers(image)

        if corners is None:
            return CalibrationResult(success=False, error="No markers detected")

        # 카메라 행렬 추정
        h, w = image.shape[:2]
        if camera_matrix is None:
            focal = max(w, h)
            camera_matrix = np.array([
                [focal, 0, w / 2],
                [0, focal, h / 2],
                [0, 0, 1]
            ], dtype=np.float64)

        if dist_coeffs is None:
            dist_coeffs = np.zeros(5)

        # 매칭되는 마커만 수집
        obj_points = []
        img_points = []
        half_size = marker_size_mm / 2

        for corner, marker_id in zip(corners, ids.flatten()):
            if marker_id in marker_3d_positions:
                cx, cy, cz = marker_3d_positions[marker_id]
                corner_pts = corner.reshape(4, 2)

                # 마커 4개 코너의 3D 좌표
                for i, (dx, dy) in enumerate([(-1, -1), (1, -1), (1, 1), (-1, 1)]):
                    obj_points.append([
                        cx + dx * half_size,
                        cy + dy * half_size,
                        cz
                    ])
                    img_points.append(corner_pts[i])

        if len(obj_points) < 4:
            return CalibrationResult(success=False,
                                   error=f"Not enough matching markers (need 4 points, got {len(obj_points)})")

        obj_pts = np.array(obj_points, dtype=np.float64)
        img_pts = np.array(img_points, dtype=np.float64)

        # RANSAC으로 PnP 풀이 (아웃라이어 처리)
        if len(obj_points) >= 6:
            success, rvec, tvec, inliers = cv2.solvePnPRansac(
                obj_pts, img_pts, camera_matrix, dist_coeffs,
                flags=cv2.SOLVEPNP_ITERATIVE
            )
        else:
            success, rvec, tvec = cv2.solvePnP(
                obj_pts, img_pts, camera_matrix, dist_coeffs,
                flags=cv2.SOLVEPNP_ITERATIVE
            )

        if not success:
            return CalibrationResult(success=False, error="PnP solve failed")

        R, _ = cv2.Rodrigues(rvec)

        return CalibrationResult(
            success=True,
            R=R,
            t=tvec,
            rvec=rvec,
            K=camera_matrix
        )

    def draw_detected_markers(self, image: np.ndarray,
                              corners: List[np.ndarray],
                              ids: np.ndarray,
                              draw_ids: bool = True) -> np.ndarray:
        """
        감지된 마커를 이미지에 그리기

        Args:
            image: 입력 이미지 (복사됨)
            corners: 마커 코너 리스트
            ids: 마커 ID 배열
            draw_ids: ID 텍스트 표시 여부

        Returns:
            마커가 그려진 이미지
        """
        vis = image.copy()
        cv2.aruco.drawDetectedMarkers(vis, corners, ids if draw_ids else None)
        return vis

    def draw_axes(self, image: np.ndarray,
                  camera_matrix: np.ndarray,
                  dist_coeffs: np.ndarray,
                  rvec: np.ndarray,
                  tvec: np.ndarray,
                  axis_length: float = 50) -> np.ndarray:
        """
        좌표축을 이미지에 그리기

        Args:
            image: 입력 이미지
            camera_matrix: 카메라 행렬
            dist_coeffs: 왜곡 계수
            rvec: 회전 벡터
            tvec: 이동 벡터
            axis_length: 축 길이 (mm)

        Returns:
            축이 그려진 이미지
        """
        vis = image.copy()
        cv2.drawFrameAxes(vis, camera_matrix, dist_coeffs, rvec, tvec, axis_length)
        return vis


class CharucoDetector:
    """
    ChArUco 보드 감지기 - 더 높은 정확도의 캘리브레이션

    ChArUco 보드는 체스보드 + ArUco 마커의 조합으로,
    부분적으로 가려져도 감지가 가능하고 정확도가 높습니다.
    """

    def __init__(self, board_size: Tuple[int, int] = (5, 7),
                 square_length: float = 40.0,
                 marker_length: float = 20.0,
                 dict_type: str = 'DICT_6X6_250'):
        """
        ChArUco 보드 감지기 초기화

        Args:
            board_size: 보드 크기 (가로 사각형 수, 세로 사각형 수)
            square_length: 체스보드 사각형 크기 (mm)
            marker_length: ArUco 마커 크기 (mm)
            dict_type: ArUco 사전 타입
        """
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required")

        self.board_size = board_size
        self.square_length = square_length
        self.marker_length = marker_length

        # ArUco 사전
        dict_id = MarkerDetector.DICT_NAMES.get(dict_type, cv2.aruco.DICT_6X6_250)
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(dict_id)

        # ChArUco 보드 생성
        self.board = cv2.aruco.CharucoBoard(
            board_size, square_length, marker_length, self.aruco_dict
        )
        self.detector = cv2.aruco.CharucoDetector(self.board)

    def detect_board(self, image: np.ndarray) -> Tuple[Optional[np.ndarray],
                                                        Optional[np.ndarray],
                                                        Optional[np.ndarray],
                                                        Optional[np.ndarray]]:
        """
        ChArUco 보드 감지

        Args:
            image: 입력 이미지

        Returns:
            (charuco_corners, charuco_ids, marker_corners, marker_ids) 튜플
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        charuco_corners, charuco_ids, marker_corners, marker_ids = \
            self.detector.detectBoard(gray)

        return charuco_corners, charuco_ids, marker_corners, marker_ids

    def calibrate_camera(self, images: List[np.ndarray],
                         image_size: Tuple[int, int]) -> Dict[str, Any]:
        """
        여러 이미지로 카메라 캘리브레이션

        Args:
            images: 이미지 리스트
            image_size: 이미지 크기 (width, height)

        Returns:
            캘리브레이션 결과 딕셔너리
        """
        all_charuco_corners = []
        all_charuco_ids = []

        for img in images:
            charuco_corners, charuco_ids, _, _ = self.detect_board(img)
            if charuco_corners is not None and len(charuco_corners) > 3:
                all_charuco_corners.append(charuco_corners)
                all_charuco_ids.append(charuco_ids)

        if len(all_charuco_corners) == 0:
            return {'success': False, 'error': 'No valid boards detected'}

        # 캘리브레이션
        ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(
            all_charuco_corners, all_charuco_ids, self.board, image_size, None, None
        )

        return {
            'success': True,
            'rms': ret,
            'camera_matrix': camera_matrix.tolist(),
            'dist_coeffs': dist_coeffs.flatten().tolist(),
            'rvecs': [r.flatten().tolist() for r in rvecs],
            'tvecs': [t.flatten().tolist() for t in tvecs]
        }

    def estimate_pose(self, image: np.ndarray,
                      camera_matrix: np.ndarray,
                      dist_coeffs: np.ndarray) -> CalibrationResult:
        """
        ChArUco 보드에서 카메라 자세 추정

        Args:
            image: 입력 이미지
            camera_matrix: 카메라 내부 파라미터
            dist_coeffs: 왜곡 계수

        Returns:
            CalibrationResult 객체
        """
        charuco_corners, charuco_ids, _, _ = self.detect_board(image)

        if charuco_corners is None or len(charuco_corners) < 4:
            return CalibrationResult(success=False,
                                   error="Not enough corners detected")

        try:
            obj_points, img_points = self.board.matchImagePoints(
                charuco_corners, charuco_ids
            )

            success, rvec, tvec = cv2.solvePnP(
                obj_points, img_points, camera_matrix, dist_coeffs
            )

            if not success:
                return CalibrationResult(success=False, error="PnP failed")

            R, _ = cv2.Rodrigues(rvec)

            return CalibrationResult(
                success=True,
                R=R,
                t=tvec,
                rvec=rvec,
                K=camera_matrix
            )

        except cv2.error as e:
            return CalibrationResult(success=False, error=str(e))


# ============ CLI Interface ============

def main():
    """CLI 엔트리포인트"""
    import sys

    if len(sys.argv) < 2:
        print(json.dumps({
            'usage': 'python marker_detector.py <command> [args]',
            'commands': {
                'detect': 'detect <image_path> - Detect markers in image',
                'calibrate': 'calibrate <image_path> <marker_size_mm> - Calibrate from marker',
                'homography': 'homography <image_path> <marker_size_mm> - Get homography matrix'
            }
        }, indent=2))
        return

    cmd = sys.argv[1]

    if cmd == 'detect' and len(sys.argv) >= 3:
        image_path = sys.argv[2]
        image = cv2.imread(image_path)

        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        detector = MarkerDetector()
        markers = detector.detect_markers_info(image)

        print(json.dumps({
            'success': True,
            'count': len(markers),
            'markers': [m.to_dict() for m in markers]
        }, indent=2))

    elif cmd == 'calibrate' and len(sys.argv) >= 4:
        image_path = sys.argv[2]
        marker_size = float(sys.argv[3])

        image = cv2.imread(image_path)
        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        detector = MarkerDetector()
        result = detector.calibrate_from_marker(image, marker_size)

        print(json.dumps(result.to_dict(), indent=2))

    elif cmd == 'homography' and len(sys.argv) >= 4:
        image_path = sys.argv[2]
        marker_size = float(sys.argv[3])

        image = cv2.imread(image_path)
        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        detector = MarkerDetector()
        corners, ids = detector.detect_markers(image)

        if corners is None:
            print(json.dumps({'error': 'No markers detected'}))
            return

        H = detector.get_homography_from_marker(corners[0], marker_size)

        print(json.dumps({
            'success': True,
            'H': H.tolist() if H is not None else None,
            'marker_id': int(ids[0][0])
        }, indent=2))

    else:
        print(json.dumps({'error': f'Unknown command: {cmd}'}))


if __name__ == '__main__':
    main()

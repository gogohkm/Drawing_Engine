#!/usr/bin/env python3
"""
Plane Tracker - ORB + FLANN 기반 평면 추적 모듈

이 모듈은 참조 이미지의 평면을 실시간으로 추적하여
Homography와 카메라 자세를 자동으로 추정합니다.

주요 기능:
1. ORB/SIFT 특징점 추출
2. FLANN 기반 특징점 매칭
3. Lowe's ratio test로 좋은 매칭 필터링
4. RANSAC 기반 Homography 계산
5. 추적된 평면에서 PnP 자세 추정

사용 예:
    tracker = PlaneTracker()
    tracker.add_target(reference_image, rect, world_coords)
    results = tracker.track(frame)
    for result in results:
        H = result.H  # Homography
        pose = result.pose  # PnP 결과

참조: OpenCV plane_tracker.py, feature_homography.py
"""
from __future__ import annotations  # 타입 힌트 지연 평가

import json
import math
from typing import List, Tuple, Optional, Dict, Any, NamedTuple, TYPE_CHECKING
from dataclasses import dataclass, field

if TYPE_CHECKING:
    import numpy as np

try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


# FLANN 매칭 파라미터
FLANN_INDEX_KDTREE = 1
FLANN_INDEX_LSH = 6

FLANN_PARAMS_ORB = dict(
    algorithm=FLANN_INDEX_LSH,
    table_number=6,
    key_size=12,
    multi_probe_level=1
)

FLANN_PARAMS_SIFT = dict(
    algorithm=FLANN_INDEX_KDTREE,
    trees=5
)

MIN_MATCH_COUNT = 10  # 최소 매칭 수


@dataclass
class PlanarTarget:
    """추적 대상 평면"""
    image: np.ndarray
    rect: Tuple[int, int, int, int]  # (x0, y0, x1, y1)
    keypoints: List
    descriptors: np.ndarray
    world_coords: Optional[Tuple[float, float, float, float]] = None  # (x0, y0, width, height) in mm
    data: Any = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'rect': list(self.rect),
            'keypoints_count': len(self.keypoints),
            'world_coords': list(self.world_coords) if self.world_coords else None
        }


@dataclass
class TrackedResult:
    """추적 결과"""
    target: PlanarTarget
    p0: np.ndarray  # 참조 이미지의 매칭 점
    p1: np.ndarray  # 현재 프레임의 매칭 점
    H: np.ndarray   # Homography 행렬
    quad: np.ndarray  # 변환된 사각형 코너
    match_count: int
    pose: Optional[Dict[str, Any]] = None  # PnP 결과

    def to_dict(self) -> Dict[str, Any]:
        result = {
            'match_count': self.match_count,
            'H': self.H.tolist() if self.H is not None else None,
            'quad': self.quad.tolist() if self.quad is not None else None,
        }
        if self.pose:
            result['pose'] = self.pose
        return result


class PlaneTracker:
    """
    ORB + FLANN 기반 평면 추적기

    특징:
    - 다중 타겟 추적 지원
    - Lowe's ratio test로 강건한 매칭
    - RANSAC으로 아웃라이어 제거
    - 실시간 추적 최적화

    사용 방법:
    1. add_target()으로 추적 대상 등록
    2. track()으로 프레임에서 추적
    3. 결과에서 H (Homography), pose (PnP) 사용
    """

    def __init__(self, detector_type: str = 'ORB', nfeatures: int = 1000):
        """
        초기화

        Args:
            detector_type: 특징점 검출기 타입 ('ORB', 'SIFT', 'AKAZE')
            nfeatures: 최대 특징점 수
        """
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required")

        self.detector_type = detector_type.upper()
        self.nfeatures = nfeatures

        # 특징점 검출기 생성
        if self.detector_type == 'ORB':
            self.detector = cv2.ORB_create(nfeatures=nfeatures)
            self.matcher = cv2.FlannBasedMatcher(FLANN_PARAMS_ORB, {})
            self.norm_type = cv2.NORM_HAMMING
        elif self.detector_type == 'SIFT':
            self.detector = cv2.SIFT_create(nfeatures=nfeatures)
            self.matcher = cv2.FlannBasedMatcher(FLANN_PARAMS_SIFT, dict(checks=50))
            self.norm_type = cv2.NORM_L2
        elif self.detector_type == 'AKAZE':
            self.detector = cv2.AKAZE_create()
            self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
            self.norm_type = cv2.NORM_HAMMING
        else:
            raise ValueError(f"Unknown detector type: {detector_type}")

        self.targets: List[PlanarTarget] = []
        self.frame_keypoints: List = []
        self.frame_descriptors: Optional[np.ndarray] = None

        # 매칭 파라미터
        self.ratio_threshold = 0.75  # Lowe's ratio test
        self.ransac_threshold = 5.0   # RANSAC 임계값

    def add_target(self, image: np.ndarray,
                   rect: Tuple[int, int, int, int],
                   world_coords: Optional[Tuple[float, float, float, float]] = None,
                   data: Any = None) -> int:
        """
        추적 대상 추가

        Args:
            image: 참조 이미지
            rect: 추적 영역 (x0, y0, x1, y1)
            world_coords: 실제 좌표 (x0, y0, width, height) in mm
            data: 사용자 데이터

        Returns:
            타겟 인덱스
        """
        x0, y0, x1, y1 = rect

        # 특징점 추출
        raw_kps, raw_descs = self._detect_features(image)

        # rect 내부 특징점만 필터링
        keypoints = []
        descriptors = []

        for kp, desc in zip(raw_kps, raw_descs if raw_descs is not None else []):
            x, y = kp.pt
            if x0 <= x <= x1 and y0 <= y <= y1:
                keypoints.append(kp)
                descriptors.append(desc)

        if len(keypoints) == 0:
            raise ValueError("No keypoints found in the specified rectangle")

        descriptors = np.array(descriptors, dtype=np.uint8 if self.norm_type == cv2.NORM_HAMMING else np.float32)

        # 매처에 추가
        self.matcher.add([descriptors])

        # 타겟 생성
        target = PlanarTarget(
            image=image.copy(),
            rect=rect,
            keypoints=keypoints,
            descriptors=descriptors,
            world_coords=world_coords,
            data=data
        )
        self.targets.append(target)

        return len(self.targets) - 1

    def clear(self):
        """모든 타겟 제거"""
        self.targets = []
        self.matcher.clear()

    def track(self, frame: np.ndarray,
              camera_matrix: Optional[np.ndarray] = None,
              dist_coeffs: Optional[np.ndarray] = None) -> List[TrackedResult]:
        """
        프레임에서 타겟 추적

        Args:
            frame: 현재 프레임
            camera_matrix: 카메라 내부 파라미터 (PnP용)
            dist_coeffs: 왜곡 계수 (PnP용)

        Returns:
            TrackedResult 리스트 (매칭 수 내림차순 정렬)
        """
        if len(self.targets) == 0:
            return []

        # 프레임에서 특징점 추출
        self.frame_keypoints, self.frame_descriptors = self._detect_features(frame)

        if self.frame_descriptors is None or len(self.frame_keypoints) < MIN_MATCH_COUNT:
            return []

        # KNN 매칭
        matches = self.matcher.knnMatch(self.frame_descriptors, k=2)

        # Lowe's ratio test
        good_matches = []
        for m in matches:
            if len(m) == 2 and m[0].distance < m[1].distance * self.ratio_threshold:
                good_matches.append(m[0])

        if len(good_matches) < MIN_MATCH_COUNT:
            return []

        # 타겟별 매칭 그룹화
        matches_by_target = [[] for _ in self.targets]
        for m in good_matches:
            matches_by_target[m.imgIdx].append(m)

        # 각 타겟 추적
        results = []

        for target_idx, target_matches in enumerate(matches_by_target):
            if len(target_matches) < MIN_MATCH_COUNT:
                continue

            target = self.targets[target_idx]

            # 매칭 점 추출
            p0 = np.float32([target.keypoints[m.trainIdx].pt for m in target_matches])
            p1 = np.float32([self.frame_keypoints[m.queryIdx].pt for m in target_matches])

            # Homography 계산 (RANSAC)
            H, status = cv2.findHomography(p0, p1, cv2.RANSAC, self.ransac_threshold)

            if H is None:
                continue

            status = status.ravel() != 0
            if status.sum() < MIN_MATCH_COUNT:
                continue

            # 인라이어만 사용
            p0_inliers = p0[status]
            p1_inliers = p1[status]

            # 사각형 변환
            x0, y0, x1, y1 = target.rect
            quad = np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1]])
            quad_transformed = cv2.perspectiveTransform(quad.reshape(1, -1, 2), H).reshape(-1, 2)

            # PnP 자세 추정 (world_coords가 있고 카메라 파라미터가 있으면)
            pose = None
            if target.world_coords is not None and camera_matrix is not None:
                pose = self._estimate_pose(
                    quad_transformed, target.world_coords,
                    camera_matrix, dist_coeffs
                )

            results.append(TrackedResult(
                target=target,
                p0=p0_inliers,
                p1=p1_inliers,
                H=H,
                quad=quad_transformed,
                match_count=int(status.sum()),
                pose=pose
            ))

        # 매칭 수 내림차순 정렬
        results.sort(key=lambda r: r.match_count, reverse=True)

        return results

    def _detect_features(self, image: np.ndarray) -> Tuple[List, Optional[np.ndarray]]:
        """특징점 및 디스크립터 추출"""
        # 그레이스케일 변환
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        keypoints, descriptors = self.detector.detectAndCompute(gray, None)

        if descriptors is None:
            return keypoints, None

        return keypoints, descriptors

    def _estimate_pose(self, quad_2d: np.ndarray,
                       world_coords: Tuple[float, float, float, float],
                       camera_matrix: np.ndarray,
                       dist_coeffs: Optional[np.ndarray]) -> Optional[Dict[str, Any]]:
        """
        PnP로 카메라 자세 추정

        Args:
            quad_2d: 이미지 상의 사각형 코너 (4x2)
            world_coords: (x0, y0, width, height) in mm
            camera_matrix: 카메라 내부 파라미터
            dist_coeffs: 왜곡 계수

        Returns:
            자세 정보 딕셔너리 또는 None
        """
        if dist_coeffs is None:
            dist_coeffs = np.zeros(5)

        x0, y0, width, height = world_coords

        # 3D 좌표 (Z=0 평면)
        quad_3d = np.float32([
            [x0, y0, 0],
            [x0 + width, y0, 0],
            [x0 + width, y0 + height, 0],
            [x0, y0 + height, 0]
        ])

        # PnP 풀이
        success, rvec, tvec = cv2.solvePnP(
            quad_3d, quad_2d, camera_matrix, dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:
            return None

        R, _ = cv2.Rodrigues(rvec)

        return {
            'R': R.tolist(),
            't': tvec.flatten().tolist(),
            'rvec': rvec.flatten().tolist()
        }

    def draw_tracked(self, frame: np.ndarray,
                     results: List[TrackedResult],
                     draw_matches: bool = True,
                     draw_quad: bool = True) -> np.ndarray:
        """
        추적 결과 시각화

        Args:
            frame: 입력 프레임
            results: 추적 결과 리스트
            draw_matches: 매칭 점 표시 여부
            draw_quad: 사각형 표시 여부

        Returns:
            시각화된 이미지
        """
        vis = frame.copy()

        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                  (255, 0, 255), (0, 255, 255)]

        for i, result in enumerate(results):
            color = colors[i % len(colors)]

            # 사각형 그리기
            if draw_quad and result.quad is not None:
                pts = np.int32(result.quad)
                cv2.polylines(vis, [pts], True, color, 2)

            # 매칭 점 그리기
            if draw_matches and result.p1 is not None:
                for pt in result.p1:
                    cv2.circle(vis, (int(pt[0]), int(pt[1])), 3, color, -1)

            # 정보 텍스트
            if result.quad is not None:
                center = result.quad.mean(axis=0)
                text = f"#{i}: {result.match_count} matches"
                cv2.putText(vis, text, (int(center[0]), int(center[1]) - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        return vis


class RealTimeTracker:
    """
    실시간 비디오 추적기

    웹캠이나 비디오 파일에서 실시간으로 평면을 추적합니다.
    """

    def __init__(self, detector_type: str = 'ORB'):
        if not HAS_CV2:
            raise ImportError("OpenCV (cv2) is required")

        self.tracker = PlaneTracker(detector_type=detector_type)
        self.cap: Optional[cv2.VideoCapture] = None
        self.paused = False

        # 기본 카메라 파라미터 (추정)
        self.camera_matrix: Optional[np.ndarray] = None
        self.dist_coeffs = np.zeros(5)

    def set_camera_params(self, focal_length: float,
                          image_size: Tuple[int, int],
                          dist_coeffs: Optional[np.ndarray] = None):
        """카메라 파라미터 설정"""
        w, h = image_size
        self.camera_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ], dtype=np.float64)

        if dist_coeffs is not None:
            self.dist_coeffs = dist_coeffs

    def add_target_from_file(self, image_path: str,
                             rect: Tuple[int, int, int, int],
                             world_coords: Optional[Tuple[float, float, float, float]] = None) -> int:
        """파일에서 타겟 추가"""
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Cannot read image: {image_path}")
        return self.tracker.add_target(image, rect, world_coords)

    def start_capture(self, source: int = 0):
        """비디오 캡처 시작"""
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video source: {source}")

        # 카메라 파라미터 자동 설정
        w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if self.camera_matrix is None:
            focal = max(w, h)
            self.set_camera_params(focal, (w, h))

    def stop_capture(self):
        """비디오 캡처 중지"""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def process_frame(self) -> Tuple[Optional[np.ndarray], List[TrackedResult]]:
        """
        한 프레임 처리

        Returns:
            (프레임, 추적 결과) 튜플
        """
        if self.cap is None or not self.cap.isOpened():
            return None, []

        ret, frame = self.cap.read()
        if not ret:
            return None, []

        results = self.tracker.track(frame, self.camera_matrix, self.dist_coeffs)

        return frame, results

    def run_interactive(self, window_name: str = 'Plane Tracker'):
        """
        대화형 추적 실행

        Keys:
            SPACE: 일시정지
            c: 타겟 지우기
            ESC: 종료
        """
        if self.cap is None:
            self.start_capture()

        cv2.namedWindow(window_name)

        while True:
            if not self.paused:
                frame, results = self.process_frame()
                if frame is None:
                    break

                vis = self.tracker.draw_tracked(frame, results)
                cv2.imshow(window_name, vis)

            key = cv2.waitKey(1) & 0xFF

            if key == ord(' '):
                self.paused = not self.paused
            elif key == ord('c'):
                self.tracker.clear()
            elif key == 27:  # ESC
                break

        self.stop_capture()
        cv2.destroyAllWindows()


# ============ CLI Interface ============

def main():
    """CLI 엔트리포인트"""
    import sys

    if len(sys.argv) < 2:
        print(json.dumps({
            'usage': 'python plane_tracker.py <command> [args]',
            'commands': {
                'track': 'track <ref_image> <x0> <y0> <x1> <y1> <test_image> - Track plane in image',
                'features': 'features <image> - Extract and count features',
                'live': 'live <ref_image> <x0> <y0> <x1> <y1> - Live webcam tracking'
            }
        }, indent=2))
        return

    cmd = sys.argv[1]

    if cmd == 'track' and len(sys.argv) >= 8:
        ref_path = sys.argv[2]
        rect = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
        test_path = sys.argv[7]

        ref_image = cv2.imread(ref_path)
        test_image = cv2.imread(test_path)

        if ref_image is None or test_image is None:
            print(json.dumps({'error': 'Cannot read images'}))
            return

        tracker = PlaneTracker()
        tracker.add_target(ref_image, rect)
        results = tracker.track(test_image)

        print(json.dumps({
            'success': True,
            'targets_tracked': len(results),
            'results': [r.to_dict() for r in results]
        }, indent=2))

    elif cmd == 'features' and len(sys.argv) >= 3:
        image_path = sys.argv[2]
        image = cv2.imread(image_path)

        if image is None:
            print(json.dumps({'error': f'Cannot read image: {image_path}'}))
            return

        tracker = PlaneTracker()
        kps, descs = tracker._detect_features(image)

        print(json.dumps({
            'success': True,
            'keypoints_count': len(kps),
            'descriptors_shape': list(descs.shape) if descs is not None else None
        }, indent=2))

    elif cmd == 'live' and len(sys.argv) >= 7:
        ref_path = sys.argv[2]
        rect = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))

        ref_image = cv2.imread(ref_path)
        if ref_image is None:
            print(json.dumps({'error': f'Cannot read image: {ref_path}'}))
            return

        rt_tracker = RealTimeTracker()
        rt_tracker.tracker.add_target(ref_image, rect)
        rt_tracker.run_interactive()

    else:
        print(json.dumps({'error': f'Unknown command: {cmd}'}))


if __name__ == '__main__':
    main()

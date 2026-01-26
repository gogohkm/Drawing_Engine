"""
Measure Module - 3D 측정 (Homography, PnP, ArUco, 평면 추적)

기존 모듈:
- frame_plane: Homography 기반 평면 캘리브레이션 (OpenCV 필요)
- pnp_solver: PnP 카메라 자세 계산 (OpenCV 필요)

신규 모듈 (Phase 1, 3):
- marker_detector: ArUco 마커 자동 감지 (OpenCV 필요)
- plane_tracker: ORB+FLANN 기반 평면 추적 (OpenCV 필요)
"""

# 기존 모듈 (OpenCV/numpy 필요)
try:
    from .frame_plane import calibrate_frame_plane, p2p_distance_mm, apply_H
    from .pnp_solver import solve_pnp, get_ray, intersect_ray_plane
    HAS_PNP_SOLVER = True
except ImportError:
    HAS_PNP_SOLVER = False
    calibrate_frame_plane = None
    p2p_distance_mm = None
    apply_H = None
    solve_pnp = None
    get_ray = None
    intersect_ray_plane = None

# 신규 모듈 (OpenCV 의존성)
try:
    from .marker_detector import MarkerDetector, CharucoDetector, MarkerInfo, CalibrationResult
    HAS_MARKER_DETECTOR = True
except ImportError:
    HAS_MARKER_DETECTOR = False
    MarkerDetector = None
    CharucoDetector = None
    MarkerInfo = None
    CalibrationResult = None

try:
    from .plane_tracker import PlaneTracker, RealTimeTracker, PlanarTarget, TrackedResult
    HAS_PLANE_TRACKER = True
except ImportError:
    HAS_PLANE_TRACKER = False
    PlaneTracker = None
    RealTimeTracker = None
    PlanarTarget = None
    TrackedResult = None

__all__ = [
    # 기존 API (가용 여부 확인 필요)
    'calibrate_frame_plane', 'p2p_distance_mm', 'apply_H',
    'solve_pnp', 'get_ray', 'intersect_ray_plane',
    # 신규 API (가용 여부 확인 필요)
    'MarkerDetector', 'CharucoDetector', 'MarkerInfo', 'CalibrationResult',
    'PlaneTracker', 'RealTimeTracker', 'PlanarTarget', 'TrackedResult',
    # 가용성 플래그
    'HAS_PNP_SOLVER', 'HAS_MARKER_DETECTOR', 'HAS_PLANE_TRACKER',
]

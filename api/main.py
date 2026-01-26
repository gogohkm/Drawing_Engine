"""
Drawing Engine API - Perspective & PnP 측정 서버

주요 기능:
- MVP-1: Homography 기반 평면 캘리브레이션
- MVP-2: PnP 기반 카메라 자세 및 3D 변환
- MVP-3: ArUco 마커 자동 감지
- MVP-4: 자동 선 추출 (Canny + HoughLinesP)
- MVP-5: 특징점 기반 평면 추적
- MVP-6: 다중 평면 3D 변환
"""
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import base64
import io

# 기존 모듈
from src.measure import calibrate_frame_plane, p2p_distance_mm, solve_pnp, get_ray, intersect_ray_plane

# 신규 모듈 (Phase 1-4)
try:
    from src.measure.marker_detector import MarkerDetector, CharucoDetector
    HAS_MARKER_DETECTOR = True
except ImportError:
    HAS_MARKER_DETECTOR = False

try:
    from src.vectorize.line_extractor import LineExtractor, ContourExtractor
    HAS_LINE_EXTRACTOR = True
except ImportError:
    HAS_LINE_EXTRACTOR = False

try:
    from src.measure.plane_tracker import PlaneTracker, RealTimeTracker
    HAS_PLANE_TRACKER = True
except ImportError:
    HAS_PLANE_TRACKER = False

try:
    from src.vectorize.transform_3d import Transform3D, PnPCalibrator, Plane
    HAS_TRANSFORM_3D = True
except ImportError:
    HAS_TRANSFORM_3D = False

# OpenCV (이미지 처리용)
try:
    import cv2
    import numpy as np
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False

app = FastAPI(
    title="Drawing Engine - Perspective & PnP API",
    description="사진에서 3D 도면으로 변환하는 측정 엔진 API",
    version="2.0.0"
)


# --- MVP-1 (Homography) Models ---

class CalibrateRequest(BaseModel):
    """4점 캘리브레이션 요청"""
    A: List[float]
    B: List[float]
    C: List[float]
    D: List[float]
    span_mm: float
    height_mm: Optional[float] = None


class P2PRequest(BaseModel):
    """두 점 거리 측정 요청"""
    H: List[List[float]]
    P1: List[float]
    P2: List[float]


# --- MVP-2 (PnP/Ray-Casting) Models ---

class PnPSolveRequest(BaseModel):
    """PnP 카메라 자세 계산 요청"""
    points2D: List[List[float]]  # [[u,v], ...]
    points3D: List[List[float]]  # [[X,Y,Z], ...]
    width: int
    height: int


class RayPlaneRequest(BaseModel):
    """픽셀→월드 좌표 변환 요청"""
    u: float
    v: float
    K: List[List[float]]
    R: List[List[float]]
    t: List[float]
    plane_n: List[float] = [0.0, 0.0, 1.0]  # Default Z=0 plane (Normal)
    plane_d: float = 0.0  # d value in n*x + d = 0


# --- MVP-3 (ArUco Marker Detection) Models ---

class MarkerDetectRequest(BaseModel):
    """ArUco 마커 감지 요청"""
    image_base64: str  # Base64 인코딩된 이미지
    dict_type: str = "DICT_6X6_250"  # ArUco 사전 타입


class MarkerCalibrateRequest(BaseModel):
    """마커 기반 캘리브레이션 요청"""
    image_base64: str
    marker_size_mm: float
    dict_type: str = "DICT_6X6_250"
    focal_length: Optional[float] = None


# --- MVP-4 (Line Extraction) Models ---

class LineExtractRequest(BaseModel):
    """선 추출 요청"""
    image_base64: str
    canny_low: int = 50
    canny_high: int = 150
    hough_threshold: int = 100
    min_length: int = 50
    max_gap: int = 10


class StructuralExtractRequest(BaseModel):
    """구조 요소 추출 요청"""
    image_base64: str
    column_tolerance: float = 5.0
    beam_tolerance: float = 5.0


# --- MVP-5 (Plane Tracking) Models ---

class PlaneTrackerAddTargetRequest(BaseModel):
    """평면 추적 대상 추가 요청"""
    image_base64: str
    rect: List[int]  # [x0, y0, x1, y1]
    world_coords: Optional[List[List[float]]] = None  # 월드 좌표 (옵션)


class PlaneTrackerTrackRequest(BaseModel):
    """평면 추적 요청"""
    frame_base64: str
    target_image_base64: str  # 참조 이미지
    target_rect: List[int]  # [x0, y0, x1, y1]


# --- MVP-6 (Multi-Plane Transform) Models ---

class MultiPlaneSetupRequest(BaseModel):
    """다중 평면 설정 요청"""
    floor_z: float = 0.0
    wall_back_y: Optional[float] = None
    wall_left_x: Optional[float] = None
    wall_right_x: Optional[float] = None
    ceiling_z: Optional[float] = None
    horizon_line_y: Optional[float] = None
    image_height: Optional[int] = None


class MultiPlaneTransformRequest(BaseModel):
    """다중 평면 자동 변환 요청"""
    pixels: List[List[float]]  # [[u, v], ...]
    R: List[List[float]]
    t: List[float]
    K: List[List[float]]
    multi_plane: MultiPlaneSetupRequest


# --- Helper Functions ---

def decode_base64_image(base64_str: str) -> 'np.ndarray':
    """Base64 이미지를 numpy 배열로 디코딩"""
    if not HAS_CV2:
        raise HTTPException(status_code=500, detail="OpenCV not installed")

    # data:image/xxx;base64, 접두사 제거
    if ',' in base64_str:
        base64_str = base64_str.split(',')[1]

    img_bytes = base64.b64decode(base64_str)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image data")

    return img


# --- Endpoints ---

@app.post("/frame/calibrate")
async def calibrate(req: CalibrateRequest):
    """4점 Homography 캘리브레이션"""
    try:
        H, Hinv, Lx, Ly = calibrate_frame_plane(
            req.A, req.B, req.C, req.D, req.span_mm, req.height_mm
        )
        return {"ok": True, "H_img_to_plane": H, "H_plane_to_img": Hinv, "Lx_mm": Lx, "Ly_mm": Ly}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/frame/p2p")
async def measure_p2p(req: P2PRequest):
    """두 점 간 거리 측정 (mm)"""
    try:
        result = p2p_distance_mm(req.H, req.P1, req.P2)
        if result is None:
            raise ValueError("Point transformation failed.")
        return {"ok": True, **result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/pnp/solve")
async def pnp_solve(req: PnPSolveRequest):
    """PnP로 카메라 자세(R, t) 계산"""
    # Guess Camera Matrix K
    f = max(req.width, req.height)
    cx, cy = req.width / 2, req.height / 2
    K = [[f, 0, cx], [0, f, cy], [0, 0, 1]]

    try:
        result = solve_pnp(req.points3D, req.points2D, K)
        if not result:
            raise HTTPException(status_code=400, detail="PnP Solver failed to find a solution")
        return {"ok": True, **result, "K": K}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/pnp/pixel-to-world")
async def pixel_to_world(req: RayPlaneRequest):
    """픽셀 좌표를 3D 월드 좌표로 변환"""
    try:
        origin, direction = get_ray(req.u, req.v, req.K, req.R, req.t)
        world_pt = intersect_ray_plane(origin, direction, req.plane_n, req.plane_d)
        if world_pt is None:
            raise HTTPException(status_code=400, detail="No intersection found")
        return {"ok": True, "world_pt": world_pt}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# === MVP-3: ArUco Marker Detection Endpoints ===

@app.post("/marker/detect")
async def detect_markers(req: MarkerDetectRequest):
    """이미지에서 ArUco 마커 감지"""
    if not HAS_MARKER_DETECTOR:
        raise HTTPException(status_code=501, detail="MarkerDetector module not available")

    try:
        img = decode_base64_image(req.image_base64)
        detector = MarkerDetector(dict_type=req.dict_type)
        corners, ids = detector.detect_markers(img)

        if ids is None:
            return {"ok": True, "markers": [], "count": 0}

        markers = []
        for i, marker_id in enumerate(ids.flatten()):
            markers.append({
                "id": int(marker_id),
                "corners": corners[i].tolist()
            })

        return {"ok": True, "markers": markers, "count": len(markers)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/marker/calibrate")
async def calibrate_from_marker(req: MarkerCalibrateRequest):
    """ArUco 마커에서 자동 캘리브레이션"""
    if not HAS_MARKER_DETECTOR:
        raise HTTPException(status_code=501, detail="MarkerDetector module not available")

    try:
        img = decode_base64_image(req.image_base64)
        detector = MarkerDetector(dict_type=req.dict_type)

        # 카메라 행렬 생성
        h, w = img.shape[:2]
        f = req.focal_length if req.focal_length else max(w, h)
        K = np.array([[f, 0, w/2], [0, f, h/2], [0, 0, 1]], dtype=np.float64)

        result = detector.calibrate_from_marker(img, req.marker_size_mm, K)

        if result is None or not result.success:
            return {"ok": False, "error": "Calibration failed - no markers detected"}

        return {
            "ok": True,
            "R": result.R.tolist() if result.R is not None else None,
            "t": result.t.flatten().tolist() if result.t is not None else None,
            "K": K.tolist(),
            "marker_ids": result.marker_ids
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/marker/homography")
async def get_marker_homography(req: MarkerCalibrateRequest):
    """마커 코너에서 Homography 계산"""
    if not HAS_MARKER_DETECTOR:
        raise HTTPException(status_code=501, detail="MarkerDetector module not available")

    try:
        img = decode_base64_image(req.image_base64)
        detector = MarkerDetector(dict_type=req.dict_type)
        corners, ids = detector.detect_markers(img)

        if corners is None or len(corners) == 0:
            return {"ok": False, "error": "No markers detected"}

        H = detector.get_homography_from_markers(corners, req.marker_size_mm)

        return {
            "ok": True,
            "H": H.tolist(),
            "marker_size_mm": req.marker_size_mm
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# === MVP-4: Line Extraction Endpoints ===

@app.post("/line/extract")
async def extract_lines(req: LineExtractRequest):
    """이미지에서 구조선 추출 (Canny + HoughLinesP)"""
    if not HAS_LINE_EXTRACTOR:
        raise HTTPException(status_code=501, detail="LineExtractor module not available")

    try:
        img = decode_base64_image(req.image_base64)
        extractor = LineExtractor(
            canny_low=req.canny_low,
            canny_high=req.canny_high,
            hough_threshold=req.hough_threshold,
            min_line_length=req.min_length,
            max_line_gap=req.max_gap
        )

        lines = extractor.extract_lines(img)

        # Line2D 객체를 직렬화 (3D 좌표 포함)
        line_data = []
        for line in lines:
            # Line2D.start/end는 이제 3D 튜플 (x, y, z)
            line_data.append({
                "start": {"x": line.start[0], "y": line.start[1], "z": line.start[2] if len(line.start) > 2 else 0},
                "end": {"x": line.end[0], "y": line.end[1], "z": line.end[2] if len(line.end) > 2 else 0},
                "angle": line.angle,
                "length": line.length
            })

        return {"ok": True, "lines": line_data, "count": len(lines)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/line/structural")
async def extract_structural_elements(req: StructuralExtractRequest):
    """구조 요소 추출 (기둥, 빔, 래프터)"""
    if not HAS_LINE_EXTRACTOR:
        raise HTTPException(status_code=501, detail="LineExtractor module not available")

    try:
        img = decode_base64_image(req.image_base64)
        extractor = LineExtractor()
        lines = extractor.extract_lines(img)

        elements = extractor.classify_structural_elements(
            lines,
            vertical_tolerance=req.column_tolerance,
            horizontal_tolerance=req.beam_tolerance
        )

        def serialize_lines(line_list):
            """선 리스트를 3D 좌표로 직렬화"""
            return [{
                "start": {"x": l.start[0], "y": l.start[1], "z": l.start[2] if len(l.start) > 2 else 0},
                "end": {"x": l.end[0], "y": l.end[1], "z": l.end[2] if len(l.end) > 2 else 0},
                "angle": l.angle,
                "length": l.length
            } for l in line_list]

        return {
            "ok": True,
            "columns": serialize_lines(elements.columns),
            "beams": serialize_lines(elements.beams),
            "rafters": serialize_lines(elements.rafters),
            "other": serialize_lines(elements.other),
            "summary": {
                "columns": len(elements.columns),
                "beams": len(elements.beams),
                "rafters": len(elements.rafters),
                "other": len(elements.other)
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# === MVP-5: Plane Tracking Endpoints ===

@app.post("/tracker/track")
async def track_plane(req: PlaneTrackerTrackRequest):
    """참조 이미지 기반 평면 추적"""
    if not HAS_PLANE_TRACKER:
        raise HTTPException(status_code=501, detail="PlaneTracker module not available")

    try:
        target_img = decode_base64_image(req.target_image_base64)
        frame = decode_base64_image(req.frame_base64)

        tracker = PlaneTracker()
        x0, y0, x1, y1 = req.target_rect
        tracker.add_target(target_img, (x0, y0, x1, y1))

        results = tracker.track(frame)

        if not results:
            return {"ok": True, "tracked": False, "message": "Target not found in frame"}

        tracked = results[0]
        return {
            "ok": True,
            "tracked": True,
            "quad": tracked.quad.tolist(),
            "H": tracked.H.tolist() if tracked.H is not None else None,
            "inliers": int(tracked.inliers)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# === MVP-6: Multi-Plane Transform Endpoints ===

@app.post("/transform/multi-plane")
async def transform_multi_plane(req: MultiPlaneTransformRequest):
    """다중 평면 자동 선택 3D 변환"""
    if not HAS_TRANSFORM_3D:
        raise HTTPException(status_code=501, detail="Transform3D module not available")

    try:
        transformer = Transform3D()
        transformer.setup_pnp(req.R, req.t, req.K)

        mp = req.multi_plane
        transformer.setup_multi_plane(
            floor_z=mp.floor_z,
            wall_back_y=mp.wall_back_y,
            wall_left_x=mp.wall_left_x,
            wall_right_x=mp.wall_right_x,
            ceiling_z=mp.ceiling_z,
            horizon_line_y=mp.horizon_line_y,
            image_height=mp.image_height
        )

        pixel_tuples = [(p[0], p[1]) for p in req.pixels]
        results = transformer.transform_polyline_auto(pixel_tuples)

        output = []
        for r in results:
            output.append({
                "point_3d": r['point'].to_list(),
                "plane": r['plane'],
                "pixel": r['pixel']
            })

        return {
            "ok": True,
            "points": output,
            "count": len(output),
            "plane_info": transformer.get_plane_info()
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/transform/plane-info")
async def get_plane_info():
    """현재 지원하는 평면 타입 정보"""
    return {
        "ok": True,
        "plane_types": [
            {"name": "floor", "description": "바닥면 (Z = constant)", "normal": [0, 0, 1]},
            {"name": "wall_back", "description": "뒷벽 (Y = constant)", "normal": [0, 1, 0]},
            {"name": "wall_left", "description": "왼쪽벽 (X = constant)", "normal": [1, 0, 0]},
            {"name": "wall_right", "description": "오른쪽벽 (X = constant)", "normal": [1, 0, 0]},
            {"name": "ceiling", "description": "천장 (Z = constant)", "normal": [0, 0, 1]}
        ],
        "auto_selection": "이미지 영역에 따라 자동 선택 (horizon_line_y 기준)"
    }


# === System Status Endpoint ===

@app.get("/status")
async def get_status():
    """시스템 상태 및 모듈 가용성 확인"""
    return {
        "ok": True,
        "modules": {
            "opencv": HAS_CV2,
            "marker_detector": HAS_MARKER_DETECTOR,
            "line_extractor": HAS_LINE_EXTRACTOR,
            "plane_tracker": HAS_PLANE_TRACKER,
            "transform_3d": HAS_TRANSFORM_3D
        },
        "features": {
            "homography_calibration": True,
            "pnp_solving": True,
            "aruco_detection": HAS_MARKER_DETECTOR,
            "line_extraction": HAS_LINE_EXTRACTOR,
            "plane_tracking": HAS_PLANE_TRACKER,
            "multi_plane_transform": HAS_TRANSFORM_3D
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

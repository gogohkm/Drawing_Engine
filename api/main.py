"""
Drawing Engine API - Perspective & PnP 측정 서버
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from src.measure import calibrate_frame_plane, p2p_distance_mm, solve_pnp, get_ray, intersect_ray_plane

app = FastAPI(title="Drawing Engine - Perspective & PnP API")


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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

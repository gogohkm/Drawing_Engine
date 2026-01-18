from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import numpy as np
from backend.frame_plane import calibrate_frame_plane, p2p_distance_mm
from backend.pnp_solver import solve_pnp, get_ray, intersect_ray_plane

app = FastAPI(title="Drawing Engine - Perspective & PnP API")

# --- MVP-1 (Homography) Models ---
class CalibrateRequest(BaseModel):
    A: List[float]
    B: List[float]
    C: List[float]
    D: List[float]
    span_mm: float
    height_mm: Optional[float] = None

class P2PRequest(BaseModel):
    H: List[List[float]]
    P1: List[float]
    P2: List[float]

# --- MVP-2 (PnP/Ray-Casting) Models ---
class PnPSolveRequest(BaseModel):
    points2D: List[List[float]] # [[u,v], ...]
    points3D: List[List[float]] # [[X,Y,Z], ...]
    width: int
    height: int

class RayPlaneRequest(BaseModel):
    u: float
    v: float
    K: List[List[float]]
    R: List[List[float]]
    t: List[float]
    plane_n: List[float] = [0.0, 0.0, 1.0] # Default Z=0 plane (Normal)
    plane_d: float = 0.0 # d value in n*x + d = 0

@app.post("/frame/calibrate")
async def calibrate(req: CalibrateRequest):
    try:
        H, Hinv, Lx, Ly = calibrate_frame_plane(
            req.A, req.B, req.C, req.D, req.span_mm, req.height_mm
        )
        return {"ok": True, "H_img_to_plane": H, "H_plane_to_img": Hinv, "Lx_mm": Lx, "Ly_mm": Ly}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/frame/p2p")
async def measure_p2p(req: P2PRequest):
    try:
        result = p2p_distance_mm(req.H, req.P1, req.P2)
        if result is None: raise ValueError("Point transformation failed.")
        return {"ok": True, **result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- PnP Endpoints ---

@app.post("/pnp/solve")
async def pnp_solve(req: PnPSolveRequest):
    # Guess Camera Matrix K
    f = max(req.width, req.height) 
    cx, cy = req.width / 2, req.height / 2
    K = [[f, 0, cx], [0, f, cy], [0, 0, 1]]
    
    try:
        result = solve_pnp(req.points3D, req.points2D, K)
        if not result:
            return {"ok": False, "error": "PnP Solver failed to find a solution"}
        return {"ok": True, **result, "K": K}
    except Exception as e:
        print(f"PnP Error: {str(e)}")
        return {"ok": False, "error": str(e)}

@app.post("/pnp/pixel-to-world")
async def pixel_to_world(req: RayPlaneRequest):
    try:
        origin, direction = get_ray(req.u, req.v, req.K, req.R, req.t)
        world_pt = intersect_ray_plane(origin, direction, req.plane_n, req.plane_d)
        if world_pt is None:
            return {"ok": False, "error": "No intersection found"}
        return {"ok": True, "world_pt": world_pt}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

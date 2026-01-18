# Project Handoff: 3D Measurement from Photo

## 1. Objective
Establish a system to measure real-world 3D distances (mm) from a single perspective photograph, integrating with a DXF viewing/generating engine.

## 2. Implemented Components

### MVP-1: Plane Homography (Completed)
- **Logic**: Uses a 3x3 Homography matrix to map 2D pixels to a 2D real-world plane (e.g., a wall or floor).
- **Files**: `backend/frame_plane.py` (solver), `homography_calib.json` (stored matrix).
- **Result**: Successfully generated `real_world_3d_output.dxf` where 2D pixels are unfolded into a 1:1 scale flat plane.

### MVP-2: True 3D PnP & Ray-Casting (Completed)
- **Logic**: Solves for Camera Pose ($R, t$) and Intrinsics ($K$) using Perspective-n-Point. Uses Ray-Casting to find 3D intersections with defined planes ($Z=0$, $Y=0$, etc.).
- **Files**: `backend/pnp_solver.py` (PnP & Intersection logic), `backend/main.py` (FastAPI endpoints).
- **Capabilities**: Can calculate $Z$ coordinates (depth/height) if 3D reference points are provided.

### DXF Engine Upgrade (Completed)
- **Core**: `knowledge/engine/image_vectorizer.py` updated.
    - `Point` class now supports `x, y, z`.
    - `write_lines_to_dxf` now writes 3D group codes (`30`, `31` for $Z$).
    - Added `cli_vectorize_real_world_dxf` to generate mm-scale DXF directly from photo + calibration.

### Frontend UI (Completed)
- **UI**: `extension/media/index.html` & `main.js`.
- **Features**: Point picking for both Homography (4 pts) and PnP (4+ pts with manual 3D entry). Visual feedback for measurements.

## 3. Current Status & Findings
- **3D DXF Generation**: Verified. `real_world_3d_output.dxf` contains mm-unit lines.
- **Z-Coordinate Issue**: Currently, most lines have $Z=0$ because they were generated via Homography (plane-based). PnP is ready to generate $Z \neq 0$ data once 3D reference points are inputted.
- **Scale**: Verified. A measured line showed ~10,057mm (10m), matching expected real-world proportions.

## 4. Instructions for Next Session
1. **PnP Calibration**: Use the new PnP UI to pick points and enter their true 3D coordinates ($X, Y, Z$) to solve for a camera pose that understands depth.
2. **3D Visualization**: Once `stgen` is upgraded for 3D, use it to verify that lines are correctly placed in 3D space (not just a flat plane).
3. **Multi-Plane Tracing**: Run `vectorize_real_world_dxf` using the `pnp` method to get a DXF with varying $Z$ levels.

## 5. Key Command
To generate a 3D DXF based on current calibration:
`python3 run_3d_vectorize.py`

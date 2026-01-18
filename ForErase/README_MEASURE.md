# Perspective Plane Measurement (MVP-1) - Implementation Summary

Implementation of 3D distance measurement from a single perspective photo on a calibrated plane.

## 1. Components Created

- **Backend**:
  - `backend/frame_plane.py`: Core geometry logic (Homography matrix, point transformation, Euclidean distance in mm).
  - `backend/main.py`: FastAPI server with `/frame/calibrate` and `/frame/p2p` endpoints.
- **Frontend (Webview)**:
  - `extension/media/index.html`: Updated layout with Plane Measurement controls (Span, Height inputs, Calibrate/Measure buttons).
  - `extension/media/main.js`: Integrated point collection and API communication for the measurement workflow.

## 2. Methodology: MVP-1 (Plane-based P2P)

1. **Photo Trace**: The photo is traced into a 2D DXF where coordinates are pixel-based (`ImageVectorizer`).
2. **Calibration**:
   - User picks 4 points on a known plane (e.g., front face of a frame).
   - User inputs the actual real-world **Span (mm)**.
   - The system calculates a **Homography Matrix (H)** that maps image pixels directly to real-world coordinates on that plane.
   - Vertical scale (Ly) is automatically derived from the image's aspect ratio of the selected rectangle if `height_mm` is not provided.
3. **Measurement**:
   - User picks any 2 points *on the calibrated plane*.
   - The system applies $H$ to transform them to plane coordinates $[X, Y]$ in mm.
   - The system calculates the distance using $\sqrt{(X_2-X_1)^2 + (Y_2-Y_1)^2}$.

## 3. How to Run & Test

### Start the Backend
```bash
# In the project root
export PYTHONPATH=.
./.venv/bin/python3 backend/main.py
```
The server will start on `http://localhost:8000`.

### Test with CLI (Example)
```bash
# Calibrate with 4 points and 10m span
curl -X POST http://localhost:8000/frame/calibrate \
-H "Content-Type: application/json" \
-d '{"A":[100,100], "B":[900,150], "C":[920,600], "D":[80,580], "span_mm":10000}'

# This returns a homography matrix H. Use it for measurement:
curl -X POST http://localhost:8000/frame/p2p \
-H "Content-Type: application/json" \
-d '{
  "H": [[...]], 
  "P1": [200, 200],
  "P2": [300, 300]
}'
```

### Visual Verification
The `extension/media/index.html` can be opened in a browser (or via VS Code Webview) to interactively pick points and see results.

## 4. Next Steps (MVP-2)
- Support multiple calibrated planes (Floor, Walls).
- Allow user to switch between planes for different measurements.
- Implement dimension line generation in DXF from the measurement result.

import json
import subprocess
import os

def run_3d_vectorization():
    # Load calibration
    with open('homography_calib.json', 'r') as f:
        calib = json.load(f)
    
    params = {"H": calib['h_matrix']}
    options = {"layer": "REAL_WORLD_3D_MM", "epsilon": 1.5, "mode": "edge"}
    
    cmd = [
        "./.venv/bin/python3",
        "knowledge/engine/image_vectorizer.py",
        "vectorize_real_world_dxf",
        "/Users/hi/2026Coding_Prj/Drawing_Engine/Ref/mosateyn8U-1024x768.jpeg",
        "/Users/hi/2026Coding_Prj/Drawing_Engine/real_world_3d_output.dxf",
        "homography",
        json.dumps(params),
        json.dumps(options)
    ]
    
    print(f"Running command...")
    result = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "."})
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)

if __name__ == "__main__":
    run_3d_vectorization()

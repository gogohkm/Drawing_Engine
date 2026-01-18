import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_pnp_workflow():
    print("--- Testing PnP Workflow ---")
    
    # 1. Solve PnP
    # Setup 4 points of a 10m x 10m square in 3D
    points3D = [
        [0, 0, 0],    # A (TL)
        [10000, 0, 0], # B (TR)
        [10000, 10000, 0], # C (BR)
        [0, 10000, 0]  # D (BL)
    ]
    # Corresponding pixels (assuming typical FOV)
    points2D = [
        [100, 100],
        [900, 150],
        [920, 800],
        [80, 750]
    ]
    
    solve_req = {
        "points2D": points2D,
        "points3D": points3D,
        "width": 1024,
        "height": 768
    }
    
    print("Sending /pnp/solve...")
    solve_res = requests.post(f"{BASE_URL}/pnp/solve", json=solve_req).json()
    
    if not solve_res.get("ok"):
        print("PnP Solve Failed:", solve_res.get("error"))
        return
    
    print("PnP Solved Success!")
    R = solve_res["R"]
    t = solve_res["t"]
    K = solve_res["K"]
    
    # 2. Test Pixel to World (Ray-Casting)
    # Pick a point in the middle of the square
    px_req = {
        "u": 500, "v": 450,
        "R": R, "t": t, "K": K,
        "plane_n": [0, 0, 1], # Floor plane
        "plane_d": 0
    }
    
    print("Sending /pnp/pixel-to-world...")
    px_res = requests.post(f"{BASE_URL}/pnp/pixel-to-world", json=px_req).json()
    
    if px_res.get("ok"):
        print("Intersection Point:", px_res["world_pt"])
    else:
        print("Ray-Casting Failed:", px_res.get("error"))

if __name__ == "__main__":
    try:
        test_pnp_workflow()
    except Exception as e:
        print("Backend might be offline. Error:", e)

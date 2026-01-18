import numpy as np
import cv2

def _to_homog(pt2):
    return np.array([pt2[0], pt2[1], 1.0], dtype=np.float64)

def apply_H(H, uv):
    """
    Applies 3x3 Homography matrix H to image point [u, v].
    Returns [X, Y] in plane coordinates.
    """
    H = np.asarray(H, dtype=np.float64)
    p_img = _to_homog(uv)
    p_plane = H @ p_img
    if abs(p_plane[2]) < 1e-9:
        return None
    return [p_plane[0] / p_plane[2], p_plane[1] / p_plane[2]]

def calibrate_frame_plane(A, B, C, D, span_mm, height_mm=None):
    """
    Calibrates a plane using 4 points on the image (A, B, C, D)
    and one known span (width) in mm.
    A: Top-Left, B: Top-Right, C: Bottom-Right, D: Bottom-Left (conceptual order)
    Actually, target points are:
    A -> [0, 0]
    B -> [L, 0]
    C -> [L, Ly]
    D -> [0, Ly]
    """
    A = np.asarray(A, dtype=np.float64)
    B = np.asarray(B, dtype=np.float64)
    C = np.asarray(C, dtype=np.float64)
    D = np.asarray(D, dtype=np.float64)

    L = float(span_mm)

    if height_mm is not None:
        Ly = float(height_mm)
    else:
        # MVP-1: Derive Ly from image aspect ratio of the 'rectangle'
        lenAB = float(np.linalg.norm(B - A))
        lenAD = float(np.linalg.norm(D - A))
        if lenAB < 1e-6:
            raise ValueError("Points A and B are too close.")
        r = lenAD / lenAB
        Ly = r * L

    src = np.array([A, B, C, D], dtype=np.float64)  # Image pixels
    dst = np.array([[0, 0], [L, 0], [L, Ly], [0, Ly]], dtype=np.float64)  # Plane (mm)

    H, _ = cv2.findHomography(src, dst, method=0)
    if H is None:
        raise ValueError("Homography calculation failed.")

    Hinv = np.linalg.inv(H)
    return H.tolist(), Hinv.tolist(), L, Ly

def p2p_distance_mm(H_img_to_plane, P1, P2):
    """
    Calculates distance in mm between two image points P1, P2
    using the calibrated Homography matrix.
    """
    X1 = apply_H(H_img_to_plane, P1)
    X2 = apply_H(H_img_to_plane, P2)
    if X1 is None or X2 is None:
        return None
    
    dx = X2[0] - X1[0]
    dy = X2[1] - X1[1]
    dist = float(np.hypot(dx, dy))
    
    return {
        "P1_plane": X1,
        "P2_plane": X2,
        "distance_mm": dist
    }

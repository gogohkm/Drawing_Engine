import numpy as np
import cv2
import math

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
        # Improved Metric Rectification
        def get_intersection(p1, p2, p3, p4):
            x1, y1 = p1; x2, y2 = p2
            x3, y3 = p3; x4, y4 = p4
            denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
            if abs(denom) < 1e-9: return None
            ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
            return np.array([x1 + ua*(x2-x1), y1 + ua*(y2-y1)])

        v1 = get_intersection(A, B, D, C) # VP horizontal
        v2 = get_intersection(A, D, B, C) # VP vertical

        # Assume principal point (c) is image center if not provided. 
        # For 1024x768, it's (512, 384)
        c = np.array([512, 384]) 

        if v1 is not None and v2 is not None:
            # Estimate focal length f: f^2 = -(v1-c).dot(v2-c)
            f_sq = -np.dot(v1 - c, v2 - c)
            f = math.sqrt(abs(f_sq)) if f_sq > 0 else 1000.0
            
            # Metric rectification formula to find Aspect Ratio
            # We transform points to a coordinate system where c is origin and scale by f
            def to_metric(p):
                return np.array([(p[0]-c[0])/f, (p[1]-c[1])/f, 1.0])
            
            ma, mb, md = to_metric(A), to_metric(B), to_metric(D)
            # The ratio of sides in 3D: (Ly/Lx)^2
            # dist_3d^2 = (m1.cross(m2).norm() / (n.dot(m1)*n.dot(m2))) ... simplification:
            v1_m = (v1 - c) / f
            v2_m = (v2 - c) / f
            
            # Complex but more accurate metric ratio
            try:
                # Normal of the plane in camera coords
                n = np.cross(np.append(v1_m, 1), np.append(v2_m, 1))
                n /= np.linalg.norm(n)
                
                def length_3d(m1, m2, n):
                    # Relative length in 3D space
                    return np.linalg.norm(np.cross(m1, m2)) / (np.dot(n, m1) * np.dot(n, m2))

                len_x = length_3d(ma, mb, n)
                len_y = length_3d(ma, md, n)
                ratio = math.sqrt(abs(len_y / len_x))
                Ly = L * ratio
                print(f"DEBUG: Metric Aspect Ratio: {ratio:.4f}, Ly: {Ly:.2f}, f: {f:.1f}")
            except:
                Ly = L * (np.linalg.norm(D - A) / np.linalg.norm(B - A))
        else:
            Ly = L * (np.linalg.norm(D - A) / np.linalg.norm(B - A))

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

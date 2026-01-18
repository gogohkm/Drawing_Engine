import numpy as np
import cv2

def solve_pnp(object_points, image_points, camera_matrix, dist_coeffs=None):
    """
    Computes camera pose (R, t) from 3D-2D point correspondences.
    - object_points: List of [X, Y, Z]
    - image_points: List of [u, v]
    - camera_matrix: 3x3 array
    """
    obj_pts = np.array(object_points, dtype=np.float64)
    img_pts = np.array(image_points, dtype=np.float64)
    K = np.array(camera_matrix, dtype=np.float64)
    dist = np.array(dist_coeffs, dtype=np.float64) if dist_coeffs is not None else np.zeros(5)

    success, rvec, tvec = cv2.solvePnP(obj_pts, img_pts, K, dist, flags=cv2.SOLVEPNP_ITERATIVE)
    
    if not success:
        return None

    R, _ = cv2.Rodrigues(rvec)
    
    return {
        "R": R.tolist(),
        "t": tvec.flatten().tolist(),
        "rvec": rvec.flatten().tolist()
    }

def get_ray(u, v, K, R, t):
    """
    Computes a 3D ray in world coordinates from a pixel (u,v).
    Ray = origin + lambda * direction
    """
    K_inv = np.linalg.inv(np.array(K))
    R_inv = np.linalg.inv(np.array(R))
    t = np.array(t).reshape(3, 1)

    # Pixel to Normalized Camera Coordinates
    p_img = np.array([u, v, 1.0]).reshape(3, 1)
    p_cam_dir = K_inv @ p_img
    
    # Camera to World Coordinates
    # Ray origin in world coord = -R_inv * t
    ray_origin = -R_inv @ t
    # Ray direction in world coord = R_inv * p_cam_dir
    ray_direction = R_inv @ p_cam_dir
    ray_direction /= np.linalg.norm(ray_direction)

    return ray_origin.flatten(), ray_direction.flatten()

def intersect_ray_plane(ray_origin, ray_direction, plane_n, plane_d):
    """
    Intersects a ray with a plane defined by n·x + d = 0
    - plane_n: normal vector [nx, ny, nz]
    - plane_d: offset
    """
    ray_o = np.array(ray_origin)
    ray_d = np.array(ray_direction)
    n = np.array(plane_n)
    d = float(plane_d)

    dot = np.dot(n, ray_d)
    if abs(dot) < 1e-6:
        return None # Parallel to plane

    t = -(np.dot(n, ray_o) + d) / dot
    if t < 0:
        return None # Intersection is behind the camera

    intersection = ray_o + t * ray_d
    return intersection.tolist()

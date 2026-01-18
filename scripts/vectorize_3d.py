#!/usr/bin/env python3
"""
3D Vectorization Script - 사진을 3D 도면으로 변환

사용법:
    # 깊이 추정 기반 (기준점 불필요)
    python scripts/vectorize_3d.py depth <image_path> <output.dxf>

    # PnP 기반 (기준점 필요)
    python scripts/vectorize_3d.py pnp <image_path> <output.dxf> <points.json>

    # Homography 기반 (4점 필요)
    python scripts/vectorize_3d.py homography <image_path> <output.dxf> <4points.json> <span_mm>
"""

import sys
import os
import json
import math

# 프로젝트 루트 추가
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from src.vectorize.image_vectorizer import ImageVectorizer, write_lines_to_dxf, Point, Line
from src.vectorize.transform_3d import Transform3D, PnPCalibrator, Point3D, Plane


def vectorize_with_depth_estimation(
    image_path: str,
    output_dxf: str,
    horizon_ratio: float = 0.35,
    camera_height_mm: float = 1600.0,
    near_depth_mm: float = 2000.0,
    far_depth_mm: float = 30000.0,
    options: dict = None
) -> dict:
    """
    깊이 추정 기반 3D 벡터화

    PnP 캘리브레이션 없이 이미지의 Y 좌표를 기반으로 깊이를 추정합니다.
    - 이미지 하단 = 카메라 가까이 (바닥)
    - 소실점 = 멀리 (무한대)

    Args:
        image_path: 입력 이미지 경로
        output_dxf: 출력 DXF 경로
        horizon_ratio: 소실점 Y 위치 (0=상단, 1=하단), 기본 0.35
        camera_height_mm: 카메라 높이 (mm)
        near_depth_mm: 이미지 하단의 깊이
        far_depth_mm: 소실점의 깊이
        options: 벡터화 옵션

    Returns:
        결과 딕셔너리
    """
    if options is None:
        options = {}

    # 1. 이미지 벡터화 (픽셀 좌표)
    vectorizer = ImageVectorizer()
    vectorizer.mode = options.get('mode', 'edge')
    vectorizer.edge_threshold = options.get('edge_threshold', 40)
    vectorizer.simplify_epsilon = options.get('epsilon', 2.0)

    if not vectorizer.load_image(image_path):
        return {'success': False, 'error': 'Failed to load image'}

    width = vectorizer.binary_image.width
    height = vectorizer.binary_image.height

    vectorizer.set_output_bounds(0, 0, width, height)
    vectorizer.vectorize()

    if not vectorizer.lines:
        return {'success': False, 'error': 'No lines extracted'}

    print(f"Extracted {len(vectorizer.lines)} lines from image ({width}x{height})")

    # 2. 3D 변환기 설정
    transformer = Transform3D()
    transformer.setup_depth_estimation(
        image_width=width,
        image_height=height,
        horizon_ratio=horizon_ratio,
        camera_height_mm=camera_height_mm,
        near_depth_mm=near_depth_mm,
        far_depth_mm=far_depth_mm
    )

    # 3. 각 선을 3D 좌표로 변환
    lines_3d = []
    for line in vectorizer.lines:
        p1_3d = transformer.pixel_to_world(line.start.x, line.start.y)
        p2_3d = transformer.pixel_to_world(line.end.x, line.end.y)

        if p1_3d and p2_3d:
            lines_3d.append(Line(
                start=Point(p1_3d.x, p1_3d.y, p1_3d.z),
                end=Point(p2_3d.x, p2_3d.y, p2_3d.z),
                layer=options.get('layer', 'TRACE_3D')
            ))

    print(f"Transformed {len(lines_3d)} lines to 3D")

    # 4. DXF 저장
    layer = options.get('layer', 'TRACE_3D')
    result = write_lines_to_dxf(lines_3d, output_dxf, layer)

    return {
        'success': True,
        'lines_2d': len(vectorizer.lines),
        'lines_3d': len(lines_3d),
        'image_size': [width, height],
        'transform_method': 'depth_estimation',
        'parameters': {
            'horizon_ratio': horizon_ratio,
            'camera_height_mm': camera_height_mm,
            'near_depth_mm': near_depth_mm,
            'far_depth_mm': far_depth_mm
        },
        **result
    }


def vectorize_with_pnp(
    image_path: str,
    output_dxf: str,
    points_2d: list,
    points_3d: list,
    planes: dict = None,
    options: dict = None
) -> dict:
    """
    PnP 기반 3D 벡터화

    2D-3D 대응점으로 카메라 자세를 계산하고 광선-평면 교차로 3D 좌표를 구합니다.

    Args:
        image_path: 입력 이미지 경로
        output_dxf: 출력 DXF 경로
        points_2d: 2D 픽셀 좌표 리스트 [[u, v], ...]
        points_3d: 3D 월드 좌표 리스트 [[x, y, z], ...]
        planes: 평면 정의 {'floor': {'z': 0}, 'wall': {'y': 10000}}
        options: 벡터화 옵션

    Returns:
        결과 딕셔너리
    """
    if options is None:
        options = {}
    if planes is None:
        planes = {'floor': {'z': 0}}

    # 1. 이미지 벡터화 (픽셀 좌표)
    vectorizer = ImageVectorizer()
    vectorizer.mode = options.get('mode', 'edge')
    vectorizer.edge_threshold = options.get('edge_threshold', 40)
    vectorizer.simplify_epsilon = options.get('epsilon', 2.0)

    if not vectorizer.load_image(image_path):
        return {'success': False, 'error': 'Failed to load image'}

    width = vectorizer.binary_image.width
    height = vectorizer.binary_image.height

    vectorizer.set_output_bounds(0, 0, width, height)
    vectorizer.vectorize()

    if not vectorizer.lines:
        return {'success': False, 'error': 'No lines extracted'}

    print(f"Extracted {len(vectorizer.lines)} lines from image ({width}x{height})")

    # 2. PnP 캘리브레이션
    calibrator = PnPCalibrator(width, height)
    for p2d, p3d in zip(points_2d, points_3d):
        calibrator.add_correspondence(tuple(p2d), tuple(p3d))

    calib_result = calibrator.calibrate()
    if not calib_result.get('success'):
        return {'success': False, 'error': f"PnP calibration failed: {calib_result.get('error')}"}

    print(f"PnP calibration successful")

    # 3. 3D 변환기 설정
    transformer = Transform3D()
    transformer.setup_pnp(calib_result['R'], calib_result['t'], calib_result['K'])
    transformer.image_width = width
    transformer.image_height = height

    # 평면 추가
    for name, params in planes.items():
        if 'z' in params:
            transformer.add_plane(name, Plane.floor(params['z']))
        elif 'y' in params:
            transformer.add_plane(name, Plane.wall_back(params['y']))
        elif 'x' in params:
            transformer.add_plane(name, Plane.wall_left(params['x']))

    # 4. 각 선을 3D 좌표로 변환
    lines_3d = []
    default_plane = 'floor'

    for line in vectorizer.lines:
        # Y 좌표가 소실점 위인지 아래인지로 평면 선택
        avg_v = (line.start.y + line.end.y) / 2
        plane_name = default_plane

        # 간단한 휴리스틱: 이미지 상단 40%는 벽으로 처리
        if avg_v < height * 0.4 and 'wall' in transformer.planes:
            plane_name = 'wall'

        p1_3d = transformer.pixel_to_world(line.start.x, line.start.y, plane_name)
        p2_3d = transformer.pixel_to_world(line.end.x, line.end.y, plane_name)

        if p1_3d and p2_3d:
            lines_3d.append(Line(
                start=Point(p1_3d.x, p1_3d.y, p1_3d.z),
                end=Point(p2_3d.x, p2_3d.y, p2_3d.z),
                layer=options.get('layer', 'TRACE_3D')
            ))

    print(f"Transformed {len(lines_3d)} lines to 3D")

    # 5. DXF 저장
    layer = options.get('layer', 'TRACE_3D')
    result = write_lines_to_dxf(lines_3d, output_dxf, layer)

    return {
        'success': True,
        'lines_2d': len(vectorizer.lines),
        'lines_3d': len(lines_3d),
        'image_size': [width, height],
        'transform_method': 'pnp',
        'calibration': {
            'R': calib_result['R'],
            't': calib_result['t'],
            'K': calib_result['K']
        },
        **result
    }


def vectorize_pixel_coords(
    image_path: str,
    output_dxf: str,
    options: dict = None
) -> dict:
    """
    픽셀 좌표 그대로 벡터화 (1:1 매핑)

    변환 없이 이미지의 픽셀 좌표를 그대로 DXF 좌표로 사용합니다.
    나중에 바닥면을 지정하여 Homography 변환할 수 있습니다.

    Args:
        image_path: 입력 이미지 경로
        output_dxf: 출력 DXF 경로
        options: 벡터화 옵션

    Returns:
        결과 딕셔너리
    """
    if options is None:
        options = {}

    # 1. 이미지 벡터화 (픽셀 좌표)
    vectorizer = ImageVectorizer()
    vectorizer.mode = options.get('mode', 'edge')
    vectorizer.edge_threshold = options.get('edge_threshold', 40)
    vectorizer.simplify_epsilon = options.get('epsilon', 2.0)
    vectorizer.min_contour_length = options.get('min_length', 10)

    if not vectorizer.load_image(image_path):
        return {'success': False, 'error': 'Failed to load image'}

    width = vectorizer.binary_image.width
    height = vectorizer.binary_image.height

    vectorizer.set_output_bounds(0, 0, width, height)
    vectorizer.vectorize()

    if not vectorizer.lines:
        return {'success': False, 'error': 'No lines extracted'}

    print(f"Extracted {len(vectorizer.lines)} lines from image ({width}x{height})")

    # 2. 픽셀 좌표 그대로 저장 (Y축 반전 없음 - DXF 뷰어 배경 이미지와 일치시키기 위해)
    # DXF 뷰어의 insert_background_image는 이미지를 Y가 위로 증가하는 좌표계에 맞춰 표시
    # 따라서 벡터화된 선도 동일하게 처리해야 배경과 일치함
    lines_pixel = []
    for line in vectorizer.lines:
        # 픽셀 좌표 그대로 저장 (이미지 좌상단 = (0,0), 우하단 = (width, height))
        lines_pixel.append(Line(
            start=Point(line.start.x, line.start.y, 0),
            end=Point(line.end.x, line.end.y, 0),
            layer=options.get('layer', 'PIXEL_TRACE')
        ))

    # 3. DXF 저장
    layer = options.get('layer', 'PIXEL_TRACE')
    result = write_lines_to_dxf(lines_pixel, output_dxf, layer)

    return {
        'success': True,
        'lines': len(lines_pixel),
        'image_size': [width, height],
        'transform_method': 'pixel',
        'note': '픽셀 좌표 그대로 저장됨. 바닥 사각형을 그린 후 transform 명령으로 변환 가능.',
        **result
    }


def transform_dxf_with_floor(
    input_dxf: str,
    output_dxf: str,
    floor_corners: list,
    span_mm: float,
    height_mm: float = None,
    image_height: int = None
) -> dict:
    """
    기존 DXF의 모든 엔티티를 바닥면 Homography로 변환

    바닥 4점 좌표와 실제 치수를 기반으로 전체 도면을 변환합니다.

    Args:
        input_dxf: 입력 DXF 파일 경로 (픽셀 좌표)
        output_dxf: 출력 DXF 파일 경로 (실제 좌표)
        floor_corners: 바닥 4점 좌표 [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
                       순서: 좌하단 → 우하단 → 우상단 → 좌상단 (반시계방향)
        span_mm: 가로 실제 길이 (mm)
        height_mm: 세로 실제 길이 (mm), None이면 자동 계산
        image_height: 원본 이미지 높이 (Y축 반전 보정용)

    Returns:
        결과 딕셔너리
    """
    try:
        import cv2
        import numpy as np
    except ImportError:
        return {'success': False, 'error': 'OpenCV required'}

    import os
    if not os.path.exists(input_dxf):
        return {'success': False, 'error': f'Input DXF not found: {input_dxf}'}

    # 1. DXF 파일에서 LINE 엔티티 읽기
    lines = read_lines_from_dxf(input_dxf)
    if not lines:
        return {'success': False, 'error': 'No lines found in DXF'}

    print(f"Read {len(lines)} lines from {input_dxf}")

    # 2. Homography 계산
    # floor_corners: 바닥 4점 (DXF 좌표계, Y는 위로)
    # 순서: 좌하단(A) → 우하단(B) → 우상단(C) → 좌상단(D)
    A, B, C, D = [np.array(p, dtype=np.float64) for p in floor_corners]
    L = float(span_mm)

    if height_mm is not None:
        Ly = float(height_mm)
    else:
        # 자동 종횡비 계산: AB(가로) 대 AD(세로) 비율
        Ly = L * (np.linalg.norm(D - A) / np.linalg.norm(B - A))

    # 소스: DXF 좌표 (픽셀)
    src = np.array([A, B, C, D], dtype=np.float64)
    # 목적지: 실제 좌표 (mm)
    # 좌하단 = (0, 0), 우하단 = (L, 0), 우상단 = (L, Ly), 좌상단 = (0, Ly)
    dst = np.array([[0, 0], [L, 0], [L, Ly], [0, Ly]], dtype=np.float64)

    H, _ = cv2.findHomography(src, dst, method=0)
    if H is None:
        return {'success': False, 'error': 'Homography calculation failed'}

    print(f"Homography calculated: {L:.0f} x {Ly:.0f} mm")

    # 3. 모든 선 변환
    # 바닥 영역 크기의 배수를 허용 범위로 설정
    max_coord = max(L, Ly) * 3  # 바닥 크기의 3배까지 허용

    # 바닥 영역의 Y 범위 계산 (소스 좌표에서)
    src_ys = [A[1], B[1], C[1], D[1]]
    src_y_min = min(src_ys)  # 바닥 뒤쪽 (먼 곳)
    src_y_max = max(src_ys)  # 바닥 앞쪽 (가까운 곳)

    # 바닥 범위를 약간 확장 (바닥 영역 + 여유)
    y_margin = (src_y_max - src_y_min) * 0.5
    allowed_y_min = src_y_min - y_margin
    allowed_y_max = src_y_max + y_margin

    print(f"Source Y range: {src_y_min:.0f} ~ {src_y_max:.0f} (allowed: {allowed_y_min:.0f} ~ {allowed_y_max:.0f})")

    def apply_H(H, point):
        # 소스 좌표가 바닥 영역 근처인지 먼저 확인
        if point[1] < allowed_y_min or point[1] > allowed_y_max:
            return None

        p = np.array([point[0], point[1], 1.0])
        p_t = H @ p
        # w가 양수이고 충분히 커야 함 (음수면 소실점 뒤쪽)
        if p_t[2] < 0.1:
            return None
        result = [p_t[0] / p_t[2], p_t[1] / p_t[2]]
        # 결과가 합리적인 범위인지 확인
        if abs(result[0]) > max_coord or abs(result[1]) > max_coord:
            return None
        return result

    lines_transformed = []
    skipped = 0
    for line in lines:
        p1 = apply_H(H, [line['start']['x'], line['start']['y']])
        p2 = apply_H(H, [line['end']['x'], line['end']['y']])

        if p1 and p2:
            lines_transformed.append(Line(
                start=Point(p1[0], p1[1], 0),
                end=Point(p2[0], p2[1], 0),
                layer='FLOOR_MM'
            ))
        else:
            skipped += 1

    if skipped > 0:
        print(f"Skipped {skipped} lines (out of bounds)")

    print(f"Transformed {len(lines_transformed)} lines")

    # 4. DXF 저장
    result = write_lines_to_dxf(lines_transformed, output_dxf, 'FLOOR_MM')

    return {
        'success': True,
        'lines_input': len(lines),
        'lines_output': len(lines_transformed),
        'floor_size_mm': [L, Ly],
        'H_matrix': H.tolist(),
        **result
    }


def read_lines_from_dxf(dxf_path: str) -> list:
    """
    DXF 파일에서 LINE 엔티티 읽기

    Args:
        dxf_path: DXF 파일 경로

    Returns:
        선 리스트 [{'start': {'x':, 'y':, 'z':}, 'end': {...}, 'layer': ...}, ...]
    """
    with open(dxf_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    lines = []
    import re

    # LINE 엔티티 패턴
    # 간단한 파서: LINE 블록을 찾아서 좌표 추출
    line_pattern = r'  0\nLINE\n(.*?)(?=  0\n[A-Z]|\nENDSEC)'
    line_blocks = re.findall(line_pattern, content, re.DOTALL)

    for block in line_blocks:
        line_data = {'start': {}, 'end': {}, 'layer': '0'}

        # 레이어
        layer_match = re.search(r'  8\n([^\n]+)', block)
        if layer_match:
            line_data['layer'] = layer_match.group(1).strip()

        # 시작점
        x1_match = re.search(r' 10\n([^\n]+)', block)
        y1_match = re.search(r' 20\n([^\n]+)', block)
        z1_match = re.search(r' 30\n([^\n]+)', block)

        # 끝점
        x2_match = re.search(r' 11\n([^\n]+)', block)
        y2_match = re.search(r' 21\n([^\n]+)', block)
        z2_match = re.search(r' 31\n([^\n]+)', block)

        if x1_match and y1_match and x2_match and y2_match:
            line_data['start']['x'] = float(x1_match.group(1))
            line_data['start']['y'] = float(y1_match.group(1))
            line_data['start']['z'] = float(z1_match.group(1)) if z1_match else 0.0

            line_data['end']['x'] = float(x2_match.group(1))
            line_data['end']['y'] = float(y2_match.group(1))
            line_data['end']['z'] = float(z2_match.group(1)) if z2_match else 0.0

            lines.append(line_data)

    return lines


def vectorize_with_homography(
    image_path: str,
    output_dxf: str,
    corners: list,
    span_mm: float,
    height_mm: float = None,
    options: dict = None
) -> dict:
    """
    Homography 기반 2D 벡터화 (Z=0 평면)

    4점 대응으로 평면 변환 행렬을 계산합니다.

    Args:
        image_path: 입력 이미지 경로
        output_dxf: 출력 DXF 경로
        corners: 4개 모서리 픽셀 좌표 [A, B, C, D] (시계방향, 좌상단부터)
        span_mm: 수평 스팬 (mm)
        height_mm: 수직 높이 (mm), None이면 자동 계산
        options: 벡터화 옵션

    Returns:
        결과 딕셔너리
    """
    if options is None:
        options = {}

    try:
        import cv2
        import numpy as np
    except ImportError:
        return {'success': False, 'error': 'OpenCV required'}

    # 1. 이미지 벡터화 (픽셀 좌표)
    vectorizer = ImageVectorizer()
    vectorizer.mode = options.get('mode', 'edge')
    vectorizer.edge_threshold = options.get('edge_threshold', 40)
    vectorizer.simplify_epsilon = options.get('epsilon', 2.0)

    if not vectorizer.load_image(image_path):
        return {'success': False, 'error': 'Failed to load image'}

    width = vectorizer.binary_image.width
    height = vectorizer.binary_image.height

    vectorizer.set_output_bounds(0, 0, width, height)
    vectorizer.vectorize()

    if not vectorizer.lines:
        return {'success': False, 'error': 'No lines extracted'}

    print(f"Extracted {len(vectorizer.lines)} lines from image ({width}x{height})")

    # 2. Homography 계산
    A, B, C, D = [np.array(p, dtype=np.float64) for p in corners]
    L = float(span_mm)

    if height_mm is not None:
        Ly = float(height_mm)
    else:
        # 자동 종횡비 계산
        Ly = L * (np.linalg.norm(D - A) / np.linalg.norm(B - A))

    src = np.array([A, B, C, D], dtype=np.float64)
    dst = np.array([[0, 0], [L, 0], [L, Ly], [0, Ly]], dtype=np.float64)

    H, _ = cv2.findHomography(src, dst, method=0)
    if H is None:
        return {'success': False, 'error': 'Homography calculation failed'}

    print(f"Homography calculated: {L:.0f} x {Ly:.0f} mm")

    # 3. 3D 변환기 설정
    transformer = Transform3D()
    transformer.setup_homography(H.tolist(), plane_z=0)

    # 4. 각 선을 평면 좌표로 변환
    lines_3d = []
    for line in vectorizer.lines:
        p1_3d = transformer.pixel_to_world(line.start.x, line.start.y)
        p2_3d = transformer.pixel_to_world(line.end.x, line.end.y)

        if p1_3d and p2_3d:
            lines_3d.append(Line(
                start=Point(p1_3d.x, p1_3d.y, p1_3d.z),
                end=Point(p2_3d.x, p2_3d.y, p2_3d.z),
                layer=options.get('layer', 'TRACE_3D')
            ))

    print(f"Transformed {len(lines_3d)} lines")

    # 5. DXF 저장
    layer = options.get('layer', 'TRACE_3D')
    result = write_lines_to_dxf(lines_3d, output_dxf, layer)

    return {
        'success': True,
        'lines_2d': len(vectorizer.lines),
        'lines_3d': len(lines_3d),
        'image_size': [width, height],
        'transform_method': 'homography',
        'plane_size_mm': [L, Ly],
        'H_matrix': H.tolist(),
        **result
    }


# ============ CLI ============

def print_usage():
    print("""
3D Vectorization Script

Usage:
    # [1단계] 픽셀 좌표 그대로 벡터화 (권장 시작점)
    python scripts/vectorize_3d.py pixel <image_path> <output.dxf> [options_json]

    # [2단계] 바닥 사각형으로 변환 (DXF에서 바닥 4점 좌표 추출 후)
    python scripts/vectorize_3d.py transform <input.dxf> <output.dxf> <floor_corners.json> <span_mm> [height_mm]

    # 직접 Homography 벡터화 (4점을 미리 알 때)
    python scripts/vectorize_3d.py homography <image_path> <output.dxf> <corners.json> <span_mm> [height_mm]

    # 기타 방법
    python scripts/vectorize_3d.py depth <image_path> <output.dxf> [options_json]
    python scripts/vectorize_3d.py pnp <image_path> <output.dxf> <points.json>

Methods:
    pixel       - 픽셀 좌표 그대로 저장 (1단계: 먼저 실행)
    transform   - 바닥 4점으로 기존 DXF 변환 (2단계: 바닥 지정 후)
    homography  - Homography 기반 직접 변환 (4점 필요)
    depth       - 깊이 추정 기반 (간이 3D, 비권장)
    pnp         - PnP 기반 (2D-3D 대응점 필요)

워크플로우 예시:
    1. pixel로 벡터화: python scripts/vectorize_3d.py pixel image.jpg trace.dxf
    2. VS Code에서 trace.dxf 열기
    3. 바닥 영역에 사각형 그리기 (create_rectangle 또는 create_polyline)
    4. 사각형의 4점 좌표 확인 (get_selected_entities)
    5. transform으로 변환: python scripts/vectorize_3d.py transform trace.dxf floor.dxf '[[x1,y1],[x2,y2],[x3,y3],[x4,y4]]' 10000

Floor Corners JSON:
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    순서: 좌하단 → 우하단 → 우상단 → 좌상단 (반시계방향)

Options JSON:
    {
        "mode": "edge",
        "edge_threshold": 40,
        "epsilon": 2.0,
        "min_length": 10,
        "layer": "TRACE"
    }
""")


def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    method = sys.argv[1]

    # ========== pixel: 픽셀 좌표 그대로 벡터화 ==========
    if method == 'pixel':
        if len(sys.argv) < 4:
            print("Usage: python scripts/vectorize_3d.py pixel <image_path> <output.dxf> [options_json]")
            return
        image_path = sys.argv[2]
        output_dxf = sys.argv[3]
        options = {}
        if len(sys.argv) > 4:
            opt_arg = sys.argv[4]
            options = json.loads(opt_arg) if opt_arg.startswith('{') else json.load(open(opt_arg))

        result = vectorize_pixel_coords(image_path, output_dxf, options)

    # ========== transform: 바닥 4점으로 DXF 변환 ==========
    elif method == 'transform':
        if len(sys.argv) < 6:
            print("Usage: python scripts/vectorize_3d.py transform <input.dxf> <output.dxf> <floor_corners.json> <span_mm> [height_mm]")
            return
        input_dxf = sys.argv[2]
        output_dxf = sys.argv[3]
        corners_arg = sys.argv[4]
        corners = json.loads(corners_arg) if corners_arg.startswith('[') else json.load(open(corners_arg))
        span_mm = float(sys.argv[5])
        height_mm = float(sys.argv[6]) if len(sys.argv) > 6 and sys.argv[6].replace('.','').isdigit() else None

        result = transform_dxf_with_floor(input_dxf, output_dxf, corners, span_mm, height_mm)

    # ========== depth: 깊이 추정 기반 ==========
    elif method == 'depth':
        if len(sys.argv) < 4:
            print("Usage: python scripts/vectorize_3d.py depth <image_path> <output.dxf> [options_json]")
            return
        image_path = sys.argv[2]
        output_dxf = sys.argv[3]
        options = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
        result = vectorize_with_depth_estimation(
            image_path, output_dxf,
            horizon_ratio=options.get('horizon_ratio', 0.35),
            camera_height_mm=options.get('camera_height_mm', 1600),
            near_depth_mm=options.get('near_depth_mm', 2000),
            far_depth_mm=options.get('far_depth_mm', 30000),
            options=options
        )

    # ========== pnp: PnP 기반 ==========
    elif method == 'pnp':
        if len(sys.argv) < 5:
            print("Usage: python scripts/vectorize_3d.py pnp <image_path> <output.dxf> <points.json>")
            return
        image_path = sys.argv[2]
        output_dxf = sys.argv[3]
        points_data = json.loads(sys.argv[4]) if sys.argv[4].startswith('{') else json.load(open(sys.argv[4]))
        options = json.loads(sys.argv[5]) if len(sys.argv) > 5 else {}

        result = vectorize_with_pnp(
            image_path, output_dxf,
            points_2d=points_data['points_2d'],
            points_3d=points_data['points_3d'],
            planes=points_data.get('planes', {'floor': {'z': 0}}),
            options=options
        )

    # ========== homography: Homography 기반 직접 변환 ==========
    elif method == 'homography':
        if len(sys.argv) < 6:
            print("Usage: python scripts/vectorize_3d.py homography <image_path> <output.dxf> <corners.json> <span_mm> [height_mm]")
            return
        image_path = sys.argv[2]
        output_dxf = sys.argv[3]
        corners = json.loads(sys.argv[4]) if sys.argv[4].startswith('[') else json.load(open(sys.argv[4]))
        span_mm = float(sys.argv[5])
        height_mm = float(sys.argv[6]) if len(sys.argv) > 6 and sys.argv[6].replace('.','').isdigit() else None
        options = json.loads(sys.argv[7]) if len(sys.argv) > 7 else {}

        result = vectorize_with_homography(
            image_path, output_dxf,
            corners=corners,
            span_mm=span_mm,
            height_mm=height_mm,
            options=options
        )

    else:
        print(f"Unknown method: {method}")
        print_usage()
        return

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

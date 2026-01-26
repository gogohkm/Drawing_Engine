"""
Vectorize Module - 이미지 벡터화 및 선 정리 (3D 좌표 지원)

기존 모듈:
- image_vectorizer: 이미지→선 벡터화 (순수 Python, OpenCV 불필요)
- line_cleaner: 벡터화 후처리 (중심선 추출, 병합, 중복 제거)

신규 모듈 (Phase 2, 4):
- line_extractor: Canny + HoughLinesP 기반 자동 선 추출 (OpenCV 필요)
- transform_3d: 픽셀→3D 변환 (다중 평면 지원)

Note: Line2D, Point2D는 Line3D, Point3D로 변경됨 (v2.0)
"""
from .image_vectorizer import ImageVectorizer, BinaryImage, GrayscaleImage, Point, Line, write_lines_to_dxf
from .line_cleaner import LineCleaner, Line3D, Point3D as CleanerPoint3D

# 신규 모듈 (OpenCV 의존성)
try:
    from .line_extractor import LineExtractor, ContourExtractor, StructuralElements
    from .line_extractor import Line3D as ExtractedLine3D, LineGroup
    HAS_LINE_EXTRACTOR = True
except ImportError:
    HAS_LINE_EXTRACTOR = False
    LineExtractor = None
    ContourExtractor = None
    StructuralElements = None
    ExtractedLine3D = None
    LineGroup = None

try:
    from .transform_3d import Transform3D, PnPCalibrator, Plane, Point3D
    HAS_TRANSFORM_3D = True
except ImportError:
    HAS_TRANSFORM_3D = False
    Transform3D = None
    PnPCalibrator = None
    Plane = None
    Point3D = None

__all__ = [
    # 기존 API
    'ImageVectorizer', 'BinaryImage', 'GrayscaleImage', 'Point', 'Line', 'write_lines_to_dxf',
    'LineCleaner', 'Line3D', 'CleanerPoint3D',
    # 신규 API (가용 여부 확인 필요)
    'LineExtractor', 'ContourExtractor', 'StructuralElements', 'ExtractedLine3D', 'LineGroup',
    'Transform3D', 'PnPCalibrator', 'Plane', 'Point3D',
    # 가용성 플래그
    'HAS_LINE_EXTRACTOR', 'HAS_TRANSFORM_3D',
]

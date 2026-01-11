"""
Common Types and Utilities
==========================
공통으로 사용되는 데이터 타입과 유틸리티 함수들.
모든 엔진 모듈에서 이 파일을 임포트하여 중복을 제거합니다.
"""

import math
from typing import Tuple, Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum


# ========== 기본 데이터 타입 ==========

@dataclass
class Point2D:
    """2D 좌표점"""
    x: float
    y: float

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def to_dict(self) -> Dict[str, float]:
        return {"x": self.x, "y": self.y}

    def distance_to(self, other: 'Point2D') -> float:
        """다른 점까지의 거리"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

    def scale(self, factor: float) -> 'Point2D':
        return Point2D(self.x * factor, self.y * factor)


@dataclass
class Point3D:
    """3D 좌표점"""
    x: float
    y: float
    z: float

    def to_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def to_dict(self) -> Dict[str, float]:
        return {"x": self.x, "y": self.y, "z": self.z}

    def __add__(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def scale(self, factor: float) -> 'Point3D':
        return Point3D(self.x * factor, self.y * factor, self.z * factor)


# ========== 작업 상태 ==========

class TaskStatus(Enum):
    """작업 상태 - context_manager와 drawing_engine에서 공통 사용"""
    PENDING = "pending"
    PLANNING = "planning"
    READY = "ready"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"
    SUCCESS = "success"  # drawing_engine 호환
    FAILED = "failed"


# ========== MCP 도구 호출 생성 ==========

class MCPToolGenerator:
    """MCP 도구 호출 생성 유틸리티"""

    TOOL_PREFIX = "mcp__stgen-dxf-viewer__"

    @classmethod
    def create_line(cls, start: Dict, end: Dict, layer: str = "0", color: int = None) -> Dict:
        """LINE 엔티티 생성 명령"""
        cmd = {
            "tool": f"{cls.TOOL_PREFIX}create_line",
            "args": {
                "start": start,
                "end": end,
                "layer": layer
            }
        }
        if color is not None:
            cmd["args"]["color"] = color
        return cmd

    @classmethod
    def create_circle(cls, center: Dict, radius: float, layer: str = "0", color: int = None) -> Dict:
        """CIRCLE 엔티티 생성 명령"""
        cmd = {
            "tool": f"{cls.TOOL_PREFIX}create_circle",
            "args": {
                "center": center,
                "radius": radius,
                "layer": layer
            }
        }
        if color is not None:
            cmd["args"]["color"] = color
        return cmd

    @classmethod
    def create_arc(cls, center: Dict, radius: float, start_angle: float,
                   end_angle: float, layer: str = "0", color: int = None) -> Dict:
        """ARC 엔티티 생성 명령"""
        cmd = {
            "tool": f"{cls.TOOL_PREFIX}create_arc",
            "args": {
                "center": center,
                "radius": radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "layer": layer
            }
        }
        if color is not None:
            cmd["args"]["color"] = color
        return cmd

    @classmethod
    def create_text(cls, position: Dict, text: str, height: float = 2.5,
                    rotation: float = 0, layer: str = "0", color: int = None) -> Dict:
        """TEXT 엔티티 생성 명령"""
        cmd = {
            "tool": f"{cls.TOOL_PREFIX}create_text",
            "args": {
                "position": position,
                "text": text,
                "height": height,
                "rotation": rotation,
                "layer": layer
            }
        }
        if color is not None:
            cmd["args"]["color"] = color
        return cmd

    @classmethod
    def create_polyline(cls, vertices: List[Dict], closed: bool = False,
                        layer: str = "0", color: int = None) -> Dict:
        """POLYLINE 엔티티 생성 명령"""
        cmd = {
            "tool": f"{cls.TOOL_PREFIX}create_polyline",
            "args": {
                "vertices": vertices,
                "closed": closed,
                "layer": layer
            }
        }
        if color is not None:
            cmd["args"]["color"] = color
        return cmd

    @classmethod
    def create_layer(cls, name: str, color: int = 7) -> Dict:
        """레이어 생성 명령"""
        return {
            "tool": f"{cls.TOOL_PREFIX}create_layer",
            "args": {
                "name": name,
                "color": color
            }
        }

    @classmethod
    def set_current_layer(cls, name: str) -> Dict:
        """현재 레이어 설정 명령"""
        return {
            "tool": f"{cls.TOOL_PREFIX}set_current_layer",
            "args": {"name": name}
        }

    @classmethod
    def entity_to_mcp_call(cls, entity: Dict, layer: str = None) -> Optional[Dict]:
        """
        엔티티 딕셔너리를 MCP 도구 호출로 변환

        Args:
            entity: 엔티티 데이터 (type, start/end, center, etc.)
            layer: 대상 레이어 (없으면 원본 사용)

        Returns:
            MCP 도구 호출 딕셔너리 또는 None
        """
        entity_type = entity.get('type', '')
        target_layer = layer or entity.get('layer', '0')

        if entity_type == 'LINE':
            return cls.create_line(
                entity.get('start', {}),
                entity.get('end', {}),
                target_layer
            )
        elif entity_type == 'CIRCLE':
            return cls.create_circle(
                entity.get('center', {}),
                entity.get('radius', 1),
                target_layer
            )
        elif entity_type == 'ARC':
            return cls.create_arc(
                entity.get('center', {}),
                entity.get('radius', 1),
                entity.get('startAngle', 0),
                entity.get('endAngle', 360),
                target_layer
            )
        elif entity_type == 'TEXT':
            return cls.create_text(
                entity.get('position', {}),
                entity.get('text', ''),
                entity.get('height', 2.5),
                entity.get('rotation', 0),
                target_layer
            )
        elif entity_type == 'LWPOLYLINE':
            return cls.create_polyline(
                entity.get('vertices', []),
                entity.get('closed', False),
                target_layer
            )

        return None


# ========== 유틸리티 함수 ==========

def calculate_distance(p1: Dict, p2: Dict) -> float:
    """두 점 사이의 거리 계산"""
    dx = p2.get('x', 0) - p1.get('x', 0)
    dy = p2.get('y', 0) - p1.get('y', 0)
    return math.sqrt(dx * dx + dy * dy)


def normalize_angle(angle: float) -> float:
    """각도를 0-360 범위로 정규화"""
    while angle < 0:
        angle += 360
    while angle >= 360:
        angle -= 360
    return angle


def calculate_line_angle(start: Dict, end: Dict) -> float:
    """라인의 각도 계산 (degrees)"""
    dx = end.get('x', 0) - start.get('x', 0)
    dy = end.get('y', 0) - start.get('y', 0)
    return math.degrees(math.atan2(dy, dx))

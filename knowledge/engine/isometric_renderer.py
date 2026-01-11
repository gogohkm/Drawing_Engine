"""
Isometric Renderer Module
========================
3D to 2D projection for steel structure drawings.
Converts 3D coordinates to isometric view for accurate representation of reference photos.

Phase 1: Basic isometric projection
Phase 2: Steel section patterns (H-beam, C-channel)
Phase 3: Array functions for repeated elements
"""

import math
from typing import List, Tuple, Dict, Optional, Any
from dataclasses import dataclass, field

# 공통 타입 임포트
try:
    from common import Point2D, Point3D
except ImportError:
    # 독립 실행 시 로컬 정의 사용
    @dataclass
    class Point3D:
        """3D point representation"""
        x: float
        y: float
        z: float

        def to_tuple(self) -> Tuple[float, float, float]:
            return (self.x, self.y, self.z)

        def __add__(self, other: 'Point3D') -> 'Point3D':
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

        def __sub__(self, other: 'Point3D') -> 'Point3D':
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

        def scale(self, factor: float) -> 'Point3D':
            return Point3D(self.x * factor, self.y * factor, self.z * factor)

    @dataclass
    class Point2D:
        """2D point representation"""
        x: float
        y: float

        def to_tuple(self) -> Tuple[float, float]:
            return (self.x, self.y)


@dataclass
class Line3D:
    """3D line representation"""
    start: Point3D
    end: Point3D
    layer: str = "0"
    color: Optional[int] = None


@dataclass
class SteelSection:
    """Steel section properties"""
    type: str  # "H", "C", "L", "BOX", "PIPE"
    height: float  # 전고 (total height)
    width: float   # 플랜지 폭 (flange width)
    web_thickness: float = 0
    flange_thickness: float = 0

    @classmethod
    def h_beam(cls, height: float, width: float, web_t: float = None, flange_t: float = None):
        """Create H-beam section"""
        web_t = web_t or height * 0.06
        flange_t = flange_t or height * 0.1
        return cls("H", height, width, web_t, flange_t)

    @classmethod
    def c_channel(cls, height: float, width: float, web_t: float = None, flange_t: float = None):
        """Create C-channel section"""
        web_t = web_t or height * 0.08
        flange_t = flange_t or height * 0.1
        return cls("C", height, width, web_t, flange_t)


class IsometricRenderer:
    """
    Isometric Projection Renderer

    Converts 3D coordinates to 2D isometric view.
    Standard isometric angle: 30 degrees

    Coordinate System:
    - X: Left-Right (horizontal in 2D, going right-down in isometric)
    - Y: Up-Down (vertical in both 2D and isometric)
    - Z: Front-Back (depth, going right-up in isometric)
    """

    def __init__(self, angle: float = 30, scale: float = 1.0, origin: Point2D = None):
        """
        Initialize isometric renderer.

        Args:
            angle: Isometric angle in degrees (default: 30)
            scale: Drawing scale factor
            origin: 2D origin point for the drawing
        """
        self.angle = angle
        self.scale = scale
        self.origin = origin or Point2D(0, 0)

        # Pre-calculate trigonometric values
        self.cos_a = math.cos(math.radians(angle))
        self.sin_a = math.sin(math.radians(angle))

        # Store generated commands for batch execution
        self.commands: List[Dict[str, Any]] = []

    def project_3d_to_2d(self, point: Point3D) -> Point2D:
        """
        Project 3D point to 2D isometric coordinates.

        Isometric projection formula:
        x_2d = x * cos(angle) - z * cos(angle)
        y_2d = y + x * sin(angle) + z * sin(angle)

        Args:
            point: 3D point to project

        Returns:
            2D point in isometric view
        """
        x_2d = (point.x * self.cos_a - point.z * self.cos_a) * self.scale + self.origin.x
        y_2d = (point.y + point.x * self.sin_a + point.z * self.sin_a) * self.scale + self.origin.y
        return Point2D(x_2d, y_2d)

    def project_point(self, x: float, y: float, z: float) -> Tuple[float, float]:
        """Convenience method for direct coordinate projection."""
        p2d = self.project_3d_to_2d(Point3D(x, y, z))
        return p2d.to_tuple()

    def clear_commands(self):
        """Clear stored commands."""
        self.commands = []

    def add_line_3d(self, start: Point3D, end: Point3D, layer: str = "0", color: int = None):
        """
        Add a 3D line to be drawn in isometric view.

        Args:
            start: Start point in 3D
            end: End point in 3D
            layer: DXF layer name
            color: AutoCAD color index (optional)
        """
        p1 = self.project_3d_to_2d(start)
        p2 = self.project_3d_to_2d(end)

        cmd = {
            "type": "line",
            "start": {"x": p1.x, "y": p1.y},
            "end": {"x": p2.x, "y": p2.y},
            "layer": layer
        }
        if color:
            cmd["color"] = color

        self.commands.append(cmd)

    def add_line(self, x1: float, y1: float, z1: float,
                 x2: float, y2: float, z2: float,
                 layer: str = "0", color: int = None):
        """Convenience method to add line with raw coordinates."""
        self.add_line_3d(Point3D(x1, y1, z1), Point3D(x2, y2, z2), layer, color)

    # ===========================================
    # Phase 2: Steel Section Patterns
    # ===========================================

    def draw_h_beam_segment(self, start: Point3D, end: Point3D,
                            section: SteelSection, layer: str = "COLUMN"):
        """
        Draw H-beam segment in 3D isometric view.

        H-beam is represented with lines showing:
        - Two flanges (top and bottom)
        - Web (center)
        - Visible edges based on viewing direction

        Args:
            start: Start point of beam centerline
            end: End point of beam centerline
            section: SteelSection with H-beam properties
            layer: DXF layer name
        """
        if section.type != "H":
            raise ValueError("Section must be H-beam type")

        h = section.height
        w = section.width
        ft = section.flange_thickness
        wt = section.web_thickness

        # Calculate beam direction vector
        dx = end.x - start.x
        dy = end.y - start.y
        dz = end.z - start.z
        length = math.sqrt(dx*dx + dy*dy + dz*dz)

        if length == 0:
            return

        # Determine beam orientation
        is_vertical = abs(dy) > max(abs(dx), abs(dz)) * 0.9
        is_horizontal_x = abs(dx) > max(abs(dy), abs(dz)) * 0.9
        is_horizontal_z = abs(dz) > max(abs(dx), abs(dy)) * 0.9

        if is_vertical:
            # Vertical column - show H-section profile
            # Flanges are perpendicular to Z axis
            self._draw_vertical_h_beam(start, end, section, layer)
        elif is_horizontal_x:
            # Horizontal beam along X axis
            self._draw_horizontal_x_h_beam(start, end, section, layer)
        elif is_horizontal_z:
            # Horizontal beam along Z axis (depth direction)
            self._draw_horizontal_z_h_beam(start, end, section, layer)
        else:
            # Angled beam (rafter)
            self._draw_angled_h_beam(start, end, section, layer)

    def _draw_vertical_h_beam(self, start: Point3D, end: Point3D,
                               section: SteelSection, layer: str):
        """Draw vertical H-beam (column)."""
        h = section.height
        w = section.width
        ft = section.flange_thickness
        wt = section.web_thickness

        # Half dimensions
        hw = w / 2
        hh = h / 2
        hwt = wt / 2

        # Bottom point (start) - draw H-section edges
        # Left flange outer
        self.add_line(start.x - hw, start.y, start.z - hh,
                      end.x - hw, end.y, end.z - hh, layer)
        # Left flange inner
        self.add_line(start.x - hw, start.y, start.z + hh,
                      end.x - hw, end.y, end.z + hh, layer)
        # Right flange outer
        self.add_line(start.x + hw, start.y, start.z - hh,
                      end.x + hw, end.y, end.z - hh, layer)
        # Right flange inner
        self.add_line(start.x + hw, start.y, start.z + hh,
                      end.x + hw, end.y, end.z + hh, layer)

        # Top and bottom caps (flange lines)
        # Bottom cap
        self.add_line(start.x - hw, start.y, start.z - hh,
                      start.x + hw, start.y, start.z - hh, layer)
        self.add_line(start.x - hw, start.y, start.z + hh,
                      start.x + hw, start.y, start.z + hh, layer)
        # Connect flanges at bottom
        self.add_line(start.x - hw, start.y, start.z - hh,
                      start.x - hw, start.y, start.z + hh, layer)
        self.add_line(start.x + hw, start.y, start.z - hh,
                      start.x + hw, start.y, start.z + hh, layer)

        # Top cap
        self.add_line(end.x - hw, end.y, end.z - hh,
                      end.x + hw, end.y, end.z - hh, layer)
        self.add_line(end.x - hw, end.y, end.z + hh,
                      end.x + hw, end.y, end.z + hh, layer)
        # Connect flanges at top
        self.add_line(end.x - hw, end.y, end.z - hh,
                      end.x - hw, end.y, end.z + hh, layer)
        self.add_line(end.x + hw, end.y, end.z - hh,
                      end.x + hw, end.y, end.z + hh, layer)

    def _draw_horizontal_x_h_beam(self, start: Point3D, end: Point3D,
                                   section: SteelSection, layer: str):
        """Draw horizontal H-beam along X axis."""
        h = section.height
        w = section.width
        hh = h / 2
        hw = w / 2

        # Top flange
        self.add_line(start.x, start.y + hh, start.z - hw,
                      end.x, end.y + hh, end.z - hw, layer)
        self.add_line(start.x, start.y + hh, start.z + hw,
                      end.x, end.y + hh, end.z + hw, layer)

        # Bottom flange
        self.add_line(start.x, start.y - hh, start.z - hw,
                      end.x, end.y - hh, end.z - hw, layer)
        self.add_line(start.x, start.y - hh, start.z + hw,
                      end.x, end.y - hh, end.z + hw, layer)

        # Web (center line for visibility)
        self.add_line(start.x, start.y + hh, start.z,
                      end.x, end.y + hh, end.z, layer)
        self.add_line(start.x, start.y - hh, start.z,
                      end.x, end.y - hh, end.z, layer)

        # End caps
        self._draw_h_section_cap(start, section, layer, face='start')
        self._draw_h_section_cap(end, section, layer, face='end')

    def _draw_horizontal_z_h_beam(self, start: Point3D, end: Point3D,
                                   section: SteelSection, layer: str):
        """Draw horizontal H-beam along Z axis (depth direction)."""
        h = section.height
        w = section.width
        hh = h / 2
        hw = w / 2

        # For Z-direction beam, flanges are in XY plane
        # Top flange lines
        self.add_line(start.x - hw, start.y + hh, start.z,
                      end.x - hw, end.y + hh, end.z, layer)
        self.add_line(start.x + hw, start.y + hh, start.z,
                      end.x + hw, end.y + hh, end.z, layer)

        # Bottom flange lines
        self.add_line(start.x - hw, start.y - hh, start.z,
                      end.x - hw, end.y - hh, end.z, layer)
        self.add_line(start.x + hw, start.y - hh, start.z,
                      end.x + hw, end.y - hh, end.z, layer)

    def _draw_angled_h_beam(self, start: Point3D, end: Point3D,
                            section: SteelSection, layer: str):
        """Draw angled H-beam (like a rafter)."""
        h = section.height
        w = section.width
        hh = h / 2
        hw = w / 2

        # Calculate perpendicular offset for flanges
        dx = end.x - start.x
        dy = end.y - start.y
        dz = end.z - start.z
        length = math.sqrt(dx*dx + dy*dy + dz*dz)

        # Normalize direction
        dx, dy, dz = dx/length, dy/length, dz/length

        # For rafters mainly in XY plane, offset in Z for width
        # Top flange (offset up perpendicular to beam direction)
        # Simplified: offset Y by height/2
        self.add_line(start.x, start.y + hh, start.z - hw,
                      end.x, end.y + hh, end.z - hw, layer)
        self.add_line(start.x, start.y + hh, start.z + hw,
                      end.x, end.y + hh, end.z + hw, layer)

        # Bottom flange
        self.add_line(start.x, start.y - hh, start.z - hw,
                      end.x, end.y - hh, end.z - hw, layer)
        self.add_line(start.x, start.y - hh, start.z + hw,
                      end.x, end.y - hh, end.z + hw, layer)

    def _draw_h_section_cap(self, point: Point3D, section: SteelSection,
                            layer: str, face: str = 'start'):
        """Draw H-section end cap at a point."""
        h = section.height
        w = section.width
        hh = h / 2
        hw = w / 2

        # Draw H shape
        # Top flange
        self.add_line(point.x, point.y + hh, point.z - hw,
                      point.x, point.y + hh, point.z + hw, layer)
        # Bottom flange
        self.add_line(point.x, point.y - hh, point.z - hw,
                      point.x, point.y - hh, point.z + hw, layer)
        # Left edge
        self.add_line(point.x, point.y + hh, point.z - hw,
                      point.x, point.y - hh, point.z - hw, layer)
        # Right edge
        self.add_line(point.x, point.y + hh, point.z + hw,
                      point.x, point.y - hh, point.z + hw, layer)

    def draw_c_channel_segment(self, start: Point3D, end: Point3D,
                               section: SteelSection, layer: str = "PURLIN"):
        """
        Draw C-channel segment in 3D isometric view.

        C-channel shows:
        - Web (back plate)
        - Two flanges (top and bottom lips)

        Args:
            start: Start point of channel centerline
            end: End point of channel centerline
            section: SteelSection with C-channel properties
            layer: DXF layer name
        """
        h = section.height
        w = section.width
        hh = h / 2

        # C-channel: web on back, flanges pointing forward
        # Web line (back)
        self.add_line(start.x, start.y + hh, start.z,
                      end.x, end.y + hh, end.z, layer)
        self.add_line(start.x, start.y - hh, start.z,
                      end.x, end.y - hh, end.z, layer)

        # Top flange
        self.add_line(start.x, start.y + hh, start.z,
                      end.x, end.y + hh, end.z + w, layer)
        # Actually draw lip extending forward
        self.add_line(start.x, start.y + hh, start.z + w,
                      end.x, end.y + hh, end.z + w, layer)

        # Bottom flange
        self.add_line(start.x, start.y - hh, start.z + w,
                      end.x, end.y - hh, end.z + w, layer)

    # ===========================================
    # Phase 3: Array Functions
    # ===========================================

    def array_along_line(self, start: Point3D, end: Point3D, count: int,
                         element_func, element_length: float = 0,
                         **kwargs) -> List[Point3D]:
        """
        Create array of elements along a 3D line.

        Args:
            start: Start point of the array line
            end: End point of the array line
            count: Number of elements
            element_func: Function to call for each element (receives start, end points)
            element_length: Length of each element (for perpendicular elements)
            **kwargs: Additional arguments passed to element_func

        Returns:
            List of element positions
        """
        positions = []

        if count < 1:
            return positions

        # Calculate spacing
        dx = (end.x - start.x) / (count + 1)
        dy = (end.y - start.y) / (count + 1)
        dz = (end.z - start.z) / (count + 1)

        for i in range(1, count + 1):
            pos = Point3D(
                start.x + dx * i,
                start.y + dy * i,
                start.z + dz * i
            )
            positions.append(pos)

            if element_func and element_length > 0:
                # Determine perpendicular direction based on main axis
                if abs(end.x - start.x) > abs(end.z - start.z):
                    # Array along X, elements extend in Z
                    elem_end = Point3D(pos.x, pos.y, pos.z + element_length)
                else:
                    # Array along Z, elements extend in X
                    elem_end = Point3D(pos.x + element_length, pos.y, pos.z)

                element_func(pos, elem_end, **kwargs)

        return positions

    def draw_purlin_array(self, rafter_start: Point3D, rafter_end: Point3D,
                          count: int, purlin_length: float,
                          section: SteelSection = None,
                          layer: str = "PURLIN"):
        """
        Draw array of purlins along a rafter.

        Purlins are perpendicular to the rafter and extend in the Z (depth) direction.

        Args:
            rafter_start: Start point of rafter
            rafter_end: End point of rafter
            count: Number of purlins
            purlin_length: Length of each purlin (depth direction)
            section: C-channel section for purlins
            layer: DXF layer name
        """
        section = section or SteelSection.c_channel(150, 75)

        def draw_purlin(start: Point3D, end: Point3D, **kwargs):
            # Purlins extend in Z direction (depth)
            purlin_end = Point3D(start.x, start.y, start.z + purlin_length)
            self.draw_c_channel_segment(start, purlin_end, section, layer)

        # Array purlins along rafter
        # Note: element_length is used differently here
        positions = []

        if count < 1:
            return

        dx = (rafter_end.x - rafter_start.x) / (count + 1)
        dy = (rafter_end.y - rafter_start.y) / (count + 1)
        dz = (rafter_end.z - rafter_start.z) / (count + 1)

        for i in range(1, count + 1):
            pos = Point3D(
                rafter_start.x + dx * i,
                rafter_start.y + dy * i,
                rafter_start.z + dz * i
            )
            # Purlin extends in depth (Z) direction
            purlin_end = Point3D(pos.x, pos.y, pos.z + purlin_length)

            # Draw as simple lines for purlins (C-channel representation)
            self.add_line(pos.x, pos.y, pos.z,
                         purlin_end.x, purlin_end.y, purlin_end.z, layer)
            # Add flange lines for visibility
            h = section.height / 2
            self.add_line(pos.x, pos.y + h, pos.z,
                         purlin_end.x, purlin_end.y + h, purlin_end.z, layer)
            self.add_line(pos.x, pos.y - h, pos.z,
                         purlin_end.x, purlin_end.y - h, purlin_end.z, layer)

    def draw_x_bracing(self, p1: Point3D, p2: Point3D, p3: Point3D, p4: Point3D,
                       layer: str = "BRACING"):
        """
        Draw X-bracing in a rectangular bay.

        Args:
            p1: Bottom-left point
            p2: Bottom-right point
            p3: Top-right point
            p4: Top-left point
            layer: DXF layer name
        """
        # Diagonal 1: p1 to p3
        self.add_line_3d(p1, p3, layer)
        # Diagonal 2: p2 to p4
        self.add_line_3d(p2, p4, layer)

    # ===========================================
    # MCP Command Generation
    # ===========================================

    def get_mcp_commands(self) -> List[Dict[str, Any]]:
        """
        Get list of MCP tool commands to execute.

        Returns:
            List of command dictionaries ready for MCP execution
        """
        return self.commands

    def generate_mcp_script(self) -> str:
        """
        Generate human-readable MCP command script.

        Returns:
            String representation of all commands
        """
        lines = ["# Isometric Drawing Commands", ""]

        for cmd in self.commands:
            if cmd["type"] == "line":
                s = cmd["start"]
                e = cmd["end"]
                layer = cmd.get("layer", "0")
                color = cmd.get("color", "")
                color_str = f", color={color}" if color else ""
                lines.append(f"create_line: ({s['x']:.2f}, {s['y']:.2f}) -> ({e['x']:.2f}, {e['y']:.2f}) [layer={layer}{color_str}]")

        return "\n".join(lines)


# ===========================================
# High-Level Drawing Functions
# ===========================================

def draw_multi_bay_portal_frame(
    renderer: IsometricRenderer,
    num_bays: int = 2,
    bay_width: float = 6000,  # mm
    building_depth: float = 20000,  # mm
    eave_height: float = 6000,  # mm
    ridge_height: float = 7500,  # mm
    column_section: SteelSection = None,
    rafter_section: SteelSection = None,
    purlin_count: int = 6
) -> Dict[str, Any]:
    """
    Draw a complete multi-bay portal frame building in isometric view.

    Args:
        renderer: IsometricRenderer instance
        num_bays: Number of bays (spans)
        bay_width: Width of each bay in mm
        building_depth: Depth of building in mm
        eave_height: Height to eave in mm
        ridge_height: Height to ridge in mm
        column_section: H-beam section for columns
        rafter_section: H-beam section for rafters
        purlin_count: Number of purlins per roof slope

    Returns:
        Summary of drawn elements
    """
    column_section = column_section or SteelSection.h_beam(400, 200)
    rafter_section = rafter_section or SteelSection.h_beam(350, 175)
    purlin_section = SteelSection.c_channel(150, 75)

    total_width = bay_width * num_bays
    ridge_x = total_width / 2

    elements = {
        "columns": 0,
        "rafters": 0,
        "purlins": 0,
        "bracing": 0
    }

    # Draw columns (front frame at z=0)
    for i in range(num_bays + 1):
        x = i * bay_width
        start = Point3D(x, 0, 0)
        end = Point3D(x, eave_height, 0)
        renderer.draw_h_beam_segment(start, end, column_section, "COLUMN")
        elements["columns"] += 1

    # Draw columns (back frame at z=building_depth)
    for i in range(num_bays + 1):
        x = i * bay_width
        start = Point3D(x, 0, building_depth)
        end = Point3D(x, eave_height, building_depth)
        renderer.draw_h_beam_segment(start, end, column_section, "COLUMN")
        elements["columns"] += 1

    # Draw rafters (front frame)
    # Left slope
    left_rafter_start = Point3D(0, eave_height, 0)
    left_rafter_end = Point3D(ridge_x, ridge_height, 0)
    renderer.draw_h_beam_segment(left_rafter_start, left_rafter_end, rafter_section, "BEAM")
    elements["rafters"] += 1

    # Right slope
    right_rafter_start = Point3D(total_width, eave_height, 0)
    right_rafter_end = Point3D(ridge_x, ridge_height, 0)
    renderer.draw_h_beam_segment(right_rafter_start, right_rafter_end, rafter_section, "BEAM")
    elements["rafters"] += 1

    # Draw rafters (back frame)
    renderer.draw_h_beam_segment(
        Point3D(0, eave_height, building_depth),
        Point3D(ridge_x, ridge_height, building_depth),
        rafter_section, "BEAM"
    )
    renderer.draw_h_beam_segment(
        Point3D(total_width, eave_height, building_depth),
        Point3D(ridge_x, ridge_height, building_depth),
        rafter_section, "BEAM"
    )
    elements["rafters"] += 2

    # Draw purlins (connecting front and back frames)
    renderer.draw_purlin_array(
        left_rafter_start, left_rafter_end,
        purlin_count, building_depth,
        purlin_section, "PURLIN"
    )
    renderer.draw_purlin_array(
        right_rafter_start, right_rafter_end,
        purlin_count, building_depth,
        purlin_section, "PURLIN"
    )
    elements["purlins"] = purlin_count * 2

    # Draw eave struts (connecting columns at eave level)
    for i in range(num_bays + 1):
        x = i * bay_width
        renderer.add_line(x, eave_height, 0, x, eave_height, building_depth, "BEAM")

    # Draw ridge beam
    renderer.add_line(ridge_x, ridge_height, 0, ridge_x, ridge_height, building_depth, "BEAM")

    # Draw X-bracing in end bays
    # Front left bay bracing
    renderer.draw_x_bracing(
        Point3D(0, 0, 0),
        Point3D(bay_width, 0, 0),
        Point3D(bay_width, eave_height, 0),
        Point3D(0, eave_height, 0),
        "BRACING"
    )
    elements["bracing"] += 1

    # Back left bay bracing
    renderer.draw_x_bracing(
        Point3D(0, 0, building_depth),
        Point3D(bay_width, 0, building_depth),
        Point3D(bay_width, eave_height, building_depth),
        Point3D(0, eave_height, building_depth),
        "BRACING"
    )
    elements["bracing"] += 1

    return elements


# ===========================================
# Utility Functions
# ===========================================

def scale_for_canvas(building_width: float, building_height: float,
                     canvas_width: float = 800, canvas_height: float = 600,
                     margin: float = 50) -> Tuple[float, Point2D]:
    """
    Calculate scale and origin to fit building in canvas.

    Args:
        building_width: Building width in mm
        building_height: Building height in mm
        canvas_width: Canvas width in pixels/units
        canvas_height: Canvas height in pixels/units
        margin: Margin around building

    Returns:
        Tuple of (scale_factor, origin_point)
    """
    available_width = canvas_width - 2 * margin
    available_height = canvas_height - 2 * margin

    # Account for isometric projection spreading
    iso_width = building_width * 1.5  # Approximate spread
    iso_height = building_height * 1.3

    scale_x = available_width / iso_width
    scale_y = available_height / iso_height
    scale = min(scale_x, scale_y)

    origin = Point2D(margin + available_width * 0.3, margin)

    return scale, origin

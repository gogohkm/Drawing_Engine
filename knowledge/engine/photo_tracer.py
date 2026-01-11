"""
Photo Tracer Module - 사진 위에 직접 트레이싱
==============================================

핵심 철학:
- 배경 이미지 좌표계를 기준으로 직접 그리기
- 비율 계산/자동 생성이 아닌, 사진에서 보이는 선을 직접 지정
- 정규화 좌표(0~1)를 배경 이미지 실제 좌표로 변환

사용 워크플로우:
1. 배경 이미지 정보 입력 (위치, 크기)
2. 사진을 보고 선의 시작점/끝점을 0~1 정규화 좌표로 지정
3. 엔진이 실제 DXF 좌표로 변환
4. MCP 도구로 실행

예시:
  # 배경 이미지: position=(-73, -77), size=(178, 100)
  # 사진에서 왼쪽 기둥: x=0.12, y는 0.0~0.58

  tracer = PhotoTracer()
  tracer.set_background(x=-73, y=-77, width=178, height=100)
  tracer.add_line("col_L", 0.12, 0.0, 0.12, 0.58, "COLUMN")
  sequence = tracer.generate_sequence()
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class TraceLine:
    """트레이싱 선 - 정규화 좌표와 실제 좌표 모두 저장"""
    line_id: str
    # 정규화 좌표 (0~1)
    nx1: float  # normalized x1
    ny1: float
    nx2: float
    ny2: float
    # 실제 DXF 좌표 (계산됨)
    x1: float = 0.0
    y1: float = 0.0
    x2: float = 0.0
    y2: float = 0.0
    # 속성
    layer: str = "0"
    color: Optional[int] = None

    def to_dict(self) -> Dict:
        return {
            "id": self.line_id,
            "normalized": {"x1": self.nx1, "y1": self.ny1, "x2": self.nx2, "y2": self.ny2},
            "actual": {"x1": self.x1, "y1": self.y1, "x2": self.x2, "y2": self.y2},
            "layer": self.layer,
            "color": self.color
        }


@dataclass
class BackgroundInfo:
    """배경 이미지 정보"""
    x: float = 0.0      # 좌하단 X
    y: float = 0.0      # 좌하단 Y
    width: float = 100.0
    height: float = 100.0

    def to_dict(self) -> Dict:
        return {
            "x": self.x, "y": self.y,
            "width": self.width, "height": self.height,
            "bounds": {
                "minX": self.x,
                "minY": self.y,
                "maxX": self.x + self.width,
                "maxY": self.y + self.height
            }
        }


class PhotoTracer:
    """
    사진 트레이싱 엔진

    핵심 기능:
    1. 배경 이미지 좌표계 설정
    2. 정규화 좌표 → 실제 좌표 변환
    3. MCP 도구 시퀀스 생성
    """

    def __init__(self):
        self.background: Optional[BackgroundInfo] = None
        self.lines: List[TraceLine] = []
        self.layers: Dict[str, int] = {}  # layer_name -> color
        self.context_id: str = ""

        # 기본 레이어 색상
        self.default_layer_colors = {
            "COLUMN": 7,      # White
            "BEAM": 4,        # Cyan
            "TRUSS": 6,       # Magenta
            "PURLIN": 3,      # Green
            "BRACING": 5,     # Blue
            "FOUNDATION": 8,  # Gray
            "OUTLINE": 7,     # White
            "0": 7            # Default
        }

    def set_background(self, x: float, y: float, width: float, height: float):
        """
        배경 이미지 정보 설정

        Args:
            x: 이미지 좌하단 X 좌표
            y: 이미지 좌하단 Y 좌표
            width: 이미지 너비
            height: 이미지 높이
        """
        self.background = BackgroundInfo(x=x, y=y, width=width, height=height)
        self.context_id = f"trace_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    def set_background_from_mcp(self, bg_info: Dict):
        """
        MCP get_background_images 결과에서 배경 설정

        Args:
            bg_info: {"position": {"x": ..., "y": ...}, "baseWidth": ..., "baseHeight": ...}
        """
        pos = bg_info.get("position", {})
        self.set_background(
            x=pos.get("x", 0),
            y=pos.get("y", 0),
            width=bg_info.get("baseWidth", 100),
            height=bg_info.get("baseHeight", 100)
        )

    def _normalize_to_actual(self, nx: float, ny: float) -> Tuple[float, float]:
        """
        정규화 좌표(0~1)를 실제 DXF 좌표로 변환

        정규화 좌표:
        - x=0: 이미지 왼쪽, x=1: 이미지 오른쪽
        - y=0: 이미지 아래쪽, y=1: 이미지 위쪽
        """
        if not self.background:
            raise ValueError("Background not set. Call set_background() first.")

        bg = self.background
        actual_x = bg.x + (nx * bg.width)
        actual_y = bg.y + (ny * bg.height)
        return actual_x, actual_y

    def add_line(self, line_id: str,
                 nx1: float, ny1: float, nx2: float, ny2: float,
                 layer: str = "0", color: Optional[int] = None):
        """
        트레이싱 선 추가 (정규화 좌표 사용)

        Args:
            line_id: 선 식별자
            nx1, ny1: 시작점 정규화 좌표 (0~1)
            nx2, ny2: 끝점 정규화 좌표 (0~1)
            layer: 레이어 이름
            color: 색상 (None이면 레이어 색상 사용)
        """
        # 실제 좌표 계산
        x1, y1 = self._normalize_to_actual(nx1, ny1)
        x2, y2 = self._normalize_to_actual(nx2, ny2)

        line = TraceLine(
            line_id=line_id,
            nx1=nx1, ny1=ny1, nx2=nx2, ny2=ny2,
            x1=x1, y1=y1, x2=x2, y2=y2,
            layer=layer,
            color=color
        )
        self.lines.append(line)

        # 레이어 등록
        if layer not in self.layers:
            self.layers[layer] = self.default_layer_colors.get(layer, 7)

    def add_lines_batch(self, lines_data: List[Dict]):
        """
        여러 선 일괄 추가

        Args:
            lines_data: [{"id": ..., "nx1": ..., "ny1": ..., "nx2": ..., "ny2": ..., "layer": ...}, ...]
        """
        for line in lines_data:
            self.add_line(
                line_id=line.get("id", f"line_{len(self.lines)}"),
                nx1=line["nx1"],
                ny1=line["ny1"],
                nx2=line["nx2"],
                ny2=line["ny2"],
                layer=line.get("layer", "0"),
                color=line.get("color")
            )

    def clear_lines(self):
        """모든 선 제거"""
        self.lines = []
        self.layers = {}

    def generate_sequence(self) -> Dict:
        """
        MCP 도구 실행 시퀀스 생성

        Returns:
            {
                "context_id": ...,
                "background": {...},
                "total_lines": ...,
                "sequence": [
                    {"step": 1, "name": "레이어 생성", "tools": [...]},
                    {"step": 2, "name": "선 그리기", "tools": [...]}
                ]
            }
        """
        if not self.background:
            return {"error": "Background not set"}

        if not self.lines:
            return {"error": "No lines to draw"}

        sequence = []

        # Step 1: 레이어 생성
        layer_tools = []
        for layer_name, color in self.layers.items():
            if layer_name != "0":  # 기본 레이어는 생성 불필요
                layer_tools.append({
                    "tool": "create_layer",
                    "args": {"name": layer_name, "color": color}
                })

        if layer_tools:
            sequence.append({
                "step": 1,
                "name": "레이어 생성",
                "parallel": True,
                "tools": layer_tools
            })

        # Step 2: 선 그리기 (레이어별 그룹화)
        lines_by_layer: Dict[str, List[TraceLine]] = {}
        for line in self.lines:
            if line.layer not in lines_by_layer:
                lines_by_layer[line.layer] = []
            lines_by_layer[line.layer].append(line)

        step_num = 2
        for layer_name, layer_lines in lines_by_layer.items():
            line_tools = []
            for line in layer_lines:
                tool_args = {
                    "start": {"x": round(line.x1, 2), "y": round(line.y1, 2)},
                    "end": {"x": round(line.x2, 2), "y": round(line.y2, 2)},
                    "layer": line.layer
                }
                if line.color is not None:
                    tool_args["color"] = line.color

                line_tools.append({
                    "tool": "create_line",
                    "args": tool_args,
                    "id": line.line_id
                })

            sequence.append({
                "step": step_num,
                "name": f"{layer_name} 레이어 선 ({len(layer_lines)}개)",
                "parallel": True,
                "tools": line_tools
            })
            step_num += 1

        return {
            "success": True,
            "context_id": self.context_id,
            "background": self.background.to_dict(),
            "total_lines": len(self.lines),
            "total_steps": len(sequence),
            "sequence": sequence
        }

    def get_lines_summary(self) -> Dict:
        """현재 등록된 선들의 요약"""
        return {
            "context_id": self.context_id,
            "background": self.background.to_dict() if self.background else None,
            "total_lines": len(self.lines),
            "layers": self.layers,
            "lines": [line.to_dict() for line in self.lines]
        }

    def to_json(self) -> str:
        """전체 상태를 JSON으로 출력"""
        return json.dumps({
            "context_id": self.context_id,
            "background": self.background.to_dict() if self.background else None,
            "layers": self.layers,
            "lines": [line.to_dict() for line in self.lines]
        }, ensure_ascii=False, indent=2)


# =============================================================================
# CLI 인터페이스 함수들
# =============================================================================

def cli_trace_init(bg_x: str, bg_y: str, bg_width: str, bg_height: str) -> str:
    """
    트레이싱 초기화 - 배경 이미지 설정

    Args:
        bg_x, bg_y: 배경 이미지 좌하단 좌표
        bg_width, bg_height: 배경 이미지 크기
    """
    tracer = PhotoTracer()
    tracer.set_background(
        x=float(bg_x),
        y=float(bg_y),
        width=float(bg_width),
        height=float(bg_height)
    )

    return json.dumps({
        "success": True,
        "context_id": tracer.context_id,
        "background": tracer.background.to_dict(),
        "message": "Background set. Now add lines with trace_add command.",
        "coordinate_system": {
            "description": "정규화 좌표 (0~1) 사용",
            "x": "0=왼쪽, 1=오른쪽",
            "y": "0=아래, 1=위"
        }
    }, ensure_ascii=False, indent=2)


def cli_trace_add(bg_json: str, lines_json: str) -> str:
    """
    선 추가 및 시퀀스 생성

    Args:
        bg_json: 배경 정보 {"x": ..., "y": ..., "width": ..., "height": ...}
        lines_json: 선 목록 [{"id": ..., "nx1": ..., "ny1": ..., "nx2": ..., "ny2": ..., "layer": ...}, ...]
    """
    try:
        bg = json.loads(bg_json)
        lines = json.loads(lines_json)

        tracer = PhotoTracer()
        tracer.set_background(
            x=bg.get("x", 0),
            y=bg.get("y", 0),
            width=bg.get("width", 100),
            height=bg.get("height", 100)
        )
        tracer.add_lines_batch(lines)

        return json.dumps(tracer.generate_sequence(), ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_trace_quick(bg_json: str, elements_json: str) -> str:
    """
    빠른 트레이싱 - 구조물 요소 기반

    사진에서 보이는 구조물 요소를 간단히 정의하면 자동으로 선으로 변환

    Args:
        bg_json: 배경 정보
        elements_json: 구조물 요소 정의
            {
                "columns": [{"x": 0.12, "y_bottom": 0, "y_top": 0.58}, ...],
                "beams": [{"x1": 0.12, "y1": 0.58, "x2": 0.5, "y2": 0.72}, ...],
                "roof_left": {"x1": 0.12, "y1": 0.58, "x2": 0.5, "y2": 0.72},
                "roof_right": {"x1": 0.5, "y1": 0.72, "x2": 0.88, "y2": 0.58}
            }
    """
    try:
        bg = json.loads(bg_json)
        elements = json.loads(elements_json)

        tracer = PhotoTracer()
        tracer.set_background(
            x=bg.get("x", 0),
            y=bg.get("y", 0),
            width=bg.get("width", 100),
            height=bg.get("height", 100)
        )

        # 기둥 변환
        for i, col in enumerate(elements.get("columns", [])):
            tracer.add_line(
                f"col_{i}",
                col["x"], col["y_bottom"],
                col["x"], col["y_top"],
                layer="COLUMN"
            )

        # 보 변환
        for i, beam in enumerate(elements.get("beams", [])):
            tracer.add_line(
                f"beam_{i}",
                beam["x1"], beam["y1"],
                beam["x2"], beam["y2"],
                layer="BEAM"
            )

        # 지붕 좌측
        if "roof_left" in elements:
            r = elements["roof_left"]
            tracer.add_line("roof_L", r["x1"], r["y1"], r["x2"], r["y2"], layer="BEAM")

        # 지붕 우측
        if "roof_right" in elements:
            r = elements["roof_right"]
            tracer.add_line("roof_R", r["x1"], r["y1"], r["x2"], r["y2"], layer="BEAM")

        # 퍼린
        for i, purlin in enumerate(elements.get("purlins", [])):
            tracer.add_line(
                f"purlin_{i}",
                purlin["x1"], purlin["y"],
                purlin["x2"], purlin["y"],
                layer="PURLIN"
            )

        # 트러스 웹
        for i, web in enumerate(elements.get("truss_webs", [])):
            tracer.add_line(
                f"web_{i}",
                web["x1"], web["y1"],
                web["x2"], web["y2"],
                layer="TRUSS"
            )

        # 가새
        for i, brace in enumerate(elements.get("bracing", [])):
            tracer.add_line(
                f"brace_{i}",
                brace["x1"], brace["y1"],
                brace["x2"], brace["y2"],
                layer="BRACING"
            )

        # 기초선
        if "foundation" in elements:
            f = elements["foundation"]
            tracer.add_line("foundation", f["x1"], f["y"], f["x2"], f["y"], layer="FOUNDATION")

        # 기타 직접 지정 선
        for line in elements.get("lines", []):
            tracer.add_line(
                line.get("id", f"line_{len(tracer.lines)}"),
                line["nx1"], line["ny1"],
                line["nx2"], line["ny2"],
                layer=line.get("layer", "0")
            )

        return json.dumps(tracer.generate_sequence(), ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def cli_trace_info() -> str:
    """트레이싱 모듈 사용법"""
    return json.dumps({
        "module": "photo_tracer",
        "version": "2.0",
        "description": "배경 이미지 위에 직접 트레이싱",

        "핵심_원칙": [
            "배경 이미지 좌표계를 기준으로 그리기",
            "정규화 좌표(0~1)로 위치 지정",
            "비율 자동계산 없음 - 직접 좌표 지정"
        ],

        "coordinate_system": {
            "정규화_좌표": "0~1 범위",
            "x=0": "이미지 왼쪽 끝",
            "x=1": "이미지 오른쪽 끝",
            "y=0": "이미지 아래쪽 끝",
            "y=1": "이미지 위쪽 끝"
        },

        "commands": {
            "trace_init": "배경 이미지 설정: trace_init <x> <y> <width> <height>",
            "trace_add": "선 추가+시퀀스: trace_add '<bg_json>' '<lines_json>'",
            "trace_quick": "빠른 트레이싱: trace_quick '<bg_json>' '<elements_json>'",
            "trace_info": "이 도움말"
        },

        "workflow": [
            "1. MCP get_background_images로 배경 이미지 정보 확인",
            "2. 사진을 보고 주요 선의 정규화 좌표(0~1) 파악",
            "3. trace_quick 또는 trace_add로 시퀀스 생성",
            "4. 생성된 시퀀스의 tools를 MCP로 실행"
        ],

        "example_trace_quick": {
            "bg": {"x": -73, "y": -77, "width": 178, "height": 100},
            "elements": {
                "columns": [
                    {"x": 0.12, "y_bottom": 0.0, "y_top": 0.58},
                    {"x": 0.88, "y_bottom": 0.0, "y_top": 0.58}
                ],
                "roof_left": {"x1": 0.12, "y1": 0.58, "x2": 0.5, "y2": 0.75},
                "roof_right": {"x1": 0.5, "y1": 0.75, "x2": 0.88, "y2": 0.58},
                "foundation": {"x1": 0.12, "y": 0.0, "x2": 0.88}
            }
        },

        "example_trace_add": {
            "bg": {"x": -73, "y": -77, "width": 178, "height": 100},
            "lines": [
                {"id": "col_L", "nx1": 0.12, "ny1": 0.0, "nx2": 0.12, "ny2": 0.58, "layer": "COLUMN"},
                {"id": "col_R", "nx1": 0.88, "ny1": 0.0, "nx2": 0.88, "ny2": 0.58, "layer": "COLUMN"},
                {"id": "roof_L", "nx1": 0.12, "ny1": 0.58, "nx2": 0.5, "ny2": 0.75, "layer": "BEAM"},
                {"id": "roof_R", "nx1": 0.5, "ny1": 0.75, "nx2": 0.88, "ny2": 0.58, "layer": "BEAM"}
            ]
        }
    }, ensure_ascii=False, indent=2)


def cli_trace_checklist() -> str:
    """사진 분석 체크리스트 - 정규화 좌표 파악용"""
    return json.dumps({
        "title": "사진 트레이싱 체크리스트",
        "description": "사진을 보고 각 요소의 정규화 좌표(0~1)를 파악합니다",

        "steps": [
            {
                "step": 1,
                "name": "배경 이미지 정보 확인",
                "action": "MCP get_background_images 호출",
                "result": "position.x, position.y, baseWidth, baseHeight 획득"
            },
            {
                "step": 2,
                "name": "외곽선 파악",
                "items": [
                    "좌측 기둥 x 위치 (0~1)",
                    "우측 기둥 x 위치 (0~1)",
                    "바닥선 y 위치 (보통 0.0 근처)",
                    "처마선 y 위치 (0~1)",
                    "지붕 최고점 x, y 위치"
                ]
            },
            {
                "step": 3,
                "name": "내부 요소 파악",
                "items": [
                    "내부 기둥들의 x 위치",
                    "보/빔의 시작점, 끝점",
                    "퍼린 라인들의 y 위치와 x 범위",
                    "트러스 웹부재 위치",
                    "가새 위치"
                ]
            },
            {
                "step": 4,
                "name": "좌표 정리",
                "format": {
                    "columns": [{"x": "...", "y_bottom": "...", "y_top": "..."}],
                    "roof_left": {"x1": "...", "y1": "...", "x2": "...", "y2": "..."},
                    "roof_right": {"x1": "...", "y1": "...", "x2": "...", "y2": "..."},
                    "purlins": [{"x1": "...", "x2": "...", "y": "..."}],
                    "foundation": {"x1": "...", "x2": "...", "y": "..."}
                }
            }
        ],

        "tips": [
            "정규화 좌표는 이미지 기준: x=0(왼쪽), x=1(오른쪽), y=0(아래), y=1(위)",
            "대략적인 위치로 시작하고 결과를 보며 조정",
            "겹쳐 보이는 프레임은 약간의 x offset으로 표현"
        ]
    }, ensure_ascii=False, indent=2)


# 하위 호환성을 위한 기존 함수들 (deprecated)
def cli_checklist() -> str:
    """[Deprecated] 기존 체크리스트 - trace_checklist 사용 권장"""
    return cli_trace_checklist()

def cli_prompt() -> str:
    """[Deprecated] 기존 프롬프트"""
    return json.dumps({
        "deprecated": True,
        "message": "Use trace_info and trace_checklist instead",
        "new_workflow": [
            "1. get_background_images로 배경 정보 확인",
            "2. trace_checklist로 분석 체크리스트 확인",
            "3. trace_quick으로 요소 기반 트레이싱",
            "4. 또는 trace_add로 직접 선 추가"
        ]
    }, ensure_ascii=False, indent=2)

def cli_info() -> str:
    """모듈 정보"""
    return cli_trace_info()

def cli_create(*args) -> str:
    """[Deprecated] 기존 create"""
    return json.dumps({
        "deprecated": True,
        "message": "Use trace_init or trace_quick instead"
    })

def cli_coords(*args) -> str:
    """[Deprecated] 기존 coords"""
    return json.dumps({
        "deprecated": True,
        "message": "Coordinates are now calculated automatically from normalized coords"
    })

def cli_sequence(*args) -> str:
    """[Deprecated] 기존 sequence"""
    return json.dumps({
        "deprecated": True,
        "message": "Use trace_add or trace_quick to get sequence directly"
    })

def cli_status(*args) -> str:
    """[Deprecated] 기존 status"""
    return json.dumps({
        "deprecated": True,
        "message": "Status tracking removed. Use simple workflow instead."
    })

def cli_draw(*args) -> str:
    """[Deprecated] 기존 draw"""
    return json.dumps({
        "deprecated": True,
        "message": "Use trace_quick instead"
    })


# =============================================================================
# Main CLI
# =============================================================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Photo Tracer v2.0 - 배경 이미지 위에 직접 트레이싱")
        print("")
        print("Commands:")
        print("  python photo_tracer.py trace_info              - 사용법")
        print("  python photo_tracer.py trace_checklist         - 분석 체크리스트")
        print("  python photo_tracer.py trace_init <x> <y> <w> <h>  - 배경 설정")
        print("  python photo_tracer.py trace_add '<bg>' '<lines>'  - 선 추가")
        print("  python photo_tracer.py trace_quick '<bg>' '<elements>' - 빠른 트레이싱")
        print("")
        print("Example:")
        print('  python photo_tracer.py trace_quick \'{"x":-73,"y":-77,"width":178,"height":100}\' \'{"columns":[{"x":0.12,"y_bottom":0,"y_top":0.58}]}\'')
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "trace_info" or cmd == "info":
        print(cli_trace_info())
    elif cmd == "trace_checklist" or cmd == "checklist":
        print(cli_trace_checklist())
    elif cmd == "trace_init" and len(sys.argv) >= 6:
        print(cli_trace_init(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    elif cmd == "trace_add" and len(sys.argv) >= 4:
        print(cli_trace_add(sys.argv[2], sys.argv[3]))
    elif cmd == "trace_quick" and len(sys.argv) >= 4:
        print(cli_trace_quick(sys.argv[2], sys.argv[3]))
    # 하위 호환성
    elif cmd == "prompt":
        print(cli_prompt())
    elif cmd == "create":
        print(cli_create())
    elif cmd == "coords":
        print(cli_coords())
    elif cmd == "sequence":
        print(cli_sequence())
    elif cmd == "status":
        print(cli_status())
    elif cmd == "draw":
        print(cli_draw())
    else:
        print(json.dumps({"error": f"Unknown command: {cmd}. Use 'trace_info' for help."}))

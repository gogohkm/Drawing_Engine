"""
Image Analyzer - 이미지 기반 도면 작도를 위한 분석 모듈

이미지에서 구조물을 분석하고 작도 계획을 생성합니다.

사용법:
    analyzer = ImageAnalyzer()

    # 1단계: 분석 결과 저장
    analyzer.save_analysis(analysis_data)

    # 2단계: 좌표 계산
    coords = analyzer.calculate_coordinates(canvas_width=800, canvas_height=500)

    # 3단계: MCP 시퀀스 생성
    sequence = analyzer.generate_drawing_sequence()
"""

import json
import os
import math
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict

# 경로 설정
KNOWLEDGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass
class AnalysisResult:
    """이미지 분석 결과 데이터 클래스"""
    # 1단계: 구조 식별
    structure_type: str = ""
    sub_type: str = ""
    usage: str = ""
    main_components: List[str] = field(default_factory=list)

    # 2단계: 비율 분석
    width_height_ratio: float = 2.0
    roof_pitch_degrees: float = 10.0
    eave_height_ratio: float = 0.7
    span_count: int = 1

    # 3단계: 패턴 분석
    columns_left: int = 1
    columns_right: int = 1
    columns_middle: int = 0
    truss_panels: int = 8
    vertical_webs: int = 7
    diagonal_webs: int = 8
    purlins_per_slope: int = 6
    bracing_levels: int = 2

    # 4단계: 상세 수준
    detail_level: str = "L2_structural"

    # 메타데이터
    analysis_id: str = ""
    created_at: str = ""
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'AnalysisResult':
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})


class ImageAnalyzer:
    """이미지 분석 및 작도 계획 생성"""

    def __init__(self):
        self.analysis: Optional[AnalysisResult] = None
        self.templates = self._load_templates()
        self.analysis_guide = self._load_analysis_guide()
        self.calculated_coords: Dict = {}

    def _load_templates(self) -> Dict:
        """구조 템플릿 로드"""
        template_path = os.path.join(KNOWLEDGE_ROOT, "patterns", "structure_templates.json")
        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def _load_analysis_guide(self) -> Dict:
        """분석 가이드 로드"""
        guide_path = os.path.join(KNOWLEDGE_ROOT, "patterns", "image_analysis.json")
        if os.path.exists(guide_path):
            with open(guide_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    # ========== 1. 분석 체크리스트 생성 ==========

    def get_analysis_checklist(self) -> Dict:
        """Claude가 이미지 분석 시 사용할 체크리스트 반환"""
        return {
            "checklist": self.analysis_guide.get("analysis_checklist", {}),
            "prompts": self.analysis_guide.get("analysis_prompts", {}),
            "common_mistakes": self.analysis_guide.get("common_mistakes", {})
        }

    def get_analysis_prompt(self, stage: int) -> str:
        """단계별 분석 프롬프트 반환"""
        prompts = self.analysis_guide.get("analysis_prompts", {})
        stage_map = {
            1: "stage1_structure",
            2: "stage2_proportions",
            3: "stage3_patterns"
        }
        stage_key = stage_map.get(stage)
        if stage_key and stage_key in prompts:
            return prompts[stage_key].get("prompt", "")
        return ""

    # ========== 2. 분석 결과 저장 ==========

    def save_analysis(self, analysis_data: Dict) -> str:
        """분석 결과 저장"""
        # 분석 ID 생성
        analysis_id = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # AnalysisResult 생성
        self.analysis = AnalysisResult(
            analysis_id=analysis_id,
            created_at=datetime.now().isoformat(),
            **{k: v for k, v in analysis_data.items() if k in AnalysisResult.__dataclass_fields__}
        )

        # 파일 저장
        analysis_dir = os.path.join(KNOWLEDGE_ROOT, "analysis_cache")
        os.makedirs(analysis_dir, exist_ok=True)

        filepath = os.path.join(analysis_dir, f"{analysis_id}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.analysis.to_dict(), f, ensure_ascii=False, indent=2)

        return analysis_id

    def load_analysis(self, analysis_id: str) -> Optional[AnalysisResult]:
        """저장된 분석 결과 로드"""
        filepath = os.path.join(KNOWLEDGE_ROOT, "analysis_cache", f"{analysis_id}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.analysis = AnalysisResult.from_dict(data)
                return self.analysis
        return None

    # ========== 3. 좌표 계산 ==========

    def calculate_coordinates(self, canvas_width: float = 800,
                             canvas_height: float = 500,
                             margin: float = 50) -> Dict:
        """
        분석 결과 기반 좌표 계산

        Args:
            canvas_width: 캔버스 너비
            canvas_height: 캔버스 높이
            margin: 여백

        Returns:
            계산된 좌표 딕셔너리
        """
        if not self.analysis:
            raise ValueError("No analysis data. Call save_analysis() first.")

        a = self.analysis

        # 기본 좌표
        left_x = margin
        right_x = canvas_width - margin
        bottom_y = margin
        total_height = canvas_height - 2 * margin
        total_width = right_x - left_x

        # 처마 높이 (기둥 상단)
        eave_y = bottom_y + total_height * a.eave_height_ratio

        # 용마루 높이 (지붕 정점)
        center_x = (left_x + right_x) / 2
        roof_rise = (total_width / 2) * math.tan(math.radians(a.roof_pitch_degrees))
        ridge_y = eave_y + roof_rise

        # 기둥 너비 (H형강 표현용)
        column_width = total_width * 0.08

        # 트러스 하현재 깊이
        truss_depth = roof_rise * 0.3  # 지붕 높이의 30%
        bottom_chord_y = eave_y - truss_depth

        coords = {
            "canvas": {
                "width": canvas_width,
                "height": canvas_height,
                "margin": margin
            },
            "bounds": {
                "left_x": left_x,
                "right_x": right_x,
                "bottom_y": bottom_y,
                "top_y": ridge_y,
                "center_x": center_x
            },
            "columns": self._calculate_column_coords(
                left_x, right_x, bottom_y, eave_y, column_width, a
            ),
            "roof": {
                "eave_y": eave_y,
                "ridge_x": center_x,
                "ridge_y": ridge_y,
                "pitch_degrees": a.roof_pitch_degrees
            },
            "truss": self._calculate_truss_coords(
                left_x, right_x, center_x, eave_y, ridge_y,
                bottom_chord_y, truss_depth, a
            ),
            "purlins": self._calculate_purlin_coords(
                left_x, right_x, center_x, eave_y, ridge_y, a
            ),
            "bracing": self._calculate_bracing_coords(
                left_x, right_x, bottom_y, eave_y, a
            )
        }

        self.calculated_coords = coords
        return coords

    def _calculate_column_coords(self, left_x: float, right_x: float,
                                  bottom_y: float, eave_y: float,
                                  column_width: float, a: AnalysisResult) -> Dict:
        """기둥 좌표 계산"""
        columns = []

        # 좌측 기둥
        columns.append({
            "name": "left_column",
            "center_x": left_x + column_width / 2,
            "bottom_y": bottom_y,
            "top_y": eave_y,
            "width": column_width
        })

        # 우측 기둥
        columns.append({
            "name": "right_column",
            "center_x": right_x - column_width / 2,
            "bottom_y": bottom_y,
            "top_y": eave_y,
            "width": column_width
        })

        # 중간 기둥
        if a.columns_middle > 0:
            span_width = (right_x - left_x) / (a.columns_middle + 1)
            for i in range(a.columns_middle):
                columns.append({
                    "name": f"middle_column_{i+1}",
                    "center_x": left_x + span_width * (i + 1),
                    "bottom_y": bottom_y,
                    "top_y": eave_y,
                    "width": column_width
                })

        return {"list": columns, "width": column_width}

    def _calculate_truss_coords(self, left_x: float, right_x: float,
                                 center_x: float, eave_y: float, ridge_y: float,
                                 bottom_chord_y: float, truss_depth: float,
                                 a: AnalysisResult) -> Dict:
        """트러스 좌표 계산"""
        # 상현재 (지붕 경사선)
        top_chord = {
            "left": {"start": (left_x, eave_y), "end": (center_x, ridge_y)},
            "right": {"start": (center_x, ridge_y), "end": (right_x, eave_y)}
        }

        # 하현재
        bottom_chord = {
            "start": (left_x, bottom_chord_y),
            "end": (right_x, bottom_chord_y)
        }

        # 수직 웹부재 위치 계산
        half_panels = a.truss_panels // 2
        panel_width = (center_x - left_x) / half_panels

        vertical_webs = []
        for i in range(1, half_panels):
            x = left_x + panel_width * i
            # 상현재 위의 Y 좌표 계산 (경사선 위)
            t = i / half_panels
            top_y = eave_y + (ridge_y - eave_y) * t
            vertical_webs.append({
                "x": x,
                "bottom_y": bottom_chord_y,
                "top_y": top_y - truss_depth * 0.1  # 약간 아래
            })

        # 우측도 대칭으로
        for i in range(1, half_panels):
            x = center_x + panel_width * i
            t = 1 - (i / half_panels)
            top_y = eave_y + (ridge_y - eave_y) * t
            vertical_webs.append({
                "x": x,
                "bottom_y": bottom_chord_y,
                "top_y": top_y - truss_depth * 0.1
            })

        # 중앙 수직 부재
        vertical_webs.append({
            "x": center_x,
            "bottom_y": bottom_chord_y,
            "top_y": ridge_y - truss_depth * 0.1
        })

        # 대각 웹부재 (하현재에서 상현재로)
        diagonal_webs = []
        for i in range(half_panels):
            # 좌측 경사면
            x1 = left_x + panel_width * i
            x2 = left_x + panel_width * (i + 1)
            t2 = (i + 1) / half_panels
            top_y2 = eave_y + (ridge_y - eave_y) * t2

            diagonal_webs.append({
                "start": (x1, bottom_chord_y),
                "end": (x2, top_y2 - truss_depth * 0.1)
            })

        for i in range(half_panels):
            # 우측 경사면
            x1 = right_x - panel_width * i
            x2 = right_x - panel_width * (i + 1)
            t2 = (i + 1) / half_panels
            top_y2 = eave_y + (ridge_y - eave_y) * t2

            diagonal_webs.append({
                "start": (x1, bottom_chord_y),
                "end": (x2, top_y2 - truss_depth * 0.1)
            })

        return {
            "top_chord": top_chord,
            "bottom_chord": bottom_chord,
            "bottom_chord_y": bottom_chord_y,
            "truss_depth": truss_depth,
            "vertical_webs": vertical_webs,
            "diagonal_webs": diagonal_webs,
            "panel_width": panel_width
        }

    def _calculate_purlin_coords(self, left_x: float, right_x: float,
                                  center_x: float, eave_y: float, ridge_y: float,
                                  a: AnalysisResult) -> List[Dict]:
        """퍼린 좌표 계산 (경사면을 따라 등간격)"""
        purlins = []

        # 좌측 경사면 길이
        slope_length = math.sqrt((center_x - left_x)**2 + (ridge_y - eave_y)**2)
        spacing = slope_length / (a.purlins_per_slope + 1)

        # 경사 방향 단위 벡터
        dx = (center_x - left_x) / slope_length
        dy = (ridge_y - eave_y) / slope_length

        # 좌측 경사면 퍼린
        for i in range(1, a.purlins_per_slope + 1):
            dist = spacing * i
            x = left_x + dx * dist
            y = eave_y + dy * dist
            purlins.append({
                "side": "left",
                "x": x,
                "y": y,
                "extends_to": right_x - (x - left_x)  # 대칭점
            })

        return purlins

    def _calculate_bracing_coords(self, left_x: float, right_x: float,
                                   bottom_y: float, eave_y: float,
                                   a: AnalysisResult) -> Dict:
        """가새 및 수평보 좌표 계산"""
        bracing = {
            "horizontal_beams": [],
            "x_bracing": []
        }

        # 수평보 레벨
        if a.bracing_levels > 0:
            level_spacing = (eave_y - bottom_y) / (a.bracing_levels + 1)
            for i in range(1, a.bracing_levels + 1):
                y = bottom_y + level_spacing * i
                bracing["horizontal_beams"].append({
                    "y": y,
                    "start_x": left_x,
                    "end_x": right_x
                })

        return bracing

    # ========== 4. MCP 시퀀스 생성 ==========

    def generate_drawing_sequence(self, detail_level: str = None) -> List[Dict]:
        """
        MCP 도구 호출 시퀀스 생성

        Args:
            detail_level: 상세 수준 (L1_outline, L2_structural, L3_detailed)

        Returns:
            MCP 도구 호출 시퀀스
        """
        if not self.calculated_coords:
            raise ValueError("No coordinates calculated. Call calculate_coordinates() first.")

        level = detail_level or (self.analysis.detail_level if self.analysis else "L2_structural")
        coords = self.calculated_coords

        sequence = []

        # Step 1: 레이어 생성
        sequence.append({
            "step": 1,
            "name": "레이어 생성",
            "parallel": True,
            "tools": [
                {"tool": "create_layer", "args": {"name": "COLUMN", "color": 7}},
                {"tool": "create_layer", "args": {"name": "BEAM", "color": 4}},
                {"tool": "create_layer", "args": {"name": "PURLIN", "color": 3}},
                {"tool": "create_layer", "args": {"name": "BRACING", "color": 5}},
                {"tool": "create_layer", "args": {"name": "BOLT", "color": 2}}
            ]
        })

        # Step 2: 기둥
        column_tools = []
        for col in coords["columns"]["list"]:
            column_tools.extend(self._generate_h_beam_column(col))

        sequence.append({
            "step": 2,
            "name": "기둥 (H형강)",
            "parallel": True,
            "layer": "COLUMN",
            "tools": column_tools
        })

        # Step 3: 트러스 상현재
        truss = coords["truss"]
        top_chord_tools = [
            {
                "tool": "create_line",
                "args": {
                    "start": {"x": truss["top_chord"]["left"]["start"][0],
                             "y": truss["top_chord"]["left"]["start"][1]},
                    "end": {"x": truss["top_chord"]["left"]["end"][0],
                           "y": truss["top_chord"]["left"]["end"][1]},
                    "layer": "BEAM"
                }
            },
            {
                "tool": "create_line",
                "args": {
                    "start": {"x": truss["top_chord"]["right"]["start"][0],
                             "y": truss["top_chord"]["right"]["start"][1]},
                    "end": {"x": truss["top_chord"]["right"]["end"][0],
                           "y": truss["top_chord"]["right"]["end"][1]},
                    "layer": "BEAM"
                }
            }
        ]

        sequence.append({
            "step": 3,
            "name": "트러스 상현재",
            "parallel": True,
            "tools": top_chord_tools
        })

        # Step 4: 트러스 하현재
        sequence.append({
            "step": 4,
            "name": "트러스 하현재",
            "parallel": False,
            "tools": [{
                "tool": "create_line",
                "args": {
                    "start": {"x": truss["bottom_chord"]["start"][0],
                             "y": truss["bottom_chord"]["start"][1]},
                    "end": {"x": truss["bottom_chord"]["end"][0],
                           "y": truss["bottom_chord"]["end"][1]},
                    "layer": "BEAM"
                }
            }]
        })

        # Step 5: 수직 웹부재
        vertical_tools = []
        for vw in truss["vertical_webs"]:
            vertical_tools.append({
                "tool": "create_line",
                "args": {
                    "start": {"x": vw["x"], "y": vw["bottom_y"]},
                    "end": {"x": vw["x"], "y": vw["top_y"]},
                    "layer": "BEAM"
                }
            })

        sequence.append({
            "step": 5,
            "name": "트러스 수직 웹부재",
            "parallel": True,
            "tools": vertical_tools
        })

        # Step 6: 대각 웹부재
        diagonal_tools = []
        for dw in truss["diagonal_webs"]:
            diagonal_tools.append({
                "tool": "create_line",
                "args": {
                    "start": {"x": dw["start"][0], "y": dw["start"][1]},
                    "end": {"x": dw["end"][0], "y": dw["end"][1]},
                    "layer": "BEAM"
                }
            })

        sequence.append({
            "step": 6,
            "name": "트러스 대각 웹부재",
            "parallel": True,
            "tools": diagonal_tools
        })

        # Step 7: 퍼린
        purlin_tools = []
        for p in coords["purlins"]:
            # 짧은 수평선으로 표현
            purlin_tools.append({
                "tool": "create_line",
                "args": {
                    "start": {"x": p["x"] - 20, "y": p["y"]},
                    "end": {"x": p["x"] + 20, "y": p["y"]},
                    "layer": "PURLIN"
                }
            })

        sequence.append({
            "step": 7,
            "name": "퍼린",
            "parallel": True,
            "tools": purlin_tools
        })

        # Step 8: 수평보
        bracing_tools = []
        for hb in coords["bracing"]["horizontal_beams"]:
            bracing_tools.append({
                "tool": "create_line",
                "args": {
                    "start": {"x": hb["start_x"], "y": hb["y"]},
                    "end": {"x": hb["end_x"], "y": hb["y"]},
                    "layer": "BRACING"
                }
            })

        if bracing_tools:
            sequence.append({
                "step": 8,
                "name": "수평보/가새",
                "parallel": True,
                "tools": bracing_tools
            })

        # Step 9: 볼트 심볼 (L2 이상)
        if level in ["L2_structural", "L3_detailed"]:
            bolt_tools = self._generate_bolt_symbols(coords)
            if bolt_tools:
                sequence.append({
                    "step": 9,
                    "name": "볼트 심볼",
                    "parallel": True,
                    "tools": bolt_tools
                })

        return sequence

    def _generate_h_beam_column(self, col: Dict) -> List[Dict]:
        """H형강 기둥 LINE 생성"""
        cx = col["center_x"]
        w = col["width"]
        by = col["bottom_y"]
        ty = col["top_y"]

        fw = w  # 플랜지 너비
        wt = w * 0.15  # 웹 두께

        return [
            # 좌측 플랜지
            {"tool": "create_line", "args": {
                "start": {"x": cx - fw/2, "y": by},
                "end": {"x": cx - fw/2, "y": ty},
                "layer": "COLUMN"
            }},
            # 우측 플랜지
            {"tool": "create_line", "args": {
                "start": {"x": cx + fw/2, "y": by},
                "end": {"x": cx + fw/2, "y": ty},
                "layer": "COLUMN"
            }},
            # 웹 좌
            {"tool": "create_line", "args": {
                "start": {"x": cx - wt/2, "y": by},
                "end": {"x": cx - wt/2, "y": ty},
                "layer": "COLUMN"
            }},
            # 웹 우
            {"tool": "create_line", "args": {
                "start": {"x": cx + wt/2, "y": by},
                "end": {"x": cx + wt/2, "y": ty},
                "layer": "COLUMN"
            }},
            # 하단 플랜지 연결
            {"tool": "create_line", "args": {
                "start": {"x": cx - fw/2, "y": by},
                "end": {"x": cx + fw/2, "y": by},
                "layer": "COLUMN"
            }},
            {"tool": "create_line", "args": {
                "start": {"x": cx - fw/2, "y": by + w*0.1},
                "end": {"x": cx + fw/2, "y": by + w*0.1},
                "layer": "COLUMN"
            }},
            # 상단 플랜지 연결
            {"tool": "create_line", "args": {
                "start": {"x": cx - fw/2, "y": ty},
                "end": {"x": cx + fw/2, "y": ty},
                "layer": "COLUMN"
            }},
            {"tool": "create_line", "args": {
                "start": {"x": cx - fw/2, "y": ty - w*0.1},
                "end": {"x": cx + fw/2, "y": ty - w*0.1},
                "layer": "COLUMN"
            }}
        ]

    def _generate_bolt_symbols(self, coords: Dict) -> List[Dict]:
        """볼트 심볼 생성"""
        bolts = []

        # 기둥 베이스 볼트
        for col in coords["columns"]["list"]:
            bolts.append({
                "tool": "create_bolt_symbol",
                "args": {
                    "center": {"x": col["center_x"], "y": col["bottom_y"] + 10},
                    "diameter": 15,
                    "layer": "BOLT"
                }
            })

        # 처마 연결부 볼트
        for col in coords["columns"]["list"]:
            bolts.append({
                "tool": "create_bolt_symbol",
                "args": {
                    "center": {"x": col["center_x"], "y": coords["roof"]["eave_y"]},
                    "diameter": 15,
                    "layer": "BOLT"
                }
            })

        # 용마루 볼트
        bolts.append({
            "tool": "create_bolt_symbol",
            "args": {
                "center": {"x": coords["roof"]["ridge_x"], "y": coords["roof"]["ridge_y"] - 10},
                "diameter": 15,
                "layer": "BOLT"
            }
        })

        return bolts

    # ========== 5. 검증 ==========

    def verify_result(self, actual_counts: Dict) -> Dict:
        """결과 검증"""
        if not self.analysis:
            return {"error": "No analysis data"}

        expected = {
            "columns": self.analysis.columns_left + self.analysis.columns_right + self.analysis.columns_middle,
            "truss_panels": self.analysis.truss_panels,
            "purlins": self.analysis.purlins_per_slope * 2,
            "vertical_webs": self.analysis.vertical_webs,
            "diagonal_webs": self.analysis.diagonal_webs
        }

        issues = []
        for key, exp_val in expected.items():
            if key in actual_counts:
                actual = actual_counts[key]
                diff = abs(actual - exp_val)
                tolerance = max(1, exp_val * 0.1)  # 10% 또는 최소 1
                if diff > tolerance:
                    issues.append(f"{key}: expected {exp_val}, got {actual}")

        return {
            "passed": len(issues) == 0,
            "expected": expected,
            "actual": actual_counts,
            "issues": issues
        }


# ========== CLI 함수 ==========

def get_checklist() -> str:
    """분석 체크리스트 반환"""
    analyzer = ImageAnalyzer()
    return json.dumps(analyzer.get_analysis_checklist(), ensure_ascii=False, indent=2)


def get_prompt(stage: int) -> str:
    """단계별 프롬프트 반환"""
    analyzer = ImageAnalyzer()
    return analyzer.get_analysis_prompt(stage)


def save_analysis(analysis_json: str) -> str:
    """분석 결과 저장"""
    try:
        analyzer = ImageAnalyzer()
        data = json.loads(analysis_json)
        analysis_id = analyzer.save_analysis(data)
        return json.dumps({"success": True, "analysis_id": analysis_id})
    except Exception as e:
        return json.dumps({"error": str(e)})


def calculate_coords(analysis_id: str, width: float = 800,
                     height: float = 500, margin: float = 50) -> str:
    """좌표 계산"""
    try:
        analyzer = ImageAnalyzer()
        analyzer.load_analysis(analysis_id)
        coords = analyzer.calculate_coordinates(width, height, margin)
        return json.dumps(coords, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


def generate_sequence(analysis_id: str, detail_level: str = "L2_structural") -> str:
    """시퀀스 생성"""
    try:
        analyzer = ImageAnalyzer()
        analyzer.load_analysis(analysis_id)
        analyzer.calculate_coordinates()
        sequence = analyzer.generate_drawing_sequence(detail_level)
        return json.dumps(sequence, ensure_ascii=False, indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python image_analyzer.py checklist")
        print("  python image_analyzer.py prompt <stage>")
        print("  python image_analyzer.py save '<analysis_json>'")
        print("  python image_analyzer.py coords <analysis_id> [width] [height]")
        print("  python image_analyzer.py sequence <analysis_id> [detail_level]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "checklist":
        print(get_checklist())
    elif cmd == "prompt" and len(sys.argv) > 2:
        print(get_prompt(int(sys.argv[2])))
    elif cmd == "save" and len(sys.argv) > 2:
        print(save_analysis(sys.argv[2]))
    elif cmd == "coords" and len(sys.argv) > 2:
        w = float(sys.argv[3]) if len(sys.argv) > 3 else 800
        h = float(sys.argv[4]) if len(sys.argv) > 4 else 500
        print(calculate_coords(sys.argv[2], w, h))
    elif cmd == "sequence" and len(sys.argv) > 2:
        level = sys.argv[3] if len(sys.argv) > 3 else "L2_structural"
        print(generate_sequence(sys.argv[2], level))
    else:
        print(json.dumps({"error": f"Unknown command: {cmd}"}))

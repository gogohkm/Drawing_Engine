"""
신호등 프리캐스트 콘크리트 기초 구조검토 프로그램
Traffic Signal Foundation Structural Analysis

기준: ACI 318-25, 토질역학 일반 원리
작성: Claude Code

검토 항목:
1. 기초 자중 및 제원
2. 지압 강도 (Bearing Strength)
3. 수동토압 (Passive Earth Pressure)
4. 전도 안정성 (Overturning Stability)
5. 활동 안정성 (Sliding Stability)
"""

import math
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FoundationInput:
    """기초 입력 데이터"""
    # 기초 치수 (mm → m 변환하여 사용)
    B_top: float       # 상부 폭 (m)
    B_bot: float       # 하부 폭 (m)
    H_found: float     # 기초 높이 (m)
    D_embed: float     # 매립 깊이 (m)

    # 재료 물성
    fc: float          # 콘크리트 설계기준강도 (MPa)
    gamma_c: float     # 콘크리트 단위중량 (kN/m³)

    # 토질 조건
    gamma_soil: float  # 흙의 단위중량 (kN/m³)
    phi_soil: float    # 흙의 내부마찰각 (도)
    c_soil: float      # 흙의 점착력 (kPa)

    # 하중 조건
    H_wind: float      # 수평 풍하중 (kN)
    h_load: float      # 지표면 위 하중 작용점 높이 (m)
    W_pole: float      # 신호등 기둥 + 신호등 자중 (kN)

    # 베이스 플레이트
    A1_plate: float    # 베이스 플레이트 면적 (m²)

    # 안전율 기준
    FS_overturn: float = 1.5   # 전도 안전율
    FS_sliding: float = 1.5    # 활동 안전율
    FS_bearing: float = 3.0    # 지지력 안전율

    # 프로젝트 정보
    project_name: str = "신호등 기초 구조검토"
    location: str = ""
    engineer: str = ""


class SignalFoundationAnalysis:
    """신호등 기초 구조검토 클래스"""

    def __init__(self, inp: FoundationInput):
        self.inp = inp
        self.results = {}
        self.report_lines = []

    def add_line(self, text: str = ""):
        """보고서에 라인 추가"""
        self.report_lines.append(text)

    def add_section(self, title: str):
        """보고서에 섹션 추가"""
        self.add_line("")
        self.add_line(f"## {title}")
        self.add_line("")

    def add_subsection(self, title: str):
        """보고서에 서브섹션 추가"""
        self.add_line("")
        self.add_line(f"### {title}")
        self.add_line("")

    def calc_foundation_volume(self) -> float:
        """역사다리꼴 기초 체적 계산 (절두체 공식)"""
        B_top = self.inp.B_top
        B_bot = self.inp.B_bot
        H = self.inp.H_found

        # 정사각형 단면 가정
        A_top = B_top ** 2
        A_bot = B_bot ** 2

        # 절두체 체적 공식
        V = (H / 3) * (A_top + A_bot + math.sqrt(A_top * A_bot))

        return V

    def calc_foundation_weight(self) -> float:
        """기초 자중 계산"""
        V = self.calc_foundation_volume()
        W = V * self.inp.gamma_c
        return W

    def calc_centroid_height(self) -> float:
        """기초 하부로부터 무게중심 높이 계산"""
        B_top = self.inp.B_top
        B_bot = self.inp.B_bot
        H = self.inp.H_found

        # 절두체 무게중심 공식
        numerator = H * (B_top**2 + 2*B_top*B_bot + 3*B_bot**2)
        denominator = 4 * (B_top**2 + B_top*B_bot + B_bot**2)

        z_bar = numerator / denominator

        return z_bar

    def calc_passive_earth_pressure_coef(self) -> float:
        """수동토압 계수 계산 (Rankine 이론)"""
        phi_rad = math.radians(self.inp.phi_soil)
        Kp = math.tan(math.pi/4 + phi_rad/2) ** 2
        return Kp

    def calc_passive_earth_pressure(self) -> tuple:
        """수동토압 합력 및 작용점 계산"""
        Kp = self.calc_passive_earth_pressure_coef()
        gamma = self.inp.gamma_soil
        D = self.inp.D_embed

        # 평균 폭 (역사다리꼴 매립부)
        # 매립부에서의 폭 계산 (선형 보간)
        ratio = D / self.inp.H_found
        B_at_surface = self.inp.B_bot + (self.inp.B_top - self.inp.B_bot) * (1 - ratio)
        B_avg = (B_at_surface + self.inp.B_bot) / 2

        # 수동토압 합력 (삼각형 분포)
        # 양쪽 측면에서 작용
        Pp = 0.5 * Kp * gamma * D**2 * B_avg * 2  # 양쪽

        # 작용점 (기초 하부로부터 D/3)
        z_p = D / 3

        return Pp, z_p, Kp, B_avg

    def calc_bearing_strength(self) -> tuple:
        """지압 강도 검토 (ACI 318-25 Section 22.8)"""
        fc = self.inp.fc  # MPa
        A1 = self.inp.A1_plate  # m²

        # A2 계산 (1:2 경사 피라미드)
        # 상부에서 하부로 1:2 경사로 확대
        # 기초 상부 폭 내에서 A2 결정
        spread = 2 * self.inp.H_found  # 1:2 경사 확대량 (양쪽)
        B_A2 = math.sqrt(A1) + spread
        B_A2 = min(B_A2, self.inp.B_bot)  # 기초 하부폭 이하로 제한
        A2 = B_A2 ** 2

        # 공칭 지압 강도 (MPa → kN/m² 변환: 1 MPa = 1000 kN/m²)
        fc_kPa = fc * 1000  # kPa = kN/m²

        ratio = math.sqrt(A2 / A1)
        ratio = min(ratio, 2.0)  # 최대 2.0 제한

        Bn_a = ratio * 0.85 * fc_kPa * A1  # kN
        Bn_b = 2.0 * 0.85 * fc_kPa * A1    # kN
        Bn = min(Bn_a, Bn_b)

        # 설계 지압 강도
        phi = 0.65
        phi_Bn = phi * Bn

        return Bn, phi_Bn, A1, A2, ratio

    def calc_overturning(self) -> dict:
        """전도 안정성 검토"""
        # 기초 자중
        W_found = self.calc_foundation_weight()

        # 전체 자중
        W_total = W_found + self.inp.W_pole

        # 토피하중 (매립부 상부 토사 중량)
        # 간략화: 기초 상부면적 × 매립깊이 위 토사 (기초 측면 토사)
        V_soil = (self.inp.B_bot**2 - self.inp.B_top**2) * self.inp.D_embed * 0.5
        W_soil = V_soil * self.inp.gamma_soil

        # 총 연직하중
        W_total_with_soil = W_total + W_soil

        # 수동토압
        Pp, z_p, Kp, B_avg = self.calc_passive_earth_pressure()

        # 전도 모멘트 (기초 하부 모서리 기준)
        M_OT = self.inp.H_wind * (self.inp.h_load + self.inp.D_embed)

        # 저항 모멘트
        # 1) 자중에 의한 모멘트 (하부폭의 절반)
        x_c = self.inp.B_bot / 2
        M_W = W_total_with_soil * x_c

        # 2) 수동토압에 의한 모멘트
        M_Pp = Pp * z_p

        # 총 저항 모멘트
        M_R = M_W + M_Pp

        # 안전율
        FS = M_R / M_OT if M_OT > 0 else float('inf')

        return {
            'W_found': W_found,
            'W_pole': self.inp.W_pole,
            'W_soil': W_soil,
            'W_total': W_total_with_soil,
            'Pp': Pp,
            'z_p': z_p,
            'Kp': Kp,
            'B_avg': B_avg,
            'M_OT': M_OT,
            'M_W': M_W,
            'M_Pp': M_Pp,
            'M_R': M_R,
            'FS': FS
        }

    def calc_sliding(self) -> dict:
        """활동 안정성 검토"""
        # 연직하중
        ot = self.calc_overturning()
        W_total = ot['W_total']

        # 마찰 저항력
        phi_rad = math.radians(self.inp.phi_soil)
        mu = math.tan(phi_rad)  # 마찰계수

        # 기초 저면 마찰력
        F_friction = mu * W_total

        # 점착력에 의한 저항 (기초 저면)
        A_base = self.inp.B_bot ** 2
        F_cohesion = self.inp.c_soil * A_base

        # 수동토압 저항
        Pp = ot['Pp']

        # 총 활동 저항력
        F_resist = F_friction + F_cohesion + Pp

        # 활동력 (수평하중)
        F_slide = self.inp.H_wind

        # 안전율
        FS = F_resist / F_slide if F_slide > 0 else float('inf')

        return {
            'W_total': W_total,
            'mu': mu,
            'F_friction': F_friction,
            'F_cohesion': F_cohesion,
            'Pp': Pp,
            'F_resist': F_resist,
            'F_slide': F_slide,
            'FS': FS
        }

    def calc_bearing_pressure(self) -> dict:
        """지반 지지력 검토 (편심 고려)"""
        ot = self.calc_overturning()

        W_total = ot['W_total']
        M_net = ot['M_OT'] - ot['M_Pp']  # 순 모멘트 (토압 저항 고려)

        # 편심
        e = M_net / W_total if W_total > 0 else 0

        B = self.inp.B_bot

        # 유효폭
        B_eff = B - 2 * e

        # 지반 반력 (사다리꼴 분포 가정)
        A_eff = B_eff * B  # 유효 면적

        if e <= B / 6:
            # 전면 압축
            q_max = (W_total / (B * B)) * (1 + 6 * e / B)
            q_min = (W_total / (B * B)) * (1 - 6 * e / B)
        else:
            # 부분 압축 (인장 발생)
            q_max = 2 * W_total / (3 * (B/2 - e) * B)
            q_min = 0

        return {
            'W_total': W_total,
            'M_net': M_net,
            'e': e,
            'e_limit': B / 6,
            'B_eff': B_eff,
            'q_max': q_max,
            'q_min': q_min,
            'is_full_compression': e <= B / 6
        }

    def generate_report(self) -> str:
        """구조검토 보고서 생성"""
        self.report_lines = []
        inp = self.inp

        # 헤더
        self.add_line("# 신호등 프리캐스트 콘크리트 기초 구조검토 보고서")
        self.add_line("")
        self.add_line("---")
        self.add_line("")

        # 프로젝트 정보
        self.add_section("1. 개요")
        self.add_line(f"| 항목 | 내용 |")
        self.add_line(f"|------|------|")
        self.add_line(f"| 프로젝트명 | {inp.project_name} |")
        self.add_line(f"| 위치 | {inp.location} |")
        self.add_line(f"| 검토자 | {inp.engineer} |")
        self.add_line(f"| 검토일자 | {datetime.now().strftime('%Y-%m-%d')} |")
        self.add_line(f"| 적용기준 | ACI 318-25, 토질역학 일반 |")

        # 설계 조건
        self.add_section("2. 설계 조건")

        self.add_subsection("2.1 기초 제원")
        self.add_line("```")
        self.add_line(f"              +--- {inp.B_top*1000:.0f} mm ---+")
        self.add_line(f"              |               |")
        self.add_line(f"             /                 \\")
        self.add_line(f"   {inp.H_found*1000:.0f} mm   /                   \\")
        self.add_line(f"           /                     \\")
        self.add_line(f"          +--- {inp.B_bot*1000:.0f} mm ---------+")
        self.add_line("```")
        self.add_line("")
        self.add_line(f"| 항목 | 값 | 단위 |")
        self.add_line(f"|------|-----|------|")
        self.add_line(f"| 상부 폭 (B_top) | {inp.B_top*1000:.0f} | mm |")
        self.add_line(f"| 하부 폭 (B_bot) | {inp.B_bot*1000:.0f} | mm |")
        self.add_line(f"| 기초 높이 (H) | {inp.H_found*1000:.0f} | mm |")
        self.add_line(f"| 매립 깊이 (D) | {inp.D_embed*1000:.0f} | mm |")

        self.add_subsection("2.2 재료 물성")
        self.add_line(f"| 항목 | 값 | 단위 |")
        self.add_line(f"|------|-----|------|")
        self.add_line(f"| 콘크리트 강도 (f'c) | {inp.fc:.1f} | MPa |")
        self.add_line(f"| 콘크리트 단위중량 (γc) | {inp.gamma_c:.1f} | kN/m³ |")

        self.add_subsection("2.3 토질 조건")
        self.add_line(f"| 항목 | 값 | 단위 |")
        self.add_line(f"|------|-----|------|")
        self.add_line(f"| 흙의 단위중량 (γ) | {inp.gamma_soil:.1f} | kN/m³ |")
        self.add_line(f"| 내부마찰각 (φ') | {inp.phi_soil:.1f} | ° |")
        self.add_line(f"| 점착력 (c) | {inp.c_soil:.1f} | kPa |")

        self.add_subsection("2.4 하중 조건")
        self.add_line(f"| 항목 | 값 | 단위 |")
        self.add_line(f"|------|-----|------|")
        self.add_line(f"| 수평 풍하중 (H) | {inp.H_wind:.2f} | kN |")
        self.add_line(f"| 하중 작용점 높이 (h) | {inp.h_load*1000:.0f} | mm |")
        self.add_line(f"| 상부 구조물 자중 (W_pole) | {inp.W_pole:.2f} | kN |")

        # 기초 자중 계산
        self.add_section("3. 기초 자중 계산")

        V = self.calc_foundation_volume()
        W_found = self.calc_foundation_weight()
        z_bar = self.calc_centroid_height()

        self.add_line("**절두체 체적 공식:**")
        self.add_line("")
        self.add_line("$$V = \\frac{H}{3}\\left(A_{top} + A_{bot} + \\sqrt{A_{top} \\times A_{bot}}\\right)$$")
        self.add_line("")

        A_top = inp.B_top ** 2
        A_bot = inp.B_bot ** 2

        self.add_line("**계산:**")
        self.add_line("")
        self.add_line(f"- $A_{{top}} = {inp.B_top:.3f}^2 = {A_top:.4f}$ m²")
        self.add_line(f"- $A_{{bot}} = {inp.B_bot:.3f}^2 = {A_bot:.4f}$ m²")
        self.add_line(f"- $\\sqrt{{A_{{top}} \\times A_{{bot}}}} = \\sqrt{{{A_top:.4f} \\times {A_bot:.4f}}} = {math.sqrt(A_top*A_bot):.4f}$ m²")
        self.add_line("")
        self.add_line(f"$$V = \\frac{{{inp.H_found:.3f}}}{{3}} \\times ({A_top:.4f} + {A_bot:.4f} + {math.sqrt(A_top*A_bot):.4f}) = {V:.4f} \\text{{ m}}^3$$")
        self.add_line("")
        self.add_line(f"$$W_{{found}} = V \\times \\gamma_c = {V:.4f} \\times {inp.gamma_c:.1f} = {W_found:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line(f"**무게중심 높이 (기초 하부로부터):** $\\bar{{z}} = {z_bar:.4f}$ m = {z_bar*1000:.1f} mm")

        # 지압 강도 검토
        self.add_section("4. 지압 강도 검토 (ACI 318-25 Section 22.8)")

        Bn, phi_Bn, A1, A2, ratio = self.calc_bearing_strength()

        self.add_line("**적용 공식:**")
        self.add_line("")
        self.add_line("$$\\phi B_n \\geq B_u$$")
        self.add_line("")
        self.add_line("$$B_n = \\min\\left[\\sqrt{\\frac{A_2}{A_1}} \\times 0.85 f'_c A_1, \\; 2 \\times 0.85 f'_c A_1\\right]$$")
        self.add_line("")

        self.add_line("**계산:**")
        self.add_line("")
        self.add_line(f"- 재하 면적: $A_1 = {A1:.4f}$ m² = {A1*1e6:.0f} mm²")
        self.add_line(f"- 확대 면적: $A_2 = {A2:.4f}$ m² = {A2*1e6:.0f} mm²")
        self.add_line(f"- 면적비: $\\sqrt{{A_2/A_1}} = {ratio:.3f}$ (≤ 2.0)")
        self.add_line("")

        fc_kPa = inp.fc * 1000
        self.add_line(f"$$B_n = \\min[{ratio:.3f} \\times 0.85 \\times {fc_kPa:.0f} \\times {A1:.4f}, \\; 2.0 \\times 0.85 \\times {fc_kPa:.0f} \\times {A1:.4f}]$$")
        self.add_line("")
        self.add_line(f"$$B_n = \\min[{ratio * 0.85 * fc_kPa * A1:.2f}, \\; {2.0 * 0.85 * fc_kPa * A1:.2f}] = {Bn:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line(f"$$\\phi B_n = 0.65 \\times {Bn:.2f} = {phi_Bn:.2f} \\text{{ kN}}$$")
        self.add_line("")

        # 작용 지압력
        Bu = W_found + inp.W_pole
        self.add_line(f"**작용 지압력:** $B_u = W_{{found}} + W_{{pole}} = {W_found:.2f} + {inp.W_pole:.2f} = {Bu:.2f}$ kN")
        self.add_line("")

        bearing_ok = phi_Bn >= Bu
        self.add_line("**판정:**")
        self.add_line("")
        geq_sign = "\\geq" if bearing_ok else "<"
        result_text = "O.K" if bearing_ok else "N.G"
        self.add_line(f"$$\\phi B_n = {phi_Bn:.2f} \\text{{ kN}} {geq_sign} B_u = {Bu:.2f} \\text{{ kN}} \\quad \\therefore \\textbf{{{result_text}}}$$")

        # 수동토압 계산
        self.add_section("5. 수동토압 계산")

        Pp, z_p, Kp, B_avg = self.calc_passive_earth_pressure()

        self.add_subsection("5.1 수동토압 계수 (Rankine 이론)")
        self.add_line("")
        self.add_line("$$K_p = \\tan^2\\left(45° + \\frac{\\phi'}{2}\\right)$$")
        self.add_line("")
        self.add_line(f"$$K_p = \\tan^2\\left(45° + \\frac{{{inp.phi_soil:.1f}°}}{{2}}\\right) = \\tan^2({45 + inp.phi_soil/2:.2f}°) = {Kp:.3f}$$")
        self.add_line("")

        self.add_subsection("5.2 수동토압 합력")
        self.add_line("")
        self.add_line("```")
        self.add_line("    Ground ============================")
        self.add_line("              |")
        self.add_line("              |<-- sigma_p = Kp x gamma x z")
        self.add_line("              |  \\")
        self.add_line(f"         D={inp.D_embed*1000:.0f}mm|    \\  Triangular Distribution")
        self.add_line("              |      \\")
        self.add_line("              |        \\")
        self.add_line("    Base -----+----------\\-")
        self.add_line("```")
        self.add_line("")
        self.add_line("**합력 공식 (양쪽 측면):**")
        self.add_line("")
        self.add_line("$$P_p = 2 \\times \\frac{1}{2} K_p \\gamma D^2 B_{avg}$$")
        self.add_line("")
        self.add_line(f"- 평균 폭: $B_{{avg}} = {B_avg:.3f}$ m")
        self.add_line(f"- 매립 깊이: $D = {inp.D_embed:.3f}$ m")
        self.add_line("")
        self.add_line(f"$$P_p = {Kp:.3f} \\times {inp.gamma_soil:.1f} \\times {inp.D_embed:.3f}^2 \\times {B_avg:.3f} = {Pp:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line(f"**작용점 (기초 하부로부터):** $z_p = D/3 = {inp.D_embed:.3f}/3 = {z_p:.3f}$ m = {z_p*1000:.1f} mm")

        # 전도 안정성 검토
        self.add_section("6. 전도 안정성 검토")

        ot = self.calc_overturning()

        self.add_line("```")
        self.add_line(f"                    H = {inp.H_wind:.2f} kN")
        self.add_line("                    <-------")
        self.add_line("                    |")
        self.add_line(f"                    | h = {inp.h_load*1000:.0f} mm")
        self.add_line("                    |")
        self.add_line("    ================+================ GL")
        self.add_line("         |          |          |")
        self.add_line(f"         |  D={inp.D_embed*1000:.0f}mm |          |")
        self.add_line("         |          |          |")
        self.add_line("    -----+----------+----------+----- Foundation Base")
        self.add_line("         ^          |          ^")
        self.add_line("        Pp      Rotation Pt")
        self.add_line("```")
        self.add_line("")

        self.add_subsection("6.1 하중 산정")
        self.add_line("")
        self.add_line(f"| 항목 | 계산 | 값 (kN) |")
        self.add_line(f"|------|------|---------|")
        self.add_line(f"| 기초 자중 | $W_{{found}}$ | {ot['W_found']:.2f} |")
        self.add_line(f"| 상부 구조물 | $W_{{pole}}$ | {ot['W_pole']:.2f} |")
        self.add_line(f"| 토피하중 | $W_{{soil}}$ | {ot['W_soil']:.2f} |")
        self.add_line(f"| **총 연직하중** | $W_{{total}}$ | **{ot['W_total']:.2f}** |")
        self.add_line("")

        self.add_subsection("6.2 전도 모멘트")
        self.add_line("")
        self.add_line("$$M_{OT} = H \\times (h + D)$$")
        self.add_line("")
        self.add_line(f"$$M_{{OT}} = {inp.H_wind:.2f} \\times ({inp.h_load:.3f} + {inp.D_embed:.3f}) = {inp.H_wind:.2f} \\times {inp.h_load + inp.D_embed:.3f}$$")
        self.add_line("")
        self.add_line(f"$$M_{{OT}} = {ot['M_OT']:.2f} \\text{{ kN·m}}$$")
        self.add_line("")

        self.add_subsection("6.3 저항 모멘트")
        self.add_line("")
        self.add_line("**1) 자중에 의한 저항 모멘트:**")
        self.add_line("")
        self.add_line(f"$$M_W = W_{{total}} \\times \\frac{{B}}{{2}} = {ot['W_total']:.2f} \\times \\frac{{{inp.B_bot:.3f}}}{{2}} = {ot['M_W']:.2f} \\text{{ kN·m}}$$")
        self.add_line("")
        self.add_line("**2) 수동토압에 의한 저항 모멘트:**")
        self.add_line("")
        self.add_line(f"$$M_{{Pp}} = P_p \\times \\frac{{D}}{{3}} = {ot['Pp']:.2f} \\times {ot['z_p']:.3f} = {ot['M_Pp']:.2f} \\text{{ kN·m}}$$")
        self.add_line("")
        self.add_line("**3) 총 저항 모멘트:**")
        self.add_line("")
        self.add_line(f"$$M_R = M_W + M_{{Pp}} = {ot['M_W']:.2f} + {ot['M_Pp']:.2f} = {ot['M_R']:.2f} \\text{{ kN·m}}$$")
        self.add_line("")

        self.add_subsection("6.4 전도 안전율")
        self.add_line("")
        self.add_line(f"$$F.S._{{전도}} = \\frac{{M_R}}{{M_{{OT}}}} = \\frac{{{ot['M_R']:.2f}}}{{{ot['M_OT']:.2f}}} = {ot['FS']:.2f}$$")
        self.add_line("")

        ot_ok = ot['FS'] >= inp.FS_overturn
        geq_sign = "\\geq" if ot_ok else "<"
        result_text = "O.K" if ot_ok else "N.G"
        self.add_line(f"$$F.S. = {ot['FS']:.2f} {geq_sign} {inp.FS_overturn:.1f} \\quad \\therefore \\textbf{{{result_text}}}$$")

        # 활동 안정성 검토
        self.add_section("7. 활동 안정성 검토")

        sl = self.calc_sliding()

        self.add_subsection("7.1 활동 저항력")
        self.add_line("")
        self.add_line("**1) 마찰 저항력:**")
        self.add_line("")
        self.add_line(f"$$\\mu = \\tan\\phi' = \\tan({inp.phi_soil:.1f}°) = {sl['mu']:.3f}$$")
        self.add_line("")
        self.add_line(f"$$F_{{friction}} = \\mu \\times W_{{total}} = {sl['mu']:.3f} \\times {sl['W_total']:.2f} = {sl['F_friction']:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line("**2) 점착력에 의한 저항:**")
        self.add_line("")
        A_base = inp.B_bot ** 2
        self.add_line(f"$$F_{{cohesion}} = c \\times A_{{base}} = {inp.c_soil:.1f} \\times {A_base:.4f} = {sl['F_cohesion']:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line("**3) 수동토압 저항:**")
        self.add_line("")
        self.add_line(f"$$P_p = {sl['Pp']:.2f} \\text{{ kN}}$$")
        self.add_line("")
        self.add_line("**4) 총 활동 저항력:**")
        self.add_line("")
        self.add_line(f"$$F_{{resist}} = F_{{friction}} + F_{{cohesion}} + P_p = {sl['F_friction']:.2f} + {sl['F_cohesion']:.2f} + {sl['Pp']:.2f} = {sl['F_resist']:.2f} \\text{{ kN}}$$")
        self.add_line("")

        self.add_subsection("7.2 활동 안전율")
        self.add_line("")
        self.add_line(f"$$F.S._{{활동}} = \\frac{{F_{{resist}}}}{{H}} = \\frac{{{sl['F_resist']:.2f}}}{{{sl['F_slide']:.2f}}} = {sl['FS']:.2f}$$")
        self.add_line("")

        sl_ok = sl['FS'] >= inp.FS_sliding
        geq_sign = "\\geq" if sl_ok else "<"
        result_text = "O.K" if sl_ok else "N.G"
        self.add_line(f"$$F.S. = {sl['FS']:.2f} {geq_sign} {inp.FS_sliding:.1f} \\quad \\therefore \\textbf{{{result_text}}}$$")

        # 지반 반력 검토
        self.add_section("8. 지반 반력 검토")

        bp = self.calc_bearing_pressure()

        self.add_subsection("8.1 편심 계산")
        self.add_line("")
        self.add_line(f"$$e = \\frac{{M_{{net}}}}{{W_{{total}}}} = \\frac{{{bp['M_net']:.2f}}}{{{bp['W_total']:.2f}}} = {bp['e']:.4f} \\text{{ m}} = {bp['e']*1000:.1f} \\text{{ mm}}$$")
        self.add_line("")
        self.add_line(f"$$e_{{limit}} = \\frac{{B}}{{6}} = \\frac{{{inp.B_bot:.3f}}}{{6}} = {bp['e_limit']:.4f} \\text{{ m}} = {bp['e_limit']*1000:.1f} \\text{{ mm}}$$")
        self.add_line("")

        if bp['is_full_compression']:
            self.add_line(f"$$e = {bp['e']*1000:.1f} \\text{{ mm}} \\leq e_{{limit}} = {bp['e_limit']*1000:.1f} \\text{{ mm}} \\quad \\therefore \\text{{전면 압축}}$$")
        else:
            self.add_line(f"$$e = {bp['e']*1000:.1f} \\text{{ mm}} > e_{{limit}} = {bp['e_limit']*1000:.1f} \\text{{ mm}} \\quad \\therefore \\text{{부분 압축 (인장 발생)}}$$")
        self.add_line("")

        self.add_subsection("8.2 지반 반력 분포")
        self.add_line("")
        self.add_line(f"$$q_{{max}} = {bp['q_max']:.2f} \\text{{ kPa}}$$")
        self.add_line(f"$$q_{{min}} = {bp['q_min']:.2f} \\text{{ kPa}}$$")
        self.add_line("")

        # 검토 결과 종합
        self.add_section("9. 검토 결과 종합")
        self.add_line("")
        self.add_line("```")
        self.add_line("+------------------------------------------------------------+")
        self.add_line("|                                                            |")
        self.add_line("|                    REVIEW SUMMARY                          |")
        self.add_line("|                                                            |")
        self.add_line("+------------------------------------------------------------+")

        # 지압 강도
        bearing_status = "O.K" if bearing_ok else "N.G"
        comp_sign = ">=" if bearing_ok else "<"
        self.add_line(f"|  [1] Bearing Strength                                      |")
        self.add_line(f"|      phi*Bn = {phi_Bn:>8.2f} kN {comp_sign} Bu = {Bu:>8.2f} kN  -> {bearing_status:>4} |")
        self.add_line("|                                                            |")

        # 전도 안정성
        ot_status = "O.K" if ot_ok else "N.G"
        comp_sign = ">=" if ot_ok else "<"
        self.add_line(f"|  [2] Overturning Stability                                 |")
        self.add_line(f"|      F.S. = {ot['FS']:>6.2f} {comp_sign} {inp.FS_overturn:>4.1f}                     -> {ot_status:>4} |")
        self.add_line(f"|      (Weight: {ot['M_W']/(ot['M_W']+ot['M_Pp'])*100:>5.1f}%, Passive EP: {ot['M_Pp']/(ot['M_W']+ot['M_Pp'])*100:>5.1f}%)            |")
        self.add_line("|                                                            |")

        # 활동 안정성
        sl_status = "O.K" if sl_ok else "N.G"
        comp_sign = ">=" if sl_ok else "<"
        self.add_line(f"|  [3] Sliding Stability                                     |")
        self.add_line(f"|      F.S. = {sl['FS']:>6.2f} {comp_sign} {inp.FS_sliding:>4.1f}                     -> {sl_status:>4} |")
        self.add_line("|                                                            |")

        # 지반 반력
        eccentricity_status = "Full Comp." if bp['is_full_compression'] else "Partial"
        comp_sign = "<=" if bp['is_full_compression'] else ">"
        self.add_line(f"|  [4] Bearing Pressure                                      |")
        self.add_line(f"|      e = {bp['e']*1000:>6.1f} mm {comp_sign} B/6 = {bp['e_limit']*1000:>6.1f} mm -> {eccentricity_status:>10} |")
        self.add_line(f"|      qmax = {bp['q_max']:>6.2f} kPa, qmin = {bp['q_min']:>6.2f} kPa           |")
        self.add_line("|                                                            |")

        # 종합 판정
        all_ok = bearing_ok and ot_ok and sl_ok
        final_status = "[O.K] ACCEPTABLE" if all_ok else "[N.G] NOT ACCEPTABLE"
        self.add_line("+------------------------------------------------------------+")
        self.add_line("|                                                            |")
        self.add_line(f"|              FINAL RESULT: {final_status:^24}       |")
        self.add_line("|                                                            |")
        self.add_line("+------------------------------------------------------------+")
        self.add_line("```")

        # 서명란
        self.add_line("")
        self.add_line("---")
        self.add_line("")
        self.add_line("| 작성 | 검토 | 승인 |")
        self.add_line("|:----:|:----:|:----:|")
        self.add_line("|      |      |      |")

        return "\n".join(self.report_lines)


def main():
    """메인 실행 함수"""

    # 예제 입력 데이터 (실제 값으로 수정 필요)
    inp = FoundationInput(
        # 기초 치수 (m)
        B_top=0.400,        # 상부 폭 400mm
        B_bot=0.600,        # 하부 폭 600mm
        H_found=0.700,      # 기초 높이 700mm
        D_embed=0.650,      # 매립 깊이 650mm (상부 50mm 노출)

        # 재료 물성
        fc=24.0,            # 콘크리트 강도 24 MPa
        gamma_c=24.0,       # 콘크리트 단위중량 24 kN/m³

        # 토질 조건
        gamma_soil=18.0,    # 흙의 단위중량 18 kN/m³
        phi_soil=30.0,      # 내부마찰각 30°
        c_soil=0.0,         # 점착력 0 kPa (사질토 가정)

        # 하중 조건
        H_wind=2.0,         # 수평 풍하중 2.0 kN
        h_load=6.0,         # 신호등 높이 6.0 m
        W_pole=1.5,         # 신호등 기둥+신호등 자중 1.5 kN

        # 베이스 플레이트
        A1_plate=0.20 * 0.20,  # 200mm x 200mm

        # 안전율 기준
        FS_overturn=1.5,
        FS_sliding=1.5,
        FS_bearing=3.0,

        # 프로젝트 정보
        project_name="신호등 기초 구조검토",
        location="서울시 OO구 OO동",
        engineer="구조기술사 OOO"
    )

    # 분석 실행
    analysis = SignalFoundationAnalysis(inp)
    report = analysis.generate_report()

    # 보고서 출력
    print(report)

    # 파일로 저장
    output_file = "신호등기초_구조검토보고서.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n\n보고서가 '{output_file}'로 저장되었습니다.")


if __name__ == "__main__":
    main()

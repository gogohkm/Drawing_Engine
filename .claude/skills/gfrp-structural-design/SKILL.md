---
name: gfrp-structural-design
description: "ASCE/SEI 74-23 GFRP 구조설계 표준(Specification, Commentary)을 검색하고 구조계산을 수행하며, 설계 워크플로우를 제공합니다. GFRP 복합재료 설계, 펄트루전, 직교이방성, 환경조정계수, 시간효과계수, 연결부 설계 관련 질문에 즉시 활성화되며, 공식 추출, 물성값 조회, 환경보정, 연결부 다중파괴모드 계산을 지원합니다."
---

# GFRP Structural Design Standards Expert

Use this skill when users ask questions about GFRP (Glass Fiber Reinforced Polymer) structural design, ASCE/SEI 74-23 standard, pultruded composites, orthotropic materials, fiber reinforced polymers, or composite structural systems.

## Trigger Keywords

**English**: GFRP, FRP, glass fiber, fiber reinforced polymer, pultruded, pultrusion, ASCE 74, composite structures, orthotropic, anisotropic, time effect factor, environmental factors, bearing strength, creep rupture, laminate, resin matrix

**Korean**: GFRP, FRP, 섬유강화플라스틱, 복합재료, 펄트루전, 펄트루젼, 유리섬유, 직교이방성, 이방성, 시간효과계수, 환경조정계수, 지압강도, 크리프파괴, 적층, 수지매트릭스

## Tools Required

- **Grep**: Search for keywords in ASCE/SEI 74-23 documents
- **Read**: Read specific chapters and reference files
- **Glob**: Pattern matching to find files
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results or reports

## Document Structure

This skill provides access to **comprehensive GFRP design documentation**:

### 1. ASCE/SEI 74-23 Specification (Chapters 1-9)
**Location**: `data/specification/*.md` (5 part files covering 125 pages)

**Purpose**: What you **must** follow - formulas, requirements, limits, design criteria using LRFD method

**Chapters**:
- **Chapter 1**: General Provisions (scope, materials, LRFD basics, load combinations)
- **Chapter 2**: Design Requirements (resistance factors φ, time effect λ, environmental factors C_M/C_T/C_CH, second-order analysis, deflection, fatigue)
- **Chapter 3**: Tension Members (gross section, net section, pin-connected, threaded rods)
- **Chapter 4**: Compression Members (flexural buckling, local flange/web buckling, torsional buckling, effective length)
- **Chapter 5**: Flexural Members & Shear (material rupture, lateral-torsional buckling, web shear, shear buckling, concentrated loads)
- **Chapter 6**: Combined Forces (beam-columns, torsion, interaction equations)
- **Chapter 7**: Plates and Built-Up Members (in-plane loading, open-hole strength, pull-through, two-way bending)
- **Chapter 8**: Bolted Connections (6+ failure modes: bearing, net tension, shear-out, block shear, pull-through, bolt shear)
- **Chapter 9**: Seismic Design (R factors, braced frames, cooling towers)

**Appendices**:
- **Appendix A**: Symbols and Notations (complete variable definitions)
- **Appendix B**: Glossary (technical terms)
- **Appendix C8.3.2**: Multi-row bolted connection full formul as

### 2. Commentary (Chapters C1-C9)
**Location**: Integrated within the 5 part files

**Purpose**: Understand **why** - background, research basis, design philosophy

**Contents**: Detailed commentary for each chapter with:
- Historical development and research citations
- Design examples and comparisons
- Limit state explanations
- Special considerations for GFRP orthotropic behavior
- Reliability basis for resistance factors

### 3. Reference Files
**Location**: `references/` directory (8 comprehensive guides)

This skill includes essential reference materials:

- `symbols.md`: Complete symbols table (150+ variables with units, sections)
- `glossary.md`: Technical terms and definitions (50+ terms)
- `abbreviations.md`: ASTM standards, acronyms, units, conversions
- `chapter-structure.md`: Complete chapter mapping and navigation guide
- `material-properties-guide.md`: **Typical GFRP properties, testing requirements, statistical basis**
- `environmental-factors.md`: **C_M, C_T, C_CH adjustment factors with tables**
- `resistance-factors.md`: **φ values by failure mode (0.50-0.85) with rationale**
- `time-effect-factors.md`: **λ values by load duration (0.60-1.00) with examples**

## Automation Scripts

Python scripts available in `scripts/` directory:
- `smart_search.py`: Category-aware keyword search (maps keywords to chapters)
- `formula_finder.py`: Extract formulas with context (±5 lines)
- `material_lookup.py`: **Property lookup with typical ranges**
- `environmental_adjustment.py`: **Calculate adjusted strengths (F_adjusted = F × C_M × C_T × C_CH)**
- `connection_checker.py`: **Multi-mode connection design helper (6+ failure modes)**

---

# Workflow by Query Type

## 1. Formula Query (공식 질의)

**User Intent**: Find specific formula or equation from ASCE/SEI 74-23 Specification.

**Example Queries**:
- "What is the formula for lateral-torsional buckling of GFRP beams?"
- "Show me the compression buckling equation"
- "GFRP 보의 전단좌굴 공식을 알려줘"

**Quick Process**:
1. Identify topic (flexure → Chapter 5, compression → Chapter 4, connections → Chapter 8, etc.)
2. Grep relevant chapter file in `data/specification/`
3. Extract formula with variable definitions from `references/symbols.md`
4. **Note orthotropic dependency**: Check if formula uses E_L, E_T, G_LT (direction-dependent)
5. **Note environmental factors**: Remind user to apply C_M, C_T, C_CH adjustments
6. Present with ASCE citation (e.g., "ASCE/SEI 74-23 Section 5.2.2")

**GFRP-Specific Considerations**:
- Formulas often include √(E_L × E_T) for orthotropic effects
- Multiple buckling modes must be checked (flexural, local flange, local web, torsional)
- Environmental factors must be applied to all material properties
- Time effect factor λ must be considered for load duration

**Keywords**: formula, equation, 공식, 계산식, buckling, strength

---

## 2. Material Properties Query (물성값 질의 - GFRP-SPECIFIC)

**User Intent**: Find typical GFRP material properties or understand testing requirements.

**Example Queries**:
- "What is typical longitudinal modulus for pultruded GFRP?"
- "What's the difference between E_L and E_T?"
- "GFRP의 전형적인 인장강도는 얼마야?"
- "How do I determine characteristic values?"

**Quick Process**:
1. Check `references/material-properties-guide.md` for quick reference
2. Identify property type (elastic moduli, strengths, thermal)
3. Return typical ranges with caveats:
   - E_L: 2,000-4,000 ksi (14-28 GPa)
   - E_T: 800-1,500 ksi (40-50% of E_L)
   - G_LT: 300-600 ksi (~15% of E_L)
   - F_L^t: 30-50 ksi (210-345 MPa)
   - F_L^c: 20-40 ksi (60-80% of F_L^t)
4. **Emphasize testing requirement**: All properties must be determined per ASTM D6121 or D7290
5. Explain statistical basis (75% confidence, 20% exclusion limit)
6. Note orthotropic behavior (L vs T direction differences)

**Typical GFRP Properties Table**:

| Property | Symbol | Typical Range | L:T Ratio |
|----------|--------|---------------|-----------|
| Long. modulus | E_L | 2,000-4,000 ksi | - |
| Trans. modulus | E_T | 800-1,500 ksi | 2.5:1 |
| Shear modulus | G_LT | 300-600 ksi | - |
| Long. tensile | F_L^t | 30-50 ksi | - |
| Trans. tensile | F_T^t | 5-10 ksi | 5:1 to 8:1 |
| Long. comp | F_L^c | 20-40 ksi | - |
| Shear | F_LT^s | 4-10 ksi | - |
| Poisson's ratio | ν_LT | 0.25-0.35 | - |

**Testing Standards Reference**:
- ASTM D3039: Tensile properties
- ASTM D3410/D695: Compressive properties
- ASTM D5379: Shear properties (V-notched beam)
- ASTM D6121: Characteristic values determination
- ASTM D7290: Filled-hole properties
- ASTM E1640: Glass transition temperature

**Keywords**: properties, modulus, strength, E_L, E_T, testing, characteristic value, 물성, 탄성계수, 강도

---

## 3. Environmental Adjustment Query (환경보정 질의 - GFRP-SPECIFIC)

**User Intent**: Apply environmental factors to adjust material properties for end-use conditions.

**Example Queries**:
- "How does moisture affect GFRP strength?"
- "What C_M factor should I use for wet service?"
- "Calculate adjusted strength for hot, wet, chemical exposure"
- "습윤환경에서 GFRP 강도감소는?"

**Quick Process**:
1. Identify exposure conditions (moisture, temperature, chemicals)
2. Check `references/environmental-factors.md` for factor values
3. Determine appropriate factors:
   - **C_M** (moisture): 0.70-1.00 (dry=1.00, wet=0.75-0.85, immersed=0.70-0.80)
   - **C_T** (temperature): 0.75-1.00 (< 100°F=1.00, check T vs T_g)
   - **C_CH** (chemical): 0.50-1.00 (varies by chemical type and pH)
   - **C_CA** (composite action): 0.60-1.00 (for built-up members)
   - **C_LS** (load sharing): 1.00-1.15 (for multiple parallel members)
4. Apply adjustment formula:
   **F_adjusted = F_reference × C_M × C_T × C_CH × C_CA × C_LS**
5. Use `scripts/environmental_adjustment.py` for automated calculation
6. **Warning**: Combined effects can reduce capacity 30-50%!

**Environmental Factors Quick Table**:

| Condition | C_M | C_T | C_CH | Total Effect |
|-----------|-----|-----|------|--------------|
| Dry, room temp, no chemicals | 1.00 | 1.00 | 1.00 | 100% |
| Wet, 140°F, mild acid | 0.80 | 0.85 | 0.90 | 61% |
| Immersed, 160°F, moderate acid | 0.75 | 0.80 | 0.85 | 51% |

**Critical Reminders**:
- Apply factors to ALL material properties (E_L, E_T, F_L^t, F_L^c, F_LT^s, etc.)
- Test in actual service environment when critical
- Combined hot + wet is worse than sum of individual effects
- Glass transition temperature T_g is absolute limit (typically 180-250°F)

**Keywords**: environmental, moisture, temperature, chemical, C_M, C_T, C_CH, adjustment, wet, 환경, 습기, 온도, 화학

---

## 4. Time Effect Factor Query (시간효과계수 질의 - GFRP-SPECIFIC)

**User Intent**: Apply time effect factor for load duration effects (creep rupture).

**Example Queries**:
- "What λ factor for dead load?"
- "Time effect factor for snow load combination"
- "Why does GFRP have time-dependent strength?"
- "지속하중에 대한 강도감소는?"

**Quick Process**:
1. Identify load duration from load combination
2. Check `references/time-effect-factors.md` for λ values
3. Return appropriate factor:
   - **Permanent (50+ years)**: λ = 0.60 (dead load only)
   - **10 years**: λ = 0.70 (D + L combinations)
   - **2 months**: λ = 0.80 (D + S combinations)
   - **7 days**: λ = 0.90 (D + L_r combinations)
   - **10 minutes**: λ = 1.00 (D + W, D + E combinations)
4. Use **shortest significant duration** in load combination
5. Explain creep rupture mechanism (matrix creep, stress concentrations over time)

**Time Effect Factors Table** (ASCE/SEI 74-23 Table 2-1):

| Load Duration | λ | Typical Loads | Reduction |
|---------------|---|---------------|-----------|
| Permanent (50+ years) | 0.60 | Dead load | 40% |
| 10 years | 0.70 | Live load | 30% |
| 2 months | 0.80 | Snow | 20% |
| 7 days | 0.90 | Roof live | 10% |
| 10 minutes | 1.00 | Wind, seismic | 0% |

**Load Combination Examples**:
- 1.4D → λ = 0.60 (dead only)
- 1.2D + 1.6L → λ = 0.70 (live controls)
- 1.2D + 1.6S → λ = 0.80 (snow controls)
- 1.2D + 1.0W → λ = 1.00 (wind controls)
- 1.2D + 1.0E → λ = 1.00 (seismic controls)

**Design Equation**:
$$R_u \leq \phi \lambda R_n$$

**Combined with φ example**:
- Flexure: φ = 0.75, λ = 0.70 (D+L case)
- Design strength = 0.75 × 0.70 × M_n = **0.525 M_n** (~50% of nominal!)

**Keywords**: time effect, duration, creep, λ, lambda, sustained load, permanent, 시간효과, 지속하중, 크리프

---

## 5. Calculation Query (계산 질의)

**User Intent**: Perform structural calculations using ASCE/SEI 74-23 formulas with GFRP-specific considerations.

**Example Queries**:
- "Calculate lateral-torsional buckling: GFRP I-beam, L_b=10ft, wet service"
- "Determine compression capacity: GFRP tube 6x6x0.375, KL=12ft, hot environment"
- "GFRP 보의 휨강도를 계산해줘: W12x6, 습윤환경, 설하중 조합"

**Quick Process**:
1. **Identify all input parameters**:
   - Section properties (shape, dimensions)
   - Material properties (E_L, E_T, G_LT, F_L^t, F_L^c, F_LT^s)
   - Environmental conditions (wet/dry, temperature, chemicals)
   - Load duration (permanent, 10-year, snow, wind, seismic)
   - Unbraced lengths, boundary conditions
2. **Apply environmental adjustments**:
   - Determine C_M, C_T, C_CH factors
   - Adjust ALL material properties: F_adjusted = F_ref × C_M × C_T × C_CH
3. **Find relevant formula** from Specification (use Formula Query workflow)
4. **Check MULTIPLE limit states** (GFRP often has 3-4 competing modes):
   - Flexure: Material rupture, LTB, local flange buckling, local web buckling
   - Compression: Flexural buckling, local flange, local web, torsional, flexural-torsional
   - Connections: Bearing, net tension, shear-out, block shear, pull-through, bolt shear
5. **Apply resistance factor φ** (varies by failure mode: 0.50-0.85)
6. **Apply time effect factor λ** (varies by load duration: 0.60-1.00)
7. Generate Python code following ASCE examples
8. Execute and validate

**GFRP-Specific Checks (CRITICAL)**:
- ✅ Orthotropic properties specified (E_L, E_T, G_LT all required)
- ✅ Environmental factors applied (C_M, C_T, C_CH)
- ✅ Time effect factor applied (λ)
- ✅ Glass transition temperature verified (T_service < T_g - 20°F)
- ✅ Multiple buckling modes checked
- ✅ Direction of loading identified (longitudinal vs transverse)
- ✅ Serviceability checked (deflection often controls due to low E)

**Example Calculation Framework**:
```python
# GFRP Beam Flexural Strength Calculation
# ASCE/SEI 74-23 Section 5.2

# 1. Material Properties (from testing per ASTM D6121)
E_L = 3000  # ksi, longitudinal modulus
E_T = 1200  # ksi, transverse modulus
G_LT = 450  # ksi, shear modulus
F_Lc = 35  # ksi, longitudinal compressive strength (reference)
F_Lt = 40  # ksi, longitudinal tensile strength (reference)
nu_LT = 0.30  # Poisson's ratio

# 2. Environmental Adjustment Factors (Section 2.4)
C_M = 0.85  # Wet service
C_T = 0.90  # Sustained 130°F
C_CH = 1.00  # No chemicals
# Adjusted strengths
F_Lc_adj = F_Lc * C_M * C_T * C_CH  # = 35 * 0.85 * 0.90 = 26.8 ksi
F_Lt_adj = F_Lt * C_M * C_T * C_CH  # = 40 * 0.85 * 0.90 = 30.6 ksi

# 3. Section Properties
S_x = 15.0  # in^3, section modulus
I_y = 5.0  # in^4, weak axis moment of inertia
J = 0.5  # in^4, torsion constant
L_b = 120  # in, unbraced length

# 4. Check Limit States
# (a) Material Rupture (Section 5.2.1)
M_n_rupture = S_x * F_Lc_adj  # = 15.0 * 26.8 = 402 kip-in

# (b) Lateral-Torsional Buckling (Section 5.2.2)
import math
C_b = 1.0  # Conservative (uniform moment)
M_n_LTB = C_b * math.sqrt(E_L * I_y * G_LT * J)  # Equation 5-7
# = 1.0 * sqrt(3000 * 5.0 * 450 * 0.5) = 1.0 * sqrt(3,375,000) = 1,837 kip-in

# (c) Local Buckling: Check flange and web per Section 5.2.3, 5.2.4
# (Not shown for brevity, but must be checked)

# 5. Controlling Limit State
M_n = min(M_n_rupture, M_n_LTB)  # = min(402, 1837) = 402 kip-in
controlling_mode = "Material Rupture"

# 6. Apply Resistance Factor (Section 2.3.2)
phi = 0.75  # Flexure resistance factor

# 7. Apply Time Effect Factor (Section 2.3.3)
lambda_factor = 0.80  # Snow load (2-month duration)

# 8. Design Strength
M_design = phi * lambda_factor * M_n
# = 0.75 * 0.80 * 402 = 241 kip-in

print(f"Nominal Strength: {M_n:.1f} kip-in ({controlling_mode})")
print(f"Design Strength: {M_design:.1f} kip-in")
print(f"Reduction Factors: φ={phi}, λ={lambda_factor}")
```

**Keywords**: calculate, compute, determine, design, capacity, strength, 계산, 산정, 설계, 강도

---

## 6. Connection Design Query (연결부 설계 - GFRP-SPECIFIC)

**User Intent**: Design bolted connections considering multiple failure modes.

**Example Queries**:
- "Design GFRP bolted connection: 3/4" bolt, e1=3", e2=2", t=0.5""
- "Check all failure modes for multi-row connection"
- "볼트연결부 설계: 볼트 4개, FRP-to-steel"

**Quick Process**:
1. Identify connection geometry:
   - Bolt diameter d_b, hole diameter d_h
   - End distance e_1, edge distance e_2
   - Pitch spacing s, gage g
   - Plate thickness t, number of bolts n, number of rows n_r
   - Materials connected (FRP-FRP vs FRP-steel)
   - Angle θ (connection force vs pultrusion direction)
2. **Check minimum geometry requirements** (Table 8-1):
   - e_1 ≥ 3d_h
   - e_2 ≥ 2d_h
   - s ≥ 3d_h
   - g ≥ 3d_h
3. **Check ALL 6+ failure modes** (Chapter 8.3):
   a. **Bolt shear/tension** (φ=0.75): Per AISC for steel bolt
   b. **Bearing** (φ=0.65): R_bf = C_b × ζ × F_br × d_b × t
   c. **Net tension** (φ=0.50): R_nt = K_nt × F_L^t × (w - d_h) × t
   d. **Shear-out** (φ=0.50): R_so = (e_2 + s/2) × t × F_LT^s
   e. **Block shear** (φ=0.65): Combined shear + tension tearing
   f. **Pull-through** (φ=0.50): R_pt = bearing pressure × washer area
4. **Multi-row load distribution** (if n_r > 1):
   - FRP-steel, 2 rows: 100% / 0%
   - FRP-steel, 3 rows: 60% / 40% / 0%
   - FRP-FRP, 2 rows: 60% / 40%
   - FRP-FRP, 3 rows: 60% / 30% / 20%
5. Use `scripts/connection_checker.py` for automated multi-mode checking
6. **Controlling mode**: Minimum of all 6+ capacities

**Connection Failure Modes Table**:

| Failure Mode | φ | Formula | Critical Parameter |
|--------------|---|---------|-------------------|
| Bolt shear | 0.75 | Per AISC | Steel bolt strength |
| Bearing | 0.65 | C_b ζ F_br d_b t | Pin-bearing strength F_br |
| Net tension | 0.50 | K_nt F_L^t (w-d_h) t | Net width, stress conc. |
| Shear-out | 0.50 | (e_2+s/2) t F_LT^s | Edge distance e_2 |
| Block shear | 0.65 | Complex | End/edge geometry |
| Pull-through | 0.50 | Punching shear | Washer size |

**Why Connection φ is Low?**:
- Stress concentrations at holes (brittle)
- Geometric variability (hole tolerance)
- Orthotropic bearing behavior
- No ductility warning before failure
- **Net tension φ=0.50 is lowest in standard!**

**Multi-Row Example**:
```python
# 3-row FRP-to-FRP connection design
n_r = 3  # number of rows
# Load distribution factors (Table C8-1)
f_u1 = 0.60  # 1st row (furthest from free end)
f_u2 = 0.30  # 2nd row
f_u3 = 0.20  # 3rd row (nearest to free end)

# Check each row
R_nt1 = f_u1 * (net tension capacity at row 1)
R_nt2 = f_u2 * (net tension capacity at row 2)
R_nt3 = f_u3 * (net tension capacity at row 3)

# Connection capacity = min of all modes
```

**Use `scripts/connection_checker.py`**:
```bash
python3 connection_checker.py \
  --d_b 0.75 --e_1 3.0 --e_2 2.0 --t 0.5 \
  --F_br 40 --F_Lt 35 --F_LTs 7 \
  --n 2 --n_r 2 --material FRP-FRP
```

**Keywords**: connection, bolt, bolted, bearing, net tension, shear-out, block shear, pull-through, 연결부, 볼트, 지압, 순인장

---

## 7. Terminology Query (용어 설명)

**User Intent**: Understand meaning and context of GFRP design terminology.

**Example Queries**:
- "What is orthotropic behavior?"
- "Explain time effect factor"
- "What's the difference between characteristic value and nominal value?"
- "펄트루전이 뭐야?"

**Quick Process**:
1. Check `references/glossary.md` first
2. If not found, search "Glossary" sections in Specification (Appendix B)
3. Present definition with ASCE citation
4. Provide usage examples from Specification chapters
5. **For GFRP-specific terms**: Explain material science background

**GFRP-Specific Terminology**:

**Orthotropic**: Material having different properties in three mutually perpendicular directions (L, T, through-thickness). GFRP is orthotropic because continuous fibers run in longitudinal direction.
- E_L ≠ E_T ≠ E_through-thickness
- F_L^t >> F_T^t (typically 5:1 to 8:1 ratio)
- Unlike steel/aluminum which are isotropic (same in all directions)

**Pultruded/Pultrusion**: Manufacturing process where continuous fibers are pulled through resin bath and heated die, creating constant cross-section shapes. Like "extrusion" but pulling instead of pushing.

**Characteristic Value**: Statistically determined minimum property value with 75% confidence that at least 80% of population exceeds this value. Per ASTM D6121:
- NOT the average value
- NOT the minimum test value
- Statistical lower bound: F_char = mean - k×std_dev

**Time Effect Factor (λ)**: Reduction factor for sustained loads due to creep rupture. GFRP strength decreases over time under constant stress:
- Short-term (10 min): λ = 1.00 (full strength)
- Long-term (50 years): λ = 0.60 (60% strength)
- Unique to GFRP and wood (metals don't have this)

**Glass Transition Temperature (T_g)**: Critical temperature above which polymer matrix becomes rubbery and loses strength/stiffness. Typically 180-250°F for polyester/vinyl ester systems. Absolute design limit.

**Bearing Strength (F_br)**: Compressive strength of GFRP under localized bolt bearing. Must be determined by testing (ASTM D7290), not calculated from material properties. Varies with:
- Load angle θ relative to pultrusion direction
- Bolt diameter to thickness ratio (d/t)
- Edge distance to diameter ratio (e/d)

**Keywords**: what is, explain, definition, meaning, 뭐야, 설명, 의미, 정의

---

## 8. Symbol/Notation Query (기호 질의)

**User Intent**: Understand what a mathematical symbol represents.

**Example Queries**:
- "What does E_L mean?"
- "Define C_M moisture factor"
- "λ 기호는 무엇을 의미하나요?"

**Quick Process**:
1. Check `references/symbols.md`
2. Return: Symbol | Definition | Units | Section Reference
3. Example: *E_L* = Longitudinal elastic modulus | ksi (MPa) | Sections 1.4, 2.3, 4.2, 5.2
4. **For GFRP-specific symbols**: Explain orthotropic context

**Common GFRP Symbols**:

**Material Properties**:
- **E_L**: Longitudinal elastic modulus (parallel to fibers) = 2,000-4,000 ksi
- **E_T**: Transverse elastic modulus (perpendicular to fibers) = 800-1,500 ksi (~40% of E_L)
- **G_LT**: In-plane shear modulus = 300-600 ksi (~15% of E_L)
- **ν_LT**: Poisson's ratio = 0.25-0.35 (typically 0.3)
- **T_g**: Glass transition temperature = 180-250°F (critical threshold)

**Strengths** (with superscripts):
- **F_L^t**: Longitudinal tensile strength = 30-50 ksi
- **F_T^t**: Transverse tensile strength = 5-10 ksi (much lower!)
- **F_L^c**: Longitudinal compressive strength = 20-40 ksi (60-80% of F_L^t)
- **F_LT^s**: Longitudinal-transverse shear strength = 4-10 ksi

**Adjustment Factors**:
- **C_M**: Moisture factor (0.70-1.00) - reduces strength for wet service
- **C_T**: Temperature factor (0.75-1.00) - reduces strength for elevated temperature
- **C_CH**: Chemical factor (0.50-1.00) - reduces strength for aggressive chemicals
- **φ**: Resistance factor (0.50-0.85) - accounts for variability, varies by failure mode
- **λ**: Time effect factor (0.60-1.00) - accounts for load duration (creep rupture)

**Superscripts**:
- **^t** = tension
- **^c** = compression
- **^f** = flexure
- **^s** = shear

**Subscripts**:
- **_L** = longitudinal direction (0°, direction of pultrusion)
- **_T** = transverse direction (90°, perpendicular to pultrusion)
- **_LT** = longitudinal-transverse (in-plane shear)
- **_w** = web
- **_f** = flange

**Keywords**: symbol, notation, variable, 기호, 표기, 변수

---

## 9. Comparison Query (비교 질의)

**User Intent**: Compare GFRP with steel/aluminum, or compare different GFRP configurations.

**Example Queries**:
- "GFRP vs steel structural design differences"
- "Compare E_L and E_T for GFRP"
- "GFRP와 철골 설계의 차이는?"
- "Why is GFRP deflection often critical?"

**Quick Process**:
1. Identify items to compare
2. For GFRP vs metals:
   - Material properties (E, density, strength)
   - Design philosophy (LRFD, factors, time effects)
   - Behavior (ductile vs brittle, isotropic vs orthotropic)
   - Environmental sensitivity
3. For GFRP directional comparison (L vs T):
   - Property ratios (E_L/E_T, F_L^t/F_T^t)
   - Orthotropic effects in design
4. Present in comparison table format

**GFRP vs Steel Comprehensive Comparison**:

| Property | GFRP (typical) | Steel (A36/A992) | Ratio | Implications |
|----------|----------------|------------------|-------|--------------|
| **E (modulus)** | 2,500 ksi | 29,000 ksi | 1:12 | **Deflection controls!** |
| **F_t (tensile)** | 35 ksi | 36-50 ksi | Similar | Good strength |
| **Density** | 0.065 lb/in³ | 0.284 lb/in³ | 1:4.4 | **Much lighter** |
| **Strength/weight** | 538 ksi/(lb/in³) | 127-176 ksi/(lb/in³) | 3-4:1 | **Excellent ratio** |
| **Ductility** | **None (brittle)** | High (ductile) | - | **No yielding warning** |
| **Directional** | **Orthotropic** | Isotropic | - | **L vs T different** |
| **Time-dependent** | **Yes (creep)** | No | - | **λ factor required** |
| **Environmental** | **Sensitive** | Minimal | - | **C_M, C_T, C_CH needed** |
| **T limit** | T_g ~200°F | ~1000°F | - | **Temperature limited** |
| **Thermal expansion** | 13×10⁻⁶/°F | 6.5×10⁻⁶/°F | 2:1 | Higher expansion |
| **Design method** | LRFD only | LRFD + ASD | - | Simpler approach |
| **Resistance factors** | φ = 0.50-0.85 | φ = 0.75-0.90 | Lower | More conservative |

**GFRP Longitudinal vs Transverse Comparison**:

| Property | Longitudinal (L) | Transverse (T) | L:T Ratio | Why Different? |
|----------|------------------|----------------|-----------|----------------|
| Modulus E | 3,000 ksi | 1,200 ksi | 2.5:1 | Continuous fibers in L |
| Tensile F^t | 40 ksi | 7 ksi | 5-8:1 | Fiber-dominated vs matrix |
| Compressive F^c | 30 ksi | 15 ksi | 2:1 | Buckling vs crushing |
| **Design impact** | **Primary load** | **Secondary load** | - | **Avoid T-loading!** |

**Critical Design Philosophy Differences**:

**Steel**:
- Yielding provides ductility and warning
- Properties uniform in all directions
- No time or environmental effects
- Deflection rarely controls
- φ factors higher (0.90 typical)

**GFRP**:
- **No yielding** - brittle failure without warning
- **Orthotropic** - must consider L vs T directions
- **Time-dependent** - λ factor for creep rupture
- **Environmentally sensitive** - C_M, C_T, C_CH factors
- **Deflection often controls** - E is 1/12 of steel
- **φ factors lower** - especially connections (0.50)
- **Multiple buckling modes** - flexural, local flange, local web, torsional

**When GFRP is Advantageous**:
1. **Corrosion resistance**: Chemical plants, marine, wastewater treatment
2. **Lightweight**: Roof structures, pedestrian bridges, temporary structures
3. **EMI transparency**: Near radar, MRI facilities
4. **Thermal insulation**: Cold storage, process equipment
5. **Ease of installation**: No welding, lighter crane requirements

**When Steel is Better**:
1. **Stiffness-critical**: Long spans with tight deflection limits
2. **High temperature**: Above 200°F sustained
3. **Ductility required**: Seismic zones needing R > 3
4. **Fire resistance**: Occupied buildings without fireproofing
5. **Cost**: Simple structural framing where corrosion not issue

**Keywords**: compare, difference, vs, 차이, 비교, steel, aluminum, metal, orthotropic, isotropic

---

## 10. Serviceability Query (사용성 질의)

**User Intent**: Check deflection, drift, or vibration criteria.

**Example Queries**:
- "What deflection limit for GFRP beams?"
- "Calculate GFRP beam deflection under service loads"
- "Why does deflection control GFRP design?"
- "GFRP 처짐 제한은?"

**Quick Process**:
1. Identify serviceability criterion (deflection, drift, vibration)
2. **Note: No φ or λ factors for serviceability!**
3. Use **service load combinations** (unfactored per ASCE 7)
4. Use **mean modulus values** (not characteristic reduced values)
5. For deflection:
   - Instantaneous: Standard elastic equation
   - Long-term creep: Δ_total = Δ_instant × (1 + ψ_creep)
   - Creep multiplier ψ typically 1.5-3.0 for sustained loads
6. Compare to limits (Section 2.6):
   - Floors: L/360 (or L/240 for special cases)
   - Roofs: L/240 or L/180
   - Cantilevers: More stringent
7. **Deflection often governs GFRP design!**

**Why Deflection Controls GFRP**:
- E_GFRP ≈ E_steel / 12 (much more flexible)
- Deflection ∝ 1/E (inversely proportional)
- Same load, same span → GFRP deflects 12× more than steel
- L/360 limit often exceeded unless section is large

**Deflection Calculation Example**:
```python
# GFRP Simple Beam Deflection
# No φ, no λ for serviceability!

# Service loads (unfactored)
w_D = 50  # plf, dead load
w_L = 100  # plf, live load
L = 20 * 12  # inches, span

# Material (mean values, not reduced)
E_L = 3000  # ksi, mean longitudinal modulus
I = 100  # in^4, moment of inertia

# Instantaneous deflection (elastic)
w_total = w_D + w_L  # = 150 plf
Delta_instant = (5 * w_total * L**4) / (384 * E_L * I)
# = (5 * 150/12 * 240^4) / (384 * 3000 * 100)
# = 2.88 in

# Long-term deflection (creep under sustained load)
psi_creep = 2.0  # Creep multiplier (typical 1.5-3.0)
w_sustained = w_D  # Only dead load is sustained
Delta_creep = psi_creep * (5 * w_sustained * L**4) / (384 * E_L * I)
# = 2.0 * (5 * 50/12 * 240^4) / (384 * 3000 * 100)
# = 0.96 in

Delta_total = Delta_instant + Delta_creep  # = 2.88 + 0.96 = 3.84 in

# Check limits
L_360 = L / 360  # = 240 / 360 = 0.67 in
L_240 = L / 240  # = 240 / 240 = 1.00 in

if Delta_total > L_360:
    print(f"FAILS L/360: {Delta_total:.2f} in > {L_360:.2f} in")
    print("Increase section size or reduce span")
else:
    print(f"OK: {Delta_total:.2f} in < {L_360:.2f} in")
```

**Deflection Limits** (Section 2.6):

| Application | Limit | Notes |
|-------------|-------|-------|
| Floor beams (general) | L/360 | Live load only |
| Floor beams (brittle finishes) | L/480 | Total load |
| Roof beams | L/240 or L/180 | Depends on use |
| Cantilevers | L/180 or L/120 | More stringent |

**Drift Limits** (lateral):
- Non-structural elements attached: 0.7% (0.007h)
- Structural elements only: 2.5% (0.025h)

**Vibration**:
- Natural frequency f > 3-5 Hz for floors (walking comfort)
- Use instantaneous stiffness (no creep for dynamic)

**Keywords**: deflection, drift, serviceability, L/360, vibration, creep, 처짐, 사용성, 진동

---

# Quick Reference Tables

## Document Categories

| Type | Location | Files | Purpose |
|------|----------|-------|---------|
| **Specification** | data/specification/ | 5 parts (125 pages) | Formulas, limits, requirements (Ch 1-9) |
| **Commentary** | Integrated in parts | Sections C1-C9 | Background, rationale, examples |
| **Appendices** | part3, part5 | App A, B, C8.3.2 | Symbols, glossary, detailed formulas |
| **References** | references/ | 8 guides | Symbols, properties, factors, structure |
| **Scripts** | scripts/ | 5 Python files | Search, lookup, calculations |

## Common Search Patterns

| Topic | Keywords | Specification Chapter | Key Considerations |
|-------|----------|----------------------|-------------------|
| **Beam Design** | flexure, bending, LTB, moment | Chapter 5 | Deflection often controls, check multiple buckling modes |
| **Column Design** | compression, buckling, KL/r | Chapter 4 | Local buckling critical, 4+ modes to check |
| **Tension Members** | tension, net area, gross area | Chapter 3 | 0.7 factor for holes, simple design |
| **Shear** | shear, web, buckling | Chapter 5.3 | Check with/without buckling, stiffeners |
| **Connections** | bolts, bearing, net tension, shear-out | Chapter 8 | **6+ failure modes, φ as low as 0.50** |
| **Material Lookup** | properties, E_L, E_T, strength | Ch 1, 2, Refs | **Must test per ASTM D6121** |
| **Environmental** | moisture, temperature, chemical, C_M, C_T | Chapter 2.4 | **Can reduce capacity 30-50%** |
| **Time Effects** | duration, creep, λ, sustained | Chapter 2.3.3 | **λ = 0.60-1.00, critical for permanent loads** |
| **Serviceability** | deflection, L/360, drift | Chapter 2.6 | **Often governs due to low E** |
| **Seismic** | earthquake, R factor, braced frame | Chapter 9 | Low R (2.0-3.0), limited ductility |

## ASCE/SEI 74-23 Chapter-to-Topic Mapping

| Spec Chapter | Topic | Reference Quick Guides | Unique GFRP Issues |
|--------------|-------|----------------------|-------------------|
| 1 | General | abbreviations.md | Scope, materials, ASTM standards |
| 2 | Design Requirements | resistance-factors.md, time-effect-factors.md, environmental-factors.md | **φ, λ, C_M, C_T, C_CH - critical!** |
| 3 | Tension | - | 0.7 factor for holes |
| 4 | Compression | - | **4+ buckling modes**, alloy-dependent |
| 5 | Flexure & Shear | - | **Deflection often controls**, LTB |
| 6 | Combined | - | Interaction equations |
| 7 | Plates | - | Open-hole stress concentration |
| 8 | Connections | - | **6+ failure modes, lowest φ (0.50)** |
| 9 | Seismic | - | Low R (2.0-3.0), height limits |
| App A | Symbols | symbols.md | 150+ variables defined |
| App B | Glossary | glossary.md | 50+ technical terms |

## Resistance Factors Quick Reference

| Limit State | φ | Why This Value? |
|-------------|---|-----------------|
| Tension (gross/net) | 0.85 | Predictable failure |
| Compression (flexural buckling) | 0.80 | Imperfection sensitive |
| Compression (local buckling) | 0.70 | Higher variability |
| Flexure (rupture, buckling) | 0.75 | Combined behavior |
| Shear (web) | 0.85 | Progressive failure |
| Torsion | 0.75 | Moderate variability |
| **Connection - Bolt** | 0.75 | Steel bolt |
| **Connection - Bearing** | 0.65 | Geometric variability |
| **Connection - Net Tension** | **0.50** | **Brittle, most critical** |
| **Connection - Shear-out** | **0.50** | **Brittle** |
| **Connection - Block Shear** | 0.65 | Combined mode |
| **Connection - Pull-through** | **0.50** | **Localized** |

**Lowest φ**: Net tension, shear-out, pull-through = **0.50** (most conservative)

## Time Effect Factors Quick Reference

| Load Duration | λ | When to Use |
|---------------|---|-------------|
| Permanent (50+ years) | 0.60 | Dead load only (1.4D) |
| 10 years | 0.70 | D + L combinations |
| 2 months (snow season) | 0.80 | D + S combinations |
| 7 days | 0.90 | D + L_r combinations |
| 10 minutes | 1.00 | D + W, D + E combinations |

**Rule**: Use **shortest significant duration** in load combination.

## Environmental Factors Quick Reference

| Factor | Symbol | Dry/Normal | Wet/Humid | Severe | Application |
|--------|--------|------------|-----------|--------|-------------|
| Moisture | C_M | 1.00 | 0.80-0.90 | 0.70-0.80 | Wet service, immersion |
| Temperature | C_T | 1.00 | 0.85-0.95 | 0.75-0.85 | Sustained elevated temp |
| Chemical | C_CH | 1.00 | 0.85-0.95 | 0.50-0.85 | Aggressive chemicals |

**Formula**: F_adjusted = F_reference × C_M × C_T × C_CH

**Warning**: Combined effects can reduce capacity **30-50%** or more!

## Units Convention

| Quantity | US Customary (Primary) | SI (in Parentheses) | Notes |
|----------|----------------------|-------------------|-------|
| Force | kip (1000 lbs) | kN | 1 kip ≈ 4.448 kN |
| Moment | kip-in | kN-mm | Inch-based typical |
| Stress | ksi (kip/in²) | MPa | 1 ksi ≈ 6.895 MPa |
| Length | in (inches) | mm | 1 in = 25.4 mm |
| Temperature | °F | °C | Critical for T_g |
| Modulus | ksi | MPa | **E_L ~2500 ksi for GFRP** |

---

# Performance Optimization

## Search Strategy Priority

1. **Chapter identification first**:
   - Use topic keywords to identify specific chapter (1-9)
   - Don't search all files - target 1-2 relevant chapters
   - Example: "connection" → Only search Chapter 8

2. **Reference files before full search**:
   - Symbols → `references/symbols.md`
   - Properties → `references/material-properties-guide.md`
   - Factors → `references/environmental-factors.md`, `resistance-factors.md`, `time-effect-factors.md`
   - Structure → `references/chapter-structure.md`

3. **Efficient chapter targeting**:
   - Connection design → Chapter 8
   - Beam design → Chapter 5
   - Column design → Chapter 4
   - Material/factors → Chapter 2
   - Example: "GFRP beam LTB" → Only search Chapter 5

4. **Smart document reading**:
   - Read only relevant sections
   - Use offset and limit for large files
   - Cross-reference Specification and Commentary when needed

## Python Script Usage

Execute automation scripts when appropriate:

```bash
# Material properties lookup
python3 scripts/material_lookup.py --property "E_L" --typical

# Environmental adjustment calculation
python3 scripts/environmental_adjustment.py \
  --F_ref 35 --C_M 0.85 --C_T 0.90 --C_CH 1.00

# Connection multi-mode checker
python3 scripts/connection_checker.py \
  --d_b 0.75 --e_1 3.0 --e_2 2.0 --t 0.5 \
  --F_br 40 --F_Lt 35 --F_LTs 7 --n 2

# Category-aware search
python3 scripts/smart_search.py "lateral-torsional buckling"

# Extract formula with context
python3 scripts/formula_finder.py "M_n =" "Chapter 5"
```

---

# Response Quality Checklist

Every response should include:

- ✅ **Accurate ASCE citation** (ASCE/SEI 74-23 Section X.Y or Chapter X)
- ✅ **Orthotropic properties specified** (E_L, E_T, G_LT when relevant)
- ✅ **Environmental factors identified** (C_M, C_T, C_CH applicable?)
- ✅ **Time effect factor noted** (λ for load duration)
- ✅ **Resistance factor specified** (φ varies by failure mode)
- ✅ **Direction clarified** (longitudinal vs transverse loading)
- ✅ **Multiple limit states checked** (GFRP has 3-4+ competing modes)
- ✅ **Units specified** (ksi, in, kip, °F)
- ✅ **Variable definitions** from symbols.md
- ✅ **Serviceability noted** (deflection often governs)
- ✅ **Testing requirements mentioned** (ASTM D6121, D7290 when relevant)
- ✅ **Working Python code** for calculations (tested and validated)

---

# Special Features: GFRP-Specific Considerations

## Critical Differences from Steel/Aluminum Design

### 1. Orthotropic Behavior
**Steel/Aluminum**: Isotropic (E_x = E_y = E_z)
**GFRP**: **Orthotropic** (E_L ≠ E_T ≠ E_TT, typically E_L = 2.5×E_T)

→ **Must specify direction** of loading and properties

### 2. Time-Dependent Strength (Creep Rupture)
**Steel/Aluminum**: No time effect
**GFRP**: **Significant** time effect (λ = 0.60-1.00)

→ **Apply λ factor** for all load combinations based on duration

### 3. Environmental Sensitivity
**Steel**: Minimal (corrosion is durability, not strength issue)
**Aluminum**: Moderate (HAZ from welding)
**GFRP**: **High sensitivity** to moisture, temperature, chemicals

→ **Apply C_M, C_T, C_CH factors** (can reduce capacity 30-50%)

### 4. No Yielding (Brittle Behavior)
**Steel**: Ductile with yielding plateau
**GFRP**: **Linear-elastic to brittle failure** (no warning)

→ **Lower φ factors** (0.50-0.85 vs steel's 0.75-0.90)

### 5. Low Stiffness
**Steel**: E = 29,000 ksi
**GFRP**: **E = 2,000-4,000 ksi** (~1/12 of steel)

→ **Deflection often governs** design, not strength

### 6. Multiple Buckling Modes
**Steel**: Typically 1-2 buckling modes
**GFRP**: **4+ buckling modes** (flexural, local flange, local web, torsional, flexural-torsional)

→ **Check all modes** separately

### 7. Complex Connection Design
**Steel**: Typically 2-3 failure modes
**GFRP**: **6+ failure modes** (bearing, net tension, shear-out, block shear, pull-through, bolt shear)

→ **Connections often critical** (φ as low as 0.50)

### 8. Temperature Limits
**Steel**: Up to ~1000°F
**GFRP**: **T_g typically 180-250°F** (absolute limit)

→ **Verify T_service < T_g - 20°F**

## When to Use Specification vs Commentary

**Use Specification when**:
- User asks "what is the formula?"
- User needs official requirements or limits
- User wants to perform calculations
- User asks about design criteria

**Use Commentary when**:
- User asks "why is this required?"
- User needs background or research basis
- User wants to understand design philosophy
- User asks "what's the difference from steel?"

**Use Both Together when**:
- Comprehensive design questions
- Teaching/learning scenarios
- Formula explanation with practical context
- Validation of complex calculations

**Use References when**:
- Quick property lookup
- Factor value tables
- Symbol definitions
- Chapter navigation

---

# Error Handling

## Common Scenarios

1. **Material properties not specified**:
   - Ask user: "Have you conducted ASTM D6121 testing for characteristic values?"
   - Provide typical ranges for preliminary design only
   - **Emphasize**: Final design MUST use test data

2. **Environmental conditions unclear**:
   - Ask user: "What are the service conditions? (dry/wet, temperature, chemicals)"
   - Explain impact of C_M, C_T, C_CH factors (30-50% reduction possible)

3. **Load duration ambiguous**:
   - Ask user: "What load combination? (dead+live, dead+snow, dead+wind, etc.)"
   - Explain λ factor selection (0.60-1.00 depending on duration)

4. **Direction not specified**:
   - Ask user: "Is loading in longitudinal or transverse direction?"
   - Explain orthotropic behavior (E_L ≠ E_T, F_L^t ≠ F_T^t)

5. **No results found**:
   - Suggest alternative keywords
   - Check all document types (Specification, Commentary, References)
   - Recommend chapter-structure.md for navigation

6. **Ambiguous query**:
   - Clarify with multiple interpretations
   - Ask user: "Did you mean [option A] or [option B]?"

7. **Missing parameters**:
   - List required values for calculation
   - Offer typical values for preliminary sizing (with disclaimers)

8. **Out of scope**:
   - Clearly state limitations (no FRP rebar, no FRP wraps, no filament wound)
   - Suggest consulting manufacturer or conducting testing

## Validation Checks

For all calculations:
- ✅ Verify orthotropic properties (E_L, E_T, G_LT all provided)
- ✅ Check environmental factors applied (C_M, C_T, C_CH)
- ✅ Check time effect factor applied (λ)
- ✅ Verify resistance factor (φ appropriate for failure mode)
- ✅ Check against ASTM limits (COV, sample size, characteristic value methodology)
- ✅ Verify temperature < T_g - 20°F
- ✅ Warn if parameters outside typical ranges
- ✅ Note all assumptions (bracing, load cases, environmental exposure)
- ✅ Cross-check multiple limit states (GFRP has 3-4+ competing modes)

---

# Special Notes

## LRFD Method - Only Design Approach

ASCE/SEI 74-23 uses **LRFD exclusively**:

**LRFD Design Equation**:
$$R_u \leq \phi \lambda R_n$$

Where:
- $R_u$ = required strength (factored loads per ASCE 7)
- $\phi$ = resistance factor (0.50-0.85, varies by failure mode)
- $\lambda$ = time effect factor (0.60-1.00, varies by load duration)
- $R_n$ = nominal resistance (based on characteristic properties adjusted for environment)

**Load Combinations**: Per ASCE 7 (same as steel/concrete):
- 1.4D
- 1.2D + 1.6L + 0.5L_r
- 1.2D + 1.6L_r + (0.5L or 0.5S)
- 1.2D + 1.6S + (0.5L or 0.8W)
- 1.2D + 1.0W + 0.5L + 0.5S
- 1.2D + 1.0E + 0.5L + 0.2S
- 0.9D + 1.0W
- 0.9D + 1.0E

**No ASD**: Standard does not provide ASD conversion. If user asks about ASD, explain LRFD is the required method.

## Testing Requirements

**Critical**: Material properties cannot be assumed - MUST be determined by testing.

**Required Testing Standards**:
- **ASTM D6121**: Characteristic properties determination (statistical methodology)
- **ASTM D7290**: Filled-hole compression and tension (for connection design)
- **ASTM D3039**: Tensile properties
- **ASTM D3410**: Compressive properties
- **ASTM D5379**: Shear properties (V-notched beam method)
- **ASTM E1640**: Glass transition temperature T_g

**Statistical Requirements**:
- Minimum sample size: 10-30 specimens per configuration
- Statistical basis: 75% confidence, 20% exclusion limit
- F_characteristic = mean - k × std_dev (where k from t-distribution)

## Version Tracking

- Standard: **ASCE/SEI 74-23** (2023 edition)
- Published by: **American Society of Civil Engineers**
- Always cite version in responses

## Material Defaults (Preliminary Design Only)

**If no test data available** (preliminary sizing only):
- E_L = 2,500 ksi (17 GPa)
- E_T = 1,000 ksi (7 GPa)
- G_LT = 400 ksi (2.8 GPa)
- F_L^t = 30 ksi (210 MPa)
- F_L^c = 20 ksi (140 MPa)
- F_LT^s = 5 ksi (35 MPa)
- ν_LT = 0.30
- T_g = 200°F (minimum acceptable)

**Warning**: Final design MUST use manufacturer test data per ASTM D6121.

---

For comprehensive GFRP structural design work, this skill integrates:
1. **Code requirements** from ASCE/SEI 74-23 Specification (Chapters 1-9)
2. **Background understanding** from Commentary (Chapters C1-C9)
3. **Quick reference data** from 8 reference guides (properties, factors, symbols)
4. **Automation tools** from 5 Python scripts (search, lookup, calculations)
5. **GFRP-specific expertise** (orthotropic, time effects, environmental sensitivity)

**Always prioritize accuracy, cite sources, apply environmental and time effect factors, check multiple failure modes, verify material properties, and follow LRFD methodology.**

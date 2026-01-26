# ASCE/SEI 74-23 Chapter Structure

Complete navigation guide to the ASCE/SEI 74-23 standard for pultruded GFRP structures.

## Document Organization

### Main Specification (9 Chapters)
Covers design requirements and formulas

### Commentary (Chapters C1-C9)
Provides background, rationale, and examples

### Appendices
- **Appendix A**: Symbols and Notations
- **Appendix B**: Glossary
- **Appendix C8.3.2**: Full formulae for multi-row bolted connections

## Chapter 1: General Provisions

**File**: `ASCE_SEI_74-23_part1_pages1-25.md` (pages 1-15)

**Sections**:
- 1.1 Scope
- 1.2 Referenced Specifications, Codes, and Standards
- 1.3 Materials
- 1.4 General Design Requirements
- 1.5 Loads and Load Combinations

**Key Content**:
- Applicability to pultruded GFRP only
- Glass fiber reinforcement with thermosetting resins
- LRFD design method
- References to ASCE 7 load combinations

**When to Use**:
- Understanding scope and limitations
- Identifying applicable standards (ASTM D6121, D7290, etc.)
- Verifying material requirements
- Finding load combination requirements

## Chapter 2: Design Requirements

**File**: `ASCE_SEI_74-23_part1_pages1-25.md` and `part2_pages26-50.md`

**Sections**:
- 2.1 Required Strength
- 2.2 Limit States
- 2.3 Design Strength
  - 2.3.1 Nominal Resistance
  - 2.3.2 Resistance Factors ($\phi$)
  - 2.3.3 Time Effect Factor ($\lambda$)
- 2.4 Classification Factors (Environmental Adjustments)
  - $C_M$ (moisture), $C_T$ (temperature), $C_{CH}$ (chemical), $C_{CA}$ (composite action), $C_{LS}$ (load sharing)
- 2.5 Structural Analysis (Second-Order Effects)
- 2.6 Deflection and Drift
- 2.7 Ponding
- 2.8 Fatigue
- 2.9 Fire, Smoke, and Toxicity
- 2.10 Effective Net Area

**Key Content**:
- LRFD equation: $R_u \leq \phi \lambda R_n$
- All resistance factors ($\phi$ = 0.50-0.85)
- Time effect factors ($\lambda$ = 0.60-1.00)
- Environmental adjustment procedures
- P-delta analysis requirements
- Deflection limits
- Fatigue design curves

**When to Use**:
- Determining design equation and factors
- Applying environmental adjustments
- Structural analysis methods
- Serviceability checks (deflection, vibration)
- Fatigue-critical applications

## Chapter 3: Design of Tension Members

**File**: `ASCE_SEI_74-23_part2_pages26-50.md`

**Sections**:
- 3.1 General Provisions
- 3.2 Tensile Strength
  - 3.2.1 Gross Section
  - 3.2.2 Net Section
- 3.3 Design of Tension Members
- 3.4 Pin-Connected Tension Members
- 3.5 Threaded Rods

**Key Formulas**:
- Gross section: $P_n = F_L^t A_g$
- Net section: $P_n = 0.7 F_L^t A_e$ (0.7 factor for holes)
- Slenderness limit: $L/r \leq 250$

**Resistance Factor**: $\phi$ = 0.85

**When to Use**:
- Designing tension rods, braces, hangers
- Calculating net section at bolt holes
- Pin-connected members
- Threaded rod connections

## Chapter 4: Design of Compression Members

**File**: `ASCE_SEI_74-23_part2_pages26-50.md`

**Sections**:
- 4.1 General Provisions
- 4.2 Flexural Buckling of Compression Members
- 4.3 Effective Length
- 4.4 Compression Members with Open Cross Sections

**Key Formulas**:
- Euler buckling: $F_{cre} = \frac{\pi^2 E_L}{(KL/r)^2}$
- Local flange buckling (I-shapes): $F_{crf} = \frac{\pi^2}{12(1-\nu_{LT}^2)} \left(\frac{t_f}{b_f}\right)^2 \sqrt{E_L E_T}$
- Local web buckling: $F_{crw} = \frac{\pi^2}{6} \frac{[\sqrt{E_L E_T} + \nu_{LT}E_T + 2G_{LT}]}{h^2/t_w}$
- Torsional buckling (angles, channels): $F_{crt} = \left(\frac{E_L G_{LT}}{12(1-\nu_{LT}^2\nu_{TL}^2)}\right)^{1/2} \left(\frac{t}{b}\right)$

**Resistance Factors**:
- Flexural buckling: $\phi$ = 0.80
- Local buckling: $\phi$ = 0.70

**When to Use**:
- Column design
- Compression members in braced frames
- Checking multiple buckling modes
- Determining K-factors

## Chapter 5: Design of Members for Flexure and Shear

**File**: `ASCE_SEI_74-23_part2_pages26-50.md` and `part3_pages51-75.md`

**Sections**:
- 5.1 General Provisions
- 5.2 Flexural Strength
  - 5.2.1 Material Rupture
  - 5.2.2 Lateral-Torsional Buckling
  - 5.2.3 Local Flange Buckling
  - 5.2.4 Local Web Buckling
- 5.3 Shear Strength
  - 5.3.1 Web Shear Without Buckling
  - 5.3.2 Web Shear Buckling
  - 5.3.3 Web Stiffeners
- 5.4 Concentrated Force on Webs

**Key Formulas**:
- Material rupture: $M_n = S \cdot F_L^c$ (or $F_L^t$ if tension controls)
- Lateral-torsional buckling: $M_n = C_b \sqrt{E_L I_y G_{LT} J}$
- Web shear: $V_n = F_{LT}^s A_s$
- Shear buckling: $F_{cr,s} = k \frac{\pi^2}{12(1-\nu_{LT}^2)} \left(\frac{t_w}{d_w}\right)^2 \sqrt{E_L E_T}$

**Resistance Factors**:
- Flexure: $\phi$ = 0.75
- Shear: $\phi$ = 0.85

**When to Use**:
- Beam design
- Checking lateral-torsional buckling
- Web shear and shear buckling
- Concentrated load design (bearing stiffeners)
- Web crippling under point loads

## Chapter 6: Design of Members Subjected to Combined Forces and Torsion

**File**: `ASCE_SEI_74-23_part3_pages51-75.md`

**Sections**:
- 6.1 General
- 6.2 Symmetry Requirements
- 6.3 Combined Axial Force and Flexure (Beam-Columns)
- 6.4 Combined Flexure, Axial Force, and Torsion

**Key Formulas**:
- Beam-column interaction: $\frac{P_u}{\lambda \phi P_n} + \frac{M_u}{\lambda \phi M_n} \leq 1.0$
- Torsion (rectangular tubes): $T_n = 2 A_m t F_{LT}^s$
- Combined: $\left(\frac{P_u}{\lambda \phi P_n}\right) + \left(\frac{M_u}{\lambda \phi M_n}\right) + \left(\frac{T_u}{\lambda \phi T_n}\right)^2 \leq 1.0$

**Resistance Factors**: Use controlling limit state factor

**When to Use**:
- Beam-columns (compression + bending)
- Members with torsion
- Complex loading situations
- Eccentrically loaded columns

## Chapter 7: Design of Plates and Built-Up Members

**File**: `ASCE_SEI_74-23_part3_pages51-75.md` and `part4_pages76-100.md`

**Sections**:
- 7.1 General
- 7.2 Design Philosophy
- 7.3 Open-Hole Strength
- 7.4 Transverse Shear (Pull-Through)
- 7.5 In-Plane Tension
- 7.6 In-Plane Compression
- 7.7 In-Plane Shear
- 7.8 Two-Way Bending of Plates

**Key Formulas**:
- Longitudinal tension: $N_n^t = F_L^t \cdot t$ (per unit width)
- Transverse tension: $N_n^t = F_T^t \cdot t$ (per unit width)
- Open-hole strength reduction: $k_L = \frac{2E_L}{E_L + E_T + \nu_{LT}G_{LT}}$
- Pull-through: $R_n^{pt} = F_{LT}^s \cdot A_{punching}$

**Resistance Factors**:
- Tension: $\phi$ = 0.85
- Compression: $\phi$ = 0.75
- Shear: $\phi$ = 0.85
- Pull-through: $\phi$ = 0.65

**When to Use**:
- Plate design (grating, decking)
- Built-up sections
- Open-hole stress concentrations
- Pull-through capacity of fasteners

## Chapter 8: Design of Bolted Connections

**File**: `ASCE_SEI_74-23_part4_pages76-100.md` and `part5_pages101-125.md`

**Sections**:
- 8.1 General
- 8.2 Connection Geometry Requirements
  - 8.2.1 Minimum Spacing
  - 8.2.2 Minimum Edge Distance
  - 8.2.3 Maximum Spacing
- 8.3 Connection Design
  - 8.3.1 General
  - 8.3.2 Design Strength Formulations
    - 8.3.2.1 Bolt Shear/Tension Strength
    - 8.3.2.2 Bearing Strength
    - 8.3.2.3 Net Tension Strength
    - 8.3.2.4 Shear-Out Strength
    - 8.3.2.5 Block Shear Strength
    - 8.3.2.6 Pull-Through Strength
  - 8.3.3 Multi-Row Connections
  - 8.3.4 Compression Members with Bearing Eccentricity
- 8.4 Column Bases and Bearing on Concrete

**Minimum Geometry (Table 8-1)**:
| Parameter | Minimum Value |
|-----------|---------------|
| End distance $e_1$ | 3$d_h$ |
| Edge distance $e_2$ | 2$d_h$ |
| Pitch spacing $s$ | 3$d_h$ |
| Gage $g$ | 3$d_h$ |

**Key Formulas**:
- Bolt shear: Use AISC steel bolt values
- Bearing: $R_{bf} = C_b \cdot \zeta \cdot F_{br} \cdot d_b \cdot t$
- Net tension: $R_{nt} = K_{nt} \cdot F_L^t \cdot (w - d_h) \cdot t$
- Shear-out: $R_{so} = (e_2 + s/2) \cdot t \cdot F_{LT}^s$
- Block shear: Combined shear + tension tearing

**Resistance Factors**:
- Bolt shear/tension: $\phi$ = 0.75
- Bearing: $\phi$ = 0.65
- Net tension: $\phi$ = 0.50
- Shear-out: $\phi$ = 0.50
- Block shear: $\phi$ = 0.65
- Pull-through: $\phi$ = 0.50

**Multi-Row Load Distribution**:
| Materials | Rows | 1st Row | 2nd Row | 3rd Row |
|-----------|------|---------|---------|---------|
| FRP-steel | 2 | 100% | 0% | - |
| FRP-steel | 3 | 60% | 40% | 0% |
| FRP-FRP | 2 | 60% | 40% | - |
| FRP-FRP | 3 | 60% | 30% | 20% |

**When to Use**:
- All connection design
- Checking 6+ failure modes
- Multi-bolt connections
- Column base plates
- Bearing on concrete

## Chapter 9: Seismic Design Requirements

**File**: `ASCE_SEI_74-23_part5_pages101-125.md`

**Sections**:
- 9.1 Seismic Loads
  - 9.1.1 Seismic Design Category A
  - 9.1.2 Design Parameters for Seismic Force-Resisting Systems
- 9.2 Seismic Force-Resisting Systems
  - 9.2.1 General
  - 9.2.2 Concentrically Braced Frame
  - 9.2.3 Enhanced Connection Strength Concentrically Braced Frame
  - 9.2.4 Ordinary Braced Cooling Towers

**Seismic Parameters (Table 9-1)**:
| System | R | $C_d$ | $\Omega_0$ |
|--------|---|--------|-----------|
| Building frame | 3.0 | 3.0 | 3.0 |
| Moment frame | 2.0 | 2.0 | 2.0 |
| Enhanced connection braced frame | 2.0 | 2.0 | 2.0 |
| Special concentric braced frame | 2.0 | 2.0 | 2.0 |

**Height Limit**: 70 ft for non-building structures

**When to Use**:
- Seismic design in SDC B-F
- Selecting appropriate R factors
- Braced frame design
- Cooling tower structures

## Appendices

### Appendix A: Symbols and Notations

**File**: `ASCE_SEI_74-23_part3_pages51-75.md` (pages 56-62)

**Content**:
- Complete symbol table
- Definitions for all variables
- Units (ksi, in, kip, °F)
- Section references

**When to Use**:
- Looking up symbol definitions
- Verifying units
- Understanding notation

### Appendix B: Glossary

**File**: `ASCE_SEI_74-23_part3_pages51-75.md` (pages 64-67)

**Content**:
- Technical term definitions
- Fundamental concepts
- Design terminology

**When to Use**:
- Understanding GFRP-specific terms
- Clarifying design concepts
- Learning terminology

### Appendix C8.3.2: Multi-Row Bolted Connections Full Formulae

**File**: `ASCE_SEI_74-23_part5_pages101-125.md` (pages 97-98)

**Content**:
- Detailed formulas for 2-row and 3-row connections
- Net tension strength by row
- Effective width calculations
- Stress concentration factors

**When to Use**:
- Detailed multi-row connection design
- Connection research
- Verifying simplified formulas

## Commentary Chapters (C1-C9)

Each chapter has corresponding commentary explaining:
- Background and rationale
- Research basis
- Design examples
- Comparisons to other standards
- Limitations and assumptions

**When to Use Commentary**:
- Understanding "why" behind requirements
- Learning design philosophy
- Seeing worked examples
- Research and development

## Quick Reference: Chapter to Topic Mapping

| Need to Design | Chapter | Key Sections |
|----------------|---------|--------------|
| **Tension rod** | 3 | 3.2, 3.3 |
| **Column** | 4 | 4.2, 4.3, 4.4 |
| **Beam** | 5 | 5.2, 5.3 |
| **Beam-column** | 6 | 6.3 |
| **Connection** | 8 | 8.2, 8.3 |
| **Plate/deck** | 7 | 7.5, 7.6, 7.7 |
| **Seismic frame** | 9 | 9.1, 9.2 |
| **Material properties** | 1, 2 | 1.3, 2.4 |
| **Load combinations** | 1 | 1.5 |
| **Environmental factors** | 2 | 2.4 |
| **Deflection limits** | 2 | 2.6 |
| **Symbols** | App A | - |
| **Terminology** | App B | - |

## File Location Quick Reference

| Pages | Content | File |
|-------|---------|------|
| 1-25 | Ch 1, Ch 2 (partial) | part1_pages1-25.md |
| 26-50 | Ch 2 (continued), Ch 3, Ch 4, Ch 5 (partial) | part2_pages26-50.md |
| 51-75 | Ch 5 (continued), Ch 6, Ch 7, App A, App B | part3_pages51-75.md |
| 76-100 | Ch 8 (partial) | part4_pages76-100.md |
| 101-125 | Ch 8 (continued), Ch 9, References, Index | part5_pages101-125.md |

---

**Navigation Tip**: Use chapter numbers and section numbers to quickly locate information across the 5 markdown files.

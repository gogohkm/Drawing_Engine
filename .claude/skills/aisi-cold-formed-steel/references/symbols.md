# Common Symbols and Notation

Quick reference for mathematical symbols used in AISI S100-16 cold-formed steel design.

**Note:** For complete symbols section, see Volume 2 pages 25-73.

---

## Geometric Properties

| Symbol | Definition | Units |
|--------|------------|-------|
| A | Gross area of cross-section | in² |
| A_e | Effective area at stress F_n | in² |
| A_g | Gross area of cross-section | in² |
| A_n | Net area | in² |
| b | Width of element (flat width excluding corners) | in |
| b_e | Effective width | in |
| d | Depth of section | in |
| D | Outside diameter | in |
| h | Height (web depth, etc.) | in |
| I | Moment of inertia | in⁴ |
| I_e | Effective moment of inertia | in⁴ |
| I_x, I_y | Moment of inertia about x, y axes | in⁴ |
| J | Torsional constant | in⁴ |
| L | Span length or member length | in or ft |
| L_b | Unbraced length for bending | in |
| L_x, L_y | Unbraced length for buckling about x, y axes | in |
| L_t | Unbraced length for twisting | in |
| r | Radius of gyration (r = √(I/A)) | in |
| r_o | Polar radius of gyration about shear center | in |
| r_x, r_y | Radius of gyration about x, y axes | in |
| S | Section modulus (S = I/c) | in³ |
| S_e | Effective section modulus | in³ |
| S_f | Section modulus referenced to extreme fiber | in³ |
| t | Thickness (base steel thickness) | in |
| t_c | Coating thickness | in |
| t_d | Design thickness (t - t_c or as specified) | in |
| w | Flat width of element | in |
| x_o, y_o | Coordinates of shear center | in |

---

## Material Properties

| Symbol | Definition | Units |
|--------|------------|-------|
| E | Modulus of elasticity (steel: 29,500 ksi) | ksi |
| F_u | Tensile strength | ksi |
| F_y | Yield strength (0.2% offset) | ksi |
| G | Shear modulus (steel: 11,300 ksi) | ksi |
| μ | Poisson's ratio (steel: 0.3) | - |

---

## Strength and Stress

| Symbol | Definition | Units |
|--------|------------|-------|
| F_cr | Critical buckling stress | ksi |
| F_cre | Elastic flexural, torsional, or flexural-torsional buckling stress | ksi |
| F_crl | Elastic local buckling stress | ksi |
| F_crd | Elastic distortional buckling stress | ksi |
| f | Calculated stress | ksi |
| M | Bending moment | kip-in |
| M_a | Required moment (ASD) | kip-in |
| M_n | Nominal moment strength | kip-in |
| M_u | Required moment (LRFD/LSD) | kip-in |
| M_cre | Critical elastic local buckling moment | kip-in |
| M_crl | Critical elastic local buckling moment | kip-in |
| M_crd | Critical elastic distortional buckling moment | kip-in |
| M_ne | Nominal flexural strength for lateral-torsional buckling | kip-in |
| M_nl | Nominal flexural strength for local buckling | kip-in |
| M_nd | Nominal flexural strength for distortional buckling | kip-in |
| P | Axial load | kip |
| P_a | Required axial strength (ASD) | kip |
| P_n | Nominal axial strength | kip |
| P_u | Required axial strength (LRFD/LSD) | kip |
| P_cre | Elastic flexural, torsional, or flexural-torsional buckling load | kip |
| P_crl | Critical elastic local buckling load | kip |
| P_crd | Critical elastic distortional buckling load | kip |
| P_ne | Nominal axial strength for flexural, torsional, or FT buckling | kip |
| P_nl | Nominal axial strength for local buckling | kip |
| P_nd | Nominal axial strength for distortional buckling | kip |
| R | Nominal strength (general) | varies |
| R_a | Required strength (ASD) | varies |
| R_n | Nominal strength | varies |
| R_u | Required strength (LRFD/LSD) | varies |
| V | Shear force | kip |
| V_a | Required shear strength (ASD) | kip |
| V_n | Nominal shear strength | kip |
| V_u | Required shear strength (LRFD/LSD) | kip |

---

## Design Factors

| Symbol | Definition | Units |
|--------|------------|-------|
| φ | Resistance factor (LRFD/LSD) | - |
| φ_b | Resistance factor for bending (typically 0.90 or 0.95) | - |
| φ_c | Resistance factor for compression (typically 0.85) | - |
| φ_t | Resistance factor for tension (typically 0.90) | - |
| φ_v | Resistance factor for shear (typically 0.90 or 0.95) | - |
| Ω | Safety factor (ASD) | - |
| Ω_b | Safety factor for bending (typically 1.67 or 1.60) | - |
| Ω_c | Safety factor for compression (typically 1.80) | - |
| Ω_t | Safety factor for tension (typically 1.67) | - |
| Ω_v | Safety factor for shear (typically 1.67 or 1.60) | - |

---

## Slenderness Parameters

| Symbol | Definition | Units |
|--------|------------|-------|
| λ | Slenderness parameter (generic) | - |
| λ_l | Local slenderness (DSM): √(F_y/F_crl) | - |
| λ_d | Distortional slenderness (DSM): √(F_y/F_crd) | - |
| λ_c | Column slenderness: (KL/r)√(F_y/E) or √(F_y/F_cre) | - |
| ρ | Reduction factor for effective width | - |

---

## Connection Symbols

| Symbol | Definition | Units |
|--------|------------|-------|
| A_b | Nominal bolt area | in² |
| A_br | Bearing area | in² |
| d | Diameter (bolt, screw, weld) | in |
| d_h | Diameter of hole | in |
| e | Edge distance | in |
| F_u1, F_u2 | Tensile strength of connected parts | ksi |
| F_xx | Weld electrode classification strength | ksi |
| L | Length (weld, connection) | in |
| n | Number of fasteners | - |
| P_n | Nominal connection strength | kip or kip/in |
| s | Spacing between fasteners | in |
| t_1, t_2 | Thickness of connected parts | in |

---

## Effective Width Method (EWM) Symbols

| Symbol | Definition | Units |
|--------|------------|-------|
| b | Flat width of compression element | in |
| b_e | Effective width | in |
| f | Calculated compression stress | ksi |
| F_crl | Elastic local buckling stress | ksi |
| k | Plate buckling coefficient | - |
| ρ | Reduction factor: (1 - 0.22/λ)/λ when λ > 0.673 | - |
| λ | Element slenderness: √(f/F_crl) | - |

---

## Direct Strength Method (DSM) Symbols

| Symbol | Definition | Units |
|--------|------------|-------|
| F_crl | Elastic critical local buckling stress | ksi |
| F_crd | Elastic critical distortional buckling stress | ksi |
| F_cre | Elastic critical global buckling stress | ksi |
| F_y | Yield strength | ksi |
| λ_l | Local slenderness: √(F_y/F_crl) | - |
| λ_d | Distortional slenderness: √(F_y/F_crd) | - |
| M_crl, M_crd, M_cre | Critical elastic buckling moments | kip-in |
| P_crl, P_crd, P_cre | Critical elastic buckling loads | kip |

---

## Subscript Meanings

| Subscript | Meaning |
|-----------|---------|
| a | allowable (ASD) |
| b | bending, bolt |
| c | compression, critical, column |
| cr | critical (buckling) |
| cre | critical elastic (global buckling) |
| crl | critical elastic local buckling |
| crd | critical elastic distortional buckling |
| d | distortional, design |
| e | effective, elastic |
| f | fiber, flange |
| g | gross |
| l | local (buckling) |
| n | nominal, net |
| t | tension, torsion |
| u | ultimate, required (LRFD/LSD) |
| v | shear |
| w | web, weld |
| x, y, z | axes |
| 1, 2 | different parts or locations |

---

## Common Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| ASD | Allowable Strength Design |
| LRFD | Load and Resistance Factor Design |
| LSD | Limit States Design |
| EWM | Effective Width Method |
| DSM | Direct Strength Method |
| LTB | Lateral-Torsional Buckling |
| FT | Flexural-Torsional (buckling) |

---

## Units

**Default AISI S100 units:**
- Force: kip (1 kip = 1000 lb)
- Length: inch (in)
- Stress: ksi (kip/in²)
- Moment: kip-in
- Distributed load: kip/in or kip/ft

**Conversions:**
- 1 kip = 1000 lb = 4.448 kN
- 1 in = 25.4 mm
- 1 ksi = 6.895 MPa
- 1 kip-in = 0.113 kN-m

---

## Greek Letters

| Symbol | Name | Common Use |
|--------|------|------------|
| α | alpha | Coefficient, angle |
| β | beta | Coefficient |
| γ | gamma | Load factor |
| δ | delta | Deflection |
| λ | lambda | Slenderness parameter |
| μ | mu | Poisson's ratio (0.3 for steel), friction coefficient |
| ν | nu | Poisson's ratio (alternate notation) |
| ρ | rho | Reduction factor (effective width) |
| φ | phi | Resistance factor (LRFD/LSD) |
| Ω | omega | Safety factor (ASD) |

---

## Special Notation

**Effective properties:**
- Subscript "e" indicates effective (accounting for local buckling)
- Example: A_e, I_e, S_e

**Critical buckling:**
- Subscript "cr" indicates critical buckling value
- Example: F_cr, M_cr, P_cr

**DSM buckling modes:**
- "crl" = critical elastic local buckling
- "crd" = critical elastic distortional buckling
- "cre" = critical elastic global (Euler) buckling

**Nominal vs Design:**
- R_n = Nominal strength
- φR_n = Design strength (LRFD)
- R_n/Ω = Allowable strength (ASD)

---

## Reference

**Complete symbols:** See AISI S100-16 Volume 2, pages 25-73

**Variable definitions:** Look for "where:" sections following equations in the specification

**Context-specific symbols:** Some symbols have different meanings in different chapters (always check context)

---

**Last Updated:** 2025-11-10
**Source:** AISI S100-16 (2016 Edition)

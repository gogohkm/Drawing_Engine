# Chapter H: Design of Members for Combined Forces and Torsion

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 62-63
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [H.1 MEMBERS SUBJECT TO FLEXURE AND AXIAL FORCE](#h1-members-subject-to-flexure-and-axial-force)
- [H.2 MEMBERS SUBJECT TO TORSION](#h2-members-subject-to-torsion)
  - [H.2.1 Pipes and Round or Oval Tubes](#h21-pipes-and-round-or-oval-tubes)
  - [H.2.2 Rectangular Tubes](#h22-rectangular-tubes)
  - [H.2.3 Rods](#h23-rods)
  - [H.2.4 Open Shapes](#h24-open-shapes)
- [H.3 MEMBERS SUBJECT TO TORSION, FLEXURE, SHEAR, AND/OR AXIAL COMPRESSION](#h3-members-subject-to-torsion-flexure-shear-andor-axial-compression)
  - [H.3.1 Flat Elements](#h31-flat-elements)
  - [H.3.2 Curved Elements](#h32-curved-elements)

---

----------|----------|------------|
| torsional rupture | 0.75 | 1.95 |
| other torsional limit states | 0.90 | 1.65 |

For the limit state of torsional rupture, the shear stress $F_s$ corresponding to the torsional strength is

For unwelded members

$$F_s = F_{su} / k_t$$ (H.2-1)

For welded members

$$F_s = F_{su}(1 - A_{wz} / A_g) / k_t + F_{suw} A_{wz} / A_g$$ (H.2-2)

For the limit states of shear yielding and shear buckling, the shear stress $F_s$ corresponding to the torsional strength is

For unwelded members

$$F_s = F_{sv}$$ (H.2-3)

For welded members

$$F_s = F_{sv}(1 - A_{wz} / A_g) + F_{svw} A_{wz} / A_g$$ (H.2-4)

where

$F_{sv}$ = shear stress corresponding to the torsional strength for an element determined using Section H.2 if no part of the cross section were weld-affected. Use buckling constants for unwelded metal (Table B.4.1 or Table B.4.2) and $F_{sy}$.

$F_{svw}$ = shear stress corresponding to the torsional strength for an element determined using Section H.2 if the entire cross section were weld-affected. Use buckling constants for weld-affected zones (Table B.4.1) and $F_{syw}$.

$A_{wz}$ = cross sectional area of the weld-affected zone
$A_g$ = gross cross sectional area of the element.

### H.2.1 Pipes and Round or Oval Tubes

The nominal torsional strength $T_n$ for pipes and round or oval tubes is

$$T_n = F_s J / R$$ (H.2-5)

For the limit state of torsional rupture, the shear stress $F_s$ corresponding to the torsional strength shall be determined in accordance with Section H.2.

For the limit state of torsional yielding and torsional buckling, the shear stress $F_s$ corresponding to the shear strength is

| LIMIT STATE | $F_s$ | $\lambda$ | Slenderness Limits |
|-------------|-------|-----------|-------------------|
| yielding | $F_{sy}$ | $\lambda \leq \lambda_1$ | $\lambda_1 = \frac{B_s - F_{sy}}{1.25D_s}$ |
| inelastic buckling | $B_s - 1.25D_s \lambda$ | $\lambda_1 < \lambda < \lambda_2$ | |
| elastic buckling | $\frac{\pi^2 E}{(1.25\lambda)^2}$ | $\lambda \geq \lambda_2$ | $\lambda_2 = \frac{C_s}{1.25}$ |

Buckling constants $B_s$, $D_s$, and $C_s$ are given in Table B.4.1 or B.4.2.

$$\lambda = 2.9 \left(\frac{R_b}{t}\right)^{5/8} \left(\frac{L_b}{R_b}\right)^{1/4}$$ (H.2-6)

- $R_b$ = mid-thickness radius of a pipe or round tube or the maximum mid-thickness radius of an oval tube
- $t$ = wall thickness

- $L_b$ = length between transverse stiffeners, or overall length if no transverse stiffeners are present
- $R$ = outside radius of the pipe or tube
- $J$ = torsion constant of the pipe or tube

### H.2.2 Rectangular Tubes

The nominal torsional strength $T_n$ for rectangular tubes is

$$T_n = F_s C$$ (H.2-7)

where $C$ is the torsional shear constant.

For the limit state of torsional rupture, the shear stress $F_s$ corresponding to the torsional strength is determined in accordance with Section H.2.

For the limit state of torsional yielding and torsional buckling, $F_s$ is determined in accordance with Section G.2 for the side with the larger slenderness.

### H.2.3 Rods

The nominal torsional strength $T_n$ for rods for the limit state of torsional yielding is

For unwelded members:

$$T_n = 0.196F_{sy} D^3$$ (H.2-8)

For welded members

$$T_n = 0.196F_{syw} D^3$$ (H.2-9)

The nominal torsional strength $T_n$ for rods for the limit state of torsional rupture is

For unwelded members

$$T_n = 0.262F_{su} D^3 / k_t$$ (H.2-10)

For welded members

$$T_n = 0.262F_{suw} D^3$$ (H.2-11)

where

$D$ = diameter of the rod

### H.2.4 Open Shapes

The nominal torsional strength $T_n$ for open shapes is the lesser of:

a) the limit states of yielding, local buckling, and rupture due to normal stress determined in accordance with Chapter B, and

b) the limit states of yielding, local buckling, and rupture due to shear stress determined in accordance with Chapter G.

## H.3 MEMBERS SUBJECT TO TORSION, FLEXURE, SHEAR, AND/OR AXIAL COMPRESSION

### H.3.1 Flat Elements

Stresses in flat elements subject to torsion, flexure, shear, and/or axial compression shall satisfy the following:

$$f_c / (\phi F_c) + [f_b / (\phi F_b)]^2 + [f_s / (\phi F_s)]^2 \leq 1.0$$ (H.3-1 LRFD)

$$f_c / (F_c / \Omega) + [f_b / (F_b / \Omega)]^2 + [f_s / (F_s / \Omega)]^2 \leq 1.0$$ (H.3-1 ASD)

where

- $f_c$ = compressive stress due to axial compression
- $f_b$ = compressive stress due to flexure
- $f_s$ = shear stress due to shear and torsion
- $F_c$ = axial compressive stress corresponding to the nominal axial compressive strength
- $F_b$ = flexural compressive stress corresponding to the nominal flexural compressive strength
- $F_s$ = shear stress corresponding to the nominal shear strength

### H.3.2 Curved Elements

Stresses in curved elements subject to torsion, flexure, shear, and/or axial compression shall satisfy the following:

$$f_c / (\phi F_c) + f_b / (\phi F_b) + [f_s / (\phi F_s)]^2 \leq 1.0$$ (H.3-2 LRFD)

$$f_c / (F_c / \Omega) + f_b / (F_b / \Omega) + [f_s / (F_s / \Omega)]^2 \leq 1.0$$ (H.3-2 ASD)

where

- $f_c$ = compressive stress due to axial compression
- $f_b$ = compressive stress due to flexure
- $f_s$ = shear stress due to shear and torsion
- $F_c$ = axial compressive stress corresponding to the nominal axial compressive strength
- $F_b$ = flexural compressive stress corresponding to the nominal flexural compressive strength
- $F_s$ = shear stress corresponding to the nominal shear strength

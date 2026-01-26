# Chapter F: Design of Members for Flexure

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 54-58
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [F.1 GENERAL PROVISIONS](#f1-general-provisions)
- [F.2 YIELDING AND RUPTURE](#f2-yielding-and-rupture)
- [F.3 LOCAL BUCKLING](#f3-local-buckling)
  - [F.3.1 Weighted Average Method](#f31-weighted-average-method)
  - [F.3.2 Direct Strength Method](#f32-direct-strength-method)
  - [F.3.3 Limiting Element Method](#f33-limiting-element-method)
- [F.4 LATERAL-TORSIONAL BUCKLING](#f4-lateral-torsional-buckling)
- [F.4.1 Bending Coefficient $C_b$](#f41-bending-coefficient-c_b)
  - [F.4.1.1 Members Supported on Both Ends](#f411-members-supported-on-both-ends)
  - [F.4.1.2 Cantilevers](#f412-cantilevers)
- [F.4.2 Slenderness for Lateral-Torsional Buckling](#f42-slenderness-for-lateral-torsional-buckling)
  - [F.4.2.1 Shapes Symmetric About the Bending Axis](#f421-shapes-symmetric-about-the-bending-axis)
  - [F.4.2.2 Singly Symmetric Open Shapes Unsymmetric About the Bending Axis](#f422-singly-symmetric-open-shapes-unsymmetric-about-the-bending-axis)
  - [F.4.2.3 Closed Shapes](#f423-closed-shapes)
  - [F.4.2.4 Rectangular Bars](#f424-rectangular-bars)
  - [F.4.2.5 Any Shape](#f425-any-shape)
- [F.5.1 Bending About Geometric Axes](#f51-bending-about-geometric-axes)
- [F.5.2 Bending About Principal Axes](#f52-bending-about-principal-axes)
- [F.5 SINGLE ANGLES](#f5-single-angles)

---

----------|----------|------------|
| rupture | 0.75 | 1.95 |
| other flexural limit states | 0.90 | 1.65 |

For all shapes except single angles, determine the nominal flexural strength using Sections F.2, F.3, and F.4. For single angles, use Section F.5.

## F.2 YIELDING AND RUPTURE

For the limit state of yielding, the nominal flexural strength $M_n = M_{ny}$ where:

a) For wrought products, $M_{ny}$ is the least of $Z F_{ty}$, $1.5S_x F_{ty}$, and $1.5S_c F_{cy}$.

b) For cast products, $M_{ny}$ is the lesser of $S_t F_{ty}$ and $S_c F_{cy}$.

For the limit state of rupture, the nominal flexural strength $M_n = M_{nu}$ where

$$M_{nu} = Z F_{tu} / k_t$$ (F.2-1)

where

- $Z$ = plastic modulus
- $S_t$ = section modulus on the tension side of the neutral axis
- $S_c$ = section modulus on the compression side of the neutral axis

## F.3 LOCAL BUCKLING

The nominal flexural strength for the limit state of local buckling $M_n = M_{nb}$ shall be determined by Section F.3.1, F.3.2, or F.3.3. Local buckling is not a limit state for a wire, rod, or bar.

### F.3.1 Weighted Average Method

The nominal flexural strength for local buckling $M_{nb}$ shall be determined as

$$M_{nb} = F_c I_f / c_{cf} + F_b I_e / c_{ce}$$ (F.3-1)

where

- $F_c$ = stress corresponding to the strength of an element in uniform compression determined using Sections B.5.4.1 through B.5.4.6. The strength of stiffened elements shall not exceed the strength of an intermediate stiffener or an edge stiffener.
- $F_b$ = stress corresponding to the strength of an element in flexural compression determined using Sections B.5.5.1 through B.5.5.5.
- $c_{cf}$ = distance from the centerline of a uniform compression element to the cross section's neutral axis
- $c_{ce}$ = distance from a flexural compression element's extreme compression fiber to the cross section's neutral axis
- $I_f$ = moment of inertia of the uniform stress elements about the cross section's neutral axis. These elements include the elements in uniform compression and the elements in uniform tension and their edge or intermediate stiffeners.
- $I_e$ = moment of inertia of the flexural compression elements about the cross section's neutral axis. These elements include the elements in flexure and their intermediate stiffeners.

If there are stiffeners located farther than the compression flange from the cross section's neutral axis, the compressive flexural strength shall not exceed

$$F_{cy} I_f / c_{cf} + F_b I_e / c_{ce}$$

where

$c_{cs}$ = distance from the cross section's neutral axis to the extreme fiber of uniform compression element

### F.3.2 Direct Strength Method

The nominal flexural strength for local buckling $M_{nb}$ shall be determined as

| LIMIT STATE | $M_{nb}$ | $\lambda_{eq}$ | Slenderness Limits |
|-------------|----------|----------------|-------------------|
| yielding | $M_{ny}$ | $\lambda_{eq} \leq \lambda_1$ | $\lambda_1 = \frac{B_w - F_{cy}}{D_b}$ |
| inelastic buckling | $M_{ny} - \left(M_{ny} - \frac{\pi^2 ES_c}{C_b^2}\right) \frac{(\lambda_{eq} - \lambda_1)}{(C_b - \lambda_1)}$ | $\lambda_1 < \lambda_{eq} < \lambda_2$ | |
| post-buckling | $\frac{S_c k_2 \sqrt{B_b E}}{\lambda_{eq}}$ | $\lambda_{eq} \geq \lambda_2$ | $\lambda_2 = C_b$ |

where $\lambda_{eq} = \pi \sqrt{\frac{E}{F_e}}$ (F.3-2)

$F_e$ = the elastic local buckling stress of the cross section determined by analysis

### F.3.3 Limiting Element Method

The nominal flexural strength for local buckling $M_{nb}$ shall be determined by limiting the stress in any element to the local buckling stress of that element, determined in accordance with Sections B.5.4.1 through B.5.4.5 and B.5.5.1 through B.5.5.4.

## F.4 LATERAL-TORSIONAL BUCKLING

For the limit state of lateral-torsional buckling, the nominal flexural strength $M_n = M_{nmb}$ where:

| LIMIT STATE | $M_{nmb}$ | SLENDERNESS LIMITS |
|-------------|-----------|-------------------|
| inelastic buckling | $M_{ny}\left(1 - \frac{\lambda}{C_b}\right)$ $\frac{\pi^2 E\lambda S_{xc}}{C_b^2}$ | $\lambda < C_b$ |
| elastic buckling | $\pi^2 ES_{xc} / \lambda^2$ | $\lambda \geq C_b$ |

for lateral-torsional buckling about an axis designated as the $x$-axis.

To determine the lateral-torsional buckling slenderness $\lambda$ use Sections F.4.2.1 through F.4.2.5. If more than one Section applies, any applicable Section shall be used.

For members without welds determine the lateral-torsional buckling strength $M_{nmb} = M_{nmbo}$ using $C_b$ for unwelded material using Table B.4.1 or B.4.2 and $F_{cy}$.

For members that are fully weld-affected determine the lateral-torsional buckling strength $M_{nmb} = M_{nmbw}$ using $C_b$ for welded material using Table B.4.1 and $F_{cyw}$.

For members with transverse welds and:

a) supported at both ends with no transverse weld farther than $0.05L$ from the member ends, $M_{nmb} = M_{nmbo}$.

b) supported at both ends with a transverse weld farther than $0.05L$ from the member ends, or supported at only one end with a transverse weld $M_{nmb} = M_{nmbw}$.

For members with longitudinal welds, the lateral-torsional buckling strength is:

$$M_{nmb} = M_{nmbo}(1 - A_{wz} / A_g) + M_{nmbw}(A_{wz} / A_g)$$ (F.4-1)

where

$A_g$ = area of the member farther than $2r/3$ from the neutral axis, where $c$ is the distance from the neutral axis to the extreme compression fiber.

$A_{wz}$ = weld-affected area within $A_g$

## F.4.1 Bending Coefficient $C_b$

### F.4.1.1 Members Supported on Both Ends

For members subjected to uniform bending moment, the bending coefficient $C_b = 1$. For other members, $C_b$ shall be taken as 1 or determined as follows.

For singly and doubly symmetric shapes between brace points:

a) If $I_w / I_y \leq 0.1$ or $I_w / I_y \geq 0.9, C_b = 1$

b) If $0.1 < I_w / I_y < 0.9$,

$$C_b = \frac{4M_{max}}{\sqrt{M_{max}^2 + 4M_A^2 + 7M_B^2 + 4M_C^2}} \quad R_m \leq 3.0$$ (F.4-2)

where

- $M_{max}$ = absolute value of the maximum moment in the unbraced segment
- $M_A$ = absolute value of the moment at the quarter point of the unbraced segment
- $M_B$ = absolute value of the moment at the midpoint of the unbraced segment
- $M_C$ = absolute value of the moment at the three-quarter point of the unbraced segment
- $R_m$ = 1.0 except for unbraced lengths of singly-symmetric members subjected to double-curvature bending from transverse loading,

$$R_m = 0.5 + 2\left(\frac{I_d}{I_y}\right)^2$$

$I_d$ = moment of inertia of the flange on the negative side of the midheight (where the direction of the load is the positive direction about the minor axis of the shape)

$I_y$ = minor axis moment of inertia of the shape

### F.4.1.2 Cantilevers

For doubly symmetric shape cantilevers unbraced at the free end with loads applied at the centroid, for a concentrated load applied at the free end $C_b = 1.3$ and for uniform transverse load $C_b = 2.1$.

## F.4.2 Slenderness for Lateral-Torsional Buckling

### F.4.2.1 Shapes Symmetric About the Bending Axis

The slenderness for shapes symmetric about the bending axis is

$$\lambda = \frac{L_b}{r_{yt}\sqrt{C_b}}$$ (F.4-3)

where $r_{yt}$ is:

a) Between brace points of beams subjected to end moment only or to transverse loads applied at the beam's neutral axis, or at brace points:

$$r_{yt} = \sqrt{\frac{I_y}{S_t}\sqrt{C_w + 0.038JL_b^2}}$$ (F.4-4)

b) Between brace points of beams subjected to transverse loads applied at the top or bottom fiber (where the load is free to move laterally with the beam if the beam buckles):

$$r_{yt} = \sqrt{\frac{I_y}{S_t}\sqrt{\frac{d}{4} + \sqrt{\frac{d^2}{16} + \frac{C_w}{I_y} + \frac{0.038JL_b^2}{I_y}}}}$$ (F.4-5)

$d/4$ is negative when the load acts toward the shear center and positive when the load acts away from the shear center.

where

- The $y$-axis is the principal axis in the plane of bending
- $I_y$ = moment of inertia about the $y$-axis
- $S_t$ = section modulus about the $x$-axis
- $d$ = depth of the beam

Alternately, for channels and I-shaped sections symmetric about the bending axis $r_{yt}$ shall be taken as $r_yd/(2r_x)$ or $1.2r_y$.

### F.4.2.2 Singly Symmetric Open Shapes Unsymmetric About the Bending Axis

For singly symmetric open shapes unsymmetric about the bending axis using $I_w \leq I_y$, determine the slenderness using Section F.4.2.1 where $r_{yt}$ is calculated with $I_w$, $S_t$ and $J$ determined as though both flanges were the same as the compression flange with the overall depth $d$ remaining the same.

### F.4.2.3 Closed Shapes

For closed shapes, the slenderness is

$$\lambda = 2.3 \sqrt{\frac{L_b S_y}{C_b \sqrt{I_y J}}}$$ (F.4-6)

### F.4.2.4 Rectangular Bars

For rectangular bars, the slenderness is

$$\lambda = \frac{2.3}{t} \sqrt{\frac{dL_b}{C_b}}$$ (F.4-7)

where

- $d$ = dimension of the bar in the plane of flexure
- $t$ = dimension of the bar perpendicular to the plane of flexure

### F.4.2.5 Any Shape

For any shape symmetric or unsymmetric about the bending axis the slenderness is:

$$\lambda = \pi \sqrt{\frac{ES_x}{C_b M_e}}$$ (F.4-8)

where $M_e$ is the elastic lateral-torsional buckling moment for a laterally unbraced span subjected to uniform bending determined by analysis or as:

$$M_{nmb} = \left[\frac{\pi^2 E}{\left(\frac{L_b}{r_{yt}\sqrt{C_b}}\right)^2}\right]^{1/3} F_{cy}^{2/3} S_{xc}$$ (F.4-13)

Buckling constants $B_b$, $D_b$, and $C_b$ are given in Tables B.4.1 and B.4.2.

b) For the limit state of yielding (Figure F.5.3):

![Figure F.5.3 showing angle orientations X, Z, W](description)

**Figure F.5.3**

$$M_n = 1.5M_y$$ (F.5-1)

where $M_y$ = yield moment about the axis of bending.

c) For the limit state of lateral-torsional buckling:

(1) for $M_e \leq M_y$, $M_n = (0.92 - 0.17M_e / M_y)M_y$ (F.5-2)

(2) for $M_e > M_y$, $M_n = (1.92 - 1.17\sqrt{M_e / M_y})M_y \leq 1.3M_y$ (F.5-3)

where $M_e$ = elastic lateral-torsional buckling moment from Section F.5.1 or F.5.2.

$C_b$ between brace points shall be determined using Equation F.2-1 but shall not exceed 1.5.

## F.5.1 Bending About Geometric Axes

Bending about a geometric axis is shown in Figure F.5.4. For combined axial compression and bending, resolve moments about principal axes and use Section F.5.2.

![Figure F.5.4 showing angle subsections](description)

Subsections (a) and (b)  Subsection (c)

**Figure F.5.4**

a) *Angles with continuous lateral-torsional restraint*: $M_e$ is the lesser of:

(1) local buckling strength determined by Section F.5a.
(2) yield strength determined by Section F.5b.

b) *Equal leg angles with lateral-torsional restraint only at the point of maximum moment*: Strengths shall be calculated with $S_c$ being the geometric section modulus. $M_e$ is the least of:

(1) local buckling strength determined by Section F.5a.
(2) yield strength determined by Section F.5b.
(3) If the leg tip is in compression, lateral-torsional buckling strength determined by Section F.5c with

$$M_e = \frac{0.73Eb^4tC_b}{L_b^2} \left[\sqrt{1 + 0.88(L_bt / b^2)^2} - 1\right]$$ (F.5-4)

If the leg tip is in tension, lateral-torsional buckling strength is determined by Section F.5c with

$$M_e = \frac{0.73Eb^4tC_b}{L_b^2} \left[\sqrt{1 + 0.88(L_bt / b^2)^2} + 1\right]$$ (F.5-5)

c) *Equal leg angles without lateral-torsional restraint*: Strengths shall be calculated with $S_c$ equal to 0.80 of the geometric section modulus.

If the leg tip is in compression, $M_e$ is the lesser of:

(1) local buckling strength determined by Section F.5a(1)
(2) lateral-torsional buckling strength determined by F.5c with

$$M_e = \frac{0.58Eb^4tC_b}{L_b^2} \left[\sqrt{1 + 0.88(L_bt / b^2)^2} - 1\right]$$ (F.5-6)

If the leg tip is in tension, $M_e$ is the lesser of:

(1) yield strength determined by Section F.5b
(2) lateral-torsional buckling strength determined by Section F.5c with

$$M_e = \frac{0.58Eb^4tC_b}{L_b^2} \left[\sqrt{1 + 0.88(L_bt / b^2)^2} + 1\right]$$ (F.5-7)

d) *Unequal leg angles without lateral-torsional restraint*: moments about the geometric axes shall be resolved into moments about the principal axes and the angle shall be designed as an angle bent about a principal axis (Section F.5.2).

## F.5.2 Bending About Principal Axes

Bending about principal axes is shown in Figure F.5.5.

![Figure F.5.5 showing angles - Z, W orientations](description)

Minor Axis Bending  Major Axis Bending

**Figure F.5.5**

a) *Major axis bending*: $M_e$ is the lesser of:

(1) local buckling strength determined by Section F.5a for the leg with its tip in compression

(2) lateral-torsional buckling strength determined by Section F.3c, where

$$M_e = \frac{9EAr_oC_b}{L_b} \left[\sqrt{1 + \left(4.4 \frac{b_o r_z}{L_b I_z}\right)^2} + 4.4 \frac{b_o r_z}{L_b I_z}\right]$$ (F.5-8)

$$\beta_w = \left[\frac{1}{I_z}\int_z \left(w^2 + z^2\right)dA\right] - 2z_{so}$$ (F.5-9)

$\beta_w$ is the coefficient of monosymmetry about the major principal axis. $\beta_w$ is positive when the short leg is in compression, negative when the long leg is in compression, and zero for equal-leg angles. (See the commentary for values for common angle sizes and equations for determining $\beta_w$.) If the short leg is in compression anywhere along the unbraced length of the angle, $\beta_w$ shall be taken as negative.

$z_{so}$ = coordinate along the $z$-axis of the shear center with respect to the centroid

$I_z$ = moment of inertia about the major principal axis

b) *Minor axis bending*:

(1) If the leg tips are in compression, $M_e$ is the lesser of the local buckling strength determined by Section F.5a(1) and the yield strength determined by Section F.5b.

(2) If the leg tips are in tension, $M_e$ is the yield strength determined by Section F.5b.

## F.5 SINGLE ANGLES

For single angles, the nominal flexural strength $M_n$ shall be determined as follows.

a) For the limit state of local buckling:

(1) If a leg tip is a point of maximum compression (Figure F.5.1):

![Figure F.5.1 showing angles X, Z, W](description)

**Figure F.5.1**

| LIMIT STATE | $M_n$ | $b/t$ | Slenderness Limits |
|-------------|-------|-------|--------------------|
| yielding | $1.5F_{cy}S_c$ | $b/t \leq \lambda_1$ | $\lambda_1 = \frac{B_b - 1.5F_{cy}}{4.0D_b}$ |
| inelastic buckling | $[B_b - 4.0D_b (b/t)]S_c$ | $\lambda_1 < b/t < \lambda_2$ | |
| elastic buckling | $\frac{\pi^2 ES_c}{(4.0b/t)^2}$ | $b/t \geq \lambda_2$ | $\lambda_2 = \frac{C_w}{4.0}$ |

Buckling constants $B_b$, $D_b$, and $C_w$ are given in Tables B.4.1 and B.4.2.

(2) If a leg is in uniform compression (Figure F.5.2):

![Figure F.5.2 showing angle X](description)

**Figure F.5.2**

| LIMIT STATE | $M_n$ | $b/t$ | Slenderness Limits |
|-------------|-------|-------|--------------------|
| yielding | $F_{cy}S_c$ | $b/t \leq \lambda_1$ | $\lambda_1 = \frac{B_b - F_{cy}}{5.0D_b}$ |
| inelastic buckling | $B_b - 5.0D_c (b/t) S_c$ | $\lambda_1 < b/t < \lambda_2$ | |
| elastic buckling | $\frac{\pi^2 ES_c}{(5.0b/t)^2}$ | $b/t \geq \lambda_2$ | $\lambda_2 = \frac{C_w}{5.0}$ |

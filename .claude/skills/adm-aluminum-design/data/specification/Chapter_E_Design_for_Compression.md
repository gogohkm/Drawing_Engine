# Chapter E: Design of Members for Compression

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 52-53
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [E.1 GENERAL PROVISIONS](#e1-general-provisions)
- [E.2 MEMBER BUCKLING](#e2-member-buckling)
  - [E.2.1 Flexural Buckling](#e21-flexural-buckling)
  - [E.2.2 Torsional and Flexural-Torsional Buckling](#e22-torsional-and-flexural-torsional-buckling)
- [E.3 LOCAL BUCKLING](#e3-local-buckling)
  - [E.3.1 Weighted Average Method](#e31-weighted-average-method)
  - [E.3.2 Direct Strength Method](#e32-direct-strength-method)
- [E.4 INTERACTION BETWEEN MEMBER BUCKLING AND LOCAL BUCKLING](#e4-interaction-between-member-buckling-and-local-buckling)

---

----------|-------|-------------------|
| yielding | $F_{cy}$ | $\lambda \leq \frac{B_c - F_{cy}}{D_c} = \lambda_1$ |
| inelastic buckling | $\left(B_c - D_c \lambda\right)\left(0.85 + 0.15 \frac{C_c - \lambda}{C_c - \lambda_1}\right)$ | $\frac{B_c - F_{cy}}{D_c} < \lambda < C_c$ |
| elastic buckling | $\frac{0.85\pi^2 E}{\lambda^2}$ | $\lambda \geq C_c$ |

$\lambda$ = greatest column slenderness determined from Sections E.2.1 and E.2.2.

For members without welds determine the nominal member buckling strength $P_{nc} = P_{nw}$ using $B_c$, $D_c$, and $C_c$ for unwelded material using Table B.4.1 or B.4.2 and $F_{cy}$.

For members that are fully weld-affected determine the nominal member buckling strength $P_{nc} = P_{nwo}$ using $B_c$, $D_c$, and $C_c$ for welded material using Table B.4.1 and $F_{cyw}$.

For members with transverse welds and:

a) supported at both ends with no transverse weld farther than $0.05L$ from the member ends, $P_{nc} = P_{nw}$

b) supported at both ends with a transverse welds weld farther than $0.05L$ from the member ends or supported at only one end with a transverse weld $P_{nc} = P_{nwo}$.

For members with longitudinal welds, the nominal member buckling strength is:

$$P_{nc} = P_{nw}(1 - A_{wz} / A_g) + P_{nwo} (A_{wz} / A_g)$$ (E.2-2)

### E.2.1 Flexural Buckling

For flexural buckling, $\lambda$ is the largest slenderness $kL/r$ of the column. The effective length factor $k$ for calculating column slenderness $kL/r$ shall be determined using Section C.3.

### E.2.2 Torsional and Flexural-Torsional Buckling

For torsional or flexural-torsional buckling,

$$\lambda = \pi \sqrt{\frac{E}{F_e}}$$ (E.2-3)

where $F_e$ is the elastic buckling stress determined by analysis or as follows:

a) For doubly symmetric members:

$$F_e = \left(\frac{\pi^2 EC_w}{(k_z L_z)^2} + GJ\right) \frac{1}{I_x + I_y}$$ (E.2-4)

b) For singly symmetric members where $y$ is the axis of symmetry:

$$F_e = \left[\frac{F_{ey} + F_{ez}}{2H}\right]\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$ (E.2-5)

c) For unsymmetric members, $F_e$ is the lowest root of the cubic equation:

$(F_e - F_{ex})(F_e - F_{ey})(F_e - F_{ez})$
$- F_{ez}^2(F_e - F_{ex})(x_o / r_o)^2 - F_{ey}^2(F_e - F_{ez})(y_o / r_o)^2 = 0$ (E.2-6)

where

$$r_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_g}$$ (E.2-7)

$$H = 1 - \frac{x_o^2 + y_o^2}{r_o^2}$$ (E.2-8)

$$F_{ex} = \frac{\pi^2 E}{\left(k_x L_x / r_x\right)^2}$$ (E.2-9)

$$F_{ey} = \frac{\pi^2 E}{\left(k_y L_y / r_y\right)^2}$$ (E.2-10)

$$F_{ez} = \frac{1}{A_g r_o^2} \left[GJ + \frac{\pi^2 EC_w}{(k_z L_z)^2}\right]$$ (E.2-11)

- $I_x, I_y$ = moments of inertia about the principal axes
- $x_o, y_o$ = coordinates of the shear center with respect to the centroid
- $r_o$ = polar radius of gyration about the shear center
- $r_x, r_y$ = radii of gyration about the centroidal principal axes

## E.3 LOCAL BUCKLING

For members without welds, the local buckling strength shall be determined in accordance with either Section E.3.1 or E.3.2. For members with welds, the local buckling strength shall be determined in accordance with Section E.3.1.

### E.3.1 Weighted Average Method

The weighted average local buckling strength is

$$P_{nc} = \sum_{i=1}^{n} F_{ci} A_i + F_{cy} \left(A_g - \sum_{i=1}^{n} A_i\right)$$ (E.3-1)

where

- $F_{ci}$ = local buckling stress of element $i$ determined using Sections B.5.4.1 through B.5.4.5.
- $A_i$ = area of element $i$

### E.3.2 Direct Strength Method

As an alternate to Section E.3.1, the local buckling strength of a shape composed of flat elements shall be determined as:

$$P_{nc} = F_c A_g$$ (E.3-2)

where $F_c$ is determined using Section B.5.4.6.

## E.4 INTERACTION BETWEEN MEMBER BUCKLING AND LOCAL BUCKLING

If the elastic local buckling stress $F_e$ is less than the member buckling stress $F_c$, the nominal compressive strength of the member shall not exceed

$$P_{nc} \leq \left[\frac{0.85\pi^2 E}{\lambda^2}\right]^{1/3} F_c^{2/3} A_g$$ (E.4-1)

where $\lambda$ = greatest column slenderness determined from Sections E.2.1 and E.2.2

If the local buckling strength is determined using Section E.3.1, $F_e$ is the smallest elastic local buckling stress for all elements of the cross section determined by Table B.5.1.

If the local buckling strength is determined using Section E.3.2, $F_e$ is the elastic local buckling stress of the cross section determined by analysis.

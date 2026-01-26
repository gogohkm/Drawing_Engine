# Chapter D: Design of Members for Tension

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 51-51
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [D.1 GENERAL PROVISIONS](#d1-general-provisions)
- [D.2 TENSILE STRENGTH](#d2-tensile-strength)
- [D.3 AREA DETERMINATION](#d3-area-determination)
  - [D.3.1 Net Area](#d31-net-area)
  - [D.3.2 Effective Net Area](#d32-effective-net-area)

---

----------|----------|------------|
| tensile rupture | 0.75 | 1.95 |
| tensile yielding | 0.90 | 1.65 |

## D.2 TENSILE STRENGTH

The nominal tensile strength $P_{nt}$ of tension members shall be determined as follows.

a) For tensile yielding in the gross section:

For unwelded members and members with transverse welds

$$P_{nt} = F_{ty} A_g$$ (D.2-1)

For members with longitudinal welds

$$P_{nt} = F_{ty}(A_g - A_{wz}) + F_{tyw} A_{wz}$$ (D.2-2)

b) For tensile rupture in the net section:

For unwelded members

$$P_{nt} = F_{tu} A_n / k_t$$ (D.2-3)

For welded members

$$P_{nt} = F_{tu}(A_n - A_{wz})/k_t + F_{tuw} A_{wz}$$ (D.2-4)

where

- $A_n$ = effective net area defined in Section D.3.2
- $A_{wz}$ = effective net area in the weld-affected zone

Block shear rupture strength for the end connections of tension members is given in Section J.7.3.

## D.3 AREA DETERMINATION

### D.3.1 Net Area

The net area $A_n$ of a member is the sum of the products of the thickness and the least net width of each element computed as follows:

The width of holes shall be taken as the nominal hole diameter for drilled or reamed holes and the nominal hole diameter plus 1/32 in. (0.8 mm) for punched holes.

For a chain of holes extending across a part in any diagonal or zigzag line, the net width of the part shall be obtained by deducting from the gross width the sum of the hole widths of all holes in the chain, and adding, for each gage space in the chain, the quantity $s^2/4g$ where

- $s$ = longitudinal center-to-center spacing (pitch) of any two consecutive holes
- $g$ = transverse center-to-center spacing (gage) between fastener gage lines

For angles, the gage for holes in opposite legs shall be the sum of the gages from the back of the angles less the thickness.

Weld metal in plug or slot welds shall not be included in the net area.

### D.3.2 Effective Net Area

The effective net area $A_e$ for angles, channels, tees, zees, rectangular tubes, and I-shaped sections shall be determined as follows:

a) If tension is transmitted directly to each of the cross-sectional elements of the member by fasteners or welds, the effective net area $A_e$ is the net area.

b) If tension is transmitted by fasteners or welds through some but not all of the cross-sectional elements of the member, the effective net area $A_e$ is:

$$A_e = A_n \left(1 - \frac{\bar{x}}{L_c}\right)\left(1 - \frac{\bar{y}}{L_c}\right)$$ (D.3-1)

where

- $A_n$ = net area of the member at the connection
- $L_c$ = length of the connection in the direction of load, measured from the center of fasteners or the end of welds. If the length of the connection $L_c$ is zero, the effective net area is the net area of the connected elements.
- $\bar{x}$ = eccentricity of the connection in the $x$-axis direction
- $\bar{y}$ = eccentricity of the connection in the $y$-axis direction

The effective net area of the section need not be less than the net area of the connected elements.

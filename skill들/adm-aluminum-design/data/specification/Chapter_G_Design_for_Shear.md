# Chapter G: Design of Members for Shear

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 59-61
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [G.1 GENERAL PROVISIONS](#g1-general-provisions)
- [G.2 MEMBERS WITH FLAT WEBS SUPPORTED ON BOTH EDGES](#g2-members-with-flat-webs-supported-on-both-edges)
- [G.3 MEMBERS WITH FLAT WEBS SUPPORTED ON ONE EDGE](#g3-members-with-flat-webs-supported-on-one-edge)
- [G.4 PIPES AND ROUND OR OVAL TUBES](#g4-pipes-and-round-or-oval-tubes)
- [G.5 RODS](#g5-rods)

---

----------|----------|-----------|
| shear rupture | 0.75 | 1.95 |
| other shear limit states | 0.90 | 1.65 |

For the limit states of shear yielding and shear buckling, the nominal shear strength $V_n$ is

For unwelded members:

$$V_n = F_{sv} A_s$$ (G.1-1)

For welded members:

$$V_n = F_{sv}(A_s - A_{wz}) + F_{svw} A_{wz}$$ (G.1-2)

where

- $F_{sv}$ = shear stress $F_s$ corresponding to the shear strength for an element determined using Section G.2, G.3, or G.4 if no part of the cross section were weld affected. Use buckling constants for unwelded metal (Table B.4.1 or Table B.4.2) and $F_{sy}$.
- $F_{svw}$ = shear stress $F_s$ corresponding to the shear strength for an element determined using Section G.2, G.3, or G.4 if the entire cross section were weld-affected. Use buckling constants for weld-affected zones (Table B.4.1) and $F_{syw}$.
- $A_s$ = shear area as defined in Section G.2, G.3, G.4 or G.5
- $A_{wz}$ = weld-affected portion of the shear area

## G.2 MEMBERS WITH FLAT WEBS SUPPORTED ON BOTH EDGES

The nominal shear strength $V_n$ of flat webs supported on both edges is

For the limit state of shear rupture

For unwelded members

$$V_n = F_{su} A_s / k_t$$ (G.2-1)

For welded members

$$V_n = F_{su}(A_s - A_{wz})/k_t + F_{suw} A_{wz}$$ (G.2-2)

where

- $A_s$ = net area of the web
- $A_{wz}$ = weld-affected area of the web

For the limit states of shear yielding and shear buckling $V_n$ is as defined in Section G.1 with

$$A_s = dt$$ (G.2-3)

and $F_s$ determined from:

| LIMIT STATE | $F_s$ | $b/t$ | Slenderness Limits |
|-------------|-------|-------|--------------------|
| yielding | $F_{sy}$ | $b/t \leq \lambda_1$ | $\lambda_1 = \frac{B_s - F_{sy}}{1.25D_s}$ |
| inelastic buckling | $B_s - 1.25D_s b/t$ | $\lambda_1 < b/t < \lambda_2$ | |
| elastic buckling | $\frac{\pi^2 E}{(1.25b/t)^2}$ | $b/t \geq \lambda_2$ | $\lambda_2 = \frac{C_s}{1.25}$ |

$b$ = clear height of the web (see Figure G.2.1) for webs without transverse stiffeners and

$$b = \sqrt{1 + 0.7\left(\frac{a_1}{a_2}\right)^2}$$ for webs with transverse stiffeners

- $a_1$ = the lesser of the clear height of the web and the distance between stiffeners
- $a_2$ = the greater of the clear height of the web and the distance between stiffeners
- $t$ = web thickness
- $d$ = full depth of the section

![Figure G.2.1 - FLAT WEBS IN SHEAR showing I-beam and angled web cross-sections](description)

**Figure G.2.1**
**FLAT WEBS IN SHEAR**

Transverse stiffeners shall have a moment of inertia $I_s$ not less than the following:

$$\frac{s}{b} \leq 0.4, \quad I_s = \frac{0.55Vb^3}{E}\left(\frac{s}{b}\right)$$ (G.2-4)

$$\frac{s}{b} > 0.4, \quad I_s = \frac{0.088Vb^3}{E}\left(\frac{b}{s}\right)$$ (G.2-5)

where

- $b$ = clear height of the web regardless of whether or not a longitudinal stiffener is present
- $I_s$ = moment of inertia of the transverse stiffener. For a stiffener composed of members of equal size on each side of the web, the moment of inertia of the stiffener shall be computed about the centerline of the web. For a stiffener composed of a member on only one side of the web, the moment of inertia of the stiffener shall be computed about the face of the web in contact with the stiffener
- $s$ = transverse stiffener spacing. For a stiffener composed of a pair of members, one on each side of the web, the stiffener spacing $s$ is the clear distance between the pairs of stiffeners. For a stiffener composed of a member on only one side of the web, the stiffener spacing $s$ is the distance between fastener lines or other connecting lines.
- $V$ = shear force on the web at the transverse stiffener

Stiffeners shall extend from flange to flange but need not be connected to either flange.

## G.3 MEMBERS WITH FLAT WEBS SUPPORTED ON ONE EDGE

The nominal shear strength $V_n$ of flat webs supported on one edge is

For the limit state of shear rupture

For unwelded members

$$V_n = F_{su} A_s / k_t$$ (G.3-1)

For welded members

$$V_n = F_{su}(A_s - A_{wz})/k_t + F_{suw} A_{wz}$$ (G.3-2)

where

- $A_s$ = net area of the web
- $A_{wz}$ = weld-affected area of the web

For the limit states of shear yielding and shear buckling $V_n$ is as defined in Section G.1 with

$$A_s = bt$$ (G.3-3)

and $F_s$ determined from:

| LIMIT STATE | $F_s$ | $b/t$ | Slenderness Limits |
|-------------|-------|-------|--------------------|
| yielding | $F_{sy}$ | $b/t \leq \lambda_1$ | $\lambda_1 = \frac{B_s - F_{sy}}{3.0D_s}$ |
| inelastic buckling | $B_s - 3.0D_s b/t$ | $\lambda_1 < b/t < \lambda_2$ | |
| elastic buckling | $\frac{\pi^2 E}{(3.0b/t)^2}$ | $b/t \geq \lambda_2$ | $\lambda_2 = \frac{C_s}{3.0}$ |

$b$ = distance from the unsupported edge to the mid-thickness of the supporting element
$t$ = web thickness

## G.4 PIPES AND ROUND OR OVAL TUBES

The nominal shear strength $V_n$ of pipes and round or oval tubes is

For the limit state of shear rupture

For unwelded members

$$V_n = F_{su} A_s / (2k_t)$$ (G.4-1)

For welded members

$$V_n = F_{su}(A_s - A_{wz})(2k_t) + F_{suw} A_{wz} / 2$$ (G.4-2)

where

- $A_s$ = net area of the pipe or tube
- $A_{wz}$ = weld-affected area of the pipe or tube

For the limit states of shear yielding and shear buckling $V_n$ is as defined in Section G.1 with

$$A_s = \pi(D_o^2 - D_i^2)/8$$ (G.4-3)

where

- $D_o$ = outside diameter of the pipe or tube
- $D_i$ = inside diameter of the pipe or tube

and $F_s$ determined from:

| LIMIT STATE | $F_s$ | $\lambda$ | Slenderness Limits |
|-------------|-------|-----------|-------------------|
| yielding | $F_{sy}$ | $\lambda \leq \lambda_1$ | $\lambda_1 = \frac{1.3B_s - F_{sy}}{1.63D_s}$ |
| inelastic | $1.3B_s - 1.63D_s \lambda$ | $\lambda_1 < \lambda < \lambda_2$ | |
| elastic buckling | $\frac{1.3\pi^2 E}{(1.25\lambda)^2}$ | $\lambda \geq \lambda_2$ | $\lambda_2 = \frac{C_s}{1.25}$ |

$$\lambda = 2.9 \left(\frac{R_b}{t}\right)^{5/8} \left(\frac{L_v}{R_b}\right)^{1/4}$$ (G.4-4)

- $R_b$ = mid-thickness radius of a pipe or round tube or maximum mid-thickness radius of an oval tube
- $t$ = wall thickness
- $L_v$ = length of pipe or tube from maximum to zero shear force

## G.5 RODS

The nominal shear strength $V_n$ of rods is

For the limit state of shear rupture

For unwelded members

$$V_n = F_{su} A_s / k_t$$ (G.5-1)

For welded members

$$V_n = F_{su}(A_s - A_{wz})/k_t + F_{suw} A_{wz}$$ (G.5-2)

where

- $A_s$ = net area of the rod
- $A_{wz}$ = weld-affected area of the rod

For the limit state of shear yielding, $V_n$ is as defined in Section G.1 with

$$A_s = \pi D^2/4$$ (G.5-3)

where

- $D$ = diameter of the rod
- $F_s = F_{sy}$ (G.5-4)

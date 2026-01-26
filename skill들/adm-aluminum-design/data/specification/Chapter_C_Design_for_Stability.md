# Chapter C: Design for Stability

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 50-50
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [C.1 GENERAL STABILITY REQUIREMENTS](#c1-general-stability-requirements)
- [C.2 CALCULATION OF REQUIRED STRENGTHS](#c2-calculation-of-required-strengths)
- [C.3 CALCULATION OF AVAILABLE STRENGTHS](#c3-calculation-of-available-strengths)

---




<!-- Original pages: 50-50 -->


# Chapter C Design for Stability

This chapter addresses requirements for the analysis and design of structures for stability.

## C.1 GENERAL STABILITY REQUIREMENTS

Stability shall be provided for the structure as a whole and for each of its components. The available strengths of members and connections determined in accordance with Section C.3 shall equal or exceed the required strengths determined in accordance with Section C.2.

## C.2 CALCULATION OF REQUIRED STRENGTHS

The required strengths of members and connections of the structure shall be determined from an elastic analysis that considers the effects of each of the following:

a) Flexural, shear, and axial deformations, including all member and connection deformations that contribute to displacements of the structure.

b) Second-order effects including $P$-$\Delta$ effects (the effect of loads acting on the displaced location of joints or nodes in a structure) and $P$-$\delta$ effects (the effect of loads acting on the deflected shape of a member between joints or nodes);

c) Geometric imperfections. The effect of geometric imperfections on the stability of the structure shall be accounted for by analyzing the structure with the members' points of intersection displaced from their nominal locations by the tolerances specified in the contract documents. The displacements shall be placed to cause the greatest destabilizing effect.

d) Member stiffness reduction due to inelasticity. The effect of member stiffness reduction due to inelasticity on the stability of the structure shall be accounted for by using a reduced stiffness as follows:

A factor $\tau_b$ shall be applied to the flexural stiffnesses of all members whose flexural stiffnesses contribute to the stability of the structure, where

- $\tau_b = 1.0$ for $\alpha P_r / P_y \leq 0.5$
- $\tau_b = 4(\alpha P_r / P_y)(1 - \alpha P_r / P_y)$ for $\alpha P_r / P_y > 0.5$
- $P_r$ = required axial compressive strength using LRFD or ASD load combinations
- $P_y$ = axial yield strength
- $\alpha = 1.0$ (LRFD); $\alpha = 1.6$ (ASD)

e) Uncertainty in stiffness and strength shall be addressed by applying a factor of 0.8 to all axial, shear, and flexural stiffnesses in the structure.

## C.3 CALCULATION OF AVAILABLE STRENGTHS

The available strengths of members and connections shall be determined in accordance with the provisions of Chapters D, E, F, G, H, and J. The effective length factor $k$ of all members that provide stability of the structure as a whole or of any of its components shall be taken as 1. The effective length factor $k$ of other members shall be taken as 1 unless a smaller value is justified by rational analysis.

Bracing intended to define the unbraced length of members shall have adequate stiffness and strength to control member movement at the brace points.

The analysis shall include all loads that affect the stability of the structure as a whole or of any of its components, including loads on members that do not provide stability. Analysis shall be conducted for either:

a) The LRFD load combinations with the results used directly to obtain the required strengths, or

b) Using the ASD load combinations with the results divided by 1.6 to obtain the required strengths.

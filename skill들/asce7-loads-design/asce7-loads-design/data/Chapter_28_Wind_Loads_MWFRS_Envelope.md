# Chapter 28: Wind Loads MWFRS Envelope

**ASCE 7-22 Minimum Design Loads and Associated Criteria for Buildings and Other Structures**

---

*This chapter combines pages 355-360 from ASCE 7-22*

---

**28.1.1 Building Types** This chapter applies to the determination of wind loads on buildings using the MWFRS wind loads. Buildings not meeting the requirements of Section 28.1.2 shall use Chapter 27.

**28.1.2 Conditions** The design wind loads determined in accordance with this chapter shall be used only for buildings complying with all the following conditions:

1. Building is a regular-shaped building as defined in Section 26.2.

2. Building does not have response characteristics making it subject to across-wind loading, vortex shedding, galloping, or flutter, or does not have a site location for which channeling effects or buffeting in the wake of upwind obstructions warrant special consideration (see Appendix C of ASCE 7).

3. Building has an approximate fundamental natural frequency greater than or equal to 1 Hz.

**28.1.3 Limitation** Torsional wind load cases shall be considered separately from lateral wind loads caused by winds acting perpendicular to each face of the building as shown in Table 28.3-1. This shall not be used when the Torsional Wind Load Procedure specified in Chapter 27.

**28.1.4 Shielding** There shall be no reductions in velocity pressures for the effects of apparent shielding afforded by buildings and other structures or by topographic features (see Appendix C of ASCE 7).

**28.1.5 Air-Permeable Cladding** For buildings with air-permeable cladding, pressures shall act on all air-impermeable surfaces, including the structural frame. Where air-permeable cladding is used, the net wind force shall be the sum of the forces on all surfaces.

### 28.2 GENERAL REQUIREMENTS

The design pressure for the determination of MWFRS wind loads for low-rise buildings are shown in Table 28.3-1.

---

**Table 28.3-1. Steps to Determine Wind Loads on MWFRS (Envelope Procedure)**

**Relevant Sections**

Step 1: Determine risk category of building; see Table 1.5-1

- Category; see Figure 26.5-1.

Step 2: Determine the basic wind speed, $V$, for applicable risk category; see Section 26.5-1.

Step 3: Determine wind load parameters:

- Wind directionality factor, $K_d$; or Exposure (B, C, or D); see Section 26.7.
- Topographic factor, $K_{zt}$; see Section 26.8 and Figure 26.8-1.
- Ground elevation factor, $K_e$; see Section 26.9 and Table 26.9-1.

Step 4: Determine velocity exposure coefficient, $K_z$ or $K_h$; Section 26.10.

Step 5: Determine the internal pressure coefficient, $(GC_{pi})$; see Section 26.13.

Step 6: Determine external pressure coefficients, $(GC_{pf})$; see Section 28.3 and Figures 28.3-1 through 28.3-6.

Step 7: Calculate wind pressure, $p$, from Equation (28.3-1).

Step 8: Determine velocity exposure coefficient, $K_z$ or $K_h$; see Section 26.10 and Table 26.10-1 for guidance on applying $(GC_{pf})$ and $(GC_{pi})$ to calculate the wind load.

Step 9: Take into account load combinations using Section 2.3.2 for guidance on use of $K_d$ for flat and gable roofs.

Step 10: Take into account Commentary Figure C28.3-2 for guidance on hip roofs.

**28.2.1 Wind Load Parameters Specified in Chapter 28** The following wind load parameters shall be determined in accordance with the provisions of this chapter:

- External pressure coefficients, $(GC_{pf})$; (Section 28.3).

**28.2.2 Wind Load Parameters Specified in Chapter 26** The following wind load parameters shall be determined in accordance with the provisions of Chapter 26:

- Wind directionality factor, $K_d$; (Section 26.6).
- Exposure category, (B, C, or D); (Section 26.7).
- Topographic factor, $K_{zt}$; (Section 26.8).
- Ground elevation factor, $K_e$; (Section 26.9).
- Velocity pressure exposure coefficient, $K_z$ or $K_h$; (Section 26.10).
- Enclosure classification, (Section 26.12).
- Internal pressure coefficient, $(GC_{pi})$; (Section 26.13).

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 293

---

**28.3.1 Design Wind Pressure for Low-Rise Buildings** Design wind pressure for the MWFRS of low-rise buildings shall be determined by the following equation:

$$p = q_h\left[(GC_{pf}) - (GC_{pi})\right] \tag{28.3-1}$$

where

$q_h$ = Velocity pressure evaluated at mean roof height $h$ using the exposure as defined in Section 26.7.3 that results in the highest wind loads for any wind direction at the site.

$(GC_{pf})$ = External pressure coefficient from Section 28.3.2, 28.3.3, or 28.3.4 as applicable. For buildings sited in wind-borne debris regions as defined in Section 26.12, an external pressure coefficient $(GC_{pf})$ for partially enclosed buildings shall be used for design.

$(GC_{pi})$ = Internal pressure coefficient from Section 26.13.

The design wind pressure $p$ shall be determined independently for each building surface as shown in Table 28.3-1. Each building surface shall be subjected to both positive (pressure) and negative (suction) design wind pressures as determined by Equation (28.3-1).

**28.3.2 External Pressure Coefficients** For the purpose of evaluating wind loading on the MWFRS, external pressure coefficients are given in Figures 28.3-1 through 28.3-6 for the basic load cases and the increased load cases, acting separately in accordance with Section 28.3.4. Appropriate roof and wall external pressure coefficient values shall be used. Combinations of external and internal pressure coefficients (see Tables 26.13-1 and 26.13-2) shall be evaluated as required to determine the most critical load case.

**EXCEPTION:** Alternatively, $C_p$ as specified in Chapter 27 may be used with $q_h$ and $G$ as specified in Section 26.11 for both Zone 2/3 and Zone 3/4B. For domed roofs located at the mid-width of the windward half of the building and all roofs sloped less than 7 degrees, the values of wind pressure shall be determined by calculating the external pressure coefficients $C_p$ from Table 27.3-1, then applying Case 1 or Case 2 pressure coefficients from Figure 28.3-1. For enclosures with sidewall corners not located at the mid-width of the windward half of the building, whichever is less, the remainder of Zone 2/3B extending to the ridge line exceeds half the least horizontal dimension or for Zone 3/4B, whichever is less, or at a distance from the windward edge of $0.5h$ but not less than 3.5h shall be used.

**28.3.3 Total Horizontal Load** The total horizontal shear shall exceed 0.8 times the horizontal wind force that would be based on using the minimum wind forces for the MWFRS.

**28.3.4 Torsional Load Cases** The total design pressure for the effect of eccentric wind loads on a rectangular building shall be determined by the following equation:

$$p_e = q_h K_z(GC_{pf})\left[N/m^2\right] \tag{28.3-2}$$

$$p_e = q_h K_z(GC_{pf})\left[psf\right] \tag{28.3-2S)}$$

where

$p_e$ = Combined net pressure on the parapet caused by the combination of the net pressures from the front and leeward surfaces of the parapet arising from the design net pressure acting toward and away from the front surfaces of windward and leeward parapets as defined in Figure 28.3-1 through 28.3-6 shall be from the top and bottom surfaces.

$(GC_{pf})$ = Combined net pressure coefficient = +1.5 for windward parapet.

For vertical surfaces of flat roofs and inclined-surface parapets on the leeward surface of windward roof overhangs shall be determined as positive pressure on the windward face and negative on the building roof.

For pressures on leeward walls, velocity pressure $q_h$ shall be determined for MWFRS as described in Section 26.10 the calculated design wind pressure shall take effect on the design of the MWFRS for as specified at partially enclosed buildings. On floors with rigid diaphragms in combination with the roof and other floor slabs, $M_t$ of the design load pattern of the walls and vertical plane normal to the assumed wind direction described in Figure 28.3-1 or using other rational methods.

**28.3.5 Horizontal Pressure at Longitudinal Direction Parapets** A horizontal pressure on the longitudinal direction parapets in the edge roof areas in combination with the roof wind pressures shall be applied for longitudinal wind pressure.

**28.3.6 Partial Loading** Wind pressures shall be applied for partial loading with cases that would have forces on all roofs being loaded simultaneously.

For the MWFRS, it is permitted to use the loads which vary (see Appendix D) when the walls shall not receive resultant forces using the exposure defined in Section 26.7.

**28.3.7 Minimum Design Wind Loading** Wind loading used for design of the MWFRS shall not be less than that determined from the following equation:

$$p_{\min} = 0.77 K_z K_{zt} K_d\left[(GC_{pf}) - (GC_{pi})\right]p_{h30}\left[kN\right] \tag{28.3-3}$$

or

$$p_{\min} = 16.0 K_z K_{zt} K_d\left[(GC_{pf}) - (GC_{pi})\right]p_{h30}\left[psf\right] \tag{28.3-3S)}$$

where

$p_{h30}$ = Velocity pressure calculated at mean roof height using the exposure as defined in Section 26.7.3.

---

**294** STANDARD ASCE/SEI 7-22

---

```
         ④    LEE WALL              ④         LEE WALL    ⑥
    ④③ ─────────────                ④③ ─────────────       ╱╱╱
        ③          ②                    ③          ②
    ④E    ③E    ②                   ④E    ③E    ②
        ①E      ①                       ①E      ①         ⑥
            ①                               ①
    ─────2a─────                    ─────2a─────
         WINDWARD                        WINDWARD
                 ↑  ↑                             ↑  ↑
              WIND DIRECTION              WIND DIRECTION
          NORMAL OR                   NORMAL OR
      PARALLEL TO RIDGE           PARALLEL TO RIDGE

           Load Case 1                    Load Case 2
```

### Notation

$a$ = 10% of least horizontal dimension or 0.4 $h$, whichever is smaller, but not less than either 4% of least horizontal dimension or 3 ft (0.9 m).

**EXCEPTION:** For buildings with $\theta = 0$ to 7° and a least horizontal dimension greater than 300 ft (90 m), dimension $a$ shall be limited to a maximum of 0.8 $h$.

$h$ = Mean roof height, ft (m), except that eave height shall be used for $\theta \leq 10°$.

$\theta$ = Angle of plane of roof from horizontal, in degrees.

### Load Case 1

| Roof Angle θ (degrees) | **Building Surface** | | | | | | | |
|------------------------|----------------------|---|---|---|---|---|---|---|
| | **1** | **2** | **3** | **4** | **1E** | **2E** | **3E** | **4E** |
| 0-5 | 0.40 | -0.69 | -0.37 | -0.29 | 0.61 | -1.07 | -0.53 | -0.43 |
| 20 | 0.53 | -0.69 | -0.48 | -0.43 | 0.80 | -1.07 | -0.69 | -0.64 |
| 30-45 | 0.56 | 0.21 | -0.43 | -0.37 | 0.69 | 0.27 | -0.53 | -0.48 |
| 90 | 0.56 | 0.56 | -0.37 | -0.37 | 0.69 | 0.69 | -0.48 | -0.48 |

### Load Case 2

| Roof Angle θ (degrees) | **Building Surface** | | | | | | | | | |
|------------------------|----------------------|---|---|---|---|---|---|---|---|---|
| | **1** | **2** | **3** | **4** | **5** | **6** | **1E** | **2E** | **3E** | **4E** | **5E** | **6E** |
| 0-90 | -0.45 | -0.69 | -0.37 | -0.45 | 0.40 | -0.29 | -0.48 | -1.07 | -0.53 | -0.48 | 0.61 | -0.43 |

### Notes

1. Plus and minus signs signify pressures acting toward and away from the surfaces, respectively.
2. For values of $\theta$ other than those shown, linear interpolation is permitted.

---

**Figure 28.3-1. Basic load cases for main wind force resisting system [$h \leq$ 60 ft ($h \leq$ 18.3 m)]: external pressure coefficients, $(GC_{pf})$, for enclosed, partially enclosed, and partially open buildings—low-rise walls and roofs.**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 295

---

```
Load Case 3:
    6T
   ┌─────────────┐
  4T│ 3T          │
   │┌────┐       │      6
  4E││ 2T │ 2T    │    ┌─────────────┐
   ││    │       │   6T│             │8E
  4E│└────┘  1T   │    │  3      2   │
   │  2E          │   4E│          ushed│
   │      1E  1   │    │  1  5T      │
   └──────1E──────┘   5T└─────2E──────┘1E
    └─────B─────┘      └─────B─────┘
       WINDWARD             WINDWARD
    ↑↑↑↑↑↑↑↑↑           ↑↑↑↑↑↑↑↑↑
 WIND DIRECTION      WIND DIRECTION
    Load Case 3          Load Case 4
```

### Notation

$a = 10\%$ of least horizontal dimension or $0.4\ h$, whichever is smaller, but not less than either 4% of least horizontal dimension or 3ft (0.9 m).

EXCEPTION: For buildings with $B \leq 7$ ft² and a least horizontal dimension greater than 300 ft (90 m), dimension $a$ shall be limited to a maximum of $0.8\ h$.

$h =$ Mean roof height, in feet (meters), except that eave height shall be used for $\theta \leq 10°$.

$\theta =$ Angle of plane of roof from horizontal, in degrees.

### Load Case 3

| Roof Angle θ (degrees) | Building Surface |        |        |        |
|------------------------|------------------|--------|--------|--------|
|                        | 1T               | 2T     | 3T     | 4T     |
| 0–5                    | 0.10             | −0.17  | −0.09  | −0.07  |
| 20                     | 0.13             | −0.17  | −0.12  | −0.11  |
| 30–45                  | 0.14             | 0.05   | −0.11  | −0.09  |
| 90                     | 0.14             | 0.14   | −0.09  | −0.09  |

### Load Case 4

|                        | Building Surface |        |
|------------------------|------------------|--------|
| Roof Angle θ (degrees) | 5T               | 6T     |
| 0–90                   | 0.10             | −0.07  |

### Notes

1. Plus and minus signs signify pressures acting toward and away from the surfaces, respectively.
2. For values of θ other than those shown, linear interpolation is permitted.

---

**Figure 28.3-2. Torsional load cases for main wind force resisting system [$h \leq 60$ ft ($h \leq 18.3$ m)]: external pressure coefficients, $(GC_{pf})$, for enclosed, partially enclosed, and partially open buildings—low-rise walls and roofs.**

---

**296** **STANDARD ASCE/SEI 7-22**

---

```
      ┌────────────────────────────┐
      │    ╱╲    ╱╲    ╱╲          │
      │   ╱  ╲  ╱  ╲  ╱  ╲         │
      │  ╱    ╲╱    ╱    ╲         │
      │ │      │    │     │         │
      │ │      │    │     │         │
      │ │      │    │     │         │
┌─────┴─┴──────┴────┴─────┴─────────┘
│
│  n×s       n×s
│ ←──→      ←──→
│  ↓╲      ↓╲
│   ╲As   ╲As
│    ╲    ╲
└──────────────────
 WIND DIRECTION
       ↑↑↑
```

### Notation

$B =$ Width of the building perpendicular to the ridge, ft (m)

$A_s =$ Effective solid area of the end wall (i.e., the projected area of any portion of the end wall that would be exposed to the wind)

$A_g =$ Total end wall area for an equivalent enclosed building

$n =$ Number of frames, but shall not be taken as less than 3, even for 2-frame building.

---

**Figure 28.3-3. Horizontal wind loads on open or partially enclosed buildings with transverse frames and pitched roofs: definitions of geometric terminology.**

---

$K_d =$ Wind directionality factor, see Section 26.6;

$(GC_{pf}) =$ External pressure coefficient given in Figure 28.3-1 for Load Case 2, where building surfaces 5 and 5E shall be used to compute the average windward wall pressure and building surfaces 6 and 6E shall be used to compute the average leeward wall pressure;

$K_{at} =$ Frame width factor = $1.8-0.01B$, $B < 100$ ft $(B < 30.5$ m); or $0.8$, $B \geq 100$ ft $(B \geq 30.5$ m);

$K_s =$ Shielding factor = $0.8(1 - 0.5n/(n + 0.7B/3)) + (1.25 q_f^{0.5})$;

$p =$ Design wind pressure, lb/ft²;

$B =$ Width of the building perpendicular to the ridge, ft (m);

$n =$ Number of frames, but shall not be taken as less than 3, even for small 2-frame building.

$A_S =$ Effective solid area of the end wall, that is, the projected area of any portion of the end wall that would be exposed to the wind (Figure 28.3-3); and

$A_E =$ Total end wall area for an equivalent enclosed building (Figure 28.3-3).

The total longitudinal force $F$ to be resisted by the MWFRS shall be determined by Equation (28.3-4):

$$F = pA_E \tag{28.3-4}$$

Equation (28.3-3) is applicable to buildings with open end walls and with end walls fully or partially enclosed with cladding. For the latter, the area that is equivalent to the end wall fully enclosed. The longitudinal force, $F$, given by Equation (28.3-4) represents the total force for which the MWFRS longitudinal bracing shall be designed. The distribution to each frame need not be based on the force of $F$ applied at the centroid of the end wall area $A_E$.

Fascia load areas not be considered separately if fascia areas are included in the $A_S$ calculation.

## 28.4 CONSENSUS STANDARDS AND OTHER REFERENCED DOCUMENTS

No consensus standards and other documents that shall be considered part of this standard are referenced in this chapter.

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **297**

---

# Page 360

This page intentionally left blank

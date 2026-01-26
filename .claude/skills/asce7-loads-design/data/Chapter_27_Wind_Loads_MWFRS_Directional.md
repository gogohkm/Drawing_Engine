# Chapter 27: Wind Loads MWFRS Directional

**ASCE 7-22 Minimum Design Loads and Associated Criteria for Buildings and Other Structures**

---

*This chapter combines pages 343-354 from ASCE 7-22*

---

**27.1.1 Building Types.** This chapter applies to the determination of Main Wind Force Resisting System (MWFRS) wind loads on buildings by using the Directional Procedure. For buildings with unusual or irregular plan configurations (e.g., those with tapered, set-back, or asymmetrically placed setbacks), more-detailed procedures may be necessary to separate applied wind loads onto the windward, leeward, and sidewall surfaces.

**27.1.2 Conditions.** Buildings whose design wind loads are to be determined in accordance with this chapter shall comply with all the following conditions:

1. The building must be a regular-shaped building as defined in Section 26.2; and
2. The building does not have response characteristics making it subject to across-wind loading, vortex shedding, instability caused by galloping or flutter, or does not have a site location for which channeling effects or buffeting in the wake of upwind obstructions warrant special consideration (Chapter 31).

**27.1.3 Limitations.** The provisions of this chapter take into consideration all of the following building parameters:

1. The building is a regular-shaped building as defined in Section 26.2; and
2. The building does not have response characteristics making it subject to across-wind loading, vortex shedding, instability caused by galloping or flutter, and does not have a site location for which channeling effects or buffeting in the wake of upwind obstructions warrant special consideration.

**27.1.4 Shielding.** There shall be no reductions in velocity pressures caused by apparent shielding afforded by buildings and other structures or terrain features.

### 27.2 GENERAL REQUIREMENTS

User Note: Use Chapter 27 to determine wind pressures on the MWFRS of buildings by using the Directional Procedure. Wind pressures determined using Chapter 27 shall be used in combination with loads from other chapters of this standard. See Chapters 26.2 and 29.1 for definitions and procedures required for determining wind pressures on building components and cladding, respectively. See Section 26.1.3 for guidance on the flat-roof uses, provisions, and building structures.

These provisions are the traditional "all heights" provisions for the determination of wind loads by using the Directional Procedure as specified in Section 26.2, with pressures as specified in this chapter.

**27.2.1 Wind Load Parameters Specified in Chapter 26.** The following wind load parameters shall be determined in accordance with Chapter 26:

- Basic wind speed, $V$ (Section 26.5);
- Wind directionality factor, $K_d$ (Section 26.6);
- Exposure category (Section 26.7);
- Topographic factor, $K_{zt}$ (Section 26.8);
- Ground elevation factor, $K_e$ (Section 26.9);
- Velocity pressure, $q$ or $q_h$ (Section 26.10);
- Gust effect factor, $G$ or $G_f$ (Section 26.11); and
- Enclosure classification (Section 26.12); and
- Internal pressure coefficient, $(GC_{pi})$ (Section 26.13).

### 27.3 DESIGN WIND LOADS: MAIN WIND FORCE RESISTING SYSTEM

**27.3.1 Rigid Buildings, Enclosed, and Partially Open Buildings.** The wind pressures for the MWFRS of buildings of all heights, or buildings of any height with all wind loads applied on the MWFRS for a rigid building, shall be determined by the following equations:

$$p = q G C_p - q_i(GC_{pi})$$ (27.3-1)

where

- $p$ = Design wind pressure to be used in determination of wind loads for MWFRS.
- $q, q_i$ = Velocity pressure calculated at respective height.
- $G$ = Gust-effect factor from Section 26.11.
- $C_p$ = External pressure coefficient from Sections 26.11 through 26.13.
- $(GC_{pi})$ = Internal pressure coefficient from Section 26.13.

**27.3.2 Wind Loads:**  Buildings shall be designed for the MWFRS Loads using external wall pressures, $C_p$, or $C_N$, as indicated elsewhere in Section 27.3. The wind pressures determined in accordance with Section 27.3.1 shall be multiplied by the following:

Step 6: Determine wind pressures acting on each building surface using Figures 27.3-1 to 27.3-7;

Step 7: Apply the provisions of Section 26.2;

Step 8: Determine base load cases, external wall pressures, roof pressures;

Step 9: For standard wind loads on wall pressure, $C_p$ or $q_h$;

Step 10: Combine wall and roof loads shall be applied perpendicular to the building surface.

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures 281**

---

**Step 1:** Determine risk category of building or Table 1.5-1.

**Step 2:** Determine the basic wind speed, $V$, for the applicable risk category; see Figure 26.5-1.

**Step 3:** Determine wind load parameters:
- Wind directionality factor, $K_d$; see Section 26.6 and Table 26.6-1.
- Exposure category B, C, or D; see Section 26.7.
- Topographic factor, $K_{zt}$; see Section 26.8 and Figure 26.8-1.
- Ground elevation factor, $K_e$; see Section 26.9 and Table 26.9-1.
- Gust effect factor, $G$ or $G_f$; see Section 26.11.
- Enclosure classification; see Section 26.12.
- Internal pressure coefficient, $(GC_{pi})$; see Section 26.13 and Table 26.13-1.

**Step 4:** Determine velocity pressure exposure coefficient, $K_z$ or $K_h$; see Table 26.10-1.

**Step 5:** Calculate velocity pressure, $q_z$ and $q_h$ (or Equation 26.10-1):

$$q_z = 0.00256 K_z K_{zt} K_d K_e V^2$$ (Eq. 26.10-1)

$$q_h = 0.00256 K_h K_{zt} K_d K_e V^2$$ (Eq. 26.10-1)

**Step 6:** Calculate wind pressure, $p$, from Equations (26.3-1):

$$p = q G C_p - q_i (GC_{pi})$$ (Eq. 27.3-1)

**Step 7:** Determine external pressure coefficients, $C_p$:
- Figure 27.3-1 for walls.
- Figures 27.3-1 for gable roofs; see Figure 30.5-1.
- Figures 27.3-2 for arched roofs; see Figure 30.5-2.
- Figures 27.3-3 for monoslope roofs; see Figure 30.5-3.
- Figures 27.3-4 through 27.3-7 for pitched roofs; see Figures 30.5-4 through 30.5-7.
- Figure 27.3-8 for troughed roof; open building; and
- Special case loads, see Figure 27.3-8.

**Step 8:** Calculate wind loads on each building surface per Step 6 of the applicable figure from Step 7.

**Step 9:** Apply loads as shown in Figure 27.3-8.

**Notes:** Walls; see Figure 30.5-1.

---

**282 STANDARD ASCE/SEI 7-22**

---

```
FLAT, GABLE, HIP ROOF

              WIND ⟹                      WIND ⟹                    WIND ⟹
      qzGCp                       qzGCp    Speed-up        qzGCp         qhGCp
    ┌─────────┐                 ┌─────────┐                 ┌────/│\────┐
qhGCp│         │qhGCp       qhGCp│         │qhGCp       qhGCp│   / │ \   │qhGCp
    │         │                 │         │                 │  /  h  \  │
    │    h    │                 │    h    │                 │ /       \ │
    │         │                 │         │                 │/         \│
qhGCp└─────────┘qhGCp       qhGCp└─────────┘qhGCp       qhGCp└───────────┘qhGCp
         L                           L                           L
       PLAN                      ELEVATION                   ELEVATION
                           Flat roof or wind parallel
                           to ridge on sloped roofs

MONOSLOPE ROOF

              WIND ⟹                                            WIND ⟹
      qzGCp         qhGCp                             qzGCp         qhGCp
    ┌────────/                               ┌────────/            /────┐
qhGCp│       /     │qhGCp                qhGCp│       /            /     │qhGCp
    │      /      │                         │      /            /      │
    │     /   h   │                         │     /        h   /       │
    │    /        │                         │    /            /        │
qhGCp└───/─────────┘qhGCp               qhGCp└───/────────────/─────────┘qhGCp
         L                                        L
       PLAN                                   ELEVATION                ELEVATION
                                         (Windward Roof Pressure)  (Leeward Roof Pressure)

MANSARD ROOF (NOTE 5)

              WIND ⟹                                            WIND ⟹
      qzGCp                                           qzGCp
    ┌────────────────┐                         ┌────────────────┐
qhGCp│   qzGCp  qhGCp│qhGCp                qhGCp│   qzGCp        │qhGCp
    │               │                         │               │
    │       h       │                         │       h       │
    │               │                         │               │
qhGCp└───────────────┘qhGCp               qhGCp└───────────────┘qhGCp
         L                                        L
       PLAN                                   ELEVATION
```

### Notation

- $B$ = Horizontal dimension of building, ft (m), measured normal to wind direction.
- $L$ = Horizontal dimension of building, ft (m), measured parallel to wind direction.
- $h$ = Mean roof height, ft (m), except that eave height shall be used for $\theta \leq 10$ degrees.
- $z$ = Height above ground, ft (m).
- $\theta$ = Angle of plane of roof from horizontal, degrees.
- $G$ = Gust-effect factor.
- $q_z$, $q_h$, $q_i$ = Velocity pressure, lb/ft² (N/m²), evaluated at respective height.
- $\theta$ = Angle of plane of roof from horizontal, degrees.
- $C_p$ = External pressure coefficient.
- $GC_{pi}$ = Combined net pressure coefficient for a parapet.

**Figure 27.3-1. Main wind force resisting system: external pressure coefficients, $C_p$, for enclosed, partially enclosed, and partially open buildings—walls and roofs.**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures 283**

---

| Surface | $L/B$ | $C_p$ | Use with |
|---------|-------|-------|----------|
| Windward wall | All values | 0.8 | $q_z$ |
| Leeward wall | 0-1 | -0.5 | $q_h$ |
|  | 2 | -0.3 | $q_h$ |
|  | ≥4 | -0.2 | $q_h$ |
| Sidewall | All values | -0.7 | $q_h$ |
| Parapet | All values | See Section 27.3.4 for $GC_{pn}$ | $q_p$ |

## Roof Pressure Coefficients, $C_p$, for use with $q_h$

### Windward Section

| Wind Direction | $h/L$ | **Angle, θ** | | | | | | | |
|----------------|-------|--------------|---|---|---|---|---|---|---|
|  | | 10° | 15° | 20° | 25° | 30° | 35° | 45° | 60° |
| Normal to Ridge for $θ \geq 10°$ | ≤0.25 | -0.7 | -0.5 | -0.3 | -0.2 | -0.2 | 0.0^a^ | | |
|  | | -0.18 | 0.0^a^ | 0.2 | 0.3 | 0.3 | 0.4 | 0.4 | 0.6 |
|  | 0.5 | -0.9 | -0.7 | -0.4 | -0.3 | -0.2 | -0.2 | 0.0^a^ | |
|  | | -0.18 | -0.18 | 0.0^a^ | 0.2 | 0.2 | 0.3 | 0.4 | 0.6 |
|  | ≥1.0 | -1.3^b^ | -1.0 | -0.7 | -0.5 | -0.3 | -0.2 | 0.0^a^ | |
|  | | -0.18 | -0.18 | -0.18 | 0.0^a^ | 0.2 | 0.2 | 0.3 | 0.6 |

### Leeward Section

| Wind Direction | $h/L$ | **Angle, θ** | | | | |
|----------------|-------|--------------|---|---|---|---|
|  | | $60° < θ \leq 80°$ | > 80 | 10° | 15° | ≥ 20° |
| Normal to Ridge for $θ \geq 10°$ | ≤0.25 | | | 0.01 θ | 0.8 | -0.3 | -0.5 | -0.6 |
|  | 0.5 | | | 0.01 θ | 0.8 | -0.5 | -0.5 | -0.6 |
|  | ≥1.0 | | | 0.01 θ | 0.8 | -0.7 | -0.6 | -0.6 |

### Horizontal Distance from Windward Edge

| Wind Direction | $h/L$ | Horizontal Distance from Windward Edge | $C_p$ |
|----------------|-------|----------------------------------------|-------|
| Normal to Ridge Parallel to Ridge, and Parallel to Ridge for all θ | ≤0.5 | $0$ to $h/2$ | $-0.9, -0.18$ |
|  | | $h/2$ to $h$ | $-0.9, -0.18$ |
|  | | $h$ to $2h$ | $-0.5, -0.18$ |
|  | | $> 2h$ | $-0.3, -0.18$ |
|  | ≥1.0 | $0$ to $h/2$ | $-1.3^b, -0.18$ |
|  | | $> h/2$ | $-0.7, -0.18$ |

^a^Value is provided for interpolation purposes.

^b^Value can be reduced linearly, with area over which it is applicable as follows:

| Area, ft² (m²) | Reduction Factor |
|----------------|------------------|
| ≤100 (9.3) | 1.0 |
| 250 (23.2) | 0.9 |
| ≥1,000 (92.9) | 0.8 |

### Notes:

1. Plus and minus signs signify pressures acting toward and away from the surfaces, respectively.

2. Linear interpolation is permitted for values of $L/B$, $h/L$, and θ, other than shown. Interpolation shall only be carried out between values of the same sign. Where no value of the same sign is given, assume 0.0 for interpolation purposes.

3. Where two values of $C_p$ are listed, this indicates that the windward roof slope is subjected to either positive or negative pressures and the roof structure shall be designed for both conditions. Interpolation for intermediate ratios of $h/L$ shall only be carried out between $C_p$ values of like sign.

4. Parapets are shown only on the flat roof elevation but may occur on any roof type shown.

5. For mansard roofs, the top horizontal surface and leeward inclined surface shall be treated as leeward surfaces according to the table.

6. Except for MWFRS at the roof consisting of moment-resisting frames, the total horizontal shear shall not be less than that determined by neglecting wind forces on roof surfaces.

---

**Figure 27.3-1** *(Continued)*. **Main wind force resisting system: external pressure coefficients, $C_p$, for enclosed, partially enclosed, and partially open buildings—walls and roofs.**

---

**284** STANDARD ASCE/SEI 7-22

---

```
        Wind      B                    B
         →    A  θ     C    f      Wind  A    B    C
              └─────────┘   ↑            ╱───────╲
                           hD            │   B   │
                            ↓            ╲───────╱
              ←─────D──────→                B

              ELEVATION              PLAN
```

**Graph: External Pressure Coefficient $C_p$ vs Ratio of Rise to Diameter, f/D**

```
  +0.8                      A (hD /D = 0.25)
  +0.6        A (hD /D = 0)
  +0.4                                    A (hD /D ≥ 1.0)
  +0.2
   0.0  ──────────────────────────────── C (hD /D = 0)
  -0.2
  -0.4                                    C (hD /D ≥ 0.5)
  -0.6
  -0.8
  -1.0
  -1.2                                    B (hD /D = 0)
  -1.4
  -1.6                                    B (hD /D ≥ 0.5)
  -1.8
   0    0.1   0.2   0.3   0.4   0.5
        Ratio of Rise to Diameter, f/D
```

### Notation

- $f$ = Dome rise, ft (m)
- $h_D$ = Height to base of dome, ft (m)
- $D$ = Diameter, ft (m)
- $\theta$ = Angle of plane of roof from horizontal, degrees

### Notes

1. Two load cases shall be considered:

   Case A: $C_p$ values between $A$ and $B$ and between $B$ and $C$ shall be determined by linear interpolation along arcs on the dome parallel to the wind direction;

   Case B: $C_p$ shall be the constant value of $A$ for $\theta \leq 25°$ and shall be determined by linear interpolation from 25 degrees to $B$ and from $B$ to $C$.

2. Values denote $C_p$ to be used with $q_{(h_{top})}$, where $h_{top}$ is the height at the top of the dome.

3. Plus and minus signs signify pressures acting toward and away from the surfaces, respectively.

4. $C_p$ is constant on the dome surface for arcs of circles perpendicular to the wind direction; for example, the arc passing through $B-B-B$ and all arcs parallel to $B-B-B$.

5. For values of $h_D/D$ between those listed on the graph curves, linear interpolation shall be permitted.

6. $\theta = 0$ degrees on dome springline; $\theta = 90$ degrees at dome center point, $f$ is measured from springline to top.

7. The total horizontal shear shall not be less than that determined by neglecting wind forces on roof surfaces.

8. For $f/D$ values less than 0.05, use Figure 27.3-1.

---

**Figure 27.3-2. Main wind force resisting system: external pressure coefficients, $C_p$, for enclosed, partially enclosed, and partially open buildings and structures—domed roofs with a circular base.**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 285

---

| Conditions | Rise-to-Span Ratio, $f/L$ |  | | |
|------------|---------------------------|---|---|---|
| | $0 < f/L \leq 0.05$ | $0.2 \leq f/L \leq 0.3$ | $f/L > 0.6$ | |
| | | Windward | Center Half | Leeward |
| | | $-0.9$ | $-0.7, -r$ | $-0.5$ |
| | | $-0.5$ | $-0.3$ | $-0.3$ |
| Roof springing from ground level (no sidewalls) | $0.3 < f/L < 0.6$ | $2.75, -0.7$ | $-0.7, -r$ | $-0.5$ |
|  | | $1, -r$ | $-0.7$ | $-0.5$ |

**Notes:**

1. Values based on the determination of average loads on main wind force resisting systems.
2. Linear interpolation is permitted for $f/L$ and $r$ values other than shown.
3. Notation: Plus and minus signs signify pressures acting toward and away from the surfaces, respectively. $r = 1.8 - 0.5f/L$, such wind-directed parallel to ridge.
4. Where two values of $r$ are listed, the roof is subjected to either positive or negative pressures and the roof structure shall be designed for both conditions.

---

**Figure 27.3-3. Main wind force resisting system: external pressure coefficients, $C_p$, for enclosed, partially open buildings and structures—arched roofs.**

---

2. No force coefficient of $C_p$ greater than $-0.8$ shall be used on surfaces that have a rise-to-span ratio that exceeds 0.6 (Section 26.11), and all the elements, and

3. Total load (drag force) on the barrel above grade of horizontal projection of the profile shall be assumed as the plan area of the building surface area of the barrel multiplied by a factor for the elevated position of the building to the mean roof height

**27.3.3 Domed Roofs** The external pressure on domed roofs shall be determined in accordance with Section 27.3.1 or 27.3.2.

**27.3.2 Domed Roofs with Circular Bases and Nominally Sloped** A rise to diameter ratio that shall be 0.5 or less for buildings of all heights. Linear interpolation is permitted to the value for $h/D = 0$ (in parallel to edge for all of the elements) by the mean wind velocity and depth forces on the parabolic-shaped faces of the building parallel to each edge. (See Figs. 27.3-2 for flat roofs or stepped or with multiple ridges.)

**27.3.3 Roof Overhangs** The positive external pressure on the underside and the overhang on windward side of roof shall be the same as the top surface pressure for any horizontal distance from the windward edge up to the edge of the overhang

Where the lower wall surface has a vertical face at the building base, and:

- Use pressure coefficients. To include pressures for each element as determined in Section 26.11 for vertical face of the building to the bottom surfaces of the building, the mean height pressure factor may be assumed as the wind pressure calculated for a solid member, the wind pressure shall be calculated accordingly.

- For other pressure systems with an angle of attack of wind from horizontal if the building face is at an angle of elevation at the top surface not less for walls up to top, the respective external pressure shall be determined by the following equation and wind speed calculated at vertical pressure:

$$p_s = q_h K_z G C_p (GC_p) \tag{27.3-1}$$

where
- Velocity pressure evaluated at mean roof height $q_h$ used as the exposure as defined in Section 26.7.3 that is responsible for the external pressure on the roof surfaces

**27.3.4 Parapets** The design wind pressure for the effect of wind on parapet MWFRS of rigid or flexible buildings is shall be calculated by the following equation:

$$p_p = q_p G C_{pn} \tag{27.3-2}$$

where

$p_p$ = Combined net pressure on the parapet caused by the combination of the net pressures from the front and lower surfaces of the parapet arising from the design net pressure acting toward and away from the front parapets and zones

$q_p$ = Velocity pressure evaluated at the top of the parapet $GC_{pn}$ = Combined net pressure coefficient = +1.5 for windward parapet = -1.0 for leeward parapet.

The net pressure on the parapet shall act normal to the face and be applied to the parapet areas that were not included in the MWFRS loads shall be determined in the following equation:

---

**286** STANDARD ASCE/SEI 7-22

---

```
    ←─0.5L─→ ←─0.5L─→              ←─0.5L─→ ←─0.5L─→
              CNW                              CNE
    Wind       ╱╱╱╱╱╱╱╱                       ╱╱╱╱╱╱╱╱      Wind
  Direction   ╱      ╱╱                       ╱╱      ╱   Direction
    ⇒        ╱      ╱╱                        ╱╱      ╱      ⇐
   γ = 0°   h    θ ╱╱                         ╱╱ θ    h   γ = 180°
           ╱╱╱╱╱╱╱╱╱                          ╱╱╱╱╱╱╱╱╱
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱                 ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
```

### Notation

- $L$ = Horizontal dimension of roof, measured in the along-wind direction, ft (m).
- $h$ = Mean roof height, ft (m).
- $\gamma$ = Direction of wind, degrees.
- $\theta$ = Angle of plane of roof from horizontal, degrees.

### Net Pressure Coefficient, $C_N$

| Roof Angle, θ | Load Case | Wind Direction, $\gamma = 0°$ | | Wind Direction, $\gamma = 180°$ | |
|---------------|-----------|-------------------------------|---|--------------------------------|---|
| | | **Clear Wind Flow** | **Obstructed Wind Flow** | **Clear Wind Flow** | **Obstructed Wind Flow** |
| | | $C_{NW}$ | $C_{NE}$ | $C_{NW}$ | $C_{NE}$ | $C_{NW}$ | $C_{NE}$ | $C_{NW}$ | $C_{NE}$ |
| $< 5.5°$ | A | 1.2 | 0.3 | $-0.5$ | $-1.2$ | 1.2 | 0.3 | $-0.5$ | $-1.2$ |
| | B | $-1.1$ | $-0.1$ | $-1.1$ | $-0.6$ | $-1.1$ | $-0.1$ | $-1.1$ | $-0.6$ |
| 7.5° | A | $-0.6$ | $-1.0$ | $-1.0$ | $-1.5$ | 0.9 | 1.5 | $-0.2$ | $-1.2$ |
| | B | $-1.4$ | 0.0 | $-1.7$ | $-0.8$ | 1.6 | 0.3 | 0.8 | $-0.3$ |
| 15° | A | $-0.9$ | $-1.3$ | $-1.1$ | $-1.5$ | 1.3 | 1.6 | 0.4 | $-1.1$ |
| | B | $-1.9$ | 0.0 | $-2.1$ | $-0.6$ | 1.8 | 0.6 | 1.2 | $-0.3$ |
| 22.5° | A | $-1.5$ | $-1.6$ | $-1.5$ | $-1.7$ | 1.7 | 1.8 | 0.5 | $-1.0$ |
| | B | $-2.4$ | $-0.3$ | $-2.3$ | $-0.9$ | 2.2 | 0.7 | 1.3 | 0.0 |
| 30° | A | $-1.8$ | $-1.8$ | $-1.5$ | $-1.8$ | 2.1 | 2.1 | 0.6 | $-1.0$ |
| | B | $-2.5$ | $-0.5$ | $-2.3$ | $-1.1$ | 2.6 | 1.0 | 1.6 | 0.1 |
| 37.5° | A | $-1.8$ | $-1.8$ | $-1.5$ | $-1.8$ | 2.1 | 2.2 | 0.7 | $-0.9$ |
| | B | $-2.4$ | $-0.6$ | $-2.2$ | $-1.1$ | 2.7 | 1.1 | 1.9 | 0.3 |
| 45° | A | $-1.6$ | $-1.8$ | $-1.3$ | $-1.8$ | 2.2 | 2.5 | 0.8 | $-0.9$ |
| | B | $-2.3$ | $-0.7$ | $-1.9$ | $-1.2$ | 2.6 | 1.4 | 2.1 | 0.4 |

### Notes

1. $C_{NW}$ and $C_{NE}$ denote net pressures (contributions from top and bottom surfaces) for windward and leeward half of roof surfaces, respectively.

2. Clear wind flow denotes relatively unobstructed wind flow with blockage less than or equal to 50%. Obstructed wind flow denotes objects below roof inhibiting wind flow (>50% blockage).

3. For values of θ between 7.5 and 45 degrees, linear interpolation is permitted.

4. For free roofs with 0.05≤h/L<0.25 and θ<5 degrees, use Figure 27.3-7.

5. Plus and minus signs signify pressures acting toward and away from the top roof surface, respectively.

6. All load cases shown for each roof angle shall be investigated.

---

**Figure 27.3-4. Main wind force resisting system (0.25 ≤ $h/L$ ≤ 1.0): net pressure coefficient, $C_N$, for open buildings with monoslope free roofs ($\theta \leq$ 45°, $\gamma = 0°$, 180°).**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 287

---

```
                    ←──────────L──────────→

                    CNW       CNE
       Wind         ╱╱╱╱╱╱   ╱╱╱╱╱╱╱
    Direction      ╱      ╲θ╱      ╱╱
       ⇒          ╱        ╲       ╱╱
     γ = 0°      h          ╲      ╱╱
                             ╲θ   ╱
                 ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
```

### Notation

- $L$ = Horizontal dimension of roof, measured in the along-wind direction, ft (m).
- $h$ = Mean roof height, ft (m).
- $\gamma$ = Direction of wind, degrees.
- $\theta$ = Angle of plane of roof from horizontal, degrees.

### Net Pressure Coefficient, $C_N$

| Roof Angle, θ | Load Case | Wind Direction, $\gamma = 0°$, 180° | | | |
|---------------|-----------|-------------------------------------|---|---|---|
| | | **Clear Wind Flow** | | **Obstructed Wind Flow** | |
| | | $C_{NW}$ | $C_{NE}$ | $C_{NW}$ | $C_{NE}$ |
| 7.5° | A | 1.1 | $-0.3$ | $-1.6$ | $-1.0$ |
| | B | 0.2 | $-1.2$ | $-0.9$ | $-1.7$ |
| 15° | A | 1.1 | $-0.4$ | $-1.2$ | $-1.0$ |
| | B | 0.1 | $-1.1$ | $-0.6$ | $-1.6$ |
| 22.5° | A | 1.1 | 0.1 | $-1.2$ | $-1.2$ |
| | B | $-0.1$ | $-0.8$ | $-0.8$ | $-1.7$ |
| 30° | A | 1.3 | 0.3 | $-0.7$ | $-0.7$ |
| | B | $-0.1$ | $-0.9$ | $-0.2$ | $-1.1$ |
| 37.5° | A | 1.3 | 0.6 | $-0.6$ | $-0.6$ |
| | B | $-0.2$ | $-0.6$ | $-0.3$ | $-0.9$ |
| 45° | A | 1.1 | 0.9 | $-0.5$ | $-0.5$ |
| | B | $-0.3$ | $-0.5$ | $-0.3$ | $-0.7$ |

### Notes

1. $C_{NW}$ and $C_{NE}$ denote net pressures (contributions from top and bottom surfaces) for windward and leeward half of roof surfaces, respectively.

2. Clear wind flow denotes relatively unobstructed wind flow with blockage less than, or equal to, 50%. Obstructed wind flow denotes objects below roof inhibiting wind flow (> 50% blockage).

3. For values of θ between 7.5 and 45 degrees, linear interpolation is permitted. For values of θ less than 7.5 degrees, use $C_N$ from Figure 27.3-4.

4. Plus and minus signs signify pressures acting toward and away from the top roof surface, respectively.

5. All load cases shown for each roof angle shall be investigated.

---

**Figure 27.3-5. Main wind force resisting system (0.25 ≤ $h/L$ ≤ 1.0): net pressure coefficient, $C_N$, for open buildings with pitched free roofs ($\theta \leq$ 45°, $\gamma = 0°$, 180°).**

---

**288** STANDARD ASCE/SEI 7-22

---

```
                    ←──────L──────→

                    CNW       CNE
       Wind         ╱╱╱╱╱╱   ╱╱╱╱╱╱╱
    Direction      ╱      ╲ ╱      ╱╱
       ⇒          ╱      θ ╲ θ     ╱╱
     γ = 0°      h                 ╱╱

                 ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
```

### Notation

- $L$ = Horizontal dimension of roof, measured in the along-wind direction, ft (m).
- $h$ = Mean roof height, ft (m).
- $\gamma$ = Direction of wind, degrees.
- $\theta$ = Angle of plane of roof from horizontal, degrees.

### Net Pressure Coefficient, $C_N$

| Roof Angle, θ | Load Case | Wind Direction, $\gamma = 0°$, 180° | | | |
|---------------|-----------|-------------------------------------|---|---|---|
| | | **Clear Wind Flow** | | **Obstructed Wind Flow** | |
| | | $C_{NW}$ | $C_{NE}$ | $C_{NW}$ | $C_{NE}$ |
| 7.5° | A | $-1.1$ | 0.3 | $-1.6$ | $-0.5$ |
| | B | $-0.2$ | 1.2 | $-0.9$ | $-0.8$ |
| 15° | A | $-1.1$ | 0.4 | $-1.2$ | $-0.5$ |
| | B | 0.1 | 1.1 | $-0.6$ | $-0.8$ |
| 22.5° | A | $-1.1$ | $-0.1$ | $-1.2$ | $-0.6$ |
| | B | $-0.1$ | 0.8 | $-0.8$ | $-0.8$ |
| 30° | A | $-1.3$ | $-0.3$ | $-1.4$ | $-0.4$ |
| | B | 0.1 | 0.9 | $-0.2$ | $-0.5$ |
| 37.5° | A | $-1.3$ | $-0.6$ | $-1.4$ | $-0.3$ |
| | B | 0.2 | 0.6 | $-0.3$ | $-0.4$ |
| 45° | A | $-1.1$ | $-0.9$ | $-1.2$ | $-0.3$ |
| | B | 0.3 | 0.5 | $-0.3$ | $-0.4$ |

### Notes

1. $C_{NW}$ and $C_{NE}$ denote net pressures (contributions from top and bottom surfaces) for windward and leeward half of roof surfaces, respectively.

2. Clear wind flow denotes relatively unobstructed wind flow with blockage less than, or equal to, 50%. Obstructed wind flow denotes objects below roof inhibiting wind flow (> 50% blockage).

3. For values of θ between 7.5 and 45 degrees, linear interpolation is permitted. For values of θ less than 7.5 degrees, use $C_N$ from Figure 27.3-4.

4. Plus and minus signs signify pressures acting toward and away from the top roof surface, respectively.

5. All load cases shown for each roof angle shall be investigated.

---

**Figure 27.3-6. Main wind force resisting system (0.25 ≤ $h/L$ ≤ 1.0): net pressure coefficient, $C_N$, for open buildings with troughed free roofs ($\theta \leq$ 45°, $\gamma = 0°$, 180°).**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 289

---

```
        ←─L─→              ←─L─→              ←─L─→
         ╱  ╲               ╱  ╲               ╱  ╲
        ╱ ↑  ╲             ╱ ↑  ╲             ╱ ↑  ╲
       ╱  h   ╲           ╱  h   ╲           ╱  h   ╲
      ╱        ╲         ╱        ╲         ╱        ╲
  Monoslope     ╲    Pitched       ╲    Trough        ╲
                 ╲                  ╲                   ╲
     Distance     ╲     Distance     ╲     Distance     ╲
      from         ╲      from         ╲      from        ╲
    Windward        ╲   Windward        ╲   Windward       ╲
      Edge           ╲     Edge           ╲     Edge         ╲
  θ ╱                ╱ θ ╱      θ        ╱ θ ╱               ╱

   ╱╱   Wind Direction    ╱╱   Wind Direction    ╱╱   Wind Direction
         γ = 90°                γ = 90°                γ = 90°
```

### Notation

$h$ = Mean roof height, ft (m). See Figures 27.3-4, 27.3-5, or 27.3-6, for a graphical depiction of this dimension.

$\gamma$ = Direction of wind, degrees.

$\theta$ = Angle of plane of roof from horizontal, degrees.

### Net Pressure Coefficient, $C_N$

| Horizontal Distance from Windward Edge | Roof Angle θ | Load Case | Clear Wind Flow $C_N$ | Obstructed Wind Flow $C_N$ |
|----------------------------------------|--------------|-----------|----------------------|---------------------------|
| $\leq h$ | All shapes | A | $-0.8$ | $-1.2$ |
| | $\theta \leq 45°$ | B | 0.8 | 0.5 |
| $> h, \leq 2h$ | All shapes | A | $-0.6$ | $-0.9$ |
| | $\theta \leq 45°$ | B | 0.5 | 0.5 |
| $> 2h$ | All shapes | A | $-0.3$ | $-0.6$ |
| | $\theta \leq 45°$ | B | 0.3 | 0.3 |

### Notes

1. $C_N$ denotes net pressures (contributions from top and bottom surfaces).

2. Clear wind flow denotes relatively unobstructed wind flow with blockage less than or equal to 50%. Obstructed wind flow denotes objects below roof inhibiting wind flow (>50% blockage).

3. Plus and minus signs signify pressures acting toward and away from the top roof surface, respectively.

4. All load cases shown for each roof angle shall be investigated.

---

**Figure 27.3-7. Main wind force resisting system: net pressure coefficient, $C_N$, for open buildings with free roofs ($\theta \leq$ 45°, $\gamma =$ 90°, 270°).**

---

**290** STANDARD ASCE/SEI 7-22

---

```
       WIND ⇒                    ⇓
                                        RESULTANT COMBINED LOAD
    ┌───────────┐          ┌───────────┐
    │     γ     │          │    p_Wy   │         0.75p_Wy
    │←─────x────→│          │     γ     │      ↓ ↓ ↓ ↓ ↓ ↓ ↓
    │           │          │←─────x────→│         ┌───────────┐
  p_Wx         p_Lx        │           │         │     γ     │
    │           │          │    p_Ly   │  0.75p_Wx│←─────x────→│ 0.75p_Lx
    └───────────┘          └───────────┘         │           │
                                                  └───────────┘
                                                   ↓ ↓ ↓ ↓ ↓ ↓ ↓
                                                    0.75p_Ly
                           CASE 3
```

Full design pressure on the projected wall area perpendicular to each principal axis of the structure, considered separately along each principal axis. Full design pressure on side walls and roof areas for wind along each principal axis as specified in Figures 27.3-1 through 27.3-7. All pressures act simultaneously for each principal wind direction.

Wall pressures are 75% of Case 1. For roof pressures, see Note 2. All pressures act simultaneously.

### CASE 2

```
                                ⇓
                         ┌───────────┐
                         │ 0.75p_Wy  │
                         │     γ     │
                         │←─────x────→│
                         │           │
                         │  0.75p_Ly │
                         └───────────┘

    ┌───────────┐                            ┌───────────┐
    │     ┌─→M_x │                           │  0.563p_Wy│
  B_x│           │                           │ ↓ ↓ ↓ ↓ ↓ ↓│
    │           │         ┌───────────┐      │     ┌─→M_x│
    ▼           │         │    ┌─→M_x │   0.563p_Wx│     │0.563p_Lx
  0.75p_Wx  0.75p_Lx      │     γ     │      │           │
                          │←─────x────→│      │  0.563p_Ly│
                          │  0.75p_Ly │      └───────────┘
                          └───────────┘

  M_x = 0.75(p_Wx + p_Lx)B_x e_x    M_x = 0.75(p_Wy + p_Ly)B_y e_y    M_x = 0.563(p_Wx + p_Lx)B_x e_x + 0.563(p_Wy + p_Ly)B_y e_y
  e_x = ±0.15B_x                     e_y = ±0.15B_y                     e_x = ±0.15B_x              e_y = ±0.15B_y
```

Three-quarters of design wind pressure on the projected wall area perpendicular to each principal axis of the structure and sidewalls in conjunction with a torsional moment, considered separately along each principal direction. Roof pressures are 75% of Case 1. All pressures and torsion act simultaneously for each principal wind direction.

### CASE 4

Wall pressures and torsional moment are 75% of Case 2 (wall pressures are 56.3% of Case 1). For roof pressures see Note 2. All pressures and torsion act simultaneously.

### Notation

- $p_{Wx}, p_{Wy}$ = Windward wall design pressure acting in the $x$, $y$ principal direction, respectively.
- $p_{Lx}, p_{Ly}$ = Leeward wall design pressure acting in the $x$, $y$ principal direction, respectively.
- $B_x, B_y$ = Horizontal dimension of building normal to the wind in the $x$, $y$ principal direction, respectively.
- $e_x, e_y$ = Eccentricity from the $x$, $y$ principal axis of the structure, respectively, as shown for rigid buildings, or as defined by Equation (27.3-4) for flexible buildings. See also Note 4.
- $M_x$ = Torsional moment per unit height acting about a vertical axis of the building.

### Notes

1. Diagrams show plan views of buildings.

2. Pressures on roof are not shown for clarity. For Cases 3 and 4 the resulting pressure on any roof area defined by the two principal wind directions of Cases 1 and 2 shall be 100% of the larger value of the roof pressures defined for Cases 1 and 2, respectively.

3. Pressures on sidewalls for Cases 1 and 2 are not shown for clarity and need not be considered at floors with rigid diaphragms continuous with the sidewalls.

4. $M_x$ shall be applied on rigid diaphragms. On floors with semi-rigid or flexible diaphragms, or without diaphragms, it shall be permitted to apply $M_x$ using an equivalent distributed pressure block on all walls receiving normal wind pressure, applied in the proportion specified for each wall in Figure 27.3-1, or using other rational methods.

---

**Figure 27.3-8. Main wind force resisting system, design wind load cases.**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 291

---

The MWFRS of buildings of all heights, the wind loads of which have been determined under the provisions of this chapter, shall be designed for the wind load cases as defined in Figure 27.3-8.

**EXCEPTION:** Buildings meeting the requirements of Section D.1 of Appendix D need only be designed for Case 1 and Case 3 of Figure 27.3-8.

The eccentricity $e$ for rigid buildings shall be measured from the geometric center of the building face and shall be considered for each principal axis $(e_x, e_y)$. The eccentricity $e$ for flexible buildings shall be determined from the following equation and shall be considered for each principal axis $(e_x, e_y)$:

$$e = \frac{e_Q + 1.7L_z\sqrt{(g_QG e_Q)^2 + (g_RRe_R)^2}}{1 + 1.7L_z\sqrt{(g_QQ)^2 + (g_RR)^2}} \tag{27.3-4}$$

where

$e_Q$ = Eccentricity $e$ as determined for rigid buildings in Figure 27.3-8; and

$e_R$ = Distance between the elastic shear center and center of mass of each floor, and $I_{zz}$, $g_Q$, $Q$, $g_R$, and $R$ shall be as defined in Section 26.11.

The sign of the eccentricity $e$ shall be plus or minus, whichever causes the more severe load effect.

## 27.4 CONSENSUS STANDARDS AND OTHER REFERENCED DOCUMENTS

No consensus standards and other documents that shall be considered part of this standard are referenced in this chapter.

---

**292** STANDARD ASCE/SEI 7-22
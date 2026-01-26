# Chapter 32: Tornado Loads

**ASCE 7-22 Minimum Design Loads and Associated Criteria for Buildings and Other Structures**

---

*This chapter combines pages 415-459 from ASCE 7-22*

---

**32.1.1 Scope.** Buildings and structures classified as Risk Category III or IV shall be designed in accordance with the tornado procedure specified in Figure 32.1-1, including the main wind force resisting system (MWFRS), components and cladding (C&C), and building or other structure tornado procedure. The provisions of this chapter, or the wind loads determined by other chapters in accordance with Chapter 1, shall not be multiplied by the importance factor $I_w$. The building or other structure tornado loads specified in this section shall take precedence over all other wind loads.

**User Note:** The tornado loads specified in this chapter provide minimum values for use in the design of buildings and other structures. The provisions are for use in determining the load-resisting structural elements for all heights of buildings and structures and therefore are only required for Risk Category III and IV buildings and structures to meet the same standard of performance and life safety requirements as Risk Category I and II buildings under extreme wind speed periods for Risk Category III and IV, respectively (which are the same as that required for Risk Category III and II buildings in accordance with Chapter 26). Tornadic wind speed and therefore are only required for Risk Category III and IV buildings, as identified in Section 1.5.1.

## 32.1.1 Tornado Loads on the Main Wind Force Resisting System

1. Determine Procedure for buildings of all heights or structures: Tornado loads on the MWFRS shall be determined using Figure 32.1-1.
2. Directional procedures for buildings of all heights or structures: The wind, topography, and effects of adjacent buildings shall be determined using one of the following:
   - Chapter 26: Directional Procedure for buildings of all heights or structures and cladding (See Section 26.1.1).
   - Chapter 27: Wind Loads procedure for any building or other structure (See Section 27.1.1).
   - Chapter 31: Wind tunnel procedure for any building or other structure regardless of height, surrounding terrain, and geometry. Multiple systems are associated with Chapter 31 by Commentary Section 32.2.2.

## 32.1.2 Tornado Loads on Building Components, Cladding, and Other Nonstructural Elements

1. Tornado loads on building appurtenance, envelope (C&C)
2. Directional Procedure for buildings of all heights or structures: applicable, shall be determined using one of the following procedures specified in this chapter.
3. Building or Structures with height less than or equal to 60 ft (18.3 m) in height: The directional procedure (see Chapter 26).
4. Building or structures between 60 ft (18.3 m) and 160 ft (48.8 m) in height: Components and cladding envelope forces design per Chapter 27 for buildings meeting the requirements specified below.

## 32.2 DEFINITIONS

The definitions in Section 32.2 apply to the provisions of Chapter 32. Symbols and notation not defined in this chapter shall be as defined in accordance with Chapter 1, unless otherwise as defined.

**TORNADO LOAD EFFECT FROM AN APPLICABLE CLASS:** The ASCE Standard provides design procedures based upon buildings intended for tornado design.

**OTHER STRUCTURES, SOLID/ISOLATED:** A structure that is completely sealed (e.g., by a windows not allowed with low permeability) not open to admit or release air. For purposes of tornado design classification, the tornado openings, including those for limited internal spaces or other openings, such as exterior or interior window openings within the tornado, are not considered.

**TORNADO-PRONE REGION:** The area of the United States which has a mapped tornado speed of greater than or equal to 130 mph (58 m/s) from Equation (32.5.1)-(1) and (32.5.1)-(2), excluding Chapter 26.

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **353**

---

This page contains a map of the western United States showing county boundaries and tornado-prone regions. The map shows:

- State boundaries for Washington, Oregon, California, Idaho, Nevada, Utah, Arizona, Montana, Wyoming, Colorado, New Mexico, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas
- Counties are shown with boundary lines
- Shaded regions indicating "Tornado-prone region"
- Two levels of shading in the legend:
  - Medium gray: "Tornado-prone region"
  - Light gray: "Outside tornado-prone region"

The tornado-prone regions are concentrated primarily in the central and eastern portions of the mapped area, with less tornado activity in the western coastal and mountain states.

---

**Figure 32.1-1. Tornado-prone region.**

**354** **STANDARD ASCE/SEI 7-22**

---

```
        ┌─────────────────────────────────────────┐
        │ Determine whether Design for            │
        │      Tornado Loads is Required          │
        └────────────────┬────────────────────────┘
                         │
                         ▼
           ┌────────────────────────────────┐
        1  │ Risk Category III or IV,       │      no
           │  per Section 1.5?              │───────────┐
           └────────┬───────────────────────┘           │
                    │ yes                                │
                    ▼                                    │
           ┌────────────────────────────────┐           │
        2  │ In Tornado-Prone Region,       │      no   │
           │  per Figure 32.1-1?            │───────────┤
           └────────┬───────────────────────┘           │
                    │ yes                                │
                    ▼                                    │
           ┌────────────────────────────────┐           │
        3  │ V_t ≥ 60 mph (26.8 m/s), per  │      no   │      ┌──────────────┐
           │    Section 32.5.2?             │───────────┤      │   Design for │
           └────────┬───────────────────────┘           │      │ Tornado Loads│
                    │ yes                                │      │   is NOT     │
                    ▼                                    │      │   Required   │
           ┌────────────────────────────────┐           │      └──────────────┘
        4  │ For Exposure B: V_t ≥ 0.5V,   │      no   │
           │  or                            │───────────┘
           │ For Exposure C: V_t ≥ 0.6V,   │
           │  or                            │
           │ For Exposure D: V_t ≥ 0.67V   │
           │  per Section 32.5.2?           │
           └────────┬───────────────────────┘
                    │ yes
                    ▼
        ┌──────────────────────────────────────┐
        │    Design for Tornado Loads          │
        │         is Required                  │
        └──────────────────────────────────────┘
```

**Figure 32.1-2. Flowchart of process for determining when design for tornado loads is required.**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **355**

---

```
  Chapter 32: General Requirements. The basic procedure used in determination of tornado
              loads is the following: (See Section 32.1 and Commentary C32.1):

              ┌─────────────────────────────────────────────────────────────┐
              │ Tornado speed, V_t, per Section 32.5.1                      │
              │ Effective plan area, A_ef, per Section 32.5.4               │
              │ Ground elevation factor, K_e, per Section 32.8              │
              │ Tornado velocity pressure coefficient, K_z(zt)_m, and       │
              │   K_zt, per Section 32.10                                   │
              │ Tornado velocity pressure exposure coefficient, K_z or K_h  │
              │ Tornado directional factor, K_d, per Section 32.6           │
              │ Tornado pressure coefficient, G_C, or Section 32.13.        │
              └──────────────────────┬──────────────────────────────────────┘
                                     │
   ┌─────────────────────────────────┼─────────────────────────────────┐
   │                                 │                                 │
   │                                 ▼                                 │
   │     Tornado loads on the MWFRS shall be                          │
   │     determined in accordance with the following:                 │
   │                                                                   │
   │      Chapter 27: Directional procedure for                       │
   │      buildings of all heights or modified by Section             │
   │      32.5.1.3 of this standard. Use approach factors,            │
   │      expressions, and conditions, and projections per            │
   │      Commentary Section 32.1.                                    │
   │                                                                   │
   │      Chapter 31: Wind tunnel procedure for any                   │
   │      building or other structure as modified by                  │
   │      Section 32.5.1.3 of this standard.                         │
   │                                                                   │
   └───────────────────────────────────────────────────────────────────┘

      Figure 32.1-3. Outline of process for determining tornado loads.
```

2. For Risk Category IV buildings, the tornado wind speed shall be determined in accordance with Figures 32.5-1A through 32.5-2E. For alternative uses the values of tornado wind speed from sections or other sources unless approved by the Authority Having Jurisdiction. V_t shall be determined from other structure Subsection shall be determined in accordance with Wind Speed sections 26.5.1, 26.5.2, and 26.5.3 as Alternatively, linear interpolation shall be permitted for determining tornado wind speeds between the values of 32.5-2A and 32.5-2E as follows:

$$V_{t,map} = V_{500} + (V_{1700} - V_{500}) \times \frac{(MRI - 500)}{(1700 - 500)}$$

**32.5.2 Design for Tornado Loads Not Required.** For Risk Category III and IV buildings and other structures not located in the tornado-prone region as shown in Figure 32.1-1, design for tornado loads is not required.

**32.5.2.1 Effective Plan Area.** The effective plan area, $A_{ef}$ of the building or other structure shall be defined as the vertical projection of the structure normal area of the structure normal to the direction of the wind plus one-half of the vertical area of all exterior roof or walls oriented within 45 degrees of the wind direction and of all exterior surfaces of buildings or other structures.

**32.5.2.2 Essential Facilities and Essential Facilities.** For Essential Facilities and Essential Facilities (Risk Category IV), values of V_t shall be determined as provided by Equation (32.5.1)-(1) in accordance with Table 1.5-2. For buildings or structures or other structure that are permanently designed as Essential Facilities and designed for horizontal winds that use all roof and wall surfaces oriented within 45 degrees of the topographic factor, Eq. $K_{zt}$ shall $K_{e}$ use all values and other wind loads shall be determined in accordance with Section 32.10, tornado directional, and internal pressure coefficients shall be determined in accordance with Section 32.6.

**32.5.2.3 Topographic Factor $K_{zt}$:** The values based upon Eq.(32.5.1)-(1) for External Facilities and include tornado K_{zt}$ determined in accordance with the provisions outlined in Section 32.8. When required by Section 32.10 in these Exposure categories to conform from the topographic features per Section 32.8 at the height above ground $Z$ at which the external pressure shall be evaluated from Equation (32.1)-(1) or Equation (32.1)-(2) using V_{ult} and load distributions. Commentary Section 26.8 uses: tornado velocities or tornado velocity coefficient Kd, and shall Kd be evaluated from Equations (32.5.1)-(1) using K_{zt}$ for height h using Commentary Section 32.6.

**32.6 TORNADO GUST FACTOR**

The tornado directional factor, $K_d$, shall be determined from Table 32.6-1 or Equation (32.6)-1.

## 32.7 TORNADO EXPOSURE

Tornado loads as defined by exposure requirements $K_z$ and $K_d$ are determined as shown in Section 32.10.1. Exposure requirements $E_w$ and use determined as described in Section 32.8 for Exposure C and are determined from the lowest value of tornado velocity pressure from Section 32.8 and Section 32.10.

## 32.8 TOPOGRAPHIC FACTOR

Tornado wind speed at the site caused due to topographic features shall be determined in accordance with Section 26.8.1. Topographic features $K_{zt}$ shall be determined separately.

## 32.9 APPROACH TERRAIN EXPOSURE

Tornado loads shall be analyzed in $K_d$ both with mean wind or at tornadoes speed, and the topography factor exposure factors Kzt, Kd, and tornado coefficients shall determined separately.

## 32.10 TORNADO VELOCITY PRESSURE

**32.10.1 Velocity Pressure.** The tornado velocity pressure, $q_z$ for calculating GC_p or K_zt or tornadoes wind, shall be determined at height z in accordance with the following:

(Eq. 32.10-1)

$$q_z = 0.00256K_zK_{zt}K_dV_t^2 \text{ (lb/ft}^2\text{)}$$

(32.10-1)

$$q_z = 0.613K_zK_{zt}K_dV_t^2 I \text{ (N/m}^2\text{)}$$

(32.10-1)

where
- $K_z$ = Tornado velocity pressure exposure coefficient, per $K_z$ or $K_h$ as defined in
- $K_{zt}$ = Topographic factor as defined in Section 32.8 and
- $V_t$ = Tornado speed, per Section 32.5, and
- $I$ = Importance factor from Table 1.5-2, and
- $K_d$ = Tornado directional factor, see Section 32.6.

For height z:

$$K_z = 2.01(z/z_g)^{2/\alpha}$$ for $15 \text{ ft} \leq z \leq z_g$$

**32.10.1.1 Tornado Gust Effect Factor.** The tornado gust-effect factor, $G_f$, for a building or other structure shall be (G_f ≤ 1) or permitted to be determined separately.

**32.10.1.2 Limitations.** Where the embedded wind factors (GC_p) and (GC_pi) are determined separately.

**32.10.1.3 Exposure Coefficients.** (GC_pi) shall be determined in accordance with Section 26.11, Figure 26.11-1, and Commentary Section C26.11.

## 32.11 TORNADO LOAD EFFECTS

**32.11.1 Tornado Gust Effect Factors:** For the tornado gust-effect factor, $G_f$, for a building or other structure shall be $(G_f \geq 0.85)$ or in accordance with Section 26.11 for wind loads. The tornado gust effect factors shall be determined in accordance from the values in Section 26.11 for buildings or other structures with heights and shall be determined from exposure C for all building and commentary from Section 32.11.

**32.11.2 Limitations:** Where the embedded wind factors, (GC_p) and (GC_pi) are determined separately, linear interpolation shall be permitted between the values and both positive and negative coefficients (GC_p) applied for all building.

## 32.12 Tornado External Pressure

Tornado external pressure coefficients, (GC_pi), shall be determined from the tornado coefficients as specified in Section 32.13.1.

The tornado internal pressure coefficients of (GC_pi) shall be determined separately.

## 32.13 TORNADO INTERNAL PRESSURE

Tornado internal pressure coefficients, (GC_{pi}), shall be determined in accordance with Section 32.13.1 or Section 32.13.2.

---

**356** **STANDARD ASCE/SEI 7-22**

---

panel systems shall be equal to the effective plan area, $A_{ef}$ of the largest single panel or group of panels subject to the load case that can occur under the load case determined by considering structural loads and load effects from the ASCE 7 Standard.

**32.5.7 TORNADO EXPOSURE**

The tornado directional factor $K_{d,t}$ shall be determined from Table 26.6-1. For buildings with enclosed or semi-enclosed pressure coefficients for windborne, buildings and other structural components being designed shall be equivalent to a factor that is permitted to be reduced to windborne debris using Table 26.6-1 in the direction being considered.

**32.5.8 TOPOGRAPHIC FACTOR**

Tornado wind speed-up caused due to topographic features shall be determined in accordance with Section 26.8.1. The topographic features K_{zt}$ shall be determined separately in accordance with Section 26.8.

**32.5.9 APPROACH TERRAIN EXPOSURE**

Tornado loads shall follow exposure C or D depending on the surface roughness from Section 26.7.2 or equivalent surface roughness determined separately.

**32.10 TORNADO VELOCITY PRESSURE**

**32.10.1 Velocity Pressure.** The tornado velocity pressure, $q_z$, evaluated at height z shall be determined in accordance with Equation (32.10)-1 or (32.10)-2 for tornado applications.

(Eq. 32.10-1)

$$q_z = 0.00256K_zK_{zt}K_{d,t}V_t^2 \text{ (lb/ft}^2\text{)}$$

(32.10-2)

$$q_z = 0.613K_zK_{zt}K_{d,t}V_t^2 \text{ (N/m}^2\text{)}$$

where
- $K_z$ = Tornado velocity pressure exposure coefficient, per definition in Section 32.10.1.1, evaluated at height z
- $K_{zt}$ = Topographic factor as defined in Section 32.8, evaluated at height z
- $K_{d,t}$ = Tornado directionality factor as defined in Section 32.6
- $V_t$ = Tornado speed from Section 32.5, and
- For height $h$:

$$K_z = 2.01(z/z_g)^{2/\alpha}$$

**32.11.1 Tornado Gust Effect Factor.** The tornado gust-effect factor, $G_f$, for a building or other structure for which the 1st building h is less than or equal to 60 ft or structures shall be determined as follows:

(Eq. 32.11-1)

$$G = 0.85$$

**32.11.1.2 Flexible or Dynamically Sensitive Building, Tornado Gust Factor $G_f$.** For flexible buildings (as defined in Section 26.2) or dynamically sensitive structures in the tornado-prone region, or structures that are not enclosed or partially enclosed, tornado velocity pressure coefficients shall be determined either in accordance with ASTM E1886, Impact resistant systems and impact-resistant coverings for use with other exterior systems as provided in Section 32.11.1.1 for the first mode of the response. For details about tornado-induced systems shall use $G_f$ of 0.85 or alternatively tornado gust factor computed from commentary-outlined wind systems or (b) permanently tornado systems or reduced wind systems designed for impact and determined by the tornado systems at the first mode of vibration as defined from dynamically flexible tornado or computed tornado-induced building in accordance with ASTM ANSI/DASMA 115 detailed tornado wind and tornado impact structural systems.

Where the tornado impact protective systems and impact-resistant structure are in accordance with ASTM E1886/E1996 or ANSI/DASMA 108 standard tornado tests for impact-resistant systems used in place of Section 32.11, with tornado loads used in place of wind pressures determined under wind zones.

**32.11.2 TORNADO ENCLOSURE CLASSIFICATION**

Building for determination of internal GC_{pi} and tornado pressure coefficients for windborne, buildings and other structural components shall be classified as enclosed, partially enclosed, or open as defined in Section 26.2. Windborne debris regions are defined as tornado-prone Regions. Where roof or upper sections (roof) partially enclosed or other building not defined by Enclosure systems being tornado windborne shall be tornado-exposed and normally enclosed are applied in open or defined in Section 26.2.1.2.1.

**32.12.1.2 Openings.** To assign the tornado enclosure classification appropriately, tornado enclosures shall be determined by the design engineer to assign with Enclosure classification category in defined or by evaluating tornado loads windborne roof structure regions shall be tornado protective systems in accordance with Section 32.13.1 is exempt plastic where tornado protective systems are defined.

Where not required by Section 32.12.1.2, to protect glazed openings, structure or tornado enclosure systems shall be protective systems and tornado structures shall be openings or openings tornado windborne debris to limit interior tornado regions classified as openings or (2) to protected or approved with ASTM E1996, Section 32.13.1 shall tornado protective tornado protective tornado systems, tornado protective tornado impactful tornado impact enclosure systems tornado testing systems, tornado tornado protective tornado protective structures of tornado shall permit protective systems in accordance with defined tornado structures.

**32.12.1.2.1 Protection Requirements for Glazed Openings:** Required tornado protective systems shall be protected in accordance with ASTM E1886 or ASTM E1996 (combined with ASTM E1886) and tornado protective tornado structures (e.g., tornado shutters tornado tornado protective tornado systems) shall be tornado protective systems tornado impact resistant tornado protective structures (e.g., tornado tornado tornado tornado impact tornado protective protective systems tornado protective tornado tornado protective systems tornado).

To prevent tornado damage to a tornado openings, glazed tornado protective tornado protective tornado structures shall be tornado windborne tornado resistant tornado tornado protective openings defined by tornado tornado protective tornado tornado systems tornado protective tornado protective systems tornado protective systems (ASTM tornado protective tornado tornado protective tornado protective tornado protective tornado protective systems tornado protective tornado tornado systems tornado systems protective tornado tornado tornado protective systems tornado tornado systems protective tornado protective systems tornado protective tornado protective tornado protective protective tornado protective systems tornado protective tornado systems tornado protective tornado protective tornado protective tornado tornado tornado tornado protective systems tornado tornado protective tornado protective systems).

**32.12.1.3 Protection Requirements for Nonglazed Impact protective protective tornado protective systems tornado protective systems protective protective tornado protective systems protective protective protective protective protective systems tornado protective protective tornado tornado protective tornado protective tornado protective tornado.

Tornado protective protective tornado protective protective protective protective systems tornado protective systems protective protective protective tornado protective tornado protective protective tornado tornado protective tornado tornado protective protective protective protective protective tornado protective tornado protective protective protective protective protective tornado protective protective protective systems tornado protective tornado protective protective protective tornado tornado protective systems tornado tornado tornado protective systems protective tornado protective tornado protective protective protective protective protective protective systems tornado tornado protective protective protective protective protective protective protective systems protective protective tornado protective protective tornado protective protective tornado protective tornado tornado tornado tornado tornado protective protective systems tornado protective tornado protective tornado protective tornado protective protective protective protective.

For buildings protective protective protective protective protective protective tornado tornado tornado tornado protective protective protective protective protective protective tornado tornado protective protective protective tornado protective tornado protective tornado tornado protective protective protective protective tornado tornado protective protective protective protective protective tornado protective tornado tornado protective protective protective tornado tornado protective protective tornado protective tornado tornado protective protective protective protective tornado tornado protective protective protective protective protective tornado protective tornado protective.

**32.13 TORNADO INTERNAL PRESSURE**

Tornado internal pressure coefficients, (GC_{pi}), shall be determined from tornado wind pressures based on building and other structure protective tornado protective tornado protective tornado protective tornado protective systems protective tornado tornado protective protective systems protective protective tornado protective protective protective protective protective tornado.

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **357**

---

This page contains a map of the western United States showing county-level tornado wind speed contours. The map displays:

- State boundaries for Washington, Oregon, California, Idaho, Montana, Wyoming, Nevada, Utah, Colorado, Arizona, New Mexico, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas
- County boundaries shown as fine grid lines
- Contour lines are not visible or minimal in this western region

### Notes:

1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

---

**Figure 32.5-1A. Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 1 ft² (0.1 m²).**

**358** **STANDARD ASCE/SEI 7-22**

---

This page contains a map of the eastern and central United States showing tornado wind speed contours. The map displays:

- State boundaries for North Dakota, South Dakota, Minnesota, Wisconsin, Michigan, Iowa, Illinois, Indiana, Ohio, Missouri, Kentucky, Tennessee, Arkansas, Mississippi, Louisiana, and portions of neighboring states
- County boundaries shown as fine grid lines throughout
- Contour lines showing tornado wind speeds with values labeled:
  - 78 mph contour in the central region
  - 70 mph contour extending from the southwest through the central plains
  - 60 mph contour in the eastern regions
  - 50 mph contour in the far eastern states

The highest tornado speeds (78-80 mph) are concentrated in the central plains region (Oklahoma, Kansas, parts of Texas), with speeds decreasing toward the coasts.

### Notes:

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability ≈ 0.000588, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE 7 Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

**Figure 32.5-1A (Continued). Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 1 ft² (0.1 m²).**

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **359**

---

This page contains a map of the western United States showing county-level tornado wind speed contours for an effective plan area of 2,000 ft² (186 m²). The map displays:

- State boundaries for Washington, Oregon, California, Idaho, Montana, Wyoming, Nevada, Utah, Colorado, Arizona, New Mexico, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas
- County boundaries shown as fine grid lines
- Minimal or no visible contour lines in the western region, indicating low or no tornado wind speeds in these areas

### Notes:

1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

---

**Figure 32.5-1B. Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 2,000 ft² (186 m²).**

**360** **STANDARD ASCE/SEI 7-22**

---

This page contains a map of the eastern and central United States showing tornado wind speed contours for an effective plan area of 2,000 ft² (186 m²). The map displays:

- State boundaries for North Dakota, South Dakota, Minnesota, Wisconsin, Michigan, Iowa, Illinois, Indiana, Ohio, Missouri, Kentucky, Tennessee, Arkansas, Mississippi, Louisiana, and portions of neighboring states
- County boundaries shown as fine grid lines throughout
- Contour lines showing tornado wind speeds with values labeled:
  - 80 mph contour in the central plains region
  - 70 mph contour extending from the southwest through the central states
  - 60 mph contour in the mid-states
  - 50 mph contour in the eastern regions

The highest tornado speeds (80 mph) are concentrated in the central plains region, with speeds decreasing progressively toward the east coast.

### Notes:

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability ≈ 0.000588, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE 7 Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

**Figure 32.5-1B (Continued). Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 2,000 ft² (186 m²).**

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **361**

---

This page contains a map of the western United States showing county-level tornado wind speed contours for an effective plan area of 10,000 ft² (929 m²). The map displays:

- State boundaries for Washington, Oregon, California, Idaho, Montana, Wyoming, Nevada, Utah, Colorado, Arizona, New Mexico, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas
- County boundaries shown as fine grid lines
- Minimal or no visible contour lines in the western region, indicating low or no tornado wind speeds in these areas

### Notes:

1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

---

**Figure 32.5-1C. Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 10,000 ft² (929 m²).**

**362** **STANDARD ASCE/SEI 7-22**

---

This page contains a map of the eastern and central United States showing tornado wind speed contours for an effective plan area of 10,000 ft² (929 m²). The map displays:

- State boundaries for North Dakota, South Dakota, Minnesota, Wisconsin, Michigan, Iowa, Illinois, Indiana, Ohio, Missouri, Kentucky, Tennessee, Arkansas, Mississippi, Louisiana, and portions of neighboring states
- County boundaries shown as fine grid lines throughout
- Contour lines showing tornado wind speeds with values labeled:
  - 84 mph contour in the central plains region (Oklahoma/Kansas area)
  - 80 mph contour surrounding the 84 mph zone
  - 70 mph contour extending through the central states
  - 60 mph contour in the mid-states
  - 50 mph contour in the eastern regions

The highest tornado speeds (84 mph) are concentrated in the central plains region (Oklahoma, Kansas), with speeds decreasing progressively toward both coasts.

### Notes:

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability ≈ 0.000588, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE 7 Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

**Figure 32.5-1C (Continued). Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 10,000 ft² (929 m²).**

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **363**

---

This page contains a map of the western United States showing county-level tornado wind speed contours for an effective plan area of 40,000 ft² (3,716 m²). The map displays:

- State boundaries for Washington, Oregon, California, Idaho, Montana, Wyoming, Nevada, Utah, Colorado, Arizona, New Mexico, North Dakota, South Dakota, Nebraska, Kansas, Oklahoma, and Texas
- County boundaries shown as fine grid lines
- Minimal or no visible contour lines in the western region, indicating low or no tornado wind speeds in these areas

### Notes:

1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

---

**Figure 32.5-1D. Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 40,000 ft² (3,716 m²).**

**364** **STANDARD ASCE/SEI 7-22**

---

This page contains a map of the eastern and central United States showing tornado wind speed contours for an effective plan area of 40,000 ft² (3,716 m²). The map displays:

- State boundaries for North Dakota, South Dakota, Minnesota, Wisconsin, Michigan, Iowa, Illinois, Indiana, Ohio, Missouri, Kentucky, Tennessee, Arkansas, Mississippi, Louisiana, and portions of neighboring states
- County boundaries shown as fine grid lines throughout
- Contour lines showing tornado wind speeds with values labeled:
  - 89 mph contour in the central plains region (Oklahoma/Kansas area)
  - 80 mph contour surrounding the 89 mph zone
  - 70 mph contour extending through the central states
  - 60 mph contour in the mid-states
  - 50 mph contour in the eastern regions

The highest tornado speeds (89 mph) are concentrated in the central plains region (Oklahoma, Kansas), with speeds decreasing progressively toward both coasts.

### Notes:

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability ≈ 0.000588, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE 7 Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

**Figure 32.5-1D (Continued). Tornado speeds for Risk Category III buildings and other structures, for effective plan area of 40,000 ft² (3,716 m²).**

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** **365**

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                366

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                367

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                368

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                369

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                370

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                371

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                372

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                373

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                374

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                375

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                376

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                377

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                378

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                379

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                380

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                381

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                382

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                383

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                384

---

This page contains a tornado speed contour map showing wind speeds across the United States.

**Map Description:** Contour map of the United States showing tornado wind speed values for Risk Category III or IV buildings. The map includes state boundaries, county lines, and contour lines indicating tornado wind speeds in miles per hour (mph).

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.
4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 3% probability of exceedance in 50 years (annual exceedance probability = 0.00058, MRI = 1,700 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

---

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                385

---

[Map of United States showing tornado speed contours]

**Figure Description:**
The map shows tornado speed contours across the United States, with emphasis on the central and southeastern regions. Contour lines are labeled with values: 50, 60, 70, 80, 89. The highest values (80-89 mi/h) are concentrated in the central plains states, particularly from Texas northward through Oklahoma, Kansas, and Nebraska. The contours generally decrease moving westward and eastward from this central corridor. The northeastern states show values around 50-60 mi/h, while western states show similar or lower values. Alaska is shown separately in the lower left corner.

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

**Figure 32.5-2G. Tornado speeds for Risk Category IV buildings and other structures, for effective plan area of 1,000,000 ft² (92,903 m²).**

---

**386**                                                **STANDARD ASCE/SEI 7-22**

---

[Map of United States showing tornado speed contours - Continued]

**Figure Description:**
This is a continuation map showing tornado speed contours across the entire continental United States. Contour lines are labeled with values: 50, 60, 70, 80, 89, 90, 100, 106, 110, 120, 125. The highest values (120-125 mi/h) are concentrated in the southern plains, particularly in Texas, Oklahoma, and Louisiana. The contours show a distinctive pattern with peak values in the south-central region, gradually decreasing toward the coasts and northern regions. The northeastern states show values of 50-90 mi/h, increasing from north to south. The western Great Lakes region shows values of 80-89 mi/h. A separate small inset shows Hawaii with lower values around 100 mi/h.

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 1.7% probability of exceedance in 50 years (annual exceedance probability = 0.00033, MRI = 3,000 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

**Figure 32.5-2G (Continued). Tornado speeds for Risk Category IV buildings and other structures, for effective plan area of 1,000,000 ft² (92,903 m²).**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures                387**

---

[Map of United States showing tornado speed contours]

**Figure Description:**
The map shows tornado speed contours across the United States for a larger effective plan area (4,000,000 ft²). Contour lines are labeled with values: 50, 60, 70, 80, 90, 100, 104. The highest values (100-104 mi/h) are concentrated in the central and southern plains states, particularly from Texas northward through Oklahoma, Kansas, Nebraska, and into parts of Iowa. The contours generally decrease moving westward and eastward from this central corridor. The northeastern states show values around 50-70 mi/h, while western states show similar values. Alaska is shown separately in the lower left corner, with values ranging from 50-90 mi/h in certain regions.

**Notes:**
1. Values are 3-s gust speeds in mi/h at 33 ft (10 m) above ground.
2. To convert tornado speeds from mi/h to m/s, multiply mapped values by 0.447.
3. Linear interpolation is permitted between contours. Point values (where shown) are provided to aid with interpolation.

**Figure 32.5-2H. Tornado speeds for Risk Category IV buildings and other structures, for effective plan area of 4,000,000 ft² (371,612 m²).**

---

**388**                                                **STANDARD ASCE/SEI 7-22**

---

[Map of United States showing tornado speed contours - Continued]

**Figure Description:**
This is a continuation map showing tornado speed contours across the entire continental United States for effective plan area of 4,000,000 ft². Contour lines are labeled with values: 67, 70, 80, 90, 100, 104, 110, 113, 120, 130, 138. The highest values (130-138 mi/h) are concentrated in the southern plains, particularly in Texas, Oklahoma, Arkansas, Louisiana, and Mississippi. The contours show a distinctive pattern with peak values in the south-central region, gradually decreasing toward the coasts and northern regions. The northeastern states show values of 67-100 mi/h. The Great Lakes region shows values of 90-104 mi/h. The Gulf Coast region shows elevated values of 110-120 mi/h. A separate small inset shows Hawaii with lower values.

4. Islands, coastal areas, and land boundaries outside the last contour shall use the last tornado speed contour.
5. Tornado speeds correspond to approximately a 1.7% probability of exceedance in 50 years (annual exceedance probability = 0.00033, MRI = 3,000 years).
6. Location-specific tornado speed is permitted to be determined using the ASCE Tornado Design Geodatabase, available at the ASCE 7 Hazard Tool (http://asce7hazardtool.online) or approved equivalent.

**Figure 32.5-2H (Continued). Tornado speeds for Risk Category IV buildings and other structures, for effective plan area of 4,000,000 ft² (371,612 m²).**

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures                389**

---

| Structure Type | Tornado Directionality Factor, $K_{d7}$ |
|----------------|----------------------------------------|
| **Buildings** | |
| Main wind force resisting system | 0.80 |
| Components and cladding | |
| For Essential Facilities and for buildings and other structures required to maintain the functionality of Essential Facilities | 1.0 |
| Roof Zone 1' as shown in Figure 30.3-2A | 0.90 |
| All other cases | 0.75 |
| **Arched roofs, circular domes, and all other structures** | Use value from Table 26.6-1 |

---

## Table 32.10-1. Tornado Velocity Pressure Exposure Coefficients, $K_{zTor}$ and $K_{hTor}$

| Height above Ground Level, $z$ or $h$ | | $K_{zTor}$ and $K_{hTor}$ |
|---------------------------------------|---|---------------------------|
| ft | m | |
| 0-200 | 0-61.0 | 1.0 |
| 250 | 76.2 | 0.96 |
| 300 | 91.4 | 0.92 |
| >328 | >100 | 0.90 |

**Notes:**

1. The tornado velocity pressure exposure coefficient, $K_{zTor}$, is permitted to be determined as follows:
   - For $0 < z \leq 200$ ft (60 m): $K_{zTor} = 1.0$
   - For $200 < z \leq 328$ ft: $K_{zTor} = [(2820 - z)/2620]^2$, where $z$ is in ft
   - [For $61 < z \leq 100$ m): $K_{zTor} = [(861 - z)/800]^2$, where $z$ is in m]
   - For $z > 328$ ft (100 m): $K_{zTor} = 0.90$
2. Linear interpolation for intermediate values of height $z$ is permitted.

---

## Table 32.13-1. Main Wind Force Resisting System and Components and Cladding Tornado Internal Pressure Coefficient, $(GC_{piT})$

| Enclosure Classification | Criteria for Enclosure Classification | Internal Pressure Combined with Atmospheric Pressure Change | Tornado Internal Pressure Coefficient, $(GC_{piT})$ |
|--------------------------|--------------------------------------|-----------------------------------------------------------|---------------------------------------------------|
| Sealed other structures | See Section 32.2 | Extreme | $+1.0$ |
| Enclosed buildings and other structures | See Table 26.13-1 | High | $+0.55$ |
| | | | $-0.18$ |
| Partially enclosed buildings and other structures | See Table 26.13-1 | High | $+0.55$ |
| | | | $-0.55$ |
| Partially open buildings and other structures | See Table 26.13-1 | Moderate | $+0.18$ |
| | | | $-0.18$ |
| Open buildings and other structures | See Table 26.13-1 | Negligible | $0.00$ |

**Notes:**

1. Plus and minus signs signify pressures acting toward and away from the internal surfaces, respectively.
2. Values of $(GC_{piT})$ shall be used with $q_z$ or $q_h$ as specified.
3. Two cases shall be considered to determine the critical load requirements for the appropriate condition:
   - (a) A positive value of $(GC_{piT})$ applied to all internal surfaces, or
   - (b) A negative value of $(GC_{piT})$ applied to all internal surfaces.

---

**390**                                                **STANDARD ASCE/SEI 7-22**

---

For large-volume buildings with no dominant opening and an exceptionally large volume, the internal pressure coefficient, $R_{iT}(GC_{piT})$ for all heights, shall be multiplied by the reduction factor, $R_{iT}$, as specified in Sections 26.13.1.

## 32.14 TORNADO EXTERNAL PRESSURE COEFFICIENTS

External pressure coefficients shall be determined using the applicable sections of Chapters 27, 29, 30, and 31, and methods of Chapter 31, as permitted in this chapter. For buildings with $h \leq 60$ ft (18 m), refer to Sections 32.15 and 32.16. For buildings with $h > 60$ ft (18 m), refer to Section 32.17.

## 32.15 TORNADO LOADS ON BUILDINGS: MAIN WIND FORCE RESISTING SYSTEM

### 32.15.1 Enclosed, Partially Enclosed, and Partially Open Buildings

Section 27.3.1 shall apply for determination of design tornado loads. For buildings with $h \leq 60$ ft (18 m), the design tornado loads for the main wind force resisting system of enclosed, partially enclosed, and partially open buildings of all heights shall be determined by the following equations, which replace Equations (27.3-1) and (27.3-2):

$$p_T = q_T G_T K_{d7} C_p - q_i (GC_{piT})(R_i/R_T) \quad (32.15-1)$$

and

$$p_T = q_h G_T K_{d7} C_p - q_i (GC_{piT})(R_i/R_T) \quad (32.15-1a)$$

where

- $q_T$ = For external pressure on walls, evaluated at height $z$ above the ground, lb/ft² (N/m²)
- $q_h$ = For external pressure on roofs evaluated at height $h$

---

## Table 32.16-1. Tornado Pressure Coefficient Adjustment Factor for Vertical Walls, $K_{zT}$

| Structure Type | $K_{zT}$ |
|----------------|----------|
| **Buildings** | |
| Negative (-) (Leeward) Pressures on Roofs | |
| Roof slope <sup>a</sup> 10 degrees | 1.1 |
| Components and Cladding | |
| Roof slope <sup>a</sup> 7 degrees | 1.0 |
| Roof slope > 7 degrees | 1.2 |
| | 1.05 |
| Roof slope > 7 degrees | |
| Roof Zone 1' | 1.2 |
| Roof Zone 2' | 1.5 |
| Roof Zone 3' | 1.0 |
| | |
| **Positive Pressures (Downward) Acting on Roofs** | |
| All Zones | 1.2 |
| Roof Overhangs | 1.8 |
| | |
| **Other Structures** | |
| Negative (-) (Uplift) Pressures on Roofing Systems and | |
| Rooftop Solar Panel Systems Parallel to the Roof Surface | |
| Roof Edge Zone | Use values for building C&C |
| Components and Cladding | |
| Negative (-) (Uplift) Pressures on Sides of Bins, Silos, and Tanks | 1.1 |
| Flat Roofs of Bins, Silos, and Tanks (0-10 degrees) | (0-177) |
| All Other Cases | 1.0 |

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures                391**

---

$$p_T = q_h (G_T K_{d7} C_p)(R_i/R_T) \quad (32.15-2)$$

$$p_T = \text{for} \, q_h (G_T K_{d7} C_p + N) \, p_T \quad (32.15-2a)$$

where

- $q_h$ = velocity pressure from Section 32.10.2 evaluated at the nominal of mean $A_f$ of the wall or sign, lb/ft² (N/m²)
- $A_f$ = Gross area of the solid freestanding wall or solid sign considered, ft² (m²)
- $C_p$ = Net pressure coefficient from Sections 32.11, and 32.12

**32.13.4 Parapets** Section 27.3.4 shall apply for determination of tornado loads on parapets. The design tornado loads for the main wind force resisting system of parapets, regardless of height, on buildings of all heights shall be determined in accordance with the following equations, which replace Equations (27.3-3):

$$p_p = q_p G_T K_{d7} C_p \quad (32.15-3)$$

where
- $q_p$ = velocity pressure from Section 32.10.2 evaluated at the top of the parapet
- $G_T$ = Tornado gust-effect factor from Section 32.11
- $K_{d7}$ = Tornado directionality factor from Section 32.6
- $C_p$ = Combined net pressure coefficient from Section 27.3.4
- $(GC_{pT}) = $ = h = 0 (ft) = 1)

**32.13.5 Circular Bins, Silos, and Tanks** Section 27.4.3 shall apply for determination of tornado loads on circular bins, silos, and tanks, as modified in this section. The design tornado pressures, $p_T$, for the main wind force resisting system of circular bins, silos, and tanks shall be determined using Section 27.3.5. The equations for buildings of less than 7 storeys, as modified in this section, The design tornado equations, which replace Equation (28.4-1).

$$p_T = q_h G_T (G_T C_p)(R_i/R_T) \quad (32.15-4)$$

$$p_T = q_h G_T (G_T C_p + N) \, p_T \quad (32.15-4a)$$

where

- $q_h$ = Tornado velocity pressure from Section 32.10.2 evaluated at mean roof height h, lb/ft² (N/m²)
- $G_T$ = Tornado directionality factor from Section 32.8, and $(GC_p)$ from Table 27.4-3

**32.13.5.5 Roofing Solar Panels Parallel to Roof Surface on Buildings of All Heights and Roof Slopes** Section 27.3.5 shall apply for determination of tornado loads on roofing solar panels parallel to the roof surface on buildings of all heights and roof slopes as modified in this section. The design tornado pressures for roofing solar panels parallel to the roof surface on buildings shall be determined in accordance with the following equations:

$$p_T = q_h (GC_{pT})(R_i/R_T) \quad (32.15-5)$$

where
- $q_h$ = For external pressure on walls evaluated at height $z$ above ground, lb/ft² (N/m²)

---

**392**                                                **STANDARD ASCE/SEI 7-22**

---

$$q_h = \text{For external pressures on roofs evaluated at height } h, \text{ lb/ft}^2 \text{ (N/m}^2\text{)}$$

where
- $q_{iT}$ = $q_h$ for positive internal pressure coefficient and $q_i$ for negative pressure coefficient Section 32.10
- $K_{zT}$ = Tornado pressure coefficient adjustment factor from Section 32.16
- $(GC_p)$ = External pressure coefficient and gust-effect factor from Table 30.5-1, and

**32.16.2 Parapets** Section 30.6 shall apply for determination of components and cladding tornado loads on parapets. The design tornado pressures, $p_T$, for components and cladding on parapets regardless of the height of the building on which it is specified shall be determined in accordance with the following equations, which replace Equation (30-3):

$$p_T = q_p K_{zT} K_{dT} (GC_p) - (GC_{piT})(R_i/R_T) \quad (32.17-1)$$

and

$$p_T = q_p K_{zT} K_{dT} (GC_p) + (GC_{piT})(R_i/R_T) \quad (32.17-1a)$$

where
- $q_p$ = Tornado velocity pressure from Section 32.10.2 evaluated at the top of the parapet, lb/ft² (N/m²)
- $K_{zT}$ = Tornado pressure coefficient adjustment factor from Section 32.16
- $(GC_p)$ = External pressure coefficient and gust-effect factor from Section 30.6.4

**32.17.3.1 Horizontal Surfaces of Elevated Buildings** Section 30.7.1 shall apply for determination of components and cladding tornado loads on horizontal surfaces of elevated buildings, as modified in this section. The design tornado pressures, $p_T$, for components and cladding loads on horizontal surfaces of elevated buildings, where wind blows through the open structure and is obstructed by the elevator buildings shall be determined in accordance with the following equations, which replace Equation (30-6):

$$p_T = q_h K_{zT} K_{dT} (GC_p) - (GC_{piT})(R_i/R_T) \quad (32.17-2)$$

and

$$p_T = q_h K_{zT} K_{dT} (GC_p) + (GC_{piT})(R_i/R_T) \quad (32.17-2a)$$

where
- $q_h$ = For external pressures on roofs evaluated at height $h$ above the ground, lb/ft² (N/m²)
- $K_{zT}$ = Tornado velocity pressure exposure factor Section 32.10.2 evaluated

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures                393**

---

$q_h$ = For external pressures on roofs evaluated at height $h$, lb/ft² (N/m²)

$q_i$ = $q_h$ for positive internal pressure coefficient and $q_i$ for negative internal pressure coefficient Section 32.10, lb/ft² (N/m²)

$K_{zT}$ = Tornado pressure coefficient adjustment factor from Section 32.16

$(GC_p)$ = Product of external pressure coefficient and gust-effect factor from Section 30.7, and

$(GC_{piT})$ = Tornado internal pressure coefficient Section 32.13

**32.17.3.2 Roof Overhangs** Section 30.7 shall apply for determination of components and cladding tornado loads on roof overhangs, as modified in this section. The design tornado pressures, $p_T$, for components and cladding on roof overhangs regardless of the height of the building on which is specified shall be determined in accordance with the following equations, which replace Equation (30-7):

$$p_T = q_h K_{zT} K_{dT} (GC_p) - (GC_{piT})(R_i/R_T) \quad (32.17-3)$$

$$p_T = q_h K_{zT} K_{dT} (GC_p) + (GC_{piT})(R_i/R_T) \quad (32.17-3a)$$

where
- $q_h$ = Tornado velocity pressure from Section 32.10.2 evaluated at mean roof height $h$, lb/ft² (N/m²)
- $K_{zT}$ = Tornado pressure coefficient adjustment factor from Section 32.16
- $(GC_p)$ = Tornado pressure coefficient and gust-effect factor from Section 30.7
- $K_{dT}$ = Tornado directionality factor from Section 32.6, and $(GC_{piT})$ = Tornado internal pressure coefficient from Section 32.13

**32.17.1.1 Bottom Horizontal Surfaces of Elevated Buildings** Section 30.7.2 shall apply for determination of components and cladding tornado loads on bottom horizontal surfaces of elevated buildings. For elevated buildings with $h \leq 60$ ft (18.3 m), the design tornado pressures, $p_T$, for components and cladding loads on bottom horizontal surfaces of elevated buildings are as specified in Section 30.7.2.1. For elevated buildings with $h > 60$ ft, the design tornado pressures, $p_T$, for bottom horizontal surfaces of elevated buildings shall be determined in accordance with the following equations, which replace Equations (30-8):

$$p_T = q_h K_{zT} K_{dT} (GC_p)(R_i/R_T) \quad (32.17-4)$$

$$p_T = q_h K_{zT} K_{dT} (GC_p + N_p)(R_i/R_T) \quad (32.17-4a)$$

where
- $q_h$ = Tornado velocity pressure from Section 32.10.2 evaluated at mean roof height $h$, lb/ft² (N/m²)
- $K_{dT}$ = Tornado directionality factor from Section 32.6
- $K_{zT}$ = Tornado pressure coefficient adjustment factor from Section 32.16, and $(GC_p)$ = Tornado pressure coefficient adjustment from Section 30.7.2

**32.17.2 Nonbuilding Structures** Section 30.10 shall apply for determination of components and cladding tornado loads on nonbuilding structures as modified in this section.

**32.17.2.1 Rooftop Solar Panel Nonbuilding Structures** The design tornado pressures on rooftop solar panel nonbuilding structures shall be determined in accordance with the following equations, which replaces Equation (30-13):

$$p_T = q_h K_{zT} K_{dT} (GC_p) - (GC_{piT})(R_i/R_T) \quad (32.17-5)$$

$$p_T = q_h K_{zT} K_{dT} (GC_p) + (GC_{piT})(R_i/R_T) \quad (32.17-5a)$$

where
- $q_h$ = Tornado velocity pressure from Section 32.10.2 evaluated

---

**394**                                                **STANDARD ASCE/SEI 7-22**

---

(1) For roof zones 1 and 2 in Figure 30.12-2, $K_{zT}$ shall equal the Zone 1 value for building roofs from Table 32.14-1, and

(2) For roof zones 3 and 4 in Figure 30.12-2, $K_{zT}$ shall equal the Zone 2 value for building roofs from Table 32.14-1;

$(GC_p)$ = External pressure coefficient from Section 30.10; and

$(GC_{piT})$ = Tornado internal pressure coefficient, as follows:

(1) For internal surface of exterior walls of isolated open-topped circular bins, silos, and tanks, use $(GC_{piT})$ from Section 30.12.3.1

(2) In all other cases, use $(GC_{piT})$ from Section 32.13.

---

## 32.18 TORNADO LOADS: WIND TUNNEL PROCEDURE

The wind tunnel procedure, as described in Chapter 31, is permitted for determination of external pressure coefficients and force coefficients for use with the tornado loading provisions of Sections 32.15 through 32.17. The wind tunnel test shall be performed on an isolated building model (without a proximity model) in a boundary layer wind tunnel for open (Exposure C) terrain.

---

## 32.19 CONSENSUS STANDARDS AND OTHER REFERENCED DOCUMENTS

This section lists the consensus standards and other documents that shall be considered part of this standard to the extent referenced in this chapter.

ASTM E1886, 2019. *Standard Test Method for Performance of Exterior Windows, Curtain Walls, Doors, and Impact Protective Systems Impacted by Missile(s) and Exposed to Cyclic Pressure Differentials.* ASTM International.
    *Cited in:* Section 32.12.3.1

ASTM E1996, 2020. *Standard Specification for Performance of Exterior Windows, Curtain Walls, Doors, and Impact Protective Systems Impacted by Windborne Debris in Hurricanes.* ASTM International.
    *Cited in:* Section 32.12.3.1, C32.12.3.1

ANSI/DASMA 115, 2017. *Standard Method for Testing Sectional Doors, Rolling Doors, and Flexible Doors: Determination of Structural Performance under Missile Impact and Cyclic Wind Pressure.* Door and Access Systems Manufacturers Association International.
    *Cited in:* Section 32.12.3.1

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures                395**

---

# Page 458

This page intentionally left blank


---

# APPENDIX A
# RESERVED FOR FUTURE PROVISIONS

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** | Page 397

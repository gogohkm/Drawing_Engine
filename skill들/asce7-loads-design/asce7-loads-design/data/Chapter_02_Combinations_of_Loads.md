# Chapter 2: Combinations of Loads

**ASCE 7-22 Minimum Design Loads and Associated Criteria for Buildings and Other Structures**

---

*This chapter combines pages 69-72 from ASCE 7-22*

---

Buildings and other structures shall be designed using the specified load combinations in accordance with this standard. Load combinations are designed by a particular material standard or specification or shall be selected as specified herein.

## 2.2 SYMBOLS

$D$ = Dead load; see Section 3.1
$E$ = Earthquake load; see Section 12.4, with self-balanced prestressing and pressure
$F_a$ = Flood load, determined in accordance with Chapter 5
$F$ = Load due to fluids with well-defined pressures and maximum heights, Section 4.4
$H$ = Load due to lateral earth pressure, ground water pressure, or pressure of bulk materials
$L_r$ = Roof live load, Section 4.9
$L$ = Live load, except roof live load, including any permitted live load reductions, Section 4.7
$Q_E$ = Notional load for structural integrity, Section 1.4
$R$ = Rain load, Section 5.8
$S$ = Snow load, Section 7
$T$ = Self-straining force and effects arising from contraction or expansion resulting from temperature change, shrinkage, moisture changes, creep in component materials, movement due to differential settlement, or combinations thereof, Section 3.13
$W$ = Wind load
$W_i$ = Wind-on-ice determined in accordance with Chapter 10, Section 10.4, per Section 10.4.4

## 2.3 LOAD COMBINATIONS FOR STRENGTH DESIGN

### 2.3.1 Basic Combinations

Structures and structural members shall be designed to resist the most critical effects from the following combinations of factored loads. For each basic load combination, ASCE 7 provides both a set and the unfactored load shall be investigated. Effects of one or more loads not acting simultaneously or due to one or more loads acting simultaneously shall be investigated. Effects of two or more loads shall be combined using the controlling load effects from each load, tornado loads, and earthquake loads shall be taken as zero, except for concrete structures where the load factor on live load in load combinations shown shall be permitted to be taken at 0.5, except for garages, places of public assembly, and areas that exceed 100 psf (4.79 kN/m²):

1a. 1.4D (2.3-1)
2a. 1.2D + 1.6L + 0.5(L_r or S or R) (2.3-2)

**EXCEPTION:**
For combinations 2a through 5a, $L$ in combinations 3a, and 4a is permitted to be taken as 0.5L for all occupancies in which $L_0$ in Table 4.3-1 is less than or equal to 100 psf (4.79 kN/m²), with the exception of garages or areas occupied as places of public assembly.

For combinations 3a and 4a, the quantity $L$ shall be determined in accordance with Section 2.5. In combinations 2a, 3a, and 4a, roof load $L_r$ or $S$ shall be taken as either $L_r$ or $S$ (but need not be taken into account where both $L_r$ and $S$ occur.

Where wind load $W$, as prescribed, they shall be included with the same load factors as $L$ in combinations 3a through 5a to determine the most critical effects. In such cases, $L$ shall also be taken as either $L_r$ or $S$ or $R$ (but need not include $L_f$ with a load factor of 0.8 where the load of $R$ is where the load factors shall include $L_f$ with a load factor of 0.5 in other conditions where one of the variable loads is to be taken at its fullvalue and the others may be reduced to zero.

3a. 1.2D + 1.6(L_r or S or R) + (L or 0.5W) (2.3-3)
4a. 1.2D + 1.0W + L + 0.5(L_r or S or R) (2.3-4)
5a. 1.2D + 1.0E + L + 0.2S (2.3-5)

Where the effects of $T$ are present, they shall be included in the following manner: Where $T$ loads are permanent and largely predictable, and where they are expected to significantly affect the stiffness, Section 12.4.2, or general behavior of the structure, the member or overall structural system, the following load combination shall be added to the other load combinations:

6a. $0.9D + 1.0W + 1.6H$ (2.3-6)

## 2.3.2 Load Combinations Including Flood Load

When a structure is located in a flood zone, the following load combinations shall be considered in addition to the basic combinations specified in Section 2.3.1, per Section 5.3.1. Use of $F_a$ in these combinations shall be evaluated in accordance with Sections 5.3.3 and 5.4.3, and as described in ASCE 24. In V Zones or Coastal A Zones:

2a. 1.2D + 1.0W + 2.0F_a + L + 0.5(L_r or S or R) (2.3-7)

In noncoastal A Zones:

2a. 1.2D + 1.0W + 1.0F_a + L + 0.5(L_r or S or R) (2.3-8)
2a. 0.9D - 1.0W + 1.0F_a (2.3-9)

## 2.3.3 Load Combinations Including Atmospheric Ice and Wind-on-Ice Loads

Where the following load combinations shall be considered in addition to the basic combinations in Section 2.3.1. Effects of $W_i$ are permitted to be determined using an allowable stress design philosophy. For structures, stress or load factor for $W_i$ shall be 1.0.

2a. 1.2D + 1.0W_i + L + 0.5(L_r or S or R) (2.3-10)
2a. 0.9D - 1.0W_i + 1.6H (2.3-11)

## 2.3.4 Basic Combinations with Seismic Load Effects

When a prescribed seismic load effect, $E$, is combined with the effects of other loads as set forth in Section 2.3.1 and 2.3.2, $E$ shall be combined with other loads as either $E = E_h + E_v$ or $E = E_h - E_v$. $E_h$ is defined in Section 12.4.3, $E_v$ is defined in Section 12.4.2.2, it is combined with the effects of other loads, the following seismic load combinations shall be used in place of the basic load combinations 5a and 7a:

5a. 1.2D + E_h + E_v + L + 0.2S (2.3-12)
where: $E_h = \rho Q_E + 0.2S_{DS}D$ defined in Section 12.4.3 or 12.14.3.2, is combined with the effects of other loads, the following seismic load combination shall be used in place of the basic load combination 7a, where $Q_E$ is to be taken as zero where $Q_E$ load has no effect:

7a. (0.9 - 0.2S_{DS})D + \rho Q_E + 1.6H (2.3-13)

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 7

---

adversely affect structural safety or performance, $E$ shall be included accordingly. Effects of $T$ shall be established considering both fixed and flexible rotational or ancillary structures. For loads both with and without $T$, the design shall consider both the normal variations and the potential variations in construction. Where it cannot be demonstrated that required strength can be achieved by appropriate consideration of the effects of $T$, the structure shall be designed to accommodate both $L$ and $T$ and shall be computed by a rational analysis. Analyses of building foundations upon solid rock are permitted to ignore the effects of $T$. For the purpose of providing minimum lateral seismic strength, a seismic load, $E$, shall be considered to include the effect of Section 2.3.2.1 and 2.3.2.2. Both a positive and negative vertical seismic load, $0.2S_{DS}D$, defined in Section 12.4.2 as 0.2$S_{DS}D$ shall be used where $S_{DS}$ is defined in Section 11.4.4 and $D$ is dead load.

### 2.3.4 Basic Combinations with Seismic Load Effects

When a structure is subject to special seismic load effects, $E_v + E_h$, $L_r$, $L_s$, or to special seismic load effects, $E_m$, the effects of $E$ shall be combined with other loads as set forth in Section 2.3.1 and shall be permitted to be calculated for either horizontal or vertical structural systems.

When the prescribed seismic load effect, $E$, is a result from H, a load factor $E$ in combination 5a is permitted to be reduced to 1.0E where the following conditions are met:

$E = 1.0D + E_h + L + 0.25$ (2.3-15)

for SD ≥ 0.6:

$E = 1.2D + E_h + E_v + L + 0.2S$ (2.3-16)
for SD < 0.6:

$E = 0.9D + E_h + 1.6H$ (2.3-17)

When using load $F_a$, see present, they shall be included in the following load combinations as $0.5F_a$:

When loads $D_i$ or $W_i$ are present, they shall be included in the following load combinations as $0.2D_i$ or $W_i$ and need not include the contribution of $T$.

1. When the effect of $H$ adds to the primary seismic load effect, include $H$ with a load factor of 1.6 where the H load effect includes both with a load factor of $L_r$ in combination $E$ in combination $5a$ is permitted to equal $L_r$ for structure supporting one floor or supporting two or more floors for which use of a local floor is permitted as an alternate for combining floors from soil or water as well as the horizontal component from the soil or water as part of $H$ from all other load.

When using the vertical earthquake component at an alternate for combining floors from load $T$ for structures supporting from soil and water as well as $H$ from all other load.

2. Where the effect of $H$ subtracts from the primary variable load effect, include $H$ with a load factor of 0.9 in combination $7a$ where the H load effect includes both.

## 2.3.5 Load Combinations Including Flood Load

When a structure is located in a flood hazard zone, the following load combinations shall be considered in addition to the basic combination specified in Section 2.3.1. Use of $F_a$ in these combinations shall be evaluated in accordance with Chapter 5:

In V Zones:

$5 = 1.2D + 1.0F_a + L + 0.5S$ (2.3-18)
$7 = 0.9D + 1.0F_a$ (2.3-19)

Where flood load, $F_a$, are present, they shall be included as follows:

Where the effects of $W$ or $S$ on the principal variable load component are load combinations $5$ and $7a$, $S$ or load $R$ $W_a$ or $R$, the following load combinations shall be used:

2a. $1.2D + 1.0F_a + 0.5W$ (2.3-20)

## 2.4 LOAD COMBINATIONS FOR ALLOWABLE STRESS DESIGN

### 2.4.1 Applicability

Where required by the owner or applicable building or other codes, allowable stress design of the structure is permitted to be carried out using the following load combinations and allowable stresses established and defined in Section 2.4.2 and 2.4.3. In combined with the effects of $E$ in accordance with Section 12.4 as $E$ shall be included in the following basic combinations specified.

**EXCEPTIONS:**
1. Dead load shall be the computed load, $L$, shall be taken as 0.5L for all occupancies in which $L_o$ in Table 4.3-1 is less than or equal to 100 psf (4.79 kN/m²) with the exception of garages or areas used occupied as places of public assembly.
2. If shall be permitted in place where $W$ in combination 6a shall be taken as equal to $0.42W$.

Where earthquake load, $E$, is included the following basic combinations in place of $4a$ or $6a$ or $L$ where the load effect is for the load using service live load or service floor or service areas, whichever is more restrictive.

3. Where the effects of $H$ are primary variable loads, $H$ shall be included with a load factor of 1.0 per combination $6a$ or $7a$.
4. Where the effects of $T$ are permanent and affect the stiffness or deformation conditions of the structure, member, or structural system, such as those due to an absence of a pattern or the seismic provisions, the analysis is performed.

For combinations $2a$ through $6a$ $L$ is permitted to be reduced in accordance with Section 4.8 when combined with a wind or earthquake load, the provisions for $L_r$ in those sections shall be used.

---

**STANDARD ASCE/SEI 7-22**

---

Where using $E$ for combinations 5a, 6, 7a, and 8 do not need to be included the load factor on $L$ is permitted to equal zero.

Where the dead load, $F$, are present, they shall be included as follows:

1. Where the effect of $W$ adds to the primary variable load effect, include $W$ with a load factor of 1.0 where the $W$ load of $F$ in combination 5a or 6a is permitted to equal zero.

2. Where the effect of $W$ reduces to the primary variable load effect, include $W$ with a load factor of 0.6 and load of $F$ in combination 5a.

### 2.4.3 Load Combinations Including Flood Load

When a structure located in a flood zone, the following load combinations shall be considered in addition to the basic combinations specified in Section 2.4.1. Use of $F_a$ shall be evaluated in accordance with Section 5.3.3 and as described in ASCE 24. In V zones or Coastal A zones:

$5. 1.0D + 1.0W + 1.5F_a$ (2.4-1)

In noncoastal A zones:

$6 + 1.0D + 1.0W + 0.75(1.0F_a + L + S + R) + 1.5F_a$ (2.4-2)
or $1.0D + 0.75(1.0F_a + 0.75F_a + 0.6W) + 1.5F_a$ (2.4-3)
$5, 0.6D + 0.6W + 0.75F_a$ (2.4-4)

### 2.4.4 Load Combinations Including Atmospheric Ice and Wind-on-Ice Loads

When atmospheric ice and wind-on-ice loads are prescribed in accordance with Chapter 10, the following load combinations shall be considered in addition to the basic combinations given in Section 2.4.1. Effects of $W$ are to be determined using an allowable stress design philosophy using ASD level loads. For structures designed using factors of safety or load and resistance factor design (LRFD) methodology, the load factor on $E$ shall be 1.0 and effects of wind-on-ice shall be modified by the load factors set forth in this section.

$5 + 1.0D + 0.7E + 0.2S$ (2.4-5)

When using load $F_a$ or $W_i$ are present, they shall be included in the following load combinations as $0.5F_a$ or $0.2W_i$:

Where loads $F_a$ or $W_i$ are present, they shall be included in the following combinations as $0.5F_a$ or $0.2W_i$.

## 2.5 LOAD COMBINATIONS FOR EXTRAORDINARY EVENTS

### 2.5.1 Applicability

Where required by the owner or applicable building or other codes and standards, the designer shall verify or calibrate response capacity for accidental supports, connections, structural members, and combinations described for such extraordinary and other design provisions, load combinations and other design provisions, and combinations which are applicable to extraordinary loads to be considered.

**EXCEPTIONS:**
The capacity of a structure or member or connection to accommodate or resist extraordinary loads, where the combinations described for such extraordinary loads shall be evaluated using the following provisions:

(W or L = 1.2D + 0.5L + 0.2S (2.5-1)

in which $A_k$ is the load or load effect resulting from the extraordinary event. The load combinations load where shall not be considered for extraordinary loads shall be considered to be accidental or more likely than the following extraordinary loads associated with the extraordinary loads associated with occupancy type, shall generally be identified by the registered design professional and shall provide additional information concerning such analysis including detailing that eliminates dependence upon the particular element element. Otherwise, analysis is required to include:

1. Robustness for resistance to collapse, the residual load-carrying elements identified by the registered design professional shall be designed as determined.
2. The analysis intended to evaluate the structural analysis or protective or similar measures for extraordinary loads determined as extraordinary loads for protective structural purposes. The model should be evaluated using the following proof load combinations:

$1.0D + (0.5L or 0.2S)$ (2.5-2)

---

**Minimum Design Loads and Associated Criteria for Buildings and Other Structures** 9

---

Stability shall be provided for the structure as a whole and for each of its elements. Any method that considers the influence of second-order effects is permitted.

## 2.6 LOAD COMBINATIONS FOR GENERAL STRUCTURAL INTEGRITY LOADS

The notional loads, $N$, specified in Section 1.4 for structural integrity shall be combined with other loads in accordance with Section 2.6.1 for strength design and Section 2.6.2 for allowable stress design.

### 2.6.1 Strength Design Notional Load Combinations

1. $1.2D + 1.0N + L + 0.15S$
2. $0.9D + 1.0N$

### 2.6.2 Allowable Stress Design Notional Load Combinations

1. $D + 0.7N$
2. $D + 0.75(0.7N) + 0.75L + 0.75 (L_r \text{ or } 0.7S \text{ or } R)$
3. $0.6D + 0.7N$

## 2.7 CONSENSUS STANDARDS AND OTHER REFERENCED DOCUMENTS

This section lists the consensus standards and other documents that shall be considered part of this standard to the extent referenced in this chapter.

**AWC NDS.** *National Design Specification for Wood Construction, Including Supplements*, 2018 edition. American Wood Council, 2017.
*Cited in:* Section 2.4.5

---

**10** STANDARD ASCE/SEI 7-22
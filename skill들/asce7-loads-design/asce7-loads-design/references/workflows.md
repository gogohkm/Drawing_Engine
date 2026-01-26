# ASCE 7-22 Design Workflows

## Workflow 1: Load Combination Selection

**Goal:** Determine all applicable load combinations for design

**Steps:**
1. List all loads present on structure:
   - D (always required)
   - L, Lr (floor vs roof)
   - S (if snow region)
   - R (rain loads)
   - W (wind loads)
   - E (if seismic zone)
   - H (earth pressure)
   - Fa (if flood zone)
   - Wi (if ice region)

2. Choose design method:
   - LRFD (modern codes, steel/concrete) → Section 2.3
   - ASD (wood, masonry, older codes) → Section 2.4

3. Generate basic combinations:
   - Run `load_combinator.py --design [LRFD/ASD] --loads D,L,W,...`
   - Or manually list from Section 2.3.1 or 2.4.1

4. Add special combinations if applicable:
   - Seismic enhanced (if SDC D-F): Section 2.3.4
   - Flood (if in flood zone): Section 2.3.2 or 2.4.3
   - Ice (if ice region): Section 2.3.3 or 2.4.4

5. Check each combination for:
   - Both + and - directions for W and E
   - Uplift cases (0.9D or 0.6D)
   - Load reductions where permitted

**Output:** Complete list of load combinations for analysis

---

## Workflow 2: Seismic Base Shear Calculation (ELF Method)

**Goal:** Calculate seismic base shear using Equivalent Lateral Force method

**Prerequisites:**
- Building meets ELF applicability (Section 12.6, Table 12.6-1)
- No significant irregularities requiring modal analysis

**Steps:**

### Step 1: Building Classification (Chapter 1)
- Determine Risk Category from Table 1.5-1
- Get Ie from Table 1.5-2

### Step 2: Site Seismic Parameters (Chapter 11)
- Get site location (latitude, longitude)
- Determine SS and S1 (from ASCE 7 Hazard Tool or maps)
- Classify site per Chapter 20 → Site Class (A-F)
- Get site coefficients Fa and Fv from Tables 11.4-1, 11.4-2
- Calculate SMS = Fa × SS and SM1 = Fv × S1
- Calculate SDS = (2/3) × SMS and SD1 = (2/3) × SM1
- Determine SDC from Tables 11.6-1 and 11.6-2

### Step 3: Structural System Selection (Chapter 12)
- Choose structural system from Table 12.2-1
- Get R, Ω0, Cd values
- Verify system permitted for SDC (Table 12.2-1)
- Check height limits

### Step 4: Calculate Approximate Period (Section 12.8.2)
- Use Eq. 12.8-7: Ta = Ct × hn^x
- Get Ct and x from Table 12.8-2 based on system type
- hn = height from base to roof level

### Step 5: Calculate Seismic Response Coefficient Cs (Section 12.8.1.1)
- Calculate Cs = SDS / (R/Ie)  [Eq. 12.8-2]
- Check maximum: Cs,max = SD1 / [T(R/Ie)]  [Eq. 12.8-3]
- Check minimum: Cs,min = 0.044 × SDS × Ie ≥ 0.01  [Eq. 12.8-5]
- For S1 ≥ 0.6g, also check: Cs,min = 0.5S1/(R/Ie)  [Eq. 12.8-6]
- Use controlling Cs value

### Step 6: Calculate Effective Seismic Weight W (Section 12.7.2)
- W = Total dead load + applicable portions of other loads
- Include: full dead load, storage live load, partitions, etc.
- Typically: W ≈ Total DL + 0.25 × LL (snow) in snow regions

### Step 7: Calculate Base Shear V (Section 12.8.1)
- V = Cs × W  [Eq. 12.8-1]

### Step 8: Distribute Forces Vertically (Section 12.8.3)
- Calculate Fx at each level using Eq. 12.8-11, 12.8-12
- k = 1 for T ≤ 0.5 sec, k = 2 for T ≥ 2.5 sec, interpolate between

### Step 9: Check Story Drift (Section 12.12)
- Calculate Δ using Eq. 12.8-15
- Check Δ ≤ Δa from Table 12.12-1

**Output:** V (base shear), Fx (story forces), drift check

---

## Workflow 3: Wind Pressure Calculation (Directional Procedure)

**Goal:** Calculate design wind pressure on MWFRS

**Method:** Chapter 27 - Directional Procedure for Main Wind Force Resisting System

**Steps:**

### Step 1: Building Classification
- Risk Category from Table 1.5-1
- Check applicability (Section 27.1)
  - Regular shaped building
  - No unusual response characteristics

### Step 2: Basic Wind Speed V (Section 26.5.1)
- Get V from ASCE 7 Hazard Tool or maps
- 3-second gust speed at 33 ft in Exposure C

### Step 3: Exposure Category (Section 26.7)
- Examine terrain in upwind direction
- Exposure B: Urban/suburban (many buildings)
- Exposure C: Open terrain (most common)
- Exposure D: Flat, unobstructed (water, desert)

### Step 4: Velocity Pressure qz (Section 26.10)
- Get Kd from Table 26.6-1 (usually 0.85)
- Get Kz from Table 26.10-1 (varies with height and exposure)
- Calculate Kzt per Section 26.8 (usually 1.0 for flat terrain)
- Get Ke from Table 26.9-1 (usually 1.0 at sea level)
- Calculate: qz = 0.00256 × Kz × Kzt × Kd × Ke × V²  [Eq. 26.10-1]

### Step 5: Gust Effect Factor G (Section 26.11)
- Rigid structure (n1 ≥ 1 Hz): G = 0.85
- Flexible structure (n1 < 1 Hz): Calculate Gf per Section 26.11.3

### Step 6: Enclosure Classification (Section 26.12)
- Enclosed, Partially Enclosed, or Open
- Determines (GCpi) from Table 26.13-1

### Step 7: External Pressure Coefficient Cp (Section 27.4)
- Get Cp from Figure 27.4-1 based on L/B ratio and wall location

### Step 8: Design Wind Pressure p (Section 27.4)
- p = qz × G × Cp - qi × (GCpi)  [Eq. 27.4-1]
- Calculate for windward wall, leeward wall, sidewalls, roof

### Step 9: Apply Load Cases (Section 27.4.5)
- Load Case 1: Full design pressure all surfaces
- Load Case 2: 75% pressure with ±5% torsion
- Design for worst case

**Output:** Design wind pressures for each surface

---

## Workflow 4: Snow Load Calculation

**Goal:** Determine design snow load on roof

**Steps:**

### Step 1: Ground Snow Load pg (Section 7.2)
- Get pg from ASCE 7 Hazard Tool or Figure 7.2-1
- Or use site-specific data per Section 7.2

### Step 2: Flat Roof Snow Load pf (Section 7.3)
- Get Ce from Table 7.3-1 (exposure factor)
  - Terrain B (sheltered): Ce = 1.0 to 1.2
  - Terrain C (partial exposure): Ce = 0.9 to 1.0
  - Terrain D (fully exposed): Ce = 0.7 to 0.9
- Get Ct from Table 7.3-2 (thermal factor)
  - Heated: Ct = 1.0
  - Unheated: Ct = 1.1 to 1.2
- Get Is from Table 1.5-2 (importance factor)
- Calculate: pf = 0.7 × Ce × Ct × Is × pg  [Eq. 7.3-1]
- Check minimum: pf,min = Is × pg (if pg ≤ 20 psf) [Eq. 7.3-4]

### Step 3: Sloped Roof Snow Load ps (Section 7.4)
- Get Cs from Figure 7.4-1 based on roof slope and surface
  - Warm roof (Ct ≥ 1.0): Cs varies with slope
  - Cold roof (Ct < 1.0): Higher Cs values
  - Slippery surface: Lower Cs (more snow slides off)
- Calculate: ps = Cs × pf  [Eq. 7.4-1]

### Step 4: Unbalanced Snow Load (Section 7.6)
- For sloped roofs: 0.3pf on windward, ps on leeward
- For curved roofs: Special provisions

### Step 5: Snow Drift (Sections 7.7-7.9)
- Leeward drift (Section 7.7): At roof step
  - Calculate hd using Eq. 7.7-1, 7.7-2
  - pd = hd × γ (snow density)
- Windward drift (Section 7.8): On lower roof
- Roof projection drift (Section 7.9)

### Step 6: Rain-on-Snow (Section 7.10)
- If pg ≤ 20 psf: Add 5 psf rain-on-snow surcharge

### Step 7: Sliding Snow (Section 7.11)
- Calculate load from snow sliding onto lower roof

**Output:** Design snow loads (balanced, unbalanced, drift)

---

## Workflow 5: Risk Category and SDC Determination

**Goal:** Classify building and determine seismic design requirements

**Part A: Risk Category (Chapter 1)**

1. Identify building use/occupancy
2. Check Table 1.5-1:
   - **Category I**: Agricultural, minor storage (rare)
   - **Category II**: Standard (offices, residential, retail) ← Most common
   - **Category III**: Schools, jails, assembly >300 people, substantial hazard
   - **Category IV**: Hospitals, fire/police stations, emergency operations centers

3. Special considerations:
   - Number of occupants (>5,000 → may upgrade to III)
   - Hazardous materials (may require III or IV)
   - Essential facility designation (IV)

**Part B: Seismic Design Category (Chapter 11)**

1. Obtain seismic parameters:
   - SDS (short-period design spectral acceleration)
   - SD1 (1-second design spectral acceleration)
   - From ASCE 7 Hazard Tool or calculate per Section 11.4

2. Use Table 11.6-1 (based on SDS):
   - Input: Risk Category (I/II/III/IV) and SDS value
   - Output: SDC based on SDS

3. Use Table 11.6-2 (based on SD1):
   - Input: Risk Category (I/II/III/IV) and SD1 value
   - Output: SDC based on SD1

4. Controlling SDC:
   - Take the MORE CONSERVATIVE (higher) of the two SDC values
   - SDC progression: A < B < C < D < E < F

5. Design requirements by SDC:
   - SDC A: Minimal seismic provisions
   - SDC B, C: Moderate seismic provisions
   - SDC D, E, F: Comprehensive seismic provisions

**Output:** Risk Category and Seismic Design Category

---

## Workflow 6: Selecting Appropriate Analysis Method

**Decision Tree:**

### For Seismic Analysis:

```
Start → Check building height and SDC
  ↓
Height ≤ limits in Table 12.6-1? → YES → Check irregularities
  ↓                                      ↓
  NO                                Tables 12.3-1, 12.3-2
  ↓                                      ↓
Must use Modal Response            Significant irregularities? → NO → Use ELF (Section 12.8)
Spectrum (Section 12.9)                 ↓                              ↓
                                       YES                      Simplest method
                                        ↓
                                  Check if irregularity
                                  requires modal analysis
                                        ↓
                               YES → Use Modal (12.9)
                               NO → Can use ELF (12.8)
```

### For Wind Analysis:

```
Start → Check building characteristics
  ↓
Simple low-rise building? → YES → Method 1: Simplified (Ch 26.4)
  ↓                               (Fastest, limited applicability)
  NO
  ↓
Regular building,                → Method 2: Analytical Directional (Ch 27)
standard shape?  → YES            (Most common, general use)
  ↓
  NO
  ↓
Complex geometry,              → Method 3: Wind Tunnel (Ch 31)
unusual response?  → YES         (Most accurate, expensive)
  ↓
  NO
  ↓
Regional climatic data?  → YES → Method 4: Directional with Regional Data
                                  (Specialized)
```

**Output:** Appropriate analysis method for project

---

## Common Calculation Sequences

### Sequence 1: New Building - Full Load Determination

1. Classify building (Risk Category)
2. Determine dead loads (Chapter 3)
3. Determine live loads (Chapter 4)
4. Determine snow loads if applicable (Chapter 7)
5. Determine wind loads (Chapters 26-27)
6. Determine seismic loads (Chapters 11-12)
7. Generate load combinations (Chapter 2)
8. Design structural members (material codes: AISC, ACI, etc.)

### Sequence 2: Seismic Upgrade - Evaluate Existing

1. Classify building (Risk Category)
2. Determine SDC for location
3. Identify structural system and get R value
4. Calculate seismic forces (Chapter 12)
5. Compare to current capacity
6. Design upgrades if needed

### Sequence 3: Wind Load Only - Simple Structure

1. Get basic wind speed V
2. Determine exposure category
3. Calculate velocity pressure qz
4. Apply pressure coefficients
5. Generate wind load combinations with D, L
6. Design for wind effects

---

Reference: ASCE 7-22 Chapters 1, 2, 7, 11, 12, 26, 27

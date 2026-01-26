---
name: "asce7-loads-design"
description: "ASCE 7-22 loads and load combinations skill for structural design. Covers wind, seismic, snow, and other environmental loads per US building standards."
---

# ASCE 7-22 Loads and Design Skill

## Purpose

This skill provides comprehensive access to ASCE 7-22 (Minimum Design Loads and Associated Criteria for Buildings and Other Structures), the authoritative US standard for determining structural loads.

**Critical Distinction:** ASCE 7 is a LOADS standard, not a material design standard. It tells you WHAT loads to apply, not HOW to design members.

## When to Use This Skill

Trigger this skill when users ask about:
- Load combinations (LRFD, ASD)
- Wind loads, wind speed, exposure categories
- Seismic loads, base shear, response spectra
- Snow loads, ground snow, snow drift
- Load calculations per ASCE 7
- Risk Categories, Seismic Design Categories
- Environmental loads (tsunami, flood, ice, rain)

**Do NOT use for:**
- Steel member design → Use AISC 360
- Concrete member design → Use ACI 318
- Material properties, connection design

## Document Structure

### Available Chapters - Complete ASCE 7-22 Coverage

**Chapter 1-5: General & Basic Loads**
- **Chapter 1**: General (31 KB)
  - Scope, definitions, risk categories, load factors
  - File: `data/Chapter_01_General.md`

- **Chapter 2**: Combinations of Loads (16 KB)
  - LRFD and ASD combinations, seismic/flood/ice combinations
  - File: `data/Chapter_02_Combinations_of_Loads.md`

- **Chapter 3**: Dead Loads, Soil Loads, and Hydrostatic Pressure (8 KB)
  - Dead load determination, soil lateral loads
  - File: `data/Chapter_03_Dead_Loads_Soil_Loads_Hydrostatic_Pressure.md`

- **Chapter 4**: Live Loads (26 KB)
  - Floor live loads, roof live loads, reduction factors
  - File: `data/Chapter_04_Live_Loads.md`

- **Chapter 5**: Flood Loads (10 KB)
  - Flood zones, flood loads, breakaway walls
  - File: `data/Chapter_05_Flood_Loads.md`

**Chapter 6-10: Environmental Loads**
- **Chapter 6**: Tsunami Loads and Effects (98 KB)
  - Tsunami risk categories, inundation depths, design procedures
  - File: `data/Chapter_06_Tsunami_Loads_and_Effects.md`

- **Chapter 7**: Snow Loads (24 KB)
  - Ground snow load, flat roof snow, snow drift, rain-on-snow
  - File: `data/Chapter_07_Snow_Loads.md`

- **Chapter 10**: Ice Loads - Atmospheric Icing (12 KB)
  - Freezing rain, in-cloud icing, wind-on-ice
  - File: `data/Chapter_10_Ice_Loads_Atmospheric_Icing.md`

**Chapter 11-23: Seismic Design**
- **Chapter 11**: Seismic Design Criteria (64 KB)
  - Site class, spectral response, SDC determination
  - File: `data/Chapter_11_Seismic_Design_Criteria.md`

- **Chapter 12**: Seismic Design Requirements for Building Structures (177 KB)
  - ELF method, base shear, drift limits, irregularities
  - File: `data/Chapter_12_Seismic_Design_Requirements_Building.md`

- **Chapter 13**: Seismic Design Requirements for Nonstructural Components (84 KB)
  - Architectural, mechanical, electrical components
  - File: `data/Chapter_13_Seismic_Design_Requirements_Nonstructural.md`

- **Chapter 14**: Material-Specific Seismic Design and Detailing Requirements (11 KB)
  - Steel, concrete, masonry, wood seismic detailing
  - File: `data/Chapter_14_Material_Specific_Seismic_Design.md`

- **Chapter 15**: Seismic Design Requirements for Nonbuilding Structures (43 KB)
  - Tanks, vessels, chimneys, towers, signs
  - File: `data/Chapter_15_Seismic_Design_Requirements_Nonbuilding.md`

- **Chapter 16**: Nonlinear Response History Analysis (23 KB)
  - Ground motion selection, modeling, acceptance criteria
  - File: `data/Chapter_16_Nonlinear_Response_History_Analysis.md`

- **Chapter 17**: Seismic Design Requirements for Seismically Isolated Structures (64 KB)
  - Base isolation systems, analysis procedures
  - File: `data/Chapter_17_Seismic_Design_Seismically_Isolated.md`

- **Chapter 18**: Seismic Design Requirements for Structures with Damping Systems (81 KB)
  - Passive, active, and hybrid damping systems
  - File: `data/Chapter_18_Seismic_Design_Structures_Damping_Systems.md`

- **Chapter 19**: Soil-Structure Interaction for Seismic Design (19 KB)
  - Foundation damping, kinematic interaction
  - File: `data/Chapter_19_Soil_Structure_Interaction_Seismic.md`

- **Chapter 20**: Site Classification Procedure for Seismic Design (7 KB)
  - Site class A through F determination
  - File: `data/Chapter_20_Site_Classification_Procedure_Seismic.md`

- **Chapter 21**: Site-Specific Ground Motion Procedures for Seismic Design (3 KB)
  - PSHA, DSHA procedures
  - File: `data/Chapter_21_Site_Specific_Ground_Motion_Procedures.md`

- **Chapter 22**: Seismic Ground Motion and Long-Period Transition Maps (32 KB)
  - Spectral response maps, long-period maps
  - File: `data/Chapter_22_Seismic_Ground_Motion_Maps.md`

- **Chapter 23**: Seismic Design Reference Documents (18 KB)
  - Referenced standards and documents
  - File: `data/Chapter_23_Seismic_Design_Reference_Documents.md`

**Chapter 24-25: Reserved**
- **Chapter 24**: Reserved for Future Provisions
  - File: `data/Chapter_24_Reserved_for_Future_Provisions.md`

- **Chapter 25**: Reserved for Future Provisions
  - File: `data/Chapter_25_Reserved_for_Future_Provisions.md`

**Chapter 26-32: Wind & Tornado Loads**
- **Chapter 26**: Wind Loads - General Requirements (58 KB)
  - Wind speed, exposure, velocity pressure, gust factor
  - File: `data/Chapter_26_Wind_Loads_General_Requirements.md`

- **Chapter 27**: Wind Loads on Buildings - MWFRS Directional Procedure (37 KB)
  - Main Wind Force Resisting System design
  - File: `data/Chapter_27_Wind_Loads_MWFRS_Directional.md`

- **Chapter 28**: Wind Loads on Buildings - MWFRS Envelope Procedure (18 KB)
  - Simplified envelope procedure
  - File: `data/Chapter_28_Wind_Loads_MWFRS_Envelope.md`

- **Chapter 29**: Wind Loads on Building Appurtenances and Other Structures (55 KB)
  - Rooftop equipment, tanks, signs, lattice structures
  - File: `data/Chapter_29_Wind_Loads_Building_Appurtenances.md`

- **Chapter 30**: Wind Loads - Components and Cladding (114 KB)
  - Cladding pressures, roof systems, wall systems
  - File: `data/Chapter_30_Wind_Loads_Components_and_Cladding.md`

- **Chapter 31**: Wind Tunnel Procedure (18 KB)
  - Wind tunnel testing requirements
  - File: `data/Chapter_31_Wind_Tunnel_Procedure.md`

- **Chapter 32**: Tornado Loads (81 KB)
  - Tornado wind speeds, missile impact, design procedures
  - File: `data/Chapter_32_Tornado_Loads.md`

**Total Coverage:** 30 chapters, ~1.2 MB of content

### Automation Scripts

Located in `scripts/` directory:

1. **`smart_search.py`** - Category-aware chapter search
   - Maps keywords to relevant chapters
   - Usage: `python3 smart_search.py "seismic base shear"`

2. **`formula_finder.py`** - Extract formulas with context
   - Finds equations and shows variables
   - Usage: `python3 formula_finder.py "V =" Chapter_12...md`

3. **`load_combinator.py`** - Generate applicable load combinations
   - LRFD and ASD combinations
   - Usage: `python3 load_combinator.py --design LRFD --loads D,L,W,S`

### Reference Files

Located in `references/` directory (to be created):
- `chapter-structure.md` - Navigation guide
- `load-combinations-index.md` - Quick reference for Ch 2
- `formulas-index.md` - 50+ key formulas
- `glossary.md` - Technical terms
- `symbols.md` - Mathematical notation
- `workflows.md` - Design workflows
- `risk-categories-guide.md` - Risk Category I-IV
- `seismic-categories-guide.md` - SDC A-F
- `wind-exposure-guide.md` - Exposure B/C/D

---

## Workflow Types

### 1. Formula Query Workflow

**Trigger:** User asks for a specific formula or equation

**Process:**
1. Identify the load type (wind, seismic, snow, etc.)
2. Use `smart_search.py` to find relevant chapter
3. Use `formula_finder.py` to extract formula with context
4. Present formula with:
   - Equation number (e.g., "Eq. 12.8-1")
   - Variable definitions
   - Context (when to use, limitations)
   - Units

**Example:**
```
User: "Show me the seismic base shear formula"

Response:
The seismic base shear is calculated using Equation 12.8-1:

V = CsW

Where:
- V = Seismic base shear
- Cs = Seismic response coefficient (Eq. 12.8-2 through 12.8-6)
- W = Effective seismic weight

From Chapter 12, Section 12.8: Equivalent Lateral Force Analysis

The seismic response coefficient Cs is determined by:
Cs = SDS / (R/Ie)  [Eq. 12.8-2]

Subject to:
- Cs need not exceed: Cs = SD1 / [T(R/Ie)]  [Eq. 12.8-3]
- Cs shall not be less than: Cs = 0.044SDSIe ≥ 0.01  [Eq. 12.8-5]

Reference: ASCE 7-22 Chapter 12.8
```

### 2. Load Combination Query Workflow

**Trigger:** User asks about load combinations, LRFD, ASD

**Process:**
1. Determine design method (LRFD or ASD)
2. Identify all applicable loads
3. Use `load_combinator.py` to generate combinations
4. Explain when each combination controls
5. Note any special requirements (flood, seismic, ice)

**Example:**
```
User: "What LRFD load combinations do I need for Dead, Live, Wind, and Snow?"

Response:
For LRFD with D, L, W, and S loads, use these combinations per ASCE 7-22 Chapter 2:

1. 1.4D                                  (Eq. 2.3-1)
2. 1.2D + 1.6L + 0.5(Lr or S or R)     (Eq. 2.3-2)
3. 1.2D + 1.6(Lr or S or R) + (L or 0.5W)  (Eq. 2.3-3)
4. 1.2D + 1.0W + L + 0.5(Lr or S or R)  (Eq. 2.3-4)

Note:
- Combination 1 typically controls for compression members
- Combination 2 usually controls for live-load-dominated structures
- Combination 4 typically controls when wind is significant
- For each combination, check both +W and -W directions

[Runs load_combinator.py to generate full list]
```

### 3. Calculation Query Workflow

**Trigger:** User wants to calculate a specific load value

**Process:**
1. Identify calculation type (wind pressure, base shear, snow load, etc.)
2. Gather required inputs from user
3. Reference appropriate chapter sections
4. Show step-by-step calculation with equation numbers
5. Provide final result with units

**Example:**
```
User: "Calculate wind pressure for 120 mph, Exposure C, at 30 ft height"

Response:
Wind pressure calculation per ASCE 7-22 Chapter 26:

Step 1: Velocity Pressure (Eq. 26.10-1)
qz = 0.00256 Kz Kzt Kd Ke V²

Given:
- V = 120 mph (basic wind speed)
- Exposure C
- z = 30 ft

Assuming:
- Kz = 0.85 (Exposure C at 30 ft, from Table 26.10-1)
- Kzt = 1.0 (no topographic effects)
- Kd = 0.85 (assuming Risk Category II, Table 26.6-1)
- Ke = 1.0 (sea level)

qz = 0.00256 × 0.85 × 1.0 × 0.85 × (120)²
qz = 28.3 psf

Reference: ASCE 7-22 Section 26.10
```

### 4. Terminology Query Workflow

**Trigger:** User asks "what is..." or definition questions

**Process:**
1. Search `glossary.md` for term
2. If not in glossary, search chapter text
3. Provide definition with context
4. Link to relevant chapter section
5. Give practical example if helpful

**Example:**
```
User: "What is Seismic Design Category?"

Response:
Seismic Design Category (SDC) is a classification from A through F that determines the level of seismic design requirements for a structure.

Per ASCE 7-22 Chapter 11.6:
- SDC A: Minimal seismic risk
- SDC B-C: Moderate seismic risk
- SDC D-F: High seismic risk (most stringent requirements)

SDC is determined by:
1. Risk Category (Table 1.5-1)
2. Site Class (Chapter 20)
3. Spectral Response Parameters (SDS, SD1)
4. Using Tables 11.6-1 and 11.6-2

Higher SDC requires:
- More rigorous structural system requirements
- Greater detailing requirements
- Additional analysis procedures
- Special inspection

Reference: ASCE 7-22 Section 11.6
```

### 5. Symbol Query Workflow

**Trigger:** User asks about a variable or symbol

**Process:**
1. Check `symbols.md` reference file
2. Search relevant chapter for symbol definition
3. Provide:
   - Symbol meaning
   - Units
   - Typical range of values
   - Where it's used

**Example:**
```
User: "What does SDS mean in seismic design?"

Response:
SDS = Design spectral response acceleration parameter at short periods

Per ASCE 7-22 Section 11.4.5:
- Units: Dimensionless (fraction of g)
- Calculated as: SDS = (2/3) Sms
- Where Sms = MCER spectral response acceleration (short period)

SDS is used to:
1. Determine Seismic Design Category (Table 11.6-1)
2. Calculate seismic response coefficient Cs (Eq. 12.8-2)
3. Determine structural system limitations

Typical values:
- Low seismicity: SDS < 0.167g
- Moderate: 0.167g ≤ SDS < 0.50g
- High: SDS ≥ 0.50g

Reference: ASCE 7-22 Sections 11.4.5, 11.6
```

### 6. Risk/Design Category Query Workflow

**Trigger:** Questions about building classification, risk category, SDC

**Process:**
1. For Risk Category:
   - Reference Table 1.5-1
   - Ask about building occupancy/function
   - Determine Category I, II, III, or IV

2. For Seismic Design Category:
   - Need: Risk Category, SDS, SD1, Site Class
   - Use Tables 11.6-1 and 11.6-2
   - Determine SDC A through F

**Example:**
```
User: "How do I determine the Risk Category for an office building?"

Response:
Risk Category determination per ASCE 7-22 Table 1.5-1:

Standard Office Building:
- Occupancy: Business (office)
- Risk Category: II (default for most buildings)

Risk Categories explained:
- **Category I**: Low hazard (agricultural, minor storage)
- **Category II**: Standard occupancy (offices, residential, retail) ← Most common
- **Category III**: Substantial hazard (schools, jails, large assembly)
- **Category IV**: Essential facilities (hospitals, fire stations, emergency shelters)

Impact of Risk Category:
- Importance factors (Ie for seismic, Is for snow)
- Load duration and return periods
- Seismic Design Category determination

For your office building, use Risk Category II unless it:
- Houses >5,000 people
- Contains hazardous materials
- Is designated as essential facility

Reference: ASCE 7-22 Table 1.5-1
```

### 7. Comparison Query Workflow

**Trigger:** "What's the difference between..." or comparison questions

**Process:**
1. Identify the two concepts being compared
2. Create side-by-side comparison table
3. Explain when to use each
4. Provide examples

**Example:**
```
User: "What's the difference between LRFD and ASD load combinations?"

Response:
LRFD vs ASD Load Combinations (ASCE 7-22 Chapter 2):

| Aspect | LRFD (Section 2.3) | ASD (Section 2.4) |
|--------|-------------------|-------------------|
| **Full Name** | Load and Resistance Factor Design | Allowable Stress Design |
| **Also Called** | Strength Design | Working Stress Design |
| **Load Factors** | Higher (1.2D, 1.6L, etc.) | Lower (1.0D, 1.0L, etc.) |
| **Philosophy** | Factor loads up, factor resistance down | Unfactored loads, reduced allowable stress |
| **Basic Combo** | 1.2D + 1.6L | D + L |
| **Wind Combo** | 1.2D + 1.0W + L + 0.5(Lr or S) | D + 0.75L + 0.75(0.6W) + 0.75(Lr or S) |

**When to use:**
- LRFD: Modern codes, steel (AISC 360), concrete (ACI 318)
- ASD: Older codes, wood (NDS), masonry, aluminum

**Key Difference:**
LRFD combinations produce higher loads (factored up), intended for use with factored resistance equations.
ASD combinations use service loads, intended for use with allowable stress values.

You CANNOT mix them - use LRFD loads with LRFD resistance, ASD loads with ASD resistance.

Reference: ASCE 7-22 Sections 2.3 and 2.4
```

### 8. Procedure Query Workflow

**Trigger:** "How do I...", step-by-step questions

**Process:**
1. Identify the design procedure requested
2. Outline step-by-step process
3. Reference relevant sections
4. Provide decision points and checks
5. List required inputs

**Example:**
```
User: "How do I perform equivalent lateral force seismic analysis?"

Response:
Equivalent Lateral Force (ELF) Procedure per ASCE 7-22 Chapter 12.8:

**Step 1: Verify ELF Method is Applicable (Section 12.6)**
- Check building height limits (Table 12.6-1)
- Check for structural irregularities (Tables 12.3-1, 12.3-2)
- Some systems/heights require modal analysis instead

**Step 2: Determine Seismic Parameters (Chapter 11)**
- Risk Category (Table 1.5-1)
- Site Class (Chapter 20)
- Spectral values SDS and SD1 (Section 11.4)
- Seismic Design Category (Section 11.6)

**Step 3: Calculate Seismic Response Coefficient Cs (Section 12.8.1.1)**
Cs = SDS / (R/Ie)  [Eq. 12.8-2]

Subject to limits:
- Maximum: Cs = SD1 / [T(R/Ie)]  [Eq. 12.8-3]
- Minimum: Cs = 0.044SDSIe ≥ 0.01  [Eq. 12.8-5]

**Step 4: Determine Approximate Period Ta (Section 12.8.2.1)**
Ta = Ct × hn^x  [Eq. 12.8-7]

Where Ct and x are from Table 12.8-2

**Step 5: Calculate Seismic Base Shear V (Section 12.8.1)**
V = CsW  [Eq. 12.8-1]

Where W = effective seismic weight

**Step 6: Distribute Vertical Forces (Section 12.8.3)**
Fx = CvxV  [Eq. 12.8-11]

Where Cvx from Eq. 12.8-12

**Step 7: Check Story Drift (Section 12.12.1)**
Δ < Δa (allowable story drift from Table 12.12-1)

**Required Inputs:**
- Building geometry (height, floor areas)
- Dead loads (seismic weight W)
- Structural system (determines R, Ω0, Cd)
- Site seismic parameters (SDS, SD1)

Reference: ASCE 7-22 Chapter 12.8
```

---

## Quick Reference Tables

### Load Symbols (Chapter 2.2)

| Symbol | Meaning | Reference |
|--------|---------|-----------|
| D | Dead load | Section 3.1 |
| L | Live load (floor) | Section 4.7 |
| Lr | Roof live load | Section 4.9 |
| S | Snow load | Chapter 7 |
| R | Rain load | Section 8.3 |
| W | Wind load | Chapter 26-30 |
| E | Seismic load | Section 12.4 |
| H | Lateral earth pressure | Section 3.2 |
| Fa | Flood load | Chapter 5 |
| Wi | Wind-on-ice | Section 10.4 |

### Risk Categories

| Category | Description | Examples |
|----------|-------------|----------|
| I | Low hazard | Agricultural, minor storage |
| II | Standard | Offices, residential, retail |
| III | Substantial | Schools, jails, large assembly (>300) |
| IV | Essential | Hospitals, fire stations, emergency |

### Seismic Design Categories

| SDC | Seismic Risk | Typical SDS Range |
|-----|--------------|-------------------|
| A | Minimal | SDS < 0.167 |
| B | Low | 0.167 ≤ SDS < 0.33 |
| C | Moderate | 0.33 ≤ SDS < 0.50 |
| D | High | SDS ≥ 0.50 |
| E | Very High | (Special conditions) |
| F | Extreme | (Near major faults) |

### Wind Exposure Categories

| Exposure | Terrain Description | Surface Roughness |
|----------|---------------------|-------------------|
| B | Urban/suburban, many obstructions | High |
| C | Open terrain, scattered obstructions | Medium |
| D | Flat, unobstructed (water, desert) | Low |

---

## Performance Optimization

### Context Management

**Priority Loading Order:**
1. Load Chapter 2 (combinations) - always needed (16 KB)
2. Load specific load chapter based on query type
3. Load calculation scripts - only when computing

**File Sizes by Category:**

*Small Files (< 20 KB):* Quick to load
- Chapter 1: 31 KB, Chapter 2: 16 KB, Chapter 3: 8 KB
- Chapter 5: 10 KB, Chapter 10: 12 KB, Chapter 14: 11 KB
- Chapter 20: 7 KB, Chapter 21: 3 KB, Chapter 28: 18 KB, Chapter 31: 18 KB

*Medium Files (20-60 KB):* Load as needed
- Chapter 4: 26 KB, Chapter 7: 24 KB, Chapter 16: 23 KB
- Chapter 19: 19 KB, Chapter 22: 32 KB, Chapter 23: 18 KB
- Chapter 15: 43 KB, Chapter 26: 58 KB, Chapter 27: 37 KB
- Chapter 29: 55 KB

*Large Files (60-120 KB):* Load selectively
- Chapter 6: 98 KB, Chapter 11: 64 KB, Chapter 17: 64 KB
- Chapter 18: 81 KB, Chapter 13: 84 KB, Chapter 30: 114 KB
- Chapter 32: 81 KB

*Very Large File:*
- **Chapter 12: 177 KB** (seismic design - load only relevant sections)
  - Use `formula_finder.py` to extract specific sections
  - Search for section numbers (e.g., "12.8" for ELF method)
  - Don't load entire file unless necessary

### Search Strategy

**Use smart_search.py first:**
```python
python3 smart_search.py "user query"
```
This maps keywords to chapters before loading files.

**For formulas, use formula_finder.py:**
```python
python3 formula_finder.py "pattern" chapter_file.md
```
Extracts equations without loading full file into context.

---

## Response Quality Checklist

When responding to ASCE 7 queries, ensure:

✅ **Cite Equation Numbers**: Always include equation numbers (e.g., "Eq. 12.8-1")
✅ **Cite Section Numbers**: Reference specific sections (e.g., "Section 12.8.3")
✅ **Include Units**: Always specify units (psf, mph, g, kips, etc.)
✅ **Clarify Scope**: Remind users ASCE 7 is for loads, not member design
✅ **Check Applicability**: Verify method applies to user's situation
✅ **Provide Context**: Explain when/why to use specific provisions
✅ **List Assumptions**: State any assumptions made in calculations
✅ **Link Chapters**: Cross-reference related chapters (e.g., Ch 11 → Ch 12)

---

## ASCE 7 Special Considerations

### 1. Loads vs. Design Distinction

**CRITICAL:** Always clarify to users:

"ASCE 7 determines LOADS (forces) to apply to structures. It does NOT design members.

For member design, use:
- Steel: AISC 360
- Concrete: ACI 318
- Wood: NDS
- Masonry: TMS 402"

### 2. Load Combination Selection

Users often confused about which combinations apply. Always:
1. Ask about ALL loads present (D, L, Lr, S, R, W, E, H, etc.)
2. Ask design method (LRFD or ASD)
3. Check for special loads (flood, ice, seismic detailed)
4. Use `load_combinator.py` to generate full list

### 3. Seismic Design Flow

Seismic design has dependencies:
```
Risk Category (Ch 1) →
Site Class (Ch 20) →
Spectral Values (Ch 11) →
SDC (Ch 11) →
Structural System Selection (Ch 12) →
Analysis Method (Ch 12) →
Design Forces (Ch 12) →
Member Design (AISC/ACI/etc.)
```

Always guide users through this flow.

### 4. Wind Load Complexity

Wind loads have multiple procedures:
- Method 1: Simplified (limited applicability)
- Method 2: Analytical (most common)
- Method 3: Wind tunnel
- Method 4: Directional with regional data

Ask about building characteristics to determine applicable method.

---

## Error Handling

### Missing Information

If user query lacks required information:
```
"To determine [X], I need:
- Building height
- Risk Category
- [Other required inputs]

Please provide these details."
```

### Out of Scope

If query is about member design, not loads:
```
"ASCE 7 provides the loads, but member design is covered by:
- Steel: AISC 360
- Concrete: ACI 318

Would you like help determining the loads per ASCE 7, or do you need assistance with member design?"
```

### Ambiguous Query

If unclear what user wants:
```
"I can help with several aspects of [topic]:
1. Load calculation procedure
2. Load combinations
3. Formula lookup
4. Definition/terminology

Which would be most helpful?"
```

---

## Common User Mistakes to Correct

1. **Mixing LRFD and ASD**: Gently correct and explain difference
2. **Confusing loads with design**: Clarify ASCE 7 scope
3. **Wrong Risk Category**: Help determine correct category
4. **Incomplete load combinations**: Ensure all applicable loads included
5. **Wrong exposure category**: Ask about surrounding terrain
6. **Ignoring special loads**: Check for flood zones, high seismic, etc.

---

## Integration with Other Tools

### Python Scripts Usage

**From skill responses:**
```
[Runs smart_search.py with query: "wind load"]
[Runs formula_finder.py on Chapter_26_Wind_Loads_General_Requirements.md]
[Runs load_combinator.py with --design LRFD --loads D,L,W]
```

### File Reading Strategy

**Efficient approach:**
1. Use smart_search first (small script)
2. Load only relevant chapter (not all 6 chapters)
3. Search within chapter for specific section
4. Extract only needed portion (use formula_finder if possible)

---

**Last Updated:** 2025-11-20
**ASCE 7 Edition:** 2022
**Status:** Production Ready - Complete Coverage (30/32 chapters)
**Note:** Chapters 8 (Rain Loads) and 9 (Reserved) not available due to source data limitations

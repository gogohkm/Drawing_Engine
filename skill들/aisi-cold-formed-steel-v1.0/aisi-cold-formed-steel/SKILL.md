---
name: aisi-cold-formed-steel
description: "AISI S100-16 Cold-Formed Steel Design (Specification, Commentary, Design Manual with 74 examples). Search specification chapters A-M, calculate member capacities using ASD/LRFD/LSD methods, apply Effective Width Method (EWM) or Direct Strength Method (DSM), lookup steel grades (ASTM A1003, A653, A792), analyze buckling modes (local, distortional, global), design connections (welds, bolts, screws), access 74 worked examples. Activates for cold-formed steel, light-gauge steel, C-section, Z-section, deck, joist, stud, purlin, girt, standing seam roof, metal building, steel framing, 냉간성형강, 경량형강, 좌굴, 유효폭 questions."
---

# AISI Cold-Formed Steel Design Skill

Comprehensive skill for AISI S100-16 (North American Specification for the Design of Cold-Formed Steel Structural Members, 2016 Edition) and AISI Cold-Formed Steel Design Manual 2017 Edition.

**Coverage:** 1,173 pages across 2 volumes, 159 organized files, 74 worked examples

**Languages:** English and Korean (한국어)

---

## Tools Required

- **Grep**: Search across specification, commentary, and examples
- **Read**: Access markdown files in `data/vol1/` and `data/vol2/`
- **Glob**: Find files by pattern
- **Bash**: Run automation scripts from `scripts/`
- **Write** (optional): Generate calculation code or reports

---

## Document Structure

This skill integrates two volumes of the AISI Cold-Formed Steel Design Manual:

### Volume 1: Design Manual (665 pages → 112 files, 1.4MB)

**Location:** `data/vol1/`

**Part I: Dimensions and Properties** (162 pages)
- `dimensions-properties/` - 24 files, 20 examples
- Steel availability, properties (Fy, Fu, E, G)
- Cross-section tables (C, Z, Hat, Angle, Track, Stud)
- Gross and effective section properties
- **Examples I-1 to I-20:** Section property calculations

**Part II: Beam Design** (256 pages)
- `beam-design/` - 23 files, 20 examples
- Bending strength (EWM and DSM methods)
- Shear strength
- Web crippling
- Combined bending and shear
- **Examples II-1 to II-15:** Beam design (many with A/B/C variants for different methods)

**Part III: Column Design** (138 pages)
- `column-design/` - 24 files, 19 examples
- Concentrically loaded columns
- Combined axial and bending
- Buckling modes (flexural, torsional, flexural-torsional)
- **Examples III-1 to III-13:** Column design (variants for EWM/DSM)

**Part IV: Connection Design** (70 pages)
- `connection-design/` - 20 files, 12 examples
- Welds (arc spot, arc seam, fillet, groove, resistance)
- Bolts (bearing, shear, tension)
- Screws (bearing, shear, pullout, pull-over, pull-through)
- Power-actuated fasteners (PAF)
- Design tables for each connection type
- **Examples IV-1 to IV-12:** Connection design

**Part V: Supplementary Information** (29 pages)
- `supplementary/` - 4 files, 1 example
- ⭐ **Specification Cross-Reference Table** (pages 628-632) - Critical mapping of specification sections to examples
- Quality construction procedures
- **Example V-1:** Ponding analysis
- `reference-data/` - 6 files
- Laterally unbraced compression flanges
- Torsional-flexural buckling (complete mathematics)
- Ponding design (Castigliano's method)
- System stability (C1.1, C1.2, C1.3 methods comparison)
- Bibliography (70+ AISI/CFSEI standards)

**Part VI: Test Procedures** (9 pages)
- `test-procedures/` - 5 files, 2 examples
- Test methods bibliography (33 ASTM standards)
- Statistical test calibration procedures (K2.1.1)
- **Examples VI-1, VI-2:** Test data calibration

**Front Matter** (5 pages)
- `front-matter/` - 4 files
- Preface, section guide, copyright, disclaimer

### Volume 2: Specification and Commentary (508 pages → 47 files, 1.6MB)

**Location:** `data/vol2/`

**Part VII: North American Specification** (171 pages)
- `specification/` - 17 files (13 chapters + 4 appendices)

**Chapters:**
- **Chapter A:** General Provisions (scope, materials, loads)
- **Chapter B:** Design Requirements (ASD, LRFD, LSD methods)
- **Chapter C:** Design for Stability (direct analysis method)
- **Chapter D:** Members in Tension
- **Chapter E:** Members in Compression (buckling modes, DSM)
- **Chapter F:** Members in Flexure (bending, lateral-torsional buckling)
- **Chapter G:** Members in Shear (shear strength, web crippling)
- **Chapter H:** Members Under Combined Forces and Torsion
- **Chapter I:** Assemblies and Systems (built-up members, diaphragms)
- **Chapter J:** Connections (welds, bolts, screws, rupture) - 171KB, largest file
- **Chapter K:** Quality Control, Testing, and Inspections
- **Chapter L:** Design for Serviceability (deflection)
- **Chapter M:** Design for Fatigue

**Appendices (Specification):**
- **Appendix 1:** Design of Elements Using Effective Width (traditional EWM)
- **Appendix 2:** General Provisions for Elastic Buckling Analysis (FEM, FSM, GBT)
- **Appendix A:** Special Provisions for USA and Mexico
- **Appendix B:** Special Provisions for Canada (CSA S136 harmonization)

**Part VIII: Commentary** (263 pages)
- `commentary/` - 20 files (13 chapters + 4 appendices + references)

**Commentary Chapters:** Match Specification Chapters A-M
- Provide background, research basis, derivations
- Test data comparisons
- Design philosophy explanations

**Commentary Appendices:** Match Specification Appendices 1-2, A-B
- Detailed theoretical derivations
- Historical development
- Validation studies

**References:** (69KB, pages 478-506)
- 400+ research papers and standards (1930s-2016)

**Appendices (Both SPEC & COMM):**
- `appendices/` - 10 files (SPEC 4 + COMM 4 + 2 support files)
- Separated into Specification and Commentary versions

---

## Reference Files

Quick-access reference materials in `references/` folder:

### 1. symbols.md
Mathematical notation from Volume 2 symbols section
- Variable definitions (A, b, E, F, M, P, etc.)
- Subscript meanings
- Units (ksi, in, kip, lb)

### 2. glossary.md
Technical term definitions
- Buckling modes (local, distortional, global)
- Section types (C, Z, Hat, Angle)
- Design terminology
- Korean-English terms (냉간성형강 = cold-formed steel)

### 3. abbreviations.md
Common abbreviations
- Design methods: ASD, LRFD, LSD
- Analysis methods: EWM, DSM
- Organizations: AISI, ASTM, CSA
- Standards: S100, A1003, A653, A792

### 4. specification-structure.md
Chapter-by-chapter organization of Specification (Chapters A-M)
- What each chapter covers
- Key sections within each chapter
- Page ranges

### 5. examples-index.md ⭐
**All 74 examples categorized by:**
- Part (I, II, III, IV, V, VI)
- Topic (properties, beam, column, connection, test)
- Method (EWM, DSM, ASD, LRFD, LSD)
- Section type (C, Z, Hat, Angle, Track)
- Page ranges

**Critical for automatic example matching!**

### 6. steel-grades-guide.md
ASTM steel grades quick reference
- **ASTM A1003:** Structural grade (SS Grades 33, 40, 50, 80, etc.)
- **ASTM A653:** Galvanized steel (Grades 33, 37, 40, 50, 80)
- **ASTM A792:** Aluminum-zinc coated (Grades 33, 37, 50, 80)
- Properties: Fy (yield), Fu (tensile), coating type

### 7. design-methods-comparison.md
**ASD vs LRFD vs LSD comparison table:**
- Load factors and combinations
- Resistance/safety factors (φ vs Ω)
- When to use each method
- Geographic preferences (USA, Canada, Mexico)

### 8. analysis-methods-comparison.md
**EWM vs DSM comparison:**
- Effective Width Method (traditional, Appendix 1)
- Direct Strength Method (modern, Chapters E-G)
- Pros and cons of each
- When to choose which method

### 9. buckling-modes-guide.md
**Three buckling modes explained:**
- **Local:** Short wavelength plate buckling
- **Distortional:** Section shape change (flange/lip rotation)
- **Global:** Member buckling (flexural, torsional, lateral-torsional)
- How to identify and calculate each

### 10. section-types-guide.md
Common cold-formed steel section types
- C-section (lipped channel)
- Z-section (cee with lips)
- Hat section
- Angle sections
- Track, Stud, Deck profiles
- Applications for each

### 11. standards-index.md
Complete list of standards referenced
- AISI standards (S902-S916 test standards, design guides)
- ASTM standards (material, test methods)
- CFSEI Technical Notes
- CSA standards (Canadian)

---

## Automation Scripts

Python scripts in `scripts/` folder for efficient searching:

### 1. smart_search.py

**Purpose:** Category-aware keyword search across both volumes

**Usage:**
```bash
python scripts/smart_search.py "beam design DSM"
```

**Features:**
- Keyword-to-category mapping
- Search Volume 1 + Volume 2 simultaneously
- Rank results by relevance
- Filter by document type (spec/commentary/examples)

**Category keywords:**
- `beam`: flexure, bending, purlin, joist, Chapter F, Part II
- `column`: compression, stud, post, Chapter E, Part III
- `connection`: weld, bolt, screw, Chapter J, Part IV
- `deck`: diaphragm, roof deck, floor deck
- `buckling`: local, distortional, global, critical load
- `steel_grade`: ASTM, A1003, A653, Fy, Fu
- `method`: ASD, LRFD, LSD, EWM, DSM

### 2. example_matcher.py ⭐

**Purpose:** Automatically match user queries to the most relevant of 74 examples

**Usage:**
```bash
python scripts/example_matcher.py "C-section beam using DSM"
```

**Features:**
- Categorizes all 74 examples by topic and method
- Filters by design method (ASD/LRFD/LSD)
- Filters by analysis method (EWM/DSM)
- Returns example number, page, and file path

**Example categories:**
- Part I (20): Section properties (gross/effective)
- Part II (20): Beams (EWM/DSM variants)
- Part III (19): Columns (EWM/DSM variants)
- Part IV (12): Connections (welds, bolts, screws)
- Part V (1): Ponding
- Part VI (2): Test calibration

### 3. formula_finder.py

**Purpose:** Extract formulas with context and variable definitions

**Usage:**
```bash
python scripts/formula_finder.py "M_n =" "data/vol2/specification/Chapter_F_Flexure.md"
```

**Features:**
- Pattern matching for equations
- Extracts ±5 context lines
- Finds variable definitions
- Preserves LaTeX formatting

### 4. specification_lookup.py

**Purpose:** Quick lookup of specification sections

**Usage:**
```bash
python scripts/specification_lookup.py "E3.2"
```

**Features:**
- Parses chapter and section numbers
- Returns specification text
- Cross-references to commentary
- Lists related examples from cross-reference table

### 5. steel_grade_lookup.py

**Purpose:** Material properties database

**Usage:**
```bash
python scripts/steel_grade_lookup.py "A653 Grade 50"
```

**Features:**
- ASTM A1003/A653/A792 database
- Returns Fy, Fu, coating type
- Thickness ranges
- Typical applications

### 6. cross_reference.py

**Purpose:** Find related sections between specification and examples

**Usage:**
```bash
python scripts/cross_reference.py "Chapter F.1"
```

**Features:**
- Uses `Specification_Cross_Reference.md` table
- Maps specification sections → examples
- Maps examples → specification requirements
- Bidirectional linking

### 7. design_method_selector.py

**Purpose:** Help users choose appropriate design approach

**Usage:**
```bash
python scripts/design_method_selector.py
```

**Features:**
- Interactive questionnaire (building location, type, code)
- Recommends ASD vs LRFD vs LSD
- Recommends EWM vs DSM
- Provides comparison tables
- Explains pros/cons

---

## Workflow by Query Type

### 1. Formula Query

**User Intent:** Find a specific formula or equation

**Trigger Keywords:**
- formula, equation, expression, 공식
- "how to calculate", "equation for"
- Variable names (M_n, P_n, F_cr, etc.)

**Workflow:**
1. Identify the topic (beam, column, connection, etc.)
2. Determine if specification or example context needed
3. Use `formula_finder.py` OR manual Grep:
   ```bash
   grep -n "M_n =" data/vol2/specification/Chapter_F_Flexure.md
   ```
4. Read ±10 lines around formula for context
5. Extract variable definitions (look for "where:" sections)
6. Check if symbols need clarification → `references/symbols.md`
7. Provide:
   - Formula in LaTeX format
   - All variable definitions with units
   - Source citation (Chapter, Section, Page)
   - Related examples if applicable

**Example Response Structure:**
```
The nominal flexural strength M_n for laterally braced members is:

$$M_n = S_e F_y$$  (AISI S100 Section F3.1.1)

where:
- S_e = effective section modulus (in³)
- F_y = yield strength (ksi)

See Example II-1A (pages 170-175) for C-section purlin calculation using EWM.
```

---

### 2. Example Query

**User Intent:** See a worked example of a design problem

**Trigger Keywords:**
- example, worked example, step-by-step, calculation, 예제
- "show me how", "demonstrate"
- "similar to"

**Workflow:**
1. **Check `references/examples-index.md` first** (fastest route)
2. Identify:
   - Member type (beam/column/connection)
   - Section type (C/Z/Hat/Angle)
   - Method preference (EWM/DSM, ASD/LRFD)
3. Use `example_matcher.py`:
   ```bash
   python scripts/example_matcher.py "C-section beam DSM LRFD"
   ```
4. If multiple matches, present options with brief descriptions
5. Read the selected example file
6. Present:
   - Example number and title
   - Given information (section, loads, materials)
   - Design method and analysis approach
   - Step-by-step solution
   - Final result
   - Page reference

**Example Index Quick Reference:**

**Part II Beams (20 examples):**
- II-1A, II-1B, II-1C: C-section purlins (EWM, DSM, LRFD-DSM variants)
- II-2A, II-2B: Z-section joists (ASD vs DSM)
- II-4A, II-4B: Through-fastened panels
- II-13: Laterally unbraced compression flange

**Part III Columns (19 examples):**
- III-1A, III-1B: Concentrically loaded C-section (EWM vs DSM)
- III-7A, III-7B, III-7C: Z-section stud wall (three variants)
- III-9A, III-9B: Built-up columns

**Part IV Connections (12 examples):**
- IV-1 to IV-8: Welded connections
- IV-9, IV-10: Bolted connections
- IV-11: Screw connection
- IV-12: Power-actuated fasteners

---

### 3. Calculation Query

**User Intent:** Perform a specific design calculation

**Trigger Keywords:**
- calculate, design, determine, check, verify, 계산
- "what is the capacity", "design a"
- Numerical values provided

**Workflow:**
1. Clarify missing information:
   - Design method: ASD, LRFD, or LSD?
   - Analysis method: EWM or DSM?
   - Steel grade: Which ASTM standard?
   - Section properties: Dimensions or standard designation?
   - Loading: Values and combinations?

2. Choose calculation path:
   - **If standard section:** Use property tables (Part I)
   - **If custom section:** Need gross/effective property calculation
   - **If simple:** Direct formula application
   - **If complex:** Follow example workflow

3. Look up relevant formulas:
   - Specification chapters (Volume 2)
   - Design tables if available (Volume 1)

4. Look up material properties:
   - Use `steel_grade_lookup.py` or `references/steel-grades-guide.md`

5. Generate Python calculation code:
   - Import necessary libraries (math, numpy)
   - Define given values
   - Apply formulas step-by-step
   - Show intermediate results
   - Apply safety/resistance factors
   - Output final design strength

6. Execute code and present results with:
   - All assumptions clearly stated
   - Method specified (e.g., "LRFD using DSM per AISI S100 Section E3")
   - Citation to specification section
   - Comparison to example if relevant

**Example Calculation Structure:**
```python
# C-Section Beam Capacity (LRFD - DSM)
# Reference: AISI S100 Chapter F, Example II-1B

import math

# Given
Fy = 50  # ksi, ASTM A653 Grade 50
E = 29500  # ksi
# ... section dimensions ...

# Calculate critical moments (DSM)
M_cre = ...  # Elastic local buckling
M_crd = ...  # Distortional buckling
M_ne = ...   # Global buckling

# Nominal strength
M_n = min(M_nl, M_nd, M_ne)  # Controlling mode

# LRFD resistance factor
phi_b = 0.90

# Design strength
phi_M_n = phi_b * M_n

print(f"Design flexural strength: {phi_M_n:.1f} kip-in")
print(f"Controlling mode: {'Local' if M_n == M_nl else 'Distortional' if M_n == M_nd else 'Global'}")
```

---

### 4. Specification Lookup

**User Intent:** Find specific requirements from the specification

**Trigger Keywords:**
- specification, requirement, code, provision, limit, 규정
- "what does the spec say", "code requirement"
- Chapter/section numbers (e.g., "Chapter E", "Section F3.1")

**Workflow:**
1. Identify chapter/section:
   - Use `references/specification-structure.md` if chapter unclear
   - Parse section numbers (e.g., "E3.2.1" = Chapter E, Section 3.2.1)

2. Use `specification_lookup.py` OR manual navigation:
   ```bash
   python scripts/specification_lookup.py "F3.1"
   ```

3. Read specification text from `data/vol2/specification/Chapter_*.md`

4. **ALWAYS cross-reference to commentary** for understanding:
   - Read corresponding `data/vol2/commentary/Commentary_*.md` section
   - Commentary explains "why" behind requirements

5. Check for related examples:
   - Use `Specification_Cross_Reference.md` table
   - List examples that demonstrate this provision

6. Present:
   - Specification text (exact wording)
   - Commentary explanation (background/rationale)
   - Related examples
   - Any special provisions (USA/Canada/Mexico)

**Chapter Quick Reference:**
- A: General (scope, materials, loads)
- B: Design requirements (ASD/LRFD/LSD)
- C: Stability (direct analysis, notional loads)
- D: Tension members
- E: Compression members (buckling, DSM)
- F: Flexural members (bending, LTB)
- G: Shear (shear strength, web crippling)
- H: Combined forces and torsion
- I: Assemblies (built-up, diaphragms)
- J: Connections (welds, bolts, screws)
- K: Quality control and testing
- L: Serviceability (deflection)
- M: Fatigue

---

### 5. Design Method Selection

**User Intent:** Understand or choose between design methods

**Trigger Keywords:**
- "which method", "ASD vs LRFD", "EWM vs DSM"
- "difference between", "when to use"
- "should I use"

**Workflow:**

**For ASD vs LRFD vs LSD:**
1. Read `references/design-methods-comparison.md`
2. Ask about project context:
   - Location (USA/Canada/Mexico)?
   - Building code requirements?
   - Client/engineer preference?
3. Explain differences:

   **ASD (Allowable Strength Design):**
   - Uses safety factors Ω
   - R_n / Ω ≥ Required strength
   - Simpler load combinations
   - Common in USA

   **LRFD (Load and Resistance Factor Design):**
   - Uses resistance factors φ
   - φR_n ≥ Required strength (factored loads)
   - More complex load combinations
   - Preferred in USA, modern approach

   **LSD (Limit States Design):**
   - Canadian variant of LRFD
   - Different load factors (NBCC)
   - See Appendix B

4. Provide comparison table from reference file
5. **Note:** Many examples have A/B variants showing both methods!

**For EWM vs DSM:**
1. Read `references/analysis-methods-comparison.md`
2. Explain differences:

   **EWM (Effective Width Method):**
   - Traditional approach (since 1946, Winter)
   - Uses reduced effective widths for slender elements
   - Found in Specification Appendix 1
   - More conservative
   - Well-established, widely accepted

   **DSM (Direct Strength Method):**
   - Modern approach (introduced 2004, 2007)
   - Uses elastic buckling analysis
   - Integrated in main Specification (Chapters E, F, G)
   - Less conservative, especially for unusual sections
   - Requires elastic buckling software (or tables)

3. When to use:
   - **EWM:** Standard sections, traditional practice, simpler hand calcs
   - **DSM:** Complex sections, optimization, computer-aided design

4. **Note:** Many examples show both methods (e.g., Example II-1A = EWM, II-1B = DSM)

---

### 6. Steel Grade Lookup

**User Intent:** Find material properties for a specific steel grade

**Trigger Keywords:**
- steel grade, material, ASTM, A1003, A653, A792
- Fy, Fu, yield strength, tensile strength
- galvanized, coating, 재료

**Workflow:**
1. Use `steel_grade_lookup.py` OR `references/steel-grades-guide.md`
2. Identify ASTM standard:
   - **A1003:** Structural grades (bare or coated)
   - **A653:** Hot-dip galvanized
   - **A792:** Aluminum-zinc coated (55% Al-Zn or Zn-5% Al)
3. Extract properties:
   - Fy (yield strength, ksi)
   - Fu (tensile strength, ksi)
   - Thickness range
   - Coating type and designation
4. Check Specification Chapter A for additional requirements:
   - Ductility requirements
   - Elongation
   - Coating adhesion

**Common Grades Quick Table:**

| ASTM | Grade | Fy (ksi) | Fu (ksi) | Coating | Notes |
|------|-------|----------|----------|---------|-------|
| A1003 | SS Grade 33 | 33 | 45 | Various | Structural |
| A1003 | SS Grade 50 | 50 | 65 | Various | Common |
| A653 | Grade 33 | 33 | 45 | G40-G90 | Galvanized |
| A653 | Grade 50 | 50 | 65 | G40-G90 | Galvanized |
| A792 | Grade 50 | 50 | 65 | AZ50 | Al-Zn |

**Note:** Volume 1 Section 1 (pages 9-21) has complete steel properties tables.

---

### 7. Buckling Mode Analysis

**User Intent:** Understand or calculate buckling behavior

**Trigger Keywords:**
- buckling, critical load, euler, 좌굴
- local, distortional, global
- flexural, torsional, lateral-torsional

**Workflow:**
1. Read `references/buckling-modes-guide.md` for overview
2. Identify which mode is relevant:

   **Local Buckling:**
   - Short wavelength (plate panels between stiffeners)
   - All thin-walled sections susceptible
   - **EWM approach:** Reduce to effective width
   - **DSM approach:** Calculate F_crl (elastic local buckling stress)
   - See: Specification Sections E3.1, F3.1, G2.1

   **Distortional Buckling:**
   - Intermediate wavelength (flange+lip rotation)
   - C-sections, Z-sections with edge stiffeners
   - **DSM only:** Calculate F_crd
   - See: Specification Sections E3.2, F3.2
   - Examples: II-1B, III-1B show distortional mode

   **Global Buckling:**
   - **Flexural:** Euler column buckling (long members)
   - **Torsional:** Twisting about shear center
   - **Flexural-torsional:** Combined (unsymmetric sections)
   - **Lateral-torsional:** Beams (out-of-plane + twist)
   - See: Specification Sections E2, E4, F2

3. For calculations:
   - **If DSM:** Need elastic critical loads (F_crl, F_crd, F_cre)
   - **If EWM:** Use effective width reductions
   - Use appropriate specification chapter formulas
   - Reference examples for similar sections

4. Explain which mode likely controls:
   - Short compression members → local or distortional
   - Long compression members → global (flexural/torsional)
   - Beams → local, distortional, or lateral-torsional

**Reference:**
- Volume 1 Part V Section 3 (pages 634-639): Torsional-flexural buckling complete derivation
- Appendix 2: Elastic buckling analysis methods (FEM, FSM, GBT)

---

### 8. Example Matching

**User Intent:** Find an example similar to their design problem

**Trigger Keywords:**
- "similar to", "like", "example of"
- "have you seen", "is there an example"

**Workflow:**
1. Extract problem characteristics from user query:
   - Member type (beam/column/connection)
   - Section type (C/Z/Hat/Angle/built-up)
   - Loading type (gravity/lateral/combined)
   - Design method preference (ASD/LRFD)
   - Analysis method preference (EWM/DSM)

2. Use `example_matcher.py`:
   ```bash
   python scripts/example_matcher.py "Z-section column with bending LRFD DSM"
   ```

3. If exact match not found, suggest closest matches with differences noted

4. Present top 3 matches with:
   - Example number
   - Brief description
   - Method used
   - Similarity score/explanation
   - Page reference

5. User selects one → read and present that example

**Example Matching Strategy:**
- Beam problems → Part II (20 examples)
- Column problems → Part III (19 examples)
- Connection problems → Part IV (12 examples)
- Property calculations → Part I (20 examples)
- Unusual cases → Part V, Part VI

---

### 9. Terminology Query

**User Intent:** Understand the definition of a technical term

**Trigger Keywords:**
- "what is", "define", "meaning of", "explain"
- "뭐야", "무슨 뜻"

**Workflow:**
1. Check `references/glossary.md` first (fastest)
2. If not in glossary, search Specification Chapter A (definitions section)
3. If still not found, search Commentary for explanatory text
4. Provide:
   - Clear definition
   - Context/usage
   - Related terms
   - Example if helpful
   - Korean translation if applicable

**Common Terms:**
- **Cold-formed steel (냉간성형강):** Steel shaped at room temperature by roll-forming or press-braking
- **Effective width (유효폭):** Reduced width that accounts for local buckling (EWM concept)
- **Direct Strength Method (DSM):** Design method using elastic buckling loads
- **Distortional buckling:** Buckling mode with cross-section distortion
- **Fy:** Yield strength (항복강도)
- **Fu:** Tensile strength (인장강도)
- **Phi (φ):** Resistance factor (LRFD)
- **Omega (Ω):** Safety factor (ASD)

---

### 10. Symbol Query

**User Intent:** Understand mathematical notation/symbols

**Trigger Keywords:**
- "what does [symbol] mean"
- "notation", "subscript", "기호"

**Workflow:**
1. Check `references/symbols.md` (extracted from Volume 2 symbols section)
2. Find symbol definition with:
   - Full name
   - Units
   - Context (when used)
3. If subscript meanings unclear, explain:
   - e = effective
   - n = nominal
   - a = allowable
   - cr = critical (buckling)
   - y = yield
   - u = ultimate

**Common Symbols:**
- **M_n:** Nominal moment strength (kip-in or kN-m)
- **P_n:** Nominal axial strength (kip or kN)
- **S_e:** Effective section modulus (in³)
- **F_cr:** Critical buckling stress (ksi)
- **φ:** Resistance factor (dimensionless)
- **Ω:** Safety factor (dimensionless)
- **L_b:** Unbraced length (in)

**Note:** Volume 2 has complete symbols section (pages 25-73), but reference file has most commonly used symbols.

---

## Quick Reference Tables

### Document Categories

| Category | Location | Files | Purpose |
|----------|----------|-------|---------|
| Design Examples | `data/vol1/` Parts I-IV | 74 examples | Step-by-step calculations |
| Specification | `data/vol2/specification/` | 17 files | Code requirements (normative) |
| Commentary | `data/vol2/commentary/` | 20 files | Background and theory (informative) |
| Appendices | `data/vol2/appendices/` | 10 files | Detailed methods (EWM, elastic buckling) |
| Supplementary | `data/vol1/supplementary/` | 4 files | Cross-reference, ponding |
| Reference Data | `data/vol1/reference-data/` | 6 files | Stability, bibliography |
| Test Procedures | `data/vol1/test-procedures/` | 5 files | ASTM standards, calibration |
| Quick References | `references/` | 11 files | Fast lookup tables |

---

### Chapter-to-Topic Mapping

| Chapter | Topic | Related Examples | Key Features |
|---------|-------|------------------|--------------|
| A | General Provisions | I-1 to I-20 | Materials (ASTM A1003, A653, A792) |
| B | Design Requirements | All | ASD (Ω), LRFD (φ), LSD methods |
| C | Stability | - | Direct analysis, notional loads |
| D | Tension | - | Net section, staggered holes |
| E | Compression | III-1 to III-13 | Buckling modes, DSM, Column curves |
| F | Flexure | II-1 to II-15 | Bending, LTB, Effective width, DSM |
| G | Shear | II-3, II-4 | Shear strength, Web crippling |
| H | Combined Forces | III-2 to III-13 | Interaction equations |
| I | Assemblies | III-9, III-10 | Built-up members, Diaphragms |
| J | Connections | IV-1 to IV-12 | Welds, Bolts, Screws, PAF |
| K | Testing | VI-1, VI-2 | Quality control, Test standards |
| L | Serviceability | V-1 | Deflection limits |
| M | Fatigue | - | S-N curves |

---

### Design Methods Comparison

| Method | Factor | Equation | Load Combinations | Region | Notes |
|--------|--------|----------|-------------------|--------|-------|
| **ASD** | Ω (safety) | R_n / Ω ≥ R_a | D, L, W, S (unfactored) | USA | Simple, conservative |
| **LRFD** | φ (resistance) | φR_n ≥ R_u | 1.2D + 1.6L + ... | USA | Modern, probabilistic |
| **LSD** | φ (resistance) | φR_n ≥ R_f | NBCC factors | Canada | Similar to LRFD |

**Typical φ and Ω values:**
- Tension: φ = 0.90, Ω = 1.67
- Compression: φ = 0.85, Ω = 1.80
- Flexure: φ = 0.90 or 0.95, Ω = 1.67 or 1.60
- Connections: φ = 0.50-0.70, Ω = 2.00-2.40

---

### Analysis Methods Comparison

| Method | Approach | Specification Location | Complexity | Conservatism | Best For |
|--------|----------|------------------------|------------|--------------|----------|
| **EWM** | Effective width reduction | Appendix 1 | Low | Higher | Standard sections, Hand calcs |
| **DSM** | Elastic buckling loads | Chapters E, F, G | Medium | Lower | All sections, Computer-aided |

**EWM (Effective Width Method):**
- Based on Winter's formula (1946)
- Reduces element width based on slenderness
- ρ = (1 - 0.22/λ)/λ when λ > 0.673
- Well-established, simple

**DSM (Direct Strength Method):**
- Requires F_crl (local), F_crd (distortional), F_cre (global)
- Uses strength curves similar to column curves
- More accurate for complex sections
- Needs finite strip or FEM software (or tables)

---

### Common Steel Grades

| ASTM | Grade | Fy (ksi) | Fu (ksi) | Coating | Typical Use |
|------|-------|----------|----------|---------|-------------|
| A1003 | SS-33 | 33 | 45 | Various | Light-duty structural |
| A1003 | SS-50 | 50 | 65 | Various | General structural |
| A1003 | SS-80 | 80 | 82 | Various | High-strength |
| A653 | Grade 33 | 33 | 45 | G40-G90 | Roof/wall panels |
| A653 | Grade 50 | 50 | 65 | G60-G90 | Structural framing |
| A792 | Grade 50 | 50 | 65 | AZ50/AZ55 | Standing seam roofs |

**Coating designations:**
- G40, G60, G90: Galvanized (oz/ft² both sides)
- AZ50, AZ55: Aluminum-zinc (55% Al, 43.4% Zn, 1.6% Si)

**Elastic modulus:** E = 29,500 ksi (203,000 MPa) for all grades
**Shear modulus:** G = 11,300 ksi (77,900 MPa)

---

### Section Types

| Type | Description | Typical Applications | Buckling Concerns |
|------|-------------|----------------------|-------------------|
| C-section | Lipped channel | Purlins, girts, joists | Local, distortional, LTB |
| Z-section | Cee with lips | Purlins, girts | Local, distortional, LTB |
| Hat section | Inverted U with brims | Roof/floor deck | Local, web crippling |
| Angle | L-shape (equal or unequal) | Bracing, lintels | Torsional-flexural |
| Track | U-channel (unlipped) | Top/bottom plates | Local (if compression) |
| Stud | C or U with punchouts | Wall framing | Local, distortional |
| Built-up | Multiple shapes | Heavy columns, beams | Connection, local |

---

### Example Categories

| Part | Topic | Count | Methods | Page Range | Key Features |
|------|-------|-------|---------|------------|--------------|
| I | Properties | 20 | Gross, Effective | 54-162 | Section calculations |
| II | Beams | 20 | EWM, DSM, ASD, LRFD | 163-418 | A/B/C variants common |
| III | Columns | 19 | EWM, DSM, ASD, LRFD | 419-556 | Buckling modes |
| IV | Connections | 12 | ASD, LRFD | 557-626 | Welds, bolts, screws |
| V | Supplementary | 1 | MASTAN2 | 627-655 | Ponding analysis |
| VI | Test Procedures | 2 | Statistical | 656-664 | φ and Ω calibration |

**Total: 74 examples**

**Variant notation:**
- A suffix: Usually EWM or ASD
- B suffix: Usually DSM or LRFD
- C suffix: Alternative method or section type

---

## Performance Optimization

### Search Strategy Priority

For fastest results, follow this search order:

1. **Check reference files first** (`references/` folder)
   - Instant answers for common queries
   - symbols.md, glossary.md, examples-index.md, steel-grades-guide.md

2. **Use automation scripts**
   - `example_matcher.py` for finding examples
   - `steel_grade_lookup.py` for materials
   - `specification_lookup.py` for code sections
   - `smart_search.py` for keyword searches

3. **Search Specification** (`data/vol2/specification/`)
   - For code requirements ("what is required?")
   - Authoritative, normative language

4. **Search Commentary** (`data/vol2/commentary/`)
   - For understanding ("why is it required?")
   - Background, research basis, derivations

5. **Search Examples** (`data/vol1/` Parts I-IV)
   - For application ("how to apply?")
   - Step-by-step worked problems

6. **Check Cross-Reference Table** (`data/vol1/supplementary/Specification_Cross_Reference.md`)
   - Maps specification sections to examples
   - Critical for connecting theory to practice

### Smart Chapter Targeting

Route queries directly to relevant chapters:

- **Beam design** → Chapter F (spec), Commentary F, Part II (examples)
- **Column design** → Chapter E (spec), Commentary E, Part III (examples)
- **Connection design** → Chapter J (spec), Commentary J, Part IV (examples)
- **Stability analysis** → Chapter C (spec), Commentary C, Section 6 (reference)
- **Material properties** → Chapter A (spec), Part I Section 1
- **Section properties** → Part I Section 2-3
- **Buckling theory** → Appendix 2 (spec), Commentary Appendix 2
- **Effective width** → Appendix 1 (spec), Commentary Appendix 1
- **Test standards** → Chapter K (spec), Part VI
- **Ponding** → Section L (spec), Part V Section 5, Example V-1

### Avoid Redundant Searches

- Don't search all files if reference files can answer
- Don't read entire chapters if section number known
- Don't search examples if specification lookup sufficient
- Don't use Grep if script exists for that task

### Volume 1 vs Volume 2 Usage

**Use Volume 1 when:**
- User needs worked examples
- Need property tables for standard sections
- Want to see step-by-step calculations
- Need design tables (connections, sections)

**Use Volume 2 when:**
- User needs code requirements
- Want theoretical background
- Need formula derivations
- Researching design philosophy

**Use both when:**
- Complete design problem
- Learning a new concept
- Validating calculations
- Understanding why requirement exists

---

## Response Quality Checklist

Every response should include appropriate items from this checklist:

### For Formula/Specification Queries:
- ✅ **Citation:** Chapter/Section/Page (e.g., "AISI S100 Section F3.1.1, page 110")
- ✅ **Formula:** In LaTeX format with proper notation
- ✅ **Variables:** All symbols defined with units
- ✅ **Applicability:** When formula applies, limitations
- ✅ **Cross-reference:** Related sections or examples

### For Calculation Queries:
- ✅ **Method specified:** ASD or LRFD or LSD
- ✅ **Approach specified:** EWM or DSM
- ✅ **Material identified:** ASTM grade and properties (Fy, Fu, E)
- ✅ **Section identified:** Type and dimensions
- ✅ **Units:** Consistent throughout (ksi, in, kip, etc.)
- ✅ **Code:** Working Python code (if applicable)
- ✅ **Result:** Clear final answer with units
- ✅ **Check:** Compare to similar example if available

### For Example Queries:
- ✅ **Example number:** (e.g., "Example II-1A")
- ✅ **Title:** Brief description
- ✅ **Method:** ASD/LRFD, EWM/DSM
- ✅ **Page reference:** Volume 1 page numbers
- ✅ **File path:** For Read tool access
- ✅ **Key results:** Final design values
- ✅ **Variants:** Note if A/B/C variants exist

### For General Queries:
- ✅ **Accuracy:** Information from actual documents, not assumed
- ✅ **Completeness:** Address all parts of user question
- ✅ **Clarity:** Technical but understandable
- ✅ **References:** Cite sources for verification
- ✅ **Korean support:** Translate key terms if user uses Korean

### Avoid:
- ❌ Speculation or assumptions not in documents
- ❌ Mixing ASD and LRFD without clarification
- ❌ Using formulas without defining variables
- ❌ Omitting units
- ❌ Citing sections without reading them
- ❌ Ignoring user's specified method preference

---

## Special Features: Cold-Formed Steel Specifics

### Three Design Methods

This specification uniquely provides THREE design methods (most codes have one or two):

**1. ASD (Allowable Strength Design):**
- Traditional method (pre-1986)
- Nominal strength ÷ Safety factor Ω
- R_n / Ω ≥ R_a (allowable strength ≥ required strength)
- Load combinations use service (unfactored) loads
- **When to use:** Client prefers, simpler load combinations, USA projects

**2. LRFD (Load and Resistance Factor Design):**
- Modern probabilistic method (1986+)
- Resistance factor φ × Nominal strength
- φR_n ≥ R_u (design strength ≥ required strength)
- Load combinations use factored loads (1.2D + 1.6L + ...)
- **When to use:** Modern practice, USA projects, optimization

**3. LSD (Limit States Design):**
- Canadian variant of LRFD
- Similar to LRFD but uses Canadian load factors (NBCC)
- See Appendix B for specific provisions
- **When to use:** Canada projects

**AISI S100 provides φ and Ω for EVERY limit state** so engineers can use any method!

**Relationship:** Approximately φ × Ω ≈ 1.5 to 1.6

---

### Two Analysis Methods

This specification provides TWO ways to account for local buckling:

**1. Effective Width Method (EWM):**
- Traditional (George Winter, 1946)
- In Specification Appendix 1
- Concept: Reduce width of slender compression elements
- Effective width: b = ρw, where ρ = (1 - 0.22/λ)/λ
- Calculate effective properties (A_e, I_e, S_e)
- Use effective properties in strength equations
- **Pros:** Simple, hand-calculable, well-established
- **Cons:** Conservative, cumbersome for complex sections
- **Examples:** I-8A, II-1A, III-1A, etc. (A suffix often means EWM)

**2. Direct Strength Method (DSM):**
- Modern (2004 edition, expanded 2007+)
- Integrated in main Specification (Chapters E, F, G)
- Concept: Use elastic critical buckling loads in strength curves
- Calculate F_crl (local), F_crd (distortional), F_cre (global)
- Apply strength curves (similar to column curves)
- **Pros:** Less conservative, better for unusual sections, unified approach
- **Cons:** Requires elastic buckling analysis (software or tables)
- **Examples:** I-8B, II-1B, III-1B, etc. (B suffix often means DSM)

**Both methods are equally valid!** Many examples show both for comparison.

---

### Three Buckling Modes

Cold-formed steel is unique because it can buckle in THREE distinct modes:

**1. Local Buckling:**
- Short wavelength (few inches)
- Individual plates buckle between stiffeners
- Half-wavelength ≈ plate width
- **All thin sections susceptible**
- Post-buckling strength exists (plates still carry load after buckling)
- **EWM:** Account via effective width
- **DSM:** Account via F_crl and local slenderness λ_l

**2. Distortional Buckling:**
- Intermediate wavelength (several inches to feet)
- Edge stiffeners (lips) rotate, flange distorts
- **Sections with edge stiffeners** (C, Z with lips)
- Critical mode for intermediate lengths
- **EWM:** Not directly addressed (use judgment)
- **DSM:** Account via F_crd and distortional slenderness λ_d
- **Specification Sections:** E3.2, F3.2

**3. Global Buckling:**
- Long wavelength (member length)
- Entire member buckles as a whole
- Types:
  - **Flexural:** Euler column buckling
  - **Torsional:** Twisting (closed/open sections)
  - **Flexural-torsional:** Combined (singly-symmetric, unsymmetric)
  - **Lateral-torsional:** Beams (out-of-plane + twist)
- **All sections** at sufficient length
- **Both EWM and DSM** account similarly
- **Specification Sections:** E2, E4, F2

**Critical difference from hot-rolled steel:**
- Hot-rolled: Usually only global buckling matters
- Cold-formed: Often local or distortional controls!

**Design must check all three modes** and use the minimum strength.

---

### Critical Differences from Hot-Rolled Steel

If you're familiar with hot-rolled steel (AISC), note these differences:

**1. Slenderness:**
- Cold-formed: Very thin (typically 14-28 gauge, 0.075"-0.013")
- Hot-rolled: Thick sections (typically > 0.25")
- **Implication:** Local buckling almost always critical for cold-formed

**2. Post-Buckling Strength:**
- Cold-formed: Plates carry significant load after local buckling
- Hot-rolled: Usually neglected
- **Implication:** Effective width concept is critical

**3. Residual Stresses:**
- Cold-formed: Different pattern, often beneficial (cold-work strengthening)
- Hot-rolled: Significant tension/compression from cooling
- **Implication:** Cold-formed may have higher yield in corners

**4. Connection Design:**
- Cold-formed: Connections often critical (thin material, bearing, tearout)
- Hot-rolled: Usually ductile, connections less critical
- **Implication:** More attention to connection limit states

**5. Buckling Modes:**
- Cold-formed: Three modes (local, distortional, global)
- Hot-rolled: Usually one mode (global)
- **Implication:** More complex buckling analysis

**6. Section Types:**
- Cold-formed: Open thin-walled (C, Z, Angle, Track)
- Hot-rolled: Wide-flange, I-sections
- **Implication:** Different torsional behavior

**7. Fabrication:**
- Cold-formed: Roll-formed or press-braked at room temp
- Hot-rolled: Rolled at high temperature
- **Implication:** Tighter tolerances, no heat effects

---

### When to Use EWM vs DSM

**Use Effective Width Method (EWM) when:**
- Standard, common sections (C, Z from manufacturer)
- Traditional practice, client familiarity
- Hand calculations preferred
- Conservative design acceptable
- No access to elastic buckling software
- Learning the basics (simpler conceptually)

**Use Direct Strength Method (DSM) when:**
- Complex, unusual sections (multi-element, perforated)
- Optimization desired (less conservative)
- Computer-aided design workflow
- Elastic buckling software available (CUFSM, THIN-WALL, etc.)
- Multiple buckling modes need consideration
- Modern, efficient design

**Use BOTH when:**
- Validating results
- Learning the specification
- Research or academic work
- Comparing to other designs

**Note:** Many Volume 1 examples present both methods side-by-side!
- Example II-1A (EWM) vs II-1B (DSM): Same purlin, different methods
- Example III-1A (EWM) vs III-1B (DSM): Same column, different methods

---

## Error Handling

### Common Issues and Solutions

**Issue 1: Method not specified**
- **User query:** "Calculate beam capacity"
- **Problem:** Could be ASD or LRFD
- **Response:** Ask "Should I use ASD (allowable strength design) or LRFD (load and resistance factor design)?"
- **Offer:** "I can show you both if you'd like. LRFD is more common in modern practice."

**Issue 2: Steel grade unclear**
- **User query:** "Design a C-section column"
- **Problem:** Material properties needed
- **Response:** Ask "Which steel grade should I use? Common options are ASTM A653 Grade 33, Grade 50, or ASTM A1003 SS-50."
- **Offer:** Show `steel-grades-guide.md` table

**Issue 3: No results found**
- **User query:** Searches for obscure topic
- **Problem:** No direct match
- **Response:**
  1. Suggest broader search
  2. List closest matches
  3. Offer to search related chapters
  4. Check if user meant different term

**Issue 4: Ambiguous query**
- **User query:** "Column design"
- **Problem:** Too broad
- **Response:** "I can help with column design! To give you the most relevant information, could you clarify:
  - Section type? (C-section, Z-section, built-up, etc.)
  - Loading? (Axial only, or combined with bending?)
  - Design method? (ASD or LRFD?)"

**Issue 5: Missing parameters**
- **User query:** "Calculate the capacity"
- **Problem:** Insufficient information
- **Response:** List required inputs:
  - Section dimensions or designation
  - Steel grade (Fy, Fu)
  - Unbraced lengths (L_x, L_y, L_t)
  - Design method (ASD/LRFD)
  - Analysis method (EWM/DSM)

**Issue 6: Conflicting methods**
- **User code:** Mixes ASD load combinations with LRFD φ factors
- **Problem:** Incorrect methodology
- **Response:**
  - Flag the error clearly
  - Explain correct approach for each method
  - Offer to redo calculation correctly

**Issue 7: Out of scope**
- **User query:** Hot-rolled steel, concrete, etc.
- **Problem:** Wrong specification
- **Response:** "This skill covers AISI S100 (cold-formed steel). For [hot-rolled steel], you'll need AISC 360. Would you like me to help with a cold-formed steel question instead?"

---

## Special Notes

### Volume 1 vs Volume 2 Usage

**Volume 1 (Design Manual):**
- **Purpose:** Practical design aid
- **Audience:** Practicing engineers
- **Content:** Examples, tables, procedures
- **Language:** "How to apply the specification"
- **Use when:** Designing real structures, learning by example

**Volume 2 (Specification & Commentary):**
- **Purpose:** Legal requirement + background
- **Audience:** Engineers, code officials, researchers
- **Content:** Normative requirements + research basis
- **Language:** "Shall" (spec), "This section is based on..." (commentary)
- **Use when:** Determining code requirements, understanding theory

**Relationship:**
- Volume 1 examples demonstrate Volume 2 specification
- `Specification_Cross_Reference.md` links them

### Example Numbering Convention

**Format:** [Part]-[Number][Variant]

Examples:
- **I-1:** Part I, Example 1 (no variants)
- **II-1A:** Part II, Example 1, Variant A (usually EWM or ASD)
- **II-1B:** Part II, Example 1, Variant B (usually DSM or LRFD)
- **II-1C:** Part II, Example 1, Variant C (alternative method/section)
- **III-7A, III-7B, III-7C:** Part III, Example 7 with three variants

**Variant meanings (common patterns):**
- **A suffix:** Often EWM, ASD, or first approach
- **B suffix:** Often DSM, LRFD, or alternative approach
- **C suffix:** Alternative section type or third method

**Always check the actual example title** to confirm what the variant represents!

### Cross-Reference Table Importance

**Location:** `data/vol1/supplementary/Specification_Cross_Reference.md` (pages 628-632)

**This is one of the most valuable files!**

**What it does:**
- Maps EVERY section of the Specification to relevant examples
- Example: "Chapter E.3.1 → See Examples III-1A, III-1B, III-5A, III-5B"
- Connects theory (spec) to practice (examples)

**Use it to:**
1. Find examples that demonstrate a specification section
2. Verify calculations against official examples
3. Learn how to apply complex provisions
4. Teach cold-formed steel design

**Always reference this table when:** User asks about a specification section and wants to see it applied.

### Bibliography Location

**Volume 1:** `data/vol1/reference-data/Bibliography_Standards_Guides.md` (pages 651-653)
- 70+ AISI and CFSEI documents
- Design guides, test standards, technical notes
- Organized by category

**Volume 2:** `data/vol2/commentary/References.md` (pages 478-506, 69KB)
- 400+ research papers and standards
- Chronological from 1930s to 2016
- Full citations with authors, titles, publications

**Use when:**
- User wants research background
- Looking for additional resources
- Citing sources for reports
- Finding test data

### File Size Considerations

**Large files (>50KB):**
- `Chapter_J_Connections.md` (171KB) - May need Read with limit/offset
- `Commentary_J_Connections.md` (85KB)
- `Appendix_2_Elastic_Buckling_Analysis_COMM.md` (82KB)
- `Section_2_Cross_Section_Tables.md` (102KB)
- `References.md` (69KB)

**For large files:** Use Grep to find section first, then Read specific lines.

### Korean Language Support

**This skill supports Korean queries:**
- 냉간성형강 = cold-formed steel
- 좌굴 = buckling
- 유효폭 = effective width
- 단면 = section
- 보 = beam
- 기둥 = column
- 접합부 = connection
- 항복강도 = yield strength (Fy)
- 인장강도 = tensile strength (Fu)
- 설계 = design
- 계산 = calculate

**When user uses Korean:**
1. Respond in Korean for explanations
2. Keep technical terms in English with Korean translation
3. Formulas and code remain in English
4. Citations in English (standard practice)

---

## Summary

This skill provides comprehensive access to the AISI S100-16 Cold-Formed Steel Specification and Design Manual.

**Key capabilities:**
- ✅ Search 1,173 pages efficiently
- ✅ Match queries to 74 examples automatically
- ✅ Explain ASD vs LRFD vs LSD
- ✅ Explain EWM vs DSM
- ✅ Lookup steel grades instantly
- ✅ Provide accurate calculations
- ✅ Cross-reference spec ↔ examples
- ✅ Support English and Korean
- ✅ Generate working Python code

**Always:**
- Cite AISI S100 sections
- Specify method (ASD/LRFD) and approach (EWM/DSM)
- Define variables with units
- Reference examples when applicable
- Provide accurate, verified information

**Never:**
- Speculate or assume
- Mix methods without clarification
- Omit units or definitions
- Cite without reading
- Ignore user's method preference

---

**Skill Version:** 1.0
**Last Updated:** 2025-11-10
**Documents:** AISI S100-16 (2016) + Design Manual (2017)
**Total Pages:** 1,173
**Total Files:** 159
**Examples:** 74

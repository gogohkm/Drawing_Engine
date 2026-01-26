# ADM 2020 Specification Structure

Navigation guide for the Aluminum Design Manual structure and chapter organization.

---

## Overall Document Structure

The ADM 2020 is organized into **8 Parts**, spanning 536 pages:

```
ADM 2020 Manual (536 pages)
├── Front Matter (Pages 9-28)
│   ├── Symbols and Notation
│   ├── Glossary
│   └── Abbreviations
│
├── Part I - Specification (Pages 29-98, 70 pages)
│   ├── Chapter A: General (A.1-A.10)
│   ├── Chapter B: Members (B.1-B.7)
│   ├── Chapter C: Connections (C.1-C.8)
│   ├── Chapter D: HSS Design (D.1-D.9)
│   ├── Chapter E: Beams (E.1-E.6)
│   ├── Chapter F: Shear (F.1-F.5)
│   ├── Chapter G: Flat Plates (G.1-G.3)
│   ├── Chapter H: Combined Forces (H.1-H.4)
│   ├── Chapter I: Composite Members (I.1-I.3)
│   ├── Chapter J: Connections (J.1-J.5)
│   ├── Chapter K: Special Members (K.1-K.3)
│   ├── Chapter L: Serviceability (L.1-L.4)
│   ├── Chapter M: Fabrication (M.1-M.6)
│   └── Chapter N: Quality Control (N.1-N.4)
│
├── Part II - Commentary (Pages 99-172, 74 pages)
│   └── Detailed commentary for all chapters (C-A through C-N)
│
├── Part III - Design Guides (Pages 173-202, 30 pages)
│   ├── DG 1: Introduction to Aluminum Design
│   ├── DG 2: Material Selection
│   ├── DG 3: Buckling Analysis
│   └── ... (additional guides)
│
├── Part IV - Material Properties (Pages 203-234, 32 pages)
│   ├── Tables of mechanical properties
│   ├── Unwelded and welded values
│   └── Temperature-dependent data
│
├── Part V - Dimensions & Properties (Pages 235-398, 164 pages)
│   ├── Section properties for standard shapes
│   ├── W-shapes, channels, angles, tubes
│   └── Geometric properties (A, Ix, Iy, Sx, rx, ry, etc.)
│
├── Part VII - Examples (Pages 399-470, 72 pages)
│   └── ~25 worked calculation examples
│
└── Part VIII - Reference Data (Pages 471-536, 66 pages)
    ├── Conversion factors
    ├── Historical data
    └── Additional tables
```

**Note:** Part VI is not present in this edition.

---

## Part I - Specification (Pages 29-98)

The core design requirements. All chapters follow the **"shall"** language for mandatory provisions.

### Chapter A: General Provisions (Pages 29-39)

**Key Sections:**
- **A.1**: Scope
- **A.2**: Referenced specifications
- **A.3**: Material properties
- **A.4**: Alloy and temper designations
- **A.5**: Loads and load combinations
- **A.6**: Design basis (ASD only)
- **A.7**: Safety factors (Ω)
- **A.8**: Temperature limits
- **A.9**: Corrosion considerations
- **A.10**: Notations and symbols

**What You'll Find Here:**
- Alloy designation system (6061-T6, etc.)
- Temperature limits (200°F for T6 sustained)
- Material specifications (ASTM B209, B221, etc.)
- Design philosophy (ASD, no LRFD)

---

### Chapter B: Members Subject to Compression (Pages 40-49)

**Key Sections:**
- **B.1**: Scope
- **B.2**: Slenderness limitations
- **B.3**: Effective length (K factors)
- **B.4**: Column strength
  - **B.4.1**: Elastic buckling (kL/r > Cc)
  - **B.4.2**: Inelastic buckling (kL/r ≤ Cc)
- **B.5**: Local buckling
- **B.6**: Built-up members
- **B.7**: Single angle compression

**Critical Tables:**
- **Table B.4.1**: Buckling constants (Bc, Dc, Cc) by alloy

**What You'll Find Here:**
- Column design equations
- Slenderness ratio (kL/r) calculations
- Buckling constants for each alloy
- Local buckling width-thickness limits

---

### Chapter C: Members Subject to Tension (Page 50)

**Key Sections:**
- **C.1**: Scope
- **C.2**: Tensile strength
- **C.3**: Effective net area
- **C.4**: Pin-connected members
- **C.5**: Threaded members

**What You'll Find Here:**
- Yielding: Pn = Fty × Ag
- Fracture: Pn = Ftu × Ae
- Net section calculations (bolt holes)
- Use of Fty (unwelded) or Fty(HAZ) (welded)

---

### Chapter D: Members Subject to Torsion (Page 51)

**Key Sections:**
- **D.1**: Scope
- **D.2**: Torsional strength
- **D.3**: Closed sections (tubes)
- **D.4**: Open sections

**What You'll Find Here:**
- Torsional stress equations
- Shear flow in closed sections
- Warping effects in open sections

---

### Chapter E: Members Subject to Flexure (Pages 52-53)

**Key Sections:**
- **E.1**: Scope
- **E.2**: Yielding (compact sections)
- **E.3**: Lateral-torsional buckling
- **E.4**: Local buckling
- **E.5**: Shear strength
- **E.6**: Deflection limits

**What You'll Find Here:**
- Beam design: Mn = Fty × S (if compact and braced)
- Lateral-torsional buckling (LTB)
- Width-thickness ratios for local buckling
- Recommended deflection limits (L/180, L/240, etc.)

---

### Chapter F: Members Subject to Shear (Pages 54-58)

**Key Sections:**
- **F.1**: Scope
- **F.2**: Shear strength of beams
- **F.3**: Web buckling
- **F.4**: Transverse stiffeners
- **F.5**: Combined shear and moment

**What You'll Find Here:**
- Vn = Fsu × Aw (for stocky webs)
- Web buckling equations
- Stiffener design requirements

---

### Chapter G: Flat Plates (Not Covered in Detail)

Flat plate buckling and strength.

---

### Chapter H: Members Subject to Combined Forces (Not Covered in Detail)

**Key Sections:**
- **H.1**: Beam-columns
- **H.2**: Interaction equations
- **H.3**: Axial + bending
- **H.4**: Stability effects (P-Δ)

**What You'll Find Here:**
- Interaction equations: P/Pn + M/Mn ≤ 1.0
- Second-order effects

---

### Chapter I: Composite Members (Not Covered in Detail)

Aluminum-concrete composite design.

---

### Chapter J: Connections (Detailed Coverage)

**Key Sections:**
- **J.1**: General
- **J.2**: Welds
  - **J.2.1**: Weld types (fillet, groove, etc.)
  - **J.2.2**: Weld strength
  - **J.2.3**: Base metal strength at welds
  - **J.2.4**: HAZ considerations ← **CRITICAL**
- **J.3**: Bolts
  - **J.3.1**: Bolt strength (shear, bearing)
  - **J.3.2**: Bolt hole deductions
  - **J.3.3**: Spacing requirements
- **J.4**: Rivets
- **J.5**: Special fasteners

**What You'll Find Here:**
- **HAZ properties for welded connections** (Fty reduced 40-50%)
- Weld strength by process (GMAW, GTAW)
- Bolt shear and bearing
- Minimum edge distances and spacing

**Critical:** Chapter J is where HAZ effects are codified!

---

### Chapter K: Special Members (Not Covered in Detail)

Poles, sign structures, etc.

---

### Chapter L: Serviceability (Not Covered in Detail)

Deflection, vibration, ponding.

---

### Chapter M: Fabrication (Not Covered in Detail)

Fabrication and erection requirements.

---

### Chapter N: Quality Control (Not Covered in Detail)

Inspection and testing.

---

## Part II - Commentary (Pages 99-172)

**Structure:** Mirrors Part I with commentary sections (C-A, C-B, C-C, etc.)

**Purpose:**
- Explains background and research basis
- Provides guidance on specification interpretation
- Not mandatory, but highly informative

**Key Commentary Sections:**
- **C-A**: Why aluminum is different from steel
- **C-B**: Buckling constant derivation
- **C-J**: Extensive HAZ discussion
- **C-E**: Beam design considerations

**Language:** Uses "should" and "may" (guidance, not requirements)

---

## Part III - Design Guides (Pages 173-202)

**Purpose:** Step-by-step design procedures

**Typical Contents:**
- Introduction to aluminum structural design
- Material selection flowcharts
- Worked calculation examples
- Common design situations

**Key Guides:**
- DG 1: Introduction to aluminum vs steel
- DG 2: Alloy and temper selection
- DG 3: Buckling analysis procedures

---

## Part IV - Material Properties (Pages 203-234)

**Purpose:** Complete material property tables

**Organization by:**
1. **Alloy series** (6061, 6063, 5052, 5083, etc.)
2. **Product form** (extrusions, plate, sheet, etc.)
3. **Thickness range** (0.125-1.0 in, etc.)
4. **Temper** (T4, T5, T6, H32, etc.)

**Properties Listed:**
- **Fty**: Tensile yield strength (unwelded)
- **Fty(HAZ)**: Tensile yield strength (welded)
- **Ftu**: Tensile ultimate strength (unwelded)
- **Ftu(HAZ)**: Tensile ultimate strength (welded)
- **Fcy**: Compressive yield strength
- **Fsu**: Shear ultimate strength
- **E**: Modulus of elasticity
- **Bc, Dc, Cc**: Buckling constants

**Temperature Data:** Properties at elevated temperatures (up to 400°F+)

---

## Part V - Dimensions & Properties (Pages 235-398)

**Purpose:** Geometric properties of standard aluminum sections

**Contents:**
- W-shapes (wide-flange beams)
- I-beams
- Channels (C-shapes)
- Angles (L-shapes)
- Structural tubes (HSS - Hollow Structural Sections)
- Pipe
- Custom extrusions

**Properties Listed:**
- A: Cross-sectional area
- Ix, Iy: Moments of inertia
- Sx, Sy: Section moduli
- rx, ry: Radii of gyration
- J: Torsional constant
- Cw: Warping constant
- Weight per foot

**Note:** Aluminum extrusions can be custom-designed; this part shows standard shapes.

---

## Part VII - Examples (Pages 399-470)

**Purpose:** Approximately **25 worked calculation examples**

**Example Topics:**
1. Column design (concentrically loaded)
2. Beam design (simple span)
3. Beam-column (interaction)
4. Welded connections (with HAZ)
5. Bolted connections
6. Lateral-torsional buckling
7. Local buckling verification
8. Built-up members
9. Composite members
10. Special connections
... (and more)

**Example Format:**
```
Example X.X: [Title]

Given:
- Problem statement
- Material: [Alloy-Temper]
- Geometry: [Dimensions]
- Loading: [Loads]

Required:
- Check capacity
- Design member/connection

Solution:
1. Step-by-step calculation
2. Reference to Specification sections
3. Checks and verification
4. Final answer

Commentary:
- Design notes
- Alternatives
- Common mistakes
```

**Value:** These examples are **critical learning resources** for proper application of the Specification.

---

## Part VIII - Reference Data (Pages 471-536)

**Purpose:** Supplementary reference information

**Contents:**
- Unit conversion factors (ksi ↔ MPa, in ↔ mm)
- Historical alloy data (older editions)
- AWS welding specifications
- ASTM material standards
- Fastener specifications
- Corrosion data
- Additional design aids

---

## Chapter Cross-Reference Guide

### For Different Member Types

| Member Type | Primary Chapter | Also See |
|-------------|----------------|----------|
| **Column** | B (Compression) | H (if bending present), K (special) |
| **Beam** | E (Flexure) | F (Shear), L (Deflection) |
| **Tension rod** | C (Tension) | J (if connections welded/bolted) |
| **Beam-column** | H (Combined) | B (compression) + E (flexure) |
| **Tube/HSS** | D (Torsion) | B, E, F depending on loading |
| **Plate** | G (Flat plates) | F (shear) |

### For Connection Design

| Connection Type | Primary Section | Critical Consideration |
|-----------------|----------------|----------------------|
| **Welded** | J.2 | **HAZ** - Use Fty(HAZ), not Fty! |
| **Bolted** | J.3 | Net section reduction at holes |
| **Riveted** | J.4 | Similar to bolts |
| **Mixed** | J.1, J.2, J.3 | Check all limit states |

### For Material Selection

| Question | Reference |
|----------|-----------|
| What alloys are available? | Chapter A (A.4), Part IV |
| Welded or unwelded? | Part IV tables (HAZ columns) |
| Temperature exposure? | Chapter A (A.8), Part IV elevated temp |
| Corrosion environment? | Chapter A (A.9), Commentary C-A |
| Buckling constants? | Table B.4.1, Part IV |

---

## How to Navigate for Common Tasks

### Task 1: Design a Column

**Path:**
1. **Chapter A**: Determine alloy, temper, temperature limits
2. **Chapter B**: Column design procedure
3. **Table B.4.1**: Get Bc, Dc, Cc for the alloy
4. **Part IV**: Verify Fcy (unwelded or welded)
5. **Part V**: Get section properties (A, r)
6. **Part VII**: Review Example [column example number]

---

### Task 2: Design a Welded Connection

**Path:**
1. **Chapter J, Section J.2**: Weld strength and types
2. **Chapter J, Section J.2.4**: **HAZ considerations** ← Critical!
3. **Part IV**: Get Fty(HAZ) for base metal
4. **Chapter A**: Safety factors for welds
5. **Part VII**: Review welded connection examples
6. **Part II (Commentary C-J)**: Understand HAZ background

---

### Task 3: Select Material

**Path:**
1. **Part III - Design Guides**: Alloy selection flowchart
2. **Chapter A (A.4)**: Alloy designation system
3. **Part IV**: Compare properties of candidate alloys
4. **Commentary (C-A)**: Material selection guidance
5. **Part VII**: Find examples with similar applications

---

### Task 4: Check Lateral-Torsional Buckling

**Path:**
1. **Chapter E, Section E.3**: LTB provisions
2. **Table B.4.2**: Beam buckling constants (or use B.4.1)
3. **Part V**: Get section properties (Sx, Cw, J)
4. **Part VII**: Review beam LTB examples
5. **Commentary (C-E)**: LTB background

---

## Key Tables Quick Reference

| Table | Location | Contents |
|-------|----------|----------|
| **B.4.1** | Chapter B | Column buckling constants (Bc, Dc, Cc) |
| **B.4.2** | Chapter B/E | Beam buckling constants |
| **Part IV** | Pages 203-234 | All material properties by alloy |
| **Part V** | Pages 235-398 | Section dimensions and properties |
| **A.4.1** | Chapter A | Temperature limits by temper |
| **J.2.x** | Chapter J | Weld strength and HAZ factors |

---

## Typical Workflow for a Design

```
1. Define loads (Chapter A: Load combinations)
   ↓
2. Select trial member (Part V: Section properties)
   ↓
3. Select material (Chapter A.4, Part IV)
   - Is it welded? → Use HAZ properties!
   ↓
4. Check applicable limit states:
   - Compression → Chapter B
   - Tension → Chapter C
   - Flexure → Chapter E
   - Shear → Chapter F
   - Combined → Chapter H
   ↓
5. Design connections (Chapter J)
   - Welds → J.2 (remember HAZ!)
   - Bolts → J.3
   ↓
6. Check serviceability (Chapter L)
   - Deflection limits
   ↓
7. Verify with examples (Part VII)
   ↓
8. Document calculations
```

---

## Page Number Reference (Consolidated Files)

After consolidation, the 536 pages are organized into 21 files:

### Specification (14 files)
- `Chapter_A_General.md` (Pages 29-39)
- `Chapter_B_Compression.md` (Pages 40-49)
- `Chapter_C_Tension.md` (Page 50)
- `Chapter_D_Torsion.md` (Page 51)
- `Chapter_E_Flexure.md` (Pages 52-53)
- `Chapter_F_Shear.md` (Pages 54-58)
- `Chapter_G_FlatPlates.md` (Pages 59-63)
- `Chapter_H_Combined.md` (Pages 64-69)
- `Chapter_I_Composite.md` (Pages 70-72)
- `Chapter_J_Connections.md` (Pages 73-85)
- `Chapter_K_Special.md` (Pages 86-88)
- `Chapter_L_Serviceability.md` (Pages 89-92)
- `Chapter_M_Fabrication.md` (Pages 93-96)
- `Chapter_N_QualityControl.md` (Pages 97-98)

### Commentary (1 file)
- `Part_II_Commentary.md` (Pages 99-172)

### Design Guide (1 file)
- `Part_III_Design_Guide.md` (Pages 173-202)

### Other Parts (5 files)
- `Symbols.md` (Pages 9-28)
- `Part_IV_Materials.md` (Pages 203-234)
- `Part_V_Dimensions.md` (Pages 235-398)
- `Part_VII_Examples.md` (Pages 399-470)
- `Part_VIII_Reference.md` (Pages 471-536)

---

## Search Strategy by Query Type

### Formula Queries
→ Search: Part I chapters (A-N)
→ Cross-reference: Commentary (Part II)

### Example Queries
→ Search: Part VII (Examples)
→ Verify: Part I (Specification sections cited)

### Material Properties
→ Search: Part IV (Material Properties)
→ Context: Chapter A (General provisions)

### Section Properties
→ Search: Part V (Dimensions)
→ Use with: Chapters B, E (design equations)

### Alloy Selection
→ Search: Part III (Design Guides), Commentary C-A
→ Verify: Part IV (property tables)

### HAZ/Welding
→ Search: Chapter J (Section J.2.4), Commentary C-J
→ Properties: Part IV (welded columns)

---

**Use this structure guide to navigate efficiently through the 536 pages of ADM 2020!**

---

*ADM 2020 Structure Reference*
*For detailed content, see individual consolidated files*

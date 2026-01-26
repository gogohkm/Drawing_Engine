# ADM 2020 Aluminum Design Skill

Claude Code user skill for structural aluminum design using the Aluminum Design Manual 2020 (ADM 2020).

---

## Overview

This skill provides comprehensive access to the ADM 2020 specification, commentary, design guides, and examples for structural aluminum design. It includes aluminum-specific considerations such as:

- **Heat-Affected Zone (HAZ)** strength reduction in welded members (20-60% capacity loss)
- **Alloy and temper** selection with property lookup
- **Buckling constants** that vary by alloy (unlike steel)
- **Temperature limits** for heat-treatable alloys
- **ASD-only design method** (LRFD not used in aluminum)

---

## Contents

### Data Files (21 consolidated documents)

Located in `data/` subdirectories:

**Specification (14 chapters)**
- `specification/Chapter_A_General_Provisions.md` - Materials, alloys, design basis
- `specification/Chapter_B_Design_Requirements.md` - Local buckling, slenderness
- `specification/Chapter_C_Design_for_Stability.md` - Stability provisions
- `specification/Chapter_D_Design_for_Tension.md` - Tension members
- `specification/Chapter_E_Design_for_Compression.md` - Columns, buckling
- `specification/Chapter_F_Design_for_Flexure.md` - Beams
- `specification/Chapter_G_Design_for_Shear.md` - Shear design
- `specification/Chapter_H_Combined_Forces_Torsion.md` - Interaction equations
- `specification/Chapter_J_Connections.md` - Welds, bolts, HAZ
- `specification/Chapter_L_Serviceability.md` - Deflections
- `specification/Chapter_M_Fabrication_Erection.md` - Construction
- `specification/Chapter_N_Quality_Control.md` - QA/QC
- `specification/Appendices_1_to_6.md` - Additional provisions

**Commentary**
- `commentary/Part_II_Commentary.md` - Background, research basis, guidance

**Design Guide**
- `design-guide/Part_III_Design_Guide.md` - Step-by-step design procedures

**Examples**
- `examples/Part_VII_Illustrative_Examples.md` - 31 worked calculation examples

**Reference Data**
- `reference-data/Part_IV_Material_Properties.md` - Complete property tables
- `reference-data/Part_V_Section_Properties.md` - Standard section dimensions
- `reference-data/Part_VII_Illustrative_Examples.md` - Additional examples
- `reference-data/Part_VIII_Sheet_Metal_Guidelines.md` - Sheet metal design

**Symbols**
- `Symbols.md` - Mathematical notation, glossary, front matter

---

### Reference Files (8 guides)

Located in `references/`:

**Basic References (extracted from source)**
- `symbols.md` - Mathematical symbols and notation
- `glossary.md` - Technical terms and definitions
- `abbreviations.md` - Common abbreviations (HAZ, ASD, tempers, etc.)

**Aluminum-Specific References (custom created)**
- `alloy-guide.md` - Quick reference for common alloys (6061-T6, 6063, 5052, 5083)
- `haz-factors.md` - HAZ strength reduction tables and design procedures
- `buckling-constants-guide.md` - Buckling constants by alloy/temper
- `specification-structure.md` - Navigation guide for 536-page manual
- `examples-index.md` - Index of all 31 worked examples

---

### Automation Scripts (4 tools)

Located in `scripts/`:

**1. extract_references.py** - Extract symbols, glossary from source documents
```bash
python3 scripts/extract_references.py
```

**2. smart_search.py** - Intelligent search with category filtering
```bash
# Search for HAZ information
python3 scripts/smart_search.py "HAZ" --welded-only

# Search in specific category
python3 scripts/smart_search.py "column buckling" --category specification

# Search for alloy-specific info
python3 scripts/smart_search.py "buckling constants" --alloy "6061-T6"
```

**3. alloy_lookup.py** - Material property lookup by alloy/temper
```bash
# Unwelded properties
python3 scripts/alloy_lookup.py "6061-T6"

# Welded (HAZ) properties
python3 scripts/alloy_lookup.py "6061-T6" --welded

# Buckling constants
python3 scripts/alloy_lookup.py "6061-T6" --buckling

# Compare welded vs unwelded
python3 scripts/alloy_lookup.py "6061-T6" --compare

# List all alloys
python3 scripts/alloy_lookup.py --list-alloys
```

**4. haz_calculator.py** - Calculate HAZ impact on member capacity
```bash
# Tension member
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type tension --area 5.0

# Column
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type column --area 8.0 --slenderness 40

# Beam
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type beam --section-modulus 15.0
```

---

## Key Features

### 1. HAZ (Heat-Affected Zone) Awareness

**Critical Difference from Steel:** Aluminum experiences severe strength reduction (20-60%) in welded areas due to loss of heat treatment.

- 6061-T6 welded: Fty drops from 35 ksi to 19 ksi (46% loss)
- 6063-T6 welded: Fty drops from 25 ksi to 14 ksi (44% loss)
- 5xxx series (non-heat-treatable): Minimal HAZ effect

**Examples Demonstrating HAZ:**
- Example 5: Welded pipe
- Example 11: Welded column (best HAZ example)
- Example 16-17: Welded girders with fatigue
- Example 24-25: Welded beams
- Example 27: Welded connection

### 2. Alloy Selection Guidance

**Common Structural Alloys:**

| Alloy | Strength | HAZ Effect | Best Use |
|-------|----------|------------|----------|
| 6061-T6 | High (35 ksi) | Severe (46% loss) | General structural, unwelded |
| 6063-T6 | Medium (25 ksi) | Severe (44% loss) | Architectural extrusions |
| 5052-H32 | Medium (23 ksi) | Minimal | Marine, welded structures |
| 5083-H112 | High (35 ksi) | Minimal | Best for welded structures! |

### 3. Buckling Constants by Alloy

**Unlike steel** (single buckling curve), aluminum requires alloy-specific constants:

- 6061-T6 unwelded: Bc = 30,000 ksi
- 6061-T6 welded: Bc = 16,000 ksi (47% reduction)
- 5083-H112 welded: Bc = 30,000 ksi (no change!)

### 4. Temperature Considerations

- T6/T5 tempers: 200°F limit for sustained loading
- Above 200°F: Significant strength degradation
- 5xxx series: Better temperature resistance

---

## Quick Start

### Typical Design Workflow

**1. Define Problem**
- Loading, geometry, environment
- Welded or unwelded?
- Temperature exposure?

**2. Select Alloy**
```bash
# Compare alloy options
python3 scripts/alloy_lookup.py "6061-T6"
python3 scripts/alloy_lookup.py "5083-H112"
```

**3. Find Applicable Specification**
- Tension → Chapter D
- Compression → Chapter E
- Flexure → Chapter F
- Connections → Chapter J

**4. Check HAZ Impact (if welded)**
```bash
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type column --area 8.0 --slenderness 40
```

**5. Find Similar Example**
- Reference `examples-index.md` for matching example
- Study calculation procedure

**6. Verify with Commentary**
- Read corresponding Commentary section for background

---

## Query Types Supported

The skill handles 8 types of queries:

1. **Formula Queries** - "Show me the column buckling equation"
2. **Example Queries** - "Find example of welded column design"
3. **Calculation Queries** - "Calculate capacity of 6061-T6 beam"
4. **Terminology Queries** - "What is HAZ?"
5. **Symbol Queries** - "What does Fty mean?"
6. **Alloy Lookup** - "Properties of 6061-T6 welded"
7. **HAZ/Welding** - "How much strength loss from welding?"
8. **Comparison** - "Aluminum vs steel design differences"

---

## Important Differences from Steel Design

| Aspect | Steel (AISC) | Aluminum (ADM) |
|--------|-------------|----------------|
| **Design Method** | LRFD + ASD | ASD only |
| **Modulus** | E = 29,000 ksi | E = 10,100 ksi (65% lower) |
| **Buckling** | Single curve | Alloy-dependent curves |
| **HAZ Effect** | Minimal (<5%) | Severe (20-60%) |
| **Temperature** | Stable to 600°F+ | Degradation >200°F |
| **Alloy Variations** | Minor (A36, A992) | Critical (6061, 5083, etc.) |
| **Heat Treatment** | Not applicable | Defines strength (T6, H32) |

---

## File Organization

```
.claude/skills/adm-aluminum-design/
├── SKILL.md                    # Main skill definition (Claude reads this)
├── README.md                   # This file (user documentation)
├── CHANGES.md                  # Consolidation methodology
│
├── data/                       # Source documents (21 files, 1.24 MB)
│   ├── Symbols.md
│   ├── specification/          # 14 chapter files
│   ├── commentary/             # Part II
│   ├── design-guide/           # Part III
│   ├── examples/               # Part VII (31 examples)
│   └── reference-data/         # Parts IV, V, VIII
│
├── references/                 # Quick reference guides (8 files)
│   ├── symbols.md
│   ├── glossary.md
│   ├── abbreviations.md
│   ├── alloy-guide.md          # ⭐ Aluminum-specific
│   ├── haz-factors.md          # ⭐ Aluminum-specific
│   ├── buckling-constants-guide.md
│   ├── specification-structure.md
│   └── examples-index.md
│
└── scripts/                    # Automation tools (4 scripts)
    ├── extract_references.py
    ├── smart_search.py         # Intelligent search
    ├── alloy_lookup.py         # Material properties
    └── haz_calculator.py       # HAZ capacity impact
```

---

## Common Tasks

### Find a Formula

**Method 1: Search**
```bash
python3 scripts/smart_search.py "column buckling" --category specification --verbose
```

**Method 2: Direct lookup in appropriate chapter**
- Compression → `data/specification/Chapter_E_Design_for_Compression.md`
- Section E.2 contains column strength equations

### Select Alloy for Welded Structure

**Step 1: Compare HAZ effects**
```bash
python3 scripts/alloy_lookup.py "6061-T6" --compare
python3 scripts/alloy_lookup.py "5083-H112" --compare
```

**Step 2: Calculate capacity difference**
```bash
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type column --area 10 --slenderness 50
python3 scripts/haz_calculator.py --alloy "5083-H112" --member-type column --area 10 --slenderness 50
```

**Result:** 5083-H112 shows minimal HAZ effect → Best choice for welded!

### Find Design Example

**Method 1: Use examples index**
- Read `references/examples-index.md`
- Match your problem to one of 31 examples

**Method 2: Search**
```bash
python3 scripts/smart_search.py "welded column" --category examples --verbose
```

**Method 3: Direct lookup**
- Example 11: Welded W-Shape in Axial Compression (pages 23-24)

---

## Tips for Success

### Always Verify Alloy and Condition

❌ **Wrong:** "Use aluminum beam"
✅ **Right:** "Use 6061-T6 beam, unwelded"
✅ **Right:** "Use 6061-T6 beam with HAZ properties (welded connections)"

### Check Temperature Exposure

- < 200°F → Use full properties for T6/T5
- > 200°F → Reduce properties or use non-heat-treatable alloys

### Understand HAZ Implications

**For heat-treatable alloys (6xxx):**
- Welding causes 40-50% strength loss
- HAZ extends ~0.5-1.5 inches from weld
- Consider alternatives:
  - Bolted connections (no HAZ)
  - 5xxx series alloys (minimal HAZ)

### Use Examples as Templates

All 31 examples follow consistent format:
1. GIVEN (problem statement)
2. FIND (objective)
3. SOLUTION (step-by-step with equations)
4. NOTES (design commentary)

Copy the workflow, adapt to your problem.

---

## Support

**For bugs or feature requests:**
- Submit issue at project repository

**For ADM 2020 interpretation questions:**
- Reference Part II Commentary
- Cross-check with worked examples
- Consult design guides (Part III)

**For aluminum vs steel differences:**
- See `references/` comparison tables
- Study Examples 11, 16, 17 (HAZ demonstrations)

---

## Version Information

**ADM Edition:** 2020 (January 2020)
**Skill Created:** 2025
**Data Size:** 1.24 MB (21 consolidated files from 536 original pages)
**Examples:** 31 worked calculations
**Reference Guides:** 8 aluminum-specific guides
**Automation Scripts:** 4 Python tools

---

## Credits

**Source:** Aluminum Design Manual 2020
**Publisher:** The Aluminum Association
**Consolidation:** Automated processing with quality verification
**Skill Development:** Custom aluminum-specific enhancements

---

**For detailed skill behavior, see SKILL.md**
**For consolidation methodology, see CHANGES.md**

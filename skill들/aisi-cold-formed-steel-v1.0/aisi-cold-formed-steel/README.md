# AISI Cold-Formed Steel Design Skill

Comprehensive Claude Code skill for AISI S100-16 (North American Specification for the Design of Cold-Formed Steel Structural Members) and AISI Cold-Formed Steel Design Manual 2017 Edition.

## Overview

This skill provides access to 1,173 pages of cold-formed steel design information organized into 159 searchable files with 74 worked examples.

**Version:** 1.0
**Last Updated:** 2025-11-10
**Languages:** English and Korean (한국어)

## What This Skill Can Do

- 🔍 **Search** 1,173 pages efficiently across 2 volumes
- 📖 **Find** relevant examples from 74 worked design problems
- 📊 **Lookup** specification requirements (Chapters A-M)
- 🧮 **Calculate** member capacities with working Python code
- 🔗 **Cross-reference** between specification and examples
- 📚 **Explain** design methods (ASD/LRFD/LSD) and analysis methods (EWM/DSM)
- 🔧 **Provide** steel grade properties (ASTM A1003, A653, A792)
- 💡 **Understand** buckling modes (local, distortional, global)
- 🌐 **Support** both English and Korean queries

## Covered Topics

### Structural Members
- **Beams:** Flexural design, lateral-torsional buckling, web crippling
- **Columns:** Axial compression, buckling modes, combined loading
- **Connections:** Welds, bolts, screws, power-actuated fasteners

### Design Methods
- **ASD:** Allowable Strength Design (safety factors Ω)
- **LRFD:** Load and Resistance Factor Design (resistance factors φ)
- **LSD:** Limit States Design (Canadian variant)

### Analysis Methods
- **EWM:** Effective Width Method (traditional, Appendix 1)
- **DSM:** Direct Strength Method (modern, Chapters E-G)

### Section Types
- C-sections (lipped channels)
- Z-sections
- Hat sections
- Angles
- Track, stud, deck profiles
- Built-up members

## Documents Included

### Volume 1: Design Manual (665 pages, 112 files)
- **Part I:** Dimensions and Properties (20 examples)
- **Part II:** Beam Design (20 examples with EWM/DSM variants)
- **Part III:** Column Design (19 examples with EWM/DSM variants)
- **Part IV:** Connection Design (12 examples)
- **Part V:** Supplementary Information (cross-reference table, ponding)
- **Part VI:** Test Procedures (33 ASTM standards, calibration)

### Volume 2: Specification and Commentary (508 pages, 47 files)
- **Part VII:** Specification Chapters A-M (normative requirements)
- **Part VIII:** Commentary (background, theory, 400+ references)
- **Appendices:** Effective width, elastic buckling, USA/Canada provisions

## Quick Start

### Common Queries

**Find a formula:**
```
"What is the equation for nominal moment strength?"
"Show me the DSM formula for compression"
```

**Find an example:**
```
"Example of C-section beam design using DSM"
"How to design a Z-section column"
"Screw connection example"
```

**Perform calculation:**
```
"Calculate capacity of C8x2.5x0.105 beam, Fy=50 ksi, LRFD"
"Design a column using ASTM A653 Grade 50"
```

**Lookup specification:**
```
"What are the requirements in Chapter F.3.1?"
"Specification for bolt spacing"
```

**Understand concepts:**
```
"Explain ASD vs LRFD"
"What is distortional buckling?"
"Difference between EWM and DSM"
```

### Reference Files

Quick lookup tables in `references/` folder:

- **symbols.md** - Mathematical notation and variables
- **glossary.md** - Technical term definitions
- **abbreviations.md** - Common abbreviations (EWM, DSM, ASD, LRFD)
- **examples-index.md** ⭐ - All 74 examples categorized
- **steel-grades-guide.md** - ASTM steel properties
- **design-methods-comparison.md** - ASD vs LRFD vs LSD
- **analysis-methods-comparison.md** - EWM vs DSM
- **buckling-modes-guide.md** - Local, distortional, global
- **section-types-guide.md** - C, Z, Hat, Angle sections
- **specification-structure.md** - Chapter organization
- **standards-index.md** - AISI/ASTM/CFSEI standards

### Automation Scripts

Python tools in `scripts/` folder:

1. **smart_search.py** - Category-aware keyword search
2. **example_matcher.py** ⭐ - Match queries to 74 examples
3. **formula_finder.py** - Extract formulas with context
4. **specification_lookup.py** - Quick spec section access
5. **steel_grade_lookup.py** - Material properties database
6. **cross_reference.py** - Link specification ↔ examples
7. **design_method_selector.py** - Choose ASD/LRFD/LSD, EWM/DSM

## File Organization

```
aisi-cold-formed-steel/
├── SKILL.md                 # Main skill file (900+ lines)
├── README.md                # This file
├── CHANGES.md               # Version history
│
├── data/                    # Symlinks to actual data
│   ├── vol1/                → ../../data/ (Volume 1)
│   └── vol2/                → ../../data_vol2/ (Volume 2)
│
├── references/              # Quick reference files (11 files)
│   ├── symbols.md
│   ├── examples-index.md   ⭐ Critical for example matching
│   ├── steel-grades-guide.md
│   └── ...
│
├── scripts/                 # Automation tools (7 scripts)
│   ├── smart_search.py
│   ├── example_matcher.py  ⭐ Matches queries to examples
│   └── ...
│
└── workflows/               # Design workflows (4 files)
    ├── beam-design-workflow.md
    ├── column-design-workflow.md
    ├── connection-design-workflow.md
    └── section-selection-workflow.md
```

## Key Features

### 1. Automatic Example Matching

The `example_matcher.py` script and `examples-index.md` enable automatic matching of user queries to the most relevant of 74 examples.

**Example:**
- Query: "C-section beam using Direct Strength Method"
- Match: Example II-1B (pages 175-181)

### 2. Cross-Reference System

The `Specification_Cross_Reference.md` table (pages 628-632) maps every specification section to relevant examples.

**Example:**
- Specification E.3.1 (Compression, DSM)
- → Examples: III-1B, III-5B, III-7B

### 3. Dual Method Support

Many examples show both design methods and analysis approaches:

**Design Methods:**
- Example II-1A: ASD approach
- Example II-1B: LRFD approach (same problem)

**Analysis Methods:**
- Example II-1A: Effective Width Method (EWM)
- Example II-1B: Direct Strength Method (DSM) (same problem)

### 4. Bilingual Support

Supports queries in English and Korean:

- "냉간성형강 보 설계" → Finds beam design examples
- "좌굴 모드" → Explains buckling modes
- Technical terms translated automatically

## Usage Tips

### Search Strategy

1. **Start with reference files** (fastest)
   - Check `examples-index.md` for examples
   - Check `steel-grades-guide.md` for materials
   - Check `symbols.md` for notation

2. **Use automation scripts**
   - `example_matcher.py` for finding examples
   - `smart_search.py` for keyword searches
   - `steel_grade_lookup.py` for properties

3. **Search specification** for requirements
   - Volume 2 `specification/` folder
   - Chapters A-M

4. **Read commentary** for understanding
   - Volume 2 `commentary/` folder
   - Background and theory

5. **Study examples** for application
   - Volume 1 Parts I-IV
   - 74 worked problems

### Choosing Methods

**Design Method (ASD vs LRFD vs LSD):**
- **USA modern practice:** LRFD
- **USA traditional:** ASD
- **Canada:** LSD
- See `design-methods-comparison.md`

**Analysis Method (EWM vs DSM):**
- **Standard sections, hand calcs:** EWM
- **Complex sections, computer-aided:** DSM
- See `analysis-methods-comparison.md`

### Common Section Types

- **C-section:** Lipped channel, common for purlins/girts
- **Z-section:** Cee with lips, common for purlins/girts
- **Hat section:** Deck profiles
- **Angle:** Bracing, lintels
- **Track:** Top/bottom plates (wall framing)
- **Stud:** Wall framing (C or U with punchouts)

## Example Categories

| Part | Topic | Count | Page Range |
|------|-------|-------|------------|
| I | Section Properties | 20 | 54-162 |
| II | Beam Design | 20 | 163-418 |
| III | Column Design | 19 | 419-556 |
| IV | Connection Design | 12 | 557-626 |
| V | Ponding Analysis | 1 | 627-655 |
| VI | Test Calibration | 2 | 656-664 |

**Total: 74 examples**

## Steel Grades Quick Reference

| ASTM | Grade | Fy (ksi) | Fu (ksi) | Common Use |
|------|-------|----------|----------|------------|
| A1003 | SS-33 | 33 | 45 | Light-duty |
| A1003 | SS-50 | 50 | 65 | General structural |
| A653 | Grade 50 | 50 | 65 | Galvanized framing |
| A792 | Grade 50 | 50 | 65 | Standing seam roofs |

**Material constants:**
- E (elastic modulus) = 29,500 ksi
- G (shear modulus) = 11,300 ksi

## Buckling Modes

**Local Buckling:**
- Short wavelength (plate panels)
- All thin-walled sections
- EWM uses effective width
- DSM uses F_crl

**Distortional Buckling:**
- Intermediate wavelength (lip rotation)
- C and Z sections with lips
- DSM uses F_crd
- Not directly in EWM

**Global Buckling:**
- Long wavelength (member buckling)
- Flexural, torsional, lateral-torsional
- Both EWM and DSM

**Design checks all three modes!**

## Specification Chapters

| Chapter | Topic | Key For |
|---------|-------|---------|
| A | General Provisions | Materials, loads |
| B | Design Requirements | ASD, LRFD, LSD |
| C | Stability | Direct analysis |
| D | Tension | Net section |
| E | Compression | Columns, buckling |
| F | Flexure | Beams, LTB |
| G | Shear | Shear strength, web crippling |
| H | Combined Forces | Interaction |
| I | Assemblies | Built-up members |
| J | Connections | Welds, bolts, screws |
| K | Testing | Quality control |
| L | Serviceability | Deflection |
| M | Fatigue | Cyclic loading |

## Response Quality

Every response includes:

- ✅ **Citation:** Chapter/Section/Page reference
- ✅ **Method:** ASD or LRFD or LSD
- ✅ **Approach:** EWM or DSM (when applicable)
- ✅ **Units:** Consistent throughout (ksi, in, kip)
- ✅ **Variables:** All symbols defined
- ✅ **Code:** Working Python code for calculations
- ✅ **Examples:** Related worked problems referenced

## Advanced Features

### Python Calculations

The skill can generate and execute Python code for design calculations:

```python
# Example: Beam capacity calculation
import math

# Given
Fy = 50  # ksi
S_e = 1.45  # in³ (effective section modulus)

# LRFD
phi_b = 0.95  # Bending resistance factor
M_n = S_e * Fy  # Nominal moment
phi_M_n = phi_b * M_n  # Design moment

print(f"Design flexural strength: {phi_M_n:.1f} kip-in")
```

### Cross-Referencing

Automatically link specification requirements to examples:

- User asks about "Chapter E.3.1"
- Skill provides specification text
- Skill lists related examples: III-1B, III-5B
- User can then read those examples

### Multi-Volume Integration

Seamlessly search across both volumes:

- Volume 1: Practical examples
- Volume 2: Code requirements and theory
- Skill navigates both automatically

## Limitations

**Not covered:**
- Hot-rolled steel (use AISC 360)
- Concrete (use ACI 318)
- Aluminum (use ADM - separate skill available)
- Wood (use NDS)

**Out of scope:**
- Structural analysis (use MASTAN2, SAP2000, etc.)
- Detailing and drafting
- Cost estimating
- Construction methods (beyond Chapter K quality control)

## Support

For issues, questions, or enhancements related to this skill:

1. Check SKILL.md for detailed workflows
2. Review reference files for quick answers
3. Run automation scripts for complex queries
4. Read relevant examples for application guidance

## Version History

See `CHANGES.md` for detailed version history.

**Current Version: 1.0 (2025-11-10)**
- Initial release
- Complete AISI S100-16 coverage
- 74 examples indexed
- 7 automation scripts
- 11 reference files
- Bilingual support (English/Korean)

## Credits

**Documents:**
- AISI S100-16 (North American Specification for the Design of Cold-Formed Steel Structural Members, 2016 Edition)
- AISI Cold-Formed Steel Design Manual, 2017 Edition
- American Iron and Steel Institute (AISI)

**License:**
- Licensed for Han KyongMin by AISI, November 16, 2023
- Single user license only
- Storage, distribution or use on network prohibited

**Skill Author:** Claude Code (Anthropic)
**Skill Version:** 1.0
**Last Updated:** 2025-11-10

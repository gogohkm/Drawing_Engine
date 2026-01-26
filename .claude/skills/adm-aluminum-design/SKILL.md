---
name: adm-aluminum-design
description: "ADM2020 알루미늄 설계 매뉴얼(Specification, Commentary, Design Guide, Examples)을 검색하고 구조계산을 수행하며, 설계 워크플로우를 제공합니다. 알루미늄 구조설계, 6061-T6/6063-T5 합금, 템퍼 지정, 열영향부(HAZ), 좌굴상수, ASD 설계 관련 질문에 즉시 활성화되며, 공식 추출, 예제 매칭, 합금별 계산, 용어 설명, 기호 정의를 지원합니다."
---

# ADM Aluminum Design Standards Expert

Use this skill when users ask questions about aluminum structural design, ADM 2020, alloy properties, temper designations, heat-affected zones (HAZ), buckling constants, or any aluminum construction related queries.

## Trigger Keywords

**English**: ADM, aluminum design, aluminium, aluminum structures, alloy, 6061-T6, 6063-T5, 5xxx series, temper, T4, T5, T6, H112, heat-affected zone, HAZ, welding aluminum, buckling constants, allowable stress design, ASD, aluminum beam, aluminum column, aluminum connection, extrusion, aluminum alloy, Aluminum Association, Specification for Aluminum Structures

**Korean**: ADM, 알루미늄설계, 알루미늄구조, 알루미늄, 합금, 6061, 6063, 템퍼, 열영향부, HAZ, 용접, 좌굴상수, 허용응력설계, 압출재

## Tools Required

- **Grep**: Search for keywords in ADM documents
- **Read**: Read specific chapters and reference files
- **Glob**: Pattern matching to find files
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results or reports

## Document Structure

This skill provides access to **comprehensive aluminum design documentation**:

### 1. ADM 2020 Specification (Part I - Design Requirements)
**Location**: `data/specification/*.md` (13 chapter files + appendices)

**Purpose**: What you **must** follow - formulas, requirements, limits, design criteria

**Chapters**:
- **A**: General Provisions (scope, materials, alloys, tempers)
- **B**: Design Requirements (loads, analysis, elements, buckling constants)
- **C**: Stability (second-order analysis, P-delta effects)
- **D**: Tension Members (tensile strength, net area)
- **E**: Compression Members (flexural buckling, local buckling, alloy-dependent)
- **F**: Flexural Members (yielding, lateral-torsional buckling, section classification)
- **G**: Shear Members (shear strength, web design)
- **H**: Combined Forces (interaction equations, torsion)
- **J**: Connections (welds with HAZ, bolts, rivets, screws, bearing)
- **L**: Serviceability (deflection limits - critical for aluminum's lower E)
- **M**: Fabrication (fabrication and erection requirements)
- **N**: Quality (QC/QA requirements)
- **Appendices 1-6**: Testing, Fatigue, Structural Analysis, Evaluation, Bracing

### 2. Commentary (Part II - Background and Rationale)
**Location**: `data/commentary/Part_II_Commentary.md` (244 KB)

**Purpose**: Understand **why** - background, research basis, design considerations

**Contents**: Detailed commentary on each Specification chapter with:
- Historical development
- Research background
- Design examples and comparisons
- Limit state explanations
- Special considerations for aluminum

### 3. Design Guide (Part III - Practical Guidance)
**Location**: `data/design-guide/Part_III_Design_Guide.md` (76 KB)

**Purpose**: **How to apply** - practical design workflow

**Topics**:
1. Introduction to aluminum design
2. Section Selection (considering aluminum's properties)
3. Bending Members (deflection often controls)
4. Compression Members (local buckling critical)
5. Combined Loading
6. Connections (HAZ effects crucial)
7. Serviceability (E = 10,100 ksi vs steel's 29,000 ksi)
8. Sustainability (recyclability, energy efficiency)

### 4. Illustrative Examples (Part VII - Step-by-Step Calculations)
**Location**: `data/examples/Part_VII_Illustrative_Examples.md` (153 KB)

**Purpose**: See **worked examples** with complete calculations

**Examples** (~25 examples covering):
- Tension members (rods, bars with HAZ effects)
- Flexural members (W-shapes, tubes, pipes, plates)
- Connections (rivets, pins, welds with HAZ reduction)
- Compression members (various sections, local buckling)
- Combined loading scenarios

### 5. Reference Data (Parts IV, V, VIII)
**Location**: `data/reference-data/`

- **Part IV - Material Properties** (114 KB): Alloy-specific mechanical properties
  - Tables for 6061-T6, 6063-T5, 5xxx series, etc.
  - Unwelded vs welded (HAZ) strengths
  - Temperature-dependent properties
  - Buckling constants by alloy and temper

- **Part V - Section Properties** (360 KB): Geometric properties
  - I-beams, channels, angles, tubes (round and rectangular)
  - A, I, S, Z, r values
  - Standard aluminum sections

- **Part VIII - Sheet Metal Guidelines** (38 KB): Building construction
  - Flashing details
  - Installation requirements
  - Design considerations for sheet metal

**Key Distinction**:
- **Specification** → "What formula should I use?" "What are the limits?"
- **Commentary** → "Why is this requirement needed?" "What's the background?"
- **Design Guide** → "How do I start a design?" "What's the workflow?"
- **Examples** → "Show me a complete calculation step-by-step"
- **Reference Data** → "What are the properties of 6061-T6?" "What sections are available?"

## Reference Files

This skill includes comprehensive reference materials:

- `references/symbols.md`: Complete symbols table (mathematical notation)
- `references/glossary.md`: Technical terms and definitions
- `references/abbreviations.md`: HAZ, ASD, ASTM, AWS, etc.
- `references/specification-structure.md`: Chapter structure and section mapping
- `references/examples-index.md`: Complete example index (~25 examples)
- `references/alloy-guide.md`: **Quick reference for common aluminum alloys**
- `references/haz-factors.md`: **Welding strength reduction factors by alloy**
- `references/buckling-constants-guide.md`: **Quick lookup for Tables B.4.1, B.4.2, B.5.1**

## Automation Scripts

Python scripts are available in `scripts/` directory:
- `smart_search.py`: Category-aware keyword search
- `formula_finder.py`: Extract formulas with context
- `example_matcher.py`: Match user queries to appropriate examples
- `alloy_lookup.py`: **Material properties lookup by alloy/temper**
- `haz_calculator.py`: **Calculate welded member strengths with HAZ**
- `extract_references.py`: Extract reference materials from documents

---

# Workflow by Query Type

## 1. Formula Query (공식 질의)

**User Intent**: Find a specific formula or equation from ADM Specification.

**Example Queries**:
- "What is the formula for flexural strength of aluminum beams?"
- "Show me the compression buckling equation"
- "알루미늄 보의 휨강도 공식을 알려줘"

**Quick Process**:
1. Identify topic (flexure → Chapter F, compression → Chapter E, etc.)
2. Grep relevant chapter file in `data/specification/`
3. Extract formula with variable definitions from `references/symbols.md`
4. **Note alloy dependency**: Check if formula uses buckling constants from Table B.4.1/B.4.2
5. Present with ADM citation (e.g., "ADM 2020 Section F.2")

**Keywords**: formula, equation, 공식, 계산식

---

## 2. Design Example Query (예제 질의)

**User Intent**: See a step-by-step worked example of a design calculation.

**Example Queries**:
- "Show me how to design an aluminum I-beam for flexure"
- "I need an example of column design with aluminum"
- "알루미늄 연결부 설계 예제를 보여줘"

**Quick Process**:
1. Check `references/examples-index.md` for example number
2. Identify appropriate example (e.g., Example 3: W-shape beam design)
3. Read from `data/examples/Part_VII_Illustrative_Examples.md`
4. Present step-by-step with complete calculations
5. Note any alloy-specific considerations (HAZ, temper, buckling constants)

**Keywords**: example, 예제, how to, step-by-step, 설계과정

---

## 3. Calculation Query (계산 질의)

**User Intent**: Perform structural calculations using ADM formulas with alloy-specific considerations.

**Example Queries**:
- "Calculate flexural strength: I-beam 6061-T6, welded, Lb=10ft"
- "Determine column capacity: Tube 6063-T5, unwelded, KL=8ft"
- "용접된 6061-T6 보의 휨강도를 계산해줘"

**Quick Process**:
1. **Identify alloy and temper** - CRITICAL for aluminum
2. **Check welded vs unwelded** - HAZ reduces strength 20-60%
3. Find formula from Specification (use Formula Query workflow)
4. Look up material properties:
   - Option A: Use `alloy_lookup.py` script
   - Option B: Search `data/reference-data/Part_IV_Material_Properties.md`
5. Get buckling constants from Table B.4.1 or B.4.2 (alloy-dependent)
6. Find similar example from Part VII for methodology
7. Generate Python code following example structure
8. Execute and validate against ADM limits

**Aluminum-Specific Checks**:
- ✅ Alloy specified (6061-T6, 6063-T5, etc.)
- ✅ Temper verified (T4, T5, T6, H112, etc.)
- ✅ Welded status confirmed (affects strength significantly)
- ✅ Temperature exposure checked (T5/T6 degrade > 200°F)
- ✅ Buckling constants looked up (alloy-dependent)
- ✅ HAZ strength reduction applied if welded

**Keywords**: calculate, compute, determine, 계산, 산정, 구해줘

---

## 4. Terminology Query (용어 설명)

**User Intent**: Understand the meaning and context of aluminum design terminology.

**Example Queries**:
- "What is a temper designation?"
- "Explain heat-affected zone (HAZ)"
- "허용응력설계법이 뭐야?"

**Quick Process**:
1. Check `references/glossary.md` first
2. If not found, search "Glossary" sections in Specification or Commentary
3. Present definition with ADM citation
4. Provide usage examples from Specification chapters
5. **For aluminum-specific terms**: Explain material science background

**Aluminum-Specific Terms**:
- Temper: Heat treatment condition (T4, T5, T6 for heat-treatable; H for strain-hardened)
- HAZ: Heat-Affected Zone - area near welds with reduced strength
- Alloy designation: 4-digit number (first digit = major alloying element)
- Buckling constants: Bc, Dc, Cc - vary by alloy and temper

**Keywords**: what is, explain, definition, 뭐야, 설명, 의미

---

## 5. Symbol/Notation Query (기호 질의)

**User Intent**: Understand what a mathematical symbol represents.

**Example Queries**:
- "What does Fty mean?"
- "Define Cb lateral-torsional buckling factor"
- "Bc 기호는 무엇을 의미하나요?"

**Quick Process**:
1. Check `references/symbols.md`
2. Return: Symbol | Definition | Units | Section Reference
3. Example: *Fty* = Tensile yield strength | ksi | Section A.4, Tables in Part IV
4. **For buckling constants**: Reference Tables B.4.1, B.4.2 by alloy

**Common Aluminum Symbols**:
- Fty = Tensile yield strength (varies by alloy: 16-50 ksi)
- Ftu = Tensile ultimate strength
- Fcy = Compressive yield strength (often = Fty for aluminum)
- E = Modulus of elasticity = 10,100 ksi (vs 29,000 for steel)
- Bc, Dc, Cc = Buckling constants (alloy and temper dependent)

**Keywords**: symbol, notation, 기호, 표기

---

## 6. Alloy Lookup Query (합금 조회 - ALUMINUM-SPECIFIC)

**User Intent**: Find material properties for a specific aluminum alloy and temper.

**Example Queries**:
- "What is the yield strength of 6061-T6?"
- "Properties of 6063-T5 welded vs unwelded"
- "6061-T6의 인장강도는 얼마야?"

**Quick Process**:
1. Identify alloy and temper from query
2. Check `references/alloy-guide.md` for quick reference
3. For detailed data, search `data/reference-data/Part_IV_Material_Properties.md`
4. Return properties:
   - **Unwelded**: Fty, Ftu, Fcy, Fsu, E
   - **Welded (HAZ)**: Fty(HAZ), Ftu(HAZ), etc. (significantly reduced)
   - Temperature limits
   - Typical applications
5. Use `scripts/alloy_lookup.py` for automated lookup

**Common Alloys Quick Reference**:

| Alloy | Temper | Fty (unwelded) | Fty (welded/HAZ) | Reduction | Applications |
|-------|--------|----------------|------------------|-----------|--------------|
| 6061 | T6 | 35 ksi | 19 ksi | 46% | General structural, most common |
| 6061 | T4 | 16 ksi | - | - | Lower strength, higher formability |
| 6063 | T6 | 25 ksi | 14 ksi | 44% | Architectural extrusions |
| 6063 | T5 | 16 ksi | 9 ksi | 44% | Lower strength architectural |
| 5xxx | H112 | 16-35 ksi | minimal | - | Marine, non-heat-treatable |

**Keywords**: alloy, properties, 6061, 6063, temper, strength, 합금, 물성

---

## 7. HAZ/Welding Query (열영향부 질의 - ALUMINUM-SPECIFIC)

**User Intent**: Understand or calculate effects of welding on aluminum strength.

**Example Queries**:
- "How much does welding reduce 6061-T6 strength?"
- "Calculate beam capacity for welded aluminum section"
- "용접된 알루미늄의 강도 감소율은?"

**Quick Process**:
1. Identify alloy and temper
2. Check `references/haz-factors.md` for reduction factors
3. For design calculations:
   - Use welded (HAZ) properties from Part IV
   - Apply to relevant formulas
   - Note that HAZ width varies by welding process
4. Cross-reference with Chapter J (Connections) for weld design
5. Use `scripts/haz_calculator.py` for automated calculations

**HAZ Strength Reduction Factors**:

| Alloy-Temper | Fty Reduction | Ftu Reduction | Notes |
|--------------|---------------|---------------|-------|
| 6061-T6 | ~46% (0.54 factor) | ~37% (0.63 factor) | Most significant |
| 6061-T4 | minimal | minimal | Already in annealed state |
| 6063-T6 | ~44% (0.56 factor) | ~33% (0.67 factor) | Similar to 6061 |
| 6063-T5 | ~44% (0.56 factor) | ~44% (0.56 factor) | |
| 5xxx-H112 | minimal | minimal | Non-heat-treatable |

**Critical Design Considerations**:
- Welding **heat-treatable** alloys (6xxx-T6/T5) → significant strength loss
- Welding **non-heat-treatable** alloys (5xxx-H) → minimal loss
- Post-weld heat treatment can restore strength (complex, often not practical)
- HAZ zone width: typically 0.5-1.5 inches from weld centerline

**Keywords**: welding, HAZ, heat-affected zone, weld, strength reduction, 용접, 열영향부

---

## 8. Comparison Query (비교 질의)

**User Intent**: Compare aluminum design with steel, or compare different aluminum alloys.

**Example Queries**:
- "Aluminum vs steel structural design differences"
- "Compare 6061-T6 and 6063-T5"
- "알루미늄과 철골 설계의 차이는?"

**Quick Process**:
1. Identify items to compare
2. For aluminum vs steel:
   - Material properties (E, density, strength)
   - Design philosophy (ASD only vs LRFD+ASD)
   - Welding effects (HAZ critical vs minimal)
   - Temperature sensitivity
3. For alloy comparison:
   - Use `references/alloy-guide.md`
   - Compare strength, weldability, applications
4. Present in comparison table format

**Aluminum vs Steel Quick Comparison**:

| Property | Aluminum (typical 6061-T6) | Steel (A36) | Ratio |
|----------|---------------------------|-------------|-------|
| E (modulus) | 10,100 ksi | 29,000 ksi | 1:2.9 (stiffer) |
| Density | 0.098 lb/in³ | 0.284 lb/in³ | 1:2.9 (lighter) |
| Yield strength | 35 ksi (unwelded) | 36 ksi | similar |
| HAZ effect | -46% (welded) | minimal | critical difference |
| Thermal expansion | 13×10⁻⁶/°F | 6.5×10⁻⁶/°F | 2:1 (higher) |
| Design method | ASD only | LRFD + ASD | simpler |

**Keywords**: compare, difference, vs, 차이, 비교, aluminum vs steel

---

# Quick Reference Tables

## Document Categories

| Type | Location | Files | Purpose |
|------|----------|-------|---------|
| **Specification** | data/specification/ | 13 + App | Formulas, limits, requirements |
| **Commentary** | data/commentary/ | 1 | Background, rationale, research |
| **Design Guide** | data/design-guide/ | 1 | Practical workflow guidance |
| **Examples** | data/examples/ | 1 (~25 ex) | Step-by-step calculations |
| **Material Properties** | data/reference-data/ | Part IV | Alloy properties, HAZ factors |
| **Section Properties** | data/reference-data/ | Part V | Geometric properties |
| **Sheet Metal Guide** | data/reference-data/ | Part VIII | Building applications |
| **References** | references/ | 8 | Symbols, glossary, alloy guide |

## Common Search Patterns

| Topic | Keywords | Specification Chapter | Examples Location | Unique Considerations |
|-------|----------|----------------------|-------------------|----------------------|
| **Beam Design** | flexure, bending, Cb, Lb, yielding | Chapter F | Part VII Ex 3-6 | Deflection often controls (low E) |
| **Column Design** | compression, buckling, KL/r, slenderness | Chapter E | Part VII Ex 9-14 | Local buckling critical, alloy-dependent |
| **Tension Members** | tension, net area, gross area, yielding | Chapter D | Part VII Ex 1-2 | HAZ if welded connections |
| **Shear** | shear strength, web | Chapter G | Part VII (various) | Similar to steel approach |
| **Connections** | bolts, welds, rivets, screws, bearing | Chapter J | Part VII Ex 7-8 | **HAZ critical for welds** |
| **Material Lookup** | alloy, 6061, 6063, properties | Part IV | - | **Alloy and temper specific** |
| **Stability** | second-order, P-delta | Chapter C, Appendix 4 | Part VII (some) | Similar to steel |
| **Serviceability** | deflection, vibration | Chapter L | Design Guide | **Critical due to low E** |

## ADM Chapter-to-Example Mapping

| Spec Chapter | Topic | Part VII Examples | Key Considerations |
|--------------|-------|-------------------|-------------------|
| A | General | - | Alloys, tempers, materials |
| B | Design Requirements | - | Buckling constants (alloy-dependent) |
| C | Stability | Various | Similar to steel approach |
| D | Tension | Example 1-2 | HAZ for welded |
| E | Compression | Example 9-14 | Local buckling, alloy-dependent |
| F | Flexure | Example 3-6 | Deflection often controls |
| G | Shear | Various | Similar to steel |
| H | Combined Forces | Various | Similar to steel |
| J | Connections | Example 7-8 | **HAZ for welds critical** |
| L | Serviceability | Design Guide Part 7 | **E = 10,100 ksi (1/3 of steel)** |
| M | Fabrication | - | Temperature limits for tempers |
| N | Quality | - | Similar to steel |

## Units Convention

| Quantity | ADM Unit | Symbol | Notes |
|----------|----------|--------|-------|
| Force | kips | kip | 1 kip = 1000 lbs (same as AISC) |
| Moment | kip-in | kip-in | Typically inch-based |
| Stress | ksi | ksi | 1 ksi = 1 kip/in² |
| Length | inches | in | Metric also available |
| Area | square inches | in² | - |
| Modulus | ksi | ksi | **E = 10,100 ksi for aluminum** |
| Temperature | °F | °F | Critical for T5/T6 tempers |

---

# Performance Optimization

## Search Strategy Priority

1. **Alloy-specific queries first**: Always identify alloy/temper before proceeding
   - Quick check: `references/alloy-guide.md`
   - Detailed: `data/reference-data/Part_IV_Material_Properties.md`
   - Script: `scripts/alloy_lookup.py`

2. **Reference files before full search**:
   - Symbols → `references/symbols.md`
   - Terms → `references/glossary.md`
   - Examples → `references/examples-index.md`
   - Alloys → `references/alloy-guide.md`
   - HAZ → `references/haz-factors.md`
   - Buckling → `references/buckling-constants-guide.md`

3. **Efficient chapter targeting**:
   - Use topic keywords to identify specific chapter
   - Don't search all files - target 1-2 relevant chapters
   - Example: "aluminum beam design" → Only search Chapter_F + Part VII examples

4. **Smart document reading**:
   - Read only relevant sections
   - Use offset and limit parameters for large files
   - Cross-reference between Specification, Commentary, and Examples when needed

## Python Script Usage

Execute automation scripts when appropriate:

```bash
# Material properties lookup
python3 scripts/alloy_lookup.py "6061-T6" --welded

# HAZ strength calculation
python3 scripts/haz_calculator.py --alloy "6061-T6" --member-type "beam"

# Category-aware search
python3 scripts/smart_search.py "lateral-torsional buckling"

# Extract formula with context
python3 scripts/formula_finder.py "Mn =" "Chapter_F"

# Find matching example
python3 scripts/example_matcher.py "aluminum beam" "flexure"
```

---

# Response Quality Checklist

Every response should include:

- ✅ **Accurate ADM citation** (ADM 2020 Section X.Y or Example Z)
- ✅ **Alloy and temper specified** (6061-T6, 6063-T5, etc.)
- ✅ **Welded vs unwelded clarified** (HAZ effects noted)
- ✅ **Temperature limits checked** if applicable (T5/T6 > 200°F)
- ✅ **Units specified** (ksi, in, kip, °F)
- ✅ **Variable definitions** from symbols.md
- ✅ **Buckling constants verified** (alloy-dependent Tables B.4.1, B.4.2)
- ✅ **Working Python code** for calculations (tested and validated)
- ✅ **Cross-references** to examples when explaining formulas
- ✅ **Limit states noted** (yielding, buckling, rupture, etc.)

---

# Special Features: Aluminum-Specific Considerations

## Critical Differences from Steel Design

### 1. Material Property Variations
**Steel**: Relatively uniform (Fy = 36, 50, or 65 ksi)
**Aluminum**: Highly variable by alloy/temper (Fty = 5-50 ksi)

→ **Always verify alloy and temper** before any calculation

### 2. Welding Effects (HAZ)
**Steel**: Minimal strength reduction from welding
**Aluminum**: **20-60% strength reduction** in heat-affected zone

→ **Check welded vs unwelded** for all welded members

### 3. Modulus of Elasticity
**Steel**: E = 29,000 ksi
**Aluminum**: E = 10,100 ksi (35% of steel)

→ **Deflection often controls** aluminum design (not strength)

### 4. Temperature Sensitivity
**Steel**: Strength stable up to ~400°F
**Aluminum**: T5/T6 tempers lose strength above 200°F

→ **Check temperature exposure** for heat-treated alloys

### 5. Buckling Constants
**Steel**: Standard formulas (uniform)
**Aluminum**: **Alloy-dependent tables** (Bc, Dc, Cc vary)

→ **Look up buckling constants** by alloy from Tables B.4.1, B.4.2

### 6. Design Method
**Steel AISC**: LRFD + ASD (dual methods)
**Aluminum ADM**: ASD only (single method)

→ **Simpler design approach** (no LRFD resistance factors)

## Alloy Selection Guide

**For General Structural Use**:
- **6061-T6**: Most common, good strength (Fty=35 ksi), weldable (with HAZ consideration)
- **6061-T4**: Lower strength (Fty=16 ksi), better formability, less HAZ effect

**For Architectural/Extrusions**:
- **6063-T6**: Moderate strength (Fty=25 ksi), excellent extrudability
- **6063-T5**: Lower strength (Fty=16 ksi), good surface finish

**For Marine/Corrosive Environments**:
- **5xxx-H112**: Non-heat-treatable, excellent corrosion resistance, minimal HAZ

**For High Strength**:
- **7xxx series**: Highest strength (not extensively covered in ADM 2020)

## When to Use Specification vs Commentary vs Design Guide vs Examples

**Use Specification when**:
- User asks "what is the formula?"
- User needs official requirements or limits
- User wants to understand code provisions
- User asks about limit states or design criteria

**Use Commentary when**:
- User asks "why is this required?"
- User needs background or research basis
- User wants to understand design philosophy
- User asks "what's the history of this provision?"

**Use Design Guide when**:
- User asks "how do I start a design?"
- User needs overall workflow guidance
- User wants practical tips and recommendations
- User asks "what should I consider?"

**Use Examples when**:
- User asks "how do I calculate this?"
- User needs step-by-step procedure
- User wants to see complete worked solution
- User asks "show me a calculation"

**Use Material Properties (Part IV) when**:
- User asks about alloy properties
- User needs HAZ factors
- User wants to compare alloys
- User needs buckling constants

**Use All Together when**:
- Comprehensive design questions
- Teaching/learning scenarios
- Formula explanation with practical context
- Validation of calculations

---

# Error Handling

## Common Scenarios

1. **Alloy not specified**:
   - Ask user: "Which aluminum alloy? (e.g., 6061-T6, 6063-T5)"
   - Offer common options: 6061-T6 (most common), 6063-T5 (architectural)

2. **Welded status unclear**:
   - Ask user: "Is this member welded? (HAZ reduces strength 20-60%)"
   - Explain HAZ implications

3. **No results found**:
   - Suggest alternative keywords
   - Check all document types (Spec, Commentary, Guide, Examples)
   - Recommend broader search terms

4. **Ambiguous query**:
   - Clarify with multiple interpretations
   - Ask user: "Did you mean [option A] or [option B]?"

5. **Missing parameters**:
   - List required values for calculation
   - Offer typical default values from examples

6. **Out of scope**:
   - Clearly state limitations (no FEM, no legal advice)
   - Suggest consulting structural engineer for complex cases

## Validation Checks

For all calculations:
- ✅ Verify alloy and temper specified
- ✅ Check welded vs unwelded status
- ✅ Verify units consistency (ksi, in, kip)
- ✅ Check against ADM limits (Fty ranges, buckling constants)
- ✅ Verify temperature exposure (< 200°F for T5/T6)
- ✅ Warn if parameters outside typical ranges
- ✅ Note all assumptions (bracing, load cases, HAZ extent)
- ✅ Cross-check with example from Part VII when possible

---

# Special Notes

## ASD (Allowable Strength Design) - Only Method

Unlike AISC steel design which offers both LRFD and ASD, ADM 2020 uses **ASD only**:

**ASD Method**:
- Allowable strength = Nominal strength / Ω (safety factor)
- Load combinations from ASCE/SEI 7 (D + L, D + L + W, etc.)
- Safety factors (Ω) vary by limit state:
  - Ω = 1.65 for flexure
  - Ω = 1.95 for compression
  - Ω = 1.95 for tension
  - Ω = 1.60 for shear
  - (See each chapter for specific values)

**No LRFD**: ADM does not provide LRFD resistance factors (φ). If user asks about LRFD, explain that aluminum design uses ASD only.

## Design Examples Format

- Examples show **complete step-by-step calculations**
- Example numbering: **Number** or **Number-Letter** (e.g., Example 3, Example 14A)
- All examples cite specific Specification sections
- Results presented to **appropriate significant figures**
- **HAZ effects shown** when welded members are designed

## Version Tracking

- Specification: **ADM 2020** (January 2020 edition)
- Published by: **The Aluminum Association**
- Always cite version in responses

## Material Defaults (if not specified by user)

Unless specified otherwise, assume:
- Alloy: 6061-T6 (most common structural aluminum)
- Condition: Unwelded (unless connection design implies welding)
- Temperature: Room temperature (< 200°F)
- E = 10,100 ksi (modulus of elasticity for aluminum)

**Always ask user to confirm** if critical to calculation.

---

For comprehensive aluminum structural design work, this skill integrates:
1. **Code requirements** from ADM 2020 Specification
2. **Background understanding** from Commentary
3. **Practical workflow** from Design Guide
4. **Worked applications** from Illustrative Examples
5. **Material data** from Properties tables
6. **Section properties** from geometric tables
7. **Alloy-specific tools** (HAZ calculator, property lookup)

**Always prioritize accuracy, cite sources, validate alloy/temper, check HAZ effects, and follow ASD methodology.**

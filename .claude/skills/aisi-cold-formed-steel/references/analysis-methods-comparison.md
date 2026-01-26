# Analysis Methods Comparison: EWM vs DSM

Comparison of Effective Width Method (EWM) and Direct Strength Method (DSM) for accounting for local buckling in cold-formed steel design per AISI S100-16.

**Both methods are equally valid** and approved by the specification.

---

## Overview

AISI S100-16 provides **two methods** for analyzing the effects of local buckling:

1. **EWM** - Effective Width Method (traditional, since 1946)
2. **DSM** - Direct Strength Method (modern, since 2004)

**Key difference:** How local buckling is accounted for in strength calculations.

---

## Effective Width Method (EWM)

### Location in Specification
- **Appendix 1:** Design of Elements Using Effective Width
- Referenced in main Specification (Chapters C-J)

### Fundamental Concept

**Thin compression elements buckle locally before yielding.**

Solution: **Reduce the width** of slender elements to an "effective width" that can reach yield stress.

**Winter's Formula (1946):**
```
b_e = ρ w
```

where:
- b_e = effective width
- w = flat width of element
- ρ = reduction factor

**Reduction factor:**
```
ρ = 1.0                           when λ ≤ 0.673
ρ = (1 - 0.22/λ) / λ              when λ > 0.673
```

**Element slenderness:**
```
λ = √(f / F_crl)
```

where:
- f = stress in element
- F_crl = elastic local buckling stress = (kπ²E) / (12(1-μ²)(w/t)²)
- k = plate buckling coefficient (depends on boundary conditions)

### Procedure

1. Calculate slenderness λ for each compression element
2. Determine reduction factor ρ
3. Calculate effective widths b_e
4. Compute effective section properties (A_e, I_e, S_e)
5. Use effective properties in strength equations

**Iteration required:** Stress f depends on section properties, which depend on effective width, which depends on stress!

### Pros
- ✅ Well-established (75+ years)
- ✅ Simple concept (reduced width)
- ✅ Hand-calculable
- ✅ Conservative
- ✅ Works for standard sections
- ✅ Widely accepted
- ✅ No special software needed

### Cons
- ❌ Cumbersome for complex sections
- ❌ Requires iteration
- ❌ Doesn't directly address distortional buckling
- ❌ More conservative (less economical)
- ❌ Element-by-element (tedious for many elements)

---

## Direct Strength Method (DSM)

### Location in Specification
- **Integrated in main Specification:**
  - Chapter E (Compression): Sections E3, E4
  - Chapter F (Flexure): Sections F3, F4
  - Chapter G (Shear): Section G2.2
  - Chapter H (Combined): Section H1.1

### Fundamental Concept

**Use elastic critical buckling loads directly in strength curves.**

Solution: **Calculate critical loads for each mode**, then apply strength reduction curves (similar to column curves).

**Three modes:**
1. **Local (L):** Plate buckling
2. **Distortional (D):** Flange/lip rotation
3. **Global (Euler):** Member buckling

**Nominal strength is minimum of three modes:**
```
P_n = min(P_nl, P_nd, P_ne)   (for compression)
M_n = min(M_nl, M_nd, M_ne)   (for flexure)
```

### Critical Loads Required

**Must determine:**
- F_crl or M_crl or P_crl = Local buckling
- F_crd or M_crd or P_crd = Distortional buckling
- F_cre or M_cre or P_cre = Global (Euler) buckling

**How to get critical loads:**
- Finite strip analysis (CUFSM, THIN-WALL)
- Finite element analysis
- Rational analysis
- Design tables/charts

### Strength Curves

**For compression (local buckling example):**

```
λ_l = √(F_y / F_crl)    (local slenderness)

If λ_l ≤ 0.776:
    P_nl = P_ne

If λ_l > 0.776:
    P_nl = [1 - 0.15(P_crl/P_ne)^0.4] (P_crl/P_ne)^0.4 P_ne
```

**Similar curves for distortional and flexure.**

### Procedure

1. Calculate gross section properties (A, I, S, etc.)
2. Determine elastic critical loads (F_crl, F_crd, F_cre)
3. Calculate slenderness parameters (λ_l, λ_d)
4. Apply strength curves to get nominal strengths for each mode
5. Take minimum of three modes

**No iteration!** (unless using approximate methods for F_crl)

### Pros
- ✅ Modern, optimized (less conservative)
- ✅ Unified approach (all modes treated similarly)
- ✅ Directly addresses distortional buckling
- ✅ Better for unusual/complex sections
- ✅ No iteration required
- ✅ More economical designs
- ✅ Section-based (not element-by-element)

### Cons
- ❌ Requires elastic buckling analysis (software)
- ❌ Less familiar to some engineers
- ❌ Need tables/charts or FEA for critical loads
- ❌ More complex theory

---

## Comparison Table

| Aspect | EWM | DSM |
|--------|-----|-----|
| **Year introduced** | 1946 (Winter) | 2004 (Schafer) |
| **Specification location** | Appendix 1 | Chapters E, F, G, H |
| **Philosophy** | Reduce width | Reduce strength |
| **Local buckling** | Effective width b_e | Strength curve with F_crl |
| **Distortional buckling** | Not directly addressed | Strength curve with F_crd |
| **Global buckling** | Same as DSM | Euler/LTB formulas |
| **Iteration** | Yes (stress/properties) | No |
| **Hand calculation** | Possible | Difficult (need F_cr) |
| **Software needed** | No | Yes (for F_cr) |
| **Conservatism** | More conservative | Less conservative |
| **Complexity** | Element-by-element | Section-based |
| **Best for** | Standard sections | Complex/unusual sections |
| **Design tables** | Available | Limited (growing) |

---

## Which Method to Use?

### Use EWM when:
- ✅ **Standard sections** (C, Z, angle) from manufacturers
- ✅ **Hand calculations** preferred
- ✅ **No elastic buckling software** available
- ✅ **Conservative design** acceptable
- ✅ **Traditional practice** / client preference
- ✅ **Learning** cold-formed steel (simpler concept)
- ✅ **Comparison** / checking DSM results

### Use DSM when:
- ✅ **Optimization** desired (lighter sections)
- ✅ **Complex sections** (multiple stiffeners, unusual shapes)
- ✅ **Elastic buckling software** available (CUFSM, THIN-WALL, etc.)
- ✅ **Distortional buckling** is concern
- ✅ **Modern practice** / computer-aided design
- ✅ **Research** or advanced design
- ✅ **Perforated sections** (web holes)

### Use BOTH when:
- ✅ **Validation** of results
- ✅ **Learning** / understanding behavior
- ✅ **Comparison** studies
- ✅ **Calibration** of new sections

---

## Example Comparison

**Many examples show both methods side-by-side:**

### Beams:
- **II-1A (EWM)** vs **II-1B (DSM):** Same C-purlin
- **II-4A (EWM)** vs **II-4B (DSM):** Same C-section without lips
- **II-6A (EWM)** vs **II-6B (DSM):** Weak-axis bending
- **II-7A (EWM)** vs **II-7B (DSM):** Hat section

### Columns:
- **III-1A (EWM)** vs **III-1B (DSM):** C-section compression
- **III-5A (EWM)** vs **III-5B (DSM):** Angle with lips
- **III-7A (EWM)** vs **III-7B, III-7C (DSM):** Z-section stud
- **III-9A (EWM)** vs **III-9B (DSM):** Hat section

**Result:** DSM typically gives 5-15% higher strength for standard sections.

---

## Distortional Buckling

### EWM Approach:
- **Not explicitly in traditional EWM**
- Some guidance in Specification for edge stiffeners
- Generally requires engineering judgment

### DSM Approach:
- **Directly addressed** with F_crd and strength curves
- Explicit equations in Sections E3.2, F3.2
- Critical for C and Z sections with lips

**Example:** II-5 demonstrates distortional buckling using DSM

---

## Elastic Critical Loads (F_cr)

**Required for DSM, calculated for EWM theory:**

### How to Obtain F_crl, F_crd, F_cre:

#### 1. Finite Strip Method (Most Common)
**Software:**
- **CUFSM** (free, Johns Hopkins)
- **THIN-WALL** (free, University of Sydney)
- Commercial FEA packages

**Process:**
- Input section geometry
- Run buckling analysis
- Read critical loads for local, distortional, global modes

#### 2. Design Tables/Charts
- Available in some references
- Limited to standard sections
- Example: AISI Design Guide CF16-1

#### 3. Rational Analysis
- Closed-form solutions for simple cases
- Appendix 2 provides methods
- Tedious for hand calculation

#### 4. Conservative Approximations
- Use EWM equations to estimate F_crl
- Use simplified formulas for F_crd
- Sacrifice some economy

---

## Specification Appendix 2

**Appendix 2: Elastic Buckling Analysis**
- Provides methods for calculating F_cr
- Three approaches:
  1. **Finite Element Method (FEM)**
  2. **Finite Strip Method (FSM)** - Most common
  3. **Generalized Beam Theory (GBT)**

**Commentary Appendix 2:**
- Detailed background
- Validation studies
- Design charts
- 30 pages (437-465)

---

## Historical Development

### Effective Width Method:
- **1946:** George Winter publishes original effective width formula
- **1968:** AISI Specification adopts EWM
- **1996:** Refinements for edge stiffeners
- **Present:** Appendix 1 of AISI S100

### Direct Strength Method:
- **1998-2003:** Research by Schafer and Pekoz
- **2004:** First appearance in AISI Specification (Appendix)
- **2007:** Moved to main Specification (Chapters E, F)
- **2016:** Fully integrated, refined curves

**Trend:** DSM gaining popularity, but EWM still widely used.

---

## Software Tools

### For EWM:
- **Hand calculations** or spreadsheet
- Most structural analysis software (RISA, SAP2000, etc.)
- Section property calculators

### For DSM:
- **CUFSM** (free) - Finite Strip Method
  - http://www.ce.jhu.edu/bschafer/cufsm/
- **THIN-WALL** (free) - Finite Strip + optimization
  - https://www.sydney.edu.au/engineering/thin-wall/
- **MASTAN2** (free) - Includes some CFS capabilities
- **CFS** (AISI) - Design software using DSM
- **Commercial FEA** - ANSYS, ABAQUS (advanced)

---

## Design Tables

### EWM Tables:
- Widely available
- Manufacturer catalogs (ClarkDietrich, MBMA, etc.)
- AISI Design Manual Volume 1 (Property tables)

### DSM Tables:
- Limited availability
- Growing number of design aids
- AISI Design Guides
- Research publications

**Recommendation:** Use software for DSM

---

## Learning Curve

**For students/new engineers:**

1. **Start with EWM:**
   - Understand effective width concept
   - See how local buckling affects capacity
   - Practice hand calculations

2. **Progress to DSM:**
   - Understand buckling modes (L, D, G)
   - Learn elastic buckling analysis
   - Compare with EWM results

3. **Use both:**
   - Validate designs
   - Understand when each is better
   - Choose appropriately for each project

---

## Common Misconceptions

**Myth:** "DSM is always better than EWM"
- **Truth:** DSM is more economical, but EWM is simpler and perfectly valid

**Myth:** "EWM doesn't consider distortional buckling"
- **Truth:** EWM has some provisions for edge stiffeners, but not as explicit as DSM

**Myth:** "DSM is too complicated for hand calculation"
- **Truth:** Partial truth; need software for F_cr, but curves are straightforward

**Myth:** "EWM is obsolete"
- **Truth:** Still in Specification, still used, still valid

---

## References

**Specification:**
- EWM: Appendix 1 (pages 197-208)
- DSM: Chapters E, F, G (integrated)
- Elastic Buckling: Appendix 2 (pages 210-229)

**Commentary:**
- EWM: Commentary Appendix 1 (pages 419-435)
- DSM: Commentary E, F, G
- Elastic Buckling: Commentary Appendix 2 (pages 437-465, 82KB)

**Examples:**
- EWM: I-8A, II-1A, II-4A, II-6A, II-7A, III-1A, III-5A, III-7A, III-9A
- DSM: I-8B, II-1B, II-4B, II-5, II-6B, II-7B, II-13, II-14, III-1B, III-5B, III-7B/C, III-9B, III-14

**Key Papers:**
- Winter, G. (1947). "Strength of Thin Steel Compression Flanges"
- Schafer, B.W. and Pekoz, T. (1998). "Direct Strength Prediction of Cold-Formed Steel Members"

---

**Last Updated:** 2025-11-10
**Source:** AISI S100-16 (2016 Edition)

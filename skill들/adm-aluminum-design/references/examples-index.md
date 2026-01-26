# ADM 2020 Illustrative Examples Index

Complete index of 31 worked calculation examples from Part VII.

---

## Overview

Part VII contains **31 comprehensive examples** illustrating proper application of the ADM 2020 Specification. Each example includes:
- Problem statement (GIVEN)
- Design objective (FIND)
- Step-by-step solution with calculations
- References to applicable Specification sections
- Design commentary and notes

**File Location:** `data/examples/Part_VII_Illustrative_Examples.md`

---

## Complete Examples List

| Example | Member Type | Loading/Analysis | Page | Key Topics |
|---------|-------------|------------------|------|------------|
| **1** | Rod | Tension, axial | 6 | Simple tension, D.2 |
| **2** | Bar, rectangular | Tension, axial | 7 | Tension with thickness selection, 5052-H36 |
| **3** | W-shape | Flexure, Shear | 8 | Combined flexure and shear |
| **4** | Tube, square | Flexure, Shear | 10 | Closed section flexure |
| **5** | Pipe (welded) | Flexure, Shear | 12 | **HAZ effects** on pipe |
| **6** | Plate | Flexure | 14 | Flat plate bending |
| **7** | Riveted connection | Bearing, Shear | 16 | Rivet design, J.4 |
| **8** | Pinned connection | Bearing, Shear, Flexure | 17 | Pin design, J.6.5 |
| **9** | W-shape | Compression, axial | 19 | Column buckling (basic) |
| **10** | Angle (corner of latticed box) | Compression, axial | 21 | Built-up column, single angle |
| **11** | W-shape (welded) | Compression, axial | 23 | **Column with HAZ effects** |
| **12** | Tube, square | Compression, axial | 25 | HSS column |
| **13** | Tube, square (with stiffeners) | Compression, axial | 27 | Intermediate stiffeners, B.5.4.4 |
| **14** | Tube, round | Compression, axial | 28 | Pipe column |
| **15** | W-shape | Flexure | 29 | Lateral-torsional buckling |
| **16** | Girder, welded | Flexure, Fatigue | 31 | **Welded girder with HAZ**, fatigue |
| **17** | Girder, welded (transverse stiffeners) | Flexure, Fatigue | 36 | Stiffened web, fatigue |
| **18** | Pipe | Flexure | 38 | Round tube bending |
| **19** | Bar, rectangular | Flexure | 40 | Simple beam design |
| **20** | Tube, rectangular | Flexure, Shear | 42 | Rectangular HSS beam |
| **21** | W-shape | Flexure | 44 | Compact section flexure |
| **22** | Unsymmetric shape | Flexure | 46 | Tee or channel with unequal flanges |
| **23** | Channel | Flexure | 48 | C-section with edge support |
| **24** | Welded beam | Flexure | 50 | **HAZ in beam web** |
| **25** | Welded beam (stiffened web) | Flexure | 51 | Longitudinal web stiffener |
| **26** | W-shape | Shear | 53 | Web shear capacity |
| **27** | Welded connection | Shear | 55 | Fillet weld design |
| **28** | Curtainwall beam | Flexure | 57 | Architectural beam (6063-T6) |
| **29** | Formed sheet | Flexure, Shear | 64 | Thin-walled sheet metal |
| **30** | Tapping screw connection | Shear, Tension | 68 | Sheet metal fasteners |
| **31** | W-shape | Flexure | 69 | Beam capacity check |

---

## Examples by Category

### Tension Members (Examples 1-2)

**Example 1: Rod in Axial Tension**
- **Alloy:** 6061-T6
- **Problem:** Select smallest standard rod diameter
- **Key Learning:** Basic tension design per D.2
- **Formula:** Required A = P / (F/Ω), F/Ω = 19.5 ksi

**Example 2: Rectangular Bar in Axial Tension**
- **Alloy:** 5052-H36
- **Problem:** Select thickness for 1 in. wide bar
- **Key Learning:** Tension design with non-heat-treatable alloy
- **Formula:** Pn = Fty × Ag / Ωt

---

### Compression Members (Examples 9-14)

**Example 9: W-Shape in Axial Compression**
- **Alloy:** 6061-T6
- **Problem:** Check W-shape column capacity
- **Key Learning:** Column buckling (E.1-E.4), slenderness effects
- **Sections:** E.1, E.2, E.3, E.4

**Example 10: Corner Angle of Latticed Box Column**
- **Alloy:** 6061-T6
- **Problem:** Design individual angle in built-up column
- **Key Learning:** Single angle compression, effective length
- **Sections:** E.1-E.4

**Example 11: Welded W-Shape in Axial Compression** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Column capacity with welded connections
- **Key Learning:** **Use HAZ properties (Fcy = 19 ksi, not 35 ksi)**
- **Critical:** Demonstrates 46% capacity reduction due to HAZ

**Example 12: Square Tube Column**
- **Alloy:** 6061-T6
- **Problem:** HSS column design
- **Key Learning:** Local buckling in tubes (B.5.4.2)
- **Sections:** E.1-E.4

**Example 13: Column with Intermediate Stiffeners**
- **Alloy:** 6061-T6
- **Problem:** Square tube with stiffeners
- **Key Learning:** Stiffener design (B.5.4.4)
- **Sections:** B.5.4.4

**Example 14: Round Tube Column**
- **Alloy:** 6061-T6
- **Problem:** Pipe column design
- **Key Learning:** Round tube local buckling (B.5.4.5)
- **Sections:** E.1, E.2, E.3

---

### Flexural Members (Examples 3-6, 15-23, 28-29, 31)

**Example 3: W-Shape in Flexure and Shear**
- **Alloy:** 6061-T6
- **Problem:** Beam capacity with combined loading
- **Key Learning:** Flexure (F.2, F.3) + Shear (G.2)
- **Sections:** F.2, F.3, G.2

**Example 15: W-Shape in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Beam with lateral-torsional buckling
- **Key Learning:** LTB analysis (F.3, F.4)
- **Sections:** F.2, F.3, F.4, G.2

**Example 16: Welded Girder in Flexure** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Welded plate girder capacity
- **Key Learning:** **HAZ effects in welded beams**, fatigue
- **Critical:** Fatigue considerations for welded members
- **Sections:** F.2, F.3, F.4 + Fatigue (Section 3)

**Example 17: Welded Girder with Transverse Stiffeners** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Stiffened web girder with fatigue
- **Key Learning:** Web buckling with stiffeners, fatigue life
- **Sections:** F.2, F.3, F.4 + Fatigue

**Example 18: Pipe in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Round tube beam capacity
- **Key Learning:** Circular section flexure
- **Sections:** F.2, F.3, F.4

**Example 19: Rectangular Bar in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Flat bar beam design
- **Key Learning:** Simple beam without LTB concerns
- **Sections:** F.2, F.4

**Example 20: Rectangular Tube in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Rectangular HSS beam
- **Key Learning:** Closed section beam design
- **Sections:** F.2, F.3, F.4, G.2

**Example 21: W-Shape in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Compact beam without LTB
- **Key Learning:** Full plastic section modulus (compact sections)
- **Sections:** F.2, F.3

**Example 22: Unsymmetric Shape in Flexure**
- **Alloy:** 6061-T6
- **Problem:** Tee or unequal flange section
- **Key Learning:** Non-symmetric section bending
- **Sections:** B.5.4.1, B.5.4.2, B.5.4.3, B.5.5.1, F.2, F.3

**Example 23: Channel in Flexure**
- **Alloy:** 6061-T6
- **Problem:** C-section beam
- **Key Learning:** Elements supported on one edge (B.5.5.2)
- **Sections:** B.5.4.1, B.5.5.1, B.5.5.2, F.2, F.3

**Example 24: Welded Beam - Allowable Web Stress** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Web stress with HAZ
- **Key Learning:** **HAZ effects on web capacity**
- **Sections:** B.5.5.1

**Example 25: Welded Beam with Stiffened Web** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Longitudinal web stiffener with HAZ
- **Key Learning:** Stiffener effectiveness with welding
- **Sections:** B.5.5.3

**Example 28: Curtainwall Beam**
- **Alloy:** 6063-T6 (architectural)
- **Problem:** Architectural beam design
- **Key Learning:** Lower-strength alloy application
- **Sections:** F.2, F.3, F.4

**Example 29: Formed Sheet in Flexure**
- **Alloy:** Various sheet alloys
- **Problem:** Thin-walled sheet metal beam
- **Key Learning:** Cold-formed sheet design
- **Sections:** B.5.4.2, B.5.5.1, F.2, F.3, J.9.3.2, L.3

---

### Shear-Dominant Examples (Examples 4-5, 26)

**Example 4: Square Tube in Flexure and Shear**
- **Alloy:** 6061-T6
- **Problem:** HSS with high shear
- **Key Learning:** Shear in closed sections
- **Sections:** F.2, F.3.3, G.2, J.9.3.1

**Example 5: Welded Pipe in Flexure and Shear** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Round tube with welded connections
- **Key Learning:** **HAZ effects in pipe**, shear (G.4)
- **Sections:** B.5.5.4, F.2, F.4, G.4

**Example 26: W-Shape with Web Shear Controlling**
- **Alloy:** 6061-T6
- **Problem:** Beam governed by shear capacity
- **Key Learning:** Web shear design (G.2)
- **Sections:** F.2, F.3, G.2

---

### Connection Examples (Examples 7-8, 27, 30)

**Example 7: Riveted Connection**
- **Alloy:** 6061-T6
- **Problem:** Rivet shear and bearing
- **Key Learning:** Rivet design per J.4
- **Sections:** J.4.6 (bearing)

**Example 8: Pinned Connection**
- **Alloy:** 6061-T6
- **Problem:** Pin connection design
- **Key Learning:** Pin in bearing, shear, flexure
- **Sections:** J.6.5

**Example 27: Welded Connection** ← **HAZ Example**
- **Alloy:** 6061-T6 (welded)
- **Problem:** Fillet weld design
- **Key Learning:** **Weld strength + HAZ base metal check**
- **Critical:** Both weld AND base metal (with HAZ) must be checked
- **Sections:** J.2

**Example 30: Tapping Screw Connection**
- **Alloy:** Sheet metal alloys
- **Problem:** Self-tapping screw design
- **Key Learning:** Sheet metal fastener capacity
- **Sections:** J.5

---

## HAZ-Critical Examples (Must-Know)

These examples explicitly demonstrate Heat-Affected Zone considerations:

1. **Example 5**: Welded Pipe in Flexure and Shear
2. **Example 11**: Welded W-Shape in Axial Compression ← **Best column HAZ example**
3. **Example 16**: Welded Girder in Flexure (with fatigue)
4. **Example 17**: Welded Girder with Transverse Stiffeners
5. **Example 24**: Allowable Web Stress in Welded Beam
6. **Example 25**: Welded Beam with Stiffened Web
7. **Example 27**: Welded Connection ← **Best connection HAZ example**

**Key Pattern:** All welded examples use reduced properties:
- Fty(HAZ) instead of Fty (typically 19 ksi vs 35 ksi for 6061-T6)
- Ftu(HAZ) instead of Ftu (typically 24 ksi vs 38 ksi for 6061-T6)
- Result: ~46% capacity reduction

---

## Examples by Alloy

### 6061-T6 (Most Examples)
Examples: 1, 3, 4, 5*, 7, 8, 9, 10, 11*, 12, 13, 14, 15, 16*, 17*, 18, 19, 20, 21, 22, 23, 24*, 25*, 26, 27*, 31
(*welded)

### 6063-T6 (Architectural)
Example: 28 (curtainwall beam)

### 5052-H36 (Non-Heat-Treatable)
Example: 2 (tension bar)

### Other Alloys
Example: 29, 30 (sheet metal - various alloys)

---

## Examples by Specification Chapter

### Chapter D (Tension)
- Examples 1, 2

### Chapter E (Compression)
- Examples 9, 10, 11, 12, 13, 14

### Chapter F (Flexure)
- Examples 3, 4, 5, 6, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31

### Chapter G (Shear)
- Examples 3, 4, 5, 15, 20, 21, 22, 23, 26, 29

### Chapter J (Connections)
- Examples 7, 8, 27, 30

### Local Buckling (B.5.4, B.5.5)
- Elements in compression: Examples 10, 11, 12, 13, 14, 21, 22, 23, 29
- Elements in flexure: Examples 16, 20, 21, 22, 23, 24, 25

---

## How to Use Examples

### For Learning

**Step 1: Read the example narrative**
- Understand the problem statement
- Note the alloy, temper, loading conditions

**Step 2: Follow the calculations**
- Verify each formula application
- Check section references in Part I (Specification)

**Step 3: Study the commentary**
- Notes explain design decisions
- Alternatives and cautions highlighted

### For Design Reference

**Matching Your Problem:**

| Your Design Task | Reference Examples |
|------------------|-------------------|
| Tension member selection | 1, 2 |
| Simple column | 9, 12, 14 |
| **Welded column** | **11** ← Use this! |
| Built-up column | 10, 13 |
| Simple beam | 15, 18, 19, 21 |
| **Welded beam** | **16, 17, 24, 25** ← Use these! |
| Beam with high shear | 4, 5, 26 |
| Unsymmetric section | 22, 23 |
| **Welded connection** | **27** ← Use this! |
| Bolted/riveted connection | 7, 8 |
| Sheet metal | 29, 30 |

### For Verification

**Check your calculations against:**
1. Example with same member type
2. Example with same loading type
3. Example with same alloy (or similar)
4. Example with same connection type (welded vs bolted)

---

## Common Example Patterns

### Standard Example Format

```
Example X: [Title]

GIVEN:
1. Loads
2. Alloy-temper
3. Product specification (ASTM B221, B209, etc.)
4. Geometry

FIND:
- Design objective
- What to calculate or verify

SOLUTION:
Step 1: Determine properties from Part IV
Step 2: Calculate geometric properties (if needed)
Step 3: Check applicable limit states
Step 4: Apply safety factors (Ω)
Step 5: Final answer

NOTES/COMMENTARY:
- Design tips
- Common mistakes to avoid
- Alternative approaches
```

### HAZ Example Pattern (Welded Members)

```
Example X: [Title] (Welded)

GIVEN:
- Alloy: 6061-T6 (welded)
- [other givens]

SOLUTION:
Step 1: **Use HAZ properties** ← CRITICAL
   - Fty(HAZ) = 19 ksi (NOT 35 ksi)
   - Ftu(HAZ) = 24 ksi (NOT 38 ksi)

Step 2: Calculate capacity with reduced strength

Step 3: Compare to unwelded capacity (for context)
   - Shows % reduction due to HAZ

NOTES:
- HAZ extends ~1 inch from weld
- Consider bolted connection to avoid HAZ
- Or use 5xxx series (minimal HAZ effect)
```

---

## Example Cross-Reference Table

Specification Section → Examples that illustrate it:

| Section | Topic | Main Examples | Other Examples |
|---------|-------|---------------|----------------|
| **B.5.4.1** | Flat elements, one edge | 10, 11, 21 | 3, 9, 13, 16, 22, 23, 26 |
| **B.5.4.2** | Flat elements, both edges | 12, 22 | 4, 9, 11, 20, 24, 29 |
| **B.5.4.5** | Pipes and tubes | 14 | 12 |
| **B.5.5.1** | Flexural elements, both edges | 24 | 3, 16, 20, 21, 22, 23 |
| **B.5.5.2** | Flexural elements, one edge free | 23 | - |
| **B.5.5.3** | Stiffened flexural elements | 25 | - |
| **D.2** | Tension members | 1 | 2 |
| **E.2** | Column strength | 9 | 10, 11, 12, 14 |
| **F.2, F.3, F.4** | Flexure - open shapes | 15, 16 | 3, 21, 22, 23, 26, 28 |
| **F.2, F.3, F.4** | Flexure - round tubes | 18 | 5 |
| **F.2, F.4** | Flexure - bars | 19 | 6 |
| **F.2, F.3, F.4** | Flexure - closed shapes | 20 | 4 |
| **G.2** | Shear - flat webs | 26 | 3, 4, 15, 20, 21, 22, 23 |
| **G.4** | Shear - round tubes | 5 | - |
| **J.2** | Welded connections | 27 | - |
| **J.4.6** | Rivets in bearing | 7 | - |
| **J.6.5** | Pins | 8 | - |

---

## Design Workflow with Examples

### Typical Design Process:

```
1. Define problem
   ↓
2. Find matching example(s)
   ↓
3. Extract relevant formulas and procedures
   ↓
4. Apply to your specific case
   ↓
5. Cross-check with Specification (Part I)
   ↓
6. Verify with Commentary (Part II) if unclear
```

### Example: Designing a Welded Column

**Step 1:** Identify as compression member with welds
**Step 2:** Reference **Example 11** (Welded W-Shape in Compression)
**Step 3:** Extract key points:
- Use Fcy(HAZ) = 19 ksi for 6061-T6 welded
- Use Bc, Dc, Cc for welded condition
- Check both elastic and inelastic buckling
**Step 4:** Apply to your column geometry
**Step 5:** Cross-check with Sections E.1-E.4
**Step 6:** Review Commentary C-E for buckling background

---

## Tips for Using Examples

### Do:
- ✅ Read the entire example, including notes
- ✅ Verify formula references in Specification
- ✅ Note which alloy/temper is used
- ✅ Check if member is welded (HAZ implications)
- ✅ Understand the limit state being checked
- ✅ Compare multiple examples if applicable

### Don't:
- ❌ Copy numbers without understanding
- ❌ Ignore HAZ properties in welded examples
- ❌ Assume all alloys behave the same
- ❌ Skip the commentary/notes section
- ❌ Use example from one loading type for different loading

---

**All 31 examples are essential learning resources for proper ADM 2020 application!**

**For welded aluminum design, Examples 5, 11, 16, 17, 24, 25, and 27 are CRITICAL.**

---

*ADM 2020 Examples Index*
*For complete worked calculations, see data/examples/Part_VII_Illustrative_Examples.md*

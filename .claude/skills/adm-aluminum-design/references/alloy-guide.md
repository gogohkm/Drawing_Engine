# Aluminum Alloy Quick Reference Guide

Common structural aluminum alloys and their properties.

---

## Most Common Structural Alloys

### 6061-T6 (Most Popular - General Structural)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty (Tensile Yield) | 35 | 19 | ksi | 46% reduction when welded |
| Ftu (Tensile Ultimate) | 38 | 24 | ksi | 37% reduction when welded |
| Fcy (Compressive Yield) | 35 | 19 | ksi | Same as Fty |
| Fsu (Shear Ultimate) | 24 | 15 | ksi | |
| E (Modulus) | 10,100 | 10,100 | ksi | Unchanged |

**Applications:**
- General structural members
- Beams, columns, connections
- Most common choice for building structures
- Good balance of strength, weldability, and cost

**Temper Notes:**
- T6 = Solution heat treated + artificially aged
- Loses strength above 200°F (limit for sustained loading)
- Cannot be re-heat-treated after welding

---

### 6061-T4 (Formable, Lower Strength)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty | 16 | ~16 | ksi | Minimal HAZ effect (already soft) |
| Ftu | 26 | ~26 | ksi | |
| E | 10,100 | 10,100 | ksi | |

**Applications:**
- Cold forming applications
- Where lower strength acceptable
- Less critical HAZ effects

---

### 6063-T6 (Architectural Extrusions)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty | 25 | 14 | ksi | 44% reduction when welded |
| Ftu | 30 | 20 | ksi | 33% reduction |
| E | 10,100 | 10,100 | ksi | |

**Applications:**
- Architectural shapes
- Extrusions with complex cross-sections
- Window frames, curtain walls
- Non-critical structural elements

**Advantages:**
- Excellent extrudability
- Good surface finish
- Lower cost than 6061

---

### 6063-T5 (Architectural, Lower Strength)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty | 16 | 9 | ksi | 44% reduction when welded |
| Ftu | 22 | 14 | ksi | |
| E | 10,100 | 10,100 | ksi | |

**Applications:**
- Architectural (non-structural)
- Trim, molding, decorative shapes
- Light-duty applications

---

### 5052-H32 (Marine, Non-Heat-Treatable)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty | 23 | ~23 | ksi | Minimal HAZ effect! |
| Ftu | 31 | ~31 | ksi | |
| E | 10,200 | 10,200 | ksi | |

**Applications:**
- Marine environments
- Excellent corrosion resistance
- Where HAZ is a concern

**Advantages:**
- **Minimal strength loss from welding** (non-heat-treatable)
- Excellent corrosion resistance
- Good formability

---

### 5083-H112 (Marine, Higher Strength)

**Typical Properties:**
| Property | Unwelded | Welded (HAZ) | Units | Notes |
|----------|----------|--------------|-------|-------|
| Fty | 35 | ~35 | ksi | Minimal HAZ effect! |
| Ftu | 44 | ~44 | ksi | |
| E | 10,400 | 10,400 | ksi | |

**Applications:**
- Marine structures
- Cryogenic applications
- Welded structures where HAZ is critical

**Advantages:**
- **Minimal strength loss from welding**
- Highest strength of 5xxx series
- Non-heat-treatable (no temper loss)

---

## Quick Selection Guide

### By Application

| Application | Recommended Alloy | Reason |
|-------------|-------------------|--------|
| **General structural** | 6061-T6 | Best strength-to-cost ratio |
| **Architectural extrusions** | 6063-T6 or 6063-T5 | Excellent extrudability, good finish |
| **Marine/corrosive** | 5052-H32 or 5083-H112 | Excellent corrosion resistance |
| **Welded structures** | 5xxx series OR 6061-T6* | 5xxx: no HAZ; 6061: accept HAZ reduction |
| **Cold forming** | 6061-T4 or 5xxx | Better formability |
| **High strength** | 7075-T6 or 7xxx | Not extensively covered in ADM 2020 |

\* For 6061-T6 welded: Design using HAZ properties (Fty=19 ksi)

### By Weldability

| Priority | Best Choice | HAZ Effect | Notes |
|----------|-------------|------------|-------|
| **Minimal HAZ** | 5xxx series (H-temper) | ~0-5% reduction | Non-heat-treatable |
| **Acceptable HAZ** | 6061-T6 | ~46% reduction | Design with Fty=19 ksi (welded) |
| **Poor choice for welding** | 7xxx series | Very significant | Not recommended |

### By Temperature Exposure

| Max Temp (Sustained) | Suitable Alloys | Notes |
|---------------------|-----------------|-------|
| **< 200°F** | All 6xxx-T6/T5 | Safe for T6/T5 tempers |
| **200-300°F** | 5xxx, 6xxx-O | T6/T5 lose strength; use H or O |
| **> 300°F** | Consult specialist | Beyond typical aluminum use |

---

## Alloy Series Overview

### 6xxx Series (Heat-Treatable, Mg-Si)
- **6061**: General structural - most common
- **6063**: Architectural extrusions
- **6066**: Higher strength (less common)

**Characteristics:**
- Heat-treatable (T4, T5, T6 tempers)
- Good weldability (with HAZ consideration)
- Moderate strength
- Good corrosion resistance
- **Significant HAZ effect when welded**

### 5xxx Series (Non-Heat-Treatable, Mg)
- **5052**: Sheet, moderate strength
- **5083**: Plate, higher strength
- **5086**: Moderate strength, good formability

**Characteristics:**
- Non-heat-treatable (H tempers: H32, H112, etc.)
- Excellent corrosion resistance
- Good weldability (**minimal HAZ**)
- Marine applications
- Cannot be strengthened by heat treatment

### 7xxx Series (Heat-Treatable, Zn)
- **7075**: Highest strength
- **7050**: Aerospace

**Characteristics:**
- Highest strength aluminum alloys
- Heat-treatable (T6, T73, etc.)
- Poor weldability (very sensitive to HAZ)
- Not extensively covered in ADM 2020

### 3xxx Series (Non-Heat-Treatable, Mn)
- **3003**: Low strength, good formability
- **3004**: Moderate strength

**Characteristics:**
- Non-heat-treatable
- Low to moderate strength
- Good corrosion resistance
- Limited structural use

---

## Design Considerations by Alloy

### For 6061-T6 (Most Common)

**When Unwelded:**
- Use Fty = 35 ksi, Ftu = 38 ksi
- Full design strength available
- Temperature limit: 200°F sustained

**When Welded:**
- **Use Fty = 19 ksi, Ftu = 24 ksi** (HAZ properties)
- Significant strength reduction (~46%)
- HAZ extends ~0.5-1.5 inches from weld
- Consider 5xxx series if HAZ unacceptable

### For 6063-T6 (Architectural)

**When Unwelded:**
- Use Fty = 25 ksi
- Adequate for many architectural loads

**When Welded:**
- Use Fty = 14 ksi (HAZ)
- 44% strength reduction
- Often still adequate for architectural loads

### For 5xxx Series (Marine/Welded)

**Advantages:**
- Minimal HAZ effect
- Use base metal properties even when welded
- Excellent for welded structures

**Disadvantages:**
- Cannot be heat-treated to increase strength
- Limited to H-temper strengths (typically 20-35 ksi)

---

## Temperature Effects

### 6xxx Series (T5/T6 Tempers)

| Temperature | Effect on Strength | Design Action |
|-------------|-------------------|---------------|
| < 200°F | Minimal (< 5%) | Use full strength |
| 200-250°F | 10-20% reduction | Reduce design values or analyze |
| 250-300°F | 30-50% reduction | Consult Part IV tables |
| > 300°F | Severe degradation | Not recommended |

**Note:** Temperature limits in Table A.4.1 (Chapter A)

### 5xxx Series (H Tempers)

| Temperature | Effect | Notes |
|-------------|--------|-------|
| < 200°F | Minimal | Stable |
| 200-300°F | Slight (< 10%) | Better than 6xxx |
| > 300°F | Moderate | Consult tables |

---

## Where to Find Detailed Properties

### In ADM 2020 Documents:

1. **Chapter A, Section A.4**: Material specifications and alloy listings
2. **Part IV - Material Properties**: Complete tables with:
   - Unwelded properties (Fty, Ftu, Fcy, Fsu, E)
   - Welded (HAZ) properties
   - Temperature-dependent values
   - Buckling constants (Bc, Dc, Cc by alloy)

3. **Tables B.4.1 and B.4.2** (Chapter B): Buckling constants by alloy/temper

### Using Python Scripts:

```bash
# Look up any alloy properties
python3 scripts/alloy_lookup.py "6061-T6" --welded

# Calculate HAZ effects
python3 scripts/haz_calculator.py --alloy "6061-T6"
```

---

**Always verify alloy and temper before design calculations!**
**For welded members, always use HAZ properties for heat-treatable alloys (6xxx).**

---

*Quick Reference Guide - ADM 2020*
*For detailed properties, consult Part IV: Material Properties*

# Heat-Affected Zone (HAZ) Strength Reduction Factors

Critical reference for welded aluminum design.

---

## Overview

**Heat-Affected Zone (HAZ)**: The region adjacent to a weld where the base metal's microstructure and properties are altered by welding heat.

**Critical Fact**: Heat-treatable aluminum alloys (6xxx, 7xxx) experience **significant strength reduction** in the HAZ. This is **the most important difference** between aluminum and steel welding.

---

## HAZ Strength Reduction by Alloy

### 6061-T6 (Most Common Structural)

| Property | Base Metal (Unwelded) | HAZ (Welded) | Reduction Factor | % Loss |
|----------|----------------------|--------------|------------------|--------|
| **Fty** | 35 ksi | 19 ksi | 0.54 | 46% |
| **Ftu** | 38 ksi | 24 ksi | 0.63 | 37% |
| **Fcy** | 35 ksi | 19 ksi | 0.54 | 46% |
| **Fsu** | 24 ksi | 15 ksi | 0.63 | 37% |

**Design Impact**: For welded 6061-T6 members, use Fty = 19 ksi (not 35 ksi!)

---

### 6061-T4 (Solution Heat Treated Only)

| Property | Base Metal | HAZ | Reduction Factor | % Loss |
|----------|-----------|-----|------------------|--------|
| **Fty** | 16 ksi | ~16 ksi | ~1.0 | Minimal |
| **Ftu** | 26 ksi | ~26 ksi | ~1.0 | Minimal |

**Note**: T4 temper is already in a "soft" condition (naturally aged), so welding has minimal additional effect.

---

### 6063-T6 (Architectural Extrusions)

| Property | Base Metal | HAZ | Reduction Factor | % Loss |
|----------|-----------|-----|------------------|--------|
| **Fty** | 25 ksi | 14 ksi | 0.56 | 44% |
| **Ftu** | 30 ksi | 20 ksi | 0.67 | 33% |
| **Fcy** | 25 ksi | 14 ksi | 0.56 | 44% |

**Design Impact**: Similar to 6061-T6, significant HAZ reduction

---

### 6063-T5 (Architectural, Lower Strength)

| Property | Base Metal | HAZ | Reduction Factor | % Loss |
|----------|-----------|-----|------------------|--------|
| **Fty** | 16 ksi | 9 ksi | 0.56 | 44% |
| **Ftu** | 22 ksi | 14 ksi | 0.64 | 36% |

---

### 5052-H32 (Marine, Non-Heat-Treatable)

| Property | Base Metal | HAZ | Reduction Factor | % Loss |
|----------|-----------|-----|------------------|--------|
| **Fty** | 23 ksi | ~23 ksi | ~1.0 | **Minimal** |
| **Ftu** | 31 ksi | ~31 ksi | ~1.0 | **Minimal** |

**Key Advantage**: 5xxx series alloys are **non-heat-treatable**, so welding does NOT significantly reduce strength!

---

### 5083-H112 (Marine, Higher Strength)

| Property | Base Metal | HAZ | Reduction Factor | % Loss |
|----------|-----------|-----|------------------|--------|
| **Fty** | 35 ksi | ~35 ksi | ~1.0 | **Minimal** |
| **Ftu** | 44 ksi | ~44 ksi | ~1.0 | **Minimal** |

**Key Advantage**: Can achieve 6061-T6 strength levels WITHOUT HAZ penalty!

---

## Quick Reference: Welding Sensitivity

| Alloy Series | Temper Type | HAZ Effect | Design Strategy |
|--------------|-------------|------------|-----------------|
| **6xxx** | T6, T5 | **Severe** (40-50% loss) | Use HAZ properties OR avoid welds |
| **6xxx** | T4 | Minimal | Use base properties |
| **5xxx** | H (strain-hardened) | **Minimal** | Use base properties |
| **3xxx** | H | Minimal | Use base properties |
| **7xxx** | T6 | **Very Severe** (> 50% loss) | Avoid welding |

---

## HAZ Geometry

### Typical HAZ Width

| Welding Process | HAZ Width (each side of weld) |
|----------------|------------------------------|
| **GMAW** (Gas Metal Arc) | 0.5 - 1.0 inch |
| **GTAW** (Gas Tungsten Arc) | 0.3 - 0.8 inch |
| **SMAW** (Shielded Metal Arc) | 0.8 - 1.5 inch |

**Design Implication**: For conservative design, assume HAZ extends **1 inch** from weld centerline.

### HAZ Extent in Different Members

**Welded I-Beam (Web to Flange):**
```
    Flange ████████████████ (HAZ in flange near weld)
            │
            │ Web (HAZ in web near weld)
            │
```

**Butt-Welded Plate:**
```
  HAZ │ Weld │ HAZ
  ←1"→│←0.5"→│←1"→
      │      │
████  │ ███  │  ████
Base  │ Weld │  Base
```

**Fillet-Welded Connection:**
```
      ▲ Fillet weld
     /│\
    / │ \
  HAZ │ HAZ
  ←1"→│←1"→
```

---

## Design Procedures for Welded Members

### Procedure 1: Conservative (Simplest)

**Approach**: Assume **entire member** uses HAZ properties

**When to Use**:
- Short members where HAZ is significant portion
- Conservative preliminary design
- When detailed analysis not justified

**Example**:
- Member: 6061-T6 beam, length = 10 ft, welded connections
- **Use Fty = 19 ksi throughout** (even though only ends are welded)

**Pros**: Simple, conservative
**Cons**: May be overly conservative for long members

---

### Procedure 2: Detailed (More Accurate)

**Approach**: Use **reduced section** with HAZ properties

**When to Use**:
- Long members with localized welds
- Optimization needed
- Final design

**Steps**:
1. Identify weld locations
2. Determine HAZ extent (typically ±1 inch from weld)
3. Calculate effective section with reduced properties in HAZ zone
4. Design using this reduced section

**Example**:
- Beam: 6061-T6, 10 ft long
- Welded splice at mid-span, weld = 0.5" wide
- HAZ zone: 1" each side of weld = 2.5" total width
- **Rest of beam**: Use Fty = 35 ksi
- **HAZ zone** (2.5"): Use Fty = 19 ksi

**Pros**: More accurate, less conservative
**Cons**: More complex

---

### Procedure 3: Avoid Welds (Best if Possible)

**Approach**: Use **mechanical connections** (bolts, rivets) instead of welding

**Advantages**:
- No HAZ strength reduction
- Use full base metal strength (Fty = 35 ksi for 6061-T6)
- Demountable

**Considerations**:
- Bolt holes create net section reduction
- May require larger sections
- Bolted connection design per Chapter J

---

## When to Consider Non-Heat-Treatable Alloys

If **welding is unavoidable** and **HAZ is unacceptable**, consider:

### Option 1: Switch to 5xxx Series

**5083-H112**:
- Fty = 35 ksi (same as 6061-T6)
- **Minimal HAZ effect**
- Excellent for welded structures

**5052-H32**:
- Fty = 23 ksi (lower than 6061-T6)
- Minimal HAZ
- Good for moderate loads

**Trade-off**: Non-heat-treatable alloys cannot be strengthened later

---

### Option 2: Design with HAZ Properties

Accept the strength reduction and design accordingly:
- Use Fty = 19 ksi for 6061-T6 welded
- Increase section size to compensate
- Document HAZ assumptions clearly

---

## Post-Weld Heat Treatment (PWHT)

### Can HAZ Strength Be Restored?

**Theoretically**: Yes, by solution heat treating + aging (re-T6 treatment)

**Practically**: **Rarely done** because:
1. Requires furnace large enough for entire component
2. Expensive ($$$)
3. May cause distortion
4. Not practical for site welds

**Conclusion**: **Assume HAZ properties are permanent**. Do not count on PWHT.

---

## ADM 2020 References

### Where to Find HAZ Properties

1. **Part IV - Material Properties**: Tables show both:
   - Unwelded (base metal) strengths
   - Welded (HAZ) strengths
   - Organized by alloy and temper

2. **Chapter J - Connections**: Section J.2.4.2 addresses weld strength with HAZ

3. **Commentary (Part II)**: Explains HAZ phenomenon and research basis

### Example from Part IV (Typical Format)

```
Alloy: 6061-T6
Product: Extrusions
Thickness: 0.125 - 1.000 in

           Unwelded    Welded (HAZ)
Fty         35 ksi      19 ksi
Ftu         38 ksi      24 ksi
Fcy         35 ksi      19 ksi
Fsu         24 ksi      15 ksi
E        10,100 ksi  10,100 ksi
```

---

## Calculation Examples

### Example 1: Welded Beam Flexural Strength

**Given**:
- Beam: 6061-T6 I-beam
- Section modulus: S = 10 in³
- Welded end connections

**Solution**:

Unwelded would be:
```
Mn = Fty × S = 35 ksi × 10 in³ = 350 kip-in
```

Welded (with HAZ):
```
Mn = Fty(HAZ) × S = 19 ksi × 10 in³ = 190 kip-in
Ma = Mn / Ω = 190 / 1.65 = 115 kip-in
```

**Result**: 46% reduction in capacity due to HAZ!

---

### Example 2: Welded Tension Member

**Given**:
- Rod: 6061-T6, diameter = 1 inch
- Welded to end fittings
- Area = 0.785 in²

**Solution**:

Yielding (HAZ controls):
```
Pn = Fty(HAZ) × Ag = 19 ksi × 0.785 in² = 14.9 kips
Pa = Pn / Ω = 14.9 / 1.95 = 7.6 kips
```

vs Unwelded would have been:
```
Pn = 35 ksi × 0.785 = 27.5 kips → Pa = 14.1 kips
```

**Reduction**: From 14.1 kips to 7.6 kips (46% loss)

---

## Design Recommendations

### For Structural Engineers

1. **Always ask**: "Is this member welded?"
2. **Always specify**: Alloy AND temper (not just "aluminum")
3. **For welded 6061-T6**: Use Fty = 19 ksi as default
4. **For critical welds**: Consider 5xxx series instead
5. **Document assumptions**: State clearly if HAZ properties used

### For Fabricators

1. **Minimize welds** where possible (use bolts/rivets)
2. **Use low heat input** welding (reduces HAZ width)
3. **GTAW preferred** over SMAW (smaller HAZ)
4. **Quality control**: HAZ cannot be "fixed" after welding

---

## Comparison: Aluminum vs Steel

| Aspect | Aluminum (6061-T6) | Steel (A36) |
|--------|-------------------|-------------|
| **Base Fty** | 35 ksi | 36 ksi |
| **HAZ Fty** | 19 ksi (46% loss) | ~36 ksi (minimal loss) |
| **Design Impact** | **CRITICAL** | Minor |
| **Why Different?** | Heat treatment lost | No heat treatment to lose |

**Key Takeaway**: HAZ is **critical for aluminum** design, unlike steel!

---

**ALWAYS USE HAZ PROPERTIES FOR WELDED HEAT-TREATABLE ALUMINUM!**

---

*ADM 2020 HAZ Reference Guide*
*For detailed values, consult Part IV: Material Properties*

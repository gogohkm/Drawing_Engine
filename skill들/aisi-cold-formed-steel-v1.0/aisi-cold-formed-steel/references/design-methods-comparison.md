# Design Methods Comparison: ASD vs LRFD vs LSD

Comparison of three design methods available in AISI S100-16.

**All three methods are equally valid** and give equivalent levels of safety when properly applied.

---

## Overview

AISI S100-16 is unique among structural codes in providing **three complete design methods**:

1. **ASD** - Allowable Strength Design
2. **LRFD** - Load and Resistance Factor Design
3. **LSD** - Limit States Design (Canadian variant)

**Key principle:** All methods use the same nominal strength (R_n), but apply different safety/resistance factors.

---

## Fundamental Equations

### ASD (Allowable Strength Design)

**Basic equation:**
```
R_n / Ω ≥ R_a
```

where:
- R_n = Nominal strength
- Ω = Safety factor (> 1.0)
- R_a = Required strength (from ASD load combinations)

**Philosophy:**
- Divide nominal strength by safety factor
- Use service (unfactored) loads
- Traditional approach (pre-1986)
- Simpler load combinations

---

### LRFD (Load and Resistance Factor Design)

**Basic equation:**
```
φ R_n ≥ R_u
```

where:
- φ = Resistance factor (< 1.0)
- R_n = Nominal strength
- R_u = Required strength (from LRFD load combinations)

**Philosophy:**
- Multiply nominal strength by resistance factor
- Use factored loads (1.2D + 1.6L + ...)
- Modern probabilistic approach (1986+)
- More complex load combinations
- Optimized for reliability

---

### LSD (Limit States Design)

**Basic equation:**
```
φ R_n ≥ R_f
```

where:
- φ = Resistance factor (same as LRFD)
- R_n = Nominal strength
- R_f = Factored resistance (from LSD load combinations per NBCC)

**Philosophy:**
- Similar to LRFD
- Uses Canadian load factors (NBCC - National Building Code of Canada)
- See Specification Appendix B

---

## Safety/Resistance Factors

**Relationship:** Approximately **φ × Ω ≈ 1.5 to 1.6**

### Typical Values

| Limit State | φ (LRFD/LSD) | Ω (ASD) | φ × Ω |
|-------------|--------------|---------|-------|
| **Tension yielding** | 0.90 | 1.67 | 1.50 |
| **Tension rupture** | 0.75 | 2.00 | 1.50 |
| **Compression** | 0.85 | 1.80 | 1.53 |
| **Flexure (F ≤ 2.78)** | 0.90 | 1.67 | 1.50 |
| **Flexure (F > 2.78)** | 0.95 | 1.67 | 1.59 |
| **Shear** | 0.90 or 0.95 | 1.67 or 1.60 | 1.50-1.52 |
| **Bearing** | 0.65 | 2.22 | 1.44 |
| **Bolt shear** | 0.65 | 2.35 | 1.53 |
| **Screw shear** | 0.50 | 3.00 | 1.50 |
| **Weld** | 0.55-0.70 | 2.35-2.80 | 1.29-1.96 |

**Note:** Connection factors are generally lower (more conservative) than member factors.

---

## Load Combinations

### ASD Load Combinations (Service Loads)

From ASCE/SEI 7:

1. D
2. D + L
3. D + (L_r or S or R)
4. D + 0.75L + 0.75(L_r or S or R)
5. D + (0.6W or 0.7E)
6. D + 0.75L + 0.75(0.6W) + 0.75(L_r or S or R)
7. D + 0.75L + 0.75(0.7E) + 0.75S
8. 0.6D + 0.6W
9. 0.6D + 0.7E

where:
- D = Dead load
- L = Live load
- L_r = Roof live load
- S = Snow load
- R = Rain load
- W = Wind load
- E = Earthquake load

**Simplest:** D + L (most common for gravity)

---

### LRFD Load Combinations (Factored Loads)

From ASCE/SEI 7:

1. 1.4D
2. 1.2D + 1.6L + 0.5(L_r or S or R)
3. 1.2D + 1.6(L_r or S or R) + (L or 0.5W)
4. 1.2D + 1.0W + L + 0.5(L_r or S or R)
5. 1.2D + 1.0E + L + 0.2S
6. 0.9D + 1.0W
7. 0.9D + 1.0E

**Most critical for gravity:** 1.2D + 1.6L

---

### LSD Load Combinations (Canada)

From NBCC (National Building Code of Canada):

**Principal combinations:**
- 1.4D
- (1.25D or 0.9D) + 1.5L + ...
- Other combinations with companion loads

**See Specification Appendix B for complete LSD provisions.**

---

## Comparison Table

| Aspect | ASD | LRFD | LSD |
|--------|-----|------|-----|
| **Factor approach** | Safety factor Ω | Resistance factor φ | Resistance factor φ |
| **Equation** | R_n/Ω ≥ R_a | φR_n ≥ R_u | φR_n ≥ R_f |
| **Load combinations** | Service loads | Factored loads | Factored loads (NBCC) |
| **Complexity** | Simpler | More complex | More complex |
| **Optimization** | Less optimized | Better optimized | Better optimized |
| **History** | Pre-1986 | 1986+ | Canadian |
| **Geographic** | USA common | USA preferred | Canada |
| **Conservatism** | More conservative* | Less conservative* | Similar to LRFD |
| **Load patterns** | Fewer combinations | More combinations | More combinations |

*For typical gravity loads; depends on load ratios

---

## When to Use Each Method

### Use ASD when:
- ✅ Client or jurisdiction requires it
- ✅ Simpler load combinations preferred
- ✅ Traditional practice (existing designs)
- ✅ Quick hand calculations
- ✅ Light-frame residential (where common)
- ✅ Working with older codes or references

### Use LRFD when:
- ✅ Modern practice (most common today in USA)
- ✅ Optimization desired (lighter sections)
- ✅ Complex loading (multiple load types)
- ✅ Building codes require it (IBC default)
- ✅ Commercial/industrial buildings
- ✅ Seismic or wind design
- ✅ Research or academic work

### Use LSD when:
- ✅ **Canadian projects** (required by NBCC)
- ✅ Following CSA S136
- ✅ Provincial building codes in Canada

---

## Example Comparison

**Same beam, same loads, different methods:**

### Given:
- C8×2.5×0.075 (Fy = 50 ksi)
- Span = 20 ft
- Dead load = 15 psf
- Live load = 30 psf
- Tributary width = 5 ft

### ASD Approach:

**Load combination:** D + L
- w_a = (15 + 30) × 5 = 225 lb/ft = 0.225 kip/ft
- M_a = 0.225 × 20² / 8 = 11.25 kip-ft = 135 kip-in

**Required:** M_n / Ω ≥ M_a
- If M_n = 225 kip-in, Ω = 1.67
- Allowable = 225 / 1.67 = 135 kip-in ✓ (exactly meets)

### LRFD Approach:

**Load combination:** 1.2D + 1.6L
- w_u = 1.2(15×5) + 1.6(30×5) = 90 + 240 = 330 lb/ft = 0.33 kip/ft
- M_u = 0.33 × 20² / 8 = 16.5 kip-ft = 198 kip-in

**Required:** φM_n ≥ M_u
- If M_n = 225 kip-in, φ = 0.90
- Design strength = 0.90 × 225 = 202.5 kip-in ✓ (slightly over)

**Result:** Both methods give similar utilization (~98-99%)

---

## Equivalence Check

For the same safety level:

**ASD:** M_n / 1.67 = M_a

**LRFD:** 0.90 M_n = M_u

**Ratio:** M_u / M_a should equal (1.67 / 0.90) = 1.86

**Actual:** 198 / 135 = 1.47

**Why different?**
- Load combinations have different ratios
- For D/L = 15/30 = 0.5, combination factor = (1.2×0.5 + 1.6) / (0.5 + 1) = 1.47 ✓
- For different D/L ratios, equivalence changes

---

## Design Examples Using Each Method

### ASD Examples:
- **II-1A:** Four-Span Continuous C-Purlins (ASD)
- **II-2A:** Four-Span Continuous Z-Purlins (ASD)
- **II-3:** Standing Seam Roof (ASD)

### LRFD Examples:
- **II-1C:** Four-Span C-Purlins Through-Fastened (LRFD)
- **IV-1 to IV-12:** All connection examples (mostly LRFD)

### Both Methods Shown:
- Many examples show equivalent ASD and LRFD solutions
- Compare variant A (often ASD) with variant B/C (often LRFD)

---

## Practical Considerations

### For Design Office:
- **Consistency:** Pick one method, use it for all projects
- **Software:** Check which method your software uses
- **Checking:** If checking someone else's work, use their method

### For Students/Learning:
- **Learn both:** Understanding both gives deeper insight
- **Start with ASD:** Simpler conceptually
- **Progress to LRFD:** Industry standard

### For Code Compliance:
- **IBC (USA):** Allows both ASD and LRFD
- **NBCC (Canada):** Requires LSD
- **Local codes:** Check requirements

---

## Common Misconceptions

**Myth:** "LRFD is always more economical than ASD"
- **Truth:** Depends on load ratios; sometimes equivalent

**Myth:** "ASD is outdated and shouldn't be used"
- **Truth:** Still valid, still used, especially for simple structures

**Myth:** "You need to use LRFD for modern buildings"
- **Truth:** Either method acceptable in USA (IBC allows both)

**Myth:** "φ and Ω are just inverse of each other"
- **Truth:** Not exactly; φ × Ω ≈ 1.5, not 1.0

---

## References

**Specification:** AISI S100-16 Chapter B (Design Requirements)
**Commentary:** Volume 2 Commentary B (pages 277-292)
**Load Combinations:** ASCE/SEI 7 (USA), NBCC (Canada)
**Examples:** Volume 1 Parts II, III, IV

**See also:**
- Specification Appendix A (USA/Mexico provisions)
- Specification Appendix B (Canada/LSD provisions)

---

**Last Updated:** 2025-11-10
**Source:** AISI S100-16 (2016 Edition)

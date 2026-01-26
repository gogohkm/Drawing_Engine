# Load Combinations Quick Reference

## LRFD (Strength Design) - Section 2.3

### Basic Combinations (Section 2.3.1)

| No. | Combination | Equation | Typical Control Scenario |
|-----|-------------|----------|--------------------------|
| 1 | 1.4D | 2.3-1 | Compression members, stability |
| 2 | 1.2D + 1.6L + 0.5(Lr or S or R) | 2.3-2 | Live load dominated structures |
| 3 | 1.2D + 1.6(Lr or S or R) + (L or 0.5W) | 2.3-3 | Roof members, snow regions |
| 4 | 1.2D + 1.0W + L + 0.5(Lr or S or R) | 2.3-4 | Wind-exposed structures |
| 5 | 1.2D + 1.0E + L + 0.2S | 2.3-5 | Seismic zones |
| 6 | 0.9D + 1.0W + 1.6H | 2.3-6 | Uplift, overturning |
| 7 | 0.9D + 1.0E + 1.6H | 2.3-7 | Seismic uplift |

### Seismic Enhanced (Section 2.3.4)

| No. | Combination | Equation | When to Use |
|-----|-------------|----------|-------------|
| 5a | 1.2D + Eh + Ev + L + 0.2S | 2.3-12 | Detailed seismic analysis |
| 7a | (0.9 - 0.2SDS)D + ρQE + 1.6H | 2.3-13 | Seismic with redundancy |

Where:
- Eh = Horizontal seismic effect
- Ev = Vertical seismic effect
- SDS = Design spectral response (short period)
- ρ = Redundancy factor

### Flood (Section 2.3.2)

| Zone | Combination | Equation |
|------|-------------|----------|
| V Zone, Coastal A | 1.2D + 1.0W + 2.0Fa + L + 0.5(Lr or S or R) | 2.3-7 |
| Noncoastal A | 1.2D + 1.0W + 1.0Fa + L + 0.5(Lr or S or R) | 2.3-8 |
| Uplift | 0.9D - 1.0W + 1.0Fa | 2.3-9 |

### Ice (Section 2.3.3)

| Combination | Equation |
|-------------|----------|
| 1.2D + 1.0Wi + L + 0.5(Lr or S or R) | 2.3-10 |
| 0.9D - 1.0Wi + 1.6H | 2.3-11 |

---

## ASD (Allowable Stress Design) - Section 2.4

### Basic Combinations (Section 2.4.1)

| No. | Combination | Equation | Notes |
|-----|-------------|----------|-------|
| 1 | D | 2.4-1 | Dead load only |
| 2 | D + L | 2.4-2 | Typical gravity |
| 3 | D + (Lr or S or R) | 2.4-3 | Roof loads |
| 4 | D + 0.75L + 0.75(Lr or S or R) | 2.4-4 | Multiple transient loads |
| 5 | D + (0.6W or 0.7E) | 2.4-5 | Wind or seismic (not both) |
| 6 | D + 0.75L + 0.75(0.6W) + 0.75(Lr or S or R) | 2.4-6 | Wind with multiple loads |
| 7 | D + 0.75L + 0.75(0.7E) + 0.75S | 2.4-7 | Seismic with multiple loads |
| 8 | 0.6D + 0.6W + H | 2.4-8 | Uplift, wind |
| 9 | 0.6D + 0.7E + H | 2.4-9 | Uplift, seismic |

---

## Load Symbols

| Symbol | Load Type | Reference |
|--------|-----------|-----------|
| D | Dead load | Section 3.1 |
| L | Live load (floor) | Section 4.7 |
| Lr | Roof live load | Section 4.9 |
| S | Snow load | Chapter 7 |
| R | Rain load | Section 8.3 |
| W | Wind load | Chapters 26-30 |
| E | Seismic load | Section 12.4 |
| H | Lateral earth pressure | Section 3.2 |
| Fa | Flood load | Chapter 5 |
| Wi | Wind-on-ice load | Section 10.4 |

---

## Selection Guide

### Choose LRFD when:
- Using modern steel design (AISC 360 LRFD)
- Using concrete design (ACI 318)
- Required by jurisdiction
- Want more economical design

### Choose ASD when:
- Using wood design (NDS)
- Using older design codes
- Required by jurisdiction
- More familiar/comfortable with method

### Key Rules:

1. **Never mix methods**: Use LRFD loads with LRFD resistance, ASD loads with ASD resistance
2. **Check all combinations**: Design for worst case from all applicable combinations
3. **Consider direction**: For W and E, check both positive and negative directions
4. **Load factor on L**: Can reduce to 0.5L in some cases (see Exception in 2.3.1)

---

## Special Load Factors

### Live Load Reduction
Per Section 2.3.1 Exception:
- L can be taken as 0.5L when L₀ ≤ 100 psf
- Except for: garages, public assembly areas

### Temperature Effects (T)
- Include when T significantly affects stiffness or behavior
- Use 1.2T or 0.5T depending on effect
- See Section 2.3.1 for details

### Self-Straining Forces
- Shrinkage, creep, settlement effects
- Usually taken as T in load combinations

---

## Common Mistakes to Avoid

1. ❌ Using LRFD loads with ASD allowable stresses
2. ❌ Forgetting to check uplift combinations (0.9D or 0.6D)
3. ❌ Not checking both +W and -W directions
4. ❌ Omitting 0.2S in seismic combinations
5. ❌ Using 1.6L instead of 0.5L when permitted
6. ❌ Forgetting flood/ice combinations in applicable zones

---

## Quick Decision Tree

```
Start
  ↓
Design method? → LRFD or ASD
  ↓
What loads are present? → D (required) + L, Lr, S, R, W, E, H, Fa, Wi
  ↓
Special conditions?
  - Flood zone? → Add flood combinations
  - High seismic? → Add enhanced seismic combinations
  - Ice region? → Add ice combinations
  ↓
Generate all applicable combinations
  ↓
Design for worst case
```

---

Reference: ASCE 7-22 Chapter 2

# Time Effect Factors ($\lambda$)

Load duration adjustment factors for pultruded GFRP structures.

## Overview

Unlike metals (steel, aluminum), GFRP materials exhibit **time-dependent strength**. Sustained loads cause creep rupture, reducing capacity over time. The time effect factor ($\lambda$) accounts for this phenomenon.

**Design Equation**:
$$R_u \leq \phi \lambda R_n$$

Where:
- $\lambda$ = time effect factor (reduces capacity for long-duration loads)
- $\phi$ = resistance factor
- $R_n$ = nominal resistance
- $R_u$ = required strength

## Standard Time Effect Factors (Table 2-1)

### Load Duration Categories

| Load Duration | $\lambda$ | Typical Load Types | Examples |
|---------------|-----------|-------------------|----------|
| **Permanent** (50+ years) | 0.60 | Dead load, sustained equipment | Self-weight, permanent partitions, HVAC |
| **10 years** | 0.70 | Long-term occupancy loads | Storage, archives, permanent displays |
| **2 months** | 0.80 | Seasonal loads | Snow (winter season) |
| **7 days** | 0.90 | Short-term construction loads | Construction staging |
| **10 minutes** | 1.00 | Impact, wind gust, seismic | Wind, earthquake, impact |

### Application by Load Type

| ASCE 7 Load | Symbol | Recommended $\lambda$ | Reasoning |
|-------------|--------|----------------------|-----------|
| Dead load | $D$ | 0.60 | Permanent - acts for structure life |
| Live load (floors) | $L$ | 0.70 | Sustained portion (10-year equivalent) |
| Roof live load | $L_r$ | 0.90 | Short-term maintenance loads |
| Snow load | $S$ | 0.80 | 2-month winter season duration |
| Wind load | $W$ | 1.00 | 10-minute design wind speed |
| Earthquake | $E$ | 1.00 | Seconds to minutes duration |
| Rain/ponding | $R$ | 0.90 | Short-term storm events |

## Physical Basis

### Creep Rupture Mechanism

**Short-term strength** (instantaneous):
- Fibers carry most load
- Matrix transfers stress between fibers
- Failure at characteristic strength $F_{characteristic}$

**Long-term strength** (sustained):
- Matrix creeps under constant stress
- Stress concentrations develop at fiber-matrix interface
- Micro-cracks accumulate over time
- Eventually rupture at ~60% of short-term strength

### Time-Strength Relationship

Typical creep rupture behavior:
$$\frac{F_{sustained}}{F_{short-term}} \approx 1 - 0.13 \log_{10}(t)$$

Where $t$ is time in hours.

**Example calculation**:
- 1 hour: $\lambda \approx 1.00$
- 168 hours (7 days): $\lambda \approx 0.90$
- 1,460 hours (2 months): $\lambda \approx 0.80$
- 87,600 hours (10 years): $\lambda \approx 0.70$
- 438,000 hours (50 years): $\lambda \approx 0.60$

This matches the standard values in Table 2-1!

### Material Factors Affecting Time Effect

1. **Fiber content**: Higher fiber fraction → less creep → higher $\lambda$
2. **Resin type**:
   - Polyester: More creep
   - Vinyl ester: Moderate creep
   - Epoxy: Least creep (higher $\lambda$ potential)
3. **Temperature**: Higher temperature → more creep → lower effective $\lambda$
4. **Moisture**: Wet conditions → more creep → lower effective $\lambda$

**Note**: Standard $\lambda$ values assume ambient temperature, dry conditions. Environmental effects captured separately by $C_M$ and $C_T$ factors.

## Load Combination Analysis

### Determining Controlling $\lambda$

For load combinations, use $\lambda$ corresponding to **shortest significant duration** in the combination.

**Example 1**: Dead + Live
- Combination: $1.2D + 1.6L$
- $D$ duration: Permanent ($\lambda_D$ = 0.60)
- $L$ duration: 10-year ($\lambda_L$ = 0.70)
- **Use $\lambda$ = 0.70** (live load governs duration)

**Example 2**: Dead + Snow
- Combination: $1.2D + 1.6S$
- $D$ duration: Permanent ($\lambda_D$ = 0.60)
- $S$ duration: 2-month ($\lambda_S$ = 0.80)
- **Use $\lambda$ = 0.80** (snow governs duration)

**Example 3**: Dead + Wind
- Combination: $1.2D + 1.0W$
- $D$ duration: Permanent ($\lambda_D$ = 0.60)
- $W$ duration: 10-minute ($\lambda_W$ = 1.00)
- **Use $\lambda$ = 1.00** (wind governs duration)

### Rationale

**Conservative approach**: Assume member sees peak stress for duration of shortest-acting load.
- If combination includes wind or seismic ($\lambda$ = 1.00), use 1.00 for entire combination
- If only gravity loads, use shortest gravity load duration

**Alternative (more accurate but complex)**:
- Proportional approach based on load magnitudes
- Requires statistical analysis of load combinations
- Not commonly used in practice

## Load Combination Table with $\lambda$

| ASCE 7 Load Combination | Controlling $\lambda$ | Reasoning |
|-------------------------|----------------------|-----------|
| 1.4$D$ | 0.60 | Dead load only - permanent |
| 1.2$D$ + 1.6$L$ + 0.5$L_r$ | 0.70 | Live load duration (10 years) |
| 1.2$D$ + 1.6$L_r$ + (0.5$L$ or 0.5$S$) | 0.90 | Roof live load (7 days) |
| 1.2$D$ + 1.6$S$ + (0.5$L$ or 0.8$W$) | 0.80 | Snow duration (2 months) |
| 1.2$D$ + 1.0$W$ + 0.5$L$ + 0.5$S$ | 1.00 | Wind duration (10 minutes) |
| 1.2$D$ + 1.0$E$ + 0.5$L$ + 0.2$S$ | 1.00 | Seismic duration (seconds) |
| 0.9$D$ + 1.0$W$ | 1.00 | Wind controls |

## Design Example

**Given**:
- GFRP beam, nominal moment capacity $M_n$ = 100 kip-in
- Resistance factor $\phi$ = 0.75 (flexure)
- Check load combination: $1.2D + 1.6S$

**Required moment**:
- $M_D$ = 30 kip-in (dead load)
- $M_S$ = 40 kip-in (snow load)
- $M_u$ = 1.2(30) + 1.6(40) = 36 + 64 = 100 kip-in

**Design strength**:
- Load duration: Snow controls → $\lambda$ = 0.80
- $\phi M_n$ = 0.75 × 0.80 × 100 = **60 kip-in**

**Check**: $M_u$ = 100 kip-in > 60 kip-in → **FAILS**

**Impact of $\lambda$**:
- If $\lambda$ = 1.00 (no time effect): $\phi M_n$ = 75 kip-in → Still fails, but closer
- **Time effect reduces capacity by 20%** for snow loads!

## Special Considerations

### Sustained Live Loads

Some occupancies have sustained portions of live load:
- **Storage**: May be sustained for years
- **Libraries/archives**: Books remain in place
- **Heavy equipment**: Machinery stays installed

**Recommendation**:
- Identify sustained vs transient portions
- Use $\lambda$ = 0.60-0.70 for sustained
- Use $\lambda$ = 0.90-1.00 for transient

**Conservative**: Use $\lambda$ = 0.70 for all floor live loads

### Temperature Effects on Duration

**Hot + sustained** is worst case:
- High temperature increases creep rate
- Could reduce effective $\lambda$ below 0.60

**If temperature > 120°F sustained**:
- Consider reduced $\lambda$ = 0.50 for permanent loads
- Or conduct creep rupture testing at elevated temperature

### Vibration and Fatigue

**Dynamic loads** (vibration, repeated loading):
- Standard $\lambda$ values don't address fatigue
- See Section 2.8 for fatigue design
- Fatigue can further reduce capacity below $\lambda R_n$

## Comparison with Wood Design

### Similar Philosophy

Wood (NDS) also uses load duration factors:
- **Permanent**: $C_D$ = 0.9 (vs GFRP $\lambda$ = 0.60)
- **10 years**: $C_D$ = 1.0 (vs GFRP $\lambda$ = 0.70)
- **Snow**: $C_D$ = 1.15 (vs GFRP $\lambda$ = 0.80)
- **Wind**: $C_D$ = 1.6 (vs GFRP $\lambda$ = 1.00)

**Key difference**: Wood factors are inverted (increase for short duration), GFRP factors directly reduce capacity for long duration.

## Serviceability Limit States

**Important**: Time effect factor does **NOT** apply to serviceability checks.

**Deflection**:
- Check using service loads (unfactored)
- Use long-term modulus (includes creep)
- No $\lambda$ factor applied

**Creep deflection**:
$$\Delta_{total} = \Delta_{instantaneous} \times (1 + \psi_{creep})$$

Where $\psi_{creep}$ = creep multiplier (typically 1.5-3.0 for GFRP under sustained load)

**Vibration**:
- Use instantaneous stiffness
- No $\lambda$ factor

## Testing and Verification

### Creep Rupture Testing

To verify or establish project-specific $\lambda$ values:

**ASTM D2990**: Creep testing
1. Load specimens to various % of short-term strength
2. Monitor time to failure
3. Plot stress vs log(time to failure)
4. Extrapolate to design life (50 years)

**Typical test duration**: 1000-10,000 hours
**Extrapolation**: To 438,000 hours (50 years)

**Result**: Can establish material-specific $\lambda$ values

### When to Consider Testing

- **High-consequence structures** (bridges, occupied buildings)
- **Unusual resin systems** (non-standard formulations)
- **Aggressive environments** (high temp + sustained load)
- **Very long design life** (>50 years)

## Summary Quick Reference

### Standard $\lambda$ Values

| Duration | $\lambda$ | When to Use |
|----------|-----------|-------------|
| 50+ years | 0.60 | Dead load alone |
| 10 years | 0.70 | $D + L$ combinations |
| 2 months | 0.80 | $D + S$ combinations |
| 7 days | 0.90 | $D + L_r$ combinations |
| 10 min | 1.00 | $D + W$, $D + E$ combinations |

### Decision Tree

```
Load combination includes:
  Wind or Seismic? → λ = 1.00
  ↓ No
  Roof live load? → λ = 0.90
  ↓ No
  Snow load? → λ = 0.80
  ↓ No
  Floor live load? → λ = 0.70
  ↓ No
  Dead load only? → λ = 0.60
```

### Impact on Design

**Compared to instantaneous capacity**:
- Permanent loads: **40% reduction** ($\lambda$ = 0.60)
- 10-year loads: **30% reduction** ($\lambda$ = 0.70)
- Snow loads: **20% reduction** ($\lambda$ = 0.80)
- Wind/seismic: **No reduction** ($\lambda$ = 1.00)

**Combined with $\phi$**:
- Example: Flexure with dead + live loads
- $\phi \lambda M_n$ = 0.75 × 0.70 × $M_n$ = **0.525 $M_n$**
- Design capacity is ~50% of nominal capacity!

## References

- ASCE/SEI 74-23 Section 2.3.3: Time Effect Factor
- ASCE/SEI 74-23 Table 2-1: Time Effect Factors
- Commentary C2.3.3: Load Duration Effects
- ASTM D2990: Creep and Stress-Rupture Testing
- Bank (2006): "Composites for Construction" - Chapter on creep

---

**Critical Takeaway**: Time effect can reduce GFRP capacity by up to 40% for sustained loads. Always apply appropriate $\lambda$ for load combination being checked. This is unique to GFRP (and wood) - steel and aluminum don't have time effect factors.

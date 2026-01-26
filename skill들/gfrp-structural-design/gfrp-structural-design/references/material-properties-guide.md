# GFRP Material Properties Guide

Quick reference for typical pultruded GFRP material properties and testing requirements.

## Overview

Pultruded GFRP materials exhibit **orthotropic** behavior with vastly different properties in longitudinal (L) versus transverse (T) directions. All properties must be determined by testing per ASTM standards, not assumed.

## Typical Property Ranges

### Elastic Moduli

| Property | Typical Range | Notes |
|----------|---------------|-------|
| $E_L$ (Longitudinal modulus) | 2,000 - 4,000 ksi (14 - 28 GPa) | ~20% of steel, ~25% of aluminum |
| $E_T$ (Transverse modulus) | 800 - 1,500 ksi (5.5 - 10 GPa) | ~40-50% of $E_L$ |
| $G_{LT}$ (Shear modulus) | 300 - 600 ksi (2 - 4 GPa) | ~15% of $E_L$ |
| $\nu_{LT}$ (Poisson's ratio) | 0.25 - 0.35 | Typically 0.3 if not tested |

**Key Point**: GFRP is much more flexible than metals. Serviceability (deflection) often controls design, not strength.

### Tensile Strengths

| Property | Typical Range | Statistical Basis |
|----------|---------------|-------------------|
| $F_L^t$ (Longitudinal tensile) | 30 - 50 ksi (210 - 345 MPa) | 75% confidence, 20% exclusion |
| $F_T^t$ (Transverse tensile) | 5 - 10 ksi (35 - 70 MPa) | Much lower than longitudinal |

**Anisotropy Ratio**: $F_L^t / F_T^t$ typically ranges from 4:1 to 8:1

### Compressive Strengths

| Property | Typical Range | Notes |
|----------|---------------|-------|
| $F_L^c$ (Longitudinal compressive) | 20 - 40 ksi (140 - 275 MPa) | 60-80% of tensile strength |
| $F_T^c$ (Transverse compressive) | 10 - 20 ksi (70 - 140 MPa) | Often higher than $F_T^t$ |

**Key Point**: Compressive strength is typically 60-80% of tensile strength, unlike steel where they're equal.

### Shear Strengths

| Property | Typical Range | Application |
|----------|---------------|-------------|
| $F_{LT}^s$ (In-plane shear) | 4 - 10 ksi (28 - 70 MPa) | Web shear, plate shear |

**Key Point**: Shear strength is relatively low compared to metals. Web buckling often controls beam design.

### Temperature Properties

| Property | Value | Significance |
|----------|-------|--------------|
| $T_g$ (Glass transition temp) | 180 - 250°F (80 - 120°C) | Critical degradation threshold |
| Max sustained service temp | $T_g - 20°F$ | Typical design limit |
| Thermal expansion coeff | ~13 × 10⁻⁶ /°F | ~2× steel, similar to aluminum |

**Critical**: Strength and stiffness degrade rapidly above $T_g$.

## Property Determination Requirements

### Testing Standards

All material properties must be determined by testing per:

| Property | Test Standard | Specimen Type |
|----------|---------------|---------------|
| Tensile properties ($F_L^t$, $F_T^t$, $E_L$, $E_T$, $\nu_{LT}$) | ASTM D3039 | Flat coupon |
| Compressive properties ($F_L^c$, $F_T^c$) | ASTM D3410 or D695 | Flat coupon with fixtures |
| Shear properties ($F_{LT}^s$, $G_{LT}$) | ASTM D5379 (V-notched beam) | Notched coupon |
| Characteristic values | ASTM D6121 | Statistical analysis |
| Filled-hole properties | ASTM D7290 | Open-hole and filled-hole tests |
| Glass transition temp | ASTM E1640 (DSC or DMA) | Thermal analysis |

### Statistical Basis for Characteristic Values

Per ASTM D6121, characteristic values use:
- **75% confidence level**
- **20% exclusion limit** (lower tail)
- **Minimum sample size**: Typically 10-30 specimens per configuration

**Calculation**:
$$F_{characteristic} = \bar{F} - k \cdot s$$

Where:
- $\bar{F}$ = mean strength from tests
- $k$ = statistical factor (from t-distribution)
- $s$ = standard deviation

This ensures 75% confidence that at least 80% of population exceeds the characteristic value.

### Coefficient of Variation (COV)

Typical COV values for GFRP:

| Property | Typical COV | Comments |
|----------|-------------|----------|
| Longitudinal tensile | 5 - 15% | Better quality control |
| Transverse tensile | 10 - 20% | More variability |
| Compressive | 10 - 20% | Test method sensitive |
| Shear | 10 - 15% | Moderate variability |
| Bearing | 15 - 25% | Geometry dependent |

**Higher than metals**: Steel COV typically 3-8%, GFRP is 2-3× more variable.

## Fiber Architecture Effects

### Typical Pultruded Section Layup

Most pultruded shapes use:
- **60-70% continuous roving** (0° fibers, longitudinal)
- **20-30% continuous strand mat** (random in-plane fibers)
- **5-10% surface veil** (outer layer, primarily for corrosion resistance)

This gives strong longitudinal properties but weaker transverse properties.

### Fiber Volume Fraction

| Parameter | Typical Value | Effect |
|-----------|---------------|--------|
| Fiber volume fraction | 40 - 60% | Higher = stronger, stiffer |
| Fiber weight fraction | 50 - 70% | Easier to measure than volume |

**Determination**: Per ASTM D2584 (burn-off) or ASTM D3171 (acid digestion)

## Resin Matrix Types

| Resin Type | Characteristics | Typical Use |
|------------|-----------------|-------------|
| **Polyester** | Most common, lowest cost, adequate corrosion resistance | General structural applications |
| **Vinyl Ester** | Better corrosion and thermal resistance than polyester | Chemical plants, elevated temps |
| **Epoxy** | Highest performance, best adhesion, most expensive | High-performance applications |

**Standard**: Most design data based on polyester or vinyl ester systems.

## Environmental Effects on Properties

### Moisture Absorption

- **Typical saturation**: 0.5 - 2.0% by weight
- **Time to saturation**: Months to years depending on thickness
- **Effect**: 10-30% strength/stiffness reduction when saturated
- **Adjustment**: Apply $C_M$ factor per Section 2.4

### Temperature Effects

| Temperature Range | Effect on Properties |
|-------------------|---------------------|
| Below $T_g - 50°F$ | Minimal degradation (<5%) |
| $T_g - 50°F$ to $T_g - 20°F$ | Moderate degradation (5-15%) |
| Above $T_g - 20°F$ | Significant degradation (>20%) |
| Above $T_g$ | Severe degradation (>50%), not recommended |

**Adjustment**: Apply $C_T$ factor per Section 2.4

### Chemical Exposure

Common chemicals and effects:
- **Mild acids/alkalis**: 5-20% reduction with $C_{CH}$
- **Strong acids (pH <3)**: 20-40% reduction
- **Strong alkalis (pH >11)**: 30-50% reduction
- **Solvents**: Case-by-case, some resins resistant

**Critical**: Test in actual chemical environment when possible.

### UV Exposure

- **Unprotected GFRP**: Surface degradation, chalking, fiber exposure
- **With surface veil and pigments**: Minimal strength loss if protected
- **Gel coat or paint**: Recommended for outdoor exposure

## Comparison with Traditional Materials

### Property Comparison Table

| Property | GFRP | Steel (A36) | Aluminum (6061-T6) | Ratio GFRP/Steel |
|----------|------|-------------|-------------------|------------------|
| $E$ (modulus) | 2,500 ksi | 29,000 ksi | 10,100 ksi | 1 : 12 |
| $F_t$ (tensile) | 35 ksi | 58 ksi | 35 ksi (unwelded) | 1 : 1.7 |
| Density | 0.065 lb/in³ | 0.284 lb/in³ | 0.098 lb/in³ | 1 : 4.4 |
| Strength/weight | 538 ksi/(lb/in³) | 204 ksi/(lb/in³) | 357 ksi/(lb/in³) | 2.6 : 1 |
| Thermal expansion | 13×10⁻⁶/°F | 6.5×10⁻⁶/°F | 13×10⁻⁶/°F | 2 : 1 vs steel |

**Key Insights**:
- **Much lower stiffness**: Deflection often governs
- **Good strength-to-weight ratio**: Lighter than metals
- **No yielding**: Brittle failure, no ductility
- **Time-dependent**: Creep under sustained load
- **Environmentally sensitive**: Requires protection

## Design Implications

### When GFRP Strength Controls
- Short-span beams with heavy loads
- Tension members (cables, hangers)
- Connections (bearing, net section)

### When GFRP Stiffness Controls
- Long-span beams (L/d > 20)
- Columns with low axial load
- Vibration-sensitive floors
- Deflection-limited applications

**Rule of Thumb**: If steel design is governed by L/360 deflection limit, GFRP likely controlled by stiffness.

## Quality Control Considerations

### Manufacturing Variability

Factors affecting properties:
1. **Fiber content** (±5% can affect $E_L$ by ±15%)
2. **Resin cure** (temperature, time profile)
3. **Pultrusion speed** (affects fiber wet-out)
4. **Die temperature** (affects resin crosslinking)

### Acceptance Criteria

Minimum requirements per production lot:
- **Tensile modulus**: ≥ 90% of characteristic value
- **Tensile strength**: ≥ 80% of characteristic value
- **Dimensional tolerance**: Per ASTM D3917

## Common Design Values

### For Preliminary Design

If no test data available, use these conservative values for initial sizing:

| Property | Conservative Value |
|----------|-------------------|
| $E_L$ | 2,500 ksi (17 GPa) |
| $E_T$ | 1,000 ksi (7 GPa) |
| $G_{LT}$ | 400 ksi (2.8 GPa) |
| $F_L^t$ | 30 ksi (210 MPa) |
| $F_L^c$ | 20 ksi (140 MPa) |
| $F_{LT}^s$ | 5 ksi (35 MPa) |
| $\nu_{LT}$ | 0.30 |

**Warning**: Final design MUST use manufacturer-specific test data. These values are for preliminary sizing only.

## Summary Checklist

When specifying GFRP materials, ensure:
- ✅ Test data per ASTM D6121 with 75% confidence, 20% exclusion
- ✅ Both longitudinal AND transverse properties determined
- ✅ Glass transition temperature ($T_g$) verified ≥ service temp + 20°F
- ✅ Environmental factors ($C_M$, $C_T$, $C_{CH}$) identified and applied
- ✅ Time effect factor ($\lambda$) appropriate for load duration
- ✅ Bearing strength for connection design determined per ASTM D7290
- ✅ Quality control procedures per ASTM D4923 and D3917
- ✅ Coefficient of variation documented for reliability calculations

## References

- ASTM D3039: Tensile Properties of Polymer Matrix Composites
- ASTM D3410/D695: Compressive Properties
- ASTM D5379: Shear Properties (V-notched beam)
- ASTM D6121: Determination of Characteristic Properties
- ASTM D7290: Filled-Hole Tension and Compression Properties
- ASTM E1640: Glass Transition Temperature
- ASTM D2584: Ignition Loss (fiber content)
- ASTM D3171: Fiber Content by Matrix Digestion
- ASTM D3917: Dimensional Tolerances
- ASTM D4923: Standard Practices for Pultruded Products

---

**Source**: ASCE/SEI 74-23 Standard, Chapter 1 and Chapter 2, with typical industry values

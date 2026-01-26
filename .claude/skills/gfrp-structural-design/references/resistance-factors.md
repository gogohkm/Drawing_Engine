# Resistance Factors ($\phi$)

LRFD resistance factors for pultruded GFRP structural members and connections.

## Overview

The resistance factor ($\phi$) accounts for:
1. Variability in material properties
2. Variability in member dimensions
3. Uncertainty in analysis models
4. Consequences of failure

**Design Equation**:
$$R_u \leq \phi \lambda R_n$$

Where:
- $R_u$ = required strength (factored loads)
- $\phi$ = resistance factor
- $\lambda$ = time effect factor
- $R_n$ = nominal resistance (based on adjusted material properties)

## Resistance Factors by Member Type

### Tension Members (Chapter 3)

| Limit State | $\phi$ | Section | Notes |
|-------------|--------|---------|-------|
| Gross section yielding | 0.85 | 3.2 | Rupture in main body |
| Net section rupture | 0.85 | 3.3 | Rupture at bolt holes |

**Why 0.85?**
- Tensile failure is relatively predictable
- Linear elastic to failure (no yielding warning)
- Similar to AISC steel tension factor

### Compression Members (Chapter 4)

| Limit State | $\phi$ | Section | Notes |
|-------------|--------|---------|-------|
| Flexural buckling | 0.80 | 4.2 | Euler buckling |
| Local flange buckling | 0.70 | 4.4 | More variable |
| Local web buckling | 0.70 | 4.4 | More variable |
| Torsional buckling | 0.70 | 4.4 | Open sections |
| Flexural-torsional buckling | 0.70 | 4.4 | Unsymmetric sections |

**Why lower than tension?**
- Buckling more sensitive to imperfections
- Local buckling especially variable in thin-walled sections
- Lower $\phi$ for local buckling reflects higher uncertainty

**Comparison to Steel**:
- AISC compression $\phi$ = 0.90 (LRFD)
- GFRP compression $\phi$ = 0.70-0.80 (more conservative due to material variability)

### Flexural Members (Chapter 5)

| Limit State | $\phi$ | Section | Notes |
|-------------|--------|---------|-------|
| Material rupture (tension/compression) | 0.75 | 5.2 | Rupture in extreme fiber |
| Lateral-torsional buckling | 0.75 | 5.2 | Unbraced beam |
| Local flange buckling | 0.75 | 5.2 | Compression flange |
| Local web buckling | 0.75 | 5.2 | Under flexure |
| Web shear | 0.85 | 5.3 | Shear in web |
| Web shear buckling | 0.85 | 5.3 | With or without stiffeners |
| Web crippling | 0.75 | 5.4 | Concentrated load |

**Why 0.75 for flexure?**
- Intermediate between tension (0.85) and compression (0.70)
- Accounts for combined tension/compression behavior
- Reflects statistical variability of strength measurements

**Why 0.85 for shear?**
- Shear failures relatively ductile (progressive)
- Less sensitive to material variability
- Similar to steel shear resistance factor

### Combined Loading (Chapter 6)

| Limit State | $\phi$ | Section | Notes |
|-------------|--------|---------|-------|
| Beam-column (axial + bending) | Use controlling limit state | 6.3 | Interaction equations |
| Torsion | 0.75 | 6.4 | Torsional strength |
| Combined torsion + flexure + axial | Use controlling limit state | 6.4 | Multiple interactions |

**Approach**: Use $\phi$ value for controlling failure mode in interaction equation.

## Resistance Factors for Plates (Chapter 7)

| Limit State | $\phi$ | Section | Application |
|-------------|--------|---------|-------------|
| In-plane tension | 0.85 | 7.5 | Plate tension |
| In-plane compression | 0.75 | 7.6 | Plate compression |
| In-plane shear | 0.85 | 7.7 | Plate shear |
| Transverse shear (pull-through) | 0.65 | 7.4 | Fastener pull-through |

**Note**: Plates often more variable than pultruded sections due to fabrication.

## Resistance Factors for Connections (Chapter 8)

### Bolted Connections

| Failure Mode | $\phi$ | Section | Why This Value? |
|--------------|--------|---------|-----------------|
| **Bolt shear/tension** | 0.75 | 8.3 | Steel bolt, per AISC |
| **Bearing** | 0.65 | 8.3 | Variable, depends on geometry |
| **Net tension** | 0.50 | 8.3 | Most critical, brittle failure |
| **Shear-out** | 0.50 | 8.3 | Brittle, geometry-dependent |
| **Block shear** | 0.65 | 8.3 | Combined shear + tension |
| **Pull-through** | 0.50 | 8.3 | Localized bearing failure |

**Why connections have lowest $\phi$?**
1. **Stress concentrations** at holes reduce predictability
2. **Brittle failures** with no warning (net tension, shear-out)
3. **Geometric variability** (hole size, edge distance tolerances)
4. **Orthotropic effects** (bearing strength varies with load angle)
5. **Multi-bolt load distribution** is non-uniform and hard to predict

**Critical**: Connection design often governs GFRP structures due to low $\phi$ values.

### Connection Factor Breakdown

**Net Tension ($\phi$ = 0.50)**:
- Most conservative factor in standard
- Reflects brittle catastrophic failure mode
- High coefficient of variation in tests (COV = 15-25%)
- No ductility or warning before failure

**Bearing ($\phi$ = 0.65)**:
- Intermediate factor
- More ductile than net tension (progressive crushing)
- Still variable due to hole tolerance and orthotropic effects

**Bolt Shear ($\phi$ = 0.75)**:
- Steel bolt, well-understood behavior
- Similar to AISC steel connection factors

## Serviceability (No Resistance Factor)

For serviceability limit states (deflection, vibration):
- **No $\phi$ factor applied** (use $\phi$ = 1.0)
- Use service load combinations (unfactored)
- Use mean modulus values (not characteristic values reduced by statistics)

**Example**:
- Strength: $M_u \leq \phi \lambda M_n$ (with $\phi$ = 0.75)
- Deflection: $\Delta_{service} \leq L/360$ (no $\phi$, no $\lambda$)

## Comparison with Other Design Standards

### GFRP vs Steel (AISC 360)

| Limit State | GFRP $\phi$ | Steel LRFD $\phi$ | Ratio |
|-------------|-------------|-------------------|-------|
| Tension yielding | 0.85 | 0.90 | 94% |
| Compression | 0.70-0.80 | 0.90 | 78-89% |
| Flexure | 0.75 | 0.90 | 83% |
| Shear | 0.85 | 0.90 (1.00 for webs) | 85-94% |
| Bolted connections | 0.50-0.75 | 0.75 | 67-100% |

**Why GFRP factors are lower?**
- Higher material variability (COV 2-3× steel)
- Brittle behavior (no yielding plateau)
- Less design/construction experience
- More sensitive to fabrication quality

### GFRP vs Aluminum (ADM 2020)

ADM uses ASD (not LRFD), so direct comparison difficult. But concept similar:
- ADM safety factors ($\Omega$) higher for aluminum than steel
- GFRP resistance factors lower than both due to higher variability

### GFRP vs Wood (NDS)

Wood also uses time-dependent factors and environmental adjustments, similar philosophy to GFRP standard.

## Reliability Basis

### Target Reliability Index

ASCE 7 target: $\beta$ = 3.0 for most structural members (probability of failure ~0.001)

**How $\phi$ values were calibrated**:
1. Collect test data from multiple sources
2. Determine statistical distributions (mean, COV)
3. Use First-Order Reliability Method (FORM) analysis
4. Calibrate $\phi$ to achieve target $\beta$ = 3.0
5. Round to practical values (0.05 increments)

**Result**: Lower $\phi$ for:
- Higher COV (more variable)
- More brittle failure modes
- Less test data available
- Higher consequence of failure

## Special Considerations

### Connection Design Philosophy

**Why $\phi_{connection} < \phi_{member}$?**

**Capacity design approach**:
- Connections should be "weak link" only if intentional
- Often better to have ductile member failure than brittle connection failure
- But GFRP has no ductility in either case

**Practical approach**:
1. Design connections for higher load than member
2. Use "overstrength" factor if ductility is needed
3. Consider multiple load paths

### Multiple Limit States

When checking multiple limit states, use appropriate $\phi$ for each:

**Example: Beam design**
- Rupture: $M_u \leq 0.75 \lambda M_{n,rupture}$
- Lateral-torsional buckling: $M_u \leq 0.75 \lambda M_{n,LTB}$
- Shear: $V_u \leq 0.85 \lambda V_n$
- Deflection: $\Delta \leq L/360$ (no $\phi$)

Check ALL limit states; controlling one may vary by load case.

## Summary Table: All Resistance Factors

| Category | Limit State | $\phi$ |
|----------|-------------|--------|
| **Tension** | Gross/net section | 0.85 |
| **Compression** | Flexural buckling | 0.80 |
| **Compression** | Local buckling | 0.70 |
| **Flexure** | Material rupture | 0.75 |
| **Flexure** | Buckling (LTB, local) | 0.75 |
| **Shear** | Web shear | 0.85 |
| **Shear** | Web buckling | 0.85 |
| **Torsion** | Torsional strength | 0.75 |
| **Connections** | Bolt shear/tension | 0.75 |
| **Connections** | Bearing | 0.65 |
| **Connections** | Net tension | 0.50 |
| **Connections** | Shear-out | 0.50 |
| **Connections** | Block shear | 0.65 |
| **Connections** | Pull-through | 0.50 |
| **Plates** | Tension | 0.85 |
| **Plates** | Compression | 0.75 |
| **Plates** | Shear | 0.85 |

## Design Implications

### Strength-Controlled Design
When strength governs (common in connections, short spans):
- Low $\phi$ significantly reduces capacity
- Connection design is often critical
- May need larger sections than stiffness alone would suggest

### Stiffness-Controlled Design
When deflection governs (common in long spans):
- $\phi$ doesn't apply to serviceability
- Low modulus is the issue, not low $\phi$
- Increasing section depth more effective than strength

### Optimization Strategy
1. **First check serviceability** (deflection, drift)
2. Size member for stiffness (if deflection controls)
3. **Then check strength** with appropriate $\phi$ factors
4. **Finally check connections** (often the critical check)

## References

- ASCE/SEI 74-23 Section 2.3.2: Resistance Factors
- Commentary C2.3: Reliability Basis
- Individual chapters for specific $\phi$ values
- Plevris et al. (2019): "Reliability analysis of GFRP pultruded members"

---

**Key Takeaway**: GFRP resistance factors (0.50-0.85) are notably lower than steel (0.75-0.90) due to higher material variability and brittle behavior. Connection design is especially critical with $\phi$ as low as 0.50.

# Environmental Adjustment Factors

Factors for adjusting GFRP material properties based on environmental exposure conditions.

## Overview

GFRP materials are sensitive to environmental conditions. All characteristic material properties must be adjusted using environmental factors before calculating nominal resistance.

**Adjusted Property Formula**:
$$F_{adjusted} = F_{reference} \times C_M \times C_T \times C_{CH} \times C_{CA} \times C_{LS}$$

Where $F_{reference}$ is the characteristic value from testing (typically at room temperature, dry conditions).

## Moisture Factor ($C_M$)

Accounts for sustained exposure to moisture or wet conditions.

### Typical Values

| Exposure Condition | $C_M$ Range | Application |
|-------------------|-------------|-------------|
| **Dry service** (indoor, climate-controlled) | 1.00 | Office buildings, interior applications |
| **Occasionally wet** (periodic moisture exposure) | 0.90 - 0.95 | Covered structures, intermittent outdoor |
| **Humid/moist** (high humidity, no direct water) | 0.85 - 0.90 | Unconditioned buildings, high humidity zones |
| **Wet service** (frequent water contact) | 0.75 - 0.85 | Cooling towers, exterior exposed structures |
| **Continuous immersion** (submerged) | 0.70 - 0.80 | Marine applications, water tanks |

### Factors Affecting $C_M$

1. **Resin type**:
   - Polyester: More moisture sensitive (lower $C_M$)
   - Vinyl ester: Better moisture resistance
   - Epoxy: Best moisture resistance (higher $C_M$)

2. **Fiber content**:
   - Higher fiber fraction → less resin → less moisture absorption → higher $C_M$

3. **Time to saturation**:
   - Thin sections: Months to saturate
   - Thick sections (>1 inch): Years to saturate
   - Design should assume eventual saturation if continuously wet

### Determination

**Preferred**: Test specimens conditioned to moisture equilibrium per ASTM D5229
- Soak in water at service temperature until weight stabilizes
- Typical: 95°F (35°C) water for 1000-3000 hours
- Test strength of saturated vs dry specimens
- $C_M$ = (saturated strength) / (dry strength)

**If no test data**: Use conservative value (0.75 for wet service, 0.85 for humid)

## Temperature Factor ($C_T$)

Accounts for sustained elevated temperature exposure.

### Typical Values

| Temperature Range | $C_T$ Range | Notes |
|------------------|-------------|-------|
| **< 100°F (38°C)** | 1.00 | No reduction for normal temperatures |
| **100-120°F (38-49°C)** | 0.95 - 1.00 | Minimal degradation |
| **120-150°F (49-66°C)** | 0.85 - 0.95 | Moderate reduction |
| **150-180°F (66-82°C)** | 0.75 - 0.85 | Significant reduction |
| **> $T_g - 20°F$** | < 0.75 | Severe degradation, not recommended |

### Critical Considerations

**Glass Transition Temperature ($T_g$)**:
- Typical for polyester/vinyl ester: 180-250°F (80-120°C)
- Service temperature should remain: **$T < T_g - 20°F$ minimum**
- Above $T_g$: Matrix becomes rubbery, severe strength/stiffness loss

**Duration effects**:
- Short-term temperature spikes (hours): Less critical
- Sustained temperature (months/years): Design case
- Thermal cycling: Additional degradation not captured by $C_T$ alone

### Determination

**Preferred Method**: Heat aging tests per ASTM D3045
1. Condition specimens at design temperature for 1000-3000 hours
2. Test at elevated temperature (not after cooling)
3. Compare to room temperature baseline
4. $C_T$ = (elevated temp strength) / (room temp strength)

**If no test data**:
- Use manufacturer data if available
- Conservative approach: Assume $C_T$ = 0.75 for any sustained $T > 120°F$

**Combined Temperature and Moisture**:
- Effects are multiplicative and synergistic
- Hot + wet is worse than sum of individual effects
- Test in combined environment when critical

## Chemical Environment Factor ($C_{CH}$)

Accounts for exposure to aggressive chemicals.

### Typical Values by Chemical Type

| Chemical Exposure | pH Range | $C_{CH}$ Range | Resin Recommendations |
|------------------|----------|----------------|----------------------|
| **No chemicals** (air, water only) | 5-9 | 1.00 | Any |
| **Weak acids** | 4-5 | 0.90 - 0.95 | Vinyl ester or epoxy |
| **Moderate acids** | 3-4 | 0.80 - 0.90 | Vinyl ester or epoxy |
| **Strong acids** | < 3 | 0.60 - 0.80 | Epoxy (test required) |
| **Weak alkalis** | 9-10 | 0.85 - 0.95 | Polyester acceptable |
| **Moderate alkalis** | 10-12 | 0.70 - 0.85 | Vinyl ester or epoxy |
| **Strong alkalis** | > 12 | 0.50 - 0.70 | Special resins only |
| **Solvents** | - | 0.60 - 0.95 | Case-by-case testing |
| **Salts/brines** | - | 0.85 - 0.95 | Vinyl ester preferred |

### Specific Chemical Guidance

**Acids**:
- Sulfuric acid: Moderate attack, use vinyl ester ($C_{CH}$ = 0.75-0.85)
- Hydrochloric acid: Moderate to severe, use epoxy
- Nitric acid: Severe attack, very limited use

**Alkalis**:
- Sodium hydroxide: Severe attack on polyester, use epoxy
- Calcium hydroxide: Moderate attack (concrete environment)

**Organic Solvents**:
- Gasoline/diesel: Generally acceptable ($C_{CH}$ = 0.90-0.95)
- Acetone/MEK: Can soften resin, test required
- Aromatic solvents: Severe swelling, generally not acceptable

### Determination

**Required**: Chemical resistance testing per ASTM C581 or similar
1. Immerse specimens in actual chemical at service temperature
2. Typical exposure: 1000-3000 hours
3. Measure strength retention
4. $C_{CH}$ = (exposed strength) / (unexposed strength)

**Do not assume**: Chemical resistance varies greatly by resin formulation
- Manufacturer data is specific to their resin system
- Generic "vinyl ester" data may not apply to your specific product

### Warning

**Synergistic effects**:
- Chemicals + temperature = accelerated degradation
- Chemicals + stress = environmental stress cracking
- Test in actual service conditions whenever possible

## Composite Action Factor ($C_{CA}$)

Accounts for composite behavior in built-up or multi-component assemblies.

### When to Apply

**Use $C_{CA} < 1.0$ when**:
- Multiple pultruded sections bolted together as a "built-up" beam
- Face sheets and core in sandwich panels
- FRP decking with overlays
- Any system relying on load transfer between components

### Typical Values

| Assembly Type | $C_{CA}$ Range | Notes |
|---------------|----------------|-------|
| **Fully bonded** (adhesive bonded) | 0.95 - 1.00 | Nearly fully composite |
| **Bolted connections** (close spacing) | 0.85 - 0.95 | Partial composite action |
| **Bolted connections** (wide spacing) | 0.70 - 0.85 | Limited composite action |
| **Mechanical interlock only** | 0.60 - 0.70 | Minimal composite action |
| **No connection** (parallel members) | Use as individual | No composite action |

### Determination

**Analysis Method**:
1. Calculate fully composite stiffness: $(EI)_{composite}$
2. Calculate non-composite stiffness: $(EI)_{non-composite} = \Sigma (EI)_i$
3. Estimate actual stiffness based on connection type: $(EI)_{actual}$
4. $C_{CA}$ = $(EI)_{actual}$ / $(EI)_{composite}$

**Conservative approach**: Design as non-composite ($C_{CA}$ = use individual sections)

## Load-Sharing Factor ($C_{LS}$)

Accounts for load distribution among multiple parallel members.

### When to Apply

**Use $C_{LS} > 1.0$ when**:
- Multiple joists or beams closely spaced (< 24 inches typical)
- Continuous deck or sheathing connects members
- Load can redistribute if one member is weaker

### Typical Values

| System Type | $C_{LS}$ Range | Requirements |
|-------------|----------------|--------------|
| **Single member** (no load sharing) | 1.00 | N/A |
| **2-3 members** | 1.00 - 1.05 | Closely spaced, connected |
| **4-6 members** | 1.05 - 1.10 | Closely spaced, stiff deck |
| **> 6 members** | 1.10 - 1.15 | Full system redundancy |

### Conditions for Load Sharing

All must be true:
1. Members are closely spaced (typically ≤ 24 inches o.c.)
2. Continuous sheathing or deck connects all members
3. Connections allow load transfer (shear transfer)
4. Similar member properties (same material, size)

**Do not use** if:
- Large spacing between members
- No continuous sheathing
- Members can act independently

### Conservative Approach

**Default**: $C_{LS}$ = 1.00 (no credit for load sharing) unless demonstrated by testing or rigorous analysis.

## Combined Environmental Effects

### Application Sequence

Apply factors in order for adjusted material property:
$$F_{design\ use} = F_{characteristic} \times C_M \times C_T \times C_{CH} \times C_{CA} \times C_{LS}$$

**Example Calculation**:
- $F_L^t$ (characteristic) = 40 ksi (from testing)
- Wet service: $C_M$ = 0.80
- Elevated temp (140°F): $C_T$ = 0.85
- Mild acid exposure: $C_{CH}$ = 0.90
- Single member: $C_{CA}$ = 1.00, $C_{LS}$ = 1.00

$$F_L^t (\text{adjusted}) = 40 \times 0.80 \times 0.85 \times 0.90 \times 1.00 \times 1.00 = 24.5 \text{ ksi}$$

**Reduction**: 39% from environmental effects alone!

### Worst-Case Design

**Conservative design approach**:
1. Identify most severe credible exposure (hot + wet + chemical)
2. Apply all relevant factors
3. Result may be 50-70% of characteristic value
4. This is why environmental exposure is critical in GFRP design

## Summary Table: Environmental Factors

| Factor | Symbol | Range | Accounts For |
|--------|--------|-------|--------------|
| Moisture | $C_M$ | 0.70 - 1.00 | Wet service, saturation effects |
| Temperature | $C_T$ | 0.75 - 1.00 | Sustained elevated temperature |
| Chemicals | $C_{CH}$ | 0.50 - 1.00 | Aggressive chemical exposure |
| Composite action | $C_{CA}$ | 0.60 - 1.00 | Built-up member partial composite |
| Load sharing | $C_{LS}$ | 1.00 - 1.15 | Multiple member redundancy |

## Design Checklist

When establishing environmental factors:
- ✅ Identify all environmental exposures over structure life
- ✅ Consider combined effects (hot + wet + chemical)
- ✅ Use manufacturer test data when available
- ✅ Conduct project-specific testing for critical applications
- ✅ Apply factors to ALL material properties ($E_L$, $E_T$, $F_L^t$, $F_L^c$, etc.)
- ✅ Document assumptions and factor sources in calculations
- ✅ Consider long-term degradation (50+ year design life)
- ✅ Review with resin manufacturer for unusual chemicals

## References

- ASCE/SEI 74-23 Section 2.4: Classification Factors
- ASTM D5229: Moisture Absorption Properties
- ASTM D3045: Heat Aging of Plastics
- ASTM C581: Chemical Resistance of Thermosetting Resins
- Manufacturer-specific chemical resistance guides

---

**Critical Note**: Environmental factors can reduce design strength by 30-50% or more. Always verify end-use conditions and apply appropriate factors. When in doubt, test in actual service environment.

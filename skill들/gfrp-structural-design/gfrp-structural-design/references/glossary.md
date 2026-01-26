# ASCE/SEI 74-23 Glossary

Technical terms and definitions for pultruded GFRP structural design.

## Fundamental Definitions

### Pultruded FRP
Structural members of pultruded FRP shapes that comply with ASTM D3917 (*Standard Specification of Dimensional Tolerance for Pultruded Glass Fiber Reinforced Plastic (FRP) Profiles*) or ASTM D3647 (*Standard Specification for Pultruded Fiber Reinforced Plastic (FRP) Grating*). In this standard, the term FRP refers specifically to pultruded FRP.

### Pultrusion
Manufacturing process by which continuous fiber rovings are saturated in resin and pulled through a series of operations (both open and closed), then pulled through a heated die, then through cooling, exiting as a continuous product.

## Material Terms

### Characteristic Value
Statistically based property value determined from tests following ASTM D6121 or ASTM D7290 for FRP structural components. Typically uses 75% confidence interval with 20% lower tail exclusion level. This represents a statistically verified minimum strength or stiffness value for design.

### Fiber Architecture
Structural arrangement of fiber mats or fiber tows (bundles) and their types, such as 0° fibers, 90° fibers, woven strands, random strand mat, stitched fibers, resulting from manufacturing processes.

### Fiber Orientation
The specific location and angular orientation or alignment of FRP structural fibers or fiber layers along their longitudinal directions. Fibers may be oriented in one or more directions to provide structural capacity.

### Fiber Volume Fraction
The ratio of fiber volume to total composite volume. This can be determined by methods from ASTM D2584 or ASTM D3171.

### Lamina
Simple layer or ply of composite material, with fibers aligned in a single direction or in multiple orientations.

### Laminate
FRP composite material formed from one or more laminae (layers) stacked and consolidated, with defined fiber orientations.

### Glass Transition Temperature ($T_g$)
Critical temperature above which the polymer matrix transitions from a glassy (rigid) state to a rubbery (flexible) state, determined per ASTM E1640. FRP strength and stiffness degrade significantly as temperature approaches $T_g$.

### Roving
Bundle or multi-end assembly of continuous filaments or fibers used in the pultrusion process.

## Design Methods

### Load and Resistance Factor Design (LRFD)
Design method in which factored loads are compared with factored resistances. Required strength (factored loads) must not exceed design strength (factored resistance).

**Design Equation**: $R_u \leq \phi \lambda R_n$

Where:
- $R_u$ = required strength due to factored loads
- $\phi$ = resistance factor (accounts for material variability)
- $\lambda$ = time effect factor (accounts for load duration)
- $R_n$ = nominal resistance (adjusted for end-use conditions)

### Allowable Stress Design (ASD) Format
Design approach based on comparison of maximum stress with allowable stress. There is limited guidance in this standard for ASD; LRFD is the primary method.

## Environmental and Adjustment Factors

### Classification Factors
Factors used to multiply the characteristic resistance to obtain the design resistance, accounting for resistance degradations at end-use environmental exposure conditions:

- **$C_M$**: Moisture adjustment factor for sustained in-service exposure
- **$C_T$**: Temperature factor for sustained elevated temperatures
- **$C_{CH}$**: Chemical environment factor
- **$C_{CA}$**: Composite action factor for assembly stiffness
- **$C_{LS}$**: Load-sharing factor for moment resistance

### End-Use Conditions
Conditions that FRP structural members may be subjected to during service life, such as sustained loads, elevated temperatures, moisture, chemicals, fire, UV exposure, resulting in material degradation.

### Time Effect Factor ($\lambda$)
Factor applied to nominal strength to account for effect of duration of load application:
- Permanent loads: $\lambda$ = 0.60
- 10-year duration: $\lambda$ = 0.70
- 2-month duration: $\lambda$ = 0.80
- 7-day duration: $\lambda$ = 0.90
- 10-minute duration: $\lambda$ = 1.00

This accounts for creep rupture and time-dependent strength degradation under sustained loading.

### Load Duration (Time Effect)
Period of continuous application of a given load. Structural capacity of GFRP decreases over time under sustained loading due to viscoelastic creep and time-dependent material degradation.

## Structural Analysis Terms

### Effective Net Area
Net area modified to account for shear lag effects in connections. Calculated as: $A_e = U \times A_n$, where $U$ is the shear lag factor.

### Elastic Analysis
Structural analysis based on assumptions that elastic moduli remain constant and stresses do not exceed proportional limit. No yielding or plastic behavior assumed (GFRP is linear-elastic to failure).

### Transformed Section
For flexural members constructed from components of different moduli, the hypothetical cross-section obtained by adjusting component widths by the ratio of component modulus to reference modulus.

### Second-Order Analysis
Structural analysis that accounts for P-δ (member local) and P-Δ (story drift) effects, where deformations amplify member forces and moments.

## Buckling Modes

### Flexural Buckling
Buckling mode in which a compression member deflects laterally without twisting, with resistance provided by flexural stiffness. Governed by Euler buckling equation.

### Local Flange Buckling
Buckling of the flange element of a compression member or beam before overall member buckling occurs. More critical in thin-walled GFRP sections than in steel.

### Local Web Buckling
Buckling of the web element under compression or shear stresses before overall member failure.

### Torsional Buckling
Buckling mode in which a compression member twists about its shear center without lateral deflection. Critical for angle sections and other open sections.

### Flexural-Torsional Buckling
Buckling mode combining bending and twisting simultaneously, with resistance from both flexural and torsional stiffness. Critical for channel sections and unsymmetric shapes.

### Lateral-Torsional Buckling
Limit state in flexural members (beams) manifested by combined lateral deflection and twisting. Resistance provided by lateral and torsional stiffness.

### Shear Buckling
Buckling mode in webs where compression principal stresses due to shear exceed buckling resistance. Can be prevented with web stiffeners.

## Connection Terms

### Bearing Failure
Limit state in bolted connections involving localized crushing or damage to the bearing face due to bearing pressures from bolt contact.

### Block Shear
Failure mode in connections combining shear failure along one plane and tension failure along a perpendicular plane, creating a "block" tear-out.

### Clip Angle
Angle section used for supporting beams on primary members by bearing and fastening.

### End Distance ($e_1$)
Distance from centerline of bolt hole nearest to the free end to the free edge, measured in direction of applied load.

### Edge Distance ($e_2$)
Distance from centerline of bolt to the nearest edge perpendicular to the load direction.

### Fastener
Generic term for screws, bolts, nails, rivets used in connections.

### Gage ($g$)
Bolt spacing across a row (perpendicular to load direction).

### Net Section
Cross-section reduced by presence of holes for fasteners.

### Pitch Spacing ($s$)
Center-to-center spacing between fastener rows, measured parallel to direction of applied load.

### Pin Bearing Strength ($F_{br}$)
Characteristic bearing strength of FRP material loaded by a cylindrical pin or bolt, determined by testing per ASTM standards.

### Pull-Through
Localized bearing failure where bolt head or washer pulls through the FRP material due to excessive bearing pressure.

### Shear Lag Effects
Reduction in net section efficiency due to non-uniform stress distribution when not all elements of a cross-section are directly connected. Accounted for by factor $U < 1.0$.

### Shear-Out
Failure mode where material between bolt hole and free edge fails in shear, "tearing out" toward the edge.

## Load Terms

### Dead Load ($D$)
Permanent gravity loads including self-weight of structure and fixed equipment.

### Live Load ($L$)
Variable gravity loads from occupancy, movable equipment, and materials.

### Roof Live Load ($L_r$)
Live load on roofs from maintenance workers, equipment during service.

### Snow Load ($S$)
Load from accumulated snow on roof surfaces.

### Wind Load ($W$)
Loads from wind pressure and suction on building surfaces.

### Earthquake Load ($E$)
Seismic forces from ground motion during earthquakes.

### Service Load Combinations
Load combinations under which the structure must maintain function and structural integrity per ASCE 7, used for serviceability limit states.

### Factored Load Combinations
Load combinations with load factors applied per ASCE 7, used for ultimate strength limit states.

## Limit States

### Limit State
Condition in which a structure or component reaches maximum load-carrying capacity or ceases to perform its intended function.

### Ultimate Limit State
Limit state associated with collapse or structural failure. Structure must have adequate strength to resist factored load combinations.

### Serviceability Limit State
Limiting condition affecting appearance, maintainability, durability, and comfort, but not ultimate capacity. Includes deflection, vibration, and drift limits.

## Seismic Design Terms

### Seismic Force-Resisting System
Structural elements designated and detailed to resist lateral forces from earthquakes.

### Seismic Response Modification Coefficient ($R$)
Factor accounting for ductility and energy dissipation capacity of structural system. GFRP systems have low $R$ values (2.0-3.0) due to limited ductility.

### Seismic Design Amplification Factor ($C_d$)
Factor for determining design story drift and deformations.

### Seismic Overstrength Factor ($\Omega_0$)
Factor accounting for structural overstrength beyond design lateral force.

## Structural Members

### Built-Up Members
Structural member fabricated from two or more pultruded sections fastened together to form a stronger composite member.

### Clear Span
Distance between inside faces of supports.

### Composite System
System combining materials or members to form a stronger structural assembly.

### Unbraced Length
Distance between points of bracing of a member, measured between centers of gravity of bracing members.

### Weak Axis
Minor principal centroidal axis of a cross-section (typically y-axis for I-shapes).

### Strong Axis
Major principal centroidal axis of a cross-section (typically x-axis for I-shapes).

## Quality Control Terms

### Quality Assurance (QA)
Administrative and procedural requirements to verify that structure is constructed as designed. Includes material properties verification, fabrication procedures, construction methods, and testing protocols.

### Quality Control (QC)
Procedures established by manufacturer and/or contractor to verify that pultrusion process conditions, fiber architecture, material properties, and geometry remain within specified tolerances using statistical sampling methods. See Chapter 10 in ASTM D7290.

### Registered Design Professional
Individual registered or licensed to practice design profession as defined by state regulatory authority and responsible for the design.

## Resistance and Capacity Terms

### Nominal Resistance ($R_n$)
Calculated maximum load or resistance based on material properties adjusted for end-use environmental conditions, before applying resistance factor.

### Design Resistance
Factored resistance accounting for variability: Design Resistance = $\phi \lambda R_n$

### Required Strength ($R_u$)
Load effect (force, moment, shear, torsion) acting on structure due to factored loads in appropriate combination.

### Resistance Factor ($\phi$)
Factor applied to nominal resistance to account for variability in material strength, fabricated member dimensions, and analysis model accuracy. Values range from 0.50 to 0.85 depending on failure mode:
- Tension: $\phi$ = 0.85
- Compression: $\phi$ = 0.70-0.80
- Flexure: $\phi$ = 0.75
- Shear: $\phi$ = 0.85
- Connections: $\phi$ = 0.50-0.85

## Directional Terms

### Longitudinal Direction (L)
Direction of pultrusion, aligned with primary continuous fibers. Direction of highest strength and stiffness.

### Transverse Direction (T)
Direction perpendicular to pultrusion within the plane of the laminate. Lower strength and stiffness than longitudinal direction.

### Through-Thickness Direction
Direction perpendicular to both longitudinal and transverse directions. Weakest direction due to resin-dominated properties.

### Orthotropic
Material having different properties in three mutually perpendicular directions (L, T, and through-thickness). GFRP is orthotropic, unlike isotropic materials (steel, aluminum).

## Miscellaneous

### Drift
Lateral deformation of structure. Inter-story drift is relative displacement between two adjacent stories.

### Two-Way Plate
Plate subjected to bending in two orthogonal directions simultaneously.

### Stress Concentration
Localized stress amplification in a structural member due to notches, holes, force transfer locations, member geometry changes, and material discontinuities.

---

## Notes

1. GFRP exhibits **no yielding** - behavior is linear-elastic until brittle failure
2. GFRP is **time-dependent** - strength decreases under sustained loading
3. GFRP is **orthotropic** - properties vary by direction (L vs T vs through-thickness)
4. GFRP is **environmentally sensitive** - moisture, temperature, and chemicals significantly reduce capacity
5. **Characteristic values** are statistically determined minimums, not average or nominal values

## Reference

Source: ASCE/SEI 74-23 - Appendix B: Glossary and Chapter 1 Commentary

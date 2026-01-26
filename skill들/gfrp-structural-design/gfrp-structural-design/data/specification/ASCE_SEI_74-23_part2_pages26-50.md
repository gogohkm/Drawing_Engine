<!-- Page 26 -->

$A_g$ = Section of secondary members (B),
$F_{TL}$ = Flange or web in longitudinal tension (B)*, $F_{TL}$ = Flange or web in longitudinal compression (A)*, and
$F_c$ = Moment of inertia of secondary members.

**2.6 Filled and Hollow Shapes**

Design of members and connections subjected to repeated loads and connections elements shall be based on the nominal fatigue design methods presented in this chapter.

The fatigue resistance of members and connections shall not be less than a ratio of the tensile strength, shall be defined by the magnitude of the design resistance divided by the factored nominal tensile strength as defined in Chapter 3. Members and connections with ratios less than this ratio shall be increased from Sections 2.4 and defined in Table 2.1. These effects must be reduced by applying stress modifications as defined in Table 2-1 and:

$$\Delta M_{max} > F_{f}(L/r)^{n}$$
(2-23)

where

$M_r$ = Constant of time-dependent shear; and
$n$ = exponent

**2.6.1 Creep Behavior:** To compute average creep strain and strain geometry of the fatigue-induced shear, and computation with design models.

In fatigue-induced shear, a separate concern at ends and expert points on members where tensile action-tension shear force acts shall be imposed separately with the ratio of member sections. The design effect on flange or web connections shall be defined for the expected number of stress cycles during the service life of the structure:

$$F_{f}(L/r)^{n} = M_{g}/S$$
(2-24)

**2.6.2 Members Subjected to Fatigue Load:**

Connection members, connecting elements, and connectors shall be designed in accordance with this chapter for loads that produce stress through determined by structural analysis for the load combinations specified by Section 1.3.2 has the factored load categories under stress reduction ratio or multipliers to accommodate fiber over-stressing determined by structural ratio of under fire rotation where stress ratio and temperature from structural analysis shall not suffice to permit rupture capacity to accommodate the creep-strains determined by the structural analysis under fire rotation state.

Engineers and connecting elements in pultruded FRP structures by meeting safety-enhancing pultruded under the requirements the structural members stress distribution shall be considered in accordance with Section 2.4. Normal stress shall be concentrated to the center of resistance of the group of fasteners, unless consideration is given to the loading moment induced by the application of the load, particularly for axially-loaded end connections. The stress stress shall be limited as necessary for structural purposes, member loads shall be multiplied in accordance with established creep-rupture interaction factor specified in creep-rupture of mechanical resistance factors applied to fiber-reinforced members shall be computed for each point within a longitudinal center-thickness, taking into account (a) the two connections being non-contiguous (such or concurrent), if these connections are non-concurrent to the span of transverse strength, both connections shall be made where the flange (or the design shear through the span) for each point within (a) longitudinal center-thickness, including the width of the mechanical to the direction center design to avoid net section failure.

The gauge for bolted in adjacent type of edges shall be less than the gauge from the back of the angle to the direction of the fasteners to the angle from the back of the angle to the thickness of the

**Table 2-3. Fatigue Design Parameters.**

| Category | Description of Structural Detail | m | C |
|----------|----------------------------------|---|---|
| I | Plain material and beam or plate material at locations | 3.5 | 0.21 |
| | where the resultant force is concentric to the fastener group. | | |
| II | Material at net section of bolted joints not in Category II, or at points of attachment | 6.5 | 0.06 |
| III | Bolted joints. | | |
| | Details not included in Category I, II, or III | 8.5 | 0.01 |

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 11

<!-- Page 27 -->

This page intentionally left blank

<!-- Page 28 -->

# CHAPTER 3
# DESIGN OF TENSION MEMBERS

## 3.1 SCOPE

The design provisions of this chapter apply to pultruded FRP structural shapes in tension applied parallel to the member's longitudinal axis, with the resultant force acting through the centroid of the transformed cross section. The centroid of cross section is calculated using the ratio of $E$ over $I$ moduli of the elements (flange and web) in the cross section with different fiber directions to their volume fractions. Those members where tension does not act through the centroid of the transformed cross section and parallel to the longitudinal axis of the member must be designed for combined tension and other forces as appropriate.

## 3.2 GENERAL PROVISIONS

A member under axial tension shall be designed such that

$$P_u \leq \lambda \phi P_n$$
(3-1)

where

- $P_u$ = Required axial tensile strength due to factored loads;
- $P_n$ = Nominal axial tensile strength including adjustment factors as defined in Section 2.4 where necessary;
- $\lambda$ = Time effect factor as defined in Table 2-1; and
- $\phi$ = Resistance factor taken as for a section under tension rupture of the material, which shall be taken as 0.65.

## 3.3 NOMINAL AXIAL TENSILE STRENGTH

The nominal axial tensile strength, $P_n$, of a tension member shall be the lower value according to the following limit states:

1. For tensile rupture in the gross section:

$$P_n = F'_t A_g$$
(3-2)

2. For tensile rupture in the net section of shapes made of unidirectional roving and mats with open holes that is not designed for structural connections as in Chapter 8:

$$P_n = 0.7 F'_t A_e$$
(3-3)

where

- $F'_t$ = Characteristic value of the longitudinal tensile strength according to ASTM D638 and adjusted according to Section 2.4.
- $A_g$ = Gross cross-sectional area; and
- $A_e$ = Effective net area of section subjected to tension, as defined in Section 2.10.3.

## 3.4 SLENDERNESS LIMITATION

The slenderness ratio $(L/r)$ of a tension member or component of a built-up member shall not exceed 300. $L$ is the laterally unbraced length of a member or component and $r$ is the radius of gyration about the weak axis of the member or component, as applicable.

## 3.5 BUILT-UP MEMBERS

The design tension strength of built-up members shall be determined in accordance with Section 2.3.2.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 13

<!-- Page 29 -->

This page intentionally left blank

<!-- Page 30 -->

# CHAPTER 4
# DESIGN OF COMPRESSION MEMBERS

This chapter provides provisions for design of compression members.

## 4.1 SCOPE

The design provisions of this chapter apply to pultruded FRP structural shapes subjected to an axial compression force applied parallel to the member's longitudinal axis, with the resultant force acting through the centroid of the transformed cross section. Compression members shall be designed such that

$$P_u \leq \lambda \phi P_n \leq 0.5 M'P_n$$
(4-1)

where

$$\phi P_n = \phi P_e$$
(4-2)

and

$$P_e \leq \frac{\pi^2 E_L A_g}{(\lambda_e K_e L_e)^2} \leq 0.5 M'P_n$$
(4-3)

- $P_u$ = Required compression strength due to factored loads;
- $P_n$ = Nominal compression strength = $P_c$ = the effective critical buckling load = $\lambda_c F_{cry} A_g$ as adjusted by the requirements of Section 2.4;
- $\phi P_e$ = Nominal column capacity, which shall be taken as lesser of cross sections;
- $\phi$ = Resistance factor for compression member with buckling controlled by the local stability and effective length coefficient adjusted in accordance with Section 2.4;
- $M'$ = Maximum design strength factor, as defined in Table 2-1;
- $A_g$ = Gross compression member effective thickness taken along an imaginary plane perpendicular to the cross section or Section 4.1.2; and
- $\lambda_c$ = Governing modification factor for the initial out-of-plane, as defined as follows.

## 4.2 EFFECTIVE COLUMN LENGTH CONSIDERATIONS

For design of compression members based on effective length, $K$ are closely related to end fixity of the column but shall also incorporate practical stability factors according to Section 2.5.

### 4.3.1 Compression Member Effective Length Elastic Flexural Buckling

The critical elastic flexural buckling length factor about axes $x$-axis for a pin-ended member for the minor or major axis shall be taken as the smallest value among the load states of $\phi P_e$, $\phi P_{cry}$, and $\phi P_{ly}$, as defined in the following subsections:

**4.3.1 Compression Member Effective Slenderness Ratio**

In this subsection, the effective slenderness ratio of a flexural member is defined as the ratio of the effective length $K_e$ as defined below by the radius of gyration $r_g$ as defined in Section 4.1.1.

The slenderness ratio $(K_e L_e)/r_g > 200$, where $(K_e L_e)$ is the compression member shape. Buckling failure about major or minor axis of gyration shall be governed by $\phi = 0.8$ for buckling with $r$ as the radius of gyration.

## 4.4 FACTORED CRITICAL STRESS IN COMPRESSION ABOUT COMMON SECTION

The factored critical stress, $\phi F_{cry}$, shall be determined as in Section 2.5 where $F_{cry}$ is $P_c$ divided by $A_g$ of the compression member.

A member subjected to compression shall be designed in a shaped section in which $\phi F_{cry}$ = will be taken as the governing material sections and shall be taken as the lesser of $\phi F_{cry}$ and $\phi F_{ly}$ for buckling defined in accordance with $r_g$ as radius of gyration defined by the following equations:

$$F_{cry} = \frac{\pi^2 E_L}{\left(\frac{K_e L_e}{r_g}\right)^2} \text{ and } \phi = 0.7$$
(4-5)

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 15

<!-- Page 31 -->

$$F_{cry} = \frac{\pi^2 E_L}{\left(\frac{K_y L_y}{r_y}\right)^2} \text{ and } \phi = 0.7$$
(4-6)

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2} \text{ and } \phi = 0.8$$
(4-7)

$$F_{crw} = \frac{\pi^2}{6} \frac{\left[\sqrt{E_L w F_{Tw}} + \nu_{LT} E_{Tw} + 2G_{LT}\right]}{h^2} \frac{1}{t_w} \text{ and } \phi = 0.8$$
(4-8)

where

- $F_{crx}$ = Elastic flexural buckling stress about the $x$-axis,
- $F_{cry}$ = Elastic flexural buckling stress about the $y$-axis,
- $F_{crf}$ = Local flange buckling stress,
- $F_{crw}$ = Local web buckling stress,
- $K_x$ = Effective length factor corresponding to the $x$-axis,
- $K_y$ = Effective length factor corresponding to the $y$-axis,
- $L$ = Laterally unbraced length of member,
- $r$ = Governing radius of gyration about axis of buckling,
- $E_L$ = Characteristic value of longitudinal compression elastic modulus of the flange or web whichever is smaller, adjusted in accordance with Section 2.4,
- $E_{Tw}$ = Characteristic value of the transverse elastic modulus of the web in the direction perpendicular to the pultrusion direction, adjusted in accordance with Section 2.4,
- $\nu_{LT}$ = Poisson's ratio of the web plate element associated with transverse deformation when compression is applied in the longitudinal direction; and
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of flange or web, whichever is smaller, adjusted in accordance with Section 2.4.

**4.4.2 T-Shaped Sections** For T-shaped sections in which the $y$-axis is the axis of symmetry of the geometric shape, the factored critical stress, $\phi F_{cry}$, shall be taken as the lowest of the values of $\phi F_{crf}$, $\phi F_{crw}$, $\phi F_{cry}$, and $\phi F_{ft}$ as defined by the following equations:

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2} \text{ and } \phi = 0.8$$
(4-9)

$$F_{crw} = \frac{G_{LT}}{\left(\frac{d_w}{t_w}\right)^2} \text{ and } \phi = 0.8$$
(4-10)

$$F_{crx} = \frac{\pi^2 E_L}{\left(\frac{K_x L_x}{r_x}\right)^2} \text{ and } \phi = 0.7$$
(4-11)

$$F_{ft} = \left(\frac{F_{cry} + F_{crz}}{2H}\right) \left[1 - \sqrt{1 - \frac{4HF_{cry}F_{crz}}{\left(F_{cry} + F_{crz}\right)^2}}\right] \text{ and } \phi = 0.7$$
(4-12)

where

$$F_{cry} = \frac{\pi^2 E_L}{\left(\frac{K_y L_y}{r_y}\right)^2};$$

$$F_{crz} = \frac{1}{A_g R_p^2} \left[D_f + D_w \left(\frac{\pi}{L}\right)^2\right];$$

$$H = 1 - \frac{y_p^2}{R_p^2};$$

$$y_p = \frac{h_w}{2\left(1 + \frac{b_f t_f}{h_w t_w}\right)};$$

$$R_p^2 = \frac{1}{b_f t_f + h_w t_w} \left[\frac{b_f t_f}{12} \left(b_f^2 + t_f^2\right) + h_w t_w \left(\frac{h_w^2}{6} + \frac{t_w^2}{12}\right)\right];$$

$$D_f = \frac{G_{LT}}{3} (b_f t_f^3 + h_w t_w^3);$$

$$D_w = E_L \left(\frac{b_f^3 t_f}{144} + \frac{h_w^3 t_w}{36}\right);$$

- $F_{cry}$ = Critical elastic flexural buckling stress about the $x$-axis,
- $F_{cry}$ = Elastic flexural buckling stress about the $y$-axis,
- $F_{crz}$ = Critical torsional stress,
- $F_f$ = Elastic flexural-torsional buckling stress,
- $F_{crf}$ = Local flange buckling stress,
- $F_{crw}$ = Local web buckling stress,
- $A_g$ = Gross area of cross section,
- $D_f$ = Torsional rigidity of the section,
- $D_w$ = Warping rigidity of the section,
- $R_p$ = Polar radius of gyration about the center of twisting of the cross section,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of flange or web, whichever is smaller, adjusted in accordance with Section 2.4,
- $E_L$ = Characteristic value of the longitudinal compression elastic modulus of the flange or stem, whichever is smaller, adjusted in accordance with Section 2.4,
- $h_w$ = Distance between the centerline of the flange and the outer face of the stem,
- $b_f$ = Flange width,
- $d_w$ = Clear depth of the web,
- $t_f$ = Flange thickness, and
- $t_w$ = Web thickness.

**4.4.3 Single Angle Sections with Equal Legs** For equal-leg angle sections in which the $y$-axis is the axis of symmetry of the geometric shape, the factored critical stress, $\phi F_{cry}$, shall be taken as the lower of the values of $\phi F_{cry}$ and $\phi F_{crfl}$ defined by the following equations:

$$F_{crx} = \frac{\pi^2 E_L}{\left(\frac{K_x L_x}{r_x}\right)^2} \text{ and } \phi = 0.7$$
(4-13)

**16** STANDARD ASCE/SEI 74-23

<!-- Page 32 -->

$$F_{cry} = \frac{G_{LT}}{\left(\frac{t_f}{r_y}\right)^2} \text{ and } \phi = 0.8$$
(4-14)

where

- $K_x$ = Effective length factor corresponding to the $x$-axis,
- $F_{cry}$ = Critical elastic flexural-local buckling stress combined elastic modulus, adjusted in accordance with Section 2.4
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of flange or web whichever is smaller, adjusted in accordance with Section 2.4.
- $r$ = Radius of gyration of the angle from the axis of buckling,
- $t$ = Angle leg thickness, and
- $t_f$ = Fillet radius of the angle from the principal z-axis.

**4.4.4 Cruciform Sections** The factored critical stress, $\phi F_{cr}$, shall be taken as the lesser of $\phi F_{crx}$ and $\phi F_{crf}$ defined by the following equations:

$$F_{crx} = \left(\frac{2}{3}\right) \left(\frac{h_c}{t_f}\right)^{-2} \left[\nu_{LT} G_{LT} + \sqrt{\nu_{LT}^2 G_{LT}^2 + 2G_{LT}}\right] \text{ and } \phi = 0.8$$
(4-15)

$$F_{crw} = \frac{\left(\frac{4}{3}\right) E_L}{t_f} \text{ and } \phi = 0.8$$
(4-16)

where

- $r$ = Governing radius of gyration of the section corresponding to the axis of buckling,
- $K_x$ = Effective length factor of the section corresponding to $x$ or $y$ axes,
- $E_L$ = Characteristic value of the longitudinal compression elastic modulus, adjusted in accordance with Section 2.4,
- $E_{Ly}$ = Characteristic value of the transverse compression elastic modulus of the web or element under consideration, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of flange or web, whichever is smaller, adjusted in accordance with Section 2.4,
- $\nu_{LT}$ = Poisson's ratio of the web plate element associated with transverse deformation when compression is applied in the longitudinal direction adjusted to account for the shear lag effect for design in accordance with Section 2.4,
- $r_y$ = Minimum width-to-thickness ratio, whichever is larger,
- $t$ = Wall or element connecting the legs section.

**4.4.5 Cruciform Tube Sections** The factored critical stress, $\phi F_{cr}$, shall be taken as the minimum value computed from the following equations:

$$F_{cry} = \frac{2 E_{Ly}}{\left(\frac{h_c}{t_f}\right)^2} \text{ and } \phi = 0.7$$
(4-17)

$$F_{crx} = \frac{E_{Lw} E_{Tw} G_{LT}}{G_{LT}^2} \text{ and } \phi = 0.8$$
(4-18)

where

- $h_c$ = Cross dimension length of member,
- $t$ = Laterally unbraced length of member,
- $K$ = Effective length factor corresponding to the critical buckling,
- $r$ = Governing radius of gyration of the section corresponding to the axis of buckling,
- $E_L$ = Characteristic value of the longitudinal compression elastic modulus, adjusted in accordance with Section 2.4,
- $E_{Tw}$ = Characteristic value of the transverse compression elastic modulus, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,

**4.6 Square, Rectangular, and Circular Solid Sections**

The factored critical stress, $\phi F_{cr}$, shall be defined by the following equation:

$$F_{cry} = \frac{2 E_L}{\left(\frac{h}{t}\right)^2} \text{ and } \phi = 0.7$$
(4-19)

where $E_L$ is the minimum characteristic value of the longitudinal compression elastic modulus of the solid section among elements comprising the cross section, adjusted in accordance with Section 2.4 if an applicable materials selection from data exceeding the radius ratio of $r/h = 0.05$ in accordance with Table 2-1.

## 4.5 COMPRESSION STRENGTH FOR MEMBERS WITH OTHER CROSS SECTIONS

The nominal axial compression strength of a member having a geometry cross section other than those presented in Sections 4.4.1 through 4.4.6, shall be determined in accordance with Section 2.5.2.

## 4.6 COMPRESSION STRENGTH FOR BUILT-UP MEMBERS

The design strength of built-up members shall be determined in accordance with Section 2.3.2.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 17

<!-- Page 33 -->

This page intentionally left blank

<!-- Page 34 -->

# CHAPTER 5
# DESIGN OF MEMBERS FOR FLEXURE AND SHEAR

## 5.1 SCOPE

This chapter provides provisions for design for flexure and shear of pultruded FRP members that act as beams. It is assumed that the beam is a principal axis of the cross section that passes through the shear center along the line of the resultant force acting at any height perpendicular to the axis against torsional deflection.

## 5.2 DESIGN REQUIREMENTS FOR FLEXURE

### 5.2.1 Design Basis Members shall be designed such that

$$M_u \leq \lambda \phi M_n$$
(5-1)

where

- $M_u$ = Required factored flexural strength;
- $M_n$ = Nominal factored flexural strength based on applicable limit state per Sections 5.2.3.1 or 5.2.3.2;
- $\lambda$ = Time effect factor as defined in Table 2-1; and
- $\phi$ = Resistance factor as defined in Section 5.2.2 to Section 5.2.10.

For doubly symmetric and simply symmetric shaped members in bending, the factored nominal strength shall be determined per Section 5.2.3.1.

The nominal flexural design strength for shapes with different fiber directions in the cross section (e.g., from having different material properties, the factored flexural strength shall be reduced by factored nominal strengths of section components with appropriate strain rates as determined per Section 5.2.3.2.

### 5.2.2 Material Rupture The factored nominal strength, $\phi M_n$, shall be calculated as follows:

$$\phi M_n = \phi F'_f S$$
(5-2)

and

$$\phi M = \phi F_f S$$
(5-3)

where

- $\phi$ = 0.65,
- $F_f$ and $\phi$ = 0.65;
- $F'_f$ and $S$ = Characteristic value of the longitudinal tensile strength and compressive strengths respectively, adjusted in accordance with Section 2.4, and
- $S = S_t$ = Elastic section modulus of the section with respect to the axis of bending.

### 5.2.3 Local Buckling The factored moment flexural strength, $\phi M_n$, determined as detailed as follows:

$$\phi M_n = \phi F_n S$$
(5-4)

where

- $\phi$ = 0.8,
- $F_n$ = Critical buckling, associated with the extreme surface in the flexural stress block; shall be defined in accordance with Section 5.2.3.1 or 5.2.3.2;

### 5.2.3.1 Local Buckling Stress about the Major Axis The critical stress, $F_n$, shall be taken as the lesser of the local buckling stress for the compression flange, $F_{crf}$, and local buckling stress of the web, $F_{crw}$, defined as

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-5)

$$F_{crw} = \frac{13\sqrt{E_L G_{LT}}}{h_c^2}$$
(5-6)

where

- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $b$ = Compression flange width,
- $t$ = Compression flange width,
- $E_L$ = Characteristic value of the longitudinal modulus of the web, adjusted in accordance with Section 2.4, and
- $h_c$ = Double 2.4,
- $E_L$ = Characteristic value of the transverse modulus of the web, adjusted by the requirements of Section 2.4,
- $h_c$ = Characteristic value of the longitudinal modulus of the web, adjusted by the requirements of Section 2.4,
- $h$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $t_w$ = Clear depth of flexural section, and
- $t$ = Web thickness.

Alternatively, the design strength can be determined directly following the procedure of Section 2.5.2.

### 5.2.3.2 Doubly Symmetric I-Shaped Bent about the Major Axis The critical stress for I-shaped bent about the Major Axis, $F_n$, shall be taken as the lower of $F_{crf}$ and $F_{crw}$ defined as

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-7)

$$F_{crw} = \frac{13\sqrt{E_L G_{LT}}}{h_c^2}$$
(5-8)

where

- $b$ = Compression flange width,
- $t$ = Compression flange width,
- $E_L$ = Characteristic value of the longitudinal modulus of the web, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $E_T$ = Characteristic value of the transverse compression elastic modulus of the flange or of the compression elastic modulus of the web in the direction perpendicular to the pultrusion direction, adjusted by the requirements of Section 2.4,
- $h_c$ = Clear depth of flexural section,
- $h$ = Overall depth of flexural section, and
- $t$ = flange thickness

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 19

<!-- Page 35 -->

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-9)

$$F_{crw} = \frac{13\sqrt{E_L G_{LT}}}{\left(\frac{h_c}{t_w}\right)^2}$$
(5-10)

$$F_{crfz} = \frac{\left(\frac{2}{3}\right) \left[E_{Ly} E_{LT} G_{LT}\right]}{\left(\frac{bf}{t_f}\right)^2}$$
(5-11)

$$F_{crw} = \frac{13\sqrt{E_{Lw} G_{LT}}}{\left(\frac{h_c}{t_w}\right)^2}$$
(5-12)

where

- $b$ = Compression flange width,
- $t$ = Compression flange width,
- $t_w$ = Wall thickness,
- $E_L$ = Characteristic value of the longitudinal modulus of the web, adjusted in accordance with Section 2.4,
- $E_{LT}$ = Characteristic value of the transverse compression elastic modulus of the flange, adjusted by the requirements of Section 2.4,
- $E_{Lw}$ = Characteristic value of the longitudinal compression elastic modulus of the web in the direction perpendicular to the pultrusion direction, adjusted by the requirements of Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $\nu_{LT}$ = Poisson's ratio

Alternatively, the design strength can be determined directly using the procedure of Section 2.5.2.

**5.2.3.3 I-Shaped Bent about the Minor Axis** The critical stress, $F_n$, for I-shaped sections bent about the minor axis defined as follows:

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-9)

$$F_{crw} = \frac{E_L}{\left(\frac{h}{t_w}\right)^2}$$
(5-10)

where

- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $b$ = Full width of the longest leg, and
- $t$ = Full thickness of the leg.

Alternatively, the design strength can be determined directly using the procedure of Section 2.5.2.

**5.2.3.4 Square and Rectangular Box Members** The critical flexural buckling stress, $F_n$, about the major axis or local buckling defined as shall be taken as the lower of local buckling stress of the compression flange, $F_{crf}$, and local buckling stress of the web, $F_{crw}$, defined as

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-13)

$$F_{crw} = \frac{(2) \left[\sqrt{E_{Lw} E_{TW}} + \nu_{LT} E_{LT} + 2G_{LT}}\right]}{\left(\frac{h}{t_w}\right)^2}$$
(5-15)

where

- $G_{LT}$ = Characteristic value of the in-plane shear modulus of the web, adjusted in accordance with Section 2.4,
- $E_{Lw}$ = Characteristic value of the longitudinal modulus of the web, adjusted in accordance with Section 2.4,
- $E_{TW}$ = Characteristic value of the transverse modulus of the web, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4,
- $\nu_{LT}$ = Poisson's ratio of the web element associated with transverse deformation when compression is applied in the direction perpendicular to the pultrusion direction,
- $h$ = Overall depth of flexural section, and
- $t_w$ = Web thickness.

**5.2.3.5 Doubly Symmetric I-Shaped Members Bent about the Minor Axis** The critical stress, $F_n$, shall be taken as

$$F_{crf} = \frac{\left(\frac{2}{3}\right) \left[E_{Ly} E_{LT} G_{LT}\right]}{\left(\frac{h}{t_w}\right)^2}$$
(5-13)

$$F_{crw} = \frac{\left(\frac{2}{3}\right) \left[\sqrt{E_{Lw} E_{TW}} + \nu_{LT} E_{LT} + 2G_{LT}}\right]}{\left(\frac{h}{t_w}\right)^2}$$
(5-14)

where

- $E_{Ly}$ = Characteristic value of the longitudinal modulus of the flange or stem, whichever is smaller, adjusted in accordance with Section 2.4,
- $E_{Lw}$ = Characteristic value of the longitudinal modulus of the web, adjusted in accordance with Section 2.4,
- $E_{TW}$ = Characteristic value of the transverse modulus of the web, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4, and
- $\nu_{LT}$ = Poisson's ratio (to be taken as 0.3 in the absence of experimental data)

Alternatively, the design strength can be determined directly using the procedure of Section 2.5.2.

**5.2.3.6 Doubly Symmetric I-Shaped Members Bent about the Major Axis** The critical stress, $F_n$, shall be taken as

$$F_{crf} = \frac{G_{LT}}{\left(\frac{bf}{2t_f}\right)^2}$$
(5-13)

$$F_{crw} = \frac{\left(\frac{2}{3}\right) \left[\sqrt{E_{Lw} E_{TW}} + \nu_{LT} E_{LT} + 2G_{LT}}\right]}{\left(\frac{h}{t_w}\right)^2}$$
(5-15)

where

- $G_{LT}$ = Characteristic value of the longitudinal modulus of the

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 20

<!-- Page 36 -->

- $b$ = Compression flange width,
- $t_f$ = Thickness of the flange, and
- $t$ = Flange thickness (depth),
- $t_w$ = Thickness of the web.

### 5.2.4 Lateral-Torsional Buckling

**5.2.4.1** The factored flexural strength, $\phi M_n$, for doubly symmetric cross sections as well as singly symmetric cross sections, according to the following equation:

$$\phi M_n = \phi F_{LT} S_x \left(h_o / t_f\right) \left(F_t / F_y\right)$$
(5-16)

where $\phi$ = 0.65,

$$c_w = \frac{I_{yf} h^2}{4},$$
(5-17)

$$E_L = \frac{G_{LT} h_0^2 h / 4t_f (r_t - r_b)r_z}{12}$$

where

- $E_L$ = Characteristic value of the longitudinal modulus of the flange, adjusted in accordance with Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of the web, adjusted in accordance with Section 2.4,
- $r_t$ = Characteristic value of the transverse compression elastic modulus of the flange in between corner beams, adjusted in accordance with Section 2.4,
- $h$ = Total depth of beam,
- $h_o$ = Overall depth of the section,
- $r_b$ = Net section depth of beam,
- $F_L$ = Characteristic value of the lateral buckling stress,
- $t_f$ = Thickness of the flange,
- $r_z$ = Radius of the element of corner beams,
- $r_m$ = Maximum depth of the element of the section between nearest point at the member,
- $t_w$ = Thickness of the web in constant.

**5.2.4.2 Unsupported Members:** Section 2.4 through the lateral strength from lateral face to the lateral point of compression section. A member subject to the lateral side and it shall be determined following the support plane of the cross section. The lateral point is subject to the lateral side and lateral buckling failure. For members when a connection point is subjected to the lateral side and when a connection force component is not the plane of the connection, When a connection point is subjected to the lateral direction with a direction face and it shall take contact from the support plane and parallel to direction connection force acting from perpendicular to the plane of connection force. Based on the moment, the effect at the support plane of the member is subject from perpendicular plane of connection force or direction of a plane such that it shall be at the plane of the lateral face for direction connection shall be factored by the contact:

$$C_b = 2 M_{max} + 3 M_A + 4 M_B + 3 M_C$$
(5-17)

where

- $M_{max}$ = Absolute value of maximum bending moment in the unbraced segment,
- $M_A$ = Absolute value of moment at quarter point of the unbraced segment,
- $M_B$ = Absolute value of moment at centerline of the unbraced segment, and
- $M_C$ = Absolute value of moment at three-quarter point of the unbraced segment.

$C_b$ is permitted to be conservatively taken as 1.0 for all cases. For cantilevers or overhangs where the free end is unbraced, $C_b$ = 1.0.

## 5.3 DESIGN OF MEMBERS FOR SHEAR

### 5.3.1 Design Basis Members shall be designed such that

$$V_u \leq \lambda \phi V_n$$
(5-18)

where

- $V_u$ = Required shear strength due to factored loads;
- $\phi$ = Resistance factor defined in Sections 5.3.2 and 5.3.3,
- $\lambda$ = Time effect factor specified in Table 2-1; and
- $V_n$ = Nominal shear strength defined in accordance with Section 5.3.2 and 5.3.3.

The factored shear strength of all members having open cross sections shall be determined in accordance with Section 5.3.2.

The nominal shear strength of members with other cross sections shall be determined in accordance with Section 2.5.2.

The nominal shear strength for all members having open cross sections other than those section defined Section 5.3.2 shall be determined according to Section 2.5.2.

## 5.4 DESIGN OF MEMBERS FOR CONCENTRATED TRANSVERSE FORCES

$\phi M_n$ for a perpendicular $M_u$ shall be designed when there is a concentrated force located along the length of the beam, the section shall be designed to resist the local stresses caused by the bearing load.

$$\phi F_{cr} = \lambda \phi F_{crt}$$
(5-19)

where

- $\phi$ = Required strength of members due to concentrated force,
- $\phi$ = 0.8,
- $\lambda$ = Time effect factor specified in Table 2-1, and
- $F_{crt}$ = Specified critical buckling stress of members under a concentrated force determined in accordance with Sections 5.4.2, 5.4.3, 5.4.4, 5.4.5, 5.4.6.

The provisions of this section are to be used to provide concentrated transverse force to member. The method shall be determined under a concentrated load acting on elements of the member under concentrated force factor. A bearing load under $\phi$ material rupture factor of the web in flexure or direct shear shall be determined in accordance with Section 2.4. Equations to estimate bearing members shall be provided when

$$V_u \leq \frac{F_{yt} t_w}{5} + \phi t_w d \phi S$$
(5-20)

where

- $\phi$ = 0.8, and
- $S_w$ = length into the center-web which the specified beam, bearing length by this length of the element which shall be subject to the web member when the beam end, according to Equation (5-20) for the web member when the web bearing load is applied.

---

**22** STANDARD ASCE/SEI 74-23

<!-- Page 37 -->

The nominal shear strength for all members having open cross sections other than those sections defined in Section 5.3.2, shall be determined in accordance with Section 2.5.2.

### 5.3.2 Web Stiffness The use of stiffness to improve the web strength in shear is out of scope for this document.

The longitudinal web area shall be the verticals element area used in the force computation.

$$GF_{crwb} = 0.35 F_{crG}$$ $\frac{t_w}{d_w}$
(5-20)

where $d_w$ shall be the web's depth and $t_w$ is the web's width. For members in Section 2.4, and the flexure of longitudinal members apply to Section 2.4. And the flexure of the member load shall be the section of the weak of web distance to the section of the web shall be used to the section modulus of the flange also in (b).

Stiffener shall be braced to the vertical element and extend the full depth of the member. As in an example web panel shear (a) through the member flange where the section or web depth of the member when the member is perpendicular stiffener flange at the load point may be determined per the member when the member perpendicular element is located at the section modulus of the compressive area under the load acts.

## 5.4 DESIGN OF MEMBERS FOR CONCENTRATED TRANSVERSE FORCES

A flexure at supports or a supports of point loads or concentrated force point along the length of the beam, the section shall be designed to resist the local stresses caused by the bearing load.

$$F_u \leq \lambda \phi F_{cri}$$
(5-28)

where

- $F_u$ = Required strength of members due to concentrated force;
- $\phi$ = 0.8;
- $\lambda$ = Time effect factor specified in Table 2-1; and
- $F_{cri}$ = Nominal critical buckling stress of members under a concentrated force determined in accordance with Sections 5.4.2, 5.4.3, 5.4.4, 5.4.5, 5.4.6.

The provisions of this section are to be used to predict concentrated load effects. A bearing load at supports or reactions of the section modulus of concrete load states of (1) material rupture at (2) web distance bearing where the member force may be determined per the following equations. The critical stress for material rupture shall be determined per member under $\phi$ material rupture factor of the member or web.

$$V_u \leq \left(\frac{F_{ycr} t_w}{5}\right) + \phi t_w d \phi S$$
(5-29)

where

- $\phi$ = 0.8;
- $F$ = Required in plane shear strength per unit length,
- $F_{cri}$ = Characteristic value of the interlaminar shear strength, defined by the requirements of Section 2.4,
- $\nu_{LT}$ = Poisson's ratio, and
- $t_w$ = Thickness of the bearing plate, or (mm),
- $d_w$ = Width of shear bearing constant from the top/bottom of the section shall be taken into account from the member web thickness of the maximum plate deflection modulus of Section 5.2.4.
- $h_w$ = Depth of the web.

Under Concentrated Load The factored strength, $\phi F_n$, of a member shall be determined from:

$$\phi F_n = \phi t_c \left(1 + \frac{0.06}{1 + \left(\frac{t_c}{t_w}\right)^{1.5}}\right) \text{ with } \phi = 0.7$$
(5-30)

where

- $d_w$ = Overall depth of the member,
- $F_{yield}$ = Characteristic value of the interlaminar shear strength, defined by the requirements of Section 2.4,
- $t_w$ = Thickness of the bearing plate, or (mm),
- $N_w$ = Horizontal distance, defined by the flange thickness,
- $t_c$ = Thickness of the bearing plate at supports or,
- $h_w$ = Depth of the web.

When $t_w$ is the thickness of the plate, and the plate's depth $h_w$ be more continuous under the bearing load shall be taken as

$$F_{ocal} = 0.84 k_N A_f t_f F_c$$
(5-31)

where

- $k_N$ = Effective area = $L_t t_f$,
- $A_f$ = Clear distance between flanges or webs at the load point,
- $F$ = Thickness of the web in (mm),
- $t$ = Flange thickness, and
- $L_t$ = Characteristic value of the longitudinal modulus of the web, adjusted by the requirements of Section 2.4,
- $E_T$ = Characteristic value of the transverse compression modulus at the flange, adjusted by the requirements of Section 2.4,
- $G_{LT}$ = Characteristic value of the in-plane shear modulus of the web,
- $\nu$ = Characteristic value of the in-plane shear modulus, and
- $t$ = Characteristic ratio for available valid data on $\nu$ ($t$)

**5.4.5 Factored Strength of Members Due to Three-Point Flexural Failure** The factored strength of members shear under three-point load shall be determined according to Section 2.5.2.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 21

<!-- Page 38 -->

$$F_{cra} = \frac{E_T}{\left(\frac{h_c}{t}\right)^2}$$
(5-28)

In the presence of a hole or other discontinuity, the nominal factored shear strength per unit length, $\phi V_n$, shall be multiplied by the open-hole (notched) strength reduction factor. The open-hole (notched) strength reduction factor is equal to the ratio between the notched nominal strength and un-notched nominal strength.

### 5.3.2 Nominal Strength of Plates Subjected to Longitudinal Tension or Compression The nominal strength, $\phi F_n$, shall be determined from

$$\lambda \phi F_n \left(\frac{A_{e}}{A_{g}}\right)$$
(7-12)

where

- $A_e$ is the effective net area of plate subjected to tension per Section 2.10.3 or
- $A_e$ is the effective compression area per Section 2.10.4, or
- $A_g$ is the gross area of the plate in accordance with Section 2.4, and
- $\phi$ and $\lambda$ are determined from Equation (5-6) for the gross area in tension.

Tension The nominal tensile strength, $V_n$, shall be determined from

$$\lambda \phi F'_t A_g$$
(7-13)

where

- $A_e$ is the effective net area of plate subjected to tension per Section 2.10.3,
- $F'_t$ is the characteristic value of the longitudinal tensile strength, adjusted in accordance with Section 2.4, and
- $\phi$ = 0.65.

**7.5.3 Nominal In-Plane Material Rupture Strength of Plates Subjected to In-Plane Compressive Strength** The nominal in-plane compressive strength, $\lambda F_n$, shall be determined from

$$\lambda \phi F'_c A_e$$
(7-14)

where

- $\phi$ = 0.8, and

**7.5.4 Nominal Buckling Strength of Plates Subjected to In-Plane Compressive Loading** The nominal buckling strength of plates, $\phi F_n$, shall be determined from the bearing strength of plates per Section 2.4. The plate shall be proportioned such that

$$\lambda \phi F_{cr}$$
(7-15)

where

- $\lambda \phi F_{cr}$ is the characteristic value of the through-the-thickness strength, adjusted in accordance with Section 2.4,
- $F'_c$ is the characteristic value of the longitudinal through-the-thickness buckling strength, adjusted as appropriate (or not used in accordance with Section 5.2.3, and
- $\phi$ = 0.8.

When the component is pulled apart perpendicular to the plane surface, failure (bearing strength can be determined for (a) $L_e/t \geq 2$ or (b) $L_e/t < 2$) shall be applied, where $L_e$ is the bearing length (the length over which the component is pulled apart perpendicular to the plane of laminate) and the material transverse strength, adjusted by the requirements of Section 2.4.

The nominal pull-through strength per fastener, $R_n$, shall be calculated as:

$$\left\{(d_h + t_f)t_f F_t\right\} \text{ with } \phi = 0.7$$
(7-16)

The nominal pull-through strength per fastener, $R_n$, shall be calculated as follows:

where

- $d_h$ = Required pull-through strength per unit length, and
- $t_f$ = thickness, and
- $R_n$ = Nominal pull-through strength per fastener shall be calculated as follows:

$$R_n = F_t d_h t_f \text{ for } L_e/t_f \geq 2$$
(7-16)

and

$$\phi \geq R_n \text{, for } L_e/t_f < 2$$
(7-17)

**7.6.2 Nominal Material Rupture Strength of Plates Subjected to Out-of-Plane Shear Conditions** The nominal maximum compressive strength, $\lambda F_{cr}$, shall be determined from

$$\lambda \phi \frac{E_t F_{cr}}{t^2}$$
(7-15)

The nominal in-plane transverse compressive strength, $\lambda F_{cr}$

where

- $t$ = Thickness of the plate,
- $E_t$ = Characteristic value of the longitudinal compressive modulus, adjusted in accordance with Section 2.4, and
- $F_{cr}$ = Characteristic value of the transverse compressive strength, adjusted by the requirements of Section 2.4 and
- $G_{LT}$ = Characteristic value of the in-plane shear modulus

Longitudinal Compression The nominal buckling strength

---

**22** STANDARD ASCE/SEI 74-23

<!-- Page 39 -->

## 5.5 DESIGN FOR COPES, NOTCHES, HOLES, AND OPENINGS

### 5.5.1 Copes, Notches, Holes, and Openings in the Flange or Web

The effect of all copes, notches, holes, and openings on the nominal flexural strength and the nominal shear strength of members shall be determined. When the required strength exceeds the factored nominal strength of members at an unreinforced cope, notch, hole, or opening, doubler plates shall be used to increase the strength of the section at these locations.

### 5.5.2 Doubler Plate Requirements

Doubler plates shall be made of pultruded material and be mechanically fastened to transfer all required forces. The use of adhesive covering the entire surface area of the doubler plate, in addition to mechanical fasteners, is permissible, but the contribution of the adhesive strength of the joint per ASTM D1144 shall be neglected.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 23

<!-- Page 40 -->

This page intentionally left blank

<!-- Page 41 -->

$$J = \frac{\pi}{2} \left(R^4 - R_i^4\right)$$
(6-4)

For a rectangular tube, the torsional constant $J$ shall be taken as

$$J = \frac{2A^2}{d_w/t_w + b_f/t_f}$$
(6-5)

For a circular tube, the warping constant $C$ shall be taken as

$$C_w = \frac{\pi t(2R - t)^3}{2}$$
(6-6)

For a rectangular tube, the warping constant $C$ shall be taken as

$$C_w = 2t(b_f - t)(h - t)$$
(6-7)

where

- $A$ = Mean of the areas enclosed by the inner and outer boundaries,
- $b_f$ = Outer width of rectangular tube section,
- $b_f$ = Width of the flange between the centers of webs in rectangular tubes,
- $d_w$ = Clear depth of web,
- $h$ = Depth of rectangular tube section,
- $R$ = Outer radius of a circular tube,
- $t$ = Thickness of an element in the cross section,
- $T_c$ = Thickness of the flange, and
- $t_w$ = Thickness of the web.

For a circular hollow tube, shall be determined as the lower of Equations (6-8) and (6-9):

$$F_{cr} = \frac{0.2(E_T)^{5/8}(E_L)^{3/8}}{\left(\frac{R}{t}\right)^{3/2}} \leq F'_{LT}$$
(6-8)

$$F_{crf} = \frac{0.7(E_T)^{5/8}(E_L)^{3/8}}{\left(\frac{R}{t}\right)^{5/4}} \frac{1}{\sqrt{R}} \leq F'_{LT}$$
(6-9)

The critical torsional buckling stress, $F_{crz}$, shall not exceed the in-plane shear strength $F'_{LT}$ as given in Section 1.3.2.

where

- $E_L$ = Longitudinal compression modulus as modified by the requirements of Section 2.4,
- $E_T$ = Transverse compression modulus as modified by the requirements of Section 2.4,
- $R$ = Circular tube outer radius, and
- $t$ = Tube thickness.

### 6.4.2 Rectangular Hollow Tubes Subject to Combined Torsion, Flexure, and Axial Force

The interaction of torsion, flexure, and axial force shall be limited by Equation (6-10),

$$\frac{P_u}{P_c} + \frac{M_{ux}}{M_{cx}} + \frac{M_{uy}}{M_{cy}} + \left(\frac{T_u}{T_c}\right)^2 \leq 1.0$$
(6-10)

where

- $P_u$ = Required axial tensile strength or compressive strength due to factored loads determined in accordance with Section 2.5.3,
- $P_c$ = $\lambda \phi P_n$ = Design axial tensile strength as determined based on the requirements of Section 3 or design axial compressive strength as determined based on the requirements of Chapter 4,
- $P_n$ = Nominal value of axial tensile strength or axial compressive strength as modified by the requirements of Section 2.4,
- $M_u$ = Required flexural strength due to factored loads determined in accordance with Section 2.5.3,
- $M_c$ = $\lambda \phi M_n$ = Design flexural strength as determined based on the requirements of Chapter 5,
- $M_n$ = Nominal value of flexural strength as modified by the requirements of Section 2.4,
- $T_u$ = Required torsional strength due to factored loads determined in accordance with Section 2.5.3,
- $T_c$ = $\lambda \phi T_n$ = Design torsional strength as determined from Equation (6-1),
- $T_n$ = Nominal value of torsional strength [Equations (6-2a) or (6-2b)] as modified by the requirements of Section 2.4,
- $x$ = Subscript referring to strong axis bending for $M_u$, $M_c$, and $M_n$,
- $y$ = Subscript referring to weak axis bending for $M_u$, $M_c$, and $M_n$,
- $\phi$ = Resistance factor as defined in Chapters 3, 4, and 5 for tension, compression, and bending and Section 6.4.1 for torsion; and
- $\lambda$ = Time effect factor defined in Table 2-1.

---

**26** STANDARD ASCE/SEI 74-23

<!-- Page 42 -->

# CHAPTER 7
# DESIGN OF PLATES AND BUILT-UP MEMBERS

This chapter presents design provisions for rectangular plates and built-up sections, such as columns, beams, and plates and both pre-molded composite structural members.

## 7.1 SCOPE

The design provisions of this chapter apply to pultruded FRP structural shapes configured as flat plates and as built-up members such as columns and beams. Built-up members are subject to requirements specified in Section 7.8.

## 7.2 GENERAL PROVISIONS

For slender plates, design shall be made in accordance with provisions for dimensional, with a thickness that is significantly less than its width and length. The plate may be of rectangular shape or a regular shape with material transverse direction is perpendicular to the pultrusion direction only.

In this chapter, the plate is defined as a structural element with requirements applicable to pultruded plates in accordance with Section 1.3. Pultruded plates shall be designed for longitudinal bending in the direction of the reinforcement of the fibers in the material transverse direction will satisfy.

$$R_c \leq \lambda \phi R_n$$
(7-2)

where

where $F'_t$ is the characteristic value of the longitudinal flexural strength, adjusted by the requirements of Section 2.4 and $G_{LT}$ is the characteristic value of the in-plane shear modulus adjusted in accordance with Section 2.4.

The design strength shall be obtained based on the material properties of the plates, $F_n$, designed as appropriate for the materials. The ultimate strength of the pultruded plate shall be based on Section 2.5.2.

The plate shall be built-up structures subjected to combined forces shall be designed as per Sections 7.6 and 7.7. The design shall be determined in accordance with Section 3.3.2.

## 7.3 DESIGN OF PLATES SUBJECTED TO FLEXURE

### 7.3.1 Flexural Strength of Plates

The nominal flexural strength, $M_n$, shall be obtained for the limit state of the plate tested in which the material strength is applied to the requirements of Section 2.4. Plates under the pultruded conditions in accordance with Section 2.4. The section modulus shall be factored for the principal material directions.

$$M_c \leq \lambda \phi M_n$$
(7-3)

where

- $M_u$ = Required flexural strength per unit length,
- $\lambda$ = Time factor defined in Table 2-1, and
- $\phi$ = Resistance factor (specified in Section 7.3.2)

The nominal flexural strength in the material longitudinal direction shall be:

$$M_c = S F'_f$$
(7-4)

where $F'_t$ is the characteristic value of the longitudinal flexural strength adjusted by the requirements of Section 2.4 and $t$ is the thickness of the plate.

The nominal flexural strength in the material transverse direction shall be:

$$M_c = S F'_f$$
(7-5)

where $F'_t$ is the characteristic value of the transverse flexural strength, adjusted by the requirements of Section 2.4.

## 7.4 DESIGN OF PLATES SUBJECTED TO THROUGH-THE-THICKNESS SHEAR

### 7.4.1 Proportioning

The nominal shear strength, $V_n$, shall be obtained from the lower of the limit states of material strength and shear buckling. A plate not perpendicular to the loads shall be designed for the transverse shear in the plane of the plate shall be adjusted as appropriate for end use conditions in accordance with Section 5.2.3. The section shall be designed for the two material principal directions.

$$V_c \leq \lambda \phi V_n$$
(7-6)

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 27

<!-- Page 43 -->

where

- $V_u$ = Required shear strength per unit length,
- $\phi$ = 0.70, and
- $\lambda$ = Time factor defined in Table 2-1.

where $F'_t$ is the characteristic value of the through-the-thickness shear strength, adjusted by the requirements of Section 2.4.

The nominal shear strength, $V_n$, also is rupture as shear at a plate shear connection when rupture in a plate connection shall be considered perpendicular to the material longitudinal direction shall be:

$$V_c = \lambda \phi F'_t A_e$$
(7-7)

where $F'_t$ is the characteristic value of the through-the-thickness shear strength, adjusted by the requirements of Section 2.4 and $A_e$ is the effective net area of the longitudinal bend, adjusted in accordance with Section 2.4.

The nominal shear strength, $V_n$, also is rupture as shear at a plane perpendicular to the material transverse direction shall be:

$$V_c = \lambda F'_t S$$
(7-8)

where $F'_t$ is the characteristic value of the through-the-thickness shear strength, adjusted by the requirements of Section 2.4 and $t$ is the width of the plate measured from the center of material shear strength to the plate center side of the beam or material when the component is pulled apart perpendicular to the plane of laminate. For pultruded plates, the critical stress shall be determined from the plate thickness.

The nominal shear strength per unit length, $\phi_n$, shall be based on plate pull-through strength (e.g. out of plane) pulled perpendicular to the beam when a perpendicular element that is incongrous. The critical stress for open bolt (notched) strength reduction factor, the open bolt (notched) strength reduction factor is equal to the ratio between the notched ultimate strength and un-notched ultimate strength.

## 7.5 DESIGN OF PLATES SUBJECTED TO IN-PLANE FORCES

### 7.5.1 Nominal Tensile Strength of Plates

The nominal tensile strength of plates, $N_t$, shall be obtained according to the Limit states of material strength and hole reduction in accordance with Section 2.4. The plate shall be proportioned such that

$$N_u \leq \lambda \phi N_t$$
(7-9)

where

- $N_u$ = Required tensile strength per unit length,
- $\phi$ = 0.65, and
- $\lambda$ = Time factor defined in Table 2-1.

**7.5.2 Nominal Material Rupture Strength of Plates Subjected to Longitudinal Tension or Compression** The nominal in-plane material strength, $N_t$, shall be determined from

$$\lambda \phi F'_t A_e / b$$
(7-10)

where

- $F'_t$ = Thickness of the plate,
- $A$ = Reduction of the longitudinal compressive strength, adjusted in accordance with Section 2.4, and
- $G_{LT}$ = Characteristic value of the in-plane shear modulus, adjusted in accordance with Section 2.4.

**7.5.3 Nominal In-Plane Material Rupture Strength of Plates Subjected to In-Plane Compressive Strength** The nominal in-plane compressive strength, $N_c$, shall be determined from

$$N_c = \lambda \phi F'_c A_e$$
(7-14)

The nominal in-plane transverse compressive strength, $N_{LT}$, of a plate, shall be determined from:

where

- $t$ = Thickness of the plate.

In the presence of a hole or other discontinuity, the nominal factored shear strength per unit length, $\phi V_n$, shall be multiplied by the open hole (notched) strength reduction factor. The open-hole (notched) strength reduction factor is equal to the ratio between the notched nominal strength and un-notched nominal strength.

### 7.5.2 Nominal Strength of Plates Subjected to Longitudinal Tension The nominal tensile strength, $N_t$, shall be determined from

$$\lambda \phi F'_t A_e / t$$
(7-12)

where $A_e$ is the effective net area of plate subjected to tension per Section 2.10.3 or is the gross area (if there are no holes, A = gross area) per Section 2.4, $F'_t$ is the characteristic value of the longitudinal tensile strength, adjusted in accordance with Section 2.4, and $\phi$ = 0.65.

**Tension** The nominal tensile strength, $V_n$, shall be determined from

$$\lambda \phi F'_t A_e$$
(7-13)

where $A_e$ is the effective net area of plate subjected to tension per Section 2.10.3, $F'_t$ is the characteristic value of the longitudinal tensile strength adjusted in accordance with Section 2.4 and $\phi$ = 0.65.

**7.5.3 Nominal In-Plane Material Rupture Strength of Plates Subjected to In-Plane Compressive Loading** The nominal in-plane compressive strength, $N_c$, shall be determined from

$$\lambda \phi F'_c A_e$$
(7-15)

The nominal in-plane transverse compressive strength, $N_{LT}$, of a plate, shall be determined from:

where

- $t$ = Thickness of the plate.

**7.5.4 Nominal Buckling Strength of Plates Subjected to In-Plane Compressive Loading** The nominal buckling strength of plates, $N_n$, shall be determined from

$$N_c = \lambda \phi F_{cr} t$$
(7-15)

where $F_{cr}$ is the characteristic value of the through-the-thickness buckling strength, adjusted in accordance with Section 2.4 and $\phi$ = 0.8 is the nominal in-plane longitudinal compressive buckling strength, adjusted as appropriate (for end use in accordance with Section 5.2.3 and $\phi$ = 0.8.

## 7.6 DESIGN OF PLATES FOR SERVICEABILITY

Plates and built-up members shall be designed to have adequate stiffness in accordance with the provisions in Section 1.6.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 28

<!-- Page 44 -->

of a rectangular plate supported around the edges shall be obtained according to the limit states of (1) material rupture in bending and (2) plate buckling. $F_{cr}$ is obtained from

$$N_{Lt} = F_{crl}t$$
(7-17)

$$F_{crl} = \frac{\pi^2}{3} \left(\frac{t}{l}\right) \left\{(M_c + \nu_{LT} E_{TL} + 6.5 E_{TG} + 3r_{LG})\right\}$$
(7-18)

where

- $E_{TG}$ = Longitudinal elastic buckling stress adjusted by the requirements of Section 2.4 and the characteristic value of the effective length factor, $K_{eff}$,
- $E_{TL}$ = Plate buckling failure transverse loading coefficient;
- $\nu_{LT}$ = Poisson's ratio,
- $M_c$ = Characteristic value of the longitudinal compressive strength, adjusted in accordance with Section 2.4 and
- $G_{LT}$ = Characteristic value of the transverse elastic modulus adjusted by the requirements of Section 2.4, and
- $E_{TL}$ = Characteristic value of the transverse compression elastic modulus adjusted by the requirements of Section 2.4, and
- $r_{LG}$ = Poisson's ratio associated with transverse deformation when compression is applied in the longitudinal direction adjusted to account for shear lag effects as indicated by available test data on $\nu_{LT}$ and $\phi = 0.8$.

### 7.6.4 Nominal Buckling Strength of Plates Subject to Combined Longitudinal and Transverse Compression

The in-plate buckling strength of a plate subjected to combined longitudinal and transverse compression shall be determined as follows:

$$\left\{\frac{N_c}{N_{crl}} + 2\sqrt{2} \left(\frac{N_{LT}}{N_{crt}}\right)^2\right\} t \leq t_c$$
(7-20)

$$\left(\frac{N_c}{N_{crl}}\right)^2 \left(\frac{N_{LT}}{N_{crt}}\right) \leq t_c$$
(7-21)

where

- $F_{crl}$ = Longitudinal elastic buckling stress adjusted by the requirements of Section 2.4 and the characteristic value of the effective length factor, $K_{eff}$,

The ratio of applied transverse to longitudinal compressive loading shall be such that $N_{LT}$ shall be determined in accordance with Section 7.5.4.

For other ranges of applied transverse to longitudinal compressive loading ratio, $N_{LT}$ strength shall be determined in accordance with Section 7.5.2.

## 7.7 DESIGN OF PLATES SUBJECTED TO IN-PLANE SHEAR LOADING

### 7.7.1 Nominal In-Plane Shear Strength of Plates

The design limit in-plane shear strength, $N_{LT,s}$, shall be the lower value according to:

where $E_L$ is the thickness of the longitudinal elastic modulus of the plate, adjusted by the requirements of Section 2.4 and $G_{LT}$ is the length of the edge of the plate, $F_{int}$ is the characteristic value of the interlaminear shear strength, adjusted by the requirements of Section 2.4, and $b$ is the depth of the plate and $t$ is the thickness of the plate. $M_c$ in Equation (7-27) shall be dependent upon the edge boundary conditions and is given for two common situations in the plate center shall be determined as:

$$\left\{\begin{array}{l}
\frac{2\pi t + 1.5k(t^2)}{19 + k(l)} \\
[or]
\frac{19 + k(l)}{t(1 + k(t)^2)}
\end{array}\right\} \cdot \sqrt{t(E_{TG}w + 2H_{LT})} \quad B_L \leq 1$$
(7-27)

$$a_{LT} = 2a_L \pm E_{TG}v$$
(7-27)

where

- $t$ = Short length of the plate in the material transverse direction,
- $l$ = Long length of the plate per Section 2.4, and
- $\lambda$ = Time factor defined in Table 2-1.

The nominal in-plane shear strength shall be determined from

$$F_{cry} = 4 a_l / F_{ELT} + 8.5 / G_c \cdot \sqrt{E_L E_w}$$
(7-28)

where $F_{cry}$ is the characteristic value of the material transverse shear strength, adjusted by the requirements of Section 2.4 and $G_c$ is the in-plane shear modulus, which is smaller, adjusted in accordance with Section 2.4.

## 7.8 DESIGN OF BUILT-UP MEMBERS

The design strength shall be determined in accordance with Section 2.3.2.

## 7.9 DESIGN OF PLATES FOR SERVICEABILITY

Plates and built-up members shall be designed to have adequate stiffness in accordance with the provisions in Section 1.6.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 29

<!-- Page 45 -->

This page intentionally left blank

<!-- Page 46 -->

# CHAPTER 8
# DESIGN OF BOLTED CONNECTIONS

## 8.1 SCOPE

The design provisions of this chapter shall apply to bearing-type connections with cold-formed or hot-formed metallic fasteners, such as bolts, screws, and pins, and other FRP and/or metallic components, and which result in a joint using the pultruded FRP members, such as elements and plates. The connections for bolt configuration shall be one of stainless-steel bolts, Commercial fasteners, shall be used. Elements within FRP members, which provide strength through friction, such as clamps shall be designed to carry shear or tension forces applied directly to members. This chapter do not apply to adhesive bonded connections.

Bolts referenced in this chapter shall conform to the provisions of Section 5.2.1.

The characteristic strengths appropriate to the material of an FRP component in a connection shall be used with the strength requirements as defined in this chapter.

The types of connection covered shall take the form of the shear configuration in Section 5.3 in which the FRP component interacts with the metallic or FRP connecting components. Simple and compound pin-connected connections, and connections in which FRP members interact with another FRP component or metallic members shall be permitted.

Fiber-reinforced polymer connections may be permitted when documented by load data qualified on the basis of Chapter 7 by load test provisions of Appendix 7A. The provisions of Chapter 7 apply to FRP solid materials or FRP and metallic pultruded nuts, if these nuts and bolts both move as an integral body (not partial bearing) when adjusted in accordance with rules specified in Section 5.2.1 (1) structural members attached or constructed with other materials, and (2) connections in which the bearing resistance can be calculated through standard design provisions.

Bolts referenced in this chapter shall conform to the provisions of ASTM A193 and ASTM F593, and nuts with other FRP requirements specified in Table 3.1.1.

The detailing of a connection with more than three bolts in a connecting line parallel to the direction of forces and shall be continued by adding the additional shear and tension bearing forces of bolts when at least four bolts, Bolts shall be arranged so as two rows parallel to the longitudinal direction.

The characteristic strength appropriate to the material of an FRP component in a connection shall be used with the strength requirements covered in this chapter in accordance with the procedures and elements, and the geometry of bolts or cut-and-connections.

**Figure 8-1. Connection geometry and definitions for a row of bolts (top) and multiple bolt group (bottom) and right-side three rows and three columns (maximum number of bolts).**

[DESCRIPTION OF FIGURE: The figure shows connection geometry diagrams with spacing dimensions for bolts. The top diagram shows a single row of bolts with spacing indicators. The bottom diagram shows a grid of bolts arranged in three rows and three columns with various spacing measurements labeled including edge distances, pitch, and gauge.]

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 31

<!-- Page 47 -->

Unreinforced or unreinforced connected members shall be designed in accordance with the requirements of Section 5.3.2.

### 8.1.1 Placement of Bolts

Members joining at a connection shall be arranged so that the center of gravity of connected elements coincides with the center of gravity of the connector unless provision is made for the effects of eccentricity so determined by an analysis and design of connection. Center of gravity provisions for connections of angles or other off-centered members with the center of gravity of the connector unless coincides with the center of gravity of the connector unless provision is made for the eccentricity in the system.

### 8.1.2 Framing Connections

Simple frame connections shall be made with fasteners, which are essentially flexible with respect to the load-carrying capacity of connected members. If the connection is rigid, the use of a single-angle bracket, (slip-single-center), provides sufficient clearance in the point of bearing between the member. A rigid frame connection, such as one utilizing end plates or cover plates in addition with welded or bolted connection with no rotation of the elements at the joint face between members, shall be in accordance with the requirements of Section 5.3.2.

### 8.1.3 Connectors

All connectors, such as bolts and other fastening means, shall have sufficient capacity to sustain forces at minimum of two FRP and/or metallic elements when load has been transferred to sections.

A design strength through all required splice and column splice connections shall be at least (1) three-quarter of the tensile strength of the connected member when an specified bearing capacity to exceed the Section 5.2.1.

When a connector is loaded parallel to FRP member or subject to combined loading, the tensile strength of the connected members shall equal or exceed forces as specified for Chapter 5 and Section 8.2.3.2 and shall not exceed the strength of the members, defined in Chapter 2.

### 8.1.4 Scope

Bolts, nuts, and washers in bolted connections between metallic and FRP elements shall be in accordance with provisions of ASTM F593 and ASTM A193 (for ASTM F593 or ASTM A193 and bolted connections, respectively), and the design requirements provisions in Chapter 2.

A design strength through all required steel bolts and columns splice connections shall have at least (1) three-quarter of the tensile strength of the connected members when an specified bearing capacity.

In this section, the connection strength depends on the strength of the nuts and of the stress ratio of bolts based upon the bearing test (in this ratio also to Section 8.90).

### 8.2 CONNECTION DESIGN

**8.2.1 Design Basis** The design strength of a bolted connection shall be determined based on the strength of the basic connection through load as determined for applicable critical strengths; also, the strength of the metallic connectors also critical strength is shown in the following equations:

$$R_u \leq \lambda \phi R_n$$
(8-1)

where

- $R_u$ = Required connection strength;
- $R_n$ = Resistance factor for bolted connection depending on applicable limit state as defined in Sections 8.2.2 to 8.2.5;
- $\lambda$ = Time effect factor specified in Table 2-1; and
- $R_n$ = Nominal connection strength defined in Sections 8.2.2 to 8.2.5 and determined by the governing failure of FRP part.

[THIS IS TABLE: Minimum Requirements for Bolted Connection Geometry and Detailing]
The table shows minimum required spacing and edge distances for different notations including:
- $D_{nom}$ : Nominal diameter of a bolt = diameter + tolerance, 1/8" less at bolt holes
- $e_s$ : End distance (Force at hole edge)
- $e_t$ : Edge distance (No force at hole edge)
- $g$ : Gauge spacing with notation "3d" for minimum requirement
- $p$ : Gauge (perpendicular) spacing with notation "3d" for minimum requirement
- $p_{max}$ : Maximum pitch with notation "24 or 12t_c (100 mm), Both limits apply"

Notes indicate:
- a) In the normal direction of load
- b) Perpendicular to the direction of load when the connected member is grounded under load or force
- Values p_c , p_max for min, connection strength shall be reduced

---

**32** STANDARD ASCE/SEI 74-23

<!-- Page 48 -->

[THIS IS FIGURE: Two side-by-side diagrams showing loading directions for bolted connections. Left diagram shows "Loading parallel to c.g., R_g" with holes and loads indicated. Right diagram shows "Loading perpendicular to c.g., R_c" with similar hole and load arrangements]

**Figure 8-2. Loading directions for reinforced plates.**

Where the pitch spacing, $p_s$ is less than specified in Table 8-1, $C_p$ shall be taken as 0.60 (or the ratio of the actual pitch spacing to that listed in Table 8-1, whichever is less. Refer to Section 8.2.7 for special reduced connection strengths.

### 8.2.2 Single Bolt Bolted Connections

The factored nominal connection strength, $\phi R_n$, shall be the maximum value of strength determined in accordance with Sections 8.2.3.1, 8.2.3.2, 8.2.3.3, 8.2.3.4, and 8.2.3.5. All minimum geometry and detailing provisions of Table 8-1 shall be satisfied.

### 8.2.2.1 Bolt Strength, $R_b$

The bolt strength is calculated in Section 8.2.3.1.

The nominal strength of a single bolt, $R_n$, shall be determined from the provisions in Section 8.2.3.1 for single shear and Table 8-2.

When bolt shear strengths are calculated based upon gross area of the bolt, gross area shall be calculated from the nominal diameter of the bolt. Strength $R_n$ based on the cross-sectional area of the bolt threads, $A_t$, determined when the shear plane of the bolt passes through the threaded section of the bolt as defined in Section 8.2.3.2, 8.2.3.3, and is verified in Equation (8-13) shall be permitted from Figure 8-2.

The connection strength $R_n$ shall not be determined when two connections fail independently, one perpendicular to bearing load at the right side of the figure. Strength $R_b$ or one perpendicular to bearing (a.g., a single to bearing, Strength $R_e$ shall be determined when the bearing bolt is located perpendicular or through the nominal strength, in accordance with connection, the case of the bolt fails at an angle, Section 8.2.3.2 and 8.2.3.5, and is verified when perpendicular distance from a right angle from angle is not at a right angle. Either on shearing, tension, two-shear planes or either case one parallel bearing surfaces when a perpendicular element (e.g., single to bearing), or when bearing load and parallel plane perpendicular of the member of shear and tension forces of bolts when a perpendicular force component is not the failure of the connection. Where a connection force component is not in the plane, based on the member of the fasteners of the hole when at least at the right angle relative of bearing (e.g. (8-2)) when a bolt is subjected to combined tension and shear stresses, the effect at the diagonal distance (e.g., bearing load shall be given by Equation (8-13).

**Table 8-2. Nominal Stress of Bolts.**

| Applied Load Condition | Nominal Stress Per Bolt Area, $F_n$ |
|------------------------|-------------------------------------|
| | ASTM F1130/F1130M | ASTM A307 | ASTM F593¹ |
| Tension, $F_{nt}$ | Static | 90 ksi | 45 ksi | as specified in ASTM F593¹ |
| | Threads excluded from shear plane | (620 MPa) | (310 MPa) | $0 F_{nt}$ |
| | Threads included in shear plane | 81 ksi | 38 ksi | |
| Shear, $F_{nv}$ | Threads excluded from shear plane | 54 ksi | 27 ksi | |
| | Threads included in shear plane | (370 MPa) | (190 MPa) | $0 F_{nv}$ |
| | | 68 ksi | 31 ksi | |
| | | (470 MPa) | (210 MPa) | |

¹ For A307 bolts use in accordance with the requirements in the ASTM F1130/F1130M and does not comply with the other provisions for A307 bolts defined in ASTM A307-14 unless explicitly defined in the applicable design codes.

² Current stress for stainless steel in Alloy Group 1 (304) and Alloy Group 2 (316).

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 33

<!-- Page 49 -->

- $F_{nv}$ = Nominal value of shear stress defined in Table 8-1; and
- $F_{nt}$ = Nominal value of tensile stress defined in Table 8-1.

The available shear stress of the bolt shall equal or exceed the factored load is determined by bearing in accordance with the requirements of Section 8.2.2, or by shear as defined in Table 8-1.

### 8.2.2.2 Pull-Through Strength, $R_t$

The pull-through strength is the force of:

$$R_{pt} = 0.5 d_h t_r F_{pt}$$
(8-2)

where

- $\phi$ = 0.5,
- $d_h$ = Bolt diameter calculated in Section 8.2.2.1,
- $t_r$ = Net tension strength, calculated in Section 8.2.2.4,
- $F_{pt}$ = Pull-through strength, calculated in Section 8.2.2.5,
- $F_b$ = Bearing strength of the FRP material in accordance with Equation (8-7) or when the calculated pull-through shear strength of the materials of two FRP materials in shear.

Figure 8-2 defines the directions of the member for bearing shear through the thickness of the plate. The location of the bearing areas are determined by bearing (e.g. calculated), or when the bearing is located at the plate edge (as Section 4.2.1).

**8.2.2.3 Tension and Shear Strength of Bolts, $R_{ts}$** The design strength of a bolt subjected to combined bearing and shear strength of the bearing areas shall be determined from the provisions given in Table 8-2, when $F_t$ is computed at the member surface face. For the resulting tension stress that bearing stress shall include a shear force (see Section 8.6), the design strength shall be less than or equal to $F_{nv}$ shear stress. The bearing capacity shall include a shear force in the plate when computed from Equations (8-7):

$$R_{pt} = 0.5 d_h t_r F_{nt}$$
(8-3)

and $\phi = 0.65$

where

- $d_h$ = Nominal diameter of the washer,
- $t_r$ = thickness of the thinnest FRP component member,
- $F_{pt}$ = Characteristic value of the through-the-thickness tensile strength in the laminate (Section 8.2.3), and
- $F_t$ = Characteristic value of shear stress in the taper.

**8.2.2.4 Angle of Bearing Strength, $R_b$** The pin-bearing strength of the bearing area(s) shall be less than strength according to Table 8-2:

where

$$R_b = 0.8 d_h F_b \cdot F_b$$
(8-5)

where $\phi = 0.5$,

- $d_h$ = Thickness of the FRP component and/or member,
- $t_r$ = Thickness of the FRP component except according to Section 8.2.3),
- $F_b$ = Characteristic value of the bearing strength in the taper strength, adjusted in accordance with Section 2.4.

$F$= Pin-bearing strength defined in Section 8.2.2.1,

$F$= Effective FP= nominal area when $F$ is the effective

$t$ = FP= Pin-bearing when P= nominal end $F_{pt}$ when $d_h$ is where

$F$ = Nominal bearing strength in the ultimate strength, adjusted by the requirements of Section 2.4, when parallel to the fiber or perpendicular in the bearing to the fiber direction (Section 8.2.3.2), and

$\theta$ = Angle of bearing, the intersection between the direction of bearing, load on the connected member to the fiber direction of FRP, and

$C_p$ = Characteristic value of the bearing strength to the taper direction, adjusted in accordance with Section 2.4.

**8.2.2.5 Net Tension Strength, $R_{ts}$** When the connection force is not in the plane of the connected member, or out-of-plane bending loads are applied to the connected member plane, the connection force component shall be given by Equation (8-7) with plate distance ($e_t$ and $p$) degrees of connection component in the direction of load which shall be computed from the following nominal strengths:

The effective width for a connection, with two side edge distances $e_t$ and $F_{ts}$ are $p$, $F_b$, $e_t$, $p$, $d_h$ defined as

$$R_{ts} = 0.8 d_h F_c$$
(8-7)

When $R_{ts}$ = $0.8 F_{nt}$ ($F_b$ for the FRP shall be less than $F_{nt}$ edge) ($F$) such that $d_h$ ($F_{nv}$ edge $e_t$ $F_{pt}$ of pitch and $e_t$ = $d_h$ when $e_t$ = in the perpendicular edge distance = $e$ ($F$

When that $R_{ts}$ $F_{nv}$ $d_h$ = $e_t$ it is for the parallel to the fiber edge distance ($ \cdot $

where $R_{ts}$ = $1.25 (F_{b}$ $e_t$ or less than edge ($e_t$ $$e_t$$ perpendicular edge distance at a bearing distance

$1 + 2e_t + 1.5p$
(8-8)

**8.2.2.6 Block Shear Strength, $R_{bs}$** The block shear strength of a member shall include perpendicular to tension when the connected member(s) are loaded in bearing from each edge or direction and parallel $e_t$ shall be computed from Equations (8-7).

The design strength of a bolt subjected to combined bearing block shear strength at the connected member is taken as

$$R_{bs} = F_{nt}A_{nt} + 0.6 R_b \cdot F_{nt} + F_{nv}$$
(8-9)

and $\phi = 0.5$ where $e_t$ is edge distance $F_{nv}$ parallel to the fiber

where

$F_{b}$ = Maximum thickness of the connected members,
$F_{nt}$ = tensile shear resistance, called on the basis in the longitudinal direction of the FRP, and
$F_{nv}$ = = Maximum shear strength of a bolt distance $d_h$ = the parallel bearing $R_{b}$ = determined

For the gross area of FRP component is present or less and bearing length of connection is normal to be less in component $e_t$ or $F_t$ $e_t$ determined by the following equation. When shall be given

$$R_{ts} = 0.8 F_{bs}F_{t}(e_s - 0.5d_h) + 2 F_{nv}$$
(8-9a)

where

- $e_s$ = 0.5, where ($e_s$ - $p_s$ as determined by the length member of FRP bearing and member parallel to the mode of failure, and
- $F_t$ = Characteristic value of tension or shear strength $t_r$ for the bearing-end (Section 8.2.3.1).

When the connection face is compression or perpendicular to the member is located when perpendicular distance when the bearing distance = ($ = $).

The factored nominal strength of the connection shall be:

The effective width for a connection, with row side edge distances $e_t$ and $p_s$, for a connection having two side edges $e_t$ with edge distance $\geq 2d_{nom}$

with edge distance = $2d_h$.

When ($ $R_{ts}$ = the perpendicular component $\geq $ or $e_t$ + $2e_s$ or more connections is located and $ where $e_t$ is the clear end distance = bearing strength, connection and less than 90 degrees of the connection force to the direction of any off-center bearing force that provides such more as straight per Equations (8-7a) shall be as determined as

$$R_{bs} = 0.8 t_c \left[e_c - n_s d_h\right]F_{nv}$$
(8-7a)

and $\phi = 0.45$

where

- $e_c$ = Clear edge of the connected component and the
- $n_s$ = maximum number of bolts parallel along the edge, and
- $F_{nv}$ shear strength, calculated in Section 8.2.2.1, and
- $F_b$ = Bearing strength, calculated in Section 8.2.2.1.

When $F_{nt}$ is larger and $e_t$ = $1.25 + 1.5 p$ = $e$ > 2 or $p_s$ = $p_s$ or $F_{ts}$ connection strength parallel at the net.

The effective width for a connection, with row side edge distance of $\geq 2d_h$ for pultruded fiber material:

$e_s = e_t$ = $p$ with row size edge perpendicular:

at $e_t$ = $2d_{nom}$ for a connection, with row side edge where $e_c$ is the side edge

with side distance = $2d_{nom}$.

For an edge or connection having one or two connections, with perpendicular bolt rows, with pitch spacing $p$ and side distance 90 degrees of the connection force component to the direction of any off-center force then by the connected mode of bolt rows. The $e_c$ member for pitch of bolts ($e_t$ connected to a single row of bolts (maximum 6 rows [eight]), the connection shall become strength shall be given by Equation (8-7a).

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 34

<!-- Page 50 -->

- $C_g = C_p = p_s = 2e_{max}$ for a connection, with row side edge,
- $p_s$ = $2d_{nom}$ for a connection,
- $e_s$ or $e_t$ having row side edges having two row side edge,
- $e_c$ or $e_t = d_{nom}$ or effective width-to in

effective width for a $\geq $ or $F_b$ having a bearing connection pitch spacing

$$R_{bs} = 0.8d_c$$
(8-7c)

When $R_{bs}$ = $(c_g = R_{bs})$ is the thickness of a pultruded shape bolt row, $R_c$, or $d_c$ and $p_s$ or = $e_s$ or $F_{nt}$, that of the connected plate or at the end distance row

When $R_{bs}$ = ($e_c$ + $d_c$) the row spacing factor $C_g$ = $2e_s$ for a connection, with no center-to-distance having row side edge, spacing $p$ $e$ > $2d_{nom}$ clearance

When $R_c$ is 0.5 to 0.7 or the perpendicular pitch $p_s$ or $e_s$ from the direction of load or $e_c$ the length of $d_c$ or spacing from side

$\phi$ = 0.5 where ($e_c$ + $d_c$) having the clear edge distance of a pultruded shape member or edge distance row

$F_{nv}$ = $C_g$ for $R_c$ = the number of perpendicular fastener rows to the direction of failure, and

$C$ = the number distance or row to $F$ parallel or that to the mode of failure.

When the connection force is compression or perpendicular to the member, the connection force component shall be less than or equal to the member force, then the connection failure shall be failure or the row when the connection failure and tension failure of the fastener from force for mode.

The factored nominal strength of the connection, $\phi R_n$, shall be computed from calculations of the following nominal strengths: $R_{pt}$ from Equation (8-2); $R_{ts}$ from Equation (8-4); $R_b$ from Equation (8-5); $R_{bs}$ from Equation (8-7a); and $R_c$ from Equation (8-7c). The critical stress for the failure, $F_b$, shall also from Equation (8-13) shall be determined as:

$$R_c = 0.8 d_c F_t$$
(8-9)

and $\phi = 0.5$

where

- $d_c$ = in the nominal of the diameter where perpendicular ($d_c$ is the bearing mode distance from ($e_t$ =

$$R_{bs} = 0.8 F_{nt} (\text{$F$ for a $p_s$} - $n_s d_h$) + \frac{F_t p_s}{2}$$
(8-9a)

where

$\phi$ = 0.5, where $p_s$ is the actual perpendicular pitch spacing provided (do not use $p_{max}$). This ensures that only connection over bolt rows and columns when the connection force that a signed with the axis of bearing at Section, failure shall be the bearing stress for the mode of connection ($R_c$ for $e_c$ $\cdot$ $F$ or $p$ for $F$ shall also $R_{bs}$ bearing pitch, or $e_c$ $= d_c$ = $p_s$ for $n_s$ in which

$$R_{bs} = 0.8d_c$$
(8-7c)

with $\phi$ = 0.5 $e_c$ = $e_c$ – 1.5 $p$, $(d_h + t_f)$ + $e_{c}$ – $p$ = $p_s$ for $F_{nv}$ – $p_s$ > $p_{max}$ ($t_c$ + $p_s$) = $F_t$ for $F_b$ $e$ + $p$ = $d_c$ = $F$ + ($F_{nt}$ or $e_c$), $\cdot$ $$e_c$$ – $t$ = $e_t$ $\cdot$ F_n + ($e_c$ $\cdot$) = $R_{bs}$ $e_c$ = $F_{nt}$ $e$ or $p$ bearing connected

and $C_g$ = 0.80 for pultruded shape or $F_{nv}$ and/or edge when parallel distance of pultruded shape

For = 0.80 for the pitch or at any side of the connector in ($e_t$ or both connection strength by the requirements of the bolt diameter or $\cdot$ which is the difference spacing

$$R_{bs} = 0.8 F_{nt} F_c \cdot 1.5 (e_c - n_s d_h) F_{nt}$$
(8-7c)

with $\phi$ = 0.5 and the equation shall $F$ or $2e_{max}$ $e$ (or in which $e$ is the difference having

When $e_t$ the center of $p$ or the ultimate shear $d_h$ shall be determined as:

$$e_s = 1.25 e + 1.5 p$$
(8-23)

$$w = \frac{\sqrt{E_c G_{LT}}}{\Delta t_c}$$
(8-24)

in which $e$ is the difference spacing

$$e = 1.25 (e + 0.5 p) + 1.5 (e + 1.5 \times)$$
(8-24)

When the connection force is perpendicular to both hole edge spacings, the connection failure shall be given by the failure of net sections over multiple connection failure shall be member failure and member force. Failure from concentrated force.

The effective width for $e$ a connection. With both side edges having a $e$ is the member a $\geq$ ($d_c$ $\cdot$ having connection $e$ shall be determined as:

$$R_{bs} = (1 - w) (e_c - n_s d_h) F_{nt}$$
(8-7a)

and $\phi$ = 0.5

where $e_c$ is the clear edge at the direction failure $\cdot$ $F_{nt}$ = the $e$ or $e_{c}$ perpendicular direction or failure, row

For = bolt having in a bolt group $e$ or row (8-7a), and $G_{LT}$ is the spacing

The effective width for a $e$ of connection on a ($e_t$ parallel distance $e$

$$R_{bs} = 0.8 F_t (2e_g e \cdot t_c)$$
(8-7a)

where

- $C_g$ = spacing pitch at member or center and $R_{bs}$ is the failure and $e_c$ is the diameter in the mode of failure

For = $F_{nv}$ at bolt side of a connection where nominal failure $t_c$. When the mode or any side of the connection, with two hole or perpendicular distance row

For a pitch section of $e$ a bolt side $F$ or $e_c$ having $R_{bs}$ = bolt and $F_b$ shall be perpendicular

When the connection force is uniform force a $\geq$ or $e_c$ at a pitch of the connection having $($ row $e_c$ at $e$ or $F_t$ side spacing, any side $e$ in $e$ or row at the distance that the shall be $e$ or bolts at any perpendicular mode having row on

When a connection force $e$ connection shear force is $e_t$ or rows perpendicular or the mode at row

where $\cdot$ in is the effective width less than or a side

When the connection force is uniform and $2e$ the difference in $e_t$ or $n_s$ at distance of in the row of ($F_{nv}$ or on), side having failure

For side row or pitch at a single $e$ on or in at at parallel pitch, or side pitch spacing

where distance $\geq 2d_{nom}$

When the connection force is perpendicular a bolt $e$ or $d_h$ degrees of ($e$ having in or, at a $\cdot$ pitch spacing ( side is the distance $\cdot$ a the mode $e_c$ $\cdot$ ) parallel spacing at a row

for the parallel failure side-spacing in single of bolts row at (maximum $e$ or), the connection force component to two member or shall pitch side at

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures* 35


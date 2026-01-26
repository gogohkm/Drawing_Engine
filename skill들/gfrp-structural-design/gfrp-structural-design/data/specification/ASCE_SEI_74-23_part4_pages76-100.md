<!-- Page 76 (Page 1 of extraction) -->

**C2.3 Proprietary FRP Building Products**

When analysis regarding safety or serviceability proof of compliance may be determined both by calculation and by full-scale tests, manufacturers' test documentation can be credited. ASTM E1512 and CSA S806-16 both cite American Specification for the Design of Cold-Formed Steel Structural Members (AISI S100) and North American Specification for the Design of Cold-Formed Steel Structural Members (CSA S136) as key documents for design by test regarding the basis points of reliability and performance as achieved by full- and large-scale tests. Appendix E. of CSA S136 provides approaches regarding minimum reliability using probabilistic evaluation and consideration of statistical uncertainty, variability in the test data measured by the COV, and the "number of tests." The number of tests affects the confidence in the measured statistical properties because small sample sizes create more uncertainty regarding the uniformity of the manufacturing. In the case of FRP members, manufacturers must be able to statistically validate a reliability policy is approximately equal to standardized material values. If these conditions are met, they may be cited in member design (e.g., specification of effective areas). More uncertainty about the product affects the reduction factor $\phi_t$ in C2.3 for a pultruded connection, $\phi_t$ in B.3.3 for a laboratory test. When this approach is encouraged, the proof by testing becomes less conservative as the sample size increases, providing more knowledge about mean and variance—that is, the distribution—of product material parameters, as it relates to an idealized and probabilistically established basis for the product (ASTM A1412).

**C2.4 NOMINAL STRENGTH AND STIFFNESS**

Variability in material mechanical properties, particularly highly stressed members, components, and systems depends on specific constituents and manufacturers. In this standard, LRFD accounts for differences between the standard condition under which the properties are determined and the worst plausible condition that affects a member or connection. A reduction factor, $\phi_t$, is used to account for these differences. The basis for selection of the load resistance factors is described in ASCE/SEI 7 and is not repeated here.

Unlike an Engineered Wood Structures (ANSI/AWC NDS) (1996), which uses specific gravity to determine design properties, there are no universal parameters for pultruded FRP members that correlate to material cross-sectional properties. FRP manufacturing consists of applying chopped or continuous oriented fibers and matrix (resins) materials, reductively: materials, sizing, and so forth. For these reasons, reference points within this standard, sometimes with information points, have been deliberately chosen for purposes such as comparative analysis.

**C2.4.2 Reference Strength and Modulus**

The reference strength and modulus values determined for design and structural analysis are based on establishing limit state behavior (e.g., yielding) and serviceability conditions that are carefully controlled and replicated in a laboratory-type manufacturing environment. The reference conditions are those that ideally represent the "best-" or mean values that can be achieved in testing. The need for minimum requirements is prescribed according to these reference points, and for a number of material and composite products placed in service for the first time.

**C2.4.3 Statistical Basis for Reference Strength and Modulus**

Obtaining reference strength and stiffness properties is fundamental to selecting load and resistance factors that are modeled probabilistically, or to the extent possible. Such models (continued on next page)

permit reference strength and stiffness values to be determined on samples of different size. The standard requires that the design ultimate strength criterion is verified by a set of test data that has a 75 percentile 95% confidence interval. This value, the 95% exclusion limit, is applied to determine the mean value and COV from all the test data, including all of the material for both the mean and variability of the strength. In an equation of the mean value and coefficient of variation, $V_m$ from $n$ tests, Eq. (C2-14a)

$$V_m = V\left(1+\frac{1}{\sqrt{n}}\right)$$
(C2-14a)

where $V$ is the COV from all of the test data and $n$ is the number of tests.

$$V_m = \phi F1(1+CV)$$
(C2-14b)

where $F1(\cdot)$ is the cumulative Gaussian function, evaluated at $z$. The 75th percentile is equal to 1.15σ with $z$ = 0.675. Setting $F1(z)$ = 0.95, where $z$ = 1.645:

$$V_m = (0.675)(1.29)V$$
(C2-15a)

This standard uses Equation C2-15b for the 5th percentile exclusion limit.

$$V_m = \phi F1(1 - 2.5COV)$$
(C2-15b)

This method is recommended in TG 5.1 Design for Fire Resistance of Concrete Structures, for the 5% exclusion limit. The COV from application of interest.

The effect of the coefficient of the mean value and COV from all of the test data on building reliability, which is included in ASTM E1990 (1998), is not considered for purposes used by this standard. A means is provided for using properties that are commonly obtained in a test for a characteristic property of a building product. Section 2.4.4 provides equations for the design to assess building reliability when test distribution for the product to attend to this objective. A minimum value of a random coefficient of variation shall be applied to the 75th percentile of the distribution. For typical production of composites, these values should be relatively small compared to other steel or concrete interval or on the 5th percentile of the distribution. For typical products, such values are a relatively small proportion of the total variability in the test data that measures the product's structural quality. This information may require supplementary testing.

It is recognized that a 5% regression chemical exceedance that will accommodate errors in strength with the prescribed structure. Hence, at a member level and in service conditions, the reference coefficient of variation $V_{ref}$ in Equation (2-6a) is specified. The coefficient interval or on the 5th percentile at test provides a confidence interval for prescribed FRP material. This limitation is to the design of pultruded FRP members.

The conditions of service vary from the reference conditions of Section 2.4.5 by applying specific adjustments that account for the load time.

**Alignment Factors for Test Use**

The standardized values for the reference load and resistance factors must recognize adjustments from the reference conditions. The test-to-service adjustment factors specified in Section 2.4.5 are well understood in wood engineering practice, and they are extended into composite engineering. The test method that is used to calculate adjusted member resistance needs measure compliance to properties in accordance with Section 2.4.5. Other test methods that are related to specific compliance to properties in service in both cold temperature and deterioration in strength may deviate at examined temperatures or seasons of the $R_b$ or $R_s$ adjustment factors (NME-7). The adjusted values that the test method provides will depend on the specifics of the environment and the structural component will fully resource in strength and stiffness design.

---

*STANDARD ASCE/SEI 74-23*

66

<!-- Page 77 (Page 2 of extraction) -->

stiffness when the temperature is reduced to normal. Adjustment for $R_{TG}$ and $R_{ts}$ is intended to reduce structural resistance to account for effects of service temperatures falling between normal and elevated ($T_g$) in accordance with the standard. Temperatures that remain far below normal can also reduce stiffness. For members exposed to the effects of sustained loads that approximately represent the combined effect of moisture and stress on strength, Section 2.4.5, applies factors designated $R_{ML}$ and $R_{ms}$. Depending upon stress magnitude, moisture level may trigger superelasticity testing.

**C2.4.4 Conditioning and Testing of Composite Structural Members**

For new materials, a minimum of 4 aggressive chemical environmental exposure tests per material shall be conducted for each structural member and component. The product manufacturer can request expedited chemical testing on these tests if their rationale is consistent with the structural form chosen. Performance of required strengths and stiffness is required for most commercially available treatments; the designer is expected to take into account potential influence on mechanical properties under a wide range of environmental conditions. To address the concerns of testing in these materials or products:

**Use of Statistics to Establish a Reliable Structural Design for Member Strength in Structural Serviceability**

Unlike traditional structural materials, where an excess of the measured (general strength and stiffness of materials in structural assemblies used in its service quality) can be readily monitored, glass, carbon, aramid, basalt, and pultruded FRP members, however, are not manufactured and delivered according to a classification or standard inspection system defined in this standard. For pultruded FRP members, manufacturers can provide documentation as a basis to support the recommendations of Section 2.4.3.

**C2.4.5 Notches, Holes, and Other Stress Concentrations**

Notches, holes, and other alterations in a section that result in an abrupt change of cross sections and cause a local increase in their strength and stiffness. The designer is cautioned that such features can reduce failure strengths of structural members when subjected to combinations of environmental conditions and stress. By these results, the designer should consider whether nominal values of unmodified strength should be referenced by another means or other means.

**C2.5 MATERIAL PERFORMANCE FACTORS**

**C2.5.1 General Requirements**

The analysis of stability of an element or a structure under permanent compression may be different from the analysis for strength. Ultimate limit states (ULS) stress analysis concerns with the strength. Published FRP composites structural components are produced from glass, carbon, aramid, basalt or other reinforcing fiber forms and thermoplastic or thermosetting resin matrices. Although physical and mechanical properties can be significant in frames with slender compression members that are subjected to combinations of gravity and lateral loads, it is tested only in fiber angles of ±45°. In most instances, local buckling and structural instability govern and therefore the influence of these aspects should be addressed. Both FRP compression members developed in both columns and beams, and special consideration of the capacity and behavior of their combinations should be considered when the temperature approaches the glass transition temperature (AISI S100).

In 1988, the Structural Stability Research Council (SSRC) has recognized the "tangent-load" approach, in which a structural analysis is carried out using the tangent stiffness values to account for the critical loads and ultimate strength behavior of the frame. The required strength of the frame is determined

directly through a second-order structural analysis, and the simplifications traditionally associated with the "effective length factor" method is consistent with conventional structural analysis and design. Current codes in the United States and Europe describe this as an advanced form of design. The ACI Building Code has recently incorporated this approach in its design of load path by 1600 times; in sections on reinforced frame that is totally one or more.

**C2.5.2 Resistance Factors**

The values of resistance factors assigned strength of all columns within that story. Section 2.5.3 does not prevent that alternative approaches to slenderness and non-dimensional factors for inelasticity but satisfies the same level, of reliability required. Although that section provided the comprehensive analysis, which is considered to be derived from the basis on which the effective length and stiffness modulus associated with the strength of the column is related.

Equation (2-3) through (2-9) provide the determination of individual or cross braced composite members. The second option is to perform directly nonlinear second-order analyses to determine directly the strength of the second-order stability of the structure accounting the effects of geometric and material imperfections and secondary stresses and moments in the plane of bending. This methodology permits the analysis and design that has been verified with experiments (Lopez-Anido et al. 1995, Zureick et al. 1995). This approach leads to greatly increased design efficiency (in terms of lighter members) in both frame in C2.5.3 methods of calculation (Davalos and Salim 1993; De Lorenzis (1998) used by Columbus and Saracca (2000). In the general case, several individual members will govern for each story; in special cases, multiple groups of members may govern the design of a story. The designer must judge the situations where the critical load must follow the step-by-step procedures, axial forces, $P_e = F_b = L_w / L_x$ in Equation (2-5) are considered as the actual loads of Equation (2-4) and the member strength capacity of the frame (L/r). For frames, the story shear capacity $Q_n$ is obtained by considering one story of the frame level.

The structural strength of materials of pultruded FRP members can be determined by elastic small deflection analysis in the framework of force and force. Calculations of elastic flexural buckling of axially loaded structural members may be conducted on stiffness and strength formulas for columns with axially applied hinges and components on individual member joints. This method is also used to determine the effective length factors for members that are partially affected or fully affected by sidesway buckling. Other empirical corrections which have been verified in tests related to serviceability are used in pultruded FRP composite tests under Equation (2-5) include the minimum and shows in the plane of warping axial force. The fact that a compression member in structural frame of warping affects the rigidity of the lateral bracing means that the effect of story deformation on stability. If the inter-story drift is determined by $Q_m$ as the in a nominal value for gravity, then the load combination of story deformation is also story-wise. The overall buckling load factors of a compression member in a braced structural frame deformation can be determined from the exact response of the column. ANSC method predicts effective slenderness ratios for $F_b$ without increasing effective lateral deflection.

where $\Delta P$ is the first order drift of the frames in question the second-order displacement value of story $g$ to to load H acting at the top of the story.

$$\Delta_{2st}=\Delta P(1-\frac{P}{P_E})/1-P$$
(C2-16)

where

$P = \text{Summation of all column on the story.}$

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

67

<!-- Page 78 (Page 3 of extraction) -->

and $P_E$ does not require the calculation of effective length, $KL$. Note the use of elastic stiffness value $E_I$ to determine forces $P_E$ also the forces in members that frame into the column.

Euler buckling load is used with Equation (2-3) in two cases. The first use is to check the level of gravity (and other applicable loads) of total lateral resistance in the member service, or in the case: As such this approach is not applicable in most is such deflections performed by FRP frames, this limitation is at "bent" frame.

The second application for using Equation (2-3) with a series of requirements for each story to provide service conditions: Equation (2-5) is based on a member's strength based on the calculated length between the member's stiffness values. A sufficient estimate of this factor is given by Heuer and AISC Load and Resistance Factor Design Specification for Structural Steel Buildings (AISC 1993); Galambos and Surovek (2008); Winter (1960). The provisions for bracing strength and stiffness in this standard for the design of member elements in structures subjected to braced stability conditions, slenderness factor or a compressive limit state, were derived from the "direct design method" (Timoshenko and Gere 1961; Bleich 1952; Euler forces have been reached). Furthermore, all required strengths and the moment limit state that must be a minimum of the member's effect on elements that are subjected to a local instability; for example, Equation (2-3) should be avoided if the braced frame shall provide individual or member force versus story stiffness lateral bracing, which moves momentary only at the point of intersection between the member and the lateral bracing. A higher rate instability due to the lateral bracing, will likely cause different and local shear forces in single members subject only at a point of instability. Moving must be attached there in all.

Now consider one of a frame's column about in one story. In the structure, flexure stiffness, EI, is a measure of the moment applied to get a unit relative deflection of the members should be provided at point of concentrated load.

When failure strength value is to be achieved strength for local failure or local strength value (effective cross-sectional) values strength for wall structures and shear wall diaphragms to shear forces. In one case, the local strength of flexure or shear stability, when local buckling occurs and failure is not a point of inflection. Shearing must be attached there (web stiffness test).

**Bracing of Members**

Bracing requires for a member that is set of lateral bracing or stiffened bracing, to prevent a member or any lateral connection at a location that will ensure member in lateral torsional buckling or flexural buckling.

**Bracing of Beams:**

When flexure of a beam occurs about its weak axis at lateral torsional buckling occurs a governing failure mode for pultruded FRP beams. However, bracing is needed. Bracing can be provided by lateral bracing and/or by support locations to prevent torsion about the longitudinal axis. Therefore, the strength of beam bracing can be estimated through theory, Galambos and Surovek 2008, but more typically it can be developed based on rules if member fails due to lateral failure mode. For unbraced panels, laterally braced along its span with a bracing spacing that is determined by the relative strength and stiffness point. At a point of inflection, shearing must be attached these (web stiffness test).

**Bracing of Frames:**

Requirements for frame stability at any specific lateral force with deflection or vibration, rather than instability (frequency analysis using structural analysis). Many cases of stability in frame are discussed by Galambos and Surovek (2008), Yura (1993), and Ziemian and McGuire (2002).

**C2.6 DESIGN FOR SERVICEABILITY**

Serviceability limit states include deflection of the structural elements under loads over time, both creep, long-term loading effects, and durability (Mottram 1990a, b; Mottram and Chambers 1997). Serviceability limit states are important when members are subject to long-term creep. FRP members are commonly used with any light frame construction technology, where limits to deflection are necessary. Serviceability includes long-term loads including temporary loads applied to structural systems during service, such as moving and operating loads or service on Serviceability Research 1996). Such context may be loaded only once for relatively short periods; for example, a composite bridge deck during service. Galambos and Surovek (2008), AASHTO LRFD Guide Specifications for Design of FRP Pedestrian Bridges and lateral vibrations due to pedestrian loads include limiting deflection or other structure and the prescription of the acceptable of stress. Accordingly, specifying serviceability limits that are separate from the consideration of strength design can help the engineer require an assessment of the facility by the registered design

professional, architect, and owner of all functional and economic performance regarding the design, function, building occupants, use scenarios, structural deflections and motions that are far less than elastic limit capacity. Serviceability loads, deflections and movements less than ultimate strength level loads are sometimes the predominant part of structures, consequences of serviceability problems can be estimated. The performance of short-term load and long-term load can be proportions of limiting deflection require. The designer should limit member deflections by limiting the member creep and excessive stresses or high performance structural impairments, requirements.

Permanent and explicit published are intended to provide a consistent procedure for the determination of deflection in service load and response. The designer may wish to consult other documents of ASCE 8 and its commentary.

**C2.6.1 Strength-Controlled Deflection of Beams**

The method proposed for calculating deflection of beams is to visually check materials at no gross curvature deviating, and breaking (static) or gross warpage of members, bridges, floors, beams, et al. When deflections on service level subjected loads are due and the design of members meet with the ASCE 7 standard criteria (relative limit state requirements at early visible and may lead to minor architectural damage, while the design should be limited that meets at state of their failure criteria such damage. Loads used for buildings shall continue to result when member stability shall be capable of providing lateral integrated with the structural system (ACI-PRC Committee on ACI Materials, 2006). When possible, some architectural information on the deflected members of buildings should be available from laboratory tests other. A fully-adjusted deflection for creep would be utilized to validate value that depends on the building performance for reference to appropriate strength of deflection methods; and general design procedures and structural deflection by design (Mottram 1990a; Kellet and Hart 2005; Mottram 1990a). However, one practice is to limit static lateral deflls to 1/400 times the story span height of elements subjected to field Central California highway bridge demonstrated a maximum deflection criteria below L/250 based on one measurement of test limited duration. AASHTO established L/800 as a moment of P-δ effects. Approaches such as these effectively relative to long-term effects of the environment to applied to verify current serviceability requirements. In addition serviceability is a design state that provides for guidance which include actions at a ratio for permitted rate zones that have specific designs of the structural member or members that may be designed for members that are not subject to creep. For example, conditions, that are subject to other lateral loads on connections, a limit of the deflection might keep static loading to levels below other limit deflections of material response. At this time, deflection of pultruded FRP members and composites is included in Chapter 2.1.5 of this standard, in which the live load capacity the material can be applied (Barbero (2011) with restricted from a synthesis of data collected by the designer based on the limits on any combinations of creep, whether as visually collected in permanent deformed loads. Whether structural failures are available for all members, models (1941) with conditions determined from a synthesis of data collected by the designer (Findley et al. 1989).

**C2.6.2 Time-Dependent Deformations**

Members must be structurally stable to operate without creep or structural viscous as a whole may cause occupant discomfort. The designer when not subject to long-term loads, and these stress levels should be maintained lower under thermal response. Such stress includes sustained load because in creep. However, such loads from an experience, load level applies. Such stress through structural behaviors is measured limits of exposure in creep through such moments by limiting the stress, deflection of the floor under live less, that is likely to note that the likely to be sustained to design not to the visually controlled value. Engineer consideration should be design to consider the dynamic nature of occupancy and response in dealing

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

68

<!-- Page 79 (Page 4 of extraction) -->

with this limit state, simple dynamic models often are sufficient (Hoppenzak 1988; Allen 1990).

Humans can be quite sensitive to vibrations in levels that are not sufficient to pose a safety hazard to structure systems. For structural systems that do not contribute any functional damage, structural dynamic analysis of an FRP typical floor system, it is necessary to limit the time static defection per period of time with accelerations on the order of peak (or steady state) of 0.5% of gravity. Deflection rate can be achieved by limiting floor span length for natural frequencies to 4 Hz with a natural period for acceleration of 0.25 s. The upper limit for typical floor system or braced structure frame.

**Damping:**

Dynamic response (e.g., vibrations) of FRP, which was determined is reasonably simulated by an effective damping ratio of 2% to 4%. The typical damping ratios for floor systems of a bridge or highway or typically simulated and predicted ratio of 2 to 3%.

During design work or earthquakes, the number of significant cycles can be up to 500 cycles, which is not sufficient to cause significant cyclic creep (of FRP pultruded members.

**C2.6.3 Vibration**

Section 2.6.3 requires that designers address structural serviceability problems of vibration under service loads. One of the most common properties of the reinforcement and the matrix (Schultz 1993). When resonance of frequencies in a composite, and resonance does may occur when vibration frequencies may occur or near to approach for resonance of the structural.

Design is through this formulation system.

$$\sqrt{AG^{eff}T} = C$$
(C2-18)

where

$a$ = Cycles to fatigue failure (arbitrarily defined),
$N$ = Cycles to fatigue failure for all points at which yield for all beam structures are produced, and
$C$ = Material constant amplitude fatigue tests.

Their recommendations are published from constant load strain yield stress testing published material form, which often tests above σ < 60% for all the categories. The definition of constant amplitude is defined in strain as strain is in strain and strain is 60% σ of $F_{lx}$ at all yield. In Section 2.7.2.6, where the definition of constant amplitude is defined in strain as and 85% for a total stress ratio or alternatively, the value can be chosen from using fiber and strain data. The reference to fiber stress values must be developed for reasonable performance testing is used in these recommendations and can be followed (Dutta 1996); stress/strain and strain data must be developed for testing concrete. For higher stress values, higher stress and strain stress ratios must be outside failure stress. For example, if they cycle stress ratios in 0.72 in failure stress tests is less than. stress of 0.72 is failure one or less. cycles must be in a failure in materials of stress cycles must be followed stress failures. The designer has the authority to determine or to vary less failure such as less cycle (Tsai and Hahn 1980; Mandell et al. 1981). Low cycle performance requirements is for the structure to sustain at least 10,000 cycles of stresses below 50% for the structural values of all for life structural at 1000 cycles has a stochastic analysis to be applied to be 50% of $F_{lx}$.

**C2.7 DESIGN OF CONNECTIONS**

The general approach to connecting structural members to be by the basic considerations of all reinforcement on the load requirements related connections. Chapter 8 provides specific design requirements.

Performance of connections is essential to the performance of structural systems built up from elements typically connected elements (see sections). Material properties used in and structural connections of all load categories design elements (e.g., pieces of other plates, angles) have been fabricated from materials with elastic or plastic or structure elements which affect materials in connections. It is important that any FRP connecting elements used in connection design match those specified for properties currently in the routine design of connections load design approaches are typically matched with each FRP connection forms. Sections 8.2 and 8.3 follow a simple recommendation form to the connection as a propagated. FRP requirement to simplify the materials required by connection as in proportion. For example: Material requirements such as a simple hole materials according elements and fasteners are permitted where the connection is terminated by later in fabrication rather than by materials. FRP connecting elements and fasteners are permitted in fabricating connection forms more critical is terminated by materials than by fabrication connections in connection than the FRP materials. This requires design to validate connections in the FRP connection types. Chapter 2 provides initial sizing of FRP elements.

---

*STANDARD ASCE/SEI 74-23*

69

<!-- Page 80 (Page 5 of extraction) -->

# CHAPTER C3
# DESIGN OF TENSION MEMBERS

**C3.1 SCOPE**

This chapter is intended to pultruded structural members with rectangular or circular cross sections where the principal tensile load fiber reinforcement is in the transverse direction. This chapter does not cover the use of FRP tendons or cables. Therefore, tension members are not expected to provide secondary prestressing in structural systems. The provisions in this chapter apply to member forces, do not and through hole connections. The member strength and stiffness values, based on the combined forces, such as tension and flexure in accordance with Chapter 5. The provisions in this chapter also provide reference for components that ensure fastening and may also reduce section strength on or near ends of fastened connections of members or components. The nominal strength of the pultruded members depends on the number of fiber architectures in various members. Chapter 6 provides guidance on connections design.

**C3.2 GENERAL PROVISIONS**

The available strength of the member shall not be based on a limited set of tensile tests, but shall be substantiated by several tests per material system and documented for the worst conditions; resistance factor, full-scale tension tests on various FRP series sections will tend to be conservative.

**C3.3 NOMINAL AXIAL TENSILE STRENGTH**

This chapter provides for axial tensile strength of an untapered failure, which is determined in accordance with an established standard. Unlike steel members, pultruded FRP members do not have a single stress-rupture failure limit, a nominal tensile failure strain plus other strength and stiffness material properties values are specified with sufficient precision for use in the design. The specified nominal tensile strengths are obtained from tests with simple gross cross-sectional area and stress concentration factors to account for possible section strength reduction.

With finite analysis failure has been observed at less than maximum under tension. Typically, tensile distances defined by the diameter of a hole near the end of member will typically show failure initiated from the hole edges in the material instead of uniform failure along the element, which would lead to shear-reduced failure in the

continued fibered load, resulting in previous failure. Therefore, to ensure that adequate strength is initiated along the path consistent design equations, the Chapter 3 equations are designed to prevent initiation of the onset of significant FRP structural failure. In addition, interference shear failure within a flange or a web edge is a failure mode that makes the appropriate design option such development only if the material in tension have sufficient tension capacity outside failure initiation region between the hole width cross-section and the perimeter of the hole in the width orientation between lateral or cross-sectional tension would likely result in failure. A reduction of significant strength that occurs from the holes at connection of 0.6 factor is used to recognize that there may be occurrence of local failure.

Based on the previous description, two separate limit states are required to prevent general net section failure at connections. The first limit state is cross section failure with the gross area, Second, a net section failure at the location of holes or notches of a typical edge holes. Consider gross holes in a tension member. If the gross area is used and end of reinforcement to distribute failure strength around the net-section thickness it is expected, and cross holes in a simple member. With end restraint through a simple member. Typical lateral or an end of a member at a point may need of strain and strain of strain stresses using either static failure gross cross-section basis. Limiting or strain based on a ratio of a typical member failure is similar for other materials such as wood and such cases and (2) load restraint along the longitudinal and the axial section fiber orientation. Strain orientation such that uniform design requires connecting the design using different types of performance in connections, and the structural component will fully resource in strength and stiffness.

**C3.4 ADJUSTMENT TO REFERENCE STRENGTH**

The reference strength, as defined by Section 2.4, is defined in Section 2.4, the designer is to use the allowable design strength and strength value. For pultruded FRP frames, Chapter 2 provides specific areas or end one conditions that differ from the standard conditions. This section suggests a reduction factor for building applications. Consequently, equations for structural application materials applied to pultruded FRP element forms, but the process used for ultimate material strength values would probably be used to be load resistances for strength in the region as measured in both ultimate and serviceability locations on the transverse areas or considered in the development of ultimate limit stated applied to also prescribe for adjusting the axial stresses and strength limits which have been published by authors of such papers. These guidelines have been based on engineering mechanics principles. Compressive strength of members with shapes

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

65

<!-- Page 81 (Page 6 of extraction) -->

(5) temperature variations from room temperature, and others. Typically, fiber reinforcement patterns in composites leading to a high degree of orthotrophy need more test data to account for matrix failure modes that cannot occur in quasi-isotropic composite sites. For example, quadriaxial glass fiber polymer composite plates tested under stress reduction on the order of 2.5 (Russo and Zuccarello 2007). Hence, the proposed stress reduction factor is limited to trying temperature and moisture filament construction only, and higher reduction factors may apply if the material is quasi-isotropic, due to asymmetrical relationship for complex fabric reinforced composites is recommended after generating additional experimental data.

**C3.4 SLENDERNESS LIMITATION**

The slenderness limitation for a tension member is intended to minimize damage during transportation and erection and is based on practical considerations.

The slenderness limitation is not essential for the stability of a tension member and therefore more liberal criteria are suggested for tension members, including those subject to small compressive forces from transient loads, such as earthquake and wind. The slenderness limitations recommended herein are based on small compressive forces that correspond to $F_{tu}$ to 1% to 2% of typical coupon compressive strength in the longitudinal direction of the member, where $F_{tu}$ is the elastic buckling stress from transient loads. The proposed slenderness limitation, that is, $L/r \leq 250$, results in a member size equivalent to the sizes being adopted in the current design practices of FRP structural members. Designers are encouraged to conduct additional evaluations if greater accuracies or higher $L/r$ ratios are desired.

**C3.5 BUILT-UP MEMBERS**

Section 2.3.2 and related commentary governs the prequalification of built-up FRP members.

---

**STANDARD ASCE/SEI 74-23**

66

<!-- Page 82 (Page 7 of extraction) -->

# CHAPTER C4
# DESIGN OF COMPRESSION MEMBERS

**C4.1 SCOPE**

In general, pultruded compression members are econom

ically successful for structures that have relatively short elements where stability may not be a major issue. For members in which such members will be designed according to the provisions established in Chapter 4, ultimate design axial strength may be reduced to account for flexural buckling. Local buckling of elements comprising the cross section are prone to local buckling. The D/t ratios for channel sections of flanged web-flange interface junction shall be considered through appropriate effective width provisions. Local buckling limit states (without allowable stress check) are also required since different local buckling mechanisms may be experienced. Furthermore, pultruded members without stiffened walls may also experience local buckling limit states (without allowable stress check) are also required since different local buckling mechanisms may be experienced. Compared to normal concrete and steel designs in-plane buckling and instability under repeated cyclic loads can be significant to web-flange distortion and height deflection of a person quality loaded compression member. Long slender members may buckle far below their fully calculated cross-sectional strength. Experience demonstrates that designers shall consider member slenderness, and the cross-section properties. In general, the composite also not alone during the life of the member. As many early designs include fiber orientation, shear forces, and combined load effects, most strength and serviceability related properties may vary. The cross section and cross-section related elements allowed a factor of safety.

**C4.2 DESIGN CONSIDERATIONS**

**C4.2.1 Slenderness and Effective Length**

When defining the slender limits, it also called second order analysis include elastic stiffness properties from the center-to-center distance between lateral supports. The member length may be different in each direction that buckling may

occur. The effective column length is $KL$, where $K$ is a dimensionless effective length factor and $L$ is the unbraced length of the column. In general, the $K$ factor depends on both the relative stiffness of the columns and beams framing at a joint. For $K$ and $L$ which are associated with flexural buckling, generally the member may be designed using flexural buckling. Members with specific cross-sections properties must be $K$ and $L$ from list in Chapter 4 are necessary. For slender compression members, the slenderness factor is also used. The use of $K$ or $1$ is immaterial to be determined by a rational analysis that accounts for the end support conditions and relative stiffness.

**Effective Slenderness Ratio**

The effective slenderness ratio, $KL$ which is used when calculating the required resistance $\phi_c$ subjected to axial loads is greater than 200. This maximum slenderness ratio was considered to account for possible accidental loads that may be applied to the $\phi_c \leq KL/r$ if $P_o$ must be used $\phi_c F_g \leq KL/r$ if $P_o$ must be carefully analyzed at $P_o \leq 0.5$, to be a ratio that: short-term lateral deflections at a compression member must be for dead load and live loads.

**C4.4 FACTORED CRITICAL STRESS IN COMPRESSION OF SOLID SECTIONS**

For axially compressed pultruded FRP columns, data from twenty-one pultruded compression-reinforced shapes have been have been determined. There are 65 I-shapes, there are 32 sections, there are tube sections. Based on 23 test with sections. The test are obtained data. These experiments located cross-sections, such of these wall sections of FRP in, 13 total were a constant factor of $P_u$, nominal capacity which will always have a correct target safety. The equations are for two categories of sections for buildings applications. Consequently, equations for factored resistance factors can be a case when developed from properties for building applications. The case the observed applications of resistance factors considered from a case the allowable stress are considered in the development of ultimate limit stated applied to also prescribe for adjusting the axial ultimate and strength limits which have been published by authors of such papers. These guidelines have been based on engineering mechanics principles. Compressive strength of members with shapes

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

67

<!-- Page 83 (Page 8 of extraction) -->

that those previously discussed should be determined by rational analysis.

Strength limit states for the design of a geometrically symmetric member are addressed through equations defining slenderness ratios, effective lengths, and methods of calculating the strength, modulus of elasticity, and dimension of a member. The instability limit states, in turn, involve overall buckling of the member due to initial imperfections in geometry. Also affecting the member strength is local buckling which can occur in combination with overall member buckling. Interaction of these buckling modes can cause failure at lower slenderness ratios than would be expected from either mode alone. If a pultruded FRP member is addressed through equations defining slenderness, effective lengths, or various, both the Euler load throughout the cross section and the maximum stress in the web, and local buckling at compression flange $F_{cr,f}$, the stress limit, analytical buckling, and analytical solutions that account for the post local buckling behavior of members are not appropriate for design of axial-loaded members with slender ratios.

**C4.3.1 Critical Load Buckling**

**Using LRFD Load Buckling**

When certain limit states for the design of geometrically symmetrical columns need effective stress with stiffnesses for $\beta$. These provisions also may be applied to unsymmetrical buckling when limit state buckling occurs. Cases such a critical buckling are to provide critical buckling location at an element with elastically restrained edges. At present ratio, for which different types of boundary conditions are considered such as simple support and clamped condition in accordance with the rational buckling and critical load uses. The following selected buckling load length (the, for the sectional buckling load

$$F_{cr,f} = \frac{\pi^2}{12(1-v^2_{LT})} \left(\frac{t}{b}\right)^2 \frac{E_L E_T}{12}$$
(C4-1)

In Equation (4-1), the quantity $(1-v^2_{LT})$, which was eliminated into the original buckling equation, now returns with reference to the preferred buckling modes when $(1-v^2_{LT})$ is returned as the test does not refer to the different buckling modes which $(1-v^2_{LT})$ buckling test of boundary conditions for this test. The axially compressed T-shaped sections are based on tests conditions which are L/2 tested and Lee (2004) on axially braced shapes having a local buckling by rational buckling for the T-shaped. The most studied for the local sections when $b$ test were $p$ with standard flange and for overall buckling load in less than 10% of the sectional buckling load. Data for the following sectional buckling load formula is collected.

**C4.3.2 Multi-Section with Equal Free**

Zamrick and Steffen (2003), on section 4-4, provide data regarding the total axially tested FRP columns for a section which have a buckling in two locations. Geometry-specific experiments to local buckling, and are buckling of local buckling allows an account of for the equations over are to stiffness factors allowing for the local buckling and critical buckling equations (Thoroddsen and Gere 1961).

---

**Figure C4-1. Experimental versus predicted strength values of axially compressed pultruded I-shaped sections under axial loading**

[THIS IS FIGURE: A scatter plot showing experimental versus predicted strength values. The x-axis represents "Test Number" (ranging from 0 to 50), and the y-axis shows what appears to be strength ratios (ranging from approximately 0.3 to 1.0). The plot contains multiple data points marked with different symbols representing "Local(1990 Load Buckling", "Column Load Buckling", and "Mattletion et al. (1998) Good buckling". Data points are scattered across the graph showing various correlations between experimental and predicted values.]

---

*STANDARD ASCE/SEI 74-23*

68

<!-- Page 84 (Page 9 of extraction) -->

[THIS IS FIGURE: Two graphs showing experimental versus predicted strength values]

**Figure C4-2. Experimental versus computed strength values of axially compressed single angle members.**

$$F_{cr,c} = \left(\frac{E_LG_{LT}}{12(1-v^2_{LT})v^2_{TL})}\right)^{1/2} \left(\frac{t}{b}\right)$$
(C4-2)

where

$F_{cr,c} = \frac{E_L G_{LT}}{12(1 + v^2_{LT}v^2_{TL})}$
$v/\theta = \frac{3E_L}{12(1 + v^2_{LT})} \leq 1$

Zureick and Steffen (2000) note that Equation (4-2), results in an overestimate of critical strength between results for axially braced members and axially loaded members. This comes from tests done simply supported along the uniformly loaded edges. Assuming that proper lateral restraints for the members under consideration prevent global (long) wavelength response of the other edge conditions such as long beams, Equation (C4-2) was expected to be less accurate simultaneously and neither of the legs is able to carry any critical load. For the T-shaped members where a single local buckling test of members is presented. The limit state assumes no lateral support to prevent global local buckling failure to the local member element. Based on the local level, where slenderness criteria for flange prevents from local buckling, the critical strength local similar tables, the use of Equation (C4-2) is sufficient. In practice, a reduction factor is used by the flange support to the section. Data for the critical support to the section should be the factor of similar test to provide the final Equation (C4-2) same the factor, which would help critical buckling, and critical compression tests should be considered similar form buckling. Finally, Section F of to Eqn. which competes with the Equation (C4-3) is negligible compared to the use the

(continuing similar analysis...)

**Figure 774.** Normalized versus predicted strength values of axially compressed I-shaped sections with equal legs.

where

$$F_{cr,c} = \left(\frac{F_L F_T}{[\frac{1}{k} + v^2_{LT}/v^2]}\right)$$
(C4-4)

$$F_{cr,c} = \left(\frac{E_LG_{LT}}{k}\right)^{1/2}\left(\frac{t}{b}\right)$$
(C4-3)

**Figure C4-4. Experimental versus predicted strength values of axially compressed tube sections.**

**C4.4.3 Circular Tube Sections**

Dion and Rosen (1996) design an expression for estimating the existing local buckling

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

69

<!-- Page 85 (Page 10 of extraction) -->

## C4.5 COMPRESSION STRENGTH FOR MEMBERS WITH OTHER CROSS SECTIONS

The design of axially compressed pultruded members having cross sections not covered in Section 4.4 should be based on a combination of analytical solutions or computational analysis coupled with physical full-scale tests of the component under consideration.

## C4.6 COMPRESSION STRENGTH FOR BUILT-UP MEMBERS

At present, no experimental data are available to support the development of design equations related to built-up sections. Compression strength of built-up members should be determined by rational analysis (see, e.g., Timoshenko and Gere 1961) or through testing structural prototypes.

---

**STANDARD ASCE/SEI 74-23**

70

<!-- Page 86 (Page 11 of extraction) -->

# CHAPTER C5
# DESIGN OF MEMBERS FOR FLEXURE AND SHEAR

**C5.1 SCOPE**

The provisions of this chapter apply to pultruded members where the loading is applied to the member in such a way that flexure and/or transverse shear must be resisted by the element. The pultruded composites used in structural framing typically have fiber reinforcement oriented in the lengthwise direction through bending in failure.

**C5.2 DESIGN OF MEMBERS FOR FLEXURE**

**C5.2.1 Rectangular and Round Members**

**Material Rupture**

When an asymmetry of flange and web thickness exists or relatively thin flanges are used, the maximum theoretical flexural stress may occur in the flange. Equation (5-2) is used for symmetrical and unsymmetrical cross-sectional structural shapes in linear. Note that although the material may not exhibit constant stress during bending, the moment corresponding to failure is assumed to be reached when the maximum cross-sectional stress equals the ultimate transverse tensile or compressive strength recorded for the flange and web material respectively.

**Local Buckling**

Local buckling occurs when individual elements of an I-beam cross-section buckle under load. In an I-beam, local buckling may occur in the web or the flange and is influenced by the section proportions and boundary conditions. The AISC Steel Construction Manual (AISC 2005), Lopez-Anido et al. (1996), Zureick and Shin (1997), Qiao et al. (2001), Muttram (2002), Keller (2002), etc., all provide methodologies to determine local buckling stress in FRP and GRP members. Generally, the member must first be determined either through analytical study or testing. The critical buckling stress of an element with elastically restrained edges can be assumed to be locally supported, as in case of flanges with boundary conditions. Barbero and Raftoyiannis (1993) and the Clarke (1996) recommend this assumption where elastically restrained edges are assumed to be locally supported, as expected. Different types of boundary condition in the standard are provided below to calculate the term (2-$\sigma$/$\sigma$cr), that typically appears in plate

buckling equations have been set to 1.0 and therefore does not appear anywhere in the section. Tests and analytical studies showed that local buckling stress values for any combination of plate material boundary conditions are influenced by shape, flange width-to-thickness ratio should identify the stress to be weak axis, the loading will not be applied to the strength of the member about its strong axis. Bending about the weak axis will generally have less buckling resistance for the lateral structural buckling of pultruded I-beams. Seible et al. (1995) done first that there are methods that the failure could be a major buckling or a longitudinal bending. The effects of the span-to-depth ratio of the section by AISC (1993) methods of prediction (Equations (5-2) and (5-3)) which are based on simple material values related to the lateral structural buckling of pultruded beam where beam type such buckling analysis of members made of isotropic material was identified. For this reason design are, the design of the effects of bending capacity determined using methods such as Roberta (2003, shown, and in others (Barbero, et al., (2000), where a value of the shear buckling coefficient, $k = 5.35$ for pultruded composite material. Hence, the approach taken in this standard is to limit the stresses at the critical section of the cross-section loading conditions.

The value of the resistance factor, $\phi = 0.5$, in Equation (5-1), which is consistent with the pultruded application. It is in the opinion. The designer can set both $\phi = 1.0$, if a more conservative estimate of the flexural strength based on the lateral structural buckling limit state. The type of this standard is indicated for use at the second limit state for the design with conservative testing of the member at a uniform or discrete load and rotation of the loaded member.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

71

<!-- Page 87 (Page 12 of extraction) -->

# Table C5-1. Values of $C_b$ for Simply Supported Members.

| Load | Lateral Bracing Along Span | $C_b$ |
|------|----------------------------|-------|
| ![Single point load diagram] | None | $\frac{1}{1.0}$ |
| ![Single point load diagram] | At load points | $\frac{1}{1.0} + \frac{1}{1.0}$ |
| ![Two point loads diagram] | None | $\frac{1}{1.14}$ |
| ![Two point loads diagram] | At load points | $\frac{1}{1.0} + \frac{1}{1.67} + \frac{1}{1.67}$ |
| ![Three point loads diagram] | None | $\frac{1}{1.14}$ |
| ![Three point loads diagram] | At load points | $\frac{1}{1.0} + \frac{1}{1.67} + \frac{1}{1.67}$ |
| ![Uniformly distributed load] | None | $[\text{uniform load formula}]$ |
| ![Uniformly distributed load] | At centerline | $\frac{1}{1.30} + \frac{1}{1.30}$ |

Source: AISC (2017).

## C5.3 DESIGN OF MEMBERS FOR SHEAR

**C5.3.3 Strength of Members Due to Web Shear Buckling**

Pultruded member web panels may buckle under the action of shear forces. Equation (5-4) for determining the critical shear stress is based on work by Seydel (1933a, b). The shear buckling coefficient, $k$, also shown in Figure C5-1, was obtained from

[THIS IS FIGURE: A graph titled "Figure C5-1. Value of coefficient k as a function of parameters α and β." The graph shows multiple curves plotting k values (y-axis, ranging from 0.00 to 9.00) against α (x-axis, ranging from 0 to 1). Multiple curves are labeled with β values ranging from β = 0.0 to β = 1.0]

---

**STANDARD ASCE/SEI 74-23**

72

<!-- Page 88 (Page 13 of extraction) -->

**C5.4.1 Design of Web Stiffener**

To prevent web buckling under normal stiffeners may be provided along the length of the beam where the shear force is high enough to cause critical stresses in the web. Stiffeners at locations close to supports, as well as intermediate stiffeners, are common means of preventing elastic buckling failure in the web. To be conservative, Section 5.3.4 requires that stiffeners be capable of carrying at least 2% to 3% of the total flange force, thereby providing a means of preventing critical load web stiffness.

**C5.4 DESIGN OF MEMBERS FOR CONCENTRATED TRANSVERSE LOADING**

Based on Equation (5-6), the factored resistance has been derived by applying an adjustment to the effective width of the bearing force applied to the plane of the web and concentrated transverse loads on the web can be determined. The theory applies to member bearing at full depth of the web. Buckling will occur when concentrated loads exceed what can be carried by the bearing area under the concentrated compressive loads whereby the depth of the web should be reduced to $N_s = 8.0$ maximum per Section 5.3.2.

**C5.4.2 Strength of Members Subjected to the Web Crip pling (Concentrated Load at the Interior of Web):**

The factored strength of members subjected to concentrated transverse forces at the interior or end is based on research by Strongwell (1996), and Barbero et al. (1997). The research indicates that the following equation (5-9) provides a good estimate of the ultimate load-carrying capacity. At the point of the shear failure is a function of the bearing strength and thickness of a bearing plate and the depth of the clear distance of the web as a result of transverse loads. For the case of

[THIS IS FIGURE: Two diagrams showing "Figure C5-2. Effective web compression zone at load" with hatched areas indicating compression zones and dimensions labeled $N$ and $C_w$]

a concentrated load near the end that near-end transverse bearing plate loads were required for beams with depths greater than 125 mm (Strongwell (1996), Barbero et al. (1997). The nominal ultimate bearing at the minimum flexural rigidity specified in Equation (3-9). This provision has been observed in literature based flexural rules data in the absence of a crippling rule has a minimum flexural capacity specified in Equation (3-9).

**C5.4.3 Lateral Nominal Strength of Members Due to Local Transverse Bending at Interior Load**

At a location in a span where a transverse force is applied to the flange, the flexural strength of the web connected to load is smaller than the critical web forces through the member at some stage. The section of the web must be adequate for the stress distribution arising from transverse forces from the load through the depth of the cross section. Buckling failures must be avoided based on a lateral transverse buckling analysis of members made of isotropic material. Equation (5-9) was developed to be effective estimate of the ultimate lateral transverse bending strength, to verify the effects of the available flexure (Roberts (2003), shown in et al. (2000)), where a value of the critical moment $M = 5.35$

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

73

<!-- Page 89 (Page 14 of extraction) -->

This page intentionally left blank

---

74

<!-- Page 90 (Page 15 of extraction) -->

# CHAPTER C6
# DESIGN OF MEMBERS SUBJECTED TO COMBINED FORCES AND TORSION

**C6.1 SCOPE**

The provisions of this chapter cover the design of doubly symmetric members loaded in combined axial compression or tension with bending, and singly symmetric or unsymmetric members where all loads occur about either the minor or major principal axes. Closed and open sections with unsymmetric loading also receive mention in this chapter. The need and distribution of member torsion loading plus axial load is usually back calculated expected to yield based on the design of the member but also to be designed for torsion and axial loads, Tension members as they appear in use are also often subject to bending due to the loads applied at point or points. For the beam-columns with small initial curvature, or use similar approximations. Members subjected to torsion, flexure, and/or axial loads often require special considerations to meet design requirements. Torsional instability of members is addressed in Section 6.4 with detailed interaction equations subjected to bending and torsion; equations are contained in Section 6.4. Designers subjected to axial loads. Pultruded FRP member strengths such as unsymmetric ones that are both directly based on the interaction behavior of columns before designing FRP composite members under combined load application. The standard builds on such application by the equations presented in this chapter for such members design as Chapter 8, and sections detail procedures for connection flexure. See Section 6.2 for equations governing the axial bending of beam-columns. Members subject to flexural or stability; compression by torsional members and axial equations may be simplified to conduct flexural analysis. Many cases of elastic members of combined stability must be considered on the member.

**C6.2 AXIALLY AND SINGLY SYMMETRIC MEMBERS SUBJECTED TO COMBINED AXIAL FORCE**

Equation (6-1) is linear interaction equation subject to axial force and bending moment and also intended to guard combined axial force; it provides a more conservative design than a parabolic equation, which is also linear for combined axial and limit states both in-plane buckling. It is anticipated that the following interaction equation for beam-columns also applies in Chapter 6 for the axial loads P with in-plane. The nominal axial compressive strength $P_n$ determined from the provisions of Chapter 4, and the nominal flexural strength $M_n$ is determined in accordance with the provisions of Chapter 5. In Chapter 6, combined load interaction for combined axial tension and flexural moment applies.

**C6.4 DOUBLY SYMMETRIC MEMBERS SUBJECTED TO COMBINED AXIAL FORCE AND BIAXIAL TORSION**

**C6.4.1 Circular and Rectangular Tubes Subjected to Combined Axial Force and Torsion**

Circular tubes and Rectangular tubes subjected to Torsion, Chapter 8 provides information properly recommended in design procedures for both rectangular and circular shapes subjected to torsion. Therefore, closed sections are generally recommended in design applications subjected to torsion loads to other shapes subjected to torsion, as it closed sections offers resulting from resistance wrapping and orientation or at torque level or moment, subjected to axial compression torsion loads may require special design requirements. Vinson and Sierakowski (1986) refers equations in Section 3.3.2.

Torsion coupled with all closed sections is assumed to be resisted primarily by shear stress $\tau$ which is along flexure or web of the rectangular tube. The shear stress will develop in the closed section surrounding to other locations into the web areas. When the critical shear stress, $\tau$ is reached due to buckling, the member section is described using Equation (6-4) as $\tau_{max}$ reference stress from shear in the longitudinal direction stress in the longitudinal critical section the torsional moment (shear flow $q = \tau(t)$) or equivalent nominal torsional constant (polar moment of inertia or of torsional composite of the web), to establish the original axial capacity in Section 3.3.2.

When the critical shear stress, $\tau$ is reached due to buckling, as described in equation of the governing Equation (6-4), or otherwise. The shear principal stress, $\tau_P$, Krell stress critical regions of the composite has following recommendations and subsequent modification.

Torsional couple tests of composite modes of reinforcement change of forces transverse which is subjected to failure either interaction which is subjected to lateral torque stress at ultimate. Through ultimate limit procedure load (Section 8.7), Vinson and Sierakowski (1987) give an equation for the elastic buckling strength of closed sections of fiber reinforced thin-walled modes of orientation change of the axially which results failure test the design. The equations use theory, developed and reinforced by equations, natural set at some level of orientation stress. Equation 8.6-3, in Appendix 8.9 provides equations 8.6-3, by Zureick and Steffen (2000), which approximation to the equation is a cylinder of moderate length.

Assuming critical loads with shear stress for all rectangular and torsion, shear 8.6-3, by Theocharides and Gere (1961),

$$\tau_{cr,t} = 2.25\pi^2\left(\frac{1}{b}\right)^2$$
(C6-1)

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

75

<!-- Page 91 (Page 16 of extraction) -->

The equations that express the critical buckling stresses do not account for initial imperfections. Vinson and Sierakowski (1978) recommend an additional multiplier of 0.67 when using these critical buckling stresses for design. The critical buckling stress values obtained should be also limited by the value of the in-plane shear strength of the composite. This limitation is to ensure that the limit state of rupture is not exceeded when the material is subjected to shear stress.

Closed-form beam equations are provided herein for rectangular shapes under torsion in terms of material and cross-sectional properties. These beam equations are extended for anisotropic materials from the global torsional buckling equations of beams subjected to torsion for isotropic materials (Timoshenko and Gere 1961). Local torsional buckling equations are not provided herein; hence, designers should use rational analysis to arrive at local torsional buckling values for various tube cross sections.

**C6.4.2 Rectangular Hollow Tubes Subjected to Combined Torsion, Flexure, and Axial Force**

Equation (6-10) combines the stresses due to bending and axial loads with the square of the fiber stress due to torsion. This equation coincides with that proposed by Bruhn (1973) for thin-walled tubes made of nitrocellulose, commonly referred to as celluloid material, and resembles Equation (C-H3-8) of AISC (2016). Qureshi (2012) demonstrates the applicability of this equation to pultruded FRP members for closed sections manufactured with fiber reinforced polymer composites.

---

**STANDARD ASCE/SEI 74-23**

76

<!-- Page 92 (Page 17 of extraction) -->

# CHAPTER C7
# DESIGN OF PLATES AND BUILT-UP MEMBERS

**C7.1 SCOPE**

The provisions of Chapter 7 apply to pultruded plates with relatively constant thickness and nominally orthotropic material pultruded plates and honeycomb or sandwich panels built-up with different materials. Plates manufactured using polymers reinforced by continuous fiber are made of pultruded plates and components with different material properties. Plate panels cover a wide range of applications and combinations.

**C7.2 GENERAL PROVISIONS**

Pultruded plates are planar structural elements whose thickness is substantially less than the span between supports or other constraining elements. Common uses of pultruded plates include decks, gratings, shear walls, and diaphragms.

Alignment and material orthotropical direction properties with plates are determined to establish these orthotropical directions on plate analysis and design of plates. The stress-strain longitudinal direction corresponds to the main longitudinal direction of the pultruded plate. The stress-strain longitudinal direction orthogonal to the pultruded material direction.

**Plate:**

[THIS IS FIGURE: Two diagrams showing plate geometry with labels for perpendicular directions, material directions, and dimensions. Case α = 0 and Case α ≠ 0 are illustrated]

**Figure C7-1. Principal material directions for pultruded plates.**

[Additional text and descriptions continue regarding material properties, stress concentrations, and design considerations...]

**Table C7-1. Material Failure Modes and Test Methods for pultruded plates.**

| Failure Mode | Characteristic Strength | Test Method | Nominal Strength |
|--------------|------------------------|-------------|------------------|
| Tensile strength | $F_t$ | ISO45 D3039 | $N_t$ |
| Compression strength | $F_c$ | ISO45 D3410 | $N_c$ |
| Tensile strength perpendicular to fiber direction | $F_{yt}$ | ISO379 D579 | $N_{yt}$ |
[Table continues with additional rows...]

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

77

<!-- Page 93 (Page 18 of extraction) -->

[THIS IS FIGURE: Multiple diagrams showing shear plate configurations]

**Figure C7-2. Shear plates for in-plane loading**
- (a) Shear plate perpendicular to the material longitudinal direction
- (b) Shear plate perpendicular to the material transverse direction

**Figure C7-3. Shear plane for through-the-thickness shear applied perpendicular to the material longitudinal direction.**

**Figure C7-4. Shear plane for through-the-thickness shear applied perpendicular to the material transverse direction.**

Figures C7-2, C7-3, and C7-4 illustrate the orthotropic plates supported by framing around the plate edge. The pultruded plate is in the material longitudinal or material transverse direction corresponding to Figures (shown 2003, 2004).

Engineering mechanics methods based on the theory of plates will provide accurate configuration of bending moments and shear forces along the plane supported edges of a plate element. The plate walls can be used to compute bearing moments and shear forces assuming that plate walls and transverse support at a plate direction. The strip method (also called yield-line theory) which is analogous to the method of plasticity for plates described by Wood and Armer (1968), Wood (1961) in AISI 2016).

**C7.3 DESIGN OF PLATES SUBJECTED TO FLEXURE**

Pultruded plates subjected to lateral loading supported on two opposite edges, such as for plates supported on one direction, have design strength based on two cases:
- (a) through load on the material longitudinal direction
- (b) transverse edge elements, have the plate supported on one direction (Tsai and Hahn 1980; Zhou and Hong 1995; Timoshenko and Woinowsky-Krieger 1959; Szilard 1974).

**C7.4 DESIGN OF PLATES SUBJECTED TO COMBINED TRANSVERSE PRESSURE AND IN-PLANE SHEAR**

Plates loaded applied transverse pressure combined with in-plane shear strength is two directions at any set of plate shear strength at the same use of a transverse shear strength is Equation (5-4) The applied in-plane shear and member thickness (Barbero 2014; ASTM 11).

**Figure C7-5. Pultruded plate subjected to in-plane shear direction σ=α (source ASTM D5379 2012).**

[THIS IS FIGURE: Diagram showing forces and directions on a pultruded plate]

**Figure C7-6. Pultruded plate subjected beam specimen in the longitudinal direction, σ=0 (Source ASTM D5379 2012)**

[THIS IS FIGURE: Diagram showing beam specimen configuration]

---

*STANDARD ASCE/SEI 74-23*

78

<!-- Page 94 (Page 19 of extraction) -->

The pull-through strength is obtained in accordance with ASTM D3410 through testing of plates. The bearing strength can be determined in accordance with ASTM D953 (2010). Equation (7-5) characterizes the failure mode diameter to fastener hole diameter ratio, pitch-to-fastener-hole diameter pitch, and the edge distance in the direction of load.

**C7.5 DESIGN OF PLATES SUBJECTED TO IN-PLANE TENSILE LOADING**

**C7.5.1 Nominal Axial Tensile Strength**

Pultruded plates are the plate reference strength behavior can be evaluated by various empirical or theoretical methods (see Jones 1998; Herak 1998). The plate thickness for tension (through-the-thickness) strength of Section 3.3.2 applies.

The open-hole effective stress concentration factor in ASTM D5766 is defined as:

$$k_t = \frac{F_t}{F_{toh}} \left(1-\frac{d}{W}\right) - \frac{F_t}{F_{toh}}$$
(C7-1)

where

$F_t^* = \text{Characteristic open-hole gross stress longitudinal tensile} strength, and
$F_t = \text{Characteristic longitudinal tensile strength.}$

$d=$ Nominal hole diameter, and
$W=$ Width of the plate

The numerical values of $k_t$ for practical $k_t$ is expected in the following the test results to be corrected $k_t$ at open-hole tension plates, specimens were calculated. Equation (7-5) to correct tensile strength as designed at the net section stress to correct for shear lag. For practical holes correction factor is calculated based on result strength data of pultruded plates and composites of the Lekhnitskii failure. The correction factor can be obtained by finding fiber strength of openings. The correction factor $k_t$ used for transverse material is defined as $$k_t^* \leq 1$$
(C7-3)

$$k_t^* = \left(\frac{2E_L}{E_L + E_T + v_{LT}G_{LT}}\right) \leq 1$$
(C7-4)

The numerical values of $k_t$ and $k_t^*$ are specified based on several computational models. It is expected that computed based on result strength data of pultruded plates. The stress at any location is given by elastic failure of plates. The stress interaction of the loaded plate stress. ANSC failure design (2006), as shown in Figure C7-6 open-hole stress concentration.

---

[THIS IS FIGURE: A graph showing "Open-hole tensile strength reduction factor in the longitudinal direction" with x-axis labeled "Hole Diameter to Width Ratio" and y-axis showing stress concentration values. Contains scattered data points and trend lines.]

**Figure C7-6. Open-hole tensile strength reduction factor in the longitudinal direction.**

The longitudinal nominal open-hole longitudinal ultimate tensile strength based on the effective net area shall be determined by the gross area in the material longitudinal transverse directions and the Poisson's ratio for the plate in each measured direction. The in-plane shear modulus and the longitudinal and transverse material directions are defined as where the ratio of these materials properties can be described by: Equations (7-5) nominal transverse direction open-hole, as assumed in Equation (7-7). A reference value for the in-plane longitudinal criteria (Barbero 2014; by test).

The failure criteria (7-5) through to direction open-hole, as assumed in Equation (7-7). A reference value for the in-plane longitudinal as well as some plate with average hole coordinate their axis (Barbero 2014).

**C7.6 DESIGN OF PLATES SUBJECTED TO IN-PLANE COMPRESSIVE LOADING**

**C7.6.1 Longitudinal Compression**

Equation (7-8-3) provides an analytical form derived from interaction of compression of open-hole plates subjected to in-plane compression.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

79

<!-- Page 95 (Page 20 of extraction) -->

[THIS IS FIGURE: Graph showing "Open-hole tensile strength reduction factor in the transverse direction" with scattered data points and trend lines]

**Figure C7-8. Open-hole tensile strength reduction factor in the transverse direction.**

provisions of Section 7.2 and are subjected to in-plane compression at at α ≠ 0. Section 7.6.2 is provided for the designer to evaluate open-hole compression for plates loaded at α ≠ 0.

**Alignment Factor (η) for Lost Use**

In situations when buckling is used per Section 2.4.2 for plates experiencing in-plane compression, the designer should account for variation in the material properties and temperature in accordance with Section 2.4.5.

**C7.6.2 In-Plane Compression Plates Subjected to Combined**

Equation (7-8-2) through (7-8-4) are provided at the transverse directions. The plates are supported adjacent to plates for other edge boundary conditions such as cantilever plates (two edges simply supported, the other edge clamped). Equations (7-8-5) through (7-8-7) are applicable for the plate and Spectral 2001), Reddy and Rao (1998) and Qatu et al. (2012) provide analysis on different plate boundary conditions.

**C7.7 DESIGN OF PLATES SUBJECTED TO IN-PLANE SHEAR LOADING**

**Orthotropic Properties (η-φ) for Plates Sub jected to Shear** Equation (7-9-2) shows the equations which are applied based on basic principles of plates for rectangular plate with three edges that are simply supported and one free edge is applied as in Equation (7-9-2) of a plate with four loaded edges shear stress is evaluated based on results obtained from numerical simulation and experiments. ASTM D5379/D5379M (2012). Dano et al. (2000) showed that analytical models with shear stress are provided to analytical or analytical or simple analytical or plate. When the plate is in the material longitudinal direction, $k_e$ = 8.98. Equation (C7-8) shows the relationships with stress states. The designer is responsible for conducting additional analyses when mechanical fasteners or mechanical fasteners are used to connect two or more plates, which should be analyzed with stress. Accordingly, based on the failure criteria of open-hole plates at shear subjected with multiple orientations of fiber in open-hole plate for use in the overall system. Accordingly, of tests described in ASTM D5766/D5766M (2011) can be utilized as a means to evaluate plates behavior to in-plane shear. When applied loads are specified for mechanical fasteners with the failure criteria. The designer must be adequate to allow stress analysis in several directions required to complement with the reinforcement given by:

$$F_{eh} = \left(\frac{1}{(F_{x}/G_{LT})}\right)^{2} \left(\frac{G_{LT}}{E_{x}}\right) \left(\frac{P_{cr}}{N_{cr}}\right)$$
(C7-6)

where
- Thickness of the plate:
- The characteristic properties in the material longitudinal direction.
$G_{LT}$ = Characteristic in-plane shear modulus adjacent for real edge dimensions in.
$F_{xcr}$ = Nominal longitudinal stress.

---

[THIS IS FIGURE: Scatter plot showing "Experimental versus predicted strength values of axially compressed single plates with open holes" with data points and trend lines]

**Figure C7-8. Experimental versus predicted strength values of axially compressed single plates with open holes.**

---

*STANDARD ASCE/SEI 74-23*

80

<!-- Page 96 (Page 21 of extraction) -->

[THIS IS FIGURE: Two diagrams showing pultruded plate V-notched beam specimens for in-plane shear strength]

**Figure C7-9. Pultruded plate V-notched beam specimens for in-plane shear strength, $F_s$:**
- (a) Shear plane perpendicular to the material longitudinal direction
- (b) Shear plane perpendicular to the material transverse direction

in-plane shear modulus and strength of pultruded composite tested per Figure C7-9 (Banks-Sills et al. 2005).

**C7.7.2 Nominal Buckling Strength of Plates Subjected to In-Plane Shear Loading**

Equation (7-9-4) provides an expression to be used for calculating the buckling strength of plates loaded in shear supported around the edges and subjected to shear loading. This expression is applicable for plates with simply supported or clamped edges (Xue et al. 2012; Chai 1992).

**C7.8 DESIGN OF BUILT-UP MEMBERS THAT**

**C7.8.1 In-Plane Shear Loading**

For plates with in aspect ratio $a > 3$, Equation (7-9-4) is used to calculate buckling strength. Other aspect ratios require the appropriate buckling coefficient (Turvey and Sana 1990). Values of the buckling coefficient $k_s$ and $k_{xz}$ in Equation (C7-9) are established by AISC values.

**C7.8 DESIGN OF BUILT-UP MEMBERS**

Built-up members are constructed from individual pultruded flat area fastened or bonded together.

[THIS IS FIGURE: Diagram showing an in-plane shear loading configuration with arrows and dimensions]

**Figure C7-10. In-plane shear loading.**

[Additional text continues with technical details about longitudinal stiffeners, buckling behavior, and design considerations...]

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

81

<!-- Page 97 (Page 22 of extraction) -->

pultruded flange components. Decking members include decking, roofing, and flooring systems consisting of two or more pultruded components that are connected. Decking members comprise planks, panels, connectors, hangers, and end caps. Pultruded decking members can be used in applications such as platforms, walkways, roofs, floors, wind walls, bridge decks, building panel systems, formwork, and trench covers. Panels can be connected using connectors, toggles, and/or hangers. Modular decking systems can be made of interlocking profiles (Dutta et al. 2007). Built-up members can be used for sheathed shear walls (vertical diaphragms) and horizontal diaphragms made with

connected pultruded plates and framing components acting as elements of the lateral force-resisting system.

**C7.9 DESIGN OF PLATES FOR SERVICEABILITY**

In addition to strength limit states, plates and built-up members also satisfy serviceability limit states that define functional performance under load and include such items as short- and long-term deflection and vibration. Shear deformations can be neglected for computing deflections of pultruded plates that satisfy the requirements of Section 7.2.

---

**STANDARD ASCE/SEI 74-23**

82

<!-- Page 98 (Page 23 of extraction) -->

# CHAPTER C8
# DESIGN OF BOLTED CONNECTIONS

**C8.1 SCOPE**

The provisions of Chapter 8 cover the design of bolted connections in pultruded structural members. The design provisions for both strength in this chapter are not based on fatigue testing. Closed-form equations for allowable bearing stress for connections of bolted connections are documented. The design provisions can be applied to members made from similar or different materials. For members from joints entirely by way of bolting between the connected members, with no connection via adhesive bonding or welding. Shear transfer is to take place through friction between the connected and connecting elements, and design equations to address local buckling and stress limitation at the section of interest are provided. The connection elements are manufactured from pultruded FRP elements. The application of this chapter is limited to bolted joints only.

Although traditional mechanical is one whose transfer of connection joints provide two types of mechanical connection of connected plate and pultruded structural members fastened with bolts or rivets are widely used, but less information is available about their behavior than adhesively bonded or welded joints. Mechanically fastened plates in pultruded FRP material is limited.

The design of bolted connections with FRP materials is mostly experimental in nature (e.g., Rosner and Rizkalla 1995; Mottram and Turvey 2003). Although a number of test programs have been conducted with materials variations, connections characteristics is mechanical properties with orientation and rotation-type combining, and the stress-strain response to the connections. A different behavior of connections is unique to the internal modelling (i.e., a model to predict or strain models coordinate or material yielding in connections) with the material and element geometry to understand the joint behavior design model. Similarly, the design provisions developed herein are based on relatively high-stressed connections, increasing temperature will potentially cause stress diffusing and changing in connection responses when the resistance of connected members and geometry to understand the structural connection cannot be used. Therefore, guidance provided by this research and its extensions covered by Chapter 8 of FRP products rather than

along manufactured by pultrusion are used, the designer is referred to publications on connections mechanically fastened in glass-fiber-reinforced polymers, which provide mechanically strength formulas.

The formally accepted design provisions, gusset, splice plates, and connecting plates are included. The bolt load and bolt holes or other mechanical metal spliced connection materials are required design element per that material (AISC 2016b, AIM 2017). Replacing steel elements must be selected from the requirements of the construction materials for the approved manufacture. Another choice might be mechanically fastened steel, not be appropriate aluminum.

Pultruded bolted end materials provide only a single row for bolts in any direction. For materials at joint of metal in a pultruded materials such as mechanically fastened metal connections strength from foot or shear bolt stress to fastened.

Quality assurance provision in one where connection with includes screws, set metal proprietary fastening systems, typical elements included the examples must be understood in Appendix D. Handbook of Composites (Lubin 1982). Section 8.2 (design of single bolted connections Chapter 8.2 establishes the full FRP bearing length. For the materials to be located as to end-to-end shall be bolted connections with mechanical location of the full FRP bearing length. For the materials to the length is limited to providing less FRP material in the gage (perpendicular to applied loading), and the end distance from the edge to the center of mechanical fasteners provide for in determining the connection design resistance by rational engineering analysis. The equations shall elements that design are based on different to ultimate limit state design where failure in the portion of the bolted in Section 8.2 through accounted for in determining the connection design resistance by rational engineering analysis. The equations shall shall be combined failure at design capacity in the location to ultimate element design shall be action of the bolted portion of the connection fails first.

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

83

<!-- Page 99 (Page 24 of extraction) -->

Connections can be designed based on a realistic assumption about the desired and minimum capacity of bolts, though certain assumptions should be used to determine the distribution of loads.

Connection size and forces and moments applied to the connections:

**C8.1.1 Serviceability**

Serviceability required by the distribution of forces and rotation are an important aspect. In the event that a more precise analysis of a joint cannot be made, then the deflection could be realistically and carefully reference within the load of the joint or the service limit load of the connection.

**C8.1.2 Clearance and Spacing Requirements**

A conservative design of the connection compared to the member of the members they connect. This is true because the resistance of connections that are adjacent as far as members is relatively more ductile. However, the possible load path in the adjacent members, and will be capable to follow failure of a member subjected to load path in the bolted connections state in the structural members. For typical deflection or elastic buckling should be avoided at normal service load; and the forces and moments at connections will be safely transformed into the capacity of the elements that are connected. Bolt spacing shall be considered for bolted connections.

The design of bolted connections between axially loaded single or multiple rows plates shall be capable of maintaining uniform bearing throughout the plates after. After this connection that are necessary to resist normal bearing actions in the design at the ends of connecting bolts may be ignored in having marginal effect on adjacent failure elements and rotation of connections in such connected holes. For rectangular bolt holes, at the most number of range of bolts that FRP material is to have rotation capacity to accommodate the required rotation determined by the analysis of the particular connection. Requirements included only bolts aligned across the connection. Although full-sized nuts bolts internal connected bolts. Although size nuts bolted nuts and joint assumptions are not loaded to final strength of attached fasteners (Rosner and Rizkalla 1995). This standard considers a connection internal extended connections. This standard considers a connection internal extended connections. connection bolts that have dimensions of which where holes size at diameter is less than a rotation or clip bolted in the web of one of the members being joined.

Maruyama (2011) represents several other ways to bolts both single bolts into several groups.

Section 2.3.5 covers the design requirements of connections, and Section 8.2 provides general information on typical configurations for each category. At the conclusion of a design, it is prudent before the locations where beams are connected. FRP slip angles are recommended where full-scale tension tests are placed, or spliced or mechanically lapped. Inspection and maintenance of mechanical-member systems are fully understood. For instance, the extent of pultruded FRP material should become greater as excess of 5% by Chapter 8 of the most recent edition of AISC.

Chapter 8 outlines the connection components, For simple bolted connections, the designer is required to select the test of the assumptions of the strength of the bolted parts or splice elements per Chapter 8 to determine the connection design per AISC analysis (AISC 2016). Direct the analysis has been completed, the detailed engineering analysis can proceed to evaluate if strength Chapter 8 are required to provide adequate configurations to check the ASTM (in FRP connections) or a established after the final component members should verify partially or wholly within the strength test by connections it.

Classification of a connection result not depend on the connections that are used to transfer forces and moments to connections is to support different categories of connections (Wood and Hurley 1997; Xiao et al. 1997). In mechanical connecting elements of $K_n = M/θ$, where $M$ is per moment and rotation $θ$ respectively; $I/L$ is per moment and $I/L$ related to rotation of bolted elements. The classification factor is related to connections as primarily defined to specify the design of connection and assumed as the connection.

The bolted connection is the maximum moment that the connection can sustain without failure. Muttram 1996; Muttram 2011. The design should also ensure that the connections are available to evaluate of Chapter 8 providing requirements to the designer used of the most recent American Concrete Institute (ACI) Institute (ACI) design using details permitted by this standard, the rotation at the onset of bolt failure will determine requirements. The standard assumes that connections can be readily considered to satisfy bolt failure specifications. The joints in a connection are readily distributed or to rotation or slip, details permitted by this standard for rotation at the onset of bolt failure specifications. The joints are assumed in equations of all of the bolted members and connecting plates. In accordance with section permits the rotation configuration in ASTM for connections. These rotation values ensure that connections can satisfy all the elements of bolt Design is in accordance with the requirements of Section 8.1.2, because both bolts and understanding of the moment resistance are provided.

When design is in accordance with Sections of Section 8.1.3, the bolts in a connection (e.g., section of bolts at a range using FRP spliced on multiple Maruyama 2011).

---

*STANDARD ASCE/SEI 74-23*

84

<!-- Page 100 (Page 25 of extraction) -->

## C8.2 GENERAL PROVISIONS

**C8.2.1 Bolts**

The provisions of Section 8 and parts of this chapter provide the design equations and details for assembling bolted connections with FRP and with nonmetallic components Chapter 9 are for plate-to-plate connections with single direction stiffness. Some results from ASTM A307 bolts per Specification for Carbon Steel Bolts and Studs, 60 000 psi Tensile Strength (ASTM F3125/F3125M (ASTM 2015a). For bolted, FRP to FRP connection, the FRP bearing strength should be checked.

Therefore, the design should use of galvanized bolts. Bolts to be used in bearing FRP connections used only be of equivalent or greater strength (ASTM F3125/F3125M 2015a); bolts other than those noted above cannot be used. Failure modes of the connection depend on the extent of the clamping forces, materials, bolt sizes, and bolt spacing. From an analysis of the elevated bolt, will vary depending upon the mechanical fastener selected and the manufacturer's recommendations. Different designers (based on the composite materials, bolt materials, and loading conditions) may need to provide both loading capacity to the design of the bolts. The usage indicated condition is to be satisfied if the bolt exceeds the ultimate capacity by more than the capacity strength limits it should be verified that the stress induced in the structural load without clamping force induced by bolt tightening (the level of which is not specifically defined in this standard) will not cause failure, although (AISC 2016), tightening the bolts is a very organized method; tightening may reduce stress and load tensioning effects by clamping forces. When using the tangent modulus theory, the specified total strength value equals should be zero; the percent-turning method produces turning by 1/3 or 1/2 for values greater than one (Gombo 1996) states bolts of 5 in. (1/2 in.) diameter of larger are permitted for a nut rotation of 30° with respect to the bolt. For tightened bolt, the turning should be specified to provide enough clamping force. The screw-tightened condition is to be satisfied of the bolt produces the maximum torque that can be applied to the fastener.

Bolt threads should be excluded from connections in which shear transfer occurs (ABC 2016). Care should be used in structural steel connection using bolt in AISC 2016) tightening the bolt is a very organized method tightening method indicates that the capacity strength should be excluded on the nominal bolt areas except when assembled bolted connections need only be bolted (2001).

For loose conventional when assembling bolted connections, the force must be directed bolt in such bearing surfaces that the contact shall. In accordance with some ASTM conventional and long requirements all the materials of the end bolts or joint used.

When a loose consideration when assembling bolted connections, the force must be prevented from bending the piles into cross-section, being tightening the bolt as the screw connection by friction (Maruyama 2003). Chapter 8 provisions require that the connection be subjected either friction or bolt that can be tightened bolts for a moment is a free-edge member. Where the moment in the connection generates bearing by material at the connector and therefore in practice the capability of the FRP materials cannot exceed the full characteristics.

To prevent crushing beneath the bolt head or nut, a washer or diameter at least equal to the bolt fastener, is always required when bolt is used for steel plates (ASTM FRP standard-tool bolts) or greater thicknesses corresponding to the diameter from edges (both head and nut). The washer must fit over the outside of concrete structure must prevent holes from this.

• Anti-seize lubricant will reduce the tendency for metallic corrosion
• Tightening of bolts should be undertaken as a uniform rate
• Nut rotation to be gradual as further clamping of the connection may be considered sufficient only after:
  - all bolts are not strengthened
  - no bolt is loose
  - washer should not damage nut, or thread bolted adherent seals should be capable of minimizing of bolt and nut and securing of the bolt at its correct distance from the end.

For avid initialing the walls of the FRP shows, care is to be taken in tightening. If tightening bolt is over-tensioned, joints can be contacted with the washer, the bolt head, and/or the nut should not have a chamfered edge. Tightening should also occur when threads are smooth.

Holes in the connection provided by clamped bolts and designed holes should be reasonably clean and free of debris at all times.

A thread bearing washer, locking washer, locking nut, or push nut can be used in a combination to restrain on loosening (Maruyama 2004) that may be caused and or be applied to excess of bolt tension less and the standard cannot be specified (ASTM A510 or A563 2015b), standard for both FRP standard-tool bolts (ASTM F3125 2015a), stainless steel bolts (ASTM F594 2015b), and not (ASTM F467 2015c) are suitable for ASTM specifications of corrosion resistance and by the design. The required thread engagement is approximately 3.5 diameters per ASTM A510-95 (1995a); and nuts are 0.5 in (1.3 cm) diameter in diameter and one bolt (ASTM F594 2015b) and of the same area.

**C8.2.2 Nuts and Washers**

The nuts to be used with the bolts shall be designated on the drawings. In the design of joints for load-carrying metal or pultruded plates, the FRP bearing standard ASTM F594 (2015b) stainless steel bolts FRP standard washers (to steel bolt) (ASTM F436 2015d) washers for the material per ASTM F436 2015d or equivalent for ASTM washers. Common standard used washers. Nuts ASTM F594 (2015b); F and G and standard steel type F467 (2015c), Table 7 and/or 8 of stainless steel bolts per ASTM F594 (2015b); washers of steel bolt as ASTM F467 (2015c)are required to be within -4 of the same of material or pultruded structure and joint assembly surfaces that may.

To prevent crushing beneath the bolt head or nut, a washer of diameter at least equal to the bolt fastener, is always required when bolts shall be 3 in. or greater and nut head that FRP shall: For standard threads, the washer shall be a minimum thickness to at least 0.095 in. (2.4 mm). Minimum washer thickness is set at

---

*Load and Resistance Factor Design (LRFD) for Pultruded Fiber Reinforced Polymer (FRP) Structures*

85


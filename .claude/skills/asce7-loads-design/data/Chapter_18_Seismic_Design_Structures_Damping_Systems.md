# Chapter 18: Seismic Design Structures Damping Systems

**ASCE 7-22 Minimum Design Loads and Associated Criteria for Buildings and Other Structures**

---

*This chapter combines pages 265-280 from ASCE 7-22*

---

**18.1.1 Scope** This chapter sets forth requirements for the design of structures with a damping system, and every element of the structure, when either strength design or allowable stress design is used in accordance with the requirements of this standard as modified by this chapter. Where elements or components are required to transfer forces from damping devices to the structure or its foundation elements, such elements are to be designed in accordance with Chapter 17.

**18.1.2 Definitions** Definitions specific to structures with damping systems are defined in Chapter 11.

**18.1.3 Notation**

**DAMPING DEVICE:** A flexible structural element of the structure that dissipates energy through damping mechanisms is required in this chapter. Damping devices that do not dissipate energy, or provide effective damping, are classified as supplemental damping devices.

**DAMPING SYSTEM:** The collection of all individual damping devices and all structural elements that transfer forces from damping devices to the other elements of the structure or to its foundation. Additional design requirements are provided in Section 18.2.

**DISPLACEMENT-DEPENDENT DAMPING DEVICE:** A damping device for which the resulting force is a function of the relative velocity between each of the device ends and the other extreme of the device. Additional design requirements and other information are provided in Section 18.2.

**VELOCITY-DEPENDENT DAMPING DEVICE:** The damping device for which the force is a function of the relative velocity between each end of the device and the other end of the device.

For effective damping equal to 5% and period of Section 12.8.1.1:

$g$ = Numerical coefficient, as set forth in Table 18.7-1; applied to account for uncertainty in damping properties at the nominal design value as opposed to at the design value;

$\rho_{int}$ = Numerical coefficient, as set forth in Table 18.7-1, applied to account for $g$ period $\beta$ for period of structure, measured in Table 18.7-1; at each direction;

$\beta$ = Numerical coefficient, as set forth in Table 18.7-1; applied to account for period of structure in the direction of consideration in the design of the structure with damping system at the design displacement, period of the damping system in the direction under consideration, Equation (18.2-4);

$B_1$ = Coefficient for effective damping of the structure at the maximum displacement in the direction of interest, Section 18.7.3.2;

$C$ = Numerical coefficient, for effective damping of the structure in the direction of interest, as prescribed in Section 18.7.3.1;

$C_0$ = Numerical coefficient, as set forth in Table 18.7-1;

$C_1$ = Numerical coefficient for the effect of the fundamental mode response coefficient, Section 18.7.3.2;

$C_2$ = Modal coefficient calculated as the ratio of the horizontal component of seismic force in the direction of force, as determined in Section 18.2.2.1;

$C_3$ = Horizontal response coefficient of the residual mode of vibration, Section 18.7.3.2;

$C_{\text{ve}}$ = Seismic response coefficient for linear response of the structure of response, Section 18.7.3.2;

$C_{\text{vm}}$ = Seismic response coefficient for the level of vibration of the residual mode of vibration, Section 18.7.3.2;

$\rho_{test,max}$ = Fundamental mode design displacement of the center of rigidity of the roof level of the structure in the direction of interest, Section 18.7.3.1;

$\rho_{test,min}$ = Residual mode MCE_R displacement of the roof level of the structure in the direction of interest, Section 18.2.2.1;

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                203

---

$D_1$ = Displacement at the center of rigidity of the roof level of the structure (in the direction of interest), calculated from the modal displacement of the first mode shape and the displacement corresponding to the fundamental mode, $D_M$, approximately equal to 1 in accordance with Section 12.8.7.

$D_{TM}$ = Maximum displacement corresponding to the sum mode of response in the direction of interest, Section 18.7.3.2.

$E_1$ = Total cumulative hysteretic energy dissipated between equal positive and negative amplitudes and obtained in the direction of interest, Section 18.7.3.2.

$F$ = Lateral seismic force on a story level in the direction of interest, Section 18.7.3.2.

$F_{a,max}$ = Value of seismic force $F_a$ corresponding to the maximum displacement of the center of rigidity at the limit of structural behavior, Section 18.7.3.2.

$F_s$ = Lateral level of level r or force applied at the residual mode, Section 18.7.3.2.

$h_x$ = Structural height, Section 18.7.2.3.

$i$ = One story level of the structure, designated the mass at level $i$, in the direction of interest, Section 18.7.3.2.

$k_{M}$ = Effective stiffness of the damping system in the direction of interest, Section 18.7.3.1.

$K_{story}$ = Story stiffness of the structure in the direction of interest, story stiffness is defined as the lateral force or shear divided by the interstory drift displacement in accordance with Section 18.7.3.2.

$Q_d(r)$ = Force in an element of the damping system required to restore equilibrium at a given relative displacement if the effective yield displacement of the structure in the direction of interest is prescribed by Section 18.7.3.2.

$Q_{d,max}$ = Maximum force in an element of the damping system required to restore equilibrium in an effective damper or hysteretic damper at its maximum displacement in the direction of interest, Section 18.7.3.2.

$T_{a,eff}$ = Sum of factors of response velocity obtained in a damper at the maximum displacement, Section 18.7.3.2.

Minimum value of the factor relative to the seismic design base shear of the fundamental mode in a given direction of response at a displacement equal to the maximum effective design displacement corresponding to Section 18.7.3.2.

$S_{ai}$ = Individual spring and environmental effects.

$S_c$ = Factors to represent possible variations in damper properties above the lower values caused by aging, environmental effects, and manufacturing, etc., is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{max,max}$ = Factor to represent possible variations in damper properties above the upper bound values caused by aging and environmental effects, etc., is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{max,min}$ = Factor to represent possible variations in damper properties below those nominal properties caused by aging, environmental effects, etc., is a multiple of all the testing period, versus, then is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{min,max}$ = Factor to represent possible variations in damper properties above the nominal values caused by aging, environmental effects, etc., is a multiple of all the testing period, versus, then is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{min,min}$ = Factor to represent possible variations in damper properties below the nominal values; and

$\lambda$ = Factor established by the RDP to represent possible variation induced by aging, environmental effects, and manufacturing.

in = Effective damping of the seismic force-resisting system in the direction of interest caused by inelastic response, determined in accordance with Section 18.2.3 and $\beta_{eff}$; in the numerical coefficient as set forth in Table 18.7-1 as a function of the response modification factor, $R$, determined in accordance with Section 12.2 and $R_{eff}$.

$\beta_M$ = Effective damping demand on the seismic force-resisting system in the direction of interest caused by inelastic response during a cycle of loading in accordance with Section 18.7.3.1.

(18.2-3)

$$\lambda_{\text{use}} = 0.75 V$$ (18.2-2)

where

$V$ is the seismic base shear value at the direction of interest, determined in accordance with Section 12.8.1 and $R_{eff}$; in the numerical coefficient, as set forth in Table 18.7-1, determined in accordance with Section 18.2.3 or a period of structure in the direction under consideration, Section 18.7.3.1.

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

204

---

mode of vibration in the direction of interest.

**EXCEPTION:** The seismic base shear need for the design of a structure with a damping system has been less for analysis and design, provided the following conditions are met:

1. The structure is located in Seismic Design Category B or C;
2. The seismic lateral resisting system is each story, configured to resist structure; and
3. The design of the structure configuration is limit, and the design lateral loads consist of distributed and concentrated linear static loads in the damping system.

A maximum and minimum analysis and design procedure shall be used to establish the bounds of response and design for the damped structure. The effects of variations in effective damping properties shall be considered, as defined in Section 18.2.8.2, during both analysis and design of the structure.

The maximum value shall be considered explicitly. The $\lambda$ factor, elements of the structure, and energy dissipation shall be considered in analytical modeling and design for various conditions.

## 18.2 GENERAL DESIGN REQUIREMENTS

**18.2.1 Seismic Design Category** The structures shall be designed and constructed to resist the effects of earthquake ground motions and the damping system, as defined in the following:

1. Except as modified in this chapter, the seismic design category shall be determined using the governing code in accordance with Section 11.6.

A system that, for each lateral direction, combines to one of the types of systems in Sections 12.2.1.1 shall be permitted to be designed using the corresponding value of $R$ given in Chapter 12.

**18.2.2 Nonlinear Analysis and Design Procedure** The required design forces and displacement shall be performed at least based on approved dynamic procedures as set forth in Section 12.1 and other force procedures of Section 18.7.3. In permitted to be based on the procedures of this chapter.

For a structure subject to the requirements of this section and where the damping system is a significant component, the damped lateral force procedures of Section 18.7.3 and other criteria, the project engineer shall also address the following:

1. The linear effective damping calculated shall be considered as specified in Section 18.7.3.1 as part of the structure response, determined by a more refined method in the response used beyond the design earthquake level. The equation is expressed by $\beta_M$ is determined by the design engineer or a structural response as given in the maximum base-shear value corresponding to test value.

2. The damped vertical values cannot be reduced by the design engineer or a more refined method unless such actions would correspond to vertical ground motion responses and structure velocity.

The system base shear used for design of the structure in the earthquake direction shall not be less than the values of the resisting force procedures of the fundamental mode resisting system shall be determined by the structures in Section 18.7.3.

The design strength of the seismic force-resisting system shall not exceed 1.5 times, is expected strength using strength reduction factors of Section 12.4, and the design of elements and procedures for Section 12.4.

An independent design review of the damping system and related structure elements are required shall be performed such that no other individual elements and the selection of appropriate parameters for use in the damping system and damping device design, the peer damping properties shall be determined.

**18.2.3 Damping System** The damping devices and their components shall be designed to resist the forces and displacements caused by wind and earthquake according to code requirements in Section 18.2.4.3.

Damping devices shall fail to failure by low-cycle fatigue shall be designed for seismic extreme by nonlinear design, corresponding to at least times that the structure experiences the structure in Section 18.2.4.3.

**18.2.4 Damping System Elements** Mean aspects for the inspection and acceptable value of the damping device element shall be established in accordance with the materials code requirements. The damping device element established be designed according to code requirements. The strength of seismic shall not exceed the demand using the projected expected strength and the force procedures of Section 18.7.3, in permitted to yield or expected strength using the code requirements and structures shall be less than the value in accordance with Table 18.2-1 and Equations (18.2-1) and (18.2-2).

$$F_{\text{max,min}} = 1.5 Q_d$$ (18.2-1)

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

205

---

**18.2.1.2 Equivalent Lateral Force Procedure** The equivalent lateral force procedure, as prescribed in this section for the analysis and design, provided all the following conditions are met:

1. The height of the building lateral system in each story, over all the story, if either of the following conditions apply:
   a. The sum of the effective damping system has force
   b. The maximum value of the damping system has at least 75% of the story stiffness is vertical irregularity and
2. The seismic force-resisting system is a Type 1 horizontal structural irregularity and
3. The seismic force-resisting system has not been subjected to the prescribed damping system limit criteria.
4. Floor displacements are rigid, as defined in Section 12.3.1
5. The height of the structure does not exceed 160 feet.

## 18.2.4 Damping System

**18.2.4.1 Device Design** The design, construction, and installation of damping devices shall be performed at criteria that their elements shall be performed and criteria shall be permitted to use the corresponding criteria of the damping device specified in this standard or other criteria of the following:

1. Elements that resist demand forces caused by wind or seismic ground motions and in accordance of other appropriate loads;
2. Elements of the damping device is permitted to exceed vertical loads;
3. Elements that are manufactured device is permitted by vertical ground motions.

**18.2.2 Seismic Hazard**

**18.2.2.1 Ground Motion Acceleration Parameters and Spectral Response Acceleration Parameters** The ground spectral response acceleration parameters (e.g., $S_{DS}$, $S_{D1}$, and other elements of the damping system with elements for the corresponding design of lateral displacement or lateral deformation displacements at the acceleration parameters in Section 11.4.1, and other appropriate lateral force response of the displacement design parameters. Other elements of the damping system with elements for the corresponding criteria is set forth in Chapter 11.

**EXCEPTION:** It shall be permitted to analyze and design the structure, the value of these damping devices corresponding to site design parameters. The damping devices shall also satisfy the limits of Section 18.2.3.

**18.2.2.2 Procedure Selection** Structures with a damping system shall be designed in accordance with the damping system corresponding to a horizontal forces procedure or vertical displacements. The structure and vertical earthquake design parameters, permitted in accordance with Section 18.7.2, is appropriate for the Section 18.2.2.1 or Section 18.2.2.2, structure is permitted to be designed in accordance with Section 18.7.3.

**EXCEPTION:** It shall be permitted to analyze and design the structure using a validated design of Section 18.2.1, subject to the limits of Section 18.2.3.

**18.2.2.3 Damping Spectrum Procedure** The response spectrum procedure shall be used to meet the seismic design requirements, the values of a horizontal structural irregularity has at least 75% of the story using the maximum value in accordance with Section 11.2. The structure is permitted to analyze or design forces, and
1. The and values damping of the fundamental mode structural system is specified in Section 18.2.2.
2. The value and the damping lateral direction in the direction of interest is permitted to determine to the provisions of Section 18.2.1.

**EXCEPTION:** The required forces permitted in accordance with the damping devices shall also satisfy the limits of Section 18.2.2.

**18.2.3 Procedure Selection** Structures with a damping system shall be designed and horizontal irregularity, and the vertical damping system in accordance with the limitations and force provided is prescribed for Section 18.2, the damping device of the design requirements is permitted to be used based on characteristics of the displacement response characteristics of the damping system except where the criteria of the damping device in the design temperature shall comply with the conditions of design device elements to set forth in Section 18.2.4. For the corresponding structure or for the structure response characteristics of the damping device damping action is permitted to be the action of the device response or corresponding seismic damping forces shall comply with Section 18.2.4.

Damping devices subject to failure by low-cycle fatigue shall be designed to withstand forces corresponding to at least two times the design displacement or lateral deformation corresponding to the design earthquake, or at least forces corresponding to the force procedures of Section 18.7.3, using the maximum strength in the damping device MCE_R.

Damping device elements shall be a damping device or limiting in it is designed for an accidental excursivity-equivalent displacement and an accidental eccentricity displacement, or shall comply with displacement and acceleration in Section 18.2.2.

The maximum drift at MCE_R and vertical ground forces if not for the model of vertical forces shall be less than 200% of the maximum drift of the damping system corresponding structures or in the damping device the forces of the force in accordance with $C_0$ for the conditions and combinations are used and they include low loading as in prescribed to be selected in a corresponding design. A damping device the force corresponding to model drift in the damping the maximum design vertical forces in provided for damping action is prescribed to be corresponding.

Damping devices provide forces as a result mode of function of vertical response, the drift of the time time the maximum of the structural force displacement in accordance with Sections 12.4.5, until use the vertical response in a corresponding to Section 12.4.5, using the maximum strength in accordance with Section 12.4.5.

**18.2.2.4 Inspection and Periodic Testing** Mean aspects for the inspection and adequate active testing of the damping device shall be established as it is important to establish maintenance frequency or a vertical structures in the building to periodic inspection operations of inspections in Section 17.8.2, including disassemble inspection.

## 18.2.5 RESPONSE HISTORY

**18.2.5.1 General Design Requirements** The damping device and elements with a corresponding effective seismic force-resisting.

The stiffness and damping properties of the damping device shall be verified by testing as prescribed in Section 18.8. The model forces is a displacement a time-history characteristics of the damping device shall be performed in a testing conducted in Section 18.8.2 and the damping device properties shall be based on Section 18.2.2.

A minimum response history analysis shall be used a mathematical model for the drift that not be design responses.

Response history procedure shall be based on lateral displacement procedures or corresponding as the accidental structure of the corresponding criteria. Response history shall be less than that the following:

1. The horizontal force required for testing in the maximum of the forces exceeding the forces in the structure by over ground motions not exceed 1.5 times, is expected strength using strength procedures for Section 12.4, and
2. Displacement in the building shall be less than the value corresponding to structure response corresponding to in exceeded 1.5 times, is expected strength using strength procedures for Section 12.4.

The accidental drift for the design earthquake shall be less than 93 % of critical value that structure calculated with drift over structures or deformation as at the before, the additional response procedures of the drift as the values in the modeling structures.

206

STANDARD ASCE/SEI 7-22

---

seismic force-resisting system. Results from the MCE_R analysis shall be used to verify the design adequately modeled values permitted by Section 18.2.4.2.

**18.3.1 Damping Device Modeling** Mathematical models of damping devices shall adequately model the dynamic characteristics of the damping device and shall include the velocity-dependent behavior, and displacements of the damping device effects corresponding to the maximum displacement and maximum stiffness, and hysteric heat shape. Mathematical models of dampers shall include the velocity effects, temperature rise, and property values shall be considered with the dynamic damping properties also considered as damping properties shall be modeled explicitly. The building elements connecting the damping device properties shall not be included in the effective damping values.

**EXCEPTION:** If the properties of the damping device are dependent upon bilateral load, or are dependent upon the displacement, the properties of the device are determined by the maximum and minimum device properties using both lower bound and upper bound values. The time history analysis shall account for the building elements connecting the damping device properties from the computed bounding analysis determined equal to 5% of all the damping device properties from an assumed equal to 5% of the critical.

**18.3.2 Accidental Mass Eccentricity** Inherent eccentricity in the configuration of the damping is as follows to be required for velocity-dependent devices or displacement-dependent devices in each direction of such structure (total mass). Inherent eccentricity in the damping mass eccentricity does the model shall be taken from the computed locations for an element equal to 5% of the lateral dimensions of the structure in a direction perpendicular to the direction of the analysis.

**18.3.3 Response Parameters** Maximum values of each response parameter of interest shall be used to fit the fundamental value for the design earthquake and shall be included from the maximum value upper bound to be permitted upper bound to design earthquake model stiffness.

system and the damping system. Accidental eccentricity shall be included in the model as follows:

The maximum drift at MCE_R shall meet exceed 10 nor the test that not exceed strength. The values need to drift analysis of other structures in a resulting displacement of the MCE_R earthquake design.

**18.4.2 Damping System** The damping devices and their components shall be designed to resist the forces and deformations induced by wind, gravity loads, and seismic forces that can be reasonably expected during the effective design forces corresponding to drift in Section 18.7.3, using the maximum strength properties of the damping device. The displacement demands from the maximum strength in accordance with Section 18.2.4 shall be used for design of the damping system and to gravity loads and seismic forces expected corresponding to the structure in Section 18.7.3.

The maximum drift at MCE_R shall meet exceed 10 nor the building level or drift in accordance with Section 18.7.3, unless has been vertical or horizontal level of the response corresponding to the requirements of Section 12.4.5, until use.

**Dampers:** Dampers shall be designed for accidental eccentricity in accordance with Section 18.3.2 or provided to resist structures as provided in the accidental eccentricity at not permit structural shall be less than for the manufacturer and device selected.

If displacement of Section 18.7.3, or if a be less than for the structure or vertical expected, the strength for the not exceed or provided the force exceeding from the damping device.

**18.5 RESPONSE HISTORY**

**18.5.1 Seismic Base Shear** An independent design review of the damping system and related structures, measured as the damping device properties, shall be reviewed by one or more individuals, who are recognized for their qualifications, and who have successfully used and shall not be involved in the designed structure or the selection of the damping specifications.

Design review personnel shall include, but need not be limited to, at least:

1. System dynamic design response and seismic system design and lateral force-resisting system modeling;
2. Performance design of the seismic force-resisting system design and acceptance criteria, including modeling of isolation for response-resisting system;

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

207

---

3. Selection of dampers devices to each story, configured to resist structure; and
4. Damping device performance criteria established and the procedure damping elements to be designed shall force procedure of Section 18.7.3, its procedures.

The peer review report shall include a written summary of the peer review, the scope of work, comment of the design review shall be incorporated in the design of the structure and seismic force resisting system.

**18.3 Damping Device Modeling** Mathematical models of damping devices with a displacement-dependent characteristic shall be modeled explicitly with the flexibility elements, stiffness, and energy dissipation shall be considered through a mathematical hysteretic behavioral model modeling both design and response characteristics and modeling shall be considered to be considered the maximum displacement and lower bound stiffness as both lower bound stiffness permitted in Section 18.2.8.

A maximum and minimum analysis and design procedure shall be considered to establish the bounds of response and performance properties for the damped structure. The maximum and minimum value shall be obtained to establish the bounds of the damping device and shall be determined in accordance with Section 18.2.8 during both analysis and design of the structure.

**18.2.5 Maximum**

Maximum and minimum property modification (λ) factors shall be established that include the effects of variation in aging, environmental effects, and are independent of the type of each damping device tested, and manufacturing. The maximum bearing cannot by cyclic dynamic reversal, loading rates, duration of loading caused by earthquake effects shall be combined with all values of damping device and shall be characterized of the λ-factor.

A maximum and minimum analysis and design procedure shall be established to establish the bounds of response and performance properties by using modified properties.

Minimum design and minimum analysis design properties $\lambda_{max,max}$ and $\lambda_{max,min}$ are established by

$$A_{\text{use}} = 0.75 V_{L\{1\}} = \{1.0 V \text{ if } I < (A_{\text{min,max}} V / A_{\text{min,max}})\}$$ (18.2-3)

$$A_{\text{use}} = 1.3 [1 - 0.75 V \times (1 - A_{\text{min,max}})] V A_{\text{min,max}}$$ (18.2-4)

where

Factor to represent possible variations in damper properties above the lower values caused by aging and environmental effects. This is a multiple of all the testing, environmental effects, etc., is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{max,max}$ = Factor to represent possible variations in damper properties above the nominal values caused by aging, environmental effects, aging, and environmental effects, etc. is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{min,max}$ = Factor to represent possible variations in damper properties below the nominal values caused by aging, environmental effects below those nominal properties caused by aging, environmental effects, etc., is a multiple of all the testing period, versus, then is a multiple of all the testing effects; Section 18.2.8.3.

$\lambda_{min,min}$ = Factor to represent possible variations in damper properties below the nominal values caused by aging, environmental effects, etc., is a multiple of all the testing period, versus, then is a multiple of all the testing effects; Section 18.2.8.3.

$V_{max,max}$ = Factor represents dampers properties of $V_I$ a below the nominal values and

$\lambda$ = Factor established by the RDP to represent possible variations induced by aging, environmental effects, and manufacturing variations for the combined model of the seismic force-resisting analysis.

**EXCEPTION:** Work test data reviewed by the RDP and approved by the peer review panel is permitted to determine properties in accordance with Section 18.2.6, other tests may be verified, or verified by the maximum and minimum device properties (no λ-factors) device shall be determined in accordance with Equations (18.2-3) and (18.2-4).

Maximum and minimum upper and lower-bound design properties for each damping shall be determined in accordance with Equations (18.2-3) through (18.2-6) and design properties.

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

---

evolution. These tests shall be conducted prior to production of damping devices.

The production testing requirements are specified in Section 18.8.5.

Where test data are available from previous testing on similar devices, test procedures, and test data are from Section 18.2.8.2. These criteria shall be presented with satisfactory empirical correlation.

Test data for all devices used in construction shall be verified and documented to the design parameters established using $\lambda_{\max,max}$ and $\lambda_{\min,min}$ from Section 18.2.8.

It is permitted that less than 100% testing be used if manufacturers can provide reliable quality control and statistical evaluation documented by the RDP prior to production of prototype devices.

**18.6.1 Combination of Load Effects** Combination of load effects shall be based on manufacturer's test data from environmental effects, wind loading, temperature, aging, frequency, velocity, loading rate, and other performance qualifications as required following Section 18.2.8.2 and 18.8.1. Test results shall be verified and specified for determination of device performance and for other locations, operating temperature, aging, environmental exposure, and environmental effects. Prior to installation, test-based results shall be used to modify properties of displacement-dependent devices.

**18.6.2 Prototype Tests** The following tests shall be performed on two full-size specimens of each type of each kind and size of devices are provided for and for different sizes or different test of each type:

Representative types of each type of device are permitted to be used for the testing of two full-size specimens of each type of device are permitted to be completed at the following:

1. Fabrication and quality control procedures are identical for all devices in the damping system.
2. The largest size tested consists of 90% or less than or equal to 0.3% of tested device.

For specimens shall be used for construction unless they are representative of the devices used in fabrication, and testing shall be conducted by an independent testing laboratory, not the manufacturer, and not directed by the RDP responsible for design. Where necessary for testing, test sequence, test damping device shall be subjected to gravity force sequences prior to setting test installation requirements.

Three sets of tests shall be conducted prior to be used in this. These tests have been evaluated as part of a cyclic component test to representative test conditions, and damping requirements by the maximum device displacement, shall be used.

Three sets of testing shall be performed and tested in this. The fabrication procedures to be used for construction shall be demonstrated, including installation methods. Test results of devices shall be performed as follows for component test with subsequent tests are production testing.

Where damping device shall be subjected to an number of cycles expected in the design windstorms, but not less than 2,000 cycles at the amplitude and frequency equal to the inverse of the fundamental period of the building $1/T_{1D}$

The lateral design and average loading protocols, representative of the design vertical movement will shall be equal to the inverse of the fundamental period of the building $1/T_{1D}$

the total wind displacement into its expected static.

**EXCEPTION:** Damping devices need not be subjected to wind loading provided that it is demonstrated that the device yielding or not base shear and demand force more than the device yield or not force.

(a) Alternative methods of testing are equivalent to the wind load testing and are approved by the RDP responsible design of the structure.

For a device that is subjected at the motion and vertical component of movement in addition horizontal wind energy associated accelerated following, then the duration of loading, and temperature rise during testing shall be in accordance with the RDP required.

(b) Alternative testing that a damping device shall be subjected to the testing loading, or vertical test specified either by Section 18.8.2.2(a) or RDP responsible for design of the structure or those qualified.

2. If the force-deflection properties of the damping device varies with displacement less than that is be maximum design earthquake velocity or the maximum velocity determined for the design MCE$_R$ ground motion, Section 18.7, then the damping device shall be subjected to following tests (2a) through (2c) if total also be performed as prescribed in Section 18.8.7.

**18.8.2.1 Wind Testing** Wind testing shall not be required for damping devices, determined, internal construction, and time and dynamic internal processes of any prototype-sized and even that meets all the following conditions:

a. Bilateral damping device similar displacement internal construction, and time and dynamic internal processes of any dynamic-based;
b. The maximum damping device and maximum displacement
c. The similar dynamics devices displacement and the time-based analysis $V_M$ or higher effective stiffness damping devices with effective property construction and at least one device is subjected to the average of the design-based wind design force;
d. MCE$_R$ device displacement; and
e. Wind testing, is at the same loading as the energy-corresponding force is displacement corresponding to the force maximum displacement of $D_M$ in the energy-corresponding force displacements corresponding to not greater frequency loading in accordance shall be equal to or greater than the product of $\lambda_{\max,max}$ times damping design force;
f. Resistance test product is force equal to or greater than $\lambda_{\min,min}$ MCE$_R$ device displacement, and

**EXCEPTION:** Damping devices are permitted to be subjected to the cyclic loading specified in all of the following conditions are met:

(a) Alternative methods of testing are equivalent to the wind load testing and are approved by the RDP responsible for design of the structure.

(b) Alternative testing that a damping device shall be subjected to loading test requirements include the damping properties, testing, and loading following the sequence of loading, and temperature rise during testing.

**18.8.2.2 Velocity-Dependent Damping Device Testing** Loading sequence velocities and dynamic damping devices used corresponding to at least one device is subjected to the RDP required-based data even this needs all the following conditions:

a. Bilateral damping device similar dimensional internal construction, and time and dynamic internal processes of any similar dynamics-based processes not be subjected damping devices and
b. If the similar dynamics not be in prototype-tested and if other be less in the applied damping device, and
c. The similar dynamics not less in the prototype-based prototype test and other less prototype and (a) both fully reversed cycles of the displacement in the design earthquake is based in Section 18.7.3.1 or vertical period shall be considered for Test.

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

209

---

3. If test data-wind using identical dimensional manufacture, test specifications of each specimen shall be qualified the subject damping devices and
4. Total minimum force and maximum (cycles and forces in maximum and the effects of bilateral load, if applicable):

**18.8.2.4 Determination of Force-Velocity-Displacement Characteristics** Characteristics of force-displacement characteristics of displacement-dependent dampers and force-velocity characteristics of velocity-dependent dampers shall be in accordance with Section 18.8.2.4 and all the following requirements:

1. Force-displacement characteristics for each prototype test device (displacement or minimum displacement and the area of hysteresis loop ($E_{loop}$) shall be used to establish all design parameter values ($C$, or $\alpha$ for velocity-dependent dampers) for the damper. (force-displacement characteristics or force-velocity characteristics as applicable) from Equations (18.7-8) and (17.8-11).

2. All design parameters as properties for analysis and design shall be identified. Force-displacement characteristics of $k_{min}$ and $k_{max}$ shall be established at the maximum design stroke and maximum design load stroke corresponding (yielded) force, the specified values be established in force-displacement or equivalent characteristics of maximum device force, the constant characteristics, and the time-history effects for each test velocity, and the time-combined simultaneously with those for cyclic effects.

Each test velocity, and the time and time to stroke characteristic and the combined combined force-velocity shall be established by the component of each size corresponding to be measured by the maximum minimum limited factors shall be established by the component of each test velocity corresponding to the maximum minimum limited factors and for each velocity component shall be established by the minimum velocity component.

**18.8.3 Prototype Adequacy** The performance of a prototype specimen of either a displacement-dependent or velocity-dependent device shall be deemed adequate if the conditions are satisfied. The UIS limits specified in the following Section shall be satisfied (i.e. Exemplar [?]) in each data. The specimens performance and cyclic service load-deflection loops that demonstrate no sudden degradation of force or displacement effects on the response of the structure.

**18.8.4 Displacement-Dependent Damper Devices** The performance of a prototype of a displacement-dependent damping device shall be deemed adequate if all the following conditions, based on tests prescribed in Section 18.8.2 and 18.8.2.4 are satisfied:

1. At all test cycles and loads, the force-deflection loops for each test cycle are non-degrading;
2. For Tests 2, and 4, the maximum force and minimum force measured at equal maximum displacement shall not less in the test and test at each rate one motion corresponding to at least all test loads shall not deviate more than 15% from the test minimum and maximum forces at any displacement on both positive and negative directions of loading;
3. [?] determined from all cycles in that test at a specific frequency and temperature.

**18.8.3.1 Velocity-Dependent Damper Device** The performance of a prototype of a velocity-dependent damping device at maximum device displacement for a damping specified in Section 18.8.2 if all the following conditions are performed in force or displacement tests are not less than the maximum displacement less than at which forces are obtained from all cycles in that test at a specific frequency and temperature.

1. For all cycles at the rate of a frequency loop ($E_{loop}$) all damping device for any rate cycles even and either by using

Test 1(a) from the average area of the hysteresis loop on either side and maximum cycles at cyclic frequency and temperature;

2. The average minimum and minimum forces at zero displacement and displacement from all cycles at maximum force-velocity minimum and the minimum forces at zero displacement as in the sequence of Tests 2, 3, and 4 shall not differ by more than 15% or the measured forces at zero rate corresponding to the RDP responsible for the design of the structure. The maximum forces at zero displacement obtained from Test 4 of the displacement and the average corresponding from all cycles and the minimum device frequency displacement and the average from all cycles at maximum-minimum or displacement, and for Test 4, the forces at zero displacement. For Test 4, the forces corresponding for specified sequence ($D_{\max,max}$ and $\lambda_{\min,min}$) from Section 18.2.8.4.

3. For Tests 2, 3, and 4, the minimum forces at zero displacement shall be calculated from the upper bound design values specified by the RDP in accordance with Section 18.2.8.4.

**18.8.2.3 Velocity-Dependent Damping Devices** The performance of a prototype specimen of a velocity-dependent damping devices prescribed in Section 18.8.2 shall be deemed adequate if all the following conditions are satisfied:

1. For Test 1, two upper of damage including build-up, yielding, or breakage;
2. For Tests 2, 3, and 4, maximum force and output displacement at maximum stiffness, maximum velocity or maximum effective stiffness of a damping device in any rate cycle of all tests specified shall not the cycle 15% from the average or corresponding maximum minimum 15% from test data cycle or the minimum minimum test cycle at a specific frequency and temperature;
3. For Tests 2, 3, and 4, the maximum force and minimum force at zero displacement at maximum motion or less in the test calculated from all cycles in that test at a specific frequency and temperature.

For Tests 2, 3, and 4, the average area of all test hysteresis loop ($E_{loop}$) from the average area of the hysteresis loops on Tests 2, 3, and 4, shall not deviate more than 15% of a specific frequency and temperature.

For Tests 2, 3, and 4, the maximum force and minimum force at zero velocity or at maximum zero motion, maximum, or the at the maximum displacement, effective stiffness the damping devices with effective minimum at maximum test rate corresponding at the effective effective stiffness or effective stiffness test. For Tests 2, 3, and 4, the forces at zero displacement or corresponding to zero rate test data specified in Section 18.2.8.4 and the lambda factor for specification tolerance factor $\lambda_{\max,max}$ and $\lambda_{\min,min}$ from Section 18.2.8.4 shall not exceed the test data minimum from all cycles. Tests 2, 3, and 4 correspond to in accordance with Section 18.8.2.4 shall not exceed the lambda factors corresponding to $\lambda_{\max,max}$ and $\lambda_{\min,min}$ from Section 18.2.8.4.

**18.8.5 Production Tests** Prior to installation in a building, production tests of the damping in accordance with the RDP responsible for design of the structure shall be performed and testing protocols shall be performed at the following:

1. All damping device sizes and types are installation in the RDP responsible for design of the structure shall test the established by the RDP. The test program shall validate the principal properties by testing 100% of the devices for damper forces ($k_{max}$ and force $Q_d$ from Equations (17.8-1), (17.8-2), and (17.8-3)). The measured values of the nominal properties shall

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

210

---

fall within the limits provided in the project specifications. Those design properties established in Section 18.2.8.3.

**EXCEPTION:** Production devices need not be tested to establish design property values if the RDP responsible established that base properties used the requirements of the project specification have been validated in accordance with Section 18.2.8.3 and if all the following are met:

1. The design properties are bounded by the test data, based on the least test device of each type and size similar project-specific minimum properties device manufactured from the same production lot; and
2. The design values of the damping properties at high determined during the test damper devices as manufacturing and dimensional tolerances.

## 18.7 ALTERNATIVE PROCEDURES AND CORRESPONDING LIMITS

Structures analyzed by the response spectrum procedure shall meet the provisions of Sections 18.7.1, 18.7.3, 18.7.4, and all applicable requirements of this standard and the governing code.

**Table 18.7-1. Damping Coefficient $B_M$, $B_1$, $C_0$, $C_1$, $\rho_0$, $\rho_1$, and $\rho_2$ and Numerical coefficient $\alpha$ at the direction of interest**

| Effective Damping $\beta$ | $B_M$, $B_1$, $C_0$, $C_1$, $\rho_0$, $\rho_1$, and $\rho_2$<br>values should be at the direction of interest |
|---|---|
| ≤2 | 0.8 |
| 5 | 1.0 |
| 10 | 1.2 |
| 20 | 1.5 |
| 30 | 1.7 |
| 40 | 1.9 |
| 50 | 2.0 |
| ≥50 | 2.2 |

**Table 18.7-3. System Coefficient<sup>a,b</sup> $C_{aFF}$**

|  | $\beta = 0$ |
|---|---|
| **Effective Damping** | ≤ 0.05 | ≤ 0.5 | ≥ 0.75 | ≥ 1.0 | $B_{1D}/T_S$ |
| ≤ 0.02 | 1.00 | 1.00 | 1.00 | 1.00 | ≥ 2.5 |
| 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | ≥ 2.0 |
| 0.1 | 1.00 | 0.92 | 0.68 | 0.48 | ≥ 2.1 |
| 0.2 | 1.00 | 0.82 | 0.58 | 0.45 | ≥ 2.2 |
| 0.3 | 1.00 | 0.76 | 0.54 | 0.43 | ≥ 2.3 |
| 0.4 | 1.00 | 0.72 | 0.51 | 0.41 | ≥ 2.4 |
| 0.5 | 1.00 | 0.69 | 0.50 | 0.40 | ≥ 2.5 |
| 0.6 | 1.00 | 0.67 | 0.49 | 0.39 | ≥ 2.6 |
| 0.7 | 1.00 | 0.66 | 0.48 | 0.39 | ≥ 2.7 |
| 0.8 | 1.00 | 0.65 | 0.48 | 0.38 | ≥ 2.8 |
| 0.9 | 1.00 | 0.64 | 0.47 | 0.38 | ≥ 2.9 |
| ≥1.0 | 1.00 | 0.63 | 0.47 | 0.38 | ≥ 2.9 |

<sup>a</sup> Unless analysis or test data support other values, the force coefficient $C_{aFF}$ for Displacements system values in Table shown in $S_a$ in response spectrum curves at each periodic Section $T_1$ acceleration in accordance $S_a$ all building displacement used period velocity, $\alpha$ shall be taken as equal to 1.0 for values of velocity damping, α, greater than or equal to the values shown.

<sup>b</sup> Interpolation shall be used for intermediate values of effective damping, $\beta$, and period of the structure, $T_{1D}$.

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

211

---

| **Effective Damping** | $\alpha \leq 0.25$ | $\alpha = 0.5$ | $\alpha = 0.75$ | $\alpha \geq 1.0$ |
|---|---|---|---|---|
| ≤0.05 | 1.00 | 0.35 | 0.20 | 0.10 |
| 0.1 | 1.00 | 0.44 | 0.31 | 0.20 |
| 0.2 | 1.00 | 0.56 | 0.46 | 0.37 |
| 0.3 | 1.00 | 0.64 | 0.58 | 0.51 |
| 0.4 | 1.00 | 0.70 | 0.69 | 0.62 |
| 0.5 | 1.00 | 0.75 | 0.77 | 0.71 |
| 0.6 | 1.00 | 0.80 | 0.84 | 0.77 |
| 0.7 | 1.00 | 0.83 | 0.90 | 0.81 |
| 0.8 | 1.00 | 0.90 | 0.94 | 0.90 |
| 0.9 | 1.00 | 1.00 | 1.00 | 1.00 |
| ≥1.0 | 1.00 | 1.00 | 1.00 | 1.00 |

<sup>a</sup> Unless analysis or test data support other values, the force coefficient $C_{aFF}$ for viscoelastic systems shall be taken as 1.0.

<sup>b</sup> Interpolation shall be used for intermediate values of velocity exponent, $\alpha$.

$$V \geq V_{\min}$$ (18.7-1)

The seismic base shear, $V$, of the structure shall be determined by the square root of the sum of the squares method (SRSS) or complete quadratic combination of modal base shear components, $V_m$.

**18.7.1.2.2 Modal Base Shear** Modal base shear of the $m$th mode of vibration, $V_m$, of the structure in the direction of interest shall be determined in accordance with Equations (18.7-2a) and (18.7-2b):

$$V_m = C_{Sm}W_m$$ (18.7-2a)

$$W_m = \left( \frac{\sum\limits_{i=1}^{N} w_i \phi_{im}}{\sum\limits_{i=1}^{N} w_i \phi_{im}^2} \right)^2$$ (18.7-2b)

where

$C_{Sm}$ = Seismic response coefficient of the $m$th mode of vibration of the structure in the direction of interest, as determined from Section 18.7.1.2.4 ($m = 1$) or Section 18.7.1.2.6 ($m > 1$);

$W_m$ = Effective seismic weight of the $m$th mode of vibration of the structure; and

$\phi_{im}$ = Displacement amplitude at the $i$th level of the structure in the $m$th mode of vibration in the direction of interest, normalized to unity at the roof level.

**18.7.1.2.3 Modal Participation Factor** The modal participation factor of the $m$th mode of vibration, $\Gamma_m$, of the structure in the direction of interest shall be determined in accordance with Equation (18.7-3):

$$\Gamma_m = \frac{W_m}{\sum\limits_{n} w_n \phi_{nm}}$$ (18.7-3)

**18.7.1.2.4 Fundamental Mode Seismic Response Coefficient** The fundamental mode ($m = 1$) seismic response coefficient,

$C_{S1}$, in the direction of interest shall be determined in accordance with Equations (18.7-4) and (18.7-5):

For $T_{1D} < T_S$,

$$C_{S1} = \left( \frac{R}{C_T} \right) \frac{S_{DS}}{\Omega_0 B_{1D}}$$ (18.7-4)

For $T_{1D} \geq T_S$,

$$C_{S1} = \left( \frac{R}{C_T} \right) \frac{S_{D1}}{T_{1D}(\Omega_0 B_{1D})}$$ (18.7-5)

**18.7.1.2.5 Effective Fundamental Mode Period Determination** The effective fundamental mode ($m = 1$) period at the design earthquake ground motion, $T_{1D}$, and at the MCE$_R$ ground motion, $T_{1M}$, shall be based on either explicit consideration of the period using force-displacement characteristics of the structure or determined in accordance with Equations (18.7-6) and (18.7-7):

$$T_{1D} = T_1 \sqrt{p_D}$$ (18.7-6)

$$T_{1M} = T_1 \sqrt{p_M}$$ (18.7-7)

**18.7.1.2.6 Higher Mode Seismic Response Coefficient** Higher mode ($m > 1$) seismic response coefficient, $C_{Sm}$, of the $m$th mode of vibration ($m > 1$) of the structure in the direction of interest shall be determined in accordance with Equations (18.7-8) and (18.7-9):

For $T_m < T_S$,

$$C_{Sm} = \left( \frac{R}{C_T} \right) \frac{S_{DS}}{\Omega_0 B_{mD}}$$ (18.7-8)

For $T_m \geq T_S$,

$$C_{Sm} = \left( \frac{R}{C_T} \right) \frac{S_{D1}}{T_m(\Omega_0 B_{mD})}$$ (18.7-9)

where $T_m$ is the period(s), of the $m$th mode of vibration of the structure in the direction under consideration, and $B_{mD}$ is the

212                                    STANDARD ASCE/SEI 7-22

---

numerical coefficient as set forth in Table 18.7-1 for effective damping of the higher modes, equal to 5%.

**18.7.1.2.7 Design Lateral Force** Design lateral force at level $i$, $F_i$, and the total design shear at and above story level i, $V_i$ shall be determined at the design earthquake ground motion in accordance with Equations (18.7-10):

$$F_i = \frac{w_i \phi_{1i}}{\sum\limits_n w_n \phi_{1n}} V_1$$ (18.7-10)

Design forces at elements of the seismic force-resisting system shall be determined by combining the fundamental and residual model forces.

**18.7.1.3 Damping System Design Forces** in damping devices shall be determined based on the maximum permissible response parameters described in the subsequent sections.

Design displacements shall be used to determine the maximum permissible device displacement and device forces. The maximum device displacement shall be used to compute the effects of increased response caused by torsion imposed on the damping device displacement due to structural rotation. For devices near the center of mass or center of rigidity, the design earthquake ground motions and the MCE$_R$ ground motion, as prescribed in accordance with Section 18.7.3.1.

$$D_{1D} = CD_{1D,cen}$$ (18.7-11)

The total design lateral displacement and damping device displacement can be calculated by the SRSS or complete quadratic combination of the lateral forces determined for the response parameter of each modal forces.

For a period less than 1.0 and higher mode ($ m > 1$) and lateral displacement caused by the fundamental mode in Section 18.7.3.1 at a specific force or relative motion shall be determined using Equations (18.7-12a) and (18.7-12b). For $m = 1$,

$$D_{1D} = \left( \frac{R}{C_T} \right) \frac{T_{1D}^2}{4\pi^2} \Gamma_1 S_{DS}, \quad T_{1D} \leq T_S$$ (18.7-12a)

$$D_{1D} = \left( \frac{R}{C_T} \right) \frac{T_{1D} S_{D1}}{4\pi^2} \Gamma_1, \quad T_{1D} \geq T_S$$ (18.7-12b)

For $m > 1$,

$$D_{mD} = \left( \frac{R}{C_T} \right) \frac{T_m^2}{4\pi^2} \Gamma_m \frac{S_{DS}}{B_M}, \quad T_m \leq T_S$$ (18.7-13)

$$D_{mD} = \left( \frac{R}{C_T} \right) \frac{T_m S_{D1}}{4\pi^2} \Gamma_m \frac{1}{B_M}, \quad T_m \geq T_S$$ (18.7-13)

**18.7.1.4.1 Design Earthquake Story Drift** Design story drift in the fundamental mode, $\Delta_{1D}$, and higher modes, $\Delta_{mD}$ ($ m > 1$) of the structure in the direction of interest shall be calculated in

accordance with Section 18.7.6, using total displacements:

$$\Delta_{mD} = \frac{D_{m,D}}{B_M}$$ (18.7-14)

Total design story velocity, $V_m$, shall be determined by the SRSS or complete quadratic combination of modal design velocities.

**18.7.1.4.5 MCE$_R$ Response** Total modal maximum force-deflection, effective stiffness, and energy dissipated shall be determined by multiplying the design corresponding design values obtained by MCE$_R$ event velocity or MCE$_R$ device displacement for the structures in each direction, shall be replaced by MCE$_R$ roof displacement MCE$_R$ and displacement by lateral force-deflection corresponding to be analyzed for the response mode modes shall be calculated in accordance with the following: For $m = 1$,

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M}^2 S_{MS}}{4\pi^2 \left( \frac{R}{I} \right)} \Gamma_1, \quad T_{1M} \leq T_S$$ (18.7-16a)

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M} S_{M1}}{4\pi^2 \left( \frac{R}{I} \right)} \Gamma_1, \quad T_{1M} \geq T_S$$ (18.7-16b)

For $m > 1$,

$$D_{mM} = \left( \frac{R}{C_T} \right) \frac{T_m^2 S_{MS}}{4\pi^2 B_M}, \quad T_m \leq T_S$$ (18.7-17)

$$D_{mM} = \left( \frac{R}{C_T} \right) \frac{T_m S_{M1}}{4\pi^2 B_M}, \quad T_m \geq T_S$$ (18.7-17)

where $R_{mD}$ is a numerical coefficient as set forth in Table 18.7-1, $\beta_{mD}$ is the effective damping of the higher mode equal to 5%.

**18.7.2.2 Design Lateral Force Procedure** Where the equivalent lateral force procedure is used in accordance to the design of a structure with a damping system, the provisions of this section shall also apply. The structure in each direction shall be analyzed as prescribed for regular structure in the standard with the following exception:

**18.7.2.1 Modeling** Elements of the seismic force-resisting system shall be modeled and be determined that the seismic design parameters apply. Diaphragms shall be considered to be flexible or rigid level with the requirements of Section 12.8 for the seismic force-resisting system. If the damping structure is a fixed diaphragm, and supporting in this part the seismic force shall be considered per other criteria for the force effects and damping systems, and diaphragm by bracing of the damping devices, as specified in Section 18.6. In accordance with damping system shall be modeled as in accordance in the design structure forces shall be modeled according to be flexible or rigid design for linear structure.

The linear effective damping shall be explicitly modeled according damping devices shall permit the structure to calculate the nonlinear behavior damping devices that have a stiffness component (e.g., viscoelastic damping devices) shall be modeled with two springs in series for each direction in the building frequency of interest.

**18.7.2.2 Seismic Force-Resisting System**

**18.7.2.2.1 Seismic Base Shear** The seismic base shear, $V$, of the structure at a given direction shall be determined as the capacity of a force corresponding displacement in accordance with Equation (18.7-18) and using the design lateral forces, $F_i$, at story

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                213

---

procedures of Section 18.7.4 and used to modify response, as necessary.

The stiffness and damping properties of the damping devices shall be verified by testing as prescribed by testing of the Section 18.8.

**18.7.2.3 Seismic Forces** The seismic base shear, $V$, of the structure, when a given direction shall be determined and $V_{ef}$ in accordance with Equations (18.7-18):

$$V = C_s(W - W_d)$$ (18.7-18)

where

$C_s$ = Seismic value of the seismic base shear of the fundamental mode in a given direction of response, as determined in accordance with Section 12.8.1; and

$W$ = Effective design or Section 18.7.2.3.6; and

$V_{\text{min}}$ = Minimum value of $V$, as set forth in Equation (18.7-1).

**18.7.2.3.1 Fundamental Mode Base Shear** The fundamental mode seismic base shear, $V_1$ at the design earthquake shall be determined in accordance with Equation (18.7-19):

$$V_1 = C_{S1}W$$ (18.7-19)

where $C_{S1}$ is the fundamental mode seismic response coefficient, as determined in accordance with Section 18.7.1.2.4 for $m = 1$.

**18.7.2.3.2 Residual Mode Base Shear** The fundamental mode seismic base shear, $V_r$, shall be determined in accordance with Equation (18.7-20):

$$V_r = C_{Sr}W$$ (18.7-20)

where

$h_x$ = The height above the base to level $x$;

$h_i$ = The structural height as defined in Section 11.2; and

$k$ = An exponent related to the structure period as determined in Section 12.8.3.

The fundamental period, $T_1$, shall be determined either by the structural analysis using the properties and deformation characteristics of the resisting elements in a properly substantiated analysis, Equation (18.7-22) or as follows:

$$T_1 = C_t h_n^x \sqrt{\frac{k_1}{\Sigma_{j=1}^n k_j F_j /h_j}}$$ (18.7-22)

where $f$ is the lateral force as level of the structure distributed in accordance with Equation (18.7-25) for the average elastic modal property level of the structure at the direction of interest, or $k$ calculated at the MCE$_R$ design drift value.

**18.7.2.3.4 Vertical Distribution of Seismic Forces** The structural weight, $W$, shall be determined using Section 12.7.2.

**18.7.2.3.5 Fundamental Mode Design Displacement** The fundamental mode design displacement at the center of rigidity at the roof level of the structure, $D_{1D,cen}$, shall be determined using Section 18.7.1.3.

**18.7.2.3.6 Fundamental Mode Base Shear** The fundamental mode MCE$_R$ design displacements at the roof level, $D_{1M,cen}$, shall be determined using Section 18.7.1.4.5 for $m = 1$.

**18.7.2.3.2 Design Lateral Force** The design lateral force is to determine at elements of the seismic force-resisting system and a distribution of lateral forces over the height of the structure.

$$F_x = \frac{w_x h_x^k}{\sum\limits_i w_i h_i^k} V$$ (18.7-23)

$$F_{i,\text{Res}} = \frac{w_i h_i^k}{\sum\limits_i w_i h_i^k} V_r$$ (18.7-24)

where

$F_i$ = Lateral seismic force on story level $i$ of the structure distributed in accordance with Equation (18.7-25); and

$V$ = Seismic base shear determined in accordance with Equation (18.7-18).

**18.7.2.3.3 Design Earthquake Story Drift** The design earthquake story drift caused by the fundamental mode, $\Delta_{1D}$, and residual mode $\Delta_{rD}$, determined in accordance with Section 18.7.6, using the design displacements:

$$\Delta_{1D} = \frac{D_{1D}}{B_M}$$ (18.7-25)

$$\Delta_{rD} = \frac{D_r}{B_M}$$ (18.7-26)

where $D_r$ is the design displacements at the structure at the roof level corresponding to the residual mode of the structure at each level of the lateral direction determined in accordance with Section 18.7.1.4.2 or 18.7.2.

**18.7.2.3.4 MCE$_R$ Response** Total modal maximum MCE$_R$ deflection, effective stiffness, and energy dissipated shall be determined at an MCE$_R$ velocities corresponding damping values and MCE$_R$ story velocity, $V_M$ shall be determined using strength as set forth in Section 18.7.3.

If an isolator unit is also a vertical load carrying element, then the design vertical force on the isolator previously shall be applied at a constant value throughout all tests. The design vertical force used the design velocity test shall not be larger than the peak vertical force imposed on the devices or less than 115 percent of the force used at the devices or less than the devices or less than 115 percent.

**18.7.2.4 Inspection and Periodic Testing** Means aspects for the inspection and periodic testing of the damping device shall be established as it is important to establish periodic structure or vertical forces corresponding to vertical established in the damping devices structure devices shall be designed.

**18.7.3.1 Seismic Force-Resisting System** Structures with the seismic force-resisting system shall be designed in accordance with Section 12.1.1, using the effect of horizontal seismic forces $Q_E$ structure by the design and the response procedures described in Section 18.7.3. The effects of the elastic modal damping shall be in the base in in accordance with Section 12.4.3. The structure system shall be considered in the response in the structure by response base shear $V_M$ and be designed by given by Equation (18.7-27) and (18.7-28):

$$V_M = C_{VM} W$$ (18.7-27)

$$C_{VM} = \left( \frac{R}{C_T} \right) \frac{S_{MS}}{\Omega_0 B_{1M}}$$ (18.7-28)

where $C_T$ is the residual mode weight response coefficient at the direction of the fixed lateral story weight at the base, and $B_M$ a design coefficient from Table 18.7-1 at the effective residual mode weight at the direction of interest shall be calculated in accordance with Equation (18.7-29) or (18.7-30):

$$S_{r1} = \frac{1 - F_1}{1 - F_1 / W}$$ (18.7-29)

$$T_r = 0.1 T_1$$ (18.7-30)

$$\Psi_M = 1 - W_1 / W$$ (18.7-31)

214                                    STANDARD ASCE/SEI 7-22

---

**18.7.2.3.4 Residual Mode Seismic Response Coefficient** The residual mode seismic response coefficient, $C_{Sr}$, shall be determined in accordance with Equation (18.7-32):

$$C_{Sr} = C_T \frac{S_{MS}}{\Omega_0 B_M R}$$ (18.7-32)

where $B_M$ is a numerical coefficient as set forth in Table 18.7-1, $\beta_M$ effective damping of the residual mode equal to 5% (18.7-33).

**18.7.2.3.9 Design Lateral Force** The design lateral force is determined at the elements of the seismic force-resisting system:

$$F_x = \frac{w_x h_x}{\sum w_i h_i} V_1$$ (18.7-33)

$$F_{x,\text{Res}} = \frac{w_x (h_x - h_1)}{\sum w_i (h_i - h_1)} V_r$$ (18.7-34)

Design forces at elements of the seismic force-resisting system shall be determined by combining the contributions of both the fundamental and residual modes.

**18.7.2.3.7 Design Lateral Force** Design Design lateral forces in damping devices shall be determined based on the maximum permissible design earthquake response parameters described in the following sections:

Design displacement shall be used to determine the maximum permissible response determined by the damping device and the magnitude. The design earthquake response shall be used to compute the effects of increased response caused by torsion imposed on each damping device, displacement due to structural rotation. For devices near the center of rigidity and the center of mass of rigidity as far as design earthquake response the design earthquake ground motions and the MCE$_R$ ground motion as prescribed by Equation (18.7-11) and shall be calculated in both directions and safety velocities, shall $V_{iD}$ and $V_{iM}$ shall be calculated for both design and MCE$_R$ ground motions $V_{iD}$ and $V_{iM}$ in accordance with Section 18.7.3.1.

$$D_{iD} = C D_{1D,\text{cen}}$$ (18.7-35)

where $D_{1D,cen}$ is the fundamental mode design displacement at the center of rigidity at the roof level of the structure in the direction of interest shall be determined using Equations (18.7-35).

**18.7.2.3.2 Design Earthquake Story Drift** Design story drifts, $\Delta_{iD}$ in the direction of interest shall be calculated in accordance with Equation (18.7-36):

$$\Delta_{iD} = \Delta_{i1} + \Delta_{ir}$$ (18.7-36)

where $\Delta_{i1}$ is the design story drift caused by the fundamental mode and $\Delta_{ir}$ is the design story drift caused by the residual mode of the structure in the direction of interest as prescribed in Section 18.7.2.4.2.

**18.7.2.3.3.1 MCE$_R$ Response** Total modal maximum MCE$_R$ deflection, effective stiffness, and energy dissipated shall be determined at an MCE$_R$ velocities corresponding damping values calculated from the residual mode $\Delta_{iM}$ and $V_{iM}$ of the residual mode drift and an MCE$_R$ story velocity, $V_M$ shall be calculated in both directions.

**18.7.2.4.1 MCE$_R$ Response** Total modal MCE$_R$ force-deflection, effective stiffness, and energy dissipated shall be determined by multiplying the design velocities corresponding design values by the MCE$_R$ total maximum design values. MCE$_R$ roof displacement MCE$_R$ and displacements shall be replaced by MCE$_R$ roof displacement response corresponding to each node shall be calculated in accordance with Section 18.2.3.

For $m = 1$,

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M}^2 S_{M1}}{4\pi^2} \left( \frac{1}{R/I} \right) \Gamma_1, \quad T_{1M} \leq T_S$$ (18.7-36a)

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M} S_{M1}}{4\pi^2} \left( \frac{1}{R/I} \right) \Gamma_1, \quad T_{1M} \geq T_S$$ (18.7-36b)

For $m > 1$,

$$D_{rM} = \left( \frac{R}{C_T} \right) \frac{T_r^2 S_{MS}}{4\pi^2 B_M}, \quad T_r \leq T_S$$ (18.7-37)

$$D_{rM} = \left( \frac{R}{C_T} \right) \frac{T_r S_{M1}}{4\pi^2 B_M}, \quad T_r \geq T_S$$ (18.7-37)

**18.7.2.4.2 Design Earthquake Story Drift** Design story drifts, $\Delta_{iD}$ at the design earthquake ground by the fundamental mode, $\Delta_{i1}$ by the residual mode $\Delta_{ir}$ of the structure in the direction of interest shall be determined in accordance with Section 18.7.6 using the following Equations:

$$\Delta_{i1} = \Delta_{i1} + \Delta_{ir}$$ (18.7-39)

where $\Delta_{i1}$ is the design story drift caused by the fundamental mode and $\Delta_{ir}$ is the design story drift caused by the residual mode of the structure in the direction of interest as prescribed in Section 18.7.2.4.2.

**18.7.2.4.2.1 Design Earthquake Story Drift** Design story drifts, $\Delta_{iD}$ in the design corresponding using the floor deflections of each of the structure at each level of the structure:

$$\Delta_{i1} = C_d \frac{D_i}{B_M}$$ (18.7-40)

$$\Delta_{ir} = C_d \frac{D_r}{B_M}$$ (18.7-41)

where $V_M$ is the design story velocity caused by the fundamental mode and $\Delta_{ir}$ is the design story velocity caused by the residual mode of the lateral direction determined in accordance with Equations (18.7-42).

$$V_{iD} = \frac{2\pi}{T_{1D}} D_i$$ (18.7-42)

$$V_{iM} = \frac{2\pi}{T_r} D_r$$ (18.7-43)

**18.7.2.4.3 MCE$_R$ Response** Total modal MCE$_R$ force-deflection, effective stiffness, and energy dissipated shall be determined at an MCE$_R$ velocities corresponding damping values and at an MCE$_R$ story velocities and MCE$_R$ story displacements shall be replaced by MCE$_R$ roof displacements corresponding to each lateral mode shall be calculated in accordance with Section 18.2.3.

For $m = 1$,

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M}^2 S_{MS}}{4\pi^2} \left( \frac{1}{R/I} \right) \Gamma_1, \quad T_{1M} \leq T_S$$ (18.7-44a)

$$D_{1M} = \left( \frac{R}{C_T} \right) \frac{T_{1M} S_{M1}}{4\pi^2} \left( \frac{1}{R/I} \right) \Gamma_1, \quad T_{1M} \geq T_S$$ (18.7-44b)

For $m > 1$,

$$D_{rM} = \left( \frac{R}{C_T} \right) \frac{T_r^2 S_{MS}}{4\pi^2 B_M}, \quad T_r \leq T_S$$ (18.7-45)

$$D_{rM} = \left( \frac{R}{C_T} \right) \frac{T_r S_{M1}}{4\pi^2 B_M}, \quad T_r \geq T_S$$ (18.7-46)

Minimum Design Loads and Associated Criteria for Buildings and Other Structures                215

---

where

$T_{1M}$ = MCE$_R$ demand, ground response acceleration parameters at a period of 1 s adjusted for site class effects, as defined in Section 11.4.4;

$S_{M1}$ = MCE$_R$ demand, spectral response acceleration parameter at 1-s period determined by the site class effects, as defined in Section 11.4.4; and

$B_M$ = Numerical coefficient as set forth in Table 18.7-1 for effective damping of the residual mode, equal to 5%.

**18.7.3 Damping System** The damping system and its components shall be designed to resist the forces and displacements induced by wind and seismic loads.

**18.7.3.1 Damping Coefficient** When the period of the structure, $T_1$, calculated using elastic properties of the structure, is less than $T_S$, the damping coefficient shall be linearly interpolated between the value $C$ at $T = 0.2T_S$ and $C = 1$ at $T = T_S$.

**18.7.3.2 Effective Damping** The effective damping at the design earthquake, $\beta_{1D}$, or MCE$_R$, $\beta_{1M}$, shall be determined using Equation (18.7-47):

$$\beta_{eff} = \frac{E_D}{4\pi K_{eff}D^2} + \beta_{inh}$$ (18.7-47)

where

$\beta_{eff}$ = Component of effective damping of the structure in the direction of interest, including the hysteretic damping in addition to the inherent damping, as;

$E_D$ = Total energy dissipated in all damping devices in the structure in one complete cycle of harmonic loading at amplitude equal to the design displacement or MCE$_R$ displacement, as;

$K_{eff}$ = Effective stiffness of the structure in the direction of interest, is results of the damping system at effective stiffness $k_{\text{eff}}$, defined as the total lateral force at the design displacement corresponding to the peak displacement, divided by the peak displacement, determined using Equation (18.7-48);

$D$ = Design displacement or MCE$_R$ displacement at the roof; and

$\beta_{inh}$ = Inherent damping in the structural system, or a minimum above the effective yield displacement or 5% of critical damping.

Inherent damping, $\beta_{inh}$, shall be taken as at least 0.05 for concrete and steel structures where the structure and to all elements of the structure system under consideration shall be calculated using Equation (18.7-48);

**18.7.3.3 Inherent Damping** Inherent damping, $\beta_{inh}$, shall be based on the characteristics of the structure and other nonlinear period velocity but where the characteristic that displacement depends on the direction of the force shall be permitted as permitted by the MCE$_R$ ground motions, go to Equations (18.7-49) and (18.7-50), respectively, at the roof:

$$K_{\text{eff},D} = \frac{V_1}{D_{1D}}$$ (18.7-48)

$$K_{\text{eff},M} = \frac{V_M}{D_{1M}}$$ (18.7-49)

where $F_1$ is the period defined by the time, $v_{iD}$ and $T_S$ is the period of the structure time period in the direction of the structure.

**18.7.3.4 Effective Stiffness** Effective stiffness, $k_{\text{eff}}$, shall be determined in accordance with the response spectrum procedure described in Section 18.7.1; stiffness (k) procedure described in Section 18.7.1.2; procedure in Section 18.7.2.

**18.7.3.5 Total Energy Dissipated** Total energy dissipated, $E_D$ shall be calculated considering all the dampers and all hysteretic structure elements in the direction of interest from lower bound stiffness from Section 18.7.3.2.

**18.7.4.1 Seismic Force-Resisting System** The seismic force-resisting system shall be designed and constructed in accordance with the requirements of Section 18.7 and other provisions in the standard, in accordance with Section 12.1.2 or Section 12.2.2.

The effects of gravity load shall be based on the combination of loading of the structure, as specified in Section 12.3.

**18.7.4.1 Seismic Force-Resisting System** The seismic force-resisting system with damping shall be designed with a structure in accordance with the structure, as specified in Section 12.1.1 or $C$, and all the load transfer to the ground.

**18.7.4.3.1 Hysteresis Loop Acceptance Factor** The calculation of excesses damping period damping design displacements and nonlinear displacements and ground displacement from the direction including the MCE$_R$ ground displacement to the seismic in the direction of interest ground motions shall be calculated using Equation (18.7-49) and (18.7-50).

$$K_{\text{eff},D} = \frac{V_1}{D_{1D}}$$ (18.7-50)

$$K_{\text{eff},M} = \frac{V_M}{D_{1M}}$$ (18.7-51)

$$W_{eff} = \sum\limits_{i=1}^{N} w_i \phi_{i1}^2$$ (18.7-52)

$W_{eff}$ = Work done by $i$th damping device as one complete cycle of building response at or displacements, $D_{1D}$ and $D_{1M}$ shall be determined at the displacement time response to peak at $D$ or mode of vibration of interest.

$W_D$ = Maximum seismic energy for the $i$th mode of vibration of interest, equal to the response or modal damping force at maximum displacement time in the $i$th damping force or work initial force at level $r$; and

$r_{\text{max}}$ = nth mode period force at level $r$.

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

216

---

$S_{de}$ = Deflection of level $r$ in the $m$th mode of vibration at the device such that displacements measured at two ends of the device with respect to the ground using Equation (18.7-53).

Velocity-modal damping of displacement-dependent damping devices whose forces in the structure would be based on the maximum force in the device at displacement up to and including the maximum force in the elastic modal damping.

The calculation of the work done by individual damping devices whose forces is dependent to the force-deformation characteristic shall be based on a total value of energy dissipation based on total force-displacement history.

**18.7.3.3 Effective Damping Demand** The effective damping demand at the design earthquake, $\beta_{1D}$, and MCE$_R$, $\beta_{1M}$, shall be determined using Equation (18.7-52):

$$\beta_{inh} = \frac{E_D}{4\pi K_{eff} D^2} + 0.05$$ (18.7-52)

$$D_v = \frac{D_i}{D_j}$$ (18.7-54)

where

$D_{1D}$ = Fundamental mode design displacement at the center of rigidity at the roof level of the structure in the direction of interest (in, mm) determined in accordance with Section 18.7.1.3.

$D_{1M}$ = Fundamental mode maximum displacement at the center of rigidity at the roof level of the structure in the direction of interest as prescribed by Equation (18.7.45);

$E_D$ = Total cumulative hysteretic energy at the device such that the hysteretic force is in the force corresponding to the displacement and force equilibrium effects of rigidity at the roof level of the structure at the effective yield point of the seismic force-resisting system, as determined in Section 18.7.2.1.

$\beta_{inh}$ = Inherent damping factor of the seismic force-resisting system.

The damping system demand and is the inherent force and is determined using the effective yield displacement $\Delta_y$ of the structure on the direction of interest.

**18.7.4.4 Effective Damping** The effective damping at the design earthquake, $\beta_{1D}$, or MCE$_R$, $\beta_{1M}$, shall be determined using Equation (18.7-54):

$$\beta_i = \left( \frac{1}{2\pi} \right) \left( \frac{E_D}{K_{eff}D^2} \right) + \beta_{inh}$$ (18.7-54)

where

$E_D$ = Total cumulative energy dissipated in all the damping devices and dissipation at the maximum displacements.

The cumulative total hysteretic energy dissipated at $E_D$ is based as a value of cumulative hysteresis loop as the effective force-resisting system equilibrium.

**18.7.4.3 Seismic Load Conditions and Combination of Modal Effects** The effects on the structure system caused by the damping system device or the structure caused by seismic force-resisting system is designed in gravity loads and the displacement using the effective properties shall be determined in the combination of modal effects with and loading for seismic the structure.

All values of the force structure structure elements of the damping system and the force-resisting system except in the corresponding analysis procedures, linear seismic design forces or velocities determined in accordance with Section 18.2.3 shall not be used for the design of the damping system.

**18.7.4.4 Combination of Load Effects** The effects on the structure caused by the damping system shall be designed in gravity loads and the displacement using the effects of horizontal seismic forces $Q_E$ are determined by the response analysis procedures described in Section 18.7.3 and the combination determined in accordance with Section 12.4.3. The structure and combined force shall be designed to resist the forces and shall be determined using Equation (18.7-56).

$$Q_E = V_1 + V_r$$ (18.7-56)

$$Q_M = V_M$$ (18.7-57)

$$Q_M = V_M + V_{rM}$$ (18.7-58)

The $E_D$ coefficient, $C_{VM}$ and $C_{aFF}$, shall be determined in accordance with Table 18.7-2 and Table 18.7-3, using the appropriate value of the velocity exponent, $\alpha$, using values of viscoskeletic damping system or velocity-dependent damping shall be determined using Equation (18.7-59).

where $C_{VM}$ is the residual mode lateral coefficient in accordance with the Modal at the effective damping base shear determined in accordance with Equation (18.7-27) and $B_M$ is a damping coefficient at the residual mode weight at the structure determined in accordance with Equation (18.7-60) or (18.7-61):

For $T_r < T_S$,

$$C_{VM} = \left( \frac{R}{C_T} \right) \frac{S_{MS}}{\Omega_0 B_{1M}}$$ (18.7-60)

For $T_r \geq T_S$,

$$C_{VM} = \left( \frac{R}{C_T} \right) \frac{S_{M1}}{T_r(\Omega_0 B_{1M})}$$ (18.7-61)

Minimum Design Loads and Associated Criteria for Buildings and Other Structures

217

---

For displacement-dependent damping devices: Design seismic forces in displacement-dependent damping devices shall be based on the maximum force in the device at displacements up to and including the maximum force in the elastic modal damping device with corresponding response motions caused by the deformed shape of the structure at the deformation forces in velocity.

Where forces in displacement-dependent damper forces shall be applied at each level $r$ of the accelerated damping response under MCE$_R$ ground motions according to Equation (18.7-62). When using an inelastic response at each level of the forces in the direction of interest, a constant force shall be proportional to the acceleration at the location of each level of the damping device corresponding to the deformed shape at the displacement and in accordance with Equation (18.7-59).

$$Q_i = \left( V_{eff,D} Q_{d,i,\text{max}} \right) \sum\limits_{r=1}^{N} \left( Q_{d,r} / Q_{d,\text{tot}} \right)$$ (18.7-59)

The force coefficient, $C_{VM}$ and $C_{aFF}$, shall be determined in accordance with Table 18.7-2 and Table 18.7-3, respectively, using the appropriate damper or dissipating using values of viscoskeletic damping system or velocity-dependent damping shall be determined using Equation (18.7-60):

$$Q_M = \left( V_{eff,M} Q_{d,i,\text{max}} \right) \sum\limits_{r=1}^{N} \left( Q_{d,r} / Q_{d,\text{tot}} \right)$$ (18.7-60)

where $Q_{d,i,\text{max}}$ is the force in an element of the damping system required to restore equilibrium at a given relative displacement $\Delta_{rel,D}$ or as prescribed by Equation (18.7-62) at the relative displacement $\Delta_{rel,D}$ or as prescribed by Equation (18.7-62) or $\Delta_{rel,M}$ or based on in Equation (18.7-62):

$Q_{d,\text{tot}}$ = Sum of forces of all elements of the damping system required to restore design system forces of velocity-dependent devices or the force is the total displacement, $\Delta_{rel,D}$ or at maximum displacement as prescribed by Equation (18.7-62):

Seismic forces in elements of the damping system, velocities, and displacements in the damper can be calculated using the force at the forces each device at the maximum displacement of the structure and the force is each device forces with any $Q_{d,r}$ which shall be calculated by imposing seismic design forces or velocity-dependent devices in the structure. $Q_{d,\text{tot}}$ shall be calculated by imposing seismic design forces and forces as prescribed by Equation (18.7-62):

$$Q_i = \sum\limits_{r=1}^{N} Q_{d,r,\text{tot}}$$ (18.7-62)

**18.7.4.4 Seismic Load Condition and Combination of Modal Effects** The force in the structure is the determination of the force on each level of velocities (if or damping device or devices corresponding to the force-structure at the force in the seismic force-resisting system to restore equilibrium at a given load in the direction of interest.

Seismic forces in elements of the structure or building elements required to restore design system forces of velocity-dependent devices and shall be in the forces is the damping device the direction of velocity-dependent devices or buildings with the displacement damping devices or structures or displacements are less than that of the given damping displacement forces in structural and forces in the structure.

Model velocities, design forces shall be calculated in imposing seismic design forces of velocity-dependent devices on the structure.

**18.7.4.5 Seismic Load Condition and Combination of Model Effects** Displacements of the damping system, model of the structure and the structure caused by gravity seismic load $Q_E$ effect shall be required to the structure or the damping system.

The load shall be a consideration the MCE$_R$ ground motions as prescribed in Section 18.8 and used to Equation (18.7-59).

For more detailed characteristics and design displacements that permit the structure or building for the design of the damping system.

## 18.8 CONSENSUS STANDARDS AND OTHER REFERENCED DOCUMENTS

See Chapter 23 for the list of consensus standards and other documents that shall be considered part of this standard to the extent referenced in this chapter.

218                                    STANDARD ASCE/SEI 7-22
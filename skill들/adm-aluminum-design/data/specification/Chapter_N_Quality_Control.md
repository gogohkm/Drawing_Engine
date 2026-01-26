# Chapter N: Quality Control and Quality Assurance

**Document:** Aluminum Design Manual 2020
**Part:** Part I - Specification for Aluminum Structures
**Original Pages:** 81-83
**Edition:** January 2020
**Publisher:** Aluminum Association

---

## Table of Contents

- [N.1 SCOPE](#n1-scope)
- [N.2 FABRICATOR'S QUALITY CONTROL PROGRAM](#n2-fabricators-quality-control-program)
- [N.3 ENGINEER'S QUALITY CONTROL PROGRAM](#n3-engineers-quality-control-program)
- [N.4 INSPECTION AND NONDESTRUCTIVE TESTING REQUIREMENTS](#n4-inspection-and-nondestructive-testing-requirements)
- [N.5 INSPECTION REQUIREMENTS](#n5-inspection-requirements)
- [N.6 NONCONFORMANCE](#n6-nonconformance)
- [1.1 GENERAL PROVISIONS](#11-general-provisions)
- [1.2 TEST CONDITIONS](#12-test-conditions)
- [1.3 DESIGN BASED ON TESTING](#13-design-based-on-testing)
  - [1.3.1 Method 1](#131-method-1)
  - [Table 1.3.1](#table-131)
  - [STATISTICAL COEFFICIENT $K$](#statistical-coefficient-k)
  - [1.3.2 Method 2](#132-method-2)

---

--|------|-----|------|
| 3 | 10.55 | 18 | 3.370 |
| 4 | 7.042 | 19 | 3.331 |
| 5 | 5.741 | 20 | 3.295 |
| 6 | 5.062 | 21 | 3.262 |
| 7 | 4.641 | 22 | 3.233 |
| 8 | 4.353 | 23 | 3.206 |
| 9 | 4.143 | 24 | 3.181 |
| 10 | 3.981 | 25 | 3.158 |
| 11 | 3.852 | 30 | 3.064 |
| 12 | 3.747 | 35 | 2.994 |
| 13 | 3.659 | 40 | 2.941 |
| 14 | 3.585 | 45 | 2.897 |
| 15 | 3.520 | 50 | 2.863 |
| 16 | 3.463 | 100 | 2.684 |
| 17 | 3.415 | | |

### 1.3.2 Method 2

The resistance and safety factors used with the average of test strengths shall be determined in accordance with this Section. Resistance factors determined using this Section shall not be greater than the resistance factors given in the *Specification*. Safety factors determined using this Section shall not be less than the safety factors given in the *Specification*.

No fewer than four identical specimens shall be tested. If any individual result deviates from the average result by more than 10%, at least three more tests shall be performed.

For LRFD of building-type structures, the design strength shall be the average of all test results multiplied by the resistance factor φ determined as follows:

$$\phi = 1.5M_m F_{m} \phi^* \sqrt{F_{m^*}V_f^2 + V_M^2 + V_P^2 + V_Q^2} \tag{1.3-2 LRFD}$$

For ASD of building-type structures, the allowable strength shall be the average of all test results divided by the safety factor Ω determined as follows:

$$\Omega = \frac{1.05\alpha + 1}{M_m F_m (\alpha + 1)} e^{\beta \sqrt{V_f^2 + V_M^2 + V_P^2 + V_Q^2}} \tag{1.3-2 ASD}$$

where

$$C_a = \text{correction factor} = \frac{n^2 - 1}{n^2 - 3n}$$

- $D_n$ = nominal dead load
- $e$ = base for natural logarithms ≈ 2.72
- $F_m$ = mean value of the fabrication factor, the ratio of the specimen's relevant geometric property to its nominal value
- $L_n$ = nominal live load

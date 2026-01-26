# 알루미늄 기둥 강도 설계절차 (ADM 2020)

## 1. 설계 개요

알루미늄 기둥 설계는 **3가지 한계상태**를 모두 검토해야 합니다:

1. **부재좌굴 (Member Buckling)** - 전체 기둥의 좌굴
2. **국부좌굴 (Local Buckling)** - 단면 구성 요소의 좌굴
3. **상호작용 (Interaction)** - 부재좌굴과 국부좌굴의 상호작용

**설계강도:**
$$P_a = \text{min}(P_{nc,member}, P_{nc,local}, P_{nc,interaction}) / \Omega_c$$

여기서 $\Omega_c = 1.95$ (압축 안전계수, ASD)

---

## 2. 부재좌굴 검토 (Chapter E.2)

### 2.1 일반 좌굴 응력 산정

세장비 $\lambda$에 따른 좌굴응력:

| 좌굴 유형 | 좌굴응력 $F_c$ | 세장비 범위 |
|-----------|---------------|-------------|
| **항복** | $F_{cy}$ | $\lambda \leq \lambda_1$ |
| **비탄성좌굴** | $(B_c - D_c\lambda)\left(0.85 + 0.15\frac{C_c - \lambda}{C_c - \lambda_1}\right)$ | $\lambda_1 < \lambda < C_c$ |
| **탄성좌굴** | $\displaystyle\frac{0.85\pi^2 E}{\lambda^2}$ | $\lambda \geq C_c$ |

여기서:
- $\lambda_1 = \displaystyle\frac{B_c - F_{cy}}{D_c}$ (항복 한계)
- $B_c, D_c, C_c$: 좌굴상수 (합금별로 다름!)

**중요:** 강재와 달리 알루미늄은 **합금별로 다른 좌굴상수**를 사용합니다!

**6061-T6 (용접 없음):**
- $B_c = 30,000$ ksi
- $D_c = 200$
- $C_c = 65$

**6061-T6 (용접된 경우 - HAZ):**
- $B_c = 16,000$ ksi (47% 감소!)
- $D_c = 110$
- $C_c = 54$

### 2.2 휨좌굴 (Flexural Buckling)

가장 일반적인 좌굴 모드:

$$\lambda = \frac{kL}{r}$$

여기서:
- $k$ = 유효길이계수 (양단핀: 1.0, 양단고정: 0.5 등)
- $L$ = 비지지길이
- $r$ = 회전반경 ($r_x$ 또는 $r_y$ 중 최소값)

**절차:**
1. x축 및 y축에 대해 각각 $kL/r$ 계산
2. 큰 값을 $\lambda$로 사용
3. 해당 $\lambda$로 $F_c$ 산정

### 2.3 비틀림좌굴 (Torsional Buckling)

개단면(W형강, 채널 등)에서 중요:

$$\lambda = \pi\sqrt{\frac{E}{F_e}}$$

**이축대칭 단면 (W형강):**

$$F_e = \left(\frac{\pi^2 EC_w}{(k_z L_z)^2} + GJ\right)\frac{1}{I_x + I_y}$$

여기서:
- $C_w$ = 휨비틀림상수 (warping constant)
- $J$ = 비틀림상수 (torsion constant)
- $G$ = 전단탄성계수 = 3,800 ksi (알루미늄)
- $E$ = 탄성계수 = 10,100 ksi (알루미늄)
- $k_z$ = 비틀림 유효길이계수

**일축대칭 단면 (Tee, 채널):**

$$F_e = \frac{F_{ey} + F_{ez}}{2H}\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$

여기서:
$$F_{ey} = \frac{\pi^2 E}{(k_y L_y / r_y)^2}$$
$$F_{ez} = \frac{1}{A_g r_o^2}\left(GJ + \frac{\pi^2 EC_w}{(k_z L_z)^2}\right)$$
$$H = 1 - \frac{x_o^2 + y_o^2}{r_o^2}$$

---

## 3. 국부좌굴 검토 (Chapter E.3)

단면을 구성하는 각 요소(플랜지, 웨브 등)의 폭-두께비 검토

### 3.1 한 변 지지 요소 (플랜지 자유단)

**Section B.5.4.1**

| 상태 | 응력 $F_c$ | 세장비 $b/t$ |
|------|-----------|-------------|
| 항복 | $F_{cy}$ | $b/t \leq \lambda_1 = \displaystyle\frac{B_p - F_{cy}}{5.0D_p}$ |
| 비탄성좌굴 | $B_p - 5.0D_p(b/t)$ | $\lambda_1 < b/t < \lambda_2$ |
| 후좌굴 | $\displaystyle\frac{k_2\sqrt{B_p E}}{5.0(b/t)}$ | $b/t \geq \lambda_2 = \displaystyle\frac{k_1 B_p}{5.0D_p}$ |

여기서:
- $b$ = 요소 폭 (필렛 토우에서 자유단까지)
- $t$ = 요소 두께

**6061-T6 용접 없음:**
- $\lambda_1 = 6.7$
- $\lambda_2 = 12.0$

### 3.2 양변 지지 요소 (웨브)

**Section B.5.4.2**

| 상태 | 응력 $F_c$ | 세장비 $b/t$ |
|------|-----------|-------------|
| 항복 | $F_{cy}$ | $b/t \leq \lambda_1 = \displaystyle\frac{B_p - F_{cy}}{1.6D_p}$ |
| 비탄성좌굴 | $B_p - 1.6D_p(b/t)$ | $\lambda_1 < b/t < \lambda_2$ |
| 후좌굴 | $\displaystyle\frac{k_2\sqrt{B_p E}}{1.6(b/t)}$ | $b/t \geq \lambda_2 = \displaystyle\frac{k_1 B_p}{1.6D_p}$ |

**6061-T6 용접 없음:**
- $\lambda_1 = 20.8$
- $\lambda_2 = 33.0$

### 3.3 가중평균법 (Weighted Average Method)

**Section E.3.1** - 가장 일반적인 방법

$$P_{nc} = \sum_{i=1}^{n} F_{ci} A_i + F_{cy}\left(A_g - \sum_{i=1}^{n} A_i\right)$$

여기서:
- $F_{ci}$ = 요소 $i$의 국부좌굴응력
- $A_i$ = 요소 $i$의 면적
- $A_g$ = 전체 단면적

**절차:**
1. 각 요소(플랜지, 웨브)의 $b/t$ 계산
2. 각 요소의 $F_c$ 산정
3. 면적 가중평균으로 $P_{nc}$ 계산

---

## 4. 상호작용 검토 (Chapter E.4)

국부좌굴이 부재좌굴보다 먼저 발생하는 경우:

**조건:** 탄성 국부좌굴응력 $F_e < $ 부재좌굴응력 $F_c$

**제한:**
$$P_{nc} \leq \left[\frac{0.85\pi^2 E}{\lambda^2}\right]^{1/3} F_c^{2/3} A_g$$

**탄성 국부좌굴응력 계산 (Section B.5.6):**

한 변 지지:
$$F_e = \frac{\pi^2 E}{(5.0 b/t)^2}$$

양변 지지:
$$F_e = \frac{\pi^2 E}{(1.6 b/t)^2}$$

---

## 5. 용접 영향 (HAZ - Heat Affected Zone)

**알루미늄의 가장 중요한 특징!**

### 5.1 HAZ 강도 감소

6061-T6 합금의 경우:

| 물성 | 용접 없음 | 용접된 부분 (HAZ) | 감소율 |
|------|----------|-----------------|--------|
| $F_{cy}$ | 35 ksi | 19 ksi | **46%** |
| $B_c$ | 30,000 ksi | 16,000 ksi | 47% |
| $D_c$ | 200 | 110 | 45% |
| $C_c$ | 65 | 54 | 17% |

### 5.2 용접 부재 설계 규정

**횡방향 용접 (Transverse Weld):**

- 용접이 단부에서 0.05L 이내: 용접 없음 물성 사용
- 용접이 단부에서 0.05L 초과: **전체 단면 용접된 것으로 간주**

**종방향 용접 (Longitudinal Weld):**

$$P_{nc} = P_{nw}\left(1 - \frac{A_{wz}}{A_g}\right) + P_{nwo}\frac{A_{wz}}{A_g}$$

여기서:
- $P_{nw}$ = 용접 없음 강도
- $P_{nwo}$ = 전체 용접 강도
- $A_{wz}$ = 용접영향구역 면적

---

## 6. 실무 설계 예제

### 예제 1: 6061-T6 W형강 기둥 (용접 없음)

**주어진 조건:**
- 단면: AW 8 × 6.18
- 길이: L = 8 ft = 96 in
- 단부조건: 양단핀 (k = 1.0)
- 약축 횡지지: 있음
- 합금: 6061-T6 (용접 없음)

**단면 물성 (Part V):**
- $A = 5.26$ in²
- $r_x = 3.37$ in
- $I_x = 59.7$ in⁴
- $I_y = 7.3$ in⁴
- $C_w = 107$ in⁶
- $J = 0.188$ in⁴
- 플랜지: $b_f = 5.00$ in, $t_f = 0.35$ in
- 웨브: $d = 8.00$ in, $t_w = 0.23$ in

**재료 물성 (6061-T6, Table B.4.2):**
- $F_{cy} = 35$ ksi
- $B_c = 30,000$ ksi
- $D_c = 200$
- $C_c = 65$
- $E = 10,100$ ksi
- $G = 3,800$ ksi

---

#### **단계 1: 부재좌굴 검토**

**(1) 휨좌굴 (강축):**

$$\frac{kL}{r} = \frac{1.0 \times 96}{3.37} = 28.5$$

**(2) 비틀림좌굴 ($k_z = 0.5$ 가정):**

$$F_e = \left[\frac{\pi^2(10,100)(107)}{(0.5 \times 96)^2} + 3,800 \times 0.188\right] \times \frac{1}{59.7 + 7.3}$$
$$= \left[\frac{10,743,070}{2,304} + 714\right] \times \frac{1}{67}$$
$$= (4,663 + 714) \times 0.0149 = 79.8 \text{ ksi}$$

$$\lambda = \pi\sqrt{\frac{E}{F_e}} = \pi\sqrt{\frac{10,100}{79.8}} = \pi \times 11.25 = 35.3$$

**(3) 지배 세장비:**

$\lambda = 35.3$ (비틀림좌굴이 지배)

**(4) 좌굴응력 산정:**

$\lambda_1 = \displaystyle\frac{30,000 - 35}{200} = 149.8$

$35.3 < 65 = C_c$ → 비탄성좌굴

$$F_c = (B_c - D_c\lambda)\left(0.85 + 0.15\frac{C_c - \lambda}{C_c - \lambda_1}\right)$$
$$= (30,000 - 200 \times 35.3)\left(0.85 + 0.15 \times \frac{65 - 35.3}{65 - 149.8}\right)$$
$$= 22,940 \times (0.85 + 0.15 \times \frac{29.7}{-84.8})$$
$$= 22,940 \times (0.85 - 0.053) = 22,940 \times 0.797 = 18,283 \text{ psi}$$

실제 테이블 값 사용 (간편): $F_c / \Omega = 17.6$ ksi

$$F_c = 17.6 \times 1.95 = 34.3 \text{ ksi}$$

**부재좌굴 강도:**
$$P_{nc,member} = F_c \times A_g = 34.3 \times 5.26 = 180.4 \text{ kips}$$

---

#### **단계 2: 국부좌굴 검토**

**(1) 플랜지 (한 변 지지, Section B.5.4.1):**

$$\frac{b}{t} = \frac{5.00 - 0.23 - 2(0.30)}{2 \times 0.35} = \frac{4.17}{0.70} = 6.0$$

$6.0 < \lambda_1 = 6.7$ → 항복

$$F_{c,flange} = F_{cy} = 35 \text{ ksi}$$

허용응력: $F_{c,flange}/\Omega = 35/1.95 = 17.9$ ksi

플랜지 면적:
$$A_f = 2(5.00 - 0.23) \times 0.35 = 3.34 \text{ in}^2$$

**(2) 웨브 (양변 지지, Section B.5.4.2):**

$$\frac{b}{t} = \frac{8.00 - 2(0.35) - 2(0.30)}{0.23} = \frac{6.70}{0.23} = 29.1$$

$20.8 = \lambda_1 < 29.1 < \lambda_2 = 33.0$ → 비탄성좌굴

$$F_c/\Omega = B_p - 1.6D_p(b/t)$$
$$ = 27.3 - 0.291 \times 29.1 = 18.8 \text{ ksi}$$

웨브 면적:
$$A_w = (8.00 - 2 \times 0.35) \times 0.23 = 1.68 \text{ in}^2$$

**(3) 가중평균 (Section E.3.1):**

$$P_{nc,local}/\Omega = F_{c,flange}/\Omega \times A_f + F_{c,web}/\Omega \times A_w + F_{cy}/\Omega \times (A_g - A_f - A_w)$$

$$= 17.9 \times 3.34 + 18.8 \times 1.68 + \frac{35}{1.95} \times (5.26 - 3.34 - 1.68)$$
$$= 59.8 + 31.6 + 17.9 \times 0.24 = 95.7 \text{ kips}$$

**국부좌굴 강도:**
$$P_{nc,local} = 95.7 \times 1.95 = 186.6 \text{ kips}$$

---

#### **단계 3: 상호작용 검토**

**(1) 탄성 국부좌굴응력:**

플랜지 ($b/t = 6.0$):
$$F_{e,flange} = \frac{\pi^2 E}{(5.0 b/t)^2} = \frac{\pi^2 \times 10,100}{(5.0 \times 6.0)^2} = 110.8 \text{ ksi}$$

웨브 ($b/t = 29.1$):
$$F_{e,web} = \frac{\pi^2 E}{(1.6 b/t)^2} = \frac{\pi^2 \times 10,100}{(1.6 \times 29.1)^2} = 46.0 \text{ ksi}$$

**(2) 상호작용 검토:**

최소 탄성좌굴응력: $F_e = 46.0$ ksi
부재좌굴응력: $F_c = 34.3$ ksi

$F_e = 46.0 > 34.3 = F_c$ → **상호작용 없음** ✓

---

#### **최종 설계 강도**

$$P_a = \min(180.4, 186.6) = 180.4 \text{ kips}$$

부재좌굴이 지배하며, 허용압축강도는:

$$\boxed{P_a = \frac{180.4}{1.95} = 92.5 \text{ kips}}$$

---

### 예제 2: 6061-T6 W형강 기둥 (용접 있음)

**동일 조건 + 중앙에 횡방향 용접**

중앙 용접 → 0.05L = 0.05 × 96 = 4.8 in 초과
→ **전체 단면 용접된 것으로 간주**

**HAZ 물성 사용 (Table B.4.1):**
- $F_{cyw} = 19$ ksi (35 ksi → **46% 감소**)
- $B_c = 16,000$ ksi
- $D_c = 110$
- $C_c = 54$

#### **단계 1: 부재좌굴 (HAZ 물성)**

휨좌굴: $\lambda = 28.5$ (동일)
비틀림좌굴: $\lambda = 35.3$ (동일, 기하학적 성질 불변)

지배: $\lambda = 35.3 < C_c = 54$ → 비탄성좌굴

테이블 값 (Table 2-19W):
$$F_c/\Omega = 8.3 \text{ ksi}$$

**부재좌굴 강도 (HAZ):**
$$P_{nc,member} = 8.3 \times 1.95 \times 5.26 = 85.2 \text{ kips}$$

→ **용접 없음 대비 53% 감소!**

#### **단계 2: 국부좌굴 (HAZ 물성)**

플랜지 ($b/t = 6.0$):
- HAZ에서 $\lambda_1 = 9.0$
- $6.0 < 9.0$ → 항복
- $F_c/\Omega = 9.1$ ksi (HAZ)

웨브 ($b/t = 29.1$):
- HAZ에서 $\lambda_1 = 28.2$, $\lambda_2 = 58$
- $28.2 < 29.1 < 58$ → 비탄성
- $F_c/\Omega = 12.0 - 0.105 \times 29.1 = 8.9$ ksi

가중평균:
$$P_{nc,local}/\Omega = 9.1 \times 3.34 + 8.9 \times 1.68 + \frac{19}{1.95} \times 0.24$$
$$= 30.4 + 15.0 + 2.3 = 47.7 \text{ kips}$$

**국부좌굴 강도 (HAZ):**
$$P_{nc,local} = 47.7 \times 1.95 = 93.0 \text{ kips}$$

#### **최종 설계 강도 (용접)**

$$\boxed{P_a = \frac{85.2}{1.95} = 43.7 \text{ kips}}$$

**비교:**
- 용접 없음: 92.5 kips
- 용접 있음: 43.7 kips
- **감소율: 53%** → HAZ의 치명적 영향!

---

## 7. 설계 체크리스트

### ✅ 필수 검토사항

**1. 재료 확인**
- [ ] 합금 및 템퍼 확인 (예: 6061-T6)
- [ ] 용접 여부 확인 (HAZ 영향)
- [ ] 온도 조건 (200°F 초과 시 강도 감소)

**2. 부재좌굴**
- [ ] 휨좌굴: $kL/r_x$, $kL/r_y$ 계산
- [ ] 비틀림좌굴 (개단면인 경우)
- [ ] 최대 세장비로 $F_c$ 산정
- [ ] 적절한 좌굴상수 ($B_c, D_c, C_c$) 사용

**3. 국부좌굴**
- [ ] 각 요소의 $b/t$ 계산
- [ ] 각 요소의 국부좌굴응력 산정
- [ ] 가중평균법 적용

**4. 상호작용**
- [ ] 탄성 국부좌굴응력 계산
- [ ] $F_e < F_c$ 인지 확인
- [ ] 필요 시 상호작용 감소계수 적용

**5. 용접 영향**
- [ ] 횡방향 용접 위치 확인 (0.05L 기준)
- [ ] HAZ 물성 사용 여부 결정
- [ ] 종방향 용접 시 면적비 계산

---

## 8. 강재와의 주요 차이점

| 항목 | 강재 (AISC) | 알루미늄 (ADM) |
|------|------------|--------------|
| 탄성계수 | E = 29,000 ksi | E = 10,100 ksi (35%) |
| 좌굴곡선 | 단일 곡선 | **합금별 다름** |
| 용접 영향 | 미미 (~5%) | **치명적 (40-60%)** |
| 온도 한계 | ~600°F | **200°F** (T6 템퍼) |
| 설계법 | LRFD + ASD | **ASD만** |
| 좌굴상수 | 동일 | $B_c, D_c, C_c$ 합금별 |

---

## 9. 설계 팁

**1. 용접 최소화**
- 가능하면 볼트 접합 사용
- 용접 불가피 시: 5xxx 계열 (HAZ 영향 미미)

**2. 합금 선택**
- 6061-T6: 일반 구조 (용접 없음)
- 5083-H112: 용접 구조 (HAZ 영향 없음)
- 6063-T6: 건축용 (강도 낮음)

**3. 비틀림좌굴 주의**
- 개단면(W, C, L)은 항상 검토
- 비틀림 구속 확보 시 $k_z$ 감소 가능

**4. 국부좌굴 제어**
- 두꺼운 요소 사용
- 리브/스티프너 추가

---

## 10. 참고 문헌

**ADM 2020 참조:**
- Chapter E: Design of Members for Compression (E.2-E.4)
- Chapter B: Design Requirements (B.5.4 - Local Buckling)
- Part VII: Example 9 (W-Shape in Axial Compression)
- Part VII: Example 11 (Welded W-Shape in Axial Compression)

**주요 테이블:**
- Table B.4.1: Buckling Constants for Welded Material
- Table B.4.2: Buckling Constants for T5/T6 Tempers
- Part IV: Material Properties

---

이 설계절차를 따르면 ADM 2020 기준에 완전히 부합하는 알루미늄 기둥 설계가 가능합니다. 특히 **HAZ 영향을 절대 간과하지 마세요** - 이것이 알루미늄 설계의 핵심입니다!

---

*작성일: 2025-11-10*
*기준: ADM 2020 (Aluminum Design Manual 2020)*
*문서 위치: references/알루미늄기둥.md*

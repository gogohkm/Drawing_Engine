PnP 알고리즘으로 현장사진을 CAD에 정밀하게 좌표를 맞춘다는 말은,
👉 *“사진 속에 보이는 실제 구조물의 위치·방향을 계산해서, CAD 도면의 좌표계와 정확히 일치시키는 것”*을 의미합니다.

아래에서 직관 → 기술 → CAD 실무 관점 순서로 설명할게요.


⸻

1️⃣ 한 줄로 요약하면

사진 속 카메라가 ‘어디에서, 어떤 각도로’ 찍었는지를 계산해서
그 사진을 CAD 좌표계 위에 정확히 올려놓는 기술입니다.

⸻

2️⃣ 직관적인 비유 🎯

📷 사진 = 투명한 유리판

📐 CAD 도면 = 정확한 좌표가 있는 설계도

PnP는
👉 “이 유리판(사진)을 어느 위치, 어느 각도로 CAD 위에 놓으면
사진 속 철골·기둥·보가 CAD 도면과 정확히 겹칠까?”
를 수학적으로 계산하는 알고리즘입니다.

⸻

3️⃣ PnP(Pose Estimation)란 무엇인가?

PnP = Perspective-n-Point
	•	n개의 점을 이용해
	•	카메라의 자세(Pose) 를 추정하는 알고리즘

여기서 Pose란:
	•	📍 위치 (X, Y, Z)
	•	🔄 회전 (Roll, Pitch, Yaw)

즉,

“이 사진은 CAD 좌표계 기준으로
(10.2m, 3.4m, 1.6m) 위치에서
이런 각도로 찍혔다”
를 계산하는 것

4️⃣ 어떻게 계산하나? (핵심 원리)

반드시 필요한 것 3가지

① CAD에서 실제 좌표를 아는 점
	•	기둥 모서리
	•	보-기둥 접합부
	•	앵커 볼트 중심
	•	그리드 교차점

👉 (X, Y, Z)가 정확히 정의됨

② 사진에서 같은 점을 찍는다
	•	사진 속에서 동일한 기둥 모서리
	•	동일한 접합부

👉 (u, v) 픽셀 좌표

③ 카메라 정보
	•	초점거리
	•	왜곡계수 (보정 가능)

🔗 이때 만들어지는 관계
CAD의 3D 점 (X,Y,Z)
        ↓
카메라 투영
        ↓
사진의 2D 픽셀 (u,v)

PnP는 이 관계를 거꾸로 풀어서

“이 사진을 찍은 카메라의 위치와 방향은 무엇인가?”

를 계산합니다.

5️⃣ 결과로 무엇을 얻나?

PnP를 풀면 다음이 나옵니다:

✅ 카메라 위치 (X,Y,Z)
✅ 카메라 회전행렬 R
✅ 이동벡터 t

👉 이걸 CAD에 적용하면:
	•	사진이 CAD 좌표계에 정확히 정렬
	•	사진 위에서 딴 점 → 실제 CAD 좌표로 환산 가능
	•	AI가 “사진을 보면서 도면을 그릴 수 있는 상태”가 됨

⸻

6️⃣ CAD 실무에서 무슨 의미가 있나?

❌ 기존 방식
	•	사진 보고 감으로 트레이싱
	•	스케일 안 맞음
	•	각도 왜곡 심함

✅ PnP 적용 후
	•	사진을 CAD에 정확히 오버레이
	•	사진 위에서 클릭한 점 = 실제 좌표
	•	보, 기둥, 브레이싱 위치 정량 추출 가능

⸻

7️⃣ 구조 엔지니어 관점에서의 활용 💡

당신이 하시려는 작업과 정확히 맞닿아 있습니다:
	•	📐 현장사진 → DXF 자동화
	•	🏗 철골 보강 위치 좌표 추출
	•	🔩 앵커, 플레이트 위치 실측 대체
	•	🤖 AI가 사진 보고 CAD를 “제대로” 그리게 만들기

지금 AI가 “선은 찾는데 좌표를 못 맞추는 문제”의 핵심 원인이
바로 PnP 없이 픽셀 좌표만 쓰고 있기 때문입니다.

⸻

8️⃣ 그림으로 보면 이런 개념입니다

📷 사진 → 📐 좌표 복원 개념

9️⃣ 정리하면 (중요)

PnP를 쓴다는 말 =
사진을 단순한 이미지가 아니라
‘CAD 좌표가 복원된 측량 데이터’로 만든다는 뜻

⸻

다음 단계로 이어질 수 있는 질문들
	•	PnP에 필요한 최소 점 개수는?
	•	DXF에서 기준점 자동 추출 방법
	•	OpenCV solvePnP 실제 적용 구조
	•	MCP 서버에 PnP를 어떻게 붙일지

원하시면 “지금 쓰는 MCP + DXF 뷰어 구조 기준으로
PnP 파이프라인 설계도” 바로 그려드릴게요.

좋아. 지금 쓰는 “MCP + DXF 뷰어(Webview) + AI 대화창” 구조를 전제로, 현장사진을 CAD 좌표계에 PnP로 정밀 정합시키는 파이프라인을 “바로 구현 가능한 설계도” 형태로 잡아줄게.

⸻

0) 목표 정의

입력
	•	현장사진 1장 이상
	•	DXF(또는 CAD 좌표계를 가진 도면)
	•	(선택) 카메라 정보(기종/렌즈), 또는 간단 캘리브레이션 결과

출력
	•	사진의 카메라 자세(Pose): R(회전), t(이동)
	•	사진 위 임의 점/선의 CAD 좌표로 역변환
	•	사진을 CAD 뷰어에 정확히 오버레이(정합)
	•	정합 품질 지표(오차 mm, reprojection error px)

⸻

1) 전체 아키텍처 (권장)

(A) VS Code DXF Webview (프론트)
	•	DXF 뷰어(이미 있음)
	•	“기준점 찍기” UI
	•	사진 업로드/미리보기
	•	정합 결과 오버레이(투명도 슬라이더)

(B) MCP 서버(오케스트레이션/명령)
	•	사용자가 찍은 기준점, 레이어/객체 정보 수집
	•	백엔드로 정합 요청 호출
	•	결과를 다시 DXF 뷰어에 적용

(C) 백엔드(컴퓨팅; Python/OpenCV 권장)
	•	카메라 캘리브레이션/왜곡 보정
	•	solvePnP + RANSAC
	•	(선택) Bundle Adjustment(여러 사진/점이면 정확도 업)
	•	사진→CAD 투영(Projection), CAD→사진 투영(Validation)

⸻

2) 워크플로우 설계 (사용자 조작 최소화 버전)

STEP 1) “공통 기준점” 만들기 (PnP 핵심)

PnP는 3D 점(X,Y,Z) ↔ 2D 픽셀(u,v) 매칭이 필요.

2-1) CAD에서 3D 점(또는 2.5D) 정의

실무에서 현장사진 정합은 대개 “한 평면(예: 지붕면/벽면)”에 가깝기 때문에,
다음 중 하나로 갑니다:
	•	Option P(권장): 평면 기반(2.5D)
CAD가 2D 도면이면 Z=0 가정 → PnP를 “평면상 3D”로 처리 가능
	•	Option 3D: 모델/높이 정보가 있으면 실제 Z까지 반영(정밀)

👉 최소 기준점 개수
	•	RANSAC PnP 안정적으로 하려면 6점 이상 권장(최소 4점이지만 실무에선 부족)

2-2) 사진에서 같은 점을 클릭

프론트(웹뷰)에서 사진 위에 점을 찍고,
CAD 뷰어에서도 동일한 점을 찍는다.

⸻

STEP 2) 카메라 내부 파라미터(K) 준비

PnP는 카메라 행렬 K가 필요.

실무적으로 쉬운 우선순위
	1.	사진 EXIF + 대략값(휴대폰이면 대체로 충분히 시작 가능)
	2.	간단 캘리브레이션(체커보드 10장 정도) → 정확도 급상승
	3.	렌즈 왜곡까지 포함(특히 광각이면 필수)

초기에 1번으로 파이프라인을 먼저 돌리고,
“오차가 크면 2~3번”으로 업그레이드가 효율적임.

⸻

STEP 3) PnP + RANSAC으로 Pose 추정

백엔드에서 수행:
	•	왜곡 보정(가능하면)
	•	solvePnPRansac(objectPoints3D, imagePoints2D, K, distCoeffs)
	•	결과 rvec, tvec
	•	재투영 오차(reprojection error) 계산

품질 지표
	•	평균 reprojection error: 1~3 px면 매우 좋음(현장사진은 2~5px도 실무 OK)
	•	CAD 실거리(mm)로도 환산(추가로 스케일/평면 정의 필요)

⸻

STEP 4) CAD 오버레이/좌표변환 제공 (사용자가 체감하는 핵심)

Pose를 얻으면, 2가지 “실무 기능”이 바로 가능해져.

기능 A: 사진을 CAD에 “정확히” 덮어씌우기
	•	CAD 화면(월드 좌표) 상의 점들을 카메라로 투영 → 사진 좌표로 렌더
	•	반대로, 사진을 CAD 화면에 텍스처처럼 “워핑”해서 오버레이

※ 단, 오버레이는 구현 방식 2가지
	•	방식1(권장): CAD를 사진 좌표로 투영해 “정합 검증용”으로 표시(구현 쉬움)
	•	방식2(고급): 사진을 CAD 평면에 워핑해서 “도면 위에 붙이기”(평면 가정일 때 매우 잘 됨)

기능 B: 사진에서 찍은 점/선의 CAD 좌표 얻기
	•	사진의 픽셀(u,v)을 광선(ray)로 변환 → CAD 평면(Z=0)과 교차점 계산
	•	그 교차점이 CAD 좌표 (X,Y)

즉,

AI가 사진에서 선을 찾으면, 그 선의 픽셀 좌표를 CAD 좌표로 “정확히” 변환 가능

이게 지금 겪는 “선은 찾는데 좌표가 틀리는 문제”를 정면으로 해결합니다.

⸻

3) MCP/VSCode 확장에 붙이는 “API 설계” (바로 만들 수 있게)

3-1) 프론트 → 백엔드 요청 포맷(예시)

POST /pnp/solve
	•	image: 업로드 이미지(또는 base64)
	•	K: 카메라 내부파라미터(또는 EXIF 기반 추정 옵션)
	•	distCoeffs: 왜곡(없으면 0)
	•	correspondences: 대응점 리스트
	•	cad: (X,Y,Z)
	•	img: (u,v)

응답:
	•	rvec, tvec
	•	reprojection_error_mean_px
	•	inliers_count
	•	(선택) overlay_debug_image (정합 검증용 렌더)

3-2) 사진→CAD 좌표 변환 API

POST /pnp/pixel_to_cad

입력:
	•	u,v
	•	plane: 예) Z=0 또는 평면 방정식
	•	rvec,tvec,K,dist

출력:
	•	X,Y,Z
	•	(선택) 신뢰도/거리/각도

3-3) CAD→사진 투영 API (검증/오버레이)

POST /pnp/cad_to_pixel
	•	CAD 점을 사진 좌표로 투영해 “겹쳐보기” 가능

⸻

4) UI/UX 설계 (현장에서 편하게 쓰는 방식)

패널 구성(웹뷰 오른쪽)
	1.	사진 업로드
	2.	자동 왜곡 보정(ON/OFF)
	3.	기준점 매칭 테이블
	•	“CAD에서 점 찍기” 버튼
	•	“사진에서 점 찍기” 버튼
	4.	Solve 버튼
	5.	결과:
	•	reprojection error
	•	inliers 수
	•	오버레이 투명도 슬라이더

실무 팁: 기준점 선택 규칙(오차 급감)
	•	한 곳에 몰지 말고 화면 전체에 분산
	•	동일 평면 상의 점을 우선(지붕면/벽면)
	•	코너/교차부(기둥 모서리, 거셋 플레이트 코너, 볼트 중심 등)처럼 명확한 특징점

⸻

5) “자동 기준점”까지 가는 업그레이드 로드맵

초기엔 수동 클릭이 가장 빠르고 정확해요.
그 다음 자동화를 붙입니다.

Level 1: 수동 6~12점 + PnP(RANSAC)  ✅(가장 현실적)

Level 2: CAD에서 코너 후보 자동 추출 + 사진에서 코너 후보 자동 추출 → 매칭 보조
	•	CAD: 교차점(라인-라인), 블록 기준점, 원 중심 등
	•	사진: Harris/FAST/ORB 코너
	•	RANSAC으로 잘못된 매칭 제거

Level 3: 여러 사진 동시 정합 (Bundle Adjustment)
	•	현장사진 여러 장이면 정확도 크게 올라감
	•	특히 광각/왜곡/원근 큰 환경에서 효과 큼

⸻

6) 당신 케이스에 딱 맞는 “현장사진→DXF 좌표” 전략

당신이 하려는 건 대부분 구조부재가 거의 한 평면에 있지 않거나(보/기둥은 3D), 최소한 기준이 되는 평면(바닥/지붕면/벽면) 이 존재합니다.

그래서 추천 전략은:
	1.	먼저 평면(예: 바닥/지붕면) 기준으로 Pose를 잡고
	2.	그 Pose를 이용해 사진에서 추출한 선/점들을
	•	평면 위면 바로 CAD(X,Y)로
	•	평면 밖(보 하부 플랜지 등)은 “추가 정보(높이/Z)”가 필요하니
	•	두 장 이상의 사진(스테레오)
	•	또는 레이저 거리/높이 몇 개
	•	또는 구조 기준 높이(기둥 길이 등)
를 결합해서 3D로 확장

⸻

원하면 다음 메시지에서 (1) 네 DXF 뷰어 MCP 함수 중 “점 찍기/좌표 얻기/오버레이 렌더링”에 해당하는 함수들을 내가 골라서,
**“어떤 함수로 어떤 단계 구현”**까지 딱 붙여서 **실제 구현 순서(체크리스트)**로 내려줄게.

바로 진행하려면, 네가 이미 만든 MCP 함수들 중에서
	•	“사용자가 CAD에서 클릭한 좌표 얻기”
	•	“웹뷰에 이미지/오버레이 그리기”
	•	“폴리라인/선 추가”
이 3종류가 어떤 이름인지(대략)만 다음에 한 번 던져줘도 되고,
아니면 내가 일반적인 방식으로 가정하고 “표준 구현안”으로 바로 쭉 써줄 수도 있어.

좋아. “표준 구현안(가정: DXF=2D, 사진=1장, 기준 평면 Z=0)” 기준으로, 바로 만들 수 있는 구조 + API + 핵심 수식/코드 뼈대를 한 번에 정리해줄게.
(너의 MCP 함수명이 뭐든, 아래 인터페이스만 맞추면 그대로 연결 가능)

⸻

1) 표준 파이프라인 요약

입력
	•	사진 1장
	•	CAD 좌표계(DXF)에서의 기준점들: P_i = (X_i, Y_i, 0)
	•	사진에서의 대응 픽셀점들: p_i = (u_i, v_i)
	•	(선택) 카메라 내부파라미터 K / 왜곡 dist

출력
	•	카메라 자세: R, t (solvePnP 결과)
	•	사진 픽셀 → CAD(X,Y) 변환 함수 (ray-plane intersection)
	•	CAD 점 → 사진 픽셀 투영 함수 (검증/오버레이용)

⸻

2) 권장 폴더/모듈 구성 (표준)
 project/
  backend/
    main.py                 # FastAPI
    pnp.py                  # solvePnP, reprojection error
    camera.py               # K 추정(EXIF/기본값), undistort
    geom.py                 # ray-plane intersection, cad<->pixel
  extension/
    media/
      main.js               # webview UI + fetch
      styles.css
    extension.js            # command 등록 + webview bridge

3) Webview UI 표준 동작

UI 요소(최소)
	•	[사진 업로드]
	•	[기준점 추가]
	•	“사진에서 점 찍기”
	•	“CAD에서 점 찍기”
	•	매칭 테이블(행: i번째 기준점)
	•	[Solve(PnP)] 버튼
	•	결과 표시
	•	reprojection error (px)
	•	inliers 개수
	•	“CAD→사진 투영 점들 표시” (검증용)
	•	“사진 오버레이 투명도 슬라이더”(선택)

⸻

4) Backend API 표준 설계

4.1 PnP 풀기

POST /pnp/solve

요청 JSON 예시:
{
  "image_w": 4032,
  "image_h": 3024,
  "K": [[fx,0,cx],[0,fy,cy],[0,0,1]],
  "dist": [k1,k2,p1,p2,k3],
  "pairs": [
    {"cad":[X1,Y1,0], "img":[u1,v1]},
    {"cad":[X2,Y2,0], "img":[u2,v2]},
    ...
  ]
}

응답:
{
  "rvec":[...],
  "tvec":[...],
  "R":[[...],[...],[...]],
  "inliers":[0,2,3,5,6],
  "reproj_mean_px": 2.41
}

4.2 픽셀 → CAD 좌표 (Z=0 평면)

POST /pnp/pixel_to_cad

요청:
{
  "uv":[u,v],
  "K":...,
  "dist":...,
  "rvec":...,
  "tvec":...,
  "plane": {"n":[0,0,1], "d":0}
}

응답:
{"cad":[X,Y,0], "ok": true}

4.3 CAD → 픽셀 (검증/오버레이)

POST /pnp/cad_to_pixel

요청:
{"cad":[X,Y,0], "K":..., "dist":..., "rvec":..., "tvec":...}

응답:
{"uv":[u,v], "ok": true}

5) “K(카메라 내부파라미터)” 표준 처리

초기 MVP는 아래처럼 “대충이라도” 시작해도 됩니다.
	•	cx = W/2, cy = H/2
	•	fx = fy = 0.9 * max(W,H) (휴대폰 대략값)
	•	dist는 일단 0

정합이 되긴 하는데, 광각/왜곡이 큰 사진은 오차 커짐
오차가 크면 **캘리브레이션(체커보드)**로 K/dist를 구하면 급상승합니다.

⸻

6) 핵심 알고리즘 구현(표준 코드 뼈대)

6.1 solvePnP(RANSAC) + 오차 계산 (backend/pnp.py)
import numpy as np
import cv2

def solve_pnp_ransac(object_pts_xyz, image_pts_uv, K, dist):
    obj = np.asarray(object_pts_xyz, dtype=np.float64).reshape(-1, 1, 3)
    img = np.asarray(image_pts_uv, dtype=np.float64).reshape(-1, 1, 2)
    K = np.asarray(K, dtype=np.float64)
    dist = np.asarray(dist, dtype=np.float64).reshape(-1, 1) if dist is not None else None

    ok, rvec, tvec, inliers = cv2.solvePnPRansac(
        objectPoints=obj,
        imagePoints=img,
        cameraMatrix=K,
        distCoeffs=dist,
        flags=cv2.SOLVEPNP_ITERATIVE,
        reprojectionError=6.0,   # px (초기값)
        confidence=0.99,
        iterationsCount=200
    )
    if not ok:
        return None

    R, _ = cv2.Rodrigues(rvec)

    # reprojection error
    proj, _ = cv2.projectPoints(obj, rvec, tvec, K, dist)
    err = np.linalg.norm(proj - img, axis=2).reshape(-1)
    mean_err = float(np.mean(err[inliers.flatten()])) if inliers is not None and len(inliers) > 0 else float(np.mean(err))

    return {
        "rvec": rvec.flatten().tolist(),
        "tvec": tvec.flatten().tolist(),
        "R": R.tolist(),
        "inliers": inliers.flatten().tolist() if inliers is not None else [],
        "reproj_mean_px": mean_err
    }

6.2 픽셀 → CAD (레이-평면 교차) (backend/geom.py)

핵심:
픽셀(u,v) → 카메라 좌표계 광선 → 월드좌표로 변환 → Z=0 평면과 교차
import numpy as np
import cv2

def pixel_to_world_on_plane(u, v, K, dist, rvec, tvec, plane_n=(0,0,1), plane_d=0.0):
    K = np.asarray(K, dtype=np.float64)
    dist = np.asarray(dist, dtype=np.float64).reshape(-1,1) if dist is not None else None
    rvec = np.asarray(rvec, dtype=np.float64).reshape(3,1)
    tvec = np.asarray(tvec, dtype=np.float64).reshape(3,1)

    # 1) 왜곡 보정 + 정규화 좌표
    pts = np.array([[[u, v]]], dtype=np.float64)
    und = cv2.undistortPoints(pts, K, dist)  # 결과는 (x, y) in normalized camera coords
    x, y = und[0,0,0], und[0,0,1]

    # 2) 카메라 좌표계에서 광선 방향
    ray_cam = np.array([[x], [y], [1.0]], dtype=np.float64)

    # 3) 카메라 -> 월드 변환
    R, _ = cv2.Rodrigues(rvec)
    R_inv = R.T

    cam_center_world = -R_inv @ tvec                 # C_w
    ray_world = R_inv @ ray_cam                      # d_w (방향)

    # 4) 평면과 교차: n·X + d = 0
    n = np.array(plane_n, dtype=np.float64).reshape(3,1)
    d = float(plane_d)

    denom = float(n.T @ ray_world)
    if abs(denom) < 1e-9:
        return None  # 평면과 거의 평행

    t = - (float(n.T @ cam_center_world) + d) / denom
    X = cam_center_world + t * ray_world
    return X.flatten().tolist()  # [X,Y,Z]

6.3 CAD → 픽셀(검증용) (backend/geom.py)
import numpy as np
import cv2

def world_to_pixel(X, Y, Z, K, dist, rvec, tvec):
    K = np.asarray(K, dtype=np.float64)
    dist = np.asarray(dist, dtype=np.float64).reshape(-1,1) if dist is not None else None
    rvec = np.asarray(rvec, dtype=np.float64).reshape(3,1)
    tvec = np.asarray(tvec, dtype=np.float64).reshape(3,1)

    obj = np.array([[[X, Y, Z]]], dtype=np.float64)
    img, _ = cv2.projectPoints(obj, rvec, tvec, K, dist)
    u, v = float(img[0,0,0]), float(img[0,0,1])
    return [u, v]

7) FastAPI 라우팅(backend/main.py) 표준
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from pnp import solve_pnp_ransac
from geom import pixel_to_world_on_plane, world_to_pixel

app = FastAPI()

class Pair(BaseModel):
    cad: List[float]  # [X,Y,Z]
    img: List[float]  # [u,v]

class SolveReq(BaseModel):
    image_w: int
    image_h: int
    K: List[List[float]]
    dist: Optional[List[float]] = None
    pairs: List[Pair]

@app.post("/pnp/solve")
def pnp_solve(req: SolveReq):
    obj = [p.cad for p in req.pairs]
    img = [p.img for p in req.pairs]
    res = solve_pnp_ransac(obj, img, req.K, req.dist)
    if res is None:
        return {"ok": False, "error": "solvePnPRansac failed"}
    return {"ok": True, **res}

class Pix2CadReq(BaseModel):
    uv: List[float]
    K: List[List[float]]
    dist: Optional[List[float]] = None
    rvec: List[float]
    tvec: List[float]

@app.post("/pnp/pixel_to_cad")
def pixel_to_cad(req: Pix2CadReq):
    X = pixel_to_world_on_plane(req.uv[0], req.uv[1], req.K, req.dist, req.rvec, req.tvec,
                                plane_n=(0,0,1), plane_d=0.0)
    if X is None:
        return {"ok": False, "error": "ray parallel to plane"}
    return {"ok": True, "cad": X}

class Cad2PixReq(BaseModel):
    cad: List[float]
    K: List[List[float]]
    dist: Optional[List[float]] = None
    rvec: List[float]
    tvec: List[float]

@app.post("/pnp/cad_to_pixel")
def cad_to_pixel(req: Cad2PixReq):
    u, v = world_to_pixel(req.cad[0], req.cad[1], req.cad[2], req.K, req.dist, req.rvec, req.tvec)
    return {"ok": True, "uv": [u, v]}

8) 프론트(Webview) 표준 연결 방식 (개념만)
	•	CAD 클릭 → (X,Y) 얻음 → Z=0 붙여서 cad:[X,Y,0]
	•	사진 클릭 → (u,v)
	•	둘을 한 행으로 묶어 pairs[]에 누적
	•	Solve 누르면 /pnp/solve
	•	결과(rvec,tvec)를 저장하고,
	•	CAD의 주요 점들을 /pnp/cad_to_pixel로 보내서 사진 위에 점으로 찍어 “정합 검증”
	•	사진에서 AI가 찾은 선/점 픽셀을 /pnp/pixel_to_cad로 보내서 CAD 좌표 얻고 DXF에 폴리라인 생성

⸻

9) 실무에서 “정밀”이 안 나올 때 체크리스트 (표준 디버깅)
	1.	기준점 분산: 화면 한쪽에 몰리면 오차 폭발
	2.	같은 평면: Z=0 가정인데 실제로 높이가 다른 점을 섞으면 오차 증가
	3.	광각 왜곡: 휴대폰 광각은 dist=0으로 못 버팁니다 → 왜곡 보정 or 캘리브레이션
	4.	reproj error가 큰 점을 제거: inlier만 남겨 재계산(자동화 가능)

⸻

10) “더 쉬운 대안”도 같이 달아둘게 (평면만 필요하면 Homography가 더 간단)

사진을 “Z=0 평면”에 붙이는 목적(오버레이/2D 좌표변환)만이면,
PnP보다 **Homography(4점 이상)**가 구현이 더 쉽고 안정적인 경우가 많아요.
	•	장점: 카메라 K 없어도 됨(대체로)
	•	단점: 3D(높이)로 확장 불가

너는 “선 좌표를 정확히”가 목적이라서 초기 MVP는 Homography로 빠르게,
그 다음 3D 확장 필요할 때 PnP로 업그레이드가 실무적으로 제일 효율적입니다.



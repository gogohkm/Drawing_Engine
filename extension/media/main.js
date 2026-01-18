/**
 * VS Code Webview Main Script - Supports Homography (MVP-1) and PnP (MVP-2)
 */

(function () {
    const vscode = acquireVsCodeApi();

    let points2D = [];
    let pnpPoints = []; // [{u, v, x, y, z}]
    let currentImage = null;
    let homographyMatrix = null;
    let cameraPose = null; // {R, t, K}
    let mode = 'idle'; // 'calibrate', 'measure', 'pnp_register', 'pnp_measure'

    const canvas = document.getElementById('image-canvas');
    const ctx = canvas.getContext('2d');
    const mainStatus = document.getElementById('main-status');

    // Homography Elements
    const calibrateBtn = document.getElementById('calibrate-plane-btn');
    const measureBtn = document.getElementById('measure-p2p-btn');
    const planeStatus = document.getElementById('plane-status');

    // PnP Elements
    const startPnpBtn = document.getElementById('start-pnp-btn');
    const solvePnpBtn = document.getElementById('solve-pnp-btn');
    const resetPnpBtn = document.getElementById('reset-pnp-btn');
    const pnpBody = document.getElementById('pnp-body');
    const pnpMeasureControls = document.getElementById('pnp-measure-controls');
    const pnpMeasureBtn = document.getElementById('pnp-measure-btn');
    const pnpMeasureStatus = document.getElementById('pnp-measure-status');
    const planeSelect = document.getElementById('plane-select');

    window.addEventListener('message', event => {
        const message = event.data;
        switch (message.command) {
            case 'loadImage': loadImage(message.data); break;
            case 'calibrateResult': handleCalibrateResult(message.result); break;
            case 'measureResult': handleMeasureResult(message.result); break;
            case 'pnpSolveResult': handlePnpSolveResult(message.result); break;
            case 'pnpMeasureResult': handlePnpMeasureResult(message.result); break;
        }
    });

    function loadImage(base64) {
        const img = new Image();
        img.onload = () => {
            canvas.width = img.width; canvas.height = img.height;
            ctx.drawImage(img, 0, 0); currentImage = img;
            mainStatus.innerText = "Photo Ready.";
        };
        img.src = base64;
    }

    canvas.addEventListener('click', (e) => {
        if (!currentImage) return;
        const rect = canvas.getBoundingClientRect();
        const u = (e.clientX - rect.left) * (canvas.width / rect.width);
        const v = (e.clientY - rect.top) * (canvas.height / rect.height);

        if (mode === 'calibrate') {
            points2D.push({ u, v });
            drawPoint(u, v, points2D.length, 'yellow');
            if (points2D.length === 4) calibratePlane();
        } else if (mode === 'measure') {
            points2D.push({ u, v });
            drawPoint(u, v, points2D.length, 'cyan');
            if (points2D.length === 2) measureP2P();
        } else if (mode === 'pnp_register') {
            const id = pnpPoints.length + 1;
            pnpPoints.push({ u, v, x: 0, y: 0, z: 0 });
            drawPoint(u, v, id, 'red');
            updatePnpTable();
        } else if (mode === 'pnp_measure') {
            points2D.push({ u, v });
            drawPoint(u, v, points2D.length, 'magenta');
            if (points2D.length === 2) measure3DDist();
        }
    });

    function drawPoint(u, v, label, color) {
        ctx.fillStyle = color;
        ctx.beginPath(); ctx.arc(u, v, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = 'white'; ctx.font = 'bold 14px Arial';
        ctx.fillText(label, u + 8, v + 8);
    }

    function redraw() { if (currentImage) ctx.drawImage(currentImage, 0, 0); }

    // --- Mode Switches ---
    calibrateBtn.onclick = () => { mode = 'calibrate'; points2D = []; redraw(); planeStatus.innerText = "Pick 4 points (TL, TR, BR, BL)"; };
    measureBtn.onclick = () => { mode = 'measure'; points2D = []; redraw(); };
    startPnpBtn.onclick = () => { mode = 'pnp_register'; pnpPoints = []; redraw(); updatePnpTable(); };

    // --- Homography Logic ---
    function calibratePlane() {
        vscode.postMessage({
            command: 'calibratePlanePython',
            pts: points2D,
            span_mm: parseFloat(document.getElementById('span-mm').value)
        });
    }
    function handleCalibrateResult(res) {
        if (res.ok) {
            homographyMatrix = res.H_img_to_plane;
            planeStatus.innerText = `Calibrated! Lx=${res.Lx_mm.toFixed(0)}, Ly=${res.Ly_mm.toFixed(0)}`;
            measureBtn.disabled = false;
        }
    }
    function measureP2P() {
        vscode.postMessage({ command: 'measureP2PPython', H: homographyMatrix, P1: points2D[0], P2: points2D[1] });
    }
    function handleMeasureResult(res) {
        if (res.ok) planeStatus.innerText = `Dist: ${res.distance_mm.toFixed(1)}mm`;
    }

    // --- PnP Logic ---
    function updatePnpTable() {
        pnpBody.innerHTML = pnpPoints.map((p, i) => `
            <tr>
                <td>${i + 1}</td>
                <td>${p.u.toFixed(0)}, ${p.v.toFixed(0)}</td>
                <td>
                    X:<input type="number" value="${p.x}" onchange="updatePnpCoord(${i}, 'x', this.value)" style="width:50px">
                    Y:<input type="number" value="${p.y}" onchange="updatePnpCoord(${i}, 'y', this.value)" style="width:50px">
                    Z:<input type="number" value="${p.z}" onchange="updatePnpCoord(${i}, 'z', this.value)" style="width:50px">
                </td>
            </tr>
        `).join('');
    }
    window.updatePnpCoord = (idx, axis, val) => { pnpPoints[idx][axis] = parseFloat(val); };

    solvePnpBtn.onclick = () => {
        vscode.postMessage({
            command: 'solvePnpPython',
            points2D: pnpPoints.map(p => [p.u, p.v]),
            points3D: pnpPoints.map(p => [p.x, p.y, p.z]),
            width: canvas.width, height: canvas.height
        });
    };

    function handlePnpSolveResult(res) {
        if (res.ok) {
            cameraPose = { R: res.R, t: res.t, K: res.K };
            mainStatus.innerText = "Camera Pose Solved!";
            pnpMeasureControls.style.display = 'block';
        } else {
            mainStatus.innerText = "PnP Failed: " + res.error;
        }
    }

    pnpMeasureBtn.onclick = () => { mode = 'pnp_measure'; points2D = []; redraw(); pnpMeasureStatus.innerText = "Pick 2 points."; };

    function measure3DDist() {
        const plane = planeSelect.value;
        let n = [0, 0, 1], d = 0;
        if (plane === 'y0') { n = [0, 1, 0]; }
        else if (plane === 'x0') { n = [1, 0, 0]; }

        vscode.postMessage({
            command: 'measure3DDistPython',
            pose: cameraPose,
            P1: points2D[0],
            P2: points2D[1],
            plane_n: n, plane_d: d
        });
    }

    function handlePnpMeasureResult(res) {
        if (res.ok) {
            pnpMeasureStatus.innerText = `3D Dist: ${res.distance_mm.toFixed(1)}mm`;
            // Line
            ctx.strokeStyle = 'magenta'; ctx.lineWidth = 3;
            ctx.beginPath(); ctx.moveTo(points2D[0].u, points2D[0].v); ctx.lineTo(points2D[1].u, points2D[1].v); ctx.stroke();
        }
    }

    resetPnpBtn.onclick = () => { pnpPoints = []; updatePnpTable(); redraw(); pnpMeasureControls.style.display = 'none'; };

}());

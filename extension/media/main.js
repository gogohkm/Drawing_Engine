/**
 * VS Code Webview Main Script for Drawing Engine PnP
 * Simplified Version: Delegates calculation to Python backend
 */

(function () {
    const vscode = acquireVsCodeApi();

    let points2D = []; // {x, y}
    let points3D = []; // {x, y, z}
    let currentImage = null;

    // UI Elements
    const imageCanvas = document.getElementById('image-canvas');
    const ctx = imageCanvas.getContext('2d');
    const solveBtn = document.getElementById('solve-pnp-btn');
    const resetBtn = document.getElementById('reset-btn');
    const statusText = document.getElementById('pnp-status');

    /**
     * Get Camera Matrix approximation
     */
    function getCameraMatrix(width, height) {
        const fx = width * 1.0;
        const fy = width * 1.0;
        const cx = width / 2;
        const cy = height / 2;
        return [
            [fx, 0, cx],
            [0, fy, cy],
            [0, 0, 1]
        ];
    }

    /**
     * Handle messages from the extension host
     */
    window.addEventListener('message', event => {
        const message = event.data;
        switch (message.command) {
            case 'loadImage':
                loadImage(message.data);
                break;
            case 'add3DPoint':
                addPoint3D(message.point);
                break;
            case 'pnpCalculated':
                // Received result from Python
                if (message.error) {
                    statusText.innerText = `Error from Python: ${message.error}`;
                    statusText.style.color = 'red';
                } else {
                    const error = message.repro_error !== undefined ? ` (Error: ${message.repro_error}px)` : '';
                    const inliers = message.inliers !== undefined ? ` [Inliers: ${message.inliers}/${points2D.length}]` : '';
                    statusText.innerText = `Success! Pose calculated in Python.${error}${inliers}`;
                    statusText.style.color = 'lightgreen';
                }
                break;
        }
    });

    function loadImage(base64Data) {
        const img = new Image();
        img.onload = () => {
            imageCanvas.width = img.width;
            imageCanvas.height = img.height;
            ctx.drawImage(img, 0, 0);
            currentImage = img;
            statusText.innerText = "Image loaded. Pick at least 4 points on the image.";
            clearPoints();
        };
        img.src = base64Data;
    }

    imageCanvas.addEventListener('click', (e) => {
        if (!currentImage) return;

        const rect = imageCanvas.getBoundingClientRect();
        const x = (e.clientX - rect.left) * (imageCanvas.width / rect.width);
        const y = (e.clientY - rect.top) * (imageCanvas.height / rect.height);

        points2D.push({ x, y });
        drawPoint(x, y, points2D.length);

        vscode.postMessage({
            command: 'request3DPoint',
            index: points2D.length
        });
    });

    function addPoint3D(point) {
        points3D.push(point);
        if (points2D.length >= 4 && points3D.length === points2D.length) {
            solveBtn.disabled = false;
            statusText.innerText = `Ready to solve. ${points2D.length} points collected.`;
        }
    }

    function drawPoint(x, y, label) {
        ctx.fillStyle = 'red';
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = 'white';
        ctx.font = '12px Arial';
        ctx.fillText(label, x + 7, y + 7);
    }

    function clearPoints() {
        points2D = [];
        points3D = [];
        solveBtn.disabled = true;
        // Redraw image
        if (currentImage) ctx.drawImage(currentImage, 0, 0);
    }

    resetBtn.addEventListener('click', () => {
        clearPoints();
        statusText.innerText = "Points reset. Pick at least 4 points.";
    });

    /**
     * Send points to Python for PnP
     */
    solveBtn.addEventListener('click', () => {
        statusText.innerText = "Requesting PnP calculation from Python backend...";

        const cameraMatrix = getCameraMatrix(imageCanvas.width, imageCanvas.height);

        vscode.postMessage({
            command: 'calculatePnpPython',
            points2D: points2D,
            points3D: points3D,
            cameraMatrix: cameraMatrix
        });
    });

}());

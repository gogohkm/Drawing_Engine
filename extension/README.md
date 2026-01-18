# PnP Registration Extension Support (Python Version)

This directory contains the frontend files to enable PnP (Perspective-n-Point) matching in your VS Code extension. Geometric calculations are handled by the Python backend via `opencv-python`.

## Files Included

1.  **index.html**: The Webview UI for point collection.
2.  **main.js**: Handles image loading, 2D/3D point picking, and communication with the extension host.

## Prerequisites

The Python environment used by the Drawing Engine **must** have `opencv-python` installed:

```bash
pip install opencv-python
```

## Integration Guide

In your VS Code extension source code (`extension.ts` or similar):

1.  **Register a Webview Panel**.
2.  **Load these files** from your extension's `media` directory.
3.  **Communication Protocol**:
    - **Extension -> Webview**:
        - `loadImage`: Sends base64 image data.
        - `add3DPoint`: Sends a CAD point `{x, y, z}`.
        - `pnpCalculated`: (Optional) Notifies that the backend calculation is done.
    - **Webview -> Extension**:
        - `request3DPoint`: Triggered when a pixel is clicked.
        - `calculatePnpPython`: Sends `points2D`, `points3D`, and `cameraMatrix` to be processed by the Python backend.

## Why Python Backend?
By performing the PnP solve in Python, we leverage the performance and reliability of the native OpenCV library and avoid complex Wasm/OpenCV.js environment issues in the browser.

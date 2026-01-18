import json
import os
import math
from knowledge.engine.image_vectorizer import ImageVectorizer, Point, Line, write_lines_to_dxf

def create_3d_demo():
    print("Generating 3D Depth Demo DXF...")
    
    # 1. Load image to get contours
    image_path = "/Users/hi/2026Coding_Prj/Drawing_Engine/Ref/mosateyn8U-1024x768.jpeg"
    vectorizer = ImageVectorizer()
    vectorizer.mode = "edge"
    vectorizer.edge_threshold = 60
    vectorizer.simplify_epsilon = 2.0
    
    if not vectorizer.load_image(image_path):
        print("Failed to load image")
        return

    # 2. Vectorize to get contours (2D pixel coordinates)
    vectorizer.vectorize()
    
    # 3. Manually transform 2D lines to 3D for DEMO
    # We will simulate a simple 3D effect:
    # Points at the bottom stay at Z=0.
    # Points at the top are projected to Z=4000 (mm).
    # This creates a 'tunnel' or 'depth' effect in the DXF.
    
    h = vectorizer.binary_image.height
    w = vectorizer.binary_image.width
    
    real_3d_lines = []
    
    for line in vectorizer.lines:
        # Original pixel coords (we need to invert Y if necessary, but here we just use raw pixels)
        # We'll map pixels to a 10m x 10m floor for this demo
        
        def px_to_real_3d(p: Point):
            # Applying updated scale factor (approx 2.4975) to match 4m reference
            scale = 2.49747 # target 4000 / current 1601.62
            rx = (p.x / w) * 10000 * scale
            ry = (p.y / h) * 10000 * scale
            
            # Artificial Z: Also scale height for consistency
            rz = (1.0 - (p.y / h)) * 4000 * scale
            
            return Point(x=rx, y=ry, z=rz)

        start_3d = px_to_real_3d(line.start)
        end_3d = px_to_real_3d(line.end)
        
        real_3d_lines.append(Line(start=start_3d, end=end_3d))

    # 4. Save to DXF
    output_path = "/Users/hi/2026Coding_Prj/Drawing_Engine/real_world_depth_demo.dxf"
    write_lines_to_dxf(real_3d_lines, output_path, "3D_DEMO_DEPTH")
    
    print(f"Success! 3D Demo created at: {output_path}")
    print(f"Total lines: {len(real_3d_lines)}")
    print("Each point now has a unique Z value based on its vertical position in the photo.")

if __name__ == "__main__":
    create_3d_demo()

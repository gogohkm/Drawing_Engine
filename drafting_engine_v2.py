import json
import os

# Mocking the stgen-dxf-viewer tool structure for programmatic generation
# In a real environment, this script would generate a list of commands or call an API.
# Here, I am writing the logic that I will execute.

def generate_drafting_commands():
    with open('drawing_memory.json', 'r') as f:
        memory = json.load(f)
    
    grid_cfg = memory['patterns'][0]
    origin = grid_cfg['origin']
    spacing = grid_cfg['spacing']
    rows = grid_cfg['rows']
    cols = grid_cfg['columns']
    
    commands = []
    
    # 1. Create Outer Frame
    commands.append({
        "tool": "create_rectangle",
        "params": {
            "corner1": {"x": -24, "y": 12.3},
            "corner2": {"x": -16, "y": 23.6},
            "layer": "Part"
        }
    })
    
    # 2. Insert Terminal Blocks in 8x4 Grid
    # Logical numbering: Column 1: 1-8, Column 2: 9-16, etc.
    for col in range(cols):
        for row in range(rows):
            x_pos = origin['x'] + (col * spacing['x'])
            y_pos = origin['y'] - (row * spacing['y'])
            
            # Unit ID for numbering
            unit_id = (col * rows) + (row + 1)
            
            # Insert Terminal Block
            commands.append({
                "tool": "insert_block",
                "params": {
                    "blockName": grid_cfg['block_name'],
                    "position": {"x": x_pos, "y": y_pos},
                    "layer": "Connectors"
                }
            })
            
            # Add Label Text (Small offset from block)
            commands.append({
                "tool": "create_text",
                "params": {
                    "position": {"x": x_pos - 0.5, "y": y_pos + 0.1},
                    "text": str(unit_id),
                    "height": 0.15,
                    "layer": "Connectors"
                }
            })
            
    return commands

if __name__ == "__main__":
    cmds = generate_drafting_commands()
    print(f"Generated {len(cmds)} drafting commands.")
    # Log the first few for verification
    for cmd in cmds[:5]:
        print(cmd)

import json

# This script simulates the 'Drawing Engine' logic
# It reads from memory and generates individual line commands

def draw_grid():
    # 1. Load Memory
    with open('drawing_memory.json', 'r') as f:
        memory = json.load(f)
    
    back_view = memory['regions']['BACK_VIEW']
    grid_cfg = back_view['sub_components']['terminal_block_grid']
    
    # 2. Offset for new drawing (further left)
    start_x = -15.0
    start_y = 12.25
    
    rows = grid_cfg['rows']
    cols = grid_cfg['columns']
    w = grid_cfg['cell_size']['width']
    h = grid_cfg['cell_size']['height']
    
    print(f"DEBUG: Drawing {rows}x{cols} grid starting at ({start_x}, {start_y})")
    
    # In a real integration, these would be MCP tool calls
    # For now, we output the commands to be executed
    commands = []
    
    for r in range(rows):
        for c in range(cols):
            # Calculate cell corners
            x0 = start_x + (c * w * 1.5) # Adding some spacing for clarity
            y0 = start_y + (r * h * 1.5)
            x1 = x0 + w
            y1 = y0 + h
            
            # Create 4 lines for each terminal box
            commands.append({"tool": "create_line", "params": {"start": {"x": x0, "y": y0}, "end": {"x": x1, "y": y0}, "layer": "Connectors"}})
            commands.append({"tool": "create_line", "params": {"start": {"x": x1, "y": y0}, "end": {"x": x1, "y": y1}, "layer": "Connectors"}})
            commands.append({"tool": "create_line", "params": {"start": {"x": x1, "y": y1}, "end": {"x": x0, "y": y1}, "layer": "Connectors"}})
            commands.append({"tool": "create_line", "params": {"start": {"x": x0, "y": y1}, "end": {"x": x0, "y": y0}, "layer": "Connectors"}})

    return commands

if __name__ == "__main__":
    cmds = draw_grid()
    # Outputting top 5 commands to verify logic
    for cmd in cmds[:5]:
        print(cmd)
    print(f"... and {len(cmds)-5} more commands.")

import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.getcwd(), 'fu-whisper'))
from fu_relay import FlameRelay

def main():
    relay = FlameRelay()
    
    # Path to the modern handler inside the project directory
    handler_path = "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/123_flame_alpha_2027_romeo/setups/python/flame-utilities/src/fu_bridge_comfyui.py"
    
    code = f"""
import flame
import json

# 1. Target or Create the correct batch group
desktop = flame.projects.current_project.current_workspace.desktop
batch = None
for b in desktop.batch_groups:
    if b.name == 'fu_pybox':
        batch = b
        break

if not batch:
    print("Creating new batch group 'fu_pybox'...")
    batch = desktop.create_batch_group('fu_pybox', reels=['source', 'precomp', 'comp'])

if not batch:
    print("ERROR: Failed to acquire batch group.")
else:
    # 2. Cleanup existing nodes for a fresh setup
    for n in batch.nodes:
        flame.delete(n)

    # 3. Create Source Nodes
    front = batch.create_node("Colour Source")
    front.name = "SOURCE_PLATE"
    front.pos_x = -500
    front.pos_y = 150

    mask = batch.create_node("Colour Source")
    mask.name = "AI_MASK"
    mask.pos_x = -500
    mask.pos_y = -150

    # 4. Create the ComfyUI Bridge (The 'fu_pybox')
    # We use the standard 'Pybox' node type and point it to our v3.13 handler
    print("Instantiating PyBox with handler: {handler_path}")
    bridge = batch.create_node("Pybox", "{handler_path}")
    bridge.name = "COMFYUI_GENERATOR"
    bridge.pos_x = 0
    bridge.pos_y = 0

    # 5. Create Output Node
    output = batch.create_node("Write File")
    output.name = "RESULT_FROM_AI"
    output.pos_x = 500
    output.pos_y = 0

    # 6. Establish Connections
    # Based on fu_bridge_comfyui.py sockets: 0=Front, 2=Matte
    batch.connect_nodes(front, "Result", bridge, "Front")
    batch.connect_nodes(mask, "Result", bridge, "Matte")
    batch.connect_nodes(bridge, "Result", output, "Front")

    # 7. Add Instructional Compasses
    c1 = batch.encompass_nodes([front.name, mask.name])
    c1.name = "1. INPUTS - Plugin source EXRs here"
    
    c2 = batch.encompass_nodes([bridge.name])
    c2.name = "2. AI ENGINE - Set Port and Trigger"
    
    c3 = batch.encompass_nodes([output.name])
    c3.name = "3. FINISHING - Read generated frame"

    # Organize schematic
    batch.organize()
    
    # 8. Focus the batch group so the user can see it
    batch.open()
    
    print("SUCCESS: ComfyUI round-trip setup complete in Batch.")
"""
    result = relay.execute(code)
    if result.get('stdout'):
        print(result['stdout'])
    if result.get('stderr'):
        print(f"Error: {result['stderr']}")
    if result.get('exception'):
        print(f"Exception: {result['exception']}")

if __name__ == "__main__":
    main()
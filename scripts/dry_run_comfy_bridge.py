"""
FU_Bridge_ComfyUI Dry Run Utility
---------------------------------
This script simulates Flame's interaction with the PyBox handler.
It performs the following:
1. Creates a dummy 'Front' EXR file.
2. Generates an initial 'initialize' JSON payload.
3. Runs the handler to verify UI setup.
4. Modifies the payload to trigger the 'Generate AI' action.
5. Runs the handler again to verify execution logic.
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
HANDLER_PATH = REPO_ROOT / "flame-utilities" / "src" / "fu_bridge_comfyui.py"
PYTHON_EXE = REPO_ROOT / ".venv" / "bin" / "python"

def run_test():
    print("--- Starting FU_Bridge_ComfyUI Dry Run ---")
    
    # 1. Create Dummy Input File
    tmp_dir = Path(tempfile.gettempdir())
    dummy_in = tmp_dir / "fu_comfy_in_front.exr"
    with open(dummy_in, "wb") as f:
        f.write(b"DUMMY_EXR_DATA")
    print(f"[1/5] Created dummy input: {dummy_in}")

    # 2. Create Initial Payload (Phase: initialize)
    payload_path = tmp_dir / "mock_flame_payload.json"
    initial_payload = {
        "state_id": "initialize",
        "adsk_metadata": {
            "project": "DryRun_Project",
            "shot_name": "test_shot",
            "frame": 101,
            "format": "exr"
        },
        "sockets": {
            "in": [],
            "out": []
        },
        "dynamic_ui": {
            "pages": [],
            "global_elements": {},
            "render_elements": {}
        },
        "message": {
            "error": "",
            "warning": "",
            "notice": "",
            "debug": ""
        }
    }
    
    with open(payload_path, "w") as f:
        json.dump(initial_payload, f, indent=4)
    print(f"[2/5] Generated initial payload: {payload_path}")

    # 3. Run Handler (Initialization Phase)
    print("[3/5] Running handler: initialize -> setup_ui...")
    subprocess.run([str(PYTHON_EXE), str(HANDLER_PATH), str(payload_path)], check=True)

    # 4. Verify UI Setup & Trigger AI
    with open(payload_path, "r") as f:
        payload = json.load(f)
    
    print(f"      Current State: {payload.get('state_id')}")
    print(f"      UI Elements: {list(payload['dynamic_ui']['global_elements'].keys())}")
    
    # Simulate user clicking 'Generate AI' and setting state to 'execute'
    if "Generate AI" in payload["dynamic_ui"]["global_elements"]:
        payload["dynamic_ui"]["global_elements"]["Generate AI"]["value"] = True
        payload["state_id"] = "execute"
        with open(payload_path, "w") as f:
            json.dump(payload, f, indent=4)
        print("[4/5] Simulated user 'Generate AI' click.")
    else:
        print("Error: 'Generate AI' button not found in payload!")
        return

    # 5. Run Handler (Execution Phase)
    print("[5/5] Running handler: execute...")
    # This will likely report a 'ComfyUI server not found' error in the JSON, 
    # which proves the logic is reaching the backend communication block.
    subprocess.run([str(PYTHON_EXE), str(HANDLER_PATH), str(payload_path)], check=True)

    # Final Verification
    with open(payload_path, "r") as f:
        final_payload = json.load(f)
    
    status = final_payload["dynamic_ui"]["global_elements"].get("Status", {}).get("value", "Unknown")
    error = final_payload["message"].get("error", "")
    
    print("\n--- Dry Run Results ---")
    print(f"Final Status: {status}")
    if error:
        print(f"Captured Error (Expected): {error}")
    
    dummy_out = tmp_dir / "fu_comfy_out_result.exr"
    if dummy_out.exists():
        print(f"Success: Output file generated (Simulation Path): {dummy_out}")
    else:
        print("Note: Output file not generated (this is expected if server check failed).")

if __name__ == "__main__":
    run_test()

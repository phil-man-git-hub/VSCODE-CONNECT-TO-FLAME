"""
FU_ML_Sharp Dry Run Utility
---------------------------
This script simulates Flame's interaction with the SHARP PyBox handler.
It performs the following:
1. Creates a dummy 'Front' EXR file.
2. Generates an initial 'initialize' JSON payload.
3. Runs the handler to verify UI setup and socket definition.
4. Modifies the payload to trigger the 'Generate 3D' action.
5. Runs the handler again to verify execution orchestration.
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
HANDLER_PATH = REPO_ROOT / "flame-utilities" / "src" / "fu_ml_sharp.py"
PYTHON_EXE = REPO_ROOT / ".venv" / "bin" / "python"

def run_test():
    print("--- Starting FU_ML_Sharp Dry Run ---")
    
    # 1. Create Dummy Input File
    tmp_dir = Path(tempfile.gettempdir())
    dummy_in = tmp_dir / "fu_sharp_in_front.exr"
    with open(dummy_in, "wb") as f:
        f.write(b"DUMMY_EXR_DATA_FOR_SHARP")
    print(f"[1/5] Created dummy input: {dummy_in}")

    # 2. Create Initial Payload (Phase: initialize)
    payload_path = tmp_dir / "mock_sharp_payload.json"
    initial_payload = {
        "state_id": "initialize",
        "adsk_metadata": {
            "project": "Sharp_Test_Project",
            "shot_name": "reconstruct_v01",
            "frame": 1,
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

    # 4. Verify UI Setup & Trigger Action
    with open(payload_path, "r") as f:
        payload = json.load(f)
    
    print(f"      Current State: {payload.get('state_id')}")
    print(f"      UI Elements: {list(payload['dynamic_ui']['global_elements'].keys())}")
    print(f"      Output Modes: {payload['dynamic_ui']['render_elements'].get('Output Mode', {}).get('items')}")
    
    # Simulate user selecting 'PLY Cloud' and clicking 'Generate 3D'
    if "Generate 3D" in payload["dynamic_ui"]["global_elements"]:
        payload["dynamic_ui"]["global_elements"]["Generate 3D"]["value"] = True
        payload["dynamic_ui"]["render_elements"]["Output Mode"]["value"] = 1 # Index 1 is PLY Cloud
        payload["state_id"] = "execute"
        # We also simulate a 'process' block being present as if Flame is rendering/displaying result
        payload["process"] = {"params": {"quality": 0}}
        
        with open(payload_path, "w") as f:
            json.dump(payload, f, indent=4)
        print("[4/5] Simulated user selection: Mode=PLY Cloud, Action=Generate.")
    else:
        print("Error: 'Generate 3D' button not found!")
        return

    # 5. Run Handler (Execution Phase)
    print("[5/5] Running handler: execute...")
    # This will likely report an error because 'sharp' binary is not installed in this CLI environment,
    # which proves the logic is correctly attempting to call the backend.
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
    
    print(f"Final State ID: {final_payload.get('state_id')}")

if __name__ == "__main__":
    run_test()

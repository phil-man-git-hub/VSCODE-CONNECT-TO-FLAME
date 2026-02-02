"""
FU_ML_Sharp
-----------
Version: 1.0.1
SDK: fu_pybox_v3_13

PyBox handler for Apple's SHARP (Sharp Monocular View Synthesis).
"""

import sys
import os
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional

def find_toolkit_root() -> Path:
    """Finds the flame-utilities root even if executed from /var/tmp/."""
    # 1. Try relative to this file
    try_path = Path(__file__).resolve().parent.parent
    if (try_path / "lib" / "fu_pybox_v3_13.py").exists():
        return try_path
    
    # 2. Scan sys.path
    for p in sys.path:
        if p.endswith("flame-utilities") and os.path.isdir(p):
            return Path(p)
            
    # 3. Scan standard Flame paths
    search_bases = [
        "/opt/Autodesk/shared/python",
        "/opt/Autodesk/project",
        "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects"
    ]

    for base in search_bases:
        base_path = Path(base)
        if not base_path.exists():
            continue
        for found in base_path.rglob("flame-utilities"):
            if (found / "lib" / "fu_pybox_v3_13.py").exists():
                return found
                
    return try_path

# Initialize Paths
REPO_ROOT = find_toolkit_root()
LIB_PATH = REPO_ROOT / "lib"
AI_LIB_PATH = LIB_PATH / "ai" / "fu-ml-sharp"

# Ensure they are in sys.path
if str(LIB_PATH) not in sys.path:
    sys.path.append(str(LIB_PATH))
if str(AI_LIB_PATH) not in sys.path:
    sys.path.append(str(AI_LIB_PATH))

import fu_pybox_v3_13 as pybox
try:
    from fu_ml_sharp_client import SharpClient, get_sharp_status
except ImportError:
    SharpClient = None


class SharpBridge(pybox.BaseClass):
    """PyBox handler for SHARP 3D integration."""

    def initialize(self) -> None:
        """Phase 1: Define sockets and image format."""
        self.set_img_format("exr")
        img_ext = self.adsk_metadata.get("format", "exr")
        
        # Define temporary frame paths
        tmp_dir = Path(tempfile.gettempdir())
        
        # Inputs (Flame writes these)
        self.set_in_socket(0, "Front", tmp_dir / f"fu_sharp_in_front.{img_ext}")

        # Outputs (Flame reads these)
        # Note: Primary output is the Result frame (Depth or Render)
        self.set_out_socket(0, "Result", tmp_dir / f"fu_sharp_out_result.{img_ext}")
        
        # We can also output the PLY cloud to a known path for Action import
        self.ply_path = tmp_dir / "fu_sharp_out_cloud.ply"

        self.set_state_id("setup_ui")
        self.setup_ui()

    def setup_ui(self) -> None:
        """Phase 2: Build the SHARP control interface."""
        
        # 1. Output Mode Selection
        output_modes = ["Depth Map", "PLY Cloud", "Turntable Render"]
        mode_sel = {
            "type": "Pup",
            "name": "Output Mode",
            "items": output_modes,
            "value": 0,
            "row": 0, "col": 0
        }

        # 2. Path to 'sharp' binary
        bin_path_field = pybox.create_text_field("Binary Path", value="sharp", row=1, col=0)

        # 3. Status Display
        status_field = pybox.create_text_field("Status", value="Idle", row=1, col=1)

        # 4. Trigger Action
        generate_btn = pybox.create_toggle_button("Generate 3D", value=False, row=0, col=1)

        # 5. Define Layout
        page = pybox.create_page("ML SHARP", "Settings", "Action")
        self.set_ui_pages(page)
        
        self.add_global_elements(bin_path_field, generate_btn, status_field)
        self.add_render_elements(mode_sel)

        self.set_state_id("execute")

    def execute(self) -> None:
        """Phase 3: Trigger SHARP inference and handle results."""
        if not self.is_processing():
            return

        gen_active = self.dynamic_ui["global_elements"].get("Generate 3D", {}).get("value", False)
        
        if gen_active:
            self._update_status("Starting Reconstruction...")
            self._run_sharp_inference()
            self.dynamic_ui["global_elements"]["Generate 3D"]["value"] = False

    def _update_status(self, msg: str) -> None:
        self.dynamic_ui["global_elements"]["Status"]["value"] = msg

    def _run_sharp_inference(self) -> None:
        """Technical orchestration with the SHARP worker."""
        bin_path = self.dynamic_ui["global_elements"]["Binary Path"]["value"]
        
        if not SharpClient:
            self.set_error_msg("Error: SHARP Client libraries not found.")
            return

        client = SharpClient(bin_path=bin_path)
        
        # 1. Verify Environment
        if not client.is_available():
            self.set_error_msg(f"Error: 'sharp' binary not found. Check your path or .venv.")
            return

        # 2. Path references
        in_path = Path(self.sockets["in"][0]["path"])
        out_result_path = Path(self.sockets["out"][0]["path"])
        
        if not in_path.exists():
            self.set_error_msg(f"Error: Input frame not found at {in_path}")
            return

        # Create a working directory for SHARP outputs
        work_dir = Path(tempfile.gettempdir()) / "fu_sharp_work"
        work_dir.mkdir(parents=True, exist_ok=True)

        try:
            # 3. Trigger Prediction
            self._update_status("AI Reconstructing...")
            mode_idx = self.dynamic_ui["render_elements"]["Output Mode"]["value"]
            mode_name = self.dynamic_ui["render_elements"]["Output Mode"]["items"][mode_idx]
            
            render_required = (mode_name != "PLY Cloud")
            
            results = client.predict(
                input_image=in_path,
                output_dir=work_dir,
                render=render_required
            )

            # 4. Finalize Output for Flame
            self._update_status("Finalizing Result...")
            
            if mode_name == "Depth Map" and results.get("depth_map"):
                shutil.copy(results["depth_map"], out_result_path)
            elif mode_name == "Turntable Render" and results.get("renders"):
                # Copy the first turntable frame
                shutil.copy(results["renders"][0], out_result_path)
            elif mode_name == "PLY Cloud" and results.get("splat_ply"):
                # PLY doesn't go to the image socket, but we copy it to the fixed path
                # so the artist can load it into Action.
                shutil.copy(results["splat_ply"], self.ply_path)
                # We still need to write something to the Result socket to satisfy Flame
                # so we just copy the input as a placeholder.
                shutil.copy(in_path, out_result_path)
                self.set_error_msg(f"PLY Cloud generated at {self.ply_path}")

            self._update_status("Done.")
            
        except Exception as e:
            self.set_error_msg(f"SHARP Error: {str(e)}")
            self._update_status("Error")

def _main(argv: list[str]) -> None:
    if not argv:
        sys.exit(1)

    handler = SharpBridge(argv[0])
    handler.dispatch()
    handler.write_to_disk()

if __name__ == "__main__":
    _main(sys.argv[1:])

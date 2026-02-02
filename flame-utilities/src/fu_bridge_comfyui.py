"""
FU_Bridge_ComfyUI
-----------------
Version: 1.1.2
SDK: fu_pybox_v3_13

This handler bridges Autodesk Flame with ComfyUI.
"""

import sys
import os
import tempfile
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional

def find_toolkit_root() -> Path:
    """Finds the flame-utilities root even if executed from /var/tmp/."""
    # 1. Try relative to this file
    try_path = Path(__file__).resolve().parent.parent
    if (try_path / "lib" / "fu_pybox_v3_13.py").exists():
        return try_path
    
    # 2. Scan sys.path (in case fu_activate added it)
    for p in sys.path:
        if p.endswith("flame-utilities") and os.path.isdir(p):
            return Path(p)
            
    # 3. Scan standard Flame project and shared paths
    search_bases = [
        "/opt/Autodesk/shared/python",
        "/opt/Autodesk/project",
        "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects"
    ]

    for base in search_bases:
        base_path = Path(base)
        if not base_path.exists():
            continue
        # Find all 'flame-utilities' directories in these hierarchies
        for found in base_path.rglob("flame-utilities"):
            if (found / "lib" / "fu_pybox_v3_13.py").exists():
                return found
                
    return try_path

# Initialize Paths
REPO_ROOT = find_toolkit_root()
LIB_PATH = REPO_ROOT / "lib"
AI_LIB_PATH = LIB_PATH / "ai" / "fu-comfyui"

# Ensure they are in sys.path
if str(LIB_PATH) not in sys.path:
    sys.path.append(str(LIB_PATH))
if str(AI_LIB_PATH) not in sys.path:
    sys.path.append(str(AI_LIB_PATH))

import fu_pybox_v3_13 as pybox
try:
    from fu_comfyui import ComfyUIClient, get_comfy_status
except ImportError:
    ComfyUIClient = None


class ComfyUIBridge(pybox.BaseClass):
    """PyBox handler for ComfyUI integration."""

    def initialize(self) -> None:
        """Phase 1: Define sockets and image format."""
        self.set_img_format("exr")
        img_ext = self.adsk_metadata.get("format", "exr")
        
        tmp_dir = Path(tempfile.gettempdir())
        
        self.set_in_socket(0, "Front", tmp_dir / f"fu_comfy_in_front.{img_ext}")
        self.set_in_socket(2, "Matte", tmp_dir / f"fu_comfy_in_matte.{img_ext}")

        self.set_out_socket(0, "Result", tmp_dir / f"fu_comfy_out_result.{img_ext}")
        self.set_out_socket(1, "OutMatte", tmp_dir / f"fu_comfy_out_matte.{img_ext}")

        self.set_state_id("setup_ui")
        self.setup_ui()

    def setup_ui(self) -> None:
        """Phase 2: Build the ComfyUI control interface."""
        # 1. Server Configuration (Column 0)
        # TextField with name hides its label and takes full width in Flame
        server_ip = pybox.create_text_field("Server IP", value="127.0.0.1", row=0, col=0)
        server_port = pybox.create_float_numeric("Port", value=8188.0, min_val=1024.0, max_val=65535.0, row=1, col=0)
        
        # 2. Status Display (Column 0 - Read Only Label)
        # TextField with is_field=False acts as a full-width label
        status_field = pybox.create_text_field("Status", value="Idle", row=2, col=0, is_field=False)

        # 3. Workflow Selection (Column 1 - Unnamed for full width)
        # Using new SDK version with isField override
        workflows = ["AI_Clean_Plate", "Background_Extender", "Texture_Synth"]
        workflow_sel = pybox.create_popup_unnamed(workflows, value=0, row=0, col=1)

        # 4. Trigger Action (Column 1 - under Workflow)
        generate_btn = pybox.create_toggle_button("Generate AI", value=False, row=1, col=1)

        # 5. Define Layout
        page = pybox.create_page("ComfyUI Bridge", "Server", "Workflow")
        self.set_ui_pages(page)
        
        self.add_global_elements(server_ip, server_port, generate_btn, status_field)
        self.add_render_elements(workflow_sel)

        self.set_state_id("execute")

    def execute(self) -> None:
        """Phase 3: Trigger ComfyUI workflow and monitor results."""
        if not self.is_processing():
            return

        gen_active = self.dynamic_ui["global_elements"].get("Generate AI", {}).get("value", False)
        
        if gen_active:
            self._update_status("Starting...")
            self._run_ai_generation()
            self.dynamic_ui["global_elements"]["Generate AI"]["value"] = False

    def _update_status(self, msg: str) -> None:
        self.dynamic_ui["global_elements"]["Status"]["value"] = msg

    def _run_ai_generation(self) -> None:
        """Full implementation of ComfyUI communication logic."""
        host = self.dynamic_ui["global_elements"]["Server IP"]["value"]
        port = int(self.dynamic_ui["global_elements"]["Port"]["value"])
        server_addr = f"{host}:{port}"
        
        if not ComfyUIClient:
            self.set_error_msg("Error: ComfyUI Client libraries not found.")
            return

        client = ComfyUIClient(server_addr)
        
        # 1. Verify Server
        if not get_comfy_status(server_addr):
            self.set_error_msg(f"Error: ComfyUI server not found at {server_addr}")
            return

        # 2. Metadata for naming
        shot_name = self.get_shot_name() or "unnamed_shot"
        frame_num = self.get_frame()
        
        # 3. Path references
        in_path = Path(self.sockets["in"][0]["path"])
        out_path = Path(self.sockets["out"][0]["path"])
        
        if not in_path.exists():
            self.set_error_msg(f"Error: Input frame not found at {in_path}")
            return

        try:
            # 4. Upload to ComfyUI
            self._update_status("Uploading...")
            upload_name = f"flame_{shot_name}_{frame_num:04d}.exr"
            client.upload_image(str(in_path), upload_name)

            # 5. Load Workflow Template
            # Access the unnamed popup using the empty string key
            template_name = self.dynamic_ui["render_elements"][""]["items"][self.dynamic_ui["render_elements"][""]["value"]]
            template_path = REPO_ROOT / "lib" / "ai" / "fu-comfyui" / "templates" / f"{template_name}.json"
            
            if not template_path.exists():
                self.set_error_msg(f"Error: Workflow template not found: {template_path.name}")
                # Fallback to simulated passthrough for testing
                import shutil
                shutil.copy(in_path, out_path)
                return

            with open(template_path, 'r') as f:
                prompt = json.load(f)

            # 6. Map Flame data to Workflow
            for node_id, node_data in prompt.items():
                node_title = node_data.get('_meta', {}).get('title', '')
                if node_title == "flame_input":
                    node_data['inputs']['image'] = upload_name
                elif node_title == "flame_output":
                    if 'path' in node_data['inputs']:
                        node_data['inputs']['path'] = str(out_path)

            # 7. Execute & Wait
            self._update_status("Executing AI...")
            history = client.run_workflow(prompt)
            
            # 8. Fetch Result
            if not out_path.exists():
                self._update_status("Fetching Result...")
                for node_id, node_output in history.get('outputs', {}).items():
                    if 'images' in node_output:
                        img_data = node_output['images'][0]
                        binary = client.get_image(img_data['filename'], img_data['subfolder'], img_data['type'])
                        with open(out_path, 'wb') as f:
                            f.write(binary)
                        break

            self._update_status("Done.")
            
        except Exception as e:
            self.set_error_msg(f"ComfyUI Error: {str(e)}")
            self._update_status("Error")

def _main(argv: list[str]) -> None:
    if not argv:
        sys.exit(1)

    handler = ComfyUIBridge(argv[0])
    handler.dispatch()
    handler.write_to_disk()

if __name__ == "__main__":
    _main(sys.argv[1:])

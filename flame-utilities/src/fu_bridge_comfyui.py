"""
FU_Bridge_ComfyUI
-----------------
Version: 1.1.0
SDK: fu_pybox_v3_13

This handler bridges Autodesk Flame with ComfyUI. It allows Flame to send 
rendered frames (EXR) to ComfyUI, trigger a specific workflow, and read 
the results back into the Batch/Timeline pipeline.
"""

import sys
import os
import tempfile
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add lib and internal ai libs to path
REPO_ROOT = Path(__file__).parent.parent
LIB_PATH = REPO_ROOT / "lib"
AI_LIB_PATH = LIB_PATH / "ai" / "fu-comfyui"

sys.path.append(str(LIB_PATH))
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
        # 1. Server Configuration
        server_addr = pybox.create_float_numeric("Server Port", value=8188.0, min_val=1024.0, max_val=65535.0, row=0, col=0)
        
        # 2. Workflow Selection
        workflows = ["AI_Clean_Plate", "Background_Extender", "Texture_Synth"]
        workflow_sel = {
            "type": "Pup",
            "name": "Workflow",
            "items": workflows,
            "value": 0,
            "row": 1, "col": 0
        }

        # 3. Status Display (Read-Only text field)
        status_field = pybox.create_text_field("Status", value="Idle", row=1, col=1)

        # 4. Trigger Action
        generate_btn = pybox.create_toggle_button("Generate AI", value=False, row=0, col=1)

        # 5. Define Layout
        page = pybox.create_page("ComfyUI Bridge", "Server", "Workflow")
        self.set_ui_pages(page)
        
        self.add_global_elements(server_addr, generate_btn, status_field)
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
        # Note: In a real PyBox session, this won't update the UI until write_to_disk is called
        # but it helps for internal tracking and logging.

    def _run_ai_generation(self) -> None:
        """Full implementation of ComfyUI communication logic."""
        server_port = int(self.dynamic_ui["global_elements"]["Server Port"]["value"])
        server_addr = f"127.0.0.1:{server_port}"
        
        if not ComfyUIClient:
            self.set_error_msg("Error: ComfyUI Client libraries not found.")
            return

        client = ComfyUIClient(server_addr)
        
        # 1. Verify Server
        if not get_comfy_status(server_addr):
            self.set_error_msg(f"Error: ComfyUI server not found at {server_addr}")
            return

        # 2. Get Metadata for naming
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
            # For this logic, we assume templates are stored in fu-comfyui/templates/
            template_name = self.dynamic_ui["render_elements"]["Workflow"]["items"][self.dynamic_ui["render_elements"]["Workflow"]["value"]]
            template_path = REPO_ROOT.parent / "fu-comfyui" / "templates" / f"{template_name}.json"
            
            if not template_path.exists():
                self.set_error_msg(f"Error: Workflow template not found: {template_path.name}")
                # Fallback to simulated passthrough for testing
                import shutil
                shutil.copy(in_path, out_path)
                return

            with open(template_path, 'r') as f:
                prompt = json.load(f)

            # 6. Map Flame data to Workflow
            # We assume nodes are tagged with names 'flame_input' and 'flame_output'
            for node_id, node_data in prompt.items():
                node_title = node_data.get('_meta', {}).get('title', '')
                if node_title == "flame_input":
                    node_data['inputs']['image'] = upload_name
                elif node_title == "flame_output":
                    # We inject the absolute output path if the ComfyUI node supports it, 
                    # otherwise we'll fetch it after generation.
                    if 'path' in node_data['inputs']:
                        node_data['inputs']['path'] = str(out_path)

            # 7. Execute & Wait
            self._update_status("Executing AI...")
            # Note: client.run_workflow uses WebSockets to wait for completion
            # This is a blocking call in the execute() phase, which is acceptable for PyBox
            history = client.run_workflow(prompt)
            
            # 8. Fetch Result (if not already written to out_path by a custom node)
            if not out_path.exists():
                self._update_status("Fetching Result...")
                # Find the output node's filename in history
                # (Simplified extraction logic)
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

def _main(argv: list[str]) -> None:
    if not argv:
        sys.exit(1)

    handler = ComfyUIBridge(argv[0])
    handler.dispatch()
    handler.write_to_disk()

if __name__ == "__main__":
    _main(sys.argv[1:])

"""
Modernized No-Op (Passthrough) PyBox Handler
--------------------------------------------
Version: 3.13.0
SDK: fu_pybox_v3_13

This handler demonstrates the simplest possible PyBox v3.13 implementation.
It sets up input/output sockets for Front and Matte passes and performs 
a direct passthrough by pointing the output sockets to the input file paths.
"""

import sys
import os
from pathlib import Path
import tempfile

# Add lib directory to path to import the modern SDK
sys.path.append(str(Path(__file__).parent.parent / "lib"))
import fu_pybox_v3_13 as pybox

class NoOpModern(pybox.BaseClass):
    """
    Passthrough handler. 
    Flame writes 'Front' -> ComfyUI/External -> Flame reads 'Result'.
    In this No-Op, we just tell Flame to read exactly what it wrote.
    """

    def initialize(self) -> None:
        # Set high-fidelity format for passthrough
        self.set_img_format("exr")
        img_ext = self.adsk_metadata.get("format", "exr")
        
        # Define temporary paths for the frames
        # Using pathlib for cleaner path construction
        tmp_dir = Path(tempfile.gettempdir())
        
        # Setup Inputs (What Flame writes)
        self.set_in_socket(0, "Front", tmp_dir / f"fu_in_front.{img_ext}")
        self.set_in_socket(2, "Matte", tmp_dir / f"fu_in_matte.{img_ext}")

        # Setup Outputs (What Flame reads)
        # Note: We point outputs to inputs to simulate a passthrough
        self.set_out_socket(0, "Result", tmp_dir / f"fu_in_front.{img_ext}")
        self.set_out_socket(1, "OutMatte", tmp_dir / f"fu_in_matte.{img_ext}")

        # Advance to UI setup phase
        self.set_state_id("setup_ui")
        self.setup_ui()

    def setup_ui(self) -> None:
        """
        No specific UI needed for a passthrough, but we could add a 
        'Enabled' toggle here if we wanted.
        """
        # Advance to execution phase
        self.set_state_id("execute")

    def execute(self) -> None:
        """
        No processing needed. Flame will simply read the 'Result' socket
        path defined in initialize().
        """
        pass

    def teardown(self) -> None:
        """Cleanup logic if needed."""
        pass

def _main(argv: list[str]) -> None:
    if not argv:
        print("Usage: python fu_pybox_no_op_v3.py <payload_json>")
        sys.exit(1)

    # 1. Initialize with the payload path
    handler = NoOpModern(argv[0])

    # 2. Dispatch to the current state logic
    handler.dispatch()

    # 3. Commit changes back to disk
    handler.write_to_disk()

if __name__ == "__main__":
    _main(sys.argv[1:])

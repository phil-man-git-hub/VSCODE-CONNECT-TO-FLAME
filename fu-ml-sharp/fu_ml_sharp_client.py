import subprocess
import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Union

# Setup logging
logging.basicConfig(level=logging.INFO, format='[fu_ml_sharp][%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class SharpClient:
    """
    Technical bridge for Apple's SHARP (Sharp Monocular View Synthesis).
    Wraps the 'sharp' CLI tool to provide 3D reconstruction services to Flame.
    """

    def __init__(self, bin_path: str = "sharp", venv_path: Optional[str] = None):
        """
        Args:
            bin_path: The name or absolute path of the 'sharp' executable.
            venv_path: Optional path to the virtual environment containing SHARP.
        """
        self.bin_path = bin_path
        self.venv_path = venv_path

    def is_available(self) -> bool:
        """Checks if the SHARP CLI is accessible in the environment."""
        try:
            cmd = [self.bin_path, "--help"]
            # We use a short timeout to prevent blocking if the binary is misbehaving
            subprocess.run(cmd, capture_output=True, check=True, timeout=5.0)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def predict(
        self, 
        input_image: Union[str, Path], 
        output_dir: Union[str, Path], 
        render: bool = True,
        checkpoint: Optional[Union[str, Path]] = None
    ) -> Dict[str, Any]:
        """
        Triggers the 3D reconstruction process.
        
        Args:
            input_image: Path to the 2D frame (EXR/JPG/PNG).
            output_dir: Where to save the .ply splat and renders.
            render: If True, also generates turntable/multiview renders.
            checkpoint: Optional path to specific model weights.
            
        Returns:
            A dictionary containing paths to the generated assets.
        """
        input_path = Path(input_image)
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        # Basic command structure based on research
        cmd = [self.bin_path, "predict", "-i", str(input_path), "-o", str(out_path)]
        
        if render:
            cmd.append("--render")
        
        if checkpoint:
            cmd.extend(["-c", str(checkpoint)])

        logger.info(f"Triggering SHARP prediction: {' '.join(cmd)}")
        
        try:
            # SHARP inference is generally very fast (< 1s), but we allow for 
            # more time for rendering passes.
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60.0)
            logger.info("SHARP prediction completed successfully.")
            
            return self._scan_results(out_path)
            
        except subprocess.CalledProcessError as e:
            logger.error(f"SHARP failed with exit code {e.returncode}")
            logger.error(f"Stderr: {e.stderr}")
            raise RuntimeError(f"SHARP inference failed: {e.stderr}")
        except subprocess.TimeoutExpired:
            logger.error("SHARP inference timed out after 60 seconds.")
            raise RuntimeError("SHARP inference timed out.")

    def _scan_results(self, output_dir: Path) -> Dict[str, Any]:
        """Scans the output directory to identify generated assets."""
        results = {
            "splat_ply": None,
            "renders": [],
            "depth_map": None
        }

        # Look for the .ply file (The Gaussian Splat)
        ply_files = list(output_dir.glob("*.ply"))
        if ply_files:
            results["splat_ply"] = str(ply_files[0])

        # Look for rendered images
        image_extensions = {".png", ".jpg", ".exr"}
        for f in output_dir.rglob("*"):
            if f.suffix.lower() in image_extensions:
                # Heuristic: identify depth maps by name
                if "depth" in f.name.lower():
                    results["depth_map"] = str(f)
                else:
                    results["renders"].append(str(f))

        return results

def get_sharp_status(bin_path: str = "sharp") -> bool:
    """Helper for fu_whisper to check if the local SHARP worker is ready."""
    client = SharpClient(bin_path=bin_path)
    return client.is_available()

# Understanding Apple SHARP (Single-Image to 3D)

## Overview
SHARP (Sharp Monocular View Synthesis) is a research project by Apple that enables the reconstruction of photorealistic 3D scenes from a single 2D image in under a second.

## Architecture
- **Technology:** 3D Gaussian Splatting (3DGS).
- **Inference Engine:** PyTorch-based, utilizing a feed-forward transformer architecture to predict Gaussian parameters.
- **Hardware Support:** Native support for Apple Silicon (MPS) and CUDA.

## Command Line Interface (CLI)
The primary way to interact with the model is via the `sharp` command:
```bash
sharp predict -i <input_image> -o <output_directory> --render
```
- `-i`: Path to input image (e.g., .exr, .jpg, .png).
- `-o`: Directory where the 3D data (.ply) and renders will be stored.
- `--render`: Triggers a rasterization pass to generate turntable or multiview images.

## Integration Potential for Flame
- **Input:** Flame can provide 16-bit Float EXR frames.
- **Output:** The resulting `.ply` files can be converted or interpreted by Flame's Action node as point clouds.
- **Speed:** Sub-second inference makes it suitable for interactive Batch workflows.

## Technical Requirements
- **Python:** 3.10+ (Recommended 3.13 for our suite).
- **PyTorch:** 2.3.1.
- **Dependencies:** `torchvision`, `pillow`, `numpy`, and likely `diff-gaussian-rasterization` for the `--render` pass.

---
*Research conducted on 2026-02-01.*

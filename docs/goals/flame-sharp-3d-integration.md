# Goal: SHARP 3D Integration (Single-Image to 3D)

## Objective
Integrate Apple's **SHARP** (Sharp Monocular View Synthesis) research model into Autodesk Flame using the **`fu_pybox_v3_13`** SDK. This will allow Flame artists to generate high-quality 3D Gaussian Splatting data or detailed depth maps from a single 2D source frame directly within the Batch schematic.

## Rationale
- **Instant Pre-viz:** SHARP can reconstruct a 3D scene in under a second, providing immediate spatial context for VFX artists.
- **Enhanced Relighting:** Extracting high-fidelity monocular depth allows for more accurate relighting in Flame's Action node.
- **Set Extensions:** Rapidly generate turntable references or multiview frames for background extensions without a full photogrammetry session.
- **Local AI Utilization:** Leverages the GPU power of the Flame workstation (MPS on Mac or CUDA on Linux) without needing cloud dependencies.

## Technical Strategy
- **Decoupled Worker:** Run the SHARP inference engine in a standalone environment to manage heavy dependencies (PyTorch).
- **PyBox Interface:** Use a v3.13 handler to provide the UI, handle the EXR input, and read the generated 3D data back into the pipeline.
- **Data Contract:** Prioritize the export of **16-bit Depth Maps** and **PLY Point Clouds** which are natively supported by Flame's Action node.

## Success Metrics
- Successful generation of a PLY point cloud from a single EXR frame inside a PyBox node.
- Sub-2-second round-trip for "Draft" quality reconstruction.
- Consistent metadata tracking (focal length, shot name) from Flame through to the AI output.

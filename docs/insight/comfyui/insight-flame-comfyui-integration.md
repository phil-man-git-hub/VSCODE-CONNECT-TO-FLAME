# Insight: Autodesk Flame & ComfyUI Integration

This document outlines the architectural strategies for connecting Autodesk Flame (a high-end VFX finishing system) with ComfyUI (a modular generative AI engine).

## Integration Philosophy
To maintain the professional standards of a VFX pipeline, the integration must prioritize **High Dynamic Range (HDR) fidelity**, **frame accuracy**, and **stateless execution**.

---

## Tier 1: Shared Storage (The "Pybox" Standard)
**Status: Recommended for Production Finishing**

This method mimics the native Flame "Pybox" architecture. It relies on a shared, high-speed filesystem (NVMe or RAM Disk) accessible by both the Flame workstation and the ComfyUI worker.

### Workflow:
1. **Render:** Flame Batch/Timeline renders a segment to a shared directory.
2. **Signal:** `fu_whisper` sends a JSON payload to ComfyUI's `/prompt` endpoint.
3. **Reference:** The JSON contains the *absolute file path* to the image.
4. **Custom Node:** ComfyUI uses a custom node (e.g., `LoadImageFromPath`) to pull the EXR directly into the tensor graph.
5. **Return:** ComfyUI writes the result to a "results" folder, and Flame reads it back via a Clip node or Write File node.

### Why this is optimal:
- **HDR Preservation:** Supports **16-bit Half-Float OpenEXR**, maintaining ACEScg or ARRI LogC4 color space without clipping.
- **Speed:** Zero network overhead for large 4K/8K frames.
- **Metadata:** Metadata (Timecode, Shot Name) remains synchronized via the sidecar JSON.

---

## Tier 2: API-Stream (HTTP/WebSockets)
**Status: Recommended for Remote/Cloud AI Workers**

Use this when ComfyUI is running on a remote GPU farm or a separate machine without a shared mount point.

### Workflow:
1. **Upload:** `fu_whisper` reads the frame from disk and sends an HTTP `POST` to ComfyUI's `/upload/image` endpoint.
2. **Execute:** Submit the workflow JSON referencing the newly uploaded filename.
3. **Monitor:** Use WebSockets to track progress and retrieve the final binary stream.

### Trade-offs:
- **Format Constraints:** Often limited to 8-bit or 10-bit PNG/WebP to reduce transfer times.
- **Latency:** Dependent on local network speeds (10GbE recommended for VFX).

---

## Tier 3: Live Buffer (NDI / Raw Tensors)
**Status: Experimental / Pre-viz Only**

For real-time "AI Filter" behavior in the Flame viewport.

### Workflow:
- **NDI:** Flame outputs its viewport via an NDI sender. ComfyUI listens via an NDI receiver node, processes the latent noise, and sends it back.
- **Direct Memory:** Using Python's `mmap` or shared shared memory buffers (highly complex implementation).

### Trade-offs:
- **Quality:** Usually restricted to 8-bit sRGB.
- **Stability:** Harder to guarantee frame-accuracy for final renders.

---

## Implementation via `fu_whisper`

The MCP server (`fu_whisper`) should act as the orchestrator. A typical tool call would look like:

```python
# Conceptual fu_whisper tool
def trigger_comfy_workflow(workflow_id, source_frame_path):
    # 1. Read the workflow JSON template
    # 2. Inject source_frame_path into the 'LoadImage' node
    # 3. Post to ComfyUI API
    # 4. Wait for completion
    # 5. Signal Flame to refresh the result clip
```

## Recommended Data Formats
| Purpose | Format | Bit Depth |
| :--- | :--- | :--- |
| **Final Finishing** | OpenEXR | 16-bit Float |
| **Texture Gen** | TIFF or OpenEXR | 16-bit Int/Float |
| **Pre-viz / Speed** | WebP (Lossless) | 8-bit |

---
*Analysis performed on 2026-02-01.*

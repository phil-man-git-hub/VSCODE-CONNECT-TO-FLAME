
# Class: PyHDRNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyNode` (inherits from `PyFlameObject`)
* **Functional Role:** High Dynamic Range (HDR) processing node in the schematic, used for HDR analysis and Dolby Vision workflows.

## Description
Represents an HDR node, providing tools for HDR analysis, trims, and Dolby Vision XML import/export in the node graph.

---


## Methods
### Properties
- `analysis_status(...)` — None( (flame.PyHDRNode)arg1) -> object 
None( (flame.PyHDRNode)arg1) -> object

- `mastering_display_ids(...)` — None( (flame.PyHDRNode)arg1) -> list 
None( (flame.PyHDRNode)arg1) -> list

- `target_display_ids(...)` — None( (flame.PyHDRNode)arg1) -> list 
None( (flame.PyHDRNode)arg1) -> list

- `mastering_display_info(...)` — None( (flame.PyHDRNode)arg1) -> object 
None( (flame.PyHDRNode)arg1) -> object

- `target_display_info(...)` — None( (flame.PyHDRNode)arg1) -> object 
None( (flame.PyHDRNode)arg1) -> object


### Built-in methods
- `analyze(...)` — analyze( (PyHDRNode)arg1 [, (str)analyze_mode='Current Shot']) -> None : 
analyze( (PyHDRNode)arg1 [, (str)analyze_mode='Current Shot']) -> None :
    Perform HDR analysis.

- `keep_analysis(...)` — keep_analysis( (PyHDRNode)arg1) -> None : 
keep_analysis( (PyHDRNode)arg1) -> None :
    Remove the dirty flag from the HDR analysis.

- `reset_analysis(...)` — reset_analysis( (PyHDRNode)arg1) -> None : 
reset_analysis( (PyHDRNode)arg1) -> None :
    Reset the current HDR analysis.

- `interpolate_trims(...)` — interpolate_trims( (PyHDRNode)arg1) -> None : 
interpolate_trims( (PyHDRNode)arg1) -> None :
    Interpolate the current HDR trims.

- `reset_trims(...)` — reset_trims( (PyHDRNode)arg1) -> None : 
reset_trims( (PyHDRNode)arg1) -> None :
    Reset the current HDR trims.

- `export_DolbyVision_xml(...)` — export_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)comment='']) -> None : 
export_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)comment='']) -> None :
    Export the current HDR to a Dolby Vision XML file.

- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None : 
import_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
    Import the current HDR from a Dolby Vision XML file.

- `has_trim(...)` — has_trim( (PyHDRNode)arg1, (int)target_display_id) -> bool : 
has_trim( (PyHDRNode)arg1, (int)target_display_id) -> bool :
    Returns True if the given Target Display ID has trims.

- `l2_from_l8(...)` — l2_from_l8( (PyHDRNode)arg1) -> object : 
l2_from_l8( (PyHDRNode)arg1) -> object :
    Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.

## API Insight

- HDR nodes provide analysis tools (`analyze`, `reset_analysis`, `keep_analysis`) and Dolby Vision XML import/export helpers.
- Call `analyze()` to run an HDR analysis; use `export_DolbyVision_xml()` / `import_DolbyVision_xml()` to exchange metadata files.

**Example:**

```python
# Run HDR analysis and export Dolby Vision XML if available
node.analyze()
if node.analysis_status:
    node.export_DolbyVision_xml('/tmp/hdr_export.xml')
```



# Class: PyHDRTimelineFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyTimelineFX` (inherits from `PyFlameObject`)
* **Functional Role:** Timeline effect for HDR processing, used for HDR analysis and Dolby Vision workflows on the timeline.

## Description
Represents an HDR Timeline FX, providing tools for HDR analysis, trims, and Dolby Vision XML import/export as timeline effects.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyHDRTimelineFX** class represents the HDR Analysis and Trims effect, essential for automating Dolby Vision and HDR workflows.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyHDRTimelineFX | HDR analysis and trim effect. |
| Parent Class  | PyTimelineFX  | Inherits general Timeline FX functionality. |
| Primary Role  | HDR Metadata Management | Programmatic control over analysis and trim curves. |

### HDR-Specific Properties
| Attribute             | Type           | Access     | Description |
|-----------------------|---------------|------------|-------------|
| analysis_status       | str            | Read-only  | Current state of HDR analysis. |
| mastering_display_ids | list of int    | Read-only  | Available Mastering Display IDs. |
| mastering_display_info| dict           | Read-only  | Info about Mastering Displays. |
| target_display_ids    | list of int    | Read-only  | Available Target Display IDs. |
| target_display_info   | dict           | Read-only  | Info about Target Displays. |

### HDR-Specific Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| analyze()             | analyze_mode                     | None      | Perform HDR analysis. |
| export_DolbyVision_xml() | file_name, shot_only, comment  | None      | Export HDR data to Dolby Vision XML. |
| import_DolbyVision_xml() | file_name, mode, shot_idx      | None      | Import HDR data from Dolby Vision XML. |
| reset_analysis()      | None                             | None      | Reset HDR analysis data. |
| reset_trims()         | None                             | None      | Reset HDR trims to neutral values. |
| keep_analysis()       | None                             | None      | Remove 'dirty' flag from analysis. |
| has_trim()            | target_display_id                | bool      | Whether trim metadata is applied. |
| interpolate_trims()   | mode                             | None      | Interpolate HDR trim keyframes. |
| l2_from_l8()          | None                             | dict      | Calculate L2 values from L8 values. |

### Inherited Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| load_setup()          | file_name                        | bool      | Manage FX state. |
| save_setup()          | file_name                        | bool      | Save FX state. |
| slide_keyframes()     | offset, sync                     | None      | Offset keyframed trims. |
| sync_connected_segments() | None                         | None      | Push HDR setup to linked segments. |

### Usage Context
PyHDRTimelineFX is essential for automating HDR analysis, trim control, and Dolby Vision XML exchange in professional workflows.

**Example:**

```python
# Perform analysis and export a Dolby Vision XML for a segment
for segment in sequence.segments:
    for fx in segment.timeline_fx:
        if isinstance(fx, flame.PyHDRTimelineFX):
            fx.analyze()
            fx.export_DolbyVision_xml('/tmp/shot123_dv.xml', shot_only=True, comment='Auto-analyzed')
```


## Methods
### Properties
- `analysis_status(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object 
None( (flame.PyHDRTimelineFX)arg1) -> object

- `mastering_display_ids(...)` — None( (flame.PyHDRTimelineFX)arg1) -> list 
None( (flame.PyHDRTimelineFX)arg1) -> list

- `target_display_ids(...)` — None( (flame.PyHDRTimelineFX)arg1) -> list 
None( (flame.PyHDRTimelineFX)arg1) -> list

- `mastering_display_info(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object 
None( (flame.PyHDRTimelineFX)arg1) -> object

- `target_display_info(...)` — None( (flame.PyHDRTimelineFX)arg1) -> object 
None( (flame.PyHDRTimelineFX)arg1) -> object


### Built-in methods
- `analyze(...)` — analyze( (PyHDRTimelineFX)arg1 [, (str)analyze_mode='Current Shot']) -> None : 
analyze( (PyHDRTimelineFX)arg1 [, (str)analyze_mode='Current Shot']) -> None :
    Perform HDR analysis.

- `keep_analysis(...)` — keep_analysis( (PyHDRTimelineFX)arg1) -> None : 
keep_analysis( (PyHDRTimelineFX)arg1) -> None :
    Remove the dirty flag from the HDR analysis.

- `reset_analysis(...)` — reset_analysis( (PyHDRTimelineFX)arg1) -> None : 
reset_analysis( (PyHDRTimelineFX)arg1) -> None :
    Reset the current HDR analysis.

- `interpolate_trims(...)` — interpolate_trims( (PyHDRTimelineFX)arg1, (str)arg2) -> None : 
interpolate_trims( (PyHDRTimelineFX)arg1, (str)arg2) -> None :
    Interpolate the current HDR trims.

- `reset_trims(...)` — reset_trims( (PyHDRTimelineFX)arg1) -> None : 
reset_trims( (PyHDRTimelineFX)arg1) -> None :
    Reset the current HDR trims.

- `export_DolbyVision_xml(...)` — export_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (bool)shot_only=False [, (str)comment='']]) -> None : 
export_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (bool)shot_only=False [, (str)comment='']]) -> None :
    Export the current HDR to a Dolby Vision XML file.

- `import_DolbyVision_xml(...)` — import_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None : 
import_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
    Import the current HDR from a Dolby Vision XML file.

- `has_trim(...)` — has_trim( (PyHDRTimelineFX)arg1, (int)target_display_id) -> bool : 
has_trim( (PyHDRTimelineFX)arg1, (int)target_display_id) -> bool :
    Returns True if the given Target Display ID has trims.

- `l2_from_l8(...)` — l2_from_l8( (PyHDRTimelineFX)arg1) -> object : 
l2_from_l8( (PyHDRTimelineFX)arg1) -> object :
    Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.



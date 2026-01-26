# Class: PyHDRNode

**Module**: `flame`

Object representing a HDR node.

## Methods
### `analysis_status(...)`

None( (flame.PyHDRNode)arg1) -> object

### `analyze(...)`

analyze( (PyHDRNode)arg1 [, (str)analyze_mode='Current Shot']) -> None :
    Perform HDR analysis.

### `keep_analysis(...)`

keep_analysis( (PyHDRNode)arg1) -> None :
    Remove the dirty flag from the HDR analysis.

### `reset_analysis(...)`

reset_analysis( (PyHDRNode)arg1) -> None :
    Reset the current HDR analysis.

### `interpolate_trims(...)`

interpolate_trims( (PyHDRNode)arg1) -> None :
    Interpolate the current HDR trims.

### `reset_trims(...)`

reset_trims( (PyHDRNode)arg1) -> None :
    Reset the current HDR trims.

### `export_DolbyVision_xml(...)`

export_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)comment='']) -> None :
    Export the current HDR to a Dolby Vision XML file.

### `import_DolbyVision_xml(...)`

import_DolbyVision_xml( (PyHDRNode)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
    Import the current HDR from a Dolby Vision XML file.

### `mastering_display_ids(...)`

None( (flame.PyHDRNode)arg1) -> list

### `target_display_ids(...)`

None( (flame.PyHDRNode)arg1) -> list

### `mastering_display_info(...)`

None( (flame.PyHDRNode)arg1) -> object

### `target_display_info(...)`

None( (flame.PyHDRNode)arg1) -> object

### `has_trim(...)`

has_trim( (PyHDRNode)arg1, (int)target_display_id) -> bool :
    Returns True if the given Target Display ID has trims.

### `l2_from_l8(...)`

l2_from_l8( (PyHDRNode)arg1) -> object :
    Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.


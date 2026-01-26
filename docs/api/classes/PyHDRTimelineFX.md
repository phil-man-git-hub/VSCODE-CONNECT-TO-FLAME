# Class: PyHDRTimelineFX

**Module**: `flame`

Object representing a HDR Timeline FX.

## Methods
### `analysis_status(...)`

None( (flame.PyHDRTimelineFX)arg1) -> object

### `analyze(...)`

analyze( (PyHDRTimelineFX)arg1 [, (str)analyze_mode='Current Shot']) -> None :
    Perform HDR analysis.

### `keep_analysis(...)`

keep_analysis( (PyHDRTimelineFX)arg1) -> None :
    Remove the dirty flag from the HDR analysis.

### `reset_analysis(...)`

reset_analysis( (PyHDRTimelineFX)arg1) -> None :
    Reset the current HDR analysis.

### `interpolate_trims(...)`

interpolate_trims( (PyHDRTimelineFX)arg1, (str)arg2) -> None :
    Interpolate the current HDR trims.

### `reset_trims(...)`

reset_trims( (PyHDRTimelineFX)arg1) -> None :
    Reset the current HDR trims.

### `export_DolbyVision_xml(...)`

export_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (bool)shot_only=False [, (str)comment='']]) -> None :
    Export the current HDR to a Dolby Vision XML file.

### `import_DolbyVision_xml(...)`

import_DolbyVision_xml( (PyHDRTimelineFX)arg1, (str)file_name [, (str)mode='Include Frame Based Transitions Trims' [, (int)shot_idx=0]]) -> None :
    Import the current HDR from a Dolby Vision XML file.

### `mastering_display_ids(...)`

None( (flame.PyHDRTimelineFX)arg1) -> list

### `target_display_ids(...)`

None( (flame.PyHDRTimelineFX)arg1) -> list

### `mastering_display_info(...)`

None( (flame.PyHDRTimelineFX)arg1) -> object

### `target_display_info(...)`

None( (flame.PyHDRTimelineFX)arg1) -> object

### `has_trim(...)`

has_trim( (PyHDRTimelineFX)arg1, (int)target_display_id) -> bool :
    Returns True if the given Target Display ID has trims.

### `l2_from_l8(...)`

l2_from_l8( (PyHDRTimelineFX)arg1) -> object :
    Dictionary containing the L2 values based on L8 values. Not valid in Dolby Vision 2.9.


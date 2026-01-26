# Class: PySegment

**Module**: `flame`

**Inherits from**: [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Segment.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `container_clip` | Return the current Matte mode. |
| `effect_types` | Return a list of available effect types for the segment |
| `effects` | Return a list of PyTimeline FX on the segment. |
| `file_path` | Return the file path of the Segment's source. |
| `groups` | Return a list of PySequenceGroups that contains the segment. |
| `head` | Return the amount of head of the Segment. |
| `markers` | Return a list of the segment's Markers. |
| `matte_channel` | Return the name of the Matte channel. |
| `matte_channels` | Return a list of all Matte channels. |
| `matte_mode` | Return the current Matte mode. |
| `original_source_uid` | Return the Clip's original source UID. |
| `parent` | The parent object of this object. |
| `record_duration` | Return the duration of the Segment. |
| `record_in` | Return the record time in of the Segment. |
| `record_out` | Return the record time out of the Segment. |
| `rgb_channel` | Return the name of the RGB channel. |
| `rgb_channels` | Return a list of all RGB channels |
| `source_audio_track` | Return the audio track of the source. |
| `source_bit_depth` | Return the Clip's bit depth. |
| `source_cached` | Return the Clip's cache status. |
| `source_colour_primaries` | Deduce the Clip's 'colour primaries' export attribute. |
| `source_duration` | Return the duration of the Segment's source. |
| `source_essence_uid` | Return the Clip's essence uid. |
| `source_frame_rate` | Return the Clip's frame rate. |
| `source_has_history` | Return the existence of history inside the Clip. |
| `source_height` | Return the Clip's height. |
| `source_in` | Return the source time in of the Segment. |
| `source_matrix_coefficients` | Deduce the Clip's 'matrix coefficients' export attribute. |
| `source_name` | Return the name of the Segment's source. |
| `source_out` | Return the source time out of the Segment. |
| `source_ratio` | Return the Clip's frame ratio. |
| `source_sample_rate` | Return the Clip's audio sample rate. |
| `source_scan_mode` | Return the Clip's scan mode. |
| `source_transfer_characteristics` | Deduce the Clip's 'transfer characteristics' export attribute. |
| `source_uid` | Return the Clip's source uid. |
| `source_unlinked` | Return the Clip's unlinked status. |
| `source_width` | Return the Clip's width. |
| `start_frame` | Return the start frame of the Segment. |
| `tail` | Return the amount of tail of the Segment. |
| `tape_name` | Return the tape name of the Segment. |
| `type` | Return the Segment type. |
| `version_uid` | Return the current version unique ID. |
| `version_uids` | Return a list of available version unique IDs. |


## Methods
### `change_start_frame`
```python
change_start_frame
```


change_start_frame( (PySegment)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :

    Modify the start frame of the segment.

    Keywords argument:

    start_frame -- New start frame of the segment.

    use_segment_connections -- Sync the start frame of connected segments.

    

---

### `clear_colour`
```python
clear_colour
```


clear_colour( (PySegment)arg1) -> None :

    Clear the colour of the Segment.

---

### `connected_segments`
```python
connected_segments
```


connected_segments( (PySegment)arg1 [, (str)scoping='all reels']) -> object :

    Return a list of the connected segments.

    Keywords argument:

    scoping -- Scopes of the sequences to query (all reels, sequences reels, current reel, current sequence).

     (Default:all reels)

---

### `copy_to_media_panel`
```python
copy_to_media_panel
```


copy_to_media_panel( (PySegment)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :

    Create a new clip with a copy of the PyObject.

    

---

### `create_connection`
```python
create_connection
```


create_connection( (PySegment)arg1) -> None :

    Create a connected segment connection.

---

### `create_effect`
```python
create_effect
```


create_effect( (PySegment)arg1, (str)effect_type [, (str)after_effect_type='']) -> object :

    Add an effect of effect_type on the Segment.

    after_effect_type can be specified to insert the effect at a specific position.

---

### `create_marker`
```python
create_marker
```


create_marker( (PySegment)arg1, (object)location) -> object :

    Create a Marker at the specified location on the Segment.

---

### `create_unlinked_segment`
```python
create_unlinked_segment
```


create_unlinked_segment( (PySegment)arg1 [, (str)source_name='' [, (str)tape_name='' [, (object)start_time=0 [, (object)source_duration=0 [, (object)head=0 [, (str)file_path='' [, (int)source_audio_track=1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='Same As Sequence' [, (str)frame_rate='Same As Sequence' [, (object)timewarp_speed=None]]]]]]]]]]]]]]) -> None :

    Replace the gap with an unlinked source media segment.

    Keywords argument:

    source_name -- Name of the source.

    tape_name -- Tape name of the source.

    start_time -- Start time of the source. Must be a PyTime or a frame number.

    source_duration -- Length of the source. Must be a PyTime, a number of frames, or "Infinite".

    head -- Amount of head media to set on the segment.

    file_path -- File path to the media.

    source_audio_track -- Audio track from the source.

    width -- Width of the video media. (0 to use the sequence width)

    height -- Height of the video media. (0 to use the sequence height)

    ratio -- Frame ratio of the video media. (0.0 to use the sequence ratio)

    bit_depth -- Bit depth of the video media. (0 to use the sequence bit depth)

    scan_mode -- Scan mode of the video media. (P, F1, F2, or Same As Sequence)

    frame_rate -- Frame rate. (60 fps, 59.54 NDF, 59.94 DF, 50 fps, 30 fps, 29.97 NDF, 29.97 DF, 25 fps, 24 fps, 23.976 fps, Same As Sequence)

    timewarp_speed -- When defined, a timewarp is applied to the segment with the percentage of timewarp_speed. For audio segments, the speed must be greater than zero.

    

---

### `duplicate_source`
```python
duplicate_source
```


duplicate_source( (PySegment)arg1) -> None :

    Insure that the segment's source is not shared anymore.

---

### `get_colour_space`
```python
get_colour_space
```


get_colour_space( (PySegment)arg1 [, (PyTime)time=None]) -> str :

    Return the colour space at the requested time. Use record_in when no time is supplied.

---

### `get_metadata`
```python
get_metadata
```


get_metadata( (PySegment)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :

    Return the metadata of the segment.

    Keywords argument:

    key -- Key of the requested metadata. All metadata is returned when not specified.

    time -- Must be a PyTime. If not specified, the segment start time is used.

---

### `match`
```python
match
```


match( (PySegment)arg1, (PyArchiveEntry)destination [, (bool)preserve_handle=False [, (bool)use_sequence_info=True [, (bool)include_nested_content=False [, (bool)include_timeline_fx=False]]]]) -> object :

    Match out the media of the PySegment to the destination.

    Returns a PyClip or a list of PyClip (with the included_nested_content option).

    Keywords argument:

    destination -- The PyObject that acts as the destination.

    preserve_handle -- Prevent the unrolling of the media handles.

    use_sequence_info -- Copy sequence segment information to the new matched clip.

    include_nested_content -- Include all sources found inside a BFX or Matte Container.

    include_timeline_fx -- Copy the Timeline FX present on the original clip to the new matched clip.

    

---

### `remove_connection`
```python
remove_connection
```


remove_connection( (PySegment)arg1) -> None :

    Remove the connected segment connection.

---

### `set_gap_bars`
```python
set_gap_bars
```


set_gap_bars( (PySegment)arg1 [, (str)type='smpte' [, (bool)full_luminance=False [, (float)softness=0.0]]]) -> object :

    Create colour bars segment for the duration of the gap.

    Returns a new PySegment on success.

    Keywords argument:

    type -- smpte or pal.

    full_luminance -- bars created at 100 or 75 percent luminance.

    softness -- softness to apply between the bars.

---

### `set_gap_colour`
```python
set_gap_colour
```


set_gap_colour( (PySegment)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None :

    Create a colour source segment for the duration of the gap, or set the colour of an existing colour source.

---

### `set_matte_channel`
```python
set_matte_channel
```


set_matte_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences' [, (str)matte_mode='Custom Matte']]]]) -> bool :

    Set the Matte channel of the source specified by channel_index or by channel_name if the matte_mode is set to Custom Matte.

    Keywords argument:

    channel_name -- Name of the channel found in matte_channels.

    channel_index -- Index of the channel found in matte_channels.

    scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).

    matte_mode -- Matte origin (Follow RGB, No Matte, Custom Matte).

    

---

### `set_rgb_channel`
```python
set_rgb_channel
```


set_rgb_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences']]]) -> bool :

    Set the RGB channel of the source specified by channel_index or by channel_name

    Keywords argument:

    channel_name -- Name of the channel found in rgb_channels.

    channel_index -- Index of the channel found in rgb_channels.

    scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).

    

---

### `set_version_uid`
```python
set_version_uid
```


set_version_uid( (PySegment)arg1, (str)version_uid [, (str)scope='Follow Source Sharing']) -> bool :

    Set the current version unique ID of the source.

    Keywords argument:

    version_uid -- version unique ID.

    scope -- Scope of the changes ( No Sharing, Follow Source Sharing, Follow Connected Segments).

    

---

### `shared_source_segments`
```python
shared_source_segments
```


shared_source_segments( (PySegment)arg1) -> object :

    Return a list of the segments sharing this segment's source.

---

### `slide_keyframes`
```python
slide_keyframes
```


slide_keyframes( (PySegment)arg1, (int)offset [, (bool)sync=False]) -> bool :

    Slide the keyframes the PySegment.

    Keywords argument:

    offset -- Relative offset to slide the keyframes.

    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

    

---

### `slip`
```python
slip
```


slip( (PySegment)arg1, (int)offset [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]) -> bool :

    Slip the media of the PySegment.

    Keywords argument:

    offset -- Relative offset to slip the media.

    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

---

### `smart_replace`
```python
smart_replace
```


smart_replace( (PySegment)arg1, (PyClip)source_clip) -> None :

    Replace the PySegment by the source_clip segment, including the Timeline FX.

---

### `smart_replace_media`
```python
smart_replace_media
```


smart_replace_media( (PySegment)arg1, (PyClip)source_clip) -> None :

    Replace the media of PySegment by the source_clip segment, leaving the PySegment Timeline FX untouched

---

### `sync_connected_segments`
```python
sync_connected_segments
```


sync_connected_segments( (PySegment)arg1) -> None :

    Sync connected segments with the Timeline FXs of the current segment.

---

### `trim_head`
```python
trim_head
```


trim_head( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :

    Modify the amount of head of the PySegment.

    Keywords argument:

    offset -- Number of frames to add or remove from the head.

    ripple -- Enable to prevent gaps from appearing when performing a trim.

    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

---

### `trim_tail`
```python
trim_tail
```


trim_tail( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :

    Modify the amount of tail of the PySegment.

    Keywords argument:

    offset -- Number of frames to add or remove from the tail.

    ripple -- Enable to prevent gaps from appearing when performing a trim.

    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

---

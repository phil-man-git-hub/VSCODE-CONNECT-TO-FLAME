# Class: PySegment

**Module**: `flame`

Object representing a Segment.

## Methods
### Properties
- `source_name(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_in(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `source_out(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `source_duration(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `source_width(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_height(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_bit_depth(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_ratio(...)` — None( (flame.PySegment)arg1) -> float 
None( (flame.PySegment)arg1) -> float

- `source_scan_mode(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_frame_rate(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_cached(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_has_history(...)` — None( (flame.PySegment)arg1) -> bool 
None( (flame.PySegment)arg1) -> bool

- `source_unlinked(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_sample_rate(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_audio_track(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_essence_uid(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_uid(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `original_source_uid(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `source_colour_primaries(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_transfer_characteristics(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `source_matrix_coefficients(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `tape_name(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `record_in(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `record_out(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `record_duration(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `start_frame(...)` — None( (flame.PySegment)arg1) -> int 
None( (flame.PySegment)arg1) -> int

- `file_path(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `markers(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `effect_types(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `effects(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `groups(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `type(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `head(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `tail(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object

- `rgb_channel(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `matte_channel(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `rgb_channels(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `matte_channels(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `version_uid(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `version_uids(...)` — None( (flame.PySegment)arg1) -> list 
None( (flame.PySegment)arg1) -> list

- `matte_mode(...)` — None( (flame.PySegment)arg1) -> str 
None( (flame.PySegment)arg1) -> str

- `container_clip(...)` — None( (flame.PySegment)arg1) -> object 
None( (flame.PySegment)arg1) -> object


### Built-in methods
- `create_effect(...)` — create_effect( (PySegment)arg1, (str)effect_type [, (str)after_effect_type='']) -> object : 
create_effect( (PySegment)arg1, (str)effect_type [, (str)after_effect_type='']) -> object :
    Add an effect of effect_type on the Segment.
    after_effect_type can be specified to insert the effect at a specific position.

- `create_marker(...)` — create_marker( (PySegment)arg1, (object)location) -> object : 
create_marker( (PySegment)arg1, (object)location) -> object :
    Create a Marker at the specified location on the Segment.

- `create_connection(...)` — create_connection( (PySegment)arg1) -> None : 
create_connection( (PySegment)arg1) -> None :
    Create a connected segment connection.

- `remove_connection(...)` — remove_connection( (PySegment)arg1) -> None : 
remove_connection( (PySegment)arg1) -> None :
    Remove the connected segment connection.

- `sync_connected_segments(...)` — sync_connected_segments( (PySegment)arg1) -> None : 
sync_connected_segments( (PySegment)arg1) -> None :
    Sync connected segments with the Timeline FXs of the current segment.

- `connected_segments(...)` — connected_segments( (PySegment)arg1 [, (str)scoping='all reels']) -> object : 
connected_segments( (PySegment)arg1 [, (str)scoping='all reels']) -> object :
    Return a list of the connected segments.
    Keywords argument:
    scoping -- Scopes of the sequences to query (all reels, sequences reels, current reel, current sequence).
     (Default:all reels)

- `duplicate_source(...)` — duplicate_source( (PySegment)arg1) -> None : 
duplicate_source( (PySegment)arg1) -> None :
    Insure that the segment's source is not shared anymore.

- `shared_source_segments(...)` — shared_source_segments( (PySegment)arg1) -> object : 
shared_source_segments( (PySegment)arg1) -> object :
    Return a list of the segments sharing this segment's source.

- `copy_to_media_panel(...)` — copy_to_media_panel( (PySegment)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object : 
copy_to_media_panel( (PySegment)arg1, (PyArchiveEntry)destination [, (str)duplicate_action='add']) -> object :
    Create a new clip with a copy of the PyObject.

- `trim_head(...)` — trim_head( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool : 
trim_head( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :
    Modify the amount of head of the PySegment.
    Keywords argument:
    offset -- Number of frames to add or remove from the head.
    ripple -- Enable to prevent gaps from appearing when performing a trim.
    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

- `trim_tail(...)` — trim_tail( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool : 
trim_tail( (PySegment)arg1, (int)offset [, (bool)ripple=False [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]]) -> bool :
    Modify the amount of tail of the PySegment.
    Keywords argument:
    offset -- Number of frames to add or remove from the tail.
    ripple -- Enable to prevent gaps from appearing when performing a trim.
    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

- `slip(...)` — slip( (PySegment)arg1, (int)offset [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]) -> bool : 
slip( (PySegment)arg1, (int)offset [, (bool)sync=False [, (str)keyframes_move_mode='Shift']]) -> bool :
    Slip the media of the PySegment.
    Keywords argument:
    offset -- Relative offset to slip the media.
    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.
    keyframes_move_mode -- Select how the animation channels are affected ( Pin, Shift, Prop)

- `slide_keyframes(...)` — slide_keyframes( (PySegment)arg1, (int)offset [, (bool)sync=False]) -> bool : 
slide_keyframes( (PySegment)arg1, (int)offset [, (bool)sync=False]) -> bool :
    Slide the keyframes the PySegment.
    Keywords argument:
    offset -- Relative offset to slide the keyframes.
    sync -- Enable to perform the same operation on the segments that belong to the same sync group as the current PySegment.

- `set_gap_colour(...)` — set_gap_colour( (PySegment)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None : 
set_gap_colour( (PySegment)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None :
    Create a colour source segment for the duration of the gap, or set the colour of an existing colour source.

- `set_gap_bars(...)` — set_gap_bars( (PySegment)arg1 [, (str)type='smpte' [, (bool)full_luminance=False [, (float)softness=0.0]]]) -> object : 
set_gap_bars( (PySegment)arg1 [, (str)type='smpte' [, (bool)full_luminance=False [, (float)softness=0.0]]]) -> object :
    Create colour bars segment for the duration of the gap.
    Returns a new PySegment on success.
    Keywords argument:
    type -- smpte or pal.
    full_luminance -- bars created at 100 or 75 percent luminance.
    softness -- softness to apply between the bars.

- `smart_replace(...)` — smart_replace( (PySegment)arg1, (PyClip)source_clip) -> None : 
smart_replace( (PySegment)arg1, (PyClip)source_clip) -> None :
    Replace the PySegment by the source_clip segment, including the Timeline FX.

- `smart_replace_media(...)` — smart_replace_media( (PySegment)arg1, (PyClip)source_clip) -> None : 
smart_replace_media( (PySegment)arg1, (PyClip)source_clip) -> None :
    Replace the media of PySegment by the source_clip segment, leaving the PySegment Timeline FX untouched

- `match(...)` — match( (PySegment)arg1, (PyArchiveEntry)destination [, (bool)preserve_handle=False [, (bool)use_sequence_info=True [, (bool)include_nested_content=False [, (bool)include_timeline_fx=False]]]]) -> object : 
match( (PySegment)arg1, (PyArchiveEntry)destination [, (bool)preserve_handle=False [, (bool)use_sequence_info=True [, (bool)include_nested_content=False [, (bool)include_timeline_fx=False]]]]) -> object :
    Match out the media of the PySegment to the destination.
    Returns a PyClip or a list of PyClip (with the included_nested_content option).
    Keywords argument:
    destination -- The PyObject that acts as the destination.
    preserve_handle -- Prevent the unrolling of the media handles.
    use_sequence_info -- Copy sequence segment information to the new matched clip.
    include_nested_content -- Include all sources found inside a BFX or Matte Container.
    include_timeline_fx -- Copy the Timeline FX present on the original clip to the new matched clip.

- `clear_colour(...)` — clear_colour( (PySegment)arg1) -> None : 
clear_colour( (PySegment)arg1) -> None :
    Clear the colour of the Segment.

- `set_rgb_channel(...)` — set_rgb_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences']]]) -> bool : 
set_rgb_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences']]]) -> bool :
    Set the RGB channel of the source specified by channel_index or by channel_name
    Keywords argument:
    channel_name -- Name of the channel found in rgb_channels.
    channel_index -- Index of the channel found in rgb_channels.
    scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).

- `set_matte_channel(...)` — set_matte_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences' [, (str)matte_mode='Custom Matte']]]]) -> bool : 
set_matte_channel( (PySegment)arg1 [, (str)channel_name='' [, (int)channel_index=-1 [, (str)scope='Follow Preferences' [, (str)matte_mode='Custom Matte']]]]) -> bool :
    Set the Matte channel of the source specified by channel_index or by channel_name if the matte_mode is set to Custom Matte.
    Keywords argument:
    channel_name -- Name of the channel found in matte_channels.
    channel_index -- Index of the channel found in matte_channels.
    scope -- Scope of the changes ( Follow Preferences, No Sharing, Follow Source Sharing, Follow Connected Segments).
    matte_mode -- Matte origin (Follow RGB, No Matte, Custom Matte).

- `set_version_uid(...)` — set_version_uid( (PySegment)arg1, (str)version_uid [, (str)scope='Follow Source Sharing']) -> bool : 
set_version_uid( (PySegment)arg1, (str)version_uid [, (str)scope='Follow Source Sharing']) -> bool :
    Set the current version unique ID of the source.
    Keywords argument:
    version_uid -- version unique ID.
    scope -- Scope of the changes ( No Sharing, Follow Source Sharing, Follow Connected Segments).

- `get_colour_space(...)` — get_colour_space( (PySegment)arg1 [, (PyTime)time=None]) -> str : 
get_colour_space( (PySegment)arg1 [, (PyTime)time=None]) -> str :
    Return the colour space at the requested time. Use record_in when no time is supplied.

- `create_unlinked_segment(...)` — create_unlinked_segment( (PySegment)arg1 [, (str)source_name='' [, (str)tape_name='' [, (object)start_time=0 [, (object)source_duration=0 [, (object)head=0 [, (str)file_path='' [, (int)source_audio_track=1 [, (int)width=0 [, (int)height=0 [, (float)ratio=0.0 [, (int)bit_depth=0 [, (str)scan_mode='Same As Sequence' [, (str)frame_rate='Same As Sequence' [, (object)timewarp_speed=None]]]]]]]]]]]]]]) -> None : 
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

- `change_start_frame(...)` — change_start_frame( (PySegment)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None : 
change_start_frame( (PySegment)arg1, (int)start_frame [, (bool)use_segment_connections=True]) -> None :
    Modify the start frame of the segment.
    Keywords argument:
    start_frame -- New start frame of the segment.
    use_segment_connections -- Sync the start frame of connected segments.

- `get_metadata(...)` — get_metadata( (PySegment)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object : 
get_metadata( (PySegment)arg1 [, (str)key='' [, (PyTime)time=None]]) -> object :
    Return the metadata of the segment.
    Keywords argument:
    key -- Key of the requested metadata. All metadata is returned when not specified.
    time -- Must be a PyTime. If not specified, the segment start time is used.



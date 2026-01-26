# Class: PySubtitleTrack

**Module**: `flame`

Object representing a Subtitle Track.

## Methods
### Built-in methods
- `export_as_srt_file(...)` — export_as_srt_file( (PySubtitleTrack)arg1, (str)file_name [, (bool)character_based_attributes=True [, (bool)export_colours=False [, (str)exclude_colour='' [, (bool)use_original_colours=False [, (bool)use_original_alignment=False [, (bool)export_alignments=False [, (str)alignment_type='an' [, (str)exclude_alignment='' [, (str)start_timecode='Same as Clip']]]]]]]]]) -> None : 
export_as_srt_file( (PySubtitleTrack)arg1, (str)file_name [, (bool)character_based_attributes=True [, (bool)export_colours=False [, (str)exclude_colour='' [, (bool)use_original_colours=False [, (bool)use_original_alignment=False [, (bool)export_alignments=False [, (str)alignment_type='an' [, (str)exclude_alignment='' [, (str)start_timecode='Same as Clip']]]]]]]]]) -> None :
    Export the Subtitles Track as a SubRip (srt) file.Keyword arguments:
    file_name -- The path and name of the file to write.
    character_based_attributes -- Export the bold, italic, and underline attributes.
    export_colours -- Export colours.
    exclude_colour -- Specify a colour, in hexadecimal or CSS colour name, to ignore.
    use_original_colours -- Reuse hexadecimal or CSS colour names from the imported file.
    use_original_alignment -- Reuse alignment tokens from the imported file .
    export_alignments -- Export alignments.
    alignment_type -- Set to a or an alignment style tokens.
    exclude_alignment -- Specify an alignment to ignore.
    start_timecode -- Specify the timecode mode, Same as Clip or, Relative to Clip Start.



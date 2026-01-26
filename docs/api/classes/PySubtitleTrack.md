
# Class: PySubtitleTrack

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PySequence, PyTrack

## Functional Role & Context
* **Functional Role:** Represents a subtitle track, providing access to subtitle export and management operations.
* **Context:** Used for automating subtitle export, alignment, and color management in the timeline or sequence.

## Description
The PySubtitleTrack class provides programmatic access to subtitle tracks, supporting automation of subtitle export, alignment, and color management in the Flame environment.

---

Object representing a Subtitle Track.

## API Insight
### Autodesk Flame API Insight (2026)

`PySubtitleTrack` is a specialized `PyTrack` that manages subtitle content, language, and text encoding on a sequence timeline. It exposes track-level controls (language, encoding) and inherits standard track methods (`set_muted`, `set_locked`, `segments`).

**Core attributes:**
- `language` (str) — Read/Write, the language code for the track (e.g., 'en', 'fr').
- `encoding_type` (str) — Read/Write, subtitle text encoding (e.g., 'UTF-8').
- `segments` (list of PySegment) — Read-only, subtitle segments on the track.

**Common methods:**
- `set_language(language_code)` — Set the track language.
- `set_encoding_type(encoding)` — Set the subtitle encoding.
- `remove_all_segments()` — Remove all subtitle segments.

**Example:**

```python
# Configure a subtitle track for export
subtitle_track.set_language('fr')
subtitle_track.set_encoding_type('UTF-8')
subtitle_track.export_as_srt_file('/tmp/shot01_fr.srt', character_based_attributes=True, export_colours=False)
```


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



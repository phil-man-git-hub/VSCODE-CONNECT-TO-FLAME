
# Class: PyTimeline

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contains:** PyClip, PySegment, PyTrack, PyTimelineFX, etc.

## Functional Role & Context
* **Functional Role:** Represents the main timeline in Flame, providing access to clips, segments, and timeline navigation.
* **Context:** Used for programmatic access to the timeline, current selection, and navigation in the Flame environment.

## Description
The PyTimeline class provides access to the main timeline, enabling automation of navigation, selection, and editing operations in Flame.

---

This class represents the Timeline.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTimeline` is a stateless utility representing the current timeline UI state and controls (accessed via `flame.timeline`). It's used for navigation, playback, and viewer control.

**Key attributes:** `current_frame`, `sequence`, `selected_segments`, `start_frame`, `end_frame`, `zoom_level`, `vertical_offset`.

**Key methods:** `go_to_frame(frame)`, `go_to_start()`, `go_to_end()`, `set_zoom(zoom_level)`, `center_on_frame(frame)`, `set_start_end(start, end)`, `play()`, `stop()`.

**Example:**

```python
# Jump to frame 100 and start playback
flame.timeline.go_to_frame(100)
flame.timeline.play()
# Check selected segments
for seg in flame.timeline.selected_segments:
    print(seg.attributes.name)
```

## Methods
### Properties
- `clip(...)` — None( (flame.PyTimeline)arg1) -> object 
None( (flame.PyTimeline)arg1) -> object

- `current_segment(...)` — None( (flame.PyTimeline)arg1) -> object 
None( (flame.PyTimeline)arg1) -> object

- `current_marker(...)` — None( (flame.PyTimeline)arg1) -> object 
None( (flame.PyTimeline)arg1) -> object

- `current_effect(...)` — None( (flame.PyTimeline)arg1) -> object 
None( (flame.PyTimeline)arg1) -> object

- `current_transition(...)` — None( (flame.PyTimeline)arg1) -> object 
None( (flame.PyTimeline)arg1) -> object

- `type(...)` — None( (flame.PyTimeline)arg1) -> str 
None( (flame.PyTimeline)arg1) -> str



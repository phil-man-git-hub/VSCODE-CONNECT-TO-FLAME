
# Class: PyTransition

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PyTrack, PyTimeline

## Functional Role & Context
* **Functional Role:** Represents a transition between segments in a track, providing access to type, timing, and editing operations.
* **Context:** Used for programmatic management of transitions, including type, duration, and alignment in the timeline or sequence.

## Description
The PyTransition class provides access to transitions in a track or timeline, enabling automation of transition management, type changes, and timing adjustments in Flame.

---

Object representing a Transition.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTransition` models the cut transition between two adjacent `PySegment` objects on a `PyTrack`. It exposes its type, alignment, timing, and convenience methods to replace or slide the transition and to set dissolve/fade parameters.

**Core attributes:** `type`, `record_time`, `in_offset`, `attributes`.

**Common methods:** `set_transition(type, duration=10, alignment='Centred', in_offset=0)`, `slide(offset, sync=False)`, `set_dissolve_to_from_colour(r,g,b)`, `set_fade_to_from_silence()`.

**Example:**

```python
# Replace a transition with a Dissolve and slide it by 2 frames
transition.set_transition('Dissolve', duration=12)
transition.slide(2)
# Set dissolve to fade to black
transition.set_dissolve_to_from_colour(0.0, 0.0, 0.0)
```

## Methods
### Properties
- `type(...)` — None( (flame.PyTransition)arg1) -> str 
None( (flame.PyTransition)arg1) -> str

- `record_time(...)` — None( (flame.PyTransition)arg1) -> object 
None( (flame.PyTransition)arg1) -> object

- `in_offset(...)` — None( (flame.PyTransition)arg1) -> int 
None( (flame.PyTransition)arg1) -> int


### Built-in methods
- `set_transition(...)` — set_transition( (PyTransition)arg1, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0]]]) -> object : 
set_transition( (PyTransition)arg1, (str)type [, (int)duration=10 [, (str)alignment='Centred' [, (int)in_offset=0]]]) -> object :
    Replace the Transition with another type of Transition.
    Returns the new PyTransition if successful.
    Keywords argument:
    type -- Type of the new Transition.
    duration -- Duration of the new Transition in frames.
    alignment -- Alignment of the new Transition.
    in_offset -- Number of frames on left side of the cut in custom alignment.

- `slide(...)` — slide( (PyTransition)arg1, (int)offset [, (bool)sync=False]) -> bool : 
slide( (PyTransition)arg1, (int)offset [, (bool)sync=False]) -> bool :
    Slide the Transition.
    Keywords argument:
    offset -- Amount of frames to slide the Transition with.
    sync -- Enable to perform the same operation on transitions that belong to the same sync group as the current PyTransition.

- `set_dissolve_to_from_colour(...)` — set_dissolve_to_from_colour( (PyTransition)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None : 
set_dissolve_to_from_colour( (PyTransition)arg1 [, (float)r=0.0 [, (float)g=0.0 [, (float)b=0.0]]]) -> None :
    Make a dissolve transition dissolve to/from a colour.

- `set_fade_to_from_silence(...)` — set_fade_to_from_silence( (PyTransition)arg1) -> None : 
set_fade_to_from_silence( (PyTransition)arg1) -> None :
    Make a fade dip to/from silence.



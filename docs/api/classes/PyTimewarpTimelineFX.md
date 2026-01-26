
# Class: PyTimewarpTimelineFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyTimelineFX
* **Context:** Used for time remapping and speed effects in the timeline.

## Functional Role & Context
* **Functional Role:** Represents a Timewarp effect in the timeline, providing access to speed and timing operations.
* **Context:** Used for automating time remapping and speed changes in timeline effects.

## Description
The PyTimewarpTimelineFX class provides access to timewarp effects in the timeline, enabling automation of speed and timing operations for advanced time effects.

---

Object representing a Timewarp node.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTimewarpTimelineFX` controls retiming, speed curves, and interpolation modes for a segment. Key writable properties include `mode` (Speed, Timing, Duration), `duration`, `frame_interpolation_mode`, `sample_mode`, and `mix_amount`.

**Common attributes & modes:**
- `mode` (str) — 'Speed'|'Timing'|'Duration'
- `duration` (int) — new duration in frames when in 'Duration' mode
- `frame_interpolation_mode` (str) — 'Motion'|'Trails'|'Mix'|'ML(2026)' etc.

**Key methods:** `get_speed(frame)`, `set_speed(frame, new_speed)`, `get_timing(frame)`, `set_timing(frame, new_timing)`, `get_duration_timing(frame)`.

**Example:**

```python
# Set a speed keyframe at the segment's midpoint
mid_frame = (segment.record_in + segment.record_out) // 2
for fx in segment.effects:
    if isinstance(fx, flame.PyTimewarpTimelineFX):
        fx.set_speed(mid_frame, 0.5)  # half-speed
        fx.frame_interpolation_mode = 'ML(2026)'
```


## Methods
### Built-in methods
- `get_speed(...)` — get_speed( (PyTimewarpTimelineFX)arg1, (float)frame) -> float : 
get_speed( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
    Return the speed attribute at the requested frame.

- `set_speed(...)` — set_speed( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_speed) -> None : 
set_speed( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_speed) -> None :
    Set the speed at the requested frame.

- `set_timing(...)` — set_timing( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_timing) -> None : 
set_timing( (PyTimewarpTimelineFX)arg1, (float)frame, (float)new_timing) -> None :
    Set the timing at the requested frame.

- `get_timing(...)` — get_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float : 
get_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
    Return the timing value at the requested frame.

- `get_duration_timing(...)` — get_duration_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float : 
get_duration_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
    Return the timing value for the current frame while in the duration mode.

- `get_speed_timing(...)` — get_speed_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float : 
get_speed_timing( (PyTimewarpTimelineFX)arg1, (float)frame) -> float :
    The timing value for the current frame while in the speed mode.



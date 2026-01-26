
# Class: PyTime

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used throughout Flame for representing time, timecodes, and frame positions.

## Functional Role & Context
* **Functional Role:** Represents a time unit, providing access to frame, timecode, and frame rate information.
* **Context:** Used for time calculations, conversions, and frame-based operations in Flame.

## Description
The PyTime class provides a unified way to represent and manipulate time, timecodes, and frames in the Flame environment.

---

Object representing a time unit

PyTime(timecode, frame_rate)
PyTime(relative_frame)
PyTime(absolute_frame, frame_rate)

## API Insight
### Autodesk Flame API Insight (2026)

`PyTime` is a versatile data object used to represent time in frames or timecode and to convert between representations based on frame rate. It is instantiated either from timecode strings or frame numbers.

**Constructors:**
- `PyTime(timecode, frame_rate)` — from a timecode string and frame rate.
- `PyTime(relative_frame)` — from a relative frame index.
- `PyTime(absolute_frame, frame_rate)` — from an absolute frame number and frame rate.

**Attributes:** `timecode`, `relative_frame`, `absolute_frame`, `frame_rate`, `hours`, `minutes`, `seconds`, `frames`.

**Example:**

```python
# Create a timecode object and inspect components
t = flame.PyTime('01:00:00:00', '24 fps')
print(t.timecode, t.relative_frame, t.frame_rate)
# Perform arithmetic by using frame counts
new_frame = t.relative_frame + 24
t2 = flame.PyTime(new_frame)
```

## Methods
### Properties
- `frame(...)` — None( (flame.PyTime)arg1) -> int 
None( (flame.PyTime)arg1) -> int

- `relative_frame(...)` — None( (flame.PyTime)arg1) -> int 
None( (flame.PyTime)arg1) -> int

- `timecode(...)` — None( (flame.PyTime)arg1) -> str 
None( (flame.PyTime)arg1) -> str

- `frame_rate(...)` — None( (flame.PyTime)arg1) -> object 
None( (flame.PyTime)arg1) -> object



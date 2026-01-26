
# Class: PyTimewarpNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used in Batch and TimelineFX for time remapping and speed effects.

## Functional Role & Context
* **Functional Role:** Represents a Timewarp node, providing access to speed and timing operations in node-based compositing.
* **Context:** Used for automating time remapping and speed changes in Batch and TimelineFX.

## Description
The PyTimewarpNode class provides access to timewarp nodes, enabling automation of speed and timing operations for advanced time effects in node graphs.

---

Object representing a Timewarp node.

## Methods
### Built-in methods
- `get_speed(...)` — get_speed( (PyTimewarpNode)arg1, (float)frame) -> float : 
get_speed( (PyTimewarpNode)arg1, (float)frame) -> float :
    Return the speed attribute at the requested frame.

- `set_speed(...)` — set_speed( (PyTimewarpNode)arg1, (float)frame, (float)new_speed) -> None : 
set_speed( (PyTimewarpNode)arg1, (float)frame, (float)new_speed) -> None :
    Set the speed at the requested frame.

- `set_timing(...)` — set_timing( (PyTimewarpNode)arg1, (float)frame, (float)new_timing) -> None : 
set_timing( (PyTimewarpNode)arg1, (float)frame, (float)new_timing) -> None :
    Set the timing at the requested frame.

- `get_timing(...)` — get_timing( (PyTimewarpNode)arg1, (float)frame) -> float : 
get_timing( (PyTimewarpNode)arg1, (float)frame) -> float :
    Return the timing value at the requested frame.

- `get_duration_timing(...)` — get_duration_timing( (PyTimewarpNode)arg1, (float)frame) -> float : 
get_duration_timing( (PyTimewarpNode)arg1, (float)frame) -> float :
    Return the timing value for the current frame while in the duration mode.

- `get_speed_timing(...)` — get_speed_timing( (PyTimewarpNode)arg1, (float)frame) -> float : 
get_speed_timing( (PyTimewarpNode)arg1, (float)frame) -> float :
    The timing value for the current frame while in the speed mode.

## API Insight

- Timewarp nodes expose `get_speed`/`set_speed` and `get_timing`/`set_timing` APIs for per-frame control of speed and timing values.
- Use `get_*` methods to inspect values and `set_*` to author speed/timing changes; these APIs are safe for automation and non-destructive editing of the node's parameters.

**Example:**

```python
# Set a speed key at frame 100 and read it back
node.set_speed(100, 0.5)
print(node.get_speed(100))
# Set a timing key and verify
node.set_timing(100, 2.0)
print(node.get_timing(100))
```



# Class: PySequenceGroup

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PySequence

## Functional Role & Context
* **Functional Role:** Represents a group of segments within a sequence, allowing batch operations on multiple segments.
* **Context:** Used for organizing, adding, and removing segments in timeline sequences.

## Description
The PySequenceGroup class provides access to segment groups in a sequence, enabling group-based editing and management in the Flame timeline.

---

Object representing a Group in a Sequence.

## Methods
### Properties
- `segments(...)` — None( (flame.PySequenceGroup)arg1) -> list 
None( (flame.PySequenceGroup)arg1) -> list


### Built-in methods
- `add(...)` — add( (PySequenceGroup)arg1, (object)segments) -> None : 
add( (PySequenceGroup)arg1, (object)segments) -> None :
    Adds a PySegment or list of PySegments to the Group.

- `remove(...)` — remove( (PySequenceGroup)arg1, (object)segments) -> None : 
remove( (PySequenceGroup)arg1, (object)segments) -> None :
    Remove a PySegment or list of PySegments from the Group.

## API Insight

- `segments` returns the list of segments in the group; use `add(segments)` and `remove(segments)` to modify membership.
- Methods accept a `PySegment` or a list of `PySegment` objects.

**Example:**

```python
# Add a segment to the group and then remove it
group.add(segment)
group.remove(segment)
```


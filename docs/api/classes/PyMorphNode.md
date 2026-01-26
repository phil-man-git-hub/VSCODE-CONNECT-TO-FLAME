
# Class: PyMorphNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used in Batch and TimelineFX for morphing operations.

## Functional Role & Context
* **Functional Role:** Represents a Morph node, providing access to morphing operations and keyframe management.
* **Context:** Used for automating morph effects, including keyframe and mix curve management in node-based compositing.

## Description
The PyMorphNode class provides programmatic access to morphing operations, supporting automation of mix curves and keyframe management in Flame.

---

Object representing a Morph node.

## Methods
### Built-in methods
- `set_mix_to_range(...)` — set_mix_to_range( (PyMorphNode)arg1) -> None : 
set_mix_to_range( (PyMorphNode)arg1) -> None :
    Move the first and last keyframes of the mix curve to the range's first and last frame.

## API Insight

- The Morph node exposes operations for manipulating mix curves and keyframes; `set_mix_to_range()` is useful for quickly snapping curve endpoints to the clip range.
- This API is safe for automated adjustments of morph parameters and is non-destructive to source media.

**Example:**

```python
# Align mix curve to clip range
node.set_mix_to_range()
```


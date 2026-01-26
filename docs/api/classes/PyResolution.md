
# Class: PyResolution

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Context:** Used for representing and manipulating resolution settings in Flame.

## Functional Role & Context
* **Functional Role:** Represents a resolution, providing access to width, height, bit depth, frame ratio, and scan format.
* **Context:** Used for programmatic access to resolution settings, conversions, and validation in Flame.

## Description
The PyResolution class provides programmatic access to resolution settings, supporting automation of resolution management and validation in the Flame environment.

---

Object representing a resolution

## API Insight
### Autodesk Flame API Insight (2026)

`PyResolution` is a lightweight data object representing width, height, bit depth, frame ratio and scan format. It can be instantiated directly and passed to other API methods (for example when creating sequences or configuring exporters).

**Constructors:**
- `PyResolution()` — default/empty resolution object.
- `PyResolution(width, height, bit_depth, frame_ratio, scan_format)` — full definition.

**Attributes:** `width`, `height`, `bit_depth`, `frame_ratio`, `scan_format`, `pixel_ratio` (read/write).

**Example:**

```python
# Create a custom resolution and use it for an exporter
res = flame.PyResolution(1920, 1080, 10, 16/9.0, 'P')
exporter.output_resolution = res
```

## Methods
### Properties
- `resolution(...)` — None( (flame.PyResolution)arg1) -> str 
None( (flame.PyResolution)arg1) -> str

- `width(...)` — None( (flame.PyResolution)arg1) -> int 
None( (flame.PyResolution)arg1) -> int

- `height(...)` — None( (flame.PyResolution)arg1) -> int 
None( (flame.PyResolution)arg1) -> int

- `frame_ratio(...)` — None( (flame.PyResolution)arg1) -> float 
None( (flame.PyResolution)arg1) -> float

- `scan_mode(...)` — None( (flame.PyResolution)arg1) -> str 
None( (flame.PyResolution)arg1) -> str

- `bit_depth(...)` — None( (flame.PyResolution)arg1) -> int 
None( (flame.PyResolution)arg1) -> int



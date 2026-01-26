
# Class: PyTypeFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyTimelineFX
* **Context:** Used for type/text effects in the timeline.

## Functional Role & Context
* **Functional Role:** Represents a Type Timeline FX, providing access to text layers and type setup operations.
* **Context:** Used for automating text effects, layer management, and type setup in the timeline.

## Description
The PyTypeFX class provides programmatic access to type timeline effects, supporting automation of text layer management and type setup in the Flame environment.

---

Object representing a Type Timeline FX.

## API Insight
### Autodesk Flame API Insight (2026)

`PyTypeTimelineFX` (exposed as `PyTypeFX` in docs) controls advanced text/titling on the timeline. It inherits from `PyTimelineFX` and adds text-layer management, font handling, and motion blur controls.

**Key properties:** `selected_layers` (list), `font` (varies: family/style/path/index), `motion_blur` (bool), `samples` (int), `phase` (float), `shutter` (float), and `attributes`.

**Layer & styling controls:** character-level styling (superscript, subscript, strikeout), masking, and layer axis parameters for position/scale.

**Example:**

```python
# Add a new centre text layer and enable motion blur
type_fx = segment.effects[0]  # assume this is a PyTypeFX
layer = type_fx.add_layer('Centre')
layer.attributes.text = 'Hello Flame'
type_fx.motion_blur = True
type_fx.samples = 8
```

## Methods
### Properties
- `layers(...)` — None( (flame.PyTypeFX)arg1) -> list 
None( (flame.PyTypeFX)arg1) -> list


### Built-in methods
- `add_layer(...)` — add_layer( (PyTypeFX)arg1 [, (str)layer_type='Centre']) -> object : 
add_layer( (PyTypeFX)arg1 [, (str)layer_type='Centre']) -> object :
    Create a new layer.
    Keyword argument:
    layer_type -- Must be one of Left, Centre(default), Right, Roll, or Crawl.

- `append_type_setup(...)` — append_type_setup( (PyTypeFX)arg1, (str)file_name) -> bool : 
append_type_setup( (PyTypeFX)arg1, (str)file_name) -> bool :
    Append a setup to the current Type setup.



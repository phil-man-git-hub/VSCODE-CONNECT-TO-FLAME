
# Class: PyColourMgtTimelineFX

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyTimelineFX` (inherits from `PyFlameObject`)
* **Functional Role:** Timeline effect for color management, used for color space conversions and management on the timeline.

## Description
Represents a Colour Management Timeline FX, providing color space and transform operations as timeline effects.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyClrMgmtTimelineFX** class represents the Colour Management effect applied to a segment on the timeline, providing access to color transformation settings.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyClrMgmtTimelineFX | Colour Management effect on the timeline. |
| Parent Class  | PyTimelineFX  | Inherits general Timeline FX functionality. |
| Location      | Contained by PySegment | Attached to a segment on the timeline. |

### Core Properties
| Attribute             | Type   | Access     | Description |
|-----------------------|--------|------------|-------------|
| input_colour_space    | str    | Read/Write | Input Color Space used by the effect. |
| output_colour_space   | str    | Read/Write | Output Color Space used by the effect. |
| type                  | str    | Read-only  | Always returns 'Colour Management'. |
| attributes            | PyAttribute | Read-only | General object metadata and properties. |

### Key Methods (Inherited)
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| load_setup()          | file_name                        | bool      | Load a saved color management setup. |
| save_setup()          | file_name                        | bool      | Save current color management settings. |
| slide_keyframes()     | offset, sync                     | None      | Slide animated keyframes within the effect. |

### Usage Context
This class is foundational for automating color pipeline tasks, batch-setting color spaces, saving/sharing looks, and color conform during project setup.

**Example:**

```python
# Iterate and set input/output colour spaces on all colour-management FX in a sequence
for segment in sequence.segments:
    for fx in segment.timeline_fx:
        if isinstance(fx, flame.PyColourMgtTimelineFX):
            fx.input_colour_space = 'ALEXA_V3_LogC'
            fx.output_colour_space = 'Rec.709'
            fx.save_setup('/tmp/colour_mgmt_setup.xml')
```


## Methods
### Built-in methods
- `set_context_variable(...)` — set_context_variable( (PyColourMgtTimelineFX)arg1, (str)name, (str)value) -> None : 
set_context_variable( (PyColourMgtTimelineFX)arg1, (str)name, (str)value) -> None :
    Set the value for the specified context variable.

- `get_context_variables(...)` — get_context_variables( (PyColourMgtTimelineFX)arg1) -> dict : 
get_context_variables( (PyColourMgtTimelineFX)arg1) -> dict :
    Get the context variables in a dictionary.

- `import_transform(...)` — import_transform( (PyColourMgtTimelineFX)arg1, (str)file_path) -> None : 
import_transform( (PyColourMgtTimelineFX)arg1, (str)file_path) -> None :
    Import a transform from a file.

- `reset_context_variables(...)` — reset_context_variables( (PyColourMgtTimelineFX)arg1) -> None : 
reset_context_variables( (PyColourMgtTimelineFX)arg1) -> None :
    Reset the context variables to their initial state from the ocio config.




# Class: PyMarker

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyFlameObject`
* **Functional Role:** Represents a Marker, used for marking frames, adding annotations, and synchronizing segments.


## Description
Represents a Marker, providing tools for frame marking, annotation, and segment synchronization in Flame.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyMarker** class provides programmatic access to Markers for annotations and organizational points on clips and sequences.

### Definition & Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyMarker      | Marker object for annotation. |
| Parent Class  | PyFlameObject | Inherits base properties and methods. |
| Purpose       | Annotation    | Represents a Marker placed on a PyClip or PySegment. |

### Unique Attributes
| Attribute         | Type           | Description |
|-------------------|---------------|-------------|
| name              | str            | Name of the Marker. |
| comment           | str            | Comment or description. |
| location          | PyTime         | Start frame/timecode. |
| duration          | PyTime         | Duration of the Marker. |
| colour            | tuple          | Color as (R, G, B) floats (0.0-1.0). |
| colour_label      | str            | Predefined color label. |
| selected          | bool           | Selection status. |
| locked_location   | bool           | Lock status for location. |

### Inherited Properties
| Property          | Description |
|-------------------|-------------|
| attributes        | All scriptable attributes. |
| parent            | Parent object (PyClip or PySegment). |

### Usage Context
Markers are accessed through their parent container (PyClip or PySegment) using properties like markers or selected_markers.

**Example:**

```python
# Access and update markers for the first selected clip
clip = flame.media_panel.selected_entries[0]
for marker in clip.markers:
    print(marker.name, marker.location)
    marker.comment = f"Reviewed by {flame.user.name}"
```

## Attributes
| Attribute         | Type   | Description |
|-------------------|--------|-------------|
| name              | str    | The Marker's name |
| comment           | str    | The Marker's comment |
| location          | PyTime | The Marker's location |
| locked_location   | bool   | Lock the Marker location. Values: True/False |
| duration          | PyTime | The Marker's duration |
| colour            | tuple  | The Marker's colour. Range: (0.0, 0.0, 0.0) to (1.0, 1.0, 1.0) |

---


## Methods
### Properties
- `has_annotations(...)` — None( (flame.PyMarker)arg1) -> bool 
None( (flame.PyMarker)arg1) -> bool


### Built-in methods
- `clear_annotations(...)` — clear_annotations( (PyMarker)arg1) -> None : 
clear_annotations( (PyMarker)arg1) -> None :
    Clear all the annotations from the Marker.

- `sync_connected_segments(...)` — sync_connected_segments( (PyMarker)arg1) -> None : 
sync_connected_segments( (PyMarker)arg1) -> None :
    Push the Segment Marker to connected segments.



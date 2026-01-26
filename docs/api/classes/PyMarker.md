# Class: PyMarker

**Module**: `flame`

**Inherits from**: [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Marker.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `has_annotations` | Returns True when the Marker contains at least one annotation. |
| `parent` | The parent object of this object. |


## Methods
### `clear_annotations`
```python
clear_annotations
```


clear_annotations( (PyMarker)arg1) -> None :

    Clear all the annotations from the Marker.

---

### `sync_connected_segments`
```python
sync_connected_segments
```


sync_connected_segments( (PyMarker)arg1) -> None :

    Push the Segment Marker to connected segments.

---

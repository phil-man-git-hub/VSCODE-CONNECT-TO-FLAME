# Class: PyReelGroup

**Module**: `flame`

**Inherits from**: [PyArchiveEntry](PyArchiveEntry.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Reel Group.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `children` | Return a list of the immediate children of the current object. |
| `parent` | The parent object of this object. |
| `reels` | Return a list of Reel objects that are immediate children of the current object. |


## Methods
### `clear`
```python
clear
```


clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool :

    Clear the Reel Group content.

---

### `clear_colour`
```python
clear_colour
```


clear_colour( (PyArchiveEntry)arg1) -> None :

    Clear the colour of an object in the Media Panel.

---

### `commit`
```python
commit
```


commit( (PyArchiveEntry)arg1) -> None :

    Commit to disk the Media Panel object or its closest container possible.

---

### `create_reel`
```python
create_reel
```


create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object :

    Create a new Reel inside a Reel Group.

---

### `get_wiretap_node_id`
```python
get_wiretap_node_id
```


get_wiretap_node_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.

---

### `get_wiretap_storage_id`
```python
get_wiretap_storage_id
```


get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.

---

### `save`
```python
save
```


save( (PyReelGroup)arg1) -> bool :

    Save the Reel Group to the defined save destination.

---

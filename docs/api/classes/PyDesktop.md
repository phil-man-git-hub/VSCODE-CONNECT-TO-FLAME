# Class: PyDesktop

**Module**: `flame`

**Inherits from**: [PyArchiveEntry](PyArchiveEntry.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Class derived from PyArchiveEntry. This class represents a Desktop.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `batch_groups` | Return a list of Batch Group objects that are immediate children of the current object. |
| `children` | Return a list of the immediate children of the current object. |
| `parent` | The parent object of this object. |
| `reel_groups` | Return a list of Reel Group objects that are immediate children of the current object. |


## Methods
### `clear`
```python
clear
```


clear( (PyDesktop)arg1) -> bool :

    Clear the Desktop.

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

### `create_batch_group`
```python
create_batch_group
```


create_batch_group( (PyDesktop)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object :

    Create a new Batch Group object in the Desktop catalogue.

    Keyword arguments:

    name -- Name of the Batch Group.

    nb_reels -- Number of reels created. *reels* overrides *nb_reels*.

    nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* ovverides *nb_shelf_reels*.

    reels -- A list of reel names. Overrides *nb_reels*.

    shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.

    start_frame -- The Batch Group's start frame. No timecodes, only a frame value.

    duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.

---

### `create_reel_group`
```python
create_reel_group
```


create_reel_group( (PyDesktop)arg1, (str)name) -> object :

    Create a new Reel Group object in the Desktop catalogue.

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


save( (PyDesktop)arg1) -> bool :

    Save the Desktop to the location defined by the *destination* attribute.

---

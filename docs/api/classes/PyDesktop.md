
# Class: PyDesktop

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyArchiveEntry` (inherits from `PyFlameObject`)
* **Functional Role:** Represents the user's current desktop layout, containing folders, reel groups, and reels.


## Description
Represents a Desktop, the top-level container for organizing reels, folders, and batch groups in the user interface.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyDesktop** class represents the main working area in Flame, acting as the root container for all open media, sequences, and batches.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyDesktop     | Represents the Desktop. |
| Parent Class  | PyArchiveEntry| Inherits basic management functions. |
| Primary Role  | Root Container for Active Content | Central access to Batch Groups, Libraries, and Media Panel items. |
| Instantiation | Singleton     | Accessed via flame.desktop. |

### Core Properties
| Attribute         | Type                    | Access     | Description |
|-------------------|------------------------|------------|-------------|
| batch_groups      | list of PyBatch         | Read-only  | All open Batch Groups. |
| libraries         | list of PyLibrary       | Read-only  | All open Libraries. |
| children          | list of PyArchiveEntry  | Read-only  | Immediate items on the Desktop. |
| selected_items    | list of PyArchiveEntry  | Read-only  | Objects currently selected in the UI. |
| parent            | PyWorkspace             | Read-only  | The parent workspace object. |
| attributes        | PyAttribute             | Read-only  | Metadata like name. |

### Key Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| create_batch_group()  | name                             | PyBatch   | Create a new Batch Group. |
| create_folder()       | name                             | PyFolder  | Create a new Folder. |
| create_reel_group()   | name                             | PyReelGroup| Create a new Reel Group. |
| reconnect_selected_clip() | None                         | bool      | Reconnect selected clip to media files. |
| reload_selected_clip()| None                             | bool      | Reload selected clip from disk. |
| get_current_batch_group() | None                         | PyBatch/None| Get the currently active Batch Group. |
| get_item()            | name                             | PyArchiveEntry/None| Retrieve an item by name. |

### Usage Context
PyDesktop is the starting point for scripting tasks involving the user's live work area, such as opening batches or finding selected media items.

**Examples:**

```python
# Reconnect the currently selected clip to its media files
desktop.reconnect_selected_clip()

# Get the currently active Batch Group and print its name
current_batch = desktop.get_current_batch_group()
if current_batch is not None:
    print(current_batch.attributes.name)
```

## Attributes
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| name        | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid         | str    | The unique identifier of an object in the Media Panel. |
| token_name  | str    | The tokenized name of an object in the Media Panel. |
| expanded    | bool   | The expanded state of an object in the Media Panel. Values: True/False |
| colour      | tuple  | The colour of an object in the Media Panel. |

---


## Methods
### Properties
- `children(...)` — None( (flame.PyDesktop)arg1) -> list 
None( (flame.PyDesktop)arg1) -> list

- `batch_groups(...)` — None( (flame.PyDesktop)arg1) -> list 
None( (flame.PyDesktop)arg1) -> list

- `reel_groups(...)` — None( (flame.PyDesktop)arg1) -> list 
None( (flame.PyDesktop)arg1) -> list


### Built-in methods
- `create_reel_group(...)` — create_reel_group( (PyDesktop)arg1, (str)name) -> object : 
create_reel_group( (PyDesktop)arg1, (str)name) -> object :
    Create a new Reel Group object in the Desktop catalogue.

- `save(...)` — save( (PyDesktop)arg1) -> bool : 
save( (PyDesktop)arg1) -> bool :
    Save the Desktop to the location defined by the *destination* attribute.

- `create_batch_group(...)` — create_batch_group( (PyDesktop)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object : 
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

- `clear(...)` — clear( (PyDesktop)arg1) -> bool : 
clear( (PyDesktop)arg1) -> bool :
    Clear the Desktop.



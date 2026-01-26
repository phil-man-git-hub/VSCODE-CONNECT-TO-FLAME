
# Class: PyMediaHubFilesFolder

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents a folder entry in the MediaHub Files tab.

## Description
Provides access to folder entries in the MediaHub Files tab, including file path and metadata.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyMediaHubFilesFolder** class represents a folder (directory) as seen in the MediaHub's Files tab.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyMediaHubFilesFolder | Folder entry in the MediaHub Files tab. |
| Parent Class  | PyArchiveEntry| Inherits archive management methods. |
| Ancestor Class| PyFlameObject | Inherits base properties. |
| Primary Role  | Directory Identification | Absolute file path to the folder. |

### Unique Attributes
| Attribute         | Type           | Access     | Description |
|-------------------|---------------|------------|-------------|
| path              | str            | Read-only  | Absolute file system path of the folder. |

### Inherited Methods
| Method                | Arguments                        | Description |
|-----------------------|----------------------------------|-------------|
| clear_colour()        | None                             | Clear custom color tag. |
| commit()              | None                             | Commit object to disk. |
| get_wiretap_node_id() | None                             | Get Wiretap Node ID. |
| get_wiretap_storage_id() | None                          | Get Wiretap server's storage ID. |

### Usage Context
Used for programmatic directory traversal or creating imported folders based on the file system hierarchy.

```python
import flame

# Access the Files Tab object
files_tab = flame.media_hub.files_tab

# List the entries in the current MediaHub path and identify folder entries
current_entries = flame.media_hub.list_entries(files_tab.get_path())
for entry in current_entries:
    if isinstance(entry, flame.PyMediaHubFilesFolder):
        print(f"Found folder at absolute path: {entry.path}")
        # Optionally navigate into this folder
        # files_tab.set_path(entry.path)
```

**Note:** The `path` attribute returns an absolute file system path and can be used to drive imports or create corresponding project folders.

## Methods
### Properties
- `path(...)` — None( (flame.PyMediaHubFilesFolder)arg1) -> str 
None( (flame.PyMediaHubFilesFolder)arg1) -> str



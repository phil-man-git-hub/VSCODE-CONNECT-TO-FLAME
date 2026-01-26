
# Class: PyMediaHubFilesEntry

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents a clip entry in the MediaHub Files tab.

## Description
Provides access to clip entries in the MediaHub Files tab, including file path and metadata.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyMediaHubFilesEntry** class represents a single media element (file or sequence) as seen in the MediaHub's Files tab.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyMediaHubFilesEntry | Clip or file sequence entry. |
| Parent Class  | PyArchiveEntry| Inherits archive management methods. |
| Ancestor Class| PyFlameObject | Inherits base properties. |
| Primary Role  | Source Identification | Absolute file path to source media. |

### Unique Attributes
| Attribute         | Type           | Access     | Description |
|-------------------|---------------|------------|-------------|
| path              | str            | Read-only  | Absolute file system path of the media entry. |

### Inherited Methods
| Method                | Arguments                        | Description |
|-----------------------|----------------------------------|-------------|
| clear_colour()        | None                             | Clear custom color tag. |
| commit()              | None                             | Commit object to disk. |
| get_wiretap_node_id() | None                             | Get Wiretap Node ID. |
| get_wiretap_storage_id() | None                          | Get Wiretap server's storage ID. |

### Usage Context
Used to select files for import, typically by iterating entries and passing their paths to import_media.

**Example:**

```python
# List and filter entries in current MediaHub Files tab path
entries = flame.media_hub.list_entries(flame.media_hub.files_tab.get_path())
exr_files = [e.path for e in entries if isinstance(e, flame.PyMediaHubFilesEntry) and e.path.endswith('.exr')]
print(f"Found {len(exr_files)} EXR files")
# Then import
# flame.media_hub.import_media(exr_files, destination_reel)
```


## Methods
### Properties
- `path(...)` — None( (flame.PyMediaHubFilesEntry)arg1) -> str 
None( (flame.PyMediaHubFilesEntry)arg1) -> str



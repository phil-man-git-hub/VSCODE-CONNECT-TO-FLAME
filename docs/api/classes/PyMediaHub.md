
# Class: PyMediaHub

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Main interface object for accessing MediaHub functionality, including file and archive management.

## Description
Provides access to the MediaHub UI, allowing users to browse, import, and manage media and archives in Flame.


## API Insight: Definition, Attributes, Methods, and Usage
The **PyMediaHub** class represents the MediaHub interface, providing programmatic control over file importing, browsing, and management.

### Definition and Hierarchy
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyMediaHub    | MediaHub interface object. |
| Parent Class  | None explicit | Top-level utility for UI component. |
| Primary Role  | File and Import Management | Control over file browsing, project selection, and import options. |
| Access        | Singleton     | Accessed via flame.media_hub. |

### Core Properties
| Attribute         | Type           | Access     | Description |
|-------------------|---------------|------------|-------------|
| files_tab         | PyMediaHubFilesTab | Read-only  | Access to file system browsing and selection. |
| projects_tab      | PyMediaHubProjectsTab| Read-only  | Access to external projects or archives. |
| active_tab        | PyMediaHubTab  | Read/Write | Currently active tab in the interface. |

### Key Methods
| Method                | Arguments                        | Returns   | Description |
|-----------------------|----------------------------------|-----------|-------------|
| import_media()        | file_list, destination           | bool      | Import media files into a folder or reel. |
| open_media_hub()      | None                             | bool      | Open the MediaHub interface. |
| close_media_hub()     | None                             | bool      | Close the MediaHub interface. |
| is_open               | None                             | bool      | Whether the MediaHub is open. |

### Related Sub-Classes
| Class                 | Role                             | Key Functionality |
|-----------------------|----------------------------------|------------------|
| PyMediaHubTab         | Base class for tabs               | Navigation methods. |
| PyMediaHubFilesTab    | Files Tab                         | File system browsing and selection. |
| PyMediaHubFilesTabOptions | Import Settings                | Controls import options before calling import_media. |

### Usage Context
To import files, set import options via files_tab.options, then use import_media to bring files into the project.

**Example:**

```python
media_hub = flame.media_hub
dest_reel = flame.project.reels[0]
# Configure import options
opts = media_hub.files_tab.options
opts.frame_ratio = 24.0
opts.bit_depth = 'From Source'
# Import files
paths = ['/mnt/assets/shot01_v01.exr', '/mnt/assets/shot02_v01.exr']
if media_hub.import_media(paths, dest_reel):
    print('Imported files')
```


## Methods
### Properties
- `files(...)` — None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubFilesTab 
None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubFilesTab

- `archives(...)` — None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubTab 
None( (flame.PyMediaHub)arg1) -> flame.PyMediaHubTab



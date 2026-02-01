# Flame Python API Object Reference

**Source:** Autodesk Flame Family 2026 Help | Autodesk Flame Python: flame module

## Core Classes

### `flame.PyFlameObject`
The base class for all Flame Python objects.
- **Attributes:**
    - `attributes`: Dictionary of object attributes.
    - `parent`: The parent object.

### `flame.PyArchiveEntry` (Inherits `PyFlameObject`)
Base class for objects in the Media Panel.
- **Methods:**
    - `clear_colour()`
    - `commit()`: Save changes to disk.
    - `get_wiretap_node_id()`
    - `get_wiretap_storage_id()`

## Hierarchy

### `flame.PyProject` (Inherits `PyArchiveEntry`)
- **Properties:** `name`, `nickname`, `description`, `current_workspace`, `shared_libraries`.
- **Methods:**
    - `create_shared_library(name)`
    - `export_ocio_config(...)`
    - `reload_ocio_config()`

### `flame.PyWorkspace` (Inherits `PyArchiveEntry`)
- **Properties:** `desktop`, `libraries`.
- **Methods:**
    - `create_library(name)`
    - `set_desktop_reels()`

### `flame.PyDesktop` (Inherits `PyArchiveEntry`)
- **Properties:** `batch_groups`, `reel_groups`.
- **Methods:**
    - `create_batch_group(...)`
    - `create_reel_group(name)`

### `flame.PyLibrary` (Inherits `PyArchiveEntry`)
- **Methods:** `acquire_exclusive_access()`, `release_exclusive_access()`.

## Batch

### `flame.PyBatch` (Inherits `PyFlameObject`)
Represents a Batch Group.
- **Properties:** `nodes`, `reels`, `shelf_reels`, `current_iteration`.
- **Methods:**
    - `create_node(type, path)`
    - `connect_nodes(out_node, out_socket, in_node, in_socket)`
    - `import_clip(path, reel)`
    - `organize()`
    - `render()`
    - `save()`
    - `go_to()`: Open this batch group.

### `flame.PyNode` (Inherits `PyFlameObject`)
- **Properties:** `name`, `type`, `pos_x`, `pos_y`, `input_sockets`, `output_sockets`.
- **Methods:**
    - `set_context(index, socket)`
    - `delete()`

### Specialized Nodes
- **`PyActionNode` / `PyActionFamilyNode`**:
    - `add_media()`
    - `import_fbx()`, `export_fbx()`
    - `create_node()` (inside Action schematic)
- **`PyWriteFileNode`**:
    - `get_resolved_media_path()`
- **`PyMatchbox`**: (Accessed via generic PyNode, but has `shader_name`)
- **`PyOpenFX`**: (Accessed via generic PyNode, but has `plugin_name`)

## Timeline

### `flame.PyClip` / `flame.PySequence` (Inherits `PyArchiveEntry`)
- **Properties:** `versions`, `audio_tracks`, `markers`, `segments`, `start_frame`, `duration`.
- **Methods:**
    - `reformat(...)`
    - `render(...)`
    - `export(...)` (via Exporter)
    - `open_as_sequence()`

### `flame.PyTrack`
- **Properties:** `segments`, `transitions`, `stereo_linked`.

### `flame.PySegment`
- **Properties:** `name`, `record_in`, `record_out`, `source_name`, `file_path`.
- **Methods:**
    - `create_effect(type)`
    - `create_marker(frame)`

## Helpers

### `flame.PyTime`
Represents a time value.
- `PyTime("10:00:00:00", "23.976 fps")`
- `PyTime(frame_int)`

### `flame.PyExporter`
Configures export settings.
- `export(sources, preset_path, out_dir)`

## Module Functions
- `flame.execute_shortcut(name)`
- `flame.import_clips(path, dest)`
- `flame.schedule_idle_event(callback)`

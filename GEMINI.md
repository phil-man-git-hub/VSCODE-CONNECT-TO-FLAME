# Gemini Repo Analysis: VSCODE-CONNECT-TO-FLAME

This document provides a technical overview and analysis of the `VSCODE-CONNECT-TO-FLAME` repository, conducted by Gemini.

## Repository Purpose
The primary goal of this repository is to bridge the gap between **Autodesk Flame's internal Python API** and modern development workflows, specifically targeting **VS Code**. It provides a real-time execution bridge, comprehensive API documentation, and high-quality type stubs for local development.

## Gemini Expert Profile: Autodesk Flame Python Specialist
As of January 2026, Gemini is configured as a specialized expert in the Autodesk Flame development ecosystem:
- **API Deep Knowledge:** Full mastery of the Flame Python API (up to version 2027.0.0 preview release pr236), including class hierarchies, methods, and properties.
- **Execution Environment Mastery:** Deep understanding of Flame's threading model and the necessity of main-thread execution (via `schedule_idle_event`) for API safety.
- **Domain-Specific Constraints:** Acute awareness of Flame's unique script loading behaviors, such as filename uniqueness requirements and the strict prohibition of `__init__.py` files.
- **Workflow Architecture:** Expert-level proficiency in managing the "Decoupled Bridge Architecture," spanning TypeScript (VS Code extension), Python (Flame Listener), and introspection-based stub generation.

## Core Components

### 1. Flame Listener (`flame-listener/`)
A Python service designed to run inside Autodesk Flame.
- **Role:** Listens on a local port (default 5555) for incoming Python code snippets.
- **Key Feature:** Enforces **main-thread execution** via `flame.schedule_idle_event` (or similar) to ensure API safety and prevent segfaults.
- **Output:** Captures `stdout`, `stderr`, and Python exceptions, returning them as JSON to the caller.

### 2. VS Code Extension (`extension/`)
A TypeScript-based extension that provides the UI bridge.
- **Features:** "Run in Flame" command, connection testing (ping), and debugging integration.
- **State:** Currently in early development (`0.0.1`), focusing on the core communication layer.

### 3. API Intelligence Pipeline (`scripts/`)
A robust data collection and generation system.
- **Collector (`collect_flame_api.py`):** Systematically crawls a running Flame instance using introspection to discover modules, classes, methods, and properties.
- **Doc Generator (`generate_api_docs.py`):** Converts JSON reports into structured Markdown for the documentation site.
- **Stub Generator (`generate_stubs_from_reports.py`):** Creates detailed `.pyi` files (2,400+ lines) to enable full IDE autocompletion without needing a local `flame` module.

### 4. Documentation (`docs/` & `site/`)
An MkDocs-powered site that serves as the "Source of Truth" for the Flame Python API, which is otherwise difficult to explore.

## Key Technical Achievements (as of Jan 2026)

- **Thread-Safety Implementation:** Successfully identified and fixed a critical issue where background thread execution caused Flame to crash. All API calls are now safely dispatched to the main UI thread.
- **Automated API Mapping:** Built a two-phase 'Discovery & Introspection' pipeline that can map the entire API of any Flame version in minutes.
- **Deep Stub Generation:** Expanded basic stubs into a rich, documented type-hinting system that captures method signatures, default values, and inheritance chains.
- **CI/CD Stabilization:** Fixed deprecated GitHub Actions and permission issues, ensuring automated documentation deployment works seamlessly.

## Python Script Loading Constraints
Autodesk Flame has specific requirements for loading Python scripts and hooks:
- **Unique Filenames:** Flame can only load scripts or hooks that have unique filenames.
- **No `__init__.py`:** Conventional Python packages with `__init__.py` files are strictly not permitted within Flame's search paths, as they can interfere with script discovery or cause loading conflicts.
- **Alternative Strategies:** Developers must employ other strategies for code organization, such as unique naming conventions or manual path management, to avoid these limitations.

## Flame Hook & API Patterns
Analysis of Autodesk-supplied example scripts reveals the following key patterns and hook categories available in Flame 2027:

### 1. Application & Project Lifecycle (`hook.py`, `project_hook.py`, `conversion_description.py`, `project_protection.py`)
- **App Events:** `app_initialized`, `app_exited`, `user_changed`.
- **Project Events:** Comprehensive lifecycle hooks for creation, edition, deletion, conversion, and restoration of projects (e.g., `project_pre_creation`, `project_post_restore`, `project_saved`).
- **Global Defaults:** Hooks to define default naming conventions for shots (`timeline_default_shot_name`), markers (`timeline_default_marker_name`), and references.
- **Monitoring:** `render_ended`, `playback_ended`, `preview_window_config_changed`.
- **Modifications:** Hooks like `project_init_conversion` allow modifying project metadata (e.g., description) during conversion.
- **Protection:** Project hooks (e.g., `project_pre_edition`, `project_pre_delete`) can use the `abort` flag to prevent changes to protected projects.

### 2. Batch Operations (`batch_hook.py`)
- **Setup:** Hooks for loading (`batch_setup_loaded`), saving (`batch_setup_saved`), and iteration (`batch_setup_iterated_pre/post`).
- **Processing:** Granular hooks for Render (`begin/end`), Burn (`begin/end`), and Export (`begin/end`) within the Batch environment.
- **Context:** Most hooks provide an `info` dictionary (often modifiable) and a `userData` object to pass state between `begin` and `end` events.

### 3. Export & Archive (`export_hook.py`, `archive_hook.py`, `post_export_dependency.py`, `post_export_asset_after_snapshot.py`)
- **Export Pipeline:** deeply nested execution order: `preCustomExport` -> `preExport` -> `preExportSequence` -> `preExportAsset` -> [Backburner/Local] -> `postExportAsset` -> ... -> `postExport`.
- **Customization:** Hooks to bypass overwrite prompts (`export_overwrite_file`), define custom export profiles (`get_custom_export_profiles`), and control background execution.
- **Archive:** Monitoring for archive restoration, completion, segment processing, and selection updates.
- **Advanced Workflows:**
    - **Chaining Jobs:** Post-export hooks can trigger Backburner jobs (e.g., for transcoding or zipping) dependent on the main export job (`backgroundJobId`).
    - **Snapshot Handling:** The `isSnapshot` key in `post_export_asset` identifies exports triggered by the "Export Snapshot" feature, allowing workflows like auto-reimporting snapshots to the Desktop.
    - **Re-import:** Using `WireTapClient` in an idle loop to monitor Backburner job status and re-import clips once processing is complete.

### 4. Custom UI Integration (`custom_actions_hook.py`, `custom_menu_structure.py`, `custom_action_object.py`)
- **Context Menus:** Python functions can be injected into various UI contexts (`Media Panel`, `Main Menu`, `Timeline`, `Batch`, `MediaHub`).
- **Menu Structure:** Support for nested submenus (`hierarchy`), custom ordering (`order`), and separators (`separator`).
- **Action Objects:** Actions can be any callable Python object (e.g., a class instance with `__call__`), allowing for stateful or parameterized actions.
- **Wait Cursor:** Control over the wait cursor (`"waitCursor": True/False`) allows for interactive actions (like dialogs) without UI freezing.

### 5. OTIO Integration Patterns (`otio_reader.py`, `otio_reader_hook.py`)
- **Mapping:** Demonstrates mapping OpenTimelineIO objects to Flame objects:
    - `otio.schema.Timeline` -> `flame.PySequence`
    - `otio.schema.Track` -> `flame.PyTrack` (Video/Audio)
    - `otio.schema.Clip` -> `flame.PySegment` (linked or unlinked)
    - `otio.schema.Transition` -> `flame.PyTransition`
- **Advanced Features:** Handles Markers, Metadata, Effects, and complex media reference resolution (translating URLs to file paths).
- **Architecture:** Uses a `FlameOTIOReader` class with a hook-dispatch system (`pre_hook_<schema>`, `post_hook_<schema>`) to allow extensibility.

### 6. Python Utilities & Examples
- **Context Variables:** `set_context_variable` API to drive OCIO transforms (e.g., 'SHOT') on Clips, Segments, and Sequences.
- **Dialogs:** Integration with `PySide6.QtWidgets` for custom file dialogs or using `flame.browser.show` for native Flame file browsing.
- **Messages:** `flame.messages.show_in_console` and `flame.messages.show_in_dialog` for user feedback.
- **Scoping:** Helper patterns to restrict actions to specific object types (`PyClipNode`, `PySegment`) or UI contexts (e.g., Batch Schematic background).
- **Version Scoping:** Fine-grained control over hook availability using `minimumVersion` and `maximumVersion` attributes on both hooks and action dictionaries.
- **Idle Processing:** Using `flame.schedule_idle_event` to implement background tasks like "Watch Folders" that process files without blocking the UI.
- **Batch Node Automation:**
    - **Creation & Connection:** Programmatically creating nodes (e.g., `Action`, `Motion Vectors Map`), setting attributes (`pos_x`, `pos_y`), and connecting them (`connect_nodes`).
    - **Caching:** Triggering `cache_range()` on specific nodes.
    - **Cleanup:** Recursively finding and deleting `batch_iterations` to manage project size.
- **Advanced Export & Transcoding:**
    - **Metadata Injection:** Injecting custom metadata (Project, User, Version) into OpenEXR headers via `batch_export_begin` and `set_metadata_value`.
    - **Single Frame Export:** Duplicating clips and manipulating In/Out marks (`export_between_marks=True`) to export specific frames (thumbnails).
    - **FFmpeg Integration:** Piping `read_frame` and `read_audio` output directly into `ffmpeg` via named pipes for custom foreground/background encoding.
    - **Wiretap Access:** Extracting `storage_id` and `node_id` to drive external command-line tools.
- **Archive Management:** Filtering and color-coding clips based on `archive_date` and `archive_error` status.
- **OS Integration:** Using `flame.execute_command` to open OS file browsers (`Finder`, `Nautilus`) pointing to specific media paths.

## Advanced Specialized APIs

### 1. OpenClip API (Virtual Media Assembly)
- **Hierarchy:** `Clip` -> `Track` -> `Feed` -> `Span`.
- **Logic:** Enables "Virtual Assembly" of media. Multiple `<span>` elements can join fragmented camera files into a single seamless stream without rendering.
- **Dynamic Discovery:** Supports `ScanPattern` tokens (`{name}`, `{version}`, `{frame}`) for "Self-Updating" clips that automatically see new renders on disk.
- **Metadata:** Extensive `<dict>` support for pipeline tracking (Artist, Job ID, Render Time) embedded directly in the `.clip` XML.

### 2. Inference Builder API (AI/ML Integration)
- **Packaging:** Packages trained **ONNX** models into encrypted **.inf** files.
- **Sidecar Logic:** Uses a `.json` sidecar to map Flame inputs (Front, Matte) to model inputs and handle technical requirements like `ScalingFactor` and `Padding`.
- **Deployment:** Turns complex Machine Learning models into simple, user-friendly nodes in the Flame Batch environment.

### 3. Shader Builder API (GLSL Tool Creation)
- **Matchbox vs. Lightbox:**
    - **Matchbox:** 2D image processing (Blurs, CC), uses `main()`.
    - **Lightbox:** 3D lighting effects in Action, uses `adskUID_lightbox()`.
- **UI Design:** Sidecar `.xml` files define professional interfaces including Color Wheels, Curve Editors, and Conditional Visibility (hiding sliders based on checkboxes).
- **Namespacing:** Mandatory `adskUID_` prefix for all global symbols to prevent crashes when multiple shaders are loaded.
- **Built-in Helpers:** Access to high-level functions like `adsk_getLightPosition()`, `adsk_rgb2hsv()`, and `adsk_getBlendedValue()`.

### 4. Wiretap SDK API (Universal Database Access)
- **Uniform Abstraction:** Exposes proprietary databases (IFFFS), file systems (Gateway), and job queues (Backburner) as a uniform navigable hierarchy of `Nodes`.
- **Librarian vs. Worker:** Follows a strict model where the **Server** only exposes data, while the **Client** performs all heavy processing (transcoding, conversion) to ensure workstation responsiveness.
- **Self-Discovery:** Utilizes multicast networking for peer-to-peer discovery (`hostname:database`), with support for hardcoded topology via `services.cfg` in complex networks.
- **Low-Level Media I/O:** Deep control over raw RGB image buffers (bottom-to-top orientation, 32-bit line padding) and block-based audio sample streaming.
- **Distributed Rendering:** Programmatic job submission to Backburner, with advanced metadata filtering for building real-time studio dashboards.

## Expert Coding Patterns & Best Practices

- **The "Sandwich" Pattern:** Leverage `pre_` and `post_` hooks to wrap Flame operations. Use `userData` dictionaries to pass state (like timestamps or IDs) between the start and end of a task.
- **Non-Destructive Temporary Objects:** Use `flame.duplicate(clip)` inside a `try...finally` block to perform temporary operations (like single-frame exports) without altering the artist's original work.
- **Safe External Execution:** Prefer `flame.execute_command` over standard Python `subprocess` to avoid memory "forking" overhead in large Flame projects.
- **The Idle Loop Relay:** For long background tasks (like Watch Folders), use `flame.schedule_idle_event` to process items one-by-one, rescheduling itself with a delay to keep the UI responsive.
- **The Success Switch:** In Wiretap SDK, functions return `bool`. Always check for `False` and immediately capture `handle.lastError()` before the next API call overwrites it.
- **Initialization Hygiene:** Always pair `WireTapClientInit()` with `WireTapClientUninit()` to ensure background network threads are safely parked before the script exits.
- **Strict Namespacing:** Always use unique prefixes (like `adskUID_` or `WireTap_`) for global variables and functions to avoid silent failures or clashing with other loaded tools.

## Architecture Analysis
The project follows a **Decoupled Bridge Architecture**:
- **Execution** is remote (inside Flame).
- **Authoring** is local (VS Code).
- **Intelligence** is static (Stubs/Docs).

This is the most effective way to handle proprietary, closed-runtime environments like Autodesk Flame.

## Future Roadmap Recommendations

1.  **Debugging Enrichment:** Integrate `debugpy` more deeply to allow line-by-line debugging of scripts running inside the Flame process.
2.  **Auth Layer:** Implement the planned token-based handshake to secure the listener beyond simple `localhost` binding.
3.  **Extension UX:** Add "Sync on Save" functionality to the VS Code extension to automatically update scripts in Flame as they are edited.
4.  **Community Snippets:** Populate `examples/snippets/` with common Flame tasks (e.g., "Archive Project", "Batch Setup Creation") to utilize the newly generated stubs.

---
*Analysis performed by Gemini CLI on 2026-01-26.*

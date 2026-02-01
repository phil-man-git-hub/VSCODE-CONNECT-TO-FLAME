# Python Hooks Reference

**Source:** Autodesk Flame Family 2026 Help | Python Hooks Reference

## Overview

Python Hooks allow you to inject external code to monitor, inspect, or modify Flame's behavior. They are essential for pipeline integration, shot management, and automation.

**Key Features:**
-   **Location:** Hooks are standard Python files (`.py`) placed in specific directories.
-   **Discovery:** Flame scans these directories and loads any file containing supported hook functions.
-   **Multiple Definitions:** You can define the same hook in multiple files. Flame will execute all of them (usually sequentially or by merging results).
-   **Blocking:** Hooks are blocking and run in the main thread. Use threading for long-running tasks.

## Hook Locations

Flame scans for hooks in the following order (by default):

1.  **User:**
    -   Linux: `/home/<user>/flame/python/`
    -   macOS: `/Users/<user>/Library/Preferences/Autodesk/flame/python/`
2.  **Project:** `/opt/Autodesk/project/<project>/python/`
3.  **Application:** `/opt/Autodesk/<version>/python/`
4.  **Shared:** `/opt/Autodesk/shared/python/`

> **Note:** You can customize the scan path using the `DL_PYTHON_HOOK_PATH` environment variable.

## Custom UI Actions

Custom UI Actions allow you to add items to Flame's context menus.

### Hook Functions
| Hook Name | Context |
|---|---|
| `get_main_menu_custom_ui_actions` | Main Menu (Flame logo) |
| `get_media_panel_custom_ui_actions` | Media Panel (right-click) |
| `get_timeline_custom_ui_actions` | Timeline (right-click) |
| `get_batch_custom_ui_actions` | Batch (right-click) |
| `get_action_custom_ui_actions` | Action/GMask/Image (right-click) |
| `get_mediahub_files_custom_ui_actions` | MediaHub Files |
| `get_mediahub_archives_custom_ui_actions` | MediaHub Archives |

### Return Format
These hooks must return a **tuple** of dictionaries. Each dictionary represents a menu group or action.

#### Action Dictionary
```python
{
    "name": "Unique Name",          # Internal unique name
    "caption": "Menu Label",        # (Optional) Visible label
    "execute": my_callback_func,    # Function to run
    "isEnabled": True,              # (Optional) Bool or Function(selection)
    "isVisible": True,              # (Optional) Bool or Function(selection)
    "minimumVersion": "2025.1"      # (Optional)
}
```

#### Group Dictionary
```python
{
    "name": "My Submenu",
    "actions": ( action_dict_1, action_dict_2 )
}
```

### Callback Signature
The `execute`, `isEnabled`, and `isVisible` callbacks receive a single argument: **`selection`**.
-   `selection` is a **tuple** of the selected Python objects (e.g., `( <PyClip>, <PySequence> )`).

## Export Hooks (`exportHook.py`)

These hooks trigger during the export process.

**Execution Order:**
1.  `pre_custom_export` (If using custom profiles)
2.  `pre_export` (Export dialog opens)
3.  `pre_export_sequence`
4.  `pre_export_asset` (Called per asset)
5.  `post_export_asset`
6.  `post_export_sequence`
7.  `post_export`
8.  `post_custom_export`

## Environment Variables

-   `DL_PYTHON_HOOK_PATH`: Colon-separated list of additional paths to scan.
-   `DL_DEBUG_PYTHON_HOOKS`: Set to `1` to enable verbose logging of hook loading and execution.

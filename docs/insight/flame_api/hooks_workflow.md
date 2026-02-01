# Python Hooks Workflow & Best Practices

**Source:** Autodesk Flame Family 2026 Help | Python Hooks Tips

## Development Workflow

### Hot reloading
You do not need to restart Flame to test hook changes.
-   **Shortcut:** `Ctrl+Shift+P+H` (Default)
-   **Action:** "Scan for python hooks" in the hotkey editor.

### Debugging
Enable verbose logging to see exactly when hooks are loaded and called.
```bash
export DL_DEBUG_PYTHON_HOOKS=1
/opt/Autodesk/<version>/bin/startApplication
```

## Common Patterns

### Passing Data Between Hooks
Hooks are stateless function calls. To share data (e.g., project name) between different hooks, use a global variable populated by `app_initialized`.

```python
current_project = None

def app_initialized(project_name):
    global current_project
    current_project = project_name

def some_other_hook(info):
    print(f"Running in project: {current_project}")
```

### Threading Long Operations
Hooks block the UI. For long tasks (like uploading to ShotGrid or copying large files), spawn a thread.

**Critical:** You must join threads at exit to prevent zombie processes or crashes.

```python
from threading import Thread
import atexit
import time

active_threads = []

def cleanup_threads():
    for t in active_threads:
        t.join()

atexit.register(cleanup_threads)

def heavy_task(asset_name):
    time.sleep(5)
    print(f"Finished processing {asset_name}")

def render_ended(moduleName, sequenceName, elapsedTime):
    t = Thread(target=heavy_task, args=(sequenceName,))
    t.start()
    active_threads.append(t)
```

### Context-Aware Actions
Custom UI actions receive the current selection. Use this to enable/disable actions dynamically.

```python
def is_video_clip(selection):
    # Only show if one item is selected and it is a Clip
    return len(selection) == 1 and isinstance(selection[0], flame.PyClip)

def get_media_panel_custom_ui_actions():
    return ([
        {
            "name": "Process Clip",
            "execute": process_func,
            "isVisible": is_video_clip
        }
    ])
```

## Wiretap & External Libraries
Flame bundles its own Python environment.
-   **Wiretap:** Use `from adsk import libwiretapPythonClientAPI`.
-   **Pip:** Install packages using `/opt/Autodesk/python/<VERSION>/bin/pip`.

# Python Console and Script Execution

The **Flame Python Console** is the primary tool for writing, editing, and executing Python code within Flame.

## The Python Console UI

Accessible via: **Flame Menu > Python > Python Console**

### Windows
-   **Terminal Window (Top/Left):** Displays output from `print()` statements, `help()` calls, and error messages (in red).
-   **Editor Window (Bottom/Right):** A text editor with syntax highlighting and tab support.
    -   **Add Tab:** Click the `+` sign in the bottom right.
    -   **Indentation:** Select lines and use `Tab` (indent) or `Shift+Tab` (unindent). `Ctrl+/` (Linux) or `Cmd+/` (macOS) to comment/uncomment.

### Icons
| Icon | Name | Description |
|---|---|---|
| ![Eraser](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-eraser.png) | Eraser | Clears terminal output. |
| ![Sound Wave](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-soundwave.png) | Sound Wave | Toggle echoing executed code to the terminal (Blue = On). |
| ![Play](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-play.png) | Play | Executes the script in the current tab (or selected code). |
| ![Save](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-save.png) | Save | Saves the current tab script to disk. |
| ![Load](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-load.png) | Load | Loads a script from disk into a new tab. |
| ![Line Num](https://help.autodesk.com/cloudhelp/2026/ENU/Flame-API/images/PythonAPI-linenums.png) | Line Numbers | Toggles line numbers in the editor. |

## Execution Methods

### 1. From the Console
-   **Run All:** Click **Play** to run the entire script in the active tab.
-   **Run Selection:** Highlight a section of code and click **Play**.

> **Important:** `import flame` only needs to be run once per tab/session.

### 2. At Startup
You can execute a script automatically when Flame launches.

Command line:
```bash
/opt/Autodesk/<version>/bin/startApplication -s /path/to/script.py
```
*Note: The script must include `import flame`.*

## Best Practices
-   Use `flame.batch.go_to()` to ensure you are in the correct tab before manipulating Batch nodes.
-   Use `flame.batch.organize()` to automatically layout nodes after creation.
-   Catch exceptions to prevent scripts from failing silently:
    ```python
    try:
        flame.batch.import_clip("bad_path", "reel")
    except Exception as e:
        print(e)
    ```

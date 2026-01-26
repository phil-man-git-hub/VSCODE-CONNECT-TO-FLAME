
# Class: PyMessages

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Handles the message bar and dialogs in the application UI.

## Description
Provides access to the message bar and dialog system, allowing display and management of messages and dialogs in Flame.

---

## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMessages`** utility exposes methods for sending user-facing messages and console logs from scripts, categorized by severity (info, warning, error) and with support for dialog boxes.

**Example:**

```python
# Log to console and notify the user via the message bar
flame.messages.log('Starting render batch...')
flame.messages.info('Render started: Check back in 10 minutes')
if errors:
    flame.messages.warning(f"Completed with {len(errors)} non-fatal issues")
if critical_failure:
    flame.messages.error('Critical: export failed, check logs')

# Display a confirmation dialog
choice = flame.messages.show_in_dialog('Confirm', 'Start export now?', 'question', ['Yes', 'No'], cancel_button='No')
if choice == 'Yes':
    start_export()
```


## Methods
### Built-in methods
- `show_in_console(...)` — show_in_console( (PyMessages)arg1, (str)message [, (str)type='info' [, (int)duration=-1]]) -> None : 
show_in_console( (PyMessages)arg1, (str)message [, (str)type='info' [, (int)duration=-1]]) -> None :
    Display an informative message in application message bar.
    message -- Message string to display.
    type -- Message type can be info, warning, or error.
    duration -- An optional time in seconds to keep message on screen.

- `clear_console(...)` — clear_console( (PyMessages)arg1) -> None : 
clear_console( (PyMessages)arg1) -> None :
    Remove currently displayed message in the message bar.

- `show_in_dialog(...)` — show_in_dialog( (PyMessages)arg1, (str)title, (str)message, (str)type, (list)buttons [, (str)cancel_button='']) -> str : 
show_in_dialog( (PyMessages)arg1, (str)title, (str)message, (str)type, (list)buttons [, (str)cancel_button='']) -> str :
    Display a custom dialog with a selection of options.
    Keywords argument:
    title -- The title of the dialog.
    message -- The message displayed in the centre of the dialog.
    type -- The type of dialog. Can be error, info, question, or warning.
    buttons -- The list of titles used to refer to the options
    cancel_button -- The text displayed in the cancel option



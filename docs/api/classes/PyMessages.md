# Class: PyMessages

**Module**: `flame`

Module handling message bar in application UI.

## Methods
### `show_in_console(...)`

show_in_console( (PyMessages)arg1, (str)message [, (str)type='info' [, (int)duration=-1]]) -> None :
    Display an informative message in application message bar.
    message -- Message string to display.
    type -- Message type can be info, warning, or error.
    duration -- An optional time in seconds to keep message on screen.

### `clear_console(...)`

clear_console( (PyMessages)arg1) -> None :
    Remove currently displayed message in the message bar.

### `show_in_dialog(...)`

show_in_dialog( (PyMessages)arg1, (str)title, (str)message, (str)type, (list)buttons [, (str)cancel_button='']) -> str :
    Display a custom dialog with a selection of options.
    Keywords argument:
    title -- The title of the dialog.
    message -- The message displayed in the centre of the dialog.
    type -- The type of dialog. Can be error, info, question, or warning.
    buttons -- The list of titles used to refer to the options
    cancel_button -- The text displayed in the cancel option


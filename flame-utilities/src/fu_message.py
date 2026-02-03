import fu_bootstrap
import flame
import time
from fu_decorators import fu_action

"""
fu_message.py

A reusable utility module demonstrating Flame's messaging capabilities.
It also serves as a test case for the 'fu_decorators' auto-registration system.
"""

def show_console_countdown():
    """
    Show a countdown within the message bar/console.
    """
    print("Starting countdown in console...")
    for i in reversed(range(0, 6)):
        if i == 0:
             flame.messages.show_in_console("Lift off!", "info", 2)
        else:
            flame.messages.show_in_console(f"Launching in {i}...", "warning", 1)
        time.sleep(1)

@fu_action(menu="media_panel", path="Flame Utilities / Messages", wait_cursor=False)
def show_demo_dialog(selection):
    """
    Display a demonstration dialog box.
    Registered to Media Panel -> Flame Utilities -> Messages -> Show Demo Dialog
    """
    response = flame.messages.show_in_dialog(
        title="fu_message.py",
        message="This is a message from your new utility script.\n\n" \
                "Click 'Run Countdown' to test console messages.",
        type="info",
        buttons=["Run Countdown", "Cancel"],
        cancel_button="Cancel"
    )
    
    if response == "Run Countdown":
        show_console_countdown()
    else:
        flame.messages.show_in_console("Operation cancelled by user.", "info", 3)

# Note: The main() block is removed or commented out because this file 
# is now loaded as a module by fu_loader.py, not run as a script.
# If you still want it runnable manually, you can keep it, but the decorator
# handles the menu entry now.


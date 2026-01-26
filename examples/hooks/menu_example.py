"""Example menu hook skeleton

It demonstrates the shape of a menu hook and a safe query function for testing.
"""

def get_menu_items():
    # Return a static list for testing; real hooks would construct menus dynamically
    return [{'name': 'example', 'action': 'do_example'}]

import fu_bootstrap
import flame
from fu_decorators import fu_action

"""
fu_colours.py

Utilities for applying studio-standard colouring to clips and segments.
Requires Flame 2025 or newer.
"""

def _apply_colour(selection, color_tuple):
    """Internal helper to apply color to a selection of PyObjects."""
    count = 0
    for item in selection:
        # Most PyObjects in Flame 2025+ have a .colour property
        if hasattr(item, 'colour'):
            try:
                item.colour = color_tuple
                count += 1
            except Exception as e:
                print(f"Error applying colour to {item.name}: {e}")
    
    if count > 0:
        flame.messages.show_in_console(f"Applied colour to {count} items.", "info", 2)

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Colour", min_version="2025")
def mark_as_final_green(selection):
    """Set selection colour to Studio Final Green."""
    _apply_colour(selection, (0.1, 0.8, 0.2))

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Colour", min_version="2025")
def mark_as_rejected_red(selection):
    """Set selection colour to Studio Rejected Red."""
    _apply_colour(selection, (0.9, 0.1, 0.1))

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Colour", min_version="2025")
def mark_as_pending_orange(selection):
    """Set selection colour to Studio Pending Orange."""
    _apply_colour(selection, (1.0, 0.5, 0.0))

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Colour", min_version="2025")
def clear_colour(selection):
    """Reset selection colour to default (usually black or transparent)."""
    _apply_colour(selection, (0.0, 0.0, 0.0))

# Also add to Timeline for segments
@fu_action(menu="timeline", path="Flame Utilities / Labels / Colour", min_version="2025")
def timeline_mark_as_final(selection):
    mark_as_final_green(selection)

@fu_action(menu="timeline", path="Flame Utilities / Labels / Colour", min_version="2025")
def timeline_clear_colour(selection):
    clear_colour(selection)

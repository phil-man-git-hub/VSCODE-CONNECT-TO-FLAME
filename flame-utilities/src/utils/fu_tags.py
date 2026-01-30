import flame
from fu_decorators import fu_action

"""
fu_tags.py

Utilities for managing studio-standard tags on clips and sequences.
Requires Flame 2026 or newer.
"""

def _add_tag(selection, tag_name):
    """Internal helper to add a tag to a selection of PyObjects."""
    count = 0
    for item in selection:
        if hasattr(item, 'tags'):
            try:
                # tags is a list of strings. We need to assign a new list to trigger update.
                current_tags = list(item.tags)
                if tag_name not in current_tags:
                    current_tags.append(tag_name)
                    item.tags = current_tags
                    count += 1
            except Exception as e:
                print(f"Error adding tag to {item.name}: {e}")
    
    if count > 0:
        flame.messages.show_in_console(f"Added tag '{tag_name}' to {count} items.", "info", 2)

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Tags", min_version="2026")
def add_approved_tag(selection):
    """Add 'Approved' tag to selection."""
    _add_tag(selection, "Approved")

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Tags", min_version="2026")
def add_vfx_tag(selection):
    """Add 'VFX' tag to selection."""
    _add_tag(selection, "VFX")

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Tags", min_version="2026")
def clear_all_tags(selection):
    """Remove all tags from selection."""
    count = 0
    for item in selection:
        if hasattr(item, 'tags'):
            item.tags = []
            count += 1
    flame.messages.show_in_console(f"Cleared tags for {count} items.", "info", 2)

# Also add to Timeline for segments
@fu_action(menu="timeline", path="Flame Utilities / Labels / Tags", min_version="2026")
def timeline_add_approved_tag(selection):
    add_approved_tag(selection)

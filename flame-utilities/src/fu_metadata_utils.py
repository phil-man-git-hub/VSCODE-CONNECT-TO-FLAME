import fu_bootstrap
import flame
from fu_decorators import fu_action

"""
fu_metadata.py

Utilities for injecting and managing custom metadata on Flame objects.
Requires Flame 2027 or newer.
"""

def _inject_studio_metadata(selection):
    """Internal helper to inject studio standard keys into object metadata."""
    count = 0
    for item in selection:
        # Flame 2027+ introduces set_metadata_value on many PyObjects
        # Especially powerful on Write File nodes for EXR header injection.
        try:
            # Gather environment info
            metadata = {
                "studio/project": flame.projects.current_project.name,
                "studio/artist": flame.users.current_user.name,
                "studio/flame_version": flame.get_version()
            }

            # If it's a Batch Write node, we apply to channels
            if hasattr(item, 'channels') and hasattr(item, 'set_metadata_value'):
                for channel in item.channels:
                    channel_name = channel[1]
                    for key, value in metadata.items():
                        item.set_metadata_value(channel_name, key, value)
                count += 1
            # For standard clips/sequences
            elif hasattr(item, 'set_metadata_value'):
                for key, value in metadata.items():
                    item.set_metadata_value(key, value)
                count += 1
        except Exception as e:
            print(f"Error injecting metadata into {item.name}: {e}")
    
    if count > 0:
        flame.messages.show_in_console(f"Injected studio metadata into {count} items.", "info", 2)

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Metadata", min_version="2027")
def inject_studio_signature(selection):
    """Inject Project, Artist, and Version info into selection metadata."""
    _inject_studio_metadata(selection)

@fu_action(menu="batch", path="Flame Utilities / Labels / Metadata", min_version="2027")
def batch_inject_metadata(selection):
    """Inject studio metadata into selected Write File nodes."""
    _inject_studio_metadata(selection)

@fu_action(menu="media_panel", path="Flame Utilities / Labels / Metadata", min_version="2027")
def print_metadata_to_console(selection):
    """Print all available metadata for the selected item to the Flame console."""
    for item in selection:
        if hasattr(item, 'metadata'):
            print(f"--- Metadata for {item.name} ---")
            print(item.metadata)
            flame.messages.show_in_console(f"Metadata printed to shell for {item.name}", "info", 2)

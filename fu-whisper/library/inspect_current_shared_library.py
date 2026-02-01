"""Shared Library Inspector"""
import flame, json
def shared_library():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Library" in str(type(o)) and getattr(o, "is_shared", False)]
    lib = selection[0] if selection else None
    if not lib:
        return {"error": "No Shared Library selected"}
    return {"name": str(lib.name), "lock": str(getattr(lib, "lock_status", "Unknown"))}
if __name__ == "__main__":
    print(json.dumps(shared_library(), indent=2))

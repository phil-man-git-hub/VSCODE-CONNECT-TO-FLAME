"""Reel Inspector"""
import flame, json
def reel():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Reel" in str(type(o))]
    r = selection[0] if selection else None
    if not r:
        return {"error": "No Reel selected"}
    return {"name": str(r.name), "clips": len(r.clips) if r.clips else 0}
if __name__ == "__main__":
    print(json.dumps(reel(), indent=2))

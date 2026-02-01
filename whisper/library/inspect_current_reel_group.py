"""Reel Group Inspector"""
import flame, json
def reel_group():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "ReelGroup" in str(type(o))]
    rg = selection[0] if selection else None
    if not rg:
        return {"error": "No Reel Group found"}
    return {"name": str(rg.name), "reels": len(rg.reels) if rg.reels else 0}
if __name__ == "__main__":
    print(json.dumps(reel_group(), indent=2))

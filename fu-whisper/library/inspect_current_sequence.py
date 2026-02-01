"""Sequence Inspector"""
import flame, json
def sequence():
    sel = flame.media_panel.get_selected_objects() if hasattr(flame.media_panel, "get_selected_objects") else []
    selection = [o for o in sel if "Sequence" in str(type(o))]
    s = selection[0] if selection else None
    if not s:
        return {"error": "No Sequence selected"}
    return {"name": str(s.name), "tracks": len(s.video_tracks) if hasattr(s, "video_tracks") else 0}
if __name__ == "__main__":
    print(json.dumps(sequence(), indent=2))

"""Hook: List Clips

This hook wraps the `examples.snippets.clip_snippet.list_clips_in_current_timeline`
snippet and returns a structure suitable for a UI action.
"""

from examples.snippets.clip_snippet import list_clips_in_current_timeline


def run_list_clips():
    """Return simple dict describing clips for UI consumption."""
    try:
        res = list_clips_in_current_timeline()
        return {'ok': True, 'clips': res.get('clips')}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}

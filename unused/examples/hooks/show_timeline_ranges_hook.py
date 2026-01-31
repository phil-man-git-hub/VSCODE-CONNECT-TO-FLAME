"""Hook: Show Timeline Frame Ranges

Uses `timeline_snippet.timeline_frame_ranges` to return range info.
"""

from examples.snippets.timeline_snippet import timeline_frame_ranges


def run_show_ranges():
    try:
        res = timeline_frame_ranges()
        return {'ok': True, 'range': res.get('range')}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}

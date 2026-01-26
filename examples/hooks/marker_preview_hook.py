"""Hook: Marker Preview

Provides a preview payload for a marker via `make_marker_payload`. Does not
mutate Flame unless explicit commit function is called by a user.
"""

from examples.snippets.marker_snippet import make_marker_payload, commit_marker


def preview_marker(frame, label='note', color='yellow'):
    try:
        payload = make_marker_payload(frame=frame, label=label, color=color)
        return {'ok': True, 'payload': payload}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}


def commit_marker_safe(frame, label='note', color='yellow'):
    # Explicitly mutate if user intentionally calls this — tests won't call it.
    try:
        res = commit_marker(frame, label=label, color=color)
        return {'ok': True, 'result': res}
    except Exception as e:
        return {'ok': False, 'error': repr(e)}

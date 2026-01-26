def make_marker_payload(frame=None, label='note', color='yellow'):
    """Return a marker payload dict (do not modify Flame state)."""
    return {'frame': frame, 'label': label, 'color': color}


def commit_marker(frame, label='note', color='yellow'):
    """Optionally insert a marker into the current timeline (mutation) if available.

    This function is intentionally explicit: tests should not call it by default.
    """
    try:
        import flame
        tl = getattr(flame, 'timeline', None) or getattr(getattr(flame, 'project', None), 'timeline', None)
        if tl is None:
            return {'error': 'no timeline'}
        # Attempt common marker API patterns defensively
        if hasattr(tl, 'create_marker'):
            m = tl.create_marker(frame, label)
            return {'created': True, 'marker': str(m)}
        elif hasattr(tl, 'markers'):
            mk = {'frame': frame, 'label': label, 'color': color}
            try:
                tl.markers.append(mk)
                return {'created': True}
            except Exception as e:
                return {'error': repr(e)}
        else:
            return {'error': 'no marker API available'}
    except Exception as e:
        return {'error': repr(e)}

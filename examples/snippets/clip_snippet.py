def list_clips_in_current_timeline():
    """Return list of clip names in the current timeline (safe read-only)."""
    try:
        import flame
        tl = getattr(flame, 'timeline', None)
        if tl is None:
            # try project -> timeline
            proj = getattr(flame, 'project', None)
            if proj is not None:
                tl = getattr(proj, 'timeline', None)
        if tl is None:
            return {'clips': None}
        clips = []
        try:
            for c in getattr(tl, 'clips', []) or []:
                clips.append(getattr(c, 'name', repr(c)))
        except Exception:
            pass
        return {'clips': clips}
    except Exception as e:
        return {'error': repr(e)}

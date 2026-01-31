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


def find_clip_by_name(name):
    """Search timelines/sequences for a clip matching `name` and return location info."""
    try:
        import flame
        # search active timeline first
        def _scan(tl):
            try:
                for c in getattr(tl, 'clips', []) or []:
                    if getattr(c, 'name', '') == name:
                        return {'timeline': getattr(tl, 'name', None), 'clip_name': name}
            except Exception:
                pass
            return None

        tl = getattr(flame, 'timeline', None)
        res = None
        if tl is not None:
            res = _scan(tl)
            if res:
                return res
        proj = getattr(flame, 'project', None)
        if proj:
            for tl in (getattr(proj, 'timelines', []) or []) + (getattr(proj, 'sequences', []) or []):
                r = _scan(tl)
                if r:
                    return r
        return {'found': False}
    except Exception as e:
        return {'error': repr(e)}

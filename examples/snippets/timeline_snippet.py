def list_timelines():
    """Return list of timelines (names) for the current project if available."""
    try:
        import flame
        proj = getattr(flame, 'project', None)
        if proj is None:
            return {'timelines': None}
        try:
            tls = getattr(proj, 'timelines', None)
            if tls is None:
                # fallback: maybe project has sequences
                tls = getattr(proj, 'sequences', None)
        except Exception:
            tls = None
        if tls is None:
            return {'timelines': None}
        names = []
        try:
            for t in tls:
                names.append(getattr(t, 'name', repr(t)))
        except Exception:
            pass
        return {'timelines': names}
    except Exception as e:
        return {'error': repr(e)}


def timeline_frame_ranges():
    """Return common frame-range info for the active timeline if available."""
    try:
        import flame
        tl = getattr(flame, 'timeline', None) or getattr(getattr(flame, 'project', None), 'timeline', None)
        if tl is None:
            return {'range': None}
        info = {}
        # try a few common attribute names
        for k in ('start_frame', 'end_frame', 'in_point', 'out_point', 'start_time', 'duration'):
            try:
                if hasattr(tl, k):
                    info[k] = getattr(tl, k)
            except Exception:
                pass
        # some APIs expose callable getters
        for fn in ('get_in_point', 'get_out_point', 'get_frame_range'):
            try:
                if hasattr(tl, fn):
                    try:
                        val = getattr(tl, fn)()
                        info[fn] = val
                    except Exception:
                        pass
            except Exception:
                pass
        return {'range': info}
    except Exception as e:
        return {'error': repr(e)}

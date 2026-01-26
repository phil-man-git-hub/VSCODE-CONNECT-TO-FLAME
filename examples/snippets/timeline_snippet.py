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

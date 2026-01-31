def get_current_project_info():
    """Return simple metadata about the current project (safe, non-destructive)."""
    try:
        import flame
        proj = getattr(flame, 'project', None)
        if proj is None:
            projects = getattr(flame, 'projects', None)
            return {'project': None, 'projects_count': len(projects) if projects is not None else None}
        name = getattr(proj, 'name', None)
        return {'project': name}
    except Exception as e:
        return {'error': repr(e)}

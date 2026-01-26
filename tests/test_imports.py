import importlib
import pytest

# Mapping: display name -> list of candidate import names (first success wins)
CHECKS = [
    ('PySide6', ['PySide6']),
    ('PyOpenColorIO', ['PyOpenColorIO', 'OpenColorIO', 'opencolorio']),
    ('OpenImageIO', ['OpenImageIO']),
    ('OpenTimelineIO', ['opentimelineio', 'OpenTimelineIO']),
    ('debugpy', ['debugpy']),
    ('numpy', ['numpy']),
]


@pytest.mark.parametrize('display,candidates', CHECKS)
def test_imports_or_skip(display, candidates):
    """Attempt to import each candidate name and pass if any import succeeds.

    Use pytest.skip if none are installed so CI can opt-in to heavy binary deps by installing them.
    """
    for name in candidates:
        try:
            m = importlib.import_module(name)
            # basic sanity checks
            assert getattr(m, '__file__', None) is not None
            # ok
            return
        except Exception:
            continue
    pytest.skip(f"{display} not available in this environment (attempted: {candidates})")

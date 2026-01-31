# TODO — short term (high priority)

1. Install `debugpy` into Flame and verify attach
   - Add `scripts/install_debugpy.py` that can locate Flame's Python or accept a path and run `pip install debugpy`.
   - Deploy `debugpy` and restart Flame, then run `Flame: Start debug server` and attach from VS Code to confirm.
   - Document UI freeze caveats and recommend non-blocking workflows for debugging.

2. Harden listener
   - Add timeouts and cancellation for long-running scripts.
   - Add better error responses and logging.

3. Tests & CI
   - Add automated tests for `ping`, `execute`, and token auth (mock + optional real-Flame tests guarded by env var).
   - Add GitHub Actions workflow to run unit tests and linting.

4. UX & polish
   - Add extension snippets and ship `.pyi` stubs in `extension/stubs/`.
   - Add file-sync/auto-reload helper (optional feature).
   - Prepare extension packaging and Marketplace publish flow.

# TODO — lower priority / future

- Add a `debug` mode for the listener that captures stack traces and execution metrics.
- Explore a safer main-thread execution API or request Flame upstream add a command port API.

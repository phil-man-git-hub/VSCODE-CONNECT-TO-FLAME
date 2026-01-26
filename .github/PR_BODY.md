Summary

This PR hardens the Flame JSON listener (`flame-listener/flame_listener.py`) to improve reliability and observability when used in production and during development/testing.

Key changes

- Add thread tracking and `atexit` cleanup to join background threads on shutdown.
- Surface background-thread and unhandled exceptions via `threading.excepthook` and `sys.excepthook`.
- Enforce per-request `execute` timeouts (`timeout` request field) and report `TimeoutError` in responses.
- Make client socket recv timeout configurable via `FLAME_LISTENER_RECV_TIMEOUT` (defaults to 5s).
- Add structured logging helper writing to `FLAME_LISTENER_LOG` (defaults to `/tmp/flame_listener.log`).
- Non-blocking `start_debug_server`: immediate ACK, start adapter in background thread, log adapter listening and attach events (uses `wait_for_client` with timeout for diagnostics).
- Add tests: `tests/test_listener_robustness.py`, `tests/test_listener_more.py` covering timeouts, thread-exception logging, debug lifecycle, recv timeout, and concurrent execs.
- Add `scripts/collect_flame_debug_logs.py` to collect a small diagnostic bundle from a running Flame for triage.
- Add GitHub Actions workflow to run tests across multiple Python versions.

Testing

- All new tests pass locally in the venv (`.venv/bin/python -m pytest`).
- Manual tests performed against a running Flame: reload hook, start debug server, verify debugpy listens and attach logs.

Migration/Config

- Optional env vars:
  - `FLAME_LISTENER_LOG` to set log file path (default `/tmp/flame_listener.log`).
  - `FLAME_LISTENER_RECV_TIMEOUT` to set the per-connection recv timeout (default: `5.0`).

Checklist

- [x] Implementation
- [x] Tests added
- [x] Documentation (CHANGELOG + docs/extension_dev.md)
- [x] CI workflow added

Notes

- The `execute` timeout cannot forcibly kill user code; it reports timeouts and leaves threads to complete. If stronger isolation is required we can add a subprocess-based executor for dangerous operations.

How to create the PR

- The branch has been pushed to `origin/harden-listener`.
- Create a PR at: https://github.com/phil-man-git-hub/FLAME-CODE/pull/new/harden-listener

If you want, I can try to create the PR via GitHub CLI if you authorize `gh` (run `gh auth login`) or provide a token in `GH_TOKEN` env var.

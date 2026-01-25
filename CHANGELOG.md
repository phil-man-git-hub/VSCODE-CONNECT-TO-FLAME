# Changelog

## Unreleased

- Repository scaffolded with docs, listener prototype, extension skeleton, and mock server.

### Harden listener and diagnostics (flame-listener)

- Add thread tracking and `atexit` cleanup to join background threads on shutdown. ✅
- Surface background-thread and unhandled exceptions using `threading.excepthook` and `sys.excepthook`. 🔍
- Run `execute` requests in worker threads with configurable per-request timeout (`timeout` request field). ⏱️
- Add configurable socket recv timeout (`FLAME_LISTENER_RECV_TIMEOUT`) and structured logs written to `FLAME_LISTENER_LOG` (default `/tmp/flame_listener.log`). 📁
- Make `start_debug_server` non-blocking: immediate ACK + background in-process debug adapter with attach logging and diagnostics (uses `wait_for_client` with timeout). 🧩
- Add unit/integration tests for timeout, thread-exception logging, debug start lifecycle, and recv-timeout behavior; add CI workflow. ✅


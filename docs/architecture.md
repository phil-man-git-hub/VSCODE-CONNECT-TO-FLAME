# Architecture

This project uses a small three‑component architecture:

- Flame listener (inside Flame) — executes Python code on the Flame main thread and returns stdout/stderr/exceptions.
- VS Code extension — sends code to the listener, shows output, manages connection and stubs.
- Stub generator — generates `.pyi` files so VS Code can provide autocomplete and type information.

Threading and execution model

All calls to the Flame API must be run on Flame's main/UI thread. The listener should receive code and schedule its execution using `flame.execute_on_main_thread()` (or equivalent) to avoid UI races.

Security and lifecycle

- Bind to localhost or use Unix domain sockets. Default to local-only access.
- Use a token-based handshake or restrict to OS-level local sockets for access control.
- Start the listener via Flame's Python startup mechanism so it is available whenever Flame runs.

Testing

Provide a `mock_flame_server.py` for local development and CI testing to allow extension development without an actual Flame instance.

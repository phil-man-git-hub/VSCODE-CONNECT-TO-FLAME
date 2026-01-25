# Communication Protocol

Transport

- TCP socket (localhost) — easiest for cross-platform dev.
- Optional: Unix domain socket for local-only secure communication.

Message format

Client → Listener (JSON):

```json
{
  "command": "execute",
  "id": "uuid-or-counter",
  "token": "optional-auth-token",
  "code": "print('hello from VS Code')"
}
```

Listener → Client (JSON response):

```json
{
  "id": "same-id",
  "stdout": "Hello\n",
  "stderr": "",
  "exception": null
}
```

Commands

- `execute` — run the provided code; return stdout/stderr and any exception details.
- `ping` — health check.
- `open_file` (optional) — request Flame to open or load a file.

Notes

- All responses must include the request `id` to allow in-flight matching and timeouts.
- Keep messages compact; only serialize structured data in JSON. Use base64 for binary payloads if needed.

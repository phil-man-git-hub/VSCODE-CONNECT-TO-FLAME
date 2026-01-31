# Communication Protocol: fu_relay

The **fu_relay** layer manages the JSON-over-TCP communication between external tools and the internal Flame listener.

## Transport
- **TCP Socket (127.0.0.1)**: Default transport for cross-platform stability.
- **Default Port**: 5555.

## Message format

### Client → fu_eavesdrop (JSON)
```json
{
  "command": "execute",
  "id": "uuid-v4-string",
  "token": "your-security-token",
  "code": "import flame; print(flame.project.current_project.name)",
  "timeout": 5.0
}
```

### fu_eavesdrop → Client (JSON response)
```json
{
  "id": "matching-uuid-v4",
  "stdout": "Project_Name\n",
  "stderr": "",
  "exception": null
}
```

## Available Commands

*   **`execute`**: Executes the provided Python code on the Flame main thread. Returns stdout, stderr, and any exception name.
*   **`ping`**: Returns `pong` if the listener is alive. Used by **fu_whisper** to verify connection.
*   **`start_debug_server`**: Launches an in-process `debugpy` adapter for remote debugging.

## Error Handling
- **ConnectionRefusedError**: `fu_eavesdrop` is not running or port is blocked.
- **TimeoutError**: The Python code took longer than the requested `timeout` (default 5s).
- **AuthError**: The provided `token` is missing or incorrect.
import socket
import json
import uuid
import os
from typing import Dict, Any, Optional

class FlameRelay:
    def __init__(self, host: str = "127.0.0.1", port: int = 5555):
        self.host = host
        self.port = port
        self.token = self._load_token()

    def _load_token(self) -> Optional[str]:
        # 1. Try environment variable
        token = os.environ.get("FLAME_TOKEN")
        if token:
            return token
        
        # 2. Try .flame.secrets.json in root or flame-listener dir
        possible_paths = [
            ".flame.secrets.json",
            "flame.project.json",
            "flame-listener/.flame.secrets.json"
        ]
        
        for path in possible_paths:
            full_path = os.path.join(os.getcwd(), path)
            if os.path.exists(full_path):
                try:
                    with open(full_path, "r") as f:
                        data = json.load(f)
                        return data.get("token")
                except Exception:
                    continue
        return None

    def send_command(self, command: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Sends a JSON command over TCP to the Flame Listener."""
        request = {
            "id": str(uuid.uuid4()),
            "command": command,
            "token": self.token,
            **payload
        }

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(10.0)
                s.connect((self.host, self.port))
                s.sendall(json.dumps(request).encode("utf-8"))
                
                # Receive response
                data = b""
                while True:
                    chunk = s.recv(4096)
                    if not chunk:
                        break
                    data += chunk
                    try:
                        return json.loads(data.decode("utf-8"))
                    except json.JSONDecodeError:
                        continue
        except ConnectionRefusedError:
            return {"exception": "ConnectionRefusedError", "stderr": "Flame Listener not found. Is it running?"}
        except socket.timeout:
            return {"exception": "TimeoutError", "stderr": "Flame Listener timed out."}
        except Exception as e:
            return {"exception": type(e).__name__, "stderr": str(e)}

    def execute(self, code: str, timeout: float = 5.0) -> Dict[str, Any]:
        return self.send_command("execute", {"code": code, "timeout": timeout})

    def ping(self) -> bool:
        response = self.send_command("ping", {})
        return response.get("stdout") == "pong"

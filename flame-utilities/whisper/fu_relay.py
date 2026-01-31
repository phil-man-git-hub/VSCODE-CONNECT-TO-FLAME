import socket
import json
import uuid
import os
from typing import Dict, Any, Optional

class FlameRelay:
    """The secure communication conduit (fu_relay) between FU_Whisper and fu_eavesdrop."""
    def __init__(self, host: str = "127.0.0.1", port: int = 5555):
        self.host = host
        self.port = port
        self.token = self._load_token()

    def _load_token(self) -> Optional[str]:
        # 1. Try environment variable
        token = os.environ.get("FLAME_TOKEN")
        if token:
            return token
        
        # 2. Try secrets/config in standard locations
        possible_paths = [
            ".flame.secrets.json",
            "flame-utilities/config/fu_eavesdrop.json",
            "flame-utilities/config/fu_secrets.json",
            "flame-utilities/.flame.secrets.json"
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
        """Sends a JSON command over TCP to the fu_eavesdrop listener."""
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
            return {"exception": "ConnectionRefusedError", "stderr": "fu_eavesdrop not found. Is it running inside Flame?"}
        except socket.timeout:
            return {"exception": "TimeoutError", "stderr": "fu_eavesdrop timed out."}
        except Exception as e:
            return {"exception": type(e).__name__, "stderr": str(e)}

    def execute(self, code: str, timeout: float = 5.0) -> Dict[str, Any]:
        return self.send_command("execute", {"code": code, "timeout": timeout})

    def ping(self) -> bool:
        response = self.send_command("ping", {})
        return response.get("stdout") == "pong"

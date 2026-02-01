import json
import urllib.request
import urllib.parse
import uuid
import os
from typing import Dict, Any, Optional

# Note: WebSocket support requires 'websocket-client' package.
# We use standard urllib where possible to minimize dependencies for the base platform.

class ComfyUIClient:
    """Technical bridge for ComfyUI API integration."""
    
    def __init__(self, server_address: str = "127.0.0.1:8188"):
        self.server_address = server_address
        self.client_id = str(uuid.uuid4())

    def queue_prompt(self, prompt: Dict[str, Any]) -> Dict[str, Any]:
        p = {"prompt": prompt, "client_id": self.client_id}
        data = json.dumps(p).encode('utf-8')
        req = urllib.request.Request(f"http://{self.server_address}/prompt", data=data)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

    def get_image(self, filename: str, subfolder: str, folder_type: str) -> bytes:
        data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
        url_values = urllib.parse.urlencode(data)
        with urllib.request.urlopen(f"http://{self.server_address}/view?{url_values}") as response:
            return response.read()

    def get_history(self, prompt_id: str) -> Dict[str, Any]:
        with urllib.request.urlopen(f"http://{self.server_address}/history/{prompt_id}") as response:
            return json.loads(response.read())

    def upload_image(self, input_path: str, name: str, overwrite: bool = False) -> Dict[str, Any]:
        with open(input_path, 'rb') as f:
            file_data = f.read()
            
        import mimetypes
        
        boundary = '----------Boundary_%s' % uuid.uuid4().hex
        headers = {'Content-Type': 'multipart/form-data; boundary=%s' % boundary}
        
        body = []
        body.append(('--' + boundary).encode('utf-8'))
        body.append(('Content-Disposition: form-data; name="image"; filename="%s"' % name).encode('utf-8'))
        body.append(('Content-Type: %s' % (mimetypes.guess_type(name)[0] or 'application/octet-stream')).encode('utf-8'))
        body.append(b'')
        body.append(file_data)
        body.append(('--' + boundary + '--').encode('utf-8'))
        body.append(b'')
        
        payload = b'\r\n'.join(body)
        req = urllib.request.Request(f"http://{self.server_address}/upload/image", data=payload, headers=headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())

# Integration platform logic for fu_whisper to consume
def get_comfy_status(server_address: str = "127.0.0.1:8188") -> bool:
    """Check if ComfyUI is reachable."""
    try:
        # object_info is a reliable way to check if the backend is alive and well
        urllib.request.urlopen(f"http://{server_address}/object_info", timeout=2)
        return True
    except:
        return False

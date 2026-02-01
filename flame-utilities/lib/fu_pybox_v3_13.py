"""
FU_PyBox v3.13 SDK
------------------
A clean-room, Python 3.13 native implementation of the Autodesk Flame PyBox protocol.
This module provides the base class and utility functions for creating modern PyBox handlers.

Architecture:
- Stateless execution via JSON payload.
- Native Pathlib integration for image sequences.
- PEP 484 Type Hinting.
- Python 3.13+ optimizations.
"""

import json
import sys
import logging
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union, Self

# Setup basic logging for debugging handlers
logging.basicConfig(level=logging.INFO, format='[fu_pybox][%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class PyBoxError(Exception):
    """Base exception for PyBox related errors."""
    pass

class PyBoxEncoder(json.JSONEncoder):
    """Custom encoder to handle Path objects and other non-standard types."""
    def default(self, obj):
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)

class BaseClass:
    """
    The modern base class for all PyBox v3.13 handlers.
    Handlers should inherit from this class and override lifecycle methods.
    """

    # --- Protocol Constants (Internal) ---
    __VALID_STATES = {"initialize", "setup_ui", "execute", "teardown"}
    __VALID_IMG_FORMATS = {"jpeg", "exr", "sgi", "tga", "tiff"}
    
    # Payload keys
    __IN = "in"
    __OUT = "out"
    __PAGES = "pages"
    __RENDER_ELEMENTS = "render_elements"
    __GLOBAL_ELEMENTS = "global_elements"
    __PATH = "path"
    __DESCRIPTION = "description"
    __VALUE = "value"
    __VALUES = "values"
    __PROCESS = "process"
    __PARAMS = "params"
    __METADATA = "adsk_metadata"
    __MESSAGE = "message"

    def __init__(self, json_path: Union[str, Path], utility_path: Optional[Union[str, Path]] = None):
        """
        Initialize the handler by loading the JSON payload from Flame.
        
        Args:
            json_path: Path to the temporary JSON file (usually sys.argv[1]).
            utility_path: Optional path to external utilities (usually sys.argv[2]).
        """
        self._path = Path(json_path)
        self._utility_path = Path(utility_path) if utility_path else None
        
        if not self._path.exists():
            raise PyBoxError(f"Payload file not found: {self._path}")

        with open(self._path, 'r', encoding='utf-8') as f:
            self.__dict__.update(json.load(f))

        if not hasattr(self, "state_id"):
            raise PyBoxError("Payload is missing required 'state_id' field.")

        # Handle UI Changes (Diffing)
        self.ui_changes: List[Dict[str, Any]] = []
        prev_data_str = getattr(self, "previous_data", None)
        if prev_data_str:
            try:
                prev_data = json.loads(prev_data_str)
                self._compute_ui_diff(prev_data)
            except (json.JSONDecodeError, KeyError) as e:
                logger.warning(f"Failed to parse previous_data for diffing: {e}")

    def _compute_ui_diff(self, prev_data: Dict[str, Any]) -> None:
        """Internal helper to find which UI elements changed since the last execution."""
        def diff_elements(pool_key: str):
            prev_pool = prev_data.get("dynamic_ui", {}).get(pool_key, {})
            curr_pool = self.dynamic_ui.get(pool_key, {})
            for name, curr_elem in curr_pool.items():
                prev_elem = prev_pool.get(name)
                if prev_elem and curr_elem != prev_elem:
                    self.ui_changes.append(curr_elem)

        diff_elements(self.__GLOBAL_ELEMENTS)
        diff_elements(self.__RENDER_ELEMENTS)

    # --- Lifecycle Methods (To be overridden) ---

    def initialize(self) -> None:
        """Phase 1: Define sockets and image formats."""
        raise NotImplementedError("Subclasses must implement initialize()")

    def setup_ui(self) -> None:
        """Phase 2: Build the node interface."""
        raise NotImplementedError("Subclasses must implement setup_ui()")

    def execute(self) -> None:
        """Phase 3: Perform actual processing/rendering."""
        raise NotImplementedError("Subclasses must implement execute()")

    def teardown(self) -> None:
        """Phase 4: Cleanup resources."""
        pass

    # --- Orchestration ---

    def dispatch(self) -> None:
        """Executes the method corresponding to the current state_id."""
        logger.info(f"Dispatching state: {self.state_id}")
        method = getattr(self, self.state_id, None)
        if not method:
            raise PyBoxError(f"Unknown state_id: {self.state_id}")
        method()

    def set_state_id(self, state_id: str) -> None:
        """Transitions the handler to the next state."""
        if state_id not in self.__VALID_STATES:
            raise ValueError(f"Invalid state transition: {state_id}")
        self.state_id = state_id

    def write_to_disk(self) -> None:
        """Writes the updated state back to the JSON payload for Flame to read."""
        # Prepare 'previous_data' for the next iteration's diff
        current_state = self.__dict__.copy()
        current_state.pop("_path", None)
        current_state.pop("_utility_path", None)
        current_state.pop("ui_changes", None)
        
        # In the original protocol, 'previous_data' is a JSON string inside the JSON
        self.previous_data = json.dumps(current_state, cls=PyBoxEncoder)
        
        with open(self._path, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, indent=4, sort_keys=True, cls=PyBoxEncoder)
        logger.info(f"Payload updated: {self._path}")

    # --- Metadata Getters ---

    def get_frame(self) -> int:
        return int(self.adsk_metadata.get("frame", 0))

    def get_project_name(self) -> str:
        return str(self.adsk_metadata.get("project", "Unknown"))

    def get_shot_name(self) -> str:
        return str(self.adsk_metadata.get("shot_name", ""))

    # --- Socket Management ---

    def set_in_socket(self, idx: int, socket_type: str, path: Union[str, Path]) -> None:
        while len(self.sockets[self.__IN]) <= idx:
            self.sockets[self.__IN].append({self.__PATH: "", self.__DESCRIPTION: "undefined"})
        
        self.sockets[self.__IN][idx] = {
            self.__PATH: str(path),
            self.__DESCRIPTION: socket_type
        }

    def set_out_socket(self, idx: int, socket_type: str, path: Union[str, Path]) -> None:
        while len(self.sockets[self.__OUT]) <= idx:
            self.sockets[self.__OUT].append({self.__PATH: "", self.__DESCRIPTION: "undefined"})
        
        self.sockets[self.__OUT][idx] = {
            self.__PATH: str(path),
            self.__DESCRIPTION: socket_type
        }

    # --- UI Management ---

    def set_ui_pages(self, *pages: Dict[str, Any]) -> None:
        self.dynamic_ui[self.__PAGES] = list(pages)

    def add_global_elements(self, *elements: Dict[str, Any]) -> None:
        for e in elements:
            self.dynamic_ui[self.__GLOBAL_ELEMENTS][e["name"]] = e

    def add_render_elements(self, *elements: Dict[str, Any]) -> None:
        for e in elements:
            self.dynamic_ui[self.__RENDER_ELEMENTS][e["name"]] = e

    def set_error_msg(self, msg: str) -> None:
        self.message["error"] = msg

    def set_img_format(self, img_format: str) -> None:
        """Set the image format for exported frames."""
        if img_format not in self.__VALID_IMG_FORMATS:
            raise ValueError(f"Invalid image format: {img_format}")
        self.adsk_metadata["format"] = img_format

    def is_processing(self) -> bool:
        """Returns True if Flame is currently requesting a render/process."""
        return hasattr(self, self.__PROCESS)

# --- UI Creation Helpers (Factory Functions) ---

def create_page(name: str, *cols: str) -> Dict[str, Any]:
    return {"name": name, "col": list(cols)}

def create_float_numeric(
    name: str, 
    value: float = 0.0, 
    min_val: float = 0.0, 
    max_val: float = 100.0, 
    row: int = 0, 
    col: int = 0, 
    page: int = 0,
    tooltip: str = ""
) -> Dict[str, Any]:
    return {
        "type": "Float",
        "name": name,
        "value": float(value),
        "default": float(value),
        "min": float(min_val),
        "max": float(max_val),
        "row": int(row),
        "col": int(col),
        "page": int(page),
        "tooltip": str(tooltip),
        "channel_name": name.replace(" ", "_") + "_chn"
    }

def create_toggle_button(
    name: str, 
    value: bool = False, 
    row: int = 0, 
    col: int = 0, 
    page: int = 0
) -> Dict[str, Any]:
    return {
        "type": "Toggle",
        "name": name,
        "value": bool(value),
        "default": bool(value),
        "row": int(row),
        "col": int(col),
        "page": int(page)
    }

def create_file_browser(
    name: str, 
    path: str = "", 
    extension: str = "exr", 
    row: int = 0, 
    col: int = 0, 
    page: int = 0
) -> Dict[str, Any]:
    return {
        "type": "Browser",
        "name": name,
        "value": str(path),
        "extension": str(extension),
        "row": int(row),
        "col": int(col),
        "page": int(page),
        "home": os.environ.get("HOME", "/")
    }

def create_text_field(
    name: str, 
    value: str = "", 
    row: int = 0, 
    col: int = 0, 
    page: int = 0
) -> Dict[str, Any]:
    return {
        "type": "TextField",
        "name": name,
        "value": str(value),
        "row": int(row),
        "col": int(col),
        "page": int(page)
    }

def create_vector_numeric(
    name: str,
    size: int = 3,
    values: Optional[List[float]] = None,
    min_val: float = -1000000.0,
    max_val: float = 1000000.0,
    row: int = 0,
    col: int = 0,
    page: int = 0
) -> Dict[str, Any]:
    if values is None:
        values = [0.0] * size
    
    # Generate component info (x, y, z)
    suffixes = ["x", "y", "z"]
    info = []
    for i in range(size):
        info.append({
            "min": float(min_val),
            "max": float(max_val),
            "default": float(values[i]),
            "inc": 1.0,
            "channel_name": f"{name}_{suffixes[i]}",
            "display_name": suffixes[i].upper()
        })

    return {
        "type": "FloatVector",
        "name": name,
        "row": int(row),
        "col": int(col),
        "page": int(page),
        "values": [float(v) for v in values],
        "info": info,
        "channel_name": name.replace(" ", "_") + "_chn"
    }

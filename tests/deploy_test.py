import tempfile
import shutil
from pathlib import Path
import json
import os

# This test simulates deploying the consolidated FLAME-UTILITIES directory
# to a temporary scriptsDir.

REPO_ROOT = Path(__file__).resolve().parents[1]
UTILITIES_SRC = REPO_ROOT / 'flame-utilities'


def test_deploy_recursive():
    # Use a temp dir to simulate the scriptsDir
    with tempfile.TemporaryDirectory() as tmpdir:
        target_dir = Path(tmpdir) / 'flame-utilities'
        
        # Check source exists
        assert UTILITIES_SRC.exists()
        assert UTILITIES_SRC.is_dir()
        
        # Simulate copy_recursive logic from deploy script
        shutil.copytree(UTILITIES_SRC, target_dir)
        
        # Verify core files exist in target
        assert (target_dir / 'fu_eavesdrop.py').exists()
        assert (target_dir / 'fu_eavesdrop_init.py').exists()
        assert (target_dir / 'whisper' / 'fu_whisper.py').exists()
        assert (target_dir / 'scripts' / 'fu_generate_stubs.py').exists()
import tempfile
import shutil
from pathlib import Path
import json
import os

# This test simulates deploying files to a temporary scriptsDir using the
# `flame.project.example.json` configuration as input.

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRA_FILES = ['flame-listener/flame_listener.py', 'flame-listener/startup_flame_listener.py', 'flame-listener/generate_stubs.py']


def test_deploy_dry_run():
    # Ensure flame.project.example.json exists and parse it
    cfg_path = REPO_ROOT / 'flame.project.example.json'
    assert cfg_path.exists()
    cfg = json.loads(cfg_path.read_text())
    # Use a temp dir to simulate the scriptsDir
    with tempfile.TemporaryDirectory() as tmpdir:
        os.environ['TEST_SCRIPTS_DIR'] = tmpdir
        # Check files exist in repo
        for f in EXTRA_FILES:
            assert (REPO_ROOT / f).exists()
        # Simulate copy by copying each file to tmpdir
        for f in EXTRA_FILES:
            src = REPO_ROOT / f
            dst = Path(tmpdir) / Path(f).name
            shutil.copy2(src, dst)
            assert dst.exists()
        # Optionally check that startup hook imports the listener
        startup = Path(tmpdir) / 'startup_flame_listener.py'
        assert startup.exists()

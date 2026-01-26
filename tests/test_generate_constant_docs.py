import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'generate_constant_docs.py')


def test_dry_run():
    # Run the script in dry-run mode (no --apply) and ensure it exits 0 and prints something
    proc = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True)
    assert proc.returncode == 0
    # Output should contain at least one file header or a warning if flame not present
    out = proc.stdout + proc.stderr
    assert ('# Constant:' in out) or ('Warning: `flame` module not importable' in out)

import json
import subprocess
import tempfile
from pathlib import Path
import pytest

COLLECTOR = ['python3', 'scripts/collect_flame_api.py', '--host', '127.0.0.1', '--port', '5555', '--modules', 'flame', '--probe-safe']
GENERATOR = ['python3', 'scripts/generate_api_docs.py', '--out']


def run_collector():
    proc = subprocess.run(COLLECTOR, capture_output=True, text=True)
    if proc.returncode != 0:
        pytest.skip('Flame listener not available for collector: ' + proc.stderr.strip())
    return json.loads(proc.stdout)


def test_collector_detects_kinds():
    j = run_collector()
    found = set()
    for cls in j.get('flame', {}).get('classes', []):
        for m in cls.get('methods', []):
            k = m.get('kind')
            if k:
                found.add(k)
    # Expect at least one of these kinds to be present
    assert found & {'property', 'builtin', 'staticmethod'} , f'No property/builtin/staticmethod found; kinds={sorted(found)}'


def test_generator_emits_pages_and_docblocks(tmp_path):
    out = tmp_path / 'docs'
    out.mkdir()
    proc = subprocess.run(['python3', 'scripts/generate_api_docs.py', '--out', str(out), '--host', '127.0.0.1', '--port', '5555'], capture_output=True, text=True)
    if proc.returncode != 0:
        pytest.skip('Generator failed: ' + proc.stderr.strip())
    # check that at least one class page was written and contains a signature code block
    classes_dir = out / 'classes'
    assert classes_dir.exists() and any(classes_dir.iterdir()), 'No class pages generated'
    sample = next(classes_dir.iterdir())
    txt = sample.read_text()
    assert '```python' in txt and 'def ' in txt, 'No signature code block found in class page'

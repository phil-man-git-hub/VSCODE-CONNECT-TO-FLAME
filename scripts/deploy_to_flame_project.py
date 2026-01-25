"""Deploy flame listener files into a Flame project `scriptsDir`.

Usage:
  python scripts/deploy_to_flame_project.py --dry-run
  python scripts/deploy_to_flame_project.py --copy

It looks for `flame.project.json` in the repository root and copies the
following files into the configured `scriptsDir`:
 - flame_listener.py
 - generate_stubs.py
 - startup_flame_listener.py
 - (optional) .flame.secrets.json (if present in repo root)

The script will create the target directory if needed and set permissive
permissions so Flame can read the files.
"""

import argparse
import json
import os
import shutil
import stat
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRA_FILES = ['flame-listener/flame_listener.py', 'flame-listener/generate_stubs.py', 'flame-listener/startup_flame_listener.py']


def load_project_config():
    cfg_path = REPO_ROOT / 'flame.project.json'
    if not cfg_path.exists():
        raise FileNotFoundError('flame.project.json not found in repo root')
    with open(cfg_path, 'r') as f:
        return json.load(f)


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def copy_file(src: Path, dst: Path):
    shutil.copy2(src, dst)
    # ensure readable
    dst.chmod(dst.stat().st_mode | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


def main(dry_run: bool):
    cfg = load_project_config()
    scripts_dir = cfg.get('scriptsDir')
    if not scripts_dir:
        raise ValueError('scriptsDir is not configured in flame.project.json')
    target = Path(scripts_dir)
    print(f'Target scripts dir: {target}')
    if dry_run:
        print('Dry run: the following files would be copied:')
        for f in EXTRA_FILES:
            print(f' - {REPO_ROOT / f} -> {target / Path(f).name}')
        secrets = REPO_ROOT / '.flame.secrets.json'
        if secrets.exists():
            print(f' - {secrets} -> {target / secrets.name} (secrets)')
        return
    ensure_dir(target)
    for f in EXTRA_FILES:
        src = REPO_ROOT / f
        if not src.exists():
            raise FileNotFoundError(f'{src} not found')
        dst = target / Path(f).name
        print(f'Copying {src} -> {dst}')
        copy_file(src, dst)
    # Optional: copy secrets if present
    secrets = REPO_ROOT / '.flame.secrets.json'
    if secrets.exists():
        dst = target / secrets.name
        print(f'Copying secrets {secrets} -> {dst}')
        copy_file(secrets, dst)
    print('Deployment complete. When launching Flame, ensure the project uses this scripts dir.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Show what will be copied')
    parser.add_argument('--copy', action='store_true', help='Actually copy files')
    args = parser.parse_args()
    if args.copy:
        main(dry_run=False)
    else:
        main(dry_run=True)

"""Deploy the consolidated FLAME-UTILITIES toolkit into a Flame project `scriptsDir`.

Usage:
  python scripts/deploy_to_flame_project.py --dry-run
  python scripts/deploy_to_flame_project.py --copy

It looks for `flame.project.json` in the repository root and copies the
entire `flame-utilities/` directory into the configured `scriptsDir`.

The script will also copy (optional) .flame.secrets.json into the target directory.
"""

import argparse
import json
import os
import shutil
import stat
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
UTILITIES_SRC = REPO_ROOT / 'flame-utilities'


def load_project_config():
    cfg_path = REPO_ROOT / 'flame-utilities' / 'config' / 'fu_eavesdrop.json'
    if not cfg_path.exists():
        # Fallback for local dev if not moved yet
        cfg_path = REPO_ROOT / 'flame.project.json'
        
    if not cfg_path.exists():
        raise FileNotFoundError('Configuration file (fu_eavesdrop.json) not found')
    with open(cfg_path, 'r') as f:
        return json.load(f)


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def copy_recursive(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    # Ensure all files are readable
    for root, dirs, files in os.walk(dst):
        for d in dirs:
            os.chmod(os.path.join(root, d), 0o755)
        for f in files:
            os.chmod(os.path.join(root, f), 0o644)


def main(dry_run: bool, scripts_dir_arg: str = None):
    if scripts_dir_arg:
        target_parent = Path(scripts_dir_arg)
    else:
        try:
            cfg = load_project_config()
            scripts_dir = cfg.get('scriptsDir')
            if not scripts_dir:
                raise ValueError('scriptsDir is not configured in fu_eavesdrop.json')
            target_parent = Path(scripts_dir)
        except FileNotFoundError:
            raise FileNotFoundError('scriptsDir must be provided via --scripts-dir or fu_eavesdrop.json')

    # The utilities source should live in /setups/flame-utilities/
    # while the ignite script lives in /setups/python/
    target_parent = Path(scripts_dir).parent
    target_utilities = target_parent / 'flame-utilities'
    
    print(f'Deployment Target: {target_utilities}')
    
    if dry_run:
        print('Dry run: The entire flame-utilities/ directory would be copied.')
        print(f' - {UTILITIES_SRC} -> {target_utilities}')
        secrets = REPO_ROOT / '.flame.secrets.json'
        if secrets.exists():
            print(f' - {secrets} -> {target_utilities / secrets.name} (secrets)')
        return

    ensure_dir(target_parent)
    print(f'Copying {UTILITIES_SRC} -> {target_utilities}')
    copy_recursive(UTILITIES_SRC, target_utilities)
    
    # Optional: copy secrets if present into the utilities folder
    secrets = REPO_ROOT / '.flame.secrets.json'
    if secrets.exists():
        dst_secrets = target_utilities / secrets.name
        print(f'Copying secrets {secrets} -> {dst_secrets}')
        shutil.copy2(secrets, dst_secrets)
        dst_secrets.chmod(dst_secrets.stat().st_mode | stat.S_IRUSR)

    print('\nDeployment complete.')
    print('IMPORTANT: To activate the toolkit in Flame, ensure you have a loader script')
    print('in the parent directory that adds flame-utilities to sys.path.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scripts-dir', help='Target scripts directory to copy files into')
    parser.add_argument('--dry-run', action='store_true', help='Show what will be copied')
    parser.add_argument('--copy', action='store_true', help='Actually copy files')
    args = parser.parse_args()
    if args.copy:
        main(dry_run=False, scripts_dir_arg=args.scripts_dir)
    else:
        main(dry_run=True, scripts_dir_arg=args.scripts_dir)
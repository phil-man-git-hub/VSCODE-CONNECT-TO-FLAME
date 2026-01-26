#!/usr/bin/env python3
"""Bump __version__ in flame-listener files following project rules.

Usage: python scripts/bump_flame_versions.py [--apply] [--deploy]

- With no flags, the script will show the current and next versions for tracked files.
- With --apply it will update the files in-place (committing the change is left to the developer).
- With --deploy it will also call the repo's deploy script to copy the updated files into the configured Flame project.
"""
import argparse
import re
from pathlib import Path
from scripts.deploy_to_flame_project import main as deploy_main

REPO_ROOT = Path(__file__).resolve().parents[1]
TRACKED = [REPO_ROOT / 'flame-listener' / 'flame_listener.py', REPO_ROOT / 'flame-listener' / 'startup_flame_listener.py']
RE_PAT = re.compile(r"__version__\s*=\s*['\"](\d+\.\d+\.\d+)['\"]")


def next_version(v: str) -> str:
    major, minor, patch = [int(x) for x in v.split('.')]
    patch += 1
    if patch >= 10:
        patch = 0
        minor += 1
    if minor >= 10:
        minor = 0
        major += 1
    return f"{major}.{minor}.{patch}"


def find_and_bump(path: Path, apply: bool = False) -> tuple[str, str]:
    txt = path.read_text()
    m = RE_PAT.search(txt)
    if not m:
        raise ValueError(f"No __version__ found in {path}")
    cur = m.group(1)
    nxt = next_version(cur)
    print(f"{path.name}: {cur} -> {nxt}")
    if apply:
        new_txt = RE_PAT.sub(f"__version__ = '{nxt}'", txt, count=1)
        path.write_text(new_txt)
    return cur, nxt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--deploy', action='store_true')
    parser.add_argument('--scripts-dir', help='Optional target scripts dir to pass to deploy script')
    args = parser.parse_args()
    for p in TRACKED:
        find_and_bump(p, apply=args.apply)
    if args.deploy and args.apply:
        # run the existing deploy script to copy files into Flame project
        deploy_main(dry_run=False, scripts_dir_arg=args.scripts_dir)
    elif args.deploy and not args.apply:
        print('Use --apply with --deploy to deploy the bumped files.')

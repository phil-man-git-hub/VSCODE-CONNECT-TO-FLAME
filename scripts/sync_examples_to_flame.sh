#!/usr/bin/env bash
set -euo pipefail

# sync_examples_to_flame.sh
# Usage:
#   ./scripts/sync_examples_to_flame.sh           # dry-run (safe preview)
#   ./scripts/sync_examples_to_flame.sh --apply   # actually apply changes
#   ./scripts/sync_examples_to_flame.sh --apply src_dir dest_dir
#
# Default source: "examples/"
# Default dest:  /Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo/setups/python/examples/

DEFAULT_SRC="examples/"
DEFAULT_DEST="/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo/setups/python/examples/"

APPLY=0
if [[ ${1:-} == "--apply" ]]; then
    APPLY=1
    shift || true
fi

SRC=${1:-$DEFAULT_SRC}
DEST=${2:-$DEFAULT_DEST}

# rsync options:
# -a   : archive mode (preserve permissions, times, symlinks)
# -v   : verbose
# -h   : human readable output
# --progress : show progress
# --delete : remove files in DEST that don't exist in SRC
# --delete-after : perform deletions after transfer (safer for some workflows)
RSYNC_OPTS=( -avh --progress --delete --delete-after )

# Common excludes to avoid copying git metadata, editor swaps, pyc, caches
EXCLUDES=( --exclude='.git/' --exclude='*.pyc' --exclude='__pycache__/' --exclude='.DS_Store' --exclude='*.swp' )

# Show summary
echo "Source: $SRC"
echo "Destination: $DEST"
if [[ $APPLY -eq 0 ]]; then
    echo "Mode: dry-run (no changes). To apply, run with --apply"
    echo
    rsync "${RSYNC_OPTS[@]}" "${EXCLUDES[@]}" --dry-run "$SRC" "$DEST"
else
    echo "Mode: APPLY (this will modify the destination)"
    echo
    rsync "${RSYNC_OPTS[@]}" "${EXCLUDES[@]}" "$SRC" "$DEST"
    echo
    echo "Sync complete."
fi

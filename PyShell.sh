# !/bin/sh

# use the script to run PyShell locally

set -e # exit early if any commands fail

SCRIPT_DIR="$(dirname "$0")"
PYTHONSAFEPATH=1 PYTHONPATH="$SCRIPT_DIR" exec uv run --project "$SCRIPT_DIR" --quiet -m app.main "$2"

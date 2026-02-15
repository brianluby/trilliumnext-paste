#!/usr/bin/env bash
#
# paste-clipboard.sh — Grab the macOS clipboard and send it to TrilliumNext
#
# Reads the current clipboard contents via pbpaste and delegates
# to paste.sh for the actual ETAPI call.

set -euo pipefail

dir="$(cd "$(dirname "$0")" && pwd)"

clipboard=$(pbpaste)

if [ -z "$clipboard" ]; then
  echo "Clipboard is empty"
  exit 1
fi

echo "$clipboard" | "$dir/paste.sh"

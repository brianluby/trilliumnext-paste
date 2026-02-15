#!/usr/bin/env bash
#
# paste.sh — Create a new note in TrilliumNext via ETAPI
#
# Expected workflow variables (set in Alfred's workflow configuration):
#   TRILLIUMNEXT_URL        — Base URL of the TrilliumNext server
#   TRILLIUMNEXT_TOKEN      — ETAPI authentication token
#   TRILLIUMNEXT_PARENT_NOTE_ID — Parent note ID (defaults to "root")

set -euo pipefail

# Accept input as $1, or read from stdin if no argument given
if [ $# -ge 1 ] && [ -n "$1" ]; then
  query="$1"
elif [ ! -t 0 ]; then
  query=$(cat)
else
  echo "No input provided"
  exit 1
fi

if [ -z "$query" ]; then
  echo "No input provided"
  exit 1
fi

url="${TRILLIUMNEXT_URL:?Set TRILLIUMNEXT_URL in workflow configuration}"
token="${TRILLIUMNEXT_TOKEN:?Set TRILLIUMNEXT_TOKEN in workflow configuration}"
parent="${TRILLIUMNEXT_PARENT_NOTE_ID:-root}"

# Generate a title from the first line, truncated to 80 chars
title=$(echo "$query" | head -1 | cut -c1-80)

response=$(curl -s -w "\n%{http_code}" -X POST "${url}/etapi/create-note" \
  -H "Authorization: ${token}" \
  -H "Content-Type: application/json" \
  -d "$(cat <<EOF
{
  "parentNoteId": "${parent}",
  "title": $(printf '%s' "$title" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'),
  "type": "text",
  "content": $(printf '%s' "$query" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')
}
EOF
)")

http_code=$(echo "$response" | tail -1)
body=$(echo "$response" | sed '$d')

if [ "$http_code" -ge 200 ] && [ "$http_code" -lt 300 ]; then
  echo "Saved to TrilliumNext"
else
  echo "Error (${http_code}): ${body}"
  exit 1
fi

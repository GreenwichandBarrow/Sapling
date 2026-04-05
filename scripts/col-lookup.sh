#!/bin/bash
# col-lookup.sh — Thin wrapper that delegates to col-lookup.py
# Kept for backward compatibility with existing skill references.
#
# Usage is identical:
#   col-lookup.sh <sheet_id> <tab> "Header Name"
#   col-lookup.sh <sheet_id> <tab> --batch "Header1,Header2,Header3"
#   col-lookup.sh <sheet_id> <tab> --cell "Company=Levin Art Group" "Header"
#   col-lookup.sh <sheet_id> <tab> --range "Company=Levin Art Group" "H1,H2"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/col-lookup.py" "$@"

#!/bin/bash
# col-lookup.sh — Resolve Google Sheets column headers to cell references
#
# Three modes:
#   COLUMN:  col-lookup.sh <sheet_id> <tab> "Header Name"                              → O
#   BATCH:   col-lookup.sh <sheet_id> <tab> --batch "Header1,Header2,Header3"           → JSON map
#   CELL:    col-lookup.sh <sheet_id> <tab> --cell "Company=Levin Art Group" "Header"   → O2
#   RANGE:   col-lookup.sh <sheet_id> <tab> --range "Company=Levin Art Group" "H1,H2"  → K2:M2
#
# Options:
#   --header-row N    Header row number (default: 1, use 2 for WEEKLY REVIEW)
#   --key-col NAME    Column to use as row identifier (default: Company)
#   --account EMAIL   Google account (default: $GOG_ACCOUNT or kay.s@greenwichandbarrow.com)

set -euo pipefail

SHEET_ID=""
TAB=""
MODE="column"  # column, batch, cell, range
HEADER_ROW=1
KEY_COL="Company"
ACCOUNT="${GOG_ACCOUNT:-kay.s@greenwichandbarrow.com}"
HEADER_NAME=""
BATCH_HEADERS=""
CELL_KEY=""
RANGE_HEADERS=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --header-row)
      HEADER_ROW="$2"; shift 2 ;;
    --key-col)
      KEY_COL="$2"; shift 2 ;;
    --account)
      ACCOUNT="$2"; shift 2 ;;
    --batch)
      MODE="batch"; BATCH_HEADERS="$2"; shift 2 ;;
    --cell)
      MODE="cell"; CELL_KEY="$2"; shift ;;
    --range)
      MODE="range"; CELL_KEY="$2"; shift ;;
    *)
      if [[ -z "$SHEET_ID" ]]; then
        SHEET_ID="$1"
      elif [[ -z "$TAB" ]]; then
        TAB="$1"
      elif [[ "$MODE" == "cell" && -z "$HEADER_NAME" ]]; then
        HEADER_NAME="$1"
      elif [[ "$MODE" == "range" && -z "$RANGE_HEADERS" ]]; then
        RANGE_HEADERS="$1"
      else
        HEADER_NAME="$1"
      fi
      shift ;;
  esac
done

if [[ -z "$SHEET_ID" || -z "$TAB" ]]; then
  echo "Usage: col-lookup.sh <sheet_id> <tab> [options] <header_name>" >&2
  exit 1
fi

# Convert column index (0-based) to letter (A, B, ..., Z, AA, AB, ...)
idx_to_letter() {
  local idx=$1
  local result=""
  while true; do
    result=$(printf "\\$(printf '%03o' $((65 + idx % 26)))")${result}
    idx=$(( idx / 26 - 1 ))
    if [[ $idx -lt 0 ]]; then break; fi
  done
  echo "$result"
}

# Step 1: Read header row and build header→letter map
HEADER_RANGE="'${TAB}'!${HEADER_ROW}:${HEADER_ROW}"
HEADER_JSON=$(gog sheets get "$SHEET_ID" "$HEADER_RANGE" -a "$ACCOUNT" -j --results-only 2>/dev/null)

# Parse headers into associative array
declare -A HEADER_MAP
HEADER_LIST=""

# Extract values array from JSON
HEADERS=$(echo "$HEADER_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
values = data.get('values', [[]])[0] if isinstance(data, dict) else data[0] if isinstance(data, list) and data else []
for i, v in enumerate(values):
    if v:
        print(f'{i}\t{v}')
" 2>/dev/null)

while IFS=$'\t' read -r idx name; do
  [[ -z "$idx" ]] && continue
  letter=$(idx_to_letter "$idx")
  HEADER_MAP["$name"]="$letter"
  HEADER_LIST="${HEADER_LIST}  ${letter}=${name}\n"
done <<< "$HEADERS"

# Resolve a single header to its column letter
resolve_col() {
  local header="$1"
  local letter="${HEADER_MAP[$header]:-}"
  if [[ -z "$letter" ]]; then
    echo "ERROR: Header \"$header\" not found in tab '$TAB'." >&2
    echo "Available headers:" >&2
    echo -e "$HEADER_LIST" >&2
    exit 1
  fi
  echo "$letter"
}

# Step 2: If cell/range mode, resolve row by key column
resolve_row() {
  local key_value="$1"
  local key_letter
  key_letter=$(resolve_col "$KEY_COL")

  # Read the key column
  local data_start=$((HEADER_ROW + 1))
  local key_range="'${TAB}'!${key_letter}${data_start}:${key_letter}1000"
  local key_data
  key_data=$(gog sheets get "$SHEET_ID" "$key_range" -a "$ACCOUNT" -p 2>/dev/null)

  # Find the row
  local row_offset=0
  local found=0
  while IFS= read -r line; do
    row_offset=$((row_offset + 1))
    # Trim whitespace for comparison
    local trimmed
    trimmed=$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    if [[ "$trimmed" == "$key_value" ]]; then
      found=1
      break
    fi
  done <<< "$key_data"

  if [[ $found -eq 0 ]]; then
    echo "ERROR: Row key \"$KEY_COL=$key_value\" not found in tab '$TAB'." >&2
    exit 1
  fi

  echo $((data_start + row_offset - 1))
}

# Execute based on mode
case "$MODE" in
  column)
    if [[ -z "$HEADER_NAME" ]]; then
      echo "ERROR: No header name provided." >&2
      exit 1
    fi
    resolve_col "$HEADER_NAME"
    ;;

  batch)
    echo -n "{"
    first=1
    IFS=',' read -ra ITEMS <<< "$BATCH_HEADERS"
    for item in "${ITEMS[@]}"; do
      item=$(echo "$item" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
      letter=$(resolve_col "$item")
      if [[ $first -eq 1 ]]; then
        first=0
      else
        echo -n ","
      fi
      echo -n "\"$item\":\"$letter\""
    done
    echo "}"
    ;;

  cell)
    if [[ -z "$HEADER_NAME" ]]; then
      echo "ERROR: No header name provided for cell mode." >&2
      exit 1
    fi
    # Parse key=value from CELL_KEY
    IFS='=' read -r KEY_COL_OVERRIDE KEY_VALUE <<< "$CELL_KEY"
    KEY_COL="$KEY_COL_OVERRIDE"
    col_letter=$(resolve_col "$HEADER_NAME")
    row_num=$(resolve_row "$KEY_VALUE")
    echo "${col_letter}${row_num}"
    ;;

  range)
    if [[ -z "$RANGE_HEADERS" ]]; then
      echo "ERROR: No headers provided for range mode." >&2
      exit 1
    fi
    # Parse key=value from CELL_KEY
    IFS='=' read -r KEY_COL_OVERRIDE KEY_VALUE <<< "$CELL_KEY"
    KEY_COL="$KEY_COL_OVERRIDE"
    row_num=$(resolve_row "$KEY_VALUE")

    # Resolve each header, find min and max columns
    first_letter=""
    last_letter=""
    IFS=',' read -ra ITEMS <<< "$RANGE_HEADERS"
    for item in "${ITEMS[@]}"; do
      item=$(echo "$item" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
      letter=$(resolve_col "$item")
      if [[ -z "$first_letter" ]]; then
        first_letter="$letter"
        last_letter="$letter"
      else
        last_letter="$letter"
      fi
    done
    echo "${first_letter}${row_num}:${last_letter}${row_num}"
    ;;
esac

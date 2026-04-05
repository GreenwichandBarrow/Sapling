#!/usr/bin/env python3
"""col-lookup.py — Resolve Google Sheets column headers to cell references.

Four modes:
  COLUMN:  col-lookup.py <sheet_id> <tab> "Header Name"                              → O
  BATCH:   col-lookup.py <sheet_id> <tab> --batch "Header1,Header2,Header3"           → JSON map
  CELL:    col-lookup.py <sheet_id> <tab> --cell "Company=Levin Art Group" "Header"   → O2
  RANGE:   col-lookup.py <sheet_id> <tab> --range "Company=Levin Art Group" "H1,H2"  → K2:M2

Options:
  --header-row N    Header row number (default: 1, use 2 for WEEKLY REVIEW)
  --key-col NAME    Column to use as row identifier (default: Company)
  --account EMAIL   Google account (default: $GOG_ACCOUNT or kay.s@greenwichandbarrow.com)
"""

import argparse
import json
import os
import subprocess
import sys


def idx_to_letter(idx):
    """Convert 0-based column index to Excel-style letter (A, B, ..., Z, AA, AB, ...)."""
    result = ""
    while True:
        result = chr(65 + idx % 26) + result
        idx = idx // 26 - 1
        if idx < 0:
            break
    return result


def read_header_row(sheet_id, tab, header_row, account):
    """Read the header row and return a dict of {header_name: column_letter}."""
    header_range = f"'{tab}'!{header_row}:{header_row}"
    cmd = [
        "gog", "sheets", "get", sheet_id, header_range,
        "-a", account, "-j", "--results-only"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"ERROR: Failed to read headers from '{tab}': {e}", file=sys.stderr)
        sys.exit(1)

    # Parse the values array
    if isinstance(data, dict):
        values = data.get("values", [[]])[0]
    elif isinstance(data, list) and data:
        values = data[0] if data else []
    else:
        values = []

    header_map = {}
    for i, v in enumerate(values):
        if v:
            header_map[str(v)] = idx_to_letter(i)

    return header_map


def resolve_col(header_map, header_name, tab):
    """Resolve a header name to its column letter."""
    letter = header_map.get(header_name)
    if not letter:
        available = "\n".join(f"  {letter}={name}" for name, letter in sorted(header_map.items(), key=lambda x: x[1]))
        print(f'ERROR: Header "{header_name}" not found in tab \'{tab}\'.', file=sys.stderr)
        print("Available headers:", file=sys.stderr)
        print(available, file=sys.stderr)
        sys.exit(1)
    return letter


def resolve_row(sheet_id, tab, header_row, account, header_map, key_col, key_value):
    """Find the row number for a given key column value."""
    key_letter = resolve_col(header_map, key_col, tab)
    data_start = header_row + 1
    key_range = f"'{tab}'!{key_letter}{data_start}:{key_letter}1000"

    cmd = ["gog", "sheets", "get", sheet_id, key_range, "-a", account, "-p"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to read key column: {e}", file=sys.stderr)
        sys.exit(1)

    for i, line in enumerate(result.stdout.splitlines()):
        trimmed = line.strip()
        if trimmed == key_value:
            return data_start + i

    print(f'ERROR: Row key "{key_col}={key_value}" not found in tab \'{tab}\'.', file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Resolve Google Sheets column headers to cell references.")
    parser.add_argument("sheet_id", help="Google Sheet ID")
    parser.add_argument("tab", help="Tab/sheet name")
    parser.add_argument("--header-row", type=int, default=1, help="Header row number (default: 1)")
    parser.add_argument("--key-col", default="Company", help="Column to use as row identifier (default: Company)")
    parser.add_argument("--account", default=os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com"),
                        help="Google account")

    # Mode selection (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--batch", metavar="HEADERS", help="Comma-separated header names → JSON map")
    mode_group.add_argument("--cell", metavar="KEY=VALUE", help="Resolve to cell reference (e.g., Company=Acme)")
    mode_group.add_argument("--range", metavar="KEY=VALUE", help="Resolve to range reference")

    # Positional args for header name(s)
    parser.add_argument("headers", nargs="*", help="Header name(s) — single for column/cell mode, comma-separated for range mode")

    args = parser.parse_args()

    # Read header row
    header_map = read_header_row(args.sheet_id, args.tab, args.header_row, args.account)

    if args.batch:
        # Batch mode: return JSON map of header→letter
        items = [h.strip() for h in args.batch.split(",")]
        result = {}
        for item in items:
            result[item] = resolve_col(header_map, item, args.tab)
        print(json.dumps(result))

    elif args.cell:
        # Cell mode: resolve key=value + header → cell reference
        if not args.headers:
            print("ERROR: No header name provided for cell mode.", file=sys.stderr)
            sys.exit(1)
        key_col_override, key_value = args.cell.split("=", 1)
        header_name = args.headers[0]
        col_letter = resolve_col(header_map, header_name, args.tab)
        row_num = resolve_row(args.sheet_id, args.tab, args.header_row, args.account,
                              header_map, key_col_override, key_value)
        print(f"{col_letter}{row_num}")

    elif args.range:
        # Range mode: resolve key=value + headers → range reference
        if not args.headers:
            print("ERROR: No headers provided for range mode.", file=sys.stderr)
            sys.exit(1)
        key_col_override, key_value = args.range.split("=", 1)
        range_headers = [h.strip() for h in args.headers[0].split(",")]
        row_num = resolve_row(args.sheet_id, args.tab, args.header_row, args.account,
                              header_map, key_col_override, key_value)
        letters = [resolve_col(header_map, h, args.tab) for h in range_headers]
        print(f"{letters[0]}{row_num}:{letters[-1]}{row_num}")

    else:
        # Column mode: resolve single header → letter
        if not args.headers:
            print("ERROR: No header name provided.", file=sys.stderr)
            sys.exit(1)
        print(resolve_col(header_map, args.headers[0], args.tab))


if __name__ == "__main__":
    main()

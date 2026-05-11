#!/usr/bin/env python3
"""One-shot rescue: build Mon-Fri Call Log tabs for week of 2026-04-27 on
Premium Pest Management sheet from the Sunday-3pm pool artifact.

Sunday 6pm jj-operations launchd prep failed silently (gog sheets metadata
timeout). This script does what that fire was supposed to do.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("JJ_BUILD_WEEK_TABS_ROOT", str(_SCRIPT_DIR.parent)))
SHEET_ID = "1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I"
POOL_PATH = ROOT / "brain/context/jj-week-pool-2026-04-26.md"
WEEK_TABS = [
    "Call Log 4.27.26",
    "Call Log 4.28.26",
    "Call Log 4.29.26",
    "Call Log 4.30.26",
    "Call Log 5.01.26",
]
HEADER_RANGE = "Full Target List!A1:Y1"
DATA_RANGE = "Full Target List!A2:Y300"


def gog(args, timeout=180):
    res = subprocess.run(
        ["gog", *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if res.returncode != 0:
        print(f"!! gog {' '.join(args[:6])}... → exit {res.returncode}", file=sys.stderr)
        print(res.stderr[:1000], file=sys.stderr)
        sys.exit(2)
    return res.stdout


def parse_pool(path: Path) -> list[int]:
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("- row:"):
            try:
                rows.append(int(line.split(":", 1)[1].strip()))
            except ValueError:
                pass
    return sorted(set(rows))


def read_rows() -> tuple[list[str], dict[int, list[str]]]:
    header_tsv = gog(["sheets", "get", SHEET_ID, HEADER_RANGE, "--plain"]).rstrip("\n")
    headers = header_tsv.split("\t")
    while len(headers) < 25:
        headers.append("")

    data_tsv = gog(["sheets", "get", SHEET_ID, DATA_RANGE, "--plain"])
    rows_by_index: dict[int, list[str]] = {}
    for offset, line in enumerate(data_tsv.split("\n")):
        if line == "" and offset == len(data_tsv.split("\n")) - 1:
            continue
        sheet_row = offset + 2
        cells = line.split("\t")
        while len(cells) < 25:
            cells.append("")
        rows_by_index[sheet_row] = cells[:25]
    return headers, rows_by_index


def chunk_evenly(seq, n):
    out = [[] for _ in range(n)]
    for i, v in enumerate(seq):
        out[i % n].append(v)
    return out


def add_tab(name: str):
    print(f"  + add-tab '{name}'")
    gog(["sheets", "add-tab", SHEET_ID, name, "--no-input"])


def write_tab(name: str, headers: list[str], rows: list[list[str]]):
    """Write headers + rows to A1:Y{n+1} via --values-json."""
    payload = json.dumps([headers, *rows])
    range_a1 = f"{name}!A1:Y{len(rows) + 1}"
    print(f"  → write {len(rows)} rows to '{name}'")
    gog(
        [
            "sheets",
            "update",
            SHEET_ID,
            range_a1,
            "--values-json",
            payload,
            "--input",
            "RAW",
            "--no-input",
        ]
    )


def main():
    if not POOL_PATH.exists():
        print(f"FAIL: pool artifact not found: {POOL_PATH}", file=sys.stderr)
        sys.exit(2)

    pool_rows = parse_pool(POOL_PATH)
    print(f"Pool size: {len(pool_rows)} (rows {pool_rows[0]}–{pool_rows[-1]})")

    headers, all_rows = read_rows()
    print(f"Read {len(all_rows)} rows from Full Target List, {len(headers)} header cols")

    pool_data = []
    missing = []
    blank_owner = []
    for idx in pool_rows:
        if idx not in all_rows:
            missing.append(idx)
            continue
        row = all_rows[idx]
        if not row[10].strip():
            blank_owner.append(idx)
        pool_data.append(row)

    if missing:
        print(
            f"FAIL: {len(missing)} pool rows not in Full Target List: {missing[:10]}",
            file=sys.stderr,
        )
        sys.exit(2)

    if blank_owner:
        print(f"WARN: {len(blank_owner)} rows have blank Col K (Owner): {blank_owner[:10]}")

    chunks = chunk_evenly(pool_data, 5)
    print("Per-day distribution:")
    for tab, c in zip(WEEK_TABS, chunks):
        print(f"  {tab}: {len(c)} rows")

    print("Creating tabs:")
    for tab in WEEK_TABS:
        add_tab(tab)

    print("Writing rows:")
    for tab, c in zip(WEEK_TABS, chunks):
        write_tab(tab, headers, c)

    print("DONE.")


if __name__ == "__main__":
    main()

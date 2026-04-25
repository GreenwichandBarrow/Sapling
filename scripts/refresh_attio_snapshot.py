#!/usr/bin/env python3
"""Refresh brain/context/attio-pipeline-snapshot.json from Attio's REST API.

Snapshot is the contract between the agent (writer) and the dashboard
(reader). It contains:
  - list metadata (list_id, list_name, stages, terminal_stage)
  - all active list entries with the 9 fields the dashboard cards use
  - closed_count (lifetime) + closed_recent (last 10 closures with ts)

Run hourly via launchd during business hours so the dashboard stays
fresh as deals advance.

Usage:
    ATTIO_API_KEY=... ./refresh_attio_snapshot.py
    # or sourcing scripts/.env.launchd
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_PATH = REPO_ROOT / "brain" / "context" / "attio-pipeline-snapshot.json"
LIST_ID = "0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b"  # Active Deals – Owners
LIST_NAME = "Active Deals – Owners"
TERMINAL_STAGE = "Closed / Not Proceeding"

API_BASE = "https://api.attio.com/v2"
PAGE_LIMIT = 50  # Attio max per page
RECENT_CLOSED_KEEP = 10
RECORD_FETCH_FIELDS = (
    "name",
    "primary_location",
    "estimated_arr_usd",
    "employee_range",
    "last_interaction",
    "categories",
)

# Stage definitions — locked at write time so reader doesn't have to
# reverse-engineer them from the entries. Mirror the existing snapshot.
STAGES = [
    {"title": "Identified", "is_terminal": False},
    {"title": "Contacted", "is_terminal": False},
    {"title": "NDA", "is_terminal": False},
    {"title": "Financials Received", "is_terminal": False},
    {"title": "Submitted LOI", "is_terminal": False},
    {"title": "Signed LOI", "is_terminal": False},
    {"title": "Closed / Not Proceeding", "is_terminal": True},
]


def _headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


def _fetch_list_entries(api_key: str) -> list[dict]:
    """Paginate through every entry on the Active Deals list."""
    out: list[dict] = []
    offset = 0
    while True:
        resp = requests.post(
            f"{API_BASE}/lists/{LIST_ID}/entries/query",
            headers=_headers(api_key),
            json={"limit": PAGE_LIMIT, "offset": offset},
            timeout=30,
        )
        resp.raise_for_status()
        page = resp.json().get("data", [])
        if not page:
            break
        out.extend(page)
        if len(page) < PAGE_LIMIT:
            break
        offset += PAGE_LIMIT
    return out


def _entry_stage_and_since(entry: dict) -> tuple[str | None, str | None]:
    """Pull (stage_title, stage_since_iso) from an entry's entry_values."""
    ev = entry.get("entry_values", {}) or {}
    stage_field = ev.get("stage") or []
    if not stage_field:
        return None, None
    stage_obj = stage_field[0] if isinstance(stage_field, list) else stage_field
    title = (stage_obj.get("status") or {}).get("title")
    # `active_from` is when the entry entered current stage
    since = stage_obj.get("active_from")
    return title, since


def _entry_record_id(entry: dict) -> str | None:
    parent = entry.get("parent_record_id")
    if isinstance(parent, dict):
        return parent.get("record_id")
    return parent


def _fetch_record(api_key: str, record_id: str) -> dict:
    """Get the parent company record's values for the fields we display."""
    resp = requests.get(
        f"{API_BASE}/objects/companies/records/{record_id}",
        headers=_headers(api_key),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("data", {})


def _first_value(values: list, key: str = "value") -> str | None:
    if not values:
        return None
    first = values[0]
    if isinstance(first, dict):
        return first.get(key)
    return str(first) if first else None


def _company_fields(record: dict) -> dict:
    """Extract dashboard-relevant fields from a company record."""
    values = record.get("values") or {}

    name = _first_value(values.get("name") or [])

    location = None
    loc_arr = values.get("primary_location") or []
    if loc_arr and isinstance(loc_arr[0], dict):
        loc = loc_arr[0]
        city = loc.get("locality")
        region = loc.get("region")
        if city and region:
            location = f"{city}, {region}"
        elif city:
            location = city

    arr_bucket = None
    arr = values.get("estimated_arr_usd") or []
    if arr and isinstance(arr[0], dict):
        # Attio stores ARR as a numeric range/select; surface a coarse bucket
        v = arr[0].get("value")
        if v is not None:
            arr_bucket = _arr_to_bucket(v)
        elif arr[0].get("option"):
            arr_bucket = (arr[0].get("option") or {}).get("title")

    employee_range = None
    emp = values.get("employee_range") or []
    if emp and isinstance(emp[0], dict):
        opt = emp[0].get("option") or {}
        employee_range = opt.get("title") or _first_value(emp)

    last_interaction = None
    li = values.get("last_interaction") or []
    if li and isinstance(li[0], dict):
        last_interaction = li[0].get("interacted_at") or li[0].get("value")

    category = None
    cats = values.get("categories") or []
    if cats and isinstance(cats[0], dict):
        opt = cats[0].get("option") or {}
        category = opt.get("title") or _first_value(cats)

    return {
        "company": name or "Unknown",
        "location": location,
        "employee_range": employee_range,
        "arr_bucket": arr_bucket,
        "last_interaction": last_interaction,
        "category": category,
    }


def _arr_to_bucket(value) -> str:
    """Map a numeric ARR estimate to one of the snapshot's bucket strings."""
    try:
        n = float(value)
    except (TypeError, ValueError):
        return None
    if n < 1_000_000:
        return "<$1M"
    if n < 10_000_000:
        return "$1M-$10M"
    if n < 50_000_000:
        return "$10M-$50M"
    return "$50M+"


def _build_snapshot(api_key: str) -> dict:
    print(f"[refresh] fetching list entries (list_id={LIST_ID})", file=sys.stderr)
    entries = _fetch_list_entries(api_key)
    print(f"[refresh] got {len(entries)} entries", file=sys.stderr)

    # Group by stage; collect closed entries separately for closed_count + recent
    by_record: dict[str, dict] = {}  # record_id -> latest entry data (for dedup)
    closed_entries: list[dict] = []

    for entry in entries:
        record_id = _entry_record_id(entry)
        stage, since = _entry_stage_and_since(entry)
        if not record_id or not stage:
            continue
        item = {"record_id": record_id, "stage": stage, "stage_since": since}
        if stage == TERMINAL_STAGE:
            closed_entries.append(item)
            continue
        # Dedupe active deals by record_id, keeping newest stage_since
        existing = by_record.get(record_id)
        if existing is None or (since and since > (existing.get("stage_since") or "")):
            by_record[record_id] = item

    print(
        f"[refresh] active records: {len(by_record)} (deduped from {len(entries) - len(closed_entries)})",
        file=sys.stderr,
    )

    # Fetch parent record details for active deals only
    deals: list[dict] = []
    for record_id, item in by_record.items():
        try:
            record = _fetch_record(api_key, record_id)
        except requests.HTTPError as e:
            print(f"[refresh] WARN: record {record_id} fetch failed: {e}", file=sys.stderr)
            continue
        fields = _company_fields(record)
        deals.append({
            "record_id": record_id,
            "company": fields["company"],
            "stage": item["stage"],
            "stage_since": item["stage_since"],
            "location": fields["location"],
            "employee_range": fields["employee_range"],
            "arr_bucket": fields["arr_bucket"],
            "last_interaction": fields["last_interaction"],
            "category": fields["category"],
        })
        time.sleep(0.05)  # Stay well under Attio's 150/min limit

    # Closed: just count + keep the most recent N as stubs (no field fetch)
    closed_entries.sort(key=lambda e: e.get("stage_since") or "", reverse=True)
    closed_recent = []
    for item in closed_entries[:RECENT_CLOSED_KEEP]:
        try:
            record = _fetch_record(api_key, item["record_id"])
        except requests.HTTPError:
            continue
        fields = _company_fields(record)
        closed_recent.append({
            "record_id": item["record_id"],
            "company": fields["company"],
            "stage_since": item["stage_since"],
            "location": fields["location"],
        })
        time.sleep(0.05)

    return {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "list_id": LIST_ID,
        "list_name": LIST_NAME,
        "stages": STAGES,
        "deals": deals,
        "closed_count": len(closed_entries),
        "closed_recent": closed_recent,
    }


def main() -> int:
    api_key = os.environ.get("ATTIO_API_KEY")
    if not api_key:
        print("ERROR: ATTIO_API_KEY not set in env", file=sys.stderr)
        return 1

    try:
        snapshot = _build_snapshot(api_key)
    except requests.HTTPError as e:
        print(f"ERROR: Attio API call failed: {e}", file=sys.stderr)
        if e.response is not None:
            print(f"  body: {e.response.text[:500]}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ERROR: snapshot build failed: {e}", file=sys.stderr)
        return 3

    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(snapshot, indent=2))
    print(
        f"[refresh] wrote {SNAPSHOT_PATH} — {len(snapshot['deals'])} active deals, "
        f"{snapshot['closed_count']} closed lifetime, fetched_at={snapshot['fetched_at']}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

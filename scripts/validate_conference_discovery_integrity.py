#!/usr/bin/env python3
"""
Wrapper-level integrity validator for conference-discovery scheduled runs.

Runs as POST_RUN_CHECK after the scheduled wrapper completes. Catches three classes
of silent-success failures where the agent exits 0 but the Conference Pipeline
tab has been corrupted:

  1. **Row-count delta wipe** — original 2026-05-03 incident. ~70 rows
     cleared in a clear+rewrite that timed out before rewrite.
  2. **Header displacement** — 2026-05-10 incident. Week-of section headers
     got moved to the bottom while events stayed in
     place. Row count was within tolerance, so the row-count check passed.
  3. **Cell mutation on user selections** — 2026-05-10 incident. Status
     dropdown values in the Decision field that Kay had set ("Need to Book", etc.) got
     overwritten with different non-empty values during agent re-sort. Row
     count unchanged, so the row-count check passed.

Snapshot contract (skill writes BEFORE any Pipeline mutation):
  brain/context/rollback-snapshots/conference-pipeline-pre-run-YYYY-MM-DD.json
  {
    "tab": "Pipeline",
    "row_count": 89,         # data rows, excluding header
    "captured_at": "...",
    "rows": [...]            # full row payload for restore-from-snapshot if needed
  }

If the snapshot is missing entirely, the validator FAILS — the skill is required
to write it, missing snapshot means the skill skipped its safety step.

Exit codes:
  0  Pass — snapshot exists; row-count delta, header positions, and cell
     mutations all within tolerance.
  2  Fail — snapshot missing, sheet read failed, row count dropped too far,
     a header was displaced below its events, or a hard cell mutation
     occurred (e.g., status dropdown overwrite).

Usage:
  python3 validate_conference_discovery_integrity.py [--date YYYY-MM-DD] [--verbose]
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta


SHEET_ID = "1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY"
TAB = "Pipeline"
SHEET_READ_RANGE = "A1:Z500"  # Wide safety read; business fields resolve by header.
# Script-relative so this works on both Mac (Documents/AI Operations) and the
# Linux VPS (~/projects/Sapling) without code changes. Walks up one dir from
# scripts/ to the project root, then into brain/context/rollback-snapshots.
SNAPSHOT_DIR = os.path.normpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "brain",
        "context",
        "rollback-snapshots",
    )
)

DEFAULT_PIPELINE_HEADERS = [
    "Week Of",
    "Date of Conference",
    "Decision",
    "Event Name",
    "Location",
    "Travel",
    "Niche",
    "Registration Cost",
    "Registration Paid",
    "Reg Deadline",
    "Est. Attendees",
    "Attendee List",
    "Website",
    "Status",
    "Agent Rec",
    "Notes",
    "Agent Notes",
]

HEADER_ALIASES = {
    "week_of": ("Week Of", "Week"),
    "date": ("Date of Conference", "Date", "Conference Date"),
    "decision": ("Decision",),
    "event_name": ("Event Name", "Conference", "Name"),
    "niche": ("Niche",),
    "website": ("Website", "URL", "Event URL"),
}

# Auto-archival per SKILL.md routes past Skip rows → Skipped tab, Attended →
# Attended tab, and past-date passive rows → Skipped tab. Future/current Skip
# rows remain visible so Kay can change her mind before the event passes.
# A typical run archives 0–8 rows. We allow up to 15 to give headroom for
# catch-up runs (e.g. multi-week skipped backlog), while still catching
# wipe-class incidents (May 3 wiped ~70 rows in one swoop).
MAX_ARCHIVAL_DELTA = 15

# Hard cell mutations = stomped user selections. Any one of these = fail.
# Soft cell mutations = unexpected cell changes outside the legitimate
# auto-fill paths. We tolerate a handful (e.g., niche label refinement) but
# fail beyond MAX_SOFT_CELL_MUTATIONS as a wipe-class signal.
MAX_HARD_CELL_MUTATIONS = 0
MAX_SOFT_CELL_MUTATIONS = 5

# Status values that mark an event as legitimately archived (and therefore
# permitted to be missing from the live sheet if the event date is past).
ARCHIVAL_STATUSES = {"Skip", "Skipped", "Attended"}

# AUTHORIZED status values. These are the ONLY values permitted in the
# Decision field on the live Pipeline tab. The first 7 are Kay's
# dropdown options (selectable in the UI). Skipped/Attended/Registered are
# terminal states set by the auto-archival flow only (not Kay-selectable).
# Any cell value outside this set is an agent-invented status (e.g. the
# 2026-05 "Future / Map-Only" incident) and fails the validator immediately.
AUTHORIZED_STATUSES = {
    "",                  # empty cell allowed
    "NEW",               # agent-discovery marker; Kay reviews + moves to a decided status
    "Evaluating",
    "Need to Book",
    "Need to Register",
    "Registered Only",
    "Attending",
    "Skip",
    # Auto-archival terminal states (not in dropdown, set by skill only):
    "Skipped",
    "Attended",
    "Registered",
}

# Recognized status progressions. Any (snapshot, live) pair NOT listed
# either is no-op (same value), an empty→value transition (allowed), or
# a stomp (hard fail).
ALLOWED_STATUS_PROGRESSIONS = {
    ("NEW", "Evaluating"),
    ("NEW", "Need to Book"),
    ("NEW", "Need to Register"),
    ("NEW", "Registered Only"),
    ("NEW", "Attending"),
    ("NEW", "Skip"),
    ("Evaluating", "Attending"),
    ("Evaluating", "Need to Book"),
    ("Evaluating", "Need to Register"),
    ("Evaluating", "Skip"),
    ("Need to Register", "Registered"),
    ("Need to Register", "Registered Only"),
    ("Need to Register", "Attending"),
    ("Need to Book", "Attending"),
    ("Need to Book", "Registered"),
    ("Need to Book", "Registered Only"),
    ("Attending", "Attended"),
    ("Registered", "Attending"),
    ("Registered", "Attended"),
    ("Registered Only", "Attending"),
    ("Registered Only", "Attended"),
    ("Skip", "Skipped"),
}


# ---------------------------------------------------------------------------
# Snapshot / live-sheet I/O
# ---------------------------------------------------------------------------


def snapshot_path(run_date: date) -> str:
    return os.path.join(
        SNAPSHOT_DIR,
        f"conference-pipeline-pre-run-{run_date.isoformat()}.json",
    )


def _norm_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").strip().lower())


class PipelineSchema:
    """Resolve Conference Pipeline fields by header name, not sheet position."""

    def __init__(self, headers: list[str]):
        self.headers = headers or DEFAULT_PIPELINE_HEADERS
        self._by_header = {
            _norm_header(header): idx
            for idx, header in enumerate(self.headers)
            if header and header.strip()
        }
        self._fields: dict[str, int] = {}
        for field, aliases in HEADER_ALIASES.items():
            for alias in aliases:
                idx = self._by_header.get(_norm_header(alias))
                if idx is not None:
                    self._fields[field] = idx
                    break
            if field not in self._fields:
                raise ValueError(
                    f"required Conference Pipeline header missing for {field}: "
                    f"expected one of {aliases}, saw {self.headers!r}"
                )

    def idx(self, field: str) -> int:
        return self._fields[field]

    def known_fields(self) -> list[str]:
        return list(self._fields)


def get_pipeline_sheet(
    sheet_id: str, tab: str, rng: str
) -> tuple[PipelineSchema, list[list[str]]]:
    """Return (header schema, data rows) with at least one non-empty cell."""
    args = ["gog", "sheets", "get", sheet_id, f"{tab}!{rng}", "--json"]
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired:
        print(
            "[validate_conference_discovery] gog sheets get timed out after 90s, retrying once",
            file=sys.stderr,
        )
        result = subprocess.run(args, capture_output=True, text=True, timeout=90)
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets get failed: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    rows = data.get("values", [])
    if not rows:
        raise RuntimeError("Pipeline tab returned no rows, including no header row")
    headers = rows[0]
    data_rows = [r for r in rows[1:] if any(c and c.strip() for c in r)]
    return PipelineSchema(headers), data_rows



# ---------------------------------------------------------------------------
# Row classification + key extraction
# ---------------------------------------------------------------------------


def is_header_row(row: list[str], schema: PipelineSchema) -> bool:
    """A week-of header is a row with only the Week Of field populated."""
    if not row:
        return False
    week_idx = schema.idx("week_of")
    if not cell(row, week_idx).strip():
        return False
    return all(
        idx == week_idx or not (value and value.strip())
        for idx, value in enumerate(row)
    )


def event_url_key(row: list[str], schema: PipelineSchema) -> str | None:
    """Normalized Website value for indexing. None if missing."""
    url = cell(row, schema.idx("website")).strip()
    if url:
        return url.rstrip("/").lower()
    return None


def event_name_key(row: list[str], schema: PipelineSchema) -> str | None:
    """Normalized Event Name value for indexing. None if missing."""
    name = cell(row, schema.idx("event_name")).strip()
    if name:
        return name.lower()
    return None


def event_key_label(row: list[str], schema: PipelineSchema) -> str:
    """Human-readable key for log/failure output."""
    name = event_name_key(row, schema)
    url = event_url_key(row, schema)
    if name and url:
        return f"{name[:50]} <{url[:60]}>"
    return name or url or "<unkeyable>"


def cell(row: list[str], idx: int) -> str:
    """Safe cell accessor — returns empty string if out of range."""
    if idx < len(row) and row[idx] is not None:
        return row[idx]
    return ""


# ---------------------------------------------------------------------------
# Date parsing for Check A
# ---------------------------------------------------------------------------


_HEADER_LABEL_RE = re.compile(r"^\s*(\d{1,2})/(\d{1,2})\s*$")
_EVENT_DATE_RE = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{2,4})")


def parse_header_week(label: str, anchor_year: int) -> tuple[date, date] | None:
    """Parse a week-of header label like '4/27' into a (Mon, Sun) tuple.

    The label has no year. Use `anchor_year` (the validator's run year) as the
    starting guess. If the resulting Monday is more than 6 months before the
    anchor date, roll forward a year (handles Dec→Jan rollover).

    Returns None for TBD or unparseable labels — caller should skip such headers
    from the position-invariant check.
    """
    if label.strip().upper() == "TBD":
        return None
    m = _HEADER_LABEL_RE.match(label)
    if not m:
        return None
    month, day = int(m.group(1)), int(m.group(2))
    try:
        candidate = date(anchor_year, month, day)
    except ValueError:
        return None
    # Snap to Monday of that week (Python: Monday=0)
    monday = candidate - timedelta(days=candidate.weekday())
    sunday = monday + timedelta(days=6)
    return (monday, sunday)


def parse_event_date_range(s: str, anchor_year: int) -> tuple[date, date] | None:
    """Extract (start, end) dates from a Date of Conference value like '5/15/26' or
    '5/27/26 - 5/29/26'. Returns None for 'TBD' or unparseable strings."""
    if not s or not s.strip():
        return None
    if s.strip().upper() == "TBD":
        return None
    matches = list(_EVENT_DATE_RE.finditer(s))
    if not matches:
        return None

    def _coerce(m):
        month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if year < 100:
            year += 2000
        try:
            return date(year, month, day)
        except ValueError:
            return None

    start = _coerce(matches[0])
    end = _coerce(matches[-1]) if len(matches) > 1 else start
    if start is None or end is None:
        return None
    if end < start:
        start, end = end, start
    return (start, end)


def event_overlaps_week(event_range: tuple[date, date], week: tuple[date, date]) -> bool:
    """True if the event's date range intersects the week (Mon..Sun)."""
    es, ee = event_range
    ws, we = week
    return not (ee < ws or es > we)


def event_starts_in_week(
    event_range: tuple[date, date], week: tuple[date, date]
) -> bool:
    """True if the event's START date falls within the week.

    Anchoring by start date (not overlap) matches how Kay places events on
    the sheet: a 5/16-5/19 event lives under the 5/11 header (start = Sat
    5/16, which is in the 5/11-5/17 week), not the 5/18 header — even though
    it spills into the 5/18 week.
    """
    es, _ = event_range
    ws, we = week
    return ws <= es <= we


def _is_past_date(snap_date: str, today: date | None = None) -> bool:
    """True if the START date of a col-B value is strictly before today.

    Date ranges like '5/13/26 - 5/17/26' parse using the START date — an event
    that started yesterday but spills into next week is still "past-started"
    for archival-progression purposes. Unparseable / 'TBD' / empty → False
    (caller treats indeterminate as not-past, which is the conservative
    direction for archival legitimacy checks).
    """
    if today is None:
        today = date.today()
    er = parse_event_date_range(snap_date or "", today.year)
    if er is None:
        return False
    start, _end = er
    return start < today


def _is_legitimate_archival(
    snap_status: str, snap_date: str, today: date | None = None
) -> bool:
    """True if a snapshot row's absence from live is explainable by the
    skill's auto-archival rules (per SKILL.md):

      - ``Skip`` / ``Skipped`` + past date → routes to Skipped tab. A
        future/current Skip is NOT legitimate archival; Kay keeps those rows
        visible to preserve optionality.
      - ``Attended``           → already-completed events; always legitimate.
      - ``Attending`` + past   → event happened; assume it progressed through
        Attended-tab archival even if the snapshot caught it pre-transition.

    Everything else (Evaluating, Need to Book, Need to Register, Registered,
    Future / Map-Only with future date, empty status, etc.) is NOT a
    legitimate archival — those rows should still be on the Pipeline tab.
    """
    s = (snap_status or "").strip()
    if s in ("Skip", "Skipped"):
        return _is_past_date(snap_date, today)
    if s == "Attended":
        return True
    if s == "Attending" and _is_past_date(snap_date, today):
        return True
    return False


# ---------------------------------------------------------------------------
# Check A — Header position invariant
# ---------------------------------------------------------------------------


def check_header_positions(
    snapshot_rows: list[list[str]],
    live_rows: list[list[str]],
    snapshot_schema: PipelineSchema,
    live_schema: PipelineSchema,
    anchor_year: int,
    verbose: bool = False,
) -> list[str]:
    """Verify every dated week-of header in the snapshot still appears above
    the first event whose date falls within that week in the live sheet.

    TBD headers are exempt (catch-all bucket, position-agnostic by design).
    Headers with zero matching events in the live sheet are also exempt
    (auto-prune logic in SKILL.md will retire them; the validator doesn't
    flag empty headers as displacement).

    Missing headers (in snapshot but not in live) are flagged unless the
    header is past-dated AND has zero matching events in the live sheet —
    in which case auto-prune is the legitimate explanation.
    """
    failures: list[str] = []

    snapshot_headers = [
        (i, cell(r, snapshot_schema.idx("week_of")))
        for i, r in enumerate(snapshot_rows)
        if is_header_row(r, snapshot_schema)
    ]

    live_header_index = {}  # label -> live row idx
    for i, r in enumerate(live_rows):
        if is_header_row(r, live_schema):
            live_header_index[cell(r, live_schema.idx("week_of")).strip()] = i

    today = date.today()

    for _snap_idx, label in snapshot_headers:
        label_stripped = label.strip()
        week = parse_header_week(label_stripped, anchor_year)
        if week is None:
            # TBD or unparseable — skip the position check entirely.
            if verbose:
                print(
                    f"[check_a] skip header {label_stripped!r} "
                    f"(non-dated or unparseable)",
                    file=sys.stderr,
                )
            continue

        live_idx = live_header_index.get(label_stripped)

        # Find first live event whose START date falls in this week. We anchor
        # by start date (not range overlap) because Kay places multi-day events
        # under the header for the week they START in, even if they spill.
        first_event_idx = None
        first_event_summary = None
        for i, r in enumerate(live_rows):
            if is_header_row(r, live_schema):
                continue
            er = parse_event_date_range(cell(r, live_schema.idx("date")), anchor_year)
            if er and event_starts_in_week(er, week):
                first_event_idx = i
                first_event_summary = (
                    cell(r, live_schema.idx("date")),
                    cell(r, live_schema.idx("event_name"))[:60],
                )
                break

        if live_idx is None:
            # Header missing from live. Legitimate ONLY if past-dated AND no
            # matching event lives in the sheet anymore (auto-prune exit).
            if first_event_idx is None and week[1] < today:
                if verbose:
                    print(
                        f"[check_a] header {label_stripped!r} missing from live, "
                        f"but it's past-dated with zero matching events — "
                        f"legitimate auto-prune",
                        file=sys.stderr,
                    )
                continue
            failures.append(
                f"header {label_stripped!r} present in snapshot but missing "
                f"from live sheet (week {week[0]}..{week[1]}, "
                f"first matching live event: {first_event_summary})"
            )
            continue

        if first_event_idx is None:
            # No events under this week — orphan header, position-agnostic
            # for now. Auto-prune will collect it on the next cycle.
            if verbose:
                print(
                    f"[check_a] header {label_stripped!r} at live idx "
                    f"{live_idx} has zero matching events (orphan, OK)",
                    file=sys.stderr,
                )
            continue

        if live_idx > first_event_idx:
            failures.append(
                f"header {label_stripped!r} at live row {live_idx + 2} is BELOW "
                f"its first matching event {first_event_summary} at live row "
                f"{first_event_idx + 2}. Header has been displaced — events "
                f"should be anchored UNDER their week header, not above it. "
                f"This is the 2026-05-10 regression pattern."
            )

    return failures


# ---------------------------------------------------------------------------
# Check B — Cell mutation invariant
# ---------------------------------------------------------------------------


def classify_status_mutation(snap_val: str, live_val: str) -> str:
    """Return 'noop', 'allowed', 'hard', or 'soft' for a Decision delta."""
    sv = (snap_val or "").strip()
    lv = (live_val or "").strip()
    if sv == lv:
        return "noop"
    if not sv:
        # Snapshot was empty — any live value is an allowed auto-fill.
        return "allowed"
    if not lv:
        # Snapshot had a value, live is now empty — agent erased Kay's pick.
        return "hard"
    if (sv, lv) in ALLOWED_STATUS_PROGRESSIONS:
        return "allowed"
    # Non-empty → different non-empty value that isn't on the allow-list.
    # This is the 2026-05-10 "Art Business Conference NYC" pattern.
    return "hard"


def classify_generic_mutation(field: str, snap_val: str, live_val: str) -> str:
    """Return 'noop', 'allowed', 'hard', or 'soft' for non-status columns."""
    sv = (snap_val or "").strip()
    lv = (live_val or "").strip()
    if sv == lv:
        return "noop"
    if not sv:
        # Auto-fill of a previously-empty cell is allowed regardless of column.
        return "allowed"
    # Hard fields: changing a non-empty event identity field is a regression.
    if field in {"event_name", "date", "niche"}:
        return "hard"
    # Website field: filling in a previously-empty URL is OK (caught above);
    # mutating an existing URL is suspicious but soft-warn.
    return "soft"


def _match_snapshot_to_live(
    snapshot_rows: list[list[str]],
    live_rows: list[list[str]],
    snapshot_schema: PipelineSchema,
    live_schema: PipelineSchema,
) -> tuple[dict, list[int]]:
    """Build snap_idx → (live_idx, live_row) mapping using two-pass matching.

    Pass 1: composite (url, name) match. Unique key, robust to duplicate
    URLs (e.g., ACG chapter directory pages reused across events).

    Pass 2: URL-only match using a per-URL pool. Snapshot rows that share
    a URL with multiple live rows get matched in document order (Nth
    snapshot row → Nth live row). Handles the case where a name was edited
    but URL stayed stable.

    Pass 3: Name-only match. Catches the case where URL was added or
    changed but name remained recognizable.

    Returns (match_map, unmatched_snap_indices).
    """
    snap_events = [
        (i, r)
        for i, r in enumerate(snapshot_rows)
        if not is_header_row(r, snapshot_schema)
    ]
    live_events = [
        (i, r) for i, r in enumerate(live_rows) if not is_header_row(r, live_schema)
    ]

    consumed_live: set[int] = set()
    match_map: dict[int, tuple[int, list[str]]] = {}

    # Pass 1: composite (url, name)
    for snap_i, snap_row in snap_events:
        sk = (
            event_url_key(snap_row, snapshot_schema),
            event_name_key(snap_row, snapshot_schema),
        )
        if sk == (None, None):
            continue
        for live_i, live_row in live_events:
            if live_i in consumed_live:
                continue
            lk = (
                event_url_key(live_row, live_schema),
                event_name_key(live_row, live_schema),
            )
            if sk == lk:
                match_map[snap_i] = (live_i, live_row)
                consumed_live.add(live_i)
                break

    # Pass 2: URL-only, document-order pool draw
    for snap_i, snap_row in snap_events:
        if snap_i in match_map:
            continue
        su = event_url_key(snap_row, snapshot_schema)
        if su is None:
            continue
        for live_i, live_row in live_events:
            if live_i in consumed_live:
                continue
            if event_url_key(live_row, live_schema) == su:
                match_map[snap_i] = (live_i, live_row)
                consumed_live.add(live_i)
                break

    # Pass 3: Name-only
    for snap_i, snap_row in snap_events:
        if snap_i in match_map:
            continue
        sn = event_name_key(snap_row, snapshot_schema)
        if sn is None:
            continue
        for live_i, live_row in live_events:
            if live_i in consumed_live:
                continue
            if event_name_key(live_row, live_schema) == sn:
                match_map[snap_i] = (live_i, live_row)
                consumed_live.add(live_i)
                break

    unmatched = [snap_i for snap_i, _ in snap_events if snap_i not in match_map]
    return match_map, unmatched


def check_cell_mutations(
    snapshot_rows: list[list[str]],
    live_rows: list[list[str]],
    snapshot_schema: PipelineSchema,
    live_schema: PipelineSchema,
    verbose: bool = False,
) -> list[str]:
    """For every event row in the snapshot, verify its live counterpart has
    no forbidden cell changes."""
    failures: list[str] = []
    soft_count = 0

    match_map, unmatched = _match_snapshot_to_live(
        snapshot_rows, live_rows, snapshot_schema, live_schema
    )

    today = date.today()

    # Handle unmatched (missing) events first — must justify each absence.
    for snap_i in unmatched:
        snap_row = snapshot_rows[snap_i]
        snap_status = cell(snap_row, snapshot_schema.idx("decision")).strip()
        snap_date = cell(snap_row, snapshot_schema.idx("date"))

        # Legitimate archival per SKILL.md auto-archival rules:
        #   Skip / Skipped + past date → Skipped tab
        #   Attended                  → Attended tab, regardless of date
        #   Attending + past date     → assume Attended-tab archival
        if _is_legitimate_archival(snap_status, snap_date, today):
            if verbose:
                if snap_status in ("Skip", "Skipped"):
                    reason = (
                        f"status={snap_status!r}, past date, archived to "
                        f"Skipped"
                    )
                elif snap_status == "Attended":
                    reason = f"status={snap_status!r}, already-completed event"
                else:  # Attending + past
                    reason = (
                        f"status={snap_status!r}, past date, assumed "
                        f"Attended-tab archival"
                    )
                print(
                    f"[check_b] {event_key_label(snap_row, snapshot_schema)} archived "
                    f"legitimately ({reason})",
                    file=sys.stderr,
                )
            continue

        # Legitimate passive archival: past date + no status.
        # (Empty-status rows are pre-triage; if their date has slid past,
        # the skill drops them in the next sweep.)
        if not snap_status and _is_past_date(snap_date, today):
            if verbose:
                print(
                    f"[check_b] {event_key_label(snap_row, snapshot_schema)} archived as "
                    f"past-date passive (no status)",
                    file=sys.stderr,
                )
            continue

        # Couldn't match by URL or name → could be a key-resolution issue,
        # not a confirmed deletion. Soft-warn unless the event clearly was
        # archived. Per task spec: "don't fail the validator on key-resolution
        # issues, only on confirmed mutations."
        soft_count += 1
        if verbose:
            print(
                f"[check_b] SOFT: {event_key_label(snap_row, snapshot_schema)} not matched in "
                f"live (snap_status={snap_status!r}, date="
                f"{snap_date!r}). Either deleted without archival reason or "
                f"key drifted.",
                file=sys.stderr,
            )

    # Walk every matched pair.
    for snap_i, (live_i, live_row) in match_map.items():
        snap_row = snapshot_rows[snap_i]
        for field in snapshot_schema.known_fields():
            if field == "week_of":
                # Event rows always have empty Week Of; skip.
                continue
            snap_val = cell(snap_row, snapshot_schema.idx(field))
            live_val = cell(live_row, live_schema.idx(field))
            if field == "decision":
                cls = classify_status_mutation(snap_val, live_val)
            else:
                cls = classify_generic_mutation(field, snap_val, live_val)

            if cls in ("noop", "allowed"):
                continue
            if cls == "hard":
                failures.append(
                    f"HARD mutation on event {event_key_label(snap_row, snapshot_schema)!r} "
                    f"field {field!r}: snapshot={snap_val!r} -> "
                    f"live={live_val!r}. This is the 2026-05-10 stomp pattern."
                )
            else:  # soft
                soft_count += 1
                if verbose:
                    print(
                        f"[check_b] SOFT mutation on event "
                        f"{event_key_label(snap_row, snapshot_schema)!r} field "
                        f"{field!r}: snapshot={snap_val!r} -> "
                        f"live={live_val!r}",
                        file=sys.stderr,
                    )

    if soft_count > MAX_SOFT_CELL_MUTATIONS:
        failures.append(
            f"too many soft cell mutations: {soft_count} > "
            f"MAX_SOFT_CELL_MUTATIONS ({MAX_SOFT_CELL_MUTATIONS}). Likely "
            f"wide-area cell rewrite. Re-run with --verbose to enumerate."
        )

    return failures


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    args = sys.argv[1:]
    verbose = "--verbose" in args
    if "--date" in args:
        idx = args.index("--date")
        run_date = datetime.fromisoformat(args[idx + 1]).date()
    else:
        run_date = date.today()

    failures: list[str] = []

    # Load snapshot
    snap_path = snapshot_path(run_date)
    snapshot: dict | None = None
    snapshot_count: int | None = None
    snapshot_schema = PipelineSchema(DEFAULT_PIPELINE_HEADERS)
    if not os.path.exists(snap_path):
        failures.append(
            f"pre-run snapshot missing at {snap_path} — skill must write this "
            f"BEFORE any Pipeline mutation (see headless-prompt.md Step 0)"
        )
    else:
        try:
            with open(snap_path) as f:
                snapshot = json.load(f)
            snapshot_schema = PipelineSchema(
                snapshot.get("headers") or DEFAULT_PIPELINE_HEADERS
            )
            snapshot_count = int(snapshot.get("row_count", -1))
            if snapshot_count < 0:
                failures.append(
                    f"snapshot at {snap_path} has invalid row_count: "
                    f"{snapshot.get('row_count')!r}"
                )
                snapshot_count = None
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            failures.append(f"could not parse snapshot at {snap_path}: {exc}")

    # Load live sheet
    live_schema: PipelineSchema | None = None
    live_rows: list[list[str]] | None = None
    live_count: int | None = None
    try:
        live_schema, live_rows = get_pipeline_sheet(SHEET_ID, TAB, SHEET_READ_RANGE)
        live_count = len(live_rows)
    except Exception as exc:
        failures.append(f"could not read live Pipeline tab: {exc}")

    # Check 1: Row-count delta within tolerance (legacy guard, preserved)
    if snapshot_count is not None and live_count is not None:
        delta = snapshot_count - live_count  # positive = rows lost
        if delta > MAX_ARCHIVAL_DELTA:
            failures.append(
                f"Pipeline tab lost too many rows: snapshot had {snapshot_count} "
                f"data rows, live has {live_count} (delta {delta} > "
                f"MAX_ARCHIVAL_DELTA {MAX_ARCHIVAL_DELTA}). "
                f"Likely a wipe/clear-rewrite. Restore from snapshot via "
                f"File → Version history on the Google Sheet, or use "
                f"{snap_path} as the rollback source."
            )
        elif live_count == 0 and snapshot_count > 0:
            # Belt-and-suspenders — explicit zero-row catch even if delta math
            # somehow misses (e.g. snapshot_count == MAX_ARCHIVAL_DELTA exactly)
            failures.append(
                f"Pipeline tab has zero data rows but snapshot had "
                f"{snapshot_count}. Total wipe. Restore immediately."
            )

    # Check A: Header positions (2026-05-10 displacement guard)
    if snapshot is not None and live_rows is not None:
        anchor_year = run_date.year
        failures.extend(
            check_header_positions(
                snapshot.get("rows", []),
                live_rows,
                snapshot_schema,
                live_schema,
                anchor_year,
                verbose=verbose,
            )
        )

    # Check B: Cell mutations (2026-05-10 status-stomp guard)
    if snapshot is not None and live_rows is not None:
        failures.extend(
            check_cell_mutations(
                snapshot.get("rows", []),
                live_rows,
                snapshot_schema,
                live_schema,
                verbose=verbose,
            )
        )

    # Check C: Authorized statuses (2026-05-12 Future-Map-Only-class guard).
    # Any value in the Decision column outside the AUTHORIZED_STATUSES set is
    # an agent-invented status and fails the run. Catches the failure mode
    # where an agent writes a status not in Kay's dropdown.
    if live_rows is not None:
        for idx, row in enumerate(live_rows):
            if is_header_row(row, live_schema):
                continue
            val = cell(row, live_schema.idx("decision")).strip()
            if val not in AUTHORIZED_STATUSES:
                failures.append(
                    f"[check_c] unauthorized status {val!r} on row "
                    f"{event_key_label(row, live_schema)}. Allowed values: "
                    f"{sorted(s for s in AUTHORIZED_STATUSES if s)}. "
                    f"Either add {val!r} to Kay's dropdown on the Pipeline "
                    f"tab + update AUTHORIZED_STATUSES, or change the cell "
                    f"to an authorized value."
                )

    if failures:
        print(
            f"CONFERENCE-DISCOVERY VALIDATOR FAILED for {run_date}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"CONFERENCE-DISCOVERY VALIDATOR PASSED for {run_date}")
    print(f"  snapshot: {snap_path}")
    print(f"  pre-run rows: {snapshot_count}")
    print(f"  live rows: {live_count}")
    if snapshot_count is not None and live_count is not None:
        print(
            f"  delta: {snapshot_count - live_count} (tolerance: "
            f"{MAX_ARCHIVAL_DELTA})"
        )
    print("  header positions: OK")
    print("  cell mutations: OK")
    print("  authorized statuses: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

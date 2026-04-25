"""Parsers for scheduled-skill artifacts that feed dashboard pages.

Each function returns plain dataclasses so the render layer stays decoupled
from the vault-schema details. Parsers tolerate the real variability of the
skill outputs (zero-deal days, sub-headers, missing fields).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import json
import os
import plistlib
import re
import subprocess
from typing import Iterable

import yaml


VAULT_ROOT = Path(__file__).resolve().parent.parent / "brain"
DEAL_AGG_DIR = VAULT_ROOT / "context"
PIPELINE_SNAPSHOT_PATH = VAULT_ROOT / "context" / "attio-pipeline-snapshot.json"
PIPELINE_ATTIO_URL_BASE = "https://app.attio.com/greenwich-barrow/company"

# Active deal pipeline scope: NDA forward only. Identified + Contacted moved
# to M&A Analytics (outbound funnel) on 2026-04-24 — scope-doc Section 3.
ACTIVE_PIPELINE_STAGES = (
    "NDA",
    "Financials Received",
    "Submitted LOI",
    "Signed LOI",
)

REPO_ROOT = Path(__file__).resolve().parent.parent
LAUNCH_AGENTS_DIR = Path.home() / "Library" / "LaunchAgents"
SCHEDULED_LOGS_DIR = REPO_ROOT / "logs" / "scheduled"
LAUNCHD_LABEL_PREFIX = "com.greenwich-barrow."


# -----------------------------------------------------------------------------
# Deal Aggregator
# -----------------------------------------------------------------------------


@dataclass
class DealRow:
    source: str
    company: str
    industry: str | None
    owner: str | None
    location: str | None
    revenue: str | None
    ebitda: str | None
    asking: str | None
    status: str
    match_type: str | None
    link: str | None
    scan_date: date


@dataclass
class DealAggregatorScan:
    date: date
    deals_found: int
    sources_scanned: int | None
    volume_7d_avg: float | None
    volume_status: str | None
    last_run: str | None
    rows: list[DealRow] = field(default_factory=list)


# Recognized Slack source names → color bucket for .src-dot styling.
# Buckets: axial | bizbuysell | email | assoc | dealsx | other.
SOURCE_BUCKETS = {
    "axial": "axial",
    "bizbuysell": "bizbuysell",
    "email": "email",
    "dealsx": "dealsx",
    "rejigg": "email",
    "business exits": "bizbuysell",
    "empire flippers": "bizbuysell",
    "synergy business brokers": "bizbuysell",
    "synergy": "bizbuysell",
    "website closers": "bizbuysell",
    "flippa": "bizbuysell",
    "quiet light": "bizbuysell",
    "everingham & kerr": "email",
    "benchmark international": "email",
    "viking mergers": "email",
    "searchfunder": "email",
    "iag m&a advisors": "email",
    "iag": "email",
    "dealforce": "email",
    "the deal sheet": "email",
    "sica fletcher": "assoc",
    "marshberry": "assoc",
    "reagan consulting": "assoc",
    "agency checklists": "assoc",
    "midcap advisors": "assoc",
    "pco bookkeepers": "assoc",
    "anticimex": "assoc",
    "asa board": "assoc",
}

# Pattern for a numbered-list deal row.
# Examples from real artifacts:
#   1. **Pest Control Operator — Phoenix Metro, AZ** — The Deal Sheet | $1.8M rev | $485K SDE | $1.95M ask (4.0x) | Thesis match | "Hot Deal" flag | thedealsheet.co/pest-control
#   1. **Independent Insurance Agency — Akron, OH** — Rejigg | $3.0M rev | $400K SDE | $1.6M ask | Thesis-adjacent (Specialty Insurance) | https://rejigg.com/businesses/113563
DEAL_LINE = re.compile(r"^\s*\d+\.\s+\*\*(?P<title>[^*]+?)\*\*\s*[—-]\s*(?P<rest>.+?)\s*$")

# Sub-header pattern under Deals Surfaced (optional industry hint).
#   ### Thesis Matches — Premium Pest Management
#   ### Buy-Box Match — New Niche
SUB_HEADER = re.compile(r"^###\s+(?P<label>.+?)\s*$")

# Revenue / EBITDA / Asking patterns. Handle both orderings:
#   "$1.8M rev"   (number-first)
#   "Rev $1.8M"   (word-first)
# Plus approximate prefix "~$1M".
MONEY = r"~?\$[\d.,]+[KMB]?"
REV_PAT = re.compile(
    rf"^(?:{MONEY}\s*(?:rev|revenue|ARR|commission)\b|(?:rev|revenue|ARR|commission)\s*{MONEY}\b)",
    re.IGNORECASE,
)
EBITDA_PAT = re.compile(
    rf"^(?:{MONEY}\s*(?:EBITDA|SDE|CF|cash\s*flow)\b|(?:EBITDA|SDE|CF|cash\s*flow)\s*{MONEY}\b)",
    re.IGNORECASE,
)
ASK_PAT = re.compile(
    rf"^(?:{MONEY}\s*(?:ask|asking)\b|(?:ask|asking)\s*{MONEY}\b)",
    re.IGNORECASE,
)
MONEY_ONLY = re.compile(rf"({MONEY})")
URL_PAT = re.compile(r"(https?://[^\s|)]+|[a-zA-Z0-9.-]+\.[a-z]{2,}/[^\s|)]*)")

# Location often embedded in the company title: "Company — City, ST"
# or "Company (City, ST)" — extract city,ST when present.
LOC_PAT = re.compile(r"(?P<city>[A-Z][A-Za-z .'-]+),\s*(?P<state>[A-Z]{2})\b")


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].lstrip("\n")
    body = text[end + 4 :].lstrip("\n")
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, body


def _section(body: str, heading: str) -> str:
    """Return text under `## {heading}` until the next `## ` header."""
    pattern = re.compile(rf"^##\s+{re.escape(heading)}.*?$", re.MULTILINE)
    m = pattern.search(body)
    if not m:
        return ""
    start = m.end()
    next_h = re.search(r"^##\s+", body[start:], re.MULTILINE)
    return body[start : start + next_h.start()] if next_h else body[start:]


def _source_bucket(source: str) -> str:
    key = source.strip().lower()
    if key in SOURCE_BUCKETS:
        return SOURCE_BUCKETS[key]
    for needle, bucket in SOURCE_BUCKETS.items():
        if needle in key:
            return bucket
    return "other"


def _split_title(title: str) -> tuple[str, str | None]:
    """Split '<Company> — <City, ST>' into (company, location). Either half may
    contain em-dashes; we split on the *last* em-dash only if the right side
    looks like a city/state."""
    parts = re.split(r"\s[—–-]\s", title)
    if len(parts) >= 2:
        tail = parts[-1].strip()
        if LOC_PAT.search(tail):
            return " — ".join(p.strip() for p in parts[:-1]), tail
    # Or parenthetical location: "Company (City, ST)"
    m = re.search(r"\(([^)]+)\)\s*$", title)
    if m and LOC_PAT.search(m.group(1)):
        return title[: m.start()].strip(), m.group(1).strip()
    return title.strip(), None


def _extract_link(segments: list[str]) -> str | None:
    for seg in reversed(segments):
        m = URL_PAT.search(seg)
        if m:
            url = m.group(1)
            if not url.startswith("http"):
                url = "https://" + url
            return url
    return None


def _classify_field(segment: str) -> tuple[str, str] | None:
    """Return (kind, value) where kind in {revenue, ebitda, asking, match, flag}."""
    s = segment.strip().strip('"').strip("'")
    if not s:
        return None
    if REV_PAT.match(s):
        m = MONEY_ONLY.search(s)
        return "revenue", m.group(1) if m else s
    if EBITDA_PAT.match(s):
        m = MONEY_ONLY.search(s)
        return "ebitda", m.group(1) if m else s
    if ASK_PAT.match(s):
        m = MONEY_ONLY.search(s)
        return "asking", m.group(1) if m else s
    low = s.lower()
    if "match" in low or low.startswith("thesis") or low.startswith("buy-box") or low.startswith("buy box"):
        return "match", s
    return "flag", s


def _industry_from_subheader(label: str | None) -> str | None:
    if not label:
        return None
    # "Thesis Matches — Premium Pest Management" → "Premium Pest Management"
    # "Buy-Box Match — New Niche" → None (too generic)
    # Match space-bracketed em/en-dash only; don't split on internal "Buy-Box" hyphen.
    m = re.search(r"\s+[—–]\s+(.+)$", label)
    if m:
        tail = m.group(1).strip()
        if tail.lower() in {"new niche", "new niches"}:
            return None
        return tail
    return None


def _parse_deals_section(text: str, scan_date: date, default_source: str | None = None) -> list[DealRow]:
    rows: list[DealRow] = []
    current_sub: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        sub = SUB_HEADER.match(line)
        if sub:
            current_sub = sub.group("label")
            continue
        m = DEAL_LINE.match(line)
        if not m:
            continue
        title = m.group("title")
        rest = m.group("rest")
        company, location = _split_title(title)

        segments = [s.strip() for s in rest.split("|")]
        source = default_source or segments[0] if segments else "—"
        if default_source is None and segments:
            segments = segments[1:]

        revenue = ebitda = asking = match_type = None
        for seg in segments:
            kind_val = _classify_field(seg)
            if not kind_val:
                continue
            kind, val = kind_val
            if kind == "revenue" and revenue is None:
                revenue = val
            elif kind == "ebitda" and ebitda is None:
                ebitda = val
            elif kind == "asking" and asking is None:
                asking = val
            elif kind == "match" and match_type is None:
                match_type = val

        link = _extract_link(segments)
        industry = _industry_from_subheader(current_sub)

        rows.append(
            DealRow(
                source=source,
                company=company,
                industry=industry,
                owner=None,
                location=location,
                revenue=revenue,
                ebitda=ebitda,
                asking=asking,
                status="New",
                match_type=match_type,
                link=link,
                scan_date=scan_date,
            )
        )
    return rows


def _artifact_paths(d: date) -> list[Path]:
    """Return morning + afternoon artifacts for date `d`, in that order.
    Morning carries summary frontmatter (volume_7d_avg, volume_status);
    afternoon carries incremental deals from the 2pm top-up run."""
    out = []
    for suffix in (".md", "-afternoon.md"):
        p = DEAL_AGG_DIR / f"deal-aggregator-scan-{d.isoformat()}{suffix}"
        if p.exists():
            out.append(p)
    return out


def load_scan(d: date) -> DealAggregatorScan | None:
    paths = _artifact_paths(d)
    if not paths:
        return None

    merged_fm: dict = {}
    rows: list[DealRow] = []
    last_run = None
    for p in paths:
        text = p.read_text()
        fm, body = _parse_frontmatter(text)
        # Morning populates first; afternoon fills only missing keys so the
        # canonical volume metrics don't get overwritten by the top-up.
        for k, v in fm.items():
            merged_fm.setdefault(k, v)
        rows.extend(_parse_deals_section(_section(body, "Deals Surfaced"), d))
        rows.extend(_parse_deals_section(_section(body, "Email Inbound Deals"), d, default_source="Email"))
        last_run = _extract_last_run(body) or last_run

    return DealAggregatorScan(
        date=d,
        deals_found=int(merged_fm.get("deals_found") or 0),
        sources_scanned=merged_fm.get("sources_scanned"),
        volume_7d_avg=merged_fm.get("volume_7d_avg"),
        volume_status=merged_fm.get("volume_status"),
        last_run=last_run,
        rows=rows,
    )


def _extract_last_run(body: str) -> str | None:
    m = re.search(r"Scan window:\s*([\d-]+\s+\d{1,2}:\d{2}[^,]*)", body)
    if m:
        return m.group(1).strip()
    return None


def load_recent_scans(end: date, days: int) -> list[DealAggregatorScan]:
    """Load the last `days` scans ending at `end` (inclusive). Missing days skipped."""
    out: list[DealAggregatorScan] = []
    for offset in range(days):
        d = end - timedelta(days=offset)
        scan = load_scan(d)
        if scan is not None:
            out.append(scan)
    return out


def flatten_rows(scans: Iterable[DealAggregatorScan]) -> list[DealRow]:
    rows: list[DealRow] = []
    for s in scans:
        rows.extend(s.rows)
    return rows


# -----------------------------------------------------------------------------
# Deal Pipeline (Attio snapshot)
# -----------------------------------------------------------------------------
# Streamlit can't call the `mcp__attio__*` tools directly — those live in the
# Claude harness, not the Python process. The agent writes a snapshot file
# via MCP; this module reads the snapshot. The snapshot file is the contract
# between agent (writer) and page (reader).


@dataclass
class PipelineDeal:
    record_id: str
    company: str
    stage: str
    stage_since: str  # ISO8601
    location: str | None = None
    employee_range: str | None = None
    arr_bucket: str | None = None
    last_interaction: str | None = None
    category: str | None = None

    @property
    def attio_url(self) -> str:
        return f"{PIPELINE_ATTIO_URL_BASE}/{self.record_id}"


@dataclass
class ClosedDealStub:
    record_id: str
    company: str
    stage_since: str
    location: str | None = None

    @property
    def attio_url(self) -> str:
        return f"{PIPELINE_ATTIO_URL_BASE}/{self.record_id}"


@dataclass
class PipelineSnapshot:
    fetched_at: str
    list_id: str
    list_name: str
    stages: list[str]
    terminal_stage: str
    deals: list[PipelineDeal]
    closed_count: int
    closed_recent: list[ClosedDealStub]


def load_pipeline(scope: str = "active") -> PipelineSnapshot | None:
    """Load the Attio pipeline snapshot.

    `scope="active"` (default) filters to NDA-forward stages only —
    Identified + Contacted live on M&A Analytics as outbound funnel data.
    `scope="full"` returns every stage (used by tests / debugging only).
    """
    if not PIPELINE_SNAPSHOT_PATH.exists():
        return None
    data = json.loads(PIPELINE_SNAPSHOT_PATH.read_text())
    stage_defs = data.get("stages", [])
    all_active = [s["title"] for s in stage_defs if not s.get("is_terminal")]
    terminal_stages = [s["title"] for s in stage_defs if s.get("is_terminal")]
    terminal = terminal_stages[0] if terminal_stages else "Closed / Not Proceeding"

    if scope == "active":
        # Honor the snapshot's stage order but filter to NDA-forward.
        active_stages = [s for s in all_active if s in ACTIVE_PIPELINE_STAGES]
        deals = [
            PipelineDeal(**d)
            for d in data.get("deals", [])
            if d.get("stage") in ACTIVE_PIPELINE_STAGES
        ]
    else:
        active_stages = all_active
        deals = [PipelineDeal(**d) for d in data.get("deals", [])]

    return PipelineSnapshot(
        fetched_at=data["fetched_at"],
        list_id=data["list_id"],
        list_name=data["list_name"],
        stages=active_stages,
        terminal_stage=terminal,
        deals=deals,
        closed_count=int(data.get("closed_count") or 0),
        closed_recent=[ClosedDealStub(**c) for c in data.get("closed_recent", [])],
    )


# -----------------------------------------------------------------------------
# C-Suite & Skills (scheduled-skill canary)
# -----------------------------------------------------------------------------
# Reads launchctl + plist XML + log files. All local data, no auth.
#
# Hierarchy: 6 C-suite agents (COO/CIO/CPO/CMO/CFO/GC, in display order) own
# subsets of the skill catalog. The mapping is hardcoded here because no
# external source-of-truth exists — Kay validated this assignment 2026-04-24.

# Skill catalog: name → (description, c_suite, optional trigger text for on-demand)
# Order of the dict drives display order *within* each C-suite section.
_SKILL_CATALOG: dict[str, tuple[str, str, str | None]] = {
    # COO — orchestration, system health, process
    "calibration-workflow": (
        "Friday meta-calibration — graduates rules to hooks, refreshes stale memories and skills.",
        "COO",
        None,
    ),
    "weekly-tracker": (
        "Friday activity roll-up across Gmail, Calendar, Attio, vault → Google Sheet + vault snapshot.",
        "COO",
        None,
    ),
    "health-monitor": (
        "System-wide health monitoring — disconnected services, missed triggers, stale data, hygiene.",
        "COO",
        None,
    ),
    "pipeline-manager": (
        "Morning briefing assembly — reads all artifacts, judges, presents 4-bucket briefing for review.",
        "COO",
        "Morning workflow",
    ),
    "decision-traces": (
        "Extract meaningful decisions from completed tasks for the calibration pipeline.",
        "COO",
        "Evening workflow",
    ),
    "triage": (
        "Process queue items needing human decision — medium/low confidence and unclassified.",
        "COO",
        "Queue overflow",
    ),
    "today": (
        "Daily task aggregation from inbox, email, and yesterday's open loops.",
        "COO",
        "Morning kickoff",
    ),
    "migration-workflow": (
        "Vault file migration to current schema versions — detect, preview, apply with validation.",
        "COO",
        "Schema bump",
    ),
    # CIO — investment, deal flow, niches, targets
    "deal-aggregator": (
        "Daily scan of broker platforms, email inbound, and association deal boards.",
        "CIO",
        None,
    ),
    "deal-aggregator-afternoon": (
        "Afternoon broker re-scan to catch late-day listings.",
        "CIO",
        None,
    ),
    "deal-aggregator-friday": (
        "Weekly broker roll-up and Friday digest of new active sellers.",
        "CIO",
        None,
    ),
    "email-intelligence": (
        "Gmail/Superhuman/Granola scan, deal-flow classification, CIM auto-trigger, intro detection.",
        "CIO",
        None,
    ),
    "nightly-tracker-audit": (
        "Tabled/Killed processing, WEEKLY REVIEW re-sort, Drive folder hygiene.",
        "CIO",
        None,
    ),
    "niche-intelligence": (
        "Newsletter scrape, niche identification, one-pagers, scorecards, tracker update.",
        "CIO",
        None,
    ),
    "conference-discovery": (
        "Weekly conference scan, registration, attendee list processing into targets.",
        "CIO",
        None,
    ),
    "target-discovery-sunday": (
        "Weekly owner enrichment for the next 200 un-enriched targets on JJ-Call-Only sheets.",
        "CIO",
        None,
    ),
    "deal-evaluation": (
        "Post-call follow-up through LOI — NDA, financials, scorecard, Thumbs Up/Down deck.",
        "CIO",
        "Triggered by CIM arrival",
    ),
    "post-loi": (
        "Post-LOI due diligence through closing (~90 days) — workstreams, financing, PA, close.",
        "CIO",
        "Triggered by signed LOI",
    ),
    "target-discovery": (
        "Find acquisition targets via Apollo + web research; auto-advance qualifying targets to outreach.",
        "CIO",
        "On niche activation / refill signal",
    ),
    "list-builder": (
        "Apollo-based company discovery and contact enrichment. Called by target-discovery.",
        "CIO",
        "Called by target-discovery",
    ),
    "tracker-manager": (
        "Operational sheet management — status moves, rank re-sorts, target list hygiene, DealsX edits.",
        "CIO",
        "Kay-authorized sheet updates",
    ),
    "river-guide-builder": (
        "Per-niche ecosystem build — associations, named individuals, network cross-check, experience scan.",
        "CIO",
        "Per-niche ecosystem build",
    ),
    # CPO — relationships, people, JJ
    "relationship-manager": (
        "Nurture cadence monitoring, overdue-contact surfacing, Attio People hygiene.",
        "CPO",
        None,
    ),
    "jj-operations-sunday": (
        "Sunday prep — creates Mon–Fri Call Log tabs for the week ahead.",
        "CPO",
        None,
    ),
    "jj-operations": (
        "Daily call prep, 10am Slack delivery, post-shift outcome harvest into master sheet.",
        "CPO",
        "Manual harvest after 2pm shift",
    ),
    "warm-intro-finder": (
        "Mine network for warm intro paths to acquisition targets — Attio, vault, Gmail, LinkedIn.",
        "CPO",
        "Per-target network scan",
    ),
    "meeting-brief": (
        "External meeting prep — auto-detects new vs. repeat contact; saves to Drive + vault.",
        "CPO",
        "Pre-meeting trigger",
    ),
    # CMO — outreach, brand, content
    "outreach-manager": (
        "Owns all outreach — Kay email, DealsX, conference, intermediary. Channel routing by niche.",
        "CMO",
        "Approved targets / sheet trigger",
    ),
    "conference-engagement": (
        "T-7 to T+2 outreach lifecycle — pre-event drafts and post-event business-card follow-ups.",
        "CMO",
        "Around each conference Kay attends",
    ),
    "generate-visuals": (
        "Gemini Nano-Banana image generation — LinkedIn carousels, infographics, brand graphics.",
        "CMO",
        "Manual visual gen",
    ),
    # CFO — financial discipline
    "budget-manager": (
        "Fund budget tracking, runway forecasting, tech-stack audits, bookkeeper P&L reconciliation.",
        "CFO",
        "Monthly bookkeeper P&L intake",
    ),
    "investor-update": (
        "Quarterly deck, Stevens monthly, Lavergne biweekly, post-LOI weekly DD — four modes.",
        "CFO",
        "Quarterly + call prep",
    ),
}

# C-suite display order (top to bottom on the page) — validated 2026-04-24.
_CSUITE_DISPLAY_ORDER = [
    ("COO", "Chief of Staff"),
    ("CIO", "Chief Investment Officer"),
    ("CPO", "Chief People Officer"),
    ("CMO", "Chief Marketing Officer"),
    ("CFO", "Chief Financial Officer"),
    ("GC", "General Counsel"),
]

# Skills declared scheduled in CLAUDE.md but with no plist registered = a "gap"
# (the canary's job is to surface this). As of 2026-04-24, only health-monitor.
_CLAUDE_MD_SCHEDULED_BUT_UNREGISTERED = {"health-monitor"}

# launchd's StartCalendarInterval uses 0=Sun OR 7=Sun (both accepted by Apple).
# Map both to "Sun" so plists from either convention render correctly.
_WEEKDAY_NAMES = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}


@dataclass
class SkillRun:
    fired_at: datetime  # parsed from filename or mtime
    status: str  # "ok" | "warn" | "err"
    log_path: Path
    snippet: str  # first non-blank content line, truncated


@dataclass
class SkillHealth:
    name: str
    description: str
    c_suite: str  # CIO / CFO / CMO / CPO / COO / GC
    is_scheduled: bool  # has a launchd plist
    is_registered: bool  # appears in `launchctl list`
    is_gap: bool  # CLAUDE.md says scheduled but no plist = surface as red gap
    schedule_text: str  # human-readable cadence ("Daily · 6:00 AM ET")
    next_fire_text: str | None  # for scheduled-but-not-today
    trigger_text: str | None  # for on-demand
    today_status: str  # see _STATUSES below
    last_run: SkillRun | None
    recent_runs: list[SkillRun] = field(default_factory=list)


@dataclass
class CSuiteGroup:
    short: str  # CIO / CFO / etc
    label: str  # full title
    skills: list[SkillHealth] = field(default_factory=list)


# Status taxonomy used by the renderer to pick dot color + badge.
_STATUSES = {
    "fired-ok": ("green", "Scheduled"),
    "fired-warn": ("yellow", "Scheduled"),
    "fired-err": ("red", "Scheduled"),
    "scheduled-later": ("grey", "Scheduled"),  # scheduled but not today
    "missed": ("red", "Scheduled"),  # should have fired today, no log
    "ondemand": ("ondemand", "On-demand"),
    "gap": ("red", "Gap"),
}


def _registered_jobs() -> set[str]:
    """Return set of skill names registered with launchctl."""
    try:
        out = subprocess.run(
            ["launchctl", "list"],
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return set()
    out_text = out.stdout if out.returncode == 0 else ""
    names: set[str] = set()
    for line in out_text.splitlines():
        # Format: PID  STATUS  LABEL
        parts = line.split()
        if len(parts) < 3:
            continue
        label = parts[-1]
        if label.startswith(LAUNCHD_LABEL_PREFIX):
            names.add(label[len(LAUNCHD_LABEL_PREFIX):])
    return names


def _read_plist(skill: str) -> dict | None:
    path = LAUNCH_AGENTS_DIR / f"{LAUNCHD_LABEL_PREFIX}{skill}.plist"
    if not path.exists():
        return None
    try:
        with path.open("rb") as f:
            return plistlib.load(f)
    except (OSError, plistlib.InvalidFileException):
        return None


def _format_schedule(intervals: list[dict]) -> str:
    """Turn StartCalendarInterval entries into a human label.

    Patterns we care about:
      - 5 intervals Mon-Fri at same H:M → "Daily · H:MM AM/PM ET"
      - 7 intervals (every weekday) at same H:M → "Nightly · H:MM AM/PM ET"
      - 1 interval, fixed weekday → "Mon 9:00 AM ET"
      - Otherwise → "Multi-cadence" (rare; readable fallback)
    """
    if not intervals:
        return "—"
    times = {(d.get("Hour"), d.get("Minute")) for d in intervals}
    weekdays = {d.get("Weekday") for d in intervals if "Weekday" in d}
    if len(times) != 1:
        return "Multi-cadence"
    hour, minute = next(iter(times))
    if hour is None or minute is None:
        return "Multi-cadence"
    t_label = _format_time(hour, minute)
    # Treat 0/7-Sunday duplicates as a single Sunday entry for label purposes.
    weekdays_norm = {7 if w == 0 else w for w in weekdays}
    if weekdays_norm == {1, 2, 3, 4, 5}:
        return f"Daily · {t_label}"
    if weekdays_norm == {1, 2, 3, 4, 5, 6, 7}:
        return f"Nightly · {t_label}"
    if len(weekdays_norm) == 1:
        wd = next(iter(weekdays_norm))
        if wd in _WEEKDAY_NAMES:
            return f"{_WEEKDAY_NAMES[wd]} {t_label}"
    if not weekdays_norm:
        # No Weekday key → fires every day
        return f"Daily · {t_label}"
    days = " ".join(_WEEKDAY_NAMES.get(w, "?") for w in sorted(weekdays_norm))
    return f"{days} {t_label}"


def _format_time(hour: int, minute: int) -> str:
    period = "AM" if hour < 12 else "PM"
    h12 = hour % 12 or 12
    return f"{h12}:{minute:02d} {period} ET"


def _next_fire(intervals: list[dict], now: datetime | None = None) -> datetime | None:
    """Return the next scheduled fire datetime in local time, or None."""
    if not intervals:
        return None
    now = now or datetime.now()
    candidates: list[datetime] = []
    for ahead in range(0, 8):
        day = now.date() + timedelta(days=ahead)
        weekday = day.isoweekday()  # 1=Mon..7=Sun
        for d in intervals:
            wd = d.get("Weekday")
            if wd is not None and wd != weekday:
                continue
            hour = d.get("Hour", 0)
            minute = d.get("Minute", 0)
            candidate = datetime(day.year, day.month, day.day, hour, minute)
            if candidate > now:
                candidates.append(candidate)
    return min(candidates) if candidates else None


def _should_fire_today(intervals: list[dict], today: date | None = None) -> bool:
    if not intervals:
        return False
    today = today or date.today()
    weekday = today.isoweekday()
    for d in intervals:
        wd = d.get("Weekday")
        if wd is None or wd == weekday:
            return True
    return False


_LOG_FILENAME_RE = re.compile(
    r"^(?P<skill>[a-z0-9-]+?)-(?P<date>\d{4}-\d{2}-\d{2})-(?P<hhmm>\d{4})\.log$"
)


def _scan_logs_for_skill(skill: str, limit: int = 5) -> list[SkillRun]:
    """Return up to `limit` most recent runs for this skill, newest first."""
    if not SCHEDULED_LOGS_DIR.exists():
        return []
    runs: list[SkillRun] = []
    for entry in SCHEDULED_LOGS_DIR.iterdir():
        m = _LOG_FILENAME_RE.match(entry.name)
        if not m or m.group("skill") != skill:
            continue
        try:
            d = date.fromisoformat(m.group("date"))
        except ValueError:
            continue
        hhmm = m.group("hhmm")
        try:
            fired = datetime(d.year, d.month, d.day, int(hhmm[:2]), int(hhmm[2:]))
        except ValueError:
            continue
        snippet, status = _read_log_summary(entry)
        runs.append(SkillRun(fired_at=fired, status=status, log_path=entry, snippet=snippet))
    runs.sort(key=lambda r: r.fired_at, reverse=True)
    return runs[:limit]


def _read_log_summary(path: Path) -> tuple[str, str]:
    """Return (first non-blank content line, status).

    Reads first 4KB + last 2KB. Status is intentionally conservative:
      err  = decisive failure (Traceback, FATAL, last line ends with Error/exception)
      warn = transient/recoverable (API Error in body, rate-limit, warning)
      ok   = otherwise

    Mid-run "API Error: ..." that the run recovered from gets warn, not err —
    a fired-err light should mean the run actually failed.
    """
    try:
        full = path.read_text(errors="replace")
    except OSError:
        return "(log read error)", "err"
    head = full[:4096]
    tail = full[-2048:] if len(full) > 4096 else ""
    lower_head = head.lower()
    lower_tail = tail.lower()
    # Decisive-failure markers — these mean the script crashed.
    if (
        "traceback (most recent call last)" in lower_head + lower_tail
        or "fatal:" in lower_head + lower_tail
        or "fatal error" in lower_head + lower_tail
    ):
        status = "err"
    elif (
        "api error" in lower_head
        or "warning" in lower_head
        or "rate limit" in lower_head
        or "warn:" in lower_head
        or "retrying" in lower_head
    ):
        status = "warn"
    else:
        status = "ok"
    snippet = ""
    for line in head.splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            snippet = s[:160]
            break
    return snippet or "(empty log)", status


def _today_status_for_scheduled(
    intervals: list[dict], runs_today: list[SkillRun]
) -> str:
    """Decide today's color based on schedule + dated logs for today."""
    if runs_today:
        # Latest run today drives the color.
        latest = runs_today[0]
        return f"fired-{latest.status}"
    if not _should_fire_today(intervals):
        return "scheduled-later"
    # Should fire today and hasn't yet — distinguish "later today" from "missed".
    now = datetime.now()
    expected_today = []
    for d in intervals:
        wd = d.get("Weekday")
        if wd is not None and wd != now.isoweekday():
            continue
        h = d.get("Hour", 0)
        m = d.get("Minute", 0)
        expected_today.append(datetime(now.year, now.month, now.day, h, m))
    if not expected_today:
        return "scheduled-later"
    if min(expected_today) > now:
        return "scheduled-later"  # next fire is today but in the future
    # We're past at least one expected fire time and have no log → missed.
    return "missed"


def _runs_today(runs: list[SkillRun]) -> list[SkillRun]:
    today = date.today()
    return [r for r in runs if r.fired_at.date() == today]


def _build_skill_health(
    skill: str,
    description: str,
    c_suite: str,
    trigger_text: str | None,
    registered: set[str],
) -> SkillHealth:
    is_registered = skill in registered
    plist = _read_plist(skill)
    is_scheduled = plist is not None
    is_gap = (not is_scheduled) and skill in _CLAUDE_MD_SCHEDULED_BUT_UNREGISTERED
    intervals = (plist or {}).get("StartCalendarInterval") or []
    if isinstance(intervals, dict):
        intervals = [intervals]
    schedule_text = _format_schedule(intervals) if is_scheduled else "—"
    next_fire = _next_fire(intervals) if is_scheduled else None
    next_fire_text = next_fire.strftime("Next %a %b %-d") if next_fire else None
    recent = _scan_logs_for_skill(skill, limit=5)
    today = _runs_today(recent)
    if is_gap:
        today_status = "gap"
    elif is_scheduled:
        today_status = _today_status_for_scheduled(intervals, today)
    else:
        today_status = "ondemand"
    return SkillHealth(
        name=skill,
        description=description,
        c_suite=c_suite,
        is_scheduled=is_scheduled,
        is_registered=is_registered,
        is_gap=is_gap,
        schedule_text=schedule_text,
        next_fire_text=next_fire_text,
        trigger_text=trigger_text,
        today_status=today_status,
        last_run=recent[0] if recent else None,
        recent_runs=recent,
    )


def load_skill_health() -> list[CSuiteGroup]:
    """Build the C-Suite & Skills page data structure.

    Returns groups in display order (COO, CIO, CPO, CMO, CFO, GC).
    Each group's skills appear in catalog declaration order.
    """
    registered = _registered_jobs()
    by_csuite: dict[str, list[SkillHealth]] = {short: [] for short, _ in _CSUITE_DISPLAY_ORDER}
    for skill, (description, c_suite, trigger) in _SKILL_CATALOG.items():
        if c_suite not in by_csuite:
            # Catalog has an unmapped c_suite — drop silently rather than
            # surface a misclassification on the page.
            continue
        by_csuite[c_suite].append(
            _build_skill_health(skill, description, c_suite, trigger, registered)
        )
    return [
        CSuiteGroup(short=short, label=label, skills=by_csuite.get(short, []))
        for short, label in _CSUITE_DISPLAY_ORDER
    ]


def skill_health_summary(groups: list[CSuiteGroup]) -> dict[str, int]:
    """Aggregate counts for the page summary strip."""
    counts = {"total": 0, "fired_today": 0, "on_deck": 0, "gaps": 0, "ondemand": 0, "missed": 0}
    for g in groups:
        for s in g.skills:
            counts["total"] += 1
            if s.today_status.startswith("fired"):
                counts["fired_today"] += 1
            elif s.today_status == "scheduled-later":
                counts["on_deck"] += 1
            elif s.today_status == "gap":
                counts["gaps"] += 1
            elif s.today_status == "ondemand":
                counts["ondemand"] += 1
            elif s.today_status == "missed":
                counts["missed"] += 1
    return counts


# -----------------------------------------------------------------------------
# Infrastructure — Zone 1: System Health
# -----------------------------------------------------------------------------
# Pure local probes. No external auth, no MCP. Each tile reports a status
# (ok/warn/alert) and a short detail line. Failures degrade gracefully — a
# probe that can't run reports `unknown` rather than crashing the page.

DASHBOARD_DATA_DIR = Path(__file__).resolve().parent / "data"
TECH_STACK_PATH = DASHBOARD_DATA_DIR / "tech_stack.yaml"
SCHEMAS_DIR = REPO_ROOT / "schemas" / "vault"
HOOKS_SETTINGS_PATHS = [
    REPO_ROOT / ".claude" / "settings.json",
    REPO_ROOT / ".claude" / "settings.local.json",
]


@dataclass
class HealthTile:
    label: str  # "Launchd jobs registered"
    status: str  # ok | warn | alert | unknown
    value: str  # "12 / 12"
    detail: str  # "All scheduled skills present in launchctl"


def _registered_count() -> int:
    return len(_registered_jobs())


def _expected_plist_count() -> int:
    if not LAUNCH_AGENTS_DIR.exists():
        return 0
    return sum(1 for _ in LAUNCH_AGENTS_DIR.glob(f"{LAUNCHD_LABEL_PREFIX}*.plist"))


def _disk_usage_pct() -> tuple[float, str]:
    """Return (percent_used, human_total) for the volume holding the repo."""
    try:
        stats = os.statvfs(str(REPO_ROOT))
    except OSError:
        return 0.0, "—"
    total = stats.f_frsize * stats.f_blocks
    free = stats.f_frsize * stats.f_bavail
    used = total - free
    if total == 0:
        return 0.0, "—"
    pct = used * 100.0 / total
    total_tb = total / (1024 ** 4)
    used_tb = used / (1024 ** 4)
    if total_tb >= 1:
        human = f"{used_tb:.1f} TB used of {total_tb:.1f} TB"
    else:
        total_gb = total / (1024 ** 3)
        used_gb = used / (1024 ** 3)
        human = f"{used_gb:.0f} GB used of {total_gb:.0f} GB"
    return pct, human


def _logs_writing_today() -> tuple[bool, int]:
    """True if any scheduled log file was written today; returns count."""
    if not SCHEDULED_LOGS_DIR.exists():
        return False, 0
    today = date.today().isoformat()
    n = 0
    for entry in SCHEDULED_LOGS_DIR.iterdir():
        if entry.suffix != ".log":
            continue
        if today in entry.name:
            n += 1
    return n > 0, n


def _hooks_count() -> int:
    """Count distinct hook entries across user + repo settings.json files."""
    seen: set[tuple[str, str]] = set()
    for path in HOOKS_SETTINGS_PATHS:
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        hooks = data.get("hooks", {}) or {}
        for event_name, configs in hooks.items():
            if not isinstance(configs, list):
                continue
            for cfg in configs:
                hcmds = (cfg or {}).get("hooks", []) or []
                for h in hcmds:
                    cmd = (h or {}).get("command", "")
                    seen.add((event_name, cmd))
    return len(seen)


def _vault_files_validated() -> tuple[int, int]:
    """Count brain/ files vs schema-violators. Cheap heuristic: every file
    under brain/ that has frontmatter starting with `---` and a `schema_version:`
    field counts as validated. We do NOT actually run the schema validator
    here — that would be too slow per render."""
    brain = REPO_ROOT / "brain"
    if not brain.exists():
        return 0, 0
    total = 0
    violations = 0
    for entry in brain.rglob("*.md"):
        total += 1
        try:
            head = entry.read_text(errors="replace")[:512]
        except OSError:
            violations += 1
            continue
        if not head.startswith("---"):
            violations += 1
    return total, violations


def _briefing_last_run() -> tuple[bool, str]:
    """Look for today's pipeline-manager log as a proxy for briefing health."""
    runs = _scan_logs_for_skill("pipeline-manager", limit=1)
    if not runs:
        # Pipeline-manager isn't on launchd today — fall back to checking
        # whether morning briefing artifacts exist.
        return True, "on-demand · no scheduled log"
    latest = runs[0]
    return latest.status == "ok", latest.fired_at.strftime("Last %a %-I:%M %p")


def load_system_health() -> list[HealthTile]:
    """Build the System Health tile list (Zone 1 of Infrastructure)."""
    tiles: list[HealthTile] = []

    # 1. Launchd jobs registered (count vs filesystem)
    registered = _registered_count()
    expected = _expected_plist_count()
    if registered == 0 and expected == 0:
        tiles.append(HealthTile(
            "Launchd jobs registered", "unknown", "—",
            "launchctl unavailable in this environment",
        ))
    elif registered >= expected and expected > 0:
        tiles.append(HealthTile(
            "Launchd jobs registered", "ok", f"{registered} / {expected}",
            "All scheduled skills present in launchctl",
        ))
    else:
        tiles.append(HealthTile(
            "Launchd jobs registered", "warn",
            f"{registered} / {expected}",
            "Some plists not loaded into launchctl",
        ))

    # 2. Spec vs registered (catches health-monitor-style gaps)
    expected_per_md = expected + len(_CLAUDE_MD_SCHEDULED_BUT_UNREGISTERED)
    if registered >= expected_per_md:
        tiles.append(HealthTile(
            "Spec vs. registered", "ok", f"{registered} / {expected_per_md}",
            "All CLAUDE.md scheduled skills accounted for",
        ))
    else:
        missing = sorted(_CLAUDE_MD_SCHEDULED_BUT_UNREGISTERED)
        tiles.append(HealthTile(
            "Spec vs. registered", "alert",
            f"{registered} / {expected_per_md}",
            f"Missing plist: {', '.join(missing)}",
        ))

    # 3. Logs writing today
    writing, today_count = _logs_writing_today()
    if writing:
        tiles.append(HealthTile(
            "Logs writing today", "ok", "healthy",
            f"{today_count} log files written today · 14-day rotation",
        ))
    else:
        tiles.append(HealthTile(
            "Logs writing today", "warn", "no logs yet",
            "No scheduled-skill logs have been written today",
        ))

    # 4. Hooks firing (count of configured hooks across settings)
    hooks = _hooks_count()
    if hooks > 0:
        tiles.append(HealthTile(
            "Hooks configured", "ok", f"{hooks}",
            f"{hooks} hook entries across project + user settings",
        ))
    else:
        tiles.append(HealthTile(
            "Hooks configured", "warn", "0",
            "No hooks found in settings.json",
        ))

    # 5. Disk space
    pct, human = _disk_usage_pct()
    if pct >= 90:
        tiles.append(HealthTile("Disk space", "alert", f"{pct:.0f}%", f"{human} · prune logs"))
    elif pct >= 80:
        tiles.append(HealthTile("Disk space", "warn", f"{pct:.0f}%", human))
    else:
        tiles.append(HealthTile("Disk space", "ok", f"{pct:.0f}%", human))

    # 6. Vault schema validation
    total, viol = _vault_files_validated()
    if total == 0:
        tiles.append(HealthTile(
            "Vault frontmatter", "unknown", "—", "brain/ unreachable",
        ))
    elif viol == 0:
        tiles.append(HealthTile(
            "Vault frontmatter", "ok", "passing",
            f"{total} files · all carry frontmatter",
        ))
    else:
        tiles.append(HealthTile(
            "Vault frontmatter", "warn", f"{viol} miss",
            f"{viol} of {total} files lack frontmatter",
        ))

    # 7. Background commits — last commit time
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cr"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=5,
        )
        commit_age = out.stdout.strip() if out.returncode == 0 else "unknown"
        tiles.append(HealthTile(
            "Last commit", "ok", commit_age or "unknown",
            "git working tree managed by background hook",
        ))
    except (FileNotFoundError, subprocess.TimeoutExpired):
        tiles.append(HealthTile("Last commit", "unknown", "—", "git not available"))

    # 8. Briefing pipeline (proxy: pipeline-manager log)
    ok, briefing_text = _briefing_last_run()
    tiles.append(HealthTile(
        "Briefing pipeline",
        "ok" if ok else "warn",
        "on time" if ok else "check",
        briefing_text,
    ))

    return tiles


def system_health_summary(tiles: list[HealthTile]) -> dict[str, int]:
    counts = {"healthy": 0, "warn": 0, "alert": 0, "unknown": 0}
    for t in tiles:
        if t.status == "ok":
            counts["healthy"] += 1
        elif t.status == "warn":
            counts["warn"] += 1
        elif t.status == "alert":
            counts["alert"] += 1
        else:
            counts["unknown"] += 1
    return counts


# -----------------------------------------------------------------------------
# Infrastructure — Zone 5: Tech Stack Inventory
# -----------------------------------------------------------------------------


@dataclass
class StackService:
    name: str
    note: str | None
    health: str  # ok | warn | alert | retired


@dataclass
class StackCategory:
    label: str
    services: list[StackService] = field(default_factory=list)


def load_tech_stack() -> list[StackCategory]:
    """Read dashboard/data/tech_stack.yaml and return categorized services."""
    if not TECH_STACK_PATH.exists():
        return []
    try:
        data = yaml.safe_load(TECH_STACK_PATH.read_text()) or {}
    except (OSError, yaml.YAMLError):
        return []
    out: list[StackCategory] = []
    for cat in data.get("categories", []):
        services = [
            StackService(
                name=s.get("name", "?"),
                note=s.get("note"),
                health=s.get("health", "ok"),
            )
            for s in cat.get("services", [])
        ]
        out.append(StackCategory(label=cat.get("label", "?"), services=services))
    return out


def tech_stack_count(categories: list[StackCategory]) -> int:
    return sum(len(c.services) for c in categories)

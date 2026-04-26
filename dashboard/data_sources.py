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
VAULT_CONTEXT_DIR = VAULT_ROOT / "context"
VAULT_ENTITIES_DIR = VAULT_ROOT / "entities"
PIPELINE_SNAPSHOT_PATH = VAULT_ROOT / "context" / "attio-pipeline-snapshot.json"
JJ_SNAPSHOT_PATH = VAULT_ROOT / "context" / "jj-activity-snapshot.json"
WEEKLY_TRACKERS_DIR = VAULT_ROOT / "trackers" / "weekly"

_SESSION_DECISIONS_RE = re.compile(r"^session-decisions-(\d{4}-\d{2}-\d{2})\.md$")
_SENT_LINE_RE = re.compile(r"^- \*\*SENT", re.MULTILINE)
_DRAFTED_LINE_RE = re.compile(r"^- \*\*DRAFTED", re.MULTILINE)
_LINKEDIN_LINE_RE = re.compile(r"^- \*\*(SENT|DRAFTED).*linkedin", re.IGNORECASE | re.MULTILINE)
_LINKEDIN_SENT_RE = re.compile(r"^- \*\*SENT.*linkedin", re.IGNORECASE | re.MULTILINE)
_LINKEDIN_DRAFTED_RE = re.compile(r"^- \*\*DRAFTED.*linkedin", re.IGNORECASE | re.MULTILINE)

_WEEKLY_TRACKER_FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-weekly-tracker\.md$")
# First number on the row after the metric label cell. Tolerant to "~49",
# "0/0/0", "$612", commas, "/" separators. Used for NDAs / JJ dials etc.
_FIRST_NUM_RE = re.compile(r"\b(\d+(?:[.,]\d+)?)\b")
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
    closed_count: int  # lifetime total (pre + post NDA)
    closed_recent: list[ClosedDealStub]
    closed_count_post_nda: int = 0  # deals with engagement signal
    closed_count_pre_nda: int = 0  # outreach attrition (no engagement)


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
        closed_count_post_nda=int(data.get("closed_count_post_nda") or 0),
        closed_count_pre_nda=int(data.get("closed_count_pre_nda") or 0),
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
# (the canary's job is to surface this). Empty as of 2026-04-25 — health-monitor
# was registered Friday morning after the Apr 24 dashboard build surfaced the gap.
_CLAUDE_MD_SCHEDULED_BUT_UNREGISTERED: set[str] = set()

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
EXTERNAL_SERVICES_PATH = DASHBOARD_DATA_DIR / "external_services.yaml"
CREDITS_PATH = DASHBOARD_DATA_DIR / "credits.yaml"
CALIBRATION_PATH = DASHBOARD_DATA_DIR / "calibration.yaml"
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


# -----------------------------------------------------------------------------
# M&A Analytics — multi-zone activity rollup
# -----------------------------------------------------------------------------
# Replaces the Weekly Activity Tracker Google Sheet. Five zones:
#   1. Deal Flow Headline — 5 KPI tiles (owner conversations, NDAs, financials,
#      LOIs, closures), 7-day window from Attio snapshot + brain/calls.
#   2. Outbound Funnel — DEFERRED placeholder (DealsX integration May 7).
#   2.5. Response Categorization — DEFERRED placeholder (DealsX AI tags).
#   3. Channel Performance — 6 channels (4 live + 2 DealsX-deferred).
#   4. Trends · 12 weeks — 4 sparkline panels (best-effort; pending where no
#      historical weekly snapshot exists).
#   5. Activity Detail · This Week — chips + counts per category.
#
# Data sources:
#   - Attio snapshot (load_pipeline scope="full") for all stage-related counts.
#   - brain/calls/* file dates + classification_type for owner conversations,
#     intermediary meetings, conferences. File format `YYYY-MM-DD-slug.md`.
#   - Email-scan-results in brain/context/ for CIM detection (regex over body).
#   - Hardcoded active-niche list (Industry Research Tracker is a Google Sheet
#     not yet wired into Streamlit; ship-and-iterate per the load-bearing test).

VAULT_CALLS_DIR = VAULT_ROOT / "calls"

# Active niches as of 2026-04-25 (validated against feedback memories +
# session decisions). Update when a niche flips status in the tracker.
_ACTIVE_NICHES = [
    "Insurance Brokerage",
    "Fine Art Storage",
    "Equipment Servicing",
    "Managed IT Services",
]

# Investor / advisor names — exclude these from "intermediary meetings" count
# since they're recurring internal-cadence calls, not deal-facing intermediaries.
_INVESTOR_SLUG_HINTS = (
    "guillermo",
    "jeff-stevens",
    "jeff-kay",
    "stevens-monthly",
    "stevens-biweekly",
    "saltoun",
    "ashford",
)
_CONFERENCE_SLUG_HINTS = (
    "xpx",
    "acg",
    "conference",
    "panel",
    "frieze",
    "pratt",
    "wsn",
)
_CIM_PATTERN = re.compile(r"\bCIM(?:s|s received)?\b", re.IGNORECASE)
_CALL_FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")


@dataclass
class KPITile:
    label: str
    color: str  # blue | purple | yellow | green | red
    icon: str
    value: int
    sub: str  # "↑ 3 vs. 0 last week" — caller pre-formats deltas


@dataclass
class ChannelRow:
    name: str
    description: str
    dot_class: str  # kay | jj | dealsx | intermediary | conference (CSS hook)
    sent: str  # display string (handles "—", "1,180", "47")
    reply: str
    positive: str
    to_nda: str
    reply_rate: str  # "12.8%" or "—"
    bar_pct: int  # 0–100, scaled width
    bar_color: str | None  # accent | green | purple | orange | None
    deferred: bool  # True → render yellow "live May 7" pill, suppress numbers


@dataclass
class TrendPanel:
    label: str
    value: str  # current bucket value, e.g. "2" or "4.3%"
    delta: str  # e.g. "↑ vs. 0 last week" or "→ same"
    delta_class: str  # up | down | flat
    bars: list[int]  # 12 heights 0–100
    bar_color: str  # accent | green | yellow | purple
    pending: bool  # True → render dim with "Pending data history" overlay


@dataclass
class ActivityRow:
    category: str
    chips: list[str]
    count: int
    empty_text: str | None  # render this when chips is empty


@dataclass
class CallSummary:
    """Lightweight parse of one brain/calls/ file."""
    date: date
    slug: str
    classification: str  # partner | client | internal | unknown
    title: str | None  # first H1 in body, falls back to slug


@dataclass
class MAAnalytics:
    week_start: date
    week_end: date
    deal_flow_tiles: list[KPITile]  # Zone 1 (5 tiles)
    channels: list[ChannelRow]  # Zone 3 (7 rows: Kay email, Kay LinkedIn, Intermediary, JJ, DealsX×2, Conference)
    trends: list[TrendPanel]  # Zone 4 (4 panels)
    trend_x_labels: tuple[str, str, str]  # (start, mid, end) shared across trends
    activity_rows: list[ActivityRow]  # Zone 5
    niche_breakdown: NicheBreakdown | None = None  # Zone 6 (Phase A.4)
    outreach_metrics: OutreachMetrics | None = None  # Phase A.1 backing data
    new_contacts: NewContactsMetric | None = None  # Phase A.3 backing data
    response_count: int = 0  # for Zone 2/2.5 placeholder context
    snapshot_fresh: bool = False  # True if Attio snapshot loaded


# -----------------------------------------------------------------------------
# Helpers — call-file parsing
# -----------------------------------------------------------------------------


def _scan_calls() -> list[CallSummary]:
    """Read every brain/calls/*.md file once and return lightweight summaries.

    Date comes from the filename (cheaper than parsing frontmatter and reliable
    since the schema validator enforces the format). classification_type is
    extracted via a single grep to avoid YAML-parsing every file."""
    if not VAULT_CALLS_DIR.exists():
        return []
    summaries: list[CallSummary] = []
    for entry in VAULT_CALLS_DIR.iterdir():
        m = _CALL_FILENAME_RE.match(entry.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        slug = m.group(2)
        classification = "unknown"
        title = None
        try:
            head = entry.read_text(errors="replace")[:1500]
        except OSError:
            head = ""
        for line in head.splitlines():
            stripped = line.strip()
            if stripped.startswith("classification_type:"):
                classification = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            elif stripped.startswith("# ") and title is None:
                title = stripped[2:].strip()
            if classification != "unknown" and title is not None:
                break
        summaries.append(CallSummary(date=d, slug=slug, classification=classification, title=title))
    return summaries


def _slug_matches(slug: str, hints: tuple[str, ...]) -> bool:
    low = slug.lower()
    return any(h in low for h in hints)


def _calls_in_window(calls: list[CallSummary], start: date, end: date) -> list[CallSummary]:
    return [c for c in calls if start <= c.date <= end]


# -----------------------------------------------------------------------------
# Zone 1 — Deal Flow Headline
# -----------------------------------------------------------------------------


def _delta_phrase(this_week: int, last_week: int) -> tuple[str, str]:
    """Return (sub_text, delta_class) honoring the mockup's phrasing."""
    if this_week == last_week:
        return f"→ same as last week ({last_week})", "flat"
    if this_week > last_week:
        return f"↑ {this_week - last_week} vs. {last_week} last week", "up"
    return f"↓ {last_week - this_week} vs. {last_week} last week", "down"


def _stage_advances_in_window(snapshot: PipelineSnapshot, stage: str, start: date, end: date) -> int:
    """Count snapshot deals whose stage_since lands in [start, end] for `stage`."""
    n = 0
    for d in snapshot.deals:
        if d.stage != stage:
            continue
        try:
            ts = datetime.fromisoformat(d.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if start <= ts.date() <= end:
            n += 1
    return n


def _closures_in_window(snapshot: PipelineSnapshot, start: date, end: date) -> int:
    n = 0
    for c in snapshot.closed_recent:
        try:
            ts = datetime.fromisoformat(c.stage_since.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if start <= ts.date() <= end:
            n += 1
    return n


def _build_deal_flow_tiles(
    snapshot: PipelineSnapshot | None,
    calls: list[CallSummary],
    week_start: date,
    week_end: date,
    prior_start: date,
    prior_end: date,
) -> list[KPITile]:
    # Owner conversations: partner-classified calls, exclude investor cadences.
    def _owner_count(start: date, end: date) -> int:
        in_window = _calls_in_window(calls, start, end)
        return sum(
            1
            for c in in_window
            if c.classification == "partner"
            and not _slug_matches(c.slug, _INVESTOR_SLUG_HINTS)
        )

    owner_now = _owner_count(week_start, week_end)
    owner_prior = _owner_count(prior_start, prior_end)
    owner_sub, _ = _delta_phrase(owner_now, owner_prior)

    if snapshot is None:
        nda = fin = loi = closed = 0
        snap_sub = "Attio snapshot unavailable"
    else:
        nda = _stage_advances_in_window(snapshot, "NDA", week_start, week_end)
        fin = _stage_advances_in_window(snapshot, "Financials Received", week_start, week_end)
        loi = _stage_advances_in_window(snapshot, "Submitted LOI", week_start, week_end) + \
              _stage_advances_in_window(snapshot, "Signed LOI", week_start, week_end)
        closed = _closures_in_window(snapshot, week_start, week_end)
        snap_sub = "from Attio snapshot"

    nda_prior = _stage_advances_in_window(snapshot, "NDA", prior_start, prior_end) if snapshot else 0
    fin_prior = (_stage_advances_in_window(snapshot, "Financials Received", prior_start, prior_end)
                 if snapshot else 0)
    loi_prior = ((_stage_advances_in_window(snapshot, "Submitted LOI", prior_start, prior_end) +
                  _stage_advances_in_window(snapshot, "Signed LOI", prior_start, prior_end))
                 if snapshot else 0)
    closed_prior = _closures_in_window(snapshot, prior_start, prior_end) if snapshot else 0

    nda_sub, _ = _delta_phrase(nda, nda_prior)
    fin_sub, _ = _delta_phrase(fin, fin_prior)
    loi_sub, _ = _delta_phrase(loi, loi_prior)
    closed_sub, _ = _delta_phrase(closed, closed_prior)

    # Suffix the snapshot context onto the closed-tile sub since the others
    # use delta phrasing only — keeps the tile strip uniform.
    if snapshot is None:
        closed_sub = snap_sub

    return [
        KPITile("Owner conversations", "blue", "💬", owner_now, owner_sub),
        KPITile("NDAs signed", "purple", "📝", nda, nda_sub),
        KPITile("Financials received", "yellow", "📊", fin, fin_sub),
        KPITile("LOIs submitted", "green", "📤", loi, loi_sub),
        KPITile("Closed / Not proceeding", "red", "⊘", closed, closed_sub),
    ]


# -----------------------------------------------------------------------------
# Zone 3 — Channel Performance
# -----------------------------------------------------------------------------


def _build_channels(
    calls: list[CallSummary],
    week_start: date,
    week_end: date,
    jj: JJActivity | None = None,
    outreach: OutreachMetrics | None = None,
) -> list[ChannelRow]:
    in_window = _calls_in_window(calls, week_start, week_end)
    intermediary = sum(
        1 for c in in_window
        if c.classification == "partner"
        and not _slug_matches(c.slug, _INVESTOR_SLUG_HINTS)
        and not _slug_matches(c.slug, _CONFERENCE_SLUG_HINTS)
    )
    conferences = sum(1 for c in in_window if _slug_matches(c.slug, _CONFERENCE_SLUG_HINTS))

    # CEO emails row — drafts/sends from session-decisions verb tags (Phase A.1).
    # Reply / positive / response-rate pending DealsX (live May 7).
    if outreach is not None:
        ceo_email_sent = str(outreach.sends_this_week)
        ceo_email_desc = (
            f"Owner-facing warm outreach · highest-touch · "
            f"{outreach.drafts_this_week} drafted this week ({outreach.drafts_last_week} prior)"
        )
        ceo_li_sent = str(outreach.linkedin_dms_sent_this_week)
        ceo_li_desc = (
            f"CEO-direct LinkedIn DMs · {outreach.linkedin_dms_drafts_this_week} drafted this week "
            f"({outreach.linkedin_dms_drafts_last_week} prior) · {outreach.linkedin_dms_sent_last_week} sent last week"
        )
    else:
        ceo_email_sent = "—"
        ceo_email_desc = "Owner-facing warm outreach · highest-touch · session-decisions parser pending"
        ceo_li_sent = "—"
        ceo_li_desc = "CEO-direct LinkedIn DMs · session-decisions parser pending"

    # Operations calls row: dials this week from snapshot. Falls back to "—"
    # when snapshot is missing so the row stays in the table without claiming a count.
    if jj is not None:
        ops_sent = str(jj.dials_this_week)
        ops_reply = "—"  # outcomes need Call Status reading; not yet wired
        ops_positive = "—"
        ops_to_nda = "0"  # operations doesn't move stages directly
        ops_desc = (
            f"Cold dial campaign · 10am–2pm ET Mon–Fri · "
            f"{jj.dials_lifetime} lifetime across {len(jj.per_niche_lifetime)} niches"
        )
    else:
        ops_sent = ops_reply = ops_positive = ops_to_nda = "—"
        ops_desc = "Cold dial campaign · operations snapshot unavailable"

    return [
        ChannelRow(
            name="CEO emails",
            description=ceo_email_desc,
            dot_class="kay",
            sent=ceo_email_sent, reply="—", positive="—", to_nda="—",
            reply_rate="—", bar_pct=0, bar_color="accent", deferred=False,
        ),
        ChannelRow(
            name="CEO LinkedIn DMs",
            description=ceo_li_desc,
            dot_class="kay",
            sent=ceo_li_sent, reply="—", positive="—", to_nda="—",
            reply_rate="—", bar_pct=0, bar_color="accent", deferred=False,
        ),
        ChannelRow(
            name="Intermediary intro",
            description="Warm intros via advisors, brokers, peers · partner-classified calls in window",
            dot_class="intermediary",
            sent=str(intermediary), reply=str(intermediary), positive=str(intermediary),
            to_nda="0", reply_rate="—", bar_pct=0, bar_color="green", deferred=False,
        ),
        ChannelRow(
            name="Operations calls",
            description=ops_desc,
            dot_class="jj",
            sent=ops_sent, reply=ops_reply, positive=ops_positive, to_nda=ops_to_nda,
            reply_rate="—", bar_pct=0, bar_color="green", deferred=False,
        ),
        ChannelRow(
            name="DealsX · email",
            description="High-volume outbound email · live May 7 (DealsX integration)",
            dot_class="dealsx",
            sent="—", reply="—", positive="—", to_nda="—",
            reply_rate="—", bar_pct=0, bar_color="purple", deferred=True,
        ),
        ChannelRow(
            name="DealsX · LinkedIn DM",
            description="High-volume LinkedIn DMs · live May 7 (DealsX integration)",
            dot_class="dealsx",
            sent="—", reply="—", positive="—", to_nda="—",
            reply_rate="—", bar_pct=0, bar_color="purple", deferred=True,
        ),
        ChannelRow(
            name="Conference",
            description="In-person event follow-ups · counted via call vault tags",
            dot_class="conference",
            sent=str(conferences), reply=str(conferences), positive=str(conferences),
            to_nda="0", reply_rate="—", bar_pct=0, bar_color="orange", deferred=False,
        ),
    ]


# -----------------------------------------------------------------------------
# Zone 4 — Trends (12 weekly buckets)
# -----------------------------------------------------------------------------


def _weekly_buckets(end: date, weeks: int = 12) -> list[tuple[date, date]]:
    """Return [oldest .. newest] list of (week_start, week_end) ranges."""
    out: list[tuple[date, date]] = []
    for offset in range(weeks - 1, -1, -1):
        week_end = end - timedelta(days=offset * 7)
        week_start = week_end - timedelta(days=6)
        out.append((week_start, week_end))
    return out


def _scale_bars(values: list[int]) -> list[int]:
    """Scale absolute counts to 0–100 for CSS height. Empty input → all zeros."""
    if not values:
        return [0] * 12
    peak = max(values)
    if peak == 0:
        return [4 for _ in values]  # min bar height to remain visible
    return [max(4, round(v * 100 / peak)) for v in values]


def _build_trends(
    snapshot: PipelineSnapshot | None,
    calls: list[CallSummary],
    today: date,
    jj: JJActivity | None = None,
    weekly_history: dict[date, WeeklyTrackerSnapshot] | None = None,
) -> list[TrendPanel]:
    buckets = _weekly_buckets(today, weeks=12)
    x_labels = (
        buckets[0][0].strftime("%b %-d"),
        buckets[6][0].strftime("%b %-d"),
        buckets[-1][1].strftime("%b %-d"),
    )

    # Owner conversations weekly — derived from brain/calls/ filename dates.
    owner_buckets: list[int] = []
    for ws, we in buckets:
        n = sum(
            1 for c in calls
            if ws <= c.date <= we
            and c.classification == "partner"
            and not _slug_matches(c.slug, _INVESTOR_SLUG_HINTS)
        )
        owner_buckets.append(n)
    owner_now = owner_buckets[-1]
    owner_prev = owner_buckets[-2] if len(owner_buckets) >= 2 else 0
    owner_sub, owner_class = _delta_phrase(owner_now, owner_prev)

    # NDAs signed weekly — prefer weekly-tracker history (captures historical
    # NDAs that no longer show in the live snapshot) with snapshot fallback
    # for the current week. Snapshot only sees deals in current state, so a
    # historical NDA that was later moved to Financials/LOI would be invisible.
    nda_buckets: list[int] = []
    for ws, we in buckets:
        # Prefer weekly-tracker history when any tracker week_end falls
        # inside this bucket (handles Fri vs Sat alignment); snapshot
        # fallback for buckets with no tracker file.
        v = 0
        tracker_match = None
        if weekly_history:
            for tracker_date, snap in weekly_history.items():
                if ws <= tracker_date <= we:
                    tracker_match = snap
                    break
        if tracker_match is not None:
            v = tracker_match.ndas
        elif snapshot is not None:
            v = _stage_advances_in_window(snapshot, "NDA", ws, we)
        nda_buckets.append(v)
    nda_now = nda_buckets[-1]
    nda_prev = nda_buckets[-2] if len(nda_buckets) >= 2 else 0
    nda_sub, nda_class = _delta_phrase(nda_now, nda_prev)
    nda_pending = sum(nda_buckets) == 0  # truly nothing across 12 weeks

    panels = [
        TrendPanel(
            label="NDAs signed · weekly",
            value=str(nda_now),
            delta=nda_sub,
            delta_class=nda_class,
            bars=_scale_bars(nda_buckets),
            bar_color="green",
            pending=nda_pending,
        ),
        TrendPanel(
            label="Reply rate · weekly avg",
            value="—",
            delta="Pending data history",
            delta_class="flat",
            bars=[0] * 12,
            bar_color="purple",
            pending=True,
        ),
        TrendPanel(
            label="Owner conversations · weekly",
            value=str(owner_now),
            delta=owner_sub,
            delta_class=owner_class,
            bars=_scale_bars(owner_buckets),
            bar_color="accent",
            pending=False,
        ),
    ]

    if jj is not None and jj.weekly_buckets:
        # Align JJ snapshot weekly buckets to the same 12-week window we built.
        # Snapshot already provides 12 buckets ending today.
        jj_counts = [b.dials for b in jj.weekly_buckets[-12:]]
        jj_now = jj_counts[-1] if jj_counts else 0
        jj_prev = jj_counts[-2] if len(jj_counts) >= 2 else 0
        jj_sub, jj_class = _delta_phrase(jj_now, jj_prev)
        jj_pending = sum(jj_counts) == 0
        if jj_pending:
            jj_value = "0"
            jj_sub = "No dials in last 12 weeks"
        else:
            jj_value = str(jj_now)
        panels.append(TrendPanel(
            label="Operations dials · weekly",
            value=jj_value,
            delta=jj_sub,
            delta_class=jj_class,
            bars=_scale_bars(jj_counts),
            bar_color="yellow",
            pending=jj_pending,
        ))
    else:
        panels.append(TrendPanel(
            label="Operations dials · weekly",
            value="—",
            delta="Operations snapshot unavailable",
            delta_class="flat",
            bars=[0] * 12,
            bar_color="yellow",
            pending=True,
        ))

    return panels, x_labels


# -----------------------------------------------------------------------------
# Zone 5 — Activity Detail
# -----------------------------------------------------------------------------


_CIM_AFFIRMATIVE = re.compile(
    r"\bCIM(?:s)?\b\s+(received|signed|attached)", re.IGNORECASE
)
# Reject phrases like "No CIM received", "None — no CIMs detected",
# "not triggered", "no CIM auto-trigger". Audited 2026-04-25 against
# every email-scan-results file in vault — every CIM mention to date
# has been a NEGATIVE confirmation, so the negation guard must come
# before the affirmative regex hits.
_CIM_NEGATION = re.compile(
    r"\b(no|none|not|never|zero)\b[^.\n]{0,40}\bCIM",
    re.IGNORECASE,
)


def _count_cims_in_window(start: date, end: date) -> int:
    """Scan email-scan-results in the window for affirmative CIM events.

    Counts a CIM when a line contains "CIM(s) received|signed|attached" AND
    the line does not contain a negation token within ~40 chars before the
    CIM mention. Without the negation guard, "No CIM received" triggers a
    false positive (audited 2026-04-25)."""
    n = 0
    if not DEAL_AGG_DIR.exists():
        return 0
    for d_offset in range((end - start).days + 1):
        d = start + timedelta(days=d_offset)
        path = DEAL_AGG_DIR / f"email-scan-results-{d.isoformat()}.md"
        if not path.exists():
            continue
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if not _CIM_AFFIRMATIVE.search(stripped):
                continue
            if _CIM_NEGATION.search(stripped):
                continue  # negative phrasing like "No CIM received"
            n += 1
    return n


# -----------------------------------------------------------------------------
# Phase A.1 — Outreach metrics (drafts/sends from session-decisions verb tags)
# -----------------------------------------------------------------------------


@dataclass
class OutreachMetrics:
    """Weekly outreach activity from session-decisions verb tags.

    Counts `- **SENT` and `- **DRAFTED` bullets across daily session-decisions
    files. LinkedIn breakdown is best-effort grep — separates DealsX/Superhuman
    once channel tagging surfaces. Reply rate / positive responses pending
    DealsX integration (live May 7).
    """
    week_start: date
    week_end: date
    sends_this_week: int
    sends_last_week: int
    drafts_this_week: int
    drafts_last_week: int
    linkedin_dms_this_week: int  # SENT + DRAFTED summed (legacy field)
    linkedin_dms_last_week: int
    linkedin_dms_sent_this_week: int = 0
    linkedin_dms_sent_last_week: int = 0
    linkedin_dms_drafts_this_week: int = 0
    linkedin_dms_drafts_last_week: int = 0


def _count_verb_tags_in_window(start: date, end: date) -> tuple[int, int, int, int, int]:
    """Sum SENT, DRAFTED, and LinkedIn-tagged bullets across the window.

    Returns (sends, drafts, linkedin_total, linkedin_sent, linkedin_drafted).
    `linkedin_total` is kept for legacy callers (= sent + drafted). Tolerates
    missing files — weekend days routinely have no session-decisions.
    """
    sends = drafts = linkedin = li_sent = li_drafted = 0
    if not VAULT_CONTEXT_DIR.exists():
        return 0, 0, 0, 0, 0
    cur = start
    while cur <= end:
        path = VAULT_CONTEXT_DIR / f"session-decisions-{cur.isoformat()}.md"
        if path.exists():
            try:
                text = path.read_text(errors="replace")
            except OSError:
                cur += timedelta(days=1)
                continue
            sends += len(_SENT_LINE_RE.findall(text))
            drafts += len(_DRAFTED_LINE_RE.findall(text))
            linkedin += len(_LINKEDIN_LINE_RE.findall(text))
            li_sent += len(_LINKEDIN_SENT_RE.findall(text))
            li_drafted += len(_LINKEDIN_DRAFTED_RE.findall(text))
        cur += timedelta(days=1)
    return sends, drafts, linkedin, li_sent, li_drafted


def load_outreach_metrics(today: date | None = None) -> OutreachMetrics:
    """Aggregate Kay's outreach activity for the current + prior week."""
    today = today or date.today()
    week_end = today
    week_start = today - timedelta(days=6)
    prior_end = week_start - timedelta(days=1)
    prior_start = prior_end - timedelta(days=6)
    sends_now, drafts_now, li_now, li_sent_now, li_drafted_now = _count_verb_tags_in_window(week_start, week_end)
    sends_prior, drafts_prior, li_prior, li_sent_prior, li_drafted_prior = _count_verb_tags_in_window(prior_start, prior_end)
    return OutreachMetrics(
        week_start=week_start,
        week_end=week_end,
        sends_this_week=sends_now,
        sends_last_week=sends_prior,
        drafts_this_week=drafts_now,
        drafts_last_week=drafts_prior,
        linkedin_dms_this_week=li_now,
        linkedin_dms_last_week=li_prior,
        linkedin_dms_sent_this_week=li_sent_now,
        linkedin_dms_sent_last_week=li_sent_prior,
        linkedin_dms_drafts_this_week=li_drafted_now,
        linkedin_dms_drafts_last_week=li_drafted_prior,
    )


# -----------------------------------------------------------------------------
# Phase A.3 — New contacts added (Attio snapshot count, WoW pending history)
# -----------------------------------------------------------------------------


@dataclass
class NewContactsMetric:
    """Top-of-funnel snapshot count. WoW delta pending historical snapshots
    (Attio refresh script writes a single rolling file today)."""
    snapshot_count: int
    fetched_at: str
    historical_pending: bool = True


def load_new_contacts(snapshot: PipelineSnapshot | None = None) -> NewContactsMetric:
    if snapshot is None:
        snapshot = load_pipeline(scope="full")
    if snapshot is None:
        return NewContactsMetric(snapshot_count=0, fetched_at="—")
    total = len(snapshot.deals) + snapshot.closed_count
    return NewContactsMetric(snapshot_count=total, fetched_at=snapshot.fetched_at)


# -----------------------------------------------------------------------------
# Phase A.4 — Per-niche outreach breakdown (JJ dials per niche; email pending)
# -----------------------------------------------------------------------------


@dataclass
class NicheBreakdownRow:
    niche: str
    jj_dials_lifetime: int
    jj_active: bool  # True if any lifetime dials → JJ-Call-Only channel
    email_pending: bool = True  # per-niche email classifier not yet wired


@dataclass
class NicheBreakdown:
    rows: list[NicheBreakdownRow]
    week_start: date
    week_end: date


# Order matches the dashboard's NICHE_SHEETS map in scripts/refresh_jj_snapshot.py.
# Active niches as of 2026-04-26.
_NICHE_BREAKDOWN_ORDER = (
    "Premium Pest Management",
    "IPLC",
    "Art Insurance",
    "Domestic TCI",
    "Art Storage",
    "Art Advisory",
)


def load_niche_breakdown(
    today: date | None = None,
    jj: JJActivity | None = None,
) -> NicheBreakdown:
    """Per-niche outreach activity. JJ dials wired via jj-activity-snapshot.json;
    per-niche weekly + per-niche email sends pending Phase B classifier."""
    today = today or date.today()
    week_end = today
    week_start = today - timedelta(days=6)
    if jj is None:
        jj = load_jj_activity()
    rows: list[NicheBreakdownRow] = []
    for niche in _NICHE_BREAKDOWN_ORDER:
        lifetime = 0
        if jj is not None:
            lifetime = int(jj.per_niche_lifetime.get(niche, 0))
        rows.append(NicheBreakdownRow(
            niche=niche,
            jj_dials_lifetime=lifetime,
            jj_active=lifetime > 0,
        ))
    return NicheBreakdown(rows=rows, week_start=week_start, week_end=week_end)


def _build_activity_rows(
    calls: list[CallSummary],
    week_start: date,
    week_end: date,
    new_contacts: NewContactsMetric | None = None,
) -> list[ActivityRow]:
    in_window = _calls_in_window(calls, week_start, week_end)

    conf_calls = [c for c in in_window if _slug_matches(c.slug, _CONFERENCE_SLUG_HINTS)]
    intermediary_calls = [
        c for c in in_window
        if c.classification == "partner"
        and not _slug_matches(c.slug, _INVESTOR_SLUG_HINTS)
        and not _slug_matches(c.slug, _CONFERENCE_SLUG_HINTS)
    ]

    def _slug_display(call: CallSummary) -> str:
        # "2026-04-23-xpx-panel" → "XPX panel · Apr 23"
        words = call.slug.replace("-", " ")
        return f"{words.title()} · {call.date.strftime('%b %-d')}"

    cim_count = _count_cims_in_window(week_start, week_end)

    if new_contacts is not None and new_contacts.snapshot_count:
        new_contacts_text = (
            f"{new_contacts.snapshot_count} companies in Attio snapshot · "
            f"WoW delta pending historical snapshots"
        )
        new_contacts_count = new_contacts.snapshot_count
    else:
        new_contacts_text = "Attio snapshot unavailable"
        new_contacts_count = 0

    return [
        ActivityRow(
            category="Active Niches",
            chips=list(_ACTIVE_NICHES),
            count=len(_ACTIVE_NICHES),
            empty_text=None,
        ),
        ActivityRow(
            category="New contacts (Attio)",
            chips=[],
            count=new_contacts_count,
            empty_text=new_contacts_text,
        ),
        ActivityRow(
            category="Conferences attended",
            chips=[_slug_display(c) for c in conf_calls],
            count=len(conf_calls),
            empty_text="No conferences this week",
        ),
        ActivityRow(
            category="Intermediary meetings",
            chips=[_slug_display(c) for c in intermediary_calls],
            count=len(intermediary_calls),
            empty_text="No intermediary meetings this week",
        ),
        ActivityRow(
            category="CIMs received",
            chips=[],
            count=cim_count,
            empty_text=(f"{cim_count} CIMs flagged in email-scan-results"
                        if cim_count else "No CIMs received this week"),
        ),
        ActivityRow(
            category="Business cards added",
            chips=[],
            count=0,
            empty_text="conference-engagement output not yet wired",
        ),
    ]


# -----------------------------------------------------------------------------
# Public loader
# -----------------------------------------------------------------------------


def load_ma_analytics(today: date | None = None) -> MAAnalytics:
    """Build the M&A Analytics page data structure.

    `today` defaults to date.today() — exposed for deterministic testing.
    Window = 7 days back to today (inclusive). Prior-week window = the 7
    days before that, used for delta phrasing on Zone 1 KPIs.
    """
    today = today or date.today()
    week_start = today - timedelta(days=6)
    week_end = today
    prior_end = week_start - timedelta(days=1)
    prior_start = prior_end - timedelta(days=6)

    snapshot = load_pipeline(scope="full")
    calls = _scan_calls()
    jj = load_jj_activity()
    weekly_history = load_weekly_tracker_history()
    outreach = load_outreach_metrics(today=today)
    new_contacts = load_new_contacts(snapshot=snapshot)
    niche_breakdown = load_niche_breakdown(today=today, jj=jj)

    deal_flow_tiles = _build_deal_flow_tiles(
        snapshot, calls, week_start, week_end, prior_start, prior_end
    )
    channels = _build_channels(calls, week_start, week_end, jj=jj, outreach=outreach)
    trends, x_labels = _build_trends(snapshot, calls, today, jj=jj, weekly_history=weekly_history)
    activity_rows = _build_activity_rows(
        calls, week_start, week_end, new_contacts=new_contacts
    )

    return MAAnalytics(
        week_start=week_start,
        week_end=week_end,
        deal_flow_tiles=deal_flow_tiles,
        channels=channels,
        trends=trends,
        trend_x_labels=x_labels,
        activity_rows=activity_rows,
        niche_breakdown=niche_breakdown,
        outreach_metrics=outreach,
        new_contacts=new_contacts,
        snapshot_fresh=snapshot is not None,
    )


# -----------------------------------------------------------------------------
# Infrastructure Zones 2/3/4 — External services / credits / calibration
# -----------------------------------------------------------------------------
# YAML-driven catalogs (mirror tech_stack.yaml). Loaders return plain
# dataclasses so the renderer stays decoupled from the YAML schema.
# Live readers (auth probes, billing API, calibration-workflow output)
# wire later by replacing the YAML reader with a live source.


@dataclass
class ExternalService:
    name: str
    kind: str  # "service" or "local"
    description: str
    health: str  # ok | warn | alert
    status_text: str
    action: str  # regen | refresh | view | muted
    action_text: str


@dataclass
class CreditTile:
    label: str
    value: str
    unit: str
    runway_text: str
    runway_color: str  # green | yellow | red | none
    trend: str
    trend_arrow: str  # up | down | flat


@dataclass
class CalibrationEntry:
    icon: str
    icon_color: str  # green | purple | accent | dim
    headline: str
    detail: str  # HTML allowed
    when: str


@dataclass
class CalibrationLog:
    last_run: str
    entries: list[CalibrationEntry] = field(default_factory=list)


def load_external_services() -> list[ExternalService]:
    if not EXTERNAL_SERVICES_PATH.exists():
        return []
    try:
        data = yaml.safe_load(EXTERNAL_SERVICES_PATH.read_text()) or {}
    except (OSError, yaml.YAMLError):
        return []
    return [
        ExternalService(
            name=s.get("name", "?"),
            kind=s.get("kind", "service"),
            description=s.get("description", ""),
            health=s.get("health", "ok"),
            status_text=s.get("status_text", ""),
            action=s.get("action", "muted"),
            action_text=s.get("action_text", "Logs ↗"),
        )
        for s in data.get("services", [])
    ]


def external_services_summary(services: list[ExternalService]) -> dict[str, int]:
    counts = {"total": len(services), "healthy": 0, "warn": 0, "alert": 0}
    for s in services:
        if s.health == "ok":
            counts["healthy"] += 1
        elif s.health == "warn":
            counts["warn"] += 1
        elif s.health == "alert":
            counts["alert"] += 1
    return counts


def load_credit_tiles() -> list[CreditTile]:
    if not CREDITS_PATH.exists():
        return []
    try:
        data = yaml.safe_load(CREDITS_PATH.read_text()) or {}
    except (OSError, yaml.YAMLError):
        return []
    return [
        CreditTile(
            label=t.get("label", "?"),
            value=str(t.get("value", "—")),
            unit=t.get("unit", ""),
            runway_text=t.get("runway_text", ""),
            runway_color=t.get("runway_color", "none"),
            trend=t.get("trend", ""),
            trend_arrow=t.get("trend_arrow", "flat"),
        )
        for t in data.get("tiles", [])
    ]


# JJ activity snapshot — written by scripts/refresh_jj_snapshot.py
@dataclass
class JJWeeklyBucket:
    week_start: date
    week_end: date
    dials: int


@dataclass
class JJActivity:
    fetched_at: str  # ISO8601
    dials_today: int
    dials_this_week: int
    dials_lifetime: int
    weekly_buckets: list[JJWeeklyBucket] = field(default_factory=list)
    per_niche_lifetime: dict[str, int] = field(default_factory=dict)
    by_day: dict[date, int] = field(default_factory=dict)

    def dials_in_window(self, start: date, end: date) -> int:
        """Sum operations dials in [start, end] inclusive from by_day."""
        return sum(n for d, n in self.by_day.items() if start <= d <= end)


def load_jj_activity() -> JJActivity | None:
    """Load operations activity snapshot. Returns None if snapshot missing."""
    if not JJ_SNAPSHOT_PATH.exists():
        return None
    try:
        data = json.loads(JJ_SNAPSHOT_PATH.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    buckets = []
    for b in data.get("weekly_buckets", []):
        try:
            buckets.append(
                JJWeeklyBucket(
                    week_start=date.fromisoformat(b["week_start"]),
                    week_end=date.fromisoformat(b["week_end"]),
                    dials=int(b.get("dials", 0)),
                )
            )
        except (KeyError, ValueError):
            continue
    by_day: dict[date, int] = {}
    for ds, n in (data.get("by_day") or {}).items():
        try:
            by_day[date.fromisoformat(ds)] = int(n)
        except (TypeError, ValueError):
            continue
    return JJActivity(
        fetched_at=data.get("fetched_at", "—"),
        dials_today=int(data.get("dials_today", 0)),
        dials_this_week=int(data.get("dials_this_week", 0)),
        dials_lifetime=int(data.get("dials_lifetime", 0)),
        weekly_buckets=buckets,
        per_niche_lifetime=dict(data.get("per_niche_lifetime", {})),
        by_day=by_day,
    )


@dataclass
class WeeklyTrackerSnapshot:
    """One week's metrics parsed from brain/trackers/weekly/{date}-weekly-tracker.md."""
    week_end: date
    ndas: int = 0
    financials: int = 0
    lois: int = 0
    jj_dials: int = 0
    owner_conversations: int = 0
    outreach_sends: int = 0
    conferences: int = 0


def load_weekly_tracker_history() -> dict[date, WeeklyTrackerSnapshot]:
    """Parse every brain/trackers/weekly/*-weekly-tracker.md into a dict
    keyed by week_end date. Tolerant to format drift across weeks — pulls
    the first number from each known metric row, returns 0 when absent."""
    out: dict[date, WeeklyTrackerSnapshot] = {}
    if not WEEKLY_TRACKERS_DIR.exists():
        return out
    for entry in WEEKLY_TRACKERS_DIR.iterdir():
        m = _WEEKLY_TRACKER_FILENAME_RE.match(entry.name)
        if not m:
            continue
        try:
            week_end = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        try:
            text = entry.read_text(errors="replace")
        except OSError:
            continue
        snap = WeeklyTrackerSnapshot(week_end=week_end)
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cells) < 2:
                continue
            label = cells[0].lower()
            value_cell = cells[1]
            num_match = _FIRST_NUM_RE.search(value_cell)
            value = int(num_match.group(1).split(".")[0].replace(",", "")) if num_match else 0
            # Match common labels — tolerant to phrasing drift
            if "ndas signed" in label or "ndas /" in label or label.startswith("ndas"):
                snap.ndas = value
                # If row is "NDAs / financials / LOIs | 0 / 0 / 0", parse all 3
                fl_nums = _FIRST_NUM_RE.findall(value_cell)
                if "/" in label and len(fl_nums) >= 3:
                    snap.financials = int(fl_nums[1].split(".")[0])
                    snap.lois = int(fl_nums[2].split(".")[0])
            elif "financials received" in label:
                snap.financials = value
            elif "lois" in label or "loi submitted" in label:
                snap.lois = value
            elif "jj dials" in label or "jj: dials" in label or label.startswith("jj dials"):
                snap.jj_dials = value
            elif "owner conversation" in label or "owner calls 15" in label or "meaningful owner" in label:
                snap.owner_conversations = value
            elif "outreach" in label and ("send" in label or "email" in label):
                snap.outreach_sends = value
            elif "conferences" in label:
                snap.conferences = value
        out[week_end] = snap
    return out


# Snapshot staleness thresholds — beyond these, dashboard surfaces a banner.
# Both refresh jobs are weekday-only (Mon-Fri); on weekends/overnights the
# snapshot legitimately ages. Use larger thresholds during expected gaps so
# the banner only fires when something has actually broken.
_ATTIO_STALE_HOURS_WEEKDAY = 2  # hourly Mon-Fri 8am-8pm ET → 1h fires expected
_ATTIO_STALE_HOURS_OFF_HOURS = 60  # weekend + after-hours: cover Fri 8pm → Mon 8am gap
_JJ_STALE_HOURS_WEEKDAY = 30  # Mon-Fri 9am/2:30pm/6pm ET — 30h covers an overnight gap
_JJ_STALE_HOURS_OFF_HOURS = 72  # weekend covers Fri 6pm → Mon 9am


@dataclass
class StalenessCheck:
    label: str  # human-readable source name
    fetched_at: str  # ISO8601 string from snapshot
    age_hours: float
    threshold_hours: int
    is_stale: bool


def _hours_since(iso_ts: str | None) -> float | None:
    if not iso_ts:
        return None
    try:
        ts = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    except ValueError:
        return None
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - ts).total_seconds() / 3600.0


def _is_business_hours_et() -> bool:
    """True if local time is Mon-Fri 8am-8pm. Used to pick threshold."""
    now = datetime.now()
    if now.isoweekday() > 5:  # Sat/Sun
        return False
    return 8 <= now.hour < 20


def _attio_threshold() -> int:
    return _ATTIO_STALE_HOURS_WEEKDAY if _is_business_hours_et() else _ATTIO_STALE_HOURS_OFF_HOURS


def _jj_threshold() -> int:
    return _JJ_STALE_HOURS_WEEKDAY if _is_business_hours_et() else _JJ_STALE_HOURS_OFF_HOURS


def _check_snapshot_staleness(path: Path, label: str, threshold: int) -> StalenessCheck | None:
    """Read fetched_at from a snapshot JSON and check if it's older than threshold.
    Returns None if file missing — staleness banners shouldn't fire on cold start."""
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    fetched_at = data.get("fetched_at")
    age = _hours_since(fetched_at)
    if age is None:
        return None
    return StalenessCheck(
        label=label,
        fetched_at=fetched_at,
        age_hours=age,
        threshold_hours=threshold,
        is_stale=age > threshold,
    )


def check_dashboard_staleness() -> list[StalenessCheck]:
    """Return only the stale snapshots — empty list = all fresh.

    Threshold is weekend-aware: a 2-day-old snapshot on Saturday is fine
    (refresh job is Mon-Fri); a 4-hour-old snapshot during business hours
    means the job is stuck.
    """
    checks = [
        _check_snapshot_staleness(PIPELINE_SNAPSHOT_PATH, "Attio pipeline", _attio_threshold()),
        _check_snapshot_staleness(JJ_SNAPSHOT_PATH, "JJ activity", _jj_threshold()),
    ]
    return [c for c in checks if c is not None and c.is_stale]


CALIBRATION_OUTPUTS_DIR = Path(__file__).resolve().parent.parent / "brain" / "outputs" / "calibrations"
_CALIBRATION_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-calibration\.md$")
_CALIBRATION_ENTRY_RE = re.compile(
    r"^### \[([CHML])(\d+)\]\s+(.+?)$\n(.+?)(?=\n### \[|\n## |\Z)",
    re.MULTILINE | re.DOTALL,
)
_SEVERITY_ICON_COLOR = {
    "C": ("⚠", "accent"),
    "H": ("↻", "accent"),
    "M": ("⟶", "purple"),
    "L": ("•", "dim"),
}


def _latest_calibration_md() -> tuple[date, Path] | None:
    if not CALIBRATION_OUTPUTS_DIR.exists():
        return None
    candidates: list[tuple[date, Path]] = []
    for p in CALIBRATION_OUTPUTS_DIR.iterdir():
        m = _CALIBRATION_FILE_RE.match(p.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        candidates.append((d, p))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0]


def _parse_calibration_md(file_date: date, path: Path, max_entries: int = 8) -> CalibrationLog:
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return CalibrationLog(last_run="—", entries=[])

    age_days = (date.today() - file_date).days
    when_label = file_date.strftime("%a %b %-d")
    if age_days >= 7:
        last_run = f"{when_label} ({age_days}d ago — stale)"
    else:
        last_run = when_label

    entries: list[CalibrationEntry] = []
    for m in _CALIBRATION_ENTRY_RE.finditer(text):
        sev = m.group(1)
        num = m.group(2)
        headline = m.group(3).strip()
        body = m.group(4).strip()

        is_applied = "ALREADY APPLIED" in body.upper()
        if is_applied:
            icon, color = "✓", "green"
        else:
            icon, color = _SEVERITY_ICON_COLOR.get(sev, ("•", "dim"))

        # Prefer the **Problem:** line as the detail; fall back to first body line.
        detail = ""
        for raw in body.split("\n"):
            line = raw.strip()
            if line.startswith("**Problem:**"):
                detail = line.replace("**Problem:**", "").strip()
                break
        if not detail:
            for raw in body.split("\n"):
                line = raw.strip()
                if line and not line.startswith("**") and not line.startswith("```"):
                    detail = line[:240]
                    break
        if not detail:
            detail = "(no detail extracted)"

        entries.append(CalibrationEntry(
            icon=icon,
            icon_color=color,
            headline=f"[{sev}{num}] {headline}",
            detail=detail,
            when="applied" if is_applied else f"sev {sev}",
        ))
        if len(entries) >= max_entries:
            break

    return CalibrationLog(last_run=last_run, entries=entries)


def load_calibration_log() -> CalibrationLog:
    """Parse the latest brain/outputs/calibrations/*.md if present, fall back to YAML."""
    latest = _latest_calibration_md()
    if latest is not None:
        file_date, path = latest
        log = _parse_calibration_md(file_date, path)
        if log.entries:
            return log

    if not CALIBRATION_PATH.exists():
        return CalibrationLog(last_run="—", entries=[])
    try:
        data = yaml.safe_load(CALIBRATION_PATH.read_text()) or {}
    except (OSError, yaml.YAMLError):
        return CalibrationLog(last_run="—", entries=[])
    entries = [
        CalibrationEntry(
            icon=e.get("icon", "•"),
            icon_color=e.get("icon_color", "accent"),
            headline=e.get("headline", ""),
            detail=e.get("detail", ""),
            when=e.get("when", ""),
        )
        for e in data.get("entries", [])
    ]
    return CalibrationLog(
        last_run=data.get("last_run", "—"),
        entries=entries,
    )

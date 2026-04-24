"""Parsers for scheduled-skill artifacts that feed dashboard pages.

Each function returns plain dataclasses so the render layer stays decoupled
from the vault-schema details. Parsers tolerate the real variability of the
skill outputs (zero-deal days, sub-headers, missing fields).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
import re
from typing import Iterable

import yaml


VAULT_ROOT = Path(__file__).resolve().parent.parent / "brain"
DEAL_AGG_DIR = VAULT_ROOT / "context"


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

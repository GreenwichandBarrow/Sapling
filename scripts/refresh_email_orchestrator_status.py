#!/usr/bin/env python3
"""Refresh Email Orchestrator status for the dashboard.

This is a read-only summarizer over email-intelligence artifacts. It never
calls Gmail and never creates or sends drafts.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
import json
import re
from zoneinfo import ZoneInfo


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTEXT_DIR = REPO_ROOT / "brain" / "context"
OUT_PATH = CONTEXT_DIR / "email-orchestrator-status.json"
DASHBOARD_TZ = ZoneInfo("America/New_York")


@dataclass
class EmailOrchestratorStatus:
    fetched_at: str
    source_artifact: str | None
    source_status: str
    drafts_pending: int = 0
    send_blockers: int = 0
    deal_items: int = 0
    pipeline_items: int = 0
    relationship_items: int = 0
    task_candidates: int = 0
    needs_kay: list[str] = field(default_factory=list)
    blocked: list[str] = field(default_factory=list)


SECTION_RE = re.compile(r"^##\s+\d+\.\s+(.+?)\s*$", re.MULTILINE)


def now_et() -> datetime:
    return datetime.now(DASHBOARD_TZ)


def latest_email_artifact() -> Path | None:
    artifacts = sorted(CONTEXT_DIR.glob("email-scan-results-*.md"))
    return artifacts[-1] if artifacts else None


def section(text: str, title_fragment: str) -> str:
    matches = list(SECTION_RE.finditer(text))
    for idx, match in enumerate(matches):
        if title_fragment.lower() not in match.group(1).lower():
            continue
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        return text[start:end].strip()
    return ""


def first_int(pattern: str, text: str) -> int:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return 0
    try:
        return int(match.group(1))
    except ValueError:
        return 0


def bullet_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip().startswith("- "))


def table_data_rows(text: str) -> int:
    rows = 0
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if "---" in stripped or stripped.lower().startswith("| source ") or stripped.lower().startswith("| draft_id "):
            continue
        rows += 1
    return rows


def source_status(path: Path, now: datetime) -> str:
    name_match = re.search(r"email-scan-results-(\d{4}-\d{2}-\d{2})\.md$", path.name)
    if not name_match:
        return "error"
    artifact_date = name_match.group(1)
    if artifact_date != now.date().isoformat():
        return "stale"
    try:
        mtime = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).astimezone(DASHBOARD_TZ)
    except OSError:
        return "error"
    age_hours = (now - mtime).total_seconds() / 3600
    return "stale" if age_hours > 30 else "ok"


def build_status() -> EmailOrchestratorStatus:
    now = now_et()
    path = latest_email_artifact()
    if path is None:
        return EmailOrchestratorStatus(
            fetched_at=now.isoformat(),
            source_artifact=None,
            source_status="missing",
            blocked=["email-scan-results artifact missing"],
        )

    try:
        text = path.read_text(errors="replace")
    except OSError as exc:
        return EmailOrchestratorStatus(
            fetched_at=now.isoformat(),
            source_artifact=str(path.relative_to(REPO_ROOT)),
            source_status="error",
            blocked=[f"email artifact unreadable: {exc}"],
        )

    draft_section = section(text, "Draft Status")
    actionable_section = section(text, "Actionable Items")
    intro_section = section(text, "Introductions")
    broker_section = section(text, "Broker BLAST")
    granola_section = section(text, "Niche Signals")

    drafts_pending = first_int(r"Unsent:\s*(\d+)", draft_section)
    stale_drafts = first_int(r"Unsent older than 48 hours:\s*(\d+)", draft_section)
    deal_items = table_data_rows(broker_section)
    task_candidates = bullet_count(actionable_section)
    if "Granola Action Items" in granola_section:
        granola_tail = granola_section.split("Granola Action Items", 1)[1]
        if "None." not in granola_tail:
            task_candidates += bullet_count(granola_tail)

    relationship_items = 0 if re.search(r"\bNone\b", intro_section, re.IGNORECASE) else bullet_count(intro_section)
    status = source_status(path, now)

    needs_kay: list[str] = []
    blocked: list[str] = []
    if status != "ok":
        blocked.append(f"source artifact is {status}")
    if stale_drafts:
        needs_kay.append(f"{stale_drafts} Gmail drafts older than 48 hours")
    if task_candidates:
        needs_kay.append(f"{task_candidates} email-derived task candidate(s)")
    if deal_items:
        needs_kay.append(f"{deal_items} broker/listing row(s) extracted")
    if relationship_items:
        needs_kay.append(f"{relationship_items} introduction/relationship item(s)")

    return EmailOrchestratorStatus(
        fetched_at=now.isoformat(),
        source_artifact=str(path.relative_to(REPO_ROOT)),
        source_status=status,
        drafts_pending=drafts_pending,
        send_blockers=0,
        deal_items=deal_items,
        pipeline_items=0,
        relationship_items=relationship_items,
        task_candidates=task_candidates,
        needs_kay=needs_kay,
        blocked=blocked,
    )


def main() -> int:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    status = build_status()
    OUT_PATH.write_text(json.dumps(asdict(status), indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT_PATH}")
    print(f"source_status={status.source_status} drafts_pending={status.drafts_pending} deal_items={status.deal_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

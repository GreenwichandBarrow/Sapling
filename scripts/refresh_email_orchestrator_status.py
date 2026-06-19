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
BACKLOG_PATH = CONTEXT_DIR / "email-follow-through-backlog.json"
COMPLETED_STATUSES = {"completed", "done", "sent"}
DASHBOARD_TZ = ZoneInfo("America/New_York")


@dataclass
class EmailOrchestratorStatus:
    fetched_at: str
    source_artifact: str | None
    source_status: str
    input_artifact: str | None = None
    input_status: str = "unknown"
    drafts_pending: int = 0
    stale_drafts: int = 0
    drafts_missing_recipient: int = 0
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


def input_for_scan(path: Path) -> Path | None:
    name_match = re.search(r"email-scan-results-(\d{4}-\d{2}-\d{2})\.md$", path.name)
    if not name_match:
        return None
    candidate = CONTEXT_DIR / f"email-intelligence-input-{name_match.group(1)}.json"
    return candidate if candidate.exists() else None


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


def artifact_status(path: Path | None, now: datetime, pattern: str) -> str:
    if path is None:
        return "missing"
    name_match = re.search(pattern, path.name)
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


def source_status(path: Path, now: datetime) -> str:
    return artifact_status(path, now, r"email-scan-results-(\d{4}-\d{2}-\d{2})\.md$")


def input_status(path: Path | None, now: datetime) -> str:
    return artifact_status(path, now, r"email-intelligence-input-(\d{4}-\d{2}-\d{2})\.json$")


def parse_md_table(text: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        if "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        row = dict(zip(headers, cells[: len(headers)]))
        if any(row.values()):
            rows.append(row)
    return rows


def missing_recipient(value: str | None) -> bool:
    raw = (value or "").strip().lower()
    return raw in {"", "none", "—", "-", "(no recipient)", "no recipient", "unassigned"}


def load_json(path: Path | None) -> dict:
    if not path:
        return {}
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def compact_email_evidence(compact_input: dict) -> list[dict[str, str]]:
    evidence: list[dict[str, str]] = []
    for key in ("inbound", "outbound", "candidate_threads", "draft_details"):
        for row in compact_input.get(key, []) or []:
            if not isinstance(row, dict):
                continue
            evidence.append({
                "date": str(row.get("date") or row.get("created_at") or ""),
                "from": str(row.get("from") or ""),
                "to": str(row.get("to") or ""),
                "subject": str(row.get("subject") or ""),
                "snippet": str(row.get("snippet") or ""),
            })
    return evidence


def tokens(value: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", (value or "").lower()) if len(token) >= 3}


def date_key(value: str) -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value or "")
    return match.group(0) if match else ""


def email_evidence_completes(record: dict, evidence: list[dict[str, str]]) -> bool:
    person = str(record.get("person") or "").strip()
    email = str(record.get("email") or "").strip().lower()
    if not person and not email:
        return False
    due = str(record.get("due_date") or "")
    person_tokens = tokens(person)
    context_tokens = tokens(" ".join([str(record.get("context") or ""), str(record.get("event") or "")]))
    for row in evidence:
        row_date = date_key(row.get("date", ""))
        if due and row_date and row_date < due:
            continue
        address_text = " ".join([row.get("from", ""), row.get("to", "")]).lower()
        full_text = " ".join([address_text, row.get("subject", ""), row.get("snippet", "")]).lower()
        if email and email in full_text:
            return True
        if person_tokens and person_tokens.issubset(tokens(address_text)):
            return True
        if person_tokens and person_tokens & tokens(address_text) and context_tokens & tokens(full_text):
            return True
    return False


def unclear_followthrough_items(evidence: list[dict[str, str]]) -> list[str]:
    data = load_json(BACKLOG_PATH)
    unclear: list[str] = []
    for record in data.get("items", []) or []:
        if not isinstance(record, dict):
            continue
        if str(record.get("status") or "").lower() in COMPLETED_STATUSES:
            continue
        if str(record.get("bucket") or "") == "warm":
            continue
        if email_evidence_completes(record, evidence):
            continue
        person = str(record.get("person") or "").strip()
        email = str(record.get("email") or "").strip()
        event = str(record.get("event") or "").strip().lower()
        has_call_artifact = bool(record.get("call_artifact"))
        weak_person = len(tokens(person)) <= 1
        if missing_recipient(person) or (not email and not has_call_artifact and (weak_person or event.startswith("needs source"))):
            unclear.append(person or "unassigned follow-through")
    return unclear


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
    pipeline_section = section(text, "Pipeline") or section(text, "Active Deal Fast-Path")

    drafts_pending = first_int(r"Unsent:\s*(\d+)", draft_section)
    stale_drafts = first_int(r"Unsent older than 48 hours:\s*(\d+)", draft_section)
    draft_rows = parse_md_table(draft_section)
    drafts_missing_recipient = sum(
        1
        for row in draft_rows
        if (row.get("status") or "").upper() == "DRAFT" and missing_recipient(row.get("to"))
    )
    deal_items = table_data_rows(broker_section)
    pipeline_items = table_data_rows(pipeline_section) or bullet_count(pipeline_section)
    task_candidates = bullet_count(actionable_section)
    if "Granola Action Items" in granola_section:
        granola_tail = granola_section.split("Granola Action Items", 1)[1]
        if "None." not in granola_tail:
            task_candidates += bullet_count(granola_tail)

    relationship_items = 0 if re.search(r"\bNone\b", intro_section, re.IGNORECASE) else bullet_count(intro_section)
    status = source_status(path, now)
    input_path = input_for_scan(path)
    input_state = input_status(input_path, now)
    compact_input = load_json(input_path)
    evidence = compact_email_evidence(compact_input)
    unclear_items = unclear_followthrough_items(evidence)

    needs_kay: list[str] = []
    blocked: list[str] = []
    if status != "ok":
        blocked.append(f"source artifact is {status}")
    if input_state != "ok":
        blocked.append(f"compact input artifact is {input_state}")
    if stale_drafts:
        needs_kay.append(f"{stale_drafts} Gmail drafts older than 48 hours")
    if drafts_missing_recipient:
        needs_kay.append(f"{drafts_missing_recipient} draft(s) missing recipient")
    if task_candidates:
        needs_kay.append(f"{task_candidates} email-derived task candidate(s)")
    if deal_items:
        needs_kay.append(f"{deal_items} broker/listing row(s) extracted")
    if relationship_items:
        needs_kay.append(f"{relationship_items} introduction/relationship item(s)")
    if unclear_items:
        names = "; ".join(unclear_items[:4])
        extra = f" (+{len(unclear_items) - 4} more)" if len(unclear_items) > 4 else ""
        needs_kay.append(f"Clarify email follow-through identity/source: {names}{extra}")

    return EmailOrchestratorStatus(
        fetched_at=now.isoformat(),
        source_artifact=str(path.relative_to(REPO_ROOT)),
        source_status=status,
        input_artifact=str(input_path.relative_to(REPO_ROOT)) if input_path else None,
        input_status=input_state,
        drafts_pending=drafts_pending,
        stale_drafts=stale_drafts,
        drafts_missing_recipient=drafts_missing_recipient,
        send_blockers=0,
        deal_items=deal_items,
        pipeline_items=pipeline_items,
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
    print(
        f"source_status={status.source_status} input_status={status.input_status} "
        f"drafts_pending={status.drafts_pending} stale_drafts={status.stale_drafts} "
        f"deal_items={status.deal_items}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Refresh Email Orchestrator status for the dashboard.

This is a safe refresh job over email-intelligence artifacts plus bounded
read-only Gmail sent-mail verification. It never creates or sends drafts.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
import json
import os
import re
import subprocess
from zoneinfo import ZoneInfo


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTEXT_DIR = REPO_ROOT / "brain" / "context"
OUT_PATH = CONTEXT_DIR / "email-orchestrator-status.json"
BACKLOG_PATH = CONTEXT_DIR / "email-follow-through-backlog.json"
COMPLETED_STATUSES = {"completed", "done", "sent"}
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")
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
    thank_you_items: list[dict[str, str]] = field(default_factory=list)
    follow_through_completed_items: list[dict[str, str]] = field(default_factory=list)
    follow_through_pending_items: list[dict[str, str]] = field(default_factory=list)
    unclear_followthrough_items: list[str] = field(default_factory=list)
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


TARGET_SOURCE_SNAPSHOTS = [
    CONTEXT_DIR / "rollback-snapshots" / "jj-dealsx-dedup-20260621T220411Z.json",
    CONTEXT_DIR / "rollback-snapshots" / "jj-dealsx-dedup-20260614T180443.json",
    CONTEXT_DIR / "rollback-snapshots" / "dealsx-new-verticals-may-pre-attio-dedup-2026-05-05.json",
]


TARGET_ALIASES = {
    "mmpc": "mmpc new york city",
    "alliance pest": "alliance pest control",
    "debug pest control": "debug pest control ri ct mass",
}


def canonical_company(value: str) -> str:
    cleaned = re.sub(r"\([^)]*\)", " ", value or "")
    cleaned = re.split(r"\s+/\s+", cleaned, maxsplit=1)[0]
    cleaned = re.sub(r"\b(co|company|inc|llc|ltd|services|service)\b", " ", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"[^a-z0-9]+", " ", cleaned.lower())
    key = re.sub(r"\s+", " ", cleaned).strip()
    return TARGET_ALIASES.get(key, key)


def https_url(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    if raw.startswith(("http://", "https://")):
        return raw
    if "." in raw and " " not in raw:
        return f"https://{raw}"
    return ""


def source_record_urls(record: dict) -> dict[str, str]:
    website = https_url(record.get("website") or record.get("Website") or record.get("domain") or "")
    owner_linkedin = str(record.get("linkedin_url") or record.get("LinkedIn Owner") or "").strip()
    company_linkedin = str(record.get("company_linkedin") or record.get("LinkedIn Company") or "").strip()
    row = record.get("row")
    if isinstance(row, list):
        if len(row) > 2:
            website = website or https_url(row[2])
        if len(row) > 16:
            owner_linkedin = owner_linkedin or str(row[16] or "").strip()
        if len(row) > 17:
            company_linkedin = company_linkedin or str(row[17] or "").strip()
    linkedin = owner_linkedin or company_linkedin
    return {
        "website_url": website,
        "linkedin_url": linkedin if linkedin.startswith(("http://", "https://")) else "",
    }


def target_source_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}

    def add_record(record: dict, source_path: Path) -> None:
        company = str(record.get("company") or record.get("Company") or record.get("name") or "").strip()
        row = record.get("row")
        if not company and isinstance(row, list) and len(row) > 1:
            company = str(row[1] or "").strip()
        key = canonical_company(company)
        if not key:
            return
        urls = source_record_urls(record)
        current = index.setdefault(key, {"source_artifact": str(source_path.relative_to(REPO_ROOT))})
        for field in ("website_url", "linkedin_url"):
            if urls.get(field) and not current.get(field):
                current[field] = urls[field]

    def walk(value, source_path: Path) -> None:
        if isinstance(value, dict):
            add_record(value, source_path)
            for child in value.values():
                walk(child, source_path)
        elif isinstance(value, list):
            for child in value:
                walk(child, source_path)

    for source_path in TARGET_SOURCE_SNAPSHOTS:
        payload = load_json(source_path)
        if payload:
            walk(payload, source_path)
    return index


def enrich_backlog_source_links() -> int:
    data = load_json(BACKLOG_PATH)
    items = data.get("items", [])
    if not isinstance(items, list):
        return 0
    index = target_source_index()
    changed = 0
    today = now_et().date().isoformat()
    for item in items:
        if not isinstance(item, dict):
            continue
        if str(item.get("bucket") or "") != "warm":
            continue
        if item.get("website_url") and item.get("linkedin_url"):
            continue
        key = canonical_company(str(item.get("person") or ""))
        source = index.get(key)
        if not source:
            continue
        for field in ("website_url", "linkedin_url", "source_artifact"):
            if source.get(field) and not item.get(field):
                item[field] = source[field]
                changed += 1
    if changed:
        data["updated_at"] = today
        BACKLOG_PATH.write_text(json.dumps(data, indent=2) + "\n")
    return changed


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


def google_date(value: str) -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value or "")
    return match.group(0) if match else ""


def run_gog_json(args: list[str], timeout: int = 30) -> dict:
    try:
        proc = subprocess.run(
            ["gog", *args],
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {}
    if proc.returncode != 0:
        return {}
    try:
        return json.loads(proc.stdout or "{}")
    except json.JSONDecodeError:
        return {}


def external_meeting_person(summary: str) -> str:
    cleaned = re.sub(r"\s+", " ", summary or "").strip()
    patterns = [
        r"^(?:Lunch\s+)?(.+?)\s+[|I]\s+Kay(?:\s+Mtg)?$",
        r"^Kay\s+[|I/]\s+(.*?)(?:\s+Mtg)?$",
        r"^(?:Lunch\s+)?(.+?)\s*/\s*Kay",
        r"^Kay\s*/\s*(.*?)$",
        r"^Call w/\s+(.*?)$",
        r"^Call\s+(.+?)(?:\s+at\s+.+)?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, cleaned, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip(" -")
    return cleaned


def is_external_calendar_event(event: dict) -> bool:
    summary = str(event.get("summary") or "").strip()
    if not summary:
        return False
    if event.get("status") == "cancelled":
        return False
    if event.get("transparency") == "transparent":
        return False
    start = event.get("start") or {}
    if "dateTime" not in start:
        return False
    lowered = summary.lower()
    skip_terms = (
        "auto payroll",
        "webinar",
        "financial literacy",
        "class",
        "hold",
        "reminder",
        "deal team day",
        "team tb",
    )
    if any(term in lowered for term in skip_terms):
        return False
    attendees = event.get("attendees") or []
    external_attendee = any(
        isinstance(att, dict)
        and not att.get("self")
        and "greenwichandbarrow.com" not in str(att.get("email") or "").lower()
        for att in attendees
    )
    kay_pair_pattern = bool(re.search(r"\b(kay\s*[/|I]|[/|I]\s*kay|call w/|call\s+)\b", summary, flags=re.IGNORECASE))
    return external_attendee or kay_pair_pattern


def seed_prior_day_thank_yous() -> int:
    data = load_json(BACKLOG_PATH)
    items = data.get("items", [])
    if not isinstance(items, list):
        return 0
    yesterday = (now_et().date() - timedelta(days=1)).isoformat()
    today = now_et().date().isoformat()
    payload = run_gog_json([
        "calendar",
        "events",
        "--from",
        yesterday,
        "--to",
        today,
        "--account",
        GOG_ACCOUNT,
        "--json",
        "--max=100",
    ])
    events = payload.get("events", []) or []
    existing_keys = {
        (
            str(item.get("bucket") or ""),
            str(item.get("calendar_event_id") or ""),
            str(item.get("person") or "").strip().lower(),
            str(item.get("event_date") or ""),
        )
        for item in items
        if isinstance(item, dict)
    }
    added = 0
    for event in events:
        if not isinstance(event, dict) or not is_external_calendar_event(event):
            continue
        summary = str(event.get("summary") or "").strip()
        person = external_meeting_person(summary)
        event_id = str(event.get("id") or "")
        key = ("thank", event_id, person.lower(), yesterday)
        fallback_key = ("thank", "", person.lower(), yesterday)
        if key in existing_keys or fallback_key in existing_keys:
            continue
        attendees = event.get("attendees") or []
        external_emails = [
            str(att.get("email") or "").lower()
            for att in attendees
            if isinstance(att, dict)
            and not att.get("self")
            and "greenwichandbarrow.com" not in str(att.get("email") or "").lower()
        ]
        items.append({
            "bucket": "thank",
            "person": person,
            "email": external_emails[0] if external_emails else "",
            "context": "24-hour thank-you after external meeting",
            "due_date": today,
            "status": "not drafted",
            "source": "calendar-prior-day-refresh",
            "event": summary,
            "event_date": yesterday,
            "calendar_event_id": event_id,
        })
        existing_keys.add(key)
        added += 1
    if added:
        data["items"] = items
        data["updated_at"] = today
        BACKLOG_PATH.write_text(json.dumps(data, indent=2) + "\n")
    return added


def sent_search_query(record: dict) -> str | None:
    email = str(record.get("email") or "").strip().lower()
    if email and "@" in email:
        return f"in:sent newer_than:30d to:{email}"

    person = str(record.get("person") or "").strip()
    event = str(record.get("event") or "").strip()
    context = str(record.get("context") or "").strip()
    if not person or event.lower().startswith("needs source"):
        return None

    person_terms = sorted(tokens(person))
    context_terms = [
        term
        for term in sorted(tokens(f"{event} {context}"))
        if term not in {"after", "call", "email", "follow", "followup", "meeting", "requested", "thank", "with"}
    ]
    if len(context_terms) < 2:
        return None

    terms = person_terms[:2] + context_terms[:4]
    return "in:sent newer_than:30d " + " ".join(terms)


def sent_thread_after_due(record: dict) -> dict | None:
    query = sent_search_query(record)
    if not query:
        return None
    payload = run_gog_json([
        "gmail",
        "search",
        query,
        "--account",
        GOG_ACCOUNT,
        "--json",
        "--max=5",
    ], timeout=20)
    due = str(record.get("due_date") or "")
    for thread in payload.get("threads", []) or []:
        thread_date = date_key(str(thread.get("date") or ""))
        if due and thread_date and thread_date < due:
            continue
        if thread.get("id"):
            return thread
    return None


def reconcile_backlog_with_sent_mail() -> list[dict[str, str]]:
    data = load_json(BACKLOG_PATH)
    items = data.get("items", [])
    if not isinstance(items, list):
        return []
    changed_rows: list[dict[str, str]] = []
    today = now_et().date().isoformat()
    for record in items:
        if not isinstance(record, dict):
            continue
        if str(record.get("status") or "").lower() in COMPLETED_STATUSES:
            continue
        if not record.get("bucket"):
            continue
        thread = sent_thread_after_due(record)
        if not thread:
            continue
        sent_at = str(thread.get("date") or "")
        record["status"] = "completed"
        record["completed_at"] = date_key(sent_at) or today
        record["completed_note"] = (
            "Auto-completed by email-orchestration refresh from Gmail sent-mail evidence; "
            f"thread {thread.get('id')}, subject {thread.get('subject')!r}, sent {sent_at}."
        )
        record["sent_evidence"] = {
            "source": "gmail_sent_search",
            "thread_id": thread.get("id", ""),
            "subject": thread.get("subject", ""),
            "sent_at": sent_at,
        }
        changed_rows.append({
            "bucket": str(record.get("bucket") or ""),
            "person": str(record.get("person") or ""),
            "event": str(record.get("event") or ""),
            "completed_at": record["completed_at"],
            "sent_at": sent_at,
            "sent_subject": str(thread.get("subject") or ""),
            "sent_thread_id": str(thread.get("id") or ""),
        })
    if changed_rows:
        data["updated_at"] = today
        BACKLOG_PATH.write_text(json.dumps(data, indent=2) + "\n")
    return changed_rows


def display_first_name(value: str) -> str:
    raw = re.sub(r"\s+", " ", value or "").strip()
    raw = re.sub(r"^(Lunch|Call)\s+", "", raw, flags=re.IGNORECASE)
    raw = re.split(r"\s+[|I/]\s+Kay|\s+at\s+", raw, maxsplit=1, flags=re.IGNORECASE)[0]
    return raw.split()[0] if raw else "Unassigned"


def follow_through_completed_summary_items(changed_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for record in changed_rows:
        if not isinstance(record, dict):
            continue
        person = display_first_name(str(record.get("person") or record.get("event") or ""))
        rows.append({
            "bucket": str(record.get("bucket") or ""),
            "person": person,
            "event": str(record.get("event") or ""),
            "completed_at": str(record.get("completed_at") or ""),
            "sent_at": str(record.get("sent_at") or ""),
            "sent_subject": str(record.get("sent_subject") or ""),
            "sent_thread_id": str(record.get("sent_thread_id") or ""),
        })
    return rows


def thank_you_summary_items() -> list[dict[str, str]]:
    """Return prior-day thank-you rows for Good Morning/dashboard review.

    Completed rows are included with sent evidence so the morning brief can say
    they were verified; pending rows are the only ones Kay should approve/add.
    """
    data = load_json(BACKLOG_PATH)
    yesterday = (now_et().date() - timedelta(days=1)).isoformat()
    rows: list[dict[str, str]] = []
    for record in data.get("items", []) or []:
        if not isinstance(record, dict):
            continue
        if str(record.get("bucket") or "") != "thank":
            continue
        if str(record.get("event_date") or "") != yesterday:
            continue
        evidence = record.get("sent_evidence") or {}
        rows.append({
            "person": str(record.get("person") or ""),
            "email": str(record.get("email") or ""),
            "event": str(record.get("event") or ""),
            "event_date": str(record.get("event_date") or ""),
            "due_date": str(record.get("due_date") or ""),
            "status": str(record.get("status") or ""),
            "completed_at": str(record.get("completed_at") or ""),
            "sent_thread_id": str(evidence.get("thread_id") or ""),
            "sent_subject": str(evidence.get("subject") or ""),
            "sent_at": str(evidence.get("sent_at") or ""),
        })
    return sorted(rows, key=lambda row: (row["status"].lower() not in COMPLETED_STATUSES, row["person"].lower()))


def pending_followthrough_summary_items(evidence: list[dict[str, str]]) -> list[dict[str, str]]:
    """Return active EOW/follow-up rows after sent-mail reconciliation.

    Good Morning should not surface EOW rows until sent-mail evidence has been
    checked. Completed rows stay suppressed; active rows carry enough identity
    detail for Kay to approve, keep, or clarify without a vague count.
    """
    data = load_json(BACKLOG_PATH)
    rows: list[dict[str, str]] = []
    for record in data.get("items", []) or []:
        if not isinstance(record, dict):
            continue
        bucket = str(record.get("bucket") or "")
        if bucket not in {"eow", "followup"}:
            continue
        if str(record.get("status") or "").lower() in COMPLETED_STATUSES:
            continue
        if record.get("needs_kay_clarification"):
            continue
        if email_evidence_completes(record, evidence):
            continue
        rows.append({
            "bucket": bucket,
            "person": str(record.get("person") or ""),
            "event": str(record.get("event") or ""),
            "context": str(record.get("context") or ""),
            "due_date": str(record.get("due_date") or ""),
            "status": str(record.get("status") or ""),
            "kay_confirmed_keep": str(bool(record.get("kay_confirmed_keep"))).lower(),
            "needs_kay_clarification": str(bool(record.get("needs_kay_clarification"))).lower(),
        })
    return sorted(rows, key=lambda row: (row["bucket"], row["due_date"], row["person"].lower()))


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
        if record.get("kay_confirmed_keep") or record.get("identity_confirmed"):
            continue
        if email_evidence_completes(record, evidence):
            continue
        person = str(record.get("person") or "").strip()
        email = str(record.get("email") or "").strip()
        event = str(record.get("event") or "").strip()
        event_l = event.lower()
        context = str(record.get("context") or "").strip()
        bucket = str(record.get("bucket") or "").strip()
        has_call_artifact = bool(record.get("call_artifact"))
        weak_person = len(tokens(person)) <= 1
        forced_clarify = bool(record.get("needs_kay_clarification"))
        missing_eow_context = bucket == "eow" and not email and not has_call_artifact
        if forced_clarify or missing_recipient(person) or missing_eow_context or (not email and not has_call_artifact and (weak_person or event_l.startswith("needs source"))):
            detail = person or "unassigned follow-through"
            if context and context.lower() != detail.lower():
                detail = f"{detail} ({context})"
            elif event and event.lower() != detail.lower():
                detail = f"{detail} ({event})"
            unclear.append(detail)
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
    seeded_count = seed_prior_day_thank_yous()
    enriched_count = enrich_backlog_source_links()
    reconciled_items_raw = reconcile_backlog_with_sent_mail()
    reconciled_count = len(reconciled_items_raw)
    follow_through_completed_items = follow_through_completed_summary_items(reconciled_items_raw)
    compact_input = load_json(input_path)
    evidence = compact_email_evidence(compact_input)
    pending_followthrough_items = pending_followthrough_summary_items(evidence)
    unclear_items = unclear_followthrough_items(evidence)
    thank_items = thank_you_summary_items()
    pending_thank_items = [
        item for item in thank_items
        if str(item.get("status") or "").lower() not in COMPLETED_STATUSES
    ]
    completed_thank_items = [
        item for item in thank_items
        if str(item.get("status") or "").lower() in COMPLETED_STATUSES
    ]

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
    if pending_thank_items:
        names = "; ".join(item.get("person") or "Unassigned" for item in pending_thank_items[:4])
        extra = f" (+{len(pending_thank_items) - 4} more)" if len(pending_thank_items) > 4 else ""
        needs_kay.append(f"{len(pending_thank_items)} prior-day thank-you(s) need approval: {names}{extra}")
    if completed_thank_items:
        needs_kay.append(f"{len(completed_thank_items)} prior-day thank-you(s) verified sent")
    if enriched_count:
        needs_kay.append(f"{enriched_count} email follow-through source link field(s) enriched")
    if follow_through_completed_items:
        names = "; ".join(item.get("person") or "Unassigned" for item in follow_through_completed_items)
        needs_kay.append(f"{len(follow_through_completed_items)} email follow-through row(s) auto-completed from sent-mail evidence: {names}")
    if pending_followthrough_items:
        names = "; ".join(item.get("person") or "Unassigned" for item in pending_followthrough_items)
        needs_kay.append(f"{len(pending_followthrough_items)} EOW/follow-up row(s) still active after sent-mail check: {names}")
    if unclear_items:
        names = "; ".join(unclear_items)
        needs_kay.append(f"Clarify email follow-through identity/source: {names}")

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
        thank_you_items=thank_items,
        follow_through_completed_items=follow_through_completed_items,
        follow_through_pending_items=pending_followthrough_items,
        unclear_followthrough_items=unclear_items,
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

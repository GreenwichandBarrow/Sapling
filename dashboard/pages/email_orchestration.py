"""Email Orchestration page.

Shows Kay's email follow-through deadlines without becoming an inbox mirror.
The page never renders email bodies and never sends email.
"""

from __future__ import annotations

from functools import lru_cache
from html import escape
import json
import re
from textwrap import dedent
from datetime import date, timedelta

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import VAULT_ROOT, load_email_orchestrator_status  # noqa: E402


GMAIL_BASE = "https://mail.google.com/mail/u/0"
BACKLOG_ARTIFACT = "brain/context/email-follow-through-backlog.json"
COMPLETED_STATUSES = {"completed", "done", "sent"}


def _source_path(source_artifact: str | None) -> Path | None:
    if not source_artifact:
        return None
    source = source_artifact.removeprefix("brain/")
    path = VAULT_ROOT / source
    return path if path.exists() else None


def _input_path(input_artifact: str | None) -> Path | None:
    if not input_artifact:
        return None
    source = input_artifact.removeprefix("brain/")
    path = VAULT_ROOT / source
    return path if path.exists() else None


def _section(body: str, heading: str) -> str:
    pattern = re.compile(rf"^##\s+{re.escape(heading)}.*?$", re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+", body[start:], re.MULTILINE)
    return body[start : start + next_heading.start()] if next_heading else body[start:]


def _parse_md_table(section: str) -> list[dict[str, str]]:
    lines = [line.strip() for line in section.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [h.strip() for h in lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        row = dict(zip(headers, cells[: len(headers)]))
        if any(row.values()):
            rows.append(row)
    return rows


def _load_source_body(source_artifact: str | None) -> str:
    path = _source_path(source_artifact)
    if not path:
        return ""
    return path.read_text()


def _backlog_path() -> Path:
    return VAULT_ROOT / "context/email-follow-through-backlog.json"


def _manual_backlog_records() -> list[dict[str, str]]:
    path = _backlog_path()
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return []
    items = []
    for item in data.get("items", []):
        if not item.get("bucket"):
            continue
        items.append(item)
    return items


def _manual_backlog_items() -> list[dict[str, str]]:
    return [
        item
        for item in _manual_backlog_records()
        if (item.get("status") or "").lower() not in COMPLETED_STATUSES
    ]


def _load_compact_input(input_artifact: str | None) -> dict:
    path = _input_path(input_artifact)
    if not path:
        return {}
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def _compact_email_evidence(compact_input: dict) -> list[dict[str, str]]:
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


def _tokens(value: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", (value or "").lower()) if len(token) >= 3}


def _date_key(value: str) -> str:
    match = re.search(r"\d{4}-\d{2}-\d{2}", value or "")
    return match.group(0) if match else ""


def _email_evidence_completes(record: dict[str, str], evidence: list[dict[str, str]]) -> bool:
    person = (record.get("person") or "").strip()
    email = (record.get("email") or "").strip().lower()
    if not person and not email:
        return False
    due = record.get("due_date") or ""
    person_tokens = _tokens(person)
    context_tokens = _tokens(" ".join([record.get("context", ""), record.get("event", "")]))
    for row in evidence:
        row_date = _date_key(row.get("date", ""))
        if due and row_date and row_date < due:
            continue
        address_text = " ".join([row.get("from", ""), row.get("to", "")]).lower()
        full_text = " ".join([address_text, row.get("subject", ""), row.get("snippet", "")]).lower()
        if email and email in full_text:
            return True
        if person_tokens and person_tokens.issubset(_tokens(address_text)):
            return True
        if person_tokens and person_tokens & _tokens(address_text) and context_tokens & _tokens(full_text):
            return True
    return False


def _draft_rows(body: str) -> list[dict[str, str]]:
    return _parse_md_table(_section(body, "3. Draft Status"))


def _age_float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _gmail_thread_link(thread_id: str) -> str | None:
    if not thread_id or thread_id in {"—", "-"}:
        return None
    return f"{GMAIL_BASE}/#all/{escape(thread_id)}"


def _missing_recipient(value: str | None) -> bool:
    raw = (value or "").strip().lower()
    return raw in {"", "none", "—", "-", "(no recipient)", "no recipient", "unassigned"}


def _row_status(row: dict[str, str]) -> str:
    age = _age_float(row.get("age_hours") or "")
    if _missing_recipient(row.get("to")):
        return "needs recipient"
    if age and age > 48:
        return "draft stale"
    return "ready"


def _contact_parts(value: str) -> tuple[str, str]:
    raw = (value or "").strip()
    if _missing_recipient(raw):
        return "Needs recipient", ""
    match = re.match(r"^(.*?)\s*<([^>]+)>$", raw)
    if match:
        return match.group(1).strip() or match.group(2).strip(), match.group(2).strip().lower()
    if "@" in raw and " " not in raw:
        return raw, raw.lower()
    return raw or "Unassigned", ""


def _identity_key(person: str = "", email: str = "") -> str:
    if email:
        return f"email:{email.lower()}"
    return f"person:{re.sub(r'[^a-z0-9]+', ' ', person.lower()).strip()}"


def _clean_display(value: str) -> str:
    cleaned = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", value or "")
    cleaned = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).split("/")[-1].replace("-", " ").title(), cleaned)
    return cleaned.strip()


@lru_cache(maxsize=1)
def _entity_email_index() -> dict[str, dict[str, str]]:
    entities_dir = VAULT_ROOT / "entities"
    if not entities_dir.exists():
        return {}
    index: dict[str, dict[str, str]] = {}
    for entity_path in entities_dir.glob("*.md"):
        try:
            body = entity_path.read_text()
        except OSError:
            continue
        email_match = re.search(r"^email:\s*([^\n]+)", body, re.MULTILINE)
        if not email_match:
            continue
        email = email_match.group(1).strip().strip('"').lower()
        if not email or "@" not in email:
            continue
        title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        event = ""
        context_match = re.search(r"- Met Kay at an? (.+?)(?: on \d{4}-\d{2}-\d{2}|\.)", body)
        if context_match:
            event = _clean_display(context_match.group(1).strip())
        index[email] = {
            "person": _clean_display(title_match.group(1).strip()) if title_match else email,
            "event": event,
        }
    return index


def _entity_for_email(email: str) -> dict[str, str]:
    if not email:
        return {}
    return _entity_email_index().get(email.lower(), {})


def _bucket_for(row: dict[str, str]) -> str:
    subject = (row.get("subject") or "").lower()
    if "heels to deals" in subject or "conference" in subject:
        return "eow"
    if "great meeting" in subject or "thank" in subject:
        return "thank"
    if "follow" in subject or "broker" in subject or "intermediary" in subject:
        return "followup"
    return "followup"


def _due_date(bucket: str, age_hours: str) -> date:
    today = date.today()
    age = _age_float(age_hours) or 0
    if bucket == "thank":
        return today - timedelta(days=1) if age > 24 else today
    if bucket == "followup":
        return today - timedelta(days=1) if age > 48 else today
    days_until_friday = (4 - today.weekday()) % 7
    return today + timedelta(days=days_until_friday)


def _due_text(bucket: str, age_hours: str) -> str:
    due = _due_date(bucket, age_hours)
    label = due.strftime("%b %-d")
    if due < date.today():
        return f"Due {label} · overdue"
    if due == date.today():
        return f"Due {label} · today"
    return f"Due {label}"


def _item(row: dict[str, str], bucket: str, manual: dict[str, str] | None = None) -> dict[str, str]:
    age = row.get("age_hours") or ""
    person, email = _contact_parts(row.get("to") or "")
    entity = _entity_for_email(email)
    manual = manual or {}
    due = manual.get("due_date") or _due_date(bucket, age).isoformat()
    return {
        "person": manual.get("person") or entity.get("person") or person,
        "email": manual.get("email") or email,
        "event": manual.get("event") or entity.get("event") or "",
        "subject": manual.get("context") or row.get("subject") or "Draft",
        "status": manual.get("status") if manual.get("status") == "overdue" else _row_status(row),
        "thread_id": row.get("thread_id") or manual.get("thread_id") or "",
        "age": age,
        "due_date": due,
        "due_text": _manual_due_text(due),
        "source": "scan",
    }


def _manual_due_text(due_date: str) -> str:
    try:
        due = date.fromisoformat(due_date)
    except ValueError:
        return "Due date missing"
    label = due.strftime("%b %-d")
    if due < date.today():
        return f"Due {label} · overdue"
    if due == date.today():
        return f"Due {label} · today"
    return f"Due {label}"


def _manual_item(record: dict[str, str]) -> dict[str, str]:
    due = record.get("due_date") or date.today().isoformat()
    return {
        "person": record.get("person") or "Unassigned",
        "email": record.get("email") or "",
        "event": record.get("event") or "",
        "subject": record.get("context") or record.get("subject") or "Follow-through item",
        "status": record.get("status") or "manual",
        "thread_id": record.get("thread_id") or "",
        "website_url": record.get("website_url") or "",
        "linkedin_url": record.get("linkedin_url") or "",
        "source_url": record.get("source_url") or "",
        "draft_url": record.get("draft_url") or "",
        "age": "",
        "due_date": due,
        "due_text": _manual_due_text(due),
        "source": "manual",
    }


def _is_warm_bundle(item: dict[str, str]) -> bool:
    """Hide campaign bundles until they are expanded into one row per recipient."""
    person = (item.get("person") or "").strip().lower()
    subject = (item.get("subject") or "").strip().lower()
    if re.match(r"^\d+\s+", person):
        return True
    bundle_terms = ("firms", "companies", "targets", "campaign")
    return any(term in person for term in bundle_terms) or any(term in subject for term in bundle_terms)


def _targeted_outreach_items(items: list[dict[str, str]]) -> list[dict[str, str]]:
    return [item for item in items if not _is_warm_bundle(item)]


def _bucketed_items(rows: list[dict[str, str]], evidence: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    buckets = {"thank": [], "followup": [], "eow": [], "warm": []}
    all_manual_records = _manual_backlog_records()
    completed_keys = {
        _identity_key(record.get("person", ""), record.get("email", ""))
        for record in all_manual_records
        if (record.get("status") or "").lower() in COMPLETED_STATUSES
    }
    manual_records = [
        record
        for record in all_manual_records
        if (record.get("status") or "").lower() not in COMPLETED_STATUSES
        and not _email_evidence_completes(record, evidence)
    ]
    manual_by_key = {}
    for record in manual_records:
        key = _identity_key(record.get("person", ""), record.get("email", ""))
        manual_by_key[key] = record

    consumed_manual_keys: set[str] = set()
    for row in rows:
        if (row.get("status") or "").upper() != "DRAFT":
            continue
        status = _row_status(row)
        if status == "needs recipient":
            continue
        person, email = _contact_parts(row.get("to") or "")
        key = _identity_key(person, email)
        if key in completed_keys:
            continue
        manual = manual_by_key.get(key)
        if manual:
            consumed_manual_keys.add(key)
        bucket = (manual or {}).get("bucket") or _bucket_for(row)
        buckets.setdefault(bucket, []).append(_item(row, bucket, manual))

    for record in manual_records:
        key = _identity_key(record.get("person", ""), record.get("email", ""))
        if key in consumed_manual_keys:
            continue
        bucket = record.get("bucket", "followup")
        buckets.setdefault(bucket, []).append(_manual_item(record))
    for bucket_items in buckets.values():
        bucket_items.sort(key=lambda item: (item["due_date"], item["person"].lower()))
    return buckets


def _priority_class(item: dict[str, str], bucket: str) -> str:
    if item["status"] == "overdue":
        return "late"
    if item["status"] in {"needs recipient", "not started", "not drafted"}:
        return "prep"
    age = _age_float(item.get("age") or "")
    if bucket == "thank" and age and age > 24:
        return "late"
    if bucket == "followup" and age and age > 48:
        return "late"
    return "ready"


def _priority_label(item: dict[str, str], bucket: str) -> str:
    if item["status"] == "overdue":
        return "overdue"
    if item["status"] in {"not started", "not drafted"}:
        return "not started"
    if item["status"] == "needs recipient":
        return "system prep"
    age = _age_float(item.get("age") or "")
    if bucket == "thank" and age and age > 24:
        return "past 24h"
    if bucket == "followup" and age and age > 48:
        return "past 48h"
    if bucket == "eow":
        return "by Friday"
    return "ready"


def _action_link(item: dict[str, str]) -> str:
    link = _gmail_thread_link(item.get("thread_id", ""))
    if not link:
        label = "not drafted" if item.get("source") == "manual" else "no thread"
        return f'<span class="gb-email-open muted">{label}</span>'
    return f'<a class="gb-email-open" href="{link}" target="_blank" rel="noreferrer noopener">Review draft</a>'


def _targeted_action_link(item: dict[str, str]) -> str:
    link = _gmail_thread_link(item.get("thread_id", ""))
    if not link:
        link = item.get("draft_url") or ""
    if link:
        return f'<a class="gb-email-open" href="{escape(link)}" target="_blank" rel="noreferrer noopener">Review draft</a>'
    return '<span class="gb-email-open muted">Prepare draft</span>'


def _targeted_source_links(item: dict[str, str]) -> str:
    links = []
    for label, key in (("Website", "website_url"), ("LinkedIn", "linkedin_url"), ("Source", "source_url")):
        url = item.get(key) or ""
        if url:
            links.append(
                f'<a class="gb-email-source-link" href="{escape(url)}" target="_blank" rel="noreferrer noopener">{label}</a>'
            )
    if not links:
        return ""
    return f'<div class="gb-email-target-links">{" · ".join(links)}</div>'


def _render_rows(items: list[dict[str, str]], bucket: str, empty: str) -> str:
    if not items:
        return f'<div class="gb-email-empty">{escape(empty)}</div>'
    rows = ""
    for item in items:
        status_class = _priority_class(item, bucket)
        rows += dedent(
            f"""
            <div class="gb-email-deadline-row">
              <div>
                <div class="gb-email-person">{escape(item['person'])}</div>
                <div class="gb-email-context">{escape(item['event']) + ' · ' if item.get('event') else ''}{escape(item['subject'])}</div>
              </div>
              <div class="gb-email-due">{escape(item['due_text'])}</div>
              <div><span class="gb-email-priority {status_class}">{escape(_priority_label(item, bucket))}</span></div>
              <div>{_action_link(item)}</div>
            </div>
            """
        ).strip()
    return rows


def _render_targeted_rows(items: list[dict[str, str]], empty: str) -> str:
    if not items:
        return f'<div class="gb-email-empty">{escape(empty)}</div>'
    rows = ""
    for index, item in enumerate(items, start=1):
        rows += dedent(
            f"""
            <div class="gb-email-deadline-row gb-targeted-outreach-row">
              <div>
                <div class="gb-email-person">{index}. {escape(item['person'])}</div>
                <div class="gb-email-context">{escape(item['event']) + ' · ' if item.get('event') else ''}{escape(item['subject'])}</div>
                {_targeted_source_links(item)}
              </div>
              <div>{_targeted_action_link(item)}</div>
            </div>
            """
        ).strip()
    return rows


def _render_bucket(
    title: str,
    subtitle: str,
    items: list[dict[str, str]],
    bucket: str,
    empty: str,
    accent: str,
) -> str:
    return dedent(
        f"""
        <div class="gb-email-deadline-bucket {accent}">
          <div class="gb-email-deadline-head">
            <div>
              <div class="gb-email-deadline-title">{escape(title)}</div>
              <div class="gb-email-deadline-subtitle">{escape(subtitle)}</div>
            </div>
            <div class="gb-email-deadline-count">{len(items)}</div>
          </div>
          <div class="gb-email-deadline-body">
            {_render_rows(items, bucket, empty)}
          </div>
        </div>
        """
    ).strip()


def _render_targeted_bucket(items: list[dict[str, str]]) -> str:
    return dedent(
        f"""
        <div class="gb-email-deadline-bucket purple">
          <div class="gb-email-deadline-head">
            <div>
              <div class="gb-email-deadline-title">Today's Targeted Outreach</div>
              <div class="gb-email-deadline-subtitle">Three specific outreach items for Kay to review/send as time opens during the day.</div>
            </div>
            <div class="gb-email-deadline-count">{len(items)}</div>
          </div>
          <div class="gb-email-deadline-body">
            {_render_targeted_rows(items, "No targeted outreach currently surfaced.")}
          </div>
        </div>
        """
    ).strip()


def render() -> None:
    import streamlit as st

    email = load_email_orchestrator_status()
    body = _load_source_body(email.source_artifact)
    compact_input = _load_compact_input(email.input_artifact)
    evidence = _compact_email_evidence(compact_input)
    buckets = _bucketed_items(_draft_rows(body), evidence)

    st.markdown(
        _render_bucket(
            "24 Hr Thank Yous",
            "External meetings only. Verified by outbound Gmail unless another channel is marked complete.",
            buckets["thank"],
            "thank",
            "No 24-hour thank-yous currently surfaced.",
            "yellow",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        _render_bucket(
            "48 Hr Follow Ups",
            "Deal, intermediary, or relationship follow-ups that should not drift.",
            buckets["followup"],
            "followup",
            "No 48-hour follow-ups currently surfaced.",
            "blue",
        ),
        unsafe_allow_html=True,
    )
    st.markdown(
        _render_bucket(
            "EOW Follow Ups",
            "Conference and networking follow-ups, one row per person met.",
            buckets["eow"],
            "eow",
            "No end-of-week follow-ups currently surfaced.",
            "green",
        ),
        unsafe_allow_html=True,
    )
    targeted_outreach = _targeted_outreach_items(buckets["warm"])
    st.markdown(_render_targeted_bucket(targeted_outreach), unsafe_allow_html=True)

    st.markdown(
        '<div class="gb-page-note">Safety boundary: dashboard links to Gmail context only. It never sends, forwards, or schedule-sends email. Manual backlog source: brain/context/email-follow-through-backlog.json. Plumbing still needed: same-day reply feed and richer meeting/contact extraction.</div>',
        unsafe_allow_html=True,
    )

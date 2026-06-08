#!/usr/bin/env python3
"""Prepare compact Gmail context for scheduled email-intelligence runs.

The Gmail thread endpoint can return very large HTML payloads. This script
keeps those payloads out of Codex logs by capturing command output internally,
writing a bounded context artifact, and printing only a short summary.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ACCOUNT = "kay.s@greenwichandbarrow.com"
MAX_BODY_CHARS = 6000
MAX_SECTION_CHARS = 1800
MAX_CANDIDATE_THREADS = 18

DEAL_NEWSLETTER_SENDERS = [
    "helenguo",
    "smbdealhunter",
    "acquiringminds",
    "bizbuysell",
    "flippa",
    "empireflippers",
    "quietlight",
    "quiet light",
    "synergy",
    "viking",
    "generational equity",
    "sunbelt",
    "transworld",
]

DEAL_KEYWORDS = [
    "for sale",
    "business match",
    "asking price",
    "ebitda",
    "sde",
    "revenue",
    "cash flow",
    "new listing",
    "exclusive listing",
    "confidential information memorandum",
    "cim",
    "nda",
    "loi",
    "management report",
    "profit and loss",
    "balance sheet",
    "p&l",
]


def run_json(cmd: list[str]) -> Any:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stderr.strip()}"
        )
    try:
        return json.loads(proc.stdout or "{}")
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON from {' '.join(cmd)}: {exc}") from exc


def gmail_search(query: str, max_results: int) -> list[dict[str, Any]]:
    data = run_json(
        [
            "gog",
            "gmail",
            "search",
            "--account",
            ACCOUNT,
            "--gmail-no-send",
            query,
            "--json",
            "--max",
            str(max_results),
        ]
    )
    threads = data.get("threads", []) if isinstance(data, dict) else []
    return [t for t in threads if isinstance(t, dict)]


def gmail_drafts() -> Any:
    return run_json(
        [
            "gog",
            "gmail",
            "drafts",
            "list",
            "--account",
            ACCOUNT,
            "--gmail-no-send",
            "--json",
        ]
    )


def draft_details(drafts_data: Any) -> list[dict[str, Any]]:
    drafts = drafts_data.get("drafts", []) if isinstance(drafts_data, dict) else []
    details: list[dict[str, Any]] = []
    for draft in drafts:
        if not isinstance(draft, dict):
            continue
        thread_id = str(draft.get("threadId") or "")
        if not thread_id:
            continue
        try:
            full = thread_get(thread_id)
        except Exception as exc:
            details.append(
                {
                    "draft_id": draft.get("id"),
                    "thread_id": thread_id,
                    "message_id": draft.get("messageId"),
                    "error": str(exc),
                }
            )
            continue
        messages = full.get("messages", []) if isinstance(full, dict) else []
        if not messages:
            details.append(
                {
                    "draft_id": draft.get("id"),
                    "thread_id": thread_id,
                    "message_id": draft.get("messageId"),
                    "error": "thread contained no messages",
                }
            )
            continue
        latest = max(
            messages,
            key=lambda m: int(str(m.get("internalDate") or "0")),
        )
        internal_ms = int(str(latest.get("internalDate") or "0"))
        dt = (
            datetime.fromtimestamp(internal_ms / 1000, tz=timezone.utc).isoformat()
            if internal_ms
            else None
        )
        details.append(
            {
                "draft_id": draft.get("id"),
                "thread_id": thread_id,
                "message_id": draft.get("messageId"),
                "latest_message_id": latest.get("id"),
                "internal_date_utc": dt,
                "from": header_value(latest, "From"),
                "to": header_value(latest, "To"),
                "subject": header_value(latest, "Subject"),
                "snippet": latest.get("snippet", ""),
                "labels": latest.get("labelIds", []),
            }
        )
    return details


def thread_get(thread_id: str) -> dict[str, Any]:
    data = run_json(
        [
            "gog",
            "gmail",
            "thread",
            "get",
            thread_id,
            "--account",
            ACCOUNT,
            "--gmail-no-send",
            "--json",
        ]
    )
    return data.get("thread", {}) if isinstance(data, dict) else {}


def header_value(message: dict[str, Any], name: str) -> str:
    headers = message.get("payload", {}).get("headers", [])
    for header in headers:
        if str(header.get("name", "")).lower() == name.lower():
            return str(header.get("value", ""))
    return ""


def b64url_decode(data: str) -> str:
    if not data:
        return ""
    padded = data + "=" * (-len(data) % 4)
    try:
        raw = base64.urlsafe_b64decode(padded.encode())
    except Exception:
        return ""
    return raw.decode("utf-8", errors="replace")


def iter_parts(payload: dict[str, Any]):
    yield payload
    for part in payload.get("parts", []) or []:
        if isinstance(part, dict):
            yield from iter_parts(part)


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return normalize_ws(text)


def normalize_ws(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def message_text(message: dict[str, Any]) -> tuple[str, int]:
    payload = message.get("payload", {})
    plain_chunks: list[str] = []
    html_chunks: list[str] = []
    raw_bytes = 0
    for part in iter_parts(payload):
        body = part.get("body", {}) if isinstance(part, dict) else {}
        data = body.get("data", "")
        if not data:
            continue
        raw_bytes += int(body.get("size") or len(data))
        decoded = b64url_decode(data)
        mime = str(part.get("mimeType", "")).lower()
        if "text/plain" in mime:
            plain_chunks.append(decoded)
        elif "text/html" in mime:
            html_chunks.append(strip_html(decoded))
    text = "\n\n".join(plain_chunks or html_chunks)
    return normalize_ws(text), raw_bytes


def candidate_reason(thread: dict[str, Any]) -> str | None:
    haystack = " ".join(
        [
            str(thread.get("from", "")),
            str(thread.get("subject", "")),
            str(thread.get("snippet", "")),
        ]
    ).lower()
    if any(sender in haystack for sender in DEAL_NEWSLETTER_SENDERS):
        return "known_deal_or_marketplace_sender"
    if any(keyword in haystack for keyword in DEAL_KEYWORDS):
        return "deal_keyword_in_metadata"
    return None


def extract_relevant_windows(text: str) -> str:
    if len(text) <= MAX_BODY_CHARS:
        return text
    lower = text.lower()
    windows: list[str] = []
    for keyword in DEAL_KEYWORDS:
        start = lower.find(keyword)
        if start == -1:
            continue
        left = max(0, start - 500)
        right = min(len(text), start + MAX_SECTION_CHARS)
        windows.append(text[left:right])
        if len("\n\n---\n\n".join(windows)) >= MAX_BODY_CHARS:
            break
    if not windows:
        windows.append(text[:MAX_BODY_CHARS])
    return "\n\n---\n\n".join(windows)[:MAX_BODY_CHARS]


def compact_thread(thread: dict[str, Any]) -> dict[str, Any]:
    reason = candidate_reason(thread)
    item = {
        "id": thread.get("id"),
        "date": thread.get("date"),
        "from": thread.get("from"),
        "subject": thread.get("subject"),
        "labels": thread.get("labels", []),
        "message_count": thread.get("messageCount"),
        "snippet": thread.get("snippet", ""),
        "candidate_reason": reason,
    }
    return item


def enrich_candidate(thread: dict[str, Any]) -> dict[str, Any]:
    item = compact_thread(thread)
    thread_id = str(thread.get("id") or "")
    if not thread_id:
        return item
    full = thread_get(thread_id)
    messages = full.get("messages", []) if isinstance(full, dict) else []
    compact_messages = []
    total_raw_bytes = 0
    for message in messages:
        if not isinstance(message, dict):
            continue
        text, raw_bytes = message_text(message)
        total_raw_bytes += raw_bytes
        compact_messages.append(
            {
                "message_id": message.get("id"),
                "from": header_value(message, "From"),
                "to": header_value(message, "To"),
                "date": header_value(message, "Date"),
                "subject": header_value(message, "Subject"),
                "snippet": message.get("snippet", ""),
                "size_estimate": message.get("sizeEstimate"),
                "text_excerpt": extract_relevant_windows(text),
            }
        )
    item["raw_body_bytes_seen"] = total_raw_bytes
    item["messages"] = compact_messages
    return item


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--inbound-max", type=int, default=50)
    parser.add_argument("--outbound-max", type=int, default=50)
    parser.add_argument("--output")
    args = parser.parse_args()

    out_path = (
        Path(args.output)
        if args.output
        else REPO_ROOT / "brain" / "context" / f"email-intelligence-input-{args.date}.json"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    inbound = [compact_thread(t) for t in gmail_search("newer_than:2d label:INBOX", args.inbound_max)]
    outbound = [
        compact_thread(t)
        for t in gmail_search(f"from:{ACCOUNT} newer_than:2d", args.outbound_max)
    ]
    candidate_threads = [t for t in inbound if t.get("candidate_reason")][
        :MAX_CANDIDATE_THREADS
    ]
    enriched = [enrich_candidate(t) for t in candidate_threads]

    drafts_data = gmail_drafts()
    artifact = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "date": args.date,
        "account": ACCOUNT,
        "safety": {
            "gmail_no_send": True,
            "raw_thread_bodies_printed_to_stdout": False,
            "max_body_chars_per_candidate_message": MAX_BODY_CHARS,
            "max_candidate_threads_enriched": MAX_CANDIDATE_THREADS,
        },
        "queries": {
            "inbound": "newer_than:2d label:INBOX",
            "outbound": f"from:{ACCOUNT} newer_than:2d",
        },
        "inbound": inbound,
        "outbound": outbound,
        "drafts": drafts_data,
        "draft_details": draft_details(drafts_data),
        "candidate_threads": enriched,
    }
    out_path.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n")
    print(
        "EMAIL-INTEL-CONTEXT: "
        f"wrote {out_path} inbound={len(inbound)} outbound={len(outbound)} "
        f"candidates={len(enriched)} bytes={out_path.stat().st_size}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"EMAIL-INTEL-CONTEXT: FAILED {exc}", file=sys.stderr)
        raise

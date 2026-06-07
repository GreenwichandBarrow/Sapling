#!/usr/bin/env python3
"""Backfill saved Google Doc transcripts for processed post-call records.

This intentionally does not run the full post-call analyzer. It only:
1. reads processed post-call entries missing transcript_doc_url,
2. pulls the note through the 1Password-backed granola-api wrapper,
3. saves a transcript Google Doc in RESEARCH/MEETINGS,
4. updates processed.json with transcript_doc_url or transcript_failed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = REPO_ROOT / "brain/trackers/post-call-analyzer/processed.json"
MEETINGS_FOLDER_ID = "1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz"
ACCOUNT = "kay.s@greenwichandbarrow.com"


def run(args: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        args,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=180,
    )


def load_ledger() -> dict[str, Any]:
    if not LEDGER_PATH.exists():
        return {"processed": [], "last_updated": ""}
    return json.loads(LEDGER_PATH.read_text() or '{"processed": [], "last_updated": ""}')


def save_ledger(ledger: dict[str, Any]) -> None:
    ledger["last_updated"] = datetime.now(UTC).isoformat(timespec="seconds")
    LEDGER_PATH.write_text(json.dumps(ledger, indent=2) + "\n")


def slugish(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    return value[:90] if value else "Untitled Call"


def parse_date(note: dict[str, Any]) -> str:
    raw = note.get("created_at") or note.get("updated_at") or ""
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return datetime.utcnow().date().isoformat()


def attendee_label(attendee: Any) -> str:
    if isinstance(attendee, str):
        return attendee
    if not isinstance(attendee, dict):
        return str(attendee)
    for key in ("name", "email", "display_name"):
        if attendee.get(key):
            return str(attendee[key])
    return json.dumps(attendee, sort_keys=True)


def transcript_lines(transcript: Any) -> list[str]:
    if isinstance(transcript, str):
        return [transcript.strip()] if transcript.strip() else []
    if not isinstance(transcript, list):
        return []

    lines: list[str] = []
    for item in transcript:
        if isinstance(item, str):
            text = item.strip()
            if text:
                lines.append(text)
            continue
        if not isinstance(item, dict):
            continue
        speaker = (
            item.get("speaker")
            or item.get("speaker_name")
            or item.get("name")
            or item.get("person")
            or ""
        )
        text = (
            item.get("text")
            or item.get("content")
            or item.get("transcript")
            or item.get("utterance")
            or ""
        )
        text = str(text).strip()
        if not text:
            continue
        if speaker:
            lines.append(f"{speaker}: {text}")
        else:
            lines.append(text)
    return lines


def build_transcript_doc(note: dict[str, Any]) -> tuple[str, bool]:
    title = slugish(str(note.get("title") or "Untitled Call"))
    attendees = note.get("attendees") or []
    attendee_lines = [f"- {attendee_label(a)}" for a in attendees]
    transcript = transcript_lines(note.get("transcript"))
    transcript_failed = False
    if not transcript:
        for key in ("transcript_markdown", "transcript_plain", "notes_markdown", "notes_plain"):
            value = note.get(key)
            if isinstance(value, str) and value.strip():
                transcript = [value.strip()]
                break
    if not transcript:
        summary = note.get("summary_markdown") or note.get("summary_text") or ""
        if isinstance(summary, str) and summary.strip():
            transcript_failed = True
            transcript = [
                "Granola summary only; full transcript unavailable in response.",
                "",
                summary.strip(),
            ]
        else:
            transcript_failed = True
            transcript = ["Full transcript unavailable in Granola response."]

    parts = [
        f"# {title} - Granola Transcript",
        "",
        f"- Granola note ID: {note.get('id', '')}",
        f"- Created: {note.get('created_at', '')}",
        f"- Updated: {note.get('updated_at', '')}",
        f"- Granola source: {note.get('web_url', '')}",
        "",
        "## Attendees",
        *(attendee_lines or ["- Unknown"]),
        "",
    ]
    summary = note.get("summary_markdown") or note.get("summary_text")
    if isinstance(summary, str) and summary.strip():
        parts.extend(["## Granola Summary", summary.strip(), ""])
    parts.extend(["## Transcript", *transcript, ""])
    return "\n".join(parts), transcript_failed


def create_doc(title: str, body: str) -> str:
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(body)
        tmp_path = f.name
    try:
        proc = run(
            [
                "gog",
                "docs",
                "create",
                title,
                f"--parent={MEETINGS_FOLDER_ID}",
                f"--file={tmp_path}",
                f"--account={ACCOUNT}",
                "--json",
            ]
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
        data = json.loads(proc.stdout)
        doc_id = data.get("id") or data.get("file", {}).get("id")
        if not doc_id:
            raise RuntimeError(f"gog docs create returned no id: {proc.stdout[:300]}")
        return (
            data.get("webViewLink")
            or data.get("file", {}).get("webViewLink")
            or f"https://docs.google.com/document/d/{doc_id}/edit"
        )
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def get_note(note_id: str) -> dict[str, Any]:
    proc = run(["granola-api", "get-note", note_id])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
    return json.loads(proc.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ledger = load_ledger()
    items = ledger.get("processed", [])
    if not isinstance(items, list):
        raise SystemExit("processed.json has unexpected shape")

    candidates = [
        item
        for item in items
        if isinstance(item, dict) and item.get("id") and not item.get("transcript_doc_url")
    ]
    selected = candidates[-args.limit :] if args.limit > 0 else candidates
    print(f"candidates={len(candidates)} selected={len(selected)} dry_run={args.dry_run}")

    changed = False
    for item in selected:
        note_id = item["id"]
        print(f"backfill {note_id}...", flush=True)
        try:
            note = get_note(note_id)
            body, transcript_failed = build_transcript_doc(note)
            title = f"{parse_date(note)} - {slugish(str(note.get('title') or note_id))} - Granola Transcript"
            if args.dry_run:
                print(f"  would create: {title} ({len(body)} chars)")
                continue
            url = create_doc(title, body)
            item["transcript_doc_url"] = url
            item["transcript_backfilled_at"] = datetime.now(UTC).isoformat(timespec="seconds")
            if transcript_failed:
                item["transcript_failed"] = True
            else:
                item.pop("transcript_failed", None)
            print(f"  created {url}")
            changed = True
        except Exception as exc:
            item["transcript_failed"] = True
            item["transcript_backfill_error"] = str(exc)[:500]
            item["transcript_backfilled_at"] = datetime.now(UTC).isoformat(timespec="seconds")
            print(f"  FAILED {exc}", file=sys.stderr)
            changed = True

    if changed and not args.dry_run:
        save_ledger(ledger)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

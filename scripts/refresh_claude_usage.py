#!/usr/bin/env python3
"""Refresh Claude Code usage snapshot for the dashboard.

Reads only local Claude JSONL metadata fields: timestamp, model, request id,
and usage counters. It does not persist prompt, response, or tool content.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
import json

CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
OUT_PATH = Path(__file__).resolve().parent.parent / "brain" / "context" / "claude-usage-snapshot.json"

DASHBOARD_TZ = ZoneInfo("America/New_York")

TOKEN_FIELDS = (
    "input_tokens",
    "output_tokens",
    "cache_read_input_tokens",
    "cache_creation_input_tokens",
)


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        ts = datetime.fromisoformat(value)
    except ValueError:
        return None
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return ts.astimezone(DASHBOARD_TZ)


def empty_totals() -> dict[str, int]:
    return {field: 0 for field in TOKEN_FIELDS} | {"total_tokens": 0}


def add_usage(target: dict[str, int], usage: dict) -> None:
    total = 0
    for field in TOKEN_FIELDS:
        value = usage.get(field, 0)
        if isinstance(value, int):
            target[field] += value
            total += value
    target["total_tokens"] += total


def main() -> int:
    now = datetime.now(DASHBOARD_TZ)
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    month = empty_totals()
    today = empty_totals()
    model_tokens: dict[str, int] = defaultdict(int)
    model_messages: Counter[str] = Counter()
    seen: set[str] = set()
    scanned_files = 0
    messages_with_usage = 0

    if CLAUDE_PROJECTS_DIR.exists():
        for path in CLAUDE_PROJECTS_DIR.rglob("*.jsonl"):
            scanned_files += 1
            try:
                lines = path.open(errors="ignore")
            except OSError:
                continue
            with lines:
                for line_no, line in enumerate(lines, 1):
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    msg = row.get("message") if isinstance(row, dict) else None
                    usage = msg.get("usage") if isinstance(msg, dict) else None
                    if not isinstance(usage, dict):
                        continue
                    ts = parse_ts(row.get("timestamp"))
                    if ts is None or ts < month_start:
                        continue
                    identity = row.get("requestId") or row.get("uuid") or f"{path}:{line_no}"
                    if identity in seen:
                        continue
                    seen.add(identity)
                    messages_with_usage += 1

                    before = month["total_tokens"]
                    add_usage(month, usage)
                    added = month["total_tokens"] - before
                    model = msg.get("model") or "unknown"
                    model_tokens[model] += added
                    model_messages[model] += 1
                    if ts >= today_start:
                        add_usage(today, usage)

    snapshot = {
        "fetched_at": now.isoformat(),
        "source": "local_claude_transcript_usage_metadata",
        "period_start": month_start.isoformat(),
        "period_end": now.isoformat(),
        "scanned_files": scanned_files,
        "messages_with_usage": messages_with_usage,
        "month": month,
        "today": today,
        "models": [
            {"model": model, "tokens": tokens, "messages": model_messages[model]}
            for model, tokens in sorted(model_tokens.items(), key=lambda item: item[1], reverse=True)
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUT_PATH}")
    print(f"month_total_tokens={month['total_tokens']} today_total_tokens={today['total_tokens']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

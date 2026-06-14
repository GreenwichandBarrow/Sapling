#!/usr/bin/env python3
"""Refresh Codex/OpenAI usage snapshot for the dashboard.

Reads local Codex session usage counters only. It aggregates the latest
cumulative token summary per session file and does not persist messages,
prompts, tool outputs, or auth data.
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
import json

CODEX_SESSIONS_DIR = Path.home() / ".codex" / "sessions"
OUT_PATH = Path(__file__).resolve().parent.parent / "brain" / "context" / "codex-usage-snapshot.json"

DASHBOARD_TZ = ZoneInfo("America/New_York")

TOKEN_FIELDS = (
    "input_tokens",
    "cached_input_tokens",
    "output_tokens",
    "reasoning_output_tokens",
    "total_tokens",
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
    return {field: 0 for field in TOKEN_FIELDS}


def add_totals(target: dict[str, int], usage: dict) -> None:
    for field in TOKEN_FIELDS:
        value = usage.get(field, 0)
        if isinstance(value, int):
            target[field] += value
    if not target.get("total_tokens"):
        target["total_tokens"] = (
            target.get("input_tokens", 0)
            + target.get("cached_input_tokens", 0)
            + target.get("output_tokens", 0)
            + target.get("reasoning_output_tokens", 0)
        )


def latest_usage_for_file(path: Path) -> tuple[datetime | None, dict[str, int] | None, str | None]:
    latest_ts: datetime | None = None
    latest_usage: dict[str, int] | None = None
    latest_model: str | None = None
    try:
        lines = path.open(errors="ignore")
    except OSError:
        return None, None, None
    with lines:
        for line in lines:
            if "total_token_usage" not in line and "last_token_usage" not in line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            payload = row.get("payload") if isinstance(row, dict) else None
            info = payload.get("info") if isinstance(payload, dict) else None
            if not isinstance(info, dict):
                continue
            usage = info.get("total_token_usage")
            if not isinstance(usage, dict):
                continue
            ts = parse_ts(row.get("timestamp")) or latest_ts
            clean = {field: usage.get(field, 0) for field in TOKEN_FIELDS if isinstance(usage.get(field, 0), int)}
            if "total_tokens" not in clean:
                clean["total_tokens"] = sum(clean.values())
            latest_ts = ts
            latest_usage = clean
            latest_model = info.get("model") or latest_model
    return latest_ts, latest_usage, latest_model


def main() -> int:
    now = datetime.now(DASHBOARD_TZ)
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

    month = empty_totals()
    today = empty_totals()
    model_tokens: dict[str, int] = defaultdict(int)
    scanned_files = 0
    sessions_with_usage = 0

    if CODEX_SESSIONS_DIR.exists():
        for path in CODEX_SESSIONS_DIR.rglob("*.jsonl"):
            # Directory layout is YYYY/MM/DD; skip obvious older years/months early.
            scanned_files += 1
            ts, usage, model = latest_usage_for_file(path)
            if ts is None or usage is None or ts < month_start:
                continue
            sessions_with_usage += 1
            add_totals(month, usage)
            model_tokens[model or "unknown"] += usage.get("total_tokens", 0)
            if ts >= today_start:
                add_totals(today, usage)

    snapshot = {
        "fetched_at": now.isoformat(),
        "source": "local_codex_session_usage_metadata",
        "period_start": month_start.isoformat(),
        "period_end": now.isoformat(),
        "scanned_files": scanned_files,
        "sessions_with_usage": sessions_with_usage,
        "month": month,
        "today": today,
        "models": [
            {"model": model, "tokens": tokens}
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

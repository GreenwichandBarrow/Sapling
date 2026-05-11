---
name: Granola MCP shape — start time only, no ended_at
description: Granola's MCP (mcp.granola.ai) exposes start time only as `date` field. No ended_at, no duration. Filters keying on call-completion must use started_at + buffer.
type: project
originSessionId: 245b9334-d58f-45df-8978-a6d8673c0ca7
---
Granola's MCP (`mcp.granola.ai/mcp`) exposes meeting start time only via its `date` field. There is no `ended_at`, `end_at`, `duration_minutes`, or any "this meeting concluded" field on either `list_meetings` or `get_meetings`.

**Why:** Discovered 2026-05-08 commissioning Phase 4 of post-call-analyzer. The detector script `scripts/post_call_analyzer_mcp_poll.py` originally filtered on `ended_at`; subprocess Claude correctly returned `ended_at: null` for every meeting because Granola has no such field, so `is_recent()` always returned False and the queue stayed empty silently. No log, no error, no signal — just silent no-op. Kay's call cadence: 30-min and 1-hour calls, rarely longer.

**How to apply:**
- Any new skill, script, or detector that needs to know "did this Granola call end" must filter on `started_at` (= Granola's `date` field) plus a buffer. Default buffer: 90 minutes after start = call has reliably ended (covers 1-hour call + 30-min runover).
- Don't ask the subprocess Claude to fabricate `ended_at` — it'll either return null or hallucinate. Drop the field from prompt schemas entirely.
- If you need a tighter "actually ended" signal (vs. "probably ended"), call `mcp__granola__get_meetings([id])` and require non-empty `summary` field — Granola only writes the summary post-call. Costs 1 MCP call per candidate.
- Phase 4 detector window: `cutoff_old <= started_at <= now - 90min`.

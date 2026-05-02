---
schema_version: 1.1.0
date: 2026-05-01
type: trace
title: "Never write to xlsx while Excel has it open — lsof check is mandatory"
tags: ["date/2026-05-01", "trace", "topic/excel-tooling", "topic/skill-guardrails", "domain/technical"]
importance: high
target: skill:task-tracker-manager
---

# xlsx writes require lsof file-lock check

## Context

The `task-tracker-manager` skill writes to a single xlsx file in Drive. Kay frequently has the file open in Excel while working with Claude — Excel autosaves to Drive on its own cadence. If openpyxl writes the file simultaneously, one of two failure modes occurs:

1. **Claude clobbers Excel:** Excel's autosave commits AFTER Claude's write, overwriting Claude's changes silently. From Kay's perspective, the change "didn't happen."
2. **Excel clobbers Claude:** Claude's write commits, then Excel autosaves the in-memory state, overwriting Claude's changes silently. Same observable failure.
3. **Drive sync conflict:** Both writers commit close in time, Drive creates a `(conflict)` copy, file integrity ambiguous.

All three modes are silent — no exception, no error log. The only signal Kay would see is "the change Claude said happened isn't reflected."

## Decisions

### Pre-write file-lock guardrail

**AI proposed:** Either (A) trust Claude not to write while Excel is open by checking conversationally, (B) hard guardrail — every write verb runs `lsof <file>` and refuses to open the workbook if Microsoft Excel has a handle.

**Chosen:** **Path B** — `assert_writable(LIVE)` in `scripts/task_tracker.py` runs `lsof` before every verb that mutates the file. If "Microsoft" or "Excel" appears in the lsof output, exit with `task-tracker-manager: refused — Excel has {path!r} open. Close it first (Cmd+Q).` Skill never writes blind.

**Reasoning:** Conversational checking fails at scale. Claude can't reliably remember "Kay said she'd close Excel" 30 minutes later. A code-level guardrail is cheap (single `subprocess.run(["lsof", path])`) and catches all paths into the verbs — direct invocation, scheduled run, future Chief-of-Staff orchestration.

**Pattern:** Mandatory pre-write integrity checks for any file with concurrent-writer risk (Excel autosave, Drive sync, Google Docs collaborators).

## Why this trace matters for future agents

The xlsx file Kay touches is co-edited with Excel autosave + Google Drive sync. Future agents adding new verbs to `task-tracker-manager` (or building adjacent skills that touch xlsx) MUST preserve the lsof guardrail. Removing it because "it's annoying for testing" would re-open the silent-clobber failure mode.

The same pattern applies to any future Claude-Excel integrations. Don't trust the user to close the file. Don't trust your earlier conversation. Check at write-time, every time.

## Key insight

**Co-edited files require code-level concurrency control, not conversational coordination.** Claude is bad at remembering "user said they'd close it" across long sessions; user is bad at remembering they said it. The lsof check is the source of truth.

## How a future agent should apply

- All new mutation verbs in `task_tracker.py` MUST call `assert_writable(LIVE)` before opening the workbook.
- If extending to new xlsx files (e.g., budget tracker, dashboard files), copy the same pattern.
- Never bypass the check with `--force` flags or environment variables; if Excel has the file open, surface to Kay and stop.
- Backups (separate from lsof check) are the second layer — if a write does corrupt despite the guardrail, the timestamped backup in `~/My Drive/STRATEGIC PLANNING/{file}.bak.{ts}.xlsx` is the recovery path.

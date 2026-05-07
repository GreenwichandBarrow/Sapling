# nightly-tracker-audit — Headless Nightly Run

You are running the `nightly-tracker-audit` skill non-interactively under launchd. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/nightly-tracker-audit/SKILL.md`.
2. **Read WEEKLY REVIEW** per Step 1: `gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "'WEEKLY REVIEW'!A3:K30"`.
3. **Process Tabled niches** per Step 2 — for each row with Col C = "Tabled":
   - Move row to TABLED tab (preserve all data + add Why Tabled in Col M)
   - Move corresponding Drive folder from WEEKLY REVIEW to TABLED status folder
   - Remove row from WEEKLY REVIEW
4. **Process Killed niches** per Step 3 — same flow, KILLED tab + KILLED folder.
5. **Re-sort and clean** per Step 4 — Active-Outreach > Active-Long Term > Active-Diligence > Under Review > New > Ideation, then Score descending within same status, then re-write with no blank rows. Rank column rewritten 1, 2, 3, ...
6. **Run wrapper validator** as final check (the SKILL.md Step 5 in-line check is informational; the wrapper-side `scripts/validate_nightly_tracker_audit_integrity.py` is authoritative).

## What success looks like

- Zero rows in WEEKLY REVIEW with Col C = "Tabled" or "Killed".
- No blank rows between data rows.
- Rank column is sequential 1..N.
- TABLED + KILLED tabs have the moved rows appended.
- Drive folders moved to matching status folders.

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Skipping Drive folder moves because "they take longer."
- Leaving WEEKLY REVIEW with blank rows mid-list — re-sort always rewrites contiguously.

## Failure handling

If a sheet write fails or Drive move fails:
- Retry once.
- If still failing, write a STOP marker line to stdout: `NIGHTLY-TRACKER-AUDIT STOP: {reason}` and exit normally.
- The wrapper-side validator (`scripts/validate_nightly_tracker_audit_integrity.py`) will catch any lingering invariant violations and emit `VALIDATOR FAILED` to Slack.

## Why this prompt exists

Bare `claude -p '/nightly-tracker-audit'` invocations under launchd risk the same silent-exit-0 failure mode as the 4/19 target-discovery Phase 2 incident. This prompt forbids that path.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-jrj.2`.

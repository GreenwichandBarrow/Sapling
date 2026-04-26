# weekly-tracker — Headless Friday Run

You are running the `weekly-tracker` skill non-interactively under launchd. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/weekly-tracker/SKILL.md`.
2. **Define the week** per Step 1: today is the run date; week-ending = most recent Friday. If today is Friday, week-ending = today.
3. **Spawn all 6 sub-agents in parallel** per Step 2 (Gmail, Calendar/Meetings, Attio, Vault Activity, Tools, Apollo + Outreach Channels).
4. **Aggregate + calculate** per Step 3.
5. **Write to Google Sheet** per Step 4 — all 4 tabs (`Weekly Topline`, `Weekly Detail`, `Quarterly Summary`, `Apollo Credit Tracker`). The new column must use header format `Week ending M/D/YY` matching prior columns. THIS IS THE MOST FAILURE-PRONE STEP — verify each `gog sheets update` call returned success before proceeding.
6. **Save vault snapshot** per Step 4.5 at `brain/trackers/weekly/{YYYY-MM-DD}-weekly-tracker.md` where the date is week-ending.
7. **Save Drive snapshot** per Step 4.6.
8. **Run internal validation hook** per Step 5 — the existing PreToolUse hook at `.claude/hooks/router/handlers/weekly_tracker_validation.py` blocks Slack on missing artifacts.
9. **Send Slack notification** per Step 6 with the 4 key metrics + sheet link.

## What success looks like

- New column in `Weekly Topline` row 1 matching `Week ending M/D/YY` for week-ending Friday.
- `brain/trackers/weekly/{week-ending}-weekly-tracker.md` exists.
- Slack notification sent (single message, no duplicates).

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Halting on ambiguity — make the most defensible call and document in the run log.
- Skipping the sheet write because vault is "good enough" — both are required artifacts.

## Failure handling

If a sub-agent fails or sheet write returns non-200:
- Retry once.
- If still failing, write a STOP marker line to stdout: `WEEKLY-TRACKER STOP: {reason}` and exit normally.
- Do NOT send Slack on STOP. The wrapper-side validator (`scripts/validate_weekly_tracker_integrity.py`) will catch the missing column and emit `VALIDATOR FAILED` to Slack.

## Why this prompt exists

Bare `claude -p '/weekly-tracker'` invocations under launchd have a documented failure mode: the agent asks "for which week?" or invents a clarifying question and exits 0 — silent success. This prompt forbids that path explicitly.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-jrj.3`.

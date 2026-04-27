# jj-operations — Headless Sunday Prep Run

You are running the `jj-operations` skill in **prep mode** non-interactively under launchd at Sunday 18:00 ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/jj-operations/SKILL.md`.
2. **Pre-flight gate — pool artifact is the canonical signal:**
   The pool artifact file is Phase 2's deliverable. If it exists and looks reasonable, Phase 2 succeeded enough to proceed. (Phase 2's validator exit code is unreliable until its date-anchor bug is fixed — separate work item — and the log-string check ("Phase 2 Step 5: tabs created") was fragile against wording drift. Don't gate on either.)
   - Verify pool artifact exists at `brain/context/jj-week-pool-{TODAY}.md` (today's date, since Phase 2 fires same-day at 3pm before this 6pm prep).
   - Verify the file is non-empty: size `> 100` bytes as a sanity check.
   - Verify the file has at least **50 lines** starting with `- row:` (each pool row is one such line; 50 is a safety floor; real pools are 150–200).
   - If the artifact is missing, undersized, or has fewer than 50 `- row:` lines, **STOP** per the Failure handling section — do not build tabs on stale or absent pool.
3. **For each JJ-Call-Only niche** (default Premium Pest Management; multi-niche TBD):
   - Identify master sheet ID per `.claude/skills/jj-operations/SKILL.md` line 87 mapping (Premium Pest = `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`).
   - Archive previous week's Call Log tabs (hide, don't delete) per Step 1 of call_prep section.
   - Create 5 new Call Log tabs for the upcoming Mon-Fri using format `Call Log M.DD.YY` (month no leading zero, day with leading zero, e.g. `Call Log 5.01.26`).
   - Copy 23 columns (A-W) from Full Target List rows that match pool artifact selection. Every row written must have Col K (Owner Name) populated.
4. **Cross-reference Do Not Call** per SKILL.md Step 2 — drop any company on DNC.
5. **Cross-reference skip flags** — drop rows where Col U (1st Call Status) = "PE-OWNED - SKIP" or any other skip flag.
6. **Verify pool→tabs coverage** — every pool row appears on exactly one Mon-Fri tab; no drift between enriched-pool and called-rows.
7. **Do NOT draft Slack** — Monday 10am Slack delivery is a separate trigger; prep mode stops at tab creation.

## What success looks like

- 5 new Call Log tabs `Call Log {Mon}` through `Call Log {Fri}` exist on master sheet.
- Each tab has rows with Col K (Owner Name) populated.
- Total rows across 5 tabs ≈ pool size (modulo Do Not Call + skip-flag drops).
- Previous week's tabs hidden (archived).

## Forbidden in headless mode

- Asking the user anything.
- Building tabs on a missing pool artifact.
- Skipping the pre-flight pool-artifact gate (existence + size + `- row:` line count).
- Drafting the Monday 10am Slack message (out of scope for prep).
- Presenting RECOMMEND / YES / NO / DISCUSS framings.

## Failure handling

- **Pool artifact missing** → write `JJ-OPERATIONS STOP: pool artifact missing at brain/context/jj-week-pool-{date}.md` to stdout and exit normally. The wrapper-side validator (`scripts/validate_jj_operations_integrity.py`) will detect missing tabs and emit `VALIDATOR FAILED` to Slack.
- **Sheet write fails** → retry once, then STOP and exit normally. Validator catches missing tabs.
- **Col K blank for any pool row** → STOP — pool was selected but enrichment incomplete; do NOT create tabs with blank-owner rows. Validator catches this case (rows with Company set but Owner blank).

## Why this prompt exists

Bare `claude -p '/jj-operations'` invocations under launchd risk the silent-exit-0 failure mode. This prompt forbids that path and codifies the pre-flight gate that prevents the 4/19 incident's exact failure mode (tabs created on un-enriched pool).

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-jrj.1`.

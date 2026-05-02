---
name: tracker-manager
description: Claude-owned operational-sheet management. Auto-executes routine tracker updates (status moves, rank re-sorts, target-list hygiene, DealsX category edits driven by stated strategic decisions) and surfaces material changes for Kay's approval before writing. Governs Industry Research Tracker, DealsX Industry Verticals, target lists, and related sheets. Use when Kay authorizes a tracker update in conversation, when niche-intelligence or scorecard output requires a sheet sync, or when nightly-tracker-audit-style cleanup is needed ad hoc.
---

# Tracker Manager

Standing owner of mechanical sheet maintenance across the G&B operational stack. Codifies the Claude-Kay contract defined in `memory/feedback_tracker_manager_scope.md`.

## When to invoke

- Kay states a strategic decision that implies tracker changes ("hand this niche to Sam," "table that one," "move to Active - Long Term")
- niche-intelligence skill produces a scorecard or one-pager that needs tracker sync
- Post-call context implies a status change (e.g., owner passed, LOI expired, deal advanced)
- End-of-day cleanup beyond what nightly-tracker-audit handles
- New conference / broker / investor-sourced niche needs routing to IDEATION or WEEKLY REVIEW
- Detected a data-hygiene violation during another workflow (PE-owned target on sheet, California target on JJ-Call-Only, etc.)

## Sheets in scope

| Sheet | Sheet ID | Claude owns? |
|---|---|---|
| Industry Research Tracker | `1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins` | Yes — WEEKLY REVIEW, TABLED, KILLED, IDEATION tabs |
| DealsX Industry Verticals complete | `1wuQy_zAweG7V_gctM2LPlTXv87YGLcBx-q1vumyv39A` | Yes — category adds / retires / edits |
| Target lists (per-niche sheets) | Various per niche folder | Yes — Col O approve/pass, Identified-in-Attio flags, DNC enforcement |
| G&B Weekly Activity Tracker | `1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE` | No — owned by weekly-tracker skill |
| Master Call List (JJ's sheet) | (various tabs) | Partial — JJ owns; Claude only writes via jj-operations skill workflow |

## Decision matrix — auto-execute vs surface-for-approval

**AUTO-EXECUTE** (proceed without confirmation; always snapshot + validate):

- Status-triggered moves (Tabled/Killed → their tabs overnight; rule-based and deterministic)
- Rank re-sorts (Active - Outreach → Active - Long Term → Under Review → New)
- Niche adds to WEEKLY REVIEW after niche-intelligence completes (scored, folder created, PPTX + XLSX in Drive)
- Score/notes updates when scorecard output changes
- Drive folder moves tied to status changes (TABLED folder ↔ WEEKLY REVIEW folder)
- DealsX category edits that directly implement Kay's stated strategic decisions in the same conversation (e.g., "trim SaaS to one vertical" → retire 3 rows + update 1 row)
- Target list hygiene: Col O approve → Identified in Attio / move to Passed tab; DNC enforcement; no-California rule on JJ-Call-Only; no-PE-owned rule on any outreach sheet
- Art Storage DNC carve-out enforcement (Acumen, Uovo, Hangman stay off any target list that uses Art Storage as the source niche)

**SURFACE FOR APPROVAL** (show preview, wait for YES/NO/REVISE):

- New DealsX category addition with full content (draft the row, show What They Do / Industries / Keywords / Example Companies preview, write only after YES)
- Retiring / deleting rows Sam is actively working (even if Kay has signaled intent, confirm the specific rows)
- Score changes ≥0.30 on any WEEKLY REVIEW row
- Moving a niche Active-Outreach → Tabled (material change even if conversation implies it)
- Any change that affects ≥5 WEEKLY REVIEW rows at once (portfolio-level shift)
- Schema / column / tab structural changes to any sheet
- Adding a new niche folder in Drive with one-pager + scorecard (material artifact-creation)

## Hard guardrails — always

1. **Snapshot before write.** Read the target range, save JSON to `/tmp/{sheet}_pre_{timestamp}.json`. Local rollback source if the write goes wrong.
2. **Validate inputs before gog call.** Never call `gog sheets update` with an empty tab_name, row number, or range spec. Assert each is non-empty before invocation.
3. **Post-write verification.** After every write, read back the changed range and diff against expected. Flag any mismatch.
4. **Named ranges over A1 refs.** Prefer `"WEEKLY REVIEW!B17"` over absolute positional writes where a named range exists.
5. **Bash for index loops.** Never use zsh for sheet-writing loops (history of zsh quoting causing empty-variable clobbers).
6. **Trace log every material change** to `brain/traces/{date}-tracker-manager-{slug}.md` with:
   - What changed (range, before, after)
   - Why (citation to conversation or skill trigger)
   - Rollback (exact `gog sheets update` command to restore pre-state)

## Out of scope — never auto-execute

- Attio CRM record-level changes (per `feedback_never_batch_changes_without_review`)
- Google Doc bodies (engagement letter, meeting briefs, call preps, deliverables)
- Financial-model cells (CFO territory — any xlsx with numbers for investors)
- Weekly Detail tab Column B / description (per `feedback_weekly_detail_description_col_b`)
- External message sends (Slack, email, Superhuman, Attio notes) — always draft-for-review per the relevant skill
- Kay-named people-records in Attio entities
- Any operation during Superhuman/GOG/Attio outage (suppress writes, per `feedback_superhuman_down_suppress_drafts` and similar)

## Standard workflow — status move example

When Kay says "move X to Active - Long Term":

1. Read current WEEKLY REVIEW tab, locate X by niche name (Col B)
2. Snapshot the row to `/tmp/wr_pre_{timestamp}.json`
3. Update Col C to "Active - Long Term" (Col D channel preserved)
4. Read back, confirm
5. Append trace log to `brain/traces/`
6. Brief Kay: "Done — {niche} moved to Active - Long Term, row {n}, validated."

## Standard workflow — DealsX category edit example

When Kay stipulates a broad change like "retire these SaaS categories":

1. Read DealsX sheet, locate target rows by Niche column
2. Snapshot range
3. Execute the sheet ops (clear / update / append) per Kay's stated instructions
4. Post-write: read back + diff
5. Brief Kay with what's now in the sheet
6. If any row affects ≥5 sub-niches on WEEKLY REVIEW, surface those downstream effects for Kay's approval before propagating to WEEKLY REVIEW

## Standard workflow — nightly sweep (when manually invoked)

1. Read WEEKLY REVIEW, TABLED, KILLED tabs
2. Find rows where Status just changed (from prior snapshot)
3. Execute moves per decision matrix (Tabled → TABLED tab, Killed → KILLED tab, folder moves in Drive)
4. Re-sort WEEKLY REVIEW by Active - Outreach → Active - Long Term → Under Review → New
5. Verify each target list sheet per-niche has correct DNC flags, no-California, no-PE-owned rows
6. Write brief summary of moves to `brain/outputs/{date}-tracker-manager-sweep.md`

## References

- Rule source: `memory/feedback_tracker_manager_scope.md`
- Related skills: `nightly-tracker-audit` (overnight automated sweep), `niche-intelligence` (creates the scorecards and one-pagers that trigger adds), `target-discovery` (populates target-list sheets on Active - Outreach status trigger)
- Safety patterns: `memory/feedback_subagent_sheet_write_safety.md`, `memory/feedback_never_batch_changes_without_review.md`
- Column conventions: `.claude/skills/niche-intelligence/references/tracker-access.md`

## Evolution

This skill is expected to grow. When Claude surfaces-for-approval on something repetitive with a consistent Kay-YES pattern, graduate it to auto-execute (update this SKILL.md and the memory rule). When an auto-action causes a problem, demote it to surface-for-approval. Revisit scope at each quarterly investor-update cycle.

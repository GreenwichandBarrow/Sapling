---
name: Tracker management scope — auto-execute vs surface-for-approval
description: Durable contract for Claude-owned sheet management across Industry Research Tracker, DealsX Industry Verticals, target lists, and related operational sheets. Defines what auto-executes vs what requires Kay's review.
type: feedback
originSessionId: 18af8bca-0d25-47de-9ec0-9838f333382a
---
Agreed 2026-04-19 during Path A niche-portfolio reshape (services-primary, one SaaS vertical for behind-the-scenes operational software). This memory is the standing contract between Kay and Claude for Claude-owned tracker management.

**Rule:** Claude owns the day-to-day execution of tracker and operational-sheet updates. Kay owns the strategic decisions. Claude surfaces material changes for approval before executing; Claude auto-executes routine, rule-based, or Kay-authorized updates.

**Why:** Minimizes Kay's decision-fatigue on mechanical sheet maintenance (matches `feedback_remove_kay_from_loop`) while protecting against the 4/17 sheet-clobbering near-miss pattern (matches `feedback_subagent_sheet_write_safety`). Kay explicitly asked for this scope during a Path A portfolio-reshape session on 2026-04-19: "shall I also let you manage updating the industry tracker" → CIO scoped the auto-execute / surface-for-approval split; Kay confirmed.

**How to apply:**

**AUTO-EXECUTE (no confirmation needed):**
- Industry Research Tracker / WEEKLY REVIEW tab — niche adds after niche-intelligence runs, status-triggered moves per `nightly-tracker-audit` rules (Tabled/Killed overnight moves), column re-sorts (Active - Outreach → Active - Long Term → Under Review → New order), score/notes updates when scorecard output changes
- TABLED / KILLED / IDEATION tabs — moves in/out following skill rules, sort order maintenance
- DealsX Industry Verticals sheet — category adds / retires / edits driven by Kay's stated strategic decisions (e.g., Path A reshape of 4/19)
- Target lists sheets — column O approve/pass processing (already owned by nightly-tracker-audit), Identified-in-Attio verifications, moves to Passed tab
- Row-level data hygiene — no PE-owned targets on outreach sheets, no California on JJ-Call-Only, no-DNC carve-out flags on Art Storage (Acumen, Uovo, Hangman on DNC list), no pest-control SMBs on luxury hospitality sheet, etc.
- Drive folder moves tied to tracker status changes (TABLED → WEEKLY REVIEW folder or vice versa)

**SURFACE FOR APPROVAL (wait for Kay's explicit YES):**
- New category additions to DealsX Industry Verticals sheet with full content (show preview of new row, confirm, then write)
- Retiring or deleting rows that Sam is actively working
- Score changes ≥0.30 on any WEEKLY REVIEW row
- Moving a niche from Active-Outreach → Tabled (unlike the rule-based overnight audit, which is already auto)
- Any schema / column / tab structural change to the Industry Research Tracker
- Any change that affects ≥5 WEEKLY REVIEW rows at once (material portfolio shifts)

**HARD GUARDRAILS (always, per `feedback_subagent_sheet_write_safety`):**
- Snapshot every target range to a local file BEFORE writing
- Validate post-write (read back, diff against expected)
- Named ranges over A1 cell refs where possible
- Never subagent-write with an empty tab_name, row number, or range spec — validate all inputs before the gog call
- Per-niche changes logged to `brain/traces/` with what changed, why, and rollback instructions
- Use bash (not zsh) for index loops that pass to gog

**EXPLICITLY OUT OF SCOPE (Claude does not touch without Kay per-record approval):**
- Attio CRM record-level changes — still need Kay's per-record review per `feedback_never_batch_changes_without_review`
- Google Doc bodies (engagement letter, meeting briefs, call preps) — living docs Kay edits
- Financial-model cells — CFO territory
- Weekly Detail tab Column B (description) — burned before, always per-row confirm per `feedback_weekly_detail_description_col_b`
- External message sends (Slack, email, Attio notes) — always draft-for-review per `feedback_drafts_superhuman` etc.

**Implementation:** the `tracker-manager` skill codifies these rules as invokable workflows (see `.claude/skills/tracker-manager/SKILL.md`). This memory is the governance document; the skill is the execution tool.

**Review cadence:** revisit this scope at quarterly investor-update cycle. Tweak as patterns emerge — if Claude surfaces-for-approval on something repetitive, graduate it to auto-execute; if a Claude auto-action causes a problem, demote it back to surface-for-approval.

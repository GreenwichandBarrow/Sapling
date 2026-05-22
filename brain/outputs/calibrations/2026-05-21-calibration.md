---
schema_version: 1.0.0
date: 2026-05-21
type: output
output_type: calibration
status: applied
title: "Calibration — 2026-05-21 (Thursday meta — 38 traces, 2026-05-15 → 2026-05-20)"
tags: ["date/2026-05-21", "output", "output/calibration", "status/applied", "topic/calibration"]
---

# Calibration Report — 2026-05-21 (Thursday Meta-Calibration)

**Traces analyzed:** 38 (May 15-20)
**Raw proposals:** 21 (architecture-strategist 8 · simplicity-advocate 8 · pattern-recognizer 5)
**After dedupe/merge:** 16 — 4 critical, 7 high, 4 medium, 1 watchlist
**Agents:** architecture-strategist · simplicity-advocate · pattern-recognizer (coordinator synthesized)
**Scope decision (operator-dismissed approval question, calibrated judgment):** apply small/reversible items now; queue heavy refactors (women-led gate, inbound classification, Superhuman sweep, weekly-tracker retirement) for a focused next-session sprint.

## Cross-cutting observation

Three independent lenses converged on the SAME meta-pattern: **the system over-adds memory files and under-wires execution.** Doctrine lives in `memory/`, execution skills don't enforce. Memory hopes recall fires; hook/skill text forces it. Ship-without-debate items are where all three agents agreed (1, 2, 3, 4, 5, 6, 7, 8).

Second meta-finding: **`#pattern/subtract-not-add`.** 5+ traces this week share the same shape — operator rejecting elaborate fixes in favor of removing the problem class (no-dashboard-maintenance-agent × 3, mac-thin-clients, todo-consolidation, pest-list-keep-7). The system has an additive bias; this calibration should reward subtraction.

## Applied this run (7 items)

### A1. CLAUDE.md — retire Mac↔VPS sync line (Critical/High shared)
**Trace evidence:** `2026-05-18-mac-macbook-thin-clients-single-vps.md`
**Change applied:** CLAUDE.md line 239 — rewrote the Evening Workflow bullet to reflect thin-client architecture. Mac+MacBook = SSH clients only; push protects against VPS disk loss, not Mac↔VPS sync.
**Why:** Old text directly contradicted the 2026-05-18 architectural decision. Architecture-strategist P5.

### A2. NEW memory `feedback_principal_only_routing_and_counting.md` (High)
**Trace evidence:** `2026-05-16-bayonne-non-principal-no-jj-route.md`, `2026-05-18-owner-conversations-strict-type-owner.md`, `2026-05-18-carlos-pe-rollup-intro-not-dealflow.md`
**Change applied:** Created `memory/feedback_principal_only_routing_and_counting.md` + added to MEMORY.md index under Deal Screening section. Cross-links to existing PE-rollup feedback.
**Why:** Three independent traces in one week hit the same wall — non-principals routing as principals. Same rule, three surfaces (JJ-routing, owner-conv metric, PE-rollup classifier). Architecture-strategist P3+P4 + Pattern-recognizer P3.

### A3. `decision-traces` SKILL.md — codify anti-pattern #6 (High)
**Trace evidence:** Cross-cutting (16+ task-tracker verb-log traces this week)
**Change applied:** Added anti-pattern #6 "Auto-emitted verb logs from scheduled/CRUD skills" to `.claude/skills/decision-traces/SKILL.md` with examples and the `#pattern/subtract-not-add` named convention.
**Why:** Pattern-recognizer P2+P4. Locks in "auto-emitted verb logs are receipts, not decisions" so the next CRUD-style skill doesn't repeat task-tracker's noise.

### A4. NEW hook `trace_litmus_guard.py` (Critical)
**Trace evidence:** Cross-cutting (14 violations in single week — past 2× graduation threshold by an order of magnitude)
**Change applied:**
- New handler `.claude/hooks/router/handlers/trace_litmus_guard.py` (router-style, registered)
- Registered in `.claude/hooks/router/pre_tool_use.py` HANDLERS list with matcher `^(Write|Edit)$`
- Blocks Write/Edit on `brain/traces/*.md` if body ≤15 non-empty lines AND has `verb/` tag AND no `## Decisions` section
- Suggests redirect to `brain/context/verb-logs/`
**Why:** Pattern-recognizer P1. Recall-dependent fix would repeat with the next skill author; hook forces it.

### A5. NEW hook `canonical_template_guard.py` (Medium)
**Trace evidence:** `2026-05-19-stale-vault-snapshot-not-canonical-template.md`
**Change applied:**
- New handler `.claude/hooks/router/handlers/canonical_template_guard.py` (warn-only, no block)
- Registered in HANDLERS with matcher `^Read$`
- Added `Read` to PreToolUse matcher in `.claude/settings.json` (was `Write|Edit|Skill|Bash`, now `Write|Edit|Skill|Bash|Read`) so the router actually receives Read events
- Fires on Read of `brain/outputs/*-templates*.md` with reminder to fetch live Drive doc via `bash scripts/fetch-template-doc.sh`
**Why:** Architecture-strategist P8 + Pattern-recognizer agreement. Reinforces existing memory `feedback_pull_canonical_doc_live_not_snapshot`.

### A6. Bucket 5 — prune `pipeline-manager/learnings.md` (Medium)
**Trace evidence:** None (lifecycle rule)
**Change applied:** Removed 7 entries dated 2026-05-03. All cite globally-graduated memory + CLAUDE.md sources, observed 18+ clean runs without violation (pipeline-manager runs daily; 18 days since entry creation). Originals preserved in git history. Added removal note.
**Why:** Per learnings.md lifecycle rule. If any of these re-violate within 30 days, re-add the specific anti-pattern.

### A7. Bucket 6 — Skill freshness audit (Medium)
**Picks (tied at 10% staleness; chose highest-touch):** `outreach-manager` (API, 22 Superhuman refs) + `pipeline-manager` (API, 14 Superhuman refs)
**Change applied:** Updated `brain/context/skill-freshness-queue.md` rows: Last Verified bumped to 2026-05-21, status flagged `needs updates — Superhuman refs, sunset 4/29, queued in calibration inbox`.
**Verdicts:** Both `needs updates`. Inline fix NOT applied this run — both SKILL.md files are 796+1290 lines and the Superhuman→Gmail rewrite is non-trivial. Queued in **Deferred** section below.

---

## Deferred to next focused session (9 items)

These items passed agent consensus but are too large/disruptive for late-Thursday application. Apply individually with focused attention.

### D1. Wire women-led-network + network-first gate into 3 execution skills (Critical)
- `niche-intelligence/SKILL.md`: add primary gate BEFORE financial scorecard — "Female-led-network availability: if absent, LOW lock-in regardless of financial fit."
- `target-discovery/SKILL.md`: require confirmed female-led network before invoking list-builder.
- `list-builder/SKILL.md`: warn if >50 targets requested without a confirmed women-led network.
- **Why deferred:** Touches 3 skills, requires careful copy. **Memory exists, zero skills enforce** — biggest structural failure in this calibration. (Architecture-strategist P1, Pattern-recognizer Finding 2.)

### D2. Inbound-classification step in `email-intelligence` + `outreach-manager` (Critical)
- 4 routes: personal intro / specific deal pitch / warm check-in / advisor counsel.
- Hard rule: "If recommending decline on a personal intro, STOP."
- **Why deferred:** Touches 2 large SKILL.md files. Critical — 2026-05-20 lost-contact incident. (Architecture-strategist P2.)

### D3. DELETE 13 task-tracker verb-log traces + fix root cause (Critical, partial)
- Already prevented going-forward by `trace_litmus_guard.py` hook (A4 above).
- Backlog: still need to (a) delete the 13 existing files OR move them to `brain/context/verb-logs/`, and (b) edit `task-tracker-manager/SKILL.md` to stop emitting them.
- **Why deferred:** File-deletion is a separate atomic decision; want clean diff.

### D4. Superhuman→Gmail SKILL.md sweep (High, Bucket 6 follow-on)
- `outreach-manager/SKILL.md`: 22 Superhuman references → Gmail wrapper.
- `pipeline-manager/SKILL.md`: 14 Superhuman references → Gmail wrapper.
- **Why deferred:** 36 occurrences across 2086 lines of SKILL.md. Surgical refactor — not a one-shot apply.

### D5. Retire `weekly-tracker` skill + delete stale memories (High)
- Skill is 752 lines (3.7× archetype cap), never produced data; dashboard owns the capability.
- Move to `.claude/skills/_archive/2026-05-21-weekly-tracker/`, disable any scheduled triggers, delete `memory/project_weekly_tracker_*` files.
- **Why deferred:** Multi-file. Need to verify no live cron/launchd jobs reference it first.

### D6. "Check existing implementation before rebuilding" pre-flight in `plan-refinery` + `health-monitor` (High)
- Three traces in one day (2026-05-17): no-dashboard-maintenance-agent, no-maintenance-agent-fix-plumbing, no-weekly-tracker-sheet-repoint.
- Same pattern: operator killing "add-an-agent-to-do-X" proposals when existing implementation works.
- **Why deferred:** Multi-skill edit, careful wording needed. (Architecture-strategist P6.)

### D7. Parallel-session order-and-read-fully gate in `commands/goodnight.md` (Medium)
- Trace: `2026-05-17-parallel-session-tracker-architecture-conflict.md`
- **Why deferred:** Small, but goodnight.md is touched nightly — want focused attention.

### D8. DELETE ~13 dated session memories + obsolete project/feedback files (Medium)
- MEMORY.md already over 200-line budget per system warning.
- Targets: March/April 2026 session memories, Linkt×3, Motion, April outreach-model pivots, dissolved iMac branch references.
- **Why deferred:** Mass-deletion needs careful per-file decision. Simplicity-advocate P2+P6.

### D9. Cross-link (DON'T collapse) the 3 women-led memories (Low)
- Pattern-recognizer's override of simplicity-advocate's P5: the three are operationally distinct (identity / sequencing / inbound classification).
- Add cross-links between them; don't merge.
- **Why deferred:** Touch-up work; waits for D1 to be done first.

---

## Watchlist (single instance — promote on next observation)

- **W1.** `#pattern/test-real-path-before-escalating` — single trace (2026-05-16 gog false alarm). Structurally identical to `canonical-source-first` + `op-resolve-first`. On 4th sibling fire, group into single "VERIFY THROUGH PRODUCTION PATH" hook.

---

## Stats

- **38 traces** processed in this run (all marked `review_status: applied`).
- **153 traces** remain unreviewed from before 2026-05-15 — backlog defer to subsequent runs or batch via dedicated cleanup.
- **Applied items:** 7 (3 hooks/handlers + 1 new memory + 1 CLAUDE.md edit + 1 SKILL.md edit + 1 learnings prune + freshness-queue update)
- **Deferred items:** 9 (D1-D9 above)
- **Watchlist:** 1 (W1)

## Rollback

After commit, the SHA will be appended here and the calibration can be reverted as one atomic commit.

---
name: calibration-workflow
description: Analyze decision traces and calibrate the system to your preferences. Proposes targeted improvements to skills, CLAUDE.md, and workflows based on patterns in your decisions. Use periodically or after accumulating decision traces.
# WARNING: 2.8x over archetype cap; refactor pending per item 2.
archetype: router
context_budget:
  skill_md: 600
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
---

<objective>
Analyze unreviewed decision traces, identify patterns and gaps, and propose prioritized improvements to the Personal OS. Calibrates the system to your preferences through human-approved changes.
</objective>

<usage>
```
/calibrate              # All unreviewed traces
/calibrate 2025-12-26   # Only traces from Dec 26
/calibrate 12-26        # Short form (assumes current year)
```
</usage>

<essential_principles>
1. **Per-item granularity:** Each decision/learning within a trace gets its own importance rating
2. **Three perspectives:** architecture-strategist, simplicity-advocate, pattern-recognizer analyze ALL items
3. **Cross-trace discovery:** Agents find patterns across traces that weren't visible during individual task execution
4. **Chatroom coordination:** Agents coordinate via chatroom to avoid duplicate proposals
5. **Human approval required:** All changes require explicit user approval before application
6. **Importance ranking:** Proposals sorted critical → high → medium → low
7. **Propose, don't overreach:** Small edits → apply directly. New skills → add to inbox for /create-skill
8. **Version tracking:** Each calibration bumps the OS version (VERSION file)
9. **Easy rollback:** Each calibration creates a single atomic commit that can be reverted
</essential_principles>

<quick_start>
1. Collect unreviewed traces
2. Create chatroom, spawn 3 analysis agents in parallel
3. Agents analyze, discover patterns, coordinate proposals
4. Present approval options (apply all / select / cancel)
5. Apply selected changes, mark traces as `review_status: applied`
6. Write calibration output ONCE → **hook auto-handles:** version bump, archive traces, update stats, stage all
7. Run /commit → single atomic commit with everything
8. Show evolution banner with level progress
</quick_start>

<thursday_buckets>
Thursday meta-calibration covers 6 buckets. Time-box: **30-60 min total** — if a bucket overruns, drop to "best-N this week" rather than blow the budget.

| # | Bucket | What | Where output lands |
|---|--------|------|--------------------|
| 1 | Rule graduation | Rules Kay corrected 2+ times → stop hooks | `.claude/hooks/` + memory file |
| 2 | Memory consolidation | Stale/duplicated `memory/*.md` → merge or delete | `memory/` |
| 3 | Skill doc refresh | SKILL.md files with outdated column refs / superseded rules | `.claude/skills/*/SKILL.md` |
| 4 | Open-loop promotion | `brain/context/session-decisions-*.md` open loops → memories | `memory/` |
| 5 | **Skill learnings promotion** | Scan `.claude/skills/*/learnings.md`, invoke `evolve` per non-empty file | parent skill's SKILL.md / workflows / references |
| 6 | **Skill freshness audit** | Pick 2 stalest skills from `brain/context/skill-freshness-queue.md`, run `create-skill/workflows/verify-skill.md` | freshness-queue date bump + weekly report |

Each bucket appends a section to the weekly calibration report (`brain/outputs/{date}-calibration-weekly.md`).
</thursday_buckets>

<bucket_5_learnings_promotion>
**Trigger:** Thursday meta-calibration.

**Process:**
1. `find .claude/skills -maxdepth 2 -name learnings.md -type f` — enumerate every skill's learnings inbox.
2. For each file: if non-empty (has dated entries beyond the template stub), add the parent skill name to the evolve queue.
3. Prioritize by recency (most recent entry first) if the queue is large.
4. Invoke `evolve` once with the full batch of skill names. Evolve promotes useful entries into the parent skill's SKILL.md / workflows / references and clears `learnings.md` back to template after promotion. Evolve handles classification + smallest-functional-change selection per its own SKILL.md.
5. Capture the resulting list of changed files for the weekly report's bucket-5 section.

**Time-box:** 10-15 min total. If the queue is too large, process the top-N most-recent skills this week; the remainder rolls to next Thursday (their `learnings.md` stays intact).

**Target:** Process ALL skills with non-empty `learnings.md` each Thursday when the queue is small. Do NOT touch `evolve` or `create-skill` themselves — they're plugin-installed reference templates.
</bucket_5_learnings_promotion>

<bucket_6_freshness_audit>
**Trigger:** Thursday meta-calibration.

**Queue file:** `brain/context/skill-freshness-queue.md` (create if missing using the seed schema documented in that file's header). Each row: skill, dependency type (API/CLI/Framework/Pure-process), last-verified date.

**Cadence by type:** API=60d · Framework=90-180d (use 180d) · CLI=180d · Pure-process=365d.

**Process:**
1. Read queue. Compute `staleness_ratio = days_since_verified / cadence_days` per row.
2. Sort descending. Pick **top 2** stalest skills.
3. For each pick, run `create-skill/workflows/verify-skill.md` (Verify-Skill workflow). It categorizes, extracts verifiable claims, checks them via Context7 / CLI version probes / direct API calls, and produces a Fresh / Needs Updates / Stale verdict.
4. If verdict is `Needs Updates` or `Stale`, apply low-risk fixes inline and surface high-risk ones for Kay's approval. Update the skill's SKILL.md with the fixes (small edits) or propose a separate calibration item.
5. Bump the row's `Last Verified` to today and add a one-line status note in the queue file's Notes column (`fresh` / `needs updates` / `stale — fixed inline`).
6. Log results in the weekly report's bucket-6 section: skills audited, verdicts, fixes applied.

**Time-box:** 10-15 min total (2 skills × ~5-7 min each). If both audits return `fresh`, that's healthy — date bump is sufficient.

**Skip self-audit on calibration-workflow** unless no other API/Framework skill has a higher staleness ratio.
</bucket_6_freshness_audit>

<workflow>
## Phase 1: Context Collection

Collect unreviewed traces using the helper script (avoids reading all files):

```bash
python3 .claude/scripts/list-unreviewed-traces.py [date_filter]
```

**Examples:**
- `python3 .claude/scripts/list-unreviewed-traces.py` → all unreviewed
- `python3 .claude/scripts/list-unreviewed-traces.py 2025-12-28` → single date
- `python3 .claude/scripts/list-unreviewed-traces.py "2025-12-27 and 2025-12-28"` → multiple dates

**Script returns:**
- Trace paths, dates, tasks, targets
- Decision/learning counts per trace
- Total counts for summary

**System Inventory (paths only, agents read on-demand):**
- Skills: `.claude/skills/*/SKILL.md`
- Hooks: `.claude/hooks/*.py`
- CLAUDE.md files: `CLAUDE.md`, `brain/CLAUDE.md`, `.claude/CLAUDE.md`
- Schemas: `schemas/vault/*.yaml`
- **SOP:** `G&B Weekly Operating Schedule` in Google Drive (MANAGER DOCUMENTS / AI OPERATIONS). This is the master operating document showing team roles, daily deliverables, notification schedule, and event-driven workflows. Calibration agents MUST review this when proposing changes — any improvement that changes a deliverable, schedule, or notification must update the SOP as part of the change.
  - Drive folder ID: `1F98mmZy6I89YBA9GT_OrOum1Hn4wu9SG`

**Weekly Tracker Data (metrics for system health assessment):**
- Vault snapshots: `brain/trackers/weekly/*.md` — read the last 4 weeks to identify trends
- Google Sheet: `1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE` — Weekly Detail tab has full metrics

**Calibration agents MUST read weekly tracker data** and assess system performance:

| Signal Quality Metric | What it tells the calibration agent |
|---|---|
| Stage 1 Calls < 2/wk for 2+ weeks | Outreach volume or targeting problem → review outreach-manager, target-discovery skills |
| Response Rate declining | Messaging/positioning problem → review outreach templates, email voice |
| Introductions Received = 0 for 3+ weeks | Network not converting → review pipeline-manager nurture cadence, meeting-brief follow-up |
| Deals in Active Review not growing | Funnel stuck → review deal-evaluation skill, identify bottleneck stage |
| NDAs = 0 for 3+ weeks | Conversations not converting → review deal-evaluation Phase 1-2 |

| System Throughput Metric | What it tells the calibration agent |
|---|---|
| Outreach Emails < 5/wk when sprint active | outreach-manager underperforming → check Linkt integration, template quality |
| Cold Calls = 0 when JJ active | JJ workflow broken → check call log creation, target sheet population |
| New Contacts = 0 for 2+ weeks | target-discovery not adding pipeline → check Linkt credits, ICP config |
| Networking Meetings = 0 for 3+ weeks | Relationship engine stalled → review nurture cadence thresholds |

The calibration agent should propose skill improvements that address the specific funnel gap the data reveals — not generic improvements.

### Draft Calibration Loop

The agent drafts emails in Gmail (`gog gmail draft create`). Kay edits before sending. The edits are learning signal. (Superhuman sunset 4/29 per `feedback_gmail_only_no_superhuman`.)

**How it works:**
1. **Pipeline-manager morning scan** reads sent emails from the last 24 hours via Gmail
2. For each sent email, checks if a matching Gmail draft exists (by recipient + subject + approximate time)
3. If a draft match is found, diffs the two: draft (what the agent wrote) vs sent (what Kay actually sent)
4. Captures the diff as a **draft calibration trace** at `brain/traces/{date}-draft-calibration.md`

**Draft calibration trace format:**
```markdown
---
schema_version: 1.0.0
date: {YYYY-MM-DD}
type: trace
tags: [date/{YYYY-MM-DD}, trace, topic/draft-calibration]
---

# Draft Calibration — {date}

## Email 1: {recipient} — {subject}
**Draft (agent):**
{original draft text}

**Sent (Kay):**
{final sent text}

**Edits detected:**
- {what changed: tone, length, opening, specific phrases, structure}
```

**What the calibration agents look for (after 10+ diffs):**
- Patterns in Kay's edits: Does she always shorten? Always change the opening? Remove certain phrases?
- Tone shifts: Does she make it warmer? More direct? Less formal?
- Structural changes: Does she reorder paragraphs? Add/remove sections?
- Phrase preferences: Specific words or constructions she consistently adds or removes

**Output:** The pattern-recognizer agent generates a **voice calibration update** — concrete rules like "Always open with a warm nicety" or "Keep to 3 sentences max" — and proposes updates to the outreach-manager email templates, pipeline-manager draft instructions, or Kay's voice profile at `brain/context/voice.md`.

**Maturity model:**
- **0-10 diffs:** Collecting data, no recommendations yet
- **10-20 diffs:** First patterns emerge, propose initial voice rules
- **20+ diffs:** High-confidence voice profile, agent drafts should need minimal editing
- **Goal:** Draft acceptance rate (sent without edits) increases over time

**Implementation:** Pipeline-manager adds a `draft_calibration` section to `brain/context/email-scan-results-{date}.md` when draft-vs-sent diffs are detected. The calibration-workflow reads these during its Friday run alongside decision traces.

### Active Experiment: Cold Email A/B Test

Outreach-manager is running an A/B test on cold email positioning (started March 2026):
- **Variant A:** "Looking to get into the space" — curiosity-first, loose approach
- **Variant B:** "Well-capitalized buyer" — direct intent, "you or someone you know"

Variant is logged in **Col Z ("Email Approach")** on each niche target sheet as `Learning` or `Direct`. Warm intros are excluded (Col Z blank). The calibration agent must:

1. Read Col Z + outreach outcomes (response, call booked, tone) from the target sheets
2. After 20-30 total sends, run the first analysis:
   - Response rate by variant (A vs B)
   - Time to response by variant
   - Tone of response (warm/curious vs defensive/transactional)
   - Conversion to Stage 1 call by variant
3. Report findings in the weekly calibration report
4. At 30+ sends, recommend whether to:
   - Declare a winner and standardize
   - Continue testing (results too close)
   - Propose a Variant C based on what's working from both

**Do not recommend ending the test before 20 sends per variant.** Small samples lie.

### Agent-Kay Alignment (Calibration Dimension)

Measures how well the agent's target recommendations match Kay's decisions. This is the tightest feedback loop in the system — every mismatch is a learning opportunity.

**Data source:** All 5 target list sheets, comparing Col Q (Agent Notes) against Col O (Kay: Decision).

**Sheet IDs:**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`

**How it works:**
1. For each sheet, read all rows where Col Q starts with `RECOMMEND:` and Col O is non-empty (Kay has decided)
2. Parse the recommendation: `RECOMMEND: Approve` or `RECOMMEND: Pass`
3. Compare against Col O value (`Approve` or `Pass`/blank)
4. Calculate alignment rate: `(matches / total decided rows) * 100`

**Mismatch analysis — surface these as learning opportunities:**

| Mismatch Type | What It Means | Action |
|---|---|---|
| Agent said Approve, Kay said Pass | Agent missed a disqualifying signal Kay caught | Extract Kay's reasoning (if available in Col O notes or session decisions). Update target-discovery ICP or screening rules. |
| Agent said Pass, Kay said Approve | Agent was too conservative or missed a positive signal | Identify what Kay saw that the agent didn't. Relax the relevant filter or add the signal to the scoring model. |

**Report format (included in weekly calibration output):**

```
## Agent-Kay Alignment

Overall: {X}% aligned ({matches}/{total} decisions)

By sheet:
- Art Insurance: {X}% ({n}/{n})
- Domestic TCI: {X}% ({n}/{n})
- IPLC: {X}% ({n}/{n})
- Art Storage: {X}% ({n}/{n})
- Art Advisory: {X}% ({n}/{n})

Mismatches this week:
1. {Company} — Agent: {Approve/Pass}, Kay: {Approve/Pass}. Reasoning gap: {what the agent missed}
2. ...

Trend: {improving / declining / stable} vs last week ({X}% → {Y}%)
```

**Maturity targets:**
- 0-70%: System is learning. High-value mismatches, prioritize fixes.
- 70-85%: Good alignment. Focus on edge cases.
- 85%+: Strong alignment. Consider graduating Col O gate from Active Review to Spot Check.

The pattern-recognizer agent owns this dimension during calibration runs. It reads the sheets, computes alignment, and proposes specific skill updates to close the gap.

## Schedule

**Runs:** Every Friday at 10am ET (automated). Processes all unreviewed traces from the week AND the weekly tracker data. Slack notification to #operations with summary and link to full calibration report.

This follows the weekly tracker (9am Friday) — Kay reviews the numbers first, then reviews system improvement proposals at 10am.

**Monthly overlay (first Friday of each month): Skill Usage + Sunset Audit.**

On the first Friday of each month, calibration runs one additional pass before normal proposal generation:

### Skill Usage Report
For every skill in `.claude/skills/` AND every launchd job:
- **Last-run date** (check `logs/scheduled/{skill}-*.log` for scheduled, grep chat history for interactive)
- **Last Kay-action-taken** (did Kay approve/reject/act on the skill's output within 7 days of run)
- **Output read signal** (did Kay open the output file / reply to the Slack ping)
- **Runs per week, last 30 days**

### Sunset Candidates
Flag any skill matching BOTH:
- Runs-per-week < 1 for last 30 days
- No Kay-action-taken on outputs in last 30 days

Propose sunset as a standard calibration item. Kay approves the sunset → skill is moved to `.claude/skills/_archive/{date}-{skill}` with a commit message explaining why. Launchd job is disabled via `launchctl unload`.

### Golden-Example Rotation
For every skill with an `examples/` folder (see `feedback_golden_examples_stable_deliverables`):
- Query `brain/outputs/` for files with `skill_origin == {skill}` AND `kay_approved == true` in last 90 days
- If 3 most recent Kay-approved outputs aren't already in `examples/`, propose rotation (add new, archive old to `examples/archive/`)
- Per `feedback_skill_output_portfolio`

### Scheduled-Skill Value Audit
For every launchd job, ask: *is this still pulling weight?* Map each to one of:
- **Core** (Kay reads output every run — keep)
- **Background** (silent but valuable — keep)
- **Vestigial** (no recent Kay interaction — sunset candidate)
- **Broken** (errors in logs — repair or sunset)

Surface the map to Kay. She confirms which stay, which sunset.

**Why this exists:** Per Harry Liu's Anacapa webinar (Apr 17 2026), scheduled automation has a noise-to-value trade-off, and the Q1 maturity signal is "admins ask which skills to sunset." At single-operator G&B we proactively run this audit monthly so vestigial skills don't accumulate.

## Phase 2: Coordinated Analysis

Create chatroom with proper frontmatter, then spawn ALL 4 agents in parallel.

**Chatroom file:** `brain/traces/agents/{date}-calibrate.md`

```yaml
---
schema_version: 1.0.0
date: {YYYY-MM-DD}
task: Calibration analysis of {n} traces from {date_filter}
agents: [coordinator, architecture-strategist, simplicity-advocate, pattern-recognizer]
status: active
---

# Agent Chatroom: Calibration Analysis

## Coordination Log
```

**Spawn 4 agents in ONE message using 4 Task tool calls:**

| Agent | Role | What It Does | Output Budget |
|-------|------|--------------|---------------|
| coordinator | Orchestration | Watches chatroom, waits for 3 `-> READY`, posts `-> CLOSE`, synthesizes all proposals | 3,000 words |
| architecture-strategist | Analysis | Reads traces, identifies gaps, posts findings + `-> READY` | 2,000 words |
| simplicity-advocate | Analysis | Reads traces, finds over-engineering, posts findings + `-> READY` | 2,000 words |
| pattern-recognizer | Analysis | Reads traces, finds patterns, posts findings + `-> READY` | 2,000 words |

**All 4 spawned by orchestrator (main conversation) using Task tool.**
All have hooks. All can write to chatroom. Coordinator doesn't spawn anyone - just coordinates.

**Give each agent:**
- Trace paths from script output (not contents)
- System inventory paths (not contents)
- Chatroom path
- Their specific role and output budget

**Orchestrator waits for coordinator's TaskOutput only.**
Coordinator returns synthesized report. Other 3 agents' outputs stay in their contexts.

## Phase 3: Proposal Generation

After all agents post `-> READY`:
1. Post `-> CLOSE` to chatroom
2. Collect TaskOutput from each agent
3. Deduplicate proposals (agents may identify same issue)
4. Merge importance ratings (take highest if disagreement)
5. Generate calibration proposal at `brain/outputs/calibrations/{date}-calibration.md`

## Phase 4: Human Approval

Present summary and options via AskUserQuestion:

```
CALIBRATION COMPLETE

Traces analyzed:     {count}
Proposals:           {count}
Learnings captured:  {count}

CRITICAL ({count})
  1. {target}: {title} ({trace_count} traces)
  ...

HIGH ({count})
  ...

What would you like to do?

[1] Apply all & commit
[2] Apply all & review first
[3] Select specific changes
[4] Cancel
```

## Phase 5: Application

Based on user choice:

**Option 1 (Apply all & commit):**
1. Apply each edit in sequence
2. Mark all processed traces as `review_status: applied`
3. Write calibration output file ONCE (with full content + Result banner) → **hook fires:**
   - Bumps VERSION (patch)
   - Moves applied traces to `brain/traces/processed/`
   - Updates `.claude/stats.yaml` with new count + level
   - Stages everything with `git add`
   - Returns message: "All changes staged. Run /commit to finalize."
4. Run `/commit` to create single atomic commit including ALL changes
5. Show evolution banner with level progress

**IMPORTANT:** Only write the calibration output file ONCE, at the very end. The hook triggers on this write and does all the housekeeping.

**Option 2 (Apply all & review first):**
- Apply edits but don't commit
- Show git diff for review
- Wait for user confirmation
- Then bump VERSION and continue with steps 4-6 above

**Option 3 (Select specific):**
- Ask which upgrades to apply (comma-separated numbers)
- Apply selected only
- Mark applied traces as `review_status: applied`
- Mark skipped traces as `review_status: skipped`
- Continue with steps 3-6 above

## Validation Gate (before Slack notification)

Before sending the Slack notification, validate all outputs. If any check fails, fix before notifying.

- [ ] **Chatroom properly closed** — `brain/traces/agents/{date}-calibrate.md` has `status: completed` in frontmatter and contains a `-> CLOSE` post from the coordinator
- [ ] **Calibration proposal generated** — `brain/outputs/calibrations/{date}-calibration.md` exists at the expected path and is non-empty
- [ ] **At least one actionable proposal** — the calibration output contains at least one proposal with a target file and a concrete edit (not just observations or "no changes needed")
- [ ] **SOP version bumped if changes applied** — if any applied proposal modifies a deliverable, schedule, or notification referenced in the SOP (G&B Weekly Operating Schedule), verify the SOP was updated as part of the change. If SOP update is missing, add it before committing.

If validation fails: fix the issue and re-validate. Do NOT send Slack until all checks pass. If chatroom is stuck (agents never posted READY), log the failure and present a degraded summary to Kay directly in the session.

## Notification

After validation passes, notify Kay. **Slack summary is 6 lines** (one per Thursday bucket — `rules-graduated / memories-cleaned / skill-docs-refreshed / open-loops-promoted / learnings-evolved / skill-audits-completed`) plus the standard header + footer:

```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Weekly Calibration Ready (Friday 10am)\nTraces analyzed: {n} | Proposals: {n} ({critical} critical, {high} high)\n• Rules graduated: {n}\n• Memories cleaned: {n}\n• Skill docs refreshed: {n}\n• Open loops promoted: {n}\n• Learnings evolved: {n} (skills: {names})\n• Skill audits completed: {n} ({skill-a}: {verdict}, {skill-b}: {verdict})\nReview in Claude Code to approve/reject changes."
  }'
```

**Option 4 (Cancel):**
- No changes made
- Traces remain pending
- User can re-run later
</workflow>

<references_index>
| Reference | Purpose |
|-----------|---------|
| references/sub-agents.md | Agent definitions, prompts, coordination protocol |
</references_index>

<leveling_system>
Track progress in `.claude/stats.yaml`:

```yaml
total_traces_processed: {count}
total_calibrations: {count}
last_calibration: {date}
creature: ember  # ember | drift | bloom (set during /onboard)
```

**Evolution stages (faster first hatch):**
| Stage | Traces | Name | Notes |
|-------|--------|------|-------|
| 1 | 0-9 | Egg | First calibration hatches it |
| 2 | 10-99 | Hatchling | Day 1 achievement |
| 3 | 100-499 | Juvenile | ~1-2 weeks |
| 4 | 500-1499 | Adult | ~1-2 months |
| 5 | 1500+ | Legendary | Long-term goal |

**Creature emoji map:**
| Creature | Emoji |
|----------|-------|
| ember | 🔥 |
| drift | 💧 |
| bloom | 🌿 |
| (none) | 🌱 |

**After applying changes:**
1. Count total traces with `review_status: applied`
2. Update `.claude/stats.yaml`
3. Calculate stage from trace count
4. If creature set: Read art from `.claude/creatures/{creature}/{stage}.txt`
5. Display evolution banner with creature
</leveling_system>

<rollback_protocol>
Every calibration creates a SINGLE atomic commit for easy rollback.

**Rollback command:** After committing, print `git revert <sha>` to terminal. Do NOT try to embed the commit SHA in the output file (this requires a two-commit pattern that adds complexity). The rollback command is ephemeral but sufficient.

**Evolution display after calibration:**

Shows after EVERY calibration - creature art (right) + metrics + changes in one compact screen.

**Creature art height by stage (grows as it evolves):**
| Stage | Height |
|-------|--------|
| Egg | 3 lines |
| Hatchling | 5 lines |
| Juvenile | 7 lines |
| Adult | 9 lines |
| Legendary | 11 lines |

**Layout principles:**
- Header combines: name · stage · version (compact)
- Metrics inline where possible
- Applied list flows alongside creature
- Separator above progress bar
- No wasted whitespace

If creature is set (user ran /onboard):

**Egg (3 lines):**
```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  🔥 EMBER · Egg · v1.0.2 → v1.0.3                      ___       ║
║  Traces: 8 processed · 3 applied                     ( 🔥 )      ║
║                                                       \_/        ║
║  ✓ calibration-workflow: Add evolution stages                    ║
║  ✓ CLAUDE.md: Update querying docs                               ║
║                                                                  ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║  [████░░░░░░░░░░░░░░░░] 8/10 to Hatchling                        ║
║  To undo: git revert {sha}                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

**Hatchling (5 lines):**
```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  🔥 EMBER · Hatchling · v1.0.5 → v1.0.6                ^  ^      ║
║  Traces: 12 processed · 4 applied                    (o  o)      ║
║                                                     (  🔥  )     ║
║  ✓ calibration-workflow: Add evolution stages        \    /      ║
║  ✓ CLAUDE.md: Update querying docs                    \  /       ║
║  ✓ today skill: Fix date formatting                              ║
║                                                                  ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║  [██████░░░░░░░░░░░░░░] 45/100 to Juvenile                       ║
║  To undo: git revert {sha}                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

**Legendary (11 lines):**
```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  🔥 EMBER · Legendary                           🔥  /\  🔥        ║
║  v2.1.0 → v2.1.1                                   /  \          ║
║                                                   / 🔥🔥 \        ║
║  Traces: 1847 processed                          /   ||   \      ║
║  Changes: 6 applied                             /    ||    \     ║
║                                                ( 🔥  ||  🔥 )     ║
║  ✓ calibration-workflow: Refactor              \    ||    /      ║
║  ✓ CLAUDE.md: Major update                      \   ||   /       ║
║  ✓ onboard: Add new creature                     \  ||  /        ║
║  ✓ today: Performance fix                     ~~~~ ETERNAL ~~~~  ║
║  ✓ client-context: Bug fix                                       ║
║  ✓ email-draft: New template                                     ║
║                                                                  ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║  [████████████████████] 1847/1500 · LEGENDARY ACHIEVED           ║
║  To undo: git revert {sha}                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

Read creature art from `.claude/creatures/{creature}/{stage}.txt` and display on RIGHT side.

If no creature (user hasn't run /onboard):
```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  🌱 PERSONAL OS · v1.0.2 → v1.0.3                                ║
║  Traces: 8 processed · 3 applied                                 ║
║                                                                  ║
║  ✓ calibration-workflow: Add evolution stages                    ║
║  ✓ CLAUDE.md: Update querying docs                               ║
║                                                                  ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║  [████░░░░░░░░░░░░░░░░] 8/10 to next stage                       ║
║  💡 Run /onboard to choose your creature companion!              ║
║  To undo: git revert {sha}                                       ║
╚══════════════════════════════════════════════════════════════════╝
```

**Progress bar:** 20 chars, █ for filled, ░ for empty

**Also append this banner to the calibration output file** at `brain/outputs/calibrations/{date}-calibration.md`
</rollback_protocol>

<success_criteria>
- [ ] Date filter applied (if provided)
- [ ] Traces collected, individual items extracted
- [ ] Per-item importance ratings assigned
- [ ] Chatroom created, all 3 agents posted -> READY
- [ ] Proposals deduplicated and ranked by importance
- [ ] Calibration proposal document generated
- [ ] User presented with 4-option approval workflow
- [ ] Selected changes applied correctly
- [ ] Traces marked with review_status
- [ ] VERSION file bumped
- [ ] `.claude/stats.yaml` updated with new trace count
- [ ] Single atomic commit created with version in message
- [ ] Evolution banner displayed with level progress
- [ ] Evolution banner appended to calibration output file
</success_criteria>

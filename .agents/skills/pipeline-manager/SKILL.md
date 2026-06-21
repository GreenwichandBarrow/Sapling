---
name: pipeline-manager
description: "Daily morning briefing — pipeline stage changes, outreach recommendations (nurture cadence), and action items (Granola). Kay reviews, approved items are appended to the To Do tab via task-tracker-manager. Runs when Kay says good morning."
# WARNING: 6.4x over archetype cap; refactor pending per item 2.
archetype: router
context_budget:
  skill_md: 1300
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI or REST call:
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `ATTIO_API_KEY`, `APOLLO_API_KEY`, `GRANOLA_KEY`, `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_*`. **NEVER `source scripts/.env.launchd` raw** — it exports literal op:// reference strings, not values (hook-blocked; see `feedback_op_env_before_op_backed_cli`).

**REST is the default, MCP is a convenience.** If an MCP call appears below (`mcp__attio__*`), it has a REST fallback in this same file. An unloaded MCP tool is NOT an outage — fall through to REST. For Granola transcripts, pipeline-manager does not call MCP/OAuth/direct REST; `post-call-analyzer` owns transcript retrieval through the 1Password-backed `granola-api` wrapper and writes `brain/calls/` plus staged task artifacts for this skill to consume.

**Health-check pattern (mandatory before claiming a service is down in an artifact):**
```bash
curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $ATTIO_API_KEY" https://api.attio.com/v2/self
# 200 = up. Non-200 = real outage. Unloaded MCP tool = not an outage.
```

**Forbidden in the briefing artifact:** writing "MCP unauthenticated / disconnected / unavailable" as a system-status alert without first running the op-env resolve + REST health-check above. Phantom outages corrupt downstream decisions.

**Gmail safety contract (mandatory):** Pipeline-manager may read Gmail evidence and create Gmail DRAFTS only. It must never send, draft-send, forward, autoreply, or schedule-send email. Every `gog gmail` command must include Kay's account and the no-send guard:
```bash
gog gmail ... --account kay.s@greenwichandbarrow.com --gmail-no-send
```
Draft creation uses `gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send ...`. If a draft command cannot be made draft-only, skip it and surface the blocker. Kay alone sends emails.
</credentials>

<learnings>
**Read `learnings.md` BEFORE running this skill, append BEFORE returning.**

Path: `.agents/skills/pipeline-manager/learnings.md`

This is the skill-local feedback loop (Harrison Wells coaching pattern, 4/30/26). Pipeline-manager-specific anti-patterns accumulate here. Cross-skill rules live in `memory/feedback_*.md`.

**Read step (before any other work):**
1. Open `learnings.md`. Internalize the active "do NOT" entries — they take precedence over any positive instruction in this SKILL.md if there's conflict.
2. Note the "Watching for" section — these are anti-pattern suspects worth flagging if you observe them.

**Append step (before returning the briefing):**
1. If you caught yourself about to violate a learning (and corrected) — note it briefly so the entry compounds confidence (5+ honored runs = pruning candidate).
2. If you observed a NEW anti-pattern (Kay corrected you mid-run, or you noticed a pattern that produced bad output) — add it under "Active learnings" with `[YYYY-MM-DD]` + source citation. If it's likely cross-skill, ALSO graduate to `memory/feedback_*.md`.
3. Do NOT append entries that just rephrase existing rules. Only NEW anti-patterns.

This file is read on every run and is the durable correction layer that complements (not replaces) global memory.
</learnings>

<objective>
Keep the pipeline truth current without Kay having to remember to update Attio manually. Source truth comes from Kay-confirmed pipeline review facts plus evidence signals (calendar, email, call notes, vault, Drive folders, and session decisions). Attio is the operating database and dashboard feed that must be reconciled to that truth, not the sole source of truth.

Kay is the bottleneck on pipeline management. This skill removes that bottleneck by turning daily pipeline truth capture into a 30-second review, then updating Attio and the dashboard snapshot from that reviewed truth.

## Codex-era role

This skill is still necessary, but it must add value as the **evidence-to-Attio reconciler**, not as a duplicate deal screener or relationship manager:
- Own: pipeline stage truth, Active Deals folder/Attio reconciliation, email/Granola evidence handoffs, stale pipeline flags, and verified task handoffs.
- Consume: `relationship-manager` artifacts for People/nurture status, `deal-aggregator` artifacts for market/listing intake, `niche-intelligence` artifacts for thesis/niche state, and `task-tracker-manager` for To Do writes.
- Avoid duplicating: broad deal sourcing, full relationship cadence analysis, and niche thesis scoring unless the section is explicitly a handoff or validator.
- Prefer deterministic reconciliation over prose-heavy judgment. When evidence is missing or stale, write the missing artifact/blocker instead of inventing a recommendation.
</objective>

<essential_principles>
## How It Works

1. **Detect** — Scan yesterday's calendar, email, Granola, and vault for activity signals
2. **Match** — Cross-reference signals against Attio pipeline entries AND People records
3. **Recommend** — Present stage change recommendations AND relationship updates to Kay
4. **Execute** — On approval, update pipeline stages AND People record attributes via Attio API
5. **Flag** — Surface stale deals (same stage 2+ weeks) AND overdue nurture contacts
6. **Follow up** — Draft thank yous, create entities for intros, append To Do rows via task-tracker-manager
7. **Nudge** — Send Slack ping so Kay knows updates are waiting

## Two Systems, One Daily Review

The pipeline-manager handles two connected but distinct tracking systems:

### Pipeline Stages (3 Lists)
For **Active Deals and Investor** pipelines. Company-based. Linear progression through stages.
- Signal: deal milestone (NDA signed, financials received, LOI, etc.)
- Action: move entry to new stage

### Network Relationships (People Records)
For **all network contacts**. Person-based. Non-linear relationship management.
- Custom attributes on People: `relationship_type`, `nurture_cadence`, `value_to_search`, `next_action`, `how_introduced`
- Signal: meeting happened, email exchanged, intro promised, thank you needed
- Actions: update `next_action`, update `nurture_cadence`, flag overdue contacts

### Daily Review Flow

On morning sign-on, Codex presents the review with the header **"Pipeline Review"** at the top. All sections are presented sequentially. Kay reviews each item and approves or skips. Approved outreach and action items are appended to the To Do tab via task-tracker-manager. **All items presented for review must be numbered.**

**Inbound Deal Flow (before sections):**
If any inbound intermediary deals were detected during Gmail ingestion, present them first. These are time-sensitive — intermediaries shop deals to multiple buyers. See "Inbound Intermediary Deal Detection" section below for format and actions.

**Pipeline Snapshot Control (daily, before Decisions assembly):**
Run a compact Active Deals reconciliation every Good Morning because deal volume is increasing and Kay should not have to remember Attio updates. This is an operating-control check, not a dashboard report.

Required inputs, in priority order:
- Kay-confirmed pipeline facts from the morning review or current session. These are authoritative once stated clearly.
- Evidence signals: `email-scan-results-{date}.md`, recent `brain/calls/`, current/prior `session-decisions`, ACTIVE DEALS Drive folders, and financials/CIM artifacts.
- Current Attio snapshot: `brain/context/attio-pipeline-snapshot.json` from `Active Deals – Owners`; use it as the current database state to reconcile, not as final truth.
- Active dashboard scope: engaged pipeline only (`Contacted` shown as `Warmed / Teaser`, plus `NDA`, `Financials Received`, `Submitted LOI`, `Signed LOI`). Exclude raw `Identified` rows from Good Morning active-pipeline counts.

Ask Kay only for missing status that cannot be defensibly inferred. The prompt must be short and operational:
`Pipeline check: I have {N} engaged active deals on the dashboard. Any new deals, passes, financials received, or stage changes since yesterday?`

If signals already show a likely stage change, recommend it directly instead of asking an open question:
`RECOMMEND: Move {Company} from {old_stage} to {new_stage} — {evidence}. → YES / NO / DISCUSS`

Daily checks:
1. **New deals** — any direct/intermediary deal with teaser/CIM/financials, new ACTIVE DEALS folder, or Kay-stated active deal must exist in Attio. If CIM/financials exist, create/move to `Financials Received`.
2. **Current deals** — list every engaged dashboard deal by company and stage internally; surface only mismatches, stale items, or requested confirmations. Do not count raw `Identified` rows as active pipeline.
3. **Passed deals** — any Kay-stated pass, decline draft sent, call note pass, or session-decision REJECT on an active deal must move to `Closed / Not Proceeding` after Kay confirms if evidence is ambiguous.
4. **Financials received** — any company Kay says is in Financials Received, or any CIM/financials artifact exists, must be in Attio at `Financials Received`; missing Attio entries are bugs to fix, not dashboard display issues.
5. **Stale deals** — flag engaged dashboard deals with no movement for 14+ days as `kill / advance / keep watching`, but only if there is a concrete company name and current stage.

Source tagging control:
- Treat source tagging as forward operating hygiene, not a broad historical CRM cleanup. Attio is the operating database to reconcile, not the sole source of truth; Salesflare-era history is incomplete unless backed by evidence.
- Every new real opportunity must get exactly one fixed source category plus a separate source detail. Fixed categories: `Conference / networking`, `Intermediary / river-guide`, `Warm email`, `LinkedIn`, `Broker marketplace`, `Cold email`, `Cold call`, `Inbound email`, `Unknown / needs review`.
- A real opportunity is one with a direct seller/owner response, intermediary/broker conversation, teaser/CIM/financials received, NDA path started, or an explicit Kay instruction to track it.
- If a meaningful active deal lacks source, ask one short Good Morning cleanup question instead of guessing: `{Company} is {stage} but source is missing. Source? → intermediary / conference / warm email / LinkedIn / marketplace / inbound / other`.
- Backfill only historical deals that reached NDA, financials, LOI, closed/not proceeding after NDA, or investor-reported examples. Do not reconstruct every old Salesflare/Attio lead.
- The dashboard must display mapped source or `Unknown / needs review`; it must never infer source attribution from incomplete CRM state.


Execution contract after Kay approves or states a factual correction:
- Treat the approved/corrected pipeline fact as source truth.
- Update Attio to match that truth.
- Run `scripts/refresh-attio-snapshot.sh` immediately after Attio changes so the dashboard reflects the new truth without waiting for the hourly timer.
- Verify `brain/context/attio-pipeline-snapshot.json` contains the expected company/stage.
- If Attio cannot be updated, write a clear blocker and surface it as a broken-system item; do not let the dashboard silently drift.

Dashboard contract:
- Dashboard pipeline cards remain read-only and sourced from the Attio snapshot.
- The snapshot should mirror reviewed pipeline truth after Attio reconciliation.
- Do not patch dashboard JSON by hand to make the UI look right. Fix the underlying Attio/snapshot reconciliation plumbing.

**Present the review in these sections, in this order:**

### Section 1: Active Deals Pipeline
Stage changes, new entries, and stale deals for the Active Deals – Owners list.
After each owner call or meeting, ask: "Was this a meaningful owner conversation?" If yes, check the `meaningful_conversation` checkbox on the Active Deals entry in Attio.
- Show: company, current stage, recommended stage, signal evidence
- Kay approves → Attio updated immediately
- Kay rejects → no change
- Flag stale deals (same stage 2+ weeks): "Kill, advance, or keep watching?"

### Section 2: Investor Pipeline
Stage changes for the Investor Engagement list.
- Quarterly update status, meeting prep triggers
- Conference decisions detected (Attend/Register Only) with registration details

### Section 3: Relationship Building
Everything related to People records (not in a pipeline list). Nurture cadence, next_actions, thank-yous, intros.

Check ALL People with nurture_cadence set against their `last_interaction` date in Attio. Surface anyone overdue.

Format: "Consider following up with {name} ({relationship_type}, {nurture_cadence}). Last contact: {date}."
- **Approve** → To Do row appended via task-tracker-manager: "Follow up with {name}" with due date based on urgency
- **Skip** → no action

Cadence thresholds:
- Weekly: overdue after 10 days
- Monthly: overdue after 5 weeks
- Quarterly: overdue after 14 weeks
- Occasionally: overdue after 7 months
- Dormant: never surfaced

**Auto-resolve "Need to..." stages BEFORE surfacing:**
Before presenting any relationship items, the Relationships Agent must run the Action-Already-Taken Verification (see Sub-Agent 2). For each contact in a "Need to..." stage (Need Thank You, Need to Schedule, Need to Reschedule), search for outbound emails by recipient + recency — NOT by subject keyword. If Kay already acted, auto-move and don't surface. Only present contacts where the action is genuinely still pending.

Also surface:
- Stale next_actions (same next_action for 2+ weeks)
- New contacts from yesterday's meetings that need to be added
- Recent contacts whose attributes need updating

Present max 5 nurture reminders per session. Prioritize by: relationship value, days overdue, relationship_type.

### Section 4: Action Items (from post-call analyzer)
Present action items staged by `post-call-analyzer`, not raw Granola scans.

Default Good Morning scope is **fresh post-call analysis only**: read non-hidden JSON files in `brain/trackers/post-call-analyzer/pending-tasks/*.json`, but surface only task batches whose `staged_at`, `call_date`, source call timestamp, or file mtime is within the prior 24 hours of the morning run. These are candidates for Kay approval, not commitments, and they are not already on the To Do sheet.

Older pending files are backlog, not morning-review material. Do not dump them into the briefing. If older files exist, surface at most one low-priority routing item: `Post-call task backlog exists — recommend Task Manager review/suppress stale items`, or omit it when the Task Manager thread already owns that cleanup.

Each fresh file is a batch of review-ready task objects produced after the transcript
Doc + meeting analysis Doc were saved. Treat these as candidates only. They are
not commitments and they are not already on the To Do sheet.

Format each item as a numbered decision:
`From {source meeting/date}: "{task_text}" — recommended {suggested_day or "timing TBD"}`
→ **YES / NO / DISCUSS**

- **YES** → append a To Do row via `task-tracker-manager` using the approved
  task text, type, project, and Kay-approved timing. Then move the source JSON
  file to `brain/trackers/post-call-analyzer/pending-tasks/processed/` only
  after every approved task in that file lands on the To Do sheet.
- **NO** → do not append. Add a short declined marker to the processed archive
  so the same task is not resurfaced forever.
- **DISCUSS** → keep the JSON file in `pending-tasks/` unless Kay resolves the
  decision in-session.

Do not query Granola MCP or re-extract meeting action items here. The server
post-call analyzer owns transcript retrieval through the 1Password-backed
Granola REST wrapper and writes these staged task files as the handoff.

## Output Format

### Briefing vs Slack Routing (CRITICAL)

The morning briefing in conversation must be **brief** — a quick reminder of what needs Kay's yes/no decision. It is NOT where Kay learns about new information that requires deep review.

**Route to Slack (not briefing):**
- New deals in pipeline (intermediary inbound, new targets discovered)
- Tracker/list updates that need scrolling or detailed review
- New intermediaries added to pipeline
- Attendee lists processed
- Any item requiring more than 2 lines of context to understand

**Keep in briefing (conversation):**
- Pipeline stage changes needing yes/no approval (1 line each)
- Pipeline summary stats (3-4 lines)
- Quick action items (draft email for Kay review, make call)
- Today's calendar/agenda items
- Stale deal flags (kill/advance/keep)
- Overdue contacts needing a touchpoint

**Rule of thumb:** If Kay needs to read more than a sentence of context to act on it, send it to Slack with a link. The briefing is a checklist, not a report.

### Briefing Format (Dashboard Sections)

Updated 2026-06-19 per Kay: Good Morning should be a concise operating edit surface for Kay, not a back-end operations report. Use dashboard-aligned sections, but each section must primarily show Kay-actionable items she can approve, reject, discuss, or update for the day. The dashboard is the reference point after morning briefing; the briefing is where daily edits/decisions happen and then dashboard/source systems get updated. Keep one compact operational-status line per section at most, only when it affects trust/freshness; it must still be numbered so Kay can reference it efficiently. If a section has no Kay-actionable material, write `N/A`. Keep closed deals out of Active Pipeline unless changed in-session.

**Header line:** one sentence pointing to the dashboard using clickable markdown:
`[https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)`

**Required sections, in order:**

Dashboard sections come first, in dashboard-navigation order, before non-dashboard operating follow-up. Current order: Email Orchestration, Active Pipeline, Deal Aggregator, C-Suite & Skills, System Health, Meeting Briefs, Tasks & Follow-up, then Decisions Needed only if needed.

1. **Email Orchestration**
   - Audience = Kay. Show only email follow-through items she needs to review/approve/handle today. This section is not an inbox digest.
   - Mirror the Email Orchestration dashboard tab subsections exactly: `24-hour thank-yous`, `48-hour follow-ups`, and `EOW follow-ups`.
   - Do not include a generic `Draft review` row. Drafts may appear only inside the relevant dashboard follow-up bucket, and only with concrete context: recipient/name, subject/purpose, age, and the decision needed. If the draft purpose is unclear, surface as `Clarify draft identity` with the draft subject/recipient; do not say only `2 Gmail drafts pending`.
   - Do not include `Deal-flow email` in Email Orchestration. Deal-flow alerts, broker blasts, marketplace emails, and auto/deal-flow label outputs belong in the Deal Aggregator section.
   - Do not invent Email Orchestration subsection labels such as `Team follow-up`, `Ops follow-up`, or other ad hoc categories. If an email item does not fit the three dashboard follow-up buckets, route it to Deal Aggregator, Tasks & Follow-up, or omit it.
   - Generic unread-email reminders are prohibited. Surface an email outside the three buckets only if there is a concrete action or analysis recommendation, e.g. `Run monthly budget assessment from Start Virtual EOW financials` rather than `read Start Virtual email`.
   - Include at most one operational-status line only when it matters for trust/freshness, and only if it is tied to a Kay decision. Do not fill this section with back-end scan mechanics.

2. **Active Pipeline**
   - Group by stage, not by generic list. Match the dashboard Active Pipeline Snapshot scope exactly: `Contacted` as `Warmed / Teaser`, plus `NDA`, `Financials Received`, `Submitted LOI`, and `Signed LOI`. Exclude raw `Identified` rows even though they are non-closed Attio rows.
   - Stage format: `Warmed / Teaser`, `NDA`, `Financials Received`, `Submitted LOI`, `Signed LOI`; under each, list the deals in that stage and the action/status Kay needs to confirm. `Warmed / Teaser` comes first because it is most likely to drift out of date.
   - Ask for status where missing, but recommend concrete stage moves when evidence supports them. Do not discuss closed deals unless changed in-session.

3. **Deal Aggregator**
   - Show only still-open surfaced-deal or source decisions Kay needs to review: thumbs up/down, source registration/access blockers, source retirement/addition approvals, or screening calibration.
   - Do not show completed source-admin confirmations as numbered items. If a source was already added/labeled/resolved, omit it from the briefing unless it creates a new decision or failure.
   - Include at most one operational-status line for run freshness/volume, only when it changes Kay's decision surface. Do not dump source mechanics or retired mode details.
   - This section's final dashboard-aligned subsections are pending the deal-aggregator plumbing review; until then, keep it sparse and action-only.

4. **C-Suite & Skills**
   - Dashboard-aligned skill/status section. Surface only Kay-relevant skill failures, missed expected runs, approvals needed, or migration/plumbing decisions. If none, write `N/A`.
   - Do not duplicate System Health failures unless Kay needs a skill-specific decision.

5. **System Health**
   - Failure-only dashboard section. Surface the same RED/YELLOW failures that would otherwise create a Slack alert: failed scheduled jobs, stale required artifacts, stale snapshots, or dashboard/system plumbing failures. If none, write `N/A`.
   - Debugger/health-monitor findings must name the failing check and the recommended fix.
   - Do not place planned plumbing work here; planned dashboard plumbing belongs in Tasks & Follow-up.

6. **Meeting Briefs**
   - Non-dashboard operating follow-up section. Scan upcoming external meetings in the brief-prep window and ask whether a brief is needed.
   - Default window: next 48 hours. Friday covers Friday + Monday + Tuesday; Sunday covers Sunday + Monday.
   - Track last-minute meeting additions for the next few weeks: if meetings are repeatedly added inside the 48-hour window without enough prep time, surface a coverage fix.

7. **Tasks & Follow-up**
   - Do not repeat the To Do list or advise Kay how to prioritize it. The To Do file is the canonical task surface.
   - If there are existing open tasks, report only the count, e.g. `Task Manager: 21 open tasks today.`
   - Surface only items that are NOT already on the To Do list and need Kay approval/routing, especially post-call analysis outputs, new relationship-manager candidates, new dashboard/plumbing failures, or newly discovered operating loops.
   - Before surfacing any task-like item, check whether it is already on today's To Do list. If it is already there, omit it from the morning brief.
   - Use roman numerals or letters for subtasks only when Kay needs to approve several new sub-items.

**Numbering and decisions:** Every referable line across every section gets a stable number, including operational/freshness lines. Continue numbering sequentially from top to bottom and do not reset numbering by section. Default to a collapsed, easy-to-reference format: main section headers are flush left, and each numbered line begins with the dashboard subsection label in bold, e.g. `1. **24-hour thank-yous:** Laura / Stephanie / Randi drafts ready`. Use expanded subsection headers only when a subsection has 2+ separate items that need individual decisions. Sub-items use roman numerals or letters. Include `Decisions Needed` only when a separate consolidated approval list helps; otherwise the numbered items inside each section are the decision surface. Keep the Obama framing for true approvals, but brief operational items can use concise `YES / NO / DISCUSS` or `KEEP / MOVE / CLOSE` choices.

```
**Good morning. {Day} {date}.** Dashboard: [https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)

**Email Orchestration**

1. **24-hour thank-yous:** {Thank-you item or N/A} → **REVIEW / SKIP / DISCUSS**
2. **48-hour follow-ups:** {Follow-up item or N/A} → **KEEP TODAY / MOVE / DROP**
3. **EOW follow-ups:** {EOW follow-up item or N/A} → **KEEP / MOVE / DROP**

**Active Pipeline**

4. **Ops:** {Snapshot freshness/count mismatch only if relevant}
5. **Warmed / Teaser:** {Deal} — {Kay action/status needed} → **ADVANCE / NURTURE / CLOSE / DISCUSS**
6. **NDA:** {Deal} — {Kay action/status needed} → **KEEP / ADVANCE / CLOSE / DISCUSS**
7. **Financials Received:** {Deal} — {Kay action/status needed} → **MODEL / REQUEST INFO / CLOSE / DISCUSS**
8. **Submitted LOI:** {Deal or N/A} → **FOLLOW UP / HOLD / DISCUSS**
9. **Signed LOI:** {Deal or N/A}

**Deal Aggregator**

10. **Ops:** {Run freshness/volume only if relevant}
11. **New surfaced deals:** {Deal/source decision} → **YES / NO / DISCUSS**
12. **Deal-flow email:** {Only if specific deal-flow email needs aggregator decision} → **RUN REVIEW / WAIT / DISCUSS**

**C-Suite & Skills**

13. **Skills:** {Skill failure/approval item or N/A} → **FIX / DEFER / DISCUSS**

**System Health**

14. **Failures:** {Failure item or N/A} → **FIX / DEFER / DISCUSS**

**Meeting Briefs**

15. **Next 48 hours:** {Meeting brief decision or N/A} → **PREP / SKIP / DISCUSS**
16. **Last-minute meeting watch:** {Gap/watch item or N/A}

**Tasks & Follow-up**

17. **Task Manager:** {Open task count only, e.g. 21 open tasks today}
18. **Post-call / new routing:** {Only new item not already on To Do, or N/A}
19. **Deferred / unresolved:** {Only new item not already on To Do, or N/A}
```

**Briefing hygiene (CRITICAL):**
- Only surface items that need action or decision. If something is done, resolved, or loop-closed — omit it entirely per `feedback_briefing_no_done_items`.
- Never report back things Kay did herself — she already knows.
- Noise (true low-value items) gets archived silently, never surfaced as a "noise" section.
- Every item has an explicit question or action per `feedback_morning_briefing_format`. No ambiguous items.

**Default to recommending, not asking** per `feedback_decision_fatigue_minimization`. Pre-decide whatever is defensible from existing patterns. Bundle related questions into a single bundled approval. When Kay makes the same call twice, codify it as a memory or skill default so she never sees it again.

**Brief-needed prompt rules (replaces retired meeting-brief-manager nightly automation):**
- Surface these in the **Meeting Briefs** section, not buried inside M&A Activity or Decisions.
- List the next 48 hours of external meetings (skip internal, skip investor calls already briefed). Same-day externals must surface — D+1-only scans drop them. Source: `memory/feedback_preflight_covers_today_and_tomorrow.md` (added 2026-05-06 after Guillermo same-day miss, second instance in 3 weeks).
- For each meeting without a current brief decision, ask "brief needed?" — Kay's yes triggers the `meeting-brief` skill for that meeting; no skips.
- **Friday rule:** On Fridays, the prompt must cover **today + Monday AND Tuesday**, not just Saturday. The weekend briefing is lighter and may not catch Monday meetings in time.
- **Sunday rule:** Cover today + Monday (standard).
- If Kay has already approved or declined a brief for the meeting in a prior session (check session-decisions files), do not re-ask. If approved and the brief does not exist, surface a broken-system item.
- **Last-minute meeting audit:** For the next few weeks, log any external meeting first seen inside the 48-hour window without an existing brief. If this happens repeatedly, recommend a coverage change such as a midday calendar delta check, calendar-change trigger, or Good Night next-48h brief sweep.

**Intermediary matches rule:** Daily broker listing matches from deal-aggregator are posted directly to #strategy-active-deals as individual Slack messages (one per deal, thumbs up/down reactions). Do NOT include individual match details in the morning briefing. The System Status line should only report: "deal-aggregator — {n} new lead matches posted to Slack".

**Routing pre-existing report sections into urgency-tagged Decisions:**
- *Pipeline shifts* (Attio stage changes, new active deals, NDA-signed detections) → 🔴 if action-needed today, 🟡 if review-needed-soon. Always Obama framing.
- *Pipeline summary stats* (Active Deals N, niche counts) → omit from briefing; lives on Active Deal Pipeline + M&A Analytics dashboard pages.
- *To Do action steps* → 🔴 (same-day) or 🟡 (this week).
- *Gmail drafts ready for Kay review* → 🔴 as a single bundled Decision: **RECOMMEND: Review N draft(s) Mon AM** → YES/NO/DISCUSS. Never ask Codex to send or schedule-send. Not one item per draft.
- *Targets for review* → 🟡 Decision (warm intro vs cadence vs pass) — bundle by niche.
- *Brief needed for TODAY (D+0) or TOMORROW (D+1) external meetings* → 🔴 Decision: **RECOMMEND: Generate brief for {name}** → YES/NO/DISCUSS (mandatory invariant per CLAUDE.md brief-decisions pre-flight + `feedback_preflight_covers_today_and_tomorrow.md`).
- *Aging deferrals (≥5 days)* → 🟢 Decision: **RECOMMEND: {kill/do-now/re-defer}** → YES/NO/DISCUSS.
- *Broken scheduled skill or stuck snapshot job* → 🔴 Decision: **RECOMMEND: Investigate {job} (last log {timestamp})** → YES/NO. Don't bury silent failures.
- *On deck for cold calls tomorrow* → **Today / ASAP** the day before only (per cold-call "On Deck" timing rule below).
- *Today's calendar/agenda* → 1-line tail above System Status, not its own bucket.

**Targets for Review rules:**
- This section surfaces targets from target-discovery's auto-advance system that need Kay's decision. Two categories only:
  1. **Warm intro targets** — warm-intro-finder found a connection path (via Attio, vault, Gmail, Kay's network). Kay decides: "draft" (create a Gmail draft for her personal outreach) or "cadence" (prepare draft-only follow-up cadence for Kay review).
  2. **Edge case targets** — borderline on buy box/ICP criteria (borderline size, geography, unclear ownership, possible PE backing). Kay decides: "approve" (route to draft-only outreach + cold call list based on channel) or "pass" (move to Passed tab on tracker).
- **Auto-approved targets do NOT appear here.** Targets that passed all buy box + ICP criteria with no warm intro flow automatically route to draft-only Gmail outreach + the cold call list. Only exceptions surface.
- Group by niche when multiple niches are active. One header per niche.
- Kay responds with decisions per item: "1 draft, 2 approve" or "1 cadence, 2 pass"
- On Kay's decision:
  - "draft" → create Gmail draft via `gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send` for Kay's review
  - "cadence" → prepare draft-only Gmail follow-ups; Kay sends each draft manually
  - "approve" → route to Gmail drafts + cold call list based on channel
  - "pass" → move target to Passed tab on the tracker sheet

Each item numbered. Each has a clear action or question. No informational items without an ask. No items requiring deep review — those go to Slack.

**Cold-call "On Deck" timing rule:** Only show cold-call items the day BEFORE they are due. Not earlier. Example: if Freedman Risk follow-up is due Thursday April 2, it appears in Wednesday April 1's briefing — not before. This prevents noise and keeps Kay focused on what's actionable today/tomorrow only.

After Kay reviews all three categories, confirm summary:
```
Pipeline manager complete:
- {n} pipeline stages updated
- {n} rows appended to To Do
- {n} draft-only emails in Gmail for Kay review
- {n} stale deals flagged
```

## Architecture: Manager + 2 Sub-Agents + 1 External Skill

Codex acts as the **manager** overseeing 2 specialized sub-agents that run in parallel on session start, plus reading an artifact from the relationship-manager skill. The manager:
- Launches both agents simultaneously
- Reads the relationship-status artifact from relationship-manager
- Reviews their outputs for quality and consistency
- Flags any red flags or conflicts to Kay before presenting
- Presents recommendations sequentially: Part 1 (pipeline changes) → Part 2 (outreach/nurture) → Part 3 (action items)
- Executes approved changes
- Runs stop hooks to validate execution

### Sub-Agent 1: Pipeline Agent
**Scope:** Active Deals and Investor Lists
**Scans:** Email (NDAs, financials, LOIs, broker correspondence, CIM attachments), calendar (deal meetings), vault (call notes), Drive ACTIVE DEALS folder (new subfolders)
**Returns:** Stage change recommendations with signal evidence. Also executes CIM auto-trigger (folder creation, filing, inbox item, deal-eval invocation) before returning recommendations — CIM deals arrive pre-screened.

**Pipeline Agent Quality Gates (CRITICAL):**

1. **Name resolution required.** Every pipeline entry presented to Kay MUST include the company/person name, not just a record ID. If the Attio API does not return a name for a record, try: (a) `mcp__attio__get_record_details` with the record ID **— or REST `curl -s -H "Authorization: Bearer $ATTIO_API_KEY" https://api.attio.com/v2/objects/{object}/records/{record_id}`**, (b) `mcp__attio__search_records` by record ID **— REST: `POST /v2/objects/{object}/records/query` with `{"filter":{"id":"{record_id}"}}`**, (c) cross-reference against the outreach tracker Google Sheet. If name STILL cannot be resolved, do NOT present the entry as a recommendation — log it as "unresolvable" and flag for investigation. Kay cannot act on nameless entries.

2. **Calendar day verification.** When presenting "today's agenda" items, verify the day of week matches. Cross-check: `date +%A` returns today's day name. Only include events from TODAY's calendar query in the "today's agenda" section. Events from yesterday's scan go in "pipeline signals" only. Events from tomorrow go in "upcoming" only. Never mix days.

3. **No unactionable items.** Every item presented to Kay must have: a name, a clear action or question, and enough context to decide. If any of these is missing, the subagent must resolve it before returning results — or exclude the item.

**ACTIVE DEALS folder detection (catch-all for broker platform NDA edge cases):**
Scan the ACTIVE DEALS Drive folder for any subfolder that does not have a matching Attio Active Deals entry. This catches the case where Kay signs an NDA on a broker platform (no email sent), creates a folder, and saves the NDA manually. When detected:
1. Create Attio Active Deals entry at "NDA Signed" stage with `source: intermediary`
2. Create entity in vault if needed
3. File any documents in the folder into the standard subfolder structure
4. Present in morning briefing: "New deal folder detected: {Company}. Created Attio entry at NDA Signed."

### Sub-Agent 2: Relationships (now relationship-manager skill)
Relationship management (nurture cadence monitoring, action-already-taken verification, overdue contacts, People record updates) is now handled by the relationship-manager skill. It writes an artifact to `brain/context/relationship-status-{date}.md` that pipeline-manager reads for Section 3 of the morning briefing.

**Fallback:** If the relationship-status artifact doesn't exist (relationship-manager didn't run), pipeline-manager does a lightweight Attio People query to surface any contacts with overdue nurture cadences for the briefing. This fallback will be removed once relationship-manager is proven stable.

### Sub-Agent 3: Post-Call Task Handoff
**Scope:** fresh staged task files from `post-call-analyzer` for the prior 24 hours.
**Reads:** `brain/trackers/post-call-analyzer/pending-tasks/*.json`, filtered by `staged_at`, `call_date`, source call timestamp, or file mtime to the prior 24 hours for routine Good Morning.
**Does not scan:** Granola MCP, Granola OAuth, local browser cache, or raw transcript sources.
**Returns:** proposed To Do rows with source meeting, task text, type, project, suggested timing, analysis Doc link, and transcript Doc link.

If no fresh pending task files exist, return "No fresh staged post-call tasks". Older pending files should be summarized as backlog only, not expanded into the briefing.
If any file is malformed, surface a single RED system item:
`RECOMMEND: Repair malformed post-call task handoff — {filename} could not be parsed.`

### Stop Hooks (post-execution validation)
1. **Pipeline validation** — confirms all approved stage changes were executed in Attio Lists
2. **Relationships validation** — confirms all approved People attribute updates were executed, no blank next_actions left behind
3. **Post-call staged-task validation** — for each pending task file presented to Kay, verify approved tasks were appended to the To Do tab before moving the file to `pending-tasks/processed/`. Files with NO/DISCUSS outcomes must be archived with an explicit declined/deferred marker or left pending, respectively. Never delete a pending task file silently.
4. **Gmail ingestion validation** — count actionable emails identified during ingestion vs inbox files written to `brain/inbox/`. Every actionable email must have a corresponding file (or an idempotency skip logged). Mismatch = dropped action items.
5. **Task-tracker validation** — for every approved action item (outreach tasks, follow-up tasks, Granola action items), verify it was appended to the To Do tab. Resolve the current week's sheet ID dynamically: `SHEET_ID=$(python3 /home/ubuntu/projects/Sapling/scripts/tracker_sheet_resolver.py --print-id)`, then read the To Do tab on that sheet and compare approved count vs appended-row count. Mismatch = tasks Kay thinks exist but don't.
6. **Niche signal validation** — if any niche signals were detected during data ingestion, confirm each was written to `brain/inbox/` with the `topic/niche-signal` tag. Glob `brain/inbox/*niche-signal*` and verify count matches signals detected. Missing signals = lost intelligence for Friday's niche run.
7. **Slack notification validation** — confirm the Slack webhook POST returned HTTP 200 OK. If non-200, retry once. If still failing, warn Kay directly in the session summary that Slack notification failed.
8. **ACTIVE DEALS folder sync** — compare ACTIVE DEALS Drive subfolders against Attio Active Deals entries. Every folder must have a matching Attio entry. Any orphaned folder = missed deal entry. Create Attio entry and flag in morning briefing.
9. **CIM auto-trigger validation** — for every CIM detected during Gmail ingestion, verify all 4 steps completed: (a) ACTIVE DEALS folder exists with CIM/ subfolder, (b) CIM file uploaded to CIM/ subfolder with size > 0, (c) inbox item written to `brain/inbox/` with `urgency: critical` and `topic/cim-received` tag, (d) deal-evaluation was invoked with `source: intermediary-inbound`. If any step failed, retry once. If still failing, flag in morning briefing: "CIM auto-trigger incomplete for {company} — {which step failed}." A missed CIM is a missed deal.
10. **Attio-Target Sheet Reconciliation** — after the morning scan completes, compare Attio Active Deals stages against target sheet outreach columns for all active targets. Use col-lookup.py to resolve header names to cells (never hardcode column letters):
   - For each Attio entry at "Identified": check target sheet "Day 0 Sent" column. If sheet has a date → MISMATCH. Auto-advance Attio to "Contacted" and log.
   - For each Attio entry at "Contacted": if cold-call status = "Connected" + positive sentiment → MISMATCH. Flag for review (potential First Conversation).
   This reconciliation runs as a safety net — it catches drift that the real-time detection missed.

11. **Outbound-email → Active Deals list-entry coverage (added 2026-04-15)** — for every outbound email to an external recipient in the past 14 days, verify an Attio Active Deals list entry exists for that recipient's company. Iterate:
   - Get all outbound emails: `gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:14d" --json --max 100 --account kay.s@greenwichandbarrow.com --gmail-no-send`
   - For each unique external recipient: find Person → find Company → verify list entry exists
   - If missing: auto-create list entry at "Contacted" stage (per Outbound Email Scan Path B). Flag in morning briefing.
   Root cause: Attio auto-creates People from email but NOT list entries. This hook closes the gap (Timothy Wong / MMPC 2026-04-09 incident).

### Email Scan Results Validation (post-ingestion)
After Gmail ingestion completes and `brain/context/email-scan-results-{date}.md` is written, validate:

- [ ] **File exists and is non-empty** — `brain/context/email-scan-results-{YYYY-MM-DD}.md` must exist and contain content beyond just frontmatter
- [ ] **Required sections present** — file contains ALL of these section headers:
  - `## Actionable Items Created`
  - `## Deal Flow Classified`
  - `## Draft Status`
  - `## Introductions Detected`
  - `## Niche Signals`
  - `## In-Person Meetings`
- [ ] **Sections populated or explicitly empty** — each section must have either item entries or an explicit "None" / "No items" marker. A missing section header means the ingestion skipped that scan entirely, which is a bug.

If any section is missing, re-run the corresponding ingestion step (e.g., missing Draft Status → re-run Gmail draft check). If the file doesn't exist at all, the entire Gmail ingestion failed — log error and retry once before alerting Kay.

### Manager Red Flags
The manager raises these to Kay before executing:
- Conflicting signals (email says deal killed but calendar shows meeting scheduled)
- Missing data (meeting happened but no Granola transcript and no call notes)
- Unusual patterns (deal jumping 2+ stages, contact going from Dormant to active without clear signal)
- Sub-agent returned empty results when activity was expected

### Manager Quality Review (CRITICAL — runs before presenting to Kay)

Before presenting the briefing, the manager (Codex orchestrator) MUST review all sub-agent outputs for these errors:

1. **Nameless entries** — Any pipeline recommendation without a resolved company/person name is REJECTED. Do not present it.
2. **Wrong-day calendar items** — Cross-check every "today" item against the actual day of week. Remove any misfiled items.
3. **Imprecise characterizations** — Compare sub-agent summaries of email actions against the email-scan-results artifact. If the sub-agent says "cancelled" but the artifact says "downgraded", use the artifact's language.
4. **Stale items without names** — "8 entries stale for 17 days" is useless without company names. Either resolve names or don't present the stat.
5. **Relationship items already handled** — Cross-check relationship-manager artifact's overdue contacts against Attio `next_action` for trigger-based conditions. Filter out trigger-based contacts before presenting.
6. **Session decisions from prior day** — Read `brain/context/session-decisions-{previous-workday}.md`. Cross-reference all recommendations against it:
   - **Suppress** items that were PASS'd or had action confirmed (SENT/CREATED/UPDATED)
   - **Verify** items that were APPROVE'd but have no action recorded — surface as: "You approved X yesterday — was it completed?"
   - **Honor deferrals** — DEFER'd with a date → suppress until that date. DEFER'd with a trigger condition → suppress until the trigger is detected in today's signals.
   - **Carry forward open loops** — items in the Open Loops section should appear in the briefing unless resolved by today's scans.
   - **Deferral aging (NEW)** — Scan ALL session-decisions files from the last 14 days (not just yesterday) for DEFER entries. For each DEFER item still open (not marked SENT/CREATED/UPDATED in any later file):
     - **Age calculation:** days since the DEFER was first logged.
     - **< 5 days old:** suppress (respect the defer).
     - **≥ 5 days old:** surface in a new briefing section titled **"Aging deferrals"** with: item name, age in days, original trigger/reason, and a forcing question: "Kill, do now, or re-defer with new trigger date?"
     - **≥ 10 days old and no trigger condition specified:** flag as RED (bold) — Kay must decide, no third defer allowed without explicit new trigger date.
     - **Exception:** Items with an absolute future date (e.g., "~Apr 20") stay suppressed until that date regardless of age.
     - **Purpose:** Prevent the DEFER pile from accumulating indefinitely (observed Apr 2026: Mark Gardella reply 7 days stale, Philip Hoffman 9+ days, broker platform registrations chronic). Aging forces triage.

The manager is the last line of defense. Sub-agents will make errors. The manager catches them so Kay doesn't have to.

### Briefing Format Stop Hooks (CRITICAL — runs immediately before output)

Before sending the briefing to Kay, validate against the dashboard-section spec:

- [ ] **Required sections present in order** — Email Orchestration, Active Pipeline, Deal Aggregator, C-Suite & Skills, System Health, Meeting Briefs, Tasks & Follow-up, then Decisions Needed only if needed.
- [ ] **Each main section has Kay-actionable numbered items or `N/A`** — no report dumps, no missing section headers. One operational-status line per section max, only for freshness/trust. Tasks & Follow-up may include a task-count line, but must not repeat existing To Do rows.
- [ ] **All referable lines are numbered sequentially across the whole brief** — includes ops/freshness lines and Kay-actionable items; numbering never resets by section; main section headers are flush left, and numbered lines default to `N. **Dashboard subsection:** item`. Use expanded subsection headers only for subsections with 2+ separate decision items; sub-items use roman numerals or letters.
- [ ] **Dashboard subsections reflected exactly** — Email Orchestration uses only 24-hour thank-yous, 48-hour follow-ups, and EOW follow-ups. Drafts appear only inside those buckets with concrete context; deal-flow email appears only in Deal Aggregator.
- [ ] **Active Pipeline is grouped by stage and excludes closed deals** — surface only active, non-closed deals; closed deals appear only if changed in the current session.
- [ ] **Deal Aggregator references one morning run** — do not combine or overwrite with retired afternoon/Friday digest output.
- [ ] **System Health is failure-only** — include only RED/YELLOW failures that would merit Slack/system alerting; otherwise `N/A`. Planned dashboard plumbing and non-failure operating work belong in Tasks & Follow-up.
- [ ] **Meeting Briefs covers the brief-prep window** — next 48 hours, plus Friday/Sunday exceptions, with missing approved briefs surfaced as broken-system items.
- [ ] **Decisions cap ≤5 items** — include only actual approvals/questions; use Obama framing and C-suite ownership labels.
- [ ] **No completed-or-resolved items** — cross-check session-decisions for SENT/CREATED/UPDATED/PASS verbs and suppress per `feedback_briefing_no_done_items`. Never report back Kay's own work.
- [ ] **No noise section** — true low-value items are archived silently, never surfaced.
- [ ] **Every surfaced item has a status, action, or ask for Kay** — no ambiguous fragments and no back-end operational narration unless it affects trust/freshness.
- [ ] **Bundled approvals where possible** — multiple email drafts/tasks ready for Kay review → one bundled approval, not one item per draft/task.

If any check fails, fix in-line before sending. Do not present a malformed briefing and ask Kay to forgive it.

## Data Ingestion (runs before signal detection)

Before scanning for signals, ingest new data from external tools into the vault. The vault is the single source of truth.

### Post-call analyzer → brain/calls/ + staged task artifacts
Pipeline-manager does not ingest Granola directly. Before signal detection:

1. Read recent `brain/calls/*.md` written by `post-call-analyzer`.
2. Read `brain/trackers/post-call-analyzer/pending-tasks/*.json` for review-ready action items, filtering routine Good Morning output to post-call task batches from the prior 24 hours.
3. Verify the post-call analyzer validator is clean if call artifacts look stale:
   `python3 scripts/validate_post_call_analyzer_integrity.py`
4. If expected call artifacts are missing, surface a system item to repair
   `post-call-analyzer`; do not query Granola MCP/OAuth from pipeline-manager.

### Gmail Draft Status Check
Check Gmail for the status of outreach drafts created by outreach-manager. Use `gog gmail drafts list --account kay.s@greenwichandbarrow.com --gmail-no-send`, Gmail search with the same guard, and the sent folder to determine whether Kay sent them manually.

Results from this check feed directly into the **Draft Status** section of `brain/context/email-scan-results-{YYYY-MM-DD}.md` (see Email Scan Results Artifact below).

1. Query Gmail drafts and recently sent emails matching known outreach targets
2. For each draft that was sent:
   - Update Attio: move target from "Identified" to "Contacted" (source: Gmail sent folder scan + target sheet "Day 0 Sent" column)
   - Log the sent date in the email-scan-results artifact
3. For drafts still unsent, flag with escalating urgency:
   - **Thank-you drafts (time-sensitive):**
     - Unsent after 24 hours: "Thank-you to {name} still unsent. Approaching 48-hour window."
     - Unsent after 48 hours: "Thank-you to {name} is 48+ hours old. Send today or it loses impact."
   - **Outreach drafts (less urgent):**
     - Unsent after 2+ business days: "{n} outreach drafts unsent in Gmail. Review and send?"
4. For any replies detected (responses to outreach emails):
   - Flag as high-priority pipeline signal
   - Recommend stage change based on reply content

This is how the system knows Kay sent the email and triggers the Attio stage advancement. Codex may prepare follow-up drafts (Day 3/14 follow-ups drafted each morning), but Kay sends manually. Cold call lists are managed independently by cold-call-operations.

### Outbound Email Scan (catches manually-sent emails + auto-creates missing Active Deals entries)

The Gmail Draft Status Check above only catches emails that originated as outreach-manager drafts. Kay also sends emails manually, forwards from another thread, or replies inline. These must also trigger pipeline stage changes.

**CRITICAL (added 2026-04-15 after Timothy Wong / MMPC gap):** Attio auto-creates **People records** from email interactions, but does NOT auto-create **Active Deals list entries**. If an outbound email's recipient has a Person record but no Active Deals list entry, this scan must CREATE the list entry — not just skip them. The scan is a reconciler-and-creator, not a read-only updater.

1. Query Gmail for all outbound emails (extended window for slow-reply cold-call follow-ups):
   ```bash
   gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:14d" --json --max 100 --account kay.s@greenwichandbarrow.com --gmail-no-send
   ```
2. For each sent email, extract the recipient address(es) and cross-reference against Attio:
   - First: find the Person record (Attio auto-creates these on first email interaction — always exists for any recipient Kay has emailed)
   - Then: check if that Person's associated Company has an **Active Deals list entry**
3. **Path A — List entry EXISTS and matches:**
   - If entry is at "Identified" → move to "Contacted"
   - If entry is at "Contacted" or later → no stage change; log sent date only
4. **Path B — Person exists but NO list entry (the Timothy Wong gap):**
   - Create new Active Deals list entry at "Contacted" stage
   - Infer niche from target sheet match (`{Niche} - Target List` sheets in LINKT TARGET LISTS folder); tag accordingly
   - Flag in morning briefing: "Auto-created Active Deals entry for {Company} at Contacted (outbound email detected, prior list entry missing)"
5. **Path C — No Person record and no list entry:**
   - This shouldn't happen (Attio auto-creates People from email) but if it does, create both
6. **Deduplication:** Skip any recipient already captured by the Gmail Draft Status Check above. Use the recipient email as the dedup key.
7. **Scope:** Only process emails sent to external recipients. Ignore internal emails (to @greenwichandbarrow.com addresses).
8. **Log cross-reference source:** Every created entry records `source: manual-outbound-email` with the message ID for audit trail.

This ensures manually-sent outreach emails (not just outreach-manager drafts) trigger the Attio stage change AND create list entries when missing. Codex may prepare follow-up cadence drafts for all targets; Kay sends manually.


### Cadence Advancement (runs during morning scan)

The target sheet is the source of truth for outreach cadence status. Codex manages cadence tracking via per-touchpoint date columns on the target sheet. Pipeline-manager reads these columns to detect cadence progression. All column references use header names resolved by col-lookup.py — never hardcoded letters.

**Outreach tracking columns (one date per touchpoint, never overwritten):**
- "Variant" — A or B (set once at Day 0)
- "Day 0 Sent" — date Day 0 email was sent
- "Day 3 Sent" — date Day 3 follow-up was sent
- "Day 6 DM Sent" — date LinkedIn DM was sent
- "Day 14 Sent" — date Day 14 final email was sent
- "Cadence Status" — Active / Complete / Replied

For each approved target ("Kay: Decision" = "Approve"), check target sheet date columns + Gmail sent folder:

1. **Email send detection:** Read "Day 0 Sent" column + Gmail sent folder scan.
   → If Day 0 sent: advance Attio from Identified to Contacted

2. **Follow-up emails:** Codex drafts Day 3/14 follow-ups in Gmail each morning. Pipeline-manager checks "Day 0 Sent" / "Day 3 Sent" dates to identify targets due for follow-up based on business days elapsed.

3. **Reply detected (any stage):** If inbound email from target detected in Gmail:
   → Update Attio to "Engaged", set "Cadence Status" to "Replied" on target sheet
   → Advance Attio stage as appropriate (Contacted → First Conversation if reply is substantive)
   → Flag in briefing as high-priority pipeline signal

4. **Cadence complete (no response):** If "Day 14 Sent" has a date and no reply after 7 business days:
   → Present: "{owner} at {company} — cadence complete, no response. Move to nurture?"

### New Approval Detection

For each row where "Kay: Decision" = "Approve" and "Day 0 Sent" is blank (no cadence started):
→ These are newly approved targets. Signal outreach-manager to draft initial outreach in Gmail.
→ Present in briefing: "{n} new approvals on {niche} target list. Outreach drafts queued."

### Conference Decision Scan
Conference decisions (Col M = "Attend"/"Register Only") are now handled by conference-discovery. Pipeline-manager does not scan the Conference Pipeline sheet.

### Target List Monitoring (Cold Call Outcomes)
Read the active niche sprint's master sheet ("{Niche} - Target List") in LINKT TARGET LISTS folder. Scan cold-call outcome columns for new entries since last scan:
- New "Connected" + "Interested" → move Attio from "Contacted" to "First Conversation"
- New "Connected" + "Not Selling" → flag for Kay's review (keep or kill?)
- New "Voicemail" → no stage change, note logged
- New "Wrong Number" → flag data quality issue
- New "Not Interested" → move to "Closed / Not Proceeding" or flag for Kay

### Niche Sprint Status Tracking

Niche sprints have 4 active states tracked on the Industry Research Tracker:

| Status | Meaning | Target Discovery Volume | Outreach |
|--------|---------|------------------------|----------|
| Under Review | Niche identified, one-pager and scorecard in progress. | None | None |
| Active-Outreach | Full owner outreach active. | 4-6 targets/day | Draft-only cadence prepared in Gmail; Kay sends manually |
| Active-Long Term | Niche winding down, finishing existing pipeline. | No new targets | Complete existing cadences only |
| Tabled/Killed | Sprint stopped. | None | None |

New niches go straight from Under Review to Active-Outreach when Kay approves. No intermediate validation gate. Customer validation happens organically through owner conversations and deal flow, not as a separate phase.

Multiple niches can be in different states simultaneously.

### Post-Meeting Niche Status Cleanup Triggers

When Kay changes a niche status during a session (e.g., approves a niche to Active-Outreach, tables or kills a niche), pipeline-manager fires downstream cleanup immediately -- not deferred to the next morning run:

1. **Sort tracker** -- Re-sort the WEEKLY REVIEW tab so active niches are at the top, Tabled/Killed at the bottom
2. **Move Drive folders** -- Move the niche's folder to the appropriate parent (ACTIVE SPRINTS for Active-Outreach, ARCHIVE for Tabled/Killed)
3. **Fire downstream skills:**
   - Active-Outreach approved --> trigger target-discovery for that niche (begins building target list)
   - Tabled/Killed --> cancel any pending target-discovery runs, stop outreach-manager drafts for that niche
   - Active-Long Term --> stop target-discovery, let existing outreach cadences complete

### Cold Call Daily Prep

Cold call prep, Call Log creation, 10am Slack delivery, and post-shift outcome harvesting are now handled by cold-call-operations. Pipeline-manager reads cold-call outcomes from the master target sheet for stage change signals (e.g., "Connected + Interested" triggers First Conversation recommendation in the morning briefing).

### Warm Intro Detection
When processing new targets (from target-discovery handoff), scan for warm intro paths before presenting to Kay:
- Search Attio People records for connections to the target's company or owner
- Search vault entities for any prior mentions
- Search Gmail for any prior correspondence with the company or person
- If a warm path exists, flag it: "Warm intro possible via {contact name} — {how connected}"

This replaces the previous approach where Kay manually flagged warm intros. The agent does the research, Kay just sees the result.

### Gmail → brain/inbox/
1. Query `gog gmail search "newer_than:2d label:INBOX" --json --max 50 --account kay.s@greenwichandbarrow.com --gmail-no-send` for recent inbound emails (outbound scanning is handled separately by the Outbound Email Scan step above)
2. Parse for actionable items: explicit requests, questions, deadlines, documents needing action
3. Check idempotency: if `source_ref` (message ID) already exists in brain/inbox/, skip
4. Write to `brain/inbox/YYYY-MM-DD-{slug}.md` using inbox schema (schemas/vault/inbox.yaml)
5. Set `source: email`, assign confidence level (high/medium/low)
6. High confidence items surface in Part 1. Medium/low go to /triage.

### Deal Flow Email Classification (absorbed from deal-aggregator Channel 2)

During Gmail ingestion, every email labeled "DEAL FLOW" must be classified as one of three categories. Classification counts (DIRECT/BLAST/NEWSLETTER) are written to the email-scan-results artifact for downstream consumption.

1. **BLAST** — BCC'd distribution, generic greeting, "New Listing" subject, sent to broker's full network of 3000+. Agent screens against buy box. **Revenue floor (auto-reject):** Any deal with stated revenue below $1.5M is auto-rejected regardless of industry fit or broker relationship — archive silently, do not flag, do not Slack, do not surface. These are too small. Remaining deals above the revenue floor are screened against active thesis criteria and the financial buy box ($1-5M EBITDA, $3-20M revenue, independently owned). Matches → Slack ping to #active-deals. No match → archive silently. Kay never sees BLAST emails unless there's a match above the revenue floor that passes the buy box.

2. **DIRECT** — Addressed to Kay by name, references prior conversation or specific criteria Kay shared, expects a response, may include "Introduction" or "RE:" in subject, sometimes has CIM/teaser attached. These ALWAYS get surfaced to Kay — never auto-archived. Present in morning briefing via Inbound Intermediary Deal Detection flow.

3. **NEWSLETTER** — Industry newsletters, deal roundups, educational content (e.g., Helen Guo / SMB Deal Hunter). Not actionable deal flow. Move to a "DEAL FLOW/ARCHIVE" label. Scan for niche signals only — patterns in what industries are being listed, new niche ideas.

**Pattern detection for classification:**
- BCC header present → BLAST
- Kay's name in greeting ("Hi Kay", "Dear Kay") + personalized context → DIRECT
- Unsubscribe link + no personalization → NEWSLETTER or BLAST
- Sender has prior reply in Gmail thread history + personalized → DIRECT
- Sender not in Attio + mass-email patterns → BLAST

**Guardrail:** When uncertain, default to DIRECT. It's better to surface an email Kay doesn't need than to archive one that needed a response.

### Email Scan Results Artifact

After Gmail ingestion completes (including deal flow classification and Gmail draft status check), write a structured results file so downstream skills (e.g., /start, deal-aggregator) can read email findings without re-scanning Gmail.

**Location:** `brain/context/email-scan-results-{YYYY-MM-DD}.md`

**Format:**
```yaml
---
date: YYYY-MM-DD
scan_timestamp: ISO-8601
emails_scanned: N
---
```

```markdown
## Actionable Items Created
- brain/inbox/YYYY-MM-DD-{slug}.md (source_ref: msg:{id})
- brain/inbox/YYYY-MM-DD-{slug}.md (source_ref: msg:{id})

## Deal Flow Classified
- DIRECT: {count} emails surfaced
- BLAST: {count} archived
- NEWSLETTER: {count} archived

## Draft Status
- Sent: {list of targets where draft was sent, with sent date}
- Unsent: {list with age in days since draft creation}

## Introductions Detected
- {introducer} -> {person} at {company}

## Niche Signals
- {signal} -> brain/inbox/YYYY-MM-DD-niche-signal-{slug}.md

## Draft Calibration (draft vs sent diffs)
{For each email where both a Gmail draft AND a matching sent email exist:}
- **{recipient} — {subject}**
  - Draft: {first 2 lines of original draft}
  - Sent: {first 2 lines of what Kay actually sent}
  - Edits: {summary of changes — tone, length, phrases added/removed, structure}
{If no draft-vs-sent pairs found: "No draft calibration data today."}
```

**Draft Status population:** The Gmail Draft Status Check AND the Outbound Email Scan (see sections above) both feed this section. For each outreach or thank-you draft created by outreach-manager or pipeline-manager:
- Check Gmail sent folder via `gog gmail search ... --account kay.s@greenwichandbarrow.com --gmail-no-send` for matching sent emails
- If sent: record target name, company, and sent date
- If unsent: record target name, company, and age in days since draft was created

For each manually-sent email detected by the Outbound Email Scan that matched an Attio Active Deals entry:
- Record target name, company, sent date, and note "(manual — not from draft)"
- This gives downstream skills (and Kay's morning review) a single place to see what was sent vs. pending without re-querying Gmail.

This artifact is the handoff contract between pipeline-manager (which scans Gmail and checks Gmail) and downstream consumers (/start, deal-aggregator). They never scan Gmail directly — they read this file.

### Active Deal Fast-Path (PRIORITY — runs during Gmail ingestion)

**Before standard inbox processing**, check every email against Active Deals in stages 3-9 (First Conversation through LOI Signed). Match by company name, contact name, or intermediary firm.

**If an email matches an active deal:**
1. **Tag as `urgency: critical`** — this is not a standard inbox item
2. **Identify what was received:** CIM, financials, LOI draft, NDA response, broker follow-up
3. **File to Drive immediately:**
   - Download any attachments from the email
   - Upload to the correct subfolder in `ANALYST / ACTIVE DEALS / {COMPANY} /` — **ALWAYS check if subfolder exists before creating** (`gog drive ls --parent {folder_id} --json` and check for matching name). Only create if it doesn't exist. Never create duplicates.
4. **Update Attio stage** based on what was received:
   - CIM/financials received → move to "Financials Received"
   - LOI response → move to appropriate LOI stage
   - Other correspondence → no stage change, just log
5. **Send immediate Slack ping to #active-deals:**
   ```
   Active Deal Update: {Company Name}
   {What was received} from {sender}. Filed to Drive.
   Attio updated: {old stage} → {new stage}
   File: {drive link}
   Deal folder: {folder link}
   ```
6. **Auto-trigger deal-evaluation:** After filing, invoke `/deal-evaluation {company name}` which will detect the current state (financials in folder) and pick up at the right phase (Phase 3 for CIM/financials, Phase 5 for LOI response).

**Validation (MUST pass before Slack ping):**
```
checks = {
    "file_in_drive": verify file exists in correct subfolder (ls the folder, confirm filename),
    "no_duplicates": verify only ONE subfolder of each type exists (no CIM + CIM(1)),
    "attio_updated": verify Attio entry stage matches the expected new stage,
    "attachment_size": verify uploaded file size > 0 (not an empty/corrupt upload),
}

If any check fails → DO NOT send Slack. Fix the issue, re-validate, then send.
```

**This fast-path ensures:**
- Active deal documents are filed same-day, not queued for Monday
- Attio reflects reality in real-time
- Kay gets a Slack ping only after verified filing
- Deal evaluation begins automatically — no manual invocation needed
- Brokers see fast response times, which signals seriousness

### Inbound Introduction Detection
During Gmail ingestion, detect introduction emails — someone introducing Kay to a new person/company. Signals:
- Subject contains "introduction", "intro", "meet", "connecting you with", "wanted to introduce"
- Email has 3+ recipients (introducer + Kay + new person)
- Body mentions a company name + person name Kay hasn't corresponded with before

**For each detected intro:**
1. Extract: introducer name, new person name, new person's company, new person's email, context given by introducer
2. Create vault entity at `brain/entities/{slug}.md` for the new person
3. Create vault entity for their company if it doesn't exist
4. Add to the active niche sprint master sheet with Source = "Intermediary Referral"
5. Add to Attio Active Deals at "Identified" with `how_introduced: "Intro from {introducer name}, {date}"`
6. Flag in Kay's morning pipeline review: "New intro received from {introducer} to {person} at {company}. Added to target list. Draft warm intro response?"
7. If Kay approves, outreach-manager drafts a warm intro email (different framing than cold — leads with the connection: "So-and-so suggested I reach out")

**Key difference from cold targets:**
- Warm intro email references the introducer by name
- Skips cold-call confirmation call — the intro IS the warm touch
- Higher priority than cold targets in the daily review
- Also draft a thank-you email to the introducer

**Cadence for warm intros:**
| Day | Channel | Action |
|-----|---------|--------|
| Day 1 | Email (Gmail) | Warm intro email referencing introducer |
| Day 1 | Email (Gmail) | Thank-you to introducer |
| Day 5-6 | Email (Gmail) | Follow-up if no response |
| Day 8-10 | LinkedIn DM (Kay) | High-value only |

No Day 3 cold call. The introducer already warmed the connection.

## Inbound Intermediary Deal Detection (runs during Gmail ingestion)

During Gmail ingestion, detect inbound deal flow from intermediaries — brokers, lawyers, CPAs, wealth advisors, M&A advisors, and other referral sources who send deals to multiple buyers. Speed is critical: these people shop deals simultaneously, and a fast response wins.

### Detection Signals
Scan incoming emails for:
- CIMs, teasers, deal summaries, or blind profiles attached or inline
- Subject lines containing: "opportunity", "deal flow", "confidential opportunity", "teaser", "investment opportunity", "acquisition opportunity", "company for sale", "business for sale"
- Body language: revenue/EBITDA figures, asking price, "under NDA", "exclusive mandate", "we represent"
- Attachments: PDFs named with CIM/teaser/profile/summary patterns
- Sender domain matches known intermediary patterns (advisory firms, brokerage firms, law firms)

### Sender Classification
1. **Check vault + Gmail history** — does the sender (or their firm) have a prior entity record or prior email correspondence with us?
   - If yes: tag as `source/intermediary-inbound`, associate with existing entity
   - If no: create a new entity at `brain/entities/{slug}.md` (an inbound deal email IS a reply, so an entity is warranted). Per `feedback_brokers_stay_in_sheet_until_reply`: cold intermediaries live in the broker target Sheet pre-reply; an inbound email crosses that threshold, so Attio People auto-creation via Gmail interaction is acceptable. Do NOT add the sender to any deleted Intermediary Pipeline list.
2. Cross-reference sender against vault entities and Gmail history for prior correspondence

### Inbox File Creation
Write each inbound deal to `brain/inbox/YYYY-MM-DD-intermediary-inbound-{slug}.md` using inbox schema with:
- `tags: [inbox, source/intermediary-inbound, person/{intermediary-slug}, company/{intermediary-firm-slug}]`
- `confidence: high` (explicit deal flow is always actionable)
- `source: email`
- Body: intermediary name, intermediary firm, deal summary (company description, industry, revenue/EBITDA if stated, geography), any attachments listed

### CIM Auto-Trigger (same-day fast-track — runs before morning review)

When the inbound deal detection finds a CIM attachment or CIM-level content (not just a teaser or blind profile), skip the morning review queue and fast-track immediately. Active deal signals get same-day treatment.

**CIM detection criteria** — email must match at least ONE:
- Attachment filename contains: `CIM`, `Confidential Information Memorandum`, `confidential-information-memorandum`, `offering-memorandum`, `information-memorandum`
- Attachment is a PDF/DOCX > 5 pages (teasers are typically 1-2 pages; CIMs are 20+)
- Email body or subject contains the phrase "Confidential Information Memorandum" or "CIM attached"
- Email body contains structured financials (revenue + EBITDA + multiples) AND a company name (not a blind profile)

**Also detect adjacent deal documents** with the same logic:
- Keywords: `teaser`, `investment opportunity`, `deal summary`, `offering memorandum`, `executive summary`, `company overview`
- These are lower-confidence but still trigger the fast-track if from a known intermediary (Attio Person record exists OR prior outbound logged in Gmail/broker target Sheet history)

**When CIM is detected, execute all 4 steps automatically:**

**Step 1: Create/find ACTIVE DEALS folder**
```bash
# Check if company folder already exists
gog drive ls --parent {ACTIVE_DEALS_FOLDER_ID} --json | grep -i "{company_name}"

# If not found, create it with standard subfolder structure
gog drive mkdir "{COMPANY NAME}" --parent {ACTIVE_DEALS_FOLDER_ID}
gog drive mkdir "CIM" --parent {new_company_folder_id}
gog drive mkdir "FINANCIALS" --parent {new_company_folder_id}
gog drive mkdir "LEGAL" --parent {new_company_folder_id}
gog drive mkdir "DILIGENCE" --parent {new_company_folder_id}
gog drive mkdir "CORRESPONDENCE" --parent {new_company_folder_id}
```

**Step 2: File the CIM**
```bash
# Download attachment from email
gog gmail attachment {message_id} {attachment_id} --output /tmp/{filename} --account kay.s@greenwichandbarrow.com --gmail-no-send

# Upload to CIM subfolder
gog drive upload /tmp/{filename} --parent {cim_folder_id} --name "{filename}"
```
- Verify upload: `gog drive ls --parent {cim_folder_id} --json` — confirm file exists and size > 0
- If the CIM subfolder already has a file with the same name, do NOT overwrite. Append `_v2` and flag the duplicate in the inbox item.

**Step 3: Create inbox item**
Write to `brain/inbox/YYYY-MM-DD-cim-received-{company-slug}.md` using inbox schema:
```yaml
---
title: "CIM Received: {Company Name}"
date: YYYY-MM-DD
type: inbox
source: email
source_ref: "{gmail_message_id}"
confidence: high
urgency: critical
tags:
  - inbox
  - date/YYYY-MM-DD
  - source/intermediary-inbound
  - topic/cim-received
  - person/{intermediary-slug}
  - company/{intermediary-firm-slug}
  - company/{target-company-slug}
---

## CIM Received — {Company Name}

**From:** [[entities/{intermediary-slug}|{Intermediary Name}]] at [[entities/{intermediary-firm-slug}|{Firm Name}]]
**Company:** {Company Name}
**Industry:** {if stated}
**Revenue:** {if stated}
**EBITDA:** {if stated}
**Geography:** {if stated}

**CIM filed to:** [Drive link]({drive_link})
**Deal folder:** [Drive link]({folder_link})

**Status:** Auto-triggered deal-evaluation (intermediary-inbound pathway)
**Next:** Deal-eval buy-box screen running. Results in morning briefing.
```

**Step 4: Auto-invoke deal-evaluation**
Trigger deal-evaluation with:
- `source: intermediary-inbound`
- `intermediary: {intermediary name}`
- `company: {company name}`
- `cim_location: {drive_file_link}`

Deal-eval reads the CIM from Drive, runs the buy-box screen, and stages results for Kay's morning review. Kay sees the completed screen (not just a "should we screen?" prompt).

**Attio updates (parallel with deal-eval):**
- Create Attio Active Deals entry at "Financials Received" stage (CIM = financials) with `source: intermediary` — Active Deals list remains the canonical deal pipeline
- Create vault entity for the target company if it doesn't exist
- (Intermediary Pipeline list deprecated — no separate intermediary-stage update happens here)

**Step 5: Auto-ack reply to broker (BOTH-FIRE chain — added 2026-05-04)**
After Step 4 completes successfully, draft a reply email to the broker acknowledging CIM receipt and setting a review-window expectation. **MANDATORY — copy MUST come from a template in the canonical Intermediary Email Templates Google Doc** (`1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4`) per `feedback_no_intermediary_drafts_outside_template`. No ad-hoc body copy.

```bash
# Lookup CIM-RECEIVED template from canonical doc
TEMPLATE_BODY=$(gog docs export 1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4 --format=md | \
  awk '/CIM RECEIVED/,/^---$/' | sed '$d')

# If template not found, skip and log a warning. Do NOT draft ad-hoc copy.
if [ -z "$TEMPLATE_BODY" ]; then
  echo "WARN: CIM-RECEIVED template not found in canonical doc. Auto-ack skipped — surface to Kay in morning briefing."
  exit 0
fi

# Fill placeholders, create Gmail draft via gog. Draft-only guard is mandatory.
gog gmail drafts create \
  --to "{intermediary_email}" \
  --subject "Re: {original_subject}" \
  --body "$FILLED_BODY" \
  --thread "{gmail_thread_id}" \
  --account kay.s@greenwichandbarrow.com \
  --gmail-no-send
```

The auto-ack creates a Gmail DRAFT only — Kay reviews and sends per `feedback_kay_handles_all_replies`. The auto-trigger (Steps 1-4) handles internal Drive/Attio/deal-eval work. The auto-ack handles the broker-facing reply. Two parallel surfaces, no conflict.

**Slack notification (after filing + Attio update verified):**
```bash
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"CIM Received: {Company Name}\nFrom: {Intermediary Name} ({Firm})\nIndustry: {industry}\nCIM filed to Drive: {drive_link}\nDeal folder: {folder_link}\nAttio: Created at Financials Received\n\nDeal-eval running buy-box screen. Results in morning briefing."}'
```

**Validation (must pass before Slack):**
```
checks = {
    "cim_in_drive": verify CIM file exists in CIM/ subfolder and size > 0,
    "no_duplicate_folders": verify only ONE company folder exists (no {Company} + {Company}(1)),
    "attio_entry_created": verify Active Deals entry exists at Financials Received,
    "inbox_item_written": verify brain/inbox/ file exists with urgency: critical,
    "deal_eval_triggered": verify deal-evaluation was invoked with correct parameters,
}

If any check fails → fix the issue, re-validate, then send Slack.
```

**Edge cases:**
- **Blind profile (no company name):** Cannot create ACTIVE DEALS folder or Attio entry. Fall through to standard morning review presentation. Inbox item still created with `urgency: high` and tag `topic/blind-profile`.
- **CIM for existing active deal:** Route to the Active Deal Fast-Path (line 292 above) instead. Do NOT create a duplicate folder or Attio entry.
- **Multiple CIMs in one email batch:** Process each independently. Each gets its own folder, inbox item, and deal-eval invocation.
- **CIM from unknown sender (no prior vault entity or Gmail correspondence):** Still fast-track the CIM filing. Create the intermediary vault entity (their CIM-send IS a reply, so an entity is warranted; no Intermediary Pipeline entry — that list is deprecated). Flag in morning briefing: "New intermediary detected: {name} at {firm}. Sent CIM for {company}."

### Morning Review Presentation

**Deals WITH CIM auto-triggered** are presented differently — Kay sees the completed buy-box screen results, not a "should we screen?" prompt:

```
INBOUND DEAL FLOW — CIM AUTO-SCREENED
──────────────────────────────────────
From: {Intermediary Name} ({Firm Name})
  Deal: {Company Name}
  CIM: Filed to Drive ✓ | Deal-eval: {Pass / Proceed / Need More Info}
  Buy-box result: {summary from deal-eval}
  Industry: {from CIM}
  Revenue: {from CIM}
  EBITDA: {from CIM}
  Geography: {from CIM}

  Action:
  - Proceed → continue deal-evaluation (Phase 3: financial analysis)
  - Pass → draft polite decline to intermediary
  - Table → keep in inbox, revisit later
```

**Deals WITHOUT CIM (teasers, blind profiles, deal summaries)** use the standard presentation:

```
INBOUND DEAL FLOW
─────────────────
From: {Intermediary Name} ({Firm Name})
  Intermediary: {Attio Person record exists / New — first contact (vault entity created, Attio People auto-created via Gmail interaction)}
  Deal: {Company name or "Blind profile"}
  Industry: {if stated}
  Revenue: {if stated, else "Not disclosed"}
  EBITDA: {if stated, else "Not disclosed"}
  Geography: {if stated}
  Attachment: {CIM/teaser/profile filename}

  Screen against buy box?
  - Yes → fast-track to deal-evaluation (intermediary buy-box screen)
  - Pass → draft polite decline to intermediary
  - Move to owner call → request management call (skips ad-hoc info-gathering)
  - Save for later → keep in inbox, revisit Friday
```

### On Kay's Approval
- **"Proceed"** (CIM auto-screened) → continue deal-evaluation at Phase 3 (financial analysis on the CIM already in Drive). The buy-box screen is done — this advances to deep analysis.
- **"Yes"** (no CIM) → trigger deal-evaluation skill with `source: intermediary-inbound` and `intermediary: {name}`. The deal-evaluation skill runs its fast buy-box screen (see deal-evaluation Intermediary Inbound Pathway).
- **"Pass"** → MANDATORY template-driven per `feedback_no_intermediary_drafts_outside_template`. Look up `DECLINE POST-REVIEW` snippet from canonical doc `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` via `gog docs export`. Fill `{first_name}`, `{their_subject}`, `{reason}` (one-line specific reason from the buy-box screen output). Create as Gmail draft via `gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send`. If template not found, skip with warning to morning briefing — do NOT draft ad-hoc copy. Also: log the deal in vault with reason. Tag the intermediary's Attio People record with the deal type they sent (e.g., `sends: manufacturing`, `sends: healthcare`) for future filtering.
- **"Move to owner call"** → request a management call directly via the intermediary. Skips the ad-hoc "need more info" info-gathering pattern (deprecated 2026-05-04 — too rare for broker engagement; we move to owner conversation instead). Trigger deal-evaluation Phase 4 (call prep) with `pending_owner_call: true`.
- **"Save for later" / "Table"** → no action, stays in inbox queue.

### Intermediary Relationship Tracking
After processing inbound deals, update the intermediary's Attio People record (if attributes exist on the People object):
- `last_deal_sent: {date}`
- `deal_types_sent: [{industry/type}]` (append, don't overwrite)
- (Intermediary Pipeline list deprecated — no separate stage advancement; the broker target Sheet + Attio People interaction history are the source of truth for intermediary relationship state)

## Niche Signal Detection (runs during data ingestion)

While processing Granola transcripts and Gmail, scan for niche-relevant signals that Kay may not have flagged. These feed into Friday's niche-intelligence run.

**What to look for:**
- Industry names or business types mentioned in calls that match buy box characteristics (B2B, recurring revenue, compliance-driven, fragmented market, founder-owned)
- Brokers or contacts mentioning deal flow in specific industries ("we're seeing a lot of activity in X")
- Multiple unrelated conversations referencing the same type of business in a week
- River guides naming industries with succession dynamics ("all these guys are retiring")
- Conference attendee clusters in unfamiliar niches
- Email threads referencing business types Kay hasn't explored

**What to flag:**
- The signal (exact quote or paraphrase)
- Source (which call, email, or meeting)
- Why it matches buy box (which characteristics align)

**Where to save:**
Write each signal to `brain/inbox/YYYY-MM-DD-niche-signal-{slug}.md` using inbox schema with:
- `tags: [inbox, topic/niche-signal, source/{source}]`
- `confidence: low` (these are passive observations, not validated niches)
- Body: the signal, source context, and buy box alignment

These signals are NOT surfaced during the daily pipeline review. They queue silently for Friday's niche-intelligence GATHER step.

## Active Niche Sprint Detection (runs daily)

**CRITICAL: The Industry Research Tracker Google Sheet is the SINGLE SOURCE OF TRUTH for niche statuses.** Never reconstruct niche statuses from session decisions, vault context, call preps, or memory. Niches get Tabled/Killed/moved between sessions and the sheet reflects reality.

**Always read the tracker directly:**

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!A3:D20" -a kay.s@greenwichandbarrow.com -j
```

Use this data for both:
1. The pipeline summary niche list (each niche with its status and channel)
2. Downstream decisions (target-discovery needs, outreach routing)

If the sheet read fails, say so in the briefing — do NOT fall back to session decisions or stale artifacts.

Niche sprint status tracking (transitions, folder moves, target-discovery triggers) is handled by niche-intelligence. Pipeline-manager consumes the sheet state, not the transition logic.

## Trigger

- **Auto:** Runs when Kay says "good morning" (triggers the daily workflow)
- **Manual:** `/pipeline-manager` on demand

## Slack Notification

Send a nudge only (not full detail):
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Pipeline updates waiting — {n} recommended changes + {n} stale deals. Open Codex to review."}'
```

## Reference

All stage IDs and API details: `references/attio-stages.md`
</essential_principles>

<signal_detection>
## Phase 1: Detect Activity Signals

Scan these sources for yesterday's date (or since last run):

### Calendar
```bash
# Yesterday's meetings (pipeline signals)
gog calendar list --from {YESTERDAY} --to {TODAY} --json

# Today's meetings (Granola reminder detection)
gog calendar list --from {TODAY} --to {TOMORROW} --json
```
Extract all external meetings (skip internal/team calls). Each meeting is a signal that a pipeline entry may need updating.

**In-person meeting detection (today):** For today's meetings, check for in-person meetings (no conferenceData, no hangoutLink, no Zoom/Meet/Teams/Webex URLs in description or location). Write any in-person meetings to the email-scan-results artifact under a new section:

```
## In-Person Meetings Today (Granola Reminder)
- {time} {title} at {location} — attendees: {names}
```

/start reads this and includes a Granola reminder in the daily note.

### Gmail
```bash
gog gmail search "after:{YESTERDAY} before:{TODAY}" --json --max 30 --account kay.s@greenwichandbarrow.com --gmail-no-send
```
Look for:
- NDA documents (PDF attachments with "NDA" in subject/filename) → NDA Executed
- Financial documents (CIM, P&L, balance sheet) → Financials Received
- **CIM attachments from intermediaries** → CIM Auto-Trigger (folder + filing + inbox + deal-eval, see "CIM Auto-Trigger" section)
- LOI drafts or signed documents → LOI stage changes
- Thank you emails sent → move from "Need to Send Thank You" to nurture. **Detection method:** search by recipient email + recency (`to:{email} newer_than:7d`), NOT by subject keyword. Thank-yous are often replies in existing threads.
- New introductions → new pipeline entries needed
- Broker correspondence → intermediary pipeline updates

### Vault
```bash
# Call notes logged yesterday
Glob: brain/calls/{YESTERDAY}*

# New entities created
git log --after={YESTERDAY} --before={TODAY} --name-only --diff-filter=A -- brain/entities/
```

### Post-call artifacts (important signal source)
Read saved call notes and staged task artifacts produced by post-call-analyzer.
These capture:
- Action items mentioned during the meeting
- Introductions promised ("I'll connect you with...")
- Next steps agreed to
- Deal-relevant information (financials coming, NDA discussion, etc.)

Do not call Granola MCP or `granola-api` from pipeline-manager. If the artifact
is missing, treat it as a post-call-analyzer health issue, not a cue to create a
parallel ingestion path.

Parse transcripts for pipeline-relevant signals: stage changes, new contacts to create, follow-up tasks.

### Conversation Context
If Kay mentions pipeline-relevant information during the session (e.g., "I met with Dan today", "Stan sent financials"), capture that as a signal too.
</signal_detection>

<matching>
## Phase 2: Match Signals to Pipeline Entries

For each signal detected, search Attio for the matching entry:

### Search by company name
```bash
curl -s -X POST "https://api.attio.com/v2/objects/companies/records/query" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"name":{"$contains":"{company_or_person_name}"}}}'
```

### Search across all 4 lists for that record
For each list, check if the company/person has an entry and what stage they're in.

### Signal → Stage Change Logic

**Network Relationship signals (People Records):**
| Signal | Attribute to Update | Recommended Value |
|--------|-------------------|-------------------|
| Meeting happened (calendar/Granola) | `next_action` | "Send thank you" |
| Thank you email sent (Gmail) | `next_action` | clear / set to next relevant action |
| Introduction promised | `next_action` | "Follow up on intro to {name}" + create new entity |
| Introduction received | `next_action` | "Schedule call with {name}" |
| No contact past nurture cadence | flag as overdue | Surface to Kay |
| New person met | All attributes | Populate relationship_type, nurture_cadence, value_to_search, how_introduced |
| Relationship deepened | `nurture_cadence` | Upgrade (Occasionally → Monthly, etc.) |
| Gone cold | `nurture_cadence` | Downgrade to Dormant |

**Query for overdue nurture contacts:**
```
For each person where nurture_cadence is set:
  - Weekly: flag if last email/meeting > 10 days ago
  - Monthly: flag if last email/meeting > 5 weeks ago
  - Quarterly: flag if last email/meeting > 14 weeks ago
  - Occasionally: never flag automatically
  - Dormant: skip
```
Use Attio's auto-enriched email/calendar interaction data for "last contact" timestamps.

**Active Deals Pipeline signals:**
| Signal | Current Stage | Recommended Stage |
|--------|--------------|-------------------|
| First owner conversation | Identified / Contacted | First Conversation |
| Follow-up deep dive | First Conversation | Second Conversation |
| NDA document in email | Any pre-NDA | NDA Executed + Slack ping |
| Financials/CIM received | NDA Executed | Financials Received |

**NDA Executed Slack Notification (all sources — cold outreach, intermediary, conference):**
When a deal moves to NDA Executed (from any source), immediately ping #active-deals:
```bash
curl -s -X POST "$SLACK_WEBHOOK_ACTIVE_DEALS" \
  -H "Content-Type: application/json" \
  -d '{"text":"New Active Deal: {Company Name}\nSource: {Cold Outreach / Intermediary / Conference}\nOwner: {Owner Name}\nNDA signed: {date}\nDeal folder: {folder_link}\n\nAnalyst: deal folder created, financials pending."}'
```
This ensures the analyst is looped in the moment a deal becomes real, regardless of how it entered the pipeline.
| LOI drafted/sent | Financials Received | LOI / Offer Submitted |
| LOI signed by both parties | LOI / Offer Submitted | LOI Signed |
| Deal passed/killed | Any | Closed / Not Proceeding |

**Investor Engagement signals:**
| Signal | Current Stage | Recommended Stage |
|--------|--------------|-------------------|
| Quarterly update sent | Current quarter | Next quarter |
| Investor meeting held | Current quarter | Next quarter |
</matching>

<recommendations>
## Phase 3: Present Recommendations

Display each recommendation to Kay one at a time using AskUserQuestion:

```
Pipeline Update: {Person/Company Name}
Current: {Pipeline} → {Current Stage}
Recommended: → {New Stage}
Signal: {What triggered this — e.g., "Coffee meeting yesterday per calendar"}

Approve this change?
- Yes, move them
- No, keep current stage
- Different stage (let me specify)
- Skip for now
```

Also present any new entries that should be added:
```
New Entry: {Person/Company Name}
Pipeline: {Which pipeline}
Starting Stage: {Recommended stage}
Signal: {How we know — e.g., "Dan Tanzilli introduced you to X"}

Add to pipeline?
```

### Stale Deal Alerts

After recommendations, flag any entries that have been in the same stage for 2+ weeks:
```
Stale: {Company Name}
Pipeline: Active Deals → {Stage}
Days in stage: {n}
Action needed? Move forward, kill, or keep watching?
```
</recommendations>

<execute>
## Phase 4: Execute Approved Changes

For each approved change, call the Attio API:

### Move entry to new stage
```bash
curl -s -X PATCH "https://api.attio.com/v2/lists/{list_id}/entries/{entry_id}" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"data":{"entry_values":{"stage":[{"status":"{status_id}"}]}}}'
```

### Add new entry to a list
```bash
curl -s -X POST "https://api.attio.com/v2/lists/{list_id}/entries" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"data":{"parent_record_id":"{record_id}","entry_values":{"stage":[{"status":"{status_id}"}]}}}'
```

### Create new company record (if needed)
```bash
curl -s -X POST "https://api.attio.com/v2/objects/companies/records" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"data":{"values":{"name":[{"value":"{company_name}"}]}}}'
```

### Update People record attributes (Network relationships)
```bash
curl -s -X PATCH "https://api.attio.com/v2/objects/people/records/{record_id}" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"data":{"values":{
    "relationship_type": "{type}",
    "nurture_cadence": "{cadence}",
    "value_to_search": "{value}",
    "next_action": "{action}",
    "how_introduced": "{intro_context}"
  }}}'
```

### Search for a person
```bash
curl -s -X POST "https://api.attio.com/v2/objects/people/records/query" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"name":{"$contains":"{person_name}"}}}'
```

### Query all people with a specific nurture cadence (for overdue checks)
```bash
curl -s -X POST "https://api.attio.com/v2/objects/people/records/query" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"nurture_cadence":"{cadence}"}}'
```

After all updates, confirm:
```
Pipeline updates complete:
- {n} pipeline entries moved to new stages
- {n} People records updated (network relationships)
- {n} new entries/contacts added
- {n} stale deals flagged
- {n} overdue nurture contacts surfaced
- {n} To Do rows appended
```
</execute>

<followup_actions>
## Phase 5: Follow-up Actions

### Upcoming Meeting Prep Triggers

**As of 2026-04-12, meeting-brief-manager nightly automation is RETIRED.** Pipeline-manager now owns the "Brief needed?" surfacing for ALL external meetings — investor, advisor, target, and general external. The meeting-brief skill runs on-demand when Kay opts in, per `feedback_meeting_brief_on_demand.md`.

**Mandatory scan each morning briefing:**
1. `gog calendar list --from {TODAY} --to {TOMORROW} --json` — list TODAY (D+0) and TOMORROW (D+1) events. Per `memory/feedback_preflight_covers_today_and_tomorrow.md` (2026-05-06): D+1-only scans drop same-day externals. Always scan D+0 + D+1, no exceptions.
   - **Friday rule:** scan covers **today + Mon AND Tue** (weekend briefing is lighter and may miss Monday)
   - **Sunday rule:** scan covers **today + Monday** (standard)
2. Filter to external meetings only (skip internal/team calls — Camilla, cold-call ops, etc.).
3. For each external meeting: check session-decisions files from the prior 3 days. If Kay has already approved or declined a brief for this meeting, SKIP — do not re-ask.
4. For each remaining external meeting, surface as a Decisions-bucket item using Obama framing:
   - **RECOMMEND: Generate brief for {name} ({time} {date})** — [one-sentence cadence/context reason] → **YES / NO / LET'S DISCUSS**
5. Kay answers YES → invoke the appropriate brief command per the routing table below. Kay answers NO → skip, no artifact.

**Briefing-assembly invariant:** If any external meeting exists in the D+0 + D+1 scan window and is neither already-decided nor surfaced in Decisions, the briefing is malformed — fix before delivering.

Every brief invocation loads `templates/{type}.md` + most recent `examples/{type}/*.md` before drafting. No generic-template fallback.

| Contact | Cadence | Brief command | Template used | Save location |
|---------|---------|---------------|---------------|---------------|
| Jeff Stevens (Anacapa) | Monthly | `/investor-update monthly jeff-stevens` (or `/investor-update call-prep jeff-stevens` with auto-detect) | `investor-update/templates/monthly-call-prep.md` | INVESTOR COMMUNICATION / MONTHLY |
| Guillermo Lavergne (Ashford) | Bi-weekly | `/investor-update biweekly guillermo-lavergne` | `investor-update/templates/biweekly-call-prep.md` | INVESTOR COMMUNICATION / BI-WEEKLY |
| Owner call (Active Deals pipeline) | On-demand | `/meeting-brief --type=owner-call {name}` | `meeting-brief/templates/owner-call.md` | Deal folder (if exists) or RESEARCH/BRIEFS + `brain/briefs/` |
| Intermediary (broker, M&A advisor, wealth advisor, law firm) | On-demand | `/meeting-brief --type=intermediary {name}` | `meeting-brief/templates/intermediary.md` | RESEARCH/BRIEFS + `brain/briefs/` |
| Conference / panel / industry event | On-demand | `/meeting-brief --type=conference-prep {event}` | `meeting-brief/templates/conference-prep.md` | RESEARCH/BRIEFS + `brain/briefs/` |
| New contact / warm intro arrival | On-demand | `/meeting-brief --type=new-contact {name}` | `meeting-brief/templates/new-contact.md` | RESEARCH/BRIEFS + `brain/briefs/` |

### Email Verification Gate (CRITICAL — applies to ALL drafts from this skill)

Before creating ANY email draft (thank-you, follow-up, decline, intro), verify the recipient email:
- **Prior correspondence exists** (Kay has emailed/received email from this address) → verified, proceed
- **Apollo-verified email** → proceed (all emails verified via Apollo people match)
- **All other emails** → run through Apollo API verification. Only proceed if `verified`. If `guessed`/`unavailable`/`bounced`, tell Kay: "no verified email for {name}" and stop. NEVER guess an email from name + domain.

Bounced emails damage Kay's sender domain reputation. Her email is her entire business.

### Follow-Up Actions

After pipeline updates, surface any follow-up tasks:

- **"Need to Send Thank You"** → FIRST verify Kay hasn't already sent the thank you (search `from:kay.s@greenwichandbarrow.com to:{contact_email} newer_than:7d` with `--account kay.s@greenwichandbarrow.com --gmail-no-send`). If already sent, auto-move to Nurture and skip. If not sent: classify recipient as intermediary (broker/IB/lawyer/CPA) vs other.
  - **Intermediary thank-you** → MANDATORY template-driven per `feedback_no_intermediary_drafts_outside_template`. Look up THANK YOU snippet from canonical doc `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` via `gog docs export`. Fill `{first_name}`, `{call_callback}` (1-2 sentences from Granola transcript referencing specific topics they raised), `{next_step}` (1 sentence committing to the action item from the call). If template not found in doc, skip with warning surfaced to morning briefing. Do NOT draft ad-hoc body copy.
  - **Non-intermediary thank-you** (owner, peer, investor, internal) → draft personalized using Kay's voice (memory: `user_outreach_voice.md`), referencing Granola/call/calendar specifics. No template doctrine for these audiences yet.
  - In both cases, create as Gmail draft via `gog gmail drafts create --account kay.s@greenwichandbarrow.com --gmail-no-send`.
- **Introduction promised** → ask Kay for the person's name/company. Create `brain/entities/{slug}.md` in the vault with proper schema. If the intro is to a target company owner, add them to Attio Active Deals at "Identified" stage. If the intro is to an intermediary (broker/IB/lawyer/CPA), do NOT create a pipeline entry — log to the broker target Sheet per `feedback_brokers_stay_in_sheet_until_reply`. When the intro email arrives later, they're already tracked.
- **Introduction received** → match the intro email to the tracked entity, move to "Contacted" stage
- **NDA Executed** → remind to request financials if not already received
- **Financials Received** → flag for financial modeling
- **Stale deals** → suggest kill/advance/table decision
- **Meeting action items → To Do rows** — Parse Granola transcript for action items, next steps, and commitments. For each, append a row to the To Do tab via the `task-tracker-manager` skill's `append` verb (`python3 scripts/task_tracker.py append --task "..." --type Work --project "G&B" [--due YYYY-MM-DD] [--notes "..."]`) with:
  - Task: the action item
  - Notes: context from the meeting
  - Due date: based on urgency/commitment made
  - Project: "G&B" (or the relevant pipeline label for deal-related actions)

  Present all proposed tasks to Kay for approval before creating. She may want to adjust priority, due date, or skip some.

**Post-meeting flow (complete sequence):**
1. Detect meeting from calendar + Granola transcript
2. Recommend pipeline stage change → Kay approves
3. Draft thank you email → Kay reviews → append To Do row with due date
4. Create entities for promised introductions → Kay confirms names
5. Extract action items from Granola → append To Do rows → Kay approves
6. Any outreach needed (e.g., new broker intro) → draft email → append To Do row

**To Do row append:** Every follow-up action that Kay approves should also be appended to the To Do tab via the `task-tracker-manager` skill's `append` verb. Examples:
- "Send thank you to Dan Tanzilli" (due: tomorrow)
- "Outreach to Eric Dreyer / Eight Quarter Advisors re: art restoration" (due: this week)
- "Follow up on Dan Tanzilli art attorney intro" (due: 1 week)

This ensures nothing falls through the cracks between pipeline updates and actual execution.
</followup_actions>

<success_criteria>
## Success Criteria

Pipeline manager run is complete when:
- [ ] Yesterday's calendar, email, Granola, and vault scanned for signals
- [ ] Signals matched against Attio pipeline entries AND People records
- [ ] Pipeline stage recommendations presented one at a time
- [ ] Network relationship recommendations presented one at a time
- [ ] Approved pipeline changes executed via Attio Lists API
- [ ] Approved People record updates executed via Attio People API
- [ ] Overdue nurture contacts surfaced
- [ ] Stale deals flagged (2+ weeks in same stage)
- [ ] Thank you emails drafted for approved contacts
- [ ] To Do rows appended for all approved follow-up actions
- [ ] Summary confirmed to user
</success_criteria>

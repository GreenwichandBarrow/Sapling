---
schema_version: 1.2.0
date: 2026-05-15
type: refactor-plan
status: draft
skill_origin: create-skill
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-shirts]]"]
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags:
  - date/2026-05-15
  - output
  - output/refactor-plan
  - status/draft
  - topic/skill-refactor
  - topic/pipeline-manager
  - person/kay-shirts
---

# Pipeline-Manager Router Refactor Plan

**Source:** `.claude/skills/pipeline-manager/SKILL.md` — 1,283 lines, single fat file, ~6x over the 200-line router cap.

**Target archetype:** Router (per `.claude/skills/create-skill/templates/router-skill.md` + `workflows/upgrade-to-router.md`).

**Planning-only.** Execution must happen in a dedicated session — pipeline-manager fires every morning via `/goodmorning` Step 3, and a botched refactor breaks the G&B morning briefing flow.

---

## 1. Current Section Inventory

Headings and line ranges in the live `SKILL.md` (1,283 lines total, frontmatter + 2 wrapping XML blocks excluded from counts):

| # | Heading | Lines | Char | Disposition |
|---|---------|------:|------|-------------|
| 0 | Frontmatter + `<learnings>` + `<objective>` | 1–33 | inline | **Keep in router** (slim) |
| 1 | Essential principles intro + How It Works (1–7) | 34–43 | inline | **Keep in router** |
| 2 | Two Systems, One Daily Review | 45–48 | conceptual | **Keep in router** (3-line summary) |
| 3 | Pipeline Stages (3 Lists) | 49–53 | conceptual | → `references/two-systems-model.md` |
| 4 | Network Relationships (People Records) | 54–59 | conceptual | → `references/two-systems-model.md` |
| 5 | Daily Review Flow | 60–66 | conceptual | **Keep in router** (orchestration order) |
| 6 | Section 1: Active Deals Pipeline | 69–76 | spec | → `workflows/assemble-active-deals.md` |
| 7 | Section 2: Investor Pipeline | 77–81 | spec | → `workflows/assemble-active-deals.md` (small enough to co-locate) |
| 8 | Section 3: Relationship Building | 82–107 | spec | → `workflows/assemble-relationship-building.md` |
| 9 | Section 4: Action Items (Granola) | 108–114 | spec | → `workflows/assemble-action-items.md` |
| 10 | Briefing vs Slack Routing | 117–137 | doctrine | → `references/briefing-routing.md` |
| 11 | Briefing Format (Decisions-only) | 138–237 | **doctrine + template** | → `workflows/assemble-decisions-list.md` + `references/decisions-list-format.md` |
| 12 | Architecture: Manager + 2 Sub-Agents + 1 External | 238–248 | architecture | **Keep in router** (router summary table) |
| 13 | Sub-Agent 1: Pipeline Agent (+ quality gates) | 249–268 | sub-agent def | → `workflows/run-pipeline-agent.md` |
| 14 | Sub-Agent 2: Relationships (now external skill) | 269–273 | pointer | **Keep in router** (1-line pointer to `relationship-manager`) |
| 15 | Sub-Agent 3: Granola Agent | 274–278 | sub-agent def | → `workflows/run-granola-agent.md` |
| 16 | Stop Hooks (1–11) | 279–298 | validation list | → `references/stop-hooks.md` |
| 17 | Email Scan Results Validation | 300–314 | validation | → `references/stop-hooks.md` |
| 18 | Manager Red Flags | 315–321 | check list | → `references/manager-quality-review.md` |
| 19 | Manager Quality Review (incl. session-decisions reconciliation + deferral aging) | 322–344 | check list | → `references/manager-quality-review.md` |
| 20 | Briefing Format Stop Hooks (11 invariants) | 346–363 | check list | → `references/briefing-format-stop-hooks.md` |
| 21 | Data Ingestion intro | 365–367 | conceptual | → `workflows/ingest-data.md` |
| 22 | Granola → brain/calls/ | 369–376 | procedure | → `workflows/ingest-data.md` |
| 23 | Superhuman Draft Status Check | 377–397 | procedure | → `workflows/ingest-data.md` |
| 24 | Outbound Email Scan (Paths A/B/C, Timothy Wong gap) | 398–425 | procedure | → `workflows/ingest-data.md` |
| 25 | Cadence Advancement | 427–453 | procedure | → `workflows/scan-cadence-advancement.md` |
| 26 | New Approval Detection | 454–459 | procedure | → `workflows/scan-cadence-advancement.md` |
| 27 | Conference Decision Scan (deprecated pointer) | 460–462 | pointer | **Keep in router** (1 line) |
| 28 | Target List Monitoring (JJ Call Outcomes) | 463–470 | procedure | → `workflows/scan-jj-outcomes.md` |
| 29 | Niche Sprint Status Tracking (4 states table) | 471–485 | reference table | → `references/niche-sprint-states.md` |
| 30 | Post-Meeting Niche Status Cleanup Triggers | 486–496 | procedure | → `workflows/handle-niche-status-change.md` |
| 31 | JJ Daily Call Prep (delegated pointer) | 497–500 | pointer | **Keep in router** (1 line) |
| 32 | Warm Intro Detection | 501–509 | procedure | → `workflows/detect-warm-intros.md` |
| 33 | Gmail → brain/inbox/ | 510–517 | procedure | → `workflows/ingest-data.md` |
| 34 | Deal Flow Email Classification (BLAST/DIRECT/NEWSLETTER) | 518–536 | doctrine | → `references/deal-flow-classification.md` |
| 35 | Email Scan Results Artifact (file spec) | 537–591 | spec | → `references/email-scan-results-artifact.md` |
| 36 | Active Deal Fast-Path | 592–634 | procedure | → `workflows/fast-path-active-deal.md` |
| 37 | Inbound Introduction Detection | 635–665 | procedure | → `workflows/detect-warm-intros.md` |
| 38 | Inbound Intermediary Deal Detection (incl. CIM Auto-Trigger 5-step, edge cases, Morning Review Presentation) | 666–887 | **the big one** | → `workflows/handle-inbound-intermediary.md` + `references/cim-auto-trigger-steps.md` |
| 39 | Niche Signal Detection | 889–912 | procedure | → `workflows/scan-niche-signals.md` |
| 40 | Active Niche Sprint Detection (tracker is single source of truth) | 914–930 | doctrine + procedure | → `references/niche-sprint-states.md` + 1-line in router |
| 41 | Trigger | 932–935 | inline | **Keep in router** (3 lines) |
| 42 | Slack Notification | 937–944 | inline curl | → `references/slack-payloads.md` |
| 43 | Reference (pointer to attio-stages) | 946–948 | pointer | **Keep in router** (auto via references_index) |
| 44 | Phase 1: Detect Activity Signals (calendar/gmail/vault/granola/conversation) | 951–1012 | procedure | → `workflows/ingest-data.md` |
| 45 | Phase 2: Match Signals to Pipeline Entries (Attio queries + signal→stage tables) | 1014–1080 | procedure + tables | → `workflows/match-signals-to-pipeline.md` + `references/signal-to-stage-tables.md` |
| 46 | Phase 3: Present Recommendations + Stale Deal Alerts | 1082–1119 | procedure | → `workflows/assemble-active-deals.md` |
| 47 | Phase 4: Execute Approved Changes (Attio API curls) | 1121–1190 | procedure | → `references/attio-api-patterns.md` |
| 48 | Phase 5: Follow-up Actions (Meeting Prep Triggers, Email Verification Gate, Follow-Up Actions, Post-meeting flow, Motion task creation) | 1192–1266 | procedure | → `workflows/followup-actions.md` + `references/brief-routing-table.md` + `references/email-verification-gate.md` |
| 49 | Success Criteria | 1268–1283 | checklist | **Keep in router** (collapsed) |

**Headings counted:** 94. **Distinct functional areas:** 7 (ingestion, matching, recommending, executing, follow-up, briefing assembly, intermediary fast-paths). **Pure duplication with CLAUDE.md detected:** sections 11 (Decisions-only format), 19 (Manager Quality Review session-decisions reconciliation), 41 (Trigger), 49 (Success Criteria language) — all replaceable with one-line CLAUDE.md pointers.

---

## 2. Proposed Router SKILL.md (target ≤200 lines)

```yaml
---
name: pipeline-manager
description: Daily morning briefing engine — pipeline stage changes, outreach recommendations (nurture cadence), and action items (Granola). CEO reviews, approved items become Motion/Sheet tasks automatically. Use when the CEO says "good morning" or invokes /pipeline-manager.
user_invocable: true
context_budget:
  skill_md: 200
  max_references: 6
  learnings_md: 50
  sub_agent_limit: 600
---

<objective>
Assemble the G&B morning briefing as a Decisions-only list. Detect activity signals (calendar, email, Granola, vault), match against Attio pipelines and People records, present recommendations, execute approvals, validate via stop hooks.
</objective>

<essential_principles>
- **Read `learnings.md` FIRST, append BEFORE returning.** Skill-local feedback loop.
- **Decisions-only format is non-negotiable.** Single ordered list, urgency-sorted (🔴 → 🟡 → 🟢), Obama framing per item, ≤5 items, ascending numbering, C-suite labels. Full spec in `references/decisions-list-format.md`.
- **Brief-decisions pre-flight is mandatory.** Scan D+0 + D+1 external meetings (Fri = today+Mon+Tue, Sun = today+Mon). Each surfaces as 🔴 Decision unless already-decided in session-decisions. Spec in `workflows/brief-decisions-preflight.md`.
- **Tracker is single source of truth for niche statuses.** Never reconstruct from session decisions or vault context.
- **Manager (Claude) catches sub-agent errors before presenting.** Nameless entries / wrong-day items / imprecise characterizations get fixed inline. Full spec in `references/manager-quality-review.md`.
</essential_principles>

<quick_start>
1. Read `learnings.md` — note any active anti-patterns.
2. Run `workflows/ingest-data.md` (calendar, Gmail, Granola, vault, draft status).
3. Run sub-agents in parallel: `workflows/run-pipeline-agent.md` + `workflows/run-granola-agent.md`. Read `brain/context/relationship-status-{date}.md` (artifact from `relationship-manager`).
4. Run `workflows/brief-decisions-preflight.md` to enumerate D+0/D+1 externals.
5. Run `workflows/assemble-decisions-list.md` — cluster, sort, Obama-frame, cap at 5.
6. Run `references/briefing-format-stop-hooks.md` checklist before output.
7. Present to the CEO. On approval: `workflows/execute-approved-changes.md`. Append to `learnings.md` if new anti-pattern observed.
</quick_start>

<routing>
| User Intent / Signal | Workflow |
|---|---|
| Morning briefing (default) | `workflows/assemble-decisions-list.md` |
| Data ingestion (any source) | `workflows/ingest-data.md` |
| Pipeline agent (Active Deals + Investor) | `workflows/run-pipeline-agent.md` |
| Granola action-items agent | `workflows/run-granola-agent.md` |
| Brief-decisions pre-flight | `workflows/brief-decisions-preflight.md` |
| Active Deal Fast-Path (Gmail attachment match) | `workflows/fast-path-active-deal.md` |
| Inbound intermediary (CIM auto-trigger) | `workflows/handle-inbound-intermediary.md` |
| Cadence advancement detection | `workflows/scan-cadence-advancement.md` |
| JJ call outcome detection | `workflows/scan-jj-outcomes.md` |
| Warm intro detection | `workflows/detect-warm-intros.md` |
| Niche signal detection | `workflows/scan-niche-signals.md` |
| Niche status change cleanup | `workflows/handle-niche-status-change.md` |
| Signal→stage matching (Attio query) | `workflows/match-signals-to-pipeline.md` |
| Execute approved changes | `workflows/execute-approved-changes.md` |
| Follow-up actions (thank-you drafts, motion tasks) | `workflows/followup-actions.md` |
</routing>

<architecture>
**Manager + 2 Sub-Agents + 1 External Skill artifact:**
- Sub-Agent 1: Pipeline Agent (Active Deals + Investor) — `workflows/run-pipeline-agent.md`
- Sub-Agent 2: External — `relationship-manager` skill writes `brain/context/relationship-status-{date}.md`
- Sub-Agent 3: Granola Agent — `workflows/run-granola-agent.md`
- Manager: runs both sub-agents in parallel, reads relationship artifact, runs quality review (`references/manager-quality-review.md`), assembles Decisions list, runs stop hooks (`references/briefing-format-stop-hooks.md` + `references/stop-hooks.md`), presents to the CEO.

**External pointers (do not duplicate here):**
- JJ prep / call log / harvest → `jj-operations` skill
- Niche sprint transitions → `niche-intelligence` skill
- Conference decisions → `conference-discovery` skill
- Relationship cadence / nurture → `relationship-manager` skill
</architecture>

<references_index>
| Reference | Purpose |
|---|---|
| `references/attio-stages.md` (existing) | List/stage IDs for Active Deals + Investor Engagement |
| `references/attio-api-patterns.md` | Curl patterns: query, move stage, create record/entry, update People |
| `references/two-systems-model.md` | Pipeline Stages (3 Lists) vs Network Relationships (People Records) |
| `references/decisions-list-format.md` | Obama framing, urgency emojis, clustering, header line, hygiene rules |
| `references/briefing-format-stop-hooks.md` | 11-item pre-output checklist (decisions cap, numbering, C-suite labels, etc.) |
| `references/manager-quality-review.md` | Manager checks: nameless / wrong-day / imprecise / session-decisions reconciliation / deferral aging |
| `references/stop-hooks.md` | Post-execution validation (11 hooks: Attio, Granola, Gmail, Motion, Slack, ACTIVE DEALS folder, etc.) |
| `references/signal-to-stage-tables.md` | Signal→stage mapping tables (Active Deals, Investor, People Records, cadence thresholds) |
| `references/cim-auto-trigger-steps.md` | 5-step detection + folder + filing + inbox + deal-eval + auto-ack |
| `references/deal-flow-classification.md` | BLAST/DIRECT/NEWSLETTER classification + revenue floor + pattern detection |
| `references/email-scan-results-artifact.md` | Schema + section spec for `brain/context/email-scan-results-{date}.md` |
| `references/niche-sprint-states.md` | 4-state table (Under Review / Active-Outreach / Active-Long Term / Tabled-Killed) + tracker-read pattern |
| `references/brief-routing-table.md` | Contact-type → brief command mapping (Jeff/Guillermo/owner/intermediary/conference/new-contact) |
| `references/email-verification-gate.md` | Apollo verification gate before any draft creation |
| `references/briefing-routing.md` | Briefing vs Slack routing decision rules |
| `references/slack-payloads.md` | Canonical curl bodies for #operations, #active-deals notifications |
</references_index>

{Canonical <learning_capture> block from create-skill/references/learning-capture.md}

<success_criteria>
- [ ] All ingestion sources scanned (calendar, Gmail, Granola, vault, draft status, outbound)
- [ ] Sub-agents ran in parallel and returned within budget
- [ ] Manager quality review passed (no nameless / no wrong-day / no imprecise)
- [ ] Decisions list ≤5 items, ascending numbering, Obama-framed, C-suite-labeled
- [ ] Brief-decisions pre-flight covered D+0 + D+1 externals (or Fri/Sun overlays)
- [ ] Briefing format stop hooks passed
- [ ] Post-execution stop hooks ran on approved changes
- [ ] Slack nudge sent (HTTP 200 verified)
- [ ] `learnings.md` appended if new anti-pattern observed
</success_criteria>
```

**Estimated final size:** ~155 lines (under 200 cap, ~25 lines headroom for the canonical learning_capture block).

---

## 3. Proposed Workflow Files

`workflows/` — each ≤200 lines per router-archetype cap. 13 workflows total.

| File | Purpose | Est. Lines | Source range in current SKILL.md |
|---|---|---:|---|
| `ingest-data.md` | Calendar/Gmail/Granola/vault/draft-status/outbound — all data ingestion before signal detection | 180 | 365–425, 510–517, 537–591 (artifact pointer), 951–1012 |
| `match-signals-to-pipeline.md` | Phase 2: query Attio by name, search across lists, signal→stage decision tree (delegate tables to ref) | 90 | 1014–1080 |
| `assemble-active-deals.md` | Section 1 + Section 2 (Active Deals + Investor) presentation logic | 80 | 69–81, 1082–1119 |
| `assemble-relationship-building.md` | Section 3 logic: read relationship-status artifact, cadence thresholds (delegate to ref), Section 3 presentation | 90 | 82–107 |
| `assemble-action-items.md` | Section 4: parse Granola transcripts, propose Motion tasks (or Sheet rows per pending decision) | 60 | 108–114, 274–278 (subagent body) |
| `assemble-decisions-list.md` | THE briefing assembler: take outputs from sections 1–4, cluster by entity, urgency-sort, Obama-frame, cap at 5, render header line | 170 | 138–237 (the load-bearing one) |
| `brief-decisions-preflight.md` | Calendar enumeration for D+0/D+1 externals + Fri/Sun overlay + session-decisions cross-ref + HOLD/zero-attendee filter | 90 | 191–197 + CLAUDE.md preflight invariant |
| `run-pipeline-agent.md` | Sub-Agent 1 spec + quality gates (name resolution, calendar day verification, no unactionable items) + ACTIVE DEALS folder detection | 110 | 249–268, 287 |
| `run-granola-agent.md` | Sub-Agent 3 spec: transcript fetch, action-item extraction, intro-promise detection, Motion/Sheet task proposal | 70 | 274–278, 997–1008, 1244–1265 |
| `fast-path-active-deal.md` | Stages 3–9 Gmail-match fast-path: 6-step procedure + 4-check validation + Slack ping | 110 | 592–634 |
| `handle-inbound-intermediary.md` | Detection signals + sender classification + inbox creation + CIM auto-trigger orchestration (delegate 5-step CIM detail to ref) + morning review presentation + on-approval actions | 200 | 666–887 |
| `scan-cadence-advancement.md` | Read target sheet columns (Day 0/3/6/14), detect sends/replies, advance Attio, new-approval detection | 90 | 427–459 |
| `scan-jj-outcomes.md` | Read JJ call columns (Q–T), Connected/Voicemail/Wrong Number/Not Interested handling | 50 | 463–470 |
| `detect-warm-intros.md` | Warm intro path scan (Attio + vault + Gmail) + Inbound Introduction Detection (intro emails, intro cadence) | 110 | 501–509, 635–665 |
| `scan-niche-signals.md` | Niche-relevant signal capture during ingestion, write to `brain/inbox/` with `topic/niche-signal` | 50 | 889–912 |
| `handle-niche-status-change.md` | Downstream cleanup triggers when the CEO changes a niche status in-session | 50 | 486–496 |
| `execute-approved-changes.md` | Phase 4: Attio API calls for stage moves, list creates, People updates (delegate curl patterns to ref) | 70 | 1121–1190 |
| `followup-actions.md` | Phase 5: thank-you drafts (intermediary template-driven vs other), intro entity creation, Motion/Sheet task creation, post-meeting flow | 170 | 1192–1266 |

**Workflow total:** 18 files. (3 more than the 4 the request listed; intermediary + ingestion + assembly each warrant their own file rather than being merged.)

---

## 4. Proposed Reference Files

`references/` — each ≤300 lines per archetype cap. 16 reference files total (1 existing + 15 new).

| File | Purpose | Est. Lines | Source |
|---|---|---:|---|
| `attio-stages.md` (existing, keep) | Attio list + stage IDs | 74 | already exists |
| `attio-api-patterns.md` | All `curl` patterns for Attio (query, list-entry patch, create company, update People, query by cadence) | 80 | 1121–1190 |
| `two-systems-model.md` | Pipeline Stages (3 Lists) vs Network Relationships (People Records) — when each applies | 40 | 45–59 |
| `decisions-list-format.md` | Obama-frame template, urgency emojis, clustering, header line + dashboard URL, hygiene rules, routing pre-existing sections | 200 | 138–237 (extracted spec, not procedure) |
| `briefing-format-stop-hooks.md` | 11-item checklist that runs immediately before output | 60 | 346–363 |
| `manager-quality-review.md` | 6 manager checks (nameless / wrong-day / imprecise / stale / relationships-already-handled / session-decisions reconciliation + deferral aging) | 90 | 315–344 |
| `stop-hooks.md` | 11 post-execution hooks (Attio, relationships, Granola, Gmail, Motion, niche signals, Slack, ACTIVE DEALS folder, CIM auto-trigger, reconciliation, outbound coverage) | 130 | 279–298 |
| `signal-to-stage-tables.md` | Active Deals signal→stage table, Investor signal→stage table, People Records signal→action table, cadence thresholds | 80 | 91–96, 1030–1080 |
| `cim-auto-trigger-steps.md` | 5-step procedure detail (detection criteria, folder creation, file upload, inbox item template, deal-eval invocation, auto-ack template lookup) + edge cases | 230 | 691–832 |
| `deal-flow-classification.md` | BLAST/DIRECT/NEWSLETTER definitions + revenue floor + pattern detection + guardrail | 60 | 518–536 |
| `email-scan-results-artifact.md` | Full schema + section spec + Draft Calibration block | 90 | 537–591 |
| `niche-sprint-states.md` | 4-state table + tracker-read pattern + Active Niche Sprint Detection (single source of truth doctrine) | 70 | 471–485, 914–930 |
| `brief-routing-table.md` | Contact-type → brief command mapping (Jeff, Guillermo, owner, intermediary, conference, new-contact) | 50 | 1213–1220 |
| `email-verification-gate.md` | Apollo verification gate doctrine before any draft creation | 30 | 1222–1229 |
| `briefing-routing.md` | Briefing vs Slack routing rules (what goes where, rule of thumb) | 50 | 117–137 |
| `slack-payloads.md` | Canonical curl JSON bodies for #operations, #active-deals, NDA Executed, CIM Received notifications | 60 | 937–944, 606–613, 808–812, 1064–1069 |

**Reference total:** 16 files. All within 300-line cap.

---

## 5. Frontmatter for new SKILL.md

```yaml
---
name: pipeline-manager
description: Daily morning briefing engine — pipeline stage changes, outreach recommendations (nurture cadence), and action items (Granola). CEO reviews, approved items become Motion/Sheet tasks automatically. Use when the CEO says "good morning" or invokes /pipeline-manager.
user_invocable: true
context_budget:
  skill_md: 200
  max_references: 6
  learnings_md: 50
  sub_agent_limit: 600
---
```

**Notes on the budget:**
- `max_references: 6` — worst case (full morning run) loads `decisions-list-format` + `briefing-format-stop-hooks` + `manager-quality-review` + `signal-to-stage-tables` + `stop-hooks` + one situational (e.g., `cim-auto-trigger-steps`).
- `learnings_md: 50` — slightly above the 40 default; pipeline-manager accumulates more anti-patterns than most skills.
- `sub_agent_limit: 600` — pipeline agent + granola agent each return up to 600 words (above default 400 — these aren't simple lookups; they synthesize multi-source data).

---

## 6. Migration Plan (staged, not big-bang)

### Step 0 — Pre-flight (5 min)
- Snapshot `SKILL.md` → `SKILL.md.backup-2026-MM-DD` in skill dir.
- `git status` clean.
- Verify no morning run currently in progress (`launchctl list | grep pipeline` or `ps -ef | grep pipeline-manager`).
- Confirm with the CEO: "Refactor session is starting; pipeline-manager will be in transition state for ~90 min."

### Step 1 — Write references first (30 min)
References have no dependencies on workflows. Write all 15 new reference files. Each is mechanical extraction — copy block from `SKILL.md.backup`, convert markdown headings → XML tags, save under `references/`. Validate each ≤300 lines.

### Step 2 — Write workflows (45 min)
Workflows reference the new references. Each workflow has `<required_reading>` block at top listing 1–4 references it needs. Write all 18 workflow files. Validate each ≤200 lines.

### Step 3 — Write new router SKILL.md as `SKILL.md.new` (15 min)
Use template from section 2 above. Validate ≤200 lines. Do NOT overwrite live `SKILL.md` yet.

### Step 4 — Sandbox dry-run (20 min)
Three options for sandboxing — pick the lowest-risk:

**Option A (preferred): symlink-swap on a non-morning day**
- Pick a Tue/Wed/Thu evening when no overnight pipeline-manager run is scheduled (it runs on `/goodmorning` trigger, not launchd — so this is naturally low-risk).
- `mv SKILL.md SKILL.md.live` and `mv SKILL.md.new SKILL.md`.
- Manually invoke `/pipeline-manager` in a fresh Claude Code session with a dry-run flag in the prompt: *"Dry-run mode: scan, assemble, but do NOT execute Attio writes, do NOT send Slack, do NOT create drafts. Show me the would-be briefing output and the would-be execution payload."*
- Compare output against yesterday's actual briefing format. Hunt for: missing sections, wrong-day items, nameless entries, dropped invariants.

**Option B: side-by-side comparison**
- Keep live `SKILL.md` untouched. Copy entire skill dir to `.claude/skills/pipeline-manager-v2/` with new structure.
- Invoke `/pipeline-manager-v2` with dry-run prompt.
- Compare output against `/pipeline-manager` output side-by-side.
- Higher confidence but doubles disk + token cost.

**Option C: shadow-mode**
- Invoke the new structure during the live morning run with a "shadow output, do not present" flag.
- Compare shadow output against the live output in evening review.
- Lowest fidelity (depends on the CEO's read), but zero blast radius.

**Recommended: Option A on Tuesday or Wednesday evening.** Risk is bounded because the swap can be reverted in 1 command, and the CEO is not depending on the briefing at 7pm.

### Step 5 — Swap in production (2 min)
- After dry-run passes: `mv SKILL.md.live SKILL.md.backup-pre-refactor` and `mv SKILL.md.new SKILL.md` (if Option A was used, this swap already happened — just delete the `.live` backup).
- Run a final `wc -l SKILL.md` to confirm ≤200 lines.
- `git add .claude/skills/pipeline-manager/ && git commit -m "refactor: pipeline-manager → router archetype"`.

### Step 6 — Validate next morning's briefing (Day +1)
- Watch the Decisions list output.
- Compare structure against prior morning's brief (header line, urgency sort, ≤5 items, C-suite labels, ascending numbering).
- Confirm brief-decisions pre-flight still surfaces D+0 + D+1 externals correctly.
- Confirm stop hooks still fire (check `learnings.md` for any new anti-pattern).
- If anomalies → execute rollback plan (section 9).

### Step 7 — One-week soak + monitoring
- Days 2–7: monitor briefing fidelity. Any regression → file a learnings.md entry and either fix in-place or roll back.
- Day 7: if clean, delete `SKILL.md.backup-pre-refactor` and close the refactor bead.

---

## 7. Risk Assessment

### Top 3 risks

1. **Decisions-list-format regression on next morning's briefing.** This is the highest-stakes invariant — the CEO reads it every morning. If the router fails to load `decisions-list-format.md` at the right step, or if `assemble-decisions-list.md` drops a clustering rule or numbering rule, the briefing comes back malformed. *Mitigation:* `briefing-format-stop-hooks.md` runs as the LAST step before output and rejects malformed briefings; reference is short enough (60 lines) to always load. Dry-run in Step 4 catches structural breakage.

2. **Brief-decisions pre-flight invariant slips.** Per CLAUDE.md, every D+0/D+1 external meeting that isn't already-decided must surface as a 🔴 Decision. The current SKILL.md has this baked at multiple call sites (sections 11, 19, 48). When fragmented into a single workflow, the integration risk is "router forgets to call it." *Mitigation:* `<essential_principles>` in the router names this invariant inline, and `success_criteria` includes "Brief-decisions pre-flight covered." Stop hook rejects if no preflight artifact present.

3. **CIM auto-trigger fast-path latency degrades.** The current SKILL.md has the full CIM 5-step procedure inline; in the new structure it lives in `workflows/handle-inbound-intermediary.md` + `references/cim-auto-trigger-steps.md`. A CIM detected during Gmail ingestion needs the router to load that workflow + reference within the same session — adds ~5,000 tokens. If the workflow file isn't surfaced when ingestion sees a CIM, the auto-trigger silently no-ops and a deal goes unscreened. *Mitigation:* `ingest-data.md` workflow includes an explicit "if CIM detected → load `workflows/handle-inbound-intermediary.md`" branch; CIM auto-trigger validation stop hook (current hook #9) catches a missed trigger and flags it in the briefing.

### Other risks (lower)

4. **`goodmorning.md` command references** `pipeline-manager` skill by name only (line 25, 27, 112) — no breakage expected since skill name is unchanged.
5. **No headless-prompt file for pipeline-manager** (checked — `ls .claude/skills/pipeline-manager/` shows only `SKILL.md`, `learnings.md`, `references/`). No launchd plist owns this skill. Refactor is invisible to the headless layer.
6. **15 other skills reference `pipeline-manager` by name in their docs.** All are conceptual references ("pipeline-manager reads this artifact," "after pipeline-manager runs"). None import structural content from `SKILL.md`. Refactor is invisible to them.
7. **`learnings.md` continuity.** Current 44 lines should be preserved verbatim — the canonical learning_capture block is appended, not replacing the file.
8. **Calibration doc deferral.** The 2026-05-15 calibration report defers Motion → Sheet handoff rewrite. Refactor must preserve the current "approved items → Motion task" language until that pattern is locked — `workflows/followup-actions.md` should mark the Motion-vs-Sheet swap as a follow-up TODO, not bundle it into this refactor.

---

## 8. Estimated Session Time + Token Cost

**Total session: ~2.0–2.5 hours of focused work.**

| Step | Time | Token cost (rough) |
|---|---|---|
| Step 0: pre-flight | 5 min | ~3K |
| Step 1: 15 references | 30 min | ~25K (mostly file writes) |
| Step 2: 18 workflows | 45 min | ~40K (extract + reformat + required_reading blocks) |
| Step 3: write router | 15 min | ~10K |
| Step 4: dry-run + diff | 20 min | ~30K (one full pipeline-manager run + comparison reads) |
| Step 5: swap | 2 min | ~1K |
| Step 6: morning validation (next day) | 10 min observational | ~5K |

**Total: ~115K tokens, well within a single Opus session budget.** Recommend using a fresh session at start (clean 1M context window) and not branching to other tasks mid-refactor. Mechanical extraction is the dominant cost; using `Edit` tool for surgical changes is cheaper than `Write`-everything-fresh.

---

## 9. Rollback Plan

If the new structure misbehaves on Monday's briefing (or any post-swap morning):

**Immediate (sub-1-minute revert):**
```bash
cd .claude/skills/pipeline-manager
mv SKILL.md SKILL.md.failed-attempt
mv SKILL.md.backup-pre-refactor SKILL.md
git add . && git commit -m "revert: pipeline-manager refactor (briefing regression)"
```
Next morning's `/goodmorning` will load the old monolithic SKILL.md and the briefing returns to the prior-working state.

**Diagnostic (after revert):**
- Diff `SKILL.md.failed-attempt` vs `SKILL.md` on the specific section that broke.
- Look at `learnings.md` for any anti-pattern that fired during the failed run.
- Look at the malformed briefing text the CEO received — identify which invariant slipped.
- File the gap in `brain/traces/{date}-pipeline-refactor-regression.md` so the next attempt avoids it.

**Re-attempt criteria:**
- Wait minimum 1 week before re-attempt (let the next calibration cycle absorb the learning).
- Re-attempt only after the specific failure mode has a guardrail (new stop hook, new required_reading entry, or new ref file).

**Note:** Refactor is reversible because it is purely a file-structure change. No external data (Attio, Gmail, vault) is touched. No schema migrations. No downstream skill changes required.

---

## 10. Open Questions for the CEO

**1. Motion vs Sheet handoff — bundle into this refactor or defer?**
The 2026-05-15 calibration doc defers the Motion → `TO DO 5.12.26` Sheet rewrite for pipeline-manager (37 refs across 5 skills, awaiting "approved-briefing-item → Sheet row" pattern lock). Should the refactor:
- (a) preserve every "Motion task" reference verbatim (no behavior change, mechanical refactor only), then bundle Motion → Sheet in a separate session?
- (b) replace Motion references inline during the refactor since we're already touching the file?
**Recommend (a).** Mechanical refactor + behavior change in one session = doubled risk surface. Lock the Motion handoff pattern first, then sweep across all 5 skills.

**2. Dry-run sandbox: which option?**
Option A (symlink-swap Tuesday evening), Option B (parallel `pipeline-manager-v2` skill), or Option C (shadow-mode on a live run)?
**Recommend Option A.** Lowest cost, fastest revert, no parallel skill clutter. But Option B may be worth the cost if the CEO wants to compare side-by-side outputs before approving the swap.

---

## File Manifest Summary

- **1 router SKILL.md** (~155 lines, from 1,283 — 88% reduction)
- **18 workflow files** (avg ~95 lines each, all ≤200)
- **16 reference files** (1 existing + 15 new, avg ~85 lines each, all ≤300)
- **1 learnings.md** (preserved, 44 lines existing + canonical learning_capture appended)
- **Total file count:** 36 files in `.claude/skills/pipeline-manager/`
- **Total surface area:** ~3,000 lines, but only ~155 + selected refs/workflows load per run vs the current 1,283-line load-every-time.

**Net token savings per morning run:** Approx. 80%. Cold-load is ~155 lines (router) + ~5–7 refs/workflows × ~90 lines avg = ~750 lines vs current 1,283. Hot-load (everything resolved) saves more because most workflows never fire on a given day.

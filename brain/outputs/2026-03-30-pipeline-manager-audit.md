---
schema_version: "1.1.0"
date: 2026-03-30
type: research
status: draft
tags: ["date/2026-03-30", "output", "output/research", "status/draft", "topic/architecture", "topic/skill-design"]
---

# Pipeline Manager Audit: Scope, Complexity, and Spin-Off Recommendations

The pipeline-manager SKILL.md is 1,207 lines. For comparison, most skills in the system are 100-300 lines. This is a monolith doing the work of 4-5 skills.

## 1. Current Responsibilities (14 distinct jobs)

**#1 - Gmail ingestion (~80 lines).** Scan inbound email, write to brain/inbox/, classify confidence.

**#2 - Deal flow email classification (~50 lines).** BLAST/DIRECT/NEWSLETTER classification for DEAL FLOW label. Includes revenue floor auto-reject, buy box screening, and Slack ping for matches.

**#3 - Active Deal Fast-Path (~50 lines).** Match emails to active deals (stages 3-9), file to Drive, update Attio, Slack ping, auto-trigger deal-eval.

**#4 - CIM Auto-Trigger (~100 lines).** Detect CIM attachments, create ACTIVE DEALS folder structure, upload CIM, create inbox item, invoke deal-evaluation, Slack, 5-point validation.

**#5 - Inbound Intermediary Deal Detection (~70 lines).** Detect broker deal emails, classify sender, create inbox items, morning presentation format with CIM-screened vs teaser paths.

**#6 - Inbound Introduction Detection (~50 lines).** Detect intro emails, create entities, add to Attio, draft warm intro response + thank-you to introducer, warm intro cadence.

**#7 - Outbound Email Scan (~30 lines).** Catch manually-sent emails, trigger Attio stage changes + JJ call date calculation.

**#8 - Superhuman Draft Status Check (~30 lines).** Check if outreach drafts were sent, flag unsent with escalating urgency, detect replies.

**#9 - Email Scan Results Artifact (~50 lines).** Write brain/context/email-scan-results file as handoff contract for downstream skills. Draft calibration section.

**#10 - Granola ingestion (~20 lines).** Pull transcripts, write to brain/calls/, create missing entities.

**#11 - Relationship management (~80 lines).** People record attributes, nurture cadence thresholds, action-already-taken verification via Gmail search, overdue contact surfacing. Already has its own sub-agent (Sub-Agent 2).

**#12 - Niche sprint status tracking (~70 lines).** Read WEEKLY REVIEW sheet, detect Active/Tabled/Killed transitions, move rows between tabs, move Drive folders, create target list templates, phase compliance checks (no owner outreach during Diligence).

**#13 - JJ Daily Call Prep (~80 lines).** Select targets from master sheet, reply-check before adding to call list, WebSearch personal tidbits, create Call Log docs from template, draft Slack message for 10am, overnight outcome harvesting.

**#14 - Conference Decision Scan (~15 lines).** Read Conference Pipeline sheet for Attend/Register decisions, create Motion tasks.

Plus: 3 sub-agent definitions, 9 stop hooks, email scan validation checklist, manager red flags, pipeline stage signal matching tables, Attio API execution templates, follow-up actions (thank-yous, intros, Motion tasks), investor call prep triggers, Slack notifications, ACTIVE DEALS folder detection catch-all.

## 2. Complexity Assessment

### High context, high API surface, time-sensitive

- **CIM Auto-Trigger (#4):** Needs buy box, folder structure, Attio stages, deal-eval interface. Touches Gmail attachments, Drive mkdir/upload, Attio create, Slack, deal-eval invocation. Must run same-day because intermediaries shop deals competitively.
- **Active Deal Fast-Path (#3):** Needs deal context across stages 3-9, Drive folder mapping, Attio stage logic. Same-day urgency.
- **JJ Daily Call Prep (#13):** Needs target sheet structure, reply-check logic, WebSearch, Drive doc templates, Slack formatting. Must be ready by 10am ET.

### High context, moderate API surface, morning batch

- **Relationship management (#11):** Needs People attributes, nurture thresholds (Weekly/Monthly/Quarterly/Occasionally/Dormant), Gmail search for action verification. Attio People API.
- **Deal flow classification (#2):** Needs buy box, revenue floor ($1.5M), intermediary pipeline state, BCC header detection. Attio query + Slack.
- **Niche sprint tracking (#12):** Needs WEEKLY REVIEW sheet structure, target-discovery interface, folder IDs for TABLED/KILLED. Sheets API + Drive.

### Low context, independent

- **Granola ingestion (#10):** Granola MCP, vault write. No dependencies on other responsibilities.
- **Superhuman draft status check (#8):** Superhuman MCP only. Independent query.
- **Conference decision scan (#14):** One sheet read, one Motion task. Minimal.
- **Outbound email scan (#7):** Gmail search + Attio matching. Independent.
- **Email scan results artifact (#9):** Just writing a file. Depends on #1-8 completing first.

### Independence analysis

Responsibilities #7, #8, #10, #11, #12, #13, #14 are all fully independent of each other. They could run in parallel with zero coordination. Responsibilities #1-6 form a chain (Gmail scan feeds classification feeds detection feeds artifact), but even within that chain, #3 (fast-path) and #4 (CIM trigger) could run as parallel handlers on the same email stream.

## 3. Natural Separation Points

### Cluster A: Email Intelligence (responsibilities 1-9)

The biggest chunk and the one that already absorbed intermediary-manager's Channel 2. It is a coherent unit: scan email, classify everything, produce a structured artifact that downstream skills consume.

Sub-clusters within email intelligence:
- **A1: Inbound scan + classification** (#1, #2, #5, #6, #9) - the core ingestion loop
- **A2: Active deal fast-path + CIM auto-trigger** (#3, #4) - same-day deal processing, high stakes, complex validation
- **A3: Outbound tracking** (#7, #8) - checking what Kay sent, what is still pending

### Cluster B: CRM Stage Management

Pipeline stage matching and Attio execution (the matching/execute phases from the SKILL.md). This is what pipeline-manager was originally named for: detect signals, recommend stage changes, execute on approval. Currently interleaved with email scanning rather than cleanly separated from it.

### Cluster C: Relationship Management (#11)

People records, nurture cadences, action-already-taken verification. Already has its own sub-agent (Sub-Agent 2: Relationships Agent). Already planned as a spin-off (relationship-manager).

### Cluster D: JJ Operations (#13)

A complete, self-contained workflow with its own audience (JJ, not Kay), its own schedule (10am delivery vs 9am briefing), its own API surface (Sheets, Drive docs, WebSearch, Slack #operations-sva), and its own validation needs. Two daily runs: morning prep and overnight outcome harvesting.

### Cluster E: Niche Sprint Status Tracking (#12)

Sheet monitoring, row moves, folder moves, template creation, phase compliance. This is closer to niche-intelligence than to pipeline management. It watches the same WEEKLY REVIEW sheet that niche-intelligence populates.

### Cluster F: Granola Ingestion (#10)

Small (20 lines), tightly coupled to signal detection. Could stay or move to a general data-ingestion pre-step.

### Cluster G: Conference Decision Scan (#14)

Tiny (15 lines). Reads the same sheet that conference-discovery owns.

## 4. Spin-Off Recommendations

### Spin-off 1: email-intelligence (Cluster A)

**What it would own:**
- All Gmail ingestion (inbound + outbound scan)
- Deal flow email classification (BLAST/DIRECT/NEWSLETTER)
- Active Deal Fast-Path (email-triggered deal processing)
- CIM Auto-Trigger (email-triggered CIM filing and deal-eval invocation)
- Inbound introduction detection
- Superhuman draft status check
- Writing the email-scan-results artifact

**What it needs from pipeline-manager:** Nothing. The dependency reverses. Email-intelligence produces the artifact (brain/context/email-scan-results), pipeline-manager consumes it.

**Schedule:** Runs first in the morning workflow (or overnight via launchd). Must complete before pipeline-manager starts.

**Communication:** Writes brain/context/email-scan-results-{date}.md. This handoff contract already exists and is well-defined.

**Why spin off:** Email scanning is the single largest chunk of pipeline-manager (responsibilities 1-9, approximately half the file). It has its own validation requirements (email scan results validation checklist), its own sub-agent potential (one for inbound, one for outbound/drafts), and its own time-sensitivity profile (CIM auto-trigger needs to run fast, draft status check can wait). Separating it would cut pipeline-manager roughly in half and let email intelligence evolve independently.

**Risk:** The Active Deal Fast-Path and CIM Auto-Trigger currently update Attio directly. If email-intelligence owns those, it has Attio write access, creating two skills writing to Attio simultaneously. Mitigation: email-intelligence only writes to Attio for same-day urgent items (CIM detected, NDA detected). Everything else goes through the artifact for pipeline-manager to present.

### Spin-off 2: relationship-manager (Cluster C) - already planned

**What it would own:**
- People record attribute management (nurture_cadence, next_action, relationship_type, value_to_search, how_introduced)
- Nurture cadence monitoring and overdue contact surfacing
- Action-already-taken verification (Gmail search before surfacing "Need to..." contacts)
- Thank-you email drafting
- Introduction processing (entity creation, warm intro drafting)
- New contact onboarding from meetings

**What it needs from pipeline-manager:** Calendar data (meetings that happened), Granola data (who attended, what was discussed). Could read from vault (brain/calls/) rather than receiving a direct handoff.

**Schedule:** Part of the morning workflow, after email-intelligence. Could also run independently on a nurture-check cadence (e.g., Monday and Thursday).

**Communication:** Returns a list of relationship actions to the orchestrator for inclusion in the morning briefing, using the same numbered-item format.

**Why spin off:** Relationship management is person-centric while pipeline management is deal-centric. Different data model, different cadences, different decision criteria. The sub-agent already exists. Formalizing it as a skill makes it testable and independently improvable.

### Spin-off 3: jj-operations (Cluster D)

**What it would own:**
- Daily target selection for JJ's calls (from master target sheet)
- Reply-check before adding targets to call list
- WebSearch for personal tidbits
- Call Log doc creation from template
- Slack message drafting and delivery (10am)
- Overnight outcome harvesting (read Call Log docs, update master sheet)
- Call type labeling (OWNER CALL vs CUSTOMER CALL)

**What it needs from pipeline-manager:** Nothing directly. The data it needs (targets where Kay approved outreach + email was sent + call date = today) lives on the master target sheet already.

**Schedule:** Two runs per day:
1. Overnight/early morning: prepare call list, create docs, draft Slack
2. After 2pm ET (post-JJ shift): harvest call outcomes, update sheet

**Communication:** Writes call outcomes to the master target sheet. Pipeline-manager reads outcomes the next morning as signals (e.g., "Connected + Interested" triggers stage change recommendation).

**Why spin off:** Most self-contained cluster. Different audience (JJ, not Kay), different schedule (10am, not 9am), different API surface (Sheets, Drive docs, WebSearch, Slack #operations-sva), different validation needs. Also the most likely to evolve independently as JJ's workflow changes. Keeping it inside pipeline-manager means every JJ workflow change requires editing a 1,200-line file.

### Spin-off 4: niche-sprint-tracker - merge into niche-intelligence (Cluster E)

**What it would own:**
- Reading WEEKLY REVIEW sheet for status changes
- Detecting Active-Diligence, Active-Outreach, Tabled, Killed transitions
- Moving rows between tabs (WEEKLY REVIEW to TABLED/KILLED)
- Moving Drive folders to status-appropriate locations
- Creating target list templates for new Active sprints
- Phase compliance checks (no owner outreach during Diligence)
- Triggering target-discovery at the appropriate pace

**Better home:** niche-intelligence already owns the WEEKLY REVIEW sheet, the one-pagers, the scorecards, and the niche lifecycle. Sprint status tracking is the operational tail of niche-intelligence. Merging it there keeps the full niche lifecycle in one skill rather than splitting it across two.

**What it needs from pipeline-manager:** Nothing. It reads the sheet directly.

**Schedule:** Nightly (after analyst call decisions are made). Or as part of the existing niche-intelligence Tuesday run plus a lightweight daily check.

### Not recommended for spin-off

**Conference Decision Scan (#14):** Too small for its own skill (15 lines). Move into conference-discovery, which already owns the Conference Pipeline sheet.

**Granola Ingestion (#10):** Keep in pipeline-manager or move to email-intelligence as a general "data ingestion" pre-step. It is 20 lines and tightly coupled to signal detection.

## 5. What Stays in Pipeline-Manager (the core)

After spin-offs, pipeline-manager becomes what it was originally named for:

1. Read signals from email-intelligence artifact, vault calls, calendar, and conversation context
2. Match signals to Attio pipeline entries across all 3 lists (Active Deals, Intermediary, Investor)
3. Recommend stage changes with signal evidence
4. Present the morning briefing in the 5-section format (assembling contributions from relationship-manager and other skills)
5. Execute approved changes via Attio Lists API
6. Flag stale deals and present kill/advance/keep decisions
7. Investor call prep triggers (Jeff monthly, Guillermo bi-weekly)
8. Manager red flags (conflicting signals, missing data, unusual patterns)
9. Stop hooks for pipeline validation only (not email, not niche, not JJ)

Estimated size after spin-offs: 300-400 lines. Focused and maintainable.

## 6. Dependency Map (post-spin-off)

Morning workflow execution order:

**Step 1 - email-intelligence** (overnight or first thing)
- Produces: brain/context/email-scan-results-{date}.md
- Side effects: CIM auto-trigger (urgent), Active Deal Fast-Path (urgent)

**Step 2 - pipeline-manager** (reads email-intelligence artifact + vault + calendar)
- Produces: morning briefing sections 1-3, stale deal flags
- Side effects: Attio stage updates (on approval)

**Step 2 parallel - relationship-manager** (reads vault calls + email-intelligence artifact)
- Produces: briefing section 4 (nurture, thank-yous, intros)
- Side effects: People record updates, Superhuman drafts

**Step 2 parallel - jj-operations** (reads master target sheet)
- Produces: Call Log docs, Slack message draft
- Side effects: Sheet updates (call outcomes, overnight)

**Independent - niche-sprint-tracker** (inside niche-intelligence, nightly)
- Reads: WEEKLY REVIEW sheet
- Side effects: row moves, folder moves, target-discovery triggers

The orchestrator (Chief of Staff) assembles all outputs into the unified 5-section morning briefing.

## 7. Implementation Priority

1. **jj-operations** - Medium effort, high impact. Most self-contained, cleanest cut, different audience and schedule. No entanglement with other responsibilities.

2. **relationship-manager** - Medium effort, high impact. Already planned, sub-agent exists, clear person-vs-deal separation. Sub-Agent 2 code can be extracted almost directly.

3. **email-intelligence** - High effort, very high impact. Biggest chunk, but also the most entangled (CIM/fast-path write to Attio directly). Needs careful artifact contract design and clear Attio write ownership rules.

4. **niche-sprint-tracker into niche-intelligence** - Low effort, medium impact. Move approximately 70 lines. Clean cut since it reads the sheet independently.

5. **conference decision scan into conference-discovery** - Trivial effort, low impact. Move approximately 15 lines.

## 8. Key Risks

**Orchestration complexity.** More skills means more coordination. The morning workflow already runs 3 sub-agents in parallel. Splitting into 4+ skills means the orchestrator (CLAUDE.md morning workflow section) needs to be updated to sequence them correctly and assemble their outputs into the unified briefing format.

**Attio write contention.** If email-intelligence and pipeline-manager both write to Attio, there need to be clear ownership rules. Proposed rule: email-intelligence writes only for time-sensitive items (CIM, NDA detected). Pipeline-manager writes for all other stage changes. Relationship-manager writes only to People records. No overlap.

**Artifact contract brittleness.** The email-scan-results file is already the handoff contract. If its format changes and downstream skills are not updated, things break silently. Consider adding a schema for the artifact, or at minimum a version field.

**Testing surface.** Each new skill needs its own test path. Currently pipeline-manager is tested as one unit. Splitting means testing each skill independently plus testing the integration (does the orchestrator correctly sequence them and assemble output).

## 9. Bottom Line

Pipeline-manager is doing the work of 4-5 skills packed into one 1,207-line file. The natural separation points are clear: email intelligence, CRM stages, relationship management, JJ operations, and niche sprint tracking. The cleanest first cut is jj-operations (self-contained, different audience, different schedule). The highest-impact cut is email-intelligence (half the file, already has a handoff contract). The already-planned cut is relationship-manager (sub-agent exists, person-vs-deal separation is clear).

After all spin-offs, pipeline-manager returns to its original purpose: signal matching, stage change recommendations, and the morning briefing assembly. Around 300 lines, focused on judgment rather than data gathering.

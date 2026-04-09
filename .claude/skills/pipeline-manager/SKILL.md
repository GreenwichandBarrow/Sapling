---
name: pipeline-manager
description: "Daily morning briefing — pipeline stage changes, outreach recommendations (nurture cadence), and action items (Granola). Kay reviews, approved items become Motion tasks automatically. Runs when Kay says good morning."
user_invocable: true
---

<objective>
Keep Attio pipelines current without Kay having to remember to update them. Scan activity signals (calendar, email, call notes, vault), match them to pipeline entries, recommend stage changes, and execute approved updates via Attio API.

Kay is the bottleneck on pipeline management. This skill removes that bottleneck by making pipeline updates a 30-second yes/no review instead of a manual drag-and-drop chore.
</objective>

<essential_principles>
## How It Works

1. **Detect** — Scan yesterday's calendar, email, Granola, and vault for activity signals
2. **Match** — Cross-reference signals against Attio pipeline entries AND People records
3. **Recommend** — Present stage change recommendations AND relationship updates to Kay
4. **Execute** — On approval, update pipeline stages AND People record attributes via Attio API
5. **Flag** — Surface stale deals (same stage 2+ weeks) AND overdue nurture contacts
6. **Follow up** — Draft thank yous, create entities for intros, create Motion tasks
7. **Nudge** — Send Slack ping so Kay knows updates are waiting

## Two Systems, One Daily Review

The pipeline-manager handles two connected but distinct tracking systems:

### Pipeline Stages (3 Lists)
For **Intermediary, Active Deals, and Investor** pipelines. Company-based. Linear progression through stages.
- Signal: deal milestone (NDA signed, financials received, LOI, etc.)
- Action: move entry to new stage

### Network Relationships (People Records)
For **all network contacts**. Person-based. Non-linear relationship management.
- Custom attributes on People: `relationship_type`, `nurture_cadence`, `value_to_search`, `next_action`, `how_introduced`
- Signal: meeting happened, email exchanged, intro promised, thank you needed
- Actions: update `next_action`, update `nurture_cadence`, flag overdue contacts

### Daily Review Flow

On morning sign-on, Claude presents the review with the header **"Pipeline Review"** at the top. All sections are presented sequentially. Kay reviews each item and approves or skips. Approved outreach and action items become Motion tasks automatically. **All items presented for review must be numbered.**

**Inbound Deal Flow (before sections):**
If any inbound intermediary deals were detected during Gmail ingestion, present them first. These are time-sensitive — intermediaries shop deals to multiple buyers. See "Inbound Intermediary Deal Detection" section below for format and actions.

**Present the review in these sections, in this order:**

### Section 1: Active Deals Pipeline
Stage changes, new entries, and stale deals for the Active Deals – Owners list.
After each owner call or meeting, ask: "Was this a meaningful owner conversation?" If yes, check the `meaningful_conversation` checkbox on the Active Deals entry in Attio.
- Show: company, current stage, recommended stage, signal evidence
- Kay approves → Attio updated immediately
- Kay rejects → no change
- Flag stale deals (same stage 2+ weeks): "Kill, advance, or keep watching?"

### Section 2: Intermediary Pipeline
Stage changes, new entries, and stale entries for the Intermediary list.
- New intermediaries to add, existing ones to advance
- Flag intermediaries going cold (no deal flow in 8+ weeks)

### Section 3: Investor Pipeline
Stage changes for the Investor Engagement list.
- Quarterly update status, meeting prep triggers
- Conference decisions detected (Attend/Register Only) with registration details

### Section 4: Relationship Building
Everything related to People records (not in a pipeline list). Nurture cadence, next_actions, thank-yous, intros.

Check ALL People with nurture_cadence set against their `last_interaction` date in Attio. Surface anyone overdue.

Format: "Consider following up with {name} ({relationship_type}, {nurture_cadence}). Last contact: {date}."
- **Approve** → Motion task created: "Follow up with {name}" with due date based on urgency
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

### Section 5: Action Items (from Granola transcripts)
Present action items extracted from recent meeting transcripts.

Format: "From your meeting with {name} on {date}: '{action item}'"
- **Approve** → Motion task created with title, description, and due date
- **Skip** → no action

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
- Quick action items (send email, make call)
- Today's calendar/agenda items
- Stale deal flags (kill/advance/keep)
- Overdue contacts needing a touchpoint

**Rule of thumb:** If Kay needs to read more than a sentence of context to act on it, send it to Slack with a link. The briefing is a checklist, not a report.

### Briefing Format

After gathering all data from the 5 sections above, RE-ORGANIZE the output into these 5 consistent sections. This is what Kay sees every morning. Same sections, same order, every day. Keep each item to 1 line.

```
Pipeline shifts to review/approve:
1. {Company}: {current stage} → {recommended stage} ({signal evidence})
2. {Contact}: nurture overdue, last contact {date}

Pipeline summary:
Active Deals: {total} ({n} Identified, {n} Contacted, {n} Financials Received)
Intermediary: {total} ({n} Actively Receiving, {n} Warmed, {n} Contacted)
Niches (from tracker, not session decisions):
- {Rank}. {Niche Name} — {Status}, {Channel}
- ...
Stale deals: {n} entries in same stage 2+ weeks

Motion action steps to review/approve:
1. {Action item} — due {date}
2. {Follow up with person} — {context}

Superhuman email drafts to review/approve:
Reminder to send:
- {Name} — {one-word context: thank-you / follow-up / reschedule}
- {Name} — {one-word context}
Reminder to delete:
- {Draft description} — orphaned/stale

Targets for review ({niche}):
1. {Name}, {Company} — Warm intro via {contact}. Draft personal email or standard cadence?
2. {Name}, {Company} — Borderline: {specific concern}. Approve or Pass?

On deck for JJ (tomorrow):
- {Target name} — {action: follow-up / first outreach}

Other items / today's agenda:
1. {Today's meetings with times}
2. {Quick flags or reminders}
```

**Intermediary matches rule:** Daily broker listing matches from lead-aggregator are posted directly to #strategy-active-deals as individual Slack messages (one per deal, thumbs up/down reactions). Do NOT include individual match details in the morning briefing. The System Status line should only report: "lead-aggregator — {n} new lead matches posted to Slack".

**Targets for Review rules:**
- This section surfaces targets from target-discovery's auto-advance system that need Kay's decision. Two categories only:
  1. **Warm intro targets** — warm-intro-finder found a connection path (via Attio, vault, Gmail, Kay's network). Kay decides: "draft" (create a Superhuman draft for her personal outreach) or "cadence" (enroll in Claude-managed email cadence via Superhuman drafts).
  2. **Edge case targets** — borderline on buy box/ICP criteria (borderline size, geography, unclear ownership, possible PE backing). Kay decides: "approve" (send to Superhuman drafts + JJ based on channel) or "pass" (move to Passed tab on tracker).
- **Auto-approved targets do NOT appear here.** Targets that passed all buy box + ICP criteria with no warm intro flow automatically to Superhuman drafts + JJ. Only exceptions surface.
- Group by niche when multiple niches are active. One header per niche.
- Kay responds with decisions per item: "1 draft, 2 approve" or "1 cadence, 2 pass"
- On Kay's decision:
  - "draft" → create Superhuman draft via `superhuman-draft.sh` for Kay's review before sending
  - "cadence" → enroll in Claude-managed email cadence via Superhuman drafts
  - "approve" → route to Superhuman drafts + JJ call list based on channel
  - "pass" → move target to Passed tab on the tracker sheet

Each item numbered. Each has a clear action or question. No informational items without an ask. No items requiring deep review — those go to Slack.

**JJ "On Deck" timing rule:** Only show JJ items the day BEFORE they are due. Not earlier. Example: if Freedman Risk follow-up is due Thursday April 2, it appears in Wednesday April 1's briefing — not before. This prevents noise and keeps Kay focused on what's actionable today/tomorrow only.

After Kay reviews all three categories, confirm summary:
```
Pipeline manager complete:
- {n} pipeline stages updated
- {n} tasks created in Motion
- {n} email drafts in Superhuman
- {n} stale deals flagged
```

## Architecture: Manager + 2 Sub-Agents + 1 External Skill

Claude acts as the **manager** overseeing 2 specialized sub-agents that run in parallel on session start, plus reading an artifact from the relationship-manager skill. The manager:
- Launches both agents simultaneously
- Reads the relationship-status artifact from relationship-manager
- Reviews their outputs for quality and consistency
- Flags any red flags or conflicts to Kay before presenting
- Presents recommendations sequentially: Part 1 (pipeline changes) → Part 2 (outreach/nurture) → Part 3 (action items)
- Executes approved changes
- Runs stop hooks to validate execution

### Sub-Agent 1: Pipeline Agent
**Scope:** Intermediary, Active Deals, and Investor Lists
**Scans:** Email (NDAs, financials, LOIs, broker correspondence, CIM attachments), calendar (deal meetings), vault (call notes), Drive ACTIVE DEALS folder (new subfolders)
**Returns:** Stage change recommendations with signal evidence. Also executes CIM auto-trigger (folder creation, filing, inbox item, deal-eval invocation) before returning recommendations — CIM deals arrive pre-screened.

**Pipeline Agent Quality Gates (CRITICAL):**

1. **Name resolution required.** Every pipeline entry presented to Kay MUST include the company/person name, not just a record ID. If the Attio API does not return a name for a record, try: (a) `mcp__attio__get_record_details` with the record ID, (b) `mcp__attio__search_records` by record ID, (c) cross-reference against the outreach tracker Google Sheet. If name STILL cannot be resolved, do NOT present the entry as a recommendation — log it as "unresolvable" and flag for investigation. Kay cannot act on nameless entries.

2. **Calendar day verification.** When presenting "today's agenda" items, verify the day of week matches. Cross-check: `date +%A` returns today's day name. Only include events from TODAY's calendar query in the "today's agenda" section. Events from yesterday's scan go in "pipeline signals" only. Events from tomorrow go in "upcoming" only. Never mix days.

3. **No unactionable items.** Every item presented to Kay must have: a name, a clear action or question, and enough context to decide. If any of these is missing, the subagent must resolve it before returning results — or exclude the item.

**ACTIVE DEALS folder detection (catch-all for broker platform NDA edge cases):**
Scan the ACTIVE DEALS Drive folder for any subfolder that does not have a matching Attio Active Deals entry. This catches the case where Kay signs an NDA on a broker platform (no email sent), creates a folder, and saves the NDA manually. When detected:
1. Create Attio Active Deals entry at "NDA Signed" stage with `source: intermediary`
2. Create entity in vault if needed
3. File any documents in the folder into the standard subfolder structure
4. Present in morning briefing: "New deal folder detected: {Company}. Created Attio entry at NDA Signed."

### Sub-Agent 2: Relationships (now relationship-manager skill)
Relationship management (nurture cadence monitoring, action-already-taken verification, overdue contacts, People record updates) is now handled by the relationship-manager skill. It writes an artifact to `brain/context/relationship-status-{date}.md` that pipeline-manager reads for Section 4 of the morning briefing.

**Fallback:** If the relationship-status artifact doesn't exist (relationship-manager didn't run), pipeline-manager does a lightweight Attio People query to surface any contacts with overdue nurture cadences for the briefing. This fallback will be removed once relationship-manager is proven stable.

### Sub-Agent 3: Granola Agent
**Scope:** All meeting transcripts since last run
**Scans:** Granola MCP for transcripts, extracts action items, next steps, commitments, intro promises
**Returns:** Proposed Motion tasks with titles, descriptions, due dates

### Stop Hooks (post-execution validation)
1. **Pipeline validation** — confirms all approved stage changes were executed in Attio Lists
2. **Relationships validation** — confirms all approved People attribute updates were executed, no blank next_actions left behind
3. **Granola ingestion validation** — count meetings returned by `mcp__granola__list_meetings` vs files actually written to `brain/calls/`. Every meeting must have a corresponding file (or an idempotency skip logged). Mismatch = data loss.
4. **Gmail ingestion validation** — count actionable emails identified during ingestion vs inbox files written to `brain/inbox/`. Every actionable email must have a corresponding file (or an idempotency skip logged). Mismatch = dropped action items.
5. **Motion task validation** — for every approved action item (outreach tasks, follow-up tasks, Granola action items), verify a corresponding Motion task was created via the Motion API (`GET /tasks`). Compare approved count vs created count. Mismatch = tasks Kay thinks exist but don't.
6. **Niche signal validation** — if any niche signals were detected during data ingestion, confirm each was written to `brain/inbox/` with the `topic/niche-signal` tag. Glob `brain/inbox/*niche-signal*` and verify count matches signals detected. Missing signals = lost intelligence for Friday's niche run.
7. **Slack notification validation** — confirm the Slack webhook POST returned HTTP 200 OK. If non-200, retry once. If still failing, warn Kay directly in the session summary that Slack notification failed.
8. **ACTIVE DEALS folder sync** — compare ACTIVE DEALS Drive subfolders against Attio Active Deals entries. Every folder must have a matching Attio entry. Any orphaned folder = missed deal entry. Create Attio entry and flag in morning briefing.
9. **CIM auto-trigger validation** — for every CIM detected during Gmail ingestion, verify all 4 steps completed: (a) ACTIVE DEALS folder exists with CIM/ subfolder, (b) CIM file uploaded to CIM/ subfolder with size > 0, (c) inbox item written to `brain/inbox/` with `urgency: critical` and `topic/cim-received` tag, (d) deal-evaluation was invoked with `source: intermediary-inbound`. If any step failed, retry once. If still failing, flag in morning briefing: "CIM auto-trigger incomplete for {company} — {which step failed}." A missed CIM is a missed deal.
10. **Attio-Target Sheet Reconciliation** — after the morning scan completes, compare Attio Active Deals stages against target sheet outreach columns for all active targets. Use col-lookup.py to resolve header names to cells (never hardcode column letters):
   - For each Attio entry at "Identified": check target sheet "Day 0 Sent" column. If sheet has a date → MISMATCH. Auto-advance Attio to "Contacted" and log.
   - For each Attio entry at "Contacted": if "JJ: Call Status" = "Connected" + positive sentiment → MISMATCH. Flag for review (potential First Conversation).
   This reconciliation runs as a safety net — it catches drift that the real-time detection missed.

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

If any section is missing, re-run the corresponding ingestion step (e.g., missing Draft Status → re-run Superhuman draft check). If the file doesn't exist at all, the entire Gmail ingestion failed — log error and retry once before alerting Kay.

### Manager Red Flags
The manager raises these to Kay before executing:
- Conflicting signals (email says deal killed but calendar shows meeting scheduled)
- Missing data (meeting happened but no Granola transcript and no call notes)
- Unusual patterns (deal jumping 2+ stages, contact going from Dormant to active without clear signal)
- Sub-agent returned empty results when activity was expected

### Manager Quality Review (CRITICAL — runs before presenting to Kay)

Before presenting the briefing, the manager (Claude orchestrator) MUST review all sub-agent outputs for these errors:

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

The manager is the last line of defense. Sub-agents will make errors. The manager catches them so Kay doesn't have to.

## Data Ingestion (runs before signal detection)

Before scanning for signals, ingest new data from external tools into the vault. The vault is the single source of truth.

### Granola → brain/calls/
1. Query `mcp__granola__list_meetings` for meetings since last run
2. For each new meeting, get full transcript via `mcp__granola__get_meeting_transcript`
3. Check idempotency: if `call_id` already exists in brain/calls/, skip
4. Write to `brain/calls/YYYY-MM-DD-{slug}.md` using call schema (schemas/vault/call.yaml)
5. Set `source: granola`, populate people/companies as wiki-links, generate tags
6. Create any missing entities in brain/entities/

### Superhuman Draft Status Check
Check Superhuman for the status of outreach drafts created by outreach-manager. NOTE: Drafts are created via superhuman-cli Bash command (NOT the MCP `superhuman_draft` tool which uses Gmail API). Use `superhuman_search` MCP or check sent folder to determine if drafts were sent.

Results from this check feed directly into the **Draft Status** section of `brain/context/email-scan-results-{YYYY-MM-DD}.md` (see Email Scan Results Artifact below).

1. Query Superhuman for all drafts and recently sent emails matching known outreach targets
2. For each draft that was sent:
   - Update Attio: move target from "Identified" to "Contacted" (source: Gmail sent folder scan + target sheet "Day 0 Sent" column)
   - Log the sent date in the email-scan-results artifact
3. For drafts still unsent, flag with escalating urgency:
   - **Thank-you drafts (time-sensitive):**
     - Unsent after 24 hours: "Thank-you to {name} still unsent. Approaching 48-hour window."
     - Unsent after 48 hours: "Thank-you to {name} is 48+ hours old. Send today or it loses impact."
   - **Outreach drafts (less urgent):**
     - Unsent after 2+ business days: "{n} outreach drafts unsent in Superhuman. Review and send?"
4. For any replies detected (responses to outreach emails):
   - Flag as high-priority pipeline signal
   - Recommend stage change based on reply content

This is how the system knows Kay sent the email and triggers the Attio stage advancement. Claude manages follow-up cadence via Superhuman drafts (Day 3/14 follow-ups drafted each morning). JJ's call list is managed independently by jj-operations.

### Outbound Email Scan (catches manually-sent emails)
The Superhuman Draft Status Check above only catches emails that originated as outreach-manager drafts. Kay also sends emails manually — typed directly in Superhuman, forwarded from another thread, or replied inline. These must also trigger pipeline stage changes.

1. Query Gmail for all outbound emails:
   ```bash
   gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:2d" --json --max 50
   ```
2. For each sent email, extract the recipient address(es) and cross-reference against Attio Active Deals entries at "Identified" stage (match by contact email, company domain, or contact name)
3. **When a match is found:**
   - Move Attio Active Deals entry from "Identified" → "Contacted" (source: Gmail sent folder scan + target sheet "Day 0 Sent" column)
   - Log the signal: record sent date, recipient, and subject in the email-scan-results artifact under Draft Status → Sent
4. **Deduplication:** Skip any recipient already captured by the Superhuman Draft Status Check above (avoid double-processing outreach-manager drafts that were sent). Use the recipient email as the dedup key.
5. **Scope:** Only process emails sent to external recipients. Ignore internal emails (to @greenwichandbarrow.com addresses).

This ensures manually-sent outreach emails (not just outreach-manager drafts) trigger the Attio stage change (Identified → Contacted). Claude manages follow-up cadence via Superhuman drafts for all targets.


### Cadence Advancement (runs during morning scan)

The target sheet is the source of truth for outreach cadence status. Claude manages cadence tracking via per-touchpoint date columns on the target sheet. Pipeline-manager reads these columns to detect cadence progression. All column references use header names resolved by col-lookup.py — never hardcoded letters.

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

2. **Follow-up emails:** Claude drafts Day 3/14 follow-ups in Superhuman each morning. Pipeline-manager checks "Day 0 Sent" / "Day 3 Sent" dates to identify targets due for follow-up based on business days elapsed.

3. **Reply detected (any stage):** If inbound email from target detected in Gmail:
   → Update Attio to "Engaged", set "Cadence Status" to "Replied" on target sheet
   → Advance Attio stage as appropriate (Contacted → First Conversation if reply is substantive)
   → Flag in briefing as high-priority pipeline signal

4. **Cadence complete (no response):** If "Day 14 Sent" has a date and no reply after 7 business days:
   → Present: "{owner} at {company} — cadence complete, no response. Move to nurture?"

### New Approval Detection

For each row where "Kay: Decision" = "Approve" and "Day 0 Sent" is blank (no cadence started):
→ These are newly approved targets. Signal outreach-manager to draft initial outreach in Superhuman.
→ Present in briefing: "{n} new approvals on {niche} target list. Outreach drafts queued."

### Conference Decision Scan
Conference decisions (Col M = "Attend"/"Register Only") are now handled by conference-discovery. Pipeline-manager does not scan the Conference Pipeline sheet.

### Target List Monitoring (JJ Call Outcomes)
Read the active niche sprint's master sheet ("{Niche} - Target List") in LINKT TARGET LISTS folder. Scan JJ's call columns (Q-T) for new entries since last scan:
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
| Active-Outreach | Full owner outreach active. | 4-6 targets/day | Full cadence via Superhuman drafts (Claude-managed) |
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

### JJ Daily Call Prep

JJ call prep, Call Log creation, 10am Slack delivery, and post-shift outcome harvesting are now handled by jj-operations. Pipeline-manager reads JJ call outcomes from the master target sheet for stage change signals (e.g., "Connected + Interested" triggers First Conversation recommendation in the morning briefing).

### Warm Intro Detection
When processing new targets (from target-discovery handoff), scan for warm intro paths before presenting to Kay:
- Search Attio People records for connections to the target's company or owner
- Search vault entities for any prior mentions
- Search Gmail for any prior correspondence with the company or person
- If a warm path exists, flag it: "Warm intro possible via {contact name} — {how connected}"

This replaces the previous approach where Kay manually flagged warm intros. The agent does the research, Kay just sees the result.

### Gmail → brain/inbox/
1. Query `gog gmail search "newer_than:2d label:INBOX" --json --max 50` for recent inbound emails (outbound scanning is handled separately by the Outbound Email Scan step above)
2. Parse for actionable items: explicit requests, questions, deadlines, documents needing action
3. Check idempotency: if `source_ref` (message ID) already exists in brain/inbox/, skip
4. Write to `brain/inbox/YYYY-MM-DD-{slug}.md` using inbox schema (schemas/vault/inbox.yaml)
5. Set `source: email`, assign confidence level (high/medium/low)
6. High confidence items surface in Part 1. Medium/low go to /triage.

### Deal Flow Email Classification (absorbed from lead-aggregator Channel 2)

During Gmail ingestion, every email labeled "DEAL FLOW" must be classified as one of three categories. Classification counts (DIRECT/BLAST/NEWSLETTER) are written to the email-scan-results artifact for downstream consumption.

1. **BLAST** — BCC'd distribution, generic greeting, "New Listing" subject, sent to broker's full network of 3000+. Agent screens against buy box. **Revenue floor (auto-reject):** Any deal with stated revenue below $1.5M is auto-rejected regardless of industry fit or broker relationship — archive silently, do not flag, do not Slack, do not surface. These are too small. Remaining deals above the revenue floor are screened against active thesis criteria and the financial buy box ($1-5M EBITDA, $3-20M revenue, independently owned). Matches → Slack ping to #active-deals. No match → archive silently. Kay never sees BLAST emails unless there's a match above the revenue floor that passes the buy box.

2. **DIRECT** — Addressed to Kay by name, references prior conversation or specific criteria Kay shared, expects a response, may include "Introduction" or "RE:" in subject, sometimes has CIM/teaser attached. These ALWAYS get surfaced to Kay — never auto-archived. Present in morning briefing via Inbound Intermediary Deal Detection flow.

3. **NEWSLETTER** — Industry newsletters, deal roundups, educational content (e.g., Helen Guo / SMB Deal Hunter). Not actionable deal flow. Move to a "DEAL FLOW/ARCHIVE" label. Scan for niche signals only — patterns in what industries are being listed, new niche ideas.

**Pattern detection for classification:**
- BCC header present → BLAST
- Kay's name in greeting ("Hi Kay", "Dear Kay") + personalized context → DIRECT
- Unsubscribe link + no personalization → NEWSLETTER or BLAST
- Sender in Attio Intermediary Pipeline at "Warmed" or higher + personalized → DIRECT
- Sender not in Attio + mass-email patterns → BLAST

**Guardrail:** When uncertain, default to DIRECT. It's better to surface an email Kay doesn't need than to archive one that needed a response.

### Email Scan Results Artifact

After Gmail ingestion completes (including deal flow classification and Superhuman draft status check), write a structured results file so downstream skills (e.g., /start, lead-aggregator) can read email findings without re-scanning Gmail.

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
{For each email where both a Superhuman draft AND a matching sent email exist:}
- **{recipient} — {subject}**
  - Draft: {first 2 lines of original draft}
  - Sent: {first 2 lines of what Kay actually sent}
  - Edits: {summary of changes — tone, length, phrases added/removed, structure}
{If no draft-vs-sent pairs found: "No draft calibration data today."}
```

**Draft Status population:** The Superhuman Draft Status Check AND the Outbound Email Scan (see sections above) both feed this section. For each outreach or thank-you draft created by outreach-manager or pipeline-manager:
- Check Superhuman sent folder / `superhuman_search` MCP for matching sent emails
- If sent: record target name, company, and sent date
- If unsent: record target name, company, and age in days since draft was created

For each manually-sent email detected by the Outbound Email Scan that matched an Attio Active Deals entry:
- Record target name, company, sent date, and note "(manual — not from draft)"
- This gives downstream skills (and Kay's morning review) a single place to see what was sent vs. pending without re-querying Superhuman or Gmail.

This artifact is the handoff contract between pipeline-manager (which scans Gmail and checks Superhuman) and downstream consumers (/start, lead-aggregator). They never scan Gmail directly — they read this file.

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
- Skips JJ confirmation call — the intro IS the warm touch
- Higher priority than cold targets in the daily review
- Also draft a thank-you email to the introducer

**Cadence for warm intros:**
| Day | Channel | Action |
|-----|---------|--------|
| Day 1 | Email (Superhuman) | Warm intro email referencing introducer |
| Day 1 | Email (Superhuman) | Thank-you to introducer |
| Day 5-6 | Email (Superhuman) | Follow-up if no response |
| Day 8-10 | LinkedIn DM (Kay) | High-value only |

No Day 3 JJ call. The introducer already warmed the connection.

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
1. **Check Attio Intermediary Pipeline** — is the sender (or their firm) already tracked?
   - If yes: tag as `source/intermediary-inbound`, associate with existing intermediary record
   - If no: create a new entity at `brain/entities/{slug}.md`, add to Attio Intermediary Pipeline at "Identified" stage with `how_introduced: "Inbound deal email, {date}"`
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
- These are lower-confidence but still trigger the fast-track if from a known intermediary (already in Attio Intermediary Pipeline at "Warmed" or later)

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
gog gmail attachment {message_id} {attachment_id} --output /tmp/{filename}

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
- Create Attio Active Deals entry at "Financials Received" stage (CIM = financials) with `source: intermediary`
- If intermediary is at "Identified" or "Contacted" in Intermediary Pipeline: recommend stage change to "Actively Receiving Deal Flow"
- Create vault entity for the target company if it doesn't exist

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
- **CIM from unknown sender (not in Attio Intermediary Pipeline):** Still fast-track the CIM filing. Create the intermediary entity and Attio entry at "Identified" stage. Flag in morning briefing: "New intermediary detected: {name} at {firm}. Sent CIM for {company}."

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
  Intermediary status: {Attio stage or "New — just added to Intermediary Pipeline"}
  Deal: {Company name or "Blind profile"}
  Industry: {if stated}
  Revenue: {if stated, else "Not disclosed"}
  EBITDA: {if stated, else "Not disclosed"}
  Geography: {if stated}
  Attachment: {CIM/teaser/profile filename}

  Screen against buy box?
  - Yes → fast-track to deal-evaluation (intermediary buy-box screen)
  - Pass → draft polite decline to intermediary
  - Need more info → draft reply requesting key financials
  - Save for later → keep in inbox, revisit Friday
```

### On Kay's Approval
- **"Proceed"** (CIM auto-screened) → continue deal-evaluation at Phase 3 (financial analysis on the CIM already in Drive). The buy-box screen is done — this advances to deep analysis.
- **"Yes"** (no CIM) → trigger deal-evaluation skill with `source: intermediary-inbound` and `intermediary: {name}`. The deal-evaluation skill runs its fast buy-box screen (see deal-evaluation Intermediary Inbound Pathway).
- **"Pass"** → draft a short, polite decline email to the intermediary. Log the deal in vault with reason. Tag the intermediary's Attio record with the deal type they sent (e.g., `sends: manufacturing`, `sends: healthcare`) for future filtering.
- **"Need more info"** → draft reply requesting: revenue, EBITDA, years in business, owner age/succession situation, customer concentration. Keep the ask short — intermediaries are busy.
- **"Save for later" / "Table"** → no action, stays in inbox queue.

### Intermediary Relationship Tracking
After processing inbound deals, update the intermediary's Attio record:
- `last_deal_sent: {date}`
- `deal_types_sent: [{industry/type}]` (append, don't overwrite)
- If intermediary is at "Identified" and sent a real deal: recommend stage change to "Actively Receiving Deal Flow"

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
  -d '{"text":"Pipeline updates waiting — {n} recommended changes + {n} stale deals. Open Claude Code to review."}'
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
gog gmail search "after:{YESTERDAY} before:{TODAY}" --json --max 30
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

### Granola (important signal source)
Check for meeting transcripts via Granola MCP. Transcripts capture:
- Action items mentioned during the meeting
- Introductions promised ("I'll connect you with...")
- Next steps agreed to
- Deal-relevant information (financials coming, NDA discussion, etc.)

```
Use mcp__granola__list_meetings to find meetings in the date range
Use mcp__granola__get_meeting_transcript for each meeting's full transcript
```
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

**Intermediary Pipeline signals:**
| Signal | Current Stage | Recommended Stage |
|--------|--------------|-------------------|
| First contact/meeting | Identified | Contacted |
| Positive response, building rapport | Contacted | Warmed |
| Started sending deal flow | Warmed | Actively Receiving Deal Flow |
| Regular deal flow coming in | Actively Receiving Deal Flow | Daily Check in on Matches |

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
- {n} Motion tasks created
```
</execute>

<followup_actions>
## Phase 5: Follow-up Actions

### Upcoming Meeting Prep Triggers

Scan calendar for **tomorrow's investor meetings only** and trigger investor-specific call prep. Pipeline-manager only handles investor call prep (Jeff, Guillermo) because these use specialized templates.

**Meeting prep is handled by meeting-brief-manager (runs nightly at 10pm ET via launchd). Pipeline-manager no longer triggers meeting-brief directly.** All external meeting briefs, new contact research, and general meeting prep are owned by meeting-brief-manager. Do not duplicate that work here.

| Contact | Cadence | Trigger |
|---------|---------|---------|
| Jeff Stevens (Anacapa) | Monthly | `/investor-update call-prep jeff` → saves to INVESTOR COMMUNICATION / MONTHLY |
| Guillermo Lavergne | Bi-weekly | `/investor-update call-prep guillermo` → saves to INVESTOR COMMUNICATION / BI-WEEKLY |

```bash
# Look at tomorrow's calendar for investor meetings only
gog calendar list --from {TOMORROW} --to {TOMORROW} --json
# On Fridays: also run for Monday
# gog calendar list --from {NEXT_MONDAY} --to {NEXT_MONDAY} --json
```

Only investor call prep runs here. Everything else is meeting-brief-manager's responsibility via its nightly launchd schedule.

### Email Verification Gate (CRITICAL — applies to ALL drafts from this skill)

Before creating ANY email draft (thank-you, follow-up, decline, intro), verify the recipient email:
- **Prior correspondence exists** (Kay has emailed/received email from this address) → verified, proceed
- **Apollo-verified email** → proceed (all emails verified via Apollo people match)
- **All other emails** → run through Apollo API verification. Only proceed if `verified`. If `guessed`/`unavailable`/`bounced`, tell Kay: "no verified email for {name}" and stop. NEVER guess an email from name + domain.

Bounced emails damage Kay's sender domain reputation. Her email is her entire business.

### Follow-Up Actions

After pipeline updates, surface any follow-up tasks:

- **"Need to Send Thank You"** → FIRST verify Kay hasn't already sent the thank you (search `from:kay.s@greenwichandbarrow.com to:{contact_email} newer_than:7d`). If already sent, auto-move to Nurture and skip. If not sent, draft a personalized thank you email using Kay's voice (see memory: user_outreach_voice.md). Reference specifics from the meeting (Granola transcript, call notes, or calendar context). Create as Superhuman draft via `~/.local/bin/superhuman-draft.sh`.
- **Introduction promised** → ask Kay for the person's name/company. Create `brain/entities/{slug}.md` in the vault with proper schema. Add them to the appropriate Attio pipeline at "Identified" stage. When the intro email arrives later, they're already tracked.
- **Introduction received** → match the intro email to the tracked entity, move to "Contacted" stage
- **NDA Executed** → remind to request financials if not already received
- **Financials Received** → flag for financial modeling
- **Stale deals** → suggest kill/advance/table decision
- **Meeting action items → Motion tasks** — Parse Granola transcript for action items, next steps, and commitments. For each, create a Motion task via `/motion` skill with:
  - Title: the action item
  - Description: context from the meeting
  - Due date: based on urgency/commitment made
  - Project: mapped to the relevant pipeline (e.g., Active Deals project for deal-related actions)

  Present all proposed tasks to Kay for approval before creating. She may want to adjust priority, due date, or skip some.

**Post-meeting flow (complete sequence):**
1. Detect meeting from calendar + Granola transcript
2. Recommend pipeline stage change → Kay approves
3. Draft thank you email → Kay reviews → create Motion task with due date
4. Create entities for promised introductions → Kay confirms names
5. Extract action items from Granola → create Motion tasks → Kay approves
6. Any outreach needed (e.g., new broker intro) → draft email → create Motion task

**Motion task creation:** Every follow-up action that Kay approves should also become a Motion task via `/motion` skill. Examples:
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
- [ ] Motion tasks created for all approved follow-up actions
- [ ] Summary confirmed to user
</success_criteria>

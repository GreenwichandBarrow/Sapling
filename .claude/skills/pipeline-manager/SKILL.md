---
name: pipeline-manager
description: "Daily pipeline management — scans yesterday's activity, recommends stage changes, Kay approves/rejects, Attio updates automatically. Flags stale deals. Runs on session start via hook."
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

**Part 1: Pipeline Updates (Intermediary, Active Deals, Investor)**
Present stage change recommendations one at a time. Kay approves/rejects.

**Part 2: Network Relationship Updates (People Records)**
1. **Recent contacts** — "You met Dan Tanzilli yesterday. Update next_action to 'follow up on art attorney intro'?"
2. **Stale next_actions** — "You've had 'send thank you to Denning' as next_action for 2 weeks. Still pending?"
3. **New contacts to add** — "You met someone new at the One Hanover happy hour. Add them?"

Each recommendation updates the People record on approval.

**Part 2b: Nurture Reminders**
After relationship updates, check ALL People with nurture_cadence set against their `last_interaction` date in Attio. Surface anyone overdue:

"Consider following up with {name} ({relationship_type}, {nurture_cadence}). Last contact: {date}."
- **Approve** → Motion task created: "Follow up with {name}" with appropriate due date
- **Skip** → no action
- **Snooze** → skip for 1 week, surface again next run

Cadence thresholds:
- Weekly: overdue after 10 days
- Monthly: overdue after 5 weeks
- Quarterly: overdue after 14 weeks
- Occasionally: overdue after 7 months
- Dormant: never surfaced

Present max 5 nurture reminders per session to avoid overwhelm. Prioritize by: relationship value (value_to_search), days overdue, relationship_type.

## Architecture: Manager + 3 Specialized Sub-Agents

Claude acts as the **manager** overseeing 3 specialized sub-agents that run in parallel on session start. The manager:
- Launches all 3 agents simultaneously
- Reviews their outputs for quality and consistency
- Flags any red flags or conflicts to Kay before presenting
- Presents recommendations sequentially: pipelines → relationships → tasks
- Executes approved changes
- Runs stop hooks to validate execution

### Sub-Agent 1: Pipeline Agent
**Scope:** Intermediary, Active Deals, and Investor Lists
**Scans:** Email (NDAs, financials, LOIs, broker correspondence), calendar (deal meetings), vault (call notes)
**Returns:** Stage change recommendations with signal evidence

### Sub-Agent 2: Relationships Agent
**Scope:** People records with custom attributes
**Scans:** Calendar (meetings with contacts), email (thank yous sent, intros received), overdue nurture cadences
**Returns:** Attribute update recommendations (next_action, nurture_cadence, relationship_type)

### Sub-Agent 3: Granola Agent
**Scope:** All meeting transcripts since last run
**Scans:** Granola MCP for transcripts, extracts action items, next steps, commitments, intro promises
**Returns:** Proposed Motion tasks with titles, descriptions, due dates

### Stop Hooks (post-execution validation)
1. **Pipeline validation** — confirms all approved stage changes were executed in Attio Lists
2. **Relationships validation** — confirms all approved People attribute updates were executed, no blank next_actions left behind

### Manager Red Flags
The manager raises these to Kay before executing:
- Conflicting signals (email says deal killed but calendar shows meeting scheduled)
- Missing data (meeting happened but no Granola transcript and no call notes)
- Unusual patterns (deal jumping 2+ stages, contact going from Dormant to active without clear signal)
- Sub-agent returned empty results when activity was expected

## Data Ingestion (runs before signal detection)

Before scanning for signals, ingest new data from external tools into the vault. The vault is the single source of truth.

### Granola → brain/calls/
1. Query `mcp__granola__list_meetings` for meetings since last run
2. For each new meeting, get full transcript via `mcp__granola__get_meeting_transcript`
3. Check idempotency: if `call_id` already exists in brain/calls/, skip
4. Write to `brain/calls/YYYY-MM-DD-{slug}.md` using call schema (schemas/vault/call.yaml)
5. Set `source: granola`, populate people/companies as wiki-links, generate tags
6. Create any missing entities in brain/entities/

### Gmail → brain/inbox/
1. Query `gog gmail search "newer_than:2d" --json --max 50` for recent emails
2. Parse for actionable items: explicit requests, questions, deadlines, documents needing action
3. Check idempotency: if `source_ref` (message ID) already exists in brain/inbox/, skip
4. Write to `brain/inbox/YYYY-MM-DD-{slug}.md` using inbox schema (schemas/vault/inbox.yaml)
5. Set `source: email`, assign confidence level (high/medium/low)
6. High confidence items surface in Part 1. Medium/low go to /triage.

## Trigger

- **Auto:** Runs on session start via hook (before `/start` daily workflow)
- **Manual:** `/pipeline-manager` on demand

## Slack Notification

Send a nudge only (not full detail):
```bash
curl -s -X POST "SLACK_WEBHOOK_REDACTED" \
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
gog calendar list --from {YESTERDAY} --to {TODAY} --json
```
Extract all external meetings (skip internal/team calls). Each meeting is a signal that a pipeline entry may need updating.

### Gmail
```bash
gog gmail search "after:{YESTERDAY} before:{TODAY}" --json --max 30
```
Look for:
- NDA documents (PDF attachments with "NDA" in subject/filename) → NDA Executed
- Financial documents (CIM, P&L, balance sheet) → Financials Received
- LOI drafts or signed documents → LOI stage changes
- Thank you emails sent → move from "Need to Send Thank You" to nurture
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
| NDA document in email | Any pre-NDA | NDA Executed |
| Financials/CIM received | NDA Executed | Financials Received |
| Started modeling/analysis | Financials Received | Active Diligence |
| LOI drafted/sent | Active Diligence | LOI / Offer Submitted |
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

After pipeline updates, surface any follow-up tasks:

- **"Need to Send Thank You"** → immediately draft a personalized thank you email using Kay's voice (see memory: user_outreach_voice.md). Reference specifics from the meeting (Granola transcript, call notes, or calendar context). Present draft for Kay's review, then queue to send via gog gmail.
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

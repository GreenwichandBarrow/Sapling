---
name: pipeline-manager
description: "Daily morning briefing — pipeline stage changes, outreach recommendations (nurture cadence), and action items (Granola). Kay reviews, approved items become Motion tasks automatically. Runs on session start."
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

After gathering all data from the 5 sections above, RE-ORGANIZE the output into these three action categories. This is what Kay sees. Items from any section can land in any category based on what the action is.

```
Pipeline shifts to review/approve:
1. {Company}: {current stage} → {recommended stage} ({signal evidence})
2. {Contact}: nurture overdue, last contact {date}
3. ...

Action steps for Motion - review/approve:
1. {Action item from Granola/email/signal} — due {date}
2. {Follow up with person} — {context}
3. ...

Email drafts for your review in Superhuman:
1. {Thank you to person} — re: {meeting/context}
2. {Follow up email to person} — re: {topic}
3. ...
```

Each item numbered. Each has a clear action. No informational items without an ask.

After Kay reviews all three categories, confirm summary:
```
Pipeline manager complete:
- {n} pipeline stages updated
- {n} tasks created in Motion
- {n} email drafts in Superhuman
- {n} stale deals flagged
```

## Architecture: Manager + 3 Specialized Sub-Agents

Claude acts as the **manager** overseeing 3 specialized sub-agents that run in parallel on session start. The manager:
- Launches all 3 agents simultaneously
- Reviews their outputs for quality and consistency
- Flags any red flags or conflicts to Kay before presenting
- Presents recommendations sequentially: Part 1 (pipeline changes) → Part 2 (outreach/nurture) → Part 3 (action items)
- Executes approved changes
- Runs stop hooks to validate execution

### Sub-Agent 1: Pipeline Agent
**Scope:** Intermediary, Active Deals, and Investor Lists
**Scans:** Email (NDAs, financials, LOIs, broker correspondence), calendar (deal meetings), vault (call notes), Drive ACTIVE DEALS folder (new subfolders)
**Returns:** Stage change recommendations with signal evidence

**ACTIVE DEALS folder detection (catch-all for broker platform NDA edge cases):**
Scan the ACTIVE DEALS Drive folder for any subfolder that does not have a matching Attio Active Deals entry. This catches the case where Kay signs an NDA on a broker platform (no email sent), creates a folder, and saves the NDA manually. When detected:
1. Create Attio Active Deals entry at "NDA Signed" stage with `source: intermediary`
2. Create entity in vault if needed
3. File any documents in the folder into the standard subfolder structure
4. Present in morning briefing: "New deal folder detected: {Company}. Created Attio entry at NDA Signed."

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
3. **Granola ingestion validation** — count meetings returned by `mcp__granola__list_meetings` vs files actually written to `brain/calls/`. Every meeting must have a corresponding file (or an idempotency skip logged). Mismatch = data loss.
4. **Gmail ingestion validation** — count actionable emails identified during ingestion vs inbox files written to `brain/inbox/`. Every actionable email must have a corresponding file (or an idempotency skip logged). Mismatch = dropped action items.
5. **Motion task validation** — for every approved action item (outreach tasks, follow-up tasks, Granola action items), verify a corresponding Motion task was created via the Motion API (`GET /tasks`). Compare approved count vs created count. Mismatch = tasks Kay thinks exist but don't.
6. **Niche signal validation** — if any niche signals were detected during data ingestion, confirm each was written to `brain/inbox/` with the `topic/niche-signal` tag. Glob `brain/inbox/*niche-signal*` and verify count matches signals detected. Missing signals = lost intelligence for Friday's niche run.
7. **Slack notification validation** — confirm the Slack webhook POST returned HTTP 200 OK. If non-200, retry once. If still failing, warn Kay directly in the session summary that Slack notification failed.
8. **ACTIVE DEALS folder sync** — compare ACTIVE DEALS Drive subfolders against Attio Active Deals entries. Every folder must have a matching Attio entry. Any orphaned folder = missed deal entry. Create Attio entry and flag in morning briefing.

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

### Superhuman Draft Status Check
Check Superhuman for the status of outreach drafts created by outreach-manager. NOTE: Drafts are created via superhuman-cli Bash command (NOT the MCP `superhuman_draft` tool which uses Gmail API). Use `superhuman_search` MCP or check sent folder to determine if drafts were sent:
2. For each draft that was sent:
   - Update Attio: move target from "Identified" to "Contacted"
   - Calculate the Day 3 call date (2 business days later) and update JJ's call columns in the master sheet
   - Log the sent date for cadence tracking
3. For drafts still unsent, flag with escalating urgency:
   - **Thank-you drafts (time-sensitive):**
     - Unsent after 24 hours: "Thank-you to {name} still unsent. Approaching 48-hour window."
     - Unsent after 48 hours: "Thank-you to {name} is 48+ hours old. Send today or it loses impact."
   - **Outreach drafts (less urgent):**
     - Unsent after 2+ business days: "{n} outreach drafts unsent in Superhuman. Review and send?"
4. For any replies detected (responses to outreach emails):
   - Flag as high-priority pipeline signal
   - Recommend stage change based on reply content

This is how the system knows Kay sent the email and triggers the rest of the cadence (JJ's Day 3 call, follow-up email at Day 5-6).

### Conference Decision Scan
Check the Conference Pipeline Google Sheet for any row where Kay marked Decision (Col M) = "Attend" or "Register Only" since last scan. For each new decision:
1. Create Motion task: "Register for {conference name}" with deadline 2 days before registration closes (Col G)
2. Provide registration link from conference website (Col J)
3. If attendee list is publicly available (Col I), begin attendee list acquisition
4. Update Status (Col K) to "Registered" after Motion task created
5. Slack Kay: "Saw you picked {conference name} for {date}. Registration task created in Motion. Link: {url}"

Kay picks conferences Monday morning. Pipeline-manager scans overnight. This gives Kay a grace period to change her mind before registration is kicked off.

### Target List Monitoring (JJ Call Outcomes)
Read the active niche sprint's master sheet ("{Niche} - Target List") in LINKT TARGET LISTS folder. Scan JJ's call columns (Q-T) for new entries since last scan:
- New "Connected" + "Interested" → move Attio from "Contacted" to "First Conversation"
- New "Connected" + "Not Selling" → flag for Kay's review (keep or kill?)
- New "Voicemail" → no stage change, note logged
- New "Wrong Number" → flag data quality issue
- New "Not Interested" → move to "Closed / Not Proceeding" or flag for Kay

### JJ Daily Call Prep (10am ET)

**JJ's hours:** 10am - 2pm ET, Mon-Fri. All notifications at 10am, not 9am.

**Overnight (before 10am):**
1. Select 4-6 targets from the master target sheet where Kay: Decision = Approved and JJ: Call Status is empty
2. For each target, create a Call Log doc from template (ID: `1nvvdOU7I5NLAwxrYgHIFTRNrEZmc67X8`):
   - Copy template → save to OPERATIONS / CALL LOGS (`1nGSQIa28fhQ9dXuKdMks_172gyxAinEs`)
   - Name: "Call Log - {Company Name} {M.DD.YY}.docx"
   - Pre-populate COMPANY INFO section from Linkt data in the master target sheet
   - Customize SCRIPT section with company-specific operational signal
3. Send Slack at 10am:

```bash
curl -s -X POST "$SLACK_WEBHOOK_SVA" \
  -H "Content-Type: application/json" \
  -d '{"text":"Good morning JJ. Here are your calls for today:\n\n1. {Owner Name} - {Company}\n   Phone: {phone}\n   Call Log: {google_doc_link}\n\n2. {Owner Name} - {Company}\n   Phone: {phone}\n   Call Log: {google_doc_link}\n\n..."}'
```

**JJ's workflow:** Click link → read script + company info → make call → fill in Call Outcome + Call Notes in the doc. JJ does NOT touch the master target sheet.

**Overnight (after JJ's shift):**
1. Read all Call Log docs updated today in OPERATIONS / CALL LOGS
2. Extract call outcomes and update master target sheet:
   - R: JJ: Call Status ← from Call Status field
   - S: JJ: Call Date ← from Call Date field
   - T: JJ: Call Notes ← summarize detailed notes into one line
   - U: JJ: Owner Sentiment ← from Owner Sentiment field
3. If Call Status = "Interested" → flag for Kay's morning briefing, trigger deal-evaluation Phase 1

JJ webhook posts to #operations-sva channel.

### Warm Intro Detection
When processing new targets (from target-discovery handoff), scan for warm intro paths before presenting to Kay:
- Search Attio People records for connections to the target's company or owner
- Search vault entities for any prior mentions
- Search Gmail for any prior correspondence with the company or person
- If a warm path exists, flag it: "Warm intro possible via {contact name} — {how connected}"

This replaces the previous approach where Kay manually flagged warm intros. The agent does the research, Kay just sees the result.

### Gmail → brain/inbox/
1. Query `gog gmail search "newer_than:2d" --json --max 50` for recent emails
2. Parse for actionable items: explicit requests, questions, deadlines, documents needing action
3. Check idempotency: if `source_ref` (message ID) already exists in brain/inbox/, skip
4. Write to `brain/inbox/YYYY-MM-DD-{slug}.md` using inbox schema (schemas/vault/inbox.yaml)
5. Set `source: email`, assign confidence level (high/medium/low)
6. High confidence items surface in Part 1. Medium/low go to /triage.

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

### Morning Review Presentation

Present inbound intermediary deals as a **separate category BEFORE Part 1 (pipeline changes)**:

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
- **"Yes"** → trigger deal-evaluation skill with `source: intermediary-inbound` and `intermediary: {name}`. The deal-evaluation skill runs its fast buy-box screen (see deal-evaluation Intermediary Inbound Pathway).
- **"Pass"** → draft a short, polite decline email to the intermediary. Log the deal in vault with reason. Tag the intermediary's Attio record with the deal type they sent (e.g., `sends: manufacturing`, `sends: healthcare`) for future filtering.
- **"Need more info"** → draft reply requesting: revenue, EBITDA, years in business, owner age/succession situation, customer concentration. Keep the ask short — intermediaries are busy.
- **"Save for later"** → no action, stays in inbox queue.

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

Check the Industry Research Tracker WEEKLY REVIEW tab for any niche with status = "Active":

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins "WEEKLY REVIEW!B3:D20" -a kay.s@greenwichandbarrow.com -j
```

The "Current Status" column (D) has an **orange header** — this is an agent-trigger column. When Kay sets a niche's status to "Active" during the analyst call, it means: run target-discovery on this niche.

**Detection logic:**
1. Read all WEEKLY REVIEW rows
2. For each row where Status = "Active", check if target-discovery is already running for this niche:
   - Check LINKT TARGET LISTS folder for a "{Niche} - Target List" sheet
   - If sheet exists with rows dated today → already running, skip
   - If no sheet or no recent rows → trigger target-discovery
3. Log which niches are in Active sprint to the daily briefing

**When a new "Active" status is detected:**
- Note it in the daily briefing: "New active sprint detected: {Niche Name}. Target discovery will run."
- Target-discovery skill runs automatically for this niche (daily, Mon-Fri)
- Continue running until Kay changes the status away from "Active"

**When status = "Tabled" or "Killed" detected:**

Kay sets these during the analyst call. Pipeline-manager moves the niche to the correct tab overnight:

1. **Read the niche's full row** from WEEKLY REVIEW (cols A-J)
2. **Append to the target tab:**
   - "Tabled" → append to TABLED tab with: Niche Hypothesis, Start Date, "Tabled", Quick notes, Red flags, Score, Why Tabled (from quick notes or ask Kay), What would need to change (from quick notes or ask Kay), Date tabled (today)
   - "Killed" → append to KILLED tab with: Niche Hypothesis, Start Date, "Killed", Quick notes, Red flags, Score, Primary reason (from quick notes or ask Kay), Pattern learned, Date killed (today)
3. **Delete the row from WEEKLY REVIEW** (use gog sheets delete-row or clear the row)
4. **Move the Drive folder:**
   - Tabled: move niche folder from WEEKLY REVIEW or IDEATION Drive folder to TABLED folder (`1_k_c1F11ZNrv4MilATFrURLHdkNx0kRx`)
   - Killed: move niche folder to KILLED folder (`19xsNk5KTVHF2jb6m_li8IAGjcw34nlMX`)
5. **Stop target-discovery** for that niche (no more daily runs)
6. **Log in daily briefing:** "Niche {name} moved to {Tabled/Killed} per analyst call decision."

**Status dropdown values (orange column D):**
- New — just added from pipeline, pending analyst review
- Under Review — analyst evaluating
- Active — triggers target-discovery sprint
- Wind-Down — finish in-flight outreach, no new targets
- Tabled — moves to TABLED tab overnight
- Killed — moves to KILLED tab overnight

**Convention:** The orange column header on any G&B tracker sheet means "this column triggers agent behavior." Kay knows that changing values in orange-header columns will cause agents to act.

### Nightly Audit Stop Hooks

After processing Tabled/Killed moves and re-sorting WEEKLY REVIEW, validate:

**1. Tabled/Killed Move Validation:**
- Re-read the TABLED/KILLED tab to confirm the niche row was appended
- Re-read WEEKLY REVIEW to confirm the row was removed
- If the niche had a Drive folder, verify it was moved to the correct status folder (TABLED or KILLED)
- If target-discovery was running for this niche, verify no Linkt task is still active

**2. Sort Validation:**
- Re-read WEEKLY REVIEW after sorting
- Confirm sort order: Active rows first, then Under Review, then New, then Wind-Down
- Confirm no data was lost during sort (row count before = row count after)

**3. Target List Template Validation (on new Active sprints):**
- When a niche is newly set to "Active," check if a target list sheet exists in LINKT TARGET LISTS
- If no sheet exists, create one from the template with all 23 columns A-W
- Verify orange header on Col O (Kay Decision)

**4. Kay Decision Column Validation (on all active target lists):**
- For each niche with status "Active," read the target list sheet
- Check for any rows where Col O = "Pass" that haven't been moved to the Passed tab
- Move them and preserve all data
- Check for any rows where Col O = "Approve" that aren't yet in Attio — flag for outreach-manager pickup

## Trigger

- **Auto:** Runs on session start via hook (before `/start` daily workflow)
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

### Upcoming Meeting Prep Triggers

Scan calendar 2 days ahead. If upcoming meetings match these contacts, trigger the appropriate skill:

| Contact | Cadence | Trigger |
|---------|---------|---------|
| Jeff Stevens (Anacapa) | Monthly | `/investor-update call-prep jeff` → saves to INVESTOR COMMUNICATION / MONTHLY |
| Guillermo Lavergne | Bi-weekly | `/investor-update call-prep guillermo` → saves to INVESTOR COMMUNICATION / BI-WEEKLY |
| Any new external contact | As needed | `/meeting-brief {contact}` → saves to RESEARCH / BRIEFS |

```bash
# Look 2 days ahead for investor calls
gog calendar list --from {TODAY} --to {DAY_AFTER_TOMORROW} --json
# If Jeff Stevens or Guillermo Lavergne appears, trigger call prep
```

Brief is ready the next morning, one full day before the call. Slack ping to #operations with the doc link.

### Follow-Up Actions

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

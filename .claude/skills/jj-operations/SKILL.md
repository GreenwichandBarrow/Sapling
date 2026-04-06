---
name: jj-operations
description: "JJ daily call prep, call log creation, 10am Slack delivery, and post-shift outcome harvesting. Owns all JJ-facing operations."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage JJ's daily calling operations end-to-end. JJ is a VA (Philippines) working Mon-Fri 10am-2pm ET. This skill handles:
1. Overnight call prep (target selection, reply checking, Call Log doc creation)
2. 10am Slack delivery (call list with links)
3. Post-shift outcome harvesting (reading Call Logs, updating master sheet)

JJ does NOT touch the master target sheet. He works from Call Log docs and Slack messages only.

**Two run modes:**
- `prep` — overnight before 10am, selects targets and creates Call Logs
- `harvest` — overnight after 2pm, reads completed Call Logs and updates the sheet

**This skill does NOT:**
- Create outreach drafts (that's outreach-manager)
- Decide which targets get approved (that's Kay via the tracker)
- Manage the target list sheet (that's target-discovery)
- Move Attio pipeline stages (that's pipeline-manager)
</objective>

<call_prep>
## Mode: Prep (Before 10am ET)

### 1. Target Selection

**JJ is decoupled from Salesforge cold outreach cadences.** JJ's call list is managed independently by jj-operations, not triggered by email send events. Targets come from Kay's approvals and the ad-hoc queue, not from Col X.

Read the active niche sprint's master sheet ("{Niche} - Target List"). Select targets where:
- Col O (Kay: Decision) = "Approve"
- Col R (JJ: Call Status) is empty
- Target's niche has Outreach Channel = "JJ-Call-Only" on WEEKLY REVIEW (see Channel Filter below)

### Two-Tier Target Selection (Calls-First)

Calls-first niches load 500-1000 targets via Phase 1 volume load. Not all will have owner names yet (owner enrichment happens weekly in Phase 2). JJ handles both tiers:

**Tier 1 (enriched):** Col J (Owner Name) is populated. JJ asks the gatekeeper for the owner by name: "Is {Owner Name} available?" Higher conversion.

**Tier 2 (raw):** Col J (Owner Name) is blank. JJ uses generic opener: "May I speak with the owner or person in charge?" Lower conversion but still valuable. JJ can extract the owner's name from the call for future attempts.

**Daily target selection priority:**
1. Fill from Tier 1 first (up to 40)
2. If Tier 1 has fewer than 40 available, backfill from Tier 2
3. Always prefer Tier 1

**Owner name backfill:** If JJ learns the owner's name during a call (gatekeeper tells him, voicemail greeting, owner introduces themselves), capture it in Call Notes. Harvest mode writes it to Col J — free enrichment from the call itself.

### Channel Filter (CRITICAL)

**Why this exists:** JJ is decoupled from Salesforge email cadences. Calling a target who's in an active email sequence creates conflicting touchpoints.

Before building the call list, read the WEEKLY REVIEW tab to determine which niches route to JJ:

```bash
gog sheets get 1vHx4E1tRTR6V3k7NQeHdCrUjDITJVtZA5YPSIFeSins --range "WEEKLY REVIEW!A3:D20" --json
```

Build a map of **niche name (Col B) → outreach channel (Col D)**. Then for each target sheet:
- Match the sheet's niche to the WEEKLY REVIEW map
- **Include** targets only if their niche's outreach channel = `JJ-Call-Only`
- **Skip** targets if their niche's outreach channel = `Salesforge Email` or any other value
- **HARD STOP:** If a niche is missing from WEEKLY REVIEW, do NOT add ANY targets from that niche to the call list. Flag in morning briefing as requiring manual review. This is a safety gate — unknown channel means unknown routing.

This filter runs BEFORE the reply check — no point checking replies for targets JJ won't call.

**Sheet IDs (all 5 target lists):**
- Art Insurance: `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`
- Domestic TCI: `1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw`
- IPLC: `1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ`
- Art Storage: `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g`
- Art Advisory: `1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0`
- Premium Pest Management: `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`

**Master sheet columns (A-X, 24 columns):**
- A-N: Source through LinkedIn (Company) — list building data
- O: Kay: Decision (Approve/Pass)
- P: Kay: Pass Reason
- Q: Agent Notes (RECOMMEND: Approve/Pass prefix)
- R: JJ: Call Status
- S: JJ: Call Date
- T: JJ: Call Notes
- U: JJ: Owner Sentiment
- V: ICP Match
- W: ICP Miss Reason
- Outreach tracking columns: "Variant", "Day 0 Sent", "Day 3 Sent", "Day 6 DM Sent", "Day 14 Sent", "Cadence Status" (managed by outreach-manager, not read or written by jj-operations)

### Ad-Hoc Call Queue

In addition to niche target sheets, jj-operations reads a "JJ Ad-Hoc Calls" Google Sheet for one-off calls that don't belong to any niche (intermediary follow-ups, conference contacts, warm intro follow-ups, etc.).

**Sheet location:** OPERATIONS folder in Google Drive
**Columns:** A (Company), B (Contact Name), C (Phone), D (Context/Script Notes), E (Target Call Date), F (Priority: Normal/Urgent), G (Call Status: Pending/Called/Voicemail/Connected/Cancelled), H (Call Date), I (Call Notes), J (Source Link)

**Morning prep reads:** Col G = "Pending" AND Col E <= today
**Harvest:** jj-operations reads ad-hoc sheet during harvest mode and updates Col G, H, I.
**Stale check:** If Col E (Target Call Date) is 3+ business days past and Col G is still "Pending", flag in morning briefing.

### 2. Reply Check (CRITICAL)

Before adding ANY target to JJ's call list, search Gmail for replies:
```bash
gog gmail search "from:{target_email}" --max 5 --plain
```
- **Reply found** → Remove from call list. Flag in pipeline-manager's morning briefing: "{owner} at {company} replied. JJ call canceled."
- **No reply** → Proceed with call assignment.

JJ only calls targets who haven't responded. A call after a reply is redundant and could annoy the owner.

### 3. Personal Tidbit (Optional)

For each verified no-reply target, search for one personal detail:
```bash
WebSearch: "{Owner Name}" "{Company Name}"
```
Extract ONE detail: recent award, conference appearance, company anniversary, industry publication, community involvement, or career milestone. Single sentence. If nothing found, leave blank.

### 4. Call Log Creation

For each target, create a Call Log doc from template (ID: `1nvvdOU7I5NLAwxrYgHIFTRNrEZmc67X8`):
- Copy template → save to OPERATIONS / CALL LOGS / TARGET LIST CALLS
- Name: "Call Log - {Company Name} {M.DD.YY}.docx"
- Pre-populate COMPANY INFO from master target sheet
- Customize SCRIPT section with company-specific operational signal
- Add "Personal Note for JJ" field with tidbit (if found)
- Include Howie's email (barrie@greenwichandbarrow.com) for scheduling

### 5. Slack Message Draft

Draft the Slack message and present to Kay for approval before sending. Use two-gate process: Kay approves content, then approves the message draft.

**Call type labels (CRITICAL):** Every call must be labeled OWNER CALL or CALLBACK. JJ needs this before dialing.

**Slack message format:**
```
Hey JJ, here are your calls for today:

OWNER CALL:
1. {Owner Name} - {Company} ({Industry})
   Phone: {phone}
   Call Log: {google_doc_link}

CALLBACK:
2. {Owner Name} - {Company} (follow-up from {date})
   Phone: {phone}
   Call Log: {google_doc_link}

AD-HOC:
{n}. {Contact Name} - {Company} ({context summary})
   Phone: {phone}
   Context: {full context from Col D}
   Call Log: {link}

Dial target today: {n} ({n} owner + {n} callbacks)
```

**Rules:**
- Claude identifies as "Claude" in all JJ messages. Never mention Kay by name.
- Send to #operations-sva channel via SLACK_WEBHOOK_SVA
- JJ dial target: 40 dials/day (1,000/month). Most will be voicemails, gatekeepers, or no-answers — that's expected. Volume is how cold calling works.
- Add at bottom: "Any feedback on this process at all along the way is welcome and appreciated. Any questions, reply here and I will get them to the right person."

### 6. Scheduling Protocol

If owner wants to schedule during JJ's call: JJ books a time with the owner, then emails Howie (barrie@greenwichandbarrow.com) with owner name, owner email, and agreed time. Howie creates the calendar invite.
</call_prep>

<call_harvest>
## Mode: Harvest (After 2pm ET)

### 1. Read Call Logs

Read all Call Log docs updated today in OPERATIONS / CALL LOGS:
- Check for docs with today's date in the filename
- Read Call Outcome and Call Notes fields

### 2. Update Master Sheet

For each completed call, update the master target sheet:
- Col R: JJ: Call Status ← from Call Status field (Connected/Voicemail/No Answer/Wrong Number)
- Col S: JJ: Call Date ← from Call Date field
- Col T: JJ: Call Notes ← summarize detailed notes into one line
- Col U: JJ: Owner Sentiment ← from Owner Sentiment field

### 3. Owner Name Backfill

If JJ's Call Notes or Call Log contain an owner name AND Col J (Owner Name) is blank on the sheet, write the name to Col J. Free enrichment from the call itself.

### 4. Post-Engagement Enrichment (Phase 3 Trigger)

If Call Status = "Connected" AND Owner Sentiment = "Interested" or "Neutral":
1. Run Apollo `/people/match` for email reveal (1 credit) — need email for follow-up
2. Run warm-intro-finder — check if Kay has a connection for a warmer follow-up
3. Flag for pipeline-manager: "JJ connected with {owner} at {company}. Sentiment: {sentiment}. Ready for follow-up."
4. If owner said "send me more info" → draft follow-up email in Superhuman immediately
5. Trigger deal-evaluation Phase 1

### 5. Flag Interested Targets

If Call Status = "Connected" and sentiment is positive → flag for pipeline-manager's morning briefing.
</call_harvest>

<stop_hooks>
## Stop Hooks

### Prep Mode Validation
- [ ] All selected targets passed reply check (no false positives)
- [ ] Call Log docs created in Drive with correct naming
- [ ] Each Call Log has pre-populated company info and customized script
- [ ] Slack message draft matches expected format with correct call type labels
- [ ] Kay approved the Slack message before sending

### Harvest Mode Validation
- [ ] All updated Call Log docs were read
- [ ] Master sheet columns R-U updated for each call
- [ ] Positive-sentiment targets flagged for pipeline-manager
- [ ] No duplicate entries in master sheet
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] JJ receives call list by 10am ET with all links working
- [ ] Call types correctly labeled (OWNER/CALLBACK)
- [ ] No targets with prior replies included in call list
- [ ] Call outcomes harvested same day and sheet updated
- [ ] Interested leads flagged immediately
</success_criteria>

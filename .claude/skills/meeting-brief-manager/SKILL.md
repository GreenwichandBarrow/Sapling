---
name: meeting-brief-manager
description: "Unified meeting prep orchestrator. Scans calendar 2 nights ahead, classifies meetings (external vs investor vs internal), routes to specialized subagents. Runs nightly via launchd."
user_invocable: true
---

<objective>
Unified meeting preparation orchestrator. Scans the calendar two nights ahead, classifies every meeting (internal, investor, external), and routes non-internal meetings to specialized subagents that produce fully formatted briefs with Google Docs and vault copies.

Replaces the standalone meeting-brief skill and absorbs call-prep mode from investor-update.

**Core principle:** Every external or investor meeting Kay walks into should have a brief ready the morning before. Tuesday meeting = brief ready Monday morning. The skill runs the night before that, giving a full day of lead time.
</objective>

<essential_principles>
## When to Trigger

- **Nightly via launchd** — runs every evening, scans calendar for day+2 (two nights ahead)
- **On-demand** — Kay invokes `/meeting-brief-manager` or asks for a meeting brief
- **Pipeline-manager integration** — pipeline-manager can trigger this during its daily scan

## Meeting Classification

Every calendar event is classified into exactly one category:

| Category | Detection Rule | Action |
|----------|---------------|--------|
| **Internal** | All attendees are `@greenwichandbarrow.com` or `@startvirtual.com` | SKIP |
| **Investor** | Any attendee email matches known investor list | Route to Subagent 2 |
| **External** | Everything else | Route to Subagent 1 |

## Known Investor Emails

Detect from Attio Investor Engagement pipeline (list_id: `f9d58294-5fb2-4794-b796-5c9ffa066025`).

Primary investors with regular cadence:
- **Jeff Stevens:** `jeffstevens@anacapapartners.com` (monthly call)
- **Guillermo Lavergne:** `glavergne@ashfordventures.com` (bi-weekly call)

At runtime, also query Attio for the full investor list to catch any investor not hardcoded above.

## Formatting Rules (All Briefs)

- G&B letterhead template (ID: `1hXnexnOTDQwAo4lII2kbsPY3IsbcfKyaJthrAPjGb78`). Logo centered.
- Avenir font, black text only
- No em dashes (U+2014). Use periods, commas, line breaks.
- File naming: `{Subject} {M.DD.YY}` for Google Docs
- Sign off "Very best, Kay" where applicable
- Always show person names, not just companies
- NEVER reference revenue, employee count, or financials in outreach-facing content
- NEVER call G&B a "fund" in owner-facing content
- Budget: single inline bullet `$XXK (XX% remaining of $550K raised) [context]`
- Coded deal names (first 2-3 letters) in investor materials
</essential_principles>

<phase_1>
## Phase 1: Calendar Scan (2 Nights Ahead)

Scan the calendar window from tomorrow through day+3 to catch meetings two days out:

```bash
gog calendar list --from {tomorrow} --to {day+3} --json
```

For each event returned:
1. Extract: event title, date, time, location, attendee emails
2. Classify using the rules above (Internal / Investor / External)
3. Log classification decisions for traceability

**Skip criteria (beyond Internal):**
- Events with no attendees (focus time, reminders)
- All-day events unless they have external attendees
- Events already briefed (check `brain/briefs/{date}-*.md` for existing brief)

**Output:** List of meetings requiring briefs, each tagged with category and routed to the appropriate subagent.
</phase_1>

<phase_2_subagent_1>
## Phase 2 — Subagent 1: External Meeting Brief

Handles all non-investor external meetings. Auto-detects whether the contact is new or a repeat contact in the Active Deals pipeline.

### Step 0: Contact Type Detection

1. Search Attio Active Deals pipeline (list_id: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`) for the person's name or company
2. If found at "First Conversation" stage or later: **repeat contact** (use 8-section template)
3. If not found, or only at "Identified"/"Contacted": **new contact** (use 6-section template)

### Step 1: Parallel Research

Run all of these in parallel:

#### Calendar Context
```bash
gog calendar list --from {meeting_date} --to {meeting_date+1} --json
```
Extract: meeting title, time, location, attendee emails.

#### Email History
```bash
gog gmail search "from:{email} OR to:{email} OR {person_name}" --max 15
```
Look for:
- Who made the introduction and what context they gave
- Prior scheduling correspondence
- Tone and relationship signals

#### Vault Search
- `brain/entities/` — existing entity file for this person or company
- `brain/calls/` — any prior call notes mentioning this person
- `brain/library/internal/salesflare/contacts.json` — legacy CRM data
- `brain/library/internal/salesflare/accounts.json` — legacy company data

#### Granola Transcripts
Query `mcp__granola__query_granola_meetings` filtered by the person's name. Get transcripts for meetings not yet captured in `brain/calls/`.

#### Web Search
```
{Person Name} {Company} {Role}
```
Get: background, company description, LinkedIn summary, recent news.

### Step 2A: New Contact Brief (6 Sections)

```
MEETING BRIEF: {Person Name}
{Meeting Type} | {Day} {Date}, {Time}
{Location}

---

HOW YOU WERE INTRODUCED

{Full connection chain: who introduced whom, when, what context was provided,
what the introducer said about Kay, what they said about the other person.
Note if this is the first conversation or if there's been prior contact.}

---

WHO {FIRST NAME} IS

- {Role and company}
- {What the company does}
- {Background/previous roles}
- {Education/credentials if relevant}
- {Network/relationships of note}

---

HOW THEY COULD BE USEFUL TO YOUR SEARCH

1. {Specific connection to G&B thesis or active niches}
2. {Network/intro potential}
3. {Industry insight they could provide}
4. {Any other strategic value}

---

WHAT TO SHARE ABOUT YOURSELF

- {What they already know. Build on this.}
- {G&B positioning. Tailored to their world.}
- {Relevant thesis angles. Only what resonates with their expertise.}
- {Mutual value framing. What you can offer them.}

---

WHAT NOT TO OVER-SHARE

- {Topics to keep high-level}
- {Things to avoid entirely}

---

SUGGESTED TALKING POINTS

1. {About their business/work}
2. {Specific question connecting their expertise to your search}
3. {Your search. Brief, conversational framing.}
4. {Mutual value. Relationship-first.}
```

### Step 2B: Repeat Contact Brief (8 Sections)

Determine call number first:
```bash
ls brain/calls/*{company-slug}* | wc -l
```
Next call = count + 1.

```
CALL PREP: {Person Name} -- Call #{n}
{Meeting Type} | {Day} {Date}, {Time}
{Location}

---

RELATIONSHIP ARC

{Timeline of all touchpoints:}
- {Date} -- {How introduced, by whom}
- {Date} -- {First email / outreach}
- {Date} -- {Call #1: key topics, outcome}
- {Date} -- {Follow-up email / NDA sent}
- {Date} -- {Call #2: key topics, outcome}
{Continue chronologically...}

---

CURRENT PIPELINE STAGE

Stage: {current stage}
Days at stage: {n}
Next milestone: {what needs to happen to advance}

---

PRIOR CALL NOTES

Call #1 ({date}):
- {Key points discussed}
- {Their concerns / questions}
- {Commitments made by either side}

Call #2 ({date}):
- {Key points discussed}
- {Progress since last call}
- {Open items carried forward}

{Continue for all prior calls...}

---

FINANCIALS STATUS

NDA: {Signed / Not yet / Sent on {date}}
Financials: {Received / Requested / Not yet}
Preliminary numbers: {Revenue, EBITDA, margins if known}
Financial model: {Started / Not yet / Key findings}

---

OPEN QUESTIONS

{Items flagged as "need to follow up" from prior calls that haven't been resolved:}
1. {Question -- from Call #{n}}
2. {Question -- from email on {date}}
3. {Question -- flagged by Kay}

---

WHAT TO PUSH FOR

Based on current stage ({stage}), the next milestone is:
- {E.g., "Get NDA signed so we can request financials"}
- {E.g., "Schedule site visit"}
- {E.g., "Understand customer concentration. Ask for top 10 client list."}
- {Specific questions to advance the deal}

---

SELLER PERSONALITY NOTES

- {Communication style -- formal/casual, responsive/slow}
- {Motivations -- why selling, timeline pressure, emotional attachment}
- {Concerns expressed -- about process, confidentiality, employees, legacy}
- {What resonates -- topics that engaged them, what they care about}

---

RED FLAGS / WATCH ITEMS

- {Anything flagged in prior conversations}
- {Initial screening concerns}
- {Inconsistencies noticed}
- {Items to verify this call}
```

### Step 3: Deliverables (External)

#### Google Doc
Copy G&B letterhead template, rename, populate with brief content:
```bash
gog drive copy "1hXnexnOTDQwAo4lII2kbsPY3IsbcfKyaJthrAPjGb78" "{Person Name} Brief {M.DD.YY}" --parent "1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ"
# Then populate content via gog docs edit or batch update
```
Save to RESEARCH/BRIEFS folder (ID: `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`).

#### Vault File
- New contacts: `brain/briefs/{YYYY-MM-DD}-{person-slug}.md`
- Repeat contacts: `brain/briefs/{YYYY-MM-DD}-{company-slug}-call-{n}.md`

Frontmatter:
```yaml
---
schema_version: "1.0.0"
date: {YYYY-MM-DD}
type: brief
title: "Meeting Brief: {Person Name}"
people: ["[[entities/{person-slug}]]"]
companies: ["[[entities/{company-slug}]]"]
tags:
  - date/{YYYY-MM-DD}
  - brief
  - person/{person-slug}
  - company/{company-slug}
  - source/claude
---
```

Ensure all referenced entities exist in `brain/entities/`. Create entity files if missing.
</phase_2_subagent_1>

<phase_2_subagent_2>
## Phase 2 — Subagent 2: Investor Call Prep

Handles all meetings classified as investor. Produces a 7-section talking points document tailored to the specific investor.

### Step 1: Parallel Research

Run all of these in parallel:

#### Last Call with This Investor
- Query Granola: `mcp__granola__query_granola_meetings` filtered by investor name for last call transcript
- Search vault: `brain/calls/` for notes from prior investor calls
- Search Gmail: `gog gmail search "from:{investor_email} OR to:{investor_email}" --max 20`

#### Current Pipeline State
- Attio Active Deals (list_id: `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`): all deals by stage, recent stage changes
- Recent pipeline movements since last investor call

#### Weekly Tracker Highlights
```bash
gog sheets get "1NGGZY_iq9h8cNzLAXSJ1vTcsfXWNU9oin2RiOMtl9NE" "'Weekly Topline'!A:Z" --json
```
Pull columns since the last call date.

#### Budget Dashboard
```bash
gog sheets get "{BUDGET_DASHBOARD_SHEET_ID}" "'Summary'!A:Z" --json
```
Extract current fund position for the inline budget bullet.

#### Vault Context
- `brain/calls/` — recent calls (all, not just with this investor)
- `brain/entities/{investor-slug}.md` — investor entity file
- `brain/briefs/` — prior call prep files for this investor

### Step 2: Build Call Prep (7 Sections)

```
CALL PREP: {Investor Name} -- {M.DD.YY}
Last call: {date of last call}

---

1. QUICK UPDATE
   - {1-2 sentence headline: what's new since last call}

---

2. LATEST THINKING / APPROACH
   - {Current thesis focus, any strategic pivots}
   - {How the search approach is evolving}

---

3. UPDATE FROM CALLS / TRIPS
   - {Recent owner calls with coded deal names (first 2-3 letters)}
   - {Conference/event takeaways}
   - {Site visits or in-person meetings}

---

4. INDUSTRY BUCKETS
   - {Active niche}: {status, what's working}
   - {Other niche}: {status, tabled/killed/exploring}

---

5. ADDITIONAL CONVERSATIONS
   - {Broker/intermediary conversations}
   - {Network intros received or made}
   - {River guide insights}

---

6. DISCUSS NEXT STEPS
   - {Open items from last call}
   - {Upcoming milestones or decisions}
   - {Ask: "Any deal activity or trends I should be aware of?"}

---

7. INTERESTING TRENDS TO SHARE
   - {Market observations, niche intelligence signals}
   - {Industry news relevant to active niches}
```

### Step 3: Deliverables (Investor)

#### Google Doc
Copy G&B letterhead template, rename, populate:
```bash
gog drive copy "1hXnexnOTDQwAo4lII2kbsPY3IsbcfKyaJthrAPjGb78" "{Investor Name} Call Prep {M.DD.YY}" --parent "{FOLDER_ID}"
```

Route to the correct folder by investor:
- **Jeff Stevens (monthly):** INVESTOR COMMUNICATION / MONTHLY (ID: `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW`)
- **Guillermo Lavergne (bi-weekly):** INVESTOR COMMUNICATION / BI-WEEKLY (ID: `1SFkrxnkBpyng6dWIcW3eDXqab9sf8wui`)

#### Vault File
Save to `brain/briefs/{YYYY-MM-DD}-{investor-slug}-call-prep.md`

Frontmatter:
```yaml
---
schema_version: "1.0.0"
date: {YYYY-MM-DD}
type: brief
title: "Investor Call Prep: {Investor Name}"
people: ["[[entities/{investor-slug}]]"]
companies: ["[[entities/{investor-company-slug}]]"]
tags:
  - date/{YYYY-MM-DD}
  - brief
  - person/{investor-slug}
  - company/{investor-company-slug}
  - topic/investor-update
  - source/claude
---
```

### Investor-Specific Rules

- **Coded deal names:** Use first 2-3 letters only (e.g., ACU, HG, PR). Never use full company names in investor materials.
- **Budget line:** Single inline bullet: `$XXK (XX% remaining of $550K raised) [context]`. No extra metrics or breakdowns.
- **No em dashes.** Periods, commas, line breaks only.
- **"Any deal activity or trends I should be aware of?"** must appear in section 6 every time.
- **Voice:** Direct, confident, honest about progress. Frame pivots as strategic decisions, not failures. Operational improvements (AI tooling) are competitive advantage.
</phase_2_subagent_2>

<phase_3>
## Phase 3: Stop Hooks (ALL Must Pass Before Slack)

Every brief produced by either subagent must pass all applicable checks before the Slack notification is sent. If any check fails, fix the issue and re-validate.

### Check 1: Google Doc Exists in Correct Folder
- External briefs: Doc exists in RESEARCH/BRIEFS (ID: `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`)
- Jeff Stevens: Doc exists in MONTHLY (ID: `1FGxl4_q44sHK-Kv7t1hHfCMfYXA3H9YW`)
- Guillermo Lavergne: Doc exists in BI-WEEKLY (ID: `1SFkrxnkBpyng6dWIcW3eDXqab9sf8wui`)
- Verify the `gog drive copy` returned a valid document ID

### Check 2: Vault Brief Exists
- Confirm the vault file exists at `brain/briefs/{expected-filename}.md`
- Read and parse frontmatter
- Verify all required fields: `schema_version`, `date`, `type`, `title`, `people`, `companies`, `tags`
- If any field is missing, add it and re-save

### Check 3: All Wiki-Linked Entities Exist
- Extract all `[[entities/{slug}]]` references from `people` and `companies` frontmatter
- For each reference, confirm `brain/entities/{slug}.md` exists
- If missing, create the entity with proper schema (read `schemas/vault/entity.yaml` for format)

### Check 4: All Sections Populated
- **New contact external:** All 6 sections (How Introduced, Who They Are, How Useful, What to Share, What Not to Over-Share, Talking Points)
- **Repeat contact external:** All 8 sections (Relationship Arc, Pipeline Stage, Prior Call Notes, Financials Status, Open Questions, What to Push For, Seller Personality, Red Flags)
- **Investor call prep:** All 7 sections (Quick Update, Latest Thinking, Update from Calls/Trips, Industry Buckets, Additional Conversations, Discuss Next Steps, Interesting Trends)
- Empty or placeholder-only sections are not acceptable. Fill with sourced content.

### Check 5: No Em Dashes
- Scan the full content of both Google Doc and vault file for U+2014 (em dash)
- Replace any found with periods, commas, or line breaks
- Also check for U+2013 (en dash) and replace

### Check 6: Doc Uses G&B Letterhead Template
- Verify the doc was created by copying template ID `1hXnexnOTDQwAo4lII2kbsPY3IsbcfKyaJthrAPjGb78`
- Logo must be centered
- Font must be Avenir
- Text must be black only
</phase_3>

<phase_4>
## Phase 4: Consolidated Slack Notification

After ALL briefs pass ALL stop hooks, send a single consolidated Slack notification to #operations.

```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Meeting briefs ready for {date}:\n\n{For each brief:}\n- {Person Name} ({meeting type}, {time}) -- {doc_link}\n\n{n} briefs prepared. All saved to Drive + vault."
  }'
```

**Rules:**
- Single notification, not one per brief
- Every brief entry must include the person's name, meeting type, time, and Google Doc link
- Doc links are mandatory. Never send the notification without them.
- If running via launchd (overnight), notification arrives with the morning batch. No overnight pings.

**If no meetings found:** Do not send a Slack notification. Silent exit.
</phase_4>

<execution_flow>
## Invocation

```
/meeting-brief-manager                    # Full scan: calendar check + classify + route
/meeting-brief-manager {person-name}      # Brief for a specific person's upcoming meeting
/meeting-brief-manager investor {name}    # Force investor call prep for a specific investor
```

## Sub-Agent Summary

| Agent | Category | Task | Parallel? |
|-------|----------|------|-----------|
| Orchestrator | All | Calendar scan, classify, route | First (always) |
| Subagent 1 | External | New or repeat contact brief | Yes (parallel with other subagents) |
| Subagent 2 | Investor | 7-section call prep | Yes (parallel with other subagents) |

If multiple meetings are found on the same target date, subagents for different meetings run in parallel.

## Nightly Automation Flow

```
1. launchd fires meeting-brief-manager
2. Calendar scan: tomorrow + day after tomorrow
3. Classify each meeting
4. Skip internals
5. Route externals to Subagent 1 (parallel if multiple)
6. Route investors to Subagent 2 (parallel if multiple)
7. All stop hooks pass
8. Single consolidated Slack notification
9. Exit
```
</execution_flow>

<success_criteria>
## Success Criteria

### Phase 1: Calendar Scan
- [ ] Calendar queried for correct date window (tomorrow through day+3)
- [ ] Every event classified (Internal / Investor / External)
- [ ] Internal meetings skipped
- [ ] Already-briefed meetings skipped
- [ ] Classification logged

### Subagent 1: External Brief
- [ ] Contact type detected correctly (new vs repeat) via Attio
- [ ] All research sources queried in parallel (calendar, Gmail, vault, Granola, web)
- [ ] New contacts: all 6 sections populated with specific, sourced information
- [ ] Repeat contacts: all 8 sections populated
- [ ] Introduction chain fully traced (not generic)
- [ ] Talking points tailored to the specific person (not boilerplate)
- [ ] Repeat contacts: call number determined and included in filename
- [ ] Repeat contacts: every prior call included in Relationship Arc chronologically
- [ ] Repeat contacts: Open Questions pulled from actual prior conversations
- [ ] Repeat contacts: What to Push For aligned with pipeline stage and next milestone
- [ ] Google Doc saved in RESEARCH/BRIEFS with G&B letterhead
- [ ] Vault file saved in brain/briefs/ with complete frontmatter
- [ ] All referenced entities exist in brain/entities/

### Subagent 2: Investor Call Prep
- [ ] Last call date and summary retrieved (Granola or vault)
- [ ] Current deal/pipeline status included
- [ ] All 7 agenda sections populated (even if some are "No updates since last call")
- [ ] "Any deal activity or trends I should be aware of?" question in section 6
- [ ] Deal names coded (first 2-3 letters only)
- [ ] Budget reported as single inline bullet
- [ ] Google Doc saved to correct investor folder (MONTHLY or BI-WEEKLY)
- [ ] Vault copy saved to brain/briefs/{date}-{investor-slug}-call-prep.md
- [ ] Delivered before the scheduled call time

### Stop Hooks (All Briefs)
- [ ] Google Doc exists in correct Drive folder
- [ ] Vault file exists with all required frontmatter fields
- [ ] All wiki-linked entities exist in brain/entities/
- [ ] All sections populated (6, 7, or 8 depending on type)
- [ ] No em dashes (U+2014) or en dashes (U+2013) in content
- [ ] Doc uses G&B letterhead template (Avenir font, black text, centered logo)

### Notification
- [ ] Single consolidated Slack notification sent to #operations
- [ ] Every brief listed with person name, meeting type, time, and Doc link
- [ ] No notification sent if no meetings found
</success_criteria>

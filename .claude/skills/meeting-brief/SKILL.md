---
name: meeting-brief
description: "Generate meeting prep briefs for external meetings. Auto-detects new vs. repeat contacts and uses the appropriate template. Saves to Google Drive (RESEARCH/BRIEFS) and brain/briefs/."
user_invocable: true
---

<objective>
Generate a concise meeting brief for any upcoming external meeting. Auto-detects whether the contact is new or already in the Active Deals pipeline and uses the appropriate template. New contacts get an intro-focused brief. Repeat contacts get a deal-progression brief with full history, open questions, and what to push for. Saves to Google Drive and the vault automatically.
</objective>

<essential_principles>
## When to Trigger

This skill should run:
- When Kay asks for a meeting brief or prep
- **Proactively, ready the morning before the meeting day.** Tuesday meeting → brief ready Monday morning. Wednesday meeting → brief ready Tuesday morning. Kay reviews it the full day before the meeting.

**How pipeline-manager triggers this:** During its daily calendar scan, pipeline-manager looks 2 days ahead. If it sees a meeting the day after tomorrow with a new contact, it triggers the meeting-brief skill that night. The brief is ready the next morning — one full day before the meeting.

## Core Questions Every Brief Must Answer

1. **How were we introduced?** — Trace the connection chain (who introduced whom, when, context)
2. **Who is this person?** — Role, company, background, relevance
3. **How could they be useful to the search?** — Specific ways they connect to G&B's acquisition thesis
4. **What should Kay share about herself?** — Tailored talking points based on what they already know and what would resonate
5. **What NOT to over-share** — What to keep high-level or avoid entirely

## Mode → Template Mapping (Step 0)

Determine meeting type from the `--type` argument OR from context clues if no flag passed:

| `--type=` | Template | Examples folder | When to use |
|-----------|----------|-----------------|-------------|
| `new-contact` | `templates/new-contact.md` | `examples/new-contact/` | First meeting, warm intro arrival, initial introduction |
| `owner-call` | `templates/owner-call.md` | `examples/owner-call/` | Active Deals pipeline "First Conversation" or later; deal-progression |
| `intermediary` | `templates/intermediary.md` | `examples/intermediary/` | Broker, M&A advisor, law firm partner, wealth advisor |
| `conference-prep` | `templates/conference-prep.md` | `examples/conference-prep/` | Conference, panel, industry event, networking room |

**Auto-detect when --type is absent:**
- Attio match in Active Deals pipeline → `owner-call`
- Vault entity tagged as `Intermediary` / `River Guide` OR sender domain matches `Intermediary Target List` Sheet → `intermediary`
- Event/conference keyword in calendar title (XPX, ACG, NPMA, conference, panel, happy hour, summit) → `conference-prep`
- No Attio match → `new-contact`

**Invariant:** always load `templates/{type}.md` AND `examples/{type}/{most-recent}.md` BEFORE drafting. Fail the run if either is unreadable. Do not fall through to a generic template.

## Delivery

Save to TWO locations, no email:
- **Google Doc** in RESEARCH/BRIEFS folder (ID: `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`) for all types unless a company-specific deal folder already exists (owner-call on active deal → route to that deal folder instead)
- **Vault file** at `brain/briefs/{YYYY-MM-DD}-{person-slug}.md` (new-contact, intermediary, conference-prep) or `brain/briefs/{YYYY-MM-DD}-{company-slug}-call-{n}.md` (owner-call, where n = call number)
</essential_principles>

<quick_start>
## Execution Flow

1. **Identify the meeting** — Check calendar for details (time, location, attendees)
2. **Gather intel** — Run these in parallel:
   - Search Gmail for intro thread / prior correspondence
   - Search brain/ (entities, calls, SalesFlare data) for any existing context
   - Web search for the person and their company
3. **Trace the introduction chain** — Who introduced whom, through whom, what context was given
4. **Assess relevance to the search** — Map their expertise/network to G&B's active niches and thesis
5. **Draft the brief** — Use the template structure below
6. **Save to both locations** — Google Doc + vault file

**READ-SIDE RULE:** When referencing an existing brief (e.g., for a morning briefing or call prep review), always check the Google Drive version first — Kay edits the Google Doc directly. The vault copy is a snapshot from creation time and may be stale. Search Drive: `gog drive search "{person name} call prep" --json` and compare modifiedTime.
</quick_start>

<research_phase>
## Phase 1: Parallel Research

Spawn or run these queries in parallel:

### Calendar
```
gog calendar list --from {date} --to {date} --json
```
Extract: meeting title, time, location, attendee emails.

### Email History
```
gog gmail search "from:{email} OR to:{email} OR {person_name}" --max 15
```
Then read the intro thread. Look for:
- Who made the introduction
- What context they gave about Kay
- What context they gave about the other person
- Any prior scheduling back-and-forth

### Vault Search
- `brain/entities/` — existing entity file?
- `brain/calls/` — any prior call notes?
- `brain/library/internal/salesflare/contacts.json` — CRM data?
- `brain/library/internal/salesflare/accounts.json` — company data?

### Web Search
```
{Person Name} {Company} {Role}
```
Get: background, company description, LinkedIn summary, recent news.
</research_phase>

<brief_structure>
## Phase 2: Brief Structure

Every brief follows this exact structure:

```
MEETING BRIEF: {Person Name}
{Meeting Type} | {Day} {Date}, {Time}
{Location}

—

HOW YOU WERE INTRODUCED

{Full connection chain: who introduced whom, when, what context was provided,
what the introducer said about Kay, what they said about the other person.
Note if this is the first conversation or if there's been prior contact.}

—

WHO {FIRST NAME} IS

• {Role and company — one line}
• {What the company does — one line}
• {Background/previous roles — one line}
• {Education/credentials if relevant — one line}
• {Network/relationships of note — one line}

—

HOW THEY COULD BE USEFUL TO YOUR SEARCH

1. {Specific connection to G&B thesis or active niches}
2. {Network/intro potential}
3. {Industry insight they could provide}
4. {Any other strategic value}

—

WHAT TO SHARE ABOUT YOURSELF

• {What they already know — build on this}
• {G&B positioning — tailored to their world}
• {Relevant thesis angles — only what resonates with their expertise}
• {Mutual value framing — what you can offer them}

—

WHAT NOT TO OVER-SHARE

• {Topics to keep high-level}
• {Things to avoid entirely}

—

SUGGESTED TALKING POINTS

1. {About their business/work}
2. {Specific question connecting their expertise to your search}
3. {Your search — brief, conversational framing}
4. {Mutual value — relationship-first}
```
</brief_structure>

<repeat_contact_flow>
## Repeat Contact Flow (Active Deals pipeline, "First Conversation" stage or later)

### Phase 1R: Parallel Research (Repeat Contact)

Spawn these queries in parallel:

#### Attio Pipeline Data
Query Active Deals pipeline for the company. Extract:
- Current stage and how long at that stage
- All custom attributes (meaningful_conversation checkbox, etc.)
- Entry history (when added, stage progression dates)

#### Prior Call Notes
Search `brain/calls/` for all files mentioning this person or company:
```
grep -r "person/{slug}" brain/calls/
grep -r "[[entities/{slug}]]" brain/calls/
```
Read each call file chronologically. Extract key points, commitments made, questions asked.

#### Granola Transcripts
Query `mcp__granola__list_meetings` filtered by the person's name. Get full transcripts for any meetings not yet in brain/calls/.

#### Email History
```
gog gmail search "from:{email} OR to:{email}" --max 30
```
Full correspondence thread. Note tone, responsiveness, any concerns raised.

#### Financials Status
- Check Attio: NDA executed? Financials received?
- Check Drive: DEALS IN REVIEW/{Company} folder exists? What's in it?
- Check brain/outputs/ for any scorecard or financial model files

### Phase 2R: Call Number
Count prior call files in brain/calls/ for this company to determine call number:
```
ls brain/calls/*{company-slug}* | wc -l
```
Next call = count + 1. Use for filename.

### Phase 3R: Repeat Contact Brief Template

```
CALL PREP: {Person Name} — Call #{n}
{Meeting Type} | {Day} {Date}, {Time}
{Location}

—

RELATIONSHIP ARC

{Timeline of all touchpoints:}
• {Date} — {How introduced, by whom}
• {Date} — {First email / outreach}
• {Date} — {Call #1: key topics, outcome}
• {Date} — {Follow-up email / NDA sent}
• {Date} — {Call #2: key topics, outcome}
{Continue chronologically...}

—

CURRENT PIPELINE STAGE

Stage: {current stage}
Days at stage: {n}
Next milestone: {what needs to happen to advance}

—

PRIOR CALL NOTES

Call #1 ({date}):
• {Key points discussed}
• {Their concerns / questions}
• {Commitments made by either side}

Call #2 ({date}):
• {Key points discussed}
• {Progress since last call}
• {Open items carried forward}

{Continue for all prior calls...}

—

FINANCIALS STATUS

NDA: {Signed / Not yet / Sent on {date}}
Financials: {Received / Requested / Not yet}
Preliminary numbers: {Revenue, EBITDA, margins if known}
Financial model: {Started / Not yet / Key findings}

—

OPEN QUESTIONS

{Items flagged as "need to follow up" from prior calls that haven't been resolved:}
1. {Question — from Call #{n}}
2. {Question — from email on {date}}
3. {Question — flagged by Kay}

—

WHAT TO PUSH FOR

Based on current stage ({stage}), the next milestone is:
• {E.g., "Get NDA signed so we can request financials"}
• {E.g., "Schedule site visit"}
• {E.g., "Understand customer concentration — ask for top 10 client list"}
• {Specific questions to advance the deal}

—

SELLER PERSONALITY NOTES

• {Communication style — formal/casual, responsive/slow}
• {Motivations — why selling, timeline pressure, emotional attachment}
• {Concerns expressed — about process, confidentiality, employees, legacy}
• {What resonates — topics that engaged them, what they care about}

—

RED FLAGS / WATCH ITEMS

• {Anything flagged in prior conversations}
• {Initial screening concerns}
• {Inconsistencies noticed}
• {Items to verify this call}
```
</repeat_contact_flow>

<save_phase>
## Phase 3: Save & Deliver

### Google Doc
Start from the G&B letterhead template (ID: `1PLYz2WH4Zqy4h2gYVqC8SVGyDrvy_ILF`) — copy it, rename, then add brief content. Logo must be centered. Use Avenir font, black text only.
```
gog drive copy "1PLYz2WH4Zqy4h2gYVqC8SVGyDrvy_ILF" "{title}" --parent "1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ"
# Then populate content via gog docs edit or batch update
```

### Vault File
Save to `brain/briefs/{YYYY-MM-DD}-{person-slug}.md` (new contacts) or `brain/briefs/{YYYY-MM-DD}-{company-slug}-call-{n}.md` (repeat contacts) with frontmatter:

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
  - {relevant topic tags}
  - source/claude
---
```

Ensure all referenced entities exist. Create entity files if needed.

### Slack Notification
After saving to both locations, ping Kay via Slack webhook with the Google Doc link so she can open it directly from the notification:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"Meeting brief ready for {Person Name} ({Date}) — saved to Drive & vault.\nhttps://docs.google.com/document/d/{DOC_ID}/edit"}'
```
The Doc link is required — never send the notification without it.

### Confirm to User
Share the Google Doc link so Kay can open it on her phone.
</save_phase>

<validation_phase>
## Phase 4: Validation

Run all validation checks before sending Slack. If any check fails, fix the issue and re-validate.

### 1. Google Doc Validation
Confirm `gog docs create` returned a document ID. Store it as `DOC_ID`.
- If no ID returned, retry the create once. If it fails again, stop and report the error.
- Verify the ID looks valid (non-empty string).

### 2. Vault File Validation
Confirm `brain/briefs/{YYYY-MM-DD}-{person-slug}.md` exists on disk.
- Read the file and parse frontmatter.
- Verify all required fields are present: `schema_version`, `date`, `type`, `title`, `people`, `companies`, `tags`.
- If any field is missing, add it and re-save.

### 3. Entity Validation
Extract all wiki-links from `people` and `companies` frontmatter fields.
- For each `[[entities/{slug}]]` reference, confirm `brain/entities/{slug}.md` exists.
- If any entity file is missing, create it with proper schema before proceeding.
- Re-read the entity schema at `schemas/vault/entity.yaml` if needed.

### 4. Content Validation
Confirm all 6 brief sections are populated (non-empty) in the vault file:
- How Introduced
- Who They Are
- How Useful
- What to Share
- What Not to Over-Share
- Talking Points

If any section is empty or placeholder-only, stop and fill it with sourced content before proceeding.

### 5. Slack Notification Validation
Only send the Slack webhook call after checks 1-4 all pass.
- Confirm the curl response includes `"ok"` (Slack returns the string `ok` on success).
- If Slack returns an error, retry once. If it fails again, report the error to the user but do not block — the brief is already saved.
</validation_phase>

<success_criteria>
## Shared (both types)
- [ ] Google Doc saved in RESEARCH/BRIEFS with G&B letterhead, Avenir font, black text only
- [ ] Vault file saved in brain/briefs/
- [ ] Referenced entities exist in brain/entities/
- [ ] Slack notification sent with person name, date, and Doc link
- [ ] Google Doc link shared with user

## New Contact
- [ ] All 6 sections populated with specific, sourced information
- [ ] Introduction chain fully traced (not generic)
- [ ] Talking points tailored to the specific person (not boilerplate)

## Repeat Contact
- [ ] All 8 sections populated (Relationship Arc, Pipeline Stage, Prior Call Notes, Financials Status, Open Questions, What to Push For, Seller Personality, Red Flags)
- [ ] Every prior call/meeting included in Relationship Arc chronologically
- [ ] Open Questions pulled from actual prior conversations (not generic)
- [ ] What to Push For aligned with current pipeline stage and next milestone
- [ ] Filename includes call number: `{date}-{company-slug}-call-{n}.md`
</success_criteria>

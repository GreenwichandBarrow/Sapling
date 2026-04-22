# Owner Call Brief — Template

**Purpose:** Call prep for meetings with business owners in Attio Active Deals pipeline at "First Conversation" stage or later. Deal-progression focus. Goal: advance the deal to the next stage.

**Golden reference:** always load the most recent file in `../examples/owner-call/` as the format anchor before drafting. If the folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{company-slug}-call-{n}.md` (where n = call number)
**Drive save:** RESEARCH/BRIEFS folder `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`
**Filename:** `{Company} Call Prep #{n} {M.DD.YY}`

---

## Structure

```
CALL PREP: {Owner Name} — Call #{n}
{Meeting Type} | {Day} {Date}, {Time}
{Location or video link}

—

RELATIONSHIP ARC

{Chronological timeline of touchpoints:}
• {Date} — {How introduced, by whom}
• {Date} — {First email / outreach}
• {Date} — {Call #1: key topics, outcome}
• {Date} — {Follow-up email / NDA sent}
• {Date} — {Call #2: key topics, outcome}
{Continue through present...}

—

CURRENT PIPELINE STAGE

Stage: {current Attio stage}
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

## Voice + Content Rules

- Deal-progression focused, not relationship-general
- Every question in "What to push for" tied to an Attio stage transition
- No em dashes
- Seller personality notes are observational, never judgmental
- Red flags surfaced with specifics, not vague concern

## Data Sources

- Attio Active Deals entry + all custom attributes
- `brain/calls/` all files mentioning this person or company (grep `person/{slug}` and wiki-links)
- Granola transcripts via `mcp__granola__list_meetings` filtered by name
- Gmail thread history (full, not just recent)
- Deal folder in `ACTIVE DEALS / {Company} /` — CIM, FINANCIALS, scorecard if exist

## Validation Gates

- [ ] All 8 sections populated
- [ ] Every prior call included in Relationship Arc chronologically
- [ ] Open Questions pulled from actual prior conversations (not generic)
- [ ] What to Push For aligned with current Attio stage + next milestone
- [ ] Filename includes call number
- [ ] No em dashes

# New Contact Meeting Brief — Template

**Purpose:** First meeting with a new contact. Usually a warm intro from an existing connection, occasionally a cold reconnection. Focus: understand the person, trace the intro chain, map them to G&B's search, decide what to share vs keep private.

**Golden reference:** always load the most recent file in `../examples/new-contact/` as the format anchor before drafting. If the folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}.md`
**Drive save:** RESEARCH/BRIEFS folder `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`
**Filename:** `{Person Name} Brief {M.DD.YY}`

---

## Structure

```
MEETING BRIEF: {Person Name}
{Meeting Type} | {Day} {Date}, {Time}
{Location or video link}

—

HOW YOU WERE INTRODUCED

{Full connection chain: who introduced whom, when, what context was provided,
what the introducer said about Kay, what they said about the other person.
Note if this is the first conversation or if there's been prior contact.}

—

WHO {FIRST NAME} IS

• {Role and company — one line}
• {What the company does — one line}
• {Background / previous roles — one line}
• {Education / credentials if relevant — one line}
• {Network / relationships of note — one line}

—

HOW THEY COULD BE USEFUL TO YOUR SEARCH

1. {Specific connection to G&B thesis or active niches}
2. {Network / intro potential}
3. {Industry insight they could provide}
4. {Any other strategic value}

—

WHAT TO SHARE ABOUT YOURSELF

• {What they already know — build on this}
• {G&B positioning tailored to their world}
• {Relevant thesis angles — only what resonates with their expertise}
• {Mutual value framing — what you can offer them}

—

WHAT NOT TO OVER-SHARE

• {Topics to keep high-level}
• {Things to avoid entirely}

—

SUGGESTED TALKING POINTS

1. {About their business / work}
2. {Specific question connecting their expertise to your search}
3. {Your search — brief, conversational framing}
4. {Mutual value — relationship-first}
```

## Voice + Content Rules

- Introduction chain MUST be fully traced, not generic
- Talking points MUST be tailored to the specific person, not boilerplate
- No em dashes
- HoldCo / Bridge-Engine-Community-Jewel language stays INTERNAL — never in new-contact briefs (traditional-searcher peer-group disclosure rule)
- If the person is a traditional searcher, apply the 4/21 disclosure calibration: no continuation-vehicle language

## Data Sources

- Calendar: `gog calendar list --from {date} --to {date} --json`
- Gmail intro thread: `gog gmail search "{introducer} {new person}" --max 15`
- Vault: `brain/entities/{person-slug}.md` if exists; `brain/calls/` and `brain/library/internal/salesflare/` for any prior context
- Web search: `{Person Name} {Company} {Role}` for background

## Validation Gates

- [ ] All 6 sections populated with specific sourced information
- [ ] Introduction chain fully traced (not "[introducer] introduced us")
- [ ] Talking points tailored to the person (not generic search-fund boilerplate)
- [ ] No em dashes
- [ ] Entity file exists in `brain/entities/{person-slug}.md` (create if missing)
- [ ] Google Doc saved in RESEARCH/BRIEFS with G&B letterhead (Avenir, black, centered logo)
- [ ] Slack notification to Kay with Doc link

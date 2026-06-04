# Follow-Up Call Brief — Template

**Purpose:** General-purpose call prep for repeat meetings outside the Active Deals pipeline. Covers coaching follow-ups (Harrison), recurring advisors, vendors with active engagement, and any other call where there's prior relationship history but no deal-progression frame. The default template for any "Call #n with a known person who isn't an Active Deals owner."

**Golden reference:** always load the most recent file in `../examples/follow-up/` as the format anchor before drafting. If the folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}-call-{n}.md`
**Drive save:** RESEARCH/BRIEFS folder `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`
**Filename:** `Call Prep — {Person Name} — {Context} #{n} — {M.DD.YY}` (Context = e.g., "Coaching", "Follow-Up", "Advisor Sync")

---

## Structure (4 sections + Relationship Arc appendix)

```
FOLLOW-UP CALL: {Person Name} — Call #{n}
{Meeting Type} | {Day} {Date}, {Time}
{Location or video link}

—

PURPOSE OF MEETING

{1-3 lines: why this meeting is happening, what we want from it, the
state of the relationship.}

—

AGENDA ITEMS

{Top items for this call, in priority order:}

1. {Topic — specific question or decision needed}
2. {Topic — specific question or decision needed}
3. {Topic — specific question or decision needed}

—

OPTIONAL ITEMS

{Lower priority — only if time permits:}

• {Topic}
• {Topic}

—

ACTION STEPS

{What gets committed coming out of this call:}

• {Kay commits to: ...}
• {Counterparty commits to: ...}
• {Decision needed in next N days: ...}

—

RELATIONSHIP ARC (appendix)

{Chronological timeline of touchpoints, oldest first:}

• {Date} — {How introduced / engagement started}
• {Date} — {Call #1: key topics, outcome}
• {Date} — {Call #2: key topics, outcome}
{Continue through present...}
```

## Voice + Content Rules

- 4 working sections, period. Relationship Arc is an appendix, not a working section.
- Agenda items must be specific (a decision, a question, a deliverable), not topics.
- Action steps name the committer (Kay vs counterparty) and a timeframe.
- No em dashes.
- Per `feedback_strategic_thresholds_need_grounding`: every agenda item must trace to a real G&B-firing case, not generic playbook scaffolding.

## Data Sources

- `brain/entities/{person-slug}.md` — relationship background
- `brain/calls/` — all prior call notes with this person (grep `person/{slug}`)
- `brain/inbox/` — any open inbox items naming this person
- Gmail thread history (recent + intro)
- `brain/context/session-decisions-*.md` — recent decisions/deferrals naming this person
- Granola transcripts via `mcp__granola__list_meetings` filtered by name

## Validation Gates

- [ ] 4 working sections populated (Purpose, Agenda, Optional, Action Steps)
- [ ] Relationship Arc at bottom with all prior touchpoints chronologically
- [ ] Each agenda item is specific (decision/question/deliverable, not topic)
- [ ] Action steps name committer + timeframe
- [ ] Filename includes call number
- [ ] No em dashes

# Intermediary Meeting Brief — Template

**Purpose:** Call prep for meetings with brokers, M&A advisors, investment bankers, law firm partners, wealth advisors, or other referral-source intermediaries. Focus: strengthen relationship, qualify their deal flow, map their network, get them sending G&B-fit deals.

**Golden reference:** always load the most recent file in `../examples/intermediary/` as the format anchor. If folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}-intermediary.md`
**Drive save:** RESEARCH/BRIEFS folder `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`
**Filename:** `{Person Name} Intermediary Prep {M.DD.YY}`

---

## Structure (4 sections + Relationship Arc appendix)

```
INTERMEDIARY PREP: {Person Name} — {Firm}
{Meeting Type} | {Day} {Date}, {Time}
{Location or video link}

—

PURPOSE OF MEETING

{Who they are, what their firm does, deal flow pattern, state of relationship.
Attio stage: {Identified / Contacted / Warmed / Actively Receiving / Daily Check-in}}

Buy box quick reference (for live use during the call):

• Revenue ${X}M – ${Y}M | EBITDA ${X}M – ${Y}M
• Industries: {active niches}
• Never: PE-owned, California, sub-$500K, franchises, restaurants, cap-intensive mfg, physician practices, lending, carve-outs

—

AGENDA ITEMS

1. {Specific deal-flow ask — anchored in an active niche, not generic}
2. {Intro ask — specific person or firm, not "anyone in X"}
3. {Market intel — multiples, financing posture, PE activity in their sector}

—

OPTIONAL ITEMS

• Reciprocal value: {what G&B can offer them — deal observations, market signals, credibility anchors}
• Red flags to watch: {blast-only behavior, conflicts with a competitor, overworked / unresponsive}

—

ACTION STEPS

• Update Attio Intermediary stage if warranted ({current} → {next})
• Update `last_deal_sent` + `deal_types_sent` fields
• Send thank-you within 24h (per `feedback_followup_timing`)
• Add any mentioned contacts to vault as entities

—

RELATIONSHIP ARC (appendix)

How introduced: {origin}

Touchpoints:

• {Date} — {meeting / email / event}
• {Date} — {meeting / email / event}

Prior deals shared: {none / list with dates}
```

## Voice + Content Rules

- 4 working sections, period. Relationship Arc is appendix, not a working section.
- Intermediaries are gatekeepers — keep the brief short, focused on deal flow.
- Reciprocal value is critical — what G&B can offer them, not just ask for.
- Buy box reminder is for Kay's live reference during the call — keep it scannable.
- No em dashes.
- Per `feedback_broker_competition`: recognize broker deals go to 3000+ buyers; calibrate expectations.
- Per `feedback_broker_emails`: short and direct, don't over-explain G&B thesis.

## Data Sources

- Attio Intermediary Pipeline entry
- `brain/entities/{person-slug}.md` and `{firm-slug}.md`
- `brain/calls/` for prior meetings
- Gmail thread history
- Firm website + recent deal announcements (web search)

## Validation Gates

- [ ] 4 working sections populated (Purpose, Agenda, Optional, Action Steps)
- [ ] Relationship Arc at bottom with touchpoints chronologically
- [ ] Buy box reminder matches current active niches
- [ ] Specific deal-flow ask (not generic "anything in X?")
- [ ] Action Steps include Attio stage update + thank-you timing
- [ ] No em dashes

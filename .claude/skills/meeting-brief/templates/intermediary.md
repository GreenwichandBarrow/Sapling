# Intermediary Meeting Brief — Template

**Purpose:** Call prep for meetings with brokers, M&A advisors, investment bankers, law firm partners, wealth advisors, or other referral-source intermediaries. Focus: strengthen relationship, qualify their deal flow, map their network, get them sending G&B-fit deals.

**Golden reference:** always load the most recent file in `../examples/intermediary/` as the format anchor. If folder is empty, stop and ask Kay for a golden.

**Vault save:** `brain/briefs/{YYYY-MM-DD}-{person-slug}-intermediary.md`
**Drive save:** RESEARCH/BRIEFS folder `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ`
**Filename:** `{Person Name} Intermediary Prep {M.DD.YY}`

---

## Structure

```
INTERMEDIARY PREP: {Person Name} — {Firm}
{Meeting Type} | {Day} {Date}, {Time}
{Location or video link}

—

WHO THEY ARE

• {Role and firm}
• {What the firm does — advisory type, typical deal size, sectors}
• {Their territory — geographic, sector, deal-size sweet spot}
• {Background / how they built their book}
• {Reputation / style — proprietary vs brokered, reputation in market}

—

RELATIONSHIP HISTORY

Attio Intermediary Pipeline stage: {Identified / Contacted / Warmed / Actively Receiving Deal Flow / Daily Check-in}
How introduced: {origin}
Touchpoints:
• {Date} — {meeting / email / event}
• {Date} — {meeting / email / event}
Prior deals shared: {none / list with dates}

—

THEIR DEAL FLOW PATTERN

{What types of deals have they shared? Size, sector, geography.}
{Are they sending G&B-fit deals? What's their hit rate?}
{What's their deal-sharing cadence — weekly blast, occasional DIRECT email, only when they have something fitting?}

—

G&B BUY BOX REMINDER FOR THEM

{Tight summary of what to send — use this as the reference during the call:}
• Revenue: ${X}M – ${Y}M
• EBITDA: ${X}M – ${Y}M
• Industries: {top-priority niches + open to adjacent}
• Geography: {tri-state, with flexibility}
• Never: {PE-owned, California, sub-$500K rev, franchises, restaurants, cap-intensive manufacturing, physician practices, lending, carve-outs}

—

WHAT TO ASK FOR

1. {Specific deal-flow request — "Anything in specialty insurance or premium pest?"}
2. {Intro request — specific other intermediary or owner}
3. {Market intelligence — "What are you seeing in multiples / financing / PE activity?"}
4. {Reciprocal value — what G&B can offer them}

—

WHAT TO SHARE (RECIPROCAL VALUE)

• {Deal observations G&B has that they'd find useful}
• {G&B's credibility signals — Anacapa LP, Chanel background, etc.}
• {Recent wins or signals that show G&B is active (without revealing specifics)}

—

RED FLAGS / WATCH ITEMS

• {Anything that suggests they won't be productive — blast-only, conflicted with a competitor, overworked}
• {Compliance concerns — do they have a clean reputation?}
• {Any prior friction}

—

POST-CALL ACTIONS

- Update Attio Intermediary stage if warranted (Identified → Contacted / Contacted → Warmed / etc.)
- Update `last_deal_sent` + `deal_types_sent` fields
- Send thank-you in 24h (per `feedback_followup_timing`)
- Add any mentioned contacts to vault as entities
```

## Voice + Content Rules

- Intermediaries are gatekeepers, not relationship targets per se — keep the brief short, focused on deal flow
- Reciprocal value is critical — what can G&B offer them, not just ask
- Buy box reminder in the brief is for Kay's live reference during the call
- No em dashes
- Per `feedback_broker_competition`: recognize broker deals go to 3000+ buyers; calibrate expectations
- Per `feedback_broker_emails`: short and direct, don't over-explain G&B thesis

## Data Sources

- Attio Intermediary Pipeline entry
- `brain/entities/{person-slug}.md` and `{firm-slug}.md`
- `brain/calls/` for prior meetings
- Gmail thread history
- Firm website + recent deal announcements (web search)

## Validation Gates

- [ ] All sections populated
- [ ] Buy box reminder matches current active niches
- [ ] Specific deal-flow ask (not generic)
- [ ] Reciprocal-value section non-empty
- [ ] Post-call actions list populated
- [ ] No em dashes

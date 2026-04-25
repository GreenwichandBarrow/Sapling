---
schema_version: 1.1.0
date: 2026-04-24
type: trace
today: "[[notes/daily/2026-04-24]]"
task: Draft first-reply email to Jim Vigna (Live Oak Bank) after XPX
had_human_override: true
importance: high
target: skill:conference-engagement
tags: [date/2026-04-24, trace, person/jim-vigna, company/live-oak-bank, pattern/disqualifier-skip-pitch, domain/sales]
---

# Decision Trace: Cut Buy-Box From Banker First-Reply When Capital-Fit Is Mismatched

## Context

Kay met [[entities/jim-vigna|Jim Vigna]] (East Coast coverage, [[entities/live-oak-bank|Live Oak Bank]]) at XPX NYC 2026-04-23. Live Oak's SBA-loan business mostly serves *self-funded searchers*. Kay runs a *traditional search fund* with investor capital — so Live Oak's typical economics don't match her deal size from the bank-financing side. Jim emailed the next day offering ongoing dialogue + take on deals + coffee/lunch.

Claude drafted a standard conference-engagement first-reply: warm opening + buy-box paragraph (~$2-5M EBITDA, NY Metro, B2B services, founder-led) + meeting close. Kay rewrote the draft over 5 iterations. The most consequential edit (v3): she cut the buy-box paragraph entirely and added "which might change things on your end" as an off-ramp.

## Decisions

### Cut the buy-box from the first reply (Kay's v3)
**AI proposed:** Lead with appreciation, give buy-box paragraph, ask for deal flow + meeting.
**Chosen:** Open with appreciation, **clarify fund-type mismatch (self-funded vs traditional)**, **drop the buy-box entirely**, accept meeting only.
**Reasoning:** When the disqualifier is real (Live Oak's economics genuinely don't fit traditional-fund check sizes), pitching the buy-box on top of acknowledging the mismatch is tonally incoherent. Either the relationship has transactional upside (full pitch) or it doesn't (relational-only). Mixing the two makes the sender look like they didn't read the room. Jim is still useful for market intel, deal sighting, network intros — but not as a capital source for Kay's specific deals.
**Pattern:** #pattern/disqualifier-skip-pitch

### Restoring a light buy-box (Claude's counter-draft v4)
**AI proposed:** Restore one tight sentence of buy-box (founder-led, ~$2-5M EBITDA, NY Metro, B2B services) because Jim's email *explicitly offered* his take on deals — without criteria, his offer becomes meaningless.
**Chosen:** Kay accepted the v4 counter-draft as the base, then iterated v5 (added off-ramp on the meeting ask).
**Reasoning:** Distinction between "pitching unprompted" (overreach) and "providing criteria when the contact has asked what kinds of deals to weigh in on" (responsive). The latter answers his question; the former imposes on him. Claude's pushback was the right read once he'd seen Jim's actual offered value.
**Pattern:** #pattern/responsive-vs-imposed-pitch

## Learnings

- **First-reply default is NOT "always include buy-box."** Read whether the contact has transactional fit. If yes, include criteria. If no, hold the relationship as relational-only.
- **Banker/lender contacts specifically:** clarify fund-type (traditional vs self-funded vs independent sponsor) within the first 2 sentences when relevant. SBA-vs-investor capital structure is a load-bearing distinction that routes them to the right internal team — without it they assume the wrong category.
- **Don't cut what the contact has explicitly asked for.** If a contact's email offers "take on deals," omitting your criteria is non-responsive, not polite restraint.
- **Future agent instruction:** for any banker/lender or capital-provider first-reply, explicitly evaluate "does Live Oak / this lender / this provider's typical economics match the seller's needs?" before drafting. If mismatched, produce a relational-only draft (no buy-box). If matched or partially matched, include criteria. Never default to "always pitch."

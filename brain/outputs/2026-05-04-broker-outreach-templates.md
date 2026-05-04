---
schema_version: 1.2.0
date: 2026-05-04
type: research
status: draft
skill_origin: outreach-manager
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/research", "status/draft", "topic/intermediary-outreach", "topic/broker-channel", "person/kay-schneider"]
---

# G&B Broker Outreach Templates — 3-Touch Cadence (Day 0 / Day 5 / Day 12)

Drafted 2026-05-04 for the new G&B Broker Outreach Templates Drive doc that the founder creates Monday afternoon. Calibrated against the V1 BROKERS variation in `G&B Intermediary Outreach Templates` (Doc ID `1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4`) and the controlling memories listed at the bottom.

These templates feed `outreach-manager` Subagent 3 (Intermediary). The orchestrator fills the placeholders and renders drafts in Gmail compose for review before send. No automated sends.

**Important departure from the existing Templates doc:** the canonical V1 BROKERS variation is ONE-AND-DONE per `feedback_no_search_fund_language_intermediaries`. This new 3-touch broker-channel cadence is an explicit override greenlit in the 5/3 broker-channel build discussion (locked plan `vivid-booping-starfish`). If G&B reverts to one-and-done after testing, archive Day 5 and Day 12.

---

## Placeholder Reference

| Placeholder | Filled by | Example |
|---|---|---|
| `{{first_name}}` | outreach-manager (formal first name per `feedback_first_reply_formal_name`) | `James` not `Jimmy` |
| `{{firm_name}}` | outreach-manager from target list | `Transworld Business Advisors of NYC` |
| `{{day_of_week_close}}` | orchestrator at send time per `feedback_day_aware_signoffs` | `Have a great week ahead.` / `Have a great weekend.` / blank for Tue-Thu |
| `{{day_0_date}}` | outreach-manager (Day 5/12 only) | `Monday the 12th` |
| `{{specific_deal_type_or_geography}}` | outreach-manager personalization hook (Day 0 only) | `closings in the NY/NJ corridor recently` or `lower-middle-market services deals` |
| `{{signer_first_name}}` | renders to "K." plus full name in body | first-name "K." token used in salutations + body, full name on intro line |
| `{{signer_full_name}}` | full sender name | renders the founder's full first + last name on intro line |
| `{{signer_signature_block}}` | Gmail signature (handled by Gmail, not template) | renders automatically |

The `{{specific_deal_type_or_geography}}` slot is where geography is allowed in the body for broker-channel outreach (per task spec — geography IS the broker-channel value prop). Everywhere else, geography stays in the footer.

The `{{signer_*}}` placeholders exist so the body literal first-name reference is filled at render time, not hardcoded in the template prose. The deliverables-naming hook flags personal-name tokens in client-facing prose; templates use placeholders so they pass the hook AND remain reusable if a second G&B operator ever joins.

---

## Day 0 — Intro (Cold)

**Subject:** Brief introduction

**Body:**

Hi {{first_name}},

Hope this finds you well.

I came across {{firm_name}} while looking at who's been active on {{specific_deal_type_or_geography}}, and wanted to introduce myself.

I'm {{signer_full_name}}, founder of Greenwich & Barrow. I'm looking to acquire and run one business for the long term, and I've been getting to know the brokers covering this end of the market. G&B is backed by 12 investors including industry experts, operators, and family offices, and we respond on CIMs under NDA within 48 hours.

Anything in your pipeline worth a look on our side? Happy to sign an NDA on a teaser. Otherwise I'd value being on {{firm_name}}'s buyer list.

{{day_of_week_close}}

Very best,
{{signer_first_name}}

{{signer_signature_block}}

What We Look For

Founder-owned or family-owned, US-based
Growing, recurring revenue
$2M-$10M EBITDA, 15%+ margins
Service-driven businesses, skilled trades
NY / NJ / PA / CT preferred

---

## Day 5 — Follow-Up

**Subject:** Re: Brief introduction

**Body:**

Hi {{first_name}},

Just circling back on my note from {{day_0_date}}. No pressure if the timing isn't right.

Happy to share G&B's broker-channel buy-box if it would help filter your pipeline. We sign NDAs same-day and respond on CIMs within 48 hours.

If this isn't a fit, just let me know and I'll take you off my list.

{{day_of_week_close}}

Very best,
{{signer_first_name}}

{{signer_signature_block}}

---

## Day 12 — Soft-Close

**Subject:** Re: Brief introduction

**Body:**

Hi {{first_name}},

Closing the loop on my earlier notes from {{day_0_date}} and last week.

If timing isn't right, no worries. I'll keep you on G&B's quarterly newsletter and reach back out if anything changes. If a fit comes up on your side, you know where to find us.

{{day_of_week_close}}

Very best,
{{signer_first_name}}

{{signer_signature_block}}

---

## Voice Compliance Checklist (applied during drafting)

- [x] No em dashes anywhere — used periods, commas, line breaks
- [x] No `>` blockquote, no code fence in any draft body — plain text per `feedback_drafts_no_blockquote`
- [x] No "fund" / "search fund" / "holding company" / "vehicle" / "ETA" / "committed equity" / "24-month window" — described in plain verbs ("looking to acquire and run one business for the long term") per `feedback_never_say_fund` + `feedback_no_search_fund_language_intermediaries`
- [x] No revenue/employee/financials in body — buy-box specs in footer only per `feedback_no_revenue_in_outreach`
- [x] No geography in body except Day 0 personalization slot — footer carries the NY/NJ/PA/CT preference per task spec + `feedback_broker_channel_opportunistic_floor`
- [x] No thesis/growth-strategy leaks (no "underpenetration," "consolidation," "roll-up") per `feedback_outreach_no_strategy_leaks`
- [x] No fake-warm framings ("your name keeps coming up") per `feedback_outreach_no_fake_lines`
- [x] Warm nicety opener on Day 0 ("Hope this finds you well") per `feedback_email_niceties`. Day 5 / Day 12 skip the opener since they're follow-ups in the same thread — opener would read forced.
- [x] 12-investor capital-credibility line in BODY (single-name-drop pattern, no full LP enumeration)
- [x] NDA offer + pipeline ask on Day 0 per `feedback_broker_emails`
- [x] Day-aware sign-off as `{{day_of_week_close}}` placeholder (not hardcoded)
- [x] Formal first-name placeholder on recipient salutation per `feedback_first_reply_formal_name`
- [x] Founder name in body uses `{{signer_*}}` placeholders so the deliverables-naming hook passes and the template is reusable
- [x] Opt-out line on Day 5
- [x] Polite close + quarterly newsletter offer on Day 12

## Voice-Rule Near-Misses Caught and Corrected

1. **First Day 0 draft used "search vehicle" structural label.** Corrected to "looking to acquire and run one business for the long term" per `feedback_no_search_fund_language_intermediaries` updated 4/30 rule (drop ALL structural labels).
2. **First Day 0 draft put "$2-10M EBITDA NY/NJ/PA/CT" in body bullets.** Moved to footer per task spec — body now opens with curiosity hook + plain-verb intro, footer carries spec.
3. **First Day 5 draft repeated the warm nicety ("Hope this finds you well") and the full G&B intro.** Stripped — Day 5 is a follow-up in the same thread, repeating the nicety reads form-letter and repeating the intro reads dense. Now Day 5 references the prior note and gets to the new value-add (broker-channel buy-box) in two sentences.
4. **First Day 12 draft hardcoded the day-of-week close.** Replaced with `{{day_of_week_close}}` placeholder so the orchestrator fills based on actual send day.
5. **First Day 0 subject was "Greenwich & Barrow — buyer for {{firm_name}}'s pipeline".** Reads transactional and pitchy. Replaced with "Brief introduction" matching V1 BROKERS canonical subject so the cadence threads cleanly (Re: Re: on follow-ups).
6. **First Day 0 footer included revenue band.** Stripped revenue from footer (kept EBITDA + margin only) — revenue in the footer technically OK per `feedback_no_search_fund_language_intermediaries` Buyer Profile pattern, but task spec was explicit about no revenue in body, and the broker-channel buy-box isn't revenue-anchored anyway.
7. **First Day 5 draft said "any deals come through this week".** Reads pushy on a 5-day-old thread. Softened to "If it would help, happy to share G&B's broker-channel buy-box."
8. **First version of this file used founder's first name in narrative prose AND in email-body literals.** PostToolUse `no-kay-in-deliverables` hook blocked. Refactored: narrative prose uses "the founder" / "G&B"; email-body literals use `{{signer_first_name}}` and `{{signer_full_name}}` placeholders that the orchestrator fills at draft-render time.

---

## Founder needs to confirm

1. **Day 0 personalization slot — what fills `{{specific_deal_type_or_geography}}`?** Two example fills drafted ("closings in the NY/NJ corridor recently" / "lower-middle-market services deals"). Outreach-manager will need a rule for which to pick per broker. Recommend: if the broker's website lists recent closings publicly, use a closing-type reference. If not, default to geography ("activity in the NY/NJ corridor"). Need a lock on the default phrasing.

2. **Geography window for the footer.** Footer currently reads "NY / NJ / PA / CT preferred." Per `feedback_broker_channel_opportunistic_floor`, geography window is NOT YET locked — that memory says "baseline NY/NJ/CT/PA from existing Axial filter." 5/3 left MA/FL as open questions. Default went with the baseline. If MA or FL should be added before Monday's draft batch, change footer.

3. **Day 5 / Day 12 cadence override.** The canonical V1 BROKERS variation in the existing Templates doc is ONE-AND-DONE per the 4/30 directive. This 3-touch broker-channel cadence overrides that. Confirm 3-touch still wanted (locked plan `vivid-booping-starfish`) — if reverted to one-and-done since 5/3, archive Day 5 and Day 12 templates immediately.

4. **Sam Curcio @ Transworld NYC sanity-check recipient.** RECOMMEND: yes, send Day 0 to Sam Curcio as the first sanity-check before bulk Day 0 sends. Reasons: (a) he's already in G&B's network from the 5/1 cleanup so the email isn't fully cold, lower bounce/reputation risk; (b) Transworld franchise pattern means the Day 0 hook ("activity in the NY/NJ corridor") fits cleanly; (c) if he engages, his reply tells G&B whether the buy-box footer reads right to a working broker; (d) if the cadence runs through Day 5 and Day 12 with Sam responding at Day 5 or Day 12, full-loop signal arrives before bulk send. Caveat: send only Day 0 first, wait 48-72 hours, then judge. If reply lands before Day 5, treat his thread as the calibration source and pause bulk.

---

## Related Memories

- `feedback_no_name_in_deliverables` (use G&B / Greenwich & Barrow in narrative prose; founder name only inside `{{signer_*}}` template slots)
- `feedback_no_search_fund_language_intermediaries` (4/30, drop structural labels)
- `feedback_broker_emails` (concise, NDA offer)
- `feedback_broker_channel_opportunistic_floor` (5/3 separate broker buy-box, geography pending)
- `feedback_email_no_em_dashes`
- `feedback_drafts_no_blockquote` (HARD RULE)
- `feedback_email_niceties`
- `feedback_outreach_about_them`
- `feedback_outreach_no_strategy_leaks`
- `feedback_never_say_fund`
- `feedback_no_revenue_in_outreach`
- `feedback_first_reply_formal_name`
- `feedback_day_aware_signoffs`
- `feedback_kay_handles_all_replies`
- `feedback_no_sunday_emails`

---

## Outcome

- **Published:** null
- **Engagement:** null
- **Hypothesis result:** pending

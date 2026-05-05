---
schema_version: 1.2.0
date: 2026-05-04
type: research
status: published
skill_origin: outreach-manager
kay_approved: true
kay_approval_date: 2026-05-04
people: []
companies: []
projects: []
tags: ["date/2026-05-04", "output", "output/research", "status/published", "topic/intermediary-outreach", "topic/broker-channel", "topic/template-locked"]
---

# G&B Broker-Channel Outreach Templates. Locked 2026-05-04 (FINAL — superseded 2026-05-04 evening)

> **2026-05-04 evening update:** Drive doc evolved beyond this snapshot. Current canonical state has 9 templates (this snapshot reflects the 4 LOCKED at template-lock midday). Cadence reduced from 3-touch to 2-touch (Day 12 dropped). See `feedback_no_intermediary_drafts_outside_template` and `session-decisions-2026-05-04.md`. Per CLAUDE.md source-of-truth rules: Drive doc `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` is canonical; this file is a creation-time snapshot only. **Current Drive state (as of 2026-05-04 evening):** Day 0 INTRODUCTION (Brokers+IBs), LEAD-YES, LEAD-NO, INTRODUCTION (Lawyers+CPAs), CIM RECEIVED, THANK YOU, DAY 5 FOLLOW-UP, DECLINE POST-REVIEW, NDA SIGNED. Cadence: Brokers+IBs = 2-touch (Day 0 + Day 5), Lawyers+CPAs = ONE-AND-DONE.

LOCKED versions reflecting all rounds of G&B operator iteration. Two audience templates plus follow-up cadence for the deal-flow audience.

Audience map (as updated 2026-05-04 evening):
- Deal-flow source layer (Brokers + IBs): 2-touch cadence (Day 0 + Day 5). Day 12 soft-close DROPPED.
- Referral-relationship layer (Lawyers + CPAs): single education-tone intro, no follow-up cadence.

Drive doc home: G&B Broker Email Templates `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4`. Original canonical Templates doc `1_cNsAPCopDAfReoDXbB4d3hZW8TcYUqJ3XKYY_er7i4` superseded for V1 / V2 / V5 / V6.

---

## Placeholder Reference

| Placeholder | Filled by | Example |
|---|---|---|
| `{{first_name}}` | outreach-manager (formal first name per `feedback_first_reply_formal_name`) | `James` not `Jimmy` |
| `{{firm_name}}` | outreach-manager from target list | `Transworld Business Advisors of NYC` |
| `{{niche}}` | outreach-manager from target context (Lawyers + CPAs only) | `pest management` |
| `{{day_0_date}}` | outreach-manager (Day 5 / 12 only) | `Monday the 12th` |
| `{{signer_first_name}}` | filled at Gmail-render time | First name only on sign-off |
| `{{signer_full_name}}` | filled at Gmail-render time | Full name on intro line |

LinkedIn URL is handled by the Gmail signature, not in template body.

---

## Template A. Brokers + IBs (Day 0 intro)

Subject: Introduction

Hi {{first_name}},

Hope this finds you well.

I came across {{firm_name}} while getting to know the brokers covering the lower-middle-market in our space, and wanted to introduce myself. As founder of Greenwich & Barrow, with nearly two decades of experience in business strategy and development I am searching full time to acquire and step into the CEO seat post close. I'm a well capitalized buyer backed by investors with operating experience, assisted by lawyers and accountants for due diligence, so that we can partner efficiently on the close process. We are able to move quickly and I would love to connect. I'm happy to send over some windows/options to hop on a quick call. Let me know what works best for you.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}


What We Look For:

Independent ownership, US-based
$5M-$50M Revenue, $2M+ EBITDA, 15%+ Margins
Industries: Transportation, Business Services, Industrial services (Capital light), Technology, Healthcare services

---

## Template B. Lawyers + CPAs (single education-tone intro, no cadence)

Subject: Introduction

Dear {{first_name}},

Hope this finds you well.

I came across {{firm_name}} while looking in the {{niche}} industry. I'm {{signer_full_name}}, founder of Greenwich & Barrow. With nearly two decades of experience in business strategy and development I am searching full time to acquire and step into the CEO seat post close. If any of your business owner clients are thinking about succession planning or considering a sale, I'm a well capitalized buyer backed by investors with operating experience. I'd welcome being a name you'd consider and to that end would love to connect. I'm happy to send over some windows/options to hop on a quick call. Let me know what works best for you.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}


What We Look For:

Independent ownership, US-based
$5M-$50M Revenue, $2M+ EBITDA, 15%+ Margins
Industries: Transportation, Business Services, Industrial services (Capital light), Technology, Healthcare services

Note for Lawyers + CPAs: dropped the "assisted by lawyers and accountants for due diligence" line that appears in Template A. Felt redundant when the recipient IS a lawyer or accountant. Body still communicates capital backing + operator-CEO commitment + meeting ask.

---

## Reply snippet — LEAD-YES (Brokers + IBs + Lawyers + CPAs, used inbound)

When a broker / IB / lawyer / CPA sends a deal that looks worth pursuing.

Subject: Re: {{their_subject}}

Hi {{first_name}},

Thanks for sending. Looks really interesting and I'd be happy to sign the NDA today if you can send it over.

Thanks so much and look forward to hearing from you.

Very best,
{{signer_first_name}}

---

## Reply snippet — LEAD-NO (Brokers + IBs + Lawyers + CPAs, used inbound)

When a deal isn't a fit. Footer attached as passive reminder rather than inline criteria in body.

Subject: Re: {{their_subject}}

Hi {{first_name}},

Thanks for thinking of me. Unfortunately this one isn't a fit on our side ({{reason}}).

Thanks again and look forward to keeping in touch.

Very best,
{{signer_first_name}}


What We Look For:

Independent ownership, US-based
$5M-$50M Revenue, $2M+ EBITDA, 15%+ Margins
Industries: Transportation, Business Services, Industrial services (Capital light), Technology, Healthcare services

---

## Template A. Day 5 follow-up (Brokers + IBs only)

Subject: Re: Introduction

Hi {{first_name}},

Just circling back on my note from {{day_0_date}}. No pressure if the timing isn't right.

Happy to share G&B's broker-channel buy-box if it would help filter your pipeline. We can move quickly on a fit.

If this isn't a fit, just let me know and I'll take you off my list.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}

---

## Template A. Day 12 soft-close (Brokers + IBs only)

Subject: Re: Introduction

Hi {{first_name}},

Closing the loop on my earlier notes from {{day_0_date}} and last week.

If timing isn't right, no worries. I'll keep you on G&B's quarterly newsletter and reach back out if anything changes. If a fit comes up on your side, you know where to find us.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}

---

## Voice Compliance Checklist

- No em dashes anywhere
- No `>` blockquote, no code fence in any draft body
- No "fund" / "search fund" / "holding company" / "vehicle" / "ETA" / "committed equity" / "24-month window"
- No revenue / employee / financials in body. Buy-box specs in footer only.
- No specific LP count in body or footer ("12 investors" REMOVED 2026-05-04 per locked broker channel build calibration; generalized to "investors with operating experience"). Aligns with `feedback_analyst_folder_content_rules`.
- No salary / IRR / hurdle math anywhere in body or footer.
- No thesis / growth-strategy leaks
- No fake-warm framings
- Warm nicety opener on Day 0 ("Hope this finds you well")
- Education tone for Lawyers + CPAs ("If any of your clients are thinking about..." soft framing, no pitch)
- Operator-CEO commitment explicit ("step into the CEO seat post close")
- Career anchor ("nearly two decades of experience in business strategy and development")
- Certainty-of-close framing for Brokers + IBs ("assisted by lawyers and accountants for due diligence, so that we can partner efficiently on the close process")
- Polite call-ask ("happy to send over some windows or options to hop on a quick call")
- Day-aware close OMITTED ("Looking forward to hearing from you" replaces it)
- Founder name handled via placeholder: `{{signer_full_name}}` on intro line; `{{signer_first_name}}` on sign-off. outreach-manager fills at Gmail-render time.
- LinkedIn URL handled by Gmail signature (not in template body)
- Footer industry signals: 5 high-level Axial-aligned categories with light caveats on Industrial services (Capital light) and Healthcare services
- Geography NOT explicitly listed in footer. Implied by industry coverage and the broker outreach context. (Earlier draft included NY / NJ / PA / CT explicitly; G&B operator removed in final pass.)

---

## Cadence Rules

- Brokers + IBs: 3-touch (Day 0 + Day 5 + Day 12). Same Gmail thread (Re: Introduction). If recipient replies before Day 5 or Day 12, cadence stops and the reply thread takes over.
- Lawyers + CPAs: ONE-AND-DONE. Single intro, no follow-up. If they reply, the thread takes over. If silence, leave them on the list and re-approach at a future inflection (new conference, mutual contact, niche-relevant news).

---

## Related Memories

- `feedback_no_name_in_deliverables` (founder first name in narrative prose blocked; in-body sign-off via placeholder)
- `feedback_no_search_fund_language_intermediaries` (drop structural labels)
- `feedback_broker_emails` (concise, NDA offer)
- `feedback_broker_channel_opportunistic_floor` (separate broker buy-box, $2M plus floor, 15 percent plus margin)
- `feedback_email_no_em_dashes`
- `feedback_drafts_no_blockquote`
- `feedback_email_niceties`
- `feedback_outreach_about_them`
- `feedback_outreach_no_strategy_leaks`
- `feedback_never_say_fund`
- `feedback_no_revenue_in_outreach`
- `feedback_first_reply_formal_name`
- `feedback_kay_handles_all_replies`
- `feedback_no_sunday_emails`
- `feedback_analyst_folder_content_rules` (LP count, salary, IRR, peer LOI, operator strategy NOT in broker-facing copy)
- `feedback_kay_ceo_deal_1_not_allocator` (G&B operator is CEO of Deal 1; do not bake socrates aspirational frames into operational docs)
- `feedback_template_iterate_mode_live_edit`

---

## Outcome

- **Published:** 2026-05-04 (vault locked)
- **Drive doc:** `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` (G&B Broker Email Templates) — Brokers + IBs intro and Lawyers + CPAs intro live in Drive. G&B operator pending sync of (a) the orphan-sentence + revenue-cutoff typos called out 2026-05-04 PM and (b) the visual signature block decision (A / B / BOTH).
- **Used by:** outreach-manager Subagent 3 (Intermediary), broker-channel daily-draft mode

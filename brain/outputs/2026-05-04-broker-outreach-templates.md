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

# G&B Broker-Channel Outreach Templates. Locked 2026-05-04

LOCKED versions of intro outreach templates for the broker-channel build. Two audience templates plus 3-touch follow-up cadence for the deal-flow audience only.

Audience map:
- Deal-flow source layer (Brokers + IBs) gets the 3-touch cadence (Day 0 / Day 5 / Day 12)
- Referral-relationship layer (Lawyers + CPAs) gets a single education-tone intro and stops; no follow-up cadence by default

---

## Placeholder Reference

| Placeholder | Filled by | Example |
|---|---|---|
| `{{first_name}}` | outreach-manager (formal first name per `feedback_first_reply_formal_name`) | `James` not `Jimmy` |
| `{{firm_name}}` | outreach-manager from target list | `Transworld Business Advisors of NYC` |
| `{{niche}}` | outreach-manager from target context | `pest management` |
| `{{day_0_date}}` | outreach-manager (Day 5 / 12 only) | `Monday the 12th` |

---

## Template A. Brokers + IBs (Day 0 intro)

Subject: Brief introduction

Hi {{first_name}},

Hope this finds you well.

I came across {{firm_name}} while getting to know the brokers covering the lower-middle-market in our space, and wanted to introduce myself. As founder of Greenwich & Barrow, I have a background in business strategy and development and am searching full time to acquire and run one business for the long term. I'm a well capitalized buyer backed by investors with operating experience. We are able to move quickly and I would love to connect. I'm happy to send over some windows or options to hop on a quick call. Let me know what works best for you.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}

What We Look For

Independent ownership, US-based
$2M plus EBITDA, $5M to $50M revenue, 15 percent plus margins
NY / NJ / PA / CT
Industry-agnostic

Greenwich & Barrow Snapshot

Founded by {{signer_full_name}}
Backed by investors with operating experience
New York-based

---

## Template B. Lawyers + CPAs (single education-tone intro, no cadence)

Subject: Introduction

Dear {{first_name}},

Hope this finds you well.

I came across {{firm_name}} while looking in the {{niche}} industry. I'm {{signer_full_name}}, founder of Greenwich & Barrow. I have a background in business strategy and development and am searching full time to acquire and run one business for the long term. If any of your clients are thinking about succession planning or considering a sale, I'm a well capitalized buyer backed by investors with operating experience. I'd welcome being a name you'd consider and to that end would love to connect. I'm happy to send over some windows or options to hop on a quick call. Let me know what works best for you.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}

What We Look For

Independent ownership, US-based
$2M plus EBITDA, $5M to $50M revenue, 15 percent plus margins
NY / NJ / PA / CT
Industry-agnostic

Greenwich & Barrow Snapshot

Founded by {{signer_full_name}}
Backed by investors with operating experience
New York-based

---

## Template A. Day 5 follow-up (Brokers + IBs only)

Subject: Re: Brief introduction

Hi {{first_name}},

Just circling back on my note from {{day_0_date}}. No pressure if the timing isn't right.

Happy to share G&B's broker-channel buy-box if it would help filter your pipeline. We can move quickly on a fit.

If this isn't a fit, just let me know and I'll take you off my list.

Looking forward to hearing from you.

Very best,
{{signer_first_name}}

---

## Template A. Day 12 soft-close (Brokers + IBs only)

Subject: Re: Brief introduction

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
- No thesis / growth-strategy leaks
- No fake-warm framings
- Warm nicety opener on Day 0 ("Hope this finds you well")
- Education tone for Lawyers + CPAs ("If any of your clients are thinking about..." soft framing, no pitch)
- Polite call-ask ("happy to send over some windows or options to hop on a quick call")
- Day-aware close OMITTED ("Looking forward to hearing from you" replaces it)
- Founder name handled via placeholder: `{{signer_full_name}}` on intro line and snapshot footer; `{{signer_first_name}}` on sign-off. outreach-manager fills at draft-render time. Keeps the deliverables-naming hook clear.
- Buy-box footer uses LOCKED broker buy-box criteria (industry-agnostic, $2M plus, NY / NJ / PA / CT)

---

## Cadence Rules

- Brokers + IBs: 3-touch (Day 0 + Day 5 + Day 12). Same thread (Re: Brief introduction). If recipient replies before Day 5 or Day 12, cadence stops and the reply thread takes over.
- Lawyers + CPAs: ONE-AND-DONE. Single intro, no follow-up. If they reply, the thread takes over. If silence, leave them on the list and re-approach at a future inflection (new conference, mutual contact, niche-relevant news).

---

## Related Memories

- `feedback_no_name_in_deliverables` (founder first name in narrative prose blocked; in-body sign-off OK)
- `feedback_no_search_fund_language_intermediaries` (drop structural labels)
- `feedback_broker_emails` (concise, NDA offer)
- `feedback_broker_channel_opportunistic_floor` (separate broker buy-box, NY / NJ / PA / CT, industry-agnostic, $2M plus)
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
- `feedback_analyst_folder_content_rules` (LP count not in broker-facing copy)

---

## Outcome

- **Published:** 2026-05-04 (vault locked)
- **Drive doc:** TBD (Drive update to G&B Intermediary Outreach Templates V1 + V5 + V6 deferred until G&B operator confirms Drive lock)
- **Used by:** outreach-manager Subagent 3 (Intermediary), broker-channel daily-draft mode

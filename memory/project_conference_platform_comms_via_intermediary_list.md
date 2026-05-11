---
name: Conference-platform comms tracked on Intermediary Target List sheet
description: 2026-05-11 pattern lock-in. Conference app/portal messages (ACG portal, Brella, Whova, etc.) bypass Gmail + Granola and are invisible to email-intelligence and post-call-analyzer. Capture is manual via rows on the Intermediary Target List Google Sheet (tab chosen by firm self-ID, not analyst inference).
type: project
---

Conference platforms (ACG portal, Brella, Whova, vendor-specific apps) host pre-event 1:1 scheduling and in-app messaging that never lands in Gmail. Email-intelligence, relationship-manager, and post-call-analyzer cannot see them. Without a manual capture step, every conference-platform send + reply is invisible to the system.

**Pattern (locked in 2026-05-11 across 3 contacts in one session — Victoria Schenkel/Rabobank, Hallie Berk/Candlewood, Krupa Shah/STREAM):** Capture conference-platform comms as rows on the Intermediary Target List sheet (`18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`). No vault entity. No separate skill. Promote to Attio only after reply per `feedback_brokers_stay_in_sheet_until_reply`.

**Tab routing — classify by FIRM self-ID, NOT analyst inference** (per `feedback_classify_intermediary_by_self_id`):
- Conference profile says "Investment Bank" → Investment Bankers tab
- Conference profile says "Advisory Firm" → Corporate Advisors tab
- Conference profile says "Commercial Bank / Lender" → Lenders tab
- Conference profile says "Broker / Business Brokerage" → Brokers tab
- Conference profile says "Family Office" → Family Offices tab
- Conference profile says "Law Firm" / "CPA" → Industry Lawyers / CPAs tab
- When in doubt, ask Kay before placement.

**Required fields per row:**
- Source: `{Conference name + date} ({channel: cold via {platform} | meeting confirmed via {platform}})`
- Firm, Website, HQ, Focus/Specialty (pull from conference profile)
- Lead Contact + Title (combined or separate per the tab's schema)
- Email + phone (from conference profile)
- 1st Outreach Date: ISO YYYY-MM-DD of send
- Notes: send/meeting status + platform + exact slot/time if confirmed + reply status

**Reply handling:**
- Kay verbally surfaces incoming replies ("Krupa accepted Thu 10am", "Victoria replied no", etc.) — there's no auto-detection from in-app channels.
- On reply: update the row's Notes column AND create the Attio People + Companies records per the post-reply flow.
- If meeting is confirmed pre-event (Krupa case), still create Attio entry now — meeting acceptance counts as "reply" for the Attio-promotion rule.

**When to graduate to a skill:** This pattern has fired 3 times in one session. If it fires 2-3 more times across upcoming conferences (XPX, ACG follow-on, NPMA workshops, etc.), promote to a `conference-comms-log` skill so Kay can say "log [conference] send to [name] via [platform]" and one command writes the row. Until then, manual is acceptable — the gating is "does it fire weekly?" not "are we tired of typing it?"

**Forbidden:** Don't create vault entities for cold conference-platform contacts before reply. The Intermediary Target List is the staging area; vault entities + Attio happen post-reply per `feedback_brokers_stay_in_sheet_until_reply`.

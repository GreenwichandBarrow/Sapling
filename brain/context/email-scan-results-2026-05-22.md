---
schema_version: 1.1.0
date: 2026-05-22
type: output
output_type: email-scan-results
status: draft
tags:
  - date/2026-05-22
  - output
  - output/email-scan-results
  - source/email-intelligence
  - topic/morning-briefing
---

# Email Scan Results — 2026-05-22 (Friday)

Headless run via systemd 7am ET. Window: `newer_than:2d` (2026-05-20 → 2026-05-22).

**Auto-trigger status:** CIM = none. NDA = none. LOI = none. Bookkeeper P&L = none (no `startvirtual.com` sender, no "Management Report" subject, no P&L attachment signal). Active Deal stages 3–9 = no matching inbound document. Bookkeeper chain skipped per detection.

## 1. Actionable Items Created

No new inbox items created this run. One inbound thread was already captured by an earlier session:

| date | inbox item | source_ref | status |
|---|---|---|---|
| 2026-05-21 | `2026-05-21-sam-lamson-emily-jim-dine-intro-offer.md` (intro offer: Emily, Jim Dine granddaughter / J Crew, art-services storage experience) | gmail msg 19e4aa3242cb8713 | already exists |

Hannah Barrett's Mid-Search Summit feedback-survey ask (cohort-broadcast email) is optional/reactive — no inbox item; pipeline-manager can decide whether to surface.

## 2. Deal Flow Classified

**DIRECT (3):**
- Sam Lamson `<Sam@libreequity.com>` 2026-05-21 — "Great meeting you at PL Summit"; warm-intro offer to Emily (Jim Dine granddaughter, J Crew fashion designer, NJ-based, art-services storage experience). Personal, no broker signal. Already in inbox.
- Hannah Barrett `<hannah.barrett@pacificlake.com>` 2026-05-20 — Mid-Search Summit feedback survey + cohort contact-sharing (24 searchers in TO line). Reactive FYI.
- Cara Lovenson `<cara@planprofessionals.com>` 2026-05-20 — Heels to Deals June 10 lunch + WhatsApp group invite. Network nurture.

**BLAST (1):**
- CorpNet Compliance Team `<info@sfmail.corpnet.com>` 2026-05-21 — "Delaware LLC Tax Due June 1 — Expedited Processing Now Required". Templated compliance-vendor solicitation, not a broker. No broker-signal keywords ("for sale", "exclusive listing", "asking price", "we represent", "new listing", "now available", "teaser") in body. Does not trigger broker-BLAST per-listing extraction.

**NEWSLETTER (12):**
- Axios AM 2026-05-22, Axios Finish Line 2026-05-21 (Mike Allen)
- NPMA Events 2026-05-21
- BizBuySell weekly 2026-05-15 (carryover; pest/HVAC roll-up signal noise)
- XPX New Jersey 2026-05-21, XPX Long Island 2026-05-21
- Walker Deibel "BuildInteractive II" 2026-05-21
- Art Market Minds 2026-05-21 + 2026-05-20 (Art Business Conference NY follow-on)
- Acquiring Minds Webinars 2026-05-20 (ETA Database launch)
- Granola product newsletter 2026-05-20

**ADMINISTRATIVE / TRANSACTIONAL (6):**
- DMARC Aggregate Report from Microsoft 2026-05-22 (admin)
- MAILER-DAEMON DMARC reports x2 2026-05-22 (admin)
- Uber Receipts 2026-05-21 (expense)
- Gusto payroll confirmation 2026-05-21 (May 27 payroll)
- Pan d'oro receipt 2026-05-21 (expense)
- 1Password invoice 2026-05-21 (subscription)

## 3. Draft Status

12 total drafts in mailbox. Recent activity:

| draft_id | created | subject | recipient | age |
|---|---|---|---|---|
| r4973240214581542157 | 2026-05-16 | "Great meeting you at Heels to Deals" | mweiner@thecorpcoach.com | 6d |
| r6313621414716482441 | 2026-05-16 | (Heels to Deals follow-up) | — | 6d |
| r442603803878436480 | 2026-05-16 | (Heels to Deals follow-up) | — | 6d |
| r2253803435468898722 | ~2026-05-13 | (older thread) | — | ~9d |
| 8 others | 2024–early 2026 | long-tenured drafts | — | retained intentionally |

**Surface to pipeline-manager:** the three 2026-05-16 Heels to Deals follow-up drafts are 6 days unsent. Kay attended Heels to Deals 5/16; nurture window closes ~7–10 days. Decision-worthy if pipeline-manager surfaces, but not stale-flagged given Kay handles all replies per `feedback_kay_handles_all_replies`. Older drafts (>30 days) not flagged.

No previous-workday session-decisions file exists at `brain/context/session-decisions-2026-05-21.md` to cross-check against. Thursday's evening shutdown did not write one.

## 4. Introductions Detected

| from | offered_intro | direction | status |
|---|---|---|---|
| Sam Lamson (Libre Equity) | Emily, Jim Dine granddaughter, J Crew fashion designer (Montclair NJ → Manhattan), art-services storage experience | warm intro to Kay | already captured in 2026-05-21 inbox; needs Kay accept/decline per `feedback_bias_yes_on_introductions` (default-accept) |

Hannah Barrett's email broadcasts 24 PL Mid-Search Summit peer searchers via TO-line contact share. Treated as cohort networking, not 1:1 intros.

## 5. Niche Signals

- **Pest / NPMA Women's Forum** (Granola 2026-05-20 "2026 Women's Forum - NPMA: Education Session"): live signal on pest niche female-led network — direct alignment with women-led-throughline organizing principle. Surfaced to relationship-manager / pipeline-manager as ecosystem signal.
- **Art services / storage facilities** (Sam Lamson warm intro): Sam frames Emily as art-services subject-matter expert (J Crew designer + Jim Dine granddaughter, "quite a bit of experience dealing with art service providers, e.g., storage facilities"). Art-services is outside current bucket-1 thesis (pest is primary per 2026-05-20 women-led-throughline convergence). Worth a separate look but not a current niche shift. Per `feedback_bias_yes_on_introductions`, default-accept the intro itself.
- **Search-fund peer cohort** (Hannah Barrett PL Mid-Search Summit TO-line): 24 mid-search searchers exposed. Peer audience, not buyer/intermediary; informs `feedback_audience_taxonomy_conferences` Peer bucket.
- **Art Business Conference NY** (Granola 2026-05-21 + 2 inbound newsletters from Art Market Minds): Kay attended/registered. Conference-engagement skill may want post-conference follow-up window.

## 6. In-Person Meetings Today

Friday 2026-05-22:

| start_ET | end_ET | summary | counterparty | type | granola_reminder |
|---|---|---|---|---|---|
| 12:30 | 13:00 | Zoom Call — Kay Schneider and Sam Curcio | Sam Curcio, Transworld Business Advisors of NY (`scurcio@tworld.com`) — intermediary/broker | external | YES — Granola bot should auto-join Zoom `https://us06web.zoom.us/j/89885880388` |
| 16:00 | 16:30 | Sarah I Kay (Audio call) | `sarah@ridgewaymh.com` | external | YES — Google Meet `https://meet.google.com/njk-grsb-vob` |

Sam Curcio is an intermediary — meeting-brief should already exist via meeting-brief-manager nightly run.

## 7. Broker BLAST Listings (per-deal extraction)

None. Zero inbound emails in the 2-day window matched broker-signal keywords ("for sale" / "exclusive listing" / "asking price" / "we represent" / "new listing" / "now available" / "teaser" / "project [codename]"). BizBuySell newsletter is a marketplace digest, not a broker BLAST per `feedback_marketplace_vs_broker_distinction`.

## 8. Auto-Drafts Created

None. Zero inbound emails carried NDA-like or CIM-like attachments triggering the `<auto_ack_drafts>` pathway.

---

## Granola Ingestion Notes

7 Granola notes since last `brain/calls/` write (last call note 2026-05-15):

| created | granola_id | title | needs brain/calls write |
|---|---|---|---|
| 2026-05-19 | not_Vzn86Nudrldub0 | Mid-Search Summit — Reflections on Searching | yes (deferred to post-call-analyzer) |
| 2026-05-19 | not_KKWlYwkGEw8dup | Mid-Search Summit — Search Fund Market Update | yes (deferred) |
| 2026-05-19 | not_JCaHfPrTIZFzWm | Mid-Search Summit — The 5+1: How to Assess Industries (AI) | yes (deferred) |
| 2026-05-19 | not_HL86I5DUTLn1jV | Mid-Search Summit — Lunch & Practicing Your Pitch | yes (deferred) |
| 2026-05-20 | not_xEkdQVGMNxxTHQ | 2026 Women's Forum — NPMA: Education Session | yes (deferred) |
| 2026-05-20 | not_7sEFNCGtIbcIUM | WSN Group | yes (deferred) |
| 2026-05-21 | not_CWgPBpifBvuH9Q | The Art Business Conference | yes (deferred) |

Per architecture (`post-call-analyzer` 1pm + 6pm ET schedule), brain/calls/ writes + Attio/Drive landing are owned by post-call-analyzer, not email-intelligence. These 7 notes will land via post-call-analyzer's next scheduled fire (1pm ET today). If they have not landed by 6pm ET fire, pipeline-manager should flag.

## Run Metadata

- Run start: 2026-05-22 ~07:00 ET (systemd weekday)
- Source data: Gmail inbound (~22 threads), Gmail outbound (2 threads), drafts (12), Granola notes (7), session-decisions-2026-05-21 (absent), calendar (today)
- MCP availability: Granola MCP not authenticated in headless context — used `~/.local/bin/granola-api` REST wrapper instead (1Password-backed). No degradation.
- Bookkeeper P&L chain: not invoked (no detection); no `BOOKKEEPER-PL-CHAIN:` stdout marker required.
- Exit: 0

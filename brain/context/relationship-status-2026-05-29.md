---
date: 2026-05-29
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **Kyle McGrath** (Markel — Industry Expert, Fine Art & Specie) — Quarterly cadence, last contact 2026-02-10, 108 days, 10 days overdue against 98-day threshold.
   Suggested action: light quarterly check-in. `next_action` reads "No immediate action. Maintain quarterly touchpoint." — generic maintenance, no specific commitment owed. Carry-forward from 2026-05-28 (1 day older, still 0 outbound from Kay in last 14d). A short ping or an explicit cadence-downgrade decision will stop the daily re-fire.

2. **Christopher Wise** (Risk Strategies — Industry Expert, Insurance) — Quarterly cadence, last contact 2026-02-18, 100 days, 2 days overdue.
   Suggested action: light quarterly check-in. `next_action` reads "Quarterly nurture. No immediate action." — generic maintenance line, no commitment owed. Carry-forward from 2026-05-28. Same shape as Kyle (insurance/specie ecosystem peer, no live-deal trigger).

3. **chris.goyette** (Private Risk Management Association — Insurance ecosystem) — Occasionally cadence, last contact 2025-10-27, 214 days, 1 day over the 213-day threshold.
   Suggested action: light bi-annual check-in or skip-with-cadence-decision. NEW surface — just crossed the Occasionally threshold today. `next_action` empty; 0 outbound from Kay in 14d. Marginal (1 day over). Record-name hygiene: stored lowercase as "chris.goyette" — recommend capitalizing to a proper name in Attio.

4. **Donald Moore** (Marsh — Insurance) — Occasionally cadence, last contact 2025-10-28, 213 days, hits the threshold exactly today.
   Suggested action: light bi-annual touch. NEW surface. `next_action` reads "Nurture bi-annually. No immediate action." — the bi-annual intent matches the Occasionally cadence; 213 days ≈ 7 months, so this is the natural touchpoint moment. 0 outbound from Kay in 14d. Marginal (0 days over).

(Slot 5 intentionally empty — non-Dormant cadence-set produced 18 raw time-overdue contacts; the remaining 14 fall into trigger-exclude, recent-contact-signal, prior-PASS, or data-quality buckets enumerated in Suppressed / Run Notes below.)

Caveat: Gmail and Google Calendar are the only channels this skill verifies. Text, phone, and in-person interactions are not captured — Attio `next_action` notes are the secondary signal where present.

## Auto-Resolved (No Action Needed)

- None — Gmail 14d outbound search from `kay.s@greenwichandbarrow.com` to each surfaced candidate (Kyle, Christopher, chris.goyette, Donald Moore) returned 0 threads.

## Suppressed (prior PASS, trigger, recent-contact, or data-quality)

- **Kristina Marcigliano** (WTW) — Quarterly, 157 days. PASS'd in 2026-05-01 Friday nurture cluster ("all do not need to be addressed"). Carry-forward suppression — recommend explicit cadence-downgrade-or-Dormant so this stops re-firing.
- **Hunter Hartwell** (Ellirock) — Quarterly, 135 days. Same 2026-05-01 PASS cluster. Same cadence-decision recommendation.
- **Dan Tanzilli** (Third Eye Collective, Art World) — Monthly, 64 days. Same 2026-05-01 PASS cluster. Same cadence-decision recommendation.
- **Britta Nelson** — Quarterly, 164 days. `next_action`: "Texted recently (late March 2026). No follow-up needed. Maintain quarterly nurture." Attio note evidence of recent contact supersedes Gmail silence per SKILL.md.
- **Richard Augustyn** (Endurance Search Partners) — Quarterly, 214 days. Trigger: "Reach out when insurance deal enters Active Deals pipeline. Do not contact before then."
- **Sarah de Blasio** (Chartwell) — Quarterly, 126 days. Trigger: "Contact immediately when a deal of interest surfaces, especially art insurance brokerage."
- **Rachele Adelman** (Oberle Risk) — Quarterly, 196 days. Trigger: "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Michael Topol** — Quarterly, 172 days. Trigger: "Re-engage when we have an insurance deal for him to review. Trigger: deal flow only, not elapsed time."
- **Lauren Young** (USV) — Occasionally, 353 days. Trigger: "Re-engage when a specific introduction need arises."
- **Chase Lacson** (Goodman Taft, assistant) — Monthly, 214 days. Assistant-vs-principal: principal is Molly Epstein. `next_action`: "Reconnection email sent to Molly 3/30. Awaiting reply." Awaiting-reply trigger excludes the chain.

## Pending Intros

- None outstanding. The Marsha Weiner → Greg Pitkoff intro completed 2026-05-27 (Greg's inbound landed). Jeremy Black holds a standing "send relevant leads when they come up" deal-sharing relationship — not a discrete pending intro. Prior intros logged in `next_action` (Rachel ↔ Zoe, Kendall ↔ Amanda, Melissa Goldberg ↔ Kendall) remain closed.

## Warm Intro Opportunities (from target-discovery)

- None — no target-discovery handoff this morning (target-discovery remains paused per Active-Outreach-is-trigger doctrine).

## Vault → Attio Syncs

- **marsha-weiner.md** — engagement note "Heels and Deals 2026-05-27 — engagement context" created on Attio person `d4b79eb0-acfe-4c8f-9a30-3cbda770a74c` (HTTP 200). Attributes set (all were empty): `nurture_cadence` = Quarterly (prospect default), `how_introduced` + `value_to_search` populated; `relationship_type` left for Kay (connector — likely Industry Expert / River Guide, enum left to her). Vault frontmatter stamped `attio_id` + `attio_synced_at: 2026-05-29T10:54:16Z`. (Pre-existing "2026-05-13 Heels to Deals" note covers the event; this note captures the distinct 2026-05-27 Greg intro — non-duplicative.)
- **greg-pitkoff.md** — first engagement note "Intro 2026-05-27 — engagement context" created on Attio person `a019e717-6b31-44cd-8d97-9ac3af65a39e` (HTTP 200, 0 prior notes). Attributes set (all empty): `nurture_cadence` = Quarterly, `how_introduced` + `value_to_search` populated; `relationship_type` left for Kay. Vault frontmatter stamped. NOTE: this is sync-only — Greg's inbound reply itself is Kay-handled per 2026-05-28 session-decisions item 9 (PASS). Not surfaced for outreach.
- **sam-transworld.md** — carry-forward non-engagement drift (file mtime 2026-05-27T17:23Z > `attio_synced_at` 2026-05-27T12:00Z). Engagement note already exists; post-sync edit was internal infrastructure content, not new engagement. Idempotency guard holds — no duplicate write. Recommend either bumping `attio_synced_at` manually or adding a "skip if post-sync diff is non-engagement-content" rule to the SKILL to stop re-detection.
- All other persons modified in last 7 days (carlos-nieto-dca, oswaldo-ponce, sam-lamson, laura-smith-bankunited, matt-becky-colleague) — `attio_synced_at` (2026-05-22) ≥ file mtime, no drift. No action.
- **carlos-in3o.md** and **erika-teresko.md** — type=person but no `## Relationship Notes` section → do not meet sync criteria. No action. (Carlos uses Quick Facts / Communication Style structure; adding a `## Relationship Notes` section in a future session would enable engagement-context sync.)
- Companies (grip-communications, the-corporate-coach) — out of scope (people-only sync).

## Attio Dedup Needed (carry-forward)

- **Austin Yoder** — 2 person records both Quarterly cadence (verified live 2026-05-29):
  - `24aef54c-9820-46b6-9b8d-8d4c2ba3972d` (email: hello@cal.com — calendar-bot artifact, last_interaction 2026-02-19)
  - `2928b44c-3e84-454d-be6a-2473d4f212b3` (email: austin@magratheapartners.com — real record, last_interaction 2026-03-23)
  Recommend Kay merge or delete the cal.com stub. Open since 2026-05-27.
- **Jim Vigna** — duplicate persists: live record `5a6ee0f6-47f6-47e5-8357-e739281112f3` (email: jim.vigna@liveoak.bank), cadence-set stub `679646d0-9df0-4ea6-828e-93a1a7465ea2` (Quarterly, no email, no last_interaction). Recommend merge.

## Metadata Drift / Record Hygiene (carry-forward)

- **`thyme@everystall.com`** — Occasionally cadence, no name, no `last_interaction` (orphan since 2025-06-03). Recommend deletion or Dormant.
- **`customercare@squarespace.com`** (name "Squarespace") — Occasionally cadence, vendor support address. Recommend Dormant.
- **`bluerideradmin@morganstanley.com`** — Quarterly cadence, system/admin stub. Recommend Dormant or deletion.
- **Michelle Perr** (UBS) — Occasionally cadence, no `last_interaction` populated. Backfill or Dormant.
- **David Wolkoff** (Former Colleague) — Occasionally, no email, no `last_interaction`. `next_action`: "Personal relationship, not search-related. Maintain warmth." Recommend Dormant or backfill.
- **chris.goyette** — surfaced above as overdue; name stored lowercase. Recommend capitalization to proper name in Attio.

## System Status Alerts

- None. Attio REST health-check returned 200 (`GET https://api.attio.com/v2/self`). Notes write succeeded (2 notes, HTTP 200 each) — `notes:read-write` scope confirmed present. Attribute PATCH succeeded (HTTP 200). Gmail wrapper (`gog gmail search`) returning JSON envelope cleanly. Vault filesystem reads/writes clean. (Attio MCP intentionally not used — REST is the default per phantom-outage doctrine; an unloaded MCP tool is NOT an outage.)

## Run Notes

- Total Attio People records scanned (full pagination, 4 pages): 1,859
- Cadence-set: 75 (Dormant 28 / Quarterly 20 / Occasionally 24 / Weekly 1 / Monthly 2)
- Non-Dormant cadence-set: 47
- Raw time-overdue (cadence threshold met or exceeded): 18 (Quarterly 11 / Occasionally 5 / Monthly 2 / Weekly 0)
- Strict trigger-language exclusions (when/once/after/if/re-engage when/do not contact/awaiting): 6 — Richard Augustyn, Sarah de Blasio, Rachele Adelman, Michael Topol, Lauren Young, Chase Lacson
- Recent-contact-signal exclusion (Attio note supersedes Gmail silence): 1 — Britta Nelson
- Prior-PASS suppressions (2026-05-01 Friday cluster, carry-forward): 3 — Kristina Marcigliano, Hunter Hartwell, Dan Tanzilli
- Data-quality / non-relationship exclusions: 4 — Austin Yoder (cal.com stub), bluerideradmin (admin), Squarespace (vendor), thyme@everystall.com (orphan)
- Action-already-taken auto-resolutions (Gmail 14d outbound search): 0
- Session-decisions cross-check (2026-05-28): no overlapping PASS/APPROVE/DEFER on the 4 surfaced contacts. Greg Pitkoff (item 9 PASS = Kay handles) and Carlos in3o (item 6 PASS) handled as suppress-from-outreach; Greg synced to Attio only, not surfaced.
- Vault → Attio syncs executed: 2 (marsha-weiner, greg-pitkoff) — notes + attributes + vault stamps all HTTP 200
- Final surfaced: 4 (Kyle McGrath, Christopher Wise, chris.goyette, Donald Moore)

---
date: 2026-05-28
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **Kyle McGrath** (Markel — Industry Expert, Fine Art & Specie) — Quarterly cadence, last contact 2026-02-12, 106 days, 8 days overdue against 98-day threshold.
   Suggested action: light quarterly check-in. `next_action` reads "No immediate action. Maintain quarterly touchpoint." — generic maintenance, no specific commitment owed. Carry-forward from 2026-05-27 (1 day older, 0 outbound from Kay in last 14d). A short ping or skip with cadence-downgrade decision is sufficient.

2. **Christopher Wise** (Risk Strategies — Industry Expert, Insurance) — Quarterly cadence, last contact 2026-02-19, 98 days, hits threshold exactly today.
   Suggested action: light quarterly check-in. `next_action` reads "Quarterly nurture. No immediate action." — generic maintenance line, no commitment owed. First surface; not previously PASS'd. Same shape as Kyle (insurance/specie ecosystem peer, no live deal trigger).

(Slots 3-5 intentionally empty — cadence-set produced 15 raw-overdue contacts; remaining 13 fall into trigger-exclude, recent-contact-signal, prior-PASS, or data-quality buckets enumerated in Suppressed / Run Notes below. No new candidates after filters.)

Caveat: Gmail and Google Calendar are the only channels this skill verifies. Text, phone, and in-person interactions are not captured — Attio `next_action` notes are the secondary signal where present.

## Auto-Resolved (No Action Needed)

- None — Gmail 14d outbound search from `kay.s@greenwichandbarrow.com` to surfaced candidates (Kyle, Christopher) returned 0 threads each.

## Suppressed (prior PASS, trigger, recent-contact, or data-quality)

- **Kristina Marcigliano** (WTW) — Quarterly, 155 days. PASS'd in 2026-05-01 Friday nurture cluster ("all do not need to be addressed"). Carry-forward suppression — recommend explicit cadence-downgrade-or-Dormant decision so this contact stops re-firing in the cadence query.
- **Hunter Hartwell** (Ellirock) — Quarterly, 133 days. Same 2026-05-01 PASS cluster. Same suppression + cadence-decision recommendation.
- **Dan Tanzilli** (Third Eye Collective, Art World) — Monthly, 62 days. Same 2026-05-01 PASS cluster. Same suppression + cadence-decision recommendation.
- **Britta Nelson** — Quarterly, 162 days. `next_action`: "Texted recently (late March 2026). No follow-up needed. Maintain quarterly nurture." Attio note evidence of recent contact supersedes Gmail silence per SKILL.md.
- **Chase Lacson** (Goodman Taft, assistant) — Monthly, 211 days. Assistant-vs-principal rule: principal is Molly Epstein. `next_action`: "Reconnection email sent to Molly 3/30. Awaiting reply." Awaiting-reply trigger excludes the chain.
- **Lauren Young** (USV) — Occasionally, 351 days. Trigger: "Re-engage when a specific introduction need arises."
- **Richard Augustyn** — Quarterly, 212 days. Trigger: "Do not contact before..." / "Reach out when insurance deal enters Active Deals pipeline."
- **Rachele Adelman** (Oberle Risk) — Quarterly, 194 days. Trigger: "When insurance DD needed on a target, reach out to August Felker, cc Rachele."
- **Michael Topol** — Quarterly, 170 days. Trigger: "Re-engage when we have an insurance deal for him to review."
- **Sarah de Blasio** (Chartwell) — Quarterly, 124 days. Trigger: "Contact immediately when a deal of interest surfaces, especially art..."

## Pending Intros

- None outstanding across cadenced contacts. Intros previously logged in `next_action` (Rachel ↔ Zoe — completed 2026-04-01; Kendall ↔ Amanda — completed; Melissa Goldberg ↔ Kendall — completed) are closed. Jeremy Black holds a "send relevant leads when they come up" standing relationship — not a pending intro.

## Warm Intro Opportunities (from target-discovery)

- None — no target-discovery handoff this morning (target-discovery remains paused per Active-Outreach-is-trigger doctrine).

## Vault → Attio Syncs

- **sam-transworld.md** — engagement-context note already exists in Attio ("Becky→Sam warm intro 2026-05-18 + 5/22 Zoom — engagement context", created 2026-05-22). Carry-forward drift: file mtime is 2026-05-27T13:23 ET (~17:23Z), `attio_synced_at` is 2026-05-27T12:00:00Z. The post-sync edit was an internal "Open Loops" / Attio-infrastructure note, not new engagement content (verified yesterday and unchanged today). Idempotency guard prevents duplicate note write. Recommend manually bumping `attio_synced_at` to 2026-05-28T07:00:00Z to permanently stop re-detection, OR adding a "skip if post-sync diff is non-engagement-content" rule to the SKILL.
- **carlos-in3o.md** — type=person, no `attio_id`, no `attio_synced_at`. Does NOT meet sync criteria — lacks `## Relationship Notes` section (file uses Quick Facts / Communication Style / Working Notes structure). No sync action. Attio person record for Carlos likely auto-created on Kay's 5-26 19:39 reply; consider adding `## Relationship Notes` to the vault file in a future session to enable engagement-context sync.
- All other persons modified in last 7 days (carlos-nieto-dca, oswaldo-ponce, sam-lamson, laura-smith-bankunited, matt-becky-colleague) — `attio_synced_at` ≥ file mtime, no drift. No action.
- Companies (poza-capital-partners, libre-equity-partners) — out of scope for this skill (people-only sync per SKILL.md).

## Attio Dedup Needed (carry-forward)

- **Austin Yoder** — 2 person records both with Quarterly cadence (verified live 2026-05-28):
  - `24aef54c-9820-46b6-9b8d-8d4c2ba3972d` (email: hello@cal.com — calendar-bot artifact)
  - `2928b44c-3e84-454d-be6a-2473d4f212b3` (email: austin@magratheapartners.com — real record)
  Recommend Kay merge or delete the cal.com stub. Open since 2026-05-27.
- **Jim Vigna** — duplicate persists: live record `5a6ee0f6-47f6-47e5-8357-e739281112f3` (email: jim.vigna@liveoak.bank), cadence-set stub `679646d0-9df0-4ea6-828e-93a1a7465ea2` (no email, no last_interaction). Recommend merge.

## Metadata Drift / Record Hygiene (carry-forward)

- **`thyme@everystall.com`** — Occasionally cadence, no name, no `last_interaction`. Likely vendor/system stub. Recommend deletion or Dormant.
- **`customercare@squarespace.com`** — Occasionally cadence, vendor support address. Recommend Dormant.
- **`bluerideradmin@morganstanley.com`** — Quarterly cadence, system/admin stub. Recommend Dormant or deletion.
- **Michelle Perr** (UBS) — Occasionally cadence, no `last_interaction` populated. Backfill or Dormant.
- **David Wolkoff** (Former Colleague) — Occasionally, no email, no `last_interaction`. `next_action`: "Personal relationship, not search-related. Maintain warmth." Recommend Dormant or backfill.

## System Status Alerts

- None. Attio REST health-check returned 200 (`GET https://api.attio.com/v2/self`). Gmail wrapper (`gog gmail search`) returning JSON envelope with `threads` array. Vault filesystem reads clean. (Attio MCP intentionally not used — REST is the default per phantom-outage doctrine; unloaded MCP tool is NOT an outage.)

## Run Notes

- Raw cadence-set (non-Dormant): 47 contacts (Weekly 1 / Monthly 2 / Quarterly 20 / Occasionally 24)
- Initial overdue (cadence threshold met or exceeded): 15
- Records with no `last_interaction` (excluded from overdue, surfaced under Metadata Drift): 3 — Jim Vigna, Michelle Perr, David Wolkoff
- Strict trigger-language exclusions (when/once/after/if/re-engage when/do not contact/awaiting): 6 — Chase Lacson, Lauren Young, Richard Augustyn, Rachele Adelman, Michael Topol, Sarah de Blasio
- Recent-contact-signal exclusions (Attio note supersedes Gmail silence): 1 — Britta Nelson
- Prior-PASS suppressions (2026-05-01 Friday cluster, carry-forward): 3 — Kristina Marcigliano, Hunter Hartwell, Dan Tanzilli
- Data-quality / non-relationship exclusions: 3 — Squarespace (vendor inbox), thyme@everystall.com (orphan), bluerideradmin@morganstanley.com (admin stub)
- Action-already-taken auto-resolutions (Gmail 14d outbound search): 0
- Session-decisions cross-check (2026-05-26): no overlapping PASS/APPROVE/DEFER on Kyle McGrath or Christopher Wise; James Emden cleared from cadence query already (next_action wiped 5-26)
- Final surfaced: 2 (Kyle McGrath, Christopher Wise)

---
date: 2026-04-28
type: relationship-status
---

## Overdue Contacts (Top 5)

1. **Molly Epstein** (Goodman Taft) — Occasionally cadence, last contact 2026-03-31 (Kay's reconnection draft, awaiting reply). Reconnection email already sent ~30 days ago with no response. Within Occasionally 213-day threshold, BUT next_action says "Awaiting response" and 4 weeks of silence after a reconnection attempt is the actionable signal. *(Note: Chase Lacson assistant record at the same firm was 147d over Monthly threshold — per SKILL.md assistant-vs-principal rule, surface the principal Molly, not Chase.)*
   Suggested action: Soft-nudge follow-up — one-line note acknowledging the silence and offering an alternative window. Or PASS/Dormant if Kay considers Molly fully dead.

2. **Hunter Hartwell** (Elli Rock) — Quarterly cadence, last contact 2026-01-14 (Jan 12 call), 6 days over the 98-day threshold. Empty next_action. Kay had a working relationship via Sara Rosenthal (TTCER) intro thread.
   Suggested action: Light check-in email — "thinking of you, what's new at Elli Rock" reference last call.

3. **Kristina Marcigliano** (WTW) — Quarterly cadence, last contact 2025-12-23 (Dec 22 meeting), 28 days over threshold. Empty next_action.
   Suggested action: Coffee/call invite if NYC-based, or quick check-in email referencing last meeting. Kay should decide if WTW relationship still warrants quarterly cadence — if not, downgrade to Occasionally.

4. **Heritage Auctions** (do-not-reply@ha.com) — Quarterly cadence, 55 days over threshold. This is a no-reply mailing-list address, not a relationship.
   Suggested action: METADATA — re-cadence to Dormant or remove from nurture. Not a real overdue.

5. **thyme@everystall.com** — Occasionally cadence, last contact 2025-06-03, 116 days over threshold. No real name on the record, no next_action.
   Suggested action: METADATA — investigate who this is (looks like a generic stall address). Either fill in person details or downgrade to Dormant.

**Caveat:** Gmail and calendar are the only verified channels. Kay also communicates by text, phone, and in-person — text-message follow-ups won't show up here. Trust Attio `next_action` text over Gmail silence when it has been recently updated by Kay.

## Auto-Resolved (No Action Needed)

- None today. Chase Lacson (assistant at Goodman Taft) was the only candidate that could have been auto-resolved via the Molly reconnection thread, but per SKILL.md the principal Molly is the one being surfaced — Chase is filtered out as an assistant record, not auto-resolved.

## Pending Intros

- None outstanding. All recently committed intros have been verified as completed:
  - Rachel Tepper → Zoe Wen: completed 2026-04-01 (Rachel replied 2026-04-02). Cleared.
  - Kendall Warson → Amanda: completed (per next_action "introduced to Amanda. No pending action").
  - Melissa Goldberg → Kendall (Cohart) → Amanda: chain completed.

## Warm Intro Opportunities (from target-discovery)

- None surfaced this run. target-discovery has not handed off new targets requiring warm-intro mining.

## Vault → Attio Syncs

- **Jim Vigna** (Live Oak Bank): engagement note "XPX 2026-04-23 — engagement context" attached (note ID `0ffba7d2-22ae-49a5-8c70-ad9c88194596`). attio_id was already set; vault `attio_synced_at` updated.
- **Ian Stuart** (CFO Consulting Partners): engagement note attached (note ID `db23fb2d-e995-46ea-be2d-f608e3c04508`). Vault `attio_synced_at` set, `attio_sync_pending` cleared. Status remains vendor-declined.
- **Peter Shakalis** (Helmsley Spear): engagement note attached (note ID `7dec3ebb-6f4f-42f4-a33d-749d82ad9cef`). Captures the network-via-James-Emden context. Vault frontmatter updated.
- **James Emden** (Helmsley Spear): engagement note attached (note ID `1b54cb0f-896f-48e6-808f-7b973d77a864`). River Guide candidate context preserved including Becky Creavin signal and Peter-grooming detail. Vault frontmatter updated.
- **Andrew Lowis** (Axial): engagement note attached (note ID `b427ecbb-cac1-46e8-8e63-88367d6ddc23`). XPX panel-speaker context, research-only-Axial-usage flag, digital-deck commitment captured. Vault frontmatter updated.

5/5 entities with `attio_sync_pending` flags from yesterday's scope-blocked attempts have synced successfully. The 4/27 token rotation gave the Attio MCP token the missing `notes:read-write` scope. Backfill complete.

## Attio Dedup Needed

- None detected this run. Two "Austin Yoder" records exist (hello@cal.com vs austin@magratheapartners.com) — confirmed they are two different people / different emails, not a dedup issue.

## System Status Alerts

- Attio token scope: VERIFIED working. Curl probe to `/v2/objects` returned 200, and 5 successful `create_note` calls confirm `notes:read-write` scope is active. Yesterday's scope-blocked sync queue is fully drained.
- Today's launchd run (`logs/scheduled/relationship-manager-2026-04-28-0650.log`) hung mid-attempt; this artifact was produced via manual recovery in the post-restart session. Per yesterday's deferral, this closes the loop for 2026-04-28.

## Metadata Drift

Surfaced for Kay's awareness — not actionable as overdue:

- **Heritage Auctions** (do-not-reply@ha.com): Quarterly cadence on a no-reply mailing-list address. Recommend re-cadence to Dormant.
- **thyme@everystall.com**: Occasionally cadence, no name, no next_action, 116d over. Recommend either fill in identity or move to Dormant.
- **Michelle Perr** (UBS): Occasionally cadence with no recorded interaction at all. Either Kay never actually engaged (downgrade to Dormant) or the interaction predates Attio sync history (leave as-is, no action).
- **Chase Lacson** (Goodman Taft assistant): Monthly cadence on an assistant role. Recommend re-cadence to "Dormant" or "Quarterly" since assistants don't warrant Monthly direct-touch — the principal (Molly Epstein) is the relationship.

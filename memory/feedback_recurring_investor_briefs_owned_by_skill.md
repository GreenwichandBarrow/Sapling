---
name: Recurring investor briefs auto-fire from owning skill 24h ahead
description: Recurring investor briefs (biweekly Guillermo, monthly Jeff Stevens, quarterly all-LP) auto-fire from the `investor-update` skill on per-cadence cron 24h ahead. Don't depend on pipeline-manager pre-flight.
type: feedback
originSessionId: 326c69dd-5175-4205-89f6-eb4a9ec64ab8
---
**Rule:** Recurring investor briefs are owned by the `investor-update` skill. They auto-fire 24 hours ahead of the scheduled call on a per-cadence cron, NOT via pipeline-manager's calendar pre-flight scan.

**Cadences:**
- **Biweekly Guillermo Lavergne** — auto-fire 24h ahead of each scheduled biweekly slot.
- **Monthly Jeff Stevens** — auto-fire 24h ahead of each scheduled monthly slot.
- **Quarterly all-12-LPs deck** — auto-fire 1 week ahead (longer prep window for the deck assembly).
- **Post-LOI weekly DD** — auto-fire 24h ahead of each weekly DD call (event-driven, post-LOI only).

**Forbidden pattern:** Assuming pipeline-manager's brief-decisions pre-flight will catch recurring biweekly/monthly investor calls. Pipeline-manager's 2-day-lookahead window can miss recurring events that fall outside it (e.g., a biweekly that's >2 days out at scan time but lands today after a weekend).

**Why:** Recurring events have two failure modes that stack:
1. **Pipeline-manager skips them** because the assumption is "the owning skill handles recurring."
2. **Owning skill doesn't auto-fire** because the schedule isn't wired (no launchd plist, no cron).

On 2026-05-06, today's biweekly Guillermo call had no brief generated. Pipeline-manager skipped (assumed `investor-update` had it). `investor-update` didn't auto-fire (no scheduled trigger wired). Required a crash-mode 10-min brief at 1 PM. The fix is to wire the `investor-update` skill to auto-fire on a per-cadence cron + have pipeline-manager STILL verify the brief exists per `feedback_preflight_covers_today_and_tomorrow` (trust-but-verify).

**How to apply:**
- Add `investor-update` plists or per-mode launchd entries:
  - `com.greenwich-barrow.investor-update-biweekly-guillermo.plist` — fires from a calendar scan that detects upcoming biweekly Guillermo events 24h out.
  - Same pattern for monthly Jeff Stevens, quarterly all-LP, and weekly post-LOI.
- On each fire, the skill: (a) checks if a brief exists for the upcoming call, (b) generates one if missing, (c) writes vault + Drive + Slack ping.
- Idempotency: skill skips if a brief already exists for the call (don't overwrite Kay's edits to the Drive Doc).

**Source:** 2026-05-06 Guillermo brief miss. Trace at `brain/traces/2026-05-06-same-day-externals-preflight-gap.md`. Cousin rule to `feedback_preflight_covers_today_and_tomorrow`.

---
name: always-polite-and-warm
description: Every external message Kay sends (email, LinkedIn, Slack, text) MUST include warmth and niceties — openers, closers, and tone throughout. Never abrupt, never terse-only-business. Politeness is core to her voice, not optional decoration.
metadata:
  type: feedback
---

## Rule

Every external message Kay sends — cold or warm, short or long — must include explicit warmth. Politeness and being-appropriate is **incredibly important** to Kay (her words, 2026-05-12). Skipping niceties in service of brevity or signal-density is wrong. It reads as cold and off-brand for her.

**Niceties to include (at least one opener + one closer, more is fine):**

| Slot | Examples |
|---|---|
| **Opener** | "Hope you're doing well." / "Hope this finds you well." / "Hope your week is off to a good start." / "Good to hear from you." / "Thanks for reaching out." / "Thanks for the check-in." |
| **Warmth mid-body** | "Congrats on [X]." / "That's a busy stretch." / "Glad things are going well." / "Sounds like a great milestone." |
| **Closer** | "Thanks!" / "Looking forward to it." / "Talk soon." / "Looking forward to hearing back." (and ALWAYS use day-aware sign-off line: "Best," / "Have a great weekend!" per `feedback_day_aware_signoffs`) |

## Why

Kay's pattern is warm-professional. She built G&B's voice around being personable, not transactional. Owners, intermediaries, investors, peer searchers — all respond better to a friendly opener and a polite closer. A pure business-only message reads as PE-vibe and undermines her positioning per `feedback_pe_vibe_from_we_centric_copy`.

Repeated calibration:
- 2026-05-12 mid-day — Kevin O'Connell LinkedIn draft pruned of all niceties for character economy. Kay corrected: "i ALWAYS include niceties." Followed by: "being polite and appropriate is incredible important to me, please remember."

## How to apply

- **Cold outreach (Connect notes, intro emails):** open with "Hope you're doing well" or equivalent. Close with "Thanks!" or "Looking forward to hearing back." Even at 300-char LinkedIn limits, fit at least one opener + one closer; trim body text to make room, not niceties.
- **Warm-thread replies:** open with "Thanks for the check-in" / "Good to hear from you" / "Thanks for reaching out" / "Congrats on [thing they mentioned]" depending on context. Close polite.
- **Conference / RSVP replies:** open with "Thank you so much for the invitation." Even when declining, the opener is warm.
- **Slack to team (JJ, Sam, internal):** still warm but shorter — "Hi {Name}," opener and "Thanks!" or "Talk soon!" closer per `feedback_slack_brevity` (brevity ≠ coldness; the niceties stay, the body shrinks).
- **Difficult messages (decline, redirect, no):** niceties matter MORE, not less. Lead with appreciation + warmth before the no.

## Forbidden patterns

- Opening with just the body content (no "Hi Name," + no opener nicety). Reads as cold.
- Closing with just "Best, Kay" without a closer nicety line. Reads as transactional.
- Using "Cheers" or "Thanks." as a one-word substitute for full niceties.
- Skipping niceties for character-count reasons. Tighten body before tightening warmth.

## Pre-flight check (add to outbound checklist)

Before showing Kay any draft, verify:
- [ ] Opener nicety present ("Hope this finds you well" / "Thanks for..." / "Good to hear from you" / "Congrats on...")
- [ ] At least one warm phrase in the body if it's longer than 3 sentences
- [ ] Closer nicety present ("Thanks!" / "Looking forward to..." / "Talk soon")
- [ ] Day-aware sign-off line per `feedback_day_aware_signoffs`

This rule reinforces and overlaps with: `user_outreach_voice`, `feedback_no_soft_signal_stacking` (one soft signal max, but niceties are NOT soft signals — they're tone-warmth and don't count toward the soft-signal cap), `feedback_day_aware_signoffs`.

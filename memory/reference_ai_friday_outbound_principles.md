---
name: AI Friday Outbound Engine principles (Apr 24 2026 session)
description: Reference framework for evaluating outbound — psychology, presumptive personalization, signal-based outreach, two-stage scoring, iteration velocity. Applied when reviewing DealsX, JJ scripts, or any new outbound playbook.
type: reference
originSessionId: 02a8f99b-e981-420b-a53a-8eb7191dc71e
---
Source: Granola notes from "AI Friday: Building an AI-Powered Outbound Engine That Converts" (Apr 24 2026). Pulled and applied 2026-04-27 to review DealsX campaign playbook.

## Core principles (use as a checklist for any outbound copy review)

1. **Psychology > features.** Lead with risk/threat reduction or *existing* discomfort, not benefits. CAVEAT for G&B: their "survival brain" framing only works when naming a discomfort the prospect *already feels* (succession uncertainty, what happens to the team). Manufactured threat ("the wrong buyer would ruin you") reads adversarial and is blocked by `feedback_outreach_about_them` + `feedback_outreach_no_fake_lines`.

2. **Presumptive personalization.** Avoid `[Company Name]` tokens at the *end* of sentences — reads as canned. Embed the company reference earlier so it passes naturally. Use all-lowercase company names in subject lines. Use a GPT call to clean/reformat company names before insertion.

3. **Signal-based > cold spray.** Hiring activity (LinkedIn Jobs), LinkedIn posting activity, operational-complexity indicators dramatically outperform generic outreach. Reference *existing momentum* — never try to create a new priority for the prospect.

4. **Two-stage scoring.** Static attributes (don't change often: public checkout, wholesale vs DTC, retail marketplace count) + dynamic signals (real-time job postings, news, hiring). G&B equivalent already exists: scorecard (static) + briefing signals (dynamic).

5. **Iteration velocity is the moat.** 10 experiments/day beats one perfect annual plan. Friday meta-calibration loop already does this.

6. **Channel strategy:**
   - Email: anonymous, infinitely scalable, hardest to convert. "Clinical trial R&D."
   - Phone: tightest feedback loop, talent-dependent.
   - LinkedIn: profile credibility, rate-limited, not anonymous.
   - Direct mail: high pattern interrupt, X-factor.

7. **One person + AI** can run outbound that used to need a 10-person SDR team. Operator hub concept = unified Claude terminal replacing CRM/inbox/calendar = Sapling OS.

## How to apply

When reviewing any outbound copy (DealsX playbook, JJ scripts, conference outreach templates, intermediary emails):
- Run through the 6 principles above as a checklist.
- Flag token-placement violations (rule #2) — this is the #1 slop tell.
- Flag manufactured threat vs. named-existing-discomfort (rule #1) — common DealsX-style overreach.
- Confirm signals being referenced are *existing momentum*, not invented priorities (rule #3).
- Check that copy has variant rotation for iteration velocity (rule #5) — if only one version exists, push for A/B variants.

## Vendors mentioned

See `reference_outbound_vendors.md` for TitanX (phone propensity), Handwrytten (direct mail), Apollo job-postings (signal detection we already pay for but aren't using).

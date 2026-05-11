---
name: Intermediary outreach — 7 per day, total
description: Daily intermediary outreach is 7 touches per day TOTAL across all channels (not additive). Channel picked per-person. Replaces the 5+5 split; bumped on 2026-05-06 to hit 50-emails-by-5/15 catch-up.
type: feedback
originSessionId: cece2f47-c8d7-4430-af72-e9cfb7942006
---
**Rule:** Daily broker/intermediary outreach is **7 touches per day, TOTAL across all channels.** Not 7 emails + LinkedIn additive. The 7-cap is the full daily volume; channel mix is determined per-person within that cap.

**Per-person channel selection (within the 7-cap):**
- Verified email available → email channel (default — email is the priority channel because the 50-by-5/15 target is email-specific)
- Email unreachable (Apollo no-match, dead bounce) but LinkedIn profile is active → LinkedIn channel
- Same person never on both channels in the same day

**Why:** Total touch volume matters for sender reputation and bandwidth, not channel-isolated cadence. The earlier 5+5 frame was additive (10 touches/day total) and overstated bandwidth. Kay corrected on 2026-05-06: total intermediary outreach is 7/day, period. Email gets first claim on those 7 slots because the 50-emails-by-Fri-5/15 catch-up target is email-specific. LinkedIn fills any remainder for Apollo no-match brokers.

Math for the catch-up: 50 emails ÷ 8 workdays remaining (5/6 → 5/15) = 6.25/day → rounded to 7 daily-cap. If on a given day every slot goes to email (all 7 brokers email-reachable), we hit ~56 emails by 5/15 — clears the target. If some slots fall to LinkedIn DMs (Apollo no-match), email count is lower but we don't go above 7 total touches.

**How to apply:**
- When outreach-manager Subagent 3 (intermediary cold) builds the daily send list, build ONE roster of 7 names — not two. For each name, pick channel (email default, LinkedIn fallback) at roster-build time.
- For Apollo no-match brokers: their slot routes to LinkedIn DM, not Hunter/Snov retry. They occupy one of the 7 daily slots, not a 6th-and-beyond bonus slot.
- Day's outreach artifact records the roster of 7 + per-name channel picked, so we can track per-channel response rates over time.
- Supersedes the prior 5+5 frame entirely (file renamed twice on 2026-05-06: first to 7+5 in error, then corrected to 7/day-total).
- After 2026-05-15 review the cadence — if 50-target was a one-off catch-up, drop back to 5/day total; if Kay wants the higher pace as steady state, 7/day stays.

**Source:** Kay confirmed 2026-05-05 morning during DealsX dedup task (original 5+5 split framing, 5 emails written, 9 person-found-no-email). Bump confirmed 2026-05-06 morning briefing — Kay clarified mid-morning that the new daily cap is 7 TOTAL, not 7 email + 5 LinkedIn additive. The earlier 7+5 phrasing in this file's first version (and in my morning recommendation) was a misread.

---
name: Calibrate before bulk writes when user signals yield uncertainty
description: When Kay says "flag if more than X" or "I imagine ~Y", treat as calibration request, not execution greenlight. Run read-only scan first, report counts, wait for confirmation.
type: feedback
originSessionId: 4d4166cd-0bb3-4a20-887c-1f29801ff285
---
When Kay greenlights a bulk scan-and-write workflow but adds ANY of these signals, treat it as a calibration request, not an execution greenlight:

- "flag and pause if more than X"
- "I imagine we have ~Y"
- "make sure we're pulling strong ones"
- "if you're pulling 100 for one niche, that's wrong"
- Any numeric upper or lower bound on expected output

**Behavior:** Run a read-only scan first. Report per-bucket counts + a small sample. Wait for explicit keep/tighten/loosen before any writes.

**Why:** On 2026-04-20, Kay greenlit Phase 3 Network Matches execution across 8 niches with "10 tops per niche, flag if more." The skill's default would have been to write up to 10/niche per self-cap. Calibration pass instead revealed thin yield (5 total hits across 8 niches) and 6 niches with zero/FP matches. Had the skill proceeded with self-capped writes, Network Matches tabs would have shipped with a false-bottom-line of "thin yield = reality" instead of the truth (thin yield = instrument gap). Calibration pass caught it.

**How to apply:**
- In the subagent prompt for any calibration pass, explicitly list forbidden tools (Attio create/update, Google Sheet writes, vault writes). Do not rely on vague "don't write" framing — subagents may reinterpret.
- Report format: per-bucket count + over-cap flag + top-3 sample. Not the full dump. Density matters.
- Apply the **two-sided cap check**: pause on `count > expected_max` AND on `count == 0 when signal_expected`. Zero-yield when user expects hits is equally a calibration signal.
- This pattern applies broadly, not just to river-guide-builder: relationship-manager morning scans, target-discovery niche refills, warm-intro-finder ecosystem scans, any bulk enumeration against Kay's data.

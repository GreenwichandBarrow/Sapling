---
name: Warm intro check before any sheet write
description: No target enters the sheet or automated pipeline without warm intro check completing first
type: feedback
---

Warm intro check (Phase E) is a HARD STOP before any target is written to the sheet. No exceptions.

**Why:** If Kay has a warm path to the owner through her network, burning that connection with a Salesforge cold email sequence is worse than no outreach at all. During the Art Advisory test run, 27 targets were written to the sheet before warm intro check ran — this was caught and hardened into a stop hook.

**How to apply:** target-discovery Phase E runs warm-intro-finder (LinkedIn CSV grep → Attio → vault → Gmail) for every target. If warm intro found → target goes to morning briefing for Kay's decision (personal draft or Salesforge). Only targets with no warm path proceed to Phase F (sheet write).

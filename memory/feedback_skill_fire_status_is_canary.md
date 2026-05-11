---
name: Scheduled-skill fire-or-no-fire status is the daily canary
description: Dashboard's C-Suite & Skills page exists because scheduled skills fail silently via launchd. Primary signal is fire/no-fire per skill per day, not override rates or invocation counts.
type: feedback
originSessionId: ebd58436-6958-4e18-98eb-a6797b0d0b46
---
The Command Center's "C-Suite & Skills" page (what Pober called "AI Agents") exists for one primary reason: **catching skills that didn't fire when they should have.**

**Why:** 4/24 dashboard scope session — I initially argued this page was "interesting-not-actionable" (override rates, invocation counts being vanity). Kay corrected: "we have often seen that skills didn't fire/launch." launchd fails silently when a plist is malformed, the Mac was shut down instead of sleeping, or a dependency broke. The only way Kay currently catches this is when something downstream breaks.

**Page design implications:**
- Primary signal per skill per day: 🟢 fired on schedule / 🟡 fired with warning / 🔴 scheduled but no fire / ⚪ not scheduled today.
- Organized by C-suite agent (CFO, CIO, CMO, CPO, GC, COO) with skills nested underneath.
- Kay checks this daily as part of her system-health glance, not weekly.
- Override rates / invocation counts / verdict splits are secondary — useful for calibration-workflow's weekly review, not daily decision surface.

**How to apply:**
- When scoping this page in build, lead with fire/no-fire status, not analytics.
- Cross-reference against `CLAUDE.md` Scheduled Skills table per `feedback_staleness_check_schedule_first.md` to know what SHOULD have fired.
- Label: prefer "C-Suite & Skills" or "Team" over Pober's "AI Agents" — reflects G&B's org model, not generic tooling.

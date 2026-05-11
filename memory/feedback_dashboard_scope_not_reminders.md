---
name: Dashboard is not a reminder/nag surface; digest lines live on health-monitor
description: Command Center dashboard excludes email-draft reminders and daily nurture prompts. Routine per-skill activity ("X conferences added", "Y niches added", "Z preps added") belongs on health-monitor as one-line digest entries, not as dedicated dashboard pages.
type: feedback
originSessionId: ebd58436-6958-4e18-98eb-a6797b0d0b46
---
The Command Center dashboard is for acting on live operational data (deals, pipeline, activity analytics) — not for reminding Kay of things she already tracks elsewhere.

**Specifically OUT of dashboard scope:**
- **Email drafts awaiting send.** Kay checks Superhuman daily — drafts are already visible there. A dashboard reminder is noise.
- **Daily nurture-cadence reminders / overdue contacts.** Kay has been ignoring these in morning briefings; they take up space without driving action. Demote relationship-manager output from daily briefing to a **Friday-only** "people to circle back with" artifact.
- **Dedicated pages for conference pipeline, new niches, investor-prep pipeline.** These are per-skill activity summaries, not daily decision surfaces.

**Where digest-style activity lines belong:** health-monitor absorbs them as one-line entries.
- "4 conferences added today" (conference-discovery)
- "5 niches added" (niche-intelligence)
- "4 investor preps drafted" (investor-update)
- Skill run status (existing)

**Why:** 4/24 dashboard scope session — Kay repeatedly pared back the scope I was proposing. Pattern: I kept adding "things Claude should surface" when Kay already has surfaces (Superhuman, Attio, sheets) for most of it. She wants the dashboard to do what no existing surface does (live ops view, activity rollup, system pulse) — not duplicate nagging. "This is starting to feel like noise right now."

**How to apply:**
- When scoping what goes on the dashboard, ask: "does Kay already see this elsewhere, and does adding it here make her MORE likely to act?" If she already sees it or it doesn't change behavior, leave it off.
- When a skill produces routine per-run activity counts, default them to health-monitor digest lines, not their own page/panel.
- Relationship-manager cadence: daily runs continue (data stays fresh) but output routes to a Friday-only review artifact, not the daily briefing. (Pending implementation — do not change mid-scoping-session per Kay's directive.)

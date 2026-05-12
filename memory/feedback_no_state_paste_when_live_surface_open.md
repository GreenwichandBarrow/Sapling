---
name: no-state-paste-when-live-surface-open
description: Don't echo back the state of a live-viewable surface (Sheet, dashboard, Drive doc) in chat after making changes. Kay sees the live file in her browser. Paste-back is redundant noise.
metadata:
  type: feedback
---

## Rule

When making changes to a surface Kay is actively viewing in her browser (Google Sheet, Streamlit dashboard, Drive doc, Attio record, etc.), confirm the action in one line and stop. **Do not paste back a table of the current state** — she can see it live.

- ✅ "Moved 4 items from Friday to Sunday."
- ❌ "Moved 4 items from Friday to Sunday. **Updated week-tab state:** | Slot | Task | ..."

## Why

Pasting back state is helpful when Kay is NOT looking at the surface (e.g., asking from her phone, or the surface isn't browser-accessible). Once she's bookmarked the Sheet and is watching it live (as of the 2026-05-12 Excel → Sheets migration), the paste is:
1. Decision-fatigue noise — adds words she has to scan
2. Redundant — she already sees it
3. Risk of drift — the chat paste can lag behind a manual edit she just made

Precipitating trace: 2026-05-12 — pasted week-tab state after every tracker mutation in the post-migration session. Kay corrected: "there is no need to paste in this chat where the tracker items have landed - I am in the file on my browser now and can see the changes live."

## How to apply

- **Tracker mutations (append, promote, schedule-to-day-slot, move, clear):** one-line confirmation only. e.g., "Moved 4 items to Sunday." or "Slot cleared." Don't echo the slot table.
- **Sheet/Doc edits she's watching:** one-line confirmation. Save the long-form state for when she explicitly asks "what's the current state?"
- **Open-items board still applies:** I CAN still surface pending decisions ("still need your YES/NO on X, Y, Z"). That's not state-paste; that's surfacing my outstanding asks.
- **Dashboard mutations:** confirm + maybe a "refresh to see" prompt. Don't enumerate what changed.
- **Exception**: when something fails or has unexpected results, surface the actual state so Kay can verify. This is the diagnostic case, not the routine case.

## Related

- `feedback_decision_fatigue_minimization` — every word should reduce, not add to, Kay's mental load
- `feedback_silent_mode_when_executing` — after plan approval, drop narration; one-line status between major steps
- `feedback_briefing_no_done_items` — same principle: only surface what needs action

## Heuristic

Before pasting a table or block of state: ask "is she actively viewing this surface?" If yes, drop the paste. One-line confirm. Move on.

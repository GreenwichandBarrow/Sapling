---
description: Resume session — load latest continuation file and summarize state
---

# /pickingback

New-session bookend. Kay opens a fresh terminal, types `/pickingback` (or natural "picking back up"), and the system loads the latest continuation file and summarizes so Kay can continue without re-explaining.

## Execute Now

### Step 1 — Find latest continuation file

Glob for `brain/context/continuation-*.md`, sorted descending by date and session number. Take the most recent.

If no continuation file exists within the last 48 hours → tell Kay: "No recent save state found — last continuation was {date or 'never'}. Proceeding fresh; you may want to run `/goodmorning` instead."

### Step 2 — Read and summarize

Read the continuation file. Extract:
- `## Active Threads` — what's in-flight
- `## Next Steps` — what's queued
- `## Open Questions` — what awaits Kay's decision

### Step 3 — Present 3-5 line summary

Format:
```
Picking back up from continuation #{N} ({date}, saved {time ago}).

Active threads:
1. {thread name} — {state}
2. {thread name} — {state}
...

Next up: {top priority item}
Open for you: {top open question if any}
```

### Step 4 — Stand by

After the summary, STOP. Do NOT:
- Re-run morning briefing
- Write a new continuation file
- Start executing on active threads without Kay's direction
- Re-ask questions already answered in the continuation

Wait for Kay's next instruction.

## Behaviors

- **Honor the continuation file as truth.** If it says a thread is pending Kay's send, don't re-draft it unprompted.
- **Never duplicate work the morning workflow already did.** If `/goodmorning` ran today and session-decisions already logged the day, the continuation is a layer ABOVE that — mid-day state, not morning briefing.
- **If Kay's first message after `/pickingback` is unrelated to the saved threads**, drop them gracefully and follow her lead. The continuation is a resource, not a mandate.
- **If continuation references external state (email thread, Attio record, tracker row)**, verify the state hasn't changed before acting on it. Stale continuation data is worse than no continuation.

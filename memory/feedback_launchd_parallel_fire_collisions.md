---
name: Diagnose simultaneous launchd "Unexpected" failures as parallel-fire collisions, not API issues
description: When two scheduled skills fail at the exact same minute with "An unknown error occurred (Unexpected)", first hypothesis is launchd parallel-fire resource contention — not API outage, not auth, not network
type: feedback
originSessionId: f14e8037-7d17-4534-81ac-ff28cad01442
---
When two or more scheduled mutating skills fail at the **exact same minute** with `error: An unknown error occurred (Unexpected)` on every retry attempt, the first hypothesis should be a **launchd parallel-fire collision** — not an API outage, not auth, not network.

**Why:** On 2026-04-28 23:04:52 ET, both `niche-intelligence` (Tuesday 23:00 plist) and `nightly-tracker-audit` (daily 23:00 plist) fired at the same second. Both ran 3 attempts × ~2 hours each = ~6 hours total, all attempts failed with the catch-all "Unexpected" error, exit 1, Slack alert at 05:19. I initially looked at the API/auth/wrapper-retry layer; the real cause was two heavyweight Opus calls simultaneously competing for memory/network/keychain on Kay's Mac. Each individually would have succeeded.

**How to apply:**
1. When a Slack failure alert names ≥2 skills with the same start timestamp (look at the `Started:` line in their respective `logs/scheduled/*.log` files), check `~/Library/LaunchAgents/com.greenwich-barrow.*.plist` for matching `<key>Hour</key> + <key>Minute</key>` blocks.
2. If two plists collide, stagger them by ≥30 min (60 min preferred for two heavyweight skills).
3. Convention: heavier skill earlier (gets the "first crack" at resources), Tuesday-only skill earlier than daily skill (so daily-fire days don't shift around).
4. Diagnostic shortcut: `grep -A 6 "StartCalendarInterval" ~/Library/LaunchAgents/com.greenwich-barrow.*.plist | grep -E "plist|Hour|Minute"` shows all schedules at a glance.
5. The wrapper retry on "Unexpected" doesn't help here — every attempt hits the same collision. Stagger is the fix, not more retries.

**Don't waste time on:** API status, auth re-verification, prompt-shrinking, retry-count bumps. Those address other failure modes. This one is purely a scheduling-conflict mode that the wrapper layer can't see.

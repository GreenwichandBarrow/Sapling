---
name: Verify infra state with live commands — don't trust CLAUDE.md / skills / memory as ground truth
description: Before stating an infrastructure fact that an operator might act on (job runs on X scheduler, costs $Y/mo, lives at path Z), run a verification command. Docs and skill text drift; reality is in `systemctl list-timers`, `ls`, `gh api`, sheet reads, etc.
type: feedback
---

When stating an infrastructure fact — what scheduler runs a job, what
something costs, where a process lives, whether a tool exists — derive the
fact from a **live verification command**, not from CLAUDE.md, a skill's
essential_principles block, or a memory file. Docs drift; reality is the
source of truth.

**Why:** Three errors in one session (2026-05-10 evening) all from the same
pattern of trusting stale doc over live reality:

1. **KeyReach cost.** Pulled "$1,500/mo" from budget-manager skill's
   `Key Financial Parameters` and recommended adding it to Tab 3 of the
   budget sheet. Kay corrected: KeyReach is free; covered by the existing
   DealsX fee. The skill's "DealsX KeyReach $1,500/mo" text was an
   ambiguous notation that I read as KeyReach=$1,500.
2. **Launchd vs systemd.** Claimed scheduling was still on Mac launchd
   based on CLAUDE.md's "Scheduled Skills (launchd)" section. Kay caught
   it: "I thought we already did that work." A `systemctl --user list-timers`
   would have shown 21 timers running on the VPS in ~3 seconds.
3. **"Mac launchd jobs may still exist"** language I wrote into the
   VPS-primary memory. Same family. Kay had already retired the
   post-call-analyzer plist; the memory I wrote was already wrong by the
   time it landed.

**How to apply:**

- **Before stating a cost in a budget context:** read the source artifact
  (current invoice email, vendor's settings page, the actual sheet row
  recording the cost). Don't pull from skill body text.
- **Before stating where a scheduled job runs:** `systemctl --user list-timers`
  on VPS. `launchctl list | grep greenwich-barrow` on Mac. Don't trust
  CLAUDE.md's scheduled-skills table without cross-checking.
- **Before claiming a tool/binary/MCP exists:** `command -v <tool>`,
  `ls ~/.claude.json | grep mcpServers`, or `ToolSearch` for deferred
  tools. Don't trust a skill that *says* it uses Tool X without checking
  Tool X is actually wired up.
- **Before stating a path / file presence:** `ls` it. Don't trust a memory
  that references a path from 3 weeks ago.
- **When the live command and the doc disagree:** the live command wins.
  Update the doc (or schedule it for the next CLAUDE.md trim batch) so the
  drift doesn't catch the next agent.

**The cost of the verify is bounded** — a few seconds of `systemctl` or
`ls`. **The cost of being wrong is correction-cost on Kay's plate**,
which is exactly what the rest of the system exists to minimize.

This pattern probably hardens into a stop hook eventually: before claiming
infra state in a Decision item or in user-visible output, the agent must
have run a verification command for the claim in the last N turns.
Capturing here first; the stop hook can graduate from this memory once
the pattern of repetition is documented across more sessions.

Source: 2026-05-10 evening session — three same-class errors in one
session that all resolved the same way (Kay corrects, agent verifies via
live command, lesson generalizes).

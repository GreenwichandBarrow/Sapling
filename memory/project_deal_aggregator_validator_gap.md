---
name: deal-aggregator validator gap (Phase 4.5 cleanup)
description: deal-aggregator (all 3 variants — main, --afternoon, --digest-mode) has no POST_RUN_CHECK validator. Pre-existing gap, deferred to Phase 4.5 cleanup batch. Three distinct ExecStart flags, not duplicates.
type: project
originSessionId: 245b9334-d58f-45df-8978-a6d8673c0ca7
---
`deal-aggregator` and its two variants (`-afternoon`, `-friday`) ship without `POST_RUN_CHECK` env vars in both launchd plists and systemd units. This violates CLAUDE.md `feedback_mutating_skill_hardening_pattern.md` ("EVERY launchd skill needs POST_RUN_CHECK validator + headless prompt + SKILL.md mandatory-validator section. Read-only skills get artifact-landed checks (lighter), NOT exempt").

**Why deferred:** Pre-existing gap — not introduced during the 2026-05-08 server migration. Adding the validator means writing `scripts/validate_deal_aggregator_integrity.py` + wiring through plist + regenerating systemd units, which expands tonight's MacBook-interchangeable scope. Tagged for Phase 4.5 cleanup batch alongside `post-call-analyzer` iMac sidecar retirement and any other "remaining unhardened skills" cleanup per the 2026-05-04 audit table.

**Three variants, three different functions** (NOT duplicates):

| Variant | Cadence | ExecStart flag | Purpose |
|---|---|---|---|
| `deal-aggregator` | Mon-Fri 06:00 ET | (none) | Default morning scan |
| `deal-aggregator-afternoon` | Mon-Fri 14:00 ET | `--afternoon` | Afternoon scan for mid-day broker blasts |
| `deal-aggregator-friday` | Fri 06:00 ET | `--digest-mode` | Weekly Friday digest |

**Friday 6am parallel-fire note:** `deal-aggregator` (Mon..Fri schedule includes Friday) and `deal-aggregator-friday` both fire at Fri 06:00. This is iMac launchd behavior preserved verbatim on systemd. Per `feedback_launchd_parallel_fire_collisions.md` parallel fires can collide — if cleanup batch sees Friday-morning failures, stagger the digest variant to 06:30 or move to a non-overlap window.

**How to apply:**
- When opening Phase 4.5 cleanup, add deal-aggregator validator as one of the gap items.
- Validator should be lighter (read-only skill — check artifact landed at expected path with non-empty content) per the doctrine for read-only skills.
- After writing the validator, re-add `POST_RUN_CHECK` env to all 3 plists, regenerate, scp updated `.service` files to server, daemon-reload. (The generator's whitespace fix from `project_systemd_env_quoting_fix.md` will handle the quoting correctly.)

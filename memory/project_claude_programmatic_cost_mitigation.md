---
name: claude-programmatic-cost-mitigation
description: "June 15 2026 Anthropic programmatic-billing change: scheduled fleet was ~$5k/mo on Opus. Sonnet model-routing shipped 5/30 (live in run-skill.sh); usage credits OFF as hard floor; re-measure due BEFORE 2026-06-15."
metadata:
  node_type: memory
  type: project
---

**Deadline: 2026-06-15.** Anthropic moves programmatic Claude usage (`claude -p` non-interactive, Agent SDK, GitHub Actions, cron) off the standard subscription onto a **separate metered credit pool, billed at full API rates** ($200/mo included on Max 20x, overage metered). Interactive terminal use and claude.ai chat are unaffected.

**The finding (30-day transcript analysis, 2026-04-29 → 05-29):** the scheduled-skill fleet was running **~$5,000/mo API-equivalent, ~99% on Opus**, because `scripts/run-skill.sh` passed no `--model` and every fire (plus its subagents, which inherit the parent model) defaulted to Opus. ~$3.5k of the $5k was cache-write churn (~1,400 short-lived runs each re-loading full context). Treat $5k as the do-nothing ceiling; the hard cron floor is comfortably $1k+/mo (some sdk-cli volume is interactive-session subagents with uncertain billing attribution).

**What shipped (2026-05-30, committed, live):**
- Model routing at the single chokepoint in `run-skill.sh`: scheduled jobs **default to Sonnet**; only **`calibration-workflow` + `niche-intelligence`** stay on **Opus** (`OPUS_SKILLS` allow-list); auth preflight dropped to **Haiku**. Per-unit override via `SKILL_MODEL` env. Subagents inherit parent model, so this routes the whole fan-out. Expected ~5x cut (~$5k → ~$1k/mo). Doctrine: `docs/scheduled-skills.md` "Model Routing (2026-05-30)".
- `post_call_analyzer_mcp_poll.py` (dead code since the 5/13 granola-api REST migration) pinned to Haiku defensively.

**Posture decisions:**
- **Usage credits left OFF** = hard floor. Jobs throttle when the included credit is spent rather than billing over. No surprise bill possible. Flip ON only as an end-state decision once the tuned number is confirmed.
- Do NOT bulk-buy discounted credits yet — size to a proven run-rate after re-measure.
- **deal-aggregator** (~$630/mo, 3 fires/day+wk) = prime downgrade target: most expensive, NOT a top-value skill per [[project-kay-skill-value-assessment]]. Cut frequency / drop to Sonnet / scope to email-only — evaluate on under-delivery, cost relief is the byproduct.
- **conference-discovery** (~$75/mo) = PROTECT from any cost-trimming (Kay's highest-value skill).
- Retirement is a *minor* cost lever (fleet is mostly reliable); model routing is the real saver.

**Status:** Harrison Wells coaching call #6 (2026-06-01) covered this — brief `brain/briefs/2026-06-01-harrison-wells-call-6.md`. Cost levers also feed the runway plan ([[traces/2026-06-02-runway-to-feb-2027-no-salary-cut]]).

**OPEN — re-measure before 2026-06-15:** re-run the same 30-day transcript analysis with ~2 weeks of Sonnet data to confirm the landing spot, a few days before the billing flip. (Scheduling was parked pending the Harrison call; call has happened — re-measure can now be scheduled.) Secondary: confirm exact new **Hetzner** rate + effective date (smaller magnitude).

**Related:** [[project-kay-skill-value-assessment]], [[project-dealsx-jj-windown-by-summer]].

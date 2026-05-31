---
schema_version: "1.0.0"
date: 2026-06-01
type: brief
title: "Coaching Call Prep: Harrison Wells (Call #6)"
people: ["[[entities/harrison-wells]]", "[[entities/kay-schneider]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags:
  - date/2026-06-01
  - brief
  - person/harrison-wells
  - person/kay-schneider
  - company/dodo-digital
  - company/greenwich-and-barrow
  - topic/ai-coaching
  - topic/claude-infrastructure
  - topic/cost-optimization
  - topic/model-routing
  - topic/scheduled-skills
  - source/claude
---

# Coaching Call Prep: Harrison Wells (Call #6)
Monday 2026-06-01, 10:00-11:00am ET
Format: G&B pre-circulates challenges list; Harrison comes with concrete recommendations.

**Priority this call:** adjusting the setup to absorb the **June 15 cost increase** before it lands. The skills working/failing inventory below exists to drive that decision — what to protect, what to downgrade, what to cut.

---

## The June 15 Cost Event (lead item)

Two cost changes both effective ~June 15. The bigger one is not Hetzner.

1. **Anthropic programmatic-billing change (dominant).** Effective **2026-06-15**, programmatic Claude usage (`claude -p` non-interactive, Agent SDK, GitHub Actions) moves off the standard subscription onto a **separate metered credit pool, billed at full API rates** ($200/mo included on Max 20x, overage metered). Interactive terminal use is unaffected. A 30-day transcript analysis (4/29–5/29) measured the **scheduled fleet at ~$5,000/mo API-equivalent**, ~99% on Opus, because the wrapper passed no `--model` and every fire (plus its subagents) inherited the Opus default.
2. **Hetzner price-change notice (secondary).** Hetzner sent a price-adjustment email (captured in email scans 5/28–5/29). Need to confirm the exact new monthly rate + effective date — far smaller magnitude than the Anthropic change.

**Mitigation already drafted (not yet shipped):** route scheduled jobs to **Sonnet** by default; keep only genuinely reasoning-heavy jobs on **Opus** (`calibration-workflow`, `niche-intelligence`); auth preflight on **Haiku**. `scripts/run-skill.sh` is the single chokepoint — it routes the whole fan-out. Expected effect ~5x reduction (~$5k → ~$1k/mo) before any frequency/consolidation work.

---

## Relationship Arc

- **2026-03-05 → 04-30** — Sessions #1–#4. Architecture, sub-agent patterns, learnings.md concept, Hetzner/Tailscale server setup. Engagement locked 4/30: **$1,200/mo, up to 2 hrs 1:1 + async, Stripe monthly, renews on the 1st.**
- **2026-05-15** — Call #5. Agenda: Granola MCP PKCE re-auth on headless server; Family Office personal-project architecture (repo-level vs project-level split); validator-design pattern for the conference-discovery corruption regression; two outstanding email asks ("Ask Harrison" MCP install + secure-API-key tool name).
- **Since 5/15:**
  - **Granola RECOVERED** — REST wrapper (`granola-api`) authenticates via public-api.granola.ai; fresh notes landing through 5/28; cleared the 7-day stall that had silently blocked post-call-analyzer. (This was Call #5's #1 issue — now closed.)
  - **Model-routing policy drafted (5/30)** in response to the June 15 billing change — see lead item.
  - **target-discovery Phase 2 validator scoped to `--pool-only` (5/31)** — stops ~192 false "missing tab" failures every Sunday.
  - **DealsX + JJ wind-down in motion** (30-day notice this week, end ~late June) — a deliberate cost lever, see [[project_dealsx_jj_windown_by_summer]].

---

## Current Engagement Stage

- **Engagement:** Active, month-to-month, $1,200/mo (Stripe), renews on the 1st.
- **Format:** G&B pre-circulates this challenges list; Harrison comes with concrete recommendations. Don't let the call drift into discovery mode.
- **Outstanding from 4/30/5/15:** "Ask Harrison" MCP install email + secure-API-key tool name — still not received. Surface live (low priority now that 1P CLI is the chosen route).

---

## Skills Working Well

Weighted by **G&B's value judgment**, not just clean logs (per [[project_kay_skill_value_assessment]] — "reliable" ≠ "valuable").

| Skill | Why it's working | Cost posture |
|---|---|---|
| **conference-discovery** | **G&B's highest-value skill.** In-person conferences = highest-ROI channel. Hardened after the 5/03 incident (pre-run snapshot + row-count-delta validator). Runs clean. | **Cheap (~$75/mo). PROTECT — do not cut or degrade.** |
| **email-intelligence** | Daily 7am artifact landing reliably (scans present 5/28–5/31); feeds deal-flow classification + the morning briefing. | Sonnet-appropriate (scanning/classification). |
| **relationship-manager** | Nurture/overdue surfacing; artifacts landing; one of 6 hardened mutating skills with its own integrity validator. | Sonnet-appropriate. |
| **jj-operations** | Sunday tab creation + pool artifact landing (week pool 5/31 present). Note: winding down by summer regardless. | Sonnet-appropriate; sunsetting. |
| **Snapshot refreshers** (attio / jj / apollo) | Keep the Command Center dashboard live; cheap hourly jobs; clean except a one-off 5/10 attio auth blip. | Cheap; low model need. |
| **Granola → post-call-analyzer** | **Recovered since 5/15** via the REST wrapper; per-call analysis + Attio notes flowing again. | Sonnet-appropriate. |

**Infra baseline (5/29 health report):** 21/21 systemd timers GREEN, **zero non-zero exits in 7 days.** The fleet is currently stable.

---

## Skills That Keep Failing

Two buckets: recurring code/validator offenders (mostly patched), and persistent un-actioned work (the real open REDs).

### A. Recurring offenders (historical, mostly patched)
| Skill | Failure pattern | Status |
|---|---|---|
| **launchd-debugger** | Self-bug — repeatedly tripped its own validator (CODE_BUG / `validator_failed`) on 5/08, 5/13–5/17. The watchdog watching the watchdog. | Needs a real fix; the thing that's supposed to catch silent failures has itself been the most frequent failer. **Question for Harrison.** |
| **target-discovery (Phase 2, Sun)** | VALIDATOR_REJECT five Sundays running (5/04, 5/11, 5/18, 5/25) — false-positive "missing Call Log tab" because the validator walked tabs that don't exist until 6pm. | **Patched 5/31** (`--pool-only` scope). Watch next 2 Sundays to confirm. |
| **nightly-tracker-audit** | CODE_BUG 5/09, 5/16. | Intermittent; needs a durable fix. |
| **deal-aggregator** | VALIDATOR FAILED / CODE_BUG 5/12. **20/20 reliable since, BUT it is the single most expensive job (~$630/mo) and NOT a top-value skill in G&B's view** — surfaces little that gets acted on. | **Prime downgrade target: cut frequency, drop to Sonnet (or Haiku for the scan pass), or scope down.** See [[project_kay_skill_value_assessment]]. |
| **attio-snapshot-refresh** | AUTH failure 5/10. | One-off; resolved. |

### B. Persistent open REDs (un-actioned work, not crashes)
- **Stale-pipeline triage** — 10 of 11 deals stale (>14d), 9 RED (>21d); close-out RECOMMENDs un-actioned for 3+ weeks. *(G&B's action queue, not an infra fault.)*
- **Orphaned entity links** — 102 orphans, degrading 3rd straight week; backfill never ran.
- **MEMORY.md size** — crossed the load-truncation threshold (~224 lines / 66KB); needs a consolidation pass.
- **Apollo credits visibility** — API-key tier doesn't expose monthly balance; only minute headroom. (Vendor limitation.)
- **vault-entity-sync check** — spec bug: no People-scoped snapshot exists, so the check can't compute. Carried.

---

## The Cost-Adjustment Decision Menu (what I want Harrison's read on)

1. **Is Sonnet-default routing the right primary lever, or is there a structural move I'm missing?** (e.g., consolidating overlapping jobs, dropping fire frequency, batching, or moving read-only scans off `claude -p` entirely to a scripted API call.) Goal: land the ~$5k → ~$1k, then push lower.
2. **deal-aggregator** — highest cost / not-highest value. Cut frequency (daily → 2-3x/wk)? Drop to Sonnet/Haiku? Scope to email-only? What does Harrison see at other clients running daily scanning jobs?
3. **Re-measure method** — how to verify the post-routing spend before June 15? Re-run the 30-day transcript analysis, or is there a cleaner per-job cost meter to instrument?
4. **launchd-debugger reliability** — the watchdog is the most frequent failer. Redesign, or replace with a simpler exit-code + artifact-landed check?
5. **Hetzner** — confirm the new rate; is the current VPS sizing right, or is there a cheaper tier that still runs the 24/7 timers?

---

## What to Push For (this call)

1. A **concrete pre-June-15 cost plan** with a verified projected number, not a discussion.
2. A **verdict on deal-aggregator** — downgrade shape (frequency vs model vs scope).
3. A **re-measurement method** to confirm the landing spot before billing flips.
4. **launchd-debugger** redesign direction.

---

## What to Share About G&B Since 5/15

Light context only:
- Granola pipeline recovered; post-call-analyzer flowing again.
- Model-routing cost policy drafted in response to the June 15 billing change.
- DealsX + JJ wind-down underway (cost + focus lever) — moving to a leaner G&B + analyst methodology by summer.

## What NOT to Over-Share

- Pipeline-specific deal names (Harrison is infra coach, not deal partner).
- LP/investor-update specifics.
- Family Office personal-life logistics beyond any architecture question.

---

## Logistics

- **Source of truth:** [[entities/harrison-wells]]; prior brief `brain/briefs/2026-05-15-harrison-wells-call-5.md`; cost doctrine in `docs/scheduled-skills.md` (Model Routing 2026-05-30); value lens [[project_kay_skill_value_assessment]]; reliability data in `brain/trackers/health/2026-05-29-health.md` + `brain/trackers/health/launchd-debugger-*.json`.
- **Calendar:** Harrison coaching call, 2026-06-01 10:00–11:00am ET, harrison@dododigital.ai. (Eric Mendelsohn / Archveo follows at 11am — separate brief already prepped.)
- **Granola call ID:** assigned post-call via post-call-analyzer (now recovered).

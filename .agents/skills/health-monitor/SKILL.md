---
name: health-monitor
description: System-wide health monitoring with specialized sub-agents. Detects disconnected services, usage limits, missed triggers, pipeline hygiene issues, data integrity problems, and stale data.
archetype: orchestrator
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
trigger: Scheduled Friday 12:30 AM ET via Codex/systemd user timer (`health-monitor.timer`). Output ready for Friday morning briefing alongside weekly-tracker. Also runs on-demand via /health-check.
schedule: Friday 12:30 AM ET
---

<objective>
Detect silent failures before they become lost deals or broken workflows. Every issue found in production this month (deal-aggregator failing silently, Project Restoration skipping stages, E&K deal untracked, Gmail draft routing failures) would have been caught by this skill.
</objective>

<credentials>
## Credentials (read first)

**1Password is the first rung — always.** Before any op://-backed CLI or REST call:
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```
Exports `ATTIO_API_KEY`, `APOLLO_API_KEY`, `GRANOLA_KEY`, `GOG_KEYRING_PASSWORD`, `SLACK_WEBHOOK_*`. **NEVER `source scripts/.env.launchd` raw** — legacy file with unresolved references; see `feedback_op_env_before_op_backed_cli`.

**REST is the default health-check transport, MCP is a convenience.** A health-monitor check that calls `mcp__granola__list_meetings` or any `mcp__attio__*` tool MUST treat "MCP not loaded" as a session-state issue, NOT a service outage. Use REST to verify the underlying service before flagging RED:
```bash
# Attio
curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $ATTIO_API_KEY" https://api.attio.com/v2/self
# Apollo
curl -s -o /dev/null -w "%{http_code}\n" -H "X-Api-Key: $APOLLO_API_KEY" https://api.apollo.io/api/v1/auth/health
# Granola (use the wrapper — resolves op:// on every call)
~/.local/bin/granola-api latest >/dev/null && echo 200 || echo down
```

**Forbidden in the health dashboard:** marking a service RED because `mcp__*` returned "not connected" without first running the REST health-check above. Phantom outages corrupt the Friday morning briefing.
</credentials>

<essential_principles>
## Architecture

4 specialized sub-agents run in parallel, each owning a domain of the system. The orchestrator aggregates results into a dashboard with green/yellow/red status per check.

### Sub-Agent 1: Service Connectivity Agent
Tests every external API and integration. Each check: can we authenticate and get a valid response?

| Service | Check | Method | GREEN | YELLOW | RED |
|---------|-------|--------|-------|--------|-----|
| Attio | API key valid, can query | `POST /v2/objects/companies/records/query` with `{"limit":1}` | 200 OK | — | Non-200 or timeout |
| Apollo | API key valid | `POST /organizations/search` | 200 OK | — | Non-200 or timeout |
| Task tracker | To Do tab readable on current week's sheet | `SHEET_ID=$(python3 /home/ubuntu/projects/Sapling/scripts/tracker_sheet_resolver.py --print-id) && gog sheets get "$SHEET_ID" "'To Do'!A1" -j` | Returns data | — | Auth error, timeout, or resolver failure |
| Gmail (gog) | OAuth valid | `gog gmail search "newer_than:1d" --max 1 --json` | Returns results | — | Auth error or empty |
| Calendar (gog) | OAuth valid | `gog calendar list --from today --to today --json` | Returns data | — | Auth error |
| Drive (gog) | OAuth valid | `gog drive ls --parent root --json --max 1` | Returns data | — | Auth error |
| Sheets (gog) | Can read tracker | `gog sheets get {TRACKER_ID} "'WEEKLY REVIEW'!A1" -j` | Returns data | — | Auth error |
| Granola | REST responding (NOT MCP) | `~/.local/bin/granola-api latest` after `source scripts/op-env.sh` | Returns data | — | Non-200 from public-api.granola.ai (NOT "MCP not loaded") |

### Sub-Agent 2: Infrastructure Agent
Checks scheduled jobs, usage limits, and webhook health.

**Scheduled Jobs:**
Expected jobs (this list is the source of truth — must match `AGENTS.md` and
`docs/scheduled-skills.md`; missing systemd timer for any skill here = RED):
- `deal-aggregator.timer` (Mon-Fri 7:30am ET)
- `email-intelligence.timer` (Mon-Fri 7am ET)
- `cold-call-snapshot-refresh.timer` (Mon-Fri 9am ET) — feeds dashboard cold-call activity
- `niche-intelligence.timer` (Tue 10:30pm ET)
- `nightly-tracker-audit.timer` (Nightly 11:30pm ET)
- `conference-discovery.timer` (Sun 9pm ET)
- `health-monitor.timer` (Fri 12:30am ET)
- `launchd-debugger.timer` (Daily 8:20am ET after email-intelligence/deal-aggregator; legacy name, systemd runner)
- `calibration-workflow.timer` (Thu 11pm ET)
- `attio-snapshot-refresh.timer` (Mon-Fri 8am ET) — feeds dashboard's landing hero, Active Deal Pipeline, M&A Analytics deal-flow KPIs
- `apollo-credits-refresh.timer` (Mon-Fri 8am ET)
- `external-services-probe.timer` (Mon-Fri 8am ET)
- `post-call-analyzer-poll.timer` (Daily 1pm + 6pm ET)
- `weekly-snapshot.timer` (Fri 10pm ET)
- `weekly-archive-export.timer` (Sat 9am ET)

**Intentionally on-demand / disabled timers (do not flag RED):**
Kay confirmed on 2026-07-17 that Cold Call Operations Sunday prep and Phase 2 target discovery should be treated as on-demand workflows unless she explicitly reactivates them. The canonical cold-call workflow name is Cold Call Operations; `jj-operations-sunday.timer` is a legacy installed alias only. `cold-call-operations-sunday.timer`, `jj-operations-sunday.timer`, and `target-discovery-sunday.timer` may be disabled/inactive without appearing in Slack health alerts or morning System Health as scheduled-skill failures.

For each:
```bash
systemctl --user list-timers --all
systemctl --user status {timer-or-service} --no-pager
```
- GREEN: exit code 0, ran within expected schedule
- YELLOW: exit code 0 but last run > 2x expected interval; OR single non-zero exit in last 7 days
- RED: non-zero exit code (like 126 = permission error); OR 2+ consecutive failed runs; OR missing systemd timer for a skill listed in `AGENTS.md` / `docs/scheduled-skills.md`

**Consecutive-failure escalation (critical):**
Slack notifies on individual fails, but repeated failures get lost in the noise. For each scheduled skill, grep the last 7 days of logs for `exit: [1-9]` — if 2+ consecutive runs failed, surface as RED in the morning briefing with the skill name, fail count, and error excerpt. Do not wait for a third fail or for Kay to notice the Slack pattern.

**Timer coverage audit:**
Cross-reference `systemctl --user list-timers --all` against `AGENTS.md` and `docs/scheduled-skills.md`. Any scheduled skill listed there but missing from systemd = RED (never deployed or silently disabled).

On RED: tail the last 50 lines of the log file for error context:
```bash
tail -50 logs/scheduled/{skill}-{date}.log
```

**Usage Limits:**
| Resource | Check | YELLOW | RED |
|----------|-------|--------|-----|
| Apollo credits | Track email reveals consumed | < 500 remaining | < 100 remaining |
| Apollo subscription | Basic plan $64/mo, auto-renews | — | Payment failed |
| DealsX shared sheet | Accessible and updated within 7 days | — | Not updated in 7+ days (activate when DealsX confirmed) |

**Webhook Health:**
Read the last health report from `brain/trackers/health/` to check prior Slack webhook status. Do NOT re-test webhooks every run (per Kay's feedback: one test per setup). Only re-test if prior report showed a failure.

### Sub-Agent 3: Pipeline Hygiene Agent
Catches deals that fall through the cracks.

**Stage Skipping Detection:**
For every Active Deals entry, check if stages were skipped. Expected progression:
```
Identified → Contacted → First Conversation → NDA Executed → Financials Received → Active Diligence → LOI Submitted → LOI Signed
```

Flag if an entry jumped forward by 2+ stages (e.g., Identified → Closed, or Identified → Financials Received without NDA Executed). Check `active_from` timestamps on each stage.

- RED: Any entry that went to Closed skipping NDA or Financials stages that Gmail shows actually happened
- YELLOW: Any entry that skipped 1 intermediate stage

**Untracked Deal Detection:**
Cross-reference Gmail deal flow (NDA attachments, CIM attachments, broker correspondence) against Attio Active Deals. Flag a missing active deal only when the email identifies an underlying selling company/opportunity that should be in the pipeline.

Do NOT flag broker/source organizations themselves as missing active deals. Everingham & Kerr, Transworld, BizBuySell, BizQuest, Baton, and similar senders are deal-flow sources unless a specific underlying company/listing has been promoted into the active pipeline. For Everingham & Kerr specifically, treat the source company as a broker/source relationship; Joe Varone is the contact. Health should ask whether a specific E&K listing should be tracked, not say "Everingham & Kerr is missing from Attio" as if E&K were the target company.

```bash
# Find NDA/CIM/deal-package signals in last 14 days
gog gmail search "(NDA OR confidential information memorandum OR CIM) newer_than:14d" --json --max 20
```
For each signal, extract the underlying company/listing name first. If there is no specific underlying company/listing, route it to source coverage or relationship-manager instead of Active Deals. Missing underlying company = RED only after source-vs-target attribution is clear.

**Stale Entry Detection:**
- YELLOW: Entry in same stage > 14 days with no email or calendar activity
- RED: Entry in same stage > 21 days with no activity
- Text-first exception: if the company/person entity, pipeline note, or Kay's latest session context says the live channel is text/phone and the owner lacks or does not use email, do NOT mark RED solely because Gmail/calendar are quiet. Surface as YELLOW `manual text-status check needed` unless Kay has already provided a current text update in the same day/week context.

**Outreach Deliverability:**
- Bounce rate: Count bounced emails over 7 days vs total sent. YELLOW at 2%, RED at 3%.
- Reply rate: Track weekly trend. YELLOW if declining 2+ consecutive weeks.
- Method: For Kay Email niches, scan Gmail sent folder for bounces and replies. For DealsX niches, check Sam's shared sheet for response data.

**Missing Vault Entities:**
For each Attio Active Deals entry, check if a corresponding `brain/entities/{slug}.md` exists. Missing = YELLOW.

**Attio vs Gmail Signal Mismatch:**
Search Gmail for NDA/CIM signals for entries still at Identified or Contacted in Attio. If Gmail shows an NDA was signed but Attio shows Identified, flag RED: "Attio stage behind reality."

### Sub-Agent 4: Data Integrity Agent
Checks vault health and data freshness.

**Schema Validation:**
```bash
# Run the vault validation on recent files
python3 .codex/hooks/router/pre_tool_use.py --check brain/calls/*.md brain/entities/*.md 2>&1
```
Or spot-check the 10 most recently modified vault files for schema compliance.

**Orphaned Entities:**
Before counting orphaned real-contact links, run the Attio -> Vault backfill so Attio contacts get matching vault entity files instead of being reported as hygiene failures:
```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
python3 scripts/backfill_vault_entities_from_attio.py
```

Then count normalized unique missing entity slugs. Normalize before counting aliases; do not count each display-text variant as a separate orphan. Exclude historical health reports, rollback snapshots, and template/example placeholders; those are not live relationship data and should not create Slack red alerts. Only valid entity slugs count as real orphan candidates.
```bash
python3 - <<'PY'
from pathlib import Path
import re
brain = Path('brain')
pattern = re.compile(r'\[\[entities/([^\]\|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
valid_slug = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
missing = set()
for path in brain.rglob('*.md'):
    rel = path.relative_to(brain)
    if rel.parts[:2] == ('trackers', 'health'):
        continue
    if rel.parts[:2] == ('context', 'rollback-snapshots'):
        continue
    text = path.read_text(errors='ignore')
    for match in pattern.finditer(text):
        slug = match.group(1).strip().rstrip('\\')
        if not valid_slug.fullmatch(slug):
            continue
        if not (brain / 'entities' / f'{slug}.md').exists():
            missing.add(slug)
for slug in sorted(missing):
    print(f'MISSING: {slug}')
PY
```
- YELLOW: 1-3 normalized unique orphaned slugs
- RED: 4+ normalized unique orphaned slugs

**Data Freshness:**
| Data | Check | YELLOW | RED |
|------|-------|--------|-----|
| Email scan results | `brain/context/email-scan-results-{today}.md` exists | Missing today's | Missing 2+ days |
| Weekly tracker | Last column date in sheet | Not updated this Friday | Not updated in 2+ weeks |
| Granola ingestion | Most recent `brain/calls/` file date | > 3 days since last meeting | > 7 days |
| Vault entity sync | Compare Attio People count vs vault entity count | Drift > 20% | Drift > 50% |
| Attio dashboard snapshot | `fetched_at` in `brain/context/attio-pipeline-snapshot.json` | > 4h during business hours OR > 60h overall | > 12h during business hours OR > 80h overall |
| Cold-call dashboard snapshot | `fetched_at` in `brain/context/jj-activity-snapshot.json` | > 30h during business hours OR > 72h overall | > 48h during business hours OR > 96h overall |

The dashboard's `data_sources.check_dashboard_staleness()` does the same
check live against a 2h/30h threshold (during business hours) and surfaces
a yellow banner above every page. Health-monitor's threshold is more
permissive — it only flags genuinely-broken refresh jobs, not the
expected hourly gap between runs.

## Execution Flow

### Step 1: Launch all 4 sub-agents in parallel
```
Agent 1: Service Connectivity (background)
Agent 2: Infrastructure (background)
Agent 3: Pipeline Hygiene (background)
Agent 4: Data Integrity (background)
```

### Step 2: Aggregate results
Merge all sub-agent reports. Calculate overall system status:
- **ALL GREEN** → system healthy
- **Any YELLOW** → warning, include in dashboard
- **Any RED** → visible in health report, dashboard, and Good Morning. Do not send Slack for health-monitor findings unless Kay explicitly re-enables health Slack alerts.

### Step 3: Write dashboard to vault
Save to `brain/trackers/health/{YYYY-MM-DD}-health.md`:

```yaml
---
schema_version: "1.0.0"
date: {YYYY-MM-DD}
type: tracker
title: "System Health — {date}"
tags: ["date/{YYYY-MM-DD}", "output", "output/tracker", "topic/health-monitor", "source/codex"]
---
```

Dashboard format:
```
# System Health — {date}

## Overall: {GREEN / YELLOW / RED}

### Service Connectivity
| Service | Status | Detail |
|---------|--------|--------|
| Attio | GREEN | API responding, 54 Active Deals entries |
| Apollo | YELLOW | 487 credits remaining (< 500 threshold) |
| ... | ... | ... |

### Infrastructure
| Component | Status | Detail |
|-----------|--------|--------|
| deal-aggregator | RED | Exit code 126, permission error since 3/23 |
| ... | ... | ... |

### Pipeline Hygiene
| Check | Status | Detail |
|-------|--------|--------|
| Stage skipping | RED | 2 entries skipped stages (Project Restoration, E&K SaaS) |
| ... | ... | ... |

### Data Integrity
| Check | Status | Detail |
|-------|--------|--------|
| Schema validation | GREEN | All recent files pass |
| ... | ... | ... |

## Action Items
1. [RED] Fix deal-aggregator scheduler permissions
2. [RED] Backfill skipped stages for Project Restoration and E&K SaaS
3. [YELLOW] Apollo credits at 487 — monitor consumption
```

### Step 4: Trend comparison
If a prior health report exists, compare:
- New REDs since last check (escalate)
- REDs that were fixed (acknowledge)
- Persistent YELLOWs becoming RED (flag degradation)

### Step 5: Notify

As of 2026-08-07, Kay does not want Slack messages for health-monitor YELLOW/RED findings because Slack reads as urgent and false positives create noise. Keep health monitoring active, but route findings to:

- `brain/trackers/health/{date}-health.md`
- dashboard System Health
- Good Morning System Health / broken-system section when Kay needs to know

Do not post health-monitor status to `#operations` unless Kay explicitly re-enables `HEALTH_MONITOR_SLACK_BRIDGE=1` or asks for a one-off Slack alert.

Legacy Slack payload, now opt-in only:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H "Content-Type: application/json" \
  -d '{"text":"System Health: {STATUS}\n{n} RED | {n} YELLOW | {n} GREEN\nTop issues:\n- {issue 1}\n- {issue 2}\nFull report: brain/trackers/health/{date}-health.md"}'
```

If ALL GREEN, no Slack notification. Silence = healthy.

## Schedule

- **Friday mornings:** Runs alongside weekly-tracker during the "good morning" flow
- **On-demand:** `/health-check` for immediate status
- **After any skill deployment:** Run to verify nothing broke

## What This Would Have Caught

| Incident | Check | How |
|----------|-------|-----|
| deal-aggregator exit 126 | Infrastructure → scheduler | Non-zero exit code flagged RED |
| Project Restoration skipped stages | Pipeline Hygiene → stage skipping | Identified → Closed without NDA/Financials |
| E&K listing attribution | Pipeline Hygiene → untracked deals | Health must distinguish broker/source company Everingham & Kerr + contact Joe Varone from the underlying selling company before flagging Attio mismatch |
| Weekly tracker missed deal activity | Data Integrity → freshness | Attio stage changes not reflected in tracker |
</essential_principles>

<success_criteria>
## Success Criteria

- [ ] All 4 sub-agents returned results (no silent failures)
- [ ] Dashboard written to `brain/trackers/health/{date}-health.md`
- [ ] Every RED has a specific action item
- [ ] No Slack notification for health-monitor YELLOW or RED findings unless Kay explicitly re-enabled it
- [ ] No Slack notification if all GREEN
- [ ] Trend comparison against prior report (if exists)
</success_criteria>

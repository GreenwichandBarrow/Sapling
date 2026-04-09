---
name: health-monitor
description: System-wide health monitoring with specialized sub-agents. Detects disconnected services, usage limits, missed triggers, pipeline hygiene issues, data integrity problems, and stale data.
trigger: Friday morning (alongside weekly-tracker) or on-demand via /health-check
---

<objective>
Detect silent failures before they become lost deals or broken workflows. Every issue found in production this month (deal-aggregator failing silently, Project Restoration skipping stages, E&K deal untracked, Superhuman drafts routing to Gmail) would have been caught by this skill.
</objective>

<essential_principles>
## Architecture

4 specialized sub-agents run in parallel, each owning a domain of the system. The orchestrator aggregates results into a dashboard with green/yellow/red status per check.

### Sub-Agent 1: Service Connectivity Agent
Tests every external API and integration. Each check: can we authenticate and get a valid response?

| Service | Check | Method | GREEN | YELLOW | RED |
|---------|-------|--------|-------|--------|-----|
| Attio | API key valid, can query | `POST /v2/objects/companies/records/query` with `{"limit":1}` | 200 OK | — | Non-200 or timeout |
| Apollo | API key valid | `POST /organizations/search` | 200 OK | — | Non-200 or timeout |
| Motion | API key valid | `GET /tasks?limit=1` | 200 OK | — | Non-200 or timeout |
| Gmail (gog) | OAuth valid | `gog gmail search "newer_than:1d" --max 1 --json` | Returns results | — | Auth error or empty |
| Calendar (gog) | OAuth valid | `gog calendar list --from today --to today --json` | Returns data | — | Auth error |
| Drive (gog) | OAuth valid | `gog drive ls --parent root --json --max 1` | Returns data | — | Auth error |
| Sheets (gog) | Can read tracker | `gog sheets get {TRACKER_ID} "'Weekly Topline'!A1" -j` | Returns data | — | Auth error |
| Granola | MCP responding | `mcp__granola__list_meetings` | Returns data | — | Error or timeout |
| Superhuman | Token fresh, draft path works | Check `~/.local/bin/superhuman-draft.sh` exists + LaunchAgent running | Both present | Script exists, agent not running | Script missing |

### Sub-Agent 2: Infrastructure Agent
Checks scheduled jobs, usage limits, and webhook health.

**Launchd Jobs:**
Expected jobs:
- `com.greenwich-barrow.deal-aggregator` (Mon-Fri 6am)
- `com.greenwich-barrow.niche-intelligence` (Tue 11pm)

For each:
```bash
launchctl list | grep greenwich
```
- GREEN: exit code 0, ran within expected schedule
- YELLOW: exit code 0 but last run > 2x expected interval
- RED: non-zero exit code (like 126 = permission error)

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
Cross-reference Gmail deal flow (NDA attachments, CIM attachments, broker correspondence) against Attio Active Deals. Flag any deal with email activity but no Attio entry.

```bash
# Find NDA-related emails in last 14 days
gog gmail search "(NDA OR confidential information memorandum OR CIM) newer_than:14d" --json --max 20
```
For each, check if the company/contact has an Attio Active Deals entry. Missing = RED.

**Stale Entry Detection:**
- YELLOW: Entry in same stage > 14 days with no email or calendar activity
- RED: Entry in same stage > 21 days with no activity

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
python3 .claude/hooks/router/pre_tool_use.py --check brain/calls/*.md brain/entities/*.md 2>&1
```
Or spot-check the 10 most recently modified vault files for schema compliance.

**Orphaned Entities:**
Check for vault entities referenced in call notes or other files that don't exist:
```bash
grep -roh '\[\[entities/[^]]*\]\]' brain/ | sort -u | while read link; do
  slug=$(echo "$link" | sed 's/\[\[entities\///;s/\]\]//;s/|.*//')
  [ ! -f "brain/entities/${slug}.md" ] && echo "MISSING: $slug"
done
```
- YELLOW: 1-3 orphaned links
- RED: 4+ orphaned links

**Data Freshness:**
| Data | Check | YELLOW | RED |
|------|-------|--------|-----|
| Email scan results | `brain/context/email-scan-results-{today}.md` exists | Missing today's | Missing 2+ days |
| Weekly tracker | Last column date in sheet | Not updated this Friday | Not updated in 2+ weeks |
| Granola ingestion | Most recent `brain/calls/` file date | > 3 days since last meeting | > 7 days |
| Vault entity sync | Compare Attio People count vs vault entity count | Drift > 20% | Drift > 50% |

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
- **Any RED** → alert, Slack notification required

### Step 3: Write dashboard to vault
Save to `brain/trackers/health/{YYYY-MM-DD}-health.md`:

```yaml
---
schema_version: "1.0.0"
date: {YYYY-MM-DD}
type: tracker
title: "System Health — {date}"
tags: ["date/{YYYY-MM-DD}", "output", "output/tracker", "topic/health-monitor", "source/claude"]
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
1. [RED] Fix deal-aggregator launchd permissions
2. [RED] Backfill skipped stages for Project Restoration and E&K SaaS
3. [YELLOW] Apollo credits at 487 — monitor consumption
```

### Step 4: Trend comparison
If a prior health report exists, compare:
- New REDs since last check (escalate)
- REDs that were fixed (acknowledge)
- Persistent YELLOWs becoming RED (flag degradation)

### Step 5: Notify (only if YELLOW or RED)
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
| deal-aggregator exit 126 | Infrastructure → launchd | Non-zero exit code flagged RED |
| Project Restoration skipped stages | Pipeline Hygiene → stage skipping | Identified → Closed without NDA/Financials |
| E&K deal not in Attio | Pipeline Hygiene → untracked deals | Gmail NDA/CIM signals with no Attio entry |
| Superhuman draft → Gmail | Service Connectivity → Superhuman | LaunchAgent not running or script missing |
| Weekly tracker missed deal activity | Data Integrity → freshness | Attio stage changes not reflected in tracker |
</essential_principles>

<success_criteria>
## Success Criteria

- [ ] All 4 sub-agents returned results (no silent failures)
- [ ] Dashboard written to `brain/trackers/health/{date}-health.md`
- [ ] Every RED has a specific action item
- [ ] Slack notification sent if any YELLOW or RED
- [ ] No Slack notification if all GREEN
- [ ] Trend comparison against prior report (if exists)
</success_criteria>

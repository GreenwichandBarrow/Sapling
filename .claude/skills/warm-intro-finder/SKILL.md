---
name: warm-intro-finder
description: "Mine Kay's network for warm intro paths to acquisition targets. Checks Attio, vault, Gmail, and LinkedIn for connections. Tags targets with intro availability and surfaces pathways."
user_invocable: true
context_budget:
  skill_md: 1500
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Find warm paths to cold targets. That's it.

For every new acquisition target, this skill checks whether Kay already knows someone who can make an introduction. Warm intros dramatically outperform cold outreach — the learnings confirm: "River guides are the silver bullet."

**Two modes:**
1. **Inline** — called by target-discovery after new targets are added to the sheet. Runs per-target, appends intro data to existing row.
2. **Batch** — invoked manually via `/warm-intro-finder` on an entire niche target list. Scans all targets missing intro data.

**Output:** For each target, writes to the target sheet:
- Col: Intro Path (warm / investor intro / cold)
- Col: Intro Contact (name + relationship context)

**This skill does NOT:**
- Create outreach drafts (that's outreach-manager)
- Manage relationships (that's relationship-manager)
- Discover new targets (that's target-discovery)
</objective>

<sources>
## Network Sources (checked in priority order)

### 0. LinkedIn Connections — Kay's Full Network (FASTEST CHECK)
```bash
# Search Kay's 901 LinkedIn connections by company name or person name
grep -i "{company_name}" archives/linkedin/connections.csv
grep -i "{owner_last_name}" archives/linkedin/connections.csv
```

**File:** `archives/linkedin/connections.csv` (exported 2026-03-23, 901 connections)
**Columns:** First Name, Last Name, URL, Email Address, Company, Position, Connected On

What to look for:
- Is the target owner a direct LinkedIn connection? (search by last name)
- Does Kay have a connection at the target company? (search by company name)
- Does Kay have a connection at a company in the same niche/industry? (search by industry keywords)

**This is a flat file grep — zero API calls, instant results.** Always run this FIRST before hitting Attio or other sources. A LinkedIn connection is a warm path even if there's no email/calendar interaction in Attio.

**Scoring:** LinkedIn 1st-degree connection = WARM (Kay has met or accepted this person). If the connection is at the target company, that's a direct intro path. If they're in the same industry, that's a shared-background bridge.

### 1. Attio CRM — Kay's Direct Network (PRIMARY)
```bash
# Search for connections to the target company
mcp__attio__search_records_by_relationship --object companies --query "{target_company}"
mcp__attio__search_records_by_content --query "{owner_name}"

# Search for connections in the target's industry/geography
mcp__attio__search_records --object people --query "{industry keyword}"
```

What to look for:
- Does Kay know anyone at this company?
- Does Kay know anyone who USED to work at this company?
- Does Kay know anyone in the same industry vertical?
- Does Kay know anyone in the same city/metro who could make a local intro?

### 2. Vault Entities + Calls — Relationship History
```bash
# Search vault for mentions of the target company or owner
grep -r "{company_name}" brain/entities/ brain/calls/ brain/outputs/
grep -r "{owner_name}" brain/entities/ brain/calls/
```

What to look for:
- Was this company or person mentioned in any call transcript?
- Did an investor, river guide, or industry expert reference them?
- Is there a prior relationship that went dormant?

### 3. Gmail — Prior Correspondence
```bash
gog gmail search -a kay.s@greenwichandbarrow.com --query "{company_name} OR {owner_name}" -j --max 5
```

What to look for:
- Any prior email exchange with the target or about the target
- Was the target CC'd in an introduction email?
- Did a broker or intermediary mention this company?

### 4. Investor Network — Warm Intro via Investors
Check if any of Kay's 12 investors have connections:
- Read `brain/entities/` for investor profiles
- Check investor portfolio companies for overlap with target's industry
- Check investor LinkedIn connections if available

Investors serve dual purpose: niche validation + natural touchpoint between quarterly updates.

### 5. LinkedIn — Mutual Connections (LAST RESORT)
```bash
# Web search for mutual connection paths
WebSearch: "{owner_name} {company_name} LinkedIn"
WebSearch: "{owner_name} NYU Stern" OR "{owner_name} Chanel" OR "{owner_name} search fund"
```

Check for shared backgrounds:
- NYU Stern alumni (Kay's network)
- Luxury/fashion industry (Kay's Chanel background)
- Search fund community (fellow searchers)
- Conference attendees (from conference-discovery lists)
</sources>

<scoring>
## Intro Path Scoring

### Warm (highest priority — use this path)
- Kay has met this person or someone at the company
- Kay has a direct contact who can make an intro (river guide, investor, industry expert)
- Prior email correspondence exists
- Mentioned in a call transcript with positive context

### Investor Intro (medium — natural touchpoint)
- An investor has a portfolio company in the same industry
- An investor has a known connection to the target's geography/network
- Tag: include which investor and the connection context

### Shared Background (medium-low — soft opener)
- Same alma mater (NYU Stern, etc.)
- Same industry background (luxury, fashion, art)
- Same conference attendee list
- Same professional community (search fund, ETA)

### Cold (no intro path found)
- No connections detected across any source
- Default — still worth pursuing, just via standard outreach-manager cadence
</scoring>

<workflow>
## Inline Mode (per-target, called by target-discovery)

For each new target added to the sheet:

1. **Extract target info:** company name, owner name, location, industry
2. **Run all 5 source checks** in parallel (Attio, vault, Gmail, investors, LinkedIn)
3. **Score the intro path** (warm / investor intro / shared background / cold)
4. **Write to sheet:** Update the target's row with intro path and contact info
5. **If warm intro found:** Flag in chatroom/output for Kay's attention

## Batch Mode (manual invocation)

When invoked via `/warm-intro-finder`:

1. **Read the target sheet** for the specified niche
2. **Filter to rows missing intro data** (no intro path assigned)
3. **Spawn parallel sub-agents** (1 per 5-10 targets) to run source checks
4. **Compile results** and update all rows
5. **Summary report:** X targets checked, Y warm intros found, Z investor intros, remainder cold
6. **Present warm intros to Kay** — these should be prioritized in outreach sequencing

## Integration with outreach-manager

When outreach-manager picks up approved targets:
- **Warm intro targets** → different email template (reference the connection)
- **Investor intro targets** → Kay reaches out to investor first, then outreach after intro
- **Cold targets** → standard outreach cadence via niche's assigned channel (Kay Email or DealsX Email)

## DealsX Screen Mode

When invoked in `dealsx-screen` mode, takes Sam's outreach list as input, runs all 5 source checks (LinkedIn grep, Attio, vault, Gmail, investor network), and returns flagged targets that should be pulled from Sam's send list because Kay has a warm intro path. This prevents Sam from cold-emailing Kay's network.
</workflow>

<sub_agents>
## Sub-Agent: Network Scanner

```
You are a warm intro finder for Greenwich & Barrow, a search fund.

TARGET: {company_name} | {owner_name} | {location} | {industry}

YOUR TASK: Search all available sources to find warm introduction paths from Kay Schneider's network to this target.

Check these sources:
1. Attio CRM — search for the company, owner, industry contacts, geographic contacts
2. Vault (brain/entities/, brain/calls/) — grep for company name and owner name
3. Gmail — search for prior correspondence
4. Investor connections — check if any of Kay's investors have relevant connections
5. LinkedIn/web — search for shared backgrounds (NYU Stern, luxury/fashion, search fund community)

SCORING:
- WARM: Direct connection exists (Kay knows someone who knows the owner)
- INVESTOR INTRO: An investor could make the connection
- SHARED BACKGROUND: Common alma mater, industry, or community
- COLD: No connection found

OUTPUT FORMAT:
Company: {name}
Owner: {name}
Intro Path: {WARM | INVESTOR INTRO | SHARED BACKGROUND | COLD}
Intro Contact: {name, relationship to Kay, how they connect to target}
Reasoning: {1-2 sentences on the path}
Confidence: {HIGH | MEDIUM | LOW}
```
</sub_agents>

<success_criteria>
## Success Criteria

- [ ] All targets in specified niche checked against all 5 sources
- [ ] Each target tagged with intro path score
- [ ] Warm intros surfaced to Kay with contact + context
- [ ] Target sheet updated with intro data
- [ ] No false positives (don't claim warm when connection is tenuous)
</success_criteria>

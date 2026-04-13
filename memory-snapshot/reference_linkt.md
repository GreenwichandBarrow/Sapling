---
name: Linkt Platform & API
description: Linkt AI list-building platform — 3 flows (profile, search, signal), 150 credits/month, 1 credit per entity, API reference
type: reference
---

## Linkt (linkt.ai) — AI-Native List Building & Enrichment

**API Key:** `sk-uGj_YvWMrrA1KGBzJiMbcfsdZTH9Oc_L6WSmi_JGoC0`
**Base URL:** `https://api.linkt.ai/v1/`
**Auth:** `x-api-key` header (NOT Bearer)
**Docs:** https://docs.linkt.ai
**Dashboard:** https://app.linkt.ai

## Plan Status

**Cancelled/downgrading as of March 31, 2026.** Was on Pro plan ($300/mo, 300 credits/mo). Re-subscribe in sprints when actively running target discovery, not as ongoing subscription. When re-subscribing, run full E2E test first.

## Credit Model

**Pro plan: 300 credits/month. 1 credit = 1 entity (company or person) created via Search flow.**
- Profile flows: no credits
- Signal monitoring: no credits
- Only Search flows consume credits
- Every credit must count. Keep ICPs tight so search results are pre-qualified.

## Three Flows

### 1. Profile Flow
- Takes a high-level description of your target criteria
- Generates foundational research on the target market
- No credits consumed
- Use to establish baseline understanding before running searches

### 2. Search Flow (costs credits)
- Core list-building engine
- Requires an ICP (Ideal Customer Profile) with detailed criteria
- AI agents research and enrich companies + decision-makers matching ICP
- Creates structured entity records with 15+ fields per company/person
- 1 credit per entity created
- Run time: 25 min to 20 hours depending on scope

### 3. Signal Flow
- Continuous monitoring for buying signals on existing companies
- Tracks: leadership_change, regulatory, job_posting, expansion, acquisition
- Runs on schedule (weekly)
- No credits consumed

## Data Returned Per Company
- Name, website, LinkedIn, headquarters (city/state/zip)
- Industry, employee count, revenue (estimated)
- Ownership/funding status
- Specialty market evidence
- Custom criteria verification (boolean checks against ICP)

## Data Returned Per Person
- Name, title, company, email (validated), phone
- LinkedIn, location (city/state)
- Tenure at company
- Role verification against ICP criteria

## Correct API Flow (CRITICAL — All Steps Required)

**Order of operations:** ICP → Sheets → Task → Execute. Skipping any step = silent failure.

### Step 1: Create ICP (with entity_targets)
```
POST /v1/icp
{
  "name": "Niche Name Search",
  "description": "Find 50 independently owned {description}. Focus on {criteria}...",
  "entity_targets": [
    {"entity_type": "company", "root": true},
    {"entity_type": "person"}
  ]
}
```
**CRITICAL:** `entity_targets` array is REQUIRED. Without it, ICP shows "Complete" immediately with 0 results. The `description` IS the prompt to Linkt's AI — write it as a clear instruction. Put target count in the description text (e.g., "Find 50...") because the `desired_count` parameter is IGNORED by Linkt.

### Step 2: Create Sheets for the ICP
```
POST /v1/sheet
{"name": "Niche - Companies", "icp_id": "{icp_id}", "entity_type": "company"}

POST /v1/sheet
{"name": "Niche - People", "icp_id": "{icp_id}", "entity_type": "person"}
```
**Both sheets (company + person) must exist before task execution.**

### Step 3: Create Task
```
POST /v1/task
{"icp_id": "{icp_id}", "type": "search"}
```

### Step 4: Execute Task
```
POST /v1/task/{task_id}/execute
Content-Type: application/json
Body: {}
```
**Empty JSON body `{}` is required.** Without it, execution fails.

### Common Failure Mode
ICPs created without `entity_targets` → task shows "Complete" instantly → 0 results. This was the root cause of all failed Linkt searches in March 2026.

## Key Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/icp` | GET/POST | List/create ICPs |
| `/v1/task` | GET/POST | List/create tasks |
| `/v1/task/{id}/execute` | POST | Execute search/signal task (requires `{}` body) |
| `/v1/sheet` | GET/POST | List/create result sheets (REQUIRED before task execution) |
| `/v1/run` | GET | List run history |
| `/v1/entity/search` | GET | Search entities (q=query&entity_type=company\|person) |
| `/v1/entity/{id}` | GET | Get enriched entity |
| `/v1/entity/export` | GET | Export entities |
| `/v1/schedule` | GET/POST | Manage recurring tasks |
| `/v1/files/upload` | POST | CSV ingest |

## Kay's Existing ICPs
- "Specialty Insurance Compliance Search Fund Target" — insurance compliance tech, $5-40M, 10-150 employees
- "NYC Tri-State Private OpCo Acquisition Search" — B2B services, $10-50M, 10+ years established

## Access
- Kay only (JJ's access removed 2026-03-22). All searches run by the agent via API.

## Kay's Usage
- Pro plan ($300/mo, 300 credits/mo). **Cancelled/downgrading March 31, 2026.**
- Final session: 263 credits burned on v3 searches across 5 niches.
- Re-subscribe in sprints only. Run full E2E test (ICP with entity_targets → sheets → task → execute → verify results) before burning credits on real searches.

## MCP Integration (Recommended)

As of 2026-03-31, Linkt is connected via MCP server — NOT raw API calls.

Config in `.mcp.json`:
```json
"linkt": {
  "type": "http",
  "url": "https://api.linkt.ai/mcp",
  "headers": {
    "x-api-key": "${LINKT_API_KEY}"
  }
}
```

MCP provides direct tool access to ICPs, Sheets, Tasks, Entities, Runs, Files.
Rate limits: 60 requests/minute, 5 concurrent executions.

## Known Issues (March 2026)

- **ICP propagation bug:** 4 of 5 ICPs failed with "ICP ID not present on run the document." Tasks created correctly but runs showed `icp_id=None`. Rapid task creation (5 tasks in 6 seconds) may trigger race condition. Report to Reid McCrabb.
- **Duplicate entities:** Multiple entries for same company (e.g., 3 entries for Howard & Gay Insurance). Use `hide_duplicates=True` when pulling results. Cross-ICP dedup is automatic; within-ICP dedup behavior unclear.
- **Credit model:** Each entity = 1 credit. Company + person = 2 credits per target. 42 targets consumed 96 credits (overhead from failed runs or enrichment).
- **ICP naming:** Name by date (e.g., "IPLC 2026-03-30"), not version (v1/v2/v3).

## Workflow for Target Discovery Skill
1. Linkt is the primary list builder — it has the database, does the discovery AND enrichment in one step
2. Claude creates/uses ICP in Linkt matching the niche sprint (via MCP tools)
3. Run Search flow — Linkt's AI agents find companies matching ICP, enrich with contact info
4. Pull enriched entities (company + person with email/phone), use `hide_duplicates=True`
5. Claude supplements with free sources (association directories, web research) for targets Linkt missed
6. Kay reviews combined list
7. Company → Attio Active Deals pipeline at "Identified"
8. Person email → Claude drafts personalized outreach via Superhuman
9. Person phone → JJ's call list

## Credit Budget Strategy (300/month on Pro, when subscribed)
- ~10-12 companies/day if running daily
- Linkt IS the list builder — discovery is what it's for, just keep searches tight and focused
- Create tight ICPs so search results are pre-qualified
- Run smaller, focused searches (10-20 entities) rather than large broad ones
- Save some credits for signal monitoring and conference attendee enrichment
- **Sprint model:** Subscribe for active niche sprints only, cancel between sprints

---
name: Apollo.io API for email verification
description: Apollo free tier API for verifying non-Linkt email addresses before outreach
type: reference
originSessionId: e26dda1b-d8f3-41ea-b671-19271a6fed00
---
## Setup
- **API key:** stored in `.env` as `APOLLO_API_KEY`
- **Account:** Free tier (50 credits/month)
- **Purpose:** Verify email addresses for non-Linkt targets before drafting outreach

## API Endpoint
People Match: `POST https://api.apollo.io/v1/people/match`

```bash
curl -s "https://api.apollo.io/v1/people/match" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $APOLLO_API_KEY" \
  -d '{
    "first_name": "{first}",
    "last_name": "{last}",
    "organization_name": "{company}",
    "domain": "{domain}"
  }'
```

## Email Status Values
- `verified` — confirmed deliverable. Draft the email.
- `guessed` — Apollo's best guess. Flag on sheet, don't draft.
- `unavailable` — no email found. Flag on sheet.
- `bounced` — known bad. Flag on sheet.
- `pending` — still checking. Retry later.

## Credit Usage
- 1 credit per People Match call (with email reveal)
- **Plan as of 2026-04-29:** paid tier with monthly credit cap (exact cap not exposed via API)
- **Billing cycle:** 1st of each month (e.g., Apr 1 – May 1, May 1 – Jun 1)
- **Monthly balance is NOT exposed via API** — Apollo's API key path only returns per-minute rate-limit headers (`x-rate-limit-minute`, `x-minute-usage`, `x-minute-requests-left`). The "999 remaining" on G&B's dashboard is per-minute throughput, NOT monthly credits.
- **To check monthly balance:** log into apollo.io → Settings → Credit Usage. Cannot be automated through the API key.
- **Dashboard tile note:** the "Apollo credits" tile in the Command Center reads the per-minute header, so the displayed number is per-minute rate-limit headroom, not monthly budget. Future fix: relabel tile to "Apollo per-min throughput" + add a manual monthly-balance field that Kay updates after checking apollo.io UI.

**Useful for budgeting subagent runs:**
- Per-minute throughput is plenty (1000/min) — never the bottleneck
- Monthly cap IS the bottleneck — plan subagent prompts with explicit credit caps (e.g., "cap at 200 credits") to avoid burning the monthly allowance unintentionally
- Linkt is sunset (per Apr 29 conversation; "no longer use Linkt"). Apollo is now the primary enrichment path

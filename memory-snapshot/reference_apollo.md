---
name: Apollo.io API for email verification
description: Apollo free tier API for verifying non-Linkt email addresses before outreach
type: reference
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
- 1 credit per People Match call
- 50 credits/month on free tier
- Only used for non-Linkt targets (Linkt does its own verification)

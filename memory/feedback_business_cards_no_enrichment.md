---
name: Business cards are gold — never cross-reference with Apollo
description: Business cards collected in-person are definitive truth. Do not enrich, verify, or cross-reference against Apollo. Use the card data as-is.
type: feedback
originSessionId: 79db8074-299b-4018-a98a-3aced9a42eb3
---
Business cards handed to Kay in person are the gold-standard contact source. They require no verification, enrichment, or cross-reference against Apollo or any other database.

**Why:** A business card is a direct, physical handoff from the person. It's more authoritative than any enrichment tool could produce. Running Apollo lookup on card data introduces three failure modes: (1) Apollo returns a stale/different email than the one the person chose to give Kay, which is actively worse, (2) wastes API budget meant for cold list-building, (3) delays the 24-hour follow-up window when speed matters most.

**How to apply:**
- In the `conference-engagement` post-conference mode: OCR card → use card data verbatim → done. No Apollo step.
- **Capture every field printed on the card.** Name, title, company, address, email, office phone, mobile phone, fax, LinkedIn, website. If it is on the card, capture it into Attio. Kay's rule (2026-04-23): "since they are on the cards, this is the time for you to capture their phone numbers as well." Extends to every other printed field.
- If a field is missing from the card (e.g., no email, only phone), ask Kay once or skip that channel. Never guess. Never Apollo-lookup.
- Attio dedup (checking if this person already exists in the CRM) is still fine — that's deduplication, not enrichment. Different operation.
- Reconciles with `feedback_apollo_only_emails`: that rule prevents guessing/scraping emails for cold-outreach strangers. A business card is a direct handoff, not a scrape, so Apollo is unnecessary and actively harmful.
- Applies to any contact source where the person directly provided their info: business cards, email signatures, LinkedIn messages where they shared contact details, event registration where they listed their email.

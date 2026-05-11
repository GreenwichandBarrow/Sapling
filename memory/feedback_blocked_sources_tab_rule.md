---
name: Deal-aggregator Blocked Sources tab — only fully-unreachable sources, not partial-blocks
description: The "Blocked Sources" tab on the G&B Deal Aggregator Sourcing List (sheet 1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw, tab created 2026-05-04) is for sources where NO automation channel works at all. Web-blocked but email-channel-active sources stay on General Sources because they're still scannable.
type: feedback
originSessionId: eadbe8c6-1597-404d-a31b-5cedebba7005
---
The G&B Deal Aggregator sourcing list has 3 tabs:
- **General Sources** — actively scanned (any working channel: web, email, API)
- **Niche-Specific Sources** — niche-tagged subset of active
- **Blocked Sources** (added 2026-05-04) — sources where NO automation channel reaches; manual browser check only

**Rule for Blocked Sources placement:** A source goes on the Blocked Sources tab ONLY when EVERY automation channel is unreachable. Specifically:
- Web returns 403 / Cloudflare gate / JS shell unreachable to WebFetch, AND
- Email subscription is unavailable OR not active, AND
- No API / RSS / other programmatic feed exists

**Web-blocked but email-channel-active stays on General Sources.** Examples (per Kay 2026-05-04):
- **Flippa** — web 403, but email subscription active → STAYS on General Sources
- **Quiet Light** — Cloudflare 403 to scraper, email subscription active → STAYS on General Sources
- **Synergy Business Brokers** — public listings visible, only DETAIL is NDA-gated → STAYS on General Sources
- **ProNova Partners** — web 403, no email channel → MOVED to Blocked Sources

**Why:** The point of the Blocked tab is to give Kay a manual-check list — sources where automation gives her nothing, so she has to physically open them in a browser. Sources with email feeds aren't manual-check candidates because the email scan still surfaces deals automatically. Putting them on Blocked would create false work for Kay.

**How to apply:**
- When verifying a source's accessibility, classify by ALL channels, not just web
- Source on Blocked tab = full-block. Has email → wrong tab.
- Don't duplicate sources across tabs (cleanup observed 5/4: ProNova was on both General as "Blocked" status AND on Blocked Sources tab — Kay called for dedup, kept on Blocked Sources only).
- When adding a new source: web-fetch test + email-subscription test + lookup for any RSS/API. Only Blocked tab if ALL three fail.

Source: 2026-05-04 broker-channel build, Kay clarified the distinction after I created the Blocked Sources tab and asked which web-blocked-but-email-active sources should migrate.

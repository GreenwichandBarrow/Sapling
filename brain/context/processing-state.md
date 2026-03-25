---
type: state
description: Processing state for automated workflows
---

## Email Scan State

```yaml
last_email_scan: 2026-03-24T13:00:00Z
backfill_complete: true
```

## Platform Scan State

```yaml
last_platform_scan: 2026-03-25
platforms_scanned:
  - rejigg: accessible. 2 thesis matches (insurance agency 113563, insurance adjusting 111136), 1 buy-box new niche (labor compliance 109771). Slacked.
  - business_exits: accessible. No thesis matches. 3 buy-box adjacent but all disqualified (customer concentration, too expensive, California).
  - bizbuysell: blocked (403), needs manual browse
  - everkerr: no public listings, relationship-only
  - quiet_light: blocked (JS required)
  - flippa: blocked (JS required)
  - benchmark: blocked (JS required)
  - fe_international: blocked (JS required)
  - website_closers: accessible. eCommerce/DTC skew, no matches.
  - dealforce: blocked (JS required)
  - gottesman: accessible. All listings $25M+ revenue, too large.
  - pronova: blocked (403)
  - woodbridge: JS-rendered. Search snippets show "Trusted LTC Compliance Partner" ($3.5M EBITDA) — thesis-adjacent. Needs manual browser check.
  - paine_pacific: partially accessible. 4 listings, no thesis matches.
  - graphic_arts_advisors: blocked (Wix/JS)
  - iag: no public listings, routes to BuyYourBiz.com marketplace
previously_flagged:
  - rejigg_112360  # Cybersecurity Insurance Platform (3/22)
  - rejigg_113762  # Environmental Risk Mgmt (3/23)
  - rejigg_111175  # Environmental Consulting (3/23)
  - business_exits_ca_property_tax  # CA Property Tax Consultants (3/23)
  - rejigg_113310  # Healthcare Revenue Mgmt (3/24, borderline)
  - rejigg_113563  # Insurance Agency, OH (3/25, thesis match)
  - rejigg_111136  # Insurance Adjusting, CT (3/25, thesis match)
  - rejigg_109771  # Labor Compliance Consulting, MI (3/25, buy-box new niche)
```

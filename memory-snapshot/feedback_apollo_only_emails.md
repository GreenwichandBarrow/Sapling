---
name: Apollo is the only email source
description: Never scrape emails from web research — Apollo /people/match is the only source for target emails
type: feedback
---

Apollo `/people/match` is the ONLY source for target emails. Web research provides owner names, titles, and LinkedIn URLs — never emails.

**Why:** Web-scraped emails are frequently wrong (generic inboxes like info@, old addresses, wrong people, different companies). The Art Advisory test run caught 4 wrong-domain emails inherited from Linkt web research that Apollo would have gotten right. Generic emails (info@, office@) bounce or go to a shared inbox — worthless for cold outreach.

**How to apply:** In target-discovery Phase D, Apollo people/match is called with the owner name + company domain. Any pre-existing email from prior data sources (Linkt, manual entry) must pass domain-match validation before use. If email domain ≠ company website domain, discard and re-run through Apollo.

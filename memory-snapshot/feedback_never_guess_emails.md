---
name: Never guess email addresses
description: CRITICAL - never construct/guess email addresses from name + domain patterns. Only use verified sources.
type: feedback
---

NEVER guess or construct an email address from a person's name + company domain. If the exact email doesn't exist in a verified source (Linkt, company website, email signature, LinkedIn, prior correspondence), do NOT use it.

**Why:** Kay's email domain is her entire business. A bounced email damages sender reputation and can get her domain flagged. This happened with cjanuski@jwigroup.com on March 31, 2026 -- the email was constructed from name + domain, bounced immediately, and should never have been drafted.

**How to apply:** Before creating ANY email draft, check if the email is from a verified source:
- Linkt-sourced emails: skip verification (Linkt validates its own data)
- Prior correspondence: if Kay has already emailed/received email from this address, it's verified
- All other emails: run through Apollo API verification before drafting. Only proceed if `verified`. If `guessed`/`unavailable`/`bounced`, tell Kay and stop.

This applies EVERYWHERE: outreach-manager, pipeline-manager, relationship-manager, ad-hoc conversation drafts, and any other context. No exceptions.

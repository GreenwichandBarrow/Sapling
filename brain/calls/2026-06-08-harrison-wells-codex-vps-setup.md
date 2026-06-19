---
schema_version: "1.1.0"
date: 2026-06-08
type: call
call_id: not_DwWI3B5j0lUjec
source: granola
classification_type: partner
people: ["[[entities/harrison-wells]]", "[[entities/kay-schneider]]"]
companies: ["[[entities/dodo-digital]]", "[[entities/greenwich-and-barrow]]"]
tags: ["date/2026-06-08", "call", "client/greenwich-and-barrow", "person/harrison-wells", "person/kay-schneider", "company/dodo-digital", "company/greenwich-and-barrow", "topic/codex-migration", "topic/vps", "topic/account-hygiene"]
granola_link: https://notes.granola.ai/d/not_DwWI3B5j0lUjec
---

# Harrison <> Kay: Codex VPS Setup

**Date:** 2026-06-08, 1:45 PM ET
**Attendees:** [[entities/harrison-wells|Harrison Wells]] ([[entities/dodo-digital|Dodo Digital]]), [[entities/kay-schneider|Kay]] ([[entities/greenwich-and-barrow|G&B]])

---

## Notes

This was a focused operating session on Kay's Codex setup rather than a business-development conversation. The main threads were account cleanup, moving execution to the VPS, and removing ambiguity between local desktop behavior and the VPS-backed environment. Harrison walked through the setup state, explained how the green-dot VPS indicator should behave, and helped Kay separate the personal Codex account from the earlier business-workspace sprawl.

The practical outcome was a cleaner understanding of what is now configured and what still needs validation. Kay now has a more reliable path to use Codex on the VPS, but the call made clear that the next risk is not model quality; it is execution drift between the UI, the alias, and the actual runtime location.

Full analysis: https://docs.google.com/document/d/1ktj2iHBf9wcWlShgefZ1KzjKHCUXa5xf8HYGcUANuKY/edit?usp=drivesdk
Granola transcript: https://docs.google.com/document/d/1Twha0my-oN71wX6wr_BWC7Heal5S_UQasSUPzNyjQEE/edit?usp=drivesdk
Granola source: https://notes.granola.ai/d/not_DwWI3B5j0lUjec

---

## AI Analysis

### Action Items
- [ ] Confirm a fresh Codex chat opens on the VPS without falling back to local desktop behavior.
- [ ] Audit shell aliases and wrappers for lingering local-only assumptions or `claude -p` execution paths.
- [ ] Verify the business workspace/API usage is fully shut down so the account stays on the personal plan.

### Signals
- The main failure mode was environment ambiguity, not idea quality.
- Harrison remains a useful calibration partner for Codex migration and operational cleanup.
- The setup now appears closer to a single-source-of-truth model, but it still needs a quick validation pass before unattended reliance.

---
*Auto-classified by post-call-analyzer*

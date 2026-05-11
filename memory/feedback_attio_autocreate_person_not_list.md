---
name: Attio auto-creates People from email but NOT list entries
description: Gap in pipeline-manager — outbound emails generated Person records but no Active Deals list entry
type: feedback
originSessionId: 86f718b9-b93e-4f82-8d6a-93917c8d6d15
---
Attio auto-creates **Person records** from any email interaction, but does NOT auto-create **list entries** (Active Deals, Intermediary Pipeline, etc.). Pipeline-manager's outbound email scan must reconcile this — for any outbound email to an external recipient, check if the Person's company has an Active Deals list entry, and CREATE one at "Contacted" stage if missing.

**Why:** 2026-04-15 Timothy Wong / MMPC incident. Kay emailed Timothy Wong 2026-04-09 (cold outreach). Attio auto-created his Person record. Pipeline-manager ran daily, saw the outbound email, but the recipient wasn't in the Active Deals list — so it registered "no match" and moved on instead of creating the list entry. Kay surfaced the gap manually 6 days later when Timothy replied on Slack.

**How to apply:** `pipeline-manager` outbound scan uses `newer_than:14d` window and is a **reconciler-and-creator**, not read-only. Every outbound email to external recipient → verify list entry exists → create at Contacted if missing, with `source: manual-outbound-email` and niche tagged from target sheet match. Stop hook #11 validates coverage. Never assume "Person exists in Attio" = "target is tracked in pipeline."

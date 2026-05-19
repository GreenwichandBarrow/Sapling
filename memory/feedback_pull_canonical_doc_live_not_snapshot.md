---
name: feedback_pull_canonical_doc_live_not_snapshot
description: Always pull the live Drive canonical doc before drafting; never draft from a stale brain/outputs vault snapshot
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8204e9db-579c-412b-8bf1-3682a28e14d1
---

Before drafting from any template/canonical doc, pull it LIVE: `bash scripts/fetch-template-doc.sh` (defaults to the Intermediary Templates doc; pass a doc ID for others). NEVER draft from `brain/outputs/2026-05-04-broker-outreach-templates.md` or any `brain/outputs/*-templates.md` snapshot.

**Why:** Vault files under `brain/outputs/` are creation-time snapshots, not canonical. The broker-templates snapshot is titled "LOCKED FINAL" yet was stale (4 of 10+ live templates) and even self-noted it was superseded — I still drafted from it. CLAUDE.md source-of-truth: Drive owns living documents; vault copies are snapshots only. Kay 2026-05-18: "we already created templates, so I think you need to update to make sure you are referencing them." Same meta-failure as skipping 1Password — not referencing the canonical source first. See [[feedback_op_env_before_op_backed_cli]], [[feedback_no_intermediary_drafts_outside_template]].

**How to apply:** `bash scripts/fetch-template-doc.sh` auto-resolves 1Password and prints the live doc. For a not-yet-enumerated intermediary context, use the doc's DIRECTORY-SOURCED VARIANT mechanism: keep body/sign-off/footer verbatim, swap only the first body sentence, propose the opener for Kay's approval. CLAUDE.md "Before writing any external message" pre-flight + outreach-manager SKILL.md both carry the pull-live rule; the snapshot has a DO-NOT-DRAFT banner.

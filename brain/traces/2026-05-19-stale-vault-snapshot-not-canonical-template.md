---
schema_version: 1.1.0
date: 2026-05-19
type: trace
task: Source the broker/intermediary email template for a warm-intro reply
had_human_override: true
tags:
  - date/2026-05-19
  - trace
  - topic/intermediary-outreach
  - topic/template-locked
  - pattern/canonical-source-first
  - status/done
---

# Stale vault snapshot is not the canonical template

## Context
Drafting a warm-intro reply to Sam (broker at [[entities/transworld|Transworld]]), introduced by [[entities/becky-wuest-creavin|Becky Wuest Creavin]]. Intermediary bodies must originate from a canonical template. With gog initially broken, I worked from the vault file `brain/outputs/2026-05-04-broker-outreach-templates.md` and proposed an ad-hoc rewrite. Kay: "we already created templates, so I think you need to update to make sure you are referencing them."

## Decisions

### Which template source to draft from
**AI proposed:** Use the 2026-05-04 vault snapshot (it is titled "LOCKED FINAL") and propose an ad-hoc warm-intro body.
**Chosen:** The vault snapshot is a creation-time artifact and stale (reproduces 4 of 10+ live templates). The live Drive doc `1gTQoCbaX8IyrTDli4Xd6IBtCqCT-DwciOUnNmgv0_J4` is canonical (CLAUDE.md source-of-truth: Drive owns living documents). Pull it live every time via `scripts/fetch-template-doc.sh`.
**Reasoning:** The snapshot's "LOCKED FINAL" header is misleading; it even states it was superseded the same evening but I still drafted from it. A snapshot in `brain/outputs/` looks authoritative but is not.
**Pattern:** #canonical-source-first

### Warm-intro template path
**AI proposed:** Treat warm-intro as a brand-new template scenario.
**Chosen:** The live doc's DIRECTORY-SOURCED VARIANT defines the sanctioned mechanism for any not-yet-enumerated context — keep body/sign-off/footer verbatim, swap only the first body sentence; propose the new opener for Kay's approval.
**Reasoning:** Not ad-hoc and not a from-scratch template — the doc already encodes how to handle new contexts. Kay sent the result, validating the swap mechanism.
**Pattern:** #canonical-source-first

## Learnings
A vault file under `brain/outputs/` is a snapshot, never the canonical living doc — pull Drive live before drafting. For not-yet-enumerated intermediary contexts, the DIRECTORY-SOURCED VARIANT swap mechanism is the compliant path, not a new template. Same meta-failure as the credentials miss: not referencing the canonical source first. Durable fix: `scripts/fetch-template-doc.sh` + SKILL.md/CLAUDE.md pointers + loud DO-NOT-DRAFT banner on the snapshot.

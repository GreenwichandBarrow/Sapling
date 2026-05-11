---
name: Broker Emails Carry One-Pager Attachment, No Embedded Visual Signature
description: 2026-05-04 visual signature decision. Outbound broker email (Day 0 intro, Day 5 follow-up, Lawyers/CPAs intro) attaches a one-pager (Megan Lawlor pattern) and uses plain-text body only. Logo card, buy-box graphic, and combined options all rejected.
type: project
originSessionId: b0545682-a352-4898-9fa7-a9ba99e3d30f
---
Outbound broker email (Day 0 INTRODUCTION, Day 5 FOLLOW-UP, Lawyers + CPAs INTRODUCTION) attaches a one-pager and uses plain-text body. NO embedded visual signature in body — logo card, buy-box graphic, and the combined option were all rejected on 2026-05-04.

**Why:** During the broker-channel build (Block 7+), the visual signature question surfaced as part of template lock. Considered three options (logo card / buy-box graphic / both). Kay rejected all three in favor of the simpler attachment-only approach. Mirrors the Megan Lawlor pattern (`project_megan_broker_outreach_pattern`) where the broker-specific one-pager goes as a separate file rather than embedded body content. Body stays plain text with the existing "What We Look For" footer where applicable. Decision lives in conversation memory rather than the canonical templates doc because it's a channel/attachment design choice, not a body-copy template.

**How to apply:**
1. When outreach-manager Subagent 3 (Intermediary) drafts a broker outbound email, attach the broker-channel one-pager (separate Drive file, version pending lock) via `gog gmail draft --attachment={one-pager-id}`.
2. Do NOT embed images, logo cards, or buy-box graphics in the body. Plain text only.
3. The "What We Look For" footer stays as plain-text on Day 0 INTRODUCTION and LEAD-NO / DECLINE POST-REVIEW templates.
4. The one-pager itself needs separate creation and lock — track as a follow-up. Likely lives in Drive `OPERATIONS / G&B MASTER TEMPLATES / Broker One-Pager` once authored.

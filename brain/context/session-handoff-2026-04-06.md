---
date: 2026-04-06
type: context
title: "Session Handoff — April 6, 2026 (Monday)"
tags: ["date/2026-04-06", "context", "topic/session-handoff"]
---

# Session Handoff — April 6, 2026

Read this at the start of the next session. It captures what happened, what's pending, and what needs fixing.

## What Happened Today

### Domain Protection (DONE)
- SPF record added to greenwichandbarrow.com
- DKIM enabled via Google Workspace Admin, key published to DNS
- DMARC upgraded from p=none to p=quarantine with rua reporting to kay.s@greenwichandbarrow.com
- MxToolbox check: no blocklisting, warnings only (Google infrastructure, not actionable)
- DMARC tighten to p=reject scheduled for ~Apr 20

### G&B Cold Call Guide (DONE — working document)
- Universal guide (not niche-specific) based on Kevin Hong's Caprae LeadGen Guidelines
- Google Doc: https://docs.google.com/document/d/12Hqfwxg4qJA3YdZh36ndd-flvYgWNZeL8sMZ9NAHlTY/edit
- Location: Operations / Call Logs in Google Drive
- Niche context lives on "Niche Context" tab on each target sheet (Pest Management tab created)
- Simplified for overseas caller — JJ redirects all deep questions to Kay
- Includes: lukewarm handoff model, ice-and-recall (4-6 week re-call), gatekeeper phone number technique
- Shared with JJ via Slack on Apr 6 — awaiting his feedback
- Kay added letterhead, headers, footers, set font to Avenir — DO NOT REMOVE these when editing

### Kevin Hong Call (DONE — intelligence gathered, no engagement)
- Kevin/Caprae is a HARD NO for service. Success fee (up to $300k, % of EV) exposes relationship to investors.
- Key insights captured in call guide: cold calling >> email, blue collar works in NY, 25 hrs/week max, lukewarm handoff, ice-and-recall, gatekeeper techniques, 15-20% of owners ever pick up
- NY is poor for cold calling generally BUT blue collar (pest management) works there
- Kay's "double sell" challenge: educating sellers who've never sold + selling herself as first-time buyer
- Full transcript saved in this conversation (not in vault — too long, key points in session decisions)

### Sam Singh / DealsX Call (DONE — evaluating)
- Email + LinkedIn at scale. $1,500/mo for 3 niches, 1,500 businesses/month. $25k flat success fee. Month-to-month.
- 3-week onboarding for domain warmup. Dashboard with live reporting.
- Sam sent deck (in Drive: RESOURCES/DEALSX) and references same day
- Kay wants to talk to references before committing
- None of Sam's references have actually closed a deal through DealsX — ask about this
- If Sam engaged: shifts our focus from outbound execution to reply management + deal evaluation
- Kay needs 2 more high-volume niches for Sam (pest management is 1 of 3)
- Kay noted Sam is good for big-TAM niches only. Small niches (art advisory) stay high-touch.

### Pest Management Enrichment (PARTIAL)
- 17 Northeast targets enriched with owner names via Apollo (11 NY metro + 6 expanded geo)
- Only 199 rows on Active tab, not 826 (rest are raw import)
- 17 is thin for JJ's 40/day target — need to go national
- Kevin confirmed blue collar works in NY, but also recommended distributed geographies

### Morning Briefing Items (PARTIALLY ADDRESSED)
- Mark Gardella reply drafted (not sent) — he replied to InsurTech follow-up asking about market sizing
- Levi (Acumen) email — Superhuman scheduled send missed. Still in drafts. Kay needs to re-send.
- 5 Art Advisory Day 0 drafts presented — NOT reviewed by Kay yet
- Ashley Emerole draft — Kay doesn't see it in Superhuman
- Fractional CFO Col Q — needs "Approve" stamps (25 targets)

## Skills That Need Updating

### Priority: Remove Salesforge/Reply.io references (34 occurrences across 6 skills)
- jj-operations/SKILL.md — 3 references
- target-discovery/SKILL.md — 12 references
- weekly-tracker/SKILL.md — 11 references
- health-monitor/SKILL.md — 6 references
- warm-intro-finder/SKILL.md — 1 reference
- niche-intelligence/references/tracker-access.md — 1 reference

### outreach-manager
- If DealsX is engaged: skill shifts from "draft and send emails" to "manage owner replies, prep Kay for calls, post-call follow-up"
- Add handwritten letter channel as future addition (backlog)
- Currently clean of Salesforge refs

### jj-operations
- Universal call guide doc ID already updated (12Hqfwxg4qJA3YdZh36ndd-flvYgWNZeL8sMZ9NAHlTY)
- Niche Call Guide references need updating — no longer per-niche guides, one universal guide + niche context tabs
- Line 159-160 still says "Other niches: create from templates/cold-call-guide-{niche-slug}.md on niche activation" — should say "use universal guide + create Niche Context tab on target sheet"
- Slack Message 2 to JJ (tracking changes) not yet sent — send when first daily call tab is ready

### conference-discovery
- Skill is still in draft/PRD status. Not implemented. Not running.
- Should run every Monday. Has not run. Needs implementation or at least manual trigger.
- Kay is prioritizing conferences as her highest-ROI activity — this skill matters.

## Stop Hooks to Add

1. **Never create Gmail API drafts.** Always present draft text in conversation. Superhuman draft script not installed.
2. **Never describe Kay as self-funded.** She is a traditional funded searcher with investors.
3. **Never mention Reply.io.** Resolved, expires Apr 16, $0.
4. **Never mention Kevin Hong/Caprae as a service option.** Hard no. Value was the call, captured in guide.
5. **When building from a reference document:** read the reference FIRST, copy its structure, adapt minimally. Do not write from scratch and layer in.
6. **One item at a time.** Do not bundle topics or rush ahead. Let Kay set the pace.
7. **Schwartzman is a pass.** One man show. Margot gave advice, no intros.

## Launchd Jobs NOT Installed

These are listed in CLAUDE.md as scheduled but NO plist files exist in ~/Library/LaunchAgents/:
- intermediary-manager (Mon-Fri 6am ET)
- email-intelligence (Mon-Fri 7am ET)
- jj-operations prep (Mon-Fri 8am ET)
- jj-operations harvest (Mon-Fri 4pm ET)
- conference-discovery (needs Monday schedule)

`launchctl list | grep greenwich` returns nothing. All scheduled skills are manual-only right now.

## Infrastructure Gaps

1. **Superhuman draft script** — ~/.local/bin/superhuman-draft.sh does not exist on this machine. Drafts cannot be created in Superhuman programmatically. Need to fix.
2. **Granola MCP** — added via `claude mcp add` but requires session restart to connect. Once active, can pull meeting transcripts directly.
3. **PDF reading** — poppler not installed. Cannot read PDF files. `brew install poppler` needed. DealsX deck is unread.
4. **greenwichbarrow.com** (without "and") — exists on Squarespace, Kay doesn't remember creating it. Web team may have. Confirm.

## Open Items for Next Session (Priority Order)

1. **Talk to Sam's references** — Kay's next step on DealsX
2. **Read DealsX deck** — install poppler, read the PDF
3. **Review Art Advisory 5 drafts** — presented but not reviewed
4. **Send Mark Gardella reply** — drafted, needs Kay's final review
5. **Re-send Levi (Acumen) email** — Superhuman scheduled send missed
6. **Pest Management go-national** — expand JJ's list beyond Northeast
7. **Send JJ Slack Message 2** — tracking changes (sheet-only, daily call tab)
8. **Install launchd jobs** — at minimum intermediary-manager and jj-operations
9. **2 more niches for Sam** — Kay needs to develop these for DealsX's 3-niche model
10. **Overdue contacts** — same 5 carried from prior sessions (Carlos, Kanayo, Michael Topol, Kristina, Lauren)

---
schema_version: 1.1.0
date: 2026-03-20
type: call
call_id: 20260320-ai-search-group
source: manual
classification_type: partner
people: []
companies: []
tags:
  - date/2026-03-20
  - call
  - topic/ai-tools
  - topic/search-fund-operations
  - topic/deal-sourcing
  - topic/proprietary-search
---

# AI in Search — Group Call

**Date:** 2026-03-20
**Attendees:** Kay + ~6-8 fellow searchers (names not captured — group WhatsApp community)
**Source:** Wispr Flow transcription (raw, cleaned by Claude)

## Notes

### Kay's Sharing: Claude Code Skills Workflow

Kay demonstrated her Claude Code skills-based workflow:
- **Skill development process:** Start with the objective, chat with Claude for ~20 minutes to land on the right skill design. Walk through every step diligently. Don't just say "build me a financial analysis skill" — say "I want a system for evaluating deals" and have Claude break it down.
- **Key advantage over ChatGPT:** No more copy-pasting 50 prompts. Skills are recallable. Just invoke the skill and it runs.
- **Deal evaluation system:** The 5-component pipeline was synthesized collaboratively with Claude. Claude guides you on how to use it.
- **Context is king:** More context = better output. Wispr Flow lets you dump 5 minutes of spoken context that would take 30 minutes to type.

### Deal Sourcing Discussion

**Brokered vs. Proprietary:**
- Kay currently focused on brokered deals but open to proprietary
- Important distinction: brokered deals have structured flow (SOW, data rooms). Proprietary is completely different workflow.
- If targets are early-stage thinking about selling, the approach changes entirely.

**Proprietary Search Tools Built by Attendees:**

1. **Lovable deal scraper** — One attendee built a deal scraper in Lovable:
   - Used Claude to generate step-by-step instructions, then fed those to Lovable
   - Built on International Women's Day (free credits)
   - Also built a personal website (4-5 tabs) to share with brokers/lenders/sellers
   - Scrapes BizBuySell and similar listing sites
   - Challenge: login walls on some sites require developer help

2. **Library database scraper** — Another attendee scraping a library database:
   - Built Python script via Claude (not Co-Work, just regular Claude chat)
   - Two-step login process with separate credentials
   - Bot detection workaround: script waits 1.5 seconds between clicks
   - Has generated ~40,000 companies so far
   - Next step: enrich data with filters, then auto-eliminate
   - Plan to use Claude for Excel/data cleaning

3. **Enrichment costs** — One attendee's friend (PE consultant) charges $500K for this work
   - Free scraping is possible but enrichment (employee count, revenue, Google reviews) requires paid tools
   - Grada notorious for bot detection
   - Google Maps/Reviews used as "is this a real business?" signal
   - 2-3 star Google reviews actually a positive signal (older businesses not social media savvy)

### CRM Discussion

- One attendee had a developer white-code a custom CRM in one weekend
- Dashboard tracks: key financials, deal stage, status, follow-ups, notes per deal
- Value: when you have 50+ deals running, tracking becomes impossible without it
- Also useful for team (interns can see prior context without wasting time)
- CRM is highly personal — build for your own workflow, don't use off-the-shelf

### Deal Evaluation Ideas

- One attendee evaluates ~5 CIMs/day using Claude with a scoring framework
- Loses track across days (day 1 grade 3 vs day 5 grade 2 — how do they stack?)
- **Opportunity:** Continuous real-time ranking platform that accumulates evaluations over time
- Kay noted this is something worth building

### Tool Tips Shared

- **Chrome extension** (Claude Co-Work) useful for LinkedIn → Notion data moves
- **LinkedIn scraping** requires screenshots due to blocking
- **Notion** good connector for tracking connections
- **Claude custom instructions** (Settings → General → Preferences): group emphasized importance of setting these up
- One attendee's tip: save good prompts from X/Threads and add to global instructions
- **Wispr Flow** for voice-to-context (Kay using it for this call)

## AI Analysis

### Action Items

1. **Share cleaned notes with group** — Kay offered to put a generic version in WhatsApp, detailed version via email for attendees who request it
2. **Explore continuous deal ranking tool** — idea from the call about real-time CIM evaluation accumulator
3. **Consider personal website for brokers/sellers** — attendee built one in Lovable, good for credibility

### Signals

- **Niche signal:** Multiple searchers struggling with proprietary deal sourcing automation. The scraping/enrichment workflow is an unsolved pain point across the community.
- **Tool signal:** Lovable gaining traction for quick tool builds among searchers. Claude Code skills approach is more advanced than what most are doing (ChatGPT prompts, Lovable builds).
- **Community signal:** Strong interest in AI tooling — this group is actively building, not just curious. Good peer network for Kay.

### Key Insight

Kay's Claude Code skills workflow is significantly more advanced than what peers are doing. Most are either: (a) using ChatGPT with copy-pasted prompts, (b) building one-off tools in Lovable, or (c) writing Python scripts for scraping. None have the integrated system (skills + hooks + vault + pipeline management) that Kay has built. This is a competitive advantage in the search.

### Kay's Takeaways

**Deal evaluation at volume:** The group is largely brokered search — one person mentioned 30 CIMs in a day. That's a completely different evaluation workflow than G&B's current approach. But as G&B's intermediary pipeline matures and deal flow increases, there's a deal-evaluation volume play worth building:
- Auto-scoring CIMs against buy box criteria
- Continuous ranking across days (the "day 1 grade 3 vs day 5 grade 2" problem)
- This is a future enhancement to the deal-evaluation skill, not needed now

**Proprietary scraping as a funnel layer:** G&B's current funnel is conferences + intermediary pipeline + network intros. The broader scraping approach (40K companies from databases, enrichment, auto-filtering) could be a third channel. But the right move is to see what Linkt produces first before building custom scraping. If Linkt gaps emerge, proprietary scraping becomes the fill.

**G&B's system advantage:** Kay's system is significantly more robust than peers'. Most searchers are using ChatGPT prompts, Lovable one-offs, or manual spreadsheets. The integrated skills + hooks + vault + pipeline automation is a genuine competitive edge in search velocity.

---
*Transcribed via Wispr Flow, cleaned and filed by Claude*

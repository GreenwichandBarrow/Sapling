---
name: last30days Skill Configuration
description: Agreed source configuration for last30days skill in niche-intelligence pipeline — no ScrapeCreators, no Brave, no X/Twitter
type: project
---

last30days runs with OpenAI key only (via Codex auth). Available sources: Reddit (OpenAI fallback), Hacker News (free), Polymarket (free).

Claude's built-in WebSearch tool supplements for broader web/news coverage that last30days can't reach.

**Not configured (by choice):**
- ScrapeCreators — skipped, don't need to register just yet (decided 2026-03-16)
- Brave Search — not set up
- X/Twitter (Bird/xAI) — not authenticated
- Bluesky, TikTok, Instagram, YouTube — not configured

**Why:** Minimize API key overhead. Reddit + HN + Polymarket + WebSearch covers enough for M&A/PE niche intelligence. Can revisit ScrapeCreators later if X/Twitter or TikTok/Instagram become valuable sources.

**How to apply:** When spawning the niche-intel-news agent, use `--search reddit,hn,polymarket` flags and supplement with WebSearch tool. Do NOT use `--agent` flag (doesn't exist).

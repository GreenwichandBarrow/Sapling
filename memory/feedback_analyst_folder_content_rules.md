---
name: Analyst- and broker-facing docs never leak salary, IRR, LP count, peer LOIs, operator strategy
description: Hard rule for buy-boxes, scorecards, briefs, and any operational doc that lands in the analyst folder or could be shared with brokers. Strip internal economics + competitive intel before write.
type: feedback
originSessionId: c0375c4c-6be2-4191-9f4b-0e97e59a3de4
---
**Rule:** Operational docs that land in the analyst folder (currently Camilla, future analysts) or could be shared with brokers / intermediaries / external recipients MUST NOT contain:

- **Kay's personal compensation** ($300K operating CEO salary, equity grant terms, etc.)
- **Investor return hurdles** (35 percent IRR, MOIC targets, waterfall structures)
- **LP count or LP names** ("twelve investors," named investor list)
- **Peer-searcher confidential intel** (specific peer LOIs, peer deal terms, peer thesis details — even depersonalized via "a peer searcher" — these are confidential investor-relationship knowledge)
- **Operator strategy details that reveal G&B's playbook** ("operator's commute radius," "post-close CEO of Deal 1," explicit succession path, channel infrastructure references like JJ-Call-Only or DealsX or specific source types Kay is using)
- **Internal financial derivations** ("$2M floor is set to support $300K + debt service + 35 percent IRR" — even if individual values are removed, the formula leaks the structure)

**Why:** Analyst folder is shared with the analyst Kay employs. Buy-boxes shared with brokers go into intermediary inboxes. Both audiences are NOT investors and have no need-to-know on internal economics, LP details, peer LOIs, or strategic-positioning context. Leaking these things (a) breaks the trust boundary with peers / brokers, (b) creates HR/comp-confidentiality issues with current and future analysts, (c) prematurely shows G&B's hand to broker counterparties before the deal-relationship is established. Most G&B-canonical docs (Services Buy Box, Insurance Buy Box, SaaS Buy Box) follow this rule by default — they end at criteria + STRICTLY CONFIDENTIAL with NO entity-framing footer at all.

**How to apply:**
- Before writing any buy-box, scorecard, brief, one-pager, or analyst-facing doc, mirror the canonical template structure. The Services Buy Box (Drive doc id `14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc`) is the reference: title + updated date + scope description + criteria sections + STRICTLY CONFIDENTIAL. NO "G&B is X" framing footer. NO "rationale" paragraphs that explain why the criteria exist.
- If a "rationale" or "context" paragraph feels necessary, ask: would I want the analyst, a broker, or a peer searcher reading this? If no, drop it.
- The financial-floor math derivation belongs in INVESTOR docs only (quarterly investor update, capital-call deck, LP report) — never in operational docs.
- The peer-searcher LOI examples (Marble & Granite Fabrication, etc.) belong in private session notes / strategy decks reviewed only by Kay + investors — never in operational docs.
- Channel-infrastructure references (JJ-Call-Only, DealsX, deal-aggregator OPPORTUNISTIC routing, Sourcing Sheet `Type` column) belong in skill files / internal infrastructure docs — never in analyst or broker-facing docs.
- When in doubt, write the criteria-only minimum and stop.

**Caught:** 2026-05-04 broker buy-box build. Initial draft included a FOOTER paragraph mentioning $300K operating CEO salary + 35 percent investor return hurdle + twelve investors + holding-company framing + operator's commute radius + peer-searcher LOI on Marble and Granite Fabrication + JJ-Call-Only channel reference. Kay's response: "you have listed my salary and many other things that are completely inappropriate." This memory exists so it never happens twice. Related: `feedback_kay_ceo_deal_1_not_allocator` (don't conflate Charter aspirational framing with current-state operational docs), `feedback_no_name_in_deliverables` (no first-name in prose).

---
schema_version: "1.0.0"
date: 2026-05-04
type: context
title: "G&B Broker-Channel Opportunistic Buy Box"
tags: ["date/2026-05-04", "context", "topic/buy-box", "topic/broker-channel", "topic/deal-aggregator", "topic/acquisition-criteria", "source/claude"]
---

# G&B Broker-Channel Opportunistic Buy Box

Vault snapshot of the broker-channel buy box. Mirrors the Drive doc (to be created in Block 4 on 2026-05-04). Source content lives at [[outputs/2026-05-04-broker-channel-buy-box-draft]].

This buy box is INTERNAL. Used by [[deal-aggregator]] to filter scraped broker listings, and by the team to know what to say YES to when a broker pings with an opportunity. NOT for owner-facing outreach.

## Locked rules (do not re-litigate)

- **Geography:** NY, NJ, PA, CT (matches existing Axial buyside filter per [[project_axial_buyside_filter_state]]).
- **Industry:** AGNOSTIC. Broker channel is opportunistic by definition. Industry strictness applies only to proprietary channels.
- **Financial floor:** $2M EBITDA practical floor + 15 percent margin (NOT $1M / 12 percent. The relaxed-floor approach was rejected on 2026-05-03 per [[feedback_broker_channel_opportunistic_floor]]).
- **Revenue band:** $5M to $50M.
- **Hard excludes intact:** California ([[feedback_no_california]]), lending ([[feedback_no_lending]]), carve-outs ([[feedback_no_carveouts]]), fashion (per Guillermo 1/15 call).
- **Channel scope:** applies only to source `Type` values `Email-only broker`, `Newsletter blast`, `Advisory + Deal Platform`, `Marketplace + Email`, `Email-only broker + Buyer Portal` per [[deal-aggregator]] SKILL.md OPPORTUNISTIC routing table.

## Why $2M / 15 percent is constraint-driven

Per [[feedback_deal_screen_300k_salary_15pct_margin]]: $300K operator salary + senior debt service (typical 5x EBITDA, 50-60 percent debt at 8-10 percent interest) + 35 percent investor IRR hurdle do not pencil below $2M EBITDA. The financial gate is a hard constraint driven by math. It does not relax by source, channel, or niche.

## Section list of the Drive doc draft (with rationale)

1. **Title block + Purpose.** Names the channel scope explicitly. Distinguishes from proprietary-channel buy boxes.
2. **Data Availability Rule.** Carried verbatim from Services Buy Box. Missing data is never grounds to auto-reject.
3. **Geography (Hard Gate).** NY/NJ/PA/CT. Explains rationale via operator commute radius and Axial parity.
4. **Industry (Agnostic, Intentional).** The defining adaptation. Explicit caveat that industry-agnostic posture is intentional FOR BROKER CHANNEL ONLY. Cites the Marble and Granite Fabrication peer-searcher LOI as the proof point.
5. **Financial Gate.** $5M-$50M revenue, $2M EBITDA floor, 15 percent margin minimum, 5+ years operating history preferred. Explicit "constraint-driven, not source-driven" line.
6. **Structural.** B2B / B2B2C, independent ownership, full or majority sale, owner-transition viable.
7. **Hard Excludes (auto-reject).** CA, lending, carve-outs, fashion, franchises, restaurants, manufacturing, physician practices, construction, seasonal, PE-backed roll-ups. One-line rationale per item.
8. **Soft Preferences.** Owner near retirement, recurring revenue, real estate optional, B2B preferred, customer concentration cap, mission-critical, management layer.
9. **What We Say YES To (Broker-Facing Decision Rule).** Six-point checklist. The action layer. This is the operational rule when a broker pings.
10. **What We Say NO To.** Explicit no-fits to save broker time. Mirrors the hard-exclude list in plain language.
11. **Channel Application.** Names the five source `Type` values that route to this buy box. Wires it into the [[deal-aggregator]] routing table.
12. **Footer.** $300K operator salary + debt service math one-liner. Capital credibility framing (twelve investors, single-name-drop pattern). No fund/search-fund/vehicle language per [[feedback_no_search_fund_language_intermediaries]]. "Holding company in formation" is the chosen phrasing.
13. **Versioning + Strictly Confidential stamp.** Updated date, version 1.0.

## Adaptations from the Services Buy Box format

The Services Buy Box (Drive doc `14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc`) was the template. Adaptations made for broker channel:

1. **Industry section flipped from hard-excludes-list to "agnostic, intentional".** Services doc lists industry hard-excludes; broker doc opens industry but keeps the hard-exclude list as a separate section. Required because the whole point of the broker channel is opportunistic cross-industry exposure.
2. **Added "What We Say YES To" + "What We Say NO To" sections.** Services doc is screen-criteria only. Broker doc adds an explicit broker-facing decision rule because brokers ping us conversationally and the team needs a quick six-point check, not a screen matrix.
3. **Added "Channel Application" section.** Services doc applies to all niches. Broker doc must name the exact source `Type` values that route here vs to a niche buy box. Required for [[deal-aggregator]] routing.
4. **Tightened financial floor from $1.5M EBITDA / 10 percent margin (Services) to $2M EBITDA / 15 percent margin.** This aligns with the consolidated buy box at [[buy-box]] and the math at [[feedback_deal_screen_300k_salary_15pct_margin]]. The looser Services-doc thresholds are stale relative to the post-2026-04-30 lock.
5. **Added owner-transition language (30 to 90 day handover).** Services doc is silent on transition. Broker doc surfaces it because brokers will ask.
6. **Added Footer with capital-credibility framing.** Services doc ends at "Strictly Confidential" with no positioning copy. Broker doc adds a footer because the buy-box doc may surface to brokers themselves at some point and it should read as serious money even when not.
7. **Added Versioning line.** Services doc shows a single "Updated" date. Broker doc shows version + updated date so future revisions can be tracked cleanly.

## Linking back

- Source draft (paste-into-Drive content): [[outputs/2026-05-04-broker-channel-buy-box-draft]]
- Channel routing logic: [[deal-aggregator]] SKILL.md OPPORTUNISTIC table (lines 137-146 as of 2026-05-04)
- Sister buy boxes: Services (Drive `14hf5QaKtcP_Um0u_P0LZyUM_zvv7haWVVkgGmRL9iyc`), Insurance (Drive `1lkxntRwn3FOPXig86qF36eNyUS0BfbMumfNuIyInD-M`), SaaS (Drive `1I8r8w0FPJUepfBxM6HM7V_q4ibmitybIBF6w6sMQumU`)
- Master buy box (consolidated): [[buy-box]]

## Kay needs to confirm

Items where the draft made a defensible call but the rule was not explicitly locked. Flag for confirmation in Block 4 before pasting to Drive:

1. **Owner-transition window: 30 to 90 days.** [[feedback_broker_channel_opportunistic_floor]] says "owner-transition viable, 30-90 day handover, no irreplaceable founder dependency". Carried as-is. Confirm: is 90 days the right ceiling, or should it be 180 days for broker channel (where deals come in opportunistically and may need longer transitions)?
2. **Operating history: 5 plus years preferred (not required).** Services doc says "5+ years operating history" as a structural item; consolidated [[buy-box]] says "10+ years preferred" with a 5-year exception. Draft uses "5 plus years preferred" as a soft preference. Confirm.
3. **Customer concentration cap: 15 percent in soft preferences.** Consolidated [[buy-box]] makes this a hard gate ("No single customer >15%"). Draft moves it to soft preference for broker channel because data is often undisclosed at first ping. Confirm: hard or soft for broker channel?
4. **Real estate optional.** Not in any prior memory. Inferred from typical lower-mid-market broker listings often bundling owner-occupied real estate. Draft says "real estate component is fine but not required". Confirm.
5. **PE-backed roll-up plays in hard excludes.** Task brief said "no PE-backed, no roll-up plays". Draft puts both in the hard-exclude list as one item. Confirm framing.
6. **Footer capital-credibility line: "backed by twelve investors".** [[feedback_no_search_fund_language_intermediaries]] permits the "twelve investors" framing as the single-name-drop pattern. Draft uses it. Confirm.
7. **Industry hard-excludes list completeness.** Draft pulled from Services Buy Box + consolidated [[buy-box]] + memory hard-rules. Specifically excludes: California, lending, carve-outs, fashion, franchises, restaurants, capital-intensive manufacturing, physician practices, construction, seasonal, PE-backed roll-ups. Confirm none missing (e.g., cannabis, defense, gambling).

## Status

- 2026-05-04: Draft created (this file + sibling output). Drive doc creation deferred to Block 4 (11:45am-1pm).
- After Block 4: [[deal-aggregator]] SKILL.md to be updated with the new Drive doc ID under the OPPORTUNISTIC routing table. Until then, broker-channel listings continue to route to the matching niche buy box.

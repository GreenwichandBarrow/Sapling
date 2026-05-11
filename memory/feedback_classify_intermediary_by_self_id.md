---
name: Classify intermediaries by firm self-identification, not by analyst inference
description: When sorting an intermediary onto the right tab (Brokers / Investment Bankers / Industry Lawyers / etc.), the canonical signal is what the firm calls itself on its homepage hero — NOT a guess based on deal-size band, IBBA membership, or back-of-envelope category fit. Self-ID first, deal-size second.
type: feedback
originSessionId: eadbe8c6-1597-404d-a31b-5cedebba7005
---
When classifying intermediaries for tab placement on the Intermediary Target List (or any equivalent categorization), use the firm's own homepage self-identification as the primary signal — with one critical refinement Kay locked in 2026-05-04 PM:

**M&A Advisors = Business Brokers, NOT Investment Bankers.** The "M&A Advisor" / "M&A Advisory" label belongs on the Brokers tab, not the IB tab. The IB tab is reserved for firms that explicitly self-identify with the "Investment Bank" or "Investment Banking" label, typically backed by FINRA/SIPC registration and bulge-bracket-style positioning.

- Hero text says "Business Brokers" / "M&A Business Brokers" / "M&A Advisor" / "M&A Advisory" / "Mergers & Acquisitions Advisory" → **Brokers tab**
- Hero text says "Investment Bank" / "Investment Banking" (explicit label) → **Investment Bankers tab**
- Hero text says "Trust + Wealth Planning" → **Family Offices** (or DELETE if not relevant)
- Hero text says "Tax / Audit / Advisory" → **CPAs**
- And so on for the other tabs

**Why this matters (2026-05-04 lesson):** The first validation pass auto-promoted firms to the IB tab based on the analyst-inferred rule "LMM platforms doing $5M-$50M EBITDA = IB-tier." That rule is wrong because it ignores how the firm POSITIONS itself in the market. Two examples from today:
- **Gottesman Company** — does $5-25M EBITDA "M&A advisory" deals, looks IB-shaped on paper, but their hero literally reads *"Sell Your Business with America's International Network of M&A Business Brokers."* They sell themselves as brokers. They go on the Brokers tab.
- **Woodbridge / Mariner** — also LMM-tier, but their hero explicitly draws the broker/IB line: *"Mariner specializes in mid-sized and more complex transactions… Business brokers usually focus on smaller Main Street companies."* They self-identify as IB. Stays on IB tab.

Same deal-size band, opposite self-ID. The deal-size proxy is unreliable.

**How to apply:**
- When validating any intermediary list against tab placement, the canonical check is: web-fetch the firm's homepage and look at the hero text + about-page positioning.
- IBBA membership ≠ broker-by-default. Some IBBA firms self-ID as IBs.
- "Investment banking" in the firm's services list ≠ IB-by-default — many brokers offer "investment banking advisory" as a service line. Read the *primary* self-description.
- Cross-tab dups (same firm on multiple tabs) — resolve by firm self-ID, not by which tab the analyst put it on first.
- When in doubt → flag for Kay's eye, don't auto-promote.

Source: 2026-05-04 broker-channel build. Kay flagged the Gottesman misclassification ("clearly not an IB") after the validation subagent's Batch B move put Gottesman on IB. Reverted Gottesman + Basso (Gottesman-affiliated principal) back to Brokers tab. Woodbridge stayed on IB after spot-check confirmed self-ID.

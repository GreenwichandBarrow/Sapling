---
name: Missing data is not a filter — apply criteria only to disclosed fields
description: In the deal-aggregator (and anywhere a buy-box is applied), missing data on a listing does not grounds for auto-rejection. Apply each criterion only when the field is disclosed; absence flags for review, not filter-out.
type: feedback
originSessionId: 848374e5-1268-4868-935b-ca7f12026b58
---
When applying any buy-box criterion (revenue band, EBITDA floor, margin floor, ownership disclosure, operating history, etc.), a missing field on the deal listing is **never grounds to auto-reject the deal**. Apply each filter only when the listing actually discloses the corresponding field.

- Disclosed + passes → deal passes the criterion
- Disclosed + fails → deal fails the criterion (reject or flag per the doc's rule)
- **Not disclosed → deal does NOT fail; it is flagged for further review**

This rule applies across all three buy-box docs (Services, Insurance, SaaS) and governs how the scan subagent interprets every filter line.

**Why:** 2026-04-21 — Kay set this explicitly during buy-box QA: "Note if a deal does not have an item on the buy box; that is not grounds to filter out that deal. It could potentially still pass." Broker teasers are uneven; a specialty insurance teaser often won't disclose EBITDA margin, a small coffee-equipment teaser often won't disclose GRR. Treating missing data as a fail would shrink the funnel below what the market actually signals, and would cost real deals.

**How to apply:**
1. When scoring a listing against a buy-box filter, check first whether the field is disclosed
2. If yes, apply the filter (auto-reject only if disclosed-and-below)
3. If no, mark the field as "Not disclosed — flag for review" and continue scoring against remaining criteria
4. A deal with several "not disclosed" fields but no disclosed-and-failed fields still passes the buy-box gate — it goes to Kay for review with the missing-data flag visible
5. Surface "most-missing" fields in the weekly performance log (feeds Friday calibration): if 60% of teasers fail to disclose X, the filter for X is effectively unenforceable at scan and the skill should expect most X-gates to be soft

**Where codified:**
- Top of G&B Services Buy Box 4.21.26 (Drive)
- Top of G&B Insurance Buy Box 4.21.26 (Drive)
- Top of G&B SaaS Buy Box 4.21.26 (Drive)
- Deal-aggregator SKILL.md scoring logic (to be wired next)

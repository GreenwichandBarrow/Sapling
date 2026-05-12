---
name: kay-outbound-includes-admin-alias
description: Email-intelligence + relationship-manager Gmail outbound scans must search BOTH from:kay.s@greenwichandbarrow.com AND from:admin@greenwichandbarrow.com — single-address scans miss replies and produce false "needs reply" surfaces
metadata:
  type: feedback
---

Kay's Gmail outbound replies are sent from EITHER `kay.s@greenwichandbarrow.com` OR `admin@greenwichandbarrow.com` (the work alias). Any skill that scans Kay's outbound to verify whether she replied to a contact MUST search both addresses. Single-address scans (the current default in `email-intelligence` and `relationship-manager`) produce false positives where the artifact claims "no Kay-outbound to this contact" when she replied via the other alias.

**Why:** 2026-05-12 morning briefing surfaced "Reply to Allison Allen PWIPM Council ask — carried 5+ days, escalating" as an open commitment-debt because the 6:50am relationship-manager Gmail probe used `from:kay.s@greenwichandbarrow.com to:{contact}` and found nothing. Kay confirmed she had actually replied on 2026-05-11 13:55 from `admin@greenwichandbarrow.com` (visible in the thread metadata when read manually). The thread `19df3f96ae20451b` ("Women's Forum First Timers") showed the reply clearly — the scan didn't catch it because the From-address filter was too narrow. Same family-of-bug suspected for any other Gmail-silence finding in either artifact.

Related but distinct: `feedback_email_intel_check_kay_outbound_first.md` requires cross-referencing Kay's outbound on a thread before flagging it "needs reply." That rule is correct but assumed a single From address — this rule expands the search predicate.

**How to apply:**
- In `email-intelligence` (`<gmail_scanning>` Outbound Email Scan): replace `gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:2d" --json --max 50` with a query that ORs both aliases: `from:(kay.s@greenwichandbarrow.com OR admin@greenwichandbarrow.com) newer_than:2d`, OR run two scans and merge results.
- In `relationship-manager` (`<action_verification>`): replace `gog gmail search "from:kay.s@greenwichandbarrow.com to:{contact_email} newer_than:14d"` with `from:(kay.s@greenwichandbarrow.com OR admin@greenwichandbarrow.com) to:{contact_email} newer_than:14d`.
- Any future skill that probes "did Kay reply" must use the same OR pattern. If Kay adds another alias (e.g., a niche-specific sender), append it here and propagate.
- The Gmail search OR syntax requires parentheses around the alias group; test with `--plain --max 5` before deploying.

If a future probe returns zero and you're about to surface a "missing reply" claim, double-check the thread metadata (`gog gmail thread get {thread_id} --plain`) before surfacing — the thread view shows the actual sender on each message and is authoritative.

Precipitating trace: `brain/context/relationship-status-2026-05-12.md` System Status Alerts section ("Gmail outbound 2-day window scan completed. No new substantive Kay-outbound to cadence-surfaced contacts...") which missed Allison Allen entirely because of this gap.

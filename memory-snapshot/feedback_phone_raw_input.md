---
name: Phone numbers must use RAW input mode
description: Never use USER_ENTERED for phone numbers on Google Sheets — +1 prefix causes #ERROR!
type: feedback
---

Phone numbers MUST be written to Google Sheets with `--input RAW`. Never use `USER_ENTERED`.

**Why:** Phone numbers from Apollo often start with `+1`. Google Sheets interprets `+1` as a formula prefix in USER_ENTERED mode, producing `#ERROR!` in cells. This broke 40 phone numbers on JJ's call log tabs on April 7.

**How to apply:** Any gog sheets update/append that writes phone numbers → always use `--input RAW`. Also strip `+1` prefix and reformat to `(XXX) XXX-XXXX` before writing.

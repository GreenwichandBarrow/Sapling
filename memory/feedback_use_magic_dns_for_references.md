---
name: Use Magic DNS for host references
description: When referencing hosts/services in configs, scripts, docs, or commands, prefer Tailscale Magic DNS names over raw IPs or public DNS — for security
type: feedback
originSessionId: 82171e9c-e7db-4fed-b99b-f6d140c0874a
---
When referencing any host, service, or endpoint (in scripts, configs, docs, command examples, or conversation), prefer **Tailscale Magic DNS names** over raw IP addresses or public DNS hostnames.

**Why:** Security. Magic DNS keeps traffic on the Tailnet (encrypted, identity-authenticated, not reachable from the public internet) instead of routing over public IPs that can be scanned, spoofed, or logged by intermediaries. Raw IPs in committed files also leak network topology.

**How to apply:**
- Writing a script that calls another machine → use `<machine-name>` (Magic DNS) not `100.x.y.z` or a public hostname.
- Documenting how to reach a service → reference the Magic DNS name.
- Ad-hoc curl/ssh/etc. in conversation → use Magic DNS.
- If a raw IP or public hostname is unavoidable (external API, third-party service), that's fine — the rule is about machines/services on Kay's Tailnet.
- If unsure whether a target has a Magic DNS name, ask before defaulting to IP.

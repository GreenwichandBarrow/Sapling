#!/bin/bash
# deal-aggregator-fingerprint.sh
# Cross-day dedup helper for deal-aggregator.
#
# Usage:
#   check FINGERPRINT            → prints "DUP" if seen within 30 days, else "NEW"
#   add   FINGERPRINT SOURCE URL → appends fingerprint record with today's date
#   hash  INDUSTRY REVBAND GEO   → prints SHA-1 fingerprint (normalized)
#
# Store: /Users/kaycschneider/Documents/AI Operations/brain/context/deal-aggregator-fingerprints.jsonl

set -euo pipefail

STORE="/Users/kaycschneider/Documents/AI Operations/brain/context/deal-aggregator-fingerprints.jsonl"
TTL_DAYS=30

normalize() {
    # lowercase, trim, collapse whitespace
    printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | awk '{$1=$1}1' | sed 's/[[:space:]]\+/ /g'
}

hash_fingerprint() {
    local industry="$1" revband="$2" geo="$3"
    local combined
    combined="$(normalize "$industry")|$(normalize "$revband")|$(normalize "$geo")"
    printf '%s' "$combined" | shasum -a 1 | awk '{print $1}'
}

check_fingerprint() {
    local fp="$1"
    if [[ ! -f "$STORE" ]]; then
        echo "NEW"
        return 0
    fi
    local cutoff
    cutoff="$(date -u -v-${TTL_DAYS}d +%Y-%m-%d)"
    # grep for the fingerprint; if found, check if date is within TTL
    local found
    found=$(grep -F "\"company_hash\":\"$fp\"" "$STORE" | tail -1 || true)
    if [[ -z "$found" ]]; then
        echo "NEW"
        return 0
    fi
    local seen_date
    seen_date=$(printf '%s' "$found" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('date_first_seen',''))")
    if [[ "$seen_date" < "$cutoff" ]]; then
        echo "NEW"
    else
        echo "DUP"
    fi
}

add_fingerprint() {
    local fp="$1" source="$2" url="$3" industry="${4:-}" revband="${5:-}" ebitdaband="${6:-}" geography="${7:-}"
    local today
    today="$(date -u +%Y-%m-%d)"
    mkdir -p "$(dirname "$STORE")"
    touch "$STORE"
    python3 -c "
import json
entry = {
    'date_first_seen': '$today',
    'source': '''$source''',
    'company_hash': '$fp',
    'industry': '''$industry''',
    'revenue_band': '''$revband''',
    'ebitda_band': '''$ebitdaband''',
    'geography': '''$geography''',
    'listing_url': '''$url'''
}
print(json.dumps(entry, ensure_ascii=False))
" >> "$STORE"
    echo "OK"
}

case "${1:-}" in
    hash)
        shift
        hash_fingerprint "$@"
        ;;
    check)
        shift
        check_fingerprint "$@"
        ;;
    add)
        shift
        add_fingerprint "$@"
        ;;
    *)
        echo "Usage: $0 {hash|check|add} ARGS" >&2
        exit 2
        ;;
esac

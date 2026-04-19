# Migration: output 1.1.0 → 1.2.0

**Schema:** output
**From:** 1.1.0
**To:** 1.2.0
**Generated:** 2026-04-19

## Changelog

Added optional skill_origin (which skill produced output) and kay_approved (Kay explicit approval flag) to power the skill-output portfolio and self-maintaining golden examples loop

## Detection

Files matching:
- `schema_version: 1.1.0`

## Transformation Rules

**Source pattern:**
```yaml
schema_version: 1.1.0
```

**Target pattern:**
```yaml
schema_version: 1.2.0
```

## Field Mappings

| Old Field | New Field | Transform |
|-----------|-----------|-----------|
| schema_version | schema_version | Update to 1.2.0 |

---
*Review and complete the transformation rules above.*

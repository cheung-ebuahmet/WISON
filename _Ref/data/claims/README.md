# Claims — Claims & Variation Tracking

> **Status**: Placeholder — awaiting first claim/variation record
> **Purpose**: Structured tracking of claims, variations, and EOT requests per contract

## Planned Schema (to be formalized as `_Ref/schema/claim-schema.yaml`)

Each claim YAML will capture:

```yaml
claim:
  id: "CL-12.1-001"
  contract: "12.1-CCECC-MEI-I"
  type: variation | eot | delay | disruption | other
  status: notice | submitted | under_review | determined | disputed | closed
  notice_date: YYYY-MM-DD
  submission_date: YYYY-MM-DD
  amount_claimed: null
  amount_determined: null
  eot_days_claimed: null
  eot_days_granted: null
  description: "..."
  linked_issues: []
```

## Relationship

- Driven by `contracts/*.yaml` → `claims.variation_notice_days`, `claims.eot_notice_days` (time-bar tracking)
- Feeds into `commercial-analysis/risk-register.md`
- Each claim links to its contract via `contract` field

## Why Separate from contracts/

Contracts YAMLs capture the contractual *framework* (notice periods, caps, procedures). Claims capture individual *instances* — each variation, EOT request, or dispute event. One contract → many claims.

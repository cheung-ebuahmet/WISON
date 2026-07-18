# Packages — Work Package Summaries

> **Status**: Placeholder — awaiting population
> **Purpose**: Per-package structured data (scope summaries, milestone dates, resource plans)

## Planned Contents

| File | Description |
|------|-------------|
| `*-scope.yaml` | Per-package scope boundary & deliverables |
| `*-milestones.yaml` | Key dates per package |
| `cross-package-matrix.md` | Interface / dependency matrix across packages |

## Relationship

- Feeds into `contracts/*.yaml` → `structure.exhibits` for scope attachment cross-references
- Input to `commercial-analysis/back-to-back-matrix.md`

## Why Separate from contracts/

Contracts YAMLs capture the legal/contractual terms. Packages capture the operational work-package view — same project, different lens.

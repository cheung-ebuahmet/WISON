# Wison Knowledge Graph — Schema &amp; Maintenance Guide

## Overview

The Wison Knowledge Graph connects all structured data assets (contracts, clauses, correspondence, prices, exhibits, risks, issues) into a single queryable network.

**Location**: `D:\Wison\_Ref\data\graph\`

| File | Format | Size (auto) | Description |
|------|--------|-------------|-------------|
| `nodes.yaml` | YAML | ~112 nodes | All entity nodes with metadata |
| `edges.yaml` | YAML | ~139 edges | All relationships (directed) |
| `graph.json` | JSON | ~112n, 139e | NetworkX-compatible export |
| `README.md` | Markdown | this file | Schema documentation |

## Quick Start

```bash
# Stats
python _tools/query_graph.py --stats

# Look up a node
python _tools/query_graph.py --node 12.1 --depth 2

# Find what a contract contains
python _tools/query_graph.py --node 10.1 --depth 1

# Impact analysis
python _tools/query_graph.py --impact AMDT-12.1-01

# Compare commercial values
python _tools/query_graph.py --compare LD
python _tools/query_graph.py --compare Payment

# Path finding
python _tools/query_graph.py --from SLT-5312-WSN-CCE-0020 --to COC-4.3.7

# Clause history
python _tools/query_graph.py --report clause-history --clause GCS-17

# Search
python _tools/query_graph.py --search "Delay LD"

# List by type
python _tools/query_graph.py --type risk
python _tools/query_graph.py --list-types
```

## Node Types

| Type | Count | ID Pattern | Example |
|------|-------|------------|---------|
| `contract` | 4 | `{id}` | `12.1`, `10.1` |
| `clause` | 40 | `{FRAMEWORK}-{ref}` | `MEI-GCS-17`, `CIVIL-COC-4.2.4` |
| `exhibit` | 27 | `{contract}-EXH-{ref}` | `12.1-EXH-Exh-D` |
| `commercial_value` | 18 | `{CATEGORY}-{contract}` | `LD-DELAY-12.1` |
| `correspondence` | 3 | `SLT-5312-WSN-...` | `SLT-5312-WSN-CCE-0020` |
| `issue` | 2 | `ISSUE-{slug}` | `ISSUE-PM-缺位` |
| `risk` | 11 | `RISK-{slug}` | `RISK-保留金释放不对称` |
| `amendment` | 1 | `AMDT-{contract}-{seq}` | `AMDT-12.1-01` |
| `clause_library` | 4 | `KO-{name}` | `KO-Delay-LD` |
| `framework` | 2 | `FRAMEWORK-{name}` | `FRAMEWORK-MEI` |

## Edge Types

| Type | Direction | Meaning |
|------|-----------|---------|
| `has_clause` | contract → clause | Contract contains this clause |
| `has_exhibit` | contract → exhibit | Contract has this attachment |
| `has_value` | contract → commercial_value | Financial term of contract |
| `has_issue` | contract → issue | Active dispute/breach |
| `governs` | parent → contract | Upstream governs downstream |
| `flows_down` | clause → clause | EPC clause passed to subcon |
| `amends` | amendment → contract | Amendment modifies contract |
| `affects` | amendment → clause/exhibit | Amendment changes this |
| `references` | correspondence → clause | Letter cites this clause |
| `relates_to` | correspondence → contract | Letter is about this contract |
| `involves` | correspondence → company | Letter involves this party |
| `exposes_to` | contract → risk | Contract creates this risk |
| `uses_framework` | contract → framework | Contract uses this framework |

## Two Frameworks

```
MEI Framework                  Civil Framework
─────────────                  ────────────────
12.1 CCECC MEI I               10.1 CCECC Civil II
12.2 TCC MEI II                10.2 TCC Civil I/III
99 LONGTAIDI FOB

Structure:                     Structure:
  Agrmt 1-13                     FOA 1-3
  SCS 1-7                        COC ~29 sections
  GCS 1.0-50.0                  Attachments 1-7
  Exh A-K                      

Clause IDs:                    Clause IDs:
  MEI-GCS-{n}                   CIVIL-COC-{n}
  MEI-SCS-{n}
```

## Node ID Naming Convention

```
{FRAMEWORK}-{DOCUMENT}-{NUMBER}[-{SUBNUMBER}]

Examples:
  MEI-GCS-17         → MEI framework, General Conditions, Clause 17
  MEI-SCS-5-6        → MEI framework, Special Conditions, Clause 5.6
  CIVIL-COC-4-2-4    → Civil framework, COC, Sub-Clause 4.2.4
  12.1-EXH-Exh-D     → Contract 12.1, Exhibit D
  LD-DELAY-12.1      → Commercial value: Delay LD for 12.1
  SLT-5312-WSN-CCE-0020 → Correspondence by ref number
  AMDT-12.1-01       → Amendment 01 to contract 12.1
  KO-Delay-LD        → Clause library knowledge object
  RISK-{slug}        → Risk from risk register
  ISSUE-{slug}       → Active issue from Commercial Issue Register
```

## Rebuilding the Graph

The graph is compiled from source YAML/MD/DOCX files. To rebuild:

```bash
python _tools/build_graph.py
```

This will re-read all source files and regenerate `nodes.yaml`, `edges.yaml`, and `graph.json`.

**Source data locations** (read by `build_graph.py`):

| Source | Path |
|--------|------|
| Contract YAMLs | `_Ref/data/contracts/*.yaml` |
| Correspondence YAMLs | `_Ref/data/correspondence/*.yaml` |
| Clause Library | `_Ref/data/clause-library/*.md` |
| Back-to-Back Matrix | `_Ref/data/commercial-analysis/back-to-back-matrix.md` |
| Risk Register | `_Ref/data/commercial-analysis/risk-register.md` |
| Amdt 01 | `Subcon_Payments/12.1 CCECC - MEI Pkg I/Contract/02_Amdt 01/Amdt 01_MEI Pkg I (Revised) .docx` |

## When to Rebuild

Rebuild after:
- Adding/updating any contract YAML
- Adding/updating any correspondence YAML
- Creating a new clause library KO
- A new amendment is executed
- A new issue or risk is registered

The graph is a **compiled asset** — it does not need to be manually edited. All facts live in the source YAMLs; the graph is a derived view.

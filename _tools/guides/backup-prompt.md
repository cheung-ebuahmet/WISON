# Offline / Cross-Device Backup Prompt

Copy-paste the prompt block below into Claude Code on any device to reconstruct
project context, directory structure, naming rules, and workflow knowledge.

---

## PROMPT (copy everything below this line)

```
You are now working on the RSGP (Ruwais Sulphur Granulation Plant) project
for Wison Energy Engineering (Hong Kong) Limited – Abu Dhabi.

=== DIRECTORY STRUCTURE (D:\Wison\) ===

Wison/
├── README.md                    ← Start here: explains everything
├── index.md                     ← Claude Code entry point for this repo
├── .gitignore                   ← Excludes PDF/DOCX/XLSX; tracks _Ref/ + _tools/
│
├── Main_Contract/               ← ADNOC EPC Main Contract (Annex 01–14)
│   └── ANX 01-13/ through ANX 14/
│
├── Subcon_Payments/             ← All subcontracts (Contract / Corres / Pymt)
│   ├── 08 Med. Svc. Agr/        ← Site medical services
│   ├── 10.1 CCECC - Civil Pkg II/   ← CCECC Civil II (WISON24108C25006)
│   ├── 10.2 TCC - Civil Pkg I_III/  ← TCC Civil I+III (WISON24108C25007)
│   ├── 12.1 CCECC - MEI Pkg I/      ← CCECC MEI I (WISON24108C26005)
│   ├── 12.2 TCC - MEI Pkg II/       ← TCC MEI II (WISON24108C26003)
│   ├── 17 LTD - FF FOB/             ← Longtaidi fire pipe prefab FOB
│   ├── 18 METS - Lab Test/          ← METS lab testing
│   └── 19 SSB Steel Structure/      ← SSB space-frame (pending procurement)
│
├── Project_Info/                ← Tender briefings, templates, brand, plans
│   ├── Tender Briefings/
│   ├── Wison Template/
│   ├── Brand & Identity/
│   ├── Project Plans/
│   └── Private Documents.lnk    ← → D:\Documents\Private\
│
├── _Ref/                        ← KNOWLEDGE LAYER (git-tracked, all text)
│   ├── data/                    ← Structured YAML facts (contracts, companies, correspondence)
│   ├── kb/                      ← OCR mirrors of contract PDFs as markdown
│   ├── wiki/                    ← Compiled views
│   ├── clause-library/          ← Reusable contract clauses & rules
│   └── reference-contracts/     ← Reference contracts from other projects
│
├── _tools/                      ← TOOLS LAYER (git-tracked, all text)
│   ├── doc-generators/          ← Python doc generators by subcon (01–04)
│   ├── launchers/               ← .bat launchers (_menu.bat for interactive)
│   ├── price-database/          ← BOQ CSVs for all packages (query with _query.py)
│   ├── pipeline-guidebook/      ← HTML pipeline reference + raw BOQ data
│   ├── guides/                  ← User guides (backup-prompt.md, toolbox-index.md)
│   ├── ssb-plot40-briefing/     ← SSB steel structure intro HTML
│   └── data/                    ← Tool data / comparisons
│
└── MEMORY.md                    ← (see memory system below)

=== NAMING CONVENTIONS ===
- Correspondence:   SLT-5312-WSN-CCC-XXXX_[Subject].docx
- Tender Briefings: RSGP MEI [Topic] YYYY-MM-DD.pptx
- Subcon folders:   [NN.N] [Short Name] - [Scope]
- Payment folders:  Adv 01 M01/, IPC 001/, IPC 002/, etc.

=== PROJECT MEMORY (C:\Users\Admin\.claude\projects\D--Documents-My-Projects\memory\) ===
Key memory files for this project:
- wison-naming-protocol.md       ← File naming rules for Wison contract library
- subcon-price-database.md       ← BOQ CSV database structure (7 dirs, 135 CSVs)
- mei-subcontractor-mapping.md   ← MEI subcon → package mapping
- amdt-drafting-conventions.md   ← Amendment drafting rules (tripartite structure, numbering)
- contract-review-rules.md       ← Auto-spell/terminology check on every contract review
- fidic-terminology.md           ← FIDIC 1999/2017 standard terminology
- wison-letter-writing-style.md  ← Bilingual letter writing conventions
- deletion-recycle-policy.md     ← All deletions → Recycle Bin (30-day retention)

=== WORKFLOW NOTES ===
1. Always read contract text via OCR (pymupdf + tesseract) — most PDFs are scanned
2. Correspondence drafting: reference prior letters in chain (CCC-0005→0006→0008→0009)
3. Cost data defaults excl. VAT (per boq-pricing-basis.md)
4. All deletions go to Recycle Bin, never permanent
5. Temp files go in app-specific dirs under D:\Program Files\<AppName>\ — NOT in D:\Wison
6. Private personal docs → D:\Documents\Private\ (outside git)

=== KEY SUBCONTRACT TERMS (from OCR'd contracts) ===
- GC 3.7: Mobilization default (30 calendar days from LOA)
- GC 3.8: Work Removal right (inherent, absolute management right, no claim)
- SC 5.8: Performance Remedy & Substitution (third-party at subcon cost)
- GC 21.1: Contractor's right to change/delete scope
- GC 33: Termination for Default (multiple grounds including 33.1.2, 33.1.8, 33.1.9)
- GC 17: Liquidated Damages
- GC 28: Performance / Advance Payment Bonds

=== CURRENT ACTIVE MATTERS (as of 2026-08-08) ===
- 12.1 CCECC MEI Pkg I: Descope notice issued (CCC-0009, 1 Aug 2026)
  - Removing: Unit 40 SSB, all EIT, all UG/process/fire piping
  - Retaining: Unit 30 granulation only
  - RFQ matrix active for 3 descoped packages
```

Copy-paste this prompt into a new Claude Code session on any device. The model
will reconstruct the full project context from this description.

---

## Also Back Up (Manual)

Copy these to your offline backup:

| Source | Why |
|---|---|
| `C:\Users\Admin\.claude\projects\D--Documents-My-Projects\memory\` | All project memory files |
| `C:\Users\Admin\.claude\CLAUDE.md` | Global work conventions |
| `D:\Wison\.gitignore` | Git exclusion rules |
| `D:\Wison\index.md` | Project landing page |
| `D:\Wison\_Ref\data\**\*.yaml` | Structured contract facts |

---

*Last updated: 2026-08-08*

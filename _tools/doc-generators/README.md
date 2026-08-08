# Wison Document Generators

All `gen_*.py` scripts centralized here. Output lands in project folders, not here.

## Quick Launch

Double-click `_menu.bat` → pick a number.

## Index

| # | Script | Project | Output |
|---|--------|---------|--------|
| 1 | `gen_deficiency_report.py` | URG/CCECC | `SLT-5312-WSN-CCC-MEI1_PERF_DEFICIENCY_RPT.docx` |
| 2 | `gen_letter_0008.py` | URG/CCECC | `SLT-5312-WSN-CCC-0008_FINAL CURE NOTICE MEI PKG I.docx` |
| 3 | `gen_final_contract.py` | METS Lab | `SUBCONTRACT - Lab Testing Services - FINAL.docx` |
| 4 | `gen_seal_contract.py` | LONGTAIDI | `用印简要说明_LONGTAIDI预制合同.docx` |
| 5 | `gen_loa_longtaidi.py` | LONGTAIDI LOA | `LOA - LONGTAIDI (from v0428).docx` |
| 6 | `gen_seal_loa.py` | LONGTAIDI LOA | `用印简要说明_LOA_LONGTAIDI.docx` |
| 7 | `gen_po_night_shift.py` | Med Services | `Medical_Service_PO_Night_Shift.docx` |
| 8 | `gen_service_instruction.py` | Med Services | `Medical_Service_Additional_Personnel_Request.docx` |
| 9 | `gen_subcontractor_matrix.py` | Wison Tools | `Subcontractor-Matrix.md` |

## Finding Scripts from Project Folders

Each project folder has a `_RUN_gen_xxx.bat` that launches the script here.
Double-click it, or run from CLI. No logic lives in project folders.

## Rules for New Scripts

1. Place `gen_*.py` here under the right project subfolder.
2. Use **absolute paths** for templates and output — no `__file__`-relative.
3. Create a `_RUN_gen_xxx.bat` launcher in the project output folder.
4. Update this README and `_menu.bat`.

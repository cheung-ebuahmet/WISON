#!/usr/bin/env python3
"""
Generate Subcontractor Application for Payment — Excel Workbook (.xlsx)
For Deliverable-Based and Professional Service Subcontracts

Corporate EPC Standard — International Best Practice
Multi-sheet professional workbook with auto-calculation fields.
"""

import datetime
from openpyxl import Workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side, NamedStyle, numbers
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# ═══════════════════════════════════════════════════════════════════════════════
# STYLE CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

DARK_BLUE   = "0B2A4A"
MED_BLUE    = "1F5C8A"
LIGHT_BLUE  = "D6E8F7"
ALT_ROW     = "F2F6FA"
ACCENT_GREY = "6B7B8D"
BORDER_GREY = "BFCBD7"
WHITE       = "FFFFFF"
DARK_GREY   = "333F4D"
RED_CONF    = "CC0000"
GOLD_BG     = "FFF3E0"
TOTAL_BG    = "E8EEF4"

FONT_TITLE      = Font(name='Calibri', size=18, bold=True, color=DARK_BLUE)
FONT_SUBTITLE   = Font(name='Calibri', size=11, italic=True, color=ACCENT_GREY)
FONT_SECTION    = Font(name='Calibri', size=14, bold=True, color=MED_BLUE)
FONT_HEADER     = Font(name='Calibri', size=9, bold=True, color=WHITE)
FONT_BODY       = Font(name='Calibri', size=10, color=DARK_GREY)
FONT_BODY_SM    = Font(name='Calibri', size=9, color=DARK_GREY)
FONT_BODY_BOLD  = Font(name='Calibri', size=10, bold=True, color=DARK_BLUE)
FONT_LABEL      = Font(name='Calibri', size=10, bold=True, color=DARK_BLUE)
FONT_SMALL      = Font(name='Calibri', size=8, color=ACCENT_GREY)
FONT_CONF       = Font(name='Calibri', size=7, bold=True, color=RED_CONF)
FONT_NOTE       = Font(name='Calibri', size=9, italic=True, color=ACCENT_GREY)
FONT_LEGEND     = Font(name='Calibri', size=8, color=ACCENT_GREY)

FILL_HEADER     = PatternFill(start_color=DARK_BLUE, end_color=DARK_BLUE, fill_type='solid')
FILL_ALT        = PatternFill(start_color=ALT_ROW, end_color=ALT_ROW, fill_type='solid')
FILL_TOTAL      = PatternFill(start_color=TOTAL_BG, end_color=TOTAL_BG, fill_type='solid')
FILL_SUB        = PatternFill(start_color="EDF2F9", end_color="EDF2F9", fill_type='solid')
FILL_EPC        = PatternFill(start_color=GOLD_BG, end_color=GOLD_BG, fill_type='solid')
FILL_LIGHT_BLUE = PatternFill(start_color=LIGHT_BLUE, end_color=LIGHT_BLUE, fill_type='solid')
FILL_WHITE      = PatternFill(start_color=WHITE, end_color=WHITE, fill_type='solid')

ALIGN_LEFT    = Alignment(horizontal='left', vertical='center', wrap_text=True)
ALIGN_CENTER  = Alignment(horizontal='center', vertical='center', wrap_text=True)
ALIGN_RIGHT   = Alignment(horizontal='right', vertical='center', wrap_text=True)

BORDER_THIN = Border(
    left=Side(style='thin', color=BORDER_GREY),
    right=Side(style='thin', color=BORDER_GREY),
    top=Side(style='thin', color=BORDER_GREY),
    bottom=Side(style='thin', color=BORDER_GREY),
)

BORDER_BOTTOM_THICK = Border(
    bottom=Side(style='medium', color=DARK_BLUE),
)


def apply_cell(ws, row, col, value, font=FONT_BODY, fill=None, alignment=ALIGN_LEFT, border=BORDER_THIN, number_format=None):
    """Apply a value and full formatting to a single cell."""
    cell = ws.cell(row=row, column=col, value=value)
    cell.font = font
    if fill:
        cell.fill = fill
    cell.alignment = alignment
    cell.border = border
    if number_format:
        cell.number_format = number_format
    return cell


def apply_header_row(ws, row, headers, start_col=1):
    """Apply dark-blue header styling to a row."""
    for i, h in enumerate(headers, start=start_col):
        apply_cell(ws, row, i, h, font=FONT_HEADER, fill=FILL_HEADER, alignment=ALIGN_CENTER)


def apply_data_row(ws, row, data, start_col=1, alt=False, font=FONT_BODY_SM, alignments=None):
    """Apply data-row styling, with optional alternating background."""
    fill = FILL_ALT if alt else None
    for i, val in enumerate(data, start=start_col):
        al = alignments[i - start_col] if alignments and (i - start_col) < len(alignments) else ALIGN_LEFT
        apply_cell(ws, row, i, val, font=font, fill=fill, alignment=al)


def set_col_widths(ws, widths, start_col=1):
    """Set column widths from a list of (col_letter_or_index, width) or just list of widths."""
    for i, w in enumerate(widths, start=start_col):
        ws.column_dimensions[get_column_letter(i)].width = w


def add_section_title(ws, row, number, title):
    """Insert a section title at the given row. Returns next available row."""
    apply_cell(ws, row, 1, f"SECTION {number}", font=FONT_SECTION, fill=None, alignment=ALIGN_LEFT, border=Border())
    apply_cell(ws, row, 2, title.upper(), font=FONT_SECTION, fill=None, alignment=ALIGN_LEFT, border=Border())
    # underline effect via bottom border on next row across all used columns
    for c in range(1, 20):
        apply_cell(ws, row + 1, c, "", font=FONT_BODY_SM, fill=None, border=BORDER_BOTTOM_THICK)
    ws.merge_cells(start_row=row + 1, start_column=1, end_row=row + 1, end_column=16)
    return row + 2


def add_note_row(ws, row, text, merge_end_col=16):
    """Add an italic instruction note."""
    apply_cell(ws, row, 1, text, font=FONT_NOTE, fill=None, alignment=ALIGN_LEFT, border=Border())
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=merge_end_col)
    return row + 1

# ═══════════════════════════════════════════════════════════════════════════════
# CREATE WORKBOOK
# ═══════════════════════════════════════════════════════════════════════════════

wb = Workbook()
today = datetime.date.today()
today_str = today.strftime("%d-%b-%Y")

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 0 — COVER & DOCUMENT CONTROL
# ═══════════════════════════════════════════════════════════════════════════════

ws_cover = wb.active
ws_cover.title = "Cover"
ws_cover.sheet_properties.tabColor = DARK_BLUE
set_col_widths(ws_cover, [3, 25, 20, 18, 20, 18, 4])

r = 1
# Confidential banner
apply_cell(ws_cover, r, 2, "CONFIDENTIAL", font=FONT_CONF, alignment=ALIGN_LEFT, border=Border()); r += 1
r += 1

# Title
apply_cell(ws_cover, r, 2, "SUBCONTRACTOR APPLICATION FOR PAYMENT", font=FONT_TITLE, alignment=ALIGN_LEFT, border=Border())
r += 1
apply_cell(ws_cover, r, 2, "For Deliverable-Based and Professional Service Subcontracts", font=FONT_SUBTITLE, alignment=ALIGN_LEFT, border=Border())
r += 2

# Separator
apply_cell(ws_cover, r, 2, "", font=FONT_SMALL, border=BORDER_BOTTOM_THICK)
ws_cover.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6); r += 2

# Document Control
apply_cell(ws_cover, r, 2, "DOCUMENT CONTROL", font=FONT_SECTION, alignment=ALIGN_LEFT, border=Border()); r += 1
doc_ctrl_headers = ["Document Number", "Revision", "Issue Date", "Status"]
apply_header_row(ws_cover, r, doc_ctrl_headers, start_col=2)
r += 1
apply_data_row(ws_cover, r, ["[XXXX-XXX-XXX-XXX]", "[A01]", today_str, "ISSUED FOR USE"], start_col=2)
r += 2

# Revision History
apply_cell(ws_cover, r, 2, "REVISION HISTORY", font=FONT_SECTION, alignment=ALIGN_LEFT, border=Border()); r += 1
rev_h = ["Rev", "Date", "Description of Revision", "Prepared By", "Checked By", "Approved By"]
apply_header_row(ws_cover, r, rev_h, start_col=2)
for ri, rd in enumerate([
    ["A01", today_str, "Issued for Use — Standard Template", "[Name]", "[Name]", "[Name]"],
    ["—", "—", "—", "—", "—", "—"],
    ["—", "—", "—", "—", "—", "—"],
]):
    apply_data_row(ws_cover, r + 1 + ri, rd, start_col=2, alt=(ri % 2 == 1))

r += 6
# Footer note
apply_cell(ws_cover, r, 2, "Controlled Document  |  Uncontrolled When Printed  |  © EPC Contractor", font=FONT_SMALL, alignment=ALIGN_LEFT, border=Border())

# Freeze & print setup
ws_cover.freeze_panes = 'B8'
ws_cover.sheet_properties.pageSetUpPr = None

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — PROJECT INFORMATION
# ═══════════════════════════════════════════════════════════════════════════════

ws_pi = wb.create_sheet("1. Project Info")
ws_pi.sheet_properties.tabColor = MED_BLUE
set_col_widths(ws_pi, [3, 28, 40, 3])

r = 1
r = add_section_title(ws_pi, r, "1", "PROJECT INFORMATION")
r += 0

proj_fields = [
    ("Project Name",             "[Insert Project Name]"),
    ("Project Number",           "[Insert Project Number]"),
    ("Client / Employer",        "[Insert Client Name]"),
    ("EPC Contractor",           "[Insert EPC Contractor Name]"),
    ("Subcontractor",            "[Insert Subcontractor Name]"),
    ("Subcontract Agreement No.","[Insert Agreement Number]"),
    ("Application Number",       "[Payment Application No. XXX]"),
    ("Application Date",         today_str),
    ("Payment Period (From)",    "[DD-Mon-YYYY]"),
    ("Payment Period (To)",      "[DD-Mon-YYYY]"),
    ("Currency",                 "[USD / EUR / CNY / AED / …]"),
    ("Contract Value",           None),  # will be formula-linked from Commercial Summary
]
for label, value in proj_fields:
    apply_cell(ws_pi, r, 2, label, font=FONT_LABEL, alignment=ALIGN_LEFT, border=Border())
    val = value if value else "[See Commercial Summary]"
    apply_cell(ws_pi, r, 3, val, font=FONT_BODY, alignment=ALIGN_LEFT, border=Border())
    r += 1

ws_pi.freeze_panes = 'B8'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — COMMERCIAL SUMMARY (the core financial sheet with formulas)
# ═══════════════════════════════════════════════════════════════════════════════

ws_cs = wb.create_sheet("2. Commercial Summary")
ws_cs.sheet_properties.tabColor = "C00000"  # dark red for financial importance
set_col_widths(ws_cs, [3, 8, 42, 18, 22, 3])

r = 1
r = add_section_title(ws_cs, r, "2", "COMMERCIAL SUMMARY")
r += 1

# Legend
apply_cell(ws_cs, r, 3, "All amounts in Contract Currency unless otherwise stated.", font=FONT_NOTE, alignment=ALIGN_LEFT, border=Border()); r += 1

comm_headers = ["Row", "Description", "Amount", "Remarks"]
apply_header_row(ws_cs, r, comm_headers, start_col=2)
r += 1

# Row definitions with formulas
# Columns: B=Row label, C=Description, D=Amount (formula or input), E=Remarks
comm_data = [
    # (row_label, description, amount_formula_or_placeholder, remarks)
    ("A", "Original Contract Value",              None, ""),
    ("B", "Approved Variations (Cumulative)",      None, "Ref: VO-XXX to VO-XXX"),
    ("C", "Current Contract Value  (A + B)",       "=D{rA}+D{rB}", ""),  # formula refs use row numbers
    ("D", "Previous Certified Amount (Cumulative)", None, "Up to App. No. XXX"),
    ("E", "Current Application Amount",            None, "THIS APPLICATION"),
    ("F", "Cumulative Certified Amount  (D + E)",  "=D{rD}+D{rE}", ""),
    ("G", "Retention  (___% per Subcontract)",     None, None),
    ("H", "Advance Recovery (if applicable)",      None, None),
    ("I", "Taxes  (VAT / GST / WHT, if applicable)", None, None),
    ("J", "NET AMOUNT DUE  (E − G − H − I)",      "=D{rE}-D{rG}-D{rH}-D{rI}", ""),
    ("K", "Remaining Contract Balance  (C − F)",   "=D{rC}-D{rF}", ""),
]

# We need to know the actual row numbers for formula compilation
formula_map = {}  # row_label -> actual excel row number
data_start_row = r

for i, (rl, desc, amt, remarks) in enumerate(comm_data):
    actual_row = r
    formula_map[rl] = actual_row

    apply_cell(ws_cs, r, 2, rl, font=FONT_BODY_BOLD, alignment=ALIGN_CENTER)
    apply_cell(ws_cs, r, 3, desc, font=FONT_BODY, alignment=ALIGN_LEFT)
    val_or_formula = amt if amt else "[XXX,XXX,XXX.XX]"
    apply_cell(ws_cs, r, 4, val_or_formula, font=FONT_BODY if amt else FONT_BODY_SM,
               alignment=ALIGN_RIGHT, number_format='#,##0.00')
    apply_cell(ws_cs, r, 5, remarks if remarks else "", font=FONT_BODY_SM, alignment=ALIGN_LEFT)
    r += 1

# Now resolve formulas using actual row numbers
for i, (rl, desc, amt, remarks) in enumerate(comm_data):
    actual_row = data_start_row + i
    if amt and "=D{" in str(amt):
        resolved = amt
        for key, rn in formula_map.items():
            resolved = resolved.replace(f"{{r{key}}}", str(rn))
        ws_cs.cell(row=actual_row, column=4).value = resolved
        ws_cs.cell(row=actual_row, column=4).font = Font(name='Calibri', size=10, bold=True, color=DARK_BLUE)
        ws_cs.cell(row=actual_row, column=4).number_format = '#,##0.00'

# Bold & highlight the NET AMOUNT DUE row (J)
net_row = formula_map["J"]
for c in range(2, 6):
    cell = ws_cs.cell(row=net_row, column=c)
    cell.font = Font(name='Calibri', size=11, bold=True, color=DARK_BLUE)
    cell.fill = FILL_LIGHT_BLUE

# Highlight the Total row (C = Current Contract Value)
total_row_c = formula_map["C"]
for c in range(2, 6):
    cell = ws_cs.cell(row=total_row_c, column=c)
    cell.fill = FILL_TOTAL

# Highlight Cumulative row F
cum_row_f = formula_map["F"]
for c in range(2, 6):
    cell = ws_cs.cell(row=cum_row_f, column=c)
    cell.fill = FILL_TOTAL

r += 1
apply_cell(ws_cs, r, 3, "Note:  Shaded cells contain formulas — do not overwrite.  Input cells (white) should be populated from the Subcontract Agreement and approved Variations.", font=FONT_NOTE, alignment=ALIGN_LEFT, border=Border())
ws_cs.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)

ws_cs.freeze_panes = 'B9'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — CONTRACT DELIVERABLES
# ═══════════════════════════════════════════════════════════════════════════════

ws_del = wb.create_sheet("3. Deliverables")
ws_del.sheet_properties.tabColor = "2E7D32"
set_col_widths(ws_del, [
    3,   # A: spacer
    5,   # B: No.
    38,  # C: Deliverable Description
    18,  # D: Ref No.
    6,   # E: Rev
    12,  # F: Contract Requirement
    14,  # G: Previous Submission
    14,  # H: Current Submission
    16,  # I: Current Status
    16,  # J: Acceptance Status
    20,  # K: Remarks
    3,   # L: spacer
])

r = 1
r = add_section_title(ws_del, r, "3", "CONTRACT DELIVERABLES")
add_note_row(ws_del, r,
    "Instruction: List all contractual deliverables. Use additional rows as required. "
    "Attach Document Transmittal / Acceptance Certificate as supporting evidence."
)
r += 1

del_headers = [
    "No.", "Deliverable Description", "Reference No.", "Rev.",
    "Contract\nRequirement", "Previous\nSubmission", "Current\nSubmission",
    "Current Status", "Acceptance\nStatus", "Remarks"
]
apply_header_row(ws_del, r, del_headers, start_col=2)
r += 1

sample_deliverables = [
    ["1",  "Process Flow Diagram — Unit 100",           "DOC-XXX-001", "A",  "IFR", "23-Jun-2026", "15-Jul-2026", "Submitted", "Accepted", ""],
    ["2",  "P&ID — Unit 200",                           "DOC-XXX-002", "B",  "IFR", "23-Jun-2026", "15-Jul-2026", "Submitted", "Accepted w/ Comments", ""],
    ["3",  "Equipment Data Sheet — P-101A/B",           "DOC-XXX-003", "0",  "IFR", "—",           "15-Jul-2026", "First Submission", "Pending Review", ""],
    ["4",  "Structural Calculation — Pipe Rack",         "DOC-XXX-004", "0",  "IFR", "—",           "—",           "In Progress", "—", ""],
    ["5",  "Vendor Document — VDR-001",                 "DOC-XXX-005", "A",  "IFA", "30-May-2026", "—",           "Vendor Hold", "—", "Awaiting vendor input"],
    ["6",  "Inspection & Test Plan — Welding",           "DOC-XXX-006", "0",  "IFR", "—",           "15-Jul-2026", "Submitted", "Pending Review", ""],
    ["7",  "Factory Acceptance Test Procedure",          "DOC-XXX-007", "0",  "IFA", "—",           "—",           "Not Started", "—", ""],
    ["8",  "Commissioning Procedure — System X",         "DOC-XXX-008", "0",  "IFC", "—",           "—",           "Not Started", "—", ""],
    ["9",  "Training Completion Report",                 "DOC-XXX-009", "0",  "IFR", "—",           "—",           "Not Started", "—", ""],
    ["10", "Final Documentation Dossier",                "DOC-XXX-010", "0",  "IFC", "—",           "—",           "Not Started", "—", ""],
]
# Add empty rows for user to fill
empty_rows = [["", "", "", "", "", "", "", "", "", ""] for _ in range(20)]
all_del_rows = sample_deliverables + empty_rows

for i, dl in enumerate(all_del_rows):
    alts = [ALIGN_CENTER, ALIGN_LEFT, ALIGN_LEFT, ALIGN_CENTER, ALIGN_CENTER,
            ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_LEFT]
    apply_data_row(ws_del, r, dl, start_col=2, alt=(i % 2 == 1), alignments=alts)
    r += 1

r += 1
# Legend
legend = "Status Codes —  IFR = Issued for Review  |  IFA = Issued for Approval  |  IFC = Issued for Construction  |  IFT = Issued for Tender"
apply_cell(ws_del, r, 2, legend, font=FONT_LEGEND, alignment=ALIGN_LEFT, border=Border())
ws_del.merge_cells(start_row=r, start_column=2, end_row=r, end_column=11)

# Data validation for status column (I = col 9)
dv_status = DataValidation(type="list", formula1='"Submitted,In Progress,Not Started,Vendor Hold,First Submission,Re-Submitted,Approved,Rejected"', allow_blank=True)
dv_status.error = "Please select a valid status."
dv_status.errorTitle = "Invalid Status"
ws_del.add_data_validation(dv_status)
dv_status.add(f'I9:I{r}')

# Data validation for acceptance column (J = col 10)
dv_acc = DataValidation(type="list", formula1='"Accepted,Accepted w/ Comments,Pending Review,Returned,Rejected,—"', allow_blank=True)
ws_del.add_data_validation(dv_acc)
dv_acc.add(f'J9:J{r}')

# Data validation for Contract Requirement (F = col 6)
dv_req = DataValidation(type="list", formula1='"IFR,IFA,IFC,IFT"', allow_blank=True)
ws_del.add_data_validation(dv_req)
dv_req.add(f'F9:F{r}')

ws_del.freeze_panes = 'C9'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 4 — CONTRACT MILESTONES
# ═══════════════════════════════════════════════════════════════════════════════

ws_ms = wb.create_sheet("4. Milestones")
ws_ms.sheet_properties.tabColor = "E65100"
set_col_widths(ws_ms, [
    3,   # A: spacer
    5,   # B: No.
    38,  # C: Milestone Description
    10,  # D: Contract Weight %
    12,  # E: Current Status
    14,  # F: Planned Completion
    16,  # G: Actual/Forecast Completion
    20,  # H: Supporting Evidence (Ref.)
    14,  # I: Engineer Certification
    14,  # J: Commercial Acceptance
    3,   # K: spacer
])

r = 1
r = add_section_title(ws_ms, r, "4", "CONTRACT MILESTONES")
add_note_row(ws_ms, r,
    "Instruction: List each contract milestone with its weighted percentage. "
    "Milestone weights must sum to 100%. Attach supporting evidence for each claimed milestone."
)
r += 1

ms_headers = [
    "No.", "Milestone Description", "Contract\nWeight (%)", "Current\nStatus",
    "Planned\nCompletion", "Actual / Forecast\nCompletion",
    "Supporting Evidence\n(Ref. No.)", "Engineer\nCertification", "Commercial\nAcceptance"
]
apply_header_row(ws_ms, r, ms_headers, start_col=2)
r += 1

sample_milestones = [
    ["1", "Kick-off Meeting Completed",                       "5%",  "Achieved",  "01-Jun-2026", "01-Jun-2026", "MOM-XXX-001",  "Certified", "Accepted"],
    ["2", "Engineering Deliverables — Phase 1 (PFD)",          "10%", "Achieved",  "15-Jun-2026", "15-Jun-2026", "DOC-XXX-001",  "Certified", "Accepted"],
    ["3", "Engineering Deliverables — Phase 2 (P&ID)",         "15%", "In Progress","30-Jun-2026", "20-Jul-2026", "DOC-XXX-002",  "Pending",   "Pending"],
    ["4", "Vendor Documents — Batch 1 Submitted",              "10%", "Achieved",  "15-Jul-2026", "10-Jul-2026", "VDR-001~010",  "Certified", "Accepted"],
    ["5", "Factory Acceptance Test — Equipment Package 1",    "20%", "Not Started","15-Aug-2026", "—",           "FAT-PKG1",     "—",         "—"],
    ["6", "Site Acceptance Test Completed",                    "15%", "Not Started","15-Sep-2026", "—",           "SAT-XXX",      "—",         "—"],
    ["7", "Commissioning Support Completed",                   "10%", "Not Started","01-Oct-2026", "—",           "COMM-XXX",     "—",         "—"],
    ["8", "Training Completion",                               "5%",  "Not Started","15-Oct-2026", "—",           "TRG-XXX",      "—",         "—"],
    ["9", "Final Documentation & Close-out",                   "10%", "Not Started","01-Nov-2026", "—",           "FD-XXX",       "—",         "—"],
]
empty_ms_rows = [["", "", "", "", "", "", "", "", ""] for _ in range(12)]
all_ms_rows = sample_milestones + empty_ms_rows

for i, ms in enumerate(all_ms_rows):
    alts = [ALIGN_CENTER, ALIGN_LEFT, ALIGN_CENTER, ALIGN_CENTER,
            ALIGN_CENTER, ALIGN_CENTER, ALIGN_LEFT, ALIGN_CENTER, ALIGN_CENTER]
    apply_data_row(ws_ms, r, ms, start_col=2, alt=(i % 2 == 1), alignments=alts)
    r += 1

# TOTAL row
r_total_ms = r
apply_cell(ws_ms, r, 2, "", font=FONT_BODY_BOLD, fill=FILL_TOTAL, alignment=ALIGN_CENTER)
apply_cell(ws_ms, r, 3, "TOTAL", font=FONT_BODY_BOLD, fill=FILL_TOTAL, alignment=ALIGN_LEFT)
# Formula to sum weight %
weight_data_start = r_total_ms - len(all_ms_rows)  # first data row
apply_cell(ws_ms, r, 4, f"=SUM(D{weight_data_start}:D{r_total_ms - 1})", font=FONT_BODY_BOLD, fill=FILL_TOTAL, alignment=ALIGN_CENTER, number_format='0%')
for c in [5, 6, 7, 8, 9, 10]:
    apply_cell(ws_ms, r, c, "", font=FONT_BODY_BOLD, fill=FILL_TOTAL, alignment=ALIGN_CENTER)
r += 1

# Conditional formatting — highlight if not 100%
# (applied via a note since conditional formatting on formula cells is complex)
apply_cell(ws_ms, r, 2, "⚠ The TOTAL Weight must equal 100%. If not, adjust milestone percentages before submission.", font=FONT_NOTE, alignment=ALIGN_LEFT, border=Border())
ws_ms.merge_cells(start_row=r, start_column=2, end_row=r, end_column=10)

# Data validation
dv_ms_status = DataValidation(type="list", formula1='"Achieved,In Progress,Not Started,Deferred"', allow_blank=True)
ws_ms.add_data_validation(dv_ms_status)
dv_ms_status.add(f'E9:E{r}')

dv_ms_cert = DataValidation(type="list", formula1='"Certified,Pending,Returned,Rejected,—"', allow_blank=True)
ws_ms.add_data_validation(dv_ms_cert)
dv_ms_cert.add(f'I9:I{r}')

dv_ms_comm = DataValidation(type="list", formula1='"Accepted,Accepted w/ Comments,Pending,Rejected,—"', allow_blank=True)
ws_ms.add_data_validation(dv_ms_comm)
dv_ms_comm.add(f'J9:J{r}')

ws_ms.freeze_panes = 'C9'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 5 — SUPPORTING DOCUMENTS
# ═══════════════════════════════════════════════════════════════════════════════

ws_sd = wb.create_sheet("5. Supporting Docs")
ws_sd.sheet_properties.tabColor = "6A1B9A"
set_col_widths(ws_sd, [3, 5, 40, 3, 5, 40, 3])

r = 1
r = add_section_title(ws_sd, r, "5", "SUPPORTING DOCUMENTS")
add_note_row(ws_sd, r, "The following documents are attached in support of this Application for Payment. Check all that apply.")
r += 1

checklist = [
    ("☐", "Deliverable Register"),
    ("☐", "Document Transmittal / Submittal Register"),
    ("☐", "Acceptance Certificate"),
    ("☐", "Progress Report"),
    ("☐", "Completion Certificate"),
    ("☐", "Technical Report"),
    ("☐", "Inspection Report"),
    ("☐", "FAT Report / Certificate"),
    ("☐", "SAT Report / Certificate"),
    ("☐", "Commissioning Report"),
    ("☐", "Performance Test Report / Certificate"),
    ("☐", "Time Sheet / Attendance Record"),
    ("☐", "Invoice"),
    ("☐", "Variation / Change Order Approval"),
    ("☐", "Meeting Minutes"),
    ("☐", "Correspondence / Letter"),
    ("☐", "Photographic Evidence"),
    ("☐", "Others (specify): _______________"),
]

# Split into two columns
half = (len(checklist) + 1) // 2
for i, (box, text) in enumerate(checklist):
    if i < half:
        apply_cell(ws_sd, r + i, 2, box, font=FONT_BODY, alignment=ALIGN_CENTER, border=Border())
        apply_cell(ws_sd, r + i, 3, text, font=FONT_BODY, alignment=ALIGN_LEFT, border=Border())
    else:
        apply_cell(ws_sd, r + i - half, 5, box, font=FONT_BODY, alignment=ALIGN_CENTER, border=Border())
        apply_cell(ws_sd, r + i - half, 6, text, font=FONT_BODY, alignment=ALIGN_LEFT, border=Border())

r += half + 1

# Attachments register
apply_cell(ws_sd, r, 2, "ATTACHMENT REGISTER", font=FONT_SECTION, alignment=ALIGN_LEFT, border=Border()); r += 1
att_headers = ["No.", "Document Title", "Document Number", "Revision", "No. of Pages", "Remarks"]
apply_header_row(ws_sd, r, att_headers, start_col=2)
for ri in range(15):
    apply_data_row(ws_sd, r + 1 + ri, ["", "", "", "", "", ""], start_col=2, alt=(ri % 2 == 1))

ws_sd.freeze_panes = 'B5'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 6 — SUBCONTRACTOR CERTIFICATION
# ═══════════════════════════════════════════════════════════════════════════════

ws_sc = wb.create_sheet("6. Certification")
ws_sc.sheet_properties.tabColor = "0277BD"
set_col_widths(ws_sc, [3, 100, 3])

r = 1
r = add_section_title(ws_sc, r, "6", "SUBCONTRACTOR CERTIFICATION")
r += 1

cert_paras = [
    "The Subcontractor hereby certifies and warrants to the EPC Contractor that:",
    "",
    "(a) All deliverables, documents, data, and information listed in this Application have been completed and submitted in accordance with the requirements of the Subcontract Agreement and all applicable technical specifications, codes, and standards referenced therein;",
    "",
    "(b) All statements, representations, and particulars set forth in this Application and all supporting documents submitted herewith are true, accurate, and complete in all material respects and do not contain any misrepresentation or omission that would render them misleading;",
    "",
    "(c) The milestone progress and deliverable completion claimed herein accurately reflect the actual status of the Services performed as at the date of this Application, and all claimed milestones have been substantially achieved in accordance with the criteria defined in the Subcontract;",
    "",
    "(d) The Services have been performed in accordance with the Project requirements, including all applicable quality assurance, health, safety, environmental, and security requirements specified in the Subcontract and the Project Execution Plan;",
    "",
    "(e) All subcontractor personnel deployed in the performance of the Services possess the qualifications, certifications, and competencies required under the Subcontract;",
    "",
    "(f) This Application for Payment is submitted in good faith and the Subcontractor is entitled to the amount claimed herein in accordance with the terms and conditions of the Subcontract;",
    "",
    "(g) The Subcontractor acknowledges that any certification found to be false, inaccurate, or misleading shall entitle the EPC Contractor to suspend payment, recover any amounts overpaid, and exercise any other rights or remedies available under the Subcontract or at law.",
]
for para in cert_paras:
    apply_cell(ws_sc, r, 2, para, font=FONT_BODY_SM if para else FONT_BODY, alignment=ALIGN_LEFT, border=Border())
    ws_sc.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    ws_sc.row_dimensions[r].height = 10 if para == "" else 20
    r += 1

r += 2

# Certification signature block
apply_cell(ws_sc, r, 2, "CERTIFICATION SIGNATURE", font=FONT_SECTION, alignment=ALIGN_LEFT, border=Border()); r += 1
cert_headers = ["", "Name", "Title / Position", "Signature", "Date"]
apply_header_row(ws_sc, r, cert_headers, start_col=2)
r += 1
apply_data_row(ws_sc, r, ["Certified By\n(Subcontractor Authorized\nRepresentative)", "[Insert Name]", "[Title]", "", "[DD-Mon-YYYY]"], start_col=2)
ws_sc.row_dimensions[r].height = 45

r += 2
apply_cell(ws_sc, r, 2, "Important:  False certification may result in suspension of payment, recovery of overpaid amounts, and exercise of remedies under the Subcontract or at law.", font=FONT_NOTE, alignment=ALIGN_LEFT, border=Border())
ws_sc.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)

ws_sc.freeze_panes = 'B8'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 7 — CONTRACTOR REVIEW
# ═══════════════════════════════════════════════════════════════════════════════

ws_cr = wb.create_sheet("7. Contractor Review")
ws_cr.sheet_properties.tabColor = "BF360C"
set_col_widths(ws_cr, [
    3,   # A
    22,  # B: Review Discipline
    18,  # C: Reviewer Name
    32,  # D: Status
    16,  # E: Certified Amount
    26,  # F: Review Comments
    14,  # G: Review Date
    14,  # H: Signature
    3,   # I
])

r = 1
r = add_section_title(ws_cr, r, "7", "CONTRACTOR REVIEW & CERTIFICATION")
add_note_row(ws_cr, r,
    "Instruction: Each discipline reviewer shall complete their review and indicate their "
    "recommendation. The Commercial / Contracts function shall consolidate all review inputs "
    "before issuing the Payment Certificate."
)
r += 1

review_headers = [
    "Review Discipline", "Reviewer Name", "Status",
    "Certified Amount", "Review Comments", "Review Date", "Signature"
]
apply_header_row(ws_cr, r, review_headers, start_col=2)
r += 1

review_disciplines = [
    "Engineering",
    "Project Management",
    "QA / QC",
    "Planning / Project Controls",
    "HSSE (if applicable)",
    "Construction (if applicable)",
    "Commissioning (if applicable)",
    "Commercial",
    "Contracts",
    "Finance / Cost Control",
]
for i, disc in enumerate(review_disciplines):
    apply_data_row(ws_cr, r, [
        disc, "[Name]",
        "☐ Accepted    ☐ Accepted w/ Comments    ☐ Returned    ☐ Rejected",
        "[Amount]", "", "[DD-Mon-YYYY]", ""
    ], start_col=2, alt=(i % 2 == 1))
    ws_cr.row_dimensions[r].height = 22
    r += 1

r += 1

# Summary
apply_cell(ws_cr, r, 2, "CONSOLIDATED REVIEW SUMMARY", font=FONT_SECTION, alignment=ALIGN_LEFT, border=Border()); r += 1
summary_items = [
    ("Summary Recommendation:", ""),
    ("□ Recommended for Full Payment", ""),
    ("□ Recommended for Partial Payment  →  Amount:", ""),
    ("□ Not Recommended  →  Reason:", ""),
    ("", ""),
    ("Certified Amount for Payment:", "[XXX,XXX,XXX.XX]"),
    ("Payment Certificate Reference:", "[PC-XXX-XXX]"),
    ("Payment Certificate Date:", "[DD-Mon-YYYY]"),
]
for label, val in summary_items:
    apply_cell(ws_cr, r, 2, label, font=FONT_LABEL if label else FONT_BODY, alignment=ALIGN_LEFT, border=Border())
    apply_cell(ws_cr, r, 3, val, font=FONT_BODY, alignment=ALIGN_LEFT, border=Border())
    r += 1

# Data validation for status
dv_review = DataValidation(type="list", formula1='"Accepted,Accepted w/ Comments,Returned,Rejected"', allow_blank=True)
ws_cr.add_data_validation(dv_review)

ws_cr.freeze_panes = 'C9'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 8 — SIGNATURES
# ═══════════════════════════════════════════════════════════════════════════════

ws_sig = wb.create_sheet("8. Signatures")
ws_sig.sheet_properties.tabColor = "37474F"
set_col_widths(ws_sig, [3, 30, 22, 22, 22, 22, 3])

r = 1
r = add_section_title(ws_sig, r, "8", "SIGNATURES")
add_note_row(ws_sig, r,
    "This Application for Payment, when certified by the EPC Contractor, constitutes authorization "
    "for the Contractor to process payment in accordance with the payment terms of the Subcontract "
    "Agreement. Each signatory confirms they have reviewed this application and that all statements "
    "herein are accurate to the best of their knowledge."
)
r += 1

sig_headers = ["Role", "Name", "Company", "Signature", "Date"]
apply_header_row(ws_sig, r, sig_headers, start_col=2)
r += 1

sig_data = [
    # (role, name, company, signature, date, fill_type)
    ("Prepared By\n(Subcontractor)",                 "[Insert Name]", "[Subcontractor]", "", "[DD-Mon-YYYY]", "sub"),
    ("Checked By\n(Subcontractor)",                  "[Insert Name]", "[Subcontractor]", "", "[DD-Mon-YYYY]", "sub"),
    ("Submitted By\n(Subcontractor Authorized Rep.)", "[Insert Name]", "[Subcontractor]", "", "[DD-Mon-YYYY]", "sub"),
    ("", "", "", "", "", "spacer"),
    ("Reviewed By\n(EPC Contractor — Project)",      "[Insert Name]", "[EPC Contractor]", "", "[DD-Mon-YYYY]", "epc"),
    ("Reviewed By\n(EPC Contractor — Commercial)",   "[Insert Name]", "[EPC Contractor]", "", "[DD-Mon-YYYY]", "epc"),
    ("Certified By\n(EPC Contractor — Contracts)",   "[Insert Name]", "[EPC Contractor]", "", "[DD-Mon-YYYY]", "epc"),
    ("Approved By\n(EPC Contractor Authorized Rep.)", "[Insert Name]", "[EPC Contractor]", "", "[DD-Mon-YYYY]", "epc"),
]

for role, name, company, sig, date, row_type in sig_data:
    if row_type == "spacer":
        r += 1
        continue
    fill = FILL_SUB if row_type == "sub" else (FILL_EPC if row_type == "epc" else None)
    apply_data_row(ws_sig, r, [role, name, company, sig, date], start_col=2)
    if fill:
        for c in range(2, 7):
            ws_sig.cell(row=r, column=c).fill = fill
    ws_sig.row_dimensions[r].height = 35
    r += 1

r += 1
apply_cell(ws_sig, r, 2, "LEGEND:", font=FONT_LABEL, alignment=ALIGN_LEFT, border=Border())
apply_cell(ws_sig, r, 3, "Blue = Subcontractor  |  Gold = EPC Contractor", font=FONT_BODY, alignment=ALIGN_LEFT, border=Border())

ws_sig.freeze_panes = 'B9'

# ═══════════════════════════════════════════════════════════════════════════════
# SHEET 9 — GUIDANCE NOTES
# ═══════════════════════════════════════════════════════════════════════════════

ws_gn = wb.create_sheet("Guidance Notes")
ws_gn.sheet_properties.tabColor = ACCENT_GREY
set_col_widths(ws_gn, [3, 110, 3])

r = 1
r = add_section_title(ws_gn, r, "—", "GUIDANCE NOTES FOR COMPLETION")
r += 1

guidance = [
    ("1.  General",
     "This template is designed for deliverable-based and professional service subcontracts. "
     "It shall NOT be used for construction or measured-quantity progress — use a Construction IPC for those. "
     "The template is compatible with FIDIC, NEC, and bespoke EPC subcontract forms."),

    ("2.  Sheet 1 — Project Information",
     "Complete all fields with accurate project data. The Contract Value shall match the Current Contract Value "
     "in Sheet 2 (Commercial Summary). Project Number and Subcontract Agreement Number must match the signed "
     "Subcontract Agreement exactly."),

    ("3.  Sheet 2 — Commercial Summary",
     "This is the financial core of the application. White cells are input cells — populate from the signed "
     "Subcontract Agreement and approved Variation Orders. Blue shaded cells contain formulas — do NOT overwrite. "
     "Retention percentage must match the Subcontract provisions. Advance recovery and tax amounts should be "
     "calculated per the applicable commercial terms."),

    ("4.  Sheet 3 — Deliverables",
     "List every contractual deliverable. If the deliverable list exceeds the rows provided, insert additional "
     "rows above the legend row. Each deliverable entry must be traceable to a specific Subcontract clause or "
     "exhibit. Drop-down validation is provided for Status, Acceptance, and Requirement columns."),

    ("5.  Sheet 4 — Milestones",
     "Milestone weights must sum to exactly 100%. A milestone may only be claimed as 'Achieved' when the "
     "deliverable or event has been formally accepted by the EPC Contractor in writing. 'In Progress' milestones "
     "shall not be claimed unless the Subcontract expressly provides for partial / progress payment against "
     "incomplete milestones."),

    ("6.  Sheet 5 — Supporting Documents",
     "Every claimed milestone and deliverable must be supported by objective evidence. Applications submitted "
     "without supporting documentation will be returned. The Contractor reserves the right to request additional "
     "evidence. Use the Attachment Register at the bottom of the sheet to list all attached documents."),

    ("7.  Sheet 6 — Certification",
     "Must be signed by the Subcontractor's Authorized Representative as defined in the Subcontract Agreement. "
     "An electronic or scanned signature is acceptable unless the Subcontract specifies otherwise."),

    ("8.  Sheet 7 — Contractor Review",
     "The EPC Contractor's discipline reviewers shall complete their respective sections. The Commercial / "
     "Contracts function consolidates all inputs. The Certified Amount in the Consolidated Review Summary "
     "is the amount authorized for payment — this may differ from the Subcontractor's claimed amount."),

    ("9.  Retention",
     "Retention shall be deducted in accordance with the Subcontract. Retention release shall be applied for "
     "separately upon achievement of the retention release milestones specified in the Subcontract (typically: "
     "50% at Provisional Acceptance / Taking-Over; 50% at Final Acceptance / End of Defects Notification Period)."),

    ("10.  Payment Terms",
     "The Contractor shall process certified applications within the period stipulated in the Subcontract "
     "Agreement. Any dispute regarding a certified amount shall be referred to the Parties' respective "
     "commercial representatives for resolution in the first instance."),

    ("11.  Record Keeping",
     "Each payment application and its supporting documents shall be retained by both Parties for the duration "
     "of the Subcontract and any applicable statutory retention period thereafter. Where the Subcontract "
     "requires original documents, the Subcontractor shall provide originals upon request."),
]

for title, text in guidance:
    apply_cell(ws_gn, r, 2, title, font=FONT_LABEL, alignment=ALIGN_LEFT, border=Border())
    ws_gn.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    ws_gn.row_dimensions[r].height = 20
    r += 1
    apply_cell(ws_gn, r, 2, text, font=FONT_BODY_SM, alignment=ALIGN_LEFT, border=Border())
    ws_gn.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    ws_gn.row_dimensions[r].height = 50
    r += 2

ws_gn.freeze_panes = 'B5'

# ═══════════════════════════════════════════════════════════════════════════════
# FINAL PRINT SETTINGS FOR ALL SHEETS
# ═══════════════════════════════════════════════════════════════════════════════

for ws in wb.worksheets:
    ws.page_setup.orientation = 'landscape' if ws.title in ["3. Deliverables", "4. Milestones", "7. Contractor Review"] else 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = None
    ws.print_title_rows = '1:8'  # repeat header rows

# Set Cover to portrait
ws_cover.page_setup.orientation = 'portrait'

# ═══════════════════════════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════════════════════════

output = r"D:\Wison\Project_Info\Wison Template\Non-Wison Template\Subcontractor_Application_for_Payment_Template.xlsx"
wb.save(output)
print(f"[DONE] Excel template saved to: {output}")

import os
os.startfile(output)

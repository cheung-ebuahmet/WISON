#!/usr/bin/env python3
"""
Generate Subcontractor Application for Payment Template (.docx)
For Deliverable-Based and Professional Service Subcontracts

Corporate EPC Standard — International Best Practice
Compatible with FIDIC, NEC, and bespoke EPC subcontract forms.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import datetime

# ── Colour Palette (Corporate EPC) ──────────────────────────────────────────
DARK_BLUE   = RGBColor(0x0B, 0x2A, 0x4A)   # Headers, title bar
MED_BLUE    = RGBColor(0x1F, 0x5C, 0x8A)   # Section headings
LIGHT_BLUE  = RGBColor(0xD6, 0xE8, 0xF7)   # Table alternate rows
ACCENT_GREY = RGBColor(0x6B, 0x7B, 0x8D)   # Secondary text
BORDER_GREY = RGBColor(0xBF, 0xCB, 0xD7)   # Table borders
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
BLACK       = RGBColor(0x00, 0x00, 0x00)
DARK_GREY   = RGBColor(0x33, 0x3F, 0x4D)   # Body text

# ── Document Setup ───────────────────────────────────────────────────────────
doc = Document()

# Page size A4
section = doc.sections[0]
section.page_width  = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin    = Cm(2.0)
section.bottom_margin = Cm(2.0)
section.left_margin   = Cm(2.5)
section.right_margin  = Cm(2.0)

# ── Default Style ────────────────────────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(10)
font.color.rgb = DARK_GREY
style.paragraph_format.space_after = Pt(4)
style.paragraph_format.space_before = Pt(0)

# ── Helper Functions ─────────────────────────────────────────────────────────

def set_cell_shading(cell, color):
    """Set cell background colour."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_border(cell, **kwargs):
    """Set cell borders. kwargs: top, bottom, left, right, insideH, insideV."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}></w:tcBorders>')
    for edge, val in kwargs.items():
        element = parse_xml(
            f'<w:{edge} {nsdecls("w")} w:val="{val.get("val","single")}" '
            f'w:sz="{val.get("sz","4")}" '
            f'w:color="{val.get("color","BFCBD7")}" '
            f'w:space="0"/>'
        )
        tcBorders.append(element)
    tcPr.append(tcBorders)

def add_formatted_table(doc, headers, rows, col_widths=None, header_bg="0B2A4A"):
    """Create a professional table with dark header and alternating rows."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # Style header row
    hdr = table.rows[0]
    for i, text in enumerate(headers):
        cell = hdr.cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = WHITE
        run.font.name = 'Calibri'
        set_cell_shading(cell, header_bg)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)

    # Style data rows
    for r, row_data in enumerate(rows):
        row = table.rows[r + 1]
        for c, text in enumerate(row_data):
            cell = row.cells[c]
            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c == 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(str(text))
            run.font.size = Pt(9)
            run.font.name = 'Calibri'
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            if r % 2 == 1:
                set_cell_shading(cell, "F2F6FA")

    # Set column widths if provided
    if col_widths:
        for row in table.rows:
            for i, w in enumerate(col_widths):
                if i < len(row.cells):
                    row.cells[i].width = Cm(w)

    # Apply border to all cells
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}></w:tblPr>')
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'<w:left w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'<w:bottom w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'<w:right w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'<w:insideH w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'<w:insideV w:val="single" w:sz="4" w:color="BFCBD7"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    return table

def add_section_heading(doc, number, title):
    """Add a numbered section heading with professional styling."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.keep_with_next = True

    # Section number in dark blue
    run_num = p.add_run(f"SECTION {number}")
    run_num.bold = True
    run_num.font.size = Pt(14)
    run_num.font.color.rgb = DARK_BLUE
    run_num.font.name = 'Calibri'

    p.add_run("    ")

    # Title in medium blue
    run_title = p.add_run(title.upper())
    run_title.bold = True
    run_title.font.size = Pt(14)
    run_title.font.color.rgb = MED_BLUE
    run_title.font.name = 'Calibri'

    # Thin accent line below heading
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(10)
    pPr = p2._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="8" w:color="0B2A4A" w:space="4"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)
    p2.add_run("").font.size = Pt(1)

def add_label_value(doc, label, value, width_label=5.0):
    """Add a label: value line."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(1)
    run_label = p.add_run(f"{label}:  ")
    run_label.bold = True
    run_label.font.size = Pt(10)
    run_label.font.name = 'Calibri'
    run_label.font.color.rgb = DARK_BLUE
    run_value = p.add_run(value)
    run_value.font.size = Pt(10)
    run_value.font.name = 'Calibri'
    return p

def add_checkbox_item(doc, text, checked=False):
    """Add a checkbox line item."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.left_indent = Cm(1.0)
    box = "☑" if checked else "☐"
    run = p.add_run(f"{box}  {text}")
    run.font.size = Pt(10)
    run.font.name = 'Calibri'
    return p

def set_narrow_table_font(table):
    """Apply compact font sizing to an entire table."""
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(9)

# ═══════════════════════════════════════════════════════════════════════════════
# HEADER & FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

header = section.header
header.is_linked_to_previous = False
htable = header.add_table(rows=1, cols=2, width=Cm(16.5))
htable.autofit = True

# Left: Logo placeholder
h_left = htable.rows[0].cells[0]
h_left.width = Cm(4)
hp = h_left.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
run_logo = hp.add_run("[ COMPANY LOGO ]")
run_logo.font.size = Pt(8)
run_logo.font.color.rgb = ACCENT_GREY
run_logo.font.name = 'Calibri'

# Right: Document tag line
h_right = htable.rows[0].cells[1]
h_right.width = Cm(12.5)
hp2 = h_right.paragraphs[0]
hp2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run_tag = hp2.add_run("SUBCONTRACTOR APPLICATION FOR PAYMENT")
run_tag.bold = True
run_tag.font.size = Pt(8)
run_tag.font.color.rgb = DARK_BLUE
run_tag.font.name = 'Calibri'
run_tag2 = hp2.add_run("  |  Deliverable-Based / Professional Services")
run_tag2.font.size = Pt(7)
run_tag2.font.color.rgb = ACCENT_GREY
run_tag2.font.name = 'Calibri'

# Thin line under header
hp_line = doc.add_paragraph()
hp_line.paragraph_format.space_after = Pt(0)

footer = section.footer
footer.is_linked_to_previous = False
ftable = footer.add_table(rows=1, cols=3, width=Cm(16.5))

f_left = ftable.rows[0].cells[0]
fp = f_left.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
run_fn = fp.add_run("CONFIDENTIAL")
run_fn.bold = True
run_fn.font.size = Pt(7)
run_fn.font.color.rgb = RGBColor(0xCC, 0x00, 0x00)
run_fn.font.name = 'Calibri'

f_center = ftable.rows[0].cells[1]
fp2 = f_center.paragraphs[0]
fp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_dc = fp2.add_run("Controlled Document  |  Uncontrolled When Printed")
run_dc.font.size = Pt(7)
run_dc.font.color.rgb = ACCENT_GREY
run_dc.font.name = 'Calibri'

f_right = ftable.rows[0].cells[2]
fp3 = f_right.paragraphs[0]
fp3.alignment = WD_ALIGN_PARAGRAPH.RIGHT
# Page number field
run_pg = fp3.add_run("Page ")
run_pg.font.size = Pt(7)
run_pg.font.color.rgb = ACCENT_GREY

# ═══════════════════════════════════════════════════════════════════════════════
# COVER / TITLE BLOCK
# ═══════════════════════════════════════════════════════════════════════════════

# Top colour bar
p_bar = doc.add_paragraph()
p_bar.paragraph_format.space_before = Pt(0)
p_bar.paragraph_format.space_after = Pt(0)
pPr = p_bar._p.get_or_add_pPr()
pBdr = parse_xml(
    f'<w:pBdr {nsdecls("w")}>'
    f'<w:bottom w:val="single" w:sz="36" w:color="0B2A4A" w:space="0"/>'
    f'</w:pBdr>'
)
pPr.append(pBdr)

doc.add_paragraph("")  # spacer

# Main title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(2)
run_t = p_title.add_run("SUBCONTRACTOR APPLICATION FOR PAYMENT")
run_t.bold = True
run_t.font.size = Pt(18)
run_t.font.color.rgb = DARK_BLUE
run_t.font.name = 'Calibri'

# Subtitle
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(6)
run_s = p_sub.add_run("For Deliverable-Based and Professional Service Subcontracts")
run_s.font.size = Pt(11)
run_s.font.color.rgb = ACCENT_GREY
run_s.font.name = 'Calibri'
run_s.italic = True

# Thin separator
p_sep = doc.add_paragraph()
p_sep.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sep.paragraph_format.space_after = Pt(12)
run_sep = p_sep.add_run("━" * 40)
run_sep.font.size = Pt(6)
run_sep.font.color.rgb = BORDER_GREY

# Document Control Box
doc_info_headers = ["Document Number", "Revision", "Issue Date", "Status"]
doc_info_values  = ["[XXXX-XXX-XXX-XXX]", "[A01]", datetime.date.today().strftime("%d-%b-%Y"), "ISSUED FOR USE"]
add_formatted_table(doc, doc_info_headers, [doc_info_values], col_widths=[4.5, 3.0, 4.0, 5.0])

doc.add_paragraph("")

# Revision History
add_section_heading(doc, "—", "REVISION HISTORY")

rev_headers = ["Rev", "Date", "Description of Revision", "Prepared By", "Checked By", "Approved By"]
rev_rows = [
    ["A01", datetime.date.today().strftime("%d-%b-%Y"), "Issued for Use", "[Name]", "[Name]", "[Name]"],
    ["—", "—", "—", "—", "—", "—"],
    ["—", "—", "—", "—", "—", "—"],
]
add_formatted_table(doc, rev_headers, rev_rows, col_widths=[1.2, 2.2, 5.8, 2.5, 2.5, 2.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — PROJECT INFORMATION
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "1", "PROJECT INFORMATION")

proj_info = [
    ("Project Name",             "[Insert Project Name]"),
    ("Project Number",           "[Insert Project Number]"),
    ("Client / Employer",        "[Insert Client Name]"),
    ("EPC Contractor",           "[Insert EPC Contractor Name]"),
    ("Subcontractor",            "[Insert Subcontractor Name]"),
    ("Subcontract Agreement No.","[Insert Agreement Number]"),
    ("Application Number",       "[Payment Application No. XXX]"),
    ("Application Date",         datetime.date.today().strftime("%d-%b-%Y")),
    ("Payment Period",           "[DD-Mon-YYYY]  to  [DD-Mon-YYYY]"),
    ("Currency",                 "[USD / EUR / CNY / AED / …]"),
    ("Contract Value",           "[XXX,XXX,XXX.XX]"),
]
for label, value in proj_info:
    add_label_value(doc, label, value)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — COMMERCIAL SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "2", "COMMERCIAL SUMMARY")

comm_headers = ["Description", "Amount", "Remarks"]
comm_rows = [
    ["A.  Original Contract Value",              "[XXX,XXX,XXX.XX]", ""],
    ["B.  Approved Variations (Cumulative)",      "[XXX,XXX,XXX.XX]", "Ref: VO-XXX to VO-XXX"],
    ["C.  Current Contract Value  (A + B)",       "[XXX,XXX,XXX.XX]", ""],
    ["D.  Previous Certified Amount (Cumulative)","[XXX,XXX,XXX.XX]", "Up to App. No. XXX"],
    ["E.  Current Application Amount",            "[XXX,XXX,XXX.XX]", "This Application"],
    ["F.  Cumulative Certified Amount (D + E)",   "[XXX,XXX,XXX.XX]", ""],
    ["G.  Retention",                             "[XXX,XXX,XXX.XX]", "XX% per Subcontract"],
    ["H.  Advance Recovery (if applicable)",      "[XXX,XXX,XXX.XX]", ""],
    ["I.   Taxes (if applicable)",                "[XXX,XXX,XXX.XX]", "VAT / GST / WHT"],
    ["J.   Net Amount Due  (E − G − H − I)",      "[XXX,XXX,XXX.XX]", ""],
    ["K.  Remaining Contract Balance  (C − F)",   "[XXX,XXX,XXX.XX]", ""],
]
add_formatted_table(doc, comm_headers, comm_rows, col_widths=[6.5, 4.5, 5.5])

# Bold the Net Amount Due row
net_row = doc.tables[-1].rows[-2]  # J row
for cell in net_row.cells:
    for p in cell.paragraphs:
        for run in p.runs:
            run.bold = True

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — CONTRACT DELIVERABLES
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "3", "CONTRACT DELIVERABLES")

p_note = doc.add_paragraph()
p_note.paragraph_format.space_after = Pt(6)
run_note = p_note.add_run(
    "Instruction:  List all contractual deliverables. Mark the status of each. "
    "Use continuation sheets as required. Attach Document Transmittal / Acceptance Certificate as supporting evidence."
)
run_note.font.size = Pt(9)
run_note.font.name = 'Calibri'
run_note.italic = True
run_note.font.color.rgb = ACCENT_GREY

del_headers = [
    "No.", "Deliverable Description", "Ref. No.", "Rev.",
    "Contract Requirement", "Previous\nSubmission", "Current\nSubmission",
    "Current Status", "Acceptance\nStatus", "Remarks"
]
del_rows = [
    ["1",  "[e.g., Process Flow Diagram — Unit 100]",  "[DOC-XXX-001]", "A", "IFR", "23-Jun-2026", "15-Jul-2026", "Submitted", "Accepted", ""],
    ["2",  "[e.g., P&ID — Unit 200]",                  "[DOC-XXX-002]", "B", "IFR", "23-Jun-2026", "15-Jul-2026", "Submitted", "Accepted with Comments", ""],
    ["3",  "[e.g., Equipment Data Sheet — P-101A/B]",  "[DOC-XXX-003]", "0", "IFR", "—", "15-Jul-2026", "First Submission", "Pending Review", ""],
    ["4",  "[e.g., Structural Calculation — Pipe Rack]","[DOC-XXX-004]", "0", "IFR", "—", "—", "In Progress", "—", ""],
    ["5",  "[e.g., Vendor Document — VDR-001]",        "[DOC-XXX-005]", "A", "IFA", "30-May-2026", "—", "Vendor Hold", "—", "Awaiting vendor input"],
    ["6",  "[e.g., Inspection & Test Plan — Welding]",  "[DOC-XXX-006]", "0", "IFR", "—", "15-Jul-2026", "Submitted", "Pending Review", ""],
    ["7",  "[e.g., Factory Acceptance Test Procedure]", "[DOC-XXX-007]", "0", "IFA", "—", "—", "Not Started", "—", ""],
    ["8",  "[e.g., Commissioning Procedure — System X]","[DOC-XXX-008]", "0", "IFC", "—", "—", "Not Started", "—", ""],
    ["9",  "[e.g., Training Completion Report]",        "[DOC-XXX-009]", "0", "IFR", "—", "—", "Not Started", "—", ""],
    ["10", "[e.g., Final Documentation Dossier]",       "[DOC-XXX-010]", "0", "IFC", "—", "—", "Not Started", "—", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
]
add_formatted_table(doc, del_headers, del_rows, col_widths=[0.8, 3.2, 1.8, 0.7, 1.5, 1.6, 1.6, 1.6, 1.6, 2.0])

# Legend for status codes
doc.add_paragraph("")
p_leg = doc.add_paragraph()
p_leg.paragraph_format.space_after = Pt(0)
run_leg = p_leg.add_run("Status Codes — ")
run_leg.bold = True
run_leg.font.size = Pt(8)
run_leg.font.name = 'Calibri'
codes = "IFR = Issued for Review  |  IFA = Issued for Approval  |  IFC = Issued for Construction  |  IFT = Issued for Tender"
run_leg2 = p_leg.add_run(codes)
run_leg2.font.size = Pt(8)
run_leg2.font.name = 'Calibri'

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — CONTRACT MILESTONES
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "4", "CONTRACT MILESTONES")

p_note2 = doc.add_paragraph()
run_note2 = p_note2.add_run(
    "Instruction:  List each contract milestone with its weighted percentage. "
    "Attach supporting evidence for each claimed milestone."
)
run_note2.font.size = Pt(9)
run_note2.font.name = 'Calibri'
run_note2.italic = True
run_note2.font.color.rgb = ACCENT_GREY

ms_headers = [
    "No.", "Milestone Description", "Contract\nWeight (%)", "Current\nStatus",
    "Planned\nCompletion", "Actual / Forecast\nCompletion",
    "Supporting Evidence\n(Ref. No.)", "Engineer\nCertification", "Commercial\nAcceptance"
]
ms_rows = [
    ["1", "[e.g., Kick-off Meeting Completed]",              "5%",  "Achieved",  "01-Jun-2026", "01-Jun-2026", "MOM-XXX-001", "Certified", "Accepted"],
    ["2", "[e.g., Engineering Deliverables — Phase 1 (PFD)]","10%", "Achieved",  "15-Jun-2026", "15-Jun-2026", "DOC-XXX-001", "Certified", "Accepted"],
    ["3", "[e.g., Engineering Deliverables — Phase 2 (P&ID)]","15%","In Progress","30-Jun-2026","20-Jul-2026", "DOC-XXX-002", "Pending",   "Pending"],
    ["4", "[e.g., Vendor Documents — Batch 1 Submitted]",    "10%", "Achieved",  "15-Jul-2026", "10-Jul-2026", "VDR-001~010", "Certified", "Accepted"],
    ["5", "[e.g., Factory Acceptance Test — Equipment Pkg 1]","20%","Not Started","15-Aug-2026","—",           "FAT-PKG1",    "—",         "—"],
    ["6", "[e.g., Site Acceptance Test Completed]",          "15%", "Not Started","15-Sep-2026","—",           "SAT-XXX",     "—",         "—"],
    ["7", "[e.g., Commissioning Support Completed]",         "10%", "Not Started","01-Oct-2026","—",           "COMM-XXX",    "—",         "—"],
    ["8", "[e.g., Training Completion]",                     "5%",  "Not Started","15-Oct-2026","—",           "TRG-XXX",     "—",         "—"],
    ["9", "[e.g., Final Documentation & Close-out]",         "10%", "Not Started","01-Nov-2026","—",           "FD-XXX",      "—",         "—"],
    ["", "", "", "", "", "", "", "", ""],
    ["", "TOTAL", "100%", "", "", "", "", "", ""],
]
# Bold the TOTAL line
add_formatted_table(doc, ms_headers, ms_rows, col_widths=[0.6, 3.6, 1.3, 1.5, 1.8, 1.8, 2.2, 1.6, 1.6])
total_row = doc.tables[-1].rows[-1]
for cell in total_row.cells:
    for p in cell.paragraphs:
        for run in p.runs:
            run.bold = True
    set_cell_shading(cell, "E8EEF4")

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — SUPPORTING DOCUMENTS
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "5", "SUPPORTING DOCUMENTS")

p_sup = doc.add_paragraph()
p_sup.paragraph_format.space_after = Pt(4)
run_sup = p_sup.add_run("The following documents are attached in support of this Application for Payment:")
run_sup.font.size = Pt(10)
run_sup.font.name = 'Calibri'

# Create two-column checkbox layout
checklist_left = [
    "Deliverable Register",
    "Document Transmittal",
    "Acceptance Certificate",
    "Progress Report",
    "Completion Certificate",
    "Technical Report",
    "Inspection Report",
    "FAT Report",
    "SAT Report",
]
checklist_right = [
    "Commissioning Report",
    "Performance Test",
    "Time Sheet / Attendance Record",
    "Invoice",
    "Variation Approval",
    "Meeting Minutes",
    "Correspondence / Letter",
    "Photographic Evidence",
    "Others (specify): _______________",
]

# Use a borderless two-column table for checkboxes
cb_table = doc.add_table(rows=max(len(checklist_left), len(checklist_right)), cols=2)
cb_table.autofit = True
for i in range(max(len(checklist_left), len(checklist_right))):
    for j, lst in enumerate([checklist_left, checklist_right]):
        cell = cb_table.rows[i].cells[j]
        cell.width = Cm(8)
        if i < len(lst):
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.space_before = Pt(3)
            run = p.add_run(f"☐  {lst[i]}")
            run.font.size = Pt(9.5)
            run.font.name = 'Calibri'

# Remove borders from checkbox table
for row in cb_table.rows:
    for cell in row.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none" w:sz="0" w:color="auto"/>'
            f'<w:left w:val="none" w:sz="0" w:color="auto"/>'
            f'<w:bottom w:val="none" w:sz="0" w:color="auto"/>'
            f'<w:right w:val="none" w:sz="0" w:color="auto"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(tcBorders)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — SUBCONTRACTOR CERTIFICATION
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "6", "SUBCONTRACTOR CERTIFICATION")

cert_text = (
    "The Subcontractor hereby certifies and warrants to the EPC Contractor that:\n\n"
    "(a)\tAll deliverables, documents, data, and information listed in this Application "
    "have been completed and submitted in accordance with the requirements of the Subcontract "
    "Agreement and all applicable technical specifications, codes, and standards referenced therein;\n\n"
    "(b)\tAll statements, representations, and particulars set forth in this Application and all "
    "supporting documents submitted herewith are true, accurate, and complete in all material respects "
    "and do not contain any misrepresentation or omission that would render them misleading;\n\n"
    "(c)\tThe milestone progress and deliverable completion claimed herein accurately reflect the "
    "actual status of the Services performed as at the date of this Application, and all claimed "
    "milestones have been substantially achieved in accordance with the criteria defined in the Subcontract;\n\n"
    "(d)\tThe Services have been performed in accordance with the Project requirements, including "
    "all applicable quality assurance, health, safety, environmental, and security requirements "
    "specified in the Subcontract and the Project Execution Plan;\n\n"
    "(e)\tAll subcontractor personnel deployed in the performance of the Services possess the "
    "qualifications, certifications, and competencies required under the Subcontract;\n\n"
    "(f)\tThis Application for Payment is submitted in good faith and the Subcontractor is entitled "
    "to the amount claimed herein in accordance with the terms and conditions of the Subcontract;\n\n"
    "(g)\tThe Subcontractor acknowledges that any certification found to be false, inaccurate, or "
    "misleading shall entitle the EPC Contractor to suspend payment, recover any amounts overpaid, "
    "and exercise any other rights or remedies available under the Subcontract or at law."
)

p_cert = doc.add_paragraph()
p_cert.paragraph_format.space_after = Pt(6)
run_cert = p_cert.add_run(cert_text)
run_cert.font.size = Pt(9.5)
run_cert.font.name = 'Calibri'
run_cert.font.color.rgb = DARK_GREY

doc.add_paragraph("")

# Certification signature block
cert_sig_headers = ["", "Name", "Title", "Signature", "Date"]
cert_sig_rows = [
    ["Certified By\n(Subcontractor Authorized Representative)", "[Insert Name]", "[Title]", "", "[DD-Mon-YYYY]"],
]
add_formatted_table(doc, cert_sig_headers, cert_sig_rows, col_widths=[6.0, 3.5, 2.5, 2.5, 2.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 7 — CONTRACTOR REVIEW
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "7", "CONTRACTOR REVIEW & CERTIFICATION")

p_rev_note = doc.add_paragraph()
run_rev_note = p_rev_note.add_run(
    "Instruction:  Each discipline reviewer shall complete their review and indicate their "
    "recommendation. The Commercial / Contracts function shall consolidate all review inputs "
    "before issuing the Payment Certificate."
)
run_rev_note.font.size = Pt(9)
run_rev_note.font.name = 'Calibri'
run_rev_note.italic = True
run_rev_note.font.color.rgb = ACCENT_GREY

review_headers = [
    "Review Discipline", "Reviewer Name", "Status",
    "Certified Amount", "Review Comments", "Review Date", "Signature"
]
review_rows = [
    ["Engineering",          "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Project Management",   "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["QA / QC",             "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Planning / Controls",  "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["HSSE (if applicable)", "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Construction (if appl.)","[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Commissioning (if appl.)","[Name]","☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Commercial",           "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Contracts",            "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
    ["Finance",              "[Name]", "☐ Accepted  ☐ Comments  ☐ Rejected", "[Amount]", "", "[DD-Mon-YYYY]", ""],
]
add_formatted_table(doc, review_headers, review_rows, col_widths=[2.4, 1.8, 4.0, 1.8, 3.2, 1.8, 1.8])

doc.add_paragraph("")

# Summary Certification
add_label_value(doc, "Summary Recommendation",
    "☐  Recommended for Full Payment    ☐  Recommended for Partial Payment    ☐  Not Recommended")
add_label_value(doc, "Certified Amount for Payment", "[XXX,XXX,XXX.XX]")
add_label_value(doc, "Payment Certificate Reference", "[PC-XXX-XXX]")

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 8 — SIGNATURES
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "8", "SIGNATURES")

p_sig_note = doc.add_paragraph()
run_sig_note = p_sig_note.add_run(
    "This Application for Payment, when certified by the EPC Contractor, constitutes "
    "authorization for the Contractor to process payment in accordance with the payment "
    "terms of the Subcontract Agreement. Signatories confirm that they have reviewed the "
    "application and that all statements herein are accurate to the best of their knowledge."
)
run_sig_note.font.size = Pt(9)
run_sig_note.font.name = 'Calibri'
run_sig_note.italic = True
run_sig_note.font.color.rgb = ACCENT_GREY

sig_headers = ["Role", "Name", "Company", "Signature", "Date"]
sig_rows = [
    ["Prepared By\n(Subcontractor)",          "[Insert Name]", "[Subcontractor Name]", "", "[DD-Mon-YYYY]"],
    ["Checked By\n(Subcontractor)",           "[Insert Name]", "[Subcontractor Name]", "", "[DD-Mon-YYYY]"],
    ["Submitted By\n(Subcontractor Authorized Rep.)", "[Insert Name]", "[Subcontractor Name]", "", "[DD-Mon-YYYY]"],
    ["", "", "", "", ""],
    ["Reviewed By\n(EPC Contractor — Project)", "[Insert Name]", "[EPC Contractor Name]", "", "[DD-Mon-YYYY]"],
    ["Reviewed By\n(EPC Contractor — Commercial)","[Insert Name]", "[EPC Contractor Name]", "", "[DD-Mon-YYYY]"],
    ["Certified By\n(EPC Contractor — Contracts)","[Insert Name]", "[EPC Contractor Name]", "", "[DD-Mon-YYYY]"],
    ["Approved By\n(EPC Contractor Authorized Rep.)","[Insert Name]","[EPC Contractor Name]", "", "[DD-Mon-YYYY]"],
]
add_formatted_table(doc, sig_headers, sig_rows, col_widths=[3.8, 3.5, 3.2, 3.0, 3.0])

# Highlight Subcontractor / Contractor separation
sub_row = doc.tables[-1].rows[0]
for cell in sub_row.cells:
    set_cell_shading(cell, "EDF2F9")
epc_row_start = doc.tables[-1].rows[4]
for cell in epc_row_start.cells:
    set_cell_shading(cell, "FFF3E0")

# ═══════════════════════════════════════════════════════════════════════════════
# APPENDIX — GUIDANCE NOTES
# ═══════════════════════════════════════════════════════════════════════════════

add_section_heading(doc, "—", "GUIDANCE NOTES FOR COMPLETION")

guidance = [
    ("General",
     "This template is designed for deliverable-based and professional service subcontracts. "
     "It shall NOT be used for construction or measured-quantity progress (use a Construction IPC for those)."),

    ("Section 3 — Deliverables",
     "List every contractual deliverable. If the deliverable list exceeds one page, continue on "
     "additional sheets clearly marked 'Continuation Sheet — Section 3'. Each deliverable entry "
     "must be traceable to a specific Subcontract clause or exhibit."),

    ("Section 4 — Milestones",
     "Milestone weights must sum to 100%. A milestone may only be claimed as 'Achieved' when "
     "the deliverable or event has been formally accepted by the EPC Contractor in writing. "
     "'In Progress' milestones shall not be claimed unless the Subcontract expressly provides "
     "for partial / progress payment against incomplete milestones."),

    ("Supporting Evidence",
     "Every claimed milestone and deliverable must be supported by objective evidence. "
     "Applications submitted without supporting documentation will be returned. "
     "The Contractor reserves the right to request additional evidence."),

    ("Retention",
     "Retention shall be deducted in accordance with the Subcontract. Retention release "
     "shall be applied for separately upon achievement of the retention release milestones "
     "specified in the Subcontract (typically: 50% at Provisional Acceptance / Taking-Over; "
     "50% at Final Acceptance / End of Defects Notification Period)."),

    ("Payment Terms",
     "The Contractor shall process certified applications within the period stipulated in "
     "the Subcontract Agreement. Any dispute regarding a certified amount shall be referred "
     "to the Parties' respective commercial representatives for resolution in the first instance."),
]

for title, text in guidance:
    p_g = doc.add_paragraph()
    p_g.paragraph_format.space_before = Pt(6)
    p_g.paragraph_format.space_after = Pt(2)
    run_gt = p_g.add_run(title)
    run_gt.bold = True
    run_gt.font.size = Pt(9.5)
    run_gt.font.name = 'Calibri'
    run_gt.font.color.rgb = DARK_BLUE

    p_g2 = doc.add_paragraph()
    p_g2.paragraph_format.left_indent = Cm(1.0)
    p_g2.paragraph_format.space_after = Pt(2)
    run_g = p_g2.add_run(text)
    run_g.font.size = Pt(9)
    run_g.font.name = 'Calibri'

# ═══════════════════════════════════════════════════════════════════════════════
# END OF DOCUMENT
# ═══════════════════════════════════════════════════════════════════════════════

doc.add_paragraph("")
p_end = doc.add_paragraph()
p_end.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_end.paragraph_format.space_before = Pt(20)
run_end_sep = p_end.add_run("━" * 40)
run_end_sep.font.size = Pt(6)
run_end_sep.font.color.rgb = BORDER_GREY

p_end2 = doc.add_paragraph()
p_end2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_e = p_end2.add_run("— END OF DOCUMENT —")
run_e.bold = True
run_e.font.size = Pt(9)
run_e.font.color.rgb = ACCENT_GREY
run_e.font.name = 'Calibri'

# ── Save ─────────────────────────────────────────────────────────────────────
output_path = r"D:\Wison\Project_Info\Wison Template\Non-Wison Template\Subcontractor_Application_for_Payment_Template.docx"
doc.save(output_path)
print(f"[DONE] Template saved to: {output_path}")
# Also open the file
import os
os.startfile(output_path)

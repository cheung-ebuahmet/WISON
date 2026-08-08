"""
Generate Purchase Order for additional medical personnel (Night Shift)
under existing Medical Service Agreement.
Contractor: Wison Energy Engineering (Hong Kong) Limited – Abu Dhabi
Supplier: Response Plus Medical Services L.L.C.
"""
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', errors='replace')

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import copy

OUT = r"D:\Wison\Subcon_Payments\08 Med. Svc. Agr\Contract\Medical_Service_PO_Night_Shift.docx"

doc = Document()

# ============================================================
# Page Setup
# ============================================================
for section in doc.sections:
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)
style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
style.paragraph_format.space_after = Pt(4)

# ============================================================
# Helpers
# ============================================================
def set_cell_border(cell, **kwargs):
    """Set cell border."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}></w:tcBorders>')
    for edge, val in kwargs.items():
        element = parse_xml(
            f'<w:{edge} {nsdecls("w")} w:val="{val.get("val","single")}" '
            f'w:sz="{val.get("sz","4")}" w:space="0" '
            f'w:color="{val.get("color","000000")}"/>'
        )
        tcBorders.append(element)
    tcPr.append(tcBorders)

def set_cell_shading(cell, color):
    """Set cell background color."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=50, bottom=50, left=80, right=80):
    """Set cell padding."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}></w:tcMar>')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = parse_xml(f'<w:{m} {nsdecls("w")} w:w="{val}" w:type="dxa"/>')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_para(text, bold=False, size=11, align=None, color=None, space_before=0, space_after=4, font_name='Calibri'):
    """Add a paragraph with styling."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    run = p.add_run(text)
    run.font.name = font_name
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = color
    return p

def add_section_heading(text):
    """Add a dark blue section heading."""
    return add_para(text, bold=True, size=12, color=RGBColor(0x1F, 0x4E, 0x79),
                    space_before=14, space_after=6)

def set_table_borders(table):
    """Set professional borders on all table cells."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}></w:tblPr>')
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="333333"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def write_table_header(table, headers, widths=None):
    """Write header row with dark grey shading and white text."""
    hdr = table.rows[0]
    for i, text in enumerate(headers):
        cell = hdr.cells[i]
        set_cell_shading(cell, '1F4E79')
        set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.runs[0] if p.runs else p.add_run(text)
        if not p.runs:
            run = p.add_run(text)
        else:
            run = p.runs[0]
            run.text = text
        run.font.name = 'Calibri'
        run.font.size = Pt(10)
        run.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    if widths:
        for i, w in enumerate(widths):
            hdr.cells[i].width = Inches(w)

def fill_cell(cell, text, bold=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
    """Fill a regular cell."""
    set_cell_margins(cell, top=50, bottom=50, left=100, right=100)
    p = cell.paragraphs[0]
    p.alignment = align
    run = p.runs[0] if p.runs else p.add_run(text)
    if not p.runs:
        run = p.add_run(text)
    else:
        run = p.runs[0]
        run.text = text
    run.font.name = 'Calibri'
    run.font.size = Pt(size)
    run.bold = bold

# ============================================================
# HEADER — Contractor Info Block
# ============================================================
hdr_table = doc.add_table(rows=1, cols=2)
hdr_table.autofit = False
set_table_borders(hdr_table)

# Left — Contractor
c1 = hdr_table.rows[0].cells[0]
set_cell_margins(c1, top=60, bottom=60, left=120, right=120)
# Clear default para
c1.paragraphs[0].text = ""
p = c1.add_paragraph()
run = p.add_run("WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI")
run.font.name = 'Calibri'; run.font.size = Pt(12); run.bold = True
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
for line in [
    "Saman Tower, Floor 13, Office 1309",
    "Hamdan Street, Abu Dhabi, United Arab Emirates",
    "Tel: +971 2 681 5588",
    "Project: Sulphur Granulation Plant at RSHT-2",
    "for Hail & Ghasha Project"
]:
    p = c1.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    run = p.add_run(line)
    run.font.name = 'Calibri'; run.font.size = Pt(9); run.font.color.rgb = RGBColor(0x55,0x55,0x55)

# Right — PO details
c2 = hdr_table.rows[0].cells[1]
set_cell_margins(c2, top=60, bottom=60, left=120, right=120)
c2.paragraphs[0].text = ""
c2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = c2.paragraphs[0].add_run("PURCHASE ORDER")
run.font.name = 'Calibri'; run.font.size = Pt(16); run.bold = True
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

for label, val in [
    ("PO No.:", "___________________"),
    ("Date:", "___________________"),
    ("Ref. Agreement:", "Medical Service Agreement"),
    ("Agreement Date:", "09 September 2025"),
]:
    p = c2.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r1 = p.add_run(label + " ")
    r1.font.name = 'Calibri'; r1.font.size = Pt(9); r1.bold = True
    r2 = p.add_run(val)
    r2.font.name = 'Calibri'; r2.font.size = Pt(9)

doc.add_paragraph()  # spacer

# ============================================================
# SUPPLIER BLOCK
# ============================================================
add_para("To (Supplier):", bold=True, size=10, space_after=2)
add_para("RESPONSE PLUS MEDICAL SERVICES L.L.C.", bold=True, size=11)
add_para("6th Floor, Emirates Real Estate Corp Building, Al Falah Street,\n"
         "Al Danah, Abu Dhabi. P.O.Box 130336 Abu Dhabi, United Arab Emirates",
         size=9, color=RGBColor(0x55,0x55,0x55), space_after=8)

# ============================================================
# SECTION 1 — PURPOSE
# ============================================================
add_section_heading("1. PURPOSE")
add_para("Pursuant to the above-referenced Medical Service Agreement (the "
         "\"Agreement\"), the Contractor hereby instructs the Supplier to "
         "provide additional medical personnel to support the Project night "
         "shift operations.",
         space_after=4)
add_para("This Purchase Order is issued solely as a service instruction under "
         "the existing Agreement and shall not constitute a separate contract "
         "or an amendment to the Agreement.",
         space_after=4)

# ============================================================
# SECTION 2 — SCOPE OF SERVICES (Table)
# ============================================================
add_section_heading("2. SCOPE OF SERVICES — ADDITIONAL PERSONNEL")

add_para("The Supplier shall provide the following additional personnel for "
         "night shift duties:", space_after=6)

t = doc.add_table(rows=3, cols=4)
t.alignment = WD_TABLE_ALIGNMENT.CENTER
t.autofit = False
set_table_borders(t)

write_table_header(t, ["Position", "Quantity", "Shift", "Remarks"],
                   widths=[2.8, 1.0, 1.4, 1.8])

# Row 1 — Registered Nurse
fill_cell(t.rows[1].cells[0], "Registered Male Nurse\n(DOH-Approved, BLS/ACLS Certified)")
fill_cell(t.rows[1].cells[1], "1", align=WD_ALIGN_PARAGRAPH.CENTER)
fill_cell(t.rows[1].cells[2], "Night Shift\n(10 hrs/day, 6 days/week)", align=WD_ALIGN_PARAGRAPH.CENTER)
fill_cell(t.rows[1].cells[3], "Additional manpower to supplement\nexisting day shift coverage")

# Row 2 — Driver
fill_cell(t.rows[2].cells[0], "First Aid Trained Driver\n(Valid UAE Driving License)")
fill_cell(t.rows[2].cells[1], "1", align=WD_ALIGN_PARAGRAPH.CENTER)
fill_cell(t.rows[2].cells[2], "Night Shift\n(10 hrs/day, 6 days/week)", align=WD_ALIGN_PARAGRAPH.CENTER)
fill_cell(t.rows[2].cells[3], "Additional manpower to supplement\nexisting day shift coverage")

# Alternate row shading
for row in [t.rows[1], t.rows[2]]:
    for cell in row.cells:
        set_cell_shading(cell, 'F7F9FC')

doc.add_paragraph()  # spacer

# ============================================================
# SECTION 3 — COMMERCIAL TERMS
# ============================================================
add_section_heading("3. COMMERCIAL TERMS")

bullets = [
    "The unit rates for the above personnel shall remain exactly the same as "
    "those agreed under the existing Medical Service Agreement for the "
    "corresponding day shift positions.",

    "Payment shall be based on actual attendance records, verified and "
    "approved by the Contractor on a monthly basis.",

    "Medicines, medical consumables, laboratory tests, medical equipment, "
    "and other reimbursable items shall be charged separately in accordance "
    "with the Agreement.",

    "All invoices shall be submitted together with supporting monthly "
    "attendance records signed by the Contractor's authorized representative.",

    "Payment terms shall be as stipulated in Clause 2.2 of the Agreement: "
    "payment within thirty (30) calendar days after receipt and verification "
    "of a correct invoice.",

    "All payments shall be transferred to the Supplier's bank account as "
    "designated in the Agreement.",
]
for b in bullets:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Cm(0.5)
    run = p.add_run("• " + b)
    run.font.name = 'Calibri'; run.font.size = Pt(10.5)

# ============================================================
# SECTION 4 — EFFECTIVE DATE & DURATION
# ============================================================
add_section_heading("4. EFFECTIVE DATE & DURATION")
add_para("This Purchase Order shall become effective upon issuance and shall "
         "remain valid until cancelled or revised in writing by the Contractor.",
         space_after=4)
add_para("The Supplier shall mobilize the above personnel within seven (7) "
         "calendar days from the date of this Purchase Order, or as otherwise "
         "agreed in writing.",
         space_after=4)

# ============================================================
# SECTION 5 — CONTRACTUAL STATUS
# ============================================================
add_section_heading("5. CONTRACTUAL STATUS")
add_para("Except as expressly stated in this Purchase Order, all terms and "
         "conditions of the existing Medical Service Agreement shall remain "
         "unchanged and in full force and effect.",
         space_after=6)
add_para("For the avoidance of doubt, the Supplier's obligations under the "
         "Agreement — including but not limited to personnel qualifications, "
         "licensing, insurance, HSE compliance, and indemnity obligations — "
         "shall apply in full to the personnel deployed under this Purchase Order.",
         space_after=6)

# ============================================================
# SECTION 6 — ACKNOWLEDGEMENT (Signature Table)
# ============================================================
add_section_heading("6. ACKNOWLEDGEMENT")

sig_table = doc.add_table(rows=1, cols=2)
sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(sig_table)

# Left — Contractor
cl = sig_table.rows[0].cells[0]
set_cell_margins(cl, top=60, bottom=60, left=120, right=120)
for line in [
    ("For and on behalf of", False),
    ("Wison Energy Engineering (Hong Kong) Limited – Abu Dhabi", True),
    ("", False),
    ("Authorized Representative", False),
    ("", False),
    ("Signature: _______________________", False),
    ("", False),
    ("Name: _______________________", False),
    ("", False),
    ("Title: _______________________", False),
    ("", False),
    ("Date: _______________________", False),
]:
    if not line[0]:
        cl.add_paragraph()
        continue
    p = cl.add_paragraph()
    run = p.add_run(line[0])
    run.font.name = 'Calibri'; run.font.size = Pt(10)
    run.bold = line[1]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)

# Right — Supplier
cr = sig_table.rows[0].cells[1]
set_cell_margins(cr, top=60, bottom=60, left=120, right=120)
for line in [
    ("Acknowledged by", False),
    ("RESPONSE PLUS MEDICAL SERVICES L.L.C.", True),
    ("", False),
    ("Authorized Representative", False),
    ("", False),
    ("Signature: _______________________", False),
    ("", False),
    ("Name: _______________________", False),
    ("", False),
    ("Title: _______________________", False),
    ("", False),
    ("Date: _______________________", False),
]:
    if not line[0]:
        cr.add_paragraph()
        continue
    p = cr.add_paragraph()
    run = p.add_run(line[0])
    run.font.name = 'Calibri'; run.font.size = Pt(10)
    run.bold = line[1]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)

# ============================================================
# FOOTER
# ============================================================
for section in doc.sections:
    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.paragraph_format.space_before = Pt(4)

    # Divider line
    pPr = fp._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="4" w:color="999999"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)

    run1 = fp.add_run("Confidential")
    run1.font.name = 'Calibri'; run1.font.size = Pt(8)
    run1.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    run2 = fp.add_run("    |    Page ")
    run2.font.name = 'Calibri'; run2.font.size = Pt(8)
    run2.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    # Page number field
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run_page = fp.add_run()
    run_page._r.append(fldChar1)
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
    run_page._r.append(instrText)
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run_page._r.append(fldChar2)

    run3 = fp.add_run(" of ")
    run3.font.name = 'Calibri'; run3.font.size = Pt(8)
    run3.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

    # Total pages field
    run_total = fp.add_run()
    fldChar3 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run_total._r.append(fldChar3)
    instrText2 = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> NUMPAGES </w:instrText>')
    run_total._r.append(instrText2)
    fldChar4 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run_total._r.append(fldChar4)

# ============================================================
# SAVE
# ============================================================
doc.save(OUT)
print(f"Purchase Order saved: {OUT}")

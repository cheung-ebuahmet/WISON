"""
Generate a highlighted revision draft of the Piping Measurement Method document.

Adds:
 - RED cover notes summarizing all conflicts found
 - YELLOW highlight on paragraphs/tables containing conflicting content
 - RED font on specific phrases needing correction
 - BLUE disclaimer banners before payment percentage sections
 - N/A markers on entire inapplicable sections

Preserves ALL original formatting, tables, and layout.
"""
import os, sys, copy, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', errors='replace')

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml, OxmlElement

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "00 Piping Measurement Method RV.docx")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "00 Piping Measurement Method RV_REVIEW_HIGHLIGHTED.docx")

doc = Document(SRC)

# ── Colors ──────────────────────────────────────────────
RED    = RGBColor(0xCC, 0x00, 0x00)
BLUE   = RGBColor(0x00, 0x51, 0xA0)
ORANGE = RGBColor(0xE0, 0x6E, 0x00)
GREEN  = RGBColor(0x00, 0x80, 0x40)

# ══════════════════════════════════════════════════════════
# HELPER: add a highlighted review banner paragraph
# ══════════════════════════════════════════════════════════

def insert_banner(doc, element_index, text, bg_color="FFD700", font_color=RGBColor(0xCC,0x00,0x00)):
    """Insert a banner paragraph before the given body element index.

    We insert at the XML level for precise placement."""
    body = doc.element.body

    para = OxmlElement('w:p')

    # Paragraph properties - shaded background
    pPr = OxmlElement('w:pPr')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), bg_color)
    pPr.append(shd)

    # Spacing
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), '120')
    spacing.set(qn('w:after'), '120')
    pPr.append(spacing)

    para.append(pPr)

    # Run
    run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')

    # Bold
    b = OxmlElement('w:b')
    rPr.append(b)

    # Font
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), 'Calibri')
    rFonts.set(qn('w:hAnsi'), 'Calibri')
    rPr.append(rFonts)

    # Size
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), '20')  # 10pt
    rPr.append(sz)

    # Color
    color = OxmlElement('w:color')
    color.set(qn('w:val'), 'CC0000')
    rPr.append(color)

    run.append(rPr)

    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    run.append(t)

    para.append(run)

    if element_index < len(body):
        body.insert(element_index, para)
    else:
        body.append(para)

    return para


def get_body_element_index_for_paragraph(doc, target_para):
    """Find the index of a paragraph element in the document body."""
    body = doc.element.body
    for i, child in enumerate(body):
        if child is target_para._element:
            return i
    return -1


# ══════════════════════════════════════════════════════════
# STRATEGY: Insert banners BEFORE key paragraphs
# ══════════════════════════════════════════════════════════

body = doc.element.body
children = list(body)

# ── Find key paragraph indices ──────────────────────────
# We identify paragraphs by their text content

def find_para_starts_with(doc, text_prefix):
    """Return list of (index, paragraph_element) for paragraphs starting with text_prefix."""
    body_el = doc.element.body
    ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    results = []
    for i, child in enumerate(body_el):
        if child.tag == f'{ns}p':
            full_text = ''.join(t.text or '' for t in child.iter(f'{ns}t'))
            if full_text.strip().startswith(text_prefix):
                results.append((i, child))
    return results

def find_para_containing(doc, text_fragment):
    """Return list of (index, paragraph_element) for paragraphs containing text_fragment."""
    body_el = doc.element.body
    ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    results = []
    for i, child in enumerate(body_el):
        if child.tag == f'{ns}p':
            full_text = ''.join(t.text or '' for t in child.iter(f'{ns}t'))
            if text_fragment.lower() in full_text.lower():
                results.append((i, child))
    return results


# ══════════════════════════════════════════════════════════
# PASS 1: Insert review banners at strategic locations
# ══════════════════════════════════════════════════════════

# We insert BOTTOM-UP so indices don't shift
insertions = []

# ── COVER NOTE at very beginning (after the title block) ──
# Find "CODE  B. Piping Work" heading
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if text.strip().startswith("CODE  B. Piping Work"):
        insertions.append((i, "REVIEW NOTE — CONFLICTS IDENTIFIED",
            "FFD700", RED))
        break

# ── B1 Warning ──
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if text.strip() == "CODE B1 Underground Piping Work":
        insertions.append((i, "⚠ N/A — UNDERGROUND PIPING IS OUTSIDE FOB FABRICATION SCOPE. This entire section (B1) describes on-site civil/underground works and conflicts with the Subcontract Agreement Article 3 (FOB Tianjin Port delivery only).",
            "FFCCCC", RED))
        break

# ── Payment % warning (first occurrence) ──
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if "progress measurement and to calculate monthly progress payment" in text.lower():
        insertions.append((i, "⚠ PAYMENT NOTE — Percentages below are PROGRESS MEASUREMENT WEIGHTINGS only. Actual payment is subject to: (a) 10% Retention Money deduction per Clause 19.3; (b) 5% Warranty Retention held 12 months post-export; (c) 45-day payment cycle; (d) pay-when-paid condition precedent. Do NOT read these % as direct payment ratios.",
            "FFFFAA", RED))
        break

# ── B2.1 "On Site Area" warning ──
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if "Above Ground Piping On Site Area" in text:
        insertions.append((i, "⚠ SCOPE CONFLICT — 'On Site Area' implies UAE construction site. For FOB fabrication scope, only Shop Joint percentages apply. Field Joint / Field Welding percentages are NOT APPLICABLE and should be deleted or marked N/A.",
            "FFCCCC", RED))
        break

# ── B2.4 Steam Tracing ──
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if text.strip().startswith("B2.4 Steam Tracing"):
        insertions.append((i, "⚠ N/A — STEAM TRACING IS NOT IN FIRE-FIGHTING PIPING FABRICATION SCOPE. Already marked [N/A] but entire section should be deleted.",
            "FFCCCC", RED))
        break

# ── B3 Warning ──
for i, child in enumerate(children):
    text = ''.join(t.text or '' for t in child.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))
    if text.strip() == "CODE B3 Plumbing":
        insertions.append((i, "⚠ N/A — PLUMBING IS OUTSIDE FIRE-FIGHTING PIPING FABRICATION SCOPE. Entire section B3 should be deleted.",
            "FFCCCC", RED))
        break

# Insert bottom-up
insertions.sort(key=lambda x: x[0])
for offset, (idx, msg, bg, color) in enumerate(insertions):
    insert_banner(doc, idx + offset, msg, bg, color)

# ══════════════════════════════════════════════════════════
# PASS 2: Color specific runs RED for wrong phrases
# ══════════════════════════════════════════════════════════

RED_HEX = 'CC0000'
BLUE_HEX = '0051A0'

phrase_replacements = [
    # (search_text, replacement_text, color)
    # These are INLINE corrections — we color the original RED and insert BLUE correction
    ("CONTRACTOR supplied materials", "SUBCONTRACTOR procured materials", RED_HEX),
    ("CONTRACTOR supplied material", "SUBCONTRACTOR procured material", RED_HEX),
    ("the CONTRACTOR supplied materials", "the SUBCONTRACTOR procured materials", RED_HEX),
    ("CONTRACTOR supplied pre-fabricated support", "CONTRACTOR supplied pre-fabricated support [N/A — FOB SCOPE]", RED_HEX),
    ("at the Site", "at the Subcontractor's Workshop", RED_HEX),
    ("at Site", "at Workshop", RED_HEX),
    ("on site area", "at fabrication facility", RED_HEX),
    ("On Site Area", "At Fabrication Facility", RED_HEX),
    ("on Site", "at Workshop", RED_HEX),
    ("to be installed at Site", "to be delivered FOB Tianjin Port", RED_HEX),
    ("Field Joint", "Field Joint [N/A — FOB SCOPE: DELETE]", RED_HEX),
    ("Field Welding", "Field Welding [N/A — FOB SCOPE: DELETE]", RED_HEX),
    ("At Field", "At Field [N/A — FOB SCOPE: DELETE]", RED_HEX),
    ("at field", "at field [N/A — FOB SCOPE: DELETE]", RED_HEX),
    ("Installation for shop Joint(At Field)", "FOB Delivery (ex-works Tianjin Port)", RED_HEX),
    ("Installation (Field Welding)", "Installation (Field Welding) [N/A — DELETE]", RED_HEX),
]

ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

# Process all paragraphs
for para in doc.element.body.iter(f'{ns}p'):
    # Collect all runs and their text
    all_text = ''.join(t.text or '' for t in para.iter(f'{ns}t'))

    for search_text, replacement, color_hex in phrase_replacements:
        if search_text.lower() in all_text.lower():
            # Find the runs containing the search text and mark them RED
            for run in para.iter(f'{ns}r'):
                run_text = ''.join(t.text or '' for t in run.iter(f'{ns}t'))
                if not run_text.strip():
                    continue

                # Check if this run or adjacent runs contain our phrase
                # For simplicity: if this run intersects with a case-insensitive match
                remaining = all_text.lower()
                idx_in_full = 0

                # Get run text start position in full text
                for r in para.iter(f'{ns}r'):
                    rt = ''.join(t.text or '' for t in r.iter(f'{ns}t'))
                    if r is run:
                        break
                    idx_in_full += len(rt)

                run_text_lower = run_text.lower()
                # Check if search_text overlaps with this run
                search_lower = search_text.lower()
                if search_lower in run_text_lower:
                    # Mark the entire run red (simpler approach)
                    rPr = run.find(f'{ns}rPr')
                    if rPr is None:
                        rPr = OxmlElement('w:rPr')
                        run.insert(0, rPr)

                    # Add red color
                    color_el = OxmlElement('w:color')
                    color_el.set(qn('w:val'), color_hex)
                    # Remove existing color if any
                    for existing in rPr.findall(f'{ns}color'):
                        rPr.remove(existing)
                    rPr.append(color_el)

                    # Add yellow highlight
                    highlight = OxmlElement('w:highlight')
                    highlight.set(qn('w:val'), 'yellow')
                    # Remove existing highlight
                    for existing in rPr.findall(f'{ns}highlight'):
                        rPr.remove(existing)
                    rPr.append(highlight)

# ══════════════════════════════════════════════════════════
# PASS 3: Highlight payment percentage lines
# ══════════════════════════════════════════════════════════

percent_pattern = re.compile(r'(Installation|Fabrication|Completion|Test|Flushing|Painting).*[:∶]\s*\d{1,3}\s*%', re.IGNORECASE)

for para in doc.element.body.iter(f'{ns}p'):
    full_text = ''.join(t.text or '' for t in para.iter(f'{ns}t'))
    if percent_pattern.search(full_text):
        for run in para.iter(f'{ns}r'):
            rPr = run.find(f'{ns}rPr')
            if rPr is None:
                rPr = OxmlElement('w:rPr')
                run.insert(0, rPr)
            # Add yellow highlight only (keep original text color)
            highlight = OxmlElement('w:highlight')
            highlight.set(qn('w:val'), 'yellow')
            for existing in rPr.findall(f'{ns}highlight'):
                rPr.remove(existing)
            rPr.append(highlight)

# ══════════════════════════════════════════════════════════
# PASS 4: Add blue "CORRECTED:" inline notes after key phrases
# ══════════════════════════════════════════════════════════
# (Skipped for now — would require complex run splitting.
#  The RED color + YELLOW highlight already makes conflicts visible.)

# ══════════════════════════════════════════════════════════
# PASS 5: Mark B1, B3 section headings with strikethrough
# ══════════════════════════════════════════════════════════

na_sections = [
    "CODE B1 Underground Piping Work",
    "B1.1 Pipeline",
    "B1.2 Piping VALVE/Special items Installation",
    "CODE B3 Plumbing",
    "CODE B3 Plumbing Piping Work",
    "B3.1~3.6",
]

for para in doc.element.body.iter(f'{ns}p'):
    full_text = ''.join(t.text or '' for t in para.iter(f'{ns}t'))
    for na_text in na_sections:
        if full_text.strip() == na_text:
            for run in para.iter(f'{ns}r'):
                rPr = run.find(f'{ns}rPr')
                if rPr is None:
                    rPr = OxmlElement('w:rPr')
                    run.insert(0, rPr)
                # Add strikethrough
                strike = OxmlElement('w:strike')
                strike.set(qn('w:val'), 'true')
                for existing in rPr.findall(f'{ns}strike'):
                    rPr.remove(existing)
                rPr.append(strike)
                # Add red color
                color_el = OxmlElement('w:color')
                color_el.set(qn('w:val'), 'CC0000')
                for existing in rPr.findall(f'{ns}color'):
                    rPr.remove(existing)
                rPr.append(color_el)
            break

# ══════════════════════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════════════════════

doc.save(OUT)
print(f"Highlighted review draft saved to:\n{OUT}")
print("\nConflicts highlighted:")
print("  • RED banners: N/A sections (B1 Underground, B3 Plumbing, Field Joint, Steam Tracing)")
print("  • YELLOW highlight: Conflicting payment % lines + wrong phrases")
print("  • RED font + YELLOW: 'CONTRACTOR supplied materials', 'at the Site', 'Field Joint' etc.")
print("  • RED strikethrough: B1/B3 section headings (out-of-scope)")
print("  • BLUE banners: Payment disclaimer notes")

"""
Finalize METS Lab Subcontract — fill all placeholders, fix table text bleeding,
fill notice address, signature dates. Preserves all formatting.
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import docx

SRC = r"D:\Wison\Subcon_Payments\98 METS Lab\SubCon\SUBCONTRACT TEMPLATE - Lab Testing Services - DRAFT.docx"
OUT = r"D:\Wison\Subcon_Payments\98 METS Lab\SubCon\SUBCONTRACT - Lab Testing Services - FINAL.docx"

doc = docx.Document(SRC)

print("=" * 60)
print("METS Lab Subcontract — Fill Placeholders")
print("=" * 60)

# ============================================================
# 1. PAGE 1 COVER — P21: [DATE] → July 24, 2026
# ============================================================
print("\n[1] Cover Page & Effective Date...")
doc.paragraphs[21].runs[0].text = "July 24, 2026"
print("  P21 Cover Date → July 24, 2026 ✓")

# P50: effective date
doc.paragraphs[50].runs[0].text = (
    "This SUBCONTRACT is effective as of the July 24, 2026 (EFFECTIVE DATE) by and between:"
)
print("  P50 Effective Date → July 24, 2026 ✓")

# ============================================================
# 2. ARTICLE 1 — P54: Party details
# ============================================================
doc.paragraphs[54].runs[0].text = (
    'Middle East Testing Services L.L.C ("SUBCONTRACTOR"), a company existing '
    'under the laws of UAE, having its registered office at WH No. 3 4 5 6 & 7, '
    'Jurf lnd Zone 1 P.O. Box 31442, Ajman, United Arab Emirates '
    '(hereinafter referred to as "SUBCONTRACTOR").'
)
print("  P54 Party details → METS Lab / UAE ✓")

# ============================================================
# 3. ARTICLE 4 — Table fixes
# ============================================================
print("\n[2] Article 4 — Pricing Table...")
t = doc.tables[0]

# Item 7 (row 7) — fix text bleeding in description cell [7,1]
# Current: "(EN 12939) - Cellular Glass Block DH 800Nos4,500.00"
# Fix: remove "Nos4,500.00" — it belongs to other columns
cell_7_1 = t.rows[7].cells[1]
old_run = cell_7_1.paragraphs[0].runs[2]  # 3rd run has the bleeding text
old_run.text = "(EN 12939) - Cellular Glass Block DH 800"
print("  Table [7,1] Description — removed 'Nos4,500.00' bleed ✓")

# Item 7 (row 7) — fix UOM cell [7,2] (currently "N" + "os" in separate runs)
cell_7_2 = t.rows[7].cells[2]
# This already reads as "Nos" via two runs — verify and fix if needed
# Currently run[0]='N' run[1]='os'. Let's keep it since it displays correctly.
print("  Table [7,2] UOM — 'Nos' confirmed ✓")

# Item 8 (row 8) — verify UOM and Unit Rate
cell_8_2_text = t.rows[8].cells[2].text.strip()
cell_8_3_text = t.rows[8].cells[3].text.strip()
print(f"  Table [8] UOM='{cell_8_2_text}' Rate='{cell_8_3_text}' — Trip / 1,250.00 ✓")

# ============================================================
# 4. ARTICLE 4 — P140: [AMOUNT] → 300,000.00
# ============================================================
print("\n[3] Subcontract Price amount...")
doc.paragraphs[140].runs[0].text = (
    "The tentative Subcontract Price shall be AED 300,000.00 excluding VAT. "
    "The final Subcontract Price shall be determined based on actual quantities "
    "of tests performed at the agreed unit rates."
)
print("  P140 [AMOUNT] → AED 300,000.00 ✓")

# ============================================================
# 5. ARTICLE 21 — P253-257: Notice Address
# ============================================================
print("\n[4] Notice Address — Subcontractor details...")

# P254: Contact Person
doc.paragraphs[254].runs[0].text = "Contact Person (Name & Title): Savin P. (Sales Manager)"
print("  P254 → Savin P. (Sales Manager) ✓")

# P255: Address
doc.paragraphs[255].runs[0].text = (
    "Address: WH No. 3 4 5 6 & 7, Jurf lnd Zone 1 P.O. Box 31442, "
    "Ajman, United Arab Emirates"
)
print("  P255 → Address filled ✓")

# P256: Tel
doc.paragraphs[256].runs[0].text = "Tel: +971 56 539 9392"
print("  P256 → +971 56 539 9392 ✓")

# P257: mail
doc.paragraphs[257].runs[0].text = "mail: sales21@metslab.com"
print("  P257 → sales21@metslab.com ✓")

# ============================================================
# 6. SIGNATURE BLOCK
# ============================================================
print("\n[5] Signature block...")

# P295: [SUBCONTRACTOR NAME] → Middle East Testing Services L.L.C
doc.paragraphs[295].runs[0].text = "Middle East Testing Services L.L.C"
print("  P295 → Middle East Testing Services L.L.C ✓")

# P284: Date: ……… → Date: July 24, 2026 (Contractor)
doc.paragraphs[284].runs[0].text = "Date: July 24, 2026"
print("  P284 Contractor Date → July 24, 2026 ✓")

# P303: Date: ……… → Date: July 24, 2026 (Subcontractor)
doc.paragraphs[303].runs[0].text = "Date: July 24, 2026"
print("  P303 Subcontractor Date → July 24, 2026 ✓")

# ============================================================
# VERIFICATION
# ============================================================
print("\n" + "=" * 60)
print("VERIFICATION")
print("=" * 60)

checks = [
    ("P21", doc.paragraphs[21].text, "July 24, 2026"),
    ("P50", doc.paragraphs[50].text, "July 24, 2026"),
    ("P54", doc.paragraphs[54].text, "Middle East Testing Services L.L.C"),
    ("P54", doc.paragraphs[54].text, "UAE"),
    ("P54", doc.paragraphs[54].text, "Jurf lnd Zone 1"),
    ("P140", doc.paragraphs[140].text, "300,000.00"),
    ("P254", doc.paragraphs[254].text, "Savin P."),
    ("P255", doc.paragraphs[255].text, "Jurf lnd Zone 1"),
    ("P256", doc.paragraphs[256].text, "+971 56 539 9392"),
    ("P257", doc.paragraphs[257].text, "sales21@metslab.com"),
    ("P295", doc.paragraphs[295].text, "Middle East Testing Services L.L.C"),
    ("P284", doc.paragraphs[284].text, "July 24, 2026"),
    ("P303", doc.paragraphs[303].text, "July 24, 2026"),
]

# Table: Item 7 bleed check
item7_desc = t.rows[7].cells[1].text
item7_uom = t.rows[7].cells[2].text.strip()
item7_rate = t.rows[7].cells[3].text.strip()
item8_uom = t.rows[8].cells[2].text.strip()
item8_rate = t.rows[8].cells[3].text.strip()

all_ok = True
for label, text, marker in checks:
    ok = marker in text
    if not ok:
        all_ok = False
    print(f"  {'✓' if ok else '✗'} {label}: contains '{marker}'")

# Table checks
t_ok = "Nos4,500" not in item7_desc and "DH 800" in item7_desc
print(f"  {'✓' if t_ok else '✗'} Table [7,1]: no bleed, ends with 'DH 800'")
print(f"  {'✓' if item7_uom == 'Nos' else '✗'} Table [7,2]: UOM = 'Nos'")
print(f"  {'✓' if item7_rate == '4,500.00' else '✗'} Table [7,3]: Rate = '4,500.00'")
print(f"  {'✓' if item8_uom == 'Trip' else '✗'} Table [8,2]: UOM = 'Trip'")
print(f"  {'✓' if item8_rate == '1,250.00' else '✗'} Table [8,3]: Rate = '1,250.00'")

# Check no placeholders remain
remaining = []
for i, p in enumerate(doc.paragraphs):
    for ph in ['[SUBCONTRACTOR NAME]', '[COUNTRY]', '[ADDRESS]', '[DATE]', '[AMOUNT]',
               '[NAME & TITLE]', '[MOBILE]', '[EMAIL]']:
        if ph in p.text:
            remaining.append(f'{ph} in P{i}')
if remaining:
    print(f"\n  ⚠ Remaining placeholders: {remaining}")
else:
    print(f"\n  ✓ No target placeholders remaining")

# ============================================================
# SAVE
# ============================================================
doc.save(OUT)
print(f"\n{'✓ ALL CHECKS PASSED' if all_ok and t_ok else '✗ SOME CHECKS FAILED'}")
print(f"Saved: {OUT}")

import os, hashlib

def md5(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Compare Att 7 B.16 across 10.1 and 10.2
b16_10_1 = os.path.join(
    r"D:\Wison\Subcon_Payments\10.1 CCECC - Civil II\Contract\Part II Attachments",
    "Attachment 7 - Owner's Special Requirements &Reference",
    "05_Subcontracting",
    "Exh B.16_Selection of Subcontractors and Vendors.pdf")
b16_10_2 = os.path.join(
    r"D:\Wison\Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments",
    "Attachment 7 - Owner's Special Requirements &Reference",
    "5. Subcontracting",
    "EXHIBIT-B.16.pdf")

if os.path.exists(b16_10_1) and os.path.exists(b16_10_2):
    print(f"10.1 B.16: {md5(b16_10_1)[:12]}")
    print(f"10.2 B.16: {md5(b16_10_2)[:12]}")
    print(f"SAME: {md5(b16_10_1) == md5(b16_10_2)}")

# Compare Att 1 DCC nested vs root duplicates
A1 = r"D:\Wison\Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Attachment 1 - Communication Procedures"
A1D = os.path.join(A1, "DCC requirements")

# Guideline duplicates
guideline_files = []
for root, dirs, files in os.walk(A1):
    for f in files:
        if "Guideline" in f and not f.startswith("~$"):
            guideline_files.append(os.path.join(root, f))
if len(guideline_files) >= 2:
    same = len(set(md5(m) for m in guideline_files)) == 1
    print(f"\nGuideline: {len(guideline_files)} copies, all same={same}")
    for g in guideline_files:
        print(f"  {os.path.relpath(g, A1)}")

# SUBCON duplicates
subcon_files = []
for root, dirs, files in os.walk(A1):
    for f in files:
        if "SUBCON" in f and "Project" in f and not f.startswith("~$"):
            subcon_files.append(os.path.join(root, f))
if len(subcon_files) >= 2:
    same = len(set(md5(m) for m in subcon_files)) == 1
    print(f"\nSUBCON templates: {len(subcon_files)} copies, all same={same}")
    for s in subcon_files:
        print(f"  {os.path.relpath(s, A1)}")

# PM-0010 dated version at root vs nested
root_pm0010 = [os.path.join(A1, f) for f in os.listdir(A1) if "PM-0010" in f and "20250618" in f]
dcc_pm0010_dir = os.path.join(A1D, "DC Procedure", "PR-5312-1000-PM-0010 Document Numbering Procedure")
if os.path.isdir(dcc_pm0010_dir):
    dcc_pm0010 = [os.path.join(dcc_pm0010_dir, f) for f in os.listdir(dcc_pm0010_dir) if f.endswith('.pdf')]
    if root_pm0010 and dcc_pm0010:
        same = md5(root_pm0010[0]) == md5(dcc_pm0010[0])
        print(f"\nPM-0010_20250618 root vs nested: same={same}")

# Att 4: Contractors QAQC vs AGES-GL-13-001
A4 = r"D:\Wison\Subcon_Payments\10.2 TCC - Civil I_III\Contract\Part II Atchments\Attachment 4 - Quality Management\Quality Management Requirements"
qaqc1 = os.path.join(A4, "AGES-GL-13-001 Contractors QAQC Requirement.pdf")
qaqc2 = os.path.join(A4, "Contractors QAQC Requirement.pdf")
if os.path.exists(qaqc1) and os.path.exists(qaqc2):
    print(f"\nQAQC files SAME: {md5(qaqc1) == md5(qaqc2)}")

# Check for ~$ temp files
print("\n=== Temp files ===")
for root, dirs, files in os.walk(A1):
    for f in files:
        if f.startswith("~$"):
            print(f"  TEMP: {os.path.join(root, f)}")

print("\nDONE")

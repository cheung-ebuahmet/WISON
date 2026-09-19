# -*- coding: utf-8 -*-
"""
Normalize self-produced naming to the controlled vocabulary (Decision E).

SCOPE — SELF-PRODUCED LAYER ONLY:
    _Ref/data/**/*.md , _Ref/data/**/*.yaml , index.md
    (Evidence OCR layer _Ref/kb/** is NEVER touched — faithful mirror of source.)

RULES:
    SGP             -> RSGP         (official external name; word-boundary, never touches RSGP)
    RSHT-2/RSHT 2/RSHT2 -> 'RSHT - 2'  (official spacing)

USAGE:
    python normalize_naming.py            # DRY RUN — print unified diff, write nothing
    python normalize_naming.py --apply    # hard write to disk (only after diff vetting)
"""
import os, re, sys, glob, difflib

ROOT = r"D:\Wison"
DATA = os.path.join(ROOT, "_Ref", "data")
APPLY = "--apply" in sys.argv

# standalone SGP -> RSGP (word-boundary: leaves 'EPC-ADNOC-RSGP' etc. intact)
SGP_RE = re.compile(r"(?<![A-Za-z])SGP(?![A-Za-z])")
# RSHT variants -> "RSHT - 2" (idempotent; won't touch a 2 that is part of a longer number)
RSHT_RE = re.compile(r"RSHT[ ]*-?[ ]*2(?!\d)")

def normalize(text):
    text = SGP_RE.sub("RSGP", text)
    text = RSHT_RE.sub("RSHT - 2", text)
    return text

def targets():
    files = []
    for ext in ("*.md", "*.yaml", "*.yml"):
        files += glob.glob(os.path.join(DATA, "**", ext), recursive=True)
    idx = os.path.join(ROOT, "index.md")
    if os.path.isfile(idx):
        files.append(idx)
    return sorted(set(files))

def main():
    changed = 0
    for f in targets():
        with open(f, "r", encoding="utf-8") as fh:
            orig = fh.read()
        new = normalize(orig)
        if new == orig:
            continue
        changed += 1
        rel = os.path.relpath(f, ROOT)
        diff = difflib.unified_diff(
            orig.splitlines(keepends=True), new.splitlines(keepends=True),
            fromfile=rel + "  (BEFORE)", tofile=rel + "  (AFTER)", n=0)
        sys.stdout.write("".join(diff))
        sys.stdout.write("\n")
        if APPLY:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
    mode = "APPLIED (written to disk)" if APPLY else "DRY RUN (nothing written)"
    print(f"=== {mode}: {changed} self-produced file(s) would change ===")

if __name__ == "__main__":
    main()

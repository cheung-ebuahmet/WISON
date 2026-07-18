#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pdf_text.py — extract the text layer from an (already-OCR'd) PDF.
Usage:  python pdf_text.py "<pdf path>" [pageRange]
        pageRange = "5" | "1-10" | omitted (whole doc, capped)
Prints page count + text. For reading the Wison Main Contract clause-by-clause.
No poppler; uses PyMuPDF (fitz). Read-only.
"""
import sys, fitz

def main():
    if len(sys.argv) < 2:
        print("usage: pdf_text.py <pdf> [range]"); return
    path = sys.argv[1]
    rng = sys.argv[2] if len(sys.argv) > 2 else None
    doc = fitz.open(path)
    n = doc.page_count
    if rng and '-' in rng:
        a, b = rng.split('-'); a, b = int(a), int(b)
    elif rng:
        a = b = int(rng)
    else:
        a, b = 1, n
    a = max(1, a); b = min(n, b)
    print(f"### FILE: {path}")
    print(f"### TOTAL PAGES: {n}  |  SHOWING {a}-{b}")
    for i in range(a - 1, b):
        t = doc[i].get_text("text").strip()
        print(f"\n----- p{i+1} -----")
        print(t if t else "[no text layer on this page]")

if __name__ == "__main__":
    main()

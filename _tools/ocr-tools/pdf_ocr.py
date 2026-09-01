#!/usr/bin/env python
"""
PDF OCR tool — pymupdf renders pages → Tesseract recognizes text.
No poppler required: pymupdf (fitz) handles PDF→image natively.

Output modes:
  1. Text only:  python pdf_ocr.py "input.pdf"
  2. Text file:  python pdf_ocr.py "input.pdf" -o out.txt
  3. Searchable PDF (invisible text layer over original image):
     python pdf_ocr.py "input.pdf" --searchable out.pdf

Usage:
    python pdf_ocr.py "input.pdf"                                    # print text
    python pdf_ocr.py "input.pdf" -o out.txt                         # save to file
    python pdf_ocr.py "input.pdf" --searchable out.pdf               # searchable PDF
    python pdf_ocr.py "input.pdf" --searchable out.pdf -o out.txt    # both
    python pdf_ocr.py "input.pdf" -l chi_sim+eng --dpi 400           # multi-lang, hi-res
"""

import argparse
import json
import sys
from pathlib import Path

import fitz  # pymupdf
import pytesseract
from PIL import Image


# ── CJK font mapping for invisible text layer ──────────────────────────
# pymupdf built-in fonts that handle non-Latin scripts
CJK_FONTS = {
    "chi_sim": "china-s",
    "chi_tra": "china-t",
    "jpn": "japan",
    "kor": "korea",
}
FALLBACK_FONT = "helv"  # Latin / default


def _pick_font(language: str) -> str:
    """Choose a pymupdf built-in font suitable for the Tesseract language."""
    for lang_code, font_name in CJK_FONTS.items():
        if lang_code in language:
            return font_name
    return FALLBACK_FONT


# ── Core OCR (text-only) ───────────────────────────────────────────────

def ocr_pdf(
    pdf_path: str,
    language: str = "eng",
    dpi: int = 300,
    output_path: str | None = None,
    pages: list[int] | None = None,
) -> str:
    """OCR a PDF, returning plain text.  If *output_path* is set, also write to file."""
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    target_pages = [p - 1 for p in pages] if pages else list(range(total_pages))

    all_text: list[str] = []

    for idx in target_pages:
        if idx < 0 or idx >= total_pages:
            print(f"[WARN] Page {idx + 1} out of range, skipping")
            continue

        page = doc[idx]
        print(f"OCR page {idx + 1}/{total_pages}...", end=" ", flush=True)

        # Render page → PIL image (NO poppler needed)
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        text = pytesseract.image_to_string(img, lang=language)
        all_text.append(f"--- Page {idx + 1} ---\n{text}")
        print(f"done ({len(text)} chars)")

    doc.close()

    result = "\n\n".join(all_text)

    if output_path:
        Path(output_path).write_text(result, encoding="utf-8")
        print(f"Saved text: {output_path}")

    return result


# ── Searchable PDF (word-level boxes → invisible text layer) ────────────

def ocr_to_searchable_pdf(
    pdf_path: str,
    language: str = "eng",
    dpi: int = 300,
    output_path: str = "output_searchable.pdf",
    pages: list[int] | None = None,
) -> None:
    """
    Create a searchable PDF: keep original image, add invisible text layer
    from Tesseract word-level boxes so text can be selected/searched.
    """
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    target_pages = [p - 1 for p in pages] if pages else list(range(total_pages))
    font = _pick_font(language)
    scale = 72.0 / dpi  # pixel → PDF-point conversion

    for idx in target_pages:
        if idx < 0 or idx >= total_pages:
            continue

        page = doc[idx]
        print(f"OCR page {idx + 1}/{total_pages}...", end=" ", flush=True)

        # Render page to image
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Word-level OCR data
        data = pytesseract.image_to_data(img, lang=language, output_type=pytesseract.Output.DICT)

        # Group words into lines: (block_num, par_num, line_num) → list of words
        lines: dict[tuple[int, int, int], list[dict]] = {}
        for i in range(len(data["text"])):
            text = (data["text"][i] or "").strip()
            if not text:
                continue
            conf = data["conf"][i]
            if isinstance(conf, str):
                conf = float(conf) if conf != "-1" else 0.0
            if conf < 30:  # skip low-confidence junk
                continue
            key = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
            lines.setdefault(key, []).append({
                "left": data["left"][i] * scale,
                "top": data["top"][i] * scale,
                "width": data["width"][i] * scale,
                "height": data["height"][i] * scale,
                "text": text,
            })

        # Insert each word as invisible-but-selectable text.
        # Use insert_text (Point) rather than insert_textbox (Rect) because
        # render_mode=3 only produces extractable text with insert_text.
        words_written = 0
        for key in sorted(lines.keys()):
            words = lines[key]
            for w in words:
                try:
                    # Position at bottom-left of the word (descender baseline)
                    x = w["left"]
                    y = w["top"] + w["height"]
                    page.insert_text(
                        fitz.Point(x, y),
                        w["text"],
                        fontname=font,
                        fontsize=w["height"] * 0.8,
                        render_mode=3,  # invisible but selectable/searchable
                    )
                    words_written += 1
                except Exception:
                    pass

        print(f"done ({words_written} words placed)")

    doc.save(output_path, deflate=True)
    doc.close()
    print(f"Saved searchable PDF: {output_path}")


# ── CLI ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="OCR a PDF using pymupdf + Tesseract (no poppler needed)"
    )
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Output plain-text file (.txt)")
    parser.add_argument("--searchable", metavar="PDF_OUT",
                        help="Output a searchable PDF (invisible text layer over image)")
    parser.add_argument(
        "-l", "--lang", default="eng",
        help="Tesseract language code(s). Common: eng, chi_sim, chi_tra, ara, chi_sim+eng, etc."
    )
    parser.add_argument(
        "--dpi", type=int, default=300,
        help="Render DPI (default: 300, higher=better but slower)"
    )
    parser.add_argument(
        "-p", "--pages", type=str, default=None,
        help="Page range, e.g. '1-3' or '1,3,5' (1-based). Default: all."
    )
    parser.add_argument(
        "--tesseract", type=str, default=None,
        help="Path to tesseract.exe if not in PATH."
    )
    parser.add_argument(
        "--list-langs", action="store_true",
        help="List available Tesseract languages and exit."
    )

    args = parser.parse_args()

    if args.tesseract:
        pytesseract.pytesseract.tesseract_cmd = args.tesseract

    if args.list_langs:
        langs = pytesseract.get_languages()
        print(f"Available Tesseract languages: {', '.join(langs)}")
        return

    # Parse page range
    page_list = None
    if args.pages:
        page_list = []
        for part in args.pages.split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-", 1)
                page_list.extend(range(int(a), int(b) + 1))
            else:
                page_list.append(int(part))

    # ── Searchable PDF mode ──
    if args.searchable:
        ocr_to_searchable_pdf(
            pdf_path=args.pdf,
            language=args.lang,
            dpi=args.dpi,
            output_path=args.searchable,
            pages=page_list,
        )

    # ── Text mode (always run if no --searchable, or alongside it if -o given) ──
    if not args.searchable or args.output:
        result = ocr_pdf(
            pdf_path=args.pdf,
            language=args.lang,
            dpi=args.dpi,
            output_path=args.output,
            pages=page_list,
        )
        if not args.output:
            print("\n" + result)


if __name__ == "__main__":
    main()

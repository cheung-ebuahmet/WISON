#!/usr/bin/env python3
"""
Batch convert all binary contract files under D:\Wison\Subcon_Payments\*\Contract\
to Markdown, stored in D:\Wison\_Ref\kb\subcon\ mirroring the source structure.

Methods (in order):
  .docx / .pdf → MarkItDown (best-effort, preserves tables/formatting)
                → fallback: python-docx (docx) or pymupdf (pdf)
  .doc          → Word COM → .docx → MarkItDown (requires MS Word installed)
                → fallback: olefile raw text extraction
"""

import os
import sys
import tempfile
import shutil
import traceback
from pathlib import Path

# --- Config ---
SRC_ROOT = Path(r"D:\Wison\Subcon_Payments")
DST_ROOT = Path(r"D:\Wison\_Ref\kb\subcon")
EXTENSIONS = {".docx", ".doc", ".pdf"}
SKIP_DIRS_CONTAIN = {"Pymt", "Corres", "Miscellaneous", "Invoice"}
MAX_SIZE_MB = 50

# Track results
failures = []
skipped = []
converted = []

# Word COM singleton
_word_app = None


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def relative_path(filepath: Path, root: Path) -> Path:
    try:
        return filepath.relative_to(root)
    except ValueError:
        return filepath


# ── .docx fallback ──────────────────────────────────────────────
def convert_docx_python_docx(src: Path, dst: Path) -> bool:
    try:
        import docx
        doc = docx.Document(str(src))
        lines = []
        for para in doc.paragraphs:
            lines.append(para.text)
        for table in doc.tables:
            lines.append("")
            for row in table.rows:
                cells = [cell.text.replace("\n", " ") for cell in row.cells]
                lines.append(" | ".join(cells))
        text = "\n".join(lines)
        if text.strip():
            dst.write_text(text, encoding="utf-8")
            return True
        return False
    except Exception:
        return False


# ── PDF fallback ────────────────────────────────────────────────
def convert_pdf_pymupdf(src: Path, dst: Path) -> bool:
    try:
        import fitz
        doc = fitz.open(str(src))
        pages = []
        for page in doc:
            text = page.get_text("text")
            if text.strip():
                pages.append(text)
        doc.close()
        text = "\n\n".join(pages)
        if text.strip():
            dst.write_text(text, encoding="utf-8")
            return True
        return False
    except Exception:
        return False


# ── MarkItDown (primary for .docx /.pdf) ────────────────────────
def convert_with_markitdown(src: Path, dst: Path) -> bool:
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(str(src))
        text = result.text_content
        if text and text.strip():
            dst.write_text(text, encoding="utf-8")
            return True
        return False
    except Exception:
        return False


# ── .doc via Word COM ───────────────────────────────────────────
def _get_word_app():
    """Lazy-init Word COM singleton."""
    global _word_app
    if _word_app is None:
        import win32com.client
        _word_app = win32com.client.Dispatch("Word.Application")
        _word_app.Visible = False
        _word_app.DisplayAlerts = 0  # wdAlertsNone
    return _word_app


def _word_doc_to_docx(src: Path) -> Path | None:
    """Convert .doc to .docx using Word COM. Returns path to temp .docx or None."""
    import win32com.client
    try:
        word = _get_word_app()
        # Use absolute short path to avoid Unicode issues
        src_str = str(src.resolve())
        doc = None
        try:
            doc = word.Documents.Open(src_str, ReadOnly=True)
        except Exception:
            # Try copying to temp with safe name
            tmp_src = Path(tempfile.gettempdir()) / ("_wison_conv_" + src.name)
            shutil.copy2(src, tmp_src)
            doc = word.Documents.Open(str(tmp_src), ReadOnly=True)
            try:
                tmp_src.unlink()
            except Exception:
                pass

        if doc is None:
            return None

        # Save as .docx (Format 16 = wdFormatXMLDocument)
        tmp_dst = Path(tempfile.gettempdir()) / ("_wison_conv_out_" + src.stem + ".docx")
        tmp_dst_str = str(tmp_dst)
        doc.SaveAs2(tmp_dst_str, FileFormat=16)
        doc.Close()
        return tmp_dst
    except Exception as e:
        return None


def _doc_olefile_text(src: Path) -> str | None:
    """Extract raw text from .doc via olefile (last resort)."""
    try:
        import olefile
        ole = olefile.OleFileIO(str(src))
        # Read WordDocument stream
        word_stream = ole.openstream('WordDocument').read()
        ole.close()
        # Basic extraction: try UTF-16LE decoding, skip binary
        # Word stores text in Unicode in recent .doc versions
        # Try to find text segments
        result = []
        i = 0
        while i < len(word_stream) - 1:
            # Try 16-bit characters
            char = word_stream[i:i+2]
            try:
                ch = char.decode('utf-16-le')
                if ch.isprintable() or ch in '\n\r\t':
                    result.append(ch)
                else:
                    if result and result[-1] != '\n':
                        result.append('\n')
            except:
                pass
            i += 2
        text = ''.join(result)
        # Filter: keep only lines with actual content
        lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 3]
        return '\n'.join(lines) if lines else None
    except Exception:
        return None


def convert_doc_file(src: Path, dst: Path) -> bool:
    """Convert .doc file using Word COM → .docx → MarkItDown."""
    # Method 1: Word COM
    tmp_docx = _word_doc_to_docx(src)
    if tmp_docx and tmp_docx.exists():
        try:
            if convert_with_markitdown(tmp_docx, dst):
                try: tmp_docx.unlink()
                except: pass
                return True
            try: tmp_docx.unlink()
            except: pass
        except Exception:
            try: tmp_docx.unlink()
            except: pass

    # Method 2: Word COM → python-docx (if MarkItDown failed)
    tmp_docx2 = _word_doc_to_docx(src)
    if tmp_docx2 and tmp_docx2.exists():
        try:
            if convert_docx_python_docx(tmp_docx2, dst):
                try: tmp_docx2.unlink()
                except: pass
                return True
            try: tmp_docx2.unlink()
            except: pass
        except Exception:
            try: tmp_docx2.unlink()
            except: pass

    # Method 3: olefile raw text (last resort)
    text = _doc_olefile_text(src)
    if text and text.strip():
        dst.write_text(text, encoding="utf-8")
        return True

    return False


# ── Main conversion dispatcher ──────────────────────────────────
def try_convert(src: Path, dst: Path) -> str:
    """Returns "ok" or "fail"."""
    ext = src.suffix.lower()
    ensure_dir(dst.parent)

    if ext == ".doc":
        if convert_doc_file(src, dst):
            return "ok"
        return "fail"

    # .docx and .pdf
    if convert_with_markitdown(src, dst):
        return "ok"

    if ext == ".docx":
        if convert_docx_python_docx(src, dst):
            return "ok"
    elif ext == ".pdf":
        if convert_pdf_pymupdf(src, dst):
            return "ok"

    return "fail"


def should_process(filepath: Path) -> bool:
    if filepath.suffix.lower() not in EXTENSIONS:
        return False
    try:
        size_mb = filepath.stat().st_size / (1024 * 1024)
        if size_mb > MAX_SIZE_MB:
            skipped.append((str(filepath), f"Too large: {size_mb:.1f} MB"))
            return False
    except OSError:
        return False
    return True


def process_directory(subcon_dir: Path):
    contract_dir = subcon_dir / "Contract"
    if not contract_dir.exists():
        return

    for root, dirs, files in os.walk(contract_dir):
        root_path = Path(root)
        for fname in files:
            fpath = root_path / fname
            if not should_process(fpath):
                continue

            rel = relative_path(fpath, SRC_ROOT)
            dst = DST_ROOT / rel.with_suffix(rel.suffix + ".md")

            if dst.exists():
                try:
                    if dst.stat().st_mtime >= fpath.stat().st_mtime:
                        continue
                except OSError:
                    pass

            print(f"  {rel}")
            result = try_convert(fpath, dst)

            if result == "ok":
                converted.append(str(rel))
            else:
                failures.append(str(rel))
                print(f"    *** FAILED ***")


def main():
    global _word_app
    print("=" * 70)
    print("Wison Subcontract Binary → Markdown Batch Converter")
    print(f"Source: {SRC_ROOT}")
    print(f"Destination: {DST_ROOT}")
    print("=" * 70)

    ensure_dir(DST_ROOT)

    for entry in sorted(SRC_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if any(s in str(entry) for s in SKIP_DIRS_CONTAIN):
            print(f"\nSKIP (non-contract): {entry.name}")
            continue

        print(f"\n{'='*70}")
        print(f"PROCESSING: {entry.name}")
        print(f"{'='*70}")
        process_directory(entry)

    # Clean up Word
    if _word_app is not None:
        try:
            _word_app.Quit()
        except Exception:
            pass
        _word_app = None

    # --- Report ---
    print("\n\n" + "=" * 70)
    print("CONVERSION REPORT")
    print("=" * 70)
    print(f"  Converted: {len(converted)}")
    print(f"  Skipped:   {len(skipped)}")
    print(f"  Failed:    {len(failures)}")

    if failures:
        print("\n--- FAILED FILES ---")
        for f in failures:
            print(f"  FAIL: {f}")

    report_path = DST_ROOT / "_conversion_report.txt"
    with open(report_path, "w", encoding="utf-8") as rpt:
        rpt.write(f"Conversion Report\n{'='*60}\n")
        rpt.write(f"Converted: {len(converted)}\n")
        rpt.write(f"Skipped: {len(skipped)}\n")
        rpt.write(f"Failed: {len(failures)}\n\n")
        if failures:
            rpt.write("--- FAILED ---\n")
            for f in failures:
                rpt.write(f"  {f}\n")
        rpt.write("\n--- CONVERTED ---\n")
        for f in sorted(converted):
            rpt.write(f"  {f}\n")
    print(f"\nReport: {report_path}")


if __name__ == "__main__":
    main()

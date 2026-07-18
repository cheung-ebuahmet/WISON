#!/usr/bin/env python3
"""
Permanently convert .doc → .docx in Subcon_Payments source directories.

Rules:
  - Word COM opens .doc, saves as .docx (Format=16) in same directory
  - On success: move .doc to Recycle Bin (NEVER permanent delete)
  - If .docx already exists and is newer: skip .doc (already done)
  - Dry-run mode so you can review before executing
"""

import os
import sys
import glob
import tempfile
import shutil
from pathlib import Path

SRC_ROOT = Path(r"D:\Wison\Subcon_Payments")
DRY_RUN = "--execute" not in sys.argv  # safe by default


def send_to_recycle_bin(filepath: Path):
    """Move file to Windows Recycle Bin."""
    import winshell
    winshell.delete_file(str(filepath), no_confirm=True, allow_undo=True)


def send_to_recycle_bin_vb(filepath: Path):
    """Fallback: use VisualBasic COM to send to Recycle Bin."""
    import clr
    clr.AddReference("Microsoft.VisualBasic")
    from Microsoft.VisualBasic.FileIO import FileSystem
    FileSystem.DeleteFile(
        str(filepath),
        Microsoft.VisualBasic.FileIO.UIOption.OnlyErrorDialogs,
        Microsoft.VisualBasic.FileIO.RecycleOption.SendToRecycleBin,
    )


def recycle(filepath: Path):
    """Send a file to Recycle Bin. Try multiple methods."""
    path_str = str(filepath.resolve())
    if DRY_RUN:
        print(f"    [DRY-RUN] Would recycle: {path_str}")
        return True

    # Method 1: winshell
    try:
        import winshell
        winshell.delete_file(path_str, no_confirm=True, allow_undo=True)
        print(f"    -> Recycled: {filepath.name}")
        return True
    except Exception:
        pass

    # Method 2: Pythonnet + VB
    try:
        import clr
        clr.AddReference("Microsoft.VisualBasic")
        from Microsoft.VisualBasic.FileIO import FileSystem
        FileSystem.DeleteFile(
            path_str,
            Microsoft.VisualBasic.FileIO.UIOption.OnlyErrorDialogs,
            Microsoft.VisualBasic.FileIO.RecycleOption.SendToRecycleBin,
        )
        print(f"    -> Recycled (VB): {filepath.name}")
        return True
    except Exception:
        pass

    # Method 3: PowerShell COM via subprocess
    try:
        import subprocess
        ps_cmd = (
            f'[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile('
            f'"{path_str}",'
            f'[Microsoft.VisualBasic.FileIO.UIOption]::OnlyErrorDialogs,'
            f'[Microsoft.VisualBasic.FileIO.RecycleOption]::SendToRecycleBin'
            f')'
        )
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             f'Add-Type -AssemblyName Microsoft.VisualBasic; {ps_cmd}'],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print(f"    -> Recycled (PS): {filepath.name}")
            return True
        else:
            print(f"    PS error: {result.stderr}")
    except Exception as e:
        print(f"    PS exception: {e}")

    print(f"    *** COULD NOT RECYCLE: {filepath.name}")
    return False


def convert_doc_to_docx(doc_path: Path) -> Path | None:
    """Convert .doc to .docx using Word COM. Returns path to new .docx."""
    docx_path = doc_path.with_suffix(".docx")

    # Already converted?
    if docx_path.exists():
        if docx_path.stat().st_mtime >= doc_path.stat().st_mtime:
            return docx_path  # already up to date

    if DRY_RUN:
        print(f"  [DRY-RUN] Would convert: {doc_path.name} -> {docx_path.name}")
        return docx_path

    import win32com.client
    word = None
    tmp_docx = None
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0

        doc = word.Documents.Open(str(doc_path.resolve()), ReadOnly=True)
        tmp_docx = Path(tempfile.gettempdir()) / ("_wison_perm_" + doc_path.stem + ".docx")
        doc.SaveAs2(str(tmp_docx), FileFormat=16)  # wdFormatXMLDocument
        doc.Close()

        # Move tmp file to target directory
        shutil.move(str(tmp_docx), str(docx_path))
        print(f"  Converted: {doc_path.name} -> {docx_path.name}")
        return docx_path
    except Exception as e:
        print(f"  FAILED converting {doc_path.name}: {e}")
        return None
    finally:
        if word:
            try:
                word.Quit()
            except Exception:
                pass


def main():
    doc_files = sorted(Path(r"D:\Wison\Subcon_Payments").rglob("*.doc"))
    # Filter out .docx (rglob *.doc also matches *.docx on some systems)
    doc_files = [f for f in doc_files if f.suffix.lower() == ".doc"]

    print("=" * 70)
    print(".doc -> .docx Permanent Conversion")
    print(f"Mode: {'DRY-RUN' if DRY_RUN else 'EXECUTE (LIVE)'}")
    print(f"Found {len(doc_files)} .doc files")
    print("=" * 70)

    if not doc_files:
        print("Nothing to do.")
        return

    converted = []
    failed = []
    recycled = []

    for doc_path in doc_files:
        print(f"\n{doc_path.relative_to(SRC_ROOT)}")
        docx_path = convert_doc_to_docx(doc_path)

        if docx_path and docx_path.exists():
            converted.append(doc_path)
            if recycle(doc_path):
                recycled.append(doc_path)
        else:
            failed.append(doc_path)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Converted: {len(converted)}")
    print(f"  Recycled: {len(recycled)}")
    print(f"  Failed:    {len(failed)}")
    if mode == "DRY-RUN":
        print(f"\n  Run with --execute to perform the conversion.")
    if failed:
        print("\n  FAILED files (still exist as .doc):")
        for f in failed:
            print(f"    {f}")


if __name__ == "__main__":
    mode = "DRY-RUN" if DRY_RUN else "LIVE"
    main()

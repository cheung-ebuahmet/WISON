#!/usr/bin/env python
"""
场景 A：原生电子版/已 OCR 的 PDF → Markdown
使用 PyMuPDF (fitz) 提取文本块，原地生成同名 .md 文件。

适用条件：PDF 中可以选中/复制文字
速度：    极快（纯文本提取，无 OCR）
输出：    原 PDF 同级目录下同名 .md，含元数据头 + 分页标记

用法：
    python pdf_to_md_native.py "文件.pdf"
    python pdf_to_md_native.py "文件.pdf" -o "指定输出.md"
    python pdf_to_md_native.py "文件.pdf" --no-page-breaks   # 不分页
"""

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import fitz  # PyMuPDF


def pdf_to_md(pdf_path, output_path=None, page_breaks=True):
    """
    从原生 PDF 提取文字并写入 Markdown。

    Args:
        pdf_path:     PDF 文件路径
        output_path:  输出 .md 路径（默认：同名 .md，原地）
        page_breaks:  是否在页面之间插入 --- 分隔符

    Returns:
        输出的 .md 文件 Path
    """
    src = Path(pdf_path).resolve()

    if not src.exists():
        raise FileNotFoundError(f"找不到 PDF: {src}")

    if output_path:
        md_path = Path(output_path).resolve()
    else:
        md_path = src.with_suffix(".md")

    doc = fitz.open(str(src))
    page_count = len(doc)

    # ── 元数据头 ────────────────────────────────
    now_utc = datetime.now(timezone.utc).isoformat(timespec="seconds")
    metadata = (
        f"<!--\n"
        f"  source:  {src}\n"
        f"  date:    {now_utc}\n"
        f"  method:  fitz (PyMuPDF) text extraction\n"
        f"  pages:   {page_count}\n"
        f"-->\n\n"
    )

    # ── 提取正文 ────────────────────────────────
    lines = [metadata]

    for i, page in enumerate(doc, start=1):
        # get_text("text") 保留物理位置间距，对段落/表格友好
        text = page.get_text("text")
        if text.strip():
            lines.append(text.rstrip())
        else:
            lines.append(f"[第 {i} 页 — 无可提取文字]")

        if page_breaks and i < page_count:
            lines.append("\n---\n")

    doc.close()

    # ── 写出 ────────────────────────────────────
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")

    return md_path, page_count


# ── CLI ────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="原生 PDF → Markdown（fitz 文本提取）",
    )
    parser.add_argument("pdf", help="PDF 文件路径")
    parser.add_argument("-o", "--output", help="输出 .md 路径（默认: 同名原地）")
    parser.add_argument(
        "--no-page-breaks",
        action="store_true",
        help="不在页面之间插入 --- 分隔符",
    )
    args = parser.parse_args()

    try:
        out_path, pages = pdf_to_md(
            args.pdf,
            output_path=args.output,
            page_breaks=not args.no_page_breaks,
        )
        print(f"✅ 原生 PDF → Markdown 完成")
        print(f"   源文件:      {args.pdf}")
        print(f"   页数:        {pages}")
        print(f"   输出:        {out_path}")
        print(f"   方式:        fitz (PyMuPDF) 文本块提取")
    except Exception as e:
        print(f"❌ 转换失败: {e}", file=sys.stderr)
        sys.exit(1)

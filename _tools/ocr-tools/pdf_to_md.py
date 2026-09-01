#!/usr/bin/env python
"""
PDF → Markdown 统一入口
自动检测 PDF 类型 → 路由到最佳处理管线。

检测逻辑：
  - 前 3 页的可提取文字总量 >= 50 字符 → 原生 PDF（fitz 文本提取）
  - 否则 → 扫描版 OCR（pymupdf 渲染 + PaddleOCR 识别）

用法：
    python pdf_to_md.py "文件.pdf"                    # 自动检测，原地生成 .md
    python pdf_to_md.py "文件.pdf" --force-ocr        # 强制 OCR
    python pdf_to_md.py "文件.pdf" --force-native     # 强制原生文本提取
    python pdf_to_md.py "文件.pdf" --dpi 200          # OCR 精度
    python pdf_to_md.py "文件.pdf" --lang en          # OCR 语言
    python pdf_to_md.py "文件.pdf" -p 1-5             # 指定页码范围

依赖：
    原生模式：fitz (PyMuPDF)
    OCR 模式：  paddlepaddle + paddleocr + fitz + pillow
"""

import argparse
import sys
from pathlib import Path

import fitz  # PyMuPDF


def _count_extractable_text(pdf_path, sample_pages=3):
    """快速采样检测 PDF 是否含有可提取文字。"""
    doc = fitz.open(str(pdf_path))
    total = 0
    pages_to_check = min(sample_pages, len(doc))
    for i in range(pages_to_check):
        text = doc[i].get_text("text")
        total += len(text.strip())
    doc.close()
    return total


def main():
    parser = argparse.ArgumentParser(
        description="PDF → Markdown（自动检测：原生文本提取 / PaddleOCR）",
    )
    parser.add_argument("pdf", help="PDF 文件路径")
    parser.add_argument("-o", "--output", help="输出 .md 路径（默认: 同名原地）")
    parser.add_argument(
        "--force-ocr",
        action="store_true",
        help="强制使用 OCR 模式（即使检测到可选文字）",
    )
    parser.add_argument(
        "--force-native",
        action="store_true",
        help="强制使用原生文本提取模式",
    )
    parser.add_argument("--dpi", type=int, default=150, help="OCR DPI（默认: 150）")
    parser.add_argument("--lang", default="ch", help="OCR 语言（默认: ch）")
    parser.add_argument("-p", "--pages", help="页码范围，如 '1-5'")
    args = parser.parse_args()

    src = Path(args.pdf).resolve()
    if not src.exists():
        print(f"❌ 找不到文件: {src}", file=sys.stderr)
        sys.exit(1)

    # ── 判断使用哪种管线 ────────────────────────
    if args.force_native:
        mode = "native"
    elif args.force_ocr:
        mode = "ocr"
    else:
        char_count = _count_extractable_text(src)
        print(f"📊 前 3 页可提取文字: {char_count} 字符")
        mode = "native" if char_count >= 50 else "ocr"

    print(f"🔀 使用管线: {'原生文本提取 (fitz)' if mode == 'native' else '扫描版 OCR (pymupdf + PaddleOCR)'}")
    print()

    # ── 执行 ────────────────────────────────────
    if mode == "native":
        from pdf_to_md_native import pdf_to_md
        out_path, pages = pdf_to_md(args.pdf, output_path=args.output)
    else:
        from pdf_to_md_ocr import scanned_pdf_to_md
        out_path, pages = scanned_pdf_to_md(
            args.pdf,
            output_path=args.output,
            dpi=args.dpi,
            lang=args.lang,
            pages_range=args.pages,
        )

    print(f"\n✅ PDF → Markdown 完成")
    print(f"   方式:  {mode}")
    print(f"   页数:  {pages}")
    print(f"   输出:  {out_path}")


if __name__ == "__main__":
    main()

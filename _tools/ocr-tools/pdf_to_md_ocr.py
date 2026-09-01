#!/usr/bin/env python
"""
场景 B：扫描版/纯图片 PDF → Markdown（全离线 OCR）
使用 PyMuPDF (fitz) 渲染页面 → PaddleOCR 识别中英文 → 原地生成同名 .md。

适用条件：PDF 中无法选中文字（纯扫描版/图片型）
速度：    较慢（逐页 OCR），150 DPI 下约 2-4 秒/页
依赖：    paddlepaddle + paddleocr + pymupdf + pillow
         首次运行会自动下载 PaddleOCR 离线模型（约 30 MB）

用法：
    python pdf_to_md_ocr.py "扫描版.pdf"
    python pdf_to_md_ocr.py "扫描版.pdf" -o "指定输出.md"
    python pdf_to_md_ocr.py "扫描版.pdf" --dpi 200          # 更高精度
    python pdf_to_md_ocr.py "扫描版.pdf" --lang en          # 仅英文
    python pdf_to_md_ocr.py "扫描版.pdf" -p 1-5             # 指定页码范围
"""

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile

import fitz  # PyMuPDF — PDF 渲染（无需 poppler）
import numpy as np
from PIL import Image

# PaddleOCR 延迟加载（首次 import 时会下载离线模型）
_paddle_ocr = None


def _get_ocr(lang="ch"):
    """延迟初始化 PaddleOCR 实例（单例）"""
    global _paddle_ocr
    if _paddle_ocr is None:
        from paddleocr import PaddleOCR
        _paddle_ocr = PaddleOCR(use_angle_cls=True, lang=lang)
    return _paddle_ocr


def pdf_page_to_image(page, dpi=150):
    """
    将 PyMuPDF 页面渲染为 numpy 数组（RGB）。

    不使用 pdf2image/poppler — pymupdf 原生渲染。
    """
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombuffer("RGB", (pix.width, pix.height), pix.samples, "raw", "RGB", 0, 1)
    return np.array(img)


def scanned_pdf_to_md(pdf_path, output_path=None, dpi=150, lang="ch", pages_range=None):
    """
    对扫描版 PDF 执行 OCR 并写入 Markdown。

    Args:
        pdf_path:     PDF 文件路径
        output_path:  输出 .md 路径（默认: 同名 .md）
        dpi:          渲染 DPI（默认 150，数值越高精度越好但越慢）
        lang:         PaddleOCR 语言代码 ("ch", "en", "korean" 等)
        pages_range:  页码范围，如 "1-5"（None = 全部）

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

    # ── 解析页码范围 ────────────────────────────
    doc = fitz.open(str(src))
    total_pages = len(doc)

    if pages_range:
        parts = pages_range.split("-")
        start = int(parts[0]) - 1
        end = int(parts[1]) if len(parts) > 1 else start + 1
        start = max(0, start)
        end = min(total_pages, end)
    else:
        start, end = 0, total_pages

    page_indices = range(start, end)
    page_count = len(page_indices)

    # ── 元数据头 ────────────────────────────────
    now_utc = datetime.now(timezone.utc).isoformat(timespec="seconds")
    metadata = (
        f"<!--\n"
        f"  source:  {src}\n"
        f"  date:    {now_utc}\n"
        f"  method:  PaddleOCR (pymupdf render → PaddleOCR recognition)\n"
        f"  pages:   {total_pages} (processed: {start + 1}–{end})\n"
        f"  dpi:     {dpi}\n"
        f"  lang:    {lang}\n"
        f"-->\n\n"
    )

    # ── OCR ─────────────────────────────────────
    ocr = _get_ocr(lang)
    lines = [metadata]

    for i, page_idx in enumerate(page_indices, start=1):
        page = doc[page_idx]
        page_num = page_idx + 1

        print(f"  [{i}/{page_count}] 正在 OCR 第 {page_num} 页...", end=" ", flush=True)

        # 渲染页面为 numpy 数组（无需写入临时文件）
        img_array = pdf_page_to_image(page, dpi=dpi)

        # PaddleOCR 识别 (输入: numpy array)
        result = ocr.ocr(img_array, cls=True)

        if result and result[0] is not None:
            # 提取文字行，按 Y 坐标排序以保持阅读顺序
            entries = []
            for entry in result[0]:
                box = entry[0]         # [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
                text = entry[1][0]     # 识别文字
                confidence = entry[1][1]  # 置信度
                y_center = (box[0][1] + box[2][1]) / 2
                entries.append((y_center, text, confidence))

            # 按 Y 坐标（从上到下）排序
            entries.sort(key=lambda e: e[0])

            page_text = "\n".join(text for _, text, _ in entries)
            lines.append(page_text)
        else:
            lines.append(f"[第 {page_num} 页 — 未识别到文字]")

        if page_idx < end - 1:
            lines.append("\n---\n")

        print("✓")

    doc.close()

    # ── 写出 ────────────────────────────────────
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(lines), encoding="utf-8")

    return md_path, page_count


# ── CLI ────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="扫描版 PDF → Markdown（pymupdf + PaddleOCR）",
    )
    parser.add_argument("pdf", help="PDF 文件路径")
    parser.add_argument("-o", "--output", help="输出 .md 路径（默认: 同名原地）")
    parser.add_argument("--dpi", type=int, default=150, help="渲染 DPI（默认: 150）")
    parser.add_argument("--lang", default="ch", help="OCR 语言（默认: ch，可选: en, korean, japan 等）")
    parser.add_argument("-p", "--pages", help="页码范围，如 '1-5'（默认: 全部）")
    args = parser.parse_args()

    try:
        out_path, pages = scanned_pdf_to_md(
            args.pdf,
            output_path=args.output,
            dpi=args.dpi,
            lang=args.lang,
            pages_range=args.pages,
        )
        print(f"\n🚀 扫描版 PDF → Markdown 完成")
        print(f"   源文件:      {args.pdf}")
        print(f"   处理页数:    {pages}")
        print(f"   输出:        {out_path}")
        print(f"   方式:        pymupdf (渲染) → PaddleOCR (识别)")
    except Exception as e:
        print(f"❌ 转换失败: {e}", file=sys.stderr)
        sys.exit(1)

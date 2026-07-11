# PDF → Markdown 转换指南

## 📍 工具位置

```
脚本：D:\Applications\ocr-tools\pdf_to_md.py          ← 统一入口（推荐）
      D:\Applications\ocr-tools\pdf_to_md_native.py    ← 电子版 PDF
      D:\Applications\ocr-tools\pdf_to_md_ocr.py       ← 扫描版 PDF

引擎：Python          D:\Program Files\Python310\python.exe
      模型缓存        D:\Documents\My Projects\PaddleOCR\models\
      环境变量        PADDLEX_HOME=D:\Documents\My Projects\PaddleOCR\models
```

---

## 🎯 一步到位（推荐）

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md.py "你的文件.pdf"
```

自动判断 PDF 类型：电子版→秒级文本提取 / 扫描版→PaddleOCR 识别。

输出：**同目录下同名 `.md` 文件**。

---

## 📋 常用命令

### 指定输出位置

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md.py "D:\A\扫描件.pdf" -o "D:\B\结果.md"
```

### 扫描版：更高精度（更慢）

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md_ocr.py "文件.pdf" --dpi 200
```

### 扫描版：只处理指定页码范围

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md_ocr.py "文件.pdf" -p 3-15
```

### 扫描版：仅英文文档（默认中英）

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md_ocr.py "英文.pdf" --lang en
```

### 强制使用电子版模式

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md.py "文件.pdf" --force-native
```

---

## 📦 批量转换整个文件夹

```powershell
# D:\A\ 下所有 PDF → D:\B\ 下同名 MD
Get-ChildItem "D:\A\*.pdf" | ForEach-Object {
    $out = "D:\B\" + $_.BaseName + ".md"
    D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md.py $_.FullName -o $out
}
```

---

## ⊞ 在 Claude Code 窗口中执行

### 方式一：直接让 Claude 帮你跑

在 Claude Code 对话框输入：

```
帮我把 D:\A\A0.pdf 转为 Markdown，输出到 D:\B\A0.md
```

Claude 会自动调用对应脚本执行。你什么都不用记。

### 方式二：自己粘贴命令

在 Claude Code 中直接粘贴 PowerShell 命令即可：

```powershell
D:\Program Files\Python310\python.exe D:\Applications\ocr-tools\pdf_to_md.py "D:\A\A0.pdf" -o "D:\B\A0.md"
```

---

## ⚙️ 两套 OCR 引擎

| | Tesseract | PaddleOCR |
|------|-----------|------------|
| 语言 | 简中 / 繁中 / 英文 / 阿拉伯语 | 中英（内置） |
| 速度 | 快 | 中等（2-4秒/页） |
| 中英混合 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 用法 | `pdf_ocr.py --tesseract ...` | `pdf_to_md_ocr.py` |
| 用途 | 通用 OCR / 可搜索 PDF | 扫描件转 Markdown |

---

## 🛠️ 什么是"可选中文字"？

打开 PDF → 鼠标拖选文字 → 能选中 = 电子版（用 `native`）。
拖选不了 = 扫描版（用 `ocr`）。
统一入口 `pdf_to_md.py` 会自动判断，你不需要自己猜。

---

## 🔗 相关工具

| 需求 | 命令 |
|------|------|
| OCR → 纯文本文件 | `pdf_ocr.py "文件.pdf" -o 结果.txt --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe"` |
| OCR → 可搜索 PDF | `pdf_ocr.py "文件.pdf" --searchable "可搜索.pdf" --tesseract "..."` |
| Tesseract 多语言 | 加 `-l chi_sim+eng` / `-l chi_tra+eng` / `-l ara+eng` |

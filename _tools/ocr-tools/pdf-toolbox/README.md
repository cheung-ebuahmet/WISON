# PDF Toolbox

Python 全栈 PDF 工具箱 — OCR 识别、可搜索 PDF 生成、页面操作、批量处理。

---

## 已安装组件

| 组件 | 路径 | 版本 |
|------|------|------|
| Python | `D:\Program Files\Python310\python.exe` | 3.10.11 |
| Tesseract OCR 引擎 | `D:\Program Files\Tesseract-OCR\tesseract.exe` | 5.4.0 |
| OCR 脚本 (Tesseract) | `D:\Wison\_tools\ocr-tools\pdf_ocr.py` | — |
| PDF → MD (原生) | `D:\Wison\_tools\ocr-tools\pdf_to_md_native.py` | — |
| PDF → MD (OCR) | `D:\Wison\_tools\ocr-tools\pdf_to_md_ocr.py` | — |
| PDF → MD (统一入口) | `D:\Wison\_tools\ocr-tools\pdf_to_md.py` | — |
| PDF24 Creator (GUI) | `D:\Program Files\PDF24\pdf24.exe` | 11.30.1 |

### Python 库（全部 15 个包，已备份至 `pip freeze`）

| 库 | 导入名 | 版本 | 用途 |
|----|--------|------|------|
| PyMuPDF | `fitz` | 1.27.2 | PDF 渲染（→图片供 OCR）、页面编辑、合并拆分 |
| pytesseract | `pytesseract` | 0.3.13 | 调用 Tesseract 识别文字 |
| pdfplumber | `pdfplumber` | 0.11.10 | 提取文字 / 表格（非扫描 PDF，支持视觉调试） |
| pikepdf | `pikepdf` | 10.9.0 | 底层 PDF 操作（旋转、元数据、修复） |
| pypdfium2 | `pypdfium2` | 5.10.1 | 备选 PDF 渲染引擎（Google PDFium 绑定） |
| pdfminer.six | `pdfminer` | 20260107 | 纯 Python PDF 文字提取（无外部依赖） |
| pdf2image | `pdf2image` | 1.17.0 | ⚠️ 已装但**不用**（需 poppler，已由 pymupdf 替代） |
| pillow | `PIL` | 12.2.0 | 图片处理、格式转换 |
| lxml | `lxml` | 6.1.1 | XML/HTML 解析（pdfminer 等库的依赖） |
| cryptography | `cryptography` | 49.0.0 | 加密/签名（pikepdf 依赖） |
| cffi | `cffi` | 2.0.0 | C 扩展接口（cryptography 依赖） |
| pycparser | `pycparser` | 3.0 | C 解析器（cffi 依赖） |
| packaging | `packaging` | 26.2 | 版本号解析 |
| charset-normalizer | `charset_normalizer` | 3.4.7 | 字符编码检测 |
| typing_extensions | `typing_extensions` | 4.15.0 | 类型注解兼容层 |
| paddlepaddle | `paddle` | latest | 百度深度学习框架（PaddleOCR 后端） |
| paddleocr | `paddleocr` | latest | 离线 OCR 引擎（中英日韩），无需 Tesseract |

> **🔄 备份**：`pip freeze > requirements.txt` 已纳入 `D:\Program Files\Backup` 自动备份。新设备上执行 `pip install -r requirements.txt` 即可一键还原所有 Python 包。

### Tesseract 语言包

| 代码 | 语言 | 文件 |
|------|------|------|
| `eng` | English (US) | `tessdata\eng.traineddata` |
| `chi_sim` | 简体中文 | `tessdata\chi_sim.traineddata` |
| `chi_tra` | 繁體中文 | `tessdata\chi_tra.traineddata` |
| `ara` | العربية | `tessdata\ara.traineddata` |

---

## 🎯 PDF → Markdown（新 — 原地生成 .md）

### 统一入口

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_to_md.py "文件.pdf"
```

自动检测 PDF 类型：
- 前 3 页可提取 ≥50 字符 → **原生模式**（fitz 文本提取，秒级）
- 否则 → **OCR 模式**（pymupdf 渲染 + PaddleOCR 识别，2-4 秒/页）

输出：**原 PDF 同级目录下同名 .md 文件**（含元数据头 `<!-- source: … method: … -->`）。

### 原生 PDF 直接转 MD（场景 A）

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_to_md_native.py "文件.pdf"
```

适用：电子版 PDF（可选中文字）。速度极快，保留段落物理位置。

### 扫描版 PDF OCR 转 MD（场景 B）

```powershell
# 中英混合 OCR
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_to_md_ocr.py "扫描版.pdf"

# 仅英文
… --lang en

# 更高精度（但更慢）
… --dpi 200

# 指定页码范围
… -p 1-5
```

适用：纯图片 PDF / 扫描件。全离线运行（首次自动下载 30MB 模型）。

---

## 快速上手

### 1. OCR 扫描 PDF → 纯文本

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py "文件.pdf" --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 2. OCR → 保存为 .txt

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py "文件.pdf" -o 结果.txt --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. OCR → 可搜索 PDF（文字层叠加在原图上）

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py "文件.pdf" --searchable 可搜索.pdf --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 4. 指定语言

```powershell
# 中英混合（常用）
… -l chi_sim+eng

# 繁中 + 英文
… -l chi_tra+eng

# 阿拉伯语 + 英文
… -l ara+eng

# 单独中文
… -l chi_sim
```

### 5. 指定页码 / 提高精度

```powershell
# 只 OCR 第 3-7 页
… -p 3-7

# 提高分辨率（300→400 DPI，更慢但更准）
… --dpi 400

# 跳页组合
… -p 1,3,5-8
```

### 6. 查看可用语言

```powershell
D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py --list-langs --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 页面操作（Python 脚本）

以下脚本可直接复制修改使用。

### 删除页面

```python
import fitz
doc = fitz.open(r"原始.pdf")
doc.delete_pages(3, 5)      # 删除第 4 和第 6 页（0-based）
doc.delete_pages(from_page=0, to_page=2)  # 删除前 3 页
doc.save(r"删页后.pdf")
doc.close()
```

### 合并多个 PDF

```python
import fitz
doc = fitz.open()
for path in [r"文件1.pdf", r"文件2.pdf", r"文件3.pdf"]:
    doc.insert_pdf(fitz.open(path))
doc.save(r"合并后.pdf")
doc.close()
```

### 拆分 PDF（每页单独保存）

```python
import fitz
doc = fitz.open(r"原始.pdf")
for i in range(doc.page_count):
    new = fitz.open()
    new.insert_pdf(doc, from_page=i, to_page=i)
    new.save(rf"第{i+1}页.pdf")
    new.close()
doc.close()
```

### 旋转页面

```python
import fitz
doc = fitz.open(r"原始.pdf")
page = doc[0]                # 第 1 页
page.set_rotation(90)        # 顺时针 90°
doc.save(r"旋转后.pdf")
doc.close()
```

### 提取图片

```python
import fitz
doc = fitz.open(r"原始.pdf")
for i in range(doc.page_count):
    for img in doc[i].get_images(full=True):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:         # GRAY 或 RGB
            pix.save(rf"page{i+1}_img{xref}.png")
        else:                 # CMYK → 转 RGB
            fitz.Pixmap(fitz.csRGB, pix).save(rf"page{i+1}_img{xref}.png")
doc.close()
```

---

## 核心原理

```
扫描 PDF（纯图片）
    │
    ▼ fitz.open() + page.get_pixmap()
PIL Image（内存中的位图）
    │
    ▼ pytesseract.image_to_string() / image_to_data()
识别的文字
    │
    ├─→ .txt 文本文件
    │
    └─→ page.insert_text(render_mode=3) → 保存在原始 PDF 上
             可搜索/可框选的 PDF（文字透明叠加层）
```

**不需要 poppler** — pymupdf (fitz) 内置 PDF 渲染引擎，直接将 PDF 页面转为像素图。

**render_mode=3** — pymupdf 的"不可见但可选择/可搜索"模式。文字叠加在原图上方但完全不遮挡。

---

## 文件清单

```
D:\Wison\_tools\ocr-tools\
├── pdf_ocr.py                       ← OCR 主脚本 (Tesseract)
├── pdf_to_md_native.py              ← 原生 PDF → MD（fitz 文本提取）
├── pdf_to_md_ocr.py                 ← 扫描版 PDF → MD（pymupdf + PaddleOCR）
├── pdf_to_md.py                     ← 统一入口（自动检测）**
├── pdf-toolbox\                     ← 本 README 所在文件夹
│   └── README.md
├── python-3.10.11-embed-amd64.zip   ← Python 嵌入版源文件（备查）

D:\Program Files\
├── Python310\                       ← Python 3.10.11 + pip 包
├── Tesseract-OCR\                   ← Tesseract 5.4.0 + 语言包
│   └── tessdata\
│       ├── eng.traineddata
│       ├── chi_sim.traineddata
│       ├── chi_tra.traineddata
│       └── ara.traineddata
├── PDF24\                           ← PDF24 Creator (GUI 备用)
└── Backup\                          ← 自动备份（含 Python310 包清单）
    └── configs\Python310\requirements.txt
```

### 🔍 两套 OCR 引擎对比

| | Tesseract | PaddleOCR |
|------|-----------|-----------|
| 引擎文件 | `D:\Program Files\Tesseract-OCR\` | Python 包内 |
| 语言包 | eng / chi_sim / chi_tra / ara | ch / en（内置，离线模型） |
| 中英识别率 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 速度 | 快 | 中等 |
| 输出格式 | 纯文本 / 可搜索 PDF / 文本文件 | 纯文本 / Markdown |
| 安装 | 独立 exe 安装 | pip 安装 + 首次自动下载模型 (~30MB) |
| 使用脚本 | `pdf_ocr.py` | `pdf_to_md_ocr.py` |
| 适用场景 | 通用 OCR / 生成可搜索 PDF | 中英扫描件 → Markdown |

## 恢复 Python 环境

新设备 / 重装后快速重建 PDF 工具链：

```powershell
# 1. 安装 Python 3.10 到 D:\Program Files\Python310\
# 2. 确保 pip 可用：
D:\Program Files\Python310\python.exe -m ensurepip

# 3. 一键安装全部 PDF 相关包：
D:\Program Files\Python310\python.exe -m pip install -r "D:\Program Files\Backup\configs\Python310\requirements.txt"

# 4. 安装 Tesseract-OCR 5.x → D:\Program Files\Tesseract-OCR\
#    https://github.com/UB-Mannheim/tesseract/wiki
#    安装时勾选中文 + 阿拉伯语语言包
```

---

## 常用命令别名建议

把以下内容加到 PowerShell Profile（`$PROFILE`）中，简化日常使用：

```powershell
# PDF OCR 别名
function ocr-pdf { D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py @args }
function ocr-cn  { D:\Program Files\Python310\python.exe D:\Wison\_tools\ocr-tools\pdf_ocr.py @args -l chi_sim+eng --tesseract "D:\Program Files\Tesseract-OCR\tesseract.exe" }
```

使用效果：

```powershell
ocr-cn "扫描件.pdf" -o 结果.txt
ocr-cn "扫描件.pdf" --searchable 可搜索.pdf
```

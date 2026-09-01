# 工具箱索引

本机已安装的工具、脚本、环境速查。

---

## PDF 处理

| 工具 | 路径 | 用途 |
|------|------|------|
| OCR 脚本 | `D:\Wison\_tools\ocr-tools\pdf_ocr.py` | 扫描 PDF → 文字 / 可搜索 PDF |
| 使用手册 | `D:\Wison\_tools\ocr-tools\pdf-toolbox\README.md` | 命令示例、语言包、代码模板 |
| PDF24 Creator | `D:\Program Files\PDF24\pdf24.exe` | GUI 页面合并/删除/旋转/压缩/OCR |

### OCR 常用命令

```powershell
$py = "D:\Program Files\Python310\python.exe"
$ocr = "D:\Wison\_tools\ocr-tools\pdf_ocr.py"
$tess = "D:\Program Files\Tesseract-OCR\tesseract.exe"

# 纯文本
& $py $ocr "文件.pdf" --tesseract $tess

# 中英混合 → 可搜索 PDF
& $py $ocr "文件.pdf" -l chi_sim+eng --tesseract $tess --searchable 输出.pdf

# 保存 txt
& $py $ocr "文件.pdf" -l chi_sim+eng --tesseract $tess -o 结果.txt
```

---

## Python 环境

| 项目 | 值 |
|------|-----|
| 可执行文件 | `D:\Program Files\Python310\python.exe` |
| 版本 | 3.10.11 (embed, x64) |
| pip | `python -m pip install <包名>` |
| 源文件 | `D:\Applications\python-3.10.11-embed-amd64.zip` |

**关键库：** pymupdf, pytesseract, pdfplumber, pikepdf, pillow, pdf2image（仅装不用）

---

## Tesseract OCR

| 项目 | 值 |
|------|-----|
| 引擎 | `D:\Program Files\Tesseract-OCR\tesseract.exe` (5.4.0) |
| 语言包 | `tessdata\` — `eng`, `chi_sim`, `chi_tra`, `ara` |

---

## 系统脚本（My Projects 目录内）

| 脚本 | 用途 |
|------|------|
| `startmenu-cleanup-and-organize.ps1` | 开始菜单清理与整理 |
| `startmenu-boost-performance.ps1` | 开始菜单性能优化 |
| `startmenu-add-shortcuts.ps1` | 添加自定义快捷方式 |
| `block-office-auto-updates.ps1` | 阻止 Office 自动更新 |
| `install-rime-weasel.ps1` | 安装 Rime 输入法 |
| `install-wecom.ps1` | 安装企业微信 |
| `relocate-wecom-data.ps1` | 迁移企业微信数据目录 |
| `remove-bloatware.ps1` | 清理系统预装软件 |
| `create-restore-point.ps1` | 创建系统还原点 |
| `fix-cjk-console-font.ps1` | 修复终端 CJK 字体 |
| `DeepSeek-API-Claude-Code-搭建指南.md` | DeepSeek API + Claude Code 配置 |

---

## 其他已装软件

| 软件 | 类型 | 安装方式 |
|------|------|----------|
| PowerToys | D:\Program Files\PowerToys | winget |
| Rime 输入法 | D:\Program Files\Rime | 脚本 |
| Node.js | D:\Program Files\NodeJS | 手动 |
| Git | D:\Program Files\Git | 手动 |
| VS Code | D:\Program Files\Microsoft VS Code | 手动 |
| OneCommander | D:\Program Files\OneCommander | 手动 |
| Bandizip | D:\Program Files\Bandizip | 手动 |
| Foxmail | D:\Program Files\Foxmail 7.2 | 手动 |
| Google Chrome | D:\Program Files\Google Chrome | 手动 |
| 企业微信 | D:\Program Files\WeCom | 脚本 |
| Sumatra PDF | D:\Applications\ | 手动 |
| Claude Code | D:\Program Files\Claude Code | npm |

---

> 所有工具软件均安装在 `D:\Program Files\<AppName>` 下。
> 安装包/源文件保留在 `D:\Applications\` 备查。

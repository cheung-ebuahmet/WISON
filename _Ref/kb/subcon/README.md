# Subcontract Knowledge Base (分包合同知识库)

此目录包含从 `D:\Wison\Subcon_Payments\` 下所有分包合同的二进制文件（.docx / .doc / .pdf）
自动转换而来的 Markdown 文本，供全文搜索使用。

## 转换统计

| 分包 | 文件数 | 失败 |
|------|--------|------|
| 10.1 CCECC Civil Pkg II | 221 | 3 |
| 10.2 TCC Civil Pkg I/III | 230 | 4 |
| 12.1 CCECC MEI Pkg I | 269 | 2 |
| 12.2 TCC MEI Pkg II | 104 | 0 |
| 08 Med. Svc. Agr | 1 | 1 |
| **总计** | **825** | **10** |

> 10 个失败文件均为扫描件/图片型 PDF（MarkItDown 和 pymupdf 均无法提取文本），
> 详见 `_conversion_report.txt`。

## 转换方法

- **.docx / .pdf**: MarkItDown（保留表格和格式）→ 回退: python-docx / pymupdf
- **.doc（旧格式）**: Word COM → .docx → MarkItDown → 回退: olefile 原始文本提取
- 转换脚本：`D:\Wison\_tools\convert-subcon-to-md.py`

## 目录结构

镜像源目录结构，按分包合同编号组织：

| 目录 | 分包商 | 专业 | 合同编号 |
|------|--------|------|----------|
| `10.1 CCECC - Civil Pkg II/` | CCECC | 土建包 II | 10.1 |
| `10.2 TCC - Civil Pkg I_III/` | TCC | 土建包 I & III | 10.2 |
| `12.1 CCECC - MEI Pkg I/` | CCECC | 机电/安装包 I | 12.1 |
| `12.2 TCC - MEI Pkg II/` | TCC | 机电/安装包 II | 12.2 |
| `08 Med. Svc. Agr/` | RPM/Burjeel | 医疗服务 | 08 |

## 重点可搜索文件

以下此前为二进制、现在可全文搜索的关键文件：

### 工作范围 & 责任矩阵 (SOW & Responsibility Matrix)
| 文件 | 路径 |
|------|------|
| CCECC Civil Pkg II SOW | `10.1 .../Att 01_Scope of Work - Civil Pkg II.docx.md` |
| CCECC Civil Pkg II 责任矩阵 | `10.1 .../Att 02_Responsibility Matrix.docx.md` |
| TCC Civil Pkg I SOW | `10.2 .../Att 01_Scope of Work - Civil Pkg I.docx.md` |
| TCC Civil Pkg III SOW | `10.2 .../Att 02_Scope of Work - Civil Pkg III.docx.md` |
| TCC Civil 责任矩阵 | `10.2 .../Att 03_Responsibility Matrix.docx.md` |
| CCECC MEI Pkg I SOW | `12.1 .../A 1.1 Scope of Work-Rev.0.doc.md` |
| **CCECC MEI Pkg I 责任矩阵** | `12.1 .../A 1.2 SOW Responsibility Matrix-Rev.0.doc.md` |
| **TCC MEI Pkg II 责任矩阵** | `12.2 .../A 1.2 SOW Responsibility Matrix-Rev.0 2025-11-04.doc.md` |

### BOQ / 价格表
| 文件 | 路径 |
|------|------|
| CCECC Civil Pkg II BOQ | `10.1 .../Att 01_BOQ - Civil - BLDG Pkg II_Rev.B_Signed.pdf.md` |
| TCC Civil Pkg I BOQ Addendum | `10.2 .../Att 01.1_BOQ Addendum - Civil - BLDG Pkg I_Signed.pdf.md` |
| TCC MEI Pkg II BOQ | `12.2 .../Appendix D.1 BOQ For MEI-Package II Rev.C.pdf.md` |

### 计量方法 (Measurement Method)
| 文件 | 路径 |
|------|------|
| Civil 计量说明（通用） | `10.1 .../01_General - Subcontractor Pricing Instructions_Rev.A.docx.md` |
| Civil 场地准备/桩基 | `10.1 .../02.A-A1-A2-Site Preparation-Piling_Rev.A.pdf.md` |
| Civil 土方/砌体/钢结构 | `10.1 .../02.A-A3-A4-A5-Earth Work-Masonry Structure-Steel Structure_Rev.A.pdf.md` |
| Civil 建筑 | `10.1 .../02.A-A6-Architecture_Rev.A.pdf.md` |
| Civil 公用设施 | `10.1 .../02.A-A7-Utilities_Rev.A.pdf.md` |
| Civil 管道 | `10.1 .../03.B-Piping_Rev.A.pdf.md` |
| Civil 拆除 | `10.1 .../10.J-Demolition_Rev.A.pdf.md` |

## 转换日期

2026-07-16（一次性批量转换）

## 说明

- 所有文件均为原始合同的文本提取版，**不替代原文**。正式合同解释以签署版 PDF/.docx 为准。
- 付款发票（Pymt/）、往来函件（Corres/）、杂项（Miscellaneous/）未转换。
- 10.1 和 10.2 的 HSE 参考标准、ADNOC 规格书存在大量重复（同一套业主标准文件），搜索时注意结果可能成对出现。

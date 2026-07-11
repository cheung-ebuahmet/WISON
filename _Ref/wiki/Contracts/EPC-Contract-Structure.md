# EPC Contract Structure — ADNOC RSGP Upgrade

> **合同类型：** EPC 总承包 (FIDIC Silver Book 类)
> **模板：** ADNOC-CICV-505A(v6) — Form of Agreement + Annexures 1~14
> **业主参考号：** 6000066707
> **双语签章版：** → `Main_Contract\01_EPC Agrmt\EPC Agrmt_RSGP Upgrade - Bilingual_Signed.pdf`

---

## 合同文件优先权顺序 (FIDIC Sub-Clause 1.5)

| 优先级 | 文件 | WISON 对应 |
|--------|------|-----------|
| 1 (最高) | Contract Agreement | → `FOA - SCC - GCC_Signed.pdf` |
| 2 | Letter of Acceptance | *(待确认位置)* |
| 3 | Letter of Tender | *(待确认位置)* |
| 4 | Particular Conditions (SCC) | ANNEXURE 1 — 在 FOA 包内 |
| 5 | General Conditions (GCC) | ANNEXURE 2 — 在 FOA 包内 |
| 6 | Employer's Requirements / Specs | ANNEXURES 3~12 |
| 7 | Drawings | ANNEXURE 3 (SOW 含设计信息) |
| 8 | Schedules / BOQ | ANNEXURE 5 (Pricing) |

---

## ANNEXURE 全表 (1~14)

| ANX | 标题 | EXHIBIT 子结构 | 文件数 | OCR | 关键度 |
|-----|------|---------------|--------|-----|--------|
| **1** | Special Conditions of Contract (SCC) | — | 在 FOA 包内 | ❌ | ⭐⭐⭐ |
| **2** | General Conditions of Contract (GCC) | — | 在 FOA 包内 | ❌ | ⭐⭐⭐ |
| **3** | Scope of Work | A.01, A.02, A.04 + B.02 + ADR-001 | 3 | ❌ | ⭐⭐⭐ |
| **4** | Schedule | A.06 + Atts 1-6 | 1 | ❌ | ⭐⭐ |
| **5** | Pricing Schedule | A.07 (Pricing+Invoicing), A.09 (LD+Bonus) | 3+1docx | ⚠️ | ⭐⭐⭐ |
| **6** | Company Provided Facilities | A.05 | 2 | ✅ | ⭐ |
| **7** | Insurance Requirements | 7-1 (Company Insurances), 7-3 (Declaration) | 2 | ⚠️* | ⭐⭐ |
| **8** | Securities - Forms | 8-A (PCG), 8-B (Perf BG), 8-C (Adv BG) | 6 | ✅ | ⭐⭐ |
| **9** | Contractor Submissions | B.06 (Execution Plan) | 2 | ✅ | ⭐⭐ |
| **10** | Execution Requirements | A.08/A.10/A.11/A.17 + B.01~B.57 | 55 | 🔴 | ⭐⭐⭐ |
| **11** | Completion & Acceptance | 11D-1~7, 11E (Release) + B.38 + Asset Handover | 4 | ⚠️ | ⭐⭐ |
| **12** | HSE Requirements | 正文 + Att 1/2 + ADR-002/003 + Project HSE Plan | 9 | ⚠️ | ⭐⭐ |
| **13** | ICV Improvement Plan | — | 1 | ❌ | ⭐ |
| **14** | Export Control | Notice of Export Control Laws | 1 | ❌ | ⭐ |

> **图例：** ✅ 有 OCR ⚠️ 部分 OCR ❌ 无 OCR 🔴 大量文件无 OCR
> \* ANX 07 的 7-2 缺失

---

## ADNOC 双层附件体系

```
ANNEXURE  (ANX, 一级, 1~14)
  └── EXHIBIT  (Exh, 二级)
        ├── A.XX = 业主源文件 (Employer-originated, ~17 个)
        └── B.XX = 承包商提交 (Contractor-submitted, ~57 个)
```

### DAS 修约机制
ADNOC 通过 Tender Bulletin 修改工作范围时不重写合同，而是签发 **DAS (Document Addendum Sheet)**。
DAS 单在法律上覆盖原合同对应章节。
→ 相关文件：`TCF 001_DAS - Tender Phase Technical Clarifications_Signed.pdf`

---

## 额外文件

| 文件 | 说明 |
|------|------|
| `00_Contract Master Index_6000066707.xlsx` | 合同文件主索引（ADNOC 目录 + Wison 核对 + OCR 审计，五合一） |
| `ADNOC Gas Project Organization and Manning_Signed.pdf` | 项目组织与人员配置 |
| `Tripartite Agrmt_LLI Supply - PO 4500125194_ocred.pdf` | 三方协议 — 长周期设备供应 (LLI) |
| `ANX 1-13_Complete Set_ocred.pdf` | ANX 1~13 全本 OCR（安全网） |

---

## 相关 Wiki 页面
- [[Performance-Guarantee]] — ANX 05 A.09 + ANX 10 A.10/A.11
- [[Liquidated-Damages]] — ANX 05 A.09 LD 条款
- [[Insurance-Requirements]] — ANX 07
- [[HSE-Obligations]] — ANX 12

# Wison 资料信息库 — 命名规则与缩写参考

> 最后更新：2026-06-27
> 本文件为通用标准，适用于所有项目/分包/标段，不绑定任何单一合同

---

## ⚠️ 核心原则（在操作任何文件前必须遵守）

1. **本缩写对照表是唯一命名标准** — 适用于所有项目、所有分包、所有标段；目录结构参照 `12.1 CCECC - MEI I` 的骨架，但文件命名以本文为准。

2. **框架内的子文件命名不动** — `Att`、`Exh`、`App` 等子目录下的原文件名不予修改。命名建议或疑问均先告知，提供几个选项，经确认后再改。

3. **Amdt 按需创建** — 有补充协议的分包商才建 `Amdt_N` 目录，不创建空占位。

4. **新增文件/文件夹时** — 遵守本文的缩写和分隔符规则。如有不适用或两可的情况，列出选项供选择，不直接修改。

5. **新增文件的前缀跟随原目录已有风格** — 若该子目录下原文件自带 ATTACHMENT / ATT / Atch 前缀，新增文件用 `Att NN_`；若原文件无此前缀（如 `01.A-`、`02.B-` 裸编号风格），新增文件沿用原目录编号风格，不强行添加 `Att`。

---

## 一、标准缩写对照表（唯一命名标准）

### 1.1 文件类型 / 文档分类

| 完整名称 | 缩写 | 说明 |
|----------|------|------|
| Agreement / Subcontract | **Subcon** / **Agrmt** | 分包合同（主合同目录用 `01 Subcon`；Part I 命名用 `Agrmt`） |
| Letter of Award | **LOA** | 授标函 |
| Amendment | **Amdt** | 变更 / 补充协议 |
| Attachment | **Att** | 附件（子附件） |
| Exhibit | **Exh** | 合同附录（A~K） |
| Appendix | **App** | 附录（一般用字母索引：App A） |
| Technical Clarification Form | **TCF** | 技术澄清表 |
| Commercial Clarification Form | **CCF** | 商务澄清表 |
| Clarification Form (综合) | **CF** | 单一文件同时涵盖技术与商务 |
| Clarification | **CLAR** | 澄清/说明函（信函标题中） |
| Measurement | **MEAS** | 计量 / 澄清 |
| Request for Information | **RFI** | 信息请求 |
| Bill of Quantities | **BOQ** | 工程量清单 |
| Scope of Work | **SOW** | 工作范围 |
| Technical Specification | **SPEC** | 技术规范 |
| Drawing | **DWG** | 图纸 |
| Responsibility Matrix | **RM** | 责任矩阵 |
| Minutes of Meeting | **MOM** | 会议纪要 |
| Site Instruction | **SI** | 现场指令 |
| Non-Conformance Report | **NCR** | 不合格报告 |
| Company Profile | **CO** | 公司资料 |
| Project (tracker/register) | **PROJ** | 项目级追踪文件 |
| EPC Agreement | **EPC Agrmt** | EPC 总包合同（业主↔Wison 主合同，FIDIC Contract Agreement） |
| Subcontract | **Subcon** | 分包合同 |
| Volume | **Vol** | 合同分册 |

### 1.2 FIDIC 合同标准术语

> 依据 FIDIC 1999/2017 彩虹族（Rainbow Suite），国际通用，双方可查阅。

| 完整名称 | 缩写 / 术语 | FIDIC 定义 |
|----------|------------|-----------|
| **Contract** | — | 整套合同文件 = Contract Agreement + Conditions + Specs + Drawings + Tender… |
| **Contract Agreement** | **Agrmt** | 那一纸签字的正式合同书（短，列出所有组成文件，优先权最高） |
| **Employer** | — | 业主（FIDIC 标准用词 = 你合同里的 Owner / ADNOC） |
| **Contractor** | — | 承包商（FIDIC 标准用词 = Wison） |
| **Subcontractor** | **Subcon** | 分包商 |
| **Engineer** | — | 工程师（Red/Yellow Book 合同管理者；Silver Book 称 Employer's Representative） |

**FIDIC 彩虹族（Rainbow Suite）速查：**

| 书 | 全称 | 适用场景 |
|----|------|---------|
| **Red Book** | Conditions of Contract for Construction | 业主设计，按量计价 |
| **Yellow Book** | Conditions of Contract for Plant & Design-Build | 承包商设计+建造 |
| **Silver Book** | Conditions of Contract for EPC/Turnkey Projects | **EPC 总承包**（ADNOC RSGP 属此类） |
| **Gold Book** | Design-Build-Operate (DBO) | 设计-建造-运营 |
| **Green Book** | Short Form of Contract | 小型/简单项目 |

**合同文件优先权顺序（FIDIC Sub-Clause 1.5）：**

| 优先级 | 文件 |
|--------|------|
| 1（最高） | **Contract Agreement**（签字的合同书） |
| 2 | Letter of Acceptance |
| 3 | Letter of Tender / Tender |
| 4 | Particular Conditions（特殊条件） |
| 5 | General Conditions（一般条件） |
| 6 | Specifications / Employer's Requirements |
| 7 | Drawings |
| 8 | Bill of Quantities / Schedules |

> **注意：** Contract Agreement ≠ Contract。后者范围更大、包含前者。日常说的"合同"通常指 Contract（整体）。

### 1.3 合同组件

| 完整名称 | 缩写 | 说明 |
|----------|------|------|
| Conditions of Contract | **CoC** | 合同条件 |
| Particular Conditions | **PCC** | 特殊/专用条件（FIDIC Particular Conditions） |
| General Conditions | **GCC** | 一般条件 |
| Letter of Acceptance | **LOA** | 中标函 / 授标函 |
| Document Addendum Sheet | **DAS** | 文件补遗单（ADNOC 体系，见下） |

> **ADNOC DAS 机制：** ADNOC 通过 Tender Bulletin (TB) 修改工作范围时，不重写整个合同，而是签发 DAS（Document Addendum Sheet）。DAS 单在法律上覆盖原合同对应章节或图纸的指定部分，优先级高于被引用的原文。你的合同中 `1005312_DAS` 即为 TB A6R 对应的补遗文件集。

### 1.4 付款 / 财务

| 完整名称 | 缩写 | 说明 |
|----------|------|------|
| Payment | **Pymt** | 付款（文件夹名） |
| Payment Certificate | **PC** | 付款证书（通用） |
| Interim Payment Certificate | **IPC** | 中期付款证书 |
| Invoice | **Inv** | 发票 |
| Advance Payment | **Adv** | 预付款（文件夹用：Adv-01） |
| Advance Payment Guarantee | **APG** | 预付款保函 |
| Performance Bond | **PEB** | 履约保函 |

### 1.5 专业 / 包名称缩写

| 完整名称 | 缩写 | 说明 |
|----------|------|------|
| Civil Works | **Civil** | 土木工程 |
| Mechanical, Electrical, Instrumentation | **MEI** | 机电仪 |
| Package I / II / III | **Pkg I** / **Pkg II** / **Pkg III** | 包号 |
| Above Ground | **AG** | 地上 |
| Underground | **UG** | 地下 |
| Foundation | **FDN** | 基础 |
| Prefabrication | **PFI** | 预制 |
| Piping Support | **Pipe Supp** | 管道支架 |
| Structural Steel | **STL** | 钢结构 |
| Masonry | **MAS** | 砌筑 |
| Earth Work | **EW** | 土方 |
| Non-Destructive Examination | **NDE** | 无损检测 |
| Mobilization | **Mob** | 动员 |
| Site Demobilization | **SD** | 现场退场 |

### 1.6 组织 / 实体代码

| 完整名称 | 代码 | 说明 |
|----------|------|------|
| Wison Energy Engineering | **WSN** | 我方（Contractor / 承包商） |
| ADNOC | **ADNOC** | 业主（Employer，阿布扎比国家石油公司） |
| China Civil Engineering Construction Corp. | **CC3** / **CCECC** | MEI / Civil II 分包商 |
| China National Chemical Engineering Third Construction Co., Ltd. | **TCC** | Civil I_III / MEI II 分包商 |
| Burjeel | **BRJ** | 医疗服务 |
| （后续新增在此补充） | | |

### 1.7 EPC 工程专业代码（Disciplines — IEC/项目通用）

> 来源：国际 EPC 油区项目 Document Numbering Procedure。在 DC / 文件编号场景中使用。

| Code | 专业 | Code | 专业 |
|------|------|------|------|
| **PR** | Process（工艺） | **PI** | Piping（管道） |
| **ME** | Mechanical - Fixed Equipment | **RE** | Mechanical - Rotary Equipment |
| **EL** | Electrical（电气） | **IN** | Instrumentation（仪表） |
| **CI** | Civil（土建） | **ST** | Structure（结构） |
| **AR** | Architecture（建筑） | **HV** | HVAC（暖通） |
| **PL** | Pipeline（管线） | **TE** | Telecommunication |
| **SF** | Safety & Firefighting | **CR** | Corrosion（防腐） |
| **MW** | Material & Welding | **QC** | Quality Control |
| **CM** | Commissioning | **CN** | Construction |
| **DC** | Document Control | **PM** | Project Management |
| **PC** | Project Control | **CC** | Cost Control |
| **SU** | Survey | **PE** | Project Engineering |

### 1.8 EPC 文件类型代码（Doc Types — IEC/项目通用）

| Code | 类型 | Code | 类型 |
|------|------|------|------|
| **SP** | Specification（规范） | **DR** | Drawing（图纸） |
| **DS** | Data Sheet（数据表） | **PR** | Procedure（程序） |
| **RP** | Report（报告） | **SH** | Schedule（计划） |
| **PL** | Plan / Program（方案） | **ST** | Study（研究） |
| **CC** | Calculation（计算书） | **DB** | Design Basis（设计基础） |
| **MR** | Material Requisition | **PO** | Purchase Order |
| **TQ** | Technical Query | **SQ** | Site Query |
| **LI** | List（清单） | **IX** | Index（索引） |
| **PH** | Philosophy（原则） | **AN** | Analysis（分析） |
| **GA** | General Arrangement | **LY** | Layout（布置图） |
| **IS** | Isometric（轴测图） | **SD** | Single Line Diagram |
| **PF** | Process Flow Diagram | **PI** | P&ID |
| **BD** | Block Diagram | **LD** | Logic Diagram |
| **SM** | Schematic Diagram | **CE** | Cause & Effect |
| **CB** | Cost Estimate & Budget | **QP** | Quality Plan |
| **VD** | Vendor Data Review | **WO** | Work Order |

### 1.9 EPC 文件状态代码（Status — 通用）

| Code | 全称 | 说明 |
|------|------|------|
| **IFA** | Issued For Approval | 报送审批 |
| **IFR** | Issued For Review | 报送审核 |
| **IFD** | Issued For Design | 供设计用 |
| **IFC** | Issued For Construction | 供施工用（最终施工版） |
| **AFD** | Approved For Design | 设计已批 |
| **AFC** | Approved For Construction | 施工已批 |
| **TBD** | To Be Developed | 待编制 |

---

## 二、文件名结构：分隔符规则

### 2.1 三种分隔符，各有明确用途

| 符号 | 用途 | 位置 | 示例 |
|------|------|------|------|
| **`_`** | **结构分割** — 将索引代码与标题分开 | 仅一次，在索引代码之后 | `Att 01` `_` `Scope of Work.pdf` |
| **` - `** | **"且" / 并列** — 两个独立内容合并；替代 `&` | 标题内部；文件夹/文件通用 | `Pymt Terms - BOQ`、`Exh A_Work Scope - Schedule` |
| **空格** | **自然可读** — 标题中的正常单词间隔；Code 与 Index 之间也用空格 | 标题内部 / Code 后 | `Scope of Work`、`Adv 01` |

### 2.2 通用格式

```
{Code} {Index}_{Title}.{ext}
```

| 字段 | 说明 | 示例 |
|------|------|------|
| `{Code}` | 缩写（见 §一 对照表） | `Att`、`App`、`Exh`、`IPC`、`Inv` |
| `{Index}` | 序号（数字）或字母 | `01`、`A`、`001` |
| `_` | **结构分割符** — 仅此一处，位于 Index 之后 | |
| `{Title}` | 人类可读标题，含自然空格 | `Scope of Work`、`Pymt Terms - BOQ` |

### 2.2a 前导零规则（Sorting Rule）

> **数字序号必须补前导零**，确保文件管理器按数字顺序排列。

| 位数 | 格式 | 示例 | 说明 |
|------|------|------|------|
| 1~99 | **NN** | `01`、`02`...`10`、`99` | Att、Exh、App、Adv 通用 |
| 100+ | **NNN** | `001`、`002`...`100` | IPC、Inv 等付款流水 |

错误 vs 正确：

```
❌ Att 1_Scope of Work.pdf        ✅ Att 01_Scope of Work.pdf
❌ Att 2_BOQ.pdf                  ✅ Att 02_BOQ.pdf
❌ Att 10_HSE Plan.pdf            ✅ Att 10_HSE Plan.pdf   (已两位，无需补)
❌ App 1_Geotechnical Report.pdf  ✅ App 01_Geotechnical Report.pdf
```

> **字母索引不需前导零**：`App A_Geotechnical Report.pdf`、`Exh A_Work Scope - Schedule` 正确。

### 2.3 `_` 在标题内部的特殊用途

标题内部 `_` 用于连接**文件类型与状态**，不加空格：

```
Att 03_CCF_Signed.pdf
         ↑   ↑
       类型  状态
```

- `CCF_Signed` = 商务澄清表 + 已签署
- `TCF_DRAFT` = 技术澄清表 + 草稿
- `Inv_Ocred` = 发票 + 已 OCR

### 2.4 复数

文件夹名、标题中的复数直接加 `s`，不改变缩写：

| 单数 | 复数 |
|------|------|
| `Att` | `Atts` |
| `Exh` | `Exhs` |
| `App` | `Apps` |

---

## 三、命名示例（按新标准）

### 3.1 附件类

```
Att 01_Scope of Work.pdf
Att 02_Pymt Terms - BOQ.pdf
Att 03_CCF_Signed.pdf
Att 04_TCF_DRAFT.docx
```

### 3.2 附录类

```
App A_Geotechnical Report.pdf
App B_Site Photos.pdf
App 01_NDE Procedures.pdf
```

### 3.3 付款类

```
IPC 001_29,565.90 Dec 2025.pdf
PC 001_Jan 2026 Progress.pdf
```

**发票（Inv）专门格式：**
```
Inv {InvoiceNumber}_{Scope}_{Subcontractor}_ocred.{ext}
```

| 字段 | 说明 | 示例 |
|------|------|------|
| `InvoiceNumber` | 对方发票原始号码，**不修改不重编** | `CCECCABU2026060004` |
| `Scope` | 专业 + 包号 | `MEI Pkg I` |
| `Subcontractor` | 分包商简称 | `CCECC` |
| `_ocred` | OCR 标记 — 非强制，OCR 自动生成，有的有有的无 | |

示例：`Inv CCECCABU2026060004_MEI Pkg I_CCECC_ocred.pdf`

**预付款保函 / 履约保函：**
```
{Type}_{Scope} {NN}_{Subcontractor}.{ext}
```

| 字段 | 说明 | 示例 |
|------|------|------|
| `Type` | `APG`（预付款保函）/ `PEB`（履约保函） | `APG` |
| `Scope` | 专业 + Pkg | `MEI Pkg I` |
| `NN` | 对应 Adv 序号 | `01` |
| `Subcontractor` | 分包商简称 | `CCECC` |

示例：
```
APG_MEI Pkg I 01_CCECC.pdf
PEB_MEI Pkg I 01_CCECC.pdf
```

**预付款目录：**
```
Adv NN MNN\
      ↑  ↑
    序号 Moiety（分期号）
```

> `Adv 01 M01` = 第一笔预付款 · 第一期。后续有 M02、M03 依此类推。仅预付款使用 Moiety 编号。

### 3.4 合同类

```
WISON24108C26005_Subcon MEI Pkg I.pdf
WISON24108C25007_Subcon Civil Pkg I_III.pdf
Amdt 01_MEI Pkg I.pdf
LOA_Civil Pkg II.pdf
```

### 3.5 信函类（Corres）

信函采用项目前缀 + 段代码 + 流水号体系，不适用 `{Code} {Index}_` 格式。

**我方发出：**
```
SLT-5312-{WSN}-{对方代码}-{NNNN}_{Title}.{ext}
```

| 字段 | 说明 | 示例 |
|------|------|------|
| `SLT-5312` | 项目信件前缀（固定） | — |
| `WSN` | 我方代码 | WSN |
| `对方代码` | 收件分包商代码 | CCC / CVT |
| `NNNN` | 4 位流水号 | 0002 |
| `Title` | 主题关键词，`_` 分隔，简明扼要 | `CLAR of PFI AG Piping Supports MEI Pkg I` |

示例：`SLT-5312-WSN-CCC-0004_CLAR of PFI AG Piping Supports MEI Pkg I.docx`

**对方来函（扫描/OCR）：**
```
SLT-5312-{WSN}-{对方代码}-{NNNN}_{Title}_ocred.{ext}
```

| 字段 | 说明 | 示例 |
|------|------|------|
| `WSN` | 我方代码（收件方在此结构中仍放第二位置） | WSN |
| `对方代码` | 发函分包商代码 | CCC |
| `Title` | 对方原主题，保留原文 | `PFI AG Piping Supports MEI Pkg I` |
| `_ocred` | OCR 处理后标记 | `_ocred` |

示例：
```
SLT-5312-WSN-CCC-0002_PFI AG Piping Supports MEI Pkg I_ocred.pdf
SLT-5312-WSN-CCC-0003_SD in Mob of MEI Pkg I_ocred.pdf
SLT-5312-WSN-CCC-0004_CLAR of PFI AG Piping Supports MEI Pkg I_ocred.pdf
```

> - `_ocred` 始终在文件名最末（扩展名前），表示扫描件已 OCR。
> - 对方段代码按各自已使用的实际代码（CCC / CVT / 等），不强制统一。

---

## 四、文件夹架构

```
D:\Wison\
├── _Wison 文件与文件夹命名规则.md   ← 本文件
│
├── Co_Pro\                           # 公司简介 / 企业资料
│
├── Main_Contract\                    # 总包合同管理（业主↔Wison）
│   ├── Templates\                    # 信函/表格模板
│   ├── 01_EPC Agrmt\                 # 总包合同主文件
│   │   ├── 00_Contract Master Index_6000066707.xlsx            #   合同文件主索引（ADNOC目录+核对+OCR状态 五合一）
│   │   ├── EPC Agrmt_RSGP Upgrade - Bilingual_Signed.pdf       #   中英双语签章版
│   │   ├── FOA - SCC - GCC_Signed.pdf                          #   协议书 + SCC + GCC（签章）
│   │   ├── ANX 1-13_Complete Set_ocred.pdf                     #   ANX 1~13 全本 OCR
│   │   ├── ANX 5_Pricing Schedule_Exh A.07_A.09_Signed.pdf     #   ANX 5 → EXH A.07 + A.09（签章）
│   │   ├── ANX 5_Pricing Schedule_Exh A.09_Liquidated Damages - Bonus Provisions_ocred.pdf
│   │   ├── ANX 5_Exh A.07_Pricing Invoicing - Variation Rates.docx  #   EXH A.07 电子参考
│   │   ├── ANX 6_Company Provided Facilities_Exh A.05_Signed.pdf
│   │   ├── ANX 6_Company Provided Facilities_Exh A.05_ocred.pdf
│   │   ├── ANX 8_Securities - Forms_8-A_Parent Company Guarantee_ocred.pdf
│   │   ├── ANX 8_Securities - Forms_8-B_Performance Bank Guarantee_ocred.pdf
│   │   ├── ANX 8_Securities - Forms_8-C_Advance Payment Bank Guarantee_ocred.pdf
│   │   ├── ANX 11_Completion - Acceptance_11D-1 to 11D-7 - 11E_Form of Release_ocred.pdf
│   │   ├── ANX 11_Completion - Acceptance_Exh B.38_Acceptance_ocred.pdf
│   │   ├── ANX 12_HSE Requirements_ocred.pdf
│   │   ├── ANX 12_HSE Requirements_Att 1_HSE Studies_ocred.pdf
│   │   ├── ANX 12_HSE Requirements_Att 2_Cover Page_ocred.pdf
│   │   ├── ANX 12_HSE Requirements_Att 2_Company HSE Standards.zip
│   │   ├── ANX 12_HSE Requirements_ADR-002_Updated HSE Requirements_ocred.pdf
│   │   ├── ANX 12_HSE Requirements_ADR-003_Asset Integrity_ocred.pdf
│   │   └── {后续新增}…
│   ├── 02_Amdt NN\                   #   第 N 号变更/补充协议（按需）
│   ├── Corres\                       #   与业主往来信函
│   └── Pymt\                         #   收款跟踪（业主 → Wison）
│
├── Project_Info\                     # 项目资料（预审、模板、图纸等）
│
├── Subcon_Payments\                  # 分包付款管理
│   ├── Templates\                    # 信函模板、空表模板
│   │
│   ├── {序号} {分包商简称} - {专业} {包号}\
│   │   │
│   │   ├── Contract\                 # 合同文件
│   │   │   ├── 01_Subcon\             #   主合同（Part I + Part II，照搬原合同结构）
│   │   │   │   ├── Part I_Agrmt - LOA - GCS - SCS\   #  Part I 按合同实际命名
│   │   │   │   │   └── LOA\          #     授标函（如适用）
│   │   │   │   └── Part II_Exhibits\ #  Part II 按合同实际命名
│   │   │   │       ├── Exh A_Work Scope - Schedule\
│   │   │   │       └── ...
│   │   │   └── 02_Amdt NN\           #   第 N 号变更/补充协议（按需）
│   │   │
│   │   ├── Corres\                   # 双方往来信函
│   │   │
│   │   ├── Pymt\                     # 付款相关
│   │   │   ├── Adv NN MNN\             #   预付款（NN = 预付款序号；MNN = Moiety 分期号）
│   │   │   ├── IPC NNN\              #   中期付款证书
│   │   │   └── Other - {用途}\       #   其他
│   │   │
│   │   └── Miscellaneous\            # 杂项 — 按需创建
│   │
│   └── …其他分包商…
└── （可扩展）
```

### 4.0 根目录命名

**分包（Subcon_Payments）：**

| 字段 | 规则 | 示例 |
|------|------|------|
| 序号 | 排序用，可含小数点 | `12.1` |
| 分包商简称 | 见 §1.5 | `CCECC` |
| 专业 | 见 §1.4 | `MEI` |
| 包号 | `Pkg I` / `Pkg II` / `Pkg III` | `Pkg I` |

> `12.1 CCECC - MEI Pkg I`（不是 `MEI I`）。

**总包（Main_Contract）：**

> 业主仅一家（ADNOC），`Main_Contract\` 下方直接是合同目录（`01_EPC Agrmt` 等），无需中间层。

### 4.1 主合同目录

| 目录 | 规则 | 说明 |
|------|------|------|
| `01_Subcon` | 两位序号 `_` 名称 | 分包主合同（Part I + Part II） |
| `01_EPC Agrmt` | 两位序号 `_` 名称 | 总包主合同（Part I + Part II） |
| `02_Amdt NN` | 两位序号 `_` `Amdt` + 空格 + 两位流水号 | 变更/补充协议，`02_Amdt 01`、`02_Amdt 02`… |

> **编号前缀统一用 `_` 分割**：`01_Subcon`、`01_EPC Agrmt`、`02_Amdt 01`、`Part I_Agrmt`、`Part II_Exhibits`。文件夹的 `{NN}_{Name}` 模式与文件的 `{Code} {Index}_{Title}` 模式不同——文件夹仅一层分割，文件有两层。
> 
> **总包 vs 分包**：分别在各自的 `Main_Contract/` 和 `Subcon_Payments/` 功能区下，`01_Subcon` 和 `01_EPC Agrmt` 不会出现在同一目录中。

### 4.2 Part I / Part II 命名

```
Part I_Agrmt - LOA - GCS - SCS
Part II_Exhibits
```

> **Part I/II 之后用 `_` 分割**，内部组件以 ` - `（空格 + 连字符 + 空格）并列。组件名称因合同而异。

### 4.3 ADNOC 总包合同特有约定

> ADNOC EPC 合同使用双层附件体系，与分包合同的单层 Att/Exh 不同：

| 层级 | 原文用词 | 缩写 | 编号 | 示例 |
|------|---------|------|------|------|
| 一级 | ANNEXURE | **ANX**（书签等短场景）/ **Annexure**（文件名） | 1~14 | `Annexures 1-13_Complete Set_ocred.pdf` |
| 二级 | EXHIBIT | **Exh** | A.01~A.17（业主源） / B.01~B.57（承包商提交） | `Exh A.07_Pricing Invoicing - Variation Rates.docx` |

> **命名规则：**
> - `00_` 前缀文件置于目录最顶部（如合同总目录 Excel）
> - `_Signed` 尾缀：签章版（不可 OCR，保留法律基准）
> - `_ocred` 尾缀：扫描件经 OCR 处理（可全文检索、建数据库）
> - 签章件与 OCR 件是唯一分类维度 —— 每个合同文件最终标记为 `_Signed` 或 `_ocred`。电子参考件（`.docx` 等）无需标记
> - ADNOC 原版 `Vol` 分册号不保留（仅打包顺序，非合同结构）
> - 前导零跟随原文：ADNOC 原文件的 EXHIBIT 编号使用 `A.01`、`A.05`、`A.09`，文件名保留原文格式。若原文无前导零则不加（如分包侧 `Exh A` 字母索引）
> - ANX 子文件的命名格式：`ANX {N}_{Short Name}_Exh {M}[_{M2}…]{_Signed|_ocred}.pdf`

---

## 五、合同结构差异速查

不同合同原文目录/命名风格各异——照搬原合同，不强制统一。

### 分包合同

| 维度 | 10.1 CCECC Civil II | 10.2 TCC Civil I_III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|------|---------------------|----------------------|------------------|-----------------|
| Part I 名称 | `Part I FOA_LOA_CF_COC` | `Part I FOA_LOA_CF_COC` | `Part I_Agrmt - LOA - GCS - SCS` | （待合同到） |
| Part II 名称 | `Part II_Exhibits` | `Part II_Atchments` | `Part II_Exhibits` | （待合同到） |
| 附件风格 | `Attachment N - …` | `Atch. N - …` | `Exh A/B/C…` | （待合同到） |
| 合同编号 | `WISON24108C25007` | `WISON24108C25007` | `WISON24108C26005` | （待合同到） |
| Pymt 子目录 | 空 | `IPC 001~005`, `Adv`, `Other-lending` | `Adv-01` | 空 |
| 有 Amdt？ | 无 | 无 | 有 (`Amdt_01`) | 无 |

### 总包合同

| 维度 | ADNOC - RSGP |
|------|-------------|
| 合同类型 | EPC 总包合同（FIDIC Silver Book 类） |
| 合同模板 | ADNOC-CICV-505A(v6) — FORM OF AGREEMENT + ANNEXURES 1~14 |
| 业主参考号 | `6000066707` |
| 主合同目录 | `Main_Contract\01_EPC Agrmt\` |
| 合同架构 | FOA → ANNEXURE 1 (SCC) → ANNEXURE 2 (GCC) → ANNEXURES 3~14（SOW / Schedule / Pricing / Facilities / Insurance / Securities / Submissions / Execution Requirements / Completion & Acceptance / HSE / ICV / Export Control） |
| 子层结构 | 每个 ANNEXURE 下设 EXHIBIT A.XX（业主源文件）和 EXHIBIT B.XX（承包商提交），总计 A 系列 ~17 个、B 系列 ~57 个 |
| 现有文件 | 21 个 — 目录 x1、签章件 x4（Bilingual / FOA / ANX 5 / ANX 6）、OCR 件 x14、电子参考件 x1、压缩包 x1 |
| 命名格式 | `ANX {N}_{Short Name}_{子件}{_Signed|_ocred}.pdf`；子件可以是 `Exh M`、`Att N`、`ADR-XXX`、`N-A` 等 |
| 已覆盖 ANX | ANX 5 (A.07/A.09)、ANX 6 (A.05)、ANX 8 (8-A/8-B/8-C)、ANX 11 (11D-1~7, 11E / B.38)、ANX 12 (正文 + Att 1/2 + ADR-002/003)、ANX 1~13 全本 OCR |
| 命名原则 | 签章 `_Signed` ←→ OCR `_ocred` 是唯一区分；`&` → ` - `；前导零跟随原文；不同属 EXH 拆分、同属且连续保留粘连 |
| 有 Amdt？ | 暂无 |

---

## 六、修订记录

| 日期 | 变更 |
|------|------|
| 2026-06-30 | 总包全面同步 — 架构图更新至 21 文件（ANX 5/6/8/11/12 + 全本 OCR），速查表汇总命名格式与原则；`&` → ` - ` 全局替换；前导零规则改为跟随原文（ADNOC `A.01` 写法）；REF 示例文件同步改名 |
| 2026-06-30 | 总包合同清单同步 — §四架构图更新为实际文件库存，§五速查表补充合同架构（ANNEXURE 1~14 + EXHIBIT A/B 双层体系），新增 §4.3 ADNOC 双层附件命名约定、`_Signed`/`_ocred` 尾缀规则 |
| 2026-06-30 | 总包合同目录扁平化 — 删除中间层 `ADNOC - RSGP`，`01_EPC Agrmt` 直放 `Main_Contract\` 下（业主仅一家无需分组） |
| 2026-06-30 | 总包合同纳入：`01_Head Agrmt` → `01_EPC Agrmt`（纠正为 FIDIC Contract Agreement 标准术语）。新增 §1.2 FIDIC 标准术语、§1.7~§1.9 EPC 工程代码 |
| 2026-07-01 | 新增 DAS（Document Addendum Sheet）术语解释 — ADNOC Tender Bulletin 修约机制（§1.3），附 `1005312_DAS` 文件背景说明 |
| 2026-06-27 | **大修** — 确立固定缩写对照表（§一），引入分隔符规则（§二），新增 TCF/CCF/CF/CoC/SCC/GCC/App/PC，Exhibit→Exh、Attachment→Att、Invoice→Inv，前导零规则，信函命名（§3.5） |
| 2026-06-27 | 新增：发票 Inv 格式、APG/PEB 命名（`Type_Scope NN_Subcon`）、Adv Moiety 目录规则（`Adv NN MNN`）、`_ocred` 非强制；修订记录精简 |

---

## 七、扩展方式

新增缩写直接追加到 §一 对应小节：

```markdown
| … | **XXX** | 说明 |
```

---

## 八、知识库（kb/）镜像结构

`_Ref\kb\` 是 `Main_Contract\` 的目录镜像，存放 OCR 转换后的 `.md` / `.csv` 文本文件。

### 三明治架构

```
D:\Wison\
├── Main_Contract\          ← 数据层（raw）—— 纯 PDF/DOCX/XLSX，不含 .md
├── _Ref\                   ← 知识层（wiki + kb）
│   ├── _Wison 命名规则.md   → WIKI.md（Schema）
│   ├── index.md             → 库存目录
│   ├── wiki\                → 人工撰写的合同知识
│   └── kb\                  → 自动生成的 OCR 产物
│       ├── README.md
│       ├── ANX 03_SOW\      ← 与 Main_Contract/ 目录一一镜像
│       ├── ANX 10_Execution Requirements\
│       └── ...
└── Subcon_Payments\         ← 数据层（raw）
```

### kb/ 命名规则

| 来源 | 产物 | 规则 |
|------|------|------|
| `{file}_ocred.pdf` | `{file}.md` | 去 `_ocred` / `_Signed` 尾缀及扩展名 |
| `{file}.xlsx` | `{file}_{SheetName}.csv` | 一 Sheet 一个 CSV |

### 原则

- **生成品可丢弃** — kb/ 内全部文件可由 OCR 重新生成，不可恢复的人工知识放 wiki/
- **结构锁定** — kb/ 目录与 Main_Contract/ 永久镜像，新增文件夹时两处同步
- **不存二进制** — kb/ 不含 PDF/DOCX/XLSX/ZIP

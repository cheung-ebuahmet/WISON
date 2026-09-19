# Wison RSGP 项目知识库建设 — 阶段性总结

**日期**：2026 年 7 月 15 日  
**范围**：`D:\Wison\` 全目录  
**状态**：终稿 Amdt 01 已锁定，知识库框架初具规模，进入持续优化阶段

---

## 一、背景

### 1.1 项目概况

**总项目**：Hail & Ghasha — Ruwais Sulphur Granulation Plant (RSGP) at RSHT - 2  
**业主**：ADNOC GAS OPERATIONS AND MARKETING – L.L.C.  
**总包商**：WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI  
**总包合同金额**：~USD 800M+  
**分包体系**：4 个主要分包合同包，覆盖 Civil（土建）和 MEI（机电仪）全部安装工程

### 1.2 资料库建立的必要性

在 2026 年 5-7 月的分包合同谈判、信函起草、付款审核与变更协议（Amdt 01）起草过程中，暴露了以下痛点：

1. **合同文件分散** — 总包 ANX 01-13 共 300+ 个 PDF 散落在多层嵌套目录中，查找一个条款需遍历数次
2. **跨合同比较低效** — 4 个分包合同的 LD、KP、保函、保险条款相似但不完全相同，手工对照极易遗漏差异
3. **OCR 产物不可检索** — 扫描件合同和附件无法全文搜索，关键数字（如误期违约金上限比例、保留金比例）藏在不可搜索的 PDF 中
4. **信函起草重复劳动** — 每份中英双语催告/通知函的架构、术语、法律保留条款都需要从零组织
5. **Amdt 01 起草迭代量极大** — 三方协议转换经历约 15 轮修改（两方→三方、来料加工→进料加工、代付→Descope、简称去括号、编号补齐、引号规范化、签署页重排），没有系统化规则记录下次将重复同样过程

---

## 二、目的

建立以 Claude Code 为引擎的 **合同管理与知识库体系**，实现：

| 目标 | 说明 |
|------|------|
| **知识可检索** | 所有 PDF 合同经 OCR 转为结构化 Markdown/YAML，全文可搜索 |
| **条款可对比** | 跨分包合同的同类条款（LD、KP、保函、保险）映射到结构化数据，一键对比差异 |
| **起草可复用** | 信函模板、变更协议起草规则、中英双语排版规范沉淀为记忆文件 |
| **付款可追溯** | 每笔 IPC 与合同价格数据库挂钩，自动校验 |
| **决策有依据** | 商业分析（风险矩阵、背靠背映射、索赔时间条）从真实合同数据驱动 |

---

## 三、已完成的前期工作

### 3.1 资料库物理架构

```text
D:\Wison\                          ← Git 仓库（自管版本）
│
├── Main_Contract/    (323 files)  ← 🗄️ 总包合同原始 PDF/DOCX（只读）
│   ├── ANX 01-13_Complete Set/    ← 总包合同全套附件（OCR 后 >300 页）
│   ├── ANX 03_SOW/                ← 工作范围
│   ├── ANX 05_Pricing/            ← 定价与 LD
│   ├── ANX 08_Securities/         ← 保函格式
│   ├── ANX 11_Completion/         ← 验收与移交
│   ├── ANX 12_HSE/                ← HSE 要求
│   └── FOA_Draft.md etc.          ← FOA 草案（OCR 产物）
│
├── Subcon_Payments/  (1092 files) ← 🗄️ 分包合同 + 信函 + 付款（只读）
│   ├── 10.1 CCECC - Civil Pkg II/ (241f) ← 中土土建 II 包
│   ├── 10.2 TCC - Civil Pkg I_III/(284f) ← 中技土建 I+III 包
│   ├── 12.1 CCECC - MEI Pkg I/   (300f) ← ★ 中土机电 I 包（Amdt 01 所在地）
│   │   ├── Contract/
│   │   │   ├── 01_Subcon/          ← 原分包合同正文 + 附件
│   │   │   └── 02_Amdt 01/         ← ★ Amdt 01 终稿 + 备份
│   │   ├── Corres/                 ← 往来信函（5 封）
│   │   └── Pymt/                   ← 付款记录（IPC）
│   ├── 12.2 TCC - MEI Pkg II/   (133f) ← 中技机电 II 包
│   ├── 08 Med. Svc. Agr/          ← 医疗服务协议
│   ├── 98 METS Lab/               ← 实验室测试分包
│   └── 99 LONGTAIDI fob/    (86f) ← ★ 隆泰迪加工商分包（独立合同，与 Amdt 01 配套）
│       ├── Part 0 Instructions to Tenderers/
│       ├── Part I Subcontract Agreement/
│       └── Part II Exhibits/
│
├── _Ref/              (1240+ files) ← 🧠 Claude Code 唯一工作区（所有产出归此）
│   ├── kb/             (374f)     ← OCR 产物（总包合同附件的 Markdown 副本）
│   │   └── subcon/     (825f)     ← ★ 2026-07-16 新增：全部分包合同二进制→MD 批量转换
│   ├── data/           (21f)      ← YAML 结构化数据
│   │   ├── contracts/             ← 4 份合同 YAML（商务条款事实来源）
│   │   ├── clause-library/        ← 条款知识对象（LD、KP、Payment、Warranty）
│   │   ├── companies/             ← 分包商实体信息
│   │   ├── correspondence/        ← 信函 YAML 索引
│   │   ├── commercial-analysis/   ← 风险矩阵 / 背靠背映射
│   │   └── timeline.md
│   ├── wiki/           (7f)       ← 人工可读的知识展示层
│   ├── schema/         (3f)       ← 数据模型定义（contract/correspondence/entity）
│   ├── reports/                   ← 自动生成报告（含本文件）
│   ├── tasks/                     ← OCR/知识库建设任务追踪
│   └── cache/                     ← 中间文件
│
├── _tools/            (55 files)  ← 🔧 Python 脚本、价格数据库、指南
│   ├── price-database/ (36f)     ← ★ 3 个分包合同价格 CSV（Green/Brown/Indirects/PS）
│   ├── AmdtReview/     (2f)      ← Amdt 01 的修改脚本快照
│   ├── guides/         (2f)      ← PDF→MD 指南、工具箱索引
│   ├── NDA - Wison Contractor (bilingual).py  ← 保密协议生成器
│   ├── generate_letter_template.py            ← 信函模板生成器
│   ├── rename_*.py                            ← 附件批量重命名
│   └── gen_subcontractor_matrix.py            ← 分包商矩阵编译器
│
├── AI_Knowledge/      (64 files)  ← 🤖 AI 原生知识层（本体论、决策引擎、模式库）
│   ├── 00_Glossary/               ← 术语表
│   ├── 01_Entities/               ← 实体定义（Contract/Party/Exposure）
│   ├── 03_Rules/                  ← 规则库（CVR Time Bar / LD Flow-Down / Warranty Gap / Payment Precondition）
│   ├── 04_Mapping/                ← 条款跨合同映射
│   ├── COMMERCIAL_DNA.md          ← ★ 商业基因：Wison 合同博弈模式
│   ├── DECISION_CORPUS.md         ← ★ 决策语料库（43KB，最大单文件）
│   ├── PATTERN_LIBRARY.md         ← ★ 模式库（25KB 条款模板与反模式）
│   └── ONTOLOGY.md                ← 知识本体定义
│
├── Project_Info/      (40 files)  ← 项目模板 / Logo / 工程资料
└── index.md                       ← 根级导航入口
```

**总计**：4 个一级分区、311 个子目录、2032 个文件、4.4 GB

### 3.2 OCR 与文本化

| 完成项 | 详情 |
|--------|------|
| **总包合同 ANX 01-13** | 全部 13 个附件经 OCR 转为 Markdown，存放在 `_Ref/kb/` 镜像目录 |
| **FOA / SCC / GCC** | 草案 PDF → MD，中英双语对照版本已生成 |
| **分包合同附件** | 3 个分包合同的 Exhibit C（技术规范）、Exhibit D（价格）、Exhibit E（质量）均已通过 OCR 或 Python 提取为结构化数据 |
| **信函** | 5 封 SLT-5312 系列中英双语信函已完成 OCR + YAML 元数据提取 |

### 3.3 价格数据库建设

| 分包合同 | 价格 CSV | 覆盖范围 |
|----------|----------|----------|
| CCECC Civil Pkg II | 12 个 CSV | Summary / Indirects / Civil (Brown/Green) / CMS / UG PIP / Plot Plan / Equipment / Labor / Provisional Sum |
| TCC Civil Pkg I | 12 个 CSV | 同上结构 |
| TCC Civil Pkg III | 8 个 CSV | Summary / Indirects / Civil (Green) / BLDG / UG PIP / Plot Plan / Equipment / Labor |
| **MEI 包** | **尚缺** | CCECC MEI Pkg I 和 TCC MEI Pkg II 的价格 CSV 未提取 |

辅助设施：
- `_column-mapping.md` — 列名中英文对照表
- `_manifest.json` — 所有 CSV 的元数据清单
- `_query.py` — 跨分包合同价格查询脚本

### 3.4 结构化数据（YAML 事实层）

| 文件 | 内容 |
|------|------|
| `contracts/EPC-ADNOC-RSGP.yaml` | 总包合同核心商务条款 |
| `contracts/10.1-CCECC-Civil-II.yaml` | 中土土建 II 包核心条款 |
| `contracts/10.2-TCC-Civil-I-III.yaml` | 中技土建 I+III 包核心条款 |
| `contracts/12.1-CCECC-MEI-I.yaml` | ★ 中土机电 I 包（含 Amdt 01 后的条款变更） |
| `clause-library/Delay-LD.md` | 误期违约金跨合同对比 |
| `clause-library/Key-Personnel.md` | 关键人员条款 |
| `clause-library/Payment.md` | 支付条款 |
| `companies/CCECC.yaml` | 中土实体信息 |
| `companies/TCC.yaml` | 中技实体信息 |
| `correspondence/*.yaml` | 4 封信函的结构化索引 |
| `commercial-analysis/back-to-back-matrix.md` | 总包→分包背靠背映射 |
| `commercial-analysis/risk-register.md` | 风险登记册 |

### 3.5 AI 知识层

`AI_Knowledge/` 是一个独立的知识工程层，包含：

- **COMMERCIAL_DNA.md** — Wison 在国际分包合同中的核心博弈模式（付款条件、风险下沉、背靠背）
- **DECISION_CORPUS.md**（43KB）— 合同条款决策的完整语料库，覆盖 LD、KP、保函、保险、支付、变更等全部领域的决策逻辑
- **PATTERN_LIBRARY.md**（25KB）— 条款模板库与常见反模式
- **CONTRACT_MAP.md** — 4 个分包合同 + 总包合同的条款映射矩阵
- **DECISION_ENGINE_SPEC.md**（20KB）— 自动决策引擎的技术规格
- **VALIDATION_ENGINE.md** — 合同审查自动验证规则

### 3.6 Amdt 01（变更协议）起草 —— 本次最大单项工作

从 2026 年 7 月 15 日起，经过约 **15 轮迭代**，完成了以下完整过程：

| 里程碑 | 内容 |
|--------|------|
| **框架转换** | 两方→三方协议（新增加工商 Longtaidi 为丙方） |
| **商业模式转型** | 来料加工（Free-issued/Tolling）→ 进料加工（Self-Procured Materials & Export） |
| **支付逻辑重构** | 代付代垫 → Descope 绝对按实对冲扣减（§3.2 + §4） |
| **标题术语归一** | Third-Party Delegation → By the Fabricator；代为付款安排 → 范围核减与财务对冲 |
| **旧条款删除** | §5 Contractor-Supplied Materials 整条删除（与新框架矛盾） |
| **新条款新增** | §5 原材料供应独立安排（占位隔离）；§7.3 加工商承诺与确认（含 §7.3.3 免责防火墙） |
| **编号补全** | §5 补齐（防断层）；§8.1 (i)(ii)(iii) → (a)(b)(c) 统一小写字母 |
| **简称整理** | 正文中去掉全部 `(CCECC)`/`（中土）`/`(Wison)`/`（惠生）` 括号；只保留定义页的全称 |
| **引号规范化** | 中文全角 `""` / 英文半角 `""`；零 ASCII 引号在中文段落 |
| **标点混修** | `Subcontractor 's` → `Subcontractor's`；`强制性督查职责` → `强制监督职责`；`与承包商联合` → `与承包商代表联合` |
| **签署页重排** | 加工商签字块从见证条款上方移至下方，三方并列 |
| **§10.1 修正** | "一式三份" → "一式三份，各方各执一份" |
| **历史归因** | 第一 WHEREAS 限缩为 "承包商与分包商（作为原分包合同的签约双方）" |
| **计价歧义消除** | §2.1 重写：复合单价 = 计量基准，净额 = 基准 − 实际支付 |

**产出物**：
- `Amdt 01_MEI Pkg I (Revised) .docx`（113 段 → 调整至 103 段终稿）
- `Amdt 01_MEI Pkg I (Revised) - BACKUP 20260714.docx`（原始备份）
- 记忆文件 `[[amdt-drafting-conventions]]`（全套起草规则，可复用）

### 3.7 工具脚本积累

| 脚本 | 功能 |
|------|------|
| `generate_letter_template.py` | 中英双语信函自动生成（模板 + 合同引用 + 条款编号自动填入） |
| `NDA - Wison Contractor (bilingual).py` | 中英双语保密协议一键生成 |
| `gen_subcontractor_matrix.py` | 分包商商务条款矩阵自动编译为 Markdown |
| `rename_10.2_TCC.py` / `rename_attachments_10.1.py` | 附件批量规范化重命名的历史脚本 |
| `consolidate_master_index.py` | MASTER-INDEX.md 自动更新 |
| `price-database/_query.py` | 跨分包合同价格查询 |
| `AmdtReview/amend_docx.py` | Amdt 修改逻辑的快照（已归档） |

### 3.8 记忆文件（跨会话持久规则）

已写入 `[[amdt-drafting-conventions]]` 等 **12 个** 项目记忆文件，覆盖：

- 合同审查自动化规则（`[[contract-review-rules]]`）
- 信函写作规范（`[[wison-letter-writing-style]]`）
- Amdt 起草全套规则（`[[amdt-drafting-conventions]]`）
- 命名协议（`[[wison-naming-protocol]]`、`[[sgp-rsht-naming-convention]]`）
- FIDIC 术语（`[[fidic-terminology]]`）
- 价格数据库（`[[subcon-price-database]]`）
- 备份/删除策略（`[[backup-system]]`、`[[deletion-recycle-policy]]`）

---

## 四、待优化与未完成事项

### 4.1 数据缺口

| 缺口 | 优先级 | 说明 |
|------|--------|------|
| **MEI 包价格 CSV** | 高 | CCECC MEI Pkg I 和 TCC MEI Pkg II 的 Exhibit D 未提取为结构化价格数据 |
| **MEI 包合同 YAML** | 高 | 12.2 TCC MEI Pkg II 的合同 YAML 未创建 |
| **99 LONGTAIDI 合同** | 高 | 隆泰迪独立加工合同数据库未建立，当前仅原始 PDF/DOCX |
| **信函 YAML 不全** | 中 | 仅 4 封信函完成结构化提取，CCECC Civil 和 TCC MEI Pkg II 的信函未覆盖 |
| **Project_Info 待重组** | 中 | 当前 `Project_Info/` 下有未分类的模板/图纸/Logo（如 `Wison Template/`、`Adnoc Template/`、`Engineering Knowledge/` 等目录混杂） |

### 4.2 知识层完善

| 缺口 | 说明 |
|------|------|
| **AI_Knowledge 子目录多数为空** | `02_Relationships/`、`04_Processes/`、`05_Playbooks/`、`06_Case_Studies/`、`07_QA/`、`08_Prompts/` 均只有骨架 README |
| **clause-library 不完整** | 当前只有 Delay-LD、Key-Personnel、Payment 三条。缺 Warranty、Insurance、Indemnity、Force Majeure、Termination、Governing Law |
| **commercial-analysis 稀疏** | back-to-back-matrix 和 risk-register 是初始版本，待更新 |
| **DECISION_CORPUS 待验证** | 43KB 的决策语料是否与当前 Amdt 01 终稿完全一致，需做一遍全量对照 |

### 4.3 工具层

| 缺口 | 说明 |
|------|------|
| **无变更协议自动生成器** | Amdt 01 的起草规则已充分沉淀，但尚未做成可复用的模板生成脚本（类似 `generate_letter_template.py`） |
| **无合同条款差异自动扫描** | 跨 4 个分包合同的条款差异目前靠手动对比，可做 CLI 工具 |
| **无 IPC 付款校验器** | 付款记录在 `Pymt/` 下有 IPC PDF，但未与价格 CSV 联动校验 |
| **_tools/ 混杂** | `AmdtReview/` 是临时快照，可清理；`check_10.2_dupes.py`、`rename_*.py` 等一次性脚本可归档 |

### 4.4 流程规范

| 缺口 | 说明 |
|------|------|
| **OCR 流程不统一** | 部分文件用 pymupdf+Tesseract（`pdf-ocr-pipeline`），部分用 MarkItDown MCP（`hybrid-doc-pipeline`），两者策略和命名规则未统一 |
| **合同修改无版本号** | Amdt 01 经 15 轮迭代但只有一个备份文件，中间版本全部覆盖。若需追溯某次修改前的状态，无法还原 |
| **记忆文件可能过时** | 部分记忆（如 `wison-agreement-simplification`）标为 "DO NOT EXECUTE YET"，但已在草稿中引用数月，需清理或执行 |

---

## 五、下一步建议

| 序号 | 行动 | 预估工作量 |
|------|------|-----------|
| 1 | **提取 MEI 包价格 CSV**（CCECC Pkg I + TCC Pkg II 的 Exhibit D） | 2-3 小时 |
| 2 | **补齐 clause-library**（Warranty / Insurance / Indemnity / FM / Termination） | 4-6 小时 |
| 3 | **建立 99 LONGTAIDI 合同结构化数据**（YAML + 价格 + 关键条款映射） | 3-4 小时 |
| 4 | **创建 Amdt 模板生成脚本**（复用 [[amdt-drafting-conventions]] 规则） | 2-3 小时 |
| 5 | **清理 AI_Knowledge 空目录**（填充或合并） | 1-2 小时 |
| 6 | **统一 OCR 管线**（选 pymupdf+Tesseract 为主线，淘汰 MarkItDown MCP 法的合同流转） | 2-3 小时 |
| 7 | **添加版本号机制**（每次 `doc.save()` 前自动按日期时间戳备份） | 0.5 小时 |
| 8 | **Project_Info 重组**（Templates / Client / Engineering / Assets 四子目录） | 1 小时 |

---

*本报告由 Claude Code 自动生成，数据截至 2026-07-15。*
*下次更新触发条件：完成任一下一步建议项或新增重大合同文件。*

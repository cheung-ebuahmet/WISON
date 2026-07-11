# Wison RSGP 项目 — 总入口

> **Claude Code 导航起点** → `_Ref/data/MASTER-INDEX.md`
> **原则: 原始资料只读，Claude 所有产出归入 `_Ref/`**

---

## 目录架构（三层分离）

```
D:\Wison\
│
├── Main_Contract/              ← 🗄️ 证据层：总包合同原始资料（只读，不加 Markdown）
├── Subcon_Payments/            ← 🗄️ 证据层：分包合同 + 信函 + 付款（只读）
├── Project_Info/               ← 🗄️ 证据层：模板 / 图纸 / 工程资料 / Logo
│   ├── [Wison Template/]       ←   → 待重组 → Templates/
│   ├── [Adnoc Template/]       ←   → 待重组 → Client/
│   ├── [Engineering Knowledge/]←   → 待重组 → Engineering/
│   ├── [*.webp / *.png]        ←   → 待重组 → Assets/
│   └── [Main Layout/]          ←   → 待重组 → Layout/
│
├── _Ref/                       ← 🧠 知识层：Claude Code 唯一工作区
│   ├── schema/                 ← 数据模型定义
│   ├── data/                   ← 结构化数据
│   │   ├── MASTER-INDEX.md     ← 知识库导航总图
│   │   ├── contracts/          ← 合同 YAML（事实唯一来源）
│   │   └── clause-library/     ← 条款知识对象（规则层）
│   ├── wiki/                   ← 展示层（由 YAML 编译生成）
│   ├── kb/                     ← OCR 产物镜像（Main_Contract 的结构副本）
│   ├── reports/                ← 自动生成报告
│   ├── tasks/                  ← 任务追踪
│   └── cache/                  ← 中间文件（可安全删除）
│
├── _Tools/                     ← 🔧 工具层：脚本与自动化
│
└── index.md                    ← 📍 你在这里
```

---

## 核心原则

| 原则 | 说明 |
|------|------|
| **证据层只读** | `Main_Contract/`、`Subcon_Payments/`、`Project_Info/` 不新增 Markdown，不修改原始文件 |
| **Claude 仅写入 `_Ref/`** | 所有产出、中间文件、缓存均归入 `_Ref/` 对应子目录 |
| **YAML 是唯一事实来源** | 合同金额、LD、保函比例等数值只存在 `_Ref/data/contracts/*.yaml`，Wiki 由之编译 |
| **四层知识链路** | PDF（证据）→ OCR（`kb/`）→ Clause（`clause-library/`）→ Wiki（`wiki/`） |
| **Claude 每次从此开始** | 首条指令：读取 `_Ref/data/MASTER-INDEX.md` 获取当前知识库状态 |

---

## 快速跳转

| 要找什么 | 去哪里 |
|----------|--------|
| 项目全局知识导航 | `_Ref/data/MASTER-INDEX.md` |
| 查某分包合同商务条款 | `_Ref/data/contracts/10.1-CCECC-Civil-II.yaml` |
| 查某条款的规则与差异 | `_Ref/data/clause-library/` |
| 查分包合同原文 | `Subcon_Payments/10.1 CCECC - Civil II/Contract/` |
| 查总包合同原文 | `Main_Contract/` |
| 发信函模板 | `Project_Info/Wison Template/Your-Letter-Number Letter-Title.docx` |
| 文件命名规则 | `_Ref/_Wison 文件与文件夹命名规则.md` |
| 运行分析脚本 | `_Tools/` |

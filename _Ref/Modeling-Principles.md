# Modeling Principles — Commercial Contract Knowledge Base

> **用途：** 所有架构决策的依据。新增合同、新增对象、修改 Schema 之前必读。
> **版本：** 1.0 | 2026-07-09

---

## 核心原则

### 原则 0：商业相关性过滤器

> **"这份资料是否影响付款、变更、索赔、工期、违约责任、风险分配或合同履约？"**

| 答案 | 处理 |
|------|------|
| 会 | OCR + Schema 字段 + Clause KO + 双向关联 |
| 不会 | 保留原始文件，不结构化，不建 Knowledge Object |

**这是整个知识库的第一道门。** 所有后续决策都源于此。

---

## 一、四层架构

```
Evidence（证据层）    →  PDF / DOCX（只读，不可修改）
    ↓
Structured Data      →  YAML（事实唯一来源）
    ↓
Knowledge Objects    →  Clause Library（规则 + 差异 + 风险）
    ↓
Views                →  Wiki（展示层，由 YAML 编译生成，不保存独立事实）
```

### 各层职责

| 层 | 可以做什么 | 不可做什么 |
|------|-----------|-----------|
| Evidence | 存放原始文件 | 新增 Markdown；修改文件名或内容 |
| YAML | 保存所有数值、日期、布尔值 | 保存长文本分析（放 KO 层） |
| Clause KO | 保存条款释义、差异对比、风险注释 | 保存独立于条款来源的金额 |
| Wiki | 编译展示、导航 | 包含 YAML 中不存在的事实 |

---

## 二、什么值得成为 Knowledge Object

### 纳入标准

只有同时满足以下三个条件，才建 Clause Library KO：

1. **商业相关性** — 直接影响付款/变更/索赔/工期/违约责任
2. **跨合同可对比** — 存在至少两份合同有不同处理方式
3. **操作指引价值** — 能产出具体的合同管理行动建议

### 商业条款 KO 清单（已锁定）

| 优先级 | 条款 | 状态 |
|:---:|------|:---:|
| ⭐⭐⭐⭐⭐ | Payment | 待建 |
| ⭐⭐⭐⭐⭐ | Variation | 待建 |
| ⭐⭐⭐⭐⭐ | Delay / LD | KP-LD ✅, Delay 待建 |
| ⭐⭐⭐⭐⭐ | EOT | 待建 |
| ⭐⭐⭐⭐⭐ | Claims / Notice | 待建 |
| ⭐⭐⭐⭐ | Termination | 待建 |
| ⭐⭐⭐⭐ | Performance Security | 待建 |
| ⭐⭐⭐⭐ | Retention | 待建 |
| ⭐⭐⭐⭐ | Advance Payment | 待建 |
| ⭐⭐⭐ | Warranty | 待建 |
| ⭐⭐⭐ | Insurance (仅商业部分) | 待建 |

### 不做 KO 的内容（永久）

- 技术规范（Drawing / Specification / ITP / NDE）
- HSE 技术标准（ADNOC HSE 体系 200+ 文件）
- 质量体系文件（QC Plan / Inspection Checklist）
- 施工方法（Method Statement / Constructability）
- 培训材料

> 这些内容保留 OCR 文本以备索赔检索，但不建 Clause Library、不建 Wiki、不加双向链接。

---

## 三、什么值得成为独立 Entity

### 当前实体类型（已锁定）

| 类型 | 何时新建 |
|------|---------|
| **Company** | 合同签约方（CCECC / TCC / ADNOC / WSN / METS） |
| **Person** | 关键人员（KP 名单中 7 人）或合同/商务决策人 |
| **Package** | 合同中的独立标段（Pkg I / II / III） |

### 不建实体

- Equipment / Material / Valve / Pipe — 工程对象，非商业对象
- Location / Discipline — 目前作为 YAML 字段足够，不需独立

### Issue 的定位（重要）

**Commercial Issue 目前内嵌于 Contract YAML 的 `issues: []` 中。**

只有当以下条件同时满足时，才升级为独立 Entity：

1. 一个 Issue 同时关联 ≥2 份合同
2. 一个 Issue 关联 ≥3 封函件
3. 一个 Issue 已升级为 Claim 或即将产生独立成本/工期影响

在此之前，Issue 是 Contract 的**生命周期属性**，不是独立图节点。

---

## 四、Schema 修改原则（LOCKED）

### `contract-schema.yaml` v2.0 — 已冻结

**允许修改的情况（需满足至少一项）：**

1. 新增一个 Contract Family（当前 Civil ✅ / MEI ✅ / EPC ⚠️ 待验证）
2. 出现现有字段无法表达的**新的商业关系类型**
3. 出现现有字段无法表达的**新的合同组件类型**（如某合同引入全新的 Exhibit 类别）

**禁止修改的情况：**

- 新增一个合同但只是数据值不同（填 YAML 即可）
- 新增一个 Canonical Type（更新 attachment-mapping.md，不改 Schema）
- 某字段为 null（那是数据缺失，不是 Schema 缺陷）

**升级流程：**

```
发现新情况
  ↓
对照本节"允许/禁止"清单
  ↓
允许 → 最小改动 → v2.1 → 记录变更原因
禁止 → 更新数据文件/Mapping，不改 Schema
```

---

## 五、证据层原则

| 原则 | 说明 |
|------|------|
| **只读** | `Main_Contract/`、`Subcon_Payments/`、`Project_Info/` 禁止写入任何新文件 |
| **不新增 Markdown** | 证据层只放 PDF / DOCX / XLSX，知识全在 `_Ref/` |
| **OCR 按商业价值分级** | critical → 优先 OCR；low/archive → 仅保留原文件 |
| **命名不动** | 原始文件名永不修改（命名规则用于新文件） |

---

## 六、设计决策记录

| 决策 | 结论 | 原因 |
|------|------|------|
| 为什么 HSE 不建 KO？ | 技术合规 > 商业影响 | 商业查询几乎不引用 ADNOC HSE 标准正文 |
| 为什么 Quality 不建 KO？ | 同上 | ITP/NDE 是工程执行工具，非合同管理工具 |
| 为什么 Issue 不独立？ | 当前多为单合同属性 | 待第一个跨合同 Issue 出现再升级 |
| 为什么 Timeline 降级？ | 合同管理员不记施工事件 | 只记商业里程碑 |
| 为什么 entity-schema 只有 3 类型？ | 商业知识库不需要 Equipment | 范围收窄到合同管理 |
| 为什么 Schema v2.0 冻结？ | 3/3 合同验证通过 | 增加新合同只需填数据 |

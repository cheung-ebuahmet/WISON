# Commercial Contract Knowledge Base — Wison RSGP

> **Claude Code 入口** — 面向合同管理（Commercial / Contract Administration）
> 最后更新: 2026-07-09

---

## 知识库地图

```
_Ref/                                    ← 商业合同知识层（仅商业相关）
├── schema/
│   ├── contract-schema.yaml             ← 合同 v2.0（含 exhibit 级 commercial_relevance）
│   ├── correspondence-schema.yaml       ← 商业函件
│   ├── entity-schema.yaml               ← 商业实体（Company/Person/Package）
│   └── issue-schema.yaml                ← 待建：商业问题
│
├── data/
│   ├── MASTER-INDEX.md                  ← 📍
│   ├── contracts/                       ← 合同 YAML（事实层）
│   │   ├── 10.1-CCECC-Civil-II.yaml     ← ✅ 95% 完整
│   │   ├── 10.2-TCC-Civil-I-III.yaml    ← ✅ 95% 完整
│   │   ├── 12.1-CCECC-MEI-I.yaml        ← ✅ 90% 完整
│   │   └── EPC-ADNOC-RSGP.yaml          ← ⚠️ 25%
│   ├── clause-library/                  ← 商业条款知识对象（规则层）
│   │   ├── Key-Personnel.md             ← ✅
│   │   ├── Key-Personnel-LD.md          ← ✅
│   │   └── Payment.md                   ← ✅ 新建
│   ├── commercial-analysis/             ← 商业分析层（解读）
│   │   └── back-to-back-matrix.md       ← ✅ 新建
│   ├── correspondence/                  ← 商业函件索引 (2 letters)
│   ├── companies/                       ← CCECC / TCC
│   └── people/                          ← Chen Zhiming
│
├── wiki/Commercial/
│   └── Subcontractor-Matrix.md          ← 自动编译
├── tasks/                               ← 成熟度追踪
└── timeline.md                          ← 合同里程碑（不记施工事件）
```

---

## 设计原则

> **"这份资料是否影响付款、变更、索赔、工期、违约责任、风险分配或合同履约？"**

| 答案 | 处理 |
|------|------|
| 会 → | OCR + Schema + Clause + 双向关联 |
| 不会 → | 保留原始文件，OCR 文本可有可无，不结构化 |

---

## 合同商业价值矩阵

| 合同 | 金额 | KP LD | 商业价值 | 成熟度 |
|------|------|:---:|:---:|:---:|
| 10.1 CCECC Civil II | AED 149.8M | AED 10,000 | ⭐ critical | 60% |
| 10.2 TCC Civil I/III | *(待)* | *(待)* | ⭐ critical | 35% |
| 12.1 CCECC MEI I | *(待)* | AED 10,000 | ⭐ critical | 35% |
| 12.2 TCC MEI II | 🔴 | 🔴 | ⭐ critical | 0% |
| EPC-ADNOC-RSGP | *(待)* | — | ⭐ critical | 25% |

> **Schema v2.0 — LOCKED** ✅ 3/3 合同验证通过（10.1 Attachment 体系 / 10.2 Atchments 体系 / 12.1 Exh A-K 体系）
> 建模原则: `_Ref/Modeling-Principles.md`

---

## 商业条款库（Clause Library）

| 优先级 | 条款 | 状态 |
|:---:|------|:---:|
| ⭐⭐⭐⭐⭐ | Payment | ✅ |
| ⭐⭐⭐⭐⭐ | Variation | ⚠️ 待建 |
| ⭐⭐⭐⭐⭐ | Delay / LD | ✅ KP-LD, ⚠️ Delay-LD |
| ⭐⭐⭐⭐⭐ | EOT | ⚠️ 待建 |
| ⭐⭐⭐⭐⭐ | Claims / Notice | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Termination | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Performance Security | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Retention | ⚠️ 待建 |
| ⭐⭐⭐⭐ | Advance Payment | ⚠️ 待建 |
| ⭐⭐⭐ | Warranty | ⚠️ 待建 |
| ⭐⭐⭐ | Insurance (商业部分) | ⚠️ 待建 |
| ⭐⭐ | 其他（不主动建 KO） | archive |

---

## Exhibit 商业价值一览（10.1 样板）

| Exhibit | 标题 | 商业价值 | 一级主题 |
|---------|------|:---:|------|
| Att 2 | Change Management | ⭐ critical | variation, claim |
| Att 5 | Scope of Work | ⭐ critical | scope, schedule, LD, KP |
| Att 6 | Commercials | ⭐ critical | boq, rates, payment |
| Att 1 | Communication Procedures | ⭐ medium | administrative |
| Att 7 | Owner's Special Requirements | ⭐ medium | back-to-back |
| Att 3 | HSE Requirements | ⭐ low | hse |
| Att 4 | Quality Management | ⭐ low | quality |

---

## 商业问题（Commercial Issues）— 活跃

| # | 合同 | 问题 | 状态 | 潜在成本 |
|---|------|------|:---:|------|
| 1 | 10.1 | 项目经理缺位 (Material Breach) | open | AED 10,000/day |
| — | — | *(后续新问题追加此处)* | | |

---

## 下一步

| # | 动作 |
|---|------|
| 1 | 10.1 样板验证通过后，批量迁移 10.2 / 12.1 / EPC |
| 2 | 建 issue-schema.yaml |
| 3 | 补建 5 个 ⭐⭐⭐⭐⭐ 条款 KO |
| 4 | 函件库：录入 10.1 Corres 目录下现有函件 |

---

## 原始数据层（只读）

| 数据区 | 路径 |
|--------|------|
| 总包合同 | `D:\Wison\Main_Contract\` |
| 分包合同 + 付款 + 信函 | `D:\Wison\Subcon_Payments\` |
| 命名规则 | `D:\Wison\_Ref\_Wison 文件与文件夹命名规则.md` |

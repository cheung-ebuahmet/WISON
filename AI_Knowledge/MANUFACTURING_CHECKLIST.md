# MANUFACTURING_CHECKLIST — 制造检查单 / Manufacturing Checklist
`[v0.2.2 · 每轮 OCR/结构化必跑 · 四阶段·固定产出·可复现]`

> **这不是检查单。这是工厂每轮生产的 BOM（Bill of Materials）。**
> 每次供给（OCR 一份文件、读一组条款、结构化一批数据），跑完本单四阶段，产出登记到 [`MANUFACTURING_LOG.md`](MANUFACTURING_LOG.md)。
> 与 [`KNOWLEDGE_SUPPLY_CHAIN.md`](KNOWLEDGE_SUPPLY_CHAIN.md) 的关系：供给链管"先造什么"（优先级）；制造检查单管"这一轮造出了什么"（产出）。

---

## 四阶段制造流水线 / 4-Stage Production Run

```
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1 — DOCUMENT STATUS        输入：PDF/文件               │
│ OCR? ▢  Quality? __%  Metadata? ▢  Signed? ▢  Missing? ▢   │
├─────────────────────────────────────────────────────────────┤
│ STAGE 2 — KNOWLEDGE PRODUCED     知识产出（结构化事实）         │
│ New Clauses __  New Definitions __  New Parties __           │
│ New Deliverables __  New Procedures __  New Dates __         │
├─────────────────────────────────────────────────────────────┤
│ STAGE 3 — COMMERCIAL OUTPUT      商业产出（可执行对象）         │
│ New Rules __  Rules Updated __  DNA Updated __               │
│ Evidence Added __  Risk Updated __  Events Added __          │
│ Unknowns Cleared __                                        │
├─────────────────────────────────────────────────────────────┤
│ STAGE 4 — CAPABILITY IMPROVEMENT  能力增长（量化 Δ）           │
│ DNA Coverage __% → __%  (+__%)                               │
│ Domain __% → __%  (e.g. Insurance 18% → 42%  +24%)          │
│ Capability __ → __  (C3 ◐ → 🟢)                              │
│ Capability Debt Repaid __                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Stage 1 — Document Status（进料检查）

| 检查项 | 选项 | 说明 |
|---|---|---|
| OCR? | ▢ YES / ▢ NO / ▢ PARTIAL | 文本层是否可提取 |
| Quality | __% | OCR 质量（人工抽查 3 页取均值） |
| Metadata | ▢ YES / ▢ NO | 文件名·日期·版本·签署方 |
| Signed? | ▢ YES / ▢ NO / ▢ DRAFT | 签署状态 |
| Missing? | ▢ YES / ▢ NO | 是否在 Master Index 标注缺失 |
| Pages | __ | 总页数 |

---

## Stage 2 — Knowledge Produced（知识产出·结构化事实）

| 产出类型 | 数量 | 说明 |
|---|---|---|
| New Clauses | __ | 未在现有 CONTRACT_MAP / COMMERCIAL_DNA 中出现的新条款引用 |
| New Definitions | __ | 新发现的定义术语 |
| New Parties | __ | 新出现的组织/角色 |
| New Deliverables | __ | 合同要求承包商提交的新交付物 |
| New Procedures | __ | 新发现的程序/流程 |
| New Dates | __ | 新发现的里程碑/截止日期 |
| New Obligations | __ | "谁·必须做什么·何时"的新实例 |
| New Exceptions | __ | 规则的例外/排除情形 |

---

## Stage 3 — Commercial Output（商业产出·可执行对象）

| 产出类型 | 数量 | 说明 |
|---|---|---|
| New Rules | __ | 新生成的可执行规则（→ `03_Rules/`） |
| Rules Updated | __ | 已有规则因新信息而修改 |
| DNA Updated | __ | COMMERCIAL_DNA 某区新增/修改了条款绑定 |
| Evidence Added | __ | Evidence Matrix 新增证据类型或来源 |
| Risk Updated | __ | Risk Taxonomy 新增风险条目或分类调整 |
| Events Added | __ | Event Library 新增事件类型 |
| Unknowns Cleared | __ | 从 UNKNOWN_REGISTRY 中消除的条目 |
| Philosophy Candidate | __ | 新发现的可能晋升为商业哲学的模式 |

---

## Stage 4 — Capability Improvement（能力增长·量化 Δ）

| 指标 | 运行前 | 运行后 | Δ | 说明 |
|---|---|---|---|---|
| DNA Coverage | __% | __% | +__% | 21 区中 🟢 率的变化 |
| Domain: [名称] | __% | __% | +__% | 商业域覆盖率的提升（以 CAPABILITY_DASHBOARD 为准） |
| Capability: [C1-C7] | [状态] | [状态] | — | 能力等级是否升级（◐→🟡→🟢） |
| Capability Debt Repaid | — | — | __ | 偿还了多少 Capability Debt 条目（→ CAPABILITY_DEBT.md） |

---

## 四问闸门 / 4-Question Gate（与供给链联动）
> 制造完成后必答。来自 [`KNOWLEDGE_SUPPLY_CHAIN.md`](KNOWLEDGE_SUPPLY_CHAIN.md)。

| Q | 答案 |
|---|---|
| Q1 补充了哪些 Facts？ | |
| Q2 增强了哪些 Capability？ | |
| Q3 消除了哪些 Unknowns？ | |
| Q4 产生了新的 DNA/Rule/Philosophy？ | |

---

## 制造产出等级 / Knowledge Yield Grade

| Grade | Rule Δ | DNA Δ | Capability Δ | 含义 |
|---|---|---|---|---|
| ⭐⭐⭐⭐⭐ | ≥3 | ≥4 | ≥+15% | 超高价值供给（如 Insurance Annex） |
| ⭐⭐⭐⭐ | 2 | 2-3 | +10-14% | 高价值供给 |
| ⭐⭐⭐ | 1 | 1-2 | +5-9% | 中等价值供给 |
| ⭐⭐ | 0 | 0-1 | +1-4% | 低价值供给（仅补充性） |
| ⭐ | 0 | 0 | 0% | 无能力增量——仅资料层 |

> ⭐⭐ 及以下：审查该文件是否真正需要制造，或是否应用更低成本方式处理。

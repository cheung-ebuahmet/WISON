# ROADMAP — 能力演进路线 / Capability Roadmap
`[v0.1.0 → v1.0 · 每版增加一种能力 · 知识供给链驱动 · 2026-07-13]`

> **核心原则**：后续所有提交以**增加一种 Capability** 为目标。每次提交让系统变得更聪明，而非更大。
> **供给哲学**：OCR/结构化不是"补资料"——是给 Rule Engine 和 Reasoning Engine **供燃料**。每次供给过四问闸门（[`KNOWLEDGE_SUPPLY_CHAIN.md`](KNOWLEDGE_SUPPLY_CHAIN.md)）。
> **驾驶舱**：[`CAPABILITY_DASHBOARD.md`](CAPABILITY_DASHBOARD.md) — 系统的智商计，不是进度表。
> **未知驱动**：[`UNKNOWN_REGISTRY.md`](UNKNOWN_REGISTRY.md) — Unknown 越少，Capability 越高。

---

## v0.3 基础设施层（当前）— Supply Chain + Dashboard
- [x] CAPABILITY_DASHBOARD.md — 能力覆盖率（非 OCR 率）
- [x] KNOWLEDGE_SUPPLY_CHAIN.md — 供给链 + 四问闸门 + 优先级算法
- [x] UNKNOWN_REGISTRY.md — 24 项开放未知 + 14 项已消除
- [ ] Risk Taxonomy 正式分类框架 (v0.2.1)
- [ ] Event Library 枚举 + 路由 (v0.2.2)
- [ ] Obligation Matrix (v0.3) — Who·Must Do·When·Condition·Evidence·Consequence

## 从 v0.1.0 到 v1.0：十层能力栈
```
Commercial Philosophy  ── 价值观，稳定，少改
        │
Commercial DNA        ── 商业事实，条款绑定
        │
Risk Taxonomy         ── 统一风险分类 ★ v0.2.1
        │
Rule Engine           ── 可执行规则（非解释）★ v0.2.0
        │
Event Library         ── 事件→条款→通知→证据→策略 ★ v0.2.2
        │
Obligation Matrix     ── 谁·必须做什么·何时·证据·后果 ★ v0.3
        │
Decision Tree         ── 是/否分支推理 ★ v0.4
        │
Clause Dependency     ── 条款间影响传播 ★ v0.5
        │
Evidence Matrix       ── 证据类型·法律权重·缺失风险 ★ v0.6
        │
Gap Detector          ── 主合同 vs External Contract 自动扫描 ★ v0.7
        │
Commercial Playbook   ── 收到 X → 第1小时/天/周做什么 ★ v0.8
        │
Reasoning Protocol    ── 横切所有层：统一推理路径（任何模型通用）★ v0.2 元能力
```

---

## v0.2 — Rule Engine + Reasoning Protocol + Supply Chain ✅
`系统从"解释合同"→"运行合同"→"供给驱动"`

### v0.2.0 Rule Engine ✅
- [x] Rule Template 定型 + 首批 4 条可执行规则
- [x] C5🟢 C7🟢 C3🟡

### v0.2.1 Supply Chain Infrastructure ✅
- [x] **CAPABILITY_DASHBOARD.md** — 能力驾驶舱（系统的智商计，非进度表）
- [x] **KNOWLEDGE_SUPPLY_CHAIN.md** — 供给链 + 四问闸门 + 优先级算法
- [x] **UNKNOWN_REGISTRY.md** — 24 项开放未知 + 14 项已消除

### v0.2.2 Risk Taxonomy（→ next）
- [ ] 统一分类：Commercial · Contractual · Financial · Schedule · Quality · Insurance · HSE · Legal · Interface · Supply Chain · Authority · Tax
- [ ] 每条 Rule/DNA → 绑定 Risk Category
- [ ] Risk Filter：按类别筛选所有敞口

### v0.2.3 Contract Event Library（→ next）
- [ ] 事件枚举 + Event → Articles → Risk → Notice → Evidence → Strategy 链
- [ ] 与 Reasoning Protocol 联动：事件输入→自动路由

---

## v0.3 — Obligation Matrix
- [ ] Obligation 模板：Who · Must Do · When · Condition · Evidence · Consequence
- [ ] 关键义务抽取（From Art 4/5/9/10/18/19/20/21/23/24/30）
- [ ] 遗漏检查能力

## v0.4 — Decision Tree
- [ ] 核心商业流程的决策树：Variation · Claim · Payment · EOT · Suspension
- [ ] 是/否分支 → 叶子结论
- [ ] 与 Rule Engine 互操作

## v0.5 — Clause Dependency Graph
- [ ] Clause A → Clause B → Clause C 依赖链
- [ ] "修改此处→影响下游"传播分析

## v0.6 — Evidence Matrix
- [ ] 证据统一字段：Type · Purpose · Legal Weight · Typical Source · Acceptability · Missing Risk
- [ ] 证据→Claim/Notice 关联
- [ ] "缺什么证据"判定能力

## v0.7 — Gap Detector
- [ ] Main Contract vs External Contract 自动比对
- [ ] 输出：Gap · Exposure Level · Recommendation
- [ ] C7 从手动验证升级为自动扫描

## v0.8 — Commercial Playbook
- [ ] 场景驱动：收到 VO / 收到 Claim / 分包延误 / 业主暂停 / NCR …
- [ ] 时间线行动：第1小时 → 第1天 → 第1周 → 升级 → Claim
- [ ] 与 Decision Tree + Evidence Matrix 联动

## v1.0 — Commercial Expert System
- [ ] 十层全通
- [ ] 任意商业问题输入 → 七步推理 → 有条款、有规则、有证据判断、有风险结论、有行动建议
- [ ] 模型无关，知识库即引擎

---

## 版本策略 / Versioning
- 每个能力增量 = 一个 minor 版本（v0.2.0, v0.2.1, …）
- 能力组完成 = patch（如 v0.2 = Rule Engine + Event Library + Risk Taxonomy）
- v1.0 = 十层全通 + 至少一个真实项目的 External Contract C7 全验 + 至少 5 个真实案例
- **提交信息格式**：`v0.x.y – Capability name: what the system can now do`

# V04_GATES — v0.4 Decision Engine 进入门槛 / Entry Gates for v0.4
`[v0.3.6 · 三道门 · 可度量 · 不满足 = 继续积累 · 满足 = v0.4 启动]`

> **v0.4 不用时间衡量，不用文件数量衡量。用三道可度量门槛。**
> 每道门 = 系统从"能推理"走向"有经验"的一个硬条件。
> 当前状态：**3/3 CLOSED**。在门打开之前，所有能力增量走 v0.3.x。

---

## Gate 1 — Decision Corpus ✅/❌

**条件**：10 类商业事件各达目标数 → Corpus 覆盖 ≥50%

| 类型 | 当前 | 目标 | 状态 |
|---|---|---|---|
| Delay | 1 | ≥3 | ❌ |
| Payment | 0 | ≥3 | ❌ |
| Variation | 0 | ≥3 | ❌ |
| KP/Personnel | 1 | ≥2 | ❌ |
| Subcontract Default | 0 | ≥2 | ❌ |
| Quality/Defect | 0 | ≥2 | ❌ |
| Acceptance | 0 | ≥2 | ❌ |
| Insurance | 0 | ≥1 | ❌ |
| Warranty | 0 | ≥1 | ❌ |
| HSE/FM | 0 | ≥1 | ❌ |
| **TOTAL** | **2/35 (6%)** | **≥20** | ❌ |

**Gate 1 通过条件**：≥6/10 类型各有 ≥1 事件 **且** Total ≥20。
**当前**：CLOSED。

---

## Gate 2 — Core Rule Validation ✅/❌

**条件**：4 条核心 Rule 全部达 Validation Level ≥ L2

| Rule | 当前 L | 目标 L | 状态 |
|---|---|---|---|
| RULE-001 CVR Time-bar | L1 | **L2** | ❌ |
| RULE-002 LD Flow-down | L2 | **L2** | ✅ |
| RULE-003 Warranty Gap | L0 | **L2** | ❌ |
| RULE-004 Payment Precondition | L0 | **L2** | ❌ |

**Gate 2 通过条件**：4/4 Rules ≥ L2。
**当前**：1/4 → CLOSED。

---

## Gate 3 — Cross-Domain Conflict Validation ✅/❌

**条件**：≥5 个冲突完成 Impact Quantification（非仅理论识别）

| Conflict | 理论 | 量化 | Event验证 | 状态 |
|---|---|---|---|---|
| CF-AC-001 (Warranty gap) | ✅ | 🟡 4mo est. | ❌ | ❌ |
| CF-AC-004 (PBG gap) | ✅ | 🟡 ~2yr est. | ❌ | ❌ |
| CF-AC-002 (Insurance window) | ✅ | ❌ | ❌ | ❌ |
| CF-AC-003 (Payment float) | ✅ | 🟡 4mo est. | ❌ | ❌ |
| CF-AC-005 (LD asymmetry) | ✅ | 🟡 条款逻辑 | ❌ | ❌ |

**Gate 3 通过条件**：≥5 冲突中 ≥3 完成 Impact Quantification **且** ≥1 有真实事件验证。
**当前**：0/5 量化 + 0/5 验证 → CLOSED。

---

## 门状态总览 / Gate Status Summary

```
Gate 1 — Corpus:          CLOSED (6% → need 57%)
Gate 2 — Rule Validation:  CLOSED (1/4 L2 → need 4/4)
Gate 3 — Conflict Quant:   CLOSED (0/5 validated → need ≥3 quantified + ≥1 event-validated)

ALL GATES: CLOSED — Decision Engine cannot start.
```

---

## 开门策略 / Path to Open

| 优先级 | 动作 | 推动的门 |
|---|---|---|
| 🔴 1 | 结构化 Payment + Variation 事件（各 ≥1） | Gate 1 |
| 🔴 2 | 真实事件验证 RULE-001 CVR（需 CVR 案例） | Gate 2 |
| 🔴 3 | 真实事件验证 RULE-003 Warranty（需 Warranty Claim） | Gate 2 |
| 🟡 4 | 量化 CF-AC-001 + CF-AC-004（需 WC/PAC 实际日期） | Gate 3 |
| 🟡 5 | 补 Subcontract Default + Acceptance 事件 | Gate 1 |
| 🟢 6 | Insurance + Warranty 真实事件（低频——等待） | Gate 1 + Gate 3 |

---

## 门的设计原则

> **门不是惩罚。是保护。** 它保护 Decision Engine 不在训练数据不足时做出表面漂亮但不可靠的判断。
> 每打开一道门 → 系统从"聪明"向"有经验"迈进一步。
> 三道门全开 → v0.4 的水到渠成，而非强行上线。

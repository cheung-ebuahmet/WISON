# CAPABILITY_DEBT — 能力债登记簿 / Capability Debt Register
`[v0.2.2 · 活文档 · 每次制造后更新 · 规则≠100%，缺口=债务]`

> **能力债（Capability Debt）= 规则已存在，但缺乏完整的证据绑定 / 例外处理 / 下游数据支撑。**
> 类比软件工程的技术债：能跑但不完整。每条债务须标注债权人（谁缺）、偿还条件（补什么）、利息（不还会怎样）。
> 偿还一条债务 → 对应 Capability 覆盖率上升 → 记录在 [`MANUFACTURING_LOG.md`](MANUFACTURING_LOG.md)。

---

## 债务登记 / Debt Register

| Debt ID | 债务人（Rule/能力） | 债务性质 | 缺什么 | 利息（不还的后果） | 偿还途径 | 优先级 |
|---|---|---|---|---|---|---|
| CD-001 | RULE-001 CVR Time-bar | Evidence Gap | Notice wording 模板未提取；Meeting Minutes 证据权重未定义 | Time-bar 判定只能做"是否逾限"，无法判定"是否有有效 Notice" | 从合同/实践提取 Notice 模板格式要求 | 🟡 B |
| CD-002 | RULE-001 CVR Time-bar | Exception Gap | Art 24.7 的完整排除清单（哪些指令明确"不构成 Variation"）未穷举 | 可能将排除情形误判为 Variation | 逐条精读 Art 24.7 并结构化 | 🟡 B |
| ~~CD-003~~ | ~~RULE-002 LD Flow-down~~ | — | ✅ **REPAID v0.3.0** — LD_Mapping: 10.1/10.2/12.1 LD 全参数已映射 | — | — | — |
| ~~CD-004~~ | ~~RULE-003 Warranty Gap~~ | — | ✅ **REPAID v0.3.0** — Warranty_Mapping: 10.1/10.2/12.1 Warranty 全参数已映射 | — | — | — |
| ~~CD-005~~ | ~~RULE-004 Payment Precondition~~ | — | ✅ **REPAID v0.3.0** — Payment_Mapping: 10.1/10.2/12.1 Payment 全参数已映射 | — | — | — |
| CD-006 | C3 Requirement | Modeling Gap | Requirement 超类未细化：Satisfied/Outstanding 判定逻辑未形式化 | C3 无法从 ◐ 升级到 🟢 | 建立 Obligation Matrix（v0.3） | 🟡 B |
| CD-007 | C6 Claim | Modeling Gap | Claim 实体未建模；Detailed Claim 的合同要求结构未定义 | 无法判断 Claim 是否"合格提交" | 精读 Art 25 + 建立 Claim 实体（v0.3） | 🟡 B |
| ~~CD-008~~ | ~~C1 Authority~~ | — | ✅ **REPAID v0.3.0** — KP_Mapping: 10.1/10.2 KP 人名+LD 条件已映射 | — | — | — |
| CD-009 | C4 B2B | Data Gap | 实际分包合同文本未读取——B2B 检查停留在主合同 side | 无法验证任何真实 Gap | 读取首份 External Contract | 🔴 A |
| ~~CD-010~~ | ~~DNA-9 Insurance~~ | — | ✅ **REPAID v0.3.2** — Insurance_Mapping: Art 41 + ANX7 + 5 subs verbatim | — | — | — |
| ~~CD-011~~ | ~~DNA-15 Acceptance~~ | — | ✅ **REPAID v0.3.3** — Acceptance_Mapping: Art 15+17+ANX11+ANX11D+分包验收全参数 | — | — | — |

---

## Confidence Debt / 可信度债（新增 v0.3.1）
> 区别于 Capability Debt——系统"能做"但"有多可靠"不确定。

| CF-ID | 映射 | 缺口维度 | 影响 | 偿还途径 |
|---|---|---|---|---|
| CF-001 | Notice | Issue Validation 42% | 无法验证 14d vs 5WD 在实际信函中的运作 | 结构化剩余 12 封函件 |
| CF-002 | Warranty | Validation 45% | 无 Warranty Claim 事件验证 PBG 空窗期 | 等待/搜索 Warranty 信函 |
| CF-003 | KP | Coverage 72% | 12.1/12.2 MEI KP 名单缺失 | 提取 12.1/12.2 Exh E KP 名单 |
| CF-004 | Payment | Validation 55% | 无 IPC 执行记录 | 提取 IPC 记录 |
| ~~CF-005~~ | ~~Insurance~~ | — | ✅ **REPAID v0.3.2** — Coverage <20%→78% · Confidence 71% | — | — |

---

## 债务统计 / Debt Summary

| 类别 | 数量 | 优先级分布 |
|---|---|---|
| Evidence Gap（证据缺失） | 2 | 🟡 B ×2 |
| Data Gap（数据缺失） | 5 | 🔴 A ×4 · 🟢 C ×1 |
| Exception Gap（例外未穷举） | 1 | 🟡 B |
| Modeling Gap（模型缺失） | 2 | 🟡 B ×2 |
| Full Gap（全空白） | 2 | 🔴 A ×2 |
| **合计** | **8** (曾12) | 🔴A=2 · 🟡B=5 · 🟢C=1 |

---

## 债务偿还记录 / Debt Repayment Log

| Debt ID | 偿还日期 | 偿还方式 | Version |
|---|---|---|---|
| CD-003 | 2026-07-13 | LD_Mapping：10.1/10.2/12.1 LD 全参数映射 → RULE-002 Runtime Ready | v0.3.0 |
| CD-004 | 2026-07-13 | Warranty_Mapping：10.1/10.2/12.1 Warranty 全参数映射 → RULE-003 Runtime Ready | v0.3.0 |
| CD-005 | 2026-07-13 | Payment_Mapping：10.1/10.2/12.1 Payment 全参数映射 → RULE-004 enhanced | v0.3.0 |
| CD-008 | 2026-07-13 | KP_Mapping：10.1/10.2 KP 人名+LD 条件映射 → C1 operational | v0.3.0 |

---

## 净能力 / Net Capability
> Gross Capability（CAPABILITY_DASHBOARD） − Capability Debt = Net Capability。
> 这是系统的"真实智商"——扣除了债务后的可用能力。

| 能力 | Gross | Debt Load | Net |
|---|---|---|---|
| C1 | 65% | 低 | 60% |
| C2 | 65% | 低 | 60% |
| C3 | 55% | 中（CD-006） | 45% |
| C4 | 70% | 高（CD-009） | 45% |
| C5 | 78% | 中（CD-001/002） | 65% |
| C6 | 55% | 中（CD-007） | 45% |
| C7 | **85%** | 中（CD-009） | **65%** |

> **v0.3.0–v0.3.3 偿还 7 条债务 (CD-003/004/005/008/010/011 + CF-005 + U-001/U-002)。C7 Net 40%→65%。Insurance 25%→78%。Acceptance 15%→62%。** 剩余 CD: 6 条 · CF: 3 条 · **VD: 10 条（新增 v0.3.5）**。

---

## Validation Debt / 验证债（新增 v0.3.5 → 详见 [`VALIDATION_DEBT.md`](VALIDATION_DEBT.md)）
> "逻辑正确但未经实测"——共 10 条。偿还=Rule/Mapping/Conflict 的 Validation Level 上升。

| VD-ID | 对象 | 缺什么验证 | 当前 L | 优先 |
|---|---|---|---|---|
| VD-001 | RULE-003 Warranty | 真实 Warranty Claim 事件 | L0 | 🔴 |
| VD-002 | RULE-004 Payment | 真实 IPC 执行记录 | L0 | 🔴 |
| VD-003 | CF-AC-001 | WC→PAC 时间差量化 | L1 | 🔴 |
| VD-004 | CF-AC-004 | PBG 空窗期时长量化 | L1 | 🔴 |
| VD-005~010 | 其余 | 见 VALIDATION_DEBT.md | — | 🟡🟢 |

## 三重全景
```
Capability Debt (CD):  6  ← 偿还=新能力（广度）
Confidence Debt (CF):  3  ← 偿还=可信度↑（深度）
Validation Debt (VD):  10 ← 偿还=可验证性↑（硬度）
─────────────────────────────────
TOTAL:                19  → 三重全清 = v1.0
```

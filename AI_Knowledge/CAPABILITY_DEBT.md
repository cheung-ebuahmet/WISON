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
| CD-003 | RULE-002 LD Flow-down | Data Gap | 无 External Contract 实际数据——只能判定"缺 LD 则 Uncovered"，无法针对具体分包输出 | C7 停留在通用规则层，无法逐包验证 | 读取首份 External Contract 并运行 RULE-002 | 🔴 A |
| CD-004 | RULE-003 Warranty Gap | Data Gap | 同 CD-003——无分包 Warranty 数据 | 同上 | 读取首份 External Contract 并运行 RULE-003 | 🔴 A |
| CD-005 | RULE-004 Payment Precondition | Evidence Gap | PBG/PCG/APG 的 ANX8 格式全文未精读；保函"见索即付"条款未确认 | 无法验证实际保函是否满足 ANX8 要求 | 精读 ANX8-A/B/C 格式 + 提取关键字段 | 🟡 B |
| CD-006 | C3 Requirement | Modeling Gap | Requirement 超类未细化：Satisfied/Outstanding 判定逻辑未形式化 | C3 无法从 ◐ 升级到 🟢 | 建立 Obligation Matrix（v0.3） | 🟡 B |
| CD-007 | C6 Claim | Modeling Gap | Claim 实体未建模；Detailed Claim 的合同要求结构未定义 | 无法判断 Claim 是否"合格提交" | 精读 Art 25 + 建立 Claim 实体（v0.3） | 🟡 B |
| CD-008 | C1 Authority | Data Gap | Engineer/Company Rep 的 Authority Constraint 阈值未填 | "PM 能否批 500 万 VO"无法推理 | 从合同/实践提取阈值 | 🟢 C |
| CD-009 | C4 B2B | Data Gap | 实际分包合同文本未读取——B2B 检查停留在主合同 side | 无法验证任何真实 Gap | 读取首份 External Contract | 🔴 A |
| CD-010 | DNA-9 Insurance | Full Gap | Art 41 + ANX7 全文未读 | Insurance Exposure 完全无法评估 | 制造 Art 41 + ANX7 | 🔴 A |
| CD-011 | DNA-15 Acceptance | Full Gap | Art 15/17 + ANX11 未读 | 验收触发付款/质保/担保降档无法推理 | 制造 Art 15/17 + ANX11 | 🔴 A |

---

## 债务统计 / Debt Summary

| 类别 | 数量 | 优先级分布 |
|---|---|---|
| Evidence Gap（证据缺失） | 2 | 🟡 B ×2 |
| Data Gap（数据缺失） | 5 | 🔴 A ×4 · 🟢 C ×1 |
| Exception Gap（例外未穷举） | 1 | 🟡 B |
| Modeling Gap（模型缺失） | 2 | 🟡 B ×2 |
| Full Gap（全空白） | 2 | 🔴 A ×2 |
| **合计** | **12** | 🔴A=6 · 🟡B=5 · 🟢C=1 |

---

## 债务偿还记录 / Debt Repayment Log
> 每次制造后，已偿还的债务移入此处。

| Debt ID | 偿还日期 | 偿还方式 | Version |
|---|---|---|---|
| — | — | — | — |

---

## 净能力 / Net Capability
> Gross Capability（CAPABILITY_DASHBOARD） − Capability Debt = Net Capability。
> 这是系统的"真实智商"——扣除了债务后的可用能力。

| 能力 | Gross | Debt Load | Net |
|---|---|---|---|
| C1 | 60% | 低（CD-008） | 55% |
| C2 | 65% | 低 | 60% |
| C3 | 50% | 中（CD-006） | 40% |
| C4 | 70% | 高（CD-009） | 45% |
| C5 | 78% | 中（CD-001/002） | 65% |
| C6 | 55% | 中（CD-007） | 45% |
| C7 | 75% | 高（CD-003/004/009） | 40% |

> C7 的 Gross 75% vs Net 40% 差距最大——因为规则已可执行，但没有分包数据供其运行。**偿还 CD-003+CD-004+CD-009 是当前最高优先级。**

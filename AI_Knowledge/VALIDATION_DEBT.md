# VALIDATION_DEBT — 验证债务登记簿 / Validation Debt Register
`[v0.3.5 · 新增负债类别 · 驱动 Calibration 优先级 · 每次验证记录后偿还]`

> **Validation Debt ≠ Capability Debt ≠ Confidence Debt。** VD 回答的是："这个结论逻辑正确——但有没有真实事件证明过？"
> 偿还一条 VD → 对应 Rule/Mapping/Conflict 的 Validation Level 上升。
> Validation Debt 越少 → Decision Engine 的信度越高 → v0.4 的门越近。

---

## 当前验证债务 / Open Validation Debts

### 🔴 HIGH — 阻塞 Decision Engine 的关键验证

| VD-ID | 对象 | 缺什么验证 | 当前 L | 目标 L | 偿还方式 | 阻塞 |
|---|---|---|---|---|---|---|
| VD-001 | RULE-003 Warranty Gap | 真实 Warranty Claim 事件 | L0 | L1 | 等/查 Warranty 相关函件或缺陷通知 | C3·C6 |
| VD-002 | RULE-004 Payment | 真实 IPC 执行记录 | L0 | L1 | 提取至少 1 份 IPC + 1 次付款争议（如有） | C3 |
| VD-003 | CF-AC-001 (Warranty gap) | WC→PAC 实际时间差量化 | L1 | L2 | 确认 Civil WC 预测日期 vs EPC PAC 预测日期 | C4·C7 |
| VD-004 | CF-AC-004 (PBG gap) | PBG 空窗期实际时长量化 | L1 | L2 | 确认 Civil PBG 到期日 vs EPC FA 预计日 | C4·C7 |

### 🟡 MEDIUM — 提升可信度的补充验证

| VD-ID | 对象 | 缺什么验证 | 当前 L | 目标 L | 偿还方式 |
|---|---|---|---|---|---|
| VD-005 | RULE-001 CVR | CVR 超时失权的真实案例 | L1 | L2 | 行业案例 / 本项目未来事件 |
| VD-006 | CF-AC-005 (LD asymmetry) | 12.1 MC Relief 实际触发情况 | L1 | L2 | 跟踪 12.1 MC 进度 → 判断 LD 退还可能性 |
| VD-007 | All Mappings | 12.2 TCC MEI II 完整数据 | L1 | L2 | 结构化 12.2 合同商业参数 |
| VD-008 | CF-AC-002/003/004 | Mitigation Strategy per conflict | L0 | L1 | 为每个 🔴/🟡 冲突制定缓解措施 |

### 🟢 LOW — 优化性验证

| VD-ID | 对象 | 缺什么验证 |
|---|---|---|
| VD-009 | All Rules | Exception 反例系统测试（主动寻找可使 Rule 失效的边缘情形） |
| VD-010 | Decision Corpus | ≥30 结构化事件（当前 2） |

---

## 验证债务统计 / VD Summary

| 优先级 | 数量 | 说明 |
|---|---|---|
| 🔴 HIGH | 4 | 阻塞 RULE-003/004 升级 + Conflict 量化 |
| 🟡 MEDIUM | 4 | 提升现有结论的可信度 |
| 🟢 LOW | 2 | 系统级优化 |
| **合计** | **10** | |

---

## 三重债务全景 / Three-Debt Panorama

| 债务类型 | 数量 | 含义 | 偿还=系统获得什么 |
|---|---|---|---|
| **Capability Debt** (CD) | 6 (曾12) | 系统"不能做什么" | 新能力 |
| **Confidence Debt** (CF) | 3 (曾5) | 系统"做到但多可靠" | 可信度 ↑ |
| **Validation Debt** (VD) | 10 | 系统"逻辑正确但未经实测" | 可验证性 ↑ |
| **合计** | **19** | | |

> **三重债务的相互关系**：
> - 偿还 CD → 系统能做新的事（广度）
> - 偿还 CF → 系统更有底气做已有的（深度）
> - 偿还 VD → 系统被证明是可靠的（硬度）
> - 三重全清 → v1.0

---

## 债务偿还记录 / VD Repayment Log

| VD-ID | 偿还日期 | 偿还方式 | Version |
|---|---|---|---|
| — | — | — | — |

> VD-001~004 的偿还需要真实项目事件——不能用推理替代。这是 Calibration 与 Construction 的本质区别。

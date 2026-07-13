# VALIDATION_REGISTER — 验证登记簿 / Validation Register
`[v0.3.5 · 所有验证记录 · 每次新增证据/事件后登记 · 驱动 Validation Level 上升]`

> **这不是日志。这是系统的 Proof of Trust。** 每一项验证记录 = 一条证据链，证明某个 Rule/Mapping/Conflict 的结论不是凭空推理，而是有合同、有数据、有事件支撑的。
> 验证记录按 Validation Level 分层：L0（未验证）→ L1（单实例）→ L2（跨合同）→ L3（全量）→ L4（反例测试）

---

## 验证记录 / Validation Records

### VR-001 · RULE-002 LD — Cross-Contract Validation ✅ L2
- **验证对象**：RULE-002（LD Flow-down）
- **验证方式**：跨合同对比——EPC ANX5 A.09 (15 milestones, 0.01167%-0.03333%/day, Cap 10%) vs 10.1 (0.1%/day, Cap 10%) vs 10.2 (0.1%/day, Cap 10%) vs 12.1 (0.1%/day, Cap 10%, MC Relief)
- **结论**：LD Cap 对等（10% = 10%），LD 费率 Inverse（分包 0.1% >> EPC 最低 0.01167%），对 Wison 有利
- **证据**：FOA p.4-5 · ANX5 A.09 §A.9.2.3 · `_Ref/data/contracts/10.1/10.2/12.1-*.yaml`
- **日期**：2026-07-13
- **Level**：L2 —— 跨 3 份合同验证通过

### VR-002 · RULE-002 LD — Issue Validation ✅ L2
- **验证对象**：RULE-002（LD Flow-down）
- **验证方式**：真实事件——12.1 MEI Pkg I Milestone #2 逾期 (Pkg1 25d + Pkg3 39d)，LD 已触发
- **结论**：LD 机制按合同生效——SLT-5312-WSN-CCC-0006 Notice 已发，AED 160,892/day 计罚
- **证据**：`Subcon_Payments/12.1/Corres/SLT-5312-WSN-CCC-0006_NOTICE DEF MEI Pkg I_ocred.pdf` · `_Ref/data/timeline.md`
- **日期**：2026-07-13
- **Level**：L2 —— 跨合同验证 + 单实例事件

### VR-003 · KP_Mapping — Issue Validation ✅ L2
- **验证对象**：KP_Mapping（关键人员映射）
- **验证方式**：真实事件——10.1 CCECC Civil II PM 陈志明 2026-05-25 离岗，6/24 假期届满未归 → KP-LD AED 10,000/天
- **结论**：KP-LD 机制按合同触发——Sub-Clause 4.2.4 + 4.3.7 Material Breach 已激活
- **证据**：`Subcon_Payments/10.1/Corres/SLT-5312-WSN-CCE-0020_Notice-PM-Absence_ocred.pdf` · `_Ref/data/clause-library/Key-Personnel-LD.md`
- **日期**：2026-07-13
- **Level**：L2 —— 2 份合同 KP 数据一致（10.1 + 10.2），1 个真实事件

### VR-004 · Insurance_Mapping — Cross-Contract Validation ✅ L2
- **验证对象**：Insurance_Mapping（保险 B2B）
- **验证方式**：跨合同对比——EPC Art 41 vs 5 份分包 Insurance Requirements (.docx) —— 全部逐字复制
- **结论**：12/12 Insurance clauses Covered——迄今 Back-to-Back 最完整的域
- **证据**：GTC Art 41.1–41.19 · ANX7-1 · 分包 Insurance Requirements (10.1/10.2/12.1/12.2/99) · `_Ref/data/contracts/*.yaml`
- **日期**：2026-07-13
- **Level**：L2 —— 跨 5 份合同验证通过

### VR-005 · Acceptance_Mapping — Clause Validation ✅ L1
- **验证对象**：Acceptance_Mapping（Handover Risk Transfer）
- **验证方式**：条款原文验证——Art 15 (MC/RFSU) + Art 17 (PA/FA) + ANX11 B.38 (50pp) + ANX11D-1~7 certificates + ANX11E Release 全文已读
- **结论**：7-event chain (MC→Commissioning→RFSU→Start-up+Perf Tests→PAC→ETC→FAC) 完整映射，每个事件的 commercial effect 已标注
- **证据**：GTC Art 15/17 · ANX11 B.38 · ANX11D forms
- **日期**：2026-07-13
- **Level**：L1 —— 条款层验证完成，跨合同对比完成（3/4 分包），待真实 PAC 事件

### VR-006 · Cross-Domain Conflict — Theoretical Validation ✅ L1
- **验证对象**：Cross-Domain Conflict Engine
- **验证方式**：五域联动理论检查——Acceptance vs Warranty/Security/Insurance/Payment/LD
- **结论**：5 个真实冲突识别（2🔴 + 3🟡），全部有 clause 引用 + Gap 量化 + 涉及分包标注
- **证据**：`CROSS_DOMAIN_CONFLICT_ENGINE.md` · CF-AC-001~005
- **日期**：2026-07-13
- **Level**：L1 —— 理论验证完成，量化模型部分完成，待真实事件冲击测试

---

## 验证缺口 / Pending Validation

| VP-ID | 对象 | 需要的验证 | 当前 Level | 目标 Level | 优先级 |
|---|---|---|---|---|---|
| VP-001 | RULE-003 Warranty | 真实 Warranty Claim 事件 | L0 | L1 | 🔴 |
| VP-002 | RULE-004 Payment | 真实 IPC 执行记录 | L0 | L1 | 🔴 |
| VP-003 | CF-AC-001 | WC→PAC 实际时间差数据 | L1 | L2 | 🔴 |
| VP-004 | CF-AC-004 | PBG 空窗期量化验证 | L1 | L2 | 🔴 |
| VP-005 | RULE-001 CVR | CVR 超时失权的真实案例 | L1 | L2 | 🟡 |
| VP-006 | All Mappings | 12.2 TCC MEI II 完整数据 | L1 | L2 | 🟡 |
| VP-007 | All Conflicts | Mitigation Strategy per conflict | L0 | L1 | 🟡 |

---

## Validation 层级分布

```
L0 (未验证):   3  (RULE-003, RULE-004, Conflict Mitigations)
L1 (条款/单实例): 2  (Acceptance, Cross-Domain theoretical)
L2 (跨合同/多实例): 3  (RULE-002 LD ×2, KP, Insurance)
L3 (全量):     0
L4 (反例):     0
──────────────────────────────
TOTAL:         8  validation records
```

# VALIDATION_ENGINE — 验证引擎 / Validation Engine
`[v0.3.5 · 不新增 Rule，验证现有 Rule 和 Mapping 的可信度 · Confidence 驱动]`

> **职责**：验证。拿每个 Mapping / Rule，用真实数据去跑，输出置信度——不是存在性检查，是一致性验证。
> **设计原则**：不发明新规则。只让现有规则更可信。

---

## 验证流程 / Validation Pipeline

```
Rule / Mapping
      │
      ▼
┌─────────────────────────────────────────────┐
│ 1. Clause Validation                        │
│    条款原文是否精确引用？是否已读全文而非摘要？      │
│    输出: Clause Confidence ████████░░        │
├─────────────────────────────────────────────┤
│ 2. Cross-Contract Validation                │
│    同一参数在 ≥2 份合同中是否一致/可解释差异？       │
│    输出: Cross-Contract Confidence          │
├─────────────────────────────────────────────┤
│ 3. Evidence Validation                      │
│    是否有真实文档支撑？（信函/证书/保函/发票）       │
│    输出: Evidence Confidence                │
├─────────────────────────────────────────────┤
│ 4. Issue Validation                         │
│    是否有真实商业事件检验过该 Rule/Mapping？       │
│    输出: Issue Confidence                   │
├─────────────────────────────────────────────┤
│ 5. Exception Discovery                      │
│    跑跨合同对比→发现不一致 → 是 Gap 还是 Exception？│
│    输出: Exception Flag + Confidence 调整     │
└─────────────────────────────────────────────┘
      │
      ▼
Overall Confidence Score (0–100%)
  → 🟢 ≥80%: 可被 Decision Engine 信任
  → 🟡 60–79%: 可推理，标注不确定性
  → 🔴 <60%: 仅供参考
```

---

## 当前验证结果 / Validation Results

### RULE-001 CVR Time-bar
```
Clause Validation       █████████░  95%  Art 24.4 全文已读
Cross-Contract          ██████░░░░  62%  12.1 5WD 已对照 · 10.1/10.2 COC 待提取
Evidence                █████░░░░░  52%  Issue #2 Notice 已读 · Notice 模板未提取
Issue Validation        ████░░░░░░  42%  1 个真实 Issue (MEI Delay LD Notice)
─────────────────────────────────────────
Overall: 63% 🟡 Adequate — Evidence + Cross-Contract 提升中
```

### RULE-002 LD Flow-down
```
Clause Validation       █████████░  98%  ANX5 A.09 全文 + FOA p.4-5
Cross-Contract          ████████░░  85%  3/4 分包 LD 全参数
Evidence                ████████░░  80%  2 个真实 Issue 触发 LD · LD_Mapping 完成
Issue Validation        ████████░░  78%  Issue #2 MEI Delay · Issue #1 KP-LD (叠加)
─────────────────────────────────────────
Overall: 85% 🟢 Healthy
```

### RULE-003 Warranty Gap
```
Clause Validation       ████████░░  82%  FOA p.5 + Art 17 框架 · Art 16 待读
Cross-Contract          ████████░░  82%  3/4 分包 Warranty 全参数
Evidence                █████░░░░░  45%  无 Warranty Claim 信函
Issue Validation        ███░░░░░░░  30%  无真实 Warranty 事件
─────────────────────────────────────────
Overall: 60% 🟡 Adequate — Issue Validation 缺口最大
```

### RULE-004 Payment Precondition
```
Clause Validation       █████████░  92%  Art 23/30 全文已读
Cross-Contract          ████████░░  80%  3/4 分包 Payment 全参数
Evidence                █████░░░░░  48%  ANX8 格式未精读 · 无 IPC 记录
Issue Validation        ███░░░░░░░  25%  无真实 Payment 事件
─────────────────────────────────────────
Overall: 61% 🟡 Adequate
```

---

## 验证得分汇总 / Validation Scorecard

| Rule/Mapping | Clause | Cross-Contract | Evidence | Issue | **Overall** |
|---|---|---|---|---|---|
| RULE-001 CVR | 95% | 62% | 52% | 42% | **63% 🟡** |
| RULE-002 LD | 98% | 85% | 80% | 78% | **85% 🟢** |
| RULE-003 Warranty | 82% | 82% | 45% | 30% | **60% 🟡** |
| RULE-004 Payment | 92% | 80% | 48% | 25% | **61% 🟡** |

---

## Exception Discovery Log
> 每次跨合同对比发现不一致 → 判定 Gap vs Exception → 标注

| 发现 | Rule | 涉及 | 判定 | 处理 |
|---|---|---|---|---|
| 10.1/10.2 LD Notice 是扣款前提 | RULE-002 | Civil COC | **Exception**（非 Gap——只是操作差异） | 标注在 LD_Mapping |
| 12.1 MC Relief 退还前期 LD | RULE-002 | 12.1 SCS | **Exception**（独有条款，对 Wison 有利） | 标注在 LD_Mapping |
| 12.1 预付款分 2 期 | RULE-004 | 12.1 | **Inverse**（比 EPC 对 Wison 更有利） | 标注在 Payment_Mapping |
| Civil PBG 至 WC+30d vs EPC FA+Warranty+45d | RULE-003 | 10.1/10.2 | **Partial Gap**（保函空窗期） | 标注在 Warranty_Mapping |
| 分包 Var Notice 5 WD vs EPC CVR 14 cal | RULE-001 | 12.1 | **Inverse**（有利——早获信息） | 标注在 Notice_Mapping |

---

## v0.3.5 目标 / Gate
- [ ] 所有 4 条 Active Rule 达 Overall ≥ 60%（当前 4/4 ✅，最低 RULE-003=60%）
- [ ] 所有现有 Mapping ≥ 2 条达 🟢 Healthy（当前 2/5 🟢：LD + Payment）
- [ ] Confidence Debt 从 5 条降至 ≤3 条
- [ ] Exception Discovery 记录 ≥ 8 条（当前 5 条）

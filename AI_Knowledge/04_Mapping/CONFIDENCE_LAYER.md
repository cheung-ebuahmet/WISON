# CONFIDENCE_LAYER — 可信度框架 / Confidence Layer
`[v0.3.5 · 所有 Mapping 均带三层元属性 · 回答"这个结论有多可靠"]`

> **以后系统能力的瓶颈不是推理，而是 Mapping Confidence。** 任何结论（Covered / Gap / Inverse / Extension / Conflict / Unknown）都必须回答一个元问题：**我有多确定？**
>
> 三层元属性 = 系统的自我审计机制。不是增加功能——是增加**质量维度**。

---

## 三层元属性 / Three Meta-Properties

### 1. Coverage（覆盖率 — 广度）
> "这个商业主题里，我们覆盖了多大比例的关键维度？"

| 维度 | 度量方式 |
|---|---|
| 合同覆盖 | 几份合同有此域的数据？（EPC + 4 Subcon = 5 contracts max） |
| 参数覆盖 | 该域关键参数中已提取/映射的比例 |
| 子域覆盖 | 该域的子维度中已覆盖的比例（如 Payment = Advance + IPC + Retention + Final） |

### 2. Confidence（可信度 — 深度）
> "每个已覆盖的维度，数据质量有多高？"

| 维度 | 度量方式 |
|---|---|
| Clause Mapping | 条款原文是否已读？引用是否精确？ ○→🟡→🟢 |
| Evidence Mapping | 是否有真实文档支撑（Corres/证书/保函/发票）？ |
| Runtime Mapping | 是否有真实 Run 过对应的 Rule 并产出结果？ |
| Issue Validation | 是否有真实商业事件验证过该结论？ |

**Confidence 不是"对错"——是"依据有多厚"。**

### 3. Validation（验证度 — 可信度）
> "这个结论是否经过真实项目事件或跨合同实例验证？"

| 层级 | 含义 |
|---|---|
| **Level 0** — 未验证 | 仅从合同文本推导，未经任何实例检验 |
| **Level 1** — 单实例验证 | 至少 1 个真实事件/函件/Issue 与此结论一致 |
| **Level 2** — 跨合同验证 | 结论在 ≥2 份不同合同中一致成立 |
| **Level 3** — 全量验证 | 全部合同 + ≥3 个真实事件一致确认 |
| **Level 4** — 反例测试 | 已主动寻找反例但未找到（负例验证） |

---

## 当前映射可信度矩阵 / Mapping Confidence Matrix

| 映射 | Coverage | Confidence | Validation | 评级 |
|---|---|---|---|---|
| **LD** | 93% █████████░ | 92% █████████░ | 85% L2 跨合同 | 🟢 |
| **Payment** | 88% ████████░░ | 85% ████████░░ | 55% L1 单实例 | 🟢 |
| **Warranty** | 85% ████████░░ | 78% ████████░░ | 45% L1 部分 | 🟡 |
| **Notice** | 75% ███████░░░ | 68% ██████░░░░ | 42% L1 部分 | 🟡 |
| **KP** | 72% ███████░░░ | 62% ██████░░░░ | 70% L2 跨合同 | 🟡 |

---

## 映射评级 / Mapping Health Grade

| Grade | Coverage + Confidence | 含义 |
|---|---|---|
| 🟢 Healthy | ≥80% / ≥80% | 已可被 Decision Engine 信任 |
| 🟡 Adequate | ≥65% / ≥60% | 可推理，但需标注不确定性 |
| 🔴 Weak | <65% / <60% | 结论仅供参考，不可作为决策依据 |

---

## Confidence 负债 / Confidence Debt
> 每项元属性缺口 = 一类新债务。区别于 Capability Debt（能力债）——这是 Confidence Debt（可信度债）。

| Debt ID | 映射 | 缺口维度 | 影响 | 偿还途径 |
|---|---|---|---|---|
| CF-001 | Notice | Issue Validation 42% | 无法验证"14d vs 5WD"在实际信函中的运作方式 | 结构化剩余 12 封函件 |
| CF-002 | Warranty | Validation 45% | 无 Warranty Claim 事件来验证 PBG 空窗期风险 | 等待/搜索 Warranty 相关信函 |
| CF-003 | KP | Coverage 72% | 12.1/12.2 KP 名单缺失→无法评估 MEI 合同人员违约敞口 | 提取 12.1/12.2 Exh E KP 名单 |
| CF-004 | Payment | Validation 55% | 无实际 IPC 数据验证付款周期 | 提取 IPC 记录 |
| CF-005 | Insurance | Coverage <20% | 整个域接近空白 | 制造 Art 41/ANX7 |

---

## Confidence 增长原则
- **不是补文档 → Confidence 上升**。是补**证据**和**验证**。
- 每完成一次 Issue→Decision 闭环 → 对应映射的 Validation 上升。
- 每提取一份跨合同参数 → Coverage 上升。
- 每精读一条原文条款并绑定 → Confidence 上升。

---

## 与 Capability Debt 的关系
- **Capability Debt** = 系统不能做什么（能力空白）
- **Confidence Debt** = 系统做到了，但有多可靠（可信度空白）
- 偿还一条 Capability Debt → 系统能做新的事
- 偿还一条 Confidence Debt → 系统更有底气做已经在做的事

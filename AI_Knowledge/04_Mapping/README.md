# 04_Mapping — Mapping Engine / 映射引擎
`[v0.3 · Canonical ⇄ Operational · 连接 AI_Knowledge 与 _Ref · 回答"是否一致、敞口在哪、该做什么"]`

> **这是整个系统的第三引擎。** `AI_Knowledge` 定义"应该如何判断"（Canonical）。`_Ref` 记录"项目实际发生了什么"（Operational）。**Mapping Engine 回答"两者是否一致、哪里存在商业敞口、应该采取什么行动"。**
>
> 每一份 Mapping 不是一个文档——是一个**可被 Rule Engine 执行的 Runtime Data 源**。当两端数据都存在时，Mapping 自动产生 Gap 判定。

---

## 架构 / Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 Commercial Intelligence Platform             │
│                                                             │
│  ┌──────────────────┐    ┌────────────┐    ┌─────────────┐ │
│  │  AI_Knowledge    │    │ 04_Mapping │    │    _Ref     │ │
│  │  (Canonical)     │◄──►│  (Bridge)  │◄──►│(Operational)│ │
│  │                  │    │            │    │             │ │
│  │  Philosophy      │    │ LD_Map     │    │ contracts/  │ │
│  │  DNA             │    │ Warranty   │    │ clause-lib/ │ │
│  │  Rule Engine     │    │ Payment    │    │ corres/     │ │
│  │  PROFILE         │    │ KP         │    │ timeline    │ │
│  └──────────────────┘    │ Notice     │    └─────────────┘ │
│                          │ Insurance  │                    │
│                          │ Acceptance │                    │
│                          └────────────┘                    │
│                                                             │
│  Mapping Engine 输出 → Gap → Risk → Action → Rule Runtime  │
└─────────────────────────────────────────────────────────────┘
```

---

## 映射域 / Mapping Domains

| 映射 | 状态 | EPC 数据 | Subcon 数据 | 可执行 |
|---|---|---|---|---|
| **LD_Mapping** | 🟢 Active | ✅ 15里程碑 0.01167-0.03333%/天 Cap 10% | ✅ 10.1/10.2/12.1 全有 | ✅ |
| **Warranty_Mapping** | 🟢 Active | ✅ 12m from ETC/PAC | ✅ 12m + 差异条款 | ✅ |
| **Payment_Mapping** | 🟢 Active | ✅ 30d + Advance 10% | ✅ 45d + 差异条款 | ✅ |
| **KP_Mapping** | 🟢 Active | ✅ EPC 无 KP-LD | ✅ 10.1/10.2/12.1 全有 AED 10K | ✅ |
| Notice_Mapping | 🟡 Pending | ✅ CVR 14d | 🟡 12.1: 5WD | ◐ |
| Insurance_Mapping | ⚪ Pending | ⚪ Art 41/ANX7 未读 | ⚪ 分包 Insurance 未提取 | ❌ |
| Acceptance_Mapping | ⚪ Pending | ⚪ Art 15/17 未读 | ⚪ 分包 Completion 未提取 | ❌ |

---

## 映射字段规范 / Mapping Schema

每份映射遵守统一格式（详见 [`mapping_schema.md`](mapping_schema.md)）：

```yaml
domain:        # 商业域
canonical:     # EPC 主合同侧（来源：AI_Knowledge/PROFILE + COMMERCIAL_DNA）
operational:   # 分包合同侧（来源：_Ref/data/contracts/*.yaml）
  - contract:  # 具体分包合同
    value:     # 该合同的取值
    source:    # 出处
gap:           # 差异分析
  - type:      # Covered / Partial / Uncovered / Inverse（分包比主合同更严）
    delta:     # 差异量化
risk:          # HIGH / MEDIUM / LOW
action:        # 建议行动
rule_binding:  # 绑定的 Rule ID
```

---

## 与 Rule Engine 的关系 / Rule Runtime

Mapping 不替代 Rule——它为 Rule 提供 **Runtime Data**：

```
此前：RULE-002 (LD Flow-down)
  → "分包无 LD → Uncovered"
  → 但无法量化 Gap ——因为不知道分包 LD 具体数值

此后：RULE-002 + LD_Mapping
  → EPC: 0.01167%/day Cap 10% ｜10.1: 0.1%/day Cap 10%
  → Gap: 分包费率 8.6× 主合同最低档（对 Wison 有利：多收的 LD 覆盖管理成本）
  → Cap: 10% vs 10% → 对等 ✅
  → Risk: LOW —— Covered（分包 LD 条款 ≥ 主合同）
```

**这就是 Mapping Engine 的本质：把 Rule 从"能跑"变成"有数据可跑"。**

---

## 映射状态与债务偿还 / Debt Repayment

每完成一份 Mapping，自动偿还对应的 Capability Debt：

| Mapping | 偿还债务 |
|---|---|
| LD_Mapping | CD-003 (RULE-002 Data Gap) |
| Warranty_Mapping | CD-004 (RULE-003 Data Gap) |
| Payment_Mapping | CD-005 (RULE-004 Evidence Gap) |
| KP_Mapping | CD-008 (C1 Authority Data Gap — 人名+阈值) |

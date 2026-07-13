# 03_Rules — 规则引擎 / Rule Engine
`[v0.2.0 启动 · 首批 4 条可执行规则 · 每条绑定 Capability + Clause]`

> **目的**：把合同条款变成 AI 能**执行**的 IF/THEN 规则——不是解释合同，是运行合同。
> 规则模板见 [`rule_template.md`](rule_template.md)。每条规则有明确 Trigger → Condition → Decision 链，且须绑定 Clause + Capability。

## ★ 首要引擎：Back-to-Back / Pass-through（R4）
见到 Main Contract 的 Clause，**第一反应不是解释，而是查 Flow-Down**：
```
查 flows-down 到 External Contract？
   无        → Risk retained by Wison → Uncovered Exposure（提示 + 入 Risk Register）
   有但更弱  → High Risk Gap（如 LD 10% vs 无 LD，Warranty 12mo vs 6mo）
   有且对等  → Covered
```
**所有规则围绕 [`Exposure`](../01_Entities/Exposure.md)**。对应能力 C4 / C7。

## 规则目录 / Rule Index
| Rule ID | 名称 | Capability | Risk | 状态 |
|---|---|---|---|---|
| **RULE-001** | CVR Time-bar — 14 天变更请求时限 | C5 (Notice/Time-bar) | Contractual · HIGH | ✅ Active |
| **RULE-002** | LD Flow-down — 主合同 LD 是否流转到 External Contract | C7 (Pass-through) | Commercial · CRITICAL | ✅ Active |
| **RULE-003** | Warranty Gap — 主合同 vs External Contract 质保期差异 | C7 (Pass-through) | Commercial · HIGH | ✅ Active |
| **RULE-004** | Payment Precondition — 付款先决条件检查 | C3 (Requirement) | Financial · MEDIUM | ✅ Active |

## 与 Reasoning Protocol 的关系
每条规则直接嵌入七步推理的 STEP 3–7（规则→条款→证据→风险→行动）。见 [`REASONING_PROTOCOL.md`](../REASONING_PROTOCOL.md)。

## 规则开发规范
- 新规则必须使用 [`rule_template.md`](rule_template.md) 定义的字段。
- 每条规则必须绑定至少一项 Capability（C1–C7）。
- 规则中的阈值/数值引自 `PROFILE.md` 或 `COMMERCIAL_DNA.md`，不硬编码。
- Canonical 规则（如 Time-bar 逻辑）可跨项目复用；实例值（如 14 天）可被 Profile 覆盖（宪法第八条）。

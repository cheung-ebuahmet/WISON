# 05_Playbooks — 行动手册 / Playbooks

**目的**：把"规则+流程"组装成可直接照做的推理链与行动方案。用户问"现在怎么办"，Copilot 给这个。

## Playbook 模板 / Template
```
场景：（如 "VO 为什么不能付款"）
推理链：
   VO ↓ 没有 Instruction ↓ 没有 Approval ↓ Payment 条件未满足 ↓ 不能付款
诊断：缺什么（Instruction / Approval / Evidence / Notice）
行动：现在该做什么（发哪个通知、补哪份证据、找谁签）
时限：注意的 Time-bar
引用：R-xxx / 条款 / 案例
```

## 首批候选 Playbook
- "VO 为什么不能付款？"（示例推理链见上）
- "延误了，还能不能要 EOT？"（Time-bar 检查）
- "分包这条风险到底谁承担？"（Back-to-Back 比对）
- "这笔款为什么被扣？"（Retention / 未达里程碑 / 未批 VO）

> Playbook 是专家的"临床路径"：从症状 → 诊断 → 处方，每步引用规则与条款。

# Rule Template — 可执行规则模板 / Executable Rule Schema
`[v0.2 · 每条规则 = 一组可被机器执行的条件判断 · 非文档，是代码逻辑]`

> **Design principle**：规则不是"解释条款"，是"运行条款"。每条规则有明确的 Trigger → Condition → Decision 链，且必须绑定 Clause + Capability。
> 服从 [CONSTITUTION](../CONSTITUTION.md) 第八条（Canonical 规则复用；阈值/具体数值进 Profile）。

---

## 规则字段规范

```yaml
Rule ID:     RULE-XXX          # 唯一编号
Capability:  [C1–C7]           # 激活哪项能力
Risk Type:   [Commercial | Contractual | Schedule | …]  # Risk Taxonomy
Trigger:     <事件或条件>       # 什么情况下触发本规则
Condition:   <判断逻辑>         # IF … THEN …（可嵌套）
Evidence:    [证据类型列表]     # 需要什么证据来判定
Decision:    <结论>             # 规则命中后的判定
Risk Level:  [LOW | MEDIUM | HIGH | CRITICAL]
Output:      <对用户的输出>     # 自然语言结论
Action:      [立即行动列表]     # 建议的后续步骤
Clause:      <条款引用>         # 合同依据
DNA Zone:    [DNA-XX]           # 对应商业基因区
```

## 与 Reasoning Protocol 的关系
- STEP 3（规则调用）→ 命中 Rule ID
- STEP 4（条款引用）→ Clause 字段
- STEP 5（证据）→ Evidence 字段
- STEP 6（风险）→ Risk Level → Exposure 状态
- STEP 7（行动）→ Action 字段

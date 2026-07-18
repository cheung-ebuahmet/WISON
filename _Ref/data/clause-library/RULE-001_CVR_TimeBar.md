# RULE-001 — CVR Time-bar
`[v0.2 首批规则 · Capability C5 · Risk: Contractual · HIGH]`

```yaml
Rule ID:     RULE-001
Name:        CVR Time-bar — 承包商变更请求 14 天时限
Capability:  C5 (分析 Event 是否触发 Notice / Time-bar)
Risk Type:   Contractual
Trigger:     承包商收到 Company 指令 或 知悉 Art 24.4(a) 所列开发事件
             (包括 Art 4.4(c), 5.2(a), 7.9(e), 8.4, 11.10(b), 11.11(b),
              12.10, 13.4, 21.12, 23.7(c), 29.1, 33.2(c), 34.1, 34.3)
Condition:
  IF (当前日期 - 触发日期) > 14 DAYS
  AND CONTRACTOR VARIATION REQUEST 未在 14 DAYS 内发出
  THEN → Time-bar 触发
Decision:   Entitlement Lost
            — 该指令/事件不构成 VARIATION
            — 承包商无权主张任何 Agreement Price 调整、KEY MILESTONE DATES 调整或其他救济
Evidence:
  - 原始指令（书面/邮件/会议纪要）
  - 指令接收日期证明
  - CVR 发出日期记录（如有）
  - 现场执行记录（证明已照做——Comply）
Risk Level: HIGH
Output:     "承包商未在收到指令/知悉事件后 14 天内发出 CONTRACTOR VARIATION REQUEST。
            依据 Art 24.4(a)(b)，该额外工作不构成 Variation，承包商丧失调价/调期及一切其他救济权利。
            已执行的工作不得计价。"
Action:
  1. [立即] 确认是否确已逾限——如有证据表明在 14 天内发出过任何书面通知，立即归档
  2. [立即] 评估已执行工作的成本敞口（Uncovered Cost Exposure）
  3. [本周] 审查现场流程：为什么 CVR 没有在时限内发出？修正流程防止重复
  4. [监控] 同类指令是否已建立"收到即判、当日发 Notice"的机制
Clause:      GTC Art 24.4(a)(b) · SC item 10
DNA Zone:    DNA-11 (Variation Logic) · DNA-12 (Notice / Time-bar)
```

---

## 商业背景 / Why this rule matters
这是整个 ADNOC LSTK 合同里最危险的一条时限。14 天不是"建议"——逾期即丧失权利，且 Art 24.7 有大量排除情形（合规指令、自身违约整改、设计修正……均不构成 Variation）。现场最常见的失败模式：工程师照做了指令，但没有同步发 CVR，14 天后才发现——做了也白做。

**口诀**：Comply first（执行零延误），Claim fast（CVR 当日发）。执行效力与商业效力解耦——这正是 Commercial Principle P4。

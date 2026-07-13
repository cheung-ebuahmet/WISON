# FAILURE_PATTERN_ENGINE — 失败模式引擎 / Failure Pattern Engine
`[v0.3.6 · 从"避免什么"学到的商业智慧 · Decision Engine 的反例训练集]`

> **优秀 Commercial Manager 不是靠成功案例成长的，是靠"避免过去犯过的错误"。**
> 每个 Failure Pattern = 一个可执行的反例：原因 → 结果 → 合同教训 → 预防措施 → DNA。
> 当新事件匹配已知 FP → Decision Engine 自动标注"警告：此情形曾导致 XX 失败"。

---

## 失败模式库 / Failure Pattern Library

### FP-001 · Notice Late — "等 cost impact 确认再发 Notice" 🟡

```
Pattern ID:     FP-001
Status:         🟡 Theoretical (合同推导 + 行业通用 · 本项目尚无已确认案例)
Domain:         Variation / Notice
Severity:       CRITICAL — 一旦触发 = 权利永久丧失

Scenario:
  Contractor 收到现场指令
  → Commercial team 认为："不确定 cost impact，不能发 Notice"
  → 等待 cost 确定后再发 CVR
  → 已超 14 DAYS (Art 24.4)

Consequence:
  Entitlement Lost — 已执行工作不得计价
  无 AGREEMENT PRICE 调整 + 无 KEY MILESTONE DATES 调整 + 无任何救济

Root Cause:
  "Notice = 承诺金额" 的误解。
  CVR 14 天起算点是"收到指令/知悉事件"，不是"cost impact 算清楚"。

Prevention:
  1. 收到指令 → 当天判定是否构成 Variation
  2. 如果"可能构成" → 当天发 CVR（标注"cost impact 待评估"）
  3. 14 天内补全 cost detail
  4. 口诀："Notice first, quantify later."

DNA Candidate:     YES — DNA-11 (Variation Logic) · DNA-12 (Notice/Time-bar)
Principle:         P4 (Operational ≠ Commercial) · P6 (Evidence is continuous)
Related Rule:      RULE-001 (CVR Time-bar)
Related Conflict:  N/A
```

### FP-002 · Subcontract LD Gap — "以为复制了条款就够了" 🟢

```
Pattern ID:     FP-002
Status:         🟢 Validated (本项目 LD_Mapping 已验证 3/4 分包 Covered)
Domain:         LD / Back-to-Back
Severity:       HIGH — Gap 可能持续整个项目周期才被发现

Scenario:
  Contract Manager 签分包时复制了主合同 LD 条款
  → 但未验证：(a) 费率是否对等 (b) Cap 是否对等 (c) 触发事件是否对齐 (d) 特殊条款(MC Relief)
  → 分包 LD < 主合同 LD → Wison 自留差额
  → 或分包 LD 包含主合同没有的退还机制 → 反向敞口

Consequence:
  分包延误 → Wison 向 ADNOC 赔 LD（主合同 10% Agg）
  → 但无法从分包全额追偿 → Uncovered LD Exposure

Root Cause:
  "Back-to-Back = 文字匹配" 的误解。
  真正的 Back-to-Back 是三参数匹配：费率 + Cap + 触发条件。

Prevention:
  1. 签分包前运行 RULE-002 (LD Flow-down)
  2. 三参数逐一比对：费率(‰)、Cap(%)、触发里程碑
  3. 特殊条款（MC Relief / 单里程碑 Cap）逐项评估
  4. Gap → 入 Risk Register + 指定 Owner

DNA Candidate:     YES — DNA-6 (LD Logic) · DNA B (Art 20 B2B)
Principle:         P2 (Check upstream) · P5 (Own what you cannot flow down)
Related Rule:      RULE-002 (LD Flow-down)
Related Conflict:  CF-AC-005 (LD refund asymmetry)
```

### FP-003 · Warranty Timing Gap — "分包 Warranty 起算点 ≠ 主合同" 🔴 NEW

```
Pattern ID:     FP-003
Status:         🟡 Theoretical (CF-AC-001 理论识别 · 未经真实 Warranty Claim 验证)
Domain:         Warranty / Acceptance
Severity:       HIGH — 时间差敞口可能持续数年不被发现

Scenario:
  Civil 分包 Warranty 从 Work Completion 起算（~Month 34）
  → EPC Warranty 从 PAC 起算（~Month 38）
  → 4 个月的 Warranty 时间差
  → Month 46-50 期间：EPC Warranty 仍有效，Civil Warranty 已过期
  → 此期间 Civil 工程出现缺陷 → Wison 对 ADNOC 承担修复，对 Civil 分包无追索权

Consequence:
  Wison 自费修复 Civil 缺陷（在 Civil Warranty 空窗期）
  金额取决于缺陷严重程度——单次可能数百万 AED

Root Cause:
  分包签合同时 Warranty 起算点未与主合同对齐。
  Civil 使用 "Work Completion" 为起算点（早），而非 "Provisional Acceptance"（与主合同对齐）。

Prevention:
  1. 签分包前运行 RULE-003 (Warranty Gap)
  2. 强制分包 Warranty 起算点 = PAC / Partial PAC / ETC（对齐主合同 FOA p.5）
  3. 或用保函覆盖 WC→PAC gap

DNA Candidate:     YES — DNA-10 (Warranty)
Principle:         P2 (Check upstream) · P5 (Own what you cannot flow down)
Related Rule:      RULE-003 (Warranty Gap)
Related Conflict:  CF-AC-001 (Warranty timing gap)
```

### FP-004 · PBG Expiry Gap — "分包保函早就死了，主合同保函还活着" 🔴 NEW

```
Pattern ID:     FP-004
Status:         🟡 Theoretical (CF-AC-004 理论识别 · 未经真实事件验证)
Domain:         Security / Acceptance
Severity:       HIGH — 结构性安全网缺口

Scenario:
  Civil 分包 PBG 到期 = Work Completion + 30 days (~Month 35)
  → EPC PBG 到期 = FA + last Warranty + 45 days (~Month 50+)
  → 约 2 年的保函空窗期
  → 空窗期内 Civil 分包违约 → Wison 对 ADNOC 的 PBG 可能被索偿
  → 但 Wison 无法从 Civil 分包追偿（保函已死）

Consequence:
  分包后期违约/缺陷 → Wison 的 EPC PBG 被 ADNOC 提取
  → Wison 无法 back-to-back 从分包 PBG 追偿 → 全额自担

Root Cause:
  分包 PBG 到期条件与主合同 PBG 到期条件不对齐。
  Civil 使用 "Work Completion + 30d"（极短），而非与 EPC FA + Warranty 对齐。

Prevention:
  1. 分包 PBG 到期条件必须对齐主合同：FA + last Warranty + 45d（至少 PA + Warranty + 45d）
  2. 或在 WC 后要求替代担保（如 Warranty Bond / 额外 Retention）
  3. 签分包前运行 Acceptance_Mapping 检查 PBG 到期对齐

DNA Candidate:     YES — DNA-8 (Security)
Principle:         P2 (Check upstream) · P5 (Own what you cannot flow down)
Related Rule:      RULE-003 (Warranty Gap — 扩展至 Security 维度)
Related Conflict:  CF-AC-004 (PBG expiry gap)
```

---

## Failure Pattern 统计 / FP Stats

| 指标 | 值 |
|---|---|
| Total Patterns | **4** |
| Validated (real event) | 1 (FP-002) |
| Theoretical (contract-derived) | 3 (FP-001/003/004) |
| CRITICAL severity | 1 (FP-001) |
| HIGH severity | 3 (FP-002/003/004) |
| DNA Candidates generated | 4 |
| Prevention rules | 4 |

---

## FP → 新事件匹配 / Matching Engine

当新 Decision Event 满足以下条件时，自动标注匹配的 FP：

```
IF Event.type IN FP.domain
   AND Event.clause_context ≈ FP.scenario
   AND FP.status != "retired"  (未被更正的失败模式)
THEN → 输出: "⚠ FP-XXX MATCH — 此情形曾导致 [consequence]。
             预防措施：[prevention]。"
```

**示例**：
> 新事件：12.1 Subcontractor 提交 CVR 在收到 Instruction 后 18 天
> → ⚠ **FP-001 MATCH** — Notice Late。
> CVR 14d 已超。Entitlement Lost per Art 24.4(b)。

---

## FP 退役机制 / Pattern Retirement

当以下条件满足时，FP 标记为 `retired`：
1. 已有 ≥3 个真实事件证明该模式在当前项目/合同版本中已不可能发生
2. 或合同条款已修改消除了该失败路径
3. 或建立了系统级防护（如自动 Notice 日历）

> 退役 ≠ 删除。退役的 FP 保留为历史教训——换项目/合同版本时重新激活。

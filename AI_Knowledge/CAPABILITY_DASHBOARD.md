# CAPABILITY_DASHBOARD — 能力驾驶舱 / Capability Dashboard
`[v0.2.2 · 活文档 · Gross − Debt = Net · 每次制造后更新 · 回答"系统什么时候真正变聪明"]`

> **这不是进度表。这是系统的智商计。** 每根进度条 = 这项商业能力的真实覆盖率（Gross）与扣除能力债后的可用能力（Net）。
> 驾驶舱数据直接驱动制造优先级（→ [`CAPABILITY_HEATMAP`](CAPABILITY_HEATMAP.md) + [`CAPABILITY_DEBT`](CAPABILITY_DEBT.md)）。
> 制造产出登记在 [`MANUFACTURING_LOG`](MANUFACTURING_LOG.md)。

---

## 总览 / Overview

```
Foundation      ██████████ 100%  CONSTITUTION + ONTOLOGY + Phase 2 Entities
Philosophy      ████████░░  75%  7 Principles ✅ · Mindset v0.1 (随用演化)
DNA             ████████░░  82%  17/21 区证据绑定
Rule Engine     ██████░░░░  55%  4 rules active · Template定型
Event Library   ██░░░░░░░░  18%  Event×State 概念已立 · 枚举+路由待建
Risk Taxonomy   ███░░░░░░░  25%  分类框架待建
Evidence Matrix ████░░░░░░  38%  概念存在于 Rules 中 · 统一矩阵待建
Decision Tree   █░░░░░░░░░   8%  Variation 路径已可推 · 形式化待建
Clause Deps     █░░░░░░░░░   5%  Art 20/24 链路已可查 · 全图待建
Gap Detector    ███░░░░░░░  30%  LD+Warranty 规则已可执行 · 自动比对待建
Playbook        █░░░░░░░░░   5%  行动建议散见于 Rules · 统一时间线待建
```

---

## 按商业域 / By Commercial Domain

```
Variation        ████████░░  82%  DNA🟢 + RULE-001 + Art 24 全文已读
Payment          ████████░░  80%  DNA🟢 + RULE-004 + Art 23/30 已读
LD / Delay       ████████░░  83%  DNA🟢 + RULE-002 + ANX5 A.09 全文
Warranty         ██████░░░░  63%  DNA🟢 + RULE-003 · 期限已定·细则待读
Security         ████████░░  80%  DNA🟢 · PBG/PCG/APG 已全·ANX8 格式待精读
Liability        ████████░░  85%  DNA🟢 · Cap 100% + Uncapped carve-outs 已全
Dispute          █████████░  90%  DNA🟢 · ICC/Abu Dhabi/English/3 arb 已全
Insurance        ████████░░  78%  DNA🟢 · Art 41+ANX7+5 subs 全读 · B2B 100% Covered
Quality          ██░░░░░░░░  17%  DNA⚪ · Art 13 未读 · ANX10 B.10 未读
HSE              ███░░░░░░░  30%  DNA🟡 · Art 21 框架已知 · 细则未读
Acceptance       ██████░░░░  62%  DNA🟢 · Art 15+17+ANX11 全读 · Event→Effect 链 · 5 跨域冲突
Testing          █░░░░░░░░░   5%  Art 16 Performance Tests 未读
Authority        ███░░░░░░░  30%  权限结构已立 · Profile 阈值得分包/现场数据
Sanctions/Export █████████░  92%  DNA🟢 · Art 51 + ANX14 · 定义全
```

---

## 按能力 / By Capability (Gross → Net)

| Cap | 名称 | Gross | Debt | Net | 规则化 |
|---|---|---|---|---|---|
| C1 | Authority | 60% | 低 (CD-008) | 55% | ❌ |
| C2 | Decision 有效性 | 65% | 低 | 60% | ❌ |
| C3 | Requirement | 50% | 中 (CD-006) | 40% | RULE-004 ✅ |
| C4 | B2B 完整性 | 70% | 高 (CD-009) | 45% | RULE-002/003 ✅ |
| C5 | Notice/Time-bar | 78% | 中 (CD-001/002) | 65% | RULE-001 ✅ |
| C6 | Claim 依据 | 55% | 中 (CD-007) | 45% | ❌ |
| C7 | Risk Pass-through | 75% | 高 (CD-003/004/009) | 40% | RULE-002/003 ✅ |

> **C7 的 Gross 75% vs Net 40% 差距最大**——规则已可执行，但缺分包数据供其运行。偿还 CD-003+CD-004+CD-009 是最高优先级。

---

## 未知缺口 / Top Unknowns（驱动优先级）
> 来自 Unknown Registry。按"解锁最多能力"排序。

| # | Unknown | 阻塞的能力 | 来源文件 | 优先级 |
|---|---|---|---|---|
| 1 | Insurance 险种/保额/免赔/Waiver of Subrogation | C3·C4·C7 | Art 41 · ANX7 | A |
| 2 | Acceptance 详细流程 (Art 15/17 + ANX11) | C2·C3·C6 | Art 15/17 · ANX11 | A |
| 3 | Quality 要求 (Art 13 + ANX10 B.10) | C3·C5 | Art 13 · ANX10 Exh B.10 | B |
| 4 | HSE 细则 (Art 21) | C3 | Art 21 | B |
| 5 | Variation Rates 费率表 (ANX5 A.07) | C3·C6 | ANX5 Exh A.07 | B |
| 6 | Performance Tests (Art 16 + ANX10 A.11) | C3·C6 | Art 16 · ANX10 Exh A.11 | C |
| 7 | 首份 External Contract 实体 | C4·C7 | 分包合同 | C |
| 8 | Claim 实体 + 规则 | C6 | Art 25 细节 + 实践 | C |

---

## 版本能力增量记录 / Capability Δ per version

| Version | Δ Capability |
|---|---|
| v0.1.0 | C1–C7 全验 PASS（Foundation：架构+DNA+证据绑定） |
| v0.2.0 | +Rule Engine（4 rules active）· +Reasoning Protocol（七步）· C5🟢 C7🟢 |
| v0.2.1 | +Supply Chain（Dashboard + 四问闸门 + Unknown Registry）——元能力 |
| v0.2.2 | +Manufacturing（Checklist + Heat Map + Debt Register + Mfg Log）——元元能力：制造可计量 |
| v0.2.3 | _next: Risk Taxonomy_ |
| v0.3.0 | _next: Obligation Matrix + Decision Tree_ |

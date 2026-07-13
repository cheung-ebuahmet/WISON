# DECISION_CORPUS_COVERAGE — 决策语料覆盖矩阵 / Decision Corpus Coverage Matrix
`[v0.3.6 · 驱动事件采集优先级 · 不是随机收集30个——是按商业生命周期全覆盖]`

> **30 个随机事件 ≠ Decision Engine 准备好了。** 30 个**覆盖全部商业类型**的事件 = Decision Engine 准备好了。
> 本矩阵定义 10 类事件的目标数量 + 当前进度 + 采集路径。
> 每新增一个结构化事件 → 回填 [`DECISION_CORPUS.md`](DECISION_CORPUS.md)。

---

## 覆盖矩阵 / Coverage Matrix

| # | 类型 | 目标 | 当前 | 进度 | 采集路径 | 优先级 |
|---|---|---|---|---|---|---|
| 1 | **Delay** | 5 | 1 (EVENT-001) | ██░░░░░░░░ 20% | 本项目 Milestone 逾期 · EOT 申请 · 分包延误通知 | 🔴 |
| 2 | **Payment** | 5 | 0 | ░░░░░░░░░░ 0% | IPC 争议 · 付款延迟 · 保留金释放 · 预付款回扣 | 🔴 |
| 3 | **Variation** | 5 | 0 | ░░░░░░░░░░ 0% | VO 指令 · CVR 提交 · Variation 被拒 · 计价争议 | 🔴 |
| 4 | **KP / Personnel** | 3 | 1 (EVENT-002) | ███░░░░░░░ 33% | PM/CM 缺位 · KP 替换 · KP-LD 扣款执行 | 🟡 |
| 5 | **Subcontract Default** | 4 | 0 | ░░░░░░░░░░ 0% | 分包未履约 · Termination 触发 · 保函兑付 | 🟡 |
| 6 | **Quality / Defect** | 3 | 0 | ░░░░░░░░░░ 0% | NCR 发出 · Punch List 争议 · Defect 修复成本 | 🟡 |
| 7 | **Acceptance / Handover** | 3 | 0 | ░░░░░░░░░░ 0% | MC 争议 · PAC 延迟 · ETC 触发 · Claims Release | 🟡 |
| 8 | **Insurance** | 2 | 0 | ░░░░░░░░░░ 0% | Claim 提交 · 保险拒赔 · Deductible 争议 | 🟢 |
| 9 | **Warranty** | 2 | 0 | ░░░░░░░░░░ 0% | Warranty Claim · DLP 期间缺陷 · 分包追偿 | 🟢 |
| 10 | **HSE / Force Majeure** | 3 | 0 | ░░░░░░░░░░ 0% | HSE 违规 · 停工令 · FM 通知 · FM 争议 | 🟢 |
| **TOTAL** | | **35** | **2** | █░░░░░░░░░ **6%** | | |

---

## 已覆盖 vs 缺口 / Coverage Gap

```
Delay            ██░░░░░░░░  20% (1/5)
KP/Personnel     ███░░░░░░░  33% (1/3)
Payment          ░░░░░░░░░░   0% ← CRITICAL GAP
Variation        ░░░░░░░░░░   0% ← CRITICAL GAP
Subcon Default   ░░░░░░░░░░   0% ← CRITICAL GAP
Quality/Defect   ░░░░░░░░░░   0%
Acceptance       ░░░░░░░░░░   0%
Insurance        ░░░░░░░░░░   0%
Warranty         ░░░░░░░░░░   0%
HSE/FM           ░░░░░░░░░░   0%
─────────────────────────────────
OVERALL          █░░░░░░░░░   6% (2/35)
```

---

## 优先采集策略 / Priority Collection Strategy

### 🔴 Tier 1 — 阻塞核心商业推理（先补这 3 类）

**Payment (0/5)**
- 为什么优先：付款是每天运行——45d vs 30d float 是每天在发生的现金流
- 采集目标：至少 1 个 IPC 争议 + 1 个保留金释放 + 1 个预付款回扣
- 来源：`Subcon_Payments/*/Pymt/` 目录 · 函件中的付款相关争议

**Variation (0/5)**
- 为什么优先：CVR 14d 是最高风险时限——没有真实 VO 案例 = Time-bar 验证永远是理论
- 采集目标：至少 1 个 CVR 成功 + 1 个 CVR 被拒 + 1 个 Variation 计价争议
- 来源：分包 Corres 目录 · 往来信函 · 未来项目 VO

**Subcontract Default (0/4)**
- 为什么优先：CF-AC-001/004（Warranty gap + PBG gap）只有在分包 default 时才暴露
- 采集目标：至少 1 个分包违约通知 + 1 个 Termination 威胁 + 1 个保函兑付
- 来源：当前项目活跃 Issue（07-16 截止日后可能产生）· 历史项目

### 🟡 Tier 2 — 深化已有能力

- Quality/Defect (0/3) · Acceptance (0/3) · KP (1→3)

### 🟢 Tier 3 — 低频高影响

- Insurance (0/2) · Warranty (0/2) · HSE/FM (0/3)

---

## v0.4 Gate 1 — Decision Corpus

| 条件 | 当前 | 目标 | 状态 |
|---|---|---|---|
| Total Events | 2 | ≥30 (或按覆盖：10 类型各 ≥ 目标 50%) | ❌ 6% |
| Delay | 1 | ≥3 | ❌ |
| Payment | 0 | ≥3 | ❌ |
| Variation | 0 | ≥3 | ❌ |
| Acceptance | 0 | ≥2 | ❌ |
| All other types | 1 | ≥1 each | ❌ |
| **Gate Status** | | | **CLOSED** |

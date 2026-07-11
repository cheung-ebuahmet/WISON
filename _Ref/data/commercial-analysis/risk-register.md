# Commercial Risk Register — RSGP 分包合同

> **视图层** — 自动汇总 Back-to-Back Gaps + Open Issues + Missing Data
> 数据来源: `data/contracts/*.yaml` + `commercial-analysis/back-to-back-matrix.md`
> 最后更新: 2026-07-09

---

## Risk Dashboard

| # | Risk | Severity | Contract | Category | Impact | Status |
|---|------|:---:|------|------|------|:---:|
| R1 | **EPC 主合同数据缺失** | 🔴 Critical | All | Back-to-Back | 无法评估 10 项商业 Gap 的敞口方向 | Open |
| R2 | **Delay LD 背靠背无法验证** | 🔴 Critical | All | LD | EPC LD 费率未知 → Wison 可能自留差额 | Open |
| R3 | **保留金释放不对称** | 🔴 High | 12.1 | Payment | PA+保函 vs Civil WC 直接释放 → 12.1 分包商现金流压力 | Monitoring |
| R4 | **12.1 预付款分期风险** | 🟡 Medium | 12.1 | Payment | 50% 锁在动员后 → 影响分包商前期现金流 | Monitoring |
| R5 | **Delay LD 金额未知** | 🟢 Resolved | All 3 | LD | 1‰/day confirmed — AED 150-162K/day | ✅ Closed |
| R6 | **12.1 性能 LD 存在** | 🟡 Medium | 12.1 | LD | MEI 合同独有 Performance LD，金额未提取 | Open |
| R7 | **管理系统 LD** | 🟡 Medium | 12.1 | LD | AED 10K/次，10.1/10.2 无此条款 | Accepted |
| R8 | **ICV 目标差异** | 🟡 Medium | 12.1 vs 10.1 | Payment | 60% vs 46% — 12.1 违约风险更高 | Monitoring |
| R9 | **保函存续期差异** | 🟡 Medium | 12.1 | Security | PA+45d after GP vs WC+30d — 12.1 保函更长 | Accepted |
| R10 | **PM 缺位 Material Breach** | 🔴 Active | 10.1 | Personnel | AED 10K/day since 6-24, deadline 7-16 | Active |
| R11 | **12.1 变更增额触发** | 🟢 Favorable | 12.1 | Variation | CO>10% vs CO>5% — 12.1 更宽松 | Accepted |

---

## By Contract

### 10.1 CCECC Civil II

| Risk | Severity | Detail |
|------|:---:|------|
| Delay LD back-to-back | 🔴 | EPC 缺失 |
| PM Absence | 🔴 | Active issue, deadline 2026-07-16 |
| Delay LD amount unknown | 🟢 | Resolved — AED 149,832/day |

### 10.2 TCC Civil I/III

| Risk | Severity | Detail |
|------|:---:|------|
| Delay LD back-to-back | 🔴 | EPC 缺失 |
| Delay LD amount unknown | 🟢 | Resolved — AED 162,120/day |

### 12.1 CCECC MEI I

| Risk | Severity | Detail |
|------|:---:|------|
| Delay LD back-to-back | 🔴 | EPC 缺失 |
| Retention mismatch | 🔴 | PA+保函 release |
| Performance LD | 🟡 | Amount unknown |
| Advance payment split | 🟡 | 50% post-mobilization |
| SM system LD | 🟡 | AED 10K/breach |
| ICV 60% | 🟡 | Higher than 10.1's 46% |
| Delay LD amount unknown | 🟢 | Resolved — AED 160,892/day |

---

## Status Summary

| Status | Count |
|:---:|:---:|
| 🔴 Critical | 2 (R1, R2) |
| 🔴 High | 1 (R3) |
| 🔴 Active | 1 (R10) |
| 🟡 Medium | 5 |
| 🟢 Resolved/Accepted | 3 |

> **最大两个风险 (R1, R2) 均源于 EPC 主合同数据缺失。** 填充 EPC YAML 是当前最高优先级行动。

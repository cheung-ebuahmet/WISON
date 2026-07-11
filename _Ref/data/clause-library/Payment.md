# Payment — 付款条款

> **Knowledge Object ID:** CL-PAY-001
> **商业优先级:** ⭐⭐⭐⭐⭐
> **最后更新:** 2026-07-09
> **数据来源:** `data/contracts/10.1-*.yaml`, `10.2-*.yaml`, `12.1-*.yaml`

---

## Summary

分包合同统一采用月度 IPC + 45 天付款周期。预付款 10% 须凭 APG + 履约保函申领。保留金 10% 从每期 IPC 中扣减。关键差异在保留金释放机制和预付款分期方式。

---

## Contract References

| 合同 | 合同形式 | 付款条款位置 | 保函条款位置 |
|------|---------|------------|------------|
| 10.1 CCECC Civil II | COC | Article 11, Attachment 6 | Article 15 |
| 10.2 TCC Civil I/III | COC | Article 11, Attachment 6 | Article 15 |
| 12.1 CCECC MEI I | SCS | Clause 19, Exh D | Clause 28 |
| EPC-ADNOC-RSGP | FIDIC Silver Book | *(待)* | *(待)* |

---

## Payment Mechanism

### 1. Advance Payment (预付款)

| 参数 | 10.1 CCECC | 10.2 TCC | 12.1 CCECC |
|------|:---:|:---:|:---:|
| 比例 | 10% | 10% | 10% |
| 分期 | 单次 | 单次 | **2 期** (50%+50%) |
| 条件 1 | APG + PB 提交 | APG + PB 提交 | APG + PB 提交 |
| 条件 2 | — | — | **动员完成**（第二期） |
| 发放时限 | 14 天 | 14 天 | **30 天** |
| 还款方式 | 每期 IPC 扣 10% | 每期 IPC 扣 10% | 每期 IPC 扣 10% |

> **商业差异:** 12.1 把 50% 预付款锁在动员之后 → 降低 Contractor 风险，但可能影响分包商早期现金流。

### 2. Interim Payment (中期付款)

| 参数 | 10.1 / 10.2 | 12.1 |
|------|:---:|:---:|
| 付款周期 | 45 天 | 45 天 |
| 起算点 | 收到正确发票 | 收到正确发票 |
| 发票截止 | — | 次月 5 日前 |
| 系统要求 | 可选 (SM system) | **强制 (SM system)** |
| 未用系统后果 | — | AED 10,000 / 次 LD |

### 3. Retention (保留金)

| 参数 | 10.1 / 10.2 | 12.1 |
|------|:---:|:---:|
| 扣减比例 | 10% | 10% |
| 额外质保金 | **+5%** (Warranty Bond) | — |
| 释放条件 | 100% at Work Completion | **Provisional Acceptance + bank guarantee** |
| 提前释放 | — | 0.5-1% (IFC 后 45 天提交 CDCE) |

> **⚠️ 商业风险:** 12.1 的保留金释放条件（Provisional Acceptance + 银行保函）比 Civil 合同（Work Completion 直接释放）对分包商更苛刻。分包商需额外提供保函才能拿回保留金。

### 4. Final Payment (最终付款)

| 参数 | 10.1 / 10.2 | 12.1 |
|------|:---:|:---:|
| 前提条件 | Work Completion + 缺陷修复 | Final Acceptance + release waiver |
| 外部审计 | ✅ (>AED 5M 须第三方审计) | ✅ (同) |
| 审计扣减率 >5% | 超额部分罚 5% | 超额部分罚 5% |

---

## Commercial Risk Points

| Risk | Level | Detail |
|------|:---:|------|
| 付款周期 Gap | 🟡 | 45天已锁定，但业主→Wison 的付款周期待确认 |
| 保留金释放不对称 | 🔴 | 12.1 须 PA + 保函才能释放 vs Civil 直接释放 |
| 预付款分期 | 🟡 | 12.1 第二期锁在动员后 → 影响分包商前期现金流 |
| 系统强制 | 🟡 | 12.1 未用 SM = AED 10K/次 LD |
| ICV 扣减 | 🟡 | 12.1 ICV 60% vs 10.1 ICV 46% — 12.1 更难达标 |
| 预付款未清 | 🔴 | 若 Work Completion 前未还清 → 余额立即到期 |
| 直接支付权 | 🔴 | 12.1 Clause 5.6: Contractor 可直接付款给 Sub-tier（分包商失控） |

---

## Cross-Contract Comparison

| Item | 10.1 Civil II | 10.2 Civil I/III | 12.1 MEI I |
|------|:---:|:---:|:---:|
| Advance % | 10% | 10% | 10% |
| Installments | 1 | 1 | **2** |
| Payment Days | 45 | 45 | 45 |
| Retention % | 10%+5% | 10%+5% | 10% |
| Retention Release | WC | WC | **PA+guarantee** |
| DLP | 12m | 12m | 12m |
| SM System LD | — | — | AED 10,000 |
| ICV Target | 46% | — | **60%** |

---

## Related

- **Clause Library:** [[Variation]] | [[Delay-LD]] | [[Performance-Security]]
- **Analysis:** [[back-to-back-matrix]]
- **Source YAML:** `10.1-CCECC-Civil-II.yaml`, `10.2-TCC-Civil-I-III.yaml`, `12.1-CCECC-MEI-I.yaml`
- **Source Contract:** COC Article 11, 15 / SCS Clause 19, 28

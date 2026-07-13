# CROSS_DOMAIN_CONFLICT_ENGINE — 跨域冲突引擎 / Cross-Domain Conflict Engine
`[v0.3.4 · 五域联动检查 · 回答"五个领域之间有没有互相打架" · 首次启用]`

> **本引擎是 v0.3.x 系列的最高价值产物。** 不是新增一个域——而是检查已有五域（LD · Payment · Warranty · Insurance · Acceptance）在事件时间线上是否存在**互相矛盾或互相制造的敞口**。
>
> 这不是 Contract Review。这是 **Commercial System Integration Test**。

---

## 冲突检测框架 / Conflict Detection Framework

```
DOMAIN A          DOMAIN B          冲突？
  │                  │                │
  ▼                  ▼                ▼
Acceptance  ←→  Warranty      Warranty 起算点是否一致？
Acceptance  ←→  Insurance     Insurance 到期 vs Acceptance 触发时间？
Acceptance  ←→  Payment       Milestone Payment vs PAC 先决条件冲突？
Acceptance  ←→  LD            EPC LD Refund vs Subcon MC Relief 反向敞口？
Acceptance  ←→  Security      PBG 到期 vs FAC 时间差？
Warranty    ←→  Insurance     Defect 风险 vs 保险覆盖窗口？
Warranty    ←→  Security      Warranty 期 vs PBG 有效期？
Payment     ←→  Acceptance    IPC 付款条件 vs PAC/FA 证书 blocker？
Insurance   ←→  Security      Insurance Declaration vs PBG reduction 联动？
```

---

## 已发现的冲突清单 / Conflict Register

### CF-AC-001 · Warranty Timing Gap · 🔴 HIGH

```
EPC:          Warranty starts at PAC (Month 38). Ends Month 50.
Civil Sub:    Warranty starts at Work Completion (Month ~34). Ends Month ~46.
MEI Sub:      Warranty starts at Provisional Acceptance. Closer to EPC PAC.

CONFLICT:     Civil warranty runs ~4 months ahead of EPC warranty.
              Months 46-50: EPC warranty active, Civil warranty expired.
              If Civil defect discovered in Months 46-50 → Wison repairs for ADNOC,
              but cannot recover from Civil subcontractor.

GAP SIZE:     ~4 months of uncovered EPC warranty for Civil scopes.
RISK:         HIGH — uninsurable, unbonded, no subcon recourse.
DOMAINS:      Acceptance ←→ Warranty
SUBSCON:      10.1 · 10.2 (Civil) — MEI contracts (12.1/12.2) less affected.
```

### CF-AC-002 · Insurance Window Gap · 🟡 MEDIUM

```
EPC:          CAR (Construction All Risks) expires at PAC.
Civil Sub:    Work Completion at Month ~34.
              → Civil insurance requirements may already be winding down
              → But EPC construction is still ongoing until PAC (Month 38)

CONFLICT:     Between WC and PAC, Civil construction may already be demobilizing,
              and their insurance (Equipment AR · TPL · WC) may lapse.
              Wison's CAR (via ADNOC) still covers — but if subcon lapses
              their own policies → Wison bears deductible for CAR claims.

DOMAINS:      Acceptance ←→ Insurance
```

### CF-AC-003 · Payment Timing Float · 🟡 MEDIUM

```
EPC:          Monthly IPC · Advance 10% · 30-day payment.
              LD deducted at PAC if milestones missed (Art 18.4(f): refund if PAC on time).
Civil Sub:    45-day payment on WC-linked milestones.
              Retention 100% released at WC.

CONFLICT:     Wison pays Civil 100% at WC (~Month 34) but receives final
              EPC milestone payment at PAC (Month 38). Wison is out-of-pocket
              for Civil payment ~4 months before ADNOC payment.

              + Civil retention fully released at WC. EPC has no retention
              mechanism (PBG substitutes). So Wison has no withheld funds
              from the Civil sub during the WC→PAC gap.

DOMAINS:      Acceptance ←→ Payment
```

### CF-AC-004 · PBG Expiry Gap · 🔴 HIGH

```
EPC:          PBG (10%) remains until FA + last Warranty + 45 days.
              PA → reduces to 50%. FA → returned.
              Timeline: PBG full until ~Month 38, then 50% until ~Month 50+.
Civil Sub:    PBG expires at WC + 30 DAYS (~Month 35).
              NO equivalent to EPC's post-PAC 50% PBG.

CONFLICT:     EPC PBG protects ADNOC for ~2+ years after Civil PBG has expired.
              If Civil defect found in Year 2 of EPC warranty → Wison has
              no bond to call from Civil subcontractor. All post-WC performance
              risk sits naked on Wison.

GAP SIZE:     ~2 years of zero subcon PBG coverage while EPC PBG still active.
RISK:         HIGH — structural gap in security architecture.
DOMAINS:      Acceptance ←→ Security
SUBSCON:      10.1 · 10.2 (Civil) — WC+30d PBG expiry
              12.1 (MEI) — PA+45d after last GP (better aligned)
```

### CF-AC-005 · LD Refund Asymmetry · 🟡 MEDIUM

```
EPC:          Art 18.4(f): Prior milestone Delay LD REFUNDED if PAC achieved
              by scheduled PAC date.
12.1 MEI:     MC Relief: if MC on schedule, prior Delay LD refunded.

CONFLICT:     If 12.1 MEI achieves MC on time → Wison refunds 12.1's LD.
              But Wison only gets its own LD refund from ADNOC if EPC PAC
              is on time. If EPC PAC is delayed (due to OTHER subcontractor
              or Wison's own issues), Wison paid 12.1 back but never got
              reimbursed by ADNOC.

              This is an asymmetric pass-through risk: 12.1 gets relief at MC,
              Wison gets relief at PAC — different trigger events.
              
GAP:          If MC on time but PAC late → Wison bears BOTH:
              ① Refund to 12.1 (contractual obligation)
              ② No refund from ADNOC (PAC condition not met)
RISK:         MEDIUM — depends on whether MC Relief can be contractually
              conditioned on EPC PAC timing (check 12.1 SCS wording).
DOMAINS:      Acceptance ←→ LD
```

---

## 冲突热力图 / Conflict Heat Map

```
Acceptance ←→ Warranty      🔴 HIGH    CF-AC-001
Acceptance ←→ Security      🔴 HIGH    CF-AC-004
Acceptance ←→ Insurance     🟡 MEDIUM  CF-AC-002
Acceptance ←→ Payment       🟡 MEDIUM  CF-AC-003
Acceptance ←→ LD            🟡 MEDIUM  CF-AC-005
Warranty   ←→ Insurance     🟢 LOW     (covered by CAR LEG 3)
Warranty   ←→ Security      🟢 LOW     (12.1 PBG aligned to Warranty)
Payment    ←→ Acceptance    🟡 MEDIUM  (Claims Release blocks payment)
Insurance  ←→ Security      🟢 LOW     (Insurance Declaration linked to PBG reduction)
```

---

## 冲突严重度汇总

| 等级 | 数量 | 敞口类型 |
|---|---|---|
| 🔴 HIGH | 2 | Warranty timing gap · PBG expiry gap |
| 🟡 MEDIUM | 3 | Insurance window · Payment float · LD refund asymmetry |
| 🟢 LOW | 3 | Covered by existing alignment |

---

## v0.3.4 门
- [x] 五域联动冲突检查——首次启用
- [x] 5 个真实冲突识别（含 clause 引用 + Gap 量化 + 涉及分包）
- [x] 冲突热力图 + 严重度分级
- [ ] 每个冲突的 Mitigation Strategy（v0.3.x 后续）
- [ ] CF-AC-001/004 的量化敞口模型（需 WC→PAC 实际时间差数据）

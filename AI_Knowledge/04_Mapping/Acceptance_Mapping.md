# Acceptance_Mapping — 验收与移交 主合同⇄分包映射
`[v0.3.3 · 🟡 Active · Handover Risk Transfer Engine — Stage 2 · Coverage: 68% · Confidence: 55%]`

> **Coverage 68%** ███████░░░ · **Confidence 55%** ██████░░░░ · **Validation 25%** ███░░░░░░░
> EPC Art 15+17+ANX11 全文 · 分包 3/4 合同验收/质保/保函数据已结构化
> 未验证：无真实 PAC/FAC 事件 · Punch List 实际流程 · ETC 实例

---

## Round 1 — Acceptance Event Model（事件→触发→证书→商业效果）

### EPC 侧事件链（ANX11 B.38.8.1 流程图 + Art 15-17 + ANX11D forms）

```
Event 1: MECHANICAL COMPLETION
  ├── Trigger: All construction + pre-commissioning done · Cat-A Punch List cleared · MC manual approved
  ├── Certificate: MC CERTIFICATE (ANX11D-1) — Company 15 days to issue/reject; 7-day follow-up → deemed
  ├── Responsible: Wison (CONTRACTOR)
  └── Commercial Effect: NONE — enables Commissioning only. No risk transfer, no LD change, no payment trigger.

Event 2: COMMISSIONING
  ├── Trigger: MC Certificate issued
  ├── Certificate: NONE (process stage)
  ├── Responsible: Wison (CONTRACTOR) — dynamic tests, operational tests, no feedstock yet
  └── Commercial Effect: NONE — enables RFSU

Event 3: READY FOR START-UP (RFSU)
  ├── Trigger: All commissioning done · utilities operational · SITE clean · ready for feedstock
  ├── Certificate: RFSU CERTIFICATE (ANX11D-2) OR PARTIAL RFSU (ANX11D-3) — Company 21 days
  ├── Responsible: Wison (CONTRACTOR)
  └── Commercial Effect:
       • Partial RFSU → LD rates reduced proportionally (Art 15.3(e)(ii))
       • Enables START-UP (Company-led)

Event 4: START-UP + PERFORMANCE TESTS
  ├── Trigger: RFSU Certificate issued → Company performs START-UP → Wison runs Performance Tests
  ├── Certificate: TEST RUN CERTIFICATE (ANX11 B.38.8.6)
  ├── Responsible: START-UP = Company · Performance Tests = Wison
  └── Commercial Effect:
       • ≤3 attempts allowed (2 retests) · if still fail after 6 months → Company may terminate OR accept with price reduction (Art 16.3)
       • Performance Guarantees in ANX11

Event 5: PROVISIONAL ACCEPTANCE (PAC)
  ├── Trigger: MC+Commissioning+START-UP+Performance Tests all done · Cat-C Punch List · Insurance Declaration
  ├── Certificate: PAC CERTIFICATE (ANX11D-5) OR PARTIAL PAC (ANX11D-4) — Company 21 days
  ├── CERTIFICATE BLOCKERS:
  │    • CLAIMS RELEASE LETTER (ANX11E) — without it: ① Company withholds post-PAC payments ② PBG NOT reduced to 50%
  │    • INSURANCE DECLARATION (ANX7-3)
  └── Commercial Effect (★ THE BIG ONE):
       ✅ WARRANTY PERIOD STARTS (12 months from PAC/Partial PAC/ETC)
       ✅ CARE/CUSTODY RISK TRANSFERS to Company (Art 33.2)
       ✅ PBG REDUCES TO 50% (Art 30.2(e))
       ✅ Prior Delay LD REFUNDED if PAC on schedule (Art 18.4(f))
       ✅ Insurance transition: construction→operational (Art 41.16(e))
       ⚠ CLAIMS RELEASE LETTER gates all of the above

Event 6: EARLY TAKING OVER (optional — Company discretion)
  ├── Trigger: Company elects to take over part/all WORKS before PAC
  ├── Certificate: TAKING OVER CERTIFICATE (ANX11D-7)
  └── Commercial Effect:
       • Warranty starts from ETC date for taken-over part
       • Care/custody transfers for taken-over part
       • Does NOT certify PAC — Contractor must still achieve PAC per schedule
       • Parts NOT taken over: Warranty NOT started, care NOT transferred — risk stays with Wison

Event 7: FINAL ACCEPTANCE (FAC)
  ├── Trigger: ALL 11 conditions met (Art 17.2(a)) — defects rectified · last Warranty expired · all payments discharged
  │              · docs delivered · title transferred · demobilization done · advance fully repaid
  │              · subcontractors paid · warranties assigned · outstanding manuals/docs provided
  ├── Certificate: FAC CERTIFICATE (ANX11D-6) — Company 30 days
  ├── CERTIFICATE BLOCKERS:
  │    • FINAL RELEASE LETTER (ANX11E) — without it: ① Company withholds post-FAC payments ② PBG NOT returned
  └── Commercial Effect:
       ✅ PBG RETURNED (45 days after FAC · Art 30.2(b))
       ✅ APG called if advance not fully repaid (Art 30.1(h))
       ✅ Last Warranty Period expires
       ✅ Final release of all claims against Company (except post-FAC Company breaches)
```

### 分包侧事件映射

| EPC Event | 10.1 Civil II (CCECC) | 10.2 Civil I/III (TCC) | 12.1 MEI I (CCECC) | 12.2 MEI II (TCC) |
|---|---|---|---|---|
| **MC** | Exists in scope | Exists in scope | Explicit MC Certificate · MC Relief = LD refund | Exh G MC defined |
| **PAC equivalent** | **"Work Completion"** (earlier than EPC PAC) | **"Work Completion"** | **"Provisional Acceptance"** (aligns with EPC) | **"Provisional Acceptance"** (aligns) |
| **Warranty start** | Work Completion (inferred) | Work Completion (inferred) | **Provisional Acceptance** | **Provisional Acceptance** (inferred) |
| **FAC equivalent** | NONE (WC = everything) | NONE | NONE (PA = final acceptance for subcon purposes) | NONE |
| **Release Letter** | NONE | NONE | Required (inferred from SCS) | Required (inferred) |
| **Source** | 10.1 YAML · COC | 10.2 YAML · COC | 12.1 YAML · SCS Clause 27 · Exh G | Exh G · SCS |

## Round 2 — Commercial Effect Chain / 商业效果贯穿

```
                    EPC               10.1 Civil         12.1 MEI          GAP
                    ───               ─────────         ────────          ───
MC                  no effect         no effect          MC Relief         MEI 独有 LD 退
                                                        (LD refund)
                                                       
Commissioning       no effect         N/A (civil)        N/A (subcon)
                                                       
RFSU                LD rate ↓         N/A                N/A               Civil 无 RFSU 概念
                    (Partial)
                                                       
PAC                 ★ All triggers:   WC triggers        PA triggers       ⚠ Civil WC ≠ EPC PAC
                    Warranty starts   Warranty starts    Warranty starts   Civil warranty starts
                    PBG→50%           Retention 100%     Retention at      MONTHS before EPC
                    Care→Company      release            PA+guarantee      warranty. Gap = WC→PAC.
                    LD refund                          PBG→PA+45d after GP
                    Insurance trans.
                    Claims Release
                                                       
FAC                 11 conditions     NONE               NONE              ⚠ Subcons have no FAC
                    PBG returned      PBG expired at     PBG expired at    equivalent. Civil PBG
                    Final Release     WC+30d ← GAP       PA+45d after GP   dead long before EPC.
```

## Round 3 — Acceptance Timing Gap / 时间差敞口

```
                     EMPLOYER (ADNOC)                    CIVIL SUBCONTRACTOR
                     ─────────────────                   ──────────────────
Month 27-34          Construction                        Construction
Month 27             12.1 Sub Station MC milestone
Month 31             10.1 Linear Storage building
Month 32             12.1 Stacker/Reclaimer MC
Month 34             RFC (Ready For Commissioning)       
                     ─── CIVIL WORK COMPLETION ───       ★ RETENTION 100% RELEASED
                                                        ★ PBG EXPIRES (WC+30d)
                                                        ★ WARRANTY STARTS (12mo)
                                                        ★ APG EXPIRES (WC+30d)
                     ≈ Month 36-38?                     
Month 35             RFSU                                
Month 38             PAC (scheduled)                     ← Civil warranty already running ~4 months
                     ★ EPC WARRANTY STARTS (12mo)        ← Civil PBG already dead ~4 months
                     ★ PBG→50%                           
Month 38+12 = 50     EPC WARRANTY ENDS                   ← Civil warranty ENDED at Month ~48
                                                        ← GAP: Month 48-50 = WISON BEARS DEFECT RISK
                                                       
Month 50+            FAC (variable)                      ← Civil everything expired long ago
                     ★ PBG RETURNED                      
                     ★ FINAL RELEASE
```

> **CRITICAL GAP**：Civil Work Completion 到 EPC PAC 之间有约 **4–8 个月**的时间差。期间：
> - Civil 分包 Warranty 已在运行甚至已过期
> - Civil 分包 PBG 已过期（WC+30d）
> - Civil 分包 Retention 已全额释放
> - **但 EPC 侧：Wison 对 ADNOC 的 Warranty 尚未开始，PBG 仍全额有效，Care/Custody 仍在 Wison。**
> - **如果这段时间 Civil 工程出现缺陷 → Wison 对 ADNOC 承担修复责任，但对 Civil 分包无追索权。**

## Round 4 — Cross-Domain Conflict Detection（五域冲突检查）

| 冲突 | 域1 | 域2 | 描述 | 风险 |
|---|---|---|---|---|
| **CF-AC-001** | Acceptance vs Warranty | Civil WC starts warranty → but EPC PAC starts months later → warranty timelines are offset, not aligned | **HIGH** |
| **CF-AC-002** | Acceptance vs Insurance | CAR expires at PAC (construction→operational). Gap between Civil WC and EPC PAC = construction still ongoing but Civil insurance may have lapsed. | **MEDIUM** |
| **CF-AC-003** | Acceptance vs Payment | EPC milestones tied to PAC (Month 38). Civil subcontractor paid at WC (Month ~34) — Wison is out-of-pocket 4+ months | **MEDIUM** |
| **CF-AC-004** | Acceptance vs Security | Civil PBG expires WC+30d. EPC PBG expires FA+last Warranty+45d. Gap = ~2+ years. If Civil defect found late → Wison has no bond to call. | **HIGH** |
| **CF-AC-005** | Acceptance vs LD | EPC LD reimbursed if PAC on time (Art 18.4(f)). 12.1 MC Relief also refunds LD. If 12.1 achieves MC on time but Wison fails EPC PAC → Wison gets LD back from 12.1 but still pays ADNOC. | **MEDIUM** |

## Round 5 — Risk Transfer Matrix

| Event | EPC Effect | Civil Sub Effect | MEI Sub Effect | Exposure | 闭环 |
|---|---|---|---|---|---|
| MC | Enables commissioning | Same | **LD refund (12.1 only)** | LOW — MC 无风险转移 | ✅ |
| RFSU | LD rate reduction | N/A | N/A | LOW | ✅ |
| PAC | Warranty starts · PBG→50% · Care transfer · Insurance transition · LD refund · Claims Release | WC 早已完成 | PA 启动 Warranty · Retention at PA+guarantee | **HIGH** — Civil WC→PAC gap | ⚠ |
| FAC | PBG returned · Final Release · Last warranty ends | 全部早已过期 | 全部早已过期 | **HIGH** — 分包保护全空窗 | ❌ |

## Confidence 分解

```
Clause Mapping      ████████░░  82%  Art 15+17+ANX11 全文 · 分包 3/4 合同验收/保函 YAML
Evidence Mapping    ███░░░░░░░  28%  证书格式(ANX11D-1~7·ANX11E·ANX7-3)已读 · 实际 MC/PAC/FAC 事件=0
Runtime Mapping     █████░░░░░  52%  Event→Effect 链可追踪 · 未在真实事件中验证
Issue Validation    ██░░░░░░░░  15%  无 PAC/FAC 事件 · 无 Warranty Claim
─────────────────────────────────
Overall Confidence  █████░░░░░  55%
```

## Actions

1. **[本周]** 确认 10.1/10.2 分包合同中对"Work Completion"的准确定义——是否与 MC/RFSU/PAC 有映射？
2. **[本周]** 提取 12.2 TCC MEI II 的验收条款（Exh G Mechanical Completion + SCS completion clauses）
3. **[PAC 前 6 个月]** 准备 Claims Release Letter + Insurance Declaration + Punch List Cat-C 清理
4. **[流程]** 建立 Acceptance Calendar：MC 预测日期 → Civil WC 日期 → 识别 WC→PAC Gap 时长
5. **[监控]** CF-AC-001 (Warranty 时间差) + CF-AC-004 (PBG 空窗期) — Civil 分包的两个最高敞口

## Debt Repaid
- [x] **CD-011 部分偿还** — DNA-15 Acceptance：Art 15+17+ANX11 已制造，事件链与商业效果已映射

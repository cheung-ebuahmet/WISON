# Warranty_Mapping — 质保期 主合同⇄分包映射
`[v0.3 首批映射 · 🟢 Active · Rule Runtime for RULE-003 · 偿还 CD-004]`

---

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 |
|---|---|---|
| Warranty Period | **12 months** from ETC / Partial PAC / PAC | FOA p.5 |
| Defects Liability | GTC Art 17 · Art 1 "DEFECT" | CONTRACT_MAP |
| PBG 到期 | FA + 最后 Warranty Period + 45 days | GTC Art 30.2(c) |
| 性能保证 | GTC Art 16 · ANX10 Exh A.11（待读） | CONTRACT_MAP |
| 保修延长触发 | ⚪ 待读 Art 16/17 细节 | — |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| 缺陷责任期 (DLP) | **12 months** | **12 months** | **12 months** | ⚪ 待提取 |
| 质保期 (Warranty) | **12 months** | **12 months** | **12 months** | ⚪ |
| **维修延长** | **+18 months** ⚠️ | **+18 months** ⚠️ | **—** | ⚪ |
| 保函到期 | **WC + 30 days** (Par 1) | **WC + 30 days** (Par 1) | **PA + 45 days after last GP** (Par 2) | ⚪ |
| 额外质保金 | **5%** Warranty Bond | **5%** Warranty Bond | — | ⚪ |
| 来源 | `10.1-*.yaml` · COC · Attachment 6 | `10.2-*.yaml` · COC · Attachment 6 | `12.1-*.yaml` · SCS Clause 27 · Exh D | ⚪ |

**Par 1** = 主合同保函至 FA+Warranty+45d；分包保函仅至 WC+30d → **保函到期 Gap**。  
**Par 2** = 12.1 保函至 PA+45d after last GP → 与主合同 PBG 到期机制**更接近**（均绑定 PA/FA + GP）。

## Gap Analysis
| Gap | 涉及合同 | 类型 | 差异 | 风险 | 对 Wison 的影响 |
|---|---|---|---|---|---|
| **Warranty 期限** | 10.1/10.2/12.1 | **Covered ✅** | 12m = 12m | **LOW** | 🟢 对等——主合同与全部分包 Warranty 对齐 |
| **维修延长** | 10.1/10.2 | **Inverse ✅** | Civil 有 +18m 维修延长；EPC 无此额外机制 | **LOW** | 🟢 **有利**——分包商在 DLP 内维修后质保自动延长 18 月，Wison 获得比主合同更长的分包追索期 |
| **保函到期 Gap** | 10.1/10.2 | **Partial ⚠️** | 分包 PBG 至 WC+30d，EPC PBG 至 FA+最后 Warranty+45d → 时间差约 (FA−WC)+Warranty+15d | **MEDIUM** | 🟡 不利——WC 后至 FA 期间，若分包商违约，Wison 对 ADNOC 仍有保函责任但对分包商的保函已过期。差额 = 无法追索的保函覆盖期 |
| **保函到期** | 12.1 | **Covered ✅** | PA+45d after GP ≈ EPC 机制 | **LOW** | 🟢 12.1 的 PBG 到期比 Civil 合理得多，与主合同对齐 |
| **额外质保金** | 10.1/10.2 | **Inverse ✅** | Civil 有 +5% Warranty Bond；EPC 无 | **LOW** | 🟢 有利——Civil 分包在 WC 后仍需维持额外 5% 质保金，为 Wison 提供额外保障 |

> **核心结论：Warranty 期限全覆盖。唯一值得关注的 Gap 是 Civil 合同的保函到期过早（WC+30d），WC 到 FA 之间的保函空窗期需靠其他手段管理。** 12.1 的 PBG 机制优于 Civil 合同。

## Rule Binding
| Rule ID | Runtime Status | 判定 | 备注 |
|---|---|---|---|
| **RULE-003** (Warranty Gap) | 🟢 **Runtime Ready** | **Covered**（期限对等）+ **Partial**（Civil PBG 到期 Gap） | 10.1/10.2 PBG 到期作为条件分支标注 |

## Actions
1. **[本周]** 确认 10.1/10.2 WC 预计日期与 EPC FA 预计日期的实际时间差 → 量化 PBG 空窗期
2. **[监控]** 若 WC 与 FA 时间差 > 6 个月 → 评估是否需要 Civil 分包商提供额外担保覆盖空窗期
3. **[流程]** 在 WC 后至 FA 期间，对 Civil 分包商的履约监控升级——因为此期间无法通过 PBG 追偿

## Debt Repaid
- [x] **CD-004** — RULE-003 Warranty Gap Data Gap：10.1/10.2/12.1 Warranty 参数已映射，RULE-003 现可产出量化判定

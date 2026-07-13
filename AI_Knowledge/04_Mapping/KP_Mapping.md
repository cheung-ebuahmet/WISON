# KP_Mapping — 关键人员 主合同⇄分包映射
`[v0.3 首批映射 · 🟢 Active · 偿还 CD-008 · 驱动 C1 Authority Data]`

> **特殊映射**：EPC 主合同**无 KP-LD 机制**（ADNOC 通过 PBG + 终止条款管理 Contractor 人员履约）。KP-LD 是 Wison 自行在分包合同中创设的**下行管控工具**——这是典型的 Contractor 商业智慧：从主合同学到的管理需求，转化为对下的合同条款，即使主合同本身没有要求。

---

## Canonical（EPC 主合同侧）
| 参数 | 取值 | 出处 |
|---|---|---|
| Key Personnel LD | **N/A** — EPC 无此机制 | 全文检索未见 |
| Contractor Representative | **Mr. Feng Guoling** (Project Manager) | FOA p.5 |
| Company Representative | **Mr. Jasem Al Hosani** (VP/A) | FOA p.5 |
| 人员变更控制 | GTC Art 19（KEY PERSONNEL 变更仅限辞职/产假/病假/死亡/解雇/政府禁止） | CONTRACT_MAP |
| 人员批准权 | Company 批准 Key Personnel | GTC Art 19 |

## Operational（分包合同侧）
| 参数 | 10.1 CCECC Civil II | 10.2 TCC Civil I/III | 12.1 CCECC MEI I | 12.2 TCC MEI II |
|---|---|---|---|---|
| KP-LD 机制 | **✅** Sub-Clause 4.2.4 | **✅** Sub-Clause 4.2.4 | **✅** SCS Clause 8 + Exh E | ⚪ 待提取 |
| KP 人数 | **7** | **7** | **7** | ⚪ |
| KP-LD /人/天 | **AED 10,000** | **AED 10,000** | **AED 10,000** | ⚪ |
| KP-LD 日上限 (7人) | AED 70,000/天 | AED 70,000/天 | AED 70,000/天 | ⚪ |
| KP-LD 上限 | **无上限**（不同于 Delay LD 10% Cap） | 同左 | 同左 | ⚪ |
| 触发 | 离岗/缺位/未替换 | 同左 | 同左 | ⚪ |
| 全职驻场义务 | ✅ Sub-Clause 4.3.6 | ✅ | ✅ | ⚪ |
| 违规=根本违约 | ✅ Sub-Clause 4.3.7 | ✅ | ✅ | ⚪ |
| **PM 名字** | **Zhiming Chen** | **Luo Jingbo** | ⚪ 待提取 | ⚪ |
| **Construction Mgr** | **Li Jianhu** | **Cao Fei** | ⚪ | ⚪ |
| **Control Mgr** | **Lawrence** | **Zhang Shi** | ⚪ | ⚪ |
| **Contract/Commer Mgr** | **Quzhao** | **Cheng Hui** | ⚪ | ⚪ |
| **HSE Mgr** | **Sajith N.G.** | **Sun Shuwen** | ⚪ | ⚪ |
| **Quality Mgr** | **Muhammad Khalid** | **Zhang Zhan** | ⚪ | ⚪ |
| **Procurement Mgr** | **Xue Xiaodong** | **Hu Zhongkui** | ⚪ | ⚪ |
| 来源 | `10.1-*.yaml` · Att 5 Appendix | `10.2-*.yaml` · Att 5 Appendix | `12.1-*.yaml` · Exh E Appendix | ⚪ |

## 带人名的 Authority 映射（C1 Data）
| Role | 10.1 CCECC | 10.2 TCC | 12.1 CCECC | Wison |
|---|---|---|---|---|
| Project Manager | **Zhiming Chen** ⚠️ absent since 5/25 | **Luo Jingbo** | ⚪ | **Feng Guoling** |
| Contract/Commercial Mgr | **Quzhao** | **Cheng Hui** | ⚪ | ⚪ |

> ⚠️ **Active Issue #1**：陈志明 (10.1 PM) 2026-05-25 离岗，6/24 假期届满未归 → KP-LD 自 6/24 起计 AED 10,000/天。SLT-5312-WSN-CCE-0020 整改截止日 **2026-07-16**。

## Gap Analysis
| Gap | 涉及合同 | 类型 | 差异 | 风险 | 对 Wison 的影响 |
|---|---|---|---|---|---|
| **KP-LD 存在性** | All | **Inverse ✅** | EPC 无 KP-LD；Subcon 有 AED 10K/人/天 | **LOW** | 🟢 **Wison 创设的下行管控**——主合同不要求，但 Wison 在分包中加入以管理分包商人员履约。纯收益 |
| **KP-LD 无上限** | All | **Inverse ⚠️** | Subcon KP-LD 无 Cap（非 Delay LD 10%），可无限累积 | **MEDIUM** | 🟢 有利（对 Wison）——但实际操作中分包商可能以"不合理惩罚"抗辩 |
| **Wison 自身 KP 风险** | EPC | **Not Comparable** | EPC 无 KP-LD，但 Art 19 限制人员变更 + Art 35.3 允许 Company 以违约为由终止 | **MEDIUM** | 🟡 Wison 自身也需管理 Key Personnel 稳定性——虽无 LD 但违规可至终止 |

## Rule Binding
| 规则 | Runtime Status | 说明 |
|---|---|---|
| C1 (Authority) | 🟢 **增强** | 关键人员名录（10.1/10.2）+ KP-LD 触发机制已映射 → C1 从 60%→可定位具体 Person |
| C3 (Requirement) | 🟡 增强 | KP 驻场义务 + 违规=根本违约 → Requirement 实例 |

## Active Issue Mapping
```
Issue #1: PM 缺位 (10.1 CCECC Civil II)
  ├── 人员: Zhiming Chen (PM), absent since 2026-05-25
  ├── 触发: Sub-Clause 4.3.3 + 4.3.7 + 4.2.4
  ├── LD: AED 10,000/day from 2026-06-24 (~AED 190K as of 2026-07-13)
  ├── 信函: SLT-5312-WSN-CCE-0020 (07-09), deadline 07-16
  └── 升级路径: KP-LD 持续扣款 → 暂停付款 → Termination (Article 21.2)
```

## Actions
1. **[07-16 截止]** 若 CCECC 未在截止日前提供合规替代 PM → 启动 KP-LD 从 IPC 扣款 + 升级通知（引用 Sub-Clause 4.3.7 Material Breach）
2. **[本周]** 补录 12.1/12.2 的 KP 名单到 YAML（MEI 合同 KP 数据当前缺）
3. **[流程]** 建立 KP 出勤月度检查——7 个职位 × 4 个分包 = 28 个检查点的 Dashboard

## Debt Repaid
- [x] **CD-008** — C1 Authority Data Gap：10.1/10.2 关键人员名录（含人名+LD 触发条件）已映射，C1 从概念层进入可操作层

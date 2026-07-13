# UNKNOWN_REGISTRY — 未知登记簿 / Unknown Registry
`[v0.3 基础设施 · 活文档 · 驱动 Knowledge Queue 优先级 · 每次供给后移除条目]`

> **目的**：系统化记录"我们知道自己不知道什么"。Unknown 越少，Capability 越高。
> 每一项 Unknown 必须标注：阻塞什么能力、答案在哪份文件、优先级。
> 与 [`KNOWLEDGE_SUPPLY_CHAIN.md`](KNOWLEDGE_SUPPLY_CHAIN.md) 和 [`CAPABILITY_DASHBOARD.md`](CAPABILITY_DASHBOARD.md) 联动。

---

## 开放未知 / Open Unknowns

### 商业核心缺口
| ID | Unknown | 阻塞能力 | 答案在 | 优先级 | 状态 |
|---|---|---|---|---|---|
| U-001 | Insurance：险种(CAR/TPL…)、保额、免赔额、Waiver of Subrogation、谁投保 | C3·C4·C7 | **Art 41 · ANX7** | 🔴 A | Open |
| U-002 | Acceptance：PA/FA 详细流程、Punch List、证书格式、Claims Release Letter 内容 | C2·C3·C6 | **Art 15/17 · ANX11** | 🔴 A | Open |
| U-003 | Quality：QRC/ITP 框架、NCR 关闭流程、Company 质量审核权限 | C3·C5 | **Art 13 · ANX10 B.10** | 🟡 B | Open |
| U-004 | HSE 细则：具体合规义务、违规后果层次（警告→暂停→终止） | C3 | **Art 21** | 🟡 B | Open |
| U-005 | Variation Rates：VO 计价的具体费率/overheads/profit 比例 | C3·C6 | **ANX5 Exh A.07** | 🟡 B | Open |
| U-006 | Performance Tests：性能保证参数、测试条件、未达标后果 | C3·C6 | **Art 16 · ANX10 A.11** | 🟢 C | Open |
| U-007 | Payment Milestones：付款里程碑的具体金额/比例 | C3 | **ANX4 Att-2** | 🟢 C | Open |
| U-008 | Subcontractor 批准程序细节（ANX10C 全文） | C4·C7 | **ANX10 Exh B.14/B.15/B.16** | 🟢 C | Open |
| U-009 | Completion Schedule 具体日期与逻辑 | C3 | **ANX4 Exh A.06** | 🟢 C | Open |
| U-010 | 首份 External Contract 实体内容 | C4·C7 | 分包合同 | 🟢 C | Open |

### 规则相关缺口
| ID | Unknown | 阻塞能力 | 答案在 | 优先级 |
|---|---|---|---|---|
| U-011 | Claim 实体建模：Detailed Claim 的合同要求结构 | C6 | Art 25 精读 + 实践 | 🟢 C |
| U-012 | EOT 的同期记录要求（Art 25.4 细节） | C5·C6 | Art 25 精读 | 🟢 C |
| U-013 | Force Majeure Notice 时限与证据要求 | C5 | Art 38/40 | 🟢 C |
| U-014 | Suspension 成本补偿的 ANX5 具体规定 | C3·C6 | ANX5 Exh A.07 | 🟢 C |
| U-015 | CONCURRENCY（并发延误）的实际判定规则 | C5·C6 | Art 1 定义 + 实践 | 🟢 C |

### 实践知识缺口（待专家访谈）
| ID | Unknown | 阻塞能力 | 答案在 | 优先级 |
|---|---|---|---|---|
| U-020 | ADNOC 在本项目最"较真"的条款是什么？ | Philosophy | 专家访谈 | 🟡 B |
| U-021 | 哪些"现场惯例"与合同白纸黑字不一致？ | P7（规范 vs 实践） | 专家访谈 | 🟡 B |
| U-022 | 承包商最常踩的 Time-bar 陷阱是哪个？ | C5 | 专家访谈 | 🟡 B |
| U-023 | Variation 被拒的最常见原因是什么？ | C3·C6 | 案例 + 访谈 | 🟢 C |
| U-024 | External Contract 实际 Back-to-Back 情况（Gap 多大？） | C4·C7 | 分包合同 + 访谈 | 🟡 B |

---

## 已消除未知 / Cleared Unknowns
| ID | Unknown | 消除方式 | 消除日期 | Version |
|---|---|---|---|---|
| U-001a | COMPANY 正式名 | FOA p.1 → ADNOC GAS OPERATIONS AND MARKETING – L.L.C. | 2026-07-13 | v0.1.0 |
| U-001b | CONTRACTOR 正式名 | FOA p.1 → Wison Energy Engineering (HK) Ltd – Abu Dhabi | 2026-07-13 | v0.1.0 |
| U-001c | 合同价格 | FOA p.5 → USD 686,205,286 | 2026-07-13 | v0.1.0 |
| U-001d | 预付款有无 | FOA p.5 → YES 10% (≠ 00_PROJECT_CONTEXT 零预付) | 2026-07-13 | v0.1.0 |
| U-001e | PBG 比例 | FOA p.5 → 10% | 2026-07-13 | v0.1.0 |
| U-001f | Liability Cap | FOA p.5 → 100% AgP | 2026-07-13 | v0.1.0 |
| U-001g | Warranty 期限 | FOA p.5 → 12 months from ETC/PAC | 2026-07-13 | v0.1.0 |
| U-001h | LD 上限 | ANX5 A.09 §A.9.2.3 → 10% Agg | 2026-07-13 | v0.1.0 |
| U-001i | 争议解决机制 | Art 46.2 → ICC/Abu Dhabi/English/3 arbitrators | 2026-07-13 | v0.1.0 |
| U-001j | Engineer 角色 | FOA p.5 → 无独立 Engineer，Company Rep 直接行使 | 2026-07-13 | v0.1.0 |
| U-001k | 适用法 | Art 46.1 → Abu Dhabi + UAE Federal | 2026-07-13 | v0.1.0 |
| U-001l | Order of Precedence | FOA Cl.1.6 → 14 层 | 2026-07-13 | v0.1.0 |
| U-001m | Art 20 B2B 法律基础 | GTC Art 20.1–20.6 → 强制 flows-downs + pay-when-paid | 2026-07-13 | v0.1.0 |

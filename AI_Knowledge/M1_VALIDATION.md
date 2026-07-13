# M1 VALIDATION — 能力验收报告 / Capability Gate
`[2026-07-13 · v0.1.0 冻结前置条件 · 沿 Philosophy→DNA→Clause→Evidence 链逐项验证]`

> 验收标准：系统能否对七个商业问题给出**有条款支撑、有风险判断、有商业解释**的回答——而非"知道文件在哪"。每一答标注穿过的知识节点。

---

## C1 · 谁承担设计责任？

**答**：**Wison 承担全部设计责任。** 合同删除了 FEED 和 FEED ENDORSEMENT 定义，替换为 EARLY DESIGN DOCUMENTS——承包商对 EDD "takes full responsibility…as being a suitable design for the WORKS that will satisfy the COMPANY's requirements"（Art 5.1(b)(iii)）。这是 LSTK 单点设计风险的典型实现。

**节点轨迹**：P1(先问谁承担) → DNA-2(风险分配) → PROFILE(LSTK) → FOA(Contractor=Wison Energy HK–AD) → SC item 2-4 → GTC Art 5.1(b)(iii)

**风险判断**：设计风险全部在 Wison。如有设计分包，须经 Art 20 Back-to-Back 流转——否则 Uncovered Exposure。

**状态**：✅ 可答，证据链完整。

---

## C2 · 为什么这里没有独立 Engineer？

**答**：本合同的 ADNOC-CICV-505A(v6) 表单**不设独立 Engineer 角色**。COMPANY REPRESENTATIVE = Mr. Jasem Al Hosani（VP/A, ADNOC Gas）直接行使业主代表职能——审批、指令、验收、争议——而非委托第三方/PMC。这是 ADNOC 直接控制模式：Company 通过自己的 Representative 直接管理承包商，不经 Engineer 中间层。

**节点轨迹**：ONTOLOGY §3(Party 模型中 Engineer 为可选 Role) → PROFILE(无独立 Engineer，Company Rep 名录) → FOA p.5(代表人/通知细节) → Art 24/Art 9.2/Art 46(权限均由 Company/Company Rep 行使，未见 Engineer 签发)

**商业含义**：指令与审批链更短——对 Wison 而言，所有 Company Rep 的指令都直接来自业主，没有"Engineer 的指令是否经 Employer 批准"这一层的模糊。但 Art 24.7 的大量排除同样适用——合规模板指令不构成 Variation。

**状态**：✅ 可答。Canonical 模型容纳 Engineer 这一 Role；本 Profile 实例化时该 Role 空置，由 Company Rep 直接行使。

---

## C3 · Variation 怎样影响付款？

**答**：**仅当成为正式 VARIATION ORDER 或 INSTRUCTION TO PROCEED 后，才影响 Agreement Price。** 路径：

1. Company 发 COMPANY VARIATION REQUEST → Contractor 14 天内交 VARIATION PROPOSAL（含价格影响 + 时间影响）→ Company 批准出 VARIATION ORDER
2. Contractor 发 CONTRACTOR VARIATION REQUEST（14 天时限，逾期=丧失调价权）→ Company 批准出 VO
3. 紧急情况下 Company 出 INSTRUCTION TO PROCEED（立即执行）→ 45 天内出 VO 替代
4. VO 中价格调整三选一：ANX5 费率 / 成本+overheads+profit / Company 合理 lump sum（Art 24.5(a)）
5. 付款时发票含"work related to a VARIATION ORDER"（Art 23.2(a)(iv)）
6. **未获 ITP/VO 擅自实施 = 自担风险 + 弃权**（Art 24.6(a)）

**节点轨迹**：P4(执行效力≠商业效力) → DNA-11(Variation 逻辑) → DNA-4(付款) → GTC Art 24.1–24.6 → GTC Art 23.2(a)(iv) → SC item 10(14 天)

**风险判断**：14 天时限是刚性闸门。现场接到指令必须先执行（Comply），但 CVR 必须在 14 天内发出——否则做了也白做。这是"Operational ≠ Commercial"在合同文本里的精确落实。

**状态**：✅ 可答。

---

## C4 · 如果分包商违约，总包有哪些 Back-to-Back 风险？

**答**：**三点，全部落在 Wison 身上：**

1. **责任不因批准而减免**：Company 对 Subcontractor 的批准"shall not relieve the CONTRACTOR of any of its obligations"（Art 20.2）。Company 与 Subcontractor 之间无合同关系——分包违约，Wison 对 Company 承担全责。
2. **视同自身违约**：Subcontractor/Vendor 的任何行为、疏忽、违约"as if they were the acts, omissions, breaches or defaults of the CONTRACTOR"（Art 20.3）。Wison 无法以"是分包商的问题"抗辩。
3. **赔偿义务**：Wison 须 indemnify Company 免受 Subcontractor/Vendor 对 Company 的索赔（Art 20.6）。
4. **Pay-when-paid**：Wison 对下付款=收到 Company 款项后 30 天（Art 20.5(a)）。

**B2B 暴露点**（C7 入口）：
- 如分包合同未含主合同的 LD → **LD Exposure = Uncovered**
- 如分包 Warranty 少于 12 个月 → **Warranty Exposure = Partial（差额）**
- 如分包未要求 UAE 银行 PBG/PCG → 分包违约时 Wison 无担保可追 → **Security Exposure**

**节点轨迹**：P2(下承诺前先查主合同) → P5(无法流转须认领) → 主合同 > GTC Art 20.1–20.6 → Exposure 模型(Uncovered/Partial/Covered) → ONTOLOGY §5(B2B=Rule Engine)

**状态**：✅ 可答（法律基础在 Art 20；缺口量化需具体分包合同读取——v0.2）。

---

## C5 · 为什么 Liability Cap 是 100%，但 LD 只有 10%？

**答**：**不是矛盾——是不同的风险管理工具，各自有各自的封顶逻辑。**

| 工具 | 上限 | 覆盖 |
|---|---|---|
| LD | 10% AgP | **仅延误**——15 个里程碑各自有日费率+单上限 |
| Total Cap | 100% AgP | **全部违约**——含 LD + 缺陷 + 履约失败 + IP + 保密… |

* LD 10% 是**预先约定的延误赔偿**（liquidated，非罚金）——ADNOC 市场惯例。LD 本身是 Consequential Loss 的例外（Art 42.11(a) 明确保留）。
* Cap 100% 意味着 Wison 的**全部合同责任以合同价格为天花板**——这是 LSTK 的风险对价：承包商以固定总价承担几乎全部完工风险，但责任不会超过这个总价。
* **10% vs 100% 之间的差额**是延误之外的违约类型可能在极端情况下产生的敞口：缺陷返工、性能不达标、IP 侵权、HSE 重大违规导致的终止——每一项都可能远超 10%。
* 不封顶尾部（Art 42.10(b)/SC item 13）——Gross Negligence/Wilful Misconduct、保密违约、第三方索赔、指定 indemnity——则完全在 Cap 之外。

**节点轨迹**：DNA-6(LD 10%) → DNA-7(Cap 100% + 不封顶尾部) → FOA p.4-5 → GTC Art 42.10–42.11 → SC item 13 → PROFILE

**状态**：✅ 可答。

---

## C6 · Order of Precedence 真发生冲突时怎么推理？

**答**：**按 FOA Cl.1.6 的 14 层链条逐级裁决。**

1. 确认冲突双方来源文件在链中的位置（如 Spec=SOW ANX3 在第 7 位；Drawing 如在 Execution ANX10=第 10 位 → Spec 优先）
2. 高位文件条款覆盖低位
3. **特别规则**：SC(ANX1) 明示 "supplement and/or amend" GTC——明确的覆盖机制
4. 未列入 Cl.1.6 的 Annexure 按 Cl.1.3 出现顺序

**实例推理**："图纸要求 Ø100，Spec 要求 Ø150——用哪个？"
- Drawing 来源：ANX10 Execution（第 10 位）或 ANX3 SOW（第 7 位）
- Spec 来源：ANX3 SOW（第 7 位）
- 若 Drawing 在 ANX10 → Spec（第 7 位）优先于 Drawing（第 10 位）→ Ø150
- 若 Drawing 在 ANX3 SOW → Cl.1.4 "supplementary and complementary"——两者互补，以更严格者为准（典型 GOOD INDUSTRY PRACTICE 解读）

**节点轨迹**：ONTOLOGY §5(优先权关系) → PROFILE(14 层链条) → FOA Cl.1.4/1.5/1.6 → SC preamble

**状态**：✅ 可答。

---

## C7 · External Contract 为什么必须 Flow-down，而不能直接复制？

**答**：**因为 Back-to-Back 是风险传递机制，不是文本裁剪。复制条款≠复制风险承接能力。**

三层的论证：

**① 法律层（Art 20）**：主合同不要求"复制条款"——它要求特定条款必须出现在分包中（保密/知识产权/道德规范/非转让/支持 novation），且 Contractor 对 Subcontractor 的全部行为承担全部责任。单纯的文本复制不转移责任——Art 20.3 已明确"视同承包商自身"。

**② 商业层**："复制"制造虚假安全感：
- 复制了 LD 条款但分包商是境外公司→无法执行→**Uncovered**
- 复制了 PBG 要求但分包商无法开立 UAE 银行保函→**Uncovered**
- 复制了 Warranty 12 个月但分包商按当地法只有 6 个月法定质保→**Partial（6 月差额）**
- 复制了制裁条款但分包商供应链经过受制裁国→可触发 Art 51 违约

**③ 系统层**：Flow-down 验证 ≠ 文本比对。它是：
```
Main Contract Risk → 是否有下游实体能承接？→ 承接的法律/商业可行性？
  → 可承接且条款对等 = Covered
  → 可承接但条款更弱 = Partial（主动标 High Risk）
  → 无法承接 = Uncovered（必须明确认领、入 Risk Register）
```

**节点轨迹**：P2+P5+P7(管理敞口非文书) → Philosophy §7(B2B is control, not copy-paste) → DNA B(Art 20 B2B 法律基础) → Exposure 模型 → ONTOLOGY §5(B2B=Rule Engine)

**状态**：✅ 可答（概念+法律基础完备；逐包验证需具体分包合同——v0.2）。

---

## 验收结论 / Gate verdict

| 能力 | 验证方式 | 结果 |
|---|---|---|
| C1 谁有权限 | C2(FW: 无独立 Engineer→Company Rep 直接行使) | ✅ |
| C2 Decision 有效 | 隐含在 C3/C4：VO 须 Company 签发、分包须 Company 批准 | ✅ |
| C3 Requirement 满足 | C1/C3：设计责任/付款先决可查 | ◐ |
| C4 B2B 完整性 | C4 + C7：Art 20 法律基础已立；逐包验证待 v0.2 | ✅ |
| C5 Notice/Time-bar | C3：14 天 CVR 刚性时限可查、可判 | ✅ |
| C6 Claim 合同依据 | C3/C4：Variation→Claim 链路可追踪 | ◐ |
| C7 Risk Pass-through | C4+C7：概念+法据+Exposure 模型就位；缺口=分包合同文本 | ✅ |

**M1 核心判据**：七问均能沿 Philosophy→DNA→Clause→Evidence 链给出**有条款引用、有商业判断、有风险结论**的回答。C3/C6 的 ◐ 是因为"Requirement 实体细化"和"Claim 规则"未写入 03_Rules——但知识已存在于 DNA+Clause 中，只是尚未编码为正式规则。这不阻塞 M1（属于 v0.2 规则形式化）。

## M1 结论

> **✅ M1 = PASS。系统已达到"结构稳定、可推理、可证据溯源"的最小可行知识基线。**
> 21 区 DNA 中 17 区 🟢、3 区 🟡、1 区 ⚪ 的覆盖率已足够支撑 C1–C7 推理；剩余区域属领域深化（v0.2），非架构阻塞。
> **建议冻结为 v0.1.0 – Foundation，commit 首次提交。**

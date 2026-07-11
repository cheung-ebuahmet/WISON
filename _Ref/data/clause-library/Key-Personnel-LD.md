# Key Personnel Liquidated Damages — 关键人员违约金

> **Topics:** LD | Sub-Clause 4.2.4 | Attachment 5
> **Library ID:** CL-LD-KP-001

---

## 条款概述

关键人员未经批准离岗、缺位或替换 → 按人按日计收违约金（Key Personnel Liquidated Damages），直到继任者经承包商批准到岗。

---

## 核心条款文本

### Sub-Clause 4.2.4 — 关键人员违约金

> Should any of the Key Personnel be removed from the PROJECT by the SUBCONTRACTOR before they have completed the tasks in respect of which they are appointed or otherwise become unavailable to perform the tasks for which they are appointed and are required to be so available, other than for the reasons referred to in Sub-Clause 4.2.3, the SUBCONTRACTOR fails to replace the Key Personnel in accordance with and in time frame specified in ATTACHMENT 5 [Key Personnel & Liquidated Damages], then the SUBCONTRACTOR shall pay to the CONTRACTOR liquidated damages set out in ATTACHMENT 5, [Key Personnel & Liquidated Damages] per individual Key Personnel (the "Key Personnel Liquidated Damages") and shall replace, at no additional cost to the CONTRACTOR, the relevant Key Personnel by a person that is qualified, skilled and experienced in the specified position with the CONTRACTOR's prior written consent (not to be unreasonably withheld).

### 附件5 — 违约金标准

| 合同 | 职位数 | LD/人/天 | 7人合计/天 |
|------|:-----:|:--------:|:----------:|
| [[10.1-CCECC-Civil-II]] | 7 | **AED 10,000** | AED 70,000 |
| [[10.2-TCC-Civil-I-III]] | *(待)* | *(待)* | *(待)* |
| [[12.1-CCECC-MEI-I]] | *(待)* | *(待)* | *(待)* |
| [[12.2-TCC-MEI-II]] | 🔴 | 🔴 | 🔴 |

---

## 触发条件

1. 关键人员被调离项目
2. 关键人员因故无法履职
3. 超出 Sub-Clause 4.2.3 允许范围（死亡/长期疾病/退休/辞职）
4. 未能按附件5规定时限替换
5. **违约方不区分原因** — 即使是分包商单方面不能履职也算

---

## 计罚起止

| 节点 | 规则 |
|------|------|
| **起算日** | 关键人员实际离岗之日 / 休假到期应返岗而未返岗之日 |
| **截止日** | 替代人员经承包商书面批准 + 实际进场到岗 |
| **计费单位** | 每日，不设上限（区别于 Delay LD 10% cap） |

---

## 扣款路径

- 直接从分包商月度 IPC（中期付款证书）中扣减
- 也可从保留金（Retention Money）中扣减

---

## 实践注意事项

1. **与 Delay LD 是独立平行的** — Key Personnel LD 不抵扣、不取代 Delay LD，可叠加计收
2. **即使安排了临时替补也仍需全额支付** — 合同原文未设"减半"或"暂停"机制
3. **分包商自费替换** — LD 之外还需承担替换人员的全部成本

---

## 相关链接

- **条款库:** [[Key-Personnel]] | [[Delay-LD]] | [[Termination]]
- **Wiki:** [[Liquidated-Damages]]
- **数据:** `data/contracts/10.1-CCECC-Civil-II.yaml` → `liquidated_damages.key_personnel`
- **源文件:** `Att 05_Key Personnel - LD.docx` (AED 10,000/day confirmed)

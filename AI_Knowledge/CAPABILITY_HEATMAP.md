# CAPABILITY_HEATMAP — 能力热力图 / Capability Heat Map
`[v0.2.2 · 活文档 · 每次制造后更新 · 驱动优先级——不是问"还有什么PDF"，是问"为什么这里这么冷"]`

> **热力图 = 系统的盲区图。** 🔥 = 高能力（热）· ❄ = 低能力（冷）。冷区自动暴露下一轮制造目标。
> 覆盖率的含义：**这个商业域里，系统能回答多大比例的真实合同问题**——不是 OCR 了多少文件。

---

## 总热力图 / Overall Heat Map

```
Variation        █████████░  88%  🔥🔥🔥🔥
Payment          ████████░░  80%  🔥🔥🔥🔥
LD / Delay       ████████░░  83%  🔥🔥🔥🔥
Security         ████████░░  80%  🔥🔥🔥🔥
Liability        ████████░░  85%  🔥🔥🔥🔥
Dispute          █████████░  90%  🔥🔥🔥🔥
Sanctions/Export █████████░  92%  🔥🔥🔥🔥
Warranty         ██████░░░░  63%  🔥🔥🔥
HSE              ███░░░░░░░  30%  🔥🔥
Authority        ███░░░░░░░  30%  🔥🔥
Insurance        ██░░░░░░░░  25%  🔥
Quality          ██░░░░░░░░  17%  ❄
Acceptance       ██░░░░░░░░  15%  ❄
Testing          █░░░░░░░░░   5%  ❄❄
```

---

## 冷区诊断 / Cold Zone Diagnostics

> 每个冷区下面回答**为什么冷**——答案直接驱动下周制造计划。

### ❄ Insurance (25%)
- **为什么冷**：Art 41 未读；ANX7（Company Provided Insurances）未读；险种/保额/免赔/Waiver of Subrogation 全未知
- **阻塞的能力**：C3（无法验证保险要求）· C4（无法检查分包保险 B2B）· C7（Insurance Exposure 无法判定）
- **下一轮目标**：Art 41 + ANX7 制造一轮 → 目标 25%→55%+
- **UNKNOWN_REGISTRY**：U-001

### ❄ Acceptance (15%)
- **为什么冷**：Art 15（MC/RFSU）· Art 17（PA/FA）未读；ANX11（证书格式）未读；Punch List·Claims Release Letter 机制未知
- **阻塞的能力**：C2·C3·C6
- **下一轮目标**：Art 15/17 + ANX11 → 15%→50%+
- **UNKNOWN_REGISTRY**：U-002

### ❄ Quality (17%)
- **为什么冷**：Art 13（Inspection & Testing）未读；ANX10 Exh B.10（QMR）未读
- **阻塞的能力**：C3·C5（NCR→Notice→Claim 链路无条款支撑）
- **下一轮目标**：Art 13 + ANX10 B.10 → 17%→45%+
- **UNKNOWN_REGISTRY**：U-003

### ❄❄ Testing (5%)
- **为什么冷**：Art 16（Performance Tests & Guarantees）未读；ANX10 Exh A.11（Performance Guarantees）未读
- **阻塞的能力**：C3·C6
- **下一轮目标**：Art 16 + ANX10 A.11 → 5%→35%+
- **UNKNOWN_REGISTRY**：U-006

---

## 能力栈热度 / Capability Stack Heat

```
C1 Authority      ██████░░░░  60%  🔥🔥🔥
C2 Decision       ██████░░░░  65%  🔥🔥🔥
C3 Requirement    █████░░░░░  50%  🔥🔥
C4 B2B            ███████░░░  70%  🔥🔥🔥🔥
C5 Notice/Time-bar ████████░░  78%  🔥🔥🔥🔥
C6 Claim          █████░░░░░  55%  🔥🔥🔥
C7 Pass-through   ████████░░  75%  🔥🔥🔥🔥
```

**最冷的能力**：C3 (50%) · C6 (55%) · C1 (60%)——这些就是制造优先级。

---

## 版本热度演进 / Heat Evolution
> 每版本记录热力图快照。

| Version | Δ | 说明 |
|---|---|---|
| v0.1.0 | — | Baseline：Variation/Payment/LD/Liability/Dispute/Sanctions 热 · Insurance/Acceptance/Quality/Testing 冷 |
| v0.2.0 | — | Rule Engine 上线：C5🟢 C7🟢 C3🟡 |
| v0.2.2 | — | Manufacturing Infrastructure 建成：热力图建立基线 |

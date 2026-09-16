# 专题会话总结文本（粘贴用）

> 用途：在终端执行 `claude -n "标题"` 新建会话后，把对应专题的总结粘贴进去，让 Claude 记住该专题上下文，作为该专题的存档会话。
> 生成：2026-09-07，基于会话 b905e7f2 全程工作归纳。

---

## T1 — Wison 分包合同与信函起草

```
本会话专题：Wison 分包合同管理与商务信函起草（CCECC MEI Pkg I 等）。

已完成工作与关键上下文：
1. 12.1 CCECC - MEI Pkg I 分包合同结构：Subcontract Agreement(7页) + LOA + Part I Special Conditions(15页) + Part II General Conditions(55页) + Exhibit A~M。
2. 分包商 CCECC = 中土(CCECC)+五矿二十三冶联合体，总包内部称呼混用（中土/五矿/五矿23冶）。
3. 起草了 CCECC MEI Pkg I 减量信函（Ref: SLT-5312-WSN-CCC-0009，2026-08-02），援引合同条款 GC 3.7/3.8/21.1/33 + SC 5.8，减量范围：Area 40 SSB + Area30/40 EIT(除package) + 地下管道转Contractor。
4. 起草了现场指令单据(SI)模板：Work_Liaison_Notice_SI_Template.xlsx，审批链 工程师→施工经理→商务/费控→项目经理。
5. 信函写作规范见记忆 wison-letter-writing-style / wison-letter-tone-and-register。

关键文件：
- 合同：D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Contract\
- 信函：D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Corres\
```

---

## T2 — Wison 目录整理与命名规范

```
本会话专题：D:\Wison 目录结构整理、脚本归位、命名规范。

已完成：
1. D:\Wison 目录审计（3055文件），三层架构：证据层(Main_Contract/Subcon_Payments/Project_Info) + 知识层(_Ref) + 工具层(_tools)。
2. 清理：.lnk、__pycache__、ltd_*.txt、双扩展名、Office临时文件~$。
3. 移动：Other CONTRACTS→_Ref\reference-contracts、SSB net roof→19 SSB Steel Structure。
4. 建立 D:\Wison\README.md（目录总览+分包商索引+命名规则）。
5. 建立 _tools\guides\backup-prompt.md（离线跨设备备份提示词）。
6. 私密文件→D:\Documents\Private（Project_Info 有快捷方式）。

命名规范（关键）：
- 信函：SLT-5312-{发}-{收}-{序号}_{简短主题}_ocred.pdf
- Tender Briefings：RSGP MEI {主题} YYYY-MM-DD.pptx
- 分包目录：[NN.N] [简称] - [范围]

规则：删除一律送回收站；脚本放 _tools；临时文件放 D:\Documents 根（非 My Projects 子目录）。
见记忆：wison-directory-classification、wison-vs-myprojects-boundary、docgen-script-location。
```

---

## T3 — Wison 信函归档与OCR流程

```
本会话专题：分包商往来信函归档处理（展平→OCR→重命名→分类→移动）。

已完成：处理了 CCECC Civil、CCECC MEI、TCC Civil、TCC MEI 四批信函（共~200文件）。

关键流程（已沉淀为 SOP，见 D:\Wison\_tools\guides\correspondence-archiving-sop.md）：
1. 展平：所有子目录文件上移到单一 Corres 目录。
2. OCR：pymupdf(fitz) + Tesseract，文字层用「可见近白色」(render_mode=0, color≈0.94)，禁用隐形层(render_mode=3)（SumatraPDF 选不中）。
3. 重命名：{完整REF}_{简短主题}_ocred.pdf，附件挂父REF。
4. 分类：COMMERCIAL(价格/费率/变更/索赔/EOT/保函/减量) vs 非COMMERCIAL(动员/HSE/质量/图纸/行政)。边界项必须问用户。
5. 对照表：Excel 含 REF/方向/日期/主题/正文简要/建议分类。

踩坑：
- os.remove 覆盖原扫描件会降分辨率，删除用回收站。
- 隐形文字层 SumatraPDF 无法选中。
- 删重按 REF 号判断（Wison 已有缩写命名版=同REF）。
- REF 正则需兼容 CC3/CVT 等含数字代号。

目标目录：
- 10.1 CCECC Civil、12.1 CCECC MEI、10.2 TCC Civil、12.2 TCC MEI 的 Corres\
```

---

## T4 — Wison 吊车租赁三家比价

```
本会话专题：XX Equipment Rental 吊车租赁三家比价表（Hareket / SinoPec / Faris）。

最终成果：D:\Wison\Subcon_Payments\XX Equipment Rental\Lifting Equipment Rental Quotation_Comparison.xlsx
两个 sheet：
1. Quotation Comparison：两两对比(12列)，单价/总价/月数列跨表引用 Multi-Vendor，Recommendation列静态显示"分包名(总价)"+颜色高亮最优家(绿Hareket/橙SinoPec/蓝Faris)。
2. Multi-Vendor：多供应商长表(8列)，改这里单价→Sheet1自动联动。

已定口径：
- Faris 单价"不含税"，与 Hareket/SinoPec 同口径。
- 260T/250T 差10吨视同混用；Faris"300T"实为400T，用户定放300T行一起比。
- Recommendation 只写"分包名(总价)"，不写 saves（无基准价）。

结论：180T/260T/600T 选 Faris；100T/160T/300T(Mobile)/400T/800T 选 Hareket；300T(Crawler) 选 SinoPec。

踩坑：openpyxl cell.fill=None 会损坏xlsx（用PatternFill()）；跨表引用公式无缓存结果在用户Excel端显示空白（故Recommendation改静态）。

见记忆：equipment-rental-comparison。
```

---

## T5 — Wison 范围重新划分与界面图

```
本会话专题：三家分包商之间范围重新划分 + 界面图更新。

三封信函（依据）：
1. TCC Civil 减量 SLT-5312-WSN-CVT-0019(文件名0017)：变电站/LCR/操作棚 从 Pkg1&3 移除。
2. CCECC Civil 增量 SLT-5312-WSN-CCE-0024：上述三项土建 转给 CCECC Pkg2。
3. CCECC MEI 减量 SLT-5312-WSN-CCC-0009：SSB+EIT(除package)+地下管道 转出。

已完成：
- 文字说明：D:\Wison\Project_Info\Scope & Interface\范围调整说明_Scope_Adjustment_Note.md
- 界面图标注：CIVIL/MEI SCOPE INTERFACE SPEC_标注.jpeg（红色框圈出变化区域）
- 原图未动，备份已清理。

界面划分现状：
- 土建3标段(紫,UNIT10=配电室/控制室/操作工室)：TCC→CCECC。
- MEI Pkg1：SSB、EIT(除package)、地下管道 减量；Area30造粒+传送系统 保留。

见记忆：scope-redistribution-3subcons。
```

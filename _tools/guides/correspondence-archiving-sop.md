# 信函归档处理流程 SOP（Correspondence Archiving SOP）

适用：把 `D:\Downloads` 等来源的往来信函（Incoming/Outgoing 分包商信函）整理归档到
`D:\Wison\Subcon_Payments\<分包商>\Corres\`。

原则：**展平 → OCR（可选中）→ 重命名（简短统一）→ 分类（COMMERCIAL/非）→ 对照表 → 用户定夺 → 执行**。

---

## 0. 前置约定

- **删除一律送回收站**（可找回），绝不永久删。用 PowerShell：
  `[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(path, 'OnlyErrorDialogs', 'SendToRecycleBin')`
- **OCR 管线**：pymupdf（fitz）渲染/取原图 → Tesseract 识别。**不用 poppler**。
- **文字层必须是"可见近白色"**（render_mode=0，color≈0.94），这样 SumatraPDF / PDF24 才能直接选中复制；**禁用 render_mode=3（隐形层）**，SumatraPDF 选不中。
- **保留原始嵌入图像像素**（不重新渲染），避免降分辨率。

## 1. 侦察（先摸清，再动手）

```python
# 列出源文件夹完整树 + 文件类型
# 判断每个 PDF 状态：
#   扫描件(无文字) = fitz 读到的总字符 < 20
#   已OCR(图+字)   = 有文字 且 有嵌入图
#   原生数字(纯字) = 有文字 且 无嵌入图
# 检查嵌入图分辨率（get_images + extract_image），记录原始尺寸
```

- REF 编号体系：`SLT-5312-{发送方}-{接收方}-{序号}`，如
  `SLT-5312-WSN-CCC-0001`（Wison→CCECC）、`SLT-5312-CCC-WSN-0001`（CCECC→Wison）。
- 方向判断：`WSN` 在前 = 去信（Outgoing），`WSN` 在后 = 来信（Incoming）。

## 2. 展平（Flatten）

- 所有文件（任意层级）上移到**文件夹根**（或指定单一子目录），删除空子目录。
- 处理 Unicode 特殊字符：`\xa0`（不间断空格）→ 普通空格。文件名带 `\xa0` 时用 `os.listdir` 拿到的原始名操作，不要手打。
- 附件文件名（`Attachment-1 ...`、`Appendix ...`）暂不动，重命名阶段再挂到父 REF。

## 3. OCR（只处理扫描件）

```python
def ocr_preserve(fp):  # 关键：保留原图像素，不 get_pixmap 重渲染
    src = fitz.open(fp); dst = fitz.open()
    for page in src:
        newpage = dst.new_page(width=page.rect.width, height=page.rect.height)
        # 取原始嵌入图（extract_image 拿原始字节），没有图才渲染
        imgs = page.get_images(full=True)
        img_bytes = src.extract_image(imgs[0][0])['image'] if imgs else page.get_pixmap(dpi=300).tobytes('png')
        text = pytesseract.image_to_string(Image.open(io.BytesIO(img_bytes)), lang='eng+chi_sim')
        newpage.insert_image(newpage.rect, stream=img_bytes)
        tw = fitz.TextWriter(newpage.rect)
        tw.append(fitz.Point(5,10), text, fontsize=6)
        tw.write_text(newpage, color=(0.94,0.94,0.94), render_mode=0)  # 可见近白
    # 原扫描件送回收站，OCR 版替换原位
```

- 已 OCR / 原生数字的文件**不要动**（保持原样，除非它也是隐形文字层）。
- OCR 后文件名加 `_ocred` 后缀；原生数字不加。

## 4. 提取主题 / 日期 / 正文

- 从 OCR 文本提取 `Subject:` / `主题:` / `Date:` / `Dear ...` 之后的正文。
- 纯编号文件（无描述性主题）需 OCR 提取 subject。
- OCR 质量差时，用 **OpenCV 预处理**（2× 放大 + 灰度 + CLAHE + 自适应二值化）重试，常能救回 subject 行：
  ```python
  img = cv2.resize(gray, (w*2, h*2), interpolation=cv2.INTER_CUBIC)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(img)
  # 或 GaussianBlur + adaptiveThreshold 二值化
  ```

## 5. 重命名

统一格式：`{完整REF}_{简短主题}_ocred.{ext}`

- **REF 保留完整前缀** `SLT-5312-` / `LT-5312-`（不截断）。
- **简短主题用缩写风格**，对齐既有命名：
  `SD in Mob`（Serious Delay in Mobilization）、`CLAR`（Clarification）、
  `RE NOTICE DEF`（Reply Notice of Default）、`Req_Waive_5%_DLP&ICV`、
  `Mob of QS Resources`（Mobilization of Quantity Surveying）、`APG and PEB`（保函）。
- 附件挂父 REF：`{父REF}_Attachment 1 ...` / `{父REF}_Appendix 1 ...`。
- 修正 `SLT-SLT-5312` 双前缀 → `SLT-5312`。
- `.PDF` → `.pdf` 统一小写。

## 6. 分类（COMMERCIAL vs 非COMMERCIAL）

**COMMERCIAL（保留用于商务管理）**：
价格/费率/BOQ、暂定金额/间接费、变更提案（Change Proposal）、索赔/EOT/保险/不可抗力、
保函（APG/PEB）、计量方法、减量通知（Scope Reduction/Descope）、扣款/违约扣罚、质保金/ICV豁免。

**非COMMERCIAL**：动员（Mobilization）、施工（Construction/进度）、HSE、质量（QA/QC/WPQR焊接工艺）、
图纸（Drawing/IFC）、行政（会议邀请/放假通知/PM缺席）、其他（zip附件）。

**边界（必须问用户）**：LD 误期违约金通知、QC 合同不合规、不可抗力前奏、地区冲突等 —— 逐条问用户定夺。

> 用户既往判例：QC 人员缺席/合同不合规 → 曾判 COMMERCIAL（CCECC），也曾判删除（TCC，用户说"不属于商务"）。
> **不同分包商/不同场景可能不同，不要套用，一律问。**

## 7. 生成对照表（Excel）

列：`No | REF号 | 方向 | 日期 | 主题 | 正文简要 | 建议分类`

- 色标：COMMERCIAL 橙底加粗、边界 黄底、非COMMERCIAL 绿/蓝/灰。
- 冻结首行 + 自动筛选（按"建议分类"列筛）。
- 交给用户逐条核对，标注"需判断的边界项"单独列出。

## 8. 执行（用户最终指令后）

- 非COMMERCIAL → 回收站。
- COMMERCIAL 且 Wison 目标目录无同 REF → 移动。
- COMMERCIAL 但 Wison 已有**同 REF**（缩写命名已存）→ **保留原版，删新版**（不移动）。
- 修正 Wison 已有的错名文件（如 023 实为 024）。

## 9. 收尾验证

1. **验证全部 PDF 文字层可选中**：
   ```python
   for f in pdfs:
       chars = sum(len(pg.get_text().strip()) for pg in doc)
       modes = set(re.findall(r'(\d)\s+Tr\b', pg.read_contents().decode(...)))
       # 异常：chars<20（无文字） 或 '3' in modes（隐形层）
   ```
2. **检查遗留**：放错目录的（机电↔土建，看 REF 前缀 `CC3`=MEI三化建、`CCC/CCE`=CCECC）、
   `~$` 临时锁定文件、`SLT-SLT` 双前缀、纯中文无 REF 的文件。
3. 清理临时脚本（送回收站）。

---

## 关键教训（踩过的坑）

1. **别用 `os.remove()` 覆盖原扫描件**（降分辨率 + 不可恢复）。保留原图像素，删除用回收站。
2. **别用 render_mode=3 隐形文字层**，SumatraPDF 选不中；用 render_mode=0 + 近白色。
3. **删重判断要按 REF 号**，不是文件名——Wison 里已有文件用缩写命名，下载来的用长标题，REF 相同就是同一个文件。
4. **附件要挂父 REF**，否则散落无归属。
5. **REF 提取正则要兼容 `CC3`/`CVT` 等含数字的代号**，且保留完整 `SLT-5312-` 前缀。

---

*SOP 记录于 2026-09-02，源自 CCECC CIVIL / CCECC MEI / TCC CIVIL / TCC MEI 四批信函归档实战。*

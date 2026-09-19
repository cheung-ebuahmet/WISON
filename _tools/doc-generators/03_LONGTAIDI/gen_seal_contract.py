"""
Generate Seal/Chop Instruction (用印说明) for LONGTAIDI Fabrication Subcontract.
"""
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', errors='replace')

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

OUT = r"D:\Wison\Subcon_Payments\99 LONGTAIDI fob\Contract\Part I Subcontract Agreement\用印简要说明_LONGTAIDI预制合同.docx"

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(10.5)
style.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def add_para(text, bold=False, size=10.5, align=None, color=None, space_before=0, space_after=3):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align: p.alignment = align
    run = p.add_run(text)
    run.font.name = 'Calibri'; run.font.size = Pt(size); run.bold = bold
    if color: run.font.color.rgb = color
    return p

def add_heading(text, size=12, space_before=12, space_after=4):
    return add_para(text, bold=True, size=size, color=RGBColor(0x1F,0x4E,0x79),
                    space_before=space_before, space_after=space_after)

def set_cell(cell, text, bold=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = cell.paragraphs[0]
    p.alignment = align
    run = p.add_run(text) if not p.runs else p.runs[0]
    if p.runs and not p.text:
        run = p.add_run(text)
    elif p.runs:
        p.runs[0].text = text
        run = p.runs[0]
    else:
        run = p.add_run(text)
    run.font.name = 'Calibri'; run.font.size = Pt(size); run.bold = bold

def shd(cell, color):
    cell._tc.get_or_add_tcPr().append(
        parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>'))

def borders(table):
    tblPr = table._tbl.tblPr
    if tblPr is None: tblPr = parse_xml(f'<w:tblPr {nsdecls("w")}></w:tblPr>'); table._tbl.insert(0, tblPr)
    b = parse_xml(f'<w:tblBorders {nsdecls("w")}>'
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="888888"/>'
        '</w:tblBorders>')
    tblPr.append(b)

# ============================================================
# TITLE
# ============================================================
add_para("用印简要说明", bold=True, size=16, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2,
         color=RGBColor(0x1F,0x4E,0x79))
add_para("Seal / Chop Instruction", bold=False, size=9, align=WD_ALIGN_PARAGRAPH.CENTER,
         color=RGBColor(0x99,0x99,0x99), space_after=10)

# ============================================================
# 一、用印文件
# ============================================================
add_heading("一、用印文件")

t1 = doc.add_table(rows=5, cols=2)
t1.alignment = WD_TABLE_ALIGNMENT.LEFT
borders(t1)
for i, w in enumerate([Inches(2.0), Inches(4.5)]):
    for row in t1.rows:
        row.cells[i].width = w

info = [
    ("文件名称", "《消防管道（3寸及以上）预制加工分包合同》（FOB 交付）"),
    ("英文名称", "Subcontract Agreement for Fire-Fighting Piping (3-inch and above)\nFabrication Works on FOB Basis"),
    ("合同编号", "WISON24108C26010"),
    ("签约方", "（1）WISON ENERGY ENGINEERING (HONG KONG) LIMITED – ABU DHABI（承包商 / Contractor）\n（2）Cangzhou Longtaidi Pipe Technology Co., Ltd. / 沧州隆泰迪管道科技有限公司（分包商 / Subcontractor）"),
    ("项目名称", "Sulphur Granulation Plant (RSGP) at RSHT - 2 for Hail & Ghasha Project"),
]
for ri, (label, val) in enumerate(info):
    set_cell(t1.rows[ri].cells[0], label, bold=True)
    shd(t1.rows[ri].cells[0], 'F0F3F7')
    set_cell(t1.rows[ri].cells[1], val)

doc.add_paragraph()

# ============================================================
# 二、用印份数与语言
# ============================================================
add_heading("二、用印份数与语言")

add_para("• 签署份数：本合同为双方协议（非三方），签署后各方各执一份正本，具有同等法律效力。", space_after=2)
add_para("• 用印方式：公司公章（或合同专用章）+ 授权代表签字。", space_after=2)
add_para("• 语言版本：英文为合同的唯一权威语言。合同正文及附件均以英文书写。", space_after=2)

doc.add_paragraph()

# ============================================================
# 三、合同核心内容
# ============================================================
add_heading("三、合同核心内容")

add_para("本合同为 Wison 与 LONGTAIDI 签订的双边分包合同，主要内容如下：", space_after=4)

scope_text = (
    "1. 工程范围（Article 3 & Exhibit A）：分包商负责公称直径 3 寸及以上消防管道（法兰连接）的 "
    "详细设计、材料接收验证、工厂预制、喷砂涂装、水压试验、以及以 FOB 方式运至中国指定港口交付。"
    "合同总量约为 6.7 万寸径焊接量。"
)
add_para(scope_text, space_after=3)

price_text = (
    "2. 合同价格（Article 5 & Exhibit D）：暂定分包合同价格为 USD 976,747.73（不含增值税），"
    "以实际验收合格的工程量按中标函中的全费用单价计量支付。所有费率和款项均以美元（USD）计价和支付。"
    "适用增值税按中华人民共和国税法另行开具发票和缴纳。"
)
add_para(price_text, space_after=3)

schedule_text = (
    "3. 工期（Article 4 & Exhibit A.2）：分包商须严格按照中标函附件及 Work Schedule 中的"
    "里程碑节点完成预制和交付。合同生效日、开工日、施工开始日均为中标函签发之日（三者同日）。"
)
add_para(schedule_text, space_after=3)

docs_text = (
    "4. 合同文件组成（Article 1）：共 18 个文件，按优先顺序为——(a) 本分包合同协议、(b) 中标函（含 LD、"
    "澄清、无偏差声明、ICV 改进计划共 4 个附件）、(c) Part I 特殊合同条件、(d) Part II 一般合同条件、"
    "(e) 附件 A 至 M（含工作范围、计量方法、技术规范、价格表、质量要求、行政程序、HSE、进度报告、"
    "业主特殊要求、采购通用条款、统一确认模板等）。"
)
add_para(docs_text, space_after=3)

other_text = (
    "5. 其他核心条款：履约保函（合同价格的 10%，生效后 14 天内提交）、保险（开工前置条件）、"
    "缺陷责任与保修期（Article 5 of Special Conditions）、知识产权与保密、"
    "管辖法与争议解决（阿布扎比法律及阿联酋联邦法律）、合同终止与转让限制。"
)
add_para(other_text, space_after=4)

doc.add_paragraph()

# ============================================================
# 四、相关审批流程
# ============================================================
add_heading("四、相关审批流程")

add_para("1.  合同评审表（Contract Review Form）—— 须随附上传，为用印前置必要条件。", space_after=2)
add_para("2.  本合同属于新签分包合同（非变更协议），须按公司分包合同审批权限完成全部内部审批流程（）后方可用印。", space_after=2)
add_para("3.  中标函（LOA）已于 2026 年 7 月 28 日签发，合同签署应在 LOA 签发后 30 日内完成。", space_after=2)
add_para("4.  双方签署后，应扫描 PDF 存档并分发双方各自留存。正本原件建议由合同管理部统一保管。", space_after=2)

doc.add_paragraph()

# ============================================================
# 五、随附上传附件清单
# ============================================================
add_heading("五、随附上传附件清单")

t2 = doc.add_table(rows=7, cols=4)
t2.alignment = WD_TABLE_ALIGNMENT.CENTER
borders(t2)

col_w = [Inches(0.4), Inches(3.2), Inches(1.5), Inches(1.6)]
for i, w in enumerate(col_w):
    for row in t2.rows:
        row.cells[i].width = w

# Header
for ci, txt in enumerate(["序号", "附件名称", "文件大小参考", "备注"]):
    set_cell(t2.rows[0].cells[ci], txt, bold=True, size=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    shd(t2.rows[0].cells[ci], '1F4E79')
    # White text
    for run in t2.rows[0].cells[ci].paragraphs[0].runs:
        run.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)

attachments = [
    ("1", "合同评审表（已签批）", "~2 MB", "必须上传"),
    ("2", "Part I 01 Subcontract Agreement（合同正文）", "~55 KB", "用印文件"),
    ("3", "Part I 02 Special Conditions of Subcontract", "~80 KB", "用印文件（Part I）"),
    ("4", "Part I 03 General Conditions of Subcontract", "~200 KB", "用印文件（Part II）"),
    ("5", "LOA——中标函（含 LD / 澄清 / 无偏差声明 / ICV 共 4 附件）", "~120 KB", "用印文件"),
    ("6", "LONGTAIDI 最终报价及 BOQ 明细", "~1 MB", "商业依据，参考附后"),
]

for ri, (no, name, size, remark) in enumerate(attachments):
    r = ri + 1
    set_cell(t2.rows[r].cells[0], no, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t2.rows[r].cells[1], name)
    set_cell(t2.rows[r].cells[2], size, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(t2.rows[r].cells[3], remark, align=WD_ALIGN_PARAGRAPH.CENTER)
    if ri % 2 == 0:
        for cell in t2.rows[r].cells:
            shd(cell, 'FAFBFC')

doc.add_paragraph()

# ============================================================
# 六、备注
# ============================================================
add_heading("六、备注")

notes = [
    "合同为双边协议（Wison–LONGTAIDI），不涉及 CCECC。LONGTAIDI 为阿联酋境外（中国）签约方，"
    "用印前须确认 LONGTAIDI 方签字人的授权委托书（POA）或法定代表人证明文件已提供。",

    "合同价格不含税（exclusive of VAT），适用中国增值税法规。履约保函金额为 USD 97,674.77"
    "（合同价格的 10%），须在合同生效后 14 日内提交。",

    "中标函中包含的 ICV 条款已标记为 N/A（FOB 中国交付不适用阿联酋本地化价值要求）。",

    "本合同项下 Exhibits G（NA）和 I（NA）为预留编号，无实质内容，不影响合同完整性。",

    "用印完成后，建议将全套合同文件（含 LOA 及所有附件）扫描为一个完整 PDF，"
    "分发双方各自存档。项目管理部及商务部各留存一份扫描件。",
]

for n in notes:
    add_para("• " + n, size=10, space_after=3)

# ============================================================
# FOOTER
# ============================================================
doc.add_paragraph()
add_para("— End —", size=9, align=WD_ALIGN_PARAGRAPH.CENTER, color=RGBColor(0xAA,0xAA,0xAA))

# ============================================================
# SAVE
# ============================================================
doc.save(OUT)
print(f"Saved: {OUT}")

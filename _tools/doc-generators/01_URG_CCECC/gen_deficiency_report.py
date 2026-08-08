import sys, os, io
# Fix Unicode output on Windows cp1252 consoles
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    """设置单元格背景颜色"""
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """设置单元格内边距"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_styled_heading(doc, text, level, space_before=12, space_after=6):
    """添加带有标准工业蓝色彩的主次标题"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True

    run = p.add_run(text)
    run.bold = True

    if level == 1:
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(31, 78, 121)  # 工业深蓝
        # 加下划线边框模拟设计感
        pBdr = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '12')
        bottom.set(qn('w:space'), '4')
        bottom.set(qn('w:color'), '1F4E79')
        pBdr.append(bottom)
        p._p.get_or_add_pPr().append(pBdr)
    elif level == 2:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(46, 116, 181)  # 钢蓝
    return p

# ============================================================
# 1. 初始化文档与页面设置
# ============================================================
doc = docx.Document()
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# 设置全局默认字体
doc.styles['Normal'].font.name = 'Arial'
doc.styles['Normal'].font.size = Pt(10.5)
doc.styles['Normal'].font.color.rgb = RGBColor(51, 51, 51)

# ============================================================
# 2. 文档头部 / 文件编号标识（右对齐）
# ============================================================
p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_meta.paragraph_format.space_after = Pt(24)
run_meta = p_meta.add_run(
    "文件编号：SLT-5312-WSN-CCC-MEI1 PERF DEFICIENCY RPT\n"
    "日期：2026年7月20日"
)
run_meta.font.size = Pt(9.5)
run_meta.font.color.rgb = RGBColor(128, 128, 128)

# ============================================================
# 3. 大标题
# ============================================================
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(18)
run_title = p_title.add_run(
    "附件：关于分包商MEI-1现场履约滞后及施工准备缺陷的专项报告"
)
run_title.font.size = Pt(18)
run_title.bold = True
run_title.font.color.rgb = RGBColor(31, 78, 121)

# 前言
p_intro = doc.add_paragraph()
p_intro.paragraph_format.space_after = Pt(12)
p_intro.paragraph_format.line_spacing = 1.25
run_intro = p_intro.add_run(
    "自4月24日召开项目开工会至今已近双月，分包商MEI-1在人员动迁、组织架构流转、"
    "技术准备及现场施工条件筑造等方面均存在严重违约与滞后。现将现场复盘的关键问题、"
    "履约风险及难点梳理如下，作为后续合同法律责任划定的事实依据。"
)

# ============================================================
# 4. 清单核心数据结构 (模块 - 细项 - 现场事实 - 履约风险)
# ============================================================
data = [
    {
        "category": "一、 关键管理体系与现场履约能力审查 (Organization & Management)",
        "items": [
            {
                "num": "1.1",
                "title": "组织架构运行瘫痪，管理职责严重错位",
                "fact": "现场虽配置了施工、质量、安全经理，但对外资源协调不力，对内施工资源控制、"
                       "质量与安全体系完全未能有效建立。",
                "risk": "技术与商务澄清对接的责任划分模糊，导致大量具体执行工作过度集中于项目经理一人。"
                       "项目经理缺乏后方总部高层的有效支持，导致通勤车辆、SSB网架拼装脚手架、"
                       "大型吊装等关键分包合同的签署进度极度缓慢，管理陷入恶性循环。"
            },
            {
                "num": "1.2",
                "title": "海外项目经验严重匮乏，缺乏国际化合规管理能力",
                "fact": "包括施工经理、各专业工程师在内的多名核心管理人员，完全不具备海外同类项目"
                       "执业经验，存在严重的语言沟通障碍。",
                "risk": "管理团队对海外项目的审批流程、跨国管理难点及属地化市场资源一无所知，"
                       "无法编制合规的前期总体策划，丧失对各项准备工作的实质控制力。"
            }
        ]
    },
    {
        "category": "二、 关键人力资源动迁滞后风险 (Mobilization Delays)",
        "items": [
            {
                "num": "2.1",
                "title": "核心管理及技术工程师严重缺位",
                "fact": "截至目前，项目计划工程师、吊装工程师、焊接工程师、设备工程师，以及文控和"
                       "各专业（钢结构、管道、设备、油漆）质检员（QC）均未到岗。",
                "risk": "直接导致前期施工组织策划停滞，大批项目亟需的合规文件和施工方案无法按时编制与提交。"
            },
            {
                "num": "2.2",
                "title": "法定/关键直接人力（Direct Labour）未按计划到场",
                "fact": "截至目前，影响现场开工的法定核心岗位，包括现场准入授权人（Permit Authority）、"
                       "许可证协调员（Permit Coordinator）、脚手架主管/检查员（Scaffold Supervisor/Inspector）、"
                       "吊装主管（Lifting Supervisor）、测量员（Surveyor）及急救员（First-aider）等"
                       "关键人员均未到岗。",
                "risk": "违反属地法律及业主现场HSSE强制规范，导致现场直接施工无法合法、安全地实质性展开。"
            }
        ]
    },
    {
        "category": "三、 技术文件与商务准备滞后情况 (Technical Documentation)",
        "items": [
            {
                "num": "3.1",
                "title": "核心施工方案（MS）及技术文件严重逾期",
                "fact": "当前急需的SSB网架吊装及拼装脚手架方案、堆取料机吊装及安装方案、"
                       "造粒机滚筒吊装方案等均未提交。一般吊装方案及灌浆料材料审批单（MAR）等"
                       "核心文件至今未能关闭。",
                "risk": "技术前置审批流程未完成，直接卡死后续各项正式工程的现场准入，"
                       "构成了重大的实质性工期延误风险。"
            },
            {
                "num": "3.2",
                "title": "质量控制（QC）与安全应急体系流于形式",
                "fact": "关键的焊接工艺评定（PQR）至今尚未开始制作焊接试件；钢结构、动设备等"
                       "检验试验计划（ITP）以及现场应急救援计划等安全文件处于缺位状态。",
                "risk": "不具备开工必备的质量控制与安全保障法定条件，"
                       "现场随时面临被业主叫停并开具违规罚单的风险。"
            }
        ]
    },
    {
        "category": "四、 施工现场临时设施与机具准备缺陷 (Site Infrastructure & Logistics)",
        "items": [
            {
                "num": "4.1",
                "title": "现场临建与预制场建设严重违约",
                "fact": "现场办公区的休息棚、库房至今未完工；原定于6月15日应交付投用的预制场，"
                       "至今仍有大量物资与配套设施未落实。",
                "risk": "分包商自身的生产、仓储及办公环境不具备基本功能，导致后续工序无法正常衔接。"
            },
            {
                "num": "4.2",
                "title": "施工关键机具与动力设施未到位",
                "fact": "现场施工急需的发电机（Power Generator）、高空作业车（Boom Lift）、"
                       "叉车（Forklift）等关键机械设备仍未调拨至现场。",
                "risk": "现场缺乏基本的垂直运输、高空作业能力及动力源，"
                       "具备施工条件后也无法立即开展实质工作。"
            }
        ]
    }
]

# ============================================================
# 5. 循环渲染高对比度、高Scannability的清单表格
# ============================================================
for cat in data:
    add_styled_heading(doc, cat["category"], level=1, space_before=16, space_after=8)

    # 建立每组条目的明细表格
    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # 定义列宽
    col_widths = [Inches(0.5), Inches(1.8), Inches(2.2), Inches(2.5)]

    # 设置表头
    hdr_cells = table.rows[0].cells
    headers = ["编号", "检查细项 / 重点难点", "现场实际情况 (Fact)", "合同履约风险 (Risk)"]
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "1F4E79")  # 深蓝色表头
        set_cell_margins(hdr_cells[i], top=120, bottom=120)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.runs[0]
        run.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)  # 白色文字
        run.font.size = Pt(10)

    # 填充数据行
    for item in cat["items"]:
        row_cells = table.add_row().cells
        row_cells[0].text = item["num"]
        row_cells[1].text = item["title"]
        row_cells[2].text = item["fact"]
        row_cells[3].text = item["risk"]

        # 格式化数据行样式
        for i in range(4):
            set_cell_margins(row_cells[i], top=100, bottom=100, left=100, right=100)
            p = row_cells[i].paragraphs[0]
            p.paragraph_format.line_spacing = 1.15

            # 对编号和标题列加粗
            if i in [0, 1]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    run.bold = True
                    run.font.size = Pt(9.5)
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    run.font.size = Pt(9.5)

        # 针对风险列文字着重处理 (浅红色背景提示法务风险)
        set_cell_background(row_cells[3], "FDF2F2")
        # 针对事实列给与清爽白灰色区分
        set_cell_background(row_cells[2], "FAFAFA")
        set_cell_background(row_cells[1], "F5F7FA")
        set_cell_background(row_cells[0], "F5F7FA")

    # 调整所有单元格实际应用宽度
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

# ============================================================
# 6. 结论与限期整改要求 (警告强调样式的文本框)
# ============================================================
add_styled_heading(
    doc,
    "⚠️ 结论与限期整改要求 (Conclusion & Demanded Actions)",
    level=1, space_before=24, space_after=6
)

alert_table = doc.add_table(rows=1, cols=1)
alert_table.alignment = WD_TABLE_ALIGNMENT.CENTER
alert_cell = alert_table.rows[0].cells[0]
alert_cell.width = Inches(7.0)
set_cell_background(alert_cell, "FFF9E6")  # 警告浅黄底色
set_cell_margins(alert_cell, top=140, bottom=140, left=180, right=180)

# 加粗警告句
p_warn_head = alert_cell.paragraphs[0]
p_warn_head.paragraph_format.space_after = Pt(4)
r_wh = p_warn_head.add_run("严重声明与限期：")
r_wh.bold = True
r_wh.font.size = Pt(10.5)
r_wh.font.color.rgb = RGBColor(199, 121, 44)

p_warn_body = alert_cell.add_paragraph()
p_warn_body.paragraph_format.line_spacing = 1.25
r_wb = p_warn_body.add_run(
    "鉴于上述因分包商MEI-1自身原因导致的严重违约行为，已引发我司及业主的强烈关注，"
    "并对项目整体关键路径（Critical Path）造成不可逆的工期威胁。\n\n"
    "我司特此限定：分包商MEI-1必须在7月31日前，对上述清单所列的所有管理、人力、文件、"
    "临建及机具缺陷完成全面闭环整改。必须立即替换并增补具备海外经验的核心管理人员，"
    "完成所有缺失人员的动迁，并闭环清偿所有逾期技术方案，确保正式工程具备开工条件。"
)
r_wb.font.size = Pt(10)
# 针对时间截点加粗高亮
for run in p_warn_body.runs:
    if "7月31日前" in run.text:
        run.bold = True

# ============================================================
# 7. 保存文件
# ============================================================
output_dir = r'D:\Wison\Subcon_Payments\12.1 CCECC - MEI Pkg I\Corres\URG'
output_path = os.path.join(output_dir, "SLT-5312-WSN-CCC-MEI1_PERF_DEFICIENCY_RPT.docx")
doc.save(output_path)
print(f"文档生成成功：{output_path}")

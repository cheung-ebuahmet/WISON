"""Bilingual (EN/ZH) Non-Disclosure Agreement — Wison (Contractor) <-> Subcontractor.

Generic NDA for proposal evaluation / intended cooperation — no project-specific
scope, no Discope or SSB references.

Usage:
    from nda_wison import NDA, fill_nda, validate_nda
    filled = fill_nda(contractor_name="Wison Energy Engineering (Hong Kong) Limited ...", ...)
"""

import os
import re

# ==============================================================================
# NDA TEMPLATE — WISON ↔ SUBCONTRACTOR
# ==============================================================================

NDA = """NON-DISCLOSURE AGREEMENT
保密协议

1.0 CONTRACTING PARTIES & EFFECTIVE DATE / 缔约主体与生效日期

1.1 Effective Date / 协议签订日期
This Non-Disclosure Agreement (hereinafter referred to as the "Agreement") is made and entered into as of [[________] - Insert Date], 2026.
本保密协议（下称"本协议"）于 2026 年[[________] - 填写月份]月[[________] - 填写日期]日签订并生效。

1.2 Contractor / 承包商
[[________] - Insert Contractor Legal Name], a company incorporated under the laws of [[________] - Insert Jurisdiction], having an office at [[________] - Insert Office Address] (hereinafter referred to as the "Contractor").
承包商：[[________] —— 填写承包商法定全称]，一家根据 [[________] —— 填写注册地] 法律设立并存续的公司，其办公地址位于 [[________] —— 填写办公地址]（下称"承包商"）。

1.3 Subcontractor / 分包商
[[________] - Insert Subcontractor Legal Name], a company organised and existing under the laws of [[________] - Insert Country of Incorporation], having an office at [[________] - Insert Subcontractor Address] (hereinafter referred to as the "Subcontractor").
分包商：[[________] —— 填写分包商法定全称]，一家根据 [[________] —— 填写注册国] 法律设立并存续的公司，其办公地址位于 [[________] —— 填写分包商地址]（下称"分包商"）。

2.0 PERMITTED PURPOSE & DEFINITION OF CONFIDENTIAL INFORMATION / 允许之目的与保密信息定义

2.1 Permitted Purpose / 允许之目的
The Contractor contemplates evaluating the technical capability, engineering capacity, commercial pricing, and overall qualifications of the Subcontractor in connection with a potential cooperation or subcontract award under one or more projects of the Contractor (the "Permitted Purpose").
承包商拟就潜在合作或分包授予事宜，评估分包商的技术能力、工程能力、商业报价及综合资质（下称"允许之目的"）。

2.2 Confidential Information / 保密信息
"Confidential Information" means any and all technical, commercial, financial, engineering, or operational data disclosed by the Contractor or its Affiliates to the Subcontractor for the Permitted Purpose, whether communicated orally, visually, in writing, or via digital access. This Confidential Information includes, but is not limited to: the existence and content of these discussions; all technical drawings, specifications, models, methodologies, pricing data, and project-related documentation; and the fact that meetings are being convened between the Parties.
"保密信息"是指承包商或其关联方为实现允许之目的而向分包商披露的任何及所有技术、商务、财务、工程或运营数据，不论是以口头、视觉、书面还是数字化访问形式流转。该保密信息包括但不限于：本洽谈工作的存在及内容、所有技术图纸、规范、模型、方法论、定价数据及项目相关文件，以及双方之间正在举行会议这一事实本身。

3.0 CONFIDENTIALITY OBLIGATIONS / 保密义务

3.1 Non-Disclosure & Restricted Use / 保密与使用限制
The Subcontractor shall use the Confidential Information solely for the Permitted Purpose and shall hold all such data in strict confidence. The Subcontractor shall not disclose, copy, replicate, publish, or distribute the Confidential Information to any third party — including, without limitation, any other subcontractors, suppliers, or commercial agents — without the prior explicit written consent of the Contractor.
分包商应仅为允许之目的使用保密信息，并对所有该等数据严格保密。未经承包商事先明确书面同意，分包商不得向任何第三方（包括但不限于任何其他分包商、供应商或商业代理）披露、复制、仿制、出版或分发保密信息。

3.2 Internal Need-to-Know Restriction / 内部知悉范围控制
The Subcontractor shall restrict access to the Confidential Information strictly to those of its directors, senior officers, or key employees who directly require access to such data to evaluate and respond to the Permitted Purpose, and who are legally bound by enforceable confidentiality undertakings no less stringent than the provisions of this Agreement. The Subcontractor shall carry total and unconditional liability for any breach of this Agreement by its personnel, advisors, or representatives.
分包商应将保密信息的知悉范围，严格限制在为评估和响应允许之目的而直接需要知悉该数据的董事、高级职员或核心员工之内，且上述人员须受法律强制执行的、严格程度不低于本协议规定的保密承诺的约束。分包商应对其人员、顾问或代表违反本协议的任何行为承担完全且无条件的法律责任。

4.0 PROPERTY OWNERSHIP & DATA RETURN / 所有权与资料归还

4.1 No Grant of Rights / 不创设权利
The provision of Confidential Information under this Agreement shall not be construed as an offer, a promise of contract award, or an implication of any commercial arrangement. No license, copyright, patent, or intellectual property right is transferred, granted, or implied from the Contractor to the Subcontractor. All Confidential Information remains the exclusive property of the Contractor.
本协议项下保密信息的提供，在任何情况下均不得解释为要约、授予合同的承诺、或对任何商业安排的默示。针对保密信息涉及的任何许可、著作权、专利或知识产权，均不构成承包商向分包商的转移、授予或默示。所有保密信息均始终为承包商的独占财产。

4.2 Return or Destruction of Data / 资料归还或销毁
Within ten (10) days upon the written demand of the Contractor, or immediately upon the abandonment of the potential cooperation, the Subcontractor shall return all tangible media containing Confidential Information and permanently delete or destroy all documents, files, data, and copies thereof. The Subcontractor shall deliver a formal corporate written certification of complete destruction within five (5) days following such action, except that one copy may be retained strictly for legal archival purposes to verify compliance under Section 6.0.
在承包商书面要求后的十（10）天内，或在潜在合作终止时，分包商应立即归还包含保密信息的所有有形介质，并永久删除或销毁所有文件、数据及其副本。分包商应在销毁完成后五（5）日内交付一份正式的公司级书面销毁证明，但允许保留一份副本仅用于依据第 6.0 条进行法律存档以验证合规性。

5.0 REMEDIES & INJUNCTIVE RELIEF / 救济与禁令机制

5.1 Irreparable Harm / 不可弥补损害
The Subcontractor explicitly acknowledges that any unauthorized disclosure or competitive use of the Confidential Information will cause immediate, irreparable commercial harm, critical competitive exposure, and severe financial losses to the Contractor.
分包商明确确认，任何针对保密信息的未经授权的披露或竞争性利用，均会对承包商造成即时的、不可弥补的商业损害、核心竞争敞口暴露及严重的财务损失。

5.2 Injunctive Relief / 禁令救济
The Parties agree that monetary damages alone may be an inadequate remedy for breach. In the event of any actual or threatened breach of this Agreement by the Subcontractor, the Contractor shall be entitled to seek immediate injunctive relief, temporary restraining orders, or specific performance from any court of competent jurisdiction to block such disclosure, without the necessity of posting a bond or proving actual financial damages.
双方同意，针对违约行为，仅凭金钱损害赔偿可能不足以作为救济措施。若分包商发生任何实际或潜在违反本协议的行为，承包商有权向任何有管辖权的法院寻求即时禁令救济、临时限制令或实际履行，以拦截该等泄密行为，且无需提供担保，亦无需证明实际经济损失。

6.0 GOVERNING LAW & DISPUTE RESOLUTION / 法律适用与争议管辖

6.1 Governing Law / 法律管辖
This Agreement shall be governed by, interpreted, and implemented in all respects in accordance with the laws of the Emirate of Abu Dhabi and the Federal Laws of the United Arab Emirates, without giving effect to any conflict of law principles.
本协议在所有方面均应受阿联酋阿布扎比酋长国法律及阿联酋联邦法律管辖，并据其进行诠释和实施，排除冲突法原则。

6.2 Dispute Resolution / 争议管辖
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, interpretation, performance, or breach, which cannot be resolved amicably through friendly consultation within thirty (30) days, shall be submitted exclusively to the jurisdiction of the Courts of the Emirate of Abu Dhabi, UAE for final litigation.
因本协议引起或与之相关的任何争议（包括关于其存在、有效性、诠释、履行或违约的任何问题），如果双方在三十（30）天内未能通过友好协商解决，均应排他性提交至阿联酋阿布扎比酋长国法院提起诉讼最终解决。

7.0 TERM & MISCELLANEOUS / 期限与附则

7.1 Survival Period / 保密期限的存续
The confidentiality and non-use obligations contained in this Agreement shall survive the termination of any technical proposals, commercial discussions, and negotiations between the Parties, and shall remain fully active, legally enforceable, and binding upon the Subcontractor for a period of five (5) years from the Effective Date.
本协议中所承担的保密和不使用义务，在双方之间任何技术提案、商务讨论及谈判往来的终止后仍然有效，并自生效日起五（5）年内对分包商持续保持完全的激活状态、法律强制执行力及约束力。

IN WITNESS WHEREOF, the Parties hereto have caused this Non-Disclosure Agreement to be executed by their duly authorized representatives as of the date first written above.

For and on behalf of Contractor / 代表承包商:
[[________] - Insert Contractor Corporate Name]
Signature by Legally Authorized Representative / 授权代表签字: ___________________________
Name / 姓名: [[________] - Insert Signatory Name]
Title / 职务: [[________] - Insert Signatory Title]
Date / 日期: [[________] - Insert Date]

For and on behalf of Subcontractor / 代表分包商:
[[________] - Insert Subcontractor Corporate Name]
Signature by Legally Authorized Representative / 授权代表签字: ___________________________
Name / 姓名: [[________] - Insert Signatory Name]
Title / 职务: [[________] - Insert Signatory Title]
Date / 日期: [[________] - Insert Date]
"""

# ---------------------------------------------------------------------------
# Placeholder mapping
# ---------------------------------------------------------------------------
PLACEHOLDER_MAP = {
    # 1.1
    "[[________] - Insert Date]": "effective_date",
    # 1.2
    "[[________] - Insert Contractor Legal Name]": "contractor_name",
    "[[________] - Insert Jurisdiction]": "contractor_jurisdiction",
    "[[________] - Insert Office Address]": "contractor_address",
    # 1.3
    "[[________] - Insert Subcontractor Legal Name]": "subcon_name",
    "[[________] - Insert Country of Incorporation]": "subcon_jurisdiction",
    "[[________] - Insert Subcontractor Address]": "subcon_address",
    # Signature block
    "[[________] - Insert Signatory Name]": "signatory_name",   # first=contractor, second=subcon
    "[[________] - Insert Signatory Title]": "signatory_title", # first=contractor, second=subcon
    "[[________] - Insert Contractor Corporate Name]": "contractor_name",
    "[[________] - Insert Subcontractor Corporate Name]": "subcon_name",
}


def validate_nda(text: str) -> dict:
    """Check whether all placeholders have been filled."""
    total = 0
    remaining = []
    for token in PLACEHOLDER_MAP:
        count = text.count(token)
        total += count
        if count > 0:
            remaining.append(token)
    return {
        "complete": len(remaining) == 0,
        "remaining": remaining,
        "count_total": total,
        "count_filled": total - len(remaining),
    }


def fill_nda(
    effective_date: str = "",
    contractor_name: str = "",
    contractor_jurisdiction: str = "",
    contractor_address: str = "",
    subcon_name: str = "",
    subcon_jurisdiction: str = "",
    subcon_address: str = "",
    contractor_signatory_name: str = "",
    contractor_signatory_title: str = "",
    subcon_signatory_name: str = "",
    subcon_signatory_title: str = "",
    signing_date: str = "",
) -> str:
    """Return a copy of the NDA with placeholder slots replaced."""
    text = NDA

    # 1.1 Effective date (month + day)
    if effective_date:
        parts = effective_date.split()
        if len(parts) >= 2:
            month, day = parts[0], parts[1]
            text = re.sub(
                r"\[\[________\] - Insert Date\]",
                f"{month} {day}", text, count=1
            )

    # Unique tokens
    replacements = {
        "[[________] - Insert Contractor Legal Name]": contractor_name,
        "[[________] - Insert Jurisdiction]": contractor_jurisdiction,
        "[[________] - Insert Office Address]": contractor_address,
        "[[________] - Insert Subcontractor Legal Name]": subcon_name,
        "[[________] - Insert Country of Incorporation]": subcon_jurisdiction,
        "[[________] - Insert Subcontractor Address]": subcon_address,
        "[[________] - Insert Contractor Corporate Name]": contractor_name,
        "[[________] - Insert Subcontractor Corporate Name]": subcon_name,
    }

    for token, value in replacements.items():
        if value:
            text = text.replace(token, value)

    # Signatory names/titles — fill first occurrence = contractor, second = subcon
    if contractor_signatory_name:
        text = text.replace(
            "[[________] - Insert Signatory Name]",
            contractor_signatory_name, 1,
        )
    if subcon_signatory_name:
        text = text.replace(
            "[[________] - Insert Signatory Name]",
            subcon_signatory_name, 1,
        )
    if contractor_signatory_title:
        text = text.replace(
            "[[________] - Insert Signatory Title]",
            contractor_signatory_title, 1,
        )
    if subcon_signatory_title:
        text = text.replace(
            "[[________] - Insert Signatory Title]",
            subcon_signatory_title, 1,
        )

    # Remaining date tokens
    if signing_date:
        text = text.replace("[[________] - Insert Date]", signing_date)

    return text


# ==============================================================================
# Quick self-test
# ==============================================================================
if __name__ == "__main__":
    v = validate_nda(NDA)
    print(f"Template: {v['count_total']} placeholders, complete={v['complete']}")

    filled = fill_nda(
        effective_date="15 July",
        contractor_name="Wison Energy Engineering (Hong Kong) Limited – Abu Dhabi",
        contractor_jurisdiction="Abu Dhabi and the United Arab Emirates",
        contractor_address="Floor 15, Ghaith Holding Tower, West 14_02 Building, Al Manhal, Abu Dhabi, U.A.E.",
        subcon_name="[Subcontractor Legal Name]",
        subcon_jurisdiction="[Country of Incorporation]",
        subcon_address="[Subcontractor Address]",
        contractor_signatory_name="[Signatory Name]",
        contractor_signatory_title="[Signatory Title]",
        subcon_signatory_name="",
        subcon_signatory_title="",
        signing_date="15 July 2026",
    )
    v2 = validate_nda(filled)
    print(f"Filled:  remaining={len(v2['remaining'])}, complete={v2['complete']}")

    # Script lives in D:\Documents\My Projects\scripts\docgen\ ; output goes to
    # the Wison Template deliverable folder (absolute path).
    out = os.path.join(r"D:\Wison\Project_Info\Wison Template", "nda_filled.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(filled)
    print(f"OK  Saved -> {out}")

> **[Architect Sync · 2026-07-13]** 本快照与已构建的 `AI_Knowledge/` 一致（R1–R5），当前实际状态略更进：
> - 思维层已建：`Commercial_Principles.md`（7 价值观）+ `Commercial_Philosophy.md`（思维 OS v0.1，待红线）。
> - **Phase 2 已 Freeze**（Contract / Party / Exposure / External Contract）。
> - 现进入 **Commercial DNA**：`COMMERCIAL_DNA.md` 已建 21 区 Canonical 框架；项目实例事实（Contract No 等）已入 `PROFILE.md`。
> - 权威文件索引见 [`index.md`](index.md)。本文件保留为项目定位快照。

# Project Identity

Project Name:
WISON ADNOC EPC Contract Intelligence System

Purpose:
Build a Commercial Risk Intelligence System for ADNOC EPC Contract Management.

This is NOT:
- Document repository
- OCR archive
- Procurement database
- Simple RAG search system

This IS:
A Contract Manager Expert System capable of:
- Risk allocation analysis
- Back-to-Back verification
- Contract obligation reasoning
- Exposure identification
- Variation / Claim analysis
- Payment entitlement reasoning
- Authority and Decision validation


---

# Project Background

Company:
WISON

Owner:
ADNOC

Project:
Ruwais Sulphur Granulation Plant (RSGP) Upgrade
Hail & Ghasha Project No.1005312
EPC Onshore Works

Contract No:
6000066707

Contract Model:
LSTK (Lump Sum Turnkey)

> ⚠ **Correction (2026-07-13 · FOA 已读)**：本节原述"零预付款"——**与 FOA p.5 不符**。FOA 载明 ADVANCE PAYMENT = YES, USD 68,620,528.60 (10%)。以 FOA 为准。

Commercial Environment:
ADNOC Group Engineering Standards (AGES)
Highly protective Owner contract model


---

# Core Design Philosophy

The system follows these principles:

1. Contract is not a document.
Contract is a Risk Allocation System.

2. Risk is the primary management object.

3. The expert thinks:

Risk →
Obligation →
Requirement →
Event →
Decision →
Commercial Consequence →
Exposure

4. Main Contract is the upstream source.

5. External Contracts must be checked for Back-to-Back risk transfer.

6. Evidence is required for every conclusion.

7. Facts, Knowledge and Reasoning must remain separated.


---

# Current Architecture Status

AI_Knowledge/

CONSTITUTION.md
- 8 principles
- Highest governance rules

ONTOLOGY.md
- Canonical Model
- Risk Flow Main Axis
- Party Model
- Event Model
- Decision Model
- Exposure Model

COMMERCIAL_DNA.md
- Phase 3 target
- Commercial thinking framework

CAPABILITIES.md
- Expert capability testing


---

# Current Ontology

## Main Relationship Chain

Employer

↓

Main Contract

↓

WISON (Contractor)

↓

External Contract

↓

Subcontractor / Third Party

↓

Requirement

↓

Execution

↓

Evidence

↓

Decision

↓

Commercial Consequence

↓

Exposure

↓

Claim / Payment / Closeout


---

# Entity Status

Completed:

## Contract
Concept:
Contract = Risk Allocation Carrier

Functions:
- Allocate risk
- Create obligations
- Create requirements
- Define commercial mechanism


## Party

Model:

Organization

×

Role

×

Authority

×

Person


Authority controls:

- Instruction
- Variation approval
- Payment approval
- Completion certification
- Claim decision


## Exposure

Exposure states:

- Covered
- Partial
- Uncovered
- Crystallised


## External Contract

Includes:

- Subcontract
- PO
- Vendor agreement
- Supplier agreement
- Inspection agreement
- Rental
- Third party agreement

Question:

Does it transfer upstream risk?


---

# Important Design Decisions

## Procurement

Decision:

Procurement is NOT a core ontology domain.

Reason:

Project objective is Contract Management, not Procurement Management.

Procurement is treated as:

Execution Process supporting Contract.


---

## PO

Decision:

PO is not a separate commercial universe.

PO is treated as:

A contractual commitment under External Contract.

Importance is lower than Subcontract in this project.


---

## Vendor

Decision:

Vendor is not a separate entity.

Use:

Party + Role.

Vendor/Supplier/OEM/Third Party are external parties.


---

## Back-to-Back

Critical Rule:

Back-to-Back is not only a relationship.

It is a Rule Engine.

Purpose:

Detect:

Upstream liability

↓

Missing downstream transfer

↓

Commercial Exposure


Example:

Main Contract LD = 10%

Subcontract LD missing

Result:

Uncovered Exposure


---

# Current Phase

Phase 2:
Entity Concept Modelling

Status:

Contract ✅
Party ✅
Exposure ✅
External Contract ✅

Phase 2 is approaching freeze.

Do NOT endlessly add entities.

Next transition:

Phase 3

Commercial DNA / Commercial Philosophy


---

# Next Planned Work

Priority:

1.
Create Commercial Philosophy

Before reading clauses.

Purpose:

Teach AI how an ADNOC EPC Contract Manager thinks.


2.
Build Commercial DNA

21 key areas:

- Contract Type
- Risk Allocation
- Payment Philosophy
- LD Philosophy
- Security
- Warranty
- Variation Logic
- Notice Logic
- Acceptance Logic
- Liability
- Insurance
- Sanctions
- Export Control
- Jurisdiction
- Dispute
etc.


3.
Only after DNA:

Read Main Contract

Extract:

Clause

↓

Risk

↓

Exposure

↓

Rule

↓

Evidence


---

# Important Working Rules

DO NOT:

- Delete original documents
- Rename original documents casually
- OCR everything first
- Build summaries before ontology
- Create entities only because documents exist


Always ask:

"Does this help the Contract Manager make a decision?"


---

# Current Collaboration Role

ChatGPT acts as:

Knowledge Architect

Not:
- Document summarizer
- OCR assistant
- File organizer


Responsibilities:

- Challenge architecture
- Maintain Canonical before Instance principle
- Prevent over-engineering
- Maintain Risk Flow logic
- Convert experience into reusable expert rules
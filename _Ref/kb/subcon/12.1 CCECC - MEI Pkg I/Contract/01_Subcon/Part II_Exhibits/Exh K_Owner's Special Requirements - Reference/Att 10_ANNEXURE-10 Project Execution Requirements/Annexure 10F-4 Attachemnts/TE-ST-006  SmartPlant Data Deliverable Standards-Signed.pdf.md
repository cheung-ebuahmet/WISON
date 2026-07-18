ADNOC Classification: Internal
SMARTPLANT DATA DELIVERABLE STANDARD
CONTROLLED INTRANET COPY
The Intranet copy of this document is the only controlled document. Copies or extracts of this
document, which have been downloaded from the Intranet, are uncontrolled copies and cannot be
guaranteed to be the latest version.
“This standards supersedes TT-ST-002”
REV
DATE SUMMARY OF CHANGES
NO.
0 Jan 2021 First issue
AUTHORIZATION SIGNATURE
Approved by:
VP(TE)
Endorsed by:
TES
Reviewed by:
TESA
Prepared by:
TESA/SP2
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 1 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
CONTENTS
Table of Contents
1. INTRODUCTION ....................................................................................................................... 5
2. OBJECTIVE .............................................................................................................................. 5
3. SCOPE ...................................................................................................................................... 5
4. ABBREVIATIONS, DEFINITIONS & REFERENCES .............................................................. 5
4.1 ABBREVIATIONS ......................................................................................................... 5
4.2 DEFINITIONS ................................................................................................................ 6
4.3 REFERENCES .............................................................................................................. 8
5 INTERRELATIONSHIPS & CUSTOMERS ............................................................................... 9
6 SMARTPLANT APPLICATIONS OVERVIEW ......................................................................... 9
6.1 SMART P&ID ................................................................................................................. 9
6.2 SMART INSTRUMENTATION ...................................................................................... 9
6.3 SMART ELECTRICAL ................................................................................................ 10
6.4 SMART 3D ................................................................................................................... 10
6.5 SMARTPLANT FOUNDATION ................ ................................................................... 11
7 SMARTPLANT APPLICATIONS GENERAL REQUIREMENTS ........................................... 13
7.1 LEVEL OF DETAIL ..................................................................................................... 13
7.2 SOFTWARE VERSION ............................................................................................... 13
7.3 ORACLE DATABASE CHARACTER SET ................................................................. 13
7.4 PLANT BREAKDOWN STRUCTURE ........................................................................ 14
7.5 LOGO DEFINITION ..................................................................................................... 14
7.6 BORDER TEMPLATE ................................................................................................. 14
7.7 SMARTPLANT APPLICATIONS DOCUMENTATION ............................................... 15
7.7.1 SMARTPLANT APPLICATION IMPLEMENTATION PLAN ................................ 16
7.7.2 SMARTPLANT APPLICATION CUSTOMIZATION DOCUMENT ....................... 16
7.7.3 EXCEPTIONS AND DEVIATIONS DOCUMENT ................................................ 16
7.8 SYMBOLS\REFERENCE DATA\SEED FILES ........................................................... 16
7.9 SMARTPLANT REFERENCE DATA CHANGE MANAGEMENT .............................. 17
7.10 TAG CLASSIFICATION .............................................................................................. 18
7.11 DATA TAGGING ......................................................................................................... 18
7.12 TAG RELATIONSHIPS ............................................................................................... 19
7.13 SMARTPLANT APPLICATION DATA FROM SUBCONTRACTORS ....................... 19
7.14 NON-SMARTPLANT DELIVERABLE INTEGRATION .............................................. 19
7.15 INTELLECTUAL PROPERTY RIGHTS (IPR) ............................................................. 20
7.16 OWNERSHIP OF PROJECT DATA ............................................................................ 20
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 2 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
7.17 DATA CHECKS AND CLEANUP ............................................................................... 20
7.18 TRAINING .................................................................................................................... 20
8 SMARTPLANT APPLICATION SPECIFIC REQUIREMENTS .............................................. 21
8.1 SMARTPLANT FOUNDATION ................................................................................... 21
8.1.1 GENERAL ............................................................................................................ 21
8.1.2 PUBLISHED DATA FROM SPID TO SPF: .......................................................... 22
8.1.3 PUBLISHED DATA FROM SPEL TO SPF: ......................................................... 23
8.1.4 PUBLISHED DATA FROM SPI TO SPF: ............................................................ 24
8.1.5 PUBLISHED DATA FROM S3D TO SPF: ........................................................... 25
8.1.6 PUBLISHED 3D CONTENTS: ............................................................................. 26
8.1.7 INTEGRATION HIERARCHY LIMITATIONS ...................................................... 26
8.1.8 SCHEMA CHANGE MANAGEMENT .................................................................. 26
8.1.9 SCHEMA MAPPING ............................................................................................ 27
8.1.10 SCHEMA MODELLING WORKFLOW ................................................................. 27
8.1.11 DATA PUBLISHING AND RETRIEVING ............................................................. 28
8.1.12 RECOMMENDED PRACTICES FOR INTEGRATION ........................................ 28
8.1.13 REPORTS CUSTOMIZATION .......... ................................................................... 29
8.1.14 INCONSISTENCY REPORT ............................................................................... 29
8.1.15 NON PUBLISHED DATA ..................................................................................... 29
8.1.16 DATA VALIDATION, TRANSFORMING & LOADING (VTL) ............................... 30
8.1.17 SPF DELIVERABLES .......................................................................................... 31
8.2 SMART PIPING & INSTRUMENT DIAGRAM (SPID) ................................................ 32
8.2.1 GENERAL ............................................................................................................ 32
8.2.2 ORACLE DATABASE SETUP ............................................................................. 33
8.2.3 SPID PROJECT SETUP ...................................................................................... 33
8.2.4 MANDATORY ATTRIBUTES AND SPF PUBLISHING ....................................... 35
8.2.5 ATTRIBUTE ADDITION ....................................................................................... 36
8.2.6 OPTION MANAGER ............................................................................................ 38
8.2.7 ITEM TAG CUSTOMIZATION: ............................................................................ 38
8.2.8 REPORTS ............................................................................................................ 39
8.2.9 SYMBOL LEGEND .............................................................................................. 39
8.2.10 DATA CHECKS AND CLEANUP ......................................................................... 39
8.2.11 SPID DELIVERABLES ......................................................................................... 40
8.3 SMART INSTRUMENTATION (SPI) .......................................................................... 41
8.3.1 GENERAL GUIDELINES ..................................................................................... 42
8.3.2 DATABASE .......................................................................................................... 43
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 3 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.3.3 PROJECT SETUP ............................................................................................... 43
8.3.4 SPI FOLDER STRUCTURE ................................................................................ 44
8.3.5 USER GROUP DEFINITION AND ACCESS ....................................................... 45
8.3.6 NAMING CONVENTIONS ................................................................................... 45
8.3.7 USER DEFINED FIELDS AND TABLES LIST .................................................... 45
8.3.8 MANDATORY ATTRIBUTES AND SPF PUBLISHING ....................................... 47
8.3.9 REPORTS ............................................................................................................ 49
8.3.10 SPI DELIVERABLES ........................................................................................... 49
8.4 SMART ELECTRICAL (SPEL) ................................................................................... 50
8.4.1 GENERAL ............................................................................................................ 50
8.4.2 ORACLE DATABASE SETUP ............................................................................. 51
8.4.3 SPEL SERVER SETUP ....................................................................................... 51
8.4.4 USER GROUP DEFINITION AND ACCESS ....................................................... 53
8.4.5 NAMING CONVENTIONS ................................................................................... 53
8.4.6 CUSTOM FIELDS AND CUSTOM SELECT LIST ............................................... 54
8.4.7 MANDATORY ATTRIBUTES AND SPF PUBLISHING ....................................... 54
8.4.8 SMART ELECTRICAL DELIVERABLES ............................................................. 59
8.5 SMART 3D (S3D) ........................................................................................................ 60
8.5.1 GENERAL ............................................................................................................ 60
8.5.2 SMART 3D MANAGEMENT PROCEDURES ..................................................... 62
8.5.3 SMART 3D MODELING PROCEDURE .............................................................. 63
8.5.4 MODELLING REQUIREMENTS .......................................................................... 65
8.5.5 3D MODEL REVIEW GENERAL REQUIREMENTS ........................................... 70
8.5.6 3D MODEL REVIEW SCOPE .............................................................................. 72
8.5.7 NAMING RULES .................................................................................................. 78
8.5.8 ATTRIBUTES ....................................................................................................... 78
8.5.9 DRAWINGS & REPORTS ................................................................................... 78
8.5.10 S3D DOCUMENTS TO BE PUBLISHED IN SPF ................................................ 79
8.5.11 3D MODEL REVIEWS AND WALKTHROUGH ................................................... 79
8.5.12 DATA CHECKS & CLEANUP .............................................................................. 79
8.5.13 EXTRACTED DOCUMENTS ............................................................................... 80
8.5.14 S3D DELIVERABLES .......................................................................................... 81
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 4 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
1. INTRODUCTION
ADNOC Gas Processing is the operating COMPANY responsible for the processing of natural
gas and associated gas from onshore oil operations in the Emirate of Abu Dhabi. ADNOC
Gas Processing was incorporated in 1978 as a Joint Venture between Abu Dhabi National Oil
COMPANY (ADNOC), with a 68 per cent shareholding, Shell and Total, each with a 15 percent
shareholding, & Partex, with a remaining 2% shareholding.
The Gas Processing operations take place at our three main onshore plant locations: Asab,
Buhasa, and Habshan-Bab. ADNOC Gas Processing’s plants process and deliver a range of
gas products into the UAE’s gas distribution network and to the Ruwais Plant. These products
consist mainly of Methane (which primarily utilized as fuel in power plants and feedstock in
fertilizer plants), NGL (a mixture of Ethane, Propane, Butane, and Paraffinic Naphtha, which
is sent to the ADNOC Gas Processing’s Ruwais Plant for further fractionation), and
Condensate (which is sent to ADNOC Refining’s Ruwais Plant for processing/ export). As a
by-product from the Acid Gas, which is produced in operations, ADNOC Gas Processing
produces Sulphur. The Ruwais Plant processes the NGL from the desert plants to produce
Ethane, Propane, Butane, and Paraffinic Naphtha. Propane is further treated at the plant to
remove Sulphur components.
2. OBJECTIVE
To define the COMPANY requirements that will be followed by the CONTRACTOR while
executing the project using SmartPlant applications. Project criteria where SmartPlant
Application formats to be followed is specified into TT-ST-001 standard. The formats and
requirements mentioned in this Standard shall be followed during the development of Project's
Engineering deliverables and shall be handed over to COMPANY after project completion.
3. SCOPE
This Standard covers SmartPlant Data Deliverables requirements for Greenfield, Brownfield
and SmartPlant Conversion during select, define, execute and management of change phase.
4. ABBREVIATIONS, DEFINITIONS & REFERENCES
4.1 ABBREVIATIONS
Term Description
EPC Engineering, Procurement and Construction
FEED Front End Engineering Design
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 5 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Hexagon Application Vendor
SP Service Pack
SPE SmartPlant® Enterprise
SPEL Smart® Electrical
SPEM Smart® Engineering Manager
SPI Smart® Instrumentation
SPF SmartPlant® Foundation
SPID Smart® Piping & Instrumentation Diagram
SPR Smart® Review
S3D Smart® 3D
SSK Smart Sketch®
OOTB Out of the Box
* Required field
YMD Year Month Date
RFI Request for Issue
EDMS Engineering Document Management System
DTC Desktop Client
FRS Functional Requirement Specification
FDS Functional Design Specification
ENS Engineering Numbering System
MOC Management of Change
IES Instrument Equipment Shelter
4.2 DEFINITIONS
General Definitions
The COMPANY is the party, which initiates the project and ultimately pays for its design and
construction. The COMPANY will generally specify the technical requirements. The
COMPANY may also include an agent or consultant authorized to act for, and on behalf of the
COMPANY.
The CONTRACTOR is the party(s), which carries out all, or part of the design, engineering,
procurement, construction, commissioning or management of the PROJECT.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 6 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
MANUFACTURER / SUPPLIER / VENDOR – The party(s) which manufactures and/or
supplies the material/equipment, and provides technical documents/drawings and services to
perform the duties specified by COMPANY/ CONTRACTOR.
Subcontractor – The party(s) which carries out all or part of the design, procurement,
installation and testing of the System(s)as specified by the CONTRACTOR/VENDOR.
The word shall is used to indicate that a provision is mandatory.
The word should is used to indicate that a provision is not mandatory, but recommended as
good practice.
Specific definitions
Term Definition
CAD Computer Aided Design
Class Term used to classify things, e.g., a class of an equipment type could be a “pump”.
CSV Comma Separated Value
Data Information to be manipulated by tools, e.g., Tag list & Properties, Maintenance
Routines, etc.
Discipline Field of expertise, e.g., Mechanical Engineering.
Document Information (Printed or Electronic) to be read by people, e.g., Reports,
Specifications, Data sheets, Drawings, etc.
Equipment Equipment is a physical object designed to perform a Tag function.
File A collection of information stored electronically under a specific name
Information The sum of documents and data.
Metadata Collection of attributes formats and structure belonging to data or documents. For
example, meta-data can describe data elements or attributes, (name, size, data
type, etc.); specify formats (length, fields, columns, etc.) and structure (where it is
located, how it is associated, ownership, etc.). Metadata may include descriptive
information about the context, quality, condition or other characteristics of the data
or documents.
Package, Preassembled collection of equipment designed to deliver a process function.
Packaged
Unit
PBS Plant Breakdown Structure
P&ID Piping & Instrumentation Diagram
Plant A plant is an assembly of Equipment’s assembled to perform a physical or
chemical process (This includes the processes of transportation and storage of
materials).
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 7 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
A Plant represents the "high level" function to be performed, and during the design,
a Plant is decomposed in Process Units and Tags.
Area A n Area represents a part of the geographical surface occupied by a Plant. Areas
are created to identify the physical location of Equipment within a Plant.
Process Process Units are created to decompose the "high level" Plant function into more
Unit granular "sub-functions". This plant breakdown structure is used by the process
engineer.
Revision A code used to identify the content of a document at a certain point in time. It is
used to track the evolution of a document during its lifecycle.
SEED A seed file is term for a template. The beauty of the seed file is that it can be used to
standardize all new drawings that you create.
Sheet A sheet is a single piece of paper and is often a one-sheet drawing.
Site A site represents a geographical surface that can be identified on a map.
DWG AutoCAD Drawing file extension
DGN MicroStation Drawing file extension
4.3 REFERENCES
The following ADNOC Gas Processing documents are hereby referenced and are
considered part of SmartPlant Data Deliverable Standard.
Ref. Document Number Title / Description
TE-PR-063 Procedure for Numbering of Engineering Drawings &
(1)
Documents.
(2) TE-PR-050 As-Built Procedure
(3) TE-PR-064 Procedure for Tagging of Assets
(4) TT-ST-001 Engineering Data Deliverable Standard
(5) TE-PR-043 Asset information Handover Procedure
(6) OE-PR-026 Management of Change for Operate phase
(7) OE-PR-048 Management of Change for Project phase
(8) OE-PR-025 Critical Documents Management Procedure
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 8 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
5 INTERRELATIONSHIPS & CUSTOMERS
This standard is applicable to all ADNOC Gas Processing Business Units, ADNOC Business
Units, Transco, Contractors, Subcontractors and Manufacturers \ Suppliers involved in the
initiation, development and update of engineering information through SmartPlant
Applications.
6 SMARTPLANT APPLICATIONS OVERVIEW
6.1 SMART P&ID
OVERVIEW / PURPOSE / FUNCTION
Smart P&ID is an application that enables the creation of intelligent P&ID’s quickly and
accurately with embedded engineering intelligence that identifies items and the connectivity
between them, and validates completed items. Engineering tag information or labels, such
as Equipment, Pipeline and Instrument identifiers can be added as the items are created, or
added later via a two way data link to the SPI and SPEL applications, ensuring the progressive
development of P&ID’s and the engineering data in an efficient and controlled manner.
This application allows engineers to review changes and issue information for detailed
engineering, where the P&ID data forms the basis of their engineering datasheets, project
reports, and schematics.
SPP&ID forms part of the integrated engineering environment linked to other project
applications and management systems and is an important component in delivering initial key
information for effective data management, consistency of data, security of data origin,
change control across the engineering disciplines and project progress.
INPUTS / OUTPUTS, DELIVERABLES & DATA TRANSFER
The P&ID’s will be generated from a standard catalogue of intelligent symbols and rule based
functionality creating the plant process philosophy in a 2D graphical environment, which can
be validated automatically.
The Output of 2D drawings, Line Lists, Equipment Schedules, Instrument Schedules,
Discipline Datasheets, project reports and schematics from a single source of data in a
controlled environment, coupled with data transfers.
6.2 SMART INSTRUMENTATION
OVERVIEW / PURPOSE / FUNCTION
Smart Instrumentation provides a single source of instrumentation information that can be
easily accessed and updated, and ensures consistency across the different instrument tasks
and deliverables.
Smart Instrumentation provides information quickly and accurately from a single source of
data providing an efficient way to engineer and manage instrumentation and control systems.
Smart Instrumentation eliminates the need to search for information in multiple locations by
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 9 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
importing/exporting data from SmartPlant P&ID and SmartPlant Electrical, and controlling the
approval and issue process.
This application forms an external yet important part of the integrated engineering
environment linked to SmartPlant P&ID, Smart Electrical (limited extent) and is an important
component in providing single source information for effective data management, consistency
of data, security of data origin, change control within the Instrumentation discipline and
reporting progress.
INPUTS / OUTPUTS, DELIVERABLES & DATA TRANSFER
Input to Smart Instrumentation can be carried out manually or by download from SmartPlant
P&ID and SmartPlant Electrical, by competent instrument designers to a single database,
facilitating faster, concurrent engineering and reducing associated man hours and cost. Smart
Instrumentation also has the ability to exchange data with Vendors again saving time,
improving data quality and streamlining data distribution.
The output from Smart Instrumentation is varied and flexible via a browser and filter
mechanism, Instrument index, Datasheets, Wiring data, Loop drawings, Process data, Hook-
Ups, EDE Manager, Calculation and calibration data as well as construction information
6.3 SMART ELECTRICAL
OVERVIEW / PURPOSE / FUNCTION
Smart Electrical provides a single source of electrical information that can be easily accessed
and updated, and ensures consistency across the different electrical tasks and deliverables.
Smart Electrical provides information quickly and accurately from a single source of data
providing an efficient way to engineer and manage electrical related data and control systems.
Smart Electrical eliminates the need to search for information in multiple locations by
importing/exporting data from SmartPlant P&ID and Smart Instrumentation, and controlling
the approval and issue process.
This application forms an external yet important part of the integrated engineering
environment linked to SmartPlant P&ID, Smart Instrumentation (Limited extent) and is an
important component in providing single source information for effective data management,
consistency of data, security of data origin, change control within the Electrical discipline and
reporting progress.
INPUTS / OUTPUTS, DELIVERABLES & DATA TRANSFER
Input to Smart Electrical can be carried out manually or by download from SmartPlant P&ID
and Smart Instrumentation, by discipline designers to a single database, facilitating faster,
concurrent engineering and reducing associated man-hours and cost.
The output from Smart Electrical is varied and flexible producing Datasheets, Wiring data,
SLDs, cable block diagrams, O&M manuals and electrical Schematics, customized reports,
Equipment Load List, and related data as well as construction information
6.4 SMART 3D
OVERVIEW / PURPOSE / FUNCTION
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 10 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
The Smart 3D model plays a key role in the integrated engineering environment deployed on
the Project. The application provides a fully interactive, front-end 3D modeling environment
for multi-user, multi-discipline design, from basic study options to detailed production
information. This environment will also interface with other applications linking with 2D logical
engineering information in the Model Management System or output to 3rd party applications
such as CAESAR II for multi-discipline use.
The benefits of using the Smart 3D Model are:
 Single design environment used all disciplines
 Multi-discipline clash detection and resolution
 Improved design quality and accuracy
 Increased productivity
 Rapid decision making & Planning without site visit
 Reduced uncertainty across all the disciplines
 Reduced project and fabrication cost
INPUTS / OUTPUTS, DELIVERABLES & DATA TRANSFER
The competent multi-discipline design team will work immersively in the Smart 3D model using
the inherent functionality to develop the plant from the controlled and standardized catalogue
information held in the model databases. This will allow all disciplines to interact on an
immediate basis where change is encountered.
The design team will also link to the 2D logical data held within the Model Object Management
system.
Lead engineers and engineers will have the facility to review and comment on the evolving
design as it progresses, to ensure design quality and accuracy.
The Smart 3D model will produce:
 3D Model
 2D drawings (Isometrics, Piping, Instrumentation, Electrical, Civil & structural Layout,
Underground facilities & Detail drawings etc.)
 Material Reports, Clash Reports, Schedules, Equipment list, Instrument List, Valves list,
Piping Supports list, Line list etc.
 Data transfer to CAESAR II
 3D review models for design, construction, maintenance and operational meetings as well
as project personnel visualization of project development.
6.5 SMARTPLANT FOUNDATION
OVERVIEW / PURPOSE / FUNCTION
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 11 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
SmartPlant Foundation is industry-standard engineering information management application
providing the backbone for the common architecture that extends SmartPlant applications;
SPI, SPEL etc. SPF ensures an open, independent data storage system to protect plant
information for the life of the plant. It addresses all of the design, build, and operation
requirements of a facility throughout the entire plant life cycle. Designed for phased
implementation by Owner/Operators and EPCs, ISO 15926-compliant SPF encompasses the
plant's design, modifications, upgrades, and refurbishment, effectively managing the evolving
plant configuration from front-end engineering design to plant De-commissioning.
Capabilities Provided by SmartPlant Foundation
 Models and audits the evolving plant configuration.
 Stores all plant information against the familiar plant structure.
 Enables effective management of change by providing an overview of engineering changes,
tracking details and status of each change.
 Enables flexible search and retrieval of information via familiar plant terminology.
 Transfer of engineering data from one tool to another.
 Management of change resulting from ongoing engineering in upstream applications.
 Accessibility of engineering information to other collaborators without requiring the original
engineering tools.
 Recording of change in data as it moves through the plant lifecycle.
 Correlation of shared objects from multiple authoring tools.
 User-controlled or manual workflows for managed data exchange, including To Do Lists, e-
mail notifications, versioning, approval/release, and configuration control.
INPUTS / OUTPUTS, DELIVERABLES & DATA TRANSFER
By providing a platform that integrates the flow of information between applications, SPF helps
EPC Projects to improve global workshare, automate data re-entry costs and consistency
checks, effectively manage change, and minimize work duplication by notifying all interested
parties of pending or proposed work.
SPF offers cost reduction by simplifying data handover at project completion, thereby
accelerating the plant commissioning process, resulting in a shorter startup time, and earlier
commercial profitability.
Interfaces enable data to be fed in from design systems with relevant, standardized project
data, eliminating duplicated effort. Several interfaces are included with SmartPlant Reference
Data, including:
 Import comprehensive data from the Smart Instrumentation project database
 Import comprehensive data from the Smart Electrical project database
 Import comprehensive data from the Smart P&ID project database
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 12 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Import comprehensive data from the S3D project database
 Export/Import standardized data to the Livelink+ application
7 SMARTPLANT APPLICATIONS GENERAL REQUIREMENTS
This section describes common requirements to be followed for all SmartPlant Applications.
7.1 LEVEL OF DETAIL
The SmartPlant Applications database completion level must satisfy the requirements for
deliverables, project data collection and data transfer to other SmartPlant applications. The all
SmartPlant Applications Database must be as complete as possible to operate & maintain plant
after project completion. All warnings on the drawings & database must be cleared prior to
SmartPlant Applications Complete Handover.
7.2 SOFTWARE VERSION
Software Version will be advised during the tendering phase by ADNOC Gas Processing.
During Project execution if any update version\patch released by Software Vendor,
CONTRACTOR shall update engineering data as per released software version prior to
handover with prior approval from ADNOC Gas Processing. CONTRACTOR can do Software
Version update after FAT if Software Version update does not have major impact on Project
schedule subject to Project Management Consultancy Team approval.
7.3 ORACLE DATABASE CHARACTER SET
Database character set: AL32UTF8
NLS character set: AL16UTF16
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 13 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
7.4 PLANT BREAKDOWN STRUCTURE
The Plant Breakdown Structure (PBS) defines the hierarchy of Objects and the relationships
between them. A Plant Breakdown Structure (PBS) is a classified hierarchy with superiors or
roots and subordinates. For all SmartPlant Applications PBS shall be Plant-Area-Unit type.
Plant: A Plant represents the "high level" function to be performed, and during the design, a
Plant is decomposed in Process Areas and Units.
Area: An Area represents a part of the geographical surface occupied by a Plant. Areas are
created to identify the physical location of Equipment/ASSET within a Plant.
Unit: Units are created to decompose the "high level" Plant function into more granular "sub-
functions". In case more than one prime CONTRACTOR for EPC Project execution Plant will
be based on CONTRACTOR’s scope following under one site.
7.5 LOGO DEFINITION
The following logo shall be used together wit h the CONTRACTOR logo on all SmartPlant
deliverables,
Drawings Documents
7.6 BORDER TEMPLATE
Following ADNOC Gas Processing border file format shall be followed for all SmartPlant
Drawing Deliverable.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 14 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
7.7 SMARTPLANT APPLICATIONS DOCUMENTATION
CONTRACTOR shall develop minimum following documents for each SmartPlant Application
(SPID, SPI, SPEL & S3D) with listed content:
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 15 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
7.7.1 SMARTPLANT APPLICATION IMPLEMENTATION PLAN
SmartPlant Application Implementation Plan shall cover all aspects of application setup and
customization carried out during the Project execution for all types of projects. CONTRACTOR
shall prepare and submit this document for ADNOC Gas Processing approval at the start of
each phase. The minimum contents shall be:
 Roles & Responsibilities of Key SmartPlant Application Personnel (Administrators, Lead
designers, users)
 Setup information
 Plant Hierarchy (PBS) structure
 Reference Data implementation plan
 Instructions for Designers for use of correct Symbols, Labels to be used
 Instructions for resolving Inconsistencies
 Setup for Reports outputs
 SmartPlant Application Database & Deliverable checklist
 Backup Procedure
 Data maintenance procedure (such as Databa se constraint checks, database maintenance,
Duplicate Items check)
7.7.2 SMARTPLANT APPLICATION CUSTOMIZATION DOCUMENT
SmartPlant Application Customization Document shall keep record and track of SmartPlant
Application customizations during the each phase. The minimum contents shall be:
 A list of all customization that are applied to SmartPlant Application on completion of the EPC
phase.
 Details must be provided for each customization change and should include the requirement
for change, method of configuration, screenshots of changes made, ADNOC Gas Processing
approval date and comments.
7.7.3 EXCEPTIONS AND DEVIATIONS DOCUMENT
SmartPlant Application Exceptions and Deviations shall be accepted or resolved prior to final
SmartPlant Data handover. SmartPlant Application Exceptions and Deviations Document shall
keep record of all exceptions and deviations from SmartPlant Application Implementation Plan
during each phase. The minimum contents shall be:
 Details of deviations and exceptions from SmartPlant Application Implementation Plan.
 Details shall include Requirement of Exception/Deviation, Screenshots showing exact
deviations/exception. Date of Approval by ADNOC Gas Processing and Comments by ADNOC
Gas Processing.
7.8 SYMBOLS\REFERENCE DATA\SEED FILES
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 16 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
ADNOC Gas Processing will formally issue to the CONTRACTOR a set of basic reference data
(Out of the box applications Symbols\SEED Files\Drawing Templates) after the commencement
of the Contract. Any change, modifications, customization, addition, deletion required in the
basic Seed Files, CONTRACTOR must consult with COMPANY and shall obtain Reference
Data Customization approval from COMPANY. Based on COMPANY approval it is
CONTRACTOR responsibility to carry out all changes, modifications, customization, addition,
deletion.
The CONTRACTOR shall ensure that all information delivered to ADNOC Gas Processing
complies with this ADNOC Gas Processing reference data. ADNOC Gas Processing may revise
the reference data during the execution of the works. ADNOC Gas Processing shall formally
transmit any updates to the CONTRACTOR, highlighting any changes. The CONTRACTOR
shall update earlier revisions of the reference data and ensure future compliance with the new
revision of reference data prior to Handover subject to Project Management Consultancy Team
approval.
If the CONTRACTOR is unable to comply with any of the requirements resulting from the
application of the ADNOC Gas Processing’s reference data, the CONTRACTOR shall obtain
written permission from the COMPANY for any deviations.
7.9 SMARTPLANT REFERENCE DATA CHANGE MANAGEMENT
All changes (additions, modifications and deletions) of Reference Data during project phase
shall be managed and tracked using procedure described in this section.
 A log file is to be used for recording and tracking all reference data change requests. The
format of the log file is included in Appendix-1.
 If existing applications reference data is inadequate for engineering during EPC phase,
CONTRACTOR application Administrator shall send a change request to ADNOC Gas
Processing Application Specialist (TES). Supporting screenshots, symbols or files shall be
provided as required. All change requests should be submitted using the change request log
file.
 ADNOC Gas Processing Application Specialist (TES) shall review the request and provide
approval or alternative feedback. ADNOC Gas Processing engineering specialists (e.g.
Process, Piping, Instrumentation, Electrical & Civil\Structural engineers) will be consulted for
approval where required. Consultation shall be recorded and updated in change request log
file.
 CONTRACTOR application Administrator (as directed by the ADNOC Gas Processing
Application Specialist (TES)) shall update application reference data to reflect approved
change requests only.
 CODELIST: ADNOC Gas Processing is using standard library of CODELIST as per the
provided data dictionary template and additions CODELIST (e.g. Insulation Purpose, Fluid
code) required to be added through Reference data change management Procedure
 ADNOC Gas Processing is providing a SEED dataset for all SmartPlant applications.
CONTRACTOR is required to modify reference / plant data through Reference data change
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 17 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
management Procedure.
Figure 1 – Reference Data Change Management Procedure
ADNOC Gas Processing
CONTRACTOR
Asset Information Management
SmartPlant Application Specialist
(TESA)
Request for new symbol /
attribute.
Send details in log file
Reviews request along with supporting
documents.
Uses alternative
NO symbol/Attribute as
Approved suggested by ADNOC
Gas Processing
?
Application Specialist
YES
Updates log file Updates Reference
data
7.10 TAG CLASSIFICATION
The Tags can be classified into process and non-process tags. The process Tags are those
Tags that will be defined in engineering and design tools such as Smart PID (SPID) and Smart
Instrumentation (SPI), etc. These Tags will be published to the SmartPlant Foundation system.
Non process Tags are those Tags that are not created in the above mentioned engineering
tools, which are already TEF (The Engineering Framework) enabled, will be loaded into the SPF
system using a bulk load utility that heavily depends on the metadata PROVIDED WITHIN THE
EXCEL SPREAD SHEETS.
7.11 DATA TAGGING
A Tag is defined as the unique identifier/label of any item within the Plant. All objects shall be
tagged into all SmartPlant application database as per COMPANY asset tag numbering
procedure. Object types, which do not have tag-naming convention details into COMPANY
asset tag naming procedure CONTRACTOR shall propose the tag-numbering format via
request/TQ to COMPANY and based on approval tag the objects into SmartPlant database.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 18 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
7.12 TAG RELATIONSHIPS
Minimum typical relationships required to be extracted for the project information handover
includes, but not limited to the following:
 All Document types to Tags
 Relevant Tags to Buildings
 Relevant Tags to Purchase Orders
 Relevant Document types to Vendors
 Relevant Documents to Purchase Orders
 Relevant Document to Buildings
 Relevant Document to Classifications
 Relevant Document to Disciplines
 Relevant Tags to document
 Relevant Tags to manufacturer
 Relevant Tags to Supplier
 Relevant Tags to Tags
 Relevant Tags to Plant
 Relevant Tags to Area
 Relevant Tags to Unit
 Relevant Tags to tag classifications
 Relevant Documents to Documents
 Relevant each metadata attribute to objects
7.13 SMARTPLANT APPLICATION DATA FROM SUBCONTRACTORS
The CONTRACTOR is responsible to ensure all Data originated by the Subcontractors and
Manufacturer/Suppliers comply with the ADNOC Gas Processing’s SmartPlant application’s
Data requirements.
The CONTRACTOR shall be responsible for any additional effort or costs associated with
ensuring the Data supplied by the Subcontractors complies with the ADNOC Gas Processing’s
requirements without any loss of information & impact on Schedule.
7.14 NON-SMARTPLANT DELIVERABLE INTEGRATION
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 19 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
In order to link Non-SmartPlant deliverables to the SPF system, CONTRACTOR must integrate
all documents with required Metadata attributes. The CONTRACTOR must utilize ADNOC Gas
Processing EDMS template as the mechanism for delivery of metadata to ADNOC Gas
Processing even though the delivered metadata exist in CONTRACTOR’s own internal EDMS
system. Document and files which will not uploaded in SPF CONTRACTOR shall provide all
metadata as per COMPANY requirements along with document files hyperlinking to COMPANY
and CONTRACTOR Shall carry out the upload in COMPANY drive storage ( OneDrive, Livelink
etc.) with metadata.
7.15 INTELLECTUAL PROPERTY RIGHTS (IPR)
The Intellectual Property Rights of all ADNOC Gas Processing’s Custom Applications/Modules
shall be considered proprietary to ADNOC Gas Processing. These customizations is not to be
shared with individuals/companies outside of Consultant’s organization unless ADNOC Gas
Processing has specifically provided either written consent allowing said individuals/companies
access to this information. Except ADNOC Group of companies who can reuse all ADNOC Gas
Processing’s Custom Applications/Modules, however implementation/training charges will be at
the cost of each COMPANY depending on scope of work.
7.16 OWNERSHIP OF PROJECT DATA
ADNOC Gas Processing will retain full ownership of SmartPlant Applications data during
lifecycle of the project (From concept to Decommissioning) and can provide this data to any
other CONTRACTOR for future update & modification as required.
7.17 DATA CHECKS AND CLEANUP
CONTRACTOR shall ensure to meet the following minimum database checks and clean-ups
guideline, prior to SmartPlant Application data handover.
 SmartPlant Applications database is free of any erroneous data.
 All SmartPlant Applications database inconsistencies shall be resolved prior to handover.
 All hyperlinked files shall be removed and converted in embedded objects prior to delivery.
 Interferences shall be resolved on a regular basis.
 Database Integrity checks shall be performed regularly and all inconsistencies shall be
resolved.
 Temporary files and directories shall be removed prior to delivery
 Database Consistency Check and Integrity reports shall run on Database on regular time
interval and shall be error free.
 All unused CAD Blocks, Title Blocks, Templates to be removed from Project Application
Directories.
7.18 TRAINING
CONTRACTOR shall provide training to Operate and maintain engineering data prior to
handover for 5 days. CONTRACTOR shall submit training plan after 60% Project completion.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 20 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Training plan shall align with the following requirements: Provide Data User training of
Engineering Applications specific to customizations implemented during the project.
 Instructor to be approved and accepted by ADNOC Gas Processing prior to training.
 Training material to be approved by ADNOC Gas Processing prior to training.
 ADNOC Gas Processing will monitor the training through customer survey.
 ADNOC Gas Processing has the right to replace the Instructor, if the person did not meet
80% of end user expectations.
8 SMARTPLANT APPLICATION SPECIFIC REQUIREMENTS
8.1 SMARTPLANT FOUNDATION
8.1.1 GENERAL
 The CONTRACTOR shall use SPF as a “Data Warehouse” in exchange of data across
applications.
 The CONTRACTOR must utilize SPF in an Integrated Environment with engineering tools,
serving as a “Data Warehouse” in exchange of data across applications.
 The CONTRACTOR must utilize SPF as the primary source for creating/reserving drawings
and its revisions.
 CONTRACTOR shall not create any new plant structure levels without prior approval from
ADNOC Gas Processing. Even in such cases, SPF’s publish and Retrieval’s mechanism
must be followed.
 The CONTRACTOR must ensure appropriate workflow procedure is followed for publish and
retrieve mechanism across engineering design tools with SPF as the backbone of
Integration. For example, first P&ID Drawing shall be retrieved from SPF into SPI, before
publish of an Instrument Index or Instrument Specification sheet.
 CONTRACTOR to ensure all documents and drawings published from engineering tools has
the associated border and title blocks in SPF.
 The CONTRACTOR must make every attempt to publish all the data (attributes) from
Engineering Tools associated with Tags and Documents/Drawings as defined by ADNOC
Gas Processing. This is to ensure that ADNOC Gas Processing receives the complete and
meaningful data as part of SPF deliverable.
 The CONTRACTOR must ensure and update Schema mapping between SPF and
Engineering tools to successfully accomplish publish/retrieve to SPF as per ADNOC Gas
Processing advice.
 The CONTRACTOR shall carry out random intelligent and non-intelligent navigation tests
from tags to documents/drawings and vice-versa irrespective of application source.
 The CONTRACTOR must deliver all Vendor/Supplier AS-BUILT (Sign Off) document in SPF
before the SAT (Site Acceptance test).
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 21 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 All the properties which have data in SmartPlant Engineering tools shall be published to SPF
in Application Vendor delivered OOTB classes.
 CONTRACTOR shall do mapping to the existing properties in SPF, if any custom properties
is required to be created in SPF Schema, it has to be created on the Product delivered
Interfaces.
 For Multi package contracts where multiple EPCs are working, all the CONTRACTORS will
use the same schema.
 Any Schema changes like new user-defined attributes or new/modify list of values must be
done with prior approval from ADNOC Gas Processing. The same shall be added to the
respective engineering tools schemas and schema mapping under appropriate categories
with ADNOC Gas Processing approval.
 In a multi package multi EPC project, if any particular EPC needs to modify the schema, it
has to be approved by ADNOC Gas Processing and these modifications will have to be
reflected in each EPC SPF system, so that final Integration with ADNOC Gas Processing
SPF system should not have any issues.
 CONTRACTOR must utilize SmartPlant Foundation Document Management all features to
submit all Documents to the ADNOC Gas Processing for review & approval.
 Manual Valve Tagging should be done in SP ID & same should be published in to SPF
 Unified schema is preconfigured with basic configurations in SPF DTC/WebClient.
CONTRACTOR shall create necessary configuration and customization in SPF like
Interfaces, Properties, EdgeDef, RelDef, Custom APIs (client and server), AccessGroup,
Roles, etc for successful data/relationships loading & publishing to SPF and its easy
navigation in SPF DTC/WebClient. Any modifications/update to Unified Schema needs to be
approved by COMPANY.
8.1.2 PUBLISHED DATA FROM SPID TO SPF:
 Equipment
 Equipment Components
 Nozzles
 Pipe Runs
 Piping Components
 Line List / Line Specification
 Instruments
 Instrument loops
 Signal Runs
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 22 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 PID Drawings
 DCS Function
In addition, the connectivity relationships to be published for these objects.
8.1.3 PUBLISHED DATA FROM SPEL TO SPF:
 Cable Schedule Reports
 Cable Routing / Trench (Start / End Info.)
 Electrical Signal I/O Lists
 Piping Speciality
 Instruments & Cabinets Requiring Electrical Power
 Single Line Diagrams & Schematics
 Electrical Equipment Datasheets
 Load list
 Any Excel Report
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 23 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.1.4 PUBLISHED DATA FROM SPI TO SPF:
 Browsers/EDE View
 Electrical Tag Signal Lists
 Instrumentation Requiring Power Supply
 Enhanced SmartLoop Reports and Diagrams
 Instrument Indexes
 Instrument Specification Sheets
 Hook-Ups
 Instrument Process Data Sheets
 Dimensional Data Sheets(DDP)
 Select Wiring Reports and Diagrams
 Wiring Diagram
 Cable schedule
 I / O List
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 24 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.1.5 PUBLISHED DATA FROM S3D TO SPF:
 Orthographic Drawings
 Structural Layout & Piping General arrangement drawings
 Reports
 Isometric Drawings
 3D Model & Data
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 25 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.1.6 PUBLISHED 3D CONTENTS:
The data is published with the 3D Model and contains the following:
 First class piping objects (including properties shown in Smart 3D)
 First class equipment objects (including properties shown in Smart 3D)
 Relationships between the graphic objects and the System, Assembly, and Space objects.
 Structural steel members, concrete structures, stairs, ladders, plates
 Plates, Stiffeners, Edge Reinforcements
 Published data includes HVAC, cableway, cables, cable lengths and routing status for the
retrieval by SmartPlant Electrical.
 CONTRACTOR shall not publish data to any custom class in SPF. And all the data to be
published in Application Vendor delivered classes.
8.1.7 INTEGRATION HIERARCHY LIMITATIONS
The integrated environment imposes the following limitations on custom hierarchies, based
on requirements from the authoring tools. This list includes the tool imposing each
restriction, so that customers can factor these limitations into their hierarchy setup based on
their current and future tool usage.
 The hierarchy must have a minimum of 3 levels. This limitation is imposed by Smart
Instrumentation.
 The names of hierarchy items cannot be changed once created. This limitation is imposed
by SmartPlant Foundation.
 The hierarchy scheme cannot be modified after the plant is created. This limitation is imposed
by Smart P&ID and SmartPlant Foundation.
 In PBS, Names of Area, Unit should match with the one present in SPF and Authoring Tools
(SPID, SPEL, S3D and SPI)
 Area and Description should not be more than 30 characters. This limitation is imposed by
Smart Instrumentation.
 Area and Unit shall be created as Area system and Unit system. This is imposed by S3D.
 The plant name must be unique within the current domain. This limitation is imposed by Smart
Instrumentation.
 Application Vendor recommends that the plant name be the same name across all authoring
tools.
 With SmartPlant Enterprise, all projects must use the same PBS hierarchy
8.1.8 SCHEMA CHANGE MANAGEMENT
CONTRACTOR’s request for creating a new SmartPlant attributes shall follow an approved
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 26 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Schema Change Management provided by the ADNOC Gas Processing, ADNOC Gas
Processing reserves the right to reject any change request in the schema.
Sr. No CONTRACTOR Date Attribute Details of Requirement Reference Supporting
Name Logged Name Documents (if any)
Sample Schema Change Management log is shown below:
Problems with Approval by Approval ADNOC Gas Schema Updated
Existing matching ADNOC Gas Date Processing By CONTRACTOR
Attribute (if any) Processing Documents (Yes/No)
(Yes/No)
8.1.9 SCHEMA MAPPING
SmartPlant integration is based on a publish/retrieve paradigm. Applications publish their
own data and retrieve data published by other applications. Publish and retrieve processes
are done by Mapping (in Schema) reference data among the different tools.
8.1.10 SCHEMA MODELLING WORKFLOW
CONTRACTOR shall follow below workflow for creating/editing reference data and
creating/editing SmartPlant schema. CONTRACTOR shall validate the schema before it is
loaded in the SPF Database.
Standard practice involves the steps below:
1. Add custom attributes in Tool databases.
2. Integrate SPF with Application tools
3. Check out CMF in the SPF Desktop Client and Launch Schema Editor
4. Synchronize tool map schema and tool metadata
5. Map objects or attributes if they already exist in SmartPlant schema
6. Create new objects or attributes if they don’t exist in SmartPlant Schema.
7. Map those tool schema objects into (publish) and out of (retrieve) the SmartPlant schema
8. Validate Tool Map Schema and SmartPlant schema.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 27 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
9. Resolve any inconsistencies in schemas.
10. Export the customizations done in CMF
11. Load the exported XML into SPF Database.
8.1.11 DATA PUBLISHING AND RETRIEVING
CONTRACTOR shall complete mapping the application tools attributes prior to SPF
publishing and retrieving activity.
CONTRACTOR shall conduct a publishing and retrieving test to check schema-mapping
consistency and data transfer between SPF and SPID.
8.1.12 RECOMMENDED PRACTICES FOR INTEGRATION
As a minimum, CONTRACTOR shall follow below recommended practices for SPE
Integration.
 Identify proper Interface for creating Tool custom attributes in SPF.
 Do not rename any select List entries in SPID.
 If a select list entry is not used then CONTRACTOR shall disable that select list entry and
create a new entry.
 Do not rename “Short Value” of piping components in SPID.
 Use Pipe Spec lookup utility between SPID and SP3D for validating piping materials class
with temperatures, pressures, and diameters assigned to the pipe run and to search
commodity codes for piping components.
 Do not renaming any Application Vendor delivered attributes in SPF.
 Follow proper naming structure for attributes to avoid duplicates.
 Prefix an identifier (e.g. ADNOC Gas Processing) to the names of all custom attributes in
SmartPlant schema.
 Use same Naming convention across all tools.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 28 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Ensure the SPE Publish, Retrieve and Run ToDoList task mechanism between SPE tools is
configured correctly.
 Verify that data is published and plant items are correlated in SPF.
 Obtain ADNOC Gas Processing’s approval prior to any modifications or additions.
8.1.13 REPORTS CUSTOMIZATION
CONTRACTOR shall generate required reports from respective application tools such as
SPID, SPI, SPEL and S3D. CONTRACTOR shall configure these reports in SPF based on
ADNOC Gas Processing requirements.
Reports can be run on an ad-hoc basis where the user can enter search criteria each time
as required. Ad hoc Reports are based on view definitions, which are in turn based on graph
definitions. The graph definition is a collection of edge definitions that represent a path
through the data model.
Once the system administrator has set up the necessary definitions, the user can login to
the Desktop client to generate a report.
8.1.14 INCONSISTENCY REPORT
SmartPlant Foundation has tools to review data inconsistencies and to view data as
published by each authoring tool within Sma rtPlant Foundation Desktop Client.
The separation of published information by application into published domains, coupled with
the correlation of like objects saved within shared domain, provides the ability to generate
inconsistency report.
CONTRACTOR shall configure Excel reports (Inconsistency reports) to be run on SPF TEF
Shared Objects.
CONTRACTOR shall configure proper access so that users can select a single shared
object or multiple shared objects in desktop client list view and all this report from the right-
click menu. The report is viewed in Excel, and the reports highlight the inconsistent
properties.
8.1.15 NON PUBLISHED DATA
Non-Published data consists of engineering documents and data not published from SPE
tools. Such Non-Published engineering (and vendor) documents and related plant items will
be loaded into SPF as Non-Published data.
CONTRACTOR shall follow below guidelines for Non-Published data:
 CONTRACTOR shall configure SPF to store and manage non-published data and
documents.
 CONTRACTOR shall configure all non-published classes, properties, select list,
relationships, etc. for all types of Documents.
 CONTRACTOR shall use standard templates, native files, (PDF, DWG, DGN, etc.) and
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 29 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
metadata information for loading non-published data into SmartPlant Foundation database.
 CONTRACTOR shall develop a utility for generating load files and validating against
metadata. This utility shall generate load files in SPF specific format (NLF format or XML
format) by reading the excel index file. These load files will be loaded into SPF system using
the SPF loader. The utility will have built-in rules to make sure that the pick list values
specified in the index file match with the values defined in SPF. This utility shall check if a
document is already loaded in the system, and create a new revision or a new document as
applicable.
 CONTRACTOR shall prepare load files to load relationships between non-published
documents and plant items into SPF.
 CONTRACTOR shall configure the numbering system for non-published data as per ADNOC
Gas Processing standard (Document No. TE-PR-063) for green field projects and shall use
"Plant specific numbering procedure" for Brown field projects.
 CONTRACTOR shall customize Forms, Methods, Conditions, Menu Structure, User Groups
and Access Permissions as per requirements.
 CONTRACTOR shall prepare and submit Non-Publish data user guide for ADNOC Gas
Processing.
 CONTRACTOR shall use Data Loader for loading data into SPF.
All Non-SPE documents/drawings which are generated outside SPE (ex: Civil Drawings,
Structural Fabrication, etc.) shall be published as Non Published data.
All the corresponding CAD files shall have rendered file available in LIVE LINK system, like
other project Documents which are not stored in SPF.
 Tags extracted from the Non-TEF documents are compared with that of the TEF Tags.
The unique tags (not present in TEF tags list) shall be loaded to SPF as Non-TEF Tags as
per the Tag classification.
Relevant relationships shall be captured in preparing the NON TEF metadata for SPF
loading (Refer 7.12)
8.1.16 DATA VALIDATION, TRANSFORMING & LOADING (VTL)
The CONTRACTOR must validate the data before handover, using VTL tool and shall
generate a report to ADNOC Gas Processing showing the data is validated and accurate.
Before final uploading of data, the CONTRACTOR must validate the data. CONTRACTOR
must handover the VTL software license and all load files.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 30 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.1.17 SPF DELIVERABLES
CONTRACTOR shall deliver SPF data to ADNOC Gas Processing as per the approved SPF
version. CONTRACTOR shall be responsible to eliminate any inconsistencies before and
after the upgrade of data to new version.
CONTRACTOR shall provide the following SPF deliverables:
Functional Requirement Specification document.
Functional Design Specification document.
Readme file to include contents/description of files, SPF version, Oracle Version,
Oracle Character Set and Oracle Table space name.
SPF Database dump
Export of CMF file (Schema)
SPF Vaults Backup
Copy of Schema folder and files of the entire component schemas under the Website
folder
Export configuration from Server Manager.
Any custom Dlls (server/client side) with source code and documentation to ensure
that SPF will work in an identical way when restored at ADNOC Gas Processing site.
Custom Schema (if any)
Any custom Templates with Macros created for Reports.
Any other load files, batch files, etc. that CONTRACTOR used for SPF configuration.
Data Loader
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 31 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Quick User Guide
8.2 SMART PIPING & INSTRUMENT DIAGRAM (SPID)
8.2.1 GENERAL
 The CONTRACTOR shall use Smart PID (SPID) software for the purpose of creating
intelligent P&ID drawings. The resulting P&ID database will be published, according to a
delivery schedule agreed upon between the ADNOC Gas Processing and the
CONTRACTOR. The exact method of publishing will depend on infrastructure and
connectivity speeds.
 The CONTRACTOR shall resolve all design inconsistencies in the P&IDs using the project
setup and SPID consistency rules.
 The CONTRACTOR shall fill in all attributes, to the fullest extent for all P&ID components
such as pipe runs, equipment, inline instruments, etc. This is to ensure that the ADNOC
Gas Processing receives the complete and meaningful P&ID data in SPID format.
 The CONTRACTOR shall extract P&ID Tag related attributes from equipment data sheets.
The CONTRACTOR shall extract P&ID related attributes from line designation table (Line
List).
 The CONTRACTOR shall ensure that P&ID instrument Tags will have association with the
appropriate instrument loops.
 The CONTRACTOR shall follow the ADNOC Gas Processing’s Tag naming conventions
for P&ID instrument tags, loop Tags, equipment tags and line tags.
 The CONTRACTOR shall follow their best design practices for putting P&ID face value
information such as annotations, descriptions, notes, sizes, etc.
 The CONTRACTOR shall remove all temporary drawings, items from stockpile test
drawings, test symbols and assemblies, temporary filters, reports, etc. from the SPID data
before delivery.
 The CONTRACTOR shall remove all items & stuff outside the drawing border before
delivering the SPID Database.
 The CONTRACTOR shall remove all Stockpile OPCs before handing over
 The CONTRACTOR shall ensure that the delivered SPID data is free of any database
exceptions and orphan entries. The CONTRACTOR shall run all appropriate utilities as
delivered with the software for identifying and resolving database issues.
 CONTRACTOR shall confirm exact VENDOR Package Details with ADNOC Gas
Processing after the issuance of Purchase Order.
 For Vendor Packages P&ID shall be in SPID format & shall be incorporated in SPID
database by CONTRACTOR.
 The CONTRACTOR shall AS-BUILT the P&ID data before its final delivery.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 32 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.2.2 ORACLE DATABASE SETUP
Smart PID shall be implemented on the latest version at EPC award stage with compatible
oracle database version and Operating system (e.g. Windows 2008 R2 64-bit / Oracle 11g R2
64-bit (11.2)).
Oracle Instance and Table space required for SPID is created on Oracle server as per the
steps given in Application Vendor installation guide. SPID project related database will reside
in this oracle Instance and Table Space.
8.2.3 SPID PROJECT SETUP
The Project setup activity involves creating the Site, Plant and PID schemas and Databases.
Below is the Snap shot of the Project Directory structure which needs to be created on a File
server
SITE CREATION: Site shall be created and con figured as follows:
Site Server Name SPPID_XXXX
Database Type Oracle
Database Instance Name SPPID
Table space Name SPPID
Temp Table space Name TEMP
Database user Name SPPID_XXXX
Database password SPPID_XXXX
Data Dictionary Table Space SPPID
Data Dictionary Temp Table space TEMP
Data Dictionary database User Name SPPID_XXXXd
Data Dictionary database Password SPPID_XXXXd
PLANT SETUP: Plant shall be created and configured as follows:
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 33 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Data Dictionary Customized Template as per the DDT
file provided in the CD
Hierarchy Hierarchy 7 (Plant/Area/Unit)
Plant Name XXXX
Table Space SPPID
Temp Table space TEMP
Database user Name XXXX
Database Password XXXX
Data Dictionary Table Space SPPID
Data Dictionary Temp Table space TEMP
Data Dictionary database User Name XXXXD
Data Dictionary database Password XXXXD
SmartPlant P&ID APPLICATION ASSOCIATION; when establishing Application Association,
the following configuration shall be followed:
Data Dictionary Customized Template as per the DDT
file provided in the CD
P&ID Reference Data Path SPPID Project reference data path
Table Space SPPID
Temp table space TEMP
Database user Name XXXXPID
Database Password XXXXPID
Data Dictionary Table Space SPPID
Data Dictionary Temp Table space TEMP
Data Dictionary database User Name XXXXPIDd
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 34 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Data Dictionary database Password XXXXPIDd
8.2.4 MANDATORY ATTRIBUTES AND SPF PUBLISHING
Following attributes shall be populated during SmartPlant P&ID development.
A. EQUIPMENT
 Item Tag
 Unit No
 Tag Prefix
 Tag Sequence Number
 Tag suffix
 Diameter
 Length
 Width
 Height
 Level
 Design pressure
 Design pressure Tube
 Design temperature Max
 Design temperature Min
 Design temperature Max Tube
 Design temperature Min Tube
 Operating pressure
 Operating Temperature
 Insulation
 Rated Power
B. INSTRUMENTS
 Item Tag.
 Measured Variable
 Instrument Type modifier
 Tag sequence No
 Tag suffix.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 35 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Failure Action
 Opening Action
C. PIPERUNS and PIPELINES
 Item Tag.
 Tag sequence No
 Fluid Code
 Tag suffix
 Design max pressure
 Design min pressure
 Design max temperature.
 Design min temperature.
 Stream out requirement
 Operating temperature.
 Operating pressure
 Pipe Material Class
 Diameter
 Insulation purpose
 Criticality Rating
D. SPID PLANTITEM DATA
 Equipment’s
 Instruments
 Instrument Loops Component
 Inline Instrument
 Pipe Runs,
 Signal Runs
 Piping Components
 Nozzles
8.2.5 ATTRIBUTE ADDITION
Apart from Application Vendor‘s delivered attributes, following attributes are created for the
different Database Item Type as per ADNOC Gas Processing requirement:
A. DRAWING
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 36 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal

| Attribute name                | Attribute Display name  |                  | Data Type  |
| ----------------------------- | ----------------------- | ---------------- | ---------- |
| ADNOC Gas Processing Drawing  | ADNOC                   | Gas  Processing  |            |
String(80)
Number  Drawing Number
B. EQUIPMENT
| Attribute name         | Attribute Display name  |     | Data Type    |
| ---------------------- | ----------------------- | --- | ------------ |
| Criticality Rating     | Criticality Rating      |     | String(20)   |
| EquipDataSheet Number  | EquipDataSheet Number   |     | String(40)   |
| Equipment Remark       | Equipment Remark        |     | String(240)  |
| Empty Weight           | Weight                  |     | Mass         |
C.  INSTRUMENT
| Attribute name  | Attribute Display name  |     | Data Type  |
| --------------- | ----------------------- | --- | ---------- |

| Instrument Remark  | Instrument Remark  |     | String(240)  |
| ------------------ | ------------------ | --- | ------------ |
D. PIPE RUN
| Attribute name      | Attribute Display Name  |     | Data Type   |
| ------------------- | ----------------------- | --- | ----------- |
| Criticality Rating  | Criticality Rating      |     | String(20)  |
Include In LineList  Include In LineList  Select list(Yes/No)
| Is Vent Or Drain   | Is Vent Or Drain   |     | Select list(Yes/No)  |
| ------------------ | ------------------ | --- | -------------------- |
| Line From          | Line From          |     | String(240)          |
| LineList Remark    | LineList Remark    |     | String(240)          |
| LineList Revision  | LineList Revision  |     | String(5)            |
| LineTo             | LineTo             |     | String(240)          |
| Test Type          | Test Type          |     | Select list          |
E. PIPING COMPONENT
| Attribute name  | Attribute Display name  |     | Data Type  |
| --------------- | ----------------------- | --- | ---------- |
Revision No.: 0  Jan. 2021  Document ID: TE-ST-006                                 Page 37 of 83

All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Tag Sequence No Tag Sequence No String(40)
Tag Suffix Tag Suffix String(40)
Tag Prefix Tag Prefix String(40)
8.2.6 OPTION MANAGER
Option Manager controls the appearance of a SPID drawing by selecting the Colors, line styles,
gapping styles and heat tracing styles. This also defines the location of symbols, rules, Template
files.
Following is the sample gapping with priority definition.
Following image shows the sample Symbology definition foe line style (pattern width and color)
The Settings are defined as shown in below:
8.2.7 ITEM TAG CUSTOMIZATION:
CONTRACTOR shall configure the Item Tag for minimum following items as per Procedure for
Tagging of Assets (TE-PR-008)
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 38 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Equipment
 Nozzle
 Pipe Line Numbering Format
 Piping Component
 Instrument
 Instrument Loop
 Manual valve
8.2.8 REPORTS
CONTRACTOR shall customize the Report Templates as per the format provided by ADNOC
Gas processing e.g. Line List Report. All Customized Template (e.g. Line List Report.) to be
saved in the SPID project report template location i.e. in the following path:
(…..\P&ID Reference Data\Report Files)
Note: CONTRACTOR shall provide all the custom reports used during the EPC phase at the
time of final delivery
8.2.9 SYMBOL LEGEND
CONTRACTOR shall follow the SYMBOL Legend Sheet provided by ADNOC Gas Processing
and changes to this LEGEND shall be incorporated according to the Reference data Change
request procedure in Appendix 1.
8.2.10 DATA CHECKS AND CLEANUP
Prior to data handover CONTRACTOR shall ensure that SPID drawings and data is not
corrupt and do not contain inconsistencies. All SPID inconsistencies shall be resolved by the
CONTRACTOR prior to handover. As a minimum, the following checks and cleanup shall be
performed:
 All linked files shall be removed and converted in embedded objects prior to delivery.
 SPID Database Constraint report shall be generated and all constraints shall be resolved.
 Clean Data Utility (DelOrpModItems.dll) shall be run
 Ensure that all drawings shall be up-to-date status
 All the inconsistencies shall be resolved from SPID drawings.
Please refer the following table for comments and justification in case of deviation:
Remark CONTRACTOR
Category Observation
(Yes/No) Comments
1 Off page connectors Any unpaired OPCs present in stockpile? Y/N
Any OPCs with Null Tags? Y/N
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 39 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
DBCleaup Performed? Y/N
Removed constrains as per
2 Data Clean up
Y/N
"Database Constraint Report”?
Any Plant Items like Piperun, Instrument
Loops & Package are present in Y/N
stockpile?
Any missing symbol from the Reference
Y/N
Data used in the drawing?
Any drawing with out of date status or in
recreate mode?
Out of Date status of
3 Y/N
P&ID Drawings
(Should not be a yellow mark) should be
updated.
8.2.11 SPID DELIVERABLES
CONTRACTOR shall ensure that SPID data does not have any data inconsistencies before
final delivery. CONTRACTOR shall adhere to the following guidelines for final SPID
deliverables:
 SPID data shall be As-Built as per approved P & ID Legend sheets.
 All drawings and reports within or extracted, using SPID, shall be updated with as-built
information.
 CONTRACTOR shall use the SmartPlant P&ID “Re-Create P&ID from Database”
functionality for each drawing before final handover to ADNOC Gas Processing.
 CONTRACTOR shall ensure that all deliverables, submitted to ADNOC Gas Processing
can be extracted from the restored backups.
 CONTRACTOR shall upgrade SPID data to ADNOC Gas Processing approved version
subject to Project Management Consultancy Team approval.
 CONTRACTOR shall be responsible to eliminate any inconsistencies in the upgrade
process to the SPID version approved by the ADNOC Gas Processing.
 CONTRACTOR shall be responsible to verify and convert all Plant Change Requests
(PCR) / received project documents in to SPID format until Project completion.
 CONTRACTOR shall perform physical verification for aboveground services, if required,
within the scope of boundary for the available set of drawings to check its correctness, in
order to satisfy the project requirements.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 40 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 CONTRACTOR shall submit a database consistency and health check report before and
after the upgrade.
 CONTRACTOR shall take responsibility, to validate the data, after upgrade, to the SPID
version approved by the ADNOC Gas Processing. Any inconsistency noticed during the
upgrade, shall be documented and provided to ADNOC Gas Processing.
 CONTRACTOR shall facilitate the ADNOC Gas Processing in uploading the data set at
ADNOC Gas Processing’s site. CONTRACTOR shall resolve any issues, which may arise
when ADNOC Gas Processing is evaluating the data, until the ‘Final Acceptance
Certification’ is obtained.
 CONTRACTOR shall provide all documents concerned with this project, in hardcopies,
PDF and native editable electronic formats (MS-Word, MS-Excel, etc.)
 Vendor Packages: All the Vendor Package P&IDs shall be redrawn in SPID by
CONTRACTOR with Vendor logo and approval as per ADNOC Gas Processing
requirement.
 CONTRACTOR shall submit the following deliverables. The following electronic
deliverables shall be made available on the CD media or USB disk.
Plant Backup file
ItemTagFormat.xml
Screen shot showing Folder structure used
Customized dll files along with source code and documentation
Readme file explaining contents/description of files, version of Smart P&ID,
SmartPlant Engineering Manager, Version of Oracle, Oracle Instance Name, Oracle
Character Set, Oracle Table space name.
In case SPID drawing extracted in AutoCAD/Microstation format provide all setup files
required (E.g. Acad.ini, Acad.dwg etc.)
List of deliverables from SPID (List of Drawings)
P&ID Drawings (PDF) and AutoCAD/ MicroStation formats
Handover folder structure to be created
Exception report to be provided
SR log details to be provided during handover
Issue log & TQ details to be provided
8.3 SMART INSTRUMENTATION (SPI)
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 41 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.3.1 GENERAL GUIDELINES
 The Contractor shall use Smart Instrumentation (SPI) software for the creation and
management of instrumentation database and deliverables.
 The CONTRACTOR shall customize all border file templates and title blocks for the various
SPI generated documents and reports to meet ADNOC Gas Processing’s border and title block
size, including applicable ADNOC Gas Processing’s CAD Standards for fonts, scale,
symbology, text sizes, drawing and tag numbering standard (Document No. TT-PR-001), etc.
The CONTRACTOR shall check with the ADNOC Gas Processing for the availability of the
relevant title block and borders so as to avoid having to reproduce them.
 The CONTRACTOR shall customize all Instrument Specification sheets to meet the ADNOC
Gas Processing’s instrument datasheet standard. The CONTRACTOR shall check with the
ADNOC Gas Processing, for the availability of these sheets so as to avoid having to reproduce
them.
 The CONTRACTOR shall set all preferences at a Domain level to ensure consistency in use
of the product and presentation of the reports.
 The CONTRACTOR shall store all reference data e.g., custom symbols, title blocks, hook-up
templates, in a single shared folder structure that is referenced by all users during the project.
 The CONTRACTOR shall generate all loop drawings using Enhanced Smart Loop functionality
available within SPI.
 Instrument mounting details shall be generated using the Hook up module and will meet the
ADNOC Gas Processing’s standard.
 The CONTRACTOR shall create required user-defined fields for relevant categories. A
summary of added attribute should be submitted as a separate document describing such
attributes.
 The CONTRACTOR shall create SPI project data complete in all respects covering the various
available modules such as Index, Process data, Calculation, Instrument Specifications, Wiring,
Loop drawing and Hook-up.
 A completed SPI database, along with all reference data, which will give the ADNOC Gas
Processing a capability of generating required instrument deliverables from within the SPI
database using SPI.
 The CONTRACTOR shall ensure that the delivered SPI data is free of any database exceptions
and orphan entries. The CONTRACTOR shall run all appropriate utilities as delivered with the
software for identifying and resolving database issues.
 The CONTRACTOR shall remove all test data, test CAD blocks, temporary browser views,
reports, etc. from the SPI data before delivery.
 The CONTRACTOR shall AS-BUILT the SPI data before its final delivery.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 42 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Instrument Index, I/O List, Specification (Data Sheet) Sheet report formats and other such
reports, as desired by ADNOC Gas Processing, shall be customized to match ADNOC Gas
Processing standards.
 Title blocks for outputs from the various SPI modules (Instrument Index, Wiring Module etc...)
shall be customized to match ADNOC Gas Processing standards.
 Border templates and title blocks for Instrument Loop Drawings and Hook-Up Drawings shall
be customized to match ADNOC Gas Processing standards.
 Enhanced Smart Report symbols, for Loop / Hook-Up drawings shall be customized to match
ADNOC Gas Processing standards.
 All applicable data for plant items (viz. Instrument, Panel, Cable etc. shall be filled. Please refer
mandatory attributes section for attribute data population details.
 The CONTRACTOR is required to ensure that the relevant instrument tags have association
with the appropriate instrument loops.
 Any template / symbol to be used on the project, if not already provided by ADNOC Gas
Processing have to be created by CONTRACTOR. Only on approval by ADNOC Gas
Processing has this to be implemented by CONTRACTOR.
 As far as possible content shown on Enhanced Smart Report drawings ( Loop Drawings / Hook-
Up drawings ) shall be intelligent i.e. labels, design value and properties shown. Use of non-
intelligent text and graphics shall be minimized.
 Specification (Data Sheet) Sheet, Loop Drawings and Hook-Up drawings from Vendor
Packages shall be incorporated in SPI by CONTRACTOR as per ADNOC Gas Processing
requirement.
 CONTRACTOR shall confirm exact VENDOR Package Details with ADNOC Gas Processing
after the issuance of Purchase order
8.3.2 DATABASE
Smart Instrumentation shall be implemented on a version, approved by the ADNOC Gas
Processing using the compatible version of Oracle, also confirmed by ADNOC Gas Processing.
Application Vendor recommends separate database instance for Smart Instrumentation. The
procedure for database instance creation has been described, in the ‘Smart Instrumentation
Installation Guide’. SPI project related data would reside in this oracle Instance.
8.3.3 PROJECT SETUP
Project server shall be created and configured as follows:
Project Name XXXX
Database Type ORACLE
Database Instance Name SPI
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 43 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Domain Name XXXX
Domain Schema Name XXXX
Domain Schema Password XXXX
Domain Type Engineering ADNOC Gas Processing
Index Table space Name XXXX
Admin Schema Login in_dbamn
Admin Schema Password in_dbamn
Database user Name System
Database password XXX
Database character set AL32UTF8
National Character set AL16UTF16
8.3.4 SPI FOLDER STRUCTURE
 Archive – stores archived files
 Backup – stores Watcom (Sybase SQL anywhere format) backup files
 CAD – stores CAD related blocks and files for Hook-Ups and Loops
 Drawings – stores drawing files.
 Import Data – stores data import files (Excel) acting as source data for bulk data import.
 RAD – stores ESL symbols and template layouts for creating ESL Hook-Ups and Loops.
 Refdata – contains all standard product files and project-specific files, particularly:
 Report Files – Excel report templates, standard and custom
 Symbols – Graphical symbol files
 Templates – Graphical Border files
 Other folders not in use for this project
 SPI_CELLS – stores Microstation CAD related files for Cell Libraries
 SPI_output – is used to save documents, files and drawings out of SPI. The files can be
moved to the required folder later.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 44 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.3.5 USER GROUP DEFINITION AND ACCESS
The following user groups / users can be defined in SPI,
 Administration (System Administrator)
 Administration (Domain Administrator)
 Instrument Engineer Group
 Instrument Designer Group
 Process Engineer Group
 Process Designer Group
 Operations/Commissioning User Group
8.3.6 NAMING CONVENTIONS
The naming conventions to be defined for minimum following Items based on ADNOC Gas
Processing Procedure for Tagging of Assets (TE-PR-008).
 Instrument (Conventional)
 Instrument (Foundation Fieldbus)
 Loop
 Device Panel
 Device Cable
 Panel
 Cable
 Wire End Naming Convention
 Control System Tag
8.3.7 USER DEFINED FIELDS AND TABLES LIST
User defined fields and User defined tables are generally accessed in the Administration
and Instrument Index module. These enable the user, to add custom attributes to the
SPI database. If required, CONTRACTOR has to propose the addition of such attributes. On
approval by ADNOC Gas Processing, this should be implemented and documented by
CONTRACTOR.
Unit of UOM
Properties Accuracy Default Values
Measure Flag
Ambient Temperature 1% °C, °K, 20°C
Area 0.1% mm2
Barometric Pressure 0.01% bar 1.013 bar
Base Pressure 0.1% bar 1.013 bar
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 45 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal

|                              |           | Unit of  | UOM       |                 |
| ---------------------------- | --------- | -------- | --------- | --------------- |
| Properties                   | Accuracy  |          |           | Default Values  |
|                              |           | Measure  | Flag      |                 |
| Base Temperature             | 10%       | °C       |           | 15.56°C         |
| Beta Ratio                   | 0.1%      |          |           |                 |
| Calibration Settings         | 0.1%      |          |           |                 |
| Compressibility Factor       | 1%        |          |           |                 |
| Electrical Conductivity      | 1%        | Siemens  |           |                 |
| Control Valve Coefficients   | 1%        |          |           |                 |
| Control Valve Cv and Ky      | 1%        |          |           |                 |
| Control Valve Opening        | 1%        | %        |           |                 |
| Critical Pressure            | 0.1%      | bar      | absolute  | 1 bar-a         |
| Density                      | 0.1%      | kg/m3    |           |                 |
| Design Pressure              | 1%        | bar      | gauge     |                 |
| Diameter                     | 0.1%      | in       |           |                 |

| Differential Pressure (for  |       |      |     |     |
| --------------------------- | ----- | ---- | --- | --- |
|                             | 0.1%  | bar  |     |     |
Control Valve)
| Differential Pressure (for DP  |       |      |     |     |
| ------------------------------ | ----- | ---- | --- | --- |
|                                | 0.1%  | bar  |     |     |
Instruments)
| Differential Range (for Flow)   | 0.1%  | mbar         |     |     |
| ------------------------------- | ----- | ------------ | --- | --- |
| Energy                          | 0.1%  | kJ           |     |     |
|                                 |       | kg/hr (Mass  |     |     |
| Flow                            | 0.1%  |              |     |     |
flow rate)
| Flow Meter Coefficients   | 0.1%  |      |     |     |
| ------------------------- | ----- | ---- | --- | --- |
| Frequency                 | 1%    | 1/s  |     |     |
m3/h
| Gas Flow        | 0.1%  |          | Normal  |     |
| --------------- | ----- | -------- | ------- | --- |
| Heat            | 0.1%  | kW       |         |     |
| Heat transfer   | 1%    | W/m2/°C  |         |     |
| Latent Heat     | 0.1%  | kJ/kg    |         |     |
| Length          | 0.1%  | mm,m,km  |         |     |
| Level           | 0.1%  | Mm       |         |     |
| Liquid Flow     | 0.1%  | m3/h     |         |     |
| Molecular Mass  | 0.1%  |          |         |     |
Revision No.: 0  Jan. 2021  Document ID: TE-ST-006                                 Page 46 of 83

All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal

|                            |           | Unit of   | UOM       |                 |
| -------------------------- | --------- | --------- | --------- | --------------- |
| Properties                 | Accuracy  |           |           | Default Values  |
|                            |           | Measure   | Flag      |                 |
| Other                      | 0.1%      |           |           |                 |
| Percentage                 | 1%        | %         |           |                 |
|                            |           | bar or m  | gauge or  |                 |
| Pressure                   | 0.1%      |           |           |                 |
|                            |           | bar       | abs       |                 |
| Relief Valve Coefficients  | 0.1%      |           |           |                 |
| Resistance/Length          | 0.1%      | Ohm/km    |           |                 |
|                            |           | bar or m  | gauge     |                 |
| Return Pressure            | 0.1%      |           |           |                 |
bar
| Return Temperature   | 0.1%  | °C          |     |     |
| -------------------- | ----- | ----------- | --- | --- |
| Sound Level          | 1%    | dBA         |     |     |
| Specific Gravity     | 1%    |             |     |     |
| Specific Heat        | 0.1%  | KJ/(kg/°C)  |     |     |
| Specific Heat Ratio  | 0.1%  |             |     |     |

| Steam Flow                | 0.1%  | kg/h  |           |     |
| ------------------------- | ----- | ----- | --------- | --- |
| Temperature               | 0.1%  | °C    |           |     |
| Thermowell Coefficients   | 1%    |       |           |     |
| Thermowell Length         | 0.1%  | mm    |           |     |
| Vapour Pressure           | 0.1%  | bar   | absolute  |     |
| Velocity                  | 1%    | m/s   |           |     |
| Viscosity (Dynamic)       | 1%    | Pa.S  |           |     |
| Volume                    | 0.1%  | m3    |           |     |
| Weight                    | 0.1%  | kg    |           |     |

8.3.8  MANDATORY ATTRIBUTES AND SPF PUBLISHING

Following attributes shall be populated during Smart Instrumentation  development.
A. Instrument:
  Tag Number
  Instrument Type
  Instrument Type Description
Revision No.: 0  Jan. 2021  Document ID: TE-ST-006                                 Page 47 of 83

All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Service
 Loop Name
 Loop Number
 Loop Service
 I/O Type Name
 Line No.
 P&ID
 Equipment Name
 Location
 Status
 Manufacturer Name
 Model Name
 Cable:
 Cable Name
 Cable Description
 End 1 Location
 End 2 Location
 Length
 Manufacturer
 Model
 Loop Drawing:
 Loop Drawing Document No.
 Hook-Up:
 Hook-Up Name
 Hook-Up Type
SPI documents are to be published to SPF.
 Instrument Indexes
 Instrument Process Data Sheets
 Instrument Specification Sheets
 Hook-Ups
 Browsers / EDE views
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 48 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Electrical Tag Signal List
 Enhanced Smart Loop Reports
 Instrumentation requiring Electrical Power Supply
 Wiring – Panel Strip Reports.
 Dimensional Data Sheet Reports
8.3.9 REPORTS
 CONTRACTOR shall customize the Report Templates (.psr format) as per the format
provided by ADNOC Gas Processing e.g. Instrument Index, I/O List Report.
 All Customized Template (e.g. . Instrument Index, I/O List Report.) to be saved in the SPI
project report template location i.e. in the following path:
 (…..\SPI\Report Files)
Note: CONTRACTOR shall provide all the custom reports (.psr format) used during the EPC
phase at the time of final delivery.
8.3.10 SPI DELIVERABLES
Smart Instrumentation Domain Backup file including Oracle Views for restoring custom
reports (.psr format).
All reference data including RAD folder, customized symbols, Title Blocks, Instrument
Hookup Templates/blocks, etc. used for the project.
A document specifying SPI version (including service pack number), any customization
carried out to SPI database, symbols and reports.
Document specifying accepted deviations from standard specification.
The electronic deliverables shall be made available on DVD media, complete with an
index.
Vendor Packages: All the vendor package deliverables shall be incorporated in SPI by
CONTRACTOR as per ADNOC Gas Processing requirement.
Hard copy in A3 size of all required deliverables as specified within the contract from
within the SPI database.
Pdf copies of all the final deliverables.
Handover folder structure to be created
Exception report to be provided
SR log details to be provided during handover
Issue log & TQ details to be provided
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 49 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.4 SMART ELECTRICAL (SPEL)
8.4.1 GENERAL
 The Contractor shall use Smart Electrical (SPEL) software for the creation and management
of electrical design data and deliverables.
 The Contractor shall always use the latest available at award of contract (ADNOC Gas
Processing accepted) software version of Smart Electrical to create all electrical data, SLDs
and schematics unless otherwise specified by the ADNOC Gas Processing.
 The Contractor must also use a compatible version of the Oracle database used by the
ADNOC Gas Processing.
 Border templates and title blocks for all SPEL generated documents and reports should be
customized to match the ADNOC Gas Processing border and title block size, including the
applicable ADNOC Gas Processing SPEL Standards for fonts, scale, symbology, text sizes,
drawing and tag numbering standards, etc. The Contractor shall check with the ADNOC Gas
Processing for the availability of the relevant title block and borders so as to avoid having to
reproduce them.
 The Contractor shall create an electrical reference database and the reference data
(symbols, schematic blocks, report templates, etc.) for use with SPEL drawings that will
comply with the ADNOC Gas Processing standards.
 The Contractor shall create new user defined attributes based on the project requirement.
The same shall be added to the data dictionary under relevant categories. A summary of
added attribute shall be submitted as a separate document describing such attributes.
 The Contractor shall follow the ADNOC Gas Processing tag naming conventions for various
electrical items like cable, motor, transformer, etc.
 The Contractor, ADNOC Opcos & Transco shall follow the best engineering design practices
for setting up SPEL consistency rules.
 The Contractor shall fill in all attributes, to the fullest extent for all indexed tags. This is to
ensure that the ADNOC Gas Processing receives the complete and meaningful SPEL
project database.
 The Contractor shall remove all temporary drawings, test drawings, test symbols, temporary
filters, reports, etc. from the SPEL data before delivery.
 The Contractor shall ensure that the delivered SPEL data is free of any database exceptions,
orphan entries.
 Border templates and title blocks for the Drawings / Documents shall be customized to match
ADNOC Gas Processing standards.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 50 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 All SLD symbols used in SLD generation shall be shown as per the electrical legend sheets
developed for Project.
 All Schematic symbols used in Schematic generation shall be shown to confirm to project
specifications.
 The contractor is required to ensure that the relevant Electrical tags have association with
the appropriate instrument loops.
 Any template / symbol to be used on the project, if not already provided by ADNOC Gas
Processing have to be created by CONTRACTOR. Only on approval by ADNOC Gas
Processing has this to be implemented by CONTRACTOR.
 As far as possible content shown on SLD / Schematic drawings shall be intelligent i.e. labels,
design value and properties shown. Use of non-intelligent text and graphics shall be
minimized.
 Vendor Packages: SLD’s, Schematic drawings from Vendor Packages shall be incorporated
in SPEL by CONTRACTOR as per ADNOC Gas Processing requirement.
 CONTRACTOR shall confirm exact VENDOR Package Details with ADNOC Gas
Processing after issuance of Package Purchase Order.
 The Contractor shall AS-BUILT the Electrical data before its final delivery based.
8.4.2 ORACLE DATABASE SETUP
Smart Electrical shall be implemented on a version, approved by the ADNOC Gas
Processing using the compatible version of Oracle, also confirmed by ADNOC Gas
Processing. Application Vendor recommends separate database instance for SmartPlant
Electrical. The procedure for database instance creation has been described, in the ‘Smart
Electrical Installation Guide’. SPEL project related data will reside in this oracle Instance.
8.4.3 SPEL SERVER SETUP
The Project setup activity involves creating the Site, Plant, Electrical and Reference schemas
and Databases. Below is a sample screenshot of the project directory structure, which needs
to be created on the Application (File) Server.
SITE CREATION; Site shall be created and configured as follows
Site Server Name SPEL_XXXX
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 51 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Database Type Oracle
Database Instance Name SPEL
Table space Name SPEL
Temp Table space Name TEMP
Database user Name SPEL_XXXX
Database password SPEL_XXXX
Data Dictionary Table Space SPEL
Data Dictionary Temp Table space TEMP
Data Dictionary database User Name SPEL_XXXXd
Data Dictionary database Password SPEL_XXXXd
PLANT SET- UP; Plant shall be created and co nfigured as follows
Data Dictionary Default to be used.
Hierarchy Hierarchy 7 (Plant/Area/Unit)
Plant Name XXXX
Table Space SPEL
Temp Table space TEMP
Database user Name XXXX
Database Password XXXX
Data Dictionary Table Space SPEL
Data Dictionary Temp Table space TEMP
Data Dictionary database User Name XXXXD
Data Dictionary database Password XXXXD
SMART ELECTRICAL APPLICATION ASSOCIATION; when establishing Application
Association, the following configuration shall be followed
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 52 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal

| Data Dictionary           |     |     |     | Default to be used.  |            |       |
| ------------------------- | --- | --- | --- | -------------------- | ---------- | ----- |
| SPEL Reference Data Path  |     |     |     | SPEL  Project        | reference  | data  |
path
| Table Space                       |            |           |       | SPEL     |     |     |
| --------------------------------- | ---------- | --------- | ----- | -------- | --- | --- |
| Temp table space                  |            |           |       | TEMP     |     |     |
| Database user Name                |            |           |       | XXXXEL   |     |     |
| Database Password                 |            |           |       | XXXXEL   |     |     |
| Data Dictionary Table Space       |            |           |       | SPEL     |     |     |
| Data Dictionary Temp Table space  |            |           |       | TEMP     |     |     |
| Electrical                        | Reference  | database  | User  | XXXXREF  |     |     |
Name
| Electrical  | Reference  | database  | Us er  | XXXXREF  |     |     |
| ----------- | ---------- | --------- | ------ | -------- | --- | --- |
Name
| Data Dictionary database User Name  |     |     |     | XXXXELD  |     |     |
| ----------------------------------- | --- | --- | --- | -------- | --- | --- |
| Data Dictionary database Password   |     |     |     | XXXXELD  |     |     |

8.4.4  USER GROUP DEFINITION AND ACCESS
The FOLLOWING PERMISSION GROUPS WILL BE CREATED AND ACCESS RIGHTS
CAN BE GIVEN TO THESE PERMISSION GROUPS. BASED ON ACCESS RIGHTS, USER
CAN CREATE OR MODIFY DATA IN SPEL.
  Administration ( SPADMIN )
  User ( SPUSER )
8.4.5  NAMING CONVENTIONS
The naming conventions to be defined for minimum following Items based on ADNOC Gas
Processing Procedure for Tagging of Assets (TE-PR-008).
  Motor
  Heaters
  Cable
  Converting Equipment (Transformers, UPS etc...)
Revision No.: 0  Jan. 2021  Document ID: TE-ST-006                                 Page 53 of 83

All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Offsite Power
 Generator
 Relays, Switches
 Power Distribution Board
 Bus
 Panel
 Instrument Enclosures
8.4.6 CUSTOM FIELDS AND CUSTOM SELECT LIST
Custom fields and Custom Select list are generally created in the Smart Electrical Data
Dictionary. These can be accessed from the Property Grid in SPEL. If required
CONTRACTOR has to propose the addition of such attributes. On approval by ADNOC Gas
Processing, this should be implemented and documented by CONTRACTOR.
8.4.7 MANDATORY ATTRIBUTES AND SPF PUBLISHING
CONTRACTOR to provide a list of attributes to be populated in SPEL. ADNOC Gas
Processing to approve this list and suggest new additions (if required).A sample list of
properties, for a Motor is listed below. CONTRACTOR has to provide such a list, of electrical
properties for an item, and get it approved from ADNOC Gas Processing.
A. Motor Attributes:
 Item Tag
 Rated Power
 Rated Voltage
 Operating Factor
 Break Power
 Supply
 Particular Power
 Frequency
 No. Of Poles
 Phase Arrangement
 LRC / FLA ratio
 Power Factor at 100%
 Power Factor at 75%
 Power Factor at 50%
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 54 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Efficiency at 100%
 Efficiency at 75%
 Efficiency at 50%
 Manufacturer
 Model
 FLA Full load current
 NDE/DE Bearing numbers
 Insulation Class
 IP protection
 Ex classification
 Serial Number
B. Heater Attributes:
 Item Tag
 Rated Power
 Absorbed Power
 Rated Voltage
 No. Of Poles
 Supply
 Frequency
 Demand Factor
 Phase Arrangement
 Power Factor at 100%
 Efficiency at 100%
 Power Factor at demand
 Efficiency at demand
 Manufacturer
 Model
C. Cable Attributes:
 Cable Tag
 Cable Description
 Cable Specification
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 55 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Reference Cable
 Conductor Arrangement
 Armour Type
 Outer Jacket Insulation
 Material
 Insulation
 Color Pattern
 Insulation Voltage Rating
 Insulation Temperature Rating
 Basic Ampacity in air
 Basic Ampacity in ground
 Estimated Length
 Design Length
 Routing Length
 Supply
 Rated Voltage
 No. Of Phases
 Full Load Current
 Starting Current
 Routing
 De-rating factor
 Utilization factor
 Voltage Drop ( Allowable at full load )
 Voltage Drop ( Allowable at starting )
D. Generator Attributes:
 Item Tag
 Rated Apparent Power
 Rated Active Power
 Power Factor
 Supply
 Rated Voltage
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 56 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 No. Of Phases
 Serial Number
 Efficiency
 Frequency
 No. Of Poles
 Manufacturer
 Model
E. Transformer Attributes:
 Item Tag
 Rated Power
 Rated Voltage
 Supply
 Frequency
 No. of Phases
 Phase Arrangement
 Secondary Output – 1 Rated Power
 Secondary Output – 1 Nominal Current
 Secondary Output – 1 Rated Voltage
 Secondary Output – 2 Rated Power
 Secondary Output – 2 Nominal Current
 Secondary Output – 2 Rated Voltage
 Manufacturer
 Model
 Short Circuit Impedance
 Cooling
 Method of connection and Standard.
 Temperature rise.
 Degree of protection IP
F. Bus Attributes:
 Item Tag
 Rated Current
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 57 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Rated Voltage
G. Panel Attributes:
 Item Tag
 Rated Voltage
 No. Of Phases
 Supply
 Frequency
 Phase Arrangement
 Manufacturer
 Model
H. Instrument Attributes:
 Item Tag
 Process Function
 Supply
 No. Of Phases
 Frequency
 Instrument Rated Power
 Power Factor
 Rated Voltage
 Manufacturer
 Model
I. SPEL documents
 Cable Schedule Reports
 Electrical Signal I/O List
 Excel Reports
 Instruments and Cabinets requiring electrical power supply
 Schematics
 Single Line Diagrams
 Interconnection Diagram
 O&M Manuals
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 58 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.4.8 SMART ELECTRICAL DELIVERABLES
CONTRACTOR shall ensure that SPEL data does not have any data inconsistencies before
final delivery. CONTRACTOR shall adhere to the following guidelines for final SPEL
deliverables:
 SPEL data shall be as built.
 All drawings and reports within or extracted, using SmartPlant Electrical, shall be updated
with as-built information.
 On SLDs all symbols and labels to be mapped and configured from the catalog manager
and SPEL database as Intelligent and no Manual mapping and configuration is
recommended.
 CONTRACTOR shall ensure that all deliverables, submitted to ADNOC Gas Processing can
be extracted from the restored backups.
 CONTRACTOR shall upgrade SPEL data to ADNOC Gas Processing approved version.
 CONTRACTOR shall be responsible to eliminate any inconsistencies in the upgrade
process, to the latest stable version. The CONTRACTOR shall seek approval, from the
ADNOC Gas Processing on the latest stable version.
 CONTRACTOR shall submit a database consistency and health check report before and
after the upgrade.
 SLDs designed in SPEL should be exported to AutoCAD/ MicroStation format
 CONTRACTOR shall take responsibility, to validate the data, after upgrade, to the SPEL
version approved by the ADNOC Gas Processing. Any inconsistency noticed during the
upgrade, shall be documented and provided to ADNOC Gas Processing.
 CONTRACTOR shall facilitate the ADNOC Gas Processing in uploading the data set at
ADNOC Gas Processing’s site. CONTRACTOR shall resolve any issues, which may arise
when ADNOC Gas Processing is evaluating the data, until the ‘Final Acceptance
Certification’ is obtained.
 CONTRACTOR shall provide all documents concerned with this project, in hardcopies, PDF
and native editable electronic formats (MS-Word, MS-Excel, etc.).
 Once the Final Handover is completed to ADNOC Gas Processing, ADNOC Gas Processing
shall retain full ownership of the project data after the handover and can provide this project
data to any other CONTRACTOR for future modification projects. ADNOC Gas Processing
owns the responsibility of the Data.
 SPEL Deliverables
List of Deliverables
Zip file backup: Plant backup and site backup (reference schema, templates, title blocks,
symbols, schematic blocks, formats, rules, etc.) used with SPEL project data.
Oracle DB dump: CONTRACTOR shall provide Oracle DB dump backup
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 59 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Screenshot showing folder structure used
Custom SLD Symbols and Border File Templates: CONTRACTOR shall deliver these symbols
and templates
Custom Schematic and Border File Templates: CONTRACTOR shall deliver these symbols
and templates
Customized Reports: CONTRACTOR shall provide these template reports
Custom Attribute / Symbol list: CONTRACTOR shall provide detailed report of customization
in case of new attributes and symbols
Generated SLD’s, Schematic, Reports and any such report that can be extracted from SPEL on
request by ADNOC Gas Processing. Hard copy of all such required deliverables shall be
provided by CONTRACTOR. Hard copy in A3 size of all required deliverables as specified within
the contract from within the SPEL database
Exception report to be provided
SR log details to be provided during handover
Issue log & TQ details to be provided
Pdf copies of all the final deliverables.
8.5 SMART 3D (S3D)
8.5.1 GENERAL
 The Contractor shall use Smart 3D software and associated software packages for the
creation and management of the 3D model, associated database and deliverables.
 The model shall be of the entire Plant, when handed over to the ADNOC Gas Processing.
The model shall be structured such that disciplines and where applicable sub-sets of
disciplines required by the ADNOC Gas Processing. Disciplines sub-sets of disciplines are
represented separately in the model by assigning levels or equivalent or making it
practicable to show graphically each level separately or combinations of the various
components of the Plant as required by ADNOC Gas Processing.
 The S3D Project (Plant) database name shall be the Project Name.
 The S3D piping specifications shall be created using the ADNOC Gas Processing
commodity codes.
 The Plant Breakdown Structure (System Hierarchy) for all disciplines shall be created as per
Contractor’s best design practices, but must comply with the project overall plant/area/unit
structure.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 60 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 The Contractor shall use their best design practices to determine additional attribute
requirements for equipment, pipe runs, etc.
 S3D reference data shall be customized for the ADNOC Gas Processing piping material
classes, piping commodity data, instrument data, specialty data, tap data, piping assemblies,
etc.
 All Pipe supports to be modelled physically.
 The Contractor shall assign tags for equipment, nozzles, line number, line ID, pipe supports,
columns, beams, etc., in accordance with the ADNOC Gas Processing Tag Numbering
System.
 The Contractor shall As-Build the S3D data before its final delivery based on the ADNOC
Gas Processing As-Built Procedure (EPR/ SVP (T)/0020).
 The scope lists the minimum content in each discipline. CONTRACTOR shall expand the
scope to meet EPC requirements.
 Consistency reports showing comparison between 3D model contents and data in SPID,
SPI and SPEL shall be submitted as and when required. These reports shall be configured
and extracted from SPF.
 Errors or conflicts between the scope described here and other ADNOC Gas Processing
documents shall be brought to the attention of ADNOC Gas Processing for resolution.
 CONTRACTOR shall obtain necessary project templates from ADNOC Gas Processing
required to complete the project in S3D.
 CONTRACTOR shall perform S3D modelling in an integrated environment with other SPE
tools (SPF, SPID, SPI and SPEL).
 CONTRACTOR shall publish 3D Model, Orthographic drawings with complete annotations,
isometric drawings, Pipe support drawings and all reports to SPF.
 CONTRACTOR shall follow the guidelines of SPF Integration section, particularly about
Plant Hierarchy, naming conventions & attributes.
 The 3D model and drawings shall be dimensionally 100% accurate.
 Working units indicated shall be maintained as specified in ADNOC Gas Processing
documents.
 CONTRACTOR shall AS-BUILT the S3D model, drawings & reports and upgrade data to
ADNOC Gas Processing approved S3D version before final handover.
 CONTRACTOR shall backup all bulk load excel files, source codes for symbols, rules,
support assemblies etc. for handover to ADNOC Gas Processing.
 Vendor packages: CONTRACTOR shall confirm the minimum list of Vendor Packages to be
modelled from ADNOC Gas Processing. The scope of modelling shall be the same as that
described for non-vendor packages3D Model reviews and Walkthrough.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 61 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.5.2 SMART 3D MANAGEMENT PROCEDURES
Contractor shall develop Smart 3D documents as per section 6.4 with following contents,
 Coordinates & Grids System Definitions.
 Model contents in each task & system.
 List of populated attributes.
 Reference Data implementation plan.
 Reference data changes approval procedure.
 Setup for Drawings & Reports task outputs (all customizations shall be listed here).
 List of drawings and reports from S3D.
 Clash checking & resolution procedure.
 Model maintenance procedure (such as integrity checks, database maintenance, TO DO
LIST etc.)
 Synchronization model with catalog.
 Workflow for Plant creation in S3D.
 SmartPlant Review procedure (area divisions, display sets and symbology details)
 S3D model validation procedure. This shall include a health checklist.
 List of all piping specifications.
 Electrical and instrument cable tray specifications.
 List of new structural sections and structural section tables.
 List of all symbols created for equipment, piping, electrical, supports etc. and their usage.
 Symbols dll file & source code file names.
 List of new attributes and their usage.
 List of customized orthographic, isometrics, and supports drawings templates, view styles,
etc.
 List of rules used and their usage.
 Rules dll files’ and source code file names.
 List of report templates and related files.
 System isometric as per requirement.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 62 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
8.5.3 SMART 3D MODELING PROCEDURE
CONTRACTOR shall submit this procedure for ADNOC Gas Processing approval before the
start of EPC phase of the project. S3D Modeling Procedure shall contain section-wise
modeling instructions for all the S3D tasks with minimum following contents,
MODELING INSTRUCTIONS FOR PIPING
 Pipeline system and pipe run creation instruction.
 Attributes populated by user.
 Piping parts.
 Line number change instructions (where to change a line number at outlets, flange points, weld
points etc.)
 Ownership and selection of gaskets and bolts at a changeover.
 Taps.
 Instrument and specialty item placement.
 Assembly placement.
 Sloped line.
 Future Piping.
 Pipe Supports
 Tie-in.
 Vessel trim.
 PSV.
 Orifice with taps.
 Instrument indicator.
 Isometric extraction, General arrangement drawing & Plot Plan extraction.
 Miscellaneous items such as Sample cooler, Sample cabinet, Firewater Hydrant, Monitors.
 Supports & populated attributes.
 Floor/Wall openings.
 HOLD items/No MTO.
 GRE/GRP piping.
 Open end (to atmosphere, to header etc.)
 Jacketed Piping-modeling procedure to be included. Isometric of jacketed lines should be
included in the deliverable list.
MODELING INSTRUCTIONS FOR EQUIPMENT
 Details of populated attributes
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 63 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Vertical vessel
 Horizontal vessel
 Platform with handrail, stair, ladder and cage.
 Pump.
 Tank.
 Heat Exchanger.
 Nozzles.
 Package Units
 Sump
 Compressor
 Coolers
 Ejectors
 Boilers
 Fire Heaters/Furnace
 Sample connection.
 Utility Hose stations and hose racks
 Fire Fighting Equipment (Safety showers, Eyewash stations etc.)
 All types of envelopes (maintenance, safety, access, escape path etc.).
 Davit, Deck crane, Monorail, EOT crane etc.
MODELING INSTRUCTIONS FOR CIVIL & STRUCTURAL
 Coordinate and grid system setup.
 Section tables.
 Primary, secondary & tertiary structures.
 Floors, slabs, walls and foundations.
 Guidelines for Plant buildings viz. Substations, IES and OMS
 Roads, paving, catch basin, Open ditch, pits, trenches, retaining walls. Volumes for
underground cables etc.
 Openings in floors and walls.
 Handrails, stairs and ladders.
 Bracings, gusset plates, stiffeners, connection plates etc.
 Fireproofing.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 64 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
MODELING INSTRUCTIONS FOR ELECTRICAL AND INSTRUMENTATION
 Cable trays & trenches (electrical & instrumentation).
 Telecom devices
 Lights and fixtures.
 Junctions boxes (electrical and instrumentation).
 Distribution panels.
 Panels.
 Local Control Stations
 Welding socket outlets
DRAWING GENERATION & REPORTS INSTRUCTIONS
 Volume placement for all types of drawings.
 Drawing and view creation procedures.
 Style selection instructions.
 Foundation / Underground Services Layouts
 Structural plan and elevation drawings
 Equipment Layout drawings.
 Cable tray layout drawings.
 Piping plan and general arrangement drawings.
 Pipe support drawings.
 Isometric drawings.
 Panel layout drawings.
 Reports instructions.
 All manual modifications/additions to the drawings
INTERFERENCE MANAGEMENT
 This section shall cover detailed instructions for interference resolution.
TO DO LIST MANAGEMENT
 This section shall cover detailed instructions for TO DO LIST resolution.
8.5.4 MODELLING REQUIREMENTS
The 3D modeling system must be able to produce required documents like isometrics, plan and
elevation drawings, etc., as well as piping material take-offs. Main objective of the 3D modeling
system must be the interference checking and data integrity to reduce the rework during
construction to an absolute minimum. The model shall be capable of executing interference
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 65 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
checks and generating reports of hard and soft clashes for resolution. Hard clashes refer to
actual physical interference of equipment, while soft clashes refer to interference with required
ergonomic space required for maintenance and operation purposes. Equipment and other
components and the space allocated shall be modeled to the extent necessary, and as further
described below, to ensure the validity of the clash check. Construction tolerances shall be
included in interference check. This means that all physical objects that need to be included in
drawings, reports and/or interference checking will need to be modeled. The Contractor shall
prepare a clash detection procedure, including all proposed construction tolerances and submit
to the ADNOC Gas Processing for acceptance. The modeling extent is, but not limited to, as
given below.
PIPING
 All process and utility piping, vents and drains, including all piping components for all sizes as
shown on the P&ID.
 Valves including hand wheels, actuators, and motor operators correct in orientation and actual
dimensions.
 Piping accessories like strainers filters and steam traps.
 Aboveground and Underground piping
 Additional Steam traps locations to be assigned in S3D
 Pipe supports, spring hangers and trunnions.
 Jacketed pipes
 Fire water Network
 Insulation – dimensionally correct around all in-line components.
 Steam tracer piping, steam tracers and steam trap piping
 Vent and drain valve sets
 Equipment trim – Valve, blinds, instrumentation, man-ways access, etc.
 Utility stations.
 Safety Equipment’s -Safety showers/Eye wash stations
 Hydrostatic testing Vents and drains
 Sampling Points, including sample cabinets and sample coolers.
 Expansion joints, silencers and other special piping items.
 Spectacle blinds spades and spacers – removal capability.
 Sloping lines to be modelled.
 All major process attributes and identification attributes will be extracted.
 Piping shall carry all attributes in the piping line list and additional attributes associated with
construction, inspection and testing requirement.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 66 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
EQUIPMENT
 Equipment models should be kept as simple as possible while still showing an accurate
dimensional representation of the equipment outline for presentation and interference
detection. Equipment parametric shall be used whenever possible for.
 Vessels, Columns and Reactors – Outline complete with all nozzles detailed/identified, special
pipe supports, lifting lugs and trunnions, platforms (including penetrations and supporting
steel), handrails and ladders. Man-ways and hand holes, internals, skirts and supports. Identify
column drop out zones. Skirt access ways.
 Tanks – Outline with nozzles detailed/identified, man ways, insulation, stairways, ladders and
platforms, handrails and all other tank appurtenances
 Pumps – Outline with nozzles connections detailed/identified including vents and drains, drive
and coupling and pump driver.
 Compressors – Outline with all equipment nozzles at all interfaces shall be detailed, driver,
acoustic enclosure, lube and seal oil skids (as package units), seal oil overhead tank, lube/seal
oil headers, local cabinets and panels with doors. All maintenance and component removal
volumes including breakout spools.
 Blowers – Outline with all equipment nozzles at all interfaces shall be detailed/identified, driver,
couplings, acoustic enclosure.
 Fired Heaters – Outline, supports, all nozzles detailed and identified, cross over piping, ducts,
stacks, platform, burners and igniters, access doors, tube withdrawal volumes.
 Shell & Tube Exchangers – Outline shell, channel and heads with nozzles detailed and
identified, saddles, tube withdrawal volume.
 Air Fin Exchangers – Outline of bundles, header boxes, all nozzles detailed and identified
plenum, fan motors and drives, chimneys. Any platforms, ladders, steelwork provided by
Vendors shall be fully detailed. Access ways and lay-down areas.
 Package Equipment: Packaged equipment, irrespective of whether it is designed by the
Contractor or its sub-contractors/suppliers, shall be modelled on a basis that is consistent with
the requirements herein and to the same accuracy and content as Contractor’s own designs.
Deviation from these requirements by the Contractor or its subcontractors shall require the
ADNOC Gas Processing prior occurrence. Package equipment shall be modelled in sufficient
detail to facilitate the review of access to all components and instrumentation for operation and
maintenance, ergonomic design, piping, instrument and electrical connections. All interfaces
including nozzles, Contractor/sub-contractor scope and equipment tie-ins shall be detailed and
identified. As a general requirement, model information for all package equipment shall contain
information and details as specified herewith in this document, to ensure overall design integrity
of the plant to be maintained and available for review by the ADNOC Gas Processing.
 General – Permanent davits, lifting beams and tackle, overhead cranes, ladders, platform
(including penetrations and supporting steel), handrails and ladders, safety showers, hose
reels, special piping items.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 67 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 The minimum attribute requirements for equipment are equipment number, insulation thickness
and a description. The minimum required nozzle attributes are tag number, size, pressure
rating, end preparation and pipe material class.
CIVIL / CONCRETE / STRUCTURE
 Drainage and sewerage: Routing outline and level, drips, manholes, catch basin, separators,
vents and sumps.
 Foundation: Foundations for all major and minor equipment / structures shall be modelled,
including foundations for standard pipe supports. The model shall depict accurate dimensions
of the foundation and shall include footing, pedestal, tie beams (if provided), slabs / rafts, piles
etc.
 Concrete Structure: All beams, wall columns, up stands, sumps, etc., in dimensionally accurate
section, floors with penetrations.
 Structural Steel: All beams, columns and bracing dimensionally accurate including primary,
secondary and tertiary steelwork in accurate section and location. Cladding, fireproofing, floor
plating/grating (including penetrations and supporting steel), platforms, hand railings, stairways
and ladders shall be included. Ladders shall be dimensionally accurate and access volume
(including cages) shall be modelled. Space reservations shall be modelled for major
connections details (such as; haunches, gusset plates) to avoid clashes with piping or cable
routes. Stairways shall be dimensionally accurate, with hand railing and access volume.
Supports and bracing. Temporary steel work required for transportation only.
 All civil structural items shall be tagged appropriately with a suitable procedure, which can help
identify the plant/unit/area, type of structure, etc.
 Reinforcement modelling for concrete structure, connection details for steel structures if
Construction Drawings are planned to be extracted from the model.
 Underground conduits: Outline
 Buildings: Outlines including foundations, accesses and HVAC air intakes
 Pits and ponds
 Tank dikes
 OMS (Operator and Maintenance shelter)
 Substation
 Wall and Fences: Volume outline including foundations
 All culverts and duct banks
 Roads: Outline, shoulders, upper and lower levels
 Paving: Outline, upper and lower levels and type
 Road crossings, protection slabs, identification slabs, anchor blocks, impact walls, crash
barriers, etc.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 68 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Topographical survey benchmarks location plan with levels.
 Above ground pedestals projection.
INSTRUMENT
 In-line Instruments – including control valve top work dimensionally accurate for actual items,
relief valves, orifice plates (including maintenance volumes). Thermocouple/RTD, analyzer
probes withdrawal clearance volumes.
 All process connections for instrument on piping and equipment
 Offline instruments including transmitters, gauges and local indicators, remote mounted
instrumentation including stands, housings and shades
 Local panels: Outline and access doors, including access volumes
 All aboveground cable ducts and cable trays
 Analyzer houses and shelters: With HVAC air intake, associated bottle racks and vent stack.
 Flare header and drain connections
 Air accumulators – local or remotely mounted
 Junction boxes including support frames and access volumes.
 All underground cable duct/cable trench: Routing, outline, top and bottom level trenches for
electrical and instrument cables and direct buried cables
 All major process attributes and identification attributes will be extracted
ELECTRICAL
 Outline for Electrical motors, Lighting fixtures, junction boxes, cable routes (like trays, trenches,
conduits), local control station, local panel, lighting panel, socket outlets, CCTV
 All transformers, transformer safety cages and access volumes, bus ducts
 Substations
 All aboveground cable ducts and cable trays
 Lighting – all lighting fittings and equipment including any supporting towers and structures,
switches and lighting control equipment
 Power and control equipment – Switchgears, bus ducts, motor control stations, miscellaneous
panels, UPS equipment and batteries, junction boxes (including supporting frames) and
distribution panels
 Communication and security – telephones, CCTV, miscellaneous panels and racks, public
address speakers, beacons and sirens
 Telecom Devices, Cable Trays & trenches
FIXED FIRE PROTECTION AND FIRE-FIGHTING SYSTEMS
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 69 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Spray systems
 Fire main piping, hydrants, block valves, fixed water monitors, dry risers and hose reels
 Fire alarm push buttons
 Fire, smoke, heat and gas detectors
 Deluge valve manifolds
 Fire Extinguishers
 Post indicator valves, valves and valve boxes
 Firefighting cabinets
 Alarm pushbutton stations
MISCELLANEOUS
 Safety showers and eye wash fountains
 Safety, access and egress
 Volumes of all emergency access and egress corridors
 Maintenance volumes and man-ways
 Bundle removal volumes for exchangers and h eaters
 Dropout volumes
 Lay-down areas
 Radiation volumes for flares
 Area classification volumes
 Crane access ways
 Restricted access roads and walkways
 High noise restricted volumes
 Maintenance and operability: All necessary lifting and mechanical handling requirements for
removal of loads of 25 kg and more shall be modelled.
8.5.5 3D MODEL REVIEW GENERAL REQUIREMENTS
 Formal model reviews, of all parts of the Plant design, shall be conducted throughout design
development. Scheduled reviews will typically include 30%, 60% and 90% of the design
completion for each significant part, (Unit or Sub-Unit), of the Work and when significant
changes to the model are to be carried out.
 The ADNOC Gas Processing shall be entitled, upon notification, to review the model at any
stage of completion. If the review data sets are required for viewing at the ADNOC Gas
Processing offices, the review data set shall be in the Application Vendor SmartPlant
Review (SPR) .VUE, .XML, .ZVF and .MDB format at the nominated version.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 70 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 SPR to be extracted from 3 model data option.
 The Contractor shall prepare checklists for each review, including 30%, 60% and 90%
reviews, for ADNOC Gas Processing review. The review itself will be conducted with the
checklist as a guideline.
 Each review shall be carried out offline on a set of model files, identified by date/status and
retained as a record of the status of the design at the time of review along with any relevant
Tag File data.
 The model software shall be capable of providing the ability, during review, to rapidly move
through views of the Plant, with zoom in/out and rotation of object or viewpoint. Views shall
be configured to limit the depth of view. Walk through simulation, point-to-point
measurement and elevation checks shall be performed on demand. The data stored for
each component shall be readily available on screen on demand.
 The software shall provide facilities to be able to tag elements with review comments, be
able to return to the same view at a later date and also be able to export review comments
to a database. All Tags shall be retained by date and each given a unique Tag number for
the duration of the project.
 Color coding -surface style rule SPR also to be extracted along with normal SPR.
 The 3D Model for review shall have facilitie s to key in the comments directly into the model
review display. The comments shall be numbered automatically by the electronic system
and saved in the database together with the view display when the formal review is made.
Block of numbers shall be pre-assigned to each review area in the model review procedure.
When comments are entered in the system care shall be taken to provide sufficient details
so that they are easily understandable by any third party.
 The review software shall have snapshot facility that allows scaled black and white and
color plots to be printed from any view.
 The review software shall be capable of providing search and retrieval facilities, that allows
retrieval of comments with a particular view of the Plant from the database at any time for
further review or comment or close out.
 Combined 3D Models vue files (All Units included) should be extracted. Also Review file for
Fire fighting system should be extracted.
 The reviews shall be broken down to manageable review areas, containing the model files
for that specific area. Some files not associated with that area may be loaded for reference
(e.g. to vrify access, etc.). The selection of review areas shall be clearly identified within the
Project schedule, and shall take account of construction priorities to enable any remodeling,
checking and isometric production to be in line with construction schedule.
 The response time of the system shall also be considered when selecting size of the model
review area, particularly where too large an area and corresponding large number of files
can result in a slow system response time.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 71 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Ergonomic compliance shall be demonstrated by the use of representative models of
human operators manipulated through the model to simulate operability and maintenance
activities.
 Virtual reality simulation shall be provided for critical construction or maintenance activities
involving mobile cranes, bundle pulling equipment and other such construction and
maintenance equipment.
 At the end of each model review session, screen dumps of comments and associated views
shall be taken. When each formal model review is complete, comments shall be collated
and electronically transferred to a consolidated model review record database for issue,
reporting and tracking progress against close out dates. Reports shall be communicated
to the ADNOC Gas Processing. A consolidated listing, including the action status on each
comment, shall be compiled and issued, as required, to the ADNOC Gas Processing. Each
comment shall remain open until it has been demonstrated to the ADNOC Gas Processing
satisfaction that it had been appropriately resolved and/or action has been taken.
8.5.6 3D MODEL REVIEW SCOPE
A) FEED Phase : Model Review
The objective of the FEED model review is, to freeze a basic plot layout and getting agreement on
the proposed design to enable the Contractor to proceed to detail design. The focus of a FEED
model review is on accessibility, safety, layout, human factors engineering, maintainability and
construction. For FEED phase database review of all tools at 45% & 90% stage and S3D Model
Review at 90% stage.
The items listed below should be included in the FEED model review, plus any other
items, which are applicable for the particular project.
Location and orientation of all equipment (incl. supporting method, lifting lugs, insulation) and
all space consumers (incl. pulling volumes and future extensions)
Structures (steel and concrete inclusive fire proofing)
Platforms incl. stairs and ladders. Essential for operation maintenance and escape.
Critical lines from line list (Lines determine the location of equipment and large size pipe
determine the plot layout).
Plot determining piping / ducts (including all 6 in. and larger, routing only, underground as well
as above ground)
Utility station locations
In-line instruments (preliminary information)
Blast walls
Bund walls
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 72 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Maintenance access ways (All including their clash volumes) essential for main access/
operation/ influence on safety. This includes a representation of main maintenance equipment
and trolleys and trucks as applicable
Major piping that influences equipment positions (underground as well as above ground).
Concrete slabs, paving and roads (different load bearing capacities shall be recognised).
Relevant floor slopes, where the fall is >50 mm (2 in) over the floor width
Package unit location and orientation (basic shapes and main components recognizable inside
these package units, the escape ways shall be defined).
Escape routes on grade and elevation (including their volumes)
Pipe racks and main pipe support structures, sleeper ways, culverts, etc.
Outline of underground electrical and instrumentation trenches
Main electrical and instrumentation cable trays / racks [200 mm (8 in)] and wider).
Main panels – outline
Main steel and bracing allocations
Underground sewer systems and collecting and separation systems drainage / sewage
Buildings in outline, e.g. control room, analyser houses, switch rooms
Drop zones/ bundle pulling areas/ laydown areas
Mobile crane aprons (based on available cranes and on lifting study)
Relevant Cranes, Hoisting equipment, lifting beams, monorails (+travel path), maintenance
cranes
Major pipe-chases in structure and buildings (reserved areas for future piping)
Major wall and floor openings for equipment travel
Unit and/ or equipment safety distances, area classification requirements
Constructability volume (incl. location of lifting slings at any time during lifting).
Firewater hydrants, monitors (and hose reels)
Underground firewater lines incl. valves and hydrants
Equipment status (filled in attribute)
Define separation distances within the plot to be taken into account
Interfaces for future extensions and space for future equipment to be taken into account
Area classifications requirements been taken into account
Location of battery limit to be specified (by unit or complex)
Sufficient area for catalyst, solids or bag filter handling
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 73 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Fencing, Ground slopes / elevations, retaining walls if any, envelopes for evaporation ponds.
B) EPC PHASE
30% MODEL REVIEW
The objective of the 30 % model review is, to freeze a basic plot layout and getting agreement
on the proposed design to enable the Contractor to proceed to detail design. The focus of a 30
% model review is on accessibility, safety, layout, human factors engineering, maintainability and
construction.
The items listed below should be included in the 30 % model review, plus any other
items, which are applicable for the particular project.
Location and orientation of all equipment (incl. supporting method, lifting lugs, insulation)
and all space consumers (incl. pulling volumes and future extensions)
Structures (steel and concrete inclusive fire proofing)
Platforms incl. stairs and ladders. Essential for operation maintenance and escape.
Critical lines from line list (Lines determine the location of equipment and large size pipe
determine the plot layout).
Plot determining piping / ducts (including all 6 in. and larger, routing only, underground as
well as above ground)
Utility station locations
In-line instruments (preliminary information)
Blast walls
Bund walls
Maintenance access ways (All including their clash volumes) essential for main access/
operation/ influence on safety. This includes a representation of main maintenance
equipment and trolleys and trucks as applicable
Major piping that influences equipment positions (underground as well as above ground).
Concrete slabs, paving and roads (different load bearing capacities shall be recognised).
Relevant floor slopes, where the fall is >50 mm (2 in) over the floor width
Package unit location and orientation (basic shapes and main components recognizable
inside these package units, the escape ways shall be defined).
Escape routes on grade and elevation (including their volumes)
Pipe racks and main pipe support structures, sleeper ways, culverts, etc.
Outline of underground electrical and instrumentation trenches
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 74 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Main electrical and instrumentation cable trays / racks [200 mm (8 in)] and wider).
Main panels – outline
Main steel and bracing allocations
Underground sewer systems and collecting and separation systems drainage / sewage
Buildings in outline, e.g. control room, analyser houses, switch rooms
Drop zones/ bundle pulling areas/ laydown areas
Mobile crane aprons (based on available cranes and on lifting study)
Relevant Cranes, Hoisting equipment, lifting beams, monorails (+travel path), maintenance
cranes
Major pipe-chases in structure and buildings (reserved areas for future piping)
Major wall and floor openings for equipment travel
Unit and/ or equipment safety distances, area classification requirements
Constructability volume (incl. location of lifting slings at any time during lifting).
Firewater hydrants, monitors (and hose reels)
Underground firewater lines incl. valves and hydrants
Equipment status (filled in attribute)
Define separation distances within the plot to be taken into account
Interfaces for future extensions and space for future equipment to be taken into account
Area classifications requirements been taken into account
Location of battery limit to be specified (by unit or complex)
Sufficient area for catalyst, solids or bag filter handling
Fencing, Ground slopes / elevations, retaining walls if any, envelopes for evaporation ponds.
60% MODEL REVIEW
The focus of a 60 % model review is on engineering and technology. The 60 % model review
shall be carried out and closed out prior to issuing the piping isometrics for construction.
The items listed below should be included in the 60 % model review, plus any other
items, which are applicable for the particular project.
The actions resulting from the 30 % model review
Location of spading points (incl. handling)
Process and utility lines (2 in. and above) incl. supports, flow measurements and main
instrumentation
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 75 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
All other piping largely completed
Equipment to latest information, including orientation of nozzles
Nozzle & Manway orientation/locations (including swing space of covers)
Ladders, stairs and platforms
Valving (position, orientation, etc.)
Control valves with access
Platforms for valves, equipment and operation
Permanent cranes, hoisting beams pad eyes, etc. (based on material handling study)
Hoisting equipment, lifting beams, monorails and davits (hoisting and transport devices for
routine maintenance of equipment or components in excess of the manual handling
requirements contained in DEP 30.00.60.20-Gen.)
Final dimensions of table tops, structures and steel constructions
Secondary steelworks and bracing
Secondary foundations – outlines
Eye wash and safety shower locations
HVAC Equipment incl. large size ducting
Pipe supports locations and types (physically supported), for piping 3 in. and above and all
critical piping. (Supports for stress critical systems shall be based on stress analysis
calculations).
Secondary supports such as trunnions, supporting steel, brackets, etc. (for clash check
purposes)
Local operation panels, all instrumentation on equipment
Firefighting systems (hydrants, monitors, water spray systems, etc.)
In-line Instruments based on final vendor data
Instrument transmitters and outlines of junction boxes, secure instrument air vessels; panels
and cabinets inclusive stands, safety critical sensors / switches
Withdrawal volumes for instruments
PSV Locations
Electrical equipment such as outdoor panels, major lighting towers
Above/ underground electrical + instrument cable trays – outline drops to all users
Above-ground instrumentation and electrical tray routing
Buildings, substation, (incl. crane and HVAC)
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 76 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Package units shall be modelled (equipment, piping, associated instruments, etc.) based on
package vendor general arrangement drawings (additional statement in [6.1])
All HAZOP comments incorporated
Utility stations
Outlines of steam tracing manifolds
Operating vessels for Remote Operated Valves (ROVs), (hydraulic and pneumatic)
Fireproofing
Pits and trenches
Battery limit valves layout
All access ways and maintenance access
Silencers
Fire and gas detectors
Local emergency stop buttons (outline)
90% MODEL REVIEW
The focus of a 90 % model review is to review th e model on the added details such as the location
of junction boxes, instrumentation, sample point locations and steam manifolds (e.g. smothering
and tracing).
This revision is intended to be a confirmation of the results of the 60 % model review.
The model shall be completed to include:
Any late or special items
Any change since the previous reviews
All remaining utility piping
HFE comments incorporated.
Model shall be in accordance with the latest issue of the P&IDS, line list, structural, civil,
instruments and equipment vendor drawings
Auxiliary piping for equipment-compressor skids, pump coolers/ seal piping
Remaining process and utility piping 40 mm (1 ½ in) and below
All stress reviews completed
Valving all sizes, instruments and supporting shown
All cable trays incl. tray supports
Instrument junction boxes, local control panels and instrument support stands
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 77 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
All auxiliary equipment and electrical motors shown
All sprinkler systems shown
Final lighting
Transmitter boxes
Sample stations
In-line instruments final
All minor civil structural items, like standard pipe supports / foundations, lighting pole
foundations, fencing, etc. as per 3-D modelling requirements shall be completed.
8.5.7 NAMING RULES
CONTRACTOR shall use ADNOC Gas Processing naming convention for equipment, nozzles,
pipelines, columns, beams, etc. Naming convention shall use the full tag number and be identical
to that in SPF/SPID/SPI/SPEL.
All tagging shall be done using naming rules. Naming rules shall be created in S3D using VB
program, which generates the names for each object.
The naming convention followed for all the tags such as line number, equipment number,
instrument number shall conform to ADNOC Ga s Processing reference documents & Integration
guidelines.
8.5.8 ATTRIBUTES
CONTRACTOR shall populate the attributes to produce required documents, such as
isometrics, plan and elevation drawings, piping material takeoffs and other reports.
CONTRACTOR shall maintain consistency of S3D attributes with SPID, SPI & SPEL & SPF.
Creation of any new attributes shall be done after approval from ADNOC Gas Processing.
8.5.9 DRAWINGS & REPORTS
EPC CONTRACTOR shall customize the templates and view styles to meet EPC requirements.
CONTRACTOR shall extract drawings and reports from S3D. All model data, drawings and
reports shall be published to SPF. CONTRACTOR shall include list of drawings and reports that
will be extracted from S3D in implementation procedure.
As far as possible, drawings shall be automatically extracted without any manual “touchups”.
CONTRACTOR shall maintain a document (e.g. an excel sheet) to list all manual
modifications/additions to S3D drawings and shall submit the same to ADNOC Gas Processing
during handover.
CONTRACTOR shall submit to ADNOC Gas Processing sample of each type of drawing & report
for approval before drawings are submitted for review/comments. These include, but not limited
to:
 Piping Plan & General Arrangement Drawings.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 78 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Structural plans, elevations and frames (steelwork, pipe racks, platforms, stairs, ladders
etc.).
 Electrical & Instrumentation layout drawings (Cable Tray layout, Panel layout etc.).
 Plot Plans (Areas and Modules).
 Civil drawings (roads layout, underground piping, piling, underground trenches, drainage
systems, foundations).
 Isometrics Drawings (Including vendor packages)
 Pipe Support Drawings
 3D Models Vue/XML/ .ZVF files (one for each unit, area, modules etc.)
 Walkthrough videos shall be created for all facilities of the plant.
 Reports
 Equipment Name and Location Report
 Piping List of Lines Report
 Piping MTO Report
 Structure MTO Report
 Electrical and Instrumentation Cable tray MTO Report
8.5.10 S3D DOCUMENTS TO BE PUBLISHED IN SPF
 3D Model & Data (Smart Review File Type)
 Model Data Filtered for Cable Schedule Data (SmartPlant Review File Type)
 Isometric Drawings (view files with links to data)
 Ort Orthographic Drawings (view files with links to data)
8.5.11 3D MODEL REVIEWS AND WALKTHROUGH
 CONTRACTOR shall use SPR to perform design reviews.
 Plant objects shall be grouped using Display Set facility of SPR.
 CONTRACTOR shall send SPR display set symbology details (color & criteria) to ADNOC
Gas Processing for approval.
 Walkthrough videos shall be created for all facilities of the plant.
8.5.12 DATA CHECKS & CLEANUP
CONTRACTOR shall perform regular maintenance of the database for optimal performance
as per guidelines mentioned in S3D documents. The model shall be as “clean” as possible
without any integrity errors and TO DO LIST entries. Deliverables such as Orthographic
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 79 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
drawings, isometrics, reports etc. may not be valid if TO DO LIST entries are not in control. As
a minimum the following checks shall be performed:
 TO-DO-LIST entries shall be monitored and cleared on a daily basis.
 Interferences shall be resolved on a regular basis.
 Database maintenance shall be performed.
 S3D Database Consistency Check report should be run without reporting inconsistencies
 All Piping line attributes must be set correctly and invalid entries removed. E.g.:
construction status holds, etc.
 Piping isometrics shall be extracted successfully for all pipelines. Lines that fail to extract
correctly shall to be modified prior to delivery. Isometric extracted drawings shall not to
be manually edited in any way to correct or change the information. Exceptions may only
be miscellaneous notes etc.
 Piping database integrity reports are run and are error free
8.5.13 EXTRACTED DOCUMENTS
Border templates and title blocks for all the extracted documents and reports shall be
customized to match the ADNOC Gas Processing border and title block size, including
applicable S3D Standards for fonts, scale, s ymbology, text sizes, drawing and tag numbering
standards, etc. The Contractor shall check with the ADNOC Gas Processing for the
availability of these title block and borders so as to avoid having to reproduce them. As a
minimum requirement, the following documents shall be capable of being extracted from the
3D model and associated database and handed over to ADNOC Gas Processing after
extraction.
 Plot plans
 Equipment arrangement and layout drawings
 General arrangement drawings for Piping, Civil and Structures including detailed plan
with elevation.
 Civil general Arrangement Drawings
 Piping isometric details including bill of materials
 Piping material take-off (MTO)
 Structural general arrangement drawings, plan and elevation including material take-off
 Pipe Support location plans
 Pipe Support Details
 Cable tray support location plans
 Structural MTO
 Instrument location plans
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 80 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 Instrument and communications equipment location plans
 Cable tray arrangements
 Cable tray MTO
 Electrical equipment location plans
 Safety Equipment location plans
 HVAC equipment and ducting arrangements
 Underground Services layout Drawings
 Contractors shall issue one set of AutoCAD drawings for all the deliverables for all the
disciplines.
8.5.14 S3D DELIVERABLES
CONTRACTOR shall ensure that S3D model does not have any corrupted objects nor contain
inconsistencies before final delivery. CONTRACTOR shall adhere to the following guidelines
for final S3D deliverables:
 Prior to handover, the ADNOC Gas Processing and/or ADNOC Gas Processing
representative will visit the project site and identify any further data required from the
project directory structure. All file types mentioned are indicative only and the handover
should not be limited to only those files mentioned if it compromises the effective re-
instancing of the project within the ADNOC Gas Processing project domain.
 Model shall be as built.
 All drawings & reports within S3D shall be updated with as-built information.
 CONTRACTOR shall upgrade S3D model to ADNOC Gas Processing approved version.
 CONTRACTOR shall submit a model consistency and health check report before and
after the upgrade.
 Temporary files and directories shall be removed prior to delivery.
 The S3D TO DO LIST shall be empty.
 Final TO DO LIST report grouped by description & discipline.
 All bulk load files e.g piping specification, Catalog & PCMCD should be part of deliverable.
 Database integrity shall be performed and all inconsistencies resolved.
 Complete Smart 3D Project Backup performed from the Smart 3D project management
environment.
 CONTRACTOR shall ensure that all deliverables (Orthographic drawings, isometrics,
support drawings, reports, SPR vue/XML files) submitted to ADNOC Gas Processing can
be re-extracted from the restored plant.
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 81 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
 CONTRACTOR shall be responsible for validating and uploading the final merged data
set in ADNOC Gas Processing’s server. CONTRACTOR shall resolve any issues until
the ‘Final Acceptance Certificate’ is obtained.
 The final S3D Project deliverables should include,
The versions used of all software and databases
Complete S3D Project Backup performed from the S3D Project management
environment
Complete backup of the project directory share, including complete backup of the
folder structures for drawings and reports created from S3D including all files the S3D
database points to.
Reports files
Piping Catalogue
Structural Catalogue
Electrical Catalogue
Instrument Catalogue
Material Description Catalogue
Pipe Support Catalogue
Implied Material Data
Component Insulation Data
Flange Insulation Data
Drawing Border Files
Final Clash Report
Final Database Consistency Check Report
Complete Verification Report
Model List Report
Line List Report
Clean Database issues report.
Final Interference Check report.
Customized/added symbol definitions
Symbol executable (.dll files)
Symbol source codes (VB & .Net)
Solid Edge files, if any.
Symbol 2D files
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 82 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252

ADNOC Classification: Internal
Drawing Border Files.
Drawing View Style definitions.
Drawing Label definitions.
Rules definitions (dimension, naming, IFC etc.).
All MS Excel Catalog bulk load files for all disciplines. It is mandatory that these files
reflect 100 percent of the catalog database (e.g., such that the entire catalog contents
can be recreated by bulk loading these files).
List of all Orthographic Drawings (Plot plans, Piping layout, General Arrangement
Drawings, Structural drawings, cable tray drawings, equipment layouts).
List of Isometrics drawings.
List of Support drawings.
Final extracted Isometric drawings within S3D, as Smart Sketch files and as PDF files.
Orthographic Drawings within S3D, as Smart Sketch files and as PDF files.
Final Database Consistency Check Report.
Complete Catalog Verification Report.
Final Project To-Do-List Report.
Equipment Name and Location Report.
Piping List of Lines Report.
Piping MTO Report.
Structure MTO Report.
Electrical and Instrumentation Cable tray MTO Report.
SmartPlant Review files (extracted from As-Built Smart 3D Model).
SmartPlant Review Video files (walk through of the plant).
CONTRACTOR documents (hardcopy, pdf file and native electronic Microsoft
Word/Excel file)
Exception report to be provided
SR log details to be provided during handover
Issue log & TQ details to be provided
Revision No.: 0 Jan. 2021 Document ID: TE-ST-006 Page 83 of 83
All parties consent to this document being signed electronically -TESA/INT/2021/252
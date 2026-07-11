# HSE-RM-ST14_V1 CFD Dispersion&Explos

> Source: `D:/Wison/Main_Contract\ANX 12_HSE Requirements\Att A\HSE-RM-ST14_V1 CFD Dispersion&Explos_ocred.pdf`
> Pages: 37

---

## Page 1

ADNOC Classification: Internal 
HEALTH SAFETY ENVIRONMENT MANAGEMENT SYSTEM 
CFD DISPERSION AND EXPLOSION 
MODELLING  
STANDARD NO.: HSE-RM-ST014 
VERSION NO.: 1 
EFFECTIVE DATE: August 2019 
THE CONTENTS OF THIS DOCUMENT ARE [PROPRIETARY AND CONFIDENTIAL].

## Page 3

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 3 of 37 
ADNOC Classification: Internal 
TABLE OF CONTENTS 
 
INTRODUCTION ........................................................................................................................................ 5 
 
PURPOSE .................................................................................................................................................. 5 
 
SCOPE ....................................................................................................................................................... 5 
 
LAWS AND REGULATIONS ..................................................................................................................... 5 
 
DEFINITIONS & ABBREVIATIONS .......................................................................................................... 6 
 
ROLES AND RESPONSIBILITIES ............................................................................................................ 9 
 
REQUIREMENTS ....................................................................................................................................... 9 
7.1. 
METHODOLOGY ....................................................................................................................................... 9 
7.2. 
MODEL DEVELOPMENT ........................................................................................................................ 11 
7.2.1. 
3D Geometry & Congestion Assessment....................................................................................... 11 
7.2.2. 
Computational Domain .................................................................................................................... 12 
7.2.3. 
Grid Modelling ................................................................................................................................... 13 
7.2.4. 
Boundary Conditions ....................................................................................................................... 14 
7.2.5. 
Choice of the Time Step Size .......................................................................................................... 15 
7.3. 
SCENARIO DEFINITION ......................................................................................................................... 15 
7.3.1. 
CFD Cases ......................................................................................................................................... 15 
7.3.2. 
Source Term Modelling .................................................................................................................... 18 
7.4. 
VENTILATION MODELLING AND ASSESSMENT ................................................................................ 18 
7.4.1. 
Wind Direction and Strength ........................................................................................................... 19 
7.4.2. 
Ventilation Distribution .................................................................................................................... 19 
7.5. 
DISPERSION ANALYSIS ........................................................................................................................ 20 
7.5.1. 
Gas Dispersion Modelling................................................................................................................ 20 
7.5.2. 
Correlation Analysis ......................................................................................................................... 20 
7.6. 
IGNITION MODELLING ........................................................................................................................... 21 
7.6.1. 
Ignition Location ............................................................................................................................... 21 
7.6.2. 
Ignition Timing .................................................................................................................................. 21 
7.6.3. 
Ignition Probabilities ........................................................................................................................ 21 
7.7. 
EXPLOSION SIMULATION & ASSESSMENT ....................................................................................... 22 
7.7.1. 
Potential Explosion Sites ................................................................................................................. 22 
7.7.2. 
Gas Cloud Sizes and Location ........................................................................................................ 22 
7.7.3. 
Combined Dispersion and Explosion Simulations ....................................................................... 23 
7.7.4. 
Exceedance Curves .......................................................................................................................... 23 
7.7.5. 
Sensitivity Analysis .......................................................................................................................... 24 
7.7.6. 
Explosion Loads ............................................................................................................................... 24 
7.8. 
SENSITIVE RECEPTORS ....................................................................................................................... 26 
7.9. 
ASSESSMENT, RECOMMENDATIONS AND ALARP DEMONSTRATION .......................................... 26 
7.10. 
QUALITY CHECKS.................................................................................................................................. 27 
7.10.1. 
COMPETENCY REQUIREMENTS .................................................................................................... 28 
7.11. 
REPORTING ............................................................................................................................................ 29 
 
COMPLIANCE ASSURANCE ................................................................................................................. 29 
8.1. 
PERFORMANCE KPIS ............................................................................................................................ 29 
 
REFERENCES ......................................................................................................................................... 30 
 
APPENDICES .......................................................................................................................................... 30 
 
QA CHECK SHEET ........................................................................................................... 31

## Page 4

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 4 of 37 
ADNOC Classification: Internal 
 
SUGGESTED REPORT CONTENT .................................................................................. 32 
 
FLACS SPECIFIC GUIDELINES (INFORMATIVE) .......................................................... 34

## Page 5

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 5 of 37 
ADNOC Classification: Internal 
 
INTRODUCTION 
Empirical models are the simplest way of estimating gas dispersion extent and deflagration over-
pressures. These models in many cases relies on correlations and hence are less reliable. 
Phenomenological models are simplified models which represent the major physical processes.  These 
models are used for simplified assessment in quantified studies. The physical effects modelling (or 
consequence modelling) using the empirical or phenomenological models is discussed in detail in 
ADNOC Quantitative Risk Assessment (QRA) Standard [Ref. 2]. 
 
CFD represents the state-of-the-art in consequence effects modelling for ventilation, flammable and toxic 
gas dispersion, smoke and explosion.   Several design aspects can benefit from the use of CFD models 
as an alternative to the simplified consequence models; these include the dispersion of dense gases in 
low wind conditions, the assessment of explosion risk in congested areas, the dispersion of gases in 
complex terrains and hot plume dispersion from a ground flare.  
 
Use of CFD provides realistic results which can provide considerable benefits in the design of the facilities 
especially for facilities where space is a constraint.  
 
 
PURPOSE 
The purpose of this Standard is to provide an overall understanding of the CFD dispersion and explosion 
modelling and its application within risk analysis for ADNOC Group. This document describes the 
methodology, key assumptions, model and scenario development requirements, quality checks, etc. that 
shall be used and in place to carry out CFD dispersion or explosion modelling.   
 
 
SCOPE 
This document stipulates the mandatory requirements applicable to the ADNOC Group and its 
Contractors.  
 
ADNOC Group and its Contractors shall ensure that all requirements listed herein are fully understood, 
implemented, complied with and monitored at all times. 
 
 
LAWS AND REGULATIONS 
UAE Legislations applicable to this Standard includes but not limited to: 
(i) 
Federal Law No. 8 (1980) UAE Labour Law and its Amendments Chapter V:  Safety, 
Protection, and the Health and Social Care of the Employees; Article (91). 
(ii) 
UAE Ministerial Order No. (32), 1982. Specifying Preventive Methods and Measures for 
Protecting Workers against Work Hazards. 
(iii) 
UAE Ministerial Order No. (37/2), 1982. Establishing the level of medical attention, the 
employer is obliged to provide to his workers. 
(iv) 
Federal Law No.: 24 of 1999 for the Protection and Development of the Environment. 
ADNOC Group must ensure, that their activities comply with all relevant Federal and Abu Dhabi laws and 
regulations at all times, including any that may be introduced after the publication of this Standard.

## Page 6

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 6 of 37 
ADNOC Classification: Internal 
 
DEFINITIONS & ABBREVIATIONS 
TERMS 
DESCRIPTIONS 
ABL 
Atmospheric Boundary Layer 
ACPH 
Air Changes Per Hour 
ACR 
Air Change Rate 
ADNOC  
Abu Dhabi National Oil Company 
ADNOC Group 
ADNOC Group includes the Directorates & Functions (in ADNOC 
Headquarter), Group Companies and Affiliates 
ALARP 
As Low As Reasonably Practicable 
CFD 
Computational Fluid Dynamics 
CFLC 
Courant-Friedrich-Levy number based on sound velocity 
CFLV 
Courant-Friedrich-Levy number based on flow velocity 
Congestion 
It is a measure of restriction to flow within the flow simulation region 
caused by the obstacles in that region 
CHSE 
Corporate HSE 
CO 
Carbon Monoxide 
CO2 
Carbon Dioxide 
CSG 
Constructive Solid Geometry 
CV 
Control Volume 
DAL 
Design Accident Load 
EDP 
Emergency Depressurizing 
EER 
Escape Evacuation and Rescue 
EERA 
Escape Evacuation and Rescue Assessment 
EPC  
Engineering, Procurement and Construction 
ESD 
Emergency Shut Down 
Exceedance curve 
A plot of the value of a variable against the plot of probability or 
frequency of exceedance of that variable 
FEED  
Front End Engineering and Design 
FERA 
Fire & Explosion Risk Assessment 
FLACS 
FLame ACceleration Simulator – One of the CFD tool for dispersion 
and explosion 
Frequency 
Number of occurrences anticipated during a unit of time 
Gas explosion 
Combustion of pre-mixed flammable gas cloud that can result in 
rapid rise in pressure 
GC 
ADNOC Group Company

## Page 7

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 7 of 37 
ADNOC Classification: Internal 
TERMS 
DESCRIPTIONS 
H&MB 
Heat and Mass Balance 
Hazard 
The potential to cause harm, including ill health and injury, damage 
to property, products or the environment; production losses or 
increased liabilities 
HSECES 
HSE Critical Equipment and System 
HSEIA   
Health, Safety and Environmental Impact Assessment; A systematic 
process of identifying HSE impacts of existing, new or substantially 
altered projects, and establishing prevention and mitigation 
requirements. 
HVAC 
Heating, Ventilation and Air Conditioning 
Incident 
An undesirable event or chain of events which cause, or could have 
caused injury, illness and/or damage (loss) to the environment, 
assets or third parties 
Individual Risk (IR) 
The combined fatal risks to a named individual. IR takes into 
account factors such as:  
 
Total Risk: The sum of risk contributions from all hazards to which 
the individual is exposed 
Occupancy: The proportion of time exposed to work hazards and  
Vulnerability i.e. probability that exposure to the hazard will result in 
fatality 
IOGP 
International Association of Oil and Gas Producers 
JIP 
Joint Industry Projects 
LFL 
Lower Flammability Limit; The lower level of gas concentration which 
will result in combustion of the gas. This is the same as Lower 
Explosive Limit (LEL) 
LPG 
Liquefied Petroleum Gas 
Overpressure 
The excess pressure above the ambient conditions 
P&IDs  
Piping & Instrumentation Diagrams 
PES 
Potential Explosion Site 
PFDs  
Process Flow Diagrams 
Phenomenological Models 
Simplified physical models, which seek to represent only the 
essential physics 
Probability 
The mathematical expression of chance, Probability/Likelihood/ 
Frequency are the number of occurrences of an event per unit time 
QRA  
Quantitative Risk Assessment; It is a formal and systematic 
approach of estimating the likelihood and consequences of 
hazardous events, and expressing the results quantitatively as risk 
to people, the environment, asset or reputation

## Page 8

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 8 of 37 
ADNOC Classification: Internal 
TERMS 
DESCRIPTIONS 
A structured approach to assessing the potential for incidents and 
expressing this potential numerically. In QRA statistical values are 
derived for potential loss of life and damage to resources and 
environment. Note: These values must never be interpreted as 
unavoidable and acceptable losses 
 
It must always be recognised that the calculated fatality (or loss) 
figures are based on experience, statistical failure and incident rates 
representing an average historical quality of management. Incident 
investigations usually show that these ‘historical’ incidents were, 
with the benefit of hindsight, quite preventable 
 
QRA is a tool which helps to translate this hindsight into foresight 
(planning) in order to assist management in deciding the best 
approach and show ways and means (e.g. improved engineering, 
procedures, supervision, etc.) to prevent the potential incidents from 
happening. QRA is not to be used to justify or encourage risk taking 
Shall / Must 
Indicates a mandatory requirement 
Should 
Indicates a recommendation to be followed 
SME 
Subject Matter Expert 
Stagnation overpressure 
The excess pressure above that in the approach flow which occurs 
on the front face of a surface where the gas velocity is brought to 
rest 
Stoichiometric 
Air/Fuel mixture is such that it contains exactly the required amount 
of oxygen to completely consume the fuel 
TDIM 
Time Dependent Ignition Model 
TR 
Temporary Refuge 
Turbulence 
Rapid irregular local fluctuations in physical variable, such as 
velocity or concentration, that arise due to the presence of eddies 
within the flow 
UAE  
United Arab Emirates 
UFL 
Upper Flammability Limit: The fuel concentration above which 
combustion will not occur.  This is the same as Upper Explosive Limit 
(UEL) 
UKOOA 
United Kingdom Offshore Operators Association 
VCE 
Vapour Cloud Explosion; The explosion resulting from the ignition of 
a cloud of flammable vapor, gas, or mist in which flame speeds 
accelerate to sufficiently high velocities to produce significant 
overpressure 
Volume blockage ratio 
The ratio of the volume occupied by the obstacles to the total volume

## Page 9

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 9 of 37 
ADNOC Classification: Internal 
 
ROLES AND RESPONSIBILITIES 
ADNOC Directorates: ADNOC Directorates shall be responsible to assign their respective Functions/ 
Divisions to be the ultimate owner of the CFD assessment reports and be responsible/ accountable for 
its distribution. 
 
ADNOC Group Companies: Within the ADNOC Group Companies, for project phases, respective project 
team/ division shall be responsible for the preparation and completion of dispersion and explosion studies 
where carried out as part of project deliverables. CHSE is responsible for issuing technical approval upon 
successful completion in line with requirements stated in ADNOC Standards. 
 
 
REQUIREMENTS  
Dispersion and explosion modelling can be carried out either using empirical and phenomenological 
models or using more sophisticated methods such as Computational Fluid Dynamics (CFD).  The former 
method provides a conservative result which does not consider volume blockages, obstructions, 
obscuration, etc. whereas CFD considers time dependency and volume blockages leading to congestion, 
turbulence, etc. which results in a more realistic result.   
 
Therefore, CFD is recommended where:  
 
 
There exist high level of congestion or facilities are designed within the congestion regions e.g. 
offshore modules, WHTs, islands with space constrains, congested onshore modules, etc.;  
 
Facilities handling high H2S / toxic composition process fluids; and 
 
Facilities handling very high pressure process streams in relatively congested areas.  
CFD studies are also recommended where reliable solutions from simpler studies are not available or 
where more accurate solutions are needed to resolve specific design issues. The use of CFD for 
modelling shall be carried out in consultation with ADNOC Group CHSE SME.  
 
This standard provides methodology and key guidance / assumptions which shall be adopted while 
carrying out dispersion and explosion modelling using CFD. 
 
7.1. 
METHODOLOGY 
The physical aspects of any fluid flow are governed by three principles: mass is conserved, Newton’s 
second law is fulfilled (also referred as momentum equation), and energy is conserved. In the physical 
models, these principles are expressed in integral equations or partial differential equations being the 
most common form of the Navier-Stokes equations for viscous flows and the Euler equations for inviscid 
flows. These physical models are the ones implemented in Computational Fluid Dynamic (CFD) tools. 
The CFD tools transform the governing equations of the fundamental physical principles of fluid flow in 
discretized algebraic forms, which are solved to find the flow field values in time and/or space.  
 
Commonly used commercial CFD software tools in oil and gas industry are FLACS, CFX, KFX, ANSYS, 
FLUENT, etc. Some of them have models for general purposes whereas others have specific models that 
have been developed for particular phenomenon, like dispersion, fires or explosions (such as KFX and 
FLACS). In the event that a GC opts to use FLACS as a commercial CFD software tool, specific guidelines 
for such use are set out in APPENDIX 3. For the avoidance of doubt, nothing in this Standard shall be 
construed as a recommendation, requirement for and/or endorsement of FLACS (or any other tool) as a 
preferred commercial CFD software tool 
 
CFD is widely used to understand phenomenon of dispersion and explosion of hazardous substances. 
Typical dispersion and explosion studies where CFD based techniques can be used are listed below:

## Page 10

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 10 of 37 
ADNOC Classification: Internal 
 
 
Forced and natural ventilation, evaluation of air changes on an offshore module/ turbulence on 
Helidecks; 
 
Flammable and toxic gas dispersion modelling to understand realistic impact; 
 
Calculation of equivalent stoichiometric volume of flammable gas for explosion modelling; 
 
Stack release dispersion;  
 
Exhaust gas studies, e.g. for helideck evaluations; 
 
Gas detection optimization studies; 
 
Flammable/ Toxic Gas Dispersion Analysis; and 
 
Gas Explosion Analysis. 
CFD analysis process starts from development of 3D model to explosion simulation and risk assessment. 
The methodology is presented in Figure 7.1.1 and shall be adopted where CFD is used for dispersion 
and explosion modelling assessment. Each of these steps are discussed in detail in the following 
subsections. 
 
 
 CFD Studies 
CFD Assessment
Model Devlopment
Scenario Definition
Ventilation Modelling and 
Assessment
3D Model, Plot Plan, 
Terrain Information, 
Layouts, Discipline 
Inputs, etc. 
Source Term Modelling, 
Metrological 
Information, Process 
Information, etc.
Flammable & Toxic Gas 
Dispersion Modelling
Ignition Modelling
Explosion Simulation & 
Assessment
Receptors Modelling
Result Presentation
Frequency Analysis
Ventilation Studies
Dispersion Studies
Explosion Studies
Exhaust Gases Studies
 
 
Figure 7.1.1: CFD Analysis Process

## Page 11

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 11 of 37 
ADNOC Classification: Internal 
7.2. 
MODEL DEVELOPMENT 
The first key step in the CFD studies is model development. The model development consists of 
development of 3D model with appropriate anticipated congestion, defining computation domain, grid 
modelling, boundary conditions, etc. These parameters of model development have direct correlation 
with the accuracy and realistic nature of dispersion and explosion results and hence needs to be defined 
as close as to realistic models.  Following sections outlines these steps, key guidelines and associated 
assumptions which shall be adopted while carrying out the CFD Studies.  
 
7.2.1. 3D GEOMETRY & CONGESTION ASSESSMENT 
For undertaking a CFD analysis a 3-dimensional geometry of the plant/module/platform is required. The 
geometry can either be built manually or imported from an existing CAD model. Care should be taken to 
ensure that the imported geometry only consists of elements compatible with the specific CFD program 
being used. For existing facilities, 3-D scanning can be utilised to capture accurate and up to date 
geometry. For building and CFD geometric model from scratch or for verification of model following 
imported geometry, typically the following information is required: 
 
 
Plot plan; 
 
Sectional drawings; 
 
Piping plan; 
 
Equipment layout; 
 
HVAC layout; 
 
Cable trays layout; 
 
Framing plans; 
 
Cladding; and 
 
Deck plans 
 
Etc.  
Although not essential, it is recommended that the following convention be adopted for geometry model: 
 
 
East-West along the x-axis, with positive x towards the east; 
 
North-South along the y-axis, with positive y towards the north; and 
 
Up-Down along the z-axis, with positive z pointing upwards. 
This results in a conventional right handed coordinate system, where the lower south-western corner of 
the facility coincides with the origin (0,0,0). 
 
The geometry model shall include all obstacles down to 2” (50 mm) or smallest dimension available within 
the computational domain.  
 
(a) 
FEED Stage Model 
In the FEED phase, sensitivity should be undertaken to check if variation in congestion (additional 
congestion) will change results dramatically and a suitable conservative model should be used for 
simulation purposes. It is recommended that at least 30% reviewed model is utilised as the base 
with added anticipated congestion.  The required anticipated congestion for making the model 
representative of the final geometry shall be added as per in guidelines given in subsection C.

## Page 12

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 12 of 37 
ADNOC Classification: Internal 
(b) 
EPC Stage Model 
The CFD model for detailed design phase should ideally be imported from the existing detailed 
CAD geometry which in in advanced stage of completion. It is recommended that at least 60% 
reviewed model is utilised as the base with added anticipated congestion.  The required anticipated 
congestion for making the model representative of the final geometry shall be added as per in 
guidelines given in subsection C.  
 
(c) 
Anticipated congestion and congestion assessment 
Artificial congestion can be either added based on review of as built model or 90% model of 
previous projects or from material take-off. Where material take-off is used, first the congested area 
is divided into separate areas by function.  For each of these areas anticipated congestion is 
estimated in terms of boxes and cylinders based on average congestion factors and inputs from 
the engineering team on the level of congestion in terms of large piping, small piping (<4”), main 
structural supports (deck supports, vessel supports, access platforms, etc), smaller structural 
elements (other supports, beams/bracing, etc.), electrical / pneumatic elements (cabinets, cable 
trays, valve actuators, etc.), etc.  
 
In either method, 3D model review shall be carried out with engineering team and company SMEs 
to review the congestion levels.  For project phases, team shall consist of ADNOC Group and 
contractor representative from disciplines such as piping, process, instrument, structures, etc.   
 
CFD reports shall provide summary of congestion levels in terms of congestion (L/V – m/m3) before 
and after adding anticipated congestion for various areas and distribution of boxes and cylindrical 
objects of various sizes for each area. Typical examples are shown below.  
 
 
 
Area 
L/V (m/m3) Before 
L/V (m/m3) After 
% Change 
 
 
 
 
 
 
 
 
 
 
 
 
 
Typically congestion level on the offshore platform are between 2 to 3 m/m3 whereas for the onshore 
modules it can range from 1 to 2.5 m/m3 based on the expected congestion.  However, these congestion 
values shall be determined based on the project specific inputs and model review and information 
available from engineering / project team.  
 
Ventilation conditions (decks, walls and relief panels) shall also be studied, reviewed with model review 
team and documented in assumption register.  3D model shall reflect these conditions accordingly.  
 
7.2.2. COMPUTATIONAL DOMAIN 
The total volume required for undertaking the CFD simulation is termed as the computational domain. 
This is the volume within which CFD computations are performed. The computational domain shall be 
extended away from the area of interest in all directions to avoid any boundary influence on the flow

## Page 13

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 13 of 37 
ADNOC Classification: Internal 
solution.  For explosion simulations, it is recommended to have a distance of twice the dimension of the 
module / facility. The main goal is to reduce boundary effects and allow for proper resolution of external 
explosion. 
 
For dispersion cases, an accurate representation of the flow profiles around large geometries requires 
that the distance to the boundary is two or more times the size of the module / facility.  However, this 
depends on the variables of interest (example: H2S ppm level) as well as on the geometry and scenario.  
Smaller domain can be used for large number of scenarios.  However, it shall be made sure distance to 
boundary is significant in all direction. 
  
7.2.3. GRID MODELLING 
Once the geometry has been created or imported, a computational mesh must be constructed.  The mesh 
generation constitutes one of the most important steps during the pre-processing stage after the definition 
of the domain geometry.  
 
Generally, CFD meshes can be structured, meaning that the lines are based on coordinate directions, or 
unstructured i.e. with no relation with coordinate directions; in the first case the mesh consists of 
quadrilateral cells in 2D, or hexahedral cells in 3D, and the unstructured mesh usually consists of triangles 
in 2D and tetrahedral in 3D, but cells can be of any other forms if needed. 
 
Structured grids usually imply shorter resolution time, however the unstructured meshes may better 
represent the geometry. Meshing involves the subdivision of the domain into a number of smaller, non-
overlapping subdomains in order to solve the flow physics within the domain geometry that has been 
created; this results in the generation of a mesh (or grid) of cells (elements or control volumes) overlaying 
the whole domain geometry.  
 
In order to have a good representation of the effect of obstacles it is important that objects are well 
represented geometrically by the chosen grid. The standard method of including solid objects is to resolve 
them using the mesh. The essential fluid flows that are described in each of these cells are usually solved 
numerically so that the discrete values of the flow properties such as the velocity, pressure, temperature, 
and other transport parameters of interest are determined.  
 
The accuracy of a CFD solution is governed by the number of cells in the mesh within the computational 
domain and within the congested areas.  In general, the provision of a large number of cells leads to the 
attainment of an accurate solution.  
 
The following guidelines shall be used in constructing structured mesh: 
 
 
Pertinent flow features should be adequately resolved; 
 
Cell aspect ratio (width/height) should be near one where flow is multi-dimensional.  It is 
recommended to apply uniform, cubical grid cells for explosion scenario (i.e. the same grid 
resolution in all directions); 
 
Grid refinement shall be carried out for all cases around the leak in order to make sure that it does 
not get strongly diluted initially.  Refinement shall be in line with CFD vendor guidelines; 
 
Cells can be stretched where flow is fully developed and essentially one-dimensional. It is 
recommended to keep the stretching not exceeding 20% with respect to adjacent cells; 
 
Sensitivity case shall be carried out for governing case to study the changes the assessment 
results (dispersion patterns and dispersion end point) due to smaller grid size. If significant changes 
are seen in the results, smaller grid size to be considered for modelling.  
 
Larger grid size (2 or 2.5m) can be used for in some simulations such as very large releases 
(200kg/sec), but it is recommended to check grid sensitivity in this case;

## Page 14

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 14 of 37 
ADNOC Classification: Internal 
 
For toxic releases it shall be ensured that that grid cell size is not more than 2m in direction of 
release in the core domain and not more than 5m in the direction of release in the stretched domain.  
Core domain shall be extended to include all sensitive receptors;  
 
Grid smoothing shall be carried out as required in line with Vendor Guidelines;  
 
For reactive gases (e.g. hydrogen) it is recommended to use even finer grid sizes as the fast flames 
may generate pressure gradients in the flame front which also should be resolved; and 
 
In directions where pressure wave propagation is of interest, it is recommended to maintain the 
grid spacing all the way to the targets in the direction of the external blast. 
 
Unstructured grids on the other hand can be constructed with any shaped cell but mesh generation is 
more complex and normally uses specialist software. The procedure for generating unstructured mesh 
involves the following steps: 
 
 
Create, read (or import) boundary mesh(es); 
 
Check quality of boundary mesh; 
 
Improve and repair boundary mesh; 
 
Generate volume mesh; 
 
Perform further refinement if required; 
 
Inspect quality of volume mesh; 
 
Remove sliver and degenerate cells; and 
 
Save volume mesh. 
ADNOC Group shall ensure that while following above grid guidelines, all the vendor recommended 
guidelines on aspect ratio, minimum number of grids, grid refinement, grid smoothing, etc. are also to be 
adhered. Grid dependency should always be checked, at least for a few of the cases (Grid dependency 
is recommended for governing cases), In case of significant deviation are found with quite different grid 
resolutions (within recommended grids guidelines), it is recommended to believe the highest-pressure 
levels calculated.  Accordingly, refine grid for all scenario under assessment.   
 
7.2.4. BOUNDARY CONDITIONS 
The boundary conditions represent the influence of the surroundings that have been cut off by the 
computational domain. As they determine to a large extent the solution inside the computational domain, 
their proper choice is very important. Often, however, these boundary conditions are not fully known. 
Therefore, the boundaries of the computational domain should be far enough away from the region of 
interest to not contaminate the solution there with the approximate boundary conditions. 
 
Inflow boundary conditions 
The normal practice adopted for inflow boundaries is to set the transported quantities of either a uniform 
or some predetermined profile over the boundary surface. At the predesignated inlet location, the exact 
distribution may be unknown. The possibility of moving the inlet boundary to a position where the fluid 
flow is allowed to develop through some distance inside the domain should therefore always be examined. 
 
Wall boundary conditions 
At solid walls a special treatment of the no-slip boundary condition by using wall functions is normally 
applied for the velocities if the resolution is not sufficient. 
 
Top boundary conditions 
The choice of the top boundary condition is very important for sustaining equilibrium boundary layer 
profiles.

## Page 15

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 15 of 37 
ADNOC Classification: Internal 
 
Lateral boundary conditions 
In commercial CFD codes symmetry boundary conditions are normally used at the lateral boundaries 
when the approach flow direction is parallel to them otherwise open lateral radiation boundaries are 
frequently used at the lateral boundaries. With these, every horizontal boundary grid point can allow for 
inflow and outflow and this might also change in time. In both cases there are requirements for the 
minimum distance between the boundary and the area of interest. However, for explosion simulation, 
symmetry boundary can increase the overpressure by reflection the overpressure over the whole domain 
so in such situation Symmetry boundary is not recommended. 
 
Outflow boundary conditions 
At the boundary behind the obstacles (where all or most of the fluid leaves the computational domain) 
open boundary conditions are used. This boundary should be ideally sufficiently far away from the area 
of interest. Boundary conditions try to model what happens beyond the boundary. Sometimes the 
boundary condition will disturb a simulation. Then the user should consider increasing the Simulation 
volume and move the boundaries to regions where less steep gradients will cross the boundaries. 
 
For commercial programs, specific boundary conditions are available, and the user should follow the best 
practice advocated by the program user/ technical manual. 
 
7.2.5. CHOICE OF THE TIME STEP SIZE 
When performing simulations, the size of the time step is another important parameter for the accuracy 
of the results.  If the relevant frequency range can be estimated, then the highest frequency should be 
resolved with at least 10 – 20 time steps per period.  Another method to estimate the time step in 
advection dominated problems is the relation Δt = CFL Δxmin / Umax, where Δxmin is the minimum grid width, 
Umax is the maximum velocity and CFL is the Courant-Friedrichs-Lewy number. 
 
7.3. 
SCENARIO DEFINITION 
CFD analysis may be utilise to assess various scenarios such as flammable concentration around a 
ventilation inlet or a diesel emergency generator; ventilation rate within an offshore module, toxic 
concentration at HVAC inlet or muster location or accommodation areas, gas explosion overpressure for 
the design/ assessment of a blast wall or specifying risk based design overpressures for plant and 
equipment.  Therefore, it is important that number of scenarios modelled are adequate to provide the 
required confidence level in results and assessment.  Source term modelling of each scenarios is equally 
important as it drives the dispersion assessment.   
 
7.3.1. CFD CASES  
As part of the scenario definition, the number of CFD cases which needs to be studied shall be determined.  
This is achieved based on leaks sources and sizes studied (failure cases and associated hole sizes i.e. 
various release rates), wind profile, wind direction, release locations and orientation of leaks, fluid 
compositions, ignition sources, location of gas cloud / PES etc. Selection of cases defines the scope of 
the CFD modelling to be carried out. CFD case guidelines for different studies are mentioned in Table 
7.3.1.

## Page 16

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 16 of 37 
ADNOC Classification: Internal 
Table 7.3.1: CFD Case Guidelines 
Parameters 
Toxic 
Dispersion  
Flammable & Smoke 
Dispersion 
Vent Flammable & 
Toxic Releases 
Flare Smoke and 
Toxic Release 
Explosion 
Applicability 
Drilling, onshore & Offshore Process 
Facilities / Valve Pits / Island Facilities / 
Offshore Process Facilities / Risers / 
Pipelines1 
Vents to 
atmosphere, Open 
Vents, 
Maintenance Vents 
All flares  
Drilling, Process 
Facilities / Island 
Facilities / 
Offshore Facilities 
/ Risers / 
Pipelines1 
Isolatable 
Sections & 
Failure 
Cases.  
For all isolatable 
sections & failure 
cases where H2S 
is more than 100 
ppm in the 
stream.   
 
For all isolatable 
sections & failure 
cases where 
flammable gas is 
present.  
Scenarios where 
pressure is close to 
atmospheric or 
atmospheric can be 
excluded.  
Scenarios / leak 
where release rate is 
less than 0.1kg/sec 
etc. can be excluded. 
Governing flow 
cases, low flow 
cases, high flow 
cases 
 
Governing flow 
cases, low flow 
case, 50% design 
flow case, high 
flow (design flow) 
case 
 
For all isolatable 
sections & failure 
cases where 
flammable gas is 
present.  
Scenarios where 
pressure is close 
to atmospheric or 
atmospheric can 
be excluded.  
Leaks Sizes 
All leaks sizes 
considered in the 
QRA or any other 
safety studies.   
 
All leaks sizes 
considered in the 
QRA or any other 
safety studies.   
Vent tip size 
Flare tip size 
All leaks sizes 
considered in the 
QRA or any other 
study.   
Wind Profile  
Minimum 2 weather conditions (2F, 5D). Sensitivity runs for 10D cases for toxic runs to study the impact 
on the sensitive receptors.  Any additional cases, as required based on wind rose. 
Wind 
Directions 
3 wind directions as minimum. (prevailing wind direction, towards sensitive receptors such as 
accommodation / muster locations / etc., critical buildings, wind in opposite directions, etc.) Based on 
review of wind rose and receptors additional direction to be studied for governing cases.  
8 wind directions for ventilation cases.  
Release 
Locations 
Location of major equipment of the isolatable sections / failure cases.  
Where, more than 1major equipment are present in the given isolable section / failure case, additional 
release locations to be studied.  
Release 
Direction 
6 release direction (+/- X, +/- Y, +/- Z.).  These can be further optimized based on equipment locations, 
3D model review, congestion assessment, etc. with associated technical rationale in consultation with 
Group Company CHSE representative.  In such cases the conservative release direction (typically 
toward sensitive receptors and most congested areas) shall be considered.

## Page 17

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 17 of 37 
ADNOC Classification: Internal 
Parameters 
Toxic 
Dispersion  
Flammable & Smoke 
Dispersion 
Vent Flammable & 
Toxic Releases 
Flare Smoke and 
Toxic Release 
Explosion 
(Example: Riser, pipeline or equipment on the boundary of the 3 model, one or 2 release location are 
sufficient or releases within the 2 plated decks up to 4 release directions i.e. +/-X, +Y and +Z are 
sufficient).  
Fluid 
Composition 
As per H&MB sheet.  
For toxic gas dispersion modelling, where gas breakthrough or significant change in fluid composition is 
expected over design life, those cases to be studied.  
Process 
Parameters  
Pressure, flow, temperature, exit velocity, etc. as per H&MB sheet / engineering design / Empirical 
modelling / vent design / flare design etc.  Time varying nature to be modelled.  (Refer source term 
modelling further guidance) 
Ignition 
Locations 
NA 
5 Locations 
(1 centre, 4 edge) 
Location of 
gas cloud 
NA 
Based on 
dispersion profile 
and identified 
PES.  
PES selection 
shall be based on 
the congestion 
patterns, unit 
boundaries and 
potential for gas 
cloud 
accumulation 
based on the 
dispersion 
patterns.  
Where gas cloud 
occupies less than 
50%, based on the 
dimension of up to 
4 location within 
the PES can be 
considered. (ex: 
for 12% filled – 4 
corners of PES 
can be considered 
for explosion 
modelling) Note 2 
 
Note 1: For offshore and onshore pipelines scenarios can be further optimized considering no congestion 
around.  
Note 2: Gas cloud shall be directed / located towards receptors while % filled approach is adopted for 
explosion modelling.

## Page 18

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 18 of 37 
ADNOC Classification: Internal 
 
Note 3: Failure cases for given isolatable sections can be optimized given appropriate technical rationale 
is provided.  Where, facilities are very similar in nature in term of number of equipment, release sources, 
congestion, process parameters (Identical trains, identical WHTs, etc.), representative module / platform 
can be studied. 
  
Scenario listed in above table are considered as core scenarios.  These scenarios shall be modelled 
using CFD software / tools for dispersion and explosion.  Correlation and statistical analysis shall not be 
used to predict gas cloud sizes from these scenarios.  Additional scenarios can be defined based on the 
intermediate release rates than those studied as part of core scenarios and for additional weather 
conditions.  
 
Correlation and statistical analysis are used to predict the gas cloud sizes for explosion modelling & 
exceedance curve assessment for these non-core scenarios. Typical examples of these non-core 
scenarios are as follows.  
 
 
Additional wind directions for each case such that 8-direction of the wind rose can be achieved. 
(i.e. 5 additional wind directions given 3 wind directions are modelled part of core scenarios); 
 
Additional release locations as required based on the size and location of isolatable sections; and  
 
Additional release cases (hole sizes) in kg / sec as required based on the study requirement to 
distribute the release rate more smoothly and thus smoothen the exceedance curve. (additional 
cases such that 5 to 6 release rates profiles are available). 
Note, these additional release scenarios shall be considered where more detailed assessment is required 
or smoothing of curve is required due to small releases cases. This shall be based on technical judgement 
of the team and discussed and finalize during assumption register workshop.  
 
7.3.2. SOURCE TERM MODELLING 
As part of the source term modelling for all the cases under consideration the release profile is determined.  
Two key inputs to be considered for the source term modelling are release rate (kg/sec) and exit velocity 
(m/s).  Time varying releases shall be considered where ESD and EDP provisions are available.  Where 
source term modelling is carried out as part of safety studies such as QRA / FERA etc.,, these can be 
taken forward for the CFD studies.  Where information is available, HYSYS simulation can be used to 
determine realistic release rates.  
 
For each case under study, the process fluid shall be based on H&MB sheets. Where species are not 
available for certain components, relevant representative species can be used in consultation with 
respective ADNOC Group CHSE.  
 
While considering the time varying releases, flare dispersion studies, etc., the changes in the composition 
of the process fluid shall be considered. This is important especially for streams containing H2S.  
 
7.4. 
VENTILATION MODELLING AND ASSESSMENT  
Ventilation modelling and assessment shall be carried out to determine following:  
 
 
Air Change Rates (ACR) for the given module / PES under consideration.;  
 
Establishing wind profile for the dispersion modelling; and 
 
Aid for the correlation analysis for non-core scenarios.  
One of the factors in the size of a flammable cloud, produced by a leak is the area-ventilation rate. 
Adequate ventilation is essential for safe operations throughout hazardous areas on congested modules

## Page 19

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 19 of 37 
ADNOC Classification: Internal 
such as offshore platforms. It ensures that small leakages of flammable or toxic gases do not accumulate 
and are diluted and removed quickly from the module / platform. The severity of an explosion following 
the ignition of such a flammable cloud will be a function of the mass of flammable gas in the cloud. Thus, 
an increased ventilation will have a beneficial effect upon the explosion hazard.  
 
For a hazardous area a minimum ventilation rate of 12 Air Changes Per Hour (ACPH) is preferred and 
that this should prevail for 95% of the year to allow for the seasonal variation of the wind. For ventilation 
simulations of a naturally ventilated area, the calculation domain shall extend far enough outside the 
installation to ensure that the wind field is not (or only marginally) influenced by the presence of the 
installation.  Guidelines for carrying out ventilation modelling using CFD tools and analysis are outlined 
in subsections below.  
 
7.4.1. WIND DIRECTION AND STRENGTH 
Use of wind stability class and boundary turbulence levels should be stated.  At least 8 wind directions 
shall be considered for ventilation modelling using CFD tools and analysis with frequency and speed 
distribution taken from the site wind rose with at least 3 wind conditions (e.g. 2F, 5D and 10D). The 
ventilation rate for other wind speeds can then be inferred from observing the relationship between 
external wind speed and internal wind speed.  
 
Typically, ventilation runs shall be carried out 80 to 120 seconds to ensure steady state wind flow field is 
established around the facility.  However, for larger computation domains such as large Islands, higher 
duration can be considered in consultation with respective ADNOC Group CHSE.  
 
These ventilation runs should be further used as initial condition for the dispersion runs.   
 
7.4.2. VENTILATION DISTRIBUTION 
The objective of performing wind flow simulation is to obtain the internal wind flow field for use with 
dispersion simulations as well as to generate ventilation distribution within the modules of interest. Using 
the wind rose frequencies and associated wind speeds/directions, a ventilation distribution can be 
developed by undertaking a set of wind flow simulations consisting of various wind direction and speeds. 
A typical ventilation exceedance curve is shown in below Figure 7.4.1 as an example.  
 
Figure 7.4.1: Example Ventilation Exceedance

## Page 20

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 20 of 37 
ADNOC Classification: Internal 
7.5. 
DISPERSION ANALYSIS 
Various release sources can be modelled, including high pressure gas, low pressure gas, flashing liquids 
or pools. The following studies may be performed using CFD dispersion analysis: 
  
 
Flammable gas dispersion;  
 
Evaporating flammable and combustible liquids; 
 
Toxic gas dispersion; 
 
Stack release dispersion; 
 
Smoke dispersion; 
 
Exhaust gas studies, e.g. for helideck evaluations; and  
 
Gas detector optimization studies. 
7.5.1. GAS DISPERSION MODELLING 
Although CFD tools require more computational time, they allow taking into account the scenario 
complexities such as barriers or semi-confined spaces, and hence they are more suitable to model 
dispersion when a realistic/complex scenario has to be considered. 
 
Dispersion simulations using CFD tools shall be performed for core scenarios. Computational domain 
shall be defined such that it is large enough to obtain a realistic bulk wind flow in and out of the module. 
The grid should be refined where high gradients in the velocity field are expected (i.e. in the high 
momentum jet zone). 
 
Where dispersion simulation is being undertaken in conjunction with the wind flow, adequate time (usually 
80 to 120 seconds) should be allowed for the wind profile to stabilize throughout the domain before the 
leak is initiated.  Leak rate is initiated by ramping up from zero (0) to the leak rate specified and kept as 
per source modelling (including time varying releases). Dispersion simulations shall be run for until the 
time (usually 300 to 350 seconds) where flammable gas cloud approaches steady state.  Once gas cloud 
reaches steady state, leak shall be shut down and sufficient time shall be allowed (typically 50 to 100 
seconds) to disperse so that rich areas of the cloud can mix with air, which can sometime result in gas 
reaching a larger maximum size.  
 
While carrying out the toxic gas dispersion the dispersion and simulation durations are much larger due 
to lower concentration of interest. Therefore, for toxic gas simulations they shall be run for sufficient time 
to ensure gas cloud reaches steady state for concentration under interest.  
 
Certain CFD tools has smoke generation modelling capabilities followed by dispersion and shall be used 
for the prediction of the smoke and associated components (CO, CO2 and SO2).  For CFD tools that do 
not have smoke generation / development modelling capabilities, excel based calculation can be carried 
out for the smoke generation and predicting associated source term modelling in consultation with the 
respective ADNOC Group CHSE.   
 
For explosion simulation purposes flammable gas cloud shall be monitored to understand FLAM and Q9 
stoichiometric volume for various time steps.  If a dispersion scenario has potential to generate gas cloud 
that can also reach, accumulate or fill adjacent modules / areas, gas cloud shall be monitored in those 
modules / areas.  
 
7.5.2. CORRELATION ANALYSIS 
For non-core scenarios, correlation analysis [8] can be used to define the flammable gas cloud volumes.  
These correlations have been derived from CFD gas dispersion simulations to represent the dependence

## Page 21

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 21 of 37 
ADNOC Classification: Internal 
of equivalent cloud volume on release rate and ventilation rate in different platform areas for different fluid 
types and ignition time ranges. The correlation takes the form of a least squares error fit of Huser and 
Kvernvold to the average (mean) of all the data points.   
 
7.6. 
IGNITION MODELLING 
Location & timing of the ignition plays a vital role in determining the blast overpressure as it influences 
flame behaviour and propagation and hence multiple ignition locations and timing needs to be considered 
while carrying out the CFD explosion modelling.  The guidance on the location, timing and associated 
probabilities are given in subsection below.  
 
7.6.1. IGNITION LOCATION 
It is recommended to use 5 ignition location for each gas cloud under study i.e. 4 edge ignition (-X,+X, -
Y, +Y) and 1 central ignition while carrying out the explosion modelling using CFD.  These edge locations 
shall be selected such that they yield the conservative results towards the sensitive receptors.  
 
Note: Once ignition location has been assigned, they shall be checked in the 3D model to ensure they 
are not inside a fully blocked control volume.  Additionally, ignition points shall not be located too close 
or half inside the objects or grid lines etc.  Certain CFD tools while carrying out porosity calculations, 
assigns control volume to adjacent grid leading to no ignition for these cases.  In general, all guidelines 
and warning for respective CFD tools shall be adhered to.  
 
7.6.2. IGNITION TIMING 
Ignition timing determines the amount of flammable mass available for explosion.  Early ignition can lead 
to smaller explosion overpressure due to much lower flammable mass available.  Therefore, where more 
realistic results are required, it is recommended for each case under study to use multiple ignition timing 
(preferably minimum of 3 timings) and associated flammable gas cloud.   
 
7.6.3. IGNITION PROBABILITIES 
Energy Institute Ignition Model 
While carrying out the ignition modelling and probabilistic explosion assessment, it is recommended to 
use flow rate based delayed ignition from Energy Institute [Ref. 9].  Further guidance on the selection of 
ignition curve and determining delayed ignition probabilities are available in the ADNOC Quantitative Risk 
Assessment (QRA) Standard, HSE-RM-ST10 [Ref. 2].  
 
Time Dependent Ignition Model (TDIM) 
For facilities where detailed information on ignition sources are available and where time is not a 
constraint, alternatively, the Time Dependent Ignition Model (TDIM) [Ref. 5] can be used for the 
probabilistic explosion analysis. From CFD calculations the volume of the gas cloud with concentration 
between LFL and UFL will give the volume that may be ignited if exposed to an intermittent ignition source. 
This information should thus be related to the intermittent ignition frequencies defined while using TDIM. 
 
For each new time-step in the dispersion analysis, the following parameters shall be calculated as they 
affect the probability of ignition: 
 
 
Total volume exposed to flammable gas (within concentration between LEL and UEL) which can 
be ignited by intermittent ignition sources; and 
 
New volume exposed to flammable gas which can be ignited by continuous ignition sources.

## Page 22

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 22 of 37 
ADNOC Classification: Internal 
Thus, for each time step (or each 1s) for each dispersion calculation, the probability for ignition from 
intermittent and constant ignition sources should be established, and this probability should be added to 
a gas cloud size class. 
 
Probability Distribution 
Once delayed ignition probabilities are determined, they can be further distributed equally for each ignition 
location.  Typically, as the release duration increases, flammable gas cloud occupies larger footprint 
leading to higher probability of ignition. Therefore, while distributing the probabilities for the ignition timing, 
higher weightage shall be given for the larger gas cloud i.e. ignition at later stages.  The assumption 
associated with these ignition probabilities shall be finalized in consultation and approval from respective 
GC CHSE representative and documented in the assumption register.  
 
7.7. 
EXPLOSION SIMULATION & ASSESSMENT 
7.7.1. POTENTIAL EXPLOSION SITES 
Potential Explosion Sites (PES) are areas in the module, congested regions, etc. where flammable gas 
cloud can accumulate leading to potential explosion.  Percentage (%) filled approach is one of the 
approaches which is adopted for explosion modelling.  In such cases, flammable gas cloud for each case 
is assigned to respective % filled scenarios.  Therefore, selection of PES plays an important role in the 
explosion assessment and development of smoother exceedance curves.  
 
For offshore module, typically one or two decks depending on grated or plated deck are considered as 
one PES.  A module can have multiple PES based on the congestion patterns, presence of hydrocarbon 
and dispersion patterns. However, while carrying out the explosion simulation the entire geometry of 
module / facilities shall be considered, and computation domain shall be defined large enough to include 
entire module and all receptors of interest. The boundary of the computational domain should be large 
enough not to influence the results of the analysis.  
 
Where multiple modules exist, the determination of computation domain, selection of PES, grid modelling, 
etc. shall take into account the effect of multiple modules.  In such cases, entire geometry shall be taken 
into account.  
 
7.7.2. GAS CLOUD SIZES AND LOCATION 
Gas Cloud Size 
Where % filled approach (equivalent stoichiometric cloud approach) is adopted for the explosion 
assessment, as a practical guideline, it is recommended to choose the shape of the cloud that will give 
maximum travel distance from ignition to end of cloud for smaller clouds.  The cloud should be made as 
a cubical rectangular box with assumed “planes of symmetry” towards confinement. The aspect ratio for 
a free cloud should be 1:1:1, for a cloud towards the ceiling 2:2:1, towards ceiling with one sidewall 2:1:1, 
etc. While determining the size of the gas cloud the dispersion patterns shall also be referred to. 
 
Explosion Scenarios and Gas Cloud Locations  
For % filled approach, it is recommended to consider minimum seven (7) flammable gas cloud % filled 
scenario cases for explosion simulation for each PES.  Typical values to be used while defining explosion 
flammable gas cloud scenarios are 1%, 3%, 6%, 12%, 25%, 50% and 100%.  Binning approach shall be 
adopted while assigned dispersion gas clouds to respective explosion gas cloud.  Where, based on 
dispersion results it is observed that binning approach may introduce large error due to rounding off, 
additional % filled scenarios should be considered.  
 
For plant / facilities with multiple modules and PES, for a given dispersion case if dispersion shows that 
gas cloud can occupy or fill more than one PES / module, then it shall be considered for all these PES / 
modules for explosion calculations.  Percentage (%) filled area may vary in these cases depending upon 
the dispersion patterns.

## Page 23

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 23 of 37 
ADNOC Classification: Internal 
 
For cases from 1% to 25%, up to 4 location of gas cloud shall be studied based considering presence of 
leak sources.  For other scenarios excluding 100% filled, two (2) location of flammable gas cloud shall be 
studied.  In such cases, the location of the gas cloud shall be selected such that it is targeted towards 
sensitive receptors and yields conservative results.  
 
Equivalent Stoichiometric Gas Cloud  
It is usually not feasible or even desirable to perform the explosion simulations with a sufficient number 
of ignition points directly on the inhomogeneous clouds resulting from the dispersion analysis. An 
idealised homogeneous equivalent stoichiometric cloud is used to give explosion loads similar to an 
inhomogeneous gas cloud.  
 
The size of the equivalent stoichiometric cloud is calculated as the amount of gas in the flammable range, 
weighted by the concentration dependency of the flame speed and expansion.  
 
As the equivalent stoichiometric cloud is smaller than the combustible part of the real cloud, the pressure 
durations may tend to be shorter than in the real case. This should be taken into account when 
establishing the pressure duration in the design loads. 
 
Using the equivalent stoichiometric cloud may underestimate far field pressure loads as the far field 
pressures are determined by the pressure at the edge of the cloud after combustion, and since the size 
of the cloud will be smaller than in the real case, the far field pressure will decay faster than the actual 
scenario.  In such cases, sensitivity can be carried out using gas cloud between UFL and LFL region 
while making estimating overpressure on the far field receptors.  
 
Note: It is recommended to use CFD flammable gas cloud dispersion results while determining the gas 
cloud for the explosion modelling when using CFD and not empirical modelling results (e.g. PHAST).   
 
7.7.3. COMBINED DISPERSION AND EXPLOSION SIMULATIONS  
Rather using the equivalent stoichiometric cloud for explosion simulation (% filled approach), there may 
be some instances where it may be desirable to undertake explosion simulation using direct result of a 
gas cloud from a dispersion analysis.  In such situation, simulation dump files or result output should be 
created at selected time instants, look at the results and restart the simulation from the dump file with 
time closest to the desired time of ignition. This provides the flexibility to select several ignition positions 
without having to rerun the dispersion simulations.  With this approach however the boundary conditions 
for the explosion model should be modified from the dispersion simulation to explosion simulation.   
 
7.7.4. EXCEEDANCE CURVES 
Exceedance curve approach shall be adopted to estimate the overpressure levels on the receptors where 
probabilities assessment is carried out.  
 
An exceedance curve is a mathematical technique which plots a given parameter in this case 
overpressure against cumulative frequency.  Cumulative frequency is the sum of the frequencies of 
events leading to a specified value of the parameter (overpressure), or greater.  Cumulative frequency is 
used because the risk-based approach requires identification of a hazard level which will not be exceeded 
at a given frequency. This is different from identifying a discrete hazard level which occurs at a particular 
frequency. 
 
Typical methodology for preparing exceedance curve for each receptor considering dispersion and 
explosion modelling is as below:

## Page 24

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 24 of 37 
ADNOC Classification: Internal 
• 
For each of the dispersion case, event frequency is assigned based on the corresponding leak 
frequency available from the part counts / isolatable section / failure modes (usually from QRA), 
wind profile probabilities, directional release probabilities, location probabilities, etc.   
• 
Where % filled approach has been adopted for explosion simulation, based on the dispersion 
patterns and gas cloud size for each of the dispersion cases, respective “% filled gas cloud 
explosion case” is assigned. This established the frequency for each gas cloud (% filled scenario) 
studied in explosion simulation.  
• 
Event frequency of each explosion scenarios are determined by combining frequency of % filled 
gas cloud with associated gas cloud locations and ignition probabilities.  
• 
Exceedance curve is plotted considering all explosion and dispersion scenarios for each of the 
receptor. Where multiple modules and PES are presented explosion assessment and exceedance 
curve shall take into consideration releases from all modules and PES.  
• 
Explosion curve shall be plotted for static and dynamic loads as necessary for each receptor.  
 
An example of the form of a typical explosion exceedance curve is shown in Figure 7.7.1 below: 
 
 
Figure 7.7.1: Example Typical Explosion Exceedance Curve 
7.7.5. SENSITIVITY ANALYSIS 
Post initial explosion assessment, once exceedance curve is available, sensitivity analysis shall be 
carried out in consultation with ADNOC Group CHSE representative.  Sensitivity analysis shall take into 
account the impact due to various gas cloud locations, ignition locations, probabilities etc.  
 
7.7.6. EXPLOSION LOADS  
Pressure components 
 
The components of the pressure are as below:  
 
 
Static pressure: The actual pressure of the fluid, which is associated not with its motion but with 
its state, i.e., the pressure in a volume where there are no pressure waves, or the pressure 
perpendicular to a surface following the flow. This is also called side-on pressure.

## Page 25

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 25 of 37 
ADNOC Classification: Internal 
 
Dynamic pressure: The pressure due to the kinetic energy of the flow, i.e., ρv2. Total pressure = 
Static + dynamic. This corresponds to the pressure at the stagnation point. 
 
Reflected pressure: The pressure when a shock wave hits an object and the dynamic pressure 
stagnates. It should be noted that the reflected pressure should be calculated from wave equations. 
 
Overpressure: The pressure minus the ambient pressure, i.e., the gauge pressure. This can be 
both positive and negative.  
Explosion assessment and reporting shall ensure appropriate components are used for reporting and 
design purposes.  
 
Properties of the Pressure Field 
 
The explosion pressure will vary both in space and time. Note that the overpressure may be both positive 
and negative, i.e., there can be a negative phase where there is a suction pressure (pressure dropping 
below the ambient pressure). Based on space averaging, the following simplified load descriptions are 
commonly used:  
 
 
Global pressure load: The time dependent average pressure over a large surface of interest, e.g., 
a wall or a deck. The maximum of this pressure as a function of time represents the maximum 
force acting on the surface. The positive and negative phase may be represented by a triangular 
pulse with a given duration. 
 
Local pressure load: The time dependent pressure averaged over a small surface, e.g., a panel 
in a blast wall. The positive and negative phase may be represented by a triangular pulse with a 
given duration. 
 
Impulse: The integral of the pressure as a function of time separately for the positive and negative 
phase.  
 
Maximum overpressure: The pressure-time history resulting from CFD simulations may contain 
pressure pulses or spikes of very short duration. If the maximum overpressure occurs in such a 
pressure pulse it may be too conservative to base the design load or risk picture on such maxima. 
The overpressure pulses can be smoothed by averaging over larger time steps. The typical response 
time of the structure to which the load is to be applied will determine the averaging time that should be 
applied. The averaging time should be somewhat smaller than the shortest response time of the structure  
 
By averaging short time fluctuations that only have an impulsive effect on the response, the resulting 
maximum overpressure will incorporate the impulsive effect of the short time pressure fluctuations without 
being unnecessarily conservative. 
 
Note: Explosion assessment for any receptor shall reflect the cumulative impact from all the potential 
explosion sites and associated explosion cases in the computation domain. Where multiple modules and 
PES are present, explosion assessment and exceedance curve shall take into consideration releases 
from all modules and PES.  
 
Explosion assessment shall highlight clearly where there exist potential for simultaneous explosion in 
multiple module / PES and its impact on the receptors. Where, applicable results shall be taken further 
to respective studies such as FERA / Fire Zone etc.

## Page 26

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 26 of 37 
ADNOC Classification: Internal 
7.8. 
SENSITIVE RECEPTORS 
The following receptors as shown in table below shall be considered for dispersion and explosion 
modelling studies.  
 
Table 7.8.1: Key Receptor Locations 
Receptors 
Vent/ Flare 
Dispersion 
Studies 
Exhaust 
Dispersion 
Studies 
Flammable / 
Toxic 
Dispersion 
studies 
Explosion 
Studies 
Key Structures Element 
 
 
 
x 
HSECES such as ESD 
Valve, etc. 
 
 
 
x 
Emergency Generators/ fired 
heaters 
x 
 
x 
x 
EER measures, supporting 
structures and systems such 
as lifeboat, life-raft, muster 
locations, TR, HVAC inlets, 
etc. 
× 
 
x 
x 
Process Buildings 
x 
 
x 
x 
Helideck 
x 
x 
x 
x 
Occupied Buildings 
x 
x 
x 
x 
Critical Buildings 
x 
x 
x 
x 
Working Locations 
× 
x 
x 
 
 
As part of model review, any other additional receptors if identified shall be considered.  
 
7.9. 
ASSESSMENT, RECOMMENDATIONS AND ALARP DEMONSTRATION 
Based on the dispersion assessment, each identified receptors and key areas in the plant shall be 
assessed as per the criteria given in respective ADNOC standards such as EERA, QRA, HSE Risk 
Management, etc.  
 
Based on explosion assessment, for each receptor once exceedance curve is plotted overpressure 
values shall be reported for 1E-04 and 1E-05 /year exceedance value. These receptors shall be assessed 
based on the DAL / impairment criteria for explosion as outlined in the ADNOC Fire & Explosion Risk 
Assessment (FERA) Standard, HSE-RM-ST09 [Ref. 1].  
 
While giving recommendations, ALARP principles and control hierarchy shall be maintained.  It is 
recommended to brainstorm the recommendations as part of ALARP workshop.

## Page 27

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 27 of 37 
ADNOC Classification: Internal 
7.10. QUALITY CHECKS 
Following quality checks shall be carried out for the CFD Studies.  
 
Scenario Development Stage:  
 
ENGINEER / CONSULTANT shall carryout review with engineering team and review and approval from 
SME from GC CHSE of identified dispersion and explosion scenarios and selection of PES to check that: 
 
 
Identified dispersion and explosion scenarios are in line with guidance and recommendation given 
in this standard for core scenarios; 
 
Identified ventilation scenarios are in line with guidance and recommendations given in this 
standard; 
 
All applicable scenarios from safety studies such as QRA / FERA / EERA are taken forward in the 
assessment;  
 
All applicable Major Accident Hazards are taken forward in the assessment; and  
 
PES are identified correctly and appropriately.  
Note: Scenario list shall be made available as part CFD Assumption register and shall be approved by 
respective GC CHSE representative prior to start of modelling.   
 
Geometry Development Stage 
 
ENGINEER / CONSULTANT shall carryout 3D model review with engineering team and SME from GC 
CHSE of CFD model to check that: 
 
 
The developed/ translated model is an accurate reflection of the actual geometry; 
 
anticipated congestion analysis is appropriate and represents a conservative congestion for the 
final expected geometry;  
 
Plated and grated decks are modelled appropriately; 
 
Non-orthogonal objects such as stairs, diagonal bracings, etc. have been remodelled/represented 
appropriately; 
 
No inadvertent gaps have been introduced due to automatic alignment of decks and wall to the 
grid; 
 
All dummy volumes reserved for interference checks have been deleted; 
 
CFD software’s best practice recommended guidelines on aspect ratio, minimum number of grids, 
grid refinement, grid smoothing, etc. are implemented.  Grid sensitivity shall be carried out for the 
governing cases;  
 
Receptors are identified appropriately; and  
 
All modules are taken into account while development of the geometry.  
A formal QA check list is provided in APPENDIX 1. 
 
Analysis Stage 
 
ENGINEER / CONSULTANT shall carryout review of CFD Analysis to check that: 
 
 
Grid follows the software best practice guidelines for the type of analysis e.g. appropriate grid size 
(cv) is used for the type of analysis (ventilation, dispersion, explosion) and that appropriate 
refinement has been undertaken for dispersion modelling;

## Page 28

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
Standard No.: HSE-RM-ST014 
Version No.: 1 
Effective date: August 2019 
Page 28 of 37 
ADNOC Classification: Internal 
 
The boundary conditions defined for the analysis are as per the software best Practice; 
 
The extent of computational domain is appropriate for the analysis; 
 
Enough monitor points, surfaces have been used at appropriate location to fulfil the objective of 
the study; 
 
Any grating modelled in ventilation or dispersion analysis has been replaced with porous plate for 
explosion simulations; 
 
The flammable gas volume has reached the maximum limit and reached a plateau by checking the 
flammable volume versus time curve from selected simulations; 
 
The flammable gas volume calculation takes account of the gas dispersion from the rich flammable 
concentration to get the maximum flammable volume after the gas flow is switched off; 
 
The ignition locations are reasonable such that the maximum overpressure potential has been 
captured (ignition maximized the flame path, ignition near a wall as well as a central ignition); 
 
Explosion exceedance curves are plotted correctly; and 
 
Sensitivity cases are carried out where required.  
7.10.1. COMPETENCY REQUIREMENTS 
CFD dispersion and explosion analysis is a highly specialized area and specialist expertise must be 
sought. The CFD analysis Team can either be a Third-Party Consultant or selected from the technical 
expertise available within ADNOC Group.  CFD Analysis should only be used by suitably competent 
persons and the results should be subject to appropriate checks by another competent person. 
 
The team performing the CFD analysis shall have the following competencies: 
 
(a) 
Be familiar with the basic principles of gas dispersion and explosion. 
(b) 
Have some understanding of the underlying physics employed within the CFD simulations. 
(c) 
Know the CFD program’s range of validity. 
(d) 
Should be aware of the limits of applicability and validation of the models and be able to justify any 
use outside these limits.  
(e) 
Understand the sensitivities of the model parameters. 
(f) 
Understand the level of detail required to fulfil the goal of the study. 
While selecting third party consultant GC Shall ensure that: 
(a) 
Proposed team shall have sufficient experience in developing the CFD models and carrying out 
CFD assessment. 
(b) 
Team members shall have sufficient hands on experience in the CFD tools being used.  Typically, 
5 years of experience for Junior engineer and 10 yr. for Senior Engineer / lead is recommended in 
CFD modelling and CFD studies preferably in oil and gas industry.  Lead shall be responsible for 
technical content and assessment. 
(c) 
Team shall have sufficient expertise in use of CFD software and have sufficient resources to 
carryout required modelling within the given schedule. 
(d) 
CVs of the engineer and team carrying out CFD studies shall be approved by respective GC CHSE 
and shall highlight relevant experience in carrying out these studies.  
In addition, the persons involved with undertaking probabilistic explosion assessment should be familiar 
with various statistical distributions/ probabilistic methods for deriving the exceedance curves.

## Page 29

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
 
Version No.: 1 
Effective date: August 2019 
Page 29 of 37 
ADNOC Classification: Internal 
 
7.11. REPORTING 
The following should generally be included within the reporting of the CFD analyses: 
 
Description of the model and anticipated congestion assessment;  
 
Site environment considerations; 
 
Metrological data such as wind speeds, directions and ventilation rates; 
 
Dispersion scenarios, their locations and directions, associated frequencies, associated 
inventories, fluid compositions, process parameters, etc.;  
 
Ventilation analysis, selection of representative ventilation rates for non-core dispersion 
simulations and their frequencies;  
 
Correlation analysis, method of estimating and justification for non-core scenarios; 
 
PES summary and analysis;  
 
Flammable cloud sizes and locations from various dispersion scenarios for FLAM and Q9; 
 
Details of ignition probability determination; 
 
Receptor analysis;  
 
Peak and averaged overpressures on surfaces, buildings, EER measures and HSECES; 
 
Peak impulses at HSECES, EER measures, buildings and large surfaces; 
 
Dynamic pressures for use with pipes; 
 
Explosion exceedance curves for the domain, selected HSCECES and structural elements;  
 
Exceedance values on all receptors; and 
 
Any other supporting information  
A suggested report content for a probabilistic explosion analysis is included in APPENDIX 2. 
 
 
COMPLIANCE ASSURANCE 
ADNOC will conduct compliance audit of this Standard at approximately three-year intervals; these audits 
will be in addition to GC’s internal audits and where required, ADNOC will take steps to minimize overlap 
and duplication between ADNOC Corporate and Group Companies internal audits. 
 
The main audit deliverable is a formal and structured report for the attention of GC Management and the 
respective ADNOC Directorate. 
 
8.1. 
PERFORMANCE KPIS 
Key Performance Indicators for this Standard shall include as a minimum the following: 
 
Table 8.1.1: Key Performance Indicator 
No. 
KPI 
Targets 
1.  
CFD Modelling conducted as per guidelines of this Standard 
100% compliance 
2.  
Model review and QA / QC carried out for CFD Modelling as 
defined in this standard 
100% compliance

## Page 30

HSE Management System 
HSE Risk Management Standards 
CFD Dispersion and Explosion Modelling 
 
Version No.: 1 
Effective date: August 2019 
Page 30 of 37 
ADNOC Classification: Internal 
 
REFERENCES 
1. 
ADNOC Fire & Explosion Risk Assessment (FERA) Standard, HSE-RM-ST09 
2. 
ADNOC Quantitative Risk Assessment (QRA) Standard, HSE-RM-ST10 
3. 
FLACS V9.0 User’s Manual 
4. 
Ignition Probability Review, Model Development and Look-Up Correlations, Research Report 
published by the Energy Institute, January 2006. ISBN 978 0 85293 454 8 
5. 
DNV Technical report JIP Ignition Modelling: Time Dependent Ignition Probability Model, Report 
no. 96-3629, Rev. 04, Det Norske Veritas 
6. 
J. Czujko: Design of Offshore Facilities to Resist Gas Explosion Hazard, Engineering Handbook, 
CorrOcean, ASA, Oslo-Norway 2001. 
7. 
NORSOK Z-013 Risk and emergency preparedness analysis, Annex G Procedure for probabilistic 
explosion simulation. 
8. 
Explosion risk analysis - Development of a general method for gas dispersion analyses on offshore 
platforms - Asmund Huser and Oddmund Kvernvold, Parallel Pro 2000 
9. 
IOGP Ignition probabilities, Report No. 434 -6 March 2010. 
10. 
ADNOC Escape Evacuation and Risk Assessment Standard, HSE-RM-ST07 
 
APPENDICES 
APPENDIX 1  
QA Check Sheet 
 
APPENDIX 2  
Suggest Report Content 
 
APPENDIX 3 
FLACS specific Guidelines

## Page 31

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
QA Check Sheet  
APPENDIX 1 
 
Version No.: 1 
Effective date: August 2019 
Page 31 of 37 
ADNOC Classification: Internal 
 
QA CHECK SHEET 
 
Item 
No 
Topic 
Acceptable? 
Notes 
1 
Geometrical representation of the obstacles is 
appropriate and complies with guidance given in 
this standard and CFD tools manual.  
 
 
2 
Anticipated congestion analysis is carried out and 
it represent expected actual geometry in terms of 
level of congestion.  
 
 
3 
Definition of the target variables is consistent with 
the analysis objectives 
 
 
4 
Computational domain complies with guidance 
given in this standard and CFD tools manual. 
 
 
5 
Grid complies with guidance given in this standard 
and CFD tools manual. 
 
 
6 
Boundary conditions complies with guidance given 
in this standard and CFD tools manual. 
 
 
7 
Computational grid is consistent with the desired 
accuracy and complies with guidance given in this 
standard and CFD tools manual. 
 
 
8 
Time step size is in accordance with CFD tool best 
practice  
 
 
9 
Scenario list and assumption register are complete 
and approved by respective GC CHSE. All 
assumptions have been justified appropriately.  
 
 
10 
Sensitivity assessment has been carried out 
 
 
11 
Model review has been carried out.  
 
 
12 
Required level of detailed information, dispersion 
and explosion assessment in line with guidance in 
this document has been reported.  
 
 
13 
Recommendation has been raised and ALARP 
workshop conducted.

## Page 32

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
Suggested Report Content (Informative) 
APPENDIX 2 
 
Version No.: 1 
Effective date: August 2019 
Page 32 of 37 
ADNOC Classification: Internal 
 
SUGGESTED REPORT CONTENT  
The following is a typical recommended content for a CFD dispersion/ explosion assessment.  The report 
structure and content shall be agreed with the GC CHSE SME and documented in assumption register.  
 
Recommended Report Content 
Ventilation 
Studies 
Dispersion 
Studies 
Explosion 
Studies 
Executive Summary 
√ 
√ 
√ 
1. Introduction 
√ 
√ 
√ 
2. Facility Overview 
√ 
√ 
√ 
3. Brief Methodology 
√ 
√ 
√ 
4. Input Parameters 
√ 
√ 
√ 
4.1 Inventory & Leak Scenario Summary 
√ 
√ 
√ 
4.2 Leak Frequencies 
 
√ 
√ 
4.3. Process parameters & Shutdown / 
Blowdown 
 
√ 
√ 
4.4. Metrological Conditions & Wind Rose 
√ 
√ 
√ 
5. Model Development 
√ 
√ 
√ 
5.1 3D Geometry & Associated Modelling 
Summary 
√ 
√ 
√ 
5.2 Congestion Assessment 
√ 
√ 
√ 
5.3 Congestion Summary 
√ 
√ 
√ 
6. Ventilation Assessment 
√ 
√ 
√ 
7. Dispersion Assessment 
 
√ 
√ 
7.1 Overview  
core and non-core dispersion Scenario & 
modelling summary 
 
√ 
√ 
7.2 Core scenario summary 
 
√ 
√ 
7.3 Non-Core Scenario Summary 
 
√ 
√ 
7.4 Equivalent Stoichiometric gas cloud as 
Cloud assessment 
 
√ 
√ 
7.5 Dispersion analysis results  
 
√ 
√ 
8. Explosion Assessment  
 
 
√ 
8.1 Overview & key aspects / assumptions 
 
 
√ 
8.2 Potential Explosion Site 
 
 
√ 
8.3 Explosion Scenarios 
 
 
√ 
8.4 Monitoring points and receptors.  
 
 
√ 
8.5 Explosion Results 
 
 
√ 
8.6 Exceedance Calculations 
 
 
√

## Page 33

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
Suggested Report Content (Informative) 
APPENDIX 2 
 
Version No.: 1 
Effective date: August 2019 
Page 33 of 37 
ADNOC Classification: Internal 
Recommended Report Content 
Ventilation 
Studies 
Dispersion 
Studies 
Explosion 
Studies 
8.7 Explosion Assessment 
 
 
√ 
9. Recommendations and ALARP 
demonstration 
 
√ 
√ 
10. Conclusion and Recommendation 
√ 
√ 
√ 
11. References 
√ 
√ 
√ 
Appendix 1 – Input Information 
√ 
√ 
√ 
Appendix 2 – 3 D model snap shots 
√ 
√ 
√ 
Appendix 3 – Supporting Information such as 
plot plan / layouts / escape drawings, etc.  
√ 
√ 
√ 
Appendix 4 – Dispersion Scenario Summary 
 
√ 
√ 
Appendix 5 – Correlation Assessment  
 
√ 
√ 
Appendix 6 – Dispersion results and contours 
 
 
√ 
Appendix 7 – Explosion Scenarios contours & 
results Summary 
 
 
√ 
Appendix 8 – Exceedance Curves  
 
√ 
√ 
Any other supporting information 
√ 
√ 
√

## Page 34

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
FLACS Specific Guidelines (Informative) 
APPENDIX 3 
 
Version No.: 1 
Effective date: August 2019 
Page 34 of 37 
ADNOC Classification: Internal 
 
 
FLACS SPECIFIC GUIDELINES (INFORMATIVE) 
Users shall be aware that FLACS may undergo revisions and the guidelines may change over time. Therefore, 
it is advised to follow the best practice guidelines in the form of user manual or latest FLACS course notes. 
However, the following may be useful as a starting point. 
GRID 
In FLACS, the grid is composed of cuboidal cells as a single-block Cartesian grid. It is possible to vary the mesh 
resolution in any of the Cartesian directions. 
 
The grid guidelines of FLACS recommends that the large objects (objects larger than 1.5 control volume) should 
be aligned with the grid lines, since the program that evaluates the porosities adjusts automatically the large 
objects to match with the mesh; and this can cause some undesired situations, like leak corners (i.e. if a wall is 
moved to match the closest grid line). It is important to check that the automatic alignment of floors and walls to 
grid does not create unintended gaps. FLACS uses a distributed porosity approach to model small obstacles. 
The distributed porosity approach involves assigning porosities to the individual mesh cells containing small “sub-
grid” obstacles. A volume porosity value of zero corresponds to a completely solid obstruction whilst a volume 
porosity value of one corresponds to free space. Additionally, FLACS calculates area porosities on each of the 
control volume faces. These area porosities play an important role in determining the local fluid flow. 
 
The numerical grid with cubical 2x2x2m cells is recommended generally for wind flow simulation.  
 
The FLACS current user manual for explosion simulations suggests the following:  
 
The user should always apply cubical grid cells in the combustion region. Deviations of the order 10% in aspect 
ratio is OK, deviations by a factor of 2 in aspect ratio is not OK. Space filled with gas from wall to wall must always 
be resolved by a minimum of 5-6 grid cells in smallest direction.  
 
Unconfined gas clouds as well as partially filled clouds should have a minimum of 13 grid cells across the cloud 
if both sides are unconfined, and a minimum of 10 grid cells in directions where cloud meets confinement on one 
side. It is not recommended to use non-cubical grids for explosion simulations. As they are often used for 
dispersion simulations, the dispersion simulation results should be mapped from the dispersion grid to a grid 
better suited for explosions. 
 
The grid can be stretched outside the combustion region in directions where pressure recordings are not of 
interest. In directions where pressure wave propagation is of interest, one should not stretch the grid because 
this will reduce the sharpness and quality of the pressures. A proper distance to external boundaries is important. 
At least 5-10 grid cells from vent opening to external boundary should be used in situations where the external 
explosion is not important. 
 
BOUNDARY CONDITIONS 
FLACS provides the following four boundary conditions for use with all simulations. 
 
Euler 
The inviscid flow equations (Euler equations) are discretized for a boundary element. This means that the 
momentum and continuity equations are solved on the boundary in the case of outflow. The ambient pressure is 
used as the pressure outside the boundary. A nozzle formulation is used in the case of inflow or sonic outflow. 
Warning: 
EULER boundary condition may give too low explosion pressures in unconfined situations. In such cases, the 
Simulation volume should be extended, and the Plane wave boundary condition should be applied.

## Page 35

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
FLACS Specific Guidelines (Informative) 
APPENDIX 3 
 
Version No.: 1 
Effective date: August 2019 
Page 35 of 37 
ADNOC Classification: Internal 
Nozzle 
A nozzle formulation is used for both sub-sonic inflow and outflow and sonic outflow. This condition is suitable 
for porous areas with small sharp-edged holes or grids (e.g. louvres and gratings). A discharge coefficient is 
calculated from the area porosity and a drag coefficient. NOZZLE condition has shown to give a bit higher 
explosion pressures than EULER, but it is more robust. 
Warning: 
NOZZLE boundary condition may give too low explosion pressures in unconfined situations. In such cases, the 
Simulation volume be extended, and the Plane wave boundary condition should be applied. 
 
Plane wave 
This boundary condition was designed to reduce the reflection of the pressure waves at open boundaries which 
occurs when using EULER or NOZZLE. The pressure wave reflection is caused by setting a fixed pressure at 
the boundary. PLANE_WAVE boundary condition extrapolates the pressure in such a way that reflections are 
almost eliminated for outgoing waves. 
 
Wind 
WIND boundary condition models an external wind field. Velocity and turbulence profiles are specified at the wind 
boundaries, either by setting some turbulence parameters manually or by choosing one of the atmospheric 
stability classes (Pasquill class). WIND boundary conditions are particularly applicable to dispersion scenarios. 
It is possible to apply WIND on both inflow and outflow boundaries and on boundaries where the flow is parallel 
to the boundary. 
Warning: 
In cases where a generated internal flow has a strong impact on the boundary flow, e.g. gas explosions, WIND 
should not be used. 
 
For wind flow simulation, wind boundary conditions are defined at the inlet faces: wind speed at a reference 
height and Pasquill stability class are the required inputs used to define the stability of the Atmospheric Boundary 
Layer (ABL) and calculate its turbulence properties. The WIND boundary condition should be applied on at least 
on two faces. 
 
For explosion simulations, it is recommended to use PLANE_WAVE boundary conditions with the boundaries far 
away so no products from combustion reaches the boundaries. For unconfined situations the distance to 
boundaries in all directions should be the same. 
 
The FLACS user manual recommends the following: 
 
 
For most explosion simulations, EULER can and should be used; 
 
For wind and dispersion simulations, NOZZLE boundary condition (similar to EULER) is more robust; 
 
PLANE WAVE boundary condition is recommended for explosion in low confinement; and 
 
and for far field blast propagation. Boundary must be extended far outside the explosion (Flames should 
not reach boundary). 
Typical boundary conditions for various simulations types are shown in the following Table.

## Page 36

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
FLACS Specific Guidelines (Informative) 
APPENDIX 3 
 
Version No.: 1 
Effective date: August 2019 
Page 36 of 37 
ADNOC Classification: Internal 
Table 1:  Typical Boundary Conditions 
Boundary Conditions 
Dispersion / 
Ventilation 
Explosion: Confined 
Explosion: 
Unconfined / Far – 
Field 
solid surface 
ground/sea 
ground/sea 
ground/sea 
EULER 
- 
all other 
- 
NOZZLE 
outflow 
- 
- 
PLANE WAVE 
- 
- 
all other 
WIND 
inflow/parallel 
boundaries 
- 
- 
 
SOURCE TERM 
(a) 
High Momentum Jets 
FLACS features a separate sub-model for high momentum gas. The sub-model calculates the approximate 
flow conditions a short distance downstream from the release point, where the jet has expanded to 
atmospheric conditions assuming that there is no air entrainment up to the point where the jet has 
expanded to atmospheric conditions. For modelling, the area of the expanded jet and the velocity at the 
pseudo-source after expansion is used. This is then entered manually into FLACS. It is important to ensure 
that the grid is sufficiently fine around the jet to avoid numerical diffusion.  
 
(b) 
Evaporating Liquid Pools 
FLACS can model evaporation from a steady-state liquid pool source. Only circular shaped pools can be 
modelled, and it is necessary to specify the evaporation rate of the liquid fuel.  
 
(c) 
Flashing Releases 
For modelling flashing releases, FLACS utility program “FLASH” can be used which calculates the location 
and characteristics of a pseudo-source for a flashing release to input as boundary conditions into FLACS. 
The model accounts for air entrainment, droplet rain-out and evaporation and provides source conditions 
at the position downstream from the release where the conditions are purely gas phase and the liquid 
fraction has either rained-out or evaporated.  
 
(d) 
Liquified Gases 
The modelling of dispersion from liquified gases (e.g. LPG, butane, ammonia) and liquids (e.g. heptane, 
hexane) can also be done in FLACS. The liquid will spread on the ground, evaporate and form a potentially 
hazardous gas cloud.  FLACS incorporates liquid releases on solid ground and on water.  The spread of 
the pool in FLACS is governed by the terrain elevation, the presence of obstructions and obstacles. 
Evaporation is locally driven by the heat transfer to the pool, the wind and flow over the pool, the 
temperature of the flow above the pool, and the vapor pressure of the evaporating species. 
 
DISPERSION 
The grid guidelines of FLACS recommend a four-step procedure for dispersion analysis:  
 
 
to cover the computational domain with a uniform grid; 
 
to refine the grid in the region of the release;  
 
to smooth the grid between the micro and macro grid; and  
 
to stretch the grid outside the main region towards the boundaries.

## Page 37

HSE Management System 
HSE Administration & Management Standards 
CFD Dispersion and Explosion Modelling 
FLACS Specific Guidelines (Informative) 
APPENDIX 3 
 
Version No.: 1 
Effective date: August 2019 
Page 37 of 37 
ADNOC Classification: Internal 
Concerning the refined grid dimensioning, the guidelines specify that the area of the expanded jet must be solved 
in only one cell and that the area across the jet of this cell should be larger than the area of the expanded jet but 
not larger than twice. Refinement needs only be done across jet direction (not along). The aspect ratio (the ratio 
between the smallest and largest side of the cell) of refined grid cells should be kept lower than two. 
 
The FLACS manual recommends a CFLC of 20 and a CFLV of 2 for dispersion simulation. The CFLC can be 
increased by the factor of grid refinement near the leak, i.e. if the region near the leak is refined by a factor of 3, 
the CFLC could be 60. It is advised that the suggested factoring for CFLC should be used to optimize the run 
times. 
 
The ‘frozen cloud’ concept may be employed to obtain, gas cloud sizes for variation in release rates. The frozen 
cloud principle assumes that for a given dispersion/ventilation scenario the variation in fuel concentration is 
approximately proportional to the ratio [leak rate/ventilation rate. For further details refer to the FLACS User 
Manual. 
 
The size of the equivalent stoichiometric cloud at the time of ignition is calculated as the amount of gas in the 
flammable range, weighted by the concentration dependency of the flame speed and expansion. For a scenario 
of high confinement, or a scenario where very high flame speeds (faster than speed of sound in cold air) are 
expected (either large clouds or very congested situations), only expansion-based weighting is used (denoted in 
FLACS dispersion simulation output variable as Q8). For most situations lower flame speeds are expected and 
the conservatism can be reduced. Here a weighting of reactivity and expansion is used (denoted as FLACS 
output variable Q9).  
 
The size the equivalent stoichiometric cloud is obtained directly from FLACS (Q8 or Q9 output variable) which is 
internally derived by integrating the gas volume in the flammable region weighted by the normalised laminar 
flame speed as a function of concentration as well as the expansion ratio for the actual gas mixture. 
 
IGNITION PROBABILITY MODELLING  
Two ignition probabilities (PI) should generally be established: 
 
 
PIconst = ignition probability from constant ignition sources (per m3 that is exposed to flammable gas for the 
first time in the last 1 second). 
 
PIintermittent = ignition probability for intermittent ignition sources (per m3 flammable volume and second). 
Constant ignition sources are expected to give ignition immediately upon contact with the cloud. The probability 
of ignition will be proportional with the new volume being exposed to flammable gas. The Q6 output from FLACS 
gives the cloud volume that was exposed to flammable gas concentrations for the first-time last second. 
 
From the CFD calculations the volume of the gas cloud with concentration between LFL and UFL will give the 
volume that may be ignited if exposed to an intermittent ignition source. This information should thus be related 
to the intermittent ignition frequencies defined. 
 
For each new time-step in the dispersion analysis, the following parameters shall be calculated as they affect the 
probability of ignition: 
 
 
Total volume exposed to flammable gas (within concentration between LEL and UEL) which can be ignited 
by intermittent ignition sources (Q9).  
 
New volume exposed to flammable gas which can be ignited by continuous ignition sources (Q6). 
Thus, for each time step (or each 1s) for each dispersion calculation, the probability for ignition from intermittent 
and constant ignition sources should be established, and this probability should be added to a gas cloud size 
class.

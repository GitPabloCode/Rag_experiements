

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERTMS/ETCS

## System Requirements Specification

## Chapter 4 Modes and Transitions

REF

:

SUBSET-026-4

ISSUE :

3.6.0

DATE  :

13/05/2016

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.1 Modification History

| Issue Number Date      | Section Number                     | Modification / Description                                                                      | Author         |
|------------------------|------------------------------------|-------------------------------------------------------------------------------------------------|----------------|
| Issue 0.0.1 1999-07-05 | /                                  | This document is based on 'SRS Class P - Modes and Transitions' issue 1.1.2 (ref. Subset-006-4) | Laffineur J.C. |
| Issue 0.0.2 1999-07-16 | /                                  | New modes/functions/transitions due to Class 1 scope, and impact from WPs (of 1999- 07-13).     | Laffineur J.C. |
| Issue 0.1.0 1999-07-23 | /                                  | Unisig Review - Stockholm - 22 & 23 July 1999                                                   | Laffineur J.C. |
| 1.0.0 1999-07-29       | Version number, editorial changes. | Finalisation meeting, Stuttgart 990729.                                                         | HE             |
| 1.2.0 990730           | Version number                     | Release version                                                                                 | HE             |
| 1.3.0 991209           | /                                  | Modifications due to Work Packages on SRS Class 1 v 1.0.0                                       | Laffineur J.C. |
| 1.4.0 991220           | /                                  | Modifications due to review meeting in Stockholm (991215 and 991216)                            | Laffineur J.C. |
| 1.4.1 991221           | /                                  | Presentation changes                                                                            | Laffineur J.C. |
| 2.0.0 991222           | Minor editing                      | Release version                                                                                 | Laffineur J.C. |
| 2.0.1                  | All                                | Modifications respect to Unisig review (doc. Unisig_all_com_SRS_2.0.0 _2)                       | Laffineur J.C. |
| 2.1.0                  | All                                | Modifications respect to Unisig review (doc. Unisig_all_com_SRS_2.0.1)                          | Laffineur J.C. |
| 2.2.0                  | Version number                     | UNISIG release                                                                                  | SAB            |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 2.2.2 02 02 01            | /                                                                                                                                                                                       | SUBSET-026 Corrected Paragraphs, Issue 2.2.2                                                                                                                                            | Laffineur J.C.   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| 2.2.4                     | Including all CLRs being in state 'EEIG' as per list of CLRs agreed by EEIG on 06/05/04.                                                                                                | Including all CLRs being in state 'EEIG' as per list of CLRs agreed by EEIG on 06/05/04.                                                                                                | Hougardy A.      |
| 2.2.4 SG checked 28/05/04 | Including all CLRs agreed with the EEIG (see 'List of CLRs agreed with EEIG for SRS v2.2.4' dated 28/05/04)                                                                             | Including all CLRs agreed with the EEIG (see 'List of CLRs agreed with EEIG for SRS v2.2.4' dated 28/05/04)                                                                             | H. Kast          |
| 2.2.5 21/01/05            | Incorporation of solution proposal for CLR 007 with EEIG users group comments Corrections according to erratum list agreed in SG meeting 170105                                         | Incorporation of solution proposal for CLR 007 with EEIG users group comments Corrections according to erratum list agreed in SG meeting 170105                                         | Hougardy A.      |
| 2.2.6 04/02/05            | Including all CLRs being in state 'EEIG pending' as per list of CLRs extracted on 28/01/05.                                                                                             | Including all CLRs being in state 'EEIG pending' as per list of CLRs extracted on 28/01/05.                                                                                             | Hougardy A.      |
| 2.2.7 16/06/05            | Including all CLRs extracted from "CR- Report_10.6.05-by number.rtf" and mentioned in column 2.2.7 in "CR status 13.6.05.xls"                                                           | Including all CLRs extracted from "CR- Report_10.6.05-by number.rtf" and mentioned in column 2.2.7 in "CR status 13.6.05.xls"                                                           | Hougardy A.      |
| 2.2.8 29/11/05            | Change marks cleaned up and updated according to last CRs decisions (including split of CRs7&126)                                                                                       | Change marks cleaned up and updated according to last CRs decisions (including split of CRs7&126)                                                                                       | Hougardy A.      |
| 2.2.9 24/02/06            | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.0.0 Removal of all CRs that are not classified as "IN" as per SUBSET-108 version 1.0.0, with the exception of | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.0.0 Removal of all CRs that are not classified as "IN" as per SUBSET-108 version 1.0.0, with the exception of | Hougardy A.      |
| 2.3.0 24/02/06            | Release version                                                                                                                                                                         | Release version                                                                                                                                                                         | HK               |
| 2.3.1 15/06/06            | Including SG CR decision made since SRS 2.2.8, correct errors in 2.2.8 detected when creating SRS 2.3.0                                                                                 | Including SG CR decision made since SRS 2.2.8, correct errors in 2.2.8 detected when creating SRS 2.3.0                                                                                 | Hougardy A.      |
| 2.3.2 17/03/08            | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.2.0 and all CRs that are in state 'Analysis completed' according to ERA CCM                                   | Including all CRs that are classified as "IN" as per SUBSET-108 version 1.2.0 and all CRs that are in state 'Analysis completed' according to ERA CCM                                   | Hougardy A.      |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 2.9.1 06/10/08   | Including all enhancement CR's retained for 3.0.0 baseline and all other error CR's that are in state 'Analysis completed' according to ERA CCM For editorial reasons, the following CR's are also included: CR656, CR804, CR821   | Hougardy A.   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| 3.0.0 23/12/08   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.0.1 22/12/09   | Including the results of the editorial review of the SRS 3.0.0 and the other error CR's that are in state 'Analysis completed' according to ERA CCM                                                                                | Hougardy A.   |
| 3.1.0 22/02/10   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.1.1 08/11/10   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR972 and 1000.                                                                                                                               | Hougardy A.   |
| 3.2.0 22/12/10   | Release version                                                                                                                                                                                                                    | Hougardy A.   |
| 3.2.1 13/12/11   | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR772                                                                                                                                         | Hougardy A.   |
| 3.3.0 07/03/12   | Baseline 3 release version                                                                                                                                                                                                         | Hougardy A.   |
| 3.3.1 04/04/14   | CR's 944, 1124, 1176, 1183, 1185                                                                                                                                                                                                   | Gemine O.     |
| 3.3.2 23/04/14   | Baseline 3 1 st maintenance pre-release version                                                                                                                                                                                    | Gemine O.     |
| 3.3.3 06/05/14   | CR 1223 Baseline 3 1 st maintenance 2 nd pre-release version                                                                                                                                                                       | Gemine O.     |
| 3.4.0 12/05/14   | Baseline 3 1 st maintenance release version                                                                                                                                                                                        | Gemine O.     |
| 3.4.1 23/06/15   | CR's 1033, 1094                                                                                                                                                                                                                    | Gemine O.     |
| 3.4.2 17/11/15   | CR's 539, 740, 933, 1087, 1089, 1091, 1107, 1128, 1187, 1190, 1197, 1249, 1262, 1265, 1266                                                                                                                                         | Gemine O.     |
| 3.4.3 16/12/15   | 1128 removed, 1117, 1283 plus update due to overall CR consolation phase                                                                                                                                                           | Gemine O.     |
| 3.5.0 18/12/15   | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC)                                                                                                                                                    | Gemine O.     |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 3.5.1    | CR 1249 reopening following RISC #75   | Gemine O.   |
|----------|----------------------------------------|-------------|
| 28/04/16 |                                        |             |
| 3.6.0    | Baseline 3 2 nd release version        | Hougardy A. |
| 13/05/16 |                                        |             |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.2 Table of Contents

| 4.1                                                                                                                              | Modification History...........................................................................................................2                                                                                                           | Modification History...........................................................................................................2                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4.2                                                                                                                              | Table of Contents..............................................................................................................6                                                                                                           | Table of Contents..............................................................................................................6                                                                                                                |
| 4.3                                                                                                                              | Introduction.......................................................................................................................8                                                                                                       | Introduction.......................................................................................................................8                                                                                                            |
| 4.3.1                                                                                                                            | 4.3.1                                                                                                                                                                                                                                      | Presentation of the document ....................................................................................8                                                                                                                              |
| 4.3.2                                                                                                                            | 4.3.2                                                                                                                                                                                                                                      | Identification of the possible modes...........................................................................8                                                                                                                                |
| 4.4 Definition 4.4.1                                                                                                             | 4.4 Definition 4.4.1                                                                                                                                                                                                                       | of the modes ...................................................................................................10 Introduction..............................................................................................................10 |
| 4.4.2 General                                                                                                                    | 4.4.2 General                                                                                                                                                                                                                              | Requirements.............................................................................................10                                                                                                                                     |
| 4.4.3 ISOLATION..............................................................................................................11  | 4.4.3 ISOLATION..............................................................................................................11                                                                                                            |                                                                                                                                                                                                                                                 |
| 4.4.4 NO POWER.............................................................................................................12    | 4.4.4 NO POWER.............................................................................................................12                                                                                                              |                                                                                                                                                                                                                                                 |
| 4.4.5 SYSTEM                                                                                                                     | 4.4.5 SYSTEM                                                                                                                                                                                                                               | FAILURE..................................................................................................13                                                                                                                                     |
| 4.4.6 SLEEPING...............................................................................................................14  | 4.4.6 SLEEPING...............................................................................................................14                                                                                                            |                                                                                                                                                                                                                                                 |
| 4.4.7 STAND                                                                                                                      | 4.4.7 STAND                                                                                                                                                                                                                                | BY...............................................................................................................16                                                                                                                             |
| 4.4.8 SHUNTING..............................................................................................................17   | 4.4.8 SHUNTING..............................................................................................................17                                                                                                             |                                                                                                                                                                                                                                                 |
| 4.4.9 FULL SUPERVISION...............................................................................................19          | 4.4.9 FULL SUPERVISION...............................................................................................19                                                                                                                    |                                                                                                                                                                                                                                                 |
| 4.4.10 UNFITTED...............................................................................................................20 | 4.4.10 UNFITTED...............................................................................................................20                                                                                                           |                                                                                                                                                                                                                                                 |
| 4.4.11 STAFF RESPONSIBLE                                                                                                         | 4.4.11 STAFF RESPONSIBLE                                                                                                                                                                                                                   | ...........................................................................................21                                                                                                                                                   |
| 4.4.12 ON SIGHT                                                                                                                  | 4.4.12 ON SIGHT                                                                                                                                                                                                                            | ...............................................................................................................24                                                                                                                               |
| 4.4.13 TRIP                                                                                                                      | 4.4.13 TRIP                                                                                                                                                                                                                                | ........................................................................................................................25                                                                                                                      |
| 4.4.14 POST TRIP..............................................................................................................26 | 4.4.14 POST TRIP..............................................................................................................26                                                                                                           |                                                                                                                                                                                                                                                 |
| 4.4.15 NON                                                                                                                       | 4.4.15 NON                                                                                                                                                                                                                                 | LEADING........................................................................................................28                                                                                                                               |
| 4.4.16 Intentionally deleted                                                                                                     | 4.4.16 Intentionally deleted                                                                                                                                                                                                               | .................................................................................................30                                                                                                                                             |
| 4.4.17 National System (SN)                                                                                                      | 4.4.17 National System (SN)                                                                                                                                                                                                                | mode.....................................................................................31                                                                                                                                                     |
| 4.4.18                                                                                                                           | 4.4.18                                                                                                                                                                                                                                     | REVERSING............................................................................................................32                                                                                                                         |
| 4.4.19 LIMITED SUPERVISION                                                                                                       | 4.4.19 LIMITED SUPERVISION                                                                                                                                                                                                                 | .........................................................................................34                                                                                                                                                     |
| 4.4.20 PASSIVE                                                                                                                   | 4.4.20 PASSIVE                                                                                                                                                                                                                             | SHUNTING..............................................................................................37                                                                                                                                        |
| 4.5 Modes and on-board functions........................................................................................39       | 4.5 Modes and on-board functions........................................................................................39                                                                                                                 |                                                                                                                                                                                                                                                 |
|                                                                                                                                  | Introduction..............................................................................................................39                                                                                                               | Introduction..............................................................................................................39                                                                                                                    |
| 4.5.1                                                                                                                            | 4.5.1                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                 |
| 4.5.2                                                                                                                            | 4.5.2                                                                                                                                                                                                                                      | Active Functions Table.............................................................................................39                                                                                                                           |
| 4.6                                                                                                                              | Transitions between modes ............................................................................................44                                                                                                                   | Transitions between modes ............................................................................................44                                                                                                                        |
| 4.6.1                                                                                                                            | 4.6.1                                                                                                                                                                                                                                      | Symbols...................................................................................................................44                                                                                                                    |
| 4.6.2                                                                                                                            | 4.6.2                                                                                                                                                                                                                                      | Transitions Table .....................................................................................................45                                                                                                                       |
| 4.6.3                                                                                                                            | Transitions Conditions Table....................................................................................46 DMI depending on modes...............................................................................................50 | Transitions Conditions Table....................................................................................46 DMI depending on modes...............................................................................................50      |
| 4.7.1                                                                                                                            | Introduction..............................................................................................................50                                                                                                               | Introduction..............................................................................................................50                                                                                                                    |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 4.7.2                                                                                                                                      | 4.7.2                                                                                                                                      | DMI versus Mode Table...........................................................................................50                         |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 4.8                                                                                                                                        | Acceptance of received information ................................................................................55                      | Acceptance of received information ................................................................................55                      |
| 4.8.1                                                                                                                                      | 4.8.1                                                                                                                                      | Introduction..............................................................................................................55               |
| 4.8.2                                                                                                                                      | 4.8.2                                                                                                                                      | Assumptions ............................................................................................................57                 |
| 4.8.3                                                                                                                                      | 4.8.3                                                                                                                                      | Accepted information depending on the level and transmission media ....................58                                                  |
| 4.8.4                                                                                                                                      | 4.8.4                                                                                                                                      | Accepted Information depending on the modes.......................................................64                                       |
| 4.8.5                                                                                                                                      | 4.8.5                                                                                                                                      | Handling of transition buffer in case of level transition announcement or RBC/RBC                                                          |
| handover................................................................................................................................68 | handover................................................................................................................................68 | handover................................................................................................................................68 |
| 4.9                                                                                                                                        | What happens to accepted and stored information when entering a given level .............70                                                | What happens to accepted and stored information when entering a given level .............70                                                |
| 4.9.1                                                                                                                                      | 4.9.1                                                                                                                                      | Introduction..............................................................................................................70               |
| 4.10                                                                                                                                       | What happens to accepted and stored information when entering a given mode........71                                                       | What happens to accepted and stored information when entering a given mode........71                                                       |
| 4.10.1                                                                                                                                     | 4.10.1                                                                                                                                     | Introduction..............................................................................................................71               |
| 4.11                                                                                                                                       | What happens to stored information when exiting NP mode .......................................75                                          | What happens to stored information when exiting NP mode .......................................75                                          |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.3 Introduction

## 4.3.1 Presentation of the document

- 4.3.1.1 This  document  defines  the  modes  of  the  ERTMS/ETCS  on-board  equipment  (see chapter 4.4 'Definition of the modes' and chapter 4.5 'Modes and on-board functions'.
- 4.3.1.2 This  document  gives  all  transitions  between  modes  (see  chapter  4.6  'Transitions between modes').
- 4.3.1.3 This document describes the possible exchanged information between the driver and the  ERTMS/ETCS on-board equipment, respect  to  the  mode  (see  chapter  4.7  'DMI depending on modes').
- 4.3.1.4 This  document  describes  how the received information is filtered,  respect  to  several criteria  such  as  the  level,  the  mode,  etc..  (see  chapter  4.8  'Acceptance  of  received information').
- 4.3.1.5 This  document  describes  how  the  stored  information  is  handled,  respect  to  several criteria such as the level, the mode, etc. (see chapter 4.9 'What happens to accepted and stored information when entering a given level', and chapter 4.10 'What happens to accepted and stored information when entering a given mode').
- 4.3.1.6 All  the  tables  that  are  included  in  this  document  shall  be  considered  as  mandatory requirements.
- 4.3.1.7 Some  notes  appear  in  this  document.  These  notes  are  here  to  help  the  reader  to understand the specifications, or to explain the reason(s) of a requirement.

## 4.3.2 Identification of the possible modes

4.3.2.1 List of the modes:

Full Supervision (FS)

Limited Supervision (LS)

On Sight (OS)

Staff Responsible (SR)

Shunting (SH)

Unfitted

(UN)

Passive Shunting (PS)

Sleeping (SL)

Stand By (SB)

Trip (TR)

## ERA * UNISIG * EEIG ERTMS USERS GROUP

Post Trip

(PT)

System Failure (SF)

Isolation (IS)

No Power (NP)

Non Leading (NL)

National System (SN)

Reversing (RV)

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4 Definition of the modes

## 4.4.1 Introduction

- 4.4.1.1 For each mode the following information is given:
- a) The context of utilisation of the mode and the functions that characterise the mode (chapter 'Description').
- b) The  ERTMS/ETCS  levels  in  which  the  mode  can  be  used  (chapter  'Used  in levels').
- c) The  related  responsibility  of  the  ERTMS/ETCS  on-board  equipment  and  of  the driver, once the equipment is in this mode (chapter 'Responsibilities').
- 4.4.1.2 A  complete  list  of  transitions  to  and  from  each  mode  is  given  in  the  section  4.6.2 'Transitions Table' ).

## 4.4.2 General Requirements

- 4.4.2.1 When the desk is open, a clear indication of the ERTMS/ETCS mode shall be shown to the driver.
- 4.4.2.2 Intentionally deleted.

## 4.4.3 ISOLATION

## 4.4.3.1 Description

- 4.4.3.1.1 In Isolation mode, the ERTMS/ETCS on-board equipment shall be physically isolated from  the  brakes  and  can  be  isolated  from  other  on-board  equipments/systems depending on the specific on-board implementation.
- 4.4.3.1.2 There  shall  be  a  clear  indication  to  the  driver  that  the  ERTMS/ETCS  on-board equipment is isolated.
- 4.4.3.1.3 To leave Isolation mode, a special operating procedure is needed (no transition from Isolation is specified). This procedure shall ensure that the on-board equipment is only put back into service when it has been proven that this is safe for operation.
- 4.4.3.1.4 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.3.2 Used in levels

- 4.4.3.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## 4.4.3.3 Responsibilities

- 4.4.3.3.1 Isolation of the ERTMS/ETCS on-board equipment is performed by the driver under his complete responsibility.
- 4.4.3.3.2 Once the ERTMS/ETCS on-board equipment is isolated, the ERTMS/ETCS on-board equipment has no more responsibility.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.4 NO POWER

## 4.4.4.1 Description

- 4.4.4.1.1 When the ERTMS/ETCS on-board equipment is not powered, the equipment is in the No Power mode.
- 4.4.4.1.1.1 Note:  in  order  to  ensure  cold  movement  detection  function,  some  parts  of  the ERTMS/ETCS on-board equipment may be fed by an auxiliary power supply.
- 4.4.4.1.2 The ERTMS/ETCS on-board equipment shall permanently command the emergency brake.
- 4.4.4.1.3 Note: for the list  of  main  functions  related  to this mode, refer to chapter  4.5 'Modes and on-board functions'.

## 4.4.4.2 Used in levels

- 4.4.4.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## 4.4.4.3 Responsibilities

- 4.4.4.3.1 The  ERTMS/ETCS  on-board  equipment  has  no  responsibility  in  this  mode,  except commanding the emergency brake and (optionally) monitoring cold movements.
- 4.4.4.3.2 The notion of responsibility of the driver is not relevant for the No Power mode.
- 4.4.4.3.3 If it is required to move a loco in NP mode as a wagon, ETCS brake command must be overridden by external means.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.5 SYSTEM FAILURE

## 4.4.5.1 Description

- 4.4.5.1.1 The  ERTMS/ETCS on-board  equipment  shall  switch  to  the  System  Failure  mode  in case of a fault, which affects safety.
- 4.4.5.1.2 The ERTMS/ETCS on-board equipment shall permanently command the Emergency Brakes.
- 4.4.5.1.3 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.5.2 Used in levels

- 4.4.5.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## 4.4.5.3 Responsibilities

- 4.4.5.3.1 The ERTMS/ETCS on-board equipment is responsible for commanding the Emergency Brakes.
- 4.4.5.3.2 No responsibility of the driver.

## 4.4.6 SLEEPING

## 4.4.6.1 Description

- 4.4.6.1.1 The Sleeping mode is defined to manage the ERTMS/ETCS on-board equipment of a slave engine that is remote controlled.
- 4.4.6.1.2 The  desk(s)  of  a  sleeping  engine  must  be  closed  (since  there  is  no  driver,  no information shall be shown).
- 4.4.6.1.3 As the engine is remote controlled by the leading engine, its ERTMS/ETCS on-board equipment shall not perform any train movement supervision.
- 4.4.6.1.4 The  ERTMS/ETCS on-board equipment shall perform the Train Position function; in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end.
- 4.4.6.1.5 Sleeping mode shall be automatically detected on-board via the train interface.
- 4.4.6.1.6 If  possible,  the  train  must  not  be  stopped  due  to  a  safety  critical  fault  in  a  sleeping engine. The ERTMS/ETCS on-board equipment should therefore try to memorise the occurrence  of  such  fault(s),  which  should  be  handled  when  the  engine  leaves  the Sleeping  mode.  The  ERTMS/ETCS  on-board  equipment  should  also  try  to  send  an error information to the RBC.
- 4.4.6.1.7 If  a  desk  of  the  sleeping  engine  is  opened  while  the  train  is  running  (this  is  an abnormal operation), the ERTMS/ETCS on-board equipment shall switch to Stand-By mode.
- 4.4.6.1.8 If  the  'sleeping  input  signal'  is  lost  (no  more  detection  of  the  remote  control),  the switch to Stand-By mode shall be made only if the train is at standstill.
- 4.4.6.1.9 Intentionally deleted.
- 4.4.6.1.10  The ERTMS/ETCS on-board equipment shall open a communication session with the RBC when at least one of the following events occurs:
- a) in all levels, on receipt of the order to contact the RBC.
- b) In level 2/3, when entering or exiting Sleeping mode (to report the change of mode to the RBC).
- c)  In  level  2/3,  when  a  safety  critical  fault  of  the  ERTMS/ETCS  on-board  equipment occurs (to report the fault to the RBC).
- 4.4.6.1.11  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.6.1.12  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.6.1.13  When in levels 2 or 3, if no compatible version has been established between the onboard  equipment  in  Sleeping  mode  and  the  RBC,  the  ERTMS/ETCS  onboard equipment shall react as specified in 3.5.3.7 d) 2 nd  bullet but no driver's indication shall be given.

## 4.4.6.2 Used in levels

- 4.4.6.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## 4.4.6.3 Responsibilities

- 4.4.6.3.1 The  ERTMS/ETCS  on-board  equipment  of  an  engine  in  Sleeping  mode  has  no responsibility for the train protection.
- 4.4.6.3.2 The notion of responsibility of the driver is not relevant for the Sleeping mode.
- 4.4.6.3.2.1 Note : The leading engine is responsible for the movement of the train. It is then the ERTMS/ETCS  on-board  equipment  of  the  leading  engine  that  is  fully/partially/not responsible for the train protection, with respect to its mode.

## 4.4.7 STAND BY

## 4.4.7.1 Description

- 4.4.7.1.1 The Stand-By mode is a default mode and cannot be selected by the driver.
- 4.4.7.1.2 It is in the Stand-By mode that the ERTMS/ETCS on-board equipment awakes.
- 4.4.7.1.3 Data  for  mission  are  collected  in  Stand-By  (see  SRS-chapter  5:  'Start  of  Mission' procedure).
- 4.4.7.1.4 In Stand-By mode, the desk of the engine can be open or closed. No interaction with the  driver  shall  be  possible  as  long  as  the  desk  is  closed,  except  isolation  of  the ERTMS/ETCS on-board equipment.
- 4.4.7.1.5 The ERTMS/ETCS on-board equipment shall perform the Standstill Supervision.
- 4.4.7.1.6 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.7.2 Used in levels

- 4.4.7.2.1 Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## 4.4.7.3 Responsibilities

- 4.4.7.3.1 The  ERTMS/ETCS  on-board  equipment  is  responsible  for  maintaining  the  train  at standstill.
- 4.4.7.3.2 The driver has no responsibility for train movements.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.8 SHUNTING

## 4.4.8.1 Description

- 4.4.8.1.1 The  purpose  of  the  Shunting  mode  is  to  enable  shunting  movements.  In  Shunting mode,  The  ERTMS/ETCS  on-board  equipment  shall  supervise  the  train  movements against:
- a) a ceiling speed: the shunting mode speed limit
- b) a list of expected balise groups (if such list was sent by the trackside equipment). The  train  shall  be  tripped  if  a  balise  group,  not  contained  in  the  list,  is  passed (When an empty list is sent, no balise group can be passed. When no list is sent, all balise groups can be passed)
- c) 'stop  if  in  shunting  mode'  information.  The  train  is  tripped  if  such  information  is received from balise groups
- d) Intentionally deleted
- 4.4.8.1.2 The Shunting mode shall not require Train Data.
- 4.4.8.1.3 The ERTMS/ETCS on-board equipment shall perform the Train Position function
- 4.4.8.1.4 Intentionally deleted.
- 4.4.8.1.5 When  in  Shunting  mode,  the  ERTMS/ETCS  on-board  shall  not  manage  level transitions. However,  an  immediate  level  transition  order  or  a conditional level transition order shall be stored and evaluated only when another mode than Shunting or Passive  Shunting has  been  entered  (i.e.  when  the  Shunting  movement  is terminated).
- 4.4.8.1.5.1 When receiving a communication session establishment order, the ERTMS/ETCS onboard in Shunting mode shall not establish the communication session, but shall store the RBC ID/phone number.
- 4.4.8.1.5.2 When  in  Shunting  mode,  the  ERTMS/ETCS  on-board  shall  not  manage  RBC-RBC hand-over, except for storing the RBC ID/phone number given at the RBC/RBC border.
- 4.4.8.1.6 Shunting  mode  can  be  selected  by  the  driver,  only  accepted  when  the  train  is  at standstill, or ordered by the trackside.
- 4.4.8.1.7 In case of selection of Shunting mode by the driver:
-  in  level  1  operations,  the  switch  to  shunting  is  always  accepted  by  the  on-board equipment
-  in  level  2  and  3  areas,  the  on-board  asks  the  trackside  for  an  authorisation.  The switch to shunting is possible only after receiving such authorisation. The trackside can send a list of balises, that the train is allowed to pass while in SH, together with the authorisation

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.8.1.8 In case of order to switch to Shunting mode from trackside, the order:
-  in level 1 is given by a balise group. A list of balises, that the train is allowed to pass after the entry in Shunting, can be sent together with the order
-  in level 2 and 3 is sent via radio. A list of balises, that the train is allowed to pass after the entry in Shunting, can be sent together with the order
- 4.4.8.1.9 When  the  switch  to  shunting  is  ordered  by  trackside,  a  driver  acknowledgement  is requested.
- 4.4.8.1.9.1 Note: in Shunting mode the train is only partially supervised, therefore it is necessary that the driver takes the responsibility.
- 4.4.8.1.10  The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed  and,  only  on driver request, the permitted speed. The display of the permitted speed shall also be stopped on driver request.
- 4.4.8.1.11  Intentionally deleted.
- 4.4.8.1.12  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.8.2 Used in levels

4.4.8.2.1 Used in level 0, NTC, 1, 2 and 3.

## 4.4.8.3 Responsibilities

- 4.4.8.3.1 The  ERTMS/ETCS  on-board  equipment  is  responsible  for  the  supervision  of  the shunting mode speed limit, and that the engine with the active antenna is tripped when passing  the  defined  border  of  the  shunting  area  (only  if  there  is  a  defined  border: balise  group  not  in  the  list  given  by  trackside,  or  balise  group  giving  the  information 'stop if in shunting').
- 4.4.8.3.2 The driver is responsible for :
- a) Remaining inside the shunting area defined by a procedure or an external system outside ERTMS/ETCS (also when the shunting area is protected by balises)
- b) Train/engine movements and shunting operations

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.9 FULL SUPERVISION

## 4.4.9.1 Description

- 4.4.9.1.1 The ERTMS/ETCS on-board equipment shall be in the Full Supervision mode when all train  and  track  data,  which  is  required  for  a  complete  supervision  of  the  train,  is available on board.
- 4.4.9.1.2 Full supervision cannot be selected by the driver, but is entered automatically when all necessary conditions are fulfilled.
- 4.4.9.1.3 To  be  in  Full  Supervision  mode,  SSP  and  gradient  are  not  required  for  the  whole length of the train, but must be available at least from the FRONT END of the train.
- 4.4.9.1.4 Once in Full Supervision mode, if SSP and gradient are not known for the whole length of the train, an indication 'ENTRY IN FULL SUPERVISION' shall be clearly displayed to the driver until SSP and gradient are known for the whole length of the train.
- 4.4.9.1.4.1 Note: this indication may also be displayed in case the train length has been increased, see 3.18.3.8.
- 4.4.9.1.5 The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile.
- 4.4.9.1.6 The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed,  the  permitted speed, the target distance and the target speed to the driver (this list is not exhaustive - refer to chapter 4.7 'DMI depending on modes').
- 4.4.9.1.7 Note: for the list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.9.2 Used in levels

- 4.4.9.2.1 Used in level 1, 2 and 3.

## 4.4.9.3 Responsibilities

- 4.4.9.3.1 The  ERTMS/ETCS  on-board  equipment  is  fully  responsible  for  the  train  protection (except for the 2 situations described below).
- 4.4.9.3.2 The  driver  is  responsible  for  respecting  the  EOA  when  approaching  an  EOA  with  a release speed.
- 4.4.9.3.3 When  'ENTRY  IN  FULL  SUPERVISION'  is  displayed  to  the  driver,  the  driver  is responsible for respecting speed restrictions that apply for the part of the train that is not covered by SSP and gradient data.

## 4.4.10 UNFITTED

## 4.4.10.1 Description

- 4.4.10.1.1  The Unfitted mode is used to allow train movements in either:
- a)  Areas that are equipped neither with ERTMS/ETCS track-side equipment nor with national train control system
- b) Intentionally deleted
- c) Areas that  are  equipped  with  ERTMS/ETCS trackside equipment and/or  national train  control  system(s),  but  operation  under  their  supervision  is  currently  not possible
- 4.4.10.1.2  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a ceiling  speed:  the  lowest  of  the  maximum  train  speed  and  the  Unfitted  mode  speed limit for unfitted area (national value).
- 4.4.10.1.2.1 Intentionally deleted.
- 4.4.10.1.3  The ERTMS/ETCS  on-board  equipment  shall also supervise temporary speed restrictions.
- 4.4.10.1.4  The ERTMS/ETCS on-board equipment shall display the train speed to the driver.
- 4.4.10.1.5  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.10.2 Used in levels

- 4.4.10.2.1  Used in level 0.

## 4.4.10.3 Responsibilities

- 4.4.10.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed and (if available) temporary speed restrictions.
- 4.4.10.3.2  The driver must respect the existing line-side signals and is fully responsible for train movements.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.11 STAFF RESPONSIBLE

## 4.4.11.1 Description

- 4.4.11.1.1  The  Staff  Responsible  mode  allows  the  driver  to  move  the  train  under  his  own responsibility in an ERTMS/ETCS equipped area.
- 4.4.11.1.2  This mode is used when the system does not know the route. For example:
- a) After the ERTMS/ETCS on-board equipment starts-up (awakening of the train).
- b) To pass a signal at danger / override an EOA.
- c)  After a trackside failure (for example: loss of radio contact).
- 4.4.11.1.3  The ERTMS/ETCS on-board equipment shall supervise train movements against :
- a) a ceiling speed: the staff responsible mode speed limit
- b) a given distance (regarding its origin location see 4.4.11.1.3.1). The ERTMS/ETCS on-board equipment shall supervise braking curves with a target speed of zero to the end of this distance. If the train overpasses this distance (see next note) the ERTMS/ETCS on-board equipment shall trip the train
- c) a  list  of  expected  balise  groups,  if  this  list  has  been  sent  by  the  RBC.  The  train shall  be  tripped  if  over-passing  a  balise  group  that  is  not  in  the  list.  (When  an empty list is sent, no balise group can be passed. When no list is sent, all balise groups can be passed)
- d) balise groups giving the order 'stop if in SR'. This order shall immediately trip the train, unless the over-passed balise group is included in a list of expected balises as defined in item c)
- e) running  in  the  direction  opposite  to  the  train  orientation  (reverse  movement protection)
- 4.4.11.1.3.1 The ERTMS/ETCS on-board shall determine the start location of the SR distance as follows:
- a) If  the  National/Default value determines the max permitted distance to run in SR mode, the starting point of this distance shall refer to the estimated position of the train  front  when  SR  mode  was  entered,  or,  already  in  Staff  Responsible  mode, when Override was activated.
- b) If  the  max  permitted  distance  to  run  in  SR  mode  is  determined  by  the  value transmitted by the RBC, or entered by the driver, the start location of the distance shall refer to the estimated position of the train front when the distance information is received or entered.
- c) If  the  max  permitted  distance  to  run  in  SR  mode  is  determined  by  the  value transmitted by EUROLOOP, the distance information transmitted by EUROLOOP shall be referred to one or more reference balise groups. On-board shall evaluate

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

the distance to run in SR mode by matching the reference balise groups given with the LRBG.

In case the LRBG is, due to a change of orientation, in front of the train when the distance to run in SR mode is to be determined from the EUROLOOP information, the  complete  distance  to  run  in  SR  mode  shall  be  determined  as  the  distance given by EUROLOOP plus the distance between the estimated train front end and the LRBG.

- 4.4.11.1.4  Note:  Since  the  gradient  is  unknown,  the  supervision  of  the  braking  curves  in  Staff Responsible mode does not ensure that the train will not pass the given distance.
- 4.4.11.1.5  The ERTMS/ETCS on-board equipment shall give the possibility to the driver to modify the value of the SR mode speed limit and of the given distance. This shall be possible only at standstill.
- 4.4.11.1.5.1 If a train movement is detected while the driver is entering the SR speed/distance limits, the ERTMS/ETCS on-board equipment shall trigger the brake command.
- 4.4.11.1.5.2 The unit, range and resolution of the SR mode speed limit and distance entered by the driver shall be as specified in A.3.11.
- 4.4.11.1.6  If  the  level  is  2/3  and  a  communication  session  is  open,  the  driver  shall  have  the possibility to request a new distance to run in Staff Responsible, by selecting "Start". This triggers an MA request.
- 4.4.11.1.6.1 Note: Once the SR distance is covered, the driver may have to go further.
- 4.4.11.1.6.2 When entering SR mode, the value applicable for SR mode speed limit and the value applicable for  SR  distance  shall  be  the  corresponding  National/Default  values. Exception for SR distance: SR mode is authorised by RBC giving an SR distance.
- 4.4.11.1.6.3 While in SR mode, the value applicable for the SR mode speed limit shall be, if available, the last value entered by the driver.
- 4.4.11.1.6.4 While in SR mode, the value applicable for the SR distance shall be, if available, the last value received by the ERTMS/ETCS on-board equipment amongst:
- a) the distance to run in SR entered by the driver;
- b) the distance to run in SR given by trackside.
- 4.4.11.1.6.5 When "Override" is selected, the SR mode speed limit value and the SR distance value previously entered by driver or given by trackside, if any, shall be deleted. The corresponding National/Default values shall enter in force.
- 4.4.11.1.6.6 If  the  train  is  in  SR  and  receives  a  new  distance  to  run  in  SR  mode  from  the RBC,  the  stored  list  of  expected  balise  groups,  if  any,  shall  be  deleted  or  shall  be replaced by the list of expected balise groups sent together with the distance to run in SR.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.11.1.6.7 If an ERTMS/ETCS on-board equipment in SR mode, after having received from EUROLOOP max permitted distance to run in SR mode information, detects the main signal  balise  group  being  part  of  this  information  then  it  shall  ignore  any  new  max permitted distance to run in SR mode information from that loop.
- 4.4.11.1.7  The  ERTMS/ETCS on-board equipment shall display the train speed and the (when active)  override  (permission to pass a signal at danger, trip inhibited). The permitted speed, target distance and the target speed shall be displayed only on driver request, until the driver requests to stop their display.
- 4.4.11.1.8  Intentionally deleted.
- 4.4.11.1.9  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information.
- 4.4.11.1.10  Note: for  the  list  of  main  functions  related  to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.11.1.11  Intentionally deleted.

## 4.4.11.2 Used in levels

- 4.4.11.2.1  Level 1, 2 and 3.

## 4.4.11.3 Responsibilities

- 4.4.11.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed, a SR distance if finite and, if available, a list of balises.
- 4.4.11.3.2  The driver must check if the track is free, if points are correctly positioned, and must respect the existing line-side information (signals, speed boards etc.).
- 4.4.11.3.3  When using the possibility to modify the value of the SR mode speed limit and of the given distance, the driver is responsible for entering reasonable values.

## 4.4.12 ON SIGHT

## 4.4.12.1 Description

- 4.4.12.1.1  The On Sight mode enables the train to enter into a track section that could be already occupied by another train, or obstructed by any kind of obstacle.
- 4.4.12.1.2  On  Sight  mode  cannot  be  selected  by  the  driver,  but  shall  be  entered  automatically when commanded by trackside and all necessary conditions are fulfilled.
- 4.4.12.1.3  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile.
- 4.4.12.1.4  The ERTMS/ETCS on-board equipment shall display the train speed to the driver. The permitted  speed,  target  distance,  target  speed  and  release  speed  (if  any)  shall  be displayed only on driver request, until the driver requests to stop their display (this list is not exhaustive - refer to chapter 4.7 'DMI depending on modes').
- 4.4.12.1.5  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information.
- 4.4.12.1.6  To be in On Sight mode, SSP and gradient are not required for the whole length of the train, but must be available at least from the FRONT END of the train.
- 4.4.12.1.7  Once in On Sight mode, if SSP and gradient are not known for the whole length of the train, an indication 'ENTRY IN ON SIGHT' shall be clearly displayed to the driver until SSP and gradient are known for the whole length of the train.
- 4.4.12.1.7.1 Note:  this  indication  may  also  be  displayed  in  case  the  train  length  has  been increased, see 3.18.3.8.

## 4.4.12.1.8  Deleted

- 4.4.12.1.9  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.12.2 Used in levels

- 4.4.12.2.1  Used in level 1, 2 and 3.

## 4.4.12.3 Responsibilities

- 4.4.12.3.1  The ERTMS/ETCS on-board equipment is responsible for the supervision of the train movements.
- 4.4.12.3.2  The  driver  is  responsible  for  checking  the  track  occupancy  when  moving  the  train, because the track may be occupied.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.13 TRIP

## 4.4.13.1 Description

## 4.4.13.1.1  Deleted

- 4.4.13.1.1.1 Note: Application of emergency brakes and train trip are two different things. For example, exceeding the permitted speed leads to application of the emergency brakes, but as long as the train does not pass the EOA/LOA, it is not a train trip.
- 4.4.13.1.2  The  ERTMS/ETCS  on-board  equipment  shall  command  the  emergency  brakes  (no brake release is possible in Trip mode).
- 4.4.13.1.3  The ERTMS/ETCS on-board equipment shall indicate to the driver the reason of the train trip.
- 4.4.13.1.4  The ERTMS/ETCS on-board equipment shall request an acknowledgement from the driver once train is at standstill (to allow the driver to acknowledge the train trip).
- 4.4.13.1.4.1 Note: This acknowledgement is mandatory to exit from Trip mode.
- 4.4.13.1.5  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.13.1.6  Closing  the  desk  while  being  in  Trip  mode  will  not  cause  a  mode  change  but  no interaction  with  the  driver  shall  be  possible  as  long  as  the  desk  is  closed,  except isolation of the ERTMS/ETCS on-board equipment

## 4.4.13.2 Used in levels

- 4.4.13.2.1  Used in level 0, NTC, 1, 2 and 3.

## 4.4.13.3 Responsibilities

- 4.4.13.3.1  The  ERTMS/ETCS on-board equipment is responsible for stopping the train and for maintaining the train at standstill.
- 4.4.13.3.2  The driver has no responsibility for train movements.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.14 POST TRIP

## 4.4.14.1 Description

- 4.4.14.1.1  The Post Trip mode shall be entered immediately after the driver acknowledges the trip.
- 4.4.14.1.2  Once  in  post  trip  mode,  the  onboard  equipment  shall  release  the  Command  of  the emergency brake.
- 4.4.14.1.2.1 The ERTMS/ETCS on-board equipment shall keep on indicating to the driver the reason of the train trip.
- 4.4.14.1.3  The train shall only be authorised to move backwards a given distance (national value). The  ERTMS/ETCS  on-board  equipment  shall  supervise  this  national  distance  for reverse  movements,  and  shall  command  the  service  brakes  if  the  distance  is  overpassed. The driver shall be informed about the reason for the brake application.
- 4.4.14.1.3.1 Note:  The  ERTMS/ETCS onboard equipment performs the Reverse Movement Protection (as in PT mode, the "normally allowed movement" is backwards, then the Reverse Movement Protection avoids the train running in forward direction when in PT mode). This implies that the given distance to run backwards in PT is considered as a directional data, oriented backwards.
- 4.4.14.1.3.2 After  the  release  of  a  brake  command initiated due to an overpassed distance allowed  for  moving  backwards  in  Post  Trip  mode,  the  ERTMS/ETCS  on-board equipment shall command the service brake for any further movement in the direction opposite to the train orientation.
- 4.4.14.1.4  When moving backwards in Post Trip mode, the train trip shall be inhibited.
- 4.4.14.1.5  Intentionally deleted.
- 4.4.14.1.6  When  ERTMS/ETCS  level  is  1,  if  the  driver  selects  'Start'  the  onboard  equipment proposes Staff Responsible. When ERTMS/ETCS level is 2 or 3, the selection of Start leads  to  an  MA  Request  to  the  RBC.  It  is  the  RBC  responsibility  to  give  an  SR authorisation, or a Full Supervision MA  or an On  Sight/Shunting MA  to an ERTMS/ETCS equipment that is in Post Trip mode.
- 4.4.14.1.7  Intentionally deleted.
- 4.4.14.1.8  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.14.1.9  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake.

## 4.4.14.2 Used in levels

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.14.2.1  Used in level 1, 2 and 3.

## 4.4.14.3 Responsibilities

- 4.4.14.3.1  The  ERTMS/ETCS  on-board  equipment  is  responsible  for  supervising  that  the  train moves  only  backwards  and  that  the  backward  movement  does  not  exceed  the maximum permitted distance (national value).
- 4.4.14.3.2  The driver is responsible if moving the train backwards.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.15 NON LEADING

## 4.4.15.1 Description

- 4.4.15.1.1  The Non-Leading mode is defined to manage the ERTMS/ETCS on-board equipment of a slave engine that is NOT electrically coupled to the leading engine (and so, not remote controlled) but has its own driver.
- 4.4.15.1.1.1 Note: This operating situation is called Tandem.
- 4.4.15.1.1.2 The ERTMS/ETCS on-board equipment shall use, as a necessary condition to enter in Non-Leading mode, a 'non leading input signal" from the train interface.
- 4.4.15.1.1.3 If  the  'non  leading  input  signal"  is  no  longer  present,  the  switch  to  Stand-By mode shall be made only if the train is at standstill.
- 4.4.15.1.2  The  ERTMS/ETCS  on-board  equipment  shall  not  perform  any  train  movement supervision in Non-Leading mode.
- 4.4.15.1.3  The  ERTMS/ETCS  on-board  equipment  shall  perform  the  Train  Position  function;  in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end.
- 4.4.15.1.4  When level is 2 or 3, the ERTMS/ETCS on-board equipment shall report its position to the RBC, according to the previously received parameters.
- 4.4.15.1.5  If possible, the train must not be stopped due to a safety critical fault in a non-leading engine. The ERTMS/ETCS on-board equipment should therefore try to memorise the occurrence  of  such  fault(s),  which  should  be  handled  when  the  engine  leaves  Non Leading  mode.  The  ERTMS/ETCS  on-board  equipment  should  also  try  to  send  an error information to the RBC.
- 4.4.15.1.6  The ERTMS/ETCS on-board equipment shall display the train speed to the driver.

## 4.4.15.1.7  Intentionally deleted

- 4.4.15.1.8  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.15.1.9  The supervision of linking consistency shall not be performed in Non Leading mode.
- 4.4.15.1.10  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake.

## 4.4.15.2 Used in levels

- 4.4.15.2.1  Used in all levels: Level 0, level 1, level 2, level 3 and level NTC.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.15.3 Responsibilities

- 4.4.15.3.1  The  ERTMS/ETCS  on-board  equipment  performs  NO  protection  functions,  except forwarding track conditions associated orders through DMI or train interface.
- 4.4.15.3.2  The driver is responsible for obeying the orders associated to track conditions, when they are displayed by the DMI.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.16 Intentionally deleted

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.17 National System (SN) mode

## 4.4.17.1 Description

- 4.4.17.1.1  In SN mode, according to the specific on-board implementation, the National System may access the following resources via the ERTMS/ETCS on-board equipment: DMI, Juridical  Recording  interface,  odometer,  train  interface  and  brakes.  This  can  be achieved through the STM interface.
- 4.4.17.1.2  A limited set of data coming from balises shall be used by the ERTMS/ETCS on-board equipment, refer to SRS chapter 4.8 'Use of received information'.
- 4.4.17.1.3  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.

## 4.4.17.2 Used in levels

- 4.4.17.2.1  Level NTC.

## 4.4.17.3 Responsibilities of ERTMS/ETCS Onboard

- 4.4.17.3.1  No train supervision functionality is provided by the ERTMS/ETCS  on-board equipment. In case the ERTMS/ETCS on-board equipment is interfaced to the National System  through  an  STM,  refer  to  the  FFFIS  STM  (Subset  035)  for  the  functionality provided by ERTMS/ETCS on-board.
- 4.4.17.3.2  Intentionally deleted.

## 4.4.17.4 Responsibilities of the National System

- 4.4.17.4.1  The National System is responsible for all train supervision and protection functions.
- 4.4.17.4.2  The National System is responsible for issuing and revoking brake command.
- 4.4.17.4.3  The  National  System  is  responsible  for  maintaining  national  system  behaviour  and interact with national trackside equipment.
- 4.4.17.4.4  The National System is responsible for interaction with the driver.

## 4.4.17.5 Responsibilities of the driver

- 4.4.17.5.1  The responsibility of the driver depends on the National System in use.

## 4.4.18 REVERSING

## 4.4.18.1 Description

- 4.4.18.1.1  The Reversing mode allows the driver to change the direction of movement of the train and  drive  from  the  same  cab,  i.e.  the  train  orientation  remains  unchanged.  This  is possible only in areas so marked by trackside.
- 4.4.18.1.2  Note: This mode is used to allow the train to escape from a dangerous situation and to reach as fast as possible a 'safer' location.
- 4.4.18.1.3  The ERTMS/ETCS on-board equipment shall supervise train movements against :
- a) a ceiling speed: the Reversing mode speed limit given from trackside
- b) a  distance  to  run  in  the  direction  opposite  to  the  train  orientation,  given  from trackside. The emergency brake shall be commanded if overpassing this distance
- 4.4.18.1.4  After  the  release  of  a  brake  command  initiated  due  to  an  overpassed  reversing distance, and while the reversing distance is still overpassed, the ERTMS/ETCS onboard equipment shall command the emergency brake for any further movement in the direction opposite to the train orientation.
- 4.4.18.1.5  The  ERTMS/ETCS  on-board  equipment  shall  display  the  train  speed,  the  permitted speed and the remaining distance to run.
- 4.4.18.1.6  In  case  the  SBI  supervision  limit  is  exceeded  (refer  to  chapter  3  table  5,  triggering condition  t4),  the  ERTMS/ETCS on-board equipment shall command the emergency brake instead of the service brake. For the revocation of the brake command, refer to 3.13.10.2.4.
- 4.4.18.1.7  The  position  reports  sent  when  in  reversing  mode  shall  refer  to  the  location  of  the driving cab (as before reversing).
- 4.4.18.1.8  Note:  The  ERTMS/ETCS  onboard  equipment  performs  the  Reverse  Movement Protection (as in RV mode, the "normally allowed movement" is backwards, then the Reverse Movement Protection avoids the train running in forward direction when in RV mode).  This  implies  that  the  given  distance  to  run  in  reversing  is  considered  as  a directional data, oriented backwards.
- 4.4.18.1.9  Note: for the list of main functions related to this mode, refer to chapter 4.5 'Modes and on-board functions'.
- 4.4.18.1.10  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake.
- 4.4.18.1.11  In case there is an alarm reporting a malfunction for the onboard balise transmission function, the ERTMS/ETCS onboard equipment shall ignore this alarm.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.18.1.12  In  case  the  ERTMS/ETCS  system  version  number  X  transmitted  by  any  balise  is greater  than  the  highest  version  X  supported  by  the  onboard  equipment  (refer  to 3.17.3.5), the information from this balise shall be ignored, the train shall not be tripped and the driver shall not be informed.

## 4.4.18.2 Used in levels

- 4.4.18.2.1  Level 1, 2, 3.

## 4.4.18.3 Responsibilities

- 4.4.18.3.1  The ERTMS/ETCS on-board equipment supervises a ceiling speed and a distance to run in reverse direction.
- 4.4.18.3.2  The driver must keep the train movement inside the received distance to run.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.19 LIMITED SUPERVISION

## 4.4.19.1 Description

- 4.4.19.1.1  The  Limited  Supervision  mode  enables  the  train  to  be  operated  in  areas  where trackside information can be supplied to realise background supervision of the train.
- 4.4.19.1.2  Limited supervision can not be selected by the driver, but shall be entered automatically when commanded by trackside and all necessary conditions are fulfilled.
- 4.4.19.1.3  The  ERTMS/ETCS  on-board  equipment  shall  supervise  train  movements  against  a dynamic speed profile.
- 4.4.19.1.4  The ERTMS/ETCS on-board equipment shall display the train speed and the release speed,  if  any  (this  list  is  not  exhaustive  -  refer  to  chapter  4.7  'DMI  depending  on modes'). Upon request by trackside (refer to clauses 4.4.19.1.4.2 to 4.4.19.1.4.6) if the generic LS  function marker  is stored on-board  or if the conditions in clause 4.4.19.1.4.7 are fulfilled, the ERTMS/ETCS on-board equipment shall also display the lowest speed amongst:
- a) the lowest MRSP element between the minimum safe front end of the train and the EOA/LOA, AND
- b) the target speed at the EOA/LOA
- 4.4.19.1.4.1 The speed resulting from 4.4.19.1.4 a) and b) is called the Lowest Supervised Speed within the Movement Authority (LSSMA)
- 4.4.19.1.4.2 Upon  an  order  to  toggle  on  the  LSSMA  display,  the  ERTMS/ETCS  on-board equipment shall start a delay timer:
- a) For order received from RBC/RIU: at the value of the time stamp of the message including the order.
- b) For  order  received  from  balise  group:  at  the  time  of  passage  over  the  first encountered balise of the balise group giving the order.
- c)  Exception to a) and b): for order that has been stored in the level transition buffer (see section 4.8.3): at the time the level transition is performed.
- 4.4.19.1.4.3 When the delay timer value becomes greater than the time-out value given by trackside, the ERTMS/ETCS on-board equipment shall display the LSSMA.
- 4.4.19.1.4.4 On reception of an order to toggle (on or off) the LSSMA display, a toggle on order  which  has  not  been  executed  yet  (because  the  on-board  delay  timer  has  not reached the delay time-out value) shall be deleted by the on-board equipment.
- 4.4.19.1.4.5 If  the  LSSMA  display  is  already  toggled  on,  the  ERTMS/ETCS  on-board equipment shall toggle off the LSSMA display in case:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- a) the clause 4.4.19.1.4.3 is not immediately fulfilled upon reception of a new order to toggle on the LSSMA display
- b) an order to toggle off the LSSMA display is received.
3. 4.4.19.1.4.6 When  entering  the  Limited  Supervision  mode,  the  LSSMA  display  shall  be toggled  off  by  the  ERTMS/ETCS  on-board  equipment,  unless  a  toggle  on  order  is received  and  leads  immediately  to  the  display  of  the  LSSMA  as  per  clauses 4.4.19.1.4.2 and 4.4.19.1.4.3.
4. 4.4.19.1.4.7 If the generic LS function marker is not stored on-board, the clauses 4.4.19.1.4.2 to 4.4.19.1.4.6 shall not apply and the LSSMA shall be displayed if:
- a) the target speed at the EOA/LOA is lower than the Limited Supervision mode speed limit, AND
- b) the LSSMA is lower than the maximum train speed.
7. 4.4.19.1.4.8 The generic LS function marker shall be deleted by the ERTMS/ETCS on-board equipment as soon as a Limited Supervision mode profile is received without it in the same balise group message.
8. 4.4.19.1.5  If  receiving  a  "track  ahead  free"  request  from  the  RBC,  the  ERTMS/ETCS on-board equipment requests the driver to enter the "track ahead free" information.
9. 4.4.19.1.6  To be in Limited Supervision mode, SSP and gradient are not required for the whole length of the train, but shall be at least available from the FRONT END of the train.
10. 4.4.19.1.7  Note: for the list of main functions related to this mode, refer to 4.5 'Modes and  onboard functions'.

## 4.4.19.2 Used in levels

- 4.4.19.2.1  Used in levels 1, 2 and 3.

## 4.4.19.3 Responsibilities

- 4.4.19.3.1  The ERTMS/ETCS on-board equipment is responsible for the background supervision of the train movement to the extent permitted by the information provided by trackside.
- 4.4.19.3.1.1 Note: The Limited Supervision mode enables the train to be operated in areas equipped with lineside signals where ETCS does not have information regarding the status of some signals, i.e. not all signals are fitted with LEUs or connected to an RBC
- 4.4.19.3.2  The  driver  must  always  observe  the  existing  line-side  information  (signals,  speed boards etc.) and National operating rules.
- 4.4.19.3.2.1 Note: the indications  given  to  the  driver  by  the  ERTMS/ETCS  on-board equipment do not substitute the observance of the line-side information. In particular the  display  of  the  LSSMA, if  deemed necessary by the trackside, only complements

## ERA * UNISIG * EEIG ERTMS USERS GROUP

the line-side information, e.g. in case there could be a discrepancy between this latter and the background supervision.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.4.20 PASSIVE SHUNTING

## 4.4.20.1 Description

- 4.4.20.1.1  The  Passive  Shunting  mode  is  defined  to  manage  the  ERTMS/ETCS  on-board equipment of a slave engine (NOT remote controlled, but mechanically coupled to the leading engine), being part of a shunting consist. This mode can also be used to carry on a shunting movement with a single engine fitted with one on-board equipment and two cabs, when the driver has to change the driving cab.
- 4.4.20.1.2  The desk of a Passive Shunting engine must be closed (since there is no driver, no information shall be shown).
- 4.4.20.1.3  As the engine is coupled to a leading engine, its ERTMS/ETCS on-board equipment shall not perform any train movement supervision.
- 4.4.20.1.4  The  ERTMS/ETCS  on-board  equipment  shall  perform  Train  Position  function;  in particular, the front/rear end of the engine (i.e., not the train) shall be used to refer to train front/rear end.
- 4.4.20.1.5  It shall only be possible to enter in Passive Shunting mode from the Shunting mode; while  in  Shunting  mode,  the  driver  shall  have  the  possibility  to  enable  the  function 'Continue Shunting on desk closure'.
- 4.4.20.1.6  When the active desk is closed, the ERTMS/ETCS on-board equipment shall switch to Passive Shunting mode if the function 'Continue Shunting on desk closure' is active and  the  'passive  shunting  input  signal'  is  received  from  the  train  interface.  If  the function  'Continue  Shunting  on  desk  closure'  is  not  active  or  the  'passive  shunting input  signal'  is  not  present,  the  ERTMS/ETCS  on-board  equipment  shall  switch  to Stand-By mode instead.
- 4.4.20.1.7  The special function 'Continue Shunting on desk closure' shall allow one and only one transition from Shunting mode to Passive Shunting mode. The special function shall be inactive once the Shunting mode is left.
- 4.4.20.1.8  If  a  desk  of  the  Passive  Shunting  engine  is  opened  and no  'Stop Shunting on desk opening'  information  previously  received  from  balise  group  is  stored  onboard,  the ERTMS/ETCS on-board equipment shall switch to Shunting mode.
- 4.4.20.1.9  If  a  desk  of  the  Passive  Shunting  engine  is  opened  and  'Stop  Shunting  on  desk opening'  information  previously  received  from  balise  group  is  stored  onboard,  the ERTMS/ETCS on-board equipment shall switch to Stand By mode.
- 4.4.20.1.10  If  possible,  the  train  must  not  be  stopped  due  to  a  safety  critical  fault  in  a  Passive Shunting  engine.  The  ERTMS/ETCS  on-board  equipment  should  therefore  try  to memorise the occurrence of such fault(s), which should be handled when the engine leaves the Passive Shunting mode.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 4.4.20.1.11  When in Passive Shunting mode, the ERTMS/ETCS on-board shall not manage level transitions.  However,  an  immediate  level  transition  order  or  a conditional level transition order shall be stored and shall be evaluated only when another mode than Shunting or Passive Shunting has been entered (i.e. when the Shunting movement is terminated).
- 4.4.20.1.12  When receiving a communication session establishment order, the ERTMS/ETCS onboard  in  Passive  Shunting  mode  shall  not  establish  the  communication  session,  but shall store the RBC ID/phone number information.
- 4.4.20.1.13  When in Passive Shunting mode, the ERTMS/ETCS on-board shall not manage RBCRBC hand-over, except for storing the RBC ID/phone number information given at the RBC/RBC border.
- 4.4.20.1.14  Note: for  the  list  of  main  functions  related  to this mode, refer to chapter  4.5 'Modes and on-board functions'.
- 4.4.20.1.15  In case of balise group message consistency error (refer to 3.16.2.4.4 and 3.16.2.5.1), the ERTMS/ETCS onboard equipment shall not command the service brake.

## 4.4.20.2 Used in levels

- 4.4.20.2.1  Used in all levels: Level 0, level 1, level 2, level 3 and level NTC

## 4.4.20.3 Responsibilities

- 4.4.20.3.1  The ERTMS/ETCS on-board equipment of an engine in Passive Shunting mode has no responsibility for the train protection.
- 4.4.20.3.2  The notion of responsibility of the driver is not relevant for the Passive Shunting mode.
- 4.4.20.3.3  Note: The leading engine is responsible for the movement of the train. It is then the ERTMS/ETCS  on-board  equipment  of  the  leading  engine  that  is  fully/partially/not responsible for the train protection, with respect to its mode.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.5 Modes and on-board functions

## 4.5.1 Introduction

4.5.1.1 The following table specifies in which modes the on-board functions are active or not. The functions are described in the 'Related SRS §' (second column of the table).

- 4.5.1.2 Note: Modes are not the only thing that can influence an onboard function. This is why this  Table  is  not  enough  in  itself  to  understand  all  the  ERTMS/ETCS  onboard behaviour.  It  must  be  understood  as  a  complement  to  all  other  SRS  chapters (especially §4.7, 4.8, 4.9 and 4.10).
- 4.5.1.3 Note: for DMI depending on modes, refer to §4.7.

## 4.5.2 Active Functions Table

## 4.5.2.1 X = functions shall be active

Empty case = function shall be inactive

O = Optional (function is not required for interoperability, but is not forbidden)

| ONBOARD-FUNCTIONS                                                                                                                                                                              | RELATED SRS §         | N P   | S B   | P S   | S H   | F S   | L S   | S R O S   | S L   |    | N L   | U N   | T R P T   | I S S N   | R V   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-------|-------|-------|-------|-------|-------|-----------|-------|----|-------|-------|-----------|-----------|-------|
| Data Consistency                                                                                                                                                                               |                       |       |       |       |       |       |       |           |       |    |       |       |           |           |       |
| Check linking consistency                                                                                                                                                                      | 3.16.2.3 3.4.4        |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Check Balise Group Message Consistency if linking consistency is checked                                                                                                                       | 3.16.2.4.1 3.16.2.4.3 |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Check Balise Group Message Consistency if no linking consistency is checked (because no linking information is available and/or because the function 'check linking consistency is not active) | 3.16.2.4.4            |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check Unlinked Balise Group Message Consistency                                                                                                                                                | 3.16.2.5              |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check correctness of radio messages                                                                                                                                                            | 3.16.3.1.1            |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check radio sequence                                                                                                                                                                           | 3.16.3.3              |       | X     | X     | X     | X     | X     | X X       | X     | X  | X     | X     | X         | X         | X     |
| Check safe radio connection (only level 2/3)                                                                                                                                                   | 3.16.3.4              |       |       |       |       | X     | X     | X         |       |    |       |       |           |           |       |
| Determine Train Speed and Position:                                                                                                                                                            |                       |       |       |       |       |       |       |           |       |    |       |       |           |           |       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| ONBOARD-FUNCTIONS                                                                                    | RELATED SRS §             | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R P T   | I S S N   | R V   |
|------------------------------------------------------------------------------------------------------|---------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-----------|-----------|-------|
| Determine train position referenced to LRBG                                                          | 3.6.1 3.6.4               |       | X     | X     | X     | X     | X     | X     | X X   | X     | X     | X     | X         | X         | X     |
| Determine train speed, train acceleration, train standstill                                          | None                      |       | X     | X     | X     | X     | X     | X     | X     | X X   | X     | X     | X         | O X       | X     |
| Determine Geographical Position                                                                      | 3.6.6                     |       | X     |       |       | X     | X     | X     | X     | X     | X     | X     | X         |           |       |
| Report train position when train reaches standstill                                                  | 3.6.5.1.4 a)              |       |       |       |       | X     | X     | X     | X     |       |       |       |           | O         | X     |
| Report train position when mode changes to… 1                                                        | 3.6.5.1.4 b)              |       | X     |       | X 2   | X     | X     | X     | X X   | X     | X     | X     | X         | O X       | X     |
| Report train position when train integrity confirmed by driver                                       | 3.6.5.1.4 c)              |       | X     |       |       | X     | X     | X     | X     |       |       |       | X         |           |       |
| Report train position when loss of train integrity is detected                                       | 3.6.5.1.4 d)              |       | X     |       |       | X     | X     | X     | X     |       |       | X     | X         |           | X     |
| Report train position when train front/rear passes an RBC/RBC border (only level 2/3)                | 3.6.5.1.4 e) 3.6.5.1.4 k) |       |       |       |       | X     | X     | X     | X     |       |       | X     |           |           |       |
| Report train position when train rear passes a level transition border (from level 2/3 to 0, NTC, 1) | 3.6.5.1.4 f)              |       |       |       |       | X     | X     | X     | X     |       | X     | X     |           | X         |       |
| Report train position when change of level due to trackside order                                    | 3.6.5.1.4 g)              |       |       |       |       | X     | X     | X     | X     | X     |       | X     |           |           |       |
| Report train position when change of level due to driver request                                     | 3.6.5.1.4 g)              |       | X     |       |       | X     | X     | X     | X     | X     |       |       |           |           |       |
| Report train position when establishing a session with RBC                                           | 3.6.5.1.4 h)              |       | X     |       | X     | X     | X     | X     | X X   | X     | X     | X     | X         | X         | X     |
| Report train position when a data consistency error is detected (only level 2/3)                     | 3.6.5.1.4 l)              |       | X     |       |       | X     | X     | X     | X X   | X     | X     | X     | X         | X         | X     |
| Report train position as requested byRBC…                                                            | 3.6.5.1.4                 |       | X     |       |       | X     | X     | X     | X     | X     | X     | X     | X         | X         | X     |
| …or Report train position at every passage of an LRBG compliant balise group                         | 3.6.5.1.4 j)              |       |       |       |       | X     | X     | X     | X     | X     | X     | X     | X         | X         | X     |
| Manage MA                                                                                            |                           |       |       |       |       |       |       |       |       |       |       |       |           |           |       |

1  For ETCS level 2 and 3 this may imply establishing a radio communication session if none is established.

2  Exception: the transition PS =&gt; SH shall not be reported

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| ONBOARD-FUNCTIONS                                                                                                                | RELATED SRS §     | N P   | S B P S   | S H   | F S   | L S   |    | S R O S   | S L   | N L U N   | T R   | P T   | S F   | I S S N   | R V   |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------|-------|-----------|-------|-------|-------|----|-----------|-------|-----------|-------|-------|-------|-----------|-------|
| Request MA Cyclically respect to approach of perturbation location (T_MAR) or MA timer elapsing (T_TIMEOUTRQST) (only level 2/3) | 3.8.2.3 a) and b) |       |           |       |       | X     | X  | X         |       |           |       |       |       |           |       |
| Request MA Cyclically when 'Start' is selected (only level 2/3)                                                                  | 4.4.11 5.4, 5.11  | X     |           |       |       |       |    | X         |       |           |       | X     |       |           |       |
| Request MA on reception of "track ahead free up to the level 2/3 transition location" (only level 0,1,NTC)                       | 3.8.2.7.1         | X     |           |       | X     | X     |    | X X       |       | X         | X     |       | X     |           | X     |
| Request MA on track description deletion (only level 2/3)                                                                        | 3.8.2.7.3         |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Determine EOA/LOA, SvL, Danger Point, etc…                                                                                       | 3.8.4 3.8.5       |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Handle Co-operative MA revocation (only level 2/3)                                                                               | 3.8.6             |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Manage Unconditional Emergency Stop                                                                                              | 3.10              | X     |           |       | X     | X     | X  | X         |       |           |       | X     |       |           |       |
| Manage Conditional Emergency Stop                                                                                                | 3.10              |       |           |       | X     | X     |    | X         |       |           |       | X     |       |           |       |
| Determine Most Restrictive Speed Profile, based on :                                                                             |                   |       |           |       |       |       |    |           |       |           |       |       |       |           |       |
| SSP                                                                                                                              | 3.11.3            |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| ASP                                                                                                                              | 3.11.4            |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| TSR                                                                                                                              | 3.11.5            |       |           |       | X     | X     | X  | X         |       | X         |       |       |       |           |       |
| Signalling related speed restriction when evaluated as a speed limit                                                             | 3.11.6            |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Mode related speed restriction                                                                                                   | 3.11.7            |       |           | X     |       | X     | X  | X         |       | X         |       |       |       |           | X     |
| Train related speed restriction                                                                                                  | 3.11.8            |       |           |       | X     | X     | X  | X         |       | X         |       |       |       |           | X     |
| STM max speed                                                                                                                    | 3.11.2.2 g)       |       |           |       | X     | X     | X  | X         |       | X         |       |       |       | X         |       |
| STM system speed                                                                                                                 | 3.11.2.2 h)       |       |           |       | X     | X     | X  | X         |       | X         |       |       |       |           |       |
| LX speed                                                                                                                         | 3.12.5.6          |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Speed restriction to ensure a given permitted braking distance                                                                   | 3.11.11           |       |           |       | X     | X     |    | X         |       |           |       |       |       |           |       |
| Override related speed restriction                                                                                               | 5.8.3.6           |       |           | X     |       |       | X  |           |       | X         |       |       |       |           |       |
| Supervise Train Speed                                                                                                            |                   |       |           |       |       |       |    |           |       |           |       |       |       |           |       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| ONBOARD-FUNCTIONS                                                                                                                                         | RELATED SRS §                          | N P S B   | P S   | S H   |    | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S S   | N R V   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------|-------|-------|----|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---------|---------|
| Speed and Distance Monitoring based on MRSP, MA, release speed, gradient, mode profile, non protected LX start location, and route unsuitability location | 3.13 5.9.3.5 5.7.3.4 3.12.2.8 3.12.5.4 |           |       |       | X  | X     |       |       | X     |       |       |       |       |       |       |         |         |
| Speed and Distance Monitoring based on MRSP                                                                                                               | 4.4.10.1                               |           |       |       |    |       |       |       |       |       | X     |       |       |       |       |         |         |
| Speed and Distance Monitoring based on MRSP, allowed distance to run in Staff Resp. mode                                                                  | 4.4.11                                 |           |       |       |    |       | X     |       |       |       |       |       |       |       |       |         |         |
| Ceiling Speed Monitoring only (no braking curve) based on MRSP                                                                                            | 4.4.8.1.1 a) 4.4.18.1.3 a)             |           |       | X     |    |       |       |       |       |       |       |       |       |       |       | X 3     | X       |
| Supervise Train Movements                                                                                                                                 |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |         |         |
| Backwards Distance Monitoring                                                                                                                             | 4.4                                    |           |       |       |    |       |       |       |       |       |       |       | X     |       |       |         | X       |
| Roll Away Protection                                                                                                                                      | 3.14.2                                 |           |       | X     | X  | X     | X     | X     |       |       | X     |       | X     |       |       |         | X       |
| Reverse Movement Protection                                                                                                                               | 3.14.3                                 |           |       |       | X  | X     | X     | X     |       |       |       |       | X     |       |       |         | X       |
| Standstill Supervision                                                                                                                                    | 3.14.4 4.4.7.1.5                       | X         |       |       |    |       |       |       |       |       |       |       |       |       |       |         |         |
| Supervise 'danger for shunting' information and list of expected balises for shunting                                                                     | 4.4.8.1.1 b) and c)                    |           |       | X     |    |       |       |       |       |       |       |       |       |       |       |         |         |
| Supervise 'Stop if in SR' information and list of expected balises for Staff Responsible                                                                  | 4.4.11.1.3 c) and d)                   |           |       |       |    |       | X     |       |       |       |       |       |       |       |       |         |         |
| Supervise signalling related speed restriction when evaluated as a trip order                                                                             | 3.11.6.4                               |           |       |       | X  | X     | X     | X     |       |       |       |       |       |       |       |         |         |
| Command Emergency Brake                                                                                                                                   | 4                                      | X         |       |       |    |       |       |       |       |       |       | X     |       |       | X     |         |         |
| Determine Mode and Level                                                                                                                                  |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |         |         |
| Determine ERTMS/ETCS Mode                                                                                                                                 | 3.12.4, 4.6                            | X X       | X     | X     | X  | X     | X     | X     | X     | X     | X     | X     | X     | X     | X     | X       | X       |
| Determine ERTMS/ETCS level                                                                                                                                | 5.10                                   | X         | X     | X     | X  | X     | X     | X X   |       | X     | X     | X     | X     |       | X     | X       | X       |
| Other functions                                                                                                                                           |                                        |           |       |       |    |       |       |       |       |       |       |       |       |       |       |         |         |
| System Version Management                                                                                                                                 | 3.17                                   | X         | X     | X     | X  | X     | X     | X     | X     | X     | X     | X     |       | X     |       | X       | X       |
| Manage Communication Session                                                                                                                              | 3.5                                    | X         | X     | X     | X  | X     |       | X X   | X     | X     | X     | X     | X     |       |       | X       | X       |
| Delete Revoked TSR                                                                                                                                        | 3.11.5.5                               | X         |       |       | X  | X     | X     |       | X     |       | X     | X     |       | X     |       |         |         |
| Override (Trip inhibition) 4                                                                                                                              | 5.8                                    |           |       | X     |    |       | X     |       |       |       | X     |       |       |       |       | X       |         |

3   In  case  the  ERTMS  on-board  equipment  is  interfaced  to  the  National  System  through  an  STM,  refer  to SUBSET-035 for details

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| ONBOARD-FUNCTIONS                                                                 | RELATED SRS §                           | N P S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   |    | N L   | U N   | T R   | P T   | S F   | I S   | S N R V   |
|-----------------------------------------------------------------------------------|-----------------------------------------|-----------|-------|-------|-------|-------|-------|-------|-------|----|-------|-------|-------|-------|-------|-------|-----------|
| Manage Track Conditions excluding Sound Horn, Non Stopping Areas, Tunnel Stopping | 3.12.1                                  |           |       |       | X     | X     |       | X     |       | X  |       | X     | X     |       |       |       |           |
| Manage Track Conditions Sound Horn, Non Stopping Areas, Tunnel Stopping Areas     | 3.12.1                                  |           |       |       | X     | X     |       | X     |       |    |       |       |       |       |       |       |           |
| Manage Track Condition Big Metal Masses                                           | 3.12.1                                  | X         | X     | X     | X     | X     | X     | X     | X     | X  | X     | X     | X     | O     |       | X     |           |
| Manage Route Suitability                                                          | 3.12.2                                  |           |       |       | X     | X     |       | X     |       |    |       |       |       |       |       |       |           |
| Manage Text Display to the driver                                                 | 3.12.3                                  | X         |       |       | X     | X     | X     | X     |       |    | X     | X     | X     |       |       |       | X         |
| Manage LSSMA display to the driver                                                | 4.4.19.1                                |           |       |       |       | X     |       |       |       |    |       |       |       |       |       |       |           |
| Manage RBC/RBC Handover (only level 2/3)                                          | 3.15.1, 5.15                            |           |       |       | X     | X     | X     | X     | X     | X  |       | X     |       |       |       |       |           |
| Manage Track Ahead Free Request (only level 2/3)                                  | 3.15.5                                  | X         |       |       |       | X     | X     | X     |       |    |       |       | X     |       |       |       |           |
| Provide Fixed Values, and Default/National Values                                 | 3.18.1 3.18.2                           | X         | X     | X     | X     | X     | X     | X     | X     | X  | X     | X     | X     |       |       | X     | X         |
| Manage change of Train Data from external sources                                 | 5.17                                    | X         |       |       | X     | X     | X     | X     |       |    | X     | X     | X     |       |       | X     |           |
| Provide Date and Time                                                             | 3.18.5                                  | X         | X     | X     | X     | X     | X     | X     | X     | X  | X     | X     | X     |       |       | X     | X         |
| Provide Juridical Data                                                            | 3.20                                    | X         | X     | X     | X     | X     | X     | X     | X     | X  | X     | X     | X     | O     | O     | X     | X         |
| Inhibition of revocable TSRs from balises(only level 2/3)                         | 3.11.5.12 3.11.5.13 3.11.5.14 3.11.5.15 |           |       |       | X     | X     |       | X     |       |    |       | X     | X     |       |       |       |           |
| Cold Movement Detection                                                           | 3.15.8                                  | O         |       |       |       |       |       |       |       |    |       |       |       |       |       |       |           |
| Continue Shunting on desk closure (Enabling transition to Passive Shunting mode)  | 5.12.4                                  |           |       | X     |       |       |       |       |       |    |       |       |       |       |       |       |           |
| Manage 'Stop Shunting on desk opening' information                                | 4.4.20.1.8 4.4.20.1.9                   |           | X     |       |       |       |       |       |       |    |       |       |       |       |       |       |           |
| Manage Virtual Balise Covers                                                      | 3.15.9                                  | X         | X     | X     | X     | X     | X X   | X     |       | X  | X     | X     | X     | O     | O     | X     | X         |
| Advance display of route related information                                      | 3.15.10                                 |           |       |       | X     |       |       | X     |       |    |       |       |       |       |       |       |           |

## Figure 1: Active Functions table

4  For UN and SN mode, conditions for re-activation of transition to Trip mode (see § 5.8.4.1a) &amp; b)) shall be supervised.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.6 Transitions between modes

## 4.6.1 Symbols

- 4.6.1.1 The indication ' 4&gt; ' means: The condition n°4 must be fulfilled to trigger the transition
- 4.6.1.2 From the mode located in the column
- 4.6.1.3 To the mode that is indicated by the arrow ' &gt; '.
- 4.6.1.4 Each transition from a given mode receives a priority order (indicated by ' -px', x is the priority order) to avoid a conflict between the different transitions when they occur at the same time (i.e. in the same clock cycle). P1 has a higher priority than P2.
- 4.6.1.5 Some transitions have received the same priority order. This has been decided when it is obvious that these transitions cannot occur at the same time, and so can never lead to a conflicting situation (for example, the RBC cannot give in the same time a MA for FS and a MA for OS to a given engine, this is why the transition 'from SR to FS' and the transition 'from SR to OS' have the same priority order).
- 4.6.1.6 "16, 17, 18" means "16 or 17 or 18".

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.6.2

## Transitions Table

| NP      | <29 -p2-       | <29 -p2-   | <29 -p2-             | <29 -p2-                             | <29 -p2-                             | <29 -p2-                       | <29 -p2-                             | <29 -p2-   | <29 -p2-     | <29 -p2-        | <29 -p2-   | <29 -p2-      | <29 -p2-   | <29 -p2-               | <29 -p2-   |
|---------|----------------|------------|----------------------|--------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|------------|--------------|-----------------|------------|---------------|------------|------------------------|------------|
| 4> -p2- | SB             | <22 -p4-   | <19, 27, 30 -p5- <28 | -p5-                                 | <28 -p5-                             | <28, -p5-                      | <28, -p5-                            | <2, 3 -p3- | <28, 47 -p3- | <28, -p6-       | <28, -p4   |               |            | <28 -p6-               | <28 -p4-   |
|         |                | PS         | <26 -p5-             |                                      |                                      |                                |                                      |            |              |                 |            |               |            |                        |            |
|         | 5, 6, 50> -p7- | 23> -p4    | SH                   | <5,6, 50,51 -p6-                     | <5,6, 50,51 -p6-                     | <5,6, 51 -p6-                  | <5,6 50,51 -p6-                      |            |              | <5,61 -p7-      | <68 -p4    | <5,6, 50 -p5- |            | <5,61 -p7              |            |
|         | 10> -p7-       |            |                      | FS                                   | <31,32 -p6-                          | <31,32 -p6-                    | <31,32 -p6-                          |            |              | <25 -p7-        |            | <31 -p5-      |            | <25 -p7-               |            |
|         | 70> -p7-       |            |                      | 70,72> -p6-                          | LS                                   | <72 -p6-                       | <70,74 -p6-                          |            |              | <71 -p7-        |            | <70 -p5-      |            | <71 -p7-               |            |
|         | 8,37> -p7-     |            |                      | 37> -p6-                             | 37> -p6-                             | SR                             | <37 -p6-                             |            |              | <44,45 -p4-     |            | <8,37 -p5-    |            | <44,45 -p4-            |            |
|         | 15> -p7-       |            |                      | 15,40> -p6-                          | 15,73> -p6-                          | 40> -p6-                       | OS                                   |            |              | <34 -p7-        |            | <15 -p5-      |            | <34 -p7-               |            |
|         | 14> -p5-       | 14> -p4    |                      |                                      |                                      |                                |                                      | SL         |              |                 |            |               |            |                        |            |
|         | 46> -p6-       |            | 46> -p5-             | 46> -p6-                             | 46> -p6-                             | 46> -p6-                       | 46> -p6-                             |            | NL           |                 |            |               |            |                        |            |
|         | 60> -p7-       |            |                      | 21> -p6-                             | 21> -p6-                             | 21> -p6-                       | 21> -p6-                             |            |              | UN              | <62 -p4-   |               |            | <21 -p7-               |            |
|         | 20> -p4-       |            | 49,52, 65> -p4-      | 12,16, 17,18, 20,41, 65,66, 69> -p4- | 12,16, 17,18, 20,41, 65,66, 69> -p4- | 18,20, 42, 43, 36, 54,65> -p4- | 12,16, 17,18, 20,41, 65,66, 69> -p4- |            |              | 67,39, 20> -p5- | TR         |               |            | <67, 39,38, 35,20 -p5- |            |
|         |                |            |                      |                                      |                                      |                                |                                      |            |              |                 | 7> -p4-    | PT            |            |                        |            |
|         | 13> -p3-       | 13> -p3-   | 13> -p3-             | 13> -p3-                             | 13> -p3-                             | 13> -p3-                       | 13> -p3-                             |            |              | 13> -p3-        | 13> -p3-   | 13> -p3-      | SF         | <13 -p3-               | <13 -p3-   |
| 1> -p1- | 1> -p1-        | 1> -p1-    | 1> -p1-              | 1> -p1-                              | 1> -p1-                              | 1> -p1-                        | 1> -p1-                              | 1> -p1-    | 1> -p1-      | 1> -p1-         | 1> -p1-    | 1> -p1-       | 1> -p1-    | <1 -p1-                | <1 -p1-    |
|         | 58> -p7-       |            |                      | 56> -p6-                             | 56> -p6-                             | 56> -p6-                       | 56> -p6-                             |            |              | 56> -p7-        | 63> -p4-   |               |            | SN                     |            |
|         |                |            |                      | 59> -p6-                             | 59> -p6-                             |                                | 59> -p6-                             |            |              |                 |            |               |            |                        | RV         |

Figure 2: Transition table.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.6.3 Transitions Conditions Table

| Condition Id   | Content of the conditions                                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [1]            | The driver isolates the ERTMS/ETCS on-board equipment.                                                                                                            |
| [2]            | (a desk is open)                                                                                                                                                  |
| [3]            | (no 'go sleeping' input signal is received any more) AND (train is at standstill)                                                                                 |
| [4]            | The ERTMS/ETCS on-board equipment is powered.                                                                                                                     |
| [5]            | (train is at standstill) AND (ERTMS/ETCS level is 0 or NTC or 1) AND (driver selects Shunting mode)                                                               |
| [6]            | (train is at standstill) AND (ERTMS/ETCS level is 2 or 3) AND (reception of the information 'Shunting granted by RBC', due to a Shunting request from the driver) |
| [7]            | (the driver acknowledges the train trip) AND (the train is at standstill) AND (the ERTMS/ETCS level is different from 0, NTC)                                     |
| [8]            | (Staff Responsible mode is proposed to the driver) AND (driver acknowledges) {4}                                                                                  |
| [9]            | Empty                                                                                                                                                             |
| [10]           | (valid Train Data is stored on board) AND (MA + SSP +gradient are on-board) AND (no specific mode is required by a Mode Profile)                                  |
| [11]           | Empty                                                                                                                                                             |
| [12]           | (The train/engine overpasses the EOA/LOA with its min safe antenna position) AND (ERTMS/ETCS level is 1)                                                          |
| [13]           | The ERTMS/ETCS on-board equipment detects a fault that affects safety                                                                                             |
| [14]           | (The 'sleeping' input signal is received) AND (train is at standstill) AND (all desks connected to the ERTMS/ETCS on-board equipment are closed)                  |
| [15]           | (An ackn. request for On Sight is displayed to the driver) AND (the driver acknowledges) see {1} here under                                                       |
| [16]           | (The train/engine overpasses the EOA/LOA with its min safe front end) AND (ERTMS/ETCS level is 2 or 3).                                                           |
| [17]           | The onboard reacts according to a linking reaction set to 'trip'.                                                                                                 |
| [18]           | (the train/engine receives and uses a trip order given by balise) AND (override is not active)                                                                    |
| [19]           | (driver selects 'exit Shunting') AND (train is at standstill).                                                                                                    |
| [20]           | (unconditional emergency stop message is accepted)                                                                                                                |
| [21]           | (ERTMS/ETCS level switches to 0) see {2} here under                                                                                                               |
| [22]           | (a desk is open) AND ('Stop Shunting on desk opening' information is stored onboard)                                                                              |
| [23]           | (a desk is open) AND (no 'Stop Shunting on desk opening' information is stored                                                                                    |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|      | onboard)                                                                                                                                                                                               |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [24] | Empty                                                                                                                                                                                                  |
| [25] | (ERTMS/ETCS level switches to 1,2 or 3) AND (MA+SSP+gradient are on-board) AND (no specific mode is required by a Mode Profile)                                                                        |
| [26] | (desks are closed) AND ('Continue Shunting on desk closure' function is active) AND (the 'passive shunting' input signal is received)                                                                  |
| [27] | (desks are closed) AND ('Continue Shunting on desk closure' function is not active)                                                                                                                    |
| [28] | (desks are closed)                                                                                                                                                                                     |
| [29] | the ERTMS/ETCS on-board equipment is NOT powered                                                                                                                                                       |
| [30] | (desks are closed) AND (no 'passive shunting' input signal is received)                                                                                                                                |
| [31] | (MA+SSP+gradient are on-board) AND (no specific mode is required by a Mode Profile) AND (ERTMS/ETCS level is 2 or 3)                                                                                   |
| [32] | (MA+SSP+gradient are on-board) AND (no specific mode is required by a Mode Profile) AND (ERTMS/ETCS level is 1) AND (no trip order is given by balise)                                                 |
| [33] | Empty                                                                                                                                                                                                  |
| [34] | (A Mode Profile defining an On Sight area is on-board) AND (The max safe front end of the train is inside the On Sight area) AND (The ERTMS/ETCS level switches to 1,2 or 3)                           |
| [35] | (driver selects Shunting mode) AND (The ERTMS/ETCS on-board equipment is interfaced to the National System through an STM) AND (a National Trip Procedure is active, see {8} here under )              |
| [36] | (the identity of the over-passed balise group is not in the list of expected balises related to SR mode) AND (override is not active).                                                                 |
| [37] | (driver selects 'override') AND (train speed is under or equal to the speed limit for triggering the 'override' function) see {3} here under                                                           |
| [38] | (The ERTMS/ETCS on-board equipment is interfaced to the National System through an STM) AND (The ERTMS/ETCS level switches to 0,1,2 or 3) AND (a National Trip Procedure is active) see {8} here under |
| [39] | (The ERTMS/ETCS level switches to 1,2 or 3) AND (no MA has been accepted)                                                                                                                              |
| [40] | (A Mode Profile defining an On Sight area is on-board) AND (The max safe front end of the train is inside the On Sight area)                                                                           |
| [41] | (T_NVCONTACT is passed) AND (associated reaction is 'train trip')                                                                                                                                      |
| [42] | (The train/engine overpasses the SR distance with its estimated front end) AND (override is not active)                                                                                                |
| [43] | (The train/engine overpasses the former EOA/LOA (when Override was activated) with the min safe antenna position) AND (override is not active), see {3} here under                                     |
| [44] | ('override' function is active) AND (ERTMS/ETCS level switches to 1) see {3} here under                                                                                                                |
| [45] | ('override' function is active) AND (no unconditional emergency stop message has                                                                                                                       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|      | been received) AND (ERTMS/ETCS level switches to 2 or 3) see {3} here under                                                                                                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [46] | (Driver selects NON LEADING) AND (train is at standstill) AND (The 'non leading' input signal is received)                                                                                                                                                                                 |
| [47] | (no 'non leading' input signal is received any more) AND (train is at standstill)                                                                                                                                                                                                          |
| [48] | Empty                                                                                                                                                                                                                                                                                      |
| [49] | (reception of information 'stop if in shunting') AND (override is not active)                                                                                                                                                                                                              |
| [50] | (An ackn. request for Shunting is displayed to the driver) AND (the driver acknowledges) see {5} here under                                                                                                                                                                                |
| [51] | (A Mode Profile defining the entry of a Shunting area is used on-board) AND (The max safe front end of the train is inside the Shunting area)                                                                                                                                              |
| [52] | (the identity of the over-passed balise group is not in the list of expected balise groups related to SH mode) AND (override is not active).                                                                                                                                               |
| [53] | Empty                                                                                                                                                                                                                                                                                      |
| [54] | (reception of information 'stop if in Staff Responsible') AND (no list of expected balise groups related to SR mode has been received or the list of expected balise groups related to SR mode does not include the identity of the over-passed balise group) AND (override is not active) |
| [56] | (the ERTMS/ETCS level switches to 'NTC')                                                                                                                                                                                                                                                   |
| [58] | (the ERTMS/ETCS level is 'NTC') AND (an acknowledgement request for SN mode is displayed to the driver) AND (the driver acknowledges)                                                                                                                                                      |
| [59] | (train is at standstill) AND (driver has acknowledged the reversing) see {6} here under                                                                                                                                                                                                    |
| [60] | (an acknowledgement request for UN mode is displayed to the driver) AND (the driver acknowledges)                                                                                                                                                                                          |
| [61] | (A Mode Profile defining a Shunting area is on-board) AND (The max safe front end of the train is inside the Shunting area) AND (The ERTMS/ETCS level switches to 1,2 or 3)                                                                                                                |
| [62] | (the driver acknowledges the train trip) AND (the train is at standstill) AND (the ERTMS/ETCS level is 0) AND (valid Train Data is on-board)                                                                                                                                               |
| [63] | (the driver acknowledges the train trip) AND (the train is at standstill) AND (the ERTMS/ETCS level is NTC) AND (valid Train Data is on-board)                                                                                                                                             |
| [65] | (The system version number X of a received balise telegram is greater than the highest version number X supported by the on-board equipment) AND (ERTMS/ETCS level is 1, 2 or 3)                                                                                                           |
| [66] | A balise group contained in the linking information is passed in the unexpected direction                                                                                                                                                                                                  |
| [67] | (The ERTMS/ETCS level switches to level 1) AND (a trip order has been received) AND (override is not active)                                                                                                                                                                               |
| [68] | (the driver acknowledges the train trip) AND (the train is at standstill) AND (the                                                                                                                                                                                                         |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|      | ERTMS/ETCS level is 0 or NTC) AND (no valid Train Data is on-board)                                                                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [69] | Estimated train front end is in rear of the start location of either SSP or gradient profile stored on-board                                                                                                                          |
| [70] | (An ackn. request for Limited Supervision is displayed to the driver) AND (the driver acknowledges) see {7} here under                                                                                                                |
| [71] | (A Mode Profile defining a Limited Supervision area is on-board) AND (The max safe front end of the train is inside the Limited Supervision area) AND (The ERTMS/ETCS level switches to 1,2 or 3)                                     |
| [72] | (A Mode Profile defining a Limited Supervision area is on-board) AND (The max safe front end of the train is inside the Limited Supervision area).                                                                                    |
| [73] | (A Mode Profile defining an On Sight area is on-board) AND (The max safe front end of the train is inside the On Sight area) AND (The estimated front end of the train is not inside an LS acknowledgement area)                      |
| [74] | (A Mode Profile defining a Limited Supervision area is on-board) AND (The max safe front end of the train is inside the Limited Supervision area) AND (The estimated front end of the train is not inside an OS acknowledgement area) |

- {1} The request to acknowledge On Sight is displayed to the driver only if certain conditions are fulfilled. These conditions are not specified here. See the 'On Sight' procedure' in 5.9.
- {2} This transition to the Unfitted mode is also a transition of level. For further information, See the 'Level Transition' procedure in 5.10 and the 'Start Of Mission' procedure in 5.4.
- {3} See the 'Override' procedure' of SRS-§5.
- {4}  The  Staff  Responsible  mode  is  proposed  to  the  driver  only  if  certain  conditions  are  fulfilled. These conditions are not specified here. See the 'Start Of Mission' procedure and the "Train Trip" procedure of SRS-§5.
- {5} The request to acknowledge Shunting is displayed to the driver only if certain conditions are fulfilled.  These conditions are not specified here. See the 'Entry in Shunting' procedure and the 'Start Of Mission' procedure of SRS-§5.
- {6} The request to acknowledge Reversing is displayed to the driver when certain conditions are fulfilled. These conditions are not specified here. See the 'reversing' procedure of SRS-§5.
- {7}  The  request  to  acknowledge  Limited  Supervision  is  displayed  to  the  driver  only  if  certain conditions  are  fulfilled.  These  conditions  are  not  specified  here.  See  the  'Limited  Supervision' procedure' of SRS-§5 (for transitions from FS/OS/UN to LS) and the "Start of mission" procedure (for transition from SB to LS).
- {8} Refer to Subset-035 for details.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.7 DMI depending on modes

## 4.7.1 Introduction

- 4.7.1.1 The  DMI  is  an  interface  that  allows  the  direct  exchange  of  information  between  the driver and the ERTMS/ETCS onboard equipment. The indirect exchange of information done via  the  train  interface  (e.g.  a  driver's  action  on  the  service  brake  used  for  the service brake feedback, opening/closing the desk) is not part of the DMI.
- 4.7.1.2 The device(s) used to select 'ERTMS/ETCS onboard equipment powered/unpowered' is (are) not part of the DMI.
- 4.7.1.3 The device(s) used to select/indicate 'ERTMS/ETCS onboard equipment isolated/not isolated' is (are) part of the DMI.
- 4.7.1.4 Intentionally deleted.
- 4.7.1.5 Information (input or output) only relevant for  National System and not originated by the ERTMS/ETCS on-board is not included in the following section.

## 4.7.2 DMI versus Mode Table

- 4.7.2.1.1 X = active: For a DMI output, this means that the output information shall be shown to the driver when the ERTMS/ETCS onboard equipment is in the mode indicated in the column. For a DMI input, this means that it shall be possible for the driver to enter this information when the ERTMS/ETCS onboard equipment is in the mode indicated in the column).
- 4.7.2.1.2 A = available: This means that the input/output shall become active ONLY if another condition(s) is (are) fulfilled. This condition(s) are not described here.
- 4.7.2.1.3 Grey cells: availability and meaning defined by national system.
- 4.7.2.1.4 NA = Not Applicable: This concerns the modes SF and IS in which the DMI inputs and outputs cannot be determined.

| Input information              | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S   | S N   | R V   |
|--------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Train Data (refer to 3.18.3.2) |       | A     |       |       | A     | A     | A     | A     |       |       | A     |       |       | NA    | NA    | A     |       |
| Selection of language          |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Driver id                      |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     |       |       | NA    | NA    | A     |       |
| Train running number           |       | A     |       |       | A     | A     | A     | A     |       | A     | A     |       |       | NA    | NA    | A     |       |
| ERTMS/ETCS level               |       | A     |       |       | A     | A     | A     | A     |       | A     | A     |       |       | NA    | NA    | A     |       |
| Track Adhesion factor          |       | A     |       |       | A     | A     | A     | A     |       |       | A     |       |       | NA    | NA    | A     |       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Input information                                   | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S   | S N   | R V   |
|-----------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| RBC contact information - RBC-id - RBC phone number |       | A     |       |       | A     | A     | A     | A     |       | A     |       |       | A     | NA    | NA    |       |       |
| Radio network-id                                    |       | A     |       |       | A     | A     | A     | A     |       | A     | A     |       | A     | NA    | NA    | A     |       |
| Train integrity confirmation                        |       | A     |       |       | A     | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Start                                               |       | A     |       |       |       |       | A     |       |       |       |       |       | A     | NA    | NA    |       |       |
| Override request                                    |       | A     |       | A     | A     | A     | A     | A     |       |       | A     |       | A     | NA    | NA    | A     |       |
| Shunting request                                    |       | A     |       |       | A     | A     | A     | A     |       |       | A     |       | A     | NA    | NA    | A     |       |
| 'Continue Shunting on desk closure' request         |       |       |       | A     |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| 'Exit of Shunting' request                          |       |       |       | X     |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Non Leading request                                 |       | A     |       | A     | A     | A     | A     | A     |       |       |       |       |       | NA    | NA    |       |       |
| Ackn of fixed text information                      |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    |       | A     |
| Ackn of plain text information                      |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    |       | A     |
| Ackn of level transition                            |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     |       | NA    | NA    | A     |       |
| Ackn of Limited Supervision mode                    |       | A     |       |       | A     | A     |       | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Ackn of On Sight mode                               |       | A     |       |       | A     | A     |       | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Ackn of Shunting mode                               |       | A     |       | A     | A     | A     |       | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Ackn of Staff Resp. mode                            |       | A     |       |       |       |       |       |       |       |       |       |       | A     | NA    | NA    |       |       |
| Ackn of Unfitted mode                               |       | A     |       |       |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Ackn of Reversing mode                              |       |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Ackn of SN mode                                     |       | A     |       |       |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Ackn of Train Trip Ackn for Roll Away Protection    |       |       |       | A     | A     | A     | A     | A     |       |       | A     | A     | A     | NA NA | NA NA |       | A     |
| Ackn for Reverse Movement Protection                |       |       |       |       | A     | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       | A     |
| Ackn for Standstill Supervision                     |       | A     |       |       |       |       |       |       |       |       |       |       |       |       | NA    |       |       |
| Ackn for Post Trip distance                         |       |       |       |       |       |       |       |       |       |       |       |       |       | NA    |       |       |       |
| exceeded Ackn of Train Data change                  |       |       |       |       | A     | A     | A     |       |       |       | A     | A     | A     | NA NA | NA NA | A     |       |
| from source different from the driver               |       |       |       |       |       |       |       | A     |       |       |       |       |       |       | NA    |       | A     |
| Ackn for reversing distance exceeded                |       |       |       |       |       |       |       |       |       |       |       |       |       | NA    |       |       |       |
| Track Ahead Free                                    |       | A     |       |       |       | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       |       |
| SR mode speed limit and distance                    |       |       |       |       |       |       | A     |       |       |       |       |       |       | NA    | NA    |       |       |
| Virtual Balise Cover                                |       | A     |       |       |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Input information   | N   | S   | P   | S   | F   | L   | S   | O   | S   | N   | U   | T   | P   | S   | I   | S   | R   |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|                     | P   | B   | S   | H   | S   | S   | R   | S   | L   | L   | N   | R   | T   | F   | S   | N   | V   |
| Isolation           | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   | X   |

| Output information                                  | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S   | S N   | R V   |
|-----------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| ERTMS/ETCS Mode                                     |       | A     |       | X     | X     | X     | X     | X     |       | X     | X     | A     | X     | A     | X     | X     | X     |
| Current ERTMS/ETCS level                            |       | A     |       | X     | X     | X     | X     | X     |       | X     | X     | A     | X     | NA    | NA    | X     | X     |
| Train Speed                                         |       | A     |       | X     | X     | X     | X     | X     |       | X     | X     | A     | X     | NA    | NA    | A     | X     |
| Permitted Speed                                     |       |       |       | A     | X     |       | A     | A     |       |       |       |       |       | NA    | NA    |       | X     |
| SBI Speed                                           |       |       |       |       | A     |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Target Speed                                        |       |       |       |       | A     |       | A     | A     |       |       |       |       |       | NA    | NA    |       |       |
| Target distance                                     |       |       |       |       | A     |       | A     | A     |       |       |       |       |       | NA    | NA    |       | X     |
| Release speed                                       |       |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Speed and distance monitoring supervision status    |       |       |       | A     | A     | A     | A     | A     |       |       | A     |       | A     | NA    | NA    |       | A     |
| Time to Indication                                  |       |       |       |       | A     |       | A     | A     |       |       |       |       |       | NA    | NA    |       |       |
| LSSMA                                               |       |       |       |       |       | A     |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Trip reason                                         |       |       |       |       |       |       |       |       |       |       |       | A     | X     | NA    | NA    |       |       |
| Train Data (refer to 3.18.3.2)                      |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     | A     |
| Driver id                                           |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Train running number                                |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| RBC contact information - RBC-id - RBC phone number |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Radio network-id                                    |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Virtual Balise Covers                               |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Brake indication                                    |       | A     |       | A     | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     | A     |
| Fixed text information                              |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    |       | A     |
| Plain text information                              |       | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    |       | A     |
| Reversing allowed                                   |       |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Output information                                                                                                                                                                                                   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S   | S N   | R V   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Track condition excluding sound horn, non stopping areas, tunnel stopping areas and big metal masses - Power control - Pantograph control - Air tightness control - Radio hole, supervision of safe radio connection |       |       |       | A     | A     |       | A     |       | A     |       | A     | A     | NA    | NA    |       |       |
| Track conditions sound horn, non stopping areas, tunnel stopping areas                                                                                                                                               |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Geographical position                                                                                                                                                                                                | A     |       |       | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    |       |       |
| Override status                                                                                                                                                                                                      |       |       | A     |       |       | A     |       |       |       | A     |       |       | NA    | NA    | A     |       |
| LX status "not protected"                                                                                                                                                                                            |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Shunting refused by RBC                                                                                                                                                                                              | A     |       |       | A     | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Shunting request not answered by RBC                                                                                                                                                                                 | A     |       |       | A     | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Entry in FS                                                                                                                                                                                                          |       |       |       | A     |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Entry in OS                                                                                                                                                                                                          |       |       |       |       |       |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Level transition announcement                                                                                                                                                                                        |       |       |       | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     |       |
| Track Ahead Free request                                                                                                                                                                                             | A     |       |       |       | A     | A     | A     |       |       |       |       | A     | NA    | NA    |       |       |
| Adhesion factor 'slippery rail'                                                                                                                                                                                      | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     | A     |
| Trackside malfunction                                                                                                                                                                                                | A     |       | A     | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     | A     |
| Notification of Train Data change from source different from the driver                                                                                                                                              | A     |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     |       |
| Operated System Version                                                                                                                                                                                              | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Radio Network registration failed                                                                                                                                                                                    | A     |       |       | A     | A     | A     | A     |       | A     |       |       | A     | NA    | NA    |       |       |
| Safe radio connection indication                                                                                                                                                                                     | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Local time                                                                                                                                                                                                           | A     |       | X     | X     | X     | X     | X     |       | X     | X     | A     | X     | NA    | NA    | A     | X     |
| Gradient                                                                                                                                                                                                             |       |       |       | X     |       |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| MRSP                                                                                                                                                                                                                 |       |       |       | X     |       |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| First Indication location                                                                                                                                                                                            |       |       |       | A     |       |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| EOA/LOA                                                                                                                                                                                                              |       |       |       | A     |       |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Brake reason                                                                                                                                                                                                         | A     |       | A     | A     | A     | A     | A     |       |       | A     |       | A     | NA    | NA    | A     | A     |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Output information       | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | I S   | S N   | R V   |
|--------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Trackside not compatible |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| Train is rejected        |       | A     |       |       |       |       |       |       |       |       |       |       |       | NA    | NA    |       |       |
| Route unsuitability(ies) |       |       |       |       | A     | A     |       | A     |       |       |       |       |       | NA    | NA    |       |       |
| Set Speed indication     |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     | A     |
| NTC not available [1]    |       |       |       |       |       |       |       |       |       | A     |       |       |       | NA    | NA    | A     |       |
| NTC data need [1]        |       |       |       |       | A     | A     | A     | A     |       |       | A     | A     | A     | NA    | NA    | A     |       |
| NTC failed [1]           |       | A     |       | A     | A     | A     | A     | A     |       | A     | A     | A     | A     | NA    | NA    | A     |       |

- [1] In case the ERTMS/ETCS on-board equipment is interfaced to the National System through an STM, refer to SUBSET-035 for details.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.8 Acceptance of received information

## 4.8.1 Introduction

- 4.8.1.1 The  aim  of  this  chapter  is  to  give  an  overview  of  which  information  is  accepted  or rejected depending on the state of the on-board (level, mode) and the nature of the received information (transmission medium, type of information: infill or non-infill).
- 4.8.1.2 The following sections have to be interpreted by applying the filters as shown in Figure 3.  The  first  filter  is  detailed  in  section  4.8.3  'Accepted  information  depending  on  the level  and  transmission  media',  the  third  filter  in  section  4.8.4  'Accepted  information depending on the modes'.
- 4.8.1.3 If  a  message  contains  level  transition  information,  any  other  information  in  that message shall be evaluated considering the level transition information.
- 4.8.1.3.1 Information received in the same message as an immediate level transition order or a conditional level transition order that causes a level transition shall be evaluated first considering  the  on-board  currently  operated  level,  as  if  a  level  transition  order  for further location had been received (i.e. conditions [1], [2] or [6] of Figure 3, if applied, shall be automatically fulfilled). Then, if relevant, it shall be immediately extracted from the buffer and re-evaluated according to the new selected level.
- 4.8.1.4 Note:  As  shown  in  Figure  3,  information  stored  following  an  announcement  of  a change  of  level,  is  re-checked  for  acceptance  when  the  level  has  changed.  This implies  that,  when  the  level  changes,  the  mode  is  -  for  a  short  moment  -  still unchanged, until the stored information has been processed. The consequence for the Third Filter is that information needs to be accepted for this short period also in modes in which this information is otherwise useless.
- 4.8.1.5 If  a  message  contains  infill  information,  this  latter  shall  be  evaluated  considering  all other non-infill information in that message.
- 4.8.1.6 When evaluating trackside information received by radio or when re-evaluating a set of information  released  from  the  transition  buffer,  linking  information,  if  any,  shall  be evaluated prior to any other location related information.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

<!-- image -->

INFORMATION

Figure 3: schematic representation of the filtering of received information:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.8.2 Assumptions

- 4.8.2.1 The following tables shall be applied assuming that:
- a) the information complies with the system version checks (see section 3.17.3) and with the data consistency checks.(see section 3.16)
- b) the direction for which the information is valid matches the current train orientation, or  the  balise  group  crossing  direction  (for  SL,  PS  and  SH  engines).(see  section 3.6.3)
- c)  In  levels  2/3,  it  is  assumed  that  the  'RBC'  information  which  is  marked  'A' (Accepted)  comes  from  the  supervising  RBC  (see  RBC/RBC  handover).  If  this information is received from the 'Accepting' RBC while the 'Handing Over' RBC is still responsible, it is stored onboard  until the RBC  transition  is  performed Exception 1: The information 'Acknowledgement  of Train Data', 'Trackside constituent  system  version',  "Session  Management"  and  'Acknowledgement  of Session Termination" shall be immediately accepted. Exception  2:  The  information  'Co-operative  shortening  of  MA',  'Revocation  of Emergency Stop' and 'LSSMA display toggle on/off order' shall be rejected.
- d) to  check  exception  [4]  in  4.8.3,  the  track  description  is  referred  to  the  LRBG  (i.e. relocation has been performed see 3.6.4.3).
- e) the  information  from  balise  is  received  while  no  reverse  movement  is  performed (see clause 3.14.3.6)
- 4.8.2.2 Regarding  4.8.2.1  a):  In  case  a  balise  is  missed  or  a  balise  telegram  cannot  be decoded, the information 'Inhibition of balise group message consistency reaction' is only  used  by  the  on-board  equipment  to  inhibit  the  service  brake reaction,  while the balise group message is rejected. If all the telegrams from a balise group are correctly read,  the  information  'Inhibition  of  balise  group  message  consistency  reaction',  if received, shall be ignored by the on-board equipment. Therefore this information need not to be referred to in the following tables.
- 4.8.2.3 In case a balise telegram contains the information VBC marker and a country/region identity that both match a stored VBC, the whole balise telegram is ignored and any further  check  in  relation  to  this  balise  telegram  is  irrelevant  (refer  to  3.15.9.3  b)). Otherwise  the  information  VBC  marker,  if  included  in  a  consistent  balise  group message, shall always be ignored by the ERTMS/ETCS on-board equipment and need not to be referred to in the following tables.
- 4.8.2.4 Note: with the exception of the data that is forwarded to a National System through the STM interface (see 3.15.6 and SUBSET-035), what will happen to the data to be used by  applications  outside  ERTMS/ETCS  (e.g.  whether  it  is  discarded,  forwarded  to  an external  application,  processed  by a national function…) is outside the scope of this specification  and  is  assumed  as  not  being  part  of  the  ERTMS/ETCS  on-board functionality.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.8.3 Accepted information depending on the level and transmission media

## 4.8.3.1 From RBC or not

4.8.3.1.1 Note: 'No' in column 'From RBC' has to be understood as any information (type: infill or  non-infill)  received  from  a  balise  group,  loop  or  RIU;  this  does  not  include information received from the STM interface.

A = Accepted R = Rejected

|                                                                                       | From RBC   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|---------------------------------------------------------------------------------------|------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information                                                                           |            | 0                         | NTC                       | 1                         | 2                         | 3                         |
| National Values                                                                       | No         | A                         | A                         | A                         | A                         | A                         |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A                         | A                         |
| Linking                                                                               | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Signalling Related Speed Restriction                                                  | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                       | Yes        |                           |                           |                           |                           |                           |
| Movement Authority + (optional) Mode Profile + (optional) List of Balises for SH area | No         | R [1]                     | R [1]                     | A [4]                     | R [1]                     | R [1]                     |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3] [4] [5]             | A [3] [4] [5]             |
| Repositioning Information                                                             | No         | R                         | R                         | A                         | R                         | R                         |
|                                                                                       | Yes        |                           |                           |                           |                           |                           |
| Gradient Profile                                                                      | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| International SSP                                                                     | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Axle Load speed profile                                                               | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                       | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Level Transition Order                                                                | No         | A                         | A                         | A                         | A                         | A                         |
|                                                                                       | Yes        | A                         | A                         | A                         | A                         | A                         |
| Conditional Level Transition Order                                                    | No         | A [11]                    | A [11]                    | A [11]                    | A [11]                    | A [11]                    |
|                                                                                       | Yes        |                           |                           |                           |                           |                           |
| Session Management                                                                    | No         | A                         | A                         | A                         | A [14]                    | A [14]                    |
| Session Management                                                                    | Yes        | A                         | A                         | A                         | A                         | A                         |
| Radio Network registration                                                            | No         | A                         | A                         | A                         | A                         | A                         |
| Radio Network registration                                                            | Yes        | A                         | A                         | A                         | A                         | A                         |
| MA Request Parameters                                                                 | No         |                           |                           |                           |                           |                           |
|                                                                                       | Yes        | A                         | A                         | A                         | A                         | A                         |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|                                                          | From RBC   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|----------------------------------------------------------|------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information                                              |            | 0                         | NTC                       | 1                         | 2                         | 3                         |
| Position Report parameters                               | No         |                           |                           |                           |                           |                           |
| Position Report parameters                               | Yes        | A                         | A                         | A                         | A                         | A                         |
| SR Authorisation + (optional) List of Balises in SR mode | No         |                           |                           |                           |                           |                           |
| SR Authorisation + (optional) List of Balises in SR mode | Yes        | R                         | R                         | R                         | A [3]                     | A [3]                     |
| Stop if in SR mode                                       | No         | R                         | R                         | A                         | A                         | A                         |
| Stop if in SR mode                                       | Yes        |                           |                           |                           |                           |                           |
| SR distance information from loop                        | No         | R                         | R                         | A                         | R                         | R                         |
| SR distance information from loop                        | Yes        |                           |                           |                           |                           |                           |
| Temporary Speed Restriction                              | No         | A                         | R [1] [2]                 | A                         | A [8]                     | A [8]                     |
| Temporary Speed Restriction                              | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Temporary Speed Restriction Revocation                   | No         | A                         | R [1] [2]                 | A                         | A                         | A                         |
| Temporary Speed Restriction Revocation                   | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Inhibition of revocable TSRs from balises in L2/3        | No         |                           |                           |                           |                           |                           |
| Inhibition of revocable TSRs from balises in L2/3        | Yes        | R [2]                     | R [2]                     | R [2]                     | A                         | A                         |
| Default Gradient for TSR                                 | No         | A                         | R [1] [2]                 | A                         | A                         | A                         |
| Default Gradient for TSR                                 | Yes        |                           |                           |                           |                           |                           |
| Route Suitability Data                                   | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
| Route Suitability Data                                   | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Adhesion Factor                                          | No         | R[1]                      | R[1]                      | A                         | R                         | R                         |
| Adhesion Factor                                          | Yes        | R[2]                      | R[2]                      | R[2]                      | A                         | A                         |
| Plain Text Information                                   | No         | A                         | R [1] [2]                 | A                         | A                         | A                         |
| Plain Text Information                                   | Yes        | R [2]                     | R [2]                     | R [2]                     | A [12]                    | A [12]                    |
| Fixed Text Information                                   | No         | A                         | R [1] [2]                 | A                         | A                         | A                         |
| Fixed Text Information                                   | Yes        | R [2]                     | R [2]                     | R [2]                     | A [12]                    | A [12]                    |
| Geographical Position                                    | No         | A                         | R [1] [2]                 | A                         | A                         | A                         |
| Geographical Position                                    | Yes        | R [2]                     | R [2]                     | R [2]                     | A                         | A                         |
| RBC Transition Order                                     | No         | R                         | R                         | R                         | A                         | A                         |
| RBC Transition Order                                     | Yes        | R                         | R                         | R                         | A [3]                     | A [3]                     |
| Danger for SH information                                | No         | A [13]                    | A [13]                    | A                         | A                         | A                         |
| Danger for SH information                                | Yes        |                           |                           |                           |                           |                           |
| Stop Shunting on desk opening                            | No         | A                         | A                         | A                         | A                         | A                         |
| Stop Shunting on desk opening                            | Yes        |                           |                           |                           |                           |                           |
| Radio Infill Area information                            | No         | R                         | R                         | A                         | R [1]                     | R [1]                     |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|                                                                                                  | From RBC   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|--------------------------------------------------------------------------------------------------|------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information                                                                                      |            | 0                         | NTC                       | 1                         | 2                         | 3                         |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| Session Management with neighbouring RIU                                                         | No         | R                         | R                         | A                         | R                         | R                         |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| EOLM information                                                                                 | No         | A                         | A                         | A                         | A                         | A                         |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| Assignment of Co-ordinate system                                                                 | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | A [10]                    | A [10]                    | A [10]                    | A [10]                    | A [10]                    |
| Infill Location Reference                                                                        | No         | R                         | R                         | A                         | R [1]                     | R [1]                     |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| Track Conditions excluding big metal masses                                                      | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                                                                  | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Track condition big metal masses                                                                 | No         | A                         | A                         | A                         | A                         | A                         |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| Location Identity (NID_C + NID_BG transmitted in the balise telegram)                            | No         | A                         | A                         | A                         | A                         | A                         |
|                                                                                                  | Yes        |                           |                           |                           |                           |                           |
| Recognition of exit from TRIP mode                                                               | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R                         | R                         | R                         | A                         | A                         |
| Acknowledgement of Train Data                                                                    | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | A                         | A                         | A                         | A                         | A                         |
| Co-operative shortening of MA + (optional) Mode Profile + (optional) List of Balises for SH area | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R                         | R                         | R                         | A [3] [4] [5]             | A [3] [4] [5]             |
| Unconditional Emergency Stop                                                                     | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R [2]                     | R [2]                     | R [2]                     | A                         | A                         |
| Conditional Emergency Stop                                                                       | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R [2]                     | R [2]                     | R [2]                     | A                         | A                         |
| Revocation of Emergency Stop (Conditional or Unconditional)                                      | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R                         | R                         | R                         | A                         | A                         |
| SH refused                                                                                       | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R                         | R                         | R                         | A [3]                     | A [3]                     |
| SH authorised + (optional) List of Balises for SH area                                           | No         |                           |                           |                           |                           |                           |
|                                                                                                  | Yes        | R                         | R                         | R                         | A [3]                     | A [3]                     |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|                                                      | From RBC   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|------------------------------------------------------|------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information                                          |            | 0                         | NTC                       | 1                         | 2                         | 3                         |
| Trackside constituent System Version                 | No         | A                         | A                         | A                         | A                         | A                         |
|                                                      | Yes        | A                         | A                         | A                         | A                         | A                         |
| System Version order                                 | No         | A                         | A                         | A                         | A                         | A                         |
|                                                      | Yes        |                           |                           |                           |                           |                           |
| Track Ahead Free Request                             | No         |                           |                           |                           |                           |                           |
| Track Ahead Free Request                             | Yes        | R                         | R                         | R                         | A [3]                     | A [3]                     |
| Train Running Number                                 | No         |                           |                           |                           |                           |                           |
| Train Running Number                                 | Yes        | R                         | R                         | R                         | A                         | A                         |
| Acknowledgement of session termination               | No         | A                         | A                         | A                         | A                         | A                         |
|                                                      | Yes        | A                         | A                         | A                         | A                         | A                         |
| Train Rejected                                       | No         |                           |                           |                           |                           |                           |
|                                                      | Yes        | R                         | R                         | R                         | A                         | A                         |
| Train Accepted                                       | No         |                           |                           |                           |                           |                           |
|                                                      | Yes        | R                         | R                         | R                         | A                         | A                         |
| SoM Position Report Confirmed by RBC                 | No         |                           |                           |                           |                           |                           |
|                                                      | Yes        | R                         | R                         | R                         | A                         | A                         |
| Reversing Area Information                           | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                      | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Reversing Supervision Information                    | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                      | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Default Balise/Loop/RIU Information                  | No         | A                         | A                         | A                         | A                         | A                         |
|                                                      | Yes        |                           |                           |                           |                           |                           |
| Track Ahead Free up to level 2/3 transition location | No         | A [9]                     | A [9]                     | A [9]                     | R                         | R                         |
| Track Ahead Free up to level 2/3 transition location | Yes        |                           |                           |                           |                           |                           |
| Permitted Braking Distance Information               | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
| Permitted Braking Distance Information               | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Level Crossing information                           | No         | R [1] [2]                 | R [1] [2]                 | A                         | A                         | A                         |
| Level Crossing information                           | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3]                     | A [3]                     |
| Virtual Balise Cover order                           | No         | A                         | A                         | A                         | A                         | A                         |
| Virtual Balise Cover order                           | Yes        |                           |                           |                           |                           |                           |
| Generic LS function marker                           | No         | A                         | A                         | A                         | A                         | A                         |
|                                                      | Yes        |                           |                           |                           |                           |                           |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|                                                    | From RBC   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|----------------------------------------------------|------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information                                        |            | 0                         | NTC                       | 1                         | 2                         | 3                         |
| LSSMA display toggle on order                      | No         | R [1]                     | R [1]                     | A                         | R [1]                     | R [1]                     |
|                                                    | Yes        | R [2]                     | R [2]                     | R [2]                     | A [3] [5]                 | A [3] [5]                 |
| LSSMA display toggle off order                     | No         | R                         | R                         | A                         | R                         | R                         |
|                                                    | Yes        | R                         | R                         | R                         | A                         | A                         |
| Data to be used by applications outside ERTMS/ETCS | No         | A                         | A                         | A                         | A                         | A                         |
|                                                    | Yes        | A                         | A                         | A                         | A                         | A                         |

- [1] exception: stored onboard if an order to switch to L1 at a further location has been received.
- [2] exception: stored onboard if an order to switch to L2/3 at a further location has been received.
- [3] exception: rejected if Train Data has been sent to the RBC and the 'Acknowledgement of Train Data' has not been received yet.
- [4] exception: rejected if the SSP and gradient already available on-board or given together with the MA do not cover the full length of the MA.
- [5] exception: rejected if emergency stop(s) have been accepted and are not yet revoked or deleted onboard (see mode transitions).
- [8] exception: revocable TSRs shall be rejected if information 'inhibition of revocable TSRs from balises in L2/3' is stored on-board.
- [9] exception: rejected if no level 2/3 transition order is stored onboard.
- [10] exception: rejected if the referred LRBG is memorised to have been reported with different 'previous LRBG'
- [11] exception: rejected if a level transition order is received in the same message, or if a previous level transition order has announced a level transition still to be executed
- [12] exception: rejected if the text message is sent with a request for report of driver acknowledgement with the same text message identifier as a previously received text message, which the driver has not yet acknowledged
- [13] exception: rejected if not received together with an immediate level transition order to L1/2/3
- [14] exception: rejected if it relates to an order to establish a communication session with an RBC referred to in an RBC transition order currently stored or received in the same message

## 4.8.3.2 From National System X (through STM interface)

|                                                          | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   | Onboard operating level   |
|----------------------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Information from National System X through STM interface | 0                         | NTC X                     | NTC Y                     | 1                         | 2                         | 3                         |
| STM max speed                                            | A [7]                     | R                         | R [6]                     | A [7]                     | A [7]                     | A [7]                     |
| STM system speed/distance                                | A [7]                     | R                         | R                         | A [7]                     | A [7]                     | A [7]                     |

- [6]  exception: stored by ETCS onboard if an order to switch to level NTC X at a further location has been received.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

[7] exception: rejected by ETCS onboard if no order to switch to level NTC X at a further location has been received.

- 4.8.3.3 Intentionally deleted.

- 4.8.3.4 Intentionally deleted.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.8.4 Accepted Information depending on the modes

4.8.4.1 Assumptions

4.8.4.1.1

For infill information, only the columns FS and LS shall apply. In all other modes, infill information shall be rejected.

4.8.4.1.2 Intentionally deleted.

4.8.4.2 Intentionally deleted.

NR = Not Relevant A = Accepted R = Rejected

| Information                                                                           | Modes   | Modes    | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes     | Modes   | Modes   | Modes   | Modes   |
|---------------------------------------------------------------------------------------|---------|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-----------|---------|---------|---------|---------|
|                                                                                       | N P     | SB       | P S     | S H     | F S     | L S     | SR      | OS      | SL      | N L     | U N     | TR      | PT        | SF      | IS      | SN      | RV      |
| National Values                                                                       | NR      | A [2]    | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A [1]     | NR      | NR      | A       | A       |
| Linking                                                                               | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | A       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| Signalling Related Speed Restriction                                                  | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| Movement Authority + (optional) Mode Profile + (optional) List of Balises for SH area | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| Repositioning Information                                                             | NR      | R        | R       | R       | A       | A       | R       | A       | R       | R       | R       | R       | R         | NR      | NR      | R       | R       |
| Gradient Profile                                                                      | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| International SSP                                                                     | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| Axle load speed profile                                                               | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| STM max speed                                                                         | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]     | NR      | NR      | A       | R       |
| STM system speed/distance                                                             | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]     | NR      | NR      | R       | R       |
| Level Transition Order and Conditional Level Transition Order                         | NR      | A [2]    | A [7]   | A [7]   | A       | A       | A       | A       | A       | A       | A       | A       | A [1] [5] | NR      | NR      | A       | R       |
| Session Management                                                                    | NR      | A        | A [3]   | A [3]   | A       | A       | A       | A       | A       | A       | A       | A       | A [1]     | NR      | NR      | A       | A       |
| Radio Network registration                                                            | NR      | A [2]    | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A [1]     | NR      | NR      | A       | A       |
| MA Request Parameters                                                                 | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]     | NR      | NR      | A       | R       |
| Position Report parameters                                                            | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | A       | A       | R       | A [1]     | NR      | NR      | A       | A       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Information                                                                      | Modes   | Modes    | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   |
|----------------------------------------------------------------------------------|---------|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|                                                                                  | N P     | SB       | P S     | S H     | F S     | L S     | SR      | OS      | SL      | N L     | U N     | TR      | PT      | SF      | IS      | SN      | RV      |
| SR Authorisation+ (optional) List of Balises in SR mode                          | NR      | A[2][ 4] | R       | R       | R       | R       | A       | R       | R       | R       | R       | R       | A [1]   | NR      | NR      | R       | R       |
| Stop if in SR mode                                                               | NR      | R        | R       | R       | R       | R       | A       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| SR distance information from loop                                                | NR      | R        | R       | R       | R       | R       | A [6]   | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Temporary Speed Restriction                                                      | NR      | A [2][4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| Temporary Speed Restriction Revocation                                           | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| Inhibition of revocable TSRs from balises in L2/3                                | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| Default Gradient for TSR                                                         | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| Route Suitability Data                                                           | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Adhesion Factor                                                                  | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Plain Text Information                                                           | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | A       |
| Fixed Text Information                                                           | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A [1]   | NR      | NR      | A       | A       |
| Geographical Position                                                            | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | A       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| RBC Transition Order                                                             | NR      | A[2][ 4] | A [8]   | A [8]   | A       | A       | A       | A       | A       | A       | R       | A       | A [1]   | NR      | NR      | R       | R       |
| Danger for SH information                                                        | NR      | R        | R       | A       | R       | R       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Stop Shunting on desk opening                                                    | NR      | R        | A       | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Radio Infill Area information                                                    | NR      | R        | R       | R       | A       | A       | A       | A       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Session Management with neighbouring RIU                                         | NR      | R        | R       | R       | A       | A       | A       | A       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| EOLM information                                                                 | NR      | R        | R       | A       | A       | A       | A       | A       | A       | A       | A       | A       | R       | NR      | NR      | A       | A       |
| Assignment of Co-ordinate system                                                 | NR      | A [2]    | R       | R       | R       | R       | A       | R       | R       | A       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Infill Location Reference                                                        | NR      | R        | R       | R       | A       | A       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Track Conditions excluding sound horn, non stopping areas, tunnel stopping areas | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | A       | A       | A       | A [1]   | NR      | NR      | A       | R       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Information                                                                                      | Modes   | Modes    | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   |
|--------------------------------------------------------------------------------------------------|---------|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|                                                                                                  | N P     | SB       | P S     | S H     | F S     | L S     | SR      | OS      | SL      | N L     | U N     | TR      | PT      | SF      | IS      | SN      | RV      |
| Track conditions sound horn, non stopping areas, tunnel stopping areas                           | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Track condition big metal masses                                                                 | NR      | A[2][ 4] | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A [1]   | NR      | NR      | A       | R       |
| Location Identity (NID_C + NID_BG)                                                               | NR      | A [2]    | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| Recognition of exit from TRIP mode                                                               | NR      | R        | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | A       | NR      | NR      | R       | R       |
| Acknowledgement of Train Data                                                                    | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A       | NR      | NR      | A       | A       |
| Co-operative shortening of MA + (optional) Mode Profile + (optional) List of Balises for SH area | NR      | R        | R       | R       | A       | A       | R       | A       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Unconditional Emergency Stop                                                                     | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | R       | NR      | NR      | A       | R       |
| Conditional Emergency Stop                                                                       | NR      | R        | R       | R       | A       | A       | R       | A       | R       | R       | A       | R       | R       | NR      | NR      | A       | R       |
| Revocation of Emergency Stop (Conditional or Unconditional)                                      | NR      | R        | R       | R       | A       | A       | R       | A       | R       | R       | R       | R       | A [1]   | NR      | NR      | R       | R       |
| SH refused                                                                                       | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | R       | R       | A [1]   | NR      | NR      | R       | R       |
| SH authorised + (optional) List of Balises for SH area                                           | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | R       | R       | A [1]   | NR      | NR      | R       | R       |
| Trackside constituent System Version                                                             | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| System Version order                                                                             | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| Track Ahead Free Request                                                                         | NR      | A [2]    | R       | R       | R       | A       | A       | A       | R       | R       | R       | R       | A[1]    | NR      | NR      | R       | R       |
| Train Running Number                                                                             | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | A       | R       | A       | A       | NR      | NR      | R       | A       |
| Acknowledgement of session termination                                                           | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| Train Rejected                                                                                   | NR      | A [2]    | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Train Accepted                                                                                   | NR      | A [2]    | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| SoM Position Report Confirmed by RBC                                                             | NR      | A [2]    | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Reversing Area Information                                                                       | NR      | A[2][    | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | A       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Information                                          | Modes   | Modes    | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   | Modes   |
|------------------------------------------------------|---------|----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|                                                      | N P     | SB       | P S     | S H     | F S     | L S     | SR      | OS      | SL      | N L     | U N     | TR      | PT      | SF      | IS      | SN      | RV      |
| Reversing Supervision Information                    | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | A       |
| Default Balise/Loop/RIU Information                  | NR      | A [2]    | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| Track Ahead Free up to level 2/3 transition location | NR      | A [2]    | R       | R       | A       | A       | A       | A       | R       | R       | A       | A       | A       | NR      | NR      | A       | R       |
| Permitted Braking Distance Information               | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Level Crossing information                           | NR      | A[2][ 4] | R       | R       | A       | A       | A       | A       | R       | R       | A       | R       | A [1]   | NR      | NR      | A       | R       |
| Virtual Balise Cover order                           | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| Generic LS function marker                           | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |
| LSSMA display toggle on order                        | NR      | R        | R       | R       | A [9]   | A       | A [9]   | A [9]   | R       | R       | A [9]   | R       | R       | NR      | NR      | A [9]   | R       |
| LSSMA display toggle off order                       | NR      | R        | R       | R       | R       | A       | R       | R       | R       | R       | R       | R       | R       | NR      | NR      | R       | R       |
| Data to be used by applications outside ERTMS/ETCS   | NR      | A        | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | A       | NR      | NR      | A       | A       |

- [1]: for level 2/3: only if following the reception of the information 'Recognition of Exit from TR mode' with a more recent time stamp; for level 1: rejected
- [2]: only if a cab is active
- [3]: for order to establish a communication session: RBC ID/phone number is stored without establishing the communication session
- [4]: only if valid Train Data are stored on-board
- [5]: only level transition announcement (i.e., immediate level transition order and conditional level transition order shall be rejected)
- [6]: rejected if override is active
- [7]:  only  immediate level transition order  and conditional level transition order shall be accepted (i.e., level transition announcement shall be rejected) and stored for later evaluation (see 4.4.8.1.5)
- [8]:  only  RBC  transition  order  with  null  distance  to  execution  shall  be  accepted  (i.e.,  RBC  transition announcement shall be rejected) for storing the RBC ID/phone number (see 4.4.8.1.5.2 &amp; 4.4.20.1.13)
- [9]: only if the max safe front end of the train is inside the Limited Supervision area of a mode profile received in the same message

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.8.5 Handling of transition buffer in case of level transition announcement or RBC/RBC handover

- 4.8.5.1 If an order to switch to level NTC, 1, 2 or 3 at a further location has been received, the ERTMS/ETCS  onboard  equipment  shall  be  able  to  store  in  a  transition  buffer  (see figure 3, first filter) three sets of information obtained from three filtered messages.
- 4.8.5.2 If  a  RBC  transition  order  has  been  received  and  the  Handing  Over  RBC  is  still  the supervising  one,  the  ERTMS/ETCS  onboard  equipment  shall  be  able  to  store  in  a transition  buffer  (see  figure  3,  second  filter)  three  sets  of  information  obtained  from three filtered messages from the Accepting RBC.
- 4.8.5.2.1 Note: the term 'set of information' refers to the part of a message being stored in the transition  buffer  (i.e.  information  which  is  neither  accepted  nor  rejected  immediately) according  to  the  conditions  stated  in  4.8.3.1  [1]  and  [2]  (for  level  transition)  or according to 4.8.2.1c (for RBC/RBC handover).
- 4.8.5.3 In case three sets of information are already stored in the transition buffer, any new set to be stored shall replace the oldest one currently stored.
- 4.8.5.4 The sets of information stored in the transition buffer shall be deleted:
- a) in case the level transition order is deleted or overwritten by another level transition order for a different level, OR
- b) in case the RBC transition order is deleted or overwritten by an order to switch to another Accepting RBC, OR
- c)  in  case  the  communication  session  with  the  RBC  that  provided  the  stored information is terminated
- 4.8.5.5 At the same time the level transition is performed or at the same time the Accepting RBC  becomes  the  supervising  one,  the  sets  of  information  stored  in  the  transition buffer shall be released and re-evaluated in the sequence they have been received.
- 4.8.5.6 This sequential re-evaluation of all the released information shall be a prerequisite to any use by the on-board equipment (e.g. it will lead neither to an intermediate change of  mode  nor  to  a  change  of  information  displayed  to  the  driver)  and  shall  obey  the following principles:
- a) Starting  from  the  information  currently  used  by  on-board  at  the  moment  the level/RBC  transition  is  effective,  the  ERTMS/ETCS  on-board  equipment  shall determine  the  new  information  for  train  supervision,  by  performing  sequential updates from the information released from the transition buffer, if accepted.
- b) For each information update related to a re-evaluated set of information, the same rules  shall  apply  as  to  information  update  related  to  new  information  accepted outside a level/RBC transition context.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- c)  The  information  resulting  from  this  sequential  update  shall  then  be  used  by  the ERTMS/ETCS on-board equipment.
2. 4.8.5.7 Accepting  re-evaluated  Conditional  Emergency  Stop  information  according  to  table 4.8.3  implies  that  the  accepted  Conditional  Emergency  Stop  information  may  be accepted or  rejected  in  a  further  step  (see  clause  3.10.2.2)  depending  on  the  given stop location. This decision, based on the comparison between the min safe front end position of the train at the time the message was received and the given stop location, shall be considered part of the evaluation process as it affects the further re-evaluation of information stored in the transition buffer (see clause 3.10.2.4).
3. 4.8.5.7.1 Note:  For  the  case  of  the  Unconditional  Emergency  Stop  information  accepting  the information  according  to  table  4.8.3  will  always  lead  to  the  train  being  tripped  (see clause 3.10.2.3) when re-evaluation of the transition buffer is completed. Information accepted during re-evaluation of information stored in the transition buffer can then be affected on transition to TR mode according to conditions in Table 4.10.
4. 4.8.5.8 Note: The requirement to acknowledge an Emergency Stop information according to clause 3.10.1.4, i.e., communicating to the RBC if the information has been accepted (Conditional or Unconditional Emergency Stop) or rejected because the train has passed the stop location (Conditional Emergency Stop only), applies to the time when the information is used, immediately after the sequential update has been completed. Regards acknowledging the reception of an emergency stop message, as for any other information received from trackside, see clause 3.16.3.5.

Chapter 4 : Modes and Transitions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.9 What happens to accepted and stored information when entering a given level

## 4.9.1 Introduction

- 4.9.1.1 Every data that can be stored onboard after being accepted may be influenced by a level transition.
- 4.9.1.2 A level transition acts on the 'status' of stored information.
- 4.9.1.3 In case of entering level 1, MA Request Parameters, Position Report Parameters and Track Ahead Free Request shall be deleted.
- 4.9.1.3.1 In  case  of  entering  level  0,  NTC  or  1,  the  information  'Inhibition  of  revocable  TSRs from balises in L2/3' shall be deleted.
- 4.9.1.4 For all other stored data, a level transition has no effect (void).

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.10 What happens to accepted and stored information when entering a given mode

## 4.10.1 Introduction

- 4.10.1.1 Every data that can be stored onboard after being accepted may be influenced by a mode transition.
- 4.10.1.2 A mode transition acts on the 'status' of stored information.
- 4.10.1.3 Depending on which mode is entered, the action shall be one of the following:
- a) data is deleted,
- b) data is to be revalidated,
- c)  data is reset (set to default values)
- d) data status is unchanged,
- e) not relevant (the action on the data cannot be determined. This concerns the entry in SF and IS modes)

D = Deleted TBR = To Be Revalidated U = Unchanged NR = Not relevant R = Reset

|                                    | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   |
|------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Data Stored on-board               | NP             | SB             | PS             | SH             | FS             | LS             | SR             | OS             | SL             | NL             | UN             | TR             | PT             | SF             | IS             | SN             | RV             |
| National Values                    | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Not yet applicable National Values | D              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Linking                            | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Movement Authority                 | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Gradient Profile                   | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| International SSP                  | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Axle load speed profile            | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| STM max speed                      | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | U              | U              | U              | NR             | NR             | U              | D              |
| STM system speed/distance          | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | U              | U              | U              | NR             | NR             | U              | D              |
| Level Transition Order             | D              | D [1] [2]      | U              | D [2]          | U              | U              | D              | U              | D [2]          | D [1]          | D              | U              | U              | NR             | NR             | D              | D              |
| Stop Shunting on desk opening      | D              | D              | U              | U              | U              | U              | U              | U              | D              | U              | U              | U              | U              | NR             | NR             | U              | U              |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|                                                                                                       | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   |
|-------------------------------------------------------------------------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Data Stored on-board                                                                                  | NP             | SB             | PS             | SH             | FS             | LS             | SR             | OS             | SL             | NL             | UN             | TR             | PT             | SF             | IS             | SN             | RV             |
| List of balises for SH area                                                                           | D              | D              | U              | U              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| MA Request Parameters                                                                                 | D              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Position Report parameters                                                                            | D              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| List of Balises in SR Authority + SR mode speed limit and distance                                    | D              | D              | D              | D              | D              | D              | U              | D              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Temporary Speed Restriction                                                                           | D              | D              | D              | D              | U              | U              | U              | U              | D              | D              | U              | U              | U              | NR             | NR             | D              | D              |
| Inhibition of revocable TSRs from balises in L2/3                                                     | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | U              | U              | NR             | NR             | D              | D              |
| Default Gradient for TSR                                                                              | D              | D              | D              | D              | U              | U              | U              | U              | D              | D              | U              | U              | U              | NR             | NR             | D              | D              |
| Signalling related Speed Restriction                                                                  | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Route Suitability Data                                                                                | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Adhesion Factor (from trackside)                                                                      | R              | R              | R              | R              | U              | U              | U              | U              | R              | R              | U              | U              | U              | NR             | NR             | R              | U              |
| Adhesion Factor (from driver)                                                                         | R              | R              | R              | R              | U              | U              | U              | U              | R              | R              | U              | U              | U              | NR             | NR             | U              | U              |
| Plain Text Information                                                                                | D              | D              | D              | D              | U              | U              | U              | U              | D              | D              | U              | U              | U              | NR             | NR             | D              | U              |
| Fixed Text Information                                                                                | D              | D              | D              | D              | U              | U              | U              | U              | D              | D              | U              | U              | U              | NR             | NR             | D              | U              |
| Geographical Position                                                                                 | D              | U              | D              | D              | U              | U              | U              | U              | D              | U              | U              | U              | U              | NR             | NR             | D              | D              |
| Mode Profile                                                                                          | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| RBC Transition Order                                                                                  | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Radio Infill Area information                                                                         | D              | D              | D              | D              | U              | U              | D              | D              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| EOLM information                                                                                      | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Track Conditions excluding sound horn, non stopping areas, tunnel stopping areas and big metal masses | R              | R              | R              | R              | U              | U              | R              | U              | R              | U              | R              | U              | U              | NR             | NR             | R              | R              |
| Track conditions sound horn, non stopping areas, tunnel stopping areas                                | R              | R              | R              | R              | U              | U              | R              | U              | R              | R              | R              | R              | R              | NR             | NR             | R              | R              |
| Track condition big metal masses                                                                      | R              | R              | R              | R              | U              | U              | R              | U              | R              | U              | U              | U              | U              | NR             | NR             | U              | R              |
| Unconditional Emergency Stops                                                                         | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | U              | U              | NR             | NR             | D              | D              |
| Conditional Emergency Stops                                                                           | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | U              | U              | NR             | NR             | D              | D              |
| Train Position                                                                                        | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Data Stored on-board                               | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   | Entered Mode   |
|----------------------------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Data Stored on-board                               | NP             | SB             | PS             | SH             | FS             | LS             | SR             | OS             | SL             | NL             | UN             | TR             | PT             | SF             | IS             | SN             | RV             |
| Train Data                                         | D              | TBR            | U              | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| ERTMS/ETCS level                                   | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Table of priority of trackside supported levels    | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Driver ID                                          | D              | TBR            | U              | U              | U              | U              | U              | U              | D              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Radio Network ID                                   | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| RBC ID/Phone Number                                | TBR            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Train Running Number                               | D              | TBR            | U              | U              | U              | U              | U              | U              | D              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Reversing Area Information                         | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | U              |
| Reversing Supervision Information                  | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | U              |
| Track Ahead Free Request                           | D              | D              | D              | D              | D              | D              | U              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Permitted Braking Distance Information             | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| Level Crossing information                         | D              | D              | D              | D              | U              | U              | D              | U              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |
| RBC/RIU System Version                             | D              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Operated System Version                            | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Virtual Balise Covers                              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Language used to display information to the driver | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| Generic LS function marker                         | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | U              | NR             | NR             | U              | U              |
| LSSMA display toggle on order                      | D              | D              | D              | D              | D              | U              | D              | D              | D              | D              | D              | D              | U              | NR             | NR             | D              | D              |

- [1]: exception: 'U' when coming from SH

- [2]: exception: 'U' when coming from PS

## 4.10.1.4 NOTES:

- 4.10.1.4.1  Intentionally deleted.
- 4.10.1.4.2  The following information is not considered to be stored information:
- a) Repositioning information
- b) Session Management (exception: the RBC ID/phone number, which is given with an order to establish a communication session, is stored on-board)
- c)  Danger for SH information
- d) Assignment of Co-ordinate system
- e) Infill Location Reference

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- f)  Location Identity (NID\_C + NID\_BG transmitted in the balise telegram)
- g) Recognition of exit from TRIP mode
- h) Acknowledgement of Train Data
- i)  SH refused
- j)  SH authorised
- k)  Balise/loop System Version
- l) Intentionally deleted
- m)  Intentionally deleted
- n) Revocation of Emergency Stop (Conditional or Unconditional)
- o) Temporary Speed Restriction Revocation
- p) Intentionally deleted
- q) Acknowledgement of session termination
- r)  Default Balise Information
- s)  Co-operative shortening of MA (if this message is used, it replaces the movement authority)
- t)  Train Rejected
- u) Train Accepted
- v)  SoM position report confirmed by RBC
- w) Track Ahead Free up to level 2/3 transition location
- x)  Signalling related speed restriction value zero (i.e., train trip order)
- y)  Stop if in SR mode
- z)  Data to be forwarded to a National System through the STM interface
22. aa)  LSSMA display toggle off order

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 4.11 What happens to stored information when exiting NP mode

- 4.11.1.1 Status of stored information, which is set to "Invalid" when No Power mode is entered, shall  be  affected,  when  relevant,  by  information  from  the  Cold  Movement  Detection function, according to the following table:
- 4.11.1.2 Note:  Status  of  stored  information,  which  remains  valid  after  NP  mode  has  been entered, is not affected by information from the Cold Movement Detection function.
- 4.11.1.3 If a cold movement has been detected, or the Cold Movement Detection function is not able  to  confirm  that  no  cold  movement  has  taken  place,  no  change  of  status  of information  to  'valid'  shall  be  made  until  it  has  been  validated  by  a  different  means than cold movement detection.

|                                                                   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   | Status of On-board stored information   |
|-------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
|                                                                   | EOLM information                        | EOLM information                        | EOLM information                        | Train Position                          | Train Position                          | Train Position                          | ERTMS/ETCS Level                        | ERTMS/ETCS Level                        | ERTMS/ETCS Level                        | Table of trackside supported levels     | Table of trackside supported levels     | Table of trackside supported levels     | RBC ID/Phone Number                     | RBC ID/Phone Number                     | RBC ID/Phone Number                     |
| Transition conditions                                             | Un- known                               | Invalid                                 | Vali d                                  | Un- known                               | Invalid                                 | Valid                                   | Un- know n                              | Invalid                                 | Valid                                   | Un- known                               | Invalid                                 | Valid                                   | Un- known                               | Invalid                                 | Valid                                   |
| No Cold movement occurred                                         |                                         |                                        |                                         |                                         |                                        |                                         |                                         |                                        |                                         |                                         |                                        |                                         |                                         |                                        |                                         |
| Cold movement detected or Cold movement information not available |                                         |                                        |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |
                                       |                                         |                                         |                                         |                                         |

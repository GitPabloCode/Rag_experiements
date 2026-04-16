## ERTMS/ETCS

## System Requirements Specification

## Chapter 6 Management of older System Versions

REF :

SUBSET-026-6

ISSUE :

3.6.0

DATE  :

13/05/2016

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.1 Modification History

| Issue Number Date   | Modification / Description                                                                                                                          | Author      |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| 3.0.0 23/12/08      | First and release version                                                                                                                           | Hougardy A. |
| 3.0.1 22/12/09      | Including the results of the editorial review of the SRS 3.0.0 and the other error CR's that are in state 'Analysis completed' according to ERA CCM | Hougardy A. |
| 3.1.0 22/02/10      | Release version                                                                                                                                     | Hougardy A. |
| 3.1.1 08/11/10      | Including all CR's that are in state 'Analysis completed' according to ERA CCM, plus CR731.                                                         | Hougardy A. |
| 3.2.0 22/12/10      | Release version                                                                                                                                     | Hougardy A. |
| 3.2.1 13/12/11      | Including all CR's that are in state 'Analysis completed' according to ERA CCM.                                                                     | Hougardy A. |
| 3.3.0 07/03/12      | Baseline 3 release version                                                                                                                          | Hougardy A. |
| 3.3.1 04/04/14      | CR's 1159, 1176, 1185                                                                                                                               | Gemine O.   |
| 3.3.2 23/04/14      | Baseline 3 1 st maintenance pre-release version                                                                                                     | Gemine O.   |
| 3.3.3 06/05/14      | CR 1223 Baseline 3 1 st maintenance 2 nd pre-release version                                                                                        | Gemine O.   |
| 3.4.0 12/05/14      | Baseline 3 1 st maintenance release version                                                                                                         | Gemine O.   |
| 3.4.1 23/06/14      | no change                                                                                                                                           | Gemine O.   |
| 3.4.2 17/11/15      | CR's 299, 1089, 1262, 1266, 1280                                                                                                                    | Gemine O.   |
| 3.4.3 16/12/15      | Update due to overall CR consolation phase                                                                                                          | Gemine O.   |
| 3.5.0 18/12/15      | Baseline 3 2 nd release version as recommended to EC (see ERA-REC-123-2015/REC)                                                                     | Gemine O.   |
| 3.5.1 28/04/16      | No change                                                                                                                                           | Gemine O.   |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

3.6.0

13/05/16

Baseline 3 2 nd release version

Hougardy A.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.2 Table of Contents

| 6.1   | Modification History ............................................................................................................ 2       | Modification History ............................................................................................................ 2       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 6.2   | Table of Contents ............................................................................................................... 4       | Table of Contents ............................................................................................................... 4       |
| 6.3   | Scope.................................................................................................................................. 5 | Scope.................................................................................................................................. 5 |
| 6.4   | Envelope of legally operated system versions.................................................................... 6                        | Envelope of legally operated system versions.................................................................... 6                        |
| 6.4.1 | 6.4.1                                                                                                                                     | Incompatible versions..................................................................................................6                  |
| 6.4.2 | 6.4.2                                                                                                                                     | Compatible versions ....................................................................................................6                 |
| 6.5   | Trackside requirements in relation to older system versions.............................................. 7                               | Trackside requirements in relation to older system versions.............................................. 7                               |
| 6.5.1 | 6.5.1                                                                                                                                     | Trackside areas operated with system version number X = 1.....................................7                                           |
| 6.5.2 | 6.5.2                                                                                                                                     | Trackside areas operated with system version number X = 2...................................32                                            |
| 6.6   | On-board requirements in relation to older system versions ............................................ 35                                | On-board requirements in relation to older system versions ............................................ 35                                |
| 6.6.1 | 6.6.1                                                                                                                                     | Introduction................................................................................................................ 35           |
| 6.6.2 | 6.6.2                                                                                                                                     | Specific requirements for on-board operating with system version number X = 1 ....35                                                      |
| 6.6.3 | 6.6.3                                                                                                                                     | Handling of air gap data related to system version number X = 1.............................35                                            |
| 6.6.4 | 6.6.4                                                                                                                                     | Handling of air gap data related to system version number X.Y = 2.0 ......................46                                              |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.3 Scope

- 6.3.1.1 The chapter defines the composition of envelope of legally operated system versions, i.e.  all  the  ERTMS/ETCS  system  versions  that  trackside  shall  be  allowed  to  operate and that on-board equipment shall support.
- 6.3.1.2 By default, all the clauses listed in the other SRS chapters are applicable regardless of the  system  version  operated  (see  SUBSET-104  §  6.1.3.2);  this  chapter  includes  the exceptions to those clauses and the additional clauses, which apply when the system version of some trackside constituents and/or the system version operated relates to a version number older than the last one introduced.

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.4 Envelope of legally operated system versions

## 6.4.1 Incompatible versions

- 6.4.1.1 The system version number X, which a trackside infrastructure is allowed to operate with, shall be one of the following: 1 or 2

## 6.4.2 Compatible versions

- 6.4.2.1 Within  system  version  number  X  =  1,  the  system  version  number  Y  that  a  trackside infrastructure is allowed to use shall be any of the following: 0 or 1
- 6.4.2.2 Within  system  version  number  X  =  2,  the  system  version  number  Y  that  a  trackside infrastructure is allowed to use shall be any of the following: 0 or 1

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.5 Trackside requirements in relation to older system versions

## 6.5.1 Trackside areas operated with system version number X = 1

## 6.5.1.1 Introduction

- 6.5.1.1.1 The  section  is  applicable  for  trackside  infrastructures  that  will  be  tendered  and  still operated with the system version number X = 1, after the entry into force of this release of the SRS.
- 6.5.1.1.2 Within a trackside infrastructure operated with the system version number X = 1, it shall be allowed to use the following values of M\_VERSION: 1.0, and 1.1
- 6.5.1.1.3 Within a trackside area operated with an RBC certified to the system version number X = 1, it shall also be allowed to use for balises the following values of M\_VERSION: 2.0 and 2.1.
- 6.5.1.1.3.1  Note:  this  configuration  is  meaningful  in  case  the  trains  operating  on  this  RBC  area support the system version number X = 2 and the on-board requirements related to the trackside information marked with 2.0 or 2.1 are applicable regardless of the operated version (i.e. they are applied by the on-board equipment even if this latter operates with the system version number X = 1 ordered by RBC).

## 6.5.1.2 Exceptions to chapter 3

6.5.1.2.1 Intentionally deleted.

- 6.5.1.2.1.1  Section 3.6.2.4 shall not apply.

6.5.1.2.2

Clause  3.7.1.1  b)  shall  be  replaced  with:  'When  needed,  limitations  related  to  the movement authority, i.e. Mode profile for On Sight or Shunting and signalling related speed restriction (see sections 3.12.4 and 3.11.6). Mode profile and Signalling related Speed restriction shall always be sent together with the MA to which the information belongs'

- 6.5.1.2.3 In clause 3.7.1.1 c), the bullet 'Optionally Speed restriction to ensure a given permitted braking distance (see section 3.11. 11)' shall not apply.
- 6.5.1.2.4 In clause 3.7.2.4, the bullet 'LX speed restrictions' shall not apply.
- 6.5.1.2.5 In  clause  3.7.2.4,  the  bullet  'Inhibition  of  revocable  TSRs  from  balises  in  L2/3  (from RBC only)' shall not apply.
- 6.5.1.2.6 Clause 3.9.3.2 shall be replaced with: 'The orders shall be sent via balise groups.'
- 6.5.1.2.7 Clause 3.9.3.8.1 shall not apply.
- 6.5.1.2.8 Clause 3.11.3.2.2 c) shall not apply.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.1.2.9 Clause 3.11.3.2.3.1 shall be replaced with: 'If at least one other specific SSP is less restrictive  than  any  'Cant  Deficiency'  SSP,  it  is  the  responsibility  of  the  trackside engineering to ensure that for all possible combinations of international train categories a  train  might  belong  to,  the  ERTMS/ETCS  on-board  equipment  will  not  replace  the 'Cant  Deficiency'  SSP  as  selected  in  3.11.3.2.3  leading  to  an  unsafe  situation  by applying the requirement 3.11.3.2.6'

- 6.5.1.2.10  Clause 3.11.5.12 shall not apply.
- 6.5.1.2.11  Clauses 3.11.9.1, 3.12.5.1, 3.12.5.2, 3.12.5.4, 3.12.5.5, 3.12.5.6, 3.12.5.7, 3.15.1.2.3.1 o) shall not apply.
- 6.5.1.2.12  Clauses 3.11.11.1, 3.11.11.2 shall not apply
- 6.5.1.2.13  Clause 3.12.3.4.3.2 shall not apply.
- 6.5.1.2.14  Clauses 3.12.3.1.11 and 3.12.3.5.1 shall not apply.
- 6.5.1.2.15  Clause  3.12.4.1  shall  be  replaced  with:  'It  shall  be  possible  for  trackside  to  send  a Mode Profile. The Mode Profile can request On Sight mode and Shunting mode.'
- 6.5.1.2.16  Intentionally deleted.
- 6.5.1.2.17  Clause 3.15.1.2.3.1 p) shall not apply.

## 6.5.1.3 Exceptions to chapter 4

6.5.1.3.1 Void.

## 6.5.1.4 Exceptions to chapter 5

6.5.1.4.1 Void.

## 6.5.1.5 Exceptions to chapter 7

6.5.1.5.1 Clause 7.3.3.5 shall be replaced with: 'Exception: Packet 255 'End of Telegram' does not follow the above defined structure.'

## 6.5.1.5.2 The table 7.4.1.1 shall be replaced with:

|   Packet Number | Packet Name                                   | Page N°   |
|-----------------|-----------------------------------------------|-----------|
|               2 | System Version Order                          |           |
|               3 | National Values                               |           |
|               5 | Linking                                       |           |
|               6 | Virtual Balise Cover order                    |           |
|              12 | Level 1 Movement Authority                    |           |
|              15 | Level 2/3 Movement Authority                  |           |
|              16 | Repositioning Information                     |           |
|              21 | Gradient Profile                              |           |
|              27 | International Static Speed Profile            |           |
|              39 | Track Condition Change of traction system {1} |           |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   Packet Number | Packet Name                                              | Page N°   |
|-----------------|----------------------------------------------------------|-----------|
|              41 | Level Transition Order                                   |           |
|              42 | Session Management                                       |           |
|              44 | Data used by applications outside the ERTMS/ETCS system. |           |
|              45 | Radio Network registration                               |           |
|              46 | Conditional Level Transition Order                       |           |
|              49 | List of balises for SH Area                              |           |
|              51 | Axle load Speed Profile                                  |           |
|              57 | Movement Authority Request Parameters                    |           |
|              58 | Position Report Parameters                               |           |
|              63 | List of Balises in SR Authority                          |           |
|              65 | Temporary Speed Restriction                              |           |
|              66 | Temporary Speed Restriction Revocation                   |           |
|              67 | Track Condition Big Metal Masses                         |           |
|              68 | Track Condition {1}                                      |           |
|              70 | Route Suitability Data {1}                               |           |
|              71 | Adhesion Factor                                          |           |
|              72 | Packet for sending plain text messages                   |           |
|              79 | Geographical Position Information                        |           |
|              80 | Mode profile                                             |           |
|              90 | Track Ahead Free up to level 2/3 transition location     |           |
|             131 | RBC transition order                                     |           |
|             132 | Danger for Shunting information                          |           |
|             133 | Radio infill area information                            |           |
|             134 | EOLM Packet                                              |           |
|             135 | Stop Shunting on desk opening                            |           |
|             136 | Infill location reference                                |           |
|             137 | Stop if in Staff Responsible                             |           |
|             138 | Reversing area information                               |           |
|             139 | Reversing supervision information                        |           |
|             140 | Train running number from RBC                            |           |
|             141 | Default Gradient for Temporary Speed Restriction         |           |
|             145 | Inhibition of balise group message consistency reaction  |           |
|             200 | Virtual Balise Cover marker                              |           |
|             203 | National Values for braking curves                       |           |
|             206 | Track Condition                                          |           |
|             207 | Route Suitability Data                                   |           |
|             239 | Track Condition Change of traction system                |           |
|             254 | Default balise, loop or RIU information                  |           |

{1}Note: used on lines where trains are operated with on-board equipment supporting only system version = 1.0.

## 6.5.1.5.2.1  The table 7.4.1.2 shall be replaced with:

|   Packet Number | Packet Name                                | Page N°   |
|-----------------|--------------------------------------------|-----------|
|               0 | Position Report                            |           |
|               1 | Position Report based on two balise groups |           |

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   Packet Number | Packet Name                                              | Page N°   |
|-----------------|----------------------------------------------------------|-----------|
|               3 | Onboard telephone numbers                                |           |
|               4 | Error Reporting                                          |           |
|               9 | Level 2/3 transition information                         |           |
|              11 | Validated train data                                     |           |
|              44 | Data used by applications outside the ERTMS/ETCS system. |           |

6.5.1.5.3 Section 7.4.2.0 (Packet Number 0: Virtual Balise Cover marker) shall not apply.

6.5.1.5.4 Table 7.4.2.1.1 (Packet Number 3: National Values) shall be replaced with:

| Description    | Downloads a set of National Values to the train   | Downloads a set of National Values to the train   | Downloads a set of National Values to the train             |
|----------------|---------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------|
| Transmitted by | Balise, RBC                                       | Balise, RBC                                       | Balise, RBC                                                 |
| Content        | Variable                                          | Length                                            | Comment                                                     |
|                | NID_PACKET                                        | 8                                                 |                                                             |
|                | Q_DIR                                             | 2                                                 |                                                             |
|                | L_PACKET                                          | 13                                                |                                                             |
|                | Q_SCALE                                           | 2                                                 |                                                             |
|                | D_VALIDNV                                         | 15                                                |                                                             |
|                | N_ITER                                            | 5                                                 |                                                             |
|                | NID_C(k)                                          | 10                                                | Identification of national area(s) to which the set applies |
|                | V_NVSHUNT                                         | 7                                                 |                                                             |
|                | V_NVSTFF                                          | 7                                                 |                                                             |
|                | V_NVONSIGHT                                       | 7                                                 |                                                             |
|                | V_NVUNFIT                                         | 7                                                 |                                                             |
|                | V_NVREL                                           | 7                                                 |                                                             |
|                | D_NVROLL                                          | 15                                                |                                                             |
|                | Q_NVSRBKTRG                                       | 1                                                 |                                                             |
|                | Q_NVEMRRLS                                        | 1                                                 |                                                             |
|                | V_NVALLOWOVTRP                                    | 7                                                 |                                                             |
|                | V_NVSUPOVTRP                                      | 7                                                 |                                                             |
|                | D_NVOVTRP                                         | 15                                                |                                                             |
|                | T_NVOVTRP                                         | 8                                                 |                                                             |
|                | D_NVPOTRP                                         | 15                                                |                                                             |
|                | M_NVCONTACT                                       | 2                                                 |                                                             |
|                | T_NVCONTACT                                       | 8                                                 |                                                             |
|                | M_NVDERUN                                         | 1                                                 |                                                             |
|                | D_NVSTFF                                          | 15                                                |                                                             |
|                | Q_NVDRIVER_ADHES                                  | 1                                                 |                                                             |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.1.5.5 Section  7.4.2.3.1  (Packet  Number  13:  Staff  Responsible  distance  Information  from loop) shall not apply.

6.5.1.5.6 Table 7.4.2.7 (Packet Number 27: International Static Speed Profile) shall be replaced with:

| Description    | Static speed profile and optionally speed limits depending on the international train category.   | Static speed profile and optionally speed limits depending on the international train category.   | Static speed profile and optionally speed limits depending on the international train category.   |
|----------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Transmitted by | Any                                                                                               | Any                                                                                               | Any                                                                                               |
| Content        | Variable                                                                                          | Length                                                                                            | Comment                                                                                           |
| Content        | NID_PACKET                                                                                        | 8                                                                                                 |                                                                                                   |
| Content        | Q_DIR                                                                                             | 2                                                                                                 |                                                                                                   |
| Content        | L_PACKET                                                                                          | 13                                                                                                |                                                                                                   |
| Content        | Q_SCALE                                                                                           | 2                                                                                                 |                                                                                                   |
| Content        | D_STATIC                                                                                          | 15                                                                                                |                                                                                                   |
| Content        | V_STATIC                                                                                          | 7                                                                                                 |                                                                                                   |
| Content        | Q_FRONT                                                                                           | 1                                                                                                 |                                                                                                   |
| Content        | N_ITER                                                                                            | 5                                                                                                 |                                                                                                   |
| Content        | NC_DIFF(n)                                                                                        | 4                                                                                                 |                                                                                                   |
| Content        | V_DIFF(n)                                                                                         | 7                                                                                                 |                                                                                                   |
| Content        | N_ITER                                                                                            | 5                                                                                                 |                                                                                                   |
| Content        | D_STATIC(k)                                                                                       | 15                                                                                                |                                                                                                   |
| Content        | V_STATIC(k)                                                                                       | 7                                                                                                 |                                                                                                   |
| Content        | Q_FRONT(k)                                                                                        | 1                                                                                                 |                                                                                                   |
| Content        | N_ITER(k)                                                                                         | 5                                                                                                 |                                                                                                   |
| Content        | NC_DIFF(k,m)                                                                                      | 4                                                                                                 |                                                                                                   |
| Content        | V_DIFF(k,m)                                                                                       | 7                                                                                                 |                                                                                                   |

6.5.1.5.7 Table 7.4.2.8 (Packet Number 39: Track Condition Change of traction system) shall be replaced with:

| Description    | The packet gives information about change of the traction system.   | The packet gives information about change of the traction system.   | The packet gives information about change of the traction system.   |
|----------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Transmitted by | Any                                                                 | Any                                                                 | Any                                                                 |
| Content        | Variable                                                            | Length                                                              | Comment                                                             |
| Content        | NID_PACKET                                                          | 8                                                                   |                                                                     |
| Content        | Q_DIR                                                               | 2                                                                   |                                                                     |
| Content        | L_PACKET                                                            | 13                                                                  |                                                                     |
| Content        | Q_SCALE                                                             | 2                                                                   |                                                                     |
| Content        | D_TRACTION                                                          | 15                                                                  |                                                                     |
| Content        | M_TRACTION                                                          | 8                                                                   | Identity of the traction system                                     |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.1.5.8 Section  7.4.2.8.1  (Packet  Number  40:  Track  Condition  Change  of  allowed  current consumption) shall not apply.

6.5.1.5.9 Table 7.4.2.11 (Packet Number 44: Data used by applications outside the ERTMS/ETCS system) shall be replaced with:

| Description    | Messages between trackside and on-board devices, which contain information used by applications outside the ERTMS/ETCS system.   | Messages between trackside and on-board devices, which contain information used by applications outside the ERTMS/ETCS system.   | Messages between trackside and on-board devices, which contain information used by applications outside the ERTMS/ETCS system.   |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Transmitted by | Any                                                                                                                              | Any                                                                                                                              | Any                                                                                                                              |
| Content        | Variable                                                                                                                         | Length                                                                                                                           | Comment                                                                                                                          |
| Content        | NID_PACKET                                                                                                                       | 8                                                                                                                                |                                                                                                                                  |
| Content        | Q_DIR                                                                                                                            | 2                                                                                                                                |                                                                                                                                  |
| Content        | L_PACKET                                                                                                                         | 13                                                                                                                               |                                                                                                                                  |
| Content        | NID_XUSER                                                                                                                        | 9                                                                                                                                |                                                                                                                                  |
| Content        | Other data, depending NID_XUSER                                                                                                  |                                                                                                                                  |                                                                                                                                  |

6.5.1.5.10  Table 7.4.2.13 (Packet Number 51: Axle Load Speed Profile) shall be replaced with:

| Description    | This packet gives the speed restrictions for trains with axle load higher than or equal to the specified value for the speed restriction   | This packet gives the speed restrictions for trains with axle load higher than or equal to the specified value for the speed restriction   | This packet gives the speed restrictions for trains with axle load higher than or equal to the specified value for the speed restriction   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Transmitted by | Any                                                                                                                                        | Any                                                                                                                                        | Any                                                                                                                                        |
| Content        | Variable                                                                                                                                   | Length                                                                                                                                     | Comment                                                                                                                                    |
|                | NID_PACKET                                                                                                                                 | 8                                                                                                                                          |                                                                                                                                            |
|                | Q_DIR                                                                                                                                      | 2                                                                                                                                          |                                                                                                                                            |
|                | L_PACKET                                                                                                                                   | 13                                                                                                                                         |                                                                                                                                            |
|                | Q_SCALE                                                                                                                                    | 2                                                                                                                                          |                                                                                                                                            |
|                | Q_TRACKINIT                                                                                                                                | 1                                                                                                                                          |                                                                                                                                            |
|                | D_AXLELOAD                                                                                                                                 | 15                                                                                                                                         |                                                                                                                                            |
|                | L_AXLELOAD                                                                                                                                 | 15                                                                                                                                         |                                                                                                                                            |
|                | Q_FRONT                                                                                                                                    | 1                                                                                                                                          |                                                                                                                                            |
|                | N_ITER                                                                                                                                     | 5                                                                                                                                          |                                                                                                                                            |
|                | M_AXLELOAD(n)                                                                                                                              | 7                                                                                                                                          |                                                                                                                                            |
|                | V_AXLELOAD(n)                                                                                                                              | 7                                                                                                                                          | Speed restriction to be applied if the axle load of the train  M_AXLELOAD(n)                                                              |
|                | N_ITER                                                                                                                                     | 5                                                                                                                                          |                                                                                                                                            |
|                | D_AXLELOAD(k)                                                                                                                              | 15                                                                                                                                         |                                                                                                                                            |
|                | L_AXLELOAD(k)                                                                                                                              | 15                                                                                                                                         |                                                                                                                                            |
|                | Q_FRONT(k)                                                                                                                                 | 1                                                                                                                                          |                                                                                                                                            |
|                | N_ITER(k)                                                                                                                                  | 5                                                                                                                                          |                                                                                                                                            |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| M_AXLELOAD(k,m)   |   7 |                                                                                 |
|-------------------|-----|---------------------------------------------------------------------------------|
| V_AXLELOAD(k,m)   |   7 | Speed restriction to be applied if the axle load of the train  M_AXLELOAD(k,m) |

- 6.5.1.5.11  Section 7.4.2.13.1 (Packet Number 52: Permitted Braking Distance Information) shall not apply.
- 6.5.1.5.12  Section  7.4.2.16.1  (Packet  Number  64:  Inhibition  of  revocable  TSRs  from  balises  in L2/3) shall not apply.
- 6.5.1.5.13  Section  7.4.2.20.1  (Packet  Number  69:  Track  Condition  Station  Platforms)  shall  not apply.
- 6.5.1.5.14  Table 7.4.2.21 (Packet Number 70: Route Suitability data) shall be replaced with:

| Description    | The packet gives the characteristics needed to enter a route.   | The packet gives the characteristics needed to enter a route.   | The packet gives the characteristics needed to enter a route.              |
|----------------|-----------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| Transmitted by | Any                                                             | Any                                                             | Any                                                                        |
| Content        | Variable                                                        | Length                                                          | Comment                                                                    |
| Content        | NID_PACKET                                                      | 8                                                               |                                                                            |
| Content        | Q_DIR                                                           | 2                                                               |                                                                            |
| Content        | L_PACKET                                                        | 13                                                              |                                                                            |
| Content        | Q_SCALE                                                         | 2                                                               |                                                                            |
| Content        | Q_TRACKINIT                                                     | 1                                                               |                                                                            |
| Content        | D_TRACKINIT                                                     | 15                                                              | Only if Q_TRACKINIT = 1                                                    |
| Content        | D_SUITABILITY                                                   | 15                                                              | Only If Q_TRACKINIT = 0, D_SUITABILITY and the following variables follows |
| Content        | Q_SUITABILITY                                                   | 2                                                               |                                                                            |
| Content        | M_AXLELOAD                                                      | 7                                                               | If Q_SUITABILITY = Max axle load.                                          |
| Content        | M_TRACTION                                                      | 8                                                               | If Q_SUITABILITY = traction system                                         |
| Content        | N_ITER                                                          | 5                                                               |                                                                            |
| Content        | D_SUITABILITY(k)                                                | 15                                                              |                                                                            |
| Content        | Q_SUITABILITY(k)                                                | 2                                                               |                                                                            |
| Content        | M_AXLELOAD(k)                                                   | 7                                                               | If Q_SUITABILITY(k) = Max axle load.                                       |
| Content        | M_TRACTION(k)                                                   | 8                                                               | If Q_SUITABILITY(k) = traction system                                      |

6.5.1.5.15  Table 7.4.2.23 (Packet Number 72: Packet for sending plain text messages) shall be replaced with:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Description    |                    |             |                               |
|----------------|--------------------|-------------|-------------------------------|
| Transmitted by | Balise, RBC        | Balise, RBC | Balise, RBC                   |
| Content        | Variable           | Length      | Comment                       |
|                | NID_PACKET         | 8           |                               |
|                | Q_DIR              | 2           |                               |
|                | L_PACKET           | 13          |                               |
|                | Q_SCALE            | 2           |                               |
|                | Q_TEXTCLASS        | 2           |                               |
|                | Q_TEXTDISPLAY      | 1           |                               |
|                | D_TEXTDISPLAY      | 15          | Start condition               |
|                | M_MODETEXTDISPLAY  | 4           | Start condition               |
|                | M_LEVELTEXTDISPLAY | 3           | Start condition               |
|                | NID_NTC            | 8           | If M_LEVELTEXTDISPLAY = (NTC) |
|                | L_TEXTDISPLAY      | 15          | End condition                 |
|                | T_TEXTDISPLAY      | 10          | End condition                 |
|                | M_MODETEXTDISPLAY  | 4           | End condition                 |
|                | M_LEVELTEXTDISPLAY | 3           | End condition                 |
|                | NID_NTC            | 8           | If M_LEVELTEXTDISPLAY = (NTC) |
|                | Q_TEXTCONFIRM      | 2           |                               |
|                | L_TEXT             | 8           |                               |
|                | X_TEXT(L_TEXT)     | 8           |                               |

6.5.1.5.16  Section 7.4.2.24 (Packet Number 76: Packet for sending fixed text messages) shall not apply.

6.5.1.5.17  Table  7.4.2.25  (Packet  Number  79:  Geographical  Position  Information)  shall  be replaced with:

| Description    | This packet gives geographical location information for one or multiple references to the train.   | This packet gives geographical location information for one or multiple references to the train.   | This packet gives geographical location information for one or multiple references to the train.   |
|----------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Transmitted by | Balise, RBC                                                                                        | Balise, RBC                                                                                        | Balise, RBC                                                                                        |
| Content        | Variable                                                                                           | Comment                                                                                            |                                                                                                    |
| Content        | NID_PACKET                                                                                         | 8                                                                                                  |                                                                                                    |
| Content        | Q_DIR                                                                                              | 2                                                                                                  |                                                                                                    |
| Content        | L_PACKET                                                                                           | 13                                                                                                 |                                                                                                    |
| Content        | Q_SCALE                                                                                            | 2                                                                                                  |                                                                                                    |
| Content        | Q_NEWCOUNTRY                                                                                       | 1                                                                                                  |                                                                                                    |
| Content        | NID_C                                                                                              | if Q_NEWCOUNTRY = 1                                                                                |                                                                                                    |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| NID_BG          |   14 | Geographical Balise Group       | Position                        | Reference                       |
|-----------------|------|---------------------------------|---------------------------------|---------------------------------|
| D_POSOFF        |   15 |                                 |                                 |                                 |
| Q_MPOSITION     |    1 | Geographical direction          | Position                        | counting                        |
| M_POSITION      |   20 | Track kilometre reference value | Track kilometre reference value | Track kilometre reference value |
| N_ITER          |    5 |                                 |                                 |                                 |
| Q_NEWCOUNTRY(k) |    1 |                                 |                                 |                                 |
| NID_C(k)        |   10 | if Q_NEWCOUNTRY(k) = 1          | if Q_NEWCOUNTRY(k) = 1          | if Q_NEWCOUNTRY(k) = 1          |
| NID_BG(k)       |   14 | Geographical Balise Group       | Position                        | Reference                       |
| D_POSOFF(k)     |   15 |                                 |                                 |                                 |
| Q_MPOSITION(k)  |    1 | Geographical direction          | Position                        | counting                        |
| M_POSITION(k)   |   20 | Track kilometre reference value | Track kilometre reference value | Track kilometre reference value |

6.5.1.5.18  Table 7.4.2.26 (Packet Number 80: Mode profile) shall be replaced with:

| Description    | Mode profile associated to an MA   | Mode profile associated to an MA   | Mode profile associated to an MA   |
|----------------|------------------------------------|------------------------------------|------------------------------------|
| Transmitted by | Any                                | Any                                | Any                                |
| Content        | Variable                           | Length                             | Comment                            |
| Content        | NID_PACKET                         | 8                                  |                                    |
| Content        | Q_DIR                              | 2                                  |                                    |
| Content        | L_PACKET                           | 13                                 |                                    |
| Content        | Q_SCALE                            | 2                                  |                                    |
| Content        | D_MAMODE                           | 15                                 |                                    |
| Content        | M_MAMODE                           | 2                                  | OS, SH                             |
| Content        | V_MAMODE                           | 7                                  |                                    |
| Content        | L_MAMODE                           | 15                                 |                                    |
| Content        | L_ACKMAMODE                        | 15                                 |                                    |
| Content        | N_ITER                             | 5                                  |                                    |
| Content        | D_MAMODE(k)                        | 15                                 |                                    |
| Content        | M_MAMODE(k)                        | 2                                  | OS, SH                             |
| Content        | V_MAMODE(k)                        | 7                                  |                                    |
| Content        | L_MAMODE(k)                        | 15                                 |                                    |
| Content        | L_ACKMAMODE(k)                     | 15                                 |                                    |

6.5.1.5.19  Section 7.4.2.26.1 (Packet Number 88: Level Crossing information) shall not apply.

6.5.1.5.20  Section  7.4.2.37.1  (Packet  Number  143:  Session  Management  with  neighbouring Radio Infill Unit) shall not apply.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.1.5.20.1 Section 7.4.2.37.3 (Packet Number 180: LSSMA display toggle order) shall not apply.

- 6.5.1.5.20.2 Section  7.4.2.37.4  (Packet  Number  181:  Generic  LS  function  marker)  shall  not apply.
- 6.5.1.5.21  Added  section  7.4.2.37.3  (Packet  Number  200:  Virtual  Balise  Cover  marker)  shall apply:

Packet Number 200: Virtual Balise Cover marker

| Description    | Indication to on-board that the telegram can be ignored according to a VBC.   | Indication to on-board that the telegram can be ignored according to a VBC.   | Indication to on-board that the telegram can be ignored according to a VBC.   |
|----------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Transmitted by | Balise                                                                        | Balise                                                                        | Balise                                                                        |
| Content        | Variable                                                                      | Length                                                                        | Comment                                                                       |
|                | NID_PACKET                                                                    | 8                                                                             |                                                                               |
|                | Q_DIR                                                                         | 2                                                                             |                                                                               |
|                | L_PACKET                                                                      | 13                                                                            |                                                                               |
|                | NID_VBCMK                                                                     | 6                                                                             |                                                                               |

6.5.1.5.22  Added  section  7.4.2.37.4  (Packet  Number  203:  National  Values  for  braking  curves) shall apply:

Packet Number 203: National Values for braking curves

| Description    | Downloads a subset of National Values to the train, used for braking curves. This subset is a complement to the National Values included in packet 3.   | Downloads a subset of National Values to the train, used for braking curves. This subset is a complement to the National Values included in packet 3.   | Downloads a subset of National Values to the train, used for braking curves. This subset is a complement to the National Values included in packet 3.   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transmitted by | Balise, RBC                                                                                                                                             | Balise, RBC                                                                                                                                             | Balise, RBC                                                                                                                                             |
| Content        | Variable                                                                                                                                                | Length                                                                                                                                                  | Comment                                                                                                                                                 |
|                | NID_PACKET                                                                                                                                              | 8                                                                                                                                                       |                                                                                                                                                         |
|                | Q_DIR                                                                                                                                                   | 2                                                                                                                                                       |                                                                                                                                                         |
|                | L_PACKET                                                                                                                                                | 13                                                                                                                                                      |                                                                                                                                                         |
|                | Q_NVGUIPERM                                                                                                                                             | 1                                                                                                                                                       |                                                                                                                                                         |
|                | Q_NVSBFBPERM                                                                                                                                            | 1                                                                                                                                                       |                                                                                                                                                         |
|                | Q_NVINHSMICPERM                                                                                                                                         | 1                                                                                                                                                       |                                                                                                                                                         |
|                | A_NVMAXREDADH1                                                                                                                                          | 6                                                                                                                                                       |                                                                                                                                                         |
|                | A_NVMAXREDADH2                                                                                                                                          | 6                                                                                                                                                       |                                                                                                                                                         |
|                | A_NVMAXREDADH3                                                                                                                                          | 6                                                                                                                                                       |                                                                                                                                                         |
|                | M_NVAVADH                                                                                                                                               | 5                                                                                                                                                       |                                                                                                                                                         |
|                | M_NVEBCL                                                                                                                                                | 4                                                                                                                                                       |                                                                                                                                                         |
|                | Q_NVKINT                                                                                                                                                | 1                                                                                                                                                       |                                                                                                                                                         |
|                | Q_NVKVINTSET                                                                                                                                            | 2                                                                                                                                                       | Only if Q_NVKINT = 1, Q_NVKVINTSET and the following variables follow                                                                                   |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| A_NVP12         |   6 | Only if Q_NVKVINTSET = 1                                                                                                                                          |
|-----------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A_NVP23         |   6 | Only if Q_NVKVINTSET = 1                                                                                                                                          |
| V_NVKVINT       |   7 | = 0km/h                                                                                                                                                           |
| M_NVKVINT       |   7 | Valid between V_NVKVINT and V_NVKVINT(1) If Q_NVKVINTSET = 1, gives the correction factor if maximum emergency brake deceleration is lower than A_NVP12           |
| M_NVKVINT       |   7 | Only if Q_NVKVINTSET = 1 Valid between V_NVKVINT and V_NVKVINT(1) Gives the correction factor if maximum emergency brake deceleration is higher than A_NVP23      |
| N_ITER          |   5 |                                                                                                                                                                   |
| V_NVKVINT(n)    |   7 |                                                                                                                                                                   |
| M_NVKVINT(n)    |   7 | Valid between V_NVKVINT(n) and V_NVKVINT(n+1) If Q_NVKVINTSET = 1, gives the correction factor if maximum emergency brake deceleration is lower than A_NVP12      |
| M_NVKVINT(n)    |   7 | Only if Q_NVKVINTSET = 1 Valid between V_NVKVINT(n) and V_NVKVINT(n+1) Gives the correction factor if maximum emergency brake deceleration is higher than A_NVP23 |
| N_ITER          |   5 |                                                                                                                                                                   |
| Q_NVKVINTSET(k) |   2 |                                                                                                                                                                   |
| A_NVP12(k)      |   6 | Only if Q_NVKVINTSET(k) = 1                                                                                                                                       |
| A_NVP23(k)      |   6 | Only if Q_NVKVINTSET(k) = 1                                                                                                                                       |
| V_NVKVINT(k)    |   7 | = 0km/h                                                                                                                                                           |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| M_NVKVINT(k)   |   7 | Valid between V_NVKVINT(k) and V_NVKVINT(k,1) If Q_NVKVINTSET(k) = 1, gives the correction factor if maximum emergency brake deceleration is lower than A_NVP12(k)          |
|----------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_NVKVINT(k)   |   7 | Only if Q_NVKVINTSET(k) = 1 Valid between V_NVKVINT(k) and V_NVKVINT(k,1) Gives the correction factor if maximum emergency brake deceleration is higher than A_NVP23(k)     |
| N_ITER(k)      |   5 |                                                                                                                                                                             |
| V_NVKVINT(k,m) |   7 |                                                                                                                                                                             |
| M_NVKVINT(k,m) |   7 | Valid between V_NVKVINT(k,m) and V_NVKVINT(k,m+1) If Q_NVKVINTSET(k) = 1, gives the correction factor if maximum emergency brake deceleration is lower than A_NVP12(k)      |
| M_NVKVINT(k,m) |   7 | Only if Q_NVKVINTSET(k) = 1 Valid between V_NVKVINT(k,m) and V_NVKVINT(k,m+1) Gives the correction factor if maximum emergency brake deceleration is higher than A_NVP23(k) |
| L_NVKRINT      |   5 | = 0m                                                                                                                                                                        |
| M_NVKRINT      |   5 | Valid between L_NVKRINT and L_NVKRINT(1)                                                                                                                                    |
| N_ITER         |   5 |                                                                                                                                                                             |
| L_NVKRINT(l)   |   5 |                                                                                                                                                                             |
| M_NVKRINT(l)   |   5 | Valid between L_NVKRINT(l) and L_NVKRINT(l+1)                                                                                                                               |
| M_NVKTINT      |   5 |                                                                                                                                                                             |

6.5.1.5.23  Added section 7.4.2.37.5 (Packet Number 206: Track Condition) shall apply:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

Packet Number 206: Track Condition

| Description    | The packet gives details concerning the track ahead to support the driver when e.g. lower pantograph   | The packet gives details concerning the track ahead to support the driver when e.g. lower pantograph   | The packet gives details concerning the track ahead to support the driver when e.g. lower pantograph   |
|----------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Transmitted by | Any                                                                                                    | Any                                                                                                    | Any                                                                                                    |
| Content        | Variable                                                                                               | Length                                                                                                 | Comment                                                                                                |
|                | NID_PACKET                                                                                             | 8                                                                                                      |                                                                                                        |
|                | Q_DIR                                                                                                  | 2                                                                                                      |                                                                                                        |
|                | L_PACKET                                                                                               | 13                                                                                                     |                                                                                                        |
|                | Q_SCALE                                                                                                | 2                                                                                                      |                                                                                                        |
|                | Q_TRACKINIT                                                                                            | 1                                                                                                      |                                                                                                        |
|                | D_TRACKINIT                                                                                            | 15                                                                                                     | Only if Q_TRACKINIT = 1                                                                                |
|                | D_TRACKCOND                                                                                            | 15                                                                                                     | Only if Q_TRACKINIT = 0, D_TRACKCOND and the following variables follow                                |
|                | L_TRACKCOND                                                                                            | 15                                                                                                     |                                                                                                        |
|                | M_TRACKCONDBC                                                                                          | 4                                                                                                      |                                                                                                        |
|                | N_ITER                                                                                                 | 5                                                                                                      |                                                                                                        |
|                | D_TRACKCOND(k)                                                                                         | 15                                                                                                     |                                                                                                        |
|                | L_TRACKCOND(k)                                                                                         | 15                                                                                                     |                                                                                                        |
|                | M_TRACKCONDBC(k)                                                                                       | 4                                                                                                      |                                                                                                        |

6.5.1.5.24  Added section 7.4.2.37.6 (Packet Number 207: Route Suitability Data) shall apply:

## Packet Number 207: Route Suitability Data

| Description    | The packet gives the characteristics needed to enter a route.   | The packet gives the characteristics needed to enter a route.   | The packet gives the characteristics needed to enter a route.              |
|----------------|-----------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| Transmitted by | Any                                                             | Any                                                             | Any                                                                        |
| Content        | Variable                                                        | Length                                                          | Comment                                                                    |
| Content        | NID_PACKET                                                      | 8                                                               |                                                                            |
| Content        | Q_DIR                                                           | 2                                                               |                                                                            |
| Content        | L_PACKET                                                        | 13                                                              |                                                                            |
| Content        | Q_SCALE                                                         | 2                                                               |                                                                            |
| Content        | Q_TRACKINIT                                                     | 1                                                               |                                                                            |
| Content        | D_TRACKINIT                                                     | 15                                                              | Only if Q_TRACKINIT = 1                                                    |
| Content        | D_SUITABILITY                                                   | 15                                                              | Only If Q_TRACKINIT = 0, D_SUITABILITY and the following variables follows |
| Content        | Q_SUITABILITY                                                   | 2                                                               |                                                                            |
| Content        | M_LINEGAUGE                                                     | 8                                                               | If Q_SUITABILITY = loading gauge                                           |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| M_AXLELOADCAT    |   7 | If Q_SUITABILITY = Max axle load.                    |
|------------------|-----|------------------------------------------------------|
| M_VOLTAGE        |   4 | If Q_SUITABILITY = traction system                   |
| NID_CTRACTION    |  10 | If Q_SUITABILITY = traction system and M_VOLTAGE ≠ 0 |
| N_ITER           |   5 |                                                      |
| D_SUITABILITY(k) |  15 |                                                      |
| Q_SUITABILITY(k) |   2 |                                                      |
| M_LINEGAUGE(k)   |   8 | If Q_SUITABILITY = loading gauge                     |
| M_AXLELOADCAT(k) |   7 | If Q_SUITABILITY = Max axle load.                    |
| M_VOLTAGE(k)     |   4 | If Q_SUITABILITY = traction system                   |
| NID_CTRACTION(k) |  10 | If Q_SUITABILITY = traction system and M_VOLTAGE ≠ 0 |

6.5.1.5.25  Added  section  7.4.2.37.7  (Packet  Number  239:  Track  Condition  Change  of  traction system) shall apply:

Packet Number 239: Track Condition Change of traction system

| Description    | The packet gives information about change of the traction system.   | The packet gives information about change of the traction system.   | The packet gives information about change of the traction system.   |
|----------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Transmitted by | Any                                                                 | Any                                                                 | Any                                                                 |
| Content        | Variable                                                            | Length                                                              | Comment                                                             |
|                | NID_PACKET                                                          | 8                                                                   |                                                                     |
|                | Q_DIR                                                               | 2                                                                   |                                                                     |
|                | L_PACKET                                                            | 13                                                                  |                                                                     |
|                | Q_SCALE                                                             | 2                                                                   |                                                                     |
|                | D_TRACTION                                                          | 15                                                                  |                                                                     |
|                | M_VOLTAGE                                                           | 4                                                                   | Identity of the traction system NID_CTRACTION given only            |
|                | NID_CTRACTION                                                       | 10                                                                  | M_VOLTAGE ≠ 0                                                       |

6.5.1.5.25.1 Added Section 7.4.3.3.1 (Packet Number 3: On-board telephone numbers) shall apply:

Packet Number 3: On-board telephone numbers

| Description    | Telephone numbers associated to the on-board equipment   | Telephone numbers associated to the on-board equipment   | Telephone numbers associated to the on-board equipment   |
|----------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Transmitted to | RBC, RIU                                                 | RBC, RIU                                                 | RBC, RIU                                                 |
| Content        | Variable                                                 | Length                                                   | Comment                                                  |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| NID_PACKET    |   8 |
|---------------|-----|
| L_PACKET      |  13 |
| N_ITER        |   5 |
| NID_RADIO (k) |  64 |

6.5.1.5.25.2 Table 7.4.3.5 (Packet Number 11: Validated train data) shall be replaced with:

| Description    | Validated train data.   | Validated train data.   | Validated train data.             |
|----------------|-------------------------|-------------------------|-----------------------------------|
| Transmitted to | RBC                     | RBC                     | RBC                               |
| Content        | Variable                | Length                  | Comment                           |
| Content        | NID_PACKET              | 8                       |                                   |
| Content        | L_PACKET                | 13                      |                                   |
| Content        | NID_OPERATIONAL         | 32                      |                                   |
| Content        | NC_TRAIN                | 15                      |                                   |
| Content        | L_TRAIN                 | 12                      |                                   |
| Content        | V_MAXTRAIN              | 7                       |                                   |
| Content        | M_LOADINGGAUGE          | 8                       |                                   |
| Content        | M_AXLELOAD              | 7                       |                                   |
| Content        | M_AIRTIGHT              | 2                       |                                   |
| Content        | N_ITER                  | 5                       |                                   |
| Content        | M_TRACTION (k)          | 8                       | Type of traction system           |
| Content        | N_ITER                  | 5                       |                                   |
| Content        | NID_NTC (k)             | 8                       | Type of National System available |

## 6.5.1.5.26  Table 7.5.1.36 (D\_VALIDNV) shall be replaced with:

| Name               | Distance to start of validity of national values   | Distance to start of validity of national values   | Distance to start of validity of national values   |
|--------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| Description        |                                                    |                                                    |                                                    |
| Length of variable | Minimum Value                                      | Maximum Value                                      | Resolution/formula                                 |
| 15 bits            | 0 cm                                               | 327.670 km                                         | 10 cm, 1m or 10 m depends on Q_SCALE               |

6.5.1.5.27  Added section 7.5.1.62.2 (M\_AXLELOAD) shall apply:

## M\_AXLELOAD

| Name                    | Axle load     | Axle load            | Axle load            |
|-------------------------|---------------|----------------------|----------------------|
| Description             |               |                      |                      |
| Length of variable      | Minimum Value | Maximum Value        | Resolution/formula   |
| 7 bits                  | 0 t           | 40 t                 | 0.5 t                |
| Special/Reserved Values | 101 0001      | Spare                | Spare                |
|                         | …             | …                    | …                    |
|                         | 111 1101      | Spare                | Spare                |
|                         | 111 1110      | Axle load above 40 t | Axle load above 40 t |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

111 1111

Spare

## 6.5.1.5.27.1 Table 7.5.1.64 (M\_ERROR) shall be replaced with:

| Name                    | Identifier of the type of error   | Identifier of the type of error                                                                        | Identifier of the type of error                                                                        |
|-------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Description             |                                   |                                                                                                        |                                                                                                        |
| Length of variable      | Minimum Value                     | Maximum Value                                                                                          | Resolution/formula                                                                                     |
| 8 bits                  |                                   |                                                                                                        |                                                                                                        |
| Special/Reserved Values | 0                                 | Balise group: linking consistency error (ref. 3.16.2.3)                                                | Balise group: linking consistency error (ref. 3.16.2.3)                                                |
| Special/Reserved Values | 1                                 | Linked balise group: message consistency error (ref. 3.16.2.4.1/4)                                     | Linked balise group: message consistency error (ref. 3.16.2.4.1/4)                                     |
| Special/Reserved Values | 2                                 | Unlinked balise group: message consistency error (ref. 3.16.2.5)                                       | Unlinked balise group: message consistency error (ref. 3.16.2.5)                                       |
| Special/Reserved Values | 3                                 | Radio: message consistency error (ref. 3.16.3.1.1a,c)                                                  | Radio: message consistency error (ref. 3.16.3.1.1a,c)                                                  |
| Special/Reserved Values | 4                                 | Radio: sequence error (ref. 3.16.3.1.1b)                                                               | Radio: sequence error (ref. 3.16.3.1.1b)                                                               |
| Special/Reserved Values | 5                                 | Radio: safe radio connection error (ref. 3.16.3.4, to be sent when communication links re-established) | Radio: safe radio connection error (ref. 3.16.3.4, to be sent when communication links re-established) |
| Special/Reserved Values | 6                                 | Non safety critical failure                                                                            | Non safety critical failure                                                                            |
| Special/Reserved Values | 7                                 | Safety critical failure (ref 4.4.6.1.6 , 4.4.15.1.5)                                                   | Safety critical failure (ref 4.4.6.1.6 , 4.4.15.1.5)                                                   |
| Special/Reserved Values | 8-255                             | Spare                                                                                                  | Spare                                                                                                  |

## 6.5.1.5.27.2

Table 7.5.1.68 (M\_LOADINGGAUGE) shall be replaced with:

| Name                    | Loading gauge                                                    | Loading gauge                                                    | Loading gauge                                                    |
|-------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Description             | Defining the loading gauge profile of a train (refer to TSI RST) | Defining the loading gauge profile of a train (refer to TSI RST) | Defining the loading gauge profile of a train (refer to TSI RST) |
| Length of variable      | Minimum Value                                                    | Maximum Value                                                    | Resolution/formula                                               |
| 8 bits                  |                                                                  |                                                                  |                                                                  |
| Special/Reserved Values | 0                                                                | No loading gauge is defined for the train                        | No loading gauge is defined for the train                        |
| Special/Reserved Values | 1-255                                                            | Non interoperable value (this is not a spare value)              | Non interoperable value (this is not a spare value)              |

## 6.5.1.5.28  Table 7.5.1.70 (M\_MAMODE) shall be replaced with:

| Name                    | Required mode for a part of the MA   | Required mode for a part of the MA   | Required mode for a part of the MA   |
|-------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| Description             |                                      | Maximum Value                        | Length                               |
|                         |                                      |                                      | 2 bits                               |
| Special/Reserved Values | 00                                   | On Sight                             |                                      |
| Special/Reserved Values | 01                                   | Shunting                             |                                      |
| Special/Reserved Values | 10 - 11                              | Spare                                |                                      |

## 6.5.1.5.28.1 Table 7.5.1.72 (M\_MODE) shall be replaced with:

| Name                    | Onboard operating mode   | Onboard operating mode   | Onboard operating mode   |
|-------------------------|--------------------------|--------------------------|--------------------------|
| Description             |                          | Maximum Value            | Length                   |
|                         |                          |                          | 4 bits                   |
| Special/Reserved Values | 0                        | Full Supervision         |                          |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

1

On Sight

2

Staff Responsible

3

Shunting

4

Unfitted

5

Sleeping

6

Stand By

7

Trip

8

Post Trip

9

System Failure

10

Isolation

11

Non Leading

12

If reported level is NTC, National System; otherwise, Limited Supervision

13

National System

14

Reversing

15

Spare

## 6.5.1.5.29  Table 7.5.1.73 (M\_MODETEXTDISPLAY) shall be replaced with:

Name

Onboard operating mode for text display

Description

The text is displayed when entering / as long as in the defined mode

Length of variable

Minimum Value

Maximum Value

Resolution/formula

4 bits

Special/Reserved Values

0

Full Supervision

1

On Sight

2

Staff Responsible

3

Spare

4

Unfitted

5

Spare

6

Stand By

7

Trip

8

Post Trip

9

Spare

10

Spare

11

Spare

12

Spare

13

Spare

14

Reversing

15

The display of the text shall not be limited by the mode.

6.5.1.5.30  Table 7.5.1.76 (M\_POSITION) shall be replaced with:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Name                    | Track kilometre reference value                                                                | Track kilometre reference value                                                                | Track kilometre reference value                                                                |
|-------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Description             | The geographical position reporting function uses this variables content as a reference value. | The geographical position reporting function uses this variables content as a reference value. | The geographical position reporting function uses this variables content as a reference value. |
| Length of variable      | Minimum Value                                                                                  | Maximum Value                                                                                  | Resolution/formula                                                                             |
| 20 bits                 | 0 m                                                                                            | 1'048'574 m                                                                                    | 1 m                                                                                            |
| Special/Reserved Values | 1'048'575                                                                                      | No more geographical position calculation after this reference location                        | No more geographical position calculation after this reference location                        |

## 6.5.1.5.31  Table 7.5.1.77 (M\_TRACKCOND) shall be replaced with:

| Name                    | Type of track condition   | Type of track condition                                                                                 | Type of track condition                                                                                 |
|-------------------------|---------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Description             |                           |                                                                                                         |                                                                                                         |
| Length of variable      | Minimum Value             | Maximum Value                                                                                           | Resolution/formula                                                                                      |
| 4 bits                  |                           |                                                                                                         |                                                                                                         |
| Special/Reserved Values | 0000                      | Non stopping area - tunnel. Initial state: stopping permitted (no tunnel)                               | Non stopping area - tunnel. Initial state: stopping permitted (no tunnel)                               |
| Special/Reserved Values | 0001                      | Non stopping area - bridge. Initial state: stopping permitted (no bridge)                               | Non stopping area - bridge. Initial state: stopping permitted (no bridge)                               |
| Special/Reserved Values | 0010                      | Non stopping area - other reasons. Initial state: stopping permitted                                    | Non stopping area - other reasons. Initial state: stopping permitted                                    |
| Special/Reserved Values | 0011                      | Powerless section - lower pantograph. Initial state: not powerless section                              | Powerless section - lower pantograph. Initial state: not powerless section                              |
| Special/Reserved Values | 0100                      | Radio hole (stop supervising T_NVCONTACT). Initial state: supervise T_NVCONTACT                         | Radio hole (stop supervising T_NVCONTACT). Initial state: supervise T_NVCONTACT                         |
| Special/Reserved Values | 0101                      | Air tightness. Initial state: no request for air tightness                                              | Air tightness. Initial state: no request for air tightness                                              |
| Special/Reserved Values | 0110                      | Switch off regenerative brake. Initial state: regenerative brake on                                     | Switch off regenerative brake. Initial state: regenerative brake on                                     |
| Special/Reserved Values | 0111                      | Switch off eddy current brake for service brake. Initial state: eddy current brake for service brake on | Switch off eddy current brake for service brake. Initial state: eddy current brake for service brake on |
| Special/Reserved Values | 1000                      | Switch off magnetic shoe brake. Initial state: magnetic shoe brake on                                   | Switch off magnetic shoe brake. Initial state: magnetic shoe brake on                                   |
| Special/Reserved Values | 1001                      | Powerless section - switch off the main power switch. Initial state: not powerless section              | Powerless section - switch off the main power switch. Initial state: not powerless section              |
| Special/Reserved Values | 1010 -1111                | Spare                                                                                                   | Spare                                                                                                   |

## 6.5.1.5.32  Added section 7.5.1.77.1 (M\_TRACKCONDBC) shall apply:

## M\_TRACKCONDBC

| Name                    | Type of track condition   | Type of track condition                                                         | Type of track condition                                                         |
|-------------------------|---------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Description             |                           |                                                                                 |                                                                                 |
| Length of variable      | Minimum Value             | Maximum Value                                                                   | Resolution/formula                                                              |
| 4 bits                  |                           |                                                                                 |                                                                                 |
| Special/Reserved Values | 0000                      | Non stopping area. Initial state: stopping permitted                            | Non stopping area. Initial state: stopping permitted                            |
| Special/Reserved Values | 0001                      | Tunnel stopping area. Initial state: no tunnel stopping area                    | Tunnel stopping area. Initial state: no tunnel stopping area                    |
| Special/Reserved Values | 0010                      | Sound horn. Initial state: no request for sound horn                            | Sound horn. Initial state: no request for sound horn                            |
| Special/Reserved Values | 0011                      | Powerless section - lower pantograph. Initial state: not powerless section      | Powerless section - lower pantograph. Initial state: not powerless section      |
| Special/Reserved Values | 0100                      | Radio hole (stop supervising T_NVCONTACT). Initial state: supervise T_NVCONTACT | Radio hole (stop supervising T_NVCONTACT). Initial state: supervise T_NVCONTACT |
| Special/Reserved Values | 0101                      | Air tightness. Initial state: no request for air tightness                      | Air tightness. Initial state: no request for air tightness                      |
| Special/Reserved Values | 0110                      | Switch off regenerative brake. Initial state: regenerative brake on             | Switch off regenerative brake. Initial state: regenerative brake on             |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 0111       | Switch off eddy current brake for service brake. Initial state: eddy current brake for service brake on     |
|------------|-------------------------------------------------------------------------------------------------------------|
| 1000       | Switch off magnetic shoe brake. Initial state: magnetic shoe brake on                                       |
| 1001       | Powerless section - switch off the main power switch. Initial state: not powerless section                  |
| 1010       | Switch off eddy current brake for emergency brake. Initial state: eddy current brake for emergency brake on |
| 1011 -1111 | Spare                                                                                                       |

## 6.5.1.5.33  Added section 7.5.1.77.1 (M\_TRACTION) shall apply:

## M\_TRACTION

| Name                    | Traction system                                                                                             | Traction system                                                                                             | Traction system                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Description             | It indicates the traction system installed on a specific line or respectively that can be used by an engine | It indicates the traction system installed on a specific line or respectively that can be used by an engine | It indicates the traction system installed on a specific line or respectively that can be used by an engine |
| Length of variable      | Minimum Value                                                                                               | Maximum Value                                                                                               | Resolution/formula                                                                                          |
| 8 bits                  |                                                                                                             |                                                                                                             |                                                                                                             |
| Special/Reserved Values | 0                                                                                                           | Line not fitted with any traction system                                                                    | Line not fitted with any traction system                                                                    |
|                         | 1                                                                                                           | 3 kV DC, Italy                                                                                              | 3 kV DC, Italy                                                                                              |
|                         | 2                                                                                                           | 25 kV AC 50 Hz, Conventional lines France                                                                   | 25 kV AC 50 Hz, Conventional lines France                                                                   |
|                         | 3                                                                                                           | 25 kV AC 50 Hz, High speed lines France                                                                     | 25 kV AC 50 Hz, High speed lines France                                                                     |
|                         | 4                                                                                                           | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 5                                                                                                           | 1.5 kV DC, France                                                                                           | 1.5 kV DC, France                                                                                           |
|                         | 6                                                                                                           | 1.5 kV DC, Netherlands                                                                                      | 1.5 kV DC, Netherlands                                                                                      |
|                         | 7                                                                                                           | 25 kV AC 50 Hz, Conventional lines Netherlands                                                              | 25 kV AC 50 Hz, Conventional lines Netherlands                                                              |
|                         | 8                                                                                                           | 25 kV AC 50 Hz, High speed lines Netherlands                                                                | 25 kV AC 50 Hz, High speed lines Netherlands                                                                |
|                         | 9-10                                                                                                        | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 11                                                                                                          | 15kV AC 16 2/3 Hz, max. train current 600A Germany                                                          | 15kV AC 16 2/3 Hz, max. train current 600A Germany                                                          |
|                         | 12                                                                                                          | 15kV AC 16 2/3 Hz, max. train current 780A Germany                                                          | 15kV AC 16 2/3 Hz, max. train current 780A Germany                                                          |
|                         | 13                                                                                                          | 15kV AC 16 2/3 Hz, max. train current 900A Germany                                                          | 15kV AC 16 2/3 Hz, max. train current 900A Germany                                                          |
|                         | 14                                                                                                          | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 15                                                                                                          | 15kV AC 16 2/3 Hz, max. train current 1500A Germany                                                         | 15kV AC 16 2/3 Hz, max. train current 1500A Germany                                                         |
|                         | 16-25                                                                                                       | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 26                                                                                                          | 25 kV AC 50 Hz, Italy                                                                                       | 25 kV AC 50 Hz, Italy                                                                                       |
|                         | 27-30                                                                                                       | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 31                                                                                                          | 25 kV AC 50 Hz, 1600mm, High speed lines Spain                                                              | 25 kV AC 50 Hz, 1600mm, High speed lines Spain                                                              |
|                         | 32                                                                                                          | 3 kV DC, Conventional lines 220 km/h Spain                                                                  | 3 kV DC, Conventional lines 220 km/h Spain                                                                  |
|                         | 33                                                                                                          | 3 kV DC, Conventional lines160 km/h Spain                                                                   | 3 kV DC, Conventional lines160 km/h Spain                                                                   |
|                         | 34                                                                                                          | 25 kV AC 50 Hz, 1600mm/1950mm, High speed lines Spain                                                       | 25 kV AC 50 Hz, 1600mm/1950mm, High speed lines Spain                                                       |
|                         | 35-40                                                                                                       | Non interoperable value (this is not a spare value)                                                         | Non interoperable value (this is not a spare value)                                                         |
|                         | 41                                                                                                          | 15 kV AC 16 2/3 Hz, 1320mm/1450 mm, Switzerland                                                             | 15 kV AC 16 2/3 Hz, 1320mm/1450 mm, Switzerland                                                             |
|                         | 42                                                                                                          | 15 kV AC 16 2/3 Hz, 1450 mm/1600 mm, Switzerland                                                            | 15 kV AC 16 2/3 Hz, 1450 mm/1600 mm, Switzerland                                                            |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 43     | 15 kV AC 16 2/3 Hz, 1950 mm, Switzerland                       |
|--------|----------------------------------------------------------------|
| 44     | 15 kV AC 16 2/3 Hz, 1320 mm/1450 mm/1600 mm, Switzerland       |
| 45     | 15 kV AC 16 2/3 Hz, 1450 mm/1600mm/1950 mm, Switzerland        |
| 46     | 15 kV AC 16 2/3 Hz, 1320 mm/1450mm/1600mm/1950 mm, Switzerland |
| 47-255 | Non interoperable value (this is not a spare value)            |

## 6.5.1.5.34  Table 7.5.1.83 (NC\_DIFF) shall be replaced with:

| Name                    | Specific SSP category                                                                                                                                                                                                                                                                                                                                                                                         | Specific SSP category                                                                                                                                                                                                                                                                                                                                                                                         | Specific SSP category                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | It is the specific SSP category for which a differential value for the static line speed exists. Used together with V_DIFF to permit trains belonging to the corresponding international train category to go faster or lower than the 'international basic static speed' given by V_STATIC. Value 0 of NC_DIFF corresponds to the LSB of NC_TRAIN, value 14 of NC_DIFF to MSB (15-bit variable) of NC_TRAIN. | It is the specific SSP category for which a differential value for the static line speed exists. Used together with V_DIFF to permit trains belonging to the corresponding international train category to go faster or lower than the 'international basic static speed' given by V_STATIC. Value 0 of NC_DIFF corresponds to the LSB of NC_TRAIN, value 14 of NC_DIFF to MSB (15-bit variable) of NC_TRAIN. | It is the specific SSP category for which a differential value for the static line speed exists. Used together with V_DIFF to permit trains belonging to the corresponding international train category to go faster or lower than the 'international basic static speed' given by V_STATIC. Value 0 of NC_DIFF corresponds to the LSB of NC_TRAIN, value 14 of NC_DIFF to MSB (15-bit variable) of NC_TRAIN. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                                                                                                                                                                 | Maximum Value                                                                                                                                                                                                                                                                                                                                                                                                 | Resolution/formula                                                                                                                                                                                                                                                                                                                                                                                            |
| 4 bits                  | 0                                                                                                                                                                                                                                                                                                                                                                                                             | 15                                                                                                                                                                                                                                                                                                                                                                                                            | Numbers                                                                                                                                                                                                                                                                                                                                                                                                       |
| Special/Reserved Values | 0                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 275 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 275 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 1                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 80 mm                                                                                                                                                                                                                                                                                                                                                              | Specific SSP applicable to Cant Deficiency 80 mm                                                                                                                                                                                                                                                                                                                                                              |
| Special/Reserved Values | 2                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 100 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 100 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 3                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 130 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 130 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 4                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 150 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 150 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 5                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 165 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 165 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 6                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 180 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 180 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 7                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 225 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 225 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 8                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 300 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 300 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 9                                                                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Freight train braked in 'P' position                                                                                                                                                                                                                                                                                                                                               | Specific SSP applicable to Freight train braked in 'P' position                                                                                                                                                                                                                                                                                                                                               |
| Special/Reserved Values | 10                                                                                                                                                                                                                                                                                                                                                                                                            | Specific SSP applicable to Freight train braked in 'G' position                                                                                                                                                                                                                                                                                                                                               | Specific SSP applicable to Freight train braked in 'G' position                                                                                                                                                                                                                                                                                                                                               |
| Special/Reserved Values | 11                                                                                                                                                                                                                                                                                                                                                                                                            | Specific SSP applicable to Passenger train                                                                                                                                                                                                                                                                                                                                                                    | Specific SSP applicable to Passenger train                                                                                                                                                                                                                                                                                                                                                                    |
| Special/Reserved Values | 12                                                                                                                                                                                                                                                                                                                                                                                                            | Specific SSP applicable to Cant Deficiency 245 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 245 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 13                                                                                                                                                                                                                                                                                                                                                                                                            | Specific SSP applicable to Cant Deficiency 210 mm                                                                                                                                                                                                                                                                                                                                                             | Specific SSP applicable to Cant Deficiency 210 mm                                                                                                                                                                                                                                                                                                                                                             |
| Special/Reserved Values | 14-15                                                                                                                                                                                                                                                                                                                                                                                                         | Spare                                                                                                                                                                                                                                                                                                                                                                                                         | Spare                                                                                                                                                                                                                                                                                                                                                                                                         |

## 6.5.1.5.34.1 Table 7.5.1.84 (NC\_TRAIN) shall be replaced with:

Name

International Train Category.

Description

Length of variable

15 bits

Train category to which the train belongs.

Thanks to NC\_TRAIN, the train knows the 'Specific' SSP category it must consider.

By receiving a list of static speed profile, thanks to NC\_DIFF, the train can select the SSP it must obey.

Each bit represents one category.

A train can belong to various categories.

Minimum Value

Maximum Value

Resolution/formula

Bitset

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Special/Reserved Values   | 000 0000 0000 0000   | Train does not belong to any of the 'International' Train Category   |
|---------------------------|----------------------|----------------------------------------------------------------------|
| Special/Reserved Values   | xxx xxxx xxxx xxx1   | Cant Deficiency 275 mm                                               |
| Special/Reserved Values   | xxx xxxx xxxx xx1x   | Cant Deficiency 80 mm                                                |
| Special/Reserved Values   | xxx xxxx xxxx x1xx   | Cant Deficiency 100 mm                                               |
| Special/Reserved Values   | xxx xxxx xxx 1xxx    | Cant Deficiency 130 mm                                               |
| Special/Reserved Values   | xxx xxxx xxx1 xxxx   | Cant Deficiency 150 mm                                               |
| Special/Reserved Values   | xxx xxxx xx1x xxxx   | Cant Deficiency 165 mm                                               |
| Special/Reserved Values   | xxx xxxx x1xx xxxx   | Cant Deficiency 180 mm                                               |
| Special/Reserved Values   | xxx xxxx 1xxx xxxx   | Cant Deficiency 225 mm                                               |
| Special/Reserved Values   | xxx xxx1 xxxx xxxx   | Cant Deficiency 300 mm                                               |
| Special/Reserved Values   | xxx xx1x xxxx xxxx   | Freight train braked in 'P' position                                 |
| Special/Reserved Values   | xxx x1xx xxxx xxxx   | Freight train braked in 'G' position                                 |
| Special/Reserved Values   | xxx 1xxx xxxx xxxx   | Passenger train                                                      |
| Special/Reserved Values   | xx1 xxxx xxxx xxxx   | Cant Deficiency 245 mm                                               |
| Special/Reserved Values   | x1x xxxx xxxx xxxx   | Cant Deficiency 210 mm                                               |
| Special/Reserved Values   | 1xx xxxx xxxx xxxx   | Spare                                                                |

## 6.5.1.5.34.2 Table 7.5.1.92 (NID\_OPERATIONAL) shall be replaced with:

| Name                    | Train Running Number                          | Train Running Number                                                         | Train Running Number                                                         |
|-------------------------|-----------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Description             | This is the operational train running number. | This is the operational train running number.                                | This is the operational train running number.                                |
| Length of variable      | Minimum Value                                 | Maximum Value                                                                | Resolution/formula                                                           |
| 32 bits                 | 0                                             | 9999 9999                                                                    | Binary Coded Decimal                                                         |
| Special/Reserved Values | For each digit ;                              |                                                                              |                                                                              |
| Special/Reserved Values | Values A - E                                  | Spare                                                                        |                                                                              |
| Special/Reserved Values | F                                             | Use value F for digit to indicate no digit (if number shorter than 8 digits) | Use value F for digit to indicate no digit (if number shorter than 8 digits) |
| Special/Reserved Values | FFFF FFFF                                     | Unknown                                                                      |                                                                              |

## 6.5.1.5.34.3 Table 7.5.1.107 (Q\_EMERGENCYSTOP) shall be replaced with:

| Name                    | Qualifier for emergency stop acknowledgement                                                                                                               | Qualifier for emergency stop acknowledgement                                                                                                               | Qualifier for emergency stop acknowledgement                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Qualifier to indicate whether the train has accepted or not a conditional emergency stop. For an unconditional emergency stop, it is set to 'not relevant' | Qualifier to indicate whether the train has accepted or not a conditional emergency stop. For an unconditional emergency stop, it is set to 'not relevant' | Qualifier to indicate whether the train has accepted or not a conditional emergency stop. For an unconditional emergency stop, it is set to 'not relevant' |
| Length of variable      | Minimum Value                                                                                                                                              | Maximum Value                                                                                                                                              | Resolution/formula                                                                                                                                         |
| 2 bits                  |                                                                                                                                                            |                                                                                                                                                            |                                                                                                                                                            |
| Special/Reserved Values | 0                                                                                                                                                          | Conditional Emergency Stop accepted                                                                                                                        | Conditional Emergency Stop accepted                                                                                                                        |
| Special/Reserved Values | 1                                                                                                                                                          | Conditional Emergency Stop rejected                                                                                                                        | Conditional Emergency Stop rejected                                                                                                                        |
| Special/Reserved Values | 2                                                                                                                                                          | Not Relevant (Unconditional Emergency Stop)                                                                                                                | Not Relevant (Unconditional Emergency Stop)                                                                                                                |
| Special/Reserved Values | 3                                                                                                                                                          | Spare                                                                                                                                                      | Spare                                                                                                                                                      |

## 6.5.1.5.35  Table 7.5.1.138 (Q\_TEXTCONFIRM) shall be replaced with:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

Description

Length of variable

Minimum Value

Maximum Value

Resolution/formula

2 bits

Special/Reserved Values

00

No confirmation required

01

Continue display until confirmed

10

Apply service brake if not confirmed when end conditions reached

11

Spare

## 6.5.1.5.35.1 Added section 7.5.1.140.1 (Q\_TRACKDEL) shall apply:

Name

Track description deleted.

Description

Qualifier to indicate whether the onboard has deleted (for any reason) track description or not.

Length of variable

Minimum Value

Maximum Value

Resolution/formula

1 bit

Special/Reserved Values

0

No track description deleted

1

Track description deleted

6.5.1.5.36  Note: the packets listed above, which are not allowed for use in balise telegrams/loop messages marked with system version number X = 1 or in messages from RBC/RIU operating  with  system  version  number  X  =  1,  may  contain  variables  that  have  been introduced in the system version number X = 2. These variables are not mentioned in this  section,  since  their  use  is  implicitly  forbidden  by  the  fact  that  the  packets  using them are not allowed.

## 6.5.1.6 Exceptions to chapter 8

6.5.1.6.1 Clause 8.4.1.4.5 shall not apply.

6.5.1.6.2 Clause  8.4.1.4.8  shall  be  replaced  with  'Exception  8:  A  message  transmitted  by  a balise group can contain several packets 200 (Virtual Balise Cover marker).'

6.5.1.6.3 The table under clause 8.4.2.1 shall be replaced with:

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| General Format of Balise Telegram   | General Format of Balise Telegram   | General Format of Balise Telegram   |                                                                                                                                  |
|-------------------------------------|-------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Field No.                           | VARIABLE                            | Length ( bits)                      | Remarks                                                                                                                          |
| 1                                   | Q_UPDOWN                            | 1                                   | Defines the direction of the information: Down-link telegram (train to track) (0) Up-link telegram (track to train) (1)          |
| 2                                   | M_VERSION                           | 7                                   | Version of the ERTMS/ETCS system.                                                                                                |
| 3                                   | Q_MEDIA                             | 1                                   | Defines the type of media: Balise (0)                                                                                            |
| 4                                   | N_PIG                               | 3                                   | Position in the group. Defines the position of the balise in the balise group.                                                   |
| 5                                   | N_TOTAL                             | 3                                   | Total number of balises in the balise group                                                                                      |
| 6                                   | M_DUP                               | 2                                   | Used to indicate whether the information of the balise is a duplicate of the balise before or after this one.                    |
| 7                                   | M_MCOUNT                            | 8                                   | Message counter (M_MCOUNT) - 8 bits. To enable detection of a change of balise group message during passage of the balise group. |
| 8                                   | NID_C                               | 10                                  | Country or region.                                                                                                               |
| 9                                   | NID_BG                              | 14                                  | Identity of the balise group.                                                                                                    |
| 10                                  | Q_LINK                              | 1                                   | Marks the balise group as linked (Q_LINK = 1) or unlinked (Q_LINK = 0)                                                           |
|                                     | Packet 200 (optional)               | 29                                  | Virtual Balise Cover marker                                                                                                      |
|                                     | Information                         | Variable                            | This information is composed according to the rules applicable for packets.                                                      |
|                                     | Packet 255                          | 8                                   | Finishing flag of the telegram                                                                                                   |

6.5.1.6.4 Clause 8.4.2.3 shall be replaced with 'When used, the packet 200 shall be transmitted as the first packet of the telegram (i.e. it is appended to the header).'

- 6.5.1.6.5 The table under clause 8.4.4.4.1 shall be replaced with:

| Track to Train message             |   Mess. ID | Optional packets                                                           |
|------------------------------------|------------|----------------------------------------------------------------------------|
| SR Authorisation                   |          2 | 63                                                                         |
| Movement Authority                 |          3 | 21, 27, 49, 80, plus common optional packets                               |
| Request To Shorten MA              |          9 | 80                                                                         |
| General Message                    |         24 | From RBC: 21, 27, plus common optional packets From RIU: 45, 254           |
| SH authorised                      |         28 | 49, plus common optional packets                                           |
| MA with Shifted Location Reference |         33 | 21, 27, 80, plus common optional packets                                   |
| Infill MA                          |         37 | 5, 21, 27, 39, 41, 44, 51, 65, 66, 68, 70, 71, 80, 138, 139, 206, 207, 239 |

6.5.1.6.6 The table under clause 8.4.4.4.1.1 shall be replaced with:

## Common optional packets

3, 5, 39, 51, 41, 42, 44, 45, 57, 58, 65, 66, 68, 70, 71, 72, 79, 131, 138, 139, 140, 203, 206, 207, 239

6.5.1.6.6.1  Clause 8.4.4.4.2 shall be replaced with: 'The train to track message 136 (Train Position Report) and 157 (SoM Position Report) may optionally include the following packets:

- a) Packet 4 (Error Reporting),
- b) Packet 44 (Data used by applications outside the ERTMS/ETCS system).'

## 6.5.1.6.6.2  Table 8.5.2 shall be replaced with:

|   Mes. Id. | Message Name                           | Type   | Invariant   | Transmitted to   |
|------------|----------------------------------------|--------|-------------|------------------|
|        129 | Validated Train Data                   | N      | No          | RBC              |
|        130 | Request for Shunting                   | N      | No          | RBC              |
|        132 | MA Request                             | N      | No          | RBC              |
|        136 | Train Position Report                  | N      | No          | RBC, RIU         |
|        137 | Request to shorten MA is granted       | N      | No          | RBC              |
|        138 | Request to shorten MA is rejected      | N      | No          | RBC              |
|        146 | Acknowledgement                        | N      | No          | RBC, RIU         |
|        147 | Acknowledgement of Emergency Stop      | N      | No          | RBC              |
|        149 | Track Ahead Free Granted               | N      | No          | RBC              |
|        150 | End of Mission                         | N      | No          | RBC              |
|        153 | Radio infill request                   | N      | No          | RIU              |
|        154 | No compatible version supported        | N      | Yes         | RBC, RIU         |
|        155 | Initiation of a communication session  | N      | Yes         | RBC, RIU         |
|        156 | Termination of a communication session | N      | Yes         | RBC, RIU         |
|        157 | SoM Position Report                    | N      | No          | RBC              |
|        159 | Session Established                    | N      | No          | RBC, RIU         |

## 6.5.1.6.6.3  Table 8.6.3 (Message 132: MA Request) shall be replaced with:

<!-- image -->

|   Field No. | VARIABLE/ PACKET   |
|-------------|--------------------|
|           1 | NID_MESSAGE        |
|           2 | L_MESSAGE          |
|           3 | T_TRAIN            |
|           4 | NID_ENGINE         |
|           5 | Q_TRACKDEL         |
|           6 | Packet 0 or 1      |
|           7 | Optional packets   |

Remarks

6.5.1.6.6.4  Section 8.6.16 (Message 158: Text Message Acknowledged by Driver) shall not apply.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.1.6.6.5  Table 8.6.17 (Message 159: Session established) shall be replaced with:

<!-- image -->

| Field   | VARIABLE/ PACKET   |
|---------|--------------------|
| No. 1   | NID_MESSAGE        |
| 2       | L_MESSAGE          |
| 3       | T_TRAIN            |
| 4       | NID_ENGINE         |
| 5       | Packet 3           |

Remarks

## 6.5.1.6.7 Table 8.7.6 (Message 15: Conditional Emergency Stop) shall be replaced with:

| Field   | VARIABLE        |
|---------|-----------------|
| No.     |                 |
| 1       | NID_MESSAGE     |
| 2       | L_MESSAGE       |
| 3       | T_TRAIN         |
| 4       | M_ACK           |
| 5       | NID_LRBG        |
| 6       | NID_EM          |
| 7       | Q_SCALE         |
| 8       | Q_DIR           |
| 9       | D_EMERGENCYSTOP |

Remarks

Identification Number of the Emergency Stop Message.

Distance between LRBG and the position reference to the emergency stop.

6.5.1.6.8 Table 8.7.14 (Message 34: Track Ahead Free Request) shall be replaced with:

Remarks

| Field   | VARIABLE     |
|---------|--------------|
| No.     |              |
| 1       | NID_MESSAGE  |
| 2       | L_MESSAGE    |
| 3       | T_TRAIN      |
| 4       | M_ACK        |
| 5       | NID_LRBG     |
| 6       | Q_SCALE      |
| 7       | Q_DIR        |
| 8       | D_TAFDISPLAY |
| 9       | L_TAFDISPLAY |

6.5.1.6.9 Intentionally deleted.

6.5.1.6.10  Note: Packets or variables that have been introduced in the system version number X = 2, which cannot be contained within messages transmitted to an RBC operating with system version number X = 1, are not mentioned in the section 6.5.1.5.

## 6.5.1.7 Additional requirements

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 6.5.1.7.1 Any balise telegram, which includes the packet 2, the packet 6, the packet 135, the packet  145,  the  packet  200,  the  packet  203,  the  packet  206,  the  packet  207  or  the packet 239, shall be marked with the system version number 1.1.
- 6.5.1.7.2 An RBC that uses the packet 203, the packet 206, the packet 207 or the packet 239 shall transmit a system version number equal to 1.1, when negotiating the establishment of the communication session.
- 6.5.1.7.3 Any message transmitted by loop, which includes the packet 206, the packet 207 or the packet 239, shall be marked with the system version number 1.1.
- 6.5.1.7.4 An RIU that uses the packet 206, the packet 207 or the packet 239 shall transmit a system  version  number  equal  to  1.1,  when  negotiating  the  establishment  of  the communication session.
- 6.5.1.7.5 A balise group or RBC message including the packet 203 shall also include the packet 3 (i.e. in a message, the packet 203 cannot be transmitted without the packet 3).
- 6.5.1.7.6 In  the  packet  70,  the  use  of  the  value  '00'  of  the  variable  Q\_SUITABILITY  shall  be forbidden.

## 6.5.2 Trackside areas operated with system version number X = 2

## 6.5.2.1 General

- 6.5.2.1.1 This  section  is  applicable  for  trackside  infrastructures  that  were  operated  with  the system version number X = 1, before the migration to the system version number X = 2.
- 6.5.2.1.1.1  This section is also applicable for trackside infrastructures with RBCs/RIUs certified to the system version number X.Y = 2.0 or for trackside infrastructures with RBCs/RIUs certified  to  the  system  version  number  X.Y  =  2.1  where  trains  are  operated  with  onboard equipment whose highest supported system version number X.Y is only 2.0.
- 6.5.2.1.2 Within a trackside infrastructure operated with the system version number X = 2, it shall be allowed to use the following values of M\_VERSION: 1.0, 1.1, 2.0 and 2.1

## 6.5.2.2 Exceptions to chapter 3, 4, 5

- 6.5.2.2.1 For  RBCs  certified  to  the  system  version  number  2.0  and  for  RBCs  certified  to  the system  version  number  2.1  handing  over  a  train  fitted  with  an  on-board  equipment whose  highest  supported  system  version  number  X.Y  is  only  2.0,  the  bullet  'The system versions supported by the on-board equipment' in clause 3.15.1.2.1 b) shall not apply.

## 6.5.2.3 Exceptions to chapter 7, 8

- 6.5.2.3.1 For the balise telegrams/loop messages marked with the system version number 1.0 or 1.1 and for messages transmitted by RIUs certified to the system version number 1.0 or 1.1, the exceptions listed in sections 6.5.1.5 and 6.5.1.6 shall apply by analogy.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

6.5.2.3.2 For  RBCs/RIUs  certified  to  the  system  version  number  2.0,  the  following  exceptions shall apply:

## 6.5.2.3.2.1  The table 7.4.1.2 shall be replaced with:

|   Packet Number | Packet Name                                              | Page N°   |
|-----------------|----------------------------------------------------------|-----------|
|               0 | Position Report                                          |           |
|               1 | Position Report based on two balise groups               |           |
|               3 | On-board telephone numbers                               |           |
|               4 | Error Reporting                                          |           |
|               5 | Train running number                                     |           |
|               9 | Level 2/3 transition information                         |           |
|              11 | Validated train data                                     |           |
|              44 | Data used by applications outside the ERTMS/ETCS system. |           |

6.5.2.3.2.2  The clauses 6.5.1.5.25.1 and 6.5.1.6.6.5 shall apply.

6.5.2.3.2.3  Note:  Packets  or  variables  that  have  been  introduced  in  the  system  version  number X.Y  =  2.1,  which  cannot  be  contained  within  messages  transmitted  to  an  RBC operating  with  system  version  number  X.Y  =  2.0,  are  not  mentioned  in  this  section 6.5.2.3.2.

- 6.5.2.3.3 For  RBCs/RIUs  certified  to  the  system  version  number  2.1,  the  following  exceptions shall apply:

## 6.5.2.3.3.1  The table 7.4.1.2 shall be replaced with:

|   Packet Number | Packet Name                                              | Page N°   |
|-----------------|----------------------------------------------------------|-----------|
|               0 | Position Report                                          |           |
|               1 | Position Report based on two balise groups               |           |
|               2 | On-board supported system versions                       |           |
|               3 | On-board telephone numbers {1}                           |           |
|               4 | Error Reporting                                          |           |
|               5 | Train running number                                     |           |
|               9 | Level 2/3 transition information                         |           |
|              11 | Validated train data                                     |           |
|              44 | Data used by applications outside the ERTMS/ETCS system. |           |

{1}Note: used by on-board equipment whose highest supported system version = 2.0.

6.5.2.3.3.2  The clause 6.5.1.5.25.1 shall apply.

- 6.5.2.3.3.3  The table 8.6.17 (Message 159: Session established) shall be replaced with:

<!-- image -->

Remarks

Chapter 6 : Management of older System Versions

4

NID\_ENGINE

5

Packet 2 or 3

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## ERA * UNISIG * EEIG ERTMS USERS GROUP

## 6.6 On-board requirements in relation to older system versions

## 6.6.1 Introduction

6.6.1.1 This section covers the following situations:

- a) Train is running on a trackside infrastructure operated with system version number X = 1
- b) Train is running on a trackside infrastructure operated with system version number X = 2, but still transmitting some balise/loop/RIU information related to system version number X = 1 (see section 6.5.2)
- c)  Train is running on a trackside infrastructure operated with system version number X =  2,  but  on-board  equipment  has  established  a  communication  session  with  a neighbouring RBC certified to system version number X = 1
- d) Train is running on a trackside infrastructure operated with system version number X = 1 or 2 and the on-board equipment has established a communication session with a RBC/RIU certified to system version number X.Y = 2.0

## 6.6.2 Specific requirements for on-board operating with system version number X = 1

## 6.6.2.1 Exceptions to chapter 3

6.6.2.1.1

Clause 3.12.3.4.7.2 shall be replaced with: 'If the driver acknowledges before the end condition is fulfilled, the on-board equipment shall consider the driver acknowledgement as always ending the text display, regardless of the end condition defined in 3.12.3.4.3.1'.

## 6.6.2.2 Exceptions to chapter 4

6.6.2.2.1 Clause 4.4.11.1.3 d) shall be replaced with: 'balise groups giving the order 'stop if in SR'. This order shall immediately trip the train.'

- 6.6.2.2.2 Condition [54] in table 4.6.3 shall be replaced with: '(reception of information 'stop if in Staff Responsible') AND (override is not active)'.

## 6.6.2.3 Exceptions to chapter 5

6.6.2.3.1 Void

## 6.6.2.4 Exceptions to chapter 7, 8

6.6.2.4.1 Void

## 6.6.3 Handling of air gap data related to system version number X = 1

## 6.6.3.1 General

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 6.6.3.1.1 For  information  received  from  trackside,  the  message  consistency  check  shall  be achieved  taking  into  account  the  exceptions  to  chapters  7  and  8,  as  described  in sections 6.5.1.5 and 6.5.1.6.
- 6.6.3.1.2 For information received from trackside, the ERTMS/ETCS on-board equipment shall use the translation tables defined here below, in order to use the information as if it had been elaborated in compliance with the current chapters 7 and 8.

## 6.6.3.2 Packets received from balise, loop, RIU, RBC

- 6.6.3.2.1 In the table below, the translation of information may depend on the on-board operated system version at the time the information is received and accepted on-board.
- 6.6.3.2.2 When a level transition or an RBC/RBC handover is announced, the information stored on-board  in  the  transition  buffer  shall  be  translated  according  to  system  version operated on-board at the time the information is released from the transition buffer (i.e. the system version operated by the trackside infrastructure, towards which the train is running).
- 6.6.3.2.3 Depending on the packet, the action can be:
- a) data is unchanged,
- b) data is rejected,
- c)  data is translated,
- d) not relevant

R = Rejected T = Translated

U = Unchanged

NR = Not relevant

| Received information   | Received information         | Action                               | Action                               |
|------------------------|------------------------------|--------------------------------------|--------------------------------------|
| Packet Number          | Packet Name                  | Operated system version number X = 1 | Operated system version number X = 2 |
| 2                      | System Version Order         | U                                    | U                                    |
| 3                      | National Values              | T [1a] [2]                           | T [1b] [2]                           |
| 5                      | Linking                      | U                                    | U                                    |
| 6                      | Virtual Balise Cover order   | U                                    | U                                    |
| 12                     | Level 1 Movement Authority   | U                                    | U                                    |
| 15                     | Level 2/3 Movement Authority | U                                    | U                                    |
| 16                     | Repositioning Information    | U                                    | U                                    |
| 21                     | Gradient Profile             | U                                    | U                                    |

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Received information   | Received information                                     | Action                               | Action                               |
|------------------------|----------------------------------------------------------|--------------------------------------|--------------------------------------|
| Packet Number          | Packet Name                                              | Operated system version number X = 1 | Operated system version number X = 2 |
| 27                     | International Static Speed Profile                       | U [3]                                | U [3]                                |
| 39                     | Track Condition Change of traction system                | T [13]                               | T [13]                               |
| 41                     | Level Transition Order                                   | U                                    | U                                    |
| 42                     | Session Management                                       | U                                    | U                                    |
| 44                     | Data used by applications outside the ERTMS/ETCS system. | U                                    | U                                    |
| 45                     | Radio Network registration                               | U                                    | U                                    |
| 46                     | Conditional Level Transition Order                       | U                                    | U                                    |
| 49                     | List of balises for SH Area                              | U                                    | U                                    |
| 51                     | Axle load Speed Profile                                  | T [4][5]                             | T [4][5]                             |
| 57                     | Movement Authority Request Parameters                    | U                                    | U                                    |
| 58                     | Position Report Parameters                               | U                                    | U                                    |
| 63                     | List of Balises in SR Authority                          | U                                    | U                                    |
| 65                     | Temporary Speed Restriction                              | U                                    | U                                    |
| 66                     | Temporary Speed Restriction Revocation                   | U                                    | U                                    |
| 67                     | Track Condition Big Metal Masses                         | U                                    | U                                    |
| 68                     | Track Condition                                          | U [8] [9]                            | U [8] [9]                            |
| 70                     | Route Suitability Data                                   | R [11] [12]                          | R [11] [12]                          |
| 71                     | Adhesion Factor                                          | U                                    | U                                    |
| 72                     | Packet for sending plain text messages                   | U [6]                                | U [6]                                |
| 76                     | Packet for sending fixed text messages                   | R                                    | R                                    |
| 79                     | Geographical Position Information                        | U [14]                               | U [14]                               |
| 80                     | Mode profile                                             | T [7]                                | T [7]                                |
| 90                     | Track Ahead Free up to level 2/3 transition location     | U                                    | U                                    |
| 131                    | RBC transition order                                     | U                                    | U                                    |
| 132                    | Danger for Shunting information                          | U                                    | U                                    |
| 133                    | Radio infill area information                            | U                                    | U                                    |
| 134                    | EOLM Packet                                              | U                                    | U                                    |
| 135                    | Stop Shunting on desk opening                            | U                                    | U                                    |
| 136                    | Infill location reference                                | U                                    | U                                    |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| Received information   | Received information                                    | Action                               | Action                               |
|------------------------|---------------------------------------------------------|--------------------------------------|--------------------------------------|
| Packet Number          | Packet Name                                             | Operated system version number X = 1 | Operated system version number X = 2 |
| 137                    | Stop if in Staff Responsible                            | U                                    | U                                    |
| 138                    | Reversing area information                              | U                                    | U                                    |
| 139                    | Reversing supervision information                       | U                                    | U                                    |
| 140                    | Train running number from RBC                           | T [10]                               | T [10]                               |
| 141                    | Default Gradient for Temporary Speed Restriction        | U                                    | U                                    |
| 145                    | Inhibition of balise group message consistency reaction | U                                    | U                                    |
| 200                    | Virtual Balise Cover marker                             | T [15]                               | T [15]                               |
| 203                    | National Values for braking curves                      | T [16]                               | T [16]                               |
| 206                    | Track Condition                                         | T [17]                               | T [17]                               |
| 207                    | Route Suitability Data                                  | T [18]                               | T [18]                               |
| 239                    | Track Condition Change of traction system               | T [19]                               | T [19]                               |
| 254                    | Default balise, loop or RIU information                 | U                                    | U                                    |

- [1a] The National Values Q\_NVLOCACC, V\_NVLIMSUPERV (introduced in system version number X = 2) shall be set to their respective default value
- [1b] The National Values Q\_NVLOCACC, V\_NVLIMSUPERV (introduced in system version number X = 2), if already stored on-board and applicable, shall not be affected by the content of the packet 3 (i.e. if these National Values were already applicable and 2 nd bullet of clause 3.18.2.5 is not applied, they shall remain applicable with their country identifier(s) previously stored).
- [2]  If  the  packet  203  is  not  received  in  the  same  message,  the  National  Values  for  braking  curves Q\_NVGUIPERM, Q\_NVSBFBPERM, Q\_NVINHSMICPERM, M\_NVAVADH, M\_NVEBCL, A\_NVP12, A\_NVP23,  V\_NVKVINT,  M\_NVKVINT,  L\_NVKRINT,  M\_NVKRINT,  M\_NVKTINT,  A\_NVMAXREDADH1, A\_NVMAXREDADH2, A\_NVMAXREDADH3 (introduced in  system  version  number  X.Y  =  1.1),  if  already stored  on-board  and  applicable,  shall  not  be  affected  by  the  content  of  the  packet  3  (i.e.  if  the  National Values for braking curves were already applicable and 2 nd bullet of clause 3.18.2.5 is not applied, they shall remain applicable with their country identifier(s) previously stored).
- [3]  Exception:  if  N\_ITER  (following  Q\_FRONT)  0,  the  variables  Q\_DIFF,  NC\_CDDIFF  (introduced  in system version number X = 2) and NC\_DIFF (as specified in system version number X = 2) shall be set according to the following table:

| Value received from X = 1 trackside   | Translated values on-board   | Translated values on-board   | Translated values on-board   |
|---------------------------------------|------------------------------|------------------------------|------------------------------|
| NC_DIFF                               | Q_DIFF                       | NC_CDDIFF                    | NC_DIFF                      |
| 0                                     | 0                            | 9                            | -                            |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   1 |   0 | 0   | -   |
|-----|-----|-----|-----|
|   2 |   0 | 1   | -   |
|   3 |   0 | 2   | -   |
|   4 |   0 | 3   | -   |
|   5 |   0 | 4   | -   |
|   6 |   0 | 5   | -   |
|   7 |   0 | 7   | -   |
|   8 |   0 | 10  | -   |
|   9 |   1 | -   | 0   |
|  10 |   1 | -   | 1   |
|  11 |   1 | -   | 2   |
|  12 |   0 | 8   | -   |
|  13 |   0 | 6   | -   |

[4] If Q\_TRACKINIT = 1, D\_TRACKINIT (introduced in system version number X = 2) shall be set to 0

- [5] The variable M\_AXLELOADCAT (introduced in system version number X = 2) shall be set according to the following table:
- [6] Exception: if Q\_TEXTCONFIRM  0, then Q\_CONFTEXTDISPLAY and Q\_TEXTREPORT (introduced in system version number X = 2) shall be set to 0
- [7] The variable Q\_MAMODE (introduced in system version number X = 2) shall be set to 1
- [8] Exception: If the packet 206 is not received in the same message and if M\_TRACKCOND = 1 or 2, then M\_TRACKCOND (modified in system version number X = 2) shall be set to 0
- [9] Exception: If the packet 206 is received in the same message, the ERTMS/ETCS on-board shall ignore the packet 68.

| Value received from X = 1 trackside                               | Translated value on-board   |
|-------------------------------------------------------------------|-----------------------------|
| M_AXLELOAD                                                        | M_AXLELOADCAT               |
| M_AXLELOAD ≤ 16 t                                                 | A                           |
| 16 t < M_AXLELOAD ≤ 17 t                                          | HS17                        |
| 17 t < M_AXLELOAD ≤ 18 t                                          | B1                          |
| 18 t < M_AXLELOAD ≤ 20 t                                          | C2                          |
| 20 t < M_AXLELOAD ≤ 22.5 t                                        | D2                          |
| 22.5 t < M_AXLELOAD ≤ 40 t or M_AXLELOAD = 'Axle load above 40 t' | E4                          |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- [10] Within the 8 digits of the variable NID\_OPERATIONAL (as specified in system version X = 1), any digit coded as "F" shall be rightmost shifted, in order to obtain a variable NID\_OPERATIONAL (as specified in system version X = 2) made of the significant digits leftmost adjusted followed by digits coded as "F".
- [11] Exception: If the packet 207 is not received in the same message and if Q\_TRACKINIT = 1, the packet shall not be rejected.
- [12] Exception: If the packet 207 is not received in the same message and if the value '10' of the variable Q\_SUITABILITY is used with M\_TRACTION equal to one of the values that are listed in the translation table [13], the variables M\_VOLTAGE and NID\_CTRACTION (introduced in system version X.Y = 1.1) shall be set according to the translation table [13]. The ERTMS/ETCS on-board shall ignore any other route suitability information not related to the traction system

[13] If the packet 239 is received in the same message or if M\_TRACTION is not equal to one of the values that are listed here below, the ERTMS/ETCS on-board shall ignore the packet 39. If the packet 239 is not received in the same message and if M\_TRACTION is equal to one of the values that are listed here below the variables M\_VOLTAGE and NID\_CTRACTION shall be set according to the following table:

| Value received from X = 1 trackside   | Translated values on-board   | Translated values on-board   |
|---------------------------------------|------------------------------|------------------------------|
| M_TRACTION                            | M_VOLTAGE                    | NID_CTRACTION                |
| 0                                     | 0                            | -                            |
| 1                                     | 3                            | 10                           |
| 2                                     | 1                            | 12                           |
| 3                                     | 1                            | 13                           |
| 5                                     | 4                            | 14                           |
| 6                                     | 4                            | 1                            |
| 7                                     | 1                            | 2                            |
| 8                                     | 1                            | 3                            |
| 11                                    | 2                            | 19                           |
| 12                                    | 2                            | 20                           |
| 13                                    | 2                            | 21                           |
| 15                                    | 2                            | 22                           |
| 26                                    | 1                            | 11                           |
| 31                                    | 1                            | 18                           |
| 32                                    | 3                            | 15                           |
| 33                                    | 3                            | 16                           |
| 34                                    | 1                            | 17                           |
| 41                                    | 2                            | 4                            |
| 42                                    | 2                            | 5                            |
| 43                                    | 2                            | 6                            |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   44 |   2 |   7 |
|------|-----|-----|
|   45 |   2 |   8 |
|   46 |   2 |   9 |

[14] Exception: if M\_POSITION = 1'048'575, then M\_POSITION (modified in system version number X = 2) shall be set to 16'777'215

- [15]  The  variable  NID\_PACKET shall be set to 0 and both the variables Q\_DIR and L\_PACKET shall be deleted
- [16] The National Values included in the packet 203 shall be appended to the packet 3 received in the same message, in order to form a single set of National Values, to which apply the distance to start of validity and the list of national area identifiers given in the packet 3.
- [17] The variable NID\_PACKET shall be set to 68.
- [18] The variable NID\_PACKET shall be set to 70
- [19] The variable NID\_PACKET shall be set to 39

## 6.6.3.3 Messages received from RBC/RIU

- 6.6.3.3.1 This section applies for the parts of radio messages,  excluding the packets themselves,  which  are  received  from  an  RBC/RIU  certified  to  the  system  version number X = 1.
- 6.6.3.3.2 Depending on the received message, the action can be:
- a) data is unchanged,
- b) data is rejected
- c)  data is translated,
- d) not relevant

R = Rejected

T = Translated

U = Unchanged

NR = Not relevant

|   Messag e Number | Message Name                       | Action   |
|-------------------|------------------------------------|----------|
|                 2 | SR Authorisation                   | U        |
|                 3 | Movement Authority                 | U        |
|                 6 | Recognition of exit from TRIP mode | U        |
|                 8 | Acknowledgement of Train Data      | U        |
|                 9 | Request to Shorten MA              | U        |
|                15 | Conditional Emergency Stop         | T [1]    |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   Messag e Number | Message Name                                              | Action   |
|-------------------|-----------------------------------------------------------|----------|
|                16 | Unconditional Emergency Stop                              | U        |
|                18 | Revocation of Emergency Stop                              | U        |
|                24 | General message                                           | U        |
|                27 | SH Refused                                                | U        |
|                28 | SH Authorised                                             | U        |
|                33 | MA with Shifted Location Reference                        | U        |
|                34 | Track Ahead Free Request                                  | T [1]    |
|                37 | Infill MA                                                 | U        |
|                40 | Train Rejected                                            | U [2]    |
|                32 | RBC/RIU system version                                    | U        |
|                39 | Acknowledgement of termination of a communication session | U        |
|                41 | Train Accepted                                            | U [2]    |
|                43 | SoM position report confirmed by RBC                      | U        |
|                45 | Assignment of coordinate system                           | U        |

- [1] Variable D\_REF (introduced in system version number X = 2) shall be set to 0
- [2] Exception: if the variable NID\_LRBG ≠ 16777215, it shall be set to 16777215, i.e. the message shall be considered as having been received with NID\_LRBG = 16777215.

Note: An RBC X=1 based on an older version of the specification may use a value different from 16777215 for NID\_LRBG in message 40 or 41.

## 6.6.3.4 Messages transmitted to RBC/RIU

- 6.6.3.4.1 This section applies for radio messages/packets, which are transmitted to an RBC or an RIU certified to the system version number X = 1.
- 6.6.3.4.1.1  Clause  3.5.3.7  d)  1 st bullet  shall  be  replaced  with:  'If  one  of  its  supported  system versions  is  compatible  with  the  one  sent  by  trackside,  it  shall  send  a  session established report, including its telephone numbers, to the trackside.'
- 6.6.3.4.1.2  Clause 3.12.3.5.2 shall not apply.
- 6.6.3.4.2 Clause 3.18.4.5.4 shall be replaced with: 'Only if valid Train Data is available: following any entry/modification of the train running number when a communication session is already  established  or  following  the  successful  establishment  of  a  communication session when valid train running number is already available, the ERTMS/ETCS onboard equipment shall send the Train Data to the RBC.

## ERA * UNISIG * EEIG ERTMS USERS GROUP

- 6.6.3.4.3 Clause 3.18.4.5.4.1 shall be replaced with: 'Exception: if the train running number has been received from the RBC, the Train Data shall not be sent back to the RBC by the ERTMS/ETCS on-board equipment.
- 6.6.3.4.4 The ERTMS/ETCS  on-board  equipment shall elaborate the information to be transmitted to the RBC/RIU certified to system version number X = 1, by applying the following  translation  table  to  the  corresponding  information  intended  for  an  RBC/RIU certified to the system version number X.Y = 2.1.
- 6.6.3.4.5 Depending on the transmitted message/packet, the action can be:
- a) data is unchanged,
- b) data is deleted (i.e. it is not sent to the receiver)
- c)  data is translated,
- d) not relevant (i.e. no corresponding requirement to trigger the sending is applicable)

D = Deleted

T = Translated

U = Unchanged

NR = Not relevant

| Mess nb pck nb   | Message name/packet name                   | Action   |
|------------------|--------------------------------------------|----------|
| XXX 0            | Position Report                            | U [1]    |
| XXX 1            | Position Report based on two balise groups | U [1]    |
| 159 2            | On-board supported system versions         | T[6]     |
| XXX 4            | Error Reporting                            | U [2]    |
| XXX 5            | Train Running Number                       | NR       |
| 132 9            | Level 2/3 transition information           | U        |
| 129 11           | Validated Train Data (packet)              | T [3]    |
| 129              | Validated Train Data (message)             | U        |
| 130              | Request for Shunting                       | U        |
| 132              | MA Request                                 | T [4]    |
| 136              | Train Position Report                      | U        |
| 137              | Request to shorten MA is granted           | U        |
| 138              | Request to shorten MA is rejected          | U        |
| 146              | Acknowledgement                            | U        |
| 147              | Acknowledgement of Emergency Stop          | T [5]    |
| 149              | Track Ahead Free Granted                   | U        |
| 150              | End of Mission                             | U        |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

|   Mess nb pck nb | Message name/packet name               | Action   |
|------------------|----------------------------------------|----------|
|              153 | Radio infill request                   | U        |
|              154 | No compatible version supported        | U        |
|              155 | Initiation of a communication session  | U        |
|              156 | Termination of a communication session | U        |
|              157 | SoM Position Report                    | U        |
|              158 | Text message acknowledged by driver    | NR       |
|              159 | Session Established                    | U        |

- [1] Exception: if M\_MODE (X=2) = 15 (PS), then M\_MODE (X=1) = 3 (SH)

Note: if M\_MODE (X=2) = 12 (LS), no translation is effected

[2] Exceptions: if M\_ERROR (X=2) = 6, then M\_ERROR (X=1) = 7; if M\_ERROR (X=2) = 7 or 8, then the packet shall be deleted

[3] the packet 11 shall be translated as follows:

| Description    | Validated train data.   | Validated train data.   | Validated train data.             |
|----------------|-------------------------|-------------------------|-----------------------------------|
| Transmitted to | RBC                     | RBC                     | RBC                               |
| Content        | Variable                | Length                  | Comment                           |
| Content        | NID_PACKET              | 8                       |                                   |
| Content        | L_PACKET                | 13                      |                                   |
| Content        | NID_OPERATIONAL         | 32                      | See translation [3a]              |
| Content        | NC_TRAIN                | 15                      | See translation [3b]              |
| Content        | L_TRAIN                 | 12                      |                                   |
| Content        | V_MAXTRAIN              | 7                       |                                   |
| Content        | M_LOADINGGAUGE          | 8                       | See translation [3c]              |
| Content        | M_AXLELOAD              | 7                       | See translation [3d]              |
| Content        | M_AIRTIGHT              | 2                       |                                   |
| Content        | N_ITER                  | 5                       | See translation [3e]              |
| Content        | N_ITER                  | 5                       |                                   |
| Content        | NID_NTC (k)             | 8                       | Type of National System available |

[3a] NID\_OPERATIONAL shall be set to the value stored on-board

[3b] NC\_TRAIN shall be set according to the following table:

| Value stored on- board   | Transmitted value to X=1 RBC   |
|--------------------------|--------------------------------|
| NC_CDTRAIN               | NC_TRAIN                       |

## ERA * UNISIG * EEIG ERTMS USERS GROUP

| 0                  | xxx xxxx xxxx xx1x   |
|--------------------|----------------------|
| 1                  | xxx xxxx xxxx x1xx   |
| 2                  | xxx xxxx xxxx 1xxx   |
| 3                  | xxx xxxx xxx1 xxxx   |
| 4                  | xxx xxxx xx1x xxxx   |
| 5                  | xxx xxxx x1xx xxxx   |
| 6                  | x1x xxxx xxxx xxxx   |
| 7                  | xxx xxxx 1xxx xxxx   |
| 8                  | xx1 xxxx xxxx xxxx   |
| 9                  | xxx xxxx xxxx xxx1   |
| 10                 | xxx xxx1 xxxx xxxx   |
| NC_TRAIN           |                      |
| 000 0000 0000 0000 | No bit is set to 1   |
| xxx xxxx xxxx xxx1 | xxx xx1x xxxx xxxx   |
| xxx xxxx xxxx xx1x | xxx x1xx xxxx xxxx   |
| xxx xxxx xxxx x1xx | xxx 1xxx xxxx xxxx   |
| Other values       | No bit is set to 1   |

[3c] M\_LOADINGGAUGE shall be set to 0

[3d] M\_AXLELOAD shall be set according to the following table:

| Value stored on- board   | Transmitted value to X=1 RBC   |
|--------------------------|--------------------------------|
| A                        | 16 t                           |
| HS17                     | 17 t                           |
| B1                       | 18 t                           |
| B2                       | 18 t                           |
| C2                       | 20 t                           |
| C3                       | 20 t                           |
| C4                       | 20 t                           |
| D2                       | 22,5 t                         |
| D3                       | 22,5 t                         |
| D4                       | 22,5 t                         |
| D4xL                     | 22,5 t                         |
| E4                       | 25 t                           |

Chapter 6 : Management of older System Versions

## ERA * UNISIG * EEIG ERTMS USERS GROUP

[3e] N\_ITER shall be set to 0

[4] Q\_MARQSTREASON shall be replaced with Q\_TRACKDEL (1 bit) as follows: if Q\_MARQSTREASON = x1xxx, Q\_TRACKDEL shall be set to 1, otherwise Q\_TRACKDEL shall be set to 0

[5] The variable Q\_EMERGENCYSTOP (modified in system version number X = 2) shall be set according to the following table:

| Value that would be transmitted to X=2 RBC   | Transmitted value to X=1 RBC   |
|----------------------------------------------|--------------------------------|
| Q_EMERGENCYSTOP                              | Q_EMERGENCYSTOP                |
| 0                                            | 0                              |
| 1                                            | 0                              |
| 2                                            | 2                              |
| 3                                            | 1                              |

[6] the packet 2 shall be replaced with the following packet numbered as 3:

| Description    | Telephone numbers associated to the onboard equipment   | Telephone numbers associated to the onboard equipment   | Telephone numbers associated to the onboard equipment   |
|----------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Transmitted to | RBC, RIU                                                | Length                                                  |                                                         |
|                | NID_PACKET                                              | 8                                                       | =3                                                      |
|                | L_PACKET                                                | 13                                                      |                                                         |
|                | N_ITER                                                  | 5                                                       |                                                         |
|                | NID_RADIO (k)                                           | 64                                                      |                                                         |

## 6.6.4 Handling of air gap data related to system version number X.Y = 2.0

## 6.6.4.1 Messages transmitted to RBC/RIU

6.6.4.1.1 This section applies for radio messages/packets, which are transmitted to an RBC or an RIU certified to the system version number X.Y = 2.0.

6.6.4.1.2 The clause 6.6.3.4.1.1 and the translation [6] referred to in clause 6.6.3.4.5 shall apply.
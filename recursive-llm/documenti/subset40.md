## 3. INTRODUCTION

## 3.1 References

- 3.1.1.1 The following documents are referenced in this document:
-  System Requirement Specification - SUBSET-026
-  Safety  Requirements  for  Technical  Interoperability  of  ETCS  in  Levels  1  &amp;  2  SUBSET-091
-  FFFIS for Eurobalise - SUBSET-036
-  FFFIS for Euroloop - SUBSET-044
-  Interface ´G´ Specification - SUBSET-100
-  Interface 'K' Specification - SUBSET-101
-  Technical Specification for the Interoperability of the Trans-European High Speed rail system, Rolling Stock subsystem, 2008/232/EC, dated 21/02/08
-  Technical Specification for the Interoperability of the Trans-European Conventional rail  system,  Rolling  Stock  subsystem  -  locomotives  and  passenger  rolling  stock, 2011/291/EU, dated 26/04/11
-  Brakes - Braking power, UIC Leaflet 544-1, 6th edition
-  Railway Applications - Braking - Wheel Slide Protection, EN 15595, dated 2009
-  Interfaces between Control-Command and Signalling trackside and other subsystems, ERA/ERTMS/033281
- 3.1.1.2 Intentionally deleted
- 3.1.1.3 Intentionally deleted

## 3.2 Aim and purpose for a subset of engineering rules

## 3.2.1 ERTMS/ETCS engineering rules

- 3.2.1.1 The  engineering  rules  are  system-related  limitations  for  installation  of  equipment, exchange  of  information,  on-board  configuration  data,  etc.  that  characterise  the implementation of ERTMS subsystems.
- 3.2.1.2 These engineering  rules  provide  additional  constraints  to  the  requirements  stated  in the SRS and other sub-level documents in order to ensure interoperability.

<!-- image -->

- 3.2.1.2.1 The Engineering Rules stated here are therefore complementary to the requirements stated in the SRS and subdocuments. References herein to other documents are not exhaustive, in particular to the SRS.
- 3.2.1.3 Intentionally deleted
- 3.2.1.4 The aim of these engineering rules is not to define the whole set of rules necessary to realise a project with ERTMS/ETCS.
- Additional rules, which are not defined in this document, may be needed, and may vary depending  on  the  project  constraints,  Clients  requirements  or  rules  and  Industry procedures.  However,  those  rules  must  not  preclude  the  use  of  any  equipment meeting the engineering rules stated here.
- 3.2.1.5 The engineering rules defined stated herein or referenced are mandatory; Engineering advice is not in the scope of this document

## 3.2.2 Transmission systems other than ERTMS/ETCS

- 3.2.2.1 Some constraints related to KER-compatible systems are described in appendix to this document.
- 3.2.2.2 Possible additional constraints related to transmission systems different from ERTMS (e.g. KER) must be defined within the relevant project.

## 3.3 Referencing balises and antennas

## 3.3.1 Referencing balises and balise groups

- 3.3.1.1 The  reference  location  of  a  balise  is  the  Balise  Reference  Marks,  which  are  visible signs on the surface of the balise.
- 3.3.1.2 Balise groups will be considered as a complete device limited by the reference location of its outer balises.
- 3.3.1.3 The reference location of a balise group is the reference location of its outer balise with N\_PIG variable = 0.
- 3.3.1.4 The «last switchable balise» of a balise group refers to the last encountered switchable balise with regards to the balise group crossing direction.
- 3.3.1.5 Distance between balise groups is by definition the distance between closest balises of the  two  groups  (i.e.  between  the  Balise  Reference  Mark  of  the  last  one  of  the  first group and the Balise Reference Mark of the first one of the second group).

<!-- image -->

-  Note: This convention should not be mixed up with the distance used in the linking information  (i.e.  between  the  Balise  Reference  Mark  of  the  balise  with  N\_PIG variable  =  0  of  the  first  group  and  the  Balise  Reference  Mark  of  the  balise  with N\_PIG variable = 0 of the second group); see following figure

<!-- image -->

## 3.3.2 Referencing antennas

- 3.3.2.1 The  reference  location  of  an  antenna  is  the  Antenna  Reference  Marks,  which  are visible signs on the surface of the antenna.

## 3.4 Intentionally deleted

<!-- image -->

## 4. RULES

## 4.1 Installation rules

## 4.1.1 Rules for balises

## 4.1.1.1 General installation rules for balises

| Rule          | Reminder: the rules of the references below must be respected.                                                                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036  Section 4.2.5: Cross-talk protection  Section 5.2 : Balise air gap interface  Section 5.6.2 : Installation requirements for balises  Section 5.6.3: Distance between balises  Section 5.7: Environmental Conditions |
| Justification | The rules of the reference above are required in order to guarantee interoperability from a transmission point of view.                                                                                                              |

## 4.1.1.2 Maximum distance between balises within a group - to determine that no further balise is expected within a group (potentially missing balise).

| Rule          | The maximum distance between two consecutive balises within the same group shall be 12 m from reference mark to reference mark.                                                                              |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                                                                              |
| Justification | The distance must be as short as possible in order to determine potential loss of balises as soon as possible, but must respect the longest minimum distance according to rule referenced in 4.1.1.1 herein. |

<!-- image -->

4.1.1.3 Maximum distance between any balise at a signal containing switched information and the stopping point - for level 1.

<!-- image -->

| Rule          | With regards to balises at a signal containing switched information any balise located in rear of the operational stopping location shall not be located further than 0.7m in rear of the operational stopping location.                                                                                                                                                                                                                                                                                |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036 section 5.2.2.5 (for the value 1.3 m)                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Justification | - A train that stops at the operational stopping point in rear of the signal showing stop should not be able to receive information contained in the balise group between the stopping point and the EOA - The rule refers to the antenna being mounted closest to the extremity of the engine where the reference mark of the antenna is 2m in rear of the extremity of the engine - For the earliest reception of a balise signal the 'side lobe zone' of the balises (= 1.3 m) is taken into account |
|               | interoperable constraints for not receiving info from balise @stopping position 1,3m EOA 2m Operational stopping point relative 1st balise of group 0,7m                                                                                                                                                                                                                                                                                                                                                |

<!-- image -->

## 4.1.1.4 Minimum distance between the balise group and the EOA/LOA.

| Rule          | The last encountered balise of the balise group giving an MA, giving an immediate level transition order, or giving a 'Stop if in SR', that is placed close to the EOA/LOA shall be a minimum distance of 1.3m plus the distance the train may run during the time Tn, calculated from the formulas in Subset-036, clause 4.2.9, in rear of the EOA/LOA. Note: for train speeds lower than 80 km/h, the time Tn always equals to 100ms. In Level 2/3 for the immediate level transition order, the maximum distance between the on-board antenna and the train front end (12.5m + max. distance first axle to front end) shall be added to the above distances. Exception: for an immediate level transition order, this rule does not apply in case the level transition has been announced and the distance for the execution of the level transition has been engineered such that the level transition is performed before the EOA/LOA is passed.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036 section 5.2.2.5 (for the value 1.3 m); section 4.2.9 (for the time Tn); section 5.6.3 (for the value 80 km/h). ERA/ERTMS/033281 section 3.1.2 (for the max distance between the first axle and the train front end).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Justification | - The underlying approach is that all information related to the extension of an MA or the level transition order at a border or the 'Stop if in SR' must have been received before the train is tripped, or override is ended, due to overpassing the EOA/LOA. - This rule is sufficient to ensure that the action resulting from the content of the balise group message will be considered by the on- board as preceding the overpassing of the EOA/LOA with the train 'min safe antenna position'/'min safe front end', i.e. it is sufficient to avoid that a train trip will occur regardless the time needed to process the balise group message (refer to SUBSET-026 section A.3.5.2). - According to the FFFIS Eurobalise no further information can be received from a balise if the (on-board) antenna has passed a balise by a distance of more than 1.3m                                                                                    |

<!-- image -->

## 4.1.1.5 Minimum distance between the last switchable balise of a balise group and limit of train detection section - for level 1

<!-- image -->

| Rule          | If the transition from one train detection section to the following one affects the information transmitted by a switchable balise, this switchable balise shall be placed at least 13.8 m in rear of the location where the detection device of the next section may start detecting the train.                                                                                                                                                                                                                                                                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036 section 5.2.2.5 (for the values 1.3 m)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Justification | - The aim of this rule is to avoid that the antenna of the train is still able to read information coming from the balise group of block n, while the train is already detected in block n+1 (e.g. as its 1 st axle short-circuits the track circuit of block n+1). - The rule takes into account the side lobe zone of the antennas and the balises, the last switchable balise of the group is therefore to be located at least 12.5 m (= the furthest location of the antenna in rear of the 1 st axle) + 1.3 m (= side lobe zone) = 13.8 m in rear of the detection device limit (to be defined). switchable balise in rear of TC joint |
| Comment       | In case of jointless track circuits the train detection area is overlapping both track circuits. The start of this area must be considered when defining the distances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

<!-- image -->

## 4.1.1.6 Number of balises that can be processed per unit of time

Rule

Let 'd' be the distance run by a train at the maximum speed of the line during 0.8 s.

In  this  distance  'd',  the  number  of  encountered  balises  shall  not exceed 8.

Note: The maximum speed of the line is the nominal line speed value (engineered SSP). Tolerances due to inaccuracy of speed measurements and speed margins before brake intervention are not to be taken into account for engineering.

Reference

Limitations of SUBSET-036 - section 4.2.9 must be considered

Justification

The rule is linked to processing of balise information on-board

Remark

Figure

Interoperable constraints to ensure that all the balises can be processed on-board

 9 balises received in window d :  NOT OK

 8 balises received in window d : OK

## 4.1.1.7 Intentionally deleted

## 4.1.1.8 Lateral and angular tolerances for balise installation

Rule

Reminder: the rules of the reference below must be respected.

Reference

Subset-036 section 5.6.2.3

Justification

-

© This document has been developed and released by UNISIG

<!-- image -->

## 4.1.1.9 Rules for balise installation in narrow curves

| Rule          | Reminder: the rules of the reference below must be respected regards the installation of Eurobalises in horizontal or vertical curves.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | Subset-036 section 5.6.5                                                                                                                 |
| Justification | -                                                                                                                                        |

## 4.1.1.10 Intentionally deleted

## 4.1.1.11 Balise group configurations

| Rule          | Reminder: the rules of the reference below must be respected regards - Number of balises in each group/use of single balise groups - TSR Balise groups   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-091 - section 8.3.2.1                                                                                                                             |
| Justification |                                                                                                                                                          |

## 4.1.1.12 Balise installation relative to track locations

| Rule          | The infill location reference given by the infill device must be in rear of the current EOA/LOA.              |
|---------------|---------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.4.3.1; 3.8.4.6.2-4; 4.8.1.5                                                            |
| Justification | An MA extension via an infill MA is only possible if there is no gap between the old MA and the MA extension. |

## 4.1.1.13 Balise installation relative to mission profile

| Rule          | Reminder: the rules of the reference below must be respected e.g. - Number of Unlinked Balise groups (marked as unlinked) - Maximum distances between Balise groups   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-091 - chapter 10 Mission Profile                                                                                                                               |
| Justification | The safety analysis and safety requirements are based on this mission profile of the reference above.                                                                 |

<!-- image -->

## 4.1.2 Rules for Eurobalise antenna

## 4.1.2.1 General installation rules for antennas (former 4.1.2.3)

| Rule          | Reminder: Installation rules presented in FFFIS for Eurobalise shall be respected.                                                                                                                                              |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036:  Section 5.2 : Balise air gap interface  Section 6.5 : Installation Requirements for Antennas  Section 6.6: Specific Environmental Conditions for Antennas  Section 6.7: Specific EMC Requirements for Antennas |
| Justification |                                                                                                                                                                                                                                 |

## 4.1.2.2 Minimum / maximum distance between the front of the engine / 1st axle of the engine and the Eurobalise antenna

<!-- image -->

<!-- image -->

<!-- image -->

| Reference     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Justification | The maximum value of 12.5m has been specified to allow the use of the same antenna for both directions, on a locomotive, and to provide sufficient space to install the antenna on all different types of trains. Furthermore the aim of the minimum distance of 2m to train front is : min2m min2m - to avoid an antenna receiving a telegram from a balise energised by another antenna - to avoid a balise energised by one antenna perturbing the transmission of an adjacent antenna. |
| Remark        | Interference with antennas of other systems, especially KER based, has to be considered as well.                                                                                                                                                                                                                                                                                                                                                                                           |

## 4.1.2.3 Intentionally deleted (former 4.1.2.2)

## 4.1.3 Rules for Euroloops

## 4.1.3.1 Intentionally deleted

## 4.1.3.2 General installation rules for Euroloops

| Rule          | Reminder: All installation rules given in FFFIS Euroloop have to be respected.                                                                                                                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-044  Section 6.1.3: Arrangements  Section 6.10: Trackside Installation Rules  Section 6.11: Specific Electrical Requirements  Section 6.13: EMC Requirements  Section 7.8: Installation constraints for the Antenna Unit Function |
| Justification |                                                                                                                                                                                                                                               |

<!-- image -->

## 4.1.4 Intentionally deleted

## 4.2 Telegrams and messages

## 4.2.1 Balise telegrams

## 4.2.1.1 Length of balise telegrams (300 km/h, 500 km/h)

| Rule          | Reminder: the rules of the references below must be respected.                                   |
|---------------|--------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-036 section 5.2.2.3.                                                                      |
| Justification | The rules are required in order to guarantee interoperability from a transmission point of view. |

## 4.2.2 Radio messages

Note:  Radio  messages  means  RBC  messages  or  radio  infill  messages  (the  same protocol is used in both cases).

## 4.2.2.1 Maximum length per message - to allow for the dimensioning of radio input buffers

| Rule          | Application data (excluding Euroradio protocol data) sent as normal priority data shall not exceed 500 bytes.                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                            |
| Justification | - the length must be sufficient for MA - track description, according to 4.3.2.1 a) - transmission delay - more risk of perturbation - size of EVC buffers |
| Remark        | A maximum number of bytes is not relevant for high priority data as only fixed size messages are used.                                                     |

## 4.2.3 Intentionally deleted

<!-- image -->

## 4.2.4 Data engineering rules for individual data types

## 4.2.4.1 Packet 145 (Inhibition of balise group, message consistency reaction)

| Rule          | For all balise groups: it shall be forbidden to transmit the packet 145 if the balise group message contains, for the same validity direction as packet 145, safety related data that, if missed, could lead to the ETCS core hazard.   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026, section 3.16.2.4.4.1 b), 3.16.2.5.1.1 b), 7.4.2.37.2                                                                                                                                                                        |
| Justification | According to SUBSET-091 table 14.1.1.2 footer 14, the message consistency check is a protective feature, which has already been credited when deriving the safety targets for the hazards BTM-H1, BTM-H4, EUB-H1, EUB-H4.               |

## 4.2.4.2 Sharing of identifiers within different transmission systems

| Rule          | Reminder: the rules of the reference below must be respected   |
|---------------|----------------------------------------------------------------|
| Reference     | SUBSET-026, section 3.18.4.4                                   |
| Justification |                                                                |

## 4.2.4.3 List of balises for SH Area

| Rule          | It shall be forbidden to send the packet 49 (list of Balises for SH Area) in a message which does not contain the packet 80 (Mode Profile) with the variable M_MAMODE = 'Shunting'. Exception: the rule does not apply for the radio message 'SH authorised' since its list of optional packets includes the packets 3, 44 and 49 only.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026, section 4.4.8.1.1 b), 8.4.4.4.1                                                                                                                                                                                                                                                                                               |
| Justification | The on-board must always link a list of balises for SH area to either one given mode profile 'Shunting' or to one SH authorisation from the RBC.                                                                                                                                                                                          |

<!-- image -->

## 4.2.4.4 Transmission of non-infill information by loop or RIU

| Rule          | The following non-infill information can be transmitted from a loop: - Packet 13 (SR distance information from loop) - Packet 44 (Data used by applications outside the ERTMS/ETCS system) - Packet 180 (LSSMA display toggle order) - Packet 254 (Default Balise/Loop/RIU information) The following non-infill information can be transmitted from an RIU: - Message 32 (RBC/RIU System Version) - Message 39 (Acknowledgement of session termination) - Packet 44 (Data used by applications outside the ERTMS/ETCS system) - Packet 45 (Radio Network registration) - Packet 143 (Session Management with neighbouring RIU) - Packet 180 (LSSMA display toggle order) - Packet 254 (Default Balise/Loop/RIU information)   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - 3.6.2.3, 4.8.1.5 SUBSET-040 - 4.2.4.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Justification | To clarify which packets not included in the list of allowable infill packets defined in section 4.2.4.5 can nevertheless be transmitted by loop or RIU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## 4.2.4.5.2

<!-- image -->

## 4.2.4.5 Infill Information

## 4.2.4.5.1

| Rule          | Infill information which is repeated from the balise group at the next main signal by any infill device shall be limited to infill MA, linking and route related track description information. All information which does not relate to Infill (e.g. information for opposite direction or EOLM etc.) shall not be given as infill information. Permitted infill information: - Packet 136 (infill location reference) - Packet 12, 80, 49 (MA, Mode Profile, List of Balises for SH area) - Packet 21 (Gradient Profile) - Packet 27, 51, 65/66, 70 (SSP, ASP, TSR, Route Suitability) - Packet 5 (Linking) - Packet 41 (Level transition) (see also next rule below) - Packet 44 (data used outside ERTMS) - Packet 39, 40 67, 68, 69 (Track condition) - Packet 71 (adhesion factor) - Packet 133 (Radio in-fill area information) - Packet 138, 139 (Reversing area information) - Packet 52 (Permitted Braking Distance Information)   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.8.4.6.3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Justification | This is to avoid any misinterpretation by on-board.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Rule          | If infill information contains an announcement of an immediate level transition at the location of the location reference for the infill information, for the distance D_LEVELTR the value of '0m' shall be used.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Justification | For infill only distance based information can be interpreted on-board                                                                                                                                              |

## 4.2.4.6.2

<!-- image -->

## 4.2.4.6 Mode Profile

## 4.2.4.6.1

| Rule          | The overlapping of mode profile areas in the mode profile packet shall be forbidden.   |
|---------------|----------------------------------------------------------------------------------------|
| Reference     |                                                                                        |
| Justification | There is no possibility to handle two mode profiles at the same location.              |

| Rule          | In case a Level 1 MA contains V_MAIN = 0 and the MA is transmitted with a mode profile, the mode profile shall start at distance zero.                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - 4.6.2 & 4.6.3 transition [32]                                                                                                                   |
| Justification | The procedures for mode transitions caused by mode profiles in Subset 026, chapter 5 do not cover 'further location' transitions from SR mode to OS, SH, LS. |

<!-- image -->

## 4.2.4.7 Track conditions

## 4.2.4.7.1

## Rule

The minimum distance (latest transmission) between announcement of  track  condition  Powerless  Section  with  pantograph  to  be  lowered and the start  location  of  this  track  condition  shall  correspond  to  17s when running at  line  speed  (engineered  SSP)  in  the  approach area (B-D in the figure below).

The minimum distance (latest transmission) between announcement of  track  condition  Powerless  Section  with  main  power  switch  to  be switched  off and  the  start location of this track condition  shall correspond  to  11s  when  running  at  line  speed  (engineered  SSP)  in the approach area (B-D in the figure below).

<!-- image -->

The minimum distance (latest transmission) between announcement of track condition Change of Traction System and the location of this track  condition  shall  correspond  to  17s  when  running  at  line  speed (engineered SSP) in the approach area (B-F in the figure below).

<!-- image -->

- A: LRBG which is the location reference point for the distances given
- B: latest announcement location
- D: start location of track condition Powerless Section with pantograph to be lowered or with main power switch to be switched off
- E: end location of track condition Powerless Section with pantograph
- to be lowered or with main power switch to be switched off
- F: location for track condition Change of Traction System

## 4.2.4.7.2

| Rule          | The minimum distance (latest transmission) between announcement of track condition - Air tightness - Switch off regenerative/eddy current (service/emergency)/magnetic shoe brake and the start location of this track condition shall correspond to 10s when running at line speed (engineered SSP) in the approach area.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 -section 3.7.1.1 c)                                                                                                                                                                                                                                                                                               |
| Justification | This distance needs to be long enough to ensure that the driver (or an optional automatic system) is able perform the related action before reaching the beginning of the track condition.                                                                                                                                   |

## 4.2.4.8 Linking data handling

## 4.2.4.8.1

| Rule          | Balise groups with balise group qualifier 'unlinked' shall never be announced via linking.                                                               |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                          |
| Justification | This is to avoid any contradiction between the consistency reaction regarding 'Unlinked' balise groups and the one regarding announced linking reaction. |

<!-- image -->

| Reference     | SUBSET-026 -section 3.7.1.1 c)                                                                                                                                                                                                                                                                                                                                         |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Justification | This distance needs to be long enough to ensure that the driver (or an optional automatic system) is able to perform the necessary actions (e.g. reduce traction power, open the main switch, lower the pantograph, change the traction system) before reaching the beginning of the powerless section or the location of the change of traction system, respectively. |

## 4.2.4.8.2

| Rule          | Balise groups with balise group qualifier 'unlinked' shall never be used to transmit linking information unless it is sent as infill information (see 4.2.4.5 herein).                                                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.6.1.4                                                                                                                                                                                                                                                                     |
| Justification | Balise groups with a balise group qualifier 'unlinked' can never become an LRBG. This rule aims at reducing system complexity caused by the relocation of information received from a mixture of linked and unlinked balise groups which in addition only leads to a degradation of performance. |

4.2.4.9 Intentionally deleted

4.2.4.9.1 Intentionally deleted

4.2.4.9.2 Intentionally deleted

## 4.2.4.10 Text transmission

| Rule          | The use of the end condition 'location' shall be allowed only if the start condition 'location" is used.   |
|---------------|------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.12.3.4; 7.4.2.23/24                                                                 |
| Justification |                                                                                                            |

## 4.2.4.11 Packet 131 (RBC Transition Order)

| Rule          | It shall be forbidden to use the special value 'Contact the last known RBC' for the RBC ETCS identity number NID_RBC.                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 7.5.1.96                                                                                                               |
| Justification | Using the special value 'Contact the last known RBC' would point to the Handing Over RBC which makes no sense in announcing an RBC Handover |

## 4.2.4.12 Intentionally deleted

<!-- image -->

<!-- image -->

## 4.2.4.13 Packet 88 (Level Crossing information)

| Rule          | The location of a level crossing, as defined by the combination of D_LX and L_LX, shall not coincide with the location of another level crossing, i.e. the defined positions of crossings shall be independent.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.12.5.4                                                                                                                                                                                     |
| Justification |                                                                                                                                                                                                                   |

## 4.2.4.14 Packets 72 and 76 (text messages)

| Rule          | It shall be forbidden to use the special value 'Contact the last known RBC' for the RBC ETCS identity number NID_RBC.                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - sections 7.4.2.23; 7.4.2.24                                                                                                       |
| Justification | The driver acknowledgement report is to be sent to the RBC interested in such report, which cannot be ensured by the use of the special value. |

## 4.3 Dimensioning rules for messages

## 4.3.1 Constraints

## 4.3.1.1 The maximum number of iterations of the same type of information:

| Rule          | In case the Engineering rules limit the number of iterations of a certain type of information, this shall take precedence over the 31 (= maximum of N_ITER) iterations stated in chapter 7 of the SRS.            |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 7.5.1.77                                                                                                                                                                                     |
| Justification | In chapter 7 of the SRS, a nominal value range for N_ITER was chosen in order to rationalise the ETCS language. Where specific limits for N_ITER are required, they are stated in the Engineering Rules document. |
| Remark        |                                                                                                                                                                                                                   |

## 4.3.2 Data

4.3.2.1 List of data that are related to dimensioning rules:

4.3.2.1.1 Note: The value for the 'Maximum number of iterations in 1 packet' in the rules below refers to the value of N\_ITER in the related packets.

<!-- image -->

## a)  Number of MA sections (excluding the End Section

|               | Maximum number of iterations in 1 packet                                | Minimum memorised on board                                                              |
|---------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Rule          | 5                                                                       | 6                                                                                       |
| Reference     |                                                                         |                                                                                         |
| Justification |                                                                         | The use of infill information requires at least one additional section to be memorised. |
| Remark        | In addition the MA includes an End Section which is not included in the | In addition the MA includes an End Section which is not included in the                 |

## b) Number of balise IDs in balise list for SR authority or for shunting mode

|               | Maximum number of iterations in 1 packet                                           | Minimum memorised on board                            |
|---------------|------------------------------------------------------------------------------------|-------------------------------------------------------|
| Rule          | 15 being transmitted using the same packet                                         |                                                       |
| Reference     |                                                                                    |                                                       |
| Justification | This packet will never be combined with other packets requiring a big data volume. | A new incoming balise list replaces the previous one. |

## c) Number of mode profile sections

|               | Maximum number of iterations in 1 packet               | Minimum memorised on board                                                                                                                                                                                           |
|---------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule          | 2                                                      | 6                                                                                                                                                                                                                    |
| Reference     | SUBSET-026 section-7.4.2.26 and section 4.2.4.6 herein |                                                                                                                                                                                                                      |
| Justification |                                                        | A mode profile contained in an Infill MA replaces the one stored only beyond the reference location. Therefore onboard can currently have 3 sections of mode profiles, and receive 3 more sections in the Infill MA. |

© This document has been developed and released by UNISIG

<!-- image -->

## d)  Number of locations with changes of SSP

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board                                                                                  |
|---------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Rule          | 31                                         | 50                                                                                                          |
| Reference     |                                            |                                                                                                             |
| Justification |                                            | 50 SSP sections memorised on- board with a change of SSP section every 500m would cover a distance of 25km. |

## e)  Number of TSR

|               | Maximum number of packets in 1 message   | Minimum memorised on board   |
|---------------|------------------------------------------|------------------------------|
| Rule          | 10                                       | 30                           |
| Reference     |                                          |                              |
| Justification |                                          |                              |

## f) Number of changes of gradient

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board                                                                            |
|---------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Rule          | 31                                         | 50                                                                                                    |
| Reference     |                                            |                                                                                                       |
| Justification |                                            | 50 gradients memorised on-board with a change in gradient every 500m would cover a distance of 25 km. |

Rule

Reference

Justification

## i) Number of linked balise groups

|               | Maximum number of iterations in 1 packet                                                                                                                                                                                                                                                                                                                                                                                                                                           | Minimum memorised on board                                                                                   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Rule          | 29                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 30                                                                                                           |
| Reference     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                              |
| Justification | 29 iterations allow for a maximum of 30 linked balise groups to be transmitted in one packet. Because new linking information completely overwrites old information, the amount of linked balises to be stored is unchanged Exception: In case linking information is transmitted as infill information, Engineering must take care of any balises between the infill location and the infill reference location (i.e. the main signal balise group) which remain stored on- board | The on-board system should be able to manage an MA of 30 km with an average of 1 linked balise group per km. |

<!-- image -->

## g) Number of locations for position reports

Maximum number of iterations in 1 packet

Rule

Reference

Justification

Remark

## h)  Number of text messages

Maximum number of iterations in 1

packet

1 plain text + 1 fixed text

15

Minimum memorised on board

If a train gets a new packet 58 from the RBC, it replaces the old position report parameter.

Minimum memorised on board

5 plain text + 5 fixed text

Rule

Reference

<!-- image -->

## j) Number of Track Conditions Change of traction system

Maximum number of iterations in 1 packet

Minimum memorised on board

Rule

Reference

No iteration in packet

SUBSET-026 - section 7.4.2.8

Justification

## k) Number of Track Conditions Big Metal masses

Maximum number of iterations in 1

packet

4

SUBSET-026 - section 7.4.2.19

Justification

## l) Number of Track Conditions

Maximum number of iterations in 1

packet

19

SUBSET-026 - section 7.4.2.20

Rule

Reference

Justification

## m)  Number of Route suitability data

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board                                                             |
|---------------|--------------------------------------------|----------------------------------------------------------------------------------------|
| Rule          | 2                                          | 1 list of loading gauges AND 1 value of axle load AND 1 value of traction system type. |
| Reference     | SUBSET-026 - section 7.4.2.21              |                                                                                        |
| Justification |                                            |                                                                                        |

© This document has been developed and released by UNISIG

1

The onboard system is able to manage one change of traction system at a time.

Minimum memorised on board

5

Minimum memorised on board

20

<!-- image -->

## n) Intentionally deleted

## o)  Number of Axle load speed profile segments

|               | Maximum number of iterations of ASP segments in 1 packet   | Minimum memorised on board   |
|---------------|------------------------------------------------------------|------------------------------|
| Rule          | 14                                                         | 30                           |
| Reference     | SUBSET-026 - section 7.4.2.13                              |                              |
| Justification |                                                            |                              |

## p)  Number of Axle load speed restriction values per ASP segment

|               | Maximum number of iterations per ASP segment   | Minimum memorised on board   |
|---------------|------------------------------------------------|------------------------------|
| Rule          | 3                                              |                              |
| Reference     | SUBSET-026 - section 7.4.2.13                  |                              |
| Justification |                                                |                              |

## q)  Number of adhesion profiles

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board   |
|---------------|--------------------------------------------|------------------------------|
| Rule          | No iteration in packet                     | 10                           |
| Reference     | SUBSET-026 - section 7.4.2.22              |                              |
| Justification |                                            |                              |

<!-- image -->

## r) Number of reversing area

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board   |
|---------------|--------------------------------------------|------------------------------|
| Rule          | No iteration in packet                     | 1                            |
| Reference     | SUBSET-026 - section 7.4.2.34              |                              |
| Justification |                                            |                              |

## s) Number of Permitted Braking Distance Speed Restrictions

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board   |
|---------------|--------------------------------------------|------------------------------|
| Rule          | 2                                          | 5                            |
| Reference     | SUBSET-026 - section 7.4.2.13.1            |                              |
| Justification |                                            |                              |

## t) Number of Track Conditions Station Platforms

|               | Maximum number of iterations in 1 packet   | Minimum memorised on-board   |
|---------------|--------------------------------------------|------------------------------|
| Rule          | 4                                          | 5                            |
| Reference     | SUBSET-026 - section 7.4.2.20.1            |                              |
| Justification |                                            |                              |

## u)  Number of Track Conditions Allowed Current Consumption

|               | Maximum number of iterations in 1 packet   | Minimum memorised on board   |
|---------------|--------------------------------------------|------------------------------|
| Rule          | No iteration in packet                     | 1                            |
| Reference     | SUBSET-026 - section 7.4.2.8.1             |                              |
| Justification |                                            |                              |

## v) Number of Level Crossings

© This document has been developed and released by UNISIG

<!-- image -->

|               | Maximum number of packets in 1 message   | Minimum memorised on board   |
|---------------|------------------------------------------|------------------------------|
| Rule          | 10                                       | 10                           |
| Reference     |                                          |                              |
| Justification |                                          |                              |

## w)  Number of Virtual Balise Covers set by trackside

|               | Maximum number of packets in 1 message   | Minimum memorised on board                                                                                                                                            |
|---------------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rule          | 10                                       | 10                                                                                                                                                                    |
| Reference     | SUBSET-026 - section 7.4.2.2.1           |                                                                                                                                                                       |
| Justification |                                          |                                                                                                                                                                       |
| Remark        |                                          | The minimum number stored on- board of this rule does not include the minimum number of VBCs set by driver that the on-board must be able to store (see rule 4.5.1.2) |

## x) Size of packet 44 with NID\_XUSER = 102

|               | Maximum number of bytes in packet 44 if NID_XUSER = 102                                                                                                                                                                                                                  | Minimum memorised on board   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| Rule          | 222                                                                                                                                                                                                                                                                      |                              |
| Reference     | SUBSET-026 sections 3.15.6.5 and 7.4.2.11 SUBSET-058 section 7.2.22                                                                                                                                                                                                      |                              |
| Justification | The total size of a packet 44 with NID_XUSER = 102, which will be forwarded in its entirety to an STM inside packet STM-45, must not exceed the maximum number of bytes which can be transmitted as user data in packet STM-45 (i.e. maximum value of variable N_LITER). | No memorisation applicable   |
| Remark        | The rule is only relevant for radio                                                                                                                                                                                                                                      |                              |

<!-- image -->

messages. In a balise group message, the maximum allowed size can never be exceeded.

## 4.3.3 Intentionally deleted

## 4.3.4 Multiple instances of Packets

## 4.3.4.1 Intentionally deleted

## 4.3.4.2 Multiple instances of packets in messages

| Rule          | Reminder: with regards to multiple instances of the same Packet inside a message, the rules of the references below must be respected.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 8.4.1.4                                                                                                             |
| Justification |                                                                                                                                          |

## 4.3.5 Intentionally deleted

## 4.4 Rules for on-board configuration data

## 4.4.1 Braking curves

## 4.4.1.1 Introduction

- 4.4.1.1.1 In order to properly set the National Values for braking curves, it is necessary to define the  conditions  under  which  the  nominal  emergency  brake  deceleration  and  build  up time are determined for the rolling stock.
- 4.4.1.1.2 If  the  braked  weight  percentage is acquired as Train Data by the ERTMS/ETCS onboard equipment and if the conversion model is applicable (i.e. the train is said to be a 'Lambda' train), the speed dependent deceleration profile and the brake build up time, which are obtained from the Conversion Model, are to be considered as the nominal emergency brake deceleration and build up time.
- 4.4.1.1.3 Otherwise, the nominal emergency brake deceleration profile(s) and build up time(s) are preconfigured and acquired as ETCS Train Data by the ERTMS/ETCS on-board equipment (i.e. the train is said to be a 'Gamma' train), and the rules specified in the section 4.4.1.2, 4.4.1.3, 4.4.1.4 and 4.4.1.5 shall apply.

<!-- image -->

4.4.1.1.3.1 Note:  these  rules  are  applicable  for  one  set  of  emergency  brake  deceleration profile, brake build up time and rolling stock correction factors belonging to a given set of ETCS Train Data, regardless of whether this latter covers one or more train formations.

## 4.4.1.2 Nominal emergency brake deceleration profile

## 4.4.1.2.1 Environmental conditions

4.4.1.2.1.1 The  nominal  emergency  brake  deceleration  shall  be  based  on  the  following environmental conditions: for conventional trains according to appendix F1.1 of UIC Leaflet 544-1, for high speed trains according to case A of 2008/232/EC.

## 4.4.1.2.2 Humidity of friction elements

4.4.1.2.2.1 The emergency brake deceleration shall be based on dry friction elements.

## 4.4.1.2.3 Track profile

If  field  tests  are  carried  out  to  define  the  nominal  emergency  brake  deceleration, they shall be performed on straight and as level as possible track. The deceleration

4.4.1.2.3.1 shall be corrected to level track.

## 4.4.1.2.4 Load

## 4.4.1.2.4.1 Passenger trains without automatic loading device

4.4.1.2.4.1.1 The  nominal  emergency  brake  deceleration  shall  be  valid  for  normally  loaded vehicles (see clause 4.2.3.2 of 2008/232/EC and clause 4.2.2.10 of 2011/291/EU).

## 4.4.1.2.4.2 Passenger trains with automatic loading device

4.4.1.2.4.2.1 For vehicles with automatic loading device the nominal emergency brake deceleration  shall  be  defined  as  the  lowest  deceleration  from  the  whole  loading range (from empty to exceptional load) and if the lowest deceleration is obtained by several  loads  then  the  greatest  load  shall  be  taken  into  account  as  the  nominal loaded condition

## 4.4.1.2.5 Use of special brake systems

4.4.1.2.5.1 Note:  All  installed  brake  systems  can  be  considered  in  the  nominal  emergency brake deceleration, based on a reliability/availability study.

4.4.1.2.5.2 In case special brake system(s) (regenerative brake, magnetic shoe brake or eddy current brake) is/are considered in the nominal emergency brake deceleration and if the train is running on lines where a certain special brake system is not permitted or must  be  inhibited  at  certain  locations  (through  the  track  condition  'Inhibition  of special brakes'), further nominal deceleration profiles without the contribution of the concerned special brake system shall be defined.

<!-- image -->

- 4.4.1.2.5.3 In  case  the  dynamic  brake  not  independent  from  the  presence  of  voltage  in  the catenary (i.e. regenerative brake not backed up by a rheostatic brake) is included in the  nominal  emergency  brake  deceleration,  further  nominal  deceleration  profile(s) without  the  contribution  of  this  brake  shall  be  defined.  Justification:  the  train  will always  encounter  a  powerless  section  (through  the  track  condition  'powerless section') wherever it will operate.

## 4.4.1.2.6 Wheel diameter

- 4.4.1.2.6.1 The nominal deceleration shall be based on new wheel diameter.

## 4.4.1.3 Emergency brake build up time

- 4.4.1.3.1 The  nominal  brake  build  up  time  shall  be  the  equivalent  brake  build-up  time  as specified in section 3.13.2.2.3.2 of SUBSET-026.

## 4.4.1.4 Rolling Stock Correction factor Kdry\_rst

- 4.4.1.4.1 Kdry\_rst(V,EBCL) shall be established for each confidence level that can be required by trackside (refer to sections 3.13.2.2.9.1.2, 3.13.2.2.9.1.3, 3.13.2.2.9.1.4  and variable  M\_NVEBCL  in  SUBSET-026).  For  the  dry  rail  reference  conditions,  see section 4.4.1.2.1.
- 4.4.1.4.2 Note: The Monte Carlo methodology has shown to be suitable for the determination of the Kdry\_rst values. However another methodology can be chosen, provided that it can be demonstrated that the required confidence levels are achieved.

## 4.4.1.5 Rolling Stock Correction factor Kwet\_rst

## 4.4.1.5.1 Trains fitted with wheel slide protection system

- 4.4.1.5.1.1 In  order  to  determine  the  correction  factor  Kwet\_rst(V),  field  tests  shall  be  made according to the provisions laid down in the following sections of EN15595:
-  6.1.2 (ambient temperature condition);
-  6.2.3 table 5 tests 1 &amp; 3 and 2 &amp; 4 (test programme for initial speed 120 km/h and maximum train speed, respectively);
-  6.4.2.1 (generation of reduced adhesion);
-  6.4.3.5 (spraying conditions for tests at speed higher than 200 km/h);
-  6.4.4.1 (correction of the measured stopping distance);
-  6.4.4.2 (number and validity of tests on dry rails);
-  6.4.4.3 (evaluation of validity of tests on wet rails).
- 4.4.1.5.1.2 For  each  pair  of  deceleration  distances  (on  dry  rail  and  with  reduced  adhesion) obtained from the tests 1 &amp; 3 and 2 &amp; 4, the increase of deceleration distance (in %)

<!-- image -->

obtained from the tests shall be used as follows to determine the correction factor: Kwet\_rst = 100/(100+ increase of deceleration distance (in %)), with the deceleration distance resulting from tests 3 &amp; 4 being the mean of the valid tests.

- 4.4.1.5.1.3 The  deceleration  distance  is  defined  as  the  total  distance  travelled  from  the triggering of brake command to the train stop, minus the distance travelled from this triggering to the elapsing of the equivalent brake build up time.
- 4.4.1.5.1.4 In  case  a  unique  Kwet\_rst  (i.e.  valid  for  all  speeds)  is  defined,  the  maximum increase  of  deceleration  distance  between  the  tests  1  &amp;  3  and  2  &amp;  4  shall  be retained.
- 4.4.1.5.1.5 Note: supplementary tests at other initial speeds (e.g. low speed) may be performed according to the same requirements, e.g. depending on a particular braking system configuration.

## 4.4.1.5.2 Trains not fitted with wheel slide protection system

- 4.4.1.5.2.1 For trains where the first four braked wheelsets are not fitted with a WSP system (without which the reference wheel/rail adhesion condition cannot be validated) the field tests specified in EN15595 cannot be used and the rules of §4.4.1.5.1 shall not be applied.
- 4.4.1.5.2.2 Note:  For  such  trains,  any  value  lower  than  or  equal  to  1  for  the  rolling  stock correction factor Kwet\_rst may be used.

## 4.4.2 On-board Supported Levels

Rule

The  default  list  of  levels  configured  on-board  shall  include  all  the levels  fitting  the  trackside  infrastructures  where  the  train  has  been granted access (i.e.  the  levels listed in the Interoperability Registers on the concerned infrastructures).

Reference

Justification

SUBSET-026 section 3.18.4.2

The  ERTMS/ETCS  on-board  equipment  must  always  be  able  to switch  to  a  level  ordered  by  trackside  (i.e.  fitting  the  line  where  the train  is),  independently  from  the  availability  of  the  parts  of  the  onboard equipment allowing to support this level.

In  case  of  degraded  operation,  it  is  always  the  responsibility  of  the Infrastructure  Manager  to  order  the  level  the  on-board  will  switch  to and,  even  though  the  train  is  not  fitted  with  the  National  System corresponding to the ordered level, to instruct the driver to follow the ad-hoc  operating  rules  applicable  for  a  train  with  a  failed  National System.

Therefore  the  so-called  on-board  default  list  of  levels  is  not  an unilateral  choice  made  by  the  Railway  Undertaking  based  on  the

<!-- image -->

devices the on-board is fitted with, but is rather a substitute of the list of  trackside  supported levels (packet 41) ordered by trackside when this list is not stored on-board.

## 4.4.3 Data Checks for Driver Input

| Rule          | The permitted range(s) for the technical and/or operational checks of a specific input field shall be within the limits defined in Subset-026, section A.3.11. The permitted resolution for a specific input field shall be equal to or lower than that defined in Subset-026, section A.3.11.   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 section A.3.11 ERA_ERTMS_015560 section 10.3.4                                                                                                                                                                                                                                        |
| Justification | Data check rules for data entered by the driver must comply with the limits defined by the SRS for this data.                                                                                                                                                                                    |

## 4.5 On-board dimensioning rules

## 4.5.1.1 STM related dimensioning rules

| Rule          | Reminder: the rules of the references below must be respected.   |
|---------------|------------------------------------------------------------------|
| Reference     | SUBSET-035  Section 15 Limitations                              |
| Justification |                                                                  |

## 4.5.1.2 Storage of Virtual Balise Covers set by driver

| Rule          | The ERTMS/ETCS on-board equipment shall be able to store at least 20 VBCs set by the driver                                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 - section 3.15.9.2                                                                                                                                                                                                                                                                                                                                      |
| Justification | In case of cross border cold movement from an LUC A to another LUC B, there should be sufficient storage capacity left for further VBC data entry by driver, assuming that the number of VBCs stored on- board from driver data entry in LUC A does not exceed the maximum allowed number of VBC that can be enforced by trackside at a time (see rule 4.3.2.1.1w) |

<!-- image -->

## 5. APPENDIX: RULES FOR KER COMPATIBILITY

5.1.1.1 The  following  rules  are  not  requested  for  ERTMS/ETCS  interoperability.  They  are additional requirements to equipment offering KER compatibility.

| Rule          | Reminder: the rules regarding KER compatibility of the reference below have to be respected                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-100  Section 4: Physical Interaction and Environment  Section 6 : RAMs  Annexes : Balise Type Specific Parameters SUBSET-101  Section 4.1.5: Balise group separation |
| Justification |                                                                                                                                                                                 |

5.1.1.2 Intentionally deleted

5.1.1.3 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 6. APPENDIX: ENGINEERING RULES FOR OLDER SYSTEM VERSIONS

## 6.1 Installation Rules

## 6.1.1 Miscellaneous

6.1.1.1 Level transitions borders and RBC/RBC handover borders

6.1.1.1.1 For any trackside system operating with system version number X = 1, the following rule shall apply:

| Rule          | Level transition borders and RBC/RBC handover borders shall not be located where shunting or reversing could take place.                                                        |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                                                 |
| Justification | Level transitions and RBC/RBC handovers are rejected by ERTMS/ETCS on-board equipment, supporting only system version number X = 1, when in Shunting mode or in Reversing mode. |

## 6.2 Telegrams and Messages

## 6.2.1 Data engineering rules for individual data types

## 6.2.1.1 Infill Information

<!-- image -->

## 6.2.1.1.1 For any balise telegram, loop message and RIU message with M\_VERSION where X = 1, rule 4.2.4.5.1 shall be replaced with:

| Rule          | Infill information which is repeated from the balise group at the next main signal by any infill device shall be limited to infill MA, linking and route related track description information. All information which does not relate to Infill (e.g. information for opposite direction or EOLM etc.) shall not be given as infill information. Permitted infill information: - Packet 136 (infill location reference) - Packet 12, 80; 49 (MA, Mode Profile, List of Balises for SH area) - Packet 21 (Gradient Profile) - Packet 27, 51, 65/66, 70 (SSP, ASP, TSR, Route Suitability) - Packet 5 (Linking) - Packet 41 (Level transition) (see also rule 4.2.4.5.2) - Packet 44 (data used outside ERTMS) - Packet 39, 67, 68, 206, 207, 239 (Track condition) - Packet 71 (adhesion factor)   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Justification | This for consistency with SRS Chapter 6, that defines which packets a Trackside operating with M_VERSION where X = 1 is allowed to transmit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## 6.2.1.2 Mode Profile

6.2.1.2.1 For any balise telegram, loop message and RIU message with M\_VERSION where X = 1, rule 4.2.4.6.2 shall be replaced with:

| Rule          | In case there is a Level 1 MA Packet with V_MAIN = 0, it is not allowed that the Message includes any mode profile packet.                                                                  |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     |                                                                                                                                                                                             |
| Justification | For an ERTMS/ETCS on-board equipment supporting only system version number X = 1, the reaction to a message containing a Level 1 MA Packet with V_MAIN = 0 and a mode profile is undefined. |

<!-- image -->

## 6.2.1.3 Level transition order

| Rule          | In a level transition order sent in a balise telegram or loop message with M_VERSION where X=1, or sent by an RBC/RIU with System Version where X=1, trackside shall include all applicable values of NID_STM containing the national system(s) installed in the infrastructure.   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | Subset-035 §7.4.1.1.17                                                                                                                                                                                                                                                             |
| Justification | When receiving such telegram or message, the on-board will not use any 'level translation' look-up table.                                                                                                                                                                          |

## 6.2.1.3.1 Conditional Level Transition Order

Rule

Any  trackside  system  operating  with  system  version  number  X  =  1 shall  not  send  packet  46  (Conditional  Level  Transition  Order)  in  a telegram or message which contains the packet 41 (Level Transition Order). In addition, it shall be forbidden to send packet 46 between a level transition announcement and the announced location of the level transition.

## Reference

Justification

In ERTMS/ETCS on-board equipment supporting only system version number  X=1,  a  packet  46  (Conditional  Level  Transition  Order)  may replace  a  packet  41  (Level  Transition  Order)  received  at  the  same time or already stored on-board and consequently cancel an announced level transition.

<!-- image -->

## 6.2.1.4 Track conditions

6.2.1.4.1 For any trackside system operating with system version number X = 1, rule 4.2.4.7.1 shall be replaced with:

<!-- image -->

| Rule          | The minimum distance (latest transmission) between announcement of track condition Powerless Section with pantograph to be lowered and the start location of this track condition shall correspond to 17s when running at line speed (engineered SSP) in the approach area (B-D in the figure below). The minimum distance (latest transmission) between announcement of track condition Powerless Section with main power switch to be switched off and the start location of this track condition shall correspond to 11s when running at line speed (engineered SSP) in the approach area (B-D in the figure below). The 'Distance to change of traction system' shall refer to the middle of a Powerless Section track condition (F in the figure below). E F powerless section Pantograph lowered/ Main power switch switched off running direction D LRBG Announcement distance D_TRACKCOND L_TRACKCOND B A D_TRACTION A: LRBG which is the location reference point for the distances given B: latest announcement location D: start location of track condition Powerless Section with pantograph to be lowered or with main power switch to be switched off E: end location of track condition Powerless Section with pantograph to be lowered or with main power switch to be switched off F: location for track condition Change of Traction System   |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | SUBSET-026 -section 3.7.1.1 c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Justification | No Change of Traction System announcement is computed by an ERTMS/ETCS on-board equipment supporting only system version number X = 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

<!-- image -->

## 6.2.1.4.2 Updating track conditions

| Rule          | A trackside operating in system version number X=1 that wants to update one track condition must at the same time resend all track conditions that it wants the ERTMS/ETCS on-board to apply, including those already entered by the train. Note: information about Big Metal Mass cannot be repeated from an RBC.   |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | Subset-026, section 3.7.3                                                                                                                                                                                                                                                                                            |
| Justification | How to update track conditions in ERTMS/ETCS on-boards supporting only system version number X=1 is open for different interpretations and there is a risk that when updating one track condition this may also replace (delete) others.                                                                             |

## 6.2.1.5 National Values

| Rule          | In National Values sent in a balise telegram with M_VERSION where X=1, or sent by an RBC with System Version where X=1, trackside shall include at least one country identifier for which the National Values are applicable.   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference     | Subset-026 §6.5.1.5.4                                                                                                                                                                                                           |
| Justification | There is no on-board behaviour defined for handling National Values received without identifier of the area(s) (country or region) in which they are applicable                                                                 |

## 6.3 Dimensioning rules for messages

## 6.3.1 Data

6.3.1.1 For any Trackside operated with system version number X=1, rule 4.3.2.1.1 c) shall be replaced with:

Number of mode profile sections

|               | Maximum number of iterations in 1 packet               | Minimum memorised on board                                   |
|---------------|--------------------------------------------------------|--------------------------------------------------------------|
| Rule          | 2                                                      | 3                                                            |
| Reference     | SUBSET-026 section-7.4.2.26 and section 4.2.4.6 herein |                                                              |
| Justification |                                                        | Based on the maximum number of iterations in 1 packet and on |

<!-- image -->

the fact that no minimum number of mode profile sections memorised on-board is specified for ERTMS/ETCS on-board equipment supporting only system version number X=1, it cannot be assumed that it stores more than 3 mode profile sections.

© This document has been developed and released by UNISIG

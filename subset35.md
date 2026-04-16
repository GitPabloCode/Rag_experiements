
<!-- image -->

- 8.6.1.1.1 Note:  In  HS  state,  when  receiving  national  trackside  information,  the  STM  treats  this information  to  be  prepared  to  take  charge  of  the  train  movement  supervision  once  it switches to Data Available state.
- 8.6.1.2 The  STM  in  HS  state  shall  have  the  possibility  to  send  an  'STM  max  speed' (V\_STMMAX) to the ERTMS/ETCS on-board through the STM Control Function.
- 8.6.1.2.1 Note: This 'STM max speed' is to allow the STM, for national reasons unknown to the ERTMS/ETCS on-board or ETCS Trackside, to request a given train speed at the level transition border in order to have a smooth transition.
- 8.6.1.3 The STM in HS shall have the possibility to send an 'STM system speed' (V\_STMSYS) together with an 'STM system distance' (D\_STMSYS) to the ERTMS/ETCS on-board through the STM Control Function.
- 8.6.1.3.1 Note:  This  'STM  system  speed'  together  with  the  'STM  system  distance'  is  sent  to allow  the  STM,  to  request  a  given  train  speed  at  a  given  position  ('STM  system distance')  before  the  level  transition  border  in  order  to  be  able  to  detect  its  national trackside.
- 8.6.1.4 When an STM in HS state receives an order to go in CS state, the STM shall have the possibility to close any connection except with STM Control Function.

## 8.7 Data Available (DA)

- 8.7.1.1 In DA state, an STM is responsible for the train movement supervision, according to the received national trackside information.
- 8.7.1.2 When an STM in DA state receives an order to go in CS state, the STM shall have the possibility to close any connection except with STM Control Function.

## 8.8 Failure (FA)

- 8.8.1.1 Being in this state, the STM is not able to work any more, due to internal or external reasons.
- 8.8.1.2 Being in this state, the STM shall not send messages any more on the bus except to report this state to the ERTMS/ETCS on-board functions.

<!-- image -->

## 9. STM MANAGER SYSTEM - REQUIREMENTS ON STM

## 9.1 Scope

  9.1.1.1 The scope of this chapter is to define how the STM handles its state.

## 9.2 STM States transitions table

## 9.2.1.1 Transitions table for STM

  | NP   | < 15      | < 15      | < 15      | < 15      | < 15      | < 15      | < 15   |
  |------|-----------|-----------|-----------|-----------|-----------|-----------|--------|
  | 1 >  | PO        |           |           |           |           |           |        |
  |      | 2 >       | CO        |           |           |           |           |        |
  |      |           | 3 >       | DE        |           |           |           |        |
  |      |           | 4a >      | 4a >      | CS        | < 4a      | < 4a < 4b |        |
  |      |           |           |           | 6 >       | HS        |           |        |
  |      |           |           |           | 9 >       | 9 >       | DA        |        |
  |      | 16 > 17 > | 16 > 17 > | 16 > 17 > | 16 > 17 > | 16 > 17 > | 16 > 17 > | FA     |

## 9.2.1.2 Transitions conditions table

  9.2.1.2.1 Note:  This  table  only  contains  the  event(s)  that  triggers  the  transition.  It  does  not describe the reasons why this(these) event(s) happens. ETCS orders referred to below are described in chapter 10.3.2.

  | Condition Id   | Content of the conditions                                                                                              |
  |----------------|------------------------------------------------------------------------------------------------------------------------|
  | 1              | STM is powered on                                                                                                      |
  | 2              | ETCS order 'Configuration'                                                                                             |
  | 3              | ETCS order 'Data Entry'                                                                                                |
  | 4a             | ETCS unconditional order 'Cold Standby'                                                                                |
  | 4b             | (ETCS conditional order 'Cold Standby' has been received) AND (STM does not or no more report National Trip Procedure) |
  | 5              | intentionally deleted                                                                                                  |
  | 6              | ETCS order 'Hot Standby'                                                                                               |
  | 7              | intentionally deleted                                                                                                  |
  | 8              | intentionally deleted                                                                                                  |
  | 9              | ETCS order 'Data Available'                                                                                            |

  © This document has been developed and released by UNISIG

<!-- image -->

  |   Condition Id | Content of the conditions                |
  |----------------|------------------------------------------|
  |             10 | intentionally deleted                    |
  |             11 | intentionally deleted                    |
  |             12 | intentionally deleted                    |
  |             13 | intentionally deleted                    |
  |             14 | intentionally deleted                    |
  |             15 | STM is powered off                       |
  |             16 | ETCS order 'Failure'                     |
  |             17 | The STM decides itself to go in FA state |

- 9.2.1.3 Note: As long as an STM in DA state is in a National Trip Procedure in SN mode, the STM  sends  cyclically  the  'National  Trip  Procedure'  information  to  the  STM  Control Function in order to fulfil the timeout requirements defined in 10.3.2.4 (transitions E16 and F16). If the mode changes to TR, the STM is expected to enter CS state even if its National  Trip  Procedure  is  not  finished,  as  the  Trip  procedure  is  handed  over  by ERTMS/ETCS  on-board  (otherwise,  the  STM  would  be  ordered  to  FA  state  through transition Q16 once the TR mode is exited).

## 9.3 General STM requirements

- 9.3.1.1 The STM antenna shall not energise trackside equipment, and shall not read trackside data, and shall not transmit data to trackside, except:
- a) in HS or DA state,
- b) for test purpose.
- 9.3.1.2 If the STM receives from the ERTMS/ETCS on-board a state transition order, which is not allowed by the state transition table (9.2.1.2), then the STM shall go in FA state.
- 9.3.1.3 The STM  shall report its NID\_STM  on  all point-to-point connections with the ERTMS/ETCS on-board:
- a) intentionally deleted
- b) with each transmitted application message from the STM to the ERTMS/ETCS onboard function or DMI channel.
- 9.3.1.4 The  STM  shall  report  its  current  state  on  all  point-to-point  connections  with  the ERTMS/ETCS on-board:
- a) intentionally deleted
- b) with each transmitted application message from the STM to the ERTMS/ETCS onboard function or DMI channel, and
- c)  whenever  the  STM  state  is  changed,  while  the  connection  to  the  respective ERTMS/ETCS on-board function or DMI channel is established.

<!-- image -->

  9.3.1.4.1 Exception: The FA state shall be reported if possible. Due to a failure of the STM itself it may not be possible to report the FA state.

  © This document has been developed and released by UNISIG

<!-- image -->

## 10. STM CONTROL FUNCTION

## 10.1 General requirements

- 10.1.1.1 It  shall  be possible to configure the ERTMS/ETCS on-board equipment with the list of STMs installed on-board.
- 10.1.1.2 The STM Control Function shall maintain a list of 'available' STMs, which includes all STMs  that  have  an  established  connection  to  the  STM  Control  Function  and  report either CS, HS or DA state.
- 10.1.1.3 Level  NTC  X  shall  be  considered  as  'Available  for  use'  for  level  transition  (see  [1] paragraph 5.10.2.4.1) if the STM X associated to this level is available.
- 10.1.1.4 The STM Control Function shall send to the STM the following information when the connection to the STM is established:
- a) The ERTMS/ETCS on-board functions that are available
- b) The ETCS bus address of all available ERTMS/ETCS on-board functions
- c)  The safety level of all available ERTMS/ETCS on-board functions (see 6.2)
- 10.1.1.4.1  Note: Only Juridical Data and DMI channels 2, 3 &amp; 4 can be marked as not available.
- 10.1.1.5 The STM Control Function shall inform the STM about the active DMI channel
- a) whenever the active DMI channel changes,
- b) whenever the connection to STM Control Function is established.

## 10.2 Association of STM X to Level NTC X

- 10.2.1.1 The ERTMS/ETCS on-board shall be configurable with a look-up table that gives the correspondence  between  NID\_NTC  values  and  the  NID\_STM  values  of  the  STM(s) fitted  on-board.  For  each  NID\_NTC  value  within  this  look-up  table,  a  list  of  one  or several NID\_STM values shall be configured, with a priority order.
- 10.2.1.1.1  Note: A National System can cover the functionalities of other National Systems having their  own  NID\_NTC  values.  For  that  case,  the  look-up  table  is  needed  to  map  the NID\_NTC  values  corresponding  to  these  encapsulated  National  Systems  to  the NID\_STM value(s) of the STM(s) fitted on-board supporting them. But an entry in the look-up  table  is  not  needed  for  the  case  there  is  a  one-to-one  relation  between NID\_NTC value and NID\_STM value.
- 10.2.1.1.2  Throughout this document, 'STM X' stands for 'STM associated to Level NTC X'. This STM is not necessarily fitted on-board.
- 10.2.1.2 If  Level  NTC  X  (defined  by  its  NID\_NTC)  is  not  already  associated  to  an  STM,  the ERTMS/ETCS on-board shall associate this Level NTC X to STM X as follows:
- a) When a level transition order to Level NTC X is accepted,

  © This document has been developed and released by UNISIG

<!-- image -->

  the STM X shall be the STM which NID\_STM is equal to NID\_NTC, if the level transition  order  is  received  from  a  trackside  constituent  with  ETCS  system version  strictly  lower  than  2.0  or  if  the  look-up  table  does  not  contain  the NID\_NTC value of Level NTC X.

  Otherwise  the  STM  X  shall  be  the  STM  having  the  highest  priority  among  the available STMs linked to the NID\_NTC value in the look-up table. If there is no available STM linked to this NID\_NTC value, the STM X shall be the STM having the highest priority among the STMs linked to this NID\_NTC value.

- b) When the ERTMS/ETCS on-board receives airgap data to be transmitted to an STM with the NID\_NTC value of Level NTC X, the STM X shall be associated as for the level transition.
- c)  When the Level NTC X is selected/validated by driver,

  the STM X shall be the STM which NID\_STM is equal to NID\_NTC, if the look-up table does not contain the NID\_NTC value of Level NTC X.

  Otherwise,  the  STM  X  shall  be  the  STM  having  the  highest  priority  among  the available STMs linked to this NID\_NTC value in the look-up table. If there is no available STM linked to this NID\_NTC value, then the STM X shall be the STM having the highest priority  among the connected STMs linked to this NID\_NTC value and that are not considered as failed or seen as isolated. Otherwise, the STM X shall be the STM having the highest priority among the STMs linked to this NID\_NTC value.

- 10.2.1.3 The association between a Level NTC X and an STM X shall be kept until the Level NTC X is left  after  having  been  entered,  or  until  the  Stand-By  or  No  Power  mode  is entered.
- 10.2.1.3.1  Note: If STM X associated to the current Level NTC X is no more available, it remains associated to Level NTC X until one of these conditions is fulfilled, even if another STM supporting NTC X is available. This avoids that there is a change of active STM that is neither due to a level transition from trackside, nor due to a driver level selection/validation.

## 10.3 STM MANAGER SYSTEM

## 10.3.1 Scope

  10.3.1.1 The present chapter does not specify the whole STM Control Function, but only the part of the STM Control Function that manages the states of the connected STM(s).

## 10.3.2 State transition orders

- 10.3.2.1 The STM Control Function STM state order table is a table that lists all the events that lead to a state order given by the STM Control Function to the STM.

<!-- image -->

  10.3.2.2 STM state order table (ERTMS/ETCS on-board STM Control Function)

  | NP         | < A15                                           | < A15                                           | < A15                                           | < A15                                                 | < A15                                                 | < A15                                                            | < A15   |
  |------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------|---------|
  | A1 >       | PO                                              | < A1                                            | < A1                                            | < A1                                                  | < A1                                                  | < A1                                                             | < A1    |
  |            | A2 >                                            | CO                                              |                                                 |                                                       |                                                       |                                                                  |         |
  |            |                                                 | A3 >                                            | DE                                              |                                                       |                                                       |                                                                  |         |
  |            |                                                 | A4a >                                           | A4a >                                           | CS                                                    | < C4a < E4a < G4a < H4a < I4a < J4a                   | < B4a < B4b < I4a < A4b < E4a < K4a < L4a                        |         |
  |            |                                                 |                                                 |                                                 | A6 > B6 >                                             | HS                                                    |                                                                  |         |
  |            |                                                 |                                                 |                                                 | A9>                                                   | A9 >                                                  | DA                                                               |         |
  | A17 > B16> | A16 > B16 > C16 > H16 > I16 > L16 > P16 > A17 > | A16 > B16 > C16 > H16 > I16 > O16 > P16 > A17 > | A16 > B16 > C16 > H16 > I16 > O16 > P16 > A17 > | A16 > B16 > C16 > D16 > H16 > N16 > O16 > P16 > A17 > | A16 > B16 > C16 > D16 > H16 > N16 > O16 > P16 > A17 > | A16 > B16 > C16 > E16 > F16 > H16 > N16 > O16 > P16 > Q16> A17 > | FA      |

  10.3.2.3

  The state indicated in table 10.3.2.2 corresponds to the last state report received from the STM or to FA state if an FA state order has been sent since the reception of the last state report. The STM Control Function shall consider the STM to be in NP when it has not received any state report from the STM.

  STM  state  order  conditions  table  applicable  to  STM  X,  associated  to  Level  NTC  X

  10.3.2.4 (ERTMS/ETCS on-board STM Control Function)

  | Condition Id   | Content of the conditions                                                 |
  |----------------|---------------------------------------------------------------------------|
  | A1             | (STM X connects to the STM Control Function) AND (STM X reports PO state) |
  | A2             | ('Request CO state' received from STM X)                                  |

  © This document has been developed and released by UNISIG

<!-- image -->

  | Condition Id   | Content of the conditions                                                                                                                                                                                                                              |
  |----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | A3             | ('Request DE state' received from STM X) AND (ETCS Train Data is validated)                                                                                                                                                                            |
  | A4a            | ('Request CS state' received from STM X)                                                                                                                                                                                                               |
  | B4a            | (ERTMS/ETCS on-board performs a level transition ordered by the trackside from Level NTC X to Level 0, 1, 2, 3)                                                                                                                                        |
  | C4a            | (announcement for a transition to Level NTC X is stored) AND (STM X reports HS state) AND (a level transition order to Level NTC Y is received before the transition to Level NTC X) AND (STM X is different from the STM Y associated to Level NTC Y) |
  | B4b            | (The driver manually changes the level from Level NTC X to Level NTC Y) AND (STM X is different from the STM Y associated to Level NTC Y)                                                                                                              |
  | E4a            | (ETCS mode changes to SB)                                                                                                                                                                                                                              |
  | G4a            | (STM X reports 'HS state') AND (no transition to any level associated to STM X for further location is stored on-board) AND (Override function is not active) AND (ETCS level is different from any level associated to STM X)                         |
  | H4a            | (ETCS mode is SB) AND (No cab is active)                                                                                                                                                                                                               |
  | I4a            | (ETCS mode changes to SH)                                                                                                                                                                                                                              |
  | J4a            | (announcement for a transition to Level NTC X is stored) AND (STM X reports HS state) AND (a level transition order to Level 0, 1, 2 or 3 is received before the transition to Level NTC X)                                                            |
  | K4a            | (The driver manually changes the level from Level NTC X to Level 0, 1, 2 or 3)                                                                                                                                                                         |
  | L4a            | (ETCS mode changes to TR)                                                                                                                                                                                                                              |
  | A4b            | (ERTMS/ETCS on-board performs a transition ordered by the trackside from Level NTC X to Level NTC Y) AND (STM X is different from the STM Y associated to Level NTC Y)                                                                                 |
  | A6             | (A transition to Level NTC X for a further location is stored on-board) AND (STM X reports CS state) AND (no other STM reports HS state)                                                                                                               |
  | B6             | (ETCS mode is SB) AND (Cab is active) AND (valid level of the ERTMS/ETCS on-board is Level NTC X) AND (STM X reports CS state) AND (no other STM reports HS state)                                                                                     |
  | A9             | (level of the ERTMS/ETCS on-board is Level NTC X) AND (STM X reports CS or HS state) AND (no other STM reports DA state) AND (ETCS mode is SN, SL or NL)                                                                                               |
  | A15            | (the ERTMS/ETCS on-board equipment is NOT powered)                                                                                                                                                                                                     |
  | A16            | (the STM Control Function receives from STM X a state request which is not allowed by the state transition table)                                                                                                                                      |
  | B16            | (STM X reports a state it must not be in according to table 9.2.1.1)                                                                                                                                                                                   |
  | C16            | (the STM Control Function has sent a state transition order except 'DA state transition order' and except 'conditional CS state transition order') AND (STM X does not report the required state within a maximum delay time of 10 seconds)            |

  © This document has been developed and released by UNISIG

<!-- image -->

  | Condition Id   | Content of the conditions                                                                                                                                                                                                                                                                                           |
  |----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | D16            | (the STM Control Function has sent a 'DA state transition order') AND (STM X does not report the required state within a maximum delay time of 5 seconds)                                                                                                                                                           |
  | E16            | (the STM Control Function has sent a 'conditional CS state transition order') AND (STM X does not report CS state or send a 'National Trip Procedure' information within a maximum delay time of 10 seconds)                                                                                                        |
  | F16            | (the STM Control Function has sent a 'conditional CS state transition order') AND (the STM Control Function has already received a 'National Trip Procedure' information from STM X) AND (STM X does not report CS state or send a 'National Trip Procedure' information within a maximum delay time of 10 seconds) |
  | H16            | (a final disconnection between the ERTMS/ETCS on-board STM Control Function and STM X was detected (see [3] and [2]))                                                                                                                                                                                               |
  | I16            | (The ERTMS/ETCS on-board performs a transition ordered by trackside to Level NTC X) AND (STM X is not available)                                                                                                                                                                                                    |
  | L16            | (STM X has not yet sent the Specific NTC Data Need) AND (STM X requests CO state)                                                                                                                                                                                                                                   |
  | N16            | (The timeout TrainDataView_STM_Response_Timeout for STM X has expired)                                                                                                                                                                                                                                              |
  | O16            | (The timeout TrainDataEntry_STM_Response_Timeout for STM X has expired)                                                                                                                                                                                                                                             |
  | P16            | (A safety-related information has not been transmitted to STM because of disconnection)                                                                                                                                                                                                                             |
  | Q16            | ('National Trip Procedure' is active) AND (STM X reports again 'National Trip Procedure' information) AND (the current ETCS mode is PT or UN)                                                                                                                                                                       |
  | A17            | (STM X reports FA state)                                                                                                                                                                                                                                                                                            |

  10.3.2.5 Note: The delay is shorter for transition to DA state because this transition is assumed as the most critical one from a safety aspect.

- 10.3.2.6

  When the conditions to change the STM state within the STM Control Function are valid according to 10.3.2.2 and 10.3.2.4, the STM  Control Function shall send the corresponding state transition order to STM X.

  10.3.2.6.1  Exception 1: The STM Control Function shall not send an order for NP or PO state.

  10.3.2.6.2  Exception 2: The STM Control Function shall not send an order for FA state if the STM has reported FA state (transition A17).

  10.3.2.7

  When the state transition  order  is  going  to  CS  state,  the  STM  Control  Function  shall send  an  'unconditional  order  CS  state'  for  the  transitions  A4a,  B4a,  C4a,  E4a,  G4a, H4a, I4a, J4a, K4a and L4a, and a 'conditional order CS state' for the transitions A4b and B4b.

  10.3.2.8 Note about Q16 condition: The Trip mode is entered if the STM X is in National Trip Procedure when a transition to level 0, 1, 2 or 3 occurs. The National Trip Procedure

<!-- image -->

  may still be reported after this transition in case the STM has been ordered to CS with a conditional order due to a previous level transition from NTC X to NTC Y.

## 10.3.3 Requirements linked to state transition orders and state reports

- 10.3.3.1 The  STM  Control  Function  shall  not  evaluate  the  state  transition  order  conditions, except conditions to FA state, if this STM has not reported the state corresponding to the last state transition order.
- 10.3.3.2 An STM is considered as active by the ERTMS/ETCS on-board from the moment it has sent the DA state order to the STM until it sends another state order to this STM (except 'conditional CS state transition order') or receives a state report different from DA from this STM.
- 10.3.3.3 The  STM  Control  Function  shall  command  the  emergency  brake  from  the  moment  a 'conditional  CS  state  transition  order'  has  been  sent  to  a  STM  and  this  STM  is  in National Trip Procedure, up to the moment this STM reports CS state, or is considered as failed and the train reaches standstill.
- 10.3.3.3.1  Note: This brake command avoids that the train could run untimely without supervision, in case the active STM does not send a brake command but still sends its National Trip Procedure which delays the activation of the STM of the newly entered area.
- 10.3.3.4 The STM Control Function shall apply the emergency brake when the level is NTC X and the mode is SN and STM X is known as installed on-board but not available.
- 10.3.3.5 Exception: the brake shall not be applied in case the STM X is known to be isolated, through the corresponding input on the Train Interface.
- 10.3.3.6 The emergency brake application shall be released by the STM Control Function when
- a) the STM X has established the connection to the STM Control Function after a nonfinal disconnection and the reported STM X state is DA,
- b) or the level changes to Level 0, 1, 2, 3,
- c)  or the level changes to a Level NTC Y that is not associated to STM X,
- d) or the mode SN is left with no change of level,
- e) or the dedicated input on the Train Interface informs the ERTMS/ETCS on-board that the STM X is isolated.
- 10.3.3.7 The ERTMS/ETCS on-board shall accept the reconnection of an STM not considered as in FA state or reporting PO state, except in case of final disconnection on Safety Layers.
- 10.3.3.8 The STM Control Function shall inform the driver that the STM X is not available while all of the following conditions are fulfilled
- -the level is NTC X,
- -and (the mode is SN) or (the mode is NL and has been so for at least 5s),
- -and STM X is known as installed on-board but not available,

<!-- image -->

- -and STM X is not known to be isolated through the corresponding input on the Train Interface.

  10.3.3.8.1  Note:  the  5s  delay  on  the  information  to  the  driver  is  required  because  the  STM  X requests to enter in CS state only after the mode has changed to NL.

## 10.4 ETCS data

  10.4.1.1 The ETCS data transmitted by the ERTMS/ETCS on-board to the STMs shall include a subset of the ETCS Train Data (defined in [1]), as listed below:

- a) Train category(ies)
- b) Train length
- c)  Traction / brake parameters
- d) Maximum train speed
- e) Loading gauge
- f)  Axle load category
- g) Traction system(s) accepted by the engine
- h) Train fitted with airtight system
9. 10.4.1.2 The ETCS data transmitted by the ERTMS/ETCS on-board to the STMs shall include a subset of the ETCS Train Data entry input fields (defined in [9]), as listed below:
- a) Train Type, if applicable for the train
11. 10.4.1.3 Note:  Extra  data  for  the  available  STMs  are  handled  in  the  Specific  NTC  Data  Entry procedure see chapter 10.7.
12. 10.4.1.4 The traction / brake parameters shall include:
- a) Equivalent brake build up time for full service brake for the combination of none of the special brakes being used
- b) Equivalent brake build up time for emergency brake for the combination of none of the special brakes being used
- c)  Traction cut off time
- d) Brake position
- e) Brake percentage, if applicable for the train
18. 10.4.1.5 The ETCS data transmitted by the ERTMS/ETCS on-board to the STMs shall include a subset of ETCS Additional Data (defined in [1]) as listed below:
- a) Train Running Number
- b) ETCS identity
- c)  Adhesion factor
- d) Date and Time (UTC Time)

  © This document has been developed and released by UNISIG

<!-- image -->

- 10.4.1.6 The ETCS data transmitted by the ERTMS/ETCS on-board to the STMs shall include the ETCS National / Default Values (defined in [1])
- 10.4.1.7 The STM Control Function shall transmit the subset of valid ETCS Train Data when the ETCS Train Data is validated.
- 10.4.1.7.1  Note: ETCS Train Data could be changed and validated from sources different from the driver if acquired from ERTMS/ETCS on-board external sources.
- 10.4.1.8 The STM Control Function shall transmit the valid ETCS Additional Data
- a) when the STM has entered into Configuration (CO) state, and
- b) when the valid ETCS Additional Data except date / time has changed.
- 10.4.1.9 The  STM  Control  Function  shall  transmit  the  currently  used  ETCS  National  /  Default Values
- a) when the STM has entered into Configuration (CO) state, and
- b) when the currently used ETCS National Values have changed (this also includes the case when the National Values are reset to the Default Values).

## 10.5 ETCS status data

- 10.5.1.1 The STM Control Function shall send the  ETCS status data consisting of the current ETCS mode and level (defined in [1]):
- a) To all connected STMs whenever the ETCS mode or level changes.
- b) To any STM when the connection to the STM Control Function is established.

## 10.6 Language used to display information to the driver

- 10.6.1.1 The STM Control Function shall transmit the language used to display information to the driver:
- a) To all connected STMs whenever the language is changed,
- b) To any STM when the connection to the STM Control Function is established.

## 10.7 Specific NTC Data Entry

## 10.7.1 Definitions

- 10.7.1.1 The 'Specific NTC Data' are the national data that need to be requested to the driver.
- 10.7.1.2 The STM may use the transmitted ETCS data: ETCS Train Data, ETCS Additional Data and ETCS National Values in order to reduce the entry of 'Specific NTC Data' by the driver.
- 10.7.1.3 All  'Specific NTC Data' used by all the different STMs are assigned a unique identity made of NID\_STM and Data Identifier.

  © This document has been developed and released by UNISIG

<!-- image -->

- 10.7.1.4 The process to deliver those 'Specific NTC Data' to the STM is called 'Specific NTC Data Entry'.
- 10.7.1.4.1  Note:  Specific  NTC  Data  Entry  is  possible  at  start-up  and  later  on  during  mission through the Train Data Entry procedure.

## 10.7.2 Responsibilities

- 10.7.2.1 The ERTMS/ETCS on-board equipment is responsible for the dialogue with the driver during the Specific NTC Data Entry/Validation process, for checking the technical range checks (if configured on-board) and for the transmission of the Specific NTC Data after the driver's validation.
- 10.7.2.2 The  STM  is  responsible  for checking  the content (e.g. range, spares, internal dependency of parameters) of the data. The STM can be exempted of technical range checks if those are configured in the ERTMS/ETCS on-board equipment.

## 10.7.3 General requirements

- 10.7.3.1 The ERTMS/ETCS on-board equipment shall offer the possibility to the driver to skip the Specific NTC Data Entry for a STM.
- 10.7.3.2 The ETCS Train Data as well as the Specific NTC Data might become invalid within the STM at any time due to national requirements. In this case, the STM may request the data from the ETCS by sending the 'Specific NTC Data Need'.
- 10.7.3.3 Specific NTC Data can be or become invalid, because:
- a) the  ETCS  Train  Data  Entry/Specific  NTC  Data  Entry  procedure  has  not  yet  been performed or has been aborted, or
- b) the driver has skipped the Specific NTC Data Entry for this STM before the STM has sent the 'End of Specific NTC Data Entry' to the ERTMS/ETCS on-board, or
- c)  the  ETCS Train Data Entry procedure has already been performed by the time the STM has entered  into  CO  state,  e.g.  the  STM  has  been  powered  on  or  restarted during train mission, or
- d) the  ETCS  Train  Data  has  changed  from  sources different  from  the  driver  and  this change impacts the validity status of the Specific  NTC Data, according to national rules, or
- e) because of STM internal function, e.g. national shunting.
- 10.7.3.4 When the ERTMS/ETCS on-board receives the 'Specific NTC Data Need' while in FS, LS,  SR,  OS,  UN,  TR,  PT  and  SN  modes,  it  shall  inform  the  driver  that  the  national system needs data.
- 10.7.3.5 The ERTMS/ETCS on-board shall delete this information to the driver when the driver initiates the Train Data entry procedure or when the corresponding STM is considered as failed or when this STM is known to be isolated by TIU 'NTC isolation status' input data.

<!-- image -->

- 10.7.3.6 The  STM  requests  its  Specific  NTC  Data  with  a  'Specific  NTC  Data  Entry  request' which  shall  include  for  each  Specific  NTC  Data,  the  following  information:  the  label, optionally a default value, and optionally values for a dedicated keyboard.
- 10.7.3.7 Note: Unless values for a dedicated keyboard are provided or the type of keyboard is configured on-board, an alphanumeric keyboard will by default be used (see document ref [9]).
- 10.7.3.8 It shall be possible to configure in the ERTMS/ETCS on-board the following parameters for any STM:
- 1) The window titles for the NTC data entry, the NTC data validation and the NTC data view windows
- 2) For each Specific NTC Data Identifier not using a dedicated keyboard:
- a)  The type of keyboard amongst numeric, enhanced numeric and alphanumeric
- b) If  the  type  of  keyboard  is  numeric  or  enhanced  numeric,  whether  leading zeros have to be kept and sent to the STM
- c) The  allowed  minimum  and  maximum  value,  that  shall  be  used  by  the ERTMS/ETCS on-board with a technical range check
- 10.7.3.9 By  analogy  to  the  modification/revalidation  of  ETCS  Train  data,  the  [1]  requirements 3.14.1.7.3,  3.18.3.3.1  regarding  the  brake  command/release  when  a  movement  is detected  while  modifying  or  revalidating  the  Train  Data  in  normal  operation  after  the start of mission shall also apply for the NTC data modification/revalidation.

## 10.7.4 Specific NTC Data Entry procedure

- 10.7.4.1 As soon as the ETCS Train Data is validated by the driver and if the connected STM is in CO, DE, CS, HS or DA state, the ERTMS/ETCS on-board shall indicate to the STM the beginning of its Specific NTC Data Entry procedure by sending the START flag.
- 10.7.4.2 The ETCS Train Data shall be sent immediately after the START flag.
## 3. GENERAL

## 3.1 References

| Ref. N°   | Document Reference      | Title                                                |
|-----------|-------------------------|------------------------------------------------------|
| [1]       | SUBSET-026              | System Requirements Specification                    |
| [2]       | SUBSET-056              | STM FFFIS Safe Time Layer                            |
| [3]       | SUBSET-057              | STM FFFIS Safe Link Layer                            |
| [4]       | SUBSET-058              | FFFIS STM Application Layer                          |
| [5]       | CENELEC 50170-2 (1996)  | PROFIBUS                                             |
| [6]       | SUBSET-034              | FIS for the Train Interface                          |
| [7]       | SUBSET-041              | Performance Requirements for Interoperability        |
| [8]       | CENELEC EN 50159 (2010) | Safety related communication in transmission systems |
| [9]       | ERA_ERTMS_015560        | ETCS Driver Machine Interface                        |
| [10]      | SUBSET-101              | Interface 'K' specification                          |
| [11]      | ERA_ERTMS_040001        | Assignment Of Values To ETCS Variables               |

## 3.2 Scope and purpose

- 3.2.1.1 The  acronym  FFFIS  stands  for  'Form  Fit  Functional  Interface  Specification'.  This means  an  interface  specification  covering  all  protocol  levels  of  communication,  and including connector and physical level.
- 3.2.1.2 The  lowest  level  boundary  of  this  specification  is  the  'Field  Data  Link'  layer  of  the PROFIBUS. The term 'bus' used afterwards in the document corresponds to this FDL layer.  The  referenced  PROFIBUS  standards  cover  the  lowest  communication  layers, physical layer including connector, see [5].
- 3.2.1.3 The upper boundary of the specification describes the functions linked to the interface between an ERTMS/ETCS on-board equipment and an STM.
- 3.2.1.4 The FFFIS STM specifies the set of requirements enabling the ERTMS/ETCS on-board equipment to be connected to any STM (i.e. the ERTMS/ETCS on-board and the STMs are interchangeable), so that:
- a) The functionality  of  the  assembly  ERTMS/ETCS  on-board  equipment  /  STM operating  in  level  NTC  /  mode  SN  is  equivalent  to  the  one  of  the  legacy  National Train Control system,
- b) The  transitions  between  ERTMS/ETCS  and  a  National  System  and  the  transitions between National Systems are seamlessly performed, with no additional constraint exported  on  the  trackside  other  than  the  installation  of  Eurobalises  for  the  level transitions.

<!-- image -->

- 3.2.1.5 Within the set  of  requirements  allocated  to  the  ERTMS/ETCS on-board in this FFFIS STM, the access to some of the ERTMS/ETCS on-board standardised interfaces (DMI, Train  Interface,  Juridical  Recording  interface)  or  functions  (e.g.  odometer)  allows minimising the number of interfaces/components needed for the installation of several National Systems on-board.
- 3.2.1.6 However,  the  use  of  specific  interfaces  or  functions  by  National  Systems,  instead  of these ERTMS/ETCS on-board interfaces/functions offered through this FFFIS STM, is permitted as long as it does not export any requirement on the ERTMS/ETCS on-board in addition to the ones specified in this FFFIS STM. Their choice and their definition are outside the scope of this specification.
- 3.2.1.7 Any implementation that does not comply with the clause 3.2.1.6 is considered as not compliant with the FFFIS STM and is outside the scope of this specification.
- 3.2.1.8 The use of the Interface 'K' (see document ref [10]), which offers access to the KER balise interface, also allows minimising the number of antennas installed on-board, but is  not  considered  as  part  of  this  FFFIS  STM  as  the  data  is  not  transmitted  over  the PROFIBUS.

<!-- image -->

## 4. INTRODUCTION

## 4.1 General requirements

- 4.1.1.1 The STM shall be identified by a unique number NID\_STM. The NID\_STM value used by  the  STM  shall  be  equal  to  one  of  the  NID\_NTC  values  as  specified  in  the  list referenced in document [11].
- 4.1.1.2 STM shall use the common Time information from ERTMS/ETCS on-board distributed through the STM interface.
- 4.1.1.3 Only one STM shall be active (supervising) at a time (see chapter 10.3.3.2 for definition of active STM).
- 4.1.1.4 The  ERTMS/ETCS  on-board  shall  be  responsible  for  monitoring  the  STM  interface safety  integrity  of  connected  STMs  and  for  applying  the  emergency  brake  in  case  of failure of the active STM.
- 4.1.1.4.1 Justification: The failure of a non active STM is not critical to train safety.

## 4.2 STM Isolation

- 4.2.1.1 It  shall be possible to isolate an STM from its interface to the ERTMS/ETCS on-board equipment. The isolation shall ensure that the function of the bus is not disturbed by the isolated STM.

<!-- image -->

## 5. ERTMS/ETCS ON-BOARD FUNCTIONS

## 5.1 Functional architecture

5.1.1.1 The ERTMS/ETCS on-board equipment shall allow the STM to communicate with the following functions:

- a) DMI
- b) STM Control
- c)  Reference Time
- d) BIU
- e) TIU
- f)  Juridical Data
- g) Odometer

Figure 1 - General configuration of STM and ERTMS/ETCS on-board

<!-- image -->

## 5.2 Data and ERTMS/ETCS on-board functions

- 5.2.1.1 The  following  paragraphs  describe  the  ERTMS/ETCS  on-board  functions  that  are available for STM and the data that shall be transmitted over the interface.
- 5.2.1.2 The data is transmitted over the STM bus using Multicast or Point-to-Point Connections, see chapter 6.5.

## 5.2.2 Reference time

<!-- image -->

- 5.2.2.1 ERTMS/ETCS  on-board  is  responsible  for  providing  common  reference  time  to  all connected STMs. This is defined in [2].

## 5.2.3 Odometer

- 5.2.3.1 Odometry data &amp; parameters shall be sent by the ERTMS/ETCS on-board to all STMs using multicast messages.

## 5.2.4 Train Interface (TIU)

- 5.2.4.1 A subset of the train interface signals specified in [6], command and status / availability are  transmitted  via  the  FFFIS  STM.  These  train  interface  signals  transmitted  via  the FFFIS STM are called Train Interface FFFIS STM signals.
- 5.2.4.2 The  TIU  Function  is  described  as  the  exchange  of  information  between  the  train interface and the STM, in this case:
- a) Status: is functional information coming from the train interface to the STM,
- b) Command: is functional information coming from the STM to the train interface.

## 5.2.4.3 Train Interface FFFIS STM command signals shall be:

| Command signal                         | Description                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------|
| Regenerative Brake                     | To allow or to suppress the use of the Regenerative Brake.                               |
| Magnetic Shoe Brake                    | To allow or to suppress the use of the Magnetic Shoes Brake.                             |
| Eddy Current Brake for Service Brake   | To allow or to suppress the use of the Eddy Current Brake for Service Brake.             |
| Eddy Current Brake for Emergency Brake | To allow or to suppress the use of the Eddy Current Brake for Emergency Brake.           |
| Pantograph                             | Lower or raise the Pantograph                                                            |
| Air Tightness                          | Open or close air flaps                                                                  |
| Main Switch / Circuit Breaker          | Open or close the Main Switch / Circuit Breaker. This is considered as only one command. |
| Traction Cut Off                       | Cut off or not the traction                                                              |

- 5.2.4.3.1 Note: Service and Emergency Brake commands are handled in the BIU interface see chapter 5.2.5.

## 5.2.4.4 Train Interface FFFIS STM status signals shall be:

| Status signal                    | Description                                        |
|----------------------------------|----------------------------------------------------|
| Traction status                  | Specifies the status of the traction power         |
| Direction Controller information | Specifies the position of the direction controller |
| Cab Status                       | Specifies the active cab                           |

- 5.2.4.4.1 Note: Service and Emergency Brake status are handled in the BIU interface see chapter 5.2.5.

## 5.2.5 Brake Interface (BIU)

© This document has been developed and released by UNISIG

<!-- image -->

- 5.2.5.1 The Brake Interface via ETCS is formally a part of the Train Interface. It shall include the  brake  interface  parameters,  command  and  status  /  availability  of  the  Emergency Brake access and the Service Brake access.
- 5.2.5.2 Note: The BIU Function is separated from the TIU Function to allow physical separation and different safety and performance levels between brake commands/status and other commands/status on the Train Interface.
- 5.2.5.3 The brake status gives the availability of the brake command.

## 5.2.6 Juridical data

- 5.2.6.1 The FFFIS STM shall offer the possibility to the STM to transmit the national juridical data to be forwarded (together with the ETCS data) to the On-Board Recording Device.

## 5.2.7 STM Control Function

- 5.2.7.1 The  STM  Control  Function  shall  control  the  STM  state  and  the  compatibility  of  the ERTMS/ETCS on-board and STM versions.
- 5.2.7.2 The STM Control Function shall handle the transmission of the ETCS data for STM and of the Specific NTC Data Entry/Data View for STM.
- 5.2.7.3 The STM Control Function shall handle the transmission of the ETCS status data for STM.
- 5.2.7.4 The STM Control Function shall handle the transmission of the language used to display information to the driver.
- 5.2.7.5 The STM Control Function shall handle the test procedure for STMs.
- 5.2.7.6 The STM Control Function shall handle the Override procedure for STMs.
- 5.2.7.7 The STM Control Function shall handle the airgap data to be transmitted to an NTC.
- 5.2.7.8 The STM  Control Function shall handle STM  max speed and STM  system speed/distance.
- 5.2.7.9 The STM Control Function shall handle the transmission of the bus address, safety level and availability of the ERTMS/ETCS on-board functions.
- 5.2.7.10 The STM Control Function shall handle the display of STM failure status.
- 5.2.7.11 The  STM  Control  Function  shall  handle  the  transmission  of  the  active  Interface  'K' Antenna/BTM.
- 5.2.7.12 The STM control function shall handle the transmission of the BTM alarm data.

## 5.2.8 DMI

- 5.2.8.1 The DMI Function shall allow an active STM to dialogue with the driver for what regards its default window (see [9] chapter 9). This includes:

<!-- image -->

- a) Management of buttons,
- b) Management of indicators,
- c)  Management of sounds,
- d) Management of text messages,
- e) Management of supervision information

## 5.3 ERTMS/ETCS on-board functions and resources available for STMs

5.3.1.1 The ERTMS/ETCS on-board shall allow the STM to access its functions and resources according to the following table:

- a) x = access is allowed in all Levels
- b) (x) = access is allowed in all Levels if possible
- c)  s = access is only allowed for an active STM (see chapter 4.1.1.3)
- d) h = access is allowed for an STM in HS for preliminary request for DMI objects (see 13.2.1.5)
5. 5.3.1.2 When an ERTMS/ETCS on-board function fails, it shall isolate itself from the bus and shall try to close the connection with the STM.

| ERTMS/ETCS ON-BOARD functions and resources available for STMs   | N P   | S B   | P S   | S H   | F S   | L S   | S R   | O S   | S L   | N L   | U N   | T R   | P T   | S F   | S N   | R V   |
|------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| STM Control Function                                             |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     |       | x     | x     |
| Reference Time                                                   |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     |       | x     | x     |
| DMI Function                                                     |       | h     |       |       | h     | h     | h     | h     |       | s, h  | h     | h     | h     |       | s, h  |       |
| Juridical Data                                                   |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | (x)   | x     | x     |
| Odometer Function                                                |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     |       | x     | x     |
| TIU command (Train Interface FFFIS STM signals)                  |       |       |       |       |       |       |       |       | s     | s     |       |       |       |       | s     |       |
| TIU status (Train Interface FFFIS STM signals)                   |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     |       | x     | x     |
| BIU command                                                      |       |       |       |       |       |       |       |       |       |       |       |       |       |       | s     |       |
| BIU status                                                       |       | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     | x     |       | x     | x     |

<!-- image -->

## 6. BUS

## 6.1 The PROFIBUS

- 6.1.1.1 The  bus  used  for  the  interface  between  STM  and  ERTMS/ETCS  on-board  functions shall be the PROFIBUS, defined by [5].
- 6.1.1.2 The PROFIBUS protocol is used up to the FDL layer.
- 6.1.1.2.1 Note: The use of the FDL layer is specified in [3], chapter 4.
- 6.1.1.3 The bus configuration parameters for the PROFIBUS shall be:
- a) Baud Rate: 1500 Kbps
- b) Minimum Station Delay of Responders (min TSDR): 11 tBit
- c)  Maximum Station Delay of Responders (max TSDR): 150 tBit
- d) Slot Time (TSL): 300 tBit
- e) Quiet Time (TQUI): 0 tBit
- f)  Setup Time (TSET): 1 tBit
- g) Time Target Rotation (TTR): 30000 tBit (20 ms)
- h) GAP Actualisation Factor (G): 10
- i)  Highest Station Address (HSA): 126
- j) Max Retry Limit (max\_retry\_limit): 1
- 6.1.1.3.1 Note: This allows for a maximum permissible line length (PROFIBUS length) of 200 m per segment and a maximum number of 32 stations when using cable type A. In case a greater length or more stations are required, repeaters can be used without changing the configuration.
- 6.1.1.3.2 Note:  PROFIBUS may also be used for other communications than the one between STM and ERTMS/ETCS on-board specified in this FFFIS STM.

## 6.1.2 Physical connection

- 6.1.2.1 The default physical medium shall be RS-485 twisted pair shielded copper cable.
- 6.1.2.2 The default connectors of the different equipments (ERTMS/ETCS on-board functions and  STMs)  shall  be  9-pin  female  D-SUB  and  cabling  according  to  PROFIBUS specifications.

## 6.1.3 Bus redundancy and retransmission

- 6.1.3.1 Retransmission is specified in [3]
- 6.1.3.2 Regarding bus redundancy, the STM and ERTMS/ETCS on-board shall have at least one bus interface each, and may have two interfaces.

© This document has been developed and released by UNISIG

<!-- image -->

- 6.1.3.3 In case STM and ERTMS/ETCS on-board do not have the same number of buses, only one bus shall be connected.
- 6.1.3.4 The dual bus configuration shall be managed by the 'Redundancy Supervisor' see Ref.: [3].

## 6.2 Safety

- 6.2.1.1 To  allow  communication  between  different  equipment  with  different  Safety  Integrity Levels  (SIL),  the  FFFIS  STM  shall  provide  communication  with  three  levels  of  safety protocol (SL):
- a) Safety Level 4 (SL 4)
- b) Safety Level 2 (SL 2)
- c)  Safety Level 0 (SL 0)
- 6.2.1.1.1 Justification: According to the requirements for Safety-related communication  in transmission  systems  (see  [8]),  an  equipment  with  no  or  a  low  Safety  Integrity  Level shall  not  masquerade  as  an  equipment  with  a  higher  Safety  Integrity  Level.  This requirement shall be fulfilled by using the defined Safety Levels.
- 6.2.1.1.2 Note: The three levels of safety are specified in [3] and [2].
- 6.2.1.2 No  equipment  shall  implement  any  Safety  Level  corresponding  to  a  higher  Safety Integrity Level (SIL).
- 6.2.1.3 ERTMS/ETCS  on-board  functions  shall  implement  all  the  safety  protocols  up  to  the Safety Level (SL) corresponding to the SIL of the function.

## 6.3 On-board Architecture

- 6.3.1.1 Each STM shall only have one physical bus address (Station/Node address) towards the ERTMS/ETCS on-board.
- 6.3.1.2 The ERTMS/ETCS on-board may use one or several physical bus addresses depending on its architecture.
- 6.3.1.3 An STM shall be able to handle one different physical address for each ERTMS/ETCS on-board function.
- 6.3.1.4 In case several STMs share the same physical address, each of them shall establish its own connection at Application Layer using different NID\_STMs.

## 6.4 Physical Addressing (Station/Nodes addresses)

- 6.4.1.1 The physical addresses shall be allocated according to the following table.

<!-- image -->

| Physical Address   | Device                               |
|--------------------|--------------------------------------|
| 2                  | STM Control Function                 |
| 0, 1, 2, 3 . . 19  | Other ERTMS/ETCS on-board functions  |
| 20 . . 49          | Unused by FFFIS STM                  |
| 50 . . 69          | STM configurable addresses range     |
| 70 . . 126         | STMs (NID_NTC+70)                    |
| 127                | Reserved for Broadcast and Multicast |

- 6.4.1.2 By default the Physical address of an STM shall be the NID\_NTC value + 70.
- 6.4.1.3 STM  configurable  addresses  range  shall  be  used  for  STMs  for  which  the  sum  of NID\_STM value +70 goes out of the Profibus physical address range
- 6.4.1.4 In case several STMs share the same physical address, the address value shall be the one of any of the supported STMs or a configurable physical address.
- 6.4.1.5 When a physical  address  in  the  STM  configurable  addresses  range  is  to  be  used,  it shall  be  possible  to  configure  the value of this physical address in order to solve any potential address conflicts.

## 6.5 Function Addressing

- 6.5.1.1 The FFFIS STM requires communication with different functions of the ERTMS/ETCS on-board as e. g. Odometer, DMI and Juridical Data.
- 6.5.1.2 The  FFFIS  STM  shall  use  Service  Access  Points  (SAPs)  to  support  communication between STMs and the different ERTMS/ETCS on-board functions.
- 6.5.1.3 All ERTMS/ETCS on-board functions shall have a defined fixed SAP.
- 6.5.1.3.1 Note: The SAP is fixed regardless of the chosen physical address.
- 6.5.1.4 For  transmitting  data  between  ERTMS/ETCS  on-board  and  the  STMs,  the  local (Source) Service Access Point (SSAP) and partner (Destination) Service Access Point (DSAP) shall have the same value.
- 6.5.1.5 The SAP number shall be defined according to the following table:

| Logical connections    | SAP# (binary)   |   # of SAP | Comment                                            |
|------------------------|-----------------|------------|----------------------------------------------------|
| DMI channel 3          | 000000          |          1 | Point-to-point                                     |
| DMI channel 4          | 000001          |          1 | Point-to-point                                     |
| Juridical Data         | 000010          |          1 | Point-to-point                                     |
| Reserved for FFFIS STM | 000011          |          1 | Not used (reserved for backward compatibility).    |
| DMI channel 1          | 000100          |          1 | Point-to-point                                     |
| DMI channel 2          | 000101          |          1 | Point-to-point                                     |
| Reserved for FFFIS STM | 000110          |          1 | Not used (reserved for backward compatibility).    |
| Reserved for FFFIS STM | 000111          |          1 | Reserved for future extension of the specification |
| Unused by FFFIS STM    | 001XXX          |          8 | To be defined by on-board implementers             |

<!-- image -->

| Logical connections    | SAP# (binary)                               |   # of SAP | Comment                                            |
|------------------------|---------------------------------------------|------------|----------------------------------------------------|
| Unused by FFFIS STM    | 01XXXX                                      |         16 | To be defined by on-board implementers             |
| Reference Time         | 100000                                      |          1 | Multicast                                          |
| STM Control            | 100001                                      |          1 | Point-to-point                                     |
| Reserved for FFFIS STM | 100010                                      |          1 | Not used (reserved for backward compatibility).    |
| Reserved for FFFIS STM | 100011                                      |          1 | Not used (reserved for backward compatibility).    |
| Reserved for FFFIS STM | 100100                                      |          1 | Not used (reserved for backward compatibility).    |
| Train Interface        | 100101                                      |          1 | Point-to-point                                     |
| Brake Interface        | 100110                                      |          1 | Point-to-point                                     |
| Odometer               | 100111                                      |          1 | Multicast for FFFIS STM version number X=4         |
| Unused by FFFIS STM    | 101XXX                                      |          8 | Defined by each implementer.                       |
| Reserved for FFFIS STM | 11XXXX Except 111111 reserved for broadcast |         15 | Reserved for future extension of the specification |
| Broadcast              | 111111                                      |          1 | Reserved due to PROFIBUS specification             |

- 6.5.1.6 There  shall  be  only  one  source  (one  station/node  address)  which  shall  transmit messages using the SAP reserved for the Reference Clock Function.
- 6.5.1.7 There  shall  be  only  one  source  (one  station/node  address)  which  shall  transmit messages using the SAP reserved for the Odometer Function.

## 6.6 Protocol Layers

- 6.6.1.1 The protocol layers are Application Layer (see [4]), Safe Time Layer (see [2]), Safe Link Layer (see [3]) and PROFIBUS FDL layer (see [5]).
- 6.6.1.2 The Safe Time Layer and Safe Link Layer together shall be considered as the Safety Layers.

Figure 2 - Application Data encapsulation by the layers in PROFIBUS telegram

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

Figure 3 - FFFIS STM Protocol Layers

<!-- image -->

<!-- image -->

## 7. CONNECTION MANAGEMENT AND VERSION CHECK

- 7.1 General  requirements  linked  to  the  opening  of  point-to-point connection between STM and ERTMS/ETCS on-board

## 7.1.1 Opening of the connection

- 7.1.1.1 A connection shall be considered as established when the version check is considered as completed and successful (see chapter 7.1.2).
- 7.1.1.2 The STM shall take the initiative to establish the connection.
- 7.1.1.3 When a STM has to establish a connection with an ERTMS/ETCS on-board function, and  fails to establish the connection  2  times,  it shall be  allowed  to  retry the establishment of connection after 10 seconds.

## 7.1.2 Check of version

- 7.1.2.1 Each time the STM opens a connection with any ERTMS/ETCS on-board function, the STM  shall  send  its  'FFFIS  STM  version  number'  to  this  ERTMS/ETCS  on-board function, followed by the STM state report information in the same application message.
- 7.1.2.2 When  receiving  the  'FFFIS  STM  version  number'  from  the  STM,  the  concerned ERTMS/ETCS on-board function shall check the version compatibility as follows:
- a) if the 'FFFIS STM version number X' from the STM is lower than the lowest 'FFFIS STM version number X' supported by the ERTMS/ETCS on-board equipment, the ERTMS/ETCS on-board function shall close the connection (final disconnection on Safety Layers).
- b) if the 'FFFIS STM version number X' from the STM is amongst the ones supported by the ERTMS/ETCS on-board equipment, the ERTMS/ETCS on-board function shall send  to  the  STM  the  highest  supported  FFFIS  STM  version  number  of  which  the version number X is equal to the one received from the STM. The ERTMS/ETCS onboard function shall be allowed to transmit application data to the STM.
- c)  if  the  'FFFIS  STM  version  number  X'  from  the  STM  is  greater  than  the  highest version  number  X  supported  by  the  ERTMS/ETCS  on-board  equipment,  the ERTMS/ETCS on-board function shall close the connection (final disconnection).
- 7.1.2.3 When receiving 'FFFIS STM version number' from ERTMS/ETCS on-board, the STM shall  check  the  version  compatibility.  If  it  is  compatible  with  the  'FFFIS  STM  version number'  of  the  STM,  then  the  version  check  is  considered  as  terminated  and successful.  The  STM  shall  be  allowed  to  transmit  further  application  data  to  the ERTMS/ETCS on-board function.
- 7.1.2.4 If  the  'FFFIS  STM  version  number'  of  the  ERTMS/ETCS  on-board  is  not  compatible with  the  'FFFIS  STM  version  number'  of  the  STM,  then  the  STM  shall  close  the connection (final disconnection) to the concerned ERTMS/ETCS on-board function.

<!-- image -->

## 7.1.3 Closing of the connection

- 7.1.3.1 Closing a connection on application layer shall be done by requesting the Safety Layers (see 6.6.1.2) to close the connection.

## 7.1.4 Connection Sequence Charts.

<!-- image -->

## Figure 4 Nominal connection establishment sequence chart

Figure 5  Bad version number disconnection sequence chart

<!-- image -->

## 7.2 General requirements linked to handling multicast connection

© This document has been developed and released by UNISIG

<!-- image -->

- 7.2.1.1 The  multicast  sender  shall  open  a  separate  connection  for  all  'FFFIS  STM  version numbers' defined in the Legal backward compatibility envelope (see table 16.3.1.1).
- 7.2.1.2 Note: For each multicast application connection (currently limited to  Odometer Function), the table 6.5.1.5 contains one SAP for each 'FFFIS STM version number'. This allows opening separate connections.
- 7.2.1.3 On each connection, the multicast sender shall transmit the corresponding 'FFFIS STM version number' over the FFFIS STM. The transmission shall be repeated to support restarting STMs.
- 7.2.1.4 When receiving 'FFFIS STM version number' from ERTMS/ETCS on-board, the STM shall check the version compatibility.
- 7.2.1.5 If  the  'FFFIS  STM  version  number'  of  the  ERTMS/ETCS  on-board  is  not  compatible with  the  'FFFIS  STM  version  number'  of  the  STM,  then  the  STM  shall  ignore  any information received from this multicast connection.

<!-- image -->

## 8. STM STATES

## 8.1 No Power (NP)

- 8.1.1.1 The NP state means that the STM is unpowered.

## 8.2 Power On (PO)

- 8.2.1.1 This state is the default state entered by the STM after the STM is switched on.
- 8.2.1.2 Once in PO state, the STM shall perform the synchronisation of the Safe Time Layer.
- 8.2.1.3 Once  in  PO  state,  the  STM  shall  establish  a  connection  with  the  ERTMS/ETCS  onboard STM Control Function.
- 8.2.1.4 When the STM has established the connection to the STM Control Function, the STM shall  send  a  'Specific  NTC  Data  Need'  information  to  the  STM  Control  Function indicating whether it needs or not Specific NTC Data.
- 8.2.1.5 Once the ERTMS/ETCS on-board has sent the bus addresses and safety levels of all available  ERTMS/ETCS  on-board  functions  (see  10.1.1.4),  it  shall  allow  STM  to establish connections with any of these functions.
- 8.2.1.6 Once the STM Control Function has sent the ETCS status data to an STM in PO state (see chapter 10.5.1.1), it shall allow this STM to request CO state.

## 8.3 Configuration (CO)

- 8.3.1.1 The  STM  CO  state  is  used  to  wait  until  all  configuration  data  between  STM  and ERTMS/ETCS on-board have been exchanged. 'Configuration data' means data that is necessary for the national operation, except Specific NTC Data.
- 8.3.1.2 Configuration data from ERTMS/ETCS on-board to STMs consists of:
- a) ETCS data (see chapter 10.4)
- b) Status / availability of the train interface FFFIS STM signals (TIU)
- c)  Status / availability of the brake interface FFFIS STM signals (BIU)
- d) Odometer performance parameters (see chapter 12.4)
- e) Brake performance parameters: Maximum time delay for the ERTMS/ETCS on-board to process the STM Emergency and the STM Service Brake commands. This is the time from receiving the brake command from the STM until the ETCS commands the brake.
- 8.3.1.2.1 Note: Configuration data has not necessarily to be sent in CO state. Some data could be sent in PO state.
- 8.3.1.2.2 Note:  The  brake  performance  parameter  can  be  used  by  the  STM  in  braking  curves calculation.

© This document has been developed and released by UNISIG

<!-- image -->

- 8.3.1.3 Once the transmission of configuration data is finished and the Specific NTC Data Entry procedure is started, if the STM does not require any Specific NTC Data, then the STM shall request Cold Standby state to the STM Control Function.
- 8.3.1.4 If an STM in Configuration State detects that the ERTMS/ETCS on-board is in the mode Non-Leading  or  Sleeping  and  has  received  all  the  configuration  data  except  for  the ETCS data, the STM shall request to go to Cold Standby state.
- 8.3.1.4.1 Justification:  This  allows  STM  operation  in  Non-Leading  or  Sleeping  in  which  ETCS Train Data is not available.
- 8.3.1.5 Once the transmission of configuration data is finished and the Specific NTC Data Entry procedure  is  started,  if  the  STM  does  require  any  Specific  NTC  Data,  then  the  STM shall request Data Entry state to the STM Control Function.
- 8.3.1.6 When an STM exits CO state, it shall have the possibility to close any connection except with STM Control Function.

## 8.4 Data Entry (DE)

- 8.4.1.1 The state DE is used by any STM that requires Specific NTC Data in order to have all the required national information for operating the train with the STM.
- 8.4.1.1.1 Note: This state is only entered once at the start up process of the STM.
- 8.4.1.2 In  the  state  DE,  the  Specific  NTC  Data  Entry  procedure  (see  chapter  10.7)  shall  be performed.
- 8.4.1.3 Once the Specific NTC Data Entry procedure is terminated, the STM shall request Cold Standby state to the STM Control Function.
- 8.4.1.4 Note:  The  Specific  NTC  Data  Entry  procedure  can  be  terminated  without  having received the Specific NTC Data (e.g. when the Specific NTC Data Entry procedure is skipped). However, the Cold Standby state is still requested in order to have the same system behaviour when the Specific NTC Data is invalid.

## 8.5 Cold Standby (CS)

- 8.5.1.1 Being in the state CS, the STM has been initialised, tested (if required), configured and is  in  possession  of  all  required  information  for  operating,  but  is  not  able  to  receive  a message from the trackside, because the reception is turned off.
- 8.5.1.1.1 Exception: Specific NTC Data could be invalid, see 10.7.3.3.

## 8.6 Hot Standby (HS)

- 8.6.1.1 Being in the state HS, the STM shall be able to process the information from or to the national trackside.
- 10.7.4.3 While a Specific NTC Data Entry is ongoing, the ERTMS/ETCS on-board shall indicate to the STM the end of its Specific NTC Data Entry procedure by sending the STOP flag when one of the following conditions is fulfilled:
- a) after having received the 'End of Specific NTC Data Entry' from the respective STM,
- b) at expiration of the timeout specified in 10.7.4.9 for the respective STM,
- c)  when the Train Data Entry procedure is aborted by the ERTMS/ETCS on-board for reasons not related to the STM interface
- d) the  Specific  NTC  Data  Entry  for  this  STM  has  been  skipped  by  the  driver  see 10.7.3.1.
- 10.7.4.3.1  Note: Reasons leading to the abortion of the Train Data entry procedure and not related to the STM interface can be e.g. the cab deactivation, the driver aborting the Train Data entry procedure,...

<!-- image -->

- 10.7.4.4 Note: ETCS Train Data is also sent without the START and STOP flags outside a Train Data entry procedure, see 10.4.1.7.
- 10.7.4.5 Once the STM has received the ETCS Train Data while its Specific NTC Data Entry is ongoing:
- a) If  the  STM  requires  Specific  NTC  Data,  the  STM shall send a 'Specific NTC Data Entry request' information to the ERTMS/ETCS on-board.
- b) If  the  STM  doesn't  require  Specific  NTC  Data,  the  STM  shall  send  an  'End  of Specific NTC Data Entry' information to the ERTMS/ETCS on-board.
- 10.7.4.6 After the ERTMS/ETCS on-board has received the Specific NTC Data Entry request, it shall  perform  the  Specific  NTC  Data  Entry/Validation  exchanges  with  the driver when the driver selects this Specific NTC Data Entry.
- 10.7.4.7 Once  the  Specific  NTC  Data  for  an  STM  has  been  validated  by  the  driver,  the ERTMS/ETCS on-board shall send the 'Specific NTC Data' to this STM.
- 10.7.4.8 When  the  STM  receives  the  Specific  NTC  Data,  it  checks  the  data  according  to  its national criteria. Depending on the check result:
- a) the STM shall send an 'End of Specific NTC Data Entry' if the checks are OK and the STM has all the requested data.
- b) the STM shall send again Specific NTC Data Entry request.
- 10.7.4.9 For  all  connected  STMs,  the  ERTMS/ETCS  on-board  shall  supervise  separately  a timeout of 10s (TrainDataEntry\_STM\_Response\_Timeout, see chapter 10.3.2.4, O16):
- a) from sending the ETCS Train Data by the ETCS while the Specific NTC Data Entry procedure is running, until the reception of a Specific NTC Data Entry request or the 'End of Specific NTC Data Entry' from the STM and
- b) from each sending Specific NTC Data by the ETCS until the reception of the Specific NTC Data Entry request or the 'End of Specific NTC Data Entry' from the STM.

<!-- image -->

## 10.7.5 Sequence diagrams for the Specific NTC Data Entry

Figure 6 - Specific NTC Data Entry performed

<!-- image -->

<!-- image -->

Figure 7 - Specific NTC Data Entry skipped for NTC B

<!-- image -->

<!-- image -->

Figure 8 - Specific NTC Data Entry aborted

<!-- image -->

## 10.8 Specific NTC Data View

10.8.1.1 This  procedure  shall  allow  the  driver  to  view  the  Specific  NTC  Data  View  values currently known by the STM.

- 10.8.1.2 When the Data View procedure is triggered, the ERTMS/ETCS on-board shall send to all available STMs a Request for Specific NTC Data View values.
- 10.8.1.3 Once the STM has received the ETCS Request for Specific NTC Data View values:
- a) If the STM requires Specific NTC Data View values to be displayed, the STM shall send those Specific NTC Data View values (labels and corresponding values) to the STM Control Function.
- b) If the STM doesn't require Specific NTC Data View values to be displayed, the STM shall send a 'No Specific NTC Data View values' to the ETCS STM Control Function.
- 10.8.1.4 When the ERTMS/ETCS on-board receives the Specific NTC Data View values, it shall present them to the driver.
- 10.8.1.5 For  all  connected  STMs,  the  ERTMS/ETCS  on-board  shall  supervise  separately  a timeout  of  10s  (TrainDataView\_STM\_Response\_Timeout,  see  chapter  10.3.2.4,  N16) from  sending  the  Request  for  Specific  NTC  Data  View  values  until  the  reception  of Specific NTC Data View values or the 'No Specific Data View values' information from the respective STM.

<!-- image -->

## 10.9 STM Test Procedure

- 10.9.1.1 The STM shall be allowed to send a Test Procedure Permission Request, including a Test Identity, to the STM Control Function.
- 10.9.1.2 Having received this Test Procedure Permission Request, the ERTMS/ETCS on-board shall grant Test Procedure Permission when technically suitable.
- 10.9.1.2.1  Note: the condition to grant this Test Procedure Permission is specific to ERTMS/ETCS on-board implementation and to the Test Identity requested by the STM.
- 10.9.1.3 Having received this  Test  Procedure  Permission,  the  STM shall perform the test  and then report the End of Test Procedure, including test result and optional text message.
- 10.9.1.3.1  Note: the way  the test result and text message  are  displayed is specific to ERTMS/ETCS on-board implementation.

## 10.10 Override

## 10.10.1 Introduction

- 10.10.1.1 This  Override  procedure  (Trip  Inhibition,  Pass  Stop  or  Pass  signal  at  danger)  is specified in order to provide an override for the active system as well as for the system to be activated without applying the brakes (e.g. trip) by both systems.
- 10.10.1.2 When Override is activated in the active system (ERTMS/ETCS on-board or STM), all on-board systems receive a notification. Each system can then activate and monitor its specific  Override  procedure  limits  (e.g.  time,  distance  and/or  reception  of  trackside information) and trip inhibition. Termination of this monitoring is done independently in each system.
- 10.10.1.3 After  a  level  transition,  the  activated  system  is  able  to  immediately  have  its  Override function active. It can then start to supervise the relevant speed for Override under the limits of the activated system according to its specific requirements. The limits may be considered from the location where driver requested Override.

## 10.10.2 Requirements

- 10.10.2.1 In addition to the conditions defined in [1], the ETCS Override status shall be activated when in level NTC, the ERTMS/ETCS on-board has received from the active STM the activation report of its own Override procedure.
- 10.10.2.2 The ETCS Override function shall be reset each time a new activation report is received from the active STM.
- 10.10.2.3 The ERTMS/ETCS on-board shall report its Override status (activated or deactivated):
- a) To any STM with an established connection to the STM Control Function whenever its Override status changes,
- b) To  any  connecting  STM  when  the  connection  to  the  STM  Control  Function  is established.

© This document has been developed and released by UNISIG

<!-- image -->

10.10.2.4 Note: If the Override function is active while in the Mode SN, no speed supervision is performed by the ERTMS/ETCS on-board and all connected STMs except for the active STM.

## 10.11 Transmission of ETCS airgap messages for STMs

- 10.11.1.1 When the ERTMS/ETCS on-board receives from an RBC or from a Balise Group as non-infill  information  airgap  data  to  be  transmitted  to  an  NTC,  the  data  shall  be transmitted by the STM Control Function to the STM associated to the Level NTC which NID\_NTC is contained in this airgap data.
- 10.11.1.1.1  Note: Airgap data received as infill information is not transmitted to STMs.
- 10.11.1.2 The  STM  Control  Function  shall  add  to  the  transmitted  airgap  data  the  odometer reading  of  the  balise  group  which  transmitted  the  airgap  message,  or  the  odometer reading of the LRBG of the message if it was received from RBC.
- 10.11.1.3 The odometer reading shall correspond to the estimated odometer value of the location reference of the balise group.

## 10.12 STM max speed and STM system speed/distance

## 10.12.1 After announcement, but before the transition to Level NTC X

- 10.12.1.1 When an 'STM max speed' (V\_STMMAX) from STM  X in HS state is accepted, the ERTMS/ETCS on-board includes the 'STM max speed' in the computation of the MRSP (see [1] 4.5.2) as a speed restriction that shall start at the level transition border.
- 10.12.1.2 When the ERTMS/ETCS on-board accepts a new 'STM max speed' (V\_STMMAX) from STM X, the ERTMS/ETCS on-board shall replace the previously  received  'STM  max speed' (V\_STMMAX) with the new value.
- 10.12.1.3 If the STM X connected or known as installed on-board (see 10.1.1.1) is not available, then the ERTMS/ETCS on-board shall consider that 'STM max speed' = 0.
- 10.12.1.3.1  Note: The purpose of the above requirement is to try to prevent the train to enter in a Level NTC area while this STM is not available.
- 10.12.1.4 When an 'STM system speed' (V\_STMSYS) together with an 'STM system distance' (D\_STMSYS) from STM X in HS state is accepted, the ERTMS/ETCS onboard includes the  'STM  system  speed'  (V\_STMSYS)  into  the  computation  of  the  MRSP  (see  [1] 4.5.2), as a new speed restriction that shall start at a location 'STM system distance' (D\_STMSYS) in rear of the level transition border and shall end at the level transition border.
- 10.12.1.5 When an ERTMS/ETCS on-board accepts a new 'STM system speed' (V\_STMSYS) and  'STM  system  distance'  (D\_STMSYS)  from  STM  X,  the  ERTMS/ETCS  on-board shall replace previously received 'STM system speed' (V\_STMSYS) and 'STM system distance' (D\_STMSYS) with the new value.

© This document has been developed and released by UNISIG

<!-- image -->

- 10.12.1.6 When the level transition announcement to level NTC X is deleted by the ERTMS/ETCS on-board:
- a) The 'STM system speed' (V\_STMSYS) shall be deleted and the supervision of the 'STM system speed' (V\_STMSYS) shall be stopped by the ERTMS/ETCS on-board;
- b) The  'STM  max  speed'  (V\_STMMAX)  shall  be  deleted  and  the  supervision  of  the 'STM max speed' (V\_STMMAX) shall be stopped by the ERTMS/ETCS on-board.
- 10.12.1.6.1  Note: when a new level transition to another level than NTC X is accepted, the previous one is deleted and replaced with this new one.
- 10.12.1.6.2  Note: when a level transition announcement to the same level NTC X is updated (i.e. with a new distance), the "STM system speed" and "STM max speed" are not deleted.

## 10.12.2 After the level transition to Level NTC X

- 10.12.2.1 Once the train has passed the level transition border, the ERTMS/ETCS on-board shall supervise the 'STM max speed' (V\_STMMAX) previously sent by the STM in HS state as  ceiling  speed  until  the  STM  DA  state  report  is  received  by  the  ERTMS/ETCS  onboard.
- 10.12.2.2 If the STM is considered to be in FA state by the ERTMS/ETCS on-board after the level transition border, then the ERTMS/ETCS on-board shall stop the supervision of 'STM max speed' (V\_STMMAX).
- 10.12.2.3 If,  for  any  reasons  (e.g.  reception  of  a  level  transition  order  or  a  manual  change  of level),  the  level  changes  to  another  level  than  NTC  X,  the  'STM  max  speed' (V\_STMMAX)  shall be deleted and the supervision of the 'STM  max  speed' (V\_STMMAX) shall be stopped by the ERTMS/ETCS on-board.

## 10.13 Validity of 'National Trip Procedure' information

- 10.13.1.1 The ERTMS/ETCS on-board shall consider that a National Trip Procedure is active if the 'National Trip Procedure' packet has been received within the last 10 seconds (see [1]).
- 10.13.1.2 Note:  if  the  National  Trip  Procedure  has  been  released  before  a  level  transition,  the ERTMS/ETCS on-board will consider it as still active for a maximum of 10 seconds after the reception of the information, but it is assumed that the level transition after the end of this National Trip Procedure won't happen within this time, as the train is at standstill.

## 10.14 Display of STM failure status

- 10.14.1.1 When an STM has reported FA state or is commanded to FA state, the ERTMS/ETCS on-board shall inform the driver about the failed status of the national system supported by this STM.
- 10.14.1.2 When at Start of Mission just after validation of ETCS Train Data an STM known by ERTMS/ETCS on-board configuration to be installed is not in CO, CS, HS or DA state and  this  STM  is  not  known  to  be  isolated  by  TIU  'NTC  isolation  status'  input  data,

© This document has been developed and released by UNISIG

<!-- image -->

ERTMS/ETCS on-board shall inform the driver about the  failed  status  of the national system supported by this STM.

## 10.15 Interface 'K' Antenna/BTM ID

10.15.1.1 If  the  ERTMS/ETCS  on-board  uses  alternative  1  of  interface  'K'  (see  [10]),  it  shall indicate to all KER (KVB, Ebicab, RSDD) STMs whether it can or not guarantee by its own  that  the  interface  'K'  data  is  coming  from  the  intended  Antenna/BTM,  when  the connection to the STM Control Function is established.

- 10.15.1.2 If  ERTMS/ETCS  on-board  cannot  guarantee  by  its  own  that  the  interface  'K'  data  is coming from the intended Antenna/BTM, the STM Control Function shall inform whether there is an active Antenna/BTM and, if so, which one:
- a)  To all connected KER STMs whenever this information changes,
- b)  To any KER STM when the connection to the STM Control Function is established.

10.15.1.3 Note: This information enables an STM using interface 'K' to fulfil a requirement of [10] asking to supervise that the interface 'K' information comes from the intended source.

## 10.16 BTM alarm data

10.16.1.1 The STM Control Function shall send the BTM alarm data consisting of the BTM alarm status and whether the antenna is within an announced Big Metal Mass track condition:

- a)  To all connected STMs whenever the BTM alarm status changes or whenever an announced Big Metal Mass track condition is entered or exited during a BTM alarm,
- b) To any STM when the connection to the STM Control Function is established.

10.16.1.2 Note: The ERTMS/ETCS on-board always sends this information over the FFFIS STM interface regardless the alarms are ignored according to [1] 3.12.1 and 3.15.7.

<!-- image -->

## 11. TIU AND BIU FUNCTIONS

- 11.1.1.1 The TIU Function shall transmit train interface inputs status / availability :
- a) To  any  STM  with  an  established  connection  to  the  TIU  Function  whenever  a  train interface inputs status / availability changes.
- b) To any connecting STM when the connection to the TIU Function is established.
- 11.1.1.1.1  The TIU  Function  shall transmit train interface  commands  configuration  to  any connecting STM when the connection to the TIU Function is established.
- 11.1.1.2 The BIU Function shall transmit the brake performance parameters to any connecting STM when the connection to the BIU Function is established.
- 11.1.1.3 The BIU Function shall transmit the brake status / availability :
- a) To any STM with an established connection to the BIU Function whenever a brake status / availability changes.
- b) To any connecting STM when the connection to the BIU Function is established.
- 11.1.1.4 When the service brake is commanded by an STM, the STM shall indicate in its request if  the  service  brake  shall  be  backed  up  automatically  by  the  ERTMS/ETCS  on-board with an Emergency Brake command if the service brake fails to be applied.
- 11.1.1.4.1  Note: If it is not the case, this has to be considered as an exception to [1].

<!-- image -->

## 12. ODOMETER FUNCTION

## 12.1 General

- 12.1.1.1 The FFFIS STM specifies the odometer information to be transmitted from ERTMS/ETCS on-board to all STMs via FFFIS STM.
- 12.1.1.2 The  ERTMS/ETCS on-board  shall  transmit  odometer  information  via  the  FFFIS  STM interface at regular intervals. This information shall include current values of estimated distance,  direction,  estimated  speed,  confidence  interval  of  measurement  of  distance (i.e. minimum and maximum distances) and confidence interval for speed (i.e. minimum and maximum speeds).
- 12.1.1.3 Every transmitted odometer information report shall be time stamped. The time base for timestamp shall be the Reference Time obtained from the Safe Time Layer, see 5.2.2. The time in the timestamp shall be the time when the odometer data were valid.
- 12.1.1.3.1  Justification: this time information allows an STM to extrapolate distance and speed to fit its algorithms and processing cycles.
- 12.1.1.4 Positive  movement  direction  is  defined  as  a  movements  in  the  forward  direction  in relation  to  cab  A.  It  shall  be  indicated  with  positive  speed  and  increasing  odometer distance values.
- 12.1.1.5 Negative  movement  direction  is  defined  as  movements  in  the  backwards  direction  in relation  to  cab  A.  It  shall  be  indicated  with  negative  speed  and  decreasing  odometer distance values.
- 12.1.1.5.1  Note:  Allocation  of  cab(s)  on  a  specific  train  is  a  pure  ERTMS/ETCS  on-board implementation issue.
- 12.1.1.6 The ERTMS/ETCS on-board shall not reset the odometer distance values as long as the ERTMS/ETCS on-board is powered-on.
- 12.1.1.6.1  Justification: The ETCS odometer information is used as a common reference within the FFFIS STM.
- 12.1.1.7 The  ERTMS/ETCS on-board  shall  transmit  odometer  configuration  data  (see  chapter 12.4) to the STMs.

## 12.2 Speed

- 12.2.1.1 Estimated speed, V\_Est, shall be the estimated speed as used by the ERTMS/ETCS on-board (also referred as the train speed in [1]).
- 12.2.1.2 Maximum  speed,  V\_Max, is  defined  as  the  most  positive  speed,  i.e.  the  highest possible  physical  speed  including  under-reading  amount,  in  case  of  movement  in positive  direction  (V\_Max  =  V\_Est  +  |V\_ura|).  For  movements  in  negative  direction

<!-- image -->

- V\_Max reports the lowest possible speed in absolute value, i.e. including over-reading amount (V\_Max = V\_Est + |V\_ora|).
- 12.2.1.3 Minimum  speed,  V\_Min, is  defined  as  the  most  negative  speed,  i.e.  the  lowest possible physical speed including over-reading amount, in case of movement in positive direction (V\_Min = V\_Est - |V\_ora|). For movements in negative direction V\_Min reports the  highest  possible  speed  in  absolute  value,  i.e.  including  under-reading  amount (V\_Min = V\_Est - |V\_ura|).

Figure 9 - Example of transmitted speed information

<!-- image -->

## 12.3 Distance

- 12.3.1.1 The estimated distance, D\_Est , shall be the most probable position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with reference to the vehicle position at the last reset of the odometry.
- 12.3.1.2 Note: For any train movement, the  most probable distance travelled between any two track positions can be computed as the difference between the measurement values of D\_Est at the two positions.
- 12.3.1.3 D\_Max is defined as the most positive position of the vehicle in the vehicle coordinate system  at  the  time  given  in  the  odometer  packet,  with  all  over-  and  under-reading amounts accumulated since the last reset of the odometry.
- 12.3.1.4 D\_Min is defined as the most negative position of the vehicle in the vehicle coordinate system  at  the  time  given  in  the  odometer  packet,  with  all  over-  and  under-reading amounts accumulated since the last reset of the odometry.
- 12.3.1.5 The confidence interval shall comply with the relevant requirements specified in [7].
- 12.3.1.6 The  resolution  part  of  an  odometer  report  shall  be  given  as  a  parameter  in  each odometer report from the ETCS Odometer Function. This allows for sensor technologies with varying resolution.

<!-- image -->

- 12.3.1.7 Note: The STM can then compute the maximum and minimum travelled distances at the current  vehicle  position  p2  with  regards  to  any  reference  location  p1  by  using  the resolution  information,  maximum  and  minimum  distances  at  the  these  locations,  as follows:

max\_distance(p1  p2) = max(D\_Res(p1), D\_Res(p2)) + D\_Max(p2) - D\_Max(p1)

min\_distance(p1  p2) = - max(D\_Res(p1), D\_Res(p2)) + D\_Min(p2) - D\_Min(p1)

- 12.3.1.8 The  distance  parameters  D\_Est,  D\_Max  and  D\_Min  are  allowed  to  wrap  when exceeding the value range. The parameters wrap individually.

## 12.4 Configuration information

- 12.4.1.1 The  ERTMS/ETCS  on-board  Odometer  Function  shall  transmit  performance  related information  (configuration  data)  over  the  FFFIS  STM.  The  transmission  shall  be repeated to support restarting STMs.
- 12.4.1.1.1  Note: The STM may use the performance-related information (e.g. ageing) to adjust its supervision, e.g. braking curves.
- 12.4.1.2 Typical  cycle  time,  T\_OdoCycle is  the  typical  time  for  the  odometer  cycle  time between each generating of new odometer data.
- 12.4.1.3 Note: The actual cycle time may well exceed T\_OdoCycle.
- 12.4.1.4 Maximum  production  delay  time,  T\_OdoMaxProd is  the  maximum  ageing  of odometer data from when the data was true until the data is available on the bus. This shall include clock synchronisation inaccuracy of the Odometer Function.
- 12.4.1.5 Note: The actual production delay time should not exceed T\_OdoMaxProd.

Figure 10 - Odometer cycle and delay times

<!-- image -->

<!-- image -->

## 13. DRIVER MACHINE INTERFACE FUNCTION

## 13.1 Introduction

- 13.1.1.1 The DMI Function allows the driver to directly interact with the ERTMS/ETCS on-board for what regards the national information related to the default window. That means that all  inputs  from  the  driver  to  the  ERTMS/ETCS  on-board  and  all  outputs  from  the ERTMS/ETCS  on-board  to  the  driver  in  the  default  window  are  controlled  by  this function.
- 13.1.1.2 The DMI Function shall provide the unified DMI and the customisable DMI services.
- 13.1.1.3 An STM designed for usage with a customisable DMI provides a set of configuration data for its default window as part of its product documentation as described in chapter 13.5.  The  ERTMS/ETCS on-board shall be configurable to store this  information  and serve  the  STM  DMI  requests  according  to  this  configuration.  The  customisable  DMI service shall be used, when configuration data for a customisable DMI layout are stored in the ERTMS/ETCS on-board for the NID\_STM of the STM.
- 13.1.1.4 An STM designed to use the unified DMI provides no configuration data as part of its product documentation. The unified DMI service shall be used, when no configuration data  for  a  customisable  DMI  layout  is  stored  in  the  ERTMS/ETCS  on-board  for  the NID\_STM of the STM.
- 13.1.1.5 Note: Unconfigurable parts of the DMI functions shall be handled in the same way by the unified and the customisable DMI services.

## 13.2 General requirements regarding DMI Function

- 13.2.1.1 The ERTMS/ETCS on-board shall only allow the active STM to communicate with the driver.
- 13.2.1.2 When the STM is no more active (see 4.1.1.3), the ERTMS/ETCS on-board shall delete all DMI objects controlled by this STM.
- 13.2.1.3 When  the  connection  between  an  STM  and  the  DMI  Function  is  disconnected,  the ERTMS/ETCS  on-board  shall  delete  all  the  DMI  objects  controlled  by  this  STM (including preliminary requests) after a timeout of 2 seconds.
- 13.2.1.3.1  Justification: The timeout of 2 seconds is to give the STM the chance to re-establish the connection.
- 13.2.1.4 When the  connection  between  the  active  STM  and  the  DMI  Function  is  lost  and  reestablished within the timeout of 2 seconds, the ERTMS/ETCS on-board shall delete all the  DMI  objects  controlled  by  the  STM  when  the  DMI  connection  to  the  STM  is established.

<!-- image -->

- 13.2.1.5 The ERTMS/ETCS on-board shall be able to receive and store preliminary request for DMI objects from an STM being in HS state and display them immediately after having received the DA state report.
- 13.2.1.5.1  Note:  The  sending  of  preliminary  request  is  to  allow  the  DMI  Function  to  prepare  in background the information to be presented to the driver once the STM switches to DA state. Therefore, the STM should send all DMI objects that needs to be displayed after the change to DA as preliminary DMI request.
- 13.2.1.6 When an STM reports PO, CS or FA, or is considered as failed, the ERTMS/ETCS onboard shall delete all preliminary requests for DMI objects from this STM.
- 13.2.1.7 If  the  ETCS  train  speed  is  configured  not  to  be  displayed  for  an  STM  while  the ERTMS/ETCS on-board is in SN mode (see chapter 13.5.1.1.7), the ERTMS/ETCS onboard shall inhibit the display of the ETCS train speed only once the DA state report is received from this STM by the STM Control Function.

## 13.3 DMI channels

- 13.3.1.1 The DMI Function shall be allowed to use up to four DMI channels. Each channel shall correspond to one connection.
- 13.3.1.2 At  most  one  DMI  channel  shall  be  active,  only  this  one  shall  be  used  for  the communication related to DMI objects with the DMI Function at application level.
- 13.3.1.3 Note 1: Connections corresponding to the inactive DMI channels may however remain open.
- 13.3.1.3.1  Note  2:  The  ERTMS/ETCS  on-board  may  report  a  DMI  channel  as  active  even  if  no interaction with the driver is possible, e.g. when no cab is active.
- 13.3.1.4 At the time the active DMI channel changes, the DMI Function shall delete all the DMI objects controlled by the STM.

## 13.4 DMI Objects

## 13.4.1 DMI object identities

- 13.4.1.1 The  DMI  objects  indicators  and  buttons  used  by  the  different  STMs  are  assigned  a unique object identity made of NID\_STM and Indicator/Button Identifier.
- 13.4.1.2 The  STM  Identity  is  implicitly  provided  by  the  STM  by  its  announced  NID\_STM  (and repeated in each message header according to the language).
- 13.4.1.3 The  Indicator/Button  Identifier  is  provided  by  the  STM  as  part  of  the  corresponding Indicator/Button request.
- 13.4.1.4 The  Indicator/Button  Identifier  is  used  by  the  STM  to  be  able  to  change  the  state  of objects  and  to  move  or  remove  them.  The  Button  Identifier  is  also  used  by  the ERTMS/ETCS on-board to transmit the button events to the STM. If the customisable DMI service is used, it is also used to define the properties of the object.

<!-- image -->

- 13.4.1.5 All  icons  (bitmap  symbols) used by the different STMs using a customisable DMI are assigned an icon identity made of NID\_STM and Icon Identifier.
- 13.4.1.6 An  Icon Identifier can  be  provided  by the STM  as  part  of  the  corresponding Indicator/Button request.
- 13.4.1.7 All  sounds  (wave  form  for  audible  information)  used  by  the  different  STMs  using  a customisable DMI are assigned a unique sound identity made of NID\_STM and Sound Identifier.
- 13.4.1.8 A  Sound  Identifier  can  be  provided  by  the  STM  as  part  of  the  corresponding  sound request.
- 13.4.1.9 For specifying the position of DMI objects, Position Identifiers are used.
- 13.4.1.10 If the unified DMI service is used, the Position Identifier specifies an area of the ETCS layout as defined in [9].
- 13.4.1.11 If  the  customisable  DMI  service  is  used,  the  Position  Identifier  and  the  NID\_STM  are used to define the position in cell coordinates and size as specified in the configuration data for this STM.

## 13.4.2 Text messages

- 13.4.2.1 The DMI Function shall display a text message when requested by the STM. The text message request shall consist of a Text Identifier, a string of text to be shown to the driver, a display attribute and a possible request for driver acknowledgement.
- 13.4.2.2 The  DMI  Function  shall  report  to  the  STM  the  acknowledgement  of  text  messages (which were required to be acknowledged) from the driver referencing the corresponding Text Identifier.
- 13.4.2.3 The DMI Function shall delete a text message when requested by the active STM. The request shall reference the Text Identifier of the text message to be deleted.
- 13.4.2.3.1  Note: The acknowledgement does not lead to the end of the display of a text message.
- 13.4.2.4 If the STM requests a text message with the same Text Identifier as a not yet deleted text  message, the ERTMS/ETCS on-board shall delete the original text message and display the new requested text message.
- 13.4.2.5 The display attribute specifies the colour of the text, its background colour, the flashing mode and the group of text messages.
- 13.4.2.6 The  flashing mode  specifies  if the slow, fast or no  flashing and  if  normal  or counterphase flashing shall be used.

## 13.4.3 Indicators

- 13.4.3.1 An Indicator is a DMI object for display of information without input.
- 13.4.3.2 The STM shall request the display of an Indicator by means of the following definition:

© This document has been developed and released by UNISIG

<!-- image -->

- a) its Indicator Identifier,
- b) an optional Icon Identifier,
- c)  an optional caption text,
- d) a Position Identifier,
- e) a display attribute.
6. 13.4.3.3 The Icon Identifier shall be used by the DMI Function in case of the customisable DMI service  to  retrieve  from  the  configuration  data  the  corresponding  icon  attached  to  an Indicator/Button object.
7. 13.4.3.4 The display attribute shall specify the background colour and the flashing mode for the whole Indicator and the display colour of the caption text.
8. 13.4.3.5 The  flashing mode  specifies  if the slow, fast or no  flashing and  if  normal  or counterphase flashing shall be used.

## 13.4.4 Buttons

- 13.4.4.1 Buttons are a pure functional extension of Indicators. All requirements of chapter 13.4.3 shall apply to Buttons, by replacing "Indicator" with "Button".
- 13.4.4.2 The extension is the transmission of Button events from the DMI Function to STM. The DMI Function shall make a distinction between push event (transition from Button not pressed to pressed state) and release event (opposite transition).
- 13.4.4.3 The DMI Function shall report  Button  push  and  release  events to the STM and shall timestamp those event reports to reflect the sequence of events.
- 13.4.4.4 The DMI Function shall use the Reference Time (see chapter 5.2.2) for timestamping the Button events reports.

## 13.4.5 Sounds

- 13.4.5.1 STM shall request a Sound by means of the following definition:
- a) an optional Sound Identifier,
- b) only in case of a unified DMI and a Sound to be generated, a sequence of segments defined by a duration and an associated frequency,

<!-- image -->

Freq.

Figure 11 : Example of sound definition

<!-- image -->

- c)  an indication if the Sound has to be repeated continuously or not or to be stopped.
2. 13.4.5.2 The  Sound  Identifier  shall  be  used  by  the  ERTMS/ETCS  on-board  in  case  of  the customisable  DMI  service  to  retrieve  from  the  configuration  data  the  corresponding sound.
3. 13.4.5.3 The Sound Identifier shall be used by the ERTMS/ETCS on-board in both DMI services to stop the generation of a Sound, if requested by the STM.
4. 13.4.5.4 The DMI Function shall be able to manage two STM requests for Sounds at the same time.
5. 13.4.5.4.1  Note: This will allow an STM  to request a long Sound  and a short  Sound simultaneously.

## 13.4.6 Supervision information

- 13.4.6.1 There shall be two sets of supervision information:
- a) Speed and distance values
- b) Colours and display modes
- 13.4.6.2 Speed and distance values consists of :
- a) Permitted Speed
- b) Target Speed
- c)  Target Distance
- d) Release Speed
- e) Intervention Speed
- 13.4.6.3 Colours and display modes consists of:
- a) Current train speed pointer

© This document has been developed and released by UNISIG

<!-- image -->

-  Colour
- b) Permitted Speed
-  Colour
-  Display mode: no display, bar only, hook only or hook and bar
- c)  Target Speed
-  Colour
-  Display mode: no display, bar only, hook only or hook and bar
- d) Target Distance
-  Display mode: no display, bar only, digital only or bar and digital
- e) Release Speed
-  Colour
-  Display mode: no display, bar only, digital only or bar and digital
- f)  Intervention Speed
-  Colour
-  Display mode: no display, display with normal bar width or display with wide bar width.
- 13.4.6.4 The DMI Function shall use the last received information for Current train speed pointer, Target  Speed,  Release  Speed,  Permitted  Speed,  Intervention  Speed  and  Target Distance.

## 13.5 Customisable DMI service

- 13.5.1.1 The configuration of the customisable DMI shall define the following data for each STM using the customisable DMI service:
- 13.5.1.1.1  The NID\_STM of the STM.
- 13.5.1.1.2  The list of Indicators defined for the STM with the following data for each Indicator:
- a) identifier (a number);
- b) font size (height in cells);
- c)  horizontal text-alignment (left, right or centred);
- d) vertical text-alignment (upper part, lower part or centred).
- 13.5.1.1.3  Two lists  of Indicator positions (one list for soft key technology and one list for touch screen technology) defined for the STM, and for each Indicator position:
- a) identifier (a number);
- b) x:y offset of the upper left corner in cells;
- c)  x:y size of the area in cells.
- 13.5.1.1.4  The list of Buttons defined for the STM with the following data for each Button:

© This document has been developed and released by UNISIG

<!-- image -->

- a) identifier (a number);
- b) font size (height in cells);
- c)  horizontal text-alignment (left, right or centred);
- d) vertical text-alignment (upper part, lower part or centred).
5. 13.5.1.1.5  Two  lists  of  Button  positions  (one  list  for  soft  key  technology  and  one  list  for  touch screen technology) defined for the STM and, for each Button position:
- a) identifier (a number);
- b) x:y offset of the upper left corner in cells;
- c)  x:y size of the area in cells;
- d) linked soft key (for soft key technology).
10. 13.5.1.1.6  The list of Icons defined for the STM and, for each Icon:
- a) identifier (a number);
- b) bitmap,  as  RGB  bitmap  file  (according  to  Microsoft  BMP  file  format);  Pixels  in  the bitmap files shall be understood as cells.
- c)  display of text upon icon: yes/no.
14. 13.5.1.1.7  ETCS speed and distance supervision
- a) For speed and distance supervision display in speed dial as for ETCS in area B0-B2, B6 and A2-A3 (applicable as long as the STM is active):
- b) Yes/No; 'Yes' means that the ETCS train speed display is re-used as such together with the supervision information as specified in 13.4.6. 'No' means that there is no display of speed and distance supervision in the ETCS way.
- c)  if Yes: speed dial range (0-140/180/250/400 km/h or same range as ETCS).
18. 13.5.1.1.8  Options for flashing of Indicators and Buttons (additionally to flashing mode):
- a) the frequency for slow and fast flashing;
- b) the flashing style either as 'yellow frame' or as 'whole area'.
21. 13.5.1.1.9  The list of Sounds defined for the STM and, for each sound, its Sound definition.
- a) identifier (a number);
- b) sound, as WAV file (according to Microsoft WAV file format);
24. 13.5.1.1.10  Moved areas of the ETCS layout:
- a) If  a  STM  needs  partially  or  totally  the  cells  used  by  an  area  defined  in  the  ETCS layout and in which ETCS DMI objects are displayed in level NTC modes SN or NL, the  ETCS  objects  displayed  in  it  must  be  moved  somewhere  else  on  the  national layout.  Therefore  it  shall  be  possible  to  specify  a  changed  location  for  moving  the following  ETCS  areas  and  their  related  ETCS  objects.  For  buttons  also  the  new related soft key (F1-F5) must be defined:

<!-- image -->

-  Areas F1-F5 for the buttons for selecting the main, override, data view, special or settings window;
-  Area A4 for the adhesion 'slippery rail';
-  Areas B7 and C8 for the ETCS mode and level display;
-  Area C1 for the mode/level acknowledgements;
-  Area C7 for the Override status indication;
-  Area C9 for the brake indication;
-  Area E1 for safe radio connection indication;
-  Area G13 for local time
- b) The new location shall be specified by a new x:y position in cells.
- c)  The moved areas shall have the same size as the original ETCS areas.

## 13.5.1.2 Recapping Table with configuration data for customisable DMI:

| Description                                                      | Multiplicity                | Range and unit                  |
|------------------------------------------------------------------|-----------------------------|---------------------------------|
| NID_STM of the STM                                               | 1                           | 0-254                           |
| Number of Indicators                                             | 1                           | 0-255                           |
| Indicator id (i)                                                 | For each Indicator          | 1-255                           |
| Font size (i)                                                    | For each Indicator          | height in cells (8-60)          |
| Horizontal text alignment (i)                                    | For each Indicator          | Left , right, centred           |
| Vertical text alignment (i)                                      | For each Indicator          | upper part, lower part, centred |
| Number of Indicator positions in case of touch screen technology | 1                           | 0-24                            |
| Indicator position id (i)                                        | For each Indicator position | 1-24                            |
| X Offset of the upper left corner (i)                            | For each Indicator position | 0-639 [cells]                   |
| Y Offset of the upper left corner (i)                            | For each Indicator position | 0-479 [cells]                   |
| Horizontal size (i)                                              | For each Indicator position | 8-640 [cells]                   |
| Vertical size (i)                                                | For each Indicator position | 8-480 [cells]                   |
| Number of Indicator positions in case of soft key technology     | 1                           | 0-24                            |
| Indicator position id (i)                                        | For each Indicator position | 1-24                            |
| X Offset of the upper left corner (i)                            | For each Indicator position | 0-639 [cells]                   |
| Y Offset of the upper left corner (i)                            | For each Indicator position | 0-479 [cells]                   |
| Horizontal size (i)                                              | For each Indicator position | 8-640 [cells]                   |
| Vertical size (i)                                                | For each Indicator position | 8-480 [cells]                   |
| Number of Buttons                                                | 1                           | 0-255                           |
| Button id (i)                                                    | For each Button             | 1-255                           |

© This document has been developed and released by UNISIG

<!-- image -->

| Font size (i)                                                 | For each Button          | height in cells (8-60)                    |
|---------------------------------------------------------------|--------------------------|-------------------------------------------|
| Horizontal text alignment (i)                                 | For each Button          | Left , right, centred                     |
| Vertical text alignment (i)                                   | For each Button          | upper part, lower part, centred           |
| Number of Button positions in case of touch screen technology | 1                        | 0-24                                      |
| Button position id for touch screen (i)                       | For each Button position | 1-24                                      |
| X Offset of the upper left corner (i)                         | For each Button position | 0-639 [cells]                             |
| Y Offset of the upper left corner (i)                         | For each Button position | 0-479 [cells]                             |
| Horizontal size (i)                                           | For each Button position | 8-640 [cells]                             |
| Vertical size (i)                                             | For each Button position | 8-480 [cells]                             |
| Number of Button positions in case of soft key technology     | 1                        | 0-24                                      |
| Button position id for soft key (i)                           | For each Button position | 1-24                                      |
| X Offset of the upper left corner (i)                         | For each Button position | 0-639 [cells]                             |
| Y Offset of the upper left corner (i)                         | For each Button position | 0-479 [cells]                             |
| Horizontal size (i)                                           | For each Button position | 8-640 [cells]                             |
| Vertical size (i)                                             | For each Button position | 8-480 [cells]                             |
| Linked soft key                                               | For each Button position | F1-F10,H2-H4                              |
| Number of Icons                                               | 1                        | 0-255                                     |
| Icon id (i)                                                   | For each Icon            | 1-255                                     |
| Icon (i)                                                      | For each Icon            | Bitmap file                               |
| Display text upon icon                                        | For each Icon            | Yes/No                                    |
| ETCS speed and distance supervision                           | 1                        | Yes/No                                    |
| ETCS speed dial range                                         | 1                        | No, same as ETCS, 140, 180, 250, 400 km/h |
| Slow flashing frequency for Buttons and Indicators            | 1                        | (0,5 - 8) Hz                              |
| Fast flashing frequency for Buttons and Indicators            | 1                        | (0,5 - 8) Hz                              |
| Flashing style                                                | 1                        | Frame, whole area                         |
| Number of Sounds                                              | 1                        | 0-255                                     |
| Sound id (i)                                                  | For each Sound           | 1-255                                     |
| sound (i)                                                     | For each Sound           | Wave file                                 |
| Number of moved areas of the ETCS layout                      | 1                        | 0 - 13                                    |
| ETCS area of moved element(i)                                 | For each moved element   | A4, B7, C1, C7-C9, E1, F1-F5, G13         |

© This document has been developed and released by UNISIG

<!-- image -->

| X Offset of the upper left corner (i) of new location   | For each moved element   | 0-639 [cells]   |
|---------------------------------------------------------|--------------------------|-----------------|
| Y Offset of the upper left corner (i) of new location   | For each moved element   | 0-479 [cells]   |
| Soft key Identifier (i)                                 | For each moved button    | F1-F10, H2-H4   |

<!-- image -->

## 14. JURIDICAL DATA FUNCTION

- 14.1.1.1 The ERTMS/ETCS on-board equipment shall be able to receive and forward national juridical data to the On-Board Recording Device.
- 14.1.1.2 The  STM  shall  use  the  Reference  Time  (see  chapter  5.2.2)  for  time  stamping  the juridical data sent to the ERTMS/ETCS on-board.
- 14.1.1.3 The time stamp of the juridical data shall represent the time the sent event occurred.
- 14.1.1.3.1  Note: This is in order to respect the event chronology.

<!-- image -->

## 15. LIMITATIONS

## 15.1 Limitations related to DMI

- 15.1.1.1 The maximum number of characters (coded in UTF-8 by 1 or 2 bytes) to display shall be
- a) 40 characters for text messages in text message request.
- b) 12 characters for button and indicator caption text in button and indicator requests
- 15.1.1.2 The allowed text font height range for the configurable elements of the DMI layout of an STM using the customisable DMI service shall be from 8 to 60 cells.
- 15.1.1.3 The allowed range for the frequencies for slow and fast flashing for an STM using the customisable DMI service is 0,5 - 8 Hz.
- 15.1.1.4 The ERTMS/ETCS on-board DMI Function shall be able to store at least 10 STM text messages.

## 15.2 Limitations related to Specific NTC Data Entry/Data View

- 15.2.1.1 The number of Data Identifiers within one 'Specific NTC Data Entry request' shall be limited to 15 Data Identifiers.
- 15.2.1.2 The number of Data Identifiers within one 'Specific NTC Data values' shall be limited to 15 Data Identifiers.
- 15.2.1.3 The  number  of  Data  Identifiers  within  one  'Specific  NTC  Data  View  values'  shall  be limited to 15 Data Identifiers.
- 15.2.1.4 The maximum number of characters (coded in UTF-8 by 1 or 2 bytes) shall be:
- a) 20 characters for data labels in 'Specific NTC Data Entry request' and 'Specific NTC Data View values'
- b) 10  characters  for  data  values  in  'Specific  NTC  Data  Entry  request'  and  'Specific NTC Data values'
- c)  10 characters for data view values in 'Specific NTC Data View values'

<!-- image -->

## 16. VERSION MANAGEMENT

## 16.1 Introduction

- 16.1.1.1 The  version  of  the  FFFIS  STM  defines  unambiguously  the  mandatory  interface functions  that  ensure  technical  exchangeability  between  ERTMS/ETCS  on-board  and STM.
- 16.1.1.2 During the life time of the FFFIS STM there may be several versions of the FFFIS STM.
- 16.1.1.3 The objective of this section is to define requirements applicable to ERTMS/ETCS onboard  equipment  and  to  STM,  when  different  versions  of  the  FFFIS  STM  have  been defined.

## 16.2 Identification/evolution of the versions

- 16.2.1.1 The evolution of the versions of the FFFIS STM shall be sequential, i. e. there shall only be a direct upgrade of an existing version and no branch is accepted.
- 16.2.1.2 The version of the FFFIS STM shall be identified by a number which complies with the following:
- a) Each Version Number will have the following format: X.Y, where X and Y are any number between 0 and 255 (examples: 2.0, 3.0, 4.2).
- b) The first number (X) distinguishes not compatible versions.
- c)  The second number (Y) indicates compatibility within a version X.
- d) If the first number of two versions is the same, that indicates that those versions are compatible, independently of the second number (e. g. version 4.5 is compatible with 4.3, 4.14).
- 16.2.1.3 The 'FFFIS STM version number X or Y' is incremented only when the functionality of the FFFIS STM changes.

## 16.3 Version numbers

- 16.3.1.1 Table of FFFIS STM version numbers

<!-- image -->

| FFFIS STM Version Number                       | Supported by ERTMS/ETCS on- board equipment   | Remark                                                                                              |
|------------------------------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------------|
| X=2, Y=0, Z=0                                  | Supplier specific                             | Initial Version, introduced in SUBSET-035 v2.0.0.                                                   |
| X=3, Y=0, Z                                    | Supplier specific                             | Introduced in SUBSET-035 v2.1.1 (General revision of the FFFIS STM) Z is vendor specific            |
| Legal backward compatibility envelope X=4, Y=0 | Yes                                           | Introduced in SUBSET-035 v3.x.0 (General revision of the FFFIS STM in the frame of ETCS baseline 3) |

- 16.3.1.2 The STM shall support and send one and only one 'FFFIS STM version number', which is  the  highest  one  amongst  those  included  in  the  'legal  backward  compatibility envelope', as defined in table 16.3.1.1.
- 16.3.1.3 The ERTMS/ETCS on-board equipment shall support any of the 'FFFIS STM version numbers X' included in the 'legal backward compatibility envelope', as defined in table 16.3.1.1.
- 16.3.1.4 All  nodes/functions  of  the  ERTMS/ETCS  on-board  equipment  shall  support  the  same 'FFFIS STM version numbers' and shall therefore send the same 'FFFIS STM version number', when opening a connection with a given STM (see section 7.1.2).
- 16.3.1.5 When a connection is successfully established with a 'FFFIS STM version number X' lower  than  the  highest  STM  version  numbers  X  included  in  the  'legal  backward compatibility envelope', the ERTMS/ETCS  on-board  equipment shall apply the corresponding  set  of  requirements  as  per  section  16.4,  in  order  to  ensure  backward compatibility between the ERTMS/ETCS on-board equipment and the STM.

## 16.4 Management of older FFFIS STM versions by ERTMS/ETCS onboard

- 16.4.1.1 The 'FFFIS STM version number' introduced in this version of the SUBSET-035 is the starting point of the 'legal backward compatibility envelope', which means that whether an ERTMS/ETCS on-board equipment supports a 'FFFIS STM version number X' lower than  the  one  introduced  in  this  version  of  the  SUBSET-035  is  supplier  specific  and outside the scope of this document.

<!-- image -->

17. ANNEX A: SYSTEM DIAGRAMS LINKED TO THE LEVEL TRANSITIONS WITH  STMS (INFORMATIVE)

## 17.1 ETCS  NTC

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.2 ETCS  NTC (Trip Mode)

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.3 ETCS  NTC (NL/SL)

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.4 NTC  ETCS

© This document has been developed and released by UNISIG

<!-- image -->

<!-- image -->

## 17.5 NTC  ETCS (National Trip Procedure)

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.6 NTC  ETCS (NL/SL)

<!-- image -->

<!-- image -->

## 17.7 NTC X  NTC Y

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.8 NTC X  NTC Y (NL/SL)

<!-- image -->

© This document has been developed and released by UNISIG

<!-- image -->

## 17.9 Power On in Level NTC (SoM)

<!-- image -->

After the event E30 of the "Start of Mission" procedure (the driver acknowledges the SN mode) - the mode changes from SB to SN, - the standstill supervision of the ETCS On-board ends, and - the access to the ETCS resources is allowed for the STM.

<!-- image -->

## 17.10 Power On in Level NTC (NL)

<!-- image -->

<!-- image -->

## 17.11 Power On in Level NTC (SL)

<!-- image -->

<!-- image -->

## 18. ANNEX B : TRAIN DATA ENTRY PROCEDURE (INFORMATIVE)

Figure 12 - Train Data Entry procedure

<!-- image -->

<!-- image -->

© This document has been developed and released by UNISIG

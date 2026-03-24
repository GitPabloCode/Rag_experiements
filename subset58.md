
## 3. SCOPE

- 3.1.1.1 The  FFFIS  STM  Application  Layer  specifies  data  formats  that  shall  be  used  in  the communication  between  Specific  Transmission  Module  STM  and  ERTMS/ETCS  onboard.
- 3.1.1.2 The boundary to lower layers is the Safe Time Layer.
- 3.1.1.3 The  boundary  to  higher  layer  is  the  application  processes  within  the  STM  and  the ERTMS/ETCS on-board.
- 3.1.1.4 The scope of this document is the Application Layer only.
- 3.1.1.5 The  transmitted  message  is  embedded  in  a  safety  protocol  structure  as  defined  by Safe Time Layer and Safe Link Layer. (See [5] and [6]).

Figure 1: FFFIS STM Layers

<!-- image -->

<!-- image -->

## 4. INTRODUCTION

## 4.1 References

| Ref. N°   | Document Reference   | Title                                                                                                            |
|-----------|----------------------|------------------------------------------------------------------------------------------------------------------|
| [1]       | SUBSET-026           | System Requirements Specification                                                                                |
| [2]       | SUBSET-027           | FIS Juridical Recording                                                                                          |
| [3]       | SUBSET-034           | Train Interface FIS                                                                                              |
| [4]       | SUBSET-035           | Specific Transmision Module FFFIS                                                                                |
| [5]       | SUBSET-056           | STM FFFIS Safe Time Layer                                                                                        |
| [6]       | SUBSET-057           | STM FFFIS Safe Link Layer                                                                                        |
| [7]       | SUBSET-059           | Performance requirements for STMs                                                                                |
| [8]       | ISO 639-1:2002(E/F)  | Codes for the representation of names of languages-Part 1: Alpha-2 Code                                          |
| [9]       | ISO 10646 Annex R    | Information technology -Universal Multiple-Octet Coded Character Set (UCS) - UCS Transformation Format 8 (UTF-8) |
| [10]      | ERA_ERTMS_015560     | ETCS Driver Machine interface                                                                                    |

© This document has been developed and released by UNISIG

<!-- image -->

## 5. INTENTIONALLY DELETED

© This document has been developed and released by UNISIG

<!-- image -->

## 6. COMPONENTS OF FFFIS STM LANGUAGE

## 6.1.1 Introduction

- 6.1.1.1 The FFFIS STM language is used for transmitting information over the Profibus link between the STM and the ERTMS/ETCS on-board functions.
- 6.1.1.2 The FFFIS STM language is based on variables, packets, and messages (variables are described in §6.1.2, packets are described in §6.1.3, and messages are described in §6.1.3.18).

## 6.1.1.2.1 Intentionally deleted

Figure 2: Application message detailed structure

| Application message   | Message Header                                       | NID_STM                         |
|-----------------------|------------------------------------------------------|---------------------------------|
| Application message   | Message Header                                       | L_MESSAGE                       |
| Application message   | First Packet                                         | NID_PACKET                      |
| Application message   | First Packet                                         | L_PACKET                        |
| Application message   | First Packet                                         | Other variables in First Packet |
| Application message   | . Other packets in application message if any .      |                                 |
| Application message   | Packet-N last data packet if different from Packet-1 | NID_PACKET                      |
| Application message   | Packet-N last data packet if different from Packet-1 | L_PACKET                        |
| Application message   | Packet-N last data packet if different from Packet-1 | Other variables in Packet       |
| Application message   | Padding bits                                         | 0 to 7 bits                     |

## 6.1.2 Definition of Variables and rules for variable coding

- 6.1.2.1 Variables shall be used to encode single data values. Variables cannot be splitted in minor units. The whole variable has one type (meaning).
- 6.1.2.2 Variables  may  have  special  values,  which  are  related  to  the  basic  meaning  of  the variable.
- 6.1.2.3 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 6.1.2.4 Intentionally deleted

- 6.1.2.5 Names  of  variables  are  unique.  A  variable  is  used  in  context  with  the  meaning  as described  in  the  variable  definition.  Variables  with  different  meanings  have  different names.
- 6.1.2.6 Signed values shall be encoded as 2's complement.
- 6.1.2.7 One bit variables (Boolean) shall always use 0 for false and 1 for true.
- 6.1.2.8 Offsets  for  numerical  values  shall  be  avoided  (0  shall  be  used  for  0,  1  for  1,  etc.) except where justified.
- 6.1.2.9 When transmitting, the most significant bit must be transmitted first.
- 6.1.2.10 All Variables have one of the following prefixes:
- 6.1.2.11 Length of variables is given in bits, unless otherwise stated.
- 6.1.2.12 Intentionally deleted
- 6.1.2.13 Reserved values and spare values for variables shall not be used.

- A\_ Acceleration

- D\_ Distance

- G\_ Gradient

- L\_

Length

- M\_ Miscellaneous

- N\_ Number

NC\_

Class Number

NID\_

Identity Number

- Q\_

Qualifier

T\_

Time/Date

V\_

Speed

- X\_ Text

## 6.1.3 Definition of Packets and rules for packets handling

- 6.1.3.1 Packets  are  multiple  variables  grouped  into  a  single  unit,  with  a  defined  internal structure.
- 6.1.3.2 This structure consists of a unique packet number, the length of the packet in bits and an  information  section  containing  a  defined  set  of  variables.  The  packet  structure  is defined as follows:

© This document has been developed and released by UNISIG

<!-- image -->

| Description   | This is the format of packets when transmitted over FFFIS STM.   | This is the format of packets when transmitted over FFFIS STM.   | This is the format of packets when transmitted over FFFIS STM.                                                                                                                                                                      |
|---------------|------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Content       | Variable                                                         | Length                                                           | Comment                                                                                                                                                                                                                             |
|               | NID_PACKET                                                       | 8                                                                | Packet identifier                                                                                                                                                                                                                   |
|               | L_PACKET                                                         | 13                                                               | Packet length                                                                                                                                                                                                                       |
|               | Q_SCALE                                                          | 2                                                                | Specifies which distance scale is used for all distance information within the packet. There is no Q_SCALE variable in packets, which do not contain distance information in a variable, which requires the information in Q_SCALE. |
|               | Other variables in packet if any                                 | N                                                                | Refer to packet definition in §7                                                                                                                                                                                                    |

- 6.1.3.3 The data element transmission order shall respect the order of data elements listed in the packet definition (from top to bottom).
- 6.1.3.4 The packet length (number of bits) shall be the length in bits of the whole packet. It shall take into account the following variables NID\_PACKET and L\_PACKET plus all other packet variables length as well as iterations for its value computation.
- 6.1.3.5 All currently not defined packet identifiers are reserved for future use. All future packet definitions shall follow the above-defined structure.
- 6.1.3.6 The sender of a packet shall ensure that the packet length will fit within one message.
- 6.1.3.7 The variable N\_ITER in a packet shall specify the number of iterations of a variable or group of variables, which follow.
- 6.1.3.8 If N\_ITER is 0 then no variable(s) which belong to the iteration given by N\_ITER shall follow.
- 6.1.3.9 The variable N\_LITER in a packet shall specify the number of iterations of a variable or group of variables, which follow.
- 6.1.3.10 If  N\_LITER  is  0  then  no  variable(s)  which  belong  to  the  iteration  given  by  N\_LITER shall follow.
- 6.1.3.11 Two nested levels of iterations shall be possible.
- 6.1.3.12 The variable L\_CAPTION in a packet shall specify the number of bytes in a data label, button label, or indicator label.
- 6.1.3.13 The variable L\_VALUE in a packet shall specify the number of bytes in a data value.

<!-- image -->

- 6.1.3.14 If L\_VALUE is 0 then no variable(s) for characters shall follow.
- 6.1.3.15 The variable L\_TEXT in a packet shall specify the number of bytes in a text string.
- 6.1.3.16 If L\_TEXT is 0 then no variable(s) for characters shall follow.
- 6.1.3.17 If,  depending on the value of a previous qualifier variable in the packet, a variable is optional, it is written indented in the packet definition.
- 6.1.3.18 If  the full ETCS packet 44 to transmit through packet STM-45 is not composed of an integer  number  of  bytes,  padding  shall  be  added  at  the  end  of  the  last  iteration  of M\_DATA(k) within this packet.

## 6.1.4 Definition of a message and rules for messages handling

- 6.1.4.1 A message is the whole application data transmitted at a given time on the interface between an ERTMS/ETCS on-board function and an STM or between an STM and an ERTMS/ETCS on-board function.
- 6.1.4.2 The  message  shall  have  the  format  as  defined  in  Figure  2:  Application  message detailed structure.
- 6.1.4.3 The data element transmission order shall respect the order of data elements listed in the message format (from top to bottom).
- 6.1.4.4 The sender of messages shall transmit the messages in a chronological way. The first transmitted message shall be the oldest.
- 6.1.4.5 Messages belonging to the same ERTMS/ETCS on-board function shall be treated by the receiver in the order of their reception.
- 6.1.4.6 The  message  header  shall  be  composed  of  the  NID\_STM  and  the  L\_MESSAGE variables.
- 6.1.4.7 The NID\_STM in the message header shall indicate the STM, which is the receiver or transmitter of the message.
- 6.1.4.8 The message header shall be part of the message at every transmission.
- 6.1.4.9 The message header shall be the same for all connections to ERTMS/ETCS on-board functions in both directions (from STM  to ERTMS/ETCS  function and from ERTMS/ETCS function to STM).
- 6.1.4.10 The Message Body shall consist of one or many packets.
- 6.1.4.11 It  shall  be  forbidden  to  send  more  instances  of  the  same  packet  type  in  the  same message.
- 6.1.4.11.1  Exception  1:  It  shall  be  possible  that  a  message  contains  several  ETCS  airgap messages for STM (packet STM-45).

© This document has been developed and released by UNISIG

<!-- image -->

- 6.1.4.11.2  Exception  2:  It  shall  be  possible  that  a  message  contains  several  'Text  message' (packet STM-38)
- 6.1.4.11.3  Exception 3: It shall be possible that a message contains several 'Delete text message' (packet STM-39)
- 6.1.4.11.4  Intentionally deleted
- 6.1.4.11.5  Intentionally deleted
- 6.1.4.11.6  Exception 4: It shall be possible that a message contains several STM information to Juridical Data Function (packet STM-161)
- 6.1.4.11.7  Intentionally deleted
- 6.1.4.12 Intentionally deleted
- 6.1.4.13 The receiver of a message shall process the packets of this message in a way that the result  is  the  same  as  if  each  packet  has  been  processed  separately  in the  received order.
- 6.1.4.14 Packets  within  a  message  depend  on  what  has  to  be  transmitted  according  to  the requirements in [4].
- 6.1.4.15 The message shall be completed by arbitrary padding bits to have the whole message length to be byte aligned for transmission through the safety layers. (See [5] and [6]).
- 6.1.4.16 Transmission  of  non  standard  packets  (i.e.  packets  which  are  not  described  in  this document, but whose numbers are within the allocated range of non standard packets, see  NID\_PACKET  definition):  in  case  a  message  includes  such  non  standard packet(s) unknown to the receiver, the non standard packet(s) shall be ignored and the message shall not be rejected.

<!-- image -->

## 7. PACKET DEFINITIONS

## 7.1 Packets related to all on-board functions (ETCS+STM)

## 7.1.1 Packet STM-1 STM/ETCS function version number

| Subset-035 Ref.           | §.7.1, 7.1.2.1, 7.1.2.2, 7.1.2.3, 7.1.2.4, 8.2.1.3, 16.3                                                                                                                                      | §.7.1, 7.1.2.1, 7.1.2.2, 7.1.2.3, 7.1.2.4, 8.2.1.3, 16.3                                                                                                                                      | §.7.1, 7.1.2.1, 7.1.2.2, 7.1.2.3, 7.1.2.4, 8.2.1.3, 16.3                                                                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA, FA                                                                                                                                                                    | PO, CO, DE, CS, HS, DA, FA                                                                                                                                                                    | PO, CO, DE, CS, HS, DA, FA                                                                                                                                                                    |
| Description               | This packet contains implicitly the connection request from the STM or the connection confirmation from the ERTMS/ETCS on-board function and provide also FFFIS STM version number for check. | This packet contains implicitly the connection request from the STM or the connection confirmation from the ERTMS/ETCS on-board function and provide also FFFIS STM version number for check. | This packet contains implicitly the connection request from the STM or the connection confirmation from the ERTMS/ETCS on-board function and provide also FFFIS STM version number for check. |
| Direction of information  | From STM to ERTMS/ETCS on-board function From ERTMS/ETCS on-board function to STM                                                                                                             | From STM to ERTMS/ETCS on-board function From ERTMS/ETCS on-board function to STM                                                                                                             | From STM to ERTMS/ETCS on-board function From ERTMS/ETCS on-board function to STM                                                                                                             |
| Content                   | Variable                                                                                                                                                                                      | Length                                                                                                                                                                                        | Comment                                                                                                                                                                                       |
|                           | NID_PACKET                                                                                                                                                                                    | 8                                                                                                                                                                                             | Packet identifier Value=1                                                                                                                                                                     |
|                           | L_PACKET                                                                                                                                                                                      | 13                                                                                                                                                                                            | Packet length                                                                                                                                                                                 |
|                           | N_VERMAJOR                                                                                                                                                                                    | 8                                                                                                                                                                                             | FFFIS STM version number, major number: X                                                                                                                                                     |
|                           | N_VERMINOR                                                                                                                                                                                    | 8                                                                                                                                                                                             | FFFIS STM version number, minor number: Y                                                                                                                                                     |

<!-- image -->

## 7.1.2 Packet STM-15: State report from STM

| Subset-035 Ref.           | §5.2.7.1, 9.3.1.4, 9.3.1.4.1, 10.1.1.2, 10.3.2.3, 10.3.2.4, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.3.3.7, 10.14.1.1, 13.2.1.5, 13.2.1.6   | §5.2.7.1, 9.3.1.4, 9.3.1.4.1, 10.1.1.2, 10.3.2.3, 10.3.2.4, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.3.3.7, 10.14.1.1, 13.2.1.5, 13.2.1.6   | §5.2.7.1, 9.3.1.4, 9.3.1.4.1, 10.1.1.2, 10.3.2.3, 10.3.2.4, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.3.3.7, 10.14.1.1, 13.2.1.5, 13.2.1.6   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA, FA                                                                                                                              | PO, CO, DE, CS, HS, DA, FA                                                                                                                              | PO, CO, DE, CS, HS, DA, FA                                                                                                                              |
| Description               | Indicates to the ERTMS/ETCS on-board the STM state.                                                                                                     | Indicates to the ERTMS/ETCS on-board the STM state.                                                                                                     | Indicates to the ERTMS/ETCS on-board the STM state.                                                                                                     |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                                                                                | From STM to ERTMS/ETCS on-board function                                                                                                                | From STM to ERTMS/ETCS on-board function                                                                                                                |
| Content                   | Variable                                                                                                                                                | Length                                                                                                                                                  | Comment                                                                                                                                                 |
|                           | NID_PACKET                                                                                                                                              | 8                                                                                                                                                       | Packet identifier Value = 15                                                                                                                            |
|                           | L_PACKET                                                                                                                                                | 13                                                                                                                                                      | Packet length                                                                                                                                           |
|                           | NID_STMSTATE                                                                                                                                            | 4                                                                                                                                                       | Current STM state                                                                                                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2 Packets related to the STM Control Function

7.2.1 Packet STM-2: ERTMS/ETCS on-board physical addresses and safety levels

| Subset-035 Ref.          | §5.2.7.9, 6.2.1.1, 6.4, 8.2.1.5, 10.1.1.4                                                             | §5.2.7.9, 6.2.1.1, 6.4, 8.2.1.5, 10.1.1.4                                                             | §5.2.7.9, 6.2.1.1, 6.4, 8.2.1.5, 10.1.1.4                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Allowed to send in state | PO                                                                                                    | PO                                                                                                    | PO                                                                                                    |
| Description              | Message defining each ERTMS/ETCS on-board function physical bus address, and associated safety level. | Message defining each ERTMS/ETCS on-board function physical bus address, and associated safety level. | Message defining each ERTMS/ETCS on-board function physical bus address, and associated safety level. |
| Direction of information | From ERTMS/ETCS on-board function to STM                                                              | From ERTMS/ETCS on-board function to STM                                                              | From ERTMS/ETCS on-board function to STM                                                              |
| Content                  | Variable                                                                                              | Length                                                                                                | Comment                                                                                               |
|                          | NID_PACKET                                                                                            | 8                                                                                                     | Packet identifier Value = 2                                                                           |
|                          | L_PACKET                                                                                              | 13                                                                                                    | Packet length                                                                                         |
|                          | N_ADDR_JD                                                                                             | 7                                                                                                     | Address of Juridical Data Function                                                                    |
|                          | Q_ADDR_JD                                                                                             | 2                                                                                                     | Safety level/Availability of Juridical Data Function                                                  |
|                          | N_ADDR_DMI_CHANNEL1                                                                                   | 7                                                                                                     | Address of DMI channel 1                                                                              |
|                          | Q_ADDR_DMI_CHANNEL1                                                                                   | 2                                                                                                     | Safety level of DMI channel 1                                                                         |
|                          | N_ADDR_DMI_CHANNEL2                                                                                   | 7                                                                                                     | Address of DMI channel 2                                                                              |
|                          | Q_ADDR_DMI_CHANNEL2                                                                                   | 2                                                                                                     | Safety level/Availability of DMI channel 2                                                            |
|                          | N_ADDR_DMI_CHANNEL3                                                                                   | 7                                                                                                     | Address of DMI channel 3                                                                              |
|                          | Q_ADDR_DMI_CHANNEL3                                                                                   | 2                                                                                                     | Safety level/Availability of DMI channel 3                                                            |
|                          | N_ADDR_DMI_CHANNEL4                                                                                   | 7                                                                                                     | Address of DMI channel 4                                                                              |
|                          | Q_ADDR_DMI_CHANNEL4                                                                                   | 2                                                                                                     | Safety level/Availability of DMI channel 4                                                            |
|                          | N_ADDR_ODO                                                                                            | 7                                                                                                     | Address of Odometer Function                                                                          |
|                          | Q_ADDR_ODO                                                                                            | 2                                                                                                     | Safety level of Odometer Function                                                                     |
|                          | N_ADDR_TI                                                                                             | 7                                                                                                     | Address of TIU Function                                                                               |
|                          | Q_ADDR_TI                                                                                             | 2                                                                                                     | Safety level of TIU Function                                                                          |
|                          | N_ADDR_BI                                                                                             | 7                                                                                                     | Address of BIU Function                                                                               |
|                          | Q_ADDR_BI                                                                                             | 2                                                                                                     | Safety level of BIU Function                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.2 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.3 Packet STM-5: ETCS status data

| Subset-035 Ref.           | §5.2.7.3, 8.2.1.6, 10.5.1.1                                                                                      | §5.2.7.3, 8.2.1.6, 10.5.1.1                                                                                      | §5.2.7.3, 8.2.1.6, 10.5.1.1                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                                           | PO, CO, DE, CS, HS, DA                                                                                           | PO, CO, DE, CS, HS, DA                                                                                           |
| Description               | This packet contains the ERTMS/ETCS on-board current status (ETCS mode and ETCS level of operation) for the STM. | This packet contains the ERTMS/ETCS on-board current status (ETCS mode and ETCS level of operation) for the STM. | This packet contains the ERTMS/ETCS on-board current status (ETCS mode and ETCS level of operation) for the STM. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                         | From ERTMS/ETCS on-board function to STM                                                                         | From ERTMS/ETCS on-board function to STM                                                                         |
| Content                   | Variable                                                                                                         | Length                                                                                                           | Comment                                                                                                          |
|                           | NID_PACKET                                                                                                       | 8                                                                                                                | Packet identifier Value=5                                                                                        |
|                           | L_PACKET                                                                                                         | 13                                                                                                               | Packet length                                                                                                    |
|                           | M_LEVEL                                                                                                          |                                                                                                                  | Defined in Chapter 7 of [1]                                                                                      |
|                           | NID_NTC                                                                                                          |                                                                                                                  | If M_LEVEL = 1 (NTC), this value shall be transmitted only in Level NTC. Variable defined in Chapter 7 of [1]    |
|                           | M_MODESTM                                                                                                        | 4                                                                                                                | ETCS mode                                                                                                        |

## 7.2.4 Packet STM-6: Override activation

| Subset-035 Ref.          | §5.2.7.6, 10.10.1.2, 10.10.2.1, 10.10.2.2                                                                            | §5.2.7.6, 10.10.1.2, 10.10.2.1, 10.10.2.2                                                                            | §5.2.7.6, 10.10.1.2, 10.10.2.1, 10.10.2.2                                                                            |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Allowed to send in state | DA                                                                                                                   | DA                                                                                                                   | DA                                                                                                                   |
| Description              | Report of the activation of the STM Override procedure from the STM to the ERTMS/ETCS on-board STM Control Function. | Report of the activation of the STM Override procedure from the STM to the ERTMS/ETCS on-board STM Control Function. | Report of the activation of the STM Override procedure from the STM to the ERTMS/ETCS on-board STM Control Function. |
| Direction of information | From STM to ERTMS/ETCS on-board function                                                                             | From STM to ERTMS/ETCS on-board function                                                                             | From STM to ERTMS/ETCS on-board function                                                                             |
| Content                  | Variable                                                                                                             | Length                                                                                                               | Comment                                                                                                              |
|                          | NID_PACKET                                                                                                           | 8                                                                                                                    | Packet identifier Value = 6                                                                                          |
|                          | L_PACKET                                                                                                             | 13                                                                                                                   | Packet length                                                                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.5 Packet STM-7: Override status

| Subset-035 Ref.           | §5.2.7.6, 10.10.1.2, 10.10.2.3                                                                               | §5.2.7.6, 10.10.1.2, 10.10.2.3                                                                               | §5.2.7.6, 10.10.1.2, 10.10.2.3                                                                               |
|---------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                                       | PO, CO, DE, CS, HS, DA                                                                                       | PO, CO, DE, CS, HS, DA                                                                                       |
| Description               | Reports a change of the ETCS Override status from the ERTMS/ETCS on- board STM Control Function to the STMs. | Reports a change of the ETCS Override status from the ERTMS/ETCS on- board STM Control Function to the STMs. | Reports a change of the ETCS Override status from the ERTMS/ETCS on- board STM Control Function to the STMs. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                     | From ERTMS/ETCS on-board function to STM                                                                     | From ERTMS/ETCS on-board function to STM                                                                     |
| Content                   | Variable                                                                                                     | Length                                                                                                       | Comment                                                                                                      |
|                           | NID_PACKET                                                                                                   | 8                                                                                                            | Packet identifier Value = 7                                                                                  |
|                           | L_PACKET                                                                                                     | 13                                                                                                           | Packet length                                                                                                |
|                           | Q_OVR_STATUS                                                                                                 | 1                                                                                                            | ETCS Override status                                                                                         |

## 7.2.6 Packet STM-13: State request from STM

| Subset-035 Ref.           | §5.2.7.1, 8.2.1.6, 8.3.1.3, 8.3.1.4, 8.3.1.5, 8.4.1.3, 8.4.1.4, 10.3.2.4                            | §5.2.7.1, 8.2.1.6, 8.3.1.3, 8.3.1.4, 8.3.1.5, 8.4.1.3, 8.4.1.4, 10.3.2.4                            | §5.2.7.1, 8.2.1.6, 8.3.1.3, 8.3.1.4, 8.3.1.5, 8.4.1.3, 8.4.1.4, 10.3.2.4                            |
|---------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE                                                                                          | PO, CO, DE                                                                                          | PO, CO, DE                                                                                          |
| Description               | Reports a request for a state change from the STM to the ERTMS/ETCS on- board STM Control Function. | Reports a request for a state change from the STM to the ERTMS/ETCS on- board STM Control Function. | Reports a request for a state change from the STM to the ERTMS/ETCS on- board STM Control Function. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                            | From STM to ERTMS/ETCS on-board function                                                            | From STM to ERTMS/ETCS on-board function                                                            |
| Content                   | Variable                                                                                            | Length                                                                                              | Comment                                                                                             |
|                           | NID_PACKET                                                                                          | 8                                                                                                   | Packet identifier Value = 13                                                                        |
|                           | L_PACKET                                                                                            | 13                                                                                                  | Packet length                                                                                       |
|                           | NID_STMSTATEREQUEST                                                                                 | 4                                                                                                   | Request to change state                                                                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.7 Packet STM-14: State order to STM

| Subset-035 Ref.           | §5.2.7.1, 8.6.1.4, 8.7.1.2, 9.2.1.2.1, 10.2.1.2, 10.3.2.2, 10.3.2.4, 10.3.2.6, 10.3.2.6.1, 10.3.2.6.2, , 10.3.2.7, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.14.1.1   | §5.2.7.1, 8.6.1.4, 8.7.1.2, 9.2.1.2.1, 10.2.1.2, 10.3.2.2, 10.3.2.4, 10.3.2.6, 10.3.2.6.1, 10.3.2.6.2, , 10.3.2.7, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.14.1.1   | §5.2.7.1, 8.6.1.4, 8.7.1.2, 9.2.1.2.1, 10.2.1.2, 10.3.2.2, 10.3.2.4, 10.3.2.6, 10.3.2.6.1, 10.3.2.6.2, , 10.3.2.7, 10.3.3.1, 10.3.3.2, 10.3.3.3, 10.14.1.1   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA, FA                                                                                                                                   | PO, CO, DE, CS, HS, DA, FA                                                                                                                                   | PO, CO, DE, CS, HS, DA, FA                                                                                                                                   |
| Description               | State order to STM.                                                                                                                                          | State order to STM.                                                                                                                                          | State order to STM.                                                                                                                                          |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                                                                     | From ERTMS/ETCS on-board function to STM                                                                                                                     | From ERTMS/ETCS on-board function to STM                                                                                                                     |
| Content                   | Variable                                                                                                                                                     | Length                                                                                                                                                       | Comment                                                                                                                                                      |
|                           | NID_PACKET                                                                                                                                                   | 8                                                                                                                                                            | Packet identifier Value = 14                                                                                                                                 |
|                           | L_PACKET                                                                                                                                                     | 13                                                                                                                                                           | Packet length                                                                                                                                                |
|                           | NID_STMSTATEORDER                                                                                                                                            | 4                                                                                                                                                            | STM state order                                                                                                                                              |

## 7.2.8 Packet STM-16: Transition variables STM max speed from STM

| Subset-035 Ref.          | §5.2.7.8, 8.6.1.2, 10.12.1.1, 10.12.1.2, 10.12.1.3, 10.12.1.6, 10.12.2.1, 10.12.2.2, 10.12.2.3¨   | §5.2.7.8, 8.6.1.2, 10.12.1.1, 10.12.1.2, 10.12.1.3, 10.12.1.6, 10.12.2.1, 10.12.2.2, 10.12.2.3¨   | §5.2.7.8, 8.6.1.2, 10.12.1.1, 10.12.1.2, 10.12.1.3, 10.12.1.6, 10.12.2.1, 10.12.2.2, 10.12.2.3¨   |
|--------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Allowed to send in state | HS                                                                                                | HS                                                                                                | HS                                                                                                |
| Description              | Transmit to the ERTMS/ETCS on-board the STM max speed.                                            | Transmit to the ERTMS/ETCS on-board the STM max speed.                                            | Transmit to the ERTMS/ETCS on-board the STM max speed.                                            |
| Direction of information | From STM to ERTMS/ETCS on-board function                                                          | From STM to ERTMS/ETCS on-board function                                                          | From STM to ERTMS/ETCS on-board function                                                          |
| Content                  | Variable                                                                                          | Length                                                                                            | Comment                                                                                           |
|                          | NID_PACKET                                                                                        | 8                                                                                                 | Packet identifier Value = 16                                                                      |
|                          | L_PACKET                                                                                          | 13                                                                                                | Packet length                                                                                     |
|                          | V_STMMAX                                                                                          | 7                                                                                                 | STM max speed                                                                                     |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.9 Packet STM-17: Transition variables STM system speed and distance from STM

| Subset-035 Ref.          | §5.2.7.8, 8.6.1.3, 10.12.1.4, 10.12.1.5, 10.12.1.6                     | §5.2.7.8, 8.6.1.3, 10.12.1.4, 10.12.1.5, 10.12.1.6                     | §5.2.7.8, 8.6.1.3, 10.12.1.4, 10.12.1.5, 10.12.1.6                     |
|--------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Allowed to send in state | HS                                                                     | HS                                                                     | HS                                                                     |
| Description              | Transmit to the ERTMS/ETCS on-board the STM system speed and distance. | Transmit to the ERTMS/ETCS on-board the STM system speed and distance. | Transmit to the ERTMS/ETCS on-board the STM system speed and distance. |
| Direction of information | From STM to ERTMS/ETCS on-board function                               | From STM to ERTMS/ETCS on-board function                               | From STM to ERTMS/ETCS on-board function                               |
| Content                  | Variable                                                               | Length                                                                 | Comment                                                                |
| Content                  | NID_PACKET                                                             | 8                                                                      | Packet identifier Value = 17                                           |
| Content                  | L_PACKET                                                               | 13                                                                     | Packet length                                                          |
| Content                  | V_STMSYS                                                               | 7                                                                      | STM system speed                                                       |
| Content                  | D_STMSYS                                                               | 15                                                                     | STM system distance                                                    |

## 7.2.10 Packet STM-18: National Trip Procedure

| Subset-035 Ref.          | §9.2.1.2.1, 9.2.1.3, 10.3.2.4, 10.3.3.3, 10.13.1.1                                           | §9.2.1.2.1, 9.2.1.3, 10.3.2.4, 10.3.3.3, 10.13.1.1                                           | §9.2.1.2.1, 9.2.1.3, 10.3.2.4, 10.3.3.3, 10.13.1.1                                           |
|--------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Allowed to send in state | DA                                                                                           | DA                                                                                           | DA                                                                                           |
| Description              | Indicates to the ERTMS/ETCS on-board that the STM is currently in a National Trip Procedure. | Indicates to the ERTMS/ETCS on-board that the STM is currently in a National Trip Procedure. | Indicates to the ERTMS/ETCS on-board that the STM is currently in a National Trip Procedure. |
| Direction of information | From STM to ERTMS/ETCS on-board function                                                     | From STM to ERTMS/ETCS on-board function                                                     | From STM to ERTMS/ETCS on-board function                                                     |
| Content                  | Variable                                                                                     | Length                                                                                       | Comment                                                                                      |
|                          | NID_PACKET                                                                                   | 8                                                                                            | Packet identifier Value = 18                                                                 |
|                          | L_PACKET                                                                                     | 13                                                                                           | Packet length                                                                                |

## 7.2.11 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.12 Packet STM-175: Train Data

| Subset-035 Ref.           | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.1, 10.4.1.2, 10.4.1.7, 10.7.4.4, 10.7.4.9   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.1, 10.4.1.2, 10.4.1.7, 10.7.4.4, 10.7.4.9   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.1, 10.4.1.2, 10.4.1.7, 10.7.4.4, 10.7.4.9   |
|---------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                    | PO, CO, DE, CS, HS, DA                                                                    | PO, CO, DE, CS, HS, DA                                                                    |
| Description               | Validated train data.                                                                     | Validated train data.                                                                     | Validated train data.                                                                     |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                  | From ERTMS/ETCS on-board function to STM                                                  | From ERTMS/ETCS on-board function to STM                                                  |
| Content                   | Variable                                                                                  | Length                                                                                    | Comment                                                                                   |
|                           | NID_PACKET                                                                                | 8                                                                                         | Packet identifier Value =175                                                              |
|                           | L_PACKET                                                                                  | 13                                                                                        | Packet length                                                                             |
|                           | NC_CDTRAIN                                                                                |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | NC_TRAIN                                                                                  |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | L_TRAIN                                                                                   |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | V_MAXTRAIN                                                                                |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | M_LOADINGGAUGE                                                                            |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | M_AXLELOADCAT                                                                             |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | M_AIRTIGHT                                                                                |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | M_TRAINTYPE                                                                               | 8                                                                                         | Train type                                                                                |
|                           | N_ITER                                                                                    |                                                                                           | Defined in Chapter 7 of[1]                                                                |
|                           | M_VOLTAGE(k)                                                                              |                                                                                           | Defined in Chapter 7 of [1]                                                               |
|                           | NID_CTRACTION(k)                                                                          |                                                                                           | NID_CTRACTION(k) given only if M_VOLTAGE(k)  0 Defined in Chapter 7 of [1]               |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.13 Packet STM-176: Train data traction/brake parameters to STM

| Subset-035 Ref.           | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 8.3.1.2.2, 10.4.1.1, 10.4.1.4, 10.4.1.7, 10.7.1.2   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 8.3.1.2.2, 10.4.1.1, 10.4.1.4, 10.4.1.7, 10.7.1.2   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 8.3.1.2.2, 10.4.1.1, 10.4.1.4, 10.4.1.7, 10.7.1.2   |
|---------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                     | PO, CO, DE, CS, HS, DA                                                                     | PO, CO, DE, CS, HS, DA                                                                     |
| Description               | Validated train data traction/brake parameters.                                            | Validated train data traction/brake parameters.                                            | Validated train data traction/brake parameters.                                            |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                   | From ERTMS/ETCS on-board function to STM                                                   | From ERTMS/ETCS on-board function to STM                                                   |
| Content                   | Variable                                                                                   | Length                                                                                     | Comment                                                                                    |
|                           | NID_PACKET                                                                                 | 8                                                                                          | Packet identifier Value = 176                                                              |
|                           | L_PACKET                                                                                   | 13                                                                                         | Packet length                                                                              |
|                           | T_BRAKE_SERVICE                                                                            |                                                                                            | Defined in [2]                                                                             |
|                           | T_BRAKE_EMERGENCY                                                                          |                                                                                            | Defined in [2]                                                                             |
|                           | T_TRACTION_CUT_OFF                                                                         |                                                                                            | Defined in [2]                                                                             |
|                           | M_BRAKE_POSITION                                                                           |                                                                                            | Defined in [2]                                                                             |
|                           | M_BRAKE_PERCENTAGE_ STM                                                                    | 8                                                                                          | Brake percentage                                                                           |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.14 Packet STM-177: Additional Data Values and date/time to STM

| Subset-035 Ref.           | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.5, 10.4.1.7, 10.4.1.8, 10.7.1.2   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.5, 10.4.1.7, 10.4.1.8, 10.7.1.2   | §5.2.7.2, 8.3.1.1, 8.3.1.2, 8.3.1.2.1, 10.4.1.5, 10.4.1.7, 10.4.1.8, 10.7.1.2   |
|---------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                          | PO, CO, DE, CS, HS, DA                                                          | PO, CO, DE, CS, HS, DA                                                          |
| Description               | ETCS additional data and date / time.                                           | ETCS additional data and date / time.                                           | ETCS additional data and date / time.                                           |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                        | From ERTMS/ETCS on-board function to STM                                        | From ERTMS/ETCS on-board function to STM                                        |
| Content                   | Variable                                                                        | Length                                                                          | Comment                                                                         |
|                           | NID_PACKET                                                                      | 8                                                                               | Packet identifier Value = 177                                                   |
|                           | L_PACKET                                                                        | 13                                                                              | Packet length                                                                   |
|                           | NID_ENGINE                                                                      |                                                                                 | Defined in Chapter 7 of [1]                                                     |
|                           | M_ADHESION                                                                      |                                                                                 | Defined in Chapter 7 of [1]                                                     |
|                           | YEAR                                                                            |                                                                                 | Defined in [2]                                                                  |
|                           | MONTH                                                                           |                                                                                 | Defined in [2]                                                                  |
|                           | DAY                                                                             |                                                                                 | Defined in [2]                                                                  |
|                           | HOUR                                                                            |                                                                                 | Defined in [2]                                                                  |
|                           | MINUTES                                                                         |                                                                                 | Defined in [2]                                                                  |
|                           | SECONDS                                                                         |                                                                                 | Defined in [2]                                                                  |
|                           | TTS                                                                             |                                                                                 | Defined in [2]                                                                  |
|                           | NID_OPERATIONAL_ST M                                                            | 32                                                                              | Train Running Number                                                            |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.15 Packet STM-178: National Values to STM

| Subset-035 Ref.           | §5.2.7.2, 8.3.1.1, 8.3.1.2.1, 10.4.1.6, 10.4.1.7, 10.4.1.9, 10.7.1.2                                    | §5.2.7.2, 8.3.1.1, 8.3.1.2.1, 10.4.1.6, 10.4.1.7, 10.4.1.9, 10.7.1.2                                    | §5.2.7.2, 8.3.1.1, 8.3.1.2.1, 10.4.1.6, 10.4.1.7, 10.4.1.9, 10.7.1.2                                    |
|---------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                                  | PO, CO, DE, CS, HS, DA                                                                                  | PO, CO, DE, CS, HS, DA                                                                                  |
| Description               | Downloads a set of National Values. Note: See [1] chapter 7.4.2.1.1 [Packet Number 3: National Values]. | Downloads a set of National Values. Note: See [1] chapter 7.4.2.1.1 [Packet Number 3: National Values]. | Downloads a set of National Values. Note: See [1] chapter 7.4.2.1.1 [Packet Number 3: National Values]. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                | From ERTMS/ETCS on-board function to STM                                                                | From ERTMS/ETCS on-board function to STM                                                                |
| Content                   | Variable                                                                                                | Length                                                                                                  | Comment                                                                                                 |
|                           | NID_PACKET                                                                                              | 8                                                                                                       | Packet identifier Value = 178                                                                           |
|                           | L_PACKET                                                                                                | 13                                                                                                      | Packet length                                                                                           |
|                           | Q_SCALE                                                                                                 |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVSHUNT                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVSTFF                                                                                                |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVONSIGHT                                                                                             |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVLIMSUPERV                                                                                           |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVUNFIT                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVREL                                                                                                 |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | D_NVROLL                                                                                                |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVSBTSMPERM                                                                                           |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVEMRRLS                                                                                              |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVGUIPERM                                                                                             |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVSBFBPERM                                                                                            |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVINHSMICPERM                                                                                         |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVALLOWOVTRP                                                                                          |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | V_NVSUPOVTRP                                                                                            |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | D_NVOVTRP                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | T_NVOVTRP                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | D_NVPOTRP                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | M_NVCONTACT                                                                                             |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | T_NVCONTACT                                                                                             |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | M_NVDERUN                                                                                               |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | D_NVSTFF                                                                                                |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |
|                           | Q_NVDRIVER_ADHES                                                                                        |                                                                                                         | Defined in Chapter 7 of [1]                                                                             |

© This document has been developed and released by UNISIG

<!-- image -->

| A_NVMAXREDADH1   | Defined in Chapter 7 of [1]                                                                       |
|------------------|---------------------------------------------------------------------------------------------------|
| A_NVMAXREDADH2   | Defined in Chapter 7 of [1]                                                                       |
| A_NVMAXREDADH3   | Defined in Chapter 7 of [1]                                                                       |
| Q_NVLOCACC       | Defined in Chapter 7 of [1]                                                                       |
| M_NVAVADH        | Defined in Chapter 7 of [1]                                                                       |
| M_NVEBCL         | Defined in Chapter 7 of [1]                                                                       |
| Q_NVKINT         | Defined in Chapter 7 of [1]                                                                       |
| Q_NVKVINTSET     | Only if Q_NVKINT = 1, Q_NVKVINTSET and the following variables follow Defined in Chapter 7 of [1] |
| A_NVP12          | Only if Q_NVKVINTSET = 1 Defined in Chapter 7 of [1]                                              |
| A_NVP23          | Only if Q_NVKVINTSET = 1 Defined in Chapter 7 of [1]                                              |
| V_NVKVINT        | = 0 km/h Defined in Chapter 7 of [1]                                                              |
| M_NVKVINT        | Valid between V_NVKVINT and V_NVKVINT(1) Defined in Chapter 7 of [1]                              |
| M_NVKVINT        | Only if Q_NVKVINTSET = 1 Valid between V_NVKVINT and V_NVKVINT(1) Defined in Chapter 7 of [1]     |
| N_ITER           | Defined in Chapter 7 of [1]                                                                       |
| V_NVKVINT(n)     | Defined in Chapter 7 of [1]                                                                       |
| M_NVKVINT(n)     | Only if Q_NVKVINTSET = 1 Defined in Chapter 7 of [1]                                              |
| N_ITER           | Defined in Chapter 7 of [1]                                                                       |
| Q_NVKVINTSET(k)  | Defined in Chapter 7 of [1]                                                                       |
| A_NVP12(k)       | Only if Q_NVKVINTSET(k) = 1 Defined in Chapter 7 of [1]                                           |
| A_NVP23(k)       | Only if Q_NVKVINTSET(k) = 1 Defined in Chapter 7 of [1]                                           |
| V_NVKVINT(k)     | Defined in Chapter 7 of [1]                                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

| M_NVKVINT(k)   | Defined in Chapter 7 of [1]                             |
|----------------|---------------------------------------------------------|
| M_NVKVINT(k)   | Only if Q_NVKVINTSET(k) = 1 Defined in Chapter 7 of [1] |
| N_ITER(k)      | Defined in Chapter 7 of [1]                             |
| V_NVKVINT(k,m) | Defined in Chapter 7 of [1]                             |
| M_NVKVINT(k,m) | Defined in Chapter 7 of [1]                             |
| M_NVKVINT(k,m) | Only if Q_NVKVINTSET(k) = 1 Defined in Chapter 7 of [1] |
| L_NVKRINT      | Defined in Chapter 7 of [1]                             |
| M_NVKRINT      | Defined in Chapter 7 of [1]                             |
| N_ITER         | Defined in Chapter 7 of [1]                             |
| L_NVKRINT(l)   | Defined in Chapter 7 of [1]                             |
| M_NVKRINT(l)   | Defined in Chapter 7 of [1]                             |
| M_NVKTINT      | Defined in Chapter 7 of [1]                             |

## 7.2.16 Packet STM-181: Specific NTC Data Need

| Subset-035 Ref.           | §8.2.1.4, 10.3.2.4, 10.7.3.2, 10.7.3.4, 10.7.5                                                                                                                                                                                                                     | §8.2.1.4, 10.3.2.4, 10.7.3.2, 10.7.3.4, 10.7.5                                                                                                                                                                                                                     | §8.2.1.4, 10.3.2.4, 10.7.3.2, 10.7.3.4, 10.7.5                                                                                                                                                                                                                     |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, CS, HS, DA                                                                                                                                                                                                                                                 | PO, CO, CS, HS, DA                                                                                                                                                                                                                                                 | PO, CO, CS, HS, DA                                                                                                                                                                                                                                                 |
| Description               | STM need for Specific NTC Data Entry. Note: At PO state STM-181 indicates that the STM will request for a Specific NTC Data during a Specific NTC Data Entry procedure. In all other states STM-181 indicates the current need of Specific NTC Data to the driver. | STM need for Specific NTC Data Entry. Note: At PO state STM-181 indicates that the STM will request for a Specific NTC Data during a Specific NTC Data Entry procedure. In all other states STM-181 indicates the current need of Specific NTC Data to the driver. | STM need for Specific NTC Data Entry. Note: At PO state STM-181 indicates that the STM will request for a Specific NTC Data during a Specific NTC Data Entry procedure. In all other states STM-181 indicates the current need of Specific NTC Data to the driver. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                           | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                           | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                           |
| Content                   | Variable                                                                                                                                                                                                                                                           | Length                                                                                                                                                                                                                                                             | Comment                                                                                                                                                                                                                                                            |
|                           | NID_PACKET                                                                                                                                                                                                                                                         | 8                                                                                                                                                                                                                                                                  | Packet identifier Value = 181                                                                                                                                                                                                                                      |
|                           | L_PACKET                                                                                                                                                                                                                                                           | 13                                                                                                                                                                                                                                                                 | Packet length                                                                                                                                                                                                                                                      |
|                           | Q_DATAENTRY                                                                                                                                                                                                                                                        | 1                                                                                                                                                                                                                                                                  | Need for Specific NTC Data Entry                                                                                                                                                                                                                                   |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.17 Packet STM-179: Specific NTC Data Entry request

| Subset-035 Ref.           | §8.3.1.3, 8.4.1.1, 10.7.3.3, 10.7.3.6, 10.7.4.3, 10.7.4.5, 10.7.4.6, 10.7.4.8, 10.7.4.9, 10.7.5, 15.2.1.1, 15.2.1.4                                                                                                                                                                         | §8.3.1.3, 8.4.1.1, 10.7.3.3, 10.7.3.6, 10.7.4.3, 10.7.4.5, 10.7.4.6, 10.7.4.8, 10.7.4.9, 10.7.5, 15.2.1.1, 15.2.1.4                                                                                                                                                                         | §8.3.1.3, 8.4.1.1, 10.7.3.3, 10.7.3.6, 10.7.4.3, 10.7.4.5, 10.7.4.6, 10.7.4.8, 10.7.4.9, 10.7.5, 15.2.1.1, 15.2.1.4                                                                                                                                                                         |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | DE, CS, HS, DA                                                                                                                                                                                                                                                                              | DE, CS, HS, DA                                                                                                                                                                                                                                                                              | DE, CS, HS, DA                                                                                                                                                                                                                                                                              |
| Description               | Request for Specific NTC Data Entry. This packet can be grouped with other STM-179 packets by using the Q_FOLLOWING indicator in order to form one common Specific NTC Data Entry request. Note: The STM indicates the "End of Specific NTC Data Entry" by a packet STM-179, with N_ITER=0. | Request for Specific NTC Data Entry. This packet can be grouped with other STM-179 packets by using the Q_FOLLOWING indicator in order to form one common Specific NTC Data Entry request. Note: The STM indicates the "End of Specific NTC Data Entry" by a packet STM-179, with N_ITER=0. | Request for Specific NTC Data Entry. This packet can be grouped with other STM-179 packets by using the Q_FOLLOWING indicator in order to form one common Specific NTC Data Entry request. Note: The STM indicates the "End of Specific NTC Data Entry" by a packet STM-179, with N_ITER=0. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                    | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                    | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                    |
| Content                   | Variable                                                                                                                                                                                                                                                                                    | Length                                                                                                                                                                                                                                                                                      | Comment                                                                                                                                                                                                                                                                                     |
|                           | NID_PACKET                                                                                                                                                                                                                                                                                  | 8                                                                                                                                                                                                                                                                                           | Packet identifier Value = 179                                                                                                                                                                                                                                                               |
|                           | L_PACKET                                                                                                                                                                                                                                                                                    | 13                                                                                                                                                                                                                                                                                          | Packet length                                                                                                                                                                                                                                                                               |
|                           | Q_FOLLOWING                                                                                                                                                                                                                                                                                 | 1                                                                                                                                                                                                                                                                                           | Indicate a following STM- 179 packet                                                                                                                                                                                                                                                        |
|                           | N_ITER                                                                                                                                                                                                                                                                                      | 5                                                                                                                                                                                                                                                                                           | Maximum iteration data =0 if there is 'End of Specific NTC Data Entry' Maximum value = 15 Variable defined in Chapter 7 of [1]                                                                                                                                                              |
|                           | NID_DATA(j)                                                                                                                                                                                                                                                                                 | 8                                                                                                                                                                                                                                                                                           | Identifier of a Specific NTC Data to be entered.                                                                                                                                                                                                                                            |
|                           | L_CAPTION(j)                                                                                                                                                                                                                                                                                | 6                                                                                                                                                                                                                                                                                           | Length of X_CAPTION for data label in bytes Maximum value = 40                                                                                                                                                                                                                              |
|                           | X_CAPTION(j,q)                                                                                                                                                                                                                                                                              | 8                                                                                                                                                                                                                                                                                           | Data label caption text byte string                                                                                                                                                                                                                                                         |
|                           | L_VALUE(j)                                                                                                                                                                                                                                                                                  | 5                                                                                                                                                                                                                                                                                           | Length of X_VALUE for default value in bytes. Maximum value = 20                                                                                                                                                                                                                            |
|                           | X_VALUE(j,i)                                                                                                                                                                                                                                                                                | 8                                                                                                                                                                                                                                                                                           | Data value caption text byte string                                                                                                                                                                                                                                                         |

© This document has been developed and released by UNISIG

<!-- image -->

| N_ITER(j)      |    | Maximum iteration data dedicated keyboard values =0 if there is no dedicated keyboard Variable defined in Chapter 7 of [1]   |
|----------------|----|------------------------------------------------------------------------------------------------------------------------------|
| L_VALUE(j,i)   |  5 | Length of X_VALUE for dedicated keyboard value in bytes Maximum value = 20                                                   |
| X_VALUE(j,i,k) |  8 | Data for dedicated keyboard value caption text byte string                                                                   |

## 7.2.18 Packet STM-180: Specific NTC Data values

| Subset-035 Ref.           | §10.7.5, 15.2.1.2, 15.2.1.4                                                            | §10.7.5, 15.2.1.2, 15.2.1.4                                                            | §10.7.5, 15.2.1.2, 15.2.1.4                                                            |
|---------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Allowed to send in states | DE, CS, HS, DA                                                                         | DE, CS, HS, DA                                                                         | DE, CS, HS, DA                                                                         |
| Description               | ERTMS/ETCS on-board report of the Specific NTC Data Entry values requested by the STM. | ERTMS/ETCS on-board report of the Specific NTC Data Entry values requested by the STM. | ERTMS/ETCS on-board report of the Specific NTC Data Entry values requested by the STM. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                               | From ERTMS/ETCS on-board function to STM                                               | From ERTMS/ETCS on-board function to STM                                               |
| Content                   | Variable                                                                               | Length                                                                                 | Comment                                                                                |
|                           | NID_PACKET                                                                             | 8                                                                                      | Packet identifier Value = 180                                                          |
|                           | L_PACKET                                                                               | 13                                                                                     | Packet length                                                                          |
|                           | N_ITER                                                                                 |                                                                                        | Maximum iteration data Maximum value = 15 Variable defined in Chapter 7 of [1]         |
|                           | NID_DATA(j)                                                                            | 8                                                                                      | Identifier of a Specific NTC Data to be selected by the driver.                        |
|                           | L_VALUE(j)                                                                             | 5                                                                                      | Length of X_VALUE in bytes Maximum value = 20                                          |
|                           | X_VALUE(j,k)                                                                           | 8                                                                                      | Data value caption text byte string selected by the driver                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.19 Packet STM-182: Request for Specific NTC Data View values

| Subset-035 Ref.           | §5.2.7.2, 10.8.1.1, 10.8.1.2, 10.8.1.5                                                                                | §5.2.7.2, 10.8.1.1, 10.8.1.2, 10.8.1.5                                                                                | §5.2.7.2, 10.8.1.1, 10.8.1.2, 10.8.1.5                                                                                |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | CS, HS, DA                                                                                                            | CS, HS, DA                                                                                                            | CS, HS, DA                                                                                                            |
| Description               | Request for Specific NTC Data View values. This request is sent to the STM when the Data View procedure is triggered. | Request for Specific NTC Data View values. This request is sent to the STM when the Data View procedure is triggered. | Request for Specific NTC Data View values. This request is sent to the STM when the Data View procedure is triggered. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                              | From ERTMS/ETCS on-board function to STM                                                                              | From ERTMS/ETCS on-board function to STM                                                                              |
| Content                   | Variable                                                                                                              | Length                                                                                                                | Comment                                                                                                               |
|                           | NID_PACKET                                                                                                            | 8                                                                                                                     | Packet identifier Value = 182                                                                                         |
|                           | L_PACKET                                                                                                              | 13                                                                                                                    | Packet length                                                                                                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.20 Packet STM-183: Specific NTC Data View values

| Subset-035 Ref.           | §5.2.7.2, 10.3.2.4, 10.8.1.1, 10.8.1.3, 10.8.1.4, 10.8.1.5, 15.2.1.3, 15.2.1.4                                                                                                                                                                                                                                               | §5.2.7.2, 10.3.2.4, 10.8.1.1, 10.8.1.3, 10.8.1.4, 10.8.1.5, 15.2.1.3, 15.2.1.4                                                                                                                                                                                                                                               | §5.2.7.2, 10.3.2.4, 10.8.1.1, 10.8.1.3, 10.8.1.4, 10.8.1.5, 15.2.1.3, 15.2.1.4                                                                                                                                                                                                                                               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | CS, HS, DA                                                                                                                                                                                                                                                                                                                   | CS, HS, DA                                                                                                                                                                                                                                                                                                                   | CS, HS, DA                                                                                                                                                                                                                                                                                                                   |
| Description               | Specific NTC Data View values. Those data are sent by the STM when the data view procedure is triggered and the ERTMS/ETCS on-board has requested for the data. This packet can be grouped with other STM-183 packets by using the Q_FOLLOWING indicator in order to form one common set of 'Specific NTC Data View values'. | Specific NTC Data View values. Those data are sent by the STM when the data view procedure is triggered and the ERTMS/ETCS on-board has requested for the data. This packet can be grouped with other STM-183 packets by using the Q_FOLLOWING indicator in order to form one common set of 'Specific NTC Data View values'. | Specific NTC Data View values. Those data are sent by the STM when the data view procedure is triggered and the ERTMS/ETCS on-board has requested for the data. This packet can be grouped with other STM-183 packets by using the Q_FOLLOWING indicator in order to form one common set of 'Specific NTC Data View values'. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                                                     | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                                                     | From STM to ERTMS/ETCS on-board function                                                                                                                                                                                                                                                                                     |
| Content                   | Variable                                                                                                                                                                                                                                                                                                                     | Length                                                                                                                                                                                                                                                                                                                       | Comment                                                                                                                                                                                                                                                                                                                      |
|                           | NID_PACKET                                                                                                                                                                                                                                                                                                                   | 8                                                                                                                                                                                                                                                                                                                            | Packet identifier Value = 183                                                                                                                                                                                                                                                                                                |
|                           | L_PACKET                                                                                                                                                                                                                                                                                                                     | 13                                                                                                                                                                                                                                                                                                                           | Packet length                                                                                                                                                                                                                                                                                                                |
|                           | Q_FOLLOWING                                                                                                                                                                                                                                                                                                                  | 1                                                                                                                                                                                                                                                                                                                            | Indicate a following STM-183 packet                                                                                                                                                                                                                                                                                          |
|                           | N_ITER                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                              | Maximum iteration data =0 if there is 'No Specific Data Values' Maximum value = 15 Variable defined in Chapter 7 of [1]                                                                                                                                                                                                      |
|                           | NID_DATA(j)                                                                                                                                                                                                                                                                                                                  | 8                                                                                                                                                                                                                                                                                                                            | Identifier of the Specific NTC Data                                                                                                                                                                                                                                                                                          |
|                           | L_CAPTION(j)                                                                                                                                                                                                                                                                                                                 | 6                                                                                                                                                                                                                                                                                                                            | Length of X_CAPTION for data label in bytes Maximum value = 40                                                                                                                                                                                                                                                               |
|                           | X_CAPTION(j,q)                                                                                                                                                                                                                                                                                                               | 8                                                                                                                                                                                                                                                                                                                            | Data label caption text byte string                                                                                                                                                                                                                                                                                          |
|                           | L_VALUE(j)                                                                                                                                                                                                                                                                                                                   | 5                                                                                                                                                                                                                                                                                                                            | Length of X_VALUE for current value in bytes. Maximum value = 20 =0 if there is no current value                                                                                                                                                                                                                             |
|                           | X_VALUE(j,i)                                                                                                                                                                                                                                                                                                                 | 8                                                                                                                                                                                                                                                                                                                            | Data value caption text byte string                                                                                                                                                                                                                                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.21 Packet STM-184: Specific NTC Data Entry flag

| Subset-035 Ref.           | §8.3.1.5, 8.4.1.2, 8.4.1.3, 8.4.1.4, 10.7.3.1, 10.7.3.3, 10.7.4.1, 10.7.4.2, 10.7.4.3, 10.7.4.4, 10.7.5                                                                                                                                    | §8.3.1.5, 8.4.1.2, 8.4.1.3, 8.4.1.4, 10.7.3.1, 10.7.3.3, 10.7.4.1, 10.7.4.2, 10.7.4.3, 10.7.4.4, 10.7.5                                                                                                                                    | §8.3.1.5, 8.4.1.2, 8.4.1.3, 8.4.1.4, 10.7.3.1, 10.7.3.3, 10.7.4.1, 10.7.4.2, 10.7.4.3, 10.7.4.4, 10.7.5                                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | CO, DE, CS, HS, DA                                                                                                                                                                                                                         | CO, DE, CS, HS, DA                                                                                                                                                                                                                         | CO, DE, CS, HS, DA                                                                                                                                                                                                                         |
| Description               | Specific NTC Data Entry flag ERTMS/ETCS on-board shall indicate to the STM the beginning of its Specific NTC Data Entry procedure by sending the START flag and the end of its Specific NTC Data Entry procedure by sending the STOP flag. | Specific NTC Data Entry flag ERTMS/ETCS on-board shall indicate to the STM the beginning of its Specific NTC Data Entry procedure by sending the START flag and the end of its Specific NTC Data Entry procedure by sending the STOP flag. | Specific NTC Data Entry flag ERTMS/ETCS on-board shall indicate to the STM the beginning of its Specific NTC Data Entry procedure by sending the START flag and the end of its Specific NTC Data Entry procedure by sending the STOP flag. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                                                                                                                                                   | From ERTMS/ETCS on-board function to STM                                                                                                                                                                                                   | From ERTMS/ETCS on-board function to STM                                                                                                                                                                                                   |
| Content                   | Variable                                                                                                                                                                                                                                   | Length                                                                                                                                                                                                                                     | Comment                                                                                                                                                                                                                                    |
|                           | NID_PACKET                                                                                                                                                                                                                                 | 8                                                                                                                                                                                                                                          | Packet identifier Value = 184                                                                                                                                                                                                              |
|                           | L_PACKET                                                                                                                                                                                                                                   | 13                                                                                                                                                                                                                                         | Packet length                                                                                                                                                                                                                              |
|                           | M_DATAENTRYFLAG                                                                                                                                                                                                                            | 1                                                                                                                                                                                                                                          | Indicate the beginning or the end of the Specific NTC Data Entry procedure to each STM.                                                                                                                                                    |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.22 Packet STM-45: ETCS airgap message for STM

| Subset-035 Ref.           | §5.2.7.7, 10.2.1.2, 10.11.1.1, 10.11.1.2, 10.11.1.3   | §5.2.7.7, 10.2.1.2, 10.11.1.1, 10.11.1.2, 10.11.1.3   | §5.2.7.7, 10.2.1.2, 10.11.1.1, 10.11.1.2, 10.11.1.3                                                                                                                                                                                                                    |
|---------------------------|-------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                | PO, CO, DE, CS, HS, DA                                | PO, CO, DE, CS, HS, DA                                                                                                                                                                                                                                                 |
| Description               | ETCS airgap packet that is forwarded to STM.          | ETCS airgap packet that is forwarded to STM.          | ETCS airgap packet that is forwarded to STM.                                                                                                                                                                                                                           |
| Direction of information  | From ERTMS/ETCS on-board function to STM              | From ERTMS/ETCS on-board function to STM              | From ERTMS/ETCS on-board function to STM                                                                                                                                                                                                                               |
| Content                   | Variable                                              | Length                                                | Comment                                                                                                                                                                                                                                                                |
|                           | NID_PACKET                                            | 8                                                     | Packet identifier Value = 45                                                                                                                                                                                                                                           |
|                           | L_PACKET                                              | 13                                                    | Packet length                                                                                                                                                                                                                                                          |
|                           | D_ESTODO_BG                                           | 32                                                    | Value of the estimated distance given from the ERTMS/ETCS on- board Odometer Function (D_EST) at the location reference of the balise group, which transmitted the airgap message included within this packet, or the LRBG of the message if it was received by radio. |
|                           | N_LITER                                               | 8                                                     | Number of bytes in ETCS packet Maximum value = 222                                                                                                                                                                                                                     |
|                           | M_DATA(k)                                             | 8                                                     | Full ETCS packet 44 (containing also ETCS packet number…) See also 6.1.3.18                                                                                                                                                                                            |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.23 Packet STM-21: Test Procedure Permission Request

| Subset-035 Ref.           | §5.2.7.5, 10.9.1.1, 10.9.1.2             | §5.2.7.5, 10.9.1.1, 10.9.1.2             | §5.2.7.5, 10.9.1.1, 10.9.1.2             |
|---------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                   | PO, CO, DE, CS, HS, DA                   | PO, CO, DE, CS, HS, DA                   |
| Description               | Request to perform a Test Procedure      | Request to perform a Test Procedure      | Request to perform a Test Procedure      |
| Direction of information  | From STM to ERTMS/ETCS on-board function | From STM to ERTMS/ETCS on-board function | From STM to ERTMS/ETCS on-board function |
| Content                   | Variable                                 | Length                                   | Comment                                  |
|                           | NID_PACKET                               | 8                                        | Packet identifier Value = 21             |
|                           | L_PACKET                                 | 13                                       | Packet length                            |
|                           | NID_TEST                                 | 8                                        | Test Identity                            |

## 7.2.24 Packet STM-22: Test Procedure Permission

| Subset-035 Ref.           | §5.2.7.5, 10.9.1.2, 10.9.1.3                  | §5.2.7.5, 10.9.1.2, 10.9.1.3                  | §5.2.7.5, 10.9.1.2, 10.9.1.3                  |
|---------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                        | PO, CO, DE, CS, HS, DA                        | PO, CO, DE, CS, HS, DA                        |
| Description               | Grant permission to perform a Test Procedure. | Grant permission to perform a Test Procedure. | Grant permission to perform a Test Procedure. |
| Direction of information  | From ERTMS/ETCS on-board function to STM      | From ERTMS/ETCS on-board function to STM      | From ERTMS/ETCS on-board function to STM      |
| Content                   | Variable                                      | Length                                        | Comment                                       |
|                           | NID_PACKET                                    | 8                                             | Packet identifier Value = 22                  |
|                           | L_PACKET                                      | 13                                            | Packet length                                 |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.25 Packet STM-23: End of Test Procedure

| Subset-035 Ref.           | §5.2.7.5, 10.9.1.3                             | §5.2.7.5, 10.9.1.3                             | §5.2.7.5, 10.9.1.3                                |
|---------------------------|------------------------------------------------|------------------------------------------------|---------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                         | PO, CO, DE, CS, HS, DA                         | PO, CO, DE, CS, HS, DA                            |
| Description               | Reports the end and result of a Test Procedure | Reports the end and result of a Test Procedure | Reports the end and result of a Test Procedure    |
| Direction of information  | From STM to ERTMS/ETCS on-board function       | From STM to ERTMS/ETCS on-board function       | From STM to ERTMS/ETCS on-board function          |
| Content                   | Variable                                       | Length                                         | Comment                                           |
|                           | NID_PACKET                                     | 8                                              | Packet identifier Value = 23                      |
|                           | L_PACKET                                       | 13                                             | Packet length                                     |
|                           | M_TESTOK                                       | 1                                              | 1=Test(s) successful                              |
|                           | L_TEXT                                         | 8                                              | Number of bytes in text string Maximum value = 80 |
|                           | X_TEXT(k)                                      | 8                                              | Text character                                    |

## 7.2.26 Packet STM-30: Driver language transmission

| Subset-035 Ref.           | §5.2.7.4, 10.6.1.1                       | §5.2.7.4, 10.6.1.1                       | §5.2.7.4, 10.6.1.1                       |
|---------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                   | PO, CO, DE, CS, HS, DA                   | PO, CO, DE, CS, HS, DA                   |
| Description               | Driver language selection.               | Driver language selection.               | Driver language selection.               |
| Direction of information  | From ERTMS/ETCS on-board function to STM | From ERTMS/ETCS on-board function to STM | From ERTMS/ETCS on-board function to STM |
| Content                   | Variable                                 | Length                                   | Comment                                  |
|                           | NID_PACKET                               | 8                                        | Packet identifier Value = 30             |
|                           | L_PACKET                                 | 13                                       | Packet length                            |
|                           | NID_DRV_LANG                             | 16                                       | Driver language selection                |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.27 Packet STM-31: Active DMI channel

| Subset-035 Ref.           | §10.1.1.5, 13.3.1.1, 13.3.1.2                | §10.1.1.5, 13.3.1.1, 13.3.1.2                | §10.1.1.5, 13.3.1.1, 13.3.1.2                |
|---------------------------|----------------------------------------------|----------------------------------------------|----------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                       | PO, CO, DE, CS, HS, DA                       | PO, CO, DE, CS, HS, DA                       |
| Description               | Informs the STM about the active DMI channel | Informs the STM about the active DMI channel | Informs the STM about the active DMI channel |
| Direction of information  | From ERTMS/ETCS on-board function to STM     | From ERTMS/ETCS on-board function to STM     | From ERTMS/ETCS on-board function to STM     |
| Content                   | Variable                                     | Length                                       | Comment                                      |
|                           | NID_PACKET                                   | 8                                            | Packet identifier Value = 31                 |
|                           | L_PACKET                                     | 13                                           | Packet length                                |
|                           | NID_DMICHANNEL                               | 3                                            | Active DMI channel identifier                |

## 7.2.28 Packet STM-20: Antenna/BTM ID

| Subset-035 Ref.           | §5.2.7.11, 10.15                                                                             | §5.2.7.11, 10.15                                                                             | §5.2.7.11, 10.15                                                                             |
|---------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                       | PO, CO, DE, CS, HS, DA                                                                       | PO, CO, DE, CS, HS, DA                                                                       |
| Description               | Identifier of the ERTMS/ETCS on-board Antenna/BTM that is currently active on Interface 'K'. | Identifier of the ERTMS/ETCS on-board Antenna/BTM that is currently active on Interface 'K'. | Identifier of the ERTMS/ETCS on-board Antenna/BTM that is currently active on Interface 'K'. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                     | From ERTMS/ETCS on-board function to STM                                                     | From ERTMS/ETCS on-board function to STM                                                     |
| Content                   | Variable                                                                                     | Length                                                                                       | Comment                                                                                      |
|                           | NID_PACKET                                                                                   | 8                                                                                            | Packet identifier Value = 20                                                                 |
|                           | L_PACKET                                                                                     | 13                                                                                           | Packet length                                                                                |
|                           | Q_CHECKNEEDED                                                                                | 1                                                                                            | Indicates if KER STM has to perform the check                                                |
|                           | Q_ANTN_BTM_ACTIVE                                                                            | 1                                                                                            | Only if Q_CHECKNEEDED=1 Indicates if there is an Antenna/BTM active                          |
|                           | NID_ANTENNA_BTM                                                                              | 2                                                                                            | Only if Q_ANTN_BTM_ACTIVE=1 Valid Antenna/BTM ID                                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.2.29 Packet STM-47: ETCS BTM status message to STM

| Subset-035 Ref.           | §5.2.7.12, 10.16                                                                                                           | §5.2.7.12, 10.16                                                                                                           | §5.2.7.12, 10.16                                                                                                           |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                                                                     | PO, CO, DE, CS, HS, DA                                                                                                     | PO, CO, DE, CS, HS, DA                                                                                                     |
| Description               | Indicates the start and stop of BTM alarms and if a Big Metal Mass track condition has been announced in case of BTM alarm | Indicates the start and stop of BTM alarms and if a Big Metal Mass track condition has been announced in case of BTM alarm | Indicates the start and stop of BTM alarms and if a Big Metal Mass track condition has been announced in case of BTM alarm |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                                   | From ERTMS/ETCS on-board function to STM                                                                                   | From ERTMS/ETCS on-board function to STM                                                                                   |
| Content                   | Variable                                                                                                                   | Length                                                                                                                     | Comment                                                                                                                    |
|                           | NID_PACKET                                                                                                                 | 8                                                                                                                          | Packet identifier Value = 47                                                                                               |
|                           | L_PACKET                                                                                                                   | 13                                                                                                                         | Packet length                                                                                                              |
|                           | Q_BTM_ALARM                                                                                                                | 1                                                                                                                          | BTM alarm status                                                                                                           |
|                           | Q_BMM_ANNOUNCED                                                                                                            | 1                                                                                                                          | Only if Q_BTM_ALARM = 1, Announced Big Metal Mass                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.3 Packets related to the Odometer Function

## 7.3.1 Packet STM-9: Odometer parameters to STM

| Subset-035 Ref.           | §5.2.3.1, 6.5.1.5, 8.3.1.2, 12.4.1.1, 12.4.1.2, 12.4.1.4                                                                                | §5.2.3.1, 6.5.1.5, 8.3.1.2, 12.4.1.1, 12.4.1.2, 12.4.1.4                                                                                | §5.2.3.1, 6.5.1.5, 8.3.1.2, 12.4.1.1, 12.4.1.2, 12.4.1.4                                                                                |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | any state, multicast                                                                                                                    | any state, multicast                                                                                                                    | any state, multicast                                                                                                                    |
| Description               | Configuration data and performance parameters from the odometer. The packet is multicast by ERTMS/ETCS on-board from Odometer Function. | Configuration data and performance parameters from the odometer. The packet is multicast by ERTMS/ETCS on-board from Odometer Function. | Configuration data and performance parameters from the odometer. The packet is multicast by ERTMS/ETCS on-board from Odometer Function. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                                                                                                | From ERTMS/ETCS on-board function to STM                                                                                                | From ERTMS/ETCS on-board function to STM                                                                                                |
| Content                   | Variable                                                                                                                                | Length                                                                                                                                  | Comment                                                                                                                                 |
|                           | NID_PACKET                                                                                                                              | 8                                                                                                                                       | Packet identifier Value = 9                                                                                                             |
|                           | L_PACKET                                                                                                                                | 13                                                                                                                                      | Packet length                                                                                                                           |
|                           | T_ODOCYCLE                                                                                                                              | 8                                                                                                                                       | Typical cycle time of odometer function                                                                                                 |
|                           | T_ODOMAXPROD                                                                                                                            | 8                                                                                                                                       | Maximum production delay time.                                                                                                          |

<!-- image -->

## 7.3.2 Packet STM-8: Odometer multicast

Subset-035

§5.2.3.1, 5.3.1.1, 6.5.1.5, 12.1, 12.2, 12.3

Ref.

Allowed to send in states

Description any state, multicast

Periodic transmission of odometer data.

Direction of information

From ERTMS/ETCS on-board function to STM

| Content   | Variable   |   Length | Comment                                             |
|-----------|------------|----------|-----------------------------------------------------|
|           | NID_PACKET |        8 | Packet identifier Value = 8                         |
|           | L_PACKET   |       13 | Packet length                                       |
|           | T_ODO      |       32 | Timestamp                                           |
|           | V_MAX      |       16 | Upper bound of the measured speed.                  |
|           | V_EST      |       16 | Estimated speed value.                              |
|           | V_MIN      |       16 | Lower bound of the measured speed.                  |
|           | D_MAX      |       32 | Positive direction side of the confidence interval. |
|           | D_EST      |       32 | Estimated value of distance.                        |
|           | D_MIN      |       32 | Negative direction side of the confidence interval. |
|           | D_RES      |        8 | Resolution of distance measurement.                 |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.4 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5 Packets related to the DMI Function

## 7.5.1 Intentionally deleted

## 7.5.2 Packet STM-32: Button Request

| Subset-035 Ref.          | §5.2.8.1 a), 13.4.1, 13.4.4, 13.5.1.1.4, 13.5.1.1.5, 13.5.1.1.8, 15.1.1.1 b)               | §5.2.8.1 a), 13.4.1, 13.4.4, 13.5.1.1.4, 13.5.1.1.5, 13.5.1.1.8, 15.1.1.1 b)               | §5.2.8.1 a), 13.4.1, 13.4.4, 13.5.1.1.4, 13.5.1.1.5, 13.5.1.1.8, 15.1.1.1 b)               |
|--------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Allowed to send in state | HS, DA                                                                                     | HS, DA                                                                                     | HS, DA                                                                                     |
| Description              | Create or update the visual states of buttons by STM. Only referenced buttons are updated. | Create or update the visual states of buttons by STM. Only referenced buttons are updated. | Create or update the visual states of buttons by STM. Only referenced buttons are updated. |
| Direction of information | From STM to ERTMS/ETCS on-board function                                                   | From STM to ERTMS/ETCS on-board function                                                   | From STM to ERTMS/ETCS on-board function                                                   |
| Content                  | Variable                                                                                   | Length                                                                                     | Comment                                                                                    |
|                          | NID_PACKET                                                                                 | 8                                                                                          | Packet identifier Value=32                                                                 |
|                          | L_PACKET                                                                                   | 13                                                                                         | Packet length                                                                              |
|                          | N_ITER                                                                                     |                                                                                            | Maximum value = 24 Variable defined in Chapter 7 of [1]                                    |
|                          | NID_BUTTON(k)                                                                              | 8                                                                                          | Button identifier                                                                          |
|                          | NID_BUTPOS(k)                                                                              | 5                                                                                          | Button position identifier                                                                 |
|                          | NID_ICON(k)                                                                                | 8                                                                                          | Icon identifier                                                                            |
|                          | M_BUT_ATTRIB(k)                                                                            | 10                                                                                         | Attributes of the button                                                                   |
|                          | L_CAPTION(k)                                                                               | 6                                                                                          | Length of X_CAPTION in bytes Maximum value = 24                                            |
|                          | X_CAPTION(k, j)                                                                            | 8                                                                                          | Caption text bytestring                                                                    |

<!-- image -->

## 7.5.3 Packet STM-34: Button event report

| Subset-035 Ref.           | §5.2.8.1 a), 13.4.1, 13.4.4              | §5.2.8.1 a), 13.4.1, 13.4.4              | §5.2.8.1 a), 13.4.1, 13.4.4                                          |
|---------------------------|------------------------------------------|------------------------------------------|----------------------------------------------------------------------|
| Allowed to send in states | DA                                       | DA                                       | DA                                                                   |
| Description               | Report the button events.                | Report the button events.                | Report the button events.                                            |
| Direction of information  | From ERTMS/ETCS on-board function to STM | From ERTMS/ETCS on-board function to STM | From ERTMS/ETCS on-board function to STM                             |
| Content                   | Variable                                 | Length                                   | Comment                                                              |
|                           | NID_PACKET                               | 8                                        | Packet identifier Value=34                                           |
|                           | L_PACKET                                 | 13                                       | Packet length                                                        |
|                           | N_ITER                                   |                                          | Number of events being reported Variable defined in Chapter 7 of [1] |
|                           | NID_BUTTON(k)                            | 8                                        | Button identifier                                                    |
|                           | Q_BUTTON(k)                              | 1                                        | Button event                                                         |
|                           | T_BUTTONEVENT(k)                         | 32                                       | Event timestamp                                                      |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5.4 Packet STM-35: Indicator request

| Subset-035 Ref.           | §5.2.8.1 b), 13.4.1, 13.4.3, 13.5.1.1.2, 13.5.1.1.3, 13.5.1.1.8, 15.1.1.1 b)                     | §5.2.8.1 b), 13.4.1, 13.4.3, 13.5.1.1.2, 13.5.1.1.3, 13.5.1.1.8, 15.1.1.1 b)                     | §5.2.8.1 b), 13.4.1, 13.4.3, 13.5.1.1.2, 13.5.1.1.3, 13.5.1.1.8, 15.1.1.1 b)                     |
|---------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Allowed to send in states | HS, DA                                                                                           | HS, DA                                                                                           | HS, DA                                                                                           |
| Description               | Create or update the visual states of indicators by STM. Only referenced indicators are updated. | Create or update the visual states of indicators by STM. Only referenced indicators are updated. | Create or update the visual states of indicators by STM. Only referenced indicators are updated. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                         | From STM to ERTMS/ETCS on-board function                                                         | From STM to ERTMS/ETCS on-board function                                                         |
| Content                   | Variable                                                                                         | Length                                                                                           | Comment                                                                                          |
|                           | NID_PACKET                                                                                       | 8                                                                                                | Packet identifier Value = 35                                                                     |
|                           | L_PACKET                                                                                         | 13                                                                                               | Packet length                                                                                    |
|                           | N_ITER                                                                                           |                                                                                                  | Maximum value = 24 Variable defined in Chapter 7 of [1]                                          |
|                           | NID_INDICATOR(k)                                                                                 | 8                                                                                                | Indicator identifier                                                                             |
|                           | NID_INDPOS(k)                                                                                    | 5                                                                                                | Indicator position identifier                                                                    |
|                           | NID_ICON(k)                                                                                      | 8                                                                                                | Icon identifier                                                                                  |
|                           | M_IND_ATTRIB(k)                                                                                  | 10                                                                                               | Attributes of the indicator                                                                      |
|                           | L_CAPTION(k)                                                                                     | 6                                                                                                | Length of X_CAPTION Maximum value = 24                                                           |
|                           | X_CAPTION(k,j)                                                                                   | 8                                                                                                | Caption text bytestring                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5.5 Packet STM-38: Text message

| Subset-035 Ref.           | §5.2.8.1 d), 13.4.2, 15.1.1.1 a)                            | §5.2.8.1 d), 13.4.2, 15.1.1.1 a)                            | §5.2.8.1 d), 13.4.2, 15.1.1.1 a)                            |
|---------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Allowed to send in states | HS, DA                                                      | HS, DA                                                      | HS, DA                                                      |
| Description               | Text messages for the DMI, with or without acknowledgement. | Text messages for the DMI, with or without acknowledgement. | Text messages for the DMI, with or without acknowledgement. |
| Direction of information  | From STM to ERTMS/ETCS on-board function                    | From STM to ERTMS/ETCS on-board function                    | From STM to ERTMS/ETCS on-board function                    |
| Content                   | Variable                                                    | Length                                                      | Comment                                                     |
|                           | NID_PACKET                                                  | 8                                                           | Packet identifier Value = 38                                |
|                           | L_PACKET                                                    | 13                                                          | Packet length                                               |
|                           | NID_XMESSAGE                                                | 8                                                           | Text message identifier                                     |
|                           | M_XATTRIBUTE                                                | 10                                                          | Attributes of text                                          |
|                           | Q_ACK                                                       | 1                                                           | Acknowledgement qualifier                                   |
|                           | L_TEXT                                                      | 8                                                           | Number of bytes in text string Maximum value = 80           |
|                           | X_TEXT(k)                                                   | 8                                                           | Text character                                              |

## 7.5.6 Packet STM-39: Delete text message

| Subset-035 Ref.           | §5.2.8.1 d), 13.4.2                        | §5.2.8.1 d), 13.4.2                        | §5.2.8.1 d), 13.4.2                        |
|---------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Allowed to send in states | HS, DA                                     | HS, DA                                     | HS, DA                                     |
| Description               | STM commands the deletion of text message. | STM commands the deletion of text message. | STM commands the deletion of text message. |
| Direction of information  | From STM to ERTMS/ETCS on-board function   | From STM to ERTMS/ETCS on-board function   | From STM to ERTMS/ETCS on-board function   |
| Content                   | Variable                                   | Length                                     | Comment                                    |
|                           | NID_PACKET                                 | 8                                          | Packet identifier Value = 39               |
|                           | L_PACKET                                   | 13                                         | Packet length                              |
|                           | NID_XMESSAGE                               | 8                                          | Text message identifier                    |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5.7 Packet STM-40: Acknowledgement reply

| Subset-035 Ref.          | §5.2.8.1 d), 13.4.2                                                 | §5.2.8.1 d), 13.4.2                                                 | §5.2.8.1 d), 13.4.2                                                 |
|--------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Allowed to send in state | DA                                                                  | DA                                                                  | DA                                                                  |
| Description              | Report from ERTMS/ETCS on-board on acknowledgement of text message. | Report from ERTMS/ETCS on-board on acknowledgement of text message. | Report from ERTMS/ETCS on-board on acknowledgement of text message. |
| Direction of information | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            |
| Content                  | Variable                                                            | Length                                                              | Comment                                                             |
|                          | NID_PACKET                                                          | 8                                                                   | Packet identifier Value = 40                                        |
|                          | L_PACKET                                                            | 13                                                                  | Packet length                                                       |
|                          | NID_XMESSAGE                                                        | 8                                                                   | Text message identifier                                             |

## 7.5.8 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5.9 Packet STM-43: Speed and distance supervision information

| Subset-035 Ref.           | §5.2.8.1e), 13.4.6, 13.5.1.1.7                                                    | §5.2.8.1e), 13.4.6, 13.5.1.1.7                                                    | §5.2.8.1e), 13.4.6, 13.5.1.1.7                                                    |
|---------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Allowed to send in states | HS, DA                                                                            | HS, DA                                                                            | HS, DA                                                                            |
| Description               | Speed and distance supervision information with values, colours and display modes | Speed and distance supervision information with values, colours and display modes | Speed and distance supervision information with values, colours and display modes |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                          | From STM to ERTMS/ETCS on-board function                                          | From STM to ERTMS/ETCS on-board function                                          |
| Content                   | Variable                                                                          | Length                                                                            | Comment                                                                           |
|                           | NID_PACKET                                                                        | 8                                                                                 | Packet identifier Value = 43                                                      |
|                           | L_PACKET                                                                          | 13                                                                                | Packet length                                                                     |
|                           | Q_SCALE                                                                           |                                                                                   | Defined in Chapter 7 of [1]                                                       |
|                           | V_PERMIT                                                                          | 10                                                                                | Permitted speed                                                                   |
|                           | V_TARGET                                                                          | 7                                                                                 | Target speed                                                                      |
|                           | V_RELEASE                                                                         | 10                                                                                | Release speed                                                                     |
|                           | V_INTERV                                                                          | 10                                                                                | Intervention speed                                                                |
|                           | D_TARGET                                                                          | 15                                                                                | Target distance                                                                   |
|                           | M_COLOUR_SP                                                                       | 3                                                                                 | Colour of speed pointer                                                           |
|                           | M_COLOUR_PS                                                                       | 3                                                                                 | Colour of permitted speed                                                         |
|                           | Q_DISPLAY_PS                                                                      | 2                                                                                 | Display of permitted speed                                                        |
|                           | M_COLOUR_TS                                                                       | 3                                                                                 | Colour of target speed                                                            |
|                           | Q_DISPLAY_TS                                                                      | 2                                                                                 | Display of target speed                                                           |
|                           | M_COLOUR_RS                                                                       | 3                                                                                 | Colour of release speed                                                           |
|                           | Q_DISPLAY_RS                                                                      | 2                                                                                 | Display of release speed                                                          |
|                           | M_COLOUR_IS                                                                       | 3                                                                                 | Colour of intervention speed                                                      |
|                           | Q_DISPLAY_IS                                                                      | 2                                                                                 | Display of intervention speed                                                     |
|                           | Q_DISPLAY_TD                                                                      | 2                                                                                 | Display of target distance                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.5.10 Packet STM-46: Sound command

| Subset-035 Ref.           | §5.2.8.1.c), 13.4.1, 13.4.5, 13.5.1.1.9   | §5.2.8.1.c), 13.4.1, 13.4.5, 13.5.1.1.9   | §5.2.8.1.c), 13.4.1, 13.4.5, 13.5.1.1.9                                                                                                                                                              |
|---------------------------|-------------------------------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allowed to send in states | HS, DA                                    | HS, DA                                    | HS, DA                                                                                                                                                                                               |
| Description               | Commands sound.                           | Commands sound.                           | Commands sound.                                                                                                                                                                                      |
| Direction of information  | From STM to ERTMS/ETCS on-board function  | From STM to ERTMS/ETCS on-board function  | From STM to ERTMS/ETCS on-board function                                                                                                                                                             |
| Content                   | Variable                                  | Length                                    | Comment                                                                                                                                                                                              |
|                           | NID_PACKET                                | 8                                         | Packet identifier Value = 46                                                                                                                                                                         |
|                           | L_PACKET                                  | 13                                        | Packet length                                                                                                                                                                                        |
|                           | N_ITER                                    |                                           | Number of sounds to be generated Maximum value = 2 The STM is able to request to the ERTMS/ETCS on- board to generate a maximum of two sounds at the same time. Variable defined in Chapter 7 of [1] |
|                           | NID_SOUND(n)                              | 8                                         | Sound identifier                                                                                                                                                                                     |
|                           | Q_SOUND(n)                                | 2                                         | Continuous/ Not continuous/ Stopped                                                                                                                                                                  |
|                           | N_ITER(n)                                 |                                           | Number of segments of sound Variable defined in Chapter 7 of [1]                                                                                                                                     |
|                           | M_FREQ (n,k)                              | 8                                         | Frequency of a segment                                                                                                                                                                               |
|                           | T_SOUND(n,k)                              | 8                                         | Duration of segment                                                                                                                                                                                  |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.6 Intentionally deleted

© This document has been developed and released by UNISIG

<!-- image -->

## 7.7 Packets related to the TIU Function

## 7.7.1 Packet STM-129: STM specific brake control command

| Subset-035 Ref.           | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5,     | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5,     | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5,           |
|---------------------------|------------------------------------------|------------------------------------------|------------------------------------------------|
| Allowed to send in states | DA                                       | DA                                       | DA                                             |
| Description               | STM specific brake command control.      | STM specific brake command control.      | STM specific brake command control.            |
| Direction of information  | From STM to ERTMS/ETCS on-board function | From STM to ERTMS/ETCS on-board function | From STM to ERTMS/ETCS on-board function       |
| Content                   | Variable                                 | Length                                   | Comment                                        |
|                           | NID_PACKET                               | 8                                        | Packet identifier Value = 129                  |
|                           | L_PACKET                                 | 13                                       | Packet length                                  |
|                           | M_TIRB_CMD                               | 2                                        | Inhibit regenerative brake                     |
|                           | M_TIMSH_CMD                              | 2                                        | Inhibit magnetic shoes brake                   |
|                           | M_TIEDCBEB_CMD                           | 2                                        | Inhibit Eddy current brake for Emergency Brake |
|                           | M_TIEDCBSB_CMD                           | 2                                        | Inhibit Eddy current brake for Service Brake   |

<!-- image -->

## 7.7.2 Packet STM-130: STM commands to train interface

| Subset-035 Ref.          | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5                      | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5                      | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5                      |
|--------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Allowed to send in state | DA                                                       | DA                                                       | DA                                                       |
| Description              | Transmission of the STM commands to the train interface. | Transmission of the STM commands to the train interface. | Transmission of the STM commands to the train interface. |
| Direction of information | From STM to ERTMS/ETCS on-board function                 | From STM to ERTMS/ETCS on-board function                 | From STM to ERTMS/ETCS on-board function                 |
| Content                  | Variable                                                 | Length                                                   | Comment                                                  |
|                          | NID_PACKET                                               | 8                                                        | Packet identifier Value = 130                            |
|                          | L_PACKET                                                 | 13                                                       | Packet length                                            |
|                          | M_TIPANTO_CMD                                            | 2                                                        | Pantograph                                               |
|                          | M_TIFLAP_CMD                                             | 2                                                        | Air tightness                                            |
|                          | M_TIMS_CMD                                               | 2                                                        | Main switch/Circuit breaker                              |
|                          | M_TITR_C_CMD                                             | 2                                                        | Traction cut-off                                         |

## 7.7.3 Packet STM-139: Train interface inputs status/availability to STM

| Subset-035 Ref.           | §5.2.4.1, 5.2.4.4, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1      | §5.2.4.1, 5.2.4.4, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1      | §5.2.4.1, 5.2.4.4, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1      |
|---------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                                 | PO, CO, DE, CS, HS, DA                                                 | PO, CO, DE, CS, HS, DA                                                 |
| Description               | Transmission of the train interface inputs status/availability to STM. | Transmission of the train interface inputs status/availability to STM. | Transmission of the train interface inputs status/availability to STM. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                               | From ERTMS/ETCS on-board function to STM                               | From ERTMS/ETCS on-board function to STM                               |
| Content                   | Variable                                                               | Length                                                                 | Comment                                                                |
|                           | NID_PACKET                                                             | 8                                                                      | Packet identifier Value = 139                                          |
|                           | L_PACKET                                                               | 13                                                                     | Packet length                                                          |
|                           | M_TITR_STATUS                                                          | 2                                                                      | Traction status                                                        |
|                           | M_TIDIR_STATUS                                                         | 3                                                                      | Direction Controller position                                          |
|                           | M_TICAB_STATUS                                                         | 2                                                                      | Cab status                                                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.7.4 Packet STM-141: Train interface command configuration to STM

| Subset-035 Ref.           | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1   | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1   | §5.2.4.1, 5.2.4.3, 5.3.1.1, 6.5.1.5, 8.3.1.2, 8.3.1.2.1, 11.1.1.1   |
|---------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                              | PO, CO, DE, CS, HS, DA                                              | PO, CO, DE, CS, HS, DA                                              |
| Description               | Transmission of the train interface commands availability to STM.   | Transmission of the train interface commands availability to STM.   | Transmission of the train interface commands availability to STM.   |
| Direction of information  | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            |
| Content                   | Variable                                                            | Length                                                              | Comment                                                             |
|                           | NID_PACKET                                                          | 8                                                                   | Packet identifier Value = 141                                       |
|                           | L_PACKET                                                            | 13                                                                  | Packet length                                                       |
|                           | M_TIRB_CMD_AVAIL                                                    | 1                                                                   | Inhibit regenerative brake command availability                     |
|                           | M_TIMSH_CMD_AVAIL                                                   | 1                                                                   | Inhibit magnetic shoes brake command availability                   |
|                           | M_TIEDCBEB_CMD_AVAIL                                                | 1                                                                   | Inhibit Eddy current brake for Emergency Brake command availability |
|                           | M_TIEDCBSB_CMD_AVAIL                                                | 1                                                                   | Inhibit Eddy current brake for Service Brake command availability   |
|                           | M_TIPANTO_CMD_AVAIL                                                 | 1                                                                   | Pantograph command availability                                     |
|                           | M_TIFLAP_CMD_AVAIL                                                  | 1                                                                   | Air tightness command availability                                  |
|                           | M_TIMS_CMD_AVAIL                                                    | 1                                                                   | Main switch/Circuit breaker command availability                    |
|                           | M_TITR_C_CMD_AVAIL                                                  | 1                                                                   | Traction cut-off command availability                               |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.8 Packets related to the BIU Function

## 7.8.1 Packet STM-128: STM emergency and service brake command to brake interface

| Subset-035 Ref.          | §5.2.5.1, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.7.3.9, 11.1.1.3        | §5.2.5.1, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.7.3.9, 11.1.1.3        | §5.2.5.1, 10.3.3.3, 10.3.3.4, 10.3.3.6, 10.7.3.9, 11.1.1.3        |
|--------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Allowed to send in state | DA                                                                | DA                                                                | DA                                                                |
| Description              | Transmission of the STM EB and SB command to the brake interface. | Transmission of the STM EB and SB command to the brake interface. | Transmission of the STM EB and SB command to the brake interface. |
| Direction of information | From STM to ERTMS/ETCS on-board function                          | From STM to ERTMS/ETCS on-board function                          | From STM to ERTMS/ETCS on-board function                          |
| Content                  | Variable                                                          | Length                                                            | Comment                                                           |
|                          | NID_PACKET                                                        | 8                                                                 | Packet identifier Value = 128                                     |
|                          | L_PACKET                                                          | 13                                                                | Packet length                                                     |
|                          | M_BIEB_CMD                                                        | 2                                                                 | EB command                                                        |
|                          | M_BISB_CMD                                                        | 2                                                                 | SB command                                                        |

## 7.8.2 Packet STM-136: Brake interface emergency and service brake status/availability to STM

| Subset-035 Ref.           | §5.2.5.1, 8.3.1.2, 11.1.1.3                             | §5.2.5.1, 8.3.1.2, 11.1.1.3                             | §5.2.5.1, 8.3.1.2, 11.1.1.3                             |
|---------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                  | PO, CO, DE, CS, HS, DA                                  | PO, CO, DE, CS, HS, DA                                  |
| Description               | Transmission of the brake status / availability to STM. | Transmission of the brake status / availability to STM. | Transmission of the brake status / availability to STM. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                | From ERTMS/ETCS on-board function to STM                | From ERTMS/ETCS on-board function to STM                |
| Content                   | Variable                                                | Length                                                  | Comment                                                 |
|                           | NID_PACKET                                              | 8                                                       | Packet identifier Value = 136                           |
|                           | L_PACKET                                                | 13                                                      | Packet length                                           |
|                           | M_BIEB_STATUS                                           | 2                                                       | EB status / availability                                |
|                           | M_BISB_STATUS                                           | 2                                                       | SB status / availability                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.8.3 Packet STM-143: Emergency and service brake parameters to STM

| Subset-035 Ref.           | §5.2.5.1, 8.3.1.2, 8.3.1.2.1, 11.1.1.2                              | §5.2.5.1, 8.3.1.2, 8.3.1.2.1, 11.1.1.2                              | §5.2.5.1, 8.3.1.2, 8.3.1.2.1, 11.1.1.2                              |
|---------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA                                              | PO, CO, DE, CS, HS, DA                                              | PO, CO, DE, CS, HS, DA                                              |
| Description               | Transmission of the train interface EB and SB configuration to STM. | Transmission of the train interface EB and SB configuration to STM. | Transmission of the train interface EB and SB configuration to STM. |
| Direction of information  | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            | From ERTMS/ETCS on-board function to STM                            |
| Content                   | Variable                                                            | Length                                                              | Comment                                                             |
|                           | NID_PACKET                                                          | 8                                                                   | Packet identifier Value = 143                                       |
|                           | L_PACKET                                                            | 13                                                                  | Packet length                                                       |
|                           | T_EB_MAXDELAY                                                       | 8                                                                   | Maximum emergency brake command issue time delay                    |
|                           | T_SB_MAXDELAY                                                       | 8                                                                   | Maximum service brake command issue time delay                      |

© This document has been developed and released by UNISIG

<!-- image -->

## 7.9 Packets related to the Juridical Data Function (JD)

## 7.9.1 Packet STM-161: STM information to JD

| Subset-035 Ref.           | §5.2.6.1, 5.3.1.1, 6.5.1.5, 14                                                            | §5.2.6.1, 5.3.1.1, 6.5.1.5, 14                                                            | §5.2.6.1, 5.3.1.1, 6.5.1.5, 14                                                            |
|---------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Allowed to send in states | PO, CO, DE, CS, HS, DA, FA                                                                | PO, CO, DE, CS, HS, DA, FA                                                                | PO, CO, DE, CS, HS, DA, FA                                                                |
| Description               | National STM data transmitted to the JD. (Structure of the data internal to each company) | National STM data transmitted to the JD. (Structure of the data internal to each company) | National STM data transmitted to the JD. (Structure of the data internal to each company) |
| Direction of information  | From STM to ERTMS/ETCS on-board function                                                  | From STM to ERTMS/ETCS on-board function                                                  | From STM to ERTMS/ETCS on-board function                                                  |
| Content                   | Variable                                                                                  | Length                                                                                    | Comment                                                                                   |
|                           | NID_PACKET                                                                                | 8                                                                                         | Packet identifier Value = 161                                                             |
|                           | L_PACKET                                                                                  | 13                                                                                        | Packet length                                                                             |
|                           | T_JD                                                                                      | 32                                                                                        | Time Stamp                                                                                |
|                           | N_LITER                                                                                   | 8                                                                                         | Number of data bytes in message Maximum value = 228                                       |
|                           | M_DATA(k)                                                                                 | 8                                                                                         | Information to JD                                                                         |

<!-- image -->

## 8. VARIABLES

## 8.1.1 D\_EST

| Name                    | Estimated value of a measured distance                                         | Estimated value of a measured distance                                         | Estimated value of a measured distance                                         |
|-------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Description             | Signed estimated value of a measured distance provided by the odometer to STM. | Signed estimated value of a measured distance provided by the odometer to STM. | Signed estimated value of a measured distance provided by the odometer to STM. |
| Length of variable      | Minimum Value                                                                  | Maximum Value                                                                  | Resolution/formula                                                             |
| 32 bits                 | - 2 147 483 648 cm                                                             | + 2 147 483 647 cm                                                             | Signed, unit 1 cm.                                                             |
| Special/Reserved Values |                                                                                |                                                                                |                                                                                |

## 8.1.2 D\_ESTODO\_BG

| Name                    | Estimated distance reference of the balise group                                                                                                                                                                                                                                                       | Estimated distance reference of the balise group                                                                                                                                                                                                                                                       | Estimated distance reference of the balise group                                                                                                                                                                                                                                                       |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Signed value of the estimated distance given from the ERTMS/ETCS on-board Odometer Function (D_EST) at the location reference of the balise group, which transmitted the airgap message included within this packet, or the LRBG of the message if it was received by radio. Coded as two's complement | Signed value of the estimated distance given from the ERTMS/ETCS on-board Odometer Function (D_EST) at the location reference of the balise group, which transmitted the airgap message included within this packet, or the LRBG of the message if it was received by radio. Coded as two's complement | Signed value of the estimated distance given from the ERTMS/ETCS on-board Odometer Function (D_EST) at the location reference of the balise group, which transmitted the airgap message included within this packet, or the LRBG of the message if it was received by radio. Coded as two's complement |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                                                          | Maximum Value                                                                                                                                                                                                                                                                                          | Resolution/formula                                                                                                                                                                                                                                                                                     |
| 32 bits                 | - 2 147 483 648 cm                                                                                                                                                                                                                                                                                     | + 2 147 483 647 cm                                                                                                                                                                                                                                                                                     | 1 cm                                                                                                                                                                                                                                                                                                   |
| Special/Reserved Values |                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                        |

## 8.1.3 D\_MAX

| Name                    | Upper bound of the confidence interval of a measured distance                                                                                                                                                                                                 | Upper bound of the confidence interval of a measured distance                                                                                                                                                                                                 | Upper bound of the confidence interval of a measured distance                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | D_MAX is defined as the most positive position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry.Coded as two's complement. | D_MAX is defined as the most positive position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry.Coded as two's complement. | D_MAX is defined as the most positive position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry.Coded as two's complement. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                 | Maximum Value                                                                                                                                                                                                                                                 | Resolution/formula                                                                                                                                                                                                                                            |
| 32 bits                 | - 2 147 483 648 cm                                                                                                                                                                                                                                            | + 2 147 483 647 cm                                                                                                                                                                                                                                            | Signed, unit 1 cm.                                                                                                                                                                                                                                            |
| Special/Reserved Values |                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                               |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.4 D\_MIN

| Name                    | Lower bound of the confidence interval of a measured distance                                                                                                                                                                                                 | Lower bound of the confidence interval of a measured distance                                                                                                                                                                                                 | Lower bound of the confidence interval of a measured distance                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | D_MIN is defined as the most negative position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry. Coded as two's complement | D_MIN is defined as the most negative position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry. Coded as two's complement | D_MIN is defined as the most negative position of the vehicle in the vehicle coordinate system at the time given in the odometer packet, with all over- and under-reading amounts accumulated since the last reset of the odometry. Coded as two's complement |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                 | Maximum Value                                                                                                                                                                                                                                                 | Resolution/formula                                                                                                                                                                                                                                            |
| 32 bits                 | - 2 147 483 648 cm                                                                                                                                                                                                                                            | + 2 147 483 647 cm                                                                                                                                                                                                                                            | Signed, unit 1 cm.                                                                                                                                                                                                                                            |
| Special/Reserved Values |                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                               |

## 8.1.5 D\_RES

| Name                           | Distance resolution                              | Distance resolution                                | Distance resolution                     |
|--------------------------------|--------------------------------------------------|----------------------------------------------------|-----------------------------------------|
| Description Length of variable | Current distance Odometer Function Minimum Value | resolution included in the the STMs. Maximum Value | from the ERTMS/ETCS Resolution/ formula |
| 8 bits                         | 0cm                                              | 255cm                                              | 1cm                                     |
| Special/Reserved Values        |                                                  |                                                    |                                         |

## 8.1.6 D\_STMSYS

| Name                    | STM system distance                                                                       | STM system distance                                                                       | STM system distance                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Description             | Distance to beginning of STM system speed area measured from the level transition border. | Distance to beginning of STM system speed area measured from the level transition border. | Distance to beginning of STM system speed area measured from the level transition border. |
| Length of variable      | Minimum Value                                                                             | Maximum Value                                                                             | Resolution/formula                                                                        |
| 15 bits                 | 0 m                                                                                       | 327.670 Km                                                                                | 10 m                                                                                      |
| Special/Reserved Values |                                                                                           |                                                                                           |                                                                                           |

## 8.1.7 D\_TARGET

| Name                    | Target distance   | Target distance   | Target distance                       |
|-------------------------|-------------------|-------------------|---------------------------------------|
| Description             | Target distance   | Target distance   | Target distance                       |
| Length of variable      | Minimum Value     | Maximum Value     | Resolution/formula                    |
| 15 bits                 | 0 m               | 327.660 Km        | 10 cm, 1 m or 10 m depends on Q_SCALE |
| Special/Reserved Values | 32767             | Unknown value     | Unknown value                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.8 L\_CAPTION

| Name                    | Length of caption text string in bytes for button, indicator and data.                                                                                                                                                                                                            | Length of caption text string in bytes for button, indicator and data.                                                                                                                                                                                                            | Length of caption text string in bytes for button, indicator and data.                                                                                                                                                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | L_CAPTION defines the length of a text caption bytestring (L_CAPTION * X_CAPTION) Additional restrictions for maximum allowed length are specified in the respective packet. Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. | L_CAPTION defines the length of a text caption bytestring (L_CAPTION * X_CAPTION) Additional restrictions for maximum allowed length are specified in the respective packet. Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. | L_CAPTION defines the length of a text caption bytestring (L_CAPTION * X_CAPTION) Additional restrictions for maximum allowed length are specified in the respective packet. Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                                     | Maximum Value                                                                                                                                                                                                                                                                     | Resolution/formula                                                                                                                                                                                                                                                                |
| 6 bits                  | 1                                                                                                                                                                                                                                                                                 | 63                                                                                                                                                                                                                                                                                | 1 byte                                                                                                                                                                                                                                                                            |
| Special/Reserved Values | 0                                                                                                                                                                                                                                                                                 | No X_CAPTION follows                                                                                                                                                                                                                                                              | No X_CAPTION follows                                                                                                                                                                                                                                                              |

## 8.1.9 L\_MESSAGE

| Name                    | Message length                                                                                                                                              | Message length                                                                                                                                              | Message length                                                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | L_MESSAGE indicates the length of the message in bytes, including all packets and all variables defined in the message header (NID_STM and L_MESSAGE also). | L_MESSAGE indicates the length of the message in bytes, including all packets and all variables defined in the message header (NID_STM and L_MESSAGE also). | L_MESSAGE indicates the length of the message in bytes, including all packets and all variables defined in the message header (NID_STM and L_MESSAGE also). |
| Length of variable      | Minimum Value                                                                                                                                               | Maximum Value                                                                                                                                               | Resolution/formula                                                                                                                                          |
| 8 bits                  | 5                                                                                                                                                           | 238                                                                                                                                                         | 1 Byte                                                                                                                                                      |
| Special/Reserved Values | 0-4                                                                                                                                                         | Reserved                                                                                                                                                    | Reserved                                                                                                                                                    |
| Special/Reserved Values | 239-255                                                                                                                                                     | Reserved                                                                                                                                                    | Reserved                                                                                                                                                    |

## 8.1.10 L\_PACKET

| Name                    | Packet length                                                                                                                                          | Packet length                                                                                                                                          | Packet length                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | L_PACKET indicates the length of the transmitted packet in bits, including NID_PACKET, L_PACKET, Q_SCALE (if included) and all other packet variables. | L_PACKET indicates the length of the transmitted packet in bits, including NID_PACKET, L_PACKET, Q_SCALE (if included) and all other packet variables. | L_PACKET indicates the length of the transmitted packet in bits, including NID_PACKET, L_PACKET, Q_SCALE (if included) and all other packet variables. |
| Length of variable      | Minimum Value                                                                                                                                          | Maximum Value                                                                                                                                          | Resolution/formula                                                                                                                                     |
| 13 bits                 | 0                                                                                                                                                      | 1888 As allowed by maximum length of application                                                                                                       | 1 bit                                                                                                                                                  |
| Special/Reserved Values | 1889-8191                                                                                                                                              | Spare                                                                                                                                                  | Spare                                                                                                                                                  |

## 8.1.11 L\_TEXT

| Name                    | Length of text string in bytes                                                                                                                          | Length of text string in bytes                                                                                                                          | Length of text string in bytes                                                                                                                          |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | L_TEXT defines the length of a text string (L_TEXT * X_TEXT) Additional restrictions for maximum allowed length are specified in the respective packet. | L_TEXT defines the length of a text string (L_TEXT * X_TEXT) Additional restrictions for maximum allowed length are specified in the respective packet. | L_TEXT defines the length of a text string (L_TEXT * X_TEXT) Additional restrictions for maximum allowed length are specified in the respective packet. |
| Length of variable      | Minimum Value                                                                                                                                           | Maximum Value                                                                                                                                           | Resolution/formula                                                                                                                                      |
| 8 bits                  | 1                                                                                                                                                       | 255                                                                                                                                                     | 1 byte                                                                                                                                                  |
| Special/Reserved Values | 0                                                                                                                                                       | No X_TEXT follows                                                                                                                                       | No X_TEXT follows                                                                                                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.12 L\_VALUE

| Name                    | Length of text string in bytes for value used for data value, default value of data and for dedicated keyboard values.                                                                    | Length of text string in bytes for value used for data value, default value of data and for dedicated keyboard values.                                                                    | Length of text string in bytes for value used for data value, default value of data and for dedicated keyboard values.                                                                    |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | L_VALUE defines the length of a data caption bytestring in bytes (L_VALUE * X_VALUE) Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. | L_VALUE defines the length of a data caption bytestring in bytes (L_VALUE * X_VALUE) Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. | L_VALUE defines the length of a data caption bytestring in bytes (L_VALUE * X_VALUE) Additional restrictions for maximum length in character in UTF-8 coding are found in [4] chapter 15. |
| Length of variable      | Minimum Value                                                                                                                                                                             | Maximum Value                                                                                                                                                                             | Resolution/formula                                                                                                                                                                        |
| 5 bits                  | 1                                                                                                                                                                                         | 20                                                                                                                                                                                        | 1 Text String byte Element                                                                                                                                                                |
| Special/Reserved Values | 0                                                                                                                                                                                         | No X_VALUE shall follow.                                                                                                                                                                  | No X_VALUE shall follow.                                                                                                                                                                  |
| Special/Reserved Values | 21-31                                                                                                                                                                                     | Reserved                                                                                                                                                                                  | Reserved                                                                                                                                                                                  |

## 8.1.13 M\_BIEB\_CMD

| Name                    | Emergency brake command                                            | Emergency brake command                                            | Emergency brake command                                            |
|-------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Description             | Information telling if the emergency brake must be applied or not. | Information telling if the emergency brake must be applied or not. | Information telling if the emergency brake must be applied or not. |
| Length of variable      | Minimum Value                                                      | Maximum Value                                                      | Resolution/formula                                                 |
| 2 bits                  |                                                                    |                                                                    |                                                                    |
| Special/Reserved Values | 00                                                                 | Reserved                                                           |                                                                    |
| Special/Reserved Values | 01                                                                 | Command to apply EB                                                |                                                                    |
| Special/Reserved Values | 10                                                                 | Command to release EB                                              |                                                                    |
| Special/Reserved Values | 11                                                                 | No command from STM ->Keep current output status                   | No command from STM ->Keep current output status                   |

## 8.1.14 M\_BIEB\_STATUS

| Name                    | Emergency brake availability status                                     | Emergency brake availability status                                     | Emergency brake availability status                                     |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Description             | Information telling if the emergency brake is failed, available or not. | Information telling if the emergency brake is failed, available or not. | Information telling if the emergency brake is failed, available or not. |
| Length of variable      | Minimum Value                                                           | Maximum Value                                                           | Resolution/formula                                                      |
| 2 bits                  |                                                                         |                                                                         |                                                                         |
| Special/Reserved Values | 00                                                                      | Fail                                                                    |                                                                         |
| Special/Reserved Values | 01                                                                      | Not available                                                           |                                                                         |
| Special/Reserved Values | 10                                                                      | Available                                                               |                                                                         |
| Special/Reserved Values | 11                                                                      | Reserved                                                                |                                                                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.15 M\_BISB\_CMD

| Name                    | Service brake command                                            | Service brake command                                            | Service brake command                                            |
|-------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Description             | Information telling if the service brake must be applied or not. | Information telling if the service brake must be applied or not. | Information telling if the service brake must be applied or not. |
| Length of variable      | Minimum Value                                                    | Maximum Value                                                    | Resolution/formula                                               |
| 2 bits                  |                                                                  |                                                                  |                                                                  |
| Special/Reserved Values | 00                                                               | Apply SB, or EB in case the SB fails to be applied               | Apply SB, or EB in case the SB fails to be applied               |
| Special/Reserved Values | 01                                                               | Apply SB                                                         | Apply SB                                                         |
| Special/Reserved Values | 10                                                               | Release SB                                                       | Release SB                                                       |
| Special/Reserved Values | 11                                                               | No command from STM ->Keep current output status                 | No command from STM ->Keep current output status                 |

## 8.1.16 M\_BISB\_STATUS

| Name                    | Service brake availability status                                     | Service brake availability status                                     | Service brake availability status                                     |
|-------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Description             | Information telling if the service brake is failed, available or not. | Information telling if the service brake is failed, available or not. | Information telling if the service brake is failed, available or not. |
| Length of variable      | Minimum Value                                                         | Maximum Value                                                         | Resolution/formula                                                    |
| 2 bits                  |                                                                       |                                                                       |                                                                       |
| Special/Reserved Values | 00                                                                    | Fail                                                                  |                                                                       |
| Special/Reserved Values | 01                                                                    | Not available                                                         |                                                                       |
| Special/Reserved Values | 10                                                                    | Available                                                             |                                                                       |
| Special/Reserved Values | 11                                                                    | Reserved                                                              |                                                                       |

## 8.1.17

## M\_BRAKE\_PERCENTAGE\_STM

| Name                    | Brake percentage                                  | Brake percentage                                  | Brake percentage                                  |
|-------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Description             | Information telling actual brake percentage value | Information telling actual brake percentage value | Information telling actual brake percentage value |
| Length of variable      | Minimum Value                                     | Maximum Value                                     | Resolution/formula                                |
| 8 bits                  | 0                                                 | 250                                               |                                                   |
| Special/Reserved Values | 251-254                                           | Spare                                             |                                                   |
| Special/Reserved Values | 255                                               | Unknown value                                     |                                                   |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.18 M\_BUT\_ATTRIB

| Name                    | Attributes for buttons.                                        | Attributes for buttons.                                                                                                                    | Attributes for buttons.                                                                                                                    |
|-------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Specifies flashing mode, text & background colour for buttons. | Specifies flashing mode, text & background colour for buttons.                                                                             | Specifies flashing mode, text & background colour for buttons.                                                                             |
| Length of variable      | Minimum Value                                                  | Maximum Value                                                                                                                              | Resolution/formula                                                                                                                         |
| 10 bits                 |                                                                |                                                                                                                                            |                                                                                                                                            |
| Special/Reserved Values | 0xxxxxxxxx                                                     | Not displayed (Note: This allow to 'removing' a button from display.)                                                                      | Not displayed (Note: This allow to 'removing' a button from display.)                                                                      |
|                         | 10xxxxxxxx                                                     | Button Normal flashing (only relevant in case "Button Slow flashing" or "Button Fast flashing" is transmitted in the same variable).       | Button Normal flashing (only relevant in case "Button Slow flashing" or "Button Fast flashing" is transmitted in the same variable).       |
|                         | 11xxxxxxxx                                                     | Button Counterphase flashing (only relevant in case "Button Slow flashing" or "Button Fast flashing" is transmitted in the same variable). | Button Counterphase flashing (only relevant in case "Button Slow flashing" or "Button Fast flashing" is transmitted in the same variable). |
|                         | 1x00xxxxxx                                                     | Button No flashing                                                                                                                         | Button No flashing                                                                                                                         |
|                         | 1x01xxxxxx                                                     | Button Slow flashing                                                                                                                       | Button Slow flashing                                                                                                                       |
|                         | 1x10xxxxxx                                                     | Button Fast flashing                                                                                                                       | Button Fast flashing                                                                                                                       |
|                         | 1x11xxxxxx                                                     | Reserved                                                                                                                                   | Reserved                                                                                                                                   |
|                         | 1xxx000xxx                                                     | Dark blue button background                                                                                                                | Dark blue button background                                                                                                                |
|                         | 1xxx001xxx                                                     | White button background                                                                                                                    | White button background                                                                                                                    |
|                         | 1xxx010xxx                                                     | Red button background                                                                                                                      | Red button background                                                                                                                      |
|                         | 1xxx011xxx                                                     | Blue button background                                                                                                                     | Blue button background                                                                                                                     |
|                         | 1xxx100xxx                                                     | Green button background                                                                                                                    | Green button background                                                                                                                    |
|                         | 1xxx101xxx                                                     | Yellow button background                                                                                                                   | Yellow button background                                                                                                                   |
|                         | 1xxx110xxx                                                     | Light red button background                                                                                                                | Light red button background                                                                                                                |
|                         | 1xxx111xxx                                                     | Light green button background                                                                                                              | Light green button background                                                                                                              |
|                         | 1xxxxxx000                                                     | Black text label                                                                                                                           | Black text label                                                                                                                           |
|                         | 1xxxxxx001                                                     | White text label                                                                                                                           | White text label                                                                                                                           |
|                         | 1xxxxxx010                                                     | Red text label                                                                                                                             | Red text label                                                                                                                             |
|                         | 1xxxxxx011                                                     | Blue text label                                                                                                                            | Blue text label                                                                                                                            |
|                         | 1xxxxxx100                                                     | Green text label                                                                                                                           | Green text label                                                                                                                           |
|                         | 1xxxxxx101                                                     | Yellow text label                                                                                                                          | Yellow text label                                                                                                                          |
|                         | 1xxxxxx110                                                     | Light red text label                                                                                                                       | Light red text label                                                                                                                       |
|                         | 1xxxxxx111                                                     | Light green text label                                                                                                                     | Light green text label                                                                                                                     |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.19 M\_COLOUR\_IS

| Name                    | Colour for intervention speed                                                                                                       | Colour for intervention speed                                                                                                       | Colour for intervention speed                                                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Colour of intervention speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of intervention speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of intervention speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. |
| Length of variable      | Minimum Value                                                                                                                       | Maximum Value                                                                                                                       | Resolution/formula                                                                                                                  |
| 3 bits                  |                                                                                                                                     |                                                                                                                                     |                                                                                                                                     |
| Special/Reserved Values | 0                                                                                                                                   | White                                                                                                                               | White                                                                                                                               |
| Special/Reserved Values | 1                                                                                                                                   | Grey                                                                                                                                | Grey                                                                                                                                |
| Special/Reserved Values | 2                                                                                                                                   | Medium grey                                                                                                                         | Medium grey                                                                                                                         |
| Special/Reserved Values | 3                                                                                                                                   | Dark grey                                                                                                                           | Dark grey                                                                                                                           |
| Special/Reserved Values | 4                                                                                                                                   | Yellow                                                                                                                              | Yellow                                                                                                                              |
| Special/Reserved Values | 5                                                                                                                                   | Orange                                                                                                                              | Orange                                                                                                                              |
| Special/Reserved Values | 6                                                                                                                                   | Red                                                                                                                                 | Red                                                                                                                                 |
| Special/Reserved Values | 7                                                                                                                                   | Reserved                                                                                                                            | Reserved                                                                                                                            |

## 8.1.20 M\_COLOUR\_PS

| Name                    | Colour for permitted speed                                                                                                       | Colour for permitted speed                                                                                                       | Colour for permitted speed                                                                                                       |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Description             | Colour of permitted speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of permitted speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of permitted speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. |
| Length of variable      | Minimum Value                                                                                                                    | Maximum Value                                                                                                                    | Resolution/formula                                                                                                               |
| 3 bits                  |                                                                                                                                  |                                                                                                                                  |                                                                                                                                  |
| Special/Reserved Values | 0                                                                                                                                | White                                                                                                                            | White                                                                                                                            |
| Special/Reserved Values | 1                                                                                                                                | Grey                                                                                                                             | Grey                                                                                                                             |
| Special/Reserved Values | 2                                                                                                                                | Medium grey                                                                                                                      | Medium grey                                                                                                                      |
| Special/Reserved Values | 3                                                                                                                                | Dark grey                                                                                                                        | Dark grey                                                                                                                        |
| Special/Reserved Values | 4                                                                                                                                | Yellow                                                                                                                           | Yellow                                                                                                                           |
| Special/Reserved Values | 5                                                                                                                                | Orange                                                                                                                           | Orange                                                                                                                           |
| Special/Reserved Values | 6                                                                                                                                | Red                                                                                                                              | Red                                                                                                                              |
| Special/Reserved Values | 7                                                                                                                                | Reserved                                                                                                                         | Reserved                                                                                                                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.21 M\_COLOUR\_RS

| Name                    | Colour for release speed                                                                                                       | Colour for release speed                                                                                                       | Colour for release speed                                                                                                       |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Description             | Colour of release speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of release speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of release speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. |
| Length of variable      | Minimum Value                                                                                                                  | Maximum Value                                                                                                                  | Resolution/formula                                                                                                             |
| 3 bits                  |                                                                                                                                |                                                                                                                                |                                                                                                                                |
| Special/Reserved Values | 0                                                                                                                              | White                                                                                                                          | White                                                                                                                          |
| Special/Reserved Values | 1                                                                                                                              | Grey                                                                                                                           | Grey                                                                                                                           |
| Special/Reserved Values | 2                                                                                                                              | Medium grey                                                                                                                    | Medium grey                                                                                                                    |
| Special/Reserved Values | 3                                                                                                                              | Dark grey                                                                                                                      | Dark grey                                                                                                                      |
| Special/Reserved Values | 4                                                                                                                              | Yellow                                                                                                                         | Yellow                                                                                                                         |
| Special/Reserved Values | 5                                                                                                                              | Orange                                                                                                                         | Orange                                                                                                                         |
| Special/Reserved Values | 6                                                                                                                              | Red                                                                                                                            | Red                                                                                                                            |
| Special/Reserved Values | 7                                                                                                                              | Reserved                                                                                                                       | Reserved                                                                                                                       |

## 8.1.22 M\_COLOUR\_SP

| Name                    | Colour for speed pointer                                                                                            | Colour for speed pointer                                                                                            | Colour for speed pointer                                                                                            |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Description             | Colour of speed pointer for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of speed pointer for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of speed pointer for speed supervision Definition of these colours is identical to the one provided in [10]. |
| Length of variable      | Minimum Value                                                                                                       | Maximum Value                                                                                                       | Resolution/formula                                                                                                  |
| 3 bits                  |                                                                                                                     |                                                                                                                     |                                                                                                                     |
| Special/Reserved Values | 0                                                                                                                   | White                                                                                                               | White                                                                                                               |
| Special/Reserved Values | 1                                                                                                                   | Grey                                                                                                                | Grey                                                                                                                |
| Special/Reserved Values | 2                                                                                                                   | Medium grey                                                                                                         | Medium grey                                                                                                         |
| Special/Reserved Values | 3                                                                                                                   | Dark grey                                                                                                           | Dark grey                                                                                                           |
| Special/Reserved Values | 4                                                                                                                   | Yellow                                                                                                              | Yellow                                                                                                              |
| Special/Reserved Values | 5                                                                                                                   | Orange                                                                                                              | Orange                                                                                                              |
| Special/Reserved Values | 6                                                                                                                   | Red                                                                                                                 | Red                                                                                                                 |
| Special/Reserved Values | 7                                                                                                                   | Reserved                                                                                                            | Reserved                                                                                                            |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.23 M\_COLOUR\_TS

| Name                    | Colour for target speed                                                                                                       | Colour for target speed                                                                                                       | Colour for target speed                                                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Description             | Colour of target speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of target speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. | Colour of target speed indication for speed supervision Definition of these colours is identical to the one provided in [10]. |
| Length of variable      | Minimum Value                                                                                                                 | Maximum Value                                                                                                                 | Resolution/formula                                                                                                            |
| 3 bits                  |                                                                                                                               |                                                                                                                               |                                                                                                                               |
| Special/Reserved Values | 0                                                                                                                             | White                                                                                                                         |                                                                                                                               |
| Special/Reserved Values | 1                                                                                                                             | Grey                                                                                                                          |                                                                                                                               |
| Special/Reserved Values | 2                                                                                                                             | Medium grey                                                                                                                   |                                                                                                                               |
| Special/Reserved Values | 3                                                                                                                             | Dark grey                                                                                                                     |                                                                                                                               |
| Special/Reserved Values | 4                                                                                                                             | Yellow                                                                                                                        |                                                                                                                               |
| Special/Reserved Values | 5                                                                                                                             | Orange                                                                                                                        |                                                                                                                               |
| Special/Reserved Values | 6                                                                                                                             | Red                                                                                                                           |                                                                                                                               |
| Special/Reserved Values | 7                                                                                                                             | Reserved                                                                                                                      |                                                                                                                               |

## 8.1.24 M\_DATA

| Name                    | Data                                  | Data                                  | Data                                  |
|-------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| Description             | Data to be transmitted transparently. | Data to be transmitted transparently. | Data to be transmitted transparently. |
| Length of variable      | Minimum Value                         | Maximum Value                         | Resolution/formula                    |
| 8 bits                  | 0                                     | 255                                   |                                       |
| Special/Reserved Values |                                       |                                       |                                       |

## 8.1.25 M\_DATAENTRYFLAG

| Name                    | Specific NTC Data Entry flag                                                                                                                                           | Specific NTC Data Entry flag                                                                                                                                           | Specific NTC Data Entry flag                                                                                                                                           |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | It is sent before sending the first packet of ETCS Train Data, with the value START, and after finishing or aborting the Specific NTC Data Entry, with the value STOP. | It is sent before sending the first packet of ETCS Train Data, with the value START, and after finishing or aborting the Specific NTC Data Entry, with the value STOP. | It is sent before sending the first packet of ETCS Train Data, with the value START, and after finishing or aborting the Specific NTC Data Entry, with the value STOP. |
| Length of variable      | Minimum Value                                                                                                                                                          | Maximum Value                                                                                                                                                          | Resolution/formula                                                                                                                                                     |
| 1 bit                   |                                                                                                                                                                        |                                                                                                                                                                        |                                                                                                                                                                        |
| Special/Reserved Values | 0                                                                                                                                                                      | Stop                                                                                                                                                                   |                                                                                                                                                                        |
| Special/Reserved Values | 1                                                                                                                                                                      | Start                                                                                                                                                                  |                                                                                                                                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.26 M\_FREQ

| Name                    | Sound segment frequency     | Sound segment frequency     | Sound segment frequency              |
|-------------------------|-----------------------------|-----------------------------|--------------------------------------|
| Description             | Frequency of sound segment. | Frequency of sound segment. | Frequency of sound segment.          |
| Length of variable      | Minimum Value               | Maximum Value               | Resolution/formula                   |
| 8 bits                  | 128 Hz                      | 8160 Hz                     | F = M_FREQ * 32 Hz Resolution: 32 Hz |
| Special/Reserved Values | 0                           | Silence                     | Silence                              |
| Special/Reserved Values | 1                           | Spare                       | Spare                                |
| Special/Reserved Values | 2                           | Spare                       | Spare                                |
| Special/Reserved Values | 3                           | Spare                       | Spare                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.27 M\_IND\_ATTRIB

| Name                    | Attributes for indicators.                                        | Attributes for indicators.                                                                                                                          | Attributes for indicators.                                                                                                                          |
|-------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Specifies flashing mode, text & background colour for indicators. | Specifies flashing mode, text & background colour for indicators.                                                                                   | Specifies flashing mode, text & background colour for indicators.                                                                                   |
| Length of variable      | Minimum Value                                                     | Maximum Value                                                                                                                                       | Resolution/formula                                                                                                                                  |
| 10 bits                 |                                                                   |                                                                                                                                                     |                                                                                                                                                     |
| Special/Reserved Values | 0xxxxxxxxx                                                        | Not displayed (Note: This allow to 'removing' an indicator from display.)                                                                           | Not displayed (Note: This allow to 'removing' an indicator from display.)                                                                           |
|                         | 10xxxxxxxx                                                        | Indicator Normal flashing (only relevant in case "indicator slow flashing" or "Indicator Fast flashing" is transmitted in the same variable).       | Indicator Normal flashing (only relevant in case "indicator slow flashing" or "Indicator Fast flashing" is transmitted in the same variable).       |
|                         | 11xxxxxxxx                                                        | Indicator Counterphase flashing (only relevant in case "indicator slow flashing" or "Indicator Fast flashing" is transmitted in the same variable). | Indicator Counterphase flashing (only relevant in case "indicator slow flashing" or "Indicator Fast flashing" is transmitted in the same variable). |
|                         | 1x00xxxxxx                                                        | Indicator No flashing                                                                                                                               | Indicator No flashing                                                                                                                               |
|                         | 1x01xxxxxx                                                        | Indicator Slow flashing                                                                                                                             | Indicator Slow flashing                                                                                                                             |
|                         | 1x10xxxxxx                                                        | Indicator Fast flashing                                                                                                                             | Indicator Fast flashing                                                                                                                             |
|                         | 1x11xxxxxx                                                        | Reserved                                                                                                                                            | Reserved                                                                                                                                            |
|                         | 1xxx000xxx                                                        | Dark blue indicator background                                                                                                                      | Dark blue indicator background                                                                                                                      |
|                         | 1xxx001xxx                                                        | White indicator background                                                                                                                          | White indicator background                                                                                                                          |
|                         | 1xxx010xxx                                                        | Red indicator background                                                                                                                            | Red indicator background                                                                                                                            |
|                         | 1xxx011xxx                                                        | Blue indicator background                                                                                                                           | Blue indicator background                                                                                                                           |
|                         | 1xxx100xxx                                                        | Green indicator background                                                                                                                          | Green indicator background                                                                                                                          |
|                         | 1xxx101xxx                                                        | Yellow indicator background                                                                                                                         | Yellow indicator background                                                                                                                         |
|                         | 1xxx110xxx                                                        | Light red indicator background                                                                                                                      | Light red indicator background                                                                                                                      |
|                         | 1xxx111xxx                                                        | Light green indicator background                                                                                                                    | Light green indicator background                                                                                                                    |
|                         | 1xxxxxx000                                                        | Black text label                                                                                                                                    | Black text label                                                                                                                                    |
|                         | 1xxxxxx001                                                        | White text label                                                                                                                                    | White text label                                                                                                                                    |
|                         | 1xxxxxx010                                                        | Red text label                                                                                                                                      | Red text label                                                                                                                                      |
|                         | 1xxxxxx011                                                        | Blue text label                                                                                                                                     | Blue text label                                                                                                                                     |
|                         | 1xxxxxx100                                                        | Green text label                                                                                                                                    | Green text label                                                                                                                                    |
|                         | 1xxxxxx101                                                        | Yellow text label                                                                                                                                   | Yellow text label                                                                                                                                   |
|                         | 1xxxxxx110                                                        | Light red text label                                                                                                                                | Light red text label                                                                                                                                |
|                         | 1xxxxxx111                                                        | Light green text label                                                                                                                              | Light green text label                                                                                                                              |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.28 M\_MODESTM

| Name                    | On-board operating mode                                                                 | On-board operating mode                                                                 | On-board operating mode                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Description             | ETCS mode Different from M_MODE defined in [1] by the addition of Passive Shunting mode | ETCS mode Different from M_MODE defined in [1] by the addition of Passive Shunting mode | ETCS mode Different from M_MODE defined in [1] by the addition of Passive Shunting mode |
| Length of variable      | Minimum Value                                                                           | Maximum Value                                                                           | Resolution/formula                                                                      |
| 4 bits                  |                                                                                         |                                                                                         |                                                                                         |
| Special/Reserved Values | 0                                                                                       | Full Supervision                                                                        |                                                                                         |
| Special/Reserved Values | 1                                                                                       | On Sight                                                                                |                                                                                         |
| Special/Reserved Values | 2                                                                                       | Staff Responsible                                                                       |                                                                                         |
| Special/Reserved Values | 3                                                                                       | Shunting                                                                                |                                                                                         |
| Special/Reserved Values | 4                                                                                       | Unfitted                                                                                |                                                                                         |
| Special/Reserved Values | 5                                                                                       | Sleeping                                                                                |                                                                                         |
| Special/Reserved Values | 6                                                                                       | Stand By                                                                                |                                                                                         |
| Special/Reserved Values | 7                                                                                       | Trip                                                                                    |                                                                                         |
| Special/Reserved Values | 8                                                                                       | Post Trip                                                                               |                                                                                         |
| Special/Reserved Values | 9                                                                                       | System Failure                                                                          |                                                                                         |
| Special/Reserved Values | 10                                                                                      | Isolation                                                                               |                                                                                         |
| Special/Reserved Values | 11                                                                                      | Non Leading                                                                             |                                                                                         |
| Special/Reserved Values | 12                                                                                      | Limited Supervision                                                                     |                                                                                         |
| Special/Reserved Values | 13                                                                                      | National System                                                                         |                                                                                         |
| Special/Reserved Values | 14                                                                                      | Reversing                                                                               |                                                                                         |
| Special/Reserved Values | 15                                                                                      | Passive Shunting                                                                        |                                                                                         |

## 8.1.29 M\_TESTOK

Name

STM Test result

Description

Length of variable

1 bit

Special/Reserved Values

Indicates the result of the STM Test

Minimum Value

Maximum Value

0

1

Test(s) not successful

Test(s) successful

© This document has been developed and released by UNISIG

Resolution/formula

<!-- image -->

## 8.1.30 M\_TICAB\_STATUS

| Name                    | Cab status on Train Interface                                                                                                        | Cab status on Train Interface                                                                                                        | Cab status on Train Interface                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Information defining the active cab. For single cab locos with only one desk, this status provides the active virtual cab (see [3]). | Information defining the active cab. For single cab locos with only one desk, this status provides the active virtual cab (see [3]). | Information defining the active cab. For single cab locos with only one desk, this status provides the active virtual cab (see [3]). |
| Length of variable      | Minimum Value                                                                                                                        | Maximum Value                                                                                                                        | Resolution/formula                                                                                                                   |
| 2 bits                  |                                                                                                                                      |                                                                                                                                      |                                                                                                                                      |
| Special/Reserved Values | 00                                                                                                                                   | Fail state (information not received from Train Interface)                                                                           | Fail state (information not received from Train Interface)                                                                           |
| Special/Reserved Values | 01                                                                                                                                   | Cab A active                                                                                                                         | Cab A active                                                                                                                         |
| Special/Reserved Values | 10                                                                                                                                   | Cab B active                                                                                                                         | Cab B active                                                                                                                         |
| Special/Reserved Values | 11                                                                                                                                   | No cab active                                                                                                                        | No cab active                                                                                                                        |

## 8.1.31 M\_TIDIR\_STATUS

| Name                    | Direction handle train interface status                           | Direction handle train interface status                           | Direction handle train interface status                           |
|-------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Description             | Information defining the position of the driver direction handle. | Information defining the position of the driver direction handle. | Information defining the position of the driver direction handle. |
| Length of variable      | Minimum Value                                                     | Maximum Value                                                     | Resolution/formula                                                |
| 3 bits                  |                                                                   |                                                                   |                                                                   |
| Special/Reserved Values | 000                                                               | Fail state                                                        | Fail state                                                        |
| Special/Reserved Values | 001                                                               | Forward                                                           | Forward                                                           |
| Special/Reserved Values | 010                                                               | Neutral                                                           | Neutral                                                           |
| Special/Reserved Values | 011                                                               | Reserved                                                          | Reserved                                                          |
| Special/Reserved Values | 100                                                               | Backward                                                          | Backward                                                          |
| Special/Reserved Values | 101                                                               | Reserved                                                          | Reserved                                                          |
| Special/Reserved Values | 110                                                               | Reserved                                                          | Reserved                                                          |
| Special/Reserved Values | 111                                                               | Status information not available                                  | Status information not available                                  |

## 8.1.32 M\_TIEDCBEB\_CMD

| Name                    | Train interface for Eddy Current Brake for Emergency Brake command                                      | Train interface for Eddy Current Brake for Emergency Brake command                                      | Train interface for Eddy Current Brake for Emergency Brake command                                      |
|-------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Description             | Information telling if the eddy current brake system use is allowed for Emergency Brake command or not. | Information telling if the eddy current brake system use is allowed for Emergency Brake command or not. | Information telling if the eddy current brake system use is allowed for Emergency Brake command or not. |
| Length of variable      | Minimum Value                                                                                           | Maximum Value                                                                                           | Resolution/formula                                                                                      |
| 2 bits                  |                                                                                                         |                                                                                                         |                                                                                                         |
| Special/Reserved Values | 00                                                                                                      | Reserved                                                                                                | Reserved                                                                                                |
| Special/Reserved Values | 01                                                                                                      | Allow eddy current brake for Emergency Brake command (on)                                               | Allow eddy current brake for Emergency Brake command (on)                                               |
| Special/Reserved Values | 10                                                                                                      | Suppress eddy current brake for Emergency Brake command (off)                                           | Suppress eddy current brake for Emergency Brake command (off)                                           |
| Special/Reserved Values | 11                                                                                                      | No command from STM->Keep current output status                                                         | No command from STM->Keep current output status                                                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.33 M\_TIEDCBSB\_CMD

| Name                    | Train interface for Eddy Current Brake for Service Brake command                                      | Train interface for Eddy Current Brake for Service Brake command                                      | Train interface for Eddy Current Brake for Service Brake command                                      |
|-------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Description             | Information telling if the eddy current brake system use is allowed for Service Brake command or not. | Information telling if the eddy current brake system use is allowed for Service Brake command or not. | Information telling if the eddy current brake system use is allowed for Service Brake command or not. |
| Length of variable      | Minimum Value                                                                                         | Maximum Value                                                                                         | Resolution/formula                                                                                    |
| 2 bits                  |                                                                                                       |                                                                                                       |                                                                                                       |
| Special/Reserved Values | 00                                                                                                    | Reserved                                                                                              | Reserved                                                                                              |
| Special/Reserved Values | 01                                                                                                    | Allow eddy current brake for Service Brake command (on)                                               | Allow eddy current brake for Service Brake command (on)                                               |
| Special/Reserved Values | 10                                                                                                    | Suppress eddy current brake for Service Brake command (off)                                           | Suppress eddy current brake for Service Brake command (off)                                           |
| Special/Reserved Values | 11                                                                                                    | No command from STM->Keep current output status                                                       | No command from STM->Keep current output status                                                       |

## 8.1.34 M\_TIEDCBEB\_CMD\_AVAIL

| Name                    | Train interface for Eddy Current Brake for Emergency Brake command availability                               | Train interface for Eddy Current Brake for Emergency Brake command availability                               | Train interface for Eddy Current Brake for Emergency Brake command availability                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the eddy current brake system for Emergency Brake command is available or not. | Boolean information telling if the eddy current brake system for Emergency Brake command is available or not. | Boolean information telling if the eddy current brake system for Emergency Brake command is available or not. |
| Length of variable      | Minimum Value                                                                                                 | Maximum Value                                                                                                 | Resolution/formula                                                                                            |
| 1 bit                   |                                                                                                               |                                                                                                               |                                                                                                               |
| Special/Reserved Values | 0                                                                                                             | Eddy current brake system for Emergency Brake command is not available                                        | Eddy current brake system for Emergency Brake command is not available                                        |
| Special/Reserved Values | 1                                                                                                             | Eddy current brake system for Emergency Brake command is available                                            | Eddy current brake system for Emergency Brake command is available                                            |

## 8.1.35 M\_TIEDCBSB\_CMD\_AVAIL

| Name                    | Train interface for Eddy Current Brake for Service Brake command availability                               | Train interface for Eddy Current Brake for Service Brake command availability                               | Train interface for Eddy Current Brake for Service Brake command availability                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the eddy current brake system for Service Brake command is available or not. | Boolean information telling if the eddy current brake system for Service Brake command is available or not. | Boolean information telling if the eddy current brake system for Service Brake command is available or not. |
| Length of variable      | Minimum Value                                                                                               | Maximum Value                                                                                               | Resolution/formula                                                                                          |
| 1 bit                   |                                                                                                             |                                                                                                             |                                                                                                             |
| Special/Reserved Values | 0                                                                                                           | Eddy current brake system for Service Brake command is not available                                        | Eddy current brake system for Service Brake command is not available                                        |
| Special/Reserved Values | 1                                                                                                           | Eddy current brake system for Service Brake command is available                                            | Eddy current brake system for Service Brake command is available                                            |

## 8.1.36 M\_TIFLAP\_CMD

| Name                    | Air tightness/Flap control train interface command                      | Air tightness/Flap control train interface command                      | Air tightness/Flap control train interface command                      |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Description             | Information for opening or closing the Flap control (air conditioning). | Information for opening or closing the Flap control (air conditioning). | Information for opening or closing the Flap control (air conditioning). |
| Length of variable      | Minimum Value                                                           | Maximum Value                                                           | Resolution/formula                                                      |
| 2 bits                  |                                                                         |                                                                         |                                                                         |
| Special/Reserved Values | 00                                                                      | Reserved                                                                |                                                                         |
| Special/Reserved Values | 01                                                                      | Flap open (air conditioning on)                                         |                                                                         |
| Special/Reserved Values | 10                                                                      | Flap close (air conditioning off)                                       |                                                                         |
| Special/Reserved Values | 11                                                                      | No command from STM->Keep current output status                         | No command from STM->Keep current output status                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.37 M\_TIFLAP\_CMD\_AVAIL

| Name                    | Air tightness train interface command availability                                   | Air tightness train interface command availability                                   | Air tightness train interface command availability                                   |
|-------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the Air tightness system command is available or not. | Boolean information telling if the Air tightness system command is available or not. | Boolean information telling if the Air tightness system command is available or not. |
| Length of variable      | Minimum Value                                                                        | Maximum Value                                                                        | Resolution/formula                                                                   |
| 1 bits                  |                                                                                      |                                                                                      |                                                                                      |
| Special/Reserved Values | 0                                                                                    | Air tightness system command is not available                                        | Air tightness system command is not available                                        |
| Special/Reserved Values | 1                                                                                    | Air tightness system command is available                                            | Air tightness system command is available                                            |

## 8.1.38 M\_TIMS\_CMD

| Name                    | Main switch/Circuit breaker train interface command   | Main switch/Circuit breaker train interface command   | Main switch/Circuit breaker train interface command   |
|-------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Description             | Information for closing or opening the Main switch.   | Information for closing or opening the Main switch.   | Information for closing or opening the Main switch.   |
| Length of variable      | Minimum Value                                         | Maximum Value                                         | Resolution/formula                                    |
| 2 bits                  |                                                       |                                                       |                                                       |
| Special/Reserved Values | 00                                                    | Reserved                                              |                                                       |
| Special/Reserved Values | 01                                                    | Main switch close (on)                                |                                                       |
| Special/Reserved Values | 10                                                    | Main switch open (off)                                |                                                       |
| Special/Reserved Values | 11                                                    | No command from STM->Keep current output status       | No command from STM->Keep current output status       |

## 8.1.39 M\_TIMS\_CMD\_AVAIL

| Name                    | Main switch/Circuit breaker train interface command availability                                   | Main switch/Circuit breaker train interface command availability                                   | Main switch/Circuit breaker train interface command availability                                   |
|-------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the Main switch/Circuit breaker system command is available or not. | Boolean information telling if the Main switch/Circuit breaker system command is available or not. | Boolean information telling if the Main switch/Circuit breaker system command is available or not. |
| Length of variable      | Minimum Value                                                                                      | Maximum Value                                                                                      | Resolution/formula                                                                                 |
| 1 bits                  |                                                                                                    |                                                                                                    |                                                                                                    |
| Special/Reserved Values | 0                                                                                                  | Main switch/Circuit breaker system command is not available                                        | Main switch/Circuit breaker system command is not available                                        |
| Special/Reserved Values | 1                                                                                                  | Main switch/Circuit breaker system command is available                                            | Main switch/Circuit breaker system command is available                                            |

## 8.1.40 M\_TIMSH\_CMD

| Name                    | Magnetic brake system train interface command                           | Magnetic brake system train interface command                           | Magnetic brake system train interface command                           |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Description             | Information telling if the magnetic brake system use is allowed or not. | Information telling if the magnetic brake system use is allowed or not. | Information telling if the magnetic brake system use is allowed or not. |
| Length of variable      | Minimum Value                                                           | Maximum Value                                                           | Resolution/formula                                                      |
| 2 bits                  |                                                                         |                                                                         |                                                                         |
| Special/Reserved Values | 00                                                                      | Reserved                                                                |                                                                         |
| Special/Reserved Values | 01                                                                      | Allow MB (on)                                                           |                                                                         |
| Special/Reserved Values | 10                                                                      | Suppress MB (off)                                                       |                                                                         |
| Special/Reserved Values | 11                                                                      | No command from STM->Keep current output status                         | No command from STM->Keep current output status                         |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.41 M\_TIMSH\_CMD\_AVAIL

| Name                    | Magnetic shoe brake train interface command availability                                   | Magnetic shoe brake train interface command availability                                   | Magnetic shoe brake train interface command availability                                   |
|-------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the magnetic shoe brake system command is available or not. | Boolean information telling if the magnetic shoe brake system command is available or not. | Boolean information telling if the magnetic shoe brake system command is available or not. |
| Length of variable      | Minimum Value                                                                              | Maximum Value                                                                              | Resolution/formula                                                                         |
| 1 bits                  |                                                                                            |                                                                                            |                                                                                            |
| Special/Reserved Values | 0                                                                                          | Magnetic shoe brake system command is not available                                        | Magnetic shoe brake system command is not available                                        |
| Special/Reserved Values | 1                                                                                          | Magnetic shoe brake system command is available                                            | Magnetic shoe brake system command is available                                            |

## 8.1.42 M\_TIPANTO\_CMD

| Name                    | Pantograph train interface command                | Pantograph train interface command                | Pantograph train interface command                |
|-------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Description             | Information for lifting or lowering a pantograph. | Information for lifting or lowering a pantograph. | Information for lifting or lowering a pantograph. |
| Length of variable      | Minimum Value                                     | Maximum Value                                     | Resolution/formula                                |
| 2 bits                  |                                                   |                                                   |                                                   |
| Special/Reserved Values | 00                                                | Reserved                                          |                                                   |
| Special/Reserved Values | 01                                                | Pantograph lift                                   |                                                   |
| Special/Reserved Values | 10                                                | Pantograph lower                                  |                                                   |
| Special/Reserved Values | 11                                                | No command from STM->Keep current output status   | No command from STM->Keep current output status   |

## 8.1.43 M\_TIPANTO\_CMD\_AVAIL

| Name                    | Pantograph train interface command availability                                   | Pantograph train interface command availability                                   | Pantograph train interface command availability                                   |
|-------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Description             | Boolean information telling if the Pantograph system command is available or not. | Boolean information telling if the Pantograph system command is available or not. | Boolean information telling if the Pantograph system command is available or not. |
| Length of variable      | Minimum Value                                                                     | Maximum Value                                                                     | Resolution/formula                                                                |
| 1 bits                  |                                                                                   |                                                                                   |                                                                                   |
| Special/Reserved Values | 0                                                                                 | Pantograph system command is not available                                        | Pantograph system command is not available                                        |
| Special/Reserved Values | 1                                                                                 | Pantograph system command is available                                            | Pantograph system command is available                                            |

## 8.1.44 M\_TIRB\_CMD

| Name                    | Regenerative brake train interface command                                  | Regenerative brake train interface command                                  | Regenerative brake train interface command                                  |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Description             | Information telling if the regenerative brake system use is allowed or not. | Information telling if the regenerative brake system use is allowed or not. | Information telling if the regenerative brake system use is allowed or not. |
| Length of variable      | Minimum Value                                                               | Maximum Value                                                               | Resolution/formula                                                          |
| 2 bits                  |                                                                             |                                                                             |                                                                             |
| Special/Reserved Values | 00                                                                          | Reserved                                                                    | Reserved                                                                    |
| Special/Reserved Values | 01                                                                          | Allow regenerative brake (on)                                               | Allow regenerative brake (on)                                               |
| Special/Reserved Values | 10                                                                          | Suppress regenerative brake (off)                                           | Suppress regenerative brake (off)                                           |
| Special/Reserved Values | 11                                                                          | No command from STM->Keep current output status                             | No command from STM->Keep current output status                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.45 M\_TIRB\_CMD\_AVAIL

| Name                    | Regenerative brake train interface command availability                                   | Regenerative brake train interface command availability                                   | Regenerative brake train interface command availability                                   |
|-------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the regenerative brake system command is available or not. | Boolean information telling if the regenerative brake system command is available or not. | Boolean information telling if the regenerative brake system command is available or not. |
| Length of variable      | Minimum Value                                                                             | Maximum Value                                                                             | Resolution/formula                                                                        |
| 1 bits                  |                                                                                           |                                                                                           |                                                                                           |
| Special/Reserved Values | 0                                                                                         | Regenerative brake system command is not available                                        | Regenerative brake system command is not available                                        |
| Special/Reserved Values | 1                                                                                         | Regenerative brake system command is available                                            | Regenerative brake system command is available                                            |

## 8.1.46 M\_TITR\_C\_CMD

| Name                    | Traction cut off train interface command    | Traction cut off train interface command        | Traction cut off train interface command        |
|-------------------------|---------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| Description             | Information for cutting the traction power. | Information for cutting the traction power.     | Information for cutting the traction power.     |
| Length of variable      | Minimum Value                               | Maximum Value                                   | Resolution/formula                              |
| 2 bits                  |                                             |                                                 |                                                 |
| Special/Reserved Values | 00                                          | Reserved                                        |                                                 |
| Special/Reserved Values | 01                                          | Traction cut off                                |                                                 |
| Special/Reserved Values | 10                                          | No traction cut off                             |                                                 |
| Special/Reserved Values | 11                                          | No command from STM->Keep current output status | No command from STM->Keep current output status |

## 8.1.47 M\_TITR\_C\_CMD\_AVAIL

| Name                    | Traction cut-off train interface command availability                                   | Traction cut-off train interface command availability                                   | Traction cut-off train interface command availability                                   |
|-------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Description             | Boolean information telling if the Traction cut-off system command is available or not. | Boolean information telling if the Traction cut-off system command is available or not. | Boolean information telling if the Traction cut-off system command is available or not. |
| Length of variable      | Minimum Value                                                                           | Maximum Value                                                                           | Resolution/formula                                                                      |
| 1 bits                  |                                                                                         |                                                                                         |                                                                                         |
| Special/Reserved Values | 0                                                                                       | Traction cut-off system command is not available                                        | Traction cut-off system command is not available                                        |
| Special/Reserved Values | 1                                                                                       | Traction cut-off system command is available                                            | Traction cut-off system command is available                                            |

## 8.1.48 M\_TITR\_STATUS

| Name                    | Traction status on Train Interface                       | Traction status on Train Interface                          | Traction status on Train Interface                          |
|-------------------------|----------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| Description             | Information defining if the traction power is on or off. | Information defining if the traction power is on or off.    | Information defining if the traction power is on or off.    |
| Length of variable      | Minimum Value                                            | Maximum Value                                               | Resolution/formula                                          |
| 2 bits                  |                                                          |                                                             |                                                             |
| Special/Reserved Values | 00                                                       | Fail status (information not received from Train Interface) | Fail status (information not received from Train Interface) |
| Special/Reserved Values | 01                                                       | Traction off                                                | Traction off                                                |
| Special/Reserved Values | 10                                                       | Traction on                                                 | Traction on                                                 |
| Special/Reserved Values | 11                                                       | Spare                                                       | Spare                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.49 M\_TRAINTYPE

Name

Train type

Description

It defines type of train as defined in [10].

Length of variable

Minimum Value

Maximum Value

Resolution/formula

8 bits

0

254

Special/Reserved Values

255

Undefined

## 8.1.50 M\_XATTRIBUTE

| Name                    | Text message attribute                                                      | Text message attribute                                                                                                | Text message attribute                                                                                                |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Description             | Specifies group, flashing mode, text & background colour for text messages. | Specifies group, flashing mode, text & background colour for text messages.                                           | Specifies group, flashing mode, text & background colour for text messages.                                           |
| Length of variable      | Minimum Value                                                               | Maximum Value                                                                                                         | Resolution/formula                                                                                                    |
| 10 bits                 |                                                                             |                                                                                                                       |                                                                                                                       |
| Special/Reserved Values | 0xxxxxxxxx                                                                  | Text message shall be displayed in group 1                                                                            | Text message shall be displayed in group 1                                                                            |
|                         | 1xxxxxxxxx                                                                  | Text message shall be displayed in group 2                                                                            | Text message shall be displayed in group 2                                                                            |
|                         | x0xxxxxxxx                                                                  | Normal flashing (only relevant in case "slow flashing" or "Fast flashing" is transmitted in the same variable).       | Normal flashing (only relevant in case "slow flashing" or "Fast flashing" is transmitted in the same variable).       |
|                         | x1xxxxxxxx                                                                  | Counterphase flashing (only relevant in case "slow flashing" or "Fast flashing" is transmitted in the same variable). | Counterphase flashing (only relevant in case "slow flashing" or "Fast flashing" is transmitted in the same variable). |
|                         | xx00xxxxxx                                                                  | No flashing                                                                                                           | No flashing                                                                                                           |
|                         | xx01xxxxxx                                                                  | Slow flashing                                                                                                         | Slow flashing                                                                                                         |
|                         | xx10xxxxxx                                                                  | Fast flashing                                                                                                         | Fast flashing                                                                                                         |
|                         | xx11xxxxxx                                                                  | Reserved                                                                                                              | Reserved                                                                                                              |
|                         | xxxx000xxx                                                                  | Dark blue text background                                                                                             | Dark blue text background                                                                                             |
|                         | xxxx001xxx                                                                  | White text background                                                                                                 | White text background                                                                                                 |
|                         | xxxx010xxx                                                                  | Red text background                                                                                                   | Red text background                                                                                                   |
|                         | xxxx011xxx                                                                  | Blue text background                                                                                                  | Blue text background                                                                                                  |
|                         | xxxx100xxx                                                                  | Green text background                                                                                                 | Green text background                                                                                                 |
|                         | xxxx101xxx                                                                  | Yellow text background                                                                                                | Yellow text background                                                                                                |
|                         | xxxx110xxx                                                                  | Light red text background                                                                                             | Light red text background                                                                                             |
|                         | xxxx111xxx                                                                  | Light green text background                                                                                           | Light green text background                                                                                           |
|                         | xxxxxxx000                                                                  | Black text                                                                                                            | Black text                                                                                                            |
|                         | xxxxxxx001                                                                  | White text                                                                                                            | White text                                                                                                            |
|                         | xxxxxxx010                                                                  | Red text                                                                                                              | Red text                                                                                                              |
|                         | xxxxxxx011                                                                  | Blue text                                                                                                             | Blue text                                                                                                             |
|                         | xxxxxxx100                                                                  | Green text                                                                                                            | Green text                                                                                                            |
|                         | xxxxxxx101                                                                  | Yellow text                                                                                                           | Yellow text                                                                                                           |
|                         | xxxxxxx110                                                                  | Light red text                                                                                                        | Light red text                                                                                                        |
|                         | xxxxxxx111                                                                  | Light green text                                                                                                      | Light green text                                                                                                      |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.51 N\_VERMAJOR

Name

FFFIS STM version major number X

Description

Length of variable

Minimum Value

Maximum Value

Resolution/formula

8 bits

0

255

Integer

Special/Reserved Values

## 8.1.52 N\_VERMINOR

| Name                    | FFFIS STM version minor number Y   | FFFIS STM version minor number Y   | FFFIS STM version minor number Y   |
|-------------------------|------------------------------------|------------------------------------|------------------------------------|
| Description             |                                    |                                    |                                    |
| Length of variable      | Minimum Value                      | Maximum Value                      | Resolution/formula                 |
| 8 bits                  | 0                                  | 255                                | Integer                            |
| Special/Reserved Values |                                    |                                    |                                    |

## 8.1.53 N\_ADDR\_BI

| Name                    | Address of BIU Function                                 | Address of BIU Function                                 | Address of BIU Function                                 |
|-------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Description             | Declares at what address the BIU Function is allocated. | Declares at what address the BIU Function is allocated. | Declares at what address the BIU Function is allocated. |
| Length of variable      | Minimum Value                                           | Maximum Value                                           | Resolution/formula                                      |
| 7 bits                  | 0                                                       | 19                                                      |                                                         |
| Special/Reserved Values | 2                                                       | STM Control Function                                    |                                                         |
| Special/Reserved Values | 20-126                                                  | Reserved                                                |                                                         |
| Special/Reserved Values | 127                                                     | Reserved for multicast                                  |                                                         |

## 8.1.54 N\_ADDR\_DMI\_CHANNEL1

| Name                    | Address of DMI channel 1                                 | Address of DMI channel 1                                 | Address of DMI channel 1                                 |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Declares at what address the DMI channel 1 is allocated. | Declares at what address the DMI channel 1 is allocated. | Declares at what address the DMI channel 1 is allocated. |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 7 bits                  | 0                                                        | 19                                                       |                                                          |
| Special/Reserved Values | 2                                                        | STM Control Function                                     |                                                          |
| Special/Reserved Values | 20-126                                                   | Reserved                                                 |                                                          |
| Special/Reserved Values | 127                                                      | Reserved for multicast                                   |                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.55 N\_ADDR\_DMI\_CHANNEL2

| Name                    | Address of DMI channel 2                                 | Address of DMI channel 2                                 | Address of DMI channel 2                                 |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Declares at what address the DMI channel 2 is allocated. | Declares at what address the DMI channel 2 is allocated. | Declares at what address the DMI channel 2 is allocated. |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 7 bits                  | 0                                                        | 19                                                       |                                                          |
| Special/Reserved Values | 2                                                        | STM Control Function                                     |                                                          |
| Special/Reserved Values | 20-126                                                   | Reserved                                                 |                                                          |
| Special/Reserved Values | 127                                                      | Reserved for multicast                                   |                                                          |

## 8.1.56 N\_ADDR\_DMI\_CHANNEL3

| Name                    | Address of DMI channel 3                                 | Address of DMI channel 3                                 | Address of DMI channel 3                                 |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Declares at what address the DMI channel 3 is allocated. | Declares at what address the DMI channel 3 is allocated. | Declares at what address the DMI channel 3 is allocated. |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 7 bits                  | 0                                                        | 19                                                       |                                                          |
| Special/Reserved Values | 2                                                        | STM Control Function                                     |                                                          |
| Special/Reserved Values | 20-126                                                   | Reserved                                                 |                                                          |
| Special/Reserved Values | 127                                                      | Reserved for multicast                                   |                                                          |

## 8.1.57 N\_ADDR\_DMI\_CHANNEL4

| Name                    | Address of DMI channel 4                                 | Address of DMI channel 4                                 | Address of DMI channel 4                                 |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Declares at what address the DMI channel 4 is allocated. | Declares at what address the DMI channel 4 is allocated. | Declares at what address the DMI channel 4 is allocated. |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 7 bits                  | 0                                                        | 19                                                       |                                                          |
| Special/Reserved Values | 2                                                        | STM Control Function                                     |                                                          |
| Special/Reserved Values | 20-126                                                   | Reserved                                                 |                                                          |
| Special/Reserved Values | 127                                                      | Reserved for multicast                                   |                                                          |

## 8.1.58 N\_ADDR\_JD

| Name                    | Address of JD Function                                 | Address of JD Function                                 | Address of JD Function                                 |
|-------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| Description             | Declares at what address the JD Function is allocated. | Declares at what address the JD Function is allocated. | Declares at what address the JD Function is allocated. |
| Length of variable      | Minimum Value                                          | Maximum Value                                          | Resolution/formula                                     |
| 7 bits                  | 0                                                      | 19                                                     |                                                        |
| Special/Reserved Values | 2                                                      | STM Control Function                                   |                                                        |
| Special/Reserved Values | 20-126                                                 | Reserved                                               |                                                        |
| Special/Reserved Values | 127                                                    | Reserved for multicast                                 |                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.59 N\_ADDR\_ODO

| Name                    | Address of the Odometer Function                             | Address of the Odometer Function                             | Address of the Odometer Function                             |
|-------------------------|--------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Description             | Declares at what address the Odometer Function is allocated. | Declares at what address the Odometer Function is allocated. | Declares at what address the Odometer Function is allocated. |
| Length of variable      | Minimum Value                                                | Maximum Value                                                | Resolution/formula                                           |
| 7 bits                  | 0                                                            | 19                                                           |                                                              |
| Special/Reserved Values | 2                                                            | STM Control Function                                         |                                                              |
| Special/Reserved Values | 20-126                                                       | Reserved                                                     |                                                              |
| Special/Reserved Values | 127                                                          | Reserved for multicast                                       |                                                              |

## 8.1.60 N\_ADDR\_TI

| Name                    | Address of TIU Function                                 | Address of TIU Function                                 | Address of TIU Function                                 |
|-------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| Description             | Declares at what address the TIU Function is allocated. | Declares at what address the TIU Function is allocated. | Declares at what address the TIU Function is allocated. |
| Length of variable      | Minimum Value                                           | Maximum Value                                           | Resolution/formula                                      |
| 7 bits                  | 0                                                       | 19                                                      |                                                         |
| Special/Reserved Values | 2                                                       | STM Control Function                                    |                                                         |
| Special/Reserved Values | 20-126                                                  | Reserved                                                |                                                         |
| Special/Reserved Values | 127                                                     | Reserved for multicast                                  |                                                         |

## 8.1.61 N\_LITER

| Name                    | Number of iterations of a data set following this variable in a packet         | Number of iterations of a data set following this variable in a packet         | Number of iterations of a data set following this variable in a packet         |
|-------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Description             | If 0 then no data set is following. Two nested levels of iterations can exist. | If 0 then no data set is following. Two nested levels of iterations can exist. | If 0 then no data set is following. Two nested levels of iterations can exist. |
| Length of variable      | Minimum Value                                                                  | Maximum Value                                                                  | Resolution/formula                                                             |
| 8 bits                  | 0                                                                              | As allowed by maximum length of application data but always under 255.         | Integers                                                                       |
| Special/Reserved Values |                                                                                |                                                                                |                                                                                |

## 8.1.62 NID\_ANTENNA\_BTM

| Name                    | Valid Antenna/BTM ID                                                     | Valid Antenna/BTM ID                                                     | Valid Antenna/BTM ID                                                     |
|-------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Description             | Identifier of the Antenna/BTM that is currently active on Interface 'K'. | Identifier of the Antenna/BTM that is currently active on Interface 'K'. | Identifier of the Antenna/BTM that is currently active on Interface 'K'. |
| Length of variable      | Minimum Value                                                            | Maximum Value                                                            | Resolution/formula                                                       |
| 2 bits                  |                                                                          |                                                                          |                                                                          |
| Special/Reserved Values | 00                                                                       | Antenna 1                                                                |                                                                          |
| Special/Reserved Values | 01                                                                       | Antenna 2                                                                |                                                                          |
| Special/Reserved Values | 10                                                                       | Antenna 3                                                                |                                                                          |
| Special/Reserved Values | 11                                                                       | Antenna 4                                                                |                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.63 NID\_BUTPOS

Name

Button Position Identifier

Description

Specifies the position to display the button on DMI.

For the unified DMI service special values are reserved for the available areas of the ETCS DMI layout specified in [10].

For the customisable DMI service the available button position identifiers are specified in the DMI layout configuration of the STM.

Length of variable

Minimum Value

Maximum Value

Resolution/formula

5 bits

1

24

Special/Reserved Values

Button areas used for unified DMI service

Soft key technology

Touch screen technology

1

F8

F8

2

F9

F9

3

F10

C2

4

H2

C3

5

H3

C4

6

H4

C5

7

Reserved

C6

8

Reserved

G1

9

Reserved

G2

10

Reserved

G3

11

Reserved

G4

12

Reserved

G5

13

Reserved

G6

14

Reserved

G7

15

Reserved

G8

16

Reserved

G9

17

Reserved

G10

18-24

Reserved, when unified DMI service is used

25-31

Reserved independent of used DMI service

## 8.1.64 NID\_BUTTON

Name

Button Identifier

Description

The button identifier is used to change the state of buttons and to move or remove them. The button identifier is also used to transmit the buttons events to the STM. If the customisable DMI service is used, it is also used to retrieve the configurable properties of the button.

Length of variable

Minimum Value

Maximum Value

Resolution/formula

8 bits

0

255

Special/Reserved Values

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.65 NID\_DATA

| Name                    | Identifier of a Specific NTC Data                                              | Identifier of a Specific NTC Data                                              | Identifier of a Specific NTC Data                                              |
|-------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Description             | One value of this variable represents a Specific NTC Data required by the STM. | One value of this variable represents a Specific NTC Data required by the STM. | One value of this variable represents a Specific NTC Data required by the STM. |
| Length of variable      | Minimum Value                                                                  | Maximum Value                                                                  | Resolution/formula                                                             |
| 8 bits                  | 0                                                                              | 255                                                                            |                                                                                |
| Special/Reserved Values |                                                                                |                                                                                |                                                                                |

## 8.1.66 NID\_DMICHANNEL

| Name                    | DMI channel Identifier                         | DMI channel Identifier                         | DMI channel Identifier                         |
|-------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| Description             | Give the identifier of the active DMI channel. | Give the identifier of the active DMI channel. | Give the identifier of the active DMI channel. |
| Length of variable      | Minimum Value                                  | Maximum Value                                  | Resolution/formula                             |
| 3 bits                  |                                                |                                                |                                                |
| Special/Reserved Values | 0                                              | No DMI channel                                 |                                                |
|                         | 1                                              | DMI channel 1                                  |                                                |
|                         | 2                                              | DMI channel 2                                  |                                                |
|                         | 3                                              | DMI channel 3                                  |                                                |
|                         | 4                                              | DMI channel 4                                  |                                                |
|                         | 5-7                                            | Reserved                                       |                                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.67 NID\_DRV\_LANG

| Name                    | Driver language Identifier                                                                                                        | Driver language Identifier                                                                                                        | Driver language Identifier                                                                                                        |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Description             | Driver Language Selection Defined according to [8] This table includes a subset of the language identifiers included in the norm. | Driver Language Selection Defined according to [8] This table includes a subset of the language identifiers included in the norm. | Driver Language Selection Defined according to [8] This table includes a subset of the language identifiers included in the norm. |
| Length of variable      | Minimum Value                                                                                                                     | Maximum Value                                                                                                                     | Resolution/formula                                                                                                                |
| 16 bits (2 characters)  |                                                                                                                                   |                                                                                                                                   |                                                                                                                                   |
| Special/Reserved Values | en                                                                                                                                | ENGLISH                                                                                                                           | ENGLISH                                                                                                                           |
|                         | de                                                                                                                                | GERMAN                                                                                                                            | GERMAN                                                                                                                            |
|                         | fr                                                                                                                                | FRENCH                                                                                                                            | FRENCH                                                                                                                            |
|                         | es                                                                                                                                | SPANISH                                                                                                                           | SPANISH                                                                                                                           |
|                         | it                                                                                                                                | ITALIAN                                                                                                                           | ITALIAN                                                                                                                           |
|                         | nl                                                                                                                                | DUTCH                                                                                                                             | DUTCH                                                                                                                             |
|                         | hu                                                                                                                                | HUNGARIAN                                                                                                                         | HUNGARIAN                                                                                                                         |
|                         | da                                                                                                                                | DANISH                                                                                                                            | DANISH                                                                                                                            |
|                         | fi                                                                                                                                | FINNISH                                                                                                                           | FINNISH                                                                                                                           |
|                         | no                                                                                                                                | NORWEGIAN                                                                                                                         | NORWEGIAN                                                                                                                         |
|                         | sv                                                                                                                                | SWEDISH                                                                                                                           | SWEDISH                                                                                                                           |
|                         | bg                                                                                                                                | BULGARIAN                                                                                                                         | BULGARIAN                                                                                                                         |
|                         | hr                                                                                                                                | CROATIAN                                                                                                                          | CROATIAN                                                                                                                          |
|                         | cs                                                                                                                                | CZECH                                                                                                                             | CZECH                                                                                                                             |
|                         | et                                                                                                                                | ESTONIAN                                                                                                                          | ESTONIAN                                                                                                                          |
|                         | el                                                                                                                                | GREEK                                                                                                                             | GREEK                                                                                                                             |
|                         | pl                                                                                                                                | POLISH                                                                                                                            | POLISH                                                                                                                            |
|                         | pt                                                                                                                                | PORTUGUESE                                                                                                                        | PORTUGUESE                                                                                                                        |
|                         | ro                                                                                                                                | ROMANIAN                                                                                                                          | ROMANIAN                                                                                                                          |
|                         | ru                                                                                                                                | RUSSIAN                                                                                                                           | RUSSIAN                                                                                                                           |
|                         | sr                                                                                                                                | SERBIAN                                                                                                                           | SERBIAN                                                                                                                           |
|                         | sh                                                                                                                                | SERBO-CROATIAN                                                                                                                    | SERBO-CROATIAN                                                                                                                    |
|                         | sk                                                                                                                                | SLOVAK                                                                                                                            | SLOVAK                                                                                                                            |
|                         | sl                                                                                                                                | SLOVENIAN                                                                                                                         | SLOVENIAN                                                                                                                         |
|                         | tr                                                                                                                                | TURKISH                                                                                                                           | TURKISH                                                                                                                           |
|                         | lv                                                                                                                                | LATVIAN                                                                                                                           | LATVIAN                                                                                                                           |
|                         | lt                                                                                                                                | LITHUANIAN                                                                                                                        | LITHUANIAN                                                                                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.68 NID\_ICON

| Name                    | Icon Identifier                                                                  | Icon Identifier                                                                  | Icon Identifier                                                                  |
|-------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Description             | Specifies bitmap to use for display of icon in case of customisable DMI service. | Specifies bitmap to use for display of icon in case of customisable DMI service. | Specifies bitmap to use for display of icon in case of customisable DMI service. |
| Length of variable      | Minimum Value                                                                    | Maximum Value                                                                    | Resolution/Formula                                                               |
| 8 bits                  | 1                                                                                | 255                                                                              |                                                                                  |
| Special/Reserved Values | 0                                                                                | No icon referenced                                                               |                                                                                  |

## 8.1.69 NID\_INDICATOR

| Name                    | Indicator Identifier                                                                                                                                                                                                  | Indicator Identifier                                                                                                                                                                                                  | Indicator Identifier                                                                                                                                                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | The indicator identifier is used to change the state of the indicators and to move or remove them. If the customisable DMI service is used, it is also used to retrieve the configurable properties of the indicator. | The indicator identifier is used to change the state of the indicators and to move or remove them. If the customisable DMI service is used, it is also used to retrieve the configurable properties of the indicator. | The indicator identifier is used to change the state of the indicators and to move or remove them. If the customisable DMI service is used, it is also used to retrieve the configurable properties of the indicator. |
| Length of variable      | Minimum Value                                                                                                                                                                                                         | Maximum Value                                                                                                                                                                                                         | Resolution/formula                                                                                                                                                                                                    |
| 8 bits                  | 0                                                                                                                                                                                                                     | 255                                                                                                                                                                                                                   |                                                                                                                                                                                                                       |
| Special/Reserved Values |                                                                                                                                                                                                                       |                                                                                                                                                                                                                       |                                                                                                                                                                                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.70 NID\_INDPOS

| Name                         | Indicator Position Identifier                                                                                                                                                                                                                                                                                                           | Indicator Position Identifier                                                                                                                                                                                                                                                                                                           | Indicator Position Identifier                                                                                                                                                                                                                                                                                                           |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description                  | Specifies the appropriate position to display the indicator on DMI. For the unified DMI service, special values are reserved for the available areas of the ETCS DMI layout specified in [10]. For the customisable DMI service, the available indicator position identifiers are specified in the DMI layout configuration of the STM. | Specifies the appropriate position to display the indicator on DMI. For the unified DMI service, special values are reserved for the available areas of the ETCS DMI layout specified in [10]. For the customisable DMI service, the available indicator position identifiers are specified in the DMI layout configuration of the STM. | Specifies the appropriate position to display the indicator on DMI. For the unified DMI service, special values are reserved for the available areas of the ETCS DMI layout specified in [10]. For the customisable DMI service, the available indicator position identifiers are specified in the DMI layout configuration of the STM. |
| Length of variable           | Minimum Value                                                                                                                                                                                                                                                                                                                           | Maximum Value                                                                                                                                                                                                                                                                                                                           | Resolution/formula                                                                                                                                                                                                                                                                                                                      |
| 5                            | 1                                                                                                                                                                                                                                                                                                                                       | 24                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                         |
| bits Special/Reserved Values | Indicator areas used for unified DMI service                                                                                                                                                                                                                                                                                            | Indicator areas used for unified DMI service                                                                                                                                                                                                                                                                                            | Indicator areas used for unified DMI service                                                                                                                                                                                                                                                                                            |
|                              | 1                                                                                                                                                                                                                                                                                                                                       | B3                                                                                                                                                                                                                                                                                                                                      | B3                                                                                                                                                                                                                                                                                                                                      |
|                              | 2                                                                                                                                                                                                                                                                                                                                       | B4                                                                                                                                                                                                                                                                                                                                      | B4                                                                                                                                                                                                                                                                                                                                      |
|                              | 3                                                                                                                                                                                                                                                                                                                                       | B5                                                                                                                                                                                                                                                                                                                                      | B5                                                                                                                                                                                                                                                                                                                                      |
|                              | 4                                                                                                                                                                                                                                                                                                                                       | H1 (Reserved in touch screen technology)                                                                                                                                                                                                                                                                                                | H1 (Reserved in touch screen technology)                                                                                                                                                                                                                                                                                                |
|                              | 5                                                                                                                                                                                                                                                                                                                                       | C2                                                                                                                                                                                                                                                                                                                                      | C2                                                                                                                                                                                                                                                                                                                                      |
|                              | 6                                                                                                                                                                                                                                                                                                                                       | C3                                                                                                                                                                                                                                                                                                                                      | C3                                                                                                                                                                                                                                                                                                                                      |
|                              | 7                                                                                                                                                                                                                                                                                                                                       | C4                                                                                                                                                                                                                                                                                                                                      | C4                                                                                                                                                                                                                                                                                                                                      |
|                              | 8                                                                                                                                                                                                                                                                                                                                       | C5                                                                                                                                                                                                                                                                                                                                      | C5                                                                                                                                                                                                                                                                                                                                      |
|                              | 9                                                                                                                                                                                                                                                                                                                                       | C6                                                                                                                                                                                                                                                                                                                                      | C6                                                                                                                                                                                                                                                                                                                                      |
|                              | 10                                                                                                                                                                                                                                                                                                                                      | G1                                                                                                                                                                                                                                                                                                                                      | G1                                                                                                                                                                                                                                                                                                                                      |
|                              | 11                                                                                                                                                                                                                                                                                                                                      | G2                                                                                                                                                                                                                                                                                                                                      | G2                                                                                                                                                                                                                                                                                                                                      |
|                              | 12                                                                                                                                                                                                                                                                                                                                      | G3                                                                                                                                                                                                                                                                                                                                      | G3                                                                                                                                                                                                                                                                                                                                      |
|                              | 13                                                                                                                                                                                                                                                                                                                                      | G4                                                                                                                                                                                                                                                                                                                                      | G4                                                                                                                                                                                                                                                                                                                                      |
|                              | 14                                                                                                                                                                                                                                                                                                                                      | G5                                                                                                                                                                                                                                                                                                                                      | G5                                                                                                                                                                                                                                                                                                                                      |
|                              | 15                                                                                                                                                                                                                                                                                                                                      | G6                                                                                                                                                                                                                                                                                                                                      | G6                                                                                                                                                                                                                                                                                                                                      |
|                              | 16                                                                                                                                                                                                                                                                                                                                      | G7                                                                                                                                                                                                                                                                                                                                      | G7                                                                                                                                                                                                                                                                                                                                      |
|                              | 17                                                                                                                                                                                                                                                                                                                                      | G8                                                                                                                                                                                                                                                                                                                                      | G8                                                                                                                                                                                                                                                                                                                                      |
|                              | 18                                                                                                                                                                                                                                                                                                                                      | G9                                                                                                                                                                                                                                                                                                                                      | G9                                                                                                                                                                                                                                                                                                                                      |
|                              | 19                                                                                                                                                                                                                                                                                                                                      | G10                                                                                                                                                                                                                                                                                                                                     | G10                                                                                                                                                                                                                                                                                                                                     |
|                              | 20-24                                                                                                                                                                                                                                                                                                                                   | Reserved, when unified DMI service is used                                                                                                                                                                                                                                                                                              | Reserved, when unified DMI service is used                                                                                                                                                                                                                                                                                              |
|                              | 25-31                                                                                                                                                                                                                                                                                                                                   | Reserved independent of used DMI service                                                                                                                                                                                                                                                                                                | Reserved independent of used DMI service                                                                                                                                                                                                                                                                                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.70.1 NID\_OPERATIONAL\_STM

| Name                    | Train Running Number                                                                                                                                                                                                                                                                                                                 | Train Running Number                                                                                                                                                                                                                                                                                                                 | Train Running Number                                                                                                                                                                                                                                                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | This is the operational train running number. The NID_OPERATIONAL_STM consists of up to 8 digits which are entered left adjusted into the data field, the leftmost digit is the digit to be entered first. In case the NID_OPERATIONAL_STM is shorter than 8 digits, the remaining space is to be filled with special character 'F'. | This is the operational train running number. The NID_OPERATIONAL_STM consists of up to 8 digits which are entered left adjusted into the data field, the leftmost digit is the digit to be entered first. In case the NID_OPERATIONAL_STM is shorter than 8 digits, the remaining space is to be filled with special character 'F'. | This is the operational train running number. The NID_OPERATIONAL_STM consists of up to 8 digits which are entered left adjusted into the data field, the leftmost digit is the digit to be entered first. In case the NID_OPERATIONAL_STM is shorter than 8 digits, the remaining space is to be filled with special character 'F'. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                                                                                        | Maximum Value                                                                                                                                                                                                                                                                                                                        | Resolution/formula                                                                                                                                                                                                                                                                                                                   |
| 32 bits                 | 0                                                                                                                                                                                                                                                                                                                                    | 9999 9999                                                                                                                                                                                                                                                                                                                            | Binary Coded Decimal                                                                                                                                                                                                                                                                                                                 |
| Special/Reserved Values | For each digit :                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                      |
| Special/Reserved Values | Values A - E                                                                                                                                                                                                                                                                                                                         | Spare                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                      |
| Special/Reserved Values | F                                                                                                                                                                                                                                                                                                                                    | Use value F for digit to indicate no digit (if number shorter than 8 digits)                                                                                                                                                                                                                                                         | Use value F for digit to indicate no digit (if number shorter than 8 digits)                                                                                                                                                                                                                                                         |
| Special/Reserved Values | FFFF FFFF                                                                                                                                                                                                                                                                                                                            | Unknown                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                      |

## 8.1.71 NID\_PACKET

| Name                    | Packet Identifier                                                                                  | Packet Identifier                                                                                  | Packet Identifier                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Description             | This is used in each packet, allowing the receiving equipment to identify the data, which follows. | This is used in each packet, allowing the receiving equipment to identify the data, which follows. | This is used in each packet, allowing the receiving equipment to identify the data, which follows. |
| Length of variable      | Minimum Value                                                                                      | Maximum Value                                                                                      | Resolution/formula                                                                                 |
| 8 bits                  | 0                                                                                                  | 199                                                                                                | Numbers                                                                                            |
| Special/Reserved Values | 200-255                                                                                            | Non standard packet, supplier specific                                                             | Non standard packet, supplier specific                                                             |

## 8.1.72 NID\_SOUND

| Name                    | Sound Identifier                                                                                                                            | Sound Identifier                                                                                                                            | Sound Identifier                                                                                                                            |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Specifies wave file to use for playing sound in case of customisable DMI service. In case of unified DMI service only used to stop a sound. | Specifies wave file to use for playing sound in case of customisable DMI service. In case of unified DMI service only used to stop a sound. | Specifies wave file to use for playing sound in case of customisable DMI service. In case of unified DMI service only used to stop a sound. |
| Length of variable      | Minimum Value                                                                                                                               | Maximum Value                                                                                                                               | Resolution/formula                                                                                                                          |
| 8 bits                  | 1                                                                                                                                           | 255                                                                                                                                         |                                                                                                                                             |
| Special/Reserved Values | 0                                                                                                                                           | No Sound identifier                                                                                                                         | No Sound identifier                                                                                                                         |

## 8.1.73 NID\_STM

| Name                    | STM identity                                                                                                                                                                                  | STM identity                                                                                                                                                                                  | STM identity                                                                                                                                                                                  |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Each value of this variable represents the identifier of a Specific Transmission Module. Values are equal to NID_NTC values, allocated according to the rule defined in [4], chapter 4.1.1.1. | Each value of this variable represents the identifier of a Specific Transmission Module. Values are equal to NID_NTC values, allocated according to the rule defined in [4], chapter 4.1.1.1. | Each value of this variable represents the identifier of a Specific Transmission Module. Values are equal to NID_NTC values, allocated according to the rule defined in [4], chapter 4.1.1.1. |
| Length of variable      | Minimum Value                                                                                                                                                                                 | Maximum Value                                                                                                                                                                                 | Resolution/formula                                                                                                                                                                            |
| 8 bits                  | 0                                                                                                                                                                                             | 254                                                                                                                                                                                           |                                                                                                                                                                                               |
| Special/Reserved Values | 255                                                                                                                                                                                           | Reserved for multicast                                                                                                                                                                        |                                                                                                                                                                                               |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.74 NID\_STMSTATE

| Name                    | Current STM state                  | Current STM state                       | Current STM state                       |
|-------------------------|------------------------------------|-----------------------------------------|-----------------------------------------|
| Description             | Tell the current state of the STM. | Tell the current state of the STM.      | Tell the current state of the STM.      |
| Length of variable      | Minimum Value                      | Maximum Value                           | Resolution/formula                      |
| 4 bits                  |                                    |                                         |                                         |
| Special/Reserved Values | 0                                  | Reserved (mapped to NP for consistency) | Reserved (mapped to NP for consistency) |
| Special/Reserved Values | 1                                  | Power On (PO)                           | Power On (PO)                           |
| Special/Reserved Values | 2                                  | Configuration (CO)                      | Configuration (CO)                      |
| Special/Reserved Values | 3                                  | Data Entry (DE)                         | Data Entry (DE)                         |
| Special/Reserved Values | 4                                  | Cold Standby (CS)                       | Cold Standby (CS)                       |
| Special/Reserved Values | 5                                  | Reserved (mapped to CS for consistency) | Reserved (mapped to CS for consistency) |
| Special/Reserved Values | 6                                  | Hot Standby (HS)                        | Hot Standby (HS)                        |
| Special/Reserved Values | 7                                  | Data Available (DA)                     | Data Available (DA)                     |
| Special/Reserved Values | 8                                  | Failure (FA)                            | Failure (FA)                            |
| Special/Reserved Values | 9-15                               | Spare values                            | Spare values                            |

## 8.1.75 NID\_STMSTATEORDER

| Name                    | STM state order                                       | STM state order                                       | STM state order                                       |
|-------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| Description             | Tell the STM state ordered by the ERTMS/ETCS on-board | Tell the STM state ordered by the ERTMS/ETCS on-board | Tell the STM state ordered by the ERTMS/ETCS on-board |
| Length of variable      | Minimum Value                                         | Maximum Value                                         | Resolution/formula                                    |
| 4 bits                  |                                                       |                                                       |                                                       |
| Special/Reserved Values | 0                                                     | Reserved (mapped to NP for consistency)               | Reserved (mapped to NP for consistency)               |
| Special/Reserved Values | 1                                                     | Reserved (mapped to PO for consistency)               | Reserved (mapped to PO for consistency)               |
| Special/Reserved Values | 2                                                     | Configuration (CO)                                    | Configuration (CO)                                    |
| Special/Reserved Values | 3                                                     | Data Entry (DE)                                       | Data Entry (DE)                                       |
| Special/Reserved Values | 4                                                     | Unconditional Cold Standby (U-CS)                     | Unconditional Cold Standby (U-CS)                     |
| Special/Reserved Values | 5                                                     | Conditional Cold Standby (C-CS)                       | Conditional Cold Standby (C-CS)                       |
| Special/Reserved Values | 6                                                     | Hot Standby (HS)                                      | Hot Standby (HS)                                      |
| Special/Reserved Values | 7                                                     | Data Available (DA)                                   | Data Available (DA)                                   |
| Special/Reserved Values | 8                                                     | Failure (FA)                                          | Failure (FA)                                          |
| Special/Reserved Values | 9-15                                                  | Spare values                                          | Spare values                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.76 NID\_STMSTATEREQUEST

| Name                    | STM state request                                                 | STM state request                                                 | STM state request                                                 |
|-------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Description             | State requested by the STM, in which the STM is intended to pass. | State requested by the STM, in which the STM is intended to pass. | State requested by the STM, in which the STM is intended to pass. |
| Length of variable      | Minimum Value                                                     | Maximum Value                                                     | Resolution/formula                                                |
| 4 bits                  |                                                                   |                                                                   |                                                                   |
| Special/Reserved Values | 0                                                                 | Reserved (mapped to NP for consistency)                           | Reserved (mapped to NP for consistency)                           |
| Special/Reserved Values | 1                                                                 | Reserved (mapped to PO for consistency)                           | Reserved (mapped to PO for consistency)                           |
| Special/Reserved Values | 2                                                                 | Configuration (CO)                                                | Configuration (CO)                                                |
| Special/Reserved Values | 3                                                                 | Data Entry (DE)                                                   | Data Entry (DE)                                                   |
| Special/Reserved Values | 4                                                                 | Cold Standby (CS)                                                 | Cold Standby (CS)                                                 |
| Special/Reserved Values | 5                                                                 | Reserved (mapped to CS for consistency)                           | Reserved (mapped to CS for consistency)                           |
| Special/Reserved Values | 6                                                                 | Reserved (mapped to HS for consistency)                           | Reserved (mapped to HS for consistency)                           |
| Special/Reserved Values | 7                                                                 | Reserved (mapped to DA for consistency)                           | Reserved (mapped to DA for consistency)                           |
| Special/Reserved Values | 8                                                                 | Reserved (mapped to FA for consistency)                           | Reserved (mapped to FA for consistency)                           |
| Special/Reserved Values | 9-15                                                              | Spare values                                                      | Spare values                                                      |

## 8.1.77 NID\_TEST

| Name                    | STM Test Identity                                                                             | STM Test Identity                                                                             | STM Test Identity                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Description             | Enables to identify the type of test that the STM requests. Its meaning is supplier-specific. | Enables to identify the type of test that the STM requests. Its meaning is supplier-specific. | Enables to identify the type of test that the STM requests. Its meaning is supplier-specific. |
| Length of variable      | Minimum Value                                                                                 | Maximum Value                                                                                 | Resolution/formula                                                                            |
| 8 bits                  | 0                                                                                             | 255                                                                                           |                                                                                               |
| Special/Reserved Values |                                                                                               |                                                                                               |                                                                                               |

## 8.1.78 NID\_XMESSAGE

| Name                    | Text message Identifier                                                     | Text message Identifier                                                     | Text message Identifier                                                     |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Description             | Text message Identifier for deletion and acknowledgement of a text message. | Text message Identifier for deletion and acknowledgement of a text message. | Text message Identifier for deletion and acknowledgement of a text message. |
| Length of variable      | Minimum Value                                                               | Maximum Value                                                               | Resolution/formula                                                          |
| 8 bits                  | 0                                                                           | 255                                                                         | Integer                                                                     |
| Special/Reserved Values |                                                                             |                                                                             |                                                                             |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.79 Q\_ACK

| Name                    | Acknowledgement qualifier                                          | Acknowledgement qualifier                                          | Acknowledgement qualifier                                          |
|-------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| Description             | Tell if a text message (NID_XMESSAGE) must be acknowledged or not. | Tell if a text message (NID_XMESSAGE) must be acknowledged or not. | Tell if a text message (NID_XMESSAGE) must be acknowledged or not. |
| Length of variable      | Minimum Value                                                      | Maximum Value                                                      | Resolution/formula                                                 |
| 1 bit                   |                                                                    |                                                                    | Boolean                                                            |
| Special/Reserved Values | 0                                                                  | No acknowledgement required                                        | No acknowledgement required                                        |
| Special/Reserved Values | 1                                                                  | Acknowledgement required                                           | Acknowledgement required                                           |

## 8.1.80 Q\_ADDR\_BI

| Name                    | Safety level of Brake Interface connection                                                     | Safety level of Brake Interface connection                                                     | Safety level of Brake Interface connection                                                     |
|-------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_BI. | Declares the highest safety level for the connection to the function at the address N_ADDR_BI. | Declares the highest safety level for the connection to the function at the address N_ADDR_BI. |
| Length of variable      | Minimum Value                                                                                  | Maximum Value                                                                                  | Resolution/formula                                                                             |
| 2 bits                  |                                                                                                |                                                                                                |                                                                                                |
| Special/Reserved Values | 0                                                                                              | SL0                                                                                            |                                                                                                |
| Special/Reserved Values | 1                                                                                              | SL2                                                                                            |                                                                                                |
| Special/Reserved Values | 2                                                                                              | SL4                                                                                            |                                                                                                |
| Special/Reserved Values | 3                                                                                              | Reserved                                                                                       |                                                                                                |

## 8.1.81 Q\_ADDR\_DMI\_CHANNEL1

| Name                    | Safety level of DMI channel 1 connection                                                                 | Safety level of DMI channel 1 connection                                                                 | Safety level of DMI channel 1 connection                                                                 |
|-------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL1. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL1. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL1. |
| Length of variable      | Minimum Value                                                                                            | Maximum Value                                                                                            | Resolution/formula                                                                                       |
| 2 bits                  |                                                                                                          |                                                                                                          |                                                                                                          |
| Special/Reserved Values | 0                                                                                                        | SL0                                                                                                      |                                                                                                          |
| Special/Reserved Values | 1                                                                                                        | SL2                                                                                                      |                                                                                                          |
| Special/Reserved Values | 2                                                                                                        | SL4                                                                                                      |                                                                                                          |
| Special/Reserved Values | 3                                                                                                        | Reserved                                                                                                 |                                                                                                          |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.82 Q\_ADDR\_DMI\_CHANNEL2

| Name                    | Safety level/Availability of DMI channel 2 connection                                                                                        | Safety level/Availability of DMI channel 2 connection                                                                                        | Safety level/Availability of DMI channel 2 connection                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL2 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL2 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL2 or if the function is not available. |
| Length of variable      | Minimum Value                                                                                                                                | Maximum Value                                                                                                                                | Resolution/formula                                                                                                                           |
| 2 bits                  |                                                                                                                                              |                                                                                                                                              |                                                                                                                                              |
| Special/Reserved Values | 0                                                                                                                                            | SL0                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 1                                                                                                                                            | SL2                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 2                                                                                                                                            | SL4                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 3                                                                                                                                            | Function not available                                                                                                                       |                                                                                                                                              |

## 8.1.83 Q\_ADDR\_DMI\_CHANNEL3

| Name                    | Safety level/Availability of DMI channel 3 connection                                                                                        | Safety level/Availability of DMI channel 3 connection                                                                                        | Safety level/Availability of DMI channel 3 connection                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL3 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL3 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL3 or if the function is not available. |
| Length of variable      | Minimum Value                                                                                                                                | Maximum Value                                                                                                                                | Resolution/formula                                                                                                                           |
| 2 bits                  |                                                                                                                                              |                                                                                                                                              |                                                                                                                                              |
| Special/Reserved Values | 0                                                                                                                                            | SL0                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 1                                                                                                                                            | SL2                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 2                                                                                                                                            | SL4                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 3                                                                                                                                            | Function not available                                                                                                                       |                                                                                                                                              |

## 8.1.84 Q\_ADDR\_DMI\_CHANNEL4

| Name                    | Safety level/Availability of DMI channel 4 connection                                                                                        | Safety level/Availability of DMI channel 4 connection                                                                                        | Safety level/Availability of DMI channel 4 connection                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL4 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL4 or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_DMI_CHANNEL4 or if the function is not available. |
| Length of variable      | Minimum Value                                                                                                                                | Maximum Value                                                                                                                                | Resolution/formula                                                                                                                           |
| 2 bits                  |                                                                                                                                              |                                                                                                                                              |                                                                                                                                              |
| Special/Reserved Values | 0                                                                                                                                            | SL0                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 1                                                                                                                                            | SL2                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 2                                                                                                                                            | SL4                                                                                                                                          |                                                                                                                                              |
| Special/Reserved Values | 3                                                                                                                                            | Function not available                                                                                                                       |                                                                                                                                              |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.85 Q\_ADDR\_JD

| Name                    | Safety level/Availability of JD connection                                                                                         | Safety level/Availability of JD connection                                                                                         | Safety level/Availability of JD connection                                                                                         |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_JD or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_JD or if the function is not available. | Declares the highest safety level for the connection to the function at the address N_ADDR_JD or if the function is not available. |
| Length of variable      | Minimum Value                                                                                                                      | Maximum Value                                                                                                                      | Resolution/formula                                                                                                                 |
| 2 bits                  |                                                                                                                                    |                                                                                                                                    |                                                                                                                                    |
| Special/Reserved Values | 0                                                                                                                                  | SL0                                                                                                                                |                                                                                                                                    |
| Special/Reserved Values | 1                                                                                                                                  | SL2                                                                                                                                |                                                                                                                                    |
| Special/Reserved Values | 2                                                                                                                                  | SL4                                                                                                                                |                                                                                                                                    |
| Special/Reserved Values | 3                                                                                                                                  | Function not available                                                                                                             |                                                                                                                                    |

## 8.1.86 Q\_ADDR\_ODO

| Name                    | Safety level of Odometer connection                                                             | Safety level of Odometer connection                                                             | Safety level of Odometer connection                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Description             | Declares the highest safety level for the connection to the function at the address N_ADDR_ODO. | Declares the highest safety level for the connection to the function at the address N_ADDR_ODO. | Declares the highest safety level for the connection to the function at the address N_ADDR_ODO. |
| Length of variable      | Minimum Value                                                                                   | Maximum Value                                                                                   | Resolution/formula                                                                              |
| 2 bits                  |                                                                                                 |                                                                                                 |                                                                                                 |
| Special/Reserved Values | 0                                                                                               | Reserved                                                                                        |                                                                                                 |
| Special/Reserved Values | 1                                                                                               | Reserved                                                                                        |                                                                                                 |
| Special/Reserved Values | 2                                                                                               | SL4                                                                                             |                                                                                                 |
| Special/Reserved Values | 3                                                                                               | Reserved                                                                                        |                                                                                                 |

## 8.1.87 Q\_ADDR\_TI

| Name                     | Safety level of Train Interface connection                                                     | Safety level of Train Interface connection                                                     | Safety level of Train Interface connection                                                     |
|--------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Description              | Declares the highest safety level for the connection to the function at the address N_ADDR_TI. | Declares the highest safety level for the connection to the function at the address N_ADDR_TI. | Declares the highest safety level for the connection to the function at the address N_ADDR_TI. |
| Length of variable       | Minimum Value                                                                                  | Maximum Value                                                                                  | Resolution/formula                                                                             |
| 2 bits                   |                                                                                                |                                                                                                |                                                                                                |
| Special/ Reserved Values | 0                                                                                              | SL0                                                                                            |                                                                                                |
| Special/ Reserved Values | 1                                                                                              | SL2                                                                                            |                                                                                                |
| Special/ Reserved Values | 2                                                                                              | SL4                                                                                            |                                                                                                |
| Special/ Reserved Values | 3                                                                                              | Reserved                                                                                       |                                                                                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.88 Q\_ANTN\_BTM\_ACTIVE

| Name                    | Qualifier indicating if there is an active Antenna/BTM         | Qualifier indicating if there is an active Antenna/BTM         | Qualifier indicating if there is an active Antenna/BTM         |
|-------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Description             | This is dynamic information depending on e.g. cabin selection. | This is dynamic information depending on e.g. cabin selection. | This is dynamic information depending on e.g. cabin selection. |
| Length of variable      | Minimum Value                                                  | Maximum Value                                                  | Resolution/formula                                             |
| 1 bit                   |                                                                |                                                                |                                                                |
| Special/Reserved Values | 0                                                              | No Antenna/BTM active                                          |                                                                |
| Special/Reserved Values | 1                                                              | One Antenna/BTM active                                         |                                                                |

## 8.1.89 Q\_BMM\_ANNOUNCED

| Name                    | Big Metal Mass announced                                                  | Big Metal Mass announced                                                  | Big Metal Mass announced                                                  |
|-------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Description             | Indicates if the train antenna is within a Big Metal Mass track condition | Indicates if the train antenna is within a Big Metal Mass track condition | Indicates if the train antenna is within a Big Metal Mass track condition |
| Length of variable      | Minimum Value                                                             | Maximum Value                                                             | Resolution/formula                                                        |
| 1 bit                   |                                                                           |                                                                           |                                                                           |
| Special/Reserved Values | 0                                                                         | Not within a Big Metal Mass track condition                               | Not within a Big Metal Mass track condition                               |
| Special/Reserved Values | 1                                                                         | Within a Big Metal Mass track condition                                   | Within a Big Metal Mass track condition                                   |

## 8.1.90 Q\_BTM\_ALARM

| Name                    | BTM alarm               | BTM alarm               | BTM alarm               |
|-------------------------|-------------------------|-------------------------|-------------------------|
| Description             | Status of the BTM alarm | Status of the BTM alarm | Status of the BTM alarm |
| Length of variable      | Minimum Value           | Maximum Value           | Resolution/formula      |
| 1 bit                   |                         |                         |                         |
| Special/Reserved Values | 0                       | BTM alarm not active    |                         |
| Special/Reserved Values | 1                       | BTM alarm active        |                         |

## 8.1.91 Q\_BUTTON

| Name                     | Button Event                   | Button Event                   | Button Event                   |
|--------------------------|--------------------------------|--------------------------------|--------------------------------|
| Description              | Qualifier for the button event | Qualifier for the button event | Qualifier for the button event |
| Length of variable       | Minimum Value                  | Maximum Value                  | Resolution/formula             |
| 1 bit                    |                                |                                |                                |
| Special/ Reserved Values | 0                              | Push event                     |                                |
| Special/ Reserved Values | 1                              | Release event                  |                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.92 Q\_CHECKNEEDED

| Name                    | Qualifier for need of checking the Interface 'K' Antenna/BTM ID                                                                                                                                                                  | Qualifier for need of checking the Interface 'K' Antenna/BTM ID                                                                                                                                                                  | Qualifier for need of checking the Interface 'K' Antenna/BTM ID                                                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | This is static information depending on ERTMS/ETCS on-board implementation. "Check needed" value is used if ERTMS/ETCS on-board cannot guarantee by its own that the interface 'K' data is coming from the intended Antenna/BTM. | This is static information depending on ERTMS/ETCS on-board implementation. "Check needed" value is used if ERTMS/ETCS on-board cannot guarantee by its own that the interface 'K' data is coming from the intended Antenna/BTM. | This is static information depending on ERTMS/ETCS on-board implementation. "Check needed" value is used if ERTMS/ETCS on-board cannot guarantee by its own that the interface 'K' data is coming from the intended Antenna/BTM. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                    | Maximum Value                                                                                                                                                                                                                    | Resolution/formula                                                                                                                                                                                                               |
| 1 bit                   |                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                  |
| Special/Reserved Values | 0                                                                                                                                                                                                                                | No check needed                                                                                                                                                                                                                  | No check needed                                                                                                                                                                                                                  |
| Special/Reserved Values | 1                                                                                                                                                                                                                                | Check needed                                                                                                                                                                                                                     | Check needed                                                                                                                                                                                                                     |

## 8.1.93 Q\_DATAENTRY

| Name                     | Need for Specific NTC Data Entry                               | Need for Specific NTC Data Entry                               | Need for Specific NTC Data Entry                               |
|--------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Description              | Qualifier indicating if the STM needs Specific NTC Data or not | Qualifier indicating if the STM needs Specific NTC Data or not | Qualifier indicating if the STM needs Specific NTC Data or not |
| Length of variable       | Minimum Value                                                  | Maximum Value                                                  | Resolution/formula                                             |
| 1 bit                    |                                                                |                                                                |                                                                |
| Special/ Reserved Values | 0                                                              | No Specifc NTC Data needed                                     | No Specifc NTC Data needed                                     |
| Special/ Reserved Values | 1                                                              | Specific NTC Data needed                                       | Specific NTC Data needed                                       |

## 8.1.94 Q\_DISPLAY\_IS

| Name                    | Display mode for intervention speed   | Display mode for intervention speed   | Display mode for intervention speed   |
|-------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| Description             | Display mode for intervention speed   | Display mode for intervention speed   | Display mode for intervention speed   |
| Length of variable      | Minimum Value                         | Maximum Value                         | Resolution/formula                    |
| 2 bits                  |                                       |                                       |                                       |
| Special/Reserved Values | 00                                    | No display                            | No display                            |
| Special/Reserved Values | 01                                    | Display with normal bar width         | Display with normal bar width         |
| Special/Reserved Values | 10                                    | Display with wide bar width           | Display with wide bar width           |
| Special/Reserved Values | 11                                    | Spare                                 | Spare                                 |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.95 Q\_DISPLAY\_PS

| Name                    | Display mode for permitted speed   | Display mode for permitted speed   | Display mode for permitted speed   |
|-------------------------|------------------------------------|------------------------------------|------------------------------------|
| Description             | Display mode for permitted speed   | Display mode for permitted speed   | Display mode for permitted speed   |
| Length of variable      | Minimum Value                      | Maximum Value                      | Resolution/formula                 |
| 2 bits                  |                                    |                                    |                                    |
| Special/Reserved Values | 00                                 | No display                         | No display                         |
| Special/Reserved Values | 01                                 | Hook only displayed                | Hook only displayed                |
| Special/Reserved Values | 10                                 | Speed bar displayed without hook   | Speed bar displayed without hook   |
| Special/Reserved Values | 11                                 | Speed bar displayed with hook      | Speed bar displayed with hook      |

## 8.1.96 Q\_DISPLAY\_RS

| Name                    | Display mode for Release Speed                         | Display mode for Release Speed                         | Display mode for Release Speed                         |
|-------------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| Description             | Display mode for release speed supervision information | Display mode for release speed supervision information | Display mode for release speed supervision information |
| Length of variable      | Minimum Value                                          | Maximum Value                                          | Resolution/formula                                     |
| 2 bits                  |                                                        |                                                        |                                                        |
| Special/Reserved Values | 00                                                     | No display                                             | No display                                             |
| Special/Reserved Values | 01                                                     | Digital indicator only displayed                       | Digital indicator only displayed                       |
| Special/Reserved Values | 10                                                     | Bar indication only displayed                          | Bar indication only displayed                          |
| Special/Reserved Values | 11                                                     | Bar and digital indicator displayed                    | Bar and digital indicator displayed                    |

## 8.1.97 Q\_DISPLAY\_TD

| Name                    | Display mode for Target Distance                         | Display mode for Target Distance                         | Display mode for Target Distance                         |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Display mode for target distance supervision information | Display mode for target distance supervision information | Display mode for target distance supervision information |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 2 bits                  |                                                          |                                                          |                                                          |
| Special/Reserved Values | 00                                                       | No display                                               | No display                                               |
| Special/Reserved Values | 01                                                       | Digital indicator only displayed                         | Digital indicator only displayed                         |
| Special/Reserved Values | 10                                                       | Bar indication only displayed                            | Bar indication only displayed                            |
| Special/Reserved Values | 11                                                       | Bar and digital indicator displayed                      | Bar and digital indicator displayed                      |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.98 Q\_DISPLAY\_TS

| Name                    | Display mode for target speed   | Display mode for target speed    | Display mode for target speed    |
|-------------------------|---------------------------------|----------------------------------|----------------------------------|
| Description             | Display mode for target speed   | Display mode for target speed    | Display mode for target speed    |
| Length of variable      | Minimum Value                   | Maximum Value                    | Resolution/formula               |
| 2 bits                  |                                 |                                  |                                  |
| Special/Reserved Values | 00                              | No display                       | No display                       |
| Special/Reserved Values | 01                              | Hook only displayed              | Hook only displayed              |
| Special/Reserved Values | 10                              | Speed bar displayed without hook | Speed bar displayed without hook |
| Special/Reserved Values | 11                              | Speed bar displayed with hook    | Speed bar displayed with hook    |

## 8.1.99 Q\_FOLLOWING

| Name                    | Indicate a following request                                                                                                                                                                                                                                                                                                                                                             | Indicate a following request                                                                                                                                                                                                                                                                                                                                                             | Indicate a following request                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Due to the possible length of an STM request for Specific NTC Data, this qualifier is used to indicate to the ERTMS/ETCS on-board whether the request for Specific NTC Data is composed of several STM- 179 packets or not. It shall also be used for the Specific NTC data View values to indicate to the ERTMS/ETCS on-board whether it is composed of several STM-183 packets or not. | Due to the possible length of an STM request for Specific NTC Data, this qualifier is used to indicate to the ERTMS/ETCS on-board whether the request for Specific NTC Data is composed of several STM- 179 packets or not. It shall also be used for the Specific NTC data View values to indicate to the ERTMS/ETCS on-board whether it is composed of several STM-183 packets or not. | Due to the possible length of an STM request for Specific NTC Data, this qualifier is used to indicate to the ERTMS/ETCS on-board whether the request for Specific NTC Data is composed of several STM- 179 packets or not. It shall also be used for the Specific NTC data View values to indicate to the ERTMS/ETCS on-board whether it is composed of several STM-183 packets or not. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                                                                                                                                            | Maximum Value                                                                                                                                                                                                                                                                                                                                                                            | Resolution/formula                                                                                                                                                                                                                                                                                                                                                                       |
| 1 bit                   |                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                          |
| Special/Reserved Values | 0                                                                                                                                                                                                                                                                                                                                                                                        | No following packet to be managed together with the current one.                                                                                                                                                                                                                                                                                                                         | No following packet to be managed together with the current one.                                                                                                                                                                                                                                                                                                                         |
| Special/Reserved Values | 1                                                                                                                                                                                                                                                                                                                                                                                        | There is a following packet to be managed together with the current one.                                                                                                                                                                                                                                                                                                                 | There is a following packet to be managed together with the current one.                                                                                                                                                                                                                                                                                                                 |

## 8.1.100 Q\_OVR\_STATUS

| Name                    | ETCS Override status                                     | ETCS Override status                                     | ETCS Override status                                     |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Description             | Indicate to all STMs that an override has been triggered | Indicate to all STMs that an override has been triggered | Indicate to all STMs that an override has been triggered |
| Length of variable      | Minimum Value                                            | Maximum Value                                            | Resolution/formula                                       |
| 1 bits                  |                                                          |                                                          |                                                          |
| Special/Reserved Values | 0                                                        | ETCS Override status not active                          | ETCS Override status not active                          |
| Special/Reserved Values | 1                                                        | ETCS Override status active                              | ETCS Override status active                              |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.101 Q\_SOUND

| Name                    | Sound qualifier                    | Sound qualifier                                              | Sound qualifier                                              |
|-------------------------|------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Description             | Qualifier for the sound generation | Qualifier for the sound generation                           | Qualifier for the sound generation                           |
| Length of variable      | Minimum Value                      | Maximum Value                                                | Resolution/formula                                           |
| 2 bits                  |                                    |                                                              |                                                              |
| Special/Reserved Values | 0                                  | Stop sound generation for specified sound identifier         | Stop sound generation for specified sound identifier         |
| Special/Reserved Values | 1                                  | One shot play (Sound is played once)                         | One shot play (Sound is played once)                         |
| Special/Reserved Values | 2                                  | Continuous play (Sound is played again when definition ends) | Continuous play (Sound is played again when definition ends) |
| Special/Reserved Values | 3                                  | Reserved                                                     | Reserved                                                     |

## 8.1.102 T\_BUTTONEVENT

| Name                    | Time stamping of a button event                                             | Time stamping of a button event                                             | Time stamping of a button event                                             |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Description             | Local Reference Time of the button event as specified in [5], chapter 3.4.8 | Local Reference Time of the button event as specified in [5], chapter 3.4.8 | Local Reference Time of the button event as specified in [5], chapter 3.4.8 |
| Length of variable      | Minimum Value                                                               | Maximum Value                                                               | Resolution/formula                                                          |
| 32 bits                 | 0                                                                           | 4 294 967 295                                                               | 1 ms                                                                        |
| Special/Reserved Values |                                                                             |                                                                             |                                                                             |

## 8.1.103 T\_EB\_MAXDELAY

| Name                    | Brake interface maximum emergency brake command issue time                                                                                                                                                                                                   | Brake interface maximum emergency brake command issue time                                                                                                                                                                                                   | Brake interface maximum emergency brake command issue time                                                                                                                                                                                                   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                | Maximum Value                                                                                                                                                                                                                                                | Resolution/formula                                                                                                                                                                                                                                           |
| 8 bits                  | 10 ms                                                                                                                                                                                                                                                        | 2550 ms                                                                                                                                                                                                                                                      | Step of 10 ms                                                                                                                                                                                                                                                |
| Special/Reserved Values | 0                                                                                                                                                                                                                                                            | Reserved                                                                                                                                                                                                                                                     | Reserved                                                                                                                                                                                                                                                     |

## 8.1.104 T\_JD

| Name                    | Time stamping of a JD message                                                                  | Time stamping of a JD message                                                                  | Time stamping of a JD message                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Description             | Local Reference Time when the data sent to the JD was valid as specified in [5], chapter 3.4.8 | Local Reference Time when the data sent to the JD was valid as specified in [5], chapter 3.4.8 | Local Reference Time when the data sent to the JD was valid as specified in [5], chapter 3.4.8 |
| Length of variable      | Minimum Value                                                                                  | Maximum Value                                                                                  | Resolution/formula                                                                             |
| 32 bits                 | 0                                                                                              | 4 294 967 295                                                                                  | 1ms                                                                                            |
| Special/Reserved Values |                                                                                                |                                                                                                |                                                                                                |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.105 T\_ODO

| Name                    | Time stamping of an odometer measurement                                                  | Time stamping of an odometer measurement                                                  | Time stamping of an odometer measurement                                                  |
|-------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Description             | Local Reference Time when the odometer data were valid as specified in [5], chapter 3.4.8 | Local Reference Time when the odometer data were valid as specified in [5], chapter 3.4.8 | Local Reference Time when the odometer data were valid as specified in [5], chapter 3.4.8 |
| Length of variable      | Minimum Value                                                                             | Maximum Value                                                                             | Resolution/formula                                                                        |
| 32 bits                 | 0                                                                                         | 4 294 967 295                                                                             | 1ms                                                                                       |
| Special/Reserved Values |                                                                                           |                                                                                           |                                                                                           |

## 8.1.106 T\_ODOCYCLE

| Name                    | Typical cycle time of ERTMS/ETCS on-board Odometer Function   | Typical cycle time of ERTMS/ETCS on-board Odometer Function   | Typical cycle time of ERTMS/ETCS on-board Odometer Function   |
|-------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Description             |                                                               |                                                               |                                                               |
| Length of variable      | Minimum Value                                                 | Maximum Value                                                 | Resolution/formula                                            |
| 8 bits                  | 0 ms                                                          | 2550 ms                                                       | Step of 10 ms                                                 |
| Special/Reserved Values |                                                               |                                                               |                                                               |

## 8.1.107 T\_ODOMAXPROD

| Name                    | Maximum production delay time   | Maximum production delay time   | Maximum production delay time   |
|-------------------------|---------------------------------|---------------------------------|---------------------------------|
| Description             | Refer to [4] §12.4.1.4          | Refer to [4] §12.4.1.4          | Refer to [4] §12.4.1.4          |
| Length of variable      | Minimum Value                   | Maximum Value                   | Resolution/formula              |
| 8 bits                  | 10 ms                           | 2550 ms                         | Step of 10ms                    |
| Special/Reserved Values | 0                               | Reserved                        | Reserved                        |

## 8.1.108 T\_SB\_MAXDELAY

| Name                    | Brake interface maximum service brake command issue time                                                                                                                                                                                                     | Brake interface maximum service brake command issue time                                                                                                                                                                                                     | Brake interface maximum service brake command issue time                                                                                                                                                                                                     |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. | This is the maximum processing of the STM brake command by the ERTMS/ETCS on-board BIU Function. This is the time from the moment the BIU Function receives the STM command on the Profibus and the time the brake command is issued on the Train Interface. |
| Length of variable      | Minimum Value                                                                                                                                                                                                                                                | Maximum Value                                                                                                                                                                                                                                                | Resolution/formula                                                                                                                                                                                                                                           |
| 8 bits                  | 10 ms                                                                                                                                                                                                                                                        | 2550 ms                                                                                                                                                                                                                                                      | Step of 10 ms                                                                                                                                                                                                                                                |
| Special/Reserved Values | 0                                                                                                                                                                                                                                                            | Not applicable (SB command not available)                                                                                                                                                                                                                    | Not applicable (SB command not available)                                                                                                                                                                                                                    |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.109 T\_SOUND

| Name                    | Sound segment duration       | Sound segment duration       | Sound segment duration                          |
|-------------------------|------------------------------|------------------------------|-------------------------------------------------|
| Description             | Duration of a sound segment. | Duration of a sound segment. | Duration of a sound segment.                    |
| Length of variable      | Minimum Value                | Maximum Value                | Resolution/formula                              |
| 8 bits                  | 100 ms                       | 10 000 ms                    | T = T_SOUND * 100 ms Range 100 ms to 10 seconds |
| Special/Reserved Values | 0                            | Reserved                     | Reserved                                        |
| Special/Reserved Values | 101-255                      | Spare                        | Spare                                           |

## 8.1.110 V\_EST

| Name                    | Estimated value of a measured speed                                                                     | Estimated value of a measured speed                                                                     | Estimated value of a measured speed                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Description             | Signed estimated value of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed estimated value of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed estimated value of a measured speed provided by the odometer to STM. Coded as two's complement . |
| Length of variable      | Minimum Value                                                                                           | Maximum Value                                                                                           | Resolution/formula                                                                                      |
| 16 bits                 | - 32 768 cm/s                                                                                           | + 32 767 cm/s                                                                                           | Signed, unit 1 cm/s                                                                                     |
| Special/Reserved Values |                                                                                                         |                                                                                                         |                                                                                                         |

## 8.1.111 V\_INTERV

| Name                    | Intervention speed   | Intervention speed   | Intervention speed   |
|-------------------------|----------------------|----------------------|----------------------|
| Description             |                      | Maximum Value        |                      |
| 10 bits                 | 0 km/h               | 600 km/h             | 1 km/h               |
| Special/Reserved Values | 601-1022             | Spare                |                      |
| Special/Reserved Values | 1023                 | Unknown value        |                      |

## 8.1.112 V\_MAX

| Name                    | Upper bound of the functional confidence interval of a measured speed                                                                                  | Upper bound of the functional confidence interval of a measured speed                                                                                  | Upper bound of the functional confidence interval of a measured speed                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Signed value of the upper bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed value of the upper bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed value of the upper bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . |
| Length of variable      | Minimum Value                                                                                                                                          | Maximum Value                                                                                                                                          | Resolution/formula                                                                                                                                     |
| 16 bits                 | - 32 768 cm/s                                                                                                                                          | + 32 767 cm/s                                                                                                                                          | Signed, unit 1 cm/s.                                                                                                                                   |
| Special/Reserved Values |                                                                                                                                                        |                                                                                                                                                        |                                                                                                                                                        |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.113 V\_MIN

| Name                    | Lower bound of the functional confidence interval of a measured speed                                                                                  | Lower bound of the functional confidence interval of a measured speed                                                                                  | Lower bound of the functional confidence interval of a measured speed                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Signed value of the lower bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed value of the lower bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . | Signed value of the lower bound of the functional confidence interval of a measured speed provided by the odometer to STM. Coded as two's complement . |
| Length of variable      | Minimum Value                                                                                                                                          | Maximum Value                                                                                                                                          | Resolution/formula                                                                                                                                     |
| 16 bits                 | - 32 768 cm/s                                                                                                                                          | + 32 767 cm/s                                                                                                                                          | Signed, unit 1 cm/s                                                                                                                                    |
| Special/Reserved Values |                                                                                                                                                        |                                                                                                                                                        |                                                                                                                                                        |

## 8.1.114 V\_PERMIT

| Name                    | Permitted speed   | Permitted speed   | Permitted speed    |
|-------------------------|-------------------|-------------------|--------------------|
| Description             |                   | Maximum Value     | Resolution/formula |
| 10 bits                 | 0 Km/h            | 600 Km/h          | 1 Km/h             |
| Special/Reserved Values | 601-1023          | Spare             | Spare              |

## 8.1.115 V\_RELEASE

| Name                    | Release speed   | Release speed   | Release speed   |
|-------------------------|-----------------|-----------------|-----------------|
| Description             |                 | Maximum Value   |                 |
| 10 bits                 | 0 km/h          | 600 km/h        | 1 km/h          |
| Special/Reserved Values | 601-1022        | Spare           |                 |
| Special/Reserved Values | 1023            | Unknown value   |                 |

## 8.1.116 V\_STMMAX

| Name                    | STM max speed   | STM max speed                      | STM max speed                      |
|-------------------------|-----------------|------------------------------------|------------------------------------|
| Description             |                 |                                    |                                    |
| 7 bits                  | 0 km/h          | 600 km/h                           | 5 km/h                             |
| Special/Reserved Values | 121-126         | Spare                              | Spare                              |
| Special/Reserved Values | 127             | No STM max speed to be supervised. | No STM max speed to be supervised. |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.117 V\_STMSYS

| Name                    | STM system speed   | STM system speed                      | STM system speed                      |
|-------------------------|--------------------|---------------------------------------|---------------------------------------|
| Description             |                    | Maximum Value                         | Resolution/formula                    |
| 7 bits                  | 0 km/h             | 600 km/h                              | 5 km/h                                |
| Special/Reserved Values | 121-126            | Spare                                 | Spare                                 |
| Special/Reserved Values | 127                | No STM system speed to be supervised. | No STM system speed to be supervised. |

## 8.1.118 V\_TARGET

| Name                    | Target speed   | Target speed   | Target speed   |
|-------------------------|----------------|----------------|----------------|
| Description             |                | Maximum Value  |                |
| 7 bits                  | 0 Km/h         | 600            | 5 km/h         |
| Special/Reserved Values | 121-126        | Spare          |                |
| Special/Reserved Values | 127            | Unknown value  |                |

## 8.1.119 X\_CAPTION

| Name                    | Caption text byte                                                       | Caption text byte                                                       | Caption text byte                                                       |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Description             | Byte of bytestring used for caption text of button, indicator and data. | Byte of bytestring used for caption text of button, indicator and data. | Byte of bytestring used for caption text of button, indicator and data. |
| Length of variable      | Minimum Value                                                           | Maximum Value                                                           | Resolution/formula                                                      |
| 8 bits                  | 0                                                                       | 255                                                                     |                                                                         |
| Special/Reserved Values |                                                                         |                                                                         |                                                                         |

## 8.1.120 X\_TEXT

| Name                    | Text byte                                                                                             | Text byte                                                                                             | Text byte                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Description             | Byte of bytestring used for text message string. Encoded in UTF-8 according to [9] with 1 or 2 bytes. | Byte of bytestring used for text message string. Encoded in UTF-8 according to [9] with 1 or 2 bytes. | Byte of bytestring used for text message string. Encoded in UTF-8 according to [9] with 1 or 2 bytes. |
| Length of variable      | Minimum Value                                                                                         | Maximum Value                                                                                         | Resolution/formula                                                                                    |
| 8 bits                  | 0                                                                                                     | 255                                                                                                   |                                                                                                       |
| Special/Reserved Values |                                                                                                       |                                                                                                       |                                                                                                       |

© This document has been developed and released by UNISIG

<!-- image -->

## 8.1.121 X\_VALUE

| Name                    | Value byte                                                                                                                          | Value byte                                                                                                                          | Value byte                                                                                                                          |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Description             | Byte of bytestring used for data value, default value of data and for dedicated keyboard values. Encoded in UTF-8 according to [9]. | Byte of bytestring used for data value, default value of data and for dedicated keyboard values. Encoded in UTF-8 according to [9]. | Byte of bytestring used for data value, default value of data and for dedicated keyboard values. Encoded in UTF-8 according to [9]. |
| Length of variable      | Minimum Value                                                                                                                       | Maximum Value                                                                                                                       | Resolution/formula                                                                                                                  |
| 8 bits                  | 0                                                                                                                                   | 255                                                                                                                                 |                                                                                                                                     |
| Special/Reserved Values |                                                                                                                                     |                                                                                                                                     |                                                                                                                                     |

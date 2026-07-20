---
title: "PtP data link CP 341 (S7-300, S7-400)"
package: ProgFBCP341enUS
topics: 15
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PtP data link CP 341 (S7-300, S7-400)

This section contains information on the following topics:

- [P_SND_RK: Fetching or sending data (S7-300, S7-400)](#p_snd_rk-fetching-or-sending-data-s7-300-s7-400)
- [P_RCV_RK: Receive data or Provide data (S7-300, S7-400)](#p_rcv_rk-receive-data-or-provide-data-s7-300-s7-400)
- [P_PRT341: Print message text with up to 4 variables (S7-300, S7-400)](#p_prt341-print-message-text-with-up-to-4-variables-s7-300-s7-400)
- [V24_STAT_340 / V24_STAT: Reading accompanying signals from the RS232C interface (S7-300, S7-400)](#v24_stat_340-v24_stat-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400)
- [V24_SET_340 / V24_SET: Writing accompanying signals to the RS232C interface (S7-300, S7-400)](#v24_set_340-v24_set-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

## P_SND_RK: Fetching or sending data (S7-300, S7-400)

This section contains information on the following topics:

- [P_SND_RK: Fetching or sending data (S7-300, S7-400)](#p_snd_rk-fetching-or-sending-data-s7-300-s7-400-1)
- [P_SND_RK: Send data with 3964(R) and ASCII drivers (S7-300, S7-400)](#p_snd_rk-send-data-with-3964r-and-ascii-drivers-s7-300-s7-400)
- [P_SND_RK: Send data with RK 512 (S7-300, S7-400)](#p_snd_rk-send-data-with-rk-512-s7-300-s7-400)
- [P_SND_RK: Fetch data with RK 512 (S7-300, S7-400)](#p_snd_rk-fetch-data-with-rk-512-s7-300-s7-400)

### P_SND_RK: Fetching or sending data (S7-300, S7-400)

#### P_SND_RK

The P_SND_RK instruction distinguishes the following applications:

- [P_SND_RK: Send data with 3964(R) and ASCII drivers](#p_snd_rk-send-data-with-3964r-and-ascii-drivers-s7-300-s7-400)
- [P_SND_RK: Send data with RK 512](#p_snd_rk-send-data-with-rk-512-s7-300-s7-400)
- [P_SND_RK: Fetch data with RK 512](#p_snd_rk-fetch-data-with-rk-512-s7-300-s7-400)

---

**See also**

[Data transmission from CPU to communication module with P_SND_RK (CP 341) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-from-cpu-to-communication-module-with-p_snd_rk-cp-341-s7-300-s7-400)

### P_SND_RK: Send data with 3964(R) and ASCII drivers (S7-300, S7-400)

#### Description

The P_SND_RK instruction transfers data blocks from a DB to the CP 341 as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the P_SND_RK instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

#### Operating principle

Data transmission is initiated by a positive edge at the input REQ. Data transmission can take several calls (program cycles), depending on the data volume.

The P_SND_RK instruction can be called in the cycle by setting signal state "1" at the R parameter input. This setting cancels the transmission to CP 341 and resets the P_SND_RK instruction to the initial state. Data that has already been received by CP 341 is still sent to the communication partner. If the signal state remains static at "1" at the input R, sending is disabled.

Parameter LADDR specifies the address of the CP 341 to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for a RESET of the P_SND_RK instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Send DB no.: CPU-specific, zero is not allowed |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8190 Send data starting from data byte |
| LEN | INPUT | INT | Data length  1 ≤ LEN ≤ 4096, specified in number of bytes |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

> **Note**
>
> The R_CPU_NO, R_TYP, R_NO, R_OFFSET, R_CF_BYT and R_CF_BIT parameters are irrelevant for procedure 3964(R) and the ASCII driver and require no data. Similarly, the SF parameter requires no data since 'S' for Send is set by default.

#### Allocation in the data area

The P_SND_RK instruction works in combination with an I_SND_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR or SFCSTATUS variable for additional details. This error variable must be loaded via symbolic access to the instance DB.

#### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/16935990155_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

#### Rules

> **Note**
>
> The P_SND_RK instruction does not have a parameter check. If the parameter assignment is incorrect, the CPU can go to STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_SND_RK instruction must be completed before the CP 341 can execute a job triggered after the CPU changed from STOP to RUN . A job initiated in the meantime is not lost. Once the startup coordination is completed, the job is sent to the CP 341.

### P_SND_RK: Send data with RK 512 (S7-300, S7-400)

#### Description

The P_SND_RK instruction can be used with parameter setting SF = 'S' to send data from an S7 data area to a CP 341.

#### Operating principle

Data transmission is initiated by a positive edge at the input REQ. Data transmission can take several calls (program cycles), depending on the data volume (LEN).

Parameter LADDR specifies the address of the CP 341 to be addressed.

The area of the data blocks is the only permissible source for data to be sent. The source is appropriately specified by setting the DB number (DB_NO) and offset (DBB_NO) of the first data byte to be transmitted from this data block.

Data blocks (DB) and extended data blocks (DX) are valid destination data types (R_TYP). The destination is appropriately specified by means of the CPU number (R_CPU_NO, relevant only to multi-processor communication), the data type (R_TYP: DB or DX), the DB number (R_NO) and the offset (R_OFFSET) to which the first byte is to be written.

The interprocessor communication flag byte and bit on the partner CPU are specified in R_CF_BYT and R_CF_BIT.

The P_SND_RK instruction can be called in the cycle by setting signal state "1" at the R parameter input. This setting cancels the transmission to CP 341 and resets the P_SND_RK instruction to the initial state. Data that has already been received by CP 341 is still sent to the communication partner. A static signal state "1" at the input R indicates that data transmission is disabled.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for a RESET of the P_SND_RK instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| SF | INPUT | CHAR | Selection for Send data or Fetch data  SF = 'S' (Send)  Default: 'S' |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. Default: 0 |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number of source  Send DB no.: CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number of source  0 ≤ DBB_NO ≤ 8190 Send data starting from data byte |
| LEN | INPUT | INT | Data length of the message frame to be sent  1 ≤ LEN ≤ 4096, specified in number of bytes; only even-numbered values are appropriate |
| R_CPU_NO | INPUT | INT | CPU number of the partner CPU  0 ≤ R_CPU_NO ≤ 4, only for multiprocessor mode. Default: 1 |
| R_TYP | INPUT | CHAR | Address type on the partner CPU  'D': Data block  ‘X’: Expanded data block |
| R_NO | INPUT | INT | Data block number on the partner CPU  0 ≤ R_NO ≤ 255 |
| R_OFFSET | INPUT | INT | Data byte number on the partner CPU  0 ≤ R_OFFSET ≤ 510, even-numbered values only |
| R_CF_BYT | INPUT | INT | Interprocessor communication flag byte on partner CPU  0 ≤ R_CF_BYTE ≤ 255  Default: 255 (means: without interprocessor communication flag) |
| R_CF_BIT | INPUT | INT | Interprocessor communication flag bit on the partner CPU  0 ≤ R_CF_BIT ≤ 7 |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

#### Information in the message frame header

The table below shows the information in the header of the RK 512 message frame.

Information in the RK 512 message frame header for "Send data" request

| Source on your S7 automation system (local CPU) | To the destination,  partner CPU | Message frame header, bytes |  |  |
| --- | --- | --- | --- | --- |
|  |  | 3/4 command type | 5/6 Z-DBNR/Z offset | 7/8 Number in |
| Data block | Data block | AD | DB/DW | Words |
| Data block | Expanded data block | AD | DB/DW | Words |
| D-DBNO: Destination data block number  D-Offset: Destination start address  DW: Offset in words |  |  |  |  |

#### Allocation in the data area

The P_SND_RK instruction works in combination with an I_SND_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

#### Special features for sending data

Note the following special features with regard to sending data:

- RK 512 allows only an even-numbered amount of data to be sent. If you specify an odd-numbered amount of data for the length (LEN), an additional filler byte with a value of "0" is sent at the end of the data.
- RK 512 allows only an even-numbered offset. If you specify an odd-numbered offset, the data is stored in the partner starting from the next lower even-numbered offset.

  Example: Offset is 7, data is stored from byte 6.

#### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/16935990155_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

#### Rule

> **Note**
>
> The P_SND_RK instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

### P_SND_RK: Fetch data with RK 512 (S7-300, S7-400)

#### Description

The P_SND_RK instruction can be used with parameter setting SF = F to fetch data from a remote communication partner and save it to an S7 data area of your automation system.

> **Note**
>
> To fetch data from a CP 341, you must always program a P_RCV_RK instruction on the CP 341.

#### Operating principle

Data transmission is initiated by a positive edge at the input REQ. Data transmission can take several calls (program cycles), depending on the data volume (LEN).

Parameter LADDR specifies the address of the CP 341 to be addressed.

The communication partner from which the data is fetched is specified by the CPU number (R_CPU_NO, relevant only to multiprocessor communication). The following data types (R_TYP) are valid sources for the data to be fetched: data blocks, extended data blocks, bit memory, inputs, outputs, counters and timers. The source is fully specified by the data type (R_TYP), the data block number (R_NO, relevant only to data blocks and expanded data blocks) and the offset(R_OFFSET) of the first data byte in this area to transmit.

The interprocessor communication flag byte and bit on the partner CPU are specified in R_CF_BYT and R_CF_BIT.

The only permissible destination areas are data blocks (DB). The destination is specified by the data block number (DB_NO) and offset (DBB_NO) to which the first byte is written.

The P_SND_RK instruction can be called in the cycle by setting signal state "1" at the R parameter input. This setting cancels the transmission from CP 341 and resets the P_SND_RK instruction to the initial state. A static signal status "1" at the input R indicates that fetching is disabled.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for a RESET of the P_SND_RK instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| SF | INPUT | CHAR | Selection for Send data or Fetch data  SF = 'F' (Fetch)default value: 'S' (Send) |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Fetching is disabled. Default: 0 |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number of destination  Send DB no.: CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number of destination  0 ≤ DBB_NO ≤ 8190 Send data starting from data byte |
| LEN | INPUT | INT | Data length of the message frame to be fetched  1 ≤ LEN ≤ 4096, specified in number of bytes<sup>1</sup> |
| R_CPU_NO | INPUT | INT | CPU number of the partner CPU  0 ≤ R_CPU_NO ≤ 4, only for multiprocessor mode. Default: 1 |
| R_TYP | INPUT | CHAR | Address type on the partner CPU  'D': Data block 'X': Expanded data block  'M': Memory bit  'I': Inputs 'O': Outputs 'C': Counters 'T': Timers |
| R_NO | INPUT | INT | Data block number on the partner CPU  0 ≤ R_NO ≤ 255 |
| R_OFFSET | INPUT | INT | Data byte number on the partner CPU |
| R_CF_BYT | INPUT | INT | Interprocessor communication flag byte on partner CPU  0 ≤ CF_BYTE ≤ 255 Default: 255 (means: without interprocessor communication flag) |
| R_CF_BIT | INPUT | INT | Interprocessor communication flag bit on the partner CPU  0 ≤ CF_BIT ≤ 7 |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

#### R_TYP, R_NO and R_OFFSET parameters

| Source on the partner CPU | R_TYP | R_NO | R_OFFSET (in bytes)  (This value is specified by the partner CPU.) |
| --- | --- | --- | --- |
| Data block | 'D' | 0 - 255 | 0 - 510  (only even-numbered values are appropriate!) |
| Expanded data block | 'X' | 0 - 255 | 0 - 510  (only even-numbered values are appropriate!) |
| Bit memory | 'M' | irrelevant | 0 - 255 |
| Inputs | 'I' | irrelevant | 0 - 255 |
| Outputs | 'O' | irrelevant | 0 - 255 |
| Counters | 'C' | irrelevant | 0 - 255 |
| Timers | 'T' | irrelevant | 0 - 255 |

#### Information in the message frame header

The table below shows the information in the header of the RK 512 message frame.

| Source on the partner CPU | To the destination, your S7 automation system (local CPU) | Message frame header, bytes |  |  |
| --- | --- | --- | --- | --- |
| 3/4 command type | 5/6 Q-DBNR/Q offset | 7/8 Number in |  |  |
| Data block | Data block | ED | DB/DW | Words |
| Expanded data block | Data block | EX | DB/DW | Words |
| Bit memory | Data block | EM | Byte address | Bytes |
| Inputs | Data block | EI | Byte address | Bytes |
| Outputs | Data block | EO | Byte address | Bytes |
| Counters | Data block | EC | Counter no. | Words |
| Timers | Data block | ET | Timer number | Words |
| S-DBNO: Source data block number  S-Offset: Source start address |  |  |  |  |

#### Allocation in the data area

The P_SND_RK instruction works in combination with an I_SND_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

#### Special features for (expanded) data blocks

Note the following special features with regard to fetching data from data blocks and expanded data blocks:

- RK 512 allows only an even-numbered amount of data to be fetched. If you specify an odd-numbered amount for the length (LEN), an extra byte is always sent. In the destination DB, however, the correct amount of data is entered.
- RK 512 allows only an even-numbered offset. If you specify an odd-numbered offset, the data is fetched from the partner starting from the next lower even-numbered offset.

  Example: Offset is 7, data is fetched as of byte 6.

#### Special features for timers and counters

If you fetch timers or counters from the communication partner, remember that 2 bytes are fetched for each timer or counter. For example, if you want to fetch 10 counters, you must enter 20 as the length.

#### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERRORparameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/16935990155_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

#### Rule

> **Note**
>
> The P_SND_RK instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

## P_RCV_RK: Receive data or Provide data (S7-300, S7-400)

This section contains information on the following topics:

- [P_SND_RK: Receive or provide data (S7-300, S7-400)](#p_snd_rk-receive-or-provide-data-s7-300-s7-400)
- [P_RCV_RK: Receiving data with 3964(R) or ASCII driver (S7-300, S7-400)](#p_rcv_rk-receiving-data-with-3964r-or-ascii-driver-s7-300-s7-400)
- [P_RCV_RK: Receive data with RK 512 (S7-300, S7-400)](#p_rcv_rk-receive-data-with-rk-512-s7-300-s7-400)
- [P_RCV_RK: Provide data with RK 512 (S7-300, S7-400)](#p_rcv_rk-provide-data-with-rk-512-s7-300-s7-400)

### P_SND_RK: Receive or provide data (S7-300, S7-400)

#### P_RCV_RK

The P_RCV_RK instruction distinguishes the following applications:

- [P_RCV_RK: Receiving data with 3964(R) or ASCII driver](#p_rcv_rk-receiving-data-with-3964r-or-ascii-driver-s7-300-s7-400)
- [P_RCV_RK: Receive data with RK 512](#p_rcv_rk-receive-data-with-rk-512-s7-300-s7-400)
- [P_RCV_RK: Provide data with RK 512](#p_rcv_rk-provide-data-with-rk-512-s7-300-s7-400)

---

**See also**

[Data transmission from the communication module to the CPU with P_RCV_RK (CP 341) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-from-the-communication-module-to-the-cpu-with-p_rcv_rk-cp-341-s7-300-s7-400)

### P_RCV_RK: Receiving data with 3964(R) or ASCII driver (S7-300, S7-400)

#### Description

The P_RCV_RK instruction transfers data from CP 341 to an S7 data area as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the P_RCV_RK instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

#### Operating principle

The (static) signal state "1" at parameter EN_R enables the check for data to be read from CP 341 . An active transmission can be canceled by setting signal state "0" at parameter EN_R . (Because transmission may sometimes not start up again after setting parameter EN_R to "1", you should set parameter R to "1" in addition to setting EN_R to "0" to cancel an active transmission.) The canceled receive request is terminated with an error message (STATUS output). Receiving is disabled as long as signal state "0" is set at parameter EN_R . Data transmission can take several calls (program cycles), depending on the data volume.

If the instruction detects signal state "1" at parameter R, the current transmission job is canceled and the P_RCV_RK instruction is reset to the initial state. Receiving is disabled as long as signal state "1" is set at parameter R.

Parameter LADDR is used to select the CP 341 to be addressed.

Output NDR indicates "Job completed without errors/data received" (all data read) and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. NDR and ERROR/STATUS are also output for the RESET of the P_RCV_RK instruction (parameter LEN == 16#00). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enable data reading |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Receiving is disabled. |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Receive DB No.: CPU-specific, zero is not allowed |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8190 Receive data starting from data byte |
| NDR <sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00; |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN <sup>1</sup> | OUTPUT | INT | Length of the message frame received  1 ≤ LEN ≤ 4096, specified in number of bytes |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

> **Note**
>
> The L_TYP, L_NO, L_OFFSET, L_CF_BYT and L_CF_BIT parameters are irrelevant for the 3964(R) procedure and ASCII driver and require no data.

#### Allocation in the data area

The P_RCV_RK instruction works in combination with an I_RCV_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0E occurs, you can examine the SFCERR or SFCSTATUS tag for additional details. This error tag must be loaded via symbolic access to the instance DB.

#### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the input circuit of EN_R and R.

![Time sequence chart](images/16935840651_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

#### Rules

> **Note**
>
> The P_RCV_RK instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_RCV_RK instruction must be completed before the CP 341 can execute a job triggered after the CPU changed from STOP to RUN.

### P_RCV_RK: Receive data with RK 512 (S7-300, S7-400)

#### Description

The P_RCV_RK instruction sends data from the CP 341 to an S7 data area. For data transmission, the P_RCV_RK instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

#### Operating principle

The (static) signal state "1" at parameter EN_R enables the check for data to be read from CP 341 . An active transmission can be canceled by setting signal state "0" at parameter EN_R . The canceled receive request is terminated with an error message (STATUS output). Receiving is disabled as long as signal state "0" is set at parameter EN_R . Data transmission can take several calls (program cycles), depending on the data volume.

Parameter LADDR specifies the address of the CP 341 to be addressed.

If the communication partner specifies the destination "DB", the data is placed in the data area specified in the RK 512 message frame header. Using the (L_...) parameter, you can identify the destination area type (L_TYP), the destination data block number (L_NO, only relevant for L_TYP = DB), the offset in the destination area (L_OFFSET) and the length (LEN) of transmitted data. If the partner specifies the data destination "DX", the data is saved to the data block (DB) that is specified at the DB_NO and DBB_NO parameters.

If the instruction detects signal state "1" at parameter R, the current transmission job is canceled and the P_RCV_RK instruction is reset to the initial state. Receiving is disabled as long as the signal state at the R parameter is "1".

Output NDR indicates "Job completed without errors/data received" (all data read). The L_TYP, L_NO and L_OFFSET parameters indicate the data storage location for the duration of one cycle. The L_CF_BYT and L_CF_BIT and the length LEN parameters of the respective job are also indicated for one cycle.

#### Using interprocessor communication flags

The interprocessor communication flag specified in the RK 512 message frame header is verified prior to data reception. The data is not transmitted unless the value of the interprocessor communication flag is "0". When transmission is completed, the interprocessor communication flag is set to the value "1" and output for one cycle (NDR) at the instruction.

The user program can evaluate the interprocessor communication flag in order to find out if the transmitted data can be processed. Once the data has been processed, the user must reset the interprocessor communication flag to "0". The communication partner can now issue a SEND request again.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enables data receipt |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Receiving is disabled. Default: 0 |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number of the receive data (destination)  Receive data block no.: CPU-specific, zero not allowed   (Relevant only for DX data destination) |
| DBB_NO | INPUT | INT | Data byte number of the receive data (destination)  0 ≤ DBB_NO ≤ 8190 Receive data starting from data byte   (Relevant only for DX data destination) |
| L_TYP<sup>1</sup> | OUTPUT | CHAR | Type of area on local CPU (destination)  'D': Data block |
| L_NO <sup>1</sup> | OUTPUT | INT | Data block number on local CPU (destination)  0 ≤ L_NO ≤ 255 |
| L_OFFSET<sup>1</sup> | OUTPUT | INT | Data byte number on local CPU (destination)  0 ≤ L_OFFSET ≤ 510 |
| L_CF_BYT<sup>1</sup> | OUTPUT | INT | Interprocessor communication flag byte on local CPU  0 ≤ L_CF_BYTE ≤ 255255 means: Without interprocessor communication flag |
| L_CF_BIT <sup>1</sup> | OUTPUT | INT | Interprocessor communication flag bit on local CPU  0 ≤ L_CF_BIT ≤ 7 |
| NDR<sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN<sup>1</sup> | OUTPUT | INT | Length of the message frame received  0 ≤ LEN ≤ 4096, specified in number of bytes |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

#### Allocation in the data area

The P_RCV_RK instruction works in combination with an I_RCV_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0E occurs, you can examine the SFCERR or SFCSTATUS variable for additional details. This error variable must be loaded via symbolic access to the instance DB.

#### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the input circuit of EN_R and R.

![Time sequence chart](images/16935840651_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

#### How to Handle an Error

ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, STATUS has a value 0. NDR and ERROR/STATUS are also output for the RESET of the P_RCV_RK instruction (parameter LEN == 16#00). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Rule

> **Note**
>
> The P_RCV_RK instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

### P_RCV_RK: Provide data with RK 512 (S7-300, S7-400)

#### Description

The P_RCV_RK instruction must be called whenever the communication partner executes a "Fetch data" job (FETCH job).

The P_RCV_RK instruction provides data from an S7 data area to CP 341 . For data transmission, the P_RCV_RK instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

#### Operating principle

A (static) signal state "1" at the EN_R parameter enables a check that determines whether data is to be provided to CP 341 . An active transmission can be canceled by setting signal state "0" at parameter EN_R . The canceled request is terminated with an error message (STATUS output). The job is disabled as long as signal state "0" is set at parameter EN_R . Data transmission can take several calls (program cycles), depending on the data volume.

The first RK 512 message frame specifies the type of source area (L_TYP), the source data block number (L_NO, relevant only if L_TYP = DB), the offset in the source area (L_OFFSET) and the length (LEN) of data to be provided. The instruction evaluates this message frame information and transmits the requested data to the CP 341. The DB_NO and DBB_NO parameters are insignificant for the P_RCV_RK instruction.

Parameter LADDR specifies the address of the CP 341 to be addressed.

If the instruction detects signal state "1" at parameter R, the current transmission job is canceled and the P_RCV_RK instruction is reset to the initial state. The request is disabled as long as the signal state at the R parameter is "1".

Output NDR indicates "Job completed without errors/data received" (all data read). The source of fetched data is indicated at the L_TYP, L_NO and L_OFFSET parameters for the duration of one cycle (valid data types: data blocks, input bytes, output bytes, timers and counters). The L_CF_BYT and L_CF_BIT and the length LEN parameters of the respective job are also indicated for one cycle.

> **Note**
>
> The length of timers or counters the communication partner fetches from the CP 341 is limited to 32 bytes (16 timers or counters, 2 bytes each).

#### Using interprocessor communication flags

Following receipt of the message frame, the interprocessor communication flags specified in the RK 512 message frame header are checked. The data is not provided unless the value of the interprocessor communication flag is "0". When transmission is completed, the interprocessor communication flag is set to the value "1" and output for one cycle (NDR) at the instruction.

The user program can evaluate the interprocessor communication flag in order to find out if the provided data can be accessed again. Once the data has been processed, the user must reset the interprocessor communication flag to "0". The communication partner can now issue a FETCH request again.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enables data provision |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Disables providing. Default: 0 |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | irrelevant |
| DBB_NO | INPUT | INT | irrelevant |
| L_TYP<sup>1</sup> | OUTPUT | CHAR | Type of area on local CPU (source)  'D': Data block  'M' Memory bit  'I': Inputs 'O': Outputs 'C': Counters 'T': Timers |
| L_NO<sup>1</sup> | OUTPUT | INT | Data block number on local CPU (source)  0 ≤ L_NO ≤ 255 (only relevant, if L_TYP = D) |
| L_OFFSET<sup>1</sup> | OUTPUT | INT | Data byte number on local CPU (source)  0 ≤ L_OFFSET ≤ 510 (dependent on the area type) |
| L_CF_BYT<sup>1</sup> | OUTPUT | INT | Interprocessor communication flag byte on local CPU  0 ≤ CF_BYTE ≤ 255  255 means: Without interprocessor communication flag |
| L_CF_BIT<sup>1</sup> | OUTPUT | INT | Interprocessor communication flag bit on local CPU  0 ≤ CF_BIT ≤ 7 |
| NDR<sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN<sup>1</sup> | OUTPUT | INT | Length of the message frame received  0 ≤ LEN ≤ 4096, specified in number of bytes |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

#### Allocation in the data area

The P_RCV_RK instruction works in combination with an I_RCV_RK instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0E occurs, you can examine the SFCERR or SFCSTATUS variable for additional details.

#### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the input circuit of EN_R and R.

![Time sequence chart](images/16935840651_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

#### How to Handle an Error

ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. NDR and ERROR/STATUS are also output for the RESET of the P_RCV_RK instruction (parameter LEN == 16#00). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Rule

> **Note**
>
> The P_RCV_RK instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

## P_PRT341: Print message text with up to 4 variables (S7-300, S7-400)

### Description

The P_PRT341 instruction is available for printing message texts. The P_PRT341 instruction transfers a process message to the CP 341, for example. CP 341 logs the process message to the connected printer.

### Operating principle

The P_PRT341 instruction transmits a message text with up to four variables to CP 341. For data transmission, the P_PRT341 instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

The DB_NO and DBB_NO parameters enable access to the pointers (to data blocks) for the format string and the four variables. The pointers must be stored without gaps and in a specific sequence in the parameterized data block. This is the pointer DB (see Figure "Pointer DB").

A positive edge at the input REQ initiates the transmission of the message text. The frame starts with the format string of the message text, This is followed by tags 1 to 4.

Data transmission can take several calls (program cycles), depending on the data volume.

The P_PRT341 instruction can be called in the cycle by setting signal state "1" at the R parameter input. This setting cancels the transmission to CP 341 and resets the P_PRT341 instruction to the initial state. Data that has already been received by CP 341 is still sent to the communication partner. A static signal state "1" at the input R indicates that the transmission of print jobs is disabled.

Parameter LADDR specifies the address of the CP 341 to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for a RESET of the P_PRT341 instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Printing is disabled |
| LADDR | INPUT | INT | Start address of CP 341  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Pointer to pointer DB:  CPU-specific, zero is not allowed  (The pointers to variables and format string are stored in the pointer DB in a fixed order.) |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8162 Pointer as of data byte |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Assignment in the Data Area, Instance DB

The P_PRT341 instruction works in combination with an I_PRINT instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR or SFCSTATUS variable for additional details.

### Assignment in the Data Area, Pointer DB

The P_PRT341 instruction uses the DB_NO and DBB_NO parameters to access a pointer DB in which the pointers to the data blocks containing the message texts and variables are stored in a fixed sequence. You have to create the pointer DB.

The figure shows the syntax of the pointer DB that is addressed by means of the DB_NO and DBB_NO parameters of the P_PRT341 instruction.

![Assignment in the Data Area, Pointer DB](images/21571800843_DV_resource.Stream@PNG-en-US.png)

### Permissible DB Number

The permissible DB numbers are CPU-specific. If the value 16#00 is specified as the DB number for "Pointer to variable", this variable is interpreted as not present and the pointer is set to the next variable or the format string.

If the DB number is equal to the value 16#00 in "Pointer to format string", the print job is canceled and event ID 16#1E43 is indicated at parameter output STATUS of the P_PRT341 instruction.

### Permissible DBB Number

The variable or format string begins at the parameterized DBB number. The variables can have a maximum length of 32 bytes and the format string can have a maximum length of 150 bytes.

If the maximum length is exceeded, the print job is canceled and event ID 16#1E41 is indicated at parameter output STATUS of the P_PRT341 instruction.

### Permissible Length

The entry length in the pointer DB is to be set for each display type (data type) independently from the precision used.

### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/21571804683_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. It does not have to have a signal state of "1" during the entire transmission operation.

### Rules

> **Note**
>
> The P_PRT341 instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_PRT341 instruction must be completed before the CP 341 can execute a job triggered after the CPU changed from STOP to RUN. A job initiated in the meantime is not lost. Once the startup coordination is completed, the job is sent to the CP 341.

---

**See also**

[Data transmission with the printer driver (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-with-the-printer-driver-s7-300-s7-400)

## V24_STAT_340 / V24_STAT: Reading accompanying signals from the RS232C interface (S7-300, S7-400)

### Description

The V24_STAT_340 (CP 340) / V24_STAT (CP 341) instruction reads the RS 232C accompanying signals from the CP 34x and makes them available to you at the block parameters. The V24_STAT_340 / V24_STAT instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

The RS 232C accompanying signals are updated each time the instruction is called (cyclic polling). The CP 34x updates the I/O status at intervals of 20 ms. The inputs/outputs are constantly updated independently of this.

The binary result BR is not affected. The instruction does not output an error message.

Parameter LADDR is used to select the CP 34x be addressed.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LADDR | INPUT | INT | Start address of CP 34x  The start address is taken from STEP 7. |
| DTR_OUT | OUTPUT | BOOL | **D**ata **t**erminal **r**eady,  CP 34x ready  (CP 34x output) |
| DSR_IN | OUTPUT | BOOL | **D**ata **s**et **r**eady,  Communication partner ready  (CP 34x input) |
| RTS_OUT | OUTPUT | BOOL | **R**equest **t**o **s**end,  CP 34x ready to send  (CP 34x output) |
| CTS_IN | OUTPUT | BOOL | **C**lear **t**o **s**end,  Communication partner can receive data from CP 34x (response to RTS = ON of CP 34x)  (CP 34x input) |
| DCD_IN | OUTPUT | BOOL | **D**ata **C**arrier **d**etect,  Receive signal level  (CP 34x input) |
| RI_IN | OUTPUT | BOOL | **R**ing **I**ndicator,  Ring indicator  (CP 34x input) |

### Allocation in the data area

The V24_STAT_340 / V24_STAT instruction does not occupy any data areas.

### Rule

> **Note**
>
> A minimum pulse duration is necessary to detect a signal change. The CPU cycle time, the update time on CP 34x and the response time of the communication partner are decisive variables.

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

## V24_SET_340 / V24_SET: Writing accompanying signals to the RS232C interface (S7-300, S7-400)

### Description

You can set or reset the interface outputs via the parameter inputs of instruction V24_SET_340 (CP 340) / V24_SET (CP 341). The V24_SET_340 / V24_SET instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

The binary result BR is not affected. The instruction does not output an error message.

Parameter LADDR is used to select the CP 34x be addressed.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LADDR | INPUT | INT | Start address of CP 34x  The start address is taken from STEP 7. |
| RTS | INPUT | BOOL | **R**equest **t**o **s**end,  CP 34x ready to send  (Control CP 34x output) |
| DTR | INPUT | BOOL | **D**ata **t**erminal **r**eady,  CP 34x ready  (Control CP 34x output) |

### Allocation in the data area

The V24_SET_340 / V24_SET instruction does not occupy any data areas.

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

## STATUS parameter (S7-300, S7-400)

### Event classes

| Event class | Meaning |
| --- | --- |
| 0 | CP startup |
| 1 | CP hardware fault |
| 2 | Error initializing |
| 3 | Incorrect parameter assignment for the instruction |
| 4 | The CP detected errors in CP - CPU data traffic |
| 5 | Error executing a CPU job |
| 6 | Error executing a partner job (for RK 512 only) |
| 7 | Send errors |
| 8 | Receive errors |
| 9 | Received response message frame with error or error message frame from the interconnection partner |
| 10 (0A<sub>H</sub>) | The CP detected errors in the response message frame of the partner |
| 30 (1E<sub>H</sub>) | Errors in communication between the CP and CPU |

### STATUS parameter

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0003 | PtP parameters applied | - |
| 0004 | Parameter already on CP (timers match) | - |
| 0007 | CPU status transition to STOP | - |
| 0008 | CPU status transition to RUN/STARTUP | - |
| 0101 | Fault while testing operating system EPROM of CP | CP defective; replace CP. |
| 0102 | RAM test of CP errored |  |
| 0103 | Request interface of CP defective |  |
| 0110 | Fault in CP firmware | Switch module off and on again. If necessary, replace module. |
| 020F | Invalid parameter assignment detected at start of parameter communication. Interface could not be parametered. | Correct invalid parameters and restart. |
| 0301 | Invalid source/destination data type or area does not exist (start address, length)  Invalid or no DB (e.g. DB 0) or  Other data type invalid or missing  Interprocessor communication byte number invalid or  Invalid interprocessor communication flag bit number or 'S' or 'F' was not selected (for the P_SND_RK instruction) | Check parameter assignment on CPU and CP and correct if necessary. **RK 512 only:** Partner returns invalid parameters in frame header.  Check parameters on CPU and CP; possibly create block.  See request tables for valid data types.   **RK 512 only:** Partner provides incorrect parameters in the message frame header. |
| 0403 | Incorrect, unknown or illegal data type | Check the program, for example to find incorrect parameter assignments in the instruction. |
| 0407 | An error has occurred during data transmission between the CPU and CP | If the error message persists, check the parameter assignment of the instructions called in the user program.  If the error is signaled immediately after POWER ON, a connection to the CPU is not set up at this time. With the 3964(R) procedure and the ASCII driver, the data transmission of the receiving CP 341 is repeated until the data are transferred to the CPU. With RK 512, the request is acknowledged negatively and must be repeated in the user program.   If the message occurs sporadically during active data transmission, the CPU can not accept the data at times. With the 3964(R) procedure and the ASCII driver, the data transmission of the receiving CP 341 is repeated until the data are transferred to the CPU. With RK 512, the request is acknowledged negatively and must be repeated in the user program. To correct or avoid errors, you should increase the call rate for the P_RCV_RK instruction in the user program. |
| 0408 | Error during data transmission between the CPU and the CP (receipt) |  |
| - CPU is temporarily overloaded, request is repeated | - Reduce the number of communication calls |  |
| - The data area of the CPU cannot be accessed for the time being, e.g., because the receive block is not called often enough. | - Increase the call rate for the receive block |  |
| - The data area of the CPU cannot be accessed for the time being, e.g., because the receive block is disabled in the interim (EN=false). | - Check if the receive block has been disabled too long |  |
| 0409 | Data reception is not possible. Error during data transmission between the CPU and the CP (receipt). Data reception is not possible. After multiple attempts, the request was cancelled after 10 s, because |  |
| - The receive block is not called. | - Check your user program to determine whether the receive block is being executed. |  |
| - The receive block is disabled. | - Check if the receive block is disabled. |  |
| - The data area of the CPU cannot be accessed. | - Check if the data area to which the data is to be transferred is available. |  |
| - Insufficient length of the data area on the CPU. | - Check the length of the data area |  |
| 040A | An error has occurred during data transmission between the CPU and the CP. The data transmission was canceled due to a RESET, because:  - Destination DB is not available - Destination DB is too short - RESET bit set at the instruction | Create destination DB in the user program or increase the length of the existing destination DB. |
| 0501 | Current request aborted as a result of CP restart. | No help available during POWER ON. When changing the parameters of the CP in the programming device, before writing an interface you should ensure there are no more requests running from the CPU. |
| 0502 | Job not permitted in this CP operating mode (e.g., device interface not parameterized) | Set the parameters for the device interface. |
| 0505 | **Only for printer drivers:**   System data block with message texts not available on the CP | Use the parameter assignment software to configure the message texts and then carry out a warm restart. |
| 0506 | **Only for printer drivers:**   Message text not available | Use the parameter assignment software to configure the message texts and then carry out a warm restart. |
| 0507 | **Only for printer drivers:**   Message text too long | Edit the message text to reduce it to a length of fewer than 150 characters (or no more than 250 characters if it contains variables). |
| 0508 | **Only for printer drivers:**   Too many conversion instructions | You have configured more conversion instructions than variables. Conversion instructions without associated variables will be ignored. |
| 0509 | **Only for printer drivers:**   Too many variables | You have configured more variables than conversion instructions. Variables without associated conversion instructions will not be output. |
| 050A | **Only for printer drivers:**   Unknown conversion instruction | Check the conversion instruction. Undefined or unsupported conversion instructions are replaced in the printout with ******. |
| 050B | **Only for printer drivers:**   Unknown control instruction | Check the control instruction. Undefined or unsupported control instructions will be ignored. The control instruction will not be output as text either. |
| 050C | **Only for printer drivers:**   Conversion instruction not executable | Check the conversion instruction. Conversion instructions that cannot be executed are output in the printout in accordance with the defined width and the valid remainder of the conversion instruction or the default display with * characters. |
| 050D | **Only for printer drivers:**   Width in conversion instruction too small or too great | Correct the specified width of the variable in the conversion instruction on the basis of the variable's maximum possible number of characters in text-based display types (A, C, D, S, T, Y, Z). Only as many characters as will fit in the specified width appear in the printout; the text is truncated to this width. In all other cases, * characters are output corresponding to the width. |
| 050E | **Only for ASCII drivers:**   An error occurred while sending. The defined end-of-text characters did not occur within the maximum allowed length or in the case of automatic appending, the maximum allowed transmission length was exceeded. | Extend the end-of-text characters in the transmission buffer at the desired point or select a shorter frame length for automatic appending. |
| 0514 | Specified start addresses too high for desired data type or start address or DB/DX number too low. | Refer to the request tables for the permissible start addresses and DB/DX numbers that can be specified in the program. |
| 0515 | **RK 512 only:**  Incorrect bit number specified in the interprocessor communication flag. | Permissible bit numbers: 0 to 7 |
| 0516 | **RK 512 only:**  Specified CPU number too high. | Permissible CPU no.: none, 0, 1, 2, 3 or 4 |
| 0517 | Transmission length > 1 kbyte is too long for CP or length is too short for interface parameter. | Split the request up into several shorter requests. |
| 051A | **RK 512 only:**  Error sending a command message frame  An associated procedure number has just been entered in STATUS. | See the solution for the previous error number. |
| 051B | **Only for printer drivers:**   Precision invalid | Correct the specified precision in the conversion instruction. The precision is initialized with a dot prefix to identify and limit the width (example: ".2" to output the decimal point and 2 decimal places). Precision is only relevant to display types A, D, F and R. It is ignored otherwise. |
| 051C | **Only for printer drivers:**   Variable invalid  (variable length incorrect/incorrect type) | Correct the specified variable. The corresponding table indicates the possible data types for each display type. |
| 051E | **Only for printer drivers:**   The "line end sequences" sent with this job (i.e.: $R / $L / $N) do not fit (any longer) on the (initial) page. | Increase the length of your page, reduce the number of lines (or line feeds) or spread your printout over a number of pages. |
| 0601 | Error in 1st command byte (not 00 or FFH) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0602 | Error in 3rd command byte (not A, 0 or FFH) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0603 | Error in 3rd command byte in the case of continuation frames (command not as for 1st frame) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0604 | Error in 4th command byte (command letter incorrect) | Header layout error at partner or a command combination has been requested that is not permitted at the CP. Check the permissible commands. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0605 | Error in 4th command byte in the case of continuation frames (command not as for 1st frame) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0606 | Error in 5th command byte (DB number not permissible) | Refer to the request tables for the permissible DB numbers, start addresses or lengths. |
| 0607 | Error in the 5th or 6th command byte (start address too high) | Refer to the request tables for the permissible DB numbers, start addresses or lengths. |
| 0608 | Error in the 7th or 8th command byte (impermissible length) | Obtain from the request tables the permissible DB/DX numbers, start addresses or lengths. |
| 0609 | Error in the 9th and 10th command bytes (illegal coordination flag for this data type or bit number too high). | Header layout error at partner. Find out from the request tables when a coordination flag is permitted. |
| 060A | Error in the 10th command byte (illegal CPU number) | Header layout error at partner. |
| 060B | SEND message frame was longer/shorter than expected (more/less data received than announced in message frame header). | Correction required at the partner |
| 060C | FETCH command message frame with user data received. | Correction required at the partner |
| 060D | The CP received a message frame during an invalid operating mode: |  |
| - Receive connection between the CPU and CP is not set up or not yet correctly set up | - Check the parameter assignment of the addressed connection |  |
| - CP startup is not yet completed | - This error message can occur only during CP startup. Repeat the request. |  |
| - The receiving CPU is in STOP mode | - Place the CPU back in RUN mode and repeat the request. |  |
| - Parameters for the interface are currently being assigned | - This is a temporary error. Repeat the request. |  |
| 060E | Synchronous fault of partner  - New (continuation) command message frame received before response message frame was sent. - First command frame expected and continuation frame came. - Continuation command expected and 1st frame came. | This error may be reported after your own automation system is restarted in the case of long message frames or when the partner is restarted. These cases represent normal system startup behavior.  The error can also occur during operation as a consequence of error statuses only recognized by the partner.  Otherwise, you must assume an error on the part of the partner device. The error may not occur in the case of commands < 128 bytes. |
| 060F | DB locked by coordination function | In local program: Reset the interprocessor communication flag after the last transmission data was processed.  In partner program: Repeat the request |
| 0610 | Message frame received too short (length < 4 bytes in the case of continuation or response message frames or <10 bytes in the case of command message frames) | You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0611 | Frame length and length specified in telegram header are not the same. | You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0612 | Error while sending the (continuation) response message frame. An associated procedure error number has been entered in STATUS immediately beforehand. | See solution for the error number entered immediately beforehand in STATUS. |
| 0701 | Sending of the first repetition:  - An error was detected when transmitting the frame or - The partner requested a repetition by means of a negative acknowledgment character (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame still has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0702 | **Only for 3964(R):**   Error establishing connection:  After STX was sent, NAK or any other code (except for DLE or STX) was received. | Check for malfunction of the partner device, possibly by using interface test device interconnected in the data link. |
| 0703 | **Only for 3964(R):**   Acknowledgment delay time (QVZ) exceeded:   After STX was sent, partner did not respond within the acknowledgment delay time. | The partner device is too slow or not ready to receive or there is a break in the transmission line, for example. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0704 | **Only for 3964(R):**   Termination by partner:  One or more codes were received from the partner during sending. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. If necessary, use an interface test device switched into the transmission line to check. |
| 0706 | **Only for 3964(R):**   End-of-connection error:  - Partner rejected frame at end of connection with NAK or a random string (except for DLE) or - Acknowledgment characters (DLE) received too early. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. If necessary, use an interface test device switched into the transmission line to check. |
| 0707 | **Only for 3964(R):**   Acknowledgment delay time exceeded at end of connection or response monitoring time exceeded after a send frame:  After connection termination with DLE ETX, no response received from partner within acknowledgment delay time. | Partner device too slow or faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0708 | **ASCII driver and printer driver only:**   The wait time for XON or CTS = ON has expired. | The communication partner has a fault, is too slow or is offline. Check the communication partner or change the parameters, if necessary. |
| 0709 | Connection attempt not possible. Number of permitted connection attempts exceeded. | Check the interface cable or the transmission parameters.  Also check that receive function between CPU and CP is correctly configured at the partner device. |
| 070A | The data could not be transmitted. The permitted number of transfer attempts was exceeded. | Check the interface cable or the transmission parameters. |
| 0801 | Expectation of the first repetition:  An error was detected on receiving a message frame and the CP requested repetition from the partner via a negative acknowledgment (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame still has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0802 | **Only for 3964(R):**   Error establishing connection:  - In idle mode, one or more random codes (other than NAK or STX) were received or - After an STX was received, the partner sent more characters without waiting for the response DLE.   After partner power ON:  - While partner is being switched on, the CP receives an undefined character. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0805 | **Only for 3964(R):**   Logical error while receiving:  After DLE was received, a further random character (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the frame header and data string or the connection is terminated with DLE ETX. Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0806 | Character delay time (ZVZ) exceeded:  - Two successive characters were not received within character delay time or   Only for 3964(R):  - First character after sending of DLE during connection setup was not received within character delay time. | Partner device too slow or faulty. Interconnect an interface tester in the transmission line to see if this is the case. |
| 0808 | **Only for 3964(R):**   Error in block check character (BCC):  The value of BCC calculated internally does not match the BCC received by the partner when the connection was terminated. | Check if the connection is seriously disrupted; in this case you may also occasionally see error codes. Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 080A | There is no free receive buffer available:  No receive buffer space available for receiving data. | Increase the call rate for the P_RCV_RK instruction. |
| 080C | Transmission error:  - A transmission error (parity error, stop bit error, overflow error) was detected.    **Only for 3964(R):**   - If a corrupted character is received in idle mode, the error is reported immediately so that disturbances on the transmission line can be detected early.    **Only in the case of RK 512 and 3964(R):**   - If this happens during send or receive operations, repetition is started. | Disturbances on the data link cause frame repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring.  Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits. |
| 080D | BREAK:  Break in receive line to partner. | Reconnect or switch on partner. |
| 0815 | Discrepancy between settings for transmission attempts of the CP and the communication partner. | Set the same number of transfer attempts at communications partner as at CP. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0816 | The length of a received message frame exceeded the maximum specified length. | Correction required at the partner |
| 0818 | **For ASCII driver only:**   DSR = OFF or CTS = OFF | The partner has switched the DSR or CTS signal to "OFF" before or during a transmission.  Check the partner's control of the RS 232C accompanying signals. |
| 0902 | **Only with RK 512:**   Memory access error in partner (memory does not exist)   **With SIMATIC S5 as partner:**   - Incorrect area at status word or - Data area does not exist (except DB/DX) or - Data area too short (except DB/DX) | Check that the partner has the desired data area and that it is big enough or check the parameters of the called system function block.  Check the specified length at the system function block. |
| 0903 | **Only with RK 512:**   DB/DX access error in the partner (DB/DX does not exist or is too short)   **With SIMATIC S5 as partner:**   - DB/DX does not exist or - DB/DX too short or - DB/DX number impermissible   Permissible source area exceeded with FETCH request | Check that the partner has the desired data area and that it is big enough or check the parameters of the called system function block.  Check the specified length at the system function block. |
| 0904 | **Only with RK 512:**   Partner reports "Illegal request type". | Partner malfunction, because the CP never outputs a system command. |
| 0905 | **Only with RK 512:** Error at the partner or SIMATIC S5 as partner:  - Source/destination type not permissible or - Memory error in partner programmable controller or - Error notifying CP/CPU at the partner or - Partner programmable controller is in STOP mode | Check if the partner can transmit the desired data type.  Check the structure of the hardware at the partner.  Set the mode selector switch of the partner programmable controller to RUN. |
| 0908 | **Only with RK 512:**   Partner detects synchronous error:  Frame sequence error. | This error occurs at restart of your own programmable controller or of the partner. This represents normal system startup behavior. You do not need to correct anything. The error is also conceivable during operation as a consequence of previous errors. Otherwise, you can assume an error on the part of the partner device. |
| 0909 | **Only with RK 512:**   DB/DX locked at the partner by coordination flag | In partner program: Reset the coordination memory after the last transmission data was processed!   In own program: Repeat the request. |
| 090A | **Only with RK 512:**   Errors in message frame header that are detected by the partner: Third command byte in the header is incorrect | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090B | **Only with RK 512:**   Error in message frame header: 1st or 4th command byte in header is incorrect | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090C | **Only with RK 512:**   Partner detects incorrect message frame length (total length). | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090D | **Only with RK 512:**   Partner was not yet restarted. | Restart the partner programmable controller or set the mode selector switch on the CP to RUN. |
| 090E | **Only with RK 512:**   Unknown error number received in the response message frame. | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 0A01 | **Only with RK 512:**   Synchronization error of partner, because:  - Response frame without request - Response frame received before continuation frame sent - Continuation response message frame received after an initial message frame was sent - A first response frame was received after a continuation frame was sent | This error is reported after your own programming device is restarted in the case of long frames or when the partner is restarted. This represents normal system startup behavior. You do not have to correct anything.  The error can also occur during operation as a consequence of error statuses only recognized by the partner.  Otherwise, you can assume an error on the part of the partner device. The error may not occur in the case of commands < 128 bytes. |
| 0A02 | RK 512 only: Error in the structure of the received response message frame (1st byte not 00 or FF) | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A03 | RK 512 only: Received response message frame has too many or too few data. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A04 | RK 512 only: Response message frame for SEND request arrived with data. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A05 | RK 512 only: No response message frame received from partner within monitoring time. | Is the partner a slow device? This error is also often displayed as a consequence of a previous error. For example, procedure receive errors (event class 8) can be displayed after a FETCH message frame was sent. Reason: As a result of disturbances, the response frame could not be received, and the monitoring time elapsed. This error also possibly occurs if the partner is restarted before it could respond to the last received FETCH frame. |
| 1E0D | Job aborted due to warm restart, hot restart or reset |  |
| 1E0E | Static error when calling RD_REC SFC. Return value RET_VAL of SFC is available for evaluation in SFCERR variable in instance DB. | Load SFCERR variable from instance DB. |
| 1E0F | Static error when calling WR_REC SFC. Return value RET_VAL of SFC is available for evaluation in SFCERR variable in instance DB. | Load SFCERR variable from instance DB. |
| 1E41 | Invalid number of bytes specified at instruction parameter LEN | You must stay within a range of values of 1 to 4096 bytes. |
| 1E42 | P_PRINT_RK instruction:  The number of bytes specified for the variable or format string in the pointer DB under length is not permissible. | You must specify a permissible length: 32 bytes for variables, 150 bytes for format strings. |
| 1E43 | P_PRINT_RK instruction: No pointer available for format string. | Enter the data block no. and data word no. for the format string in the pointer DB. |

> **Note**
>
> An error message is only output if the ERROR bit (job canceled with error) is also set. In all other cases, the STATUS word is zero.

### Calling the SFCERR or SFCSTATUS variable

You can call the SFCERR or SFCSTATUS variable to obtain more detailed information about the pending event class 30 error, 14 (1E0EH) or 15 (1E0FH).

You can load the SFCERR or SFCSTATUS variable only by means of symbolic access to instance DB of the corresponding instruction.

Error messages entered in the SFCERR variable can be found in the system functions SFC 58 under "WR_REC: Write data record to I/O" and SFC 59 under "RD_REC: Read data record from I/O".

Error messages entered in the SFCSTATUS variable can be found in the system functions SFB 52 under "RDREC: Read data record" and SFB 53 under "WRREC: Write data record".

---

**See also**

[WR_REC: Write data record to I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400)
  
[RD_REC: Read data record from I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)
  
[RDREC: Read data record](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdrec-read-data-record-s7-300-s7-400)
  
[WRREC: Write data record](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wrrec-write-data-record-s7-300-s7-400)

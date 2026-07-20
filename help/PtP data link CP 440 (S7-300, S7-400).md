---
title: "PtP data link CP 440 (S7-300, S7-400)"
package: ProgFBCP440enUS
topics: 5
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PtP data link CP 440 (S7-300, S7-400)

This section contains information on the following topics:

- [SEND_440: Sending Data (S7-300, S7-400)](#send_440-sending-data-s7-300-s7-400)
- [RECV_440: receiving data (S7-300, S7-400)](#recv_440-receiving-data-s7-300-s7-400)
- [RES_RECV: Delete receive buffer (S7-300, S7-400)](#res_recv-delete-receive-buffer-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

## SEND_440: Sending Data (S7-300, S7-400)

### Description

The SEND_440 instruction transmits a data block from a DB to the CP 440 as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the SEND_440 instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

Data transmission is initiated by a positive edge at the input REQ. Data transmission can take several calls (program cycles), depending on the data volume.

The SEND_440 instruction can be called in the cycle by setting signal state "1" at parameter input R. This setting cancels the transmission to CP 440 and resets the SEND_440 instruction to the initial state. Data that has already been received by CP 440 is still sent to the communication partner. A static signal state "1" at the input R indicates that data transmission is disabled.

Parameter LADDR specifies the address of the CP 440 to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for a RESET of the SEND_440 instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of CP 440  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Send DB no.:   CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8190 Transmitted data as of data byte;   Offset is CPU-specific |
| LEN | INPUT | INT | Data length  1 ≤ LEN ≤ 400, specified in number of bytes |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The SEND_440 instruction works in combination with an I_SEND_440 instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR variable for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/16936395019_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

### Rules

> **Note**
>
> The SEND_440 instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

## RECV_440: receiving data (S7-300, S7-400)

### Description

The RECV_440 instruction transfers data from the CP 440 to an S7 data area as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the RECV_440 instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program. .

### Operating principle

The (static) signal state "1" at parameter EN_R enables the check for data to be read from CP 440. An active transmission can be canceled by setting signal state "0" at parameter EN_R. The canceled receive request is terminated with an error message (STATUS output). Receiving is disabled as long as signal state "0" is set at parameter EN_R. Data transmission can take several calls (program cycles), depending on the data volume.

If the instruction detects signal state "1" at the R parameter, the current transmission job is canceled and the RECV_440 instruction is reset to the initial state. Receiving is disabled as long as signal state "1" is set at parameter R.

Parameter LADDR is used to select the CP 440 to be addressed.

Output NDR indicates "Job completed without errors/data received" (all data read) and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, STATUS has a value 0. NDR and ERROR/STATUS are also output for the RESET of the RECV_440 instruction (parameter LEN == 16#00). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enable data reading |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Receiving is disabled. |
| LADDR | INPUT | INT | Start address of CP 440  The basic address can be found in the configuration table in STEP 7. |
| DB_NO | INPUT | INT | Data block number  Receive data block no.:  CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number  Offset is CPU-specific |
| NDR<sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN<sup>1</sup> | OUTPUT | INT | Length of the message frame received  1 ≤ LEN ≤ 400, specified in number of bytes |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The RECV_440 instruction works in combination with an I_RECV_440 instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0E occurs, you can examine the SFCERR variable for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the input circuit of EN_R and R.

![Time sequence chart](images/16936429323_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

### Rule

> **Note**
>
> The RECV_440 instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

## RES_RECV: Delete receive buffer (S7-300, S7-400)

### Description

The RES_RECV instruction clears the entire input buffer of CP 440. All message frames in memory are discarded. A message frame received at the time the RES_RECV instruction is called is saved.

### Operating principle

A positive edge at the input REQ enables the instruction. The job can run over several calls (program cycles).

The RES_RECV instruction can be called in the cycle by setting signal state "1" at parameter input R. This action cancels the delete operation and resets the RES_RECV instruction to the initial state.

Parameter LADDR specifies the address of the CP 440 to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, STATUS has a value 0. DONE and ERROR/STATUS are also output for RESET of the RES_RECV instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of CP 440  The start address is taken from STEP 7. |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The RES_RECV instruction works in combination with an I_RES_RECV instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR variable for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/21663484939_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

### Rule

> **Note**
>
> The RES_RECV instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

## STATUS parameter (S7-300, S7-400)

### Event classes

| Event class | Meaning |
| --- | --- |
| 0 (0<sub>H</sub>) | CP startup |
| 2 (02<sub>H</sub>) | Error initializing |
| 5 (05<sub>H</sub>) | Error executing a CPU job |
| 7 (07<sub>H</sub>) | Send errors |
| 8 (08<sub>H</sub>) | Receive errors |
| 11 (0B<sub>H</sub>) | Warnings |
| 30 (1E<sub>H</sub>) | Errors in communication between the CP and CPU |
| 128 (80<sub>H</sub>) | Module fault |

### STATUS parameter

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0001 | Initialization of the CP completed | - |
| 0003 | PtP parameters applied | - |
| 0004 | Parameter already on CP (timers match) | - |
| 0007 | CPU status transition to STOP | - |
| 0008 | CPU status transition to RUN/STARTUP | - |
| 0201 | No parameters  Parameter memory empty or has unknown contents | Load interface parameters. |
| 0204 | Impermissible character frame | Correct the impermissible parameter assignment, load the parameters onto the module and carry out a cold restart. |
| 0205 | Impermissible transmission rate | Correct the impermissible parameter assignment, load the parameters onto the module and carry out a cold restart. |
| 020F | Invalid parameter assignment detected at start of parameter communication. Interface could not be parametered. | Correct invalid parameters and restart. |
| 0212 | Impermissible  - Monitoring time - Character Delay Time   Only for 3964(R):  - Acknowledgment delay | Correct the impermissible parameter assignment, load the parameters onto the module and carry out a cold restart. |
| 0501 | Current request aborted as a result of CP restart. | No help available during POWER ON. When changing the parameters of the CP in the programming device, before writing an interface you should ensure there are no more requests running from the CPU. |
| 0502 | Job not permitted in this CP operating mode (e.g., device interface not parameterized) | Set the parameters for the device interface. |
| 050E | - Invalid frame length or | - Frame length is > 400 bytes. Reduce the message frame length  or |
| - The configured end-of-text characters did not occur within the maximum permissible length. | - Add the end-of-text characters at the place you want in the send buffer. |  |
| 0517 | Transmission length > 400 bytes exceeds CP capacity. | Split the job up into several shorter jobs. |
| 051D | Send/receive job interrupted by:  - Communication block reset - Parameter reassignment | Repeat the call for the communication block. |
| 0522 | A new SEND job has been started, although the old job has not yet been completed. | Only start the new SEND job when the old job has been completed with DONE or ERROR. |
| 0701 | Only for 3964(R):  Sending of the first repetition:  - An error was detected when transmitting the frame or - The partner requested a repetition by means of a negative acknowledgment character (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0702 | Only for 3964(R):  Error establishing connection:  After STX was sent, NAK or any other code (except for DLE or STX) was received. | Check for malfunctioning of the partner device, possibly using an interface test device switched into the transmission line. |
| 0703 | Only for 3964(R):  Acknowledgment delay time (QVZ) exceeded:   After STX was sent, partner did not respond within the acknowledgment delay time. | The partner device is too slow or not ready to receive or there is a break on the send line, for example. Identify the malfunctioning of the partner device, possibly by using an interface test device switched into the transmission line. |
| 0704 | Only for 3964(R):  Termination by partner:  One or more codes were received from the partner during sending. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester in the transmission line to check the status. |
| 0705 | Only for 3964(R):  Negative acknowledgment when sending | Check if the partner also indicates an error; possibly it has not received all of the transmitted data (for example, due to an interrupted data link) or because fatal errors are pending or the characteristics of the partner device is faulty. You can interconnect an interface tester in the transmission line to check the status. |
| 0706 | Only for 3964(R):  End-of-connection error:  - Partner rejected frame at end of connection with NAK or a random string (except for DLE) or - Acknowledgment characters (DLE) received too early. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester in the transmission line to check the status. |
| 0707 | Only for 3964(R):  Acknowledgment delay time exceeded at end of connection or response monitoring time exceeded after a send frame:  After connection termination with DLE ETX, no response received from partner within acknowledgment delay time. | Partner device faulty or too slow. You can interconnect an interface tester in the transmission line to check the status. |
| 0708 | For ASCII driver only:  The wait time for XON or CTS = ON has expired. | The communication partner has a fault, is too slow or is offline. Check the communication partner or change the parameters, if necessary. |
| 0709 | Only for 3964(R):  Connection attempt not possible. Number of permitted connection attempts exceeded. | Check the interface cable or the transmission parameters.  Also check that receive function between CPU and CP is correctly configured at the partner device. |
| 070A | Only for 3964(R):  The data could not be transmitted. The permitted number of transfer attempts was exceeded. | Check the interface cable or the transmission parameters. |
| 070B | Only for 3964(R):  Initialization conflict cannot be resolved because both partners have high priority. | Change the parameter assignment. |
| 070C | Only for 3964(R):  Initialization conflict cannot be resolved because both partners have low priority. | Change the parameter assignment. |
| 0801 | Only for 3964(R):  Expectation of the first repetition:  An error was detected on receiving a frame and the CP requested repetition from the partner via a negative acknowledgment (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0802 | Only for 3964(R):  Error establishing connection:  - In idle mode, one or more random codes (other than NAK or STX) were received or - After an STX was received, the partner sent more characters without waiting for the response DLE.   After partner power ON:  - While partner is being switched on, the CP receives an undefined character. | You can interconnect an interface tester in the transmission line to check the error response of the partner device. |
| 0805 | Only for 3964(R):  Logical error while receiving:  After DLE was received, a further random character (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the frame header and data string or the connection is terminated with DLE ETX. You can interconnect an interface tester in the transmission line to check the error response of the partner device. |
| 0806 | Character delay time (ZVZ) exceeded:  - Two successive characters were not received within character delay time or   Only for 3964(R):  - First character after sending of DLE during connection setup was not received within character delay time. | Partner device faulty or too slow. You can interconnect an interface tester in the transmission line to check the status. |
| 0807 | Illegal frame length:  A zero-length frame has been received. | Receipt of a zero-length frame is not an error.  Check why the communication partner is sending message frames without user data. |
| 0808 | Only for 3964(R):  Error in block check character (BCC):  The value of BCC calculated internally does not match the BCC received by the partner when the connection was terminated. | Check if the connection is seriously disrupted; in this case you may also occasionally see error codes. You can interconnect an interface tester in the transmission line to check the error response of the partner device. |
| 0809 | Only for 3964(R):  Waiting time for block repetition has expired | Declare a block waiting time at the communication partner identical to that of the CP 440. Check for malfunctioning of the communication partner, possibly by using an interface tester interconnected in the data link. |
| 080A | There is no free receive buffer available:  No receive buffer space available for receiving data. | Increase the call rate for the RECV_440 instruction. |
| 080C | Transmission error:  - A transmission error (parity error, stop bit error, overflow error) was detected.   Only for 3964(R):  - If a corrupted character is received in idle mode, the error is reported immediately so that disturbances on the transmission line can be detected early.   Only for 3964(R):  - If this happens during send or receive operations, repetition is started. | Disturbances on the data link cause frame repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring.  Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits. |
| 080D | BREAK:  Break in receive line to partner. | Reconnect or switch on partner. |
| 080E | Receive buffer overflow when flow control not enabled. | Increase the call rate for the receive instruction in the user program or configure the parameters for communication with flow control. |
| 0810 | Parity error | Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits. |
| 0811 | Character frame error | Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0812 | For ASCII driver only:  More characters were received after the CP had sent XOFF or set CTS to OFF. | Reassign the parameters for the communication partner or deal with the data in the CP more quickly. |
| 0814 | For ASCII driver only:  A message frame or several message frames have got lost, because you have been working without flow control. | Work with flow control as much as you can. Use the entire receive buffer. Set the "Reaction to CPU Stop" parameter in the basic parameters to "Continue". |
| 0816 | The length of a received message frame was longer than the maximum specified length. | Correction required at the partner |
| 0820 | Static error when calling RD_REC SFC. Return value RET_VAL of SFC is available for evaluation in SFCERR variable in instance DB. | Analyze the SFCERR variable from the instance DB. |
| 0B01 | Receive buffer more than 2/3 full | Call the receive block more often to avoid the receive buffer overflowing. |
| 8000 | Module firmware not found | Perform a firmware update |
| 1E0D | - Job canceled due to a cold restart, warm restart, reset or | - Repeat the request. |
| - Module firmware does not exist | - Check if the module is inserted. |  |
| 1E0E | Static error when calling RD_REC SFC. Return value RET_VAL of SFC is available for evaluation in SFCERR variable in instance DB. | Load SFCERR variable from instance DB. |
| 1E0F | Static error when calling WR_REC SFC. Return value RET_VAL of SFC is available for evaluation in SFCERR variable in instance DB. | Load SFCERR variable from instance DB. |
| 1E41 | Invalid number of bytes specified at instruction parameter LEN. | Keep to the value range 1 to 400 bytes. |

> **Note**
>
> An error message is only output if the ERROR bit (job canceled with error) is also set. In all other cases, the STATUS word is zero.

### Calling the SFCERR Variable

You can obtain more information on errors 14 (1E0EH) and 15 (1E0FH) in event class 30 by means of the SFCERR variable.

You can load the SFCERR variable from the instance DB of the corresponding instruction.

Error messages entered in the SFCERR variable can be found in the system functions SFC 58 under "WR_REC: Write data record to I/O" and SFC 59 under "RD_REC: Read data record from I/O".

---

**See also**

[WR_REC: Write data record to I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400)
  
[RD_REC: Read data record from I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)

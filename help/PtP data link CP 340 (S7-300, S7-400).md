---
title: "PtP data link CP 340 (S7-300, S7-400)"
package: ProgFBCP340enUS
topics: 8
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PtP data link CP 340 (S7-300, S7-400)

This section contains information on the following topics:

- [P_SEND: Sending Data (S7-300, S7-400)](#p_send-sending-data-s7-300-s7-400)
- [P_RCV: receiving data (S7-300, S7-400)](#p_rcv-receiving-data-s7-300-s7-400)
- [P_PRINT: Print message text with up to 4 variables (S7-300, S7-400)](#p_print-print-message-text-with-up-to-4-variables-s7-300-s7-400)
- [P_RESET: Delete receive buffer (S7-300, S7-400)](#p_reset-delete-receive-buffer-s7-300-s7-400)
- [V24_STAT_340 / V24_STAT: Reading accompanying signals from the RS232C interface (S7-300, S7-400)](#v24_stat_340-v24_stat-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400)
- [V24_SET_340 / V24_SET: Writing accompanying signals to the RS232C interface (S7-300, S7-400)](#v24_set_340-v24_set-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

## P_SEND: Sending Data (S7-300, S7-400)

### Description

The P_SEND instruction transfers data blocks from a DB to CP 340 as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the P_SEND instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

Data transmission is initiated by a positive edge at the input REQ. Data transmission can take several calls (program cycles), depending on the data volume.

The P_SEND instruction can be called in the cycle by setting signal state "1" at the R parameter input. This setting cancels the transmission to CP 340 and resets the P_SEND instruction to the initial state. Data that has already been received by CP 340 is still sent to the communication partner. A static signal state "1" at the input R indicates that data transmission is disabled.

Parameter LADDR specifies the address of the CP 340 to be addressed.

Output DONE indicates "Job completed without errors". ERROR indicates error events. A corresponding event number is displayed in [STATUS parameter](#status-parameter-s7-300-s7-400) if an error occurs. If no error occurs, STATUS has a value 0. DONE and ERROR/STATUS are also output for RESET of the P_SEND instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of CP 340  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Send DB no.:   CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8190 send data, starting from data byte |
| LEN | INPUT | INT | Data length  1 ≤ LEN ≤ 1024, specified in number of bytes |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors   [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The P_SEND instruction works in combination with an I_SEND instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR or SFCSTATUS variable for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ and R.

![Time sequence chart](images/16935481995_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

### Rules

> **Note**
>
> The P_SEND instruction has no parameter check. If incorrect parameters are assigned, the CPU can change to STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_SEND instruction must be completed before the CP 340 can execute a job triggered after the CPU changed from STOP to RUN . A job initiated in the meantime is not lost. Once the startup coordination is completed, the job is sent to the CP 340 .

## P_RCV: receiving data (S7-300, S7-400)

### Description

The P_RCV instruction transfers data from the CP 340 to an S7 data area as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the P_RCV instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

The (static) signal state "1" at parameter EN_R enables the check for data to be read from CP 340. An active transmission can be canceled by setting signal state "0" at parameter EN_R. (Because transmission may sometimes not start up again after setting parameter EN_R to "1", you should set parameter R to "1" in addition to setting EN_R to "0" to cancel an active transmission.) The canceled receive request is terminated with an error message (STATUS output). Receiving is disabled as long as signal state "0" is set at parameter EN_R. Data transmission can take several calls (program cycles), depending on the data volume.

If the instruction detects signal state "1" at the R parameter, the current transmission job is canceled and the P_RCV instruction is reset to the initial state. Receiving is disabled as long as signal state "1" is set at parameter R. If the signal state returns to "0", the canceled message frame is received again from the beginning.

Parameter LADDR is used to select the CP 340 to be addressed.

Output NDR indicates "Job completed without errors/data received" (all data read) and ERROR indicates error events. [STATUS](#status-parameter-s7-300-s7-400)  indicates the error event numbers. If no error occurs, STATUS has a value 0. NDR and ERROR/STATUS are also output by the RESET of P_RCV (parameter LEN == 16#00). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enable data reading |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Receiving is disabled. |
| LADDR | INPUT | INT | Start address of CP 340  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Receive data block no.:   CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8190 Receive data starting from data byte |
| NDR <sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00; |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN <sup>1</sup> | OUTPUT | INT | Length of the message frame received  1 ≤ LEN ≤ 1024, specified in number of bytes |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The P_RCV instruction works in combination with an I_RCV instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0E occurs, you can examine the SFCERR or SFCSTATUS tag for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the input circuit of EN_R and R.

![Time sequence chart](images/16935531403_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

### Rules

> **Note**
>
> The P_RCV instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_RCV instruction must be completed before the CP 340 can execute a job triggered after the CPU changed from STOP to RUN.

## P_PRINT: Print message text with up to 4 variables (S7-300, S7-400)

### Description

The P_PRINT instruction is available for printing message texts. The P_PRINT instruction transfers a process message to the CP 340, for example. CP 340 logs the process message to the connected printer.

The P_PRINT instruction sends up to four variables to the CP 340. For data transmission, the P_PRINT instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

The DB_NO and DBB_NO parameters enable access to the pointers (to data blocks) for the format string and the four variables. The pointers must be stored without gaps and in a specific sequence in the parameterized data block. This is the pointer DB (see Figure "Pointer DB").

A positive edge at the input REQ initiates the transmission of the message text. The frame starts with the format string of the message text, This is followed by tags 1 to 4.

Data transmission can take several calls (program cycles), depending on the data volume.

The P_PRINT instruction can be called in the cycle by setting signal state "1" at parameter input R. This setting cancels the transmission to CP 340 and resets the P_PRINT instruction to the initial state. Data that has already been received by CP 340 is still sent to the communication partner. A static signal state "1" at the input R indicates that the transmission of print jobs is disabled.

Parameter LADDR specifies the address of the CP 340 to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no error occurs, STATUS has a value 0. DONE and ERROR/STATUS are also output for RESET of the P_PRINT instruction. The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Printing is disabled |
| LADDR | INPUT | INT | Start address of CP 340  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Pointer to pointer DB:   CPU-specific, zero not allowed  (The pointers to variables and format string are stored in the pointer DB in a fixed order (see previous figure).) |
| DBB_NO | INPUT | INT | Data byte number  0 ≤ DBB_NO ≤ 8162 Pointer as of data byte |
| DONE <sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Assignment in the Data Area, Instance DB

The P_PRINT instruction works in combination with an I_PRINT instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> Exception: If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR or SFCSTATUS variable for additional details.

### Assignment in the Data Area, Pointer DB

The P_PRINT instruction uses the DB_NO and DBB_NO parameters to access a pointer DB in which the pointers to the data blocks containing the message texts and variables are stored in a fixed sequence. You have to create the pointer DB.

The figure shows the syntax of the pointer DB that is addressed by means of the DB_NO and DBB_NO parameters of the P_PRINT instruction.

![Assignment in the Data Area, Pointer DB](images/21571800843_DV_resource.Stream@PNG-en-US.png)

### Permissible DB Number

The permissible DB numbers are CPU-specific. If the value 16#00 is specified as the DB number for "Pointer to variable", this variable is interpreted as not present and the pointer is set to the next variable or the format string.

If the DB number is equal to the value 16#00 in "Pointer to format string", the print job is canceled and event ID 16#1E43 is indicated at parameter output STATUS of the P_PRINT instruction.

### Permissible DBB Number

The variable or format string begins at the parameterized DBB number. The variables can have a maximum length of 32 bytes and the format string can have a maximum length of 150 bytes.

If the maximum length is exceeded, the print job is canceled and event ID 16#1E41 is indicated at parameter output STATUS of the P_PRINT instruction.

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
> The P_PRINT instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CP-CPU startup routine of the P_PRINT instruction must be completed before the CP 340 can execute a job triggered after the CPU changed from STOP to RUN. A job initiated in the meantime is not lost. Once the startup coordination is completed, the job is sent to the CP 340.

---

**See also**

[Data transmission with the printer driver (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-with-the-printer-driver-s7-300-s7-400)

## P_RESET: Delete receive buffer (S7-300, S7-400)

### Description

The P_RESET instruction clears the entire input buffer of CP 340. All message frames in memory are discarded. A message frame received at the time the P_RESET instruction is called is saved.

A positive edge at the input REQ enables the instruction. The job can run over several calls (program cycles).

Parameter LADDR specifies the address of the CP 340 to be addressed.

The DONE output indicates "Job completed without errors". ERROR indicates error events. A corresponding event number is displayed in [STATUS parameter](#status-parameter-s7-300-s7-400) if an error occurs. If no errors occurs, STATUS has the value 0. If an error occurs, the binary result BR is reset. If the block is completed without errors, the binary result has the status "1".

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| LADDR | INPUT | INT | Start address of CP 340  The start address is taken from STEP 7. |
| DONE <sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00; |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors   [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information |
| <sup>1 </sup>The parameter is available until the next call of the instruction! |  |  |  |

### Allocation in the data area

The P_RESET instruction works in combination with an I_P_RESET instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> **Exception:** If the error STATUS == W#16#1E0F occurs, you can examine the SFCERR or SFCSTATUS variable for additional details.

### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the input circuit of REQ.

![Time sequence chart](images/17002395915_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

### Rule

> **Note**
>
> The P_RESET instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

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
| 5 | Error executing a CPU job |
| 7 | Send errors |
| 8 | Receive errors |
| 30 (1E<sub>H</sub>) | Errors in communication between the CP and CPU |

### STATUS parameter

| Error code  (W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0502 | Job not permitted in this CP operating mode (e.g., device interface not parameterized) | Evaluate the diagnostic interrupt and rectify the error accordingly. |
| 0505 | **Only for printer drivers:**   System data block with message texts not available on the CP | Use the parameter assignment software to configure the message texts and then carry out a warm restart. |
| 0506 | **Only for printer drivers:**   Message text not available | Use the parameter assignment software to configure the message texts and then carry out a warm restart. |
| 0507 | **Only for printer drivers:**   Message text too long | Edit the message text to reduce it to a length of fewer than 150 characters (or no more than 250 characters if it contains variables). |
| 0508 | **Only for printer drivers:**   Too many conversion instructions | You have configured more conversion instructions than variables. Conversion instructions without associated variables will be ignored. |
| 0509 | **Only for printer drivers:**   Too many variables | You have configured more variables than conversion instructions. Variables without associated conversion instructions will not be output. |
| 050A | **Only for printer drivers:**   Unknown conversion instruction | Check the conversion instruction. Undefined or unsupported conversion instructions are replaced in the printout with ******. |
| 050B | **Only for printer drivers:**   Unknown control instruction | Check the control instruction. Undefined or unsupported control instructions will be ignored. The control instruction will not be output as text either. |
| 050C | **Only for printer drivers:**   Conversion instruction not executable | Check the conversion instruction. Conversion instructions that cannot be executed are output in the printout in accordance with the defined width and the valid remainder of the conversion instruction or the default display with * characters. |
| 050D | **Only for printer drivers:**   Width in conversion instruction too small or too great | Correct the specified width of the variable in the conversion instruction on the basis of the variable's maximum possible number of characters in text-based display types (A, C, D, S, T, Y, Z). Only as many characters as will fit in the specified width appear in the printout; the text is truncated to this width. In all other cases, * characters are output corresponding to the width. |
| 050E | **Only for 3964(R) and ASCII drivers:**   Invalid frame length | Frame length is &gt; 1,024 bytes. The rest of the frame (&gt; 1,024 bytes) is still being received by the CP 340; this means that the first part of the frame is discarded.  Select a shorter frame length. |
| 051B | **Only for printer drivers:**   Precision invalid | Correct the specified precision in the conversion instruction. The precision is initialized with a dot prefix to identify and limit the width (example: ".2" to output the decimal point and 2 decimal places). Precision is only relevant to display types A, D, F and R. It is ignored otherwise. |
| 051C | **Only for printer drivers:**   Variable invalid  (variable length incorrect/incorrect type) | Correct the specified variable. The corresponding table indicates the possible data types for each display type. |
| 051E | **Only for printer drivers:**   The "line end sequences" sent with this job (i.e.: $R / $L / $N) do not fit (any longer) on the (initial) page. | Increase the length of your page, reduce the number of lines (or line feeds) or spread your printout over a number of pages. |
| 0701 | **Only for 3964(R):**   Sending of the first repetition:  - An error was detected when transmitting the frame or - The partner requested a repetition by means of a negative acknowledgment character (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0702 | **Only for 3964(R):**   Error establishing connection:  After STX was sent, NAK or any other code (except for DLE or STX) was received. | Check for malfunction of the partner device; you may need to use an interface test device (FOXPG) interconnected in the data link. |
| 0703 | **Only for 3964(R):**   Acknowledgment delay time (QVZ) exceeded:   After STX was sent, partner did not respond within the acknowledgment delay time. | The partner device is too slow or not ready to receive or there is a break in the transmission line, for example. Check for malfunction of the partner device; you may need to use an interface test device (FOXPG) interconnected in the data link. |
| 0704 | **Only for 3964(R):**   Termination by partner:  One or more codes were received from the partner during sending. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to check this state. |
| 0705 | **Only for 3964(R):**   Negative acknowledgment when sending | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to check this state. |
| 0706 | **Only for 3964(R):**   End-of-connection error:  - Partner rejected frame at end of connection with NAK or a random string (except for DLE) or - Acknowledgment characters (DLE) received too early. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to check this state. |
| 0707 | **Only for 3964(R):**   Acknowledgment delay time exceeded at end of connection or response monitoring time exceeded after a send frame:  After connection termination with DLE ETX, no response received from partner within acknowledgment delay time. | Partner device too slow or faulty. You can interconnect an interface tester (FOXPG) in the transmission line to check this state. |
| 0708 | **Only for ASCII drivers and printer drivers:**   The wait time for XON or CTS = ON has expired. | The communication partner has a fault, is too slow or is offline. Check the communication partner or change the parameters, if necessary. |
| 070B | **Only for 3964(R):**   Initialization conflict cannot be resolved because both partners have high priority. | Change the parameter assignment. |
| 070C | **Only for 3964(R):**   Initialization conflict cannot be resolved because both partners have low priority. | Change the parameter assignment. |
| 0801 | **Only for 3964(R):**   Expectation of the first repetition:  An error was detected on receiving a frame and the CP requested repetition from the partner via a negative acknowledgment (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0802 | **Only for 3964(R):**   Error establishing connection:  - In idle mode, one or more random codes (other than NAK or STX) were received or - After an STX was received, the partner sent more characters without waiting for the response DLE.   After partner power ON:  - While partner is being switched on, the CP receives an undefined character. | Check for malfunction of the partner device; you may need to use an interface test device (FOXPG) interconnected in the data link. |
| 0805 | **Only for 3964(R):**   Logical error while receiving:  After DLE was received, a further random character (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the frame header and data string or the connection is terminated with DLE ETX. Check for malfunction of the partner device; you may need to use an interface test device (FOXPG) interconnected in the data link. |
| 0806 | **Character delay time (ZVZ) exceeded:**   - Two successive characters were not received within character delay time or    **Only for 3964(R):**   - First character after sending of DLE during connection setup was not received within character delay time. | Partner device too slow or faulty. Check this using an interface test device (FOXPG) interconnected in the data link. |
| 0807 | **Illegal frame length:**   A zero-length frame has been received. | Receipt of a zero-length frame is not an error.  Check why the communication partner is sending frames without user data. |
| 0808 | **Only for 3964(R):**   Error in block check character (BCC):  The value of BCC calculated internally does not match the BCC received by the partner when the connection was terminated. | Check if the connection is seriously disrupted; in this case you may also occasionally see error codes. Check for malfunction of the partner device; you may need to use an interface test device (FOXPG) interconnected in the data link. |
| 0809 | **Only for 3964(R):**   The number of repetitions must the set to the same value. | Declare a block waiting time at the communication partner identical to that of the CP 340. Check for malfunction of the communication partner; you may need to use an interface test device (FOXPG) that is switched into the transmission line. |
| 080A | There is no free receive buffer available:  No receive buffer space available for receiving data. | Increase the call rate for the P_RCV instruction. |
| 080C | Transmission error:  - A transmission error (parity error, stop bit error, overflow error) was detected.    **Only for 3964(R):**   - If this happens during send or receive operations, repetition is started. - If a corrupted character is received in idle mode, the error is reported immediately so that disturbances on the transmission line can be detected early. - If the SF LED (red) and the RxD LED (green) light up, there is a break in the connecting cable (cable break) between the two communication partners. | Disturbances on the data link cause frame repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring.  Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits. |
| 080D | BREAK:  Break in receive line to partner. | Reconnect or switch on partner. |
| 0810 | **Only for ASCII drivers:**   Parity error:  If the SF LED (red) and the RxD LED (green) light up, there is a break in the connecting cable (cable break) between the two communication partners. | Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0811 | **Only for ASCII drivers:**   Character frame error:  If the SF LED (red) and the RxD LED (green) light up, there is a break in the connecting cable (cable break) between the two communication partners. | Check the connecting cables of the communication partners or verify that both devices have matching settings for baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0812 | **Only for ASCII drivers:**   More characters were received after the CP had sent XOFF or set CTS to OFF. | Reset the parameters for the communication partner or read data from CP more quickly. |
| 0818 | **Only for ASCII drivers:**   DSR = OFF or CTS = OFF | The partner has switched the DSR or CTS signal to "OFF" before or during a transmission.  Check the partner's control of the RS 232C accompanying signals. |
| 1E0D | Job aborted due to warm restart, hot restart or reset |  |
| 1E0E | Static error when calling RD_REC SFC or RDREC SFB. The RET_VAL return value for the SFC/SFB is made available to you for evaluation in the SFCERR or SFCSTATUS variable respectively on the instance DB. | Load the SFCERR or SFCSTATUS variable from the instance DB. |
| 1E0F | Static error when calling WR_REC SFC or RDREC SFB. The RET_VAL return value for the SFC/SFB is made available to you for evaluation in the SFCERR or SFCSTATUS variable respectively on the instance DB. | Load the SFCERR or SFCSTATUS variable from the instance DB. |
| 1E41 | The number of bytes specified at the FBs' LEN parameter is not permissible. | You must stay within a range of values of 1 to 1,024 bytes. |
| 1E41 | P_PRINT instruction:  The number of bytes specified for the variable or format string in the pointer DB under length is not permissible. | You must specify a permissible length: 32 bytes for variables, 150 bytes for format strings. |
| 1E43 | P_PRINT instruction: No pointer available for format string. | Enter the data block no. and data word no. for the format string in the pointer DB. |

> **Note**
>
> An error message is only output if the ERROR bit (job canceled with error) is also set. In all other cases the STATUS word is zero.

### Calling the SFCERR or SFCSTATUS variable

You can call the SFCERR or SFCSTATUS variable to obtain more detailed information about the pending event class 30 error, 14 (1E0EH) or 15 (1E0FH).

You can load the SFCERR or SFCSTATUS variable only by means of symbolic access to instance DB of the corresponding instruction.

Error messages entered in the SFCERR variable can be found in the system functions SFC 58 under "WR_REC: Write data record to I/O" and SFC 59 under "RD_REC: Read data record from I/O".

Error messages entered in the SFCSTATUS variable can be found in the system functions SFB 52 under "RDREC: Read data record" and SFB 53 under "WRREC: Write data record".

---

**See also**

[RDREC: Read data record](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdrec-read-data-record-s7-300-s7-400)
  
[WRREC: Write data record](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wrrec-write-data-record-s7-300-s7-400)
  
[WR_REC: Write data record to I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400)
  
[RD_REC: Read data record from I/O](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)

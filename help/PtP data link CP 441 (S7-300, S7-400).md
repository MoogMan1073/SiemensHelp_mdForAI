---
title: "PtP data link CP 441 (S7-300, S7-400)"
package: ProgFBCP441enUS
topics: 5
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PtP data link CP 441 (S7-300, S7-400)

This section contains information on the following topics:

- [Communication instructions (S7-300, S7-400)](#communication-instructions-s7-300-s7-400)
- [V24_STAT_441: Reading accompanying signals from the RS232C interface (S7-300, S7-400)](#v24_stat_441-reading-accompanying-signals-from-the-rs232c-interface-s7-300-s7-400)
- [V24_SET_441: Writing accompanying signals to the RS232C interface (S7-300, S7-400)](#v24_set_441-writing-accompanying-signals-to-the-rs232c-interface-s7-300-s7-400)
- [SYSTAT error message area (S7-300, S7-400)](#systat-error-message-area-s7-300-s7-400)

## Communication instructions (S7-300, S7-400)

### Introduction

Instead of using its own blocks, the CP 441 communicates by means of instructions of the S7-400 automation system

The S7-400 automation system provides a number of instructions which can be called in the user program to initiate and control communication between the CPU and CP 441 communication processor. The instructions are saved to non-volatile memory of the CPU.

### Instructions from the automation system S7-400

The table below lists the instructions that the S7-400 automation system provides for communication between the CPU and CP 441.

Instructions from the automation system S7-400

| SFB | Meaning |
| --- | --- |
| BSEND | With the instruction BSEND, you can send data from a S7-data range to a communication partner with a destination. |
| BRCV | With the instruction BRCV, you can receive the data from a communication partner and transfer it to a S7-data range. |
| FETCH | RK 512 only: With the instruction FETCH, you can fetch the data from a communication partner. |
| PUT | RK 512 only: With the instruction PUT, you can send the data to the communication partner with dynamic destination addresses.. |
| PRINT | With the instruction PRINT, you can print a message text on a printer with up to four variables. |
| STATUS | With the instruction STATUS, you can call the status of a communication connection. |

### Further Information

A detailed description of the instructions from the automation system S7-400 and their settings can be found under "Overview of instructions for S7 communication".

---

**See also**

[Overview of the S7 communication instructions](S7%20communication%20%28S7-300%2C%20S7-400%29.md#overview-of-the-s7-communication-instructions-s7-300-s7-400)
  
[Data transmission from CPU to communication module with BSEND (CP 441-2) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-from-cpu-to-communication-module-with-bsend-cp-441-2-s7-300-s7-400)
  
[Data transmission from the communication module to the CPU with BRCV (CP 441-2) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-from-the-communication-module-to-the-cpu-with-brcv-cp-441-2-s7-300-s7-400)
  
[Fetching data with RK512 (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#fetching-data-with-rk512-s7-300-s7-400)

## V24_STAT_441: Reading accompanying signals from the RS232C interface (S7-300, S7-400)

### Description

The V24_STAT_441 instruction reads the RS 232C accompanying signals from an interface of the CP 441 and makes them available to you at the block parameters. The V24_STAT_441 instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

The RS 232C accompanying signals are updated each time the instruction is called (cyclic polling). At the V24_STAT_441 instruction, select the interface by setting an ID that represents the "local ID" of one of the connections operating on this interface.

The binary result BR is not affected.

> **Note**
>
> A positive voltage at the RS232 C input signals DSR, CTS, DCD and RI is mapped accordingly to signal status "1" of the input signals DSR_IN, CTS_IN, DCD_IN and RI_IN of the V24_STAT_441 instruction.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | VAR_INPUT | BOOL | Enables transmission at the rising edge |
| ID | VAR_INPUT | WORD | Clear communication connection to a communication partner |
| NDR | VAR_OUTPUT | BOOL | Rising edge indicates that new receive data is available to the user program |
| ERROR | VAR_OUTPUT | BOOL | Rising edge indicates errors |
| STATUS | VAR_OUTPUT | WORD | Contains detailed error information or a warning |
| DTR_OUT | OUTPUT | BOOL | **D**ata **t**erminal **r**eady, CP 441 ready  (CP 441 output) |
| DSR_IN | OUTPUT | BOOL | **D**ata **s**et **r**eady, Communication partner ready  (CP 441 input) |
| RTS_OUT | OUTPUT | BOOL | **R**equest **t**o **s**end, CP 441 ready to send<sup>1</sup>  (CP 441 output) |
| CTS_IN | OUTPUT | BOOL | **C**lear **t**o **s**end, Communication partner is ready to receive data from CP 441 (response to RTS = ON of the CP 441)  (CP 441 input) |
| DCD_IN | OUTPUT | BOOL | **D**ata **C**arrier **d**etect, receive signal level  (CP 441 input) |
| RI_IN | OUTPUT | BOOL | **R**ing **I**ndicator, Indication of incoming call  (CP 441 input) |

### Example

Example of the call of the V24_STAT_441 instruction

| STL |  |  |  |
| --- | --- | --- | --- |
|  | CALL FB 5, DB55 |  |  |
|  |  | REQ | := DB30.DBX10.0 |
|  |  | ID | :=W#16#1000 |
|  |  | NDR | := DB30.DBX10.1 |
|  |  | ERROR | := DB30.DBX10.2 |
|  |  | STATUS | := DB30.DBW20 |
|  |  | DTR_OUT | := DB30.DBX30.0 |
|  |  | DSR_IN | := DB30.DBX30.1 |
|  |  | RTS_OUT | := DB30.DBX30.2 |
|  |  | CTS_IN | := DB30.DBX30.3 |
|  |  | DCD_IN | := DB30.DBX30.4 |
|  |  | RI_IN | := DB30.DBX30.5 |

clipboard

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

## V24_SET_441: Writing accompanying signals to the RS232C interface (S7-300, S7-400)

### Description

You can set or reset the interface outputs of CP 441 via the parameter inputs of the V24_SET_441 instruction. The V24_SET_441 instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

### Operating principle

At the V24_SET_441 instruction, select the interface by setting an ID that represents the "local ID" of one of the connections operating on this interface.

The binary result BR is not affected.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | VAR_INPUT | BOOL | Enables transmission at the rising edge |
| ID | VAR_INPUT | WORD | Clear communication connection to a communication partner |
| DONE | VAR_OUTPUT | BOOL | Signals error-free completion of the job at a rising edge |
| ERROR | VAR_OUTPUT | BOOL | Rising edge indicates errors |
| STATUS | VAR_OUTPUT | WORD | Contains detailed error information or a warning |
| RTS | INPUT | BOOL | **R**equest **t**o **s**end, CP 441 ready to send  (Control CP 441 output) |
| DTR | INPUT | BOOL | **D**ata **t**erminal **r**eady, CP 441 ready  (Control CP 441 output) |

### Example

Example of the call of the V24_SET_441 instruction

| STL |  |  |  |
| --- | --- | --- | --- |
|  | CALL FB 6, DB56 |  |  |
|  |  | REQ | := DB40.DBX10.0 |
|  |  | ID | :=W#16#1000 |
|  |  | DONE | := DB40.DBX10.1 |
|  |  | ERROR | := DB40.DBX10.2 |
|  |  | STATUS | := DB40.DBW20 |
|  |  | RTS | := DB40.DBX30.2 |
|  |  | DTR | := DB40.DBX30.0 |

clipboard

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

## SYSTAT error message area (S7-300, S7-400)

### Error-Signaling Area SYSTAT

The error-signaling area SYSTAT is an error area which is available for every interface (ID number). The SYSTAT records all errors/events which can occur during data transmission on an interface.

> **Note**
>
> Because the STATUS request is executed asynchronously to the rest of the requests running at an interface, an SFB with a specific R_ID cannot be assigned to the error messages. This means that although SYSTAT can display which errors have occurred at an interface, it cannot show which SFB call (R_ID number) triggered the error.

### Errors/Events

The SYSTAT messages are entered in bytes 2 to 15 of the LOCAL parameter when the STATUS SFB is called. In addition to the error byte (byte 2), the first six errors/events are displayed. Error event 1 is the oldest.

If other error events occur, these cannot be reported until the "old" entries are deleted. The error-signaling area must therefore be deleted in good time. This is done when the STATUS SFB is called.

**The errors/events are stored as follows:**

| Symbol | Meaning |
| --- | --- |
| - Byte 0 | Operating state of CP (02H for RUN, 05H for defective) |
| - Byte 1 | Reserved |
| - Byte 2 | Bit 0 -F Enter error in SYSTAT  Bit 1 -U Error overflow  Bit 2 -B Break |
| - Byte 3 | Reserved |
| - Byte 4/5 | Event 1 |
| - Byte 6/7 | Event 2 |
| - Byte 8/9 | Event 3 |
| - Byte 10/11 | Event 4 |
| - Byte 12/13 | Event 5 |
| - Byte 14/15 | Event 6 |

### Event classes

| Event class | Meaning |
| --- | --- |
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

### Event numbers

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0101 | Fault while testing operating system EPROM of CP | CP defective; replace CP. |
| 0102 | RAM test of CP errored |  |
| 0103 | Request interface of CP defective |  |
| 0104 | No interface submodule inserted | Insert suitable interface submodule for CP. |
| 0105 | - Parameter memory defective - Interface submodule unplugged after parameter assignment | Exchange CP or insert suitable interface submodule for CP. |
| 0110 | Fault in CP firmware | Switch module off and on again. If necessary, replace module. |
| 0201 | No parameters  Parameter memory empty or has unknown contents | Load interface parameters. |
| 0208 | Parameter assignment and interface submodule incompatible | Check parameters set for interface submodule. |
| 020F | Invalid parameter assignment detected at start of parameter communication. Interface could not be parametered. | Correct invalid parameters and restart. |
| 0210 | Total baud rate exceeded | Reduce the baud rates of the two interfaces so that the total baud rate is not exceeded. |
| 0211 | Total baud rate back in range | Total baud rate was out of range. It is now back in range after the excursion. |
| 0301 | Invalid or no source/destination data type  Invalid area (start address, length)  Invalid or no DB (e.g. DB 0) or  Other data type invalid or missing | Check parameters on CPU and CP and correct if necessary.   **RK 512 only:** Partner returns invalid parameters in telegram header.  Check parameters on CPU and CP; possibly create block.  See request tables for valid data types.   **RK 512 only:** Partner provides incorrect parameters in the message frame header. |
| 0302 | Area too short | Check parameters on CPU and CP; possibly check block/area.   **RK 512 only:**Partner provides incorrect parameters in the message frame header. |
| 0303 | Area cannot be accessed | Check parameters on CPU and CP. Obtain the permissible start addresses and lengths from the request tables.   **RK 512 only:** Partner provides incorrect parameters in the message frame header. |
| 0401 | CP cannot accept requests (overload) | In your user program, reduce number of requests called concurrently for CP. |
| 0402 | CP cannot process request type | Check if the system function blocks you have called in user program are valid for CP. |
| 0403 | Incorrect, unknown or illegal data type | Check program, e.g. for incorrect parameters of SFB. |
| 0407 | An error has occurred during data transmission between the CPU and the CP. Data cannot be received because there is no access to the CPU destination frame or the CPU destination frame does not exist or is too short. Writing data to the CPU destination frame or reading data from the CPU source frame during a CPU stop when assigning parameters is not permitted. | Check the destination frame on the CPU. Check the parameter assignment for "Response to a CPU Stop". |
| 0408 | - **Only for 3964R and ASCII drivers** - A temporary error has occurred during data transmission between the CPU and the CP (receive). The request is queued for repetition because the CPU is temporarily overloaded or the receive block (BRCV) is requested too infrequently or the receive block has been temporarily blocked. | - Reduce the number of communication requests. Call the receive block more often. Check if the receive block has been blocked too long. |
| 0409 | - **Only for 3964R and ASCII drivers** - An error has occurred during data transmission between the CPU and the CP. Data reception is not possible. After multiple attempts (see (04)07H), the request has canceled after 10 seconds because the receive block (BRCV) could not be called or is blocked. | - Check if the receive block has been called or has been blocked. |
| 040B | Error during data transmission between CPU and CP, because  - no connection has been configured - no receipt possible via configured connection | - Configure the connection in "NetPro" - Enter in "NetPro" under "Object Properties Connection) as communication direction:   - 2: Partner → local or   - 3: Local ↔ partner |
| 0501 | Current request aborted as a result of CP restart. | No remedy is possible at POWER ON. When changing the parameters of the CP in the programming device, before writing an interface you should ensure there are no more requests running from the CPU. |
| 0502 | Job not permitted in this CP operating mode (e.g., device interface not parameterized) | Set the parameters for the device interface. |
| 0503 | Wrong time, incorrect format | Check the time parameters. |
| 0505 | **Only for printer drivers:**   System data block with message texts not available on the CP | Use the parameter assignment software to configure the message text and then carry out a restart. |
| 0506 | **Only for printer drivers:**   Message text not available | Use the parameter assignment software to configure the message texts and then carry out a warm restart. |
| 0507 | **Only for printer drivers:**   Message text too long | Edit the message text to reduce it to a length of fewer than 150 characters (or no more than 250 characters if it contains variables). |
| 0508 | **Only for printer drivers:**   Too many conversion instructions | You have configured more conversion instructions than variables. Conversion instructions without associated variables will be ignored. |
| 0509 | **Only for printer drivers:**   Too many variables | You have configured more variables than conversion instructions. Variables without associated conversion instructions will not be output. |
| 050A | **Only for printer drivers:**   Unknown conversion instruction | Check the conversion instruction. Undefined or unsupported conversion instructions are replaced in the printout with ******. |
| 050B | **Only for printer drivers:**   Unknown control instruction | Check the control instruction. Undefined or unsupported control instructions will be ignored. The control instruction will not be output as text either. |
| 050C | **Only for printer drivers:**   Conversion instruction not executable | Check the conversion instruction. Conversion instructions that cannot be executed are output in the expression in accordance with the defined width and the valid remainder of the conversion instruction or the standard representation with * characters. |
| 050D | **Only for printer drivers:**   Width in conversion instruction too small or too great | Correct the specified width of the variable in the conversion instruction on the basis of the variable's maximum possible number of characters in text-based display types (A, C, D, S, T, Y, Z). Only as many characters as will fit in the specified width appear in the printout; the text is truncated to this width. In all other cases, * characters are output corresponding to the width. |
| 050E | **Only for ASCII drivers:**   An error occurred while sending. The defined end-of-text characters did not occur within the maximum allowed length or in the case of automatic appending, the maximum allowed transmission length was exceeded. | Extend the end-of-text characters in the transmission buffer at the desired point or select a shorter telegram length for automatic appending. |
| 050F | Number of requests that can be processed simultaneously too great | Change your STEP 7 program so that fewer requests can run simultaneously. |
| 0510 | Area occupied (resource) | Repeat the request. |
| 0511 | Length not permissible for this request type | Divide up the data to be transmitted into several requests. |
| 0512 | **RK 512 only:**Mismatch between SFB's source and destination parameters. | Obtain the permissible values from the request tables. |
| 0513 | Data type error (DB ...):  Unknown or impermissible data type (e.g. DE)   **RK 512 only:** Mismatch between SFB's source and destination data types. | Obtain the permissible data types and their combinations from the request tables. |
| 0514 | Specified start addresses too high for desired data type or start address or DB/DX number too low. | Obtain from the request tables the permissible start addresses and DB/DX numbers that can be specified in the program. |
| 0515 | **RK 512 only:** Wrong bit number specified for coordination flag. | Permissible bit numbers: 0 to 7 |
| 0516 | **RK 512 only:** Specified CPU too high. | Permissible CPU numbers: none, 1, 2, 3 or 4 |
| 0517 | An error occurred while receiving. The receive telegram is longer than 4 KB or is longer than the defined "fixed receive length" or the receive telegram does not fit into the destination frame. | Reduce the length of your connection partner's telegram or increase the length of your receive DB. |
| 0518 | Transmission length at sending too great ( >4 KB) | RK 512 only: Obtain the permissible lengths from the request tables.  Split the request up into several shorter requests. |
| 0519 | CP in wrong mode for PLC request | Check if the addressed interface is parametered. |
| 051A | **RK 512 only:** Error sending a command telegram  An associated procedure number has just been entered in STATUS. | See the remedy for the previous error number. |
| 051B | **Only for printer drivers:**   Precision invalid | Correct the specified precision in the conversion instruction. The precision is always initialized with a dot prefix to identify and limit the width (for example, ".2" to output the decimal point and two decimals.) Precision is only relevant to display types A, D, F and R. It is ignored otherwise. |
| 051C | **Only for printer drivers:**   Variable invalid  (variable length incorrect/incorrect type) | Correct the specified send variable. |
| 0601 | Error in 1st command byte (not 00 or FFH) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0602 | Error in 3rd command byte (not A, 0 or FFH) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0603 | Error in 3rd command byte in the case of continuation telegrams (command not as for 1st telegram) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0604 | Error in 4th command byte (command letter incorrect) | Header layout error at partner or a command combination has been requested that is not permitted at the CP. Check the permissible commands. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0605 | Error in 4th command byte in the case of continuation telegrams (command not as for 1st telegram) | Header layout error at partner. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0606 | Error in 5th command byte (DB number not permissible) | Obtain from the request tables the permissible DB numbers, start addresses or lengths. |
| 0607 | Error in 5th or 6th command byte (start address too high) | Obtain from the request tables the permissible DB numbers, start addresses or lengths. |
| 0608 | Error in 7th or 8th command byte (impermissible length) | Obtain from the request tables the permissible DB/DX numbers, start addresses or lengths. |
| 0609 | Error in 9th and 10th command byte (coordination flag for this data type impermissible or bit number too high) | Header layout error at partner. Find out from the request tables when a coordination flag is permitted. |
| 060A | Error in 10th command byte (CPU number not permitted) | Header layout error at partner. |
| 060B | SEND telegram was longer/shorter than expected (more/less data received than announced in telegram header). | Correction required at the partner |
| 060C | GET command telegram received with user data | Correction required at the partner |
| 060D | The CP received a telegram during an invalid operating mode.  - Receive connection between CPU and CP not set up or not yet correctly set up - CP startup is not fully completed. - Parameters for the interface are currently being assigned | - Check if the addressed connection has been assigned the correct parameters. - This error message can occur only during CP startup. Repeat the request. - This is a temporary error. Repeat the request. |
| 060E | Synchronous fault of partner  - New (continuation) command telegram received before response telegram sent. - 1. 1st command telegram expected and continuation telegram came. - Continuation command telegram expected and 1st telegram came | This error may be reported after your own programming device is restarted in the case of long telegrams or when the partner is restarted. These cases represent normal system start-up characteristics.  The error can also occur during operation as a consequence of error statuses only recognized by the partner.  Otherwise, you have to assume an error on the part of the partner device. The error may not occur in the case of requests <128 bytes. |
| 060F | DB locked by coordination function | In local program: After processing of the last transmission data, enable the last receive block with "EN".  In partner program: Repeat the request |
| 0610 | Telegram received too short (length <4 bytes in the case of continuation or response telegrams or <10 bytes in the case of command telegrams) | You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0611 | Telegram length and length specified in telegram header are not the same. | You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0612 | Error sending the (continuation) response telegram. An associated procedure error number has been entered in STATUS immediately beforehand. | See remedy for the error number entered immediately beforehand in STATUS. |
| 0701 | Sending of the first repetition:  - An error was detected when transmitting the telegram or - The partner requested a repetition by means of a negative acknowledgment character (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0702 | Error establishing connection:  - After STX was sent, NAK or another code (except DLE or STX) was received or - The response came too early or - An initialization conflict occurred | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0703 | Acknowledgment delay time (QVZ) exceeded:   After STX was sent, partner did not respond within the acknowledgment delay time. | The partner device is too slow or not ready to receive or there is a break in the transmission line, for example. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0704 | Termination by partner:  One or more codes were received from the partner during sending | Check if the partner also indicates an error; possibly it has not received all of the transmitted data (for example, due to an interrupted data link) or because fatal errors are pending or the characteristics of the partner device is faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0705 | Negative acknowledgment when sending | Check if the partner also indicates an error; possibly it has not received all of the transmitted data (for example, due to an interrupted data link) or because fatal errors are pending or the characteristics of the partner device is faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0706 | End-of-connection error:  - Partner rejected telegram at end of connection with NAK or a random string (except for DLE) or - Acknowledgment characters (DLE) received too early. | Check if the partner also indicates an error; possibly it has not received all of the transmitted data (for example, due to an interrupted data link) or because fatal errors are pending or the characteristics of the partner device is faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0707 | Acknowledgment delay time exceeded at end of connection or response monitoring time exceeded after a send telegram:  After connection termination with DLE ETX, no response received from partner within acknowledgment delay time. | Partner device too slow or faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0708 | ASCII Driver and printer driver only: The wait time for XON or CTS = ON has expired. | The communication partner is faulty, too slow or has been taken offline. Check the communication partner; you may need to change the parameter assignment. |
| 0709 | Connection setup not possible. Number of permitted setup attempts exceeded. | Check the interface cable or the transmission parameters. |
| 070A | The data could not be transmitted. The permitted number of transfer attempts was exceeded. | Check the interface cable or the transmission parameters. |
| 0801 | Expectation of the first repetition:  An error was detected on receiving a telegram and the CP requested repetition from the partner via a negative acknowledgment (NAK). | A repetition is not an error, but it can indicate that there is interference on the data link or the partner device has malfunctioned. If the message frame has not been transmitted after the maximum number of repetitions, an error number describing the first error that occurred is output. |
| 0802 | **Error establishing connection:**   - In idle mode, one or more random codes (other than NAK or STX) were received or - After an STX was received, the partner sent more characters without waiting for the response DLE.    **After POWER ON of the partner:**   - While partner is being switched on, the CP receives an undefined character. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0805 | Logical error while receiving:  After DLE was received, a further random code (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the telegram header and data string or the connection is terminated with DLE ETX. Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0806 | Character delay time (ZVZ) exceeded:  - Two successive characters were not received within character delay time or - 1. character after sending of DLE while establishing connection was not received within the character delay time. | Partner device too slow or faulty. Interconnect an interface tester in the transmission line to see if this is the case. |
| 0808 | Block check character (BCC) error (only in the case of RK 512 with the 3964R procedure and the 3964R procedure)  The value of BCC calculated internally does not match the BCC received by the partner when the connection was terminated. | Check if there is a serious problem with the connection. In this case, error codes of the event class 8/event number 12 sometimes occur. Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 080A | There is no free receive buffer available:  After receipt of STX, there was no empty receive buffer available to the procedure at connection setup and after an additional waiting time | Increase the call rate for the receive instruction in the user program. |
| 080C | Transmission error:  A transmission error (parity error, stop bit error, overflow error) was detected.   If a corrupted character is received in idle mode, the error is reported immediately so that disturbances on the transmission line can be detected early.   **Only in the case of RK 512 and 3964(R):**   If this occurs during send or receive operation, repetitions are initiated. | Disturbances on the data link cause telegram repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring.  Check that the settings for baud rate, parity and number of stop bits are the same on both devices. |
| 080D | BREAK   The connection line (receive line) to the partner device is interrupted | Establish the connection between the devices or switch on the partner device. In the case of TTY, Check if there is a current loop in the idle state. |
| 0812 | **Only for ASCII drivers:**   More characters were received after the CP had sent XOFF or set CTS to OFF. | Reset the parameters for the communication partner or read data from CP more quickly. |
| 0815 | Discrepancy between settings for transfer attempts at CP and communication partner. | Set the same number of transfer attempts at communications partner as at CP. You can interconnect an interface tester in the transmission line to debug the partner device. |
| 0816 | - The length of a received telegram was longer than the length agreed upon or - the length of the parametered receive buffer (with CP 441 only) is too short. | - A correction is necessary at the partner or - the length of the receive buffer (with CP 441 only) must be enlargened |
| 0818 | **Only for ASCII drivers:**   DSR = OFF or CTS = OFF | The partner has switched the DSR or CTS signal to "OFF" before or during a transmission.  Check the partner's control of the RS 232C accompanying signals. |
| 0902 | **RK 512 only:** Memory access error at partner (memory does not exist)  With SIMATIC S5 as partner:  - Incorrect area at status word or - Data area does not exist (except DB/DX) or - Data area too short (except DB/DX) | Check that the partner has the desired data area and that it is big enough or check the parameters of the called system function block.  Check the specified length at the system function block. |
| 0903 | **RK 512 only:** DB/DX access error at the partner (DB/DX does not exist or is too short)  With SIMATIC S5 as partner:  - DB/DX does not exist or - DB/DX too short or - DB/DX number impermissible   Permissible source area for GET request exceeded | Check that the partner has the desired data area and that it is big enough or check the parameters of the called system function block.  Check the specified length at the system function block. |
| 0904 | **RK 512 only:** Partner returns "Request type not permitted". | Partner malfunction, because a system command is never issued from the CP 441. |
| 0905 | **RK 512 only:** Error at partner or at SIMATIC S5 as partner:  - Source/destination type not permissible or - Memory error in partner programmable controller or - Error notifying CP/CPU at the partner or - Partner programmable controller is in STOP state | Check if the partner can transmit the desired data type.  Check the structure of the hardware at the partner.  Set the partner programmable controller to RUN. |
| 0908 | **RK 512 only:** Partner detecting synchronization error:  Telegram sequence error. | This error occurs at restart of your own programmable controller or of the partner. This represents normal system start-up characteristics. You do not need to correct anything. The error is also conceivable during operation as a consequence of previous errors. Otherwise, you can assume an error on the part of the partner device. |
| 0909 | **RK 512 only:** DB/DX disabled at partner by coordination flag | In partner program: After processing of the last transmission data, reset the coordination flag.   In own program: Repeat the request. |
| 090A | **RK 512 only:** Error detected by partner in telegram header: 3rd command byte in header is incorrect | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090B | **RK 512 only:** Error in telegram header: 1. or incorrect command byte 4 in header | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090C | **RK 512 only:** Partner detects incorrect telegram length (total length). | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 090D | **RK 512 only:** Partner has not yet restarted. | Restart the partner programmable controller or set the mode selector on the CP or CPU to RUN. |
| 090E | **RK 512 only:** Unknown error number received in response telegram. | Check if the error is the result of disturbances or of a malfunction at the partner. Interconnect an interface tester in the transmission line to see if this is the case. |
| 0A01 | **RK 512 only:** Synchronization error of partner, because:  - Response telegram without request - Response telegram received before continuation telegram sent - Continuation response telegram received after an initial telegram was sent - A first response telegram was received after a continuation telegram was sent | This error is reported after your own programming device is restarted in the case of long telegrams or when the partner is restarted. This represents normal system start-up characteristics. You do not have to correct anything.  The error can also occur during operation as a consequence of error statuses only recognized by the partner.  Otherwise, you can assume an error on the part of the partner device. The error may not occur in the case of requests <128 bytes. |
| 0A02 | **RK 512 only:** Error in the structure of the received response telegram (1st byte not 00 or FF) | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A03 | **RK 512 only:** Received response telegram has too many data or not enough data. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A04 | **RK 512 only:** Response telegram for SEND request arrived with data. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |
| 0A05 | **RK 512 only:** No response telegram from partner within monitoring time. | Is the partner a slow device? This error is also often displayed as a consequence of a previous error. For example, procedure receive errors (event class 8) can be displayed after a GET telegram was sent. Reason: As a result of disturbances, the response telegram could not be received and the monitoring time elapsed. This error can also occur if a restart was carried out at the partner before it could respond to the most recently received GET telegram. |
| 0A06 | **RK 512 only:** Received response telegram after GET request has not enough data. | Check for malfunction at partner device, possibly by using interface test device switched into the transmission line. |

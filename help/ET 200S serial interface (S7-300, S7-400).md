---
title: "ET 200S serial interface (S7-300, S7-400)"
package: ProgFB1SIenUS
topics: 22
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# ET 200S serial interface (S7-300, S7-400)

This section contains information on the following topics:

- [ET 200S 1SI for 3964(R) and ASCII (S7-300, S7-400)](#et-200s-1si-for-3964r-and-ascii-s7-300-s7-400)
- [ET 200S 1SI for Modbus (S7-300, S7-400)](#et-200s-1si-for-modbus-s7-300-s7-400)
- [ET 200S 1SI for USS (S7-300, S7-400)](#et-200s-1si-for-uss-s7-300-s7-400)

## ET 200S 1SI for 3964(R) and ASCII (S7-300, S7-400)

This section contains information on the following topics:

- [S_RCV: receiving data (S7-300, S7-400)](#s_rcv-receiving-data-s7-300-s7-400)
- [S_SEND: Sending Data (S7-300, S7-400)](#s_send-sending-data-s7-300-s7-400)
- [S_VSTAT: Read accompanying signals at the RS 232C interface (S7-300, S7-400)](#s_vstat-read-accompanying-signals-at-the-rs-232c-interface-s7-300-s7-400)
- [S_VSET: Write accompanying signals at the RS 232C interface (S7-300, S7-400)](#s_vset-write-accompanying-signals-at-the-rs-232c-interface-s7-300-s7-400)
- [S_XON: Assign parameters for XON/XOFF data flow control (S7-300, S7-400)](#s_xon-assign-parameters-for-xonxoff-data-flow-control-s7-300-s7-400)
- [S_RTS: Assign parameters for RTS/CTS data flow control (S7-300, S7-400)](#s_rts-assign-parameters-for-rtscts-data-flow-control-s7-300-s7-400)
- [S_V24: Assign parameters for data flow control using automatic operation of the RS 232C accompanying signals (S7-300, S7-400)](#s_v24-assign-parameters-for-data-flow-control-using-automatic-operation-of-the-rs-232c-accompanying-signals-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

### S_VSTAT: Read accompanying signals at the RS 232C interface (S7-300, S7-400)

#### Description

The S_VSTAT instruction reads the RS 232C accompanying signals of the ET 200S 1SI module and makes them available to you in the block parameters. For data transmission, the S_VSTAT instruction is called by means of (unconditional) static operation in the cycle or alternatively, in a time-controlled program.

#### Operating principle

The RS 232C accompanying signals are updated each time the instruction is called (cyclic polling).

The address of the ET 200S 1SI module to be addressed is specified in the LADDR parameter.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| DONE<sup>1</sup> | OUTPUT | BOOL | Indicates that the instruction has terminated.  (ET 200S 1SI output) |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| DTR_OUT <sup>1</sup> | OUTPUT | BOOL | Data terminal ready,  ET 200S 1SI ready for operation.  (ET 200S 1SI output) |
| DSR_IN <sup>1</sup> | OUTPUT | BOOL | Data set ready; communication partner ready for operation.  (ET 200S 1SI input) |
| RTS_OUT <sup>1</sup> | OUTPUT | BOOL | Request to send,  ET 200S 1SI clear to send.  (ET 200S 1SI output) |
| CTS_IN <sup>1</sup> | OUTPUT | BOOL | Clear to send; communication partner can receive data from the ET 200S 1SI module (response to RTS = ON of the ET 200S 1SI)  (ET 200S 1SI input) |
| DCD_IN <sup>1</sup> | OUTPUT | BOOL | Data carrier detect  (ET 200S 1SI input) |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> On successful completion of a job, these parameters remain available for the duration of **one** CPU cycle. |  |  |  |

#### Allocation in the data area

The S_VSTAT instruction works in combination with an I_STAT instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

> **Note**
>
> A minimum pulse duration is necessary to detect a signal change. Determining factors are the CPU cycle time, the update time on the ET 200S 1SI module and the response time of the communication partner.

#### Startup

The COM_RST parameter of the S_VSTAT instruction is used to report a startup to the instruction.

Set the COM_RST parameter in the startup OB to 1.

Call the instruction in cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

### S_VSET: Write accompanying signals at the RS 232C interface (S7-300, S7-400)

#### Description

You can set and reset the interface outputs using the corresponding parameter inputs of the S_VSET instruction. The S_VSET instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

The address of the ET 200S 1SI module to be addressed is specified in the LADDR parameter.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| RTS | INPUT | BOOL | Request to send,  ET 200S 1SI clear to send.  (Controls ET 200S 1SI output) |
| DTR | INPUT | BOOL | Data terminal ready,  ET 200S 1SI ready for operation.  (Controls ET 200S 1SI output) |
| DONE<sup>1</sup> | OUTPUT | BOOL | (ET 200S 1SI output) |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> On successful completion of a job, these parameters remain available for the duration of **one** CPU cycle. |  |  |  |

#### Allocation in the data area

The S_VSET instruction works in combination with an I_SET instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited

#### Startup

The COM_RST parameter of the S_VSET instruction is used to report a startup to the instruction.

Set the COM_RST parameter in the startup OB to 1.

Call the instruction in cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)

### S_XON: Assign parameters for XON/XOFF data flow control (S7-300, S7-400)

#### Description

Using the S_XON instruction, you can set additional parameters if the module is configured for XON/XOFF data flow control.

> **Note**
>
> The instruction S_XON must be started before the instructions S_SEND, S_RCV, S_VSET and S_VSTAT and have completed its task (DONE = TRUE).

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| XON | INPUT | BYTE | XON character  0 to 7F<sub>H</sub> (7 data bits) 0 to FF<sub>H</sub> (8 data bits)  Default: 11 (DC1) |
| XOFF | INPUT | BYTE | XOFF character  0 to 7F<sub>H</sub> (7 data bits) 0 to FF<sub>H</sub> (8 data bits)  Default: 13 (DC3) |
| WAIT_FOR_XON | INPUT | TIME | Wait time for XON after XOFF  20 ms to 10 min 55 s 350 ms  Default: 2 s |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00 |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> The DONE, ERROR and STATUS parameters are available for **one** CPU cycle following a successful request. |  |  |  |

#### Allocation in the data area

The S_XON instruction works in combination with an I_XON instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If error STATUS == W#16#1Exx occurs, you can view the SFCERR variable for more precise error information.

#### Startup

The COM_RST parameter of the S_XON instruction is used to report a startup to the instruction.

Set the COM_RST parameter in the startup OB to 1.

Call the instruction in cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

---

**See also**

[Data flow control and secondary signals (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-flow-control-and-secondary-signals-s7-300-s7-400)

### S_RTS: Assign parameters for RTS/CTS data flow control (S7-300, S7-400)

#### Description

Using the S_RTS instruction, you can configure additional parameters if the module is configured for RTS/CTS data flow control.

> **Note**
>
> The instruction S_RTS must be started before the instructions S_SEND, S_RCV, S_VSET and S_VSTAT and have completed its task (DONE = TRUE).

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S SI module  The start address is taken from STEP 7. |
| WAIT_FOR_CTS | INPUT | TIME | Wait time for CTS = ON  20 ms to 10 min 55 s 350 ms  Default: 2 s |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00 |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> The DONE, ERROR and STATUS parameters are available for **one** CPU cycle following a successful request. |  |  |  |

#### Allocation in the data area

The S_RTS instruction works in combination with an I_RTS instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If error STATUS == W#16#1Exx occurs, you can view the SFCERR variable for more precise error information.

#### Startup

The COM_RST parameter of the S_RTS instruction is used to report a startup to the instruction.

Set the COM_RST parameter in the startup OB to 1.

Call the instruction in cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

---

**See also**

[Data flow control and secondary signals (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-flow-control-and-secondary-signals-s7-300-s7-400)

### S_V24: Assign parameters for data flow control using automatic operation of the RS 232C accompanying signals (S7-300, S7-400)

#### Description

Using the S_V24 instruction, you can configure additional parameters if the module is configured for automatic control of the RS 232C accompanying signals.

> **Note**
>
> The instruction S_V24 must be started before the instructions S_SEND, S_RCV, S_VSET and S_VSTAT and have completed its task (DONE = TRUE).

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| TIME_RTS_OFF | INPUT | TIME | Time that must elapse after transmission before RTS is disabled.   0 ms to 10 min 55 s 350 ms  Default: 10 ms |
| DATA_WAIT_TIME | INPUT | TIME | Time to wait until the partner sets CTS = ON once RTS has been set.   0 ms to 10 min 55 s 350 ms  Default: 10 ms |
| DONE<sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00 |
| ERROR<sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| STATUS<sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> The DONE, ERROR and STATUS parameters are available for **one** CPU cycle following a successful request. |  |  |  |

#### Allocation in the data area

The S_V24 instruction works in combination with an I_V24 instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If error STATUS == W#16#1Exx occurs, you can view the SFCERR variable for more precise error information.

#### Startup

The COM_RST parameter of the S_V24 instruction is used to report a startup to the instruction.

Set the COM_RST parameter in the startup OB to 1.

Call the instruction in cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

---

**See also**

[RS232 mode (CP 34x, 44x, CPU 31xC-2 PtP + ET 200S 1SI) (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#rs232-mode-cp-34x-44x-cpu-31xc-2-ptp-et-200s-1si-s7-300-s7-400)
  
[Data flow control and secondary signals (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-flow-control-and-secondary-signals-s7-300-s7-400)

### STATUS parameter (S7-300, S7-400)

#### Event classes

| Event class | Meaning |
| --- | --- |
| 2 | Error initializing |
| 5 | Error executing a CPU job |
| 7 | Send errors |
| 8 | Receive errors |
| 11 (0B<sub>H</sub>) | Warning |
| 30 (1E<sub>H</sub>) | Errors in communication between the module and CPU |

#### STATUS parameter

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0201 | No (valid) configuration available. | Provide the module with correct parameters. If necessary, ensure the system is correctly installed. |
| 0502 | Request not permitted in this operating mode of the ET 200S 1SI module (e.g., device interface not parameterized). | The send message frame is longer than 224 bytes. The ET 200S 1SI module canceled the transmission job.   Select a shorter message frame length. |
| 050E | Invalid telegram length | The send message frame is longer than 224 bytes. The ET 200S 1SI module canceled the transmission job.   Select a shorter telegram length. |
| 0550 | The parameter update request is invalid for the currently selected form of ET 200S 1SI module data flow control. | Edit the instruction parameters (S_XON, S_RTS, S_V24) in the AS program or modify the data flow control function of the ET 200S 1SI module in the hardware configuration to ensure compatibility. |
| 0551 | Frame execution error during communication between the ET 200S 1SI module and the automation system. The error occurred in the automation system during transmission of a received message frame from the ET 200S 1SI module. | The module and the automation system have canceled the transmission. Repeat the receive request; the ET 200S 1SI module sends the received message again. |
| 0702 | Only for 3964(R):  Error establishing connection:  After STX was sent, NAK or any other code (except for DLE or STX) was received. | You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0703 | Only for 3964(R):  Acknowledgment delay time (QVZ) exceeded:  After STX was sent, partner did not respond within the acknowledgment delay time. | The partner device is too slow or not ready to receive or there is a break in the transmission line, for example. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0704 | Only for 3964(R):  Termination by partner:  One or more characters were received from the partner during sending. | Check if the partner is also indicating errors, possibly because not all transmitted data arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0705 | Only for 3964(R):  Negative acknowledgment when sending | Check if the partner is also indicating errors, possibly because not all transmit data has arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0706 | Only for 3964(R):  End-of-connection error:  - Partner rejected telegram at end of connection with NAK or a random string (except for DLE) or - Acknowledgment characters (DLE) received too early. | Check if the partner is also indicating errors, possibly because not all transmit data has arrived (e.g., break in the transmission line), fatal errors are pending or the partner device has malfunctioned. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0707 | Only for 3964(R):  Acknowledgment delay time exceeded at end of connection or response monitoring time exceeded after a send telegram:  After connection termination with DLE ETX, no response received from partner within acknowledgment delay time. | Partner device too slow or faulty. If necessary, use an interface test device switched into the transmission line to check. |
| 0708 | Only for ASCII drivers:  The wait time for XON or CTS = ON has expired. | The communication partner is faulty, too slow or has been taken offline. Check the communication partner; you may need to change the parameter assignment. |
| 070B | Only for 3964(R):  Initialization conflict cannot be resolved because both partners have high priority. | Change the parameter assignment. |
| 070C | Only for 3964(R):  Initialization conflict cannot be resolved because both partners have low priority. | Change the parameter assignment. |
| 0802 | Only for 3964(R):  Error establishing connection:  - In idle mode, one or more random codes (other than NAK or STX) were received or - After an STX was received, partner sent more characters without waiting for response DLE.   After partner power ON:  - The module receives an undefined character while the partner is being switched on. | You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0805 | Only for 3964(R):  Logical error while receiving:  After DLE was received, a further random code (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the telegram header and data string or the connection is terminated with DLE ETX. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0806 | Character delay time (ZVZ) exceeded:  - Two successive characters were not received within character delay time or   Only for 3964(R):  - 1. character after sending of DLE while establishing connection was not received within the character delay time. | Partner device too slow or faulty. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0807 | Only for 3964(R):  Illegal telegram length:  A zero-length telegram has been received. | Receipt of a zero-length telegram is not an error.   Check why the communication partner is sending telegrams without user data. |
| 0808 | Only for 3964(R):  Error in block check character (BCC):  The value of BCC calculated internally does not match the BCC received by the partner when the connection was terminated. | Check if the connection is seriously disrupted; in this case you may also occasionally see error codes. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 0809 | Only for 3964(R):  The number of repetitions must the set to the same value. | Declare a block wait time at the communication partner identical to that in your module. Check for malfunction of the communication partner; you may need to use an interface test device that is switched into the transmission line. |
| 080A | There is no free receive buffer available:  No receive buffer space available for receiving data. | Increase the call rate for the S_RCV instruction. |
| 080C | Transmission error:  - Transmission error (parity/stop bit/overflow error) detected.   Only for 3964(R):  - If this happens during send or receive operations, repetition is started. - If a corrupted character is received in idle mode, the error is reported immediately so that disturbances on the transmission line can be detected early. - If the SF LED (red) lights up, there is a break in the connecting cable between the two communication partners. | Disturbances on the transmission line cause message frame repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring. Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits. |
| 080D | BREAK: Break in receive line to partner. | Reconnect or switch on partner. |
| 0810 | Only for ASCII drivers:  Parity error:  - If the SF LED (red) lights up, there is a break in the connecting cable between the two communication partners. | Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0811 | Only for ASCII drivers:  Character frame error:  - If the SF LED (red) lights up, there is a break in the connecting cable between the two communication partners. | Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0812 | Only for ASCII drivers:  More characters were received after the module had sent XOFF or set CTS to OFF. | Reconfigure the communication partner or read module data more rapidly. |
| 0818 | Only for ASCII drivers:  DSR = OFF or CTS = OFF | The partner has switched the DSR or CTS signal to "OFF" before or during a transmission.  Check the partner's control of the RS 232C accompanying signals. |
| 0850 | The length of the receive message frame is greater than 224 bytes or the defined message frame length. | Adjust the message frame length of the partner |
| 0B01 | Reception buffer is more than 2/3 full |  |
| 1E0D | "Job aborted due to warm restart, hot restart or reset" |  |
| 1E0E | Static error at the call of SFC DPRD_DAT. The RET_VAL return value of the SFC is available for evaluation in the SFCERR variable of the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E0F | Static error at the call of SFC DPWR_DAT. The RET_VAL return value of the SFC is available for evaluation in the SFCERR variable of the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E10 | Static error during the call of SFC RD_LGADR. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E11 | Static error during the call of SFC RDSYSST. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E20 | Parameter out of range. | Modify the input of the instruction so that it is within the valid range. |
| 1E41 | Invalid number of bytes specified at instruction parameter LEN | You must stay within a range of values of 1 to 224 bytes. |

#### Evaluating the SFCERR variable

More detailed information on the error events (1E) 0E<sub>H</sub>, (1E) 0F<sub>H</sub>, (1E) 10<sub>H</sub> and (1E) 11<sub>H</sub> of event class 30 is available in the [SFCERR](http://support.automation.siemens.com) variable.

You can load the SFCERR variable from the instance DB of the corresponding instruction.

The error messages entered in the SFCERR variable are described in the sections on the "DPRD_DAR" and SFC15 "DPWR_DAT" system functions in the System Software for S7-300/400, System and Standard Functions Reference Manual.

## ET 200S 1SI for Modbus (S7-300, S7-400)

This section contains information on the following topics:

- [Sending and receiving as Modbus master (S7-300, S7-400)](#sending-and-receiving-as-modbus-master-s7-300-s7-400)
- [S_RCV: receiving data (S7-300, S7-400)](#s_rcv-receiving-data-s7-300-s7-400)
- [S_SEND: Sending Data (S7-300, S7-400)](#s_send-sending-data-s7-300-s7-400)
- [S_MODB: Modbus slave instruction for ET 200S 1SI (S7-300, S7-400)](#s_modb-modbus-slave-instruction-for-et-200s-1si-s7-300-s7-400)
- [STATUS parameter (Modbus / USS) (S7-300, S7-400)](#status-parameter-modbus-uss-s7-300-s7-400)
- [ERROR_NR, ERROR_INFO parameters (S7-300, S7-400)](#error_nr-error_info-parameters-s7-300-s7-400)

### Sending and receiving as Modbus master (S7-300, S7-400)

#### Description

Data is transferred between the module and CPU by means of the S_SEND and S_RCV instructions. The S_SEND instruction is activated by an edge at the REQ input if data is to be output. The S_RCV instruction is set ready to receive with EN_R=1. An S_RCV is required for all reading function codes.

#### Sending and receiving data using the Modbus master protocol

The S_SEND and S_RCV instructions must be activated in order to execute a Modbus master job. The S_SEND instruction is activated by an edge at the REQ input when data is to be output to the module. The S_RCV instruction is made ready to receive data from the module with EN_R=1. An S_RCV is required for all reading function codes. The figure below shows the overall characteristics of the S_SEND and S_RCV parameters when a Modbus job is executed.

![Sending and receiving data using the Modbus master protocol](images/21648933771_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Send and receive sequence**
>
> As the interface between the user program and the interface module operates in half-duplex mode you must observe the following items:
>
> After positive acknowledgment of the Modbus master read job, you first have to fetch the receive data from the interface module by calling the S_RCV instruction before starting a new Modbus master send job.

### S_RCV: receiving data (S7-300, S7-400)

#### Description

The S_RCV instruction sends data from the ET 200S 1SI module to an S7 data area as specified at the DB_NO and DBB_NO parameters. For data transmission, the S_RCV instruction is called in the cycle or alternatively, in a static (unconditional) operation of a time-controlled program.

#### Operating principle

The (static) signal state "1" at parameter EN_R enables the check for data to be read from the ET 200S 1SI module. An active transmission can be canceled by setting signal state "0" at parameter EN_R and with signal state "1" at parameter R. (Because transmission may sometimes not start up again after setting parameter EN_R to "1", you should set parameter R to "1" in addition to setting EN_R to "0" to cancel an active transmission.) The canceled receive request is terminated with an error message (STATUS output). Receiving is disabled as long as signal state "0" is set at parameter EN_R. Data transmission can take several calls (program cycles), depending on the data volume.

If the instruction detects signal state "1" at the R parameter, the current transmission job is canceled and the S_RCV instruction is reset to the initial state. Receiving is disabled as long as signal state "1" is set at parameter R. If the signal state returns to "0", the canceled message frame is received again from the beginning.

Parameter LADDR specifies the address of the ET 200S 1SI to be addressed.

Output NDR indicates "Job completed without errors/data received" (all data read) and ERROR indicates error events. A corresponding error number is displayed in STATUS if an error occurs. If the receive buffer is filled to more than 2/3 of its capacity, STATUS returns a warning at each call of S_RCV. If no errors or warnings are pending, STATUS has a value of "0".

NDR and ERROR/STATUS are also output after the reset of the S_RCV instruction (LEN == 16#00) (see time sequence chart). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| EN_R | INPUT | BOOL | Enable data reading |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Receiving is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Receive data block no.: CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number (received data)   **S7-1500**: 0 ≤ DBB_NO and  DBB_NO + LEN ≤ size of the DB   **S7-300/400**: 0 ≤ DBB_NO and  DBB_NO + LEN < 8190 |
| NDR <sup>1</sup> | OUTPUT | BOOL | Job completed without errors, data received  STATUS parameter == 16#00 |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-s7-300-s7-400)  contains the error information. |
| LEN <sup>1</sup> | OUTPUT | INT | Length of the message frame received  1 ≤ LEN ≤ 224 specified in number of bytes |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> On successful completion of a receive job, the NDR, ERROR, LEN and STATUS parameters remain available for the duration of **one** CPU cycle! |  |  |  |

#### Allocation in the data area

The S_RCV instruction works in combination with an I_RCV instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If the error STATUS == W#16#1Exx occurs, you can examine the SFCERR variable for additional details. This error variable must be loaded via symbolic access to the instance DB.

#### Startup

The COM_RST parameter of S_RCV instruction is used to report a startup to the instruction.

In the startup OB, set parameter COM_RST to 1.

Call the instruction in the cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

#### Time sequence chart

The figure below illustrates the characteristics of the NDR, LEN and ERROR parameters, depending on the wiring of the EN_R and R inputs.

![Time sequence chart](images/21620102411_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input EN_R must be set to the static signal state "1". Parameter EN_R must be provided the logic operation result "1" for the duration of the receive request.

#### Rules

> **Note**
>
> The S_RCV instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CPU startup routine of the ET 200S module for the S_RCV instruction must be completed before the ET 200S 1SI module can receive a job initiated after the status transition of the CPU from STOP to RUN.

### S_SEND: Sending Data (S7-300, S7-400)

#### Description

The S_SEND instruction transmits a data block from a DB to the ET 200S 1SI as specified at the DB_NO, DBB_NO and LEN parameters. For data transmission, the S_SEND instruction is called in a static (unconditional) operation in the cycle or **alternatively**, in a time-controlled program.

#### Operating principle

Data transmission is initiated by a positive edge at the REQ input. Data transmission can take several calls (program cycles), depending on the data volume.

The S_SEND instruction can be called in the cycle by setting signal state "1" at parameter input R. This setting cancels the transmission to the ET 200S 1SI module and resets the S_SEND instruction to the initial state. Data that has already been received by the ET 200S 1SI module is still transmitted to the communication partner. A static signal state "1" at the input R indicates that data transmission is disabled.

Parameter LADDR specifies the address of the ET 200S 1SI to be addressed.

Output DONE indicates "Job completed without errors" and ERROR indicates error events. A corresponding event number is displayed in STATUS if an error occurs. If no errors occurs, the STATUS has a value 0. DONE and ERROR/STATUS are also output for RESET of the S_SEND instruction (see the time sequence chart). The binary result BR is reset if an error occurs. If the block is completed without errors, the binary result has the status "1".

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | INPUT | BOOL | Job trigger at the positive edge |
| R | INPUT | BOOL | Cancel the job  Cancels the job in progress. Transmission is disabled. |
| LADDR | INPUT | INT | Start address of the ET 200S 1SI module  The start address is taken from STEP 7. |
| DB_NO | INPUT | INT | Data block number  Send DB no.: CPU-specific, zero not allowed |
| DBB_NO | INPUT | INT | Data byte number (transmit data)   **S7-1500**: 0 ≤ DBB_NO and  DBB_NO + LEN ≤ size of the DB   **S7-300/400**: 0 ≤ DBB_NO and  DBB_NO + LEN < 8190 |
| LEN | INPUT | INT | Data length  1 ≤ LEN ≤ 224 specified in number of bytes |
| DONE <sup>1</sup> | OUTPUT | BOOL | Job completed without errors  STATUS parameter == 16#00 |
| ERROR <sup>1</sup> | OUTPUT | BOOL | Job canceled with errors  The [STATUS parameter](#status-parameter-modbus-uss-s7-300-s7-400)  contains the error information. |
| STATUS <sup>1</sup> | OUTPUT | WORD | Error specification  If ERROR == 1, [STATUS parameter](#status-parameter-modbus-uss-s7-300-s7-400) contains the error information. |
| COM_RST | IN_OUT | BOOL | Instruction restart |
| <sup>1</sup> On successful completion of a transmission job, the DONE, ERROR and STATUS parameters remain available for the duration of  **one** CPU cycle! |  |  |  |

#### Allocation in the data area

The S_SEND instruction works in combination with an I_SEND instance DB. The DB number is included with the call. Access to the data in the instance DB is prohibited.

> **Note**
>
> Exception: If the error STATUS == W#16#1Exx occurs, you can examine the SFCERR variable for additional details. This error variable must be loaded via symbolic access to the instance DB.

#### Startup

The COM_RST parameter of S_SEND instruction is used to report a startup to the instruction.

In the startup OB, set parameter COM_RST to 1.

Call the instruction in the cyclic mode without setting or resetting the COM_RST parameter.

If the COM_RST parameter is set:

- The instruction acquires information about the ET 200S 1SI module (number of bytes in the I/O area, whether or not in the distributed I/O).
- The instruction resets itself, while cancelling any job started previously (prior the last CPU transition to STOP).

Once the instruction acquired information about the ET 200S 1SI module, it automatically resets the COM_RST parameter.

#### Time sequence chart

The figure below illustrates the characteristics of the DONE and ERROR parameters, depending on the wiring of the REQ and R inputs.

![Time sequence chart](images/60582717067_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Input REQ is edge-triggered. A positive edge at the input REQ is sufficient. The RLO (result of the logic operation) does not necessarily have to be "1" for the entire duration of the transmission.

#### Rules

> **Note**
>
> The S_SEND instruction has no parameter check. If incorrect parameters are assigned, the CPU can go into STOP mode.

> **Note**
>
> The CPU startup routine of the ET 200S module for the S_SEND instruction must be completed (see above) before the ET 200S 1SI module can execute a job initiated after the status transition of the CPU from STOP to RUN. A job initiated in the meantime is not lost. Once the startup coordination is completed, the job is sent to the ET 200S 1SI module.

---

**See also**

[Data transmission with the ET 200S 1SI Modbus master (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#data-transmission-with-the-et-200s-1si-modbus-master-s7-300-s7-400)

### S_MODB: Modbus slave instruction for ET 200S 1SI (S7-300, S7-400)

#### Description

To enable execution of a Modbus slave job, the S_MODB instruction must be called cyclically in the user program. The S_MODB instruction receives the job from serial interface module ET200S Modbus/USS, executes it and returns the response to the module. Communication between the CPU and module is handled by means of the S_SEND and S_RCV instructions which are called by S_MODB .

#### Operating principle

Following each warm restart of the CPU, the user program must initialize the Modbus communication instruction. Initialization is triggered by a rising edge at the CP_START input. The instruction records the size of the I, Q, F, T and C address areas of the CPU in its instance data block. On successful completion of initialization, the FB sets the CP_START_OK output.

An initialization error is specified by the CP_START_ERROR output. In this case, Modbus communication is not possible and all requests from the Modbus master are answered with an exception code message.

S_MODB uses a Modbus data conversion table that is located in the data block in order to map the Modbus addresses to the SIMATIC S7 memory areas.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LADDR | INPUT | INT | Start address of serial interface module ET 200S 1SI.  The start address is taken from STEP 7. |
| START_TIMER | INPUT | TIMER | Time for initialization timeout:  CPU time that the instruction uses to prevent the initialization from freezing. |
| START_TIME | INPUT | S5TIME | Time value for initialization timeout:  Valid maximum time for the instruction's initialization |
| DB_No | INPUT | BLOCK_DB | Number of the data block that contains the Modbus conversion table:  See the data areas in the SIMATIC CPU |
| OB_MASK | INPUT | BOOL | Masks I/O access errors and delays interrupts:  TRUE can be set to specify that access errors to non-existing I/O are reported to the Modbus master only |
| CP_START | INPUT | BOOL | Start initialization of the instruction |
| CP_START_FM | INPUT | BOOL | Initialization is triggered by a rising edge at the input START:  Memory element to which the instruction saves the previous value of CP_START |
| CP_NDR | OUTPUT | BOOL | Receive order frame |
| CP_START_OK | OUTPUT | BOOL | Initialization successfully completed:   Initialization was completed without errors before expiration of the monitoring time. |
| CP_START_ERROR | OUTPUT | BOOL | Initialization terminated with error:  Initialization could not be completed without errors, even after expiration of the monitoring time. |
| ERROR_NR | OUTPUT | WORD | Error number  See Diagnostics |
| ERROR_INFO | OUTPUT | WORD | Additional error information  See Diagnostics |

#### Allocation in the data area

The S_MODB instruction works in combination with an IDB_MODB instance DB, the number of which is specified in the call.

Access to the data in the instance DB is prohibited.

#### How to Handle an Error

Input parameter OB_MASK can be used to instruct the Modbus instruction to mask I/O access errors. If an attempt is made to write to an I/O that is not available, the CPU does not go into STOP mode or call an error OB. The instruction detects the access error, cancels the job and returns an error response to the Modbus master.

### STATUS parameter (Modbus / USS) (S7-300, S7-400)

#### Event classes

| Event class | Meaning |
| --- | --- |
| 2 | Error initializing |
| 5 | Error executing a CPU job |
| 8 | Receive errors |
| 14 (0E<sub>H</sub>) | General processing errors: Parameter assignment, processing of an S_SEND job. Evaluation of data received, receipt of an exception code message |
| 30 (1E<sub>H</sub>) | Errors in communication between the module and CPU |

#### STATUS parameter

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0201 | No (valid) configuration available. | Provide the module with correct parameters. If necessary, ensure the system is correctly installed. |
| 0502 | Order inadmissible in this operating mode of the serial interface module ET 200S Modbus/USS (example: device interface is not configured). | Evaluate the diagnostic interrupt and rectify the error accordingly. |
| 050E | Invalid telegram length | The send message frame is longer than 224 bytes. The send job was aborted by the ET 200S Modbus/USS module.   Select a shorter telegram length. |
| 0530 | Modbus master send job rejected because the response of the communication partner to a previous reading Modbus master send job has not yet been retrieved. | After a successful read Modbus master send job, you must first read the response from the communication partner from the module before you start a new Modbus master send job. |
| 0551 | Frame sequence errors in the communication between the serial interface module ET 200S Modbus/USS and the CPU. The error occurred while transmitting a received message frame of the ET 200S SI serial interface module to the CPU. | The module and the CPU have canceled the transmission. Repeat the receive job. The ET 200S Modbus/USS serial interface module sends the received message again. |
| 0806 | Character delay time exceeded. Two successive characters were not received within the character delay time. | Partner device too slow or faulty. You can interconnect an interface tester (FOXPG) in the transmission line to debug the partner device. |
| 080A | Overflow of the receive buffer at the master during the reception of the response message frame. | Check the protocol settings of the slave. |
| 080C | Transmission error (parity/stop bit/overflow error) detected. | Disturbances on the data link cause telegram repetitions, thus lowering user data throughput. The risk of undetected error increases. Change your system setup or cable wiring.  Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits. |
| 080D | BREAK: Break in receive line to partner. | Reconnect or switch on partner. |
| 0810 | Parity error: If the SF LED (red) lights up, there is a break in the cable that connects the two communication partners. | Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0811 | Character frame error: If the SF LED (red) lights up, there is a break in the cable that connects the two communication partners. | Check the cables of the communication partners or verify that both devices have matching settings for the baud rate, parity and number of stop bits.  Change your system setup or cable wiring. |
| 0812 | Additional characters were received after the CTS serial port was set to OFF. | Reconfigure the communications partner or fetch from the serial interface faster. |
| 0830 | **Master**: A request message frame has been sent and the response monitoring time has elapsed without the start of a response message frame being detected.   **Slave**: Broadcast not permitted with this function code. | Check if the transmission line has been interrupted (interface analysis may be necessary).   Check that the same settings have been made on the module and communication partner for the following protocol parameters: transmission rate, number of data bits, parity and number of stop bits.   Check that the value for the response monitoring time in PtP_PARAM is large enough.   Check to see if the specified slave address is available.   The Modbus master system is only allowed to use the broadcast function for the function codes enabled for this purpose. |
| 0831 | **Master**: The first character in the slave response message frame is different from the slave address that was sent in the request message frame (for normal operation).   **Slave**: Function code received not permissible. | The wrong slave has responded.  Check if the transmission line has been interrupted (interface analysis may be necessary).  This function code cannot be used for this driver. |
| 0832 | Maximum number of bits or registers exceeded or number of bits cannot be divided by 16 if the SIMATIC timers or counters memory areas are accessed. | Limit the maximum number of bits to 2,040 and the maximum number of registers to 127. Access to SIMATIC timers/counters only in 16-bit intervals. |
| 0833 | Bit or register number for function code FC 15/16 and message frame element byte_count do not match. | Correct the bit/register number or byte_count. |
| 0834 | Illegal bit coding for "Set bit / Reset bit" recognized. | Use only the 0000Hex or FF00Hex codes for FC05. |
| 0835 | Illegal diagnostic subcode (not 0000Hex) at function code FC 08 "Loop back test" recognized. | Use only the subcode 0000Hex for FC08. |
| 0836 | The internally generated value of the CRC 16 checksum does not match the CRC checksum received. | Check the formation of the CRC checksum on the Modbus master system. |
| 0837 | Message frame sequence error: The Modbus master system sent a new request message frame before the driver transmitted the last response message frame. | Increase the timeout on the slave response message frame for Modbus master system. |
| 0850 | Length of the receive message frame greater than 224 bytes or greater than the configured message frame length. | Adjust the message frame length of the partner. |
| 0E20 | This connection requires 8 data bits. The driver is not ready for operation. | Correct the parameter assignment of the driver. |
| 0E21 | The parameterized multiplication factor for the character delay time is not within the range of 1 to 10. The driver is operating with default setting 1. | Correct the parameter assignment of the driver. |
| 0E22 | The operating mode set for the driver is illegal. "Normal operation" or "Noise suppression operation" must be specified. The driver is not ready for operation. | Correct the parameter assignment of the driver. |
| 0E23 | **Master**: An illegal value has been set for the response monitoring time: Valid values are between 50 and 655,000 ms. The driver is not ready for operation.    **Slave**: An illegal value has been set for the slave address. Slave address 0 is illegal.  The driver is not ready for operation. | Correct the parameter assignment of the driver.     Correct the parameter assignment of the driver. |
| 0E2E | An error occurred while the interface parameter file was being read. The driver is not ready for operation. | Restart the master (Mains_ON). |
| 0E40 | The value specified for LEN with S_SEND is too small. | The minimum length is 2 bytes. |
| 0E41 | The value specified for LEN with S_SEND is too small. A greater length is required for the transmitted function code. | The minimum length for this function code is 6 bytes. |
| 0E42 | The transmitted function code is illegal. | Only use permissible function codes. |
| 0E43 | Slave address 0 (= broadcast) is not permissible with this function code. | Only use the slave address 0 with suitable function codes. |
| 0E44 | The value of the "number of bits" transmitted is not within the range of 1 to 2,040. | The "number of bits" must be within the range of 1 to 2,040. |
| 0E45 | The value of the "number of registers" transmitted is not within the range of 1 to 127. | The "number of registers" must be within the range of 1 to 127. |
| 0E46 | Function code 15 or 16: The values of the "number of bits"/"number of registers" transmitted is not in the range of 1 to 2,040 or 1 - 127. | The "number of bits"/"number of registers" must be within the range of 1 to 2,040 or 1 to 127. |
| 0E47 | Function code 15 or 16: LEN for S_SEND does not correspond to the "number of bits"/"number of registers" transmitted.   LEN is too small. | Increase LEN for SEND until enough user data is transmitted to the module.   More user data must be sent to the module because of the "number of bits"/"number of registers". |
| 0E48 | Function code 5: The code specified in the SEND source DB for "set bit" (FF00H) or "delete bit" (0000H) is incorrect. | The only permissible codes are "set bit" (FF00H), "delete bit" or 0000H. |
| 0E49 | Function code 8: The code specified in the SEND source code for "diagnostic code" is incorrect. | The only permissible code is "diagnostic code" 0000H. |
| 0E4A | The length of this function code is greater than the maximum length. | The manual contains the maximum lengths for each function code. |
| 0E50 | The master received a response without sending anything. | A slave or another master is on the network.   Check if the transmission line has been interrupted (interface analysis may be necessary). |
| 0E51 | Function code incorrect:  The function code received in the response message frame is different from the function code sent. | Check the slave device. |
| 0E52 | Byte underflow: The number of characters received is less than indicated by the byte counter of the response message frame or expected for this function code. | Check the slave device. |
| 0E53 | Byte overflow: The number of characters received is greater than indicated by the byte counter of the response message frame or expected for this function code. | Check the slave device. |
| 0E54 | Byte counter incorrect: The byte counter received in the response message frame is too small. | Check the slave device. |
| 0E55 | Byte counter wrong: The byte counter received in the response message frame is wrong. | Check the slave device. |
| 0E56 | Echo incorrect: The response message frame data echoed by the slave (number of bits, etc.) is different from the data sent in the response message frame. | Check the slave device. |
| 0E57 | CRC check incorrect: An error occurred when checking the CRC 16 checksum of the response message frame from the slave. | Check the slave device. |
| 0E61 | Response message frame with exception code 01: Illegal function | Refer to the manual for the slave device. |
| 0E62 | Response message frame with exception code 02: Illegal data address | Refer to the manual for the slave device. |
| 0E63 | Response message frame with exception code 03: Illegal data value | Refer to the manual for the slave device. |
| 0E64 | Response message frame with exception code 04: Failure in associated device | Refer to the manual for the slave device. |
| 0E65 | Response message frame with exception code 05: Acknowledgement | Refer to the manual for the slave device. |
| 0E66 | Response message frame with exception code 06: Occupied; message frame rejected | Refer to the manual for the slave device. |
| 0E67 | Response message frame with exception code 07: Negative acknowledgement | Refer to the manual for the slave device. |
| 1E0D | "Job aborted due to warm restart, hot restart or reset" |  |
| 1E0E | Static error during call of the SFC DP_RDDAT. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E0F | Static error during call of the SFC DP_WRDAT. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E10 | Static error during the call of SFC RD_LGADR. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E11 | Static error during the call of SFC RDSYSST. The RET_VAL return value of the SFC is made available for evaluation in the SFCERR variable at the instance DB. | Load the SFCERR tag from the instance DB. |
| 1E20 | Parameter out of range. | Enter a parameter within the valid range for the instruction. |
| 1E41 | Invalid number of bytes specified at instruction parameter LEN | You must stay within a range of values of 1 to 256 bytes. |

#### Evaluating the SFCERR variable

More detailed information on errors (1E) 0E<sub>H</sub>, (1E) 0F<sub>H</sub>, (1E) 10<sub>H</sub> and (1E) 11<sub>H</sub> belonging to event class 30 can be obtained via the SFCERR variable.

You can load the SFCERR variable from the instance DB of the corresponding instruction.

Error messages entered in the SFCERR variable can be found in the system functions "DPRD_DAT: Read consistent data of a DP standard slave" and SFC15 "DPWR_DAT: Write consistent data of a DP standard slave" and RD_LGADR: Determine all logical addresses of a module.

---

**See also**

[DPRD_DAT: Read consistent data of a DP standard slave](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)
  
[DPWR_DAT: Write consistent data of a DP standard slave](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)
  
[RD_LGADR: Determine all logical addresses of a module](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_lgadr-determine-all-logical-addresses-of-a-module-s7-300-s7-400)

### ERROR_NR, ERROR_INFO parameters (S7-300, S7-400)

#### Error classes for diagnostics

| Error numbers from ... to | Description | Meaning |
| --- | --- | --- |
| 1 ... 9 | Instruction and CP initialization error | Error numbers 1 to 9 indicate that initialization was terminated with errors. The CP_START_ERROR parameter is set to 1.  Modbus communication to the master system is not possible. |
| 10 ... 19 | Error executing a function code | Error numbers 10 to 19 indicate that an error occurred during the processing of a function code. The CP transmitted an invalid execution job to the communication instruction.  The error is also reported to the driver.  Subsequent execution jobs continue to be processed. |
| 90 ... 99 | Other faults/errors | A processing error has occurred.  The error is not reported to the driver.  Subsequent execution jobs continue to be processed. |

#### Error numbers

| ERROR_ No (decimal) | ERROR_INFO | Error Text | Remedy |
| --- | --- | --- | --- |
| 0 | 0 | No error |  |
| 1 | SFC 51->RET_VAL | Error reading the system status list with SFC 51. | Analyze RET_VAL in ERROR_INFO; eliminate the cause. |
| 2 | S_SEND->STATUS, S_RCV->STATUS | Timeout or error during module initialization (error in S_SEND request). | Check if this interface was assigned parameters for operation with "Modbus slave" protocol. Verify the "ID" specified in the communication instruction. Analyze ERROR_INFO. |
| 11 | Start address | The driver transferred an invalid start address to the communication instruction. | Check the Modbus address of the Modbus master system. |
| 12 | Number of registers | The driver transferred an invalid number of registers to the communication instruction.  Number of registers = 0. | Check the number of registers of the Modbus master system. If necessary, restart the module (Mains_ON). |
| 13 | Number of registers | The driver transferred an invalid number of registers to the communication instruction:  Number of registers > 128. | Check the number of registers of the Modbus master system. If necessary, restart the module (Mains_ON). |
| 14 | Bit memory M –  End address | Attempt to access the SIMATIC flags memory area beyond the end of the area. Notice: The area length in the SIMATIC CPU depends on the type of CPU. | Reduce the length of the Modbus start address or the access length in the Modbus master system. |
| 15 | Outputs Q –  End address    Inputs I –  End address | Attempt to access the SIMATIC outputs memory area beyond the end of the area. Notice: The area length in the SIMATIC CPU depends on the type of CPU. | Reduce the length of the Modbus start address or the access length in the Modbus master system. |
| 16 | Timers T –  End address | Attempt to access the SIMATIC timers memory area beyond the end of the area. Notice: The area length in the SIMATIC CPU depends on the type of CPU. | Reduce the length of the Modbus start address or the access length in the Modbus master system. |
| 17 | Counters C – End address | Attempt to access the SIMATIC counters memory area beyond the end of the area. Notice: The area length in the SIMATIC CPU depends on the type of CPU. | Reduce the length of the Modbus start address or the access length in the Modbus master system. |
| 18 | 0 | The driver transferred an invalid SIMATIC memory area to the communication instruction. | If necessary, restart the module (Mains_ON). |
| 19 |  | Error during access to SIMATIC I/Os. | Check if the required I/Os exist and are error-free. |
| 20 | DB# | DB does not exist. | Add the DB to your project. |
| 21 | DB# | DB length invalid | Increase the DB length. |
| 22 | DB# | DB# is below the minimum DB value. | Change the minimum DB value. |
| 23 | DB# | DB# is above the maximum DB value. | Change the maximum DB value. |
| 24 | Flag address | Flag is below the lower limit. | Change the lower limits of the flags in the conversion DB. |
| 25 | Flag address | Flag is above the upper limit. | Change the upper limits of the flags in the conversion DB. |
| 26 | Output address | Output is below the lower limit. | Change the lower limits of the outputs in the conversion DB. |
| 27 | Output address | Output is above the upper limit. | Change the upper limits of the outputs in the conversion DB. |
| 90 | S_SEND-> STATUS | Error during transmission of an acknowledgement message frame to the driver with S_SEND. | Analyze the STATUS information. |
| 94 | S_RCV->STATUS | Error reading SYSTAT with S_RCV (STATUS). | Analyze the STATUS information. |

## ET 200S 1SI for USS (S7-300, S7-400)

This section contains information on the following topics:

- [S_USST: Send data to a USS slave (S7-300, S7-400)](#s_usst-send-data-to-a-uss-slave-s7-300-s7-400)
- [S_USSR: Receive data from a USS slave (S7-300, S7-400)](#s_ussr-receive-data-from-a-uss-slave-s7-300-s7-400)
- [S_USSI: Initialize USS (S7-300, S7-400)](#s_ussi-initialize-uss-s7-300-s7-400)
- [Network data DB (S7-300, S7-400)](#network-data-db-s7-300-s7-400)
- [Network data DB (S7-300, S7-400)](#network-data-db-s7-300-s7-400-1)
- [Communication processor DB (S7-300, S7-400)](#communication-processor-db-s7-300-s7-400)

### S_USST: Send data to a USS slave (S7-300, S7-400)

#### Description

The S_USST instruction handles the transmission of network data (PZD and any PKW data) to the slaves, depending on the network data structure used.

#### Operating principle

The instruction fetches the parameter assignment of the current slave from the polling list (parameter DB) and transmits the data from the network data DB. It evaluates the communication control word of the current slave (triggering of a PKW request/acknowledgement of a parameter change report), completes the USS transmit data and transmits it to the send buffer of the communications processor DB. It then initiates network data transmission to the slave by calling the S_SEND instruction.

If the instruction detects a parameter assignment error in the parameter DB, an error signal is stored in the parameter assignment error 2 byte of the network data DB.

The instruction is called once per automation system cycle.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DBPA | INPUT | INT | Block number of the parameter DB  CPU-specific (zero is not allowed) |
| SYPA | INPUT | INT | Start address of the system parameters in the parameter DB  0 <= SYPA <= 8174 |
| SLPA | INPUT | INT | Start address of the slave parameters in the parameter DB  0 <= SLPA <= 8184 |

#### Program structure of S_USST

![Program structure of S_USST](images/21526520331_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of USS communication (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#overview-of-uss-communication-s7-300-s7-400)

### S_USSR: Receive data from a USS slave (S7-300, S7-400)

#### Description

The S_USSR instruction handles the receipt of network data (PZD and any PKW data) from the slaves, depending on the network data structure used.

#### Operating principle

The instruction fetches the parameter assignment of the current slave from the polling list (parameter DB) and evaluates the status word of the TRANSMIT block.

If the current request has been terminated without errors (bit 9 = 0 in the communication status word of the network data DB), the incoming data from the receive buffer of the communications DB is transmitted to the network data DB and evaluated. The communication status word is then updated in the network data DB.

If the current request has been terminated with an error (bit 9 = 1 in the communication status word of the network data DB), the data of the current slave is not accepted from the receive buffer of the communications processor DB. The instruction specifies this in the communication status word of the network data DB and enters the cause of error in the communication error word.

If the block detects a parameter assignment error in the parameter DB, an error signal is stored in the parameter assignment error 1 byte of the network data DB.

The instruction is called once per automation system cycle.

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DBPA | INPUT | INT | Block number of the parameter DB  CPU-specific (zero is not allowed) |
| SYPA | INPUT | INT | Start address of the system parameters in the parameter DB  0 <= SYPA <= 8174 |
| SLPA | INPUT | INT | Start address of the slave parameters in the parameter DB  0 <= SLPA <= 8184 |

#### Program syntax of S_USSR

The diagram below shows the program syntax of S_USSR.

![Program syntax of S_USSR](images/21541470219_DV_resource.Stream@PNG-en-US.png)

#### Rule

> **Note**
>
> The parameters of the U_USST instruction correspond to the parameters of the S_USSR instruction. The two functions access the same configuration (system and slave parameters) in the parameter DB and, consequently, have to be assigned identical parameters.

---

**See also**

[Overview of USS communication (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#overview-of-uss-communication-s7-300-s7-400)

### S_USSI: Initialize USS (S7-300, S7-400)

#### Description

The S_USSI instruction is an optional function.

Call of this instruction during the startup of the S7 system initiates the generation of the communications processor DB, network data DB and parameter DB. These data blocks are indispensible for communication. The DBPA is also preset. The S_USSI instruction can be used to generate and preset the specified data area, provided all slaves have the same network data structure.

> **Note**
>
> If you do not use S_USSI, you have to pre-assign a value (e.g., 20000) to DMW 2 in the communications processor DB.

> **Note**
>
> **S_USSI on S7‑1500**
>
> Note the following when using the S_USSI instruction of the distributed I/O ET 200S 1SI on an S7‑1500.
>
> The parameter ANZ shows the value 0 even in the case of an error.
>
> If the CPU is switched to STOP with the S_USSI instruction, check all possible errors listed at the parameter ANZ.

#### Operating principle

When called, the instruction first checks the plausibility of its parameter assignment in terms of the number of slaves, network data structure, start node number and PKW repetitions. If the block detects an error during this, the data blocks are not generated or preset. The CPU goes into STOP mode and the user receives an error message via the error byte of the S_USSI instruction. Once the parameter error has been eliminated, all data blocks that have already been generated must be deleted before a restart.

After the plausibility check, the block checks whether the data blocks to be generated already exist:

- If the data blocks to be generated do not already exist, they are generated and the DBPA is preset.
- If the data blocks to be generated already exist, the length of each data block is checked. If the DB is long enough, the parameter DB is preset again and the contents of the network data DB and the communications processor DB are deleted. If a DB is too short, the CPU goes into STOP mode. You can identify the faulty DB by the condition code byte of the S_USSI instruction. For the error to be eliminated, the three data blocks must be completely deleted. The data blocks are then generated again at the next restart and the parameter DB is preset.

The S_USSI instruction must be called once during system startup (OB 100).

#### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| SANZ | INPUT | INT | Number of slaves with the same network data structure (system parameters in the DBPA)  1 ≤ SANZ ≤ 31 |
| TNU1 | INPUT | INT | Start node number (station number)  0 ≤ TNU1 ≤ 31 |
| PKW | INPUT | INT | PKW, number  Number of words of the PKW interface 0, 3 or 4 |
| PZD | INPUT | INT | PZD, number  Number of words of PZD interface  0 <= PZD <= 16 |
| DBND | INPUT | INT | Network data DB number  CPU-specific (zero is not allowed)  Permitted range: 60000 to 60999 |
| DBPA | INPUT | INT | Parameter DB number  CPU-specific (zero is not allowed)  Permitted range: 60000 to 60999 |
| DBCP | INPUT | INT | Communications processor DB number  CPU-specific (zero is not allowed)  Permitted range: 60000 to 60999 |
| WDH | INPUT | INT | Number of permissible PKW request repetitions  0 ≤ WDH ≤ 32767 |
| ANZ | OUTPUT | BYTE | Error byte  0: No error  1: Too many slaves  2: Invalid data for the network data structure  3: Configuration DB: Invalid number or DB too short  4: Network DB: Invalid number or DB too short  5: Incorrect station number  6: Communication processor DB: Invalid number or DB too short  7: Free  8: Repetition counter: Incorrect value |

---

**See also**

[Overview of USS communication (S7-300, S7-400)](Configuration%20for%20point-to-point%20links%20%28S7-300%2C%20S7-400%29.md#overview-of-uss-communication-s7-300-s7-400)

### Network data DB (S7-300, S7-400)

#### Description

The network data DB forms the interface between the communication and control programs. The user must make this block available as "empty" and it must be sufficiently long.

#### Operating principle

You can generate and preset these blocks by calling the S_USSI instruction during CPU startup (DBPA only) or enter them manually.

Only the transmit data for a slave is entered in the network data DB send buffer that is assigned to the slave by the control program. The response data from the slave is accepted from the appropriate reception buffer (after evaluation of bit 9 in the communication control word). Status words can be used to precisely monitor communication, while the control word allows you to precisely control the beginning of a parameter assignment request.

**The communication interface contains the following data for each slave:**

- Slave-related communication data (communication control, tracking, 6 data words)
- Buffer for the current PKW job (only if a PKW area exists)
- Send buffer for network data (maximum of 20 data words)
- Reception buffer for network data (maximum of 20 data words)

The lengths of the send and receive buffer depend on the network data structure selected. If the PKW interface does not exist, the buffer for the current PKW job is not used.

The total length of the network data DB required depends on the number of slaves and the network data structure used.

Number of data words per slave = 2 x (PKW + PZD) + PKW + 6

where PKW = 0, 3 or 4 and 0 <= PZD <= 16

**Example**: A drive with a PKW area of 3 words and a PZD area of 2 words requires 19 data words in the network data DB.

With 31 slaves and the maximum network data length, the network data DB is 1,550 data words long. DBW0 is reserved.

#### Slave data assignment in the network data DB with 4 words in the PKW area and 0 to 16 words in the PZD area.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DBWn | Internal |  | Communication control    Communication tracking  Error status  PKW attempt counter  Parameter error |  |
| DBWn+2 | Communication control word (KSTW) |  |  |  |
| DBWn+4 | Communication status word |  |  |  |
| DBWn+6 | Communication error word |  |  |  |
| DBWn+8 | Internal |  |  |  |
| DBWn+10 | Parameter error 1 byte, parameter error 2 byte |  |  |  |
| DBWn+12 | Parameter ID | PKE | Buffer for current  PKW job |  |
| DBWn+14 | Index | IND |  |  |
| DBWn+16 | Parameter value 1 | PWE1 |  |  |
| DBWn+18 | Parameter value 2 | PWE2 |  |  |
| DBWn+20 | Parameter ID | PKE | PKW area | Send buffer |
| DBWn+22 | Index | IND |  |  |
| DBWn+24 | Parameter value 1 | PWE1 |  |  |
| DBWn+26 | Parameter value 2 | PWE2 |  |  |
| DBWn+28 | Control word (STW) | PZD1 | PZD area  (max. 16 words PZD) |  |
| DBWn+30 | Main setpoint (HSW) | PZD2 |  |  |
| DBWn+32 | Setpoint/Additional control word | PZD3 |  |  |
| DBWn+34 | Setpoint/Additional control word | PZD4 |  |  |
| ... | ... |  |  |  |
| DBWn+58 | Setpoint/Additional control word | PZD16 | PKW area | Receive buffer |
| DBWn+60 | Parameter ID | PKE |  |  |
| DBWn+62 | Index | IND |  |  |
| DBWn+64 | Parameter value 1 | PWE1 |  |  |
| DBWn+66 | Parameter value 2 | PWE2 |  |  |
| DBWn+68 | Status word (ZSW) | PZD1 | PZD area  (max. 16 words PZD) |  |
| DBWn+70 | Main process value (HIW) | PZD2 |  |  |
| DBWn+72 | Process value/Additional status word | PZD3 |  |  |
| DBWn+74 | Process value/Additional status word | PZD4 |  |  |
| ... | ... |  |  |  |
| DBWn+98 | Process value/Additional status word | PZD16 |  |  |
|  | • |  |  |  |
| (n = 2, 4 , 6...) | • |  |  |  |

> **Note**
>
> If there is no PKW area, neither the buffer for current PKW jobs nor the PKW area in the send buffer exists.

#### Communication control word KSTW (DBWn)

The bits in the communication control word coordinate the user program and the S_USST instruction.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

- Bit 0: Triggers the PKW job

  Bit 0 is set by the user if a new PKW job is in the send buffer and is to be processed. The instruction resets the bit if the PKW job is accepted.
- Bit 1: Acceptance of parameter change report

  Bit 1 is set by the user if the parameter change report has been accepted. The instruction resets the bit in order to acknowledge acceptance. Following this acknowledgement, the slave either continues to process the current job or transmits the next parameter change report.

#### Communication status word (DBWn+4)

The S_USST and S_USSR instructions set the bits in the communication status word.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

- Bit 0: PKW job in progress

  If the PKW job was accepted and the parameter ID (PKE) contains a valid job ID, instruction S_USST sets the bit to 0. Instruction S_USSR resets the bit after the PKW job has been executed (with or without errors) or if there are problems with the PKW interface.
- Bit 1: PKW job completed without errors

  Instruction S_USSR sets bit 1 if a PKW job has been executed without errors. The response should be taken from the receive buffer. Instruction S_USST resets the bit when a new PKW job is initiated.

  > **Note**
  >
  > The PKW jobs for the slave are processed in the order specified in the polling list (DBPA). Only one job is active for each slave at any one time. If more than one slave is entered in the polling list, the response data for a new PKW job is only available on a positive edge of bit 1 (or bit 2).
- Bit 2: PKW job completed with errors

  Instruction S_USSR sets bit 2 for the response ID in the PKE. The error number is in the PWE of the slave response. Instruction S_USST resets the bit when a new PKW job is initiated.

  > **Note**
  >
  > The last PKW job transmitted by the user is stored in the send interface after processing. Transmission to the slave is repeated until a new job is entered. This might require additional responses in the user program in the event of the status PKW job being terminated with an error (bit 2) and a PKW interface error (bit 4).
- Bit 3: PKW job ID is invalid.

  Instruction S_USST sets bit 3 if job ID 15 is set in the PKE or index 255 is entered in job ID 4. Instruction S_USST resets the bit if the next PKW job is triggered with a valid job ID in the PKE.
- Bit 4: PKW interface with an error (counter overflow).

  Instruction S_USSR sets bit 4 if the slave does not respond to the PKW job within a configurable number of job repetitions (WDH parameter in the parameter DB) or in the case of response ID 8 in the PKE. Instruction S_USSR resets the bit when a new PKW job is initiated and correctly executed.
- Bit 5: Response data contains a parameter change report.

  Instruction S_USSR sets bit 5 if a parameter change report from the slave is present (response IDs 9 to 12 and toggle bit 11 inverted). Instruction S_USST resets the bit when the user acknowledges the parameter change report (communication control word, bit 1).
- Bit 6: Operational fault on the slave.

  Instruction S_USSR sets and resets bit 6. The instruction evaluates the slave's status word (bit 3).
- Bit 7: There is a warning from the slave.

  Instruction S_USSR sets and resets bit 7. The instruction evaluates the slave's status word (bit 7).
- Bit 8: Automation system control requested.

  Instruction S_USSR sets and resets bit 8. The instruction evaluates the status word (bit 9) and the control word (bit 10).
- Bit 9: Group communication fault.

  Instruction S_USSR sets and resets bit 9. The instruction evaluates the feedback messages from the S_SEND and S_RCV standard blocks and checks the message frame received with respect to ADR, STX, BCC and LGE. The instruction also reports a timeout of the message frame monitoring time.

  > **Note**
  >
  > The receive data from the network data DB is only valid where bit 9 = 0.

#### Structure of the communication error word (DBWn+6)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

- Bit 0: Addressing error (ADR)
- Bit 3: Start of message frame not detected (no STX for first character)
- Bit 4: Incorrect block check character (BCC)
- Bit 6: Incorrect message frame length (LGE)

  Instruction S_USSR sets bits 0, 3, 4 and 6 if an error is detected in the received frame (ADR, STX, BCC, LGE).
- Bit 7: Message frame monitoring time has elapsed

  Instruction S_USSR sets bit 7 if the time between the transmission of the message frame from the master to the slave and the arrival of the response from the slave exceeds the valid time calculated by the program (frame monitoring time).

The remaining bits are not used.

#### Parameter error 1 byte

Error message from the S_USSR instruction, parameter assignment error in parameter DB

- Value 0: No error
- Value 1: Incorrect data for PKW/PZD

#### Parameter error 2 byte

Error message from the S_USSR instruction, parameter assignment error in parameter DB

- Value 0: No error
- Value 1: Incorrect data for PKW/PZD

#### Parameter ID PKE in the send buffer

The user must assign the parameter number (bits 0 to 10) and the job ID (bits 12 to 15). The toggle bit for the parameter change report (bit 11) is masked by the S_USSR and S_USST instructions.

### Network data DB (S7-300, S7-400)

#### Description

The arameter DB contains the program parameters required for communication control. The user needs to generate this block and set suitable defaults for the communication system (S_USSI or manually). The slaves on the bus are processed in the sequence in which they are entered in the DBPA (polling list).

A slave can also be entered more than once in the parameter DB in order to effectively step up its priority class.

#### Operating principle

The length of the parameter DB depends on the number (n) of slaves to be addressed in a bus cycle.   
Number of data words of the parameter DB = (n x 4) + 5.

4 data words are required for each instance of slave communication and 4 data words are assigned once for the system parameters. DBW0 is reserved.

#### Data block allocation

|  |  |  |
| --- | --- | --- |
| DBW 0 | Free | System parameters |
| DBW 2 | DBCP |  |
| DBW 4 | SANZ |  |
| DBW 6 | SLAV |  |
| DBW 8 | WDH |  |
| DBW 10 | Number of PKW, number of PZD | Communications  Parameter set slave 1 |
| DBW 12 | TUN |  |
| DBW 14 | DBND |  |
| DBW 16 | KSTW |  |
| DBW 18 | Number of PKW, number of PZD | Communications  Parameter set slave 2 |
| DBW 20 | TUN |  |
| DBW 22 | DBND |  |
| DBW 24 | KSTW |  |
|  |  |  |
|  |  |  |
|  | Number of PKW, number of PZD | Communications  Parameter set slave n |
|  | TUN |  |
|  | DBND |  |
| DBW (n x 8 + 8) | KSTW |  |

#### System parameters

| Symbol | Meaning |
| --- | --- |
| DBCP | Block number of the communications processor DB |
| SANZ | Total number of slave parameter sets in the parameter DB. If some individual slaves are to be addressed more frequently than others in a bus cycle, their slave parameters must be entered more than once in the parameter DB. The SANZ system parameter must be adjusted accordingly. |
| SLAV | Number of the current slave (consecutive). Required by the S_USST FC and the S_USSR FC to calculate the current parameter set. This data word must be preset to 1. This is carried out by the S_USSI FC, if it is being used. |
| WDH | Number of permissible PKW job repetitions (value range: 0 through 32,767). If the current PKW job is not terminated within the set number, problems at the PKW interface are reported. |

#### Slave communication parameter

| Symbol | Meaning |
| --- | --- |
| Number of PKW, number of PZD | Definition of network data structure Left byte: Number of words for PKW area (0, 3, 4) Right byte: Number of words for PZD area (0 to 16)   Any deviations from this are detected as parameter assignment errors (by the S_USST and S_USSR FCs) and entered in the parameter assignment error 1 byte, parameter assignment error 2 byte of the network data DB. |
| TUN | Node number corresponding to the bus address set on the drive (0 to 31). |
| DBND | Block number of the network data DB. |
| KSTW | Address of the communication control word KSTW for the slave in the network data DB. |

### Communication processor DB (S7-300, S7-400)

#### Description

This data block is used to handle data traffic between the CPU and serial interface module ET 200S Modbus/USS. Provide this block with a sufficient length. The communication processor DB must have a length of at least 50 words (DBW 0 to 98).

#### Syntax of the communication processor DB

|  |  |  |  |
| --- | --- | --- | --- |
| DBW 0 | Communication status |  | SEND and RECEIVE  FC17        FC17  FC17, OB1    SEND |
| DBW 2 | Maximum number of cycles to expire when waiting to receive data | Cycle counter for timeout formation when waiting to receive data |  |
| DBW 4 | Measured start interval |  |  |
| DBW 6 | Duration of the last cycle (OB1_MIN_CYCLE) |  |  |
| DBW 8 | Transmission frame length (LEN) |  |  |
| DBB10 | Free |  |  |
| DBB 11  :  :  DBB 54 | Send buffer |  | Send frame to module  (length is determined by the network data structure of the current slave) |
| DBB 55  :  :  DBB 98 | Receive buffer |  | Received frame from module (length is determined by the network data structure of the current slave) |

#### Communication status DBW0

| Bit no. |  |  |
| --- | --- | --- |
| 0 | Input REQ for S_SEND | This bit is reset if bit 8 is set. |
| 1 | Input R for S_SEND | S_USST resets this bit at cyclic intervals. |
| 2 | Output DONE of S_SEND |  |
| 3 | Output ERROR of S_SEND |  |
| 4 | Input EN_R for S_RCV | S_USSR sets this bit at cyclic intervals. |
| 5 | Input R for S_RCV | S_USSR resets this bit at cyclic intervals. |
| 6 | Output NDR of S_RCV |  |
| 7 | Output ERROR of S_RCV |  |
| 8 | Job in progress (S_SEND saves the DONE bit) | S_USST resets this bit at cyclic intervals. |

#### Duration of the last cycle DBW6

S_USST uses this parameter to measure slave response times. Before each call of S_USST , the user program must copy the cycle time of the automation system (OB1_MIN_CYCLE) to this parameter.

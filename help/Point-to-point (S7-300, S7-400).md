---
title: "Point-to-point (S7-300, S7-400)"
package: ProgFBCMPtP34enUS
topics: 17
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Point-to-point (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of Freeport communication (S7-300, S7-400)](#overview-of-freeport-communication-s7-300-s7-400)
- [Using the instructions (S7-300, S7-400)](#using-the-instructions-s7-300-s7-400)
- [General parameters for Freeport operations (S7-300, S7-400)](#general-parameters-for-freeport-operations-s7-300-s7-400)
- [Port_Config: Configure PtP communication port (S7-300, S7-400)](#port_config-configure-ptp-communication-port-s7-300-s7-400)
- [Send_Config: Configure PtP sender (S7-300, S7-400)](#send_config-configure-ptp-sender-s7-300-s7-400)
- [Receive_Config: Configure PtP recipient (S7-300, S7-400)](#receive_config-configure-ptp-recipient-s7-300-s7-400)
- [P3964_Config: Configuring the 3964(R) protocol (S7-300, S7-400)](#p3964_config-configuring-the-3964r-protocol-s7-300-s7-400)
- [Send_P2P: Sending data (S7-300, S7-400)](#send_p2p-sending-data-s7-300-s7-400)
- [Using the BUFFER and LENGTH parameters for communication operations (S7-300, S7-400)](#using-the-buffer-and-length-parameters-for-communication-operations-s7-300-s7-400)
- [Receive_P2P: Receiving data (S7-300, S7-400)](#receive_p2p-receiving-data-s7-300-s7-400)
- [Receive_Reset: Clear receive buffer (S7-300, S7-400)](#receive_reset-clear-receive-buffer-s7-300-s7-400)
- [Signal_Get: Read status (S7-300, S7-400)](#signal_get-read-status-s7-300-s7-400)
- [Signal_Set: Set accompanying signals (S7-300, S7-400)](#signal_set-set-accompanying-signals-s7-300-s7-400)
- [Get_Features: Get extended functions (S7-300, S7-400)](#get_features-get-extended-functions-s7-300-s7-400)
- [Set_Features: Set extended functions (S7-300, S7-400)](#set_features-set-extended-functions-s7-300-s7-400)
- [Error messages (S7-300, S7-400)](#error-messages-s7-300-s7-400)

## Overview of Freeport communication (S7-300, S7-400)

STEP 7 offers extended instructions that can be used for Freeport communication with a protocol specified in the user program. These instructions can be divided into two categories:

- Configuration instructions
- Communication instructions

### Data communication

Two types of data exchange between the CPU and the communication module are possible with the communication modules:

- Acyclic data exchange (Universal)

  The Freeport instructions communicate with the communication module asynchronously by reading or writing data records.

  Data transmission takes place across several cycles.

  > **Note**
  >
  > **CPU configuration limits**
  >
  > When using the instructions with asynchronous communication, you should take into account the configuration limits of the respective CPU for reading and writing data records. If multiple instructions need to read or write data records simultaneously on a CPU, there may need to be a gap between the calls of each instruction by the user program.
- Cyclic data exchange (Performance optimized for many short frames)

  The Freeport instructions communicate with the communication module synchronously with the application cycle via the IO data of the communication module. Using cyclic data optimizes the reaction time, especially if you are using several CM PtPs in parallel.

  > **Note**
  >
  > Cyclic data exchange is available with the instruction library PtP-Communication as of V4.0.

### Configuration instructions

Before the user program can start the Freeport communication, the communication interface and the parameters for sending and receiving of data must be configured.

The interface configuration and the data configuration can be set for each CM in the device configuration or with the following instructions of your user program:

- [Port_Config](#port_config-configure-ptp-communication-port-s7-300-s7-400)
- [Send_Config](#send_config-configure-ptp-sender-s7-300-s7-400)
- [Receive_Config](#receive_config-configure-ptp-recipient-s7-300-s7-400)
- [P3964_Config](#p3964_config-configuring-the-3964r-protocol-s7-300-s7-400)

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Device configuration <-> Configuration instructions**  The device configuration parameters are transferred to the CM upon each Power On of the CPU (return of voltage).   The parameters of the configuration instructions are transferred to the CM as defined in your user program.  The parameters of the device configuration are not synchronized with the parameters of the configuration instructions, which means the parameters of the configuration instructions are not applied to the CPU device configuration.  With your user program, you determine the parameters that apply in the CM and when they apply. |  |

### Communication instructions

The user program uses the instructions for Freeport communication to send data to and receive data from the communication interfaces. The CMs send data to and receive data from the communication stations.

- [Send_P2P](#send_p2p-sending-data-s7-300-s7-400)
- [Receive_P2P](#receive_p2p-receiving-data-s7-300-s7-400)

> **Note**
>
> **Data consistency**
>
> - If the data to be sent is transmitted consistently, it cannot be changed after the positive edge at the REQ parameter until DONE has been set by the Send_P2P instruction.
> - If the receive data is to be read consistently, it may only be evaluated in the cycle in which NDR = TRUE.

The receive buffer can be reset with additional instructions and special RS232 signals can be queried and set.

- [Receive_Reset](#receive_reset-clear-receive-buffer-s7-300-s7-400)
- [Signal_Get](#signal_get-read-status-s7-300-s7-400)
- [Signal_Set](#signal_set-set-accompanying-signals-s7-300-s7-400)

The following instructions let you read or write extended functions, as long as these are supported by the module.

- [Get_Features](#get_features-get-extended-functions-s7-300-s7-400)
- [Set_Features](#set_features-set-extended-functions-s7-300-s7-400)

All Freeport instructions work asynchronously. The instructions must therefore be called until the DONE or NDR output parameter indicates that the execution is complete.

The user program can determine the send and receive status with the help of the query architecture. Send_P2P and Receive_P2P can be run at the same time. The communication modules buffer the send and receive data as required until a module-specific maximum buffer size has been reached.

> **Note**
>
> **Resolution of bit times**
>
> The number of bit times is specified with the configured data transmission rate for different parameters. Specifying the parameter in bit times makes it independent of the data transmission rate. All parameters with unit of bit times can be specified with a maximum number of 65535.

## Using the instructions (S7-300, S7-400)

The Freeport instructions must be called cyclically to query received data or the end of transmission for a send process.

Depending on the data volume and on whether the Performance option has been activated, data transmission may take place over several calls (program cycles).  
If a command is completed with DONE = TRUE or NDR = TRUE, it has been executed without errors.

> **Note**
>
> **Backing up STATUS**
>
> The DONE, NDR, ERROR and STATUS parameters are only available for one block cycle. To display the STATUS, you should therefore copy it to a free data area.

### Master

Typical sequence for a master:

1. The Send_P2P instruction triggers transmission to the CM.   
   Data transmission is initiated by a positive edge at the REQ input.
2. The Send_P2P instruction is executed in subsequent cycles to query the status of the transmission process.
3. When the Send_P2P instruction signals that transmission is complete at the DONE output, the user code can prepare the receipt of the answer.
4. The Receive_P2P instruction is run repeatedly to query an answer. If the CM has acquired response data, the Receive_P2P instruction copies the response to the CPU and signals that new data has been received at the NDR output.
5. The user program can process the response.
6. Back to step 1 and repetition of the sequence.

### Slave

Typical sequence for a slave:

1. The user program runs the Receive_P2P instruction in each cycle.
2. If the CM has received a request, the Receive_P2P signals that new data is available at the NDR output and the request is copied to the CPU.
3. The user program processes the request and creates a response.
4. The response is returned to the master with the Send_P2P instruction.
5. The Send_P2P instruction must be run repeatedly to ensure that the send process is actually taking place.
6. Back to step 1 and repetition of the sequence.

The slave must ensure that Receive_P2P is called up often enough so that a transmission can be received by the master before it cancels the process due to a timeout while waiting for the response. To do so, the user program Receive_P2P can be called from within a cycle OB whose cycle time is sufficiently short so that the master can receive a transmission before the timeout setting expires. If the OB cycle time is set so that two runs can take place during the timeout setting of the master, the user program can receive all transmissions without any losses.

## General parameters for Freeport operations (S7-300, S7-400)

General input parameters of the Freeport instructions

| Parameter | Description |
| --- | --- |
| REQ | Data transmission is initiated by a positive edge at the REQ input. Another edge at REQ may only be generated after the command has been completed (DONE or ERROR). Data transmission can take several calls (program cycles), depending on the data volume.  When you add a Freeport instruction to your program, STEP 7 prompts you to specify the instance DB (or to have STEP 7 create a corresponding instance DB). Use a unique DB for each PtP instruction call. |
| PORT | A port address is assigned during configuration of the communication module. The PORT parameter communicates assignment to a specific communication module to the instruction.  You can select a symbolic name for the standard port after the configuration. The assigned CM port value is the "Hardware ID" property of the device configuration with S7-1200/1500 and the "Input address" with S7-300/400. The symbolic port name is assigned in the symbol table. |

The output parameters DONE, NDR, ERROR and STATUS of the Freeport instructions indicate the execution status of the Freeport functions.

Output parameters DONE, NDR, ERROR and STATUS

| Parameter | Data type | Standard | Description |
| --- | --- | --- | --- |
| DONE | Bool | FALSE | Set to TRUE for one cycle to indicate that the last request was completed with errors; otherwise FALSE. |
| UNIVERSAL <sup>1)</sup> | Bool | FALSE | Type of data communication between the CPU and the CM specified via PORT:  FALSE: Performance optimization (cyclic)  - Receive frames max. 24 bytes - Send frames max. 30 bytes   TRUE: Universal (acyclic)  - Limiting the frame length depending on the CM to 1, 2, or 4 KB |
| NDR | Bool | FALSE | Set to TRUE for one cycle to indicate that new data has been received; otherwise FALSE. |
| ERROR | Bool | FALSE | Set to TRUE for one cycle to indicate that the last request was completed with errors; the corresponding error code can be found in STATUS; otherwise FALSE. |
| STATUS | Word | 16#0000 or 16#7000 | Result status:  - If the DONE or NDR bit is set, STATUS is set to 0/16#7000 or to a specific status code. - If the ERROR bit is set, STATUS displays an error code. - If none of the bits listed above is set, the instruction can return status results that describe the current status of the function.   The value in STATUS is valid until you call this instruction again (with one and the same port address). |
| <sup>1)</sup> Available from library version V4.0 |  |  |  |

In/out parameter COM_RST

| Parameter | Data type | Standard | Description |
| --- | --- | --- | --- |
| COM_RST | Bool | FALSE | Initialization of the instruction   The instruction is initialized with TRUE. COM_RST is then set back to FALSE.  Note: You must set COM_RST to TRUE during startup and should not subsequently change the parameter (that is, do not assign a value when you call the instruction). COM_RST is reset by the instruction following initialization of the instance DB. |

> **Note**
>
> Please note that the parameters DONE, NDR, ERROR and STATUS are only set for one cycle.

Shared error codes

| Error code | Description |
| --- | --- |
| 16#0000 | No error |
| 16#7000 | Function not active |
| 16#7001 | Initial call after request started. |
| 16#7002 | Subsequent call after request started. |
| 16#8x3A | Invalid pointer in parameter x |

Shared error classes of the STATUS parameter

| Description of the class | Error classes | Description |
| --- | --- | --- |
| Port configuration | 16#81Ax | For the description of frequent errors in the interface configuration |
| Send configuration | 16#81Bx | For the description of errors in the send configuration |
| Receive configuration | 16#81Cx | For the description of errors in the receive configuration |
| Sending | 16#81Dx | For the description of runtime errors during sending |
| Receiving | 16#81Ex | For the description of runtime errors during receiving |
| RS232 accompanying signals | 16#81Fx | For the description of errors in connection with signal processing |

## Port_Config: Configure PtP communication port (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Port_Config instruction (port configuration) allows you to change parameters such as the data transmission rate in runtime using your program. The data pending in the CM is deleted with the execution of Port_Config.

Configuration changes of Port_Config are saved on the CM and not in the CPU. When the voltage returns, the CM is configured with the data saved in the device configuration.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the transmission of data to the CM upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| PROTOCOL | IN | UInt | Word | 0 | Protocol  - 0 = Freeport protocol - 1 = Protocol 3964(R) |
| BAUD | IN | UInt | Word | 6 | Data transmission rate of the port:  - 1 = 300 bps - 2 = 600 bps - 3 = 1200 bps - 4 = 2400 bps - 5 = 4800 bps - 6 = 9600 bps - 7 = 19200 bps - 8 = 38400 bps - 9 = 57600 bps - 10 = 76800 bps - 11 = 115200 bps - 12 = 250000 bits/s |
| PARITY | IN | UInt | Word | 1 | Parity of the port:  - 1 = no parity - 2 = even parity - 3 = odd parity - 4 = mark parity - 5 = space parity - 6 = any |
| DATABITS | IN | UInt | Word | 1 | Bits per character:  - 1 = 8 data bits - 2 = 7 data bits |
| STOPBITS | IN | UInt | Word | 1 | Stop bits:  - 1 = 1 stop bit - 2 = 2 stop bits |
| FLOWCTRL | IN | UInt | Word | 1 | Flow control:  - 1 = no flow control - 2 = XON/XOFF - 3 = Hardware RTS always ON - 4 = Hardware RTS switched - 5 = Hardware RTS always ON, ignore DTR/DSR |
| XONCHAR | IN | Char |  | 16#0011 | Specifies the character that serves as XON character. It is typically a DC1 character (11H). This parameter is only evaluated when software flow control is active. |
| XOFFCHAR | IN | Char |  | 16#0013 | Specifies the character that serves as XOFF character. It is typically a DC3 character (13H). This parameter is only evaluated when software flow control is active. |
| WAITIME | IN | UInt | Word | 2000 | Specifies how long to wait for an XON character after receipt of an XOFF character or how long to wait for a CTS = ON signal after CTS = OFF (0 to 65535 ms). This parameter is only evaluated when flow control is active. |
| MODE | IN | USInt | Byte | 0 | Operating mode  Valid operating modes are:   - 0 = Full duplex (RS232) - 1 = Full duplex (RS422) four-wire mode (point-to-point) - 2 = Full duplex (RS 422) four-wire mode (multipoint master; CM PtP (ET 200SP)) - 3 = Full duplex (RS 422) four-wire mode (multipoint slave; CM PtP (ET 200SP)) - 4 = Half duplex (RS485) two-wire mode <sup>1)</sup> |
| LINE_PRE | IN | USInt | Byte | 0 | Receive line initial state  Valid initial states are:  - 0 = "No" initial state <sup>1)</sup> - 1 = signal R(A)=5 V, signal R(B)=0 V (break detection):  Break detection is possible with this initial state.  Can only be selected with: "Full duplex (RS422) four-wire mode (point-to-point connection)" and "Full duplex (RS422) four-wire mode (multipoint slave)". - 2 = signal R(A)=0 V, signal R(B)=5 V:  This default setting corresponds to the idle state (no active send operation). No break detection is possible with this initial state. |
| BRK_DET | IN | USInt | Byte | 0 | Break detection  The following settings are permitted:   - 0 = break detection deactivated - 1 = break detection activated |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |
| <sup>1)</sup> Required setting for the use of PROFIBUS cables with CM 1241 for RS485 |  |  |  |  |  |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Send_Config: Configure PtP sender (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Send_Config instruction (send configuration) allows you to change send parameters in runtime using your program (conditions that identify the start and the end of the data to be sent). Any data pending in a CM is deleted when Send_Config is executed.

Configuration changes of Send_Config are saved on the CM and not in the CPU. The parameters saved in the device configuration are restored once the voltage returns to the CPU or the communication module.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Activates the configuration change upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:   - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| RTSONDLY | IN | UInt | Word | 0 | Number of milliseconds to wait after activation of RTS before a transmission of send data is started. This parameter is only valid if the hardware flow control is active. The valid range is 0 to 65535 ms. The value 0 deactivates the function. |
| RTSOFFDLY | IN | UInt | Word | 0 | Number of milliseconds to wait after transmission of send data before RTS is deactivated: This parameter is only valid if the hardware flow control is active. The valid range is 0 to 65535 ms. The value 0 deactivates the function. |
| BREAK | IN | UInt | Word | 0 | This parameter specifies that a BREAK is to be sent at the start of each frame for the specified number of bit times. The maximum is 65535 bit times. The value 0 deactivates the function. |
| IDLELINE | IN | UInt | Word | 0 | This parameter specifies that the line is to remain in idle for the specified number of bit times prior to the start of each frame. The maximum is 65535 bit times. The value 0 deactivates the function. |
| USR_END | IN | STRING[2] |  | 0 | Input of end delimiters.  No more than 2 end delimiters can be configured.  All data including the end delimiter(s) is sent, independent of the configured frame length. |
| APP_END | IN | STRING[5] |  | 0 | Input of characters to be appended.  You can append up to 5 characters. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Receive_Config: Configure PtP recipient (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Receive_Config instruction (receive configuration) allows you to change receive parameters in runtime using your program. This instruction configures the conditions that mark the start and the end of received data. Any data pending in a CM is deleted when Receive_Config is executed.

Configuration changes of Receive_Config are saved **non-retentive** on the CM. The parameters saved in the device configuration are restored once the voltage returns to the CPU or the communication module. The Receive_Config instruction therefore must be called again from the user program when the voltage returns to the CPU or to the communication module in order to overwrite the parameters stored in the device configuration.

### Parameter

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Activates the configuration change upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC variable table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| RECEIVE_CONDITIONS | IN | Variant | Any | ‑ | The data structure of Receive_Conditions specifies the start and end conditions used to identify the start and end of a frame. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

More information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

### Start conditions for the Receive_P2P instruction

The Receive_P2P instruction uses the configuration specified in the device configuration or by the Receive_Config instruction to determine the start and end of Freeport communication frames. The start of the frame is defined by the start conditions. The start of the frame can be determined with one or several start conditions.  
If Break as well as Idle Line is activated, Break must be met first and then Idle Line as well. After that, one of the other conditions (start character or start sequence) is sufficient to start data transmission.  
The start condition "Any character" cannot be combined with other start conditions.

### Data type structure of the Receive_Conditions parameter, part 1 (start conditions)

Structure of Receive_Conditions for start conditions

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| START.STARTCOND | IN | Word | 16#0002 | Specifying the start condition   - 01H - detection of the start character - 02H - Any character - 04H - detection of a line break - 08H - detection of an idle line - 10H - detection of start sequence 1 - 20H - detection of start sequence 2 - 40H - detection of start sequence 3 - 80H - detection of start sequence 4   The start conditions can be combined by adding the values together. |
| START.IDLETIME | IN | Word | 16#0028 | The number of bit times required in the idle state for a new frame start to be detected (default value: W#16#28). Only in connection with the condition "Detection of an idle line".  0 to FFFF |
| START.STARTCHAR | IN | Byte | 16#0002 | The start character for the condition "Start character". (default value: B#16#2) |
| START.SEQ[1].CTL | IN | Byte | 0 | Start sequence 1, deactivate/activate comparison for each character: (default value: B#16#0)  These are the activation bits for each character of the start character string.   - 01H - character 1 - 02H - character 2 - 04H - character 3 - 08H - character 4 - 10H - character 5   When a bit is deactivated for a specific character, this means that each character in this position in the character string represents a valid start character string (e.g. 1FH = all 5 characters interpreted). |
| START.SEQ[1].STR[1] .. START.SEQ[1].STR.[5] | IN | Char[5] | 0 | Start sequence 1, start character (5 characters) |
| START.SEQ[2].CTL | IN | Byte | 0 | Start sequence 2, deactivate/activate comparison for each character. Default value: B#16#0) |
| START.SEQ[2].STR[1] .. START.SEQ[2].STR.[5] | IN | Char[5] | 0 | Start sequence 2, start character (5 characters) |
| START.SEQ[3].CTL | IN | Byte | 0 | Start sequence 3, deactivate/activate comparison for each character. Default value: B#16#0 |
| START.SEQ[3].STR[1] .. START.SEQ[3].STR.[5] | IN | Char[5] | 0 | Start sequence 3, start character (5 characters) |
| START.SEQ[4].CTL | IN | Byte | 0 | Start sequence 4, deactivate/activate comparison for each character. Default value: B#16#0 |
| START.SEQ[4].STR[1] .. START.SEQ[4].STR.[5] | IN | Char[5] | 0 | Start sequence 4, start character (5 characters) |

### Example

Have a look at the following received data in hexadecimal coding: "**68** 10 aa **68** bb 10 aa 16". The configured start character strings are available in the following table. Start character strings are evaluated once the first character 68H has been successfully received. After the fourth character has been successfully received (the second 68H), start condition 1 has been met. Once the start conditions have been met, the evaluation of the end conditions starts.

Processing of the start character string can be canceled due to different errors in parity, framing or time intervals between characters. These errors prevent receipt of the data because the start condition has not been met (an error message is output).

Start conditions

| Start condition | First character | First character +1 | First character +2 | First character +3 | First character +4 |
| --- | --- | --- | --- | --- | --- |
| 1 | **68**H | xx | xx | **68**H | xx |
| 2 | 10H | aaH | xx | xx | xx |
| 3 | dcH | aaH | xx | xx | xx |
| 4 | e5H | xx | xx | xx | xx |

### End conditions for the Receive_P2P instruction

The end of a frame is defined by the first occurrence of one or more configured end conditions.

You can configure the end conditions either in the properties of the communication interface in the device configuration, or with the Receive_Config instruction. The receive parameters (start and end conditions) are reset to the settings in the device configuration each time the voltage returns to the CPU or the communication module. When the STEP 7 user program executes Receive_Config, the settings are set to the parameters of Receive_Config .

### Data type structure of the Receive_Conditions parameter, part 2 (end conditions)

Structure of Receive_Conditions for end conditions

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| END.ENDCOND | IN | Word | 0 | This parameter specifies the condition for the frame end:  - 01H - response timeout - 02H - message timeout - 04H - character delay time - 08H - maximum frame length - 10H - read message length from message (N+LEN+M) - 20H - end sequence - 40H - fixed frame length |
| END.FIXLEN | IN | Word | 1 | Fixed frame length: Only used if the end condition "Fixed frame length" has been selected.  1 to 4000 bytes (up to 4 KB depending on the module) |
| END.MAXLEN | IN | Word | 1 | Maximum frame length: Only used if the end condition "Maximum frame length" has been selected.  1 to 4000 bytes (up to 4 KB depending on the module) |
| END.N | IN | Word | 0 | Byte position of the length field in the frame. Only used with end condition N+LEN+M.  1 to 4000 bytes (up to 4 KB depending on the module) |
| END.LENGTHSIZE | IN | Word | 0 | Size of the length field (1, 2, or 4 bytes). Only used with end condition N+LEN+M. |
| END.LENGTHM | IN | Word | 0 | Number of characters after the length field that are not included in the value of the length field. This entry is only used with end condition N+LEN+M. 0 to 255 bytes |
| END.RCVTIME | IN | Word | 200 | Specify the wait time for the first received character after a frame has been sent. The receive instruction is terminated with an error message if a character is not received within the specified time. This information is used only with the condition "Response timeout". (0 to 65535 ms).  Note: This parameter cannot be used as sole end criterion but only in connection with at least one other end condition. |
| END.MSGTIME | IN | Word | 200 | Specify how long to wait for receipt of the complete frame after receipt of the first character. This parameter is used only if the condition "Message timeout" is selected. (0 to 65535 ms) |
| END.CHARGAP | IN | Word | 12 | Enter the maximum number of bit times between characters. If the number of bit times between characters exceeds the specified value, the end condition has been met. This information is used only with the condition "Character delay time". (0 to 65535 bit times)  Note: For higher data transfer speeds, a value of at least 100 bit times is recommended. |
| END.SEQ.CTL | IN | Byte | 0 | End delimiter sequence 1, deactivate/activate comparison for each character:  These are the activation bits for each character of the end character string. Character 1 is bit 0, character 2 is bit 1, ..., character 5 is bit 4. If a bit is deactivated for a specific character, this means that each character represents a congruence at this position of the character string.   **Note:**   Note the sequence when checking characters:  If one end delimiter is to be used, the entry must be made in character 5 (END.SEQ.STR[5]) and only this character must be activated in END.SEQ.CTL. If two end delimiters are to be used, the entry must be made in END.SEQ.STR[5] and END.SEQ.STR[4] and only these characters must be activated in END.SEQ.CTL. The same applies to the use of additional characters. |
| END.SEQ.STR[1] .. END.SEQ.STR[5] | IN | Char[5] | 0 | End delimiter string 1, start character (5 characters) |

General parameters of the Receive_P2P instruction

| Parameter | Declaration | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| GENERAL.MBUF_SIZE | IN | Byte | 255 | Input number of frames that are to be buffered in the receive buffer of the CM.  If no other conditions are active that influence the reaction of the receive buffer (prevent timeout, data flow control), additional frames are discarded once the limit has been reached. (1 to 255 frames) |
| GENERAL.OW_PROT | IN | Byte | 0 | Activates the no overwriting function of the buffered frame if the CM receives a new frame and the receive buffer of the CM was not yet read. This step prevents already buffered received frames from being lost.   - 0 - not activated - 1 - activated |
| GENERAL.CLR_MBUF | IN | Byte | 0 | Activates deletion of the receive buffer during CPU startup. The receive buffer is automatically deleted when the CPU switches from STOP to RUN. The receive buffer only contains frames received after CPU startup.  - 0 - not activated - 1 - activated |

## P3964_Config: Configuring the 3964(R) protocol (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The P3964_Config instruction (protocol configuration) allows you to change protocol parameters for 3964(R), such as character delay time, priority and block check, in runtime using your program.

Configuration changes of P3964_Config are saved on the CM and not in the CPU. The parameters saved in the device configuration are restored once the voltage returns to the CPU or the communication module.

### Parameter

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the instruction upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| BCC | IN | USInt | Byte | 1 | Activates/deactivates the use of the block check  - 0 = without block check - 1 = with block check |
| Priority | IN | USInt | Byte | 1 | Selection of the priority  - 0 = low priority - 1 = high priority |
| CharacterDelayTime | IN | UInt | Word | 16#00DC | Setting the character delay time (depending on the set data transmission rate) (default value: 220 ms)  1 ms to 65535 ms |
| AcknDelayTime | IN | UInt | Word | 16#07D0 | Setting the acknowledgment delay time (depending on the set data transmission rate) (default value: 2000 ms)  1 ms to 65535 ms |
| BuildupAttempts | IN | USInt | Byte | 16#0006 | Setting the number of connection attempts (default value: 6 connection attempts) 1 to 255 |
| RepetitionAttempts | IN | USInt | Byte | 16#0006 | Setting the number of transmission attempts (default value: 6 connection attempts) 1 to 255 |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Send_P2P: Sending data (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Send_P2P instruction (send point-to-point data) starts the transmission of data and transmits the contents of the assigned buffer to the communication module. The CPU program is still being executed while the CM sends the data with the data transmission rate. Only one send instruction per communication module may be pending at any time. The CM signals an error if a second Send_P2P instruction is executed while the CM is already sending a frame.

### Parameter

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the transmission of data to the CM upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| BUFFER | IN | Variant | Any | 0 | This parameter points to the memory area of the send buffer.    **Notes:**    - Boolean data and Boolean fields are not supported. - If the send buffer is in the optimized memory area, the maximum permitted length of the sent data is 1024 bytes. Exception: Arrays of Byte, Word or DWord are supported up to a length of 4096 bytes. - If the send buffer is a String or WString, the content of the string is transferred without the current and maximum length.   Additional information under "[Using the BUFFER and LENGTH parameters for communication operations](#using-the-buffer-and-length-parameters-for-communication-operations-s7-300-s7-400)" |
| LENGTH | IN | UInt | Word | 0 | Length in bytes of the data to be transferred.  The memory area addressed in the BUFFER parameter is completely transmitted with LENGTH = 0.   Additional information under "[Using the BUFFER and LENGTH parameters for communication operations](#using-the-buffer-and-length-parameters-for-communication-operations-s7-300-s7-400)" |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the Send_P2P instruction  The instruction is initialized with 1. The instruction then resets COM_RST to 0.  Note: The parameter is only available for S7-300/400 instructions. |
| UNIVERSAL <sup>1)</sup> | OUT | Bool | --- | FALSE | Type of data communication between the CPU and the CM specified via PORT:  FALSE: Performance optimization (cyclic)  - Receive frames max. 24 bytes - Send frames max. 30 bytes   TRUE: Universal (acyclic)  - Limiting the frame length depending on the CM to 1, 2, or 4 KB |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |
| <sup>1)</sup> Available from library version V4.0 |  |  |  |  |  |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

### Parameter

The DONE and ERROR outputs are in FALSE status when a send instruction is being processed. At the end of the send instruction, one of the DONE or ERROR outputs is set to TRUE for one cycle to signal the status of the send instruction. The error code at the STATUS output can be evaluated when the status of ERROR is TRUE.

The instruction outputs the status 16#7001 when the communication interface accepts the send data. Subsequent executions of Send_P2P output the value 16#7002 if the CM is still sending. At the end of the send instruction, the CM outputs the status 16#0000 for the send instruction (if no error has occurred). Subsequent executions of Send_P2P with REQ = 0 output the status 16#7000 (free).

The diagram below shows the relationship between the output values and REQ. It is based on the assumption that the instruction is called cyclically to check the status of the send process (indicated by the STATUS values).

![Parameter](images/41109843979_DV_resource.Stream@PNG-de-DE.png)

The figure below shows how the DONE and STATUS parameters are only valid for one cycle if a pulse is pending at the REQ line (for one cycle) to trigger the send instruction.

![Parameter](images/41109840011_DV_resource.Stream@PNG-de-DE.png)

The figure below shows the relationship of the DONE, ERROR and STATUS parameters in case of an error.

![Parameter](images/41109834891_DV_resource.Stream@PNG-de-DE.png)

The DONE, ERROR and STATUS values are only valid until Send_P2P is executed again with the same instance DB.

## Using the BUFFER and LENGTH parameters for communication operations (S7-300, S7-400)

### Interaction of BUFFER and LENGTH parameters for Send_P2P

The minimum data size sent by the Send_P2P instruction is one byte.

The BUFFER parameter specifies the size of the data to be sent if a "0" is passed at the LENGTH parameter during call. The specification of a tag is sufficient for this.

You cannot use the data type Bool or arrays of the Bool type for the BUFFER parameter. If large amounts of data are being transferred we recommend the mapping to the array or structure data types.

BUFFER parameter

| BUFFER | Description |
| --- | --- |
| Elementary data type | When sending: The LENGTH value must include the byte size of this data type.   Example: For a Word value, the LENGTH must be two. For a DWord value or Real value, the LENGTH must be four. |
| Structure | If the option for performance optimization is not activated:  - For optimized memory: The maximum permissible length of the BUFFER is 1024 Byte; otherwise 4 KB are permitted depending on the module. - When transmitting, the following applies: The LENGTH value can include a byte size smaller than the complete byte length of the structure; in this case, only the first LENGTH bytes of the structure from BUFFER are sent.   If the option for performance optimization is activated:  - The maximum permitted length of the BUFFER is 30 bytes. |
| Array | For optimized memory: If the array data type is not equal to Byte, Word or DWord, the maximum permitted buffer length is 1024 bytes. Depending on the data structure, up to 4 KB can be transmitted if the memory is not optimized, independent of the data structure.  For sending: The LENGTH value can include a byte size smaller than the complete byte length of the array, whereby, this byte size is a multiple of the byte size of the data element. Example: The LENGTH parameter of an array of the Word type must be a multiple of two and a multiple of four for an array of the Real type.  If BUFFER includes an array with 15 DWord elements (a total of 60 bytes), for example, and you specify LENGTH = 20, the first five DWord elements from the array are transmitted. If LENGTH is not specified or has the value 0, the entire array is transmitted. |
| String | The LENGTH parameter includes the number or characters to be sent. Only the characters of the String are transmitted. The bytes with the maximum and actual length of the String are not sent. |

LENGTH parameter

| LENGTH | Description |
| --- | --- |
| = 0 | The complete content of the memory area specified by BUFFER is transferred.  If BUFFER points to a string, the entire content of the string is transferred, without the bytes with the maximum and actual length. |
| > 0 | The content up to the configured length of the memory area specified by BUFFER is transferred. |

## Receive_P2P: Receiving data (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Receive_P2P instruction (receive data using point-to-point communication) checks the frames received in the CM. If a frame is available, it is transmitted from the CM to the CPU. A receive error is indicated at the STATUS parameter.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| BUFFER | IN | Variant | Any | 0 | This parameter points to the start address of the receive buffer. This buffer must be large enough to receive the maximum frame length.   **Note:**    - Boolean data or Boolean fields are not supported. - If the receive buffer is in the optimized memory area, the maximum permitted length of the received data is 1024 bytes.   Exception: Arrays of Byte, Word or DWord are supported up to a length of 4096 bytes. - If the receive buffer is a String or WString, the received data is written to the content of the string and the current length of the string is set accordingly.   Additional information under "[Using the BUFFER and LENGTH parameters for communication operations](#using-the-buffer-and-length-parameters-for-communication-operations-s7-300-s7-400)" |
| UNIVERSAL <sup>1)</sup> | OUT | Bool | --- | FALSE | Type of data communication between the CPU and the CM specified via PORT:  FALSE: Performance optimization (cyclic)  - Receive frames max. 24 bytes - Send frames max. 30 bytes   TRUE: Universal (acyclic)  - Limiting the frame length depending on the CM to 1, 2, or 4 KB |
| NDR | OUT | Bool |  | FALSE | TRUE for one cycle if new data is available and the instruction has been completed without errors. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle once the instruction has been completed with an error. |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |
| LENGTH | OUT | UInt | Word | 0 | Length of the frame received in bytes   More information under "[Using the BUFFER and LENGTH parameters for communication operations](#using-the-buffer-and-length-parameters-for-communication-operations-s7-300-s7-400)". |
| <sup>1)</sup> Available as of library version V4.0 |  |  |  |  |  |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

The error code at the STATUS output can be evaluated if the status of ERROR is TRUE. The STATUS value provides the reason for terminating the receive operation in the CM.   
This is usually a positive value which indicates that the receive operation has been successful and the frame criterion that has been detected.   
If the STATUS value is negative (the most significant bit of the hexadecimal value is set), the receive operation was terminated due to an error condition, such as a parity, framing or overflow error.

Each communication module can buffer a module-specific number for frames. If several frames are available in the CM, the Receive_P2P instruction outputs the oldest available frame (FIFO).

## Receive_Reset: Clear receive buffer (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Receive_Reset instruction (reset receiver) clears the receive buffer in the CM.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the transmission of data to the CM upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle means that the last request was completed without errors. |
| ERROR | OUT | Bool |  | FALSE | TRUE means that the last request was completed with errors. If this output is TRUE, the STATUS output contains the corresponding error codes. |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Signal_Get: Read status (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Signal_Get instruction (get RS232 signals) reads the current states of the RS232 accompanying signals and displays them at the corresponding instruction outputs.

> **Note**
>
> **Restriction**
>
> - This instruction can only be used with CMs RS232 BA and RS232 HF.
> - If RS232C is set for the operating mode, this instruction can also be used with CM PtP (ET200SP).

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the transmission of data to the CM upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| NDR | OUT | Bool |  | FALSE | TRUE for one cycle if the RS232 accompanying signals have been read and the instruction has been completed without errors. |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle once the instruction has been completed with an error |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |
| DTR | OUT | Bool |  | FALSE | Data device ready, module ready (output) |
| DSR | OUT | Bool |  | FALSE | Data device ready, communication station ready (input) |
| RTS | OUT | Bool |  | FALSE | Send request, module ready to send (output) |
| CTS | OUT | Bool |  | FALSE | Ready to send, communication station can receive data (input) |
| DCD | OUT | Bool |  | FALSE | Data carrier signal detected, signal level received |
| RING | OUT | Bool |  | FALSE | Call display, signaling incoming call |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Signal_Set: Set accompanying signals (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Signal_Set instruction (set RS232 signals) allows you to set the RS232 communication signals.

> **Note**
>
> **Restrictions**
>
> - This instruction can only be used with CMs RS232 BA and RS232 HF.
> - If RS232C is set for the operating mode, this instruction can also be used with CM PtP (ET200SP).

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the instruction upon a positive edge of this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| SIGNAL | IN | Byte |  | 0 | Selection of the signal to be set (more than one possible):   - 01H = RTS - 02H = DTR - 04H = DSR (for interface type DCE only) |
| RTS | IN | Bool |  | FALSE | Send request, module ready to send   Set this value at the output (TRUE or FALSE), default value: FALSE |
| DTR | IN | Bool |  | FALSE | Data terminal ready, module ready   Set this value at the output (TRUE or FALSE), default value: FALSE |
| DSR | IN | Bool |  | FALSE | Data terminal ready (for DCE interface type only), not used. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle after the last request has been completed with errors |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Get_Features: Get extended functions (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

If supported by the module, you can use the Get_Features instruction (get extended functions) to get information on the ability of the module to support CRC and to generate diagnostic messages.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the instruction upon a positive edge of this input. |
| PORT | IN | PORT | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| NDR | OUT | Bool |  | FALSE | TRUE for one cycle if new data is available and the instruction has been completed without errors |
| MODBUS_CRC | OUT | Bool |  | FALSE | Modbus CRC support |
| DIAG_ALARM | OUT | Bool |  | FALSE | Generation of diagnostic messages |
| SUPPLY_VOLT | OUT | Bool |  | FALSE | Diagnostics for missing supply voltage L+ is available |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle once the instruction has been completed with an error |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Set_Features: Set extended functions (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

If supported by the module, you can use the Set_Features instruction (select extended functions) to activate CRC support and the generation of diagnostic messages.

### Parameters

| Parameter | Declaration | Data type |  | Default | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/ 1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | The instruction to set extended functions is started upon a positive edge at this input. |
| PORT | IN | PORT (UInt) | Word | 0 | Specifies the communication module which is used for the communication:  - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC tag table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| EN_MODBUS_CRC | IN | Bool |  | FALSE | Activate Modbus CRC support |
| EN_DIAG_ALARM | IN | Bool |  | FALSE | Activate generation of diagnostic messages |
| EN_SUPPLY_VOLT | IN | Bool |  | FALSE | Enable diagnostics for missing supply voltage L+  Note: This diagnostics is not supported by S7-1500 / ET 200MP communication modules. This also applies if the parameter can be set in combination with e.g. MODBUS_CRC. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE. |
| DONE | OUT | Bool |  | FALSE | TRUE for one execution once the last request is completed without errors |
| ERROR | OUT | Bool |  | FALSE | TRUE for one cycle once the instruction has been completed with an error |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Additional information about the general parameters is available at "[General parameters for Freeport operations](#general-parameters-for-freeport-operations-s7-300-s7-400)".

## Error messages (S7-300, S7-400)

### Overview of PtP error messages

The error messages are provided at the STATUS output of an instruction and can be evaluated there or processed in the user program.

| Error code | Description | Solution |
| --- | --- | --- |
| 16#0000 | No error | ‑ |
| **RECEIVE status and error codes** |  |  |
| 16#0094 | frame end identified based on the "Receipt of fixed/maximum frame length" | ‑ |
| 16#0095 | frame end identified based on "Message timeout" | ‑ |
| 16#0096 | frame end identified based on expiration of the "Character delay time" | ‑ |
| 16#0097 | The frame was aborted because the maximum response time was reached. | ‑ |
| 16#0098 | frame end identified based on the fulfillment of the "Read message length from message" conditions | ‑ |
| 16#0099 | frame end identified based on the receipt of the "End sequence" | ‑ |
| **SEND status and error codes** |  |  |
| 16#7000 | Block idle | ‑ |
| 16#7001 | Initial call for a new frame: Data transmission initiated | ‑ |
| 16#7002 | Interim call: Data transmission running | ‑ |
| 16#8085 | Invalid length | Select a suitable frame length.  - UNIVERSAL = 1 (data communication via data sets): Depending on the module, permissible are: 1 to 1024/2048/4096 bytes - UNIVERSAL = 0 (data communication via IO data; Performance optimized for many short frames): Maximum length is 30 bytes (Send_P2P instruction). |
| 16#8087 | The number of characters received by the CM PtP module exceeds the number supported for UNIVERSAL = 0 (performance optimization). | Select a suitable frame length or use UNIVERSAL = 1 (data communication via data sets).  With UNIVERSAL = 0 (performance optimization), the maximum length is 24 bytes (Receive_P2P instruction). |
| 16#8088 | The specified length exceeds the range set in the receive buffer.  Note: When the data type STRING has been specified at the BUFFER parameter, this error code also appears if the current string is shorter than the length specified at the LENGTH parameter. | Change the range in the receive buffer or select a frame length which corresponds to the range set in the receive buffer.  Depending on the module, permissible are: 1 to 1024/2048/4096 bytes |
| 16#8090 | Configuration error: Odd number of bytes for WString | Select an even number of bytes. |
| 16#8091 | Data records 48, 49 and 50 are not supported for UNIVERSAL = 0 (performance optimization). | Deactivate the "Performance optimized for many short frames" parameter.  or  Access the receive and transmit data via the IO data.  or  Use at least version V4.0 of the instruction library PtP Communication. |
| **RECEIVE status and error codes** |  |  |
| 16#7001 | Initial call for a new frame: Data transmission initiated | ‑ |
| 16#7002 | Interim call: Data transmission running | ‑ |
| 16#8088 | The number of characters received exceeds the number specified at the BUFFER parameter. | Select a suitable frame length.  Depending on the module, permissible are: 1 to 1024/2048/4096 bytes |
| 16#8090 | Configuration error: Odd number of bytes for WString | Select an even number of bytes. |
| **Error message codes of the special functions** |  |  |
| 16#818F | Incorrect parameter number setting (with USS only) | Select a suitable parameter number (PARAM). The following are permissible: 0 to 2047 |
| 16#8190 | Incorrect setting of the CRC calculation | Select a suitable value for the CRC calculation.  The following are valid: deactivated or activated.  Check whether the module addressed supports CRC calculation. |
| 16#8191 | Incorrect setting of the diagnostic error interrupt | Select a suitable value for "Diagnostics interrupt".  The following are valid: Diagnostics interrupt deactivated or diagnostic interrupt activated.  Check whether the module addressed supports the generation of diagnostic interrupts. |
| 16#8193 | The module does not support supply voltage diagnostics L+. | Select a suitable value for "Diagnostics interrupt".  The following are valid: Diagnostics interrupt deactivated or diagnostic interrupt activated.  Check whether the module addressed supports the generation of diagnostic interrupts. |
| **Error message codes of the "Port configuration"** |  |  |
| 16#81A0 | The module does not support this protocol. | Select a valid protocol for the module (PROTOCOL). |
| 16#81A1 | The module does not support this data transmission rate. | Select a valid data transmission rate for the module (BAUD). |
| 16#81A2 | The module does not support this parity setting. | Select a suitable value for "Parity" (PARITY).  The following are valid:   - None (1) - Even (2) - Odd (3) - Mark (4) - Space (5) - Any (6) |
| 16#81A3 | The module does not support this number of data bits. | Select a suitable value for "Number of data bits" (DATABITS).  The following are valid:   - 7 (2) - 8 (1) |
| 16#81A4 | The module does not support this number of stop bits. | Select a suitable value for "Number of stop bits" (STOPBITS).  The following are valid:   - 1 (1) - 2 (2) |
| 16#81A5 | The module does not support this type of data flow control. | Select a valid data flow control for the module (FLOWCTRL). |
| 16#81A7 | Invalid value for XON or XOFF | Select suitable values for XON (XONCHAR) and XOFF (XOFFCHAR).  Valid range of values: 0 to 127 |
| 16#81AA | Invalid operating mode | Valid operating modes are:   - Full duplex (RS232) (0) - Full duplex (RS422) four-wire mode (point-to-point) (1) - Full duplex (RS422) four-wire mode (multipoint master) (2)/ (CM PtP (ET 200SP)) - Full duplex (RS422) four-wire mode (multipoint slave) (3)/ (CM PtP (ET 200SP)) - Half duplex (RS485) two-wire operation. (4) |
| 16#81AB | Invalid receive line initial state | Valid initial states are:  - "No" default setting (0) - Signal R(A)=5 V, signal R(B)=0 V (break detection) (1):  Can only be selected with: "Full duplex (RS422) four-wire operation (point-to-point connection)" and "Full duplex (RS422) four-wire mode (multipoint slave)". - Signal R(A)=0 V, signal R(B)=5 V (2): This default setting corresponds to the idle state (no active send operation). |
| 16#81AC | Invalid value for "Break detection" | Select a suitable value for "Break detection". The following are valid:   - Break detection deactivated (0) - Break detection activated (1). |
| 16#81AF | The module does not support this protocol. | Select a valid protocol for the module. |
| **Error codes of the "Send configuration"** |  |  |
| 16#81B5 | More than two end delimiters or  end sequence > 5 characters | Select suitable values for "End delimiter" and "End sequence".  The following are valid:   - deactivated (0), - 1 (1) or 2 (2) end delimiters   or   - deactivated (0), - 1 (1) up to 5 (5) characters for the end sequence. |
| 16#81B6 | Send configuration rejected because the 3964(R) protocol was selected | Make sure that no send configuration is transmitted if the 3964(R) protocol is set. |
| **Error codes of the "Receive configuration"** |  |  |
| 16#81C0 | Invalid start condition | Select a suitable start condition.  The following are valid:   - Send break before frame start - Send Idle Line. |
| 16#81C1 | Invalid end condition or no end condition selected | Select a suitable end condition (see [Receiving data with Freeport](Configuration%20for%20point-to-point%20links%20%28S7-1500%29.md#receiving-data-with-freeport-s7-1500)). |
| 16#81C3 | Invalid value for "Maximum message length" | Select a suitable value for "Maximum message length" (MAXLEN).  Valid range of values (depending on the module): 1 to 1024/2048/4096 (bytes) |
| 16#81C4 | Invalid value for "Offset of the length specification in the message" | Select a suitable value for "Offset of the length specification in the message".  Valid range of values (depending on the module): 1 to 1024/2048/4096 (bytes) |
| 16#81C5 | Invalid value for "Size of length field" | Select a suitable value for "Size of length field" (LENGTHSIZE).  Valid range of values in bytes:   - 1 (1) - 2 (2) - 4 (4) |
| 16#81C6 | Invalid value for "Number of characters not counted in length specification" | Select a suitable value for "Number of characters not counted in length specification" (LENGTHM).  Valid range of values: 0 to 255 (bytes) |
| 16#81C7 | The total of "Offset in the message + size of length field + number of characters not counted" is greater than the maximum frame length | Select a suitable value for "Offset in message", "Size of length field" and "Number of characters not counted".  Valid range of values:  - Offset in the message (depending on the module):  0 ... 1024/2048/4096 (bytes) - Size of length field: 1, 2, or 4 (bytes) - Number of characters not counted: 0 to 255 (bytes) |
| 16#81C8 | Invalid value for "Response timeout" | Select a suitable value for "Response timeout".  Valid range of values: 1 to 65535 (ms) |
| 16#81C9 | Invalid value for "Character delay time" | Select a suitable value for "Character delay time".  Valid range of values: 1 to 65535 (bit times) |
| 16#81CB | frame end sequence is activated, but no character is activated for the check | Activate one or several characters for the check. |
| 16#81CC | frame start sequence is activated, but no character is activated for the check | Activate one or several characters for the check. |
| 16#81CD | Invalid value for "Prevent overwriting" | Select a suitable value for "Prevent overwriting".  The following are valid:   - Prevent overwriting is deactivated (0) or - Prevent overwriting is activated (1) |
| 16#81CE | Invalid value for "Clear receive buffer on startup" | Select a suitable value for "Clear receive buffer on startup".  The following are valid:   - Clear receive buffer on startup is deactivated (0) - Clear receive buffer on startup is activated (1) |
| **SEND status and error codes** |  |  |
| 16#81D0 | Receiving send request during runtime of a send command | Make sure that you do not receive an additional send request during runtime of a send command. |
| 16#81D1 | The wait time for XON or CTS = ON has expired. | The communication partner has a fault, is too slow or is offline. Check the communication partner or change the parameters, if necessary. |
| 16#81D2 | "Hardware RTS always ON": Send job canceled due to change from DSR = ON to OFF | Check the communication partner. Make sure that DSR is ON for the entire duration of transmission. |
| 16#81D3 | Send buffer overflow / send frame too long | Select a shorter frame length.  The following are valid (depending on the module): 1 to 1024/2048/4096 (bytes) |
| 16#81D5 | Transmission canceled due to parameter changes, detected wire break, or CPU in STOP | Check the parameter assignment, wire break, and CPU status. |
| 16#81D6 | Transmission canceled because end identifier was not received | Check the parameter assignment of the end delimiters and the frame of the communication partner. |
| 16#81D7 | Communication error between the user program and module | Check the communication (e.g., matching the sequence number). |
| 16#81D8 | Transmission attempt rejected because module is not configured | Configure the module. |
| 16#81DF | The module has reset the interface to the FB for one of the following reasons:  - Module was restarted - Module parameters were reassigned - CPU STOP | — |
| **Error codes of the receive configuration** |  |  |
| 16#81E0 | Frame aborted: Receive buffer overflow/received frame too large | Increase the call rate for the receive function in the user program or configure communication with data flow control. |
| 16#81E1 | Frame aborted: Parity error | Check the connection line of the communication partners, or verify that the same data transmission rate, parity and stop bit number are configured for both devices. |
| 16#81E2 | Frame aborted: Character frame error | Check the settings for start bit, data bits, parity bit, data transmission rate, and stop bit(s). |
| 16#81E3 | Frame aborted: Character overflow error | Firmware error: Please contact Customer Support. |
| 16#81E4 | Frame aborted: The total length of "Offset in the message + size of length field + number of characters not counted" is greater than the receive buffer | Select a suitable value for offset in message, size of length field, and number of characters not counted. |
| 16#81E5 | Frame aborted: Break | Break in receive line to partner.   Reconnect or switch on partner. |
| 16#81E6 | Maximum number of "Buffered received frames" exceeded | In the user program call the instruction more often or configure a communication with data flow control or increase the number of buffered frames. |
| 16#81E7 | Synchronization error module and Receive_P2P | Make sure that different instances of the Receive_P2P do not access the same module. |
| 16#81E8 | Frame aborted: The character delay time has expired before the message end criterion was detected | Partner device faulty or too slow. Check this, if required, using an interface tester that is interconnected in the transmission line. |
| 16#81E9 | Modbus CRC error (only communication modules which support Modbus) | Checksum error of the Modbus frame. Check the communication partner. |
| 16#81EA | Modbus frame too short (only communication modules which support Modbus) | Minimum length of Modbus frame not met. Check the communication partner. |
| 16#81EB | Frame aborted: Maximum frame length reached | Select a shorter frame length at the communication partner.  The following are valid (depending on the module): 1 to 1024/2048/4096 (bytes)  Check the parameters for end of frame detection. |
| **Error codes V24 accompanying signals** |  |  |
| 16#81F0 | The module does not support V24 accompanying signals | You have tried to set accompanying signals for a module that does not support V24 accompanying signals. Make sure that this is an RS232 module or that RS232 mode (ET 200SP) is set. |
| 16#81F1 | No operation of the V24 accompanying signals | The V24 accompanying signals cannot be operated manually if hardware data flow control is active. |
| 16#81F2 | The DSR signal cannot be set because the module has the type DTE. | Check the configured type of the module.   The module type must be DCE (data communication equipment). |
| 16#81F3 | The DTR signal cannot be set because the module has the type DCE. | Check the configured type of the module.   The module type must be DTE (data terminal equipment). |
| 16#81F4 | Block header error (e.g. incorrect block type or incorrect block length) | Check the instance DB and the block header. |
| **Error codes of the receive configuration** |  |  |
| 16#8201 <sup>1)</sup> | Receive_Conditions is a pointer to an invalid data type | Enter a pointer to one of the following data types: DB, BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TIME_OF_DAY, TIME, S5TIME, DATE_AND_TIME, STRING |
| 16#8225 | Receive_Conditions points to an optimized memory area greater than 1 kB   or   Receive_Conditions points to an optimized memory area and the receive length is greater than the area addressed by Receive_Conditions. | Enter a pointer to an area with a maximum length of:  - Optimized memory area: 1 KB - Non-optimized memory area: 4 KB   Note: If the pointer points to an optimized memory area, do not send more than 1 KB. |
| 16#8229 <sup>1)</sup> | Receive_Conditions is a pointer to BOOL with a number of bits not equal to n * 8 | If you are using a pointer to BOOL, the number of bits must be a multiple of 8. |
| **Error codes, general** |  |  |
| 16#8280 | Negative acknowledgment when reading module | You can find more detailed information on error causes in the RDREC.STATUS static parameters and in the description of the SFB RDREC.  - Check the input at the PORT parameter - Set the COM_RST parameter before the 1st call. |
| 16#8281 | Negative acknowledgment when writing module | Check the input at the PORT parameter  You can find more detailed information on error causes in the WRREC.STATUS static parameters and in the description of the SFB WRREC. |
| 16#8282 | Module not available | Check the input at the PORT parameter and ensure that the module can be reached. |
| **Error codes of the receive configuration** |  |  |
| 16#82C1 | Invalid value for "Buffered received frames". | Select a suitable value for "Buffered received frames".  Valid range of values: 1 to 255 |
| 16#82C2 | Receive configuration rejected because the 3964(R) protocol was selected | Make sure that no receive configuration is sent if the 3964(R) protocol is set. |
| 16#8301 <sup>1)</sup> | Receive_Conditions is a pointer to an invalid data type | Select a valid data type.  The following are valid: DB, BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TIME_OF_DAY, TIME, S5TIME, DATE_AND_TIME, STRING |
| 16#8322 | Range length error when reading a parameter | Check the input at the Receive_Conditions parameter |
| 16#8324 | Range error when reading a parameter | Check the input at the Receive_Conditions parameter |
| 16#8328 | Setting error when reading a parameter | Check the input at the Receive_Conditions parameter |
| **SEND status and error codes** |  |  |
| 16#8328 <sup>1)</sup> | BUFFER is a pointer to BOOL with a number of bits not equal to n * 8 | If you are using a pointer to BOOL, the number of bits must be a multiple of 8. |
| **Error codes of the receive configuration** |  |  |
| 16#8332 | Invalid data block at the Receive_Conditions parameter | Check the input at the Receive_Conditions parameter |
| 16#833A | The designation of the data block at the Receive_Conditions parameter refers to a data block which is not loaded. | Check the input at the Receive_Conditions parameter |
| 16#8351 | Invalid data type | Check the input at the Receive_Conditions parameter |
| 16#8352 <sup>1)</sup> | Receive_Conditions does not point to a data block | Check the pointer to Receive_Conditions |
| 16#8353 <sup>1)</sup> | Receive_Conditions does not point to a structure of the type Receive_Conditions | Check the pointer to Receive_Conditions |
| **Error codes 3964(R) protocol** |  |  |
| 16#8380 | Parameter assignment error: Invalid value for "Character delay time". | Select a suitable value for "Character delay time" (CharacterDelayTime).  Valid range of values: 1 ... 65535 (ms) |
| 16#8381 | Parameter assignment error: Invalid value for "Response timeout". | Select a suitable value for "Response timeout" (AcknDelayTime).  Valid range of values: 1 ... 65535 (ms) |
| 16#8382 | Parameter assignment error: Invalid value for "Priority". | Select a suitable value for "Priority" (Priority).  The following are valid:   - High (1) - Low (0) |
| 16#8383 | Parameter assignment error: Invalid value for "Block check" | Select a suitable value for "Block check" (BCC).  The following are valid:   - With block check (1) - Without block check (0) |
| 16#8384 | Parameter assignment error: Invalid value for "Connection attempts". | Select a suitable value for "Connection attempts" (BuildupAttempts).  Valid range of values: 1 to 255 |
| 16#8385 | Parameter assignment error: Invalid value for "Transmission attempts". | Select a suitable value for "Transmission attempts" (RepetitionAttempts).  Valid range of values: 1 to 255 |
| 16#8386 | Runtime error: Number of connection attempts exceeded | Check the interface cable and the transmission parameters.   Also check whether the receive function is configured correctly at the partner device. |
| 16#8387 | Runtime error: Number of transmission attempts exceeded | Check the interface cable, the transmission parameters and the configuration of the communication partner. |
| 16#8388 | Runtime error: Error at the "Block check character"   The internally calculated value of the block check character does not correspond to the block check character received by the partner at the connection end. | Check if the connection is seriously disrupted; in this case you may also occasionally see error codes. Check for proper function at the partner device, possibly by using an interface test device that is switched into the transmission line. |
| 16#8389 | Runtime error: Invalid character received while waiting for free receive buffer | The send request of the communication partner (STX, 02H) is only answered with DLE when the receive buffer is empty. No additional character may be received before (except STX again).  Check for proper function at the partner device, possibly by using an interface test device that is switched into the transmission line. |
| 16#838A | Runtime error: Logical error during receiving.  After DLE was received, a further random character (other than DLE or ETX) was received. | Check if the partner always duplicates the DLE in the frame header and data string or the connection is terminated with DLE ETX. Check for proper function at the partner device, possibly by using an interface test device that is switched into the transmission line. |
| 16#838B | Runtime error: Character delay time exceeded | Partner device too slow or faulty.  Verify by using an interface test device that is switched into the transmission line, if necessary. |
| 16#838C | Runtime error: Wait time for free receive buffer has started | In the user program call the instruction more often or configure a communication with data flow control. |
| 16#838D | Runtime error: frame repetition does not start within 4 s after NAK | Check the communication partner. A received frame that is possibly corrupted must be repeated by the partner within 4 seconds. |
| 16#838E | Runtime error: In idle mode, one or several characters (other than NAK or STX) were received. | Check for proper function of the partner device, possibly using an interface test device that is switched into the transmission line. |
| 16#838F | Runtime error: Initialization conflict - Both partners have set high priority | Set the "Low" priority at one of the partners |
| 16#8391 | Parameter assignment error: 3964 configuration data rejected because Freeport is set | If the Freeport protocol is set, make sure that no 3964 parameter assignment data is sent. |
| **Error codes, general** |  |  |
| 16#8FFF | The module is not ready temporarily due to a reset. | Repeat the request. |
| <sup>1)</sup> Only with instructions for S7-300/400 CPUs |  |  |

---

**See also**

[Modbus_Master: Communicate as Modbus master (S7-300, S7-400)](MODBUS%20%28RTU%29%20%28S7-300%2C%20S7-400%29.md#modbus_master-communicate-as-modbus-master-s7-300-s7-400)

---
title: "MODBUS (RTU) (S7-300, S7-400)"
package: ProgFBCMMB34enUS
topics: 7
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# MODBUS (RTU) (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the Modbus RTU communication (S7-300, S7-400)](#overview-of-the-modbus-rtu-communication-s7-300-s7-400)
- [Modbus_Comm_Load: Configure communication module for Modbus (S7-300, S7-400)](#modbus_comm_load-configure-communication-module-for-modbus-s7-300-s7-400)
- [Modbus_Master: Communicate as Modbus master (S7-300, S7-400)](#modbus_master-communicate-as-modbus-master-s7-300-s7-400)
- [Modbus_Slave: Communicate as Modbus slave (S7-300, S7-400)](#modbus_slave-communicate-as-modbus-slave-s7-300-s7-400)
- [Frame structure (S7-300, S7-400)](#frame-structure-s7-300-s7-400)
- [Error messages (S7-300, S7-400)](#error-messages-s7-300-s7-400)

## Overview of the Modbus RTU communication (S7-300, S7-400)

### Modbus RTU communication

Modbus RTU (Remote Terminal Unit) is a standard protocol for communication in the network and uses the RS232 or RS422/485 connection for serial data transmission between Modbus devices in the network.

Modbus RTU uses a master/slave network in which the entire communication is triggered by only one master device while the slaves can only respond to the request of the master. The master sends a request to a slave address and only the slave with this slave address responds to the command.

Exception: Modbus slave address 0 sends a broadcast frame to all slaves (without slave response).

### Modbus function codes

- A CPU that is operated as a Modbus RTU master can read and write data and I/O states in a Modbus RTU slave connected by means of a communication connection.
- A CPU operated as a Modbus RTU slave allows a Modbus RTU master connected over a communication connection to read and write data and I/O states in its own CPU.

Functions for reading data: Reading distributed I/O and program data

| Modbus function code | Functions for reading data from the slave (server) - standard addressing |
| --- | --- |
| 01 | Read output bits: 1 to 2000/1992<sup>1)</sup> bits per request |
| 02 | Read input bits: 1 to 2000/1992<sup>1)</sup> bits per request |
| 03 | Read hold register: 1 to 125/124<sup>1)</sup> words per request |
| 04 | Read input words: 1 to 125/124<sup>1)</sup> words per request |
| 1) for extended addressing |  |

Functions for writing data: Changing distributed I/O and program data

| Modbus function code | Functions for writing of data in the slave (server) - standard addressing |
| --- | --- |
| 05 | Write one output bit: 1 bit per request |
| 06 | Write one hold register: 1 word per request |
| 15 | Write one or several output bits: 1 to 1960 bits per request |
| 16 | Write one or several hold registers: 1 to 122 words per request |

- The Modbus function codes 08 and 11 offer diagnostic options for communication with the slave device.
- Modbus slave address 0 sends a broadcast frame to all slaves (without slave response; for function codes 5, 6, 15, 16).

Station addresses in the Modbus network

| Station |  | Address |
| --- | --- | --- |
| RTU station | Standard station address | 1 to 247 and 0 for broadcast |
| Extended station address | 1 to 65535 and 0 for broadcast |  |

### Modbus memory addresses

The number of Modbus memory addresses (input/output addresses) that is actually available depends on the CPU version and the available work memory.

### Modbus RTU instructions in your program

- Modbus_Comm_Load: You need to run Modbus_Comm_Load to set up PtP parameters such as data transmission rate, parity and data flow control. Once you have configured the communication module for the Modbus RTU protocol, it can only be used by the Modbus_Master instruction or the Modbus_Slave instruction.
- Modbus_Master: The CPU can be used as Modbus RTU master device with the Modbus master instruction for communication with one or more Modbus slave devices.
- Modbus_Slave: The CPU can be used as Modbus RTU slave device with the Modbus slave instruction for communication with a Modbus master device.

## Modbus_Comm_Load: Configure communication module for Modbus (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Modbus_Comm_Load instruction configures a communication module for communication by means of the Modbus RTU protocol. An instance data block is automatically assigned when you add the Modbus_Comm_Load instruction in your program.

Configuration changes of Modbus_Comm_Load are saved on the CM and not in the CPU. With voltage recovery and pulling/plugging, the CM is configured with the data saved in the device configuration. The Modbus_Comm_Load instruction must be called in these scenarios.

### Parameters

| Parameter | Declaration | Data type |  | Standard | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | Starts the instruction upon a positive edge of this input. |
| PORT | IN | Port | Word | 0 | Specifies the communication module which is used for the communication:   - For S7-1500/S7-1200: "HW identifier" from the device configuration. The symbolic port name is assigned in the "System constants" tab of the PLC variable table and can be applied from there. - For S7-300/S7-400: "Input address" from the device configuration. In the S7-300/400/WinAC systems the PORT parameter is assigned the input address assigned in HWCN. |
| BAUD | IN | UDInt | DInt | 9600 | Selection of the data transmission rate  Valid values are: 300, 600, 1200, 2400, 4800, 9600, 19200, 38400 , 57600, 76800, 115200 bps. |
| PARITY | IN | UInt | Word | 0 | Selection of parity:  - 0 – None - 1 – Odd - 2 – Even |
| FLOW_CTRL | IN | UInt | Word | 0 | Selection of flow control:  - 0 – (default) no flow control - 1 – Hardware flow control with RTS always ON (not with RS422/485 CMs) - 2 – Hardware flow control with RTS switched (not with RS422/485 CMs) |
| RTS_ON_DLY | IN | UInt | Word | 0 | Selection RTS ON delay:  - 0 – No delay from "RTS active" until the first character of the frame is sent. - 1 to 65535 – Delay in milliseconds from "RTS active" until the first character of the frame is sent (not with RS422/485 CMs). RTS delays must be used independent of the selection FLOW_CTRL. |
| RTS_OFF_DLY | IN | UInt | Word | 0 | Selection RTS OFF delay:  - 0 – No delay after transmission of last character until "RTS inactive" - 1 to 65535 – Delay in milliseconds after transmission of last character until "RTS inactive" (not with RS422/485 ports). RTS delays must be used independent of the selection FLOW_CTRL. |
| RESP_TO | IN | UInt | Word | 1000 | Response timeout:  5 ms to 65535 ms - Time in milliseconds that Modbus_Master waits for a response from the slave. If the slave does not respond within this period, Modbus_Master repeats the request or terminates the request with an error if the specified number of repetitions (see below, RETRIES parameter) has been sent. |
| MB_DB | IN/OUT | MB_BASE |  | ‑ | A reference to the instance data block of the Modbus_Master or Modbus_Slave instructions.   The MB_DB parameter must be connected with the (static and therefore not visible in the instruction) MB_DB parameter of the Modbus_Master or Modbus_Slave instruction. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the Modbus_Comm_Load instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE.  Note: The parameter is only available for S7-300/400 instructions. |
| DONE | OUT | Bool |  | FALSE | The DONE bit is TRUE for one cycle after the last request has been completed without errors. |
| ERROR | OUT | Bool |  | FALSE | The ERROR bit is TRUE for one cycle after the last request has been completed with errors. The error code in the STATUS parameter is only valid in the cycle in which ERROR = TRUE. |
| STATUS | OUT | Word |  | 16#7000 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

Modbus_Comm_Load is executed to configure a port for the Modbus RTU protocol. Once you have configured the port for the Modbus RTU protocol, it can only be used by the Modbus_Master or Modbus_Slave instructions.

You have to run Modbus_Comm_Load for the configuration of each communication port that is to be used for Modbus communication. You must assign a unique Modbus_Comm_Load instance DB to each port that you use. Only run Modbus_Comm_Load again if you need to change communication parameters, such as data transmission rate or parity, or in case the network has returned.

For example, an instance data block is assigned to the instruction if you add Modbus_Master or Modbus_Slave to your program. You need to connect the MB_DB parameter of the Modbus_Comm_Load instruction to the MB_DB parameter of the Modbus_Master or Modbus_Slave instruction.

### Modbus_Comm_Load data block variables

The table below shows the public static variables in the instance DB of Modbus_Comm_Load that you can use in your program.

Static variables in the instance DB

| Tag | Data type |  | Standard | Description |
| --- | --- | --- | --- | --- |
|  | S7- 1200/1500 | S7- 300/400/ WinAC |  |  |
| ICHAR_GAP | Word |  | 0 | Maximum character delay time between characters. This parameter is specified in milliseconds and increases the anticipated period between the received characters. The corresponding number of bit times for this parameter is added to the Modbus default value of 35 bit times (3.5 character times). |
| RETRIES | Word |  | 2 | Number of retries that the master executes before the error code 0x80C8 for "No response" is returned. |
| EN_SUPPLY_VOLT | Bool |  | 0 | Enable diagnostics for missing supply voltage L+ |
| MODE | USInt | Byte | 0 | Operating mode  Valid operating modes are:  - 0 = Full duplex (RS232) - 1 = Full duplex (RS422) four-wire mode (point-to-point) - 2 = Full duplex (RS 422) four-wire mode (multipoint master, CM PtP (ET 200SP)) - 3 = Full duplex (RS 422) four-wire mode (multipoint slave, CM PtP (ET 200SP)) - 4 = Half duplex (RS485) two-wire mode <sup>1)</sup> |
| LINE_PRE | USInt | Byte | 0 | Receive line initial state  Valid initial states are:  - 0 = "No" initial state <sup>1)</sup> - 1 = signal R(A)=5 V, signal R(B)=0 V (break detection):  Break detection is possible with this initial state.  Can only be selected with: "Full duplex (RS422) four-wire operation (point-to-point connection)" and "Full duplex (RS422) four-wire mode (multipoint slave)". - 2 = signal R(A)=0 V, signal R(B)=5 V:  This default setting corresponds to the idle state (no active send operation). No break detection is possible with this initial state. |
| BRK_DET | USInt | Byte | 0 | Break detection  The following are valid:  - 0 = break detection deactivated - 1 = break detection activated |
| EN_DIAG_ALARM | Bool |  | 0 | Activate diagnostics interrupt:  - 0 - not activated - 1 - activated |
| STOP_BITS | USINT | Byte | 1 | Number of stop bits;   - 1 = 1 stop bit, - 2 = 2 stop bits, - 0, 3 to 255 = reserved |
| <sup>1)</sup> Required setting for the use of PROFIBUS cables with CM 1241 for RS485 |  |  |  |  |

### Instruction versions

Version 3.1 is functionally identical to version 3.0 and its version number was only incremented due to internal measures.

## Modbus_Master: Communicate as Modbus master (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

The Modbus_Master instruction communicates as Modbus master via a port configured by the Modbus_Comm_Load instruction. An instance data block is automatically assigned when you add the Modbus_Master instruction in your program. The MB_DB parameter of the Modbus_Comm_Load instruction must be connected to the (static) MB_DB parameter of the Modbus_Master instruction.

> **Note**
>
> You cannot activate retentivity (Retain) for an instance DB of the Modbus_Master instruction.

### Parameters

| Parameters | Declaration | Data type |  | Standard | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/1500 | S7- 300/400/ WinAC |  |  |  |  |
| REQ | IN | Bool |  | FALSE | FALSE = no request TRUE = request to send data to the Modbus slave |
| MB_ADDR | IN | UInt | Word | ‑ | Modbus RTU station address:  Standard addressing range (1 to 247 as well as 0 for Broadcast) Extended addressing range (1 to 65535 as well as 0 for Broadcast)  The value 0 is reserved for the broadcast of a telegram to all Modbus slaves. Only the Modbus function codes 05, 06, 15 and 16 are supported for the broadcast. |
| MODE | IN | USInt | Byte | 0 | Mode selection: Specifies the type of request (read, write or diagnostics). More information is available in the table of Modbus functions below. |
| DATA_ADDR | IN | UDInt | DWord | 0 | Start address in the slave: Specifies the start address of the data that is accessed in the Modbus slave. The valid addresses are listed in the table of Modbus functions below. |
| DATA_LEN | IN | UInt | Word | 0 | Data length: Specifies the number of bits or words this instruction is to access. The valid lengths are listed in the table of Modbus functions below. |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the Modbus_Master instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE.  Note: The parameter is only available for S7-300/400 instructions. |
| DATA_PTR | IN/OUT | Variant | Any | ‑ | Data pointer: Points to the flag or DB address for the data to be written or read.   As of instruction version V3.0:  The parameter may point to an optimized memory area. In the optimized memory area, a single element or an array is permitted with the following data types: Bool, Byte, Char, Word, Int, DWord, DInt, Real, USInt, UInt, UDInt, SInt, WChar. Every other data type results in error message 16#818C. |
| DONE | OUT | Bool |  | FALSE | The DONE bit is TRUE for one cycle after the last request has been completed without errors. |
| BUSY | OUT | Bool |  | ‑ | - FALSE – no command active for Modbus_Master - TRUE – command for Modbus_Master in progress |
| ERROR | OUT | Bool |  | FALSE | The ERROR bit is TRUE for one cycle after the last request has been completed with errors. The error code in the STATUS parameter is only valid in the cycle in which ERROR = TRUE. |
| STATUS | OUT | Word |  | 0 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

### Tags in the data block of the Modbus master

The table below shows the public static variables in the instance DB of Modbus_Master that you can use in your program.

Static variables in the instance DB

| Tag | Data type | Standard | Description |
| --- | --- | --- | --- |
| Blocked_Proc_Timeout | Real | 3.0 | Duration (in seconds) for which to wait for a blocked Modbus master instance before this instance is removed as ACTIVE. This may happen, for example, if a master request was output and the program then stops to call the master function before it has completely finished the request. The time value must be greater than 0 and less than 55 seconds to avoid an error to occur.   See also "Rules for communication by the Modbus-Master" and "Calling the Modbus_Master instruction with different parameter settings". |
| Extended_Addressing | Bool | FALSE | Configures the slave station address as single or double byte.   - FALSE = One-byte address; 0 to 247 - TRUE = Two-byte address (corresponds to extended addressing);  0 to 65535 |
| Compatibility_Mode <sup>1)</sup> | Bool | FALSE | Compatibility mode with CP 341 and CP 441-2 and ET 200S 1SI with driver for Modbus RTU and with ET 200S 1SI for Modbus.  The default value is 0.  - FALSE = as per Modbus specification, not compatible - TRUE = compatible    - For FC1 and FC2: The data read from the received frame is written word for word to the addressed CPU memory and exchanged byte by byte. If the number of bits to be transmitted is not a multiple of 16, the bits which are not relevant are set to null in the last word.   - For FC15: The words to be transmitted are read word by word from the addressed memory and written byte by byte to the send frame. If the number of bits to be transmitted is not a multiple of 8, the bits in the last byte which are not relevant are read unchanged from the addressed memory and entered in the send frame. |
| MB_DB | MB_BASE | - | The MB_DB parameter of the Modbus_Comm_Load instruction must be connected to this MB_DB parameter of the Modbus_Master instruction. |
| <sup>1)</sup> The PtP communication modules respond as defined in the Modbus specification. To retain a response as with CP 341, CP 441‑2 and ET 200SP 1SI for Modbus, use the "Compatibility_Mode" parameter. |  |  |  |

You program can write values to the Blocked_Proc_Timeout and Extended_Addressing variables to control the Modbus master operations.

### Rules for communication by the Modbus-Master

- Modbus_Comm_Load must be run to configure a port so that the Modbus_Master instruction can communicate with this port.
- A port which is to be used as Modbus master must not be used by Modbus_Slave . You can use one or several instances of Modbus_Master <sup>1)</sup> with this port. But all versions of the Modbus_Master must use the same instance DB for the port.
- The Modbus instructions do not use communication alarm events to control the communication process. Your program must query the Modbus_Master instruction for completed commands (DONE, ERROR).
- We recommend to call all executions of Modbus_Master for a specific port from a program cycle OB. Modbus master instructions can only be executed in one program cycle or in one cyclical/time-controlled processing level. They may not be processed in different processing levels. The priority interruption of a Modbus master instruction by another Modbus master instruction in a processing level with higher priority results in improper operation. Modbus master instructions may mot be processed in startup, diagnostic or time error levels.

<sup>1)</sup> "Instance of Modbus master" here means a call of the Modbus_Master instruction with the same interconnection to a Modbus_Comm_Load instruction and the same setting for the MB_ADDR, MODE, DATA_ADDR and DATA_LEN parameters.

Example

Modbus_Master is called with MODE=0 and DATA_ADDR=10

This job is now active until it is completed with DONE=1 or ERROR=1 or until the time monitoring configured at the Blocked_Proc_Timeout parameter has expired. If a new command is started after the watchdog time expires and before the previous command has been completed, the previous command is aborted without an error message.

If, while this command is running, the instruction is now called a second time with the same instance data but different MODE and DATA_ADDR parameter settings, this second call is terminated with ERROR=1 and STATUS=8200.

### Calling the Modbus_Master instruction with different parameter settings

If multiple calls of the Modbus_Master instruction with different settings for MB_ADDR, MODE, DATA_ADDR or DATA_LEN are placed in your program, you must ensure that only one of these calls is active at any given time. Otherwise, the error message 16#8200 is output (interface is busy with an ongoing request).

If a call cannot be processed in full, the watchdog is activated by the Blocked_Proc_Timeout parameter and terminates the ongoing command.

### REQ parameter

FALSE = no request; TRUE = request to send data to the Modbus slave

Enable the requested transmission. This transmits the contents of the buffer to the point-to-point communication interface.

### You use the DATA_ADDR and MODE parameters to select the Modbus function code.

DATA_ADDR (Modbus start address in the slave): Specifies the start address of the data that is accessed in the Modbus slave.

The Modbus_Master instruction uses the MODE input instead of a function code input. The combination of MODE and DATA_ADDR specifies the function code that is used in the actual Modbus frame. The table below shows how the MODE parameter, the Modbus function code and the Modbus address range in DATA_ADDR are related.

Modbus functions

| MODE | DATA_ADDR (Modbus address) |  |  | DATA_LEN  (data length) |  |  | Modbus function code | Operation and data |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |  |  |  | Bits per request |  |  | 01 | Read output bits: |  |  |
| 1 | to | 9999 | 1 | to | 2000/1992 <sup>1</sup> | 0 | to | 9998 |  |  |
| 0 |  |  |  | Bits per request |  |  | 02 | Read input bits: |  |  |
| 10001 | to | 19999 | 1 | to | 2000/1992 <sup>1</sup> | 0 | to | 9998 |  |  |
| 0 |  |  |  | Words per request |  |  | 03 | Read hold register: |  |  |
| 40001 | to | 49999 | 1 | to | 125/124 <sup>1</sup> | 0 | to | 9998 |  |  |
| 400001 | to | 465535 | 1 | to | 125/124 <sup>1</sup> | 0 | to | 65534 |  |  |
| 0 |  |  |  | Words per request |  |  | 04 | Read input words: |  |  |
| 30001 | to | 39999 | 1 | to | 125/124 <sup>1</sup> | 0 | to | 9998 |  |  |
| 1 |  |  |  | Bits per request |  |  | 05 | Write one output bit: |  |  |
| 1 | to | 9999 | 1 |  |  | 0 | to | 9998 |  |  |
| 1 |  |  |  | 1 word per request |  |  | 06 | Write one hold register: |  |  |
| 40001 | to | 49999 | 1 |  |  | 0 | to | 9998 |  |  |
| 400001 | to | 465535 | 1 |  |  | 0 | to | 65524 |  |  |
| 1 |  |  |  | Bits per request |  |  | 15 | Write multiple output bits: |  |  |
| 1 | to | 9999 | 2 | to | 1968/1960 <sup>1</sup> | 0 | to | 9998 |  |  |
| 1 |  |  |  | Words per request |  |  | 16 | Write multiple hold registers: |  |  |
| 40001 | to | 49999 | 2 | to | 123/122 | 0 | to | 9998 |  |  |
| 400001 | to | 465534 | 2 | to | 123/122 <sup>1</sup> | 0 | to | 65534 |  |  |
| 2 <sup>2</sup> |  |  |  | Bits per request |  |  | 15 | Write one or several output bits: |  |  |
| 1 | to | 9999 | 1 | to | 1968/1960 <sup>1</sup> | 0 | to | 9998 |  |  |
| 2 <sup>2</sup> |  |  |  | Words per request |  |  | 16 | Write one or several hold registers: |  |  |
| 40001 | to | 49999 | 1 | to | 123 | 0 | to | 9998 |  |  |
| 400001 | to | 465535 | 1 | to | 122 <sup>1</sup> | 0 | to | 65534 |  |  |
| 11 | Both DATA_ADDR and DATA_LEN operands of the Modbus_Master are ignored with this function. |  |  |  |  |  | 11 | Read status word and event counter of the slave communication. The status word indicates busy (0 – not busy, 0xFFFF - busy). The event counter is incremented for each successful processing of a frame. |  |  |
| 80 |  |  |  | 1 word per request |  |  | 08 | Check slave status with data diagnostic code 0x0000 (loopback test – slave returns an echo of the request) |  |  |
| - |  |  | 1 |  |  | - |  |  |  |  |
| 81 |  |  |  | 1 word per request |  |  | 08 | Reset slave event counter using data diagnostic code 0x000A |  |  |
| - |  |  | 1 |  |  | - |  |  |  |  |
| 104 <sup>3</sup> |  |  |  | Words per request |  |  | 04 | Read input words |  |  |
| 0 | to | 65535 | 1 | to | 125/124 <sup>1</sup> | 0 | to | 65535 |  |  |
| 3 to 10, 12 to 79, 82 to 103, 105 to 255 | - |  |  | - |  |  |  | Reserved |  |  |
| <sup>1 </sup> In extended addressing, see the Extended_Adressing parameter, the maximum data length is shorter by 1 byte or 1 word depending on the data type of the function.   <sup>2</sup> MODE 2 allows you to write one or more output bits and one or more holding registers using the Modbus functions 15 and 16.  MODE 1 uses the Modbus functions 5 and 6 to write 1 output bit and 1 holding register, and Modbus functions 15 and 16 to write multiple output bits and multiple holding registers.    <sup>3</sup> The following applies to S7-300/400/WinAC: Is not supported. |  |  |  |  |  |  |  |  |  |  |

### DATA_PTR parameter

The DATA_PTR parameter points to the DB or bit memory address in which reading or writing is performed. If you use a data block, you must create a global data block that provides the data memory for read and write processes on Modbus slaves.

> **Note**
>
> **S7-1200/1500 - The data block addressed using DATA_PTR must support direct addressing**
>
> The data block must permit direct (absolute) and symbolic addressing.

> **Note**
>
> **Using function code 5**
>
> Function code 5 is used to set or delete individual bits.
>
> When a bit is set, the value "16#FF00" must be specified in the first word of the addressed DB or bit memory area via DATA_PTR.
>
> - With S7-1200, the value "16#0100" can also be specified to set a bit.
> - To reset a bit, the value "16#0000" must be specified in the first word of the DB or bit memory area addressed via DATA_PTR.
>
> All other values are rejected with ERROR = TRUE and STATUS = 16#8384.

### Data block structures for the DATA_PTR parameter

- These data types are valid for reading words of the Modbus address range (DATA_PTR) 30001 to 39999, 40001 to 49999 and 400001 to 465535 as well as for writing words to the Modbus address range (DATA_PTR parameter) 40001 to 49999 and 400001 to 465535.

  - Standard array of data types WORD, UINT or INT
  - Named structure of the WORD, UINT or INT type in which each element has a unique name and a 16-bit data type.
  - Named complex structure in which each element has a unique name and a 16-bit or 32-bit data type.
- For reading and writing bits for the Modbus address range (DATA_PTR parameter) 00001 to 09999 and for reading bits from 10001 to 19999.

  - Standard field from Boolean data types.
  - Named Boolean structure from clearly named Boolean variables.
- To reduce the risk of data corruption, it is recommended that each Modbus_Master instruction has its own separate memory area.
- It is not necessary for the data areas for DATA_PTR to be located in the same global data block. You can create a data block with several areas for Modbus read processes, a data block for Modbus write processes or a data block for each slave station.

### Instruction versions

Version 3.0 is functionally identical to version 2.4 and its version number was only incremented due to internal measures.

---

**See also**

[Modbus_Slave: Communicate as Modbus slave (S7-300, S7-400)](#modbus_slave-communicate-as-modbus-slave-s7-300-s7-400)

## Modbus_Slave: Communicate as Modbus slave (S7-300, S7-400)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is only possible from firmware version V2.1 of the module.

### Description

Your program can use the Modbus_Slave instruction to communicate as a Modbus slave by using a CM (RS422/485 or RS232). STEP 7 automatically creates an instance DB when you add the instruction. The MB_DB parameter of the Modbus_Comm_Load instruction must be connected to the (static) MB_DB parameter of the Modbus_Slave instruction.

> **Note**
>
> You cannot activate retentivity (Retain) for an instance DB of the Modbus_Slave instruction.

### Parameters

| Parameters | Declaration | Data type |  | Standard | Description |
| --- | --- | --- | --- | --- | --- |
| S7- 1200/1500 | S7- 300/400/ WinAC |  |  |  |  |
| MB_ADDR | IN | UInt | Word | ‑ | Standard address of the Modbus slave: Standard addressing range (1 to 247) Extended addressing range (0 to 65535)   Note: 0 is the broadcast address |
| COM_RST | IN/OUT | --- | Bool | FALSE | Initialization of the Modbus_Slave instruction  The instruction is initialized with TRUE. The instruction then resets COM_RST to FALSE.  Note: The parameter is only available for S7-300/400 instructions. |
| MB_HOLD_REG | IN/OUT | Variant | Any | ‑ | Pointer to the Modbus hold register DB: The Modbus hold register may be the memory area of the flags or a data block.  As of instruction version V4.0:  The parameter must point to a memory area that has a length of at least 16 bits. A shorter length results in error message 16#8187. This applies to single elements, arrays, STRUCTs and UDTs. For example, a Single Bool or an array consisting of less than 16 Boolean elements results in the error message.  If the length is not a multiple of 16 bits, the remaining bits at the end of the memory area cannot be read or written by the Modbus_Slave instruction.  The parameter may point to an optimized memory area. In the optimized memory area, a single element or an array is permitted with the following data types: Bool, Byte, Char, Word, Int, DWord, DInt, Real, USInt, UInt, UDInt, SInt, WChar. Every other data type results in error message 16#818C. |
| NDR | OUT | Bool |  | FALSE | New data available:   - FALSE – No new data - TRUE – Indicates that new data was written by the Modbus master   The NDR bit is TRUE for one cycle after the last request has been completed without errors. |
| DR | OUT | Bool |  | FALSE | Read data:   - FALSE – No data read - TRUE – Indicates that the instruction has stored the data received by the Modbus master in the target area.   The DR bit is TRUE for one cycle after the last request has been completed without errors. |
| ERROR | OUT | Bool |  | FALSE | The ERROR bit is TRUE for one cycle after the last request has been completed with errors. If the execution was terminated with an error, the error code in the STATUS parameter is only valid in the cycle in which ERROR = TRUE. |
| STATUS | OUT | Word |  | 0 | Error code (see [Error messages](#error-messages-s7-300-s7-400)) |

The function codes of the Modbus communication (1, 2, 4, 5 and 15) can read and write bits and words directly in the process image input and in the process image output of the CPU. The MB_HOLD_REG parameter must be defined as data type greater than one byte for these function codes. The table below shows the sample assignment of Modbus addresses to the process image in the CPU.

Assignment of Modbus addresses to the process image

| Modbus functions |  |  |  |  |  | S7-1200 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Code | Function | Data area | Address area |  |  | Data area | CPU address |  |  |
| 01 | Read bits | Output | 0 | to | 8191 | Process image output | O0.0 | to | O1023.7 |
| 02 | Read bits | Input | 0 | to | 8191 | Process image input | I0.0 | to | I1023.7 |
| 04 | Read words | Input | 0 | to | 511 | Process image input | IW0 | to | IW1022 |
| 05 | Write bit | Output | 0 | to | 8191 | Process image output | O0.0 | to | O1023.7 |
| 15 | Write bits | Output | 0 | to | 8191 | Process image output | O0.0 | to | O1023.7 |

Assignment of Modbus addresses to the process image

| Modbus functions |  |  |  |  |  | S7-1500 / S7-300 / S7-400 |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Function code | Function | Data area | Address area |  |  | Data area | CPU address |  |  |
| 01 | Read bits | Output | 0 | to | 9998 | Process image output | O0.0 | to | A1249.6 |
| 02 | Read bits | Input | 0 | to | 9998 | Process image input | I0.0 | to | I1249.6 |
| 04 | Read words | Input | 0 | to | 9998 | Process image input | IW0 | to | IW19996 |
| 05 | Write bit | Output | 0 | to | 9998 | Process image output | O0.0 | to | A1249.6 |
| 15 | Write bits | Output | 0 | to | 9998 | Process image output | O0.0 | to | A1249.6 |

> **Note**
>
> The available address area may be smaller, depending on the memory configuration of the CPU.

The function codes of the Modbus communication (3, 6, 16) use a Modbus hold register which is an address area in the memory area of the flags or a data block. The type of holding register is specified by the MB_HOLD_REG parameter of the Modbus_Slave instruction.

> **Note**
>
> **S7-1200/1500 - type of the MB_HOLD_REG data block**
>
> The data block with Modbus hold register must permit direct (absolute) and symbolic addressing.

Diagnostic functions

| Modbus diagnostic functions of the S7-1200 Modbus_Slave |  |  |
| --- | --- | --- |
| Function codes | Subfunction | Description |
| 08 | 0000H | Output request data of echo test: The Modbus_Slave instruction returns the echo of a received data word to the Modbus master. |
| 08 | 000AH | Clear communication event counter: The Modbus_Slave instruction clears the communication event counter used for Modbus function 11. |
| 11 |  | Call communication event counter: The Modbus_Slave instruction uses an internal communication event counter to detect the number of successful Modbus read and Modbus write requests that are sent to the Modbus slave. The counter is not incremented for function 8, function 11 and broadcast requests. It is also not incremented for requests that result in communication errors (for example, parity or CRC errors). |

The Modbus_Slave instruction supports broadcast write requests from Modbus masters as long as the requests include access to valid addresses. Modbus_Slave generates error code 16#8188 for function codes that are not supported by the broadcast function.

### Variables of the Modbus slave in instruction version V3.0

This table below shows the public static variables in the instance data block of Modbus_Slave that you can use in your program.

Variables of the Modbus slave

| Tag | Data type | Standard | Description |
| --- | --- | --- | --- |
| HR_Start_Offset | Word | 0 | Specifies the start address of the Modbus hold register (default = 0) |
| QB_Start | Word | 0 | Start address of the valid writable addressing range of the outputs (byte 0 to 65535)  Note: The variable is not available for S7-300, S7-400 and WinAC. |
| QB_Count | Word | 0xFFFF | Number of output bytes that can be written by the Modbus master.  Note: The variable is not available for S7-300, S7-400 and WinAC. |
| Extended_Addressing | Bool | FALSE | Extended addressing, configures slave addressing as single or double byte  (FALSE = single byte address, TRUE = double byte address) |
| Request_Count | Word | 0 | The number of all requests received by this slave |
| Slave_Message_Count | Word | 0 | The number of requests received for this specific slave |
| Bad_CRC_Count | Word | 0 | The number of received requests that have a CRC error |
| Broadcast_Count | Word | 0 | The number of received broadcast requests |
| Exception_Count | Word | 0 | Modbus-specific errors that are acknowledged with an exception to the master |
| Success_Count | Word | 0 | The number of received requests without protocol errors for this specific slave |
| MB_DB | MB_BASE | - | The MB_DB parameter of the Modbus_Comm_Load instruction must be connected to this MB_DB parameter of the Modbus_Master instruction. |

You program can write values to the HR_Start_Offset and Extended_Addressing tags and control the Modbus slave operations. The other variables can be read to monitor the Modbus status.

### Rules for Modbus slave communication

- Modbus_Comm_Load must be run to configure a port so that the Modbus_Slave instruction can communicate by means of this port.
- If a port is to respond as slave to a Modbus master, this port may not be programmed with the Modbus_Master instruction.
- Only one instance of Modbus_Slave can be used with a specific port; otherwise you may encounter unexpected behavior.
- The Modbus instructions do not use communication alarm events to control the communication process. Your program must control the communication process by querying the Modbus_Slave instruction for completed send and receive processes.
- The Modbus_Slave instruction must be executed regularly with a frequency that allows a timely response to incoming requests of a Modbus master. We recommend executing Modbus_Slave in each cycle from a program cycle OB. Modbus_Slave can be executed from a cyclic interrupt OB but we do not recommend it, because excessive time delays in the interrupt program can temporarily block the execution of other interrupt programs.

### Time control of the Modbus signal

Modbus_Slave must be executed regularly to receive each request of the Modbus master and respond accordingly. The frequency with which Modbus_Slave is executed depends on the timeout value specified for the response by the Modbus master. This can be seen in the figure below.

![Time control of the Modbus signal](images/154524467595_DV_resource.Stream@PNG-en-US.png)

The timeout period of the (RESP_TO) response is the duration that a Modbus master waits for the beginning of an answer from a Modbus slave. This period is not defined by the Modbus protocol, but by a parameter of the Modbus_Comm_Load instruction. As both receiving and sending a frame requires multiple calls of the Modbus_Slave instruction (at least three), you should execute Modbus_Slave at least twelve times during the timeout period for the response of the Modbus master so that the Modbus slave receives and sends data twice as many times as specified by the timeout period.

### HR_Start_Offset

The Modbus holding register addresses start at 40001 or 400001. These addresses correspond to the start address of the holding register in the target system memory. But you can configure the HR_Start_Offset variable to configure a start address different than 40001 or 400001 for the Modbus hold register.

The address 0 in the received frame correspond to the start address of the hold register in the target system memory. Use the HR_Start_Offset variable to configure a start address other than 0 for the Modbus hold register.

You can, for example, configure a hold register with start at MW100 and a length of 100 words. With HR_Start_Offset = 20, the address 20 in the received frame corresponds to the start address of the holding register in the target memory (MW100). Each address in the received frame below 20 and above 119 results in an addressing error.

Example for addressing the Modbus hold register when DATA_PTR is a pointer to MW100 with a length of 100 words

| HR_Start_Offset | Address | Minimum | Maximum |
| --- | --- | --- | --- |
| 0 | Modbus address (word) | 0 | 99 |
| S7-1500 address | MW100 | MW298 |  |
| 20 | Modbus address (word) | 20 | 119 |
| S7-1500 address | MW100 | MW298 |  |

HR_Start_Offset is a word value which specifies the start address of the Modbus hold register and is saved in the Modbus_Slave instance data block. You select this public static variable by means of the parameter drop-down list once you have added Modbus_Slave in your program.

If you have added Modbus_Slave to an LAD network, for example, you can go to a previous network and assign the value HR_Start_Offset using the move command. The value must be assigned prior to execution of Modbus_Slave.

Enter Modbus slave tag using the standard DB name:

1. Position the cursor in the OUT1 parameter field and enter the character m.
2. Select the required instance DB of the Modbus_Slave instruction from the drop-down list.
3. Position the cursor to the right of the DB name (after the quotation mark) and enter a point.
4. Select "Modbus_Slave_DB.HR_Start_Offset" in the drop-down list.

### Instruction versions

Version 4.0 is functionally identical to version 3.0 and its version number was only incremented due to internal measures.

## Frame structure (S7-300, S7-400)

### Extended_Addressing

You access the Extended_Addressing variable as described for the HR_Start_Offset reference, except that the Extended_Addressing variable is a Boolean value.

You can configure a single byte (Modbus standard) or two bytes (Extended_Adressing = TRUE) with Extended_Adressing = FALSE for addressing the Modbus slave. Extended addressing is used to address more than 247 devices in a single network. With Extended_Adressing = TRUE you can address up to 65535 addresses. The following example shows a Modbus frame.

Slave address with one byte (Byte 0)

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address | Function code | Start address |  | Data |  |  |
| Valid response | Slave address | Function code | Length | Data... |  |  |  |
| Error message | Slave address | 0xxx | Exception code |  |  |  |  |

Slave address with two bytes (Byte 0 and Byte 1)

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address |  | Function code | Start address |  | Data |  |
| Valid response | Slave address |  | Function code | Length | Data... |  |  |
| Error message | Slave address |  | 0xxx | Exception code |  |  |  |

### Frame description

Data traffic between master and slave / slave and master starts with the slave address, following by the function code. The data is then transferred. The structure of the data field depends on the function code used. The checksum (CRC) is transmitted at the end of the frame.

### Function codes with performance optimization

With the option for performance optimization activated, there are restrictions to the configuration limits of the transferred data. More information on the restrictions can be found in the section [Function codes](Configuration%20for%20point-to-point%20links%20%28S7-1500%29.md#function-codes-s7-1500).

### Function code 1 - This function allows individual output bits to be read

FC 1 - Read output bits

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 1 | Start address |  | Number of outputs |  |
| Valid response | Slave address | Function code 1 | Length <sup>1)</sup> | Output data <sup>3)</sup> |  |  |
| Error message | Slave address | 0x81 | Exception code <sup>2)</sup> | --- |  |  |
| <sup>1)</sup> Length: If there is a remainder when the number of outputs is divided by 8, the number of bytes must be increased by 1.   <sup>2)</sup> E code: 01 or 02 or 03 or 04   <sup>3)</sup> The output data can contain multiple bytes |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 1 | Start address |  | Number of outputs |  |
| Valid response | Slave address |  | Function code 1 | Length <sup>1</sup> | Output data |  |  |
| Error message | Slave address |  | 0x81 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: If there is a remainder when the number of outputs is divided by 8, the number of bytes must be increased by 1.   <sup>2</sup> E code: 01 or 02 or 03 or 04   <sup>3</sup> The output data can comprise multiple bytes |  |  |  |  |  |  |  |

### Function code 2 - This function allows individual input bits to be read

FC 2 - Read input bits

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 2 | Start address |  | Number of inputs |  |
| Valid response | Slave address | Function code 2 | Length <sup>1</sup> | Input data |  |  |
| Error message | Slave address | 0x82 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: If there is a remainder when the number of inputs is divided by 8, the number of bytes must be increased by 1.   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 2 | Start address |  | Number of inputs |  |
| Valid response | Slave address |  | Function code 2 | Length <sup>1</sup> | Input data |  |  |
| Error message | Slave address |  | 0x82 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: If there is a remainder when the number of inputs is divided by 8, the number of bytes must be increased by 1.   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 3 - This function allows individual registers to be read

FC 3 - Read hold register

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 3 | Start address |  | Number of registers |  |
| Valid response | Slave address | Function code 3 | Length <sup>1</sup> | Register data |  |  |
| Error message | Slave address | 0x83 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: Number of bytes   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 3 | Start address |  | Number of registers |  |
| Valid response | Slave address |  | Function code 3 | Length <sup>1</sup> | Register data |  |  |
| Error message | Slave address |  | 0x83 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: Number of bytes   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 4 - This function allows individual registers to be read

FC 4 - Read input words

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 4 | Start address |  | Number of input words |  |
| Valid response | Slave address | Function code 4 | Length <sup>1</sup> | Input data |  |  |
| Error message | Slave address | 0x84 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: 2 * number of input words   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 4 | Start address |  | Number of input words |  |
| Valid response | Slave address |  | Function code 4 | Length <sup>1</sup> | Input data |  |  |
| Error message | Slave address |  | 0x84 | Exception code <sup>2</sup> | --- |  |  |
| <sup>1</sup> Length: 2 * number of input words   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 5 - This function can set or delete individual bits

FC 5 - Write an output bit

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 5 | Start address |  | Value |  |
| Valid response | Slave address | Function code 5 | Length | Value |  |  |
| Error message | Slave address | 0x85 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 5 | Start address |  | Value |  |
| Valid response | Slave address |  | Function code 5 | Length | Value |  |  |
| Error message | Slave address |  | 0x85 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 6 - This function allows individual registers to be written

FC 6 - Write hold register

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 6 | Address |  | Register |  |
| Valid response | Slave address | Function code 6 | Address |  | Register |  |
| Error message | Slave address | 0x86 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 6 | Address |  | Register |  |
| Valid response | Slave address |  | Function code 6 | Address |  | Register |  |
| Error message | Slave address |  | 0x86 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 8 - This function is used to check the communication connection

FC 8 - Slave status

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 8 | Diagnostic code |  | Test value |  |
| Valid response | Slave address | Function code 8 | Diagnostic code |  | Test value |  |
| Error message | Slave address | 0x88 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 03 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 8 | Diagnostic code |  | Test value |  |
| Valid response | Slave address |  | Function code 8 | Diagnostic code |  | Test value |  |
| Error message | Slave address |  | 0x88 | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 03 or 04 |  |  |  |  |  |  |  |

### Function code 11 - This function can read 2 bytes of "Status word" and 2 bytes of "Event counter"

FC 11 - Event counter for slave communication

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 11 | --- |  |  |  |
| Valid response | Slave address | Function code 11 | Status |  | Event counter |  |
| Error message | Slave address | 0x8B | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 04 |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 11 | --- |  |  |  |
| Valid response | Slave address |  | Function code 11 | Status |  | Event counter |  |
| Error message | Slave address |  | 0x8B | Exception code <sup>1</sup> | --- |  |  |
| <sup>1</sup> E code: 01 or 04 |  |  |  |  |  |  |  |

### Function code 15 - This function allows multiple bits to be written

FC 15 - Write one/multiple output bits

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 | Byte n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 15 | Start address |  | Number of output words |  | Byte counter <sup>1</sup> | Value |  |
| Valid response | Slave address | Function code 15 | Start address |  | Number of output words |  | --- |  |  |
| Error message | Slave address | 0x8F | Exception code <sup>2</sup> | --- |  |  |  |  |  |
| <sup>1</sup> Byte counter: If there is a remainder when the number of bytes is divided by 8, the number of bytes must be increased by 1.   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 | Byte 8 | Byte n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 15 | Start address |  | Number of output words |  | Byte counter <sup>1</sup> | Value |  |
| Valid response | Slave address |  | Function code 15 | Start address |  | Number of output words |  | --- |  |  |
| Error message | Slave address |  | 0x8F | Exception code <sup>2</sup> |  | --- |  |  |  |  |
| <sup>1</sup> Byte counter: If there is a remainder when the number of bytes is divided by 8, the number of bytes must be increased by 1.   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |  |  |  |

### Function code 16 - This function allows individual or multiple registers to be written

FC 16 - Write one/multiple hold registers

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 | Byte n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address | Function code 16 | Start address |  | Number of registers |  | Byte counter <sup>1</sup> | Value |  |
| Valid response | Slave address | Function code 16 | Start address |  | Number of registers |  | --- |  |  |
| Error message | Slave address | 0x90 | Exception code <sup>2</sup> | --- |  |  |  |  |  |
| <sup>1</sup> Byte counter: Number of registers * 2    <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |  |  |

|  | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 | Byte 7 | Byte 8 | Byte n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Query | Slave address |  | Function code 16 | Start address |  | Number of registers |  | Byte counter <sup>1</sup> | Value |  |
| Valid response | Slave address |  | Function code 16 | Start address |  | Number of registers |  | --- |  |  |
| Error message | Slave address |  | 0x90 | Exception code <sup>2</sup> |  | --- |  |  |  |  |
| <sup>1</sup> Byte counter: Number of registers * 2   <sup>2</sup> E code: 01 or 02 or 03 or 04 |  |  |  |  |  |  |  |  |  |  |

## Error messages (S7-300, S7-400)

### Overview of the Modbus error messages

| Error code | Description | Solution |
| --- | --- | --- |
| 16#0000 | No error | ‑ |
| **Configuration error of the interface -**  **Modbus_Comm_Load** |  |  |
| 16#8181 | The module does not support this data transmission rate. | Select a valid data transmission rate for the module at the BAUD parameter. |
| 16#8182 | The module does not support this parity setting. | Select a suitable value for "Parity" at the PARITY parameter.  The following are valid:   - None (1) - Even (2) - Odd (3) - Mark (4) - Space (5) - Any (6) |
| 16#8183 | The module does not support this type of data flow control. | Select a valid data flow control for the module at the FLOW_CTRL parameter. |
| 16#8184 | Invalid value for "Response timeout". | Select a suitable value for "Response timeout" at the RESP_TO parameter.  Valid range of values: 1 to 65535 (ms) |
| 16#8280 | Negative acknowledgment when reading module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the Send_Config.RDREC.STATUS or Receive_Config.RDREC.STATUS static parameters or RDREC.STATUS and in the description of the SFB RDREC. |
| 16#8281 | Negative acknowledgment when writing module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the Send_Config.WRREC.STATUS or Receive_Config.WRREC.STATUS static parameters or WRREC.STATUS and in the description of the SFB WRREC. |
| 16#8282 | Module not available | Check the input at the PORT parameter and ensure that the module can be reached. |
| **Configuration error -**  **Modbus_Slave** |  |  |
| 16#8186 | Invalid slave address | Select a suitable slave address at the MB_ADDR parameter.  The following are valid: 1-247 at standard address area;  1-65535 at extended address area  (0 is reserved for Broadcast) |
| 16#8187 | Invalid value at MB_HOLD_REG parameter | Select a suitable value for the hold register at the MB_HOLD_REG parameter. |
| 16#8188 | Invalid operating mode or broadcast (MB_ADDR = 0) and MODE parameter ≠ 1 | Select the value 1 for MODE in Broadcast mode or select a different operating mode. |
| 16#818C | The pointer to a MB_HOLD_REG area must be a data block or a bit memory address area. | Select a suitable value for the pointer to the MB_HOLD_REG area. |
| 16#8280 | Negative acknowledgment when reading module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the static parameters Send_P2P.RDREC.STATUS or Receive_P2P.RDREC.STATUS, and in the description of the SFB RDREC. |
| 16#8281 | Negative acknowledgment when writing module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the static parameters Send_P2P.WRREC.STATUS or Receive_P2P.WRREC.STATUS, and in the description of the SFB WRREC. |
| 16#8389 | Invalid data area definition:  - Illegal value of data_type - DB number not permitted or not available:   - Invalid value of db   - DB number does not exist   - DB number is already being used by another data area   - DB with optimized access   - DB is not in work memory - Illegal valid for length - Overlapping of MODBUS address areas that belong to the same MODBUS data type | Check the definition of the data areas.  See section AUTOHOTSPOT |
| 16#8452 <sup>1)</sup> | MB_HOLD_REG is not a pointer to a DB or a bit memory area | Check the MB_HOLD_REG pointer |
| 16#8453 <sup>1)</sup> | MB_HOLD_REG is not a pointer of type BOOL or WORD | Check the MB_HOLD_REG pointer |
| 16#8454 <sup>1)</sup> | The area addressed by MB_HOLD_REG is longer than the DB, or the area addressed is too small for the number of data bytes to be read or written. | Check the MB_HOLD_REG pointer |
| 16#8455 <sup>1)</sup> | MB_HOLD_REG points to a write-protected DB | Check the MB_HOLD_REG pointer |
| 16#8456 <sup>1)</sup> | Error during instruction execution. The cause of the error is shown in the STATUS parameter. | Determine the value of the SFCSTATUS parameter. Check what this means in the description for SFC51, STATUS parameter. |
| **Configuration error -**  **Modbus_Master** |  |  |
| 16#8180 | Invalid value for MB_DB parameter | The value configured for MB_DB (instance data DB) at the Modbus_Comm_Load instruction is not valid.  Check the interconnection of the Modbus_Comm_Load instruction and its error messages. |
| 16#8186 | Invalid station address | Select a suitable station address at the MB_ADDR parameter.  The following are valid: 1-247 at standard address area;  1-65535 at extended address area  (0 is reserved for Broadcast) |
| 16#8188 | Invalid operating mode or broadcast (MB_ADDR = 0) and MODE parameter ≠ 1 | Select the value 1 for MODE in Broadcast mode or select a different operating mode. |
| 16#8189 | Invalid data address | Select a suitable value for the data address at the DATA_ADDR parameter.  See description Modbus_Master in the Info system |
| 16#818A | Invalid length | Select a suitable data length at the DATA_LEN parameter.  See description Modbus_Master in the Info system |
| 16#818B | Invalid value for DATA_PTR | Select a suitable value for the data pointer at the DATA_PTR parameter (M or DB address).  See description Modbus_Master in the Info system |
| 16#818C | Interconnection error of the DATA_PTR parameter | Check the interconnection of the instruction. |
| 16#818D | The area addressed by DATA_PTR is longer than the DB, or the area addressed is too small for the number of data bytes to be read or written. | Check the DATA_PTR pointer |
| 16#8280 | Negative acknowledgment when reading module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the static parameters Send_P2P.RDREC.STATUS or Receive_P2P.RDREC.STATUS, and in the description of the SFB RDREC. |
| 16#8281 | Negative acknowledgment when writing module | Check the input at the PORT parameter.  You can find more detailed information on error causes in the static parameters Send_P2P.WRREC.STATUS or Receive_P2P.WRREC.STATUS or Receive_Reset and in the description of the SFB WRREC. |
| **Communication errors -**  **Modbus_Master**  **and**  **Modbus_Slave** |  |  |
| 16#80D1 | The wait time for XON or CTS = ON has expired. | The communication partner has a fault, is too slow or is offline. Check the communication partner or change the parameters, if necessary. |
| 16#80D2 | "Hardware RTS always ON": Send job canceled due to change from DSR = ON to OFF | Check the communication partner. Make sure that DSR is ON for the entire duration of transmission. |
| 16#80E0 | Frame aborted: Send buffer overflow / send frame too long | In the user program call the instruction more often or configure a communication with data flow control. |
| 16#80E1 | Frame aborted: Parity error | Check the connection line of the communication partners, or verify that the same data transmission rate, parity and stop bit number are configured for both devices. |
| 16#80E2 | Frame aborted: Character frame error | Check the settings for start bit, data bits, parity bit, data transmission rate, and stop bit(s). |
| 16#80E3 | Frame aborted: Character overflow error | Check the number of data in the frame of the communication partner. |
| 16#80E4 | Frame aborted: Maximum frame length reached | Select a shorter frame length at the communication partner.  The following are valid (depending on the module): 1-1024/2048/4096 (bytes) |
| **Communication error -**  **Modbus_Master** |  |  |
| 16#80C8 | The slave does not respond within the set time | Check the data transmission rate, parity and wiring of the slave. |
| 16#80C9 | The slave does not respond within the time set by Blocked_Proc_Timeout. | Check the setting for Blocked_Proc_Timeout.   Check if the module has been configured with the Modbus_Comm_Load instruction. The module may possibly need to be reconfigured using Modbus_Comm_Load after a pull/plug or after voltage recovery. |
| 16#8200 | The interface is busy with an ongoing request. | Repeat the command later. Make sure that there are no commands still running before you start a new one. |
| **Protocol error -**  **Modbus_Slave** (only communication modules that support Modbus) |  |  |
| 16#8380 | CRC error | Checksum error of the Modbus frame. Check the communication partner. |
| 16#8381 | The function code is not supported or is not supported for broadcast. | Check the communication partner and make sure that a valid function code is sent. |
| 16#8382 | Invalid length information in the request frame | Select a suitable data length at the DATA_LEN parameter. |
| 16#8383 | Invalid data address in the request frame | Select a suitable value for the data address at the DATA_ADDR parameter. |
| 16#8384 | Invalid data value error in the request frame | Check the data value in the request frame of the Modbus master |
| 16#8385 | The diagnostic value is not supported by the Modbus slave (function code 08) | The Modbus slave only supports the diagnostic values 16#0000 and 16#000A. |
| **Protocol error -**  **Modbus_Master** (only communication modules that support Modbus) |  |  |
| 16#8380 | CRC error | Checksum error of the Modbus frame. Check the communication partner. |
| 16#8381 | Response frame from Modbus slave with the following error message: The function code is not supported. | Check the communication partner and make sure that a valid function code is sent. |
| 16#8382 | Response frame from Modbus slave with the following error message: Invalid length | Select a suitable data length. |
| 16#8383 | Response frame from Modbus slave with the following error message: Invalid data address in the request frame | Select a suitable value for the data address at the DATA_ADDR parameter. |
| 16#8384 | Response frame from Modbus slave with the following error message: Data value error | Check the request frame to the Modbus slave. |
| 16#8385 | Response frame from Modbus slave with the following error message: The diagnostic value is not supported by the Modbus slave | The Modbus slave only supports the diagnostic values 16#0000 and 16#000A. |
| 16#8386 | The returned function code does not match the requested function code. | Check the response frame and the addressing of the slave. |
| 16#8387 | A slave that was not requested answers | Check the response frame of the device. Check the address settings of the slave. |
| 16#8388 | Error in the response of the slave to a write request. | Check the response frame of the slave. |
| 16#8828 <sup>1)</sup> | DATA_PTR points to a bit address that is not equal to n * 8 | Check the DATA_PTR pointer |
| 16#8852 <sup>1)</sup> | DATA_PTR is not a pointer to a DB or a bit memory area | Check the DATA_PTR pointer |
| 16#8853 <sup>1)</sup> | DATA_PTR is not a pointer of type BOOL or WORD | Check the DATA_PTR pointer |
| 16#8855 <sup>1)</sup> | DATA_PTR points to a write-protected DB | Check the DATA_PTR pointer |
| 16#8856 <sup>1)</sup> | Error during call of SFC51 | Call the Modbus_Master instruction again |
| **Error -**  **Modbus_Slave** (only communication modules that support Modbus) |  |  |
| 16#8428 <sup>1)</sup> | MB_HOLD_REG points to a bit address that is not equal to n * 8 | Check the MB_HOLD_REG pointer |
| 16#8452 <sup>1)</sup> | MB_HOLD_REG is not a pointer to a DB or a bit memory area | Check the MB_HOLD_REG pointer |
| 16#8453 <sup>1)</sup> | MB_HOLD_REG is not a pointer of type BOOL or WORD | Check the MB_HOLD_REG pointer |
| 16#8454 <sup>1)</sup> | The area addressed by MB_HOLD_REG is longer than the DB, or the area addressed is too small for the number of data bytes to be read or written. | Check the MB_HOLD_REG pointer |
| 16#8455 <sup>1)</sup> | MB_HOLD_REG points to a write-protected DB | Check the MB_HOLD_REG pointer |
| 16#8456 <sup>1)</sup> | Error during call of SFC51 | Call the Modbus_Slave instruction again |
| **Error codes, general** |  |  |
| 16#8FFF | The module is not ready temporarily due to a reset. | Repeat the request. |
| <sup>1)</sup> Only with instructions for S7-300/400 CPUs |  |  |

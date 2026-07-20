---
title: "MODBUS (RTU) (S7-1200)"
package: ProgKomMODBUS2MenUS
topics: 13
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# MODBUS (RTU) (S7-1200)

This section contains information on the following topics:

- [MB_COMM_LOAD: Configure port on the PtP module for Modbus RTU (S7-1200)](#mb_comm_load-configure-port-on-the-ptp-module-for-modbus-rtu-s7-1200)
- [MB_MASTER: Communicate via the PtP port as Modbus master (S7-1200)](#mb_master-communicate-via-the-ptp-port-as-modbus-master-s7-1200)
- [MB_SLAVE: Communicate via the PtP port as Modbus slave (S7-1200)](#mb_slave-communicate-via-the-ptp-port-as-modbus-slave-s7-1200)

## MB_COMM_LOAD: Configure port on the PtP module for Modbus RTU (S7-1200)

### Description

The "MB_COMM_LOAD" instruction configures a port for communication using the Modbus RTU protocol. The following hardware can be used for this:

- Up to three point-to-point modules (PtP) CM 1241 RS485 or CM 1241 RS232
- A communications board CB 1241 RS485 in addition to this

After configuration of the port, you communicate over Modbus by executing the "MB_SLAVE" or "MB_MASTER" instruction.

### Call

"MB_COMM_LOAD" must be called once to configure the port for the Modbus RTU protocol. On completion of the configuration, the port can be used by the "[MB_MASTER](#description-of-mb_master-s7-1200)" and "[MB_SLAVE](#description-of-mb_slave-s7-1200)" instructions.

"MB_COMM_LOAD" only needs to be called again if one of the communication parameters has to be modified. Each "MB_COMM_LOAD" call deletes the communications buffer. To avoid data loss during communication, you should not call the instruction unnecessarily.

One instance of "MB_COMM_LOAD" must be used to configure the port of each communication module that is used for Modbus communication. You assign a unique "MB_COMM_LOAD" instance data block for each port that you use. The S7-1200 CPU is limited to three communication modules.

An instance data block is assigned when you insert the "[MB_MASTER](#description-of-mb_master-s7-1200)" or "[MB_SLAVE](#description-of-mb_slave-s7-1200)" instruction. This instance data block is referenced when you specify the MB_DB parameter on the "MB_COMM_LOAD" instruction.

### Parameters

The following table shows the parameters of the "MB_COMM_LOAD" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Execution of the instruction upon a rising edge. |
| PORT | Input | PORT | I, Q, M, D, L or constant | ID of the communications port:  After you have inserted the communications module in the device configuration, the port ID appears in the drop-down list at the PORT box connection. This constant can also be referenced within the "Constants" tab of the tag table. |
| BAUD | Input | UDINT | I, Q, M, D, L or constant | Baud rate selection:  300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 76800, 115200   All other values are invalid. |
| PARITY | Input | UINT | I, Q, M, D, L or constant | Parity selection:  - 0 – None - 1 – Odd - 2 – Even |
| FLOW_CTRL | Input | UINT | I, Q, M, D, L or constant | Flow control selection:  - 0 – (default) No flow control - 1 – Hardware flow control with RTS always ON (does not apply to RS485 ports) - 2 - Hardware flow control with RTS switched |
| RTS_ON_DLY | Input | UINT | I, Q, M, D, L or constant | RTS on-delay selection:  - 0 – (default) No delay of RTS active until the first character of the message is transmitted. - 1 to 65535 – Delay in milliseconds of "RTS active" until the first character of the message is transmitted (does not apply to RS-485 ports). RTS delays must be used depending on the selection of FLOW_CTRL. |
| RTS_OFF_DLY | Input | UINT | I, Q, M, D, L or constant | RTS off-delay selection:  - 0 – (default) No delay after the last character transmitted until "RTS inactive" - 1 to 65535 – Delay in milliseconds after the last character transmitted until "RTS inactive" (does not apply to RS-485 ports). RTS delays must be used regardless of the selection of FLOW_CTRL. |
| RESP_TO | Input | UINT | I, Q, M, D, L or constant | Response timeout:  Time in milliseconds allowed by "[MB_MASTER](#description-of-mb_master-s7-1200)" for the slave to respond. If the slave does not respond in this time, "[MB_MASTER](#description-of-mb_master-s7-1200)" repeats the request or terminates the request with an error if the specified number of retries has been sent.  5 ms to 65535 ms (default = 1000 ms). |
| MB_DB | Input | MB_BASE | D | A reference to the instance data block of the "[MB_MASTER](#description-of-mb_master-s7-1200)" or "[MB_SLAVE](#description-of-mb_slave-s7-1200)" instructions. After you insert "[MB_SLAVE](#description-of-mb_slave-s7-1200)" or "[MB_MASTER](#description-of-mb_master-s7-1200)" in your program, the DB identifier appears in the drop-down list at the MB_DB box connection. |
| DONE | Output | BOOL | I, Q, M, D, L | Execution of instruction completed without error. |
| ERROR | Output | BOOL | I, Q, M, D, L | Error:  - 0 – No error detected - 1 – Indicates that an error was detected. An error code is output in the STATUS parameter. |
| STATUS | Output | WORD | I, Q, M, D, L | Port configuration error code |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameter STATUS

| Error code*  (W#16#...) | Description |
| --- | --- |
| 0000 | No error |
| 8180 | Invalid value for the port ID (wrong address for the communications module). |
| 8181 | Invalid baud rate value. |
| 8182 | Invalid parity value. |
| 8183 | Invalid flow control value. |
| 8184 | Invalid value for the timeout of the response (the time before which a timeout is reported must be at least 25 ms). |
| 8185 | Incorrect pointer in the MB_DB parameter to the instance DB of the "[MB_MASTER](#description-of-mb_master-s7-1200)" or "[MB_SLAVE](#description-of-mb_slave-s7-1200)" instruction. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

### MB_COMM_LOAD data block tags

The table below shows the public static tags in the instance DB of MB_COMM_LOAD that you can use in your program.

Static tags in the instance DB

| Tag | Data type | Default | Description |
| --- | --- | --- | --- |
| ICHAR_GAP | WORD | 0 | Delay for the character spacing between characters. This parameter is specified in milliseconds and is used to increase the anticipated period between the received characters. The corresponding number of bit times for this parameter is added to the Modbus standard value of 35 bit times (3.5 character times). |
| RETRIES | WORD | 2 | The number of repeated attempts by the master before the error code 0x80C8 is returned for "No response". |
| STOP_BITS | USINT | 1 | Number of stop bits per character Valid values 1 and 2 |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## MB_MASTER: Communicate via the PtP port as Modbus master (S7-1200)

This section contains information on the following topics:

- [Description of MB_MASTER (S7-1200)](#description-of-mb_master-s7-1200)
- [Parameter REQ (S7-1200)](#parameter-req-s7-1200)
- [DATA_ADDR and MODE parameters (S7-1200)](#data_addr-and-mode-parameters-s7-1200)
- [Parameter DATA_PTR (S7-1200)](#parameter-data_ptr-s7-1200)
- [Instance DB of the "MB_MASTER" instruction (S7-1200)](#instance-db-of-the-mb_master-instruction-s7-1200)
- [Sample program for a Modbus master (S7-1200)](#sample-program-for-a-modbus-master-s7-1200)

### Description of MB_MASTER (S7-1200)

#### Description

The "MB_MASTER" instruction allows your program to communicate as a Modbus master using a port on a point-to-point module (CM) or a communications board (CB). You can access data in one or more Modbus slave devices.

Before the "MB_MASTER" instruction can communicate with a port, "[MB_COMM_LOAD](#mb_comm_load-configure-port-on-the-ptp-module-for-modbus-rtu-s7-1200)" must first execute.

An instance DB is created when you insert the "MB_MASTER" instruction in your program. You specify this instance DB in the MB_DB input parameter of the "[MB_COMM_LOAD](#mb_comm_load-configure-port-on-the-ptp-module-for-modbus-rtu-s7-1200)" instruction.

#### Rules for Modbus master communication

- A port used for Modbus master requests cannot be used for "MB_SLAVE".
- A port can be used for one or more "MB_MASTER" calls if the same instance DB is used.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must poll the "MB_MASTER" instruction for completed send and receive operations.
- Calling the instruction:

  - Call the "MB_MASTER" instruction if possible in a cyclic program OB. The instruction can only be called in a time delay or cyclic interrupt OB.
  - Do not call more than one "MB_MASTER" instruction in organization blocks with different priority classes. If a "MB_MASTER" instruction executes "preemptively" from a higher priority class, the instruction may execute incorrectly.
  - Do not call the "MB_MASTER" instruction in a startup, diagnostics or time error OB.
- After a transfer has started, the EN parameter (LAD/FBD) must remain set to the value "1" until the DONE or ERROR output parameter is set to "1" by the instruction. A renewed call by the REQ parameter while the instruction is executing causes an error. After the instruction executes, the bit in the REQ parameter remains set for the time specified by the BLOCKED_PROC_TIMEOUT parameter in the instance DB.
- If "MB_MASTER" sends a request to a slave, make sure that "MB_MASTER" continues to execute until the response from the slave arrives.

#### Parameters

The following table shows the parameters of the "MB_MASTER" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| [REQ](#parameter-req-s7-1200) | Input | BOOL | I, Q, M, D, L | Request input:  - 0 – No request - 1 – Request to transmit data to Modbus slave(s) |
| MB_ADDR | Input | UINT | I, Q, M, D, L or constant | Modbus RTU station address:   - Default address range: 0 to 247 - Extended address range: 0 to 65535   The value "0" is reserved for broadcasting a message to all Modbus slaves. Modbus function codes 05, 06, 15, and 16 are the only function codes supported for broadcast. |
| [MODE](#data_addr-and-mode-parameters-s7-1200) | Input | USINT | I, Q, M, D, L or constant | Mode selection: Specifies the type of request: Read, write, or diagnostics:  Refer to the Modbus functions table for details. |
| [DATA_ADDR](#data_addr-and-mode-parameters-s7-1200) | Input | UDINT | I, Q, M, D, L or constant | Starting address in the slave: Specifies the starting address of the data to be accessed in the Modbus slave. You will find the valid addresses in the Modbus functions table. |
| DATA_LEN | Input | UINT | I, Q, M, D, L or constant | Data length: Specifies the number of bits or words to be accessed in this request. You will find the valid lengths in the Modbus functions table. |
| [DATA_PTR](#parameter-data_ptr-s7-1200) | In_Out | VARIANT | M, D | Points to the DB or bit memory address of the CPU for the data to be written or read. For a DB, this must be created with the "Standard - compatible with S7-300/400" access type. |
| DONE | Output | BOOL | I, Q, M, D, L | - 0: Transaction not completed - 1: Transaction completed without error |
| BUSY | Output | BOOL | I, Q, M, D, L | - 0: No "MB_MASTER" transaction in progress - 1: "MB_MASTER" transaction in progress |
| ERROR | Output | BOOL | I, Q, M, D, L | - 0: No error - 1: Error, the error code is indicated by the STATUS parameter |
| STATUS | Output | WORD | I, Q, M, D, L | Execution condition code |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter STATUS

Communications and configuration error messages of the instruction

| Error code*  (W#16#....) | Description |
| --- | --- |
| 0000 | No error |
| 80C8 | Slave timeout. Check the baud rate, parity and the connectors on the slave. |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission within the wait time.  This error is also generated during hardware flow control if the recipient does not detect CTS within the wait time. |
| 80D2 | The send request was aborted because no DSR signal is received from the DCE. |
| 80E0 | The message was terminated because the receive buffer is full. |
| 80E1 | The message was terminated as a result of a parity error. |
| 80E2 | The message was terminated as a result of a framing error. |
| 80E3 | The message was terminated as a result of an overrun error. |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size. |
| 8180 | Invalid value for the port ID. |
| 8186 | Invalid Modbus station address |
| 8188 | The MODE parameter has an invalid value for a broadcast call. |
| 8189 | Invalid data address value. |
| 818A | Invalid data length value. |
| 818B | Invalid pointer to the local data source/destination: Size not correct |
| 818C | The DATA_PTR parameter has an invalid pointer. Use a pointer to a bit memory area or a DB with the "Standard - compatible with S7-300/400" access type. |
| 8200 | Port is busy processing a send request |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

Error messages of the Modbus protocol

| Error code*  (W#16#....) | Response code of slave | Description |
| --- | --- | --- |
| 8380 | - | CRC error |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Data length error |
| 8383 | 02 | Error in the data address or address outside the valid range of DATA_PTR |
| 8384 | &gt; 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |
| 8386 | - | Function code of the response does not match the function code of the query. |
| 8387 | - | Response from wrong slave |
| 8388 | - | The response of the slave to a write call is not correct. The data sent by the slave does not match the query from the master. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

### Parameter REQ (S7-1200)

#### Description

- REQ = FALSE: No request
- REQ = TRUE: Request to transmit data to Modbus slave(s)

You can control this input by means of a level-controlled or edge-controlled contact.

A state machine is started every time this input is activated to ensure that another instruction "MB_MASTER" that uses the same instance DB can only issue a request when the current request has been processed. All other input states are recorded and saved internally for the current request until the reply has been received or an error has been detected.

If the same instance of "MB_MASTER" is executed again with REQ input = 1 before the current request is completely processed, no subsequent transfers are made. However, if the request has been processed, a new request is issued at the time when "MB_MASTER" is executed again with REQ input = 1.

### DATA_ADDR and MODE parameters (S7-1200)

#### Description

You specify the start address for data access to the Modbus slave using the DATA_ADDR parameter.

With the MODE parameter and the Modbus address, you specify the function code to be transferred to the Modbus slave. The following table shows the relationship between the MODE parameter, the function code and Modbus address range.

| MODE | Modbus function | Data length | Operation and data | Modbus address |
| --- | --- | --- | --- | --- |
| 0 | 01 | 1 to 2000  1 to 1992 <sup>(1)</sup> | Read output bits:  1 to (1992 or 2000) bits per query | 1 to 9999 |
| 0 | 02 | 1 to 2000  1 to 1992 <sup>(1)</sup> | Read input bits:  1 to (1992 or 2000) bits per query | 10001 to 19999 |
| 0 | 03 | 1 to 125  1 to 124 <sup>(1)</sup> | Read holding register:  1 to (124 or 125) WORD per query | 40001 to 49999 or  400001 to 465535 |
| 0 | 04 | 1 to 125  1 to 124 <sup>(1)</sup> | Read input WORD:  1 to (124 or 125) WORD per query | 30001 to 39999 |
| 1 | 05 | 1 | Writing an output bit:  One bit per query | 1 to 9999 |
| 1 | 06 | 1 | Writing a holding register:  1 WORD per query | 40001 to 49999 or  400001 to 465535 |
| 1 | 15 | 2 to 1968  2 to 1960 <sup>(1)</sup> | Writing multiple output bits:  2 to (1960 or 1968) bits per query | 1 to 9999 |
| 1 | 16 | 2 to 123  2 to 122 <sup>(1)</sup> | Writing multiple holding registers:  2 to (122 or 123) WORD per query | 40001 to 49999 or  400001 to 465535 |
| 2 | 15 | 1 to 1968  2 to 1960 <sup>(1)</sup> | Writing one or more output bits:  1 to (1960 or 1968) bits per query | 1 to 9999 |
| 2 | 16 | 1 to 123  2 to 122 <sup>(1)</sup> | Writing one or more holding registers:  1 to (122 or 123) WORD per query | 40001 to 49999 or  400001 to 465535 |
| 11 | 11 | 0 | Reading out the communications status word of the slaves and the event counter:  The status word indicates execution of the instruction (0: is not executing; 0xFFFF: is executing). The event counter is incremented each time a message is transferred successfully.  The DATA_ADDR and DATA_LEN parameters of the "MB_MASTER" instruction are ignored with this function. | - |
| 80 | 08 | 1 | Checking the slave status by reading the error code (0x0000):  1 WORD per query | - |
| 81 | 08 | 1 | Resetting the event counter of the slave with the diagnostics code 0x000A:  1 WORD per query | - |
| 3 to 10, 12 to 79, 82 to 2555 |  |  | Reserved | - |
| <sup>(1) </sup>For the "Extended address range", the maximum data length is reduced by one byte or one WORD depending on which data type is used for the function. |  |  |  |  |
|  |  |  |  |  |

### Parameter DATA_PTR (S7-1200)

#### Description

The DATA_PTR parameter is a pointer to a data block or bit memory from which the data should be written or read. If you use a data block, create a global data block with the "Standard - compatible with S7-300/400" access type.

#### Data block structures for the  DATA_PTR parameter

- These data types are valid for **reading of words** of Modbus addresses 30001 to 39999, 40001 to 49999, and 400001 to 465536 and also for **writing of words** to Modbus addresses 40001 to 49999 and 400001 to 465536.

  - Standard array of WORD, UINT, or INT data types (see below).
  - Named WORD, UINT, or INT structure where each element has a unique name and 16 bit data type.
  - Named complex structure where each element has a unique name and 16 bit or 32 bit data type.
- For reading and writing of bits of Modbus addresses 00001 to 09999 and 10001 to 19999.

  - Standard array of Boolean data types.
  - Named Boolean structure of uniquely named Boolean variables.
- Although not required, it is recommended that each "MB_MASTER" instruction has its own separate memory area in a global data block. The reason for this recommendation is that there is a greater possibility of data corruption if multiple "MB_MASTER" instructions are reading and writing the same area of a global data block.
- The memory areas for DATA_PTR do not need to be in the same global data block. You can create one data block with multiple areas for Modbus read operations, one data block for Modbus write operations, or one data block for each slave station.

### Instance DB of the "MB_MASTER" instruction (S7-1200)

#### Static variables of the instance DB

The following table describes the static variables of the instance DB of the instruction that you can use in the user program.

| Variable | Data type | Description |
| --- | --- | --- |
| MB_STATE | UINT | Internal status of the Modbus instruction |
| BLOCKED_ PROC_TIMEOUT | REAL | Time between completion of the instruction call and resetting the ACTIVE bit in the instance DB. The time buffer is used to avoid execution of the instruction being terminated before a job has been sent completely. The default time is 500 ms. |
| EXTENDED_ ADDRESSING | BOOL | Configuring addressing:  - 0: Default address area (1 byte) - 1: Extended address area (2 bytes)   For additional information, refer to the section EXTENDED_ADDRESSING: [Instance DB of the "MB_SLAVE" instruction](#instance-db-of-the-mb_slave-instruction-s7-1200) |

### Sample program for a Modbus master (S7-1200)

#### Networks (LAD)

**Network 1:** Initialize parameters of the RS-485 module only once during the first cycle.

![Networks (LAD)](images/23886364171_DV_resource.Stream@PNG-de-DE.png)

**Network 2:** Read 100 words from the holding register of the slave.

![Networks (LAD)](images/23886372363_DV_resource.Stream@PNG-de-DE.png)

**Network 3:** This is an optional network that displays the values of the first 3 words as soon as the read operation has executed.

![Networks (LAD)](images/23886572555_DV_resource.Stream@PNG-de-DE.png)

**Network 4:** Write 64 bits to the process image output, starting at slave address Q2.0.

![Networks (LAD)](images/23886721547_DV_resource.Stream@PNG-de-DE.png)

## MB_SLAVE: Communicate via the PtP port as Modbus slave (S7-1200)

This section contains information on the following topics:

- [Description of MB_SLAVE (S7-1200)](#description-of-mb_slave-s7-1200)
- [Instance DB of the "MB_SLAVE" instruction (S7-1200)](#instance-db-of-the-mb_slave-instruction-s7-1200)
- [Sample program for a Modbus slave (S7-1200)](#sample-program-for-a-modbus-slave-s7-1200)

### Description of MB_SLAVE (S7-1200)

#### Description

The "MB_SLAVE" instruction allows your program to communicate as a Modbus slave using a port on a point-to-point module (PtP) or a communications board (CB). A Modbus RTU master can issue a request and then your program responds via "MB_SLAVE" execution.

You must assign a unique instance data block when you insert the "MB_SLAVE" instruction in your program. This instance data block is used when you specify it at the MB_DB parameter of the "[MB_COMM_LOAD](#mb_comm_load-configure-port-on-the-ptp-module-for-modbus-rtu-s7-1200)" instruction.

Modbus communication function codes (1, 2, 4, 5, and 15) can read and write bits and words directly in the process image input and process image output in the target system. The following table shows the mapping of Modbus addresses to the process image in the CPU.

| Modbus functions of "MB_SLAVE" |  |  |  |  |  | S7-1200 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Codes** | **Function** | **Data area** | **Address range** |  |  | **Data area** | **CPU address** |
| 01 | Read bits | Output | 1 | to | 8192 | Process image output | Q0.0 to Q1023.7 |
| 02 | Read bits | Input | 10001 | to | 18192 | Process image input | I0.0 to I1023.7 |
| 04 | Read words | Input | 30001 | to | 30512 | Process image input | IW0 to IW1022 |
| 05 | Write bit | Output | 1 | to | 8192 | Process image output | Q0.0 to Q1023.7 |
| 15 | Write bits | Output | 1 | to | 8192 | Process image output | Q0.0 to Q1023.7 |

Modbus communication function codes (function codes 3, 6, 16) use a separate holding register. To do this, you can use bit memory or a data block with the "Standard - compatible with S7-300/400" access type.

You specify the type of the holding register using the MB_HOLD_REG parameter of the MB_SLAVE instruction. The following table shows the mapping of the Modbus holding register to the DB address of MB_HOLD_REG in the target system.

| Modbus functions of "MB_SLAVE" |  |  |  | S7-1200 |  |
| --- | --- | --- | --- | --- | --- |
| **Codes** | **Function** | **Data area** | **Address range**    **(WORD number)** | **Address in the DB**    **(BYTE number)** | **Bit memory address**    **(BYTE number)** |
| 03 | Read words | Holding register | 40001 to 49999 or | DW0 to DW19998 or | MW0 to CPU limit |
| 400001 to 465535 | DW0 to DW131068 |  |  |  |  |
| 06 | Write word | Holding register | 40001 to 49999 or | DW0 to DW19998 or |  |
| 400001 to 465535 | DW0 to DW131068 |  |  |  |  |
| 16 | Write words | Holding register | 40001 to 49999 or | DW0 to DW19998 or |  |
| 400001 to 465535 | DW0 to DW131068 |  |  |  |  |

The table below shows the supported Modbus diagnostic functions.

| S7-1200 "MB_SLAVE" Modbus diagnostic functions |  |  |
| --- | --- | --- |
| **Codes** | **Subfunction** | **Description** |
| 08 | 0000H | Return query data echo test: The "MB_SLAVE" instruction returns the echo of a received data word to a Modbus master. |
| 08 | 000AH | Clear communication event counter: The "MB_SLAVE" instruction clears the communication event counter that is used for Modbus function 11. |
| 11 | - | Get communication event counter: The "MB_SLAVE" instruction uses an internal communication event counter for recording the number of successful Modbus read and write requests that are sent to the Modbus slave. The counter is not incremented on any Function 8, Function 11, or broadcast requests. It is also not incremented on any requests that result in a communication error (for example, parity or CRC errors). |

The "MB_SLAVE" instruction supports broadcast write requests from Modbus masters as long as the requests include access to valid addresses.

Regardless of the validity of a request, "MB_SLAVE" gives no response to a Modbus master as the result of a broadcast request.

#### Rules of Modbus slave communication

- "MB_COMM_LOAD" must be executed to configure a port, before the "MB_SLAVE" instruction can communicate with this port.
- If a port is to respond as a slave to a Modbus master, then that port cannot be used by "[MB_MASTER](#description-of-mb_master-s7-1200)". Only one instance of "MB_SLAVE" can be used with a given port.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must control the communication process by polling the "MB_SLAVE" instruction for completed send and receive operations.
- The "MB_SLAVE" instruction must be executed periodically at a rate that allows it to make a timely response to incoming requests from a Modbus master. It is therefore advisable to call the instruction in a cyclic program OB. Calling the "MB_SLAVE" instruction in an interrupt OB is possible but not advisable since it can lead to long delays in execution.

#### Frequency of execution of "MB_SLAVE"

The "MB_SLAVE" instruction must be executed periodically to receive each request from the Modbus master and to respond as required. The frequency of execution of "MB_SLAVE" is dependent upon the specified response timeout period of the Modbus master. This is illustrated in the following diagram.

![Frequency of execution of "MB_SLAVE"](images/20044425355_DV_resource.Stream@PNG-en-US.png)

The response timeout period is the amount of time a Modbus master waits for the start of a response from a Modbus slave. This time period is not defined by the Modbus protocol, but rather by a parameter of each Modbus master. The frequency of execution (time between one execution and the next execution) of "MB_SLAVE" must be based on the particular parameters of your Modbus master. As a minimum, you should execute "MB_SLAVE" twice within the response timeout period of the Modbus master.

#### Parameter

The following table shows the parameters of the "MB_SLAVE" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MB_ADDR | Input | V1.0: USINT  V2.0: UINT | I, Q, M, D, L or constant | Station address of the Modbus slave (address range: 0 to 255) |
| MB_HOLD_REG | In_Out | VARIANT | D | Pointer to the Modbus holding register DB. The DB must be created with the "Standard - compatible with S7-300/400" access type. |
| NDR | Output | BOOL | I, Q, M, D, L | New data ready:   - 0: No new data - 1: Indicates that new data has been written by the Modbus master |
| DR | Output | BOOL | I, Q, M, D, L | Read data:   - 0: No data read - 1: Indicates that data has been read by the Modbus master |
| ERROR | Output | BOOL | I, Q, M, D, L | - 0: No error detected - 1: Error, a corresponding error code is output in the STATUS |
| STATUS | Output | WORD | I, Q, M, D, L | Error code |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter STATUS

| STATUS* (W#16#....) | Description |  |
| --- | --- | --- |
| 80C8 | The specified response timeout (refer to RCVTIME or MSGTIME) is "0". |  |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission within the wait time.  This error is also generated during hardware flow control if the recipient does not detect CTS within the wait time. |  |
| 80D2 | The send request was aborted because no DSR signal is received from the DCE. |  |
| 80E0 | The message was terminated because the receive buffer is full |  |
| 80E1 | The message was terminated as a result of a parity error |  |
| 80E2 | The message was terminated as a result of a message frame error |  |
| 80E3 | The message was terminated as a result of a overrun error |  |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size |  |
| 8180 | Invalid value for the port ID. |  |
| 8186 | Invalid Modbus station address |  |
| 8187 | Invalid pointer to MB_HOLD_REG-DB |  |
| 818C | Pointer to a type safe DB type MB_HOLD_REG (must be a Classic DB type) |  |
|  |  |  |
| Response code sent to Modbus master (B#16#...) |  |  |
| 8380 | No response | CRC error |
| 8381 | 01 | Function code not supported or not supported in a broadcast |
| 8382 | 03 | Data length error |
| 8383 | 02 | Error in the data address or address outside the valid range of MB_HOLD_REG |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

### Instance DB of the "MB_SLAVE" instruction (S7-1200)

#### Static variables of the instance DB

The following table describes the static variables of the instance DB of the instruction that you can use in the user program. Your program can write values to the HR_Start_Offset and Extended_Addressing variables and control the Modbus slave operations.

The other variables can be read to monitor the Modbus status.

| Variable | Data type | Description |
| --- | --- | --- |
| HR_Start_Offset | WORD | Start address of the Modbus holding register (default = " 0") |
| Extended_ Addressing | BOOL | Configuring addressing:  - 0: Default address area (1 byte) - 1: Extended address area (2 bytes) |
| Request_Count | WORD | Total number of queries received by the slave |
| Slave_Message_Count | WORD | Number of queries sent to this specific slave |
| Bad_CRC_Count | WORD | Number of received queries with CRC errors |
| Broadcast_Count | WORD | Number of received broadcast queries |
| Exception_Count | WORD | Number of Modbus-specific errors that require the return of an exception |
| Success_Count | WORD | The number of requests received for this specific slave without protocol errors |

#### HR_Start_Offset

The addresses of the Modbus holding register start at 40001 or 400001. These addresses correspond to the start address of the holding register in the target system memory. Using the HR_Start_Offset variable, you can set the offset to a different start address.

Example: A holding register starts at MW 100 and has a length of 100 WORD. With an offset of 20 in the HR_Start_Offset parameter, the holding register begins at address 40021 instead of 40001. Each address below 40021 and above 400119 causes an addressing error.

|  | HR_Start_Offset = 0 |  |  | HR_Start_Offset = 20 |  |
| --- | --- | --- | --- | --- | --- |
|  | Modbus word address | S7-1200 byte address |  | Modbus word address | S7-1200 byte address |
| Minimum | 40001 | MW100 |  | 40021 | MW100 |
| Maximum | 40099 | MW198 |  | 40119 | MW198 |
|  |  |  |  |  |  |

#### Extended_Addressing

To address the Modbus slave, a single byte (default address range) or a double byte (extended address range) can be configured. Extended addressing is used to address more than 247 devices in a single network. If you decide on extended addressing, you can address a maximum of 64,000 addresses. Below, you will see a frame of Modbus function 1 as an example.

Slave address with one byte (byte 0)

| Function 1 | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address | F code | Start address |  | Length of the coils |  |  |
| Valid response | Slave address | F code | Length | Coil data |  |  |  |
| Error response | Slave address | 0x81 | E code |  |  |  |  |
|  |  |  |  |  |  |  |  |

Slave address with two bytes (byte 0 and byte 1)

| Function 1 | Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 | Byte 5 | Byte 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address |  | F code | Start address |  | Length of the coils |  |
| Valid response | Slave address |  | F code | Length | Coil data |  |  |
| Error response | Slave address |  | 0x81 | F code |  |  |  |

### Sample program for a Modbus slave (S7-1200)

#### Networks (LAD)

**Network 1:** Initialize parameters of the RS-485 module only once during the first cycle.

![Networks (LAD)](images/23888330123_DV_resource.Stream@PNG-de-DE.png)

**Network 2:** Check the requests of the Modbus master in every cycle. 100 words starting at MW1000 are configured for the Modbus holding register.

![Networks (LAD)](images/23888658315_DV_resource.Stream@PNG-de-DE.png)

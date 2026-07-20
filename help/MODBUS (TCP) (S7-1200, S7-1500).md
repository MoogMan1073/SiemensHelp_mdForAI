---
title: "MODBUS (TCP) (S7-1200, S7-1500)"
package: ProgKomModbTCP2MenUS
topics: 50
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# MODBUS (TCP) (S7-1200, S7-1500)

This section contains information on the following topics:

- [MODBUS (TCP) for the library versions V2.1 and V3.x of the S7-1200 CPUs (S7-1200)](#modbus-tcp-for-the-library-versions-v21-and-v3x-of-the-s7-1200-cpus-s7-1200)
- [MODBUS (TCP) for the library versions V4.0 and later of the S7-1200 CPUs and as of V3.x of the S7-1500 CPUs (S7-1200, S7-1500)](#modbus-tcp-for-the-library-versions-v40-and-later-of-the-s7-1200-cpus-and-as-of-v3x-of-the-s7-1500-cpus-s7-1200-s7-1500)
- [Redundant MODBUS (TCP) communication for library versions V5.0 or higher (S7-1200, S7-1500)](#redundant-modbus-tcp-communication-for-library-versions-v50-or-higher-s7-1200-s7-1500)

## MODBUS (TCP) for the library versions V2.1 and V3.x of the S7-1200 CPUs (S7-1200)

This section contains information on the following topics:

- [MB_CLIENT: Communicating via PROFINET as a Modbus TCP client (S7-1200)](#mb_client-communicating-via-profinet-as-a-modbus-tcp-client-s7-1200)
- [MB_SERVER: Communicating via PROFINET as a Modbus TCP server (S7-1200)](#mb_server-communicating-via-profinet-as-a-modbus-tcp-server-s7-1200)
- [Examples (S7-1200)](#examples-s7-1200)

### MB_CLIENT: Communicating via PROFINET as a Modbus TCP client (S7-1200)

This section contains information on the following topics:

- [Description of MB_CLIENT (S7-1200)](#description-of-mb_client-s7-1200)
- [REQ and DISCONNECT parameters (S7-1200)](#req-and-disconnect-parameters-s7-1200)
- [MB_MODE, MB_DATA_ADDR and DATA_LEN parameters (S7-1200)](#mb_mode-mb_data_addr-and-data_len-parameters-s7-1200)
- [MB_DATA_PTR parameter (S7-1200)](#mb_data_ptr-parameter-s7-1200)
- [Parameter STATUS (S7-1200)](#parameter-status-s7-1200)

#### Description of MB_CLIENT (S7-1200)

##### Description

The "MB_CLIENT" instruction communicates as a Modbus TCP client via the PROFINET connection of the S7-1200 CPU. To use the instruction, you do not require any additional hardware module. With the "MB_CLIENT" instruction, you establish a connection between the client and the server, send requests and receive responses and control connection termination of the Modbus TCP server.

##### Parameters

The following table shows the parameters of the "MB_CLIENT" instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| [REQ](#req-and-disconnect-parameters-s7-1200) | Input | BOOL | Communication request with the Modbus TCP server  The REQ parameter is level-controlled. This means that as long as the input is set (REQ=true), the instruction sends communication requests.  - The instance DB for other clients is blocked with the communications request. - Changes to the input parameters will not become effective until the server has responded or an error message has been output. - If the parameter REQ is set again during an ongoing Modbus request, no additional transmission takes place afterwards. |
| [DISCONNECT](#req-and-disconnect-parameters-s7-1200) | Input | BOOL | With this parameter, you control the establishment and termination of the connection to the Modbus server:  - 0: Establish a communications connection to the specified IP address and port number. - 1: Disconnect the communication connection. No other function is executed during connection termination. The value 7003 is output at the STATUS parameter after successful connection termination.   The request is sent immediately if the REQ parameter is set during connection establishment. |
| CONNECT_ID | Input | UINT | Unique ID to identify the connection. Each instance of the instructions "MB_CLIENT" and "[MB_SERVER](#description-of-mb_server-s7-1200)" must be assigned a unique connection ID. |
| IP_OCTET_1 | Input | USINT | 1st octet of the IP address* of the Modbus TCP server. |
| IP_OCTET_2 | Input | USINT | 2nd octet of the IP address* of the Modbus TCP server. |
| IP_OCTET_3 | Input | USINT | 3rd octet of the IP address* of the Modbus TCP server. |
| IP_OCTET_4 | Input | USINT | 4th octet of the IP address* of the Modbus TCP server. |
| IP_PORT | Input | UINT | IP port number of the server to which the client establishes the connection and communicates using the TCP/IP protocol (default value: 502). |
| [MB_MODE](#mb_mode-mb_data_addr-and-data_len-parameters-s7-1200) | Input | USINT | Selects the mode of the request (read, write or diagnostics). |
| [MB_DATA_ADDR](#mb_mode-mb_data_addr-and-data_len-parameters-s7-1200) | Input | UDINT | Start address of the data accessed by the "MB_CLIENT" instruction. |
| DATA_LEN | Input | UINT | Data length: Number of bits or words for the data access (see "MB_MODE and MB_DATA_ADDR parameters" - data length). |
| [MB_DATA_PTR](#mb_data_ptr-parameter-s7-1200) | InOut | VARIANT | Pointer to the Modbus data register: The register is a buffer for the data received from the Modbus server or to be sent to the Modbus server. The pointer must reference a global data block with standard access.  The number of bits addressed must be divisible by 8. |
| DONE | Out | BOOL | The bit at output parameter DONE is set to "1" as soon as the last job is completed without errors. |
| BUSY | Out | BOOL | - 0: No "MB_CLIENT " job in progress - 1: "MB_ CLIENT " job in progress |
| ERROR | Out | BOOL | - 0: No error - 1: Error occurred. The cause of error is indicated by the STATUS parameter. |
| [STATUS](#parameter-status-s7-1200) | Out | WORD | Error code of the instruction. |
| * 8-bit long component of the 32-bit IPv4 IP address of the Modbus TCP server. |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **Consistent input data during an "MB_CLIENT" call**
>
> When a Modbus client calls a Modbus instruction, the status of the input parameters is stored internally and then compared at the next call. The comparison is used to determine whether this particular call initialized the current request. Several "MB_CLIENT" calls can be executed if you use a common instance DB. The values of the input parameters must not be changed while an "MB_CLIENT" instance is being executed. If the input parameters are changed during execution, "MB_CLIENT" cannot be used to check whether or not the instance is currently being executed.

##### Multiple client connections

A Modbus TCP client can support several TCP connections and the maximum number of connections depends on the CPU being used. The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections. Modbus TCP connections can also be shared by client and/or server connections.

With individual client connections, remember the following rules:

- Each "MB_CLIENT" connection must use a unique instance DB.
- For each "MB_CLIENT" connection, a unique server IP address must be specified.
- Each "MB_CLIENT" connection requires a unique connection ID.

  The relevant individual connection ID must be used for each individual instance DB of the instruction. The connection ID and instance DB belong together in pairs and must be unique for each connection.
- Unique numbers for the IP port may or may not be required depending on the server configuration.

##### Static tags of the instruction

The following table describes the editable static tags of the instance data block of the "MB_CLIENT" instruction.

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| Blocked_Proc_Timeout | REAL | 3.0 | Wait time in seconds before the static tag ACTIVE is reset if there is a blocked Modbus instance. This can, for example, occur if a client request is output and the execution of the client function aborts before the request was fully executed. The maximum wait time is 55 seconds. |
| MB_Transaction_ID | WORD | 1 | Transaction ID of the Modbus TCP protocol. The start value of "1" should only be changed if the Modbus TCP server requires a different value. |
| MB_Unit_ID | BYTE | 255 | Unit Identifier  Modbus device detection:  A Modbus TCP server is addressed using its IP address. For this reason, the MB_UNIT_ID parameter is not used in the case of Modbus TCP addressing.  The MB_UNIT_ID parameter corresponds to the field of the slave address in the Modbus RTU protocol. If a Modbus TCP server is used as a gateway for a Modbus RTU protocol, the slave device in the serial network can be identified using MB_UNIT_ID. The MB_UNIT_ID parameter would in this case forward the request to the correct Modbus RTU slave address.  Please note that some Modbus TCP devices may require the MB_UNIT_ID parameter for the initialization within a limited value range. |
| RCV_TIMEOUT | REAL | 2.0 | Time interval in seconds in which the "MB_CLIENT" instruction waits for a response from the server. |
| Connected | BOOL | 0 | Indicates whether the connection to the assigned client has been established or not: 1 = connected, 0 = not connected. |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[MB_CLIENT example 1: Send several requests via a TCP connection (S7-1200)](#mb_client-example-1-send-several-requests-via-a-tcp-connection-s7-1200)
  
[MB_CLIENT example 2: Send multiple requests via several TCP connections (S7-1200)](#mb_client-example-2-send-multiple-requests-via-several-tcp-connections-s7-1200)
  
[MB_CLIENT example 3: Coordinate several requests (S7-1200)](#mb_client-example-3-coordinate-several-requests-s7-1200)

#### REQ and DISCONNECT parameters (S7-1200)

##### Description

If no instance of the "MB_CLIENT" instruction is executing and if the value of the DISCONNECT parameter is "0", a new job executes if REQ=1. If there is not yet a connection, this is established during execution.

If the same instance of the "MB_CLIENT" instruction executes again (DISCONNECT = 0 and REQ = 1), before the active job was executed, this is not executed on completion of the active job. A new job can only be started on completion of the active job (REQ = 1).

You can monitor the status of execution with the DONE parameter. You can use this to monitor the status of execution if the "MB_CLIENT" instruction is executed sequentially.

---

**See also**

[Description of MB_CLIENT (S7-1200)](#description-of-mb_client-s7-1200)

#### MB_MODE, MB_DATA_ADDR and DATA_LEN parameters (S7-1200)

##### Description

The combination of the MB_MODE, MB_DATA_ADDR and DATA_LEN parameters defines the Modbus function code used in the current Modbus message for the values 0, 1 and 2 of MB_MODE:

- MB_MODE contains the information on whether to read or to write.

  MB_MODE=0: Read, MB_MODE=1 and 2: Writing
- MB_DATA_ADDR contains the information on what is to be read or written, as well as address information from which the "MB_CLIENT" instruction calculates the remote address.
- DATA_LEN contains the number of values to be read/written.

Examples:

- The combination MB_MODE=1, MB_DATA_ADDR=1, DATA_LEN=1 specifies the function code 05. 1 output bit is written starting from the remote address 0.
- The combination MB_MODE=1, MB_DATA_ADDR=1, DATA_LEN=2 specifies the function code 15. 2 output bits are written starting from the remote address 0.

The following table shows the relationship between the input parameters MB_MODE, MB_DATA_ADDR, DATA_LEN of the "MB_CLIENT" instruction and the associated Modbus function.

| MB_MODE | MB_DATA_ADDR | DATA_LEN | Modbus function | Function and data type |
| --- | --- | --- | --- | --- |
| 0 | 1 to 9,999 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 9,998 |
| 0 | 10,001 to 19,999 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 9,998 |
| 0 | 40,001 to 49,999 | 1 to 125 | 03 | Read 1 to 125 holding registers on the remote address 0 to 9,998 |
| 0 | 30,001 to 39,999 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 9,998 |
| 1 | 1 to 9,999 | 1 | 05 | Write 1 output bit on the remote address 0 to 9,998 |
| 1 | 40,001 to 49,999 | 1 | 06 | Write 1 holding register on the remote address 0 to 9,998 |
| 1 | 1 to 9,999 | 2 to 1,968 | 15 | Write 2 to 1,968 output bits on the remote address 0 to 9,998 |
| 1 | 40,001 to 49,999 | 2 to 123 | 16 | Write 2 to 123 holding registers on the remote address 0 to 9,998 |
| 2 | 1 to 9,999 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 9,998 |
| 2 | 40,001 to 49,999 | 1 to 123 | 16 | Write 1 to 123 holding registers on the remote address 0 to 9,998 |
| 11 | The MB_DATA_ADDR and DATA_LEN parameters are not evaluated when this function is executed. |  | 11 | Read status word and event counter of the server:  - The status word reflects the the processing status (0 - not processing, 0xFFFF - processing). - The event counter is incremented when the Modbus request was executed successfully. If an error occurred during execution of a Modbus function, a message is sent by the server but the event counter is not incremented. |
| 80 | - | 1 | 08 | Check the server status with the diagnostic code 0x0000 (return loop test - the server sends the request back):  - 1 WORD per call |
| 81 | - | 1 | 08 | Reset the event counter of the server with the diagnostic code 0x000A:  - 1 WORD per call |
| 3 to 10, 12 to 79, 82 to 255 |  |  |  | Reserved |

> **Note**
>
> **Unit Identifier for RTU devices over MB TCP**
>
> You can find the Unit Identifier for RTU devices over Modbus TCP as "MB_Unit_ID" tag in the editable static tags of the instance data block of the instruction "MB_CLIENT". The Unit Identifier is used for unique assignment of the coupling partners.

---

**See also**

[Description of MB_CLIENT (S7-1200)](#description-of-mb_client-s7-1200)

#### MB_DATA_PTR parameter (S7-1200)

##### Description

The MB_DATA_PTR parameter is a pointer to a data buffer for storing the data read from or written to the Modbus server. As the data buffer, you can use a global data block or a memory area (M).

For a buffer in the memory area (M), use a pointer in the ANY format as follows: "P#bit address" "data type" "length" (example: P#M1000.0 WORD 500).

The MB_DATA_PTR parameter uses a communications buffer:

- For the communication functions of the "MB_CLIENT" instruction:

  - Reading and writing of 1 bit of data of the Modbus server addresses 00001 to 09999 and 10001 to 19999.
  - Reading of 16-bit WORD data of the Modbus server addresses 30001 to 39999 and 40001 to 49999.
  - Writing 16-bit WORD data of the Modbus server addresses 40001 to 49999.
- During data transmission (length: bit or WORD) from or to the global DB or the memory area (M) that you assigned with the MB_DATA_PTR parameter.

If you use a data block for the buffer in the MB_DATA_PTR parameter, you will need to assign data types to the DB elements.

- Use the 1-bit data type BOOL for a Modbus bit address
- Use a 16-bit data type such as WORD, UINT, INT or REAL for a Modbus WORD address.
- Use a 32-bit data type (double word) such as DWORD, DINT or REAL for two Modbus WORD addresses.
- With MB_DATA_PTR, you can also access complex DB elements such as:

  - Standard arrays
  - Structures with unique element names
  - Complex structures with unique naming of the elements and data type lengths of 16 or 32 bits.
- The data areas for the MB_DATA_PTR parameter can also be in different global data blocks (or in different memory areas). You can, for example, use a data block for the the read jobs and another one for the write jobs or a separate data block for each "MB_CLIENT" station.

---

**See also**

[Description of MB_CLIENT (S7-1200)](#description-of-mb_client-s7-1200)

#### Parameter STATUS  (S7-1200)

##### Parameter STATUS (general status information) (library version V2.1)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 7000 | No call active (REQ=0). |
| 7001 | First call with REQ=1: Processing started; BUSY has the value 1. |
| 7002 | Intermediate call (REQ  irrelevant). Processing already active; BUSY has the value 1. |
| 7003 | Connection is being terminated. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (general status information) (library version V3.x)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 7000 | No call active (REQ=0). |
| 7001 | First call with REQ=1: Processing started; BUSY has the value 1. |
| 7002 | Intermediate call (REQ irrelevant). Processing already active; BUSY has the value 1. |
| 7003 | Terminating connection. |
| 7004 | Connection established and monitored. No job processing active. |
| 7005 | Data was sent. |
| 7006 | Data was received. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (protocol error)

| STATUS* (W#16#) | Local and/or remote errors | Error code in the answer from MB_SERVER (B#16#) | Description |
| --- | --- | --- | --- |
| 80C8 | Local | - | No response of the server in the defined period. Check the connection to the Modbus server. This error is only reported on completion of the configured repeated attempts.   If the "MB_CLIENT" instruction does not receive an answer with the originally transferred transaction ID (MB_TRANSACTION_ID tag) within the defined period, this error code is output. |
| 8380 | Local | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | Remote | 01 | Function code is not supported. |
| 8382 | Local | - | - The length of the Modbus frame in the frame header does not match the number of received bytes. - The number of bytes does not match the number of actually transmitted bytes (only functions 1-4). For example, this is the case when "MB_CLIENT" requests an odd number of words, but "MB_SERVER" always sends an even number of words. - The start address in the received frame does not match the saved start address (functions 5, 6, 15, 16). - The number of words does not match the number of actually transmitted words (functions 15 and 16). |
| Remote | 03 | Invalid length specification in received Modbus frame. Check the server side. |  |
| 8383 | Local | - | Error reading or writing data or access outside the address area of [MB_DATA_PTR](#mb_data_ptr-parameter-s7-1200). |
| Remote | 02 | Error reading or writing data or access outside the address area of the server |  |
| 8384 | Local | - | - Invalid exception code received. - A different data value was received than was originally sent by the client (functions 5, 6 and 8). - Invalid status value received (function 11) |
| Remote | 03 | Error in data value for function 5 |  |
| 8385 | Local | - | - Diagnostics code not supported. - A different subfunction code was received than was originally sent by the client (function 8). |
| Remote | 03 | Diagnostics code not supported |  |
| 8386 | Local | - | Received function code does not match the one sent originally. |
| 8387 | Local | - | - The assigned connection ID is different from that used for previous requests. Only one connection ID can be used for each instance DB of the "MB_CLIENT" instruction. - The error code is also output when the ID of the Modbus TCP protocol received by the server is not "0". |
| 8388 | Local | - | The Modbus server sent a different data length than was requested. This error occurs only when using the Modbus functions 15 or 16. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |  |

##### Parameter STATUS (parameter error)

In addition to the errors listed in the following table, errors are also possible with the "MB_CLIENT" instruction caused by the communications instructions ("TCON", "TDISCON", "TSEND" and "TRCV").

| STATUS* (W#16#) | Description |
| --- | --- |
| 80BB | Invalid value at ACTIVE_EST parameter (identifier for the type of connection establishment, see T_CON_PARAM):   - Only passive connection establishment permitted for server (ACTIVE_EST = FALSE). - Only active connection establishment permitted for client (ACTIVE_EST = TRUE). |
| 8188 | The MB_MODE parameter has an invalid value. |
| 8189 | Invalid addressing of data at the MB_DATA_ADDR parameter. |
| 818A | Invalid data length at the MB_DATA_LEN parameter. |
| 818B | The MB_DATA_PTR parameter has an invalid pointer. You should also check the values of the [MB_DATA_ADDR](#mb_mode-mb_data_addr-and-data_len-parameters-s7-1200) and MB_DATA_LEN parameters. |
| 818C | - The [MB_DATA_PTR](#description-of-mb_client-s7-1200) pointer references an an optimized data block. Either use a data block with standard access or a memory area. - Timeout at parameter BLOCKED_PROC_TIMEOUT (see static tags of instruction). The limit of 55 seconds has been exceeded. |
| 8200 | - A further Modbus request is currently being processed via the port. - Another instance of MB_CLIENT with the same connection parameters is processing an existing Modbus request. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

> **Note**
>
> **Error codes of internally used communications instructions.**
>
> With the "MB_CLIENT" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND" and "TRCV") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_CLIENT" instruction. The error codes are displayed for the respective instruction under STATUS in the Static section.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

---

**See also**

[MB_HOLD_REG parameter (S7-1200)](#mb_hold_reg-parameter-s7-1200)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

### MB_SERVER: Communicating via PROFINET as a Modbus TCP server (S7-1200)

This section contains information on the following topics:

- [Description of MB_SERVER (S7-1200)](#description-of-mb_server-s7-1200)
- [MB_HOLD_REG parameter (S7-1200)](#mb_hold_reg-parameter-s7-1200)
- [Parameter STATUS (S7-1200)](#parameter-status-s7-1200-1)

#### Description of MB_SERVER (S7-1200)

##### Description

The "MB_SERVER" instruction communicates as a Modbus TCP server via the PROFINET connection of the S7-1200 CPU. To use the instruction, you do not require any additional hardware module. The "MB_SERVER" instruction processes connection requests of a Modbus TCP client, receives requests from Modbus functions and sends responses.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security information**  Note that each client of the network is given read and write access to the process image inputs and outputs and to the data block or bit memory area defined by the Modbus holding register.  The option is available to restrict access to an IP address to prevent unauthorized read and write operations. Note, however, that the shared address can also be used for unauthorized access. |  |

##### Parameters

The following table shows the parameters of the "MB_SERVER" instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DISCONNECT | Input | BOOL | The instruction "MB_SERVER" enters into a passive connection with a partner module, which means the server responds to a TCP connection request from each requesting IP address. You can use this parameter to control when a connection request is accepted:  - 0: A passive connection is established when there is no communications connection. - 1: Initialization of the connection termination. If the input is set, no other operations are executed. The value 7003 is output at the STATUS parameter after successful connection termination. |
| CONNECT_ID | Input | UINT | The parameter uniquely identifies a connection within the CPU. Each individual instance of the instructions "[MB_CLIENT](#description-of-mb_client-s7-1200)" and "MB_SERVER" must have a unique CONNECT_ID parameter. |
| IP_PORT | Input | UINT | Start value=502. The number of the IP port defines which IP port is monitored for connection requests of the Modbus client.   The following TCP port numbers must not be used for the passive connection of the "MB_SERVER" instruction: 20, 21, 25, 80, 102, 123, 5001, 34962, 34963 and 34964. |
| [MB_HOLD_REG](#mb_hold_reg-parameter-s7-1200) | InOut | VARIANT | Pointer to the Modbus holding register of the "MB_SERVER" instruction: Use a global data block with standard access as holding register. The holding register contains the values that may be accessed by a Modbus client using the Modbus functions 3 (read), 6 (write) and 16 (read). |
| NDR | Output | BOOL | "New Data Ready":  - 0: No new data - 1: New data written by the Modbus client written |
| DR | Output | BOOL | "Data Read":  - 0: No data read - 1: Data read by the Modbus client |
| ERROR | Output | BOOL | If an error occurs during the call of the "MB_SERVER" instruction, the output of the ERROR parameter is set to TRUE. Detailed information about the cause of the problem is indicated by the STATUS parameter. |
| [STATUS](#parameter-status-s7-1200-1) | Output | WORD | Error code of the instruction. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Mapping of Modbus addresses to the process image

The "MB_SERVER" instruction allows incoming Modbus functions (1, 2, 4, 5 and 15) direct read and write access to the process image input and output of the S7-1200 CPU (use of the data types BOOL and WORD).

For the data transfer of the function codes 3, 6 and 16, the holding register (MB_HOLD_REG parameter) must be defined longer than one byte. The following table shows the mapping of the Modbus addresses to the process image of the CPU.

| Modbus function |  |  |  |  |  | S7-1200 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Code** | **Function** | **Data area** | **Address space** |  |  | **Data area** | **CPU address** |
| 01 | Read: Bits | Output | 0 | to | 8191 | Process image output | Q0.0 to Q1023.7 |
| 02 | Read: Bits | Input | 0 | to | 8191 | Process image input | I0.0 to I1023.7 |
| 04 | Read: WORD | Input | 0 | to | 1021 | Process image input | IW0 to IW1022 |
| 05 | Write: Bits | Output | 0 | to | 8191 | Process image output | Q0.0 to Q1023.7 |
| 15 | Write: Bits | Output | 0 | to | 8191 | Process image output | Q0.0 to Q1023.7 |

Incoming Modbus alarms with the function codes 3, 6 and 16 write to or read from the Modbus holding registers (you specify the holding registers with the MB_HOLD_REG parameter).

##### Multiple server connections

You can create multiple Server connections. This allows a single CPU to establish connections to more than one Modbus TCP client at the same time.

A Modbus TCP server can support several TCP connections and the maximum number of connections depends on the CPU being used.

The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections.

Modbus TCP connections can also be shared by client and/or server connections.

In the case of Server connections, remember the following rules:

- Each "MB_SERVER" connection must use a unique instance DB.
- Each "MB_SERVER" connection must be created with a unique IP port number. Only one connection is supported for each port.
- Each "MB_SERVER" connection must use a unique connection ID.

  The relevant individual connection ID must be used for each individual instance DB of the instruction. The connection ID and instance DB belong together in pairs and must be unique for each connection.
- For each connection, the "MB_SERVER" instruction must be called individually.

##### Modbus diagnostics functions

The table below contains a description of the Modbus diagnostics functions.

| Code | Subfunction | Description |
| --- | --- | --- |
| 08 | 0x0000 | Echo test: The "MB_SERVER" instruction receives a data word and returns this unchanged to the Modbus master. |
| 08 | 0x000A | Reset event counter: The "MB_SERVER" instruction resets the event counter for communication that is used for Modbus function 11. |
| 11 | - | Fetch event counter of the communication: The "MB_SERVER" instruction uses an internal event counter for communication to record the number of successfully executed read and write requests sent to the Modbus server.  The event counter is not incremented by the functions 8, 11 or broadcast requests. The same applies to requests that result in a communications error (for example parity errors or CRC errors). The broadcast function is not available for Modbus TCP because only one client/server connection can exist at any one time. |

##### Static tags of the instruction

The following table describes the static tags of the instance data block of the "MB_SERVER" instruction used in the program. You can write the HR_Start_Offset tag. You can read the other tags to monitor the Modbus status.

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| HR_Start_Offset | WORD | 0 | Assign the start address of the Modbus holding register. |
| Request_Count | WORD | 0 | Total number of requests received by the server. |
| Server_Message_Count | WORD | 0 | Total number of received alarms for the relevant server. |
| Xmt_Rcv_Count | WORD | 0 | Counter for detecting the number of transfers during which an error occurred. The counter is also incremented if an invalid Modbus alarm is received. |
| Exception_Count | WORD | 0 | Counter for detecting the number of errors specifically for Modbus cause an exception. |
| Success_Count | WORD | 0 | Counter for detecting the number of requests that contain no error in the transferred protocol. |
| Connected | BOOL | 0 | Indicates whether the connection to the assigned client has been established or not: 1 = connected, 0 = not connected. |

##### Example: Addressing via static tag HR_Start_Offset

The addresses of the Modbus holding register start at 0 (from the perspective of the MB_CLIENT at 40.001). These addresses correspond to the address area of the CPU memory area for the holding register. You can also define the HR_Start_Offset tag so that the Modbus holding register has a start address other than 0.

Example: The holding register begins at MW100, and has a length of 100 WORD. An offset value in the HR_Start_Offset parameter means that the start address of the holding register is moved from 0 to 20. This causes an error whenever the holding register is addressed below the address 20 and above the address 119.

| HR_Start_Offset | Address | Minimum | Maximum |
| --- | --- | --- | --- |
| 0 | Modbus address (WORD) | 0 | 99 |
| CPU address | MW100 | MW298 |  |
| 20 | Modbus address (WORD) | 20 | 119 |
| CPU address | MW100 | MW298 |  |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[MB_SERVER example: Multiple TCP connections (S7-1200)](#mb_server-example-multiple-tcp-connections-s7-1200)

#### MB_HOLD_REG parameter (S7-1200)

##### Description

The MB_HOLD_REG parameter is a pointer to a data buffer for storing the data read from or written to the Modbus server. As the data buffer, you can use a global data block or a memory area (M).

- The high limit for the number of addresses in the data block (D) is determined by the maximum work memory of the CPU.
- The high limit for the number of bit memories (M) is determined by the size of the CPU memory area.

The following table shows examples of mapping Modbus addresses to the holding register for the Modbus functions 3 (read WORD), 6 (write WORD), 16 (write several WORD) and 23 (write and read several words).

| Modbus addresses | MB_HOLD_REG parameter - examples |  |  |
| --- | --- | --- | --- |
| 0 | MW100 | DB10.DBW0 | "Recipe".ingredient[1] |
| 1 | MW102 | DB10.DBW2 | "Recipe".ingredient[2] |
| 2 | MW104 | DB10.DBW4 | "Recipe".ingredient[3] |
| 3 | MW106 | DB10.DBW6 | "Recipe".ingredient[4] |
| 4 | MW108 | DB10.DBW8 | "Recipe".ingredient[5] |

---

**See also**

[Description of MB_SERVER (S7-1200)](#description-of-mb_server-s7-1200)

#### Parameter STATUS (S7-1200)

##### Parameter STATUS (general status information) (library version V2.1)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 7000 | No call active (REQ=0). |
| 7001 | First call with REQ=1: Processing started; BUSY has the value 1. |
| 7002 | Intermediate call (REQ  irrelevant). Processing already active; BUSY has the value 1. |
| 7003 | Connection is being terminated. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (general status information) (library version V3.x)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 7000 | No call active (REQ=0). |
| 7001 | First call. Connection establishment triggered. |
| 7002 | Intermediate call. Establishing connection. |
| 7003 | Terminating connection. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (protocol error)

| STATUS* (W#16#) | Error code in the answer from MB_SERVER (B#16#) | Description |
| --- | --- | --- |
| 8380 | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | 01 | Function code is not supported. |
| 8382 | 03 | Error in data length |
| 8383 | 02 | Error in the data address or access outside the address area of [MB_HOLD_REG](#mb_hold_reg-parameter-s7-1200). |
| 8384 | 03 | Error in the data value (function 5) |
| 8385 | 03 | Diagnostics code not supported |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Parameter STATUS (parameter error)

| STATUS* (W#16#) | Description |
| --- | --- |
| 80BB | Invalid value at ACTIVE_EST parameter (identifier for the type of connection establishment, see T_CON_PARAM):   - Only passive connection establishment permitted for server (ACTIVE_EST = FALSE). - Only active connection establishment permitted for client (ACTIVE_EST = TRUE). |
| 8187 | The MB_HOLD_REG parameter has an invalid pointer. Data area is too small. |
| 818C | - The pointer at parameter MB_HOLD_REG references an optimized data block. Either use a data block with standard access or a memory area. - Error due to timeout of execution (more than 55 seconds). |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

> **Note**
>
> **Error codes of internally used communications instructions.**
>
> With the "MB_SERVER" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND" and "TRCV") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_SERVER" instruction. The error codes are displayed for the respective instruction under STATUS in the Static section.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

---

**See also**

[Description of MB_SERVER (S7-1200)](#description-of-mb_server-s7-1200)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

### Examples (S7-1200)

This section contains information on the following topics:

- [MB_CLIENT example 1: Send several requests via a TCP connection (S7-1200)](#mb_client-example-1-send-several-requests-via-a-tcp-connection-s7-1200)
- [MB_CLIENT example 2: Send multiple requests via several TCP connections (S7-1200)](#mb_client-example-2-send-multiple-requests-via-several-tcp-connections-s7-1200)
- [MB_CLIENT example 3: Coordinate several requests (S7-1200)](#mb_client-example-3-coordinate-several-requests-s7-1200)
- [MB_SERVER example: Multiple TCP connections (S7-1200)](#mb_server-example-multiple-tcp-connections-s7-1200)

#### MB_CLIENT example 1: Send several requests via a TCP connection (S7-1200)

##### Description

Several requests of the Modbus Client can be sent via a TCP connection. To do this, use the same instance DB, the same connection ID and the same port number.

Only one client can be active at any one time. After processing of a client has been completed, the next client is processed. The order of execution must be defined in the program.

In the following sample program, the value of the STATUS output parameter is also copied.

##### Network 1: Modbus function 1 - 16 read output bits

![Network 1: Modbus function 1 - 16 read output bits](images/31127658379_DV_resource.Stream@PNG-de-DE.png)

##### Network 2: Modbus function 2 - 32 read input bits

![Network 2: Modbus function 2 - 32 read input bits](images/31128332683_DV_resource.Stream@PNG-de-DE.png)

#### MB_CLIENT example 2: Send multiple requests via several TCP connections (S7-1200)

##### Description

Requests from the Modbus client can be sent via different TCP connections. If you require this, use a different instance DB and a different connection ID.

Use a different port number, if the connections are to the same Modbus server. If the connections are to different Modbus servers, you can freely assign the port number.

##### Network 1: Modbus function 4 - read input (WORD)

![Network 1: Modbus function 4 - read input (WORD)](images/31128812939_DV_resource.Stream@PNG-de-DE.png)

##### Network 2: Modbus function 3 - read holding register (WORD)

![Network 2: Modbus function 3 - read holding register (WORD)](images/31129372043_DV_resource.Stream@PNG-de-DE.png)

#### MB_CLIENT example 3: Coordinate several requests (S7-1200)

##### Description

Make sure that the individual Modbus requests are executed. You control coordination of requests with the program. The following example demonstrates how the output parameters of the first and second client request can be used to coordinate execution of the instructions.

##### Network 1: Modbus function 3 - read holding register (WORD)

![Network 1: Modbus function 3 - read holding register (WORD)](images/31131049995_DV_resource.Stream@PNG-de-DE.png)

##### Network 2: Modbus function 3 - read holding register (WORD)

![Network 2: Modbus function 3 - read holding register (WORD)](images/31131148299_DV_resource.Stream@PNG-de-DE.png)

#### MB_SERVER example: Multiple TCP connections (S7-1200)

##### Description

You can use several Modbus TCP server connections. To do this, the "MB_SERVER" instruction must be called independently for each connection.

Every connection requires the following:

- An independent instance data block of the instruction
- A unique connection ID
- A separate IP port (on the S7-1200, only one connection is permitted per IP port)

To optimize the performance "MB_SERVER" should be executed once per program cycle for each connection.

##### Network 1: Connection #1 with associated IP port connection ID and instance DB

![Network 1: Connection #1 with associated IP port connection ID and instance DB](images/31126060555_DV_resource.Stream@PNG-de-DE.png)

##### Network 2: Connection #1 with associated IP port connection ID and instance DB

![Network 2: Connection #1 with associated IP port connection ID and instance DB](images/31126363403_DV_resource.Stream@PNG-de-DE.png)

## MODBUS (TCP) for the library versions V4.0 and later of the S7-1200 CPUs and as of V3.x of the S7-1500 CPUs (S7-1200, S7-1500)

This section contains information on the following topics:

- [MB_CLIENT: Communicating via PROFINET as a Modbus TCP client (S7-1200, S7-1500)](#mb_client-communicating-via-profinet-as-a-modbus-tcp-client-s7-1200-s7-1500)
- [MB_SERVER: Communicating via PROFINET as a Modbus TCP server (S7-1200, S7-1500)](#mb_server-communicating-via-profinet-as-a-modbus-tcp-server-s7-1200-s7-1500)
- [Differences between the versions <= V3.x and >= V4.0 of the Modbus TCP library (S7-1200, S7-1500)](#differences-between-the-versions-v3x-and-v40-of-the-modbus-tcp-library-s7-1200-s7-1500)

### MB_CLIENT: Communicating via PROFINET as a Modbus TCP client (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description of MB_CLIENT (S7-1200, S7-1500)](#description-of-mb_client-s7-1200-s7-1500)
- [REQ and DISCONNECT parameters (S7-1200, S7-1500)](#req-and-disconnect-parameters-s7-1200-s7-1500)
- [MB_MODE, MB_DATA_ADDR and MB_DATA_LEN parameters (S7-1200, S7-1500)](#mb_mode-mb_data_addr-and-mb_data_len-parameters-s7-1200-s7-1500)
- [MB_DATA_PTR parameter (S7-1200, S7-1500)](#mb_data_ptr-parameter-s7-1200-s7-1500)
- [Modbus function 23 (S7-1200, S7-1500)](#modbus-function-23-s7-1200-s7-1500)
- [CONNECT parameter (S7-1200, S7-1500)](#connect-parameter-s7-1200-s7-1500)
- [Parameter STATUS (S7-1200, S7-1500)](#parameter-status-s7-1200-s7-1500)

#### Description of MB_CLIENT (S7-1200, S7-1500)

##### Description

The "MB_CLIENT" instruction communicates as a Modbus TCP client via the PROFINET connection. With the "MB_CLIENT" instruction, you establish a connection between the client and the server, send Modbus requests and receive responses and control connection termination of the Modbus TCP client.

For the S7-1200 with firmware version V4.0 you can use the "MB_CLIENT" instruction up to and including library version V3.1. With the S7-1200 as of firmware version V4.1 and the S7-1500, you can use the "MB_CLIENT" instruction of all library versions.

The connection can take place via the local interface of the CPU or CM/CP.

To use the instruction, you do not require an additional hardware module.

As of instruction version V6.0, you can use the Modbus function 23. It is used to write data to the Modbus server and read data from the Modbus server in one job.

See: [Modbus function 23](#modbus-function-23-s7-1200-s7-1500)

##### Multiple client connections

A Modbus TCP client can support several TCP connections and the maximum number of connections depends on the CPU being used. The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections. Modbus TCP connections can also be shared by "MB_CLIENT" and/or "MB_SERVER" instances.

With individual client connections, remember the following rules:

- Each "MB_CLIENT" connection must use a unique instance DB.
- For each "MB_CLIENT" connection, a unique server IP address must be specified.
- Each "MB_CLIENT" connection requires a unique connection ID.

  The relevant individual connection ID must be used for each individual instance DB of the instruction. The connection ID and instance DB belong together in pairs and must be unique for each connection.
- Unique numbers for the IP port may or may not be required depending on the server configuration.

##### Parameters

The following table shows the parameters of the "MB_CLIENT" instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| [REQ](#req-and-disconnect-parameters-s7-1200-s7-1500) | Input | BOOL | Modbus query to the Modbus TCP server  The REQ parameter is level-controlled. This means that as long as the input is set (REQ=true), the instruction sends communication requests.  - After the Modbus query has started, the instance DB is locked for other clients. - Changes to the input parameters will not become effective until the server has responded or an error message has been output. - If the parameter REQ is set again during an ongoing Modbus request, no additional transmission takes place afterwards. |
| [DISCONNECT](#req-and-disconnect-parameters-s7-1200-s7-1500) | Input | BOOL | With this parameter, you control the establishment and termination of the connection to the Modbus server:  - 0: Establish communications connection to the connection partner configured at the CONNECT parameter (see CONNECT parameter). - 1: Disconnect the communication connection. No other function is executed during connection termination. The value 0003 is output at the STATUS parameter after successful connection termination.   The Modbus request is sent immediately if the REQ parameter is set during connection establishment. |
| [MB_MODE](#mb_mode-mb_data_addr-and-mb_data_len-parameters-s7-1200-s7-1500) | Input | USINT | Selects the mode of the Modbus request (read, write or diagnostics) or direct selection of a Modbus function |
| [MB_DATA_ADDR](#mb_mode-mb_data_addr-and-mb_data_len-parameters-s7-1200-s7-1500) | Input | UDINT | depends on MB_MODE  Note: This parameter is not used for Modbus function 23 and it must have its default value as the value. |
| MB_DATA_LEN | Input | UINT | Data length: Number of bits or words for the data access (see [MB_MODE, MB_DATA_ADDR and MB_DATA_LEN parameters](#mb_mode-mb_data_addr-and-mb_data_len-parameters-s7-1200-s7-1500)).   Note: This parameter is not used for Modbus function 23 and it must have its default value as the value. |
| [MB_DATA_PTR](#mb_data_ptr-parameter-s7-1200-s7-1500) | InOut | VARIANT | Pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server.  Note: This parameter is not used for Modbus function 23 and it must have its default value as the value. |
| [CONNECT](#connect-parameter-s7-1200-s7-1500) | InOut | VARIANT | Pointer to the structure of the connection description  The following structures (system data types) can be used:  - TCON_IP_v4: Includes all address parameters that are required for establishing a programmed connection. When using TCON_IP_v4, the connection is established when calling the "MB_CLIENT" instruction. - TCON_Configured: Includes the address parameters of a configured connection. When using TCON_Configured, an existing connection is used that was created by the CPU after download of the hardware configuration.   For instruction versions > V4.1 of MB_CLIENT, the following connection descriptions for TCP are also possible:  - TCON_IP_V4_SEC (firmware version V4.3 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters according to TCON_IP_V4_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500) - TCON_QDN (firmware version V4.4 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters in accordance with TCON_QDN](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn-s7-1500) - TCON_QDN_SEC (firmware version V4.4 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters in accordance with TCON_QDN_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)   For more information on secure connections, see [Secure Open User Communication](Configuring%20devices%20and%20networks.md#secure-open-user-communication-s7-1500-s7-1500t) |
| DONE | Out | BOOL | The bit at output parameter DONE is set to "1" as soon as the last Modbus job is completed without errors. |
| BUSY | Out | BOOL | - 0: No Modbus request in progress - 1: Modbus request being processed  The output parameter BUSY is not set during connection establishment and termination. |
| ERROR | Out | BOOL | - 0: No error - 1: Error occurred. The cause of error is indicated by the STATUS parameter. |
| [STATUS](#parameter-status-s7-1200-s7-1500) | Out | WORD | Detailed status information of the instruction. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **Consistent input data during an "MB_CLIENT" call**
>
> When a Modbus client instruction is called, the values of the input parameters are stored internally and then compared at the next call. The comparison is used to determine whether this particular call initialized the current request. Several "MB_CLIENT" calls can be executed if you use a common instance DB. The values of the input parameters must not be changed while an "MB_CLIENT" instance is being executed. If the input parameters are changed during execution, "MB_CLIENT" cannot be used to check whether or not the instance is currently being executed.

##### Static tags of the instruction

The following table describes the editable static tags of the instance data block of the "MB_CLIENT" instruction.

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| Blocked_Proc_Timeout | REAL | 3.0 | Wait time in seconds before the static tag ACTIVE is reset if there is a blocked Modbus instance. This can, for example, occur if a client request is output and the execution of the client function aborts before the request was fully executed. The wait time must be between 0.5 s and 55 s. |
| MB_Transaction_ID | WORD | 1 | Transaction ID of the Modbus TCP protocol. The start value of "1" should only be changed if the Modbus TCP server requires a different value. |
| MB_Unit_ID | BYTE | 255 | Unit Identifier  Modbus device detection:  A Modbus TCP server is addressed using its IP address. For this reason, the MB_UNIT_ID parameter is not used in the case of Modbus TCP addressing.  The MB_UNIT_ID parameter corresponds to the field of the slave address in the Modbus RTU protocol. If a Modbus TCP server is used as a gateway for a Modbus RTU protocol, the slave device in the serial network can be identified using MB_UNIT_ID. The MB_UNIT_ID parameter would in this case forward the request to the correct Modbus RTU slave address.  Please note that some Modbus TCP devices may require the MB_UNIT_ID parameter for the initialization within a limited value range.  Use the following links to get more information on the MB_Unit_ID parameter:   [https://support.industry.siemens.com/cs/ww/en/view/102420337](https://support.industry.siemens.com/cs/document/102420337/what-is-the-function-of-the-mb_unit_id-in-the-instance-data-block-of-the-modbus-block-mb_client?dti=0&dl=en&lc=de-WW)    [http://support.automation.siemens.com/WW/view/en/109736516](https://support.industry.siemens.com/cs/document/109736516/how-do-you-clear-the-status-168382-in-the-case-of-a-modbus-tcp-connection-between-simatic-s7-1500-s7-1200-and-sentron-pac-devices?dti=0&dl=en&lc=de-WW) |
| RCV_TIMEOUT | REAL | 2.0 | Time interval in seconds in which the "MB_CLIENT" instruction waits for a response from the server. It must be between 0.5 s and 55 s. |
| Connected | BOOL | 0 | Indicates whether the connection to the assigned server has been established or not: 1 = connected, 0 = not connected. |
| RETRIES | WORD | 0 | Number of send attempts made by the "MB_CLIENT" instruction before it returns the error W#16#80C8. |

> **Note**
>
> **Tag MB_Transaction_ID**
>
> If the transaction ID in the answer of the Modbus TCP server does not match the transaction ID of the job from "MB_CLIENT", the "MB_CLIENT" instruction waits for the time period RCV_TIMEOUT * RETRIES for the answer of the Modbus TCP server with the correct transaction ID; once this time has expired, it returns the error W#16#80C8.

##### Example

An example project for the Modbus TCP communication between two S7-1500 CPUs can be found in the Service and Support Portal under Entry ID [94766380](http://support.automation.siemens.com/WW/view/en/94766380).

Two Modbus functions are used in this example. For each Modbus function, a Modbus TCP connection is established using a Modbus block pair (MB_CLIENT and MB_SERVER).

![Example](images/102575198859_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### REQ and DISCONNECT parameters (S7-1200, S7-1500)

##### Description

If no job is active and if the value of the DISCONNECT parameter is "0", a new job executes if REQ=1. If there is not yet a connection, this is established during execution.

If the same instance of the "MB_CLIENT" instruction executes again (DISCONNECT = 0 and REQ = 1), before the active job was executed, this is not executed on completion of the active job. A new job can only be started on completion of the active job (REQ = 1).

The status of the execution is output by the output parameters. You can use it to monitor the execution status when the "MB_CLIENT" instruction is executed sequentially.

#### MB_MODE, MB_DATA_ADDR and MB_DATA_LEN parameters (S7-1200, S7-1500)

##### Description

The combination of the MB_MODE, MB_DATA_ADDR and MB_DATA_LEN parameters defines the Modbus function code used in the current Modbus message for the values 0, 1 and 2 of MB_MODE:

- MB_MODE contains the information on whether to read or to write.

  MB_MODE=0: Read, MB_MODE=1 and 2: Write (Note: With MB_MODE=2, there is not distinction between Modbus functions 15 and 05 or between Modbus functions 16 and 06.)
- MB_DATA_ADDR contains the information on what is to be read or written, as well as address information from which the "MB_CLIENT" instruction calculates the remote address.
- MB_DATA_LEN contains the number of values to be read/written.

Examples:

- The combination MB_MODE=1, MB_DATA_ADDR=1, MB_DATA_LEN=1 specifies the function code 05. 1 output bit is written starting from the remote address 0.
- The combination MB_MODE=1, MB_DATA_ADDR=1, MB_DATA_LEN=2 specifies the function code 15. 2 output bits are written starting from the remote address 0.

The following applies to the values 101 to 106 and 115 to 116 from MB_MODE:

- MB_MODE defines the Modbus function code.
- MB_DATA_ADDR contains the remote address.
- MB_DATA_LEN contains the number of values to be read/written.

Example:

- MB_MODE=104, MB_DATA_ADDR=17,834, MB_DATA_LEN=125

  - MB_MODE=104 defines the function code 04 (read input words).
  - MB_DATA_ADDR=17,834 defines the remote address 17,834.
  - MB_DATA_LEN=125 defines that 125 values are read.

The following table shows the relationship between the input parameters MB_MODE, MB_DATA_ADDR, MB_DATA_LEN of the "MB_CLIENT" instruction and the associated Modbus function.

| MB_MODE | MB_DATA_ADDR | MB_DATA_LEN | Modbus function | Function and data type |
| --- | --- | --- | --- | --- |
| 0 | 1 to 9,999 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 9,998 |
| 0 | 10,001 to 19,999 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 9,998 |
| 0 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 125 | 03 | - Read 1 to 125 holding registers on the remote address 0 to 9,998 - Read 1 to 125 holding registers on the remote address 0 to 65,534 |
| 0 | 30,001 to 39,999 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 9,998 |
| 1 | 1 to 9,999 | 1 | 05 | Write 1 output bit on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 | 06 | - Write 1 holding register on the remote address 0 to 9,998 - Write 1 holding register on the remote address 0 to 65,534 |
| 1 | 1 to 9,999 | 2 to 1,968 | 15 | Write 2 to 1,968 output bits on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 2 to 123 | 16 | - Write 2 to 123 holding registers on the remote address 0 to 9,998 - Write 2 to 123 holding registers on the remote address 0 to 65,534 |
| 2 | 1 to 9,999 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 9,998 |
| 2 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 123 | 16 | - Write 1 to 123 holding registers on the remote address 0 to 9,998 - Write 1 to 123 holding registers on the remote address 0 to 65,534 |
| 11 | The MB_DATA_ADDR and MB_DATA_LEN parameters are not evaluated when this function is executed. |  | 11 | Read status word and event counter of the server:  - The status word reflects the the processing status (0 - not processing, 0xFFFF - processing). - The event counter is incremented when the Modbus request was executed successfully. If an error occurred during execution of a Modbus function, a message is sent by the server but the event counter is not incremented. |
| 80 | - | 1 | 08 | Check the server status with the diagnostic code 0x0000 (return loop test - the server sends the request back):  - 1 WORD per call |
| 81 | - | 1 | 08 | Reset the event counter of the server with the diagnostic code 0x000A:  - 1 WORD per call |
| 101 | 0 to 65,535 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 65,535 |
| 102 | 0 to 65,535 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 65,535 |
| 103 | 0 to 65,535 | 1 to 125 | 03 | Read 1 to 125 holding registers on the remote address 0 to 65,535 |
| 104 | 0 to 65,535 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 65,535 |
| 105 | 0 to 65,535 | 1 | 05 | Write 1 output bit on the remote address 0 to 65,535 |
| 106 | 0 to 65,535 | 1 | 06 | Write 1 holding register on the remote address 0 to 65,535 |
| 115 | 0 to 65,535 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 65,535 |
| 116 | 0 to 65,535 | 1 to 123 | 16 | Write 1 to 123 holding registers on the remote address 0 to 65,535 |
| 123 | Not used | Not used | 23 | Write holding registers of the remote device and read holding registers of the remote device in one job.  Note: This Modbus function is supported by "MB_CLIENT" as of instruction version V6.0. The parameters RD_MB_DATA_ADDR, RD_MB_DATA_LEN, WR_MB_DATA_ADDR, WR_MB_DATA_LEN, RD_MB_DATA_PTR, WR_MB_DATA_PTR are used for this purpose.  See: [Modbus function 23](#modbus-function-23-s7-1200-s7-1500) |
| 3 to 10, 12 to 79, 82 to 100, 107 to 114, 117 to 122, 124 to 255 |  |  |  | Reserved |

> **Note**
>
> **Unit Identifier for RTU devices over MB TCP**
>
> You can find the Unit Identifier for RTU devices over Modbus TCP as "MB_Unit_ID" tag in the editable static tags of the instance data block of the instruction "MB_CLIENT". The Unit Identifier is used for unique assignment of the coupling partners.

---

**See also**

[Description of MB_CLIENT (S7-1200, S7-1500)](#description-of-mb_client-s7-1200-s7-1500)

#### MB_DATA_PTR parameter (S7-1200, S7-1500)

##### Description

The MB_DATA_PTR parameter is a pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server. As the data buffer, you can use a global data block or a memory area (M).

For a buffer in the memory area (M), use a pointer in the ANY format as follows: "P#bit address" "data type" "length" (example: P#M1000.0 WORD 500).

Depending on the memory area in which the data buffer is located, MB_DATA_PTR can reference different data structures:

- When you use a global DB with optimized access, MB_DATA_PTR can reference a tag with elementary data type or an array of elementary data types. The following data types are supported:

  | Data type | Length in bits |
  | --- | --- |
  | Bool | 1 |
  | Byte, SInt, USInt, Char | 8 |
  | Word, Int, WChar, UInt | 16 |
  | DWord, DInt, UDInt, Real | 32 |

  In such cases, all supported data types can be used for all Modbus functions. For example, MB_CLIENT can also write a received bit in a tag of the byte type to a specified address without changing other bits in this byte. Therefore, it is not necessary to have an array of bits in order to execute bit-oriented functions.
- If you use a bit memory address area or a global DB with standard access as memory area, there is no longer any restriction to the elementary data types for MB_DATA_PTR; MB_DATA_PTR can then also reference complex data structures such as PLC data types (UDTs) and system data types (SDTs).

> **Note**
>
> **Using a bit memory address area as data buffer**
>
> If you use a bit memory address area as data buffer for MB_DATA_PTR, you need to observe this variable. With S7-1500-CPUs it is 16 KB, with S7-1200-CPUs it is 8 KB.

#### Modbus function 23 (S7-1200, S7-1500)

##### Description

With the Modbus function 23, the following is carried out in a job:

1. Data is transferred from the CPU to the Modbus server and written into one or more holding registers.
2. Data is read from one or more holding registers of the Modbus server and transferred to the CPU.

The "MB_CLIENT" instruction supports the Modbus function 23 as of instruction version V6.0.

##### Parameters

When the Modbus function 23 is used, the MB_MODE parameter must have the value 123.

The parameters MB_DATA_ADDR, MB_DATA_LEN and MB_DATA_PTR are not used and must have their default values as values.

When Modbus function 23 is used, six new parameters are used, which are described in the following table. Each of these parameters starts with "RD_" or "WR_" to indicate that it belongs to the read or write task. The default is that these parameters are hidden. When using Modbus function 23, these six parameters must all be used.

If you use another Modbus function, then these six parameters must have the value 0 or they must be empty. Otherwise, the STATUS value 16#818D is returned.

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| RD_MB_DATA_ADDR | Input | UInt | Start address on the remote device as of which data is to be read.  Permitted values: 0 to 65535 |
| RD_MB_DATA_LEN | Input | UInt | Number of registers to be read from the remote device.  Permitted values: 1 to 125 |
| WR_MB_DATA_ADDR | Input | UInt | Start address on the remote device as of which data is to be written.  Permitted values: 0 to 65535 |
| WR_MB_DATA_LEN | Input | UInt | Number of registers to be written to the remote device.  Permitted values: 1 to 121 |
| RD_MB_DATA_PTR | InOut | Variant | Pointer to a data buffer for the data to be read from the Modbus server.  The same data types as for MB_DATA_PTR are permitted as data types. |
| WR_MB_DATA_PTR | InOut | Variant | Pointer to a data buffer for the data to be written to the Modbus server.  The same data types as for MB_DATA_PTR are permitted as data types. |

##### STATUS parameter

The meaning of the STATUS values 16#8383, 8189, 818A, 818B is expanded. The STATUS value 16#818D is added.

See: [Parameter STATUS](#parameter-status-s7-1200-s7-1500)

##### Upgrade project, upgrade instruction

When you upgrade an existing project (e.g. created with TIA Portal V16) with MB_CLIENT instructions (e.g. instruction version V5.2), the new instruction version is not automatically used in your program.

To use Modbus function 23, you must upgrade the instruction version manually.

#### CONNECT parameter (S7-1200, S7-1500)

##### Connection descriptions at the CONNECT parameter up to and including instruction version V4.1 of MB_CLIENT

Two different connection descriptions can be used for the "MB_CLIENT" instruction:

- Programmed connections with the structure TCON_IP_v4

  The connection parameters are stored in the TCON_IP_v4 structure and the connection is set up with the call of the instruction "MB_CLIENT".
- Configured connections with the structure TCON_Configured

  The configured connection has already been established by the CPU. Use the structure TCON_Configured to specify which existing connection is to be used for the instruction.

Each instance of the instruction "MB_CLIENT" requires a unique connection. Create a separate structure TCON_IP_v4 or TCON_Configured for each instance of the instruction to describe the connection.

##### Connection description for programmed connections

Use the following structure for connection description to TCON_IP_v4 for programmed connections at the CONNECT parameter:

- Make sure that only connections of the type TCP are specified in the TCON_IP_v4 structure.
- The connection may not use the following TCP port numbers: 20, 21, 25, 80, 102, 123, 5001, 34962, 34963 and 34964.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | - | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | - | Reference to this connection (value range: 1 to 4095).  The parameter uniquely identifies a connection within the CPU. Each individual instance of the instruction "MB_CLIENT" must use a unique ID.  Note: For S7-1500 CPUs with firmware version V2.9 or higher and S7-1200 CPUs with firmware version V4.5 or higher, ID may also have been supplied by the instruction "TCONSettings". In this case, ID is outside the value range 1 to 4095. |
| 4 | ConnectionType | BYTE | 11 | Connection type  Select 11 (decimal) for TCP. Other connection types are not permitted. If another connection type (e.g. UDP) is used, a corresponding error message is output at the STATUS parameter of the instruction. |
| 5 | ActiveEstablished | BOOL | TRUE | ID for the manner in which the connection is established  Select TRUE for active connection establishment. |
| 6 … 9 | RemoteAddress | ARRAY [1..4] of BYTE | - | IP address of the connection partner (Modbus server), for example, for 192.168.0.1:   - addr[1] = 192 - addr[2] = 168 - addr[3] = 0 - addr[4] = 1 |
| 10 … 11 | RemotePort | UINT | 502 | Port number of the remote connection partner (value range: 1 to 49151).  Use the IP port number of the server to which the client establishes the connection and communicates using the TCP/IP protocol (default value: 502). |
| 12 … 13 | LocalPort | UINT | 0 | Port number of the local connection partner:  - Port numbers: 1 to 49151 - Any port: "0" |

> **Note**
>
> **Migration of the instruction "MB_CLIENT" version 2.1**
>
> The parameters CONNECT_ID, IP_PORT and IP_OCTET_x are mapped in version 3.0 of the "MB_CLIENT" instruction in the TCON_IP_v4 structure:
>
> - The parameter CONNECT_ID of the "MB_CLIENT" V2.1 instruction corresponds to the ID parameter of TCON_IP_v4.
> - The parameter IP_PORT of the "MB_CLIENT" V2.1 instruction corresponds to the RemotePort parameter of TCON_IP_v4.
> - The four parameters IP_OCTET_x of the "MB_CLIENT" V2.1 instruction correspond to the array of the RemoteAddress parameter of TCON_IP_v4.

##### Connection description for configured connections

For programmed connections at the CONNECT parameter, use the following structure for connection description to TCON_Configured.

- Make sure that only connections of the type TCP are specified in the TCON_Configured structure.
- The connection may not use the following TCP port numbers: 20, 21, 25, 80, 102, 123, 5001, 34962, 34963 and 34964.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceId | HW_ANY | - | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | - | Reference to this connection (value range: 1 to 4095).  Enter the connection ID of the existing connection. |
| 4 | ConnectionType | BYTE | 0 | Connection type  Select 254 (decimal) for a configured connection. |

---

**See also**

[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[Secure Open User Communication (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-open-user-communication-s7-1500-s7-1500t)

#### Parameter STATUS  (S7-1200, S7-1500)

##### Parameter STATUS (general status information)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 7000 | No job active and no connection established (REQ=0, DISCONNECT=1). |
| 7001 | Connection establishment triggered. |
| 7002 | Intermediate call. Connection is being established. |
| 7003 | Connection is being terminated. |
| 7004 | Connection established and monitored. No job processing active. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (protocol error)

| STATUS* (W#16#) | Local and/or remote errors | Error code in the answer from MB_SERVER (B#16#) | Description |
| --- | --- | --- | --- |
| 80C8 | Local | - | No response of the server in the defined period. Check the connection to the Modbus server. This error is only reported on completion of the configured repeated attempts.   If the "MB_CLIENT" instruction does not receive an answer with the originally transferred transaction ID (see static tag MB_TRANSACTION_ID) within the defined period, this error code is output. |
| 8380 | Local | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | Remote | 01 | Function code is not supported. |
| 8382 | Local | - | - The length of the Modbus frame in the frame header does not match the number of received bytes. - The number of bytes does not match the number of actually transmitted bytes (only functions 1-4). For example, this is the case when "MB_CLIENT" requests an odd number of words, but "MB_SERVER" always sends an even number of words. - The start address in the received frame does not match the saved start address (functions 5, 6, 15, 16). - The number of words does not match the number of actually transmitted words (functions 15 and 16). |
| Remote | 03 | Invalid length specification in received Modbus frame. Check the server side. |  |
| 8383 | Local | - | - Instruction version < V6.0: Error reading or writing data or access outside the address area of [MB_DATA_PTR](#mb_data_ptr-parameter-s7-1200-s7-1500). - Instruction version >= V6.0: Error reading or writing data or access outside the address area of MB_DATA_PTR, RD_MB_DATA_PTR or WR_MB_DATA_PTR. |
| Remote | 02 | Error reading or writing data or access outside the address area of the server |  |
| 8384 | Local | - | - Invalid exception code received. - A different data value was received than was originally sent by the client (functions 5, 6 and 8). - Invalid status value received (function 11) |
| Remote | 03 | Error in data value for function 5 |  |
| 8385 | Local | - | - Diagnostics code not supported. - A different subfunction code was received than was originally sent by the client (function 8). |
| Remote | 03 | Diagnostics code not supported |  |
| 8386 | Local | - | Received function code does not match the one sent originally. |
| 8387 | Local | - | The protocol ID of the Modbus TCP frame received by the server is not "0". |
| 8388 | Local | - | The Modbus server sent a different data length than was requested. This error occurs only when using the Modbus functions 5, 6, 15 or 16. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |  |

##### Parameter STATUS (parameter error)

| STATUS* (W#16#) | Description |
| --- | --- |
| 80B6 | Invalid connection type, only TCP connections are supported. |
| 80BB | Invalid value at ActiveEstablished parameter (identifier for the type of connection establishment, see [CONNECT parameter](#connect-parameter-s7-1200-s7-1500)):   - Only passive connection establishment permitted for server (ActiveEstablished = FALSE). - Only active connection establishment permitted for client (ActiveEstablished = TRUE). |
| 8188 | The MB_MODE parameter has an invalid value. |
| 8189 | - Instruction version < V6.0: Invalid addressing of data at the MB_DATA_ADDR parameter. - Instruction version >= V6.0: Invalid addressing of data at the MB_DATA_ADDR, RD_MB_DATA_ADDR or WR_MB_DATA_ADDR parameter. |
| 818A | - Instruction version < V6.0: Invalid data length at the MB_DATA_LEN parameter. - Instruction version >= V6.0: Invalid data length at the MB_DATA_LEN, RD_MB_DATA_LEN or WR_MB_DATA_LEN parameter. |
| 818B | - Instruction version < V6.0: The MB_DATA_PTR parameter has an invalid pointer. You should also check the values of the [MB_DATA_ADDR](#mb_data_ptr-parameter-s7-1200-s7-1500) and MB_DATA_LEN parameters. - Instruction version >= V6.0: Invalid pointer at the MB_DATA_PTR, RD_MB_DATA_PTR or WR_MB_DATA_PTR parameter. Also check the values of the parameters MB_DATA_ADDR and MB_DATA_LEN or, for MB_MODE = 123, the values of the parameters RD_MB_DATA_ADDR / WR_MB_DATA_ADDR and RD_MB_DATA_LEN / WR_MB_DATA_LEN. |
| 818C | Timeout at parameter BLOCKED_PROC_TIMEOUT or RCV_TIMEOUT (see static tags of instruction). BLOCKED_PROC_TIMEOUT and RCV_TIMEOUT must be between 0.5 s and 55 s. |
| 818D | One or more parameters do not have their default value but are not used with the specified Modbus function.  Example: If MB_MODE has the value 123, MB_DATA_ADDR and MB_DATA_LEN must have the value 0 and MB_DATA_PTR must be empty. If MB_MODE has a value other than 123, all parameters that begin with "RD_" or "WR_" must have the value 0 or be empty. |
| 8200 | - A different Modbus request is currently being processed via the port. - Another instance of MB_CLIENT with the same connection parameters is processing an existing Modbus request. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

> **Note**
>
> **Error codes of internally used communications instructions**
>
> With the "MB_CLIENT" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND", "TRCV", "T_DIAG" and "TRESET") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_CLIENT" instruction. The error codes are displayed for the respective instruction under STATUS in the "Static" section.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

> **Note**
>
> **Communication error when sending or receiving data**
>
> If a communication error occurs when sending or receiving data (80C4 (Temporary communications error. The specified connection is temporarily down.), 80C5 (Remote partner closed connection actively.), 80A1 (The specified connection is disconnected or is not yet established.)), the existing connection is terminated.
>
> This also means that you can see all STATUS values that are returned when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.
>
> Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)

### MB_SERVER: Communicating via PROFINET as a Modbus TCP server (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description of MB_SERVER (S7-1200, S7-1500)](#description-of-mb_server-s7-1200-s7-1500)
- [MB_HOLD_REG parameter (S7-1200, S7-1500)](#mb_hold_reg-parameter-s7-1200-s7-1500)
- [CONNECT parameter (S7-1200, S7-1500)](#connect-parameter-s7-1200-s7-1500-1)
- [Parameter STATUS (S7-1200, S7-1500)](#parameter-status-s7-1200-s7-1500-1)
- [Access to data areas in DBs instead of direct access to MODBUS addresses as of version V5.0 (S7-1200, S7-1500)](#access-to-data-areas-in-dbs-instead-of-direct-access-to-modbus-addresses-as-of-version-v50-s7-1200-s7-1500)
- [Restriction of read access to process images as of version V5.0 (S7-1200, S7-1500)](#restriction-of-read-access-to-process-images-as-of-version-v50-s7-1200-s7-1500)
- [The statistical tags NDR_immediate and DR_immediate (S7-1200, S7-1500)](#the-statistical-tags-ndr_immediate-and-dr_immediate-s7-1200-s7-1500)

#### Description of MB_SERVER (S7-1200, S7-1500)

##### Description

The "MB_SERVER" instruction communicates as Modbus TCP server via a PROFINET connection. The instruction "MB_SERVER" processes connection requests of a Modbus TCP client, receives and processes Modbus requests and sends responses.

For the S7-1200 with firmware version V4.0 you can use the "MB_SERVER" instruction up to and including library version V3.1. With the S7-1200 as of firmware version V4.1 and the S7-1500, you can use the "MB_SERVER" instruction of all library versions.

The connection can take place via the local interface of the CPU or CM/CP.

To use the instruction, you do not require an additional hardware module.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security information**  Note that each client of the network is given read and write access to the process image inputs and outputs and to the data block or bit memory area defined by the Modbus holding register.  The option is available to restrict access to an IP address to prevent unauthorized read and write operations. Note, however, that the shared address can also be used for unauthorized access. |  |

##### Multiple server connections

You can create multiple Server connections. This allows a single CPU to accept connections from multiple Modbus TCP clients at the same time.

A Modbus TCP server can support several TCP connections and the maximum number of connections depends on the CPU being used.

The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections.

Modbus TCP connections can also be shared by "MB_CLIENT" and/or "MB_SERVER" instances.

In the case of Server connections, remember the following rules:

- Each "MB_SERVER" connection must use a unique instance DB.
- Each "MB_SERVER" connection must use a unique connection ID.

  The relevant individual connection ID must be used for each individual instance DB of the instruction. The connection ID and instance DB belong together in pairs and must be unique for each connection.
- For each connection, the "MB_SERVER" instruction must be called individually.

##### Parameters

The following table shows the parameters of the "MB_SERVER" instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| DISCONNECT | Input | BOOL | The "MB_SERVER" instruction is used to enter into a passive connection with a partner module. The server responds to a connection request from the IP address which is entered in the SDT "TCON_IP_v4" in the CONNECT parameter.   You can use this parameter to control when a connection request is accepted:  - 0: A passive connection is established when there is no communications connection. - 1: Initialization of the connection termination. If the input is set, no other operations are executed. The value 0003 is output at the STATUS parameter after successful connection termination. |
| [MB_HOLD_REG](#mb_hold_reg-parameter-s7-1200-s7-1500) | InOut | VARIANT | Pointer to the Modbus holding register of the "MB_SERVER" instruction  MB_HOLD_REG must always reference a memory area that is larger than two bytes.  The holding register contains the values that may be accessed by a Modbus client using the Modbus functions 3 (read), 6 (write), 16 (multiple write) and 23 (reading and writing in one job).  As the holding register, use either a global data block with optimized access or the memory area of the bit memories. |
| [CONNECT](#connect-parameter-s7-1200-s7-1500-1) | InOut | VARIANT | Pointer to the structure of the connection description  The following structures (SDTs) can be used:  - TCON_IP_v4: Includes all address parameters that are required for establishing a programmed connection. The default address is 0.0.0.0 (any IP address), but you can enter a specific IP address so that the server only responds to requests from this address. When using TCON_IP_v4, the connection is established when calling the "MB_SERVER" instruction. - TCON_Configured: Includes the address parameters of a configured connection. When using TCON_Configured, the connection is established by the CPU after download of the hardware configuration.   For instruction versions > V4.2 of MB_SERVER, the following connection descriptions for TCP are also possible:  - TCON_IP_V4_SEC (firmware version V4.3 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters according to TCON_IP_V4_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500) - TCON_QDN (firmware version V4.4 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters in accordance with TCON_QDN](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn-s7-1500) - TCON_QDN_SEC (firmware version V4.4 or higher of the S7-1200 CPUs or firmware version V2.5 or higher of the S7-1500 CPUs)   For a description, see [Connection parameters in accordance with TCON_QDN_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)   For more information on secure connections, see [Secure Open User Communication](Configuring%20devices%20and%20networks.md#secure-open-user-communication-s7-1500-s7-1500t) |
| NDR | Output | BOOL | "New Data Ready":  - 0: No new data - 1: New data written by the Modbus client written |
| DR | Output | BOOL | "Data Read":  - 0: No data read - 1: Data read by the Modbus client |
| ERROR | Output | BOOL | If an error occurs during the call of the "MB_SERVER" instruction, the output of the ERROR parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS parameter. |
| [STATUS](#parameter-status-s7-1200-s7-1500-1) | Output | WORD | Detailed status information of the instruction. |

> **Note**
>
> **Use of Modbus function 23 in the instruction "MB_SERVER"**
>
> The instruction "MB_SERVER" supports the use of Modbus function 23 with which you can write to a holding register and read from a holding register in one job; however, the instruction "MB_CLIENT" supports this function as of instruction version V6.0. Instruction versions < V6.0 return an error code.
>
> Also note that for a job with read access and write access, write access is executed before the read access.

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Static tags of MB_SERVER in instruction version V4.2

The following table describes the static tags of the instance data block of the "MB_SERVER" instruction used in the program. You can write the HR_Start_Offset tag. You can read the other tags to monitor the Modbus status.

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| HR_Start_Offset | WORD | 0 | Assign the start address of the Modbus holding register. |
| QB_Start | WORD | 0 | Start address of the permitted addressing range of the outputs that can be written (bytes 0 to 65535) |
| QB_Count | WORD | 0xFFFF | Number of output bytes that can be written by the Modbus master.  Example:  QB_Start=0 and QB_Count=10: Output bytes 0 to 9 can be written.  QB_Count=0: No output byte can be written. |
| Request_Count | WORD | 0 | Total number of requests received by the server. |
| Server_Message_Count | WORD | 0 | Total number of received alarms for the relevant server. |
| Xmt_Rcv_Count | WORD | 0 | Counter for detecting the number of transfers during which an error occurred. The counter is only incremented when an invalid Modbus request is received. |
| Exception_Count | WORD | 0 | Counters for detecting the number of errors specifically for Modbus which cause an error message to "MB_CLIENT". |
| Success_Count | WORD | 0 | Event counter for detecting the number of requests that were successfully executed by the server. |
| Connected | BOOL | FALSE | Indicates whether the connection to the assigned client has been established or not: TRUE = connected, FALSE = not connected. |

##### Mapping of Modbus addresses to the process image

The "MB_SERVER" instruction allows incoming Modbus functions (1, 2, 4, 5 and 15) direct read and write access to the process image inputs and outputs of the CPU (use of the data types BOOL and WORD).

For S7-1200-CPUs, the address space for the process image of the inputs and the process image of the outputs is 1 KB; it is 32 KB each for S7-1500-CPUs.

The following table shows the address space of the Modbus functions listed above.

| Modbus function |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Function code** | **Function** | **Data area** | **Address space** |  |  |
| 01 | Read: Bits | Output | 0 | to | 65.535 |
| 02 | Read: Bits | Input | 0 | to | 65.535 |
| 04 | Read: WORD | Input | 0 | to | 65.535 |
| 05 | Write: Bit | Output | 0 | to | 65.535 |
| 15 | Write: Bits | Output | 0 | to | 65.535 |

Incoming Modbus requests with the function codes 3, 6, 16 and 23 write or read the Modbus holding registers (you specify the holding register with the MB_HOLD_REG parameter).

##### Example: Addressing via static tag HR_Start_Offset

The addresses of the Modbus holding register start at 0 (from the perspective of the MB_CLIENT at 40.001). These addresses correspond to the address area of the CPU memory area for the holding register. You can also define the HR_Start_Offset tag so that the Modbus holding register has a start address other than 0.

Example: The holding register begins at MW100, and has a length of 100 WORD. An offset value in the HR_Start_Offset parameter means that the start address of the holding register is moved from 0 to 20. This causes an error whenever the holding register is addressed below the address 20 and above the address 119.

| HR_Start_Offset | Address | Minimum | Maximum |
| --- | --- | --- | --- |
| 0 | Modbus address (WORD) | 0 | 99 |
| CPU address | MW100 | MW298 |  |
| 20 | Modbus address (WORD) | 20 | 119 |
| CPU address | MW100 | MW298 |  |

##### Modbus functions

The following table lists all the Modbus functions that are supported by the "MB_SERVER" instruction.

| Function code | Description |
| --- | --- |
| 01 | Read output bits |
| 02 | Read input bits |
| 03 | Read a holding register |
| 04 | Read input words |
| 05 | Write an output bit |
| 06 | Write a holding register |
| 08 | Diagnostics function:  - Echo test (subfunction 0x0000): The "MB_SERVER" instruction receives a data word and returns this unchanged to the Modbus client. - Reset event counter (subfunction 0x000A): The "MB_SERVER" instruction resets the following event counters: "Success_Count", "Xmt_Rcv_Count", "Exception_Count", "Server_Message_Count" and "Request_Count". |
| 11 | Diagnostics function: Fetch event counter of the communication  The "MB_SERVER" instruction uses an internal event counter for communication to record the number of successfully executed read and write requests sent to the Modbus server.  The event counter is not incremented with the functions 8 or 11. The same holds true for requests that cause a communications error, for example, if a protocol error has occurred (e.g., the function code in the received Modbus request is not supported). |
| 15 | Write output bits |
| 16 | Write a holding register |
| 23 | Write a holding register and read holding register with a request |

##### Example

An example project for the Modbus TCP communication between two S7-1500 CPUs can be found in the Service and Support Portal under Entry ID [94766380](http://support.automation.siemens.com/WW/view/en/94766380).

Two Modbus functions are used in this example. For each Modbus function, a Modbus TCP connection is established using a Modbus block pair (MB_CLIENT and MB_SERVER).

![Example](images/102575198859_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### MB_HOLD_REG parameter (S7-1200, S7-1500)

##### Description

The MB_HOLD_REG parameter is a pointer to a data buffer for storing the data read from or written to the Modbus server. You can use a global data block or a bit memory (M) as memory area.

- The high limit for the number of addresses in the data block (D) is determined by the maximum size of a DB of your CPU.
- The high limit for the number of bit memories (M) is determined by the maximum bit memory area of your CPU.

The following table shows examples of mapping Modbus addresses to the holding register for the Modbus functions 3 (read multiple WORD), 6 (write one WORD), 16 (write multiple WORD) and 23 (write and read multiple words).

| Modbus addresses | MB_HOLD_REG parameter - examples |  |  |
| --- | --- | --- | --- |
| 0 | MW100 | DB10.DBW0 | "Recipe".ingredient[1] |
| 1 | MW102 | DB10.DBW2 | "Recipe".ingredient[2] |
| 2 | MW104 | DB10.DBW4 | "Recipe".ingredient[3] |
| 3 | MW106 | DB10.DBW6 | "Recipe".ingredient[4] |
| 4 | MW108 | DB10.DBW8 | "Recipe".ingredient[5] |

#### CONNECT parameter (S7-1200, S7-1500)

##### Connection descriptions at the CONNECT parameter up to and including instruction version V4.2 of MB_SERVER

Two different connection descriptions can be used for the "MB_SERVER" instruction:

- Programmed connections with the structure TCON_IP_v4

  The connection parameters are stored in the TCON_IP_v4 structure and the connection is set up with the call of the instruction "MB_SERVER".
- Configured connections with the structure TCON_Configured (only with S7-1500)

  The configured connection has already been established by the CPU. Use the structure TCON_Configured to specify which existing connection is to be used for the instruction.

Each instance of the instruction "MB_SERVER" requires a unique connection. Create a separate structure TCON_IP_v4 or TCON_Configured for each instance of the instruction to describe the connection.

##### Connection description for programmed connections

For programmed connections at the CONNECT parameter, use the following structure for connection description to TCON_IP_v4.

Make sure that only connections of the type TCP are specified in the TCON_IP_v4 structure.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | - | Hardware identifier of the local interface |
| 2 … 3 | ID | CONN_OUC | - | Reference to this connection (value range: 1 to 4095).  The parameter uniquely identifies a connection within the CPU. Each individual instance of the instruction "MB_SERVER" must use a unique ID. The ID must also not be used simultaneously by another instruction of a different type of communication.  Note: For S7-1500 CPUs with firmware version V2.9 or higher and S7-1200 CPUs with firmware version V4.5 or higher, ID may also have been supplied by the instruction "TCONSettings". In this case, ID is outside the value range 1 to 4095. |
| 4 | ConnectionType | BYTE | 11 | Connection type  Select 11 (decimal) for TCP. Other connection types are not permitted. If another connection type (e.g. UDP) is used, a corresponding error message is output at the STATUS parameter of the instruction. |
| 5 | ActiveEstablished | BOOL | FALSE | ID for the manner in which the connection is established  Select FALSE for passive connection establishment. |
| 6 … 9 | RemoteAddress | ARRAY [1..4] of BYTE | 0.0.0.0 | IP address of the connection partner, for example, for 192.168.0.1:   - addr[1] = 192 - addr[2] = 168 - addr[3] = 0 - addr[4] = 1   If the instruction "MB_SERVER" is to accept connection requests from any connection partner, use "0.0.0.0" as IP address. |
| 10 … 11 | RemotePort | UINT | 0 | Port number of the remote connection partner (value range: 1 to 49151).  If the instruction "MB_SERVER" is to accept connection requests from any port of the remote partner, use "0" as port number. |
| 12 … 13 | LocalPort | UINT | 502 | Port number of the local connection partner (value range: 1 to 49151).  The number of the IP port defines which IP port is monitored for connection requests of the Modbus client.   The default value is 502. |

> **Note**
>
> **Migration of the instruction "MB_SERVER" version 2.1**
>
> The parameters CONNECT_ID and IP_PORT are mapped in version 3.0 of the "MB_SERVER" instruction in the TCON_IP_v4 structure:
>
> - The parameter CONNECT_ID of the "MB_SERVER" V2.1 instruction corresponds to the ID parameter of TCON_IP_v4.
> - The parameter IP_PORT of the "MB_SERVER" V2.1 instruction corresponds to the LocalPort parameter of TCON_IP_v4.

##### Connection description for configured connections

For configured connections at the CONNECT parameter, use the following structure for connection description to TCON_Configured.

Make sure that only connections of the type TCP are specified in the TCON_Configured structure.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | - | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | - | Reference to this connection (value range: 1 to 4095).  ID must be unique CPU-wide. ID must also not be used simultaneously by another instruction of a different type of communication.  Enter the connection ID of the existing connection. |
| 4 | ConnectionType | BYTE | - | Connection type  Select 254 (decimal) for a configured connection. |

---

**See also**

[Connection parameters according to TCON_IP_V4_SEC (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500)
  
[Connection parameters in accordance with TCON_QDN (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn-s7-1500)
  
[Connection parameters in accordance with TCON_QDN_SEC (S7-1500)](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)
  
[Secure Open User Communication (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-open-user-communication-s7-1500-s7-1500t)

#### Parameter STATUS (S7-1200, S7-1500)

##### Parameter STATUS (general status information)

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 7000 | No call active and no connection established (REQ=0, DISCONNECT=1). |
| 7001 | First call. Connection establishment triggered. |
| 7002 | Intermediate call. Connection is being established. |
| 7003 | Connection is being terminated. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

##### Parameter STATUS (protocol error)

| STATUS* (W#16#) | Error code in the error message from "MB_SERVER" (B#16#) | Description |
| --- | --- | --- |
| 8380 | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | 01 | Function code is not supported. |
| 8382 | 03 | Error in data length:  - Invalid length specification in received Modbus frame. - The frame length entered in the header of the Modbus frame does not match the number of actually received bytes. - The number of bytes entered in the header of the Modbus frame does not match the number of actually received bytes (functions 15 and 16). |
| 8383 | 02 | Error in data address or access outside the address area of the holding register ([MB_HOLD_REG](#mb_hold_reg-parameter-s7-1200-s7-1500) parameter). |
| 8384 | 03 | Error in the data value (function 05) |
| 8385 | 03 | Diagnostic code is not supported (only with function 08). |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Parameter STATUS (parameter error)

| STATUS* (W#16#) | Description |
| --- | --- |
| 80BB | Invalid value at ActiveEstablished parameter (identifier for the type of connection establishment, see [CONNECT parameter](#connect-parameter-s7-1200-s7-1500-1)):   Only passive connection establishment permitted for server (active_established = FALSE). |
| 8187 | The MB_HOLD_REG parameter has an invalid pointer. Data area is too small. |
| 8389 | Invalid data area definition:  - Invalid data_type value - DB number invalid or does not exist:   - Invalid db value   - DB number does not exist   - DB number is already used by another data area   - DB with optimized access   - DB is not located in the work memory - Invalid length value - Overlapping of MODBUS address ranges that belong to the same MODBUS data type |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

> **Note**
>
> **Error codes of internally used communications instructions**
>
> With the "MB_SERVER" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND", "TRCV", "T_DIAG" and "T_RESET") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_SERVER" instruction. The error codes are displayed for the respective instruction under STATUS in the "Static" section.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

> **Note**
>
> **Communication error when sending or receiving data**
>
> If a communication error occurs when sending or receiving data (80C4 (Temporary communication error. The specified connection is temporarily terminated.), 80C5 (The remote partner has actively terminated the connection.), 80A1 (The specified connection is interrupted or has not been established yet.)), the existing connection is terminated.
>
> This also means that you can see all STATUS values that are returned when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.
>
> Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)

#### Access to data areas in DBs instead of direct access to MODBUS addresses as of version V5.0 (S7-1200, S7-1500)

##### Access to data areas in DBs instead of direct access to MODBUS addresses as of version V5.0

With version V5.0 of MB_SERVER instructions and firmware versions V2.5 (S7-1500 CPUs) and V4.2 (S7-1200 CPUs), you can access data areas in DBs instead of directly accessing process images and holding registers. In doing so, the attribute "Optimized block access" must be disabled for the DB and it must not be located solely in the load memory.

If a MODBUS request arrives and you have not defined a data area for the MODBUS data type of the corresponding function code, the request is treated as in the previous instruction versions, i.e. process images and holding registers are accessed directly.

If, on the other hand, you have defined a data area for the MODBUS data type of the function code, the instruction MB_SERVER reads from or writes to that data area. Whether it reads or writes depends on the job type.

One individual MODBUS request can only ever be read from or written to one data area. If, for example, you want to read holding registers that extend over multiple data areas, you therefore require multiple MODBUS requests.

##### Rules for defining data areas

You can define up to eight data areas in different DBs; each DB must only contain one data area. An individual MODBUS request can only ever read from precisely one data area or write to precisely one data area. Each data area corresponds to one MODBUS address area. The data areas are defined in the static tag Data_Area_Array of the instance DB; Data_Area_Array is a field consisting of eight elements.

If you want to use less than eight data areas, the required data areas must be located one behind the other without any gaps. The first blank entry in the data areas ends the data area search during processing. If, for example, you have defined the field elements 1, 2, 4 and 5, only field elements 1 and 2 will be recognized as field element 3 is empty.

The Data_Area_Array field consists of 8 elements: Data_Area_Array[1] to Data_Area_Array[8]

Each field element Data_Area_Array[x], 1 <= x <= 8, is a UDT of the type MB_DataArea and is structured as follows:

| Parameter | Data type | Meaning |
| --- | --- | --- |
| data_type | UInt | Identifier for the MODBUS data type that is mapped to this data area:  - 0: Identifier for an empty field element or an unused data area. In this case, the values of db, start and length are irrelevant. - 1: Process image output (used with function codes 1, 5 and 15) - 2: Process image input (used with function code 2) - 3: Holding register (used with function codes 3, 6 and 16) - 4: Input register (used with function code 4)   Note: If you have defined a data area for a MODBUS data type, the instruction MB_SERVER can no longer access this MODBUS data type directly. If the address of a MODBUS request for such a data type does not correspond to a defined data area, a value of W#16#8383 is returned in STATUS. |
| db | UInt | Number of the data block to which the MODBUS register or bits subsequently defined are mapped.  The DB number must be unique in the data areas. The same DB number must not be defined in multiple data areas.  The DB must have standard access and must not be located solely in the load memory.  Data areas also start with the byte address 0 of the DB.  Permitted values: 1 to 60999 |
| start | UInt | First MODBUS address that is mapped to the data block starting from address 0.0.  Permitted values: 0 to 65535 |
| length | UInt | Number of bits (for the values 1 and 2 of data_type) or number of registers (for the values 3 and 4 of data_type).  The MODBUS address areas of one and the same MODBUS data type must not overlap.  Permitted values: 1 to 65535 |

##### Examples of the definition of data areas

- First example: data_type = 3, db = 1, start = 10, length = 6

  The holding registers (data_type = 3) are mapped in data block 1 (db = 1). The Modbus address 10 (start = 10) is located at data word 0. The last valid Modbus address 15 (length = 6) is located at data word 5.
- Second example: data_type = 2, db = 15, start = 1700, length = 112

  The inputs (data_type = 2) are mapped in data block 15 (db = 15). The Modbus address 1700 (start = 1700) is located at data word 0. The last valid Modbus address 1811 (length = 112) is located at data word 111.

#### Restriction of read access to process images as of version V5.0 (S7-1200, S7-1500)

##### **Restriction of read access to process images**

With version V5.0 of MB_SERVER instructions, you can define one area in the process image input and one area in the process image output to which remote MODBUS devices can have read access. Read access by remote MODBUS devices to addresses outside these process image areas is then no longer possible.

> **Note**
>
> **Restriction of write access to process images**
>
> The option of restricting write access to the process image output of a specific area is possible as of instruction version V4.2.

##### **Definition of read areas in the process images**

Read areas in the process images are defined in the following static tags of the instance DB:

- QB_Read_Start: Address of the first byte in the process image output that can be read by a remote MODBUS device (applies to function code 1)
- QB_Read_Count: Number of bytes in the process image output that can be read by a remote MODBUS device (applies to function code 1)
- IB_Read_Start: Address of the first byte in the process image input that can be read by a remote MODBUS device (applies to function codes 2 and 4)
- IB_Read_Count: Number of bytes in the process image input that can be read by a remote MODBUS device (applies to function codes 2 and 4)

##### **Static tags in the instance DB for defining write and read areas in the process images**

The following table describes the static tags in the instance DB of instruction MB_SERVER that are listed above and which you use to define the read areas in the process images.

For the sake of completeness, the table also lists the static tags that you use to define the write areas in the process images as of version V4.2 (QB_Start and QB_Count).

| Tag | Data type | Start value |
| --- | --- | --- |
| QB_Start | UInt | 0 |
| QB_Count | UInt | 65535 |
| QB_Read_Start | UInt | 0 |
| QB_Read_Count | UInt | 65535 |
| IB_Read_Start | UInt | 0 |
| IB_Read_Count | UInt | 65535 |

#### The statistical tags NDR_immediate and DR_immediate (S7-1200, S7-1500)

##### NDR_immediate and DR_immediate

The statistical tags NDR_immediate and DR_immediate are contained in the instance data block of the instruction MB_SERVER as of instruction version V5.0.

| Tag | Data type | Start value | Meaning |
| --- | --- | --- | --- |
| NDR_immediate | BOOL | FALSE | Identical meaning as the parameter NDR (New Data Ready).  NDR_immediate is updated in the same call by MB_SERVER in which a MODBUS-TCP write request is processed. |
| DR_immediate | BOOL | FALSE | Identical meaning as the parameter DR (Data Read).  DR_immediate is updated in the same call by MB_SERVER in which a MODBUS-TCP read request is processed. |

### Differences between the versions <= V3.x and >= V4.0 of the Modbus TCP library (S7-1200, S7-1500)

#### Differences between the versions <= V3.x and >= V4.0 of the Modbus instructions

The following differences between versions exist with the MB_SERVER/MB_CLIENT MODBUS instructions:

- Address parameter

  - In versions <= 3.x, the address data for the Modbus TCP server is specified via the input parameters "IP_x".
  - Versions >= 4.0 use TCON_IP_V4 and TCON_Configured system data types at the CONNECT input parameter for this purpose.
- If an error occurs during execution, as of version 4.0 of the Modbus instructions, there are more STATUS alarms available which can be evaluated accordingly.

You can find detailed information in the instruction descriptions for [MB_CLIENT](#description-of-mb_client-s7-1200-s7-1500) and [MB_SERVER](#description-of-mb_server-s7-1200-s7-1500).

> **Note**
>
> **Changing the Modbus TCP library from a version <= V3.x to a version >= V4.0**
>
> When you replace the Modbus TCP library from a version <= V3.x to a version >= V4.0 you also need to replace the Open User Communication library. Afterwards check all the instructions relevant for your program.

## Redundant MODBUS (TCP) communication for library versions V5.0 or higher (S7-1200, S7-1500)

This section contains information on the following topics:

- [MB_RED_CLIENT: Redundant communication over PROFINET as MODBUS-TCP client (S7-1200, S7-1500)](#mb_red_client-redundant-communication-over-profinet-as-modbus-tcp-client-s7-1200-s7-1500)
- [MB_RED_SERVER: Communicating via PROFINET as a MODBUS TCP server (S7-1200, S7-1500)](#mb_red_server-communicating-via-profinet-as-a-modbus-tcp-server-s7-1200-s7-1500)

### MB_RED_CLIENT: Redundant communication over PROFINET as MODBUS-TCP client (S7-1200, S7-1500)

This section contains information on the following topics:

- [MB_RED_CLIENT description (S7-1200, S7-1500)](#mb_red_client-description-s7-1200-s7-1500)
- [Operation and redundancy (S7-1200, S7-1500)](#operation-and-redundancy-s7-1200-s7-1500)
- [Parameter assignment (S7-1200, S7-1500)](#parameter-assignment-s7-1200-s7-1500)
- [Licensing (S7-1200, S7-1500)](#licensing-s7-1200-s7-1500)
- [Input parameters MB_MODE, MB_DATA_ADDR, MB_DATA_LEN and MB_DATA_PTR (S7-1200, S7-1500)](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500)
- [Output parameters STATUS_x, RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR (S7-1200, S7-1500)](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500)

#### MB_RED_CLIENT description (S7-1200, S7-1500)

##### Description

You can use this instruction to establish a connection between a 1200/1500 CPU and a device that supports the Modbus/TCP protocol.

The instruction "MB_RED_CLIENT" communicates as a Modbus/TCP client over the PROFINET connection. You use the instruction "MB_RED_CLIENT" to establish a redundant connection between the client and the server, send Modbus requests, receive responses and control connection termination by the Modbus/TCP client.

The instruction "MB_RED_CLIENT" can be used in the following CPUs:

|  | "MB_RED_CLIENT" V1.0 | "MB_RED_CLIENT" V1.1 |
| --- | --- | --- |
| S7-1200 | FW V4.2 and higher | FW V4.2 and higher |
| S7-1500 | FW V2.5 and higher | FW V2.5 and higher |
| S7-1500R | -- | FW V2.6 and higher |
| S7-1500H | -- | FW V2.6 and higher |

To use the instruction, you do not require an additional hardware module.

##### Multiple client connections

The CPUs can process multiple Modbus/TCP client connections. The maximum number of connections depends on the CPU being used and can be found in the technical specifications of the CPU. The total number of connections of one CPU, including those of the Modbus/TCP clients and server must not exceed the maximum number of supported connections.

With individual client connections, remember the following rules:

- Each "MB_RED_CLIENT" connection must use a unique instance DB.
- For each "MB_RED_CLIENT" connection, a unique server IP address must be specified.
- Each "MB_RED_CLIENT" connection requires a unique connection ID. The connection IDs must be unique throughout the CPU.

For information concerning the redundancy setup, refer to: [Operation and redundancy](#operation-and-redundancy-s7-1200-s7-1500).

##### Parameters

The following table shows the parameters of the instruction "MB_RED_CLIENT":

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| [REG_KEY](#licensing-s7-1200-s7-1500) | Input | STRING[17] | Registration code for licensing  The "MB_RED_CLIENT" instruction must be licensed on each CPU individually. |
| USE_ALL_CONN | Input | BOOL | Specify the number of configured connections over which the frame is to be sent  - 0: Send frame over one connection, switch to next connection only in case of error - 1: Send frame over all configured connections |
| REQ | Input | BOOL | Modbus query to the Modbus/TCP server  The REQ parameter is level-controlled. This means that as long as the input is set (REQ = TRUE), the instruction sends communication requests. If the connection has not been established yet, it is established now and the Modbus frame is sent immediately thereafter.  Changes to the input parameters will not become effective until the server has responded or an error message has been output.   If the parameter REQ is set again during an ongoing Modbus request, no additional transmission takes place afterwards. |
| DISCONNECT | Input | BOOL | With this parameter, you control the establishment and termination of the connection to the Modbus server:  - 0: Establish communication connection to the connection partner configured at the CONNECT parameter (see CONNECT parameter). - 1: Disconnect the communication connection. No other function is executed during connection termination. The value 0003 is output at the STATUS_x parameter after successful connection termination. |
| [MB_MODE](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500) | Input | USINT | Selects the mode of the Modbus request (read, write or diagnostics) or direct selection of a Modbus function |
| [MB_DATA_ADDR](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500) | Input | UDINT | Modbus address depending on MB_MODE |
| MB_DATA_LEN | Input | UINT | Data length: Number of bits or registers for the data access. |
| [MB_DATA_PTR](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500) | InOut | VARIANT | Pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server. |
| [LICENSED](#licensing-s7-1200-s7-1500) | Output | BOOL | - 0: Instruction is not licensed - 1: Instruction is licensed |
| [IDENT_CODE](#licensing-s7-1200-s7-1500) | Output | STRING[18] | Identification for licensing. Use this string to request the registration code REG_KEY. |
| DONE | Output | BOOL | The bit at output parameter DONE is set to "1" as soon as the activated Modbus job is completed without errors on at least one connection. |
| BUSY | Output | BOOL | - 0: No Modbus request in progress - 1: Modbus request being processed  The output parameter BUSY is not set during connection establishment and termination. |
| ERROR | Output | BOOL | - 0: No error - 1: The activated Modbus job could not be transmitted successfully on any of the configured connections. The cause of error is indicated by the STATUS_x parameter. |
| [STATUS_0A](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 0A. |
| [STATUS_1A](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 1A. |
| [STATUS_0B](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 0B. |
| [STATUS_1B](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 1B. |
| [RED_ERR_S7](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | BOOL | - 0: No redundancy error in SIMATIC - 1: Redundancy error in SIMATIC |
| [RED_ERR_DEV](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | BOOL | - 0: No redundancy error on side of link partner - 1: Redundancy error on side of link partner |
| [TOT_COM_ERR](#output-parameters-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | BOOL | - 0: At least 1 configured connection is established - 1: Complete loss of communication, all configured connections are terminated |

> **Note**
>
> **Consistent input data during an "MB_RED_CLIENT" call**
>
> When a Modbus client instruction is called, the values of the input parameters are stored internally. They must not be changed while the frame is being processed.

#### Operation and redundancy (S7-1200, S7-1500)

##### Description

The communication nodes can be designed as standalone or redundant. If one of the partners is designed as standalone, we refer to it as single-sided redundancy. If both partners are designed redundantly, we refer to it as double-sided redundancy.

**Port numbers for client and server**

The Modbus client uses a port number starting at 2000. The Modbus server is usually addressed over the port number 502.

##### Single-sided redundancy

**Description**

One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.

**Configuration**

If the S7 is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner and one connection from the S7 connection point 1 to junction A of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**

The figure illustrates the connection designations.

![Modbus/TCP: Single-sided redundancy S7](images/112743929483_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Single-sided redundancy S7

If the S7 is designed as standalone and the link partner is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner and one connection from the S7 connection point 0 to junction B of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **0** to the partner/node **B** => connection **0B**

The figure illustrates the connection designations.

![Modbus/TCP: Single-sided redundancy partner](images/104186959371_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Single-sided redundancy partner

##### Double-sided redundancy

**Description**

One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.

**Configuration**

In the case of double-sided redundancy, two connections are created from connection point 0 and two connections from connection point 1 of the S7 to the junctions A and B of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**
- Connection from the S7 connection point **0** to the partner/node **B** => connection **0B**
- Connection from the S7 connection point **1** to the partner/node **B** => connection **1B**

The figure illustrates the connection designations.

![Modbus/TCP: Double-sided redundancy](images/112743940107_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Double-sided redundancy

##### Frame processing

**General**

The frames can be sent via one or via all configured connections.

**Send frames via one connection**

The MODBUS frame is sent via one - the currently active - connection with the setting USE_ALL_CONN = FALSE. In case of a timeout (no response from the server) or a connection fault an attempt is made to send the frame via the other (maximum 4) configured connections. The sequence is then 0A, 1A, 0B and 1B. If a frame was transmitted successfully via a connection, this connection is marked as "active" and the further frame traffic is executed via this connection. In the case of a connection fault of the active connection it is again attempted to send the frame via all configured connections. If all send attempts fail, ERROR and STATUS_x are set accordingly.

If a response frame was received, a plausibility check is executed. If this check is successful, the required actions are performed and the job is executed without errors; the output DONE is set. If errors are detected during the check, the job is ended without errors, the bit ERROR is set and an error number is displayed at STATUS_x. In this case no new attempt is made to send the frame on the next configured connection. A switchover to the other configured connections only takes place if a connection fault was detected or no response was received.

**Sending frames via all connections**

The MODBUS frame is sent via all configured, established connections with the setting USE_ALL_CONN = TRUE. A validity check is performed after the response frame has been received on one of the connections. If this check is successful, the required actions are performed. If a valid response frame was received on at least one connection, the output DONE is set.

##### Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR

**Description**

The redundancy bits RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR are set based on the states of the status outputs.

**Display of the interrupt bits for redundancy setup on both sides**

![Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR](images/104278212619_DV_resource.Stream@PNG-en-US.png)

**Display of the interrupt bits for redundancy setup on one side**

![Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR](images/104296715531_DV_resource.Stream@PNG-en-US.png)

#### Parameter assignment (S7-1200, S7-1500)

##### Description

The instruction "MB_RED_CLIENT" **V1.0** and **V1.1** can be used for S7-1200 and for S7-1500.

**S7-1200**

The connections are implemented over the local interface of the CPU or CM/CP. The connections are configured and established using the structure TCON_IP_V4.

**S7-1500**

The connections are implemented over the local interface of the CPU or CM/CP. Configured connections over the structure TCON_IP_V4 as well as configured connections over the structure TCON_Configured are possible.

The instruction "MB_RED_CLIENT" **V1.1** can be used for S7-1500R and for S7-1500H.

**S7-1500R and S7-1500H**

The connections are implemented over the local interface of the CPU or CM/CP. The connections are configured and established using the structure TCON_IP_V4.

##### Configuration of "MB_RED_CLIENT"

The following settings are made with the help of the configuration dialog of the instruction "MB_RED_CLIENT":

- Connection parameters for the connections 0A, 1A, 0B and 1B (Redundancy configuration see [Operation and Redundancy](#operation-and-redundancy-s7-1200-s7-1500))
- Internal parameter (optional)

The configuration dialog can be opened with the instruction or via the technology objects.

> **Note**
>
> **Using the configuration dialog**
>
> The configuration dialog can only be used when called with single-instance DBs. If there is a multi-instance, the parameters have to be set manually.

**Connection parameters**

![Modbus/TCP: configured client connection](images/113201711755_DV_resource.Stream@PNG-en-US.PNG)

Modbus/TCP: configured client connection

![Modbus/TCP: configured client connection](images/113201745803_DV_resource.Stream@PNG-en-US.PNG)

Modbus/TCP: configured client connection

| Tag | Start value | Description |
| --- | --- | --- |
| **Configured connections** |  |  |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used  These connection IDs must be unique throughout the CPU. |
| Local port | 0 | Local port number of the client. By default no port number is entered for the client. |
| Remote IP | 0.0.0.0 | Remote IP address of the server |
| Remote port | 502 | Remote port number of the server  The default port for Modbus/TCP server is 502. |
| **Configured connections** |  |  |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used  These connections are configured in the network view. |

**Internal parameter (optional)**

![Configuration of "MB_RED_CLIENT"](images/113201735179_DV_resource.Stream@PNG-en-US.png)

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| Blocked Proc Time | REAL | 3.0 | Wait time in seconds before the static tag ACTIVE is reset if there is a blocked Modbus instance. This can, for example, occur if a client request is output and the execution of the client function aborts before the request was fully executed. The wait time must be between 0.5 s and 55 s. |
| Receive timeout | REAL | 2.0 | Time interval in seconds in which the "MB_RED_CLIENT" instruction waits for a response from the server. It must be between 0.5 s and 55 s. |
| MB_Unit_ID | BYTE | 255 | Modbus device detection:  A Modbus TCP server is addressed using its IP address. For this reason, the MB_UNIT_ID parameter is not used in the case of Modbus TCP addressing.  The MB_UNIT_ID parameter corresponds to the field of the slave address in the Modbus RTU protocol. If a Modbus/TCP server is used as a gateway for a Modbus RTU protocol, the slave device in the serial network can be identified using MB_UNIT_ID. The MB_UNIT_ID parameter would in this case forward the request to the correct Modbus RTU slave address.  Please note that some Modbus/TCP devices may require the MB_UNIT_ID parameter for the initialization within a limited value range. |
| Retries | WORD | 3 | Number of send attempts made by the "MB_RED_CLIENT" instruction before it returns the error W#16#80C8. |

> **Note**
>
> **Tag MB_Transaction_ID**
>
> If the transaction ID in the answer of the Modbus TCP server does not match the transaction ID of the job from "MB_RED_CLIENT", the "MB_RED_CLIENT" instruction waits for the time period RCV_TIMEOUT * RETRIES for the answer of the Modbus TCP server with the correct transaction ID; once this time has expired, it returns the error W#16#80C8.

#### Licensing (S7-1200, S7-1500)

The "MB_RED_CLIENT" instruction is subject to a fee and must be licensed on each CPU individually. Licensing takes place in two steps:

- Reading out the IDENT_CODE and
- Entering the registration key REG_KEY.

> **Note**
>
> **S7-1500R and S7-1500H**
>
> For an S7-R/H station only CPU1 is licensed. A replacement of CPU1 after licensing is therefore no longer possible.

> **Note**
>
> **Transfer of the license / PLCSIM**
>
> It is not possible to transfer the license from one CPU to another.
>
> The instruction may not be licensed with PLCSIM.

##### Procedure

**Reading out the IDENT_CODE**

Proceed as follows to read out the IDENT_CODE:

1. Assign parameters to the "MB_RED_CLIENT" instruction in line with your requirements in a cyclic OB. Download the program to the CPU and set it to RUN.
2. Open the instance DB of the Modbus instruction and click the "Monitor all" button.
3. An 18-digit character string is displayed at the IDENT_CODE output.

   ![Procedure](images/113202649611_DV_resource.Stream@PNG-en-US.png)
4. Copy this string using copy/paste from the data block and paste it in the form that was sent to you by email after you ordered the product or is included on the CD.
5. Send the form to [Customer support](https://support.industry.siemens.com/my/ww/en/requests/#createRequest) using a service request. You will then receive the registration key for your CPU.

**Entering the registration key REG_KEY**

The registration key REG_KEY must be specified at each "MB_RED_CLIENT" instruction. You should save the REG_KEY in a global data block from which all "MB_RED_CLIENT" instructions receive the necessary registration key.

Proceed as follows to enter the registration key REG_KEY:

- Insert a new global data block with a unique symbolic name, for example "License_DB", using "Add new block…".
- Create a REG_KEY parameter in this block with the data type STRING[17].

  ![REG_KEY in DB](images/66691684107_DV_resource.Stream@PNG-en-US.png)

  REG_KEY in DB
- Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
- In the cyclic OB, enter the name of the license DB and the name of the string, e.g. License_DB.REG_KEY, at the parameter REG_KEY of the "MB_RED_CLIENT" instruction.
- Download the modified blocks to the CPU. The registration key can be entered during runtime; a change from STOP -> RUN is not necessary.

The Modbus/TCP communication using the "MB_RED_CLIENT" instruction is now licensed for this CPU, the output bit LICENSED is TRUE.

**Missing or incorrect licensing**

If you enter an incorrect registration key or none at all, the ERROR-LED of the CPU flashes. In addition for S7-1200 and S7-1500, a cyclic entry is made in the diagnostics buffer regarding the missing license. Only the area length error is displayed for R and H stations.

![Procedure](images/113202685835_DV_resource.Stream@PNG-en-US.png)

In the case of a missing or incorrect registration key, the Modbus/TCP communication is processed but W#16#0A90 "No valid license available" is always displayed at the STATUS_x output. The output bit LICENSED is FALSE.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **If OB121 is missing in the controller in the S7-1500 (R/H), the CPU is set to STOP.** |  |

#### Input parameters MB_MODE, MB_DATA_ADDR, MB_DATA_LEN and MB_DATA_PTR (S7-1200, S7-1500)

##### Description

The combination of the parameters MB_MODE, MB_DATA_ADDR and MB_DATA_LEN defines the function code used in the current Modbus message:

- **MB_MODE** contains the information on whether to read or to write.

  **Read**: MB_MODE = 0, 101, 102, 103 and 104  
  **Write**: MB_MODE = 1, 2, 105, 106, 115 and 116 (Note: With MB_MODE = 2, there is not distinction between Modbus functions 15 and 05 or between Modbus functions 16 and 06.)
- **MB_DATA_ADDR** contains the information on what is to be read or written, as well as address information from which the "MB_RED_CLIENT" instruction calculates the remote address.
- **MB_DATA_LEN** contains the number of values to be read/written.

The following table shows the relationship between the input parameters MB_MODE, MB_DATA_ADDR, MB_DATA_LEN of the "MB_RED_CLIENT" instruction and the Modbus function.

| MB_MODE | MB_DATA_ADDR | MB_DATA_LEN | Modbus function | Function and data type |
| --- | --- | --- | --- | --- |
| 0 | 1 to 9,999 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 9,998 |
| 0 | 10,001 to 19,999 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 9,998 |
| 0 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 125 | 03 | - Read 1 to 125 holding registers on the remote address 0 to 9,998 - Read 1 to 125 holding registers on the remote address 0 to 65,534 |
| 0 | 30,001 to 39,999 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 9,998 |
| 1 | 1 to 9,999 | 1 | 05 | Write 1 output bit on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 | 06 | - Write 1 holding register on the remote address 0 to 9,998 - Write 1 holding register on the remote address 0 to 65,534 |
| 1 | 1 to 9,999 | 2 to 1,968 | 15 | Write 2 to 1,968 output bits on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 2 to 123 | 16 | - Write 2 to 123 holding registers on the remote address 0 to 9,998 - Write 2 to 123 holding registers on the remote address 0 to 65,534 |
| 2 | 1 to 9,999 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 9,998 |
| 2 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 123 | 16 | - Write 1 to 123 holding registers on the remote address 0 to 9,998 - Write 1 to 123 holding registers on the remote address 0 to 65,534 |
| 11 | The MB_DATA_ADDR and MB_DATA_LEN parameters are not evaluated when this function is executed. |  | 11 | Read status word and event counter of the server:  - The status word reflects the processing status (0 - not processing, 0xFFFF - processing). - The event counter is incremented when the Modbus request was executed successfully. If an error occurred during execution of a Modbus function, a message is sent by the server but the event counter is not incremented. |
| 80 | - | 1 | 08 | Check the server status with the diagnostic code 0x0000 (return loop test - the server sends the request back):  - 1 WORD per call |
| 81 | - | 1 | 08 | Reset the event counter of the server with the diagnostic code 0x000A:  - 1 WORD per call |
| 101 | 0 to 65,535 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 65,535 |
| 102 | 0 to 65,535 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 65,535 |
| 103 | 0 to 65,535 | 1 to 125 | 03 | Read 1 to 125 holding registers on the remote address 0 to 65,535 |
| 104 | 0 to 65,535 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 65,535 |
| 105 | 0 to 65,535 | 1 | 05 | Write 1 output bit on the remote address 0 to 65,535 |
| 106 | 0 to 65,535 | 1 | 06 | Write 1 holding register on the remote address 0 to 65,535 |
| 115 | 0 to 65,535 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 65,535 |
| 116 | 0 to 65,535 | 1 to 123 | 16 | Write 1 to 123 holding registers on the remote address 0 to 65,535 |
| 3 to 10, 12 to 79, 82 to 100, 107 to 114, 117 to 255 |  |  |  | Reserved |

##### Example

| Tag | Meaning |
| --- | --- |
| MB_MODE = 1 MB_DATA_ADDR = 1 MB_DATA_LEN = 1 | 1 output bit with function code 5 is written starting from the remote address 0. |
| MB_MODE = 1 MB_DATA_ADDR = 1 MB_DATA_LEN = 2 | 2 output bits with function code 15 are written starting from the remote address 0. |
| MB_MODE = 104 MB_DATA_ADDR = 17834 MB_DATA_LEN = 125 | 125 input words with function code 4 is read starting from the remote address 17.834. |

##### MB_DATA_PTR

The MB_DATA_PTR parameter is a pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server. As the data buffer, you can use a global data block or a memory area (M).

For a buffer in the memory area (M), use a pointer in the ANY format as follows: "P#bit address" "data type" "length" (example: P#M1000.0 WORD 500).

Depending on the memory area in which the data buffer is located, MB_DATA_PTR can reference different data structures:

- When you use a global DB with optimized access, MB_DATA_PTR can reference a tag with elementary data type or an array of elementary data types. The following data types are supported:

  | Data type | Length in bits |
  | --- | --- |
  | Bool | 1 |
  | Byte, SInt, USInt, Char | 8 |
  | Word, Int, WChar, UInt | 16 |
  | DWord, DInt, UDInt, Real | 32 |

  You can hereby use all supported data types for all Modbus functions. For example, MB_RED_CLIENT can also write a received bit in a tag of the byte type to a specified address without changing other bits in this byte. Therefore, it is not necessary to have an array of bits in order to execute bit-oriented functions.
- If you use a bit memory address area or a global DB with standard access as memory area, there is no longer any restriction to the elementary data types for MB_DATA_PTR; MB_DATA_PTR can then also reference complex data structures such as PLC data types (UDTs) and system data types (SDTs).

> **Note**
>
> **Using a bit memory address area as data buffer**
>
> If you use a bit memory address area as data buffer for MB_DATA_PTR, you need to observe this variable. With S7-1500(R/H) CPUs it is 16 KB, with S7-1200 CPUs it is 8 KB.

#### Output parameters STATUS_x, RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR (S7-1200, S7-1500)

##### Parameter STATUS_x (general status information)

The error messages are displayed at the status outputs of the instruction "MB_RED_CLIENT".

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 0A90 | The instruction "MB_RED_CLIENT" is not licensed. Additional information is available here: [Licensing](#licensing-s7-1200-s7-1500). |
| 0AFF | The connection is not configured and is not used. The connection 0A must be configured. |
| 7000 | No job active and no connection established (REQ=0, DISCONNECT=1). |
| 7001 | Connection establishment triggered. |
| 7002 | Intermediate call. Connection is being established. |
| 7003 | Connection is being terminated. |
| 7004 | Connection established and monitored. No job processing active. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Parameter STATUS_x (protocol error)

| STATUS* (W#16#) | Description |
| --- | --- |
| 80C8 | No response of the server in the defined period. Check the connection to the Modbus server. This error is only reported on completion of the configured repeated attempts.   If the "MB_RED_CLIENT" instruction does not receive an answer with the originally transferred transaction ID (see static tag MB_TRANSACTION_ID) within the defined period, this error code is output. |
| 8380 | Received Modbus frame has incorrect format or too few bytes were received. |
| 8382 | - The length of the Modbus frame in the frame header does not match the number of received bytes. - The number of bytes does not match the number of actually transmitted bytes (only functions 1-4). - The start address in the received frame does not match the saved start address (functions 5, 6, 15, 16). - The number of words does not match the number of actually transmitted words (functions 15 and 16). |
| 8383 | Error reading or writing data or access outside the address area of [MB_DATA_PTR](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500). |
| 8384 | - Invalid exception code received. - A different data value was received than was originally sent by the client (functions 5, 6 and 8). - Invalid status value received (function 11) |
| 8385 | - Diagnostics code not supported. - A different subfunction code was received than was originally sent by the client (function 8). |
| 8386 | Received function code does not match the one sent originally. |
| 8387 | The protocol ID of the Modbus TCP frame received by the server is not "0". |
| 8388 | The Modbus server sent a different data length than was processed. This error occurs only when using the Modbus functions 5, 6, 15 or 16. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Parameter STATUS_x (parameter error)

| STATUS* (W#16#) | Description |  |
| --- | --- | --- |
| 80B6 | Invalid connection type, only TCP connections are supported. |  |
| 80BB | The ActiveEstablished parameter has an invalid value. Only active connection establishment permitted for client (ActiveEstablished = TRUE). |  |
| 8188 | The MB_MODE parameter has an invalid value. |  |
| 8189 | Invalid addressing of data at the MB_DATA_ADDR parameter. |  |
| 818A | Invalid data length at the MB_DATA_LEN parameter. |  |
| 818B | The MB_DATA_PTR parameter has an invalid pointer. You should also check the values of the [MB_DATA_ADDR](#input-parameters-mb_mode-mb_data_addr-mb_data_len-and-mb_data_ptr-s7-1200-s7-1500) and MB_DATA_LEN parameters. |  |
| 818C | Timeout at parameter BLOCKED_PROC_TIMEOUT or RCV_TIMEOUT (see static tags of instruction). BLOCKED_PROC_TIMEOUT and RCV_TIMEOUT must be between 0.5 s and 55 s. |  |
| 8200 | - A different Modbus request is currently being processed via the port. - Another instance of MB_RED_CLIENT with the same connection parameters is processing an existing Modbus request. |  |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

> **Note**
>
> **Error codes of internally used communication instructions**
>
> With the "MB_RED_CLIENT" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND", "TRCV", "T_DIAG" and "TRESET") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_RED_CLIENT" instruction. The error codes are displayed for the respective instruction under STATUS in the "Static" section.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

> **Note**
>
> **Communication error when sending or receiving data**
>
> If a communication error occurs when sending or receiving data (80C4 (Temporary communications error. The specified connection is temporarily down.), 80C5 (Remote partner closed connection actively.), 80A1 (The specified connection is disconnected or is not yet established.)), the existing connection is terminated.
>
> This also means that you can see all STATUS values that are returned when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.
>
> Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

### MB_RED_SERVER: Communicating via PROFINET as a MODBUS TCP server (S7-1200, S7-1500)

This section contains information on the following topics:

- [MB_RED_SERVER description (S7-1200, S7-1500)](#mb_red_server-description-s7-1200-s7-1500)
- [Operation and redundancy (S7-1200, S7-1500)](#operation-and-redundancy-s7-1200-s7-1500-1)
- [Parameter assignment (S7-1200, S7-1500)](#parameter-assignment-s7-1200-s7-1500-1)
- [Licensing (S7-1200, S7-1500)](#licensing-s7-1200-s7-1500-1)
- [MB_HOLD_REG input parameter (S7-1200, S7-1500)](#mb_hold_reg-input-parameter-s7-1200-s7-1500)
- [Output parameters ERROR_x, STATUS_x, RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR (S7-1200, S7-1500)](#output-parameters-error_x-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500)

#### MB_RED_SERVER description (S7-1200, S7-1500)

##### Description

You can use this instruction to establish a connection between a 1200/1500 CPU and a device that supports the Modbus/TCP protocol.

The instruction "MB_RED_SERVER" communicates as a Modbus/TCP server over the PROFINET connection. The instruction ""MB_RED_SERVER"" processes connection requests of a Modbus/TCP client, receives and processes Modbus requests and sends responses.

The instruction "MB_RED_SERVER" can be used in the following CPUs:

|  | "MB_RED_SERVER" V1.0 | "MB_RED_SERVER" V1.1 |
| --- | --- | --- |
| S7-1200 | FW V4.2 and higher | FW V4.2 and higher |
| S7-1500 | FW V2.5 and higher | FW V2.5 and higher |
| S7-1500R | -- | FW V2.6 and higher |
| S7-1500H | -- | FW V2.6 and higher |

To use the instruction, you do not require an additional hardware module.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security information**  Note that each client of the network is given read and write access to the process image inputs and outputs and to the data block or bit memory area defined by the Modbus holding register. The option is available to restrict access to an IP address to prevent unauthorized read and write operations. Note, however, that the shared address can also be used for unauthorized access. |  |

##### Multiple server connections

The CPUs can:

- processing multiple server connections and
- accepting multiple connections from different clients simultaneously at one server port.

The maximum number of connections depends on the CPU being used and can be found in the technical specifications of the CPU. The total number of connections of one CPU, including those of the Modbus/TCP clients and server must not exceed the maximum number of supported connections.

In the case of server connections, remember the following rules:

- Each ""MB_RED_SERVER"" connection must use a unique instance DB.
- One unique connection/connection ID is required for each and every client that wants to connect to the server port.
- The connection IDs must be unique throughout the CPU.

For information concerning the redundancy setup, refer to: [Operation and redundancy](#operation-and-redundancy-s7-1200-s7-1500-1).

##### Parameters

The following table shows the parameters of the instruction "MB_RED_SERVER":

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| [REG_KEY](#licensing-s7-1200-s7-1500-1) | Input | STRING[17] | Registration code for licensing  The "MB_RED_SERVER" instruction must be licensed on each CPU individually. |
| DISCONNECT | Input | BOOL | The "MB_RED_SERVER" instruction is used to enter into a passive connection with a partner module. The server responds to a connection request from the IP addresses which are given in the connection descriptions as specified or unspecified.   You can use this parameter to control when a connection request is accepted:  - 0: A passive connection is established when there is no communications connection. - 1: Initialization of the connection termination. If the input is set, no additional client requests are being processed and termination of the connection is initiated. The value 0003 is output at the STATUS_x parameter after successful connection termination. |
| [MB_HOLD_REG](#mb_hold_reg-input-parameter-s7-1200-s7-1500) | InOut | VARIANT | Pointer to the Modbus holding register of the "MB_RED_SERVER" instruction  MB_HOLD_REG must always reference a memory area that is larger than two bytes.  The holding register contains the values that may be accessed by a Modbus client using the Modbus functions 3 (read), 6 (write), 16 (multiple write) and 23 (reading and writing in one job). |
| [LICENSED](#licensing-s7-1200-s7-1500-1) | Output | BOOL | - 0: Instruction is not licensed - 1: Instruction is licensed |
| [IDENT_CODE](#licensing-s7-1200-s7-1500-1) | Output | STRING[18] | Identification for licensing. Use this string to request the registration code REG_KEY. |
| DR_NDR_0A | Output | BOOL | "Data Read" or "New Data Ready" to connection 0A:  - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR_0A | Output | BOOL | If an error occurs during a call of the "MB_RED_SERVER" instruction to connection 0A, the output of the ERROR_0A parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS_0A parameter. |
| [STATUS_0A](#output-parameters-error_x-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 0A. |
| DR_NDR_1A | Output | BOOL | "Data Read" or "New Data Ready" to connection 1A:  - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR_1A | Output | BOOL | If an error occurs during a call of the "MB_RED_SERVER" instruction to connection 1A, the output of the ERROR_1A parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS_1A parameter. |
| [STATUS_1A](#output-parameters-error_x-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 1A. |
| DR_NDR_0B | Output | BOOL | "Data Read" or "New Data Ready" to connection 0B:  - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR_0B | Output | BOOL | If an error occurs during a call of the "MB_RED_SERVER" instruction to connection 0B, the output of the ERROR_0B parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS_0B parameter. |
| [STATUS_0B](#output-parameters-error_x-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 0B. |
| DR_NDR_1B | Output | BOOL | "Data Read" or "New Data Ready" to connection 1B:  - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR_1B | Output | BOOL | If an error occurs during a call of the "MB_RED_SERVER" instruction to connection 1B, the output of the ERROR_1B parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS_1B parameter. |
| [STATUS_1B](#output-parameters-error_x-status_x-red_err_s7-red_err_dev-and-tot_com_err-s7-1200-s7-1500) | Output | WORD | Detailed status information of the instruction on connection 1B. |
| [RED_ERR_S7](#operation-and-redundancy-s7-1200-s7-1500-1) | Output | BOOL | - 0: No redundancy error in SIMATIC - 1: Redundancy error in SIMATIC |
| [RED_ERR_DEV](#operation-and-redundancy-s7-1200-s7-1500-1) | Output | BOOL | - 0: No redundancy error on side of link partner - 1: Redundancy error on side of link partner |
| [TOT_COM_ERR](#operation-and-redundancy-s7-1200-s7-1500-1) | Output | BOOL | - 0: At least one configured connection is established - 1: Complete loss of communication, all configured connections are terminated |

##### Mapping of Modbus addresses to the process image

The "MB_RED_SERVER" instruction allows incoming Modbus functions (1, 2, 4, 5 and 15) direct read and write access to the process image inputs and outputs of the CPU (use of the data types BOOL and WORD).

For S7-1200-CPUs, the address space for the process image of the inputs and the process image of the outputs is 1 KB; it is 32 KB each for S7-1500-CPUs.

The following table shows the address space of the Modbus functions listed above.

| Modbus function |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Function code** | **Function** | **Data area** | **Address space** |  |  |
| 01 | Read: Bits | Output | 0 | to | 65.535 |
| 02 | Read: Bits | Input | 0 | to | 65.535 |
| 04 | Read: WORD | Input | 0 | to | 65.535 |
| 05 | Write: Bit | Output | 0 | to | 65.535 |
| 15 | Write: Bits | Output | 0 | to | 65.535 |

Incoming Modbus requests with the function codes 3, 6, 16 and 23 write or read the Modbus holding registers (you specify the holding register with the MB_HOLD_REG parameter or via Data_Area_Array).

##### Modbus functions

The following table lists all the Modbus functions that are supported by the "MB_RED_SERVER" instruction.

| Function code | Description |
| --- | --- |
| 01 | Read output bits |
| 02 | Read input bits |
| 03 | Read a holding register |
| 04 | Read input words |
| 05 | Write an output bit |
| 06 | Write a holding register |
| 08 | Diagnostics function:  - Echo test (subfunction 0x0000): The "MB_RED_SERVER" instruction receives a data word and returns this unchanged to the Modbus client. - Reset event counter (subfunction 0x000A): The ""MB_RED_SERVER"" instruction resets the following event counters: "Success_Count", "Xmt_Rcv_Count", "Exception_Count", "Server_Message_Count" and "Request_Count". |
| 11 | Diagnostics function: Fetch event counter of the communication  The ""MB_RED_SERVER"" instruction uses an internal event counter for communication to record the number of successfully executed read and write requests sent to the Modbus server.  The event counter is not incremented with the functions 8 or 11. The same holds true for requests that cause a communications error, for example, if a protocol error has occurred (e.g., the function code in the received Modbus request is not supported). |
| 15 | Write output bits |
| 16 | Write a holding register |
| 23 | Write a holding register and read a holding register with a request |

#### Operation and redundancy (S7-1200, S7-1500)

##### Description

The communication nodes can be designed as standalone or redundant. If one of the partners is designed as standalone, we refer to it as single-sided redundancy. If both partners are designed redundantly, we refer to it as double-sided redundancy.

**Port numbers for client and server**

The Modbus client uses a port number starting at 2000. The Modbus server is usually addressed over the port number 502. Depending on the CPU, it is possible to configure port 502 for multiple connections (Multiport). If the local port 502 was configured for two or more connections, the requesting clients are randomly distributed to the existing server connections in the case of unspecified connections. The first client that wants to connect to the "MB_RED_SERVER" instruction is not automatically assigned the connection 0A. Once the assignment of the client requests to the server connections has taken place, the assignment remains intact during the frame exchange until the connection is terminated.

##### Single-sided redundancy

**Description**

One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.

**Configuration**

If the S7 is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner and one connection from the S7 connection point 1 to junction A of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**

The figure illustrates the connection designations.

![Modbus/TCP: Single-sided redundancy S7](images/112743929483_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Single-sided redundancy S7

If the S7 is designed as standalone and the link partner is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner and one connection from the S7 connection point 0 to junction B of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **0** to the partner/node **B** => connection **0B**

The figure illustrates the connection designations.

![Modbus/TCP: Single-sided redundancy partner](images/104186959371_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Single-sided redundancy partner

##### Double-sided redundancy

**Description**

One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.

**Configuration**

In the case of double-sided redundancy, two connections are created from connection point 0 and two connections from connection point 1 of the S7 to the junctions A and B of the link partner.

- Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**
- Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**
- Connection from the S7 connection point **0** to the partner/node **B** => connection **0B**
- Connection from the S7 connection point **1** to the partner/node **B** => connection **1B**

The figure illustrates the connection designations.

![Modbus/TCP: Double-sided redundancy](images/112743940107_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: Double-sided redundancy

##### Frame processing

Frames can be received via all configured connections. The client can send frames either via one connection or via all connections. If a frame was received on a connection, the status is displayed at the corresponding output DR_NDR_x or ERROR_x. Each connection runs independently and has no influence on the display of the other connections.

##### Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR

**Description**

The redundancy bits RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR are set based on the states of the status outputs.

**Display of the interrupt bits for redundancy setup on both sides**

![Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR](images/104278212619_DV_resource.Stream@PNG-en-US.png)

**Display of the interrupt bits for redundancy setup on one side**

![Redundancy outputs RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR](images/104296715531_DV_resource.Stream@PNG-en-US.png)

#### Parameter assignment (S7-1200, S7-1500)

##### Description

The instruction "MB_RED_SERVER" **V1.0** and **V1.1** can be used for S7-1200 and for S7-1500.

**S7-1200**

The connections are implemented over the local interface of the CPU or CM/CP. The connections are configured and established using the structure TCON_IP_V4.

**S7-1500**

The connections are implemented over the local interface of the CPU or CM/CP. Configured connections over the structure TCON_IP_V4 as well as configured connections over the structure TCON_Configured are possible.

The instruction "MB_RED_SERVER" **V1.1** can be used for S7-1500R and for S7-1500H.

**S7-1500R and S7-1500H**

The connections are implemented over the local interface of the CPU or CM/CP. The connections are configured and established using the structure TCON_IP_V4.

##### Configuration of "MB_RED_SERVER"

The following settings are made with the help of the configuration dialog of the instruction "MB_RED_SERVER":

- Connection parameters for the connections 0A, 1A, 0B and 1B (Redundancy configuration see [Operation and Redundancy](#operation-and-redundancy-s7-1200-s7-1500-1))
- Internal parameter (optional)

The configuration dialog can be opened with the instruction or via the technology objects.

> **Note**
>
> **Using the configuration dialog**
>
> The configuration dialog can only be used when called with single-instance DBs. If there is a multi-instance, the parameters have to be set manually.

**Connection parameters**

![Modbus/TCP: configured server connection](images/113202502539_DV_resource.Stream@PNG-en-US.PNG)

Modbus/TCP: configured server connection

![Modbus/TCP: configured server connection](images/113202536587_DV_resource.Stream@PNG-en-US.PNG)

Modbus/TCP: configured server connection

| Tag | Start value | Description |
| --- | --- | --- |
| **Configured connections** |  |  |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used. These connection IDs must be unique throughout the CPU. |
| Local port | 502 | Local port number of the server block. The default port for Modbus/TCP server is 502. |
| Remote IP | 0.0.0.0 | Remote IP address of the client. By default no IP address is entered for the client. |
| Remote port | 0 | Remote port number of the client. By default no port number is entered for the client. |
| **Configured connections** |  |  |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used. These connections are configured in the network view. |

**Internal parameter (optional)**

![Configuration of "MB_RED_SERVER"](images/113202402315_DV_resource.Stream@PNG-en-US.PNG)

| Tag | Data type | Start value | Description |
| --- | --- | --- | --- |
| HR_Start_Offset | WORD | 0 | Assign the start address of the Modbus holding register. |
| QB_Start | UINT | 0 | Start address of the permitted addressing range of the outputs that can be written (bytes 0 to 65535) |
| QB_Count | UINT | 0 | Number of output bytes that can be written by the Modbus master.   Example:   QB_Start=0 and QB_Count=10: Output bytes 0 to 9 can be written.  QB_Count=0: No output byte can be written. |
| QB_Read_Start | UINT | 0 | Start address of the permitted addressing range of the outputs that can be read (bytes 0 to 65535) |
| QB_Read_Count | UINT | 0 | Number of output bytes that can be read by the Modbus master.   Example:   QB_Read_Start=0 and QB_Read_Count=10: Output bytes 0 to 9 can be read.  QB_Read_Count=0: No output byte can be read. |
| IB_Read_Start | UINT | 0 | Start address of the permitted addressing range of the inputs that can be read (bytes 0 to 65535) |
| IB_Read_Count | UINT | 0 | Number of input bytes that can be read by the Modbus master.   Example:   IB_Read_Start=0 and IB_Read_Count=10: Input bytes 0 to 9 can be read.  IB_Read_Count=0: No input byte can be read. |
| Data_Area_Array | ARRAY [1..8] |  |  |
| data_type | UINT | 0 | Data Type: 0 to 4 |
| db | UINT | 0 | Data block number |
| start | UINT | 0 | First Modbus address in the data block |
| length | UINT | 0 | Number of Modbus values in the data block |

##### Addressing via static tag HR_Start_Offset

The addresses of the Modbus holding register start at 0.

Example: The holding register begins at MW100, and has a length of 100 WORD.

![Modbus/TCP: HR_Start_Offset = 0](images/104209410315_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: HR_Start_Offset = 0

You can define the tag HR_Start_Offset so that the Modbus holding register has a start address other than 0.

Example: An offset value 20 in the parameter HR_Start_Offset means that the start address of the holding register is moved from 0 to 20. This causes an error whenever the holding register is addressed below the address 20 and above the address 119.

![Modbus/TCP: HR_Start_Offset = 20](images/104210533643_DV_resource.Stream@PNG-en-US.png)

Modbus/TCP: HR_Start_Offset = 20

##### Data_Area_Array [1..8]

**Description**

![Data_Area_Array [1..8]](images/113202513163_DV_resource.Stream@PNG-en-US.PNG)

There are eight data areas available for mapping the MODBUS addresses in the SIMATIC S7 memory. If the first data area is defined, the parameter MB_HOLD_REG is not evaluated. Instead, the Modbus register and bits are written in the data blocks or read from them depending on the job type. These values can be further processed in the subsequent execution of the program.

You can only read from one DB or write to one DB with any job. Access to registers or bit values that are located in several DBs, even if the numbers are in a sequence without gaps, are to be divided into two jobs. Keep this in mind during configuration. It is possible to map more Modbus areas (registers or bit values) in one data block than can be processed with one frame.

****data_type****

The data_type parameter specifies which MODBUS data types are mapped in this data block. If the value 0 is entered in data_type, the corresponding data area is not used. If multiple Data_Area are to be used, these must be defined one after the other. All entries after a data_type = 0 are not processed.

| Identifier | Data type | Description |
| --- | --- | --- |
| 0 | Area not used |  |
| 1 | Output bits (Coils) | Bit |
| 2 | Input bits (Inputs) | Bit |
| 3 | Holding register | Word |
| 4 | Input words (Input Register) | Word |

**db**

The db parameter specifies the data block which maps the MODBUS registers or bit values defined below. The DB number 0 is not permitted because it is reserved for the system.

**start, length**

start specifies the first Modbus address which is mapped in data word 0 of the DB. The parameter length defines the length of how many MODBUS addresses are mapped in the data block. The defined data areas must not overlap. The length parameter must not be 0.

##### Example: Address mapping with Data_Area_Array

|  |  |  |
| --- | --- | --- |
| Data area 1 | data_type | 3: Holding register |
| db | 11 |  |
| start | 0 |  |
| length | 500 |  |
| Data area 2 | data_type | 3: Holding register |
| db | 12 |  |
| start | 720 |  |
| length | 181 |  |
| Data area 3 | data_type | 4: Input words |
| db | 13 |  |
| start | 720 |  |
| length | 281 |  |
| Data area 4 | data_type | 1: Output bits |
| db | 14 |  |
| start | 640 |  |
| length | 611 |  |
| Data area 5 | data_type | 2: Input bit |
| db | 15 |  |
| start | 1700 |  |
| length | 601 |  |
| Data area 6 | data_type | 1: Output bits |
| db | 16 |  |
| start | 1700 |  |
| length | 601 |  |
| Data area 7 | data_type | Not used |
| db | 0 |  |
| start | 0 |  |
| length | 0 |  |
| Data area 8 | data_type | Not used |
| db | 0 |  |
| start | 0 |  |
| length | 0 |  |

![Example: Address mapping with Data_Area_Array](images/104210543627_DV_resource.Stream@PNG-en-US.png)

#### Licensing (S7-1200, S7-1500)

The instruction "MB_RED_SERVER" is subject to a fee and must be licensed on each CPU individually. Licensing takes place in two steps:

- Reading out the IDENT_CODE and
- Entering the registration key REG_KEY.

> **Note**
>
> **S7-1500R and S7-1500H**
>
> For an S7-R/H station only CPU1 is licensed. A replacement of CPU1 after licensing is therefore no longer possible.

> **Note**
>
> **Transfer of the license / PLCSIM**
>
> It is not possible to transfer the license from one CPU to another.
>
> The instruction may not be licensed with PLCSIM.

##### Procedure

**Reading out the IDENT_CODE**

Proceed as follows to read out the IDENT_CODE:

1. Assign parameters to the "MB_RED_SERVER" instruction in line with your requirements in a cyclic OB. Download the program to the CPU and set it to RUN.
2. Open the instance DB of the Modbus instruction and click the "Monitor all" button.
3. An 18-digit character string is displayed at the IDENT_CODE output.

   ![Procedure](images/113202649611_DV_resource.Stream@PNG-en-US.png)
4. Copy this string using copy/paste from the data block and paste it in the form that was sent to you by email after you ordered the product or is included on the CD.
5. Send the form to [Customer support](https://support.industry.siemens.com/my/ww/en/requests/#createRequest) using a service request. You will then receive the registration key for your CPU.

**Entering the registration key REG_KEY**

The registration key REG_KEY must be specified at each "MB_RED_SERVER" instruction. You should save the REG_KEY in a global data block from which all "MB_RED_SERVER" instructions receive the necessary registration key.

Proceed as follows to enter the registration key REG_KEY:

- Insert a new global data block with a unique symbolic name, for example "License_DB", using "Add new block…".
- Create a REG_KEY parameter in this block with the data type STRING[17].

  ![REG_KEY in DB](images/66691684107_DV_resource.Stream@PNG-en-US.png)

  REG_KEY in DB
- Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
- In the cyclic OB, enter the name of the license DB and the name of the string, e.g. License_DB.REG_KEY, at the parameter REG_KEY of the ""MB_RED_SERVER"" instruction.
- Download the modified blocks to the CPU. The registration key can be entered during runtime; a change from STOP -> RUN is not necessary.

The Modbus/TCP communication using the "MB_RED_SERVER" instruction is now licensed for this CPU, the output bit LICENSED is TRUE.

**Missing or incorrect licensing**

If you enter an incorrect registration key or none at all, the ERROR-LED of the CPU flashes. In addition for S7-1200 and S7-1500, a cyclic entry is made in the diagnostics buffer regarding the missing license. Only the area length error is displayed for R and H stations.

![Procedure](images/113202685835_DV_resource.Stream@PNG-en-US.png)

In the case of a missing or incorrect registration key, the Modbus/TCP communication is processed but W#16#0A90 "No valid license available" is always displayed at the STATUS_x output. The output bit LICENSED is FALSE.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **If OB121 is missing in the controller in the S7-1500 (R/H), the CPU is set to STOP.** |  |

#### MB_HOLD_REG input parameter (S7-1200, S7-1500)

##### Description

The MB_HOLD_REG parameter is a pointer to a data buffer for storing the data to which a Modbus client has read or write access. You can use a global data block (D) or bit memory (M) as memory area.

- The high limit for the number of addresses in the data block (D) is determined by the maximum size of a DB of your CPU.
- The high limit for the number of bit memories (M) is determined by the maximum bit memory area of your CPU.

The following figures show some examples of mapping Modbus addresses to the holding register for the Modbus functions 3 (read multiple WORD), 6 (write one WORD), 16 (write multiple WORD) and 23 (write and read multiple WORD).

**MB_HOLD_REG: Data block with offset 0**

![Description](images/104272978059_DV_resource.Stream@PNG-en-US.png)

**MB_HOLD_REG: Data block with offset 60**

![Description](images/104275816587_DV_resource.Stream@PNG-en-US.png)

##### Data_Area_Array [1..8]

To use the optional parameters Data_Area_Array [1..8] see [Parameter assignment](#parameter-assignment-s7-1200-s7-1500-1).

#### Output parameters ERROR_x, STATUS_x, RED_ERR_S7, RED_ERR_DEV and TOT_COM_ERR (S7-1200, S7-1500)

##### Parameter STATUS_x (general status information)

The error messages are displayed at the status outputs of the instruction "MB_RED_SERVER".

| STATUS* (W#16#) | Description |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 0A90 | The instruction "MB_RED_SERVER" is not licensed. Additional information is available here: [Licensing](#licensing-s7-1200-s7-1500-1). |
| 0AFF | The connection is not configured and is not used. The connection 0A must be configured. |
| 7000 | No call active and no connection established (REQ=0, DISCONNECT=1). |
| 7001 | First call. Connection establishment triggered. |
| 7002 | Intermediate call. Connection is being established. |
| 7003 | Connection is being terminated. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

##### Parameter STATUS_x (protocol error)

| STATUS* (W#16#) | Error code in the error message from "MB_RED_SERVER" (B#16#) | Description |
| --- | --- | --- |
| 8380 | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | 01 | Function code is not supported. |
| 8382 | 03 | Error in data length:  - Invalid length specification in received Modbus frame - The frame length entered in the header of the Modbus frame does not match the number of actually received bytes. - The number of bytes entered in the header of the Modbus frame does not match the number of actually received bytes (functions 15 and 16). |
| 8383 | 02 | Error in data address or access outside the address area of the holding register ([MB_HOLD_REG](#mb_hold_reg-input-parameter-s7-1200-s7-1500) parameter). |
| 8384 | 03 | Error in the data value (function 05) |
| 8385 | 03 | Diagnostic code is not supported (only with function 08). |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |  |

##### Parameter STATUS_x (parameter error)

| STATUS* (W#16#) | Description |
| --- | --- |
| 80BB | The ActiveEstablished parameter has an invalid value   Only passive connection establishment permitted for server (active_established = FALSE). |
| 8187 | The MB_HOLD_REG parameter has an invalid pointer. Data area is too small. |
| 8389 | Invalid data area definition:  - Invalid data_type value - DB number invalid or does not exist:   - Invalid db value   - DB number does not exist   - DB number is already used by another data area   - DB with optimized access   - DB is not located in the work memory - Invalid length value - Overlapping of MODBUS address ranges that belong to the same MODBUS data type |
| * The status codes can be displayed as integer or hexadecimal values in the program editor. You can find information on switching the display formats under "See also". |  |

> **Note**
>
> **Error codes of internally used communication instructions**
>
> With the "MB_RED_SERVER"" instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND", "TRCV", "T_DIAG" and "T_RESET") used by the instruction can occur.
>
> The error codes are assigned via the instance data block of the "MB_RED_SERVER" instruction. The error codes are displayed for the respective instruction under STATUS in the "Static" section of the individual instances.
>
> The meaning of the error codes is available in the documentation of the corresponding communications instruction.

> **Note**
>
> **Communication error when sending or receiving data**
>
> If a communication error occurs when sending or receiving data (80C4 (Temporary communication error. The specified connection is temporarily terminated.), 80C5 (The remote partner has actively terminated the connection.), 80A1 (The specified connection is interrupted or has not been established yet.)), the existing connection is terminated.
>
> This also means that you can see all STATUS values that are returned when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.
>
> Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

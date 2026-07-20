---
title: "Open User Communication (S7-1200, S7-1500)"
package: ProgKomOUC2MenUS
topics: 74
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Open User Communication (S7-1200, S7-1500)

This section contains information on the following topics:

- [Data consistency (S7-1200, S7-1500)](#data-consistency-s7-1200-s7-1500)
- [TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500)
- [TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500)
- [Program example for send functions (S7-1200, S7-1500)](#program-example-for-send-functions-s7-1200-s7-1500)
- [TMAIL_C: Transfer email (S7-1200, S7-1500)](#tmail_c-transfer-email-s7-1200-s7-1500)
- [CommConfig: Reading and changing communication parameters (S7-1500)](#commconfig-reading-and-changing-communication-parameters-s7-1500)
- [Other (S7-1200, S7-1500)](#other-s7-1200-s7-1500)
- [Changes to the communications instructions (S7-1200, S7-1500)](#changes-to-the-communications-instructions-s7-1200-s7-1500)

## Data consistency (S7-1200, S7-1500)

### Ensuring data consistency

In the S7-1500 module series, you can change parameters during ongoing operation with the instructions of the Open User Communication. Changed parameters are used immediately, even if a job is still active. Both can lead to data inconsistency! To avoid data inconsistencies, you should never change parameters while a job is running.

## TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)

This section contains information on the following topics:

- [TSEND_C: Send data via Ethernet (S7-1200)](#tsend_c-send-data-via-ethernet-s7-1200)
- [TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)

### TSEND_C: Send data via Ethernet (S7-1200)

#### Validity

The following description of the "TSEND_C" instruction applies to S7-1200 CPUs with firmware version &lt; V4.0.

#### Description

The "TSEND_C" instruction sets up and establishes a TCP or ISO-on-TCP communication connection. Once the connection has been set up and established, it is automatically maintained and monitored by the CPU. The connection description specified at the CONNECT parameter is used to set up the communication connection.

The instruction is executed asynchronously and has the following functions:

- A communication connection is set up and established:  
  The communication connection is set up and established with CONT=1. Once the connection is successfully established, the DONE parameter is set to "1" for one cycle. An existing connection is terminated and the connection which has been set up is removed when the CPU goes into STOP mode. To set up and establish the connection again, you must execute "TSEND_C" again. For information on the number of possible communication connections, refer to the technical specifications for your CPU.
- Sending data via an existing communication connection:  
  You specify the send area with the DATA parameter. This includes the address and the length of the data to be sent. Do not use a data area with the data type BOOL or Array of BOOL at the DATA parameter. If you use purely symbolic values at the DATA parameter, the LEN parameter must have the value "0".
- The send job is executed when a rising edge is detected at the REQ parameter. With the LEN parameter, you specify the maximum number of bytes sent with a send job. When sending data (rising edge at the REQ parameter), the CONT parameter must have the value "1" in order to establish or maintain a connection. The data to be sent must not be edited until the send job is completed. If the send job executes successfully, the DONE parameter is set to "1". Signal state "1" at the DONE parameter is not confirmation that the data sent has already been read by the communication partner.
- Terminating the communication connection:

  The communication connection is terminated when the CONT parameter is set to "0" even if an ongoing data transfer is not complete yet. This does not apply if you are using an already configured connection for "TSEND_C".

When setting the COM_RST parameter to "1", the currently established connection or a current data transmission can be reset at any time. This terminates the existing communication connection and a new connection is established. If data is being transferred when it executes again, this can lead to a loss of data.

To enable "TSEND_C" again after the execution (DONE = 1), call the instruction once with REQ = 0.

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and create connections of the type TCP, UDP or ISO-on-TCP and want to assign parameters to them, you can use the support of the connection parameter assignment.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

#### Parameters

The following table shows the parameters of the "TSEND_C" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Starts the send job on a rising edge. |
| CONT | Input | BOOL | I, Q, M, D, L | Controls the communication connection:  - 0: Disconnect the communication connection - 1: Establish and maintain the communication connection   When sending data (rising edge at the REQ parameter), the CONT parameter must have the value TRUE in order to establish or maintain a connection. |
| LEN | Input | UINT | I, Q, M, D, L or constant | Maximum number of bytes to be sent with the job. If you use purely symbolic values at the DATA parameter, the LEN parameter must have the value "0". |
| CONNECT | InOut | TCON_Param | D | Pointer to the connection description  See also: [Connection parameters with structure according to TCON_Param](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t) |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the send area containing the address and the length of the data to be sent (maximum length: 8192 bytes).  When transferring structures, the structures must be identical at the sending and receiving end. |
| COM_RST | InOut | BOOL | I, Q, M, D, L | Restarts the instruction:  - 0: Irrelevant - 1: Complete restart of the instruction causing an existing connection to be terminated and a new connection to be established. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or still in progress - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set if errors occur during execution of "TSEND_C". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is specified in the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

#### ERROR and STATUS parameters

| ERROR | STATUS*  (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Job completed without error. |
| 0 | 0001 | The connection establishment is complete. |
| 0 | 0003 | The connection termination is complete. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | - Start execution of the job - Establish connection - Wait for connection partner |
| 0 | 7002 | Data was sent. |
| 0 | 7003 | Connection is being terminated. |
| 0 | 7004 | Connection established and monitored, no job processing active. |
| 1 | 80A0 | Group error for error codes 80A1 and 80A2. |
| 1 | 80A1 | - Connection or local port already being used by user. - Communication error:   - The specified connection has not yet been established.   - The specified connection is being terminated. Transfer via this connection is not possible.   - The interface is being re-initialized. |
| 1 | 80A2 | Local port is being used by the system. |
| 1 | 80A3 | Attempt being made to terminate a non-existent connection. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid, in other words, it matches the IP address of the local partner. |
| 1 | 80A7 | Communication error: You called the instruction with COM_RST = 1 before the send job was complete. |
| 1 | 80AA | A connection is currently being established with the same connection ID by another block. Repeat the job with a new rising edge at the REQ parameter. |
| 1 | 80B2 | The CONNECT parameter points to a data block that was generated with the attribute "Only store in load memory". |
| 1 | 80B3 | Inconsistent parameter assignment: Group error for error codes 80A0 to 80A2, 80A4, 80B4 to 80B9. |
| 1 | 80B4 | When using the protocol variant ISO on TCP (connection_type = B#16#12) for the passive establishment of a connection (active_est = FALSE) one or both of the following conditions was violated: "local_tsap_id_len &gt;= B#16#02" and/or "local_tsap_id[1] = B#16#E0". |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP. |
| 1 | 80B6 | Parameter assignment error in the connection_type parameter of the data block for connection description. |
| 1 | 80B7 | Error in one of the following parameters of the data block for connection description: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len. |
| 1 | 8085 | The LEN parameter is larger than the highest permitted value. |
| 1 | 8086 | The ID parameter within the CONNECT parameter is outside the permitted range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible. |
| 1 | 8088 | The value at the LEN parameter does not correspond to the receive area set at the DATA parameter. |
| 1 | 8089 | The CONNECT parameter does not point to a data block. |
| 1 | 8091 | Maximum nesting depth exceeded. |
| 1 | 809A | The CONNECT parameter points to a field that does not correspond to the length of the connection description. |
| 1 | 809B | The ID of the local device in the connection description does not correspond to the CPU. |
| 1 | 80C3 | - All connection resources are in use. - A block with this ID is already being processed in a different priority group. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is receiving new parameters or the connection is being established. - The configured connection is currently being removed by a "TDISCON" instruction. - The connection used is being terminated by a call with COM_RST= 1. |
| 1 | 80C6 | Remote network error. Remote partner cannot be reached. |
| 1 | 8722 | Parameter CONNECT: The source area is invalid. The area does not exist in the DB. |
| 1 | 873A | Parameter CONNECT: Access to the connection description is not possible (for example, DB does not exist). |
| 1 | 877F | Parameter CONNECT: Internal error. |
| 1 | 8822 | Parameter DATA: Invalid source area, the area does not exist in the DB. |
| 1 | 8824 | Parameter DATA: Area error in the VARIANT pointer. |
| 1 | 8832 | Parameter DATA: The DB number is too high. |
| 1 | 883A | Parameter DATA: No access to the data area, for example because the data block does not exist |
| 1 | 887F | Parameter DATA: Internal error, e.g. invalid VARIANT reference. |
| 1 | 893A | Parameter ADDR: Access to send area not possible (e.g. because the DB does not exist). |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

> **Note**
>
> **Error messages of the instructions "TCON", "TSEND", "T_DIAG" and "TDISCON"**
>
> Internally, the "TSEND_C" instruction uses the instructions "[TCON](#tcon-establish-communication-connection-s7-1200)", "[TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)", "[T_DIAG](#t_diag-checking-the-connection-s7-1200-s7-1500)", "[T_RESET](#t_reset-resetting-the-connection-s7-1200-s7-1500)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)". The error messages of these instructions can also be output at the STATUS parameter. The meaning of the error codes is described in the corresponding instructions. In the event of identical error codes for internally used instructions with different meanings, the instance data block of "TSEND_C" can be used to determine which instruction output the error.

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)

### TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)

#### Validity

The following description of the "TSEND_C" instruction is valid for:

- Ethernet

  - CPU S7-1200 with firmware version ≥ V4.0 and CPU S7-1500
  - CPU S7-1500 as of firmware version V2.1: UDP multicast communication
  - CPU S7-1500 as of firmware version V2.0 and TSEND_C as of instruction version V3.2: Secure communication
- PROFIBUS

  FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL

#### Description

The "TSEND_C" instruction sets up and establishes a communication connection. Once the connection has been set up and established, it is automatically maintained and monitored by the CPU.

The instruction is executed asynchronously and has the following functions:

- Setting up and establishing a communication connection
- Sending data via an existing communication connection
- Terminating or resetting the communication connection

Internally, the instruction "TSEND_C" uses the communication instructions "TCON", "TSEND", "T_DIAG", "T_RESET" and "TDISCON".

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and wish to create and assign parameters to connections of the type TCP, UDP, ISO‑on‑TCP or FDL, you can use the support of the connection parameter assignment. UDP multicast connections via the integrated PROFINET interfaces are possible for S7-1500-CPUs as of firmware version V2.1 and higher.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

#### Setting up and establishing a communication connection

The communication connection is set up and established with CONT=1. For information on the number of possible communication connections, refer to the technical specifications for your CPU. The connection description specified at the CONNECT parameter is used to set up the communication connection. The following connection types can be used:

- Programmed connections (structure of connection via "TCON"):

  - TCP / UDP: Connection description via the TCON_IP_v4 system data type
  - TCP using secure communication Connection description via the system data types TCON_IP_V4_SEC or TCON_QDN_SEC
  - ISO-on-TCP: Connection description via the TCON_IP_RFC system data type
  - ISO: Connection description via the system data type TCON_ISOnative (CP 1543‑1 / CP 1545‑1)
  - Telecontrol connections to SMS clients: Connection description via the TCON_PHONE system data type

    For this connection type, the station requires access to the mobile network via a mobile network CP.
  - FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL
- Configured connections

  - Specify an existing connection in the TCON_Configured system data type.

An existing connection is terminated and the connection which has been set up is removed when the CPU goes into STOP mode. To set up and establish the connection again, you must execute "TSEND_C" again.

#### Sending data via an existing communication connection

The send job is executed when a rising edge is detected at the REQ parameter. As described above, the communication connection is established first.

You specify the send area with the DATA parameter. This includes the address and the length of the data to be sent. Do not use a data area with the data type BOOL or Array of BOOL at the DATA parameter. With the LEN parameter, you specify the maximum number of bytes sent with a send job. If you use a send area with optimized access at the DATA parameter, the LEN parameter must have the value "0".

The data to be sent must not be edited until the send job is completed.

#### Terminating and resetting the communication connection

The communication connection is terminated when the CONT parameter is set to "0" even if an ongoing data transfer is not complete yet. This does not apply if you are using a configured connection for "TSEND_C".

The connection can be reset at any time by setting the parameter COM_RST to "1". This terminates the existing communication connection and a new connection is established. If data is being transferred at this time, this can lead to data loss.

#### Parameters

The following table shows the parameters of the "TSEND_C" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C or constant | Starts the send job on a rising edge. |
| CONT | Input | BOOL | I, Q, M, D, L | Controls the communication connection:  - 0: Disconnect the communication connection. - 1: Establish and maintain the communication connection. |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Optional parameter (hidden)  Maximum number of bytes to be sent with the job. If you use a send area with optimized access at the DATA parameter, the value "0" must be used at the LEN parameter.  For FDL connections of the CM 1542‑5, the maximum length is 240 bytes. In this regard, note the maximum lengths that can be processed by the connection partner. |
| CONNECT | InOut | VARIANT | D | Pointer to the structure of the connection description:  - Programmed connection:   - For TCP or UDP, use the TCON_IP_v4 system data type. For a description, refer to[Connection parameters with structure according to TCON_IP_v4](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500).   - For TCP with secure communication, use the structure TCON_IP_V4_SEC or TCON_QDN_SEC.     For a description, refer to: [Connection parameters in accordance with TCON_IP_V4_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500) or [connection parameters in accordance with TCON_QDN_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)   - For ISO-on-TCP, use the TCON_IP_RFC system data type. For a description, refer to [Connection parameters with structure according to TCON_IP_RFC](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500).   - For ISO, use the TCON_ISOnative system data type (CP 1543‑1 / CP 1545‑1). For description, refer to instruction "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)".   - For connections to SMS clients, use the TCON_PHONE system data type. For a description, refer to [Connection parameters to TCON_Phone](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_phone-s7-1200-s7-1500-s7-1500t).   - For FDL connections of the CM 1542‑5, use the system data type TCON_FDL; see [Connection parameters to TCON_FDL](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_fdl-s7-1200-s7-1500). - Configured connection:   - For existing connections, use the TCON_Configured system data type. For a description, see "System data type for configured connections" below. |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the send area containing the address and the length of the data to be sent.  When transferring structures, the structures must be identical at the sending and receiving end. |
| ADDR | InOut | VARIANT | D | Hidden parameter that needs to be used, however, with UDP. In this case it contains a pointer to the system data type TADDR_Param. Store the address information of the recipient (IP address and port number) in a data block with the system data type TADDR_Param.  See also: [Structure of the address information of the remote partner with UDP](#addressing-the-remote-partner-via-taddr_param-s7-1200-s7-1500) |
| COM_RST | InOut | BOOL | I, Q, M, D, L | Optional parameter (hidden)  Resets the connection:  - 0: Irrelevant - 1: The existing connection is reset.   The COM_RST parameter is reset after evaluation by the "TSEND_C" instruction and should not, therefore, be interconnected statically. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Send job not yet started or still in progress. - 1: Send job executed without error. This state is only displayed for one cycle. |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Send job not yet started or already completed. - 1: Send job not yet completed. A new send job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred during connection establishment, data transfer or connection termination.   The output parameter ERROR can be set due to an error in the "TSEND_C" instruction or the communication instructions used internally. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of instruction (see the "ERROR and STATUS parameters" description). |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### REQ, CONT and COM_RST parameters

The parameter CONT controls the connection establishment of the "TSEND_C" instruction regardless of the REQ parameter. The behavior of the CONT parameter partially depends on whether a programmed or a configured connection is used:

- With CONT = "0": No data is sent (regardless of whether a programmed or a configured connection is used).
- When changing CONT = "0" to "1":

  - With a programmed connection, it is established with "TCON".
  - With a configured connection, it is checked with "T_DIAG".
- With CONT = "1":

  - As long as no data is sent (REQ="0"), the connection is checked with "T_DIAG".
  - If the internally used communication instructions signal that no connection end point exists, the connection is automatically reestablished with "TCON".
- When changing CONT = "1" to "0":

  - With a programmed connection, it is terminated with "TDISCON".
  - With a configured connection, it is reset with "T_RESET".

The parameter COM_RST resets the connection when changing from "0" to "1":

- If a connection is established, it is reset with "T_RESET" (regardless of whether a programmed or configured connection is used).
- If no connection is established, the setting of the parameter has no effect.

The REQ and COM_RST parameters only have an effect if CONT has been set to "1". The following table shows the relationship between the REQ, CONT and COM_RST parameters:

| REQ | CONT | COM_RST | Status of the instruction | Description |
| --- | --- | --- | --- | --- |
| Irrelevant | 0 | Irrelevant | Not yet executed | No job active (STATUS = 7000). |
| Irrelevant | 0 | Irrelevant | Initialization | Connection is being terminated. The instruction is being reset. |
| Irrelevant | 0 &gt; 1 | Irrelevant | Connection establishment | Connection is being established. Data is not being transferred yet. |
| 0 | 1 | 0 | Connection established | The connection is established and is monitored with the instruction "T_DIAG". |
| Irrelevant | 1 | 0 &gt; 1 | Connection established | The connection is interrupted by "T_RESET" briefly and reset. |
| 0 &gt; 1 | 1 | 0 | Connection established | Instruction starts sending. |
| Irrelevant | 1 | 0 &gt; 1 | Data is being sent | Data transfer is interrupted. The connection is being reset. |

#### System data type for configured connections

For configured connections at the CONNECT parameter, use the following structure for connection description to TCON_Configured:

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | - | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | - | Reference to the connection (value range: 1 to 4095).  Enter the connection ID of the existing connection. |
| 4 | ConnectionType | BYTE | - | Connection type  Select 254 (decimal) for a configured connection. |

> **Note**
>
> For reasons of compatibility, the parameters InterfaceID and ConnectionType are part of the structure for the connection description to TCON_Configured. These parameters do not have an effect on the connection parameter assignment; only the parameter ID for the connection ID is evaluated in the connection parameter assignment.

#### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a send job executed successfully. The ERROR parameter is set if errors occur during execution of "TSEND_C". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| DONE | BUSY | ERROR | Description |
| --- | --- | --- | --- |
| 0 | 0 | 0 | The instruction has not been executed yet (no rising edge at REQ parameter). |
| 0 | 1 | 0 | The instruction is being executed and calls the internally used communication instructions. |
| 1 | 0 | 0 | The send job was completed successfully. "0000" is output at the STATUS parameter. DONE = "1" is only displayed for one cycle. |
| 0 | 0 | 1 | The execution of the instruction or an intermediate step during processing was terminated with an error. If there is a subsequent error due to an internally used communication instruction, the error that occurred first during processing is displayed. This state is only displayed for one cycle. |

#### ERROR and STATUS parameters

| ERROR | STATUS*  (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Send job was executed without error. |
| 0 | 0001 | Communication connection established. |
| 0 | 0003 | Communication connection closed. |
| 0 | 7000 | No active send job execution; no communication connection established. |
| 0 | 7001 | Initial call for establishing a connection. |
| 0 | 7002 | Connection is currently being established (REQ irrelevant) |
| 0 | 7003 | Communication connection is being terminated. |
| 0 | 7004 | Communication connection has been established and is being monitored. No send job execution active. |
| 0 | 7005 | Data transfer in progress. |
| 1 | 80A1 | - Connection or local port already being used by user. - Communication error:   - The specified connection has not yet been established.   - The specified connection is being terminated.     Transfer via this connection is not possible.   - The interface is being re-initialized. |
| 1 | 80A3 | The nested "T_DIAG" instruction has reported that the connection has closed. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid or it matches the IP address of the local partner. |
| 1 | 80A7 | Communication error: You called the instruction with COM_RST = 1 before the send job was complete. |
| 1 | 80AA | A connection is currently being established with the same connection ID by another block. Repeat the job with a new rising edge at the REQ parameter. |
| 1 | 80B3 | - When using the protocol variant UDP the ADDR parameter does not contain any data. - Error in the connection description - The local port is already being used in a different connection description. |
| 1 | 80B4 | You have violated one or both of the following conditions for passive connection establishment (active_est = FALSE) when using the ISO-on-TCP protocol variant (connection_type = B#16#12):   - local_tsap_id_len &gt;= B#16#02 - local_tsap_id[1] = B#16#E0 |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP. |
| 1 | 80B6 | Parameter assignment error in the connection_type parameter of the data block for connection description. |
| 1 | 80B7 | - For system data type TCON_Param:   Error in one of the following parameters of the data block for connection description: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len. - For system data types TCON_IP_V4 and TCON_IP_RFC:   IP address of the partner end point was set to 0.0.0.0. |
| 1 | 8085 | The LEN parameter is larger than the highest permitted value. |
| 1 | 8086 | The ID parameter within the CONNECT parameter is outside the permitted range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible. |
| 1 | 8088 | The value at the LEN parameter does not correspond to the receive area set at the DATA parameter. |
| 1 | 8089 | - The CONNECT parameter does not point to a data block. - The CONNECT parameter does not point to a connection description. - The manually created connection description has an incorrect structure for the selected connection type. |
| 1 | 8091 | Maximum nesting depth exceeded. |
| 1 | 809A | The CONNECT parameter points to a field that does not correspond to the length of the connection description. |
| 1 | 809B | InterfaceID is invalid:  - It does not point to a local CPU interface or a CP. - If you are using the connection parameter assignment, it cannot have the value 0. - It must not have the value 0 in the used TCON_xxx structure. See [TCON: Establish communication connection](#tcon-establish-communication-connection-s7-1200-s7-1500) - TCON_QDN or TCON_QDN_SEC requires a configured DNS server. |
| 1 | 80C3 | - All connection resources are in use. - A block with this ID is already being processed in a different priority group. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is receiving new parameters or the connection is being established. - The configured connection is currently being removed by a "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instruction. - The connection used is being terminated by a call with COM_RST = 1. - Temporarily no receive resources available at the connection partner. The connection partner is not ready to receive. |
| 1 | 80C5 | - Connection terminated by the communication partner. - LSAP of the remote connection partner is not released. - When no connection is established, see also the description of STATUS 16#80C5 for [TCON](#tcon-establish-communication-connection-s7-1200-s7-1500) - When connection is established, see also the description of STATUS 16#80C5 for [TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1) |
| 1 | 80C6 | Network error:  - Remote partner cannot be reached. - Physical interruption on PROFIBUS. |
| 1 | 8722 | Parameter CONNECT: The source area is invalid. The area does not exist in the DB. |
| 1 | 873A | Parameter CONNECT: Access to the connection description is not possible (for example, because the DB is not available). |
| 1 | 877F | Parameter CONNECT: Internal error. |
| 1 | 8822 | Parameter DATA: Invalid source area, the area does not exist in the DB. |
| 1 | 8824 | Parameter DATA: Area error in the VARIANT pointer. |
| 1 | 8832 | Parameter DATA: The DB number is too high. |
| 1 | 883A | Parameter DATA: No access to the data area, for example because the data block does not exist |
| 1 | 887F | Parameter DATA: Internal error, e.g. invalid VARIANT reference. |
| 1 | 893A | Parameter ADDR: Access to send area not possible (e.g. because the DB does not exist). |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

> **Note**
>
> **Error messages of the instructions "TCON", "TSEND", "T_DIAG", "T_RESET" and "TDISCON"**
>
> Internally, the "TSEND_C" instruction uses the instructions "[TCON](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)", "[TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)", "[T_DIAG](#t_diag-checking-the-connection-s7-1200-s7-1500)", "[T_RESET](#t_reset-resetting-the-connection-s7-1200-s7-1500)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)". The error messages of these instructions can also be output at the STATUS parameter. The meaning of the error codes is described in the corresponding instructions. In the event of identical error codes for internally used instructions with different meanings, the instance data block of "TSEND_C" can be used to determine which instruction output the error.

#### Example

You can find the example here: [Program example for send functions](#program-example-for-send-functions-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

## TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)

This section contains information on the following topics:

- [TRCV_C: Receive data via Ethernet (S7-1200)](#trcv_c-receive-data-via-ethernet-s7-1200)
- [TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1)

### TRCV_C: Receive data via Ethernet (S7-1200)

#### Validity

The following description of the "TRCV_C" instruction applies to S7-1200 CPUs with firmware version &lt; V4.0.

#### Description

The "TRCV_C" instruction is executed asynchronously and has the following functions:

1. **Setting up and establishing a communication connection:**

   "TRCV_C" sets up and establishes a TCP or ISO-on-TCP communication connection. Once the connection has been set up and established, it is automatically maintained and monitored by the CPU.

   The connection description specified at the CONNECT parameter is used to set up the communication connection. To establish a connection, the CONT parameter must be set to the value "1". Once the connection is successfully established, the DONE parameter is set to "1".

   An existing connection is terminated and the connection which has been set up is removed when the CPU goes into STOP mode. To set up and establish the connection again, you must execute "TRCV_C" again.

   For information on the number of possible communication connections, refer to the technical specifications for your CPU.
2. **Receiving data via an existing communication connection:**
     
   If the EN_R parameter is set to the value "1", receipt of data is enabled. When receiving data (rising edge at the EN_R parameter), the CONT parameter must have the value TRUE in order to establish or maintain a connection.

   The received data is entered in a receive area. You specify the length of the receive area either with the LEN parameter (if LEN &lt;&gt; 0) or with the length information of the DATA parameter (if LEN = 0) in accordance with the protocol variant used. If you use purely symbolic values at the DATA parameter, the LEN parameter must have the value "0".

   After data has been received successfully, the signal state at the DONE parameter is "1". If errors occur in the data transfer, the DONE parameter is set to "0".
3. **Terminating the communication connection:**

   The communication connection is terminated immediately when the CONT parameter is set to "0".

TRCV_C is executed again when the COM_RST parameter is set. This terminates the existing communication connection and a new connection is established. If data is being received when it executes again, this can lead to a loss of data.

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and create connections of the type TCP, UDP or ISO-on-TCP and want to assign parameters to them, you can use the support of the connection parameter assignment.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

#### Receive modes of TRCV_C

The following table shows how the received data is entered in the receive area.

| Protocol variant | Availability of data in the receive area | connection_type parameter of the connection description | Parameter LEN |
| --- | --- | --- | --- |
| TCP  (Ad-hoc mode) | If NDR is set, at least one data byte is available. | Hexadecimal value: B#16#11  Integer value: 17 | 0 |
| TCP   (Receipt of data with specified length) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#11  Integer value: 17 | 1 to 8192 |
| ISO on TCP  (Message-oriented data transfer) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#12  Integer value: 18 | - 1 to 1452, if a CP is used. - 1 to 8192, if no CP is used. |

#### TCP (Ad-hoc mode)

The ad-hoc mode is only available with the TCP protocol variant. You use the ad-hoc mode to receive data with dynamic length with the "TRCV" instruction.

You set ad-hoc mode by assigning the value "0" to the LEN parameter.

Immediately after receiving a data block, the "TRCV_C" instruction transfers it to the receive area and sets NDR. RCVD_LEN contains information on the number of data bytes contained in this data block. The lowest possible value of RCVD_LEN is 1.

All data types can be used for data blocks with standard access when you use ad-hoc mode. Only ARRAY of BYTE or data types with a length of 8 bits can be used for data blocks with optimized access (e.g., CHAR, USINT, SINT, etc.).

#### TCP (Receipt of data with specified length)

You use the value of the LEN parameter to specify the length for the data receipt. The data receipt is not complete until the length of data specified at the LEN parameter has been completely received. Only then is the data available in the receive area (DATA parameter). The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

#### ISO on TCP (Message-oriented data transfer)

Complete message blocks are sent via a connection with the protocol variant ISO on TCP; these are recognized as such by the recipient. When using ISO on TCP, "TRCV_C" signals data receipt as soon as the message block has been completely received. The receive area is defined by the LEN and DATA parameters. If the receive buffer (DATA parameter) is too small for the sent data, "TRCV_C" signals an error. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

#### Parameters

The following table shows the parameters of the "TRCV_C" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Receive enable |
| CONT | Input | BOOL | I, Q, M, D, L | Controls the communication connection:  - 0: Disconnect the communication connection - 1: Establish and maintain the communication connection   When receiving data (rising edge at the EN_R parameter), the CONT parameter must have the value TRUE in order to establish or maintain a connection. |
| LEN | Input | UINT | I, Q, M, D, L or constant | Maximum length of the data to be received (maximum value: 8192 bytes). If you use purely symbolic values at the DATA parameter, the LEN parameter must have the value "0". |
| CONNECT | InOut | TCON_Param | D | Pointer to the connection description  See also: [Connection parameters with structure according to TCON_Param](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t) |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the receive area  When transferring structures, the structures must be identical at the sending and receiving end. |
| COM_RST | InOut | BOOL | I, Q, M, D, L | Restarts the instruction:  - 0: Irrelevant - 1: Complete restart of the instruction causing an existing connection to be terminated |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or still in progress - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |
| RCVD_LEN | Output | UINT | I, Q, M, D, L | Amount of data actually received in bytes |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set if errors occur during execution of "TRCV_C". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

#### ERROR and STATUS parameters

| ERROR | STATUS*  (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Job completed without error. |
| 0 | 0001 | The connection establishment is complete. |
| 0 | 0003 | The connection termination is complete. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | - Start execution of the job - Establish connection - Wait for connection partner |
| 0 | 7002 | Data is being received. |
| 0 | 7003 | Connection is being terminated. |
| 0 | 7004 | - Connection established and monitored - No job processing active |
| 0 | 7006 | Data is currently being received. |
| 1 | 8085 | - The LEN parameter is larger than the highest permitted value. - The value at the LEN or DATA parameter was changed after the first call. |
| 1 | 8086 | The ID parameter is outside the permitted range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible |
| 1 | 8088 | The value at the LEN parameter does not correspond to the receive area set at the DATA parameter. |
| 1 | 8089 | The CONNECT parameter does not point to a data block. |
| 1 | 8091 | Maximum nesting depth exceeded. |
| 1 | 809A | The CONNECT parameter points to a field that does not correspond to the length of the connection description. |
| 1 | 809B | The ID of the local device (local_device_id) in the connection description does not correspond to the CPU. |
| 1 | 80A0 | Group error for error codes W#16#80A1 and W#16#80A2. |
| 1 | 80A1 | - Connection or local port already being used by user. - Communication error:   - The specified connection has not yet been established.   - The specified connection is being terminated.     Transfer via this connection is not possible.   - The interface is being re-initialized. |
| 1 | 80A2 | Local port is being used by the system. |
| 1 | 80A3 | - Attempt being made to re-establish an existing connection. - Attempt being made to terminate a non-existent connection. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid, in other words, it matches the IP address of the local partner. |
| 1 | 80A7 | Communication error: You called the instruction with COM_RST = 1 before the send job was complete. |
| 1 | 80B2 | The CONNECT parameter points to a data block that was generated with the attribute "Only store in load memory". |
| 1 | 80B3 | Inconsistent parameter assignment: Group error for error codes W#16#80A0 to W#16#80A2, W#16#80A4, W#16#80B4 to W#16#80B9. |
| 1 | 80B4 | When using the protocol variant ISO on TCP (connection_type = B#16#12) for the passive establishment of a connection (active_est = FALSE) one or both of the following conditions was violated: "local_tsap_id_len &gt;= B#16#02" and/or "local_tsap_id[1] = B#16#E0". |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP. |
| 1 | 80B6 | Parameter assignment error in the connection_type parameter of the data block for connection description. |
| 1 | 80B7 | Error in one of the following parameters of the data block for connection description: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len. |
| 1 | 80C3 | - All connection resources are in use. - A block with this ID is already being processed in a different priority group. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is receiving new parameters or the connection is being established. - The configured connection is currently being removed by a "TDISCON" instruction. - The connection used is being terminated by a call with COM_RST= 1. |
| 1 | 80C6 | The remote partner cannot be reached (network error). |
| 1 | 8722 | Error in the CONNECT parameter: Invalid source area (area not declared in data block). |
| 1 | 873A | Error in the CONNECT parameter: Access to connection description is not possible (no access to data block). |
| 1 | 877F | Error in the CONNECT parameter: Internal error |
| 1 | 8922 | Parameter DATA: Invalid destination area; the area does not exist in the DB. |
| 1 | 8924 | Parameter DATA: Area error in the VARIANT pointer. |
| 1 | 8932 | Parameter DATA: The DB number is too high. |
| 1 | 893A | Parameter DATA: No access to the data area, for example because the data block does not exist. |
| 1 | 897F | Parameter DATA: Internal error, e.g. invalid VARIANT reference. |
| 1 | 8A3A | Parameter ADDR: No access to the address range, for example because the data block does not exist. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

> **Note**
>
> **Error messages of the instructions "TCON", "TRCV" and "TDISCON"**
>
> Internally, the "TRV_C" instruction uses the "[TCON](#tcon-establish-communication-connection-s7-1200)", "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instructions. The error messages of these instructions are contained in the respective descriptions.

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)

### TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)

#### Validity

The following description of the "TRCV_C" instruction is valid for:

- Ethernet:

  - CPU S7-1200 with firmware version as of V4.0 and CPU S7-1500
  - CPU S7-1500 as of firmware version V2.1: UDP multicast communication
  - CPU S7-1500 as of firmware version V2.0 and TRCV_C as of instruction version V3.2: Secure communication
- PROFIBUS: FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL

#### Description

The "TRCV_C" instruction is executed asynchronously and implements the following functions in sequence:

- Setting up and establishing a communication connection
- Receiving data via an existing communication connection
- Terminating or resetting the communication connection

Internally, the instruction "TRCV_C" uses the communication instructions "TCON", "TRCV", "T_DIAG", "T_RESET" and "TDISCON".

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and wish to create and assign parameters to connections of the type TCP, UDP, ISO‑on‑TCP or FDL, you can use the support of the connection parameter assignment. UDP multicast connections via the integrated PROFINET interfaces are possible for S7-1500-CPUs as of firmware version V2.1 and higher.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

#### Setting up and establishing a communication connection

The communication connection is set up and established with CONT=1. For information on the number of possible communication connections, refer to the technical specifications for your CPU. The connection description specified at the CONNECT parameter is used to set up the communication connection. The following connection types can be used:

- Programmed connections (structure of connection via "TCON"):

  - TCP / UDP: Connection description via the TCON_IP_v4 system data type
  - TCP using secure communication Connection description via the system data types TCON_IP_V4_SEC or TCON_QDN_SEC
  - ISO-on-TCP: Connection description via the TCON_IP_RFC system data type
  - ISO: Connection description via the system data type TCON_ISOnative (CP 1543‑1 / CP 1545‑1)
  - Telecontrol connections to SMS clients: Connection description via the TCON_PHONE system data type

    For this connection type, the station requires access to the mobile network via a mobile network CP.
  - FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL
- Configured connections

  - Specify an existing connection in the TCON_Configured system data type.

An existing connection is terminated and the connection which has been set up is removed when the CPU goes into STOP mode. To set up and establish the connection again, you must execute "TRCV_C" again.

#### Receiving data via an existing communication connection

Receipt of data is enabled when the EN_R parameter is set to the value "1". The received data is entered in a receive area. You specify the length of the receive area either with the LEN parameter (if LEN &lt;&gt; 0) or with the length information of the DATA parameter (if LEN = 0), depending on the protocol variant being used. If you use purely symbolic values at the DATA parameter, the LEN parameter must have the value "0".

Receive modes of TRCV_C:

- **TCP**
   **(Ad-hoc mode)**

  The ad-hoc mode is only available with the TCP protocol variant. You use the ad-hoc mode to receive data with dynamic length with the "TRCV_C" instruction.

  You set ad-hoc mode by assigning the value "1" to the ADHOC parameter.

  Immediately after receiving a data block, the "TRCV_C" instruction transfers it to the receive area and sets DONE. RCVD_LEN contains information on the number of data bytes contained in this data block. The lowest possible value of RCVD_LEN is 1.

  All data types can be used for data blocks with standard access when you use ad-hoc mode. Only ARRAY of BYTE or data types with a length of 8 bits can be used for data blocks with optimized access (e.g., CHAR, USINT, SINT, etc.).
- **TCP**
   **(Receipt of data with specified length)**

  Assign the value "0" to the ADHOC parameter for receipt of data with specified length. If ad-hoc mode is disabled, the data reception is not complete until the length of data specified at the LEN parameter has been completely received. Only then is the data available in the receive area (DATA parameter). The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.
- **ISO**‑**on**‑**TCP** **(Message-oriented data transfer)**

  Complete message blocks are sent via a connection with the protocol variant ISO‑on‑TCP; these are recognized as such by the recipient. The receive area is defined by the LEN and DATA parameters. If the receive buffer (DATA parameter) is too small for the sent data, "TRCV_C" signals an error. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

The following table shows how the received data is entered in the receive area.

| Protocol variant | Availability of data in the receive area | connection_type parameter of the connection description | Parameter LEN |
| --- | --- | --- | --- |
| TCP  (Ad-hoc mode) | If DONE is set, at least one data byte is available. | Hexadecimal value: B#16#11  Integer value: 17 | 1 up to maximum length (depending on the CPU) |
| TCP   (Receipt of data with specified length) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#11  Integer value: 17 | 1 to 8192 |
| ISO‑on‑TCP  (Message-oriented data transfer) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#12  Integer value: 18 | 1 to 8192 |
| FDL | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#15  Decimal: 21 | 1 to 240 |

#### Terminating the communication connection

The communication connection is terminated when the CONT parameter is set to "0" even if an ongoing data transfer is not complete yet. This does not apply if you are using a configured connection, however.

The connection can be reset at any time by setting the parameter COM_RST to "1". This terminates the existing communication connection and a new connection is established. If data is being transferred at this time, this can lead to data loss.

#### Parameters

The following table shows the parameters of the "TRCV_C" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L, T, C or constant | Receive enable  After the occurrence of 16#80C5 EN_R can be set to FALSE. This avoids the output of error code 16#80C4 after the client terminates the connection:  - 0: The instruction TRCV_C stops calling the instruction TRCV. Therefore, the status code 16#80C4 is not returned if the connection is not established. - 1: The instruction TRCV_C begins with calling the instruction TRCV. Therefore, the status code 16#80C4 is returned if the connection is not established. |
| CONT | Input | BOOL | I, Q, M, D, L | Controls the communication connection:  - 0: Disconnect the communication connection. - 1: Establish communication connection and maintain after receipt of data. |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Maximum length of the data to be received. If you use a receive area with optimized access at the DATA parameter, the value "0" must be used at the LEN parameter. |
| ADHOC | Input | BOOL | I, Q, M, D, L or constant | Optional parameter (hidden)  Use ad-hoc mode for the TCP protocol variant.  ADHOC must have the value FALSE if no TCP protocol is used. |
| CONNECT | InOut | VARIANT | D | Pointer to the connection description  - Programmed connection:   - For TCP or UDP, use the structure TCON_IP_v4     For a description, refer to:[Connection parameters with structure according to TCON_IP_v4](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500)   - For TCP with secure communication, use the structure TCON_IP_V4_SEC or TCON_QDN_SEC.     For a description, refer to: [Connection parameters in accordance with TCON_IP_V4_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500) or [connection parameters in accordance with TCON_QDN_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500)   - For ISO-on-TCP, use the structure TCON_IP_RFC     For a description, refer to: [Connection parameters with structure according to TCON_IP_RFC](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500)   - For ISO, use the structure TCON_ISOnative (CP 1543‑1 / CP 1545‑1)     For description, refer to instruction "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)": "Structure of the connection description according to TCON_ISOnative"   - For connections to SMS clients, use the TCON_PHONE system data type.     For a description, refer to [Connection parameters to TCON_Phone](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_phone-s7-1200-s7-1500-s7-1500t).   - For FDL connections of the CM 1542‑5, use the system data type TCON_FDL; see [Connection parameters to TCON_FDL](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_fdl-s7-1200-s7-1500). - Configured connection:   - For existing connections, use the TCON_Configured system data type. For a description, see "System data type for configured connections" below. |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the receive area.  When transferring structures, the structures must be identical at the sending and receiving end. |
| ADDR | InOut | VARIANT | D | Hidden parameter that needs to be used, however, with UDP. In this case it contains a pointer to the system data type TADDR_Param. Store the address information of the sender (IP address and port number) in a data block with the system data type TADDR_Param.  See also: [Structure of the address information of the remote partner with UDP](#addressing-the-remote-partner-via-taddr_param-s7-1200-s7-1500) |
| COM_RST | InOut | BOOL | I, Q, M, D, L | Optional parameter (hidden)  Resets the connection:  - 0: Irrelevant - 1: The existing connection is reset.   The COM_RST parameter is reset after evaluation by the "TRCV_C" instruction and should not, therefore, be interconnected statically. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Receipt not yet started or still in progress. - 1: Receipt executed without error. This state is only displayed for one cycle. |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Receipt not yet started or already completed. - 1: Receipt not yet completed. A new send job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred during connection establishment, data reception or connection termination.   The output parameter ERROR can be set due to an error in the "TRCV_C" instruction or the communication instructions used internally. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |
| RCVD_LEN | Output | UDINT | I, Q, M, D, L | Amount of data actually received in bytes |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### EN_R, CONT and COM_RST parameters

The parameter CONT controls the connection establishment of the "TRCV_C" instruction regardless of the EN_R parameter. The behavior of the CONT parameter partially depends on whether a programmed or a configured connection is used:

- With CONT = "0": No data is received (regardless of whether a programmed or a configured connection is used).
- When changing CONT = "0" to "1":

  - With a programmed connection, it is established with "TCON".
  - With a configured connection, it is checked with "T_DIAG".
- With CONT = "1":

  - As long as no data is received (EN_R ="0"), the connection is checked with "T_DIAG".
  - If the internally used communication instructions signal that no connection end point exists, the connection is automatically reestablished with "TCON".
- When changing CONT = "1" to "0":

  - With a programmed connection, it is terminated with "TDISCON".
  - With a configured connection, it is reset with "T_RESET".

The parameter COM_RST resets the connection when changing from "0" to "1":

- If a connection is established, it is reset with "T_RESET" (regardless of whether a programmed or configured connection is used).
- If no connection is established, the setting of the parameter has no effect.

The EN_R and COM_RST parameters only have an effect if CONT has been set to "1". The following table shows the relationship between the EN_R, CONT and COM_RST parameters:

| EN_R | CONT | COM_RST | Status of the instruction | Description |
| --- | --- | --- | --- | --- |
| Irrelevant | 0 | Irrelevant | Not yet executed | No job active (STATUS = 7000). |
| Irrelevant | 0 | Irrelevant | Initialization | Connection is being terminated. The instruction is being reset. |
| Irrelevant | 0 &gt; 1 | Irrelevant | Connection establishment | Connection is being established. Data is not being transferred yet. |
| 0 | 1 | 0 | Connection established | The connection is established and is monitored with the instruction "T_DIAG". |
| Irrelevant | 1 | 0 &gt; 1 | Connection established | The connection is interrupted by "T_RESET" briefly and reset. |
| 0 &gt; 1 | 1 | 0 | Connection established | Instruction starts receiving. |
| Irrelevant | 1 | 0 &gt; 1 | Data is being received | Data transfer is interrupted. The connection is being reset. |

#### System data type for configured connections

For configured connections at the CONNECT parameter, use the following structure for connection description to TCON_Configured:

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceID | HW_ANY | - | Hardware identifier of the local interface (value range: 0 to 65535). |
| 2 … 3 | ID | CONN_OUC | - | Reference to the connection (value range: 1 to 4095).  Enter the connection ID of the existing connection. |
| 4 | ConnectionType | BYTE | - | Connection type  Select 254 (decimal) for a configured connection. |

#### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set if errors occur during execution of "TRCV_C". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| DONE | BUSY | ERROR | Description |
| --- | --- | --- | --- |
| 0 | 0 | 0 | The instruction has not been executed yet (no rising edge at EN_R parameter). |
| 0 | 1 | 0 | The instruction is being executed and calls the internally used communication instructions. |
| 1 | 0 | 0 | The receipt has been completed successfully. "0000" is output at the parameter STATUS. DONE = "1" is only displayed for one cycle. |
| 0 | 0 | 1 | The execution of the instruction or an intermediate step during processing was terminated with an error. If there is a subsequent error due to an internally used communication instruction, the error that occurred first during processing is displayed. This state is only displayed for one cycle. |

#### ERROR and STATUS parameters

| ERROR | STATUS  (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Receive job executed without error. |
| 0 | 0001 | Communication connection established. |
| 0 | 0003 | Communication connection closed. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | Initial call for establishing a connection. |
| 0 | 7002 | Connection is currently being established (EN_R irrelevant):  - Passive connection establishment: Wait for connection from the remote partner - Active connection establishment: Attempt to establish a connection to a remote partner |
| 0 | 7003 | Communication connection is being terminated. |
| 0 | 7004 | Communication connection has been established and is being monitored. No receive job processing active. |
| 0 | 7006 | Communication connection has been established and is being monitored. Receive job processing active, waiting for data to be received. |
| 1 | 8085 | - The LEN parameter is larger than the highest permitted value. - The value at the LEN or DATA parameter was changed after the first call. |
| 1 | 8086 | The ID parameter is outside the permitted range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible |
| 1 | 8088 | The value at the LEN parameter does not correspond to the receive area set at the DATA parameter. |
| 1 | 8089 | - The CONNECT parameter does not point to a data block. - The CONNECT parameter does not point to a connection description. - The manually created connection description has an incorrect structure for the selected connection type. |
| 1 | 8091 | Maximum nesting depth exceeded. |
| 1 | 809A | The CONNECT parameter points to a field that does not correspond to the length of the connection description. |
| 1 | 809B | InterfaceID is invalid:  - It does not point to a local CPU interface or a CP. - If you are using the connection parameter assignment, it cannot have the value 0. - It must not have the value 0 in the used TCON_xxx structure. See [TCON: Establish communication connection](#tcon-establish-communication-connection-s7-1200-s7-1500) - TCON_QDN or TCON_QDN_SEC requires a configured DNS server. |
| 1 | 80A1 | - Connection or local port already being used by user. - Communication error:   - The specified connection has not yet been established.   - The specified connection is being terminated.     Transfer via this connection is not possible.   - The interface is being re-initialized. |
| 1 | 80A3 | The nested "T_DIAG" instruction has reported that the connection has closed. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid or it matches the IP address of the local partner. |
| 1 | 80A7 | Communication error: You called the instruction with COM_RST = 1 before the send job was complete. |
| 1 | 80AA | A connection is currently being established with the same connection ID by another block. Repeat the job with a new rising edge at the EN_R parameter. |
| 1 | 80B3 | - When using the protocol variant UDP the ADDR parameter does not contain any data. - Error in the connection description - The local port is already being used in a different connection description. |
| 1 | 80B4 | When using the protocol variant ISO on TCP (connection_type = B#16#12) for the passive establishment of a connection (active_est = FALSE) one or both of the following conditions was violated: "local_tsap_id_len &gt;= B#16#02" and/or "local_tsap_id[1] = B#16#E0". |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP. |
| 1 | 80B6 | Parameter assignment error in the connection_type parameter of the data block for connection description. |
| 1 | 80B7 | - For system data type TCON_Param:   Error in one of the following parameters of the data block for connection description: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len. - For system data types TCON_IP_V4 and TCON_IP_RFC:   IP address of the partner end point was set to 0.0.0.0. |
| 1 | 80C3 | - All connection resources are in use. - A block with this ID is already being processed in a different priority group. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is receiving new parameters or the connection is being established. - The configured connection is currently being removed by a "TDISCON" instruction. - The connection used is being terminated by a call with COM_RST = 1. |
| 1 | 80C5 | The remote partner has terminated the connection.  - When no connection is established, see also the description of STATUS 16#80C5 for [TCON](#tcon-establish-communication-connection-s7-1200-s7-1500) - When connection is established, see also the description of STATUS 16#80C5 for [TRCV](#trcv-receive-data-via-communication-connection-s7-1200-s7-1500-1) |
| 1 | 80C6 | The remote partner cannot be reached (network error). |
| 1 | 8722 | Error in the CONNECT parameter: Invalid source area (area not declared in data block). |
| 1 | 873A | Error in the CONNECT parameter: Access to connection description is not possible (no access to data block). |
| 1 | 877F | Error in the CONNECT parameter: Internal error |
| 1 | 8922 | Parameter DATA: Invalid destination area; the area does not exist in the DB. |
| 1 | 8924 | Parameter DATA: Area error in the VARIANT pointer. |
| 1 | 8932 | Parameter DATA: The DB number is too high. |
| 1 | 893A | Parameter DATA: No access to the data area, for example because the data block does not exist. |
| 1 | 897F | Parameter DATA: Internal error, e.g. invalid VARIANT reference. |
| 1 | 8A3A | Parameter ADDR: No access to the address range, for example because the data block does not exist. |

> **Note**
>
> **How to avoid the STATUS value 16#80C4 when the remote connection is interrupted.**
>
> If the connection is established and EN_R is set to TRUE, monitor the STATUS programmatically to the value 16#80C5. If 16#80C5 occurs, set input EN_R immediately to FALSE. This causes the instruction TRCV_C to terminate the call of TRCV and thus the STATUS 16#80C4 does not occur. Instead the STATUS 16#7002 is returned (while the CONT input is TRUE), until the remote device establishes the connection again. The input EN_R can be reset to TRUE, after the STATUS 16#7002 has been returned by the instruction TRCV_C. This has no effect on the operation until the connection is restored. The behavior is now the same as when the connection was first established.

> **Note**
>
> **Error messages of the instructions "TCON", "TRCV" and "TDISCON"**
>
> Internally, the "TRV_C" instruction uses the "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)", "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instructions. The error messages of these instructions are contained in the respective descriptions.

#### Example

You can find the example here: [Program example for send functions](#program-example-for-send-functions-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

## Program example for send functions (S7-1200, S7-1500)

### Introduction

In the following example, you create a programmed connection between two CPUs of the S7-1500 series and send a character string from CPU 1 to CPU 2. The character string to be sent is of the data type STRING.

### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. Their connection is not yet configured.

  ![Requirement](images/80740041611_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under Properties &gt; Protection ensures that read and write access is permitted for each CPU.

### Program of CPU 1

Create nine tags in a global data block for storing the data of "TSEND_C".

![Program of CPU 1](images/94431803787_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_TSEND_C" and create the following local tags in the FB.

![Program of CPU 1](images/94435304075_DV_resource.Stream@PNG-de-DE.png)

Network 1: Interconnect the parameters of the "TSEND_C" instruction as follows. Do not interconnect the parameter CONNECT yet.

![Program of CPU 1](images/94431824011_DV_resource.Stream@PNG-de-DE.png)

Network 2: Save the status for an error of TSEND_C as follows.

![Program of CPU 1](images/80742269323_DV_resource.Stream@PNG-de-DE.png)

**Configuration of TSEND_C**

To interconnect the parameter CONNECT, open the wizard of the "TSEND_C" instruction with Properties &gt; Configuration.

Make the following settings for the configuration of TSEND_C:

| Input field | Entry |
| --- | --- |
| End point | Select a CPU for sender and receiver using the drop-down list.   Interface, subnet and address are entered automatically. |
| Connection data | Use the drop-down list and the selection "New" to create one data block per CPU.   This data block is required for storing the connection data. The name of the data block can be freely selected.   The active connection establishment is enabled for CPU 1 (local CPU). |
| Connection type | Select the entry "TCP".   This means an Ethernet connection with the "TCP" protocol is used for connection establishment. |
| Configuration mode | Select the entry "Use program block".   This means connection establishment takes place by means of a programmed connection. |
| Connection ID | You enter a freely selected connection ID for the communication connection.   The connection ID must not already be assigned in the project. |
| Partner port | You enter a value for the partner port. The value must be &gt;=2000. |

![Program of CPU 1](images/80742363787_DV_resource.Stream@PNG-de-DE.png)

### Program of CPU 2

Create ten tags in a global data block for storing the data of "TRCV_C".

![Program of CPU 2](images/94430691851_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_TRCV_C" and create the following local tags in the FB.

![Program of CPU 2](images/94434898443_DV_resource.Stream@PNG-de-DE.png)

Network 1: Interconnect the parameters of the "TRCV_C" instruction as follows. Do not interconnect the parameter CONNECT yet.

![Program of CPU 2](images/94431800075_DV_resource.Stream@PNG-de-DE.png)

Network 2: Save the status for an error of TRCV_C as follows.

![Program of CPU 2](images/80741843339_DV_resource.Stream@PNG-de-DE.png)

**Configuration of TRCV_C**

Make the following settings for the configuration of TRCV_C:

> **Note**
>
> **Connection data**
>
> By configuring TSEND_C, you have already created a data block ("SLI_cDB_Connector") with the stored connection data for each CPU. Instead of creating new data blocks and entering the connection data, you can simply use the created data blocks ("SLI_cDB_Connector").
>
> For the created data blocks to be available for selection, they must still be available in the project tree under Program blocks &gt; System blocks.

![Program of CPU 2](images/80741937803_DV_resource.Stream@PNG-de-DE.png)

### Procedure for connection establishment

To establish the communication connection in RUN mode, follow these steps:

1. Change the EN_R parameter to "1" for TRCV_C.
2. Change the CONT parameter to "1" for TRCV_C.
3. Change the REQ parameter to "1" for TSEND_C.
4. Change the CONT parameter to "1" for TSEND_C.

### Procedure for connection termination

To terminate the communication connection in RUN mode, follow these steps:

1. Change the CONT parameter to "0" for TSEND_C.
2. Change the REQ parameter to "0" for TSEND_C.
3. Change the CONT parameter to "0" for TRCV_C.
4. Change the EN_R parameter to "0" for TRCV_C.

### Behavior of CPU 1

When the input parameter REQ ("start") returns the signal state "TRUE", the "TSEND_C" instruction is started. When the input parameter CONT ("comControl") supplies the signal state "TRUE", the "TSEND_C" instruction creates a communication connection between CPU 1 and CPU 2. To do this, the connection data is retrieved with the input parameter CONNECT (or the data block "SLI_cDB_Connector").

For multiple calls, the "TSEND_C" instruction transmits the data record detected at input parameter DATA ("sendData"). Successful transfer of the data record is indicated by the output parameter DONE ("#statDone") with the signal state "TRUE" and the output parameter STATUS ("status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status of DONE ("#statDone") in the tag "done".

After transmitting the data record to CPU 2, the communication connection continues to be monitored (status "7004"). The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 1](images/94431807499_DV_resource.Stream@PNG-de-DE.png)

### Behavior of CPU 2

When the input parameter EN_R ("start") returns the signal state "TRUE", the "TRCV_C" instruction is started. When the input parameter CONT ("comControl") supplies the signal state "TRUE", the "TRCV_C" instruction creates a communication connection between CPU 2 and CPU 1. To do this, the connection data is retrieved with the input parameter CONNECT (or the data block "SLI_cDB_Connector").

For multiple calls, the "TRCV_C" instruction receives the transmitted data record. The data record is recorded at the parameter DATA ("rcvData"). Successful transfer of the data record is indicated by the output parameter DONE ("done") with the signal state "TRUE" and the output parameter STATUS ("status") with the value "0000". The length in BYTE of the actually transmitted data record is detected with the output parameter RCVD_LEN ("#statRcvLen"). This value is only displayed during the success status. Then "0" is detected.

Because the values of the output parameters are only displayed for the moment of their validity, do the following:

- Save the value of "#statRcvLen" in "rcvLen".
- Save the value of "#statDone" in "done".
- Save the value of "#status" in "memErrStatus".

After the data record has been received by CPU 2, the communication connection continues to be monitored (status "7006"). The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing of the example is taking place without errors.

![Behavior of CPU 2](images/94431796363_DV_resource.Stream@PNG-de-DE.png)

### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

## TMAIL_C: Transfer email (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description of TMAIL_C (S7-1200, S7-1500)](#description-of-tmail_c-s7-1200-s7-1500)
- [Description TMAIL_C as of version V4.0 (S7-1200, S7-1500)](#description-tmail_c-as-of-version-v40-s7-1200-s7-1500)
- [Description of TMAIL_C as of version V5.0 (S7-1200, S7-1500)](#description-of-tmail_c-as-of-version-v50-s7-1200-s7-1500)
- [Description of TMAIL_C as of version V6.0 (S7-1200, S7-1500)](#description-of-tmail_c-as-of-version-v60-s7-1200-s7-1500)
- [TO_S and CC parameters (S7-1200, S7-1500)](#to_s-and-cc-parameters-s7-1200-s7-1500)
- [MAIL_ADDR_PARAM parameter (S7-1200, S7-1500)](#mail_addr_param-parameter-s7-1200-s7-1500)
- [Parameter MAIL_ADDR_PARAM as of Version 4.0 of TMAIL_C (S7-1200, S7-1500)](#parameter-mail_addr_param-as-of-version-40-of-tmail_c-s7-1200-s7-1500)
- [DONE, BUSY and ERROR parameters (S7-1200, S7-1500)](#done-busy-and-error-parameters-s7-1200-s7-1500)
- [STATUS parameter (S7-1200, S7-1500)](#status-parameter-s7-1200-s7-1500)
- [Example: Sending an e-mail with TMAIL_C (S7-1200, S7-1500)](#example-sending-an-e-mail-with-tmail_c-s7-1200-s7-1500)

### Description of TMAIL_C (S7-1200, S7-1500)

#### Description

You can use the "TMAIL_C" instruction to send an e-mail via the Ethernet interface of the S7-1500 CPU or S7-1200 &gt; V4.0, a communication module (CM), or a communication processor (CP).

The instruction can only be used once the hardware has been configured and if the network infrastructure allows for a communication connection to the mail server.

You define the content of the e-mail, and the connection data, using the following parameters:

- You define the recipient addresses with the parameters TO_S and CC.
- You define the content of the e-mail with the parameters SUBJECT and TEXT.
- You can define an attachment using VARIANT pointers at the ATTACHMENT and ATTACHMENT_NAME parameters.
- The connection data is defined, and addressing and authentication for the mail server executed, using the system data type TMail_V4, TMail_V6 or TMail_FQDN at the MAIL_ADDR_PARAM parameter.

  - If you are using the interface of the S7-1500 CPU, the system data type TMail_V4 must be used. In this case, the e-mail can only be sent via SMTP.
  - Any of the system data types can be used if you are using the interface of a CM/CP. The e-mail can then also be sent via SMTPS.
- You start the sending of an e-mail with an edge change from "0" to "1" for the REQ parameter.
- The job status is indicated by the output parameters "BUSY", "DONE", "ERROR" and "STATUS".

You cannot send an SMS directly with the "TMAIL_C" instruction. Whether or not the e-mail can be forwarded by the mail server as an SMS depends on your telecommunications provider.

> **Note**
>
> **Number of e-mails to be sent**
>
> You can send more than one e-mail simultaneously using a PLC. When a CP 1243‑8 IRC or CP 154x‑1 is used, you can only send one e-mail for each CP. When two CPs are used, parallel sending of two e-mails is possible.

#### Operation of the instruction

The "TMAIL_C" instruction works asynchronously, which means its execution extends over multiple calls. You must specify an instance when you call the instruction "TMAIL_C".

In the following cases, the connection to the mail server will be lost:

- If the CPU switches to STOP while "TMAIL_C" is active.
- If communication problems occur at the Industrial Ethernet bus.

In this case, the transfer of the e-mail will be interrupted and it will not reach its recipient. The connection is also canceled once the instruction has been successfully executed and the e-mail sent.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing user programs**  You can change the parts of your user program that directly affect calls of "TMAIL_C" only:  - The CPU is in "STOP" mode. - No e-mail is being sent (REQ = 0 and BUSY = 0).   This relates, in particular, to deleting and replacing program blocks that contain "TMAIL_C" calls or calls for the instance of "TMAIL_C".  Ignoring this restriction can tie up connection resources. The automation system can change to an undefined status with the TCP/IP communication functions via Industrial Ethernet.  A warm or cold restart of the CPU is required after the changes are transferred. |  |

#### Data consistency

The TO_S, CC, SUBJECT, TEXT, ATTACHMENT and MAIL_ADDR_PARAM parameters are applied by the "TMAIL_C" instruction while it is running, which means that they can only be changed after the job has been completed (BUSY = 0).

#### SMTP authentication

Authentication refers here to a procedure for verifying identity, for example, with a password query.

If you are using the S7-1500 CPU interface, the instruction "TMAIL_C" supports the SMTP authentication procedure AUTH-LOGIN which is required by most mail servers. For information about the authentication procedure of your mail server, refer to your mail server manual or the website of your Internet service provider.

- Before you can use the AUTH-LOGIN authentication procedure, the "TMAIL_C" instruction requires the user name with which it is to log on to the mail server. This user name corresponds to the user name with which you set up a mail account on your mail server. It is transferred via the UserName parameter to the structure at parameter MAIL_ADDR_PARAM.

  If no user name is specified at the MAIL_ADDR_PARAM parameter, the AUTH-LOGIN authentication procedure is not used. The e-mail is then sent without authentication.
- To log on, the "TMAIL_C" instruction also requires the associated password. This password corresponds to the password you specified when you set up your mail account. It is transferred via the PassWord parameter to the structure at parameter MAIL_ADDR_PARAM.

#### Parameters

The following table shows the parameters of the "TMAIL_C" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C or constant | Control parameter REQUEST: Activates the sending of an e-mail on a rising edge. |
| [TO_S](#to_s-and-cc-parameters-s7-1200-s7-1500) | Input | STRING | D, L or constant | Recipient addresses  STRING with a maximum length of 240 characters (bytes).   For the e-mail address format, see the example in the parameter description. |
| [CC](#to_s-and-cc-parameters-s7-1200-s7-1500) | Input | STRING | D, L or constant | CC recipient addresses (optional)  STRING with a maximum length of 240 characters (bytes).   Same e-mail address format as for the TO_S parameter. If an empty string is assigned here, the e-mail is not sent to a CC recipient. |
| SUBJECT | Input | STRING | D, L or constant | Subject of the e-mail  STRING with a maximum length of 240 characters (bytes). |
| TEXT | Input | STRING | D, L or constant | Text of the e-mail (optional)  STRING with a maximum length of 240 characters (bytes). If an empty string is assigned at this parameter, the e-mail is sent without text. |
| ATTACHMENT | Input | VARIANT | D | E-mail attachment (optional)  Reference to a byte/word/double word field (ArrayOfByte, ArrayOfWord or ArrayOfDWord) with a maximum length of 64 Kb. If no value is assigned, the e-mail is sent without an attachment. |
| ATTACHMENT_NAME | Input | STRING | D, L or constant | E-mail attachment name (optional)  Reference to a character string with a maximum length of 50 characters (bytes) to define the file name of the attachment. If an empty string is assigned at this parameter, the attachment of the e-mail is received with a file name assigned by the e-mail receiving program. It is therefore recommended to use a defined file name. |
| [MAIL_ADDR_PARAM](#mail_addr_param-parameter-s7-1200-s7-1500) | Input | VARIANT | D | Connection parameter and address of the e-mail server  To define the connection parameters, use the structure TMail_V4, TMail_V6 or TMail_FQDN (see parameter description). |
| [DONE](#done-busy-and-error-parameters-s7-1200-s7-1500) | Output | BOOL | I, Q, M, D, L | Status parameter  - DONE = 0: Job not yet started or still executing. - DONE = 1: Job executed without errors. |
| [BUSY](#done-busy-and-error-parameters-s7-1200-s7-1500) | Output | BOOL | I, Q, M, D, L | Status parameter  - BUSY = 0: Processing of "TMAIL_C" was terminated - BUSY = 1: Sending of an e-mail is not yet complete. |
| [ERROR](#done-busy-and-error-parameters-s7-1200-s7-1500) | Output | BOOL | I, Q, M, D, L | Status parameter  - ERROR = 0: No error occurred. - ERROR = 1: An error occurred during processing. STATUS supplies detailed information on the type of error. |
| [STATUS](#status-parameter-s7-1200-s7-1500) | Output | WORD | I, Q, M, D, L | Status parameter  Return value or error information of the "TMAIL_C" instruction (see parameter description). |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **Optional parameters**
>
> The optional parameters CC, TEXT, and ATTACHMENT are only sent with the e-mail if the corresponding parameters contain a string of length &gt; 0.

#### Example

You will find an example of sending e-mails with the TMAIL_C [Example: Sending an e-mail with TMAIL_C](#example-sending-an-e-mail-with-tmail_c-s7-1200-s7-1500) instruction with the following link:

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Description TMAIL_C as of version V4.0 (S7-1200, S7-1500)](#description-tmail_c-as-of-version-v40-s7-1200-s7-1500)
  
[Description of TMAIL_C as of version V5.0 (S7-1200, S7-1500)](#description-of-tmail_c-as-of-version-v50-s7-1200-s7-1500)

### Description TMAIL_C as of version V4.0 (S7-1200, S7-1500)

#### Introduction

The instruction TMAIL_C as of version V4.0 is described below. This description does not include all details, but instead explains the differences as compared to the instruction versions &lt; V4.0.

The handling of the required certificates is also not described here.

#### CPs using Secure Communication

The following CPs send secure e-mails via the instruction TMAIL_C as of version V4.0:

- CP 1543‑1 ‑ V2.0
- CP 1545‑1
- CP 1542SP‑1 IRC ‑ V1.0, CP 1543SP‑1 ‑ V1.0
- CP 1243‑1 ‑ V2.1
- CP 1242‑7 GPRS V2 ‑ V2.1
- CP 1243‑7 LTE ‑ V2.1
- CP 1243‑8 IRC ‑ V2.1

You set the data to be sent and the TCP port of the e-mail server at the parameter MAIL_ADDR_PARAM of the following system data types:

TMAIL_V4_SEC, TMAIL_V6_SEC, TMAIL_QDN_SEC

> **Note**
>
> **Compatibility with the TMAIL_C versions &lt; V4.0**
>
> For reasons of compatibility, you can also use the existing system data types TMAIL_V4, TMAIL_V6 and TMAIL_FQDN as follows:
>
> - CPUs:
>
>   TMAIL_V4, TMAIL_FQDN
> - All CPs mentioned above and CP 1542SP‑1:
>
>   TMAIL_V4, TMAIL_V6, TMAIL_FQDN

#### Rules for CPs

Observe the following rules:

- You must use only one CP as an e-mail client for each TMAIL_C instance of a CPU.
- The e-mail servers of the CPs (e-mail clients) have to be accessible from an IP network.
- If an e-mail server is to be reached via its fully qualified domain name, the DNS servers, which are configured in the CP, must also be reachable in the IP network.

#### Parameters

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ... |  |  |  |  |
| [MAIL_ADDR_PARAM](#parameter-mail_addr_param-as-of-version-40-of-tmail_c-s7-1200-s7-1500) | Input | VARIANT | D | The data required for the send process (including the connection parameters, the address of the e-mail server and the TCP port used)  Select one of the following system data types for this:  - TMail_V4_SEC - TMail_V6_SEC - TMail_QDN_SEC |
| ... |  |  |  |  |

#### Diagnostic options when an error occurs

You have the following two diagnostic options when an error occurs:

- Evaluation of the STATUS parameter

  The same values can occur as with the instruction-versions &lt; V4.0.

  Only the value W#16#8015 receives an extension. See [STATUS parameter](#status-parameter-s7-1200-s7-1500)
- Evaluation of the MS_STATUS tag in the instance data of TMAIL_C. This tag has been added in the version V4.0 of TMAIL_C. It contains both the protocol codes and their corresponding textual descriptions. The protocol codes are defined in RFC 5321 "Simple Mail Transfer Protocol". You can also find the associated textual descriptions there, in the corresponding expansions or on other media.

  Examples of diagnostic information in MS_STATUS:

  - 550 SMTP AUTH required before submission
  - 550 StartTLS required
  - 550 Requested action not taken
  - 550 A valid address is required.

---

**See also**

[Secure OUC via e-mail (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-via-e-mail-s7-1500-s7-1500t)

### Description of TMAIL_C as of version V5.0 (S7-1200, S7-1500)

#### Introduction

The instruction TMAIL_C as of version V5.0 is described below. This description does not include all details, explaining only the differences as compared to the instruction versions &lt; V5.0.

#### Description

As of version V5.0 of the TMAIL_C instruction, the ATTACHMENT parameter supports additional data types.

As of version V5.0, you can use the instruction TMAIL_C to send an e-mail as well with Secure Communication over an integrated Ethernet port of your S7-1500 CPU. This is only possible if your S7-1500 CPU has at least firmware version V2.5. The data required for the sending process is defined with one of the system data types TMAIL_V4_SEC or TMAIL_QDN_SEC at the MAIL_ADDR_PARAM parameter.

If you use the system data type TMAIL_V4, e-mails can only be sent unsecured over an integrated Ethernet port of your S7-1500 CPU.

The system data types TMAIL_FQDN and TMAIL_V6 are not supported for sending e-mails over an integrated S7-1500 CPU Ethernet port.

> **Note**
>
> **S7-1500 Software Controller**
>
> You cannot use the system data types TMAIL_V4_SEC or TMAIL_QDN_SEC with an S7-1500 Software Controller over ID=59.

#### ATTACHMENT parameter

As of instruction version V5.0 of TMAIL_C, the ATTACHMENT parameter also supports the following data types: ARRAY of CHAR, ARRAY of LWORD (only with S7-1500 CPUs) and STRING (note: An empty string at the ATTACHMENT parameter causes the e-mail to be sent without an attachment).

This also affects the value W#16#8016 of STATUS: This value is no longer output when using the data types ARRAY of CHAR, ARRAY of LWORD (only for S7-1500 CPUs) and STRING as of instruction version V5.0.

#### Additional return value at the STATUS parameter

With version V5.0 of TMAIL_C instructions, the following return value is also output at the [Parameter STATUS](#status-parameter-s7-1200-s7-1500) parameter:

| STATUS (W#16#...) | Explanation | Notes |
| --- | --- | --- |
| 8009 | Internal function error | An internal function has returned an error. You can find detailed information in the SFB_STATUS parameter of the instance DB. Its possible values are described below. |

The following table shows the possible values at the SFB_STATUS parameter of the instance DB:

| Parameter  SFB_STATUS  of the instance DB (W#16#...) | Explanation |
| --- | --- |
| 8080 | Evaluate the Status parameter of the T_MAIL sub-instance:  - 8080_04xx: Temporarily negative replies from SMTP server. Try again. Details can be found with RFC 5321. - 8080_05xx: Permanently negative replies from SMTP server. Details can be found with RFC 5321. |
| 8085 | The connection ID (ID parameter) is already being used by a configured connection. |
| 8086 | The ID parameter is outside the valid range. |
| 8087 | Maximum number of connections reached; no additional connection possible |
| 8090 | WatchDog time must be &gt;= zero. |
| 8092 | The TO_S and CC parameters are empty or the sub-parameter From is empty or incomplete. |
| 8093 | The MAIL_ADDR_PARAM parameter requires the connection to be upgraded to a secure connection, but the mail server does not support the STARTTLS command. |
| 8095 | Invalid response from mail server. The mail server might not be RFC-compliant. |
| 809A | The SDT structure at the MAIL_ADDR_PARAM parameter is not supported at an integrated interface. |
| 809B | Invalid interface ID in SDT at MAIL_ADDR_PARAM. |
| 80A1 | The specified connection or the remote port is already being used. |
| 80A3 | ID is used by a connection created by the user program. |
| 80A4 | IP address of the remote endpoint of the connection is invalid or it corresponds to the IP address of the local partner. |
| 80A7 | Communication error: You executed TDISCON before TMAIL_C had completed. |
| 80B7 | Remote port is 0 or IP address of the partner endpoint was set to 0.0.0.0. |
| 80C3 | Too few resources in the CPU |
| 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is currently receiving new parameters. - The configured connection is currently being removed by a TDISCON instruction. |
| 80C5 | The mail server refuses to establish the connection, has terminated the connection or is actively ending it. |
| 80C6 | The connection partner cannot be reached (network error). |
| 80C7 | Execution timeout |
| 80C8 | Attempt being made to re-establish an existing connection. |
| 80C9 | Validation of the connection partner failed. The mail server does not correspond to the defined partner at Parameter MailServerAddress. |
| 80CE | The IP address of the local interface is 0.0.0.0. |
| 80D0 | The MailServerAddress parameter contains an empty string in the attempt to use DNS. |
| 80D1 | The MailServerAddress parameter is not a fully qualified domain name. The dot at the end might be missing. |
| 80D2 | No DNS server address is configured. |
| 80D3 | The fully qualified domain name could not be resolved. Possible causes:  - The DNS- server cannot be reached, for example because it has been shut down or the remote port cannot be reached. - An error occurred during communication with the DNS- server. - The DNS server returned a valid DNS response, but the response contained no IPv4 address. |
| 80E0 | Communication with the mail server failed due to a message with errors. Possible causes:  - Invalid message authentication code - Message decoding failed. - Error decompressing a message - Internal capacity overflow |
| 80E1 | Error during the handshake. Possible causes:  - Abort by the user - Security not high enough - Renewed negotiation is not supported - SSL/TLS version is not supported. - Decryption error |
| 80E2 | Certificate not supported / invalid  Possible cause: The time-of-day of the module concerned is not set or the module is not synchronized.  Example: The default setting for the date of the module is 1 January 2012 and it was not set during commissioning. The validity period of the certificate starts on 20 August 2016 and ends on 20 August 2024. In this case, the date of the module is outside the validity period of the certificate; the certificate is invalid for the module. |
| 80E3 | Mail server certificate has been discarded. |
| 80E4 | No valid certification authority found for the mail server certificate. |
| 80E5 | Mail server certificate expired. |
| 80E6 | Integrity errors in the Transport-Layer-Security protocol |
| 80E7 | Unsupported extension in mail server certificate |
| 80E9 | TLS server without server certificate is not supported |

#### Expanded value range of connection parameters InterfaceID and ID

The following applies for the connection parameters InterfaceID and ID in the SDTs TMAIL_V4_SEC and TMAIL_QDN_SEC when you send e-mails over a secure connection via an integrated port in your S7-1500 CPU:

| Parameter | Description |
| --- | --- |
| InterfaceID | Hardware identifier of the interface Value range:  - 0 (new): The operating system selects a suitable integrated port itself. - Hardware identifier of the integrated port to be used. |
| ID | Reference to the connection: Value range:  - 0 (new): The operating system selects a free connection ID from the internal range. - 1 to 4095: the connection ID to be used |

---

**See also**

[Secure OUC via e-mail (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-via-e-mail-s7-1500-s7-1500t)

### Description of TMAIL_C as of version V6.0 (S7-1200, S7-1500)

#### Introduction

The instruction TMAIL_C as of version V6.0 is described below. This description does not include all details, but instead explains the differences as compared to the instruction versions &lt; V6.0.

> **Note**
>
> **S7-1200 CPUs**
>
> As of instruction version V6.0, all expansions described in the section "Description of TMAIL_C as of version V5.0" also apply to the S7-1200 CPUs.

#### Overview

As of version V6.0 of the TMAIL_C instruction, you can send data logs, recipes and user files located on the SIMATIC memory card as e-mail attachments via an integrated interface of your CPU. If there is no SIMATIC memory card, you can use files of the CPU-internal load memory with S7-1200 CPU.

You use the TMail_FileReference system data type at the ATTACHMENT parameter. The SDT TMail_FileReference is available in TIA Portal as of V16.0, in the S7-1200 CPUs as of firmware version V4.4 and in the S7-1500 CPUs as of firmware version V2.8.

In the structures that are permissible at MAIL_ADDR_PARAM, the value null is now also permissible for the WatchDogTime parameter.

When the TMail_FileReference SDT is used, the name of the attached file is automatically assigned to the ATTACHMENT_NAME parameter.

New error information is introduced that indicates an invalid path or file name.

#### Structure of the TMail_FileReference system data type

| Parameter | Data type | Start value | Description |
| --- | --- | --- | --- |
| DirectoryPath | String[254] | "/DataLogs/" | Path of the file to be attached |
| FileName | String[254] | "datalog.csv" | File name with or without extension |

The size of the file to be sent is not limited by the TMAIL_C instruction.

#### Rules for addressing a file using the TMail_FileReference SDT

First, the rules that apply to both the DirectoryPath parameter and the FileName are given. Violating these rules causes error information to be output at the STATUS parameter.

- No parameter can be an empty string.
- No ASCII control characters (0x00 to 0x1F) can be used.
- The following characters must not be used:

  - &lt;
  - &gt;
  - :
  - "
  - / (This character is allowed in the DirectoryPath parameter as a separator.)
  - \
  - |
  - ?
  - *
- The parameter cannot end with a space or a dot.

#### DirectoryPath parameter of the TMail_FileReference SDT

When the desired path is entered in the DirectoryPath parameter of the SDT, note that you can extrapolate the root directory from the firmware logic of the PLC and do not need to know it. To address a directory correctly, the DirectoryPath parameter must begin and end with "/". Every path therefore has the form "/abcdef/".

You can also reach a directory with a greater depth than root directory + 1. In this case, the path has the form "/abc/def/", where each "/" signifies a new directory. The maximum depth including root directory is 8.

If you want to address a file in the root directory, place a single "/" in the DirectoryPath.

In addition to the rules in the previous section, it must also be noted that the use of relative paths is not permitted. This means that "../" is an invalid path name. Moreover, the use of a dot to represent the current directory is not permitted. For example, "./" is not permitted.

#### Filename parameter of the TMail_FileReference SDT

In addition to the specified rules, note that the file name is limited to 60 characters by the operating system of the PLC. If you try to enter a file name containing more than 60 characters, the TMAIL_C instruction is aborted with an error.

A file extension is possible, but not necessary.

#### Parameter WatchDogTime

Every structure that you can use at the MAIL_ADDR_PARAM parameter contains the WatchDogTime parameter. You use this parameter to define the maximum execution time for the send operation.

As of instruction version V6.0 of TMAIL_C, you can also assign the value null to this parameter. The value null means that there is no time monitoring for the execution of TMAIL_C.

As of instruction version V6.0, the value W#16#8090 can no longer occur at the SFB_STATUS parameter of the instance DB.

#### Parameter ATTACHMENT_NAME

At the ATTACHMENT_NAME parameter, you can define the name under which the e-mail attachment appears when the recipient receives the e-mail.

When TMail_FileReference is used, its FileName parameter is automatically assigned to the ATTACHMENT_NAME parameter. In this case, therefore, do not assign a value to the ATTACHMENT_NAME parameter. Otherwise, the TMAIL_C instruction will generate an error.

#### New error codes

As of version V6.0 of the TMAIL_C, there are also the following return values at the STATUS parameter of TMAIL_C or at the SFB_STATUS parameter of the instance DB:

| STATUS parameter of TMAIL_C or SFB_STATUS parameter of the instance DB (W#16#...) | Explanation |
| --- | --- |
| 8088 | The file does not exist or is currently unavailable. |
| 8089 | The file cannot be opened because the maximum number of simultaneously open files has already been reached (59 with S7-1500 CPUs and 26 with S7-1200 CPUs). |
| 808A | The DirectoryPath parameter contains an invalid string or is empty. |
| 808B | The FileName parameter contains an invalid string or is empty. |
| 808C | The ATTACHMENT_NAME parameter must be empty if you are using TMail_FileReference. |

### TO_S and CC parameters (S7-1200, S7-1500)

#### Description

The TO_S and CC parameters are strings, for example, with the following content:

- &lt;wenna@mydomain.com&gt;, &lt;ruby@mydomain.com&gt;
- &lt;admin@mydomain.com&gt;, &lt;judy@mydomain.com&gt;

Note the following rules when entering the parameters:

- For OUC versions &lt;V6.0 (S7-1500) or &lt;V7.0 (S7-1200), it is recommended to enter a space and "&lt;" before each address. In all other application versions "&lt;" is optional.
- For OUC versions &lt;V6.0 (S7-1500) or &lt;V7.0 (S7-1200), it is recommended to enter a space and "&gt;" after each address. In all other application versions "&gt;" is optional.
- A comma must be entered between the addresses in TO_S and CC.

For runtime and memory space reasons, the "TMAIL_C" instruction does not perform a syntax check of parameter TO_S or CC.

### MAIL_ADDR_PARAM parameter (S7-1200, S7-1500)

#### Description

At the MAIL_ADDR_PARAM parameter, you define the connection for sending the e-mail in the structure TMail_V4, TMail_V6 or Tmail_FQDN, and save the e-mail server address and login details.

The structure you use at the MAIL_ADDR_PARAM parameter depends on the format in which the e-mail server is to be addressed:

- TMail_V4: Addressing by IP address to IPv4.
- TMail_V6: Addressing by IP address to IPv6.
- TMail_FQDN: Addressing by fully qualified domain name (FQDN).

Which structure you can use depends on the interface addressed at the InterfaceId parameter:

- If you want to use the "TMAIL_C" instruction with the internal interface, the TMail_V4 structure must be used at the MAIL_ADDR_PARAM parameter.
- If you are using a communication processor (CP) or communication module (CM), you can use all three addressing options (IPv4, IPv6 and FQDN).

**TMail_V4**
**: Addressing the mail server by IP address (IPv4)**

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_V4 |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#20 as the connection type for IPv4. |  |
| ActiveEstablished |  | BOOL | Status bit. Set to "1" once the connection is established. |  |
| CertIndex |  | BYTE | - =0: SMTP used (**S**imple **M**ail **T**ransfer **P**rotocol). SMTP must be used if the e-mail is being sent via the interface of an S7-1500 CPU. - ≠0: SMTPS used to secure the connection before it is established (with CPs/CMs). |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WATCH_DOG_TIME parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerAddress |  | IP_V4 | IP address of the mail server. IPv4 in the following format: XXX.XXX.XXX.XXX (decimal).   Example: 192.142.131.237. |  |
| UserName |  | STRING[254] | Mail server login name |  |
| PassWord |  | STRING[254] | Mail server password |  |
| From |  | EMAIL_ADDR | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
| FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |  |  |

**TMail_V6**
**: Addressing the mail server by IP address to IPv6**

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_V6 |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#21 as the connection type for IPv6. |  |
| ActiveEstablished |  | BOOL | Status bit. Set to "1" once the connection is established. |  |
| CertIndex |  | BYTE | - =0: SMTP used (**S**imple **M**ail **T**ransfer **P**rotocol). SMTP must be used if the e-mail is being sent via the interface of an S7-1500 CPU. - ≠0: SMTPS used to secure the connection before it is established (with CPs/CMs). You use the CertIndex parameter to specify the certificate to be used (see "Project navigation" &gt; "Global security settings" &gt; "Certificate manager"). |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WATCH_DOG_TIME parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerAddress |  | IP_V6 | IP address of the mail server (IPv6) in the following format: XXXX.XXXX.XXXX.XXXX.XXXX.XXXX.XXXX.XXXX (hexadecimal).   The address is divided into 8 blocks of 2 bytes each (16 bytes in total).   Example: 2001:db8:1f11:08d3:290:27ff:0370:2093 |  |
| UserName |  | STRING[254] | Mail server login name |  |
| PassWord |  | STRING[254] | Mail server password |  |
| From |  | EMAIL_ADDR | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
| FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |  |  |

**TMail_FQDN**
**: Addressing the mail server via the** 
**FQDN**

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_FQDN |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#22 as the connection type for FQDN. |  |
| ActiveEstablished |  | BOOL | Status bit. Set to "1" once the connection is established. |  |
| CertIndex |  | BYTE | - =0: SMTP used (**S**imple **M**ail **T**ransfer **P**rotocol). SMTP must be used if the e-mail is being sent via the interface of an S7-1500 CPU. - ≠0: SMTPS used to secure the connection before it is established (with CPs/CMs). You use the CertIndex parameter to specify the certificate to be used (see "Project navigation" &gt; "Global security settings" &gt; "Certificate manager"). |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WATCH_DOG_TIME parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerAddress |  | STRING[254] | FQDN (**F**ully **Q**ualified **D**omain **N**ame) of the mail server. The mail server is addressed using the fully qualified domain name.   Example: "www.mymailserver.com." |  |
| UserName |  | STRING[254] | Mail server login name |  |
| PassWord |  | STRING[254] | Mail server password |  |
| From |  | Struct | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
| FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |  |  |

### Parameter MAIL_ADDR_PARAM as of Version 4.0 of TMAIL_C (S7-1200, S7-1500)

#### Description

You use the MAIL_ADDR_PARAM parameter to specify the data required for the send process, for example the connection parameters, the address of the email server and the TCP port used.

Depending on the format in which the e-mail server is to be addressed, you use one of the following structures at the MAIL_ADDR_PARAM parameter:

- TMail_V4_SEC: Addressing via the IP address in IPv4 format
- TMail_V6_SEC: Addressing via the IP address in IPv6 format
- TMail_QDN_SEC: Addressing via the fully qualified host name (FQDN)

#### TMail_V4_SEC: Addressing of the mail server via the IP address in IPv4 format

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_V4_SEC |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the Ethernet interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#20 as the connection type for IPv4. |  |
| ActiveEstablishment |  | BOOL | Active/passive connection establishment. Because the CP is always the SMTP client, this parameter must be set to "1". |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WatchDogTime parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerAddress |  | IP_V4 | IP address of the mail server intrinsic in IPv4 format: XXX.XXX.XXX.XXX (decimal place).   Example: 192.142.131.237. |  |
| UserName |  | STRING[254] | User name.  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| PassWord |  | STRING[254] | User password.  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| From |  | EMAIL_ADDR | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
|  |  | FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |
|  | RemotePort |  | UINT | TCP port of the mail server |
| ActivateSecureConn |  | BOOL | - 1: Secure SMTP connection - 0: SMTP connection (non-secure). In this case, the following parameters are irrelevant. |  |
| ExtTLSCapabilities |  | BYTE | Not currently used |  |
| TLSServerCertRef |  | UDINT | Reference to the X.509 V3 (CA) certificate of the mail server, which is used by the TLS client to validate the authentication of the TLS server. |  |

#### TMail_V6_SEC: Addressing of the e-mail server via the IP address in IPv6 format

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_V6_SEC |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the Ethernet interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#21 as the connection type for IPv6. |  |
| ActiveEstablishment |  | BOOL | Active/passive connection establishment. Because the CP is always the SMTP client, this parameter must be set to "1". |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WatchDogTime parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerAddress |  | IP_V6 | IP address of the mail server in IPv6 format: XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX (hexadecimal). The address is divided into 8 blocks of 2 bytes each (16 bytes in total).  Example: 2001:db8:1f11:08d3:290:27ff:0370:2093 |  |
| UserName |  | STRING[254] | User name.  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| PassWord |  | STRING[254] | User password.  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| From |  | EMAIL_ADDR | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
|  |  | FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |
|  | RemotePort |  | UINT | TCP port of the mail server |
| ActivateSecureConn |  | BOOL | - 1: Secure SMTP connection - 0: SMTP connection (non-secure). In this case, the following parameters are irrelevant. |  |
| ExtTLSCapabilities |  | BYTE | Not currently used |  |
| TLSServerCertRef |  | UDINT | Reference to the X.509 V3 (CA) certificate of the mail server, which is used by the TLS client to validate the authentication of the TLS server. |  |

#### TMail_QDN_SEC: Addressing of the mail server via FQDN

| Parameter |  |  | Data type | Description |
| --- | --- | --- | --- | --- |
| TMail_QDN_SEC |  |  | Struct |  |
|  | InterfaceId |  | LADDR | Hardware identifier of the Ethernet interface |
| ID |  | CONN_OUC | Connection ID |  |
| ConnectionType |  | BYTE | Connection type. Select 16#22 as the connection type for FQDN. |  |
| ActiveEstablishment |  | BOOL | Active/passive connection establishment. Because the S7-CP is always the SMTP client, this parameter must be set to "1". |  |
| WatchDogTime |  | TIME | Execution watchdog. Use this parameter to define the maximum execution time for the send operation.  Note: Connection establishment can take longer (approx. one minute) if the connection is slow. When you specify the WatchDogTime parameter, remember to allow for the time required to establish the connection.  The connection is terminated once the specified time has elapsed. |  |
| MailServerQDN |  | STRING[254] | FQDN (Fully Qualified Domain Name) of the mail server. The mail server is addressed using the fully qualified domain name, which must be end with "."  Example: "www.mymailserver.com." |  |
| UserName |  | STRING[254] | User name  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| PassWord |  | STRING[254] | User password  This is required if users wants to access their email inbox in order to identify themselves as the owner of the email inbox to the email provider. |  |
| From |  | EMAIL_ADDR | E-mail sender address, which is defined using the following two STRING parameters. For example: "myname@mymailserver.com". |  |
|  |  | LocalPartPlusAtSign | STRING[64] | Local part of sender address, including @ sign. Example: "myname@" |
|  |  | FullQualifiedDomainName | STRING[254] | Fully Qualified Domain Name (abbreviated to FQDN) of the mail server. Example: "mymailserver.com" |
|  | RemotePort |  | UINT | TCP port of the mail server |
| ActivateSecureConn |  | BOOL | - 1: Secure SMTP connection - 0: Unsecured SMTP connection In this case, the following parameters are irrelevant. |  |
| ExtTLSCapabilities |  | BYTE | Not currently used |  |
| TLSServerCertRef |  | UDINT | Reference to the X.509 V3 (CA) certificate of the mail server, which is used by the TLS client to validate the authentication of the TLS server. |  |

---

**See also**

[Secure OUC via e-mail (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-via-e-mail-s7-1500-s7-1500t)

### DONE, BUSY and ERROR parameters (S7-1200, S7-1500)

#### Description

The output parameters DONE, BUSY and ERROR are each displayed for only one cycle if the status of the BUSY output parameter changes from "1" to "0".

The following table shows the relationship between DONE, BUSY, and ERROR. Using this table, you can determine the current status of the instruction "TMAIL_C and when the sending of the e-mail is complete.

| DONE | BUSY | ERROR | Description |
| --- | --- | --- | --- |
| 0 | 1 | 0 | The job is being processed. |
| 1 | 0 | 0 | Job successfully completed. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error can be found in the [STATUS](#status-parameter-s7-1200-s7-1500) parameter. |
| 0 | 0 | 0 | The "TMAIL_C" instruction was not assigned a (new) job. |

### STATUS parameter (S7-1200, S7-1500)

#### Description

The following table shows the return values of "TMAIL_C" at the STATUS parameter:

| Return value  STATUS*  (W#16#...): | Explanation | Notes |
| --- | --- | --- |
| 0000 | The processing of "TMAIL_C" was completed without errors. | Error-free completion of "TMAIL_C" does not mean that the e-mail sent will necessarily arrive.   An incorrect entry of the recipient addresses does not generate a status error of the "TMAIL_C" instruction. In this case, there is no guarantee that the e-mail will be sent to other recipients, even if these were entered correctly. |
| 7001 | "TMAIL_C" is active (BUSY = 1). | First call: Job triggered. |
| 7002 | "TMAIL_C" is active (BUSY = 1). | Intermediate call: Job already active. |
| 80xx | The processing of "TMAIL_C" was completed with an error code of the internally called communication instructions. | For detailed information, refer to the STATUS parameter descriptions for the "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)", "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)", "[TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)" and "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)" communication instructions. |
| 8010 | Error during connection establishment | You can find further information on evaluation in the SFB_STATUS parameter of the instance data block. The error code displayed at the SFB_STATUS parameter is explained in the STATUS parameter description for the "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)" instruction. |
| 8011 | Error sending the data | You can find further information on evaluation in the SFB_STATUS parameter of the instance data block. The error code displayed at the SFB_STATUS parameter is explained in the STATUS parameter description for the "[TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)" instruction. |
| 8012 | Error receiving the data | You can find further information on evaluation in the SFB_STATUS parameter of the instance data block. The error code displayed at the SFB_STATUS parameter is explained in the STATUS parameter description for the "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)" instruction. |
| 8013 | Error during connection establishment | You can find further information on evaluation in the SFB_STATUS parameter of the instance data block. The error code displayed at the SFB_STATUS parameter is explained in the STATUS parameter description for the "[TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instructions. |
| 8014 | Establishment of a connection is not possible. | You might have entered an incorrect mail server IP address ([MailServerAddress](#mail_addr_param-parameter-s7-1200-s7-1500)) or too short a time span ([WatchDogTime](#mail_addr_param-parameter-s7-1200-s7-1500)) for connection establishment. It is also possible that the CPU has no connection to the network or that the CPU configuration is incorrect. |
| 8015 | Incorrect data type for MAIL_ADDR_PARAM | The only valid data types are the system data types (structures) TMail_V4, TMail_V6 and TMail_FQDN.  As of instruction version V4.0, the following system data types are also valid: TMail_V4_SEC, TMail_V6_SEC and TMail_QDN_SEC |
| 8016 | Incorrect data type for the ATTACHMENT parameter | The only valid data types are ArrayOfByte, ArrayOfWord and ArrayOfDWord. |
| 8017 | Incorrect data length for the ATTACHMENT parameter | Data length must be &lt;= 65534 bytes. |
| 82xx** | The error message originates from the mail server and corresponds, except for the "8", to the error number of the SMTP protocol. | STATUS is a HEX value, but the last three digits correspond to the decimal value of the error number of the mail server or the SMTP protocol.  You can find more detailed information on the SMTP error code and other error codes in the SMTP protocol on the Internet or in the error documentation of the mail server.  For instruction versions &lt; V5.0, the following applies: You can also view the most recent error message from the mail server in your instance DB in the BUFFER1 parameter. You can find the last data sent by the "TMAIL_C" instruction under DATA in the instance DB. |
| 84xx** | The error message originates from the mail server and corresponds, except for the "8", to the error number of the SMTP protocol.  The following lines list several error codes that can occur. | STATUS is a HEX value, but the last three digits correspond to the decimal value of the error number of the mail server or the SMTP protocol.  You can find more detailed information on the SMTP error code and other error codes in the SMTP protocol on the Internet or in the error documentation of the mail server.  For instruction versions &lt; V5.0, the following applies: You can also view the most recent error message from the mail server in your instance DB in the BUFFER1 parameter. You can find the last data sent by the "TMAIL_C" instruction under DATA in the instance DB. |
| 8401 | No channels available. Possible cause: There is already an e-mail connection via the CP. A second connection cannot be established in parallel. | Specific error for CP 154x‑1 |
| 8403 | A TCP/IP connection to the mail server was not possible. | Specific error for CP 154x‑1 |
| 8405 | Server has denied login request. | Specific error for CP 154x‑1 |
| 8406 | SMTP client has detected an internal SSL error or a problem with the certificate structure. | Specific error for CP 154x‑1 |
| 8407 | Request to use SSL denied. | Specific error for CP 154x‑1 |
| 8408 | Client unable to identify socket for establishing a TCP/IP connection to the mail server. | Specific error for CP 154x‑1 |
| 8409 | Writing via the connection not possible. Possible cause: The communication partner has reset the connection or the connection has been lost. | Specific error for CP 154x‑1 |
| 8410 | Reading via the connection not possible. Possible cause: The communication partner has reset the connection or the connection has been lost. | Specific error for CP 154x‑1 |
| 8411 | E-mail could not be sent. Cause: Insufficient memory space to execute the send operation. | Specific error for CP 154x‑1 |
| 8412 | Configured DNS server was unable to resolve the specified domain name. | Specific error for CP 154x‑1 |
| 8413 | An internal error in the DNS subsystem prevented domain name resolution. | Specific error for CP 154x‑1 |
| 8414 | Empty character string entered as domain name. | Specific error for CP 154x‑1 |
| 8415 | An internal error has occurred in the cURL module. Execution was stopped. | Specific error for CP 154x‑1 |
| 8416 | An internal error has occurred in the SMTP module. Execution was stopped. | Specific error for CP 154x‑1 |
| 8417 | Request to SMTP on a channel already in use or invalid channel ID. Execution was stopped. | Specific error for CP 154x‑1 |
| 8418 | E-mail send job aborted. Possible causes: Execution time exceeded (WatchDogTime parameter) or CP transition from start to stop. | Specific error for CP 154x‑1 |
| 8419 | Channel interrupted and cannot be used before the connection is closed. | Specific error for CP 154x‑1 |
| 8420 | Server certificate string could not be verified with CP root certificate. | Specific error for CP 154x‑1 |
| 8421 | Internal error occurred. Execution was stopped. | Specific error for CP 154x‑1 |
| 8450 | Action not executed: Mailbox not available/cannot be reached | Try again later. |
| 8451 | Action aborted: Local processing error | Try again later. |
| 85xx** | The error message originates from the mail server and corresponds, except for the "8", to the error number of the SMTP protocol.  The following lines list several error codes that can occur. | STATUS is a HEX value, but the last three digits correspond to the decimal value of the error number of the mail server or the SMTP protocol.  You can find more detailed information on the SMTP error code and other error codes in the SMTP protocol on the Internet or in the error documentation of the mail server.  For instruction versions &lt; V5.0, the following applies: You can also view the most recent error message from the mail server in your instance DB in the BUFFER1 parameter. You can find the last data sent by the "TMAIL_C" instruction under DATA in the instance DB. |
| 8500 | Syntax error: Error not recognized. This also includes the error when a command string is too long. This can also occur when the e-mail server does not support the LOGIN authentication method. | Check the parameters of "TMAIL_C". Try to send an e-mail without authentication. To do this, replace the content of the UserName parameter with an empty string. If no user name is specified, the LOGIN authentication method is not used. |
| 8501 | Syntax error: Incorrect input at a parameter | Possible cause: Incorrect address at the parameters TO_S or CC (see also: [TO_S and CC parameters](#to_s-and-cc-parameters-s7-1200-s7-1500)). |
| 8502 | Command unknown or not implemented | Check your entries, in particular the FROM parameter. It might be incomplete and you might have forgotten the "@" or "." (see also: [TO_S and CC parameters](#to_s-and-cc-parameters-s7-1200-s7-1500)). |
| 8504 | Command parameters not implemented | Check your entries, in particular the FROM parameter. It might be incomplete and you might have forgotten the "@" (see also: [TO_S and CC parameters](#to_s-and-cc-parameters-s7-1200-s7-1500)). |
| 8535 | SMTP authentication incomplete | You have possibly entered an incorrect user name or incorrect password. |
| 8550 | Mail server cannot be reached. You have no access rights. | You might have entered an incorrect user name or password, or the mail server might not support your login. Another cause of error could be an incorrect entry of the domain name after the "@" or a missing "." at the TO_S, CC and FROM parameters (see also: [TO_S and CC parameters](#to_s-and-cc-parameters-s7-1200-s7-1500)). |
| 8552 | Action aborted: Assigned memory size has been exceeded | Try again later. |
| 8554 | Transfer failed | Try again later. |
| 8555 | Error due to incorrect entry of the e-mail address. | If multiple addresses were entered, these need to be separated by a comma. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also".  ** According to RFC 5321, the second, third and fourth digit in the STATUS value 8xyz has the following meaning: The second digit indicates whether the SMTP response is good, bad or incomplete (x=2 e.g. means that the SMTP response was positive). The second digit classifies the error which occurred. The third digit indicates which error has occurred within the class. |  |  |

### Example: Sending an e-mail with TMAIL_C (S7-1200, S7-1500)

#### Introduction

The following call example shows you how the TMAIL_C instruction works.

#### Requirement

- Hardware must be configured beforehand for sending e-mails.
- The infrastructure of the network must allow a communication connection to the mail server.

#### E-mail attachment

The e-mail should be sent with an attachment.

Create an Array of Byte with the name "Data" in a global data block ("SLI_gDB_MailAttach_scl") as a source for the attachment. The array will be interconnected with the ATTACHMENT input parameter at a later time.

![E-mail attachment](images/99734921739_DV_resource.Stream@PNG-de-DE.png)

#### Storage of data

You enter the connection information of the CPU and address data of the mail server in the TMail_V4. system data type

- Create a global data block ("SLI_gDB_TMAIL_C_scl").
- Create a tag "Par1" with the data type "TMail_V4" in the data block.
- In the following structure, enter the parameters of your CPU based on the configuration and the connection data of your mail server. For more information, refer to the description of the [MAIL_ADDR_PARAM](#mail_addr_param-parameter-s7-1200-s7-1500) input parameter.

The "Par1" tag will be interconnected with the MAIL_ADDR_PARAM input parameter later.

![Storage of data](images/99736248715_DV_resource.Stream@PNG-de-DE.png)

Also create the following tags in the global data block:

![Storage of data](images/99734912907_DV_resource.Stream@PNG-de-DE.png)

#### Calling the instruction

Create a new function block in the SCL language with the following interfaces:

![Calling the instruction](images/99734904075_DV_resource.Stream@PNG-de-DE.png)

Copy the following source code to the programming window with a call of TMAIL_C:

Call TMAIL_C

//Set "sendMail" to "TRUE" to start TMAIL_C.  
#TMAIL_C_Instance(REQ:="SLI_gDB_TMAIL_C_scl".sendMail AND NOT("SLI_gDB_TMAIL_C_scl".busy),  
                  TO_S:="SLI_gDB_TMAIL_C_scl".target,  
                  SUBJECT:="SLI_gDB_TMAIL_C_scl".subject,  
                  TEXT:="SLI_gDB_TMAIL_C_scl".text,  
                  ATTACHMENT:="SLI_gDB_MailAttach_scl".data,  
                  MAIL_ADDR_PARAM:="SLI_gDB_TMAIL_C_scl".par1,  
                  DONE=&gt;#done,  
                  BUSY=&gt;"SLI_gDB_TMAIL_C_scl".busy,  
                  ERROR=&gt;"SLI_gDB_TMAIL_C_scl".error,  
                  STATUS=&gt;#status);

//INFO: Saves the success status of TMAIL_C.  
IF #done THEN  
    "SLI_gDB_TMAIL_C_scl".done := TRUE;  
    "SLI_gDB_TMAIL_C_scl".sendMail := FALSE;  
END_IF;

//INFO: In case of an error, saves the error status of TMAIL_C and resets "sendMail".  
IF "SLI_gDB_TMAIL_C_scl".error THEN  
    "SLI_gDB_TMAIL_C_scl".memErrStatus := #status;  
    "SLI_gDB_TMAIL_C_scl".sendMail := FALSE;  
END_IF;

#### Result

If the "sendMail" tag returns the signal state "TRUE" (edge change from "0" to "1" at the REQ parameter), the instruction "TMAIL_C" is executed. As soon as the "#done" tag returns the signal state "TRUE", the "sendMail" tag is automatically reset to the signal state "FALSE". Success in sending the e-mail ("#done" is "TRUE") is also saved in the "done" tag.

In the event of an error in the instruction "TMAIL_C", the value of the STATUS parameter ("#status") is saved in the "memErrStatus" tag and the "sendMail" tag is reset.

---

**See also**

[Description of TMAIL_C (S7-1200, S7-1500)](#description-of-tmail_c-s7-1200-s7-1500)

## CommConfig: Reading and changing communication parameters (S7-1500)

This section contains information on the following topics:

- [Description CommConfig (S7-1500)](#description-commconfig-s7-1500)
- [UDT "Conf_Hostname" (S7-1500)](#udt-conf_hostname-s7-1500)
- [UDT "Conf_Domainname" (S7-1500)](#udt-conf_domainname-s7-1500)
- [UDT "Conf_ClientId" (S7-1500)](#udt-conf_clientid-s7-1500)
- [UDT "Conf_ClientId_Opaque" (S7-1500)](#udt-conf_clientid_opaque-s7-1500)
- [UDT "Conf_DNS" (S7-1500)](#udt-conf_dns-s7-1500)
- [UDT "Conf_DNS_IPV4" (S7-1500)](#udt-conf_dns_ipv4-s7-1500)
- [UDT "Conf_IPSuitev4" (S7-1500)](#udt-conf_ipsuitev4-s7-1500)
- [UDT "Conf_IPSuitev4_IPV4" (S7-1500)](#udt-conf_ipsuitev4_ipv4-s7-1500)
- [UDT "Conf_NTP" (S7-1500)](#udt-conf_ntp-s7-1500)

### Description CommConfig (S7-1500)

#### Description

The "CommConfig" instruction allows you to read and change the following communication parameters of your S7-1500 CPU simply:

- DNS host name
- DNS domain name
- DHCP ClientId
- DNS server addresses
- IP suite (IP address, subnet mask, default gateway or default router)
- NTP server addresses (you cannot read this communication parameter, only change it.)

> **Note**
>
> **Change of communication parameters with other instructions**
>
> You can also change communication parameters using the "T_CONFIG" instruction.
>
> The following functional differences exist compared to the "CommConfig" instruction:
>
> - Changing the PROFINET device name (NoS) is only possible with "T_CONFIG".
> - Changing the communication parameters on the CPs 154x-1 is only possible with "T_CONFIG".

#### Functional description

The "CommConfig" instruction is an asynchronous instruction. Processing extends over multiple calls. You start processing with a rising edge at the "REQ" parameter.

The parameters "Busy" and "Done" indicate the status of the job.

If an error occurs during execution, this is signaled by the parameters "Error" and "Status".

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### Parameter

The following table shows the parameters of the "CommConfig" instruction:

| Parameter | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | Bool | Control parameter Request  Activates the job on a positive edge. |
| HW_ID | Input | HW_IO | Hardware identifier of the submodule whose communication parameters are to be read or changed |
| MODE | Input | USInt | The MODE parameter is used to select which function of the "CommConfig" instruction you want to execute:  - 0: Read communication parameters from submodules and transfer them to the area referenced by DATA - 1: Transfer communication parameters that are located in the area referenced by DATA to the submodule  Note: Make sure that the structure of DATA matches the communication parameters of the submodule and that the values to be transferred to the submodule are permissible. Otherwise "CommConfig" returns an error. You must have set the adaptation of the parameter directly on the device beforehand for each configuration. - 2 to 255: Reserved |
| DONE | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still in progress. - 1: Job completed without error. This state is only displayed for one call. |
| BUSY | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started |
| ERROR | Output | Bool | Status parameter with the following values:  - 0: No error occurred. - 1: Error occurred during processing. This state is only displayed for one call. |
| STATUS | Output | Word | Return value or error information of the "CommConfig" instruction. |
| DATA | InOut | Variant | - For MODE=0: Pointer to the target range for the communication parameters to be read from the submodule - For MODE=1: Pointer to the source range of the communication parameters to be transferred to the submodule. Only certain UDTs are permitted for DATA (see below). You must select a UDT that matches HW_ID. |

You can find additional information on valid data types under [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

#### UDTs supported by "CommConfig"

"CommConfig" supports the following UDTs:

- Conf_Hostname, see [UDT "Conf_Hostname"](#udt-conf_hostname-s7-1500)
- Conf_Domainname, see [UDT "Conf_Domainname"](#udt-conf_domainname-s7-1500)
- Conf_ClientId, see [UDT "Conf_ClientId"](#udt-conf_clientid-s7-1500)
- Conf_ClientId_Opaque, see [UDT "Conf_ClientId_Opaque"](#udt-conf_clientid_opaque-s7-1500)
- Conf_DNS, see [UDT "Conf_DNS"](#udt-conf_dns-s7-1500)
- Conf_DNS_IPV4, see [UDT "Conf_DNS_IPV4"](#udt-conf_dns_ipv4-s7-1500)
- Conf_IPSuitev4, see [UDT "Conf_IPSuitev4"](#udt-conf_ipsuitev4-s7-1500)
- Conf_IPSuitev4_IPV4, see [UDT "Conf_IPSuitev4_IPV4"](#udt-conf_ipsuitev4_ipv4-s7-1500)
- Conf_NTP, see [UDT "Conf_NTP"](#udt-conf_ntp-s7-1500)

#### Relation between UDTs and valid values of HW_ID

The following table describes which values of HW_ID are permissible for the individual UDTs.

| UDT | Valid types for HW_ID | Possible values for HW_ID |
| --- | --- | --- |
| Conf_Hostname | HW_SubModule | Local~Common |
| Conf_Domainname | HW_SubModule | Local~Common |
| Conf_ClientId | HW_Interface | e.g. Local~PROFINET_interface_2 |
| Conf_ClientId_Opaque | HW_Interface | e.g. Local~PROFINET_interface_2 |
| Conf_DNS | HW_SubModule | Local~Common |
| Conf_DNS_IPV4 | HW_SubModule | Local~Common |
| Conf_IPSuitev4 | HW_Interface | e.g. Local~PROFINET_interface_2 |
| Conf_IPSuitev4_IPV4 | HW_Interface | e.g. Local~PROFINET_interface_2 |
| Conf_NTP | HW_Interface | Local~Common |

#### STATUS parameter

| STATUS (W#16#...) | Explanation |
| --- | --- |
| 0000 | "CommConfig" was completed without errors. |
| 7000 | No job processing active. |
| 7001 | Start of job execution |
| 7002 | Intermediate call (REQ  irrelevant): |
| 8089 | DATA does not point to a valid data type.  Note: "CommConfig" only supports the UDTs provided in the CommConfig library. |
| 8090 | Invalid parameter HW_ID  Possible causes:  - The value of HW_ID does not correspond to a real object in the CPU. - The object referenced by HW_ID is not a hardware identifier of a submodule |
| 8091 | Invalid configuration  Possible causes:  - You want to write the IP suite with the UDT "Conf_IPSuitev4" or the UDT "Conf_IPSuitev4_IPV4", but "IP address is set directly at the device" is not selected. - You want to write the NTP server addresses using the UDT "Conf_NTP", but "Time synchronization with NTP server" is not selected. |
| 8093 | Invalid value of MODE |
| 8094 | Invalid value in the UDT referenced by DATA  Possible causes:  - The "Count" parameter in UDT "Conf_DNS" contains a value &gt; 4. - An element of the field "DNS_Server in UDT "Conf_DNS" does not have the correct format of an IPv4 IP address. - The "Count" parameter in the UDT "Conf_DNS_IPV4" contains a value &gt; 4. - The "write_mode" parameter in the UDT "Conf_IPSuitev4" does not have the value 1 (permanent) or 2 (temporary), but the "MODE" parameter has the value 1 (write). - The "IPAddress" parameter in the UDT "Conf_IPSuite v4" does not have the correct format of an IPv4 address. - The parameter "SubnetMaskPrefix" in the UDT "Conf_IPSuitev4" is outside the range 4 - 30. - The "Gateway" parameter in the UDT "Conf_IPSuitev4" does not have the correct format of an IPv4 address. - The "write_mode" parameter in the UDT "Conf_IPSuitev4_IPV4" does not have the value 1 (permanent) or 2 (temporary), but the "MODE" parameter has the value 1 (write). - The "Count" parameter in the "Conf_NTP" UDT contains a value &gt; 4. - One of the elements of the field "NTP_Server" in the UDT "Conf_NTP" does not have the correct format of an IPv4 address. - When using the UDT "ConfClientId", you have used a string of length 1. - When using the UDT ConfClientId", you have used a character outside the range 0x21 to 0x7E. - When using the UDT you have used "Conf_ClientId_Opaque" for the value of length "1". |
| 80A0 | Error when reading the communication parameters |
| 80A1 | Error when writing the communication parameters |
| 80A9 | This function is not supported.  Possible causes:  - The function specified in MODE is not supported for the UDT specified by DATA. - The target device does not support this function.   Note: The UDT "Conf_NTP" does not support MODE=0. |
| 80AA | The combination of host name and domain name (including delimiters) exceeds the maximum length of 254 characters. |
| 80AB | Invalid name  Possible causes:  - You tried to change the communication parameter "DNS hostname" with "CommConfig". The new name contains an illegal character. - You tried to change the communication parameter "DNS domain name" with "CommConfig". The new name contains an illegal character. - The domain name has a name part (label) of inadmissible length. |
| 80AC | The sum of the lengths of the host name, domain name and ClientId exceeds the limit of 260 characters. |
| 80AD | Error when writing the ClientId: The memory card is full or write-protected |
| 80B0 | Invalid index  Possible cause:  - The addressed submodule (HW_ID) does not have the communication parameters specified via DATA. See section "Relation between UDTs and valid values of HW_ID". |
| 80B6 | Access error  Possible cause:  - Due to the current configuration, no read or write access to the UDT referenced by DATA is possible. |
| 80B7 | Invalid range  Possible cause:  - A value of the data record read by the CPU does not match the format of the UDT referenced by DATA. |
| 80B8 | Invalid parameters  Possible cause:  - Invalid value when writing the communication parameters |
| 80C2 | Resource is currently in use |
| 80C3 | Resource not available |

#### Maximum number of simultaneously active jobs

The maximum number of simultaneously active jobs is determined by the following rules:

- At any given time only one write operation of the UDTs "Conf_IPSuitev4", "Conf_IPSuitev4_IPV4" or "Conf_NTP" can be active.
- Writing one of the UDTs "Conf_IPSuitev4", "Conf_IPSuitev4_IPV4" or "Conf_NTP" can be combined with writing any other UDT. The number of simultaneous write requests of the other UDTs is limited to 20.
- The maximum number of simultaneous read jobs of any UDTs is 20.

If you do not comply with these rules, CommConfig returns either error code 0x80C2 or error code 0x80C3.

---

**See also**

[Assigning addresses via DHCP (S7-1500)](Configuring%20devices%20and%20networks.md#assigning-addresses-via-dhcp-s7-1500)
  
[T_CONFIG: Configure interface (S7-1200, S7-1500)](#t_config-configure-interface-s7-1200-s7-1500)

### UDT "Conf_Hostname" (S7-1500)

#### UDT "Conf_Hostname"

The UDT "Conf_Hostname" is used to read or change the "DNS Hostname" communication parameter. The host name can be combined with the domain name to form a Fully Qualified Domain Name (FQDN).

The UDT "Conf_Hostname is structured as follows:

| Parameter | Data type |
| --- | --- |
| Host name | String[63] |

The permissible characters are the same as in RFC 1035: A, … Z, a, … z, 0, … 9, hyphen. The length is limited to 63 characters. Host name must begin and end with a letter or digit. The combination of host name and domain name must not exceed 254 characters (including delimiters) and must form an FQDN. The last delimiter is not necessary because root-label is always empty. The sum of the lengths of the host name, domain name and ClientId must not exceed 260 characters.

If you use the UDT "Conf_Hostname", you have to select a value of the type "HW_SubModule" for HW_ID.

> **Note**
>
> **Validity of data obtained via DHCP**
>
> If you change the host name with "CommConfig", all data obtained via DHCP (IP Suite, domain name, NTP server, DNS server) will be invalid and will be obtained again from the DHCP server. Therefore, you should only change the host name in urgent cases and not during operation.
>
> All connections can be dropped if the IP address of the interface changes.

---

**See also**

[Assigning addresses via DHCP (S7-1500)](Configuring%20devices%20and%20networks.md#assigning-addresses-via-dhcp-s7-1500)

### UDT "Conf_Domainname"  (S7-1500)

#### UDT "Conf_Domainname"

The UDT "Conf_Domainname" is used to read or change the "DNS domain name" communication parameter. The domain consists of the top-level domain and one or more subdomains. The domain name can be combined with the host name to form a Fully Qualified Domain Name (FQDN).

The UDT "Conf_Domainname" is structured as follows:

| Parameter | Data type |
| --- | --- |
| Domain name | String[252] |

The maximum length is 252 characters. The combination of host name and domain name must not exceed 254 characters (including delimiters) and must form an FQDN. The last delimiter is not necessary because root-label is always empty. The sum of the lengths of the host name, domain name and ClientId must not exceed 260 characters.

If you use the UDT "Conf_Domainname", you have to select a value of the type "HW_SubModule" for HW_ID.

The permissible characters can be found in RFC1035 and RFC1123.

> **Note**
>
> **Validity of data obtained via DHCP**
>
> If you change the domain name with "CommConfig", all data obtained via DHCP will be invalid: IP Suite, domain name, NTP server, DNS server. Therefore, you should only change the domain name in urgent cases and not during operation.
>
> All connections can be dropped if the IP address of the interface changes.

---

**See also**

[Assigning addresses via DHCP (S7-1500)](Configuring%20devices%20and%20networks.md#assigning-addresses-via-dhcp-s7-1500)

### UDT "Conf_ClientId" (S7-1500)

#### UDT "Conf_ClientId"

The UDT "Conf_ClientId" is used to read or change the "DHCP ClientId" communication parameter . It can be parameterized individually for each interface with DHCP.

The UDT "Conf_ClientId" is structured as follows:

| Parameter | Data type |
| --- | --- |
| ClientId | String[254] |

The sum of the lengths of the host name, domain name and ClientId must not exceed 260 characters. The combination of host name and domain name must not exceed 254 characters (including delimiters) and must form an FQDN. The last delimiter is not necessary because root-label is always empty.

If you use the UDT "Conf_ClientId", you have to select a value of the type "HW_Interface" for HW_ID.

For "ClientId", only ASCII characters with a value between 0x21 and 0x7E are permitted. If you violate this rule, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).

The length of "ClientId" must be 0 or have a value between 2 and 254. A string of length 1 results in the error 0x8094.

If you enter a string of length 0 (empty string), "CommConfig" writes an empty ClientId in the data record for DHCP parameters. If the ClientId is empty, the DHCP client identifies itself with the MAC address on the DHCP server.

If you enter a string with a length of 2 to 254, a distinction is made between the following two cases:

- The string begins with the escape sequence "\0". In this case "CommConfig" removes the escape sequence from the string and replaces it with 0x00.
- The string does not begin with the escape sequence "\0". In this case the string is copied unchanged into the data record for DHCP parameters.

The communication parameter "DHCP ClientId" applies accordingly during reading: If the first byte read has the value 0x00, it is replaced by "\0". During reading, there is no check whether the read characters are permitted. Therefore, not all read characters can be displayed correctly. If the ClientId read does not fit into the field "ClientId" of the UDT "Conf_ClientId", error 0x80B7 is output (invalid range).

> **Note**
>
> **Validity of data obtained via DHCP**
>
> If you change ClientId with "CommConfig", all data obtained via DHCP will be invalid: IP Suite, domain name, NTP server, DNS server. Therefore, you should only change ClientId in urgent cases and not during operation.
>
> All connections can be dropped if the IP address of the interface changes.

> **Note**
>
> **Writing the ClientId**
>
> The ClientId can only be written with "CommConfig" if DHCP is configured to use the ClientId.

---

**See also**

[Assigning addresses via DHCP (S7-1500)](Configuring%20devices%20and%20networks.md#assigning-addresses-via-dhcp-s7-1500)

### UDT "Conf_ClientId_Opaque" (S7-1500)

#### UDT "Conf_ClientId_Opaque"

The UDT "Conf_ClientId_Opaque" is used to read or change the "DHCP ClientId" communication parameter. The UDT "Conf_ClientId_Opaque" provides greater flexibility compared to the use of the UDT "Conf_ClientId".

The UDT "Conf_ClientId_Opaque" is structured as follows:

| Parameter | Data type |
| --- | --- |
| Length | Byte |
| ClientId | Array[0 .. 253] of bytes |

The sum of the lengths of the host name, domain name and ClientId must not exceed 260 characters. The combination of host name and domain name must not exceed 254 characters (including delimiters) and must form an FQDN. The last delimiter is not necessary because root-label is always empty.

The difference between the UDTs "Conf_ClientId" and "Conf_ClientId_Opaque" is that you are not subject to any restrictions regarding the characters when using "Conf_ClientId_Opaque". "CommConfig" only checks the value of the "Length" parameter.

The value of "Length" must be 0 or between 2 and 254. Another value results in error 0x8094 (invalid value in the UDT referenced by DATA).

With the UDT "Conf_ClientId_Opaque" there is no special handling of the escape sequence "\0", as there with the UDT "Conf_ClientId". You may have to use 0x00 as first byte in the "ClientId" field.

> **Note**
>
> **Using the UDTs "Conf_ClientId" and "Conf_ClientId_Opaque"**
>
> Use either the UDT "Conf_ClientId" or the UDT "Conf_ClientId_Opaque".

> **Note**
>
> **Validity of data obtained via DHCP**
>
> If you change ClientId with "CommConfig", all data obtained via DHCP will be invalid: IP Suite, domain name, NTP server, DNS server. Therefore, you should only change ClientId in urgent cases and not during operation.

All connections via the IP Suite can be dropped as soon as the old address becomes invalid.

> **Note**
>
> **Writing the ClientId**
>
> The ClientId can only be written with "CommConfig" if DHCP is configured to use the ClientId.

---

**See also**

[Assigning addresses via DHCP (S7-1500)](Configuring%20devices%20and%20networks.md#assigning-addresses-via-dhcp-s7-1500)

### UDT "Conf_DNS" (S7-1500)

#### UDT "Conf_DNS"

The UDT "Conf_DNS" provides an interface to read or change the addresses of the DNS servers of the CPU.

The UDT "Conf_DNS" is structured as follows:

| Parameter | Data type |
| --- | --- |
| Count | UInt |
| DNS_Server | Array[1 .. 4] of String[39] |

The interface of the UDT "Conf_DNS" only supports IPv4 addresses.

In the "Count" parameter "CommConfig" enters the number of DNS servers read, or specify the number of DNS servers. The permissible values are 0 to 4. If the value is 0, then no DNS servers are configured or you want to delete all configured DNS servers. If the value is greater than 4, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA). If you assign three field elements in the "DNS_Server" parameter, but only specify the value 2 in the "Count" parameter, the third DNS server is not configured. In this case, "CommConfig" does not return an error. If you assign three field elements in the "DNS_Server" parameter and the specify the value 4 in the "Count" parameter, "CommConfig" returns the error 0x8094. "CommConfig" does not allow you to specify the address 0.0.0.0 for a DNS server.

The IP addresses of the DNS servers are defined as strings in the parameter "DNS_Server". The "DNS_Server" parameter consists of a field of strings. These must be in the format "www.xxx.yyy.zzz", where each substring covers the range "000" to "255". The string is therefore a maximum of 15 characters long. The field element with index 1 specifies the primary DNS server, the field element with the index 2 specifies the primary backup DNS server. If you specify an invalid IP address or an IP address in the wrong format, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).

> **Note**
>
> **Configuring the DNS servers**
>
> You must configure all DNS servers each time you write "CommConfig" with the UDT "Conf_DNS".
>
> If you violate this rule, the addresses of those DNS servers in the CPU that belong to the unassigned field elements are deleted.
>
> If you want to change the address of a DNS server, for example, you must first read the addresses of all DNS servers with "CommConfig", then change the address to be changed locally and finally write all addresses again with "CommConfig".

### UDT "Conf_DNS_IPV4" (S7-1500)

#### UDT "Conf_DNS_IPV4"

The UDT "Conf_DNS_IPV4" provides the same functionality as the UDT "Conf_DNS", but with a different interface.

The UDT "Conf_DNS_IPV4" is structured as follows:

| Parameters | Data type |
| --- | --- |
| Count | UInt |
| DNS_Server | Array[1 .. 4] of IP_V4 |

In the "Count" parameter "CommConfig" enters the number of DNS servers read, or specify the number of DNS servers. The permissible values are 0 to 4. If the value is 0, then no DNS servers are configured or you want to delete all configured DNS servers. If the value is greater than 4, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA). If you assign three field elements in the "DNS_Server" parameter, but only specify the value 2 in the "Count" parameter, the third DNS server is not configured. In this case, "CommConfig" does not return an error. If you assign three field elements in the "DNS_Server" parameter and the specify the value 4 in the "Count" parameter, "CommConfig" returns the error 0x8094. "CommConfig" does not allow you to specify the address 0.0.0.0 for a DNS server.

The IP addresses of the DNS servers are defined in the parameter "DNS_Server" as IP_V4 data types. The "DNS_Server" parameter consists of a field of IP_V4 data types. An IP_V4 data type in turn consists of a byte field with 4 elements (index 1 to 4). Each byte covers the range from "000" to "255". Together, these four bytes form an IP address, where the field element with index 1 is the highest-value byte of the IP address. In the "DNS_Server" field the field element with index 1 defines the primary DNS server, the field element with index 2 the primary backup DNS server.

> **Note**
>
> **Configuring the DNS servers**
>
> You must configure all DNS servers each time you write "CommConfig" with the UDT "Conf_DNS_IPV4".
>
> If you violate this rule, the addresses of those DNS servers in the CPU that belong to the unassigned field elements are deleted.
>
> If you want to change the address of a DNS server, for example, you must first read the addresses of all DNS servers with "CommConfig", then change the address to be changed locally and finally write all addresses again with "CommConfig".

### UDT "Conf_IPSuitev4" (S7-1500)

#### UDT "Conf_IPSuitev4"

The UDT "Conf_IPSuitev4" provides an interface to read or change the IP suite of the communication interface.

The UDT "Conf_IPSuitev4" is structured as follows:

| Parameters | Data type |
| --- | --- |
| write_mode | UInt |
| IPAddress | String[15] |
| SubnetMaskPrefix | UInt |
| Gateway | String[15] |

The "write_mode" parameter determines whether the IP suite is stored permanently when it is written or not. The following values are valid for "write_mode":

- 0: Value after performing a read operation. If you specify this value for a write operation, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).
- 1: The IP suite should be saved permanently.
- 2: The IP suite should be saved temporarily. In this case the IP suite is lost during a POWER-OFF-POWER-ON transition.

The IP address of the IP suite is defined as a string in the "IPAddress" parameter. This must be in the format "www.xxx.yyy.zzz", with each substring covering the range "000" to "255". The string is therefore a maximum of 15 characters long. If you specify an invalid IP address or an IP address in the wrong format, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).

The "SubnetmaskPrefix" parameter specifies the subnet mask of the IP suite, in CIDR notation. CIDR means Classless Inter-Domain Routing. This notation indicates the number of bits set in the subnet mask. These start at the MSB (most significant bit) and adjoin each other. Example: 9 in CIDR notation corresponds to 11111111.10000000.00000000.00000000 in binary notation and 255.128.0.0 in decimal notation. The allowed range for the "SubnetMaskPrefix" parameter is 4 to 30.

The following table shows the subnet mask values for the permissible values of the "SubnetMaskPrefix" parameter.

| Value of "SubnetMaskPrefix" (CIDR) | Value of the subnet mask |
| --- | --- |
| 4 | 240.0.0.0 |
| 5 | 248.0.0.0 |
| 6 | 252.0.0.0 |
| 7 | 254.0.0.0 |
| 8 | 255.0.0.0 |
| 9 | 255.128.0.0 |
| 10 | 255.192.0.0 |
| 11 | 255.224.0.0 |
| 12 | 255.240.0.0 |
| 13 | 255.248.0.0 |
| 14 | 255.252.0.0 |
| 15 | 255.254.0.0 |
| 16 | 255.255.0.0 |
| 17 | 255.255.128.0 |
| 18 | 255.255.192.0 |
| 19 | 255.255.224.0 |
| 20 | 255.255.240.0 |
| 21 | 255.255.248.0 |
| 22 | 255.255.252.0 |
| 23 | 255.255.254.0 |
| 24 | 255.255.255.0 |
| 25 | 255.255.255.128 |
| 26 | 255.255.255.192 |
| 27 | 255.255.255.224 |
| 28 | 255.255.255.240 |
| 29 | 255.255.255.248 |
| 30 | 255.255.255.252 |

The default gateway (or default router address) of the IP suite is defined as a string in the "Gateway" parameter. This character string must be an IPV4 address in the format "www.xxx.yyy.zzz", with each substring covering the range "000" to "255". The string is therefore a maximum of 15 characters long. If you specify an invalid gateway address or a gateway address in the wrong format, "CommConfig" returns error 0x8094 (invalid value in the UDT referenced by DATA).

> **Note**
>
> **Specify the default gateway or default router**
>
> The default gateway or default router is defined only once per CPU. This means that your last setting applies. The interface is irrelevant for the default gateway or the default router. If you do not want to change the default gateway or the default router when writing the IP suite, first read its value and then write it again.

### UDT "Conf_IPSuitev4_IPV4" (S7-1500)

#### UDT "Conf_IPSuitev4_IPV4"

The UDT "Conf_IPSuitev4_IPV4" offers the same functionality as the UDT "Conf_IPSuitev4", but with a different interface.

The UDT "Conf_IPSuitev4_IPV4" is structured as follows:

| Parameters | Data type |
| --- | --- |
| write_mode | UInt |
| IPAddress | IP_V4 |
| SubnetMask | IP_V4 |
| Gateway | IP_V4 |

The "write_mode" parameter determines whether the IP suite is stored permanently when it is written or not. The following values are valid for "write_mode":

- 0: Value after performing a read operation. If you specify this value for a write operation, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).
- 1: The IP suite should be saved permanently.
- 2: The IP suite should be saved temporarily. In this case the IP suite is lost during a POWER-OFF-POWER-ON transition.

The IP address of the IP suite is defined in the "IPAddress" parameter as IP_V4 data type. An IP_V4 data type consists of a byte field with 4 elements (index 1 to 4). Each byte covers the range from 0 to 255. Together, these four bytes form an IP address, where the field element with index 1 is the highest-value byte of the IP address.

The subnet mask of the IP suite is defined as IP_V4-Data type in the "Subnetmask" parameter.

The default gateway (or default router address) of the IP suite is defined in the "Gateway" parameter as IP_V4 data type.

> **Note**
>
> **Specify the default gateway or default router**
>
> The default gateway or default router is defined only once per CPU. This means that your last setting applies. The interface is irrelevant for the default gateway or the default router. If you do not want to change the default gateway or the default router when writing the IP suite, first read its value and then write it again.

### UDT "Conf_NTP" (S7-1500)

#### UDT "Conf_NTP"

The UDT "Conf_NTP" provides an interface to change the addresses of the NTP servers of the CPU (NTP = Network Time Protocol).

The UDT "Conf_NTP" is structured as follows:

| Parameters | Data type |
| --- | --- |
| Count | UInt |
| NTP_Server | Array[1 .. 4] of String[254] |

The UDT "Conf_NTP" only supports IPv4 addresses.

The "Count" parameter is used to specify the number of NTP servers that you want to configure. The permissible values are 0 to 4. If the value is greater than 4, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA). If you assign 3 field elements in the parameter "NTP_Server", but only specify the value 2 in the "Count" parameter, then the third NTP server is not configured. In this case, "CommConfig" does not return an error. If you assign 3 field elements in the parameter "NTP_Server" and specify the value 4 in the "Count" parameter, then "CommConfig" returns the error 0x8094. "CommConfig" does not allow you to specify the address 0.0.0.0 for an NTP server. If you specify the value 0, no NTP server address is changed.

The IP addresses of the NTP servers are defined as strings in the parameter "NTP_Server". The "NTP_Server" parameter consists of a field of strings. These must be in the format "www.xxx.yyy.zzz", where each substring covers the range "000" to "255". The string is therefore a maximum of 15 characters long. The field element with index 1 specifies the primary NTP server, the field element with the index 2 specifies the primary backup NTP server. If you specify an invalid IP address or an IP address in the wrong format, "CommConfig" returns the error 0x8094 (invalid value in the UDT referenced by DATA).

> **Note**
>
> **Configuring the NTP servers**
>
> You must configure all NTP servers each time you write "CommConfig" with the UDT "Conf_NTP". If you violate this rule, the addresses of those NTP servers in the CPU that belong to the unused field elements are deleted.

> **Note**
>
> **Read the addresses of the NTP servers**
>
> Reading the addresses of the NTP servers is not possible with the UDT "CONF_NTP". If you call CommConfig with MODE=0 call and refer to the UDT "Conf_NTP" at the parameter "DATA", CommConfig returns the error 0x80A9 (function is not supported).

## Other (S7-1200, S7-1500)

This section contains information on the following topics:

- [TCON: Establishing a communication connection (S7-1200, S7-1500)](#tcon-establishing-a-communication-connection-s7-1200-s7-1500)
- [TDISCON: Terminate communication connection (S7-1200, S7-1500)](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)
- [TSEND: Send data via communication connection (S7-1200, S7-1500)](#tsend-send-data-via-communication-connection-s7-1200-s7-1500)
- [TRCV: Receive data via communication connection (S7-1200, S7-1500)](#trcv-receive-data-via-communication-connection-s7-1200-s7-1500)
- [Program example for TCON, TDISCON, TSEND &amp; TRCV (S7-1200, S7-1500)](#program-example-for-tcon-tdiscon-tsend-trcv-s7-1200-s7-1500)
- [Sending and receiving data via Ethernet (UDP) or FDL (S7-1200, S7-1500)](#sending-and-receiving-data-via-ethernet-udp-or-fdl-s7-1200-s7-1500)
- [T_RESET: Resetting the connection (S7-1200, S7-1500)](#t_reset-resetting-the-connection-s7-1200-s7-1500)
- [Program example for T_RESET (S7-1200, S7-1500)](#program-example-for-t_reset-s7-1200-s7-1500)
- [T_DIAG: Checking the connection (S7-1200, S7-1500)](#t_diag-checking-the-connection-s7-1200-s7-1500)
- [Program example for T_DIAG (S7-1200, S7-1500)](#program-example-for-t_diag-s7-1200-s7-1500)
- [T_CONFIG: Configure interface (S7-1200, S7-1500)](#t_config-configure-interface-s7-1200-s7-1500)
- [TCONSettings: Preparing and installing the communication connection (S7-1200, S7-1500)](#tconsettings-preparing-and-installing-the-communication-connection-s7-1200-s7-1500)

### TCON: Establishing a communication connection (S7-1200, S7-1500)

This section contains information on the following topics:

- [TCON: Establish communication connection (S7-1200)](#tcon-establish-communication-connection-s7-1200)
- [TCON: Establish communication connection (S7-1200, S7-1500)](#tcon-establish-communication-connection-s7-1200-s7-1500)

#### TCON: Establish communication connection (S7-1200)

##### Validity

The following description of the "TCON" instruction applies to S7-1200 CPUs with firmware version &lt; V4.0.

##### Description

You use the "TCON" instruction to set up and establish a communication connection. Once the connection has been set up and established, it is automatically maintained and monitored by the CPU. "TCON" executes asynchronously.

The connection data specified for the CONNECT and ID parameters are used to set up the communication connection. To establish the connection, a rising edge must be detected at the REQ parameter. Once the connection is successfully established, the DONE parameter is set to "1".

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and create connections of the type TCP, UDP or ISO-on-TCP and want to assign parameters to them, you can use the support of the connection parameter assignment.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

##### Number of possible connections

For information on the number of possible communication connections, refer to the technical specifications for your CPU.

##### TCP and ISO‑on‑TCP connections

Both communication partners call the "TCON" instruction to set up and establish the communication connection. During parameter assignment, you specify which partner is the active communication end point and which is the passive one.

If the connection aborts, for example due to a line break or due to the remote communication partner, the active partner attempts to reestablish the configured connection. You do not have to call "TCON" again. This applies only if "TCON" has been executed successfully once (DONE = 1).

An existing connection is terminated and the connection set up is removed when the "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instruction is executed or when the CPU changes to STOP mode. To set up and establish the connection again, you will need to execute "TCON" again.

##### Parameters

The following table shows the parameters of the "TCON" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Starts the job to establish the connection specified in the ID upon a rising edge. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the assigned connection.  Value range: W#16#0001 to W#16#0FFF |
| CONNECT | InOut | TCON_Param | D | Pointer to the connection description  See also: [Connection parameters with structure according to TCON_Param](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:   - 0: Job not yet started or still in progress - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. You use the DONE parameter to check whether or not a job has been executed successfully. The ERROR parameter is set if errors occur during execution of "TCON". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Connection successfully established. |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start job execution, establish connection. |
| 0 | 7002 | Connection is being established (REQ irrelevant). |
| 1 | 8085 | Connection ID (ID parameter) is already being used by a configured connection. |
| 1 | 8086 | The ID parameter is outside the valid range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible |
| 1 | 8089 | The CONNECT parameter does not point to a data block. |
| 1 | 809A | The structure at the CONNECT parameter is not supported on an integrated interface or the length is invalid or an incorrect "InterfaceID" is specified in the connection description (SDT). |
| 1 | 809B | The element InterfaceId within the TCON_xxx structure does not reference a hardware identifier of a CPU or CM/CP interface or has the value "0". |
| 1 | 80A0 | Group error for error codes W#16#80A1 and W#16#80A2. |
| 1 | 80A1 | The specified connection or the local port is already being used. |
| 1 | 80A2 | Local port is being used by the system. |
| 1 | 80A3 | Attempt being made to re-establish an existing connection. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid, in other words, it matches the IP address of the local partner. |
| 1 | 80A5 | Connection ID is already in use. |
| 1 | 80A7 | Communication error: You executed "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" before "TCON" had completed. |
| 1 | 80B2 | The CONNECT parameter points to a data block that was generated with the attribute "Only store in load memory". |
| 1 | 80B4 | You have violated one or more of the following conditions for passive connection establishment with the ISO-on-TCP protocol variant (connection_type = B#16#12):  - local_tsap_id_len &gt;= B#16#02 - local_tsap_id[1] = B#16#E0 - With local_tsap_id_len &gt;= B#16#03, local_tsap_id[1] is an ASCII character. - local_tsap_id[1] is an ASCII character and local_tsap_id_len &gt;= B#16#03. |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP. |
| 1 | 80B6 | Parameter assignment error at the connection_type parameter of the SDT TCON_Param. |
| 1 | 80B7 | Error in one of the following parameters of the data block for connection description: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len.  Note: If you call TCON in TCP for the passive end, local_tsap_id_len must have the value 2 and rem_tsap_id_len the value 0. |
| 1 | 80B8 | Connection description of the structure element ID and the block parameter ID are not identical. |
| 1 | 80C3 | All connection resources are in use. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is currently receiving new parameters. - The configured connection is currently being removed by a "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instruction. |
| * The error codes in the program editor can be displayed as integer or hexadecimal values. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)

#### TCON: Establish communication connection (S7-1200, S7-1500)

##### Description

You use the "TCON" instruction to set up and establish a communication connection. Once the connection has been set up and established, it is automatically maintained and monitored by the CPU. "TCON" executes asynchronously.

For S7-1500-CPUs as of firmware version V2.0 and higher, you can set up an access point for IPv4 multicast communication with the instruction "TCON" via the integrated PROFINET interfaces.

The connection data specified for the CONNECT and ID parameters are used to set up the communication connection. At the CONNECT parameter, if possible, only use the predefined structures as created by the connection parameter assignment in the Inspector window of the program editor.

As of firmware version V2.0 of the S7-1500 CPUs, you can specify the value 0 for specific TCON_xxx structures at the Interface ID parameter. You thus allow the firmware to select the Industrial Ethernet interface to be used. This specification of the value 0 is possible with the following SDTs: TCON_IP_V4_SEC, TCON_QDN, TCON_QDN_SEC, TMail_QDN_SEC, TMail_V4 and TMAIL_V4_SEC. With all other SDTs, you must assign a fixed value to the Interface ID.

To establish the connection, a rising edge must be detected at the REQ parameter. Once the connection is successfully established, the DONE parameter is set to "1".

> **Note**
>
> **Support when programming connections**
>
> If you select an instruction for communication TCON, TSEND_C or TRCV_C in a program block and wish to create and assign parameters to connections of the type TCP, UDP, ISO‑on‑TCP or FDL, you can use the support of the connection parameter assignment.
>
> You can find the connection parameter assignment in the Inspector window of the program editor.

##### Calling of "TCON" with a connection ID provided by "TCONSettings"

S7-1500 CPUs with firmware version V2.9 or higher and S7-1200 CPUs with firmware version V4.5 or higher include the instruction "TCONSettings". If you call "TCON" with a connection ID provided by "TCONSettings", "TCON" establishes the connection prepared by "TCONSettings". "TCON" checks whether the connection type and the interface are permitted and returns the return value W#16#8090 if appropriate.

> **Note**
>
> **Error message when you use a connection ID supplied by "TCONSettings"**
>
> If a TCON call is made with a connection ID provided by "TCONSettings" and the call terminates with an error, the connection ID may no longer be valid. This may be because the CPU releases the connection resource and invalidates the connection ID when specific error conditions occur.
>
> In this situation, if the TCON call is started, the BUSY output is set to TRUE, and the call terminates with an error, the connection ID provided by "TCONSettings" is no longer valid and a new connection ID must be requested with "TCONSettings".
>
> If the TCON call is started and that call immediately ends with an error (BUSY output was never set to TRUE for the current call), the connection ID provided by "TCONSettings" is still valid. You have to fix the cause of the error and then you can start a new TCON call with the same connection ID provided by "TCONSettings".

##### Number of possible connections

For information on the number of possible communication connections, refer to the technical specifications for your CPU.

##### Connection with TCP and ISO‑on‑TCP

Both communication partners call the "TCON" instruction to set up and establish the communication connection. During parameter assignment, you specify which partner is the active communication end point and which is the passive one.

If the connection aborts, for example due to a line break or due to the remote communication partner, the active partner attempts to reestablish the configured connection. You do not have to call "TCON" again. This applies only if "TCON" has been executed successfully once (DONE = 1).

An existing connection is terminated and the connection set up is removed when the "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instruction is executed or when the CPU changes to STOP mode. To set up and establish the connection again, you will need to execute "TCON" again.

##### Telecontrol connections between CP and SMS client

Use the TCON_PHONE system data type for connection description in the CONNECT parameter.

For this connection type, the station requires access to the mobile network via a mobile network CP.

##### FDL connections

To set up the FDL connections of the CM 1542‑5, see [Setting up communication over FDL](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#setting-up-communication-over-fdl-s7-300-s7-400).

##### Parameter

The following table shows the parameters of the "TCON" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Starts the job to establish the connection specified on a rising edge. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the assigned connection.  Value range: W#16#0001 to W#16#0FFF  Note: A connection ID supplied by "TCONSettings" is outside this range of values. |
| CONNECT | InOut | VARIANT | D | Pointer to the connection description  - For TCP or UDP, use the structure TCON_IP_v4 or TCON_QDN   For a description, refer to: [Connection parameters with structure according to TCON_IP_v4](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_v4-s7-1200-s7-1500) or [Connection parameters in accordance with TCON_QDN](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn-s7-1500) - With TCP via secure communication, use the structure TCON_IP_V4_SEC or TCON_QDN_SEC   For a description, refer to: [Connection parameters according to TCON_IP_V4_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-according-to-tcon_ip_v4_sec-s7-1500) or [Connection parameters in accordance with TCON_QDN_SEC](Configuring%20devices%20and%20networks.md#connection-parameters-in-accordance-with-tcon_qdn_sec-s7-1500) - For ISO-on-TCP, use the structure TCON_IP_RFC   For a description, refer to: [Connection parameters with structure according to TCON_IP_RFC](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_ip_rfc-s7-1200-s7-1500) - For ISO connections of the CP 1543‑1 / CP 1545‑1, use the structure TCON_ISOnative.   For a description, refer to: "Structure of the connection description according to TCON_ISOnative" - For connections to SMS clients, use the TCON_PHONE system data type.   For a description, refer to [Connection parameters to TCON_Phone](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_phone-s7-1200-s7-1500-s7-1500t). - For FDL connections of the CM 1542‑5, use the system data type TCON_FDL; see [Connection parameters to TCON_FDL](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_fdl-s7-1200-s7-1500). |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:   - 0: Job not yet started or still in progress - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. You use the DONE parameter to check whether or not a job has been executed successfully. The ERROR parameter is set if errors occur during execution of "TCON". The error information is output at the STATUS parameter.

The instruction "TCON" generates an error message in version 3.0 if an active connection establishment to a remote partner fails. Create a rising edge at the REQ parameter to establish a connection once again.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

##### Structure of the connection description according to TCON_ISOnative

A connection description DB with a structure according to TCON_ISOnative is used to assign the communication connection parameters for ISO. The fixed data structure of the TCON_ISOnative contains all parameters that are required to establish the connection.

| Byte | Parameter |  | Data type | Start value | Description |
| --- | --- | --- | --- | --- | --- |
| 0 … 1 | InterfaceId |  | HW_ANY | 0 | Hardware identifier of the CP interface |
| 2 … 3 | ID |  | CONN_OUC | 1 | Reference to this connection (unique ID in the value range: 1 to 4095). |
| 4 | ConnectionType |  | BYTE | 16#16 | Connection type: ISO |
| 5 | ActiveEstablished |  | BOOL | TRUE | ID for the manner in which the connection is established:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 8 to 13 | RemoteMacAddress |  | ARRAY [1..6] of BYTE | - | MAC address of the partner end point, for example, for 00-74-41-FD-AE-84:   - MacAddr[1] = 00 - MacAddr[2] = 74 - MacAddr[3] = 41 - MacAddr[4] = FD - MacAddr[5] = AE - MacAddr[6] = 84 |
| 14 - 19 | LocalMacAddress |  | ARRAY [1..6] of BYTE | - | MAC address of the local end point, for example, for 00-74-41-FD-AE-84:   - MacAddr[1] = 00 - MacAddr[2] = 74 - MacAddr[3] = 41 - MacAddr[4] = FD - MacAddr[5] = AE - MacAddr[6] = 84 |
| 20 - 53 | RemoteTSelector |  | Struct | - | TSelector of the remote connection partner:  - Bytes 20 to 21 = TSelLength - Bytes 22 to 53 = TSel[1-32] |
|  | TSelLength | UINT | - | Value range from 0 to 32 |  |
| TSel | ARRAY [1..32] of BYTE | - | Value range in each case 0 to 255 in bytes |  |  |
| 54 - 87 | LocalTSelector |  | Struct | - | TSelector of the local connection partner:  - Bytes 20 to 21 = TSelLength - Bytes 22 to 53 = TSel[1-32] |
|  | TSelLength | UINT |  | Value range from 0 to 32 |  |
| TSel | ARRAY [1..32] of BYTE | - | Value range in each case 0 to 255 in bytes |  |  |
| 88 - 89 | CrRetransmitionTime |  | UINT | - | Duration until connection attempt is repeated in seconds. |
| 90 - 91 | DataRetransmitionTime |  | UINT | 100 ms | Duration until data transfer is repeated in milliseconds. |
| 92 - 93 | MaxRetransmitionCount |  | UINT | - | Maximum number of repetitions. |
| 94 - 95 | InactivityTime |  | UINT | - | in seconds |
| 96 - 97 | WindowTime |  | UINT |  | in seconds |

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Connection successfully established. |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start job execution, establish connection. |
| 0 | 7002 | Connection is being established (REQ irrelevant). |
| 1 | 8085 | Connection ID (ID parameter) is already being used by a configured connection. |
| 1 | 8086 | The ID parameter is outside the valid range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible |
| 1 | 8089 | The CONNECT parameter does not point to a connection description or the connection description was created manually. |
| 1 | 8090 | You have tried to establish a prepared connection, the properties of which are incompatible with the protocol or interface that are specified at the CONNECT parameter. |
| 1 | 809A | The structure at the CONNECT parameter is not supported on an integrated interface or the length is invalid. |
| 1 | 809B | - The InterfaceId element within the TCON_xxx structure does not reference a hardware identifier of a CPU or CM/CP interface. - The InterfaceId element cannot have the value "0" in the TCON_xxx structure used; see section "Description". - In the TCON_QDN or TCON_QDN_SEC structure used, the InterfaceId element has neither the value "0" nor the InterfaceId of a valid CP. - TCON_QDN or TCON_QDN_SEC requires a configured DNS server. |
| 1 | 809C | For UDP Multicast communication, InterfaceID = 0 is not permitted. The hardware identifier of the local PLC or CP interface intended for Multicast communication must be entered. |
| 1 | 80A1 | The specified connection or the local port is already being used. |
| 1 | 80A2 | Local port is being used by the system. See also: [Assignment of port numbers](Configuring%20devices%20and%20networks.md#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t) |
| 1 | 80A3 | ID is used by a connection created by the user program, which uses the same connection description at the CONNECT parameter. |
| 1 | 80A4 | IP address of the remote endpoint of the connection is invalid or it corresponds to the IP address of the local partner. |
| 1 | 80A7 | Communication error: You executed "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" before "TCON" had completed. |
| 1 | 80B4 | Only with TCON_IP_RFC: The local T selector was not specified or the first byte does not contain the value 0x0E (only with a length of T selector = 2) or the local T selector starts with "SIMATIC-". |
| 1 | 80B5 | Only passive connection establishment is permitted for connection type 13 = UDP (parameter ActiveEstablished of the structure TCON_IP_v4 / TCON_PARAM has the value TRUE). |
| 1 | 80B6 | Parameter assignment error in the ConnectionType parameter of the data block for connection description.  - Only valid with TCON_IP_v4: 0x11, 0x0B and 0x13. - Only valid with TCON_IP_RFC: 0x0C and 0x12 |
| 1 | 80B7 | With TCON_IP_v4:  - TCP (active connection establishment): Remote port is "0". - TCP (passive connection establishment): Local port is "0". - UDP: Local port is "0". - IP address of the partner end point was set to 0.0.0.0.   With TCON_IP_RFC:   - Local (LocalTSelector) or remote (RemoteTSelector) T selector was specified with a length of more than 32 bytes. - For TSelLength of the T selector (local or remote), a length greater than 32 was entered. - Error in the length of the IP address of the specific connection partner. - IP address of the partner end point was set to 0.0.0.0. |
| 1 | 80B8 | Parameter ID in the local connection description (structure at CONNECT parameter) and parameter ID of the instruction are different. |
| 1 | 80C3 | All connection resources are assigned, or the local port may be dynamically used by other applications or connections. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The connection cannot be established because the firewalls on the connection path are not open for the required ports. - The interface is currently receiving new parameters. - The configured connection is currently being removed by a "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instruction. |
| 1 | 80C5 | The connection partner refuses to establish the connection, has terminated the connection or actively ended it. |
| 1 | 80C6 | The connection partner cannot be reached (network error). |
| 1 | 80C7 | Execution timeout. |
| 1 | 80C8 | Value at the ID parameter is already being used by a connection that was created using the user program. The connection uses the identical ID, but different connection settings at the parameter CONNECT. |
| 1 | 80C9 | Validation of the connection partner failed. The connection partner that wants to establish the connection does not match the defined partner of the structure at the CONNECT parameter. |
| 1 | 80CE | The IP address of the local interface is 0.0.0.0. |
| 1 | 80D0 | In connection with TCP and the active connection end point: The remote_qdn parameter is an empty string. In this case, no connection can be established. |
| 1 | 80D1 | The remote_qdn parameter is not a fully qualified domain name. The dot at the end might be missing. |
| 1 | 80D2 | No DNS server address is configured. |
| 1 | 80D3 | The fully qualified domain name could not be resolved. Possible causes:  - The DNS server is not reachable, for example, because it has been shut down or the remote port is not reachable (e.g. due to a firewall). - An error occurred during communication with the DNS server. - The DNS server returned a valid DNS answer, but the answer contained no IPv4 address. |
| 1 | 80E0 | Unsuitable or poor message was received. |
| 1 | 80E1 | Error during the handshake. Possible causes:  - Abort by the user - Security not high enough - Renewed negotiation is not supported - SSL/TLS version is not supported - Validation of the host name failed |
| 1 | 80E2 | Certificate not supported / certificate invalid / no certificate  Possible cause: The time-of-day of the module concerned is not set or the module is not synchronized.  Example: The default setting for the date of the module is 1 January 2012 and it was not set during commissioning. The validity period of the certificate starts on 20 August 2016 and ends on 20 August 2024. In this case, the date of the module is outside the validity period of the certificate; the certificate is invalid for the module. |
| 1 | 80E3 | Certificate was discarded. |
| 1 | 80E4 | No valid certification authority found. |
| 1 | 80E5 | Certificate expired. |
| 1 | 80E6 | Integrity errors in the Transport Layer Security Protocol |
| 1 | 80E7 | Not supported extension in X.509-V3 certificate |
| 1 | 80E9 | TLS server without server certificate is not supported. |
| 1 | 80EA | DTLS (UDP) protocol is not supported. |
| 1 | 80EB | A client cannot request a client certificate. |
| 1 | 80EC | The server cannot perform validation based on the subjectAlternateName (only clients can do this). |
| 1 | 80ED | TLSServerCertRef_m-ID invalid |
| 1 | xxyy, xx &gt; 80 | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| * The error codes in the program editor can be displayed as integer or hexadecimal values. For information on switching the display formats, refer to "See also". |  |  |

##### Example

You can find the example here: [Program example for TCON, TDISCON, TSEND &amp; TRCV](#program-example-for-tcon-tdiscon-tsend-trcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Overview of connection configuration (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#overview-of-connection-configuration-s7-1200-s7-1500-s7-1500t)
  
[Starting connection parameter assignment (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#starting-connection-parameter-assignment-s7-1200-s7-1500-s7-1500t)
  
[Creating and assigning parameters to connections (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#creating-and-assigning-parameters-to-connections-s7-1200-s7-1500-s7-1500t)
  
[Secure OUC between two S7-1500 CPUs (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-between-two-s7-1500-cpus-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as a TLS client to an external PLC (TLS server) (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-from-an-s7-1500-cpu-as-a-tls-client-to-an-external-plc-tls-server-s7-1500-s7-1500t)
  
[Secure OUC from an S7-1500 CPU as TLS server to an external PLC (TLS client) (S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#secure-ouc-from-an-s7-1500-cpu-as-tls-server-to-an-external-plc-tls-client-s7-1500-s7-1500t)
  
[TCON: Establish communication connection (S7-1200)](#tcon-establish-communication-connection-s7-1200)

### TDISCON: Terminate communication connection (S7-1200, S7-1500)

#### Description

The "TDISCON" instruction terminates a communication connection from the CPU to a connection partner.

> **Note**
>
> **Call of "TDISCON" with a connection ID provided by "TCONSettings"**
>
> S7-1500 CPUs with firmware version V2.9 or higher and S7-1200 CPUs with firmware version V4.5 or higher include the instruction "TCONSettings". If you call "TDISCON" with a connection ID provided by "TCONSettings", this connection ID and the corresponding connection resource are enabled again.

#### Functional description

"TDISCON" is an instruction that works asynchronously, which means its job processing extends over multiple calls. You start the job for terminating a connection by calling the "TDISCON" instruction with REQ = 1.

After "TDISCON" has been successfully executed, the ID specified for "TCON" is no longer valid and cannot be used for sending or receiving.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions (see also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)).

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can recognize the current status of "TDISCON" or when the establishment of the connection is completed.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | Job successfully completed. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| 0 | 0 | 0 | The instruction was not assigned a (new) job. |

#### Parameters

The following table shows the parameters of the instruction "TDISCON":

| Parameter | Declaration | Data type | Memory area |  | Description |
| --- | --- | --- | --- | --- | --- |
| S7-1200 | S7-1500 |  |  |  |  |
| REQ | Input | BOOL | I, Q, M, D, L or constant | I, Q, M, D, L or constant | Control parameter REQUEST starts the job for terminating the connection specified by ID. The job starts on a rising edge. |
| ID | Input | CONN_OUC (WORD) | D, L or constant | I, Q, M, D, L or constant | Reference to the connection to be terminated (connection ID)  Value range: W#16#0001 to W#16#0FFF  Note: A connection ID supplied by "TCONSettings" is outside this range of values. |
| DONE | Output | BOOL | I, Q, M, D, L | I, Q, M, D, L | Status parameter:   - 0: Job not yet started or still executing. - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | I, Q, M, D, L | Status parameter:  - BUSY = 1: The job is not yet complete. - BUSY = 0: The job has been completed or has not yet started. |
| ERROR | Output | BOOL | I, Q, M, D, L | I, Q, M, D, L | Status parameter:  - ERROR = 0: No error. - ERROR=1: An error occurred during processing. STATUS supplies detailed information on the type of error |
| STATUS | Output | WORD | I, Q, M, D, L | I, Q, M, D, L | Status parameter:   Error information (see "Parameters ERROR and STATUS") |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Connection terminated successfully. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | Start of job processing, connection being terminated. |
| 0 | 7002 | Intermediate call (REQ irrelevant), connection being terminated. |
| 1 | 8086 | The ID parameter is not in the permitted value range. |
| 1 | 80A3 | Attempt is being made to terminate a non-existent connection or the connection is already terminated. |
| 1 | 80C4 | Temporary communication error: New parameters are being assigned to the interface or the connection is currently being established. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

#### Example

You can find the example here: [Program example for TCON, TDISCON, TSEND &amp; TRCV](#program-example-for-tcon-tdiscon-tsend-trcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)

### TSEND: Send data via communication connection (S7-1200, S7-1500)

This section contains information on the following topics:

- [TSEND: Send data via communication connection (S7-1200)](#tsend-send-data-via-communication-connection-s7-1200)
- [TSEND: Send data via communication connection (S7-1200, S7-1500)](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)

#### TSEND: Send data via communication connection (S7-1200)

##### Description

The following description of the "TSEND" instruction is valid for the CPU S7-1200 to version 3.0.

You use the "TSEND" instruction to send data over an existing communication connection. TSEND executes asynchronously.

You specify the send area with the DATA parameter. This includes the address and the length of the data to be sent. All data types except BOOL and Array of BOOL can be used for the data to be sent.

The send job is executed when a rising edge is detected at the REQ parameter.

With the LEN parameter, you specify the maximum number of bytes sent with a send job.

- When data is transferred with TCP (streaming protocol), the "TSEND" instruction provides no information about the length of the data sent to "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)".
- When data is transferred with ISO-on-TCP (message-oriented protocol), the length of the data sent is communicated to "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)". The amount of data sent with "TSEND" as packet must also be received again at the receiving end ("[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)"):

  - If the receive buffer is too small for the sent data, an error occurs at the receiving end.
  - If the receive buffer is sufficiently large, "TRCV" returns with DONE=1 as soon as the data packet is received.

The data to be sent must not be edited until the send job is completed. If the send job executes successfully, the DONE parameter is set to "1". Signal state "1" at the DONE parameter is not confirmation that the data sent has already been read by the communication partner.

##### Parameter

The following table shows the parameters of the "TSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Starts the send job on a rising edge. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the connection established with "TCON". Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | UINT | I, Q, M, D, L or constant | Maximum number of bytes to be sent with the job. |
| DATA | InOut | VARIANT | I, Q, M, D | Pointer to the send area containing the address and the length of the data to be sent. The address references:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   When transferring structures, the structures must be identical at the sending and receiving end. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or still in progress - 1: Job completed without error |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### LEN and DATA parameters

- With LEN = 0 , all the data specified with the DATA parameter is sent.
- If the number of bytes at the LEN parameter is larger than the length of the data to be sent that was defined with the DATA parameter, the error code 8088 is output at the STATUS parameter (see description of the STATUS parameter below).
- If a structure (Struct) is referenced via the DATA parameter, LEN can be shorter than the structure. In this case, only the data up to the length of the LEN parameter is transferred.
- With data types STRING and WSTRING, all data is transferred if the parameter LEN = 0. When LEN &gt; 0, the length must be at least the maximum number of bytes plus two additional bytes which contain the length information. You will find more detailed information on the structure of the data types in: "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".
- The maximum number of bytes that can be transmitted amounts to 8192.
- When you use structured tags from optimized DBs, the address of the structured tag should be interconnected at the DATA parameter and the parameter LEN = 0. This guarantees type-safe transmission of the entire structure if the same structure is used at the receiving end.

##### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set when errors occurred during execution of "TSEND". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is specified in the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

> **Note**
>
> Because "TSEND" is executed asynchronously, you must keep the data in the send area consistent until the DONE parameter or the ERROR parameter changes to the value "1".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Send job completed without error. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | Start of job execution, data is being sent.  When processing this job, the operating system accesses the data in the DATA send area. |
| 0 | 7002 | Job executing (REQ irrelevant).  When processing this job, the operating system accesses the data in the DATA send area. |
| 1 | 8085 | - The LEN parameter is greater than the highest permitted value (65536). - DATA and LEN parameters both have the value "0". |
| 1 | 8086 | The ID parameter is outside the permitted address range (1..0xFFF). |
| 1 | 8088 | The LEN parameter is greater than the area specified in DATA. |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is being terminated. Transfer via this connection is not possible. - The interface is being re-initialized. |
| 1 | 80B3 | The protocol variant (ConnectionType parameter in the connection description) is set to UDP. Use the instruction "TUSEND" with a UDP connection. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority group. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established to the partner at this time. - The interface is receiving new parameter settings or the connection is being established. |
| 1 | 80C5 | Connection terminated by the communication partner. |
| 1 | 80C6 | Network error. Communication partner cannot be reached. |
| 1 | 80C7 | Execution timeout. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### TSEND: Send data via communication connection (S7-1200, S7-1500)

##### Description

The following description of the "TSEND" instruction is valid for:

- Ethernet

  CPU S7-1200 with firmware version ≥ V4.0 and CPU S7-1500
- PROFIBUS

  FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL

You use the "TSEND" instruction to send data over an existing communication connection. TSEND executes asynchronously.

You specify the send area with the DATA parameter. This includes the address and the length of the data to be sent. All data types except BOOL and Array of BOOL can be used for the data to be sent.

The send job is executed when a rising edge is detected at the REQ parameter.

With the LEN parameter, you specify the maximum number of bytes sent with a send job.

- When data is transferred with TCP (streaming protocol), the "TSEND" instruction provides no information about the length of the data sent to "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)".
- When data is transferred with ISO-on-TCP (message-oriented protocol), the length of the data sent is communicated to "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)". The amount of data sent with "TSEND" as packet must also be received again at the receiving end ("[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)"):

  - If the receive buffer is too small for the sent data, an error occurs at the receiving end.
  - If the receive buffer is sufficiently large, "TRCV" returns with DONE=1 as soon as the data packet is received.

The data to be sent must not be edited until the send job is completed. If the send job executes successfully, the DONE parameter is set to "1". Signal state "1" at the DONE parameter is not confirmation that the data sent has already been read by the communication partner.

##### Parameter

The following table shows the parameters of the "TSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Starts the send job on a rising edge. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the connection established with "TCON". Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Maximum number of bytes that are sent with the job (maximum permissible value for S7-1200: 8192, maximum permissible value for S7-1500: 65536).  For FDL connections of the CM 1542‑5, the maximum length is 240 bytes. In this regard, note the maximum lengths that can be processed by the connection partner. |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the send area containing the address and the length of the data to be sent. The address references:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block - Local data   When transferring structures, the structures must be identical at the sending and receiving end. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or still in progress - 1: Job completed without error |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### LEN and DATA parameters

- With LEN = 0 , all the data specified with the DATA parameter is sent.
- If the number of bytes at the LEN parameter is larger than the length of the data to be sent that was defined with the DATA parameter, the error code 8088 is output at the STATUS parameter (see description of the STATUS parameter below).
- If a structure (Struct) is referenced via the DATA parameter, LEN can be shorter than the structure. In this case, only the data up to the length of the LEN parameter is transferred.
- With data types STRING and WSTRING, all data is transferred if the parameter LEN = 0. When LEN &gt; 0, the length must be at least the maximum number of bytes plus two additional bytes which contain the length information. You will find more detailed information on the structure of the data types in: "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".
- The maximum number of bytes that can be transmitted depends on the device.
- When you use structured tags from optimized DBs, the address of the structured tag should be interconnected at the DATA parameter and the parameter LEN = 0. This guarantees type-safe transmission of the entire structure if the same structure is used at the receiving end.

##### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set if errors occur during execution of "TSEND". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is specified in the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

> **Note**
>
> Because "TSEND" is executed asynchronously, you must keep the data in the send area consistent until the DONE parameter or the ERROR parameter changes to the value "1".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Description |
| --- | --- | --- |
| 0 | 0000 | Send job completed without error. |
| 0 | 7000 | No job processing active. |
| 0 | 7001 | Start of job execution, data is being sent.  When processing this job, the operating system accesses the data in the DATA send area. |
| 0 | 7002 | Job executing (REQ irrelevant).  When processing this job, the operating system accesses the data in the DATA send area. |
| 1 | 8085 | - The LEN parameter is larger than the highest permitted value.   For S7-1200: 8192; for S7-1500 (TCP): 65536; for S7-1500 (FDL): 240 / 236 - DATA and LEN parameters both have the value "0". |
| 1 | 8086 | The ID parameter is outside the permitted address range. |
| 1 | 8088 | The LEN parameter is greater than the area specified in DATA. |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is being terminated. Transfer via this connection is not possible. - The interface is being re-initialized. |
| 1 | 80B1 | You changed the DATA parameter before the current job finished. |
| 1 | 80B3 | The protocol variant (ConnectionType parameter in the connection description) is set to UDP. Use the instruction "TUSEND" with a UDP connection. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority group. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established to the partner at this time. - The interface is receiving new parameter settings or the connection is being established. - Only for FDL / PROFIBUS: Temporarily no receive resource is available at the connection partner. The connection partner is not ready to receive. - The R/H system is in the SYNCUP system state or there is a primary-backup switchover. The connection is closed. Processing of TSEND is stopped. |
| 1 | 80C5 | - Connection terminated by the communication partner. - LSAP of the remote connection partner is not released |
| 1 | 80C6 | Network error:  - Remote partner cannot be reached. - Physical interruption on PROFIBUS |
| 1 | 80C7 | Execution timeout. |
| 1 | 80EE | Handshake not yet completed |
| 1 | xxyy, xx &gt; 80 | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Example

You can find the example here: [Program example for TCON, TDISCON, TSEND &amp; TRCV](#program-example-for-tcon-tdiscon-tsend-trcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[TSEND: Send data via communication connection (S7-1200)](#tsend-send-data-via-communication-connection-s7-1200)

### TRCV: Receive data via communication connection (S7-1200, S7-1500)

This section contains information on the following topics:

- [TRCV: Receive data via communication connection (S7-1200)](#trcv-receive-data-via-communication-connection-s7-1200)
- [TRCV: Receive data via communication connection (S7-1200, S7-1500)](#trcv-receive-data-via-communication-connection-s7-1200-s7-1500-1)

#### TRCV: Receive data via communication connection (S7-1200)

##### Description

The following description of the "TRCV" instruction is valid for the CPU S7-1200 up to version 3.0.

You use the "TRCV" instruction to receive data over an existing communication connection. "TRCV" executes asynchronously.

Receipt of data is enabled when the EN_R parameter is set to the value "1". The received data is entered in a receive area. You specify the length of the receive area either with the LEN parameter (if LEN &lt;&gt; 0) or with the length information of the DATA parameter (if LEN = 0), depending on the protocol variant being used.

While data is being received, you cannot make changes to the DATA parameter or the defined receive area to ensure consistency of the received data.

After successful receipt of data, the NDR parameter is set to the value "1". You can query the amount of data actually received at the RCVD_LEN parameter.

##### Receive modes of "TRCV"

The following table shows how the received data is entered in the receive area.

| Protocol variant | Availability of data in the receive area | connection_type* parameter of the connection description | Parameter LEN |
| --- | --- | --- | --- |
| TCP  (Ad-hoc mode) | If NDR is set, at least one data byte is available. | Hexadecimal value: B#16#11  Integer value: 17 | 0 |
| TCP   (Receipt of data with specified length) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#11  Integer value: 17 | 1 to 8192 |
| ISO on TCP  (Message-oriented data transfer) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#12  Integer value: 18 | - 1 to 1452, if a CP is used. - 1 to 8192, if no CP is used. |
| * See "[Connection parameters with structure according to TCON_Param](Configuring%20devices%20and%20networks.md#connection-parameters-with-structure-according-to-tcon_param-s7-1200-s7-1500-s7-1500t)". |  |  |  |

##### TCP (Ad-hoc mode)

The ad-hoc mode is only available with the TCP protocol variant. You use the ad-hoc mode to receive data with dynamic length with the "TRCV" instruction.

You set ad-hoc mode by assigning the value "0" to the LEN parameter.

Immediately after receiving a data block, the "TRCV" instruction transfers it to the receive area and sets NDR. RCVD_LEN contains information on the number of data bytes contained in this data block. The lowest possible value of RCVD_LEN is 1.

All data types can be used for data blocks with standard access when you use ad-hoc mode. Only ARRAY of BYTE or data types with a length of 8 bits can be used for data blocks with optimized access (e.g., CHAR, USINT, SINT, etc.).

##### TCP (Receipt of data with specified length)

For receipt of data with a specified length, enter the length of the data at the LEN parameter. The data receipt is not complete until the length of data specified at the LEN parameter has been completely received. Only then is the data available in the receive area (DATA parameter). The receipt of data is signaled by the NDR output parameter. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

##### ISO on TCP (Message-oriented data transfer)

Complete message blocks are sent via a connection with the protocol variant ISO on TCP; these are recognized as such by the recipient. When using ISO on TCP, "TRCV" signals data receipt as soon as the message block has been completely received. The receive area is defined by the LEN and DATA parameters. If the receive buffer (DATA parameter) is too small for the sent data, "TRCV" signals an error. The successful receipt of data is signaled by the NDR output parameter. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

##### Parameter

The following table shows the parameters of the "TRCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Receive enable |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the connection established with "[TCON](#tcon-establish-communication-connection-s7-1200)".  Value range: W#16#0001 (1) to W#16#0FFF (4095) |
| LEN | Input | UINT | I, Q, M, D, L or constant | Length of the receive area in bytes (hidden).   If you use a memory area with optimized access at the DATA parameter, the LEN parameter must have the value "0". |
| DATA | InOut | VARIANT | I, Q, M, D | Pointer to the receive area  When transferring structures, the structures must be identical at the sending and receiving end. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter (New Data Received):  - 0: Job not yet started or still in progress - 1: Job completed without error |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: No error. - 1: An error occurred during execution of the instruction.   Detailed information is output via the STATUS parameter. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter:  Output of status and error information. |
| RCVD_LEN | Output | UINT | I, Q, M, D, L | Amount of data actually received in bytes |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### LEN, DATA and RCVD_LEN parameters

- If LEN = 0, the received data is saved in the receive area specified at the DATA parameter. The number of bytes received is indicated at the RCVD_LEN parameter.

  With LEN = 0 (default setting of the LEN parameter), the length of the data to be received is defined by the DATA parameter. It is recommended that the receive area (DATA parameter) has the same size as the data to be transmitted by TSEND.

  If LEN has the value 0 and the sent data was transferred in segments that are smaller than the DATA receive area, the following applies. It is recommended to keep EN_R set until the associated TSEND instruction has sent all data. STATUS shows the value 7002 as long as the size of the data sent by TSEND is not equal to the size of the DATA receive area. EN_R must be set until the amount of the received data is equal to the size of the DATA receive area. If you pulse EN_R, you must do so until BUSY=0 or ERROR &lt;&gt; 0.

  The data in the DATA receive area is only valid when BUSY has the value 0.
- If the length specified at the LEN parameter is greater than the length of the data received at the DATA parameter, the error code 8088 is output at the STATUS parameter (see description of the STATUS) parameter in the following.
- If a structure (Struct) is referenced via the DATA parameter, LEN can be shorter than the structure. In this case, only the data up to the length of the LEN parameter is transferred.
- If the DATA parameter references a data block with optimized access, the LEN parameter must be set to "0".
- If a STRING data type is referenced via the DATA parameter, the length specified at the LEN parameter must be 0 or &gt;=2 (LEN = 1 is not permitted).
- If a WSTRING data type is referenced via the DATA parameter, the length specified at the LEN parameter must be 0 or &gt;=5.

##### BUSY, NDR and ERROR parameters

You can check the status of the job with the BUSY, NDR, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the NDR parameter, you can check whether or not a job executed successfully. The ERROR parameter is set when errors occurred during execution of TRCV. The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, NDR and ERROR parameters:

| BUSY | NDR | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

> **Note**
>
> Because "TRCV" is executed asynchronously, the data in the receive area is only consistent when the NDR parameter is set to the value "1".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Job completed successfully. The current length of the received data is output at the RCVD_LEN parameter. |
| 0 | 7000 | Block not ready to receive. |
| 0 | 7001 | Block is ready to receive, receive job was activated. |
| 0 | 7002 | Interim call, the receive job is executing.  Note: While the job is being processed, data is written to the receive area. Access to the receive area during this time may provide inconsistent data. |
| 1 | 8085 | - The LEN parameter is larger than the highest permitted value. - The value of the LEN or DATA parameter was changed after the first call. - Both LEN parameters and the DATA parameter have the value "0" or LEN is longer than the maximum permitted value (65536). |
| 1 | 8086 | The ID parameter is outside the permitted address range (1 .. 0x0FFF). |
| 1 | 8088 | - Receive area is too small. - The value at the LEN parameter is larger than the receive area set at the DATA parameter. |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is being terminated. Receive job over this connection is not possible. - The connection is being re-initialized. |
| 1 | 80B3 | The protocol variant (connection_type parameter in the connection description) is set to UDP. Use the instruction "TURCV" with a UDP connection. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority group. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established to the partner at this time. - The interface is receiving new parameter settings or the connection is being established. |
| 1 | 80C5 | The remote partner has terminated the connection. |
| 1 | 80C6 | The remote partner cannot be reached (network error). |
| 1 | 80C7 | Execution timeout. |
| 1 | 80C9 | The length of the receive area is smaller than the length of the sent data. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### TRCV: Receive data via communication connection (S7-1200, S7-1500)

##### Description

The following description of the "TRCV" instruction is valid for:

- Ethernet

  CPU S7-1200 with firmware version ≥ V4.0 and CPU S7-1500
- PROFIBUS

  FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL

You use the "TRCV" instruction to receive data over an existing communication connection. "TRCV" executes asynchronously.

Receipt of data is enabled when the EN_R parameter is set to the value "1". The received data is entered in a receive area. You specify the length of the receive area either with the LEN parameter (if LEN &lt;&gt; 0) or with the length information of the DATA parameter (if LEN = 0), depending on the protocol variant being used.

While data is being received, you cannot make changes to the DATA parameter or the defined receive area to ensure consistency of the received data.

After successful receipt of data, the NDR parameter is set to the value "1". You can query the amount of data actually received at the RCVD_LEN parameter.

##### Receive modes of "TRCV"

The following table shows how the received data is entered in the receive area.

| Protocol variant | Parameter ADHOC | Availability of data in the receive area | connection_type parameter of the connection description | Parameter LEN |
| --- | --- | --- | --- | --- |
| TCP  (Ad-hoc mode) | 1 (ad-hoc activated) | If NDR is set, at least one data byte is available. | Hexadecimal value: B#16#11  Integer value: 17 | As much data will be read as is currently available; not exceeding the data length specified by LEN.  LEN = 0 (recommended): Length of the receive area referenced by DATA |
| TCP   (Receipt of data with specified length) | 0 (ad-hoc deactivated) | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#11  Integer value: 17 | - S7-1200: 1 to 8192 - S7-1500: 1 to 65536 |
| ISO on TCP  (Message-oriented data transfer) | - | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#12  Integer value: 18 | - S7-1200: 1 to 8192 - S7-1500: 1 to 65536 |
| FDL | - | The data is available as soon as the data length specified at the LEN parameter has been fully received. | Hexadecimal value: B#16#15  Decimal: 21 | 1 to 240 |

##### TCP (Ad-hoc mode)

The ad-hoc mode is only available with the TCP protocol variant. You use the ad-hoc mode to receive data with dynamic length with the "TRCV" instruction.

You set ad-hoc mode by assigning the value "1" to the ADHOC parameter.

Immediately after receiving a data block, the "TRCV" instruction transfers it to the receive area and sets NDR. RCVD_LEN contains information on the number of data bytes contained in this data block. The lowest possible value of RCVD_LEN is 1.

All data types can be used for data blocks with standard access when you use ad-hoc mode.

However, for data blocks with optimized access, the permitted data types depend on the CPU type:

- With S7-1200 CPUs only ARRAY of BYTE or data types with a length of 8 bits can be used for data blocks with optimized access (e.g., CHAR, USINT, SINT, etc.).
- With S7-1500 CPUs, all data types can be used.

##### TCP (Receipt of data with specified length)

Assign the value "0" to the ADHOC parameter for receipt of data with specified length. If ad-hoc mode is disabled, the data reception is not complete until the length of data specified at the LEN parameter has been completely received. Only then is the data available in the receive area (DATA parameter). The successful receipt of data is signaled by the NDR output parameter. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

##### ISO on TCP (Message-oriented data transfer)

Complete message blocks are sent via a connection with the protocol variant ISO on TCP; these are recognized as such by the recipient. When using ISO on TCP, "TRCV" signals data receipt as soon as the message block has been completely received. The receive area is defined by the LEN and DATA parameters. If the receive buffer (DATA parameter) is too small for the sent data, "TRCV" signals an error. The successful receipt of data is signaled by the NDR output parameter. The actually received data length in bytes at the RCVD_LEN parameter corresponds to the data length at the LEN parameter after receipt.

##### Parameter

The following table shows the parameters of the "TRCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Receive enable |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the connection established with "TCON".  Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Length of the receive area in bytes (hidden)  Maximum value for S7-1200: 8192; maximum value for S7-1500: 65536; maximum value for CM 1542‑5 (FDL): 240.  If you use a receive area with optimized access at the DATA parameter, the LEN parameter must have the value "0". |
| ADHOC | Input | BOOL | I, Q, M, D, L or constant | Use ad-hoc mode for the TCP protocol variant (hidden).  ADHOC must have the value FALSE if no TCP protocol is used. |
| DATA | InOut | VARIANT | I, Q, M, D, L | Pointer to the receive area  When transferring structures, the structures must be identical at the sending and receiving end. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter (New Data Received):  - 0: Job not yet started or still in progress - 1: New data received |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |
| RCVD_LEN | Output | UDINT | I, Q, M, D, L | Amount of data actually received in bytes |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### LEN, DATA and RCVD_LEN parameters

- If LEN = 0, the received data is saved in the receive area specified at the DATA parameter. The number of bytes received is indicated at the RCVD_LEN parameter.

  With LEN = 0 (default setting of the LEN parameter), the length of the data to be received is defined by the DATA parameter. It is recommended that the receive area (DATA parameter) has the same size as the data to be transmitted by TSEND.

  If LEN has the value 0 and the sent data was transferred in segments that are smaller than the DATA receive area, the following applies. It is recommended to keep EN_R set until the associated TSEND instruction has sent all data. STATUS shows the value 7002 as long as the size of the data sent by TSEND is not equal to the size of the DATA receive area. EN_R must be set until the amount of the received data is equal to the size of the DATA receive area. If you pulse EN_R, you must do so until BUSY=0 or ERROR &lt;&gt; 0.

  The data in the DATA receive area is only valid when BUSY has the value 0.
- If the length specified at the LEN parameter is greater than the length of the data received at the DATA parameter, the error code 8088 is output at the STATUS parameter (see description of the STATUS) parameter in the following.
- If a structure (Struct) is referenced via the DATA parameter, LEN can be shorter than the structure. In this case, only the data up to the length of the LEN parameter is transferred.
- If the DATA parameter references a data block with optimized access, the LEN parameter must be set to "0". If the length of the data does not match for elementary data types, the data will not be received and the error code 8088 is output at the STATUS parameter.
- If a STRING data type is referenced via the DATA parameter, the length specified at the LEN parameter must be 0 or &gt;=2 (LEN = 1 is not permitted).
- If a WSTRING data type is referenced via the DATA parameter, the length specified at the LEN parameter must be 0 or &gt;=5.

##### BUSY, NDR and ERROR parameters

You can check the status of the job with the BUSY, NDR, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the NDR parameter, you can check whether or not a job executed successfully. The ERROR parameter is set when errors occurred during execution of TRCV. The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, NDR and ERROR parameters:

| BUSY | NDR | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

> **Note**
>
> Because "TRCV" is executed asynchronously, the data in the receive area is only consistent when the NDR parameter is set to the value "1".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Job completed successfully. The current length of the received data is output at the RCVD_LEN parameter. |
| 0 | 7000 | Block not ready to receive. |
| 0 | 7001 | Block is ready to receive, receive job was activated. |
| 0 | 7002 | Interim call, the receive job is executing.  Note: While the job is being processed, data is written to the receive area. Access to the receive area during this time may provide inconsistent data. |
| 1 | 8085 | - The LEN parameter is greater than the maximum permissible value (for S7-1200: 8192 bytes, for S7-1500: 65536 bytes). - The value of the LEN or DATA parameter was changed after the first call. - Both LEN parameters and the DATA parameter have the value "0" or LEN is longer than the maximum permissible value (for S7-1200: 8192 bytes, for S7-1500: 65536 bytes). |
| 1 | 8086 | The ID parameter is outside the valid range. |
| 1 | 8088 | - Receive area is too small. - The value at the LEN parameter is larger than the receive area set at the DATA parameter. |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is being terminated. Receive job over this connection is not possible. - The connection is being re-initialized. |
| 1 | 80B1 | You changed the DATA parameter before the current job finished. |
| 1 | 80B3 | The protocol variant (connection_type parameter in the connection description) is set to UDP. Use the instruction "TURCV" with a UDP connection. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority group. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established to the partner at this time. - The interface is receiving new parameter settings or the connection is being established. - The R/H system is in the SYNCUP system state or there is a primary-backup switchover. The connection is closed. Processing of TRCV is stopped. |
| 1 | 80C5 | The remote partner has terminated the connection. |
| 1 | 80C6 | The remote partner cannot be reached (network error). |
| 1 | 80C7 | Execution timeout. |
| 1 | 80C9 | The length of the receive area is smaller than the length of the sent data. |
| 1 | 80EE | Handshake not yet completed |
| 1 | xxyy, xx &gt; 80 | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Example

You can find the example here: [Program example for TCON, TDISCON, TSEND &amp; TRCV](#program-example-for-tcon-tdiscon-tsend-trcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Principle of operation of connection-oriented protocols (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#principle-of-operation-of-connection-oriented-protocols-s7-1200-s7-1500-s7-1500t)
  
[Basics of Open User Communication (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#basics-of-open-user-communication-s7-1200-s7-1500-s7-1500t)
  
[TRCV: Receive data via communication connection (S7-1200)](#trcv-receive-data-via-communication-connection-s7-1200)
  
[TCON: Establish communication connection (S7-1200, S7-1500)](#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Program example for TCON, TDISCON, TSEND & TRCV (S7-1200, S7-1500)

#### Introduction

In the following example, you create a programmed connection between two CPUs of the S7-1500 series and send a data record from CPU 1 to CPU 2.

#### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. Their connection is not yet configured.

  ![Requirement](images/94530587531_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under Properties &gt; Protection ensures that read and write access is permitted for each CPU.

#### Program of CPU 1: Storage of data

For the data record, create the following PLC data type.

![Program of CPU 1: Storage of data](images/94531455371_DV_resource.Stream@PNG-de-DE.png)

For the data transfer, create the following data block ("SLI_plcDB_sendData_TSEND") based on the created PLC data type.

![Program of CPU 1: Storage of data](images/94531489803_DV_resource.Stream@PNG-de-DE.png)

To store the data, create a global data block ("SLI_gDB_TSEND") with the following structures and tags.

![Program of CPU 1: Storage of data](images/94531385611_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 1: Interconnect parameters

Create the FB "SLI_FB_TSEND" Create the following local tags in it.

![Program of CPU 1: Interconnect parameters](images/94531446539_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "TCON" as follows:

![Program of CPU 1: Interconnect parameters](images/94531498635_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of TCON, save the status as follows.

![Program of CPU 1: Interconnect parameters](images/94531507467_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: Interconnect the parameter of the instruction "TSEND" as follows:

![Program of CPU 1: Interconnect parameters](images/94531541899_DV_resource.Stream@PNG-de-DE.png)

**Network 4**: In case of error of TSEND, save the status as follows.

![Program of CPU 1: Interconnect parameters](images/94531601931_DV_resource.Stream@PNG-de-DE.png)

**Network 5**: Interconnect the parameter of the instruction "TDISCON" as follows:

![Program of CPU 1: Interconnect parameters](images/94531623563_DV_resource.Stream@PNG-de-DE.png)

**Network 6**: In case of error of TDISCON, save the status as follows.

![Program of CPU 1: Interconnect parameters](images/94531632395_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 1: Configuration of TCON

To interconnect the input parameter CONNECT, open the wizard of the "TCON" instruction with its Properties &gt; Configuration.

Make the following settings for the configuration of TCON:

| Input field | Entry |
| --- | --- |
| End point | Select a CPU for sender and receiver using the drop-down list.   Interface, subnet and address are entered automatically. |
| Connection data | Use the drop-down list and the selection "New" to create one data block per CPU.   This data block is required for storing the connection data. The name of the data block can be freely selected.   The active connection establishment is enabled for CPU 1 (local CPU). |
| Connection type | Select the entry "ISO-on-TCP".   This means an Ethernet connection with the "ISO-on-TCP" protocol is used for connection setup. |
| Connection ID | You enter a freely selected connection ID for the communication connection.   The connection ID must not already be assigned in the project. Ensure that the value matches the value of the "connectionID" tag that is used. |
| TSAP ID | The address details are automatically entered during the selection of the connection type "ISO-on-TCP". |

![Program of CPU 1: Configuration of TCON](images/94531641227_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 2: Storage of data

For the data record, create the following PLC data type.

![Program of CPU 2: Storage of data](images/94531455371_DV_resource.Stream@PNG-de-DE.png)

For the data transfer, create the following data block ("SLI_plcDB_rcvData_TRCV") based on the created PLC data type.

![Program of CPU 2: Storage of data](images/94531101323_DV_resource.Stream@PNG-de-DE.png)

To store the data, create a global data block ("SLI_gDB_TRCV") with the following structures and tags.

![Program of CPU 2: Storage of data](images/94530596363_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 2: Interconnect parameters

Create the FB "SLI_FB_TRCV" Create the following local tags in it.

![Program of CPU 2: Interconnect parameters](images/94531079691_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "TCON" as follows:

![Program of CPU 2: Interconnect parameters](images/94531170187_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of TCON, save the status as follows.

![Program of CPU 2: Interconnect parameters](images/94531204619_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: Interconnect the parameter of the instruction "TRCV" as follows:

![Program of CPU 2: Interconnect parameters](images/94531226251_DV_resource.Stream@PNG-de-DE.png)

**Network 4**: In case of error of TRCV, save the status as follows.

![Program of CPU 2: Interconnect parameters](images/94531235083_DV_resource.Stream@PNG-de-DE.png)

**Network 5**: Interconnect the parameter of the instruction "TDISCON" as follows:

![Program of CPU 2: Interconnect parameters](images/94531256715_DV_resource.Stream@PNG-de-DE.png)

**Network 6**: In case of error of TDISCON, save the status as follows.

![Program of CPU 2: Interconnect parameters](images/94531316747_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 2: Configuration of TCON

You make the following settings for the connection of CPU 2 / TCON according to the example of CPU 1 / TCON:

> **Note**
>
> **Connection data**
>
> By configuring CPU 1 / TCON, you have already created a data block ("PLC_Tsend_Connection_DB", "PLC_Trcv_Connection_DB") with the stored connection data for each CPU. Instead of creating new data blocks and entering the connection data, you can simply use the created data blocks ("PLC_Tsend_Connection_DB", "PLC_Trcv_Connection_DB").
>
> For the created data blocks to be available for selection, they must still be available in the project tree under Program blocks &gt; System blocks.

![Program of CPU 2: Configuration of TCON](images/94531325579_DV_resource.Stream@PNG-de-DE.png)

#### Procedure for establishing connection

Observe the order of the action steps:

1. Change the parameter REQ to "TRUE" for CPU 2 / TCON.

2. Change the parameter REQ to "TRUE" for CPU 1 / TCON.

3. Change the parameter REQ to "FALSE" for CPU 2 / TCON.

4. Change the parameter REQ to "FALSE" for CPU 1 / TCON.

#### Procedure for terminating connection

Observe the order of the action steps:

1. Change the parameter REQ to "TRUE" for CPU 1 / TDISCON.

2. Change the parameter REQ to "TRUE" for CPU 2 / TDISCON.

3. Change the parameter REQ to "FALSE" for CPU 1 / TDISCON.

4. Change the parameter REQ to "FALSE" for CPU 2 / TDISCON.

#### Behavior of CPU 1

**Network 1 (TCON):**

When the input parameter REQ ("TCON.start") supplies the signal state "TRUE", the "TCON" instruction is started. For multiple calls, the "TCON" instruction creates a communication connection to the partner CPU. To do this, the connection data is retrieved with the input parameter CONNECT (data block "PLC_Trcv_Connection_DB").

Successful connection setup is indicated by the output parameter DONE ("#doneCON") with the signal state "TRUE" and the output parameter STATUS ("TCON.status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "TCON.done". Reset the success status of any previous connection termination ("TDISCON.done").

The output parameter ERROR ("TCON.error") or the tag "TCON.memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 1](images/94531407243_DV_resource.Stream@PNG-de-DE.png)

**Network 2 (TCON):**

When TCON signals an error ("TCON.error" is "TRUE"), the reported status ("TCON.status") is stored permanently ("TCON.memErrStatus").

**Network 3 (TSEND):**

Based on the input parameter ID ("connectionID"), the "TSEND" instruction knows the communication connection to be used.

When the input parameter REQ ("TSEND.start") supplies the signal state "TRUE", the "TSEND" instruction is started. For multiple calls, the "TSEND" instruction transmits the data record detected at input parameter DATA ("SLI_plcDB_sendData_TSEND").

Successful transfer of the data record is indicated by the output parameter DONE ("#doneSEND") with the signal state "TRUE" and the output parameter STATUS ("TSEND.status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "TSEND.done".

The output parameter ERROR ("TSEND.error") or the tag "TSEND.memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 1](images/94531424907_DV_resource.Stream@PNG-de-DE.png)

**Network 4 (TSEND):**

When TSEND signals an error ("TSEND.error" is "TRUE"), the reported status ("TSEND.status") is stored permanently ("TSEND.memErrStatus").

**Network 5 (TDISCON):**

When the input parameter REQ ("TDISCON.start") supplies the signal state "TRUE", the "TDISCON" instruction is started. For multiple calls, the instruction "TDISCON" terminates the communication connection. The communication connection used at the input parameter ID ("connectionID") is retrieved for this purpose.

Successful connection termination is indicated by the output parameter DONE ("#doneDISC") with the signal state "TRUE" and the output parameter STATUS ("TDISCON.status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "TDISCON.done". Reset the success messages for connection setup ("TCON.done") and for data transfer ("TSEND.done").

The output parameter ERROR ("TDISCON.error") or the tag "TDISCON.memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 1](images/94531416075_DV_resource.Stream@PNG-de-DE.png)

**Network 6 (TDISCON):**

When TDISCON signals an error ("TDISCON.error" is "TRUE"), the reported status ("TDISCON.status") is stored permanently ("TDISCON.memErrStatus").

#### Behavior of CPU 2

For TCON and TDISCON, the behavior is the same as that for CPU 1.

![Behavior of CPU 2](images/94530950795_DV_resource.Stream@PNG-de-DE.png)

![Behavior of CPU 2](images/94531036427_DV_resource.Stream@PNG-de-DE.png)

**Network 3 (TRCV):**

Based on the input parameter ID ("connectionID"), the "TRCV" instruction knows the communication connection to be used.

When the input parameter EN_R ("TRCV.start") supplies the signal state "TRUE", the "TRCV" instruction is started. For multiple calls, the "TRCV" instruction receives the transmitted data record. The data record is detected at the input parameter DATA ("SLI_plcDB_rcvData_TRCV").

![Behavior of CPU 2](images/94531110155_DV_resource.Stream@PNG-de-DE.png)

The length in BYTE of the actually transmitted data record is detected with the output parameter LEN ("#length"). This value is only displayed during the success status. Then "0" is detected. Successful receipt of the data record is indicated by the output parameter DONE ("#doneRCV") with the signal state "TRUE" and the output parameter STATUS ("TRCV.status") with the value "0000".

Because the values of the output parameters are only displayed for the moment of their validity, do the following:

- Save the success status in the tag "TRCV.done"
- Save the length in BYTE in the tag "TRCV.readLength".

The output parameter ERROR ("TRCV.error") or the tag "TRCV.memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 2](images/94531045259_DV_resource.Stream@PNG-de-DE.png)

**Network 4 (TRCV):**

When TRCV signals an error ("TRCV.error" is "TRUE"), the reported status ("TRCV.status") is stored permanently ("TRCV.memErrStatus").

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[TCON: Establish communication connection (S7-1200, S7-1500)](#tcon-establish-communication-connection-s7-1200-s7-1500)
  
[TDISCON: Terminate communication connection (S7-1200, S7-1500)](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)
  
[TSEND: Send data via communication connection (S7-1200, S7-1500)](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)
  
[TRCV: Receive data via communication connection (S7-1200, S7-1500)](#trcv-receive-data-via-communication-connection-s7-1200-s7-1500-1)

### Sending and receiving data via Ethernet (UDP) or FDL (S7-1200, S7-1500)

This section contains information on the following topics:

- [TUSEND: Sending data (S7-1200, S7-1500)](#tusend-sending-data-s7-1200-s7-1500)
- [TURCV: Receiving data (S7-1200, S7-1500)](#turcv-receiving-data-s7-1200-s7-1500)
- [Addressing the remote partner via TADDR_Param (S7-1200, S7-1500)](#addressing-the-remote-partner-via-taddr_param-s7-1200-s7-1500)
- [Addressing the remote partner via TADDR_SEND_QDN and TADDR_RCV_IP (S7-1500)](#addressing-the-remote-partner-via-taddr_send_qdn-and-taddr_rcv_ip-s7-1500)
- [Program example for TUSEND &amp; TURCV (S7-1200, S7-1500)](#program-example-for-tusend-turcv-s7-1200-s7-1500)

#### TUSEND: Sending data (S7-1200, S7-1500)

##### Description

TUSEND supports data transfer via UDP (for S7-1500-CPUs as of firmware version V2.0 and higher via the integrated PROFINET interfaces also as multicast communication) and via FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0 with the system data type TCON_FDL.

The "TUSEND" instruction sends data to the communication partner addressed by the ADDR parameter.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Data transfer via UDP**  When transferring data with UDP according to RFC 768, the data is transferred to the partner without acknowledgement and therefore non-securely. This means that data can be lost without this being indicated by the block.  The risk of undetected transmission errors increases significantly when more than 1472 bytes are transferred. |  |

> **Note**
>
> For sequential send operations to different partners, you only need to adjust the ADDR parameter when calling "TUSEND". You do not need to call the "[TCON](#tcon-establish-communication-connection-s7-1200)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instructions again. The UDP port must be set up at the specific partner in order for this partner to receive data.

##### Sending more than 1472 bytes

As of firmware version V2.5 of the S7-1500 CPUs, you can send up to 2048 bytes of data over UDP rather than just 1472 bytes if you are using Unicast or Multicast.

If you send more than 1472 bytes, you must check that the recipient supports more than 1472 bytes. If this is not the case, the failure of receipt will not be indicated at the sender end.

##### Functional description

The "TUSEND" instruction works asynchronously, which means its job processing extends over multiple calls. Create a rising edge at the REQ parameter to establish a connection once again.

The output parameters BUSY, DONE, ERROR and STATUS indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500).

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can determine the current status of "TUSEND" or when the send process is concluded.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | FALSE | FALSE | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TUSEND", make sure the data in the send area remains consistent until the DONE parameter or the ERROR parameter has the value TRUE.

##### Parameter

The following table shows the parameters of the "TUSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter REQUEST starts the send job on a rising edge.  The data is transferred from the area specified by DATA and LEN. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the associated connection between the user program and the communication layer of the operating system. ID must be identical to the associated parameter ID in the local connection description with the .TCON instruction:   Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Number of bytes to be sent with the job  Value range for Ethernet/UDP: 1 to 1472 (as of firmware version V2.5 of S7-1500 CPUs for Unicast or Multicast: 1 to 2048)  For FDL connections of the CM 1542‑5, the maximum length is 240 bytes. In this regard, note the maximum lengths that can be processed by the connection partner. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job executed without errors. This value is only displayed for one cycle. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet complete. A new job cannot be triggered. - BUSY = 0: Job is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR = 1: An error occurred during processing. STATUS supplies detailed information on the type of error |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Error information |
| DATA | InOut | VARIANT | I, Q, M, D | Send area, contains address and length  The address refers to:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   When transferring structures, the structures must be identical at the sending and receiving end. |
| ADDR | InOut | VARIANT | D | Address information of the communication partner  See also: [Addressing the remote partner via TADDR_Param](#addressing-the-remote-partner-via-taddr_param-s7-1200-s7-1500) and [Addressing the remote partner via TADDR_SEND_QDN and TADDR_RCV_IP](#addressing-the-remote-partner-via-taddr_send_qdn-and-taddr_rcv_ip-s7-1500)   and [Connection parameters to TCON_FDL](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_fdl-s7-1200-s7-1500) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Send job completed without error |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start of job processing, data being sent  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 0 | 7002 | Intermediate call (REQ irrelevant), job is being processed  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 1 | 8085 | The LEN parameter has the value "0" or is greater than the highest permitted value. |
| 1 | 8086 | The ID parameter is not in the permitted value range. |
| 0 | 8088 | The LEN parameter is greater than the memory area specified in DATA. |
| 1 | 8089 | The parameter ADDR does not point to a data block with the structure TADDR_Param or TADDR_SEND_QDN. |
| 1 | 80A1 | Communication error:  - The specified connection between user program and communication layer of the operating system has not yet been established. - The specified connection between the user program and the communication layer of the operating system is currently being terminated. Transmission over this connection is not possible. - The interface is being reinitialized. |
| 1 | 80B1 | You changed the DATA parameter before the current job finished. |
| 1 | 80A4 | IP address (at the ADDR parameter) of the remote connection end point is invalid; it might correspond to the local partner's own IP address. |
| 1 | 80B3 | - The protocol variant (connection_type parameter in the connection description) is not set to UDP. Use "[TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)". - Parameter ADDR: Invalid information for port no. |
| 1 | 80B7 | The length of the structure referenced by the parameter ADDR is not 8 bytes. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The remote partner is not reachable. - The connection between the user program and the communication layer of the operating system cannot be established at this time. - New parameter settings are being assigned to the interface. - Only for FDL / PROFIBUS: Temporarily no receive resource is available at the connection partner. The connection partner is not ready to receive. - The R/H system is in the SYNCUP system state or there is a primary-backup switchover. The connection is closed. Processing of TUSEND is stopped. |
| 1 | 80C5 | - Connection terminated by the communication partner. - LSAP of the remote connection partner is not released |
| 1 | 80C6 | Network error:  - Remote partner cannot be reached. - Physical interruption on PROFIBUS |
| 1 | 80C7 | Execution timeout. |
| 1 | 80D3 | The fully qualified domain name could not be resolved. Possible causes:  - The DNS server is not reachable, for example, because it has been shut down or the remote port is not reachable. - An error occurred during communication with the DNS server. - The DNS server returned a valid DNS answer, but the answer contained no IPv4 address. |
| 1 | 80EA | DTLS (UDP) protocol is not supported |
| 1 | xxyy, xx &gt; 80 | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Example

You can find the example here: [Program example for TUSEND &amp; TURCV](#program-example-for-tusend-turcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)

#### TURCV: Receiving data (S7-1200, S7-1500)

##### Description

The "TURCV" instruction receives data via UDP (for S7-1500-CPUs as of firmware version V2.0 and higher via the integrated PROFINET interfaces also as multicast communication) and via FDL connections of the S7‑1500 with CM 1542‑5 as of V2.0. After successful completion of "TURCV", the ADDR parameter will show you the address of the remote partner (the sender).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unsecured data transfer**  When transferring data with UDP according to RFC 768, the data is transferred to the remote partner without acknowledgement and is therefore unreliable. This means that data can be lost without this being indicated by the block. |  |

##### Receipt of more than 1472 bytes

As of firmware version V2.5 of the S7-1500 CPUs, you can receive up to 2048 bytes of data via UDP rather than 1472 bytes as before.

However, if your receiving module supports a max. of 1472 bytes and your sending module transfers more than 1472 bytes, TURCV returns a value of W#16#8085 or W#16#80C9 in the STATUS parameter.

##### Functional description

"TURCV" is an instruction that works asynchronously, which means its job processing extends over multiple calls. You start the receive job by calling "TURCV" with EN_R = 1.

The output parameters BUSY, DONE, ERROR and STATUS indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500).

The following table shows the relationship between BUSY, NDR and ERROR. Using this table, you can determine the current status of TURCV or when the receive process is concluded.

| BUSY | NDR | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | FALSE | FALSE | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. New data was received. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TURCV", the data in the receive area is only consistent when the NDR parameter has the value TRUE.

##### Parameter

The following table shows the parameters of the "TURCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Control parameter enabled to receive  When EN_R = 1, "TURCV" is ready to receive. The receive job is being processed. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the associated connection between the user program and the communication layer of the operating system. ID must be identical to the associated ID parameter in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | UDINT | I, Q, M, D, L or constant | Length of the receive area in bytes: 0 (recommended) or 1 to 1472 (as of firmware version V2.5 of S7-1500 CPUs for Unicast or Multicast: 1 to 2048)  Maximum value for CM 1542‑5 (FDL): 240 |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:  - NDR = 0: Job not yet started or still running. - NDR = 1: Job successfully completed |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: An error occurred during processing. STATUS supplies detailed information on the type of error |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet complete. A new job cannot be triggered. - BUSY = 0: Job is complete. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS: Error information |
| RCVD_LEN | Output | UDINT | I, Q, M, D, L | Amount of data actually received in bytes |
| DATA | InOut | VARIANT | I, Q, M, D, L | Receive area  The address references:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   When transferring structures, the structures must be identical at the sending and receiving end. |
| ADDR | InOut | VARIANT | D | Address information of the remote partner  See also: [Addressing the remote partner via TADDR_Param](#addressing-the-remote-partner-via-taddr_param-s7-1200-s7-1500) and [Addressing the remote partner via TADDR_SEND_QDN and TADDR_RCV_IP](#addressing-the-remote-partner-via-taddr_send_qdn-and-taddr_rcv_ip-s7-1500) and [Connection parameters to TCON_FDL](Configuring%20devices%20and%20networks.md#connection-parameters-to-tcon_fdl-s7-1200-s7-1500) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### ERROR and STATUS parameters

| ERROR | STATUS* (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | New data was accepted. The current length of the received data is shown in RCVD_LEN. |
| 0 | 7000 | Block not ready to receive |
| 0 | 7001 | Block is ready to receive, receive job was activated |
| 0 | 7002 | Intermediate call, receive job being processed  Note: During this processing phase, "TURCV" writes data to the receive area. For this reason, an error could result in inconsistent data in the receive area. |
| 1 | 8085 | The LEN parameter is greater than the largest permitted value, or you changed the value of the LEN or DATA parameter since the first call |
| 1 | 8086 | The ID parameter is not in the permitted value range |
| 1 | 8088 | - Receive area is too small - Value in LEN is higher than the receive area specified by DATA |
| 1 | 8089 | The parameter ADDR does not point to a data block with the structure TADDR_Param or TADDR_RCV_IP. |
| 1 | 80A1 | Communication error:  - The specified connection between user program and communication layer of the operating system has not yet been established. - The specified connection between the user program and the communication layer of the operating system is currently being terminated. A receive job over this connection is not possible. - New parameter settings are being assigned to the interface. |
| 1 | 80B1 | You changed the DATA parameter before the current job finished. |
| 1 | 80B3 | The protocol variant (connection_type parameter in the connection description) is not set to UDP. Please use "[TRCV](#trcv-receive-data-via-communication-connection-s7-1200)". |
| 1 | 80B7 | The length at ADDR parameter does not correspond to 8 bytes. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - New parameter settings are being assigned to the interface. - The R/H system is in the SYNCUP system state or there is a primary-backup switchover. The connection is closed. Processing of TURCV is stopped. |
| 1 | 80C5 | The remote partner has terminated the connection. |
| 1 | 80C7 | Execution timeout. |
| 1 | 80C9 | With RFC1006 / UDP: The received data is longer than expected (size of receive buffer exceeded). |
| 1 | 80EA | DTLS (UDP) protocol is not supported |
| 1 | xxyy, xx &gt; 80 | For general error information, refer to [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

##### Example

You can find the example here: [Program example for TUSEND &amp; TURCV](#program-example-for-tusend-turcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[TCON: Establish communication connection (S7-1200)](#tcon-establish-communication-connection-s7-1200)
  
[TDISCON: Terminate communication connection (S7-1200, S7-1500)](#tdiscon-terminate-communication-connection-s7-1200-s7-1500)
  
[GET_ERR_ID: Get error ID locally (S7-1200, S7-1500)](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500)

#### Addressing the remote partner via TADDR_Param (S7-1200, S7-1500)

##### Overview

When using a UDP connection, you can store the address information for the remote partner in the system data type TADDR_Param:

- With the "[TUSEND](#tusend-sending-data-s7-1200-s7-1500)" instruction, you transfer the address information of the recipient at the parameter ADDR via TADDR_Param.

  The stored address data of the remote partner are read from the system data type by the instruction.

  > **Note**
  >
  > **Supporting a limited broadcast**
  >
  > For S7-1500 CPUs as of firmware version V2.0, the following applies to the instruction "TUSEND": When addressing the remote partner via the "TADDR_Param" system data type, a limited broadcast (255.255.255.255 as the IP address of the remote partner) is supported with consistent compliance to IP routing rules. Accordingly, limited broadcasts are only sent over an interface through which a default router is accessible according to configuration.
  >
  > It is recommended to use of directed broadcast addresses because they - according to the IP standards - are not subject to this restriction.
- With the "[TURCV](#turcv-receiving-data-s7-1200-s7-1500)" instruction, you receive the address of the sender at the parameter ADDR via TADDR_Param.

  The address data is written by the instruction in the system data type.

##### Structure of the address information according to TADDR_Param

The system data type TADDR_Param contains the address information of the remote partner and consists of the IP address and the port number.

The system data type TADDR_Param has the following structure:

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 to 3 | rem_ip_addr | ARRAY [1..4] of USINT | B#16#00 ... | - IP address of the remote partner, e.g. 192.168.002.003:   - rem_ip_addr[1] = B#16#C0 (192)   - rem_ip_addr[2] = B#16#A8 (168)   - rem_ip_addr[3] = B#16#02 (002)   - rem_ip_addr[4] = B#16#03 (003)The IP address can be taken from the Devices &amp; networks view in the interface properties of the remote partner. As an alternative these are also displayed in the properties of the UDP connection under Address details. - Multicast address of an IPv4 multicast group (for the "TUSEND" instruction with S7-1500-CPUs as of firmware version V2.0 and higher). |
| 4 to 5 | rem_port_nr | UINT | B#16#00 ... | Remote port-number (for possible values, see: [Assignment of port numbers](Configuring%20devices%20and%20networks.md#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)):  - rem_port_nr[1] = high byte of the port no. in hexadecimal notation - rem_port_nr[2] = low byte of port no. in hexadecimal notation   The port number can be taken from the Devices &amp; networks view in the UDP connection properties. The port number is indicated under Address details as a decimal value.  Example: Port number = 2000 (decimal) / W#16#07D0 (hexadecimal)  - rem_port_nr[1] = 07 (high byte) - rem_port_nr[2] = D0 (low byte) |
| 6 to 7 | reserved | WORD | B#16#00 ... | Not used. Leave the value "0" at this parameter. |

##### Creating TADDR_Param in a data block

You have the following options for creating TADDR_Param:

- Create a new data block and select TADDR_Param as type in the dialog "Add new data block".
- Open an existing data block create a new tag and enter in the column Data type TADDR_Param.

A data block can contain several system data types TADDR_Param.

#### Addressing the remote partner via TADDR_SEND_QDN and TADDR_RCV_IP (S7-1500)

##### Overview

For S7-1500 CPUs as of firmware version V2.0, you can address the recipient with its fully qualified domain name when sending data via UDP. With the instruction TUSEND at the parameter ADDR, you hereby reference a structure of the type TADDR_SEND_QDN.

The receiver can return an IPv4 or an IPv6 address. With the TURCV instruction at the ADDR parameter, you therefore reference a structure of the type TADDR_RCV_IP. Only this can include both IP address types.

##### Structure of the address information according to TADDR_SEND_QDN

The system data type TADDR_SEND_QDN contains the address information of the remote partner (of the receiver) and consists of the fully qualified domain name and port number.

It has the following structure:

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 to 255 | RemoteQDN | ARRAY of STRING[1..254] | - | Fully qualified domain name of the partner end point, which must finish with "."  Please note that the name including the concluding period must not exceed 254 characters in a SIMATIC environment. |
| 256 to 257 | RemotePort | UINT | B#16#00 ... | Remote port-number (for possible values, see: [Assignment of port numbers](Configuring%20devices%20and%20networks.md#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)):  - RemotePort[1] = high byte of the port no. in hexadecimal notation - RemotePort[2] = low byte of port no. in hexadecimal notation   Example: Port number = 2000 (decimal) / W#16#07D0 (hexadecimal)  - RemotePort[1] = 07 (high byte) - RemotePort[2] = D0 (low byte) |
| 258 to 259 | reserved | WORD | W#16#00 | Not used. Leave the value "0" at this parameter. |

> **Note**
>
> **Runtime of the instruction TUSEND**
>
> With each call of TUSEND, the fully qualified domain name is resolved in the IP address. As a result, the execution time of TUSEND is longer than if you address the receiver directly via its IPv4 address.

##### Structure of the address information according to TADDR_RCV_IP

The system data type TADDR_RCV_IP contains the address information of the remote partner (of the sender) and consists of the IP address, the port number and the information on whether the IP address is an IPv4 or IPv6 address.

It has the following structure:

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 to 15 | RemoteAddress | ARRAY [1..16] of BYTE | B#16#00 ... | IP address of the remote partner, e.g. for the IPv4 address 192.168.002.003:  - RemoteAddress[1] = B#16#C0 (192) - RemoteAddress[2] = B#16#A8 (168) - RemoteAddress[3] = B#16#02 (002) - RemoteAddress[4] = B#16#03 (003)   The following applies to the IPv6 address. |
| 16 to 17 | RemotePort | UINT | B#16#00 ... | Remote port-number (for possible values, see: [Assignment of port numbers](Configuring%20devices%20and%20networks.md#assignment-of-port-numbers-s7-1200-s7-1500-s7-1500t)):  - RemotePort[1] = high byte of the port no. in hexadecimal notation - RemotePort[2] = low byte of port no. in hexadecimal notation   Example: Port number = 2000 (decimal) / W#16#07D0 (hexadecimal)  - RemotePort[1] = 07 (high byte) - RemotePort[2] = D0 (low byte) |
| 18 | RemAddrType | BYTE | B#16#00 | Type of the remote address:  - B#16#03: IPv4 - B#16#04: IPv6 |
| 19 | reserved | BYTE | B#16#00 | Not used. Leave the value "0" at this parameter. |

#### Program example for TUSEND & TURCV (S7-1200, S7-1500)

##### Introduction

In the following example you create a configured UDP connection between two CPUs of the S7-1500 series. Transmit a data record from CPU1 to CPU2 using the instructions "TUSEND" and "TURCV".

##### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. A UDP connection is configured.

  ![Requirement](images/94531792907_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.

##### Program of CPU 1

For the data record, create the following PLC data type "TUSEND_User".

![Program of CPU 1](images/94532176523_DV_resource.Stream@PNG-de-DE.png)

For the data transfer, create the following data block ("SLI_plcDB_sendData_TUSEND") based on the PLC data type "TUSEND_User".

![Program of CPU 1](images/94532185355_DV_resource.Stream@PNG-de-DE.png)

For addressing the communication partner, create the following data block ("SLI_plcDB_taddr_param_TUSEND") based on the system data type "TADDR_Param.

![Program of CPU 1](images/94532206987_DV_resource.Stream@PNG-de-DE.png)

You can find the address date in the "Network view" under "Connections &gt; Properties &gt; Address details". The data of the CPU that had been selected previously are specified in the address details under "Local". In the following figure, CPU 1 "TUsend") is selected.

![Program of CPU 1](images/94531801739_DV_resource.Stream@PNG-de-DE.png)

To store the data, create a global data block ("SLI_gDB_TUSEND") with the following structures and tags.

![Program of CPU 1](images/94532082059_DV_resource.Stream@PNG-de-DE.png)

Create the FB "SLI_FB_TUSEND" Create the following local tags in it.

![Program of CPU 1](images/94725628043_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "TUSEND" as follows:

![Program of CPU 1](images/94532241419_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of TUSEND, save the status as follows.

![Program of CPU 1](images/94532288651_DV_resource.Stream@PNG-de-DE.png)

##### Program of CPU 2

For the data record, create the PLC data type "TUSEND_User" based on the example of CPU 1.

For receiving data, create the following data block ("SLI_plcDB_rcvData_TURCV") based on the created PLC data type ("TUSEND_User").

![Program of CPU 2](images/94532012299_DV_resource.Stream@PNG-de-DE.png)

For addressing the communication partner, create the following data block ("SLI_plcDB_taddr_param_TURCV") based on the system data type "TADDR_Param.

![Program of CPU 2](images/94532029963_DV_resource.Stream@PNG-de-DE.png)

To store the data, create a global data block ("SLI_gDB_TURCV") with the following structures and tags.

![Program of CPU 2](images/94531921803_DV_resource.Stream@PNG-de-DE.png)

Create the FB "SLI_FB_TURCV" Create the following local tags in it.

![Program of CPU 2](images/94531990667_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "TURCV" as follows:

![Program of CPU 2](images/94532064395_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of TURCV, save the status as follows.

![Program of CPU 2](images/94532073227_DV_resource.Stream@PNG-de-DE.png)

##### Assigning communication connection

The address parameters for the connection of the two CPUs must be uniform.

- In each case store the hexadecimal value of the hardware identifier of the configured UDP connection at the input parameter ID ("connectionID").

  You can find the hardware identifier in the "Network view" under "Connections".

  ![Assigning communication connection](images/94531848971_DV_resource.Stream@PNG-de-DE.png)

##### Result of CPU 1

**Network 1 (TUSEND):**

Based on the input parameter ID ("connectionID"), the "TUSEND" instruction knows the communication connection to be used. Based on the input parameter ADDR ("SLI_plcDB_taddr_param_TUSEND"), the communication partner (CPU 2) can be addressed.

When the input parameter REQ ("TUSEND.start") supplies the signal state "TRUE", the "TUSEND" instruction is started. For multiple calls, the "TUSEND" instruction transmits the data record detected at input parameter DATA ("SLI_plcDB_sendData_TUSEND"). The size of the data record to be transmitted is restricted by the value of the input parameter LEN ("TUSEND.maxLength").

Successful transfer of the data record is indicated by the output parameter DONE ("#doneSEND") with the signal state "TRUE" and the output parameter STATUS ("TUSEND.status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "TUSEND.done".

The output parameter ERROR ("TUSEND.error") or the tag "TUSEND.memErrStatus" indicates that processing in the example is taking place without errors.

![Result of CPU 1](images/94532154891_DV_resource.Stream@PNG-de-DE.png)

**Network 2 (TUSEND):**

When TUSEND signals an error ("TUSEND.error" is "TRUE"), the reported status ("TUSEND.status") is stored permanently ("TUSEND.memErrStatus").

##### Result of CPU 2

**Network 1 (TURCV):**

Based on the input parameter ID ("connectionID"), the "TURCV" instruction knows the communication connection to be used. The communication partner (CPU 1) can be addressed based on the input parameter ADDR ("SLI_plcDB_taddr_param_TURCV").

When the input parameter EN_R ("TURCV.start") supplies the signal state "TRUE", the "TURCV" instruction is started. For multiple calls, the "TURCV" instruction receives the transmitted data record. The data record is detected at the input parameter DATA ("SLI_plcDB_rcvData_TURCV").

![Result of CPU 2](images/94532021131_DV_resource.Stream@PNG-de-DE.png)

The length in BYTES of the actually transmitted data record is detected with the output parameter LEN ("#length"). This value is only displayed during the success status. Then "0" is detected. Successful receipt of the data record is indicated by the output parameter DONE ("#doneRCV") with the signal state "TRUE" and the output parameter STATUS ("TURCV.status") with the value "0000".

Because the values of the output parameters are only displayed for the moment of their validity, do the following:

- Save the success status in the tag "TURCV.done"
- Save the length in BYTES in the tag "TURCV.readLength".

The output parameter ERROR ("TURCV.error") or the tag "TURCV.memErrStatus" indicates that processing in the example is taking place without errors.

![Result of CPU 2](images/94531981835_DV_resource.Stream@PNG-de-DE.png)

**Network 2 (TURCV):**

When TURCV signals an error ("TURCV.error" is "TRUE"), the reported status ("TURCV.status") is stored permanently ("TURCV.memErrStatus").

##### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[TUSEND: Sending data (S7-1200, S7-1500)](#tusend-sending-data-s7-1200-s7-1500)
  
[TURCV: Receiving data (S7-1200, S7-1500)](#turcv-receiving-data-s7-1200-s7-1500)

### T_RESET: Resetting the connection (S7-1200, S7-1500)

#### Description

The "T_RESET" instruction terminates and then reestablishes an existing connection.

The local end points of the connection are retained. They are generated automatically:

- If a connection has been configured and loaded to the CPU.
- If a connection has been generated by the user program, for example, by calling the instruction "[TCON](#tcon-establish-communication-connection-s7-1200)".

The instruction "T_RESET" can be executed for all connection types (TCP, UDP, ISO-on-TCP, etc.). It does not matter whether the local interface of the CPU or the interface of a CM/CP was used for the connection.

Once the instruction "T_RESET" has been called using the REQ parameter, the connection specified with the ID parameter is terminated and, if necessary, the data send and receive buffer cleared. Canceling the connection also cancels any data transfer in progress. There is therefore a risk of losing data if data transfer is in progress. The CPU defined as the active connection partner will then automatically attempt to restore the interrupted communication connection. You therefore do not need to call the "[TCON](#tcon-establish-communication-connection-s7-1200)" instruction to reestablish the communication connection.

The output parameters DONE, BUSY and STATUS indicate the status of the job.

#### Parameter

The following table shows the parameters of the instruction "T_RESET":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter REQUEST starts the job for terminating the connection specified by ID. The job starts on a rising edge. |
| ID | Input | CONN_OUC | I, Q, M, D, L or constant | Reference to the connection to the passive partner ID being interrupted must be identical to the corresponding parameter ID in the local connection description.  Value range: W#16#0001 to W#16#0FFF |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE  - 0: Job not yet started or still executing. - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter BUSY  - 0: Job is complete. - 1: The job is not yet complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR  - 0: No error occurred. - 1: Error occurred during processing. The STATUS parameter supplies detailed information on the type of error |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS  Error information (see "STATUS parameter" table). |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameter STATUS

| STATUS* (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error. |
| 0001 | Connection has not been established. |
| 7000 | No job processing active. |
| 7001 | Connection termination launched. |
| 7002 | Connection being terminated. |
| 8081 | Unknown connection specified at the ID parameter. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

#### Example

You can find the example here: [Program example for T_RESET](#program-example-for-t_reset-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Program example for T_RESET (S7-1200, S7-1500)

#### Introduction

In the following example you use a configured connection (by UDP for example) between two CPUs (S7-1500). Reset the connection using instruction "T_RESET".

#### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. A UDP connection is configured.

  ![Requirement](images/94531792907_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.

#### Create tags and interconnect parameters (program of CPU 1)

To store the data, create a global data block ("SLI_gDB_T_RESET") with the following structures and tags.

![Create tags and interconnect parameters (program of CPU 1)](images/94532459019_DV_resource.Stream@PNG-de-DE.png)

Create the FB "SLI_FB_T_RESET" Create the following local tags in it.

![Create tags and interconnect parameters (program of CPU 1)](images/94532707083_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "T_RESET" as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94532895115_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of T_RESET, save the status as follows.

![Create tags and interconnect parameters (program of CPU 1)](images/94533031947_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: To reset the "REQ" parameter, create the following interconnections.

![Create tags and interconnect parameters (program of CPU 1)](images/94533040779_DV_resource.Stream@PNG-de-DE.png)

#### Assigning communication connection

The addressing parameters must be adapted for the connection.

- Store the hexadecimal value of the hardware identifier of the configured UDP connection at the input parameter ID ("connectionID").

  You can find the hardware identifier in the "Network view" under "Connections".

  ![Assigning communication connection](images/94531848971_DV_resource.Stream@PNG-de-DE.png)

#### Result

**Network 1:**

Based on the input parameter ID ("connectionID"), the "T_RESET" instruction knows the communication connection to be used.

When the input parameter REQ ("T_RESET.start") supplies the signal state "TRUE", the "T_RESET" instruction is started. The "T_RESET" instruction terminates the specified communication connection. All jobs that use the connection are terminated. The active connection partner (CPU 1) then re-establishes the connection automatically.

Successful transfer of the data record is indicated by the output parameter DONE ("#done") with the signal state "TRUE" and the output parameter STATUS ("T_RESET.status") with the value "0000".   
Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "T_RESET.done".

The output parameter ERROR ("T_RESET.error") or the tag "T_RESET.memErrStatus" indicates that processing in the example is taking place without errors.

![Result](images/94532698251_DV_resource.Stream@PNG-de-DE.png)

**Network 2:**

When T_RESET signals an error ("T_RESET.error" is "TRUE"), the reported status ("T_RESET.status") is stored permanently ("T_RESET.memErrStatus").

**Network 3:**

After the successful processing of T_RESET ("T_RESET.done"), T_RESET is stopped.

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[T_RESET: Resetting the connection (S7-1200, S7-1500)](#t_reset-resetting-the-connection-s7-1200-s7-1500)

### T_DIAG: Checking the connection (S7-1200, S7-1500)

#### Description

You use the "T_DIAG" instruction to check the status of a connection and read further information on the local end point of this connection.

- The connection is referenced by the ID parameter. You can read both connection end points configured in the connection editor and programmed connection end points (e.g. with the "TCON" instruction).

  Temporary connection end points (for example end points created when you connect to an engineering station) cannot be diagnosed, as no connection ID is generated in this process.
- The connection information read is stored in a structure referenced by the RESULT parameter.
- The output parameter STATUS indicates whether it was possible to read the connection information. The connection information in the structure at the RESULT parameter is only valid if the "T_DIAG" instruction has been completed with STATUS = W#16#0000 and ERROR = FALSE.

  Connection information cannot be evaluated if an error occurs.
- As of firmware version V2.9, the S7-1500 CPU contains the instruction "TCONSettings". If you call "T_DIAG" with a connection ID provided by "TCONSettings", the structure referenced by the RESULT parameter contains the following values:

  | Name | Value |
  | --- | --- |
  | InterfaceID | 64 (default value) |
  | ID | Identical to Parameter ID |
  | ConnectionType | 0 |
  | ActiveEstablished | FALSE |
  | State | 1 (disconnected) |
  | Child | 3 (programmed connection) |
  | SentBytes | 0 |
  | ReceivedBytes | 0 |
  | ConnTrials | 0 |
  | ConnTrialsSuccess | 0 |
  | LastConnErrReason | 0 |
  | LastConnErrTimeStamp | LDT#1970-01-01-00:00:00 |
  | LastDisconnReason | 0 |
  | LastDisconnTimeStamp | LDT#1970-01-01-00:00:00 |
- As of firmware version V4.5, the S7-1200 CPU contains the instruction "TCONSettings". If you call "T_DIAG" with a connection ID provided by "TCONSettings", the structure referenced by the RESULT parameter contains the following values:

  | Name | Value |
  | --- | --- |
  | InterfaceID | 64 (default value) |
  | ID | Identical to Parameter ID |
  | ConnectionType | 0 |
  | ActiveEstablished | FALSE |
  | State | 1 (disconnected) |
  | Child | 3 (programmed connection) |
  | SentBytes | 0 |
  | ReceivedBytes | 0 |

#### Possible connection information

Two different structures can be used to read the connection information at the RESULT parameter:

- The "TDiag_Status" structure only contains the most important information about a connection end point, for example the protocol used, the connection status and the number of data bytes sent or received.
- The structure "TDiag_StatusExt" (with S7-1500 CPUs only) supplies not just the most important information, but also the number of connection attempts, the reason for a connection abort, etc.

The structure and parameters of the two structures are described below (see the "TDIAG_Status and TDIAG_StatusExt structures" table).

#### Parameters

The following table shows the parameters of the instruction "T_DIAG":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Starts the instruction to check the connection specified in the ID parameter when there is a positive edge. |
| ID | Input | CONN_OUC (WORD) | I, Q, M, D, L or constant | Reference to the assigned connection.   Value range: W#16#0001 to W#16#0FFF |
| RESULT | InOut | VARIANT | D | Pointer to the structure in which the connection information is stored. The structures TDiag_Status or TDiag_StatusExt (with S7-1500 CPUs only) can be used at the RESULT parameter (for a description, see the "TDIAG_Status and TDIAG_StatusExt structures" table). |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: Instruction not yet started or still in progress. - 1: Instruction executed without errors. |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: Instruction not yet started or already completed. - 1: Instruction not yet completed. A new job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: No error. - 1: Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### BUSY, DONE and ERROR parameters

You can check the status of "T_DIAG" instruction execution with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. You use the DONE parameter to check whether or not an instruction has been executed successfully. The ERROR parameter is set if errors occur during execution of "T_DIAG".

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The instruction is being processed. |
| 0 | 1 | 0 | The instruction has been executed successfully. The data in the structure referenced by RESULT are only valid if this is the case. |
| 0 | 0 | 1 | Instruction completed with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new instruction has been assigned. |

#### Parameter STATUS

The following table shows the meaning of the values at the STATUS parameter:

| STATUS* (W#16#...) | Explanation |
| --- | --- |
| 0000 | The instruction "T_DIAG" has been executed successfully. The data in the structure referenced at the RESULT parameter can be evaluated. |
| 7000 | No instruction processing active. |
| 7001 | Instruction processing launched. |
| 7002 | Connection information is being read (REQ parameter irrelevant). |
| 8086 | The value at the ID parameter is outside the valid range. |
| 8089 | The RESULT parameter points to an invalid data type (structures TDIAG_Status and TDIAG_StatusExt only). |
| 80A3 | The ID parameter references a connection end point which does not exist. With programmed connections, this error can also occur after the "TDISCON" instruction is called. |
| 80B1 | The RESULT parameter was changed before the execution of T_DIAG was completed. A change of RESULT is not permitted during execution of T_DIAG. |
| 80C4 | Internal error. Access to the connection end point is temporarily unavailable. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

#### Structures TDIAG_Status and TDIAG_StatusExt

> **Note**
>
> **TDIAG_StatusExt structure**
>
> The TDIAG_StatusExt structure only exists with S7-1500 CPUs.

The table below details the form of the TDIAG_Status and TDIAG_StatusExt structures:

- From the InterfaceID to the ReceivedBytes parameter, the "TDIAG_StatusExt" and "TDIAG_Status" structures are identical.
- The structure TDIAG_StatusExt also includes the parameters ConnTrials to LastDisconnTimeStamp.

> **Note**
>
> **Usage of the structures TDIAG_StatusExt and TDIAG_StatusExt_V2**
>
> It is strongly recommended to use TDIAG_StatusExt_V2 as a structure for the detailed information in new projects.
>
> If you are using TDIAG_StatusExt, accessing the "LastConnErrTimeStamp" structure element will cause your CPU to enter the "Defective" operating state.

The value of each element is only valid if the instruction has been executed without errors. If an error occurs, the content of the parameters will not change.

| Name | Data type | Description |
| --- | --- | --- |
| The following parameters are in both the TDIAG_Status and the TDIAG_StatusExt structure: |  |  |
| InterfaceID | HW_ANY | Interface ID (LADDR) of the CPU or the CM/CP. |
| ID | CONN_OUC | ID of the connection diagnosed. Following a successful call, the value of this element is identical to the parameter ID of the "T_DIAG" instruction. |
| ConnectionType | BYTE | Protocol type used for connection:  - 0x01: Not used. - ... - 0x0B: TCP protocol (IP_v4) - 0x0C: ISO-on-TCP protocol (RFC1006) - 0x0D: TCP protocol (DNS) - 0x0E: Dial-in protocol - 0x0F: WDC protocol - 0x10: SMTP protocol - 0x11: TCP protocol - 0x12: TCP and ISO-on-TCP protocol (RFC1006) - 0x13: UDP protocol - 0x14: Reserved - 0x15: PROFIBUS bus access protocol (FDL) - 0x16: ISO 8073 transport protocol (ISO native) - ... - 0x20: SMTP or SMTPS protocol - based on IPv4 - 0x21 SMTP or SMTPS protocol - based on IPv6 - 0x22: SMTP or SMTPS protocol based on FQDN (**F**ully **Q**ualified **D**omain **N**ame) - ... - 0x70: S7 connection - Other: Reserved |
| ActiveEstablished | BOOL | - FALSE: Locally, the passive connection end point - TRUE: Locally, the active connection end point |
| State | BYTE | Current status of the connection end point  - 0x00: Not used. - 0x01: Connection terminated. Temporary status, for example, after the "T_RESET" instruction is called. The system then automatically attempts to reestablish the connection. - 0x02: The active connection end point is attempting to establish a connection to the remote communication partner. - 0x03: The passive connection end point is waiting for establishment of the connection to the remote communication partner. - 0x04: Connection established. - 0x05: The connection is being terminated. This may be because the "T_RESET" or "T_DISCON" instruction has been called. Other possible reasons are protocol errors and line breaks. - 0x06..0xFF: Not used. |
| Kind | BYTE | Mode of the connection end point:  - 0x00: Not used. - 0x01: Configured, static connection which has been configured and loaded to the CPU. - 0x02: Configured, dynamic connection which has been configured and loaded to the CPU (not currently supported). - 0x03: Programmed connection generated in the user program with the instruction "TCON". A call of the instruction "TDISCON" or a transition to CPU STOP status has destroyed the connection end point. - 0x04: Temporary, dynamic connection established by the engineering station (ES) or operator station (OS) (this connection currently not be diagnosed due to the missing ID). - 0x05..0xFF: Not used. |
| SentBytes | UDINT | Number of data bytes sent. |
| ReceivedBytes | UDINT | Number of data bytes received. |
| The following parameters only occur in the TDiag_StatusExt structure: |  |  |
| ConnTrials | UDINT | Number of connection attempts. Once a connection has been successfully established, ConnTrials has the value 0. If this element is not equal to 0, this indicates that there are connection problems.   Note: With a passive connection end point, this value is never greater than 1. |
| ConnTrialsSuccess | UDINT | Number of successful connection attempts. This element is never reset during the life cycle of a connection end point, and returns to 0 after reaching 0xFFFF FFFF.   Note: This parameter is 1 if there has never been a problem in this connection. |
| LastConnErrReason | UDINT | Error ID output during the last connection attempt with errors (the error messages are identical to those at the LastDisconnReason parameter):  - 0x4F01: Remote connection end point cannot be reached (this error usually occurs during connection establishment). - 0x4F02: Connection terminated locally. - 0x4F03: Connection terminated by remote communication partner. - 0x4F04: Connection terminated by a protocol error. - 0x4F05: Connection terminated by a network problem detected locally. - 0x4F06: Connection terminated by a network problem detected remotely. - 0x4F07: Connected terminated due to timeout in protocol. - 0x4F08: Incorrect parameter assignment: Connection to be established to local partner's own address. - 0x4F09: Connection temporarily reset by a call of the instruction "T_RESET". - 0x4F0A: Insufficient connection resources available (quantity exceeded) - 0x4F0B: Internal error: Incorrect addressing parameters - 0x4F0C: Internal CPU communication error - 0x4F0D: Internal AS communication error between CPU and CM/CP - 0x4F0E: The local TCP/UDP port (or RFC1006-T selector) specified is already in use. |
| LastConnErrTimeStamp | LDT | Time of the last connection attempt with errors. |
| LastDisconnReason | UDINT | Error ID which led to the last connection termination (the error messages are identical to those at the LastConnErrReason parameter):  - 0x4F01: Remote connection end point cannot be reached (this error usually occurs during connection establishment). - 0x4F02: Connection terminated locally. - 0x4F03: Connection terminated by remote communication partner. - 0x4F04: Connection terminated by a protocol error. - 0x4F05: Connection terminated by a network problem detected locally. - 0x4F06: Connection terminated by a network problem detected remotely. - 0x4F07: Connected terminated due to timeout in protocol. - 0x4F08: Incorrect parameter assignment: Connection to be established to local partner's own address. - 0x4F09: Connection temporarily reset by a call of the instruction "T_RESET". - 0x4F0A: Insufficient connection resources available (quantity exceeded) - 0x4F0B: Internal error: Incorrect addressing parameters - 0x4F0C: Internal CPU communication error - 0x4F0D: Internal AS communication error between CPU and CM/CP - 0x4F0E: The local TCP/UDP port (or RFC1006-T selector) specified is already in use. |
| LastDisconnTimeStamp | LDT | Time of the last connection termination. |

#### Example

You can find the example here: [Program example for T_DIAG](#program-example-for-t_diag-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Program example for T_DIAG (S7-1200, S7-1500)

#### Introduction

In the following example you use a configured connection (by UDP for example) between two CPUs (S7-1500). The instruction "T_DIAG" is used to diagnose the connection and read information from the local end point of the connection.

#### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. A UDP connection is configured.

  ![Requirement](images/94531792907_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.

#### Create tags and interconnect parameters (program of CPU 1)

To store the data, create a global data block ("SLI_gDB_T_DIAG") with the following structures and tags.

Note: "TDiag_StatusExt" is a system data type for recorded the diagnostics data.

![Create tags and interconnect parameters (program of CPU 1)](images/94533399179_DV_resource.Stream@PNG-de-DE.png)

Create the FB "SLI_FB_T_DIAG" Create the following local tags in it.

![Create tags and interconnect parameters (program of CPU 1)](images/94533502475_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "T_DIAG" as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94533511307_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of T_DIAG, save the status as follows.

![Create tags and interconnect parameters (program of CPU 1)](images/94533545739_DV_resource.Stream@PNG-de-DE.png)

#### Assigning communication connection

The addressing parameters must be adapted for the connection.

- Store the hexadecimal value of the hardware identifier of the configured UDP connection at the input parameter ID ("connectionID").

  You can find the hardware identifier in the "Network view" under "Connections".

  ![Assigning communication connection](images/94531848971_DV_resource.Stream@PNG-de-DE.png)

#### Result

**Network 1:**

Based on the input parameter ID ("connectionID"), the "T_DIAG" instruction knows the communication connection to be used.

When the input parameter REQ ("T_DIAG.start") supplies the signal state "TRUE", the "T_DIAG" instruction is started. The "T_DIAG" instruction reads the status of the connection and the status of the local end point of the connection.

Successful transfer of the data record is indicated by the output parameter DONE ("#done") with the signal state "TRUE" and the output parameter STATUS ("T_DIAG.status") with the value "0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "T_DIAG.done".

The output parameter ERROR ("T_DIAG.error") or the tag "T_DIAG.memErrStatus" indicates that processing in the example is taking place without errors.

![Result](images/94533446411_DV_resource.Stream@PNG-de-DE.png)

The diagnostics data are recorded at the RESULT parameter ("TDiag_StatusExt").

![Result](images/94533493643_DV_resource.Stream@PNG-de-DE.png)

**Network 2:**

When T_DIAG signals an error ("T_DIAG.error" is "TRUE"), the reported status ("T_DIAG.status") is stored permanently ("T_DIAG.memErrStatus").

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[T_DIAG: Checking the connection (S7-1200, S7-1500)](#t_diag-checking-the-connection-s7-1200-s7-1500)

### T_CONFIG: Configure interface (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description T_CONFIG (S7-1200, S7-1500)](#description-t_config-s7-1200-s7-1500)
- [Parameter CONF_DATA (S7-1200, S7-1500)](#parameter-conf_data-s7-1200-s7-1500)
- [DONE, BUSY and ERROR parameters
  (S7-1200, S7-1500)](#done-busy-and-error-parameters-s7-1200-s7-1500-1)
- [Parameter STATUS and ERR_LOC (S7-1200, S7-1500)](#parameter-status-and-err_loc-s7-1200-s7-1500)
- [Program example for T_CONFIG (S7-1200, S7-1500)](#program-example-for-t_config-s7-1200-s7-1500)

#### Description T_CONFIG (S7-1200, S7-1500)

##### Description

The "T_CONFIG" instruction is used for the program-controlled configuration of the integrated PROFINET interfaces of the CPU or the Ethernet interface of a CP/CM.

##### Configuration of the integrated PROFINET interfaces of the CPU

With the "T_CONFIG" instruction, you can change the Ethernet address, the PROFINET device name or the IP addresses of the NTP servers for time-of-day synchronization from within the user program. The existing configuration data is overwritten.

You can make the following changes:

- Settings for the IP protocol

  - IP address
  - Subnet mask
  - Router address

  These settings match the settings in the device view or in the network view for the properties of the PROFINET interface: Ethernet addresses &gt; Internet Protocol Version 4 (IPv4)
- Settings for PROFINET

  - Assignment of the PROFINET device name

    > **Note**
    >
    > **Dependency between device names and IP protocol**
    >
    > The IP protocol must also be set when a new device name is assigned.

  These settings match the settings in the device view or in the network view for the properties of the PROFINET interface: Ethernet addresses &gt; PROFINET
- Settings for time-of-day synchronization

  - Assignment of the IP addresses of the NTP servers for time-of-day synchronization (only with S7-1500 and there only for the PROFINET interface [X1] of a modular CPU)

  These settings match the settings in the device view or in the network view:

  - TIA Portal prior to V17.0: For the properties of the PROFINET interface: Time-of-day synchronization &gt; NTP mode
  - TIA Portal as of V17.0: For the properties of the CPU: Time &gt; Time-of-day synchronization &gt; NTP mode

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Restart of CPU after execution of the "T_CONFIG" instruction (only S7-1200 CPUs with firmware versions V2.0 to V4.1.2)**  The CPU is restarted after you have executed the instruction to change an IP parameter. The CPU goes to STOP mode, a warm restart is carried out and the CPU starts up again (RUN mode).   Make sure that the control process is in a secure operating mode after the CPU has been restarted following execution of the instruction. Uncontrolled operation can result in serious material damage or personal injury due to malfunctions or programming errors, for example. Non-retentive data could be lost. |  |

##### Configuration of the Ethernet interface of a CP 154x‑1

With the "T_CONFIG" instruction you can change the IPv6 address, the MAC address or the IP addresses of up to two DNS servers of the Ethernet interface of a CP from within the user program. In addition, the NTP servers can be configured for the CP. The existing configuration data is overwritten.

##### Requirement

- To use the instruction, you must set specific properties of the PROFINET interface. For this purpose open the properties of the PROFINET interface in the device view. In the "Ethernet addresses" or "Time synchronization" dialog, enable the following options:

  - In order to change the IP address parameters with "T_CONFIG": Select the setting "IP address is set directly at the device" under "IP protocol".
  - In order to change the PROFINET device name with "T_CONFIG":

    Select the setting "PROFINET device name is set directly at the device" under "PROFINET".

    Also select the setting "IP address is set directly at the device" under "IP protocol".
  - To change the IP addresses of the NTP servers with "T_CONFIG".

    Select the setting "IP address is set directly at the device" under "IP protocol".

    Select "Enabled time synchronization via NTP server" and specify the IP address of at least one NTP server.
- The configuration data must be stored in the following system data types and assigned at the parameter [CONF_DATA](#parameter-conf_data-s7-1200-s7-1500):

  - Store the IP address, subnet mask, and the router address in the system data type IF_CONF_V4.
  - Store the device name in the system type IF_CONF_NOS. Observe the restrictions that exist for assigning the name of the device (see parameter [CONF_DATA](#parameter-conf_data-s7-1200-s7-1500)).
  - Use store the IP addresses for the NTP time synchronization in the system data type IF_CONF_NTP.
  - Store the IPv6 address of the PROFINET interface of a CP 1543-1 in the system data type IF_CONF_IPV6.
  - Store the MAC address of the PROFINET interface of a CP 1543-1 in the system data type IF_CONF_MAC.
  - Store the IP addresses of up to two DNS servers for the PROFINET interface of a CP 1543-1 in the system data type IF_CONF_DNS.

##### Functional description

The "T_CONFIG" instruction works asynchronously, which means its execution extends over multiple calls. The configuration process is started by calling "T_CONFIG" with REQ = 1. Only one job can be active at any time.

The block is edge triggered which means that after BUSY= FALSE the block must be re-called with REQ=FALSE to enable the instance.

##### Parameter

The following table shows the parameters of the "T_CONFIG" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Calling the instruction with REQ = 1 starts processing of the instruction. |
| INTERFACE | Input | HW_INTERFACE | I, Q, M, D, L or constant | Hardware identifier of the interface  The hardware ID is displayed in the properties of the interface in the device view, and in the system constants of the PLC tags. |
| [CONF_DATA](#parameter-conf_data-s7-1200-s7-1500) | Input | VARIANT | D, L | Pointer to the higher-level structure that contains the system data types IF_CONF_HEADER, IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC and IF_CONF_DNS (see description of the parameters CONF_DATA). |
| [DONE](#done-busy-and-error-parameters-s7-1200-s7-1500-1) | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: Processing not yet complete. - 1: Processing of instruction finished successfully. |
| [BUSY](#done-busy-and-error-parameters-s7-1200-s7-1500-1) | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: Processing of the instruction has not started, completed or canceled yet. - 1: Processing of instruction is in progress |
| [ERROR](#done-busy-and-error-parameters-s7-1200-s7-1500-1) | Output | BOOL | I, Q, M, D, L | Status parameter:  - 0: No error - 1: Error |
| [STATUS](#parameter-status-and-err_loc-s7-1200-s7-1500) | Output | DWORD | I, Q, M, D, L | Detailed status information:  Detailed error and status information in the form of an error code are output at the parameter STATUS. |
| [ERR_LOC](#parameter-status-and-err_loc-s7-1200-s7-1500) | Output | DWORD | I, Q, M, D, L | Error location:  - 0: Error during execution of the instruction or when assigning parameters. - &gt; 0: Errors in the structure or content of the configuration data at the parameter CONF_DATA. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

##### Example

You can find the example here: [Program example for T_CONFIG](#program-example-for-t_config-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)
  
[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

#### Parameter CONF_DATA (S7-1200, S7-1500)

##### Structure of the configuration data

The configuration data at the parameter CONF_DATA can be stored in a global data block or in the section "Static" of the block interface.

The configuration data must be stored according to the following structure:

| Name |  | Data type | Description |
| --- | --- | --- | --- |
| ConfData |  | Struct | Parent structure that is assigned at the parameter CONF_DATA. |
|  | Header | IF_CONF_HEADER | The header is used to define the number of these system data types. The system data type IF_CONF_HEADER must always be included. |
| IPData | IF_CONF_V4 | The IP address, subnet mask and router address are stored in this system data type. |  |
| NoS | IF_CONF_NOS | The PROFINET device names are stored in this system data type. Only create IF_CONF_NOS if you also want to change the device names with "T_CONFIG". |  |
| NTP | IF_CONF_NTP | In this system data type, use store the IP addresses of the NTP servers for time synchronization. |  |
| IP_V6 | IF_CONF_V6 | Store the IPv6 address of a CP 154x‑1 in this system data type. |  |
| MAC | IF_CONF_MAC | Store the MAC address of a CP 154x‑1 in this system data type. |  |
| DNS | IF_CONF_DNS | Store the IP addresses of up to two DNS servers for a CP 154x‑1 in this system data type. |  |

Create the system data types IF_CONF_HEADER, IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC and IF_CONF_DNS be entering the name of the system data type in the "Data type" column of the data block or the block interface. The name for the system data types can be freely assigned. The system data types can be combined in any order.

> **Note**
>
> **Parameter "Mode" when using a CP 154x‑1, a CP 154xSP-1 or a CP1243-x**
>
> When using a CP 154x‑1, a CP 154xSP-1 or a CP1243-x, only the value 2 (temporary validity) is permitted for the "Mode" parameter.

##### System data type IF_CONF_Header

Use the system data type IF_CONF_Header to specify the number of system data types IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC and IF_CONF_DNS that are used when executing "T_CONFIG".

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | FieldType | UINT | 0 | Field type: Must always have the value "0". |
| 2 ... 3 | FieldId | UINT | 0 | Error ID: Must always have the value "0". |
| 4 ... 5 | SubfieldCount | UINT | 0 | Number of system data types IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC and IF_CONF_DNS used |

##### System data type IF_CONF_V4

The IP address, subnet mask and router address are defined with the system data type IF_CONF_V4.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 30 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 18 | Length of the system data type IF_CONF_V4  The start value must be used for the length specification since the parameters of IF_CONF_V4 have a fixed length and structure. |
| 4 ... 5 | Mode | UINT | 0 | Validity of addressing:  - 1: Permanent validity of the configuration data - 2: Temporary validity of the configuration data including the deletion of existing permanent configuration data |
| 6 ... 9 | InterfaceAddress | IP_V4 * | 0.0.0.0 | IP address |
| 10 - 12 | SubnetMask | IP_V4 * | 0.0.0.0 | Subnet mask |
| 14 - 16 | DefaultRouter | IP_V4 * | 0.0.0.0 | Router address  For program-controlled configuration ensure that in the case of a CPU with several PROFINET interfaces only one router address may be assigned at one interface since there must be only one default router in the PLC. A faulty configuration leads to a diagnosis during runtime, the instruction T_CONFIG does not return an error. |
| * The data type IP_V4 is a structure of 4 BYTE, which includes the respective address of the respective parameter (e.g. at parameter SubnetMask the four-digit address of the subnet mask of the IP protocol). |  |  |  |  |

##### System data type IF_CONF_NOS

With the system data type IF_CONF_NOS you specify the station name to be assigned when the "T_CONFIG" instruction executes.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 40 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 246 | Length of the system data type IF_CONF_NOS in bytes.   - For an absolute length, the value for the Lenght parameter consists of:   - 6 bytes for the parameter Id, Length and Mode.   - up to 240 bytes for the device name (parameter NOS).Example: An overall length of 10 is the result for the device name "plc1" with a length of 4 characters (=4 bytes). - Use the default start value 246 at the Lenght parameter for a dynamic length.    Make sure that you enter the value "0" after the name (see description for NOS parameter). |
| 4 ... 5 | Mode | UINT | 0 | Validity of the device name change:  - 1: Permanent validity of the device name. - 2: Temporary validity of the device name. |
| 6 ... 244 | NOS | ARRAY [1...240] of Byte | 0 | Device name (Name of Station)  - You must occupy the ARRAY from the first byte. The station name is deleted if "0" is assigned as the first byte. - The minimum length for the name is 1 byte. The maximum length for a name is 240 bytes. - If the device name is shorter than specified at the parameter Length then a zero byte (16#0 hex) must be entered after the actual station name (according to IEC 61185-6-10). Otherwise NOS will be rejected and the instruction "T_CONFIG" outputs the error code DW#16#C0809400 at the parameter STATUS. - If the device name is longer than specified at the parameter Length then the device name will only be written up to the specified length.     The following restrictions apply for the device name:  - The name must be specified in ASCII code. - Only lowercase letters, numbers, hyphen or dots can be used for the name.    - The name cannot begin or end with a hyphen.   - The name cannot have the form n.n.n.n (n = 0 to 999).   - The name must not begin with the string "port-xyz" or "port-xyz-abcde" (a, b, c, d, e, x, y, z = 0 to 9). - A name component between two points can be up to 63 characters long. - No special characters such as umlauts, brackets, underscore, slash, blank etc.   The error code C080_9400 is output at the parameter STATUS if an invalid character is used. |

##### System data type IF_CONF_NTP

Using the system data type IF_CONF_NTP you specify the IP addresses of the NTP servers for time synchronization.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 17 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 22 | Length of the system data type IF_CONF_NTP in bytes  The start value must be used for the length specification since the parameters of IF_CONF_NTP have a fixed length and structure. |
| 4 ... 5 | Mode | UINT | 2 | Validity:  - 1: Permanent validity (not permitted) - 2: Temporary validity |
| 6 ... 9 | NTP_IP[1] | ARRAY [1...4] of IP_V4 |  | IP address of NTP server 1  Note: As of TIA Portal V17.0, you can set the IP address of NTP server 1 to 0.0.0.0 in order to switch off the NTP client. |
| ... | ... |  |  | IP address of NTP server 2 ... 3  Note: As of TIA Portal V17.0, you can set the IP address of NTP server 2 and NTP server 3 to 0.0.0.0 to switch off the NTP client. |
| 18 ... 21 | NTP_IP[4] | ARRAY [1...4] of IP_V4 |  | IP address of NTP server 4  Note: As of TIA Portal V17.0 you can set the IP address of NTP server 4 to 0.0.0.0 to switch off the NTP client. |

##### System data type IF_CONF_V6 (only when using a CP 154x‑1)

With the system data type IF_CONF_V6 you assign an IPv6 address for the interface selected with INTERFACE.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 22 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 22 | Length of the system data type IF_CONF_V6 in bytes  The start value must be used for the length specification since the parameters of IF_CONF_V6 have a fixed length and structure. |
| 4 ... 5 | Mode | UINT | 0 | Validity of the IPv6 address:  - 1: Permanent validity - 2: Temporary validity |
| 6 ... 21 | InterfaceAddress | IP_V6 * |  | IPv6 address |
| * The data type IP_V6 is a structure of 16 bytes. |  |  |  |  |

##### IF_CONF_MAC system data type (is not supported)

With the system data type IF_CONF_MAC you assign the MAC address for the interface selected with INTERFACE.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 3 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 12 | Length of the system data type IF_CONF_MAC in bytes  The start value must be used for the length specification since the parameters of IF_CONF_MAC have a fixed length and structure. |
| 4 ... 5 | Mode | UINT | 0 | Validity of MAC address:  - 1: Permanent validity - 2: Temporary validity |
| 6 ... 11 | Mac | ARRAY [1...6] of Byte |  | MAC address  Note that by changing the MAC address, connections can abort. |

##### System data type IF_CONF_DNS (only when using a CP 154x‑1)

With the system data type IF_CONF_DNS you assign the IP addresses of up to two DNS servers for the interface selected with INTERFACE.

| Byte | Parameter | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 ... 1 | Id | UINT | 16 | System data type ID The start value of this parameter must not be changed. |
| 2 ... 3 | Length | UINT | 14 | Length of the system data type IF_CONF_DNS in bytes  The start value must be used for the length specification since the parameters of IF_CONF_DNS have a fixed length and structure. |
| 4 ... 5 | Mode | UINT | 0 | Validity:  - 1: Permanent validity - 2: Temporary validity |
| 6 ... 9 | DNS_IP1 | IP_V4 |  | IP address of DNS server 1 |
| 10 ... 13 | DNS_IP2 | IP_V4 |  | IP address of DNS server 2  If only one address is to be set, the IP address of DNS server 2 must be set to 0.0.0.0. |

#### DONE, BUSY and ERROR parameters (S7-1200, S7-1500)

##### Description

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can determine the current status of the instruction and when the transfer of configuration data is concluded.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | FALSE | FALSE | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the parameter [STATUS](#parameter-status-and-err_loc-s7-1200-s7-1500). |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

#### Parameter STATUS and ERR_LOC (S7-1200, S7-1500)

##### Description

The status and error messages of the instruction "T_CONFIG" are output at the parameters STATUS and ERR_LOC.

- The cause of the error is output at the parameter STATUS.
- The location of the error that occurred is output at the parameter ERR_LOC. The following options are available here:

  - 16#0000_0000: Error when calling the instruction (e.g. errors when assigning parameters to the instruction or in communication with the PROFINET interface).
  - 16#0001_0000: Error with the configuration data in the parameters of the system data type IF_CONF_HEADER.
  - 16#0001_000x: Error in the configuration data in the parameters of system data type IF_CONF_V4 or IF_CONF_NOS or IF_CONF_NTP or IF_CONF_V6 or IF_CONF_MAC or IF_CONF_DNS (x specifies the position of the bad sub block in the T_CONFIG structure. If the T_CONFIG structure contains, for example a sub block for the IP address and a sub block for the station name and the error is located in the sub block for the station name, ERR_LOC has the value 0001_0002.)

The following table shows the possible values ​​for the parameters STATUS and ERR_LOC:

| STATUS* | ERR_LOC* | Explanation |
| --- | --- | --- |
| 0000_0000 | 0000_0000 | Order processing completed without errors. |
| 0070_0000 | 0000_0000 | No job processing active. |
| 0070_0100 | 0000_0000 | Start of the order processing. |
| 0070_0200 | 0000_0000 | Intermediate call (REQ irrelevant). |
| C0xx_yy00, xx&gt;80 | 0000_0000 | General error information. See also: [GET_ERR_ID: Get error ID locally](LAD%20%28S7-1200%2C%20S7-1500%29.md#get_err_id-get-error-id-locally-s7-1200-s7-1500) |
| C080_8000 | 0000_0000 | Error at call of the instruction:  The hardware ID at the parameter Interface is invalid. |
| C080_8100 | 0000_0000 | Error at call of the instruction:  The hardware ID at the parameter Interface does not address a PROFINET interface. |
| C080_8700 | 0000_0000 | Error at call of the instruction:  Incorrect length of the data block at the parameter CONF_DATA. |
| C080_8800 | 0001_0000 | Error in the system data type IF_CONF_HEADER:  The parameter FieldType has an invalid value. Use the value "0" for FieldType. |
| C080_8900 | 0001_0000 | Error in the system data type IF_CONF_HEADER:  The parameter FieldId has an invalid value. Use the value "0" for FieldId. |
| C080_8A00 | 0001_0000 | Error in the system data type IF_CONF_HEADER:  Incorrect number at the parameter SubfieldCount. Enter the correct number of system data types IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS being used. |
| C080_8B00 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  The parameter Id has an invalid value. For IF_CONF_V4 use "30", for IF_CONF_NOS "40", for IF_CONF_NTP "17", for IF_CONF_V6 "22", for IF_CONF_MAC "3", for IF_CONF_DNS "16".  Note: IF_CONF_NTP is only permitted if T_CONFIG is used on the first interface [X1] of an S7-1500 modular CPU. |
| C080_8C00 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  Incorrect data type system used, wrong order or multiple use of a system data type. |
| C080_8D00 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  The parameter Length has an incorrect or invalid value. |
| C080_8E00 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  The parameter Mode has an incorrect or invalid value.  - With IF_CONF_V4 and IF_CONF_NOS only the values "1" (permanent) or "2" (temporary) are permitted. - With IF_CONF_NTP only the value "2" (temporary) is permitted. |
| C080_9000 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  Configuration data cannot be applied. Possible cause:  - With IF_CONF_V4: In the hardware configuration, the setting "Set IP address on the device" was not selected.. - With IF_CONF_NOS: In the hardware configuration, the setting "Set PROFINET device name on the device" was not selected.. - With IF_CONF_NTP: In the hardware configuration, the setting "Enable time synchronization via NTP server" was not selected and no IP address was set for NTP servers. |
| C080_9400 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  A parameter value is undefined or invalid. |
| C080_9500 | 0001_000x | Error in the system data type IF_CONF_V4, IF_CONF_NOS, IF_CONF_NTP, IF_CONF_V6, IF_CONF_MAC or IF_CONF_DNS:  The values ​​of two parameters are inconsistent. |
| C080_C200 | 0000_0000 | Error at call of the instruction:  The configuration data can not be transferred. Possible cause: The PROFINET interface is not accessible. |
| C080_C300 | 0000_0000 | Error at call of the instruction:  Insufficient resources (e.g., multiple calling of "T_CONFIG" with different parameters). |
| C080_C400 | 0000_0000 | Error at call of the instruction:  Temporary communication error. Try to call the instruction again at a later time. |
| C080_D200 | 0000_0000 | Error at call of the instruction:  Call not possible. Instruction is not supported by the selected PROFINET interface. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

#### Program example for T_CONFIG (S7-1200, S7-1500)

##### Introduction

In the following example you use a configured connection (by UDP for example) between two CPUs. Configure the IP address and the PROFINET device name of CPU 1 using the instruction "T_CONFIG".

##### Requirements

**Set connection:**

- Two CPUs (for example, S7-1513-1 PN) are available and connected to each other via PROFINET.
- A configured connection is not required.

**Setting up PROFINET of CPU 1:**

1. Open the device view of the CPU 1 "&gt; Properties &gt; PROFINET interface &gt; Ethernet addresses &gt; PROFINET".
2. To set the device names, select the following options:

   - "IP address is set directly at the device".
   - "PROFINET device name is set directly at the device".

**Adjust the value of "hwid":**

- Change the value of "hwid" according to the hardware identifier of the PROFINET interface of your local device (CPU 1).

  > **Note**
  >
  > Open "PLC tags &gt; Show all tags &gt; System constants". Find the entry "&lt;Local~PROFINET_interface_1&gt;", with the data type "Hw_Interface". The "value" cell contains the hardware identifier.

##### Create tags and interconnect parameters (program of CPU 1)

To store the data, create a global data block ("SLI_gDB_T_CONFIG") with the following structures and tags.

![Create tags and interconnect parameters (program of CPU 1)](images/94533660939_DV_resource.Stream@PNG-de-DE.png)

In the structure "configData": Assign parameters for the system data type "IF_CONF_Header" for specifying the size of the PROFINET data, as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94533669771_DV_resource.Stream@PNG-de-DE.png)

In the structure "configData": Assign parameters for the system data type "IF_CONF_v4" for defining the IP address, as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94533729803_DV_resource.Stream@PNG-de-DE.png)

In the structure "configData": Assign parameters for the system data type "IF_CONF_NOS" for defining the PROFINET device name, as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94533828235_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Structure of "configData"**
>
> The information of the structure "configData" can be interpreted as follows:
>
> - In the Header (IF_CONF_Header).
>
>   SubfieldCount = 2: The value means: Two additional structures ("deviceIP", "deviceName") (*) are used below.
>
>   *Make sure to maintain the order of both structures.
> - For In the structure "deviceName" (system data type IF_CONF_NOS)
>
>   - Lenght = 11 (*). The value corresponds to the overall length of the structure NOS (5 bytes for the device name"myplc" + 6 bytes for the parameters Id, Length and Mode)
>
>     *Instead of an absolute length, you can use the default start value (Lenght = 0) for a dynamic length.
>   - Mode = 1. The value causes a permanent change of the device name in "myplc".
>   - NOS[1] ... NOS[5]. The NOS array contains the new device name (1 character / byte).

Create the FB "SLI_FB_T_CONFIG" Create the following local tags in it.

![Create tags and interconnect parameters (program of CPU 1)](images/94725637131_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "T_CONFIG" as follows:

![Create tags and interconnect parameters (program of CPU 1)](images/94533944331_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of T_CONFIG, save the status as follows.

![Create tags and interconnect parameters (program of CPU 1)](images/94533965963_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: To exit T_CONFIG, create the following interconnections.

![Create tags and interconnect parameters (program of CPU 1)](images/94533974795_DV_resource.Stream@PNG-de-DE.png)

##### Result

**Network 1:**

When the input parameter REQ ("T_CONFIG.start") supplies the signal state "TRUE", the "T_CONFIG" instruction is started. The instruction "T_CONFIG" configures the integrated PROFINET interface of the CPU for multiple calls. Based on the input parameter INTERFACE ("T_CONFIG.hwid"), the "T_CONFIG" instruction knows the interface to be used.

Successful transfer of the data record () is indicated by the output parameter DONE ("#done") with the signal state "TRUE". At the same time the value "0000_0000" is displayed at the output parameter STATUS ("T_CONFIG.status"). Because the values of the output parameters are only displayed for the moment of their validity, save the success message in the tag "T_CONFIG.done".

The output parameter ERROR ("T_CONFIG.error") or the tag "T_CONFIG.memErrStat" indicates that processing in the example is taking place without errors.

![Result](images/94533837067_DV_resource.Stream@PNG-de-DE.png)

**Network 2:**

If T_CONFIG signals an error ("T_CONFIG.error", "TRUE"), save the alarm as follows:

- Save the status ("T_CONFIG.status") in the "T_CONFIG.memErrStat" tag.
- Save the error location, output at the output parameter ERR_LOC ("#errorLocation") from T_CONFIG, in the tag "T_CONFIG.errorLocation".

**Online &amp; diagnostics**

To check whether the PROFINET data were changed, open the path "Online &amp; Diagnostics &gt; Functions &gt; Assign name" in the project tree.

![Result](images/94533909899_DV_resource.Stream@PNG-de-DE.png)

##### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Description T_CONFIG (S7-1200, S7-1500)](#description-t_config-s7-1200-s7-1500)

### TCONSettings: Preparing and installing the communication connection (S7-1200, S7-1500)

This section contains information on the following topics:

- [Description of TCONSettings (S7-1200, S7-1500)](#description-of-tconsettings-s7-1200-s7-1500)
- [Request a connection ID and, if necessary, specify a connection property (S7-1200, S7-1500)](#request-a-connection-id-and-if-necessary-specify-a-connection-property-s7-1200-s7-1500)
- [Reading a property of a prepared or an existing connection (S7-1200, S7-1500)](#reading-a-property-of-a-prepared-or-an-existing-connection-s7-1200-s7-1500)
- [Specifying a property of a prepared or an existing connection (S7-1200, S7-1500)](#specifying-a-property-of-a-prepared-or-an-existing-connection-s7-1200-s7-1500)
- [Which connection properties can be read or specified with "TCONSettings"? (S7-1200, S7-1500)](#which-connection-properties-can-be-read-or-specified-with-tconsettings-s7-1200-s7-1500)
- [Terminating a TCP connection (S7-1200, S7-1500)](#terminating-a-tcp-connection-s7-1200-s7-1500)
- [Changing the TTL value for UDP multicast (S7-1500)](#changing-the-ttl-value-for-udp-multicast-s7-1500)

#### Description of TCONSettings (S7-1200, S7-1500)

##### Description

You can use the "TCONSettings" instruction to execute the following functions:

- You request a connection ID for a new OUC connection.
- You request a connection ID for a new OUC connection and at the same time specify a property for this connection.
- You read a property of a prepared or an existing OUC connection.
- You specify a property for a prepared or an existing OUC connection.

You can read or specify the following connection properties with the "TCONSettings" instruction:

- How a TCP connection is terminated
- TTL value for UDP multicast (for S7-1500 CPUs only)

See also: [Which connection properties can be read or specified with "TCONSettings"?](#which-connection-properties-can-be-read-or-specified-with-tconsettings-s7-1200-s7-1500)

##### Functional description

The "TCONSettings" instruction is an asynchronous instruction. Processing extends over multiple calls. You start processing with a rising edge at the "REQ" parameter.

The parameters "Busy" and "Done" indicate the status of the job.

If an error occurs during execution, this is signaled by the parameters "Error" and "Status".

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

##### Parameters

The following table shows the parameters of the "TCONSettings" instruction:

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| REQ | Input | Bool | Control parameter Request  Activates the job on a positive edge. |
| MODE | Input | USInt | Use the "Mode" parameter to select the information you want to read from your CPU:  - 0: Request a connection ID for a new OUC connection and, if necessary, specify a property of the associated connection (if a valid value for a property is present in the OPTION parameter) - 1: Reading a property of the OUC connection referenced by ID - 2: Specify a property of the OUC connection referenced by ID - 3 to 255: Reserved |
| DONE | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or still in progress. - 1: Job completed without error. This state is only displayed for one call. |
| BUSY | Output | Bool | Status parameter with the following values:  - 0: Job not yet started or already completed. - 1: Job not yet completed. A new job with this instance cannot be started |
| ERROR | Output | Bool | Status parameter with the following values:  - 0: No error occurred. - 1: Error occurred during processing. STATUS supplies detailed information on the type of error. This state is only displayed for one call. |
| STATUS | Output | Word | Return value or error information of the "TCONSettings" instruction. |
| ID | InOut | CONN_OUC | Reference to the connection:  Note: For MODE=0, ID is an output parameter, for MODE=1 and MODE=2 ID is an input parameter. |
| OPTION | InOut | Variant | Pointer to the description of the connection property to be read or specified:  - TCON_TCPTermination: How to terminate the TCP connection. - TCON_IPMulticastTTL: TTL value for UDP Multicast |

You can find additional information on valid data types under [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

##### BUSY, DONE and ERROR parameters

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set if errors occur during the execution of "TCONSettings". The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | 0 | 0 | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

##### STATUS parameter

| STATUS (W#16#...) | Explanation |
| --- | --- |
| 0000 | "TCONSettings" was completed without errors. |
| 7000 | No job processing active. |
| 7001 | Start of job execution |
| 7002 | Intermediate call (REQ  irrelevant): |
| 8086 | ID is outside the permitted range. |
| 8087 | Maximum number of OUC connections reached; no additional connections possible. |
| 8089 | OPTION does not point to a valid data type or OPTION is empty. |
| 8090 | OPTION points to a connection property which must not be changed for the connection referenced by ID. |
| 8091 | Invalid value for MODE |
| 8092 | A value in the data block referenced by OPTION is not permitted.  Example: IPMulticastTTLValue has the value 0. |
| 8093 | If MODE has the value 0, ID must also have the value 0. |
| 809A | OPTION points to a data type that is not permitted for "TCONSettings". |
| 80A3 | ID points to a non-existent communication endpoint. |
| 80B1 | The OPTION parameter was changed before the execution of "TCONSettings" was completed. It is not permitted to change OPTION while "TCONSettings" are being executed. |
| 80C3 | The maximum number of simultaneously active jobs has already been reached. |

##### Maximum number of simultaneously active jobs

The maximum number of simultaneously active jobs is identical to the maximum number of OUC connections of your CPU.

#### Request a connection ID and, if necessary, specify a connection property (S7-1200, S7-1500)

##### Reserving a connection resource

You call TCONSettings with MODE=0. You assign the relevant parameters as follows:

- Enter a tag with value 0 at the parameter ID.
- If you do not want to specify a property for the associated connection, leave the OPTION parameter empty.

  If, on the other hand, you want to specify a property for the associated connection, assign a valid value to the parameter OPTION. See also:[Which connection properties can be read or specified with "TCONSettings"?](#which-connection-properties-can-be-read-or-specified-with-tconsettings-s7-1200-s7-1500)

After the DONE parameter has assumed the value TRUE, a connection ID for a new OUC connection is available at the ID parameter and, if necessary, the desired property was specified for this connection. An OUC connection resource was used for the ID. The corresponding diagnostic objects have been created. The corresponding connection is therefore prepared, but not yet known to external communication partners.

You have not specified any details for the connection, neither the connection partner nor the protocol nor the interface nor the DB with the connection description.

> **Note**
>
> **Establishing the connection**
>
> TCONSettings does not establish a connection.

##### Establishing the associated connection

If you want to establish the corresponding connection after the successful version of "TCONSettings", follow this step:

- Save the connection ID provided by "TCONSettings" and call the instruction "TCON" with exactly this ID.

The number of available OUC connections does not change, because this connection has already been taken into account when calling "TCONSettings".

##### Release the connection ID and the corresponding connection resource

If you want to release the connection ID provided by "TCONSettings" and the corresponding connection resource, follow this step:

- Call the "TDISCON" instruction with exactly this ID.

##### CPU changes to STOP mode

When the CPU changes to STOP mode, all connection IDs provided by "TCONSettings" and the corresponding connection resources are released again.

##### Download in "RUN" mode

> **Note**
>
> **Downloading changes in the "RUN" operating state does not release any connection resources.**
>
> To prevent reserved connection IDs from being lost when downloading in "RUN" mode, perform one of the following steps:
>
> - Store the IDs in a memory area that is not initialized after the download.
> - Release the reserved connections by calling the "TDISCON" instruction before downloading.

#### Reading a property of a prepared or an existing connection  (S7-1200, S7-1500)

##### Reading a property of a prepared or an existing connection

You call "TCONSettings" with MODE=1. You assign the relevant parameters as follows:

- At the ID parameter you specify the reference to the desired connection.
- At the OPTION parameter you specify which connection property you want to read. See also: [Which connection properties can be read or specified with "TCONSettings"?](#which-connection-properties-can-be-read-or-specified-with-tconsettings-s7-1200-s7-1500)

After the DONE parameter has assumed the value TRUE, the current values of the desired property are available in the data area specified by OPTION.

#### Specifying a property of a prepared or an existing connection (S7-1200, S7-1500)

##### Specifying a property of a prepared or an existing connection

You call "TCONSettings" with MODE=2. You assign the relevant parameters as follows:

- At the ID parameter you specify the reference to the connection to which you want to assign a property.
- At the OPTION parameter you indicate which connection property you want to specify. See also: [Which connection properties can be read or specified with "TCONSettings"?](#which-connection-properties-can-be-read-or-specified-with-tconsettings-s7-1200-s7-1500)

After the DONE parameter has assumed the value TRUE, the connection has been assigned the desired property.

##### Connections created by OUC and Modbus instructions

The instructions of the OUC library ending with "_C" and the instructions of the MODBUS-TCP library establish connections by calling the instruction "TCON" internally. You can change such connections with "TCONSettings" in the same way as connections that you have created by explicitly calling "TCON".

#### Which connection properties can be read or specified with "TCONSettings"? (S7-1200, S7-1500)

##### Connection properties that can generally be read and specified

The following connection properties can be read and specified with the "TCONSettings" instruction:

- How a TCP connection is terminated. See also: [Terminating a TCP connection](#terminating-a-tcp-connection-s7-1200-s7-1500)
- TTL value for UDP multicast (for S7-1500 CPUs only). See also: [Changing the TTL value for UDP multicast](#changing-the-ttl-value-for-udp-multicast-s7-1500)

##### Relation between the protocol or the interface and the actual readable or specifiable connection properties

Not every protocol or interface can read or specify all of the above connection properties. The following table shows which connection properties are possible for the individual protocols or interfaces.

| Protocol / interface | Terminating a connection | TTL value for UDP Multicast |
| --- | --- | --- |
| Programmed connection: | Yes | Yes |
| Configured connection: | No <sup>1)</sup> | Yes |
| TCP | Yes | No <sup>2)</sup> |
| UDP Multicast | No <sup>3)</sup> | Yes |
| UDP | No <sup>3)</sup> | No <sup>2)</sup> |
| ISO on TCP | No | No <sup>2)</sup> |
| CPU interface | Yes | Yes |
| CP interface | No | No |
| Virtual CP interface | Yes | Yes |
| <sup>1)</sup> You cannot call "TDISCON" for a configured connection. Therefore, there is no way to end the connection in an orderly manner.   <sup>2)</sup> This property is only available with UDP Multicast. The default value for multicast TTL is 1.   <sup>3)</sup> UDP is connectionless at the protocol level, so no termination is necessary. |  |  |

##### Conflicts in the specification of connection properties

Each predefinable connection property is only permitted for specific protocols or interfaces. Therefore, there may be conflicts between your specification of a connection property and the desired protocol or interface. In this case "TCONSettings" returns the value W#16#8090 at the STATUS parameter.

#### Terminating a TCP connection (S7-1200, S7-1500)

##### How can you terminate a TCP connection?

You can terminate an existing TCP connection in the following two ways:

- With a TCP-Reset (default)

  The connection is closed after the frame has been sent with the RST bit set in the header. The associated resources are immediately deleted and released. Remaining data is neither sent nor transferred to the user program.

  > **Note**
  >
  > **Terminating a TCP connection in S7-1500 CPUs with firmware version &lt; V2.9 and S7-1200 CPUs with firmware version &lt; V4.5**
  >
  > In S7-1500 CPUs with firmware version &lt; V2.9 and S7-1200 CPUs with firmware version &lt; V4.5, a TCP connection is always terminated with a TCP reset.
- With a TCP-Finish

  If you have set TCP-Finish as the way of terminating a connection and then call the instruction "TDISCON", the connection is closed from the user's point of view after the termination of "TDISCON" with DONE=TRUE, i.e. the connection ID is available again. In the lower layers in the TCP/IP stack of the module, however, the resources are still assigned for some time, as are the diagnostic objects belonging to the connection.

  If you remove many connections using TCP-Finish and reserve (with "TCONSettings") or establish (with "TCON") connections before the timer for releasing the resources expires, this can result in a resource bottleneck.

##### Conditions for a TCP-Finish

The following conditions must be met in order for you to terminate a connection in an orderly manner using a TCP-Finish:

- The protocol used is TCP.
- The associated interface is located on the CPU.
- The reason for the termination of the connection is the call of the "TDISCON" instruction.

> **Note**
>
> **Terminating a TCP connection during transition to STOP**
>
> During the transition to STOP, a TCP connection is always terminated with a TCP-Reset.

##### SDT for connection termination: TCON_TCPTermination

The SDT for the connection termination has the following structure:

| Parameters | Data type | Start value | Description |
| --- | --- | --- | --- |
| GracefulShutdown | Bool | FALSE | - FALSE: Use a TCP-Reset to terminate the connection. - TRUE: Use a TCP-Finish to terminate the connection. |

#### Changing the TTL value for UDP multicast (S7-1500)

##### TTL value for UDP Multicast

A UDP packet (UDP: User Datagram Protocol), which is sent to a multicast address contains, like all IP packets, a TTL value (TTL: Time to Live). The TTL value is a measure of how far a packet is allowed to propagate. The CPU assigns the value 1 to it; therefore a UDP packet sent to a multicast address cannot be sent across router boundaries.

##### Procedure for changing the TTL value for UDP Multicast

To change the TTL value in UDP Multicast for an established connection (programmed or configured), follow these steps:

1. Call "TCONSettings" with MODE = 2. Enter the reference to the desired connection in the parameter ID and the pointer to the SDT specified below in the parameter OPTION.
2. Call "T_RESET".

   > **Note**
   >
   > **Validity of the new TTL value**
   >
   > With immediate effect, UDP packets sent to a Multicast address include the new TTL value. They can therefore be sent via (new TTL value - 1) router.

##### Conditions for the specification of a new TTL value

The following conditions must be met so that you can specify a new TTL value:

- The protocol used is UDP.
- The remote address is a Multicast address.

##### SDT for the TTL value for UDP Multicast

The SDT for the TTL value for UDP Multicast has the following structure:

| Parameters | Data type | Start value | Description |
| --- | --- | --- | --- |
| IPMulticastTTLValue | USInt | 1 | TTL value for the IP layer of a UDP multicast packet. Permitted values: 1 to 255 |

## Changes to the communications instructions (S7-1200, S7-1500)

This section contains information on the following topics:

- [Differences between the versions &lt;= V3.x and &gt;= V4.1 of the OUC library (S7-1200, S7-1500)](#differences-between-the-versions-v3x-and-v41-of-the-ouc-library-s7-1200-s7-1500)
- [Changes with the TSEND_C instruction (S7-1200, S7-1500)](#changes-with-the-tsend_c-instruction-s7-1200-s7-1500)
- [Changes with the TRCV_C instruction (S7-1200, S7-1500)](#changes-with-the-trcv_c-instruction-s7-1200-s7-1500)
- [Changes with the TCON instruction (S7-1200, S7-1500)](#changes-with-the-tcon-instruction-s7-1200-s7-1500)
- [Changes with the TSEND/TUSEND instructions (S7-1200, S7-1500)](#changes-with-the-tsendtusend-instructions-s7-1200-s7-1500)
- [Changes with the TRCV/TURCV instructions (S7-1200, S7-1500)](#changes-with-the-trcvturcv-instructions-s7-1200-s7-1500)

### Differences between the versions <= V3.x and >= V4.1 of the OUC library (S7-1200, S7-1500)

#### Introduction

CPU S7-1200 as of firmware version 4.1 supports new instruction versions for Open User Communication (OUC). The new instructions are included in the library with version 4.1.

If you want to use this library, changes must be made to the user program, since some of the new instructions for Open User Communication behave differently.

This section describes the differences in detail, especially in the call behavior of the instructions.

> **Note**
>
> **Description only relevant when upgrading from the CPU S7-1200 ≤ V4.0 to S7-1200 ≥ V4.1**
>
> If you are using an S7-1500 CPU, changes between the library versions are not relevant. The same applies if you are using an S7-1200 ≥ Version 4.1 and do not convert the library for the Open User Communication to versvon &lt;4.1.

#### Differences between the versions &lt;= V3.x and &gt;= V4.1 of the Open User Communication library

The following table shows the instruction that have differences between the versions &lt;= V3.x and &gt;= V4.1 of the Open User Communication library Click on the name of the instruction for detailed information.

| Instruction | Version in library &lt;= V3.x   (CPU FW ≤ V4.0) | Version in library &gt;= V4.1   (CPU FW ≥ V4.1) |
| --- | --- | --- |
| [TSEND_C](#changes-with-the-tsend_c-instruction-s7-1200-s7-1500) | V2.1 | V3.0 |
| [TRCV_C](#changes-with-the-trcv_c-instruction-s7-1200-s7-1500) | V2.1 | V3.0 |
| TMAIL_C * | V2.1 | V3.0 |
| [TCON](#changes-with-the-tcon-instruction-s7-1200-s7-1500) | V3.0 | V4.0 |
| TDISCON | V2.1 | V2.1 (identical to library &lt;= V3.x) |
| [TSEND](#changes-with-the-tsendtusend-instructions-s7-1200-s7-1500) | V3.0 | V4.0 |
| [TRCV](#changes-with-the-trcvturcv-instructions-s7-1200-s7-1500) | V3.0 | V4.0 |
| [TUSEND](#changes-with-the-tsendtusend-instructions-s7-1200-s7-1500) | V3.0 | V4.0 |
| [TURCV](#changes-with-the-trcvturcv-instructions-s7-1200-s7-1500) | V3.0 | V4.0 |
| T_RESET * | V1.1 | V1.2 |
| T_DIAG * | V1.1 | V1.2 |
| T_CONFIG | V1.0 | V1.0 (identical to library &lt;= V3.x) |
| * There are no differences in the versions that affect the user program. |  |  |

> **Note**
>
> **Changing the Open User Communication library from a version &lt;= V3.x to a version &gt;= V4.1**
>
> When replacing the Open User Communication library from a version &lt;= V3.x to a version &gt;= V4.1 you also need to replace the Modbus TCP library. Afterwards check all the instructions relevant for your program.

---

**See also**

[Differences between the versions &lt;= V3.x and &gt;= V4.0 of the Modbus TCP library (S7-1200, S7-1500)](MODBUS%20%28TCP%29%20%28S7-1200%2C%20S7-1500%29.md#differences-between-the-versions-v3x-and-v40-of-the-modbus-tcp-library-s7-1200-s7-1500)
  
[Replacing a hardware component](Configuring%20devices%20and%20networks.md#replacing-a-hardware-component)

### Changes with the TSEND_C instruction (S7-1200, S7-1500)

#### **Call behavior of TSEND_C (V&lt;3.0)**

Up to version 2.1 of the TSEND_C instruction, the DONE output parameter is set twice: Once when a connection is established by the internally used TCON instruction and then after a send operation by the internally used TSEND instruction.

The following diagram shows the connection establishment and the sending of data with TSEND_C V2.1:

![Call behavior of TSEND_C (V&lt;3.0)](images/69715468939_DV_resource.Stream@PNG-en-US.png)

When setting the COM_RST parameter to "1", the current connection establishment or a current data transmission can be reset at any time. This terminates the existing communication connection and a new connection is established.

#### Call behavior of TSEND_C (V≥3.0)

As of the TSEND_C version, the DONE parameter is only set when data transfer has been completed by the internally used TSEND instruction (STATUS = 0000).

![Call behavior of TSEND_C (V≥3.0)](images/69724292875_DV_resource.Stream@PNG-en-US.png)

The existing connection is temporarily interrupted and reset when the COM_RST parameter is set to "1". However, unlike TSEND_C V2.1, the connection endpoint is retained.

> **Note**
>
> **Additional protocols with TSEND_C as of version 3.0**
>
> Version 3.0 of the TSEND_C instruction also supports UDP and UDP Broadcast via the interface of the CPU and via CM/CP.

---

**See also**

[TSEND_C: Send data via Ethernet (S7-1200)](#tsend_c-send-data-via-ethernet-s7-1200)
  
[TSEND_C: Establishing a connection and sending data (S7-1200, S7-1500)](#tsend_c-establishing-a-connection-and-sending-data-s7-1200-s7-1500-1)

### Changes with the TRCV_C instruction (S7-1200, S7-1500)

#### **Call behavior of TRCV_C (V&lt;3.0)**

Up to version 2.1 of the TRCV_C instruction, the DONE output parameter is set after the connection is established. The STATUS output parameter does not distinguish whether the connection or the data transfer has been completed.

The following diagram shows the connection establishment and the sending of data with TRCV_C V2.1:

![Call behavior of TRCV_C (V&lt;3.0)](images/69726776971_DV_resource.Stream@PNG-en-US.png)

The current connection establishment or a current data transmission can be reset at any time by setting the COM_RST parameter to "1". This terminates the existing communication connection and a new connection is established.

#### Call behavior of **TRCV_C** (V≥3.0)

As of the TRCV_C version, the DONE parameter is only set when data transfer has been completed by the internally used TRCV instruction (STATUS = 0000). The completion of the connection establishment by the internally used TCON instruction is displayed by the output value 0x0001 at the STATUS parameter.

![Call behavior ofTRCV_C(V≥3.0)](images/69753556619_DV_resource.Stream@PNG-en-US.png)

The existing connection is temporarily interrupted and reset when the COM_RST parameter is set to "1". However, unlike TSEND_C V2.1, the connection endpoint is retained.

> **Note**
>
> **Additional protocols with TRCV_C as of version 3.0**
>
> Version 3.0 of the TRCV_C instruction also supports UDP and UDP Broadcast via the interface of the CPU and via CM/CP.

> **Note**
>
> **ADHOC mode for the TCP protocol variant**
>
> In accordance with the TRCV instruction, with TRCV_C up to version 2.1, ADHOC mode is activated by assigning the value "0" to the LEN parameter. As of version 3.0 of the instruction, you use the ADHOC parameter for this. You can find detailed information in the descriptions of the instructions.

---

**See also**

[Changes with the TRCV/TURCV instructions (S7-1200, S7-1500)](#changes-with-the-trcvturcv-instructions-s7-1200-s7-1500)
  
[TRCV_C: Receive data via Ethernet (S7-1200)](#trcv_c-receive-data-via-ethernet-s7-1200)
  
[TRCV_C: Establishing a connection and receiving data (S7-1200, S7-1500)](#trcv_c-establishing-a-connection-and-receiving-data-s7-1200-s7-1500-1)

### Changes with the TCON instruction (S7-1200, S7-1500)

#### Changed call behavior with connection errors

**Previous call behavior of** 
**TCON**
 **(V&lt;4.0)**

- The previous TCON instruction (V&lt;4.0) is activated with a rising edge at the REQ input parameter.
- If the remote communication partner cannot be reached, the instruction sets the BUSY output parameter.
- An error message is not output.

The following diagram shows the behavior of TCON on the part of the active connection partner. If no connection is made, the instruction is not called again.

![Changed call behavior with connection errors](images/69578947723_DV_resource.Stream@PNG-en-US.png)

**New call behavior of** 
**TCON** 
**(V≥4.0)**

- The new TCON instruction is also activated with a rising edge at the REQ input parameter.
- Unlike before, an error message is output when the remote communication partner cannot be reached. The error can be queried and the call started again by a new edge at the REQ parameter.
- The following changes result for the user program:

  - Additional error messages of TCON that can be evaluated (see description of [TCON](#tcon-establish-communication-connection-s7-1200-s7-1500)).
  - The connection establishment can be re-initialized via a new rising edge. To do this, query the DONE and ERROR parameters to ensure that an error is present.

The following diagram shows the behavior of TCON on the part of the active connection partner. The instruction is called again after a network error (error code 80C6).

![Changed call behavior with connection errors](images/69547609867_DV_resource.Stream@PNG-en-US.png)

#### Call behavior without communication errors

If there is no connection error, the TCON versions have the same behavior.

The following diagram shows the behavior of TCON on the part of the active connection partner.

![Call behavior without communication errors](images/69579003403_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[TCON: Establish communication connection (S7-1200)](#tcon-establish-communication-connection-s7-1200)

### Changes with the TSEND/TUSEND instructions (S7-1200, S7-1500)

#### Send operation with an established connection

If no delay or interruption occurs during sending, versions 3.0 and 4.0 of the TSEND/TUSEND instructions behave the same way:

- The instruction is started with a positive edge at the "REQ" parameter. The instruction is executed asynchronously, i.e. it must be called until the full execution is indicated by the DONE parameter.
- A maximum of 8 KB of data can be sent with TSEND. A maximum of 1472 bytes with TUSEND (as of firmware version V2.5 of the S7-1500 CPUs for Unicast or Multicast: 2048 bytes). The amounts are based on the full execution of the instruction, i.e. all required calls until the DONE parameter is set.
- Data transmission takes place in three steps:

  - The data is written from the operand area to an internal buffer (indicated by STATUS=7001).
  - The transmission to the remote communication partner follows.
  - If the transmission is successful, DONE is set to "1" and STATUS is reset to "0" (see call 5 in the diagram below).

![Send operation with an established connection](images/69581404555_DV_resource.Stream@PNG-en-US.png)

#### Send operation with time-delayed call

If the send operation is not performed via a communication module (CM) or a communication processor (CP), versions 3.0 and 4.0 of the TSEND/TUSEND instructions behave the same way:

- In the following example, TSEND or TUSEND are only called once with a rising edge at the REQ parameter (see call 2 in the diagram below).
- If the time delay is sufficiently long and the data could be transferred, the DONE parameter is set directly to "1" in the next call (call 3 here).

![Send operation with time-delayed call](images/69592839947_DV_resource.Stream@PNG-en-US.png)

If the send operation is performed via a CM/CP, version 4.0 of the TSEND/TUSEND instructions behaves differently. In this case, the instruction must be called multiple times until the receipt of data is confirmed by the NDR parameter of the TRCV/TURCV instructions.

#### Send operation with interrupted connection

If the connection is interrupted during the send operation, the ERROR and STATUS parameters indicate the error and its cause. In the following example, the connection was interrupted during call number 5 and this error is indicated accordingly with the STATUS parameter.

As of version 4.0 of the TSEND/TUSEND instructions, more STATUS alarms are available that can be correspondingly evaluated (see description of [TSEND](#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)/[TUSEND](#tusend-sending-data-s7-1200-s7-1500)) .

![Send operation with interrupted connection](images/69601523083_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[TSEND: Send data via communication connection (S7-1200)](#tsend-send-data-via-communication-connection-s7-1200)

### Changes with the TRCV/TURCV instructions (S7-1200, S7-1500)

#### Receive operation with an established connection

If no delay or interruption occurs during sending, version 3.0 and 4.0 of the TRCV/TURCV instructions behave the same way:

- A maximum of 8 KB of data can be sent with TRCV. A maximum of 1472 bytes with TURCV (as of firmware version V2.5 of the S7-1500 CPUs for Unicast or Multicast: 2048 bytes). The amounts are based on the full execution of the instruction, i.e. all required calls until the DONE parameter is set.
- The instruction receives data if the EN_R parameter is set to "1".
- The data reception is not complete until the length of data specified at the the LEN parameter has been completely received. The length of the received data is output at the RCVD_LEN output parameter. Only then does the data in the area defined at the DATA parameter become available.

![Receive operation with an established connection](images/69649219979_DV_resource.Stream@PNG-en-US.png)

#### Receive operation with time-delayed call

If the send operation is not performed via a communication module (CM) or a communication processor (CP), versions 3.0 and 4.0 of the TRCV/TURCV instructions behave the same way:

- In the following example, TRCV or TURCV are only called once with a rising edge at the EN_R parameter (see call 2 in the diagram below).
- If the time delay is sufficiently long and the data could be transferred, the NDR parameter is set directly to "1" in the next call (call 3 here).

![Receive operation with time-delayed call](images/69668258571_DV_resource.Stream@PNG-en-US.png)

If the send operation is performed via a CM/CP, version 4.0 of the TSEND/TUSEND instructions behaves differently. In this case, the instruction must be called multiple times until the receipt of data is confirmed by the NDR parameter.

#### Receive operation with interrupted connection

If the connection is interrupted during receiving, the ERROR and STATUS parameters indicate the error and its cause. In the following example, call number 5 resulted in a temporary communication error, which is accordingly indicated by the STATUS parameter.

![Receive operation with interrupted connection](images/69669710475_DV_resource.Stream@PNG-en-US.png)

As of version 4.0 of the TRCV/TURCV instructions, more STATUS alarms are available that can be correspondingly evaluated (see description of [TRCV](#trcv-receive-data-via-communication-connection-s7-1200-s7-1500-1)/[TURCV](#turcv-receiving-data-s7-1200-s7-1500)).

#### Receive operation using ADHOC mode

ADHOC mode is only available with the TCP protocol variant. You can use ADHOC mode to receive data of variable length with the TRCV instruction. If ADHOC mode is active, NDR is set as soon as at least one received byte has been transferred to the receive area.

**Data reception in ADHOC mode with TRCV &lt; 3.0 (S7-1200 &lt; V4.0)**

In the older version of [TRCV](#trcv-receive-data-via-communication-connection-s7-1200), ADHOC mode was activated by setting the LEN parameter to "0". In the following example, 10 bytes of data are transferred with call 5.

![Receive operation using ADHOC mode](images/69673186315_DV_resource.Stream@PNG-en-US.png)

**Data receipt in ADHOC mode with TRCV ≥ 3.0 (S7-1200 ≥ V4.0 or S7-1500)**

As of version 3.0 of the TRCV instruction, ADHOC mode is activated with its own parameter (ADHOC).

![Receive operation using ADHOC mode](images/69677414795_DV_resource.Stream@PNG-en-US.png)

If an error occurs during execution, as of version 4.0 of the TRCV instructions, there are more STATUS alarms available which can be evaluated accordingly.

If the send operation is performed via a CM/CP, version 4.0 of the TRCV/TURCV instructions behaves differently. In this case, the instruction must be called multiple times until the receipt of data is confirmed by the NDR parameter.

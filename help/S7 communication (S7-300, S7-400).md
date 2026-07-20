---
title: "S7 communication (S7-300, S7-400)"
package: ProgKomS7Com34enUS
topics: 27
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# S7 communication (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the S7 communication instructions (S7-300, S7-400)](#overview-of-the-s7-communication-instructions-s7-300-s7-400)
- [Data consistency (S7-300, S7-400)](#data-consistency-s7-300-s7-400)
- [Common parameters of instructions for S7 communication (S7-300, S7-400)](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400)
- [Startup characteristics of instructions for S7 communication (S7-300, S7-400)](#startup-characteristics-of-instructions-for-s7-communication-s7-300-s7-400)
- [Error behavior of instructions for S7 communication (S7-300, S7-400)](#error-behavior-of-instructions-for-s7-communication-s7-300-s7-400)
- [GET: Read data from a remote CPU (S7-300, S7-400)](#get-read-data-from-a-remote-cpu-s7-300-s7-400)
- [PUT: Write data to a remote CPU (S7-300, S7-400)](#put-write-data-to-a-remote-cpu-s7-300-s7-400)
- [USEND: Send data uncoordinated (S7-300, S7-400)](#usend-send-data-uncoordinated-s7-300-s7-400)
- [URCV: Receive data uncoordinated (S7-300, S7-400)](#urcv-receive-data-uncoordinated-s7-300-s7-400)
- [BSEND: Send data in segments (S7-300, S7-400)](#bsend-send-data-in-segments-s7-300-s7-400)
- [BRCV: Receive data in segments (S7-300, S7-400)](#brcv-receive-data-in-segments-s7-300-s7-400)
- [C_CNTRL: Query connection status (S7-300)](#c_cntrl-query-connection-status-s7-300)
- [Others (S7-300)](#others-s7-300)
- [CONTROL: Determine connection status for the instance of an instruction (S7-400)](#control-determine-connection-status-for-the-instance-of-an-instruction-s7-400)
- [PRINT: Send data to printer (S7-400)](#print-send-data-to-printer-s7-400)
- [START: Execute a warm restart or cold restart on a remote device (S7-400)](#start-execute-a-warm-restart-or-cold-restart-on-a-remote-device-s7-400)
- [STOP: Change a remote device to STOP mode (S7-400)](#stop-change-a-remote-device-to-stop-mode-s7-400)
- [RESUME: Initiate a hot restart on a remote device (S7-400)](#resume-initiate-a-hot-restart-on-a-remote-device-s7-400)
- [STATUS: Query the status of a remote partner (S7-400)](#status-query-the-status-of-a-remote-partner-s7-400)
- [USTATUS: Uncoordinated receiving of remote device status (S7-400)](#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400)

## Overview of the S7 communication instructions (S7-300, S7-400)

### Classification

For S7 communication, connection configuration is needed. The integrated communication functions are called in the user program via instructions.

These instructions can be classified in the following categories:

- Instructions for data exchange
- Instructions for changing the operating mode
- Instructions for querying the operating mode
- One instruction each for querying the connection

  > **Note**
  >
  > If your S7-300 CPU does not have an Ethernet interface, you will need a [SIMATIC NET CP](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#industrial-ethernet-s7-300-s7-400) from the S7-300 product range to execute S7-300 instructions. For further information, please see the related documentation.

### Instructions for data exchange

Communication instructions for data exchange are used to exchange data between two communication partners. If a communication instruction exists only on the local module, this is known as data exchange configured at one end. If it exists on the local as well as on the remote module, this is known as data exchange configured at both ends.

| Instruction | Brief description |
| --- | --- |
| "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)" /  "[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)" | Fast unacknowledged exchange of data regardless of the sequential processing of the communication function ("URCV") on the communication partner (for example, operational and maintenance alarms). This means that the data can be overwritten by more recent data at the communication partner. |
| "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" /  "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)" | Secure transfer of a data block to the communication partner. This means that data transmission is not complete until the receive function ("BRCV") on the communication partner has accepted the data. |
| "[GET](#get-read-data-from-a-remote-cpu-s7-300-s7-400)" | Program-controlled reading of tags without additional communication function in the user program of the communication partner. |
| "[PUT](#put-write-data-to-a-remote-cpu-s7-300-s7-400)" | Program-controlled writing of tags without additional communication function in the user program of the communication partner. |
| "[PRINT](#description-of-print-s7-400)" | Send data to a printer (S7-400 only: CP441). |

### Instructions for changing the operating mode

With instructions for changing the operating mode, you control the operating mode of a remote device.

The data exchange instructions for changing the operating mode are configured at one end.

| Instruction | Brief description |
| --- | --- |
| "[START](#start-execute-a-warm-restart-or-cold-restart-on-a-remote-device-s7-400)" | Trigger a WARM RESTART of an S7-300/400 CPU if it is in STOP mode. |
| "[STOP](#stop-change-a-remote-device-to-stop-mode-s7-400)" | STOP of an S7-300/400 CPU if it is in RUN, HOLD, or startup mode |
| "[RESUME](#resume-initiate-a-hot-restart-on-a-remote-device-s7-400)" | Trigger a hot restart of an S7-400 CPU if it is in STOP mode. |

### Instructions for querying the operating mode

With instructions for querying the operating mode, you can obtain information about the operating mode of a remote device.

With the "STATUS" instruction, data exchange is configured at one end, while with the "[USTATUS](#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400)" instruction, data exchange is configured at both ends.

| Instruction | Brief description |
| --- | --- |
| "[STATUS](#status-query-the-status-of-a-remote-partner-s7-400)" | Supplies the operating mode of a communication partner (S7-400 CPU) when requested by the user. |
| "[USTATUS](#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400)" | Receives the operating mode of an S7-400 CPU when it changes its mode, if the corresponding connection attribute (send operating mode messages) has been set. |

### Instruction for querying the connection

| Instruction for S7-400 | Instruction for S7-300 | Brief description |
| --- | --- | --- |
| "[CONTROL](#control-determine-connection-status-for-the-instance-of-an-instruction-s7-400)" | - | Queries the state of a connection that belongs to an instance of an instruction. |
| - | "[C_CNTRL](#c_cntrl-query-connection-status-s7-300)" | Query the status of a connection using the connection ID. |

> **Note**
>
> You can also use the "[C_DIAG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#c_diag-determine-current-connection-status-s7-400)" instruction to diagnose the current connection status (for S7-400 only).

## Data consistency (S7-300, S7-400)

### Definition

The size of the data area which can be modified simultaneously by concurrent processes is called the consistent data area. Data areas which are larger than the consistent data area can thus be falsified as a whole.

This means that a data area which belongs together and which is larger than consistent data area can consist in part of new and of old consistent data blocks at the same time.

### Example

An inconsistency can arise if a communication block is interrupted, for example, by a hardware interrupt OB with a higher priority. If the user program in this OB now changes the data which have already been processed in part by the communication block, the transferred data originate:

- In part from the time before the hardware interrupt was processed
- And in part from the time after the hardware interrupt was processed

This means that these data are inconsistent (not coherent).

### Effect

If larger packages of data are to be transferred in a consistent form, the transfer should not be interrupted. This can, for example, increase the interrupt reaction time of the CPU.

### Data consistency with SIMATIC

- If the user program includes a communication function, for example "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" / "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)" that accesses common data, access to this data area can, for example, be coordinated using the DONE parameter. The data consistency of the communication areas which are transferred locally with a communication block can therefore be ensured in the user program.
- However, in the case of S7 communication functions, for example "[PUT](#put-write-data-to-a-remote-cpu-s7-300-s7-400)" / "[GET](#get-read-data-from-a-remote-cpu-s7-300-s7-400)" or write/read using OP communication, the size of the consistent data areas must already be taken into consideration during programming or configuration, since no communication block is available in the user program of the target device (server) to synchronize communication data in the user program.
- With the S7-300, the communication data are copied consistently into the user memory in blocks of 32 bytes in the cycle control point of the operating system. Data consistency is not guaranteed for larger data areas. If a defined data consistency is required, the communication data in the user program may not exceed 32 bytes (maximum of 8 bytes, depending on the version).

- In the S7-400 by contrast the communication data are not processed in the cycle control point, but in fixed time slices during the program cycle. The consistency of a tag is ensured by the system.
- These communication areas can then be accessed consistently using the "[PUT](#put-write-data-to-a-remote-cpu-s7-300-s7-400)" / "[GET](#get-read-data-from-a-remote-cpu-s7-300-s7-400)" instructions or when reading/writing tags, for example by an OP or an OS.

  > **Note**
  >
  > Additional information on data consistency is provided in the description of the specific instructions.

## Common parameters of instructions for S7 communication (S7-300, S7-400)

### Classification

The parameters of the instructions for S7 communication can be divided into the following five categories according to their functions:

1. Control parameters are used to activate an instruction.
2. Addressing parameters are used to address the remote communication partner.
3. Send parameters point to the data areas that are to be sent to the remote partner.
4. Receive parameters point to the data areas where the data received from remote partners will be entered.
5. Status parameters are used to monitor whether the instruction has completed its task without error or for the analysis of any errors that have occurred.

### Control parameters

Data exchange will only be activated if the appropriate control parameters have a defined value (for example, are set) when the instruction is called or when the value has undergone a specific change since the previous call (for example, a positive edge).

> **Note**
>
> **First call for S7-300**
>
> For the first call, set the REQ parameter to FALSE .

### Addressing parameters

| Parameters | Description |
| --- | --- |
| ID | Reference to the local connection description (specified by the configuration of the connection). Note: The ID W#16#EEEE is not permitted for S7communication instructions. |
| R_ID | With the R_ID parameter, you specify that a send and a receive instruction belong together: The R_ID parameter must match in the instruction at the sending end and the instruction at the receiving end.  This allows the communication of several instruction pairs via the same logic connection.  - R_ID must be specified in the form DW#16#wxyzWXYZ. - The instruction pairs of a logical connection specified in R_ID must be unique for this connection. |

The PI_NAME parameter is only described for the relevant instructions (S7-400 only).

> **Note**
>
> **Addressing parameters ID and R_ID**
>
> **S7-300:** You can change the settings of the addressing parameters ID and R_ID during runtime. The new parameters are validated with each new job after the previous job has been closed.
>
> You can use the following options to reduce the number of instance DBs and therefore the work memory required:
>
> 1. With tag IDs, you can use several connections via one data instance block.
> 2. With tag R_IDs, you can define several pairs of sending and receiving instructions for one job with a single instance.
> 3. You can combine cases 1 and 2.
>
> Please note that the new parameters are valid after the last job is executed. When you activate the sending operation, the R_ID parameter in the instruction at the sending end must match its counterpart at the receiving end.
>
> **S7-400:** The ID and R_ID addressing parameters are evaluated only when the instruction is called the first time or when loading the instance over another (the actual parameters or the predefined values from the instance). The first call therefore specifies the communication relation (connection) with the remote partner until the next warm or cold restart.

### Status parameters

With the status parameters, you monitor whether the instruction has completed its task correctly or whether it is still active. The status parameters also indicate errors.

> **Note**
>
> The status parameters are valid for one cycle only, namely from the first command following the call until the next call. As a result, you must evaluate these parameters after each instruction cycle.

### Send and receive parameters

If you do not use all send or receive parameters of an instruction, the first unused parameter must be a NIL pointer and the parameters used must be located one after the other without any gaps.

> **Note**
>
> **First call for S7-400**
>
> During the first call, the ANY pointer specifies the maximum amount of user data that can be transferred for the job. On the basis of this, a communication data buffer is created in the work memory of the CPU to ensure data consistency. This buffer occupies up to 480 bytes of work memory. We recommend you run the first call in the warm or cold restart OB if the block is not reloaded with the instruction call when the CPU is in RUN mode.
>
> At subsequent calls you can send/receive any amount of data, however, no more than with the first call.
>
> The "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" and "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)" instructions are an exception to this rule. You can use them to transfer up to 64 kbytes per job.

For communication instructions configured at both ends

- The number of the SD_i and RD_i parameters used must match at the send and receive end.
- The data types of the SD_i and RD_i parameters that belong together must match at the send and receive end.
- The amount of data to be sent according to the SD_i parameter must not exceed the range made available by the corresponding RD_i (does not apply to "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" / "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)").

If you do not keep to the rules above, this is indicated by ERROR = 1 and STATUS = 4.

### User data size

With the "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)", "[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)", "[GET](#get-read-data-from-a-remote-cpu-s7-300-s7-400)" and "[PUT](#put-write-data-to-a-remote-cpu-s7-300-s7-400)" instructions, the amount of data to be transmitted must not exceed a defined user data length. The maximum user data size depends on:

- The instruction used
- The communication partner.

The guaranteed minimum size of the user data for an instruction with 1-4 tags is listed in the following table:

| Instruction | Partner: S7-300 | Partner: S7-400 |
| --- | --- | --- |
| PUT / GET | 160 bytes | 400 bytes |
| USEND / URCV | 160 bytes | 440 bytes |
| BSEND / BRCV | 32768/65534 bytes | 65534 bytes |

Further information on the user data size can be found in the technical data of the respective CPU.

### Exact user data size

If the user data size specified above is insufficient you can determine the maximum byte length of the user data as follows:

- First read the data block size valid for communication from the following table:

| Local CPU | Remote CPU | Data block size in bytes |
| --- | --- | --- |
| S7-300 | Any | 240 (S7-300) |
| S7-400 | S7-300 | 240 (S7-400) |
| S7-400 | S7-400 | 480 |

- Use this value in the following table to read the maximum possible user data length in bytes as total of the parameters used. It applies for even lengths of the areas SD_i, RD_i, and ADDR_i. For each range of uneven length the maximum possible user data length is reduced by one byte.

|  |  | Number of SD_i, RD_i, ADDR_i parameters used |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Data block size | Instruction | 1 | 2 | 3 | 4 |
| 240 (S7-300) | PUT/GET/ USEND | 160 | - | - | - |
| 240 (S7-300 via integrated interface) | PUT | 212 | - | - | - |
| GET | 222 | - | - | - |  |
| USEND | 212 | - | - | - |  |
| 240 (S7-400) | PUT | 212 | 196 | 180 | 164 |
| GET | 222 | 218 | 214 | 210 |  |
| USEND | 212 | - | - | - |  |
| 480 | PUT | 452 | 436 | 420 | 404 |
| GET | 462 | 458 | 454 | 450 |  |
| USEND | 452 | 448 | 444 | 440 |  |

## Startup characteristics of instructions for S7 communication (S7-300, S7-400)

### Requirements

In the following description for S7-400, it is assumed that:

- The connection descriptions (SDBs) exist on the modules.
- The configured connections have been established.
- The actual parameter for ID matches the configured connection ID for each instruction.

### Warm restart and cold restart

During a warm and a cold restart, all instructions are set to the NO_INIT status. The actual parameters stored in the instance DBs are unchanged.

### Warm restart and cold restart with data exchange instructions configured at both ends

With data exchange instructions configured at both ends, the two modules do not normally both run a warm or cold restart at he same time. The adjustment is made implicitly by the instruction based on the following rules.

- The receive blocks ("[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)", "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)") react as follows:

  - If the instruction has received a job but has not acknowledged this job at the time of the warm or cold restart, it generates a sequence abort frame ("[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)") and then immediately branches to the NO_INIT status.
  - With "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)", it is possible that another data segment will be received despite the transferred sequence abort. This will be discarded locally.
  - With "[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)", the change to the NO_INIT status occurs immediately.
- The send blocks ("[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)", "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)") react as follows:

  - If the "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" instruction has started a job sequence that has not yet been completed, it sends a sequence abort during the warm or cold restart. It then branches to the NO_INIT status immediately afterwards. An acknowledgement that arrives at a later time is discarded locally.
  - If the "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" instruction has already sent or received a sequence abort when the warm or cold restart is requested, it changes immediately to the NO_INIT status.
  - In all other cases and if the instruction sends only alarms (for example, "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)"), local processing is aborted and the instruction immediately branches to the NO_INIT status.

### Warm restart and cold restart with data exchange instructions configured at one end

It is assumed that the server on the communication partner is operational after the connections have been established, in other words that it can process jobs or output alarms at any time.

Instructions that send out jobs and expect acknowledgements respond as follows:

- The current processing is aborted followed by a branch to the NO_INIT status immediately afterwards. If an acknowledgement for the job sent prior to the warm or cold restart arrives later, it is discarded locally.
- A new job may have been sent before the acknowledgement of the earlier job is received.

Instructions that output or receive alarms react as follows:

- The current processing is aborted followed by a branch to the NO_INIT status immediately afterwards.
- With "[USTATUS](#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400)", alarms that arrive during the NO_INIT and DISABLED statuses are discarded locally.

### Hot restart

The instructions for S7 communication are set to the NO_INIT status only during a warm or cold restart. This means that they react like user function blocks that can be resumed following a hot restart.

### Memory reset

A memory reset always causes all connections to be terminated. Since a warm or cold restart is the only possible startup type for the user program after a memory reset, all instructions for S7 communication (if they still exist) are set to the NO_INIT status and initialized. Partner blocks in a module whose memory was not reset change to the IDLE or ENABLED or DISABLED statuses as a reaction to the connection being aborted.

## Error behavior of instructions for S7 communication (S7-300, S7-400)

### Introduction

The following section describes how instructions for S7 communication in S7-400 react to problems.

### Connection abort

The connections assigned to the instruction instances are monitored for aborts.

If a connection is aborted, the reaction of the instruction depends on its internal status:

- If the connection abort is detected in the IDLE or ENABLED status, the instruction reacts as follows:

  - It branches to the ERROR status and outputs the error ID "Communication problems" at the ERROR and STATUS output parameters.
  - When it is next called, the instruction returns to its original status and checks the connection again.
- An instruction that is not in the IDLE or DISABLED status reacts as follows:

  - It aborts its processing, changes to the ERROR status immediately or at the next call, and outputs the error ID "Communication problems" at the ERROR and STATUS output parameters.
  - When it is next called, the instruction changes to the IDLE, DISABLED or ENABLED status. In the IDLE and ENABLED statuses, the connection is checked again.

This procedure will also be executed if the connection has again been set up in the meantime.

### Power down

A power down with battery backup followed by a restart causes all established connections to be terminated. Therefore, the points made above apply to all instructions involved.

If there is a power down with battery backup followed by an automatic warm or cold restart, the points made about terminated connections and warm or cold restarts apply.

In the special case of an automatic warm or cold restart without battery backup, where a memory reset is executed automatically after power returns, the instructions for S7 communication react as described in the "[Startup characteristics of instructions for S7 communication](#startup-characteristics-of-instructions-for-s7-communication-s7-300-s7-400)" section.

### Reaction to operating mode changes

If there is an operating mode change between the STOP, STARTUP, RUN, and HOLD modes, the instruction remains in its current status (exception: During a warm or cold restart, it changes to the NO_INIT status). This applies both to communications instructions configured at one end and at both ends.

### Error interface to the user program

If an error occurs during the processing of an instruction, it always changes to the ERROR status. At the same time, the ERROR output parameter is set to "1" and the corresponding error ID is entered in the STATUS output parameter. You can evaluate this information in your program.

Examples of possible errors:

- Error when collecting send data.
- Error when copying receive data into the receive areas (for example, attempting to access a DB that does not exist)
- The length of the data area sent does not match the length of the receive area specified in the partner instruction.

## GET: Read data from a remote CPU (S7-300, S7-400)

### Description

With the help of the instruction, you can read data from a remote CPU if the connection does not take place via a CP.

- **S7-300:** The data is read on a positive edge at REQ. The parameter values ID, ADDR_1 and RD_1 are adopted on each positive edge at REQ . After a job has been completed, you can assign new values to the ID, ADDR_1 and RD_1 parameters.
- **S7-400:** The instruction is started on a positive edge at control input REQ . The relevant pointers to the areas to be read out (ADDR_i) are then sent to the partner CPU.

The remote partner returns the data. The received data is copied to the configured receive areas (RD_i) at the next call. Make sure that the areas defined with the parameters ADDR_i and RD_i match in terms of number, length and data type.

Completion of this action is indicated by the status parameter NDR having the value "1". Reading can only be activated again after the previous reading process has been completed.

The remote CPU can be in RUN or STOP mode. Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being read or if the data type check results in an error.

### Parameters

The following table shows the parameters of the "GET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR /   STATUS | Output   Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| **S7-300:** ADDR_1     **S7-400:** ADDR_i   (1≤ i ≤4) | InOut | ANY | S7-300: M, D       S7-400: I, Q, M, D, T, C | Pointers to the areas on the partner CPU that are to be read.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10).  When transferring data structures (e.g., Struct, Array), the data type CHAR, BYTE, WORD or DWORD must be used at the ADDR parameter. |
| **S7-300:** RD_1     **S7-400:** RD_i   (1≤ i ≤4) | InOut | ANY | S7-300: M, D    S7-400: I, Q, M, D, T, C | Pointers to the areas on the local CPU in which the read data is entered.  Only the data types BOOL are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for the "GET" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   - Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 4 | Errors in the receive area pointers RD_i relating to the data length or the data type. |
| 1 | 8 | Access error on the partner CPU. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "GET" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 20 | - **S7-400**    Not enough work memory. Remedy: Reduce the program code in the memory. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.)   - Possible when first called |
| 1 | 27 | **For S7-300 only:** No function code for this instruction exists in the CPU. |

### Data consistency

The data is received in a consistent state if the following point is observed:

Evaluate the part of the receive area RD_i currently being used completely before initiating another job.

## PUT: Write data to a remote CPU (S7-300, S7-400)

### Description

With the help of the instruction, you can write data to a remote CPU if the connection does not take place via a CP.

- **S7-300:** The data is sent on a positive edge at REQ. The parameter values ID, ADDR_1 and SD_1 are adopted on each positive edge at REQ. After a job has been completed, you can assign new values to the ID, ADDR_1 and SD_1 parameters.
- **S7-400:** The instruction is started on a positive edge at control input REQ. The pointers to the areas to be written (ADDR_i) and the data (SD_i) are then sent to the partner CPU.

The remote partner saves the required data under the addresses supplied with the data and returns an execution acknowledgement. Make sure that the areas defined with the parameters ADDR_i and SD_i match in terms of number, length and data type.

If no errors occur, this is indicated at the next call with status parameter DONE = "1". The writing process can only be activated again after the last job is complete.

The remote CPU can be in RUN or STOP mode. Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being written or if the execution check results in an error.

### Parameters

The following table shows the parameters of the "PUT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job executed without errors. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| **S7-300:** ADDR_1     **S7-400:** ADDR_i (1≤ i ≤4) | InOut | ANY | S7-300: M, D       S7-400:  I, Q, M, D, T, C | Pointers to the areas on the partner CPU to which the data will be written.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10).  When transferring data structures (e.g., Struct, Array), the data type CHAR, BYTE, WORD or DWORD must be used at the ADDR parameter. |
| **S7-300:** SD_1     **S7-400:** SD_i  (1≤ i ≤4) | InOut | ANY | S7-300: M, D    S7-400:  I, Q, M, D, T, C | Pointers to the areas on the local CPU which contain the data to be sent.  Only the data types BOOL are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for PUT that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   - Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 4 | Errors in the send area pointers SD_i relating to the data length or the data type |
| 1 | 8 | Access error on the partner CPU. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB) |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "PUT" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 20 | - **S7-400**     Not enough work memory. Remedy: Load the associated instance DB again. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded at CPU-RUN (STOP-RUN transition of the CPU or CP required).   - Possible when first called |
| 1 | 27 | **For S7-300 only:** No function code for this instruction exists in the CPU. |

### Data consistency for S7-300:

To ensure data consistency, send area SD_1 may not be written to again until the current send job has been completed. This is the case when the value of the status parameter DONE changes to "1".

### Data consistency for S7-400 and S7-300 via an integrated interface:

When a send operation is activated (rising edge at REQ), the data to be sent from the send area SD_i is copied from the user program. After the instruction call, you can write to these areas again without corrupting the current send data.

> **Note**
>
> The send operation is only complete when the DONE status parameter has the value "1".

## USEND: Send data uncoordinated (S7-300, S7-400)

### Description

The "USEND" instruction sends data to a remote partner instruction of type "[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)". The sending process is carried out without coordination with the partner instruction. This means that the data transfer is carried out without acknowledgment by the partner instruction.

- **S7-300:** The data is sent on a positive edge at REQ. The parameter values R_ID, ID and SD_1 are adopted on each positive edge at REQ . After a job has been completed, you can assign new values to the R_ID, ID and SD_1 parameters.
- **S7-400:**The data is sent on a positive edge at control input REQ. The data to be sent is referenced by the parameters SD_1, ... SD_4 (it is not necessary for all four send parameters to have a value).

You must, however, make sure that the areas defined by the parameters SD_1 to SD_4 / SD_1 and RD_1 to RD_4 / RD_1 (with the associated partner instruction "[URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400)") match in terms of:

- Number
- Length and
- Data type

The R_ID parameter must be identical in both instructions.

Successful completion of the send operation is indicated when the value of the DONE status parameter is set to logical "1".

### Parameters

The following table shows the parameters of the "USEND" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a positive edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job executed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| **S7-300:** SD_1     **S7-400:** SD_i  (1≤ i ≤4) | InOut | ANY | S7-300: M, D    S7-400:  I, Q, M, D, T, C | Pointer on the i-th send area. Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   - Maximum number of parallel jobs/instances exceeded |
| 1 | 4 | Errors in the send area pointers SD_i relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "USEND" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection ID. - Also for S7-300:   The instances were overloaded at CPU-RUN (STOP-RUN transition of the CPU or CP required). |
| 1 | 20 | - **S7-400**    Not enough work memory. Remedy: Reduce the program code in the memory. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded at CPU-RUN (STOP-RUN transition of the CPU or CP required).   - Possible when first called |
| 1 | 27 | **For S7-300 only:** No function code for this instruction exists in the CPU. |

### Data consistency

**S7-300:** To ensure data consistency, send area SD_1 may not be written to again until the current send job has been completed. This is the case when the value of the status parameter DONE changes to "1".

**S7-400 and S7-300 via an integrated interface:** When a send operation is activated (positive edge at REQ), the data to be sent from the send area SD_i is copied from the user program. After the instruction call, you can write to these areas again without corrupting the current send data.

> **Note**
>
> The send operation is only complete when the DONE status parameter has the value "1".

## URCV: Receive data uncoordinated (S7-300, S7-400)

### Description

The "URCV" instruction receives data asynchronously from a remote partner instruction of type "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)" and copies this data into the configured receive areas.

The instruction is ready to receive if there is a logical 1 at the EN_R input. An active job can be canceled with EN_R=0.

- **S7-300:** The parameters R_ID, ID and RD_1 are adopted on each positive edge at EN_R. After a job has been completed, you can assign new values to the R_ID, ID and RD_1 parameters.
- **S7-400:** The receive data areas are referenced by the parameters RD_1 to RD_4.

Make sure that the areas defined by the parameters RD_i / RD_1 and SD_i / SD_1 (with the associated partner instruction "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)") match in terms of:

- Number
- Length and
- Data type

Successful completion of the copy operation is indicated when the value of the NDR status parameter is set to logical "1". The R_ID parameter must be identical in both instructions.

### Parameters

The following table shows the parameters of the "URCV" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive, signals ready to receive if the input is set. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| **S7-300:** RD_1     **S7-400:** RD_i  (1≤ i ≤4) | InOut | ANY | S7-300: M, D    S7-400: I, Q, M, D, T, C | Pointer to the i-th receive area: Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 9 | Overrun warning: older received data were overwritten by newer received data. |
| 0 | 11 | Warning: The received data is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   Maximum number of parallel jobs/instances exceeded |
| 1 | 4 | Errors in the receive area pointers RD_i relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "URCV" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection ID. - Also for S7-300:   The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) |
| 1 | 19 | The associated "[USEND](#usend-send-data-uncoordinated-s7-300-s7-400)" instruction sends data faster than this can be copied to the receive areas by "URCV". |
| 1 | 20 | - **S7-400**    Not enough work memory. Remedy: Reduce the program code in the memory. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.)   - Possible when first called |
| 1 | 27 | **For S7-300 only:** No function code for this block exists in the CPU. |

### Data consistency

The data is received in a consistent state if the following point is observed:

- **S7-300:** After the status parameter NDR has changed to value "1", you must call "URCV" again immediately with value "0" at EN_R. This ensures that the receive area is not already overwritten before you have evaluated it. Evaluate the receive area RD_1 completely before you call the block with value "1" at control input EN_R.
- **S7-400:** After the status parameter NDR has changed to the value "1", there is new receive data in your receive areas (RD_i). A new block call may cause these data to be overwritten with new receive data. If you want to prevent this, call "URCV" (for example, during cyclic block processing) with the value 0 at EN_R until you have finished processing the received data.

## BSEND: Send data in segments (S7-300, S7-400)

### Description

The "BSEND" instruction sends data to a remote partner instruction of type "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)". With this type of data transfer, more data can be transported between the communication partners than is possible with all other communication instructions for configured S7 connections. The following aggregates can be transferred:

- 32768 bytes for S7-300 via SIMATIC-Net CPs
- 65534 bytes for S7-400 and S7-300 via an integrated interface

### Functional description

The data area to be transmitted is segmented. Each segment is sent individually to the partner. The last segment is acknowledged by the partner when it is received, regardless of the associated "[BRCV](#brcv-receive-data-in-segments-s7-300-s7-400)" call.

- **S7-300:** The data is sent on a positive edge at REQ. The parameters R_ID, ID, SD_1 and LEN are adopted on each positive edge at REQ . After a job has been completed, you can assign new values to the R_ID, ID, SD_1 and LEN parameters. To transfer segmented data, the instruction must be called cyclically in the user program.  
  The start address and the maximum length of the data to be sent are specified by SD_1. The length of the data block is specified by LEN based on the job.
- **S7-400 and S7-300 via an integrated interface:** The send operation is activated after the instruction is called and a positive edge on control input REQ. Sending the data from the user memory is asynchronous to the execution of the user program.  
  The start address of the data to be sent is specified by SD_1. The length of the send data is specified by LEN based on the job. In this case, LEN replaces the length section of SD_1.

The R_ID parameter must be identical in the related instructions. If there is a positive edge at control input R, the current sending process is canceled. Successful completion of the send operation is indicated by the value of the DONE status parameter being set to "1".

A new send job cannot be processed until the previous send operation has been completed and the status parameter DONE or ERROR has the value "1".

Due to the asynchronous data transfer, a new data transfer can only be initiated if the previous data has been fetched by a partner instruction call. Until the data is fetched, the status value "7" (see below) will be output when "BSEND" is called.

### Parameters

The following table shows the parameters of the "BSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange at a positive edge |
| R | Input | BOOL | I, Q, M, D, L | Control parameter reset, activates an abort of the current data exchange at a positive edge |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400)   If there is a connection via a CP 441 to S5 or third-party devices, R_ID contains the address information of the remote device. For further information, refer to the description of the CP 441. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job completed without error. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies   detailed information - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| SD_1 | InOut | ANY | S7-300: M, D    S7-400:  I, Q, M, D, T, C | Pointer to the send area.  Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified. (For example: P#DB10.DBX5.0 byte 10) |
| LEN | InOut | WORD | I, Q, M, D, L | Length of the data field to be sent in bytes |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for "BSEND" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | - Communication problems, for example: Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Negative acknowledgment of partner instruction. The function cannot be executed. |
| 1 | 3 | R_ID is unknown on the connection specified by the ID or the receive block  has not yet been called. |
| 1 | 4 | Error in the send area pointer SD_1 involving the data length or the data  type, or the value "0" was transferred at the LEN parameter. |
| 1 | 5 | Reset request was executed. |
| 1 | 6 | Partner instruction is in DISABLED status (EN_R has the value "0"). Also check the input parameters of BRCV for consistency with BSEND. |
| 1 | 7 | Partner instruction is in the wrong state.   The receive instruction was not called again after the last data transmission. |
| 1 | 8 | Access to remote object in the user memory was rejected: The destination area for the associated "BRCV" is too small.  The corresponding BRCV reports ERROR  = 1, STATUS  = 4 or ERROR = 1, STATUS = 10. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - an instance DB was specified that does not belong to "BSEND" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection. - Also for S7-300:   The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) |
| 1 | 20 | - **S7-400**    Not enough work memory. Remedy: Reduce the program code in the memory. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.)   - Possible when first called   - Memory bottleneck in CP |
| 1 | 27 | **For S7-300 only:** No function code for this instruction exists in the CPU. |

### Data consistency

To ensure data consistency, you may only write to the part of the currently used sending area SD_1 after the current send operation is complete. This is the case when the value of the status parameter DONE changes to "1".

## BRCV: Receive data in segments (S7-300, S7-400)

### Description

The "BRCV" instruction receives data from a remote partner instruction of type "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)". After each received data segment, an acknowledgment is sent to the partner instruction and the LEN parameter is updated.

The instruction is ready to receive data after it is called with the value "1" at control input EN_R. An active job can be canceled with EN_R=0.

The start address and the maximum length of the receive area are specified by RD_1. The length of the received block of data is shown in LEN .

- **S7-300:** The parameters R_ID, ID and RD_1 are adopted on each positive edge at EN_R. After a job has been completed, you can assign new values to the R_ID, ID and RD_1 parameters. For the transmission of segmented data, the instruction must be called cyclically in the user program.
- **S7-400 and S7-300 via an integrated interface:** Receipt of the data from the user memory is asynchronous to the execution of the user program.

The R_ID parameter must be identical in the related instructions.

Value "1" at the NDR status parameter indicates that all data segments have been received without error. The received data remains unchanged until the next call with EN_R=1.

If the instruction is called again while data is being received asynchronously, this leads to a warning being output in the STATUS parameter; if the call is made with EN_R=0, receiving is canceled and the instruction returns to its initial state.

### Parameters

The following table shows the parameters of the "BRCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive, signals ready to receive if the input is set. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400)   If there is a connection via a CP 441 to S5 or third-party devices, R_ID contains the address information of the remote device. For further information, refer to the description of the CP 441. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| RD_1 | InOut | ANY | S7-300: M, D    S7-400: I, Q, M, D, T, C | Pointer to the receive area. The length information specifies the maximum length of the block to be received.   Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** When the ANY pointer accesses a DB, the DB must always be specified.  (For example: P# DB10.DBX5.0 byte 10). |
| LEN | InOut | WORD | I, Q, M, D, L | Length of the data already received in bytes. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for "BRCV" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: The received data is already being processed in a priority class with lower priority. |
| 0 | 17 | Warning: Instruction receives data asynchronously. The LEN parameter shows the amount of data already received in bytes. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Also for S7-300:   Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Function cannot be executed (protocol error) |
| 1 | 4 | Error in the receive area pointer RD_1 relating to the data length or data type. The block of data sent is longer than the receive area. |
| 1 | 5 | Reset request received, incomplete transfer. |
| 1 | 8 | Access error in associated "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)": After the last valid data segment has been sent, ERROR  = 1 and STATUS  = 4 or ERROR = 1 and STATUS = 10 is reported. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "BRCV" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection. - Also for S7-300:   The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) |
| 1 | 20 | - **S7-400**    Not enough work memory. Remedy: Reduce the program code in the memory. - **S7-300**    - Maximum number of parallel jobs/instances exceeded   - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.)   - Possible when first called   - Memory bottleneck in CP |
| 1 | 27 | **For S7-300 only:** No function code for this instruction exists in the CPU. |

### Data consistency

The data is received in a consistent state if the following point is observed: Evaluate the currently used part of the receive area RD_1 completely before you call the block again with the value 1 at control input EN_R.

### Special case for receiving data (S7-400 only)

If the receiving CPU has a "BRCV" instruction that is ready to receive data (in other words, a call with EN_R =1 has already been made) and the CPU changes to STOP mode before the corresponding send instruction has sent the first data segment of a job, the following will occur:

- The data in the first job after the receiving CPU has gone into STOP mode are fully entered in the receive area.
- The "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" partner instruction receives a positive acknowledgment of this.
- No more "[BSEND](#bsend-send-data-in-segments-s7-300-s7-400)" jobs can be accepted by a receiving CPU in STOP mode.
- As long as the CPU remains in STOP mode, both NDR and LEN have the value "0".

To prevent information about the received data being lost, perform a hot restart on the receiving CPU and call "BRCV" with EN_R=1.

## C_CNTRL: Query connection status (S7-300)

### Description

With this instruction, you query the status of a connection **for S7-300**. The current status of the connection addressed by ID is obtained following the instruction call with value "1" at the EN_R control input.

### Parameters

The following table shows the parameters of the "C_CNTRL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter, signals ready to receive if the input is set. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| C_CONN | Output | BOOL | I, Q, M, D, L | Status of the corresponding connection.  Possible values:  - 0: Connection aborted or not yet established. - 1: Connection available. |
| C_STATUS | Output | WORD | I, Q, M, D, L | Connection status:  - W#16#0000: Connection is not set up - W#16#0001: Connection is being set up - W#16#0002: Connection is set up - W#16#000F: No data on connection status available (for example during CP startup) - W#16#00FF: Connection is not configured |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters RET_VAL, ERROR and STATUS

The RET_VAL output parameter can have the following two values for the "C_CNTRL" instruction:

- 0000H: No error occurred during execution.
- 8000H: An error occurred during execution.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 1 | 10 | CP access error. Another job is currently running. Repeat job later. |
| 1 | 27 | There is no function code on the CPU for this instruction. |

> **Note**
>
> The output parameters ERROR and STATUS need to be evaluated even if the output parameter RET_VAL shows the value 0000H .

## Others (S7-300)

This section contains information on the following topics:

- [GET_S: Read data from a remote CPU (S7-300)](#get_s-read-data-from-a-remote-cpu-s7-300)
- [PUT_S: Write data to a remote CPU (S7-300)](#put_s-write-data-to-a-remote-cpu-s7-300)
- [USEND_S: Send data uncoordinated (S7-300)](#usend_s-send-data-uncoordinated-s7-300)
- [URCV_S: Receive data uncoordinated (S7-300)](#urcv_s-receive-data-uncoordinated-s7-300)

### GET_S: Read data from a remote CPU (S7-300)

#### Description

With this instruction, you can read data from a remote CPU **with S7-300**. The connection can take place via the integrated interface as well as a CP.

The data is read on a rising edge at REQ. The parameter values ID, ADDR_1 and RD_1 are adopted on each positive edge at REQ . After a job has been completed, you can assign new values to the ID, ADDR_1 and RD_1 parameters.

The remote partner returns the data. The received data is copied to the configured receive areas (RD_1) at the next call. Make sure that the areas defined with the parameters ADDR_1 and RD_1 match in terms of number, length and data type.

Completion of this action is indicated by the status parameter NDR having the value "1". Reading can only be activated again after the previous reading process has been completed.

The remote CPU can be in RUN or STOP mode. Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being read or if the data type check results in an error.

#### Parameters

The following table shows the parameters of the "GET_S" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR /   STATUS | Output   Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| ADDR_1 | InOut | ANY | M, D | Pointers to the areas on the partner CPU that are to be read. |
| RD_1 | InOut | ANY | M, D | Pointers to the areas on the local CPU in which the read data is entered.  Only the data types BOOL are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information for the "GET_S" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 4 | Errors in the receive area pointers RD_1 relating to the data length or the data type. |
| 1 | 8 | Access error on the partner CPU. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "GET_S" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 20 | - Maximum number of parallel jobs/instances exceeded - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) - Possible when first called |
| 1 | 27 | There is no function code on the CPU for this instruction. |

#### Data consistency

The data is received in a consistent state if the following point is observed:

Evaluate the part of the receive area RD_1 currently being used completely before initiating another job.

### PUT_S: Write data to a remote CPU (S7-300)

#### Description

With this instruction, you can write data to a remote CPU **with S7-300**. The connection can take place via the integrated interface as well as a CP.

The data is sent on a rising edge at REQ. The parameter values ID, ADDR_1 and SD_1 are adopted on each positive edge at REQ. After a job has been completed, you can assign new values to the ID, ADDR_1 and SD_1 parameters.

The remote partner saves the required data under the addresses supplied with the data and returns an execution acknowledgement. Make sure that the areas defined with the parameters ADDR_1 and SD_1 match in terms of number, length and data type.

If no errors occur, this is indicated at the next call with status parameter DONE = "1". The writing process can only be activated again after the last job is complete.

The remote CPU can be in RUN or STOP mode. Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being written or if the execution check results in an error.

#### Parameters

The following table shows the parameters of the "PUT_S" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job executed without errors. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| ADDR_1 | InOut | ANY | M, D | Pointers to the areas on the partner CPU to which the data will be written. |
| SD_1 | InOut | ANY | M, D | Pointers to the areas on the local CPU which contain the data to be sent.  Only the data types BOOL are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information for "PUT_S" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Maximum number of parallel jobs/instances exceeded. |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 4 | Errors in the send area pointers SD_1 relating to the data length or the data type. |
| 1 | 8 | Access error on the partner CPU. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB) |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "PUT_S" - A global DB was specified instead of an instance DB - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 20 | - Maximum number of parallel jobs/instances exceeded - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) - Possible when first called |
| 1 | 27 | There is no function code on the CPU for this instruction. |

#### Data consistency

To ensure data consistency, send area SD_1 may not be written to again until the current send job has been completed. This is the case when the value of the status parameter DONE changes to "1".

### USEND_S: Send data uncoordinated (S7-300)

#### Description

The instruction "USEND_S" sends data to a remote partner instruction of type "[URCV_S](#urcv_s-receive-data-uncoordinated-s7-300)" **with S7-300**. The sending process is carried out without coordination with the partner instruction. This means that the data transfer is carried out without acknowledgement by the partner instruction.

The data is sent on a rising edge at REQ. The parameter values R_ID, ID and SD_1 are adopted on each positive edge at REQ . After a job has been completed, you can assign new values to the R_ID, ID and SD_1 parameters.

Make sure that the areas defined by the parameters SD_1 and RD_1 (for the associated partner instruction "[URCV_S](#urcv_s-receive-data-uncoordinated-s7-300)") match in terms of:

- Number
- Length and
- Data type

The R_ID parameter must be identical in both instructions.

Successful completion of the send operation is indicated when the value of the DONE status parameter is set to logical "1".

#### Parameters

The following table shows the parameters of the "USEND_S" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job has been executed error-free. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| SD_1 | InOut | ANY | M, D | Pointer to the send area. Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

| ERROR | STATUS(decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Maximum number of parallel jobs/instances exceeded |
| 1 | 4 | Errors in the send area pointers SD_1 relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "USEND_S" - A global DB was specified instead of an instance DB - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection ID. - The instances were overloaded at CPU-RUN (STOP-RUN transition of the CPU or CP required.) |
| 1 | 20 | - Maximum number of parallel jobs/instances exceeded - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) - Possible when first called |
| 1 | 27 | There is no function code on the CPU for this instruction. |

#### Data consistency

To ensure data consistency, send area SD_1 may not be written to again until the current send job has been completed. This is the case when the value of the status parameter DONE changes to "1".

### URCV_S: Receive data uncoordinated (S7-300)

#### Description

The instruction "URCV_S" receives data asynchronously from a remote partner instruction of type "[USEND_S](#usend_s-send-data-uncoordinated-s7-300)" and copies this data into the configured receive areas **with S7-300**.

The instruction is ready to receive if there is a logical 1 at the EN_R input. An active job can be canceled with EN_R=0.

The parameter values R_ID, ID and RD_1 are adopted on each positive edge at EN_R. After a job has been completed, you can assign new values to the R_ID, ID and RD_1 parameters.

Make sure that the areas defined by the parameters RD_1 and SD_1 (for the associated partner instruction "[USEND_S](#usend_s-send-data-uncoordinated-s7-300)") match in terms of:

- Number
- Length
- Data type

Successful completion of the copy operation is indicated when the value of the NDR status parameter is set to logical "1". The R_ID parameter must be identical in both instructions.

#### Parameters

The following table shows the parameters of the "URCV_S" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter enabled to receive, signals ready to receive if the input is set. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| R_ID | Input | DWORD | I, Q, M, D, L or constant | Addressing parameter R_ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still executing. - 1: Job completed without errors. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| RD_1 | InOut | ANY | M, D | Pointer to the i-nth receive area: Only the data types BOOL are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME, COUNTER, TIMER.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P#DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

| ERROR | STATUS(decimal) | Explanation |
| --- | --- | --- |
| 0 | 9 | Overrun warning: Older received data are overwritten by newer received data. |
| 0 | 11 | Warning: The received data is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established - Maximum number of parallel jobs/instances exceeded |
| 1 | 4 | Errors in the receive area pointers RD_1 relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called  - An instance DB was specified that does not belong to "URCV_S" - A global DB instead of an instance DB was specified. - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 18 | - R_ID already exists in the connection ID. - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) |
| 1 | 19 | The associated "[USEND_S](#usend_s-send-data-uncoordinated-s7-300)" instruction sends data faster than this can be copied to the receive areas by "URCV_S". |
| 1 | 20 | - Maximum number of parallel jobs/instances exceeded - The instances were loaded over others with the CPU in RUN (STOP-RUN change required on the CPU or CP.) - Possible when first called |
| 1 | 27 | There is no function code in the CPU for this block. |

#### Data consistency

The data is received in a consistent state if the following point is observed:

After the status parameter NDR has changed to "1", call "URCV_S" again immediately with the value "0" at EN_R. This ensures that the receive area is not already overwritten before you have evaluated it. Evaluate the receive area RD_1 completely before you call the block with value "1" at control input EN_R.

## CONTROL: Determine connection status for the instance of an instruction (S7-400)

### Description

With the "CONTROL" instruction, you can obtain the status of the connection belonging to a local communication instruction instance on an **S7-400**.

After the instruction is called with the value "1" at control input EN_R, the current status of the connection belonging to the communication instruction instance selected with I_DB is queried.

### Parameters

The following table shows the parameters of the "CONTROL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter, signals ready to receive if the input is set. |
| I_DB | Input | WORD | I, Q, M, D, L or constant | Number of the instance DB |
| OFFSET | Input | WORD | I, Q, M, D, L or constant | Offset of the data record in bytes in the multi- instance DB (if no multi-instance DB  exists, "0" must be entered here). |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| I_TYP | Output | BYTE | I, Q, M, D, L | Identifier for the block type belonging to the selected instance. |
| I_STATE | Output | BYTE | I, Q, M, D, L | - = 0: The corresponding instruction instance has not been called since the last cold/warm restart or loading. - <> 0: The corresponding instruction instance has been called at least once since the last cold/warm restart or loading. |
| I_CONN | Output | BOOL | I, Q, M, D, L | Status of the corresponding connection.  Possible values:  - 0: Connection aborted or not yet established. - 1: Connection available. |
| I_STATUS | Output | WORD | I, Q, M, D, L | Status parameter STATUS of the queried  communication instruction instance. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Output parameter I_TYP

The following table lists the different instruction types and the corresponding identifiers

| Instruction type | Identifier (W#16#...) |
| --- | --- |
| [USEND](#usend-send-data-uncoordinated-s7-300-s7-400) | 00 |
| [URCV](#urcv-receive-data-uncoordinated-s7-300-s7-400) | 01 |
| [BSEND](#bsend-send-data-in-segments-s7-300-s7-400) | 04 |
| [BRCV](#brcv-receive-data-in-segments-s7-300-s7-400) | 05 |
| [GET](#get-read-data-from-a-remote-cpu-s7-300-s7-400) | 06 |
| [PUT](#put-write-data-to-a-remote-cpu-s7-300-s7-400) | 07 |
| [PRINT](#description-of-print-s7-400) | 08 |
| [START](#start-execute-a-warm-restart-or-cold-restart-on-a-remote-device-s7-400) | 0B |
| [STOP](#stop-change-a-remote-device-to-stop-mode-s7-400) | 0C |
| [RESUME](#resume-initiate-a-hot-restart-on-a-remote-device-s7-400) | 0D |
| [STATUS](#status-query-the-status-of-a-remote-partner-s7-400) | 0E |
| [USTATUS](#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400) | 0F |
| [ALARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm-create-plc-alarms-with-acknowledgement-display-s7-400) | 15 |
| [ALARM_8](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm_8-create-plc-alarms-without-associated-values-for-eight-signals-s7-400) | 16 |
| [ALARM_8P](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#alarm_8p-create-plc-alarms-without-associated-values-for-eight-signals-s7-400) | 17 |
| [NOTIFY](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#notify-report-a-signal-change-s7-400) | 18 |
| [AR_SEND](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#ar_send-send-archive-data-s7-400) | 19 |
| [NOTIFY_8P](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#notify_8p-report-up-to-eight-signal-changes-s7-400) | 1A |
| (no instruction exists; I_DB or OFFSET wrong) | FF |

### Parameters RET_VAL, ERROR and STATUS

The output parameter RET_VAL can have the following two values for the "CONTROL" instruction:

- 0000H: No error occurred during execution.
- 8000H: An error occurred during execution.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 1 | 10 | Access to local user memory not possible (e.g.: A memory byte that does not exist in the CPU being used was specified as the actual parameter for I_TYP). |
| 1 | 12 | When the instruction was called:  - An instance DB was specified at the I_DB parameter that does not belong to the "CONTROL" instruction. - A global DB was specified instead of an instance DB. - No instance DB found (Remedy: Load the associated instance DB again). |

> **Note**
>
> The output parameters ERROR and STATUS need to be evaluated even if the output parameter RET_VAL shows the value 0000H .

## PRINT: Send data to printer (S7-400)

This section contains information on the following topics:

- [Description of PRINT (S7-400)](#description-of-print-s7-400)
- [FORMAT parameter (S7-400)](#format-parameter-s7-400)

### Description of PRINT (S7-400)

#### Description

With the "PRINT" instruction, you can send data and a formatting instruction to a remote printer **with S7-400**, for example, using the CP 441.

When there is a rising edge at control input REQ , the format description (FORMAT parameter) and the data (SD_i) are sent to the printer selected with ID and PRN_NR .

If you do not use all four send areas, make sure that the first area is described by the SD_1 parameter, the second area (if it exists) by SD_2, the third area (if it exists) by SD_3.

Successful execution of the job is indicated by the status parameter DONE having the value "1". If any errors occur, they are indicated in the status parameters ERROR and STATUS.

#### Parameters

The following table shows the parameters of the "PRINT" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the data exchange on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job has been executed error-free. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| PRN_NR | InOut | BYTE | I, Q, M, D, L | Printer number |
| [FORMAT](#format-parameter-s7-400) | InOut | STRING | I, Q, M, D, L | Format description |
| SD_i  (1≤ i ≤4) | InOut | ANY | M, D, T, C | Pointer to the "i-nth" send data area.  Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME.   **Note:** If the ANY pointer accesses a DB, the DB must always be specified (for example: P# DB10.DBX5.0 byte 10). |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information for "PRINT" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS(decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote). - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 2 | Negative acknowledgement from printer. The function cannot be executed. |
| 1 | 3 | PRN_NR is unknown on the communication link specified by the ID. |
| 1 | 4 | Data length or data type related error in the FORMAT in/out parameter or in the send area pointers SD_i. |
| 1 | 6 | The remote printer is in OFFLINE mode. |
| 1 | 7 | The remote printer is not in the correct status (for example, paper out). |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called:  - An instance DB was specified that does not belong to "PRINT" - A global DB instead of an instance DB was specified. - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 13 | Error in the [FORMAT](#format-parameter-s7-400) in/out parameter. |
| 1 | 20 | **S7-400**   Not enough work memory. Solution: Reduce the program code in the memory. |

#### Amount of transferable data

The amount of data that can be transferred to a remote printer must not exceed a maximum length. This maximum data length is calculated as follows:

maxleng = 420 - format

In this case `format` is the current length of the FORMAT parameter in bytes. The data to be printed can be distributed over one or more send areas.

### FORMAT parameter (S7-400)

#### Description

The character string FORMAT contains character and format elements that are to be printed. It has the following structure:

![Structure of characters and format elements](images/18816654859_DV_resource.Stream@PNG-en-US.png)

Structure of characters and format elements

Exactly one conversion instruction must exist in FORMAT for each send area SD_1 to SD_4 that is to be printed. The conversion instructions are used on the send areas SD_i according to order specified. Characters and instructions can follow each other in any order.

#### Characters

Permissible:

- All printable characters
- $$ (Dollar character), $' (single inverted comma),$L and $l (line feed), $P and $p (page), $R and $r (carriage return), $T and $t (tabulator)

  ![Syntax diagram of a conversion instruction](images/18817037579_DV_resource.Stream@PNG-en-US.png)

  Syntax diagram of a conversion instruction

| Element of a conversion instruction | Meaning |  |
| --- | --- | --- |
| Flags | - None: - -: | right-justified output  left-justified output |
| Width | - None: - n: | output in standard representation   Exactly n characters are output. If the output is right-justified, this may be preceded by blanks, with left- justified output the blanks come after the characters. |
| Precision | Precision is only relevant for representations A, D, F and R (see following table). |  |
| - None: - 0: - n: | Output is in standard representation no output of the decimal point or of  decimal places for F and R representations  - with F and R: output of the decimal point and n decimal places - with A and D (date): number of digits for the year: Possible values: 2 and 4. |  |
| Representation | The following table contains:  - The possible representations - The data types possible for each representation - for each representation, the standard representation (the printer output is in standard representation if you specify no width and no precision in the FORMAT parameter. |  |

#### Conversion instruction

The following table shows the possible representations in the conversion instruction of the FORMAT parameter.

| Representation | Possible data  types | Example | Length | Comments |
| --- | --- | --- | --- | --- |
| A, a | DATE | 25.07.1996 | 10 | - |
|  | DWORD |  |  |  |
| C, c | CHAR | K | 1 | - |
|  | BYTE | M | 1 |  |
|  | WORD | KL | 2 |  |
|  | DWORD | KLMN | 4 |  |
|  | ARRAY of CHAR | KLMNOP | Number of characters |  |
|  | ARRAY of BYTE |  |  |  |
| D, d | DATE | 1996-07-25 | 10 | - |
|  | DWORD |  |  |  |
| F, f | REAL | 0.345678 | 8 | - |
|  | DWORD |  |  |  |
| H, h | all data types incl. ARRAY of BYTE | Depending on data type | Depending on data type | Hexadecimal representation |
| I, i | INT | - 32 768 | max. 6 | - |
|  | WORD | - 2 147 483 648 | max. 11 |  |
| N, n | WORD | Text output | - | The relevant send area SD_i contains a reference (number) to a text to be printed. The text is on the module (for example, CP 441), which creates a printable string. If no text is found under the specified number, **** will be output. |
| R, r | REAL | 0.12E-04 | 8 | - |
|  | DWORD |  |  |  |
| S, s | STRING | Text output |  | - |
| T, t | TIME | 2d_3h_10m_5s_250ms | max. 21 | If an error occurs, **** will be output. |
|  | DWORD |  |  |  |
| U, u | BYTE | 255 | max. 3 | - |
|  | WORD | 65 535 | max. 5 |  |
|  | DWORD | 4 294 967 295 | max. 10 |  |
| X, x | BOOL | 1 | 1 | - |
|  | BYTE | 101 .. | 8 |  |
|  | WORD | 101 .. | 16 |  |
|  | DWORD | 101 .. | 32 |  |
| Z, z | TIME_OF_DAY (TOD) | 15:38:59.874 | 12 | - |

At the points in this table at which a maximum length is specified for the representation, the actual length can of course be shorter.

> **Note**
>
> With the data types C and S, the following points depend on the printer being used:
>
> - which characters can be printed
> - what the printer prints for non-printable characters, unless the printer driver has a conversion table for these characters.

#### Control instruction

Using the control instruction you can do the following:

- Print the characters % and \
- Change the printer settings.

  ![Syntax diagram of the control instruction](images/18817074699_DV_resource.Stream@PNG-en-US.png)

  Syntax diagram of the control instruction

If you attempt to disable, for example, a font that is not enabled or execute a function that the printer does not recognize, the control instruction is ignored. The following table show the possible errors for the FORMAT in/out parameter.

| Error | Printer output |
| --- | --- |
| Conversion instruction cannot be executed | * characters are output according to the (maximum) length of the default representation or the specified width. |
| Specified width too small | In the representations A, C, D, N, S, T, and Z, as many characters are printed as specified by the selected width. With all other representations, * characters are printed across the specified width. |
| Too many conversion instructions | The conversion instructions to which no send area pointer SD_i belongs are ignored. |
| Too few conversion instructions | Send areas for which there is no conversion instruction are not printed out. |
| Undefined or unsupported conversion instructions | ****** is printed out. |
| Incomplete conversion instruction | ****** is printed out. |
| Undefined or unsupported control instructions | Control instructions that do not comply with the syntax shown in the figure above are ignored. |

## START: Execute a warm restart or cold restart on a remote device (S7-400)

### Description

If there is a positive edge at control input REQ, the "START" instruction activates a warm restart or a cold restart on the remote device addressed by ID **with S7-400**.

You can find additional information on the topic of warm and cold restarts here: [Cold and warm restart](http://support.automation.siemens.com/WW/view/de/34053759)

The following conditions must be met if the remote device is a CPU:

- The CPU must be in STOP mode.
- The mode selector of the CPU must be set to "RUN".

Once the warm or cold restart is complete, the device changes to RUN mode and sends a positive execution acknowledgement. The status parameter DONE is set to "1" with the evaluation of the positive acknowledgement. The status parameters ERROR and STATUS show any errors that have occurred.

Another activation of a warm or cold restart is not possible until the last activation is completed.

### Parameters

The following table shows the parameters of the "START" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the instruction on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job executed without errors. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| PI_NAME | InOut | ANY | I, Q, M, D, T, C | Pointer to memory area in which the name of the program (ASCII code) to be started is located. This name must not contain more than 32 characters.  With a standard system from the S7 family, it must be P_PROGRAM. |
| ARG | InOut | ANY | I, Q, M, D, T, C | Execution argument.   - If you do not assign a value to ARG , a warm restart is run on the remote device. - If you assign the value "C," a cold restart is run on the remote device (if the remote device is capable of this type of startup). |
| IO_STATE | InOut | BYTE | I, Q, M, D, L | Not currently relevant. Do not assign a value to this parameter if your communication partner is an S7 series automation system. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### ERROR and STATUS parameters

The following table contains all specific error information for START that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS(decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote). - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 3 | The program name entered in PI_NAME is unknown. |
| 1 | 4 | Error in the pointers PI_NAME or ARG relating to the data length or the data  type. |
| 1 | 7 | No complete restart possible on the partner device. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "START" - A global DB was specified instead of an instance DB - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 20 | S7-400: Not enough work memory. Solution: Reduce the program code in the memory. |

## STOP: Change a remote device to STOP mode (S7-400)

### Description

If there is a rising edge at control input REQ , the "STOP" instruction activates a change to STOP mode on the remote device addressed by ID**with S7-400**. The mode change is possible when the device is in RUN, HOLD, or startup.

Successful execution of the job is indicated by the status parameter DONE having the value "1". If any errors occur, they are indicated in the status parameters ERROR and STATUS.

The mode change can only be repeated on the same remote device if the previous "STOP" instruction has been completed.

### Parameters

The following table shows the parameters of the "STOP" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the instruction on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job has been executed error-free. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   There is an error. STATUS supplies detailed information on the type of error. |
| PI_NAME | InOut | ANY | I, Q, M, D | Pointer to the memory area in which the name of the program (ASCII code) to be started is located. This name must not contain more than 32 characters.  With a standard system from the S7 family, it must be P_PROGRAM. |
| IO_STATE | InOut | BYTE | I, Q, M, D, L | Not currently relevant. Do not assign a value to this parameter if your communication partner is an S7 series automation system. |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for the "STOP" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote). - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 3 | The program name entered in PI_NAME is unknown. |
| 1 | 4 | Error in the pointer PI_NAME relating to the data length or the data type. |
| 1 | 7 | The partner device is already in the STOP state. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to STOP - A global DB was specified instead of an instance DB - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 20 | S7-400: Not enough work memory. Solution: Reduce the program code in the memory. |

## RESUME: Initiate a hot restart on a remote device (S7-400)

### Description

If there is a rising edge at control input REQ, the "RESUME" instruction activates a hot restart in the remote device addressed by ID**with S7-400**. The following conditions must be present if the remote device is a CPU:

- The CPU must be in STOP mode.
- The mode selector of the CPU must be set to RUN.
- You must have enabled manual hot restart during configuration.
- There must be no condition preventing a hot restart.

Once the hot restart has been completed, the device changes to RUN mode and sends a positive execution acknowledgement. The status parameter DONE is set to "1" with the evaluation of the positive acknowledgement. The status parameters ERROR and STATUS show any errors that have occurred.

Another activation of the hot restart in the same remote device is not possible until the last activation is complete.

### Parameters

The following table shows the parameters of the "RESUME" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the instruction on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job has been executed error-free. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies   detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| PI_NAME | InOut | ANY | I, Q, M, D | Pointer to memory area in which the name of the program (ASCII code) to be started is located. This name must not contain more than 32 characters. With an S7, it must  be P_PROGRAM. |
| ARG | InOut | ANY | I, Q, M, D, T, C | Execution argument. Not currently relevant. Do not assign a value to this parameter if your communication partner is an S7 series automation system. |
| IO_STATE | InOut | BYTE | I, Q, M, D, L | Not currently relevant. Do not assign a value to this parameter if your communication partner is an S7 series automation system. |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for "RESUME" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | - Communications problems, for example, connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 3 | The program name entered in PI_NAME is unknown. |
| 1 | 4 | Error in the pointers PI_NAME or ARG relating to the data length or the data  type. |
| 1 | 7 | Hot restart not possible |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to RESUME. - A global DB was specified instead of an instance DB - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 20 | S7-400: Not enough work memory. Solution: Reduce the program code in the memory. |

## STATUS: Query the status of a remote partner (S7-400)

### Description

With the "STATUS" instruction, you can query the device status of a remote communication partner **with S7-400**.

If there is a rising edge at control input REQ, a job is sent to the remote partner. The reply is evaluated to determine whether problems have occurred. If no errors occurred, the received status is copied to the tags of the PHYS, LOG and LOCAL parameters with the next call. Completion of this action is indicated by the status parameter NDR having the value "1".

You can only query the status of the same communications partner again after the last query is complete.

### Parameters

The following table shows the parameters of the "STATUS" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter request, activates the instruction on a rising edge. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still executing. - 1: Job completed without errors. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   <> 0000H: Warning, STATUS supplies detailed information. - ERROR=1   There is an error. STATUS supplies detailed information on the type of error. |
| PHYS | InOut | ANY | I, Q, M, D | Physical status (minimum length: one byte)  Possible values:  - 10H fully functional. - 13H service required. |
| LOG | InOut | ANY | I, Q, M, D | Logical status (minimum length: one byte)  Possible value:  - 00H status change permitted. |
| LOCAL | InOut | ANY | I, Q, M, D | Status if the partner device is an S7 CPU (minimum length: two bytes) |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### In/out parameter LOCAL

If the communications partner is an S7 CPU, the in/out parameter LOCAL contains its current status: The first byte is reserved, the second byte contains an ID for the status.

| Operating mode | Corresponding identifier |
| --- | --- |
| STOP | 00H |
| STARTUP (warm restart) | 01H |
| RUN | 02H |
| STARTUP (hot restart) | 03H |
| HOLD | 04H |
| STARTUP (cold restart) | 06H |
| RUN | 09H |
| LINK-UP | 0BH |
| UPDATE | 0CH |

### Parameters ERROR and STATUS

The following table contains all specific error information for STATUS that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning:  - New job not active because the previous job is still busy. - The job is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communications problems, for example  - Connection description not loaded (local or remote). - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 2 | Negative acknowledgement from the partner device. The function cannot be executed. |
| 1 | 4 | Error in PHYS, LOG or LOCAL relating to the data length or the data type. |
| 1 | 8 | Access to a remote object was rejected. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to STATUS - A global DB was specified instead of an instance DB - No instance DB found (Solution: Load the associated instance DB again). |
| 1 | 20 | S7-400: Not enough work memory. Solution: Reduce the program code in the memory. |

## USTATUS: Uncoordinated receiving of remote device status (S7-400)

### Description

The "USTATUS" instruction receives the device status change of a remote communication partner **with S7-400**. The partner sends its status unsolicited when a change occurs if you have configured this behavior.

If EN_R 1 is set at the control input during the call and a frame of the partner is pending, the status information is entered in the tags of the PHYS, LOG and LOCAL parameters at the next call. Completion of this action is indicated by the status parameter NDR having the value "1".

The transfer of the operating status messages must be enabled on the connection used by the "USTATUS" instruction.

> **Note**
>
> You can only place one instance of the "USTATUS" instruction per connection.

### Parameters

The following table shows the parameters of the "USTATUS" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L | Control parameter (enabled to receive), signals ready to receive if the input is set. |
| ID | Input | WORD | M, D or constant | Addressing parameter ID  See also: [Common parameters of instructions for S7 communication](#common-parameters-of-instructions-for-s7-communication-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still executing. - 1: Job successfully completed. |
| ERROR  STATUS | Output  Output | BOOL  WORD | I, Q, M, D, L  I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   0000H: Neither warning nor error   0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| PHYS | InOut | ANY | I, Q, M, D | Physical status (minimum length: one byte)  Possible values:  - 10H fully functional. - 13H service required. |
| LOG | InOut | ANY | I, Q, M, D | Logical status (minimum length: one byte)  Possible value:  - 00H status change permitted. |
| LOCAL | InOut | ANY | I, Q, M, D | Status if the partner device is an S7 CPU (minimum length: two bytes) |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### In/out parameter LOCAL

If the communication partner is an S7 CPU, the in/out parameter LOCAL contains its current status: The first byte is reserved, the second byte contains an ID for the status.

| Operating mode | Corresponding identifier |
| --- | --- |
| STOP | 00H |
| STARTUP (warm restart) | 01H |
| RUN | 02H |
| STARTUP (hot restart) | 03H |
| HOLD | 04H |
| STARTUP (cold restart) | 06H |
| RUN | 09H |
| LINK-UP | 0BH |
| UPDATE | 0CH |

### Parameters ERROR and STATUS

The following table contains all specific error information for "USTATUS" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 9 | Overrun warning: an older device status has been overwritten by a more recent device status. |
| 0 | 11 | The received data is already being processed in a priority class with lower priority. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote). - Connection interrupted (for example: cable, CPU off, CP in STOP mode). |
| 1 | 4 | Error in PHYS, LOG or LOCAL relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 12 | When the instruction was called   - An instance DB was specified that does not belong to "USTATUS" - A global DB was specified instead of an instance DB. - No instance DB found (Remedy: Load the associated instance DB again). |
| 1 | 18 | There is already an instance for "USTATUS" for the connection  identified by ID. |
| 1 | 19 | The remote CPU sends data faster than it can be accepted in the user program by the instruction. |
| 1 | 20 | S7-400: Not enough work memory. Remedy: Reduce the program code in the memory. |

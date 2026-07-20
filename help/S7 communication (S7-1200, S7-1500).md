---
title: "S7 communication (S7-1200, S7-1500)"
package: ProgKomS7Com2MenUS
topics: 12
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# S7 communication (S7-1200, S7-1500)

This section contains information on the following topics:

- [Data consistency (S7-1200, S7-1500)](#data-consistency-s7-1200-s7-1500)
- [Useful information about the instructions for S7 communication (S7-1200, S7-1500)](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500)
- [GET: Read data from a remote CPU (S7-1200, S7-1500)](#get-read-data-from-a-remote-cpu-s7-1200-s7-1500)
- [PUT: Write data to a remote CPU (S7-1200, S7-1500)](#put-write-data-to-a-remote-cpu-s7-1200-s7-1500)
- [Other (S7-1200, S7-1500)](#other-s7-1200-s7-1500)

## Data consistency (S7-1200, S7-1500)

### Definition

A data block which cannot be modified by concurrent processes is called consistent data area. A data block which is larger than the consistent data area can thus be falsified as a whole during transmission. This means that a data block which belongs together and which is larger than consistent data area can consist in part of new and of old consistent data at the same time.

### Example

An inconsistency can occur when an instruction for communication is interrupted, for example, by a hardware interrupt OB with higher priority. If the user program in this OB now changes the data that has already been partly processed by the instruction, the transferred data originates:

- In part from the time before the hardware interrupt was processed
- And in part from the time after the hardware interrupt was processed

This means that these data are inconsistent (not coherent).

### Ensuring data consistency

If the communication process can be interrupted by an interrupt OB, you must ensure that the data is transferred consistently. Make sure that only an image of the data and not the data to be transferred is not changed directly by the interrupt OB. Copy the image of the data to the transfer area of the communication instruction prior to the next data transfer.

- If the user program contains a communication instruction that accesses common data, access to this data area can be coordinated, for example, by means of the DONE parameter. The data consistency of the communication areas which are transferred locally with a communication instruction can therefore be ensured in the user program.
- In the case of S7 communication instructions "[PUT](#put-write-data-to-a-remote-cpu-s7-1200-s7-1500)"/"[GET](#get-read-data-from-a-remote-cpu-s7-1200-s7-1500)", the size of the consistent data areas must already be taken into consideration during programming or configuration, because a communication block is not available in the user program of the target device (server) to synchronize communication data to the user program.
- For the S7-300 and C7-300 (exception: CPU 318-2 DP) the communication data are copied consistently into the user memory in blocks of 32 bytes in the cycle control point of the operating system. Data consistency is not guaranteed for larger data areas. If a defined   
  data consistency is required, the communication data in the user program may not exceed 32 bytes (maximum of 8 bytes, depending on the version).
- In the S7-400 and S7-1500, on the other hand, the communication data in 462-byte blocks is not processed at the cycle control point, but in fixed time slices during the program cycle. The consistency of a tag is ensured by the system. These communication areas can then be accessed consistently using the "[PUT](#put-write-data-to-a-remote-cpu-s7-1200-s7-1500)" / "[GET](#get-read-data-from-a-remote-cpu-s7-1200-s7-1500)" instructions or when reading/writing tags, for example by an OP or an OS.

  > **Note**
  >
  > Additional information on data consistency is provided in the description of the specific instructions.

In the S7-1500 module series, you can change parameters during ongoing operation with the instructions of S7 communication. Changed parameters are used immediately, even if a job is still active. Both can lead to data inconsistency! To avoid data inconsistencies, you should never change parameters while a job is running.

### Effect on interrupt reaction times

The interrupt reaction times of the CPU are slightly extended by copying the data. The greater the quantity of data which must be transferred with absolute consistency, the longer the interrupt reaction time of a system.

## Useful information about the instructions for S7 communication (S7-1200, S7-1500)

### Classification

The parameters of the instructions for S7 communication can be divided into the following five categories according to their functions:

1. Control parameters are used to activate an instruction.
2. Addressing parameters are used to address the remote communication partner.
3. Send parameters point to the data areas that are to be sent to the remote partner.
4. Receive parameters point to the data areas where the data received from remote partners will be entered.
5. Status parameters are used to monitor whether the instruction has completed its task without error or for the analysis of any errors that have occurred.

### Functional description

The instructions for S7 communication are asynchronous instructions, which means that their execution can extend over several calls. The CPU processes asynchronous instructions parallel to the cyclic user program up to a CPU-specific maximum number.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Control parameter

Data exchange will only be activated if the appropriate control parameters have a defined value (for example, are set) when the instruction is called or when the value has undergone a specific change since the previous call (for example, a positive edge).

### Addressing parameters

| Parameter | Description |
| --- | --- |
| ID | Reference to the local connection description (specified by the configuration of the connection). |
| R_ID | With the R_ID parameter, you specify that a send and a receive instruction belong together: The R_ID parameter must match in the instruction at the sending end and the instruction at the receiving end.  This allows the communication of several instruction pairs via the same logic connection.  - R_ID must be specified in the form DW#16#wxyzWXYZ. - The instruction pairs of a logical connection specified in R_ID must be unique for this connection. |

You determine with which partner data is exchanged using the addressing parameter "ID". This references the connection via which the data is sent or received.

- You can call multiple S7 communication instructions (e.g. two PUT instructions) with the same ID. In this case, the instructions are processed sequentially, which means that the data is transferred successively over the same connection.
- You can set up and use multiple connections to the same partner. S7 communication instructions with different IDs are processed in parallel over several connections.

> **Note**
>
> **Addressing parameters ID and R_ID**
>
> You can reassign the addressing parameters ID and R_ID during runtime. The new parameters are validated with each new job after the previous job has been closed.
>
> You can use the following options to reduce the number of instance DBs and therefore the work memory required:
>
> 1. With tag IDs, you can use several connections via one data instance block.
> 2. With tag R_IDs, you can define several pairs of sending and receiving instructions for one job with a single instance.
> 3. You can combine cases 1 and 2.
>
> Please note that the new parameters are valid after the last job is executed. When you activate the sending operation, the R_ID parameter in the instruction at the sending end must match its counterpart at the receiving end.

### Status parameter

With the status parameters, you monitor whether the instruction has completed its task correctly or whether it is still active. The status parameters also indicate errors.

> **Note**
>
> The status parameters are valid for one cycle only, namely from the first command following the call until the next call. As a result, you must evaluate these parameters after each instruction cycle.

### Send and receive parameters

For communication instructions configured at both ends

- The number of the SD_i and RD_i parameters used must match at the send and receive end.
- The data types of the SD_i and RD_i parameters that belong together must match at the send and receive end.
- The amount of data to be sent according to the SD_i parameter must not exceed the range made available by the corresponding RD_i (does not apply to "[BSEND](#bsend-send-data-in-segments-s7-1500)" / "[BRCV](#brcv-receive-data-in-segments-s7-1500)"). The RD_i parameters must (with exception of "BSEND"/"BRCV") have the identical data size.

If you do not keep to the rules above, this is indicated by ERROR = 1 and STATUS = 4.

> **Note**
>
> **Supplying the send and receive parameters**
>
> With the VARIANT data type, send and receive parameters must always be supplied any time a communication instruction is called. It is not possible, for example, to supply the send parameters of the communication instructions at startup and to only trigger the send job in cyclic operation.

### User data size

With the "[USEND](#usend-send-data-uncoordinated-s7-1500)", "[URCV](#urcv-receive-data-uncoordinated-s7-1500)", "[GET](#get-read-data-from-a-remote-cpu-s7-1200-s7-1500)" and "[PUT](#put-write-data-to-a-remote-cpu-s7-1200-s7-1500)" instructions, the amount of data to be transferred must not exceed a defined user data size. The maximum user data size depends on:

- The instruction used
- The communication partner.

The guaranteed minimum size of the user data for an instruction with 1-4 tags is listed in the following table:

| Instruction | Partner: S7-300 | Partner: S7-400 | Partner: S7-1200 | Partner: S7-1500 |
| --- | --- | --- | --- | --- |
| PUT / GET | 160 bytes | 400 bytes | 160 bytes | 880 bytes |
| USEND / URCV | 160 bytes | 440 bytes | - | 920 bytes |
| BSEND / BRCV | 32768/65534 bytes | 65534 bytes | - | - 65534 bytes with standard access - 65535 bytes with optimized access |

Further information on the user data size can be found in the technical data of the respective CPU.

### Exact user data size

If the user data size specified above is insufficient you can determine the maximum byte length of the user data as follows:

First read the data block size valid for communication from the following table:

| Local CPU | Remote CPU | Data block size in bytes |
| --- | --- | --- |
| S7-1200 | Any | 240 |
| S7-1500 | S7-300 | 240 |
| S7-400 | 480 |  |
| S7-1200 | 240 |  |
| S7-1500 | 960 |  |

Use this value in the following table to read the maximum possible user data length in bytes as total of the parameters used. It applies for even lengths of the areas SD_i, RD_i, and ADDR_i.

For each range of uneven length the maximum possible user data length is reduced by one byte.

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
| 480 (S7-400) | PUT | 452 | 436 | 420 | 404 |
| GET | 462 | 458 | 454 | 450 |  |
| USEND | 452 | 448 | 444 | 440 |  |
| 240 (S7-1200) | PUT | 212 | 196 | 180 | 164 |
| GET | 222 | 218 | 214 | 210 |  |
| 960 (S7-1500) | PUT | 932 | 916 | 900 | 884 |
| GET | 942 | 938 | 934 | 930 |  |
| USEND | 932 | 928 | 924 | 920 |  |

## GET: Read data from a remote CPU (S7-1200, S7-1500)

### Description

With the instruction "GET", you can read data from a remote CPU.

The instruction is started on a positive edge at control input REQ:

- The relevant pointers to the areas to be read out (ADDR_i) are then sent to the partner CPU. The partner CPU can be in RUN or STOP mode.
- The partner CPU returns the data:

  - If the reply exceeds the maximum user data length, this is displayed with error code "2" at the STATUS parameter.
  - The received data is copied to the configured receive areas (RD_i) at the next call.

- Completion of this action is indicated by the status parameter NDR having the value "1".

Reading can only be activated again after the previous reading process has been completed. Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being read or if the data type check results in an error.

Changes in the data areas addressed on the partner CPU are not registered by the "GET" instruction.

### Requirements for using the instruction

- The "Permit access with PUT/GET communication from remote partner" function was activated in the properties of the partner CPU under "Protection".
- The blocks which you access with the "GET" instruction were created with the access type "standard".
- Make sure that the areas defined with the parameters ADDR_i and SD_i match in terms of number, length and data type.
- The area to be read (ADDR_i parameter) cannot be larger than the area for data storage (RD_i parameter).

### Parameters

The following table shows the parameters of the "GET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter request, activates the data exchange on a positive edge. |
| ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameters for specifying the connection to the partner CPU. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:   - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   - 0000H: Neither warning nor error   - &lt;&gt; 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred. STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| ADDR_1 | InOut | REMOTE | I, Q, M, D | Pointers to the areas on the partner CPU that are to be read.  When the REMOTE pointer accesses a DB, the DB must always be specified.   Example: P#DB10.DBX5.0 Byte 10. |
| ADDR_2 | InOut | REMOTE |  |  |
| ADDR_3 | InOut | REMOTE |  |  |
| ADDR_4 | InOut | REMOTE |  |  |
| RD_1 | InOut | VARIANT | I, Q, M, D, L | Pointers to the areas on the local CPU in which the read data is entered. |
| RD_2 | InOut | VARIANT |  |  |
| RD_3 | InOut | VARIANT |  |  |
| RD_4 | InOut | VARIANT |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

The following table contains all specific error information for the "GET" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: New job not active because the previous job is still busy. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established |
| 1 | 2 | - Negative acknowledgment from the partner device. The function cannot be executed. - Response from the remote station exceeds the maximum user data length (see: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500)). - Access protection is activated on the partner CPU. Deactivate access protection in the CPU settings. |
| 1 | 4 | Error in the pointers to the data storage RD_i:  - Data types of the parameters RD_i and ADDR_i are not compatible with each other. - The length of the area RD_i is smaller than the length of the data of the ADDR_i parameter that is to be read. |
| 1 | 8 | Access error on the partner CPU. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

> **Note**
>
> **Data consistency**
>
> Data is received consistently if you read the part of the receive area RD_i currently being used completely before initiating another job.

### Example

In the following example use an S7 connection and in CPU 1 read out a data record of CPU 2. The data record to be sent is of the data type INT.

**Requirement**

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. The connection is not yet configured.
- A low protection level under “&lt;CPU&gt; &gt; Properties &gt; Protection“ ensures that read and write access is permitted for the CPUs.
- Access with the PUT/GET instruction is permitted.

  ![Example](images/81320890123_DV_resource.Stream@PNG-de-DE.png)

**Program of CPU 1**

Create six tags in a global data block for storing the data of “GET“.

![Example](images/81320975755_DV_resource.Stream@PNG-de-DE.png)

Create one tag in a global data block for storing the data record to be received.

![Example](images/81321006219_DV_resource.Stream@PNG-de-DE.png)

Network 1: Interconnect the parameters of the "GET" instruction as follows.

![Example](images/81321143051_DV_resource.Stream@PNG-de-DE.png)

Network 2: Save the status for an error of GET as follows.

![Example](images/81321151883_DV_resource.Stream@PNG-de-DE.png)

Network 3: Save the success status of GET as follows.

![Example](images/81321199115_DV_resource.Stream@PNG-de-DE.png)

**Configuration of GET**

To interconnect the input parameter ID, open the wizard of the "GET" instruction with “Properties &gt; Configuration“.

Make the following settings for the connection:

| Section | Setting |
| --- | --- |
| End point | Select the communication partner.   The remaining connection data will be entered automatically. An S7 connection is created automatically and its identifier entered at the input parameter ID. |
| Active | Make sure that the active connection goes out from CPU 1. |

**Program of CPU 2**

Create one tag in a global data block for storing the data record to be sent.

![Example](images/81320984587_DV_resource.Stream@PNG-de-DE.png)

In “Properties &gt; Attributes“ of the data block disable the optimized block access.

![Example](images/81324071819_DV_resource.Stream@PNG-de-DE.png)

**Behavior of GET**

When the input parameter REQ ("start") supplies the signal state "TRUE", the "GET" instruction is started. The instruction calls up the connection data and makes contact with the communications partner of the S7 connection being used. To achieve this, the identifier of the S7 connection is stored at the input parameter ID.

Via the parameter ADDR_1 the storage location of the data record of CPU 2 to be sent (“myValue“) is identified. The data record (“myValue“) is read out and at the parameter RD_1 the identified storage location (“readValue“) is entered.

![Example](images/81321280779_DV_resource.Stream@PNG-de-DE.png)

Successful processing is indicated by the output parameter NDR ("done") with the signal state "TRUE" and the output parameter STATUS ("status") with the value "16#0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "memDoneStat". The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing took place without errors.

![Example](images/81321271947_DV_resource.Stream@PNG-de-DE.png)

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

## PUT: Write data to a remote CPU (S7-1200, S7-1500)

### Description

You can write data to a remote CPU with the instruction "PUT".

The instruction is started on a positive edge at control input REQ:

- The pointers to the areas to be written (ADDR_i) and the data (SD_i) are then sent to the partner CPU. The partner CPU can be in RUN or STOP mode.
- The data to be sent is copied from the configured send areas ((SD_i). The partner CPU saves the sent data under the addresses supplied with the data and returns an execution acknowledgment.
- If no errors occur, this is indicated at the next instruction call with status parameter DONE = "1". The writing process can only be activated again after the last job is complete.

Errors and warnings are output via ERROR and STATUS if access problems occurred while the data was being written or if the execution check results in an error.

### Requirements for using the instruction

- The "Permit access with PUT/GET communication from remote partner" function was activated in the properties of the partner CPU under "Protection".
- The blocks which you access with the "PUT" instruction were created with the access type "standard".
- Make sure that the areas defined with the parameters ADDR_i and SD_i match in terms of number, length and data type.
- The area to be written (ADDR_i parameter) must be as large as the send area (SD_i parameter).

### Parameters

The following table shows the parameters of the "PUT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter request, activates the data exchange on a positive edge. |
| ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameters for specifying the connection to the partner CPU. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing - 1: Job executed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameters ERROR and STATUS, error code:  - ERROR=0   STATUS has the value:   - 0000H: Neither warning nor error   - &lt;&gt; 0000H: Warning, STATUS supplies detailed information. - ERROR=1   An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L |  |
| ADDR_1 | InOut | REMOTE | I, Q, M, D | Pointers to the areas on the partner CPU to which the data will be written.  When the REMOTE pointer accesses a DB, the DB must always be specified.   Example: P#DB10.DBX5.0 Byte 10.  When transferring data structures (e.g., Struct, Array) the following data type must be used at the ADDR_i parameters.  - For S7-1200 CPUs of all firmware versions and for S7-1500 CPUs as of firmware version V2.8.2: BYTE, CHAR, WORD, INT, DWORD, DINT or REAL - For S7-1500-CPUs with firmware version &lt; V2.8.2: CHAR   Note: As of firmware version V2.8.2, you can therefore transfer programs that contain the "PUT" instruction from S7-300, S7-400 and S7-1200 CPUs to S7-1500 CPUs. |
| ADDR_2 | InOut | REMOTE |  |  |
| ADDR_3 | InOut | REMOTE |  |  |
| ADDR_4 | InOut | REMOTE |  |  |
| SD_1 | InOut | VARIANT | I, Q, M, D, L | Pointers to the areas on the local CPU which contain the data to be sent.  Only the BOOL data types are permitted (not permitted: Bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL.  The following applies to S7-1500 CPUs with firmware version &lt; V2.8.2: When transferring data structures (e.g., Struct, Array) the data type CHAR must be used at the SD_i parameters.  Note: As of firmware version V2.8.2, you can therefore transfer programs that contain the "PUT" instruction from S7-300, S7-400 and S7-1200 CPUs to S7-1500 CPUs. |
| SD_2 | InOut | VARIANT |  |  |
| SD_3 | InOut | VARIANT |  |  |
| SD_4 | InOut | VARIANT |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### ERROR and STATUS parameters

The following table contains all specific error information for the "PUT" instruction that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: New job not active because the previous job is still busy. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problems, for example  - Connection description not loaded (local or remote). - Link down (for example, cable, CPU off, CP in STOP mode). - Connection to partner not yet established. |
| 1 | 2 | - Negative acknowledgment of partner CPU. The function cannot be executed. - Access on the partner CPU was not granted. Activate the access in the CPU settings. |
| 1 | 4 | Error in the pointers to the data storage:  - Data types of the parameters SD_i and ADDR_i are not compatible with each other. - The length of the area SD_i is greater than the length of the data of the ADDR_i parameter that is to be written. - Not possible to access SD_i. - Maximum user data size exceeded. - Number of the parameters SD_i and ADDR_i does not match. |
| 1 | 8 | Access error with the partner CPU (e.g. DB not loaded or write-protected). |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

### Data consistency

When a send operation is activated (positive edge at REQ), the data to be sent from the send area SD_i is copied from the user program. After the block call, you can write to these areas without corrupting the current send data.

> **Note**
>
> The send operation is only complete when the DONE status parameter has the value "1".

### Example

In the following example use an S7 connection and transfer a data record from CPU 1 to CPU 2. The data record to be sent is of the data type INT.

**Requirement**

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. The connection is not yet configured.
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.
- Access with the PUT/GET instruction is permitted.

  ![Example](images/81320890123_DV_resource.Stream@PNG-de-DE.png)

**Program of CPU 1**

Create six tags in a global data block for storing the data of "PUT".

![Example](images/81325843467_DV_resource.Stream@PNG-de-DE.png)

Create one tag in a global data block for storing the data record to be sent.

![Example](images/81325954699_DV_resource.Stream@PNG-de-DE.png)

Network 1: Interconnect the parameters of the "PUT" instruction as follows.

![Example](images/81326087563_DV_resource.Stream@PNG-de-DE.png)

Network 2: Save the status for an error of PUT as follows.

![Example](images/81326147595_DV_resource.Stream@PNG-de-DE.png)

Network 3: Save the success status of PUT as follows.

![Example](images/81326156427_DV_resource.Stream@PNG-de-DE.png)

**Configuration of PUT**

To interconnect the input parameter ID, open the wizard of the "PUT" instruction with "Properties &gt; Configuration".

Make the following settings for the connection:

| Section | Setting |
| --- | --- |
| End point | Select the communication partner.   The remaining connection data will be entered automatically. An S7 connection is created automatically and its identifier entered at the input parameter ID. |
| Active | Make sure that the active connection goes out from CPU 1. |

**Program of CPU 2**

Create one tag in a global data block for storing the data record to be received.

![Example](images/81325963531_DV_resource.Stream@PNG-de-DE.png)

In "Properties &gt; Attributes" of the data block disable the optimized block access.

![Example](images/81324071819_DV_resource.Stream@PNG-de-DE.png)

**Behavior of PUT**

When the input parameter REQ ("start") returns the signal state "TRUE", the "PUT" instruction is started. The instruction calls up the connection data and makes contact with the communications partner of the S7 connection being used. To achieve this, the identifier of the S7 connection is stored at the input parameter ID.

At the parameter SD_1 the storage location of the data record of CPU 1 to be sent ("writeValue") is identified. At the parameter ADDR_1 the storage location ("myValue") of the data record in CPU 2 is identified. The data record ("writeValue") is transferred and indicated at the storage location of CPU 2 ("myValue").

![Example](images/81326178059_DV_resource.Stream@PNG-de-DE.png)

Successful processing is indicated by the output parameter DONE ("done") with the signal state "TRUE" and the output parameter STATUS ("status") with the value "16#0000". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "memDoneStat". The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing took place without errors.

![Example](images/81326238091_DV_resource.Stream@PNG-de-DE.png)

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)
  
[Padding bytes when using structured data types](Programming%20basics.md#padding-bytes-when-using-structured-data-types)

## Other (S7-1200, S7-1500)

This section contains information on the following topics:

- [USEND: Send data uncoordinated (S7-1500)](#usend-send-data-uncoordinated-s7-1500)
- [URCV: Receive data uncoordinated (S7-1500)](#urcv-receive-data-uncoordinated-s7-1500)
- [Program example for USEND &amp; URCV (S7-1200, S7-1500)](#program-example-for-usend-urcv-s7-1200-s7-1500)
- [BSEND: Send data in segments (S7-1500)](#bsend-send-data-in-segments-s7-1500)
- [BRCV: Receive data in segments (S7-1500)](#brcv-receive-data-in-segments-s7-1500)
- [Program example for BSEND &amp; BRCV (S7-1200, S7-1500)](#program-example-for-bsend-brcv-s7-1200-s7-1500)

### USEND: Send data uncoordinated (S7-1500)

#### Description

The "USEND" instruction sends data to a remote partner instruction of type "[URCV](#urcv-receive-data-uncoordinated-s7-1500)". The sending process is carried out without coordination with the partner instruction. This means that the data transfer is carried out without acknowledgment by the partner instruction.

When a send operation is activated (positive edge at REQ), the data to be sent from the send areas SD_i are copied from the user program. After the instruction call, you can write to these send areas again without corrupting the current send data.

Successful completion of the send operation is indicated by the value of the DONE status parameter being set to "1".

#### Parameters

The following table shows the parameters of the instruction "USEND":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter request, activates the data exchange on a positive edge. |
| ID | Input | CONN_PRG | I, Q, M, D, L, P or constant | Addressing parameters for specifying the connection to the partner CPU. |
| R_ID | Input | CONN_R_ID | I, Q, M, D, L or constant | Addressing parameter R_ID for defining the instruction pairs "USEND" and "URCV".  See also: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Job not yet started or still executing. - 1: Job executed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Neither warning nor error. - 1: An error has occurred. STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter  See "ERROR and STATUS parameters" table. |
| SD_i (1≤ i ≤4) | InOut | VARIANT | I, Q, M, D, L | Pointer on the i-th send area. Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL or STRUCT.  The maximum user data size for SD_i parameters depends on the partner CPU ("URCV" instruction) and on the number of parameters used.   Additional information is available in: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: New job not active because the previous job is still busy. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problem has occurred. Possible causes:  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established |
| 1 | 4 | - Errors in the send area pointers SD_i relating to the data length or the data type. - Maximum user data length was exceeded. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 18 | Value at R_ID parameter already exists in the connection specified at the ID parameter (R_ID value must be unique for the connection). |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with lower priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

#### Example

You can find the example here: [Program example for USEND &amp; URCV](#program-example-for-usend-urcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### URCV: Receive data uncoordinated (S7-1500)

#### Description

The "URCV" instruction receives data asynchronously from a remote partner instruction of type "[USEND](#usend-send-data-uncoordinated-s7-1500)" and copies this data into the configured receive areas.

The instruction is ready to receive if there is a logical 1 at the EN_R input. An active job can be canceled with EN_R=0.

The receive data areas are referenced by the parameters RD_1 to RD_4. Make sure that the areas defined by the parameters RD_i / RD_1 and SD_i / SD_1 (with the associated partner instruction "[USEND](#usend-send-data-uncoordinated-s7-1500)") match in terms of number and length.

Successful completion of the copy operation is indicated when the value of the NDR status parameter is set to logical "1". Once the status parameter NDR has changed to "1", there will be new receive data in your receive areas (RD_i). A new block call may cause these data to be overwritten with new receive data. If you want to prevent this, call "URCV" (for example, during cyclic block processing) with the value 0 at EN_R until you have finished processing the received data.

#### Parameters

The following table shows the parameters of the instruction "URCV":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Control parameter enabled to receive, signals ready to receive if the input is set. |
| ID | Input | CONN_PRG | I, Q, M, D, L, P or constant | Addressing parameters for specifying the connection to the partner CPU. |
| R_ID | Input | CONN_R_ID | I, Q, M, D, L or constant | Addressing parameter for defining the instruction pairs "USEND" and "URCV". See also: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Neither warning nor error - 1: An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter See "ERROR and STATUS parameters" table. |
| RD_i (1≤ i ≤4) | InOut | VARIANT | I, Q, M, D, L | Pointer to the i-th receive area: Only the BOOL data types are permitted (not permitted: bit array), BYTE, CHAR, WORD, INT, DWORD, DINT, REAL or STRUCT.  Additional information is available in: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

| ERROR | STATUS   (decimal) | Explanation |
| --- | --- | --- |
| 0 | 9 | Warning: older received data were overwritten by newer received data. |
| 0 | 11 | Warning: The received data is already being processed in a priority class with lower priority (error can occur when copying data to the receive area). |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problem has occurred. Possible causes:  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established |
| 1 | 4 | Errors in the receive area pointers RD_i relating to the data length or the data type. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 18 | Value at R_ID parameter already exists in the connection specified at the ID parameter (R_ID value must be unique for the connection). |
| 1 | 19 | The associated "[USEND](#usend-send-data-uncoordinated-s7-1500)" instruction sends data faster than it can be copied to the receive areas by "URCV". |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with lower priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

#### Example

You can find the example here: [Program example for USEND &amp; URCV](#program-example-for-usend-urcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Program example for USEND & URCV (S7-1200, S7-1500)

#### Introduction

In the following example you create an S7 connection between two CPUs of the S7-1500 series. You send a character string (data type STRING) from the CPU 1 to the CPU 2. The data transfer is carried out without acknowledgement by the communication partner.

#### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. An S7 connection is configured.

  ![Requirement](images/94472702091_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.

#### Program of CPU 1

Create the following tags for storing the data of USEND in a global data block.

![Program of CPU 1](images/94472445195_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_USEND". Create the following local tags in it.

![Program of CPU 1](images/94472693259_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "USEND" as follows:

![Program of CPU 1](images/94472809355_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of USEND, save the status as follows.

![Program of CPU 1](images/94472818187_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 2

Create the following tags for storing the data of URCV in a global data block.

![Program of CPU 2](images/94459601035_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_URCV". Create the following local tags in it.

![Program of CPU 2](images/94472316299_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "URCV" as follows:

![Program of CPU 2](images/94472363531_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of URCV, save the status as follows.

![Program of CPU 2](images/94472436363_DV_resource.Stream@PNG-de-DE.png)

#### Assigning communication connection

The addressing parameters for connecting the two CPUs and for defining the instruction pair must be uniform.

- In each case store the hexadecimal value of the hardware ID of the configured S7 connection at the input parameter ID ("connectionID").

  You can find the hardware identifier in the "Network view" under "Connections".

  ![Assigning communication connection](images/94472723723_DV_resource.Stream@PNG-de-DE.png)
- In each case store a self-selected identifier (as hex value, in byte size) for the instruction pair at the input parameter R_ID ("instructionPair"). The identifier must not be already assigned for another instruction pair.

#### Behavior of CPU 1

When the input parameter REQ ("start") supplies the signal state "TRUE", the "USEND" instruction is started. The "USEND" instruction hereby copies the data record detected at input parameter SD_1 ("sendData") to the work memory of the CPU. Successful copying of the data record is indicated by the output parameter DONE ("#done") with the signal state "TRUE". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "done".

Corresponding to the input parameter ID ("connectionID") and R_ID ("instructionPair"), the instruction "URCV" of the CPU 2 as receiver of the data record ("sendData" is addressed with the value "HelloData"). Data transfer via S7 connection continues without further participation by USEND ("start" may be set to "FALSE").

The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing of USEND in the example is taking place without errors.

![Behavior of CPU 1](images/94472646027_DV_resource.Stream@PNG-de-DE.png)

#### Behavior of CPU 2

CPU 2 receives a data record of CPU 1 via the S7 connection. Corresponding to the input parameter ID ("connectionID") and R_ID ("instructionPair"), the instruction "URCV" knows the receiver of the data record.

When the input parameter EN_R ("start") supplies the signal state "TRUE", the "URCV" instruction is started and is ready to receive. The "URCV" instruction reads out the transferred data record and copies the data record into the value area at the RD_1 ("rcvData") input parameter.

Successful copying of the data record is indicated by the output parameter NDR ("#done") with the signal state "TRUE". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "done".

The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing of URCV in the example is taking place without errors.

![Behavior of CPU 2](images/94459609867_DV_resource.Stream@PNG-de-DE.png)

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[USEND: Send data uncoordinated (S7-1500)](#usend-send-data-uncoordinated-s7-1500)
  
[URCV: Receive data uncoordinated (S7-1500)](#urcv-receive-data-uncoordinated-s7-1500)

### BSEND: Send data in segments (S7-1500)

#### Description

The "BSEND" instruction sends data to a remote partner instruction of type "[BRCV](#brcv-receive-data-in-segments-s7-1500)". With this type of data transfer, more data can be transported between the communication partners than is possible with all other communication instructions for configured S7 connections. In each case, the maximum data volume amounts to 65534 bytes (standard access) or 65535 bytes (optimized access) for the integrated interface and for SIMATIC Net CP.

#### Functional description

You specify the instruction pair "BSEND" and "BRCV" with the input parameter R_ID. The R_ID parameter must be identical in the related instructions.

The send job is activated after the instruction is called and a positive edge is detected at control input REQ. After the call, "BSEND" is not processed in the background, which means the data can only be read within the user program.

The data area to be transmitted is segmented. Each segment is sent individually to the partner. Each segment is acknowledged by the partner after the application of this segment by "[BRCV](#brcv-receive-data-in-segments-s7-1500)". If the data is segmented, "BSEND" must be called multiple times until all segments have been transferred.

The data area of the data to be sent is specified by SD_1. To ensure data consistency, you may only write to the part of the currently used sending area SD_1 after the current send operation is complete. This is the case when the value of the status parameter DONE changes to "1".

The length of the send data is specified by LEN based on the job. With LEN = "0", all data addressed with the SD_1 parameter is sent.

If there is a positive edge at control input R, the current sending process is canceled.

Due to the asynchronous data transfer, a new data transfer can only be initiated if the previous data has been fetched by a partner instruction call. When the data has been collected, the status parameter "NDR" is set in the partner instruction "BRCV".

> **Note**
>
> **Migration of S7-400 user programs**
>
> An S7-400 CPU interprets the parameter SD_1 as pointer and not as data area.
>
> With S7-1500, LEN may not exceed the area of SD1. This was permitted with S7-400. Recommendation: Use the maximum size for the LEN parameter (65534 bytes for the integrated interface) as size of the data area at the SD_1 parameter.

#### Parameters

The following table shows the parameters of the instruction "BSEND":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter request, activates the data exchange at a positive edge |
| R | Input | BOOL | I, Q, M, D, L or constant | Control parameter reset, activates an abort of the current data exchange at a positive edge |
| ID | Input | CONN_PRG | I, Q, M, D, L, P or constant | Addressing parameters for specifying the connection to the partner CPU. |
| R_ID | Input | CONN_R_ID | I, Q, M, D, L or constant | Addressing parameter for defining the instruction pairs "BSEND" and "[BRCV](#brcv-receive-data-in-segments-s7-1500)". See also: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |
| SD_1 | InOut | VARIANT | I, Q, M, D, L | Pointer to send area  When transferring structures, the structures must be identical at the sending and receiving end. |
| LEN | InOut | WORD | I, Q, M, D, L | Length of the block of data to be sent in bytes.  With LEN = "0", all data is sent by SD_1. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Job not yet started or still executing. - 1: Job executed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Neither warning nor error. - 1: An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter  See "ERROR and STATUS parameters" table. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information for "BSEND" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 11 | Warning: New job not active because the previous job is still busy. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problem has occurred. Possible causes:  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established |
| 1 | 2 | Negative acknowledgment of partner instruction. The instruction cannot be executed. |
| 1 | 3 | R_ID is unknown on the connection specified by the ID or the receive block  has not yet been called. |
| 1 | 4 | - Error in the data length or data type in the send area pointer SD_1. - Value for LEN is greater than area SD_1. |
| 1 | 5 | Reset request was executed. |
| 1 | 6 | Partner instruction is in DISABLED status (EN_R has the value "0"). Also check the input parameters of "[BRCV](#brcv-receive-data-in-segments-s7-1500)" for consistency with "BSEND". |
| 1 | 7 | "[BRCV](#brcv-receive-data-in-segments-s7-1500)" partner instruction not called since the last data transfer. |
| 1 | 8 | Access to remote object in the user memory was rejected: The target range for the associated "[BRCV](#brcv-receive-data-in-segments-s7-1500)" is too small.  ERROR = 1, STATUS = 4 or ERROR = 1, STATUS = 10 reported at the output parameters of "[BRCV](#brcv-receive-data-in-segments-s7-1500)". |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 18 | R_ID already exists in the connection. |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with lower priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

#### Example

You can find the example here: [Program example for BSEND &amp; BRCV](#program-example-for-bsend-brcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### BRCV: Receive data in segments (S7-1500)

#### Description

The "BRCV" instruction receives data from a remote partner instruction of type "[BSEND](#bsend-send-data-in-segments-s7-1500)". The R_ID parameter must be identical in the related instructions.

The instruction is ready to receive data (STATUS = 25) after it is called with the value "1" at control input EN_R. An active job can be canceled with EN_R=0.

The maximum receive area is specified by RD_1. Data will be received consistently if you fully evaluate the part of the RD_1 receive area currently in use before calling the block again with value 1 at control input EN_R.

After each received data segment, an acknowledgment is sent to the partner instruction. If there are multiple segments it will be necessary to call "BRCV" several times until all of the segments have been received. Asynchronous data receipt is indicated by STATUS = 17. The amount of data currently received is indicated at the parameter LEN. The RD_1 parameter must remain constant during the operation.

Value "1" at the NDR status parameter indicates that all data segments have been received without error. The received data remains unchanged until the next call with EN_R=1.

#### Parameters

The following table shows the parameters of the instruction "BRCV":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Control parameter enabled to receive, signals ready to receive if the input is set. |
| ID | Input | CONN_PRG | I, Q, M, D, L, P or constant | Addressing parameters for specifying the connection to the partner CPU. |
| R_ID | Input | CONN_R_ID | I, Q, M, D, L or constant | Addressing parameter for defining the instruction pairs "[BSEND](#bsend-send-data-in-segments-s7-1500)" and "BRCV". See also: [Useful information about the instructions for S7 communication](#useful-information-about-the-instructions-for-s7-communication-s7-1200-s7-1500) |
| RD_1 | InOut | VARIANT | I, Q, M, D, L | Pointer to the receive area.  When transferring structures, the structures must be identical at the sending and receiving end. |
| LEN | InOut | WORD | I, Q, M, D, L | Length of the data already received in bytes. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Job not yet started or still running. - 1: Job successfully completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter  - 0: Neither warning nor error - 1: An error has occurred, STATUS supplies detailed information on the type of error. |
| STATUS | Output | WORD | I, Q, M, D, L | Status parameter See "ERROR and STATUS parameters" table. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

The following table contains all specific error information for "BRCV" that can be output via the ERROR and STATUS parameters.

| ERROR | STATUS (decimal) | Explanation |
| --- | --- | --- |
| 0 | 17 | Warning: Instruction receives data asynchronously. The LEN parameter shows the amount of data already received in bytes. |
| 0 | 25 | Communication has started. The job is being processed. |
| 1 | 1 | Communication problem has occurred. Possible causes:  - Connection description not loaded (local or remote) - Connection interrupted (for example: cable, CPU off, CP in STOP mode) - Connection to partner not yet established |
| 1 | 2 | Function cannot be executed (protocol error) |
| 1 | 4 | Error in the receive area pointer RD_1 relating to the data length or data type. The block of data sent is longer than the receive area. |
| 1 | 5 | Reset request received, incomplete transfer. |
| 1 | 8 | Access error in associated "[BSEND](#bsend-send-data-in-segments-s7-1500)": After the last valid data segment has been sent, ERROR  = 1 and STATUS  = 4 or ERROR = 1 and STATUS = 10 is reported. |
| 1 | 10 | Access to the local user memory not possible (for example, access to a deleted DB). |
| 1 | 18 | Value at R_ID parameter already exists in the connection specified at the ID parameter (R_ID value must be unique for the connection). |
| 1 | 20 | - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with lower priority (first call). |
| 1 | W#16#80C3 | (only with S7-1500)  - Maximum number of parallel jobs exceeded. - The job is currently being processed in a priority class with low priority (first call). |

#### Example

You can find the example here: [Program example for BSEND &amp; BRCV](#program-example-for-bsend-brcv-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](Asynchronous%20instructions%20%28S7-1200%2C%20S7-1500%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

### Program example for BSEND & BRCV (S7-1200, S7-1500)

#### Introduction

In the following example you create an S7 connection between two CPUs of the S7-1500 series. You send a data record from CPU 1 to CPU 2 using BSEND and BRCV. The data transfer is carried out with acknowledgement by BRCV.

#### Requirement

- Two CPUs of the S7-1500 series are available and connected to each other over PROFINET. An S7 connection is configured.

  ![Requirement](images/94472878219_DV_resource.Stream@PNG-de-DE.png)
- A low protection level under "&lt;CPU&gt; &gt; Properties &gt; Protection" ensures that read and write access is permitted for the CPUs.

#### Program of CPU 1

Create the following tags for storing the data of BSEND in a global data block.

![Program of CPU 1](images/94473392907_DV_resource.Stream@PNG-de-DE.png)

For the data record, create the following PLC data type.

![Program of CPU 1](images/94473739403_DV_resource.Stream@PNG-de-DE.png)

For the data transfer, create the following data block based on the created PLC data type ("BSEND_User").

![Program of CPU 1](images/94474029835_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_BSEND". Create the following local tags in it.

![Program of CPU 1](images/94473730571_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "BSEND" as follows:

![Program of CPU 1](images/94474166667_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of BSEND, save the status as follows.

![Program of CPU 1](images/94474175499_DV_resource.Stream@PNG-de-DE.png)

#### Program of CPU 2

Create the following tags for storing the data of BRCV in a global data block.

![Program of CPU 2](images/94473011083_DV_resource.Stream@PNG-de-DE.png)

For the data record, create the following PLC data type.

![Program of CPU 2](images/94473739403_DV_resource.Stream@PNG-de-DE.png)

For the data transfer, create the following data block based on the created PLC data type ("BSEND_User").

![Program of CPU 2](images/94473306379_DV_resource.Stream@PNG-de-DE.png)

Create an FB "SLI_FB_BSEND". Create the following local tags in it.

![Program of CPU 2](images/94473271947_DV_resource.Stream@PNG-de-DE.png)

**Network 1**: Interconnect the parameter of the instruction "BRCV" as follows:

![Program of CPU 2](images/94473324043_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: In case of error of BRCV, save the status as follows.

![Program of CPU 2](images/94473384075_DV_resource.Stream@PNG-de-DE.png)

#### Assigning communication connection

The addressing parameters for connecting the two CPUs and for defining the instruction pair must be uniform.

- In each case store the hexadecimal value of the hardware ID of the configured S7 connection at the input parameter ID ("connectionID").

  You can find the hardware identifier in the "Network view" under "Connections".

  ![Assigning communication connection](images/94473002251_DV_resource.Stream@PNG-de-DE.png)
- In each case store a self-selected identifier (as hex value, in byte size) for the instruction pair at the input parameter R_ID ("instructionPair"). The identifier must not be already assigned for another instruction pair.

#### Behavior of CPU 1

Corresponding to the input parameter ID ("connectionID") and R_ID ("instructionPair"), the instruction "BRCV" of the CPU 2 is addressed as receiver of the data record ("SLI_plcDB_sendData_BSEND").

When the input parameter REQ ("start") supplies the signal state "TRUE", the "BSEND" instruction is started. For multiple calls, the "BSEND" instruction transmits the data record detected at input parameter SD_1 ("SLI_plcDB_sendData_BSEND") in segments to the CPU 2. According to the value "0" of the input parameter LEN ("maxLength"), is the length of the data record.

Successful transfer of the data record () is indicated by the output parameter DONE ("#done") with the signal state "TRUE". Because the values of the output parameters are only displayed for the moment of their validity, save the success status in the tag "done".

The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 1](images/94473427339_DV_resource.Stream@PNG-de-DE.png)

A new data transfer can only be initiated if the previous data has been fetched by calling of BRCV.

#### Behavior of CPU 2

CPU 2 receives a data record (in segments) of CPU 1 via the S7 connection. Corresponding to the input parameter ID ("connectionID") and R_ID ("instructionPair"), the instruction "BRCV" knows the receiver of the data record.

When the input parameter EN_R ("start") supplies the signal state "TRUE", the "BRCV" instruction is started and is ready to receive. Over several calls the "BRCV" instruction reads out the data record in segments and saves the data record at the input parameter RD_1 ("SLI_plcDB_rcvData_BRCV").

![Behavior of CPU 2](images/94473315211_DV_resource.Stream@PNG-de-DE.png)

Successful receipt of the entire data record is indicated by the output parameter NDR ("#done") with the signal state "TRUE". The length in BYTES of the actually transmitted data record is detected by the output parameter LEN ("#length"). This value is only displayed during the success status. Then "0" is detected. Because the values of the output parameters are only displayed for the moment of their validity, save the success status of "#done" in the tag "done" and the length in BYTES in the tag "readLength".

The output parameter ERROR ("error") or the tag "memErrStatus" indicates that processing in the example is taking place without errors.

![Behavior of CPU 2](images/94473173515_DV_resource.Stream@PNG-de-DE.png)

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[BSEND: Send data in segments (S7-1500)](#bsend-send-data-in-segments-s7-1500)
  
[BRCV: Receive data in segments (S7-1500)](#brcv-receive-data-in-segments-s7-1500)

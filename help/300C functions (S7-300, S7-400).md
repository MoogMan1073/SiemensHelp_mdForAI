---
title: "300C functions (S7-300, S7-400)"
package: ProgKom300C34enUS
topics: 9
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# 300C functions (S7-300, S7-400)

This section contains information on the following topics:

- [ASCII, 3964(R) (S7-300, S7-400)](#ascii-3964r-s7-300-s7-400)
- [RK 512 (S7-300, S7-400)](#rk-512-s7-300-s7-400)

## ASCII, 3964(R) (S7-300, S7-400)

This section contains information on the following topics:

- [SEND_PTP: Send data (ASCII, 3964(R)) (S7-300, S7-400)](#send_ptp-send-data-ascii-3964r-s7-300-s7-400)
- [RCV_PTP: Fetch data (ASCII, 3964(R)) (S7-300, S7-400)](#rcv_ptp-fetch-data-ascii-3964r-s7-300-s7-400)
- [RES_RCVB: Reset receive buffer (ASCII, 3964(R)) (S7-300, S7-400)](#res_rcvb-reset-receive-buffer-ascii-3964r-s7-300-s7-400)

### SEND_PTP: Send data (ASCII, 3964(R)) (S7-300, S7-400)

#### Description

You use the SEND_PTP instruction to send a block of data from a data block.

- The sending process is activated after the block is called and a positive edge is detected at the control input REQ.
- The range of data to be transmitted is specified by SD_1 (DB number and start address), and the length of the data block by LEN.
- For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at the control input R, an active sending process will be aborted and the instruction reset to the initial state. A canceled job is terminated with an error message (STATUS output).
- Use LADDR to specify the submodule I/O address, which you have defined during hardware configuration.
- DONE will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.

If the job was processed with DONE = TRUE this means that:

- When using the ASCII driver: The data where transmitted to the communication partner. It is not ensured that all data were received by the communication partner.
- When using the procedure 3964(R): The data have been transmitted to the communication partner and they where acknowledged positively by the partner. It is not ensured that the data were also passed onto the partner CPU.

In STATUS, the CPU indicates the respective event ID as the result of an error or warning. DONE or ERROR/STATUS are also output on RESET of the instruction (R = TRUE).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the instruction was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect.

#### Instance DB

The "SEND_PTP" instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Parameters

The following table shows the parameters of the instruction "SEND_PTP":

| Parameters | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| REQ | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Request: activates data exchange at the positive edge. |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset. Job is aborted. Transmission is disabled. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The I/O address of the submodule, which you have specified during hardware configuration. |
| DONE | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  - FALSE: Job not yet started or still running. - TRUE: Job was executed error-free. |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call): Job complete with error |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000: Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR = TRUE: An error has occurred, STATUS supplies detailed information on the type of error. |
| SD_1 | InOut | ANY | CPU-specific | 0 | Send parameters:   Here you enter the following values:  - The number of the DB from which the data will be transmitted. - The data byte number, starting from which data will be transmitted. Possible values: 0 to 8190   For example: DB 10 from byte 2 -> DB10.DBB2  Note: Note that for S7-300 CPUs, the parameter SD_1 always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| LEN | InOut | INT | 1 to 1024 | 1 | Here you specify the length of the data block that is to be transmitted (length is set here indirectly). |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Data consistency

Data consistency is limited to 206 bytes. If you want consistent data transmission exceeding 206 bytes, you must take the following into account:

Do not write to the currently used section of the send range SD_1 again until the sending process has concluded. This is the case when the status parameter DONE assumes the value TRUE.

### RCV_PTP: Fetch data (ASCII, 3964(R)) (S7-300, S7-400)

#### Description

You use the RCV_PTP instruction to receive data and then store them in a data block.

- After the instruction has been called with the value TRUE at control input EN_R, it is ready to receive data. You cancel the current transmission by setting the signal status of parameter EN_R to FALSE. A canceled job is terminated with an error message (STATUS output). The input is switched off as long as the signal status of parameter EN_R is set to FALSE.
- The receive area is specified by RD_1 (DB number and start address), and the length of the data block by LEN.
- For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at control input R, the current transmission will be canceled and the instruction reset to its initial state. A canceled receive job is terminated with an error message (STATUS output).
- Use LADDR to specify the submodule I/O address, which you have defined during hardware configuration.
- NDR will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.
- In STATUS , the CPU indicates the respective event ID as the result of an error or warning.
- NDR or ERROR/STATUS are also output on RESET of the instruction (R = TRUE) (parameter LEN == 16#00).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the instruction was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect.

#### Instance DB

The "RCV_PTP" instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Parameters

The following table shows the parameters of the instruction "RCV_PTP":

| Parameters | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Enable to receive:  Receive enable |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset:  Job is aborted. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The I/O address of the submodule, which you have specified during hardware configuration. |
| NDR | Output | BOOL | TRUE/FALSE | FALSE | Job done without error, data were accepted  - FALSE: Job not started yet or still running - TRUE: Job completed without errors |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call): Job complete with error |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000:  Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR = TRUE: An error has occurred, STATUS supplies detailed information on the type of error. |
| RD_1 | InOut | ANY | CPU-specific | 0 | Receive parameter:   Here you specify:  - The number of the DB in which the received data are to be stored. - The data byte number starting at which the received data will be stored. Possible values: 0 to 8190   For example: DB 20 starting with byte 5 -> DB20.DBB5  Note: Note that for S7-300 CPUs, the parameter RD_1 always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| LEN | InOut | INT | 0 to 1024 | 0 | Output of the data length (number of bytes) |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Data consistency

Data consistency is limited to 206 bytes. If you want consistent data transmission exceeding 206 bytes, you must take the following into account:

Do not access the receive DB again until the data have been completely received (NDR = TRUE). Then, disable the receiving DB (EN_R = FALSE) until you have processed the data.

### RES_RCVB: Reset receive buffer (ASCII, 3964(R)) (S7-300, S7-400)

#### Description

You use the RES_RECV instruction to delete the entire receive buffer of the module. All stored message frames are discarded. A message frame that is incoming when the RES_RCVB instruction is called will be saved.

- The job is activated after the instruction is called and a positive edge is detected at control input REQ. The job can run across multiple calls (program cycles).
- For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at control input R, the deleting process will be canceled and the instruction reset to its initial state. A canceled job is terminated with an error message (STATUS output).
- Use LADDR to specify the submodule I/O address, which you have defined during hardware configuration.
- DONE will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.
- In STATUS the CPU indicates the respective event ID as the result of an error or warning.
- DONE or ERROR/STATUS are also output on RESET of the instruction (R = TRUE).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the block was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect.

#### Instance DB

The RES_RCVB instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Parameter

The following table shows the parameters of the instruction RES_RCVB:

| Parameter | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| REQ | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Request:   Activates the job on a positive edge. |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset:  Job is aborted. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The I/O address of the submodule, which you have specified during hardware configuration. |
| DONE | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  - FALSE: Job not yet started or still running. - TRUE: Job was executed error-free. |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call): Job complete with error |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000: Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR = TRUE: An error has occurred, STATUS supplies detailed information on the type of error. |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

## RK 512 (S7-300, S7-400)

This section contains information on the following topics:

- [SEND_RK: Send data (RK 512) (S7-300, S7-400)](#send_rk-send-data-rk-512-s7-300-s7-400)
- [FETCH_RK: Fetch data (RK 512) (S7-300, S7-400)](#fetch_rk-fetch-data-rk-512-s7-300-s7-400)
- [SERVE_RK: Receive and provide data (RK 512) (S7-300, S7-400)](#serve_rk-receive-and-provide-data-rk-512-s7-300-s7-400)

### SEND_RK: Send data (RK 512) (S7-300, S7-400)

#### Description

You use the SEND_RK to send a block of data from a data block.

- The send job is activated after the instruction is called and a positive edge is detected at control input REQ.
- The range of data to be transmitted is specified by SD_1 (DB number and start address), and the length of the data block by LEN.
- You also specify the receive area on the partner in the instruction. The CPU enters this information in the message frame header and transfers it to the partner.
- The destination is specified by the CPU number in R_CPU (only relevant for multiprocessor communication), the data type in R_TYPE (data blocks (DB) and expanded data blocks (DX)), the data block number in R_DBNO and the offset in R_OFFSET to which the first byte is to be written.
- In R_CF_BYT and R_CF_BIT you declare the interprocessor communication flag byte and bit on the partner CPU.
- With the SYNC_DB parameter, you specify the DB where the data that are common to all instructions used for initialization during startup and synchronization will be stored. The DB number must be identical for all instructions used in your user program.
- For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at control input R, the active sending process will be aborted and the instruction reset to the initial state. A canceled job is terminated with an error message (STATUS output).
- Use LADDR to specify the submodule I/O address, which you have defined during hardware configuration.
- DONE will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.
- If the job was processed with DONE = TRUE, the data were sent to the communication partner, the communication partner acknowledged them positively, and they were then passed on to the partner CPU.
- In STATUS, the CPU indicates the respective event ID as the result of an error or warning.
- DONE or ERROR/STATUS are also output on RESET of the instruction (R = TRUE).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the block was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect.

#### Instance DB

The SEND_RK instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Special features when sending data

Take the following special features into account when "sending data":

- With RK 512 you can only send an even number of data. If you declare an odd length (LEN) of data, an additional fill byte with the value "0" will be appended to the transmitted data.
- In RK 512 you can only declare an even offset. If you declare an odd offset the data are stored in the partner station from the next lower even offset.

  Example: Offset is "7", the data will be stored as of byte "6".

#### Parameters

The following table shows the parameters of the instruction SEND_RK:

| Parameters | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| SYNC_DB | Input | INT | CPU-specific | 0 | Number of the DB where the common data for the synchronization of the RK instructions are stored (minimum length = 240 bytes). |
| REQ | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Request:   Activates the job on a positive edge. |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset:  Job is aborted. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The I/O address of the submodule, which you have specified during hardware configuration. |
| R_CPU | Input | INT | 0 to 4 | 1 | CPU number of the partner CPU  (only for multiprocessor operation) |
| R_TYPE | Input | CHAR | ‘D’, ‘X’ | 'D' | Address type on the partner CPU (only uppercase allowed)  'D': Data block  'X': Expanded data block |
| R_DBNO | Input | INT | 0 to 255 | 0 | Data block number on the partner CPU |
| R_OFFSET | Input | INT | 0 to 510  (even values only) | 0 | Data byte number on the partner CPU |
| R_CF_BYT | Input | INT | 0 to 255 | 255 | Communication flag byte on partner CPU  (255: Means: without interprocessor communication flag) |
| R_CF_BIT | Input | INT | 0 to 7 | 0 | Communication flag bit on the partner CPU |
| DONE | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  - FALSE: Job not yet started or still running. - TRUE: Job was executed error-free. |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call): Job complete with error |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000: Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR=TRUE:   An error has occurred, STATUS supplies detailed information on the type of error. |
| SD_1 | Input | ANY | CPU-specific | 0 | Send parameters:   Here you specify:  - The number of the DB from which the data will be transmitted. - The data byte number, starting from which data will be transmitted. Possible values: 0 to 8190   For example: DB 10 from byte 2 -> DB10.DBB2  Note: Note that for S7-300 CPUs, the parameter SD_1 always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| LEN | Input | INT | 1 to 1024 | 1 | Here you specify the length of the data block that is to be transmitted (length is set here indirectly). |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Data in the message frame header

The table below shows the data in the message frame header of the RK 512 message frame.

| Source on your S7 automation system (local CPU) | To target,  partner CPU | Message frame header, bytes |  |  |
| --- | --- | --- | --- | --- |
|  |  | **3/4 command type** | **5/6 D-DBNO** <sup>1</sup>  **/  D offset** <sup>2</sup> | **7/8 number in** |
| Data block | Data block | AD | DB/DW<sup>3</sup> | Words |
| Data block | Expanded data block | AD | DB/DW<sup>3</sup> | Words |
| <sup>1</sup> D-DBNO: Destination data block number   <sup>2</sup> D offset: Destination start address   <sup>3 </sup>DW: Offset in words |  |  |  |  |

#### Data consistency

Data consistency is limited to 128 bytes. If you want consistent data transmission exceeding 128 bytes, you must take the following into account:

Do not write to the currently used section of the send range SD_1 again until the sending process has concluded. This is the case when the status parameter DONE assumes the value TRUE.

### FETCH_RK: Fetch data (RK 512) (S7-300, S7-400)

#### Description

You use the FETCH_RK instruction to retrieve a block of data from the partner and store the data in a data block.

- The sending process is activated after the block is called and a positive edge is detected at the control input REQ.
- The area in which the retrieved data are stored is specified by RD_1 (DB number and start address), and the length of the data block by LEN.
- You also specify the partner area from which the data will be fetched for the instruction. The CPU enters this information in the RK512 message frame header and transfers it to the partner.
- The partner area is determined by the CPU number in R_CPU (only relevant for multiprocessor communication), the data type in R_TYPE (data blocks, expanded data blocks, memory bits, inputs, outputs, counters and timers), the data block number in R_DBNO (only relevant for data blocks and expanded data blocks) and the offset in R_OFFSET, from where the first byte is to be retrieved.
- Use R_CF_BYT and R_CF_BIT to declare the interprocessor communication flag byte and bit on the partner CPU.
- With the SYNC_DB parameter, you specify the DB where the data that are common to all instructions used for initialization during startup and synchronization will be stored. The DB number must be identical for all instructions used in your user program.
- For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at control input R, the current transmission will be canceled and the instruction reset to its initial state. A canceled job is terminated with an error message (STATUS output).
- Use LADDR to specify the submodule I/O address, which you have defined during hardware configuration.
- DONE will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.
- In STATUS, the CPU indicates the respective event ID as the result of an error or warning.
- DONE or ERROR/STATUS are also output on RESET of the instruction (R = TRUE).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the instruction was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect. If data will be retrieved from your CPU, you must program a [SERVE_RK](#serve_rk-receive-and-provide-data-rk-512-s7-300-s7-400) instruction on your CPU.

#### Instance DB

The FETCH_RK instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Special features for (expanded) data blocks

Note the following special features when "retrieving data" from a data block and expanded data blocks:

- With RK 512 you can only send an even number of data. If you declare an odd length (LEN) of data, an additional byte will always be appended to the transmitted data. In the destination DB, however, the correct number of data is always entered.
- In RK 512 you can only declare an even offset. If you declare an odd offset the data are stored in the partner station starting with the next smaller even offset.

  Example: Offset is 7, the data are stored from byte 6.

#### Special features for timers and counters

When you retrieve times or counters from your communication partner, you must take into account that you must retrieve two bytes for every time or counter. For example, if you want to retrieve 10 counters you must declare a length of 20.

#### Parameters

The following table shows the parameters of the instruction "FETCH_RK":

| Parameters | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| SYNC_DB | Input | INT | CPU-specific | 0 | Number of the DB where the common data for the synchronization of the RK instructions are stored (minimum length = 240 bytes). |
| REQ | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Request:   Activates the job on a positive edge. |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset:  Job is aborted. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The I/O address of your sub-module that you specified during hardware configuration. |
| R_CPU | Input | INT | 0 to 4 | 1 | CPU number of the partner CPU  (only for multiprocessor operation) |
| R_TYPE | Input | CHAR | 'D', 'X', 'M', 'I', 'Q', 'C', 'T' | 'D' | Address type on the partner CPU  - 'D': Data block - 'X': Expanded data block - 'M': Bit memory - 'I': Inputs - 'Q': Outputs - 'C': Counters - 'T': Timers |
| R_DBNO | Input | INT | 0 to 255 | 0 | Data block number on the partner CPU |
| R_OFFSET | Input | INT | See table: "Parameters for data source (partner CPU)" | 0 | Data byte number on the partner CPU |
| R_CF_BYT | Input | INT | 0 to 255 | 255 | Communication flag byte on partner CPU  (255: Means: without interprocessor communication flag) |
| R_CF_BIT | Input | INT | 0 to 7 | 0 | Communication flag bit on the partner CPU |
| DONE | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  - FALSE: Job not yet started or still running. - TRUE: Job was executed error-free. |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  Job complete with errors |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000: Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR=TRUE:   An error has occurred, STATUS supplies detailed information on the type of error. |
| RD_1 | Input | ANY | CPU-specific | 0 | Receive parameter:   Here you specify:  - The number of the DB in which the retrieved data are to be stored. - The data byte number starting at which the retrieved data are to be stored. Possible values: 0 to 8190   For example: DB 10 from byte 2 -> DB10.DBB2  Note: Note that for S7-300 CPUs, the parameter RD_1 always requires the full specification of the DB parameters (for example, P#DB13.DBX0.0 byte 100). The omission of an explicit DB number is only permitted for S7-300 CPUs and leads to an error message in the user program. |
| LEN | Input | INT | 1 to 1024 | 1 | Here you specify the length of the data block that is to be retrieved (length is set here indirectly).   A length of two bytes must be declared for each timer and counter. |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters for data source (partner CPU)

The data types that can be transmitted are shown in the table below.  
The value R_OFFSET is specified by the partner CPU.

| Source on the partner CPU | R_TYPE | R_NO | R_OFFSET (in bytes) |
| --- | --- | --- | --- |
| Data block | 'D' | 0 - 255 | 0 - 510<sup>, </sup>only even values |
| Expanded data block | 'X' | 0 - 255 | 0 - 510<sup>, </sup>only even values |
| Bit memory | ’M’ | irrelevant | 0 - 255 |
| Inputs | 'I' | irrelevant | 0 - 255 |
| Outputs | ’Q’ | irrelevant | 0 - 255 |
| Counters | 'C' | irrelevant | 0 - 255 |
| Timers | 'T' | irrelevant | 0 - 255 |

#### Data in the message frame header

The table below shows the data in the message frame header of the RK 512 message frame.

| Source on the partner CPU | To the destination, your S7 automation system (local CPU) | Message frame header, bytes |  |  |
| --- | --- | --- | --- | --- |
| 3/4 command type | 5/6 S-DBNO<sup>1</sup> /  S offset<sup>2</sup> | 7/8 number in |  |  |
| Data block | Data block | ED | DB/DW | Words |
| Expanded data block | Data block | EX | DB/DW | Words |
| Bit memory | Data block | EM | Byte address | Bytes |
| Inputs | Data block | EE | Byte address | Bytes |
| Outputs | Data block | IO | Byte address | Bytes |
| Counters | Data block | EC | Counter number | Words |
| Timers | Data block | ET | Time number | Words |
| <sup>1</sup> S-DBNO: Source Data Block Number   <sup>2</sup> S offset: Source start address |  |  |  |  |

#### Data consistency

Data consistency is limited to 128 bytes. If you want consistent data transmission exceeding 128 bytes, you must take the following into account:

Do not write to the currently used section of the receive range RD_1 again until the transmission process has concluded. This is the case when the status parameter DONE assumes the value TRUE.

### SERVE_RK: Receive and provide data (RK 512) (S7-300, S7-400)

#### Description

You use the SERVE_RK instruction to receive and provide data.

- Receiving data: The data are stored in the area that is specified by the partner in the RK 512 message frame header. A call of the instruction is required when the communication partner executes a "Send data" job (SEND job).
- Serving data: The data are retrieved from the area that is specified by the partner in the RK 512 message frame header. A call of the instruction is required when the communication partner executes a "Fetch data" job (FETCH job).

After the instruction has been called with the value TRUE at control input EN_R, it is ready to fetch data. You cancel the current transmission by setting the signal status of parameter EN_R to FALSE. A canceled job is terminated with an error message (STATUS output). The input is switched off as long as the signal status of parameter EN_R is set to FALSE.

With the SYNC_DB parameter, you specify the DB where the data that are common to all instructions used for initialization during startup and synchronization will be stored. The DB number must be identical for all instructions used in your user program.

For the instruction to process the job, you must call it with R (Reset) = FALSE. With a positive edge at control input R, the current transmission will be canceled and the instruction reset to its initial state. A canceled job is terminated with an error message (STATUS output).

Use LADDR to specify the submodule I/O address, which you have defined in HW Config.

NDR will be set to TRUE if the job was completed without errors; ERROR will be set to TRUE if the job was completed with errors.

With NDR = TRUE for an instruction call, the CPU indicates in the parameters L_TYPE, L_DBNO and L_OFFSET the area where data were stored or from where they were retrieved. Also shown are the parameters L_CF_BYT and L_CF_BIT of a call as well as the length LEN of the respective job.

In STATUS, the CPU indicates the respective event ID as the result of an error or warning.

NDR or ERROR/STATUS are also output on RESET of the instruction (R = TRUE) (parameter LEN == 16#00).

The binary result BR is reset if an error has occurred. The status of the binary result is TRUE if the block was completed without errors.

> **Note**
>
> A parameter check is not included in the instruction. The CPU can go to STOP mode if the parameter assignment is incorrect.

#### Instance DB

The SERVE_RK instruction operates in combination with an instance DB. The DB number is passed on with the call. Access to the data in the instance DB is not allowed.

#### Using interprocessor communication flags

You can lock or enable SEND and FETCH jobs of your communication partner via an interprocessor communication flag. Thus, you can prevent overwriting or reading of data that have not yet been processed.

You can specify an interprocessor communication flag for every job.

![Using interprocessor communication flags](images/19191116811_DV_resource.Stream@PNG-en-US.png)

#### Example: SEND_RK with interprocessor communication flag:

In this example the communication partner transmits data to DB 101 on your CPU

1. On your CPU, set the interprocessor communication flag 100.6 to FALSE.
2. On your communication partner, specify interprocessor communication flag 100.6 (parameters R_CF_BYT, R_CF_BIT) for the SEND job.

   The interprocessor communication flag is transferred to your CPU in the RK 512 message frame header.

   Before it processes the job, the CPU verifies the interprocessor communication flag that is specified in the RK 512 message frame header. The job is only processed if the interprocessor communication flag is set to FALSE on your CPU. If the interprocessor communication flag is set to TRUE, then the error message "32 hex" will be transmitted to the communication partner in the response message frame.

   After the data have been transferred to DB 101, interprocessor communication flag 100.6 will be set to TRUE on your CPU by SERVE. Also, the communication flag byte and bit on SERVE are output for the duration of one call (if NDR = TRUE).
3. When you evaluate the interprocessor communication flag (interprocessor communication flag 100.6 = TRUE) in your user program you can see whether the job is complete and the transmitted data can be processed.
4. After you have processed the data in your user program you must reset the interprocessor communication flag 100.6 to FALSE. Your communication partner can only execute the job again without error when this has been done.

#### Parameter

The following table shows the parameters of the instruction "SERVE_RK":

| Parameter | Declaration | Data type | Range of values | Default | Description |
| --- | --- | --- | --- | --- | --- |
| SYNC_DB | Input | INT | CPU-specific | 0 | Number of the DB where the common data for the synchronization of the RK instructions are stored (minimum length = 240 bytes). |
| EN_R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Enable to receive:  Job enable |
| R | Input | BOOL | TRUE/FALSE | FALSE | Control parameter Reset:  Job is aborted. |
| LADDR | Input | WORD | CPU-specific | W#16#03FF | The submodule I/O address, which you have specified during hardware configuration. |
| NDR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter New Data Ready (this parameter is only set for the duration of one call):  - FALSE: Job not yet started or still running. - TRUE: Job was executed error-free. |
| ERROR | Output | BOOL | TRUE/FALSE | FALSE | Status parameter (this parameter is only set for the duration of one call):  Job complete with errors |
| STATUS | Output | WORD | W#16#0000 to W#16#FFFF | W#16#0000 | Status parameter (This parameter is only set for the duration of one call. To display the status, you should copy STATUS to a free data area.)  STATUS has the following meaning, dependent on the ERROR bit:  - ERROR=FALSE:   - STATUS has the value W#16#0000: Neither warning nor error   - STATUS has the value <> W#16#0000: Warning, STATUS supplies detailed information. - ERROR=TRUE:   An error has occurred, STATUS supplies detailed information on the type of error. |
| L_TYPE | Output | CHAR | 'D'          'D', 'M', 'I', 'Q', 'C', 'T', | ' ' | **Receiving data:**   Type of the destination area on the local CPU (only upper case allowed):  - 'D': Data block    **Serving data:**   Type of the source area on the local CPU (only uppercase allowed):  - 'D': Data block - 'M': Bit memory - 'I': Inputs - 'Q': Outputs - 'C': Counters - 'T': Timers   This parameter is only set for the duration of one call. |
| L_DBNO | Output | INT | CPU-specific | 0 | Data block number on local CPU. This parameter is only set for the duration of one call. |
| L_OFFSET | Output | INT | 0 - 510 | 0 | Data byte number on local CPU. This parameter is only set for the duration of one call. |
| L_CF_BYT | Output | INT | 0 to 255 | 0 | Communication flag byte on local CPU. This parameter is only set for the duration of one call.   (255: Means: without interprocessor communication flag) |
| L_CF_BIT | Output | INT | 0 to 7 | 0 | interprocessor communication flag on local CPU. This parameter is only set for the duration of one call. |
| LEN | InOut | INT | 0 to 1024 | 0 | Length of message frame, number in bytes (this parameter is only set for the duration of one call). |
|  |  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Data consistency

Data consistency is limited to 128 bytes. If you want consistent data transmission exceeding 128 bytes, you must take the following into account:

Use the connection memory function. Do not access the data again until they have been completely transmitted (evaluation of the interprocessor communication flag specified for this job; the interprocessor communication flag is active for one instruction call if NDR = TRUE). Do not reset the interprocessor communication flag to FALSE until you have processed the data.

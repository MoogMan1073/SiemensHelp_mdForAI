---
title: "Communication with iSlave / iDevice (S7-300, S7-400)"
package: ProgKomISlave34enUS
topics: 4
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communication with iSlave / iDevice (S7-300, S7-400)

This section contains information on the following topics:

- [I_GET: Read data from a communication partner within the local S7 station (S7-300, S7-400)](#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)
- [I_PUT: Write data to a communication partner within the local S7 station (S7-300, S7-400)](#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)
- [I_ABORT: Abort an existing connection to a communication partner within the local S7 station (S7-300, S7-400)](#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)

## I_GET: Read data from a communication partner within the local S7 station (S7-300, S7-400)

### Description

With the "I_GET" instruction, you can read data from a communication partner that is inside the local S7 station. The communication partner can be located in the central controller, an expansion unit, or be part of the distributed configuration. Please make sure that you have assigned distributed communication partners to the local CPU. There is no corresponding instruction on the communication partner.

Receiving is activated by calling the instruction with REQ=1. Then call the instruction until receipt of data is indicated with BUSY=0. RET_VAL Then contains the length of the received block of data in bytes.

Make sure that the receive area defined with the RD parameter (on the receiving CPU) is at least as long as the read area defined by the VAR_ADDR parameter (on the communication partner). The data types of RD and VAR_ADDR must also match.

### Parameter

The following table shows the parameters of the "I_GET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| CONT | Input | BOOL | I, Q, M, D, L | Control parameter "continue"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| IOID | Input | BYTE | I, Q, M, D, L, P or constant | Identifier of the address area on the partner module:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L, P or constant | Logical address of the partner module For a mixed module, the lower of the two addresses must be specified. |
| VAR_ADDR | Input | ANY | I, Q, M, D | Reference to the area on the partner CPU from which the data will be read. Choose a data type that is supported by the communication partner. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code.  If no error occurs, RET_VAL contains the length in bytes of the block of data copied to the receive area RD as a positive number. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY=1: Receiving is not yet complete. - BUSY=0: Receiving is complete or there is no receiving process active. |
| RD | Output | ANY | I, Q, M, D | Reference to the receive area (receive data area). The following data types are permitted: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5_TIME, DATE_AND_TIME as well as arrays of the data types listed with the exception of BOOL.  The receive area RD must be at least as long as the read area VAR_ADDR on the communication partner. The data types for RD and VAR_ADDR must also match. The maximum size of the receive area is 76 bytes. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection established by "I_GET" is terminated. Whether the received data located in a buffer of the operating system are lost depends on the type of subsequent restart performed:

- Following a hot restart (not on the S7-300 and the S7-400H), the data is copied to the area defined by RD.
- Following a warm or cold restart, the data are discarded.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the data transfer with "I_GET": The data will also be read in STOP mode.

### Data consistency

The data are received in a consistent state.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## I_PUT: Write data to a communication partner within the local S7 station (S7-300, S7-400)

### Description

With the "I_PUT" instruction, you write data to a communication partner that is inside the local S7 station. The communication partner can be located in the central controller, an expansion unit, or be part of the distributed configuration. Please make sure that you have assigned distributed communication partners to the local CPU. There is no corresponding instruction on the communication partner.

The send operation is started after the instruction is called with signal level 1 at the REQ control input.

Make sure that the send area defined with the SD parameter (on the sending CPU) is the same length as the receive area defined by the VAR_ADDR parameter (on the communication partner). The data types of SD and VAR_ADDR must also match.

### Parameter

The following table shows the parameters of the "I_PUT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| CONT | Input | BOOL | I, Q, M, D, L | Control parameter "continue"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| IOID | Input | BYTE | I, Q, M, D, L, P or constant | Identifier of the address area on the partner module:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L, P or constant | Logical address of the partner module. For a mixed module, the lower of the two addresses must be specified. |
| VAR_ADDR | Input | ANY | I, Q, M, D, L | Reference to the area on the partner CPU to which the data will be written. Choose a data type that is supported by the communication partner. |
| SD | Input | ANY | I, Q, M, D | Reference to the area on the local CPU that contains the data to be sent. The following data types are permitted: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME as well as arrays of the data types listed with the exception of BOOL.  SD must be the same length as the VAR_ADDR parameter of the communication partner. The data types for SD and VAR_ADDR must also match. The maximum size of the send area is 76 bytes. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY=1: Sending is not yet complete. - BUSY=0: Sending is complete or there is no sending process active. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection established by "I_PUT" is terminated. Data can no longer be sent. If the send data have already been copied to the internal buffer when the CPU changes mode, the contents of the buffer are discarded.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the data transfer with "I_PUT". The transmitted data will be written nevertheless.

### Data consistency

The data are sent in a consistent state.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## I_ABORT: Abort an existing connection to a communication partner within the local S7 station (S7-300, S7-400)

### Description

With the "I_ABORT" instruction, you abort a connection that was established with an "[I_GET](#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" or "[I_PUT](#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" instruction to a communication partner that is within the local S7 station. If the job belonging to "[I_GET](#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" or "[I_PUT](#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" is completed (BUSY = 0), the connection resources used at both ends are released after "I_ABORT" is called.

If the job belonging to "[I_GET](#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" or "[I_PUT](#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" is not yet completed (BUSY = 1), you will need to call the relevant instruction again with REQ = 0 and CONT = 0 after the connection has been aborted and then wait for BUSY = 0. Only then are all the connection resources released again.

You can only call "I_ABORT" at the end that is executing "[I_PUT](#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" or "[I_GET](#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" (in other words, at the client end).

The connection abort is activated by calling the instruction with REQ=1.

### Parameters

The following table shows the parameters of the "I_ABORT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| IOID | Input | BYTE | I, Q, M, D, L, P or constant | Identifier of the address area on the partner module:  - B#16#54 = Peripheral input (PI) - B#16#55 = Peripheral output (PQ)   If the module is a mixed module, the area identifier of the lower address must be specified. If the addresses are identical, specify B#16#54. |
| LADDR | Input | WORD | I, Q, M, D, L, P or constant | Logical address of the partner module. For a mixed module, the lower of the two addresses must be specified. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The connection abort is not yet completed. - BUSY = 0: The connection abort is completed. |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection abort started with "I_ABORT" will be completed.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the connection abort with "I_ABORT". The connection is aborted.

### RET_VAL parameter

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

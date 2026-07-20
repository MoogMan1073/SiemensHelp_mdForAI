---
title: "MPI communication (S7-300, S7-400)"
package: ProgKomMPI34enUS
topics: 6
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# MPI communication (S7-300, S7-400)

This section contains information on the following topics:

- [X_SEND: Send data to a communication partner outside the local S7 station (S7-300, S7-400)](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)
- [X_RCV: Receive data from a communication partner outside the local S7 station (S7-300, S7-400)](#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)
- [X_GET: Read data from a communication partner outside the local S7 station (S7-300, S7-400)](#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)
- [X_PUT: Write data to a communication partner outside the local S7 station (S7-300, S7-400)](#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)
- [X_ABORT: Abort an existing connection to a communication partner outside the local S7 station (S7-300, S7-400)](#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)

## X_SEND: Send data to a communication partner outside the local S7 station (S7-300, S7-400)

### Description

With the "X_SEND" instruction, you send data to a communication partner outside the local S7 station. The data is received on the communication partner using the "[X_RCV](#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction. The send operation is started after the instruction is called with REQ=1.

Make sure that the send area defined by the SD parameter (on the sending CPU) is smaller than or the same size as the receive area defined by the RD parameter (on the communication partner). If SD is data type BOOL, RD must also be data type BOOL.

### Parameters

The following table shows the parameters of the "X_SEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| CONT | Input | BOOL | I, Q, M, D, L | Control parameter "continue"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| DEST_ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameter "destination ID". It contains the configured MPI address of the communication partner. |
| REQ_ID | Input | DWORD | I, Q, M, D, L or constant | Job identifier to identify the data on the communication partner. |
| SD | Input | ANY | I, Q, M, D | Reference to the send area. The following data types are allowed: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5TIME, DATE_AND_TIME and arrays of the specified data types with the exception of BOOL. The maximum size of the send area is 76 bytes. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: Sending is not yet completed. - BUSY = 0: Sending is completed or there is no send operation active. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Data consistency

The data are sent in a consistent state.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## X_RCV: Receive data from a communication partner outside the local S7 station (S7-300, S7-400)

### Description

With the "X_RCV" instruction, you receive the data sent by one or more communication partners outside the local S7 station using the "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction.

With the "X_RCV" instruction

- you can check whether data are available at the current time. The data were entered in an internal queue by the operating system.
- You can copy the oldest block of data from the queue to a selected receive area.

### Parameters

The following table shows the parameters of the "X_RCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_DT | Input | BOOL | I, Q, M, D, L | Control parameter "enable data transfer". Use the value 0 to verify whether at least one data block is available. The value 1 causes the oldest data block in the queue to copied into the work memory area that you have specified with RD. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. If no error occurs, RET_VAL contains  - if EN_DT=0/1 and NDA = 0: W#16#7000. In this case, no block of data is in the queue. - If EN_DT=0 and NDA=1 the length of the oldest block of data entered in the queue as a positive number in bytes. - If EN_DT=1 and NDA=1 the length of the oldest block of data copied to the receive area RD as a positive number in bytes. |
| REQ_ID | Output | DWORD | I, Q, M, D, L | Job identifier of the "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction whose sent data is first in the queue, in other words, the oldest data in the queue. If there is no block of data in the queue, REQ_ID has the value "0". |
| NDA | Output | BOOL | I, Q, M, D, L | Status parameter "new data arrived".  NDA=0:  - There is no block of data in the queue.   NDA=1:   - The queue contains at least one block of data. ("X_RCV" call with EN_DT=0). - The oldest block of data in the queue was copied to the user program ("X_RCV" call with EN_DT=1). |
| RD | Output | ANY | I, Q, M, D | Reference to the receive area (receive data area). The following data types are allowed: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5_TIME, DATE_AND_TIME and arrays of the specified data types with the exception of BOOL.  If you want to discard the oldest block of data in the queue, assign RD the value NIL. .The maximum size of the receive area is 76 bytes. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Show data reception with EN_DT=0

As soon as data from a communication partner arrive, they are entered in the queue by the operating system in the order in which they are received.

If you want to check whether at least one block of data is in the queue, call "X_RCV" with EN_DT=0 and evaluate the output parameter NDA as follows:

- NDA=0 means that the queue does not contain a block of data. REQ_ID is irrelevant, RET_VAL contains W#16#7000.
- NDA=1 means that there is at least one block of data that can be fetched in the queue .

  In this case, you also evaluate the output parameters RET_VAL and possibly REQ_ID. RET_VAL contains the length of the data block in bytes, REQ_ID has the job ID of the send block. If there are several blocks of data in the queue, REQ_ID and RET_VAL belong to the oldest block of data in the queue.

  ![Show data reception with EN_DT=0](images/18888558731_DV_resource.Stream@PNG-en-US.png)

### Accepting data in the receive area with EN_DT=1

If you call "X_RCV" with EN_DT=1 , the oldest available block of data in the queue is copied to the area of the work memory specified by RD. RD must be greater than or equal to the send area of the associated "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction that is defined by the SD parameter. If its input parameter SD is data type BOOL, RD must also be data type BOOL. If you want to store the received data in different areas, you can determine REQ_ID (instruction call with EN_DT=0) and select RD (with EN_DT=1) accordingly in the subsequent call. If an error occurred when copying, then the length of the copied block of data in bytes is in RET_VAL and a positive acknowledgment will be sent to the sender.

![Accepting data in the receive area with EN_DT=1](images/18885820811_DV_resource.Stream@PNG-en-US.png)

### Discarding data

If you do not want to accept the data, assign the value NIL to RD. In this case, the sender receives a negative acknowledgment (RET_VAL of the corresponding "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction has the value W#16#80B8) and "0" is entered in RET_VAL of the "X_RCV" instruction.

### Data consistency

After a call with EN_DT=1 and RETVAL=W#16#00xy, there is new data in the receive area RD. A further block call can overwrite this data. To prevent this, do not call "X_RCV" with the same receive area RD until you have evaluated the received data.

### Change to STOP mode

If the CPU changes to STOP mode

- All newly arriving jobs are acknowledged negatively.
- Applies for the jobs that have already arrived: All jobs that have arrived and are in the queue are acknowledged negatively.

  - Following a warm or cold restart, the data are discarded.
  - If there is a subsequent hot restart (not on an S7-300 or S7-400H), the data block belonging to the oldest job is entered in the user program, if it was queried before the transition to STOP mode (by calling "X_RCV" with EN_DT=0). Otherwise it is discarded.

    All other blocks of data are discarded.

### Connection abort

If the connection is terminated a job belonging to the connection that is already in the queue is discarded.

Exception: If this job is the oldest in the queue and you have already detected its presence by calling X_RCV" with EN_DT=0, you can enter it in the receive area with EN_DT=1.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

## X_GET: Read data from a communication partner outside the local S7 station (S7-300, S7-400)

### Description

With the "X_GET" instruction, you can read data from a communication partner that is inside the local S7 station. There is no corresponding instruction on the communication partner.

The read operation is started after the instruction is called with REQ=1. Following this, you continue to call "X_GET" until the receipt of the data is indicated with BUSY=0. RET_VAL contains the length of the received block of data in bytes.

Make sure that the receive area defined with the RD parameter (on the receiving CPU) is at least as long as the read area defined by the VAR_ADDR parameter (on the communication partner). The data types of RD and VAR_ADDR must also match.

### Parameters

The following table shows the parameters of the "X_GET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| CONT | Input | BOOL | I, Q, M, D, L | Control parameter "continue"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| DEST_ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameter "destination ID". It contains the MPI address of the communication partner. You have configured this. |
| VAR_ADDR | Input | ANY | I, Q, M, D | Reference to the area on the partner CPU from which the data will be read. Choose a data type that is supported by the communication partner. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code.  If no error occurs, RET_VAL contains the length in bytes of the block of data copied to the receive area RD as a positive number. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: Receiving is not yet completed. - BUSY = 0: Receiving is completed or there is no receive operation active. |
| RD | Output | ANY | I, Q, M, D | Reference to the receive area (receive data area). The following data types are allowed: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME, S5_TIME, DATE_AND_TIME and arrays of the specified data types with the exception of BOOL.  The receive area RD must be at least as long as the read area VAR_ADDR on the communication partner. The data types for RD and VAR_ADDR must also match. The maximum size of the receive area is 76 bytes. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection established by "X_GET" is terminated. Whether the received data located in a buffer of the operating system are lost depends on the type of subsequent restart performed:

- Following a hot restart (not on the S7-300 and the S7-400H), the data is copied to the area defined by RD.
- Following a warm or cold restart, the data are discarded.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the data transfer with "X_GET": The data will also be read in STOP mode.

### Data consistency

The data are received in a consistent state.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## X_PUT: Write data to a communication partner outside the local S7 station (S7-300, S7-400)

### Description

With the "X_PUT" instruction, you write data to a communication partner that is outside the local S7 station. There is no corresponding instruction on the communication partner.

The read operation is started after the instruction is called with REQ=1. Following this, you continue to call "X_PUT" until the receipt of the data is indicated with BUSY=0.

Make sure that the send area defined with the SD parameter (on the sending CPU) is the same length as the receive area defined by the VAR_ADDR parameter (on the communication partner). The data types of SD and VAR_ADDR must also match.

### Parameters

The following table shows the parameters of the "X_PUT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| CONT | Input | BOOL | I, Q, M, D, L | Control parameter "continue"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400). |
| DEST_ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameter "destination ID". It contains the MPI address of the communication partner. You have configured this. |
| VAR_ADDR | Input | ANY | I, Q, M, D | Reference to the area on the partner CPU to which the data will be written. Choose a data type that is supported by the communication partner. |
| SD | Input | ANY | I, Q, M, D | Reference to the area on the local CPU that contains the data to be sent. The following data types are allowed: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TOD, TIME,S5_TIME, DATE_AND_TIME and arrays of the specified data types with the exception of BOOL.  SD must be the same length as the VAR_ADDR parameter of the communication partner. The data types for SD and VAR_ADDR must also match. The maximum size of the send area is 76 bytes. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: Sending is not yet completed. - BUSY = 0: Sending is completed or there is no send operation active. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection established by "X_PUT" is terminated. Data can no longer be sent. If the send data have already been copied to the internal buffer when the CPU changes mode, the contents of the buffer are discarded.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the data transfer with "X_PUT": The transmitted data will be written nevertheless.

### Data consistency

The data are sent in a consistent state.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## X_ABORT: Abort an existing connection to a communication partner outside the local S7 station (S7-300, S7-400)

### Description

With the "X_ABORT" instruction, you abort a connection that was established with an "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" or "[X_PUT](#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction to a communication partner that is outside the local S7 station.

- If the job belonging to "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" or "[X_PUT](#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" is completed (BUSY=0), the connection resources used at both ends are released again after the "X_ABORT" instruction is called.
- If the job belonging to "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" or "[X_PUT](#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" is not yet completed (BUSY=1), you will need to call the relevant instruction again with REQ=0 and CONT=0 after the connection has aborted and then wait for BUSY=0. Only then are all the connection resources released again.

You can only call "X_ABORT" at the end that is executing "[X_SEND](#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_PUT](#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" or "[X_GET](#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)". The connection abort is activated by calling the instruction with REQ=1.

### Parameters

The following table shows the parameters of the "X_ABORT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter "request to activate"  See also: [Common parameters of instructions for S7 basic communication](Communication%20%28S7-300%2C%20S7-400%29.md#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400) |
| DEST_ID | Input | WORD | I, Q, M, D, L or constant | Addressing parameter "destination ID". It contains the MPI address of the communication partner. You have configured this. |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains the corresponding error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The connection abort is not yet completed. - BUSY = 0: The connection abort is completed. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Change to STOP mode

If the CPU changes to STOP mode, the connection abort started with "X_ABORT" will be completed.

### Transition of communication partner to STOP mode

If the CPU of the communication partner changes to STOP mode, this does not affect the connection abort with "X_ABORT". The connection is aborted.

### Parameter RET_VAL

See also:

- [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)
- [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

---

**See also**

[Difference between synchronous and asynchronous instructions (S7-300, S7-400)](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

---
title: "Communication (S7-300, S7-400)"
package: ProgTecComMain34enUS
topics: 6
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communication (S7-300, S7-400)

This section contains information on the following topics:

- [Common parameter and error information (S7-300, S7-400)](#common-parameter-and-error-information-s7-300-s7-400)
- [S7 communication (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#s7-communication-s7-300-s7-400)
- [Open User Communication (S7-300, S7-400)](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#open-user-communication-s7-300-s7-400)
- [Web server (S7-300, S7-400)](Web%20server%20%28S7-300%2C%20S7-400%29.md#web-server-s7-300-s7-400)
- [Additional communication (S7-300, S7-400)](#additional-communication-s7-300-s7-400)
- [Communications processor (S7-300, S7-400)](#communications-processor-s7-300-s7-400)
- [300C functions (S7-300, S7-400)](300C%20functions%20%28S7-300%2C%20S7-400%29.md#300c-functions-s7-300-s7-400)
- [Communication with iSlave / iDevice (S7-300, S7-400)](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#communication-with-islave-idevice-s7-300-s7-400)
- [PROFINET CBA (S7-300, S7-400)](PROFINET%20CBA%20%28S7-300%2C%20S7-400%29.md#profinet-cba-s7-300-s7-400)
- [MPI communication (S7-300, S7-400)](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#mpi-communication-s7-300-s7-400)
- [TeleService (S7-300, S7-400)](TeleService%20%28S7-300%2C%20S7-400%29.md#teleservice-s7-300-s7-400)
- Failsafe HMI Mobile Panels (S7-300, S7-400)

## Common parameter and error information (S7-300, S7-400)

This section contains information on the following topics:

- [Common parameters of instructions for S7 basic communication (S7-300, S7-400)](#common-parameters-of-instructions-for-s7-basic-communication-s7-300-s7-400)
- [Error information of communication instructions for non-configured S7 connections (S7-300, S7-400)](#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400)

### Common parameters of instructions for S7 basic communication (S7-300, S7-400)

#### REQ parameter

The REQ input parameter (request to activate) is a level-triggered control parameter. It is used to trigger the job (the data transfer or the connection termination):

- If you call the instruction for a job that is not currently active, the job is started with REQ = 1. If at the time of the first call of an instruction there is still no connection to the communication partner, then the connection will be established before starting the data transmission.
- If you have initiated a job and it is not yet completed when you call the instruction again for the same job, REQ is not evaluated by the instruction.

#### Parameters REQ_ID (only "X_SEND" and "X_RCV")

The input parameter REQ_ID is used to identify your send data. It is passed by the operating system of the sending CPU to the "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction of the CPU of the communication partner.

You require the REQ_ID parameter at the receiving end

- if you call several "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instructions with different REQ_ID parameters on one send CPU and transfer the data to a communication partner.
- if you use the "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instruction to send data to one communication partner from several send CPUs.

By evaluating REQ_ID, you can save the received data in different memory areas.

#### Parameters RET_VAL and BUSY

The instructions for S7 basic communication asynchronous, in other words, the processing of a job extends over more than one call. The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

#### CONT parameter

The CONT input parameter (continue) is a control parameter. Using this parameter, you decide whether or not a connection to the communication partner remains established after the job has completed.

- If you select CONT=0 at the first call, the connection is terminated again after the data transfer is completed. The connection is then available again for data exchange with a new communication partner.

  This method ensures that connection resources are only occupied when they are actually in use.
- If you select CONT=1 at the first call, the connection remains established after the completion of the data transfer.

  This method is, for example, useful when you exchange data cyclically between two stations.

  > **Note**
  >
  > You can also use "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" or "[I_ABORT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" to explicitly abort a connection established with CONT=1.

### Error information of communication instructions for non-configured S7 connections (S7-300, S7-400)

#### Display

You can classify the "real" error information for the instructions "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)", "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)", and "[I_ABORT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" specified in the following table, as follows:

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 809x | Error on the CPU on which the instruction is running |
| 80Ax | Permanent communication error |
| 80Bx | Error on the communication partner |
| 80Cx | Temporary error |

The following table contains specific error information for the instructions.

| Error code  (W#16#...) | Explanation (general) | Explanation (instruction-specific) |
| --- | --- | --- |
| 0000 | Execution completed without errors. | "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_ABORT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)": REQ=1, and the specified connection is not established. |
| "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)": EN_DT=1 and RD=NIL |  |  |
| 00xy | - | "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" when NDA=1 and RD&lt;&gt;NIL: RET_VAL contains the length of the received data block (with EN_DT=0) or the data block copied to RD (with EN_DT=1). |
| "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)": RET_VAL contains the length of the received block of data. |  |  |
| "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)": RET_VAL contains the length of the received block of data. |  |  |
| 7000 | - | "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)", "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" and "[I_ABORT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)": Call with REQ=0 (call without processing), BUSY has the value "0", no data transfer active. |
| "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)": EN_DT=0/1 and NDA=0 |  |  |
| 7001 | First call with REQ=1: Data transfer was triggered; BUSY has the value "1". | - |
| 7002 | Intermediate call (REQ irrelevant): Data transfer is already active; BUSY has the value "1". | "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_ABORT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_abort-abort-an-existing-connection-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)": Intermediate call with REQ=1 |
| 8090 | Specified destination address of the communication partner is invalid, for example:  - Wrong IOID - Wrong base address exists - Wrong MPI address (&gt; 126) | - |
| 8092 | Error in SD or RD, for example: addressing of the local data area is not permitted. | "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", for example  - illegal length for SD - SD=NIL is illegal |
| "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", for example  - More data was received than can fit in the area specified by RD. - RD is of the data type BOOL, the received data is, however, longer than one byte. |  |  |
| "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)", for example  - illegal length for RD - The length or the data type of RD does not match the received data. - RD=NIL is illegal. |  |  |
| "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)", for example  - illegal length for SD - SD=NIL is illegal |  |  |
| 8095 | The block is already being executed in a lower priority class. |  |
| 80A0 | Error in the received acknowledgment | "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)":  The data type specified in the SD of the sending CPU is not supported by the communication partner. |
| 80A1 | Communications problems: Instruction called after existing connection was canceled | "[AS_DIAL](TeleService%20%28S7-300%2C%20S7-400%29.md#description-of-as_dial-s7-300-s7-400)":  - The processing of a communication instruction was rejected by the local TS Adapter because no remote connection has been set up by "AS_DIAL". - The remote connection to the remote TS Adapter was aborted during the processing of the communication instruction. |
| 80B0 | Object is not reachable, for example, DB not loaded | Possible for "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" |
| 80B1 | Error in the ANY pointer. The length of the data area to be transferred is incorrect. | - |
| 80B2 | Hardware error: module does not exist  - The configured slot is not occupied. - Actual module type does not match expected type - Distributed I/O is not available. - No entry for the module in the corresponding SDB. | Possible for "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)". |
| 80B3 | Data may either only be read or only written, for example, write-protected DB | Possible for "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)". |
| 80B4 | Data type error in the ANY pointer, or ARRAY of the specified data type not permitted. | "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)": The data type specified in VAR_ADDR is not supported by the communication partner. |
| 80B5 | Execution rejected due to illegal mode | Possible for "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)".  With "[AS_DIAL](TeleService%20%28S7-300%2C%20S7-400%29.md#description-of-as_dial-s7-300-s7-400)":  - The processing of a communication instruction was rejected by local TS Adapter because the "DIAL" function of "AS_DIAL" is not yet completed. - The DIAL function of "AS_DIAL" was requested even though a remote connection is already set up for AS-AS remote coupling. |
| 80B6 | The received acknowledgment contains an unknown error code. | - |
| 80B7 | Data type and/or length of the transferred data does not fit in the area on the partner CPU to which it should be written. | Possible for "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_PUT](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_put-write-data-to-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" |
| 80B8 | - | "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)": "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" of the communication partner rejected the data acceptance (RD=NIL). |
| 80B9 | - | "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)": The block of data was identified by the communication partner (calling "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" with EN_DT=0), it has not yet been entered in the user program because the partner is in STOP mode. |
| 80BA | The response of the communication partner does not fit in the communication frame. | - |
| 80C0 | The specified connection is being used by another job. | - |
| 80C1 | Lack of resources on the CPU on which the instruction is executed, for example:  - The maximum number of  different send jobs is already being executed on the module. - The connection resource is in use, for example, receiving data. | - |
| 80C2 | Temporary lack of resources on the communication partner, for example:  - The communication partner is currently processing the maximum number of jobs. - The required resources (memory, etc.) are being used. - Not enough work memory. (Compress memory). | With "[AS_DIAL](TeleService%20%28S7-300%2C%20S7-400%29.md#description-of-as_dial-s7-300-s7-400)":  - Temporary lack of resources on the remote CPU. - The remote CPU with the MPI address is not available or does not exist. |
| 80C3 | Error in establishing a connection, for example:  - The local S7 station is not attached to the MPI subnet. - You have addressed your own station on the MPI subnet. - The communication partner is no longer reachable. - Temporary lack of resources on the communication partner | - |

## Additional communication (S7-300, S7-400)

This section contains information on the following topics:

- [MODBUS (TCP) (S7-300, S7-400)](MODBUS-TCP%20%28S7-300%2C%20S7-400%29.md#modbustcp-s7-300-s7-400)

## Communications processor (S7-300, S7-400)

This section contains information on the following topics:

- [Point-to-point (S7-300, S7-400)](Point-to-point%20%28S7-300%2C%20S7-400%29.md#point-to-point-s7-300-s7-400)
- [USS (S7-300, S7-400)](USS%20%28S7-300%2C%20S7-400%29.md#uss-s7-300-s7-400)
- [MODBUS (RTU) (S7-300, S7-400)](MODBUS%20%28RTU%29%20%28S7-300%2C%20S7-400%29.md#modbus-rtu-s7-300-s7-400)
- [PtP data link CP 340 (S7-300, S7-400)](PtP%20data%20link%20CP%20340%20%28S7-300%2C%20S7-400%29.md#ptp-data-link-cp-340-s7-300-s7-400)
- [PtP data link CP 341 (S7-300, S7-400)](PtP%20data%20link%20CP%20341%20%28S7-300%2C%20S7-400%29.md#ptp-data-link-cp-341-s7-300-s7-400)
- [PtP data link CP 440 (S7-300, S7-400)](PtP%20data%20link%20CP%20440%20%28S7-300%2C%20S7-400%29.md#ptp-data-link-cp-440-s7-300-s7-400)
- [PtP data link CP 441 (S7-300, S7-400)](PtP%20data%20link%20CP%20441%20%28S7-300%2C%20S7-400%29.md#ptp-data-link-cp-441-s7-300-s7-400)
- [Modbus slave (RTU) (S7-300, S7-400)](Modbus%20slave%20%28RTU%29%20%28S7-300%2C%20S7-400%29.md#modbus-slave-rtu-s7-300-s7-400)
- [ET 200S serial interface (S7-300, S7-400)](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#et-200s-serial-interface-s7-300-s7-400)
- [MODBUS/TCP CP (S7-300, S7-400)](MODBUS-TCP%20CP%20%28S7-300%2C%20S7-400%29.md#modbustcp-cp-s7-300-s7-400)
- [SIMATIC NET CPs (S7-300, S7-400)](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#simatic-net-cps-s7-300-s7-400)

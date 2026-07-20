---
title: "TeleService (S7-300, S7-400)"
package: ProgInstTeleServ34enUS
topics: 25
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TeleService (S7-300, S7-400)

This section contains information on the following topics:

- [PG_DIAL: Establish remote connection to programming device/PC (S7-300, S7-400)](#pg_dial-establish-remote-connection-to-programming-devicepc-s7-300-s7-400)
- [AS_DIAL: Establish remote connection to AS (S7-300, S7-400)](#as_dial-establish-remote-connection-to-as-s7-300-s7-400)
- [SMS_SEND: Send text (SMS) message (S7-300, S7-400)](#sms_send-send-text-sms-message-s7-300-s7-400)
- [AS_MAIL: Transfer email (S7-300, S7-400)](#as_mail-transfer-email-s7-300-s7-400)

## PG_DIAL: Establish remote connection to programming device/PC (S7-300, S7-400)

This section contains information on the following topics:

- [Description of PG_DIAL (S7-300, S7-400)](#description-of-pg_dial-s7-300-s7-400)
- [PHONE_NO parameter (S7-300, S7-400)](#phone_no-parameter-s7-300-s7-400)
- [EVENT_ID parameter (S7-300, S7-400)](#event_id-parameter-s7-300-s7-400)
- [BUSY parameter (S7-300, S7-400)](#busy-parameter-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

### Description of PG_DIAL (S7-300, S7-400)

#### Description

The "PG_DIAL" instruction transfers a telephone number and an event ID to a TS Adapter. Using the specified telephone number, the TS Adapter establishes a remote connection to a programming device/PC. The event ID is transferred to the programming device/PC and passed to a waiting application.

If the event ID ([EVENT_ID](#event_id-parameter-s7-300-s7-400) parameter) was successfully transferred to the application, the TS Adapter receives an acknowledgement that is passed to the "PG_DIAL" instruction. The processing of "PG_DIAL" then is terminated and the status transferred to the caller of "PG_DIAL". The application on the programming device/PC is responsible for terminating the remote connection.

If an error occurs during the processing that leads to the processing aborting, the error code is transferred to the caller of "PG_DIAL". Any established remote connection will be terminated by the TS Adapter.

#### Calling "PG_DIAL"

You can call the "PG_DIAL" instruction in the cycle or a time-controlled program. An instance DB must be specified when "PG_DIAL" is called.

"PG_DIAL" must be called more than once to process a block function. This means that calling "PG_DIAL" in a "queue" is pointless. The end of the block function is indicated by BUSY = 0.

#### Communication connection abort

If the CPU changes to STOP mode while "PG_DIAL" is active, the communication connection to the TS Adapter is aborted.

The communication connection to the TS Adapter is also lost if serious communication problems arise on the MPI bus or, for example, the CPU is switched off. In these cases the telephone number and event ID that were already transferred to the TS Adapter and not discarded by the adapter. The TS Adapter establishes the remote connection to the PG/PC and transfers the event ID. However, the acknowledgement that is transferred from the programming device/PC to the TS Adapter, is discarded by the TS Adapter.

If a user program attempts to establish a remote connection while the TS Adapter is in the status described above, "PG_DIAL" is terminated with the return value W#16#B10A. The user program can later repeat the establishment of a remote connection. You also receive the return value W#16#B10A, if various CPUs attempt to establish a remote connection at the same time via the same TS Adapter.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing user programs**  You can change the parts of your user program that directly affect calls of "PG_DIAL" only when the CPU is in STOP mode. This relates, in particular, to deleting and replacing program blocks that contain "PG_DIAL" calls. Ignoring this restriction can tie up connection resources. The status of the automation system relating to the communication instructions for non-configured S7 connections may become undefined. A warm or cold restart of the CPU is required after the changes are transferred. |  |

#### Data consistency

The input parameters of the function block are copied to in internal buffer when "PG_DIAL" is first called. Do not change this data before the first call is completed (return value W#16#7001), otherwise inconsistent data could be transferred.

#### Parameters

The following table shows the parameters of the "PG_DIAL" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MPI_TS_ADAPTER | Input | INT | I, Q, M, D, L or constant | MPI address of the TS Adapter |
| [PHONE_NO](#phone_no-parameter-s7-300-s7-400) | Input | ANY | D | Reference to a data string with a maximum length of 31 characters |
| [EVENT_ID](#event_id-parameter-s7-300-s7-400) | Input | ANY | I, Q, M, D | Reference to a byte array with a maximum length of 16 characters |
| [BUSY](#busy-parameter-s7-300-s7-400) | Output | BOOL | I, Q, M, D, L | - BUSY=1: The establishment of the remote connection is not yet completed. - BUSY=0: The processing of "PG_DIAL" was stopped. |
| [STATUS](#status-parameter-s7-300-s7-400) | Output | INT | I, Q, M, D, L | Return value of "PG_DIAL" |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Virtual block parameters EN and ENO and the BR bit

The virtual block parameters EN and ENO occur only when "PG_DIAL" is included in the LAD or FBD representation of the STEP 7 editor. They are closely linked with the BR bit (binary result) of the status word.

- **Input parameters** 
  **EN**

  The status of the result of logic operation (RLO) is saved to the BR bit during the block call.
- **Output parameters** 
  **ENO**

  If "PG_DIAL" is processed error-free, the status of the BR bit that existed when the block was called is restored again at the end of the block call.

  If an error message is output via the output parameter STATUS, the BR bit is set to "0" immediately before exiting "PG_DIAL".

---

**See also**

[Establishing a connection from and to remote systens (PG-AS-remote coupling)](Establishing%20a%20remote%20connection%20with%20TeleService.md#establishing-a-connection-from-and-to-remote-systens-pg-as-remote-coupling)

### PHONE_NO parameter (S7-300, S7-400)

#### Description

The input parameter PHONE_NO specifies the telephone number to which a remote connection will be established. Enter the complete telephone number including country code, area code and subscriber number. The string is transferred unchanged to the modem. If you use characters that are not numerals, make sure that the modem used supports these characters.

The TS Adapter uses the following parameter values to establish a remote connection:

- Location: Dial procedure, access code
- Call settings: "Wait for dial tone before dialing", "Number of redial attempts" and "Redial after"

### EVENT_ID parameter (S7-300, S7-400)

#### Description

The EVENT_ID input parameter specifies the event ID. This is transferred transparently from the user program of the automation system to the user program on the PG/PC by "PG_DIAL", the TS Adapter and the TeleService application on the PG/PC. You can structure the event ID as required and transfer any information from the automation system to the PG/PC.

If a length less than 16 is transferred when "PG_DIAL" is called, the remaining bytes of the array are padded with B#16#00.

### BUSY parameter (S7-300, S7-400)

#### Description

"PG_DIAL" is an asynchronous instruction, in other words, its processing extends over multiple calls.

- If the BUSY output parameter = 1, the internal status of "PG_DIAL" is output in the output parameter [STATUS](#status-parameter-s7-300-s7-400).
- When processing is completed, this is indicated by the output parameter BUSY = 0. The [STATUS](#status-parameter-s7-300-s7-400) output parameter then indicates whether the job was completed error-free (STATUS = W#16#0000) or with errors.

### STATUS parameter (S7-300, S7-400)

#### Description

The return values of "PG_DIAL" can be classified as follows:

- W#16#0000: "PG_DIAL" was completed successfully
- W#16#7xxx: Status of "PG_DIAL"
- W#16#8xxx: An error was reported during the internal call of a communication instruction or the "BLKMOV" instruction
- W#16#9xxx: Parameter error when calling "PG_DIAL"
- W#16#Bxxx: An error was reported by the TS Adapter

The following tables shows the return values of "PG_DIAL" except for error codes of the communication instructions used.

| Return value  (W#16#...) | Explanation | Notes |
| --- | --- | --- |
| 0000 | The processing of "PG_DIAL" was completed without errors. |  |
| 7000 | "PG_DIAL" was reset (the communication with the TS Adapter was terminated in the meantime). | Call "PG_DIAL" again. |
| 7001 | "PG_DIAL" is active (first call, BUSY = 1). The function has just been started. |  |
| 7002 | "PG_DIAL" is active (subsequent call, BUSY = 1). The processing of the function is not yet completed. |  |
| 8xxx or 8zxx | The processing of "PG_DIAL" was completed with an error code of the internally called communication instructions.  If the error message originates from the "BLKMOV" instruction, the meaning is as follows  - z = 2: Error copying the PHONE_NO parameter to the internal buffer - z = 3: Error copying the EVENT_ID parameter to the internal buffer | You will find more detailed information in the error information of the communication instructions:   [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400) |
| 9001 | Length of PHONE_NO = 0 or &gt; 31 | The telephone number must consist of at least 1 character and not more than 31 characters. |
| 9002 | Length of EVENT_ID = 0 or &gt; 16 | The event ID must consist of at least 1 character and not more than 16 characters. |
| B000 | It was possible to establish the remote connection to the PG/PC. With TeleService, however, no program logged on for the transferred event ID. |  |
| B10A | A job is already stored on the TS Adapter and this job is currently being processed by the TS Adapter. | Call "PG_DIAL" again. |
| B10B | After the establishment of the remote connection, the connection was terminated by the partner before the event ID could be transferred. | Call "PG_DIAL" again. |
| B206 | It was not possible to establish the remote connection to the PG/PC. | Check the parameter assignment of the modem in the TS Adapter (local and remote). |
| B302 | The TS Adapter is directly connected to a PG/PC (direct connection). | Terminate the communication on the direct connection. |
| B305 | A remote connection to a PG/PC is still established. | Call "PG_DIAL" again later. |

## AS_DIAL: Establish remote connection to AS (S7-300, S7-400)

This section contains information on the following topics:

- [Description of AS_DIAL (S7-300, S7-400)](#description-of-as_dial-s7-300-s7-400)
- [PHONE_NO parameter (S7-300, S7-400)](#phone_no-parameter-s7-300-s7-400-1)
- [Parameter REQ_DIAL (S7-300, S7-400)](#parameter-req_dial-s7-300-s7-400)
- [REQ_HANGUP parameter (S7-300, S7-400)](#req_hangup-parameter-s7-300-s7-400)
- [BUSY parameter (S7-300, S7-400)](#busy-parameter-s7-300-s7-400-1)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400-1)

### Description of AS_DIAL (S7-300, S7-400)

#### Definition

Local and remote automation system

- Local: The S7 automation system from which the initiative to establish the remote connection originates is described as local.
- Remote: The S7 automation system to which the remote connection will be established is described as remote.

#### Description

With the "AS_DIAL" instruction, you can establish a remote connection from a local S7 automation system to a remote S7 automation system and then exchange process data. You can use the "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" instructions to exchange process data.

The "AS_DIAL" instruction has two functions:

- **Function** 
  **DIAL**
  **:** Establishing a remote connection to a remote TS Adapter. You use the [REQ_DIAL](#parameter-req_dial-s7-300-s7-400) input parameter to request this function.
- **Function** 
  **HANGUP**
  **:** Terminating an existing remote connection to a remote TS Adapter. You use the [REQ_HANGUP](#req_hangup-parameter-s7-300-s7-400) input parameter to request this function.

Only one of the functions can be active at one time. The DIAL function is terminated by the HANGUP function request.

If an error occurs during the processing that leads to the processing aborting, the error code is transferred to the caller of "AS_DIAL". Any established remote connection will be terminated by the TS Adapter.

#### Calling "AS_DIAL"

You can call "AS_DIAL" in the cycle or in a time-controlled program. If you call "AS_DIAL" in different tasks, make sure that the calls are interlocked.

- An instance DB must be specified when "AS_DIAL" is called. Always use the same instance for a remote connection.

  **Exception:** If the local CPU communicates via multiple local TS Adapters, assign a separate instance to each TS Adapter.
- "AS_DIAL" must be called more than once to process a block function. This means that calling "AS_DIAL" in a "queue" is pointless. The end of the block function is indicated by BUSY = 0.
- To communicate with the TS Adapter, "AS_DIAL" also uses communication instructions for non-configured S7 connections.

  Therefore, make sure that no communication instructions for non-configured S7 connections ("[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)") that were started with DEST_ID = "MPI address of the local TS Adapter" are active when the remote connection is being established or terminated by "AS_DIAL".

#### Parameters

The following table shows the parameters of the "AS_DIAL" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ADDR_TS_ ADAPTER | Input | INT | I, Q, M, D, L or constant | Input parameters of the DIAL and HANGUP functions:   MPI address of the TS Adapter on the local MPI network |
| [PHONE_NO](#phone_no-parameter-s7-300-s7-400-1) | Input | ANY | D | Input parameters of the DIAL function:  Telephone number of the modem of the remote automation system (max. 31 characters) |
| LOGIN | Input | ANY | D | Input parameters of the DIAL function:  User name for authorization on the remote TS Adapter (max. 8 characters) |
| PASSWORD | Input | ANY | D | Input parameters of the DIAL function: Password for authorization on the remote TS Adapter (max. 8 characters) |
| ADDR_CPU | Input | INT | I, Q, M, D, L or constant | Input parameters of the DIAL function:   MPI address of the CPU on the remote MPI network to which the connection is to be established. |
| [REQ_DIAL](#parameter-req_dial-s7-300-s7-400) | Input | BOOL | I, Q, M, D | Input parameters for requesting the DIAL function:   Establishing a remote connection to a remote TS Adapter |
| [REQ_HANGUP](#req_hangup-parameter-s7-300-s7-400) | Input | BOOL | I, Q, M, D | Input parameters for requesting the HANGUP function:   Terminating an existing remote connection to a remote TS Adapter |
| [STATUS](#status-parameter-s7-300-s7-400-1) | Output | INT | I, Q, M, D, L | Return value of "AS_DIAL" |
| [BUSY](#busy-parameter-s7-300-s7-400-1) | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The DIAL or HANGUP function is still active; in other words, establishment/termination of the remote connection is not yet completed. - BUSY=0: Processing of the "AS_DIAL" instruction is completed. No function is still active. |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Virtual block parameters EN and ENO and the BR bit

The virtual block parameters EN and ENO occur only with the integration of "AS_DIAL" in the LAD or FBD representation.

- Input parameter EN: The status of the result of logic operation (RLO) is saved to the BR bit during the block call.
- Output parameter ENO:

  If "AS_DIAL" is processed error-free, the status of the BR bit that existed when the block was called is restored again at the end of the block call.

  If an error message is output via the [STATUS](#status-parameter-s7-300-s7-400-1) output parameter, the BR bit is set to "0" immediately before exiting "AS_DIAL".

---

**See also**

[Data exchange between remote systems (AS-AS-remote coupling)](Establishing%20a%20remote%20connection%20with%20TeleService.md#data-exchange-between-remote-systems-as-as-remote-coupling)

### PHONE_NO parameter (S7-300, S7-400)

#### Description

The input parameter PHONE_NO specifies the telephone number to which a remote connection will be established. Enter the complete telephone number including country code, area code and subscriber number. The string is transferred unchanged to the modem. If you use characters that are not numerals, make sure that the modem used supports these characters.

The TS Adapter uses the following parameter values to establish a remote connection:

- Location: Dial procedure, access code
- Call settings: "Wait for dial tone before dialing", "Number of redial attempts" and "Redial after"

### Parameter REQ_DIAL (S7-300, S7-400)

#### Description

The DIAL function can only be requested if [BUSY](#busy-parameter-s7-300-s7-400-1) = 0 was reported at the last of "AS_DIAL" call. With the REQ_DIAL input parameter, you start the DIAL function. The REQ_DIAL input parameter is level-triggered.

REQ_DIAL triggers the DIAL function of the "AS_DIAL" instruction. The "AS_DIAL" instruction checks the parameters for plausibility and transfers these to the local TS Adapter.

If an error is detected during the processing of the DIAL function, this causes processing of the DIAL function to be aborted. "AS_DIAL" automatically executes the [HANGUP](#req_hangup-parameter-s7-300-s7-400) function and then outputs the error message in the [STATUS](#status-parameter-s7-300-s7-400-1) return value.

Result: With [BUSY](#busy-parameter-s7-300-s7-400-1) = 0, the result of the connection establishment is displayed in the [STATUS](#status-parameter-s7-300-s7-400-1) return value.

### REQ_HANGUP parameter (S7-300, S7-400)

#### Description

With the REQ_HANGUP input parameter, you start the HANGUP function. The HANGUP function terminates a remote connection to the remote TS Adapter, which was established earlier by the [DIAL](#parameter-req_dial-s7-300-s7-400) function.

The REQ_HANGUP input parameter is level-triggered. The HANGUP function can also be started if the [DIAL](#parameter-req_dial-s7-300-s7-400) function was already started.

The end of the HANGUP function is notified by the output parameter [BUSY](#busy-parameter-s7-300-s7-400-1) = 0. The [STATUS](#status-parameter-s7-300-s7-400-1) output parameter then supplies the result of the function processing.

| Value | Meaning |
| --- | --- |
| W#16#0000 | The remote connection was terminated normally by the HANGUP function. |
| W#16#3007 | The remote connection was terminated by the local TS Adapter because an error occurred. |
| W#16#3008 | The remote connection has broken down spontaneously or the remote TS Adapter has hung up. |
|  |  |

### BUSY parameter (S7-300, S7-400)

#### Description

"AS_DIAL" is an asynchronous instruction, in other words, its processing extends over multiple calls.

- If BUSY = 1, the internal [STATUS](#status-parameter-s7-300-s7-400-1) of "AS_DIAL" is output in the [STATUS](#status-parameter-s7-300-s7-400-1) output parameter. At least one further "AS_DIAL" call is necessary.
- If BUSY = 0, the processing is completed. The [STATUS](#status-parameter-s7-300-s7-400-1) output parameter then indicates whether the job was completed error-free or with errors.

### STATUS parameter (S7-300, S7-400)

#### Description

The return values of "AS_DIAL" can be classified as follows:

- W#16#0000: "AS_DIAL" was completed without errors
- W#16#3xxx: Most recent status of remote connection in the TS Adapter
- W#16#7xxx: Status of "AS_DIAL"
- W#16#8xxx: An error was reported during the internal call of a communication instruction ("[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)").
- W#16#9xxx: Parameter error when calling "AS_DIAL"
- W#16#Bxxx: Error during connection establishment

The following table shows the return values of "AS_DIAL" except for error codes of the communication instructions used:

| Return value  (W#16#...) | Explanation | Notes |
| --- | --- | --- |
| 0000 | No function is active.  The processing of "AS_DIAL" was completed without errors. | This message is only displayed once after successful completion of the relevant function. |
| 3007 | The local TS Adapter has hung up. | Is only displayed by the HANGUP function. |
| 3008 | The remote connection has broken down spontaneously or the remote TS Adapter has hung up. | Is only displayed by the HANGUP function. |
| 7000 | No function is active. | No function was processed or requested via the input parameters. |
| 7001 | DIAL function is active (first call, BUSY = 1). The function has just been started. | The REQ_DIAL input parameter is not evaluated until the end of the (BUSY = 0) function. |
| 7002 | DIAL function is active (subsequent call, BUSY = 1). The processing of the function is not yet completed. | The REQ_DIAL input parameter is not evaluated until the end of the (BUSY = 0) function. |
| 7701 | The HANGUP function is active (first call). The function has just been started. | The input parameters REQ_DIAL and REQ_HANGUP are not evaluated until the end of the (BUSY = 0) function. |
| 7702 | HANGUP function is active (subsequent call). The processing of the function is not yet completed. | The input parameters REQ_DIAL and REQ_HANGUP are not evaluated until the end of the (BUSY = 0) function. |
| 8xxx | Error message: The processing of the active block function was terminated because of an error message (RET_VAL &lt; 0) of an instruction called within the block. | You will find more detailed information in the error information of the communication instructions:   [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400). |
| 9001 | Length of PHONE_NO = 0 or &gt; 31 | The telephone number must consist of at least 1 character and not more than 31 characters. |
| 9003 | Length of LOGIN &gt; 8 | The user name for authorization on the remote TS Adapter must not exceed 8 characters. |
| 9004 | Length of PASSWORD &gt; 8 | The password for authorization on the remote TS Adapter must not exceed 8 characters. |
| B100 | TS Adapter cannot currently establish a connection. | The TS Adapter cannot currently call a connection to the modem. Call "AS_DIAL" again. |
| B10A | An event ID of a "PG_DIAL" function is already stored in the TS Adapter or an "AS_DIAL" function is active that is still to be transferred. | Call "AS_DIAL" again. |
| B10B | The remote connection was terminated again after successful establishment of the remote connection. | Call "AS_DIAL" again. |
| B206 | It was not possible to establish the remote connection to the TS Adapter. | Check the parameter assignment of the modem in the TS Adapter (local and remote). |
| B20A | The remote TS Adapter type does not support AS-AS remote coupling. | Use a TS Adapter that supports the AS-AS remote coupling. |
| B20B | The "AS_DIAL" instruction and the version of the TS Adapter are incompatible. | Use a TS Adapter that supports the AS-AS remote coupling. |
| B20C | The remote TS Adapter cannot join the MPI network.   Cause: Network parameter error | Check the parameter assignment of the network parameters in the remote TS Adapter. |
| B20D | The version of the remote TS Adapter does not support an AS-AS remote coupling. | Use a TS Adapter that supports the AS-AS remote coupling. |
| B20E | Data transfer to the remote TS Adapter was aborted.  Cause: Transmission error | Call "AS_DIAL" again. |
| B20F | The remote TS Adapter has not called back. | Check the access protection parameter settings (callback number) and modem in the remote TS Adapter. |
| B210 | The data transmission to the remote TS Adapter is disrupted.  Cause: Timeout | Call "AS_DIAL" again. |
| B252 | The remote TS Adapter rejects the job due to lack of authorization. | You have not specified a user name and password for the "AS_DIAL" call. |
| B253 | The remote TS Adapter rejects the authorization.  Cause: Unknown user name | Check the call parameters of "AS_DIAL" in your user program. |
| B254 | The remote TS Adapter rejects the authorization.  Cause: Incorrect password | Check the call parameters of "AS_DIAL" in your user program. |
| B302 | The TS Adapter is directly connected to a PG/PC (direct connection). | Terminate the communication on the direct connection. |
| B305 | A remote connection to a PG/PC is still established by the local TS Adapter. | Call "AS_DIAL" again later. |

## SMS_SEND: Send text (SMS) message (S7-300, S7-400)

This section contains information on the following topics:

- [Description of SMS_SEND (S7-300, S7-400)](#description-of-sms_send-s7-300-s7-400)
- [PHONE_NO parameter (S7-300, S7-400)](#phone_no-parameter-s7-300-s7-400-2)
- [Parameter SCENTER_NO (S7-300, S7-400)](#parameter-scenter_no-s7-300-s7-400)
- [MESSAGE parameter (S7-300, S7-400)](#message-parameter-s7-300-s7-400)
- [BUSY parameter (S7-300, S7-400)](#busy-parameter-s7-300-s7-400-2)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400-2)

### Description of SMS_SEND (S7-300, S7-400)

#### Description

The "SMS_SEND" instruction transfers a telephone number, a service center number and an SMS message to a TS Adapter. The TS Adapter transfers this data via GSM commands to a wireless modem.

After the SMS message has been sent, the TS Adapter receives an acknowledgement that is forwarded to the "SMS_SEND" instruction. The processing of "SMS_SEND" is then terminated and the status communicated to the caller. This status is only an acknowledgement that the SMS has been sent, not a confirmation of receipt.

If an error occurs during the processing that leads to the processing aborting, the error code is transferred to the caller of "SMS_SEND".

#### Calling "SMS_SEND"

You can call the "SMS_SEND" instruction in the cycle or a time-controlled program.

An instance DB must be specified when "SMS_SEND" is called.

"SMS_SEND" must be called more than once to process a block function. This means that calling "SMS_SEND" in a "queue" is pointless. The end of the block function is indicated by BUSY = 0.

#### Communication connection abort

If the CPU changes to STOP mode while "SMS_SEND" is active, the communication connection to the TS Adapter is aborted. The communication connection to the TS Adapter is also lost if serious communication problems arise on the MPI bus or, for example, the CPU is switched off.

In these cases the telephone number, service center number and SMS message that were already transferred to the TS adapter are not discarded by the TS adapter. The TS Adapter transfers the data to the wireless modem. However, the acknowledgement that is transferred from the wireless modem to the TS Adapter, is discarded by the TS Adapter.

If a user program attempts to send an SMS to the CPU while the TS Adapter is in the status described above, "SMS_SEND" is terminated with the return value W#16#B10A. The user program can later repeat the sending of an SMS. You also receive the return value W#16#B10A, if different CPUs attempt to send an SMS at the same time via the same TS Adapter.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing the STEP 7 user program**  You can only change the parts of your STEP 7 user program that directly affect calls of "SMS_SEND" when the CPU is in STOP mode. This relates, in particular, to deleting and replacing program blocks that contain "SMS_SEND" calls. Ignoring this restriction can tie up connection resources. The automation system can change to an undefined status for the communication instructions for non-configured S7 connections ("[X_PUT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_put-write-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_SEND](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_send-send-data-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_RCV](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_rcv-receive-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)", "[X_ABORT](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_abort-abort-an-existing-connection-to-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)").  A warm or cold restart of the CPU is required after the changes are transferred. |  |

#### Data consistency

The input parameters of the function block are copied to in internal buffer when "SMS_SEND" is first called. Do not change this data before the first call is completed (return value W#16#7001), otherwise inconsistent data could be transferred.

#### Transfer of PIN to the wireless modem

If you use a SIM card on which the PIN check is enabled, the PIN must be transferred during the initialization phase of the wireless modem. This is possible using the init string of the TS Adapter, which you can set using TeleService. Set the init string as follows (example for PIN = 4711):

- AT+CPIN="4711";AT&amp;F.....

When power is restored, the TS Adapter sends the string "AT+CPIN="4711" once, along with the PIN for the SIM card used in the wireless modem, to the connected components. The wireless modem is then initialized with "AT&amp;F...".

**Caution:** An incorrect PIN is not reported during the initialization, but only when an SMS is sent via the feedback message of "SMS_SEND".

#### Sending a fax

By prefixing a special number of the network provider (for example, "99") before actual number, the SMS is converted by the network provider into a fax and sent to a fax machine. This is a service of the network provider, not a function of the TS Adapter.

The fax number is entered with the prefix of the network provider in the PHONE_NO parameter.

Example of a network with the fax number 07214711:

- PHONE_NO = '9907214711'

#### Sending an e-mail

By dialing a special number of the network provider (for example, "8000") and appending an e-mail address before the SMS message, the SMS can be sent to an e-mail address. This is a service of the network provider, not a function of the TS Adapter.

You enter the corresponding number in the [PHONE_NO](#phone_no-parameter-s7-300-s7-400-2) parameter.

In the SMS message, the e-mail address prefixes the actual text of the message and is delimited from this by a separator. This shortens the maximum length of the SMS payload by the length of the e-mail address + separator. Separators are, for example, blanks (" ") or colons (":").

Some service providers demand a "*" instead of the "@" character.

Example:

- The text 'CPU in STOP' is to be sent to the e-mail address "Surname*provider.com".
- PHONE_NO = 8000
- MESSAGE = Surname*provider.comCPU in STOP

#### Parameters

The following table shows the parameters of the "SMS_SEND" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| MPI_TS_ ADAPTER | Input | INT | I, Q, M, D, L or constant | MPI address of the TS Adapter |
| [PHONE_NO](#phone_no-parameter-s7-300-s7-400-2) | Input | ANY | D | Reference to a data string with a maximum length of 31 characters |
| [SCENTER_NO](#parameter-scenter_no-s7-300-s7-400) | Input | ANY | D | Reference to a data string with a maximum length of 20 characters |
| [MESSAGE](#message-parameter-s7-300-s7-400) | Input | ANY | D | Reference to a data string with a maximum length of 160 characters |
| [BUSY](#busy-parameter-s7-300-s7-400-2) | Output | BOOL | I, Q, M, D, L | - BUSY=1: The sending of the SMS is not yet completed - BUSY=0: Processing of "SMS_SEND" was terminated |
| [STATUS](#status-parameter-s7-300-s7-400-2) | Output | INT | I, Q, M, D, L | Return value of "SMS_SEND" |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Virtual parameters EN and ENO and the BR bit

The virtual block parameters EN and ENO occur only with the integration of "SMS_SEND" in the LAD or FBD representation.

- Input parameter EN:

  The status of the result of logic operation (RLO) is saved to the BR bit during the block call.
- Output parameter ENO:

  If "SMS_SEND" is processed error-free, the status of the BR bit that existed when the block was called is restored again at the end of the block call.  
  If an error message is output via the output parameter STATUS, the BR bit is set to "0" immediately before exiting "SMS_SEND".

---

**See also**

[Send SMS from a system](Establishing%20a%20remote%20connection%20with%20TeleService.md#send-sms-from-a-system)

### PHONE_NO parameter (S7-300, S7-400)

#### Description

The input parameter PHONE_NO specifies the telephone number to which an SMS is to be sent. Enter the complete telephone number including country code, area code and subscriber number. The string is transferred unchanged to the wireless modem. If you use characters that are not numerals, make sure that the wireless modem used supports these characters.

### Parameter SCENTER_NO (S7-300, S7-400)

#### Description

The SCENTER_NO input parameter specifies the service center number to which the SMS will be sent. The string is transferred unchanged to the wireless modem.

### MESSAGE parameter (S7-300, S7-400)

#### Description

The MESSAGE input parameter specifies the SMS message. This is transferred using the "SMS_SEND" instruction, via the TS Adapter and the GSM wireless modem to the network provider.

### BUSY parameter (S7-300, S7-400)

#### Description

"SMS_SEND" is an asynchronous instruction, in other words, its processing extends over multiple calls.

- If the BUSY output parameter = 1, the internal status of "SMS_SEND" is output in the output parameter [STATUS](#status-parameter-s7-300-s7-400-2).
- When processing is completed, this is indicated by the output parameter BUSY = 0. The [STATUS](#status-parameter-s7-300-s7-400-2) output parameter then indicates whether the job was completed error-free (STATUS = W#16#0000) or with errors.

### STATUS parameter (S7-300, S7-400)

#### Description

The return values of "SMS_SEND" can be classified as follows:

- W#16#0000: "SMS_SEND" was ended successfully.
- W#16#7xxx: Status of "SMS_SEND"
- W#16#8xxx: when calling a communication instruction or the instruction "BLKMOV" an error was reported.
- W#16#9xxx: parameter error when calling "SMS_SEND"
- W#16#Bxxx: an error was reported by the TS adapter.
- W#16#Cxxx: an error was reported by the wireless modem.

The following table shows the return values of "SMS_SEND" except for error codes of the communication instructions used or the wireless modem.

| Return value  (W#16#...) | Explanation | Notes |
| --- | --- | --- |
| 0000 | The processing of "SMS_SEND" was completed without errors. |  |
| 7000 | "SMS_SEND" was reset (the communication with the TS adapter was terminated in the meantime). | Call "SMS_SEND" again. |
| 7001 | "SMS_SEND" is active (first call, BUSY = 1). The function has just been started. |  |
| 7002 | "SMS_SEND" is active (next call, BUSY = 1). The processing of the function is not yet completed. |  |
| 8xxx or  8zxx | Processing of "SMS_SEND" was completed with an error code of the communication instructions called internally or the "BLKMOV" instruction.  If the error message originates from the "BLKMOV" instruction, the meaning is as follows  - z = 2 : Error copying the parameter PHONE_NO to the internal buffer - z = 3 : Error copying the parameter SCENTER_NO to the internal buffer - z = 4 : Error copying the parameter MESSAGE to the internal buffer | For detailed information, refer to the description of the "BLKMOV" instruction and the error information of the communication instructions:   [Error information of communication instructions for non-configured S7 connections](Communication%20%28S7-300%2C%20S7-400%29.md#error-information-of-communication-instructions-for-non-configured-s7-connections-s7-300-s7-400) |
| 9001 | Length of PHONE_NO = 0 or &gt; 31 | The telephone number must consist of at least 1 character and not more than 31 characters. |
| 9002 | Length of SCENTER_NO = 0 or &gt; 20 | The service center number must consist of at least 1 character and not more than 20 characters. |
| 9003 | Length of MESSAGE = 0 or &gt; 160 | The SMS message must consist of at least 1 character and not more than 160 characters. |
| B10A | A job is already stored on the TS Adapter and this job is currently being processed by the TS Adapter. | Call "SMS_SEND" again. |
| B301 | A remote connection to a PG/PC is still established. | Call "SMS_SEND" again later. |
| B302 | The TS Adapter is directly connected to a PG/PC (direct connection). | Connect the TS adapter to a GSM wireless modem. |
| B303 | The TS Adapter is not connected to a wireless modem or a PG/PC. | Connect the TS adapter to a GSM wireless modem. |
| B304 | The interface to the wireless modem is not currently ready to send an SMS. | Call "SMS_SEND" again later. |
| B614 | The connected modem did not reply to the SMS-specific command within the monitoring period. | Check whether you have connected a GSM wireless modem.  Call "SMS_SEND" again later. |
| B615 | The TS Adapter has received an unspecific error message from the connected modem. | Check whether you have connected a GSM wireless modem. |
| Cxxx | The processing of "SMS_SEND" was terminated with an error code of the GSM modem.  xxx: Error number | For a list of the error numbers, refer to the your wireless modem manual or to the GSM standards GSM 04.11, GSM 03.40 and GSM 07.05.  Examples:  - C136 = No SIM card present in the GSM modem - C137 = PIN for GSM modem not correct (see transfer of the PIN to the wireless modem) - C001 = Wrong phone number for the service center |

## AS_MAIL: Transfer email (S7-300, S7-400)

This section contains information on the following topics:

- [Description of AS_MAIL (S7-300, S7-400)](#description-of-as_mail-s7-300-s7-400)
- [STATUS and SFC_STATUS parameters (S7-300, S7-400)](#status-and-sfc_status-parameters-s7-300-s7-400)
- [Example of "AS_MAIL" call (S7-300, S7-400)](#example-of-as_mail-call-s7-300-s7-400)

### Description of AS_MAIL (S7-300, S7-400)

#### Required instructions

The "AS_MAIL" instruction uses the Simple Mail Transfer Protocol (SMTP) to transfer an e-mail from a CPU to a mail server. "To run, "AS_MAIL" requires the following instructions:

- "[S_COMP: Compare character strings](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#s_comp-compare-character-strings-s7-300-s7-400)"
- "[FIND: Find characters in a character string](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#find-find-characters-in-a-character-string-s7-300-s7-400)"
- "[INSERT: Insert characters in a character string](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#insert-insert-characters-in-a-character-string-s7-300-s7-400)"
- "[LEFT: Read the left character of a character string](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#left-read-the-left-character-of-a-character-string-s7-300-s7-400)"
- "[LEN: Determine the length of a character string](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#len-determine-the-length-of-a-character-string-s7-300-s7-400)"
- "[RIGHT: Read the right characters of a character string](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#right-read-the-right-characters-of-a-character-string-s7-300-s7-400)"

#### Description

"AS_MAIL" is an asynchronous instruction, in other words, its processing extends over multiple calls. When you call the "AS_MAIL" instruction, you must specify an instance DB.

You initialize the block by a call with COM_RST = 1.

You start the sending of an e-mail with an edge change from "0" to "1" for the REQ parameter.

The job status is indicated by the output parameters BUSY , "DONE", "ERROR", "STATUS" and "SFC_STATUS". "SFC_STATUS" corresponds in this case to the "STATUS" output parameter of the called communication blocks or the "BLKMOV" instruction.

The output parameters DONE, ERROR, STATUS, and SFC_STATUS are each displayed for only one cycle if the status of the BUSY output parameter changes from "1" to "0".

The following table shows the relationship between BUSY, DONE, and ERROR. Using this table, you can determine the current status of the instruction "AS_MAIL" or when the sending of the e-mail is completed.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | Irrelevant | Irrelevant | The job is being processed. |
| 0 | 1 | 0 | Job successfully completed. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error can be found in the STATUS and SFC_STATUS parameters. |
| 0 | 0 | 0 | The "AS_MAIL" instruction was not assigned a (new) job. |
|  |  |  |  |

If the CPU changes to STOP mode while "AS_MAIL" is active, the communication connection to the mail server aborts. The communication connection to the mail server will also be lost if communication problems occur on the Industrial Ethernet bus. In this case, the transfer of the e-mail will be interrupted and it will not reach its recipient.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing user programs**  You can change the parts of your user program that directly affect calls of "AS_MAIL" only:  - when the CPU is in "STOP" mode or - when no mail is being sent (REQ = 0 and BUSY = 0).   This relates, in particular, to deleting and replacing program blocks that contain "AS_MAIL" calls or calls for the instance DB of "AS_MAIL".  Ignoring this restriction can tie up connection resources. The automation system can change to an undefined status for the TPC/IP communication functions via Industrial Ethernet.  After transferring the changes, run a warm or cold restart on the CPU or set the COM_RST parameter of the "AS_MAIL" instruction. |  |

#### Data consistency

The ADDR_MAIL_SERVER input parameter of the instruction is re-adopted by the "AS_MAIL" instruction each time the sending of an e-mail is triggered. If a change is made during operation, the "new" value only becomes effective once an e-mail is triggered again.

In contrast, the parameter settings of WATCH_DOG_TIME, TO_S, CC, FROM, SUB, TEXT, ATTACHMENT, and, if applicable, USERNAME and PASSWORD are adopted while the "AS_MAIL" instruction is running, which means that they may only be changed when the job has completed (BUSY = 0)

#### Setting the parameters of the TS Adapter IE

On the TS Adapter IE, you need to specify parameters for outgoing calls in such a way as to enable the TS Adapter IE to establish a connection to the dial-up server of your service provider.

If you set "When required" for connection establishment, the connection will only be established when an e-mail needs to be sent.

Connection establishment can take longer (approx. one minute) for an analog modem connection. When you specify the WATCH_DOG_TIME parameter, remember to allow for the time required to establish the connection.

#### Parameters

The following table shows the parameters of the "AS_MAIL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| COM_RST | Input / Output | BOOL | I, Q, M, D, L | Input/output parameter "COMPLETE"  RESTART:  The block has an initialization routine that is  processed when the COM_RST input is set.  The COM_RST parameter of the "AS_MAIL" instruction must be set to "1":  - once, before the first call and - every time that the corresponding instance DB is reloaded.   After initialization, the "AS_MAIL" instruction, resets the COM_RST parameter. |
| REQ | Input | BOOL | I, Q, M, D, L | Control parameter REQUEST: Activates the sending of an e-mail on a rising edge. |
| ADDR_MAIL_ SERVER | Input | DWORD | I, Q, M, D, L | IP address input parameter of the mail server: Specify as a data word in HEX format, for example: IP address = 192.168.0.200.  ADDR_MAIL_SERVER = DW#16#C0A800C8, where:  - 192 = 16#C0, - 168 =16#A8 - 0 = 16#00 and - 200 = 16#C8. |
| WATCH_DOG_TIME | Input | TIME | I, Q, M, D, L | Input parameter for max. period of time:  The "AS_MAIL" instruction should establish a connection within the period specified by WATCH_DOG_TIME. The block is exited with an error if this period is exceeded. The time before the block is exited and the error is output can exceed the WATCH_DOG_TIME because connection termination also takes a certain amount of time. To begin with, you should set a period of 2 minutes. If you have an ISDN telephone connection, a significantly shorter period can be selected. |
| USERNAME | Input | ANY | D | Input parameter for user name:  Reference to a STRING type tag with a maximum length of 180 characters. A user name is an absolute requirement for authentication. |
| PASSWORD | Input | ANY | D | Input parameter for password:  Reference to a STRING type tag with a maximum length of 180 characters. A password is an absolute requirement for authentication. |
| TO_S | Input | ANY | D | Input parameter for receiver addresses:  Reference to a STRING type tag with a maximum length of 240 characters (see call example). |
| CC | Input | ANY | D | Input parameter for CC recipient addresses:  Reference to a STRING type tag with a maximum length of 240 characters (see call example). |
| FROM | Input | ANY | D | Input parameter for sender address:  Reference to a STRING type tag with a maximum length of 240 characters (see call example). |
| SUB | Input | ANY | D | Input parameter for subject of the e-mail:  Reference to a STRING type tag with a maximum length of 240 characters. |
| TEXT | Input | ANY | D | Input parameter for text of the e-mail:  Reference to a data string with a maximum length of 240 characters. |
| ATTACHMENT | Input | ANY | I, Q, M, D, L | Input parameter for e-mail attachment:  Reference to a byte/word/double word field with a maximum length of 65534 bytes. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: E-mail transmission is not yet complete. - BUSY=0: The processing of "AS_MAIL" was stopped. |
| DONE | Output | BOOL | I, Q, M, D, L | - DONE = 0: Job not yet started or still executing. - DONE = 1: Job was executed without errors. |
| ERROR | Output | BOOL | I, Q, M, D, L | ERROR=1: An error occurred during processing. STATUS and SFC_STATUS supply detailed information about the type of error. |
| [STATUS](#status-and-sfc_status-parameters-s7-300-s7-400) | Output | INT | I, Q, M, D, L | Output/status parameter STATUS:  Return value or error information of the "AS_MAIL" instruction. |
| [SFC_STATUS](#status-and-sfc_status-parameters-s7-300-s7-400) | Output | INT | I, Q, M, D, L | Output/status parameter "SFC_STATUS":  Error information of the called communication blocks or the "BLKMOV" instruction. |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **Notes to the parameters for the instruction**
>
> - If the assignment of the parameters USERNAME and PASSWORD is removed, re-entered or changed in the block in which "AS_MAIL" is called, this change will only become effective if the corresponding instance DB is reloaded and the COM_RST parameter is set. Otherwise, the pointer remains on the corresponding parameter in the instance DB.
> - Because of runtime and memory space, the "AS_MAIL" instruction does not perform any syntax check of the parameters TO_S, CC and FROM. Please note the correct syntax of the parameter.
> - The optional parameters CC, TEXT and ATTACHMENT are only sent with the e-mail if they are assigned in the block in which the "AS_MAIL" instruction is called. If such an assignment is removed from the call interface of the "AS_MAIL" instruction, this change only becomes effective when the corresponding instance DB is reloaded and the COM_RST parameter is set. Otherwise, the pointer remains on the corresponding parameter in the instance DB.  
>   Please note that empty strings are not permitted in a parameter assignment.
> - If the ATTACHMENT parameter points to an array in a data block and if the size of this array is changed and stored, the ANY pointer of the ATTACHMENT parameter must be entered again at the interface of the "AS_MAIL" instruction.

#### SMTP authentication

Authentication refers here to a procedure for ensuring an identity, for example, by a password query.

The "AS_MAIL" instruction supports the SMTP authentication procedure AUTH-LOGIN, that is requested by most mail servers. For information about the authentication procedure of your mail server, please refer to your mail server manual or the website of your Internet service provider.

To use the AUTH-LOGIN authentication procedure, the "AS_MAIL" instruction requires the user name with which it can log in with the mail server. This user name corresponds to the user name with which you set up a mail account on your mail server. It is available to the "AS_MAIL" instruction in the USERNAME parameter.

To log on, the "AS_MAIL" instruction also requires the associated password. This password corresponds to the password you specified when you set up your mail account. It is made available to the "AS_MAIL" instruction in the PASSWORD parameter.

The user name and the password are each transferred to the mail server unencrypted (BASE64-coded).

If no user name is specified in the DB, the AUTH-LOGIN authentication procedure is not used. The e-mail is then sent without authentication.

---

**See also**

[Send an email from a system](Establishing%20a%20remote%20connection%20with%20TeleService.md#send-an-email-from-a-system)

### STATUS and SFC_STATUS parameters (S7-300, S7-400)

#### Description

The return values of the "AS_MAIL" instruction can be classified as follows:

- W#16#0000: "AS_MAIL" was completed successfully
- W#16#7xxx: Status of "AS_MAIL"
- W#16#8xxx: An error was reported during the internal call of a communication instruction, during the "BLKMOV" instruction call, or by the mail server.

The following table shows the return values of "AS_MAIL" except for error codes of the communication blocks called internally and the "BLKMOV" instruction.

| Return value  STATUS  (W#16#...): | Return value  SFC_STATUS  (W#16#...): | Explanation | Notes |
| --- | --- | --- | --- |
| 0000 | - | The processing of "AS_MAIL" was completed without errors. | A error-free completion of "AS_MAIL" does not mean that the sent e-mail will necessarily arrive (see below - note on point 1) |
| 7001 |  | "AS_MAIL" is active (BUSY = 1). |  |
| 7002 | 7002 | "AS_MAIL" is active (BUSY = 1). |  |
| 8xxx | xxxx | Processing of "AS_MAIL" was completed with an error code of the communication instructions called internally or the "BLKMOV" instruction. | For detailed information on the evaluation of the SFC_STATUS parameter, refer to the descriptions of the STATUS parameter of the "BLKMOV" instruction. |
| 800z | xxxx | The error message originates from the "BLKMOV" instruction and means:  - z = 1 Error copying the TO_S parameter to the internal buffer - z = 2 Error copying the CC parameter to the internal buffer - z = 3 Error copying the FROM parameter to the internal buffer - z = 4 Error copying the SUB parameter to the internal buffer - z = 5 Error copying the TEXT parameter to the internal buffer - z = 6 Error copying the ATTACHMENT parameter to the internal buffer - z = 7 Error copying the USERNAME parameter to the internal buffer - z = 8 Error copying the PASSWORD parameter to the internal buffer |  |
| 8010 | xxxx | Error during connection establishment. | COM_RST was possibly not set after loading instance DB. |
| 8011 | xxxx | Error sending the data. | For detailed information on the evaluation of SFC_STATUS, refer to the descriptions of the STATUS parameter of the "[TSEND](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#tsend-send-data-via-communication-connection-s7-300-s7-400)" instruction. |
| 8012 | xxxx | Error receiving the data. | For more information on the evaluation of SFC_STATUS, refer to the descriptions of the STATUS parameter of the "[TRCV](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction. |
| 8013 | xxxx | Error during connection establishment. | For more information on the evaluation of SFC_STATUS, refer to the descriptions of the STATUS parameter of the "[TCON](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#tcon-establish-communication-connection-s7-300-s7-400)" and "[TDISCON](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#tdiscon-terminate-communication-connection-s7-300-s7-400)" instructions. |
| 8014 | - | Establishment of a connection is not possible. | You have possibly entered an incorrect mail server IP address (ADDR_MAIL_SERVER) or a time span that is too short (WATCH_DOG_TIME) to establish the connection. It is also possible that the CPU has no connection to the network or that the CPU configuration is incorrect. |
| 82xx, 84xx, or 85xx | - | The error message originates from the mail server and corresponds, except for the "8", to the error number of the SMTP protocol.  The following columns list several error codes that can occur: | See point 2 in the note. |
| 8450 | - | Action not executed: Mailbox not available/not reachable. | Try again later. |
| 8451 | - | Action aborted: Local processing error | Try again later. |
| 8500 | - | Syntax error: Error not recognized. This also includes the error when a command string is too long. This can also be occur when the e-mail server does not support the LOGIN authentication procedure. | Check the parameters of "AS_MAIL". Try to send an e-mail without authentication. To do this, replace the USERNAME parameter with an empty string. |
| 8501 | - | Syntax error: Parameter or argument incorrect | You have possibly entered an incorrect address in TO_S or CC. |
| 8502 | - | Command unknown or not implemented. | Check your entries, in particular the FROM parameter. This is possibly incomplete and you have forgotten "@" or ".". |
| 8535 | - | SMTP authentication incomplete. | You have possibly entered an incorrect user name or incorrect password. |
| 8550 | - | Mail server cannot be reached, you have no access rights. | You have possibly entered an incorrect user name or password, or the mail server does not support your LOGIN. Another cause of error could be an incorrect entry of the domain name after the "@" in TO_S or CC. |
| 8552 | - | Action aborted: Assigned memory size has been exceeded | Try again later. |
| 8554 | - | Transmission failed. | Try again later. |

> **Note**
>
> **Status error**
>
> 1. An incorrect entry of the recipient addresses does not generate a status error of the "AS_MAIL" instruction. In this case, there is no guarantee that the e-mail will be sent to other recipients, even if these were entered correctly.
> 2. You will find more detailed information on the SMTP error code and other error codes in SMTP protocol on the Internet or in the error documentation of the mail server. You can also view the most recent message from the mail server in your instance DB in the BUFFER1 parameter. If you look under "Data", you will find the data most recently sent by the "AS_MAIL" instruction.

### Example of "AS_MAIL" call (S7-300, S7-400)

#### Description

The data that is available to the "AS_MAIL" instruction based on the ANY pointer is stored in a data block. In this example, DB 2 is used for this.

Because of runtime and memory space, the "AS_MAIL" instruction does not perform any syntax check of the parameters TO_S, CC and FROM.

#### Parameters TO_S, CC and FROM

The TO_S, CC and FROM parameters are ANY pointers to strings with, for example, the following content:

- TO: &lt;wenna@mydomain.com&gt;, &lt;ruby@mydomain.com&gt;,
- CC: &lt;admin@mydomain.com&gt;, &lt;judy@mydomain.com&gt;,
- FROM: &lt;admin@mydomain.com&gt;

Note the following rules when entering the parameters:

- The "TO:", "CC:" and "FROM:" characters must be entered.
- A space and an opening angled bracket "&lt;" must be entered before each address.
- A closing angled bracket "&gt;" must be entered after each address.
- A comma must be entered after each address in TO_S and CC.
- Only one e-mail may be entered in FROM, and there must be no comma at the end of this address.

#### Initialization / startup in OB 100

The COM_RST parameter of the "AS_MAIL" instruction must be set before the first call of the  
 instruction, or always after a reloading of the associated instance DB.

In the following example, DB 1 is the instance DB of the "AS_MAIL" instruction.

| SET |  | //Set RLO |
| --- | --- | --- |
| R | DB1.REQ | //REQ is reset so that the "AS_MAIL" instruction does not start to send an e-mail immediately after COM_RST is set. |
| S | DB1.COM_RST | //COM_RST is set; this must be set once for initialization before the first call of the "AS_MAIL" instruction, or always after reloading the associated instance DB. |
|  |  |  |

#### Cyclic call

This example of the "AS_MAIL" instruction call must be called cyclically (for example, in OB1).   
In the user program, use "Modify tags" to set the REQ parameter to "1".

You can copy these lines to an STL source file and compile them. To do this, however, the blocks DB 1 and DB 2 must be entered in the project's tag table.

| Example of "AS_MAIL" call | Explanation |
| --- | --- |
| DATA_BLOCK "DB2" | //Global data block with the data for the "AS_MAIL" instruction |
| TITLE = |  |
| VERSION : 1.0 |  |
|  |  |
| STRUCT |  |
| TO_S : STRING [240 ] := 'TO: &lt;wenna@mydomain.com&gt;, &lt;ruby@mydomain.com&gt;,'; | //Address of recipient |
| CC : STRING [240 ] := 'CC: &lt;admin@mydomain.com&gt;, &lt;judy@mydomain.com&gt;,'; | //CC Address of recipient |
| FROM : STRING [60 ] := 'FROM: &lt;admin@mydomain.com&gt;'; | //Address of sender |
| SUB : STRING [60 ] := 'Status plant 7'; | //Subject |
| TEXT : STRING [240 ] := 'Fault in plant 7 sector 2'; | //Text |
| USERNAME : STRING [60 ] := 'admin'; | //User name for LOGIN authentication |
| PASSWORD : STRING [60 ] := 'test'; | //Password for LOGIN authentication |
| ATTACHMENT : ARRAY [1 .. 178 ] OF BYTE; | //Attachment |
| END_STRUCT ; |  |
| BEGIN |  |
| END_DATA_BLOCK |  |
|  |  |
| DATA_BLOCK "DB1" | //Instance DB of the "AS_MAIL" instruction |
| TITLE = |  |
| AUTHOR : TELESERV |  |
| FAMILY : TELESERV |  |
| VERSION : 1.0 |  |
|  |  |
| "AS_MAIL" |  |
| BEGIN |  |
| END_DATA_BLOCK |  |
|  |  |
| FUNCTION_BLOCK FB 1 |  |
| TITLE =Example AS_MAIL | The COM_RST parameter of the "AS_MAIL" instruction must be set before the first "AS_MAIL" call, or always after reloading the associated instance DB. The call condition is set during the execution of the user program. |
| VERSION : 1.0 |  |
| VAR |  |
| CallCondition: BOOL ; |  |
| END_VAR |  |
| BEGIN |  |
| NETWORK |  |
| CALL AS_MAIL, DB1 ( | //Calling AS_MAIL |
| REQ := # CallCondition, | //Job triggered on rising edge |
| ADR_MAIL_SERVER := DW#16#C0A800C8, | //Corresponds to the IP address 192.168.0.200 in HEX format |
| WATCH_DOG_TIME := T#2M, | //Time span of 2 minutes within which sending should be completed |
| USERNAME := DB2.USERNAME, | //Pointer to user name of the sender. If there is no DB2.USERNAME , in other words, no parameter is assigned, the LOGIN authentication procedure is not used. |
| PASSWORD := DB2.PASSWORD, | //Pointer to the password |
| TO_S := DB2.TO_S, | //Pointer to the recipient address |
| CC := DB2.CC, | //Pointer to the CC recipient address (optional). If there is no DB2.CC, in other words, if this is not assigned, the e-mail is not sent to the CC recipient. |
| FROM := DB2.FROM, | //Pointer to the address of the sender |
| SUB := DB2.SUB, | //Pointer to the subject of the mail |
| TEXT := DB2.TEXT, | //Pointer to the text of the mail (optional). If there is no DB2.TEXT, in other words, if this is not assigned, the e-mail is sent without text. |
| ATTACHMENT := DB2.ATTACHMENT, | //Pointer to the mail attachment (optional). Example: 101 bytes in the mail attachment - ATTACHMENT := P#DB2.DBX974.0 BYTE 101 (example relates to the above DB).  //If there is no DB2.ATTACHMENT, in other words, if this is not assigned, the e-mail is sent without an attachment. |
| BUSY := M46.0, | //Output/status parameter BUSY |
| DONE := M46.1, | //Output/status parameter DONE |
| ERROR := M46.2, | //Output/status parameter ERROR |
| STATUS := MW48, | //Output/status parameter STATUS |
| SFC_STATUS := MW50 | //Output/status parameter SFC_STATUS |
| ); |  |
|  | //Checking the call results at the end of the processing |
| U M 46.0; | //Is BUSY ==0? |
| SPB End; | //No, BUSY ==1, "AS_MAIL" is still processing the job |
| U M 46.1; | //Was the processing of "AS_MAIL" completed  without errors? |
| SPB End; |  |
| NOP 0; | //No, an error occurred during processing, BUSY ==0, BR ==0. |
|  | //Add further error evaluation here, if necessary, STATUS, SFC_STATUS |
| End:BE; |  |
| END_FUNCTION_BLOCK |  |
|  |  |

> **Note**
>
> **Optional parameters**
>
> For the optional parameters USERNAME, PASSWORD, CC, TEXT and ATTACHMENT, the following applies:
>
> If an assignment is removed or re-inserted, this change will only be valid when the associated instance DB (in this example, DB 1) is reloaded and the "COM_RST" parameter is set.

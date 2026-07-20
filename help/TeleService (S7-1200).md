---
title: "TeleService (S7-1200)"
package: ProgInstTeleServ2MenUS
topics: 5
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TeleService (S7-1200)

This section contains information on the following topics:

- [TM_MAIL: Transfer email (S7-1200)](#tm_mail-transfer-email-s7-1200)

## TM_MAIL: Transfer email (S7-1200)

This section contains information on the following topics:

- [Description of TM_MAIL (S7-1200)](#description-of-tm_mail-s7-1200)
- [Parameters TO_S, CC, and FROM (S7-1200)](#parameters-to_s-cc-and-from-s7-1200)
- [STATUS and SFB_STATUS parameters (S7-1200)](#status-and-sfb_status-parameters-s7-1200)

### Description of TM_MAIL (S7-1200)

#### Description

The "TM_MAIL" instruction works asynchronously, in other words, its execution extends over multiple calls. You must specify an instance when you call the instruction "TM_MAIL". The attribute "retentive" must not be set in the instance. This attribute ensures that the instance is initialized when the CPU switches from STOP to RUN and that a new e-mail send job can be triggered afterwards.

You start the sending of an e-mail with an edge change from "0" to "1" for the REQ parameter. The job status is indicated by the output parameters "BUSY", "DONE", "ERROR", "STATUS" and "SFC_STATUS". "SFC_STATUS" corresponds in this case to the "STATUS" output parameter of the called communication blocks.

The output parameters DONE, ERROR, STATUS, and SFC_STATUS are each displayed for only one cycle if the status of the BUSY output parameter changes from "1" to "0". The following table shows the relationship between BUSY, DONE, and ERROR. Using this table, you can determine the current status of the instruction "TM_MAIL" and when the sending of the e-mail is complete.

| DONE | BUSY | ERROR | Description |
| --- | --- | --- | --- |
| 0 | 1 | 0 | The job is being processed. |
| 1 | 0 | 0 | Job successfully completed. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error can be found in the STATUS and SFC_STATUS parameters. |
| 0 | 0 | 0 | The "TM_MAIL" instruction was not assigned a (new) job. |

If the CPU changes to STOP mode while "TM_MAIL" is active, the communication connection to the mail server aborts. The communication connection to the mail server will also be lost if communication problems occur on the Industrial Ethernet bus. In this case, the transfer of the e-mail will be interrupted and it will not reach its recipient.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Changing user programs**  You can change the parts of your user program that directly affect calls of "TM_MAIL" only:  - when the CPU is in "STOP" mode - when no mail is being sent (REQ = 0 and BUSY = 0).   This relates, in particular, to deleting and replacing program blocks that contain "TM_MAIL" calls or calls for the instance of "TM_MAIL".  Ignoring this restriction can tie up connection resources. The automation system can change to an undefined status for the TPC/IP communication functions via Industrial Ethernet.  A warm or cold restart of the CPU is required after the changes are transferred. |  |

#### Data consistency

The ADDR_MAIL_SERVER input parameter of the instruction is taken from the "TM_MAIL" instruction again each time the sending of an e-mail is triggered. If a change is made during operation, the "new" value only becomes effective once an e-mail is triggered again.

In contrast, the WATCH_DOG_TIME, TO_S, CC, FROM, SUBJECT, TEXT, ATTACHMENT, and, if applicable, USERNAME and PASSWORD parameters are taken from the "TM_MAIL" instruction while it is running, which means that they can only be changed after the job is complete (BUSY = 0)

#### Setting the parameters of the TS Adapter IE

On the TS Adapter IE, you need to specify parameters for outgoing calls in such a way as to enable the TS Adapter IE to establish a connection to the dial-up server of your service provider.

If you set "When required" for connection establishment, the connection will only be established when an e-mail needs to be sent.

Connection establishment can take longer (approx. one minute) for an analog modem connection. When you specify the WATCH_DOG_TIME parameter, remember to allow for the time required to establish the connection.

#### Parameter

The following table shows the parameters of the "TM_MAIL" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Control parameter REQUEST: Activates the sending of an e-mail on a rising edge. |
| ID | Input | CONN_OUC (Word) | D, L or constant | Reference to the connection to be established. See ID parameter of the [TCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200), [TDISCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tdiscon-terminate-communication-connection-s7-1200-s7-1500), [TSEND](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1), and [TRCV](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv-receive-data-via-communication-connection-s7-1200) instructions. A number that is not used for any additional instances of this instruction in the user program must be entered here. |
| [TO_S](#parameters-to_s-cc-and-from-s7-1200) | Input | STRING | D | Input parameter for receiver addresses:  STRING with a maximum length of 240 characters (see example call). |
| [CC](#parameters-to_s-cc-and-from-s7-1200) | Input | STRING | D | Input parameter for CC recipient addresses (optional): STRING with a maximum length of 240 characters (see example call).  If an empty string is assigned here, the e-mail is not sent to a CC recipient. |
| SUBJECT | Input | STRING | D | Input parameter for subject of the e-mail:  STRING with a maximum length of 240 characters. |
| TEXT | Input | STRING | D | Input parameter for text of the e-mail (optional):  Reference to a data string with a maximum length of 240 characters.  If an empty string is assigned at this parameter, the e-mail is sent without text. |
| ATTACHMENT | Input | VARIANT | I, Q, M, D, L | Input parameter for e-mail attachment (optional): Reference to a byte/word/double word field with a maximum length of 65534 bytes. The specified attachment must be in the file format BIN.  If no value is assigned, the e-mail is sent without an attachment. |
| DONE | Output | BOOL | I, Q, M, D, L | - DONE = 0: Job not yet started or still executing. - DONE = 1: Job executed without errors. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: Sending of an e-mail is not yet complete. - BUSY = 0: Processing of "TM_MAIL" was terminated |
| ERROR | Output | BOOL | I, Q, M, D, L | ERROR = 1: An error occurred during processing. STATUS and SFC_STATUS supply detailed information about the type of error. |
| [STATUS](#status-and-sfb_status-parameters-s7-1200) | Output | WORD | I, Q, M, D, L | Output/status parameter STATUS:  Return value or error information of the "TM_MAIL" instruction. |
| ADDR_MAIL_SERVER | Static* | DWORD | I, Q, M, D, L | IP address input parameter of the mail server: Specify as a data word in HEX format, for example: IP address = 192.168.0.200.  ADDR_MAIL_SERVER = DW#16#C0A800C8, where:  - 192 = 16#C0, - 168 =16#A8 - 0 = 16#00 and - 200 = 16#C8. |
| WATCH_DOG_TIME | Static* | TIME | I, Q, M, D, L | Input parameter for max. period of time:  The "TM_MAIL" instruction should establish a connection within the period specified by WATCH_DOG_TIME. The block is exited with an error if this period is exceeded. The time before the block is exited and the error is output can exceed the WATCH_DOG_TIME because connection termination also takes a certain amount of time. To begin with, you should set a period of 2 minutes. If you have an ISDN telephone connection, a significantly shorter period can be selected. |
| USERNAME | Static* | STRING | D | Input parameter for user name:  STRING with a maximum length of 180 characters. A user name is an absolute requirement for authentication. |
| PASSWORD | Static* | STRING | D | Input parameter for password:  STRING with a maximum length of 180 characters. A password is an absolute requirement for authentication. |
| [FROM](#parameters-to_s-cc-and-from-s7-1200) | Static* | STRING | D | Input parameter for sender address:  STRING with a maximum length of 240 characters (see example call). |
| [SFC_STATUS](#status-and-sfb_status-parameters-s7-1200) | Static* | WORD | I, Q, M, D, L | Output/status parameter "SFC_STATUS":  Error information of the called communication blocks. |
| * The values of the parameter are not modified at every call of the instruction "TM_MAIL". The values are in the static parameters of the instance and are only written once at the first call of the instruction. |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

> **Note**
>
> **Optional parameters**
>
> The optional parameters CC, TEXT, and ATTACHMENT are only sent with the e-mail if the corresponding parameters contain a string of length > 0.

> **Note**
>
> **Parameter ATTACHMENT**
>
> The specified attachment must be in the file format BIN. If text is to be transferred, you have the following options:
>
> - In Windows, you link the file format BIN with a text editor.
> - You use the Windows functions "Send to" or "Open with".

#### SMTP authentication

Authentication refers here to a procedure for ensuring an identity, for example, by a password query.

The "TM_MAIL" instruction supports the SMTP authentication procedure AUTH-LOGIN that is requested by most mail servers. For information about the authentication procedure of your mail server, refer to your mail server manual or the website of your Internet service provider.

To use the AUTH-LOGIN authentication procedure, the "TM_MAIL" instruction requires the user name with which it can log onto the mail server. This user name corresponds to the user name with which you set up a mail account on your mail server. It is made available to the "TM_MAIL" instruction in the USERNAME parameter.

To log on, the "TM_MAIL" instruction also requires the associated password. This password corresponds to the password you specified when you set up your mail account. It is made available to the "TM_MAIL" instruction in the PASSWORD parameter.

The user name and the password are each transferred to the mail server unencrypted (BASE64-coded).

If no user name is specified in the DB, the AUTH-LOGIN authentication procedure is not used. The e-mail is then sent without authentication.

#### Example

You can find a detailed application example in the Siemens Industry Online Support under the following FAQ ID: [67262019](https://support.industry.siemens.com/cs/ww/en/view/67262019).

### Parameters TO_S, CC, and FROM (S7-1200)

#### Description

The TO_S, CC, and FROM parameters are strings with, for example, the following content:

- TO: <wenna@mydomain.com>, <ruby@mydomain.com>,
- CC: <admin@mydomain.com>, <judy@mydomain.com>,
- FROM: <admin@mydomain.com>

Note the following rules when entering the parameters:

- The "TO:", "CC:", and "FROM:" characters must be entered.
- A space and an opening pointed bracket "<" must be entered before each address.
- A closing pointed bracket ">" must be entered after each address.
- A comma must be entered after each address in TO and CC.
- Only one e-mail may be entered in FROM, and there must not be a comma at the end of this address

Because of runtime and memory space, the "TM_MAIL" instruction does not perform any syntax check of the parameters TO_S, CC and FROM.

### STATUS and SFB_STATUS parameters (S7-1200)

#### Description

The return values of the "TM_MAIL" instruction can be classified as follows:

- W#16#0000: "TM_MAIL" was completed successfully
- W#16#7xxx: Status of "TM_MAIL"
- W#16#8xxx: An error was reported during the internal call of a communication block or from the mail server.

The following table shows the return values of "TM_MAIL" except for error codes of the internally called communication blocks.

| Return value  STATUS*  (W#16#...): | Return value  SFB_STATUS  (W#16#...): | Explanation | Notes |
| --- | --- | --- | --- |
| 0000 | - | The processing of "TM_MAIL" was completed without errors. | A without error completion of "TM_MAIL" does not mean that the sent e-mail will necessarily arrive (see below - note on point 1) |
| 7001 |  | "TM_MAIL" is active (BUSY = 1). | Initial call; job has started |
| 7002 | 7002 | "TM_MAIL" is active (BUSY = 1). | Intermediate call; job already active |
| 8xxx | xxxx | The processing of "TM_MAIL" was completed with an error code of the internally called communication instructions. | For detailed information on the evaluation of the SFB_STATUS parameter, refer to the descriptions of the STATUS parameter of the communication instructions. |
| 8010 | xxxx | Error during connection establishment. | For further information on the evaluation of the SFB_STATUS parameter, refer to the descriptions of the STATUS parameter of the "[TCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)" instruction. |
| 8011 | xxxx | Error sending the data. | For further information on the evaluation of SFB_STATUS, refer to the descriptions of the STATUS parameter of the "[TSEND](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tsend-send-data-via-communication-connection-s7-1200-s7-1500-1)" instruction. |
| 8012 | xxxx | Error receiving the data. | For further information on the evaluation of SFB_STATUS, refer to the descriptions of the STATUS parameter of the "[TRCV](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#trcv-receive-data-via-communication-connection-s7-1200)" instruction. |
| 8013 | xxxx | Error during connection establishment. | For further information on the evaluation of SFB_STATUS, refer to the descriptions of the STATUS parameter of the "[TCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tcon-establish-communication-connection-s7-1200)" and "[TDISCON](Open%20User%20Communication%20%28S7-1200%2C%20S7-1500%29.md#tdiscon-terminate-communication-connection-s7-1200-s7-1500)" instructions. |
| 8014 | - | Establishment of a connection is not possible. | You have possibly entered an incorrect mail server IP address (ADDR_MAIL_SERVER) or a time span that is too short (WATCH_DOG_TIME) to establish the connection. It is also possible that the CPU has no connection to the network or that the CPU configuration is incorrect. |
| 8016 | - | Error copying the attachment | - |
| 82xx, 84xx, or 85xx | - | The error message originates from the mail server and the last three digits correspond to the error number of the SMTP protocol.  The following columns list several error codes that can occur: | See point 2 in the note. |
| 8450 | - | Action not executed: Mailbox not available/not reachable. | Try again later. |
| 8451 | - | Action aborted: Local processing error | Try again later. |
| 8500 | - | Syntax error: Error not recognized. This also includes the error when a command string is too long. This can also occur when the e-mail server does not support the LOGIN authentication procedure. | Check the parameters of "TM_MAIL". Try to send an e-mail without authentication. To do this, replace the USERNAME parameter with an empty string. |
| 8501 | - | Syntax error: Parameter or argument incorrect | You have possibly entered an incorrect address in TO_S or CC. |
| 8502 | - | Command unknown or not implemented. | Check your entries, in particular the FROM parameter. This is possibly incomplete and you have forgotten "@" or ".". |
| 8535 | - | SMTP authentication incomplete. | You have possibly entered an incorrect user name or incorrect password. |
| 8550 | - | Mail server cannot be reached, you have no access rights. | You have possibly entered an incorrect user name or password, or the mail server does not support your LOGIN. Another cause of error could be an incorrect entry of the domain name after the "@" in TO_S or CC. |
| 8552 | - | Action aborted: Assigned memory size has been exceeded | Try again later. |
| 8554 | - | Transmission failed. | Try again later. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |  |  |

> **Note**
>
> **Status error**
>
> 1. An incorrect entry of the recipient addresses does not generate a status error of the "TM_MAIL" instruction. In this case, there is no guarantee that the e-mail will be sent to other recipients, even if these were entered correctly.
> 2. You can find more detailed information on the SMTP error code and other error codes in SMTP protocol on the Internet or in the error documentation of the mail server. You can also view the most recent message from the mail server in your instance DB in the BUFFER1 parameter. If you look under "Data", you will find the data most recently sent by the "TM_MAIL" instruction.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

---
title: "Point-to-point (S7-1200)"
package: ProgKomPtP2MenUS
topics: 10
devices: [S7-1200]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Point-to-point (S7-1200)

This section contains information on the following topics:

- [PORT_CFG: Configure communication parameters dynamically (S7-1200)](#port_cfg-configure-communication-parameters-dynamically-s7-1200)
- [SEND_CFG: Configure serial transmission parameters dynamically (S7-1200)](#send_cfg-configure-serial-transmission-parameters-dynamically-s7-1200)
- [RCV_CFG: Configure serial receive parameters dynamically (S7-1200)](#rcv_cfg-configure-serial-receive-parameters-dynamically-s7-1200)
- [SEND_PTP: Transmit send buffer data (S7-1200)](#send_ptp-transmit-send-buffer-data-s7-1200)
- [RCV_PTP: Enable receive messages (S7-1200)](#rcv_ptp-enable-receive-messages-s7-1200)
- [RCV_RST: Delete receive buffer (S7-1200)](#rcv_rst-delete-receive-buffer-s7-1200)
- [SGN_GET: Query RS-232 signals (S7-1200)](#sgn_get-query-rs-232-signals-s7-1200)
- [SGN_SET: Set RS-232 signals (S7-1200)](#sgn_set-set-rs-232-signals-s7-1200)
- [General status information of the communications blocks (S7-1200)](#general-status-information-of-the-communications-blocks-s7-1200)

## PORT_CFG: Configure communication parameters dynamically (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

The instruction "PORT_CFG" allows dynamic configuration of communications parameters for a point-to-point communications port.

You set up the original static configuration of the port in the hardware configuration. You can change this configuration by executing the "PORT_CFG" instruction. You can also use this function to save created blocks in libraries and to avoid configuration in the hardware configuration when you reuse it.

With "PORT_CFG" you can influence the following communications parameter settings:

- Parity
- Baud rate
- Number of bits per character
- Number of stop bits
- Type and properties of flow control

The changes made by the "PORT_CFG" instruction are not stored permanently on the target system.

You can transfer serial data via the electrical connections RS-232 (half and full duplex) and RS-485 (half duplex).

### Parameters

The following table shows the parameters of the "PORT_CFG" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Activates the configuration change on a rising edge |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| PROTOCOL | Input | UINT | I, Q, M, D, L or constant | Transmission protocol:  - 0: Point-to-point communication protocol - 1..n: Future definition for specific transmission protocols |
| BAUD | Input | UINT | I, Q, M, D, L or constant | Baud rate of the port:  - 1: 300 baud - 2: 600 baud - 3: 1200 baud - 4: 2400 baud - 5: 4800 baud - 6: 9600 baud (default) - 7: 19200 baud - 8: 38400 baud - 9: 57600 baud - 10: 76800 baud - 11: 115200 baud |
| PARITY | Input | UINT | I, Q, M, D, L or constant | Parity of the port:  - 1: No parity (default) - 2: Even parity - 3: Odd parity - 4: Mark parity - 5: Space parity |
| DATABITS | Input | UINT | I, Q, M, D, L or constant | Bits per character:  - 1: 8 bits per character (default) - 2: 7 bits per character |
| STOPBITS | Input | UINT | I, Q, M, D, L or constant | Number of stop bits:  - 1: 1 stop bit (default) - 2: 2 stop bits |
| FLOWCTRL | Input | UINT | I, Q, M, D, L or constant | Data flow control:  - 1: None (default) - 2: XON/XOFF - 3: Hardware flow control (RTS always activated) - 4: Hardware flow control (RTS can be deactivated during transmission) |
| XONCHAR | Input | CHAR | I, Q, M, D, L or constant | Indicates the character used as XON character. The character DC1 (11H) is set as default. |
| XOFFCHAR | Input | CHAR | I, Q, M, D, L or constant | Indicates the character used as XOFF character. The character DC3 (13H) is set as default. |
| WAITTIME | Input | UINT | I, Q, M, D, L or constant | Specifies the wait time for XON or CTS after the start of the transmission.   The specified value must be greater than 0. 2000 milliseconds are set as default. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#...) | Description |
| --- | --- |
| 80A0 | The specified protocol is invalid. |
| 80A1 | The specified baud rate is invalid. |
| 80A2 | The specified parity rate is invalid. |
| 80A3 | The specified number of bits per character is invalid. |
| 80A4 | The specified number of stop bits is invalid. |
| 80A5 | The specified type of flow control is invalid. |
| 80A6 | Incorrect value at the WAITTIME parameter  When the data flow control is enabled, the value at the WAITTIME parameter must be greater than zero. |
| 80A7 | Invalid values at XONCHAR and XOFFCHAR parameters. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## SEND_CFG: Configure serial transmission parameters dynamically (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

The instruction "SEND_CFG" allows dynamic configuration of serial transmission parameters for a point-to-point communications port. All the messages waiting for transfer are discarded after execution of SEND_CFG.

You set up the original static configuration of the port in the hardware configuration. You can change this configuration by executing the "SEND_CFG" instruction. You can also use this function to save created blocks in libraries and to avoid configuration in the hardware configuration when you reuse it. With "SEND_CFG" you can influence the following transmission parameter settings:

- Time between the activation of RTS (Request to Send) and the start of the transmission
- Time between the end of transmission and the deactivation of RTS
- Define bit times for breaks

The changes made by the "SEND_CFG" instruction are not stored permanently on the target system.

You can transfer serial data via the electrical connections RS-232 (half and full duplex) and RS-485 (half duplex).

### Parameters

The following table shows the parameters of the "SEND_CFG" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Activates the configuration change on a rising edge |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| RTSONDLY | Input | UINT | I, Q, M, D, L or constant | The time that should elapse after activating RTS until the start of transmission.   Valid values for this parameter are as follows:  - 0 (default) - 0 to 65535 ms in steps of 1 ms   This parameter does not apply to RS-485 modules. |
| RTSOFFDLY | Input | UINT | I, Q, M, D, L or constant | Time that should elapse after the end of transmission until deactivation of RTS.   Valid values for this parameter are as follows:  - 0 (default) - 0 to 65535 ms in steps of 1 ms   This parameter does not apply to RS-485 modules. |
| BREAK | Input | UINT | I, Q, M, D, L or constant | Specifies the bit times for a break, which are sent at the start of the message.  12 bit times are set as default. A maximum of 25000 bit times can be specified. |
| IDLELINE | Input | UINT | I, Q, M, D, L or constant | Specifies the bit times for idle line after the break at the start of the message.  12 bit times are set as default. A maximum of 25000 bit times can be specified. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#...) | Description |
| --- | --- |
| 80B0 | The configuration of a transmission interruption is not permitted. |
| 80B1 | The specified break time exceeds the permitted maximum of 25000 bit times. |
| 80B2 | The specified time for idle line exceeds the permitted maximum of 25000 bit times. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## RCV_CFG: Configure serial receive parameters dynamically (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

The instruction "RCV_CFG" allows dynamic configuration of serial receive parameters for a point-to-point communications port. You can use this instruction to configure the conditions that specify the start and end of the message to be transmitted. The receipt of messages that correspond to these conditions can be enabled by the "[RCV_PTP](#rcv_ptp-enable-receive-messages-s7-1200)" instruction.

You set up the original static configuration of the port in the properties of the hardware configuration. Execute the "RCV_CFG" instruction in your program to change the configuration. You can also use this function to save created blocks in libraries and to avoid configuration in the hardware configuration when you reuse it. The changes made by the "RCV_CFG" instruction are not stored permanently on the target system.

All the messages waiting for transfer are discarded after execution of the "RCV_CFG" instruction.

### Parameters

The following table shows the parameters of the "RCV_CFG" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Activates the configuration change on a rising edge. |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| CONDITIONS | Input | CONDITIONS | D, L | Data structure defining the conditions for start and end of data transmission. |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred. |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Data type CONDITIONS

You can use the CONDITIONS structure to define the start and end conditions for the message transmission. The structure CONDITIONS is included in the instance DB of the "RCV_CFG" instruction. Use the structure CONDITIONS to define the start and end conditions when the transmission of a message is complete and when the next message transfer is to start:

- You define the start conditions for the data transfer in the START structure.
- You define the end conditions for the data transfer in the END structure.

You can define one or more start and end conditions for this. If you specify multiple start or end conditions these are linked by an OR logic instruction.

The following table shows the "CONDITIONS" structure:

| Parameters |  | Data type | Description |
| --- | --- | --- | --- |
| START |  | STRUCT | Start conditions |
|  | STARTCOND | UINT | Specifies the start condition (details, see below).  The start condition can be specified as a 16-bit hexadecimal value. Possible values for the start condition are:  - 1: Start character - 2: Any character (default) - 4: Line break - 8: Idle line - 16: Character string 1 - 32: Character string 2 - 64: Character string 3 - 128: Character string 4   Multiple start conditions can also be defined at the STARTCOND parameter. The total from the values of the individual conditions is specified for this. If, for example, you want to define "Idle line" OR "Character string 1" OR "Character string 4" as start condition, the value "152" must be specified. |
| IDLETIME | UINT | Specifies the maximum idle time of the line before receipt is started.   Valid values for this parameter are as follows:  - 40 bit times (default) - 0 to 2500 bit times |  |
| STARTCHAR | BYTE | Specifies the start character. This setting is only enabled when the configured start condition is "Start character".  Valid values for this parameter are as follows:  - 02 (STX): Default setting - B#16#00 to B#16#FF |  |
| SEQ[1].CTL | BYTE | Character string 1: Control sequence for each character   You can use the bit position of the character to define which characters of the character string will be considered or ignored. To evaluate the characters, the corresponding bits have to be set.   - Bit 0: 1 character - Bit 1: 2 characters - Bit 2: 3 characters - Bit 3: 4 characters - Bit 4: 5 characters   A character is ignored when the corresponding bit is reset. |  |
| SEQ[1].STR | CHAR[5] | Character string 1: Start character (5 characters) |  |
| SEQ[2].CTL | BYTE | Character string 2: Ignore/compare control sequence for each character |  |
| SEQ[2].STR | CHAR[5] | Character string 2: Start character (5 characters) |  |
| SEQ[3].CTL | BYTE | Character string 3: Ignore/compare control sequence for each character |  |
| SEQ[3].STR | CHAR[5] | Character string 3: Start character (5 characters) |  |
| SEQ[4].CTL | BYTE | Character string 4: Ignore/compare control sequence for each character |  |
| SEQ[4].STR | CHAR[5] | Character string 4: Start character (5 characters) |  |
| END |  | STRUCT | End conditions |
|  | ENDCOND | UINT | Specifies the end condition (details, see below).  The end condition can be specified as a 16-bit hexadecimal value. Possible values for the end condition are:  - 1: Reply timeout - 2: Message timeout - 4: Timeout within the character string - 8: Maximum length - 16: N+LEN+M; the information on the message length in integrated in the message and will be evaluated. - 32: Character string 1   Multiple end conditions can also be defined at the ENDCOND parameter. The total from the values of the individual end conditions is specified for this. If, for example, you want to define the end condition "Maximum length" OR "Sequence 1", the value "40" must be specified. |
| MAXLEN | UINT | Specifies the maximum number of characters in a message.   Valid values* for this parameter are as follows:  - 1 character (default) - 0 to 1024 characters   This setting is only enabled if the "Maximum length" end condition is set at the ENDCOND parameter. |  |
| N | UINT | Offset of the length field in the message  Valid values for this parameter are as follows:  - 0 characters (default) - 0 to 1024 characters   This setting is only enabled if the "N+LEN+M" end condition is set at the ENDCOND parameter. |  |
| LENGTHSIZE | UINT | Size of the length field in bytes  Valid values* for this parameter are as follows:  - 0 bytes (default) - 1 byte - 2 bytes - 4 bytes   This setting is only enabled if the "N+LEN+M" end condition is set at the ENDCOND parameter. |  |
| LENGTHM | UINT | Specifies the number of end characters that follow the length field but are not contained in the length of the message.   Valid values for this parameter are as follows:  - 0 characters (default) - 0 to 255 characters   This setting is only enabled if the "N+LEN+M" end condition is set at the ENDCOND parameter. |  |
| RCVTIME | UINT | Specifies the maximum duration for the receipt of the first character of a message.  Valid values for this parameter are as follows:  - 200 ms (default) - 0 to 65535 ms in steps of 1 ms   This setting is only enabled if the "Reply timeout" end condition is set at the ENDCOND parameter. |  |
| MSGTIME | UINT | Specifies the maximum duration of the receipt of a message.   Valid values for this parameter are as follows:  - 200 ms (default) - 0 to 65535 ms in steps of 1 ms   This setting is only enabled if the "Message timeout" end condition is set at the ENDCOND parameter. |  |
| CHARGAP | UINT | Specifies the time interval between received consecutive characters.  Valid values for this parameter are as follows:  - 12 bit times (default) - 0 to 2500 bit times   This setting is only enabled if the "Timeout within the character string" end condition is set at the ENDCOND parameter. |  |
| SEQ.CTL | BYTE | Character string: Control sequence for each character   You can use the bit position of the character to define which characters of the character string will be considered or ignored. To evaluate the characters, the corresponding bits have to be set.   - Bit 0: 1 character - Bit 1: 2 characters - Bit 2: 3 characters - Bit 3: 4 characters - Bit 4: 5 characters   A character is ignored when the corresponding bit is reset. |  |
| SEQ.STR | CHAR[5] | Character string: Start character (5 characters) |  |
| * These value ranges also apply to the corresponding hardware settings for specifying the end of message. |  |  |  |

### Start conditions for the message receipt ( STARTCOND parameter)

The start of the message is recognized by the receiver if a configured start condition applies. The following conditions can be defined as start conditions for message receipt:

- Start character: The start of a message is recognized when a certain character occurs. This character is stored as first character of the message. All characters received before the start character are rejected.
- Any character: Any character can define the start of a message. This character is stored as first character of the message.
- Line break: The start of a message is recognized if the received data stream is interrupted for longer than one character length.
- Idle line: The start of a message is recognized when the send transmission line is in the idle state for a certain time (specified in bit times) followed by renewed transmission of characters.
- Character string (sequence): The start of a message is recognized when a specified character sequence occurs in the data stream. You can specify up to four character sequences with up to five characters each.

  Example: A received hexadecimal message includes the following characters: "68 10 aa 68 bb 10 aa 16". The configured start character sequences are listed in the following

  table. Start character sequences will be evaluated once the first character 68H

  has been received successfully. After the fourth character has been received successfully (the

  second 68H), the start condition "1" has been met. Once the start conditions have been met,

  evaluation of the end conditions will start.

  Processing of the start character sequence can end due to different errors in parity,

  framing or time intervals between characters. These errors will prevent

  reception of the message, because the start condition has not

  been met.

| Start condition | First character | First character +1 | First character +2 | First character +3 | First character +4 |
| --- | --- | --- | --- | --- | --- |
| 1 | 68H | xx | xx | 68H | xx |
| 2 | 10H | aaH | xx | xx | xx |
| 3 | dcH | aaH | xx | xx | xx |
| 4 | e5H | xx | xx | xx | xx |

### End conditions for the message receipt ( ENDCOND parameter)

The start of a message is recognized by the receiver if a configured end condition applies. The following conditions can be defined as end conditions for message receipt:

- Reply timeout: The receipt of messages will end when the specified maximum duration for the receipt of a character is exceeded. The maximum duration is defined at the RCVTIME parameter. The defined time starts to run down as soon at the last transmission is completed and the RCV_PTP instruction enables the receipt of the message. If no character was received within the defined time (RCVTIME), the RCV_PTP instruction reports an error.
- Message timeout: The receipt of messages will end when the specified maximum duration for the receipt of a message is exceeded. The maximum duration is defined at the MSGTIME parameter. The defined time starts to run down as soon as the first character of the message is received.
- Timeout within the character string: The receipt of messages will end when the time interval between the receipt of two consecutive characters is longer than the value at the CHARGAP parameter.
- Maximum length: The receipt of messages will end when the length of the message defined at the MAXLEN parameter is exceeded.
- Reading message length (N+LEN+M): The receipt of messages will end when a certain message length is reached. This length is calculated by the values of the following parameters:

  - N: Position of the character in the message, as of which the length field begins.
  - LENGTHSIZE: Size of the length field in bytes
  - LENGTHM: Number of end characters that follow the length field. These characters are not taken into account in the evaluation of the message length.
- Character string: The receipt of messages will end when a defined character sequence is received. The character string can contain a maximum of five characters. For each character of the character string, you can use the bit position to define if this will be considered or ignored in the evaluation.

### STATUS parameter

| Error code*  (W#16#...) | Description |
| --- | --- |
| 80C0 | Error in start condition |
| 80C1 | - Error in end condition - No end condition defined |
| 80C2 | Receive interrupt enabled |
| 80C3 | A value that is equal to 0 or greater than 4132 was entered at the MAXLEN parameter while the "Maximum length" end condition was set. |
| 80C4 | A value that is greater than 4131 was entered at the N parameter while the "N+LEN+M" end condition was set. |
| 80C5 | A value that is equal to 0 or invalid was entered at the LENGTHSIZE parameter while the "N+LEN+M" end condition was set. |
| 80C6 | A value that is greater than 255 was entered at the LENGTHM parameter while the "N+LEN+M" end condition was set. |
| 80C7 | A message length greater than 4132 was calculated while the "N+LEN+M" end condition was set. |
| 80C8 | A value that is equal to 0 was entered at the RCVTIME parameter while the "Reply timeout" end condition was set. |
| 80C9 | A value that is equal to 0 or greater than 2500 was entered at the CHARGAP parameter while the "Timeout within a character string" end condition was set. |
| 80CA | A value that is equal to 0 or greater than 2500 was entered at the IDLETIME parameter while the "Idle line" start condition was set. |
| 80CB | All characters of the character string are marked as "Don't care" even though "Character string" is set as the end condition. |
| 80CC | All characters of the character string are marked as "Don't care" even though "Character string" is set as the start condition. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## SEND_PTP: Transmit send buffer data (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

You use the "SEND_PTP" instruction to start the transmission of data. The "SEND_PTP" instruction does not execute the actual transmission of the data. The data of the send buffer is transmitted to the relevant point-to-point communication module (CM). The CM executes the actual transmission.

### Parameters

The following table shows the parameters of the "SEND_PTP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Enables the requested transmission on a rising edge of this enable input. The content of buffer is transmitted to the point-to-point communication module (CM). |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| BUFFER | Input | VARIANT | I, Q, M, D, L or constant | Pointer to the start address of the send buffer. Boolean values or Array of BOOL are not supported. |
| LENGTH | Input | UINT | I, Q, M, D, L or constant | Length of the send buffer |
| PTRCL | Input | BOOL | I, Q, M, D, L or constant | This parameter selects the buffer for normal point-to-point communication or for specific Siemens protocols implemented in the connected CM.  FALSE = point-to-point operations controlled by the user program (only valid option) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#...) | Description |
| --- | --- |
| 7000 | The send operation is not active. |
| 7001 | The send operation is processing the first call. |
| 7002 | The send operation is processing subsequent calls (queries following the first call). |
| 8080 | The identifier entered for the communications port number is invalid. |
| 8088 | The length of the LENGHT parameter does not correspond to the length of data to be sent. See also: Parameters LENGHT and BUFFER. |
| 80D0 | A new send request was received while a transmission was taking place. |
| 80D1 | The transmission was interrupted because the CTS signal was not confirmed within the specified wait time. |
| 80D2 | The send request was interrupted because the communications partner (DCE) signaled that it was not willing to receive (DSR). |
| 80D3 | The send request was interrupted because the maximum size of the waiting loop was exceeded (more than 1024 Byte). |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

### LENGTH and BUFFER parameters

The minimum data size that can be sent by the "PTP_SEND" instruction is one byte. The parameter BUFFER defines the size of the data to be sent. You can use neither the BOOL nor the Array of BOOL data type for the BUFFER parameter.

| LENGTH parameter | BUFFER parameter | Description |
| --- | --- | --- |
| LENGTH = 0 | Not used | The complete data is sent as defined by the BUFFER parameter. If LENGTH = 0, you do not need to specify the number of bytes transferred. |
| LENGTH &gt; 0 | Elementary data type | The LENGTH value must contain the byte count of this data type. Otherwise, data is not transferred and error 8088 is output. |
| STRUCT | The LENGTH value can contain a byte count that is smaller than the complete byte length of the structure. In this case, only the first LENGTH bytes are transferred. |  |
| ARRAY | The LENGTH value can contain a byte count that is smaller than the complete byte length of the field. In this case, only the field elements that fit completely in the LENGTH bytes are transferred.  The LENGTH value must be a multiple of the byte count of the data elements. Otherwise, STATUS = 8088, ERROR = 1, and no data is transferred. |  |
| STRING | The complete memory arrangement of the character sequence format will be transmitted as well as the information about maximum length of the character string and the actual length of the character string.  The LENGTH value must contain bytes for maximum length, actual length, and the characters of the character string.   With the data type STRING, all lengths and characters have the size of one byte.  If a character string is used for the BUFFER parameter, the LENGTH value must also contain two bytes for the two length fields. |  |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## RCV_PTP: Enable receive messages (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

With the RCV_PTP instruction you enable receipt of a sent message. Each message must be enabled individually. The sent data is only available in the receive area when the message has been acknowledged by the relevant communications partner.

### Parameters

The following table shows the parameters of the "RCV_PTP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L or constant | Enables receipt on a rising edge |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| BUFFER | Input | VARIANT | I, Q, M, D, L or constant | Points to the start address of the receive buffer. Do not use a tag of the type STRING in the receive buffer. |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |
| LENGTH | Output | UINT | I, Q, M, D, L | Length of the message in the receive buffer |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#....) | Description |
| --- | --- |
| 80E0 | Receipt of messages was terminated because the receive buffer is full. |
| 80E1 | Receipt of messages was terminated as a result of a parity error. |
| 80E2 | Receipt of messages was terminated as a result of a framing error. |
| 80E3 | Receipt of messages was terminated as a result of an overflow error. |
| 80E4 | Receipt of messages was terminated because the calculated message length (N+LEN+M) exceeds the size of the receive buffer. |
| 8080 | The identifier entered for the communications port number is invalid. |
| 8088 | A data type STRING is referenced via the BUFFER parameter. |
| 0094 | Receipt of messages was terminated because the maximum character length was received. |
| 0095 | Receipt of messages was terminated as a result of a timeout. |
| 0096 | Receipt of messages was terminated because of a timeout within the character string. |
| 0097 | Receipt of messages was terminated as a result of a reply timeout. |
| 0098 | Receipt of messages was terminated because the "N+LEN+M" length condition has been satisfied. |
| 0099 | Receipt of messages was terminated because the character string defined as the end condition was received. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## RCV_RST: Delete receive buffer (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

With the "RCV_RST" instruction, you delete the receive buffer of a communications partner.

### Parameters

The following table shows the parameters of the "RCV_RST" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Enables deleting of the receive buffer on a rising edge |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction  You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

## SGN_GET: Query RS-232 signals (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

With the "SGN_GET" instruction, you query the current state of several signals of an RS-232 communications module.

### Parameters

The following table shows the parameters of the "SGN_GET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Enables the query on a rising edge |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200)) |
| NDR | Output | BOOL | I, Q, M, D, L | Is set for one cycle if new data are ready for sending and the instruction was executed error-free. |
| DTR | Output | BOOL | I, Q, M, D, L | Data terminal ready, module ready |
| DSR | Output | BOOL | I, Q, M, D, L | Data set ready, communications partner ready |
| RTS | Output | BOOL | I, Q, M, D, L | Send request, module ready to send |
| CTS | Output | BOOL | I, Q, M, D, L | Clear to send, communications partner can receive data (reaction to RTS = ON of the module). |
| DCD | Output | BOOL | I, Q, M, D, L | Data carrier detect, received signal level |
| RING | Output | BOOL | I, Q, M, D, L | Ring display, display of an incoming call |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#....) | Description |
| --- | --- |
| 80F0 | The communication module is an RS-485 module and no signals are available. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## SGN_SET: Set RS-232 signals (S7-1200)

> **Note**
>
> **Use with CM1241**
>
> The use of this instruction with a CM1241 is possible only as of firmware version V2.1 of the module.

### Description

With the "SGN_SET" instruction, you set the status of the output signals of an RS-232 communications module.

### Parameters

The following table shows the parameters of the "SGN_SET" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L or constant | Activates the action on a rising edge  Initial value: FALSE |
| PORT | Input | PORT | I, Q, M, D, L or constant | Identification of the communication port ([HW-ID](Configuring%20automation%20systems.md#addressing-modules-s7-1200))  Initial value: FALSE |
| SIGNAL | Input | BYTE | I, Q, M, D, L or constant | Specifies the signals to be set:  - Set 01H = RTS - Set 02H = DTR - Set 04H = DSR   Initial value: FALSE |
| RTS | Input | BOOL | I, Q, M, D, L or constant | Send request, module ready to send  Initial value: FALSE |
| DTR | Input | BOOL | I, Q, M, D, L or constant | Data terminal ready, module ready  Initial value: FALSE |
| DSR | Input | BOOL | I, Q, M, D, L or constant | Data set ready (applies only to interfaces of the DCE type)  Initial value: FALSE |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or is still executing - 1: Job executed without errors   Initial value: FALSE |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: No error - 1: Error occurred   Initial value: FALSE |
| STATUS | Output | WORD | I, Q, M, D, L | Status of the instruction  Initial value: 0 |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter

| Error code*  (W#16#...) | Description |
| --- | --- |
| 80F0 | The communication module is an RS-485 module and no signals are available. |
| 80F1 | No signals are settable because H/W flow control is enabled. |
| 80F2 | The DSR signal cannot be set because the module is a DTE device. |
| 80F3 | The DTR signal cannot be set because the module is a DCE device. |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

You will find more detailed information on general error codes of the communication instructions in “[General status information of the communications blocks](#general-status-information-of-the-communications-blocks-s7-1200)“.

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

## General status information of the communications blocks (S7-1200)

### General information on execution status of the communications blocks

The following table shows which general information can be output at the STATUS parameter of the communications blocks:

| Error code*  (W#16#....) | Description |
| --- | --- |
| 0000 | No error |
| 7000 | No job processing active. |
| 7001 | Start of job processing. Parameter BUSY = 1, DONE = 0. |
| 7002 | Intermediate call (REQ  irrelevant): Instruction already active; BUSY has the value "1". |
| 8x3A | Invalid pointer at parameter x. |
| 8070 | All internal instance memories are in use. |
| 8080 | The identifier entered for the communications port is invalid |
| 8081 | Timeout, module error, internal error |
| 8082 | Parameter assignment failed because parameter assignment is currently being performed in the background. |
| 8083 | Buffer overflow: The CM or CB has returned a receipt message with a length that is greater than permitted by the length parameter. |
| 8085 | Error specifying the length at the LENGHT parameter. The specified length is "0" or greater than the maximum permitted value. |
| 8090 | Message length invalid, module invalid, message invalid |
| 8091 | Incorrect version in parameterization message |
| 8092 | Invalid record length in parameterization message |
| * The error codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". |  |

---

**See also**

[Switching display formats in the program status](Testing%20the%20user%20program.md#switching-display-formats-in-the-program-status)

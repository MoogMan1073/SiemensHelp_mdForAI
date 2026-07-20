---
title: "Open User Communication (S7-300, S7-400)"
package: ProgKomOpenU34enUS
topics: 21
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Open User Communication (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [Functional description of instructions for Open User Communication via Industrial Ethernet (S7-300, S7-400)](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)
- [Assigning parameters for communications connections with TCP and ISO on TCP (S7-300, S7-400)](#assigning-parameters-for-communications-connections-with-tcp-and-iso-on-tcp-s7-300-s7-400)
- [Assigning parameters for the local communications access point with UDP (S7-300, S7-400)](#assigning-parameters-for-the-local-communications-access-point-with-udp-s7-300-s7-400)
- [Structure of the address information for the remote partner with UDP (S7-300, S7-400)](#structure-of-the-address-information-for-the-remote-partner-with-udp-s7-300-s7-400)
- [Relationship between CPU and protocol variant used (connection_type) and transferable data length (S7-300, S7-400)](#relationship-between-cpu-and-protocol-variant-used-connection_type-and-transferable-data-length-s7-300-s7-400)
- [Examples of parameters for communications connections (S7-300, S7-400)](#examples-of-parameters-for-communications-connections-s7-300-s7-400)
- [TCON: Establish communication connection (S7-300, S7-400)](#tcon-establish-communication-connection-s7-300-s7-400)
- [TDISCON: Terminate communication connection (S7-300, S7-400)](#tdiscon-terminate-communication-connection-s7-300-s7-400)
- [TSEND: Send data via communication connection (S7-300, S7-400)](#tsend-send-data-via-communication-connection-s7-300-s7-400)
- [TRCV: Receive data via communication connection (S7-300, S7-400)](#trcv-receive-data-via-communication-connection-s7-300-s7-400)
- [TUSEND: Send data via Ethernet (UDP) (S7-300, S7-400)](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)
- [TURCV: Receive data via Ethernet (UDP) (S7-300, S7-400)](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)
- [IP_CONF: Change IP configuration parameters (S7-300, S7-400)](#ip_conf-change-ip-configuration-parameters-s7-300-s7-400)
- [Data exchange using FETCH and WRITE (S7-300, S7-400)](#data-exchange-using-fetch-and-write-s7-300-s7-400)

## Overview (S7-300, S7-400)

### Open User Communication via Industrial Ethernet

The following instructions and UDTs are available for exchanging data with other communication partners by means of the user program via Ethernet (TCP, ISO-on-TCP, UDP protocols):

- Connection-oriented protocols: TCP as per RFC 793, ISO on TCP as per RFC 1006:

  - UDT 65 "[TCON_PAR](#assigning-parameters-for-the-local-communications-access-point-with-udp-s7-300-s7-400)" with the data structure for assigning connection parameters
  - UDT 651 to UDT 656 with protocol-specific defaults
  - "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" for establishing the connection
  - "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)" for terminating the connection
  - "[TSEND](#tsend-send-data-via-communication-connection-s7-300-s7-400)" for sending data
  - "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" for receiving data
- Connectionless protocol: UDP as per RFC 768

  - UDT 65 "[TCON_PAR](#assigning-parameters-for-the-local-communications-access-point-with-udp-s7-300-s7-400)" with the data structure for assigning parameters of the local communications access point
  - UDT 657 with protocol-specific defaults
  - UDT 66 "[TCON_ADR](#structure-of-the-address-information-for-the-remote-partner-with-udp-s7-300-s7-400)" with the data structure for assigning addressing parameters of the remote partner
  - UDT 661 with protocol-specific defaults
  - "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" for setting up the local communication access point
  - "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)" for canceling the local communication access point
  - "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)" for sending data
  - "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)" for receiving data

## Functional description of instructions for Open User Communication via Industrial Ethernet (S7-300, S7-400)

### Connection-oriented and connectionless protocols

The following protocol variants are distinguished in the data communication:

- Connection-oriented protocol variants:

  They establish a logical connection to the communication partner before data transmission is started. After the data transmission is complete, they then terminate the connection, if necessary. Connection-oriented protocols are used for data transmission when reliable, guaranteed delivery is of particular importance. Usually, there can be several logical connections over one physical line.

  With the instructions for Open User Communication via Industrial Ethernet, the following connection-oriented protocols are supported:

  - TCP as per RFC 793
  - ISO on TCP as per RFC 1006
- Connectionless protocol variants:

  They work without a connection. There is thus no establishment and termination of a connection with a remote partner. Unacknowledged connectionless protocols transmit the data to the remote partner and are therefore unprotected. This means the data can be lost without any indication at the block.

  With the instructions for Open User Communication via Industrial Ethernet, the following connectionless protocols are supported:

  - UDP per RFC 768 (broadcast or unicast, no support for multicast)

The functional description of the instructions depends on the protocol variant being used. This is discussed in more detail in the following section.

### Receive area

This term will be used repeatedly in the following sections. This means the area in which the instruction enters the received data.

The receive area is specified by the following two variables:

- Pointer to the start of the area
- Length of the area

Depending on the protocol variant being used, the length of the area is specified either by the LEN parameter (if LEN <> 0) or the length information of the DATA parameter (if LEN = 0).

The following data types are permitted in the ANY pointer: BOOL, BYTE, CHAR, WORD, INT, DWORD, DINT, REAL, DATE, TIME_OF_DAY, TIME, S5TIME, DATE_AND_TIME.

### TCP

During data transmission, no information about the length or about the start and end of a message is transmitted. This is not a problem during sending because the sender knows how many data bytes it will be sending. However, the receiver has no means of detecting where one message ends in the data stream and the next one begins. We therefore recommend that you select the size of receive area of the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction to match the value of the LEN parameter of the "[TSEND](#tsend-send-data-via-communication-connection-s7-300-s7-400)" instruction on the communication partner (number of bytes to be sent).

- Date reception in ad-hoc mode:

  The receive area is identical with the area specified by the DATA parameter of the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction.

  - Immediately after receiving a block of data, the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction transfers this data block to the receive area and sets NDR to "1". The maximum length is 8192 bytes.
  - If you have selected a receive area that is longer than the sent data, the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction copies all received data completely in the receive area. It then sets NDR to TRUE and writes the length of the sent data to RCVD_LEN.
  - If you have selected a receive area that is smaller than the sent data, the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction copies as many bytes into the receive area until it is full. It then sets NDR to TRUE and writes the length of the receive area to RCVD_LEN. With each subsequent call, you receive a further block of the sent data.
- Data reception with specified length:

  - The receive area is formed by the DATA parameters (start address of the receive area) and LEN (length of the receive area) by "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)".
  - If data are received that do not completely fill the receive area, then these data will not be made available to you initially. They will only become available when additional data has filled up the receive area completely. Please note that in this case data from two different send jobs are located in the same receive area. If you cannot determine the end of the first message or the start of the second message, you will not be able to recognize the first or the second message.
  - If you have selected a receive area that is smaller than the sent data, the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction copies as many bytes into the receive area until it is completely full.
  - If "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" has completely filled the receive area, it will set NDR to TRUE and describes RCVD_LEN with the value of LEN. Thus with each subsequent call, you get an additional block of the sent data.

### ISO on TCP

During data transfer, information on the length and end of a message is also transferred.

If you have selected a receive area that is longer than the sent data, then the "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" instruction enters all the sent data completely in the receive area. It then sets NDR to TRUE and writes the length of the sent data to RCVD_LEN.

If you have selected a receive area shorter than the length of the sent data, then "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)" will not copy any data to the receive area and returns the following error information: ERROR=1, STATUS=W#16#8088.

### UDP

There is no connection establishment as is the case with the TCP and ISO on TCP protocols. You must therefore specify a reference to the address parameters of the recipient (IP address and port no.) when you call the send block "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)". In the same way, on completion of the receive block "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)", you will receive a reference to the address parameters of the sender (IP address and port no.).

- To use the "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)" and "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)" instructions, you must first call the "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" instruction both at the sender and receiver end to set up the local communication access point.
- Each time you call "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)", you can reference the remote partner once again by specifying its IP address and its port number.
- During data transfer, information on the length and end of a message is also transferred.

If you have selected a receive area that is longer than the sent data, "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)" will copy all sent data completely to the receive area. It then sets NDR to TRUE and writes the length of the sent data to RCVD_LEN.

If you have selected a receive area shorter than the length of the sent data, TURCV does not copy any data to the receive area and returns the following error information: ERROR = 1, STATUS = W#16#8088.

### Port numbers for TCP and UDP

The address assignment for a connection is made as follows:

- With TCP:

  - Active connection: Via the remote IP address, the remote port and the local port (specify the port number of the local port explicitly or let the operating system set it).
  - Passive connection: Via the local port. If you want to use the local port several times, you have to either pre-define the remote IP address or the remote IP address together with the remote port.
- With UDP: Via the remote IP address, the remote port and the local port (specify the port number of the local port explicitly).

The areas listed below apply to the local port. These areas apply to the remote port of the remote partner is an S7 CPU. Otherwise, there are no restrictions for the remote port.

- For CPUs 31x-2 PN/DP up to and including firmware version V2.6 and CPUs 41x-3 PN/DP up to and including firmware version V5.1:

  - Permissible port numbers in the configuration (UDT 65): 2000 to 5000
  - The operating system assigns a port from the dynamic range of numbers between 49152 and 65534 if a port number is not assigned explicitly.
- For CPUs 31x-2 PN/DP as of firmware version V2.7 and CPUs 41x-3 PN/DP as of firmware version V5.2:

  - Permissible port numbers in the configuration (UDT 65): 1 to 49151  
    We recommend restricting the port numbers from 2000 to 5000, since Siemens reserves ports from the number ranges 1 to 1999 and 5001 to 49151 for use by the system.
  - The operating system assigns a port from the dynamic range of numbers between 49152 and 65534 if a port number is not assigned explicitly.
- For CPUs 31x-2 PN/DP as of firmware version V3.2, CPUs 41x-3 PN/DP as of firmware version V6.0 and CPUs 41x-5H PN/DP as of firmware version V6.0:

  - A port can be used several times.

You can find the port numbers reserved by the system in the following list:

| Protocol | Port number | Service |
| --- | --- | --- |
| - | 0 | (This port is reserved. It cannot be used.) |
| TCP | 20 and 21 | FTP |
| TCP | 25 | SMTP |
| TCP | 80 | HTTP |
| TCP | 102 | RFC 1006 |
| UDP | 135 | RPC-DCOM |
| UDP | 161 | SNMP REQUEST |
| TCP, UDP | 34962 | PNIO |
| TCP, UDP | 34963 | PNIO |
| TCP, UDP | 34964 | PNIO |
| UDP | 65532 | NTP |
| UDP | 65533 | NTP |
| UDP | 65534 | NTP |
| UDP | 65535 | NTP |

Also see http://www.iana.org/assignments/port-numbers.

> **Note**
>
> Do not use port numbers reserved for the system.
>
> Identical port numbers must not be used for active and passive connection establishment in a device.

## Assigning parameters for communications connections with TCP and ISO on TCP (S7-300, S7-400)

### Data block for assigning parameters

To be able to assign parameters for TCP and ISO on TCP for communication connections, create a DB that contains the data structure from the UDT 65 "TCON_PAR". This data structure contains the parameters necessary for configuring the connection. You will need such a data structure for every connection. You can assemble this structure in a shared DB.

The CONNECT connection parameter of the "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" instruction contains a reference to the address of the associated connection description (e.g. P#DB100.DBX0.0 byte 64).

### Form of the connection description (UDT 65)

| Byte | Parameters | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| 0 to 1 | block_length | WORD | W#16#40 | Length of UDT 65: 64 bytes (fixed) |
| 2 to 3 | id | WORD | W#16#0001 | Reference to the connection (range of values: W#16#0001 to W#16#0FFF) You must specify the value of this parameter in the respective block for the ID. |
| 4 | connection_type | BYTE | B#16#11 | Protocol variant:  - B#16#11: TCP (not possible when using a CP) - B#16#12: ISO on TCP |
| 5 | active_est | BOOL | FALSE | ID for the manner in which the connection is established:  - FALSE: Passive connection establishment - TRUE: Active connection establishment |
| 6 | local_device_id | BYTE | B#16#02 | - B#16#00: Communication via CP 443-1EX (only with S7-400 and connection_type = B#16#12). Permitted CPs: CP443-1EX4x, CP443-1EX20, CP443-1GX20, CP443-1EX30, CP443-1GX30 - B#16#01: Communication via IE interface on interface slot 1 (IF1) for WinAC RTX (only TCP) - B#16#02: Communication over the integrated IE interface with CPUs 315-2 PN/DP and 317-2 PN/DP - B#16#03: Communication via the integrated IE-interface with CPU 319-3 PN/DP - B#16#05: Communication via the integrated IE interface with CPUs 414-3 PN/DP, 416-3 PN/DP, 416-3F PN/DP and 41x-5H PN/DP (Rack 0) - B#16#06: Communication via IE interface on interface slot 2 (IF2) for WinAC RTX (only TCP) - B#16#0B: Communication via IE interface on interface slot 3 (IF3) for WinAC RTX (only TCP) - B#16#0F: Communication via IE interface on interface slot 4 (IF4) for WinAC RTX (only TCP) - B#16#15: Communication via the integrated IE interface with CPUs 41x-5H PN/DP (Rack 1) |
| 7 | local_tsap_id_len | BYTE | B#16#02 | Length of parameter local_tsap_id used; possible values:  - 0 or 2, for connection_type = B#16#01 (active end: 0, passive end: 2) - 0 or 2, for connection_type = B#16#11 (active end: 0 or 2, passive end: 2) - 2 to 16. if connection_type = B#16#12 |
| 8 | rem_subnet_id_len | BYTE | B#16#00 | This parameter is currently not used. Assign with B#16#00. |
| 9 | rem_staddr_len | BYTE | B#16#00 | Length of the address of the remote connection end point:  - 0: unspecified, i.e. parameter rem_staddr is irrelevant. - 4: Valid IP address in the rem_staddr parameter |
| 10 | rem_tsap_id_len | BYTE | B#16#00 | Length of parameter rem_tsap_id used; possible values:  - 0 or 2, for connection_type = B#16#01  For the passive end only value B#16#00 is permitted. - 0 or 2. if connection_type = B#16#11   Only the value B#16#00 is permissible for the passive side (only for S7-400). - 0 or 2 to 16, if connection_type = B#16#12 (active end: 2 to 16; passive end: 0 or 2 to 16, 0 means unspecified) |
| 11 | next_staddr_len | BYTE | B#16#00 | length of the next_staddr parameter used (only relevant for ISO-on-TCP) |
| 12 to 27 | local_tsap_id | ARRAY [1..16] of BYTE | B#16#07 B#16#D0 B#16#00 ... | With connection_type =  - B#16#11: local port no. (possible values, see: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)), local_tsap_id[1] = high byte of the port no. in hexadecimal format, local_tsap_id[2] = low byte of the port number in hexadecimal format,  local_tsap_id[3-16] = B#16#00 - B#16#12: local TSAP ID: see below. - B#16#01: local port no. (possible values, see: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)), local_tsap_id[1] = low byte of the port no. in hexadecimal format, local_tsap_id[2] = high byte of the port number in hexadecimal format,  local_tsap_id[3-16] = B#16#00   Note: If there are multiple connections to the same communication partner, you have to ensure that each value of local_tsap_id that you use in your CPU is unique. |
| 28 to 33 | rem_subnet_id | ARRAY [1..6] of BYTE | B#16#00 ... | This parameter is currently not used. Assign 0 to it. |
| 34 to 39 | rem_staddr | ARRAY [1..6] of BYTE | B#16#00 ... | IP address of the remote connection end point, for example, 192.168.0.1:  With connection_type =  - B#16#1x: rem_staddr[1] = B#16#C0 (192), rem_staddr[2] = B#16#A8 (168), rem_staddr[3] = B#16#00 (0), rem_staddr[4] = B#16#01 (1), rem_staddr[5-6]= B#16#00 (reserved) |
| 40 to 55 | rem_tsap_id | ARRAY [1..16] of BYTE | B#16#00 ... | With connection_type =  - B#16#11: remote port no. (possible values, see: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)), rem_tsap_id[1] = high byte of the port no. in hexadecimal format, rem_tsap_id[2] = low byte of the port number in hexadecimal format,  rem_tsap_id[3-16] = B#16#00 - B#16#12: remote TSAP ID: see below. |
| 56 to 61 | next_staddr | ARRAY [1..6] of BYTE | B#16#00 ... | With local_device_id =  - B#16#00: next_staddr[1]: Rack and slot of the corresponding (local) CP (bits 0 to 4: slot, bits 5 to 7: rack number) next_staddr[2-6]: B#16#00 - B#16#02, B#16#03, B#16#05:  next_staddr[1-6]: B#16#00 - B#16#01, B#16#06, B#16#0B, B#16#0F:  next_staddr[1-6]: B#16#00 (in this case is next_staddr_len=B#16#00) |
| 62 to 63 | spare | WORD | W#16#0000 | Standby: Assign "0" to this parameter. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Length and form of the local and remote TSAP ID for ISO on TCP

- Active connection establishment:

  - Remote TSAP-ID:  
    All character strings with a length between 1 and 16 bytes are permitted. Each character can have a value between B#16#00 and B#16#FF.
  - Remote TSAP-ID:  
    For integrated IE interfaces, all character strings with a length between 1 and 16 bytes are permitted. Each character can have a value between B#16#00 and B#16#FF.
- Passive connection establishment:

  - Remote TSAP-ID:  
    All character strings with a length between 0 and 16 bytes are permitted. Each character can have a value between B#16#00 and B#16#FF.
  - Local TSAP-ID:

| loc_tsap_id_len | local_tsap_id[1] | local_tsap_id[2] | local_tsap_id[3 to 16] |
| --- | --- | --- | --- |
| 2 | B#16#E0 (connection type T connection) | 0 (only for integrated IE interfaces) or rack and slot of the local CPU (bits 0 to 4 slot, bits 5 to 7 rack number) | Does not exist |
| > 2 | B#16#E0 (connection type T connection) | 0 (only for integrated IE interfaces) or rack and slot of the local CPU (bits 0 to 4 slot, bits 5 to 7 rack number) | TSAP extension |
|  | Only for integrated IE interfaces: a ASCII character (B#16#20 to B#16#7E) | irrelevant | TSAP extension |

### CPU dependencies for protocol variants TCP and ISO on TCP

To determine which protocol variants (TCP and ISO on TCP) can be used on which CPU, refer to the following paragraph:

[Relationship between CPU and protocol variant used (connection_type) and transferable data length](#relationship-between-cpu-and-protocol-variant-used-connection_type-and-transferable-data-length-s7-300-s7-400).

For information on the number of possible connections, please refer to the specifications for your CPU.

### Connection establishment

A communication partner A must trigger the active connection establishment. A communication partner B must trigger the passive connection establishment. If both communication partners have triggered their connection establishment then the operating system can completely establish the communication connection.

When assigning parameters to the connection specify which communication partner will activate the connection establishment and which will execute a passive communication establishment on the request of the communication partner.

In UDP, both partners must initiate passive connection establishment.

## Assigning parameters for the local communications access point with UDP (S7-300, S7-400)

### Data structure for configuring the local communications access point

To assign parameters for the local communications access point, create a DB that contains the data structure from the UDT 65 "TCON_PAR". This data structure contains the parameters necessary for configuring the connection between the user program and the communications layer of the operating system.

The CONNECT parameter of the "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" instruction contains a reference to the address of the associated connection description (e.g. P#DB100.DBX0.0 byte 64).

### Form of the connection description for UDP (UDT 65)

| Byte | Parameters | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 0 to 1 | block_length | WORD | W#16#40 | Length of UDT 65: 64 bytes (fixed) |
| 2 to 3 | id | WORD | W#16#0001 | Reference to this connection between the user program and the communications level of the operating system (range of values: W#16#0001 to W#16#0FFF) You must specify the value of this parameter in the respective block for the ID. |
| 4 | connection_type | BYTE | B#16#13 | Protocol variant:  - B#16#13: UDP (not possible when using a CP) |
| 5 | active_est | BOOL | FALSE | ID for the manner in which the connection is established: You must assign FALSE to this parameter. |
| 6 | local_device_id | BYTE | B#16#02 | - B#16#01: Communication via IE interface on interface slot 1 (IF1) for WinAC RTX - B#16#02: Communication via the integrated IE-interface with CPU 317-2 PN/DP - B#16#03: Communication via the integrated IE-interface with CPU 319-3 PN/DP - B#16#04: for Sinumerik 840D sl - B#16#05: Communication via the integrated IE interface with CPUs 414-3 PN/DP, 416-3 PN/DP, 416-3F PN/DP and 41x-5H PN/DP (Rack 0) - B#16#06: Communication via IE interface on interface slot 2 (IF2) for WinAC RTX - B#16#0B: Communication via IE interface on interface slot 3 (IF3) for WinAC RTX - B#16#0F: Communication via IE interface on interface slot 4 (IF4) for WinAC RTX - B#16#15: Communication via the integrated IE interface with CPUs 41x-5H PN/DP (Rack 1) |
| 7 | local_tsap_id_len | BYTE | B#16#02 | Length of local_tsap_id parameter (local port) used; 2 bytes |
| 8 | rem_subnet_id_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| 9 | rem_staddr_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| 10 | rem_tsap_id_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| 11 | next_staddr_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| 12 to 27 | local_tsap_id | ARRAY [1..16] of BYTE | B#16#07 B#16#D0 B#16#00 ... | Local port no. (for possible values, see: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)), local_tsap_id[1] = high byte of the port no. in hexadecimal format, local_tsap_id[2] = low byte of the port no. in hexadecimal format,  local_tsap_id[3-16] = B#16#00 (reserved)  Note: Ensure that each value of local_tsap_id that you use in your CPU is unique. |
| 28 to 33 | rem_subnet_id | ARRAY [1..6] of BYTE | B#16#00 ... | This parameter is not used. Assign "0" to it. |
| 34 to 39 | rem_staddr | ARRAY [1..6] of BYTE | B#16#00 ... | This parameter is not used. Assign "0" to it. |
| 40 to 55 | rem_tsap_id | ARRAY [1..16] of BYTE | B#16#00 ... | This parameter is not used. Assign "0" to it. |
| 56 to 61 | next_staddr | ARRAY [1..6] of BYTE | B#16#00 ... | This parameter is not used. Assign "0" to it. |
| 62 to 63 | spare | WORD | W#16#0000 | Standby: Assign "0" to this parameter. |
|  |  |  |  |  |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### CPU dependency of the UDP protocol variant

To determine which CPUs are suitable for use with the UDP protocol variant, refer to the following paragraph:

[Relationship between CPU and protocol variant used (connection_type) and transferable data length](#relationship-between-cpu-and-protocol-variant-used-connection_type-and-transferable-data-length-s7-300-s7-400)

For information on the number of possible connections between the user program and the communications layer of the operating system, please refer to the specifications for your CPU.

### Configuring the local communications access point

Each communications partner must configure its local communications point independently of the other partner. This pertains to establishing the connection between the user program and communications layer of the operating system.

In UDP, both partners must initiate passive connection establishment.

## Structure of the address information for the remote partner with UDP (S7-300, S7-400)

### Overview

- With "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)", you transfer the address information of the receiver at the ADDR parameter. This address information must have the structure specified below.
- With "[TURCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)", you receive the address of the sender of the received data at the ADDRparameter. This address information must have the structure specified below.

### Data block for the address information of the remote partner

You must create a DB that contains one or more data structures as per UDT 66 "TADDR_PAR".

In parameter ADDR of "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)", you transfer a pointer to the address of the associated remote partner (e.g. P#DB100.DBX0.0 byte 8). This pointer is received in the ADDRparameter of "[TURCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)".

### Form of the address information for the remote partner (UDT 66)

| Byte | Parameter | Data type | Initial value | Description |
| --- | --- | --- | --- | --- |
| 0 to 3 | rem_ip_addr | ARRAY [1..4] of BYTE | B#16#00 ... | IP address of the remote partner, e.g. 192.168.2.3:  - rem_ip_addr[1] = B#16#C0 (192) - rem_ip_addr[2] = B#16#A8 (168) - rem_ip_addr[3] = B#16#02 (2) - rem_ip_addr[4] = B#16#03 (3) |
| 4 to 5 | rem_port_nr | ARRAY [1..2] of BYTE | B#16#00 ... | remote port no. (possible values see: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400))  - rem_port_nr[1] = high byte of the port no. in hexadecimal notation - rem_port_nr[2] = low byte of port no. in hexadecimal notation |
| 6 to 7 | spare | ARRAY [1..2] of BYTE | B#16#00 ... | Standby: Assign "0" to this parameter. |

## Relationship between CPU and protocol variant used (connection_type) and transferable data length (S7-300, S7-400)

### Relationship between CPU and protocol variant used (connection_type) and transferable data length

The table below shows which protocol variants you can use on which CPU, and which data lengths you can transfer.

| Protocol variant | Parameter "connection _type" in  UDT 65 | CPU | Data length  in bytes for communication  over integrated  IE interface | Data length in bytes for communication via CP |
| --- | --- | --- | --- | --- |
| TCP | B#16#11 | CPUs 31x-2 PN/DP as of firmware version V2.4 | 1 to 8192 | - |
| CPUs 31x-2 PN/DP as of firmware version V3.1 | 1 to 32767 |  |  |  |
| CPUs 31x-3 PN/DP as of firmware version V3.2 | 1 to 32767 |  |  |  |
| CPUs 41x-3 PN/DP | 1 to 32767 | - |  |  |
| CPUs 41x-5H PN/DP | 1 to 32767 | - |  |  |
| B#16#01 | CPUs 31x-2 PN/DP | 1 to 1472 | - |  |
|  |  |  |  |  |
| ISO on TCP | B#16#12 | CPUs 31x-2 PN/DP as of firmware version V2.4 | 1 to 8192 | - |
| CPUs 31x-2 PN/DP as of firmware version V3.1 | 1 to 32767 |  |  |  |
| CPUs 31x-3 PN/DP as of firmware version V3.2 | 1 to 32767 |  |  |  |
| CPUs 41x as of firmware version V4.1 (without CPUs 41x-4H) | - | 1 to 1452 |  |  |
| CPUs 41x-3 PN/DP | 1 to 32767 | 1 to 1452 |  |  |
| CPUs 41x-5H PN/DP | 1 to 32767 | 1 to 1452 |  |  |
|  |  |  |  |  |
| UDP | B#16#13 | CPUs 31x-2 PN/DP as of firmware version V2.4, CPUs 41x-3 PN/DP and 41x-5H PN/DP | 1 to 1472 | - |

## Examples of parameters for communications connections (S7-300, S7-400)

### Example 1: Communication via ISO on TCP and CP 443-1 between two S7-400 CPUs

The two communication partners are two CPUs 414-2. The communication is handled by two CPs 443-1.

The following table shows the most important data for both communications partners:

| Property | Communication partner A: CPU 414-2 with CP 443-1 | Communication partner B: CPU 414-2 with CP 443-1 |
| --- | --- | --- |
| Connection establishment | active | passive |
| IP address | 192.168.4.14 | 192.168.4.16 |
| Physical address of the CPU | Rack 0, slot 3 | Rack 0, slot 4 |
| Physical address of the associated CP | Rack 0, slot 6 | Rack 1, slot 8 |
| Local TSAP-ID (Note: the coding of the actual TSAP to distinguish the connection occurs as of the third byte) | 0xE0 03 54 43 50 2D 31 | 0xE0 04 54 43 50 2D 31 |

The following table shows the parameter entries in the DB relevant for active establishment of a connection by communication partner A:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#0414 | Reference to this connection |
| connection_type | BYTE | B#16#12 | Protocol variant: ISO on TCP |
| active_est | BOOL | TRUE | Active connection establishment |
| local_device_id | BYTE | B#16#00 | Communication AS-internal via CP |
| local_tsap_id_len | BYTE | B#16#07 | Length of parameter local_tsap_id |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#07 | Length of parameter rem_tsap_id |
| next_staddr_len | BYTE | B#16#01 | Length of parameter next_staddr |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#E0 - local_tsap_id[2] = B#16#03 - local_tsap_id[3] = B#16#54 (ASCII equivalent of "T") - local_tsap_id[4] = B#16#43 (ASCII equivalent of "C") - local_tsap_id[5] = B#16#50 (ASCII equivalent of "P") - local_tsap_id[6] = B#16#2D (ASCII equivalent of "-") - local_tsap_id[7] = B#16#31 (ASCII equivalent of "1") - local_tsap_id[8-16] = B#16#00 | local TSAP-ID: 0xE0035443502D31 |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.4.16"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#04 (4) - rem_staddr[4] = B#16#10 (16) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |
| rem_tsap_id | ARRAY [1..16] of BYTE | - rem_tsap_id[1] = B#16#E0 - rem_tsap_id[2] = B#16#04 - rem_tsap_id[3] = B#16#54   (ASCII equivalent of "T") - rem_tsap_id[4] = B#16#43    (ASCII equivalent of "C") - rem_tsap_id[5] = B#16#50    (ASCII equivalent of "P") - rem_tsap_id[6] = B#16#2D   (ASCII equivalent of "-") - rem_tsap_id[7] = B#16#31   (ASCII equivalent of "1") - rem_tsap_id[8-16] = B#16#00 | remote TSAP-ID: 0xE0045443502D31 |
| next_staddr | ARRAY [1..6] of BYTE | - next_staddr[1] = B#16#06 - next_staddr[2-6] = B#16#00 | Rack = 0, slot = 6  (bits 7 to 5: Rack no., bits 4 to 0: slot no.) |

The following table shows the parameter entries in the DB relevant for passive establishment of a connection by communication partner B:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#0416 | Reference to this connection |
| connection_type | BYTE | B#16#12 | Protocol variant: ISO on TCP |
| active_est | BOOL | FALSE | Passive connection establishment |
| local_device_id | BYTE | B#16#00 | Communication AS-internal via CP |
| local_tsap_id_len | BYTE | B#16#07 | Length of parameter local_tsap_id used |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#07 | Length of parameter rem_tsap_id |
| next_staddr_len | BYTE | B#16#01 | Length of parameter next_staddr |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#E0 - local_tsap_id[2] = B#16#04 - local_tsap_id[3] = B#16#54   (ASCII equivalent of "T") - local_tsap_id[4] = B#16#43   (ASCII equivalent of "C") - local_tsap_id[5] = B#16#50    (ASCII equivalent of "P") - local_tsap_id[6] = B#16#2D (ASCII equivalent of "-") - local_tsap_id[7] = B#16#31   (ASCII equivalent of "1") - local_tsap_id[8-16] = B#16#00 | local TSAP-ID: 0xE0045443502D31 |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.4.14"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#04 (4) - rem_staddr[4] = B#16#0E (14) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |
| rem_tsap_id | ARRAY [1..16] of BYTE | - rem_tsap_id[1] = B#16#E0 - rem_tsap_id[2] = B#16#03 - rem_tsap_id[3] = B#16#54   (ASCII equivalent of "T") - rem_tsap_id[4] = B#16#43   (ASCII equivalent of "C") - rem_tsap_id[5] = B#16#50   (ASCII equivalent of "P") - rem_tsap_id[6] = B#16#2D   (ASCII equivalent of "-") - rem_tsap_id[7] = B#16#31   (ASCII equivalent of "1") - rem_tsap_id[8-16] = B#16#00 | remote TSAP-ID: 0xE0035443502D31 |
| next_staddr | ARRAY [1..6] of BYTE | - next_staddr[1] = B#16#28 - next_staddr[2-6] = B#16#00 | Rack = 1, slot = 8  (bits 7 to 5: Rack no., bits 4 to 0: slot no.) |

### Example 2: Communication over TCP and integrated PROFINET interfaces between an S7-400 CPU and an S7-300 CPU

One partner is a CPU 416-3 PN/DP, the other is a CPU 319-3 PN/DP. The following table shows the most important data for both communications partners:

| Property | Communication partner A: CPU 416-3 PN/DP | Communication partner B: CPU 319-3 PN/DP |
| --- | --- | --- |
| Connection establishment | active | passive |
| IP address | 192.168.3.142 | 192.168.3.125 |
| Local port no. | irrelevant | 2005 |

The following table shows the parameter entries in the DB relevant for active establishment of a connection by communication partner A:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#0014 | Reference to this connection |
| connection_type | BYTE | B#16#11 | Protocol variant: TCP |
| active_est | BOOL | TRUE | Active connection establishment |
| local_device_id | BYTE | B#16#05 | Communication via the integrated Ethernet interface with S7-400 CPUs |
| local_tsap_id_len | BYTE | B#16#00 (only this value is possible) | Parameter local_tsap_id is not used |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#02 (only this value is possible) | Length of parameter rem_tsap_id |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.3.125"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#03 (3) - rem_staddr[4] = B#16#7D (125) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |
| rem_tsap_id | ARRAY [1..16] of BYTE | "2005"  - rem_tsap_id[1] = B#16#07 - rem_tsap_id[2] = B#16#D5 - rem_tsap_id[3-16] = B#16#00 | Remote port no.: 2005 = W#16#07D5 |

The following table shows the parameter entries in the DB relevant for passive establishment of a connection by communication partner B:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#000F | Reference to this connection |
| connection_type | BYTE | B#16#11 | Protocol variant: TCP |
| active_est | BOOL | FALSE | Passive connection establishment |
| local_device_id | BYTE | B#16#03 | Communication via the integrated Ethernet interface with the CPU 319-3 PN/DP |
| local_tsap_id_len | BYTE | B#16#02 (only this value is possible) | Length of parameter local_tsap_id |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#00 (only this value is possible) | Length of parameter rem_tsap_id |
| local_tsap_id | ARRAY [1..16] of BYTE | "2005"  - local_tsap_id[1] = B#16#07 - local_tsap_id[2] = B#16#D5 - local_tsap_id[3-16] = B#16#00 | Local port no.: 2005 = W#16#07D5 |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.3.142"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#03 (3) - rem_staddr[4] = B#16#8E (142) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |

### Example 3: Communication over UDP and integrated PROFINET interfaces between an S7-300 CPU and an S7-400 CPU

One partner is a CPU 319-3 PN/DP, the other is a CPU 414-3 PN/DP. The following table shows the most important data for both communications partners:

| Property | Communication partner A: CPU 319-3 PN/DP | Communication partner B: CPU 414-3 PN/DP |
| --- | --- | --- |
| Sender/receiver | Sender | Receiver |
| IP address | 192.168.3.142 | 192.168.3.125 |
| Local port no. | 2004 | 2005 |

The following table shows the parameter entries in the DB relevant for the sender (communication partner A) for assigning parameters to the local communications access point:

| Parameter | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#0014 | Reference to this connection between the application program and the communication layer of the operating system. |
| connection_type | BYTE | B#16#13 | Protocol variant: UDP |
| active_est | BOOL | FALSE | Only this value can be used with the protocol variant UDP. |
| local_device_id | BYTE | B#16#03 | Communication via the integrated Ethernet interface with the CPU 319-3 PN/DP |
| local_tsap_id_len | BYTE | B#16#02 | Length of parameter local_tsap_id |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#07 - local_tsap_id[2] = B#16#D4 - local_tsap_id[3-16] = B#16#00 | Local port no.: 2004 = W#16#07D4 |

The following table shows the parameter entries in the DB relevant for the receiver (communication partner B) for assigning parameters to the local communications access point:

| Parameter | Data type | Value in example | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#000F | Reference to this connection between the application program and the communication layer of the operating system. |
| connection_type | BYTE | B#16#13 | Protocol variant: UDP |
| active_est | BOOL | FALSE | Only this value can be used with the protocol variant UDP. |
| local_device_id | BYTE | B#16#05 | Communication via the integrated Ethernet interface with S7-400 CPUs |
| local_tsap_id_len | BYTE | B#16#02 | Length of parameter local_tsap_id |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#07 - local_tsap_id[2] = B#16#D5 - local_tsap_id[3-16] = B#16#00 | Local port no.: 2005 = W#16#07D5 |

When "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)" is called on the sender, you transfer the following address parameters of the receiver in a DB:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| rem_ip_addr | ARRAY [1..4] of BYTE | - rem_ip_addr[1] = B#16#C0 (192) - rem_ip_addr[2] = B#16#A8 (168) - rem_ip_addr[3] = B#16#3 (3) - rem_ip_addr[4] = B#16#7D (125) | IP address of the receiver: 192.168.3.125 |
| rem_port_nr | ARRAY [1..2] of BYTE | - rem_port_nr[1] = B#16#07 - rem_port_nr[2] = B#16#D5 | Port no. of the receiver: 2005 = W#16#07D5 |

When "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)" is called on the receiver, you receive the following address parameters of the sender in a DB:

| Parameters | Data type | Value in example | Description |
| --- | --- | --- | --- |
| rem_ip_addr | ARRAY [1..4] of BYTE | - rem_ip_addr[1] = B#16#C0 (192) - rem_ip_addr[2] = B#16#A8 (168) - rem_ip_addr[3] = B#16#3 (3) - rem_ip_addr[4] = B#16#8E (142) | IP address of the sender: 192.168.3.142 |
| rem_port_nr | ARRAY [1..2] of BYTE | - rem_port_nr[1] = B#16#07 - rem_port_nr[2] = B#16#D4 | Port no. of the sender: 2004 = W#16#07D4 |

### Example 4: Communication over ISO on TCP and integrated PROFINET interfaces between two S7-400 CPUs

One of the communication partners is a CPU 414-3 PN/DP as of firmware version V5.0, the other is a CPU 416-3 PN/DP with firmware version V5.0. Communication is handled over the integrated PROFINET interfaces.

The following table shows the most important data of the two communication partners.

| Property | Communication partner A: CPU 414-3 PN/DP | Communication partner B: CPU 416-3 PN/DP |
| --- | --- | --- |
| Sender/receiver | Sender | Receiver |
| Connection establishment | passive | active |
| IP address | 192.168.0.14 | 192.168.0.16 |

The following table shows all parameter entries of communication partner A in the corresponding DB.

| Parameter | Data type | Value in example | Description |
| --- | --- | --- | --- |
| block_length | WORD | W#16#40 | Length of UDT65: 64 bytes (fixed) |
| id | WORD | W#16#0001 | Reference to this connection |
| connection_type | BYTE | B#16#12 | Protocol variant:  - B#16#12: ISO on TCP |
| active_est | BOOL | FALSE | Passive connection establishment |
| local_device_id | BYTE | B#16#05 | Communication via the integrated IE interface for CPUs 41x PN/DP |
| local_tsap_id_len | BYTE | B#16#03 | Length of parameter local_tsap_id |
| rem_subnet_id_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#03 | Length of parameter rem_tsap_id |
| next_staddr_len | BYTE | B#16#00 | This parameter is not used (because communication is over the integrated interface). Assign with B#16#00 . |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#E0 - local_tsap_id[2] = B#16#03 - local_tsap_id[3] = B#16#01 - local_tsap_id[4-16] = B#16#00 | local TSAP-ID: 0xE00301 |
| rem_subnet_id | ARRAY [1..6] of BYTE | rem_subnet_id[1-6] = B#16#00 | This parameter is not used. Assign "0" to it. |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.0.16"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#00 (0) - rem_staddr[4] = B#16#10 (16) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |
| rem_tsap_id | ARRAY [1..16] of BYTE | - rem_tsap_id[1] = B#16#E0 - rem_tsap_id[2] = B#16#03 - rem_tsap_id[3] = B#16#01 - rem_tsap_id[4-16] = B#16#00 | remote TSAP-ID: 0xE00301 |
| next_staddr | ARRAY [1..6] of BYTE | next_staddr[1-6] = B#16#00 | This parameter is not used (because communication is over the integrated interface) |
| spare | WORD | W#16#0000 | This parameter is not used. Assign "0" to it. |

The following table shows all parameter entries of communication partner B in the corresponding DB.

| Parameter | Data type | Value in example | Description |
| --- | --- | --- | --- |
| block_length | WORD | W#16#40 | Length of UDT65: 64 bytes (fixed) |
| id | WORD | W#16#0001 | Reference to this connection |
| connection_type | BYTE | B#16#12 | Protocol variant:  - B#16#12: ISO on TCP |
| active_est | BOOL | TRUE | Active connection establishment |
| local_device_id | BYTE | B#16#05 | Communication via the integrated IE interface for CPUs 41x PN/DP |
| local_tsap_id_len | BYTE | B#16#03 | Length of parameter local_tsap_id |
| rem_subnet_id_len | BYTE | B#16#00 | This parameter is not used. Assign with B#16#00. |
| rem_staddr_len | BYTE | B#16#04 | Length of the address of the remote connection end point:  - 4: Valid IP address in the rem_staddr parameter |
| rem_tsap_id_len | BYTE | B#16#03 | Length of parameter rem_tsap_id |
| next_staddr_len | BYTE | B#16#00 | This parameter is not used (because communication is over the integrated interface). Assign with B#16#00. |
| local_tsap_id | ARRAY [1..16] of BYTE | - local_tsap_id[1] = B#16#E0 - local_tsap_id[2] = B#16#03 - local_tsap_id[3] = B#16#01 - local_tsap_id[4-16] = B#16#00 | local TSAP-ID: 0xE00301 |
| rem_subnet_id | ARRAY [1..6] of BYTE | rem_subnet_id[1-6] = B#16#00 | This parameter is not used. Assign "0" to it. |
| rem_staddr | ARRAY [1..6] of BYTE | "192.168.0.14"  - rem_staddr[1] = B#16#C0 (192) - rem_staddr[2] = B#16#A8 (168) - rem_staddr[3] = B#16#00 (0) - rem_staddr[4] = B#16#0E (14) - rem_staddr[5-6] = B#16#00 | IP address of the remote connection end point |
| rem_tsap_id | ARRAY [1..16] of BYTE | - rem_tsap_id[1] = B#16#E0 - rem_tsap_id[2] = B#16#03 - rem_tsap_id[3] = B#16#01 - rem_tsap_id[4-16] = B#16#00 | remote TSAP-ID: 0xE00301 |
| next_staddr | ARRAY [1..6] of BYTE | next_staddr[1-6] = B#16#00 | This parameter is not used (because communication is over the integrated interface) |
| spare | WORD | W#16#0000 | This parameter is not used. Assign "0" to it. |

### Data types

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

## TCON: Establish communication connection (S7-300, S7-400)

### Number of connections possible

For information on the number of possible TCP or UDP connections, refer to the specifications for your CPU.

### Use with TCP and ISO on TCP

Both communication partners call the "TCON" instruction to set up and establish the communication connection. In the parameter assignment, you specify which partner is the active communication end point and which is passive.

After the connection is set up and established, it is automatically maintained and monitored by the CPU.

If the connection is terminated, for example due to a line break or due to the remote communication partner, the active partner attempts to re-establish the configured connection. You do not have to call "TCON" again.

An existing connection is terminated and the connection is removed when the "TDISCON" instruction is called or when the CPU has gone into STOP mode. To set up and establish the connection again, call "TCON" again.

### Use with UDP

Both communication partners call the "TCON" instruction to configure their local communication access point (local port). A connection is configured between the user program and the communication layer of the operating system. No connection is established to the remote partner.

The local access point is used to send and receive UDP message frames.

The following parameters must match in the configuration of the local access point (UDT 65) or in the configuration of the remote partner (UDT 66).

- With UDP: Reference to the connection and the local port no.

### Functional description

The "TCON" instruction is asynchronous, in other words, job processing extends over multiple calls. You start the job for setting up and establishing a connection by calling "TCON" with REQ  = 1.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can recognize the current status of "TCON" or when the connection was set up or established (for TCP and ISO-on-TCP).

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

### Parameters

The following table shows the parameters of the "TCON" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C | Control parameter REQUEST starts the job for establishing the connection specified by ID. The job starts on a rising edge. |
| ID | Input | WORD | M, D or constant | Reference to the connection to be established to the remote partner or between the user program and the communication layer of the operating system. ID must be identical to the corresponding parameter ID in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet complete. - BUSY = 0: The job is complete. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: An error occurred while processing the job. STATUS provides detailed information on the type of error |
| STATUS | Output | WORD | M, D | Status parameter STATUS: Error information |
| CONNECT | InOut | ANY | D | Pointers to the associated connection description (UDT 65)    See also:  - [Assigning parameters for communications connections with TCP and ISO on TCP](#assigning-parameters-for-communications-connections-with-tcp-and-iso-on-tcp-s7-300-s7-400) - [Assigning parameters for the local communications access point with UDP](#assigning-parameters-for-the-local-communications-access-point-with-udp-s7-300-s7-400)   Note: You can enter the CONNECT parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: CONN_DB.Conn1 |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Connection was established successfully |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start job processing, establishing connection |
| 0 | 7002 | Intermediate call (REQ irrelevant), connection being established |
| 1 | 8086 | The ID parameter is outside the permitted range. |
| 1 | 8087 | Maximum number of connections reached; no additional connection possible. |
| 1 | 8089 | The CONNECT parameter does not point to a data block. |
| 1 | 809A | The CONNECT parameter points to a field that does not match the length of the connection description (UDT65). |
| 1 | 809B | The local_device_id in the connection description does not match the CPU. |
| 1 | 80A0 | Group error for error codes W#16#80A1 and W#16#80A2 |
| 1 | 80A1 | - Connection or port is already being used by the user - Invalid protocol variant for the selected IE interface |
| 1 | 80A2 | Local or remote port is being used by the system |
| 1 | 80A3 | Attempt being made to re-establish an existing connection |
| 1 | 80A4 | IP address of the remote connection end point is invalid, e.g., it matches the local partner's own IP address |
| 1 | 80A7 | Communication error: You have called "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)" before "TCON" was completed. Connection establishment was aborted by calling "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)". |
| 1 | 80B2 | The CONNECT parameter points to a data block that was generated with the keyword UNLINKED. |
| 1 | 80B3 | Inconsistent parameter assignment: Group error for error codes W#16#80A0 to W#16#80A2, W#16#80A4, W#16#80B4 to W#16#80B9 |
| 1 | 80B4 | You have violated one or more of the following conditions when establishing a connection passively (active_est = FALSE) with the ISO-on-TCP protocol variant (connection_type = B#16#12):  - local_tsap_id_len >= B#16#02 - local_tsap_id[1] = B#16#E0 - With local_tsap_id_len >= B#16#03, local_tsap_id[1] is an ASCII character. - local_tsap_id[1] is an ASCII character and local_tsap_id_len >= B#16#03 |
| 1 | 80B5 | Error in parameter active_est (UDT 65) with the UDP protocol variant |
| 1 | 80B6 | Parameters assignment error in parameter connection_type (UDT 65) |
| 1 | 80B7 | Error in one of the following parameters of UDT 65: block_length, local_tsap_id_len, rem_subnet_id_len, rem_staddr_len, rem_tsap_id_len, next_staddr_len |
| 1 | 80B8 | Parameters in the local connection description (UDT 65) and Parameter ID are different |
| 1 | 80C3 | All connection resources are in use. |
| 1 | 80C4 | Temporary communication error:  - The connection cannot be established at this time. - The interface is receiving new parameters. - The configured connection is currently being removed by a "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)". - The H system is connecting and updating. |
| 1 | 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

---

**See also**

[Assigning parameters for communications connections with TCP and ISO on TCP (S7-300, S7-400)](#assigning-parameters-for-communications-connections-with-tcp-and-iso-on-tcp-s7-300-s7-400)
  
[Assigning parameters for the local communications access point with UDP (S7-300, S7-400)](#assigning-parameters-for-the-local-communications-access-point-with-udp-s7-300-s7-400)

## TDISCON: Terminate communication connection (S7-300, S7-400)

### Use with TCP and ISO on TCP

The "TDISCON" instruction terminates a communication connection from the CPU to a communication partner.

### Use with UDP

The "TDISCON" instruction closes the local communication access point. This means that the connection between the user program and the communication layer of the operating system is terminated.

### Functional description

The "TDISCON" instruction is asynchronous, in other words, job processing extends over multiple calls. You start the job for terminating a connection by calling the "TDISCON" instruction with REQ = 1.

After the "TDISCON" instruction has been successfully executed, the ID specified for the "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" instruction is no longer valid and cannot be used for sending or receiving.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions (see also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)).

### Parameters

The following table shows the parameters of the "TDISCON" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C | Starts the job to terminate the connection specified in the ID on a rising edge. |
| ID | Input | WORD | M, D or constant | Reference to the connection established with "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)". Range of values: W#16#0001 to W#16#0FFF |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:   - 0: Job not yet started or still in progress - 1: Job completed without error |
| BUSY | Output | BOOL | I, Q, M, D, L | Status parameter with the following values:  - 0: Job not yet started or already completed - 1: Job not yet completed. A new job cannot be started. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - 0: No error - 1: Error occurred |
| STATUS | Output | WORD | M, D | Status of the instruction |
|  |  |  |  |  |

### Parameters BUSY, DONE and ERROR

You can check the status of the job with the BUSY, DONE, ERROR and STATUS parameters. The BUSY parameter indicates the processing status. With the DONE parameter, you can check whether or not a job executed successfully. The ERROR parameter is set when errors occurred during execution of TDISCON. The error information is output at the STATUS parameter.

The following table shows the relationship between the BUSY, DONE and ERROR parameters:

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| 1 | - | - | The job is being processed. |
| 0 | 1 | 0 | The job was completed successfully. |
| 0 | 0 | 1 | The job ended with an error. The cause of the error is output at the STATUS parameter. |
| 0 | 0 | 0 | No new job was assigned. |

### Parameters ERROR and STATUS

| ERROR | STATUS  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Connection successfully terminated |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start of job execution, connection is being terminated. |
| 0 | 7002 | Connection is being terminated (REQ irrelevant). |
| 1 | 8086 | The ID parameter is outside the permitted address range. |
| 1 | 80A3 | Attempt being made to terminate a non-existent connection. |
| 1 | 80C4 | Temporary communication error: The interface is currently receiving new parameters, or the connection is currently being established / the H system is connecting and updating. |

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)

## TSEND: Send data via communication connection (S7-300, S7-400)

### Description

The "TSEND" instruction sends data over an existing communication connection.

### Functional description

"TSEND" is an asynchronous instruction, in other words, its processing extends over multiple calls. You start the job by calling "TSEND" with REQ = 1.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The DONE output parameter is set if the data to be sent to the local interface was transferred completely.

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can determine the current "TSEND" status.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TSEND", make sure the data in the send area remains consistent until the DONE parameter or the ERROR parameter has the value TRUE.

### Parameters

The following table shows the parameters of the "TSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C | Control parameter REQUEST starts the send job on a rising edge.  The data is transferred from the area specified by DATA and LEN. |
| ID | Input | WORD | M, D or constant | Reference to the associated connection. ID must be identical to the corresponding parameter ID in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | INT | I, Q, M, D, L | Maximum number of bytes to be sent with the job   See also:  [Relationship between CPU and protocol variant used (connection_type) and transferable data length](#relationship-between-cpu-and-protocol-variant-used-connection_type-and-transferable-data-length-s7-300-s7-400) |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: The data was transferred completely to the local interface for sending. |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet completed. A new job cannot be triggered. - BUSY = 0: The job is completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: Error occurred during processing. STATUS supplies detailed information on the type of error |
| STATUS | Output | WORD | M, D | Status parameter STATUS: Error information |
| DATA | InOut | ANY | I, Q, M, D | Send area, contains address and length  The address refers to:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   Note: Do not use ARRAY of BOOL as send area.  Note: You can enter the DATA parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Send job completed without error |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start of job processing, data being sent  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 0 | 7002 | Intermediate call (REQ irrelevant), job is being processed  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 1 | 8085 | The LEN parameter has the value "0" or is greater than the highest permitted value. |
| 1 | 8086 | The ID parameter is not in the permitted range |
| 1 | 8088 | The LEN parameter is greater than the memory area specified in DATA. |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is currently being terminated. Transmission over this connection is not possible. - The interface is being reinitialized. |
| 1 | 80B3 | The connection type (connection_type parameter in the connection description) is set to UDP. Please use "[TUSEND](#tusend-send-data-via-ethernet-udp-s7-300-s7-400)". |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection to the partner cannot be established at the moment. - The interface is receiving new parameter settings or the connection is currently being established. |
| 1 | 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## TRCV: Receive data via communication connection (S7-300, S7-400)

### Description

The "TRCV" instruction receives data over an existing communication connection.

### Receive area

This means the area in which the function block enters the received data.

The receive area is specified by the following two variables:

- Pointer to the start of the area
- Length of the area

Depending on the protocol variant being used, the length of the area is specified either by the LEN parameter (if LEN <> 0) or the length information of the DATA parameter (if LEN = 0).

### Receive modes of TRCV

The following table shows how "TRCV" enters the received data in the receive area.

| Protocol variant | Entering the data  in the receive area | connection_type parameter | Value of the LEN parameter |
| --- | --- | --- | --- |
| TCP | Ad-hoc mode | B#16#01, B#16#11 | 0 |
| TCP | Data reception with specified length | B#16#01, B#16#11 | <> 0 |
| ISO on TCP | protocol-controlled | B#16#12 | 0 (recommended) or <> 0 |

### TCP / ad-hoc mode

The ad-hoc mode exists only with the TCP protocol variant. You set ad-hoc mode by assigning the value "0" to the LEN parameter.

The receive area is identical to the area formed by DATA. A maximum of 8192 bytes are received. Immediately after receiving a block of data, the "TRCV" instruction transfers this to the receive area and sets NDR to "1".

### TCP / data reception with specified length

You set data reception with a specified length by assigning a value other than zero to the LEN parameter.

The receive area is defined by the LEN and DATA parameters. As soon as LEN bytes have been received, TRCV transfers them to the receive area and sets NDR to "1".

### ISO on TCP / protocol-controlled data transfer

With the ISO-on-TCP protocol variant, data is transferred protocol-controlled.

The receive area is defined by the LEN and DATA parameters. As soon as all job data has been received, "TRCV" transfers it to the receive area and sets NDR to "1".

### Data exchange of data type STRING

If you want to exchange data of the data type STRING with the "TSEND" and "TRCV" instructions, only the Ad-hoc-Mode with LEN=0 is appropriate. Besides, you have to set the string length for "TRCV" at least that large as for the "TSEND" instruction. If you do not follow this rule, it can lead to errors during the further string processing.

If you use ARRAY of BYTE as receive area for a sent character string, the first byte contains the maximum length that is set by the sender abd the secind byte the actual character string length.

### Functional description

"TRCV" is an asynchronous instruction, in other words, its processing extends over multiple calls. You start the receive job by calling TRCV with EN_R = 1.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The following table shows the relationship between BUSY, NDR and ERROR. Using this table, you can determine the current status of "TRCV" or when the receive operation is completed.

| BUSY | NDR | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TRCV", the data in the receive area is only consistent when the NDR parameter has the value TRUE.

### Parameters

The following table shows the parameters of the "TRCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L, T, C | Control parameter enabled to receive: With EN_R = 1, "TRCV" is ready to receive. The receive job is being processed. |
| ID | Input | WORD | M, D or constant | Reference to the associated connection. ID must be identical to the associated parameter ID in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | INT | I, Q, M, D, L | Length of the receive area in bytes  For the meaning of LEN = 0 or LEN <> 0, see above (receive modes of "TRCV").  For the value range, see also: [Relationship between CPU and protocol variant used (connection_type) and transferable data length](#relationship-between-cpu-and-protocol-variant-used-connection_type-and-transferable-data-length-s7-300-s7-400). |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:  - NDR = 0: Job not yet started or still running - NDR = 1: Job successfully completed |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: Error occurred during processing. STATUS supplies detailed information on the type of error |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet completed. A new job cannot be triggered. - BUSY = 0: The job is completed. |
| STATUS | Output | WORD | M, D | Status parameter STATUS: Error information |
| RCVD_LEN | Output | INT | I, Q, M, D, L | Amount of data actually received in bytes |
| DATA | InOut | ANY | I, Q, M, D | Receive area (definition see above), contains address and length  The address refers to:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   Note: Do not use ARRAY of BOOL as receive area.  Note: You can enter the DATA parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | New data was accepted. The current length of the received data is shown in RCVD_LEN. |
| 0 | 7000 | Block not ready to receive |
| 0 | 7001 | Block is ready to receive, receive job was activated |
| 0 | 7002 | Intermediate call, receive job being processed  Note: During this processing phase the instruction writes data to the receive area. For this reason, an error could result in inconsistent data in the receive area. |
| 1 | 8085 | The LEN parameter is greater than the largest permitted value, or you changed the value of the LEN or DATA parameter since the first call |
| 1 | 8086 | The ID parameter is not in the permitted range |
| 1 | 8088 | - Receive area is too small - Value in LEN is higher than the receive area specified by DATA |
| 1 | 80A1 | Communication error:  - The specified connection has not yet been established. - The specified connection is currently being terminated. A receive job over this connection is not possible. - New parameter settings are being assigned to the interface. |
| 1 | 80B3 | The protocol variant (connection_type parameter in the connection description) is set to UDP. Please use "[TURCV](#turcv-receive-data-via-ethernet-udp-s7-300-s7-400)". |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection to the partner cannot be established at the moment. - The interface is receiving new parameter settings or the connection is currently being established. |
| 1 | 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## TUSEND: Send data via Ethernet (UDP) (S7-300, S7-400)

### Description

The "TUSEND" instruction sends data to the remote partner addressed by the ADDR parameter using UDP.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Data transfer via UDP**  When transferring data with UDP according to RFC 768, the data is transferred to the remote partner without acknowledgement and is therefore unreliable. This means that data can be lost without this being indicated by the block. |  |

> **Note**
>
> For sequential send operations to different partners, you only need to adjust the ADDR parameter when calling "TUSEND". You do not need to call the "[TCON](#tcon-establish-communication-connection-s7-300-s7-400)" and "[TDISCON](#tdiscon-terminate-communication-connection-s7-300-s7-400)" instructions again.

### Functional description

"The TUSEND" instruction works asynchronously, which means its job processing extends over multiple calls. You start the job by calling "TUSEND" with REQ = 1.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can determine the current status of "TUSEND" or when the send process is concluded.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TUSEND", make sure the data in the send area remains consistent until the DONE parameter or the ERROR parameter has the value TRUE.

### Parameters

The following table shows the parameters of the "TUSEND" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C | Control parameter REQUEST starts the send job on a rising edge.  The data is transferred from the area specified by DATA and LEN. |
| ID | Input | WORD | M, D or constant | Reference to the associated connection between the user program and the communication layer of the operating system. ID must be identical to the corresponding parameter ID in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | INT | I, Q, M, D, L | Number of bytes to be sent with the job  Range of values: 1 to 1472 |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet completed. A new job cannot be triggered. - BUSY = 0: The job is completed. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: Error occurred during processing. STATUS supplies detailed information on the type of error |
| STATUS | Output | WORD | M, D | Status parameter STATUS: Error information |
| DATA | InOut | ANY | I, Q, M, D | Send area, contains address and length  The address refers to:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   Note: You can enter the DATA parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
| ADDR | InOut | ANY | D | Pointers to the address of the receiver (for example, P#DB100.DBX0.0 byte 8)   See also: [Structure of the address information for the remote partner with UDP](#structure-of-the-address-information-for-the-remote-partner-with-udp-s7-300-s7-400)  Note: You can enter the ADDR parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | Send job completed without error |
| 0 | 7000 | No job processing active |
| 0 | 7001 | Start of job processing, data being sent  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 0 | 7002 | Intermediate call (REQ irrelevant), job is being processed  Note: During this processing phase, the operating system accesses the data in the DATA send area. |
| 1 | 8085 | The LEN parameter has the value "0" or is greater than the highest permitted value. |
| 1 | 8086 | The ID parameter is not in the permitted range |
| 0 | 8088 | The LEN parameter is greater than the memory area specified in DATA. |
| 1 | 8089 | The ADDR parameter does not point to a data block |
| 1 | 80A1 | Communication error:  - The specified connection between user program and communication layer of the operating system has not yet been established. - The specified connection between the user program and the communication layer of the operating system is currently being terminated. Transmission over this connection is not possible. - The interface is being reinitialized. |
| 1 | 80A4 | IP address of the remote connection end point is invalid, e.g., it matches the local partner's own IP address. |
| 1 | 80B3 | - The protocol variant (connection_type parameter in the connection description) is not set to UDP. Please use "[TSEND](#tsend-send-data-via-communication-connection-s7-300-s7-400)". - ADDR parameter: Invalid information for port no. |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error:  - The connection between the user program and the communication layer of the operating system cannot be established at this time. - New parameter settings are being assigned to the interface. |
| 1 | 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## TURCV: Receive data via Ethernet (UDP) (S7-300, S7-400)

### Description

The "TURCV" instruction receives data via UDP. After successful completion of "TURCV", the ADDR parameter will show you the address of the remote partner (the sender).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Data transfer via UDP according to RFC 768**  When transferring data with UDP according to RFC 768, the data is transferred to the remote partner without acknowledgement and is therefore unreliable. This means that data can be lost without this being indicated by the block. |  |

### Functional description

"TURCV" is an asynchronous instruction, in other words, its job processing extends over multiple calls. You start the receive job by calling "TURCV" with EN_R = 1.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

The following table shows the relationship between BUSY, NDR and ERROR. Using this table, you can determine the current status of TURCV or when the receive process is concluded.

| BUSY | NDR | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |

> **Note**
>
> Due to the asynchronous operation of "TURCV", the data in the receive area is only consistent when the NDR parameter has the value TRUE.

### Parameters

The following table shows the parameters of the "TURCV" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| EN_R | Input | BOOL | I, Q, M, D, L, T, C | Control parameter enabled to receive: With EN_R = 1, "TURCV" is ready to receive. The receive job is being processed. |
| ID | Input | WORD | M, D or constant | Reference to the associated connection between the user program and the communication layer of the operating system. ID must be identical to the associated parameter ID in the local connection description. Value range: W#16#0001 to W#16#0FFF |
| LEN | Input | INT | I, Q, M, D, L | Length of the receive area in bytes: 0 (recommended) or 1 to 1472  See also: [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400) |
| NDR | Output | BOOL | I, Q, M, D, L | Status parameter NDR:  - NDR = 0: Job not yet started or still running - NDR = 1: Job successfully completed |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  - ERROR=1: Error occurred during processing. STATUS supplies detailed information on the type of error |
| BUSY | Output | BOOL | I, Q, M, D, L | - BUSY = 1: The job is not yet completed. A new job cannot be triggered. - BUSY = 0: The job is completed. |
| STATUS | Output | WORD | M, D | Status parameter STATUS: Error information |
| RCVD_LEN | Output | INT | I, Q, M, D, L | Amount of data actually received in bytes |
| DATA | InOut | ANY | I, Q, M, D | Receive area (for definition, see [Functional description of instructions for Open User Communication via Industrial Ethernet](#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400) ) The address references:  - The process image of the inputs - The process image of the outputs - A bit memory - A data block   Note: You can enter the DATA parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
| ADDR | InOut | ANY | D | Pointers to the address of the receiver (for example, P#DB100.DBX0.0 byte 8), see also: [Structure of the address information for the remote partner with UDP](#structure-of-the-address-information-for-the-remote-partner-with-udp-s7-300-s7-400)   Note: You can enter the ADDR parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameters ERROR and STATUS

| ERROR | STATUS  (W#16#...) | Explanation |
| --- | --- | --- |
| 0 | 0000 | New data was accepted. The current length of the received data is shown in RCVD_LEN. |
| 0 | 7000 | Block not ready to receive |
| 0 | 7001 | Block is ready to receive, receive job was activated |
| 0 | 7002 | Intermediate call, receive job being processed  Note: During this processing phase, "TURCV" writes data to the receive area. For this reason, an error could result in inconsistent data in the receive area. |
| 1 | 8085 | The LEN parameter is greater than the largest permitted value, or you changed the value of the LEN or DATA parameter since the first call |
| 1 | 8086 | The ID parameter is not in the permitted range |
| 1 | 8088 | - Receive area is too small - Value in LEN is higher than the receive area specified by DATA |
| 1 | 8089 | The ADDR parameter does not point to a data block |
| 1 | 80A1 | Communication error:  - The specified connection between user program and communication layer of the operating system has not yet been established. - The specified connection between the user program and the communication layer of the operating system is currently being terminated. A receive job over this connection is not possible. - New parameter settings are being assigned to the interface. |
| 1 | 80B3 | The protocol variant (connection_type parameter in the connection description) is not set to UDP. Please use "[TRCV](#trcv-receive-data-via-communication-connection-s7-300-s7-400)". |
| 1 | 80C3 | - A block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 1 | 80C4 | Temporary communication error: New parameter settings are being assigned to the interface. |
| 1 | 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## IP_CONF: Change IP configuration parameters (S7-300, S7-400)

This section contains information on the following topics:

- [Description of IP_CONF (S7-300, S7-400)](#description-of-ip_conf-s7-300-s7-400)
- [Data block CONF_DB (S7-300, S7-400)](#data-block-conf_db-s7-300-s7-400)

### Description of IP_CONF (S7-300, S7-400)

#### Description

The "IP_CONF" instruction is used for the program-controlled configuration of the integrated PROFINET interface of the CPU. The existing configuration data is overwritten.

You can make the following interface configuration settings:

- IP parameters: IP address, subnet mask, router address
- PROFINET IO device name (if the CPU is operated as a PROFINET IO device)

You have to store the configuration data in a configuration DB.

You can make the program-controlled setting of the IP configuration with the "IP_CONF" instruction as an alternative to configuration with STEP 7. It only takes effect, however, if you explicitly specified in the hardware configuration that IP parameters are assigned via the user program.

> **Note**
>
> As an alternative to project engineering, the configuration data of the communication processor can be set using the "IP_CONFIG" instruction (see SIMATIC NET CP).

#### Functional description

The "IP_CONF" instruction works asynchronously, that is, its execution extends over multiple calls. You start the transfer operation by calling "IP_CONF" with REQ = 1.

Only one job can be active at any time.

The job status is indicated by the output parameters BUSY and STATUS. Here, STATUS corresponds to the output parameter RET_VAL of the asynchronous instructions (see also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)).

The following table shows the relationship between BUSY, DONE and ERROR. Using this table, you can determine the current status of the instruction and when the transfer of configuration data is concluded.

| BUSY | DONE | ERROR | Description |
| --- | --- | --- | --- |
| TRUE | irrelevant | irrelevant | The job is being processed. |
| FALSE | TRUE | FALSE | Job successfully completed. |
| FALSE | FALSE | TRUE | The job ended with an error. The cause of the error can be found in the STATUS parameter. |
| FALSE | FALSE | FALSE | The instruction was not assigned a (new) job. |
|  |  |  |  |

#### Parameters

The following table shows the parameters of the "IP_CONF" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L, T, C | Control parameter REQUEST. starts the instruction on a rising edge. |
| LADDR | Input | WORD | M, D or constant | Diagnostics address of the PROFINET interface |
| [CONF_DB](#data-block-conf_db-s7-300-s7-400) | Input | ANY | D | Pointer to the configuration data (permitted data types: BYTE, WORD, BLOCK_DB)  Note: You can enter the CONF_DB parameter in these two ways:  - absolute. Example: P#DB13.DBX0.0 byte 64 - symbolic. Example: DB_name.variable |
| DONE | Output | BOOL | I, Q, M, D, L | Status parameter DONE:   - 0: Job not yet started or still executing. - 1: Job executed without errors |
| BUSY | Output | BOOL | I, Q, M, D, L | - 0: Job is complete. - 1: The job is not yet completed. A new job cannot be triggered. |
| ERROR | Output | BOOL | I, Q, M, D, L | Status parameter ERROR:  ERROR=1: Error occurred during processing. STATUS supplies detailed information on the type of error |
| STATUS | Output | DWORD | I, Q, M, D, L | Error information |
| ERR_LOC | Output | DWORD | I, Q, M, D, L | Error source (field_id and subfield_type_id of the parameter block causing the error) |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

#### Parameters ERROR and STATUS

| ERROR | STATUS (DW#16#..) | ERR_LOC* | Explanation |
| --- | --- | --- | --- |
| 0 | 00000000 | 0 | Job execution terminated without error |
| 0 | 00700000 | 0 | No job processing active |
| 0 | 00700100 | 0 | Start of job execution |
| 0 | 00700200 | 0 | Intermediate call (REQ  irrelevant) |
| 1 | C08xyy00 | 0 | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
| 1 | C0808000 | 0 | LADDR is invalid |
| 1 | C0808100 | 0 | LADDR is not assigned to the supported PROFINET interface |
| 1 | C0808200 | 0 | Error in the CONF_DB parameter: Data type is not supported. |
| 1 | C0808300 | 0 | Error in the CONF_DB parameter: The pointer points to an unsupported area. |
| 1 | C0808400 | 0 | Error in the CONF_DB parameter: Incorrect length of the ANY pointer |
| 1 | C0808700 | 0 | Error in the CONF_DB parameter: Inconsistency of the length specified in the configuration data |
| 1 | C0808800 | s, 0 | field_type_id has an illegal value |
| 1 | C0808900 | s, 0 | field_id has an illegal value |
| 1 | C0808A00 | s, 0 | Wrong number for subfield_cnt |
| 1 | C0808B00 | s, t | subfield_id has an illegal value |
| 1 | C0808C00 | s, t | Subfield used more than once |
| 1 | C0808D00 | s, t | subfield_len has an incorrect or illegal value |
| 1 | C0808E00 | s, t | subfield_mode has an illegal value |
| 1 | C0808F00 | s, t | There is a conflict with an earlier subfield in the subfield. |
| 1 | C0809000 | s, t | The parameters of the subfield are write-protected. E.g. parameters are specified via configuration or PNIO mode is enabled. |
| 1 | C0809400 | s, t | The parameter value in the subfield is not defined or illegal |
| 1 | C080C200 | 0 | Transfer cannot be carried out (e.g. because the interface is not reachable). |
| 1 | C080C300 | 0 | Insufficient resources (for example, multiple calling of "IP_CONF" with different parameters) |
| 1 | C080C400 | 0 | Temporary communication error |
| * In the table above, f is the field_id and s the subfield_type_id of the parameter block causing the error. |  |  |  |

### Data block CONF_DB (S7-300, S7-400)

#### Description

The following figure shows how the configuration data to be transferred is stored in the configuration DB.

![Description](images/22276443531_DV_resource.Stream@PNG-en-US.png)

The configuration data therefore comprises exactly one field and several subfields:

- The field consists of a header and the subfields. The header, in turn, consists of the following elements:

  - field_type_id (data type INT): Zero
  - field_id (data type INT): Zero
  - subfield_cnt (data type INT): Number of subfields:
- Each subfield consists, in turn, of a header (subfield_type_id, subfield_length, subfield_mode) and the subfield-specific parameters. Each subfield must consist of an even number of bytes.

  The following values are permitted for subfield_mode:

  - 1: permanent validity of the configuration data
  - 2: temporary validity of the configuration data including the deletion of existing permanent configuration data

    > **Note**
    >
    > Exactly one field is currently permitted. Its parameters field_type_id and field_id must have the value zero. Other fields with different values for field_type_id and field_id are subject to future extensions.

#### Permitted subfields

| subfield_type_id | Name of the subfield | Explanation |
| --- | --- | --- |
| 30 | SUB_IP_SUITE_IPV4 | IP parameters: IP address, subnet mask, router address |
| 40 | SUB_NOS | PROFINET IO device name (Name of Station) |

#### Type definition for the subfield "SUB_IP_SUITE_IPV4"

| Name |  | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| SUB_IP_SUITE_V4 |  | Struct |  |  |
|  | Id | INT | 30 | subfield_type_id |
|  | len | INT | 18 | subfield_length |
|  | mode | INT | 1 | subfield_mode (1: permanent, 2: temporary) |
|  | ipaddr_3 | BYTE | b#16#C8 | IP address high byte: 200 |
|  | ipaddr_2 | BYTE | b#16#0C | IP address high byte: 12 |
|  | ipaddr_1 | BYTE | b#16#01 | IP address low byte: 1 |
|  | ipaddr_0 | BYTE | b#16#90 | IP address low byte: 144 |
|  | snmask_3 | BYTE | b#16#FF | Subnet mask high byte: 255 |
|  | snmask_2 | BYTE | b#16#FF | Subnet mask high byte: 255 |
|  | snmask_1 | BYTE | b#16#FF | Subnet mask low byte: 255 |
|  | snmask_0 | BYTE | b#16#00 | Subnet mask low byte: 0 |
|  | router_3 | BYTE | b#16#C8 | Router high byte: 200 |
|  | router_2 | BYTE | b#16#0C | Router high byte: 12 |
|  | router_1 | BYTE | b#16#01 | Router low byte: 1 |
|  | router_0 | BYTE | b#16#01 | Router low byte: 1 |
|  |  |  |  |  |

#### Type definition for the subfield "SUB_NOS"

| Name |  | Data type | Start value | Description |
| --- | --- | --- | --- | --- |
| SUB_NOS |  | Struct |  |  |
|  | id | INT | 40 | subfield_type_id |
|  | len | INT | 246 | subfield_length |
|  | mode | INT | 1 | subfield_mode (1: permanent, 2: temporary) |
|  | nos | ARRAY[1..240] of BYTE | 0 | Device name: You must occupy the ARRAY from the first byte. If the ARRAY is longer than the device name to be assigned, enter a zero byte after the actual device name (complying with IEC 61158-6-10). Otherwise, nos is rejected and the "[IP_CONF](#description-of-ip_conf-s7-300-s7-400)" instruction enters the error code DW#16#C0809400 in STATUS. If you enter zero the first byte, the device name is deleted. |
|  |  |  |  |  |

The device name is subject to the following limitations:

- Restricted to a total of 240 characters (lower case letters, numbers, dash, or dot)
- A name component within the device name, in other words, a character string between two dots, must not exceed 63 characters. The name components must not begin or end with the "-" character.
- No special characters such as umlauts, brackets, underscore, slash, blank space, etc. The only special character permitted is the dash.
- The device name must not begin or end with the "-" or "." characters.
- The device name must not begin with a number.
- The device name form n.n.n.n (n = 0, ... 999) is not permitted.
- The device name must not begin with the string "port-xyz" or "port-xyz-abcde" (a, b, c, d, e, x, y, z = 0, ... 9).
- The character string ".." is not permitted in the device name.

  > **Note**
  >
  > You can also create an ARRAY "nos" that is shorter then 240 bytes, but not less than 2 bytes. In this case, you must adjust the "len" (length of subfield) tag accordingly.

## Data exchange using FETCH and WRITE (S7-300, S7-400)

This section contains information on the following topics:

- [FW_TCP: Swap data using FETCH and WRITE via TCP (S7-300, S7-400)](#fw_tcp-swap-data-using-fetch-and-write-via-tcp-s7-300-s7-400)
- [FW_IOT: Swap data using FETCH and WRITE via ISO-on-TCP (S7-300, S7-400)](#fw_iot-swap-data-using-fetch-and-write-via-iso-on-tcp-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

### FW_TCP: Swap data using FETCH and WRITE via TCP (S7-300, S7-400)

#### Description

With the "FW_TCP" instruction, the FETCH/WRITE functions are provided via the TCP connection.

#### Call

Since a separate TCP connection is required for each of the services FETCH/WRITE, the instruction is called twice in OB1:

- The first call with the FETCH_TCP_DB instance data block provides the FETCH service via the TCP connection.
- The second call with the WRITE_TCP_DB instance data block provides the WRITE service via the TCP connection.

The TCP connection is automatically established after a cold restart, warm restart and hot restart of the CPU, as well as after changes to the connection parameters. The parameters for the connection establishment are stored in the "ConnectParam" data block (description: See below). The input parameter ENABLE provides the option of manually controlling the establishment and termination of the connection. When the connection parameters are changed, the connection is automatically terminated and re-established.

The following figure is a schematic representation of the "FW_TCP" instruction, which is called in OB1 and implements the FETCH and WRITE services via TCP connections.

![Call](images/23192142987_DV_resource.Stream@PNG-en-US.png)

#### Connection parameters of the "ConnectParam" instance data block

The following connection parameters are checked before the connection is established:

- connection_type
- id
- local_tsap_id

If one of these parameters is wrongly defined, the communication connection will not be established. No data is sent or received.

- After the communication connection has been established, a 16-byte header frame of the FETCH/WRITE services is received. The header frame contains the information indicating whether a FETCH or WRITE job is pending.
- If a FETCH job is pending, the data requested by the communication partner is prepared in the instance data block DB210 of the instruction and the acknowledgement frame generated. The acknowledgement frame is sent including the prepared data.
- If a WRITE job is pending, the user data is received and written to the destination area after the evaluation of the 16-byte header frame. The acknowledgement frame is then generated in instance data block DB310 and sent.

The following table shows the data structure of the connection parameters for a TCP connection. This is 64 bytes long.

| Parameter | Data type | Start value | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#1 | Connection ID: The value of the parameter must be within the following range:  id = W#16#0001 to W#16#0FFF (1 to 4095) |
| connection_type | BYTE | B#16#11 | Connection type. The following is valid for the TCP connection:  - connection_type = B#16#11 (TCP native) or - connection_type = B#16#1 (TCP native or compatibility mode) |
| active_est | BOOL | FALSE | Passive connection establishment |
| local_device_id | BYTE | B#16#3 | ID for the local PN/IE interface (here: CPU 319-3PN/DP). |
| local_tsap_id_len | BYTE | B#16#2 | Length of the local_tsap_id parameter used in bytes:  - 0 or 2, if connection type = 17 (TCP) - Only the value "0" is permitted for the active end. |
| rem_subnet_id_len | BYTE | B#16#0 | This parameter is not used. |
| rem_staddr_len | BYTE | B#16#0 | Length of address of partner end point (rem_staddr parameter) in bytes. Since this is an unspecified connection, the parameter is irrelevant. |
| rem_tsap_id_len | BYTE | B#16#0 | Length of the rem_tsap_id parameter used in bytes:   - 0 or 2, if connection type = 17 (TCP). - Only the value 0 is permitted for the passive end. |
| next_staddr_len | BYTE | B#16#0 | This parameter is not used. |
| local_tsap_id | ARRAY [1..16] of BYTE | B#16#7  B#16#D0  B#16#0  :  :  B#16#0 | Local port for the TCP connection. Possible values: 1 to 49151 (recommended values: 2000...5000).  - local_tsap_id[1] = high byte of the port no. in hexadecimal notation; - local_tsap_id[2] = low byte of port no. in hexadecimal notation; - local_tsap_id[3-16] = irrelevant   Note: Make sure that every value of local_tsap_id is unique within the CPU. |
| rem_subnet_id | ARRAY [1..6] of BYTE | B#16#0 … | This parameter is not used. |
| rem_staddr | ARRAY [1..6] of BYTE | B#16#0 | IP address of the partner end point, for example, for 192.168.2.3:   - rem_staddr[1] = 192 - rem_staddr[2] = 168 - rem_staddr[3] = 2 - rem_staddr[4] = 3 - rem_staddr[5-6] = irrelevant   Not relevant for unspecified connections with passive connection establishment. |
| rem_tsap_id | ARRAY [1..16] of BYTE | B#16#0 | Port of the communication partner.  For 17 (TCP) possible values: 1 to 49151 (recommended values: 2000...5000).  - rem_tsap_id[1] = high byte of the port no. in hexadecimal notation; - rem_tsap_id[2] = low byte of port no. in hexadecimal notation; - rem_tsap_id[3-16] = irrelevant   Not relevant for unspecified connections with passive connection establishment. |
| next_staddr | ARRAY [1..6] of BYTE | B#16#0 | This parameter is not used. |
| spare | WORD | W#16#0 | This parameter is not used. |

#### Parameters

The following table shows the parameters of the "FW_TCP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ENABLE | Input | BOOL | I, Q, M, D, L, T, C | The establishment and termination of the connection is initiated with this parameter:  - 0 = Connection is terminated - 1 = Connection is established |
| CONNECT | Input | ANY | D | ANY pointer to the data area of DB211 that contains the parameters for establishing the TCP connection. This data area must be at least 64 bytes in size. |
| ADDRMODE | Input | INT | I, Q, M, D, L or constant | This parameter defines how the data of the FETCH or WRITE job are addressed (in S7 or S5 address mode).  - 0 = S7 address mode   (Start address of the data is interpreted as a byte address) - 1 = S5 address mode   (Start address of the data is interpreted as a word address) |
| NDR | Output | BOOL | I, Q, M, D, L | new data record parameter:  This parameter shows that the data of the WRITE job has been successfully adopted and that the acknowledgement frame was generated and sent. |
| ERROR | Output | BOOL | I, Q, M, D, L | This parameter is set when:  - An error occurred establishing or terminating the connection - An error occurred during the sending or receiving of data. - An invalid FETCH/WRITE header frame was received. |
| MODE | Output | BYTE | I, Q, M, D, L | This parameter shows whether a FETCH or WRITE job was executed.  - 0 = No job active - 1 = WRITE job - 2 = FETCH job |
| [STATUS](#status-parameter-s7-300-s7-400) | Output | WORD | M, D | Internal communication status bits are output in the STATUS parameter. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### FW_IOT: Swap data using FETCH and WRITE via ISO-on-TCP (S7-300, S7-400)

#### Description

With the "FW_IOT" instruction, the FETCH/WRITE services are provided via the ISO-on-TCP connection.

#### Call

Since a separate TCP connection is required for each of the FETCH/WRITE services, the "FW_IOT" instruction is called twice in OB1:

- The first call with the FETCH_IOT_DB instance data block provides the FETCH service via the ISO-on-TCP connections.
- The second call with the WRITE_IOT_DB instance data block provides the WRITE service via the ISO-on-TCP connection.

The ISO-on-TCP connection is automatically established after a cold restart, warm restart and hot restart of the CPU, as well as after the changes to the connection parameters. The parameters for the establishment of the connection are stored in the "ConnectParam" DB. With the ENABLE input parameter, the user has the option of manually controlling connection establishment and termination. When the connection parameters are changed, the connection is automatically terminated and re-established. The following table shows the data structure of the connection parameters for an ISO-on-TCP connection: This is 64 bytes long.

The following figure is a schematic representation of the "FW_IOT" instruction, which is called in OB1 and implements the FETCH and WRITE services via ISO-on-TCP connections.

![Call](images/20159622027_DV_resource.Stream@PNG-en-US.png)

#### Connection parameters of the "ConnectParam" instance data block

The following connection parameters are checked before the connection is established:

- connection_type
- id
- local_tsap_id
- **local_tsap_id _len**

If one of these parameters is wrongly defined, the communication connection will not be established. No data is sent or received.

- After the communication connection has been established, a 16-byte header frame of the FETCH/WRITE services is received. The header frame contains the information indicating whether a FETCH or WRITE job is pending.
- If a FETCH job is pending, the data requested by the communication partner is prepared in the FETCH_IOT_DB instance data block of the instruction and the acknowledgement frame generated. The acknowledgement frame is sent including the prepared data.
- If a WRITE job is pending, the user data is received and written to the destination area after the evaluation of the 16-byte header frame. The acknowledgement frame is then generated in the WRITE_IOT_DB instance data block and sent.

The following table shows the data structure of the connection parameters for a TCP connection. This is 64 bytes long.

| Parameter | Data type | Start value | Description |
| --- | --- | --- | --- |
| id | WORD | W#16#1 | Connection ID: The value of the parameter must be within the following range:  id = W#16#0001 to W#16#0FFF (1 to 4095) |
| connection_type | BYTE | B#16#1**2** | Connection type. The following is valid for an ISO-on-TCP connection:  connection_type = B#16#12 |
| active_est | BOOL | FALSE | Passive connection establishment |
| local_device_id | BYTE | B#16#3 | ID for the local PN/IE interface (here: CPU 319-3PN/DP). |
| local_tsap_id_len | BYTE | B#16#2 | Length of the local_tsap_id parameter used in bytes:  - 2 to 16, if connection type = 18 (ISO-on-TCP) |
| rem_subnet_id_len | BYTE | B#16#0 | This parameter is not used. |
| rem_staddr_len | BYTE | B#16#0 | Length of address of partner end point (rem_staddr parameter) in bytes. Since this is an unspecified connection, the parameter is irrelevant. |
| rem_tsap_id_len | BYTE | B#16#0 | Length of the rem_tsap_id parameter used in bytes:   - 2 to 16, if connection type = 18 (ISO-on-TCP) |
| next_staddr_len | BYTE | B#16#0 | This parameter is not used. |
| local_tsap_id | ARRAY [1..16] of BYTE | B#16#7  B#16#D0  B#16#0  :  :  B#16#0 | Local TSAP ID for the ISO-on-TCP connection.   - local_tsap_id[1] = B#16#E0; - local_tsap_id[2] = rack and slot of local end points (bits 0 to 4: slot number, bits 5 to 7: rack number); - local_tsap_id[3-16] = TSAP extension, optional   Note: Make sure that every value of local_tsap_id is unique within the CPU. |
| rem_subnet_id | ARRAY [1..6] of BYTE | B#16#0 … | This parameter is not used. |
| rem_staddr | ARRAY [1..6] of BYTE | B#16#0 | IP address of the partner end point, for example, for 192.168.2.3:   - rem_staddr[1] = 192 - rem_staddr[2] = 168 - rem_staddr[3] = 2 - rem_staddr[4] = 3 - rem_staddr[5-6] = irrelevant   Not relevant for unspecified connections with passive connection establishment. |
| rem_tsap_id | ARRAY [1..16] of BYTE | B#16#0 | Port of the communication partner.  For partner TSAP ID with ISO-on-TCP:  - rem_tsap_id[1] = B#16#E0; - rem_tsap_id[2] = rack and slot of partner end point (bits 0 to 4: slot number, bits 5 to 7: rack number); - rem_tsap_id[3-16] = TSAP extension, optional   Not relevant for unspecified connections with passive connection establishment. |
| next_staddr | ARRAY [1..6] of BYTE | B#16#0 | This parameter is not used. |
| spare | WORD | W#16#0 | This parameter is not used. |

#### Parameters

The following table shows the parameters of the "FW_IOT" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| ENABLE | Input | BOOL | I, Q, M, D, L, T, C | The establishment and termination of the connection is initiated with this parameter:  - 0 = Connection is terminated - 1 = Connection is established |
| CONNECT | Input | ANY | D | ANY pointer to the data area of the DB that contains the parameters for establishing the TCP connection. This data area must be at least 64 bytes in size. |
| ADDRMODE | Input | INT | I, Q, M, D, L or constant | This parameter defines how the data of the FETCH or WRITE job are addressed (in S7 or S5 address mode).  - 0 = S7 address mode   (Start address of the data is interpreted as a byte address) - 1 = S5 address mode   (Start address of the data is interpreted as a word address) |
| NDR | Output | BOOL | I, Q, M, D, L | new data record parameter:  This parameter shows that the data of the WRITE job has been successfully adopted and that the acknowledgement frame was generated and sent. |
| ERROR | Output | BOOL | I, Q, M, D, L | This parameter is set when:  - An error occurred establishing or terminating the connection - An error occurred during the sending or receiving of data. - An invalid FETCH/WRITE header frame was received. |
| MODE | Output | BYTE | I, Q, M, D, L | This parameter shows whether a FETCH or WRITE job was executed.  - 0 = No job active - 1 = WRITE job - 2 = FETCH job |
| [STATUS](#status-parameter-s7-300-s7-400) | Output | WORD | M, D | Internal communication status bits are output in the STATUS parameter. |

You can find additional information on valid data types under "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### STATUS parameter (S7-300, S7-400)

#### Structure of the STATUS parameter

The STATUS output parameter of the "FW_TCP" and "FW_IOT" instructions provides information on the status of the communication between S7 station and PC station.

This status word is structured as follows:

| Bit | Instance DB.FBStatus | Description |
| --- | --- | --- |
| **High byte** |  |  |
| 0 | NotConnected | No connection established or connection interrupted  - The FETCH/WRITE client has not yet initiated the establishment of the connection - Error during connection establishment |
| 1 | ErrorConnect | Error in connection establishment (for example: Error in the data structure of the connection parameter) |
| 2 | ErrorDisConnect | Error during connection termination |
| 3 | ErrorConType | Wrong connection type in the data structure of the connection parameters) |
| 4 | Not assigned |  |
| 5 | BusyConnect | Connection is being established |
| 6 | BusyDisConnect | Connection is being terminated |
| 7 | Not assigned |  |
| **Low byte** |  |  |
| 8 | ErrorRec1 | TCP connection:  - Error in receive job - FETCH/WRITE header frame could not be received   ISO-on-TCP connection  - Error in receive job - FETCH/WRITE header frame including user data could not be received |
| 9 | ErrorRec2 | TCP connection  - Error in receive job - User data could not be received |
| 10 | ErrorSend | TCP and ISO-on-TCP connection  - Error in send job - FETCH/WRITE acknowledgement frame including user data could not be sent |
| 11 | Not assigned |  |
| 12 | BusyRec1 | Receive job is running |
| 13 | BusyRec2 | Receive job is running |
| 14 | BusySend | Send job is running |
| 15 | ErrorHeader | Undefined FETCH/WRITE header frame received. |

#### Addresses and tags of the instance data block

The error status of the connection establishment and termination, and the error status of the send and receive job are stored in the instance data block of the instructions "FW_TCP" and "FW_IOT".

- The instance data block of the "FW_TCP" instruction comprises 8348 bytes.
- The instance data block of the "FW_IOT" instruction comprises 16544 bytes.

The following table shows an overview of the addresses and tags of the instance data block where the status is stored.

| Tag | Data type | Address | Description |
| --- | --- | --- | --- |
| DoneError.STATUS_Connect | WORD | 22.0 | Connection establishment status |
| DoneError.STATUS_REC_1 | WORD | 24.0 | Status of the first receive job |
| DoneError.STATUS_REC_2 | WORD | 26.0 | Status of the second receive job (only for TCP) |
| DoneError.STATUS_SEND | WORD | 28.0 | Status of the send job |
| DoneError.STATUS_DisConnect | WORD | 30.0 | Connection termination status |

#### Value of the STATUS parameter

The following table provides an overview of the status values of the connection establishment.

| STATUS (W#16#...) | Description |
| --- | --- |
| 0000 | Connection was established successfully. |
| 8086 | The ID parameter is outside the permitted range. |
| 8087 | Maximum number of connections reached; no additional connection possible. |
| 8089 | The CONNECT parameter does not point to a data block. |
| 809A | The CONNECT parameter points to a field that does not match the length of the connection description. |
| 809B | The local_device_id in the connection description does not match the CPU. |
| 80A1 | Connection or port is already in use. |
| 80A2 | Local or remote port is being used by the system. |
| 80A3 | Attempt is being made to terminate a non-existent connection. |
| 80A4 | IP address of the remote connection end point is invalid; for example, it matches the local partner's own IP address |
| 80B2 | The CONNECT parameter points to a data block that was generated with the keyword UNLINKED. |
| 80B3 | Inconsistent parameter assignment |
| 80B4 | You have violated one or more of the following conditions when establishing a connection passively (active_est = FALSE) with the ISO-on-TCP protocol variant (connection_type = B#16#12):  - local_tsap_id_len >= B#16#02 - local_tsap_id[1] = B#16#E0 |
| 80B6 | Parameter assignment error relating to the connection_type parameter |
| 80B7 | Error in the connection description |
| 80C3 | All connection resources are in use:  - Another block with this ID is already being processed in a different priority class. - Internal lack of resources. |
| 80C4 | Temporary communications error:  - The connection cannot be established at this time. - New parameter settings are being assigned to the interface. - The configured connection is currently being removed by the "TDISCON" instruction. |
| 82xx | General error information |
|  |  |

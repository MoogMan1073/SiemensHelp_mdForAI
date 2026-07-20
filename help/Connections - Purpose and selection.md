---
title: "Connections - Purpose and selection"
package: HWCConMeaning34enUS
topics: 12
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Connections - Purpose and selection

This section contains information on the following topics:

- [Introduction to configuring connections](#introduction-to-configuring-connections)
- [Points to note about configuring connections](#points-to-note-about-configuring-connections)
- [Range of applications of connection types (S7-300, S7-400, S7-1500)](#range-of-applications-of-connection-types-s7-300-s7-400-s7-1500)
- [Selecting connection types (S7-300, S7-400)](#selecting-connection-types-s7-300-s7-400)
- [Selection of connection types (S7-1500)](#selection-of-connection-types-s7-1500)
- [Instructions for communication tasks (S7-300, S7-400, S7-1500)](#instructions-for-communication-tasks-s7-300-s7-400-s7-1500)
- [Communication connections via CPs (S7-300, S7-400, S7-1500)](#communication-connections-via-cps-s7-300-s7-400-s7-1500)
- [Communication connections to PC stations (S7-300, S7-400, S7-1500)](#communication-connections-to-pc-stations-s7-300-s7-400-s7-1500)
- [Unspecified connections (S7-300, S7-400, S7-1500)](#unspecified-connections-s7-300-s7-400-s7-1500)
- [Programmed communication connections via CP (S7-300, S7-400, S7-1500)](#programmed-communication-connections-via-cp-s7-300-s7-400-s7-1500)
- [Connections with Open User Communication via CPU and CP](#connections-with-open-user-communication-via-cpu-and-cp)

## Introduction to configuring connections

### Why set up connections?

A communication connection, or connection, defines a logical assignment of two communication partners for performing communication services.

You can configure communication connections and under certain circumstances even set them up in a program-controlled manner.

This chapter shows you how to define connections, which special aspects you need to take into account, and which communication instructions you can use in the user program.

### Definition

A connection defines the following:

- Communication partner involved
- Type of connection (for example S7, ISO-on-TCP, ISO-Transport, FDL, UDP, e-mail or TCP connection)
- Special properties, such as

  - Setup characteristics

    A connection can remain permanently enabled or, if necessary, can be enabled and disabled.
  - Sending operating mode messages
- Communication path

  - within the devices (CPU - CP)
  - in the network (subnets / router)

### What you need to know about connection configuration

During connection configuration, one unique local ID is issued per connection. Only this local ID is needed when configuring the communication modules. The local ID is clearly assigned to the addresses of the local and remote connection partners.

If a connection endpoint refers to the application of a PC station, the connection name is used as "Local ID" for connection identification.

After the project is opened, the project-wide connection table is displayed. If you deselect the "Display all connections" check box in the shortcut menu of the connection table, only object-specific connections of selected objects are displayed. The created connections can be displayed separately for the following objects:

- Programmable modules that can be the endpoint of a connection
- Communications modules (CPs) used on the connection path
- Subnets

The addresses of the local and remote connection partners are set when the devices are networked and assigned to the connections during configuration. The following connections are an exception to this rule:

- Available UDP connection

  For the free UDP connection, the address at the communications interface is assigned in the user program.
- Programmed communication connection

  > **Note**
  >
  > The term "connection" is used under SIMATIC communication also with UDP. This is because the communication partners are assigned to one another and therefore logically "connected" during configuration. With the UDP, there is no explicit establishing of a connection between the communication partners.

### Networking and the path selection determine the configuration status

Depending on whether the connection partners are present in the project and networked, the address parameters of the connection endpoints can be fully or only partly specified.

- Fully specified

  - The addresses and network parameters of the local and remote communication partners are defined.
  - The communications connection is ready for operation after the connection parameters have been loaded to the device.
- Unspecified (partly specified)

  Only the local communication partner is defined. The partner for the selected connection type is either disconnected, is outside the project or is not defined because it requires special handling.

  Application case:

  - The complete networking of the devices is not yet possible, as the hardware configuration is not yet complete.
  - A ready-to-receive status has to be established for any (unspecified) communication partners.

  The communications connection is provisionally ready for operation after the connection parameters have been loaded to the device.

### Programmed communication connections

In certain application areas it is not beneficial to establish the communication connections statically via the the configuration. Alternatively, you can set up certain connection types in a program-controlled manner via a specific application, and therefore dynamically if necessary.

## Points to note about configuring connections

The network view provides you with a clearly structured platform for configuring communication connections between configured devices.

### Essential functions

- Graphic connection configuration in the network view

  You can create a connection graphically with only a few mouse clicks.
- Highlight possible connection partners

  You select a communication type - the possible communication partners are automatically highlighted.
- Automatic search for connection paths

  You arrange for the automatic assignment of the best possible connection path or the selection of alternative connection paths.
- Automatic transfer of configurations

  If you configure or network modules later on, connections that have already been configured and are supported by the module are automatically assigned.
- User-friendly selection of connection display

  If you select an object in the network view, for example a subnet or the interface for a module capable of communication, the associated configured connection link is displayed in the connection table.
- Taking into account available resources

  If connection resources are required for a connection type, any limitation specified during the creation of the connection will be taken into account. The maximum number of connection resources varies for both the CPU device types and for the CP device types.

![Essential functions](images/47041908491_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Connection display in the network view |
| ② | Connection table |
| ③ | "Properties" tab for a connection in the inspector window |

---

**See also**

[Overview of connection diagnostics](Device%20and%20network%20diagnostics.md#overview-of-connection-diagnostics)

## Range of applications of connection types (S7-300, S7-400, S7-1500)

### Introduction

The following sections provide a brief overview of the connection types that you can use for communication to specific device types and areas of application.

### Additional information

For more information on possible forms of communication in SIMATIC and the intended use of the connection types, refer the manual on communication with SIMATIC.

### S7 connections

The features of S7 connections include:

- Connection type can be used in all S7 devices
- Can be used on the following subnet types: MPI, PROFIBUS, Industrial Ethernet
- When using BSEND/BRCV SFBs: secure transfer of data between SIMATIC S7-400/1500 stations; e.g., exchange of data block contents (up to 64 Kbytes)
- With CPU 317-2 PN/DP and with CPU 31x and a CP and when using BSEND/BRCV FBs: secure transfer of data to S7-300, S7-400, and S7-1500
- When using USEND/URCV SFBs: rapid, unsecured transfer of data regardless of the time at which the communication partner processes it; for example for operating and maintenance messages
- Acknowledgement of data transfer from communication partner at layer 7 of the ISO reference model

### FDL connection

PROFIBUS-FDL (Fieldbus Data Link) is characterized by the following features:

- Transfer of data to a communication partner (for example SIMATIC S5 or PC), which supports sending and receiving according to the SDA function (Send Data with Acknowledge)
- Receipt of data is confirmed by the communication partner's FDL service using an acknowledgement
- Usable subnet type: PROFIBUS
- Corresponds to standard EN 50170 Vol.2 PROFIBUS
- Allows layer 2 of the ISO reference model to be assigned
- Interface in the S7 user program: SEND/RECEIVE;
- FDL services available as C functions on the PC

### ISO transport connection

The ISO transport connection is characterized by the following features:

- "Data blocking" suited to large volumes of data
- Communication to a partner (for example SIMATIC S5 or PC) which supports sending and receiving data in accordance with ISO transport
- Usable subnet type: Industrial Ethernet
- Receipt of data is confirmed by the communication partner's ISO transport service using an acknowledgement
- Interface in the S7 user program: SEND/RECEIVE and FETCH/WRITE;
- ISO transport service (ISO 8073 class 4) corresponds to layer 4 of the ISO reference model
- ISO transport services available as C functions on the PC

### ISO-on-TCP connection

The ISO-on-TCP transport connection is characterized by the following features:

- Corresponds to the standard TCP/IP (Transmission Control Protocol/Internet Protocol) with the RFC 1006 extension in accordance with layer 4 of the ISO reference model. RFC 1006 describes how the services from ISO layer 4 can be mapped on TCP
- Communication to a partner (for example PC or external system) which supports sending and receiving data in accordance with ISO-on-TCP
- Usable subnet type: Industrial Ethernet
- The receipt of data is confirmed using an acknowledgement
- Interface in the STEP 7 user program: SEND/RECEIVE and FETCH/WRITE;
- ISO-on-TCP transport services available as C functions on the PC

### TCP connection

The TCP connection is characterized by the following features:

- Corresponds to the standard TCP/IP (Transmission Control Protocol/Internet Protocol):
- Communication with a partner (for example PC or third-party system) that supports sending and receipt of data in compliance with TCP/IP
- Usable subnet type: Industrial Ethernet
- Interface in the STEP 7 user program: SEND/RECEIVE and FETCH/WRITE;
- TCP/IP implementation of the PC operating system can usually be used

### UDP connection

The UDP connection (User Datagram Protocol) is characterized by the following features:

- Usable subnet type: Industrial Ethernet (TCP/IP protocol)
- Unsecured transmission of related data fields between two nodes
- Interface in the S7 user program: SEND/RECEIVE.

### E-mail connection

The e-mail connection is characterized by the following features:

- Usable subnet type: Industrial Ethernet (TCP/IP protocol)
- Enables for example the sending of for example process data from data blocks via e-mail using a CP with IT functionality (IT-CP)
- The mail server with which all e-mails sent by an IT-CP are served is defined by the e-mail connection.

### FTP connection (specially set up TCP connection)

You use the FTP connection to process FTP order sequences.

When using the file transfer functions (FTP), CPs with IT functionality allow you to transfer files to and from the S7 devices.

### HMI connection

[Configuring HMI connections](Configuring%20devices%20and%20networks.md#configuring-hmi-connections)

---

**See also**

[USEND: Send data uncoordinated (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#usend-send-data-uncoordinated-s7-300-s7-400)
  
[URCV: Receive data uncoordinated (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#urcv-receive-data-uncoordinated-s7-300-s7-400)
  
[BSEND: Send data in segments (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#bsend-send-data-in-segments-s7-300-s7-400)
  
[BRCV: Receive data in segments (S7-300, S7-400)](S7%20communication%20%28S7-300%2C%20S7-400%29.md#brcv-receive-data-in-segments-s7-300-s7-400)
  
[USEND: Send data uncoordinated (S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#usend-send-data-uncoordinated-s7-1500)
  
[URCV: Receive data uncoordinated (S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#urcv-receive-data-uncoordinated-s7-1500)
  
[BSEND: Send data in segments (S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#bsend-send-data-in-segments-s7-1500)
  
[BRCV: Receive data in segments (S7-1500)](S7%20communication%20%28S7-1200%2C%20S7-1500%29.md#brcv-receive-data-in-segments-s7-1500)

## Selecting connection types (S7-300, S7-400)

### Selecting the connection type

Which type of connection you select depends on the required transmission properties, as well as on the subnet and transmission protocol by means of which the connection is established. In addition, the device type at each connection endpoint limits the connection types.

Which instructions or services you use at the interface (connection endpoints), depends on the connection type and the device type.

The following table shows these dependencies:

| Connection type | Subnet type / protocol | Device type: Connection between SIMATIC ... | Interface |
| --- | --- | --- | --- |
| S7 connection | MPI,  PROFIBUS,  Industrial Ethernet | S7 - S7, S7 - PG/PC, S7 - PG/PC with WinCC, PG/PC - PG/PC  S7 - partner in another project (S7, PG/PC with WinCC) | **Instructions for S7:** USEND, URCV, BSEND, BRCV, GET, PUT, START, STOP, RESUME, STATUS, USTATUS   **PG/PC:** OPC services or programming interfaces |
| FDL connection | PROFIBUS (FDL protocol) | S7 - S7, S7 - S5, S7 - PC/PG, S7 - external device, PG/PC - PG/PC  S7 - partner in another project (S7, S5, PG/PC, external device) | **Instructions for S7:**  AG_SEND,  AG_RECV,  AG_LSEND,  AG_LRECV    **PG/PC:** OPC services |
| ISO  transport connection | Industrial Ethernet (ISO transport protocol) | S7 - S7, S7 - S5, S7 - PC/PG, S7 - external device, PG/PC - PG/PC  S7 - unspecified  S7 - partner in another project (S7, S5, PG/PC, external device, unspecified) | **Instructions for S7:**  AG_SEND,  AG_RECV,  AG_LSEND,  AG_LRECV AG_LOCK AG_UNLOCK   **PG/PC:**OPC services |
| ISO-on-TCP  connection | Industrial Ethernet (TCP/IP protocol) | S7 - S7, S7 - S5,  S7 - PC/PG, S7 - external devices,  PG/PC - PG/PC, S7 - unspecified  S7 - partner in another project (S7, S5, PG/PC, external device, unspecified) | **Instructions for S7:**  AG_SEND,  AG_RECV,  AG_LSEND,  AG_LRECV AG_LOCK AG_UNLOCK   **PG/PC:**OPC services |
| TCP connection | Industrial Ethernet  (TCP/IP protocol) | S7 - S7, S7 - S5,  S7 - PC/PG, PG/PC - PG/PC S7 - external device,  S7 - unspecified  S7 - partner in another project (S7, S5, PG/PC, external device, unspecified) | **Instructions for S7:**  AG_SEND*,  AG_RECV*,  AG_LSEND**,  AG_LRECV**  AG_LOCK AG_UNLOCK   **PG/PC:**OPC services |
| UDP connection | Industrial Ethernet (TCP/IP protocol) | S7 - S7, S7 - S5, S7 - PC/PG, S7 - external device, S7 - unspecified  S7 - partner in another project (S7, S5, PG/PC, external device, unspecified) | **Instructions for S7:**  AG_SEND,  AG_RECV,  AG_LSEND,  AG_LRECV |
| E-mail connection | Industrial Ethernet (TCP/IP protocol) | S7 - unspecified (S7 - mail server),  S7 - PC/PG (S7 - mail server) | **Instructions for S7:**  AG_SEND,  AG_LSEND |
| FTP connection (specially set up TCP connection) | Industrial Ethernet (TCP/IP protocol) | S7 - unspecified | **Instructions for S7:**  FTP_CONNECT, FTP_STORE, FTP_RETRIEVE, FTP_DELETE, FTP_QUIT |

### Connection to broadcast and multicast nodes

> **Note**
>
> For special connection types, there is the option of selecting not just one connection partner but several (broadcast and multicast nodes). You can select the connection partner "Broadcast to all..." or "... multicast nodes" in the dialog box for entering a new connection.
>
> ● You can set up a connection to "all broadcast nodes" (sending to all broadcast recipients at the same time) for connections of the FDL and UDP connection type.
>
> ● You can set up a connection to "all multicast nodes" (sending to several nodes at the same time) for connections of the FDL and UDP connection type.

## Selection of connection types (S7-1500)

### Selection of connection type

You must decide on a communication service according to your automation task. The selection of communication service affects the following:

- The functionality that will be available
- The time at which the connection will be established
- The activities you will have to perform (e.g., configuring of connections, programming of instructions)

The table below provides an overview of the available communication services.

| Communication service | Functionality | Via interface: |  |  |
| --- | --- | --- | --- | --- |
| PN | DP | Serial |  |  |
| PG communication | For commissioning, test, diagnostics | X | X | - |
| HMI communication | For operator control and monitoring | X | X | - |
| I/O communication | Data exchange between e.g.:  - IO controllers and IO devices - DP master and DP slave | X | X | - |
| S7 communication | Data exchange between client and server or between clients: Configuration of connection required  Using PUT/GET, BSEND/BRCV, or USEND/URCV instructions | X | X | - |
| Open communication via TCP/IP | Data exchange via PROFINET with TCP/IP protocol  With connection configuration: TSEND_C/TRCV_C or TSEND/TRCV instructions  By means of user program only: TCON, TSEND, T_RCV, T_DISCON, or TSEND_C and TRCV_C instructions | X | - | - |
| Open communication via ISO-on-TCP | Data exchange via PROFINET with ISO-on-TCP protocol   With connection configuration: TSEND_C/TRCV_C or TSEND/TRCV instructions  By means of user program only: TCON, TSEND, T_RCV, T_DISCON, or TSEND_C and TRCV_C instructions | X | - | - |
| Open communication via UDP | Data exchange via PROFINET with UDP protocol  With connection configuration: TSEND_C/TRCV_C or TSEND/TRCV instructions  By means of user program only: TCON, TSEND, T_RCV, T_DISCON, or TSEND_C and TRCV_C instructions | X | - | - |
| Open communication via ISO (CPs with PN interface only) | Data exchange via PROFINET with ISO protocol  With connection configuration: TSEND_C/TRCV_C or TSEND/TRCV instructions  By means of user program only: TCON, TSEND, T_RCV, T_DISCON, or TSEND_C and TRCV_C instructions | X | - | - |
| Open communication via e-mail | Data exchange via e-mail  By means of user program only: TMAIL_C instruction | X | - | - |
| Open communication via FTP (CPs with PN interface only) | Data exchange via FTP (File Transfer Protocol)  By means of user program only: FTP_CMD instruction | X | - | - |
| Open communication via FDL (CMs with DP interface only) | Data exchange via PROFIBUS with FDL protocol  With connection configuration: TSEND_C/TRCV_C or TSEND/TRCV instructions  By means of user program only: TCON, TSEND, T_RCV, T_DISCON, or TSEND_C and TRCV_C instructions | - | X | - |
| Point-to-point connection | Data exchange via point-to-point with Freeport, 3964 (R), USS, or Modbus protocol  Using SEND_P2P/RCV_P2P or MB_COMM_LOAD, MB_MASTER, MB_SLAVE instructions | - | - | X |
| S7 routing | Data exchange across network boundaries, e.g., for parameter assignment, test, and diagnostic purposes | X | X | - |
| Data record routing | Extension of S7 routing, e.g., for parameter assignment and diagnostics of field devices on PROFIBUS by an engineering system with a PROFINET interface. | X | X | - |
| Web server | Data exchange via the Internet, e.g., for diagnostics | X | - | - |
| SNMP (Simple Network Management Protocol) | Data exchange via SNMP standard protocol, for network diagnostics and parameter assignment | X | - | - |
| Time-of-day synchronization | Via NTP (Network Time Protocol); CPU is client | X | - | - |
| CPU is time master or times slave | - | X | - |  |

### Connection to broadcast and multicast nodes

> **Note**
>
> For special connection types, there is the option of selecting not just one connection partner but several (broadcast and multicast devices). You can select the connection partner "To all broadcast..." or "... multicast devices" in the dialog box for entering a new connection.
>
> ● You can set up a connection to "all broadcast devices" (sending to all broadcast recipients at the same time) for FDL and UDP connection types.
>
> ● You can set up a connection to "all multicast devices" (sending to several devices at the same time) for FDL and UDP connection types.

## Instructions for communication tasks (S7-300, S7-400, S7-1500)

### Interface to user program

Special instructions are available for your communication interface in the SIMATIC S7-300/400/1500 user program. Here is an overview of the instructions for the individual connection types.

The PUT/GET instructions are used for the S7-1500. See the following tables for the instructions of the S7-300/400.

### Instructions for S7 connections

The system function blocks assigned to the instructions are integrated in the CPUs of the S7-400.

For S7-300 with more recent CPUs and CPs, you have the option of running the S7 communication actively (i.e. as client) via the CP's interface. The instructions have the same designation as the S7-400 SFBs, but must be called cyclically in the S7-300 CPU user program.

The CP must support the client function for S7 communication.

An S7-300 CPU with integrated PROFINET interface can also be configured as a client for S7 communication. The same blocks from the above scenario using S7-300 and CP are used. The client functionality is only available at the PROFINET interface.

| Name | Brief description |
| --- | --- |
| USEND  URCV | Uncoordinated exchange of data via a send and receive SFB   Max. length SFB 8/9: 440 bytes split into 4x100 bytes  Max. length FB 8/9: 160 bytes |
| BSEND  BRCV | Exchange of data blocks of variable lengths between a send SFB and a receive SFB  Max. length SFB 12/13: 64 KB  Max. length FB 12/13: 32 KB |
| GET | Read data from a remote device  Max. length SFB 14: 400 bytes split into 4x100 bytes  Max. length FB 14: 160 |
| PUT | Write data to a remote device  Max. length SFB 15: 400 bytes split into 4x100 bytes  Max. length FB 15: 160 |
| START | Run a restart (warm start) in a remote device |
| STOP | Put a remote device in "STOP" mode |
| RESUME | Run a resume process in a remote device |
| STATUS | Specific querying of the status of a remote device |
| USTATUS | Receipt of status messages from remote device |
| CONTROL | Query the status of the connection which belongs to an SFB instance |
| C_CNTRL | Query the status of a connection (for S7-300 CPUs) |

[Instructions for S7 communication](S7%20communication%20%28S7-300%2C%20S7-400%29.md#overview-of-the-s7-communication-instructions-s7-300-s7-400)

### Instructions for point-to-point connections

You can use the BSEND, BRCV, GET, PUT and STATUS SFBs for connections of the point-to-point connection type (see above table).

The PRINT SFB can also be used:

| Name | Brief description |
| --- | --- |
| PRINT | Send data to a printer |

### Instructions for FDL, ISO-on-TCP, UDP and TCP connections, as well as e-mail connection

| Name | Brief description |
| --- | --- |
| AG_SEND | Sends data via a configured connection to the communication partner (with older CPs and with CPs for S7-400, the following limitation applies to this FC: <= 240 bytes) |
| AG_RECV | Receives data via a configured connection from the communication partner (with older CPs and with CPs for S7-400, the following limitation applies to this FC:<= 240 bytes, not e-mail) |
| AG_LSEND | Sends data via a configured connection to the communication partner |
| AG_LRECV | Receives data via a configured connection to the communication partner (not e-mail) |
| AG_LOCK | Lock external data access using FETCH/WRITE (not with UPD, e-mail) |
| AG_UNLOCK | Unlock external data access using FETCH/WRITE (not with UPD, e-mail) |
| AG_CNTRL | Diagnose connections via the user program |

[Instructions for open communications services (SEND/RECEIVE interface)](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#instructions-for-open-communications-services-sendreceive-interface-s7-300-s7-400)

[Instructions for open communications services (SEND/RECEIVE interface)](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#instructions-for-open-communications-services-sendreceive-interface-s7-300-s7-400-1)

### Instructions for FTP services via TCP connections (FTP connection)

| Name | Brief description |
| --- | --- |
| FTP_CONNECT | Establish FTP connection |
| FTP_STORE | Transfer data block (file DB) from FTP client to FTP server |
| FTP_RETRIEVE | Transfer file from FTP server to FTP client |
| FTP_DELETE | Delete file from FTP server |
| FTP_QUIT | Quit the FTP connection stated by the ID |

[Instructions for FTP services](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#instructions-for-ftp-services-s7-300-s7-400)

### Instructions for programmed open communication services with ISO-on-TCP, UDP and TCP connections, as well as for e-mail connection via CPs

| Name | Brief description |
| --- | --- |
| IP_CONFIG | Set up program controlled communication connections and IP configuration of the CP. |

[Instructions for programmed connections](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#instructions-for-programmed-connections-s7-300-s7-400)

### Instructions for programmed open communication services (Open User Communication) with ISO-on-TCP, UDP and TCP connections via CPU or CP<sup>*) </sup>

*) Note: With these instructions, communication via CP is only possible using ISO-on-TCP.

| Name | Brief description |
| --- | --- |
| TCON | Connection establishment |
| TDISCON | Disconnection |
| TSEND | Sending data |
| TRCV | Receiving data |
| TUSEND | Sending of data; connectionless protocol UDP in accordance with RFC 768 |
| TURCV | Receiving of data; connectionless protocol UDP in accordance with RFC 768 |

[Overview](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#overview-s7-300-s7-400)

## Communication connections via CPs (S7-300, S7-400, S7-1500)

### Data volumes and configuration limit

The number of communication connections which are supported by the respective CP can be found in the equipment manual accompanying every CP. The number of connections per device can be increased by adding other CPs.

If several CPs are fitted in a device, an automatic switch is made to the next CP when this limit is exceeded. Specifically assign the connections using the path selection as required.

### Ethernet CP

The Ethernet CP can transfer the following data volumes via one connection per order:

|  | ISO transport | ISO-on-TCP | TCP | UDP |
| --- | --- | --- | --- | --- |
| Sending | 8192 bytes | 8192 bytes | 8192 bytes | 2048 bytes |
| Receiving | 8192 bytes | 8192 bytes | 8192 bytes | 2048 bytes |

> **Note**
>
> Data transfer > 240 byte transfer is supported by the current CPs.
>
> CPs with an older product version support the transfer of data with a data length of up to 240 bytes.
>
> For more information, refer to the details provided in the Ethernet CP equipment manual.

### Tasks of the Ethernet CP during online mode

During the transfer of data via a connection, the Ethernet CP takes on the following tasks:

- Receiving

  Receiving data from the Ethernet and forwarding to the user data area in the CPU
- Sending

  Transferring data from the user data area of the CPU and sending data via the Ethernet

The connection is established automatically as soon as the partner can be reached.

With a free UDP/FDL connection, the following also applies:

- When receiving

  Entering the sender who sent the message in the order header
- When sending

  Evaluating the order header and addressing the partner

### PROFIBUS-CP

The PROFIBUS CP can transfer the following data volumes via one connection per order:

| FDL connection type | Specified | Unspecified - free layer 2 access | Broadcast | Multicast |
| --- | --- | --- | --- | --- |
| Sending | 240 bytes | 236 bytes <sup>1)</sup> | 236 bytes <sup>1)</sup> | 236 bytes <sup>1)</sup> |
| Receiving | 240 bytes | 236 bytes <sup>1)</sup> | 236 bytes <sup>1)</sup> | 236 bytes <sup>1)</sup> |

<sup>1) The order header also assigns 4 bytes alongside the user data stated</sup>

### Tasks of the PROFIBUS CP during online mode

When processing the transfer of data via an FDL connection, the PROFIBUS-CP takes on the following tasks:

- With specified connections

  - Receiving

    Receiving data from the PROFIBUS and forwarding to the user data area in the CPU
  - Sending

    Transferring data from the user data area of the CPU and sending data via the PROFIBUS
- With unspecified connections also

  - When receiving

    Entering the sender and FDL service in the order header
  - When sending

    Evaluating the order header and addressing the partner; performing the selected FDL service

## Communication connections to PC stations (S7-300, S7-400, S7-1500)

### Connection endpoints of a PC station

On PC stations, you configure connections with one of the following components as connection endpoint:

- OPC server as central communication service provider

  Depending on the available CP, you can use the following connection types:

  - S7 connection
  - ISO connection
  - ISO-on-TCP connection
  - TCP connection
  - FDL connection
- Standard application

  With the S7 connection type, communication is possible via Ind. Ethernet or PROFIBUS, depending on the available CP.

> **Note**
>
> **CPU 1515SP PC as router for S7 connections**
>
> If you assign the "PROFINET onboard [X2]" interface to the CPU 1515SP PC of the SIMATIC PC station, the CPU 1515SP PC can be used as a router for S7 connections. With the setting "None, or a different Windows setting" on the CP interface "PROFINET onboard [X2]" , it is not possible to use the CPU 1515SP PC as a router for routed S7 connections.   
> An existing S7 connection routed by the CPU 1515SP PC becomes invalid if the assignment of the interface of the CPU 1515SP PC is changed from "SIMATIC PC station" to "None, or a different Windows setting". Since the PLC now no longer handles routing functions for this connection, when the CPU 1515SP PC is compiled, no message relating to the invalid connection is displayed. The invalid routed S7 connection is displayed only when the end points of the connection are compiled.   
> The interfaces required for routed S7 connections must remain explicitly assigned on the CPU 1515SP PC . You can edit the assignment of the interface of the CPU 1515SP PC in the properties under "PROFINET onboard [X2] > Interface assignment".

### Special features of the connection configuration with OPC server

In the case of connections with OPC as connection endpoint, more connections can generally be configured than can be operated at any time in the CP used in the PC stations.

That is because by the connection properties differentiate between "Maintain permanently" and "Set up on demand".

Accordingly, the number of connections with the property "Maintain permanently" cannot exceed the maximum number of CP connection resources. If it proves possible to establish additional connections on demand, you have to keep free the CP's corresponding connection resources. Therefore, configure a smaller number connections with the property "Maintain permanently" than the maximum number of CP connection resources permits.

A warning may possibly be indicated during the compiling of the connection configuration.

### Additional information

Industrial communication with the PG/PC Band 1 under the entry ID: [42783968](http://support.automation.siemens.com/WW/view/en/42783968)

Industrial communication with the PG/PC Band 2 under the entry ID: [42783660](http://support.automation.siemens.com/WW/view/en/42783660)

Commissioning PC stations - Manual under the entry ID: [13542666](http://support.automation.siemens.com/WW/view/en/13542666)

---

**See also**

Software components of a PC station

## Unspecified connections (S7-300, S7-400, S7-1500)

### Unspecified connections with Industrial Ethernet

Connections to an as yet unknown device (for example a diagnostics device) are configured as "unspecified" connections. The unspecified connection can be used in different ways as explained below based on the example of an ISO-on-TCP connection; on an ISO transport or TCP connection, the procedure is analogous.

- **Declaring ready for communication - passive connection establishment**

  Connection establishment must be set to "passive".

  The following then applies to the address setting for an ISO-on-TCP connection:

  the remote IP address and the remote TSAP are empty, in other words, they are not relevant for the CP. During connection establishment, every partner is then accepted (partner = connection name that addresses the CP with the correct IP address and TSAP).

  There is also the option of partial specification, in other words, the communication is permitted with any partner that matches the specified TSAP.
- **Connection to a specific station in any project.**

  The following then applies to the address setting for an ISO-on-TCP connection:

  You can specify the remote IP address and the port for any target station. The target station can be inside or outside of the current STEP 7 project.

  Use this variant if you have not created the partner station in the current project.
- **Connection without specifying a port**

  TCP connections are unspecified in the following situations:

  - The local port is not specified (active connection establishment).
  - The remote port is not specified (no active connection establishment).
- **IP addressing using DHCP**

  If you select the option of IP addressing using DHCP, it is not initially possible to create a fully specified connection in the project because the local IP address is unknown. You will therefore have to select "Unspecified" without active connection establishment as the connection type.

The following table summarizes the possibilities for setting the "remote" address parameters:

| Significance of the connection establishment | IP address / MAC address (remote) | TSAP / port (remote) | Active connection establishment |
| --- | --- | --- | --- |
| By either partner | Empty | Empty | no |
| By either partner via a specific TSAP | Empty | Specified | no |
| To or from a specific partner | Specified | Specified | yes The local port can remain unspecified (but does not need to). |
| Unspecified | no |  |  |

The free UDP connection represents a further variant. With this type of connection, the address of the connection partner remains open in the configuration. The communication stations are determined by address information in the communication job of the user program.

### Unspecified connections on PROFIBUS

An unspecified FDL connection with open layer 2 access enables program-controlled addressing of the communication partner and communication between two stations on PROFIBUS with the following properties:

The local station is specified by configuration. The remote node is entered by the user program in the job header of the job buffer with the AG_SEND instruction call. This means that each node on PROFIBUS (PROFIBUS addresses from 0 to 126) can be reached.

### Additional information

You will find further information below in the sections describing specific connections.

[Free UDP connection](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#free-udp-connection-s7-300-s7-400-s7-1500)

[FDL unspecified FDL connection (free layer 2 access)](Connection%20types%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#fdl-unspecified-fdl-connection-free-layer-2-access-s7-300-s7-400)

## Programmed communication connections via CP (S7-300, S7-400, S7-1500)

### Range of application

In certain applications it is advantageous not to set up the communication connections or the IP configuration of the CP via the configuration interface, but rather to set up these connections in a program-controlled manner using a specific application.

You have the option of freely configuring the communication connections in a program-controlled manner via industrial Ethernet CPs. Keep in mind the system performance of the CP type you are using.

Typical application cases are, for example, with manufacturers of standard machines. To be able to offer most comfortable interfaces to their clients, these manufacturers adapt the communication services to the respective operator inputs. The end users require no knowledge about how to configure connections.

The IP_CONFIG instruction is available for these applications, which permits the flexible transfer of data blocks with configuration data to an Ethernet CP.

### Interaction of programming and configuration

Connections are either configured or configured by the user program as the S7 device is running. A mixed form of these variants is not possible within one CP!

### Principle

Configuration data for communication connections are transferred to the CP via the IP_CONFIG instruction in the user program.

The configuration DB can be loaded in this manner in the CP at any time. The previous connections and configuration data (IP address, subnet mask, default router, NTP time server and other parameters) are then overwritten.

The Ethernet CP uses the configuration data to detect whether the communication connections are to be set up using the user program.

### Scale

A maximum of 64 connections can be specified in the IP_CONFIG instruction. However, the maximum number of connections supported by the CP type you are using is decisive.

### Special features/constraints

- Consistency check only with configured connection

  The connection configuration is linked to consistency checks which are not possible or are only partly possible with the programmed configuration.
- Connection configuration by partner needed

  When configuring specified connections, the connection for the partner is implicitly created during configuration. This is not possible with a programmed configuration. In this case, appropriate consistent connections must be configured for the partners.
- Configuration of IP access protection

  IP access protection can be used to limit communication via the CP of the local S7 device to partners with very specific IP addresses. This parameter assignment also applies to programmed communication connections.
- DHCP/DNS is supported

  IP addressing is also possible via DHCP/DNS for the programmed configuration.

---

**See also**

[Overview (S7-300, S7-400)](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#overview-s7-300-s7-400)

## Connections with Open User Communication via CPU and CP

### Open User Communication via Industrial Ethernet - programmed communication connections

Open User Communication provides Industrial Ethernet services that you use via the instruction interface in the user program. Communication connections are set up via the instruction interface in the user program; it is not necessary to configure the connections.

### Services via the CPU's interface

These Open User Communication services are available with S7-1500 and S7-1200 as of FW V4.5 for data exchange as well as via configured connections over the integrated Ethernet interface of a CPU:

- TCP as per RFC 793
- ISO-on-TCP as per RFC 1006
- UDP as per RFC 768 (broadcast or unicast, no support for multicast)

### Services via the CP's interface

These Open User Communication services are available with S7-300/400/1500 for data exchange via the Ethernet interface of a CP:

- TCP as per RFC 793
- ISO as per RFC 905 (only S7-1500)
- ISO-on-TCP as per RFC 1006
- UDP as per RFC 768 (broadcast or unicast, no support for multicast)

---

**See also**

[Functional description of instructions for Open User Communication via Industrial Ethernet (S7-300, S7-400)](Open%20User%20Communication%20%28S7-300%2C%20S7-400%29.md#functional-description-of-instructions-for-open-user-communication-via-industrial-ethernet-s7-300-s7-400)

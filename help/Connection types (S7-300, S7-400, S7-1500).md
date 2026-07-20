---
title: "Connection types (S7-300, S7-400, S7-1500)"
package: HWCConProp34enUS
topics: 52
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Connection types (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [S7 connection (S7-300, S7-400, S7-1500)](#s7-connection-s7-300-s7-400-s7-1500)
- [ISO transport connection (S7-300, S7-400, S7-1500)](#iso-transport-connection-s7-300-s7-400-s7-1500)
- [ISO-on-TCP connection (S7-300, S7-400, S7-1500)](#iso-on-tcp-connection-s7-300-s7-400-s7-1500)
- [TCP connection (S7-300, S7-400, S7-1500)](#tcp-connection-s7-300-s7-400-s7-1500)
- [UDP connection (S7-300, S7-400, S7-1500)](#udp-connection-s7-300-s7-400-s7-1500)
- [FETCH/WRITE mode (S7-300, S7-400)](#fetchwrite-mode-s7-300-s7-400)
- [FDL connection (S7-300, S7-400)](#fdl-connection-s7-300-s7-400)
- [E-mail connection (S7-300, S7-400, S7-1500)](#e-mail-connection-s7-300-s7-400-s7-1500)
- [Point-to-point link (S7-300, S7-400, S7-1500)](#point-to-point-link-s7-300-s7-400-s7-1500)

## S7 connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [S7 connection - general settings (S7-300, S7-400, S7-1500)](#s7-connection---general-settings-s7-300-s7-400-s7-1500)
- [S7 connection - address details (S7-300, S7-400, S7-1500)](#s7-connection---address-details-s7-300-s7-400-s7-1500)

### S7 connection - general settings (S7-300, S7-400, S7-1500)

#### General connection parameters

General connection parameters are displayed in the "General" parameter group under the properties of the connection; these connection parameters identify the local connection endpoint.

Here, you can assign the connection path and specify all aspects of the connection partner.

#### Local ID

The local ID of the module from which the connection is viewed is displayed here (local partner). You can change the local ID. You may need to do this if you have already programmed communication function blocks, and you want to use the local ID specified in those function blocks for the connection.

#### Special connection properties

Display of connection properties (can be modified depending on the components used):

- Configured at one end

  Configured at one end means that the connection partner functions as a server on this connection and cannot send or receive actively.

  Communications instructions used at both ends (with "pairs of blocks") cannot be used on connections configured at one end; for example [USEND](S7%20communication%20%28S7-300%2C%20S7-400%29.md#usend-send-data-uncoordinated-s7-300-s7-400) and [URCV](S7%20communication%20%28S7-300%2C%20S7-400%29.md#urcv-receive-data-uncoordinated-s7-300-s7-400), [BSEND](S7%20communication%20%28S7-300%2C%20S7-400%29.md#bsend-send-data-in-segments-s7-300-s7-400) and [BRCV](S7%20communication%20%28S7-300%2C%20S7-400%29.md#brcv-receive-data-in-segments-s7-300-s7-400) or [USTATUS](S7%20communication%20%28S7-300%2C%20S7-400%29.md#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400).
- Active connection establishment

  Use this option to specify whether the connection is established from this device.

  If you selected "Unspecified" as the connection partner when you created the connection, the option is deselected by default. If you select this option, you must specify the address of the partner in the "Addresses" tab.
- Send operating mode messages

  Indicates whether or not the local partner sends operating mode messages to the connection partner.

#### Address details

Displaying address details of the S7 connection. With an unspecified partner, the values for the rack and slot can be changed. All other values are obtained from the current configuration and cannot be changed.

### S7 connection - address details (S7-300, S7-400, S7-1500)

#### Meaning

A connection resource such as shown under "Properties > Address details" is part of the TSAP (Transport Service Access Point) of the local module or partner.

When a connection is established, the connection-specific resources of a module are assigned permanently to this connection. This assignment requires that the connection resource can be addressed. The TSAP (Transport Service Access Point) is, as it were, the address of the resource that is formed with the help of the connection resource or, in the case of S7-1500 CPUs, with SIMATIC-ACC (SIMATIC Application Controlled Communication).

The ability to use connection resources is subject to rules and restrictions. For example, not every connection resource can be used for every connection type.

#### Structure of the TSAP

- For S7-1500 CPU:

  "SIMATIC-ACC"<nnn><mm>

  nnn = Local ID

  mm = any value
- For S7-300/400 CPU:

  <xx>.<yz>

  xx = Number of the connection resource

  y = Rack number

  z = Slot number

#### TSAP structure, dependent on partner

The configuration of the TSAP for S7-1500 CPUs is dependent on the remote connection partner. When an S7-1500 CPU is connected to an S7-300/400 CPU, an S7-1500 CPU also uses a TSAP configuration that includes the connection resource.

See the following examples of TSAPs of various connection configurations

- Connection between two S7-1500 CPUs:

  - S7-1500 CPU "A" with local ID 200:

    TSAP: SIMATIC-ACC20001
  - S7-1500 CPU "B" with local ID 3B2:

    TSAP: SIMATIC-ACC3B201
- Connection between S7-1500 CPU and S7-300/400 CPU:

  - S7-1500 CPU (rack 0, slot 1, connection resource 10):

    TSAP: 10.01
  - S7-300/400 CPU (rack 0, slot 2, connection resource 11):

    TSAP: 11.02

#### Value ranges of connection resource

The following table provides information on the meaning of the values and the type of connection. Depending on the connection partner and connection type, the range of values is automatically limited to valid values or the value of the connection resource is assigned permanently.

| Connection resource  (1st byte of TSAP) | Meaning | Type | Meaning |
| --- | --- | --- | --- |
| 0x01 ("PG") | Programming device connection | Free connection (not configured) | At least one resource per CPU is reserved for programming device connections. However, for certain S7-300 CPUs it is possible to reserve multiple resources in the CPU properties. |
| 0x02 ("OP") | OP connection | Free connection (not configured) | At least one resource per CPU is reserved for OP connections. However, for certain S7-300 CPUs it is possible to reserve multiple resources in the CPU properties. |
| 0x03 | Other | Free connection (configured, unspecified connection) | This connection resource can operate multiple connections. Use: Connection configured at one end with unspecified connection partner! The connection partner does not have to be configured if the connection resource 0x03 is addressed. |
| 0x10..0xDF | Connections with static or dynamic connection setup | Configured unspecified connection | One of these connection resources can operate one (and only one) connection. Use: Connection configured at both ends with unspecified connection partner! |

#### Free S7 connections

Free S7 connections are set up dynamically during runtime; the following connections are free:

- Programming device connections (0x01)

  S7 connections that are typically set up from a programming device or from a PC (with ES functionality). This type of connection is used to configure and program the addressed station/module as well as to test and commission it; afterwards, the connection is typically cleared again. This connection resource allows both read and write access (e.g., monitoring and loading).
- OP connections (0x02)

  S7 connections that are typically set up from an OP or from a PC (with OS functionality). This type of connection is used to monitor the addressed station/module with regard to the process that is being controlled.
- Other (0x03)

  Use is not specified. For example, this resource is used automatically when an S7 connection configured at both ends is configured from an S7-400 to an S7-300.
- S7 basic communication (0xFD)

  Connections that are typically set up from a CPU to another module (CPU, FM, etc.) within a subnet. The connection setup is initiated by the application program, in which a connection configuration does not exist. This type of connection allows process data to be exchanged between the modules. For certain S7-300 CPUs, it is possible to reserve resources for S7 basic communication.

#### Recommendation for selection of the connection resource

STEP 7 always suggests a free connection resource for the local partner. We recommend that you accept it.

## ISO transport connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [ISO transport – special connection properties (S7-300, S7-400, S7-1500)](#iso-transport-special-connection-properties-s7-300-s7-400-s7-1500)
- [ISO OPC establishment details (S7-300, S7-400, S7-1500)](#iso-opc-establishment-details-s7-300-s7-400-s7-1500)
- [ISO transport address details (S7-300, S7-400, S7-1500)](#iso-transport-address-details-s7-300-s7-400-s7-1500)
- [ISO transport options (S7-300, S7-400, S7-1500)](#iso-transport-options-s7-300-s7-400-s7-1500)
- [ISO transport - dynamics (S7-300, S7-400, S7-1500)](#iso-transport---dynamics-s7-300-s7-400-s7-1500)
- [ISO OPC properties (S7-300, S7-400, S7-1500)](#iso-opc-properties-s7-300-s7-400-s7-1500)

### ISO transport – special connection properties (S7-300, S7-400, S7-1500)

#### Relevance

You can specify additional properties of the local connection endpoint in the "Properties > General > Special connection properties" parameter group.

#### Establishing an active connection

Use this option to specify whether the connection is established from this device. This is the default option if the address of the partner is specified.

- ON: Connection is established actively.
- OFF: Connection is established by the partner.

If you selected "Unspecified" as the connection partner when you created the connection, the option is deselected by default. If you select the option you must specify the address of the partner in the "Addresses" tab.

> **Note**
>
> **Effect on the mode**
>
> Note the effect on the mode.
>
> - S7-300 / S7-400
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), disable the "Active connection establishment" option.
> - OPC server
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), enable the "Active connection establishment" option.

#### Name

A connection endpoint name is proposed here when you create the connection. This name contains a connection number as suffix.

Use this field to identify the partner on unspecified connections.

### ISO OPC establishment details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > Establishment details".

#### Options for connection establishment

Entries in this area are possible only if you have selected active connection establishment in "Special connection properties".

Choose from the two following alternatives:

- Keeping the connection established permanently

  The connection is established permanently when you start up the PC station and is re-established following an interruption on the connection.
- Establishing the connection on request (access to tag)

  You can also specify how long the connection should stay up after access.

#### Monitoring connection establishment

- Timeout: Error wait time during the connection establishment

  If, during this wait time, the connection cannot be established, the connection is reset and a pending request acknowledged with an error.

  Range of values: 0 to 99999 ms

  Default: 15000 ms

  > **Note**
  >
  > The connection establishment monitoring that can be set here, has the following relationship with the time monitoring that can be set in the module configuration: The lower value is valid.
  >
  > Time monitoring can be configured in the module configuration in "Properties Ethernet interface".

### ISO transport address details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Address parameter

An ISO transport connection is specified by the local and remote connection endpoint.

- Local addresses:  
  Local MAC address and local TSAP (Transport Service Access Point)
- Remote addresses:  
  Remote MAC address and remote TSAP

  ![Sending and receiving via one ISO transport connection each](images/142903870219_DV_resource.Stream@PNG-en-US.png)

  Sending and receiving via one ISO transport connection each

#### TSAP format

ISO transport connections have a TSAP length of 1 to 16 bytes. For the entry the actual length is displayed automatically (visible display: 16 ASCII characters). Local and remote TSAPs can be entered as a hexadecimal value or as an ASCII string. For ASCII input, the entered characters are also displayed in hexadecimal. With hexadecimal input, printable characters are shown as an ASCII value (8 hexadecimal characters are visible). If non-printable characters are entered, the ASCII display is greyed out (ASCII input is no longer possible) and the non-printable characters are shown as periods.

#### Local and remote TSAPs

Remote and local TSAPs can be identical because the connection through the different MAC addresses is unique. If more than one connection is to be set up between two stations, the TSAPs must differ.

- Specified connection

  The TSAPs of an ISO transport connection must agree as follows:

  - Remote TSAP (on the Ethernet CP) = local TSAP (on the target station)
  - Local TSAP (on the Ethernet CP) = remote TSAP (on the target station)
- Unspecified connection

Some address parameters are not specified: [Unspecified connections](Connections%20-%20Purpose%20and%20selection.md#unspecified-connections-s7-300-s7-400-s7-1500)

#### Default TSAPs

Default values (changeable) are recommended for configuring local and remote TSAPs (for example ISO-1 for the first connection between two partners). If new connections are configured between the same partners, the default values will be incremented automatically (for example ISO-2, etc.). For a new connection to a new partner, the default value will start with ISO-1 again.

### ISO transport options (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Options".

#### Operating modes

- **SEND/RECV:**

  This is the standard mode with the AG_SEND/AG_LSEND, and AG_RECV/AG_LRECV FCs.
- **FETCH/WRITE:**

  System memory areas in the SIMATIC S7 can be accessed from the following devices if you select one of the operating modes below for the ISO transport connection:

  - SIMATIC S5
  - SIMATIC PC stations
  - Third-party devices

  The connection can then only be used for this mode. It will not be possible to send or receive via the AG_SEND/AG_LSEND or AG_RECV/AG_LRECV instructions.

  - FETCH

    Selecting the operating mode Fetch enables direct read access to data areas in the SIMATIC S7. Access can, for example, be from a SIMATIC S5 station or a third-party station.
  - WRITE

    Selecting the operating mode Write enables direct write access to data areas in the SIMATIC S7. Access can, for example, be from a SIMATIC S5 station or a third-party station.
- **SPEED SEND/RECV:**

  Selecting the SPEED SEND/RECV mode allows you to use the AG_SSEND and AG_SRECV instructions.

  AG_SSEND/AG_SRECV (SPEED SEND/RECEIVE) provide faster and therefore optimized transmission within a S7-400 station. Check the device documentation of the CP you are using to see whether this operating mode is supported by the CP and in conjunction with the selected CPU.

#### FETCH/WRITE requirements: Mode of connection establishment

Please select one of the following options in the parameter group "Properties > General > Special connection properties" in line with the station type for connection establishment.

- SIMATIC S7 station: PASSIVE connection establishment
- PC station: Active connection establishment

#### "S7 addressing mode" option (for FETCH/WRITE only)

You can select the addressing mode when you configure the FETCH ACTIVE/WRITE ACTIVE mode.

- S7 addressing mode: Byte address
- S5 addressing mode: Word address

This allows applications to access S5 or S7 stations without modifying the addresses. This is particularly useful for existing S5 applications, for example, that can now be used unchanged when accessing S7 stations.

The addressing mode for accessing SIMATIC S7 (option selected) is set by default.

---

**See also**

[Connection configuration for FETCH/WRITE (S7-300, S7-400)](#connection-configuration-for-fetchwrite-s7-300-s7-400)
  
[Use of FETCH/WRITE (S7-300, S7-400)](#use-of-fetchwrite-s7-300-s7-400)

### ISO transport - dynamics (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Dynamics".

The relevant timers and counters for this connection are displayed. You can accept these default values.

Where necessary (for example when linking to third-party systems), you can also set the timers and counters individually to achieve the required dynamic response of the connection.

### ISO OPC properties (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > OPC".

Here, you set connection-specific properties for an ISO transport connection used by the OPC server.

You can set the following parameters:

#### Timeout for job

If a pending job cannot be processed during the wait time set here, the connection is reset and the job acknowledged with an error.

Range of values: 0 to 99999 ms

- Default setting: 15000 ms

#### Send buffer size

Default size of the default send buffer. Additional send buffers of any length (up to 65535 bytes) may be used at runtime.

Range of values:

- Default setting: 256 bytes

- Range of values: 65535 bytes maximum

#### "Optimization of direct access for tag services" option

If you use this option, the OPC server attempts to combine direct accesses to several tags to minimize the number of jobs that need to be sent.

This option is enabled by default.

#### "Immediate response when interrupted connection is detected" option

If you select this option, you specify that the application is notified that a communication job (FETCH, or WRITE) cannot be executed when a connection is unavailable. The code is sent regardless of whether or not a current attempt to establish the connection succeeds.

If you do not select this option, the application is informed of the nonavailability of a connection only when the connection times out.

The option described here is relevant and available only when the two modes listed below are used:

- The connection is configured as a permanent connection.

  Connections can be configured as permanently established connections (in "Details of connection establishment"). This means that jobs can be forwarded to the partner with the shortest possible reaction time without needing to establish the connection first.

  If there is a disruption on the connection, the system automatically attempts to re-establish the connection. In this situation, there may be delays before a message can be forwarded to the application.
- You are using the FETCH or WRITE job types (can be selected in "Options").

Only with these job types is an immediate reaction necessary in certain situations if there is no connection.

## ISO-on-TCP connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [ISO-on-TCP - special connection properties (S7-300, S7-400, S7-1500)](#iso-on-tcp---special-connection-properties-s7-300-s7-400-s7-1500)
- [ISO-on-TCP OPC establishment details (S7-300, S7-400, S7-1500)](#iso-on-tcp-opc-establishment-details-s7-300-s7-400-s7-1500)
- [ISO-on-TCP address details (S7-300, S7-400, S7-1500)](#iso-on-tcp-address-details-s7-300-s7-400-s7-1500)
- [ISO-on-TCP general (S7-300, S7-400, S7-1500)](#iso-on-tcp-general-s7-300-s7-400-s7-1500)
- [ISO-on-TCP OPC properties (S7-300, S7-400, S7-1500)](#iso-on-tcp-opc-properties-s7-300-s7-400-s7-1500)

### ISO-on-TCP - special connection properties (S7-300, S7-400, S7-1500)

#### Relevance

You can specify additional properties of the local connection endpoint in the "Properties > General > Special connection properties" parameter group.

#### Active connection establishment

Use this option to specify whether the connection is established from this device. This is the default option if the address of the partner is specified.

- ON: Connection is established actively.
- OFF: Connection is established by the partner.

If you selected "Unspecified" as the connection partner when you created the connection, the option is deselected by default. If you select the option you must specify the address of the partner in the "Addresses" tab.

> **Note**
>
> **Effect on the mode**
>
> Note the effect on the mode.
>
> - S7-300 / S7-400
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), disable the "Active connection establishment" option.
> - OPC server
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), enable the "Active connection establishment" option.

#### Name

A connection endpoint name is proposed here when you create the connection. This name contains a connection number as suffix.

Use this field to identify the partner on unspecified connections.

### ISO-on-TCP OPC establishment details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > Establishment details".

#### Options for connection establishment

Entries in this area are possible only if you have selected active connection establishment in "Special connection properties".

Choose from the two following alternatives:

- The connection is established permanently

  The connection is established permanently when you start up the PC station and is re-established following an interruption on the connection.
- The connection is established when it is required (access to tag)

  You can also specify how long the connection should stay up after access.

#### Connection establishment monitoring

Timeout: Error wait time during the connection establishment

If, during this wait time, the connection cannot be established, the connection is reset and a pending request acknowledged with an error.

Range of values: 0 to 99999 ms

Default: 15000 ms

> **Note**
>
> The connection establishment monitoring that can be set here, has the following relationship with the time monitoring that can be set in the module configuration: The lower value is valid.
>
> Time monitoring can be configured in the module configuration in "Properties Ethernet interface".

### ISO-on-TCP address details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Address parameter

A connection is specified through the local and remote connection endpoint.

- Local addresses:  
  Local IP address and local TSAP (Transport Service Access Point)
- Remote addresses:  
  Remote IP address and remote TSAP

  ![Sending and receiving via an ISO-on-TCP transport connection](images/142903874315_DV_resource.Stream@PNG-en-US.png)

  Sending and receiving via an ISO-on-TCP transport connection

#### Addresses tab

In the Addresses tab the relevant local and remote address information is displayed as recommended values. You have the possibility of setting the TSAPs individually.

#### TSAP format

ISO-on-TCP connections have a TSAP length of 1 to 16 bytes. For the entry the actual length is displayed automatically (visible display: 16 ASCII characters). Local and remote TSAPs can be entered as a hexadecimal value or as an ASCII string. For ASCII input, the entered characters are also displayed in hexadecimal. With hexadecimal input, printable characters are shown as an ASCII value (8 hexadecimal characters are visible). If non-printable characters are entered, the ASCII display is greyed out (ASCII input is no longer possible) and the non-printable characters are shown as periods.

#### Local and remote TSAPs

Remote and local TSAPs can be identical because the connection through the different IP addresses is unique. If more than one connection will be set up between two stations then the TSAPs must also differ.

- Specified connection

  In the configuration of the Ethernet CP and the Ethernet target Station, the TSAPs of an ISO-on-TCP connection must be crossed over.

  - Remote TSAP (on the Ethernet CP) = local TSAP (on the target station)
  - Local TSAP (on the Ethernet CP) = remote TSAP (on the target station)
- Unspecified connection

  Some address parameters are not specified: [Unspecified connections](Connections%20-%20Purpose%20and%20selection.md#unspecified-connections-s7-300-s7-400-s7-1500)

#### Default TSAPs

For configuration of local and remote TSAPs there is a default value "TCP-1" for the first connection between both partners (changeable). For a new connection between the same partners the standard value "TCP-2" is suggested. For a new connection to a new partner TCP-1 is started again.

### ISO-on-TCP general (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Options".

#### Operating modes

- **SEND/RECV:**

  This is the standard mode with the AG_SEND/AG_LSEND, and AG_RECV/AG_LRECV FCs.
- **FETCH/WRITE:**

  System memory areas in the SIMATIC S7 can be accessed from the following devices if you select one of the operating modes below for the ISO transport connection:

  - SIMATIC S5
  - SIMATIC PC stations
  - Third-party devices

  The connection can then only be used for this mode. It will not be possible to send or receive via the AG_SEND/AG_LSEND or AG_RECV/AG_LRECV instructions.

  - FETCH

    Selecting the operating mode Fetch enables direct read access to data areas in the SIMATIC S7. Access can for example be from a SIMATIC S5 station or a third-party station.
  - WRITE

    Selecting the operating mode Write enables direct write access to data areas in the SIMATIC S7. Access can for example be from a SIMATIC S5 station or a third-party station.
- **SPEED SEND/RECV:**

  Selecting the operating mode SPEED SEND/RECV allows you to use the instructions AG_SSEND and AG_SRECV.

  AG_SSEND/AG_SRECV (SPEED SEND/RECEIVE) provide faster and therefore optimized transmission within a S7-400 station. Check the device documentation to see whether this operating mode is supported by the CP used.

#### FETCH/WRITE requirements: Mode of connection establishment

Please select one of the following options in the parameter group "Properties > General > Special connection properties" in line with the station type for connection establishment.

- SIMATIC S7 station: PASSIVE connection establishment
- PC station: Active connection setup

#### "S7 addressing mode" option (for FETCH/WRITE only)

You can select the addressing mode when you configure the FETCH ACTIVE/WRITE ACTIVE mode.

- S7 addressing mode: Byte address
- S5 addressing mode: Word address

This allows applications to access S5 or S7 stations without modifying the addresses. This is, for example, an interesting option for existing S5 applications that are now to be used unchanged to access S7 stations.

The addressing mode for accessing SIMATIC S7 (option selected) is set by default.

---

**See also**

[Connection configuration for FETCH/WRITE (S7-300, S7-400)](#connection-configuration-for-fetchwrite-s7-300-s7-400)
  
[Use of FETCH/WRITE (S7-300, S7-400)](#use-of-fetchwrite-s7-300-s7-400)

### ISO-on-TCP OPC properties (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > OPC".

Here, you set connection-specific properties for an ISO-on_TCP connection used by the OPC server.

You can set the following parameters:

#### Timeout for job

If a pending job cannot be processed during the wait time set here, the connection is reset and the job acknowledged with an error.

Range of values: 0 to 99999 ms

- Default setting: 15000 ms

#### Send buffer size

Default size of the default send buffer. Additional send buffers of any length (up to 65535 bytes) may be used at runtime.

Range of values:

- Default setting: 256 bytes

- Range of values: 65535 bytes maximum

#### "Optimization of direct access for tag services" option

If you use this option, the OPC server attempts to combine direct accesses to several tags to minimize the number of jobs that need to be sent.

This option is enabled by default.

#### "Immediate response when interrupted connection is detected" option

If you select this option, you specify that the application is notified that a communication job (FETCH, or WRITE) cannot be executed when a connection is unavailable. The code is sent regardless of whether or not a current attempt to establish the connection succeeds.

If you do not select this option, the application is informed of the nonavailability of a connection only when the connection times out.

The option described here is relevant and available only when the two modes listed below are used:

- The connection is configured as a permanent connection.

  Connections can be configured as permanently established connections (in "Details of connection establishment"). This means that jobs can be forwarded to the partner with the shortest possible reaction time without needing to establish the connection first.

  If there is a disruption on the connection, the system automatically attempts to re-establish the connection. In this situation, there may be delays before a message can be forwarded to the application.
- You are using the FETCH or WRITE job types (can be selected in "Options").

  Only with these job types is an immediate reaction necessary in certain situations if there is no connection.

## TCP connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [TCP - special connection properties (S7-300, S7-400, S7-1500)](#tcp---special-connection-properties-s7-300-s7-400-s7-1500)
- [TCP OPC establishment details (S7-300, S7-400, S7-1500)](#tcp-opc-establishment-details-s7-300-s7-400-s7-1500)
- [TCP address details (S7-300, S7-400, S7-1500)](#tcp-address-details-s7-300-s7-400-s7-1500)
- [TCP options (S7-300, S7-400, S7-1500)](#tcp-options-s7-300-s7-400-s7-1500)
- [TCP OPC properties (S7-300, S7-400, S7-1500)](#tcp-opc-properties-s7-300-s7-400-s7-1500)
- [Port settings (S7-300, S7-400, S7-1500)](#port-settings-s7-300-s7-400-s7-1500)

### TCP - special connection properties (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Special connection properties".

Connection parameters specify additional properties for the local connection endpoint.

#### Establishing an active connection

Use this option to specify whether the connection is established from this device. This is the default option if the address of the partner is specified.

- ON: Connection is established actively.
- OFF: Connection is established by the partner.

If you selected "Unspecified" as the connection partner when you created the connection, the option is deselected by default. If you select the option you must specify the address of the partner in the "Addresses" tab.

> **Note**
>
> **Effect on the mode**
>
> Note the effect on the mode.
>
> - S7-300 / S7-400
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), disable the "Active connection establishment" option.
> - OPC server
>
>   If you want to use FETCH or WRITE mode (see the "Options" parameter group), enable the "Active connection establishment" option.

#### FTP mode (with S7-300 / S7-400 - connection unspecified)

Selecting this option has the following results:

- The TCP connection is now used as an FTP connection.
- Parameter group "Address details": The addresses are specified automatically (port = 21; note: This setting is not visible under "Address details").
- Parameter group "Options": The mode is permanently set to FTP.

The "Active connection establishment" option is irrelevant and is not available.

Requirement: This option can only be selected for certain CPs with S7-300 / S7-400 when using an unspecified TCP connection.

### TCP OPC establishment details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > Establishment details".

#### Options for connection establishment

Entries in this area are possible only if you have selected active connection establishment in "Special connection properties".

Choose from the two following alternatives:

- The connection is established permanently

  The connection is established permanently when you start up the PC station and is re-established following an interruption on the connection.
- The connection is established when it is required (access to tag)

  You can also specify how long the connection should stay up after access.

#### Connection establishment monitoring

- Timeout: Error wait time during the connection establishment

  If, during this wait time, the connection cannot be established, the connection is reset and a pending request acknowledged with an error.

  Range of values: 0 to 99999 ms

  Default: 15000 ms

  > **Note**
  >
  > The connection establishment monitoring that can be set here, has the following relationship with the time monitoring that can be set in the module configuration: The lower value is valid.
  >
  > Time monitoring can be configured in the module configuration in "Properties Ethernet interface".

### TCP address details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Address parameters and connection types

With TCP, the communication partners are addressed through the local and remote endpoint as follows.

- Local addresses: Local IP address and local port
- Remote addresses: Remote IP address and remote port

  ![Sending and receiving over a TCP connection](images/142870034955_DV_resource.Stream@PNG-en-US.png)

  Sending and receiving over a TCP connection

#### Ports

The ports define the access point to the user program within the station/CPU. They must be unique within the station/CPU.

- Specified connection

  In the configuration of the Ethernet CP and the Ethernet target Station, the ports of a TCP connection must be crossed over.

  - Remote port (on the Ethernet CP) = local port (on the target station)
  - Local port (on the Ethernet CP) = remote port (on the target station)
- Unspecified connection

  Some address parameters are not specified. See [Unspecified connections](Connections%20-%20Purpose%20and%20selection.md#unspecified-connections-s7-300-s7-400-s7-1500)

---

**See also**

[Port settings (S7-300, S7-400, S7-1500)](#port-settings-s7-300-s7-400-s7-1500)

### TCP options (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Options".

#### Operating mode

- **SEND/RECV:**

  This is the standard mode with the AG_SEND/AG_LSEND, and AG_RECV/AG_LRECV FCs.
- **FETCH/WRITE:**

  System memory areas in the SIMATIC S7 can be accessed from the following devices if you select one of the operating modes below for the TCP connection:

  - SIMATIC S5
  - SIMATIC PC stations
  - Third-party devices

  The connection can then only be used for this mode. It is then not possible to send or receive using the AG_SEND/AG_LSEND or AG_RECV/AG_LRECV FCs.

  - FETCH

    Selecting this operating mode enables direct read access to data areas in the SIMATIC S7. Access can, for example, be from a SIMATIC S5 station or a third-party station.
  - WRITE

    Selecting this operating mode enables direct write access to data areas in the SIMATIC S7. Access can, for example, be from a SIMATIC S5 station or a third-party station.
- **FTP**

  If you have selected the "Use for FTP protocol" option in "Properties > General > Special connection properties", "FTP" will be displayed here and the TCP connection is then used as an "FTP connection"; no other options can be selected.

  Requirement: The option can only be selected for an unspecified TCP connection.
- **SPEED SEND/RECV**

  Selecting the SPEED SEND/RECV mode allows you to use the AG_SSEND and AG_SRECV instructions.

  The AG_SSEND/AG_SRECV (SPEED SEND/RECEIVE) instructions provide faster and therefore optimized transmission within an S7-400 station. Check the device documentation to see whether this operating mode is supported by the CP you are using.

#### FETCH/WRITE requirements: Mode of connection establishment

Select one of the following options for connection establishment in the "General" tab as suitable for the station type.

- SIMATIC S7 station: PASSIVE connection establishment
- PC station: Active connection establishment

#### "S7 addressing mode" option (for FETCH/WRITE only)

You can select the addressing mode here when you configure for FETCH/WRITE mode.

- S7 addressing mode: Byte address
- S5 addressing mode: Word address

This allows applications to access S5 or S7 stations without modifying the addresses. This is particularly useful for existing S5 applications, for example, that can now be used unchanged when accessing S7 stations.

The addressing mode for accessing SIMATIC S7 (option selected) is set by default.

---

**See also**

[Connection configuration for FETCH/WRITE (S7-300, S7-400)](#connection-configuration-for-fetchwrite-s7-300-s7-400)
  
[Use of FETCH/WRITE (S7-300, S7-400)](#use-of-fetchwrite-s7-300-s7-400)

### TCP OPC properties (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > OPC".

Here, you set connection-specific properties for a TCP connection used by the OPC server.

You can set the following parameters:

#### Job timeout

If a pending job cannot be processed during the wait time set here, the connection is reset and the job acknowledged with an error.

Range of values:

- Default setting: 15000 ms

#### Send buffer size

Default size of the default send buffer. Additional send buffers of any length (up to 65535 bytes) may be used at runtime.

Range of values:

- Default setting: 256 bytes
- Range of values: 65535 bytes maximum

#### Optimization of direct access for tag services

If you use this option, the OPC server attempts to combine direct accesses to several tags to minimize the number of jobs that need to be sent.

This option is enabled by default.

#### Use miniprotocol

With this option, you specify whether or not the data is transferred as individual fields with length information about the field size (2 bytes in the job buffer). The recipient then reads the data out according to the length information. This property must be configured identically for both communications partners.

As default, the option is disabled; the recipient then reads the data out according to the set receive buffer size.

- Receive buffer size

  If you do not use a miniprotocol, you can set the size of the receive buffer here.

  Range of values: 0 to 65535 bytes

  - Default setting: 256 bytes

### Port settings (S7-300, S7-400, S7-1500)

#### Port settings

The ports define the access point to the user program within the station/CPU. They must be unique within the station/CPU. Please see the section below on the features of unspecific connections to redundant partners.

The following table provides information about the value range:

| Port |  | Use/note |
| --- | --- | --- |
| 0 |  | Permanently assigned; must not be used. |
| 1...1023 |  | Assigned by default, should not be used (well-known ports) |
| 1024...49151 <sup>1)</sup> | Ports for application-specific protocols |  |
| **2000...5000** | Area in which a free port is searched for and assigned by the configuration tool.  You can set the ports in this range individually. |  |
| 5001...49151 <sup>1)</sup> | The ports above 5000 are used by the system.  Note: If you want to use these ports, please contact your system administrator to verify availability. |  |
| 49152...65535 |  | Dynamically assigned ports.  The use of these ports is not recommended. |

The following local ports are reserved; you should not use them for any other purpose during connection configuration.

| Port | Protocol | Service |
| --- | --- | --- |
| 20, 21 | TCP | FTP |
| 25 | TCP | SMTP |
| 80 | TCP | HTTP |
| 102 | TCP | RFC1006 |
| 123 | UDP (TCP) | NTP ***** |
| 135 | TCP | RPC-DCOM |
| 161 | UDP | SNMP_REQUEST |
| 34964 | UDP | PN IO |
| 65532 | UDP | NTP |
| 65533 | UDP | NTP |
| 65534 | UDP | NTP |
| 65535 | UDP | NTP |
| ***** For CP 443‑1 and CP 443‑1 Advanced as of firmware version V3, Port 123 is reserved for NTP.   <sup>1)</sup> For S7-1500, as of firmware version V3.0, the highest permissible port number that can be assigned in conjunction with the TCON instruction is 65535. |  |  |

#### Ports for unspecific connections to redundant partners

If you create unspecific connections to a redundant partner, for example from an S7‑400 with CP to a redundant IEC master, you can use the same local port in CP 443‑1 (Advanced) for the two unspecific TCP connections.

## UDP connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [UDP address details (S7-300, S7-400, S7-1500)](#udp-address-details-s7-300-s7-400-s7-1500)
- [UDP with broadcast and multicast (S7-300, S7-400, S7-1500)](#udp-with-broadcast-and-multicast-s7-300-s7-400-s7-1500)
- [Free UDP connection (S7-300, S7-400, S7-1500)](#free-udp-connection-s7-300-s7-400-s7-1500)
- [UDP options (S7-300, S7-400, S7-1500)](#udp-options-s7-300-s7-400-s7-1500)
- [Port settings (S7-300, S7-400, S7-1500)](#port-settings-s7-300-s7-400-s7-1500-1)

### UDP address details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Address parameters and connection types

For UDP the communication partners are addressed through the local and remote endpoint as follows.

- Local addresses:  
  Local IP address and local port
- Remote addresses:  
  Remote IP address and remote port

  > **Note**
  >
  > The term "connection" is also used here for UDP, because during configuration – as for TCP as well – the communication partners are assigned to each other and thus are logically "connected". In actuality, there is no explicit connection setup between communication partners during station operation in UDP.

  ![Sending and receiving over a UDP connection](images/142861536651_DV_resource.Stream@PNG-en-US.png)

  Sending and receiving over a UDP connection

Depending on the desired connection type, the remote address parameters are either specified or left open in the configuration.

- Specified UDP connection

  You have specified the connection of a target station when creating the new connection.
- UDP connection specified as broadcast

  You have specified "Broadcast" as the partner when creating the new connection (requires the connection to be created interactively or initially as an unspecified connection).
- UDP connection specified as multicast

  You have specified "Multicast" as the partner when creating the new connection (requires the connection to be created interactively or initially as an unspecified connection).
- Unspecified UDP connection

  You have selected "Unspecified" as the connection type when creating the connection.

#### Unspecified UDP connection

You can use the unspecified UDP connection in two ways:

- Available UDP connection

  To configure an available UDP connection, select the option "Address assignment in the block" option. In this case, entries can no longer be made in the input fields for the remote IP address and the remote port because the target addresses are now specified by the user program.
- Connection to a "third-party station" in a different project.

  You can specify the remote IP address and the port for any target station. The target station can be inside or outside of the current project.

  > **Note**
  >
  > **Partner addresses must be specified**
  >
  > Since there is no connection setup in UDP (datagram service), communication via the configured UDP connection is only possible if the partner addresses (IP address and port) are also specified.

See [Unspecified connections](Connections%20-%20Purpose%20and%20selection.md#unspecified-connections-s7-300-s7-400-s7-1500)

#### Connection to all broadcast devices

If you select "All broadcast devices" for the connection partner, you are specifying that UDP frames will be sent to all accessible broadcast devices.

In the "Address details" parameter group under the IP address (IP) for the partner, a valid broadcast address in the network is suggested for the partner.

Under "Port", you must enter a port address that is appropriate for all partners to be accessed.

---

**See also**

[Port settings (S7-300, S7-400, S7-1500)](#port-settings-s7-300-s7-400-s7-1500-1)

### UDP with broadcast and multicast (S7-300, S7-400, S7-1500)

#### Application

When selecting the connection partner for UDP connections, you also have the two options:

- Connection to all broadcast devices

  If you select "All broadcast devices" for the partner, you specify are specifying that UDP frames are sent to all accessible broadcast devices.

  > **Note**
  >
  > With broadcast, S7-CPs can only be used to send; an S7-CP does not allow receipt of user data on broadcast connections, (see below).
- Connection to all multicast devices

  If you select "All multicast devices" for the partner, you are specifying that UDP frames are sent to all accessible broadcast devices.

  Multicast and broadcast are special connection options that are supported by Industrial Ethernet CPs on UDP connections and can be configured.

  As of TIA Portal V14, the S7-1500 CPUs with firmware version V2.0.1 and higher support UDP multicast via the integrated CPU ports as well.

  > **Note**
  >
  > **Maximum number of UDP multicast connections**
  >
  > The maximum number of possible UDP multicast connections varies depending on the device and the interface used. For the maximum number of supported UDP multicast connections, please refer to the manuals that apply to the respective devices.

The frames are sent without acknowledgement because the UDP protocol does not provide for any acknowledgements. This is intended to prevent a data flood of acknowledgements. For example, if frames are sent to 100 partners, then 100 acknowledgements (1 per partner) would arrive at the same time. Such a flood of data could not be analyzed by the sender module.

See also [Creating UDP / FDL connections with broadcast / multicast](Configuring%20connections.md#creating-udp-fdl-connections-with-broadcast-multicast)

#### When do I use multicast instead of broadcast?

To enable simultaneous sending of a frame to a number of partners, the connection option "Multicast for UDP connections" was introduced.

As opposed to the broadcast connection option, this connection type can also receive frames that are sent to multiple devices in the multicast group.

By specifying a specific receiver group (multicast group), you can prevent extra load on recipients for which the data is not intended. For this reason, multicast is always a better solution than broadcast if frames are sent to groups of partner stations.

#### Why does an S7-CP not allow user data to be received on broadcast connections?

S7-CPs do not receive any broadcast frames for user data transfer. Only usable frames, such as an ARP request, are forwarded beyond the LAN controller and evaluated. However, S7 CPs can send broadcast frames to the network.

Reason:

Often there is a requirement to send frames to a number of partner devices from one device. In this regard, the important thing is that the frames are sent at the same time and arrive at the partner devices at virtually the same time. Consequently, sending and receiving of broadcast frames is always required. With a broadcast message, the frame is also actually received by all devices in the network.

A typical application is a situation where broadcast frames are required to find a MAC address for an IP address (ARP request).

Therefore a communication module must always pick up broadcast frames and analyze them from the software side. A significant disadvantage in this regard is that if there are too many broadcast frames on the network, performance drops significantly. This is due to the fact each individual module must process all broadcast frames in order to determine whether the frame was destined for it.

To avoid the disadvantages cited above, the S7-CPs behave as follows relative to broadcast:

- After receipt, the broadcast frames are filtered out with high priority for all Ethernet CPs. In other words, all unusable frames are discarded immediately. Only usable frames, such as an ARP request, are forwarded beyond the LAN controller and evaluated. This prevents the possible negative influence of broadcast frames on the other connections.

#### Parameter group "Address details" - Connection to all multicast devices

By selecting the "All multicast nodes" for the connection partner, you are specifying the following:

- Sent UDP frames are delivered to all accessible multicast devices of the multicast group.
- The local device for multicast frames is ready to receive in the specified multicast group.

The multicast group is specified via the IP address and the port number.

Under IP address (IP) for the partner, an valid IP address in the network is suggested for the multicast group. With multicast, the partner is always a group of recipients (multicast group).

Enter a port number under "Port" for all partners that you want to access. It must apply to all of these partners.

In principle, it is possible to address multiple multicast groups under one IP address. To do this you can create multiple UDP connections with the same IP address but different PORT addresses.

> **Note**
>
> You should assign identical port numbers for the local port and for the partner port within a multicast group. This is the only way that frames can be both sent and received by the CP within the one multicast group!
>
> Note the following example for three devices in the multicast group:

![Sending and receiving in a multicast group via identical port numbers](images/142903865867_DV_resource.Stream@PNG-en-US.png)

Sending and receiving in a multicast group via identical port numbers

#### IP addresses for IP multicast

- Value range

  For IP multicast, the IP addresses from 224.0.0.0 to 239.255.255.255 can be used.

  Because the IP addresses up to 224.0.0.255 are reserved for special purposes, we recommend using the IP addresses starting from 224.0.1.0 (default setting) for IP multicast.
- Identification of the multicast group

  A multicast group is not identified via the entire IP address; rather, the first address byte and the most significant bit of the second address byte are ignored. This is an important feature, because it means that apparently different IP addresses can address the same multicast group.

  Example:

  The following IP addresses each address the same multicast group.

  ![IP addresses for IP multicast](images/142903759371_DV_resource.Stream@PNG-en-US.png)

### Free UDP connection (S7-300, S7-400, S7-1500)

#### Program-controlled addressing

A free UDP connection enables program-controlled addressing of the communication peer. Communication between two devices in Industrial Ethernet has the following characteristics:

- Data transfer is bidirectional, i.e. you can send and receive simultaneously on the UDP connection.
- The local station is specified by configuration. The remote device is entered by the user program in the request header of the request buffer with the AG_SEND call. Thus, any device can be accessed on the Ethernet/LAN/WAN.
- The sender's IP address and port can be read from the request header of the AG_RECV.

  ![Sending and receiving via an unspecified UDP connection - Addressing via program](images/142903755275_DV_resource.Stream@PNG-en-US.png)

  Sending and receiving via an unspecified UDP connection - Addressing via program

#### Data volumes and configuration limit

See the manual provided with the Ethernet CP for the number of UDP connections that the respective Ethernet CP can support. The number of connections per station can be increased by accepting additional CPs .

Each job buffer can transfer up to 2042 bytes of user data. The job header reserves an additional 6 bytes.

### UDP options (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Options".

#### Operating mode

- **SEND/RECV:**

  This is the standard mode with the AG_SEND/AG_LSEND, and AG_RECV/AG_LRECV FCs.
- **SPEED SEND/RECV**

  Selecting the SPEED SEND/RECV mode allows you to use the AG_SSEND and AG_SRECV instructions.

  The AG_SSEND/AG_SRECV (SPEED SEND/RECEIVE) instructions provide faster and therefore optimized transmission within an S7-400 station. Check the device documentation to see whether this operating mode is supported by the CP you are using.

### Port settings (S7-300, S7-400, S7-1500)

#### Port settings

The ports define the access point to the user program within the station/CPU. They must be unique within the station/CPU. Please see the section below on the features of unspecific connections to redundant partners.

The following table provides information about the value range:

| Port |  | Use/note |
| --- | --- | --- |
| 0 |  | Permanently assigned; must not be used. |
| 1...1023 |  | Assigned by default, should not be used (well-known ports) |
| 1024...49151 <sup>1)</sup> | Ports for application-specific protocols |  |
| **2000...5000** | Area in which a free port is searched for and assigned by the configuration tool.  You can set the ports in this range individually. |  |
| 5001...49151 <sup>1)</sup> | The ports above 5000 are used by the system.  Note: If you want to use these ports, please contact your system administrator to verify availability. |  |
| 49152...65535 |  | Dynamically assigned ports.  The use of these ports is not recommended. |

The following local ports are reserved; you should not use them for any other purpose during connection configuration.

| Port | Protocol | Service |
| --- | --- | --- |
| 20, 21 | TCP | FTP |
| 25 | TCP | SMTP |
| 80 | TCP | HTTP |
| 102 | TCP | RFC1006 |
| 123 | UDP (TCP) | NTP ***** |
| 135 | TCP | RPC-DCOM |
| 161 | UDP | SNMP_REQUEST |
| 34964 | UDP | PN IO |
| 65532 | UDP | NTP |
| 65533 | UDP | NTP |
| 65534 | UDP | NTP |
| 65535 | UDP | NTP |
| ***** For CP 443‑1 and CP 443‑1 Advanced as of firmware version V3, Port 123 is reserved for NTP.   <sup>1)</sup> For S7-1500, as of firmware version V3.0, the highest permissible port number that can be assigned in conjunction with the TCON instruction is 65535. |  |  |

#### Ports for unspecific connections to redundant partners

If you create unspecific connections to a redundant partner, for example from an S7‑400 with CP to a redundant IEC master, you can use the same local port in CP 443‑1 (Advanced) for the two unspecific TCP connections.

## FETCH/WRITE mode (S7-300, S7-400)

This section contains information on the following topics:

- [Use of FETCH/WRITE (S7-300, S7-400)](#use-of-fetchwrite-s7-300-s7-400)
- [Connection configuration for FETCH/WRITE (S7-300, S7-400)](#connection-configuration-for-fetchwrite-s7-300-s7-400)

### Use of FETCH/WRITE (S7-300, S7-400)

#### FETCH/WRITE

You can use the FETCH/WRITE services to access system memory areas of the S7 CPU.

- FETCH: Read data directly
- WRITE: Write data directly

Access is possible from the following devices:

- SIMATIC S5
- SIMATIC PC stations
- Non-SIMATIC devices

#### Connection types

The FETCH/WRITE services can be configured and used in SIMATIC S7 with the following connection types:

- ISO transport connections
- ISO-on-TCP connections
- TCP connections

#### System memory

You can use FETCH or WRITE to access the following operand ranges in the SIMATIC S7 system memory:

- Data blocks (DB)

  (Note the following limit for DB access: the highest DB no. is 255)
- Bit memory (M)
- Process image input (PII)
- Process image output (PIQ)
- I/O area inputs (PIW, PID, PIB)
- I/O area outputs (PQW, PQD, PQB)
- Counters (C)
- Timers (T)

#### Link to non-SIMATIC systems

In principle, FETCH and WRITE can be used to access S7 system memory areas from any non-SIEMENS device.

To implement this access for PC applications, for example, you must become acquainted with the PDU structure for the jobs. Refer to the device documentation for this purpose.

#### Alarms in the diagnostic buffer

FETCH/WRITE access may give rise to negative acknowledgements from the S7 CPU and corresponding connection-specific entries in the diagnostic buffer.

Alarm coding in the diagnostic buffer at FETCH/WRITE

| Coding | Meaning |
| --- | --- |
| 01<sub>H</sub> | Hardware error |
| 03<sub>H</sub> | Object access is not allowed. |
| 05<sub>H</sub> | Invalid address (syntax ID, range, type, bit number) |
| 06<sub>H</sub> | Data type is not supported. |
| 07<sub>H</sub> | Data type is inconsistent. |
| 0A<sub>H</sub> | The object does not exist, or the range limit was exceeded. |
| FF<sub>H</sub> | Internal protocol error |

#### Additional information

The PDU structure needed to access non-SIMATIC systems is described in the documentation for S7 CPs.

### Connection configuration for FETCH/WRITE (S7-300, S7-400)

#### Configuring the operating mode to suit the type of device

The following operating modes can be configured for the communication endpoint, according to the type of station:

- SIMATIC S7 station: FETCH PASSIVE/WRITE PASSIVE

  If you select either FETCH PASSIVE or WRITE PASSIVE mode for the connection, the system memory areas in SIMATIC S7 can be accessed directly from a SIMATIC S5 station or a non-SIMATIC station (unspecified connection).

  The connection can then only be used for this mode. It is then not possible to send or receive using the AG_SEND/AG_LSEND or AG_RECV/AG_LRECV FCs.

  The connection is established passively, which means that only the partner station (SIMATIC S5 station, a PC station, or a non-SIMATIC station) can establish the connection. You make the necessary settings under "Properties > Options". Once you have selected the operating mode, you will not be able to change the connection setup type.
- SIMATIC PC station: FETCH ACTIVE/WRITE ACTIVE

  If you select either FETCH ACTIVE or WRITE ACTIVE mode, the system memory areas in the SIMATIC S7 or SIMATIC S5 station can be accessed directly from the PC station.

  The connection is established actively, which means that the partner station must await the connection to be established (passive connection setup for the partner). You make the necessary settings under "Properties > Options". Once you have selected the operating mode, you will not be able to change the connection setup type.

#### "S7 addressing mode" option

You can select the addressing mode when you configure FETCH ACTIVE/WRITE ACTIVE mode. This defines how the address information in the FETCH/WRITE call in the SIMATIC S7 station will be interpreted when DBs are accessed:

- S7 addressing mode: Byte address
- S5 addressing mode: Word address

This allows applications to access S5 or S7 stations without modifying the addresses. This is particularly useful for existing S5 applications, for example, that can now be used unchanged when accessing S7 stations.

The addressing mode for accessing SIMATIC S7 (option selected) is set by default.

## FDL connection (S7-300, S7-400)

This section contains information on the following topics:

- [FDL connections - overview (S7-300, S7-400)](#fdl-connections---overview-s7-300-s7-400)
- [FDL address details (S7-300, S7-400)](#fdl-address-details-s7-300-s7-400)
- [FDL options (S7-300, S7-400)](#fdl-options-s7-300-s7-400)
- [FDL OPC properties](#fdl-opc-properties)
- [FDL unspecified FDL connection (free layer 2 access) (S7-300, S7-400)](#fdl-unspecified-fdl-connection-free-layer-2-access-s7-300-s7-400)
- [FDL connection with broadcast (S7-300, S7-400)](#fdl-connection-with-broadcast-s7-300-s7-400)
- [FDL connection with multicast (S7-300, S7-400)](#fdl-connection-with-multicast-s7-300-s7-400)
- [Setting up communication over FDL (S7-300, S7-400)](#setting-up-communication-over-fdl-s7-300-s7-400)

### FDL connections - overview (S7-300, S7-400)

#### Area of application

Data transmission over configured FDL connection is suitable for transmission of contiguous data blocks between two or more PROFIBUS stations.

There is a distinction between

- Specified FDL connection

  The communication stations are uniquely specified by the connection configuration.

  The connection partner can be inside or outside of the STEP7 project.
- Unspecified FDL connection (free layer 2 access)

  The address of the connection partner remains open in the configuration. The communication stations are determined by address information in the communication job of the user program. This means up to 126 stations can be reached via one configured unspecified FDL connection, if these stations support FDL connections.

  The connection partner can be inside or outside of the project.
- FDL connection with broadcast

  All stations ready to receive broadcasts on the PROFIBUS are reached.
- FDL connection with multicast

  All stations belonging to the multicast group on the PROFIBUS are reached.

> **Note**
>
> **Configuration prerequisite**
>
> If FDL connections will be used, the CP mode of the PROFIBUS CP **should not be set** to **DP slave passive**.

> **Note**
>
> **Priority of the telegrams**
>
> Note that the PROFIBUS-CPs for SIMATIC S7 send the telegrams in "LOW" priority.
>
> Partner stations (SIMATIC S5, S7, or third-party stations) must also use "LOW" priority, otherwise a connection willl not be established.

### FDL address details (S7-300, S7-400)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Address parameters for FDL connections

An FDL connection is specified by the local and remote connection endpoint. This includes:

- PROFIBUS address of the node that is to be reached.
- Local LSAP (Link Service Access Point):   
  The local LSAP controls the readiness to receive of the PROFIBUS-CP. The receive resources for data receive in the PROFIBUS-CP are provided on the FDL connection for the LSAP.
- Remote LSAP (Link Service Access Point):   
  The remote LSAP controls the send mode of the PROFIBUS-CP. The PROFIBUS-CP sends to the nodes on the FDL connection via the LSAP. The target node must be ready to receive for this SAP.

#### Specified FDL connection

The relevant local and remote address information is displayed as recommended values for a specified FDL connection. You have the option to set the LSAP addresses individually, if necessary.

#### Unspecified FDL connection

You can use the unspecified FDL connection in two ways:

- Connection to a "third-party station" in a different project.

  You can specify the remote PROFIBUS address and the LSAP for any target station. The target station can be inside or outside of the current STEP 7 project.

  If the remote address is unspecified, then communication via the FDL connection is not possible.
- Free layer-2 access

  Click the relevant check box to configure a free layer 2 access. The input fields for the remote PROFIBUS address and the remote LSAP can no longer be specified in this case because the target addresses are now specified by the user program.

#### FDL connection with broadcast

The remote address parameters for FDL connection with broadcast are permanently set. All broadcast nodes can be reached via the PROFIBUS address 127. Receive data is received via LSAP 63 from all broadcast nodes.

The local address parameters are entered in the job header of the message for sending and delivered to the recipient. The user program for the remote partner can thus determine the sender of the broadcast frame.

> **Note**
>
> **CP receives only on a broadcast connection**
>
> If you use an FDL connection with broadcast, you cannot use any other broadcast connection on the CP.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **"Activate cyclic distribution of bus parameters" function**  If you select this option for the subnet in "General > Bus parameters", the bus parameters will be sent cyclically during operation as broadcast frames. To avoid frame handling conflicts in the user program that receives broadcast frames, you should take the following action:  - ignore all frames that are sent with an LSAP >56    **or** - disable the option under "General > Bus parameters". |  |

#### FDL connection with multicast

The remote address parameters for FDL connection with multicast are permanently set. All multicast nodes can be reached via the PROFIBUS address 127. Sending and receiving data is handled by all nodes in the multicast group via the same LSAP (range 1 to 56). This means the value of the LSAP can only be selected locally and is automatically transferred to the remote LSAP.

The local address parameters are entered in the job header of the message for sending and delivered to the recipient. The user program for the remote partner can use this information to determine the sender of the multicast frame.

### FDL options (S7-300, S7-400)

#### Relevance

Connection configuration in the parameter group "Properties > General > Options".

#### Operating mode

- SEND/RECV:

  This is the standard mode with the AG_SEND/AG_LSEND, and AG_RECV/AG_LRECV FCs. This mode is the default on FDL connections and this cannot be modified.

### FDL OPC properties

#### Relevance

Connection configuration for OPC in the parameter group "Properties > General > OPC".

Here, you set connection-specific properties for an FDL connection used by the OPC server.

You can set the following parameters:

#### Timeout

If a pending job cannot be processed during this wait time, the connection is reset and the job acknowledged with an error.

#### Max number of send retries

Here, specify how many retries there will be for a job if, for example, the connection partner cannot be reached due to a temporary lack of resources.

#### Send buffer size

The size of the default send buffer is set here.

This setting applies to both acknowledged and unacknowledged sending.

Additional send buffers of any length (maximum 244 or 246 bytes) can be used at runtime.

Default setting:

244 bytes or 246 bytes (with default SAPs, if the default SAP 255 is set for both the local and remote SAP)

#### Maximum number of parallel send jobs

Maximum number of simultaneous send jobs on the connection configured here.

#### Number of resources for received jobs

Specify how many receive jobs the OPC server will be able to receive simultaneously on the FDL connection configured here.

Select a value suitable for the expected amount of traffic; in other words,

- For a low total number of connections: Select a higher value to achieve a fast reaction time.
- For a high total number of connections: Select a lower value to avoid resource conflicts.

  - Default setting: 3

#### Send with higher priority

Specify whether the FDL frames on the connection configured here are sent via the LAN with priority (option enabled).

### FDL unspecified FDL connection (free layer 2 access) (S7-300, S7-400)

#### Properties

An unspecified FDL connection with open layer 2 access enables program-controlled addressing of the communication partner and communication between two stations on PROFIBUS with the following properties:

- Data transfer is bidirectional, which means you can send and receive data simultaneously on the FDL connection.
- The local station is specified by configuration. The remote node is entered by the user program in the job header of the job buffer with the AG_SEND instruction call. This means that each node on PROFIBUS (PROFIBUS addresses from 0 to 126) can be reached.
- The PB address, the LSAP, and the sender service can be read from the job header of the AG_RECV.

The figure below illustrates program-controlled addressing in the job buffer:

![Properties](images/23819013387_DV_resource.Stream@PNG-en-US.png)

#### Data volume and configuration limits

Each job buffer can transfer up to 236 bytes of user data. The job header reserves an additional 4 bytes.

### FDL connection with broadcast (S7-300, S7-400)

#### Properties

A broadcast connection sends a message to multiple recipients with **one** job. This means messages can be received on the same broadcast connection that are simultaneously received by other stations on the PROFIBUS.

The properties can be summarized as follows:

- Data transfer is bidirectional, which means you can send and receive data simultaneously on the broadcast connection.
- Sending and receiving takes place via the FDL service SDN (Send Data with No Acknowledge).
- The AG_SEND call needs a job buffer for sending. The job header of this buffer must be reserved.
- The PB address, the LSAP, and service of the broadcast sender can be read from the job header of the AG_RECV.
- The LSAP range from 1 to 56 is reserved for sending. LSAP 63 is reserved for all broadcast stations for receiving.

The figure below illustrates sending and receiving via an FDL connection with program-controlled broadcast addressing:

![Properties](images/23819060235_DV_resource.Stream@PNG-en-US.png)

#### Configuring an FDL connection with broadcast

When creating the FDL connection select "All broadcast stations" as connection partner/station.

#### See also

[Creating UDP / FDL connections with broadcast / multicast](Configuring%20connections.md#creating-udp-fdl-connections-with-broadcast-multicast)

#### Data volume and configuration limits

PROFIBUS-CP only supports **one** broadcast connection.

Each job buffer can transfer up to 236 bytes of user data. The job header reserves an additional 4 bytes.

> **Note**
>
> **CP receives only on a broadcast connection**
>
> If you use an FDL connection with broadcast, you cannot receive any additional broadcast connection messages on the respective CP, neither on any FMS connection with broadcast.   
> Reason:   
> The receive LSAP for broadcast (63) is reserved with a broadcast connection.

### FDL connection with multicast (S7-300, S7-400)

#### Properties

An FDL connection with multicast sends a message to multiple recipients of a multicast group with one job.

The properties can be summarized as follows:

- Data transfer is bidirectional, which means you can send and receive data simultaneously on the FDL connection with multicast.
- Sending and receiving takes place via the FDL service SDN (Send Data with No Acknowledge).
- The system sends via an LSAP (range from 1 to 56) that is uniform for the multicast group.
- The AG_SEND call needs a job buffer for sending. The job header of this buffer must be reserved.
- The PB address, the LSAP, and service of the multicast sender can be read from the job header of the AG_RECV.

The picture below illustrates sending and receiving via an FDL connection with program-controlled multicast addressing:

![Properties](images/23819094283_DV_resource.Stream@PNG-en-US.png)

#### Configuring an FDL connection with multicast

When creating the FDL connection select "All multicast nodes" as connection partner/station.

#### See also

[Creating UDP / FDL connections with broadcast / multicast](Configuring%20connections.md#creating-udp-fdl-connections-with-broadcast-multicast)

#### Data volume and configuration limits

See the device documentation for PROFIBUS-CP for the number of FDL connections that the respective PROFIBUS-CP supports. The number of connections per station can be increased by accepting additional CPs .

Each job buffer can transfer up to 236 bytes of user data. The job header reserves an additional 4 bytes.

### Setting up communication over FDL (S7-300, S7-400)

#### Requirement

- Configuration software: STEP 7 Professional V14
- End point of the connection: CPU S7-1500 firmware version V2.0 or higher with communication module CM 1542‑5 with firmware version V2.0

#### Setting up a configured FDL connection

Proceed as follows to set up a configured FDL connection in STEP 7:

1. Create a TSEND_C instruction in the program editor.
2. Select the TSEND_C instruction and go to "Properties" > "General" > "Connection parameters" in the Inspector window.
3. Under End point, select the partner end point. Use one of the two partner end points below:

   - CPU S7‑1500 with CM 1542‑5
   - Unspecified
4. Select "Use configured connection" under Configuration type.
5. Select "FDL" under Connection type.
6. Select the following interfaces under Interfaces:

   - Local: PROFIBUS interface of CM 1542‑5
   - Specified partner: PROFIBUS interface of CM 1542‑5
7. Select the setting <new> under Connection data.

The figure below shows a fully configured FDL connection in STEP 7.

![Configuring the FDL connection](images/91821287307_DV_resource.Stream@PNG-en-US.png)

Configuring the FDL connection

#### Setting up an FDL connection in the user program

For communication via FDL, you need to create the data block of the TCON_FDL system data type yourself in each case, assign parameters and call it directly at the instruction. Follow these steps:

1. Create a global data block in the project tree.
2. In the global data block, define a tag of the data type TCON_FDL.

   The example below shows the global data block "FDL_connection" in which the tag "FDL_connection" of the data type TCON_FDL is defined.

   ![Programming an FDL connection](images/91821291019_DV_resource.Stream@PNG-en-US.png)

   Programming an FDL connection
3. Program the parameters of the FDL connection (e.g. the PROFIBUS addresses) in the tag of the data type TCON_FDL.
4. Create a TCON instruction in the program editor.
5. Interconnect the CONNECT parameter of the TCON instruction with the tag of the data type TCON_FDL.

   In the example below, the CONNECT parameter of the TCON instruction is interconnected with the tag "FDL_Connection" (data type TCON_FDL).

   ![Example: TCON instruction for FDL connection](images/91821294731_DV_resource.Stream@PNG-de-DE.png)

   Example: TCON instruction for FDL connection

## E-mail connection (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Setting up an email connection (S7-300, S7-400, S7-1500)](#setting-up-an-email-connection-s7-300-s7-400-s7-1500)
- [E-mail address details (S7-300, S7-400, S7-1500)](#e-mail-address-details-s7-300-s7-400-s7-1500)
- [Sending email (S7-300, S7-400, S7-1500)](#sending-email-s7-300-s7-400-s7-1500)

### Setting up an email connection (S7-300, S7-400, S7-1500)

Emails can be sent from the automation system, but they cannot be received.

To send email in the user program of the S7-CPU, use the send call of the SEND/RECEIVE interface (FC AG_SEND / AG_LSEND).

#### Configuration overview

Set up exactly one e-mail connection per CP for sending e-mails. This e-mail connection specifies the mail server that delivers all e-mails sent by the CP.

An email connection can be set up as follows:

- Connection configuration (standard application)  
  This application is described below.
- User program with FB CP_CONFIG and configuration data block  
  There are application ranges for which it is sensible to set up the communication connections with a program-controlled procedure via specific applications rather than via the configuration interface.

#### Procedure - example of graphic configuration

Configuration of an email connection is described below. The procedure is basically the same as when setting up an unspecified connection: [Creating an unspecified connection](Configuring%20connections.md#creating-an-unspecified-connection).

Select the connection type, email connection, in the drop-down list box.

This step activates the connection mode: The CPUs available for the selected connection type are selected and highlighted.

1. Click on the CPU from which a connection will be set up.
2. Move the cursor within the CPU and confirm the connection endpoint with another click of the mouse.  
   An unspecified connection will be created.
3. In "Properties > Address details" in the Inspector window, enter the address parameters according to the information in the address details:

   [E-mail address details](#e-mail-address-details-s7-300-s7-400-s7-1500)

After downloading the configuration data the user program can send e-mails over this e-mail connection.

#### Using an OPC server as an SMTP server

Instead of an unspecified connection, you can select an OPC server as an SMTP server as the connection partner. This means that the IP address of the SMTP interface of the PC station it is entered in the partner's address details.

> **Note**
>
> **The PC interface must support the SMTP protocol**
>
> The e-mail connection via the OPC server is only created consistently when an interface with SMTP protocol support is enabled on the PC station. Read the documentation of the module your using.

---

**See also**

[DNS configuration](Communications%20modules%20and%20network%20components.md#dns-configuration)

### E-mail address details (S7-300, S7-400, S7-1500)

#### Relevance

Connection configuration in the parameter group "Properties > General > Address details".

#### Parameter

Enter the parameters required for the delivery of the e-mail. You can set the following parameters:

|  |  |  |
| --- | --- | --- |
| **Parameters** | **Description** | **Example** |
| E-mail server (SMTP) | Address of the mail server via which the e-mails are sent.   The IP address can be specified absolutely or symbolically.   The following applies to symbolic names:   A valid name has 1 to 64 characters of which at least one character must be a letter.  If one or more "." characters are used, the following constraint also applies: A valid name has 1 to 3 characters behind the last "."; at least one of these characters must be a letter.  A symbolic name can only be used if the Internet CP knows the address of the Domain Name System (DNS). Make an appropriate entry when configuring the Internet CP in the DNS configuration.  A maximum of 64 characters can be entered. | absolute: 140.80.0.4  symbolic name: t-online.de |
| Default sender name | Specification of an address that is always inserted in the email as sender address, if the sender specification (FROM parameter) is empty in the header of the email.  This information is normally irrelevant for delivery of the mail. It is simply information for the mail recipient. Since some mail servers do not forward jobs if there is no sender information, it is advisable to enter information here!  A maximum of 126 characters can be entered.   **Note:**  Remember that a default sender name must be specified if you want a test mail to be initiated by special diagnostics. | Station2.CPU412@xy.factory2.de |

---

**See also**

[DNS configuration](Communications%20modules%20and%20network%20components.md#dns-configuration)

### Sending email (S7-300, S7-400, S7-1500)

#### Requirement

You can send email if the email connection has been set up via the connection configuration. You must use the specified ID to call the FC AG_SEND/AG_LSEND for the connection configuration.

#### Procedure

Proceed as follows to send an e-mail:

1. Make the e-mail data available in a data block.
2. Use the AG_SEND or AG_LSEND instruction in the user program.

#### Data block

The entire email, meaning the address information and the message itself, will be set up in any data block. The example in STL notation below shows the appropriate information for the required DB structure.

Use the programming editor to create and enter the DB data.

The following table contains information about email data blocks in STL notation:

| Address | Name | Type | Start value | Comment | Entry |
| --- | --- | --- | --- | --- | --- |
| 0.0 | - | STRUCT | - | - | - |
| +0.0 | TO<sup>1)</sup> | STRING[40] | "TO:name.name@t-online.de;" | Recipient | Mandatory |
| +42.0 | CC<sup>1)</sup> | STRING[40] | "CC:name.name@t-online.de;" | CC recipient | Optional |
| +84.0 | FROM | STRING[40] | "FROM:plant.werk2@xyz-online.de;" | Sender | Optional |
| +126.0 | SUB | STRING[40] | 'SUB:Status Station 7;' | Subject | Optional |
| +168.0 | Text | STRING[100] | 'TXT:Fault in plant section 2;' | Mail text | Mandatory |
| +270.0 | Attachment | STRING[4] | 'BNY:**'** | Here the attachment is initiated<sup>3)</sup> | Optional |
| +276.0 | Value1 | BYTE | **B#16#27** <sup>2)</sup> | Attachment/binary value<sup>3)</sup> | Optional |
| +277.0 | Value2 | BYTE | **B#16#03** <sup>2)</sup> | Attachment/binary value<sup>3)</sup> | Optional |
| =278.0 | - | END_STRUCT | - | - | - |
| 1) Multiple recipients can be specified. The information must then be separated by a comma.  2) The information in bold will be delivered to the recipient as attachment  3) Data can also be supplied dynamically. |  |  |  |  |  |

#### Comments on the table

- Structure and syntax of the data in the email DB

  The structure suggested here with multiple STRINGs is one of several variants. Crucial are the entries in the column "Initial value" with the IDs contained therein (TO:, SUB:, CC:, FROM:, TXT:, BNY:), which must be used in the DB in precisely this notation to identify the mail content. All entries must end with a semicolon; only the last entry does not need a semicolon.

  The string length is only shown in the table as an example; it can be customized to the actual character count (exception: The string length for identifying the attachment must be specified with [4]).

  For example, another variant would be using only one STRING in total, and assigning the entire text to this string with the identifiers.
- If you encounter a problem entering the "@" symbol, try the input ALT+64 instead.
- Attachments

  The user data entered in the email DB can also be delivered to the recipient entirely or partially as attachment. For this the sender must give the data the identifier "BNY:"

  The data specified after this identifier will then be delivered to the recipient as attachment.

  In the table the attachment is 2 bytes; this is only an example however. You can enter attachments that are as complex as you like.
- Data length

  The data length specified in the call AG_SEND/AG_LSEND must at least include the length of the data in the DB; note the specifications in the address column of the programming editor (Note: The specification corresponds to the number of bytes).

#### Sending an email with AG_SEND/AG_LSEND <sup>1)</sup>

Use the FC AG_SEND instruction to send an e-mail or with data lengths >240 bytes, use AG_LSEND. A detailed description of call parameters is available in the online help for the instructions.

See also [AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet)](SIMATIC%20NET%20CPs%20%28S7-300%2C%20S7-400%29.md#ag_send-ag_lsend-ag_ssend-ind-ethernet-s7-300-s7-400)

Example:

| **STL** | **Explanation** |
| --- | --- |
| call fc 50 | //AG_LSEND block call |
| ACT := M 10.0 | //Bit for job trigger |
| ID := MW 12 | //Connection ID (connection configuration) |
| LADDR := W#16#0100 | //Module address 256Dec. in hardware configuration |
| SEND := P#db99.dbx10.0 byte 278, | //Address of the data block; DB length |
| LEN := MW 14 | //Length of the data range to be sent |
| DONE := M 10.6 | //Address for return parameter DONE |
| ERROR := M 10.7 | //Address for return parameter ERROR |
| STATUS := MW 16 | //Address for return parameter STATUS |

## Point-to-point link (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Point-to-point communication (S7-300, S7-400, S7-1500)](#point-to-point-communication-s7-300-s7-400-s7-1500)
- [Assigning parameters for a point-to-point link (S7-300, S7-400, S7-1500)](#assigning-parameters-for-a-point-to-point-link-s7-300-s7-400-s7-1500)
- [PtP communication direction (S7-300, S7-400, S7-1500)](#ptp-communication-direction-s7-300-s7-400-s7-1500)
- [PtP link path (S7-300, S7-400, S7-1500)](#ptp-link-path-s7-300-s7-400-s7-1500)
- [PtP - special connection properties (S7-300, S7-400, S7-1500)](#ptp---special-connection-properties-s7-300-s7-400-s7-1500)

### Point-to-point communication (S7-300, S7-400, S7-1500)

#### Types of communication over PtP links

When communicating over a PtP connection, two different types of communication are distinguished:

- Homogeneous communication
- Heterogeneous communication

Support of PtP communication means that external devices such as printers can be accessed.

#### Homogeneous PtP communication

The PtP CP forwards data between modules that support the S7 protocol. Users have the full range of communications functions available if these are provided by the end devices connected via PtP (for example CPU with CPU or PG with CPU).

On these connections, the PtP CPs are not the endpoint of the connection but take over the role of a router.

With a homogeneous link, all the communications functions defined in S7 can be used if they are supported by both connection partners. Protocol handling for specific communication instruction calls is therefore not necessary on the CP.

#### Heterogeneous PtP communication

The PtP CP operates like a gateway using other protocols such as RK512, 3964, open drivers and special protocols. Selected blocks serve as a user interface synchronized with the user program. At the receiving end, the user program acting as server can be accessed via the heterogeneous PtP link once again using communications functions synchronized with the program.

From a communications engineering perspective, the PtP CP is the endpoint of the S7 connection in heterogeneous communication. Communication between a CPU and CP is therefore based on S7 protocol elements. The CP handles the conversion of these protocol elements to the PtP protocol and vice versa.

For heterogeneous communication, the following communication instructions can be used on the CPU:

- BSEND
- BRCV
- PUT
- GET

On the PtP CP, the suitable S7 protocol elements must be implemented for the BSEND, BRCV, PUT and GET instructions as client (CP is active) and PUT and GET instructions as server (CP is passive).

| Instructions | Client | Server |
| --- | --- | --- |
| [BSEND](S7%20communication%20%28S7-300%2C%20S7-400%29.md#bsend-send-data-in-segments-s7-300-s7-400) | Yes | no |
| [BRCV](S7%20communication%20%28S7-300%2C%20S7-400%29.md#brcv-receive-data-in-segments-s7-300-s7-400) | Yes | no |
| [PUT](S7%20communication%20%28S7-300%2C%20S7-400%29.md#put-write-data-to-a-remote-cpu-s7-300-s7-400) | Yes | Yes |
| [GET](S7%20communication%20%28S7-300%2C%20S7-400%29.md#get-read-data-from-a-remote-cpu-s7-300-s7-400) | Yes | Yes |

#### Communications functions

Heterogeneous communication can have two different qualities depending on the application:

- Controlled communications functions:

  With controlled communications functions, it is possible to control the transfer. This means that the transfer can not only be started at the active end but can be enabled at the passive end by the control and the end of the transfer can be detected.

  This functionality is implemented for the communications instructions in S7 with the parameters "EN_R" (ready to receive) and "NDR" (receipt of data complete).
- Non-controlled communications functions:

  With non-controlled communications functions, the transfer is handled by the active partner without the passive partner being able to take any action.

### Assigning parameters for a point-to-point link (S7-300, S7-400, S7-1500)

#### Hardware for configuring PtP

To establish a PtP connection, you require a CP 441. Communications modules of the type CP 441 have slots allowing the use of one (CP 441-1) or two (CP 441-2) PtP interface modules.

You will find PtP interface modules of the type IF963 in the hardware catalog of the SIMATIC S7-400 under the communications modules for PtP. The IF963 modules are available for the following interface types:

- RS-232C
- TTY
- RS-422/485

Depending on the interface type, the IF963 modules support at most the following communications protocols:

- ASCII
- 3964(R)
- RK512
- Printers
- Modbus master
- Modbus slave

If you use a PtP interface in a CP 441, a PtP subnet is automatically displayed and an unspecified PtP connection is added.

Once you have selected the CP 441 or selected the required interface directly, you can select and configure the protocol in the Inspector window.

#### PtP connection to an S7 device as the connection partner

You can enter a maximum of 8 connections in the connection table for the local partner. For the connection partner, you enter only **one** connection in the connection table. The connection partner can receive data from the 8 connections via this one connection.

Example: Settings for the local partner:

- 3964(R) protocol
- Communication direction 1: Local --> partner
- max. 8 connections, local IDs: 1000; 1001, ..., 1007

Settings for the connection partner:

- 3964(R) protocol
- Communication direction 2: Partner --> local
- max. 1 connection, local ID: 1000

#### Number of connections

The maximum number of configurable connections per device (CPU/FM) depends on the resources of the module you are using.

### PtP communication direction (S7-300, S7-400, S7-1500)

#### Communications direction

For PtP connections, you can specify different communications directions. To do this, select the corresponding check box:

- Local → partner:

  Connections via which you want to send frames.
- Partner → local:

  Connections via which you want to receive frames.
- Local ↔ partner:

  Connections via which you want to send and receive frames.

> **Note**
>
> You will find more detailed information on specifying the communications direction in the documentation of your module.

### PtP link path (S7-300, S7-400, S7-1500)

#### Setting the connection path

In "General > Connection path". you can set the path taken by the connection from the local endpoint to the connection partner in the settings relating to the communications direction. You can select the path depending on the configured PtP CPs. Example: The local partner contains two PtP CPs. In this case, you can select the CP via which the connection will run.

Special feature: In contrast to the S7 connections, when configuring PtP connections to an unspecified partner, networking of the local partner is not essential. The communications partners only need to be networked in your real system before you put the connection into operation.

#### Selection options for the connection partners

- Via CP:

  For the local partner, you can select the PtP CP via which the connection will run (name of the CP along with the rack and slot).
- Interface:

  SIMATIC S7 CPs have several channels (interfaces) via which the PtP connections can be established. The channel and the protocol used for the channel are displayed (channel/protocol). You configured the protocol with the special configuration software of the CP.
- Type:

  The Interface type " PtP" is displayed here.

#### "Connection selected via RK512 CPU no.:" (local)

Automation systems capable of multicomputing (for example SIMATIC S7-400) can contain several CPUs. For this reason, you need to specify a CPU number with which the partner can access the connection.

If you have selected **Partner -> Local** or **Local <-> Partner** as the communications direction and want to receive frames from the partner using an SFB, enter the number of the CPU (1 to 4) of the **local partner** here.

The CPU number specified here must match the CPU number entered in the command frame header of the CP (for the structure of the command frame, refer to the documentation of the CP you are using). If they match, the partner accesses the connection using this CPU number.

> **Note**
>
> If you want to send and receive frames using SFBs, complete the two boxes below "Local" and "Partner". You will find the maximum number of connections over which you can send/receive frames in the documentation of the CP you are using.

#### "RK512 CPU no.:" (partner)

Automation systems capable of multicomputing (for example SIMATIC S7-400) can contain several CPUs. For this reason, you need to specify a CPU number to which the connection will go.

If you have selected **Local -> Partner** or **Local <-> Partner** as the communications direction and want to send frames to the partner using an SFB, enter the number of the CPU (1 to 4) of the **connection partner** here.

The CP enters the CPU no. you have specified in the command frame header of the frame to be sent. Using this CPU number, one of the 4 CPUs of the connection partner will be accessed.

When transferring to third-party devices, it is also possible to specify "0" as the CPU no. This makes broadcast access possible on the partner station. If a CP 441 is the partner, CPU 1 is then always accessed.

> **Note**
>
> If you want to send and receive frames using SFBs, complete the two boxes below "Local" and "Partner". You will find the maximum number of connections over which you can send/receive frames in the documentation of the CP you are using.

### PtP - special connection properties (S7-300, S7-400, S7-1500)

#### Relevance

You can specify additional properties of the local connection endpoint in the "Properties > General > Special connection properties" parameter group.

#### Configured at one end

Configured at one end means that the connection partner functions as a server on this connection and cannot send or receive actively.

#### Establishing an active connection

Use this option to specify whether the connection is established from this device. This is the default option if the address of the partner is specified.

- ON: Connection is established actively.
- OFF: Connection is established by the partner.

If you selected "Unspecified" as the connection partner when you created the connection, the option is deselected by default. If you select the option you must specify the address of the partner in the "Addresses" tab.

> **Note**
>
> Not every node is capable of handling the connection establishment. In this case, the partner must initiate the establishment; the check boxes are grayed out and cannot be changed.

#### Send status messages

The connection partners can also exchange their status messages via an existing connection.

Select the check box if you want the local device to send its status messages to the partner. The status messages can then be received on the partner using the [USTATUS](S7%20communication%20%28S7-300%2C%20S7-400%29.md#ustatus-uncoordinated-receiving-of-remote-device-status-s7-400) instruction (SFB 23).

---
title: "Basics (RT Unified)"
package: CommunicationWCCUenUS
topics: 25
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Basics (RT Unified)

This section contains information on the following topics:

- [Basics of communication (RT Unified)](#basics-of-communication-rt-unified)
- [Configuring an HMI connection (RT Unified)](#configuring-an-hmi-connection-rt-unified)
- [Device configuration (RT Unified)](#device-configuration-rt-unified)

## Basics of communication (RT Unified)

This section contains information on the following topics:

- [Communication between devices (RT Unified)](#communication-between-devices-rt-unified)
- [Configuring communication (RT Unified)](#configuring-communication-rt-unified)
- [Secure communication and certificates (RT Unified)](#secure-communication-and-certificates-rt-unified)
- [Networks and connections (RT Unified)](#networks-and-connections-rt-unified)
- [Synchronization (RT Unified)](#synchronization-rt-unified)

### Communication between devices (RT Unified)

#### Communication

The data exchange between two devices is known as communication. The devices can be interconnected directly or via a network. The networked devices in communication are referred to as communication partners.

![Communication](images/159451423115_DV_resource.Stream@PNG-en-US.png)

Data transferred between the communication partners is used for various purposes:

- Display processes
- Operate processes
- Output alarms
- Archive process values and alarms
- Document process values and alarms
- Administer process parameters and machine parameters

#### Communication partners in the automation system

An automation system consists of the following communication partners:

- PLC

  The PLC controls a process by means of a user program.
- HMI device

  The HMI device is used to operate and monitor the process.

  Communication between the communication partners PLC and HMI device is described below.

  Additional information on other forms of communication is available in the online help of the TIA Portal in the section "Editing devices &amp; networks".

  If the following requirements are met, the PLC and HMI device form an automation system:

  - PLC and HMI device are linked to each other
  - Network between PLC and HMI device is configured

#### Network configuration

The basis for all types of communication is a network configuration.

- Every device in a network has a unique address.
- The devices carry out communication with consistent transmission characteristics.

#### Data exchange using tags

Process values such as temperatures and levels are transferred by tags in Runtime. Process values are stored in the memory of one of the connected automation systems.

To access the process data with the HMI device, link the external HMI tags to the PLC tags.

For additional information on configuring tags, refer to "[Configuring tags](Configuring%20tags%20%28RT%20Unified%29.md#basics-rt-unified)".

#### Communication via a uniform and vendor-neutral interface

With OPC UA (Open Platform Communications Unified Architecture), WinCC has a uniform and manufacturer-independent software interface. This interface enables standardized data exchange between industrial, office, and manufacturing applications.

For more detailed information, refer to the documentation for OPC UA.

---

**See also**

[Supported PLCs and communication channels (RT Unified)](#supported-plcs-and-communication-channels-rt-unified)
  
[Configuring communication (RT Unified)](#configuring-communication-rt-unified)
  
[Resources Monitor (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#resources-monitor-rt-unified)

### Configuring communication (RT Unified)

#### Introduction

To configure an automation system, you configure the connections in the "Devices &amp; networks" editor. Connections of devices that are within the same project and were created with the "Devices &amp; networks" editor are referred to as integrated connections. Connections of devices that were created with the "Connections" editor are referred to as non-integrated connections. The devices do not all have to be within the same project.

You use the graphic and table network view for the configuration.

#### Requirement

- The network configuration is complete.
- HMI device and PLC are available in the hardware catalog.

> **Note**
>
> **Non-integrated configuration**
>
> If integrated configuration of the HMI connections is not possible, create non-integrated HMI connections of the HMI device using the "Connections" editor.

#### Procedure

To set up an automation system, always follow the steps below:

1. **Inserting devices**

   You drag a PLC and an HMI device from the hardware catalog to the network view of the "Devices &amp; networks" editor.
2. **Configuring devices**

   Depending on the HMI device used, you add the required communications modules to your PC station.
3. **Networking devices**

   In the networking step, you configure the physical connection of the devices.

   To connect the devices, you connect the interfaces of the devices with communications capability using drag and drop.
4. **Connecting devices**

   To set up a logical communication connection between the communication partners, you create an HMI connection between the networked devices.

   The tabular network overview supplements the graphical network view.

   In addition, the created HMI connection is also visible in the "Connections" editor of the HMI device where it can be configured.

---

**See also**

[Supported PLCs and communication channels (RT Unified)](#supported-plcs-and-communication-channels-rt-unified)
  
[Networking the HMI device and PLCs (RT Unified)](#networking-the-hmi-device-and-plcs-rt-unified)
  
[Creating an integrated HMI connection (RT Unified)](#creating-an-integrated-hmi-connection-rt-unified)
  
[Creating a non-integrated HMI connection (RT Unified)](#creating-a-non-integrated-hmi-connection-rt-unified)
  
[Communication between devices (RT Unified)](#communication-between-devices-rt-unified)

### Secure communication and certificates (RT Unified)

#### Introduction

Runtime Unified supports secure communication with PLCs of the series S7-1200 and S7-1500.

With secure communication, the connection between Runtime and PLC is encrypted by the TLS protocol. A valid PLC certificate must be configured on the PLC.

> **Note**
>
> **Encryption with TLS**
>
> Always use the most current version of TLS. Disable the older version.
>
> The use of older versions (TLS 1.0 und 1.1) is at your own risk.

Also observe the instructions in SiePortal:

- [Making use of Runtime by using certificates](https://support.industry.siemens.com/cs/ww/en/view/109806850)
- [Security guidelines for SIMATIC HMI operator devices and SIMATIC WinCC Unified](https://support.industry.siemens.com/cs/ww/en/view/109481300)

**Connection without secure communication**

The connection between Runtime and a PLC without certificate is possible in the following cases:

- If the PLC does not support the use of certificates, e.g. PLCs with older firmware or other series.
- If the option "Only allow secure PG/PC and HMI communication" has been disabled in the engineering at the PLC.

  If this option is disabled, the use of a PLC certificate is optional. If no PLC certificate has been configured, communication is encrypted via CSI. If a PLC certificate has been configured, it is used for authentication and encryption.

  > **Note**
  >
  > Disabling this option increases the security risk. Using certificates is recommended.

#### Requirement

The following requirements apply for secure communication between Runtime and PLC:

- The PLC has the following firmware:

  - S7-1200: Firmware 4.5 and higher
  - S7-1500: Firmware 2.9 and higher
- A valid certificate has been configured for the PLC in engineering in the certificate manager:

  - Self-signed end unit certificate   
    or
  - End entity certificate issued by a certification authority as well as the root certificate of the certification authority and its certificate revocation list.
  > **Note**
  >
  > It is recommended to enable the "Only allow secure PG/PC and HMI communication" option on the PLC under "Protection &amp; Security &gt; Connection mechanism". If this option is enabled, the PLC always uses secure communication.
- The HMI device has an integrated connection to the PLC.  
  Or

  The HMI device has a non-integrated connection to a device proxy. The device proxy uses the current device proxy data of the PLC.  
  Or

  The HMI device has been connected to the PLC using the "ChangeConnection" system function.

  > **Note**
  >
  > The HMI device does not initially trust the PLC certificate after calling the system function. To establish a secure connection, you must trust the certificate manually:
  >
  > - Unified PC: SIMATIC Runtime Manager &gt; Settings &gt; Certificates
  > - Unified Panel: Control Panel &gt; Security &gt; Certificates

#### Connection establishment

With secure communication, the PLC sends its certificate to the HMI device for establishing the connection. The HMI device checks the certificate:

- If the HMI device trusts the PLC certificate, the connection is established. The session remains until the connection is interrupted. The process is repeated the next time the connection is established.

  > **Note**
  >
  > Stopping or restarting Runtime interrupts the connection.
  >
  > The following actions do not interrupt the connection:
  >
  > - Stopping or restarting the PLC.
  > - Download to device (PLC or HMI device)
- If the HMI device does not trust the certificate, the connection is rejected. A system event is output. After the time needed for reconnection (ReconnectTime) has elapsed, the HMI device starts a new connection attempt.

If an integrated connection to the PLC is configured on the HMI device or a non-integrated connection to a device proxy of the PLC, the PLC certificates are loaded into the device when the HMI device is loaded. They are part of the current configuration of the HMI device and automatically have the "Trusted" status. The connection is established automatically.

If the "ChangeConnection" system function was called on the HMI device, the HMI device does not trust the PLC certificate at first. The PLC certificate has the status "untrusted". You must trust the certificate manually:

- Unified PC: SIMATIC Runtime Manager &gt; Settings &gt; Certificates
- Unified Panel: Control Panel &gt; Security &gt; Certificates

#### Change to PLC configuration after loading the HMI device.

If you change the PLC configuration in the Engineering System and do not reload the HMI device, the following scenarios may occur the next time a connection is established.

**PLC certificate deleted**

If secure communication is not mandatory for the PLC, the connection is established.

If secure communication is mandatory for the PLC, no connection is established.

**PLC certificate added for the first time or existing PLC certificate replaced.**

The connection is rejected. Trust the certificate on the HMI device manually:

- Unified PC: Via "SIMATIC Runtime Manager &gt; Settings &gt; Certificates"
- Unified Panel: Via "Control Panel &gt; Security &gt; Certificates"

The next connection attempt is successful.

#### Connection with secure communication from a Panel to Runtime Unified.

Only secure communication is supported between Runtime and Panels.

A Panel that does not support secure communication cannot communicate with Runtime.

Secure communication cannot be disabled for a Panel that supports it.

Disabling the "Only allow secure PG/PC and HMI communication" option in the properties of a PLC has no effect.

#### Certificate revocation list (CRL)

A certificate revocation list contains certificates that were revoked before they expired and, therefore, are no longer trusted. A certificate revocation list is provided as a CERT file (encoded in PEM or DER format). More than one certificate revocation list can exist.

You can find or manage the certificate revocation lists of the HMI device here:

- Unified PC: SIMATIC Runtime Manager &gt; Settings &gt; Certificates
- Unified Panel: Control Panel &gt; Security &gt; Certificates

While the HMI connection to a PLC is being established, the PLC certificate is compared with the certificate revocation list. If the certificate is listed there, the connection is denied. An alarm is output.

### Networks and connections (RT Unified)

This section contains information on the following topics:

- [SIMATIC communication networks (RT Unified)](#simatic-communication-networks-rt-unified)
- [Connections (RT Unified)](#connections-rt-unified)

#### SIMATIC communication networks (RT Unified)

This section contains information on the following topics:

- [Communication networks (RT Unified)](#communication-networks-rt-unified)
- [PROFINET Industrial Ethernet (RT Unified)](#profinet-industrial-ethernet-rt-unified)

##### Communication networks (RT Unified)

###### Overview

Communication networks are a central component of an automation solutions. Industrial networks fulfill special requirements:

- Coupling of automation systems as well as simple sensors, actuators, and PCs
- Error-free transfer of information at the right time
- Robustness against electromagnetic interference, mechanical stresses and soiling
- Flexible adaptation to the production requirements

Industrial networks belong to the LANs (Local Area Networks) and allow communication within a limited area.

Industrial networks fulfill the following communication functions:

- Process and field communication of the automation systems including sensors and actuators
- Data communication between automation systems
- IT communication for integrating information technology

###### HMI devices in the plant network

You connect an HMI device in the network to SIMATIC S7 modules that have an integrated interface of the corresponding communication channel.

You can connect multiple HMI devices to one SIMATIC S7 PLC and multiple SIMATIC S7 PLCs to one HMI device. The maximum number of communication partners that you can connect to an HMI device is dependent on the HMI device used.

Additional information is available in the documentation for the respective HMI device.

---

**See also**

[PROFINET Industrial Ethernet (RT Unified)](#profinet-industrial-ethernet-rt-unified)

##### PROFINET Industrial Ethernet (RT Unified)

###### PROFINET

PROFINET is an open standard for industrial automation defined by IEEE 61158 and based on Industrial Ethernet. PROFINET makes use of IT standards all the way to the field level and enables plant-wide engineering.

With PROFINET, you realize automation solutions, the high performance and communication in real-time requirements.

###### Industrial Ethernet

Industrial Ethernet, which is based on IEEE 802.3, enables you to connect your automation system to your office networks. Industrial Ethernet provides IT services that you can use to access production data from the office environment.

---

**See also**

[Communication networks (RT Unified)](#communication-networks-rt-unified)

#### Connections (RT Unified)

This section contains information on the following topics:

- [HMI connection (RT Unified)](#hmi-connection-rt-unified)
- [Additional connection types (RT Unified)](#additional-connection-types-rt-unified)
- [Supported PLCs and communication channels (RT Unified)](#supported-plcs-and-communication-channels-rt-unified)

##### HMI connection (RT Unified)

###### Definition

An HMI connection is a logical connection between an HMI device and a PLC. The HMI connection enables communication between the communication partners.

Unlike an S7 connection, the HMI connection is assigned to the HMI device.

###### Layout

The HMI connection defines the following within the plant network:

- Communication partners

  The HMI connection identifies the devices in the plant configuration.
- Communication channel over which these communication partners communicate.

  The HMI connection requires a configured network.
- Communication path

  The HMI connection defines the interface parameters and the network addresses of the communication partners.

###### HMI connection types

The options for addressing external tags depend on the type of HMI connection between WinCC and the PLC in question. The TIA Portal supports the following types of connection:

- Integrated HMI connection

  In the TIA Portal you configure integrated HMI connections between the devices in the "Devices &amp; Networks" editor. An integrated HMI connection enables an optimized data exchange.
- Non-integrated HMI connection

  In the case of a non-integrated connection, the PLC program can be created outside the WinCC project. You configure the PLC and the WinCC project independently each other. For configuration in WinCC, you only need to know the addresses used in the PLC and their function.

  You use a non-integrated HMI connection, for example, in the following application cases:

  - You configure a WinCC project for external PLCs.
  - You do not have access to the device configuration of a SIMATIC PLC, for example, because you are working without a STEP 7 license.

  You configure a non-integrated HMI connection for the HMI device in the "Connections" editor of the WinCC project.

---

**See also**

[Creating an integrated HMI connection (RT Unified)](#creating-an-integrated-hmi-connection-rt-unified)
  
[Creating a non-integrated HMI connection (RT Unified)](#creating-a-non-integrated-hmi-connection-rt-unified)
  
[Additional connection types (RT Unified)](#additional-connection-types-rt-unified)
  
[Setting up switch on/switch off of a connection in runtime (RT Unified)](#setting-up-switch-onswitch-off-of-a-connection-in-runtime-rt-unified)

##### Additional connection types (RT Unified)

###### Overview

The following table provides an overview of the connection types that you can use in addition to the HMI connection for communication to specific device types and areas of application.

Additional information on connection types is available in the online help of the TIA Portal in the section "Editing devices &amp; networks".

| Connection type | Description | Application |
| --- | --- | --- |
| S7 connections | Connection type can be used in all S7 devices | Data exchange between SIMATIC S7 stations |
| FDL connection | Fieldbus Data Link  Security layer  Based on PROFIBUS | Communication with a partner that supports sending and receiving according to the SDA function (Send Data with Acknowledge), e.g. SIMATIC S5 or PC. |
| ISO transport connection | Suitable for large amounts of data  Based on ISO transport | Communication with a partner that supports sending and receiving data in accordance with ISO transport, e.g. SIMATIC S5 or PC. |
| ISO-on-TCP connection | Transmission Control Protocol/Internet Protocol with the extension RFC 1006  Corresponds to the standard TCP/IP | Communication with a partner that supports sending and receiving of data in accordance with ISO-on-TCP, e.g. PC or external system. |
| TCP connection | Transmission Control Protocol/Internet Protocol  Corresponds to the standard TCP/IP | Communication with a partner that supports sending and receiving data in accordance with TCP/IP, e.g. PC or external system. |
| UDP connection | User Datagram Protocol  Subnet: Industrial Ethernet | Unsecured transmission of related data fields between two nodes |
| Email connection | In the case of an email connection, the mail server via which all emails sent by an IT-CP are delivered is defined. | For example, enables the sending of process data, for example, from data blocks via email using a CP with IT functionality (IT-CP); |
| P2P connection | Peer-to-Peer  Communication between two equal devices | Communication with external devices. e.g. a printer. |

---

**See also**

[HMI connection (RT Unified)](#hmi-connection-rt-unified)

##### Supported PLCs and communication channels (RT Unified)

###### Overview

Your HMI device can communicate with the following SIMATIC PLC families via integrated HMI connections:

| SIMATIC PLC family | Supported communication channels | Comment |
| --- | --- | --- |
| SIMATIC S7-1200/1500 | Industrial Ethernet | Parallel communication with several PLCs is possible |
| SIMATIC S7-300/400 | Industrial Ethernet | Parallel communication with several PLCs is possible |

###### Communication drivers

In the case of non-integrated connections, the HMI devices, PC systems and PLCs communicate via the following communication drivers:

| Communication drivers | Interface/Communication channel | HMI device/  Panel | PC system | Comment |
| --- | --- | --- | --- | --- |
| SIMATIC S7-1200/1500 | Industrial Ethernet/PROFINET | x |  | Parallel communication with several PLCs is possible |
| Ethernet  MPI/DP |  | x |  |  |
| SIMATIC S7-300/400 | Industrial Ethernet/PROFINET | x |  | Parallel communication with several PLCs is possible |
| Ethernet  MPI/DP |  | x |  |  |
| SIMATIC HMI HTTP | Ethernet ⇒ http/https |  | x |  |
| Allen-Bradley Ethernet IP | Industrial Ethernet | x |  | Parallel communication with several PLCs is possible |
| Allen Bradley DF1 | COM interface |  | x |  |
| Mitsubishi FX | COM interface |  | x | Parallel communication with several PLCs is possible |
| Mitsubishi iQr/iQF | Industrial Ethernet | x |  |  |
| Mitsubishi MC TCP/IP | Industrial Ethernet | x |  | Parallel communication with several PLCs is possible |
| Ethernet |  | x |  |  |
| Modbus RTU | COM interface |  | x |  |
| Modbus TCP/IP | Industrial Ethernet | x |  | Parallel communication with several PLCs is possible |
| Ethernet |  | x |  |  |
| Omron Ethernet/IP | Industrial Ethernet | x |  | Parallel communication with several PLCs is possible |
| Omron Host Link | COM interface |  | x |  |
| OPC UA | OPC | x | x | Parallel communication via OPC UA connections possible |
| LOGO! | Ethernet |  | x |  |

---

**See also**

[Communication between devices (RT Unified)](#communication-between-devices-rt-unified)
  
[Configuring communication (RT Unified)](#configuring-communication-rt-unified)

### Synchronization (RT Unified)

#### Time synchronization on the S7-1200/1500

1. To make settings for the time synchronization, select the "Online &amp; Diagnostics" node of the PLC in the project tree.
2. In the Inspector window, select "Properties &gt; General &gt; Time of day".

   ![Time synchronization on the S7-1200/1500](images/159586963851_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > **Example of window**
   >
   > Different settings are available depending on the configured PLC.
3. Select the time zone where the device is located.
4. Enable the time synchronization for the device by selecting how the NTP server is accessed under "Time synchronization".
5. Specify at least one NTP server.
6. Complete the settings for

   - Update interval
   - Daylight saving time
   - Start of standard time

#### Time synchronization on the S7-300/400

1. To make settings for the time synchronization, select the "Online &amp; Diagnostics" node of the PLC in the project tree.
2. In the Inspector window, select "Properties &gt; General &gt; Time of day".

   ![Time synchronization on the S7-300/400](images/160082060811_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > **Example of window**
   >
   > Different settings are available depending on the configured PLC.
3. Select the synchronization type for the interfaces.
4. Specify a correction factor.

#### Time synchronization for PROFINET interfaces on Panels

> **Note**
>
> Activating this service reduces security against unauthorized access to functions and data of the PLC from the outside and via the network.

1. To make settings for the time synchronization, select the "Online &amp; Diagnostics" node of the panel in the project tree.
2. Select "Properties &gt; PROFINET interface [x] &gt; Time synchronization" in the Inspector window.

   ![Time synchronization for PROFINET interfaces on Panels](images/159588765579_DV_resource.Stream@PNG-en-US.png)
3. Enable the time synchronization.
4. Specify at least one NTP server.

## Configuring an HMI connection (RT Unified)

This section contains information on the following topics:

- [Configuring an integrated HMI connection (RT Unified)](#configuring-an-integrated-hmi-connection-rt-unified)
- [Configuring a non-integrated HMI connection (RT Unified)](#configuring-a-non-integrated-hmi-connection-rt-unified)
- [Setting up switch on/switch off of a connection in runtime (RT Unified)](#setting-up-switch-onswitch-off-of-a-connection-in-runtime-rt-unified)

### Configuring an integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [Networking the HMI device and PLCs (RT Unified)](#networking-the-hmi-device-and-plcs-rt-unified)
- [Creating an integrated HMI connection (RT Unified)](#creating-an-integrated-hmi-connection-rt-unified)

#### Networking the HMI device and PLCs (RT Unified)

##### Introduction

You can network an HMI device to several PLCs. The networking of devices is depicted by lines that are colored depending on the interface type.

The number of available interfaces and interface types depends on the device. To make additional interfaces available on the device, add a communications module to the device.

##### Requirement

- The "Devices &amp; Networks" editor is open.
- The networks are configured.
- An HMI device is configured in the "Devices &amp; Networks" editor.
- The PLC is configured in the "Devices &amp; Networks" editor.

##### Procedure

To network an HMI device and a PLC, follow these steps:

1. Open the network view of the "Devices &amp; Networks" editor.
2. Enable the "Networking" mode.
3. Use a drag-and-drop operation to interconnect the interfaces of the desired communication network of the devices.

   A connection is shown as graphic and table in the network view.

   ![Procedure](images/159465916171_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159465916171_DV_resource.Stream@PNG-en-US.png)

   The tabular network overview supplements the graphical network view with the following additional functions:

   - You obtain detailed information on the structure and parameter settings of the devices.
   - Using the "Subnet" column, you can connect communication-capable components to subnets that have been created.

     ![Procedure](images/159466936715_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/159466936715_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating an integrated HMI connection (RT Unified)](#creating-an-integrated-hmi-connection-rt-unified)
  
[SIMATIC communication networks (RT Unified)](#simatic-communication-networks-rt-unified)

#### Creating an integrated HMI connection (RT Unified)

##### Introduction

An integrated HMI connection connects an HMI device and a SIMATIC S7 PLC within your project.

##### Connection resources

Each connection requires connection resources for the end point or transition point on the devices involved. The number of connection resources is device-specific.

If all connection resources of a communication partner are allocated, no new connection can be configured.

##### Requirement

- The networks are configured.
- An HMI device and a SIMATIC PLC are configured and networked.
- The network view is open in the "Devices &amp; Networks" editor.

##### Create an integrated HMI connection

1. Enable the "Connections" mode.
2. Select the "HMI connection" connection type.

   The devices available for connection are highlighted in color.

   ![Create an integrated HMI connection](images/159467514635_DV_resource.Stream@PNG-de-DE.png)

   ![Create an integrated HMI connection](images/159467514635_DV_resource.Stream@PNG-de-DE.png)
3. Use a drag-and-drop operation to interconnect the interfaces of the desired communication channel of the HMI device and PLC with each other.

   The HMI connection is shown as graphic and table in the network view.

   In the table area of the editor, the HMI connection is displayed on the "Connections" tab.
4. Change the connection parameters in the tabular area according to the requirements of your project.

**Note**

**Change local connection names**

You can change the local name for the connection only in the tabular area of the editor.

##### Open the graphic view of the connection partners

1. Select the HMI connection.
2. Click "Highlight HMI connection" and select the HMI connection.

   ![Open the graphic view of the connection partners](images/159468380811_DV_resource.Stream@PNG-en-US.png)

   ![Open the graphic view of the connection partners](images/159468380811_DV_resource.Stream@PNG-en-US.png)

   The connection path is shown in the Inspector window under "Properties &gt; General &gt; General".

##### Change the connection path

1. Open the graphic view display of the connection partners.
2. Select a different interface in the Inspector window under "Properties &gt; General &gt; General &gt; Interface".

   The existing connection parameters are highlighted as invalid.
3. To validate the connection parameters, click on "Find connection path".

   The connection parameters are reassigned and validated.

##### Create an integrated HMI connection in the "Tags" editor

1. Double-click on "HMI tags" below your HMI device in the project tree.
2. Select a tag table.

   The "HMI tags" editor opens.
3. Create an HMI tag.
4. Connect the HMI tag to an existing PLC tag of the matching data type.
5. The integrated HMI connection to the PLC is established automatically.

![Create an integrated HMI connection in the "Tags" editor](images/159468391179_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[HMI connection (RT Unified)](#hmi-connection-rt-unified)
  
[Networking the HMI device and PLCs (RT Unified)](#networking-the-hmi-device-and-plcs-rt-unified)
  
[S7-1500 | Integrated HMI connection (RT Unified)](Communication%20with%20SIMATIC%20PLCs%20%28RT%20Unified%29.md#s7-1500-integrated-hmi-connection-rt-unified)
  
[S7-300/400 | Integrated HMI connection (RT Unified)](Communication%20with%20SIMATIC%20PLCs%20%28RT%20Unified%29.md#s7-300400-integrated-hmi-connection-rt-unified)

### Configuring a non-integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [Configuring non-integrated connections (RT Unified)](#configuring-non-integrated-connections-rt-unified)
- [Creating a non-integrated HMI connection (RT Unified)](#creating-a-non-integrated-hmi-connection-rt-unified)

#### Configuring non-integrated connections (RT Unified)

##### Introduction

A non-integrated HMI connection requires a communication driver and a good understanding of the address structure of the communication partner.

##### Addressing with non-integrated connections

In the case of a project with a non-integrated connection, you always configure a tag connection exclusively with absolute addressing.

Select the valid data type yourself. If the address of a PLC tag changes in a project with a non-integrated connection during the course of the project, you also have to perform the change in WinCC. The tag connection is not checked for validity in Runtime. No alarm is displayed.

##### Communication drivers

A communication driver is a software component that establishes a connection between a PLC and an HMI device. The communication driver thus enables the assignment of process values to HMI tags.

Depending on the HMI device used and the connected communication partner, you select the interface used as well as the profile and transmission speed.

##### Basic procedure

The following steps are required to work in your project in a non-integrated connection:

1. Create an HMI connection
2. Select communication drivers and interfaces
3. Address the communication partners
4. Assign the communication network
5. Close the connection

---

**See also**

[Creating a non-integrated HMI connection (RT Unified)](#creating-a-non-integrated-hmi-connection-rt-unified)
  
[Supported PLCs and communication channels (RT Unified)](#supported-plcs-and-communication-channels-rt-unified)

#### Creating a non-integrated HMI connection (RT Unified)

##### Introduction

A non-integrated connection connects an HMI device to a PLC that is configured outside your project. You create the non-integrated HMI connection in the "Connections" editor of the HMI device.

##### Requirements

- A project is open.
- An HMI device has been created.

##### Procedure

To create a non-integrated connection, follow these steps:

1. Double-click "Connections" in the project tree below your HMI device.

   The "Connections" editor opens.

   Existing integrated connections are identified with ![Procedure](images/104228638859_DV_resource.Stream@PNG-de-DE.png).

   Existing non-integrated connections are identified with ![Procedure](images/104228646283_DV_resource.Stream@PNG-de-DE.png).
2. Create a new connection with "Add".
3. Select the communication driver. Use the communication driver of the required PLC family.
4. Select the required interface of the HMI device in the graphic area of the editor under "Parameters &gt; [HMI device type] &gt; Interface".

   The number of available interfaces on the HMI device depends on the communication driver.
5. Change the connection parameters according to the requirements of your project.

---

**See also**

[HMI connection (RT Unified)](#hmi-connection-rt-unified)
  
[Configuring non-integrated connections (RT Unified)](#configuring-non-integrated-connections-rt-unified)
  
[Supported PLCs and communication channels (RT Unified)](#supported-plcs-and-communication-channels-rt-unified)
  
[S7-1500 | Non-integrated HMI connection (RT Unified)](Communication%20with%20SIMATIC%20PLCs%20%28RT%20Unified%29.md#s7-1500-non-integrated-hmi-connection-rt-unified)
  
[S7-300/400 | Non-integrated HMI connection (RT Unified)](Communication%20with%20SIMATIC%20PLCs%20%28RT%20Unified%29.md#s7-300400-non-integrated-hmi-connection-rt-unified)

### Setting up switch on/switch off of a connection in runtime (RT Unified)

#### Introduction

If an HMI device and a PLC do not have to always be connected, terminate the connection in Runtime and establish it again when necessary. This reduces the load on the communication channel.

Configure a Runtime script for enabling/disabling a connection in runtime.

> **Note**
>
> **Alarm system and system diagnostics**
>
> After switching off the connection to a PLC, the alarms from this PLC continue to be displayed. The system diagnostics for this PLC is also available.

#### Requirement

- An HMI connection is configured.
- A button is configured in the HMI device of the HMI connection.
- The "Screens" editor is open.

#### Procedure

To configure enabling/disabling of a connection in Runtime, follow these steps:

1. Select a button.
2. Select the event that is to trigger enabling/disabling in runtime under "Properties &gt; Events" in the Inspector window.
3. Program a script to the event which enables or disables the connection via the "Set Connection mode" snippet.

#### Result

Pressing this button triggers enabling/disabling of the connection in Runtime.

---

**See also**

[Introduction to runtime scripting (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#introduction-to-runtime-scripting-rt-unified)
  
[HMI connection (RT Unified)](#hmi-connection-rt-unified)

## Device configuration (RT Unified)

This section contains information on the following topics:

- [HMI devices (RT Unified)](#hmi-devices-rt-unified)
- [Inserting a HMI device into the project (RT Unified)](#inserting-a-hmi-device-into-the-project-rt-unified)

### HMI devices (RT Unified)

Panels and PC systems are used as HMI devices.

#### Definition

An HMI device visualizes the plant process, shows the process values and enables access to the plant control system via operator inputs.

The HMI device needs a runtime software for process visualization and operation. The device must have the corresponding interfaces and communication drivers to connect the HMI device to the plant network and the PLC.

#### Structure in the device navigation

Edit further components, to configure a PC system:

- PC station

  The hardware basis of a PC system is an industrial PC.

  The PC provides the operating system, the firmware and the hardware equipment.
- WinCC Runtime software

  The Runtime software visualizes your WinCC Runtime project and enables process operation. The runtime software is available in the hardware catalog.
- Communications modules

  If the PC station does not have the required interfaces, install the required communications modules in the PC station.

A Panel is a complete integrated HMI device which does not require further components.

---

**See also**

[Inserting a HMI device into the project (RT Unified)](#inserting-a-hmi-device-into-the-project-rt-unified)

### Inserting a HMI device into the project (RT Unified)

#### Requirements

- The networks are configured.
- HMI device and PLC each support the communication channel of the respective network.
- The network view is open in the "Devices &amp; Networks" editor.
- A corresponding interface is required at both ends to connect the HMI device to the PLC.

#### Configuring a SIMATIC WinCC Unified PC

1. Drag the SIMATIC WinCC Unified PC from the hardware catalog to the work area.

   A SIMATIC PC system with the WinCC Unified PC RT is created.

   ![Configuring a SIMATIC WinCC Unified PC](images/159514571787_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a SIMATIC WinCC Unified PC](images/159514571787_DV_resource.Stream@PNG-en-US.png)
2. Select a communication module for the required interface type in the hardware catalog.
3. Drag the communication module onto the SIMATIC WinCC Unified PC.

   The communication module is added.

   ![Configuring a SIMATIC WinCC Unified PC](images/160093106187_DV_resource.Stream@PNG-de-DE.png)

   ![Configuring a SIMATIC WinCC Unified PC](images/160093106187_DV_resource.Stream@PNG-de-DE.png)
4. Drag a PLC from the hardware catalog to the work area.

   The PLC is created.
5. Network the devices.

#### Configuring a SIMATIC Unified Comfort Panel

1. Drag a SIMATIC Unified Comfort Panel from the hardware catalog to the work area.

   The SIMATIC Unified Comfort Panel is created.
2. Drag the matching PLC from the hardware catalog to the work area.

   The PLC is created.
3. Network the devices.

---

**See also**

[HMI devices (RT Unified)](#hmi-devices-rt-unified)

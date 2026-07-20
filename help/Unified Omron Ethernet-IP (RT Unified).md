---
title: "Unified Omron Ethernet/IP (RT Unified)"
package: CSP5WCCUenUS
topics: 14
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Unified Omron Ethernet/IP (RT Unified)

This section contains information on the following topics:

- [Configuring a connection via Omron Ethernet/IP (RT Unified)](#configuring-a-connection-via-omron-ethernetip-rt-unified)
- [Communication between HMI device and PLC (RT Unified)](#communication-between-hmi-device-and-plc-rt-unified)
- [Configuring the controller type and protocol (RT Unified)](#configuring-the-controller-type-and-protocol-rt-unified)
- [Communication with Omron Ethernet/IP (RT Unified)](#communication-with-omron-ethernetip-rt-unified)
- [Parameter for the connection (RT Unified)](#parameter-for-the-connection-rt-unified)
- [Parameterization of the connection (RT Unified)](#parameterization-of-the-connection-rt-unified)
- [Commissioning components (RT Unified)](#commissioning-components-rt-unified)
- [Security Information (RT Unified)](#security-information-rt-unified)

## Configuring a connection via Omron Ethernet/IP (RT Unified)

### Introduction

This section describes the communication between Omron Ethernet/IP controllers and HMI devices. These controllers communicate by means following protocols:

- Ethernet/IP – allows communication of Omron Ethernet/IP controller with WinCC Unified PC/Unified Comfort Panel device using Ethernet interface.
- TCP/IP – allows communication of multiple Omron Ethernet/IP controller with WinCC Unified PC/Unified Comfort Panel device using Ethernet interface.

You configure a connection to a PLC with a Omron Ethernet/IP communication driver in the "Connections" editor of the HMI device.

**Requirements**

- A project is open.
- An HMI device has been created.

**Procedure**

1. Double-click the HMI device under "Devices" in the project tree.

   ![Introduction](images/138559449995_DV_resource.Stream@PNG-en-US.png)
2. Double-click the "Connections" item.
3. Double-click "&lt;Add&gt;" in the "Connections" editor.
4. In the "Communication drivers" column, select the “Omron Ethernet/IP" driver.
5. Select all necessary connection parameters for the interface in the Inspector window under "Parameters".
6. Under "PLC device" area:

   - Choose the required CPU type – Currently, CJ1, CJ2 and CS1 series are supported.
   - To set the connection parameters, such as addresses and profiles, click the connection that you have created in the "Connections" editor. For more information on setting the parameters, configuring the PLC area, see “Parameters for the connection (Omron Ethernet/IP " driver).

## Communication between HMI device and PLC (RT Unified)

### Communication principle

The HMI device and the PLC communicate using tags.

**Tags**

The PLC and the HMI device use process values for data exchange. In your configuration, create tags that point to an address on the PLC. The HMI device reads and displays the value from the defined address. The operator can also make an entry on the HMI device that is then written to the address on the PLC.

> **Note**
>
> A maximum of 16 connections are supported for communication drivers of 3-party PLCs. This number can be a combination or 16 individual communication drivers. The specification is only valid for Ethernet-based communication drivers and is additionally limited by the maximum possible number of connections at the respective PLC type.

## Configuring the controller type and protocol (RT Unified)

### Select the PLC

1. For a connection with a Omron Ethernet/IP controller via the Ethernet/IP protocol, double-click "Connections" in the project window of the HMI device.
2. In the work area, select the connnection in the "Communication driver" column.  
   The Properties window displays the parameters of the selected protocol. For more details on configuring the IP address, see Omron Comfort guide.

For subsequent changes of the parameters, double-click "Connections" in the project window of the HMI device. Select the connection and edit its parameters in the properties dialog box.

> **Note**
>
> The settings on the HMI device and on the PLC must match.

## Communication with Omron Ethernet/IP (RT Unified)

This section contains information on the following topics:

- [Communication Types (RT Unified)](#communication-types-rt-unified)
- [Permitted data tyes for Omron Ethernet/IP (RT Unified)](#permitted-data-tyes-for-omron-ethernetip-rt-unified)
- [Communication partners (RT Unified)](#communication-partners-rt-unified)

### Communication Types (RT Unified)

#### Approved communication types

The following communication types are system-tested and approved for Omron Ethernet/IP:

- One-to-one connection to the approved PLCs .
- An HMI device allows up to 8 multiple parallel connections to the PLC, and it allows you to configure with the serial drivers. CPU types can be mixed.

**Supported CPU types**

The following CPU types are supported in the configuration of the Omron Ethernet/IP:

- CJ1 Series PLCs:

  - CJ1M
- CJ2 Series PLCs:

  - CJ2H
  - CJ2M
- CS1 Series PLCs:

  - CS1H
  - CS1G

> **Note**
>
> The above mentioned CPU types have been tested and released for WinCC Unified PC/Unified Comfort Panel.

### Permitted data tyes for Omron Ethernet/IP (RT Unified)

#### Permitted data types

The table lists the data types that can be used when configuring tags:

| Data Type | Operands | Length |
| --- | --- | --- |
| Bool | I/O, HR, AR, DM, EM, T, C, TCF, CCF | 1 byte |
| DInt | I/O, HR, AR, DM, EM, T, C | 4 bytes |
| DWord | I/O, HR, AR, DM, EM, T, C | 4 bytes |
| Int | I/O, HR, AR, DM, EM, T, C | 2 bytes |
| LInt | I/O, HR, AR, DM, EM | 8 bytes |
| LReal | I/O, HR, AR, DM, EM | 8 bytes |
| LWord | I/O, HR, AR, DM, EM | 8 bytes |
| Real | I/O, HR, AR, DM, EM | 4 bytes |
| String | I/O, HR, AR, DM, EM | 1 to 80 characters |
| UDInt | I/O, HR, AR, DM, EM, T, C | 4 bytes |
| UDIntBCD | I/O, HR, AR, DM, EM, T, C | 4 bytes |
| UInt | I/O, HR, AR, DM, EM, T, C | 2 bytes |
| UIntBCD | I/O, HR, AR, DM, EM, T, C | 2 bytes |
| ULInt | I/O, HR, AR, DM, EM | 8 bytes |
| ULIntBCD | I/O, HR, AR, DM, EM | 8 bytes |
| Word | I/O, HR, AR, DM, EM, T, C | 2 bytes |

> **Note**
>
> - Array data type is supported for all the above mentioned data types except Bool and String.
> - CJ1 PLC supports all operands except EM.

### Communication partners (RT Unified)

#### Introduction

This section describes communication between WinCC Unified PC/Unified Comfort Panel and Omron Ethernet/IP. The TCP/IP protocol is used for communication purposes.

CJ1, CJ2 and CS1 CPUs are supported.

## Parameter for the connection (RT Unified)

### Parameter to be set

To set the connection parameters, such as addresses and profiles, click the connection that you have created in the "Connections" editor.

The communication partners are displayed schematically in the Inspector window under "Parameter". The "HMI device" and "PLC" areas are available for assigning parameters according to the interface used.

**Parameters for the HMI device**

You can select only one interface for the HMI device in the Inspector window under "Parameter". Depending on the HMI device, there are several interfaces available.

To set up the IP address of the HMI device:

1. Click on the HMI device.

   ![Parameter to be set](images/138559449995_DV_resource.Stream@PNG-en-US.png)
2. Open the "Device configuration" editor.
3. Click the Ethernet interface.
4. Assign the IP address in the inspector window under: "General &gt; PROFINET (X1) interface &gt; Ethernet addresses"

**Parameters for the PLC**

- CPU type

  For "CPU type", you set the type of PLC to which the HMI device is connected.

  The following settings are possible:

  - Currently, CJ1, CJ2 and CS1 series PLC are supported.

  IP address

  Set the IP address of the Ethenet module of the PLC. Only the IP address can be used on a WinCC Unified PC/Unified Comfort Panel.

> **Note**
>
> Downloading of Unified Omron Ethernet/IP panel project configured in V16 and Updates from TIA Portal V17 to Unified Comfort Panel (UCP) is not supported.
>
> Migrating Projects:
>
> To migrate projects from V16 and 16 updates to V17, perform the following:
>
> 1. Migrate the TIA portal V16 Unified Omron Ethernet/IP panel project to TIA Portal V17
> 2. Change the device version from V16.x.x.x to V17.0.0.0
> 3. Compile and download to Unified Comfort Panel having V17 Runtime (applicable in configuring V16 and V16 updates project)
> 4. Downloading of UCP project containing Omron Ethernet/IP connection with device version V16.x.x.x configured in TIA portal V17 to Unified Comfort Panel (UCP) is not supported

## Parameterization of the connection (RT Unified)

This section contains information on the following topics:

- [Procedure to connect to CJ1/CJ2/CS1 Series PLC (RT Unified)](#procedure-to-connect-to-cj1cj2cs1-series-plc-rt-unified)
- [Address areas for Omron Ethernet/IP (RT Unified)](#address-areas-for-omron-ethernetip-rt-unified)

### Procedure to connect to CJ1/CJ2/CS1 Series PLC (RT Unified)

#### Procedure to connect CJ1/CJ2/CS1 series PLC

1. Open CX - Programmer.
2. Click the toolbar button [New] in CX - programmer.
3. Select the Device type as CJ1M, CJ2M or CS1H.
4. Click on setting in device Type area and select the CPU Type and Click **OK**.
5. Create a new Project under tree structure **Programs -&gt; New Program1 -&gt; Section1.**
6. Change to Run Mode by clicking **PLC -&gt; Work Online**.
7. Navigate (Double Click) to IO table and Unit Setup -&gt; Built-In Port -&gt; Ethernet Unit (Based on PLC , e.g. For CJ2M, Ethernet unit is CJ1W-EIP21)
8. Set the IP address, Subnet mask and default gateway for the Ethernet Unit and Click **OK**.
9. Before Program transfer begins, check for errors.
10. To transfer project to PLC, Select **PLC -&gt; Transfer** -&gt; To PLC. Click **OK**.
11. To upload project From PLC, Select **PLC -&gt; Transfer** -&gt; From PLC. Click **OK.**

### Address areas for Omron Ethernet/IP (RT Unified)

#### Address areas for CJ2

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **Bool** | **DInt** | **Dword** | **Int** | **LInt** | **Lreal** | **Lword** | **Real** |
| I/O | I/O 0.0 - I/O 6143.15 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6142 |
| HR | HR 0.0 - HR 511.15 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 510 |
| AR | AR 0.0 - AR 1471.15 | AR 0 - AR 1470 | AR 0 - AR 1470 | AR 0 - AR 1471 | AR 0 - AR 1468 | AR 0 - AR 1468 | AR 0 - AR 1468 | AR 0 - AR 1470 |
| DM | DM 0.0 - DM   32767.15 | DM 0 - DM   32766 | DM 0 - DM   32766 | DM 0 - DM   32767 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM   32766 |
| EM | EM 0.0:0 - EM   32767.15:25 | EM 0:0 - EM   32766:25 | EM 0:0 - EM   32766:25 | EM 0:0 - EM  32767:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM   32766:25 |
| T | T 0 - T 4095 | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | NA | NA | NA | NA |
| C | C 0 - C 4095 | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | NA | NA | NA | NA |
| TCF | TCF 0 - TCF 4095 | NA | NA | NA | NA | NA | NA | NA |
| CCF | CCF 0 - CCF 4095 | NA | NA | NA | NA | NA | NA | NA |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **String** | **UDInt** | **UDIntBCD** | **UInt** | **UIntBCD** | **ULInt** | **ULIntBCD** | **Word** |
| I/O | I/O 0 - I/O 6143 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6143 |
| HR | HR 0 - HR 511 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 511 |
| AR | AR 0 - AR 1471 | AR 0 - AR 1470 | AR 0 - AR 1470 | AR 0 - AR 1471 | AR 0 - AR 1471 | AR 0 - AR 1468 | AR 0 - AR 1468 | AR 0 - AR 1471 |
| DM | DM 0 - DM 32767 | DM 0 - DM 32766 | DM 0 - DM 32766 | DM 0 - DM 32767 | DM 0 - DM 32767 | DM 0 - DM 32764 | DM 0 - DM 32764 | DM 0 - DM 32767 |
| EM | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32766:25 | EM 0:0 - EM 32766:25 | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32764:25 | EM 0:0 - EM 32764:25 | EM 0:0 - EM 32767:25 |
| T | NA | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | T 0 - T 4095 | NA | NA | T 0 - T 4095 |
| C | NA | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | C 0 - C 4095 | NA | NA | C 0 - C 4095 |
| TCF | NA | NA | NA | NA | NA | NA | NA | NA |
| CCF | NA | NA | NA | NA | NA | NA | NA | NA |

#### Address areas for CS1

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **Bool** | **DInt** | **Dword** | **Int** | **LInt** | **Lreal** | **Lword** | **Real** |
| I/O | I/O 0.0 - I/O 6143.15 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6142 |
| HR | HR 0.0 - HR 511.15 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 510 |
| AR | AR 0.0 - AR 959.15 | AR 0 - AR 958 | AR 0 - AR 958 | AR 0 - AR 959 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 958 |
| DM | DM 0.0 - DM   32767.15 | DM 0 - DM   32766 | DM 0 - DM   32766 | DM 0 - DM   32767 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM 32766 |
| EM | EM 0.0:0 - EM   32767.15:25 | EM 0:0 - EM   32766:25 | EM 0:0 - EM   32766:25 | EM 0:0 - EM  32767:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM   32764:25 | EM 0:0 - EM 32766:25 |
| T | T 0 - T 4095 | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | NA | NA | NA | NA |
| C | C 0 - C 4095 | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | NA | NA | NA | NA |
| TCF | TCF 0 - TCF 4095 | NA | NA | NA | NA | NA | NA | NA |
| CCF | CCF 0 - CCF 4095 | NA | NA | NA | NA | NA | NA | NA |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **String** | **UDInt** | **UDIntBCD** | **UInt** | **UIntBCD** | **ULInt** | **ULIntBCD** | **Word** |
| I/O | I/O 0 - I/O 6143 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6143 |
| HR | HR 0 - HR 511 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 511 |
| AR | AR 0 - AR 959 | AR 0 - AR 958 | AR 0 - AR 958 | AR 0 - AR 959 | AR 0 - AR 959 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 959 |
| DM | DM 0 - DM 32767 | DM 0 - DM 32766 | DM 0 - DM 32766 | DM 0 - DM 32767 | DM 0 - DM 32767 | DM 0 - DM 32764 | DM 0 - DM 32764 | DM 0 - DM 32767 |
| EM | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32766:25 | EM 0:0 - EM 32766:25 | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32767:25 | EM 0:0 - EM 32764:25 | EM 0:0 - EM 32764:25 | EM 0:0 - EM 32767:25 |
| T | NA | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | T 0 - T 4095 | NA | NA | T 0 - T 4095 |
| C | NA | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | C 0 - C 4095 | NA | NA | C 0 - C 4095 |
| TCF | NA | NA | NA | NA | NA | NA | NA | NA |
| CCF | NA | NA | NA | NA | NA | NA | NA | NA |

#### Address areas for CJ1

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **Bool** | **DInt** | **Dword** | **Int** | **LInt** | **Lreal** | **Lword** | **Real** |
| I/O | I/O 0.0 - I/O 6143.15 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6142 |
| HR | HR 0.0 - HR 511.15 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 510 |
| AR | AR 0.0 - AR 959.15 | AR 0 - AR 958 | AR 0 - AR 958 | AR 0 - AR 959 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 958 |
| DM | DM 0.0 - DM   32767.15 | DM 0 - DM   32766 | DM 0 - DM   32766 | DM 0 - DM   32767 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM   32764 | DM 0 - DM   32766 |
| T | T 0 - T 4095 | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | NA | NA | NA | NA |
| C | C 0 - C 4095 | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | NA | NA | NA | NA |
| TCF | TCF 0 - TCF 4095 | NA | NA | NA | NA | NA | NA | NA |
| CCF | CCF 0 - CCF 4095 | NA | NA | NA | NA | NA | NA | NA |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Address Areas** | **String** | **UDInt** | **UDIntBCD** | **UInt** | **UIntBCD** | **ULInt** | **ULIntBCD** | **Word** |
| I/O | I/O 0 - I/O 6143 | I/O 0 - I/O 6142 | I/O 0 - I/O 6142 | I/O 0 - I/O 6143 | I/O 0 - I/O 6143 | I/O 0 - I/O 6140 | I/O 0 - I/O 6140 | I/O 0 - I/O 6143 |
| HR | HR 0 - HR 511 | HR 0 - HR 510 | HR 0 - HR 510 | HR 0 - HR 511 | HR 0 - HR 511 | HR 0 - HR 508 | HR 0 - HR 508 | HR 0 - HR 511 |
| AR | AR 0 - AR 959 | AR 0 - AR 958 | AR 0 - AR 958 | AR 0 - AR 959 | AR 0 - AR 959 | AR 0 - AR 956 | AR 0 - AR 956 | AR 0 - AR 959 |
| DM | DM 0 - DM 32767 | DM 0 - DM 32766 | DM 0 - DM 32766 | DM 0 - DM 32767 | DM 0 - DM 32767 | DM 0 - DM 32764 | DM 0 - DM 32764 | DM 0 - DM 32767 |
| T | NA | T 0 - T 4094 | T 0 - T 4094 | T 0 - T 4095 | T 0 - T 4095 | NA | NA | T 0 - T 4095 |
| C | NA | C 0 - C 4094 | C 0 - C 4094 | C 0 - C 4095 | C 0 - C 4095 | NA | NA | C 0 - C 4095 |
| TCF | NA | NA | NA | NA | NA | NA | NA | NA |
| CCF | NA | NA | NA | NA | NA | NA | NA | NA |

## Commissioning components (RT Unified)

### Transferring the PLC program to the PLC

1. Connect the PC to the PLC CPU using the appropriate cable.
2. Load the program files to the PLC CPU.
3. Then set the PLC CPU to RUN.

### Transferring the project to the PC/Panel

1. Open TIA Portal.
2. Create a new project or open an existing project as required in TIA Portal.
3. Click "Download to device" on the menu. The "Extended download to device" dialog box appears for the first compilation.
4. In the "Extended download to device" dialog box, do either of the following:

   - **To download to the PC**: Enter the IP address of the PC or the device name.
   - **To download to the Panel**: Enter the IP address of the panel.
5. Click "Connect". The connection to the device is established.
6. Click "Load" to download the project to the PC. The "Load preview" dialog box opens. The project is compiled at the same time and the result is displayed simultaneously in the "Load preview" dialog box.
7. Check the displayed pre-settings and change them as necessary.
8. Click "Load".

   After successful download, the project can be executed on the WebRH or the panel.

   Please refer to the documentation for the HMI device used for more detailed information on transfer settings.

## Security Information (RT Unified)

Use firewall If it is connected to the internet or use Omron channel in a secured environment.

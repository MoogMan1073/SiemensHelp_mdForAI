---
title: "Unified Mitsubishi iQR/iQF (RT Unified)"
package: CSP3WCCUenUS
topics: 16
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Unified Mitsubishi iQR/iQF (RT Unified)

This section contains information on the following topics:

- [Configuring a connection through Mitsubishi iQR/iQF TCP/IP (RT Unified)](#configuring-a-connection-through-mitsubishi-iqriqf-tcpip-rt-unified)
- [Communication between the HMI device and PLC (RT Unified)](#communication-between-the-hmi-device-and-plc-rt-unified)
- [Configuring the Controller type and Protocol (RT Unified)](#configuring-the-controller-type-and-protocol-rt-unified)
- [Communication with Mitsubishi iQR/iQF TCP/IP (RT Unified)](#communication-with-mitsubishi-iqriqf-tcpip-rt-unified)
- [Parameters for the connection (Mitsubishi iQR/iQF TCP/IP) (RT Unified)](#parameters-for-the-connection-mitsubishi-iqriqf-tcpip-rt-unified)
- [Permitted data types for Mitsubishi iQR/iQF TCP/IP (RT Unified)](#permitted-data-types-for-mitsubishi-iqriqf-tcpip-rt-unified)
- [Parameterization of the connection (RT Unified)](#parameterization-of-the-connection-rt-unified)

## Configuring a connection through Mitsubishi iQR/iQF TCP/IP (RT Unified)

### Introduction

This section describes the communication between Mitsubishi iQR/iQF controllers and HMI devices. These controllers communicate by means of the following protocols:

- Seamless Message Protocol (SLMP) – allows communication of Mitsubishi iQR/iQF controller with Unified panel device using ethernet interface.
- TCP/IP – allows communication of multiple Mitsubishi iQR/iQF controllers with Unified panel device using ethernet interface.

You configure a connection to a PLC with a Mitsubishi iQR/iQF TCPI/IP communication driver in the "Connections" editor of the HMI device.

The ethernet interfaces are named differently depending on the HMI device.

**Requirements**

- A project is open.
- An HMI device has been created.

**Procedure**

1. Double-click the HMI device under "Devices" in the project tree.
2. Double-click the "Connections" item.

   ![Introduction](images/137872107019_DV_resource.Stream@PNG-en-US.png)
3. Double-click "<Add new>" in the "Connections" editor.
4. In the "Communication drivers" column, select the “Mitsubishi iQR/iQF TCP/IP " driver.
5. Select all necessary connection parameters for the interface in the Inspector window under "Parameter".
6. Under PLC area:

   - Choose the required CPU type – iQR or iQF series.
   - To set the connection parameters, such as addresses and profiles, click the connection that you have created in the "Connections" editor. For more information on setting the parameters, configuring the PLC area, see “Parameters for the connection (Mitsubishi iQR/iQF TCP/IP" driver).

## Communication between the HMI device and PLC (RT Unified)

### Communication principle

The HMI device and the PLC communicate using tags and the user data areas.

**Tags**

The PLC and the HMI device exchange data using process values. In your configuration, create tags that point to an address on the PLC. The HMI device reads and displays the value from the defined address. The operator can also make an entry on the HMI device that is then written to the address on the PLC.

> **Note**
>
> A maximum of 16 connections are supported for communication drivers of 3-party PLCs. This number can be a combination or 16 individual communication drivers. The specification is only valid for Ethernet-based communication drivers and is additionally limited by the maximum possible number of connections at the respective PLC type.

## Configuring the Controller type and Protocol (RT Unified)

### Select the PLC

1. For a connection with a Mitsubishi iQR/iQF TCP/IP controller through the SLMP protocol, double click "Connections" in the project window of the HMI device.
2. In the work area, select the connection in the "Communication driver" column.

The Properties window displays the parameters of the selected protocol. For more details on configuring the IP address, see Mitsubishi Basic guide.

For subsequent changes of the parameters, double-click "Connections" in the project window of the HMI device. Select the connection and edit its parameters in the properties dialog box.

> **Note**
>
> The settings on the HMI device and on the PLC must match.

## Communication with Mitsubishi iQR/iQF TCP/IP (RT Unified)

This section contains information on the following topics:

- [Communication Types (RT Unified)](#communication-types-rt-unified)
- [Communication Partners (RT Unified)](#communication-partners-rt-unified)

### Communication Types (RT Unified)

#### Approved communication types

The following communication types are system-tested and approved for Mitsubishi iQR/iQF TCP/IP:

- one-to-one connection to the approved PLCs.
- An HMI device allows up to 8 multiple parallel connections to the PLC, and it allows you to configure with the serial drivers. CPU types (iQR and iQF) can be mixed.

### Communication Partners (RT Unified)

#### Introduction

This section describes the communication between Comfort Panels and Mitsubishi iQR/iQF TCP/IP. The SLMP protocol is used for communication purposes.

**Available communication partners**

The following Mitsubishi iQR PLCs are supported through the SLMP protocol:

- R04CPU
- R08CPU
- R016CPU
- R32CPU
- R120CPU
- R04ENCPU
- R08ENCPU
- R16ENCPU
- R32ENCPU
- R120ENCPU

The following Mitsubishi iQF PLCs are supported through the SLMP protocol:

- FX5U-32MR/DS
- FX5U-32MR/ES
- FX5U-32MT/DS
- FX5U-32MT/DSS
- FX5U-32MT/ES
- FX5U-32MT/ESS
- FX5U-64MR/DS
- FX5U-64MR/ES
- FX5U-64MT/DS
- FX5U-64MT/DSS
- FX5U-64MT/ES
- FX5U-64MT/ESS
- FX5U-80MR/DS
- FX5U-80MR/ES
- FX5U-80MT/DS
- FX5U-80MT/DSS
- FX5U-80MT/ES
- FX5U-80MT/ESS
- FX5UC-32MT/D
- FX5UC-32MT/DSS
- FX5UC-64MT/D
- FX5UC-64MT/DSS
- FX5UC-96MT/D
- FX5UC-96MT/DSS

> **Note**
>
> Following are the tested PLCs:
>
> - R08CPU
> - R16ENCPU
> - R32CPU
> - R120ENCPU
> - FX5U-32MT/ESS

## Parameters for the connection (Mitsubishi iQR/iQF TCP/IP) (RT Unified)

### Parameter to be set

To set the connection parameter, such as address and profile, click the connection that you have created in the "Connections" editor.

The communication partners are displayed schematically in the Inspector window under "Parameter". The "HMI device" and "PLC" areas are available for assigning parameters according to the interface used.

![Parameter to be set](images/137872107019_DV_resource.Stream@PNG-en-US.png)

**Parameters for the HMI device**

You can select only one interface for the HMI device in the Inspector window under "Parameter". Depending on the HMI device, there are several interfaces available.

If you are directly connected to the HMI device during configuration, you can set up the IP address of the HMI device in WinCC. The IP address is transferred to the HMI device during project transfer.

> **Note**
>
> The IP address in the control panel will be overwritten upon subsequent loading if you have already set up the IP address in the HMI device control panel.
>
> The IP address already set up in the control panel will be retained upon subsequent loading if you activate "Set IP address using a different method".

To set up the IP address of the HMI device:

1. Click on the HMI device.
2. Open the "Device configuration" editor.
3. Click the Ethernet interface.
4. Assign the IP address in the inspector window under:

   "General > interface > Ethernet addresses"

**Parameters for the PLC**

- CPU type

  For "CPU type", you set the type of PLC to which the HMI device is connected.

  The following settings are possible:

  - iQR series
  - iQF series
- IP address

  Set the IP address or host name of the Ethernet/IP module of the PLC. Only the IP address can be used on a comfort Panel.
- Port

  Set the port number of the module of the PLC as per your choice. Range is selected between 1-65534.

> **Note**
>
> Downloading of Unified Mitsubishi iQR/iQF panel project configured in V16 and Updates from TIA Portal V17 to Unified Comfort Panel (UCP) is not supported.
>
> Migrating Projects:
>
> To migrate projects from V16 and 16 updates to V17, perform the following:
>
> 1. Migrate the TIA portal V16 Unified Mitsubishi iQR/iQF panel project to TIA Portal V17
> 2. Change the device version from V16.x.x.x to V17.0.0.0
> 3. Compile and download to Unified Comfort Panel having V17 Runtime (applicable in configuring V16 and V16 updates project)
> 4. Downloading of UCP project containing Mitsubishi iQR/iQF connection with device version V16.x.x.x configured in TIA portal V17 to Unified Comfort Panel (UCP) is not supported

## Permitted data types for Mitsubishi iQR/iQF TCP/IP (RT Unified)

### Permitted data types

The table lists the data types that can be used when configuring tags:

| Data Type | Operands | Length |
| --- | --- | --- |
| Int | D, CN, W, TN, STN, SW | 2 bytes |
| word | D, TN, CN, SW, STN, W, SD | 2 bytes |
| DWord | D, LCN, W, SW, LTN, LSTN | 4 bytes |
| DInt | D, LCN, W, SW, LTN, LSTN | 4 bytes |
| Real | D, W, SW | 4 bytes |
| LReal | D, W, SW | 8 bytes |
| Bit | D, M, X, Y, F, B, SB, W, SW, SD, SM, CC, CS, TS, TC, LCS, LCC, STS, STC,   LTS, LTC, LSTS, LSTC, L | 1bit |
| String | D, W, SW | 1 to 80 characters |
| WString | D, W, SW | 1 to 40 characters |

> **Note**
>
> - The operands LTN, LTS, LTC, LSTN, LSTC, LSTS, LCN support read only for iQR.
> - L operand is supported only for iQR.
> - LCN is not supported for iQF.
> - Array data type is supported for all the above mentioned data types except string, WString, and bit.

The table lists the supported bit blocks.

## Parameterization of the connection (RT Unified)

This section contains information on the following topics:

- [iQR PLC (RT Unified)](#iqr-plc-rt-unified)
- [iQF PLC (RT Unified)](#iqf-plc-rt-unified)
- [Address areas for Mitsubishi iQR (RT Unified)](#address-areas-for-mitsubishi-iqr-rt-unified)
- [Address areas for Mitsubishi iQF (RT Unified)](#address-areas-for-mitsubishi-iqf-rt-unified)
- [Commissioning Components (RT Unified)](#commissioning-components-rt-unified)
- [Security Information (RT Unified)](#security-information-rt-unified)

### iQR PLC (RT Unified)

#### Procedure to connect iQR PLC

1. The supported PLCs are available in Gx Works 3.
2. Start Gx Works 3.
3. Create a new project. A pop-up window appears.
4. Select **Series** as **RCPU** and **Type** as per the CPU used.
5. Select the **program language** and click **Ok**.
6. Select **Online -> Current Connection Destination**.
7. On the **Connection Destination** window:

   - Set **PC side I/F** according to the communication type (USB, Ethernet etc.).
   - Set **PLC side I/F** according to the module in use.
   - Set **Other station setting** based on network.
8. Execute connection test to check if the active connection link is successful. If the connection is successful, click **Ok**, else check the connectivity.
9. Select **Online -> Read from PLC**, and execute **read from PLC** by choosing the **Select All** option.
10. In the project navigation window, select **parameter -> <CPU model used> -> Module Parameter**.
11. Select **Setting Item List > Basic settings**. Perform the following steps:

    - Own node settings - > Provide Configuration details such as IP address, Subnet Mask, Default Gateway, Enable Online Edit etc.
    - **External Device Configuration –**

      - Double-click **Detailed Setting**. The Ethernet Configuration window appears.

      - Configure the protocol as SLMP TCP/IP and enter a valid port number. By default, the remaining fields will get populated based on node settings.
12. Download the configured details to PLC by executing **Write to PLC > Select All** option.

### iQF PLC (RT Unified)

#### Procedure to connect iQR PLC

1. The supported PLCs are available in Gx Works 3.
2. Start Gx Works 3.
3. Create a new project. A pop-up window appears.
4. Select **Series** as **FX5CPU** and **Type** as per the CPU used.
5. Select the program language, and click **Ok**.
6. Select **Online->Current Connection** Destination.
7. On the **Connection Destination** window:

   - Set **PC side I/F** according communication type (USB, Ethernet etc).
   - Set **PLC side I/F** according to the module in use.
   - Set **Other station** setting based on network.
8. Execute **connection test** to check if the active connection link is successful. If the connection is successful, click **Ok,** else check the connectivity.
9. Select **Online->Read from PLC,** and execute **read from PLC** by choosing the **Select All** option.
10. In the project navigation window, select **parameter-><CPU model used >->Module Parameter><enable online change>.**
11. Select **Setting Item List** > **Basic settings.** Perform the following steps:

    - Own node settings - > Provide Configuration details such as IP addresss,Subnet Mask, Default Gateway ,Enable Online Edit etc.
    - **External Device Configuration** -

      - Double-click **Detailed Setting**. The Ethernet Configuration window appears.

      - Configure the protocol as SLMP TCP/IP, and enter a valid port number. By default, the remaining fields will get populated based on node settings.
12. Download the configured details to PLC by executing **Write to PLC >Select All** option.

### Address areas for Mitsubishi iQR (RT Unified)

#### Address areas of iQR

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **iQR** | **Bool** | **Word** | **String** | **DWord** | **Int** | **DInt** | **Real** | **LReal** | **WString** |
| B | 9A61FFF |  |  |  |  |  |  |  |  |
| CC | 8993439 |  |  |  |  |  |  |  |  |
| CN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| CS | 8993439 |  |  |  |  |  |  |  |  |
| D | D 0.0 - 10117631.15 | 10117631 | 10117627 | 10117630 | 10117631 | 10117630 | 10117630 | 10117628 | 10117592 |
| F | 32767 |  |  |  |  |  |  |  |  |
| L | 32767 |  |  |  |  |  |  |  |  |
| LCC | 4761215 |  |  |  |  |  |  |  |  |
| LCN |  |  |  | 4761214 |  | 4761214 |  |  |  |
| LCS | 4761215 |  |  |  |  |  |  |  |  |
| LSTC | 2529407 |  |  |  |  |  |  |  |  |
| LSTN |  |  |  | 2529406 |  | 2529406 |  |  |  |
| LSTS | 2529407 |  |  |  |  |  |  |  |  |
| LTC | 2529407 |  |  |  |  |  |  |  |  |
| LTN |  |  |  | 2529406 |  | 2529406 |  |  |  |
| LTS | 2529407 |  |  |  |  |  |  |  |  |
| M | 161882111 |  |  |  |  |  |  |  |  |
| SB | 9A61FFF |  |  |  |  |  |  |  |  |
| SD | SD0.0 - SD 1911.15 | 1911 |  |  |  |  |  |  |  |
| SM | 1911 |  |  |  |  |  |  |  |  |
| STC | 8993439 |  |  |  |  |  |  |  |  |
| STN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| STS | 8993439 |  |  |  |  |  |  |  |  |
| SW | SW 0.0 - SW 9A61FF.15 | 9A61FF | 9A61EB | 9A61FE | 9A61FF | 9A61FE | 9A61FE | 9A61FC | 9A61D8 |
| TC | 8993439 |  |  |  |  |  |  |  |  |
| TN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| TS | 8993439 |  |  |  |  |  |  |  |  |
| W | W 0.0 - W 9A61FF.15 | 9A61FF | 9A61EB | 9A61FE | 9A61FF | 9A61FE | 9A61FE | 9A61FC | 9A61D8 |
| X | 2FFF |  |  |  |  |  |  |  |  |
| Y | 2FFF |  |  |  |  |  |  |  |  |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **iQR** | **4-bit block** | **8-bit block** | **12-bit block** | **16-bit block** | **20-bit block** | **24-bit block** | **28-bit block** | **32-bit block** |
| B | 9A61FFC | 9A61FF8 | 9A61FF4 | 9A61FF0 | 9A61FEC | 9A61FE8 | 9A61FE4 | 9A61FE0 |
| CC |  |  |  |  |  |  |  |  |
| CN |  |  |  |  |  |  |  |  |
| CS |  |  |  |  |  |  |  |  |
| D |  |  |  |  |  |  |  |  |
| F | 32764 | 32760 | 32756 | 32752 | 32748 | 32744 | 32740 | 32736 |
| L | 32764 | 32760 | 32756 | 32752 | 32748 | 32744 | 32740 | 32736 |
| LCC |  |  |  |  |  |  |  |  |
| LCN |  |  |  |  |  |  |  |  |
| LCS |  |  |  |  |  |  |  |  |
| LSTC |  |  |  |  |  |  |  |  |
| LSTN |  |  |  |  |  |  |  |  |
| LSTS |  |  |  |  |  |  |  |  |
| LTC |  |  |  |  |  |  |  |  |
| LTN |  |  |  |  |  |  |  |  |
| LTS |  |  |  |  |  |  |  |  |
| M | 161882108 | 161882104 | 161882100 | 161882096 | 161882092 | 161882088 | 161882084 | 161882080 |
| SB | 9A61FFC | 9A61FF8 | 9A61FF4 | 9A61FF0 | 9A61FEC | 9A61FE8 | 9A61FE4 | 9A61FE0 |
| SD |  |  |  |  |  |  |  |  |
| SM | 1908 | 1904 | 1900 | 1896 | 1892 | 1888 | 1884 | 1880 |
| STC |  |  |  |  |  |  |  |  |
| STN |  |  |  |  |  |  |  |  |
| STS |  |  |  |  |  |  |  |  |
| SW |  |  |  |  |  |  |  |  |
| TC |  |  |  |  |  |  |  |  |
| TN |  |  |  |  |  |  |  |  |
| TS |  |  |  |  |  |  |  |  |
| W |  |  |  |  |  |  |  |  |
| X | 2FFC | 2FF8 | 2FF4 | 2FF0 | 2FEC | 2FE8 | 2FE4 | 2FE0 |
| Y | 2FFC | 2FF8 | 2FF4 | 2FF0 | 2FEC | 2FE8 | 2FE4 | 2FE0 |

> **Note**
>
> D, SD,SW, W supports bit values for iQR and IQF.

### Address areas for Mitsubishi iQF (RT Unified)

#### Address areas of iQF

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **iQF** | **Bool** | **Word** | **String** | **DWord** | **Int** | **DInt** | **Real** | **LReal** | **WString** |
| B | 9A61FFF |  |  |  |  |  |  |  |  |
| CC | 8993439 |  |  |  |  |  |  |  |  |
| CN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| CS | 8993439 |  |  |  |  |  |  |  |  |
| D | D 0.0 - D 10117631.15 | 10117631 | 10117627 | 10117630 | 10117631 | 10117630 | 10117630 | 10117628 | 10117592 |
| F | 32767 |  |  |  |  |  |  |  |  |
| LCC | 4761215 |  |  |  |  |  |  |  |  |
| LCS | 4761215 |  |  |  |  |  |  |  |  |
| M | 161882111 |  |  |  |  |  |  |  |  |
| SB | 9A61FFF |  |  |  |  |  |  |  |  |
| SD | SD0.0 - SD 1911.15 | 1911 |  |  |  |  |  |  |  |
| SM | 1911 |  |  |  |  |  |  |  |  |
| STC | 8993439 |  |  |  |  |  |  |  |  |
| STN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| STS | 8993439 |  |  |  |  |  |  |  |  |
| SW | SW 0.0 - SW 9A61FF.15 | 9A61FF | 9A61EB | 9A61FE | 9A61FF | 9A61FE | 9A61FE | 9A61FC | 9A61D8 |
| TC | 8993439 |  |  |  |  |  |  |  |  |
| TN |  | 8993439 |  |  | 8993439 |  |  |  |  |
| TS | 8993439 |  |  |  |  |  |  |  |  |
| W | W 0.0 - W 9A61FF.15 | 9A61FF | 9A61EB | 9A61FE | 9A61FF | 9A61FE | 9A61FE | 9A61FC | 9A61D8 |
| X | 2FFF |  |  |  |  |  |  |  |  |
| Y | 2FFF |  |  |  |  |  |  |  |  |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **iQF** | **4-bit block** | **8-bit block** | **12-bit block** | **16-bit block** | **20-bit block** | **24-bit block** | **28-bit block** | **32-bit block** |
| B | 9A61FFC | 9A61FF8 | 9A61FF4 | 9A61FF0 | 9A61FEC | 9A61FE8 | 9A61FE4 | 9A61FE0 |
| CC |  |  |  |  |  |  |  |  |
| CN |  |  |  |  |  |  |  |  |
| CS |  |  |  |  |  |  |  |  |
| D |  |  |  |  |  |  |  |  |
| F | 32764 | 32760 | 32756 | 32752 | 32748 | 32744 | 32740 | 32736 |
| LCC |  |  |  |  |  |  |  |  |
| LCS |  |  |  |  |  |  |  |  |
| M | 161882108 | 161882104 | 161882100 | 161882096 | 161882092 | 161882088 | 161882084 | 161882080 |
| SB | 9A61FFC | 9A61FF8 | 9A61FF4 | 9A61FF0 | 9A61FEC | 9A61FE8 | 9A61FE4 | 9A61FE0 |
| SD |  |  |  |  |  |  |  |  |
| SM | 1908 | 1904 | 1900 | 1896 | 1892 | 1888 | 1884 | 1880 |
| STC |  |  |  |  |  |  |  |  |
| STN |  |  |  |  |  |  |  |  |
| STS |  |  |  |  |  |  |  |  |
| SW |  |  |  |  |  |  |  |  |
| TC |  |  |  |  |  |  |  |  |
| TN |  |  |  |  |  |  |  |  |
| TS |  |  |  |  |  |  |  |  |
| W |  |  |  |  |  |  |  |  |
| X | 2FFC | 2FF8 | 2FF4 | 2FF0 | 2FEC | 2FE8 | 2FE4 | 2FE0 |
| Y | 2FFC | 2FF8 | 2FF4 | 2FF0 | 2FEC | 2FE8 | 2FE4 | 2FE0 |

### Commissioning Components (RT Unified)

#### Transferring a project to the HMI device

1. Switch the HMI device to "transfer mode".
2. Set all necessary transfer parameters.

   - Interface
   - Target storage location
3. Start the project transfer.

   The project is compiled automatically.

   All compilation and transfer steps are logged to a message window.

**Interconnecting the PLC with the HMI device**

1. Interconnect the PLC with the HMI device using a suitable cable.
2. The message "Connection to PLC .... is established" is output to the HMI device.

### Security Information (RT Unified)

Use firewall If it is connected to the internet or use Mitsubishi iQR/iQF in a secured environment.

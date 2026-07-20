---
title: "Unified Allen-Bradley EtherNet/IP (RT Unified)"
package: CSP2WCCUenUS
topics: 12
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Unified Allen-Bradley EtherNet/IP (RT Unified)

This section contains information on the following topics:

- [Supported Devices (RT Unified)](#supported-devices-rt-unified)
- [Communication with Allen-Bradley EtherNet/IP (RT Unified)](#communication-with-allen-bradley-ethernetip-rt-unified)
- [Communication through Allen-Bradley EtherNet/IP protocol (RT Unified)](#communication-through-allen-bradley-ethernetip-protocol-rt-unified)

## Supported Devices (RT Unified)

Allen-Bradley EtherNet/IP supports the following:

- WinCC Unified
- Unified Comfort Panel

### Supported Unified Comfort devices

The following Unified Comfort devices are supported:

- MTP700 Unified Comfort
- MTP1000 Unified Comfort
- MTP1200 Unified Comfort
- MTP1500 Unified Comfort
- MTP1900 Unified Comfort
- MTP2200 Unified Comfort

### Supported PLCs

The following PLCs are supported:

- ControlLogix
- CompactLogix
- SLC
- MicroLogix
- GuardLogix

## Communication with Allen-Bradley EtherNet/IP (RT Unified)

This section contains information on the following topics:

- [Communication between the HMI device and the PLC (RT Unified)](#communication-between-the-hmi-device-and-the-plc-rt-unified)

### Communication between the HMI device and the PLC (RT Unified)

#### Communications principle

The PLC and WinCC Unified PC/Unified Comfort Panel communicate using tags.

**Tags**

The PLC and WinCC Unified PC/Unified Comfort Panel use process values for data exchange. In your configuration, create tags that point to an address on the PLC. WinCC Unified PC/Unified Comfort Panel reads and displays the value from the defined address. An entry made by an operator on WinCC Unified PC/Unified Comfort Panel is written to the address on the PLC.

> **Note**
>
> A maximum of 16 connections are supported for communication drivers of 3-party PLCs. This number can be a combination or 16 individual communication drivers. The specification is only valid for Ethernet-based communication drivers and is additionally limited by the maximum possible number of connections at the respective PLC type.

## Communication through Allen-Bradley EtherNet/IP protocol (RT Unified)

This section contains information on the following topics:

- [Requirements for communication (Allen-Bradley EtherNet/IP) (RT Unified)](#requirements-for-communication-allen-bradley-ethernetip-rt-unified)
- [Configuring the controller type and protocol (Allen-Bradley EtherNet/IP) (RT Unified)](#configuring-the-controller-type-and-protocol-allen-bradley-ethernetip-rt-unified)
- [Configuring the protocol parameters (Allen-Bradley EtherNet/IP) (RT Unified)](#configuring-the-protocol-parameters-allen-bradley-ethernetip-rt-unified)
- [Permitted data types and operands (Allen-Bradley EtherNet/IP) (RT Unified)](#permitted-data-types-and-operands-allen-bradley-ethernetip-rt-unified)
- [Optimizing the configuration (Allen-Bradley EtherNet/IP) (RT Unified)](#optimizing-the-configuration-allen-bradley-ethernetip-rt-unified)
- [Commissioning components (communications modules) (RT Unified)](#commissioning-components-communications-modules-rt-unified)
- [Security Information (RT Unified)](#security-information-rt-unified)

### Requirements for communication (Allen-Bradley EtherNet/IP) (RT Unified)

#### Connections via Allen-Bradley EtherNet/IP

The connection of the HMI device to the Allen-Bradley PLC (controller) can take place through the following components:

- Existing Ethernet network that also contains the PLCs
- Cross-over Ethernet cable connected directly to the Ethernet interface of the CPU or the communication module

The connection of the HMI device to an Allen-Bradley PLC is limited primarily to the physical connection of the HMI device. No special blocks are required on the PLC for the connection.

#### Approved communication types with Allen-Bradley EtherNet/IP

The following communication types are system-tested and approved:

- Point-to-point connection to the approved PLCs
- Multipoint connection from a HMI device (Allen-Bradley Ethernet/IP-Client) with up to 8 PLCs with the respectively approved PLCs. CPU types can be mixed.

**Connection**

Connection with the following PLCs is approved with Allen-Bradley EtherNet/IP:

- CPU type: "ControlLogix, CompactLogix"

  - ControlLogix

    - 556x(1756-L6x) with Ethernet module 1756-ENBT
  - Guard Logix-System ControlLogix

    - 556xS(1756-L6xS) with Ethernet module 1756-ENBT

    - 556xS(1756-L7x) with Ethernet module 1756-ENBT and 1756-EN2TR

    - 556xS(1756-L7xS) with Ethernet module 1756-ENBT and 1756-EN2TR
  - CompactLogix

    - 533xE(1769-L3xE) with Ethernet interface onboard

    - 532xE(1769-L2xE) with Ethernet interface onboard

    - 534x (1768-L4x) with Ethernet module 1768-ENBT

    - 534x(1768-L45S) with Ethernet module 1768-ENBT

    - 534x(1768-L43S) with Ethernet module 1768-ENBT
- CPU type: "SLC, MicroLogix"

  - MicroLogix 1100 (with Ethernet interface onboard)
  - MicroLogix 1400 (with Ethernet interface onboard)
  - SLC 5/05 (with Ethernet interface onboard)

### Configuring the controller type and protocol (Allen-Bradley EtherNet/IP) (RT Unified)

#### Select the PLC

1. For a connection with a Allen-Bradley controller through the Allen-Bradley EtherNet/IP communication driver, double-click "Connections" in the project window of the HMI device.
2. In the work area, select "Allen-Bradley EtherNet/IP" protocol in the "Communication driver" column.

   The Properties window displays the parameters of the selected communication driver.

For subsequent changes of the parameters, double-click "Connections" in the project window of the HMI device. Select the connection and edit its parameters in the properties dialog box.

![Select the PLC](images/135472621323_DV_resource.Stream@PNG-en-US.png)

### Configuring the protocol parameters (Allen-Bradley EtherNet/IP) (RT Unified)

#### Parameters to be set

To set the parameters, double-click "Connections" in the project window of the HMI device.

"Allen-Bradley EtherNet/IP" is selected in the "Communication drivers" column in the work area.

The communication partners are displayed schematically in the Properties window under "Parameters". The "PLC" area is available for assigning parameters according to the interface used.

**Device-dependent parameters**

**PLC-dependent parameters**

- CPU type

  For "CPU type", set the CPU type of the PLC used.
- IP address

  Set the IP address of the PLC.
- Communication path

  Set the CIP path from the Ethernet module to the PLC. This establishes a logical connection between the Ethernet module and PLC, even if both devices are in different CIP networks.

  For additional information on this see section: Examples: Communication path.

### Permitted data types and operands (Allen-Bradley EtherNet/IP) (RT Unified)

#### Permitted data types

The table lists the data types that can be used when configuring tags.

#### CPU type: ControlLogix, CompactLogix

| Data type | Length |
| --- | --- |
| Bool | 1 bit |
| DInt | 4 bytes |
| Int | 2 bytes |
| Real | 4 bytes |
| SInt | 1 byte |
| String | 1 to 82 characters |
| UDInt | 4 bytes |
| UInt | 2 bytes |
| USInt | 1 byte |

Permitted data types arrays

| Address | Permitted data types |
| --- | --- |
| Array | SInt, USInt, Int, UInt, DInt, UDInt, Real |
| Individual bits from the basic data types of the PLC SInt, USInt, Int, UInt, DInt, UDInt | Bool* |

* Any changed value of certain defined bits is written back to the PLC. There is no check to determine whether any other bits have changed. The PLC (or other PLCs) may only read access the value.

#### CPU type: SLC, MicroLogix

| Data type | Operand type | Length |
| --- | --- | --- |
| ASCII | A | 1 to 80 characters |
| Bool | N, R, C, T, B, S, I, O | 1 bit |
| DInt | N | 4 bytes |
| Int | N, R, C, T, S | 2 bytes |
| Real | N, F | 4 bytes |
| String | ST | 1 to 82 characters |
| UDInt | N | 4 bytes |
| UInt | N, R, C, T, B, I, O | 2 bytes |

Permitted data types arrays

| Address | Permitted data types |
| --- | --- |
| Array | Int, UInt, DInt, UDInt, Real |

#### Distinctive features for connections with Allen-Bradley Ethernet/IP

With the communication driver Allen Bradley Ethernet/IP and the CPU type SLC, MicroLogix, you can only use array tags for discrete alarms and trends.

> **Note**
>
> I/O modules with 8 or 16 ports occupy one data word on the PLC.
>
> I/O modules with 24 or 32 ports occupy two data words.
>
> The HMI device does not output an error message if using non-existent bits.
>
> You should always make sure that I/O modules with 8 or 24 ports only occupy the bits that are assigned to a port.

#### Addressing in the CompactLogix, ControlLogix CPU type

**Addressing**

A tag is uniquely referenced in WinCC by means of an address in the PLC. The address must correspond with the tag name in the PLC. The tag address is defined by a string with a length of up to 128 characters.

**Using characters for addressing**

Valid characters for tag addressing:

- Letters (a to z, A to Z)
- Numbers (0 to 9)
- Underscore ( _ )

The tag address consists of tag name and other character strings used to specify the tag in the PLC.

Tag name properties:

- The tag name may begin but not end with an underscore character
- Strings with successive underscore and space characters are invalid
- The address may not exceed a length of 128 characters

  > **Note**
  >
  > The characters reserved for tag addressing may not be used in program/tag names or at any other address instance.

The reserved characters are listed below:

| Reserved character | Function |
| --- | --- |
| . | Element delimiter |
| : | Definition of a program tag |
| , | Delimiter for addressing multi-dimensional arrays |
| / | Reserved for bit addressing |
| [] | Addressing of array elements or arrays |

**PLC and program tags**

The Allen-Bradley EtherNet/IP communication driver supports addressing of PLC tags (global project tags) and/or program tags (global program tags).

A program tag is declared based on the program name in the PLC and actual tag name which are delimited by colon. PLC tags are simply addressed by their name.

> **Note**
>
> **Addressing errors**
>
> Addressing errors occur when the tag name and data type are inconsistent.
>
> Note that the tag name defined in the address field in WinCC must match the tag name in the PLC. Make sure that the data types of tags in WinCC match the data types in the PLC.

> **Note**
>
> Module-specific tags, e.g. for data on input and output modules, cannot be addressed directly. Instead, use an alias tag in the PLC.
>
> Example: Local:3:O. Data cannot be addressed in WinCC.
>
> If the alias "MyOut" is defined for Local:3:O in the PLC, you can address with WinCC via MyOut.Data.

#### Addressing syntax

**Notation of addresses**

The tables below define the notation for the individual addressing options for Allen-Bradley EtherNet/IP.

| Data types | Type | Address |
| --- | --- | --- |
| Basic data types | PLC tag | Tag name |
| Program tag | Program name: tag name |  |
| Arrays | PLC tag | Array tag |
| Program tag | Program name: array tag |  |
| Bits | PLC tag | Tagname/bitnumber |
| Program tag | Programname: tagname/bitnumber |  |
| Structure elements | PLC tag | Structure tag. Structure element |
| Program tag | Program name: structure tag. structure element |  |

> **Note**
>
> Bit addressing with the data types Bool, Real and String is not permitted and will cause an addressing fault.

**Description of the syntax**

Syntax description:

`Programname:)tagname([x(,y)(,z)]){.tagname([x(,y)(,z)])}(/bitnumber)`

- The "( )" defines an optional, single instance of an expression.
- The "{ }" defines an optional expression with multiple single instances.

The address string length may not exceed 128 characters.

#### Addressing types

**Arrays**

An array is a data structure that includes several data of the same type. WinCC only supports one-dimensional arrays.

In the address column of the tag editor, enter the array name possibly by specifying a start element. The length is defined in the Array Elements input box of the tag editor. If array limits in the PLC are exceeded (due to faulty indexing), addressing errors result.

These arrays must be declared in the PLC as controller or program tags.

Two- or three-dimensional arrays in the PLC can only be addressed in WinCC if these can be mapped area-wise onto one-dimensional arrays.

> **Note**
>
> During all read accesses and all write accesses, all array elements of a tag are always read or written, respectively. The contents of an array tag which is interconnected with a PLC are always transferred whenever there is a change. The HMI device and the PLC cannot concurrently write data to the same array tag for this reason. Instead of writing data only to a single element, the program writes the entire array to the PLC.

**Array elements**

Elements of one-dimensional, two-dimensional and three-dimensional arrays in the PLC are indexed by setting an index and the corresponding notation in the tag editor. Array addressing starts at element "0", with arrays of all basic types being valid for element addressing. Read/write operations are only carried out at the addressed element, and not for the entire array.

**Bits and bit tags**

Bit access is allowed to all basic data types except for Bool, Real and String. Bit addressing is also allowed at array/structure elements. The Bool data type is set in WinCC when bits and bit tags in the basic data types are addressed.

Single-digit bit numbers are addressed with "/x" or "/0x" (x = bit number). Bit numbers are defined by up to two digits.

> **Note**
>
> With the "Bool" data type in the data types SInt, Int and DInt, after changing the specified bit the complete tag is then written in the PLC again. In the meantime, no check is made as to whether other bits in the tag have since changed. Therefore, the PLC may have only read access to the specified tag.

**Structures**

User-defined data types are created by means of structures. These structures group tags of different data types. Structures may consist of basic types, arrays and of other structures. In WinCC, only structure elements are addressed and not entire structures.

**Structure elements**

Structure elements are addressed by means of the name of the structure and of the required structure element. This addressing is separated by point. In addition to basic data types, the structure elements may represent arrays or other structures. Only one-dimensional arrays may be used as a structure element.

> **Note**
>
> The nesting depth of structures is only limited by the maximum length of 128 characters for the address.

#### Examples: Communication path

**Example 1:**

Connection with a PLC in the same Allen-Bradley rack.

1, 0

| Number | Meaning |
| --- | --- |
| 1 | Stands for a backplane connection |
| 0 | Stands for a CPU slot number |

**Example 2:**

Connection with a PLC in remote Allen-Bradley racks. Two Allen-Bradley racks are networked on Ethernet.

1, 2, 2, 190.130.3.101, 1, 5

| Number | Meaning |
| --- | --- |
| 1 | Backplane connection |
| 2 | Stands for the CPU slot number of the second Ethernet module |
| 2 | Stands for an Ethernet connection |
| 190.130.3.101 | IP address of a remote AB rack on the network - in particular, the third Ethernet module |
| 1 | Backplane connection |
| 5 | Slot number of the CPU |

#### Addressing in the SLC, MicroLogix CPU type

**Addressing**

The addressing in the SLC, MicroLogix CPU type is entered in the following order:

- File type
- File number/Slot
- Element number
- Subordinate element
- Bit number

![Addressing in the SLC, MicroLogix CPU type](images/135471370891_DV_resource.Stream@PNG-en-US.png)

The address then appears in the following format without spaces:

- File type file number: Element number. Subordinate element
- e. g. T10:2.ACC

**Operand type**

You have the following options under operand type:

- I
- O
- S
- B
- C
- T
- R
- F
- N
- ST
- A

**File number/Slot**

Select the number between two limits under file number:

- Low limit
- High limit

The limit values depend on the selected operand type.

**Subordinate element**

You can select a subordinate element when you have selected one of the following operand types:

- R
- C
- T

#### Address areas for PLC, SLC, MicroLogix

**SLCMicro**

| Address areas | Bool | SInt | USInt | Int | UInt | DInt | UDInt | Real | String |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | N3:0/0 - N999:199 9/15 | -- | -- | N3:0 - N999:199 9 | N3:0 - N999:199 9 | N3:0 - N999:199 9 | N3:0 - N999:199 9 | N3:0 - N999:19 99 | N3:0 - N999:199 9 |
| R | R3:0.EN -  R999:199 9.ER -  R999:199 9.DN -  R999:199 9.FD -  R999:199   9.IN -  R999:199 9.EU -  R999:199 9.EM -  R999:199 9.UL | -- | -- | R3:0.LEN - R999:199 9.POS | R3:0.LEN -  R999:199 9.POS | -- | -- | -- | R3:0.LEN - R999:199 9.POS |
| C | C3:0.DN - C999:199 9.CU - C999:199 9.CD - C999:199 9.OV - C999:199 9.UN | -- | -- | C3:0.PRE - C999:199 9.ACC | C3:0.PRE - C999:199 9.ACC | -- | -- | -- | C3:0.PRE - C999:199 9.ACC |
| T | T3:0.EN - T999:1999 .TT - T999:1999 .DN | -- | -- | T3:0.PRE - T999:1999 .ACC | T3:0.PRE - T999:1999 .ACC | -- | -- | -- | T3:0.PRE - T999:1999 .ACC |
| B | B3:0/0 - B999:1999 /15 | -- | -- | B3:0 - B999:1999 | B3:0 - B999:1999 | -- | -- | -- | B3:0 - B999:1999 |
| S | S2:0/0 - S2:127/65 535 | -- | -- | S2:0 - S2:127 | S2:0 - S2:127 | -- | -- | -- | S2:0 - S2:127 |
| I | I1:0/0 - I999:255/1 5 | -- | -- | I1:0 - I999:255 | I1:0 - I999:255 | -- | -- | -- | I1:0 - I999:255 |
| O | O0:0/0 - O999:255/ 15 | -- | -- | O0:0 - O999:255 | O0:0 - O999:255 | -- | -- | -- | O0:0 - O999:255 |
| F | -- | -- | -- | -- | -- | F3:0 - F999:1999 | F3:0 - F999:1999 | F3:0 - F999:199 9 | F3:0 - F999:1999 |
| D | D3:0/0 - D999:199 9/15 | -- | -- | D3:0 - D999:199 9 | D3:0 - D999:199 9 | -- | -- | -- | D3:0 - D999:199 9 |
| A | A3:0/0 - A999:1999 /15 | A3:0 - A999:1999 | A3:0 - A999:1999 | A3:0 - A999:1999 | A3:0 - A999:1999 | A3:0 - A999:1999 | A3:0 - A999:1999 | A3:0 - A999:19 99 | A3:0 - A999:1999 |
| ST | ST3:0/0 - ST999:19 99/15 | ST3:0 - ST999:19 99 | ST3:0 - ST999:19 99 | ST3:0 - ST999:19 99 | ST3:0 - ST999:19 99 | ST3:0 - ST999:19 99 | ST3:0 - ST999:19 99 | ST3:0 - ST999:1 999 | ST3:0 - ST999:19 99 |

**PLC5**

| Address areas | Bool | SInt | USInt | Int | UInt | DInt | UDInt | Real | String |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | N3:0/0 - N999:199 9/15 | -- | -- | N3:0/0 - N999:199 9/15 | N3:0/0 - N999:199 9/15 | N3:0/0 - N999:199 9/15 | N3:0/0 - N999:199 9/15 | N3:0/0 - N999:199 9/15 | N3:0/0 - N999:199 9/15 |
| R | R3:0.EN - R999:199 9.ER - R999:199 9.DN - R999:199 9.FD - R999:199 9.IN - R999:199 9.EU - R999:199 9.EM - R999:199 9.UL | -- | -- | R3:0.LEN - R999:199 9.POS | R3:0.LEN - R999:199 9.POS | -- | -- | -- | R3:0.LEN - R999:199 9.POS |
| C | C3:0.DN - C999:199 9.CU - C999:199 9.CD - C999:199 9.OV - C999:199 9.UN | -- | -- | C3:0.PRE - C999:199 9.ACC | C3:0.PRE - C999:199 9.ACC | -- | -- | -- | C3:0.PRE - C999:199 9.ACC |
| T | T3:0.EN - T999:199 9.TT - T999:199 9.DN | -- | -- | T3:0.PRE - T999:199 9.ACC | T3:0.PRE - T999:199 9.ACC | -- | -- | -- | T3:0.PRE - T999:199 9.ACC |
| B | B3:0/0 - B999:199 9/15 | -- | -- | B3:0 - B999:199 9 | B3:0 - B999:199 9 | -- | -- | -- | B3:0 - B999:199 9 |
| S | S2:0/0 - S2:127/65 535 | -- | -- | S2:0 - S2:127 | S2:0 - S2:127 | -- | -- | -- | S2:0 - S2:127 |
| I | I1:0/0 - I999:277/1 7 | -- | -- | I1:0 - I999:277 | I1:0 - I999:277 | -- | -- | -- | I1:0 - I999:277 |
| O | O0:0/0 - O999:277/ 17 | -- | -- | O0:0 - O999:277 | O0:0 - O999:277 | -- | -- | -- | O0:0 - O999:277 |
| F | -- | -- | -- | -- | -- | F3:0 - F999:199 9 | F3:0 - F999:199 9 | F3:0 - F999:199 9 | F3:0 - F999:199 9 |
| D | D3:0/0 - D999:199 9/15 | -- | -- | D3:0/0 - D999:199 9/15 | D3:0/0 - D999:199 9/15 | -- | -- | -- | D3:0/0 - D999:199 9/15 |
| A | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 | A3:0/0 - A999:199 9/15 |
| ST | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 | ST3:0/0 - ST999:19 99/15 |

### Optimizing the configuration (Allen-Bradley EtherNet/IP) (RT Unified)

#### Acquisition cycle and update time

The acquisition cycles of the tags specified in the configuration software are decisive factors for the actual update times that can be achieved.

The update time is the sum of the acquisition cycle + transmission time + processing time.

To achieve optimum update times, remember the following points during configuration:

- Keep the individual data areas as small as possible and as large as necessary.
- If the acquisition cycles you select are too short, this is detrimental to the overall performance. Set the acquisition cycle to suit the rate of change of the process values. The rate of temperature changes of a furnace, for example, is significantly slower than the speed rate of an electrical drive. As a general guideline, the acquisition cycle should be approx. 1 second.
- Put the tags of an alarm or a screen in one data area without gaps.
- To allow changes in the PLC to be recognized reliably, these must be available at least during the actual acquisition cycle.

**Screens**

With screens, the update rate that can be achieved depends on the type and amount of data to be displayed.

In the interest of short update times during configuration, make sure that you configure short acquisition cycles only for objects which need to be updated quickly.

> **Note**
>
> Downloading of Unified Allen-Bradley Ethernet/IP panel project configured in V16 and Updates from TIA Portal V17 to Unified Comfort Panel (UCP) is not supported.
>
> Migrating Projects:
>
> To migrate projects from V16 and 16 updates to V17, perform the following:
>
> 1. Migrate the TIA portal V16 Allen-Bradley Ethernet/IP panel project to TIA Portal V17
> 2. Change the device version from V16.x.x.x to V17.0.0.0
> 3. Compile and download to Unified Comfort Panel having V17 Runtime (applicable in configuring V16 and V16 updates project)
> 4. Downloading of UCP project containing Allen-Bradley connection with device version V16.x.x.x configured in TIA portal V17 to Unified Comfort Panel (UCP) is not supported

### Commissioning components (communications modules) (RT Unified)

#### Transferring the PLC program to the PLC

1. Connect the PC to the PLC CPU using the appropriate cable.
2. Load the program files to the PLC CPU.
3. Then set the PLC CPU to RUN.

#### Transferring the project to the PC/Panel

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

### Security Information (RT Unified)

Use firewall If it is connected to the internet or use Allen-Bradley in a secured environment.

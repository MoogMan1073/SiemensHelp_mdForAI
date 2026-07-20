---
title: "Unified Mitsubishi MC TCP/IP (RT Unified)"
package: CSP4WCCUenUS
topics: 16
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Unified Mitsubishi MC TCP/IP (RT Unified)

This section contains information on the following topics:

- [Configuring a connection through Mitsubishi MC TCP/IP (RT Unified)](#configuring-a-connection-through-mitsubishi-mc-tcpip-rt-unified)
- [Parameters for the connection (Mitsubishi MC TCP/IP) (RT Unified)](#parameters-for-the-connection-mitsubishi-mc-tcpip-rt-unified)
- [Connecting HMI device to PLC (RT Unified)](#connecting-hmi-device-to-plc-rt-unified)
- [Parameterization of the communications modules (RT Unified)](#parameterization-of-the-communications-modules-rt-unified)
- [Performance features of communication (RT Unified)](#performance-features-of-communication-rt-unified)
- [Commissioning Components (RT Unified)](#commissioning-components-rt-unified)
- [Security Information (RT Unified)](#security-information-rt-unified)

## Configuring a connection through Mitsubishi MC TCP/IP (RT Unified)

### Introduction

You configure a connection to a PLC with a Mitsubishi MC TCPI/IP (Unified) communication driver in the "Connections" editor of the HMI device.

The Ethernet interfaces are named differently depending on the HMI device.

Example: PROFINET interface corresponds to the Ethernet interface.

### Requirements

- A project is open.
- An HMI device has been created.

### Procedure

1. Double-click on the HMI device under "Devices" in the project tree.
2. Double-click on the "Connections" item.
3. Double-click "<Add new>" in the "Connections" editor.
4. In the "Communication driver" column, select "Mitsubishi MC TCPI/IP" driver.

   ![Procedure](images/137886187659_DV_resource.Stream@PNG-en-US.png)
5. Select all necessary connection parameters for the interface in the Inspector window under "Parameters".

## Parameters for the connection (Mitsubishi MC TCP/IP) (RT Unified)

### Parameters to be set

To set the connection parameters, such as addresses and profiles, click the connection that you have created in the "Connections" editor.

The communication partners are displayed schematically in the Inspector window under "Parameters". The "HMI device" and "PLC" areas are available for assigning parameters according to the interface used.

### Parameters for the HMI device

You can select only one interface for the HMI device in the Inspector window under "Parameters". Depending on the HMI device, there are several interfaces available.

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

   "General > PROFINET interface > Ethernet addresses"

### Parameters for the PLC

- CPU type

  For "CPU type", you set the type of PLC to which the HMI device is connected.

  The following settings are possible:

  - FX3
  - Q

  If you select the FX3 CPU type, the Mitsubishi MC protocol "1E" is used and "3E" for the "Q" CPU type.

  The "Binary code" protocol variant is always used.

  > **Note**
  >
  > If the CPU type is changed for a configured connection, tags with the following properties must be revised:
  >
  > - Operands that do not exist for the new CPU type, such as "W", "B", "F".
  > - Inputs and outputs with different addressing (hexadecimal/octal)
  > - Addresses greater than the valid address area of the new CPU type
- IP address

  Set the IP address or host name of the Ethernet/IP module of the PLC. Only the IP address can be used on a Basic Panel.
- Port

  Set the port number of the module of the PLC.

## Connecting HMI device to PLC (RT Unified)

This section contains information on the following topics:

- [Connections through Mitsubishi MC TCP/IP (RT Unified)](#connections-through-mitsubishi-mc-tcpip-rt-unified)

### Connections through Mitsubishi MC TCP/IP (RT Unified)

#### Connection

The HMI device can be connected to the Mitsubishi PLC using the following components:

- Existing Ethernet network that also contains the PLCs.
- Cross-over Ethernet cable connected directly to the Ethernet interface of the CPU or the communication module.

The connection of the HMI device to a Mitsubishi PLC is limited primarily to the physical connection of the HMI device. Special blocks for the connection are not required in the PLC.

Connect the HMI device to one or several Q-series and/or FX3 PLCs. Connect the HMI device via the following interfaces:

- Communication interface OnBoard.
- Approved communication module suitable for the PLC.

> **Note**
>
> Downloading of Unified Mitsubishi TCP/IP panel project configured in V16 and Updates from TIA Portal V17 to Unified Comfort Panel (UCP) is not supported.
>
> Migrating Projects:
>
> To migrate projects from V16 and 16 updates to V17, perform the following:
>
> 1. Migrate the TIA portal V16 Unified Mitsubishi TCP/IP panel project to TIA Portal V17
> 2. Change the device version from V16.x.x.x to V17.0.0.0
> 3. Compile and download to Unified Comfort Panel having V17 Runtime (applicable in configuring V16 and V16 updates project)
> 4. Downloading of UCP project containing Mitsubishi MC TCP/IP connection with device version V16.x.x.x configured in TIA portal V17 to Unified Comfort Panel (UCP) is not supported

> **Note**
>
> A maximum of 16 connections are supported for communication drivers of 3-party PLCs. This number can be a combination or 16 individual communication drivers. The specification is only valid for Ethernet-based communication drivers and is additionally limited by the maximum possible number of connections at the respective PLC type.

## Parameterization of the communications modules (RT Unified)

This section contains information on the following topics:

- [FX3 PLCs (RT Unified)](#fx3-plcs-rt-unified)
- [Q PLCs (RT Unified)](#q-plcs-rt-unified)
- [Internal Ethernet port of the Q0xUDEH CPU (RT Unified)](#internal-ethernet-port-of-the-q0xudeh-cpu-rt-unified)

### FX3 PLCs (RT Unified)

#### Procedure

1. Start the FX-Configurator.
2. Select the module.
3. Assign the following settings in the "Operational settings" dialog:

   - Communication data code:

     Binary code
   - Initial timing:

     Always wait for OPEN
   - IP address:

     IP address
   - Send frame setting:

     Ethernet(V2.0)
   - TCP Existence confirmation setting:

     Use the Ping
4. Assign the following settings in the "Open Settings" dialog:

   - Protocol:

     TCP
   - Open system:

     Unpassive
   - Fixed buffer:

     Receive
   - Fixed buffer communication procedure:

     Procedure exist(MC)
   - Pairing open

     Disable
   - Existence confirmation

     No confirm
   - Host station Port No. (DEC)

     Port number

     > **Note**
     >
     > The port number chosen in the communication module must match the port number in WinCC. A connection with a port number must be assigned for each connected HMI device.
     >
     > You must specify port numbers in decimal values.
5. Confirm the default settings of the other dialog boxes.

The network number and station number parameters are not relevant for the connection and can be chosen as required.

### Q PLCs (RT Unified)

#### Procedure

1. Click "Edit network parameters".
2. Select the network type:

   - Ethernet

     The network number and the group / station number are not evaluated and can be freely assigned
3. Assign the following settings in the "Operational settings" dialog:

   - Communication data code:

     Binary code
   - Initial timing:

     Always wait for OPEN
   - IP address:

     IP address
   - Send frame setting:

     Ethernet(V2.0)
   - Enable write operations during RUN
4. Assign the following settings in the "Open settings" dialog:

   - Protocol:

     TCP
   - Open system:

     Unpassive
   - Pairing open

     Disable
   - Existence confirmation

     No confirm
   - Host station Port No. (HEX)

     Port-Nummer

     > **Note**
     >
     > The port number chosen in the communication module must match the port number in WinCC. A connection with a port number must be assigned for each connected HMI device.
     >
     > You must specify port numbers in hexadecimal values.

### Internal Ethernet port of the Q0xUDEH CPU (RT Unified)

#### Procedure

1. Assign the following settings in the "Internal Ethernet Port" dialog:

   - IP address:

     IP address
   - Communication data code:

     Binary code
   - Enable online changes
2. Assign the following settings in the "Open settings" dialog:

   - Protocol:

     TCP
   - Open system:

     MC-Protocol
   - Host station Port No. (HEX)

     Port number

     > **Note**
     >
     > The port number chosen in the communication module must match the port number in WinCC. A connection with a port number must be assigned for each connected HMI device.

## Performance features of communication (RT Unified)

This section contains information on the following topics:

- [Permitted data types for Mitsubishi MC TCP/IP (RT Unified)](#permitted-data-types-for-mitsubishi-mc-tcpip-rt-unified)
- [Supported CPU types for Mitsubishi MC TCP/IP (RT Unified)](#supported-cpu-types-for-mitsubishi-mc-tcpip-rt-unified)
- [Addresses for Mitsubishi MC TCP/IP (RT Unified)](#addresses-for-mitsubishi-mc-tcpip-rt-unified)
- [Address areas for Mitsubishi MC TCP/IP (RT Unified)](#address-areas-for-mitsubishi-mc-tcpip-rt-unified)

### Permitted data types for Mitsubishi MC TCP/IP (RT Unified)

#### Permitted data types

The table lists the data types that can be used when configuring tags.

| Data type | Operand type | Length |
| --- | --- | --- |
| 4-bit block | M, L, F, V, B, TS, TC, CS, CC, SB, DX, DY, SM, S, X, Y | 1 byte |
| 8-bit block | M, L, F, V, B, TS, TC, CS, CC, SB, DX, DY, SM, S, X, Y | 1 byte |
| 12-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 2 bytes |
| 16-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 2 bytes |
| 20-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 4 bytes |
| 24-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 4 bytes |
| 28-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 4 bytes |
| 32-bit block | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y | 4 bytes |
| Bool | M, L, F, V, B, TS, TC, CS, CC, SB, DX, DY, SM, S, X, Y | 1-bit |
| DInt | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 4 bytes |
| DWord | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 4 bytes |
| Int | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 2 bytes |
| Real<sup>1</sup> | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 4 bytes |
| String<sup>1</sup> | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 1 to 80 characters |
| Word | M, L, F, V, B, W, R, TS, TC, TN, CS, CC, CN, SB, SW, SM, SD, S, DX, DY, D, X, Y, Z | 2 bytes |

> **Note**
>
> **Known limitations are mentioned below:**
>
> - For Q-Series CPU, some of the operands (W, TN, SN, CN, SW, SD, D) for Bit Block data types and SS, SC operands for String data type are not supported.
> - For FX3 CPU type, some of the operands (D, TN, CN, R) for Bit Block data types and CN operand for Bool data type are not supported.
> - In FX3 Series CPU type, S operand is not supported for Int, DInt, Word, DWord, Real & String data types.
> - In Q Series CPU type, R operand is not supported for all data types.
> - Z operand will support address range from 0-19 only, this address range (of 0 to max 19 or less) is dependent on the given CPU type, and PLC configuration.

1. The "String" and "Real" data types are not available for all CPUs.
2. Operand types L, F, V, B, W, TC, SS, SC, SN, CC, SB, SW, SM, SD, DX, DY and Z are only available for CPU type "Q".

> **Note**
>
> Note the following for write accesses:
>
> Tags can only be written if "Enable online changes" or "Enable write operations during RUN" was selected when parameterizing the Mitsubishi communication modules.

### Supported CPU types for Mitsubishi MC TCP/IP (RT Unified)

#### CPU types

The following CPU types are supported for configuring the Mitsubishi MC TCP/IP (Unified) communication driver.

- FX3 series

  - FX 3G / FX 3G with communication module FX3U-ENET
  - FX 3U / FX 3U with communication module FX3U-ENET
  - FX 3UC / FX 3UC with communication module FX3U-ENET
- Q series

  - Q-Series with QJ71E71-100 communication module

### Addresses for Mitsubishi MC TCP/IP (RT Unified)

#### Address areas for connections through Mitsubishi MC TCP/IP (Unified)

The address area boundaries differ for the different series; refer to the Mitsubishi Computerlink manuals for this information.

Examples of address area boundaries dependent on the CPU and communication format:

| Name | Operand type | Max. address FX3 | Max. address Q-Series |
| --- | --- | --- | --- |
| Inputs | X | X 777 (Octal format) | X FFFF (HEX) |
| Outputs | Y | Y 777 (Octal format) | Y FFFF (HEX) |
| Auxiliary Relay | M | M 65535 | M 65535 |
| Counter Current Value | CN | CN 65535 | CN 65535 |
| Timer Current Value | TN | TN 65535 | TN 65535 |
| Data Registers | D | D 65535 | D 65535 |
| Link Registers | W | -- | W FFFF (HEX) |
| Latching Relay | L | -- | L 65535 |
| Annunciator | F | -- | F 65535 |
| Link Relay | B | -- | B FFFF (HEX) |
| Link Special Relay | SB | -- | SB FFFF (HEX) |
| Link Special Register | SW | -- | SW FFFF (HEX) |
| Counter Contact | CS | CS 65535 | CS 65535 |
| Counter Coil | CC | -- | CC 65535 |
| Timer Contact | TS | TS 65535 | TS 65535 |
| Timer Coil | TC | -- | TC 65535 |
| Special Relay | SM | -- | SM 65535 |
| Special Register | SD | -- | SD 65535 |
| Extension Register | R | R 65535 | R 65535 |
| Step Relay | S | S 65535 | S 65535 |
| Edge Relay | V | -- | V 65535 |
| Retentive Timer Contact | SS | -- | SS 65535 |
| Retentive Timer Coil | SC | -- | SC 65535 |
| Retentive Timer Current Value | SN | -- | SN 65535 |
| Input Relay Direct | DX | -- | DX FFFF (HEX) |
| Output Relay Direct | DY | -- | DY FFFF (HEX) |
| Index | Z | -- | Z 65535 |

### Address areas for Mitsubishi MC TCP/IP (RT Unified)

#### FX3

| Address areas | Data types |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bool | Int | Word | DInt | DWord | Real | String | 4-bit block | 8-bit block | 12-bit block | 16-bit block | 20-bit block | 24-bit block | 28-bit block | 32-bit block |  |
| D | -- | D0 -  D65535 | D0 -  D65535 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 | D0 -  D65535 | -- | -- | D0 -  D65535 | D0 -  D65535 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 |
| M | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 |
| CN | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 |
| TN | -- | TN0 -  TN65535 | TN0 -  TN65535 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65535 | -- | -- | TN0 -  TN65535 | TN0 -  TN65535 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 |
| R | -- | R0 -  R65535 | R0 -  R65535 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 | R0 -  R65535 | -- | -- | R0 -  R65535 | R0 -  R65535 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 |
| S | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 |
| CS | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 |
| TS | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65534 | TS0 -  TS65534 | TS0 -  TS65534 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | X0 -  X776 | X0 -  X776 | X0 -  X776 | X0 -  X776 |
| X | X0 -  X777 | X0 -  X777 | X0 -  X777 | X0 -  X776 | X0 -  X776 | X0 -  X776 | X0 -  X777 | X0 -  X774 | X0 -  X770 | X0 -  X764 | X0 -  X760 | X0 -  X754 | X0 -  X750 | X0 -  X744 | X0 -  X740 |
| Y | Y0 -  Y777 | Y0 -  Y777 | Y0 -  Y777 | Y0 -  Y776 | Y0 -  Y776 | Y0 -  Y776 | Y0 -  Y777 | Y0 -  Y774 | Y0 -  Y770 | Y0 -  Y764 | Y0 -  Y760 | Y0 -  Y754 | Y0 -  Y750 | Y0 -  Y744 | Y0 -  Y740 |

#### Q

| Address area | Data types |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bool | Int | Word | DInt | DWord | Real | String | 4-bit block | 8-bit block | 12-bit block | 16-bit block | 20-bit block | 24-bit block | 28-bit block | 32-bit block |  |
| B | B0 -  BFFFF | B0 -  BFFFF | B0 -  BFFFF | B0 -  BFFFE | B0 -  BFFFE | B0 -  BFFFE | B0 -  BFFFF | B0 -  BFFFC | B0 -  BFFF8 | B0 -  BFFF4 | B0 -  BFFF0 | B0 -  BFFEC | B0 -  BFFE8 | B0 -  BFFE4 | B0 -  BFFE0 |
| SB | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFE | SB0 -  SBFFFE | SB0 -  SBFFFE | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFF | SB0 -  SBFFFE | SB0 -  SBFFFE | SB0 -  SBFFFE | SB0 -  SBFFFE |
| CC | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65534 | CC0 -  CC65534 | CC0 -  CC65534 | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65535 | CC0 -  CC65534 | CC0 -  CC65534 | CC0 -  CC65534 | CC0 -  CC65534 |
| TC | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65534 | TC0 -  TC65534 | TC0 -  TC65534 | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65535 | TC0 -  TC65534 | TC0 -  TC65534 | TC0 -  TC65534 | TC0 -  TC65534 |
| D | -- | D0 -  D65535 | D0 -  D65535 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 | D0 -  D65535 | -- | -- | D0 -  D65535 | D0 -  D65535 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 | D0 -  D65534 |
| SD | -- | SD0 -  SD65535 | SD0 -  SD65535 | SD0 -  SD65534 | SD0 -  SD65534 | SD0 -  SD65534 | SD0 -  SD65535 | -- | -- | SD0 -  SD65535 | SD0 -  SD65535 | SD0 -  SD65534 | SD0 -  SD65534 | SD0 -  SD65534 | SD0 -  SD65534 |
| F | F0 -  F65535 | F0 -  F65535 | F0 -  F65535 | F0 -  F65534 | F0 -  F65534 | F0 -  F65534 | F0 -  F65535 | F0 -  F65535 | F0 -  F65535 | F0 -  F65535 | F0 -  F65535 | F0 -  F65534 | F0 -  F65534 | F0 -  F65534 | F0 -  F65534 |
| L | L0 -  L65535 | L0 -  L65535 | L0 -  L65535 | L0 -  L65534 | L0 -  L65534 | L0 -  L65534 | L0 -  L65535 | L0 -  L65535 | L0 -  L65535 | L0 -  L65535 | L0 -  L65535 | L0 -  L65534 | L0 -  L65534 | L0 -  L65534 | L0 -  L65534 |
| M | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65535 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 | M0 -  M65534 |
| SM | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65534 | SM0 -  SM65534 | SM0 -  SM65534 | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65535 | SM0 -  SM65534 | SM0 -  SM65534 | SM0 -  SM65534 | SM0 -  SM65534 |
| CN | -- | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65535 | -- | -- | CN0 -  CN65535 | CN0 -  CN65535 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 | CN0 -  CN65534 |
| TN | -- | TN0 -  TN65535 | TN0 -  TN65535 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65535 | -- | -- | TN0 -  TN65535 | TN0 -  TN65535 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 | TN0 -  TN65534 |
| R | -- | R0 -  R65535 | R0 -  R65535 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 | R0 -  R65535 | -- | -- | R0 -  R65535 | R0 -  R65535 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 | R0 -  R65534 |
| S | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65535 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 | S0 -  S65534 |
| CS | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65535 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 | CS0 -  CS65534 |
| TS | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65534 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65535 | TS0 -  TS65534 | TS0 -  TS65534 | TS0 -  TS65534 | TS0 -  TS65534 |
| V | V0 -  V65535 | V0 -  V65535 | V0 -  V65535 | V0 -  V65534 | V0 -  V65534 | V0 -  V65534 | V0 -  V65535 | V0 -  V65535 | V0 -  V65535 | V0 -  V65535 | V0 -  V65535 | V0 -  V65534 | V0 -  V65534 | V0 -  V65534 | V0 -  V65534 |
| W | -- | W0 -  WFFFF | W0 -  WFFFF | W0 -  WFFFE | W0 -  WFFFE | W0 -  WFFFE | W0 -  WFFFF | -- | -- | W0 -  WFFFF | W0 -  WFFFF | W0 -  WFFFE | W0 -  WFFFE | W0 -  WFFFE | W0 -  WFFFE |
| SW | -- | SW0 -  SWFFFF | SW0 -  SWFFFF | SW0 -  SWFFFE | SW0 -  SWFFFE | SW0 -  SWFFFE | SW0 -  SWFFFF | -- | -- | SW0 -  SWFFFF | SW0 -  SWFFFF | SW0 -  SWFFFE | SW0 -  SWFFFE | SW0 -  SWFFFE | SW0 -  SWFFFE |
| X | X0 -  XFFFF | X0 -  XFFFF | X0 -  XFFFF | X0 -  XFFFE | X0 -  XFFFE | X0 -  XFFFE | X0 -  XFFFF | X0 -  XFFFC | X0 -  XFFF8 | X0 -  XFFF4 | X0 -  XFFF0 | X0 -  XFFEC | X0 -  XFFE8 | X0 -  XFFE4 | X0 -  XFFE0 |
| DX | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFE | DX0 -  DXFFFE | DX0 -  DXFFFE | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFF | DX0 -  DXFFFE | DX0 -  DXFFFE | DX0 -  DXFFFE | DX0 -  DXFFFE |
| Y | Y0 -  YFFFF | Y0 -  YFFFF | Y0 -  YFFFF | Y0 -  YFFFE | Y0 -  YFFFE | Y0 -  YFFFE | Y0 -  YFFFF | Y0 -  YFFFC | Y0 -  YFFF8 | Y0 -  YFFF4 | Y0 -  YFFF0 | Y0 -  YFFEC | Y0 -  YFFE8 | Y0 -  YFFE4 | Y0 -  YFFE0 |
| DY | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFE | DY0 -  DYFFFE | DY0 -  DYFFFE | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFF | DY0 -  DYFFFE | DY0 -  DYFFFE | DY0 -  DYFFFE | DY0 -  DYFFFE |
| Z | -- | Z0 -  Z19 | Z0 -  Z19 | Z0 -  Z19 | Z0 -  Z19 | Z0 -  Z19 | Z0 -  Z19 | -- | -- | _ | _ | _ | _ | _ | _ |

## Commissioning Components (RT Unified)

### Transferring a project to the HMI device

1. Switch the HMI device to "transfer mode".
2. Set all necessary transfer parameters.

   - Interface
   - Transfer parameters
   - Target storage location
3. Start the project transfer.

   - The project is compiled automatically.
   - All compilation and transfer steps are logged to a message window.

### Interconnecting the PLC with the HMI device

1. Interconnect the PLC with the HMI device using a suitable cable.
2. The message "Connection to PLC .... is established" is output to the HMI device.

## Security Information (RT Unified)

Use firewall If it is connected to the internet or use Mitsubishi MC channel in a secured environment.

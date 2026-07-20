---
title: "Unified Standard Modbus RTU (RT Unified)"
package: CSP6WCCUenUS
topics: 12
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Unified Standard Modbus RTU (RT Unified)

This section contains information on the following topics:

- [Supported devices (RT Unified)](#supported-devices-rt-unified)
- [Communication with Standard Modbus RTU (RT Unified)](#communication-with-standard-modbus-rtu-rt-unified)
- [Communication through Standard Modbus RTU (RT Unified)](#communication-through-standard-modbus-rtu-rt-unified)

## Supported devices (RT Unified)

Unified Standard Modbus RTU supports the following:

- Unified Comfort

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

- Compact
- Quantum
- Momentum

## Communication with Standard Modbus RTU (RT Unified)

This section contains information on the following topics:

- [Communication between the HMI device and the PLC (RT Unified)](#communication-between-the-hmi-device-and-the-plc-rt-unified)

### Communication between the HMI device and the PLC (RT Unified)

#### Communications principle

The PLC and Unified Comfort communicate using tags.

**Tags**

The PLC and Unified Comfort use process values for data exchange. In your configuration, create tags that point to an address on the PLC. Unified Comfort reads and displays the value from the defined address. An entry made by an operator on Unified Comfort is written to the address on the PLC.

## Communication through Standard Modbus RTU (RT Unified)

This section contains information on the following topics:

- [Requirements for communication (Standard Modbus RTU) (RT Unified)](#requirements-for-communication-standard-modbus-rtu-rt-unified)
- [Configuring the controller type and protocol (Standard Modbus RTU) (RT Unified)](#configuring-the-controller-type-and-protocol-standard-modbus-rtu-rt-unified)
- [Configuring the protocol parameters (Standard Modbus RTU) (RT Unified)](#configuring-the-protocol-parameters-standard-modbus-rtu-rt-unified)
- [Permitted data types and operands (Standard Modbus RTU) (RT Unified)](#permitted-data-types-and-operands-standard-modbus-rtu-rt-unified)
- [Optimizing the configuration (Standard Modbus RTU) (RT Unified)](#optimizing-the-configuration-standard-modbus-rtu-rt-unified)
- [Commissioning components (communications modules) (RT Unified)](#commissioning-components-communications-modules-rt-unified)
- [Security Information (RT Unified)](#security-information-rt-unified)

### Requirements for communication (Standard Modbus RTU) (RT Unified)

#### Connection

Connect the HMI device to the Standard Modbus RTU interface of the Standard Modbus RTU slave.

The connection of the HMI device to PLC is limited primarily to the physical connection of the HMI device. Special blocks for the connection are not required in the PLC.

### Configuring the controller type and protocol (Standard Modbus RTU) (RT Unified)

#### Select the PLC

1. For a connection with a Modbus controller through the Standard Modbus RTU protocol, double-click "Connections" in the project window of the HMI device.
2. In the work area, select "Standard Modbus RTU" protocol in the "Communication driver" column.

   The Properties window displays the parameters of the selected protocol.

For subsequent changes of the parameters, double-click "Connections" in the project window of the HMI device. Select the connection and edit its parameters in the properties dialog box.

![Select the PLC](images/151961293451_DV_resource.Stream@PNG-en-US.png)

### Configuring the protocol parameters (Standard Modbus RTU) (RT Unified)

#### Parameters to be set

To set the parameters, double-click "Connections" in the project window of the HMI device. "Standard Modbus RTU" is selected in the "Communication drivers" column in the work area. You can now enter or modify the protocol parameters in the Properties window:

**Device-dependent parameters**

**HMI device parameters**

You can select an interface for the HMI device in the Inspector window under "Parameters". Depending on the HMI device, there are several interfaces available.

**Type**

Only RS 485 and RS 422 are system-tested.

- Baud rate

  For "Baud rate", select the transmission speed between the HMI device and Modicon PLC. A baud rate of 19200 or 9600 can be selected for the communication.

  A baud rate of 4800 can be selected for certain HMI devices.
- Data bits

  For "Data bits", only the value "8" can be selected.
- Parity

  For "Parity", you can choose from "None", "Even", and "Odd".
- Stop bits

  For "Stop bits", you can choose between 1 and 2 bits.

**PLC-dependent parameters**

- Slave address

  Under "Remote slave address", only when using a bridge, set the slave address for the remote PLC.  
  If no bridge is being used, the default value 255 (or 0) must remain.
- Change word order

  The "Change word order" parameter only modifies the word order for the representation of 32-bit values. The setting has an effect on the data types Double and Float. The byte sequence cannot be altered.

  - "Change word order" disabled

    For double words, the "Least Significant Word" is sent before the "Most Significant Word".

    This setting has been system-tested for all approved PLCs.
  - "Change word order" enabled

    For double words, the "Most Significant Word" is sent before the "Least Significant Word".
- Change bit order

  - "Change bit order" disabled

    The standard bit counting method (16 LSB - 1 MSB) used for the Modicon controllers will only be used for these CPUs in the "Tags" editor with selected data type "Bit". The following bit position assignment applies:

  |  | Left byte |  |  |  |  |  |  |  | Right byte |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | How the tags are counted | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

  - "Change bit order" enabled

    This bit counting method (0 LSB - 15 MSB) is only used for selected controllers (for example, the Premium and Micro series) in the "Tags" editor when any data type that supports 16 bits is selected. The following bit position assignment applies:

  | How the bit positions are counted | Left byte |  |  |  |  |  |  |  | Right byte |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | In the engineering system, you configure: | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

### Permitted data types and operands (Standard Modbus RTU) (RT Unified)

#### Permitted operands

The table lists the operands that can be used when configuring tags:

| Operand | Name |
| --- | --- |
| 0x | Coil  (discrete output) |
| 1x | Discrete Input |
| 3x | Input Register |
| 4x | Holding Register  (output) |
| 6x | Extended Memory (only available with "Quantum/Momentum" CPU) |

#### Permitted data types

The table lists the user data types with address range in engineering system:

| HMI Data Type | Operand | Address Range in Engineering System (ES)  (minimum and maximum values) |
| --- | --- | --- |
| Bit | 0x | 0x1 - 0x65535 |
| 1x | 1x100001 - 1x165535 |  |
| 3x | 3x300001 - 3x365535 |  |
| 4x | 4x400001 - 4x465535 |  |
| 6x | 6x60000 - 6x69999 |  |
| 16 Bit Group | 0x | 0x1 - 0x65520 |
| 1x | 1x100001 - 1x165520 |  |
| Int | 3x | 3x300001 - 3x365535 |
| 4x | 4x400001 - 4x465535 |  |
| 6x | 6x60000 - 6x69999 |  |
| +/- Int | 3x | 3x300001 - 3x365535 |
| 4x | 4x400001 - 4x465535 |  |
| 6x | 6x60000 - 6x69999 |  |
| Double | 4x | 4x400001 - 4x465534 |
| 6x | 6x60000 - 6x69998 |  |
| +/- Double | 4x | 4x400001 - 4x465534 |
| 6x | 6x60000 - 6x69998 |  |
| ASCII | 4x | 4x400001 - 4x465535 |
| 6x | 6x60000 - 6x69999 |  |
| Float | 4x | 4x400001 - 4x465534 |
| 6x | 6x60000 - 6x69998 |  |
| Array (Int, +/- Int, Double, +/- Double, Float) | 4x | Refer to the respective data type and operand |
| 6x | Refer to the respective data type and operand |  |

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | Note the following for write access: For data type "Bit" in the areas "4x" and "6x", the entire word is written back to the controller following a change to the specified bit. There is no check to determine whether any other bits in the word have changed. As a result, the PLC only has read access to the specified word. |

The standard bit counting method (16 LSB - 1 MSB) used for Modicon controllers will only be used for these CPUs in the "Tags" editor with selected data type "Bit". The following bit location assignment applies:

|  | Left byte |  |  |  |  |  |  |  | Right byte |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| How the tags are counted | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

**Format for "Signed"**

The placeholder "+/-" stands for the data types "Signed Int" and "Signed Double".

### Optimizing the configuration (Standard Modbus RTU) (RT Unified)

#### Acquisition cycle and update time

The acquisition cycles of the tags specified in the configuration software are decisive factors for the actual update times that can be achieved.

The update time is the sum of the acquisition cycle + transmission time + processing time.

To achieve optimum update times, remember the following points during configuration:

- Keep the individual data areas as small as possible and as large as necessary.
- Define data areas that belong together as belonging together. You can improve the update time by setting up one large data area instead of several small areas.
- If the acquisition cycles you select are too short, this is detrimental to the overall performance. Set the acquisition cycle to suit the rate of change of the process values. The rate of temperature changes of a furnace, for example, is significantly slower than the speed rate of an electrical drive. As a general guideline, the acquisition cycle should be approx. 1 second.
- Put the tags of an alarm or a screen in one data area without gaps.
- To allow changes in the PLC to be recognized reliably, these must be available at least during the actual acquisition cycle.

**Screens**

With screens, the update rate that can actually be achieved depends on the type and amount of data to be displayed.

In the interest of short update times during configuration, make sure that you configure short acquisition cycles only for objects which actually need to be updated quickly.

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

   - **To download to the Panel**: Enter the IP address of the panel.
5. Click "Connect". The connection to the device is established.
6. Click "Load" to download the project to the PC. The "Load preview" dialog box opens.  
   The project is compiled at the same time and the result is displayed simultaneously in the "Load preview" dialog box.
7. Check the displayed pre-settings and change them as necessary.
8. Click "Load".   
   After successful download, the project can be executed on the WebRH or the panel.  
   Please refer to the documentation for the HMI device used for more detailed information on transfer settings.

**Note**

Simulation view is not supported for Modbus RTU connections.

### Security Information (RT Unified)

Use firewall If it is connected to the internet or use Modbus channel in a secured environment.

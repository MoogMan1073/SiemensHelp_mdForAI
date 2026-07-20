---
title: "Communication with SIMATIC PLCs (RT Unified)"
package: CommSimaticWCCUenUS
topics: 47
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Communication with SIMATIC PLCs (RT Unified)

This section contains information on the following topics:

- [Communicating with SIMATIC S7-1200/1500 (RT Unified)](#communicating-with-simatic-s7-12001500-rt-unified)
- [Communicating with SIMATIC S7-300/400 (RT Unified)](#communicating-with-simatic-s7-300400-rt-unified)
- [Communicating with the SIMATIC S7-1500 Software Controller (RT Unified)](#communicating-with-the-simatic-s7-1500-software-controller-rt-unified)

## Communicating with SIMATIC S7-1200/1500 (RT Unified)

This section contains information on the following topics:

- [Communication with S7-1200/1500 (RT Unified)](#communication-with-s7-12001500-rt-unified)
- [Permitted data types for SIMATIC S7-1200/1500 (RT Unified)](#permitted-data-types-for-simatic-s7-12001500-rt-unified)
- [Symbolic addressing (RT Unified)](#symbolic-addressing-rt-unified)
- [Interface and communication parameters (RT Unified)](#interface-and-communication-parameters-rt-unified)
- [Reading and setting the operating state of an S7-1200/1500 (RT Unified)](#reading-and-setting-the-operating-state-of-an-s7-12001500-rt-unified)
- [Troubleshooting for SIMATIC S7-1200/1500 (RT Unified)](#troubleshooting-for-simatic-s7-12001500-rt-unified)

### Communication with S7-1200/1500 (RT Unified)

#### Overview

You can configure the following communication channel for communication between an HMI device and the SIMATIC S7-1200/1500 PLC.

- PROFINET

---

**See also**

[Permitted data types for SIMATIC S7-1200/1500 (RT Unified)](#permitted-data-types-for-simatic-s7-12001500-rt-unified)
  
[Symbolic addressing (RT Unified)](#symbolic-addressing-rt-unified)

### Permitted data types for SIMATIC S7-1200/1500 (RT Unified)

#### Permitted data types for connections with SIMATIC S7-1500

The table below lists the data types that can be used when configuring tags.

| Data type | Length |
| --- | --- |
| BOOL | 1 bit |
| BYTE | 1 byte |
| CHAR | 1 byte |
| DATE | 2 bytes |
| DATE_AND_TIME | 8 bytes |
| DINT | 4 bytes |
| DTL | 12 bytes |
| DWORD | 4 bytes |
| INT | 2 bytes |
| LDT | 8 bytes  The value range of the data type LDT of an S7-1500 stretches from 1970-1-1 00:00:00.000000000 to 2262-04-11 23:47:16.854775807. |
| LINT | 8 bytes |
| LREAL | 8 bytes |
| LTIME | 8 bytes |
| LTIME_OF_DAY | 8 bytes |
| REAL | 4 bytes |
| S5TIME | 2 bytes |
| SINT | 1 byte |
| STRING | (2+n) bytes, n = 0 to 254 |
| TIME | 4 bytes |
| TIME_OF_DAY | 4 bytes |
| UDINT | 4 bytes |
| UINT | 2 bytes |
| ULINT | 8 bytes |
| USINT | 1 byte |
| WCHAR | 2 bytes |
| WORD | 2 bytes |
| WSTRING | (2+n) 2 bytes, n = 0 to 254 |

---

**See also**

[Communication with S7-1200/1500 (RT Unified)](#communication-with-s7-12001500-rt-unified)
  
[Symbolic addressing (RT Unified)](#symbolic-addressing-rt-unified)

### Symbolic addressing (RT Unified)

#### Introduction

Data are exchanged between the HMI device and the PLC via tags.

Depending on the addressed data blocks, these tags are addressed as absolute or symbolic in the PLC.

- Symbolic addressing

  For symbolic addressing, a validity check of the tag connection is performed in runtime. If an address is changed in the PLC, the change is registered and an error message is issued.

  For symbolic addressing, select the PLC tag via its name and connect it to an external HMI tag. The valid data type for the external HMI tag is automatically selected by the system.
- Absolute addressing

  The linking of tags is not checked in runtime. You select the valid data type of the tags. If the tag address changes in the PLC, compile and load the HMI device again so that the change is registered in Runtime.

#### Data blocks and symbolic access

Data blocks with optimized access support only symbolic addressing.

During the symbolic addressing of a data block, the address of an element in the data block is dynamically assigned and is automatically adopted in the HMI tag in the event of a change.

Neither the connected data block nor the WinCC project must be compiled.

For symbolic addressing of elements in a data block, you need to recompile and reload the WinCC project only in case of the following changes:

- Name or data type of the connected data block element or of the global PLC tag
- Name or data type of a higher-level structure node of the connected element in the data block element or global PLC tag
- Number of the connected data block

#### HMI connections and symbolic access

With symbolic addressing of tags, you create an integrated HMI connection:

- Integrated connection

  You address the tags symbolically as well as absolutely over an integrated connection.
- Non-integrated connection

  You address the tags only absolutely over a non-integrated connection.

  A non-integrated connection is available for all supported PLCs.

#### Disabling symbolic access

In WinCC, symbolic addressing is the default method.

To change the default setting, follow these steps:

1. Select "Options > Settings > Visualization > HMI tags" in the menu.
2. Activate the "Symbolic access" option.

---

**See also**

[Communication with S7-1200/1500 (RT Unified)](#communication-with-s7-12001500-rt-unified)
  
[Permitted data types for SIMATIC S7-1200/1500 (RT Unified)](#permitted-data-types-for-simatic-s7-12001500-rt-unified)

### Interface and communication parameters (RT Unified)

This section contains information on the following topics:

- [S7-1500 | Integrated HMI connection (RT Unified)](#s7-1500-integrated-hmi-connection-rt-unified)
- [S7-1500 | Non-integrated HMI connection (RT Unified)](#s7-1500-non-integrated-hmi-connection-rt-unified)

#### S7-1500 | Integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [PROFINET interface parameters (RT Unified)](#profinet-interface-parameters-rt-unified)

##### PROFINET interface parameters (RT Unified)

The following table shows the interface parameters of an integrated HMI connection:

PROFINET parameters of the HMI device

| Parameters | Description |
| --- | --- |
| Subnet | Specifies the subnet of the HMI connection via which the HMI device is connected to the network. |
| MAC address | Specifies the MAC address for the connection type "ISO connection".   This option is only available when the "Use ISO protocol" option is selected. |
| IP address | Specifies the IP address of the communication partner.   This property is only available when the "Set IP address in the project" option is selected. |
| Subnet mask | Specifies the subnet mask.  This property is only available when the "Set IP address in the project" option is selected.   The subnet mask determines which part of the IP address addresses the network and which part of the IP address addresses the device. |
| Router address | Specifies the router address.  This property is only available when the "Use router" option is selected. |

PROFINET parameters of the PLC

| Parameters | Description |
| --- | --- |
| Subnet | Specifies the subnet of the HMI connection via which the HMI device is connected to the network. |
| IP address | Specifies the IP address of the communication partner.  This property is only available when the "Set IP address in the project" option is selected. |
| Subnet mask | Specifies the subnet mask.  This property is only available when the "Set IP address in the project" option is selected.   The subnet mask determines which part of the IP address addresses the network and which part of the IP address addresses the device. |
| Router address | Specifies the router address.  This property is only available when the "Use router" option is selected. |
| PROFINET device name | Shows the PROFINET device name or specifies it.  This property is only available when the "Generate PROFINET device name automatically" option is deactivated. |
| Converted name | Shows the name that is automatically generated from the PROFINET device name and satisfies the DNS conventions. |
| Device number | Shows the device number by which an IO device can be identified. |

#### S7-1500 | Non-integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [PROFINET interface parameters (RT Unified)](#profinet-interface-parameters-rt-unified-1)

##### PROFINET interface parameters (RT Unified)

The following table shows the interface parameters of a non-integrated HMI connection:

PROFINET parameters of the HMI device

| Parameters | Description |
| --- | --- |
| Interface | Specifies the communication channel. |
| Address | Specifies the IP address of the device. |
| Access point | Defines a logical device name through which the communication partner can be reached. |

PROFINET parameters of the PLC

| Parameters | Description |
| --- | --- |
| Address | Specifies the IP address of the device. |

### Reading and setting the operating state of an S7-1200/1500 (RT Unified)

The operating state of an S7-1200/1500 can be read and set via the system tags "@ConnectionName_PLC_OpState" and "@ConnectionName_PLC_OpStateCtrl".

The system tags are automatically available when a connection to an S7-1200/1500 PLC is configured.

> **Note**
>
> The tags are available as of version 18.0.0.2. If the version of a device is changed to an older version, these tags are no longer available.

If the connection is removed or the connection type is changed, the tags are removed.

You cannot change or delete the tags.

If the name of the connection is changed, the tag name changes accordingly.

These tags are not counted.

> **Note**
>
> **Length of the tag name**
>
> A tag name may contain a maximum of 128 characters. If the tag name contains more than 128 characters, the name of the connection is shortened to be able to integrate it into the tag name.
>
> If the name of the system tags created after shortening the connection name conflicts with an existing name, a new tag is created with the additional suffix, e.g. (1), (2).
>
> Assign short connection names so that shortening the connection name is not necessary to reach the maximum length of the tag name of less than 128 characters.

#### Reading the operating state of an S7-1200/1500

1. Read the value of the "@ConnectionName_PLC_OpState" tag.

| State | Value |
| --- | --- |
| STOP | 4 |
| START UP | 6 |
| RUN | 8 |
| HOLD | 10 |

#### Setting the operating state of an S7-1200/1500

1. Set the value of tag "@ConnectionName_PLC_OpStateCtrl" according to the desired state of the PLC.

| State | Value |
| --- | --- |
| STOP | 4 |
| RUN | 8 |

### Troubleshooting for SIMATIC S7-1200/1500 (RT Unified)

This section contains information on the following topics:

- [Causes of a faulty connection (RT Unified)](#causes-of-a-faulty-connection-rt-unified)
- [Procedure if there is no connection (RT Unified)](#procedure-if-there-is-no-connection-rt-unified)
- [Error messages SIMATIC S7-1200/1500 (RT Unified)](#error-messages-simatic-s7-12001500-rt-unified)

#### Causes of a faulty connection (RT Unified)

##### Causes for a connection not getting established

If communication between the PLC and the HMI device cannot be established, the causes could be the following:

- Integrated connection not configured
- Hardware fault: Cable not plugged in, PLC switched off, network component interrupted
- Connection is not online
- Erroneous network configuration, for example. wrong access point, Invalid IP address of a device
- Failed authentication on the PLC side (wrong or invalid password)
- Wrong or invalid connection certificate
- A connection that has already been established is broken as a result of a system function call.
- Connection resources exhausted

##### Connection not online

The connection can be set to not 'Online' In the Engineering System. In this case, connection establishment does not take place.

##### Breaking and switching the connection with a system function

A connection can be broken, established and switched by calling a system function in a script.

- "SetConnectionMode": The specified connection is established or disconnected.
- "ChangeConnection": Changes the connection parameters of an HMI connection.

  Is used to switch between PLCs at runtime.

  When "SwitchConnection" (ChangeConnection) is used, the current connection to the PLC is disconnected and an attempt is made to establish a connection to another PLC. Connection establishment to the other PLC can be rejected or the connection may later be lost.

#### Procedure if there is no connection (RT Unified)

The connection is established at the start of Runtime.

If a connection cannot be established, Runtime issues a system alarm.

##### Requirement

Configure a screen with a screen object "Alarm view" that is shown on the HMI device in Runtime.

The system alarm for a failed connection establishment is displayed here.

> **Note**
>
> If a connection is configured as not "online" or is not established by calling a system function, a system alarm is not issued. This is not an error; it is configured behavior.

The system alarm provides information on the cause of the faulty connection establishment.

##### Finding the cause of the error

1. Check the cable and the plug-in connections.
2. Check whether the connection has been configured as "online".

   ![Finding the cause of the error](images/159958183819_DV_resource.Stream@PNG-en-US.png)
3. Check whether a script has called the system functions "SetConnectionMode" (SetConnectionMode) or "SwitchConnection" (ChangeConnection).

   More information: [Setting up switch on/switch off of a connection in runtime](Basics%20%28RT%20Unified%29.md#setting-up-switch-onswitch-off-of-a-connection-in-runtime-rt-unified)
4. Check the network configuration.

   IP addresses within a subnet must be unique.

   ![Finding the cause of the error](images/160040365835_DV_resource.Stream@PNG-en-US.png)

   If required, select the function "Find connection path" to assign the optimum connection path to the connection.
5. Check the availability and validity period of the certificate in the TIA Portal.

   The alarm text contains the name of a lapsed certificate.

   More information: AUTOHOTSPOT

   Connection establishment is not possible with PLCs that do not provide a certificate.
6. The password given for the PLC in "Device configuration > Properties > General > Access protection" must match the password that is specified for the connection.

#### Error messages SIMATIC S7-1200/1500 (RT Unified)

The following alarms are output if the connection cannot be established:

| ID | Cause |
| --- | --- |
| 536870948 | The connection to the PLC could not be established. |
| 537526273 | The connection to an S7-1200/1500 PLC could not be established. |
| 537526274 | The S7-1200/1500 PLC is not in RUN mode. |
| 537526275 | The runtime settings of the WinCC Unified Device for controller alarms are configured for "Automatic Update", but the PLC S7-1200/1500 PLC does not support full text alarms. |
| 537526276 | The S7-1200/1500 PLC communication resources for HMI tags are overloaded. |

You can find the configured alarm texts under [HMI device] > "HMI alarms > System events".

More information: [Reference to system events](Configuring%20alarms%20%28RT%20Unified%29.md#reference-rt-unified).

The following alarms can be displayed for certificates.

| ID | Cause |
| --- | --- |
| 536870941 | The certificate was not found in the certificate memory. |
| 536870942 | Certificate expires soon. |
| 536870943 | Certificate has expired. |

The alarms specify the relevant device, the name of the certificate and if applicable, the date.

## Communicating with SIMATIC S7-300/400 (RT Unified)

This section contains information on the following topics:

- [Communication with SIMATIC S7-300/400 (RT Unified)](#communication-with-simatic-s7-300400-rt-unified)
- [Permissible data types for SIMATIC S7-300/400 (RT Unified)](#permissible-data-types-for-simatic-s7-300400-rt-unified)
- [Interface and communication parameters (RT Unified)](#interface-and-communication-parameters-rt-unified-1)
- [Configuring a connection via "Named connections" (RT Unified)](#configuring-a-connection-via-named-connections-rt-unified)
- [Cyclic operation (RT Unified)](#cyclic-operation-rt-unified)
- [Troubleshooting for SIMATIC S7-300/400 (RT Unified)](#troubleshooting-for-simatic-s7-300400-rt-unified)

### Communication with SIMATIC S7-300/400 (RT Unified)

#### Introduction

The combined designation for the PLCs S7-300 and S7-400 is SIMATIC S7-300/400.

You can configure the following communication channel for communication between an HMI device and the SIMATIC S7-300/400 PLC:

- PROFINET

---

**See also**

[Permissible data types for SIMATIC S7-300/400 (RT Unified)](#permissible-data-types-for-simatic-s7-300400-rt-unified)
  
[Cyclic operation (RT Unified)](#cyclic-operation-rt-unified)

### Permissible data types for SIMATIC S7-300/400 (RT Unified)

#### Permitted data types for connections with SIMATIC S7-300/400

The table lists the data types that can be used when configuring tags.

| Data type | Length |
| --- | --- |
| BOOL | 1 bit |
| BYTE | 1 byte |
| CHAR | 1 byte |
| DATE | 2 bytes |
| DATE_AND_TIME | 8 bytes |
| DINT | 4 bytes |
| DWORD | 4 bytes |
| INT | 2 bytes |
| REAL | 4 bytes |
| S5TIME | 2 bytes |
| STRING | (2+n) bytes, n = 0 to 254  - With SIMATIC S7-300:    - Read access: 220 characters   - Write access: 210 characters - ASCII - Characters from the Windows 1252 code page |
| TIME | 4 bytes |
| TIME_OF_DAY, TOD | 4 bytes |
| WORD | 2 bytes |

---

**See also**

[Communication with SIMATIC S7-300/400 (RT Unified)](#communication-with-simatic-s7-300400-rt-unified)
  
[Cyclic operation (RT Unified)](#cyclic-operation-rt-unified)

### Interface and communication parameters (RT Unified)

This section contains information on the following topics:

- [S7-300/400 | Integrated HMI connection (RT Unified)](#s7-300400-integrated-hmi-connection-rt-unified)
- [S7-300/400 | Non-integrated HMI connection (RT Unified)](#s7-300400-non-integrated-hmi-connection-rt-unified)

#### S7-300/400 | Integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [PROFINET interface parameters (RT Unified)](#profinet-interface-parameters-rt-unified-2)

##### PROFINET interface parameters (RT Unified)

The following table shows the interface parameters of an integrated HMI connection:

PROFINET parameters of the HMI device

| Parameters | Description |
| --- | --- |
| Subnet | Specifies the subnet of the HMI connection via which the HMI device is connected to the network. |
| MAC address | Specifies the MAC address for the connection type "ISO connection".   This option is only available when the "Use ISO protocol" option is selected. |
| IP address | Specifies the IP address of the communication partner.  This property is only available when the "Set IP address in the project" option is selected. |
| Subnet mask | Specifies the subnet mask.  This property is only available when the "Set IP address in the project" option is selected.   The subnet mask determines which part of the IP address addresses the network and which part of the IP address addresses the device. |
| Router address | Specifies the router address.  This property is only available when the "Use router" option is selected. |

PROFINET parameters of the PLC

| Parameters | Description |
| --- | --- |
| Subnet | Specifies the subnet of the HMI connection via which the HMI device is connected to the network. |
| IP address | Specifies the IP address of the communication partner.   This property is only available when the "Set IP address in the project" option is selected. |
| Subnet mask | Specifies the subnet mask.  This property is only available when the "Set IP address in the project" option is selected.   The subnet mask determines which part of the IP address addresses the network and which part of the IP address addresses the device. |
| Router address | Specifies the router address.  This property is only available when the "Use router" option is selected. |
| PROFINET device name | Shows the PROFINET device name or specifies it.  This property is only available when the "Generate PROFINET device name automatically" option is deactivated. |
| Converted name | Shows the name that is automatically generated from the PROFINET device name and satisfies the DNS conventions. |
| Device number | Shows the device number by which an IO device can be identified. |

#### S7-300/400 | Non-integrated HMI connection (RT Unified)

This section contains information on the following topics:

- [PROFINET interface parameters (RT Unified)](#profinet-interface-parameters-rt-unified-3)

##### PROFINET interface parameters (RT Unified)

The following table shows the interface parameters of a non-integrated HMI connection:

PROFINET parameters of the HMI device

| Parameters | Description |
| --- | --- |
| Interface | Specifies the communication channel. |
| Address | Specifies the IP address of the device. |
| Access point | Specifies the device name through which the  communication partner can be reached. |

PROFINET parameters of the PLC

| Parameters | Description |
| --- | --- |
| Address | Specifies the IP address of the device. |
| Expansion slot | Specifies the number of the expansion slot of the PLC to be addressed. |
| Rack | Specifies the rack number of the PLC to be addressed. |
| Cyclic operation | Enables/disables cyclic operation. |

### Configuring a connection via "Named connections" (RT Unified)

#### Introduction

For setting up a logical connection, one of the symbolic connection names listed in the "Connection name" field is assigned to a selected application name.

The symbolic connection names and application names are configured in STEP 7.

NAMED CONNECTIONS can only be configured for integrated connections.

> **Note**
>
> With routed HMI connections between WinCC RT Unified and the S7-300/400 PLCs, the use of "Named Connection" is mandatory, independent of the router.

#### Requirements

A "Named connection" has been created in STEP 7.

The following communication partners are configured in the "Devices & Networks" editor:

- SIMATIC PC with WinCC RT Professional
- SIMATIC S7-300/400

#### Procedure

1. Double-click the "Devices & Networks" item in the project tree.

   The available communication partners in the project are displayed in the network view.
2. Click on the HMI device in the "Network view".
3. Select the entry "S7RTM is installed" in the Inspector window under "Parameters > XDB configuration".

   ![Procedure](images/160543378315_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/160543378315_DV_resource.Stream@PNG-en-US.png)

   If you have not installed S7RTM, select "Generate XDB file". Then select the path in which the XDB file will be stored.
4. Click the "Connections" button and select "HMI connection" for the connection type.
5. Click the PROFINET interface of the PLC and drag and drop a connection to the PROFINET interface of the PC.
6. Click the connecting line.
7. Click "Highlight HMI connection" and select the HMI connection.

   The connection is displayed graphically in the Inspector window.
8. Select the "NAMED CONNECTION" interface in the Inspector window under "Properties > General > Connection path > Interface" of WinCC RT Professional.

**Note**

The application and connection name can also be entered manually, for e.g. if an XDB file does not exist for the symbolic connection name or if the project is to be transferred to another computer. It is necessary to check the correct writing of the name in STEP 7 because there is no name validation in CS mode.

### Cyclic operation (RT Unified)

This section contains information on the following topics:

- [Basics of cyclic operation (RT Unified)](#basics-of-cyclic-operation-rt-unified)
- [Configuring cyclic operation (RT Unified)](#configuring-cyclic-operation-rt-unified)

#### Basics of cyclic operation (RT Unified)

##### Operating principle of cyclic operation

When the "Cyclic operation" option is enabled, the HMI device sends a telegram to the PLC at the beginning of communication indicating that certain tags are required on a recurring basis.

The PLC then always transmits the data at the same cyclic interval. This saves the HMI device from having to output new requests for the data.

When cyclic operation is disabled, the HMI device sends a request whenever information is required.

##### Advantages and properties of cyclic operation

The list below shows the advantages and properties of "Cyclic operation" option:

- Cyclic operation reduces the data transmission load at the HMI device. The PLC resources are used to reduce the load on the HMI device.
- The PLC only supports a certain number of cyclic services. The HMI device handles the operation if the PLC cannot provide any further resources for cyclic services.
- The HMI device generates the cycle if the PLC does not support cyclic operation.
- Screen tags are not integrated into cyclic operation.
- Cyclic operation is only set up at the restart of Runtime.
- The HMI device transfers several jobs to the PLC if cyclic operation is enabled, depending on the PLC.
- The HMI device only transfers one job at a time to the PLC if cyclic operation is disabled.

---

**See also**

[Configuring cyclic operation (RT Unified)](#configuring-cyclic-operation-rt-unified)

#### Configuring cyclic operation (RT Unified)

##### Introduction

You configure cyclic operation for an HMI connection at an HMI connection in the "Connections" editor of the HMI device.

##### Requirement

- The devices and networks are configured.
- An HMI connection is created in the "Connections" editor.

##### Procedure

To enable an HMI connection for cyclic operation, follow these steps:

1. Double-click "Connections" in the project tree below your HMI device.

   The "Connections" editor opens.
2. Select the desired HMI connection.

   The parameters of the connection are displayed in the graphic overview.
3. Activate "PLC > Cyclic operation".

##### Result

The PLC then always transmits the required data at the same cyclic interval.

---

**See also**

[Basics of cyclic operation (RT Unified)](#basics-of-cyclic-operation-rt-unified)

### Troubleshooting for SIMATIC S7-300/400 (RT Unified)

This section contains information on the following topics:

- [Causes of a faulty connection (RT Unified)](#causes-of-a-faulty-connection-rt-unified-1)
- [Procedure if there is no connection (RT Unified)](#procedure-if-there-is-no-connection-rt-unified-1)
- [SIMATIC S7-300/400 error messages (RT Unified)](#simatic-s7-300400-error-messages-rt-unified)

#### Causes of a faulty connection (RT Unified)

##### Causes for a connection not getting established

If communication between the PLC and the HMI device cannot be established, the causes could be the following:

- Integrated connection not configured
- Hardware fault: Cable not plugged in, PLC switched off, network component interrupted
- Connection is not online
- Fault network configuration, for example, invalid IP address of a device
- Failed authentication on the PLC side (wrong or invalid password)
- A connection that has already been established is broken as a result of a system function call.
- Connection resources exhausted

##### Connection not online

The connection can be set to not 'Online' In the Engineering System. In this case, connection establishment does not take place.

##### Breaking and switching the connection with a system function

A connection can be broken, established and switched by calling a system function in a script.

- "SetConnectionMode": The specified connection is established or disconnected.
- "ChangeConnection": Changes the connection parameters of an HMI connection.

  Is used to switch between PLCs at runtime.

  When "SwitchConnection" (ChangeConnection) is used, the current connection to the PLC is disconnected and an attempt is made to establish a connection to another PLC. Connection establishment to the other PLC can be rejected or the connection may later be lost.

#### Procedure if there is no connection (RT Unified)

The connection is established at the start of Runtime.

If a connection cannot be established, Runtime issues a system alarm.

##### Requirement

Configure a screen with a screen object "Alarm view" that is shown on the HMI device in Runtime.

The system alarm for a failed connection establishment is displayed here.

> **Note**
>
> If a connection is configured as not "online" or is not established by calling a system function, a system alarm is not issued. This is not an error; it is configured behavior.

The system alarm provides information on the cause of the faulty connection establishment.

##### Finding the cause of the error

1. Check the cable and the plug-in connections.
2. Check whether the connection has been configured as "online".

   ![Finding the cause of the error](images/160079804299_DV_resource.Stream@PNG-en-US.png)
3. Check whether a script has called the system functions "SetConnectionMode" (SetConnectionMode) or "SwitchConnection" (ChangeConnection).

   More information: [Setting up switch on/switch off of a connection in runtime](Basics%20%28RT%20Unified%29.md#setting-up-switch-onswitch-off-of-a-connection-in-runtime-rt-unified)
4. Check the network configuration.

   IP addresses within a subnet must be unique.

   ![Finding the cause of the error](images/160079814411_DV_resource.Stream@PNG-en-US.png)

   If required, select the function "Find connection path" to assign the optimum connection path to the connection.
5. The password given for the PLC in "Device configuration > Properties > General > Protection" must match the password that is specified for the connection.

#### SIMATIC S7-300/400 error messages (RT Unified)

The following alarms are output if the connection cannot be established:

| ID | Cause |
| --- | --- |
| 536870948 | The connection to the PLC could not be established. |
| 537526273 | The connection to a S7-300/400 PLC could not be established. |
| 537526274 | The S7-300/400 PLC is not in the RUN mode. |
| 537526275 | The runtime settings of the WinCC Unified Device for controller alarms are configured for "Automatic Update" but the PLC S7-300/400 PLC does not support full text alarms. |
| 537526276 | The communication resources of the S7-300/400 PLC for HMI tags are overloaded. |

You can find the configured alarm texts under [HMI device] > "HMI alarms > System events".

More information: [Reference to system events](Configuring%20alarms%20%28RT%20Unified%29.md#reference-rt-unified).

## Communicating with the SIMATIC S7-1500 Software Controller (RT Unified)

This section contains information on the following topics:

- [Communication with SIMATIC S7-1500 Software Controller (RT Unified)](#communication-with-simatic-s7-1500-software-controller-rt-unified)
- [Communication via PROFINET (RT Unified)](#communication-via-profinet-rt-unified)

### Communication with SIMATIC S7-1500 Software Controller (RT Unified)

#### Introduction

This section describes the communication between a SIMATIC S7-1500 Software Controller V30.0 and HMI devices as well as other PLCs via the PROFINET communication channel.

Connections are configured over the Windows-based network or through a virtual network provided together with the Software Controller. A combination of both is possible.

You can configure connections to a SIMATIC S7-1500 Software Controller in the "Devices & Networks" editor.

### Communication via PROFINET (RT Unified)

This section contains information on the following topics:

- [Basics of HMI connections to an SIMATIC S7-1500 Software Controller (RT Unified)](#basics-of-hmi-connections-to-an-simatic-s7-1500-software-controller-rt-unified)
- [Configuring an HMI connection (RT Unified)](#configuring-an-hmi-connection-rt-unified)
- [PROFINET parameters (RT Unified)](#profinet-parameters-rt-unified)

#### Basics of HMI connections to an SIMATIC S7-1500 Software Controller (RT Unified)

##### Introduction

The SIMATIC S7-1500 Software Controller V30.0 supports direct and routed connections.

You can find more information on networking with a SIMATIC S7-1500 Software Controller in the documentation for the SIMATIC S7-1500 Sofware Controller.

You have the following options:

- [Configuring an internal HMI connection](#configuring-an-internal-hmi-connection-rt-unified)
- [Configuring internal connection and connection to external PLCs](#configuring-internal-connection-and-connection-to-external-plcs-rt-unified)
- [Configuring a connection with an external routed PLC](#configuring-a-connection-with-an-external-routed-plc-rt-unified)
- [Configuring connections to external PLCs in different subnets](#configuring-connections-to-external-plcs-in-different-subnets-rt-unified)

The options described can be used together in a project.

##### Access point (Access point)

The access point S7ONLINE is created during the installation of the Software Controllers. STEP7 requires this access point in order to be able to perform online functionality.

An access point represents an interface on the target system. Applications access this access point. The linked interface can be a physical interface of the computer (e.g. x1, x2 for a PC system), or an internal virtual interface (e.g. the "Rt VMM Network Adapter").

Access points that are configured in the engineering system must be configured in exactly the same way on the target system of Runtime.

#### Configuring an HMI connection (RT Unified)

This section contains information on the following topics:

- [Configuring an internal HMI connection (RT Unified)](#configuring-an-internal-hmi-connection-rt-unified)
- [Configuring internal connection and connection to external PLCs (RT Unified)](#configuring-internal-connection-and-connection-to-external-plcs-rt-unified)
- [Configuring a connection with an external routed PLC (RT Unified)](#configuring-a-connection-with-an-external-routed-plc-rt-unified)
- [Configuring connections to external PLCs in different subnets (RT Unified)](#configuring-connections-to-external-plcs-in-different-subnets-rt-unified)

##### Configuring an internal HMI connection (RT Unified)

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Communication via Ethernet**  In Ethernet-based communication, the end user is responsible for the security of his data network.   Targeted attacks can overload the device and interfere with proper functioning. |  |

You configure the internal connection if the Software Controller and Runtime are installed on a PC.

###### Requirements

The following communication partners are created in the "Devices & Networks" editor:

- PC system with WinCC Unified Runtime
- SIMATIC S7-1500 Software Controller on PC system with PROFINET interface.

###### Procedure

1. Open the network view in the "Devices & Networks" editor.
2. Drag and drop Runtime of the PC system onto the Software Controller.

   ![Procedure](images/164271085323_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164271085323_DV_resource.Stream@PNG-de-DE.png)
3. Switch to "Connections" mode.
4. Select the "HMI connection" connection type.

   The devices available for connection are highlighted in color.
5. To create an integrated HMI connection between Runtime and Software Controller, drag and drop the Runtime onto the CPU.

   ![Procedure](images/164272117899_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164272117899_DV_resource.Stream@PNG-de-DE.png)

   The properties of the HMI connection are displayed in the Inspector window.
6. Under "Local" (WinCC Unified PC Runtime), the "Vmm Network Adapter" is created as the interface.

   ![Procedure](images/164422689547_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164422689547_DV_resource.Stream@PNG-en-US.png)

   The "Vmm Network Adapter" is the interface to the virtual network that is provided with the Software Controller.
7. Under "Partner" ("Software Controller"), select "Runtime communication interface" as the interface.

   An integrated HMI connection with the access point S7ONLINE is created.

   ![Procedure](images/164272587275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164272587275_DV_resource.Stream@PNG-de-DE.png)
8. On the PC on which Runtime is running, configure the PG/PC interface in the Microsoft Windows Control Panel by assigning the RT-VMM network adapter to the S7ONLINE access point.

   ![Procedure](images/164422700555_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164422700555_DV_resource.Stream@PNG-de-DE.png)

**Note**

The created HMI connection is also shown in the tabular area of the editor on the "Connections" tab. Check the connection parameters in the table.

You can change the local name for the connection only in the table.

###### Result

You have created a connection between an HMI device and a SIMATIC S7-1500 Software Controller. The IP address and subnet mask connection parameters are configured.

##### Configuring internal connection and connection to external PLCs (RT Unified)

To exchange data between an external PLC and WinCC Unified Runtime, configure a connection via the S7ONLINE access point.

###### Requirement

You have created an integrated HMI connection between a Software Controller and WinCC Unified Runtime.

The procedure is described here: [Configuring an internal HMI connection](#configuring-an-internal-hmi-connection-rt-unified).

###### Procedure (Windows network)

1. Assign "None, or a different Windows setting" to the interface on the PC system.

   ![Procedure (Windows network)](images/164423694731_DV_resource.Stream@PNG-en-US.png)

   ![Procedure (Windows network)](images/164423694731_DV_resource.Stream@PNG-en-US.png)
2. Select "Network" in the editor.
3. Create a connection between the PC system and the PLC.
4. Select "Connections" and "HMI connection" in the editor.
5. Create an integrated HMI connection to the external PLC by dragging and dropping Runtime onto the PLC.

   ![Procedure (Windows network)](images/164327676427_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure (Windows network)](images/164327676427_DV_resource.Stream@PNG-de-DE.png)

   The connection is assigned the S7ONLINE1 access point.

   If additional connections are created, the suffix of the access point S7ONLINE is incremented.

###### Procedure (virtual network)

1. Assign "Software PLC_x" to the interface on the PC system.

   ![Procedure (virtual network)](images/164425420683_DV_resource.Stream@PNG-en-US.png)

   ![Procedure (virtual network)](images/164425420683_DV_resource.Stream@PNG-en-US.png)
2. Select "Network" in the editor.
3. Create a connection between the PC system and the PLC.
4. Select "Connections" and "HMI connection" in the editor.
5. Configure an integrated HMI connection to the external PLC by dragging and dropping Runtime onto the PLC.
6. Select "Add routed S7 connection".

   ![Procedure (virtual network)](images/164426237835_DV_resource.Stream@PNG-en-US.png)

   ![Procedure (virtual network)](images/164426237835_DV_resource.Stream@PNG-en-US.png)

   The "Rt Vmm Network Adapter" is assigned to Runtime as the interface.

   ![Procedure (virtual network)](images/164426875787_DV_resource.Stream@PNG-en-US.png)

   ![Procedure (virtual network)](images/164426875787_DV_resource.Stream@PNG-en-US.png)

   The connection is assigned the S7ONLINEx access point.

**Note**

Connections through the virtual network of the Software Controllers are always routed connections.

##### Configuring a connection with an external routed PLC (RT Unified)

Communication can be configured between the Software Controller and a routed PLC.

###### Requirements

The following communication partners are created in the "Devices & Networks" editor:

- HMI device with PROFINET or Ethernet interface
- SIMATIC S7-1500 Software Controller on PC system with PROFINET interface.
- An internal connection is configured between the Software Controller and Runtime.

  The procedure is described here: [Configuring an internal HMI connection](#configuring-an-internal-hmi-connection-rt-unified).

###### Procedure

1. Create the PLCs in the "Devices & Networks" editor.

   The devices must support routing.
2. Create a connection between the routing PLC and the routed PLC.

   ![Procedure](images/164354850955_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164354850955_DV_resource.Stream@PNG-de-DE.png)
3. Create an integrated HMI connection between Runtime and the routed PLC.

   - Select "Connections" and "HMI connection" in the editor.
   - Drag and drop Runtime onto the PLC.

   ![Procedure](images/164361817355_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164361817355_DV_resource.Stream@PNG-de-DE.png)
4. Select "Add routed S7 connection".

   ![Procedure](images/164362859019_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164362859019_DV_resource.Stream@PNG-de-DE.png)

###### Result

Communication between the devices is possible via integrated connections.

![Result](images/164365184395_DV_resource.Stream@PNG-de-DE.png)

###### Advanced options

In this scenario you can also integrate multiple PLCs in separate subnets.

For more information, refer to the section: [Configuring connections to external PLCs in different subnets](#configuring-connections-to-external-plcs-in-different-subnets-rt-unified).

##### Configuring connections to external PLCs in different subnets (RT Unified)

Communication can be configured between the Software Controller and multiple PLCs via different subnets.

###### Requirements

The following communication partners are created in the "Devices & Networks" editor:

- HMI device with PROFINET or Ethernet interface
- SIMATIC S7-1500 Software Controller on PC system with PROFINET interface.
- An internal connection is configured between the Software Controller and Runtime.

  The procedure is described here: [Configuring an internal HMI connection](#configuring-an-internal-hmi-connection-rt-unified).

###### Procedure

1. Create the PLCs in the "Devices & Networks" editor.
2. Create the connections between the PC system and the PLCs.
3. Create integrated HMI connections between Runtime and the PLCs by dragging and dropping Runtime onto the respective PLC.

   ![Procedure](images/164365756811_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/164365756811_DV_resource.Stream@PNG-de-DE.png)
4. Edit the IP addresses of the interfaces.

###### Advanced options

You can also integrate routed PLCs into this scenario.

For more information, refer to the section: [Configuring a connection with an external routed PLC](#configuring-a-connection-with-an-external-routed-plc-rt-unified).

#### PROFINET parameters (RT Unified)

This section contains information on the following topics:

- [PROFINET parameters for the HMI connection (RT Unified)](#profinet-parameters-for-the-hmi-connection-rt-unified)
- [PROFINET parameters for the HMI device (RT Unified)](#profinet-parameters-for-the-hmi-device-rt-unified)
- [PROFINET parameters for the PLC (RT Unified)](#profinet-parameters-for-the-plc-rt-unified)
- [Protection of communication (RT Unified)](#protection-of-communication-rt-unified)

##### PROFINET parameters for the HMI connection (RT Unified)

###### PROFINET parameters for the HMI connection

An overview of the configured HMI connection parameters can be found in the properties for the HMI connection.

Only limited changes are possible in this Inspector window.

###### Displaying and changing the HMI connection parameters

1. Click the HMI connection in the "Devices & Networks" editor.
2. Change the parameters of the HMI connection in the Inspector window under "Properties > General > General".

   ![Displaying and changing the HMI connection parameters](images/70061866123_DV_resource.Stream@PNG-en-US.png)

###### "Connection"

Shows the name of the HMI connection.

###### "Connection path"

The communication partners of the selected HMI connection and the associated PROFINET parameters are displayed in the "Connection path" area. Some of the areas displayed cannot be edited in this dialog.

- "End point"

  Displays the device name. This area cannot be edited.
- "Interface"

  Displays the selected interface of the device. You can choose between several interfaces, depending on the device.
- "Interface type"

  Displays the selected interface type. This area cannot be edited.
- "Subnet"

  Displays the selected subnet. This area cannot be edited.
- "Address"

  Displays the selected IP address of the device. This area cannot be edited.
- "Find connection path" button

  Enables the subsequent specification of connections.

##### PROFINET parameters for the HMI device (RT Unified)

###### PROFINET parameters for the HMI device

An overview of the configured HMI device parameters can be found in the properties for the HMI device.

###### Displaying and changing PROFINET parameters of the HMI device

1. Click the HMI device in the "Devices & Networks" editor.
2. Change the parameters of the HMI device in the Inspector window under "Properties > General".

   ![Displaying and changing PROFINET parameters of the HMI device](images/67214999563_DV_resource.Stream@PNG-en-US.png)

###### "Interface networked with"

In the "Interface networked with" area, select the subnet of the HMI connection via which the HMI device is connected to the network. You use the "Add new subnet" button to create a new subnet.

###### "IP protocol"

- "Set IP address in the project"

  When you transfer the WinCC project to the HMI device, this IP address is set up directly in the HMI device.

  > **Note**
  >
  > The device is automatically restarted in the case of HMI devices with the Windows CE 3.0 operating system.
  >
  > HMI devices with Windows CE 3.0:
  >
  > - Mobile Panel 177 PN
  > - Mobile Panel 177 DP
- "Subnet mask"

  You assign data of the subnet mask in the "Subnet mask" area.
- "Use IP router"

  If you are using an IP router, select "Use IP router" and enter the router address in the "Router address" field.
- "IP address is set directly at the device"

  If the function "Set IP address using a different method" is activated, the IP address is not taken from the project. You have to enter the IP address directly in the Control Panel of the HMI device.

##### PROFINET parameters for the PLC (RT Unified)

###### PROFINET parameters for the PLC

An overview of the configured parameters can be found in the properties for the PLC.

###### Displaying and changing PROFINET parameters of the PLC

1. Click the PLC in the "Devices & Networks" editor.
2. Change the parameters of the PLC in the Inspector window under "Properties > General > General".

   ![Displaying and changing PROFINET parameters of the PLC](images/70061907339_DV_resource.Stream@PNG-en-US.png)

###### "Interface networked with"

In the "Subnet" area, select the subnet of the HMI connection via which the PLC is connected to the network. You use the "Add new subnet" button to create a new subnet.

###### "IP protocol"

- "Interface type"

  Depending on the HMI device type, you have various interfaces to choose from.
- "IP address"

  You assign the IP address of the HMI device in the "IP address" area.
- "Subnet mask"

  You assign data of the subnet mask in the "Subnet mask" area.

  If you are using an IP router, select "Use IP router" and enter the router address in the field.

##### Protection of communication (RT Unified)

This section contains information on the following topics:

- [Security levels (RT Unified)](#security-levels-rt-unified)
- [Access password for the HMI connection (RT Unified)](#access-password-for-the-hmi-connection-rt-unified)

###### Security levels (RT Unified)

If you want to protect the PLC and HMI device communication, you can assign protection levels for the communication.

For an SIMATIC S7-1500 Software Controller, you can enter multiple passwords to set up different access rights for different user groups.

The passwords are entered in a table, so that exactly one protection level is assigned to each password.

The effect of the password is given in the "Protection" column.

###### Example

You select the "Complete protection" protection level for a standard CPU (i.e., not an F-CPU) when configuring it.

Afterwards, you enter a separate password for every protection level above it in the table.

For users who do not know any of the passwords, the CPU is completely protected. Not even HMI access is possible.

For users who know one of the assigned passwords, the effect depends on the table row in which the password occurs:

- The password in row 1 (no protection) allows access as if the CPU were completely unprotected. Users who know this password have unrestricted access to the CPU.
- The password in row 2 (write protection) allows access as if the CPU were write-protected. Despite knowing the password, users who know this password only have read access to the CPU.
- The password in row 3 (read and write protection) allows access as if the CPU were read-protected and write-protected, so that only HMI access is possible for users who know this password.

###### Access password for the HMI connection (RT Unified)

###### Introduction

Communication with a PLC with the"Complete protection" protection level is protected by a password. The password is stored in the properties of the PLC.

Enter the password from the PLC in the "Access password" area.

Communication to the PLC is denied if an incorrect password or no password is entered.

###### Entering the access password

Enter the access password for the HMI connection in the "Connections" editor.

![Entering the access password](images/122130390667_DV_resource.Stream@PNG-en-US.png)

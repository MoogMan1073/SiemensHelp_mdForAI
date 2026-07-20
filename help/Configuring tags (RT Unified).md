---
title: "Configuring tags (RT Unified)"
package: TagsWCCUenUS
topics: 77
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring tags (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring tags (RT Unified)](#configuring-tags-rt-unified-1)
- [Configuring user data types (RT Unified)](#configuring-user-data-types-rt-unified)
- [Logging tags (RT Unified)](#logging-tags-rt-unified)
- [Displaying tags (RT Unified)](#displaying-tags-rt-unified)
- [Reference (RT Unified)](#reference-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Basics of tags (RT Unified)](#basics-of-tags-rt-unified)
- [Overview of HMI tag tables (RT Unified)](#overview-of-hmi-tag-tables-rt-unified)
- [Internal tags (RT Unified)](#internal-tags-rt-unified)
- [External tags (RT Unified)](#external-tags-rt-unified)
- [Addressing external tags (RT Unified)](#addressing-external-tags-rt-unified)
- [Indirect addressing (RT Unified)](#indirect-addressing-rt-unified)
- [Address multiplexing (RT Unified)](#address-multiplexing-rt-unified)
- [System tags (RT Unified)](#system-tags-rt-unified)
- [Basics on arrays (RT Unified)](#basics-on-arrays-rt-unified)
- [Updating the tag value in runtime (RT Unified)](#updating-the-tag-value-in-runtime-rt-unified)
- [Limits and start values of a tag (RT Unified)](#limits-and-start-values-of-a-tag-rt-unified)
- [Data logging (RT Unified)](#data-logging-rt-unified)
- [Basics of tag management (RT Unified)](#basics-of-tag-management-rt-unified)
- [Basics of user data types (RT Unified)](#basics-of-user-data-types-rt-unified)
- [Export and import of tags (RT Unified)](#export-and-import-of-tags-rt-unified)

### Basics of tags (RT Unified)

#### Introduction

Process values are forwarded in runtime using tags. Process values are data which is stored in the memory of one of the connected automation systems. They represent the status of a plant in the form of temperatures, fill levels or switching states, for example. Define external tags for processing the process values in WinCC.

WinCC works with two types of tag:

- External tags
- Internal tags

The external tags form the link between WinCC and the automation systems. The values of external tags correspond to the process values from the memory of an automation system. The value of an external tag is determined by reading the process value from the memory of the automation system. It is also possible to rewrite a process value in the memory of the automation system.

Internal tags do not have a process link and only convey values within the WinCC. The tag values are only available as long as runtime is running.

In WinCC, you can visualize and change process values, which are transferred using tags, on your HMI device.

![Introduction](images/102714666635_DV_resource.Stream@PNG-en-US.png)

#### Tags in WinCC

For external tags, the properties of the tag are used to define the connection that the WinCC uses to communicate with the automation system and form of data exchange.

Tags that are not supplied with values by the process - the internal tags - are not connected to the automation system. In the tag's "Connection" property, this is identified by the "Internal tag" entry.

You can create tags in different tag tables for greater clarity. You then directly access the individual tag tables in the "HMI tags" node in the project tree. The tags from all tag tables can be displayed with the help of the table "Show all tags".

With structures you bundle a number of different tags that form one logical unit. Structures are project-associated data and are available for all HMI devices of the project. You use the "Types" editor in the project library to create and edit a structure.

#### Composition of the number of tags

The number of tags used is displayed differently in different places in WinCC.

| Symbol | Meaning |
| --- | --- |
| Default tag table | - In the HMI device: All configured external, internal tags and the system tags. - In the PLC: All configured PLC tags and the system constants. |
| User-defined tag tables | - In the HMI device: All configured external and internal tags in the tag table. - In the PLC: All PLC tags configured in the tag table. |
| Compile | When compiling an HMI device, the following information about tags is provided in the Inspector window:  - Number of tags: Addition of all configured, external and internal tags and their subelements from user data types or arrays.   Example: Two external tags of a user data type with five elements and one internal tag of the type "array" with ten elements: 2 + 2*5 + 1 + 1*10 = 23 - Tags used: The configured, external and internal tags or their elements that have a use in the HMI device. |
| PowerTags | The number of PowerTags of an HMI device in "Settings &gt; General &gt; Information" results from the elements of the lowest level of all configure external tags in the HMI device.  Example: Two external tags of a user data type with five elements: 2*5 = 10 |

---

**See also**

[Overview of HMI tag tables (RT Unified)](#overview-of-hmi-tag-tables-rt-unified)
  
[External tags (RT Unified)](#external-tags-rt-unified)
  
[Internal tags (RT Unified)](#internal-tags-rt-unified)
  
[Resources Monitor (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#resources-monitor-rt-unified)

### Overview of HMI tag tables (RT Unified)

#### Introduction

HMI tag tables contain the definitions of the HMI tags that apply across all devices. A tag table is created automatically for each HMI device created in the project.

In the project tree there is an "HMI tags" folder for each HMI device. The following tables can be contained in this folder:

- Default tag table
- User-defined tag tables
- Table of all tags

In the project tree you can create additional tag tables in the "HMI tags" folder and use these to sort and group tags and constants. You can move tags to a different tag table using a drag-and-drop operation or with the help of the "Tag table" field. Activate the "Tags table" field using the shortcut menu of the column headings.

In WinCC you can display the locations of use for all tags. Use the "Cross-references" command in the shortcut menu or the F11 key to call the "Cross-references" editor for a selected tag table. In the editor you can see all objects that the respective tag uses and you can jump directly to the location of use of the tag.

#### Default tag table

There is one default tag table for each HMI device of the project. It cannot be deleted or moved. The default tag table contains HMI tags and, depending on the HMI device, also system tags. You can declare all HMI tags in the standard tag table or, as necessary, in additional user-defined tag tables.

#### User-defined tag tables

You can create multiple user-defined tag tables for each HMI device in order to group tags according to your requirements. You can rename, gather into groups, or delete user-defined tag tables. To group tag tables, create additional subfolders in the HMI tags folder.

#### Show all tags

The "HMI tags" tab in the "All tags" table shows an overview of all HMI tags and system tags of the HMI device in question. This table cannot be deleted, renamed or moved. The "Tags table" column shows you in which tag table a tag is included. Using the "Tags table" field, the assignment of a tag to a tags table can be changed.

The "All tags" table contains an additional tab "System tags". The system tags are created by the system and used for internal management of the project. The names of the system tags begin with the "@" character. System tags cannot be deleted or renamed. You can evaluate the value of a system tag, but cannot modify it.

#### Discrete alarms, analog alarms and logging tags

The following tables are also available in an HMI tag table:

- Discrete alarms

  In the "Discrete alarms" table, you configure discrete alarms to the HMI tag selected in the HMI tag table. When you configure a discrete alarm, multiple selection in the HMI tag table is not possible. You configure the discrete alarms for each HMI tag separately.
- Analog alarms

  In the "Analog alarms" table, you configure analog alarms to the HMI tag selected in the HMI tag table. When you configure an analog alarm, multiple selection in the HMI tag table is not possible. You configure the analog alarms for each HMI tag separately.
- Logging tags

  In the "Logging tags" table, you configure logging tags to the HMI tag selected in the HMI tag table. When you configure a logging tag, multiple selection in the HMI tag table is not possible. You configure the logging tags for each HMI tag separately.

With the help of these tables you configure alarms and logging tags for the currently selected HMI tag.

### Internal tags (RT Unified)

#### Introduction

Internal tags do not have any connection to the PLC.

#### Principle

Internal tags are stored in the memory of the HMI device. Therefore, only this HMI device has read and write access to the internal tags. You can create internal tags to perform local calculations, for example.

You can use the HMI data types for internal tags. Availability depends on the HMI device being used.

The following HMI data types are available:

| HMI data type | Data format |
| --- | --- |
| Bool | Binary tag |
| Byte | Unsigned 8-bit value |
| DateTime | Date/time format |
| DInt | Signed 32-bit value |
| DWord | Unsigned 32-bit value |
| Int | Signed 16-bit value |
| LInt | Signed 32-bit value |
| LReal | Floating-point number 64-bit IEEE 754 |
| LTime | Signed duration |
| LWord | Unsigned 64-bit value |
| Real | Floating-point number 32-bit IEEE 754 |
| SInt | Signed 8-bit value |
| UDInt | Unsigned 32-bit value |
| UInt | Unsigned 16-bit value |
| ULInt | Unsigned 64-bit value |
| USInt | Unsigned 8-bit value |
| WChar | Text tag, 16-bit character set |
| Word | Unsigned 16-bit value |
| WString | Text tag, 16-bit character set |
| Array | Data structure |

---

**See also**

[System tags (RT Unified)](#system-tags-rt-unified)

### External tags (RT Unified)

#### Introduction

External tags allow the data exchange between the components of an automation system, for example, between an HMI device and a PLC.

An external tag is the image of a defined memory location in the PLC. You have read and write access to this storage location from both the HMI device and from the PLC.

As external tags map a storage location in the PLC, the applicable data types depend on the PLC that is connected to the HMI device.

If you write a PLC control program in STEP 7, the PLC tags created in the control program will be added to the PLC tag table. If you want to connect an external tag to a PLC tag, access the PLC tags directly via the PLC tag table and connect them to the external tag.

#### Data types

All simple data types available on the connected PLC are available at an external tag in WinCC. If the data type of the PLC tag is not available in WinCC, a compatible data type is automatically used at the HMI tag. Interconnected PLC data types and arrays are not supported.

If you use PLC data types, the data type is adopted by WinCC. You can change the data type at the HMI tag, if necessary.

#### Central tag management in STEP 7

You can connect also connect DB instances of user-defined PLC data types (UDT) to the HMI tags.

The PLC data type and the corresponding DB instances are created and updated centrally in STEP 7. In WinCC, you can use the following sources as the PLC tag (DB instances):

- Data block elements that use a UDT as data type
- Data block instances of a UDT

The data type is taken from STEP 7 and is not converted to an HMI data type. The access type is always "Symbolic access". Depending on the release for WinCC in STEP 7, elements and structured elements of the PLC data type are applied to WinCC.

> **Note**
>
> **Accessing PLC data types**
>
> Access to PLC data types is only available in conjunction with SIMATIC S7-1500.

#### Synchronization with PLC tags

A variety of options for synchronizing external tags with the PLC tags are available in the runtime settings under "Settings for tags".

When you perform synchronization, you have the option of automatically applying the tag names of the PLC to external tags and reconnecting the existing tags.

The generated tag name is derived from the position of the data value in the hierarchical structure of the data block.

#### Update of tag values

For external tags, the current tag values are transmitted in runtime via the communication connection between WinCC and the connected automation systems and then saved in the runtime memory. Next, the tag value will be updated to the set cycle time. For use in the runtime project, WinCC accesses tag values in the runtime memory that were read from the PLC at the previous cycle time. As a result, the value in the PLC can already change while the value from the runtime memory is being processed.

---

**See also**

[Creating external tags (RT Unified)](#creating-external-tags-rt-unified)

### Addressing external tags (RT Unified)

#### Introduction

The options for addressing external tags depend on the type of connection between WinCC and the PLC in question. A distinction must be made between the following connection types:

- Integrated connection  
  Connections of devices which are within a project and were created with the "Devices &amp; Networks" editor are referred to as integrated connections.
- Non-integrated connection  
  Connections of devices which were created with the "Connections" editor are referred to as non-integrated connections. It is not necessary that all of the devices be within a single project.

The connection type can also be recognized by its icon.

| Symbol | Meaning |
| --- | --- |
| ![Introduction](images/23072055691_DV_resource.Stream@PNG-de-DE.png) | Integrated connection |
| ![Introduction](images/23081203083_DV_resource.Stream@PNG-de-DE.png) | Non-integrated connection |

#### Addressing with integrated connections

An integrated connection offers the advantage that you can address a tag both symbolically and absolutely.

For symbolic addressing, you select the PLC tag via its name and connect it to the HMI tag. The valid data type for the HMI tag is automatically selected by the system.

During the symbolic addressing of a data block with optimized access and standard access, the address of an element in the data block is dynamically assigned and is automatically adopted in the HMI tag in the event of a change. You do not need to compile the connected data block or the WinCC project for this step.  
For data blocks with optimized access, only symbolic addressing is available.

For symbolic addressing of elements in a data block, you only need to recompile and reload the WinCC project in case of the following changes:

- If the name or the data type of the linked data block element or global PLC tag has changed.
- If the name or the data type of the higher level structure node of a linked element in the data block element or global PLC tag has changed.
- If the name of the connected data block has changed.

Symbolic addressing is currently available with the following PLCs:

- SIMATIC S7-1500
- SIMATIC ET 200 CPU
- SIMATIC S7-1500 software controller

Symbolic addressing is also available if you have an integrated link.

You can also use absolute addressing with an integrated connection. You have to use absolute addressing for PLC tags from a SIMATIC S7-300/400 PLC. If you have connected an HMI tag with a PLC tag and the address of the PLC tag changes, you only have to recompile the control program to update the new address in WinCC. Then you recompile the WinCC project and load it onto the HMI device.

In WinCC, symbolic addressing is the default method. To change the default setting, select the menu command "Options &gt; Settings &gt; Visualization &gt; HMI tags".

The availability of an integrated connection depends on the PLC used. The following table shows the availability:

| Controller | Integrated connection | Comments |
| --- | --- | --- |
| S7-300/400 | Yes | The linking of tags is not checked in runtime. If the tag address changes in the PLC and the HMI device is not compiled again and loaded, the change is not registered in runtime. |
| S7-1500 | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |
| SIMATIC ET 200 CPU | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |
| SIMATIC S7-1500 software controller | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |

Create an integrated connection in the "Devices &amp; Networks" editor. If the PLC is contained in the project and integrated connections are supported, you can then also have the connection created automatically. To do this, when configuring the HMI tag, simply select an existing PLC tag to which you want to connect the HMI tag. The integrated connection is then automatically created by the system.

#### Addressing with non-integrated connections

In the case of a project with a non-integrated connection, you always configure a tag connection with absolute addressing. Select the valid data type yourself. If the address of a PLC tag changes in a project with a non-integrated connection during the course of the project, you also have to make the change in WinCC. The tag connection cannot be checked for validity in runtime, an error message is not issued.

A non-integrated connection is available for all supported PLCs.

Symbolic addressing is not available in a non-integrated connection.

With a non-integrated connection, the control program does not need to be part of the WinCC project. You can perform the configuration of the PLC and the WinCC project independently of each other. For configuration in WinCC, only the addresses used in the PLC and their function have to be known.

### Indirect addressing (RT Unified)

#### Introduction

With indirect addressing, the process value of the tag used on an screen object is not determined until runtime. In WinCC Unified Runtime, you use an HMI tag of type "WString" for indirect addressing. You also need HMI tags whose values are to be displayed in Runtime. In Runtime you enter the name of the tag in the string tag whose value you want to display and process.

#### Restrictions

The following restrictions exist for indirect addressing:

- Indirect addressing can only be used for the process value at a screen object, e.g. IO field.
- HMI tags for indirect addressing are of the data type "WString".
- Indirect addressing can be used to access internal or external HMI tags that are configured on the same HMI device.

#### Application example

The operator enters the name of one of several machines in an IO field. Depending on the input of the operator, a process value of the machine is displayed in another IO field.

To configure such a scenario, configure the string tag with activation of indirect addressing for an I/O field. Use this I/O field to output the values. Configure the same tag to another IO field without activation of indirect addressing. Use this I/O field to enter the machine names. Also configure a series of tags whose values you want to output.

When the operator enters the name of a different machine, the value of the string tag for indirect addressing changes. The output field shows the content of the tag whose name is included in the string tag.

You can use other mechanisms in WinCC to supply the string tag for indirect addressing, for example, a script.

---

**See also**

[Addressing tags indirectly (RT Unified)](#addressing-tags-indirectly-rt-unified)

### Address multiplexing (RT Unified)

#### Introduction

With address multiplexing you can address a large number of memory locations in the address range of the PLC with a single tag. You read and write to the addresses without defining a tag for each individual address.

#### Multiplexing with absolute addressing

When using multiplexing with absolute addressing, you configure tags as placeholders for the address in the PLC to be addressed.

If you want to access, for example, an address of the format "%DBx.DBWy", the expression for multiplexing is as follows:

"%DB[HMITag1].DBW[HMITag2]"

In Runtime, you supply the HMI tag "HMITag1" with the required value for the data block you want to address.

In Runtime, you supply the HMI tag "HMITag2" with the required address from the data block.

HMI tags are supplied with values, for example, with the help of values from the PLC, IO fields, or via a script.

Absolute address multiplexing is possible with all elementary data types.

Absolute address multiplexing is not possible with arrays or structured data types.

Multiplexing with absolute addresses is supported for the following PLCs and communications drivers.

- SIMATIC S7-300/400
- SIMATIC S7-1200
- SIMATIC S7-1500

#### Multiplexing with symbolic addressing

When multiplexing with symbolic addressing you access different array elements of an array tag in a data block of the connected PLC by means of a multiplex tag and an index tag.

If you want to access, for example, the various elements of the array tag "Arraytag_1" in the data block "Datablock_1", the expression for symbolic addressing is as follows:

"Datablock_1.Arraytag_1[HMITag_1]"

You control the access to the index of the array elements with the HMI tag "HMITag_1". In Runtime, you supply the tag with the index of the array element that you want to access.

Multiplexing with symbolic addressing is only available if the following components support symbolic addressing:

- HMI device
- PLC
- Communication driver

Symbolic addressing is supported by the following communication drivers:

- SIMATIC S7-1200
- SIMATIC S7-1500

Structured tags with PLC user data types as well as arrays can also be used for multiplexing with symbolic addressing.

Multiplexing is possible under the following conditions:

- The path of the connected PLC tag includes at least one array index.
- The array, which is left in the path of the PLC tags, is one-dimensional.
- If there are multiple arrays in the path of the PLC tags, only the array at the far left is available for multiplexing.
- The index tag must be of the "USInt", "UInt", "UDInt", "SInt", "Int" or "DInt" data type.

The following figure shows multiplexing with symbolic addressing using a structured HMI tag with user-defined PLC user data types. The data block element "MachineXY.Motors[0]" is connected to the HMI tag "MachinXY_Motors{0}". The symbolic addressing of the HMI tag "MachineXY_Motors{0}" is multiplexed by the HMI tag "MotorIndex":

![Multiplexing with symbolic addressing](images/81976087435_DV_resource.Stream@PNG-en-US.png)

The following tags can not be used as index tags for multiplexing with symbolic addressing:

- HMI tags that are not of the "USInt", "UInt", "UDInt", "SInt", "Int" or "DInt" data type
- HMI tags that are already multiplexed
- Array elements
- HMI tags that are elements of structured HMI tags

> **Note**
>
> In Runtime, the first array element is always addressed with the index value "0". Have your array element in the data blocks also start with the index "0".

> **Note**
>
> You can export the HMI tags that are used for multiplexing with symbolic addressing to MS Excel. You can also import such HMI tags from MS Excel into an HMI tag table that contains all HMI tags of the HMI device.

---

**See also**

[External tags (RT Unified)](#external-tags-rt-unified)
  
[Addressing external tags (RT Unified)](#addressing-external-tags-rt-unified)
  
[Configuring address multiplexing with absolute addressing (RT Unified)](#configuring-address-multiplexing-with-absolute-addressing-rt-unified)
  
[Configuring address multiplexing with symbolic addressing (RT Unified)](#configuring-address-multiplexing-with-symbolic-addressing-rt-unified)

### System tags (RT Unified)

#### Introduction

System tags are internal tags that are required for internal management of the project.

#### Principle

The system tag names always start with the "@" character. You may not delete or rename these tags. You cannot change the value of a tag.

> **Note**
>
> You must not create any tags whose name starts with a @.

By default, the following system tags are available for the WinCC Unified devices:

| System tag | Data type | Meaning |
| --- | --- | --- |
| @CurrentLanguage | UDInt | Contains the current runtime language. |
| @DeltaActivationState | UDInt | Contains the current phase when loading changes. |
| @DiagnosticsIndicatorTag | UDInt | Specifies the diagnostic status. The diagnostic status contains the collective status of all relevant PLCs. The worst status of all PLCs is always used in this case.  "@DiagnosticsIndicatorTag" can have the following values:  - Uncertain (0) - Good (1) - Maintenance (2) - Error (3) |
| @LocalMachineName | WString | Contains the IP address of the local computer.  "@LocalMachineName" is a local system tag of the current session. This means the system tag cannot be used as the trigger of a Scheduled task, for example. |
| @ServerMachineName | WString | Contains the name of the PC on which Runtime is running. |
| @SystemActivationState | UDInt | Signals whether Runtime is active and can have the following values:  - System startup in progress (1) - System started (activated) (2) - System stopped (3) - System shutdown in progress (4) - System restart in progress (5) |
| @SystemHealthIndex | UDInt | Shows the current status of the Runtime system.   When the "@SystemHealthIndex" value is 0, the Runtime system is in optimal health. Runtime is in the state expected by the Engineering System. There are no messages that may have a negative impact on the "@SystemHealthIndex".  The greater the "@SystemHealthIndex" value, the less healthy the state of the Runtime system. |
| @UserName | WString | Contains the currently logged-on user.   "@UserName" is a local system tag of the current session. This means the system tag cannot be used as the trigger of a Scheduled task, for example. |

---

**See also**

[Internal tags (RT Unified)](#internal-tags-rt-unified)
  
[Shutdown behavior (RT Unified)](Runtime%20API%20%28RT%20Unified%29.md#shutdown-behavior-rt-unified)

### Basics on arrays (RT Unified)

#### Definition

An array is a data list with data elements of a uniform data type. This data list is referred to as array tag or array for short. The data elements are referred to as array elements.

The individual array elements can be addressed using integer indices. The properties of each array element are the same and are configured centrally at the array tag.

![Definition](images/171638290059_DV_resource.Stream@PNG-en-US.png)

#### Advantages

You can combine a large number of array elements in a structured manner with just one array tag. The common properties of the array elements can be defined centrally in the array tag. Use each individual array element in the configuration as a tag.

#### Restrictions

The following restrictions apply for using arrays on HMI devices and in runtime:

- An array can only contain one dimension. Multi-dimensional arrays of the PLC are mapped to single tags on the HMI systems.
- Only elementary data types without additional substructure can be used as data type of an array. Only scalar arrays are supported.
- The lower index of an array must begin with "0". In case of deviating lower limits of PLC tags, the indices are shifted accordingly.
- Unlike individual tags, scalable arrays do not support ranges, linear scaling or tag multiplexing.

#### Application examples

Array tags can be used in the following situations:

- To group process values in profile trends: You map process values to trends which are acquired at different points in time, for example.
- To access specific values which are grouped in trends: For example, display all recorded values of the profile trend by gradually increasing the index tag.
- To configure discrete alarms with successive bit number.
- To save the complete machine data records in a parameter set.

#### Special features

On HMI devices and in runtime, all array elements are always read or written by the PLC at once when an element in a scalar array is accessed (with the exception of arrays of String/WString).

Example for the HMI devices and in runtime:

- An array tag which consists of 100 array elements of data type "Real" was configured.
- If an array element with a length of 4 bytes changes, 100 x 4 bytes are written to the PLC.

> **Note**
>
> **Increased system load and performance loss**
>
> As a result of the simultaneous transfer of all array elements in a scalar array, writing to the PLC in particular when a large array is accessed takes longer than writing a tag with the same data type. Take this into consideration when designing the communication.
>
> For scalar arrays, the PLC usually reads entire array tags faster than the sum of the read accesses to the same number of elementary tags of the same data type.

> **Note**
>
> **Data inconsistency at array tags**
>
> If the value of a single element is to be changed in an array tag, the whole array is read, changed and rewritten as a complete array. Changes carried out in the meantime to other array elements in the PLC are overwritten during rewriting.
>
> You should always prevent different parts of the system, for example the HMI device and the PLC, from writing values to the same array tag at the same time. Use synchronous transfer of parameter sets, for example, to synchronize an array tag with the PLC.

#### Use in scripts

To maintain performance, always use internal arrays in scripts to change scalable arrays.

**Procedure**

1. Copy the PLC array at the beginning of the script into an internal array.
2. Use the internal array for further use in the script.
3. When you have finished editing, write the internal array back to the PLC array.

**Result**

No load is placed on communication to the PLC while the script processes the internal array.

---

**See also**

[Basics of tags (RT Unified)](#basics-of-tags-rt-unified)
  
[Creating array tags (RT Unified)](#creating-array-tags-rt-unified)

### Updating the tag value in runtime (RT Unified)

#### Introduction

Tags contain process values which change while runtime is running. Value changes are handled differently at internal and external tags.

#### Principle

When runtime starts, the value of a tag is equal to its start value. Tag values change in runtime.

In runtime, you have the following options for changing the value of a tag:

- A value change in an external tag in the PLC.
- By input, for example, in an I/O field.
- A value assignment in a script.

#### Updating the value of external tags

The value of an external tag is updated as follows:

- Cyclic in operation

  If you select the "Cyclic in operation" acquisition mode, the tag is updated in runtime while it is displayed in a screen or is logged. The acquisition cycle determines the update cycle for tag value updates on the HMI device. You can either choose a default acquisition cycle or define a user-specific cycle.
- On demand

  If you select the "On demand" acquisition mode, the tag is not updated cyclically. It will only be updated on demand using the "UpdateTag" system function, for example, or by a script.

---

**See also**

[Defining the acquisition cycle for a tag (RT Unified)](#defining-the-acquisition-cycle-for-a-tag-rt-unified)

### Limits and start values of a tag (RT Unified)

#### Introduction

You can configure start values and restrict the value ranges with limits for numerical tags.

Use the limits to warn the operator when the value of a tag enters a critical range, for example.

Use the start values to assign a default value to an I/O field that is specified as start value in the linked tag.

#### Tags limits

You can specify a value range defined by a high limit and a low limit for numerical tags.

You configure four limit values that limit the value range. Using the limits Upper 2 and Lower 2 , you specify the maximum and minimum value for the value range. The limits Upper 1 and Lower 1 specify the threshold values at which the normal range is exceeded or undershot.

| Limit | Application |
| --- | --- |
| Upper 2 | Specifies the maximum value. |
| Lower 2 | Specifies the minimum value. |

If the operator enters a value for the tag that is outside the configured value range, the input is rejected. When the tag value leaves the value range, the function list is processed.

> **Note**
>
> If you want to output an analog alarm when a limit is violated, configure the respective tag in the "Analog alarms" tab. You can also configure the analog alarm in the "HMI alarms" editor. The values for output of an analog alarm depend on the configured tag limits.

> **Note**
>
> **Limitation**
>
> Tags with the following data types do not support limits:
>
> - Array and array elements
> - Byte
> - Char
> - DWord, LWord and Word

#### Start value of a tag

You can configure a start value for numeric tags and tags for date/time values. The tag will be preset to this value when runtime starts. In this way, you can ensure that the tag has a defined status when runtime starts.

The start value cannot have the data type Raw or TextRef.

For external tags, the start value will be displayed on the HMI device until it is overwritten by the PLC or by input.

If no start value was configured, the tag contains the value "0" when starting runtime.

Use the "Persistence" setting to specify whether the value of the tag is to be retained when runtime is closed. The value saved will be used as the start value when you restart runtime.

---

**See also**

[Defining limits for a tag (RT Unified)](#defining-limits-for-a-tag-rt-unified)

### Data logging (RT Unified)

#### Introduction

Data logging is used to collect, process and log process data from an industrial system. When you analyze the logged process data, you can extract important business and technical information regarding the operational state of the system.

The process values to be logged are compiled, processed and saved in the log database in runtime. Current or previously logged process values can be output in runtime as a table or trend. In addition, it is possible to print out logged process values as a report.

#### Use

You can use data logging for the following tasks:

- Early detection of danger / fault states
- Increase of productivity
- Enhancement of product quality
- Optimization of maintenance cycles
- Documentation of process value trends

#### Configuration

You configure the logging of process values in the "Logs" editor. You create a data log and an alarm log. The data log stores process values in logging tags. When you configure the data log, select the storage location, the logging period and the size of the log. You also specify the settings for the logging segments.

You configure trend views and process controls for displaying process data in runtime in the "Screens" editor. These views allow you to output the process data in the form of trends and tables.

#### Logging tags

You can log the values of internal and external tags. Use the logging tags for logging tag values. In logging tags, you specify how the values of the corresponding tags are written to the log.

You can create a logging tag for each HMI tag in the tag tables. You define the logging tags in the "HMI Tags" editor under "Logging tags". You specify for each logging tag to which log the tag is written.

With the default logging type "On change", the process value is compared to the saved value and the new value is only written to the log if the process value has changed.

To preserve memory, you can activate "smoothing" for the logging tags. By doing so, insignificantly small changes are filtered out prior to writing and the number of logged values is reduced.

Another way to save storage space is to use "Compression" for the logging tags. You select one of the 8 compression modes that calculate the values to be stored.

You create logging tags for internal and external tags. When logging the PLC tag values, the time stamp contains the time at which the value occurred in the PLC.

> **Note**
>
> **Supported data type for logging external tags**
>
> When logging external PLC tags, all data types are supported except "Raw", "TextRef", "Struct" and "Array". The data type "TextRef" must not be used within the "Faceplate container" object.

### Basics of tag management (RT Unified)

#### Basics of tag management

You can always rename, copy or delete tags.

When a tag is renamed, the new name must be unique for the whole device.

> **Note**
>
> The connection to the tags can be interrupted in runtime under the following conditions during renaming:
>
> - HMI tag is used in a type, for example, to dynamize an object property via a script.
> - One or more instances of the type are used in the project.
> - Project is in runtime.
> - After the renaming, execute the command "Compile &gt; Software (only changes)".
>
> Solution: Exit runtime and rename the tag. Execute the "Compile &gt; Software (rebuild all)" command.

If you use the "Copy" command to copy a tag to the clipboard, the references are copied along with the tag.

If you use the "Insert" command to add a tag to another device, the tag will be added without the connected references. Only the object name of the reference will be inserted. If a reference of the same name and valid properties exists in the target system, the existing reference will then be connected to the copied tag.

If you copy a tag, some of the objects linked to the tag are copied as well. The following objects are copied:

- Logging tags
- Cycles
- Alarms

If you add the copied tag to another device, the tag is added together with the linked objects.

Before you delete a tag, check in the "Cross-references" editor where the tag is used and what impact the deletion of the tag will have on your project.

### Basics of user data types (RT Unified)

#### Introduction

With user data types you bundle a number of different tags that form one logical unit. You create a user data type as a type and use instances of this type in the project. User data types are project-associated data and are available for all HMI devices of the project.

WinCC also supports the connection of PLC data types (UDTs) as user data types.

User data types also differ in their applicability with a specific communication driver. User data types are available for the following communication drivers:

- SIMATIC S7-300/400
- SIMATIC S7-1500

Create user data types and user data type elements in the project library.

#### Principle

For example, the different conditions of a motor can be described using 6 unique Boolean tags.

![Principle](images/74978625803_DV_resource.Stream@PNG-en-US.png)

If the overall condition should be described with a single tag, this tag can be created based on a user data type. For each of the individual Boolean tags you create a user data type element in the user data type.

This user data type can then be assigned complete to a faceplate for the motor. The created and released version of user data type is displayed at the tag in the "Data type" selection field.

The configured properties of a user data type are used in the instances of the user data type. If required, you change individual properties directly at the point of use, e.g. at a tag. Changing a property at the tag does not affect the user data type created.

### Export and import of tags (RT Unified)

#### Introduction

With Export and Import, you have the option to export tags from one project and import them into another project. There is also the option to create larger numbers of tags outside of WinCC, edit them and subsequently import into any WinCC project.

You export and import tags with the "Import" and "Export" buttons in the "HMI Tags" editor. When importing the tag data to WinCC, pay attention to the structure required in the import file.

#### Tag data structure

The tag data file must be in "*.xlsx" data format for the tag import and must be structured according to specific rules.

The import file in Microsoft Excel consists of a number of worksheets:

- HMI Tags (tags)
- SubstituteValueUsage (substitute value)

Each tag is on a separate row in the import file. The import file with the tag data must have the following format:

#### Example of the worksheet "HMI Tags"

![Example of the worksheet "HMI Tags"](images/111983504907_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| Name | Indicates the configured name of an HMI tag. |
| Path | Specifies which folders in the project tree contain the tag. The folder structure is represented by ",": "FolderName1,FolderName2,TagName". |
| PLC Tag | Specifies which PLC tag is linked to the HMI tag. |
| Connection | Indicates the name of the connection. |
| Date type | Specifies the data type of the PLC tag. The data types allowed depend on the communication driver being used. See the "Communication" section of the documentation for additional information on the data types permitted for the various communication drivers. |
| HMI Data type | Specifies the data type of the HMI tag. The data types allowed depend on the communication driver being used. See the "Communication" section of the documentation for additional information on the data types permitted for the various communication drivers. |
| Length | Specifies the length of the tag in bytes. This entry is only useful for data types with a dynamic length, for example, strings. This entry remains empty for other data types. |
| Access Method | Specifies the type of access. |
| Address | Specifies the tag address in the PLC. The tag address must exactly match the one used in WinCC, for example, "%DB1.DBW0". The tag address is empty for internal tags. |
| Start Value | Specifies the start value of a tag. |
| Quality code | Provides information on the quality of the connection. |
| Persistency | Indicates whether the value is to be retained after the end of runtime. |
| Substitute Value | Indicates the substitute value. The substitute value is used when a process value with errors is read. |
| ID tag | The update ID updates the value of a tag with the aid of a function or a PLC job.  The update ID must be unique within an HMI device. |
| Update Mode | Indicates whether the tag is to be updated locally or for the entire project. |
| Acquisition mode | Indicates the acquisition mode. |
| Acquisition cycle | Indicates the acquisition cycle used. |
| Limit Upper 2 type | Indicates whether the limit value "Upper 2" is monitored by a constant or not at all. |
| Limit Upper 2 | Displays the limit value "Upper 2". |
| Limit Lower 2 type | Indicates whether the limit value "Lower 2" is monitored by a constant or not at all. |
| Limit Lower 2 | Displays the limit value "Lower 2". |
| End value PLC | Specifies the end value of the PLC tag. |
| Start value PLC | Specifies the start value of the PLC tag. |
| End value HMI | Specifies the end value of the HMI tag. |
| Start value HMI | Specifies the start value of the HMI tag. |

> **Note**
>
> **HMI tags with user data type**
>
> When exporting HMI tags that use a user data type as the data type, configured limit values and start values are not exported.

#### Example of the worksheet "SubstituteValueUsage"

![Example of the worksheet "SubstituteValueUsage"](images/31177091211_DV_resource.Stream@PNG-de-DE.png)

Meaning of the entries

| List entry | Meaning |
| --- | --- |
| HMI Tag name | Specifies the tag for which a substitute value has been defined. The tag must be available in the "HMI-Tags" worksheet. |
| Substitute Value Usage | Indicates the substitute value. The substitute value can be used in the following situations:  - As start value - After communication error - Upper 2 limit value - Lower 2 limit value |

> **Note**
>
> **"No value" in the table**
>
> Entries in the table which have the value "No value" delete the corresponding values in an existing tag of the same name.

---

**See also**

[Importing and exporting tags (RT Unified)](#importing-and-exporting-tags-rt-unified)

## Configuring tags (RT Unified)

This section contains information on the following topics:

- [Working with tag tables (RT Unified)](#working-with-tag-tables-rt-unified)
- [Creating external tags (RT Unified)](#creating-external-tags-rt-unified)
- [Creating OPC tags (RT Unified)](#creating-opc-tags-rt-unified)
- [Creating internal tags (RT Unified)](#creating-internal-tags-rt-unified)
- [Addressing tags indirectly (RT Unified)](#addressing-tags-indirectly-rt-unified)
- [Configuring multiple tags (RT Unified)](#configuring-multiple-tags-rt-unified)
- [Adapting the data type of a tag (RT Unified)](#adapting-the-data-type-of-a-tag-rt-unified)
- [Creating array tags (RT Unified)](#creating-array-tags-rt-unified)
- [Configuring address multiplexing with absolute addressing (RT Unified)](#configuring-address-multiplexing-with-absolute-addressing-rt-unified)
- [Configuring address multiplexing with symbolic addressing (RT Unified)](#configuring-address-multiplexing-with-symbolic-addressing-rt-unified)
- [Defining the acquisition cycle for a tag (RT Unified)](#defining-the-acquisition-cycle-for-a-tag-rt-unified)
- [Specify tag persistency (RT Unified)](#specify-tag-persistency-rt-unified)
- [Defining limits for a tag (RT Unified)](#defining-limits-for-a-tag-rt-unified)
- [Specify "Local session" scope (RT Unified)](#specify-local-session-scope-rt-unified)
- [Synchronizing tags (RT Unified)](#synchronizing-tags-rt-unified)
- [Importing and exporting tags (RT Unified)](#importing-and-exporting-tags-rt-unified)
- [Defining a substitute value (RT Unified)](#defining-a-substitute-value-rt-unified)
- [Connecting a tag to another PLC (RT Unified)](#connecting-a-tag-to-another-plc-rt-unified)

### Working with tag tables (RT Unified)

Tags are displayed in tag tables.

Here you create tags, edit their properties and export them.

#### Adapting the view of the table

The shortcut menu of a column header allows you to

- adjust the width of individual or all columns
- show or hide individual columns

  ![Adapting the view of the table](images/152143749387_DV_resource.Stream@PNG-en-US.png)

To arrange columns, drag a column header to a different position.

To have your individually designed view displayed again the next time you call up the tag table, click ![Adapting the view of the table](images/152144388107_DV_resource.Stream@PNG-de-DE.png) "Save window settings".

To insert a tag above a selected line, click ![Adapting the view of the table](images/152144550283_DV_resource.Stream@PNG-de-DE.png) "Lines above ...".

To sort the Table, click on a column header.

---

**See also**

[Creating external tags (RT Unified)](#creating-external-tags-rt-unified)
  
[Creating internal tags (RT Unified)](#creating-internal-tags-rt-unified)
  
[Creating OPC tags (RT Unified)](#creating-opc-tags-rt-unified)

### Creating external tags (RT Unified)

#### Introduction

You can access an address in the PLC via a PLC tag using an external tag. The following options are available for addressing:

- Symbolic addressing
- Absolute addressing

If possible, use symbolic addressing when configuring a tag. Symbolic addressing enables high-performance data access and is therefore less prone to errors. The system monitors the assignment of the storage address and the locations of use are automatically updated when changes occur.

You create tags either in the standard tag table or in a tag table you defined yourself.

#### Requirement

- The project is open.
- A connection to the PLC is configured.
- The Inspector window is open.

#### Procedure

To create an external tag, proceed as follows:

1. Open the "HMI tags" folder in the project tree and double-click the standard tag table. The tag table opens.  
   Alternatively, create and then open a new tag table.
2. In the "Name" column, double-click "Add" in the tag table.

   A new tag is created.
3. Select the "Properties &gt; Properties &gt;General" category in the Inspector window and, if required, enter a unique tag name in the "Name" field.

   The tag name must be unique throughout the device.
4. Select the connection to the required PLC in the "Connection" box.

   If the connection you require is not displayed, you must first create the connection to the PLC. You create the connection to a SIMATIC S7 PLC in the "Devices &amp; Networks" editor. You create the connection to external PLCs in the "Connections" editor.  
   If the project contains the PLC and supports integrated connections, you can also have the connection created automatically. To do this, when configuring the HMI tag, simply select an existing PLC tag to which you want to connect the HMI tag. The integrated connection is then automatically created by the system.
5. If you are working with an integrated connection, click the ![Procedure](images/70487246859_DV_resource.Stream@PNG-de-DE.png) button in the "PLC tag" field and select an already created PLC tag in the object list. Click ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) to confirm the selection.

   ![Procedure](images/158851842955_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158851842955_DV_resource.Stream@PNG-en-US.png)

   Alternatively, use the autocomplete to select a PLC tag for an integrated connection.

   If you select a PLC tag from the autocomplete list, it is entered in the input path. The elements of the PLC tags are displayed in the autocomplete list. If you have selected a PLC tag that can be connected to the HMI tags, the PLC tag is connected to the HMI tags.
6. If you are working with a non-integrated connection, enter the address from the PLC in the "Address" field. To enter the address, make sure that the access mode "Absolute access" is configured.

   The "PLC tag" field remains empty.
7. Configure the other properties of the tag in the inspector window.

   You can also configure all tag properties directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| - You also create new tags directly at the location of use, for example, on an I/O field. To do this, click "Add new" in the object list.   You then configure the new tag in the Inspector window. - You can also create external HMI tags by dragging and dropping data block elements or global PLC tags into an HMI tag table. |  |

#### Result

An external tag has been created and linked to a PLC tag or an address in the PLC.

---

**See also**

[Basics of tags (RT Unified)](#basics-of-tags-rt-unified)
  
[External tags (RT Unified)](#external-tags-rt-unified)
  
[Addressing external tags (RT Unified)](#addressing-external-tags-rt-unified)

### Creating OPC tags (RT Unified)

#### Requirement

- A connection to an OPC UA server has been set up.
- When the connection to the OPC UA server is secured via a certificate, the application instance certificate of the WinCC Unified clients must be in the "Trusted" folder of the OPC UA server.

#### Procedure

To create an external tag, proceed as follows:

1. Open the "HMI tags" folder in the project tree and double-click the tag table. The tag table opens.  
   Alternatively, create and then open a new tag table.
2. In the "Name" column, double-click "Add" in the tag table.

   A new tag is created.
3. Select the "Properties &gt; Properties &gt;General" category in the Inspector window and, if required, enter a unique tag name in the "Name" field.

   The tag name must be unique throughout the device.
4. If required, select the "Display name" field to enter a name to be displayed in runtime.
5. Select the connection to the desired OPC UA server in the "Connection" field.

   If the connection you require is not displayed, you must first create the connection to the OPC UA server. You establish the connection to an OPC UA server in the "Connections" editor.
6. Click in the "Address" field and follow these steps:

   - In the left area, browse through the address space of the OPC UA server to the node below which the required tag is located.
   - Select the tag in the right area.
   - Confirm your selection.

#### Result

The new HMI tag is connected to the tag of the OPC UA server. It is available for configuring HMI screens.

After loading the project into a Runtime:

- Runtime has read and write access to the connected OPC UA tag.
- Changes to the tag value on the OPC UA server are automatically passed on to the runtime.

---

**See also**

[Defining connection settings to the OPC UA server (RT Unified)](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#defining-connection-settings-to-the-opc-ua-server-rt-unified)

### Creating internal tags (RT Unified)

#### Introduction

You must at least set the name and data type for internal tags. Select the "Internal tag" item, rather than a connection to a PLC.

For documentation purposes, it is a good idea to enter a comment for every tag.

#### Procedure

1. Open the "HMI tags" folder in the project tree and double-click the entry "Standard tag table". The tag table opens.  
   Alternatively, create and then open a new tag table.
2. In the "Name" column, double-click "Add" in the tag table. A new tag is created.
3. If the Inspector window is not open, select the "Inspector window" option in the "View" menu.
4. Select the "Properties &gt; Properties &gt;General" category in the Inspector window and, if required, enter a unique tag name in the "Name" field.
5. If required, select the "Display name" field to enter a name to be displayed in runtime.

   The name to be displayed is language-specific and can be translated for the required runtime languages. The display name is available for Basic Panels, Panels and Runtime Advanced.

   ![Procedure](images/131117628299_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131117628299_DV_resource.Stream@PNG-en-US.png)
6. Select "Internal tag" as the connection in the "Connection" field.
7. Select the required data type in the "Data type" field.
8. In the "Length" field, you can specify the maximum number of characters to be stored in the tag in accordance with the selected data type.

   The length is automatically defined by the data type for numerical tags.
9. As an option, you can enter a comment regarding the use of the tag. To do so, click "Properties &gt; Properties &gt; Comment" in the Inspector window and enter a text.

**Note**

This tag name must be unique throughout the project. The tag name must not contain the special characters line feed, carriage return or quotation marks.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for effective configuring** |
| - You also configure the tag properties directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu. - You also create new tags directly at the location of use, for example, on an I/O field. To do this, click "Add new" in the object list. You then configure the new tag in the Inspector window. |  |

#### Result

An internal tag is created. You can now use this in your project.

In additional steps you can configure the tag, for example, by setting the start value and limits.

---

**See also**

[Basics of tags (RT Unified)](#basics-of-tags-rt-unified)
  
[Internal tags (RT Unified)](#internal-tags-rt-unified)
  
[Configuring discrete alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-analog-alarms-rt-unified-1)

### Addressing tags indirectly (RT Unified)

#### Introduction

With indirect addressing, the tag used is first determined during runtime. Instead of individual tags, you define a series of tags. In Runtime, the tag name is used to access individual tags.

#### Requirements

- The HMI tag "Temperature_Motor" of type "WString" that you want to use for indirect addressing has been created.
- A series of HMI tags is created, for example, the "Motor1", "Motor2" and "Motor3" tags.
- The Inspector window with the tag properties is open.
- You have created a screen and the "Screens" editor is open.

#### Procedure

To address tags indirectly, proceed as follows:

1. Insert an IO field into the screen and select the following settings for this example in the Inspector window under "Properties &gt; Properties &gt; General":

   - Mode: Output
   - Output format: {I}
2. Link the process value to a tag.
3. Open the object list in the "Tag" field using the selection button, select the "Temperature_Motor" tag and activate the "Use indirect addressing" option.

   ![Procedure](images/172758112011_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172758112011_DV_resource.Stream@PNG-en-US.png)
4. Add another I/O field to the screen and select the following setting for this example in the Inspector window under "Properties &gt; Properties &gt; General":

   - Mode: Input/output
5. Link the process value to a tag.
6. Open the object list in the "Tag" field using the selection button, select the "Temperature_Motor" tag. Do not activate the option "Use indirect addressing".
7. Save the project.

#### Result

If you enter the name of one of the tags "Motor1", "Motor2" or "Motor3" in the IO field in Runtime, the value of the respective tag is displayed in the other IO field.

---

**See also**

[Internal tags (RT Unified)](#internal-tags-rt-unified)
  
[Indirect addressing (RT Unified)](#indirect-addressing-rt-unified)
  
[Creating internal tags (RT Unified)](#creating-internal-tags-rt-unified)

### Configuring multiple tags (RT Unified)

#### Introduction

In a tag table, you create a large number of identical tags by automatically filling the rows of the table below a tag. The tag names are incremented automatically when filling in automatically.

You can also use the auto fill function to fill table cells below a tag with a single tag property and thus modify the corresponding tags.

If you apply the automatic filling in to already filled cells of a tab table, you will be asked whether you want to overwrite the cells or insert new tags.

If you do not want to overwrite already configured tags, activate insert mode. Activate insert mode by keeping the &lt;Ctrl&gt; key pressed during insertion. Already existing entries in the tag table are moved down if insert mode is activated.

| Symbol | Meaning |
| --- | --- |
| ![Introduction](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| You can configure multiple tags simultaneously and use them in the screen. If you use drag and drop to drag multiple tags from the detail view to the screen, an I/O field is created for each tag that is connected to the respective tag. |  |

#### Requirements

- The project is open.
- A tag table is open.
- The tag which is to serve as a template for other tags is configured.

#### Procedure

1. If you want to create new tags, mark in the "Name" column the tag that should be used as a template for the new tags.

   If you want to copy a property of a tag to the tags below it, select the cell which contains this property.

   The selected cell will be highlighted in color and a small blue square will appear in its bottom right corner. When you move the mouse over this square, the cursor will change to a black cross.

   ![Procedure](images/70484772619_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70484772619_DV_resource.Stream@PNG-en-US.png)
2. Hold down the mouse button and drag this square over the cells below that you wish to fill automatically.

   The marking will be extended to cover this area.

   ![Procedure](images/70484778123_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70484778123_DV_resource.Stream@PNG-en-US.png)
3. Now release the mouse button. All of the marked cells are filled automatically.

   New tags will be created in all empty rows in the marked area.

   ![Procedure](images/70485139467_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70485139467_DV_resource.Stream@PNG-en-US.png)
4. In the tag table, select all the tags that you want to configure at the same time.

   If the selected property is identical for all the tags, the setting for this property will appear in the Inspector window.

   The associated field will remain blank otherwise.
5. You can define the shared properties in the Inspector window or directly in the tag table.

#### Result

Depending on which cells were selected, the function may automatically fill individual properties or create and configure new tags.

### Adapting the data type of a tag (RT Unified)

#### Introduction

When you create a tag, you assign one of the possible data types to the tag. This data type depends on the type of data for which you would like to use the tag.

The data types available depend on the connected communication partner, such as a PLC.

> **Note**
>
> If you modify the data type of an existing, external tag, the previously defined tag address is identified as invalid. This reason for this is that the PLC address changes when the data type is modified.

#### Format adjustment

WinCC sets the data type of an external tag according to the data type of the connected PLC tag. If the data type of the PLC tag is not available in WinCC, a compatible data type is automatically used at the HMI tag. As required, you can specify that WinCC uses a different data type and converts the format of the data type of the PLC tag and the data type of the HMI tag.

> **Note**
>
> If you use a tag with a PLC user data type and subsequently change it, the data type is reset to an array with elements of the "Int" type. The PLC user data type must be recompiled.

In WinCC, you have access to the following data types:

| HMI data type | Description | Value range |
| --- | --- | --- |
| Bool | Binary tag | 0 to 1 |
| SInt | Signed 8-bit value | -128 ... +127 |
| USInt | Unsigned 8-bit value | 0 ... 255 |
| Int | Signed 16-bit value | -32768 ... +32767 |
| UInt | Unsigned 16-bit value | 0 ... 65535 |
| DInt | Signed 32-bit value | -2147483648 ... +2147483647 |
| UDInt | Unsigned 32-bit value | 0 ... 4294967295 |
| LInt | Signed 64-bit value | -9223372036854775808 to +9223372036854775807 |
| ULInt | Unsigned 64-bit value | 0 to 18446744073709551615 |
| Real | 32-bit floating-point number IEEE 754 | +-3.402823e+38 |
| LReal | 64-bit floating-point number IEEE 754 | +-1.79769313486231e+308 |
| Byte | Bit array of 8 bits | 8-bit |
| Word | Bit array of 16 bits | 16-bit |
| DWord | Bit array of 32 bits | 32-bit |
| LWord | Bit array of 64 bits | 64-bit |
| String | Text tag, 8-bit character set | - |
| WString | Text tag, 16-bit character set | - |
| WChar | Text tag | - |
| DateTime | Date/time format | 01.01.1601 00:00 … 31.12.9999 23:59:59 |
| LTime | Signed 64-bit integer value | -9223372036854775808 … +9223372036854775807 100ns |
|  |  |  |

For format adaptation, select the desired PLC data type at the respective external tag. The suitable standard data type is then selected automatically in the "HMI data type" field for use in WinCC. Change the format adaptation as required.

#### Data types without format adaptation

The data types are shown 1:1 without format adaptation.

**SIMATIC S7-300/400 data types without format adjustment**

| PLC data type | Description |
| --- | --- |
| Bool | No format adaptation |
| String | No format adaptation |

### Creating array tags (RT Unified)

#### Introduction

Create an array tag to configure a large number of tags of the same data type. The array elements are saved to a consecutive address space.

You can create an array tag as an internal tag or as an external tag.

> **Note**
>
> **Connecting HMI tags to PLC array tags**
>
> If you want to create an array tag as an external tag, first configure an array tag in a data block of the connected PLC. You then connect the array tag to an HMI tag.

> **Note**
>
> HMI array tags of the following data types are only supported with connected PLC array tags:
>
> - Char
> - WChar
> - String

#### Creating HMI array tags

To create an array tag, follow these steps:

1. Open the HMI tag table.
2. Double click &lt;Add&gt; in the "Name" column of the HMI tag table.  
   A new HMI tag is created.

#### Configuring HMI array tags

1. Click in the Data type column of the HMI tag table ![Configuring HMI array tags](images/70806108299_DV_resource.Stream@PNG-de-DE.png) and select the "Array" data type.
2. Click ![Configuring HMI array tags](images/70487246859_DV_resource.Stream@PNG-de-DE.png) in the data type column.

   The dialog box for configuring the array is opened.

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)
3. Select the data type for the array tag in the "Data type" field.

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)
4. Define the number of array elements in the "Array limits" field. The lower limit is "0".
5. Click ![Configuring HMI array tags](images/84603740299_DV_resource.Stream@PNG-de-DE.png).

   The settings for the array are saved.

**Note**

In the case of PLC array tags, addresses are automatically assigned to the array tag with its elements. You can manually adjust the address of the array tags.

#### Result

A HMI array tag is created. The properties of the array elements are inherited from the parent array tag.

---

**See also**

[Basics on arrays (RT Unified)](#basics-on-arrays-rt-unified)
  
[Basics of tags (RT Unified)](#basics-of-tags-rt-unified)

### Configuring address multiplexing with absolute addressing (RT Unified)

#### Introduction

When using address multiplexing, you can efficiently access different addresses in the PLC with the help of a small number of tags. Instead of the absolute address in the PLC you use tags to be able to change the address in Runtime.

#### Requirements

- The HMI device is connected to a PLC.
- 2 HMI tags of numeric type are created.
- The HMI tag for address multiplexing is created.

#### Procedure

1. Select the HMI tag for address multiplexing in the tag table, and select "Properties &gt; Properties &gt; General" in the Inspector window.

   The general properties of the tag are displayed.

   ![Procedure](images/172890450315_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172890450315_DV_resource.Stream@PNG-en-US.png)
2. Select the data type "Bool" for this example.
3. Use the "Connection" field to select the connection to the PLC.

   ![Procedure](images/172890518923_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172890518923_DV_resource.Stream@PNG-en-US.png)
4. Select the "Absolute access" access mode.
5. Click the selection button in the "Address" field. The address dialog opens.

   ![Procedure](images/70497393675_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70497393675_DV_resource.Stream@PNG-en-US.png)
6. Click the selection button in the "DB number" field and select the entry "HMI tag".

   ![Procedure](images/70497746443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70497746443_DV_resource.Stream@PNG-en-US.png)
7. Click the ![Procedure](images/172910982283_DV_resource.Stream@PNG-de-DE.png) button in the "DB number" field and select an HMI tag of numeric type for the DB number in the object list. Or create a new tag with the help of the object list. Accept the tag by clicking the ![Procedure](images/172910986379_DV_resource.Stream@PNG-de-DE.png) button.

   ![Procedure](images/70498649611_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70498649611_DV_resource.Stream@PNG-en-US.png)
8. Repeat steps 3 and 4 for the "Address" field and configure an additional numeric type HMI tag for calling the address area in the data block.

   ![Procedure](images/70499080203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70499080203_DV_resource.Stream@PNG-en-US.png)

The selection options in the Address dialog depend on the selected data type of the multiplex tag. The Address dialog offers only address settings that can be configured with the selected data type.

#### Result

In runtime, the multiplex tag is used to access the memory location corresponding to the address currently found in the tag. You control access to the data block with the tag in the DB number field. You control access to the address in the selected data block with the tag in the "Address" field.

> **Note**
>
> The value in the memory location will only be read at the next update cycle for the addressed tag.
>
> If, for example, you use a multiplex tag in a script, do not attempt to access contents of the memory location directly after changing it.

---

**See also**

[External tags (RT Unified)](#external-tags-rt-unified)
  
[Addressing external tags (RT Unified)](#addressing-external-tags-rt-unified)
  
[Address multiplexing (RT Unified)](#address-multiplexing-rt-unified)
  
[Creating external tags (RT Unified)](#creating-external-tags-rt-unified)
  
[Configuring address multiplexing with symbolic addressing (RT Unified)](#configuring-address-multiplexing-with-symbolic-addressing-rt-unified)

### Configuring address multiplexing with symbolic addressing (RT Unified)

#### Introduction

When using address multiplexing, you can efficiently access different addresses in the PLC with the help of a small number of tags. Instead of the symbolic address in the PLC you use tags to be able to change the address in Runtime.

#### Requirements

- A data block with an array tag is created in the connected PLC.
- The data block was compiled.
- The HMI tag for address multiplexing is created.
- The Properties window for this tag is open.

#### Procedure

1. Select the tag for address multiplexing in the tag table, and select "Properties &gt; Properties &gt; General" in the Inspector window. The general properties of the tag are displayed.

   ![Procedure](images/172903149067_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172903149067_DV_resource.Stream@PNG-en-US.png)
2. Use the "Connection" field to select the connection to the PLC.

   ![Procedure](images/172903780619_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172903780619_DV_resource.Stream@PNG-en-US.png)
3. Select the access type "Symbolic access".
4. Navigate via the field "PLC tag" to the data block of the PLC and select an array element of the array tag.

   ![Procedure](images/172903913227_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172903913227_DV_resource.Stream@PNG-en-US.png)
5. Click the selection button in the "Address" field. The address dialog opens.
6. Click the selection button in the "Index tag" field and select the entry "HMI_Tag".

   ![Procedure](images/172906106379_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172906106379_DV_resource.Stream@PNG-en-US.png)
7. In the "Index tag" field, click the ![Procedure](images/172910982283_DV_resource.Stream@PNG-de-DE.png) button and select an HMI tag for the array index in the object list. Or create a new tag with the help of the object list. Accept the tag by clicking the ![Procedure](images/172910986379_DV_resource.Stream@PNG-de-DE.png) button.

   ![Procedure](images/172906162187_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/172906162187_DV_resource.Stream@PNG-en-US.png)

#### Result

In Runtime, the array element whose index value is contained in the index tag is accessed.

---

**See also**

[Configuring address multiplexing with absolute addressing (RT Unified)](#configuring-address-multiplexing-with-absolute-addressing-rt-unified)
  
[Creating external tags (RT Unified)](#creating-external-tags-rt-unified)
  
[Address multiplexing (RT Unified)](#address-multiplexing-rt-unified)
  
[Addressing external tags (RT Unified)](#addressing-external-tags-rt-unified)
  
[External tags (RT Unified)](#external-tags-rt-unified)

### Defining the acquisition cycle for a tag (RT Unified)

#### Introduction

The value of an external tag can be changed in runtime by the PLC to which the tag is linked. To ensure that the HMI device is informed of any changes in tag values by the PLC, the values must be updated on the HMI. The value is updated at regular intervals while the tag is displayed in the process screen or is logged. The interval for regular updates is set with the acquisition cycle.

#### Requirement

- You have created the tag for which you want to define an acquisition cycle.
- The Inspector window with the tag properties is open.

#### Procedure

To configure an acquisition cycle for a tag, follow these steps:

1. In the Inspector window, select "Properties &gt; Properties &gt; Settings".
2. Select the acquisition mode for the tag:

   - "Cyclic in operation": The tag is updated at regular intervals as long as it is displayed or archived in the screen.
   - "On demand": Updating is performed only on demand, for example, with the "UpdateTag" system function or a script.
3. If you have selected the "Cyclic in operation" acquisition mode, specify the desired cycle time in the "Acquisition cycle" field.

   You have the option of selecting a user-defined cycle.

> **Note**
>
> For structured HMI tags, the acquisition mode can be selected for the respective structured HMI tag as well as their individual subordinate elements.
>
> When the acquisition mode of structured HMI tags is changed, it is applied to all subordinate elements. This means changing the acquisition mode may overwrite subordinate elements.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| Configure the acquisition cycle directly in the work area of the tag table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

The configured tag is updated in runtime with the selected acquisition cycle.

---

**See also**

[Updating the tag value in runtime (RT Unified)](#updating-the-tag-value-in-runtime-rt-unified)
  
[Defining cycles (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#defining-cycles-rt-unified)

### Specify tag persistency (RT Unified)

#### Introduction

In Runtime Unified you have the option to define tag persistency for internal tags. The last values of these persistent tags are used after Runtime has been started.

A separate database, in which the last values of the persistency tags are stored, is used for tag persistency. These values are available again after restarting runtime or restarting or switching off the HMI device.

You activate tag persistency in the runtime settings of the respective HMI device by specifying the database storage location.

> **Note**
>
> **Complete loading of a runtime project**
>
> Tag persistency can only be used when you enable the option "Keep current values of tags and pending alarms in runtime" in the "Load preview" dialog.
>
> When you disable the option "Keep current values of tags and pending alarms in runtime" in the "Load preview" dialog, the database for the tag persistency is emptied. The persistency tags apply the defined start value. If no initial value is defined, the valid default value is used for the data type.

#### Requirement

- The tag for which you want to set the persistency is created.
- The Inspector window with the properties for this tag is open.

#### Procedure

1. In the Inspector window, select "Properties &gt; Properties &gt; Settings".
2. Activate the option "Persistency for internal tags" under "Persistency".
3. Download the full project.

#### Result

The last value of the configured tag is stored in the tag persistency database.

---

**See also**

[Creating internal tags (RT Unified)](#creating-internal-tags-rt-unified)
  
[Initial download of a project (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#initial-download-of-a-project-rt-unified-1)
  
[Storage system (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#storage-system-rt-unified-1)
  
[Storage system (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#storage-system-rt-unified)

### Defining limits for a tag (RT Unified)

> **Note**
>
> **Limitation**
>
> Tags with the following data types do not support limits:
>
> - Array and array elements
> - Byte
> - Char
> - DWord, LWord and Word

#### Introduction

For numerical tags, you can specify a value range by defining a low and high limit as well as the threshold values.

#### Requirement

- The tag for which you want to set the limits is created.
- The Inspector window with the properties for this tag is open.

#### Procedure

To define limits for a tag, proceed as follows:

1. In the Inspector window, select "Properties &gt; Properties &gt; Range". If you want to define one of the limits as a constant value, select "Constant" using the ![Procedure](images/13196575115_DV_resource.Stream@PNG-de-DE.png) button. Enter a number in the relevant field.

   If you want to define one of the limits as a tag value, select "HMI tag" using the ![Procedure](images/13196575115_DV_resource.Stream@PNG-de-DE.png) button. Use the object list to define the tag for the limit.
2. To set additional limits for the tag, repeat step 1 with the appropriate settings.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You also configure the limits directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

You have set a value range defined by the limits for the selected tag.

---

**See also**

[Limits and start values of a tag (RT Unified)](#limits-and-start-values-of-a-tag-rt-unified)

### Specify "Local session" scope (RT Unified)

#### Introduction

Internal tags apply "system-wide" by default.

The scope of an internal tag can be changed to "Local session". Session-related data is processed independently in each local user session in a multi-user environment.

The use of session-local tags in Unified Collaboration and in the Web Client is supported.

#### Example scenarios for local session tags

- Individual navigation in screen windows or in different menu structures
- Session-related blocking/unblocking of the user
- Session-related position, alignment and rotation of objects in a screen.

#### Restrictions

> **Note**
>
> A configuration of tags that contradicts the restrictions, leads either to an error in the engineering system or to an error in runtime.

The "Session local" scope is available only for internal tags.

Local session tags

- Are only accessible within the respective user session
- Can only be used in local scripts. Using it in a global script will result in an error.
- Cannot be used as a trigger of a task
- Cannot be used as a trigger of an alarm or for dynamization of an alarm list
- Cannot be used to dynamize objects through a resource list
- Cannot be used to specify a limit value, substitute value or start value of another tag
- Cannot be used as logging tag
- Cannot be logged
- Do not support the properties

  - GMP (Good Manufacturing Practice)
  - Persistence
- Cannot be used in Openness applications

#### End of a session

- A user session on a Panel ends when Runtime stops.

  A user change on a Panel does not end the session on the Panel. The value of a session-local tag remains on the Panel in this case.
- When displayed in a browser, the user session ends when the view is refreshed, for example, by pressing &lt;F5&gt;.

  A new user session is created. The value of a session-local tag is set to 0 (zero). The currently logged on user remains logged on.
- The values of the local session tags are not saved and are lost.
- Values of system-wide tags remain unchanged after the end of a session.

#### Procedure

1. Open a HMI tag table.
2. Display the "Scope" column.
3. Create an internal tag or select an already created internal tag.
4. In the "Scope" column, select the "Local session" entry.

   You can also make this setting in the Inspector window under "Properties &gt; Properties &gt; Settings".

#### Result

You have created a tag that can take on different values in different sessions.

This tag can, for example, be addressed by the same script in different sessions. The dynamization of an object can be controlled by the same tag, which takes different values in different sessions.

> **Note**
>
> **Local session tags only as of V18**
>
> If the version of the device is smaller than V18, the tag automatically becomes "system-wide" because the limited scope is not supported.

### Synchronizing tags (RT Unified)

#### Introduction

To synchronize the PLC and HMI tags, WinCC offers the following options:

- Synchronizing tags with or without name matching between PLC and WinCC

  The following options are available for this:
- Link tags with addresses in the PLC

  This procedure is suitable, for example, if changes were made to the connection between the HMI device and the PLC and the tag connections were lost in the process. The function can also be used if you have configured the control program and HMI project separately.

#### Requirement

- External HMI tags have been created.
- PLC tags have been created.
- An HMI connection to a PLC in the project has been established.

#### Procedure

To synchronize HMI tags with PLC tags, follow these steps:

1. In the project tree, select the directory that contains the tags in question.
2. Select "Synchronize with the PLC tag" from the shortcut menu.

   A dialog opens.

   ![Procedure](images/89640849291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/89640849291_DV_resource.Stream@PNG-en-US.png)
3. Select the option you want to use.

   If you want to synchronize the tags without name matching, disable "Replace WinCC tag name with PLC tag name".

   If you want to reconnect HMI tags with absolute access, select "Data type and absolute address match".
4. Confirm with "Synchronize".

   The system searches for a suitable PLC tag according to the selected option.

#### Result

The external HMI tags are synchronized with the PLC tags.

If you have selected the option "Data type and absolute address match", the tag connection is established as soon as a suitable PLC tag is found.

If you have selected a different option, the WinCC tags are updated accordingly and the PLC tag names are applied in WinCC.

---

**See also**

[Settings for tags (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#settings-for-tags-rt-unified)
  
[Settings for tags (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#settings-for-tags-rt-unified-1)

### Importing and exporting tags (RT Unified)

#### Introduction

WinCC gives you the option of exporting tags to an .xlsx file and reimporting them into the project once you are done editing them. You export and import tags in the "HMI Tags" editor

For importing the tags, the xlsx import file must be structured according to the requirements. You will find more detailed information on the import file under "[Export and import of tags](#export-and-import-of-tags-rt-unified)".

#### Exporting tags

1. Click the ![Exporting tags](images/70613019147_DV_resource.Stream@PNG-de-DE.png) button in the "HMI Tags" tab.

   The "Export" dialog box opens.

   ![Exporting tags](images/75166390539_DV_resource.Stream@PNG-en-US.png)

   ![Exporting tags](images/75166390539_DV_resource.Stream@PNG-en-US.png)
2. Click "..." and specify in which file the data are saved.
3. Click "Export".

   The export will start.

> **Note**
>
> It is not possible to export HMI tags of the data type "UDT" which contain structured elements via Excel for subsequent editing.
>
> After export, only the higher-level HMI tag appears in Excel. Its lower-level elements cannot be edited.

#### Importing tags

1. Click "HMI tags" in the project tree.
2. Double-click "Show all tags". The "HMI tags" editor opens.
3. Click ![Importing tags](images/70613888907_DV_resource.Stream@PNG-de-DE.png) in the "HMI Tags" tab.
4. The "Import" dialog box opens.

   ![Importing tags](images/76071197963_DV_resource.Stream@PNG-en-US.PNG)

   ![Importing tags](images/76071197963_DV_resource.Stream@PNG-en-US.PNG)
5. Click "..." and select the file that you want to import.
6. Click "Import".

   The import starts

#### Result

The relevant tags have been created in WinCC. Alarms relating to the import operation are displayed in the output window. A log file is saved in the source directory of the import files. The log file has the same name as the respective import file but with the "*.xml" extension.

Check when importing the data whether there are any links to objects, for example, dynamic parameters such as tags.

- If an object with the same name already exists, the existing object is used.
- If no object of the same name yet exists, create an object with the relevant name or create a new link.

> **Note**
>
> The syntax of the import file is checked during xlsx file import. The meaning of the properties or dependencies between the properties is not checked.

### Defining a substitute value (RT Unified)

#### Introduction

You can define a specific value as a substitute value for a tag.

In the "Use substitute value" area you define when WinCC should use this substitute value. The current process value is then not accepted from the automation system.

You can define a substitute value for the following cases:

![Introduction](images/102696926731_DV_resource.Stream@PNG-en-US.png)

- The configured ranges have been violated

  If you have set limit values for the tag, WinCC sets the substitute value as soon as the process value violates a limit.
- In the event of a communications error

  WinCC sets the substitute value when the connection to the automation system is disturbed and there is no valid process value.

#### Requirement

- The tag table is open.
- The Inspector window with the tag properties is open.
- The HMI tag is linked to a PLC tag

#### Procedure

To configure a substitute value, follow these steps:

1. Select the desired tag in the tag table, and select "Properties &gt; Properties &gt; Values" in the Inspector window.
2. In the "Use substitute value" segment, select when you want WinCC to use this substitute value in the tag.
3. Enter the required substitute value in the "Substitute value" field.

#### Result

The configured tag is populated with the substitute value in runtime once the selected condition is fulfilled.

> **Note**
>
> If you have set a high or low limit in an I/O field, you cannot enter any value outside these limits.
>
> WinCC ignores incorrect entries and therefore does not set a substitute value. The substitute value is only set by WinCC when an incorrect process value is read.

### Connecting a tag to another PLC (RT Unified)

#### Introduction

In WinCC, you can change the PLC connection of a tag at any time. This is needed when you change the configuration of your plant, for example.

Depending on the PLC selected, you may need to modify the configuration of the tag. The tag properties which must be changed will be highlighted in color.

#### Requirement

- The external tag, whose connection you wish to change, must already exist.
- The connection to the PLC must already exist.
- The Properties window for this tag is open.

#### Procedure

To change the PLC connection of a tag, proceed as follows:

1. In the Inspector window select "Properties &gt; Properties &gt; General."
2. Select the new connection in the "Connection" field.

   The tag properties that you must change will be highlighted in color in the tag table and in the Inspector window.
3. Change all highlighted properties of the tag to suit the requirements of the new PLC.

#### Result

The external tag is connected to the new PLC.

## Configuring user data types (RT Unified)

This section contains information on the following topics:

- [Creating an HMI user data type (RT Unified)](#creating-an-hmi-user-data-type-rt-unified)
- [Creating HMI user data type elements (RT Unified)](#creating-hmi-user-data-type-elements-rt-unified)
- [Adding a PLC user data type to the project library (RT Unified)](#adding-a-plc-user-data-type-to-the-project-library-rt-unified)
- [Managing versions of user data types (RT Unified)](#managing-versions-of-user-data-types-rt-unified)
- [Setting a user data type version as default (RT Unified)](#setting-a-user-data-type-version-as-default-rt-unified)
- [Creating tags with a HMI user data type (RT Unified)](#creating-tags-with-a-hmi-user-data-type-rt-unified)

### Creating an HMI user data type (RT Unified)

#### Introduction

You create an HMI user data type in the project library.

#### Requirement

- A project is open.
- The "Libraries" task card is displayed or the library view is open.

#### Procedure

To create an HMI user data type, follow these steps:

1. Click the "Libraries" task card.
2. Click the "Project library" entry.

   The folder structure of the project library is open.
3. Click "Add new type" in the "Types" folder.

   A dialog opens.

   ![Procedure](images/158895293707_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158895293707_DV_resource.Stream@PNG-en-US.png)
4. Click the "HMI user data type" button in the dialog box.
5. In the "Specify device for the new type" area, select the HMI device on which the HMI user data type is used.
6. Enter a descriptive name in the "Name" field.
7. Click "OK" to apply your settings. The HMI user data type is created. The library view opens.

#### Result

An HMI user data type with the configured properties is created. Version 0.0.1 of the HMI user data type is created and receives the status "in work".

Create the required user data type elements in the next step.

Before you use the version of an HMI user data type, for example at a tag, the version must be released.

### Creating HMI user data type elements (RT Unified)

#### Introduction

You add or delete user data type elements in the "HMI user data types" table.

#### Requirement

- The library view is open.
- An HMI user data type is created and opened in the editor.

#### Procedure

1. Select a communication driver for the HMI user data type.

   - If you select the &lt;Internal communication&gt; entry, you can only assign the HMI user data type to the internal tags as the data type.
   - If a connection to a PLC is selected as the communications driver, you can only assign the HMI user data type to tags with a connection to this PLC as the data type.
   - The configured communication driver applies to all user data type elements of an HMI user data type.
2. Double-click "Add" in the "Name" column of the table. A new user data type element is added to the HMI user data type.
3. Assign a name.
4. Select the required data type in the "Data type" field.
5. Create as many user data type elements as you need.
6. You configure the user data type elements in the "Properties" group of the Inspector window.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| You can also configure the properties of the user data type elements directly in the table. To view hidden columns, activate the column titles using the shortcut menu.   If you want to transfer a property of a user data type element to other user data type elements, follow these steps:  | Symbol | Meaning | | --- | --- | | 1. Select the cell that contains the property.    The selected cell will be highlighted in color and a small blue square will appear in its bottom right corner. 2. When you move the mouse over this square, the cursor will change to a black cross. 3. Hold down the mouse button and drag the cursor up or down over the cells that you want to fill out automatically.    The marking will be extended to cover this area. 4. Now release the mouse button.     The "Autocompletion" dialog opens. 5. Select the "Overwrite attributes of the user data type element" option. |  | |  |

#### Result

You have added elements to version 0.0.1 of the HMI user data type. The version 0.0.1 has the status "in work".

To use the version in the project, release the version.

### Adding a PLC user data type to the project library (RT Unified)

#### Introduction

You can use PLC data types in the HMI device.

#### Requirement

- A project is open.
- A PLC data type is configured in the PLC.
- The project view is open.
- The project library is open.

#### Procedure

1. Drag the PLC data type to the "Types" directory of the project library with a drag-and-drop operation.

   The "Add type" dialog opens.
2. Specify a type name and a version and click "OK" to confirm.

   In version 0.0.1, the PLC user data type appears in the project library.

#### Result

You have added the PLC user data type of the project library.

Version 0.0.1 of the PLC user data type was created and receives the status "default".

### Managing versions of user data types (RT Unified)

#### Introduction

All HMI user data types have at least one version. When an HMI user data type is created, a version is created at the same time; this version has the status "in work". You can edit the user data type in this status as required. When the editing is complete, you release the version of the HMI user data type. The latest released version is always used at the default.

#### Requirement

- An HMI user data type is created.
- The HMI user data type has the version 0.0.1. and the status "in work".
- The "Libraries" task card or the library view is open.

#### Releasing a version

1. Select the version 0.0.1 of the HMI user data type in the project library.
2. Select "Release version" in the shortcut menu.

   A dialog opens.
3. If necessary, change the properties of the version:

   - Enter a name for the type in the "Type name" field.
   - In the "Version" field, define a main and an intermediate version number for the version to be released.
   - To clean up version management of the type, enable "Delete unused type versions from the library".

You have released version 0.0.1 of the HMI user data type.

#### Editing a version

1. Select, for example, the released version 0.0.1 of an HMI user data type in the project library.
2. Select "Edit type" from the shortcut menu.

The library view opens. The new version 0.0.2 of the HMI user data type was created.

The version has the status "in work".

#### Restoring the last version of the HMI user data type

The last released version of the HMI user data type is version 0.0.2.

You edit the HMI user data type. A new version of the HMI user data type, 0.0.3, is generated and receives the status "in work".

1. Select the version of the HMI user data type in the project library.
2. Select "Discard changes and delete version" in the shortcut menu.

Alternatively

1. If you have opened a version for editing, click "Discard changes and delete version" in the toolbar.  
   The version is deleted.

All changes to the HMI user data type since the last release operation are discarded. The HMI user data type is released again and has version 0.0.2.

#### Deleting user data type

If you delete a user data type, all instances and master copies of this user data type are deleted as well. The same is true for HMI tags that use an HMI user data type and for PLC user data types.

To delete a user data type, follow these steps:

1. In the project library, under "Types", select the user data type you want to delete.
2. Select "Delete" from the shortcut menu.

---

**See also**

[Setting a user data type version as default (RT Unified)](#setting-a-user-data-type-version-as-default-rt-unified)

### Setting a user data type version as default (RT Unified)

When you add a user data type to a library, use data types from a library, and release or update versions, the highest released version is used as the default. This version has the "default" identifier. Alternatively, you can specify a different released version as default.

#### Requirements

- You have opened the project library or a global library.
- The desired type version is released.

#### Procedure

1. Select a version.
2. Right-click to call up the shortcut menu.
3. Select the shortcut menu command "Set as 'default'".

#### Result

When instantiating, creating, releasing and updating, the default user data type version is used instead of the highest released version. The default user data type version is also used when you create newer user data type versions.

The icon in the "Status" column shows whether the references of the type are consistent with other types:

- Green: The references of the user data type are consistent. The version of the user data type labeled "Default" references the "Default" user data type version of the dependent type.
- Yellow: The references of the user data type are inconsistent. The version of the user data type labeled "Default" does not reference the "Default" user data type version of the dependent type.

### Creating tags with a HMI user data type (RT Unified)

#### Introduction

When a tag is created, you assign the version of an HMI user data type as a data type. In the "Tag" editor you can create internal tags or tags with a link to a PLC. A tag provides all HMI user data type versions that use the same communication driver as the tag itself.   
You can only use an HMI user data type in combination with a PLC when you have selected absolute addressing.

#### Requirement

- An HMI user data type with a user data type element is created.
- The HMI user data type is released.
- The tag table is open.
- The Inspector window with the tag properties is open.

#### Procedure

To create a tag of the "User data type" data type, follow these steps:

1. In the "Name" column, double-click "Add" in the tag table. A new tag is created.
2. Enter a unique tag name in the "Name" field.
3. Select the connection to the required PLC in the "Connection" box.
4. Select the desired version of the HMI user data type in the "Data type" field.

   The selected connection determines which HMI user data types are displayed.

   For internal tags, only HMI user data type versions of the &lt;Internal user data type&gt; type are available.

   ![Procedure](images/158898974859_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/158898974859_DV_resource.Stream@PNG-en-US.png)
5. In the "Address" field, enter the address of the PLC that you want to access with the external tag. The specified address must always point to the start data bit, for example, &lt;DB1.DBX0.0&gt;.

**Note**

For tags with a connection to a PLC, only those HMI user data types that have a link to a PLC are available.

#### Result

You have created a tag of the "User data type" data type. In additional steps you can configure the tag, for example, by setting the start value and limits.

If you wish to change the properties of an HMI user data type tag, you must change the properties of the HMI user data type elements.

Properties, such as "Start value" and "Linear scaling", can also be changed in the HMI user data type instances used.

## Logging tags (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Configuring logging tags (RT Unified)](#configuring-logging-tags-rt-unified)
- [Configuring multiple logging tags (RT Unified)](#configuring-multiple-logging-tags-rt-unified)
- [Configuring tag triggers (RT Unified)](#configuring-tag-triggers-rt-unified)
- [Configuring limit values (RT Unified)](#configuring-limit-values-rt-unified)
- [Configuring smoothing (RT Unified)](#configuring-smoothing-rt-unified)
- [Configuring compression (RT Unified)](#configuring-compression-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Basics of data logging (RT Unified)](#basics-of-data-logging-rt-unified)
- [Size of a log entry in the data log (RT Unified)](#size-of-a-log-entry-in-the-data-log-rt-unified)
- [Logging modes and logging process (RT Unified)](#logging-modes-and-logging-process-rt-unified)

#### Basics of data logging (RT Unified)

##### Introduction

Data logging is used to collect and log process data from an industrial system. This allows you to analyze error statuses and document your process.

From the archived process data, you extract important business and technical information about the operating status of a plant in an evaluation.

##### Logging concept

WinCC Unified is optimized for event-driven logging. The process values are saved by configured events and selected processing mechanisms in the data log. Event-driven logging does not depend on the logging mode.

In the past, we have used query-driven logging. This method saved the values at fixed cycles without additional processing in the log. You can map query-driven logging by using the "Cyclic" logging mode and by not configuring any smoothing or compression. The procedure is not recommended.

Event-driven logging offers the following advantages compared to query-driven logging:

- High accuracy

  Note that logging can only be as precise as the data acquisition at the PLC.
- High performance because fewer values must be logged

If you need a query-driven representation of the values for data evaluation, we recommend that you use event-driven logging and then interpolate the missing values.

##### Configuration

You configure the logging tags in the "Logging tags" tab in the "HMI tags" editor.

You use logging tags in the following controls in Runtime:

- Trend control
- f(x) trend control
- Process control

##### Use

You can use data logging for the following tasks:

- Early detection of danger and fault conditions
- Increase of productivity
- Increase of product quality
- Optimization of maintenance cycles
- Documentation of process value trends

---

**See also**

[Log basics (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#log-basics-rt-unified)
  
[How it works (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#how-it-works-rt-unified)
  
[Storage locations of logs (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#storage-locations-of-logs-rt-unified)
  
[Creating a data log and an alarm log (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#creating-a-data-log-and-an-alarm-log-rt-unified)
  
[Editing log contents with scripts and system functions (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#editing-log-contents-with-scripts-and-system-functions-rt-unified)
  
[Size of a log entry in the data log (RT Unified)](#size-of-a-log-entry-in-the-data-log-rt-unified)

#### Size of a log entry in the data log (RT Unified)

The size of a log entry depends on the database type used.

The following values result for the data log:

|  | SQLite | Microsoft SQL |
| --- | --- | --- |
| Additional memory requirement per segment | Approx. 0.5 MB | Approx. 5 MB |
| Size of a log entry | Approx. 50 bytes | Approx. 50 bytes |

##### Recommended use of database types

The use of Microsoft SQL is recommended for data logs under the following conditions:

- Number of tag value changes to be logged greater than 500 per second
- More than 1.3 billion log entries must be available (excluding deleted log segments in backup)

---

**See also**

[Basics of data logging (RT Unified)](#basics-of-data-logging-rt-unified)
  
[How it works (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#how-it-works-rt-unified)

#### Logging modes and logging process (RT Unified)

Logging begins when Runtime starts. The process values to be logged are acquired, processed, and saved in the data log. Current or previously logged process values can be output in runtime.

Three logging modes are available for logging tags:

- On change: When the process value changes, it is logged.
- On demand: When the tag trigger is triggered, the process value is logged.
- Cyclic: Logging is carried out according to a defined cycle.

The amount of logged data can be reduced due the following processing mechanisms:

- Limits
- Smoothing
- Compression

  When you select an existing logging tag as source, the values are compressed with the selected compression mode.

Data logging ends when runtime is terminated.

##### Logging process

![Logging process](images/143765205515_DV_resource.Stream@PNG-en-US.png)

##### "On change" logging mode

When the process value changes, the process value is saved in the data log in the "On change" logging mode while runtime is running. You can also define a tag trigger.

- The acquisition cycle of the external tags controls when the process value is read from the memory of the connected PLC.

  The external tags in WinCC correspond to a process value in the memory of a connected PLC.
- When the process value changes, the runtime component of the logging system processes the process value.
- If you have configured smoothing, the value is calculated accordingly.
- The processed process value is written to the data log.

For defined tag triggers, the tag is also logged when the trigger occurs.

##### "On demand" logging mode

- The process value is read from the PLC when the request by the tag trigger occurs.

  The external tags in WinCC correspond to a process value in the memory of a connected PLC.
- If you have configured smoothing, the value is calculated accordingly.
- The processed process value is written to the data log.
- With each new request by the tag trigger, the process value is read, processed and logged again from the memory of the connected PLC.

##### "Cyclic" logging mode

The process values are recorded in constant cycles and stored in the data log. You have the option of using a predefined cycle or a user-defined cycle.

The process value is only logged if it differs from the previous value. If every value is to be logged, no smoothing and no compression must be configured for the logging tag.

> **Note**
>
> Depending on the configuration, the database can grow very quickly. This can occur, for example, when you select a short cycle without smoothing and without compression.

- The acquisition cycle of the external tag controls when the process value is read from the memory of the connected PLC.

  The external tags in WinCC correspond to a process value in the memory of a connected PLC.
- If you have configured smoothing or compression, the value is calculated accordingly.
- The logging cycle determines when the processed process value is written to the log database.

> **Note**
>
> The logging cycle is independent of the acquisition cycle of the external tag. It does not make sense to set the logging cycle shorter than the acquisition cycle.

### Configuring logging tags (RT Unified)

#### Introduction

You manage the logging tags at various locations:

- You have the following options in the "HMI tags" editor:

  - Create logging tags
  - Edit logging tags
  - Delete logging tags
- You have the following options in the "Logs" editor:

  - Edit logging tags
  - Delete logging tags

> **Note**
>
> **Logging tags are deleted**
>
> Logging tags are deleted with the following actions and must be recreated:
>
> - The logging tag is assigned to an array element. The data type of the array is changed.
> - The logging tag is assigned to a user data type element. The data type of the user data type element is changed, and a new version is released without updating the associated instances. The new version of the user data type is assigned to the tag manually in the "HMI tags" editor.

> **Note**
>
> **Local session tags**
>
> Local session tags cannot
>
> - be used as a trigger
> - be used as an logging tag
> - be logged.

#### Requirement

- The "HMI tags" editor is open.
- The logging tag tab is expanded.
- You have created a tag.

#### Procedure

1. Select an existing tag in the tag table.
2. In the table of the "Logging tag" editor table, double-click "&lt;Add&gt;" in the "Name" column.

   A new logging tag is created.

   The logging tag is linked to the selected tag. The data type of the logging tag corresponds to the data type of the higher-level tag.

   ![Procedure](images/136207635979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/136207635979_DV_resource.Stream@PNG-en-US.png)
3. Assign a data log to the new logging tag. Every logging tag can be assigned to another log.
4. Specify the logging mode.
5. When the "Cyclic" logging mode is set, define the logging cycle and the factor under "Properties &gt; Properties &gt; Cycle".

   The product of logging cycle and factor determines the time interval between two logs. For example, if you define "1 second" as the time basis and "5" as the time factor, the process values are logged every 5 seconds.

   The factor is a multiplier for the duration of the configured logging cycle.

   The factor is used to reduce the number of cycle times. Cycle times that you configure are used for the acquisition cycle and the logging cycles to acquire and then log the measured values. As the different measured values are acquired and logged with different cycle times, different times must also be defined. The factor reduces the number of defined times. This means that times with factor are used several times. A logging cycle of 120 s with factor = 1 corresponds to a logging cycle of 60 s with factor = 2. Both measured values are logged every 120 s.
6. Define the tag trigger depending on the logging mode.
7. Define the limit values.
8. Define the smoothing.
9. If you have selected the "Cyclic" logging mode, define the compression.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You can also configure the properties of the logging tags directly in the logging tags table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Copying logging tags

You can copy logging tags within an HMI device. To do this, use the shortcut menu or the shortcuts &lt;Ctrl + C&gt; and &lt;Ctrl + V&gt;.

You copy logging tags, for example, from:

- "HMI tags" editor
- "Logs" editor
- Data source of a control in which logging tags are used

You insert logging tags, for example, at the following locations:

- "HMI tags" editor
- Data source of a control in which logging tags are used

> **Note**
>
> If you hare using cascading logging tags by having defined a source under "Compression", the reference becomes invalid due to the copy process. Redefine the source for the inserted logging tag.

---

**See also**

[Creating a data log and an alarm log (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#creating-a-data-log-and-an-alarm-log-rt-unified)
  
[Configuring tag triggers (RT Unified)](#configuring-tag-triggers-rt-unified)
  
[Configuring limit values (RT Unified)](#configuring-limit-values-rt-unified)
  
[Configuring smoothing (RT Unified)](#configuring-smoothing-rt-unified)
  
[Configuring compression (RT Unified)](#configuring-compression-rt-unified)

### Configuring multiple logging tags (RT Unified)

#### Introduction

You can create multiple logging tags at the same time in the "HMI tags" editor. Then you adapt the properties of multiple logging tags by automatic filling. This will shorten the configuration time.

You edit and delete the logging tags in the "HMI tags" editor or in the "Logs" editor.

#### Requirement

- Multiple tags are configured.
- A tag table is open.

#### Procedure

1. Select multiple tags of the tag table.

   If you have already configured logging tags, all logging tags that are assigned to the selected tags are displayed.
2. Select the button "Add new logging tag to each selected loggable tag".

   A tag is added to each selected tag that can be archived.
3. When you want to transfer a property of a logging tag to other logging tags, select the cell that contains this property.

   The selected cell will be highlighted in color and a small blue square will appear in its bottom right corner.
4. When you move the mouse over this square, the cursor will change to a black cross.
5. Hold down the mouse button and drag the cursor up or down over the cells that you want to fill out automatically.

   The marking will be extended to cover this area.

   ![Procedure](images/136228740363_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/136228740363_DV_resource.Stream@PNG-en-US.png)
6. Now release the mouse button.

   All of the marked cells are filled automatically.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| For a better overview, you can sort the columns of the logging tag table in ascending or descending order. To do this, click on the column title. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

- You have created multiple logging tags.
- You have defined the properties of the logging tags through automatic filling.

  If properties for individual logging tags cannot be applied, the previous values are retained.

### Configuring tag triggers (RT Unified)

#### Introduction

When you use the "On demand" and "On change" logging modes, you have the option of defining a tag trigger. In the "On demand" logging mode, you log the tags regardless of the value change, and you can trigger logging, for example, at the end of a process or a shift. When the defined bit of the trigger tag changes according to the defined mode, the tag is logged.

#### Requirement

- You have created a logging tag.
- The logging mode "On demand" or "On change" is defined for the logging tag.

#### Procedure

1. Select an existing logging tag in the "Logging tags" tab.
2. In the Inspector window under "Properties &gt; Properties", select the "Tag trigger" area.
3. Specify a trigger mode:

   - None: The tag trigger is not used.
   - Rising edge: When the bit changes from 0 to 1, the trigger is triggered.
   - Falling edge: When the bit changes from 1 to 0, the trigger is triggered.
   - Rising and falling edge: When the bit changes from 0 to 1 or from 1 to 0, the trigger is triggered.
4. Define the trigger tag.
5. Specify the bit that is to be considered.

**Note**

Local session tags cannot be used as triggers.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You can also configure the tag trigger directly in the logging tags table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

You have defined a tag trigger that triggers logging.

---

**See also**

[Configuring logging tags (RT Unified)](#configuring-logging-tags-rt-unified)

### Configuring limit values (RT Unified)

#### Introduction

You have the option of archiving tag values outside or within a defined limit scope. To do this, define a valid range and the corresponding limit values. In runtime, the process values are evaluated after the configured limit scope and only the process values within the defined range are logged.

#### Limit scope

The following limit scopes are available:

| Limit scope | Description | Example |
| --- | --- | --- |
| No limits | No limit values are defined for logging. | Limit values are not taken into consideration. |
| Greater | The process values that are greater than the lower limit value are logged. | Low limit =3;  Logged values = 4, 5, 6 |
| Less | Only the process values that are less than the high limit are logged. | High limit =6;  Logged values = 3, 4, 5 |
| Greater or equal | Only process values that are equal to or greater than the lower limit are logged. | Low limit =3;  Logged values = 3, 4, 5, 6 |
| Less or equal | Only the process values that are equal to or less than the high limit are logged. | High limit =6;  Logged values = 3, 4, 5, 6 |
| Within limits | Only the process values that are within the two configured limits are logged. | Low limit = 3, high limit = 6;  Logged values = 4, 5 |
| Within or equal | Only the process values that are within the two limits or equal to one of the limit values are logged. | Low limit = 3, high limit = 6;  Logged values = 3, 4, 5, 6 |
| Outside limits | Only the process values that are outside of the two configured limits are logged. | Low limit = 3, high limit = 6;  Logged values = 1, 2, 7, 8 |
| Outside or equal | Only the process values that are outside the two limits or that correspond to one of the limit values are logged. | Low limit = 3, high limit = 6;  Logged values = 1, 2, 3, 6, 7, 8 |

#### Requirement

- You have created a logging tag.

#### Procedure

1. Select an existing logging tag in the "Logging tags" tab.
2. In the Inspector window under "Properties &gt; Properties", select the "Limit values" area.
3. Specify the limit values. You have the following options:

   - Use constants.

     Select "Constant" using the selection button.

     Enter a number in the relevant field.
   - Use HMI tags.

     Select "HMI tag" using the selection button.

     Open the selection dialog. Only tags that correspond to the data type of the logging tag are displayed. Local session tags are not permitted.

     Select a tag.
   - Apply the limit values of the associated HMI tag.

     Activate "Use tag limits".

     The limit values of the HMI tag are used and grayed out in the corresponding fields.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You can also configure the limits directly in the logging tags table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

You have specified a value range for the selected logging tag that is defined by the limit values.

---

**See also**

[Configuring logging tags (RT Unified)](#configuring-logging-tags-rt-unified)

### Configuring smoothing (RT Unified)

#### Introduction

You can compress the data volume of the logged data using smoothing to reduce the memory space required. Smoothing reduces the noise in the collected data.

The process values are only logged in accordance with certain predefined criteria.

> **Note**
>
> **Smoothing**
>
> If the value "No smoothing" is set in the properties of the logging tag under "Smoothing &gt; Mode", the values are nevertheless smoothed.
>
> **Example:**
>
> A logging tag changes its value as follows: "100" &gt; "101" &gt; "101".
>
> Even if "No smoothing" is set in the properties of the tag, the values [100, 101] are logged.

#### Requirement

- You have created a logging tag.

#### Procedure

Select one of the following modes:

- No smoothing

  The values are logged without smoothing.
- Comparing values

  Values are logged when the value changes and/or the quality code is changed. No logging is triggered when only the time stamp changes.
- Value

  You specify a limit value that defines the maximum permitted distance between the values. All value changes occurring within the defined interval from the last logged value are not logged.
- Relative value

  You specify a percentage deviation that defines the maximum interval between the values. All value changes occurring within the defined interval relative to the last logged value are not logged.

  Example:

  - You define a deviation of 10%, the last logged value is 100.
  - The value 105 is not logged because the value change is less than 10%. On the other hand, the value 130 is logged because the value change is more than 10% and is therefore relevant for logging.
- Swinging door

  The Swinging Door algorithm is a combination of value-based and time-based smoothing.

  The swinging door algorithm evaluates values on the basis of the defined rate of change and only logs them if the following value is outside the calculated range. The compression rate depends on the maximum tolerated deviation. The deviation is set as an absolute value.

  ![Procedure](images/160342945035_DV_resource.Stream@PNG-de-DE.png)

  | Symbol | Meaning |
  | --- | --- |
  | t | Time interval between received values |
  | d | Configured deviation |
  | v<sub>0</sub> | Previously logged value |
  | v<sub>1</sub> | Current value |

  The starting point for calculating the next logging time is the last value logged.

  Using the set deviation, you can influence the precision with which the values are saved. The greater the deviation, the fewer values are logged. Values for which "Deviation is within the tolerated deviation" is true are not taken into account.

  With the maximum time, you specify the time after which a new value will definitely be logged. This specifies additional reference values for the logged data even if no significant changes occur during this time. With the minimum time, you specify the time interval after which the next value for logging is calculated. All measured values within the minimum time are not logged.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You can also configure smoothing directly in the logging tags table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Example – Smoothing with the value

You specify a constant value for the deviation. All values that are within the defined deviation and have not changed significantly are not logged.

Only the values outside the deviation are written to the log.

![Example – Smoothing with the value](images/102442248587_DV_resource.Stream@PNG-de-DE.png)

#### Example – Swinging door with deviation and maximum time

You define the deviation and the maximum time after which the next value is written to the log.

Once the first value has been saved, the following values are evaluated in the pre-defined rate of change. If the value is within the rate of change, it is not logged. If the value is outside the deviation, it is logged. In addition, the values that do not have a significant change compared to the previous logging value are logged at regular defined intervals.

![Example – Swinging door with deviation and maximum time](images/102474902923_DV_resource.Stream@PNG-de-DE.png)

#### Example – Swinging door with deviation and minimum time

You define the deviation and the minimum time after which the next value is to be evaluated in runtime.

Once the first value has been saved, the next value for logging in runtime is calculated after the preset time. If the value is within the rate of change, it is not logged. If the value is outside the deviation, it is logged.

![Example – Swinging door with deviation and minimum time](images/102475274379_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Configuring logging tags (RT Unified)](#configuring-logging-tags-rt-unified)

### Configuring compression (RT Unified)

#### Introduction

In the "Cyclic" logging mode, you can compress the data volume of the logged data using compression to reduce the memory space required.

If you have selected "Cyclic" as logging mode, runtime logs the tag values according to the logging cycle, the defined smoothing and the defined compression.

Various compression modes are available.

#### Supported data types

The following table shows which compression mode supports which data types. You can see from the table in which data type the source data is converted by compaction. A "==" means that the source data type remains unchanged.

|  | Compression mode |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Data type** | **No compression** | **Minimum** | **Maximum** | **Minimum with time stamp** | **Maximum with time stamp** | **Total** | **Average** | **Time average sloped step by step** | **End** |
| Bool | == | Not supported | Not supported | Not supported | Not supported | Not supported | LReal | LReal | == |
| SInt | == | == | == | == | == | LInt | LReal | LReal | == |
| USInt | == | == | == | == | == | ULInt | LReal | LReal | == |
| Int | == | == | == | == | == | LInt | LReal | LReal | == |
| UInt | == | == | == | == | == | ULint | LReal | LReal | == |
| DInt | == | == | == | == | == | LInt | LReal | LReal | == |
| UDInt | == | == | == | == | == | ULInt | LReal | LReal | == |
| LInt | == | == | == | == | == | Not supported | Not supported | Not supported | == |
| ULInt | == | == | == | == | == | Not supported | Not supported | Not supported | == |
| Real | == | == | == | == | == | LReal | LReal | LReal | == |
| LReal | == | == | == | == | == | LReal | LReal | LReal | == |
| String | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| Time | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| DateTime | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| Char | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| Byte | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| Word | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| DWord | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |
| LWord | == | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | == |

> **Note**
>
> Note the following when configuring the cycle and the compression:
>
> - You can overload the processor if you use short cycles and compression. Make sure that the computing power of the processor is sufficient to calculate the values to be logged for each cycle.
> - Depending on the configuration, the database can grow very quickly. This can occur, for example, when you select a short cycle in combination with the smoothing mode "No smoothing" and the compression mode "No compression".

#### Requirement

- You have created a logging tag.
- The "Cyclic" logging mode is defined for the logging tag.

#### Procedure

| 1. Select one of the following modes:       | Compression mode | Description |    | --- | --- |    | No compression | Every value is logged. Logging receives a time stamp of the interval end. Examples: - If you have not defined any smoothing, every value is logged. - If you have defined the "Compare values" smoothing mode, the value is only logged when the value changes and/or the quality code is changed. |    | Minimum | The minimum of the values determined within the logging interval, including the start value, is logged. The logging receives a time stamp of the interval start. |    | Maximum | The maximum of the values determined within the logging interval, including the start value, is logged. The logging receives a time stamp of the interval start. |    | Minimum with time stamp | The minimum of the values determined within the logging interval, including the start value, is logged. Unlike in the "Minimum" mode, in this mode the logged minimum value receives the time stamp of its occurrence. |    | Maximum with time stamp | The maximum of the values determined within the logging interval, including the start value, is logged. Unlike in the "Maximum" mode, in this mode the logged maximum value receives the time stamp of its occurrence. |    | Total | The total of all values determined within the specified logging interval is logged without the start and end values. |    | Average | The average value of all values determined within the specified logging interval is logged without the start and end values. |    | Time average sloped step by step | The time-weighted average value of all values determined within the specified logging interval without start and end value is logged. |    | End | The last value determined within the specified logging interval is logged. The logging receives a time stamp of the interval start. Examples: - If you have not defined any smoothing, the zero value and the quality code "NoData" will be logged when there are no value changes. - If you have defined the "Compare values" smoothing mode, the value is only logged when the value changes and/or the quality code is changed. |       | Symbol | Meaning |    | --- | --- |    | **Note**  Each value is logged when you select "No smoothing" for the smoothing mode in combination with the compression mode "No compression". This will quickly increase the log size. |  | 2. You have the option of defining a delay. The delay value defines the latest possible time up to which the compression value is logged after the end of a logging cycle. If the time stamp of a value is after the delay value, the value is not logged. 3. Under "Source", you can select an existing logging tag whose values are to be compressed with the selected compression mode. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| You can also configure compression directly in the logging tags table. To view hidden columns, activate the column titles using the shortcut menu. |  |

#### Result

You have configured compression for a logging tag.

---

**See also**

[Configuring logging tags (RT Unified)](#configuring-logging-tags-rt-unified)

## Displaying tags (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-2)
- [Configuring a trend control (RT Unified)](#configuring-a-trend-control-rt-unified)
- [Configuring the function trend control (RT Unified)](#configuring-the-function-trend-control-rt-unified)
- [Configuring bit-triggered trends (RT Unified)](#configuring-bit-triggered-trends-rt-unified)
- [Configuring the process control (RT Unified)](#configuring-the-process-control-rt-unified)
- [Configuring the trend companion (RT Unified)](#configuring-the-trend-companion-rt-unified)
- [Configuring the toolbar and information bar (RT Unified)](#configuring-the-toolbar-and-information-bar-rt-unified)
- [Defining the data source (RT Unified)](#defining-the-data-source-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Outputting the tag values (RT Unified)](#outputting-the-tag-values-rt-unified)
- [Outputting tag values as trends (RT Unified)](#outputting-tag-values-as-trends-rt-unified)
- [Representing multiple trends (RT Unified)](#representing-multiple-trends-rt-unified)
- [Basics of time range (RT Unified)](#basics-of-time-range-rt-unified)
- [Representing trend directions (RT Unified)](#representing-trend-directions-rt-unified)
- [Outputting tag values in tabular format (RT Unified)](#outputting-tag-values-in-tabular-format-rt-unified)
- [Configuring tag evaluation (RT Unified)](#configuring-tag-evaluation-rt-unified)

#### Outputting the tag values (RT Unified)

##### Overview

With WinCC you can output tag values in the HMI screen with different screen objects and change them.

- The I/O field is used for the input and output of process values.
- Bars are used for graphic display of the process values in form of a scale.
- Sliders are used for the input and output of process values within a defined range.
- The gauge is used to display the process values in form of an analog gauge.

In runtime you can also output tag values as table or as trend. You can use either process values or logged values as source for the tag values.

- Use a trend for the graphic display of tag values. Trends allows you to display the change in motor temperature, for example.
- Use a table to compare tag values. In the table you can, for example, compare fill levels of supply tanks.

##### Controls for displaying tag values

To display tag values as a trend, use the trend control. The versions of trend views are available:

- "Trend control": You display a tag value over time, for example, the change in temperature. You can compare the current values and logged values or monitor the change in current values on the HMI device.
- "Function trend control": You display a tag value against a second tag value, for example, the engine speed against the heat produced.

You can use the "Trend companion" to create statistics, for example, from the displayed values. Furthermore, you can use the trend companion as reading assistance for the trend control.

To display tag values in a table, use the process control.

![Controls for displaying tag values](images/104046995723_DV_resource.Stream@PNG-de-DE.png)

##### Displayed values

When configuring the trend control, specify which tag values are to be displayed.

- "Online": The trend is continued with current individual values from the PLC.
- "Log": In runtime, the trend control displays the values of a tag from a data log. The trend shows the logged values in a particular window in time. The operator can move the time window in runtime to view the desired information from the log.

##### Data types

Tags of the data type "Word" or "Int" and array tags of the data type "Word" or "Int" are permitted for display in a curve.

#### Outputting tag values as trends (RT Unified)

##### Introduction

You have the option of displaying the values of tags graphically in runtime with the help of the following controls:

- You can visualize the trend control to display currently pending process values or logged values in runtime as trends over time.
- You use the function trend control to visualize currently pending process values or logged values in runtime as trends in relation to other tags.

The axis designations are different for the two trend views:

- The trend control has a "Time axis" and a "Value axis"
- The function trend control has an "X axis" and a "Y axis"

You can display up to nine trends in both the function trend control and the trend control.

##### Structure of a trend control

Configure the trend control appearance in the Inspector window: You define the number of trend areas and configure the trends it contains.

You can configure multiple trends, value axes and time axes for each trend area. You can alter the appearance, labeling and assignment in the Inspector window for each individual trend, value axis and time axis created.

##### Configure trend areas

You can divide the display area into multiple trend areas, if necessary. Each area functions like a standalone trend control. This allows you to show temperature changes or values from different days, for example, as trends and compare them. The "Range proportion" specifies how much space is provided for a given area in the trend control.

Each range proportion is calculated on the basis of the total number of range components. If you have configured a total of three trend areas, for example, a range proportion of "1" will result in three trend areas of equal size. To increase the range proportions in relation to each other, increase the range proportion of one or more trend areas.

##### Configuring axes

You configure the axes of the trend control for each trend area in the properties of the trend areas.

The following properties are set by default with a value axis:

- The value range is based on the current values of the assigned trend
- The value axis scale is linear and based on the value range

  Alternatively, you can configure a logarithmic scale:

  - In logarithmic scaling, only positive values are displayed.
  - In negative logarithmic scaling, only negative values are displayed.

If you configure a value axis for the trend control, you can also set up axis segments. You assign a value range and a display name to each axis segment.

In the function trend control, the value axis corresponds to both the "X axis" and the "Y axis".

##### Configuring trends

You configure the axes for each trend area:

- The time and value axes in the trend control
- The different value axes in the function trend control

By default, the data area is based on the current values of the associated trend.

You can also configure the visualization of limits and values with "Uncertain status" for a trend. If a trend exceeds or falls below a configured limit, the trend is colored.

##### Configuring the time axis and time range (trend control)

The time range for trend display is configured with time axes. In a trend control, you can create multiple time axes that you can assign to one or more trend areas.

If you configure several time axes to a trend control, the sequence of the time axes in the Inspector window corresponds to the sequence in the trend control. If multiple time axes run along the same side of a trend control, the first time axis in the list is at the bottom left. The last time axis is at the top right.

#### Representing multiple trends (RT Unified)

##### Introduction

If you display several trends simultaneously in the trend control, assign each trend its own value and time axis. Alternatively, you can assign a shared time and/or value axis to several trends.

You configure the axes of a trend control for each individual trend in the Inspector window under "Properties &gt; Trend areas".

The axes are assigned to the configured trends in the Inspector window under "Properties &gt; Trend areas &gt; Trends".

##### Representation using different axes

If the values to be displayed in a trend control differ greatly, a common value axis makes no sense. If you assign each trend its own value axis, they should also display different scales. Individual axes can be hidden if required.

The figure below shows two trends with different value axes using a trend control as an example:

![Representation using different axes](images/103918373643_DV_resource.Stream@PNG-de-DE.png)

##### Representation using common axes

If the comparability of the trend directions is important, common axes in a trend control is sensible. Connected trend views can have a common time axis.

If you configure trends with a shared time axis, use tags with the same update cycle for the data supply.

In the case of different updating cycles, the length of the time axis is not identical for all tags. Since the trends are updated at different times due to the different updating cycles, a minimal different in the end time for the time axis occurs on each change. As a result, the trends displayed skip slightly to and fro on each change.

![Representation using common axes](images/103894744587_DV_resource.Stream@PNG-de-DE.png)

#### Basics of time range (RT Unified)

##### Time range

The time range is the range from which the values at the HMI device are shown. The time range is determined by the start time and the end time. The time range is always in the past. If the end time is later than the current system time, the current system time is used as a temporary end time.

A distinction is made between the following time ranges:

- Static time range
- Dynamic time range

##### Static time range

The static time range is determined by fixed start and end times. The values are displayed within this time range.

##### Dynamic time range

The dynamic time range is determined by a period of time beginning with a fixed start time. The end time thus corresponds to the conclusion of the time period.

You set the time period as follows:

- Duration, e.g. 30 minutes
- The number of measurement points multiplied by the update cycle also produces a duration.

##### Configuring time range

Configure the time range for all controls. Configure the time range in the time column or in the time axis for the process control and the trend control. For the function trend control, configure the time range directly at the trend.

You select one of three options for the time range:

- "Time span": You define the time range using a starting time and a following time span. You set the time interval with the settings "Time range base" and "Time range factor", for example, 30 minutes.
- "Start time and end time": You define the time range using a starting time and an end time.
- "Measuring points": You define the time range using a starting time and a number of measuring points.

#### Representing trend directions (RT Unified)

##### Introduction

In a trend control, you display a trend direction with one of the following modes:

- Dots
- Interpolated
- Stepped
- Values

Select "Properties &gt; Trend areas &gt; Trends &gt; Trend mode" to configure the trend display in the Inspector window.

##### Dots

Values are shown as dots. The display of the points can be configured as you wish.

The following image shows the trend direction with the format pattern "Dots":

![Dots](images/23382216459_DV_resource.Stream@PNG-de-DE.png)

##### Interpolated

The trend curve is interpolated on a linear basis from the values. The display of the lines and points can be configured as you wish.

The following image shows the trend direction with the format pattern "Interpolated":

![Interpolated](images/23381142027_DV_resource.Stream@PNG-de-DE.png)

##### Stepped

The trend curve is interpolated as a stepped curve from the values. The display of the lines and points can be configured as you wish.

The following image shows the trend direction with the format pattern "Stepped":

![Stepped](images/23382076043_DV_resource.Stream@PNG-de-DE.png)

##### Values

The values are displayed as text at each time stamp or each main grid line of the time axis. A unit can be displayed additionally for the values.

The figure below shows the trend direction with the format pattern "Values":

![Values](images/33854050955_DV_resource.Stream@PNG-de-DE.PNG)

#### Outputting tag values in tabular format (RT Unified)

##### Introduction

To display tag values in tables in runtime, add a process control to a screen. A time stamp is displayed for each value. The values are displayed in value columns, and the time stamps in time columns. Assign the time column to one or several value columns. You have the option of configuring a time column and nine value columns in the process control.

If you assign multiple value and/or time columns to a process control, the sequence of columns in the Inspector window corresponds to the sequence in the process control. If you assign the same time column to multiple value columns, the value columns in the list are automatically grouped according to the assigned time column.

- The time range for the table display is configured using the time column. A table has a common time column for multiple value columns. The first column [0] in the process view of the process control is the time column.
- You configure the values of the process control using value columns. You can display several value columns in a table, for example to compare the fill levels of several containers. Each value column is connected to the time column.

##### Configuration options in the process control

You can configure the following properties in the process control in line with your requirements:

- Configure the appearance of the process control:

  - Colors
  - Time base
  - Window settings of the control
- Configure the columns of the process control in the Inspector window.

  - Configure the time range using the time columns. A table can have a common time column for multiple value columns as well as separate time columns.
  - Configure the display of the tag values using the value columns. Each value column is connected to a time column. The value columns can have a common time column.
- Configure the appearance of the table
- Configure the toolbar and information bar of the process control.
- If required, configure data export from the process control.

#### Configuring tag evaluation (RT Unified)

##### Introduction

Also configure a trend companion if you want to evaluate data from the trend control in runtime. You can also configure the trend companion as "Ruler".

You connect the trend companion to one of the following controls:

- Trend control
- Function trend control

Set a "Display mode" in the trend companion. The display mode determines which data is shown in the trend companion.

The contents of the trend companion are shown in columns. The available columns depend on the connected control. A block is assigned to each column. You define the alignment and appearance of the column headers using the blocks. By default, the format of the connected control, for example the time display, is used for the display format.

##### Configuration options in the trend companion

You can configure the following properties in the trend companion in line with your requirements:

- Configure the view of the trend companion in the Inspector window:
- Select the "Mode" of the trend companion under "Properties &gt; General".
- Configure the display, labeling and sequence of the columns.

##### Display modes

Three different display modes are available in the trend companion:

- Ruler mode

  The ruler window shows the coordinate values of the trends on the ruler or values of a selected row in the table.
- Statistics area mode

  The statistics area window shows the values of the lower limit and upper limit of the trends between two rulers or the selected area in the table. You can only connect the statistics area window to the trend control or the process control.
- Statistics mode

  The statistics window displays the statistical evaluation of the trends. The statistics include:

  - Minimum
  - Maximum
  - Average
  - Standard deviation
  - Integral

All windows can also display additional information on the connected trends or columns, such as time stamps.

### Configuring a trend control (RT Unified)

#### Introduction

For the graphic display of tag values in runtime, add a trend control to a screen. The trend control allows you to display current and logged values for a specific time window, for example. For the display of data logs in runtime, you can move the time window to view the logged values.

The list of elements in a group always starts with 0, for example trend [0] is the first trend that has already been created in the object. For a clearer display of multiple trends, you can configure different names, line types and colors.

#### Requirement

- Data log with backup has been configured.
- The HMI tag for temperature measurement has been configured, for example "MotorTemperature".
- The HMI tag for velocity measurement has been configured, for example "MotorSpeed".
- A screen has been configured.

#### Configuring the trend area and axes

1. Add the "trend control" object to the screen from the "Toolbox" task card.
2. Go to "Properties" and set the required height, width and position of the object.
3. Open the "Trend areas" group under "Properties".

   The index numbers of the trend areas created for the object are displayed.
4. Expand the index number of the first trend area.

   The properties of the first trend area are displayed.
5. Define the colors for displaying the trend area and the reference lines.
6. Configure the time axis and value axis settings under "Bottom time axis" and "Left value axis".

**Note**

To add another trend area, go to "Properties &gt; Trend areas &gt; [0] trend areas &gt; Trends" and click the selection button in the "Static value" column. In the dialog, click "Add".

#### Configuring trends

1. Go to "Trend areas &gt; [0] trend areas &gt; Trends" and click on the selection button in the "Static value" column.

   A dialog opens.
2. Click "Add" in the "Index" column.

   This adds another trend. Close the dialog.
3. Expand the index number of the first trend [0]. The trend settings are displayed.
4. Specify the name of the first trend under "Display name", for example "Speed".
5. Select the entry "Online" under "Data source Y &gt; Source".
6. Under "Tag" enter the tag "MotorSpeed".
7. Configure the line color for the trend, for example, blue.
8. Expand the index number of the second trend [1]. The trend settings are displayed.
9. Specify the name of the second trend under "Display name", for example "Temperature".
10. Specify "Online" as the source type under "Data source" and enter the name of the tag "MotorTemperature".
11. Configure the line color for the trend, for example, red.

#### Result

The trend control is now configured. In runtime, you monitor value changes over time on the basis of two trends. One trend shows the temperatures measured and the other trend the velocity.

Configure an additional value display if you want to evaluate the data of the trend control in runtime. You can also configure the value display as a "Ruler".

---

**See also**

[Trend control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#trend-control-rt-unified)
  
[Configuring trend control for plant objects (RT Unified)](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#configuring-trend-control-for-plant-objects-rt-unified)

### Configuring the function trend control (RT Unified)

#### Introduction

You use the function trend control to represent the values of a tag as a function of another tag. This means that you can present temperature trends as a function of the velocity, for example.

You can also compare the trend to a setpoint trend.

#### Requirement

- Data log with backup has been configured.
- The HMI tag for temperature measurement has been configured, for example "MotorTemperature".
- The HMI tag for velocity measurement has been configured, for example "MotorSpeed".
- A screen has been configured.

#### Configuring function trend areas and axes

1. Add the "trend control" object to the screen from the "Toolbox" task card.
2. Go to "Properties" and set the required height, width and position of the object.
3. Open the "Function trend area" group under "Properties".

   The index numbers of the function trend areas created for the object are displayed.
4. Expand the index number of the first function trend area.

   The properties of the first function trend area are displayed.
5. Enter a meaningful name for the function trend area, for example, "SpeedToTemperature".
6. Open the temperature value axis settings under "Left value axis".
7. Define the value range for temperature, for example, by entering a maximum scale value of 350 degrees and a minimum scale value of 0 degrees.
8. Open the velocity value axis settings under "Bottom value axis".
9. Define the value range for speed, for example, by entering a maximum scale value of 1400 rpm and a minimum scale value of 0 rpm.

**Note**

To add another function trend area, go to "Properties &gt; Function trend area &gt; [0] function trend area &gt; Function trends" and click on the selection button in the "Static value" column. In the dialog, click "Add".

> **Note**
>
> **Available scaling types**
>
> The f(x) trend view supports the "Linear" scaling type.

#### Configuring trends

1. Go to "Function trend area &gt; [0] function trend area &gt; Function trends &gt; [0] function trend".
2. Specify "Online" as the source type under "Data source X", and enter the name of the process tag "MotorTemperature" under "Tag".
3. Specify "Online" as the source type under "Data source Y", and enter the name of the process tag "MotorSpeed" under "Tag".
4. Specify the time range of 1 second under "Properties &gt; Function trend area &gt; Function trends".

#### Result

The function trend control is now configured. In runtime, you monitor value changes on the basis of two trends. One trend shows the temperatures and the other trend the speed. In the function trend control, you can, for example, monitor how the temperature of the motor increases as the velocity increases.

Configure an additional value display if you want to evaluate the data of the trend control in runtime. You can also configure the value display as a "Ruler".

---

**See also**

[Function trend control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#function-trend-control-rt-unified)

### Configuring bit-triggered trends (RT Unified)

By setting a trigger bit in the "Trend transfer" tag, the HMI device either reads in a trend value or an entire trend buffer. This is defined in the configuration. Bit-triggered trends are usually used to represent fast changing values.

To trigger bit-triggered trends, appropriate external tags must be created in the "Tags" editor and connected to trend areas during configuration. The HMI device and PLC then communicate with each other via these trend areas.

#### Explanation of terms

**Trend buffer**

External array tag, the values of which are displayed as a trend. The number of array elements must be the same as the number of the measuring values of the trend. The tag is only available if the archive has not been selected as the "Source settings".

**Trend request**

When you open a screen with one or more trends on the HMI device, the HMI device sets the associated bits in the trend request area. After deselecting the screen, the HMI device resets the corresponding bits in the trend request area.

The trend request area can be used in the PLC to evaluate which trend is currently displayed on the HMI device. Trends can also be triggered without evaluation of the trend request area.

**Trend transfer 1**

This area is used to trigger trends. In your control program, set the bit assigned to the trend in the trend transfer area and the trend group bit. The trend group bit is the last bit in the trend transfer area. The HMI device detects the triggering and reads either a value or the entire buffer from the PLC. It then resets the trend bit and the trend group bit.

![Explanation of terms](images/110945544203_DV_resource.Stream@PNG-en-US..png)

The trend transfer area must not be changed by the control program until the trend group bit has been reset.

**Switch buffer**

An external array tag with trend values as a second buffer that can be set when configuring a trend. While the HMI device reads the values from buffer 1, the PLC writes to buffer 2. If the HMI device reads buffer 2, the control writes to buffer 1. This prevents the trend values from being overwritten by the PLC while the HMI device is reading the trend.

**Trend transfer 2** (required only with switch buffers)

Trend transfer 2 is required for trends that are configured with switch buffers. It is structured in the same way as trend transfer 1.

**Trigger bit**

Each trend is assigned a specific bit for communication between the HMI device and the PLC. If you assign trigger bit "4" to a trend, for example, the trend is identified by bit 4 in the trend request and in the trend transfers.  
Do not use the group bit as trigger bit. The HMI device uses the group bit to detect the trigger signal. The position of the group bit in the trend transfer depends on the selected PLC.

#### Requirement

The following data blocks of the PLC were configured in STEP 7:

- Trend buffer (trend tag of the Array type)
- Trend request
- Trend transfer 1

A screen is configured.

#### Configuring the bit-triggered trend without a switch buffer

1. Add the "Trend control" object to the screen from the "Toolbox" task card.

   ![Configuring the bit-triggered trend without a switch buffer](images/142423191947_DV_resource.Stream@PNG-de-DE.png)
2. Set the desired height, width and position for the object under "Properties &gt; Layout" in the Inspector window.
3. Expand the "Time axis" group under "Properties" and select the "Points" axis mode under "Settings". Under "Range", specify how many values are to be displayed on the X axis. Under "Label", select the scale labeling of the intermediate values, the step size and the number of graduation lines.
4. Under "Properties", expand the "Trend" group.
5. In the "Name" column, click the "Add new" entry and specify the name for the trend. If needed, change the style of the trend (color, line, mode).
6. In the "Trend values" column, specify the number of values. This number depends on how many array tags you have assigned for the "Trend buffers".
7. In the "Trend type" column, select the "Bit-triggered real time" variant.
8. Set in the column "Source settings &gt; Data source" the tags for:

   - Process values
   - Trend request
   - Trend transfer

   Then enter the bit position in "Trend request" and "Trend transfer".

   ![Configuring the bit-triggered trend without a switch buffer](images/142405198347_DV_resource.Stream@PNG-en-US.png)

#### Configuring the bit-triggered trend with switch buffer

The procedure is first the same as before for the configuration of a bit-triggered trend without switch buffer (steps 1-6).

1. Select the variant "Bit-triggered buffer" in the "Trend type" column.
2. Select in the column "Source settings &gt; Data source" the tags for:

   - Process values
   - Trend request
   - Trend transfer 1

   Then enter the bit position in "Trend request" and "Trend transfer".
3. Check the "Activate buffer" check box and select the tags for:

   - Buffer tag
   - Trend transfer 2

![Configuring the bit-triggered trend with switch buffer](images/142404191115_DV_resource.Stream@PNG-en-US.png)

### Configuring the process control (RT Unified)

#### Introduction

To display tag values in tables in runtime, add a process control to a screen. The time column shows the time at which the value was reached. The value columns show the values at a given time stamp.

You can use the process control to display the incoming temperature values of a motor in a table in runtime, for example.

#### Requirement

- HMI tag for temperature measurement has been configured, for example "MotorTemperature"
- Cycle for regular display updates has been configured
- The screen is open
- The Inspector window is open

#### Configuring the process control

1. Add the required process control to the screen from the "Tools" task card.
2. Enter the label for the process control, for example "MotorTemperatureView", under "Properties" in the Inspector window.
3. Go to "Properties &gt; Process view &gt; Columns &gt; [0]" and configure the time column with the time ranges for the table.
4. Under "Sort order", define the order in which the columns of the process control are shown.
5. Configure the "Time range" and "Format" of the time display in the time column, for example "Time span".
6. Set the start time, the basis and the factor for the time range, for example 10 minutes.
7. If the values in the time column are to be updated automatically, enable "Update".
8. Go to "Properties &gt; Process view &gt; Columns &gt; [1]" and configure the properties for the value column.
9. Enter the name of the column, for example "Temperature".
10. Configure the type "Online" for current values under "Data source" and enter the tag "MotorTemperature" under "Tag".
11. Configure the display of content and the headers for the given value column.
12. Configure the toolbar and information bar of the process control.
13. If required, configure the security settings of the process control.

#### Result

The process control is now configured and displays the temperature of the motor at the measured time in runtime.

---

**See also**

[Process control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#process-control-rt-unified)
  
[Configuring reordering of the columns (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#configuring-reordering-of-the-columns-rt-unified)

### Configuring the trend companion (RT Unified)

#### Introduction

The trend companion allows you to display statistical data, for example mean values for the trend control with temperature trends. The calculation of statistical data gives the user access to trends and value changes over time. As well as calculating statistical data, you can use the trend companion as a viewing aid for trend values at a ruler position.

#### Requirement

- Trend control or function trend control has been configured in the screen
- Cycle for regular display updates has been configured
- The screen is open
- The Inspector window is open

#### Procedure

1. Add the required trend companion to the screen from the "Toolbox" task card.
2. Select the relevant control under "Properties &gt; Data source" in the Inspector window to connect the trend companion to the selected control.
3. To display the trend companion below the selected control, select the option "Dock to data source".
4. Select the "Trend companion mode" of the trend companion under "Properties", for example "Statistic result".
5. Configure the appearance of the selected mode under "Properties &gt; Statistic mode appearance":

   - Change the colors, row height and fonts in the trend companion if required.
   - Configure the headers under "Properties &gt; Statistic mode appearance &gt; Header settings" if required.
6. Configure the trend companion columns under "Properties &gt; Statistic mode appearance &gt; Columns":

   - Change the display, labels or order of columns if required.
7. Configure the view of the trend companion in the Inspector window:

   - Change the display, labeling and colors of the trend companion if required, or use the colors of the control to which the trend companion is docked.
   - Configure the information bar and the toolbar of the trend companion.

**Note**

The "Print" button [3] is reserved for future versions

#### Configuring selection

If, for example, a user wants to export values from a row, they must select the row. You specify the selection range and colors for selection during configuration. You define the settings for selection for each display mode.

1. In the Inspector window, go to "Properties &gt; Trend ruler appearance" and select the "Selection mode" for the selection range, for example "Multiple elements".
2. Select the color mode for selection, for example rows.
3. If required, select the "Border color" and "Border width" to be displayed around the selection area.
4. Choose the colors for selection as required.

#### Result

The trend companion is configured. The statistical values calculated are displayed in the trend companion in runtime.

---

**See also**

[Trend companion (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#trend-companion-rt-unified)
  
[Configuring reordering of the columns (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#configuring-reordering-of-the-columns-rt-unified)

### Configuring the toolbar and information bar (RT Unified)

#### Introduction

You can operate the controls in runtime using the buttons in the toolbar. The information bar displays the status messages of the control. During configuration, you define the contents of the toolbar and information bar.

![Introduction](images/150697104139_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Information bar |

#### Requirement

- You have opened the screen which contains at least one object, for example, the trend companion.
- The Inspector window is open.

#### Configuring the toolbar

To configure the toolbar, follow these steps:

1. In the Inspector window under "Properties &gt; Miscellaneous &gt; Toolbar", configure the general properties of the toolbar, such as background color or visibility.
2. In the Inspector window, under "Properties &gt; Properties &gt; Miscellaneous &gt; Toolbar &gt; Elements &gt; Button &gt; Visibility", enable the buttons that you need in Runtime.
3. Configure the button display, for example, background color, border and size.
4. Under "Properties &gt; Properties &gt; Miscellaneous &gt; Toolbar &gt; Elements &gt; Button &gt; Authorization", select the authorization that is required in Runtime to operate the button.
5. When a button is not operated in Runtime, disable "Allow operator control". You can reactivate a disabled a button by using a script in runtime, for example.

#### Configuring the information bar

To configure the information bar, follow these steps:

1. In the Inspector window under "Properties &gt; Properties &gt; Miscellaneous &gt; Information bar", configure the general properties of the information bar, such as background color or visibility.
2. In the Inspector window under "Properties &gt; Properties &gt; Miscellaneous &gt; Information bar &gt; Elements &gt; State display &gt; Visibility", enable the elements that you need in Runtime.
3. Configure the display of the respective element.
4. Select the authorization that is required in Runtime to operate the element.
5. When an element is not operated in Runtime, disable "Allow operator control". You can enable a disabled element again, for example, with a script in Runtime.

### Defining the data source (RT Unified)

#### Introduction

Using the data source, you define the sources from which the values are displayed on the HMI device in runtime. The following sources are available:

- Current process values from tags
- Archived values from logging tags

To set up data supply for the controls over a tag, enter the name of the tag in the "Static value" column under "Data source &gt; Tag".

#### Requirement

- An online tag or logging tag is configured
- Value column or trend has been created
- The Inspector window is open

#### Displaying current process values

Proceed as follows to display current process values:

1. Click "Properties &gt; Process view &gt; Columns" in the Inspector window to define the data source for a process control.

   The first column is always reserved for the time column. You enter the data source for value columns [1] to [N].
2. Click "Properties &gt; Trend areas &gt; Trends" in the Inspector window to define the data source for a trend control.

   For the function trend control, click on "Properties &gt; Function trend area &gt; Function trends".
3. Configure the "data source":

   - Select the entry "Online" as "Source type".
   - When you configure the trend of an function trend control, enter one tag each for "Data source X" and "Data source Y".
   - When you configure the trend of a trend control or a value column, enter the corresponding tag under "Tag".
   - Select the update cycle.

> **Note**
>
> **Using UDTs**
>
> In the "Static value" column under "Tag" first enter the name of the data type and then the name of the element separated by a period, for example, "PLCDatatypeName.ElementName".

#### Displaying values from a log

Proceed as follows to display values from a log:

1. Click "Properties &gt; Process view &gt; Columns" in the Inspector window to define the data source for a process control.

   The first column is always reserved for the time column. You enter the data source for value columns [1] to [N].
2. Click "Properties &gt; Trend areas &gt; Trends" in the Inspector window to define the data source for a trend control.

   For the function trend control, click on "Properties &gt; Function trend area &gt; Function trends".
3. Configure the "data source":

   - Select the entry "Logs" as "Source".
   - When you configure the trend of an function trend control, enter one tag each for "Data source X" and "Data source Y".
   - When you configure the trend of a trend control or a value column, enter the corresponding tag under "Tag".

> **Note**
>
> **Using logging tags**
>
> In the "Static value" column under "Tag" first enter the name of the HMI tag and then the name of the associated logging tag separated by a period, for example, "HMITag_1:LoggingTag_1".

## Reference (RT Unified)

This section contains information on the following topics:

- [Quality codes of HMI tags (RT Unified)](#quality-codes-of-hmi-tags-rt-unified)
- [Data types (RT Unified)](#data-types-rt-unified)

### Quality codes of HMI tags (RT Unified)

#### Introduction

The "Quality Code" is required to evaluate the status and quality of a tag. The quality of the entire value transfer and value processing of the respective HMI tag is summarized in the indicated Quality Code. For example, it is possible to determine from the Quality Code whether the current value is a start value or substitute value.

The Quality Code is binary-coded. The value must be converted to hexadecimal format for the analysis of the Quality Code.

The quality codes are prioritized. If several codes occur at the same time, the Quality Code reflecting the lowest quality is displayed.

#### Evaluation of Quality Codes

You can evaluate the Quality Code in a number of different ways:

- Evaluation with JScript functions
- Evaluation using the "Quality Code changed" event of an I/O field.

#### Structure

The Quality Code has the following binary structure:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| High byte: Specific information for WinCC Unified |  |  |  |  |  |  |  | Low byte: Quality Code according to PROFIBUS PA or OPC DA |  |  |  |  |  |  |  |
| Flags |  |  |  | Enhanced substatus |  |  |  | Quality |  | Substatus |  |  |  | Limits |  |
| Bit 15 | Bit 14 | Bit 13 | Bit 12 | Bit 11 | Bit 10 | Bit 9 | Bit 8 | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |

#### Quality Code according to PROFIBUS PA or OPC DA

The Quality Code according to PROFIBUS PA, or OPC DA, is described by the low byte (bit 7 to bit 0).

- **Quality**
   **(bit 7 and bit 6)**

  Quality represents the basic values of the quality levels. Making use of the substatus and limits gives rise to intermediate values over and above the quality stage concerned.

  |  |  |  |
  | --- | --- | --- |
  | Bit 7 | Bit 6 |  |
  | 0 | 0 | Bad - The value is not useful. The reasons are indicated by the sub-status. |
  | 0 | 1 | Uncertain - The quality of the value is less than normal, but the value may still be useful. The reasons are indicated by the sub-status. |
  | 1 | 0 | Good (Non-Cascade) - The quality of the value is good. Possible alarm conditions may be indicated by the sub-status. |
  | 1 | 1 | Good (Cascade) - The quality of the value is good and may be used in control. |
- **Sub-status (bit 5 to bit 2)**

  The quality alone is not enough. Sub-statuses divide the individual qualities.
- **Limit**
   **(bit 1 and bit 0)**

  The Quality Codes can be further subdivided by limits. Limits are optional.

  |  |  |  |
  | --- | --- | --- |
  | Bit 1 | Bit 0 |  |
  | 0 | 0 | O.K. - The value is free to move. |
  | 0 | 1 | Low limited - The value has acceded its low limits. |
  | 1 | 0 | High limited - The value has acceded its high limits. |
  | 1 | 1 | Constant (high and low limited) - The value cannot move, no matter what the process does. |

  For example, the limits further subdivide the Quality Code 0x54 (Engineering Unit Range Violation) into the Quality Codes 0x55, 0x56 and 0x57.

#### Specific information for WinCC Unified

Specific information for WinCC Unified is described by the high byte (bit 15 to bit 8).

- **Flags**
   **(bit 15 to bit 12)**

  Flags contain information on the interpretation of the Quality Code.

  |  |  |  |
  | --- | --- | --- |
  | Bit 15 | reserved |  |
  | Bit 14 | Time corrected | 1: The data timestamp applied by external data source has been corrected by the system. Thus, Bit 13 "Source time" is not set.   Time correction happens if the external timestamp is older than the timestamp of the last known value. |
  | Bit 13 | Source time | 1: The data timestamp has been produced and assigned by external data source. |
  | Bit 12 | Source quality | 0: The data quality has been determined and assigned by external data source. |
- **Extended sub-status (bit 11 to bit 8)**

  The extended sub-status provides more detailed information about the sub-status. The extended sub-status is relevant for some Quality Codes formed by the HMI system.

#### Externally generated quality code of tags

If bit 12 is not set, the Quality Code was generated from an external source in accordance with PROFIBUS PA. The table begins with the worst Quality Code and ends with the best Quality Code. The best Quality Code has the lowest priority, while the worst Quality Code has the highest priority. If several statuses occur for one tag in the process, the poorest code is passed on.

| Code (hex) | Quality |  | Low byte |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q | Q | S | S | S | S | L | L |  |  |  |
| 0x23 | Bad | Device passivated - Diagnostic alerts inhibited | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| 0x3C | Bad | Function check - Local override | 0 | 0 | 1 | 1 | 1 | 1 | - | - |
| 0x04 | Bad | Configuration Error - Set if the value is not useful because there is some inconsistency regarding the parameterization or configuration, depending on what a specific manufacturer can detect. | 0 | 0 | 0 | 0 | 0 | 1 | - | - |
| 0x1C | Bad | Out of Service - The value is not reliable because the block is not being evaluated, and may be under construction by a configurer. Set if the block mode is O/S. | 0 | 0 | 0 | 1 | 1 | 1 | - | - |
| 0x73 | Uncertain | Simulated value - Start | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0x74 | Uncertain | Simulated value - End | 0 | 1 | 1 | 1 | 0 | 1 | - | - |
| 0x84 | Good (Non-Cascade) | Active Update event - Set if the value is good and the block has an active Update event. | 1 | 0 | 0 | 0 | 0 | 1 | - | - |
| 0x24 | Bad | Maintenance alarm - More diagnostics available. | 0 | 0 | 1 | 0 | 0 | 1 | - | - |
| 0x18 | Bad | No Communication, with no usable value - Set if there has never been any communication with this value since it was last "Out of Service". | 0 | 0 | 0 | 1 | 1 | 0 | - | - |
| 0x14 | Bad | No Communication, with last usable value - Set if this value had been set by communication, which has now failed. | 0 | 0 | 0 | 1 | 0 | 1 | - | - |
| 0x0C | Bad | Device Failure - Set if the source of the value is affected by a device failure. | 0 | 0 | 0 | 0 | 1 | 1 | - | - |
| 0x10 | Bad | Sensor failure | 0 | 0 | 0 | 1 | 0 | 0 | - | - |
| 0x08 | Bad | Not connected - Set if this input is required to be connected and is not connected. | 0 | 0 | 0 | 0 | 1 | 0 | - | - |
| 0x00 | Bad | Non-specific - There is no specific reason why the value is bad. Used for propagation. | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| 0x28 | Bad | Process related - Substitute value | 0 | 0 | 1 | 0 | 1 | 0 | - | - |
| 0x2B | Bad | Process related - No maintenance | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 1 |
| 0x68 | Uncertain | Maintenance demanded | 0 | 1 | 1 | 0 | 1 | 0 | - | - |
| 0x60 | Uncertain | Simulated value - Set when the process value is written by the operator while the block is in manual mode. | 0 | 1 | 1 | 0 | 0 | 0 | - | - |
| 0x64 | Uncertain | Sensor calibration | 0 | 1 | 1 | 0 | 0 | 1 | - | - |
| 0x5C | Uncertain | Configuration error | 0 | 1 | 0 | 1 | 1 | 1 | - | - |
| 0x58 | Uncertain | Sub-normal | 0 | 1 | 0 | 1 | 1 | 0 | - | - |
| 0x54 | Uncertain | Engineering Unit Range Violation - Set if the value lies outside of the set of values defined for this parameter. The Limits define which direction has been exceeded. | 0 | 1 | 0 | 1 | 0 | 1 | - | - |
| 0x50 | Uncertain | Sensor conversion not accurate | 0 | 1 | 0 | 1 | 0 | 0 | - | - |
| 0x4B | Uncertain | Substitute (constant) | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 0x78 | Uncertain | Process related - No maintenance | 0 | 1 | 1 | 1 | 1 | 0 | - | - |
| 0x4C | Uncertain | Initial Value - Value of volatile parameters during and after reset of the device or of a parameter. | 0 | 1 | 0 | 0 | 1 | 1 | - | - |
| 0x48 | Uncertain | Substitute value - Predefined value is used instead of the calculated one. This is used for fail safe handling. | 0 | 1 | 0 | 0 | 1 | 0 | - | - |
| 0x44 | Uncertain | Last Usable Value - Whatever was writing this value has stopped doing so. This is used for fail safe handling. | 0 | 1 | 0 | 0 | 0 | 1 | - | - |
| 0x40 | Uncertain | Non-specific - There is no specific reason why the value is uncertain. Used for propagation. | 0 | 1 | 0 | 0 | 0 | 0 | - | - |
| 0xE0 | Good(Cascade) | Initiate Fail Safe (IFS) - The value is from a block that wants its downstream  output block (e.g. AO) to go to Fail Safe. | 1 | 1 | 0 | 1 | 1 | 0 | - | - |
| 0xD8 | Good(Cascade) | Local Override (LO) - The value is from a block that has been locked out by a local key switch or is a Complex AO/DO with interlock logic active. The failure of normal control must be propagated to a function running in a host system for alarm and display purposes. This also implies "Not Invited". | 1 | 1 | 0 | 1 | 1 | 0 | - | - |
| 0xD4 | Good (Cascade) | Do Not Select (DNS) - The value is from a block which should not be selected, due to conditions in or above the block. | 1 | 1 | 0 | 1 | 0 | 1 | - | - |
| 0xCC | Good (Cascade) | Not Invited (NI) - The value is from a block which does not have a target mode that would use this input. | 1 | 1 | 0 | 0 | 1 | 1 | - | - |
| 0xC8 | Good (Cascade) | Initialization Request (IR) - The value is an initialization value for a source (back calculation input parameter), because the lower loop is broken or the mode is wrong. | 1 | 1 | 0 | 0 | 1 | 0 | - | - |
| 0xC4 | Good (Cascade) | Initialization Acknowledge (IA) - The value is an initialized value from a source (cascade input, remote-cascade in, and remote-output in parameters). | 1 | 1 | 0 | 0 | 0 | 1 | - | - |
| 0xA0 | Good (Non-Cascade) | Initiate fail safe | 1 | 0 | 1 | 0 | 0 | 0 | - | - |
| 0x98 | Good (Non-Cascade) | Unacknowledged  Critical Alarm - Set if the value is good and the block has an unacknowledged Alarm with a priority greater than or equal to 8. | 1 | 0 | 0 | 1 | 1 | 0 | - | - |
| 0x94 | Good (Non-Cascade) | Unacknowledged Advisory Alarm - Set if the value is good and the block has an unacknowledged Alarm with a priority less than 8. | 1 | 0 | 0 | 1 | 0 | 1 | - | - |
| 0x90 | Good (Non-Cascade) | Unacknowledged Update event - Set if the value is good and the block has an unacknowledged Update event. | 1 | 0 | 0 | 1 | 0 | 0 | - | - |
| 0x8C | Good (Non-Cascade) | Active  Critical Alarm -  Set if the value is good and the block has an active Alarm with a priority greater than or equal to 8. | 1 | 0 | 0 | 0 | 1 | 1 | - | - |
| 0x88 | Good (Non-Cascade) | Active Advisory Alarm - Set if the value is good and the block has an active Alarm with a priority less than 8. | 1 | 0 | 0 | 0 | 1 | 0 | - | - |
| 0xA8 | Good (Non-Cascade) | Maintenance demanded | 1 | 0 | 1 | 0 | 1 | 0 | - | - |
| 0xA4 | Good (Non-Cascade) | Maintenance required | 1 | 0 | 1 | 0 | 0 | 1 | - | - |
| 0xBC | Good (Non-Cascade) | Function check - Local override | 1 | 0 | 1 | 1 | 1 | 1 | - | - |
| 0xC0 | Good(Cascade) | OK -  No error or special condition is associated with this value. | 1 | 1 | 0 | 0 | 0 | 0 | - | - |
| 0x80 | Good (Non-Cascade) | OK -  No error or special condition is associated with this value. | 1 | 0 | 0 | 0 | 0 | 0 | - | - |

#### Internally generated quality code of tags

If bit 12 in flags is set, the Quality Code was generated by the HMI system. The table begins with the worst Quality Code and ends with the best Quality Code. The best Quality Code has the lowest priority, while the worst Quality Code has the highest priority. If several statuses occur for one tag in the process, the poorest code is passed on.

> **Note**
>
> The Quality Codes in the following table with 3 hexadecimal places have an extended sub-status (bit 11 to bit 8).

| Code (hex) | Quality |  | Low byte |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q | Q | S | S | S | S | L | L |  |  |  |
| 0x70n | Bad | Disabled | 0 | 0 | 0 | 0 | - | - | - | - |
| 0x300 | Bad | Unusable value - A logged value has been identified to be incorrect, but a respective correction value is not available. The corresponding sub-status is set to ‘non-specific’. | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0x04 | Bad | Configuration Error - Set if the value is not useful because there is some inconsistency regarding the parameterization or configuration, depending on what a specific manufacturer can detect. | 0 | 0 | 0 | 0 | 0 | 1 | - | - |
| 0x1C | Bad | Out of Service - The value is not reliable because the block is not being evaluated, and may be under construction by a configurer. Set if the block mode is O/S. | 0 | 0 | 0 | 1 | 1 | 1 | - | - |
| 0x18 | Bad | No Communication, with no usable value - Set if there has never been any communication with this value since it was last "Out of Service". | 0 | 0 | 0 | 1 | 1 | 0 | - | - |
| 0x14 | Bad | No Communication, with last usable value - Set if this value had been set by communication, which has now failed. | 0 | 0 | 0 | 1 | 0 | 1 | - | - |
| 0x10 | Bad | Sensor failure | 0 | 0 | 0 | 1 | 0 | 0 | - | - |
| 0x08 | Bad | Not Connected - Set if this input is required to be connected and is not connected. | 0 | 0 | 0 | 0 | 1 | 0 | - | - |
| 0x100 | Bad | Aggregated value - The value has been calculated out of multiple values with less than the re-quired number of good sources. This includes data aggregation by means of data compression algorithms. The corresponding sub-status is set to ‘non-specific’. | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0x00 | Bad | non-specific - There is no specific reason why the value is bad. Used for propagation. | 0 | 0 | 0 | 0 | 0 | 0 | - | - |
| 0x74n | Uncertain | Disabled - The provider of the value, e.g. logging tag for logged value, has been disabled and the previous value was GOOD or UNCERTAIN. In case of GOOD the corresponding sub- status is set to ‘last usable value’. In case of UNCERTAIN the corresponding sub-status is taken from the last sub-status. | 0 | 1 | 0 | 0 | - | - | - | - |
| 0x158 | Uncertain | Aggregated value - The value has been calculated out of multiple values with less than the required number of good sources to be GOOD as well as less than required number of bad sources to be BAD. This includes data aggregation by means of data compression algorithms. The corresponding sub-status is set to ‘sub-normal’. | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0x58 | Uncertain | Sub-normal | 0 | 1 | 0 | 1 | 1 | 0 | - | - |
| 0x54 | Uncertain | Engineering Unit Range Violation - Set if the value lies outside of the set of values defined for this parameter. The Limits define which direction has been exceeded. | 0 | 1 | 0 | 1 | 0 | 1 | - | - |
| 0x4C | Uncertain | Initial Value - Value of volatile parameters during and after reset of the device or of a parameter. | 0 | 1 | 0 | 0 | 1 | 1 | - | - |
| 0x48 | Uncertain | Substitute value - Predefined value is used instead of the calculated one. This is used for fail safe handling. | 0 | 1 | 0 | 0 | 1 | 0 | - | - |
| 0x44 | Uncertain | Last Usable Value - Whatever was writing this value has stopped doing so. This is used for fail safe handling. | 0 | 1 | 0 | 0 | 0 | 1 | - | - |
| 0x40 | Uncertain | Non-specific - There is no specific reason why the value is uncertain. Used for propagation. | 0 | 1 | 0 | 0 | 0 | 0 | - | - |
| 0x3C0 | Good(Cascade) | Corrected value - A logged value has been corrected. The corresponding sub-status is set to ‘non-specific’. | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0x2C0 | Good(Cascade) | Manual input - A logged value has been created manually. The corresponding sub-status is set to ‘non-specific’. | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0x1C0 | Good(Cascade) | Aggregated value -The value has been calculated out of multiple (GOOD) values. This includes data aggregation by means of data compression algorithms. The corresponding sub-status is set to ‘non-specific’. | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0xD8 | Good (Cascade) | Local Override (LO) - The value is from a block that has been locked out by a local key switch or is a Complex AO/DO with interlock logic active. The failure of normal control must be propagated to a function running in a host system for alarm and display purposes. This also implies "Not Invited". | 1 | 1 | 0 | 1 | 1 | 0 | - | - |
| 0x6C0 | Good(Cascade) | Initial value - The local data source has been initialized with the configured initial value. The corresponding sub-status is set to ‘non-specific’. | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0x4C0 | Good(Cascade) | Last usable value - The local data source has been initialized with the last usable value, if pre-sent inside a local persistency. The corresponding sub-status is set to ‘non-specific’. | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0xC0 | Good(Cascade) | OK -  No error or special condition is associated with this value. | 1 | 1 | 0 | 0 | 0 | 0 | - | - |

#### Quality Codes in Communication with OPC

When connecting to a OPC UA server, the OPC UA status code is shown in a quality code.

| Quality Code in WinCC | Status code according to OPC |
| --- | --- |
| 0x48 | 0x40 |
| 0x4C | 0x40 |
| 0x5C | 0x40 |
| 0x60 | 0x40 |
| 0x80...0xD4 | 0xC0 |
| 0xD8 | 0xC0 |

### Data types (RT Unified)

This section contains information on the following topics:

- [Data types for SIMATIC S7-300/400 (RT Unified)](#data-types-for-simatic-s7-300400-rt-unified)
- [Data types for SIMATIC S7-1200 (RT Unified)](#data-types-for-simatic-s7-1200-rt-unified)
- [Data types for SIMATIC S7-1500 (RT Unified)](#data-types-for-simatic-s7-1500-rt-unified)
- [User-defined PLC data types (UDT) (RT Unified)](#user-defined-plc-data-types-udt-rt-unified)

#### Data types for SIMATIC S7-300/400 (RT Unified)

##### Overview

The following table shows the data types for SIMATIC S7-300/400 with the corresponding HMI data types and value ranges in WinCC.

| Data type | Value range |
| --- | --- |
| Array of Char | - Array of Char is mapped in HMI to a tag of the String data type - The maximum array of Char is 254 characters. - With SIMATIC S7-300    - Read access: 222 characters   - Write access: 212 characters - 0 ... 224 (ASCII) - Characters from the Windows 1252 code page |
| Bool | 0 (FALSE), 1 (TRUE) |
| Byte | 0 ... 255 |
| Char | 0 ... 255 (ASCII) |
| Counter | 0 ... 999 |
| Date | 1990-01-01 ... 2168-12-31 |
| DInt | −2147483648 … +2147483647 |
| DWord | 0 .. 4294967295 |
| Int | −32768 … 32767 |
| Real | ±1.17549E-38 to ±3.40282E+38 and 0.0 |
| S5Time | 0 … 2h46m30s0ms |
| String | - The maximum length of a string is 254 characters. - With SIMATIC S7-300    - Read access: 220 characters   - Write access: 210 characters - ASCII - Characters from the Windows 1252 code page |
| Time<sup> 1</sup> | -24d20h31m23s648ms ... +24d20h31m23s647ms |
| Time_Of_Day | 00:00:00 ... 23:59:59.999 |
| Timer | -0ms ... 2h46m30s0ms |
| Word | 0 ... 65535 |

1: If the value is set via the HMI, then the granularity is in 100 nanosecond intervals. In contrast, the granularity of WinCC Advanced, WinCC Comfort and WinCC Professional is milliseconds.

#### Data types for SIMATIC S7-1200 (RT Unified)

##### Overview

The following table shows the data types for SIMATIC S7-1200 with the corresponding HMI data types and value ranges in WinCC.

| Data type | Value range |
| --- | --- |
| Array of Char | - Array of Char is mapped in HMI to a tag of the String data type - The maximum array of Char is 254 characters. - 0 ... 255 (ASCII) - Characters from the Windows 1252 code page |
| Array of WChar | - Array of WChar is mapped in HMI to a tag of the String data type - The maximum array of WChar is 255 characters. - Characters from the Unicode code page |
| Bool | 0 (FALSE), 1 (TRUE) |
| Byte | 0 ... 255 |
| Char | 0 … 255 (ASCII) |
| Date | 1990-01-01 ... 2168-12-31 |
| DInt | −2147483648 … +2147483647 |
| DTL | 1970-01-01-00:00:00.0 ... 2262-04-11-23:47:16.854775807 |
| DWord | 0 ... 4294967295 |
| Int | -32768 ... +32767 |
| LReal | ±1.79769313486231E+308 ... ±2.22507385850720E-308 and 0.0 |
| Real | ±1.17549E-38 ... ±-3.40282E+38 and 0.0 |
| SInt | -128 ... +127 |
| String | - The maximum length of a string is 254 characters. - ASCII - Characters from the Windows 1252 code page |
| Time<sup> 1</sup> | -24d20h31m23s648ms ... +24d20h31m23s647ms |
| Time_Of_Day, TOD | 00:00:00 ... 23:59:59.999 |
| UDInt | 0 ... 4294967295 |
| UInt | 0 … 65535 |
| USInt | 0 ... 255 |
| WChar | UNICODE |
| Word | 0 … 65535 |
| WString | UNICODE |
| PLCUDT | - |

1: If the value is set via the HMI, then the granularity is in 100 nanosecond intervals. In contrast, the granularity of WinCC Advanced, WinCC Comfort and WinCC Professional is milliseconds.

#### Data types for SIMATIC S7-1500 (RT Unified)

##### Overview

The following table shows the data types for SIMATIC S7-1500 with the corresponding HMI data types and value ranges in WinCC.

| Data type | Value range |
| --- | --- |
| Array of Char | - Array of Char is mapped in HMI to a tag of the String data type - The maximum array of Char is 254 characters. - 0 ... 255 (ASCII) - Characters from the Windows 1252 code page |
| Array of WChar | - Array of WChar is mapped in HMI to a tag of the String data type - The maximum array of WChar is 255 characters. - Characters from the Unicode code page |
| Bool | 0 (FALSE), 1 (TRUE) |
| Byte | 0 ... 255 |
| Char | 0 … 255 (ASCII) |
| Counter | 0 … 65535 |
| Date | 1990-01-01 ... 2168-12-31 |
| Date_And_Time, DT | 1990‑1‑1-0:0:0.0 ... 2089‑12‑31-23:59:59.999 |
| DInt | −2147483648 … +2147483647 |
| DTL | 1970-01-01-00:00:00.0 ... 2262-04-11-23:47:16.854775807 |
| DWord | 0 ... 4294967295 |
| Int | -32768 ... +32767 |
| LDT | 1970-01-01-00:00:00.000000000 ... 2263-04-11-23:47:16.854775808 |
| LInt | -9223372036854775808 ... +9223372036854775807 |
| LReal | ±1.79769313486231E+308 ... ±2.22507385850720E-308 and 0.0 |
| LTime<sup> 1</sup> | - Value range: -9223372036854775808 to 9223372036854775807 - Unit: ns - Resulting time interval:    -106751d23h47m16s854ms775us808ns ... +106751d23h47m16s854ms775us807ns  For more information on setting an LTime value via the HMI, refer to section [IO field](Configuring%20screens%20%28RT%20Unified%29.md#io-field-rt-unified). |
| LTime_Of_Day, LTOD | 00:00:00.000000000 ... 23:59:59.999999999 |
| LWord | 0 ... 18446744073709551615 |
| Real | ±1.17549E-38 ... ±-3.40282E+38 and 0.0 |
| S5Time | 0ms ... 2h46m30s0ms |
| SInt | -128 ... +127 |
| String | - The maximum length of a string is 254 characters. - ASCII - Characters from the Windows 1252 code page |
| Time<sup> 1</sup> | -24d20h31m23s648ms ... +24d20h31m23s647ms |
| Time_Of_Day, TOD | 00:00:00 ... 23:59:59.999 |
| Timer | -24d20h31m23s648ms ... +24d20h31m23s647ms |
| UDInt | 0 ... 4294967295 |
| UInt | 0 … 65535 |
| ULInt | 0 ... 18446744073709551615 |
| USInt | 0 ... 255 |
| WChar | UNICODE |
| Word | 0 … 65535 |
| WString | UNICODE |
| PLCUDT | - |

1: If the value is set via the HMI, then the granularity is in 100 nanosecond intervals. In contrast, the granularity of WinCC Advanced, WinCC Comfort and WinCC Professional is milliseconds.

#### User-defined PLC data types (UDT) (RT Unified)

##### Overview

You can connect with the HMI tags and DB instances of user-defined PLC data types (UDT).

The PLC data type and the corresponding DB instances are created and updated centrally in STEP 7. In WinCC, you can use the following sources as PLC tag (DB instances):

- Data block elements that use a UDT as data type
- Instance data blocks of a UDT

The data type is taken from STEP 7 and is not converted into an HMI data type. The access type is always "Symbolic access".

##### Elements of a PLC data type

You have access to the following elements in WinCC with a structured PLC data type:

- Elements that have been released for WinCC in STEP 7.
- Elements whose data types are supported in WinCC.

> **Note**
>
> **Invalid elements of a PLC data type in WinCC**
>
> Invalid elements generate an error in WinCC.
>
> If you disable the "Accessible from HMI" option for the corresponding elements of the associated PLC data type in STEP 7, these elements are excluded in WinCC.

##### Naming conventions

The following characters are invalid in the name of the PLC data type and generate an error in WinCC:

- Period: "."
- Square brackets: "[" and "]"

##### Properties

The properties of the PLC data type and its elements are adopted in WinCC. Depending on the data type used, the properties are read-only or can be written to in WinCC.

If you change the connection of the PLC data type in WinCC, all elements of the PLC data type are deleted and the properties of the newly connected PLC tag are used.

In WinCC, you have access to STEP 7 comments on elements of the PLC data type.

You have limited access to properties in WinCC for the following elements of PLC data types:

- Elements of the data type "Struct"
- PLC data type
- Multidimensional arrays
- Array of complex data types except "DTL"

##### Mapping of the data type "DTL"

If a PLC data type contains elements of the data type "DTL", these elements are mapped in WinCC without lower-level elements. The data type "DTL" turns into "DateTime" in WinCC.

##### Tags with elements of the "DTL" data type

Tags that use the "DTL" data type element by element can only be used as read-only with symbolic addressing, e.g. with SIMATIC S7 1500. With absolute addressing, write access is also possible.

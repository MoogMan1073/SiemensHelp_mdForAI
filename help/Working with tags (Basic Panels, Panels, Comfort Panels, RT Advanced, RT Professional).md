---
title: "Working with tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: TagsWCCPenUS
topics: 88
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Working with Arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-arrays-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with Arrays (RT Professional)](#working-with-arrays-rt-professional)
- [Working with user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with cycles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-cycles-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with cycles (RT Professional)](#working-with-cycles-rt-professional)
- [Reference (RT Professional)](#reference-rt-professional)
- [Archive tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#archive-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Displaying Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#displaying-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Overview of HMI tag tables (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-tag-tables-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [External tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#external-tags-basic-panels-panels-comfort-panels-rt-advanced)
- [External tags (RT Professional)](#external-tags-rt-professional)
- [Addressing external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Internal Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#internal-tags-basic-panels-panels-comfort-panels-rt-advanced)
- [Internal Tags (RT Professional)](#internal-tags-rt-professional)
- [System tags (RT Professional)](#system-tags-rt-professional)
- [System diagnostics with performance tags (RT Professional)](#system-diagnostics-with-performance-tags-rt-professional)
- [Overview of performance tags (RT Professional)](#overview-of-performance-tags-rt-professional)
- [Diagnostic Tags of Tag Logging Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#diagnostic-tags-of-tag-logging-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Raw data tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#raw-data-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Process values are forwarded in runtime using tags. Process values are data which is stored in the memory of one of the connected automation systems. They represent the status of a plant in the form of temperatures, fill levels or switching states, for example. Define external tags for processing the process values in WinCC.

WinCC works with two types of tag:

- External tags
- Internal tags

The external tags form the link between WinCC and the automation systems. The values of external tags correspond to the process values from the memory of an automation system. The value of an external tag is determined by reading the process value from the memory of the automation system. It is also possible to rewrite a process value in the memory of the automation system.

![Introduction](images/23276049035_DV_resource.Stream@PNG-en-US.png)

Internal tags do not have a process link and only convey values within the WinCC. The tag values are only available as long as runtime is running.

#### Tags in WinCC

For external tags, the properties of the tag are used to define the connection that the WinCC uses to communicate with the automation system and form of data exchange.

Tags that are not supplied with values by the process - the internal tags - are not connected to the automation system. In the tag's "Connection" property, this is identified by the "Internal tag" entry.

You can create tags in different tag tables for greater clarity. You then directly access the individual tag tables in the "HMI tags" node in the project tree. The tags from all tag tables can be displayed with the help of the table "Show all tags".

With structures you bundle a number of different tags that form one logical unit. Structures are project-associated data and are available for all HMI devices of the project. You use the "Types" editor in the project library to create and edit a structure.

---

**See also**

[Internal Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#internal-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[External tags (RT Professional)](#external-tags-rt-professional)
  
[Cycle basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#cycle-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-arrays-basic-panels-panels-comfort-panels-rt-advanced)
  
[Overview of HMI tag tables (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-hmi-tag-tables-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Addressing external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Cycle basics (RT Professional)](#cycle-basics-rt-professional)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[External tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#external-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Internal Tags (RT Professional)](#internal-tags-rt-professional)
  
[Outputting tag values in screens (Basic) (Basic Panels)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#outputting-tag-values-in-screens-basic-basic-panels)

### Overview of HMI tag tables (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

HMI tag tables contain the definitions of the HMI tags that apply across all devices. A tag table is created automatically for each HMI device created in the project.

In the project tree there is an "HMI tags" folder for each HMI device. The following tables can be contained in this folder:

- Default tag table
- User-defined tag tables
- Table of all tags

In the project tree you can create additional tag tables in the HMI tags folder and use these to sort and group tags and constants. You can move tags to a different tag table using a drag-and-drop operation or with the help of the "Tag table" field. Activate the "Tags table" field using the shortcut menu of the column headings.

#### Default tag table

There is one default tag table for each HMI device of the project. It cannot be deleted or moved. The default tag table contains HMI tags and, depending on the HMI device, also system tags. You can declare all HMI tags in the standard tags table or, as necessary, additional user-defined tables of tags.

#### User-defined tag tables

You can create multiple user-defined tag tables for each HMI device in order to group tags according to your requirements. You can rename, gather into groups, or delete user-defined tag tables. To group tag tables, create additional subfolders in the HMI tags folder.

#### All tags

The "All tags" table shows an overview of all HMI tags and system tags of the HMI device in question. This table cannot be deleted, renamed or moved. This table also contains the "Tags table" column, which indicates the tag table of where a tag is included. Using the "Tags table" field, the assignment of a tag to a tags table can be changed.

With devices for Runtime Professional, the table "All tags" contain an additional tab "System tags". The system tags are created by the system and used for internal management of the project. The names of the system tags begin with the "@" character. System tags cannot be deleted or renamed. You can evaluate the value of a system tag, but cannot modify it.

#### Additional tables

The following tables are also available in an HMI tag table:

- Discrete alarms
- Analog alarms
- Logging tags

With the help of these tables you configure alarms and logging tags for the currently selected HMI tag.

#### Discrete alarms table

In the "Discrete alarms" table, you configure discrete alarms to the HMI tag selected in the HMI tag table. When you configure a discrete alarm, multiple selection in the HMI tag table is not possible. You configure the discrete alarms for each HMI tag separately.

#### Analog alarms table

In the "Analog alarms" table, you configure analog alarms to the HMI tag selected in the HMI tag table. When you configure an analog alarm, multiple selection in the HMI tag table is not possible. You configure the analog alarms for each HMI tag separately.

#### Logging tags table

In the "Logging tags" table, you configure logging tags to the HMI tag selected in the HMI tag table. When you configure a logging tag, multiple selection in the HMI tag table is not possible. You configure the logging tags for each HMI tag separately. The "Logging tags" table is only available if the HMI device used supports logging.   
If WinCC Runtime Professional is used, you can also assign several log tags to a tag. With the other HMI devices, you can only assign one log tag to a tag.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### External tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

External tags allow communication (data exchange) between the components of an automation system, for example, between an HMI device and a PLC.

#### Principle

An external tag is the image of a defined memory location in the PLC. You have read and write access to this storage location from both the HMI device and from the PLC.

Since external tags are the image of a storage location in the PLC, the applicable data types depend on the PLC which is connected to the HMI device.

If you write a PLC control program in STEP 7, the PLC tags created in the control program will be added to the PLC tag table. If you want to connect an external tag to a PLC tag, access the PLC tags directly via the PLC tag table and connect them to the external tag.

#### Data types

All the data types which are available at the connected PLC are available at an external tag in WinCC. Information about data types which are available for connection to other PLCs can be found in the documentation about the respective communication drivers.

See "[Basics of communication](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)" for additional information.

> **Note**
>
> As well as external tags, area pointers are also available for communication between the HMI device and PLC. You can set up and enable the area indicators in the "Connections" editor.

#### Central tag management in STEP 7

You can connect also connect DB instances of user-defined PLC data types (UDT) to the HMI tags.

The PLC data type and the corresponding DB instances are created and updated centrally in STEP 7. In WinCC, you can use the following sources as PLC tag (DB instances):

- Data block elements that use a UDT as data type
- Data block instances of a UDT

The data type is taken from STEP 7 and is not converted to an HMI data type. The access type is always "Symbolic access". Depending on the release for WinCC in STEP 7, elements and structured elements of the PLC data type are applied to WinCC. Elements of a structured UDT are applied and displayed in the PLC tag table if the instance-specific properties "Visible in HMI" and "Accessible from HMI" have been set.

> **Note**
>
> ****Accessing PLC data types****
>
> Access to PLC data types is only available in conjunction with SIMATIC S7-1200 or S7-1500.

#### Synchronization with PLC tags

A variety of options for synchronizing external tags with the PLC tags are available in the Runtime settings under "Settings for tags".

When you perform synchronization, you have the option of automatically applying the tag names of the PLC to external tags and reconnecting the existing tags.

The generated tag name is derived from the position of the data value in the hierarchical structure of the data block.

#### Update of tag values

For external tags, the current tag values are transmitted in Runtime via the communication connection between WinCC and the connected automation systems and then saved in the runtime memory. Next, the tag value will be updated to the set cycle time. For use in the runtime project, WinCC accesses tag values in the runtime memory that were read from the PLC at the previous cycle time. As a result, the value in the PLC can already change while the value from the runtime memory is being processed.

> **Note**
>
> **PLC array elements in conjunction with S7-1200 or S7-1500**
>
> The index of the PLC array elements can begin with any number. In WinCC, indexing always starts with 0.
>
> A PLC tag "Array [1..3] of Int", for example, is mapped to "Array [0..2] of Int" in WinCC.
>
> When you access an array in a script, pay attention to the correct indexing.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of communication (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### External tags (RT Professional)

#### Introduction

External tags allow communication (data exchange) between the components of an automation system, for example, between an HMI device and a PLC.

#### Principle

An external tag is the image of a defined memory location in the PLC. You have read and write access to this storage location from both the HMI device and from the PLC.

Since external tags are the image of a storage location in the PLC, the applicable data types depend on the PLC which is connected to the HMI device.

If you write a PLC control program in STEP 7, the PLC tags created in the control program will be added to the PLC tag table. If you want to connect an external tag to a PLC tag, access the PLC tags directly via the PLC tag table and connect them to the external tag.

#### Data types

All the data types which are available at the connected PLC are available at an external tag in WinCC. If the data type of the PLC tag is not available in WinCC, a compatible data type is automatically used at the HMI tag. If you use PLC data types, the data type is adopted by WinCC. You can change the data type at the HMI tag, if necessary.

#### Central tag management in STEP 7

You can connect also connect DB instances of user-defined PLC data types (UDT) to the HMI tags.

The PLC data type and the corresponding DB instances are created and updated centrally in STEP 7. In WinCC, you can use the following sources as PLC tag (DB instances):

- Data block elements that use a UDT as data type
- Data block instances of a UDT

The data type is taken from STEP 7 and is not converted to an HMI data type. The access type is always "Symbolic access". Depending on the release for WinCC in STEP 7, elements and structured

elements of the PLC data type are also transferred to WinCC.

> **Note**
>
> **Accessing PLC data types**
>
> Access to PLC data types is only available in conjunction with SIMATIC S7-1200 or S7-1500.

#### Synchronization with PLC tags

A variety of options for synchronizing external tags with the PLC tags are available in the Runtime settings under "Settings for tags".

When you perform synchronization, you have the option of automatically applying the tag names of the PLC to external tags and reconnecting the existing tags.

The generated tag name is derived from the position of the data value in the hierarchical structure of the data block.

#### Update of tag values

For external tags, the current tag values are transmitted in Runtime via the communication connection between WinCC and the connected automation systems and then saved in the runtime memory. Next, the tag value will be updated to the set cycle time. For use in the runtime project, WinCC accesses tag values in the runtime memory that were read from the PLC at the previous cycle time. As a result, the value in the PLC can already change while the value from the runtime memory is being processed.

You can read out the process values directly from the PLC memory, if necessary. Use the GetTag functions for this purpose. For more detailed information, refer to the documentation for C functions under "[GetTag](C%20scripting%20%28RT%20Professional%29.md#gettag-rt-professional)".

> **Note**
>
> **PLC array elements in conjunction with S7-1200 or S7-1500**
>
> The index of the PLC array elements can begin with any number. In WinCC, indexing always starts with 0.
>
> A PLC tag "Array [1..3] of Int", for example, is mapped to "Array [0..2] of Int" in WinCC.
>
> When you access an array in a script, pay attention to the correct indexing.

#### Displaying the PLC tag comment

If you want to see the comments for the connected PLC tag, select the column "Source comment" in the HMI tag table. The source comment is not available in runtime.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adapting-the-data-type-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Synchronizing tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#synchronizing-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User-defined PLC data types (UDT) (RT Professional)](#user-defined-plc-data-types-udt-rt-professional)
  
[Basics of communication (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[GetTag (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#gettag-rt-professional)

### Addressing external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The options for addressing external tags depend on the type of connection between WinCC and the PLC in question. A distinction must be made between the following connection types:

- Integrated connection  
  Connections of devices which are within a project and were created with the "Devices & Networks" editor are referred to as integrated connections.
- Non-integrated connection  
  Connections of devices which were created with the "Connections" editor are referred to as non-integrated connections. It is not necessary that all of the devices be within a single project.

The connection type can also be recognized by its icon.

| Symbol | Meaning |
| --- | --- |
| ![Introduction](images/23072055691_DV_resource.Stream@PNG-de-DE.png) | Integrated connection |
| ![Introduction](images/23081203083_DV_resource.Stream@PNG-de-DE.png) | Non-integrated connection |

You can find additional information in the section "[Basics of communication](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

#### Addressing with integrated connections

An integrated connection offers the advantage that you can address a tag both symbolically and absolutely.

For symbolic addressing, you select the PLC tag via its name and connect it to the HMI tag. The valid data type for the HMI tag is automatically selected by the system. You have to distinguish between the following cases when you address elements in data blocks:

**Symbolic addressing of data blocks with optimized access and standard access:**

During the symbolic addressing of a data block with optimized access and standard access, the address of an element in the data block is dynamically assigned and is automatically adopted in the HMI tag in the event of a change. You do not need to compile the connected data block or the WinCC project for this step.  
For data blocks with optimized access, only symbolic addressing is available.

For symbolic addressing of elements in a data block, you only need to recompile and reload the WinCC project in case of the following changes:

- If the name or the data type of the linked data block element or global PLC tag has changed.
- If the name or the data type of the higher level structure node of a linked element in the data block element or global PLC tag has changed.
- If the name of the connected data block has changed.

Symbolic addressing is currently available with the following PLCs:

- SIMATIC S7-1200
- SIMATIC S7-1500
- SIMATIC ET 200 CPU
- SIMATIC S7-1500 software controller

Symbolic addressing is also available if you have an integrated link.

You can also use absolute addressing with an integrated connection. You have to use absolute addressing for PLC tags from a SIMATIC S7-300/400 PLC. If you have connected an HMI tag with a PLC tag and the address of the PLC tag changes, you only have to recompile the control program to update the new address in WinCC. Then you recompile the WinCC project and load it onto the HMI device.

In WinCC, symbolic addressing is the default method. To change the default setting, select the menu command "Options > Settings". Select "Visualization > Tags" in the "Settings" dialog. If required, disable the "Symbolic access" option.

The availability of an integrated connection depends on the PLC used. The following table shows the availability:

| PLC | Integrated connection | Comments |
| --- | --- | --- |
| S7-300/400 | Yes | The linking of tags is not checked in Runtime. If the tag address changes in the PLC and the HMI device is not compiled again and loaded, the change is not registered in runtime. |
| S7-1200 | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |
| S7-1500 | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |
| SIMATIC ET 200 CPU | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |
| SIMATIC S7-1500 software controller | Yes | A validity check of the tag connection is performed in runtime during symbolic addressing. If an address is changed in the PLC, the change is registered and an error message is issued. In the case of absolute addressing, the behavior described for the S7-300/400 applies. |

Create an integrated connection in the "Devices & Networks" editor. If the PLC is contained in the project and integrated connections are supported, you can then also have the connection created automatically. To do this, when configuring the HMI tag, simply select an existing PLC tag to which you want to connect the HMI tag. The integrated connection is then automatically created by the system.

#### Addressing with non-integrated connections

In the case of a project with a non-integrated connection, you always configure a tag connection with absolute addressing. Select the valid data type yourself. If the address of a PLC tag changes in a project with a non-integrated connection during the course of the project, you also have to make the change in WinCC. The tag connection cannot be checked for validity in Runtime, an error message is not issued.

A non-integrated connection is available for all supported PLCs.

Symbolic addressing is not available in a non-integrated connection.

With a non-integrated connection, the control program does not need to be part of the WinCC project. You can perform the configuration of the PLC and the WinCC project independently of each other. For configuration in WinCC, only the addresses used in the PLC and their function have to be known.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of communication (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Internal Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Internal tags do not have any connection to the PLC. Internal tags transport values within the HMI device. The tag values are only available as long as runtime is running.

#### Principle

Internal tags are stored in the memory of the HMI device. Therefore, only this HMI device has read and write access to the internal tags. You can create internal tags to perform local calculations, for example.

You can use the HMI data types for internal tags. Availability depends on the HMI device being used.

The following HMI data types are available:

| HMI data type | Data format |
| --- | --- |
| Array | One-dimensional array |
| Bool | Binary tag |
| DateTime | Date/time format |
| DInt | Signed 32-bit value |
| Int | Signed 16-bit value |
| LReal | Floating-point number 64-bit IEEE 754 |
| Real | Floating-point number 32-bit IEEE 754 |
| SInt | Signed 8-bit value |
| UDnt | Unsigned 32-bit value |
| UInt | Unsigned 16-bit value |
| USInt | Unsigned 8-bit value |
| WString | Text tag, 16-bit character set |

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Internal Tags (RT Professional)

#### Introduction

Internal tags do not have any connection to the PLC.

#### Principle

Internal tags are stored in the memory of the HMI device. Therefore, only this HMI device has read and write access to the internal tags. You can create internal tags to perform local calculations, for example.

You can use the HMI data types for internal tags. Availability depends on the HMI device being used.

The following HMI data types are available:

| HMI data type | Data format |
| --- | --- |
| Array | One-dimensional array |
| Bool | Binary tag |
| DateTime | Date/time format |
| DInt | Signed 32-bit value |
| Int | Signed 16-bit value |
| LReal | Floating-point number 64-bit IEEE 754 |
| Raw | Raw data |
| Real | Floating-point number 32-bit IEEE 754 |
| SInt | Signed 8-bit value |
| String | Text tag, 8-bit character set |
| TextRef | Text reference |
| UDInt | Unsigned 32-bit value |
| UInt | Unsigned 16-bit value |
| USInt | Unsigned 8-bit value |
| WString | Text tag, 16-bit character set |

#### System tags

System tags are required for internal management of the project. The names of these tags always start with the "@" character. You may not delete or rename these tags. You cannot change the value of a tag.

Exceptions are the tags that are created by the "Redundancy" option. These can be set via scripts, for example:

- @RM_MASTER
- @RM_MASTER_NAME

> **Note**
>
> You must not create any tags whose name starts with a @.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adapting-the-data-type-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### System tags (RT Professional)

System tags are required for internal management of the project. The names of these tags always start with the "@" character. You may not delete or rename these tags. You can evaluate the value of the tags, but you cannot change it.

The following tags are exceptions to this rule: These can be set via scripts, for example:

| System tag | Component | Use |
| --- | --- | --- |
| @RM_MASTER and @RM_MASTER_NAME | WinCC redundancy option | You change the value of the redundancy tags via scripts, for example. |
| @PRF_<...>_RESET | System diagnostics | Use these tags to reset the values of performance tags. |
| @<Connectionname>@ForceConnectionStateEx | Connection status | You use the system variable of the channel to establish or terminate the connection. |
| @<Connection name>@ConnectionStateEx* | Connection status | You use the system variable to query the current connection status. |
| *To query the connection status to the PLC you can also use the "Connection status" function in WinCC Explorer. |  |  |

> **Note**
>
> You must not create any tags whose name starts with a @.

#### Diagnostics status

To evaluate the diagnostics status, @DiagnosticsIndicatorTag is available.

| System tag | Data type | Meaning |
| --- | --- | --- |
| @DiagnosticsIndicatorTag | UDInt | Indicates the diagnostics status. The diagnostics status contains the collective status of all relevant PLCs. The worst status of all PLCs is always used in this case.  "@DiagnosticsIndicatorTag" can have the following values:  - Good (0) - Error (1) |

---

**See also**

[System diagnostics with performance tags (RT Professional)](#system-diagnostics-with-performance-tags-rt-professional)
  
[Overview of performance tags (RT Professional)](#overview-of-performance-tags-rt-professional)
  
[Diagnostic Tags of Tag Logging Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#diagnostic-tags-of-tag-logging-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Raw data tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#raw-data-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### System diagnostics with performance tags (RT Professional)

For analysis of the WinCC project, WinCC provides the system tags "@PRF_...".

You use them to evaluate the time response of the server. You can also view this performance evaluation in the Windows system monitor.

#### Creating performance tags

The system tags for performance analysis are available in the default tag table of the HMI device in the "System tags" tab.

The system tags are assigned to various components:

| Tag name | Component | Creation of tags |
| --- | --- | --- |
| @PRF_DMRT_SRV_...  @PRF_DMRT_RESET | WinCC tag management (data manager) | The system tags are generated when you create a WinCC project. |
| @PRF_TLGRT_... | WinCC Tag Logging |  |
| @PRF_ALGRT_... | WinCC Alarm Logging |  |
| @PRF_REDUNDACY_... | WinCC Redundancy |  |
| @PRF_TIMESYNC_ | Basic Process Control: Time Synchronization |  |
| @PRF_CLDCN_... | WinCC/Cloud Connector |  |
| @PRF_DMRT_CHNCON_ <connection name>_... | WinCC Process communication | As soon as you create a new connection, additional performance tags are created for this connection in the database.  These tags are not visible in the "System tags" tab. |
| @PRF_ALGRT_CHNCON_ <connection name>_... | WinCC Alarm Logging |  |

#### Types of performance tags

Performance tags can be assigned to the following data types:

| Tags | Data type | Access | Description |
| --- | --- | --- | --- |
| Relative tags | Floating-point number 64-bit IEEE 754 | Read | Values that are in effect relative to the time of reading, for example, currently pending values or values per second.  The reset tag has no effect on these values.  The tag name ends in:  - ..._ACTIVE - ..._CIENTS - ..._PENDING - ..._PERIOD - ..._QUALITY - ..._QUEUE - ..._SECOND - ..._SIZE - ..._STATE   Update cycle: 1 second |
| Counter tags | Floating-point number 64-bit IEEE 754 | Read | Absolute values since Runtime activation  You can reset the value to "0" using the reset tag.  The tag name ends in:  - ..._AVERAGE - ..._PEAK - ..._TOTAL   The reset behavior depends on the tag:  - ..._COUNT   Update cycle: 1 second |
| Reset tags | Unsigned 32-bit value | Read  Write | You can set the value of the reset tag, for example, via scripts:  - 0: Disabled - 1: The value of all associated counter tags is reset to "0".   The value of the reset tag itself is also reset to "0".   The tag name ends in:  - ...RESET |

#### Display in the Windows system monitor

The Windows system monitor displays counters that correspond to the WinCC Performance tags.

You can find these counters in the following groups:

| Counter group | Performance tags |
| --- | --- |
| WinCC DataManager Server | @PRF_DMRT_SRV_... |
| WinCC Taglogging Server | @PRF_TLGRT_... |
| WinCC Alarmlogging Server | @PRF_ALGRT_... |
| WinCC Redundancy | @PRF_REDUNDACY_... |
| WinCC Time Synchronization | @PRF_TIMESYNC_ |
| WinCC DataManager Connections | @PRF_DMRT_CHNCON_ <connection>_... * |
| WinCC Alarmlogging Connections | @PRF_ALGRT_CHNCON_ <connection name>_... * |
| *) The connections are displayed as instances. |  |

**Procedure**

1. In the Windows program group "Management", open the "Performance Monitor" application.
2. In the navigation area, click on "Performance Monitor" below the "Monitoring Tools".
3. Click the "+" button in the toolbar of the content area
4. In the "Add power indicators" dialog, select the required groups or individual counters.

   To display more details for a selected counter, enable the option "Show description".
5. Click "Add" and close the dialog.

**Example: Display in Runtime**

![Display in the Windows system monitor](images/136809914123_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of performance tags (RT Professional)](#overview-of-performance-tags-rt-professional)
  
[Checking connections with performance tags (RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#checking-connections-with-performance-tags-rt-professional)

### Overview of performance tags (RT Professional)

For analysis of the WinCC project, WinCC provides the system tags "@PRF_...".

You use them to evaluate the time response of the server and the communication connection.

#### Performance tags: Tags

> **Note**
>
> **Connection-specific performance tags**
>
> When a connection is configured, performance tags are created in the database with the names "@PRF_DMRT_CHNCON_<connection name>_...".
>
> These tags are not visible in the "System tags" tab, but can be used just like any other performance tag.
>
> When you link the connection-specific performance tags to objects, the tag assignment will have a red background in the engineering system. However, access in Runtime still works.

| System tag | Description |
| --- | --- |
| @PRF_DMRT_RESET | The Reset tag resets the values of the following performance tags:  - @PRF_DMRT_SRV_..._PEAK - @PRF_DMRT_SRV_..._TOTAL |
| @PRF_DMRT_SRV_CYCLIC_READ_CALLBACKS_PENDING | Tag updates during cyclic reading of client applications that have not been sent yet.  A constantly increasing value indicates a system overload. Possible causes:  - Cyclic read requests are processed too slowly by one or multiple client applications. - Tags are written faster during cyclic reading than the clients can read the values. |
| @PRF_DMRT_SRV_CYCLIC_READ_REQUESTS_ACTIVE | Pending cyclic read requests  A constantly increasing value indicates a system overload. Possible causes:  - Too many active or too slow client applications |
| @PRF_DMRT_SRV_CYCLIC_READ_REQUESTS_TOTAL | Cyclic read requests since activation of Runtime  A value that is increasing relatively quickly can indicate the following behavior:  - Frequent restarts - An inefficient client application |
| @PRF_DMRT_SRV_READ_REQUESTS_ACTIVE | Pending read requests  Cyclic read requests are not included.  A constantly increasing value indicates a system overload. Possible causes:  - A data source is overloaded and does not process the read requests fast enough. - The Data Manager is overloaded. |
| @PRF_DMRT_SRV_READ_REQUESTS_PER_SECOND <sup>1)</sup> | Read requests/second  Cyclic read requests are not included. |
| @PRF_DMRT_SRV_READ_REQUESTS_TOTAL | Read requests since activation of Runtime  Cyclic read requests are not included. |
| @PRF_DMRT_SRV_TAG_READS_PER_SECOND <sup>1)</sup> | Tags read/second  Tag updates are not included dues to cyclic read requests. |
| @PRF_DMRT_SRV_TAG_READS_PER_SECOND_PEAK | Maximum number of read tags/second |
| @PRF_DMRT_SRV_TAG_READS_TOTAL | Tags read since activation of Runtime  Tag updates are not included dues to cyclic read requests. |
| @PRF_DMRT_SRV_TAG_WRITES_PER_SECOND <sup>1)</sup> | Tags written/second |
| @PRF_DMRT_SRV_TAG_WRITES_PER_SECOND_PEAK | Maximum number of written tags/second |
| @PRF_DMRT_SRV_TAG_WRITES_TOTAL | Tags written since activation of Runtime |
| @PRF_DMRT_SRV_WRITE_REQUESTS_ACTIVE | Pending write requests  A constantly increasing value indicates a system overload. Possible causes:  - A data source is overloaded and does not process the write requests fast enough. - The Data Manager is overloaded. |
| @PRF_DMRT_SRV_WRITE_REQUESTS_PER_SECOND <sup>1)</sup> | Write requests/second |
| @PRF_DMRT_SRV_WRITE_REQUESTS_TOTAL | Write requests since activation of Runtime |
| 1) The information "PER_SECOND" refers to the last second prior to the tag update. |  |

#### Performance tags: Data logging

System tags with the names "@TLGRT_..." are created for process value logs.

| System tag | Description |
| --- | --- |
| @PRF_TLGRT_AVERAGE_TAGS_PER_SECOND | Critical indicator for the average performance of the logging system:  Average number of logged tags/second |
| @PRF_TLGRT_MAX_SIZEOF_ARCHIVING_QUEUE | Maximum logging queue size |
| @PRF_TLGRT_MAX_SIZEOF_NOTIFY_QUEUE | Maximum notification queue size  Contains the notifications of all registered WinCC clients |
| @PRF_TLGRT_MAX_TAGS_LAST_SECOND | Maximum number of tags that were logged in all logs one second ago  In conjunction with the value of the tag @PRF_TLGRT_TAGS_PER_SECOND, this value is an indicator for an even logging load. |
| @PRF_TLGRT_MIN_SIZEOF_ARCHIVING_QUEUE | Minimum logging queue size |
| @PRF_TLGRT_MIN_SIZEOF_NOTIFY_QUEUE | Minimum notification queue size  Contains the notifications of all registered WinCC clients |
| @PRF_TLGRT_MIN_TAGS_LAST_SECOND | Minimum number of tags that were logged in all logs one second ago  In conjunction with the value of the tag @PRF_TLGRT_TAGS_PER_SECOND, this value is an indicator for an even logging load. |
| @PRF_TLGRT_SIZEOF_ARCHIVING_QUEUE | Logging queue size |
| @PRF_TLGRT_SIZEOF_NOTIFY_QUEUE | Notification queue size  Contains the notifications of all registered WinCC clients |
| @PRF_TLGRT_TAGS_LAST_SECOND | Number of tags that were logged in all logs one second ago  In conjunction with the value of the tag @PRF_TLGRT_TAGS_PER_SECOND, this value is an indicator for an even logging load. |
| @PRF_TLGRT_TAGS_PER_SECOND <sup>1)</sup> | Critical indicator for the actual performance of the logging system:  Tags that are logged in all logs per second |
| 1) The information "PER_SECOND" refers to the last second prior to the tag update. |  |

#### Performance tags: Alarm logging

> **Note**
>
> **Connection-specific performance tags**
>
> When a connection is configured, performance tags are created in the database with the names "@PRF_ALGRT_CHNCON_<connection name>_...".
>
> These tags are not visible in the "System tags" tab, but can be used just like any other performance tag.
>
> When you link the connection-specific performance tags to objects, the tag assignment will have a red background in the engineering system. However, access in Runtime still works.

Performance tags with the names "@PRF_ALGRT_CHNCON_<connection name>_..." are created for the communication channels in use.

| System tag | Description |
| --- | --- |
| @PRF_ALGRT_RESET | The reset tag resets the performance tags that contain absolute values since Runtime activation:  - @PRF_ALGRT_..._AVERAGE - @PRF_ALGRT_..._PEAK - @PRF_ALGRT_..._TOTAL |
| @PRF_ALGRT_ALARMS_PER_SECOND <sup>1)</sup> | Critical indicator for the current performance of the alarm system:  Number of generated alarms/second |
| @PRF_ALGRT_ALARMS_PER_SECOND_AVERAGE | Critical indicator for the average performance of the alarm system:  Average number of alarms/second |
| @PRF_ALGRT_ALARMS_PER_SECOND_PEAK | Maximum number of alarms/second |
| @PRF_ALGRT_ALARMS_TOTAL | Number of generated alarms since activation of Runtime |
| @PRF_ALGRT_ARCHIVING_QUEUE_SIZE | Current logging queue size |
| @PRF_ALGRT_ARCHIVING_QUEUE_SIZE_PEAK | Maximum logging queue size |
| @PRF_ALGRT_CLIENTS | Number of currently connected clients  All WinCC clients on which Alarm Logging Runtime is running are counted, for example, WebUX clients and WebNavigator clients. |
| @PRF_ALGRT_CLIENTS_AVERAGE | Average number of connected clients/second since activation of Runtime |
| @PRF_ALGRT_CLIENTS_PEAK | Maximum number of simultaneously connected clients |
| @PRF_ALGRT_INPUT_QUEUE_SIZE | Current input queue size |
| @PRF_ALGRT_INPUT_QUEUE_SIZE_PEAK | Maximum input queue size |
| @PRF_ALGRT_QUALITY | Utilization of the communication channel:  - 0: Good, utilization up to max. 70% - 10: Critical, utilization 70% to 100% - 20: Overflow, alarm loss |
| 1) The information "PER_SECOND" refers to the last second prior to the tag update. |  |

#### Performance tags: Redundancy

The performance tags @PRF_REDUNDANCY_... map the states of the redundant servers.

| System tag | Description |
| --- | --- |
| @PRF_REDUNDANCY_IS_SYNCHRONIZED | Synchronization status:  - 0: Redundant applications are not synchronized. - 1: Redundancy synchronization of all applications is complete.   In addition to WinCC, the status can be influenced by other applications registered for the redundancy, for example, SIMATIC BATCH. |
| @PRF_REDUNDANCY_VALIDATION | Validation points of the server. The validation value determines which server will be the primary server.  The validation value depends, for example, on the connection and Runtime status.  If the redundancy was configured correctly, the validation value is the same on both redundant servers.  When the validation values are not identical, the server with the greater value will become the primary server.  Typical values:  - 37: The server status is good.   - Runtime is active.   - Redundant connection over serial interface - 35: The server status is good.   - Runtime is active.   - Redundant connection over LAN - < 35: The server has the internal status "FAULT".   Check the connection status or the server status. The "FAULT" status is set for a critical operating state, for example, when a server application no longer responds.   When a server takes on the "FAULT" status, the partner server becomes the primary server.   Example calculations:  - When Runtime is disabled on the server, the validation is reduced by four points. - When the terminal bus cannot be reached, validation is reduced by 20 points. |
| @PRF_REDUNDANCY_PARTNER_VALIDATION | Validation points of the redundant partner server  If the redundancy was configured correctly, this value is the same on both redundant servers. |
| @PRF_REDUNDANCY_AS_COUNT | Number of AS connections on the server  If the redundancy was configured correctly, this value is the same on both redundant servers.  The following conditions cause a redundancy switchover:  - The validation values are identical on the redundant servers. - The number of AS connections is different.   In this case, the server with more AS connections will become the primary server. |
| @PRF_REDUNDANCY_PARTNER_AS_COUNT | Number of AS connections on the redundant partner server  If the redundancy was configured correctly, this value is the same on both redundant servers. |
| @PRF_REDUNDANCY_CURRENT_STATE | Redundancy status of the server:  - 0: Undefined status - 1: Server is primary server - 2: Server is standby - 3: Server is in "FAULT" status - 4: Server is standalone or no redundant operation |
| @PRF_REDUNDANCY_PARTNER_CURRENT_STATE | Redundancy status of the redundant partner server |
| @PRF_REDUNDANCY_FAULT_POSTPONED | Tag value = 1: The server has the status "FAULT_POSTPONED".  The internal state of the local server is "FAULT", but the partner server cannot assume the "Master" state. A redundancy switchover is not possible. The cause is, for example, an ongoing redundancy synchronization.  As soon as the conditions for a redundancy switchover are met, the server changes to the "FAULT" status. The tag "@PRF_REDUNDANCY_CURRENT_STATE" takes on the value "3". |
| @PRF_REDUNDANCY_PARTNER_FAULT_POSTPONED | Tag value = 1: The redundant partner server has the status "FAULT_POSTPONED". |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT | Number of redundancy switchovers since activation of Runtime or since the last reset with "@PRF_REDUNDANCY_SWITCHOVER_COUNT_RESET". |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT_PERIOD | Number of redundancy switchovers in a defined period  Default setting:  - Time period: 1 calendar day - The value is reset every day at midnight (0:00). |
| @PRF_REDUNDANCY_SWITCHOVER_COUNT_RESET | The reset tag resets the value of the following performance tag:  - @PRF_REDUNCANCY_SWITCHOVER_COUNT |

#### Performance tags: Time synchronization

| System tag | Description |
| --- | --- |
| @PRF_TIMESYNC_CURRENT_STATE | Status of the time synchronization. The value depends on the role of the device.  Standby:  - 0: No primary server available. Synchronization is not possible. - 1: Primary server for synchronization is connected.   Primary server:  - 0: It is not possible to send time frames over the system bus. - 1: Time frames are sent over the system bus. |
| @PRF_TIMESYNC_SIGNAL_QUALITY | Quality of the external signal with which the local time is synchronized  - The values 1 to 4 stand for "weak" to "very good". - 0: No signal received or the tag is not updated. |
| @PRF_TIMESYNC_TIME_DIFF | Time difference between the local system and the time specified in the telegram of the primary server  Unit: millisecond |
| @PRF_TIMESYNC_RESET | Currently not in use. |

#### Performance tags: Cloud Connector

| System tag | Description |
| --- | --- |
| @PRF_CLDCN_RESET | The reset tag resets the values of the following performance tags:  - @PRF_CLDCN_TAG_FAILED_WRITES_TOTAL - @PRF_CLDCN_TAG_WRITES_TOTAL |
| @PRF_CLDCN_TAG_FAILED_WRITES_TOTAL | Number of transmitted tags that were not acknowledged by the cloud |
| @PRF_CLDCN_TAG_WRITES_PER_SECOND | Number or tags transmitted per second |
| @PRF_CLDCN_TAG_WRITES_TOTAL | Total number of tags transmitted over a connection |

### Diagnostic Tags of Tag Logging Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

The diagnostic tags for Tag Logging enable you to record the current archiving performance of the system.

Diagnostic tags are created as internal tags in the WinCC Explorer and are part of the "TagLoggingRT" tag group.

You can use the system tags in the "Performance" tag group to evaluate the time behavior of the server and the communication connection.

#### @TLGRT_TAGS_PER_SECOND

The tag specifies the average archiving rate of Tag Logging cyclically as an archive tag per second.

#### @TLGRT_AVERAGE_TAGS_PER_SECOND

The tag specifies the arithmetic average value of the average archiving rate of Tag Logging cyclically as an archive tag per second since Runtime as started.

#### @TLGRT_SIZEOF_NOTIFY_QUEUE

This tag contains the current number of entries in the ClientNotify queue.

All local trend and table windows receive their current data from this queue.

#### @TLGRT_SIZEOF_NLL_INPUT_QUEUE

This tag contains the current number of entries in the queue for the format DLL.

This queue archives values that are transmitted by the raw data tag.

### Raw data tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Definition

In WinCC, you can create external and internal tags of the type "Raw data type". The format and the length of a raw data tag are not fixed. Its length can be in the range from 1 and 65535 bytes. It is either defined by the user or results from a specific application.

The contents of a raw data tag are not fixed. Only senders and receivers can interpret the contents of a raw data tag. They are not interpreted by WinCC.

> **Note**
>
> A raw data tag cannot be displayed in screens.

#### Potential Applications within WinCC

Raw data tags can be used in the following areas in WinCC:

- For data exchange with the PLC alarm blocks for processing and acknowledgment of alarms.
- In scripts for data exchanged with the help of functions "Get/SetTagRaw".
- In tag logs
- To transfer jobs, data, processing acknowledgments between WinCC and the PLC.

  > **Note**
  >
  > When the raw data tag is displayed in an I/O field, you must observe the conventions of the string with a "\0" character at the end.

#### "Properties address"

For external raw data tags, the "Address properties" dialog is not the same for all communication drivers because the parameters of the tag address and the supported raw data tag types depend on the type of communication being used.

#### Format adaptation

There is no format adaptation in WinCC for the "raw data type".

## Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Creating tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating internal tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-internal-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Updating internal tags project-wide or locally (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#updating-internal-tags-project-wide-or-locally-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating multiple tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-multiple-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adapting-the-data-type-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can access an address in the PLC via a PLC tag using an external tag. The following options are available for addressing:

- Symbolic addressing
- Absolute Addressing

You can find further details on symbolic addressing in section "[Addressing external tags](#addressing-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)". If possible, use symbolic addressing when configuring a tag. You create tags either in the standard tag table or in a tag table you defined yourself.

##### Requirement

- You have opened the project.
- A connection to the PLC is configured.
- The Inspector window is open.

##### Procedure

To create an external tag, proceed as follows:

1. Open the "HMI tags" folder in the project tree and double-click the standard tag table. The tag table open.  
   Alternatively, create a new tag table and then open it.
2. In the "Name" column, double-click "Add" in the tag table. A new tag is created.
3. Select the "Properties > Properties >General" category in the Inspector window and, if required, enter a unique tag name in the "Name" field. The tag name must be unique throughout the device.
4. If required, select the "Display name" field to enter a name to be displayed in Runtime. The name to be displayed is language-specific and can be translated for the required Runtime languages. The display name is available for Basic Panels, Panels and Runtime Advanced.
5. Select the connection to the required PLC in the "Connection" box. If the connection you require is not displayed, you must first create the connection to the PLC. You create the connection to a SIMATIC S7 PLC in the "Devices & Networks" editor. You create the connection to external PLCs in the "Connections" editor.  
   If the project contains the PLC and supports integrated connections, you can also have the connection created automatically. To do this, when configuring the HMI tag, simply select an existing PLC tag to which you want to connect the HMI tag. The integrated connection is then automatically created by the system.
6. If you are working with an integrated connection, click the ![Procedure](images/70487246859_DV_resource.Stream@PNG-de-DE.png) button in the "PLC tag" field and select an already created PLC tag in the object list. Click the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) button to confirm the selection.

   ![Procedure](images/111879727499_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111879727499_DV_resource.Stream@PNG-en-US.png)

   Alternatively, use the autocomplete to select a PLC tag for an integrated connection.

   If you select a PLC tag from the autocomplete list, it is entered in the input path. The elements of the PLC tags are displayed in the autocomplete list. If you have selected a PLC tag that can be connected to the HMI tags, the PLC tag is connected to the HMI tags.
7. If you are working with a non-integrated connection, enter the address from the PLC in the "Address" field. The "PLC tag" field remains empty.
8. Configure the other properties of the tag in the inspector window.

You can also configure all tag properties directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu.

You can also create new tags alternatively directly at the application point, e.g. on an I/O field. To do this, click the ![Procedure](images/70485818891_DV_resource.Stream@PNG-en-US.png) button in the object list. You then configure the new tag in the Inspector window.

##### Result

An external tag has been created and linked to a PLC tag or an address in the PLC.

##### Alternative procedure

You can also create external HMI tags by dragging and dropping data block elements or global PLC tags in an HMI tag table.

---

**See also**

[Creating internal tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-internal-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating multiple tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-multiple-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Addressing external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adapting-the-data-type-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating internal tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You must at least set the name and data type for internal tags. The "Internal tag" item is selected, rather than a connection to a PLC.  
For documentation purposes, it is a good idea to enter a comment for every tag.

##### Requirement

You have opened the project.

##### Procedure

1. Open the "HMI tags" folder in the project tree and double-click the entry "Standard tag table". The tag table opens.  
   Alternatively, create and then open a new tag table.
2. Double-click "Add" in the "Name" column of the tag table. A new tag is created.
3. If the Inspector window is not open, select the "Inspector window" option in the "View" menu.
4. Select the "Properties > Properties >General" category in the Inspector window and, if required, enter a unique tag name in the "Name" field. This tag name must be unique throughout the project.
5. If required, select the "Display name" field to enter a name to be displayed in Runtime. The name to be displayed is language-specific and can be translated for the required Runtime languages. The display name is available for Basic Panels, Panels and Runtime Advanced.

   ![Procedure](images/131117628299_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131117628299_DV_resource.Stream@PNG-en-US.png)
6. Select "Internal tag" as the connection in the "Connection" field.
7. Select the required data type in the "Data type" field.
8. In the "Length" field, you must specify the maximum number of characters to be stored in the tag according to the selected data type. The length is automatically defined by the data type for numerical tags.
9. As an option, you can enter a comment regarding the use of the tag. To do so, click "Properties > Properties > Comment" in the Inspector window and enter a text.

You can also configure all tag properties directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu.

You can also create new tags alternatively directly at the application point, e.g. on an I/O field. Click the ![Procedure](images/70485818891_DV_resource.Stream@PNG-en-US.png) button in the object list. You can then configure the new tag in the Properties window that opens.

##### Result

An internal tag is created. You can now use this in your project.

In additional steps you can configure the tag, for example, by setting the start value and limits.

---

**See also**

[Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating OPC UA tags (RT Professional)](OPC%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-opc-ua-tags-rt-professional)

#### Updating internal tags project-wide or locally (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

Internal tags that you create on a WinCC server are always updated project-wide.

Internal tags that you create on a WinCC client with its own project are always updated locally on the computer.

##### Setting the update of the internal tags

1. In the Inspector window, select the category "Properties > Properties > Settings".
2. Select the desired update variant:

   - Client-/Server-wide
   - Local HMI device

![Setting the update of the internal tags](images/142639887883_DV_resource.Stream@PNG-en-US.png)

##### Setting Runtime persistence

If you want the value of the internal tags to be retained when Runtime is stopped, select the check box "Persistence for internal tags".

If the "Local HMI device" setting is enabled, the "Persistence for internal tags" setting has no effect.

Changed tag values are reset again when Runtime is disabled.

#### Creating multiple tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In a tag table, you create additional identical tags by automatically filling the rows of the table below a tag.

The tag names are incremented automatically when filling in automatically.

You can also use the auto fill function to fill table cells below a tag with a single tag property and thus modify the corresponding tags.

If you apply the automatic filling in to already filled cells of a tab table, you will be asked whether you want to overwrite the cells or insert new tags.

If you do not want to overwrite already configured tags, activate insert mode. Activate insert mode by keeping the <Ctrl> key pressed during insertion. Already existing entries in the tag table are moved down if insert mode is activated.

##### Requirement

- You have opened the project.
- A tag table is open.
- The tag which is to serve as a template for other tags is configured.

##### Procedure

1. If you want to create new tags, mark in the "Name" column the tag that should be used as a template for the new tags.

   If you want to copy a property of a tag to the tags below it, select the cell which contains this property.

   The selected cell will be highlighted in color and a small blue square will appear in its bottom right corner. If you move the mouse over this square, the cursor will change to a black cross.

   ![Procedure](images/70484772619_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70484772619_DV_resource.Stream@PNG-en-US.png)
2. Hold down the mouse button and drag this square over the cells below that you wish to fill automatically.

   The marking will be extended to cover this area.

   ![Procedure](images/70484778123_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70484778123_DV_resource.Stream@PNG-en-US.png)
3. Now release the mouse button. All of the marked cells will be filled automatically.

   New tags will be created in all empty cells in the marked area.

   ![Procedure](images/70485139467_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70485139467_DV_resource.Stream@PNG-en-US.png)

##### Result

Depending on which cells were selected, the function may automatically fill individual properties or create new tags.

---

**See also**

[Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you create a tag, you assign one of the possible data types to the tag. This data type depends on the type of data for which you would like to use the tag.

The data types available depend on the connected communication partner, such as a PLC.

> **Note**
>
> If you modify the data type of an existing, external tag, the previously defined tag address is identified as invalid. This reason for this is that the PLC address also changes when the data type is modified.

##### Format adaptation

WinCC sets the data type of an external tag according to the data type of the connected PLC tag. If the data type of the PLC tag is not available in WinCC, a compatible data type is automatically used at the HMI tag. If required, you can specify that WinCC uses a different data type and matches the format of the data type of the PLC tag and the data type of the HMI tag.

In WinCC, you have access to the following data types:

| HMI data type | Description | Value range |
| --- | --- | --- |
| Array | Tag with contained elements<sup>2)3)</sup> |  |
| DateTime | Date/time format<sup>2)</sup> |  |
| SInt | Signed 8-bit value | -128 ... +127 |
| USInt | Unsigned 8-bit value | 0 ... 255 |
| Int | Signed 16-bit value | -32768 ... +32767 |
| UInt | Unsigned 16-bit value | 0 ... 65535 |
| DInt | Signed 32-bit value | -2147483648 ... +2147483647 |
| UDInt | Unsigned 32-bit value | 0 ... 4294967295 |
| Real | Floating-point number 32-bit IEEE 754 | +-3.402823e+38 |
| LReal | Floating-point number 64-bit IEEE 754 | +-1.79769313486231e+308 |
| Bool | Binary tag | 0 ... 1 |
| String | Text tag, 8-bit character set |  |
| WString | Text tag, 16-bit character set |  |
| TextRef | Text reference<sup>1</sup> |  |
| Raw | Raw data type |  |
| <sup>1</sup>: The "TextRef" data type is only available for internal tags. With tags of the "TextRef" data type, you reference an entry in the project texts. If you would like to display a text on an object and if, when the configured language is changed, you want the text to change to that language, use the "TextRef" data type. You have to assign the project text to the variable.   <sup>2</sup>: Only available in conjunction with S7-1200 or S7-1500    <sup>3</sup>: To avoid structural conflicts in runtime, synchronize the tag name and replace the delimiters "[" and "]". |  |  |

For format adaptation, select the desired PLC data type at the respective external tag. The suitable standard data type is then selected automatically in the "HMI data type" field for use in WinCC. Change the format adaptation as required. You can find more detailed information about this in section

[Mapping and coding of data types](#mapping-and-coding-of-data-types-rt-professional)

##### Data types without format adaptation

The data types are shown 1:1 without format adaptation.

**SIMATIC S7-300/400 data types without format adaptation**

| PLC data type | Description |
| --- | --- |
| Bool | No format adaptation |
| String | No format adaptation |

**OPC-DA data types without format adaptation**

| OPC-DA data type | Description |
| --- | --- |
| VT_BSTR | No format adaptation |
| VT_BOOL | No format adaptation |

---

**See also**

[Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Mapping and coding of data types (RT Professional)](#mapping-and-coding-of-data-types-rt-professional)
  
[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Data types (RT Professional)](#data-types-rt-professional)

### Editing Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Edit tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#edit-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring multiple tags simultaneously (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-multiple-tags-simultaneously-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using multiple tags simultaneously in a screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-multiple-tags-simultaneously-in-a-screen-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Synchronizing tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#synchronizing-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can always rename, copy or delete tags.

When a tag is renamed, the new name must be unique for the whole device.

If you use the "Copy" command to copy a tag to the clipboard, the objects and references linked to the tag are copied as well.

If you use the "Insert" command to add a tag to another device, the tag will be added without the connected references. Only the object name of the reference will be inserted. If a reference of the same name and valid properties exists in the target system, the existing reference will then be connected to the copied tag.

If you copy a tag, some of the objects linked to the tag are copied as well. The following objects are copied:

- Logging tags
- Cycles
- Alarms

If you add the copied tag to another device, the tag is added together with the linked objects.

##### Requirements

- The tag which you wish to rename, copy or delete must exist.
- The tag table containing the tag is open.

##### Renaming tags

> **Note**
>
> The connection to the tags can be interrupted in Runtime under the following conditions during renaming:
>
> - HMI tag is used in a type, for example, to dynamize an object property via a script.
> - One or more instances of the type are used in the project.
> - Project is in Runtime.
> - After the renaming, execute the command "Compile > Software (only changes)".
>
> Solution: Exit Runtime and rename the tag. Execute the "Compile > Software (rebuild all)" command.

1. In the "Name" field, select the tag in the tag table.
2. Select "Rename" from the shortcut menu.
3. Type in a new name.

   The tag appears under its new name.

##### Copying tags

1. Select one or more tags in the tag table.
2. Select "Copy" from the shortcut menu.
3. Click on the point at which you want to insert the tag. For example, click another tag table in the same device or the tag table in a second device.
4. Select "Paste" from the shortcut menu. The tag is inserted as described above.

##### Deleting a tag

1. Select one or more tags in the tag table.
2. Select the "Cross-reference" command from the "Tools" menu. In the "Cross-reference" editor, check to see where the tags are used. In this manner, you can see what impact the deletion of the tag will have on your project.
3. Select "Delete" in the pop-up menu of the tag.

   All marked tags will be deleted.

> **Note**
>
> If you want a warning to be output during compiling when HMI tags are deleted in screens, clear the "Do not check deleted HMI tags in screens" check box under "Runtime settings > General > Compiler options". If this option is not activated, the affected field with the deleted tag is marked as invalid.

##### Export and import of tags

WinCC gives you the option to export and import tags. With Export and Import, you have the option to export tags from one project and import them into another project. There is also the option to create larger numbers of tags outside of WinCC, edit them and subsequently import into any WinCC project.

---

**See also**

[Edit tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#edit-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring multiple tags simultaneously (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-multiple-tags-simultaneously-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using multiple tags simultaneously in a screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-multiple-tags-simultaneously-in-a-screen-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Synchronizing tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#synchronizing-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating external tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-external-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing and exporting tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#importing-and-exporting-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Edit tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can modify tags at any time to adapt them to changed requirements in the project.

##### Edit tags

You have the following options to change the configuration of a tag:

- You open the tag table in which the tag is contained.
- Open the tag table "Show all tags".
- You open the Inspector window of a tag with the "Edit" button in the object selection on the display and operating object.

In the tag tables, you can perform such tasks as comparing and adjusting the properties of multiple tags or sorting the tags by their properties.

You can change the properties either directly in the table or in the Inspector window.

If you change a tag property and this change causes a conflict with another property, it will be highlighted in color to draw your attention to this fact. If you link the tag with another controller, for example, which does not support the set data type, this property is highlighted in color.

---

**See also**

[Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring multiple tags simultaneously (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In WinCC, you can assign the same properties to multiple tags in a single operation. This facilitates efficient programming.

##### Requirement

- You created the tags you want to configure.
- The tag table is open.
- The Inspector window is open.

##### Procedure

1. In the tag table, select all the tags that you want to configure at the same time.

   If the selected property is identical for all the tags, the setting for this property will appear in the Inspector window. The associated field will remain blank otherwise.
2. You can define the shared properties in the Inspector window or directly in the tag table.

if you change a property commonly on several tags, only this one property is changed. The other properties of the tag remain unchanged.

##### Result

All marked tags will be reconfigured.

To edit tag properties which differ from one tag to the other, simply clear the multiple selection.

---

**See also**

[Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Using multiple tags simultaneously in a screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In WinCC, you can create multiple I/O fields that are linked with tags in one screen in a single operation. This facilitates efficient programming.

##### Requirement

- Several tags are set up.
- A screen is open.

##### Procedure

1. In the project tree, select the required tag table under "HMI tags".

   ![Procedure](images/70488401035_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70488401035_DV_resource.Stream@PNG-en-US.png)
2. Select the detail view at the bottom of the project tree. The detail view shows the tags that exist in the selected tag group.

   ![Procedure](images/70488484747_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70488484747_DV_resource.Stream@PNG-en-US.png)
3. Mark the tags in the detail window.
4. Drag the tags to the screen. For each tag, this creates an I/O field that is connected to the tag.

> **Note**
>
> When you move a PLC tag from the detail window to the work area by drag&drop, a network and a connection are created additionally in the "Devices & Networks" editor.

---

**See also**

[Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In WinCC, you can map the location of a data value in the structure of a data block in the WinCC tag name. To do this, you synchronize the WinCC tags with the connected PLC tags. If necessary, the PLC name is set as a prefix.

You configure the name matching based on the requirements of your project set under "Runtime Settings > Settings for Tags". WinCC offers you several options for this.

You specify whether the names are matched and the conditions for this to occur during synchronization.

##### Settings for tags

To avoid conflicts within complex tag types that you configure under "Settings for tags", the delimiters of the path statement from STEP 7 are replaced in WinCC similar to name matching:

- Compatibility mode

  In compatibility mode, an underscore is set between the names of the data block and the element name of the first hierarchy level. The delimiters in the lower hierarchy levels are retained. When you enable this option, all other options are disabled.
- Replace delimiter

  Depending on your selection, the delimiters of all hierarchy levels are replaced during synchronization.
- PLC prefix

  The PLC name is set as a prefix to the WinCC tag name. You set the option for each HMI connection.

> **Note**
>
> **Duplicate tag names**
>
> If the newly generated tag name is already in use, a number is added in parentheses, for example, Datablock_1_Static_2{1}(1).

##### Example

The "PLC1" controller contains the structured data block "DB1". The "Db1.a[1].b.c[3]" data block element is used in a picture. Depending on your settings, the WinCC tag name is generated as follows:

| WinCC tag name | Selected option | Comment |
| --- | --- | --- |
| Db1_a[1].b.c[3] | Compatibility mode |  |
| Plc1.Db1.a[1].b.c[3] | PLC prefix |  |
| Db1;a(1);b;c(3) | Dot and parenthesis replaced with ; ( ) |  |
| Plc1_Db1_a{10}_b_c{3} | Dot and parenthesis replaced with _ { }  PLC prefix |  |
| Db1.a[1].b.c[3] | Delimiter replaced without character selection | The tag name is enclosed in quotes at the point of use in the picture: "Db1.a[1].b.c[3]" |

---

**See also**

[Synchronizing tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#synchronizing-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Synchronizing tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To synchronize the PLC and HMI tags, WinCC offers the following options:

- Synchronizing tags with or without name matching between PLC and WinCC

  The following options are available for this:
- Link tags with addresses in the PLC

  This procedure is suitable, for example, if changes were made to the connection between the HMI device and the PLC and the tag connections were lost. The function can also be used if you have configured the control program and HMI project separately.

##### Requirement

- External HMI tags have been created.
- PLC tags have been created.
- An HMI connection to a PLC in the project has been established.

##### Procedure

To synchronize HMI tags with PLC tags, follow these steps:

1. In the project tree, select the directory that contains the tags in question.
2. Select "Connect HMI tags to matching PLC tags" from the shortcut menu.

   A dialog opens.

   ![Procedure](images/89640849291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/89640849291_DV_resource.Stream@PNG-en-US.png)
3. Select the option you want to use.

   If you want to synchronize the tags without name matching, disable "Replace WinCC tag name with PLC tag name".

   If you want to connect HMI tags new with absolute access, select "Data type and absolute address match".
4. Confirm with "Synchronize".

   The system searches for a suitable PLC tag according to the selected option.

##### Result

The external HMI tags are synchronized with the PLC tags.

If you have selected the option "Data type and absolute address match", the tag connection is established as soon as a suitable PLC tag is found.

If you have selected a different option, the WinCC tags are updated accordingly and the PLC tag names are applied in WinCC.

---

**See also**

[Manage tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#manage-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Tag Configuration Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#tag-configuration-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Special configuration options (Basic Panels, Panels, Comfort Panels, RT Advanced)](#special-configuration-options-basic-panels-panels-comfort-panels-rt-advanced)
- [Special configuration options (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#special-configuration-options-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Tag Configuration Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining Limits for a Tag (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-limits-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)
- [Start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Defining the start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Connecting a tag to another PLC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#connecting-a-tag-to-another-plc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Linear scaling of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#linear-scaling-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Applying linear scaling to a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#applying-linear-scaling-to-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Making characters available for HMI tags of the type WString/WChar (Panels, Comfort Panels, RT Advanced, RT Professional)](#making-characters-available-for-hmi-tags-of-the-type-wstringwchar-panels-comfort-panels-rt-advanced-rt-professional)

##### Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

You can restrict the value ranges with limits for numerical tags.

###### Principle

You can specify a value range defined by a high limit and a low limit for numerical tags.

You configure four limit values that limit the value range. Using the limits Upper 2 and Lower 2 , you specify the maximum and minimum value for the value range. The limits Upper 1 and Lower 1 specify the threshold values at which the normal range is exceeded or undershot.

| Limit | Use |
| --- | --- |
| Upper 2 | Specifies the maximum value. |
| Upper 1 | Specifies the value at which the normal range is exceeded. |
| Lower 1 | Specifies the value at which the normal range is undershot. |
| Lower 2 | Specifies the minimum value. |

If the operator enters a value for the tag that is outside the configured value range, the input is rejected. The value is not accepted. You configure a function list when configuring for Runtime Advanced and Panels. When the tag value leaves the value range, the function list is processed.

> **Note**
>
> If you want to output an analog alarm when a limit is violated, configure the respective tag in the "Analog alarms" tab. You can also configure the analog alarm in the "HMI alarms" editor. The values for output of an analog alarm depend on the configured tag limits.

###### Application example

Use the limits to warn the operator when the value of a tag enters a critical range, for example.

---

**See also**

[Defining Limits for a Tag (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-limits-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)
  
[Start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Defining the start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Connecting a tag to another PLC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#connecting-a-tag-to-another-plc-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Linear scaling of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#linear-scaling-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Applying linear scaling to a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#applying-linear-scaling-to-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Defining Limits for a Tag (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

For numerical tags, you can specify a value range by defining a low and high limit as well as the threshold values.

> **Note**
>
> No limits can be defined for arrays or individual array elements. To define limit values, use numeric tags.

For Runtime Advanced and Panels you can configure the system to process a function list whenever a tag value drops below or exceeds its configured value range.

###### Requirements

- The tag for which you want to set the limits is created.
- The Inspector window with the properties for this tag is open.

###### Procedure

To define limits for a tag, proceed as follows:

1. In the Inspector window, select "Properties > Properties > Range". If you want to define one of the limits as a constant value, select "Constant" using the ![Procedure](images/13196575115_DV_resource.Stream@PNG-de-DE.png) button. Enter a number in the relevant field.

   If you want to define one of the limits as a tag value, select "HMI tag" using the ![Procedure](images/13196575115_DV_resource.Stream@PNG-de-DE.png) button. Use the object list to define the tag for the limit.
2. To set additional limits for the tag, repeat step 1 with the appropriate settings.

###### Alternative procedure

You can also configure the limits directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu.

###### Configuring a function list for Runtime Advanced and Panels

When you configure Runtime Advanced and Panels, you can have a function list called up if a high or low limit is violated.

1. If you want to start a function list when the value drops below the value range, click "Properties > Events > On falling below" in the Inspector window. Create a function list in this dialog.
2. If you want to start a function list when the value exceeds the value range, click "Properties > Events > On exceeding" in the Inspector window. Create a function list in this dialog.

###### Result

You have set a value range defined by the limits for the selected tag. If the value range is exceeded or undershot, a function list may be carried out.

---

**See also**

[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)

##### Start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Value of a tag at start of Runtime

You can configure a start value for numeric tags and tags for date/time values. The tag will be preset to this value when Runtime starts. In this way, you can ensure that the tag has a defined status when Runtime starts.

For external tags, the start value will be displayed on the HMI device until it is overwritten by the PLC or by input.

If no start value was configured, the tag contains the value "0" when starting Runtime.

In WinCC Runtime Professional you can enter a tag value in place of the start value on a tag with the "String" data type. The tag value is saved in the "Project texts" editor and is multilingual. After the text has been translated, it is displayed in Runtime as a language-dependent start value.

###### Application example

You can assign a default value to an I/O field. Enter the desired default value as start value for the tag that is linked to the I/O field.

---

**See also**

[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)
  
[Defining the start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Defining the start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In WinCC you can configure a start value for a numeric tag and a tag for date/time values which this adopts at Runtime start.

###### Requirement

- You have created the tag for which you want to define a start value.
- The Inspector window with the tag properties is open.

###### Procedure

To configure a start value, proceed as follows:

1. In the Inspector window select "Properties > Properties > Values."
2. Enter the desired "Start value."

###### Alternative procedure

You can also configure the start value directly in the tag table. To view hidden columns, activate the column titles using the shortcut menu.

###### Result

The start value you selected for the tag is transferred to the project.

---

**See also**

[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)
  
[Start value of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#start-value-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Connecting a tag to another PLC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In WinCC, you can change the PLC connection of a tag at any time. This is needed when you change the configuration of your plant, for example.

Depending on the PLC selected, you may need to modify the configuration of the tag. The tag properties which must be changed will be highlighted in color.

###### Requirement

- The external tag, whose connection you wish to change, must already exist.
- The connection to the PLC must already exist.
- The Properties window for this tag is open.

###### Procedure

To change the PLC connection of a tag, proceed as follows:

1. In the Inspector window select "Properties > Properties > General."
2. Select the new connection in the "Connection" field.

   The tag properties that you must change will be highlighted in color in the tag table and in the Inspector window.
3. Change all highlighted properties of the tag to suit the requirements of the new PLC.

###### Result

The external tag is connected to the new PLC.

---

**See also**

[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)

##### Linear scaling of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

Numeric data types can be processed with linear scaling. The process values in the PLC for an external tag can be mapped onto a specific value range in the project.

###### Principle

To apply linear scaling to a tag, you must specify one value range on the HMI device and one on the PLC. The value ranges will be mapped to each other linearly.

![Principle](images/7022231819_DV_resource.Stream@PNG-en-US.png)

As soon as data from the HMI device is written to an external tag, it will be automatically mapped to the value range of the PLC. As soon as data from the HMI device is read from the external tag, a corresponding transformation will be performed in the other direction.

> **Note**
>
> You can also use the system functions "LinearScaling" and "InvertLinearScaling" to automatically convert process values.

###### Application example

The user enters length dimensions in centimeters but the PLC is expecting inches. The entered values are automatically converted before they are forwarded to the controller. Using linear scaling, the value range [0 to 100] on the PLC can be mapped onto the value range [0 to 254] on the HMI device.

---

**See also**

[Applying linear scaling to a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#applying-linear-scaling-to-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)

##### Applying linear scaling to a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

To apply linear scaling to a tag, you must specify one value range on the HMI device and one on the PLC. The value ranges will be mapped to each other linearly.

###### Requirement

- The external tag to which linear scaling is to be applied must exist.
- The Inspector window with the properties for this tag is open.

###### Procedure

To apply linear scaling to a tag, follow these steps:

1. In the Inspector window select "Properties > Properties > Linear scaling."
2. Click on "Enable" to switch on linear scaling.

   Using this option, you can temporarily switch off linear scaling for testing purposes, for example. Settings which were made earlier for linear scaling remain unchanged.
3. In the "PLC" area, enter the start and end values of the value range to be applied to the process values on the PLC.
4. In the "HMI device" area, enter the end and start values of the value range to be applied to the process values on the HMI device.

###### Result

In Runtime the data will be automatically mapped from one value range to the other.

> **Note**
>
> You can also use the "LinearScaling" and "InvertLinearScaling" system functions to automatically convert process values.

---

**See also**

[Linear scaling of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#linear-scaling-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)

##### Making characters available for HMI tags of the type WString/WChar (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In tags of the type WString or WChar, you specify the strings that can be displayed with specific fonts.

Only those characters that are used in texts in the configuration are transferred to the Basic Panels and Comfort Panels via the configuration. Therefore, it is possible that characters that are displayed via tags of the WString or WChar type are not displayed.

The Tahoma and Courier New fonts are fully pre-installed on the Comfort Panels. The Tahoma font is fully pre-installed on the Basic Panels. The characters of most languages can be displayed with the Tahoma font. The characters of the Chinese, Taiwanese, Japanese and Korean languages cannot be displayed with Tahoma.

WinCC Runtime Advanced supports all fonts that are installed on the configuration PC and the Runtime PC. If you want to use a different font, install it on the configuration PC and the Runtime PC.

For Comfort Panels, it is possible to load the complete font to the HMI device via ProSave.

For Basic Panels, it is not possible to install fonts via ProSave. Therefore, the characters must always be contained in the configured texts.

###### Basics

For Comfort Panels, you can download the following fonts to the HMI device with the additional ProSave options:

- SimSun for the input of strings in Chinese (PRC), Chinese (Singapore), English, German, Italian, French and Spanish.
- Gulim for the input of strings in Korean.
- MS PGothic for the input of strings in Japanese.

You can find additional information on the topic of "Loading Asian fonts via ProSave" under [Loading Asian fonts to the HMI device](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#loading-asian-fonts-to-the-hmi-device-panels-comfort-panels-rt-advanced).

> **Note**
>
> **"Chinese traditional"**
>
> To display traditional Chinese characters, you need the "MingLiU" font. It is not possible to load this font to the Comfort Panels via the ProSave options. The SimSun and Tahoma fonts cannot be used to display traditional Chinese characters.
>
> Therefore, the traditional Chinese characters that occur in WStrings/WChars must be contained in the configured texts on Comfort Panels.

###### **Using characters as configured texts in screens**

To use fonts that are not installed on an HMI device in Runtime, provide the characters as configured texts in a screen:

1. Create a new screen.
2. Insert a text box.
3. In the properties of the text box, set a font that contains characters that you wish to use later.
4. Insert the characters of the font that you wish to use later into the text box.

After the project is compiled, you can use the characters configured in the text in HMI tags of the type WString/WChar.

---

**See also**

[Loading Asian fonts to the HMI device (Panels, Comfort Panels, RT Advanced)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#loading-asian-fonts-to-the-hmi-device-panels-comfort-panels-rt-advanced)

#### Special configuration options (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring address multiplexing with absolute addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-absolute-addressing-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring address multiplexing with symbolic addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-symbolic-addressing-basic-panels-panels-comfort-panels-rt-advanced)
- [Indirect addressing of tags (Panels, Comfort Panels, RT Advanced)](#indirect-addressing-of-tags-panels-comfort-panels-rt-advanced)
- [Addressing tags indirectly (Panels, Comfort Panels, RT Advanced)](#addressing-tags-indirectly-panels-comfort-panels-rt-advanced)
- [Using tags to trigger functions (Panels, Comfort Panels, RT Advanced)](#using-tags-to-trigger-functions-panels-comfort-panels-rt-advanced)
- [Updating the Tag Value in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#updating-the-tag-value-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-the-acquisition-cycle-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)

##### Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Using address multiplexing, you can use a single tag to access a multitude of memory locations within the PLC's address range. You read and write to the addresses without defining a tag for each individual address.

The square brackets indicate address multiplexing.

###### Multiplexing with absolute addressing

When using multiplexing with absolute addressing, you configure tags as placeholders for the address in the PLC to be addressed.

If you want to access, for example, an address of the format "%DBx.DBWy", the expression for multiplexing is as follows:

"%DB[HMITag1].DBW[HMITag2]"

In Runtime, you supply the tag "HMITag1" with the required value for the data block you want to address.

In Runtime, you supply the tag "HMITag2" with the required address from the data block.

Tags are supplied with values, for example, with the help of values from the PLC or via a script.

Multiplexing with absolute addresses is supported for the following PLCs and communication drivers.

- SIMATIC S7-300/400
- SIMATIC S7-1200
- SIMATIC S7-1500

Multiplexing with absolute addresses is not available for data blocks with optimized access.

###### Multiplexing with symbolic addressing

When multiplexing with symbolic addressing, you access various array elements of an array tag in a data block of the connected controller by means of a multiplex tag and an index tag.

First, connect an element of the desired array tags in a data block to the multiplex tags in the HMI device. Then replace the array index (leftmost in the symbolic address) with the index tag.

If you want to access, for example, the various elements of the array tag "Arraytag_1" in the data block "Datablock_1", the expression for symbolic addressing is as follows:

"Datablock_1.Arraytag_1["HMITag_1"]

You control the access to the index of the array elements with the HMI tag "HMITag_1". In Runtime, you supply the tag with the index of the array element that you want to access.

Multiplexing with symbolic addressing is only available if the following components support symbolic addressing:

- HMI device
- PLC
- Communication driver

Symbolic addressing is supported by the following communication drivers:

- SIMATIC S7-1200
- SIMATIC S7-1500

Structured HMI tags with user-defined PLC data types (UDT) and arrays can be used for multiplexing with symbolic addressing.

Multiplexing is possible under the following conditions:

- The path of the connected PLC tag includes at least one array index.
- The array, which is left in the path of the PLC tags, is one-dimensional.
- If there are multiple arrays in the path of the PLC tags, only the array at the far left is available for multiplexing.
- The index tag must be of the "USInt", "UInt", "UDInt", "SInt", "Int" or "DInt" data type.

The following figure shows multiplexing with symbolic addressing using a structured HMI tag with custom PLC data types (UDT). The data block element "db1.udt3Arr[0]" is linked to the HMI tag "db1_udt3Arr{0}". Symbolic addressing of the HMI tag "db1_udt3Arr{0}" is multiplexed by the "index" HMI tag:

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

[Configuring address multiplexing with absolute addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-absolute-addressing-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring address multiplexing with symbolic addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-symbolic-addressing-basic-panels-panels-comfort-panels-rt-advanced)
  
[Updating the Tag Value in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#updating-the-tag-value-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Indirect addressing of tags (Panels, Comfort Panels, RT Advanced)](#indirect-addressing-of-tags-panels-comfort-panels-rt-advanced)
  
[Addressing tags indirectly (Panels, Comfort Panels, RT Advanced)](#addressing-tags-indirectly-panels-comfort-panels-rt-advanced)
  
[Using tags to trigger functions (Panels, Comfort Panels, RT Advanced)](#using-tags-to-trigger-functions-panels-comfort-panels-rt-advanced)
  
[Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-the-acquisition-cycle-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring address multiplexing with absolute addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

When using address multiplexing, you can efficiently access different addresses in the PLC with the help of a small number of tags. Instead of the absolute address in the PLC, you use tags in order to be able to change the address in Runtime.

###### Requirement

- The tag for address multiplexing is created and connected to the PLC.
- The Properties window for this tag is open.

###### Procedure

1. Select the tag for address multiplexing in the tag table, and select "Properties > Properties > General" in the Inspector window. The general properties of the tag are displayed.

   ![Procedure](images/70497360907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70497360907_DV_resource.Stream@PNG-en-US.png)
2. Select the "Int" data type for this example.
3. Select the access type "Absolute addressing".
4. Click the selection button in the "Address" field. The address dialog opens.

   ![Procedure](images/70497393675_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70497393675_DV_resource.Stream@PNG-en-US.png)
5. Click the selection button in the "DB number" field and select the entry "HMI tag".

   ![Procedure](images/70497746443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70497746443_DV_resource.Stream@PNG-en-US.png)
6. In the "DB number" field, click the ![Procedure](images/70487246859_DV_resource.Stream@PNG-de-DE.png) button and select a tag for the DB number in the object list. Or create a new tag with the help of the object list. Accept the tag by clicking the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) button.

   ![Procedure](images/70498649611_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70498649611_DV_resource.Stream@PNG-en-US.png)
7. Repeat steps 3 and 4 for the "Address" field and configure a further tag for calling the address area in the data block.

   ![Procedure](images/70499080203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70499080203_DV_resource.Stream@PNG-en-US.png)

The selection options in the Address dialog depend on the selected data type of the multiplex tag. The Address dialog offers only address settings that can be configured with the selected data type.

###### Result

In runtime, the multiplex tag is used to access the memory location corresponding to the address currently found in the tag. You control access to the data block with the tag in the DB number field. You control access to the address in the selected data block with the tag in the "Address" field.

> **Note**
>
> The value in the memory location will only be read at the next update cycle for the addressed tag.
>
> If, for example, you use a multiplex tag in a script, do not attempt to access contents of the memory location directly after changing it.

---

**See also**

[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring address multiplexing with symbolic addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-symbolic-addressing-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring address multiplexing with symbolic addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

When using address multiplexing, you can efficiently access different addresses in the PLC with the help of a small number of tags. Instead of the symbolic address in the PLC, you use tags in order to be able to change the address in Runtime.

###### Requirement

- The tag for address multiplexing is created.
- The Properties window for this tag is open.
- A data block with an array tag is created in the connected PLC.
- The data block was compiled.

###### Procedure

1. Select the tag for address multiplexing in the tag table, and select "Properties > Properties > General" in the Inspector window. The general properties of the tag are displayed.

   ![Procedure](images/70501480715_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70501480715_DV_resource.Stream@PNG-en-US.png)
2. Select the connection to the PLC via the "Connection" field.

   ![Procedure](images/70501603083_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70501603083_DV_resource.Stream@PNG-en-US.png)
3. Select the access type "Symbolic access".
4. Navigate to the data block of the PLC via the "PLC tag" field and select an array element of the array tag.

   ![Procedure](images/70501994507_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70501994507_DV_resource.Stream@PNG-en-US.png)
5. Click the selection button in the "Address" field. The address dialog opens.
6. Click the selection button in the "Index tag" field and select the entry "HMI tag".

   ![Procedure](images/21487263627_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/21487263627_DV_resource.Stream@PNG-en-US.png)
7. In the "Index tag" field, click the ![Procedure](images/70487246859_DV_resource.Stream@PNG-de-DE.png) button and select a tag for the array index in the object list. Or create a new tag with the help of the object list. Accept the tag by clicking the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) button.

   ![Procedure](images/21487400331_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/21487400331_DV_resource.Stream@PNG-en-US.png)

###### Result

In Runtime, the array element whose index value is contained in the index tag is accessed.

---

**See also**

[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring address multiplexing with absolute addressing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-address-multiplexing-with-absolute-addressing-basic-panels-panels-comfort-panels-rt-advanced)

##### Indirect addressing of tags (Panels, Comfort Panels, RT Advanced)

###### Principle

In multiplexes, a type of indirect addressing, the tag used is first determined at runtime. A list of tags is defined for the multiplex tag. The relevant tag is selected from the list of tags in runtime. The selection of the tag depends on the value of the index tag.

In Runtime, the system first reads the value of the index tag. Then the tag which is specified in the corresponding place in the tag list is accessed.

###### Application example

Using indirect addressing, you could configure the following scenario:

The operator selects one of several machines from a selection list. Depending on the operator's selection, data from the selected machine will be displayed in an output field.

To configure such a scenario, configure the index tag for a symbolic I/O field. Configure the multiplex tag at an I/O field. Configure the tag list of the multiplex tag to reflect the structure of the selection list.

If the operator selects another machine, the value of the index tag will change. The selection field then displays the content of the tag that is pointed to in the tag list in the multiplex tag by the new index value.

---

**See also**

[Addressing tags indirectly (Panels, Comfort Panels, RT Advanced)](#addressing-tags-indirectly-panels-comfort-panels-rt-advanced)
  
[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)

##### Addressing tags indirectly (Panels, Comfort Panels, RT Advanced)

###### Introduction

With indirect addressing, the tag used is first determined at runtime. Instead of a single tag, a list of tags is defined. The list entries consist of an index value and the name of the tag to be used. You can control which entry in the tag list is accessed using an index tag.

> **Note**
>
> **Data type of the index tags**
>
> If you use tags in the tag list with different data types, the properties of the largest data type are used. If you use tags of the INT and REAL data types, for example, the values are shown in floating point numbers.

###### Requirement

- The tag which you wish to address indirectly must already exist.
- The index tag must exist.
- The tags which will be contained in the tag list must already exist.
- The Inspector window with the tag properties is open.

###### Procedure

To address tags indirectly, proceed as follows:

1. In the Inspector window select "Properties > Properties > Multiplexing".
2. Select the "Multiplexing" option to activate indirect addressing.

   Using this option, you can temporarily switch off indirect addressing for testing purposes, for example. Settings which were made earlier for indirect addressing remain unchanged.
3. Select an "Index tag" or define a new tag using the object list.
4. Click the first entry in the "Tags" column in the tag list.
5. Select a tag as a list entry or define a new tag using the object list.

   The entry in the "Index" column will be generated automatically.
6. Repeat step 5 for all tags that you wish to add to the tag list.
7. If necessary, you can use drag-and-drop to change the order of the entries in the list.

###### Result

In runtime, the system will dynamically access the tag in the tag list which has the same index value as the value currently in the index tag.

---

**See also**

[Indirect addressing of tags (Panels, Comfort Panels, RT Advanced)](#indirect-addressing-of-tags-panels-comfort-panels-rt-advanced)
  
[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)

##### Using tags to trigger functions (Panels, Comfort Panels, RT Advanced)

###### Introduction

You can use the values of variables as the triggering event for an action in runtime. To start an action in Runtime, configure a function list for a tag. Include one or more system functions or VB scripts in the function list. The function list is processed when the configured event occurs.

The following events are available for a tag:

- Change in value of the tag

  Function list processing is triggered by each change in the value of the variable.

  When the tag is defined as an array tag, the function list is processed whenever an array element changes.
- Violation of the tag's high limit

  The function list is processed when the high limit is violated.
- Violation of the tag's low limit

  The function list is processed when the low limit is violated.

###### Requirement

- The tag whose value you wish to use as an event already exists.
- The Inspector window with the properties for this tag is open.

###### Procedure

To configure a tag with a function list, proceed as follows:

1. Under "Properties > Events >" in the Inspector window, select the event for which you want to create a function list.

   The function list associated with the selected event is shown.
2. Click "<Add function>". The second table column contains a selection button.
3. Click the selection button and select a system function.
4. Define the parameter values.

Alternatively, select a script to run in the function list, rather than a system function. The "VB scripts" entry is only displayed if there is a script available in the project.

###### Result

If the configured event occurs in Runtime, the function list or the script is processed.

---

**See also**

[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)

##### Updating the Tag Value in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Tags contain process values which change while Runtime is running. Value changes are handled differently at internal and external tags.

###### Principle

When Runtime starts, the value of a tag is equal to its start value. Tag values change in Runtime.

In Runtime, you have the following options for changing the value of a tag:

- A value change in an external tag in the PLC.
- By input, for example, in an I/O field.
- By running a system function, such as "SetValue."
- A value assignment in a script.

###### Updating the Value of External Tags

The value of an external tag is updated as follows:

- Cyclic in operation

  If you select the "Cyclic in operation" acquisition mode, the tag is updated in Runtime while it is displayed in a screen or is logged. The acquisition cycle determines the update cycle for tag value updates on the HMI device. You can either choose a default acquisition cycle or define a user-specific cycle.
- Cyclic continuous

  If you select the "Cyclic continuous" acquisition mode, the tag will be updated continuously in Runtime, even if it is not in the currently-open screen. This setting is activated for tags that are configured to trigger a function list when their value changes, for example.

  Only use the "Cyclic continuous" setting for tags that must truly be updated. Frequent read operations increase communication load.
- On demand

  If you select the "On demand" acquisition mode, the tag is not updated cyclically. It will only be updated on demand using the "UpdateTag" system function, for example, or by a script.

---

**See also**

[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)

##### Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

The value of an external tag can be changed in Runtime by the PLC to which the tag is linked. To ensure that the HMI device is informed of any changes in tag values by the PLC, the values must be updated on the HMI. The value is updated at regular intervals while the tag is displayed in the process screen or is logged. The interval for regular updates is set with the acquisition cycle. The update can also be made continuous.

###### Requirement

- You have created the tag for which you want to define an acquisition cycle.
- The Inspector window with the tag properties is open.

###### Procedure

To configure an acquisition cycle for a tag, follow these steps:

1. In the Inspector window select "Properties > Properties > General."
2. If you want to update the tag at regular intervals as long as it is being displayed on the screen or logged, select "Cyclic in operation" as the acquisition mode.  
   Or:  
   If you want to update the tag at regular intervals even though it is not being displayed on the screen or logged, select "Cyclic continuous" as the acquisition mode.  
   The "Cyclic continuous" setting is selected for a tag, for example, that has a function list configured for a change of its value and that is not directly visible in a screen.
3. Select the required cycle time in the "Acquisition cycle" field or define a new acquisition cycle using the object list.

Alternatively, you can configure the acquisition cycle directly in the work area of the tag table. To view hidden columns, activate the column titles using the shortcut menu.

> **Note**
>
> Only use the "Cyclic continuous" acquisition mode for tags that really have to be continuously updated. Frequent read operations generate a heavy communication load.

> **Note**
>
> For structured HMI tags, the acquisition mode can be selected for the respective structured HMI tag as well as their individual subordinate elements. The acquisition mode of the elements of the array tag cannot be changed. The elements of the array tag is automatically assigned to the acquisition mode of the higher-level array tag.
>
> When the acquisition mode of structured HMI tags is changed, it is applied to all subordinate elements. This means changing the acquisition mode may overwrite subordinate elements.

###### Result

The configured tag is updated in Runtime with the selected acquisition cycle.

---

**See also**

[Address multiplexing (Basic Panels, Panels, Comfort Panels, RT Advanced)](#address-multiplexing-basic-panels-panels-comfort-panels-rt-advanced)

#### Special configuration options (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Defining a substitute value (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-a-substitute-value-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-acquisition-cycle-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Indirect addressing of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#indirect-addressing-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Addressing tags indirectly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-tags-indirectly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Monitor connection status (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#monitor-connection-status-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Defining a substitute value (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can define a specific value as a substitute value for a tag.

In the "Use substitute value" area you define when WinCC should use this substitute value. The current process value is then not accepted from the automation system.

![Introduction](images/21731100811_DV_resource.Stream@PNG-en-US.png)

You can define a substitute value for the following cases:

- As start value

  WinCC sets the substitute value when the project is activated and there is no current process value.
- After communication error

  WinCC sets the substitute value when the connection to the automation system is disturbed and there is no valid process value.
- Maximum exceeded

  If you have set an upper limit for the tag, WinCC sets the substitute value as soon as the process value exceeds this upper limit.
- Minimum undershot

  If you have set a lower limit for the tag, WinCC sets the substitute value as soon as the process value falls below this lower limit.

###### Requirement

- The tag table is open.
- The Inspector window with the tag properties is open.

###### Procedure

To configure a substitute value, follow these steps:

1. Select the desired tag in the tag table, and select "Properties > Properties > Values" in the Inspector window.
2. In the "Use substitute value" segment, select when you want WinCC to use this substitute value in the tag.
3. Enter the required substitute value in the "Substitute value" field.

###### Result

The configured tag is populated with the substitute value in Runtime once the selected condition is fulfilled.

> **Note**
>
> If you have set a high or low limit in an I/O field, you cannot enter any value outside these limits.
>
> WinCC ignores incorrect entries and therefore does not set a substitute value. The substitute value is only set by WinCC when an incorrect process value is read.

---

**See also**

[Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-acquisition-cycle-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag Limits (Basic Panels, Panels, Comfort Panels, RT Advanced)](#tag-limits-basic-panels-panels-comfort-panels-rt-advanced)
  
[Indirect addressing of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#indirect-addressing-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Addressing tags indirectly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-tags-indirectly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Defining the acquisition cycle for a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

If you are using tags, you define the acquisition cycle for Runtime Professional at the object on which the tag is to be used.

If you are logging a tag, define the acquisition cycle at the connected logging tag. The connected tag is updated with this acquisition cycle.

If you use a tag on a graphic object, the tag is updated with the acquisition cycle of the graphic object. The graphic objects in a screen are usually updated with the update cycle of the screen. You configure the update cycles of the screen and the objects in it in the "Dynamization overview" editor. All the objects used in a screen that require a trigger are shown in the "Dynamization overview" editor. Select the required acquisition cycle for each object. For a high-performance configuration, you should only configure an acquisition cycle for individual objects that deviates from the screen cycle if there truly is a need for it.

###### Requirement

- You have configured a screen.
- The screen contains an object on which a tag is configured.

###### Procedure

To define the acquisition cycle, follow these steps:

1. Select the screen from the project tree and select "Dynamization overview" from the shortcut menu.  
   The "Dynamization overview" editor opens.

   ![Procedure](images/21729389323_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/21729389323_DV_resource.Stream@PNG-en-US.png)
2. Configure the update cycle for the screen in the upper area of the "Dynamization overview" dialog. Select the desired update cycle for the screen in the "Cycle" field or define your own cycle using the object list. The set cycle time has an effect on all objects whose cycle is set to the value "Screen cycle".
3. If you want to configure a different cycle time for an individual object, select the desired object in the table of the editor and select the acquisition cycle in the "Cycle" field or define your own cycle using the object list.

If you want to change the acquisition cycle for an individual object only, select this object in the screen and select "Dynamization overview" from the shortcut menu.

###### Result

The configured object is updated in Runtime with the selected cycle.

---

**See also**

[Defining a substitute value (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-a-substitute-value-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Indirect addressing of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

With indirect addressing, the tag used is first determined at runtime. Use a string tag for indirect addressing in WinCC Runtime Professional. You also need a series of tags whose values are to be displayed in Runtime. In Runtime you enter the name of the tag in the string tag whose value you want to display and process.

###### Application example

The operator enters the name of one or several machines in the input field. Depending on the operator input, a process value of the machine is displayed in an output field.

To configure such a scenario, configure the string tag with activation of indirect addressing for an I/O field. Use this I/O field to output the values. Configure the same tag to another I/O field without activation of indirect addressing. Use this I/O field to enter the machine names. Also configure a series of tags whose values you want to output.

When the operator enters the name of a different machine, the value of the string tag for indirect addressing changes. The output field shows the content of the tag whose name is included in the string tag.

You can use other mechanisms in WinCC to supply the string tag for indirect addressing, for example, a script.

---

**See also**

[Addressing tags indirectly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#addressing-tags-indirectly-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Defining a substitute value (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-a-substitute-value-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Addressing tags indirectly (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

With indirect addressing, the tag used is first determined during runtime. Instead of individual tags, you define a series of tags. In Runtime, the tag name is used to access individual tags.

> **Note**
>
> **The dynamic interconnection of tags on the screen window**
>
> To interconnect tags dynamically on the screen window during runtime, use the tag prefix on the screen window or indirectly addressed tags. Avoid using both methods at the same time.

###### Requirements

- The "Temperature_Motor" tag that you want to use for indirect addressing does exist.
- A series of tags is created, for example, the "Motor1", "Motor2" and "Motor3" tags.
- The Inspector window with the tag properties is open.
- You have created a screen and the "Screens" editor is open.

###### Procedure

To address tags indirectly, proceed as follows:

1. Add an I/O field to the screen and select the following settings for this example in the information window under "Properties > Properties > General":

   - Mode: Output
   - Display format: Decimal
2. Open the object list in the "Tag" field using the selection button, select the "Temperature_Motor" tag and activate the "Use indirect addressing" option.

   ![Procedure](images/22973061259_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/22973061259_DV_resource.Stream@PNG-en-US.png)
3. The "Temperature_Motor" tag is configured for indirect addressing. The additional text ("indirect") is displayed in front of the tag name in the "Tag" field.

   ![Procedure](images/23025312523_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/23025312523_DV_resource.Stream@PNG-en-US.png)
4. Add another I/O field to the screen and select the following settings for this example in the information window under "Properties > Properties > General":

   - Mode: Entry
   - Display format: Character string
5. Open the object list in the "Tag" field using the selection button, select the "Temperature_Motor" tag. Do not activate the option "Use indirect addressing".
6. Save the project.

###### Result

If you enter the name of one of the tags "Motor1", "Motor2" or "Motor3" in the input field in Runtime, the value of the respective tag is displayed in the output field.

---

**See also**

[Indirect addressing of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#indirect-addressing-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Defining a substitute value (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-a-substitute-value-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Monitor connection status (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring tags for the connection status in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-tags-for-the-connection-status-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

###### Configuring tags for the connection status in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

The connection to the configured PLCs is established during the activation of Runtime.

To selectively deactivate or activate individual connections in Runtime, use a system tag of the "ConnectionStates" tag group.

**Diagnostics: Performance of a connection**

Use the WinCC performance tags to evaluate the time behavior of a connection.

###### Tag group "ConnectionStates"

To specify or determine the status of a connection, create the following system tags for each connection:

- @<Connectionname>@ForceConnectionStateEx

  Use the tag to establish or terminate the connection in Runtime.
- @<Connectionname>@ConnectionStateEx

  Use the tag to determine the status of the connection in runtime.

The tags have the tag type "Unsigned 32-bit value" (DWORD).

If you change the name of the connection, the two system tags are also renamed.

###### Tag values

| Tag | Use | Value | Explanation |
| --- | --- | --- | --- |
| @<...>@ForceConnectionStateEx | Determine the connection state | 1 | Establishment of connection  Start value = 1:  When Runtime is activated, the connection is established. |
| 0 | Termination of connection  Start value = 0:  When Runtime is activated, the connection remains deactivated.  The tags of the connection are not archived. |  |  |
| @<...>@ConnectionStateEx | Determine the current connection status | 1 | The connection is ready to use. |
| 0 | The connection is interrupted or terminated. |  |  |

###### Procedure

1. Create the tag table "ConnectionStates" under "HMI tags"
2. Create the tags:

   - @<...>@ForceConnectionStateEx
   - @<...>@ConnectionStateEx
3. Select the connection that is to be activated, deactivated or whose status is to be queried.

###### Using tags

**Querying the connection status**

To determine the status of the connection, read the value of the tag "@<...>@ConnectionStateEx".

If you only want to query whether a certain connection is established or terminated, use the system tag "@<Connection name>@ConnectionStateEx".

**Terminating a connection**

To deactivate a connection, set the value "0" in the "@<...>@ForceConnectionStateEx" tag.

The archiving of the associated process tags is stopped.

**Establishing a connection**

To reactivate an interrupted connection, set the value "1" in the "@<...>@ForceConnectionStateEx" tag.

The process tags of the connection are archived again.

## Working with Arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-arrays-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating array tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-array-tags-basic-panels-panels-comfort-panels-rt-advanced)
- [Examples of arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-of-arrays-basic-panels-panels-comfort-panels-rt-advanced)

### Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Definition

An array is a data list with data elements of a uniform data type. This data list is referred to as array tag or array for short. The data elements are referred to as array elements.

The individual array elements can be addressed by one or multiple integer indices. The properties of each array element are mainly identical and can be configured centrally at the array tag.

![Definition](images/171638290059_DV_resource.Stream@PNG-en-US.png)

#### Advantages

Many similar array elements can be combined in a structured manner with only one array tag. You can specify the shared properties of similar array elements centrally at the array tag. You can then generally use each individual array element as individual tag with the same data type in the configuration.

#### Restrictions

When using arrays on HMI devices, RT Advanced and RT Professional, the following restrictions apply:

- An array can only contain one dimension. Multi-dimensional arrays of the PLCs are mapped to individual tags on the HMI systems.
- Only elementary data types without additional substructure can be used as data type of an array. This means that only scalable arrays are supported.
- The lower index of an array must begin with "0". The indices are moved accordingly for other low limits on the PLCs.
- Unlike individual tags, scalable arrays do not support ranges, linear scaling or tag multiplexing.

#### Application examples

Array tags can be used in the following situations:

- To group process values in profile trends: You map process values to trends which are acquired at different points in time, for example.
- To access specific values which are grouped in trends: For example, display all recorded values of the profile trend by gradually increasing the index tag.
- To configure discrete alarms with successive bit number.
- To save the complete machine data records in a recipe.

#### Tag count with arrays

- Scalable arrays on HMI devices and RT Advanced are counted as one tag.
- In RT Professional, each array element contained is counted separately.
- Multi-dimensional arrays of the PLCs are mapped to individual tags of the same data type and are counted as such.
- Structured arrays of the PLC are mapped to individual tags with the corresponding data type and are counted as such.

#### Special features

On HMI devices as well as in RT Advanced, all array elements are always read or written at once by the PLC when an element of a scalable array is accessed (except arrays of String/WString).

In RT Professional, the array elements are always read and written individually to and from the PLC.

Example for HMI devices and RT Advanced:

- An array tag which consists of 100 array elements of data type "Real" was configured.
- If an array element with a length of 4 bytes changes, 100 x 4 bytes are written to the PLC.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Increased system load and performance losses**  Due to the simultaneous transmission of all array elements of a scalable array, writing to the PLC, in particular, takes longer when accessing an element of a larger array than writing a tag with the same data type. Take this into consideration when designing the communication.  Also note that, with scalable arrays, reading entire array tags by the PLC is usually faster than the sum of read accesses to the same number of elementary tags of the same data type. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Data inconsistency at array tags**  If the value of a single element must be changed in a scalable array tag, the entire array is read, changed and rewritten as a complete array. Changes to other array elements carried out in the meantime in the PLC are overwritten during rewriting.  You should always prevent the HMI device and the PLC from concurrently writing values to the same array tag. Use synchronous transfer of recipe data records, for example, to synchronize an array tag with the PLC. |  |

> **Note**
>
> **Array tags as list entry of multiplex tags**
>
> You can use the array tags of the Char or WChar data type just like the tags of the String data type.
>
> The use of an array tag of the Char or WChar data type as list entry of a multiplex tag in the "HMI tags" editor is not supported.

#### Use in scripts

To maintain performance, always use internal arrays in scripts to change scalable arrays.

1. Copy the PLC array to the internal array at the start of the script.
2. No load is placed on communication to the PLC while the script processes the internal array.

   | Symbol | Meaning |
   | --- | --- |
   |  | **Caution** |
   | **Data inconsistency at array tags**  If the value of a single element must be changed in an array tag, the whole array is read, changed and rewritten as a complete array. Changes to other array elements carried out in the meantime in the PLC are overwritten during rewriting.  You should always prevent the HMI device and the PLC from concurrently writing values to the same array tag. Use synchronous transfer of recipe data records, for example, to synchronize an array tag with the PLC. |  |

---

**See also**

[Creating array tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-array-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Examples of arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-of-arrays-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[WinCC Runtime Advanced (RT Advanced)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#wincc-runtime-advanced-rt-advanced)
  
[Basic Panel (Basic Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-panel-basic-panels)
  
[Mobile Panel (Panels, Comfort Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#mobile-panel-panels-comfort-panels)
  
[Comfort Panel (Panels, Comfort Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#comfort-panel-panels-comfort-panels)
  
[Basic Panel 2nd Generation (Basic Panels)](Performance%20features%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-panel-2nd-generation-basic-panels)
  
[Creating array tags for OPC UA connection (RT Professional)](OPC%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-array-tags-for-opc-ua-connection-rt-professional)

### Creating array tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

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
> HMI array tags of the following data types are only supported with PLC array tags:
>
> - Char
> - WChar
> - String
> - WString

#### Creating HMI array tags

To create an array tag, follow these steps:

1. Open the HMI tag table.
2. Double click <Add> in the "Name" column of the HMI tag table.  
   A new HMI tag is created.

> **Note**
>
> You can delete individual elements of the array tags via the shortcut menu.

#### Configuring HMI array tags

1. Click in the Data type column of the HMI tag table ![Configuring HMI array tags](images/70806108299_DV_resource.Stream@PNG-de-DE.png) and select the "Array" data type.
2. Click ![Configuring HMI array tags](images/70487246859_DV_resource.Stream@PNG-de-DE.png) in the data type column.

   The dialog box for configuring the array is opened.

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)
3. Select the desired data type for the array tag in the "Data type" field.

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)
4. Define the number of array elements in the "Array limits" field. The lower limit must begin with "0".
5. Click ![Configuring HMI array tags](images/84603740299_DV_resource.Stream@PNG-de-DE.png). The settings for the array are saved.
6. As with tags with elementary data types, you still need to assign the address of the array tag in the PLC.
7. Save the project.

#### Result

An array tag is created. The properties of the array elements are inherited from the parent array tag.

---

**See also**

[Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-arrays-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating array tags for OPC UA connection (RT Professional)](OPC%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-array-tags-for-opc-ua-connection-rt-professional)

### Examples of arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Array tags combine a large number of tags, e.g. 100 array elements.

The common properties of array elements of the same kind can be defined centrally in the array tag. In the configuration, you then use each individual array element as an individual tag with the same data type. However, array elements cannot be used as parameters in function lists.

You use array tags as complete arrays in the following places:

- In the "Alarms" editor
- In the "Recipes" editor
- For address multiplexing
- In function lists

#### Examples

You can drag a PLC array tag straight from the PLC tag table to the HMI tag table.

Alternatively, you can configure an array tag separately with the corresponding number of array elements to handle multiple tags of the same data type.

- The individual array elements can be accessed indirectly by means of an index tag, for example.
- Use these index tags to operate and monitor the array elements.

---

**See also**

[Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-arrays-basic-panels-panels-comfort-panels-rt-advanced)

## Working with Arrays (RT Professional)

This section contains information on the following topics:

- [Basics on arrays (RT Professional)](#basics-on-arrays-rt-professional)
- [Creating array tags (RT Professional)](#creating-array-tags-rt-professional)

### Basics on arrays (RT Professional)

#### Definition

Individual array elements can be addressed via one or more integer indices. The properties of each array element are mainly identical and can be configured centrally at the array tag.

An array is a data list with data elements of a uniform data type. This data list is referred to as array tag or array for short. The data elements are referred to as array elements.

![Definition](images/59998774667_DV_resource.Stream@PNG-en-US.png)

#### Advantages

You can group many array elements of the same type into structures using just one array tag. You can specify the common properties of the array elements of the same type centrally at the array tag. In the configuration, you then use each individual array element as individual tags with the same data type.

#### Restrictions

The following restrictions apply to the use of arrays:

- An array can contain only one dimension. Multi-dimensional arrays of controllers are mapped to individual tags on the HMI systems.
- The lower index of an array must begin with "0". The indices are shifted accordingly for other low limits on the controllers.
- Only elementary data types that are not substructured can be used as data type. Thus, only scalable arrays are supported.
- However, Int- and Bool-type array elements cannot be used as parameters in function lists.
- Unlike individual tags, scalable arrays do not support areas, linear scaling or tag multiplexing.
- External array tags are only possible with the S7-1200 and S7-1500 PLCs.

  > **Note**
  >
  > **Synchronization**
  >
  > To avoid structural conflicts in runtime, synchronize the tag names and replace the delimiters "[" and "]" for external array tags.
  >
  > Configure "Settings for tags" for this in the runtime settings.

#### Tag counting with arrays

- Scalable arrays on HMI devices and RT Advanced are counted as one tag.
- In RT Professional, each contained array element is counted separately.
- Multi-dimensional arrays of controllers are mapped to individual tags of the same data type and counted like these.
- Structured arrays of the PLC are mapped to individual tags with the corresponding data type and counted like these.

#### Special features

On HMI devices and in RT Advanced, all array elements are read from or written to the PLC at the same time during access to an element of a scalable array (except arrays of String/WString).

In RT Professional, the array elements are always read and written individually to and from the PLC.

Multidimensional arrays are also possible in conjunction with PLC data types (UDT) of the S7-1200 and S7-1500 PLCs.

> **Note**
>
> **Array tags as list entry of multiplex tags**
>
> You can use the array tags of the Char or WChar data type just like the tags of the String data type.
>
> The use of an array tag of the Char or WChar data type as list entry of a multiplex tag in the "HMI tags" editor is not supported, however.

#### Example for writing an array element in the PLC

- An array tag which consists of 100 array elements of data type "Real" was configured.
- If an array element with a length of 4 bytes changes, 4 bytes are written to the PLC.

---

**See also**

[Settings for synchronization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#settings-for-synchronization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Creating array tags (RT Professional)

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
> HMI array tags of the following data types are only supported with PLC array tags:
>
> - Char
> - WChar
> - String
> - WString

#### Creating HMI array tags

To create an array tag, follow these steps:

1. Open the HMI tag table.
2. Double click <Add> in the "Name" column of the HMI tag table.  
   A new HMI tag is created.

> **Note**
>
> You can delete individual elements of the array tags via the shortcut menu.

#### Configuring HMI array tags

1. Click in the Data type column of the HMI tag table ![Configuring HMI array tags](images/70806108299_DV_resource.Stream@PNG-de-DE.png) and select the "Array" data type.
2. Click ![Configuring HMI array tags](images/70487246859_DV_resource.Stream@PNG-de-DE.png) in the data type column.

   The dialog box for configuring the array is opened.

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80118494219_DV_resource.Stream@PNG-en-US.png)
3. Select the desired data type for the array tag in the "Data type" field.

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)

   ![Configuring HMI array tags](images/80120248715_DV_resource.Stream@PNG-en-US.png)
4. Define the number of array elements in the "Array limits" field. The lower limit must begin with "0".
5. Click ![Configuring HMI array tags](images/84603740299_DV_resource.Stream@PNG-de-DE.png). The settings for the array are saved.
6. As with tags with elementary data types, you still need to assign the address of the array tag in the PLC.
7. Save the project.

#### Result

An array tag is created. The properties of the array elements are inherited from the parent array tag.

## Working with user data types (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a user data type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-user-data-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating user data type elements (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-user-data-type-elements-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing versions of user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-versions-of-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating tags with a user data type data type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-tags-with-a-user-data-type-data-type-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

With user data types you bundle a number of different tags that form one logical unit. You create a user data type as a type and use instances of this type in the project. User data types are project-associated data and are available for all HMI devices of the project.

User data types differ in their association to a family of devices. User data types are available for the following families of devices:

- WinCC Runtime Advanced and Panels
- WinCC Runtime Professional

WinCC also supports the connection of PLC data types (UDTs) and user data types to HMITags.

User data types also differ in their applicability with a specific communication driver. User data types are available for the following communication drivers:

- SIMATIC S7-300/400
- SIMATIC S7-1200
- SIMATIC S7-1500

Create user data types and user data type elements in the project library.

#### Principle

For example, the different conditions of a motor can be described using 6 unique Boolean tags.

![Principle](images/74978625803_DV_resource.Stream@PNG-en-US.png)

If the overall condition should be described with a single tag, this tag can be created based on a user data type. For each of the individual Boolean tags you create a user data type element in the user data type.

This user data type can then be assigned complete to a faceplate for the motor. The created and released version of user data type is displayed at the tag in the "Data type" selection field.

The configured properties of a user data type are used in the instances of the user data type. If required, you change individual properties directly at the point of use, e.g. at a tag. Changing a property at the tag does not affect the user data type created.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Availability of user data types**  The connection of user data types to faceplates is only supported in WinCC Runtime Advanced and Panels. |  |

#### License regulation in Runtime

If you use external tags of the "User data type" data type in a faceplate instance, each user data type element is counted as a tag in Runtime.

#### Example

You have created two screens in the "Screens" editor: Screen_1 and Screen_2.

3 instances of a faceplate type are inserted in Screen_1. 4 instances of a faceplate type are inserted in Screen_2.

Each faceplate instance is connected to an external tag of the "User data type" data type. The user data type includes 10 user data type elements.

Screen 1: 3 faceplate instances * 10 user data type elements corresponds to 30 external tags = 30 PowerTags.

Screen 2: 4 faceplate instances * 10 user data type elements corresponds to 40 external tags = 40 PowerTags.

In Runtime, 70 PowerTags are counted together for both screens. This also applies to the user data type elements that are not required.

---

**See also**

[Creating tags with a user data type data type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-tags-with-a-user-data-type-data-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating user data type elements (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-user-data-type-elements-panels-comfort-panels-rt-advanced-rt-professional)

### Creating a user data type (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You create a user data type in the project library.

#### Requirement

- A project is open.
- The "Libraries" task card is displayed or the library view is open.

#### Procedure

To create a user data type, follow these steps:

1. Click the "Libraries" task card.
2. Double-click the "Project library" item. The folder structure of the project library opens.
3. Click "Add new type".

   A dialog opens.

   ![Procedure](images/75087157387_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/75087157387_DV_resource.Stream@PNG-en-US.png)
4. Click the "HMI UDT" button in the dialog.
5. In the "Specify device for the new type" area select the HMI device on which the user data type is used.
6. Enter a descriptive name in the "Name" field.
7. Click "OK" to apply your settings. The user data type is created. The library view opens.

#### Result

A user data type with the configured properties is created. Version 0.0.1 of the user data type is created and receives the status "In work".

Create the required user data type elements in the next step.

Before you use the version of user data types, for example at a tag, the version must be released.

### Creating user data type elements (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You define user data type elements in the library view. You add or delete elements in the "HMI user data types" table in the work area.

#### Requirement

- The library view is open.
- A user data type is created and opened in the editor.

#### Procedure

1. Select a communication driver for the user data type.

- If you select the <Internal communication> entry, you can only assign the user data type to the internal tags as the data type.
- If a connection to a PLC is selected as the communication driver, the user data type can only be assigned to tags with a connection to this PLC as the data type.
- The communication type set applies to all user data type elements of a user data type. In a user data type for the"WinCC Runtime Professional" family of devices, you can define for each user data type element whether the configured driver is used for control or internal communication.

1. Double-click "Add" in the "Name" column of the table. A new user data type element is added to the user data type.
2. Assign a name.
3. Select the required data type in the "Data Type" field.
4. Create as many user data type elements as you need.
5. You configure the user data type elements in the "Properties" group in the Inspector window.

Alternatively, you can configure the properties of the user data type elements directly in the table. To view hidden columns, activate the column titles using the shortcut menu.

#### Result

You have added elements to version 0.0.1 of the user data type. The version 0.0.1 has the status "in progress".

To use the version in the project, release the version in the next step.

---

**See also**

[Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)

### Managing versions of user data types (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

All user data types have at least one version. When a user data type is created, a version is created at the same time and this version has the status "In work". You can edit the user data type in this status as required. When the editing is complete, you release the version of the user data type.

#### Requirement

- You have created a user data type.
- The user data type has the version 0.0.1. and the status "In work".
- The "Libraries" task card or the library view is open.

#### Releasing a version

1. Select the version 0.0.1 of the user data type in the project library.
2. Select "Release version" in the shortcut menu.

   A dialog opens.
3. If necessary, change the properties of the version:

   - Enter a name for the type in the "Name" field.
   - In the "Version" field, define a main and an intermediate version number for the   
     version to be released.
   - To clean up version management of the type, enable "Delete unused type versions from the library".

You have released version 0.0.1 of the user data type.

#### Editing a version

1. Select, for example, the released version 0.0.1 of a user data type in the project library.
2. Select "Edit type" in the shortcut menu.

The library view opens. The new version 0.0.2 of the user data type is created.

The version has the status "in work".

#### Restoring the last version of a user data type

The last released version of the user data type is version 0.0.2.

You edit the user data type. A new version of the user data type, 0.0.3, is generated and receives the status "In work".

1. Select the version of the user data type in the project library.
2. Select "Discard changes and delete version" in the shortcut menu.

Alternatively

1. If you have opened a version for editing, click "Discard changes and delete version" in the toolbar.  
   The version is deleted.

All changes to the user data type since the last release operation are discarded. The user data type is released again and has version 0.0.2.

#### Deleting user data type

If you delete a user data type, all instances and master copies of this user data type are deleted as well. The same is true for HMI tags that use an HMI user data type.

To delete a user data type, follow these steps:

1. In the project library, under "Types", select the user data type you want to delete.
2. Select "Delete" from the shortcut menu.

### Creating tags with a user data type data type (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

When a tag is created, you assign the version of user data type as a data type. In the "Tag" editor you can create internal tags or tags with a link to a PLC. A tag has access to all user data type versions that use the same communication driver as the tag itself.   
In connection with a PLC, a user data type can only be used if the absolute addressing is selected.

#### Requirement

- A user data type with a user data type element is created.
- The user data type is enabled.
- The tag table is open.
- The Inspector window with the tag properties is open.

#### Procedure

To create a tag of the "User data type" data type, follow these steps:

1. In the "Name" column, double-click "Add" in the tag table. A new tag is created.
2. In the Inspector window select "Properties > Properties > General".
3. Enter a unique tag name in the "Name" field.
4. Select the connection to the required PLC in the "Connection" box.
5. Select the desired version of the user data type in the "Data type" field.

   The selected connection determines which user data types will be displayed.

   For internal tags, only user data type versions of the <Internal user data type> type are available.

   ![Procedure](images/90778524811_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/90778524811_DV_resource.Stream@PNG-en-US.png)

   For tags with a connection to a PLC, only those user data types that have a link to a PLC can be accessed.

   ![Procedure](images/90794347019_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/90794347019_DV_resource.Stream@PNG-en-US.png)
6. Enter the address of the PLC that you want to access with the external tags in the "Address" field of the "Settings" area. The specified address must always point to the start data bit, for example, <DB1.DBX0.0>.

#### Result

You have created a tag of the "User data type" data type. In additional steps you can configure the tag, for example, by setting the start value and limits.

With tags of the "User data type" data type, you can connect the dynamic properties of a faceplate instance, which then supplies these properties with values in Runtime.

If you wish to change the properties of a user data type tag, you must change the properties of the user data type element.

Properties such as "Start value", "Use substitute value" or " Linear scaling" can be changed in the employed instances of the user data type.

---

**See also**

[Basics on user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)

## Working with cycles (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Cycle basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#cycle-basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining cycles (Panels, Comfort Panels, RT Advanced)](#defining-cycles-panels-comfort-panels-rt-advanced)

### Cycle basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Cycles are used to control actions that regularly occur in runtime. Common applications are the acquisition cycle, the logging cycle and the update cycle. You can also define your own cycles in addition to those already provided in WinCC.

#### Principle

In Runtime, actions that are performed regularly are controlled by cycles. Typical applications for cycles:

- Acquisition of external tags  
  The acquisition cycle determines when the HMI device will read the process value of an external tag from the PLC. Set the acquisition cycle to suit the rate of change of the process values. The temperature of an oven, for example, changes much more slowly than the speed of an electrical drive.  
  Do not set the acquisition cycle too low, since this will unnecessarily increase the communication load of the process.
- Logging process values  
  The logging cycle determines when a process value is saved in the logging database. The logging cycle is always an integer multiple of the acquisition cycle.

The smallest possible value for the cycle depends on the HMI device that will be used in your project. For most HMIs, this value is 100 ms. The values of all other cycles are always an integer multiple of the smallest value.

If the cycles provided in WinCC do not meet the needs of your project, you can define your own cycles using the "Cycles" editor. User-defined cycles must always be an integer multiple of the smallest value.

> **Note**
>
> **Device dependency**
>
> You cannot configure self-defined cycle times for Basic Panels.

#### Application example

You can use cycles for the following tasks:

- To regularly log a process.
- To draw attention to maintenance intervals.

#### Updating external tags in Runtime

If you select the "Cyclic in operation" acquisition mode to update the external tags in Runtime for Comfort Panels and the external tag is not being used in the current screen, the tag will not always contain the current value. In the following cases, it is therefore necessary to select the "Cyclic continuous" acquisition type:

- In a tooltip that displays limits when editing the recipe element. This means that the tags of these limits must be set to "Cyclic continuous" if the limits of recipe elements (recipe tags) are dynamically assigned ("Upper 2" and "Lower 2" with tags).
- The trigger tags of HMI alarms (discrete alarms and analog alarms) are automatically changed to "Cyclic continuous". Resetting this is not allowed.
- When using chained text lists for dynamic parameters of HMI alarms (discrete alarms and analog alarms), the tags of the second and all other subordinate levels must be changed to "Cyclic continuous".
- For "bit-triggered" trends, the control tags Trend request, Trend transfer 1, and Trend transfer 2 must be set to "Cyclic continuous".
- In VB scripts, if the tag name is formed dynamically by linking strings.

---

**See also**

[Defining cycles (Panels, Comfort Panels, RT Advanced)](#defining-cycles-panels-comfort-panels-rt-advanced)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Defining cycles (Panels, Comfort Panels, RT Advanced)

#### Introduction

Use cycles to control actions that are run at regular intervals in Runtime. You can also define your own cycles in addition to those already provided in WinCC.

#### Requirement

You have opened the project.

#### Procedure

1. Double-click the "Cycles" entry in the project navigation.  
   The "Cycles" editor opens.
2. In the "Name" column of the "Cycles" editor, double-click "Add".  
   A new cycle time is created.
3. Enter a unique name in the "Name" field.
4. Select the desired cycle unit.
5. Select the desired value for the cycle time.

   The available selection of values varies depending on the cycle unit selected. The smallest possible value for the cycle depends on the HMI device that will be used in your project. For most HMIs, this value is 100 ms. The available values are always an integer multiple of this value.
6. As an option, you can enter a comment regarding the use of the cycle.

#### Result

The cycle you configured is created and beside the default cycles in WinCC for use during configuration.

---

**See also**

[Cycle basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#cycle-basics-basic-panels-panels-comfort-panels-rt-advanced)

## Working with cycles (RT Professional)

This section contains information on the following topics:

- [Cycle basics (RT Professional)](#cycle-basics-rt-professional)
- [Defining cycles (RT Professional)](#defining-cycles-rt-professional)
- [Define starting point (RT Professional)](#define-starting-point-rt-professional)

### Cycle basics (RT Professional)

#### Introduction

Cycles are used to control actions that regularly occur in Runtime. Common applications are the acquisition cycle, the logging cycle and the screen cycle. You can also define your own cycles in addition to those already provided in WinCC.

#### Principle

In Runtime, actions that are performed regularly are controlled by cycles. Typical applications for cycles:

- Refreshing screens  
  The screen cycle determines how often a screen will be refreshed. The screen cycle gives you the option to trigger all dynamizations in a screen at the same time. Use the predefined cycles in WinCC or self-defined cycles as cycle times. The standard setting for the screen cycle is 2 seconds.
- Updating objects  
  With the default setting, all dynamic properties in a screen use the screen cycle. You can use other cycles to update individual objects, if necessary. See [Basics on dynamizing screens](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional) for additional information.
- Triggering scheduled tasks  
  In scheduled tasks you have the option to configure a task with a cyclical trigger. Use the cycle time to determine when the scheduled task is executed. See [Triggers](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#triggers-panels-comfort-panels-rt-advanced-rt-professional) for additional information
- Logging process values  
  The logging cycle determines when a process value is saved in the logging database. The logging cycle is always an integer multiple of the acquisition cycle. See [Cycles and Events](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#cycles-and-events-rt-professional) for additional information.

The smallest values ​​for a cycle in Runtime Professional are 100 and 125 ms. The next possible values ​​are 250 and 300 ms. You can configure all other values with an increment of 100 ms.

> **Note**
>
> **Cycle value 500 ms**
>
> The cycle value of 500 ms is available only for logging of process values.

> **Note**
>
> **Cycle value 125 ms**
>
> The cycle value of 125 ms is only supported in Runtime scripting by the "ActivateDynamic" method. You define all other cycles in the "Cycles" editor.

> **Note**
>
> **Defining your own cycles**
>
> If the cycles predefined in WinCC do not meet the requirements of your project, you can define your own cycles using the "Cycles" editor.
>
> You can create an unlimited number of cycles and use these for configuring the logging. Keep in mind that you can only monitor up to 15 different update cycles in Runtime.

> **Note**
>
> **Using cycles in screens**
>
> Use the 15 system-defined cycles to dynamize the object and screen properties and as screen cycle.

#### Starting point

You can define a starting point for every cycle in WinCC. This starting point will also apply to the cycles provided with the system. The following starting points are possible:

- Trigger cycle at start of Runtime
- Trigger cycle at system shutdown
- Trigger cycle at user-defined starting point

You can use cycle starting points for the following tasks:

- To synchronize different tasks within the system
- To relieve the load on the communication channels by postponing tasks with a high communication load.

#### Application example

You can use cycles for the following tasks:

- To regularly log a process.
- To draw attention to maintenance intervals.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Define starting point (RT Professional)](#define-starting-point-rt-professional)
  
[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Cycles and Events (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#cycles-and-events-rt-professional)

### Defining cycles (RT Professional)

#### Introduction

Use cycles to control actions that are run at regular intervals in Runtime. You can also define your own cycles in addition to those already provided in WinCC.

#### Requirement

The project is open.

#### Procedure

1. Double-click the "Cycles" entry in the project navigation.  
   The "Cycles" editor opens.
2. In the "Name" column of the "Cycles" editor, double-click "Add".  
   A new cycle time is created.
3. Enter a unique name in the "Name" field.
4. Select the desired cycle unit.
5. Select the desired value for the cycle time.

   The available selection of values varies depending on the cycle unit selected.
6. As an option, you can enter a comment regarding the use of the cycle.

#### Result

The cycle you configured is created and beside the default cycles in WinCC for use during configuration.

---

**See also**

[Cycle basics (RT Professional)](#cycle-basics-rt-professional)

### Define starting point (RT Professional)

#### Introduction

For cycles, define the starting points to start different cycles at different times. Staggering the start of the update processes will also stagger the communication load on the connection to the PLC.

#### Requirement

- The "Cycles" editor is open.
- The Inspector window with the cycle properties is open.

#### Procedure

To define the starting point for a cycle, follow these steps:

1. Select the cycle from the table in the "Cycles" editor.
2. Click "Properties > Properties > Starting point" in the Inspector window.  
   The properties for the starting point of the cycle are displayed.
3. Select the settings for the starting point.
4. Save the project.

#### Result

The selected cycle is started in Runtime at the configured starting point.

---

**See also**

[Cycle basics (RT Professional)](#cycle-basics-rt-professional)

## Reference (RT Professional)

This section contains information on the following topics:

- [Mapping and coding of data types (RT Professional)](#mapping-and-coding-of-data-types-rt-professional)
- [Coding and value range of data types (RT Professional)](#coding-and-value-range-of-data-types-rt-professional)
- [Data types (RT Professional)](#data-types-rt-professional)

### Mapping and coding of data types (RT Professional)

#### Introduction

WinCC sets the data type of an external tag according to the data type of the connected PLC tag. If the data type of the PLC tag is not available in WinCC, a compatible data type is automatically used at the HMI tag. As required, you can specify that WinCC uses a different data type and adapts the format of the data type of the PLC tag and the data type of the HMI tag. The following sections include the data types that are typically used for mapping. You will also find optional mapping versions that you can set yourself.

#### Coding of data types

In addition to mapping of data types, you can also change the coding of many mapping versions. Coding is used to map and process the binary information of PLC tag according to the requirements. The values of the PLC tags can be mapped with the following coding:

**BCD**

The BCD code is a binary decimal code that maps each individual digit of a number in binary form. The value of the digits is according to the number sequence 8-4-2-1. The result is the following value table:

| Decimal digit | BCD code |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

**Aiken**

The Aiken code is a complementary BCD code. The value of the digits is according to the number sequence 2-4-2-1. The result is the following value table:

| Decimal digit | Aiken code |
| --- | --- |
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 1011 |
| 6 | 1100 |
| 7 | 1101 |
| 8 | 1110 |
| 9 | 1111 |

**Excess**

Excess-3 code is used for Excess coding. The Excess-3 code is a complementary BCD code. The value of the digits is according to the number sequence 8-4-(-2)-(-1). The result is the following value table:

| Decimal digit | Excess code |
| --- | --- |
| 0 | 0011 |
| 1 | 0100 |
| 2 | 0101 |
| 3 | 0110 |
| 4 | 0111 |
| 5 | 1000 |
| 6 | 1001 |
| 7 | 1010 |
| 8 | 1011 |
| 9 | 1100 |

**ExtBCD**

The "ExtBCD" coding used the BCD code described above for coding. But with "ExtBCD" the Most Significant Bit is interpreted as sign.

**MSB**

The "MSB" coding uses the binary code standard for coding. But with "MSB" the Most Significant Bit is interpreted as sign.

**NanoToMilliseconds**

The PLC tags with the data types "LTime"and "LTime_Of_Day" contain a number of nanoseconds. However, since HMI tags do not process nanoseconds, these are converted into milliseconds by the coding "NanoToMilliseconds" in the HMI runtimes:

| Value of the PLC tag with  PLC data type "LTime" or "LTime_Of_Day" | Converted value in the HMI tags with the HMI data type "DInt" or "UDInt" |
| --- | --- |
| 1000000 | 1 |
| 2000000 | 2 |
| 10000000 | 10 |
| 100000000 | 100 |
| ... | ... |

---

**See also**

[Coding and value range of data types (RT Professional)](#coding-and-value-range-of-data-types-rt-professional)
  
[Adapting the data type of a tag (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adapting-the-data-type-of-a-tag-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Coding and value range of data types (RT Professional)

#### Coding and value range

Depending on the selected coding, the value ranges listed in the tables are available for the different data types.

**PLC data type Byte**

| Conversion | Value range |
| --- | --- |
| Byte to UnsignedByte | 0...255 |
| Byte to UnsignedWord | 0...255 |
| Byte to UnsignedDword | 0...255 |
| Byte to SignedByte | 0...127 |
| Byte to SignedWord | 0...255 |
| Byte to SignedDword | 0...255 |
| Byte to BCDByte | 0...99 |
| Byte to BCDWord | 0...255 |
| Byte to BCDDword | 0...255 |
| Byte to AikenByte | 0...99 |
| Byte to AikenWord | 0...255 |
| Byte to AikenDword | 0...255 |
| Byte to ExcessByte | 0...99 |
| Byte to ExcessWord | 0...255 |
| Byte to ExcessDword | 0...255 |

**PLC data type Char**

| Conversion | Value range |
| --- | --- |
| Char to UnsignedByte | 0...127 |
| Char to UnsignedWord | 0...127 |
| Char to UnsignedDword | 0...127 |
| Char to SignedByte | -128...+127 |
| Char to SignedWord | -128...+127 |
| Char to SignedDword | -128...+127 |
| Char to MSBByte | -128...+127 |
| Char to MSBWord | -128...+127 |
| Char to MSBDword | -128...+127 |
| Char to BCDByte | 0...99 |
| Char to BCDWord | 0...127 |
| Char to BCDDword | 0...127 |
| Char to SignedBCDByte | -9...+9 |
| Char to SignedBCDWord | -128...+127 |
| Char to SignedBCDDword | -128...+127 |
| Char to ExtSignedBCDByte | -79...+79 |
| Char to ExtSignedBCDWord | -128...+127 |
| Char to ExtSignedBCDDword | -128...+127 |
| Char to AikenByte | 0...99 |
| Char to AikenWord | 0...127 |
| Char to AikenDword | 0...127 |
| Char to SignedAikenByte | -9...+9 |
| Char to SignedAikenWord | -128...+127 |
| Char to SignedAikenDword | -128...+127 |
| Char to ExcessByte | 0...99 |
| Char to ExcessWord | 0...127 |
| Char to ExcessDword | 0...127 |
| Char to SignedExcessByte | -9...+9 |
| Char to SignedExcessWord | -128...+127 |
| Char to SignedExcessDword | -128...+127 |
| Char to UnsignedByte | 0...127 |
| Char to UnsignedWord | 0...127 |
| Char to UnsignedDword | 0...127 |

**PLC data type Real**

| Conversion | Value range |
| --- | --- |
| Real to Real | +-1.79769313486231e+308 |
| Real to UnsignedByte | 0...255 |
| Real to UnsignedWord | 0...65535 |
| Real to UnsignedDword | 0...4294967295 |
| Real to SignedByte | -128...+127 |
| Real to SignedWord | -32768...+32767 |
| Real to SignedDword | -2147483647...+2147483647 |
| Real to Float | +-3.402823e+38 |
| Real to MSBByte | -127...+127 |
| Real to MSBWord | -32767...+32767 |
| Real to MSBDword | -2147483647...+2147483647 |
| Real to BCDByte | 0...99 |
| Real to BCDWord | 0...9999 |
| Real to BCDDword | 0...99999999 |
| Real to SignedBCDByte | -9...+9 |
| Real to SignedBCDWord | -999...+999 |
| Real to SignedBCDDword | -9999999...+9999999 |
| Real to ExtSignedBCDByte | -79...+79 |
| Real to ExtSignedBCDWord | -7999...+7999 |
| Real to ExtSignedBCDDword | -79999999...+79999999 |
| Real to AikenByte | 0...99 |
| Real to AikenWord | 0...9999 |
| Real to AikenDword | 0...99999999 |
| Real to SignedAikenByte | -9...+9 |
| Real to SignedAikenWord | -999...+999 |
| Real to SignedAikenDword | -9999999...+9999999 |
| Real to ExcessByte | 0...99 |
| Real to ExcessWord | 0...9999 |
| Real to ExcessDword | 0...99999999 |
| Real to SignedExcessByte | -9...+9 |
| Real to SignedExcessWord | -999...+999 |
| Real to SignedExcessDword | -9999999...+9999999 |
| Real to S5Timer | 10...9990000 |
| Real to S5Float | +-1.701411e+38 |

**PLC data type DWord**

| Conversion | Value range |
| --- | --- |
| DWord to UnsignedDword | 0...4294967295 |
| DWord to UnsignedByte | 0...255 |
| DWord to UnsignedWord | 0...65535 |
| DWord to SignedByte | 0...127 |
| DWord to SignedWord | 0...32767 |
| DWord to SignedDword | 0...2147483647 |
| DWord to BCDByte | 0...99 |
| DWord to BCDWord | 0...9999 |
| DWord to BCDDword | 0...99999999 |
| DWord to AikenByte | 0...99 |
| DWord to AikenWord | 0...9999 |
| DWord to AikenDword | 0...99999999 |
| DWord to ExcessByte | 0...99 |
| DWord to ExcessWord | 0...9999 |
| DWord to ExcessDword | 0...99999999 |
| DWord to SimaticTimer | 10...9990000 |
| DWord to SimaticBCDTimer | 10...9990000 |
| DWord to UnsignedDword | 0...4294967295 |
| DWord to UnsignedByte | 0...255 |
| DWord to UnsignedWord | 0...65535 |

**PLC data type Float**

| Conversion | Value range |
| --- | --- |
| Float to Float | +-3.402823e+38 (no conversion) |
| Float to UnsignedByte | 0...255 |
| Float to UnsignedWord | 0...65535 |
| Float to UnsignedDword | 0 to 4.294967e+09 |
| Float to SignedByte | -128...+127 |
| Float to SignedWord | -32768...+32767 |
| Float to SignedDword | -2.147483e+09 to +2.147483e+09 |
| Float to Real | +-3.402823e+38 |
| Float to MSBByte | -127...+127 |
| Float to MSBWord | -32767...+32767 |
| Float to MSBDword | -2.147483e+09 to +2.147483e+09 |
| Float to BCDByte | 0...99 |
| Float to BCDWord | 0...9999 |
| Float to BCDDword | 0...9.999999e+07 |
| Float to SignedBCDByte | -9...+9 |
| Float to SignedBCDWord | -999...+999 |
| Float to SignedBCDDword | -9999999...+9999999 |
| Float to ExtSignedBCDByte | -79...+79 |
| Float to ExtSignedBCDWord | -7999...+7999 |
| Float to ExtSignedBCDDword | -7.999999e+07 to +7.999999e+07 |
| Float to AikenByte | 0...99 |
| Float to AikenWord | 0...9999 |
| Float to AikenDword | 0...9.999999e+07 |
| Float to SignedAikenByte | -9...+9 |
| Float to SignedAikenWord | -999...+999 |
| Float to SignedAikenDword | -9999999...+9999999 |
| Float to ExcessByte | 0...99 |
| Float to ExcessWord | 0...9999 |
| Float to ExcessDword | 0...9.999999e+07 |
| Float to SignedExcessByte | -9...+9 |
| Float to SignedExcessWord | -999...+999 |
| Float to SignedExcessDword | -9999999...+9999999 |
| Float to S5Timer | 10...9990000 |
| Float to S5Float | +-1.701411e+38 |

**PLC data type Long**

| Conversion | Value range |
| --- | --- |
| Long to SignedDword | -2147483647...+2147483647 |
| Long to UnsignedByte | 0...255 |
| Long to UnsignedWord | 0...65535 |
| Long to UnsignedDword | 0...2147483647 |
| Long to SignedByte | -128...+127 |
| Long to SignedWord | -32768...+32767 |
| Long to MSBByte | -127...+127 |
| Long to MSBWord | -32767...+32767 |
| Long to MSBDword | -2147483647...+2147483647 |
| Long to BCDByte | 0...99 |
| Long to BCDWord | 0...9999 |
| Long to BCDDword | 0...99999999 |
| Long to SignedBCDByte | -9...+9 |
| Long to SignedBCDWord | -999...+999 |
| Long to SignedBCDDword | -9999999...+9999999 |
| Long to ExtSignedBCDByte | -79..+79 |
| Long to ExtSignedBCDWord | -7999...+7999 |
| Long to ExtSignedBCDDword | -79999999...+79999999 |
| Long to AikenByte | 0...99 |
| Long to AikenWord | 0...9999 |
| Long to AikenDword | 0...99999999 |
| Long to SignedAikenByte | -9...+9 |
| Long to SignedAikenWord | -999...+999 |
| Long to SignedAikenDword | -9999999...+9999999 |
| Long to ExcessByte | 0...99 |
| Long to ExcessWord | 0...9999 |
| Long to ExcessDword | 0...99999999 |
| Long to SignedExcessByte | -9...+9 |
| Long to SignedExcessWord | -999...+999 |
| Long to SignedExcessDword | -9999999...+9999999 |
| Long to SimaticTimer | 10...9990000 |
| Long to SimaticBCDTimer | 10...9990000 |

**PLC data type Short**

| Conversion | Value range |
| --- | --- |
| Short to UnsignedByte | 0...255 |
| Short to UnsignedWord | 0...32767 |
| Short to UnsignedDword | 0...32767 |
| Short to SignedByte | -128...+127 |
| Short to SignedWord | -32768...+32767 |
| Short to SignedDword | -32768...+32767 |
| Short to MSBByte | -127...+127 |
| Short to MSBWord | -32767...+32767 |
| Short to MSBDword | -32768...+32767 |
| Short to BCDByte | 0...99 |
| Short to BCDWord | 0...9999 |
| Short to BCDDword | 0...32767 |
| Short to SignedBCDByte | -9...+9 |
| Short to SignedBCDWord | -999...+999 |
| Short to SignedBCDDword | -32768...+32767 |
| Short to ExtSignedBCDByte | -79...+79 |
| Short to ExtSignedBCDWord | -7999...+7999 |
| Short to ExtSignedBCDDword | -32768...+32767 |
| Short to AikenByte | 0...99 |
| Short to AikenWord | 0...9999 |
| Short to AikenDword | 0...32767 |
| Short to SignedAikenByte | -9...+9 |
| Short to SignedAikenWord | -999...+999 |
| Short to SignedAikenDword | -32768...+32767 |
| Short to ExcessByte | 0...99 |
| Short to ExcessWord | 0...9999 |
| Short to ExcessDword | 0...32767 |
| Short to SignedExcessByte | -9...+9 |
| Short to SignedExcessWord | -999...+999 |
| Short to SignedExcessDword | -32768...+32767 |
| Short to UnsignedByte | 0...255 |
| Short to UnsignedWord | 0...32767 |
| Short to UnsignedDword | 0...32767 |

**PLC data type Word**

| Conversion | Value range |
| --- | --- |
| Word to UnsignedWord | 0...65535 |
| Word to UnsignedByte | 0...255 |
| Word to UnsignedDword | 0...65535 |
| Word to SignedByte | 0...127 |
| Word to SignedWord | 0...32767 |
| Word to SignedDword | 0...65535 |
| Word to BCDByte | 0...99 |
| Word to BCDWord | 0...9999 |
| Word to BCDDword | 0...65535 |
| Word to AikenByte | 0...99 |
| Word to AikenWord | 0...9999 |
| Word to AikenDword | 0...65535 |
| Word to ExcessByte | 0...99 |
| Word to ExcessWord | 0...9999 |
| Word to ExcessDword | 0...65535 |
| Word to SimaticCounter | 0...999 |
| Word to SimaticBCDCounter | 0...999 |
| Word to UnsignedWord | 0...65535 |
| Word to UnsignedByte | 0...255 |
| Word to UnsignedDword | 0...65535 |

---

**See also**

[Mapping and coding of data types (RT Professional)](#mapping-and-coding-of-data-types-rt-professional)

### Data types (RT Professional)

This section contains information on the following topics:

- [Raw data tags (RT Professional)](#raw-data-tags-rt-professional)
- [Data types for SIMATIC S7-300/400 (RT Professional)](#data-types-for-simatic-s7-300400-rt-professional)
- [Data types for SIMATIC S7-1200 and S7-1500 (RT Professional)](#data-types-for-simatic-s7-1200-and-s7-1500-rt-professional)
- [Data types for OPC DA (RT Professional)](#data-types-for-opc-da-rt-professional)
- [Data types for Allen Bradley Ethernet IP (RT Professional)](#data-types-for-allen-bradley-ethernet-ip-rt-professional)
- [Data types for Modicon Modbus TCP/IP (RT Professional)](#data-types-for-modicon-modbus-tcpip-rt-professional)
- [Data types for Mitsubishi MC (RT Professional)](#data-types-for-mitsubishi-mc-rt-professional)

#### Raw data tags (RT Professional)

##### Definition

In WinCC, you can create external and internal tags of the type "Raw data type". The format and the length of a raw data tag are not fixed. Its length can be in the range from 1 and 65535 bytes. It is either defined by the user or results from a specific application.

The contents of a raw data tag are not fixed. Only senders and receivers can interpret the contents of a raw data tag. They are not interpreted by WinCC.

> **Note**
>
> A raw data tag cannot be displayed in screens.

##### Potential Applications within WinCC

Raw data tags can be used in the following areas in WinCC:

- For data exchange with the PLC alarm blocks for processing and acknowledgment of alarms.
- In scripts for data exchanged with the help of functions "Get/SetTagRaw".
- In tag logs
- To transfer jobs, data, processing acknowledgments between WinCC and the PLC.

  > **Note**
  >
  > When the raw data tag is displayed in an I/O field, you must observe the conventions of the string with a "\0" character at the end.

##### "Properties address"

For external raw data tags, the "Address properties" dialog is not the same for all communication drivers because the parameters of the tag address and the supported raw data tag types depend on the type of communication being used.

##### Format adaptation

There is no format adaptation in WinCC for the "raw data type".

#### Data types for SIMATIC S7-300/400 (RT Professional)

##### Overview

The following table shows the data types for SIMATIC S7-300/400 with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bool | Bool | 0 (FALSE), 1 (TRUE) |
| Byte | USInt | 0 ... 255 |
| Word | UInt | 0 ... 65 535 |
| DWord | UDInt | 0 ... 4294967295 |
| Char | USInt | 0 ... 255 |
| Int | Int | −32768 … 32767 |
| DInt | DInt | −2147483648 … +2147483647 |
| Real | Real | ±1.17549E-38 to ±3.40282E+38 and 0.0 |
| Time | DInt | −2147483648 … +2147483647 |
| Date | DateTime/UInt | 0 … 65535 |
| Time_of_Day, TOD | DateTime/UDInt | 0 … 86399999 |
| S5Time | UDInt | 0 … 9990000 |
| Counter | UInt | 0 ... 999 |
| Timer | UDInt | 0 … 9990000 |
| String | String | - |

#### Data types for SIMATIC S7-1200 and S7-1500 (RT Professional)

This section contains information on the following topics:

- [Data types for SIMATIC S7-1200 - V2 (RT Professional)](#data-types-for-simatic-s7-1200---v2-rt-professional)
- [Data types for SIMATIC S7-1500 (RT Professional)](#data-types-for-simatic-s7-1500-rt-professional)
- [User-defined PLC data types (UDT) (RT Professional)](#user-defined-plc-data-types-udt-rt-professional)

##### Data types for SIMATIC S7-1200 - V2 (RT Professional)

###### Overview

The following table shows the data types for SIMATIC S7-1200 - V2 with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bool | Bool | 0 (FALSE), 1 (TRUE) |
| SInt | SInt | -128 ... +127 |
| Int | Int | -32768 ... +32767 |
| DInt | DInt | −2147483648 … +2147483647 |
| USInt | USInt | 0 ... 255 |
| UInt | UInt | 0 … 65535 |
| UDInt | UDInt | 0 ... 4294967295 |
| Real | Real | ±1.17549E-38 to ±-3.40282E+38 and 0.0 |
| LReal | LReal | ±1.79769313486231E+308 to ±2.22507385850720E-308 and 0.0 |
| Time | DInt | −2147483648 … +2147483647 |
| Date | DateTime/UInt | 0 … 65535 |
| DTL | DateTime | - |
| Time_of_Day, TOD | DateTime/UDInt | 0 … 86399999 |
| String | String | - |
| Char | USInt | 0 ... 255 |
| Array of Char | String | - |
| Byte | USInt | 0 ... 255 |
| Word | UInt | 0 … 65535 |
| DWord | UDInt | 0 ... 4294967295 |
| PlcUDT | PlcUDT |  |

##### Data types for SIMATIC S7-1500 (RT Professional)

###### Overview

The following table shows the data types for SIMATIC S7-1500 with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bool | Bool | 0 (FALSE), 1 (TRUE) |
| SInt | SInt | -128 ... +127 |
| Int | Int | -32768 ... +32767 |
| DInt | DInt | −2147483648 … +2147483647 |
| LInt | LReal | -4,503,599,627,370,495 … +4,503,599,627,370,495 |
| USInt | USInt | 0 ... 255 |
| UInt | UInt | 0 … 65535 |
| UDInt | UDInt | 0 ... 4294967295 |
| ULInt | LReal | 0 … 4,503,599,627,370,495 |
| Real | Real | ±1.17549E-38 to ±-3.40282E+38 and 0.0 |
| LReal | LReal | ±1.79769313486231E+308 to ±2.22507385850720E-308 and 0.0 |
| S5Time | UDInt | 0 … 9990000 |
| Time | DInt | −2147483648 … +2147483647 |
| LTime | DInt | −2147483648 … +2147483647 |
| Date | DateTime/UInt | 0 … 65535 |
| Time_of_Day, TOD | DateTime/UDInt | 0 … 86399999 |
| LTime_of_Day, LTOD | DateTime/UDInt | 0 … 86399999 |
| Date_And_Time, DT | DateTime | - |
| LDT | DateTime | - |
| DTL | DateTime | - |
| String | String | - |
| WString | WString | - |
| Char | USInt | 0 ... 255 |
| WChar | WString | - |
| Byte | USInt | 0 ... 255 |
| Word | UInt | 0 … 65535 |
| DWord | UDInt | 0 ... 4294967295 |
| Timer | UDInt | 0 … 9990000 |
| Counter | UInt | 0 ... 999 |
| PLCUDT | PLCUDT |  |

> **Note**
>
> The 64-bit PLC data types LINT, UINT and LWORD are mapped to the HMI data type LREAL in the HMI channel. A loss of accuracy can be expected when the value exceeds the size 2^50.

##### User-defined PLC data types (UDT) (RT Professional)

###### Overview

You can connect with the HMI tags and DB instances of user-defined PLC data types (UDT).

The PLC data type and the corresponding DB instances are created and updated centrally in STEP 7. In WinCC, you can use the following sources as PLC tag (DB instances):

- Data block elements that use a UDT as data type
- Instance data blocks of a UDT

The data type is taken from STEP 7 and is not converted into an HMI data type. The access type is always "Symbolic access".

###### Elements of a PLC data type

You have access to the following elements in WinCC with a structured PLC data type:

- Elements that have been released for WinCC in STEP 7.
- Elements whose data types are supported in WinCC.

> **Note**
>
> **Invalid elements of a PLC data type in WinCC**
>
> Invalid elements generate an error in WinCC.
>
> If you disable the "Accessible from HMI" option for the corresponding elements of the associated PLC data type in STEP 7, these elements are excluded in WinCC.

###### Naming conventions

The following characters are invalid in the name of the PLC data type and generate an error in WinCC:

- Period: "."
- Brackets: "(" and ")"

###### Properties

The properties of the PLC data type and its elements are adopted in WinCC. Depending on the data type used, the properties are read-only or can be written to in WinCC.

If you change the connection of the PLC data type in WinCC, all elements of the PLC data type are deleted and the properties of the newly connected PLC tag are used.

In WinCC, you have access to STEP 7 comments on elements of the PLC data type.

You have limited access to properties in WinCC for the following elements of PLC data types:

- Elements of the data type "Struct"
- PLC data type
- Multidimensional arrays
- Array of complex data types except "DTL"

###### Mapping of the data type "DTL"

If a PLC data type contains elements of the data type "DTL", these elements are mapped in WinCC without lower-level elements. The data type "DTL" turns into "DateTime" in WinCC.

###### Tags with elements of the "DTL" data type

Tags that use the "DTL" data type element by element can only be used as read-only with symbolic addressing, e.g. with SIMATIC S7 1200 and SIMATIC S7 1500. With absolute addressing, write access is also possible.

#### Data types for OPC DA (RT Professional)

##### Overview

The following table shows the data types for OPC DA with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| VT_EMPTY | DInt | 4 |
| VT_BOOL | Bool | 1 |
| VT_I1 | SInt | 1 |
| VT_UI1 | USInt | 1 |
| VT_I2 | Int | 2 |
| VT_UI2 | UInt | 2 |
| VT_I4 | DInt | 4 |
| VT_UI4 | UDInt | 4 |
| VT_R4 | Real | 4 |
| VT_R8 | LReal | 8 |
| VT_BSTR | WString | Number of characters |
| VT_DATE | VT_ARRAY (Array [lo..hi] of VT_DATE) | Raw /  Array [lo..hi] of DateTime | - |
| VT_I1 | VT_ARRAY (Array [lo..hi] of VT_I1) | Raw /  Array [lo..hi] of SInt | - |
| VT_UI1 | VT_ARRAY (Array [lo..hi] of VT_UI1) | Raw /  Array [lo..hi] of USInt | - |
| VT_I2 | VT_ARRAY (Array [lo..hi] of VT_I2) | Raw /  Array [lo..hi] of Int | - |
| VT_UI2 | VT_ARRAY (Array [lo..hi] of VT_UI2) | Raw /  Array [lo..hi] of UInt | - |
| VT_I4 | VT_ARRAY (Array [lo..hi] of VT_I4) | Raw /  Array [lo..hi] of DInt | - |
| VT_UI4 | VT_ARRAY (Array [lo..hi] of VT_UI4) | Raw /  Array [lo..hi] of UDInt | - |
| VT_R4 | VT_ARRAY (Array [lo..hi] of VT_R4) | Raw /  Array [lo..hi] of Real | - |
| VT_R8 | VT_ARRAY (Array [lo..hi] of VT_R8) | Raw /  Array [lo..hi] of LReal | - |

#### Data types for Allen Bradley Ethernet IP (RT Professional)

##### Overview

The following table shows the data types for Allen Bradley Ethernet IP with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bool | Bool | 0 (FALSE), 1 (TRUE) |
| SInt | SInt | -128 … +127 |
| USInt | USInt | 0 … 255 |
| Int | Int | -32768..+32767 |
| UInt | UInt | 0 … 65535 |
| DInt | DInt | −2147483648 … +2147483647 |
| UDInt | UDInt | 0 … 4294967295 |
| Real | Real | ±1.17549E-38 to ±-3.40282E+38 and 0.0 |
| String | String | Cannot be used |

#### Data types for Modicon Modbus TCP/IP (RT Professional)

##### Overview

The following table shows the data types for Modicon Modbus TCP/IP with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bit | Bool | 0 (FALSE), 1 (TRUE) |
| +/- Int | Int | -32768 … +32767 |
| Int | UInt | 0 … 65535 |
| 16 bit group | UInt | 0 … 65535 |
| +/- Double | DInt | −2147483648 … +2147483647 |
| Double | UDInt | 0 … 4294967295 |
| Float | Real | ±1.17549E-38 to ±-3.40282E+38 and 0.0 |
| ASCII | String | Cannot be used |

#### Data types for Mitsubishi MC (RT Professional)

##### Overview

The following table shows the data types for Mitsubishi MC with the corresponding HMI data types and value ranges in WinCC.

| PLC data type | HMI data type | Value range |
| --- | --- | --- |
| Bool | Bool | 0 (FALSE), 1 (TRUE) |
| 4-bit block | USInt | 0 … 255 |
| 8-bit block | USInt | 0 … 255 |
| 12-bit block | UInt | 0 … 65535 |
| 16-bit block | UInt | 0 … 65535 |
| Int | Int | -32768 … +32767 |
| Word | UInt | 0 … 65535 |
| 20-bit block | UDInt | 0 … 4294967295 |
| 24-bit block | UDInt | 0 … 4294967295 |
| 28-bit block | UDInt | 0 … 4294967295 |
| 32-bit block | UDInt | 0 … 4294967295 |
| DInt | DInt | −2147483648 … +2147483647 |
| DWord | UDInt | 0 … 4294967295 |
| Real | Real | ±1.17549E-38 to ±-3.40282E+38 and 0.0 |
| String | String | Cannot be used |

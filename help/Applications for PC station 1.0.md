---
title: "Applications for PC station 1.0"
package: HWCSimNetPCApplenUS
topics: 37
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Applications for PC station 1.0

This section contains information on the following topics:

- [OPC Server user application](#opc-server-user-application)

## OPC Server user application

This section contains information on the following topics:

- [OPC server](#opc-server)

### OPC server

This section contains information on the following topics:

- [General protocol-specific settings](#general-protocol-specific-settings)
- [S7-specific settings](#s7-specific-settings)
- [S7 connections for access to optimized data blocks with S7-1200/S7-1500](#s7-connections-for-access-to-optimized-data-blocks-with-s7-1200s7-1500)
- [Redundant OPC UA server](#redundant-opc-ua-server)
- [PLC alarms for OPC server](#plc-alarms-for-opc-server)
- [Editor for OPC program alarms](#editor-for-opc-program-alarms)
- [Access to historical data (Historical Access)](#access-to-historical-data-historical-access)
- [Editor for OPC UA PubSub communication](#editor-for-opc-ua-pubsub-communication)

#### General protocol-specific settings

This section contains information on the following topics:

- [General](#general)
- [Access protection](#access-protection)

##### General

This section contains information on the following topics:

- [Cycle time](#cycle-time)

###### Cycle time

###### Effects of the selectable cycle time

The cycle time influences how often the OPC server updates the values of the OPC items in its cache using a new communications job and how often it checks for changes. The cycle time therefore influences the performance, the communication load, and the processor load.

If the value for the cycle time is set too low, this increases processor load unnecessarily!

###### Relationship between the cycle time and update interval (UpdateRate)

The update interval (UpdateRate) parameter that you can set in the user program specifies the shortest interval for checking the values of the OPC items of an active OPC group. The server checks whether or not the values of the OPC items have changed at the earliest when this interval has elapsed. This limits the communication load.

The update intervals used by the OPC server for SIMATIC NET are multiples of the cycle time specified here during configuration. The shortest possible update interval is the cycle time.

###### Relationship between the cycle times set for specific protocols

Since the SIMATIC NET OPC Server can use variables of different protocols at the same time,

the minimum update interval of the OPC Server is the highest value set for the cycle time for the active protocols (protocols for which connections are configured).

Example:

A cycle time of 100 ms is configured for S7. No other protocol is being used. 100 ms is used by the OPC server as the minimum update time. The DP protocol is now added and the cycle time configured for this protocol is 50 ms. Result: The OPC server now uses the value 50 ms as the minimum update time for all protocols.

Note: The response described results from the requirements of the OPC standard. The OPC standard specifies that data changes must not be signaled more quickly than specified by the minimum update rate.

###### Actual update interval

The actual update interval (UpdateRate) that can be achieved during operation depends on various factors including:

- The underlying communication protocol
- The communication partner
- Number and type of items

As a result, the actual update interval that can be achieved maybe longer than the minimum value configured here.

If the process value changes several times within the actual update interval, some value changes will not be forwarded to the application.

Note:

The data throughput with asynchronous and synchronous jobs does not depend on the update interval parameter (UpdateRate) and the cycle time set in the configuration.

##### Access protection

This section contains information on the following topics:

- [Enabling access protection](#enabling-access-protection)
- [Syntax - OPC item-specific access rights](#syntax---opc-item-specific-access-rights)
- [Leading zeros in items - example with wildcards:](#leading-zeros-in-items---example-with-wildcards)

###### Enabling access protection

###### Reference

Settings for the OPC server / "Properties > General" parameter group; a protocol-specific node is selected.

###### Meaning of access permissions for OPC variables

With the OPC server, access permissions to individual variables or groups of variables can be specified for a specific protocol. By specifying access permissions, you can, for example, prevent an internal controller calculation variable from being overwritten.

- Standard rights

  For OPC items that are not specifically named, you can specify a default value here:

  - Read-write: Read and write
  - Read: Read
  - Write: Write
  - None: No access
- OPC item-specific access rights

  If you select this option, you can assign access permissions explicitly for certain OPC items in the input box.

---

**See also**

[Syntax - OPC item-specific access rights](#syntax---opc-item-specific-access-rights)

###### Syntax - OPC item-specific access rights

You can enter access rights for one or more OPC items.

The default rights defined for the other OPC items are not affected.

###### The syntax for OPC item-specific access rights is defined as follows:

<OPCItem>=<rights>

where:

- <OPCItem>

  You specify one or more OPC Items according to the syntax defined in the OPC documentation. It is also possible to use aliases.

  The following placeholders can be used:

  * Any number of irrelevant characters

  ? exactly one character is irrelevant
- <rights>

| Symbol | Meaning |
| --- | --- |
| Read-write | Read and write |
| Read | Read |
| Write | Write |
| None | No access |

###### Rules for evaluation

- The specific rights assigned here have priority over the default rights you assigned in the input area Access protection.
- The specific rights assigned here are evaluated in the order shown here. If there is a multiple assignment for an OPC item, the last assignment is always valid.

  Example:

  DP:[CP 5611]Slave040_QB*=RW

  DP:[CP 5611]Slave040_QB1=R

  DP:[CP 5611]Slave040_QB2=W

  DP:[CP 5611]Slave040_QB1=W

  DP:[CP 5611]Slave040_QB1*=R

  Due to this entry, the following access rights are effective:

  DP:[CP 5611]Slave040_QB2=W

  DP:[CP 5611]Slave040_QB1=R

  Tip: Please read the detailed description of the syntax in the OPC documentation listed below. There, you will find a series of examples - also for applications such as PROFINET IO.
- Leading zeros in items and in the definitions made here for the access rights are always ignored.

  The following example illustrates the advantage of this:

  You configure the following access right: Slave004_QB0=R

  You have therefore implicitly assigned the access right to the following items:

  - Item 1: Slave00004_QB000
  - Item 2: Slave4_QB00,1 (note: the syntax ",1" is demanded by the OPC Scout)

  When using the wildcards "*" and "?", this means the following:

  Do not use these wildcards at positions at which a leading zero can precede an item!

  Example:

  The definition Slave0?9M06_AB1=R must be replaced by the two following definitions:

  - Slave?9M06_AB1=R
  - Slave9M06_AB1=R

###### Further information

Read the detailed description of the syntax in the OPC documentation. There, you will find a series of examples - also for applications such as PROFINET IO.

---

**See also**

[Leading zeros in items - example with wildcards:](#leading-zeros-in-items---example-with-wildcards)

###### Leading zeros in items - example with wildcards:

You are using the following item:

- Slave00004_QB000

An access right definition that would fail in the comparison might be:

- Slave0?4_QB0=R

Reason:

In the comparison, a leading "0" is found in the item, the item is therefore reduced to: Slave4_QB

Due to the wildcard "?", the leading "0" in the definition is no longer detected as a leading "0". The definition for the access right is therefore not reduced and the comparison fails.

###### Remedy:

To achieve the required rights for this example, the following two definitions would be necessary:

- Slave?4_AB0=R
- Slave4_AB0=R

---

**See also**

[Syntax - OPC item-specific access rights](#syntax---opc-item-specific-access-rights)

#### S7-specific settings

This section contains information on the following topics:

- [OPC symbols](#opc-symbols)
- [OPC alarms:](#opc-alarms)
- [Assignment table for OPC alarms](#assignment-table-for-opc-alarms)

##### OPC symbols

This section contains information on the following topics:

- [Using symbols](#using-symbols)
- [Symbol configuration](#symbol-configuration)
- [Entering limit values for EU Lo and EU Hi](#entering-limit-values-for-eu-lo-and-eu-hi)
- [Range of values of the data types](#range-of-values-of-the-data-types)
- [Syntax - OPC item-specific access rights](#syntax---opc-item-specific-access-rights-1)

###### Using symbols

###### Reference

Settings for OPC server / "Properties > S7 > OPC symbols" parameter group.

###### Using symbols (as of OPC server V6.1)

Here, you can specify whether symbols from the symbol tables configured for a CPU will be included in the system data for the OPC server. This is necessary before user applications (OPC client) can access variables symbolically via the OPC server.

The symbol tables of the CPUs to which S7 connections are configured for the OPC server are used. Only symbols that relate to data blocks (DBs) are taken into account.

The available alternatives have the following meaning:

- None

  No symbols from STEP 7 are included in the system data for the OPC Server. The access rights configured for the OPC items under Access protection apply.
- All

  All relevant symbols from STEP 7 are included in the system data for the OPC server.

  Making this selection sets the access rights for all symbolic access to the assigned variables to Read/Write (RW). These rights have priority over the access rights for the OPC items set under Access rights.
- Configuring

  All selected and specifically configured symbols from STEP 7 are adopted in the system data for the OPC server. With the "Configure" button, you open the "Symbol configuration" dialog in which you can select and configure the symbols.
- Array elements visible at runtime (selectable as of OPC server V8.0)

  Here, you can decide whether you want the elements of arrays to be visible on the OPC server during runtime. This relates to the arrays configured as symbols.

  As default, the option is disabled because making array elements visible causes a high load on the OPC server. With older OPC server versions (< V8.0), array elements are always visible and this setting cannot be disabled.

  > **Note**
  >
  > **Consistency**
  >
  > If you select the "All" option, the current CPU symbol tables are taken into account when you save and compile.
  >
  > If you use the "Configured" option, remember that subsequent changes in the symbol tables have the following effects in the system data for the OPCserver:
  >
  > - Newly added symbols are ignored
  > - Selected symbols that were removed later in the symbol table cannot be saved.

  > **Note**
  >
  > **Bit arrays**
  >
  > Symbols that include data of the "bit array" type are not included in the system data of the OPC server!

  > **Note**
  >
  > **Note on the procedure**
  >
  > While the symbols are being adopted as described here, no FB in which symbols are used may be open in LAD / STL / FBD. Otherwise some symbols will not be read in.

###### Symbol configuration

###### Reference

Settings for OPC server / "Properties > S7 > OPC symbols" parameter group.

Calling the symbol configuration with the "Configure symbols" button.

###### Overview

In this dialog, you can select and configure the symbols to be adopted in the system data of the OPC server.

The CPUs relevant for the selection of symbols are those to which S7 connections are configured for the OPC server.

In the navigation area on the left, you will see the relevant stations and CPUs along with any structure elements. In the content area on the right, you will see the symbols defined for the selected CPU or the selected structure element. The assigned data type and the currently configured properties are shown for each symbol. These properties can be configured in the lower part of the dialog.

> **Note**
>
> Note that the display in the "Access" column can also contain the value "mixed(default access right)". This is displayed when the access right in a lower level element is not the same as the default access right. The default access right is specified as standard for newly created lower-level elements.

###### Selecting and configuring symbols

1. First select the symbol group of a CPU or a structure element in the navigation area.
2. Then select one or more symbols with the mouse pointer in the content area.
3. Configure the properties of the selected symbols in the lower part of the dialog as described below.

###### "Elements in active branch" display

The displays have the following meanings:

- Symbols: Total number of symbols in the selected branch or in the selected structure element (a selected structure element is included in this number).
- Array elements: Number of elements in the array

  - Value shown on the left: Number of elements selected as visible
  - Value shown on the right: Total number of elements
- Activated historical data: Total number of archived symbols in the selected branch or in the selected structure element (a selected structure element is included in this number).

For the elements "DTL" and "Array[...] of DTL", the following applies to the difference between the displayed number for the enabled options "Enable access to historical data" and "Visible" as shown in the following example:

| Element | Number of symbols with enabled option "Enable access to historical data". | Number of symbols with the "Visible" option enabled |
| --- | --- | --- |
| DTL | 1 | 9 |
| Array[1..n] of DTL | 1 | n * 9 + 1  n = Number of array elements |

###### Configurable properties

- "Visible" option

  If you disable this option, the selected symbol is excluded from the download to the OPC server.
- "Download only visible symbols" option

  If you select the option, only the symbols marked as "visible" are adopted in the system data of the OPC server and are therefore visible to the OPC client. The option reduces the time for the download to the OPC server considerably if large numbers of symbols are marked as "not visible".
- Access right

  From the drop-down list, you can assign the following access permissions to the selected symbols:

  - Read-write: Read and write
  - Read: Read
  - Write: Write
  - None: No access

    The access permissions selected here have priority over the access permissions configured for the OPC items in access protection.
  > **Note**
  >
  > Note that the setting for "Access right" is not exported and therefore also not imported, but the current setting is always displayed.
- Connection  
  From the drop-down list of the configured connections, select the S7 connection via which the symbolic variable access will be made.
- "Edit EU Lo / Hi" input boxes - Specify tolerance range for measured values (EU Lo and EU Hi limit values)

  Here, you specify limit values for calculating a deadband for a selected OPC item. The input boxes are enabled under the following condition:

  - You have only selected a single symbol;
  - An elementary data type is assigned to the symbol that permits a numeric representation (INT, DINT, REAL, BYTE, WORD, DWORD).

    Note:

    This entry is possible only for OPC servers as of version 6.4.

    See also [Entering limit values for EU Lo and EU Hi](#entering-limit-values-for-eu-lo-and-eu-hi)

###### "Access path" display

The storage path of the selected object in the current STEP 7 project is displayed in the navigation area.

###### Special features

- Bit arrays are not adopted

  Symbols that include data of the "bit array" type are not adopted in the system data of the OPC server. This restriction applies although this symbol is displayed for selection. This restriction applies regardless of whether you set the "visible" option (see above) for these symbols.
- The data types "Array of UDT" and "Array of Struct" are displayed differently

  With symbols of the complex data type "Array of UDT" or "Array of Struct", the structure of the "UDT" or "Struct" data type is only displayed once in the left-hand area of the dialog. The "Array" entry in the "Data type" box on the right indicates that this involves an array.

  Only the first array element is displayed with its addresses and therefore the address assignment of the individual elements.

  In contrast to this, other tools, such as the Symbol File Configurator display multiple array elements.

  The data structures involved are nevertheless identical.

  Note that the setting for the "Visible" option described above applies to all elements of an array including array elements that are not displayed.

###### Entering limit values for EU Lo and EU Hi

###### Entering the tolerance range for measured values (high and low limit values EU Lo and EU Hi)

Here, you specify limit values for calculating a deadband for a selected OPC item (for the meaning, see below).

You can specify numeric values as integers, floating points or in exponential notation (scientific notation)

Note: As separator use the "." character instead of the "," character.

- EU Lo (Engineering Unit Low)

  Low limit
- EU Lo (Engineering Unit Low)

  High limit

the following must apply: EU Lo <= EU Hi

If an input box is left empty it is automatically completed with "0".

Make sure that you keep to the value ranges depending on the data type. [Range of values of the data types](#range-of-values-of-the-data-types)

- Examples:

  - EU Lo = 10 EU Hi = 25
  - EU Lo = 4.5 EU Hi = 14.5
  - EU Lo = 1.2e-2 EU Hi = 2.5e-2
- Notes:

  - The tolerance range ("Percent Deadband") applies to a group of OPC items.
  - This entry is possible only for OPC servers as of version 6.4.

###### Meaning of the low limit value EU Lo and high EU Hi

Fo rmeasured values, you can specify deadbands for measured value acquisition. Within such a percent deadband, a measured value can change without the change being signaled.

To achieve this, a relative value is calculated from the specified parameters according to the following formula. This value specifies the maximum number of units by which a physical value can change up or down without a value change being signaled.

---------------------------------------------------------  
A = PD / 100 x ( EU HI – EU Lo)  
---------------------------------------------------------

where:

A = amount of the deviation (up or down)

PD = Percent Deadband / %

EU Lo = low limit value

EU Hi = High limit value

###### Example

With a temperature measurement, you assume that there is a typical deadband for the measured value in the range between 30°C and 40°C. As the percent deadband, set 10%.

You would therefore select the following values:

EU Lo = 30

EU Hi = 40

PD = 10%

This results in: A = 10 / 100 x (40 – 30) = 1

A temperature change is therefore signaled when the temperature is more than 1 °C above or below the previous measured value.

---

**See also**

[Symbol configuration](#symbol-configuration)

###### Range of values of the data types

The following ranges of values for the data types used are valid:

| Data type | Value range |
| --- | --- |
| BYTE | 0 ... 256 |
| INT | -32768 ... 32767 |
| WORD | 0 ... 65535 |
| DWORD | 0 ... 4294967295.0 |
| DINT | -2147483648 ... 2147483647.0 |
| REAL POS UPPER | 3.402823e+38 |
| REAL POS UNDER | 1.175495e-38 |
| REAL NEG UPPER | -1.175495e-38 (negative low limit) |
| REAL NEG UNDER | -3.402823e+38 (negative low limit) |

---

**See also**

[Entering limit values for EU Lo and EU Hi](#entering-limit-values-for-eu-lo-and-eu-hi)

###### Syntax - OPC item-specific access rights

You can enter access rights for one or more OPC items.

The default rights defined for the other OPC items are not affected.

###### The syntax for OPC item-specific access rights is defined as follows:

<OPCItem>=<rights>

where:

- <OPCItem>

  You specify one or more OPC Items according to the syntax defined in the OPC documentation. It is also possible to use aliases.

  The following placeholders can be used:

  * Any number of irrelevant characters

  ? exactly one character is irrelevant
- <rights>

| Symbol | Meaning |
| --- | --- |
| Read-write | Read and write |
| Read | Read |
| Write | Write |
| None | No access |

###### Rules for evaluation

- The specific rights assigned here have priority over the default rights you assigned in the input area Access protection.
- The specific rights assigned here are evaluated in the order shown here. If there is a multiple assignment for an OPC item, the last assignment is always valid.

  Example:

  DP:[CP 5611]Slave040_QB*=RW

  DP:[CP 5611]Slave040_QB1=R

  DP:[CP 5611]Slave040_QB2=W

  DP:[CP 5611]Slave040_QB1=W

  DP:[CP 5611]Slave040_QB1*=R

  Due to this entry, the following access rights are effective:

  DP:[CP 5611]Slave040_QB2=W

  DP:[CP 5611]Slave040_QB1=R

  Tip: Please read the detailed description of the syntax in the OPC documentation listed below. There, you will find a series of examples - also for applications such as PROFINET IO.
- Leading zeros in items and in the definitions made here for the access rights are always ignored.

  The following example illustrates the advantage of this:

  You configure the following access right: Slave004_QB0=R

  You have therefore implicitly assigned the access right to the following items:

  - Item 1: Slave00004_QB000
  - Item 2: Slave4_QB00,1 (note: the syntax ",1" is demanded by the OPC Scout)

  When using the wildcards "*" and "?", this means the following:

  Do not use these wildcards at positions at which a leading zero can precede an item!

  Example:

  The definition Slave0?9M06_AB1=R must be replaced by the two following definitions:

  - Slave?9M06_AB1=R
  - Slave9M06_AB1=R

###### Further information

Read the detailed description of the syntax in the OPC documentation. There, you will find a series of examples - also for applications such as PROFINET IO.

##### OPC alarms:

This section contains information on the following topics:

- [Configuring OPC alarms](#configuring-opc-alarms)

###### Configuring OPC alarms

###### Reference

Settings for OPC server / "Properties > S7 > OPC alarms" parameter group.

###### Language / message text language setting

For OPC alarms, you specify which language versions of the text library for alarm texts (block- and symbol-related alarms) will be downloaded to the OPC server.

Using the two check boxes, you can set the following:

- The default language (specified as the default language for display devices):   
  When the default language for alarms is one of the following STEP 7 default languages: German (Germany), English (USA), French (France), Spanish (Traditional Sort), Italian (Italy). Otherwise the check box is disabled.
- English (USA)   
  (if English (USA) is installed as the default language)   
  If the default language for display devices is already English (USA), the check box is disabled.

You can select one or both options. If you select both options, a check is made as to whether multiple language text storage was selected in "Language for display devices" in the project. If this is the case, the relevant text libraries are downloaded when you download to the PC station.

###### Time stamps for alarms

In this parameter group, you decide which entity will set the time stamp of an alarm. If you leave time stamping to the CPU, you obtain alarms with the exact time of their occurrence. With the option of specifying a time offset, you can also register alarms occurring, for example, in plants with different time zones with a common reference time in the acquisition system.

- CPU time stamp

  Alarms are given the time stamp of the signaling CPU. Exception: StatepathEvents are locally generated alarms and are given the PC time (UTC).
- CPU time + offset

  Alarms are given the time stamp of the CPU sending the alarm; a selectable time offset accurate to a second is added to the time stamp. Exception: StatepathEvents are locally generated alarms and are given the PC time (UTC).

  Range of the time offset: -23:59:59 to + 23:59:59
- PC time (UTC)

  Alarms are given the time stamp (UTC) at the time of arrival at the receiving PC station (OPC server).

##### Assignment table for OPC alarms

This section contains information on the following topics:

- [Assignment table for OPC alarms](#assignment-table-for-opc-alarms-1)

###### Assignment table for OPC alarms

###### Reference

Settings for OPC server / "Properties > S7 > Assignment table OPC alarms" parameter group.

###### Meaning

The alarm classes configured in the project in "Common data > Alarm classes" are displayed in a table. The OPC alarm category "OffNormal" is assigned to the message classes as default. If necessary, assign a different OPC alarm category.

#### S7 connections for access to optimized data blocks with S7-1200/S7-1500

To allow data access to optimized data blocks of the OPC server V12 to data blocks of unsure types, bit memory, inputs, outputs, counters and timers of a SIMATIC S7-1500 and SIMATIC S7-1200, you can configure a S7 connection to the CPU.

S7 connections for access to optimized data blocks in the S7-1200/S7-1500 are available only using Industrial Ethernet.

##### Requirements

- STEP 7 Professional V12 SP1 or higher
- OPC server V12 or higher
- S7-1500 or S7-1200 V4.0 or higher

##### Connection names for OPC server V12 and S7 connections

When you create an S7 connection for an OPC server, STEP 7 proposes a valid S7 connection name. You can change the S7 connection name at any time. Some characters and connection names are used by the system and cannot be used when assigning the connection name. STEP 7 checks for invalid characters in the connection name automatically.

##### Connection table

In the table network view in the "Connections" tab, the connections you have created and their parameters are displayed in the connection table. In the "Partner" column, you can change the communications partner to the OPC server V12.

##### Parameters of special connection properties

In the Inspector window of the selected S7 connection configured at one end (one-way), go to "Properties > Configuration > Special connection properties", the "One-way" and "Active connection establishment" check boxes are selected. You cannot make any changes in the "Special connection properties" parameter group.

##### Address details

In the Inspector window of the selected S7 connection configured at one end in "Properties > Configuration > Address details" you will see the TSAPs of the communications partners in the connection resources. The local TSAP is structured as follows:

SNOPCCxxxxyyyyyy

- SNOPCC = SIMATIC NET OPC Configured connection
- xxxx = index of the OPC server V12
- yyyyyy = connection ID of the S7 connection

The partner TSAP is "SIMATIC-ROOT-OTH".

You cannot make any changes in the "Address details" parameter group.

##### OPC parameters

In the Inspector window of the selected S7 connection configured at one end in "Properties > Configuration > OPC" you have the following configuration options:

- Enabling optimized access
- Configuration of the buffer size for optimized access to tags
- Administration of the optimized access to tags by entering the access password

**Buffer size:**

It may be useful to change the default buffer size in specific applications with particularly large numbers of data tags on a CPU (S7-1500 or S7-1200 V4.0). Access to contiguous data tags within a data area is optimized to improve performance. Optimum results are achieved with buffer sizes that include at least the majority of the contiguous data tags that are accessed regularly and often.

To ensure that S7OPT data can be read or written within one CPU cycle, you need to set the value for the "Buffer size for optimization" parameter in the OPC properties of the S7 connection to less than or equal to 64 bytes for an S7-1200 CPU (as of firmware version V4.0) or less than or equal to 512 bytes for an S7-1500 CPU (as of firmware version V2.0). For an S7-1500 CPU where the firmware version is less than V2.0, you must set the parameter less than or equal to 64 bytes.

##### Connection resources

With configured S7 connections for an OPC server V12 or higher, to allow data access to optimized data blocks on a PLC S7-1500 or S7-1200 V4.0 or higher, the connection resources required for this are displayed on the PLC page. You will find the display of the required connection resources in the properties of the relevant CPU in the Inspector window in "Properties > General > Connection resources".

For S7 connections for data access to optimized data blocks of an OPC server V12 or higher, the resources of such an S7 connection are not assigned to the "S7 communication" row on the PLC but to the rows "Other communication" (S7-1500) or "Free available connections" (S7-1200 V4.0 or higher). For a configured S7 connection for an OPC server V12 to an S7-1500 or S7-1200 V4.0 or higher, more than one connection resource is required.

##### Replacing a OPC server

With the "Change device" shortcut menu of a selected OPC server you have the option of replacing an OPC server V12 which allows access to optimized data blocks on S7-1500 or S7-1200 V4.0 with an OPC server < V12 and vice versa.

If S7 connections had already been configured for the OPC server you are replacing, during the replacement of the OPC server you will receive a message that the existing S7 connections will be deleted. Following replacement, these need to be recreated.

##### Display of an S7 connection configured at one end (one-way) between an OPC server V12 and an S7-1500 or S7-1200 V4.0 or higher

When an OPC server V12 has sent a successful job for data access to optimized data blocks on an S7-1500 or S7-1200 V4.0 or higher, this connection is displayed in the online connection table of the corresponding PLCs in STEP 7.

Such connections are also shown in the Inspector window "Connection information" of the selected online CPU: the online connection resources used on the PLC are displayed here.

#### Redundant OPC UA server

This section contains information on the following topics:

- [Redundant OPC UA server - basics](#redundant-opc-ua-server---basics)
- [Configuring S7 UA redundancy tab](#configuring-s7-ua-redundancy-tab)
- [Assigning an S7-UA redundancy group](#assigning-an-s7-ua-redundancy-group)

##### Redundant OPC UA server - basics

###### Transparent OPC UA redundancy servers

The following figure shows how the OPC UA servers are embedded in a redundancy group and configured for the transparent OPC UA redundancy solution.

![Transparent OPC UA redundancy servers](images/48087077003_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | You configure a PC station for each redundant OPC UA server. The redundant PC stations assigned to an OPC UA client form a redundancy group. This assignment is made by the uniform configuration of the "IP address of the redundancy group" for the OPC UA servers. |
| ② | The OPC UA client that is using the redundancy is located on a higher-level PC station.  The higher-level PC station does not need to be configured for use of OPC UA redundancy in the STEP 7 project. |
| ③ | The communication between the OPC UA servers and the programmable controllers is via multiple, identically configured S7 connections.  Depending on the configuration, S7 connections can be used via Ind. Ethernet or via PROFIBUS. |

###### Setting a SIMATIC NET OPC server as S7 OPC UA server for transparent OPC UA redundancy

You can achieve transparent redundancy to be used by the higher-level OPC UA client by following the steps outlined below during configuration:

1. To operate PC stations with redundant SIMATIC NET OPC UA servers, create a component of the type OPC server >= V8.1 for each station. Enable S7 UA redundancy for these OPC servers.
2. They adopt the virtual IP address. You specified this virtual IP address previously in the network load balancing manager (NLB) for both PC stations. The virtual IP address is mapped to the real IP addresses of the OPC UA server.
3. You specify a port via which the two OPC UA servers can communicate so that they can synchronize their data;
4. You configure identical S7 connections for both OPC UA servers for communication with the connected automation systems;
5. Authentication certificates are generated automatically and assigned to the PC stations. If necessary, assign the two redundant PC stations newly generated authentication certificates.

###### Consistency check

When you save and compile the configuration, a consistency check is run. In relation to OPC UA redundancy, the following checks are made:

- The server-to-server addresses within a redundancy group must be unique. A common IP address of a redundancy group may also only be used once within a project.
- Each member of a redundancy group must have the same S7 connections with the same connection names and the same communications partners.
- The hardware configuration of the PC stations in the redundancy groups must be identical. In other words, the modules used for the redundancy function must be identical in the redundant PC stations.
- The parameters of the S7 connections must be identical; these include connection establishment, alarms, optimizations, PDU size, number of parallel jobs, monitoring times.
- The S7 settings of the OPC UA servers must be identical; these include cycle time, access rights, S7 alarms and S7 symbols.

  > **Note**
  >
  > **Recommendation: Permanently established S7 connections**
  >
  > We strongly recommend that you configure active, permanently established S7 connections on the OPC UA servers. This achieves shorter failover times if there is a server failure.

###### Procedure / recommendation

The parameter assignments of the redundant OPC UA servers must match each other. When you save and compile the configuration, a consistency check is run.

By using the STEP 7 options for copying, you reduce the risk of inconsistent information. Either copy the entire PC station or only the OPC server. If you have already configured S7 connections, these are also copied. The connections in the copied PC station must still be assigned the relevant connection partner.

---

**See also**

[Configuring S7 UA redundancy tab](#configuring-s7-ua-redundancy-tab)

##### Configuring S7 UA redundancy tab

###### Reference

Setting a redundant OPC UA server in the "Properties > General > S7 UA Redundancy" parameter group

###### Transparent OPC UA redundancy

In this parameter group, you configure the PC station as a redundant OPC UA server for operation with transparent OPC UA redundancy. Here, use the SIMATIC NET OPC server version 8.1

The redundant PC stations assigned to an OPC UA client belong to a redundancy group.

###### In this parameter group, follow the steps outlined below:

1. Select the "Enable redundancy" option.
2. Enter the IP address of the redundancy group. Here, you have the following options:

   - You can either enter the IP address directly or accept or modify the proposed IP address.

     Select this option if you want to create a new redundancy group.
   - Click the "Assign" button

     Select this option to assign the OPC server to an existing redundancy group.

     > **Note**
     >
     > After entering or assigning, note the "IP addresses of the other members of the redundancy group" table at the end of the parameter group. You can see which OPC servers are assigned to the same redundancy group.
3. Specify the redundancy port for communication with the OPC UA client; if appropriate, accept the default setting.
4. Set the parameters for the server-to server communication.
5. If necessary check the authentication certificate assigned to the OPC server using the "Display..." button.

###### Parameters / input areas / buttons

- "Enable redundancy" option

  By selecting the option, you enable the parameter assignment option for the OPC UA server functionality.
- "Assign..." button

  You open the dialog in which the redundancy groups that have already been created can be selected.
- "IP address of redundancy group" parameter

  Virtual IP address via which the OPC UA client reaches the redundant OPC UA server (the redundancy group).

  You specify this virtual IP address in the network load balancing manager (NLB) for both PC stations. The virtual IP address is mapped to the real IP addresses of the OPC UA server.
- "Redundancy port" parameter

  Port via which communication with the OPC UA client is handled.

  Default: 4845
- "Server-to-server port" parameter

  Port via which the communication for synchronization with the OPC UA servers in the redundancy group is handled.

  Default: 4846
- "Server-to-server interface" parameter

  Here, select the interface to the subnet via which the synchronization with the OPC UA servers in the redundancy group is handled.
- "Certificate" input area / "Display..." button

  STEP 7 automatically generates a certificate that it is transferred to the OPC UA client during connection establishment. The OPC UA client uses this for authentication during the subsequent communication.

  The certificate is also used to transfer the key for data encryption.

  The private key remains on the server and is used for encryption. With the corresponding public key it received from the server with the certificate, the client can then encrypt messages of the server.

  You can display the currently valid certificate here and check it.

  Note:  
  The certificate display does not recognize whether or not a certificate is already being displayed. Each time you click the "Display..." button, a new certificate display is opened.
- "Certificate" input area / "Update" button

  You instruct STEP 7 to create a new certificate.

###### IP addresses of the other members of the redundancy group

Display of the other members of the redundancy group. A redundancy group is made up of the PC stations that are assigned the same "IP address of the redundancy group".

> **Note**
>
> **Maximum number of members in a redundancy group**
>
> In the current version of STEP 7 V12, **2** OPC UA servers are supported within a redundancy group.

---

**See also**

[Redundant OPC UA server - basics](#redundant-opc-ua-server---basics)

##### Assigning an S7-UA redundancy group

###### Reference

Setting a redundant OPC UA server in the "Properties > General > S7 UA Redundancy > S7 UA Redundancy Master" parameter group

###### Assigning an existing S7-UA redundancy group

The table shows the redundancy groups available and selectable in the STEP 7 project along with their IP addresses.

If you have assigned a new IP address to the current OPC server, the following entry appears instead of this assignment:

- "(own redundancy group <IP address>)"

###### Follow the steps outlined below:

1. Select the required redundancy group.
2. Confirm the dialog with the "OK" button.

The IP address of the selected redundancy group is then adopted in the "S7-UA Redundancy" parameter group.

---

**See also**

[Redundant OPC UA server - basics](#redundant-opc-ua-server---basics)

#### PLC alarms for OPC server

##### SIMATIC NET OPC server - Recommendations on the configuration of CPU messages

If you configure PLC alarms for an OPC server of a PC station, their consistent configuration will not be verified by STEP 7. To ensure error-free functioning of the PLC alarms, note the following recommendations:

- Only ever configure one S7 connection with interrupt capability per PLC for receiving alarms.
- Only use one language for alarm texts in a given project. The use of multi-language alarm texts is not supported.
- For all alarms, avoid inputting user-specific sources (additional text 1). The uniqueness of the alarms is automatically ensured if the default sources are used.

#### Editor for OPC program alarms

##### General

The editor for OPC program alarms is available as of OPC server V14. This helps you to configure OPC program alarms of an S7 connection between a PC station or OPC server and an S7-1500/S7-1500S so that the display in the user-specific view, for example corresponds to your plant topology. At the same time you can add, rename or delete areas, sources and conditions in the user-specific view and can also manage them in different langages. The structure and the names of the OPC program alarms in the default view are preset based on the tree structure from the STEP 7 project. The texts of the OPC program alarms are configured in the STEP 7 configuration of the S7-1500/S7-1500S. The created structure of the OPC program alarms in the user-specific view is displayed identically in the OPC UA client with browsing interface after you have compiled and downloaded the configuration of the PC station.

##### Default view

The available OPC program alarms are displayed in the default view. With a high number of OPC program alarms, coordination between the PLC configuration and OPC configuration is advisable to make management clearer.

The requirement is an S7 connection in whose OPC properties the check boxes "Maintain connection permanently" and "Receive program alarms" are enabled (select "Network view" > "Connections" tab > "S7 connection" > "General" tab > "OPC" > "Connection establishment" or "Alarms").

> **Note**
>
> A If after configuration in the editor you disable the check boxes "maintain connection permanently" or "Receive program alarms" in the OPC properties of the S7 connection, the OPC program alarms configured up to then are no longer displayed in the default view until the options are enabled again.

> **Note**
>
> If you do not configure OPC program alarms in the user-specific view and download the STEP 7 project to the PC station, the OPC program alarms in the OPC UA client will be displayed identical to the preset tree structure of the STEP 7 project.

##### User-specific view

In the user-specific view, you have the option of structuring OPC program alarms to meet your requirements. Using the context menu for "S7OPTAREAS:" you define the areas and sources according to your plant topology and add the conditions in the relevant sources.

Between the default view and the user-specific view, arrow symbols show you the graphic assignment of the conditions. If a condition is selected in the the user-specific view, you will see the origin and target based on the arrow symbol. Depending on which node is selected or the extent to which the tree structures are expanded or collapsed the position of the arrow symbol changes. With collapsed tree structures, the arrow symbols can e displayed merged. The following options exist for the graphic assignment of the conditions by arrow symbols:

- The tree structures are fully expanded in both views. By selecting a condition the direct 1:1 assignment between the origin and destination of the condition is diplayed.
- The area or the source in which the condition (origin) is contained is collapsed in the default view. A condition (destination) is selected in the user-specific view. From the area or the source the arrow symbol points from the default view to the condition (destination) in the user-specific view.
- The area or the source in which the configured condition (destination) is contained is collapsed in the user-specific view. A condition (origin) is selected in the default view. From the area or the source the arrow symbol points from the user-specific view to the condition (origin) in the default view.
- A condition is selected in the default view that is not configured in the user-specific view. No arrow symbol is displayed, since no assignment is made or is possible.

As soon as you have configured a condition in the user-specific view, this is grayed out in the default view. If you delete a condition from the user-specific view, this is no longer grayed out in the default view and can be used again elsewhere in the user-specific view.

> **Note**
>
> If you delete OPC program alarms from the S7-1500/S7-1500S, these are no longer displayed in the default view. In the user-specific view, these OPC program alarms are marked red and are inconsistent. You can no longer use the inconsistent OPC program alarms and need to delete them manually.

> **Note**
>
> All the OPC program alarms configured on the PLC that are not configured in the user-specific view are nevertheless also loaded on the PC station when it is loaded. On the OPC client, these OPC program alarms not configured in the editor are contained in a special folder. The name of this folder corresponds to the name in the PLC configuration.

##### Meaning of the icons used

In the editor for OPC program alarms there are the following icons that are used to display areas, sources and conditions in both views:

![Meaning of the icons used](images/87347163659_DV_resource.Stream@PNG-de-DE.png)

Area:

Every station name (e.g. Station1), device name (e.g. Controller1) or group (e.g. Group1) is represented in the default view as an area. The resulting tree structure is decided by the STEP 7 project structure.

The area must first be created in the user-specific view because there is no area present at the start. Several areas can be defined.

![Meaning of the icons used](images/87354771723_DV_resource.Stream@PNG-de-DE.png)

Source:   
The source in the default view consists of the station name (e.g. Station1), device name (e.g. Controller1) and the symbolic name of the data block of the PLC alarm (e.g. Motor1).

A source must be added to an area in the user-specific view. Several sources can be added to an area.

![Meaning of the icons used](images/87354762891_DV_resource.Stream@PNG-de-DE.png)

Condition:   
The condition in the default view consists of the name of the configured OPC program alarm. Example: alarm_motor1

Conditions are dragged from the default view to the required source within the user-specific view.

##### "General" Tab

The "General" tab displays the properties "Condition", "OPC severity" and "OPC event type" of the selected OPC program alarm. The input box "Condition" can be edited.

##### "General" > "OPC alarm instances" tab

In the "General" > "OPC alarm instances" tab, you obtain an overview of various properties of the OPC program alarm. These properties are read-only at this point and cannot be changed.

The following properties of the OPC program alarms:

- Name  
  Specifies the name of the OPC program alarm
- ID  
  Specifies the ID of the OPC program alarm.
- PLC name  
  Specifies the name of the S7-1500/S7-1500S on which the OPC program alarms are configured.
- Message text  
  Specifies the message texts configured on the S7-1500/S7-1500S.
- Condition  
  Specifies the name of the condition
- OPC severity  
  Specifies the OPC severity of the OPC program alarm.
- Area  
  Specifies the name of the area of the OPC program alarm

##### "Languages & Resources" dialog box

In the "Languages & Resources" dialog box you can set the editing language and the reference language in all languages supported by "STEP 7 Professional (TIA portal)". This gives you the option, for example, of editing and saving in German and when you then later switch over to the English language, you can rename and store the names of the OPC alarms in English. Depending on which language you now set the names of the OPC program alarms will always be displayed to you in the "correct" language. New names of the OPC program alarms that have not yet been translated are enclosed in the characters "<" and ">" in the user-specific view.. In the default view the same names are used for all languages as was defined in the configuration in the PLC.

You can add further project languages with "Project tree" > "Languages & resources" > "Project languages".

In e.g. "Project tree" > "Languages & resources" > "Project texts" all project texts including the alarm texts of the conditions can be displayed and edited. In the same Inspector window, project texts can also be imported or selected project texts, here conditions, can be exported.

> **Note**
>
> For the translation of the names of the OPC program alarms into the various languages, for easier handling the described import or export function is recommended.

##### Typical procedure for the first use of the editor

Proceed as follows:

1. Create OPC program alarms in the S7-1500/S7-1500S for the STEP 7 project. With the S7 connection, the OPC properties "Maintain connection permanently" and "Receive program alarms" must be enabled.
2. Open the editor for OPC program alarms by double-clicking on "Editor for OPC program alarms" in the tree tree structure of the project tree of the relevant OPC server of the STEP 7 project.
3. In the user-specific view select the command "Add area node" from the shortcut menu of "S7OPTAREAS:"
4. Assign the newly created area any name (forbidden characters "\" and control characters). In keeping with your plant topology you can place other areas in the area.
5. Select the command "Add source" from the shortcut menu of the relevant area.
6. Assign the source any name (forbidden characters: control characters).
7. Drag the conditions from the default view to the required position in the user-specific view.
8. Assign the condition any name (forbidden characters: control characters).
9. If necessary, specify the editing and reference language in the "Languages & Resources" dialog box. Note that the untranslated names in pointed brackets (<>) will be translated.
10. Save and compile or load the new configuration in the PC station and in the PLC..
11. Open an OPC UA client that has a browsing interface.
12. Enable and monitor the configured OPC program alarms.

> **Note**
>
> If you select a node that has already been created, you can use the keys "x", "+" and "-" in the numeric keypad to speed up opening and closing of the lower-level tree structure.
>
> - Multiplication kex "x": Opens the entire lower-level tree structure of the selected node.
> - Addition key "+": Opens only the selected node.
> - Subtraction key "-": Closes the entire lower-level tree structure of the selected node.
>
> This functions both in the default view and in the user-specific view.

##### Typical procedure for further use of the editor

1. Open the editor for OPC program alarms by double-clicking on "Editor for OPC program alarms" in the tree tree structure of the project tree of the relevant OPC server of the STEP 7 project.
2. Analyze the actual situation of the existing configuration.
3. Decide what you want to reconfigure.
4. Make the changes accordingly.
5. Save and compile or load the new configuration in the PC station and in the PLC..
6. Open an OPC UA client that has a browsing interface.
7. Enable and monitor the configured OPC program alarms.

##### Consistency check

The configuration in the editor for OPC program alarms is checked for consistency before it is downloaded to the PC station. During this, the following compilation errors or warnings can be triggered:

| Compilation error or warning | Remedy |
| --- | --- |
| Error: The OPC program alarms of the specified PLC are connected via several connections. | The OPC program alarms may only be connected via one S7 connection. |
| Error: The combination of the specified source and condition is not unique in a language. | The combination of source and condition must be configured to be unique. |
| Error: The OPC program alarm in the specified path contains invalid characters in the specified language. | Only permitted characters may be used: |
| Error: The OPC program alarm in the specified path contains at least one area node, a source or a condition with invisible ANSI code characters in the specified language. | Only permitted characters may be used: |
| Error: For the OPC program alarm in the specified path at least one area node, a source or a condition is not translated into the specified language. | All translations must exist for the languages used. |
| Error: The OPC program alarm in the specified path is no longer valid because there is no S7 connection with valid alarm properties to the specified PLC. | A suitable S7 connection needs to be created or the named OPC program alarm needs to be deleted in the user-specific view. |
| Error: The OPC program alarm in the specified path is no longer valid because the corresponding PLC alarm instance no longer exists. | The named OPC program alarm needs to be deleted in the user-specific view. |
| Warning: The specified alarm text is not translated in the specified language. | The preset text must be adapted to the specified language. |
| Warning: The specified OPC program alarm on the specified path is not configured in the user-specific view, but the OPC server uses at least one OPC program alarm that was configured in the user-specific view. | If necessary, configure OPC program alarm shown in the warning in the user-specific view. |

> **Note**
>
> Displayed compilation errors must be eliminated efoe you can download the configuration to the PC station.
>
> Compilation warnings can if applicable be ignored, in other words the configuration can be downloaded to the PC station without rectifying the warning.

#### Access to historical data (Historical Access)

##### Requirements

The following requirements are linked to the use of historical data:

- You can enable a maximum of 1000 symbols simultaneously over the S7OPT and 1000 symbols over the S7 OPC UA server as historical data.
- Only visible symbols can be enabled as historical data.
- Only symbols with at least read permission (read or read/write) can be enabled as historical data.
- Access to historical data is only possible for the following S7OPT or S7 data types:

  | S7OPT data types | OPC UA data type |
  | --- | --- |
  | BYTE | Byte |
  | USINT | NByte |
  | CHAR | SByte |
  | SINT | SByte |
  | WCHAR | UInt16 |
  | WORD | UInt16 |
  | UINT | UInt16 |
  | DWORD | UInt32 |
  | UDINT | UInt32 |
  | LWORD | UInt64 |
  | ULINT | UInt64 |
  | INT | Int16 |
  | DINT | Int32 |
  | LINT | Int64 |
  | REAL | Float |
  | LREAL | Double |
  | DATE_TIME | UtcTime |
  | LDT | UtcTime |
  | DTL | UtcTime |
  | DATE | UtcTime |
  | TIME | Int32 |
  | LTIME | Int64 |
  | TOD | UInt32 |
  | LTOD | UInt64 |
  | S5TIME | UInt16 |
  | BOOL | Boolean |
  | STRING | String (UTF-8) |
  | WSTRING | String (UTF-8) |
  | TIMER | UInt16 |
  | COUNTER | UInt16 |

  | Supported S7 data types | OPC UA data type |
  | --- | --- |
  | BYTE | Byte |
  | CHAR | SByte |
  | WORD | UInt16 |
  | DWORD | UInt32 |
  | INT | Int16 |
  | DINT | Int32 |
  | REAL | Float |
  | DATE_TIME | UtcTime |
  | DATE | UtcTime |
  | TIME | Int32 |
  | TOD | UInt32 |
  | S5TIME | UInt16 |
  | BOOL | Boolean |
  | STRING | String (UTF-8) |
  | TIMER | UInt16 |
  | COUNTER | UInt16 |

##### Activating historical data

To activate historical data, you navigate to the configured symbols and select the "Enable access to historical data" check box.

> **Note**
>
> Access to historical data is enabled by default for all symbols.

##### Using historical data in the symbol configuration

When you select a row in the table that contains historical data, the value "True" is displayed in the "Historical data" column.

When you select a row in the table that does not contain any historical data, the value "False" is displayed in the "Historical data" column.

When you select a row in the table that does not contain any historical data but one of the child nodes contains historical data, the value "mixed(False)" is displayed in the "Historical data" column.

When you select a row in the table that contains historical data but in which historical data are disabled in one of the child nodes, the value "mixed(True)" is displayed in the "Historical data" column.

Use "Number of historical data" to display the number of selected historical data on the left side of the symbol configuration.

If no value is displayed in the "Historical data" table column, the selected node does not contain any historical data that can be enabled.

##### CSV Import / Export

When historical data are enabled during CSV Import / Export, you have the following selection of access rights:

- N  
  None
- R  
  Read only access - Historical data are not enabled
- HR  
  Read access - Historical data are enabled
- W  
  Write only access
- RW  
  Read and write access - Historical data are not enabled
- HRW  
  Read and write access - Historical data are enabled

#### Editor for OPC UA PubSub communication

This section contains information on the following topics:

- [OPC UA PubSub communication model](#opc-ua-pubsub-communication-model)
- [Secure OPC UA PubSub communication](#secure-opc-ua-pubsub-communication)
- [Supported data types for OPC UA PubSub communication](#supported-data-types-for-opc-ua-pubsub-communication)
- [Configuring an OPC UA Publisher with local Security Key Service](#configuring-an-opc-ua-publisher-with-local-security-key-service)
- [Configuring an OPC UA Subscriber](#configuring-an-opc-ua-subscriber)
- [Configuring the local SKS](#configuring-the-local-sks)
- [Content Masks](#content-masks)

##### OPC UA PubSub communication model

###### General

As of Version V19, the SIMATIC NET OPC UA server supports secure OPC UA PubSub communication over UDP according to OPC UA Specification Part 14 for the S7 and "S7 optimized" protocols.

###### How does OPC UA PubSub communication work in the PC application?

The Publisher sends its published data using a UDP Multicast address in the network.

In order to subscribe to data, the Subscriber receives information about the structure of the packet to be subscribed from the Publisher. The Subscriber can use this data to filter all packets received over the network.

The following figure shows the main components of the OPC UA PubSub communication model:

![OPC UA PubSub communication model](images/123910905355_DV_resource.Stream@PNG-en-US.png)

OPC UA PubSub communication model

Definition of terms

| Term | Description |
| --- | --- |
| Connection | A connection saves data about the network protocol used and the IP address via which the published data is sent or via which the subscribed data is received.  Important parameters are the address, the PublisherId and the transport profile URI. |
| Publisher | OPC UA PubSub components that send network messages to a network (publish). |
| Subscriber | OPC UA PubSub components that receive network messages of the Publisher from the network (subscribe). |
| PublishedDataSet (Publisher) | A PublishedDataSet contains a list (DataSet collection) of data points and their data type information that will be published. The following contents are compiled:  - Tags - Metadata |
| DataSetWriter (Publisher) | A DataSetWriter makes the information of a PublishedDataSet available as a data set for creation of a DataSetMessage. It describes how the data is structured in the packet. DataSetWriters are grouped in WriterGroups.  Among other things, the message format (message mapping) "UADP" (UA Datagram Protocol) is defined here. |
| WriterGroup (Publisher) | A WriterGroup defines the time intervals of published data. In addition, the settings for the encryption and signing of the packet are stored here.  Creates a network message from the DataSetMessage.  In so doing, additional parameters are defined for the message format (message mapping). |
| DataSetMessage | Can be encrypted and signed and has the following content:  - One or more data sets - Header with metadata |
| Network message | Transmission unit with the following contents:  - Header consisting of several parts - One or more DataSetMessages - A Security Footer (optional) and a signature (optional) |
| Frame on the transport layer | Transmission unit with the following contents:  - Header, including the data of the transport profile. - A network message |
| SubscribedDataSet (Subscriber) | The SubscribedDataSet contains information on the location in the address space where the subscribed data will be stored.  The contents of the received data set are assigned to the variables of the Subscriber. |
| DataSetReader (Subscriber) | The DataSetReader decrypts and distributes the data. DataSetReaders are grouped into ReaderGroups.  The parameters encoded by the Publisher are evaluated. |
| ReaderGroup (Subscriber) | A ReaderGroup forwards the message to the DataSetReaders. |
| Security Key Service | The Security Key Service (SKS) manages the security groups and makes the keys contained in them available to the Publishers and Subscribers. |
| SecurityGroup (SKS) | The keys for the encryption are managed in security groups within the SKS. Each security group manages one key and has a unique ID in the SKS. |

**Configuration limits and structure**

- A total of up to 500 variables/items can be configured for a PC application.
- The PC application can contain 1 to 500 connections.
- The PC application can contain 1 to 500 published data sets.
- The PC application can contain 1 to 500 subscribed data sets.
- A connection can contain one or more WriterGroups.
- A WriterGroup can contain one or more DataSetWriters.
- A connection can contain one or more ReaderGroups.
- A ReaderGroup can contain one or more DataSetReaders.

**Security (SKS)**

- Exactly one SKS can be used.
- The PC application contains an internal server for Security Key Services: the local SKS

  The parameters of the local SKS are inherited from the OPC server and are read-only.

  The local SKS is used by default.
- Alternatively, an external SKS can be configured: the default SKS

  The parameters of the default SKS can be configured.

##### Secure OPC UA PubSub communication

To make OPC UA PubSub communication secure, the network messages are sent encrypted (symmetrical encryption). For this, the Publisher and Subscriber must have the appropriate key for the encryption and decryption. The Security Key Service (SKS) takes on the management of the keys for the different OPC UA PubSub communications.

The SKS manages the keys of the secure OPC UA PubSub communications. The following SKSs are available:

- Local SKS

  The local SKS is used by default.

  It is part of the OPC UA server application and manages the keys of all OPC UA PubSub participants in the project. Both Publishers and Subscribers receive their keys for their OPC UA PubSub communication from this SKS.
- Default SKS

  As an alternative to the local SKS, an external SKS can be used.

  The SKS can be combined with a Global Discovery Server (GDS).

Each key in the SKS is stored in its own security group. This has a unique ID within the SKS. During configuration, Publishers and Subscribers receive the SecurityGroupID of their key as well as a description of the endpoint for access to the SKS. They log in to the SKS with this information. A rights concept ensures that only the partners involved in the OPC UA PubSub communication have access to the information of the specific security group. As a precondition for access to the SKS, the application URI of the SKS client must be stored in its certificate as "Alternative subject". In order to read the keys from the SKS, a Publisher or Subscriber must have OPC UA client functionality.

###### OPC UA PubSub security – Application URI

When an OPC UA client accesses a SecurityGroup, that the SKS manages, the SKS checks the application URI of the OPC UA client. If the OPC UA client is not authorized to access the SecurityGroup, the access is refused. This ensures that only authorized OPC UA clients can access the keys in a SecurityGroup. Because the application URI of the OPC UA client is also contained in its certificate, the OPC UA client cannot use a falsified application URI. The certificate of the OPC UA client must also be classified as trustworthy by the OPC UA server. Otherwise, a connection between the OPC UA client and OPC UA server cannot be established.

Depending on the use of the OPC UA server, the application URI is used in the configuration as follows:

- Use as SKS server: The application URI is entered in the endpoint description of the SKS server. The endpoint description is necessary for an SKS client to connect to the OPC UA server as SKS server.
- Use as SKS client: To register the SKS client in the SecurityGroup of SKS server, the application URI of the SKS client is entered in the Identity of the security group role for the SKS server.

The application URI of the OPC UA server of the SIMATIC NET PC software is contained in the respective server certificate of the OPC UA server and can be read out from the detailed information of the certificate. It can be found there under "Subject Alternative Name" in the form "URL=<Application URI>". Copy this URI and use it for your secure OPC UA PubSub configuration.

Example of an ApplicationURI of the SIMATIC NET S7OPT OPC UA server: `urn:Siemens.Automation.SimaticNET.S7OPT:(12345678-9ABC-DEF0-1234-567890ABCDEF)`

> **Note**
>
> The application URI is retained even after recreation of the OPC UA configuration and, thus, the OPC UA server certificates. The application URI changes when the SIMATIC NET PC software is updated or reinstalled. Therefore, be sure to adapt the application URI in the configuration after an update or reinstallation.

##### Supported data types for OPC UA PubSub communication

The following data types are supported for OPC UA PubSub communication with SIMATIC NET OPC UA server V19 or higher:

> **Note**
>
> The data types must be configured as follows for use by OPC UA services (options selected):
>
> - "Accessible from HMI/OPC UA"
> - "Writable from HMI/OPC UA"
> - "DB accessible from OPC UA"

| S7 data type | OPC UA data type |
| --- | --- |
| Bool | Boolean |
| Byte | Byte |
| Char | SByte |
| DInt | Int32 |
| DWord | UInt32 |
| Int | Int16 |
| LReal | Double |
| Real | Float |
| UInt | UInt16 |
| UDInt | UInt32 |
| USInt | Byte |
| Word | UInt16 |

##### Configuring an OPC UA Publisher with local Security Key Service

As a precondition, you must have an existing STEP 7 project or create a new STEP 7 project in which S7 connections to a PC station with OPC UA server V19 or higher have been configured. In addition, a data block created with the supported data types is required, see section "[Supported data types for OPC UA PubSub communication](#supported-data-types-for-opc-ua-pubsub-communication)".

To publish data via the PC station, follow these steps:

1. Open the STEP 7 project.
2. Open the "Device configuration" for the OPC UA server, and select the "All" option for "OPC symbols" for the S7 connection, or the "Configured" option if only a subset of the OPC symbols will be used.
3. Navigate in the project tree to the PC station via which the data will be published, "PC station > OPC server > OPC UA PubSub", to open the editor.
4. For the S7 / S7OPT OPC UA server, click "Published data sets > Add data set" and select the newly created data set.
5. Click the button with the three dots in the "Tag" column. In the dialog box that opens, navigate to the data block you created previously.
6. Select the tags from the data block that will be published using this data set.
7. In "Configure local SKS", click "Add new SecurityGroup".
8. Select the newly created SecurityGroup and navigate in its properties to "Settings for role rights" and import the ApplicationURI for each Subscriber using the "Import ApplicationURI from certificate" button.
9. Click "Connections > Add new connection" to create a new connection.
10. Select the newly created connection and navigate in its properties to "General > Port". The ports for Publisher and Subscriber must be identical.
11. Go to "General > Advanced > Network interface" and enter the network address of the PC station via which the data will be published in the input box.
12. Click "WriterGroups > Add new WriterGroup" for the newly created connection.
13. Select "WriterGroup > Default SecurityKeyService" to make the security settings.
14. For "Endpoint description", click "Add new" and assign the certificate with the ApplicationURI of the Security Key Service for "Server > Application URI" using the "Select" button. Alternatively, you can also enter the ApplicationURI directly or paste a copied ApplicationURI.
15. For "Discovery URL", click "Add new". There, specify the IP address and the port of the OPC UA server that was configured as the Security Key Service server.
16. Select the WriterGroup and navigate in its properties to "General > Security".
17. Assign the value "Sign and encrypt" (default setting) from the "Security profile" drop-down list and enter the ID of the security group for "Security Group ID". You obtain this ID from the properties of the default SecurityKeyService.
18. For the newly created WriterGroup, click "Add new DataSetWriter" and select the newly created DataSetWriter. Navigate in the properties of the DataSetWriter to "General > PublishedDataSet" and select the data set to be published from the drop-down list.
19. Compile the STEP 7 project and download it to the devices.

##### Configuring an OPC UA Subscriber

As a precondition, you must have an existing STEP 7 project or create a new STEP 7 project in which S7 connections to a PC station with OPC UA server V19 or higher have been configured. In addition, a data block created with the supported data types is required, see section "[Supported data types for OPC UA PubSub communication](#supported-data-types-for-opc-ua-pubsub-communication)".

To subscribe to data via the PC station, follow these steps:

1. Open the STEP 7 project.
2. Open the "Device configuration" for the OPC UA server, and select the "All" option for "OPC symbols" for the S7 connection, or the "Configured" option if only a subset of the OPC symbols will be used.
3. Navigate in the project tree to the PC station via which the data will be subscribed, "PC station > OPC server > OPC UA PubSub", to open the editor.
4. Click "Connections > Add new connection" to create a new connection.
5. Select the newly created connection and navigate in its properties to "General > Port". The ports for Publisher and Subscriber must be identical.
6. Go to "General > Advanced > Network interface" and enter the network address of the PC station via which the data will be subscribed in the input box.
7. Click "ReaderGroups > Add new ReaderGroup" for the newly created connection.
8. For the newly created ReaderGroup, click "Add new DataSetReader" and select the newly created DataSetReader.
9. Import the DataSetWriter of the Publisher from the current STEP 7 project using the "Import from project" button. Alternatively, you can also import from a file or from devices accessible online.
10. Click the button with the three dots in the "Tag" column. In the dialog box that opens, navigate to the tag to which the selected subscribed data will be written and confirm this with the green check mark.
11. Compile the STEP 7 project and download it to the devices.

##### Configuring the local SKS

Requirement: A PC station with OPC UA server V19 or higher is configured in your STEP 7 project.

To configure the local SKS via a PC station, follow these steps:

1. Open the STEP 7 project.
2. Navigate in the project tree to the local PC station, "PC station > OPC server > OPC UA PubSub", to open the editor.
3. For "Configure local SKS", click "Add new ".
4. Select the newly created security group, navigate in its properties to "Settings for role rights" and import the application URI for each Subscriber using the "Import application URI from certificate" button.
5. Compile the STEP 7 project and download it to the devices.

##### Content Masks

The tables describe the contents of the masks that are displayed in the parameter groups of the readers. The explanation corresponds to the original text of the specification.

The individual bits have a fixed setting.

###### NetworkMessageContentMask

Defines the header fields of a network message.

Bit assignment (hex) of the mask: 0x3F

| Parameter | Bit no. | Explanation | Assignment |
| --- | --- | --- | --- |
| PublisherId | 0 | The PublisherId is included in the NetworkMessages. | 1 |
| GroupHeader | 1 | The GroupHeader is included in the NetworkMessages. | 1 |
| WriterGroupId | 2 | The WriterGroupId field is included in the GroupHeader. The flag is only valid if Bit 1 is set. | 1 |
| GroupVersion | 3 | The GroupVersion field is included in the GroupHeader. The flag is only valid if Bit 1 is set. | 1 |
| NetworkMessage Number | 4 | The NetworkMessageNumber field is included in the GroupHeader. The field is required if more than one NetworkMessage is needed to transfer all DataSets of the group. The flag is only valid if Bit 1 is set. | 1 |
| SequenceNumber | 5 | The SequenceNumber field is included in the GroupHeader. The flag is only valid if Bit 1 is set. | 1 |
| PayloadHeader | 6 | The PayloadHeader is included in the NetworkMessages. | 0 |
| Timestamp | 7 | The sender timestamp is included in the NetworkMessages. | 0 |
| PicoSeconds | 8 | The sender PicoSeconds portion of the timestamp is included in the NetworkMessages. | 0 |
| DataSetClassId | 9 | The DataSetClassId is included in the NetworkMessages. | 0 |
| PromotedFields | 10 | The PromotedFields are included in the NetworkMessages. | 0 |

###### DataSetMessageContentMask

Describes the contents of the DataSetMessage header.

Bit assignment (hex) of the mask: 0x24

| Parameter | Bit no. | Explanation | Assignment |
| --- | --- | --- | --- |
| TimeStamp | 0 | If this flag is set, a timestamp shall be included in the DataSetMessage header. | 0 |
| PicoSeconds | 1 | If this flag is set, a PicoSeconds timestamp field shall be included in the DataSetMessage header. This flag is ignored if the HeaderTimestamp flag is not set. | 0 |
| Status | 2 | If this flag is set, the DataSetMessage status is included in the DataSetMessage header. | 1 |
| MajorVersion | 3 | If this flag is set, the ConfigurationVersion.MajorVersion is included in the DataSetMessage header. | 0 |
| MinorVersion | 4 | If this flag is set, the ConfigurationVersion.MinorVersion is included in the DataSetMessage header. | 0 |
| SequenceNumber | 5 | If this flag is set, the DataSetMessageSequenceNumber is included in the DataSetMessage header. | 1 |

###### DataSetFieldContentMask

Describes how to decode the data elements of a DataSetMessage of the subscribers:

- As RawData
- As Variant
- As DataValue

  With the "DataValue" type, additional information can be supplied with the data elements (bit 0..4).

Bit assignment (hex) of the mask: 0x20

Since the Publisher uses the header "UADP Periodic Fixed" for encoding the DataSetMessages and NetworkMessages, bit 5 (RawData) is set. All fields of the DataSetMessage are interpreted as raw data (structure) and bits 0..4 are ignored.

| Parameter | Bit no. | Explanation | Assignment |
| --- | --- | --- | --- |
| StatusCode | 0 | The DataValue structure field StatusCode is included in the DataSetMessages. If this flag is set, the fields are represented as DataValue. | 0 |
| SourceTimestamp | 1 | The DataValue structure field SourceTimestamp is included in the DataSetMessages. If this flag is set, the fields are represented as DataValue. | 0 |
| ServerTimestamp | 2 | The DataValue structure field ServerTimestamp is included in the DataSetMessages.  If this flag is set, the fields are represented as DataValue. | 0 |
| SourcePicoSeconds | 3 | The DataValue structure field SourcePicoSeconds is included in the DataSetMessages. If this flag is set, the fields are represented as DataValue. This flag is ignored if the SourceTimestamp flag is not set. | 0 |
| ServerPicoSeconds | 4 | The DataValue structure field ServerPicoSeconds is included in the DataSetMessages. If this flag is set, the fields are represented as DataValue. This flag is ignored if the ServerTimestamp flag is not set. | 0 |
| RawData | 5 | If this flag is set, the values of the DataSet are encoded as Structure (RawData) and all other field related flags shall be ignored. The RawData representation is handled like a Structure DataType where the DataSet fields are handled like Structure fields and fields with Structure DataType are handled like nested structures. All restrictions for the encoding of Structure DataTypes also apply to the RawData Field Encoding. Fields shall not have an abstract DataType or shall have a fixed ValueRank. Fields shall have dimensions defined if the DataType is String or ByteString or if it is an array. This includes Structure fields with such fields. The flag shall be ignored and the fields shall be represented as Variant if the fields do not fulfil these requirements. | 1 |

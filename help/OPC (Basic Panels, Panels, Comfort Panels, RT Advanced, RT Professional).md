---
title: "OPC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: OPCWCCPenUS
topics: 70
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# OPC (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [OPC for Runtime Advanced (Panels, Comfort Panels, RT Advanced)](OPC%20for%20Runtime%20Advanced%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#opc-for-runtime-advanced-panels-comfort-panels-rt-advanced)
- [OPC for Runtime Professional (RT Professional)](#opc-for-runtime-professional-rt-professional)

## OPC for Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Configuration (RT Professional)](#configuration-rt-professional)
- [WinCC OPC server (RT Professional)](#wincc-opc-server-rt-professional)
- [WinCC OPC connection (RT Professional)](#wincc-opc-connection-rt-professional)
- [WinCC OPC UA connection (RT Professional)](#wincc-opc-ua-connection-rt-professional)
- [Commissioning OPC (RT Professional)](#commissioning-opc-rt-professional)

### Basics (RT Professional)

This section contains information on the following topics:

- [OPC (RT Professional)](#opc-rt-professional)
- [OPC Specifications (RT Professional)](#opc-specifications-rt-professional)
- [Compatibility (RT Professional)](#compatibility-rt-professional)
- [Licensing (RT Professional)](#licensing-rt-professional)
- [Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)

#### OPC (RT Professional)

OPC refers to standardized multi-vendor software interfaces for data exchange in automation engineering.

The OPC interfaces provide a standardized environment in which devices and applications from various manufacturers can be linked.

OPC is based on the Windows technology COM (Component Object Model) and DCOM (Distributed Component Object Model).

OPC UA (Unified Architecture) is the technology succeeding OPC. OPC UA is platform-independent and can use different reports as a communication medium.

> **Note**
>
> OPC XML DA is no longer supported.

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[OPC Specifications (RT Professional)](#opc-specifications-rt-professional)
  
[Compatibility (RT Professional)](#compatibility-rt-professional)

#### OPC Specifications (RT Professional)

OPC specifies interfaces to gain access to the following objects in WinCC:

- Process values (OPC Data Access 2.05a, 3.0; OPC UA 1.02)
- Logged process values (OPC Historical Data Access 1.20; OPC UA 1.02)
- Historical alarms (OPC Historical Alarms and Events v1.10)*
- Alarms (OPC Alarms and Events 1.10); OPC UA Alarms and Conditions 1.02

For detailed information about the individual OPC specifications, refer to the website of OPC Foundation.

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[OPC Foundation](http://www.opcfoundation.org)

#### Compatibility (RT Professional)

Support of the mentioned specifications is checked regularly by the "Compliance Test Tool" (CTT) of the OPC Foundation. Interoperability with OPC products of other manufacturers is ensured through the participation in "OPC Interoperability Workshops".

The test results submitted are published on the website of the OPC Foundation. The results can be called up from there using the search term "OPC Self-Certified Products".

---

**See also**

[OPC (RT Professional)](#opc-rt-professional)

#### Licensing (RT Professional)

##### Licensing

For the operation of one of the supported WinCC OPC servers, the following license must be installed:

- WinCC Runtime Professional

#### Using OPC in WinCC (RT Professional)

##### Introduction

On a HMI device with "WinCC Runtime Professional" there are server for the following OPC interfaces available:

- OPC Data Access: Access to the data management of WinCC
- OPC Historical Data Access: Access to the WinCC log system
- OPC Alarms&amp;Events: Access to the WinCC alarm system
- OPC Unified Architecture: Access to the WinCC data management, alarm system and log system

In addition, WinCC by default contains an OPC channel that can access corresponding servers with data access support as a client via OPC DA or OPC UA.

> **Note**
>
> OPC XML DA is no longer supported.

##### OPC communication concept of WinCC

The following screen shows the OPC communication concept of WinCC:

![OPC communication concept of WinCC](images/172866137867_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Licensing (RT Professional)](#licensing-rt-professional)
  
[Functionality of the WinCC OPC DA Server (RT Professional)](#functionality-of-the-wincc-opc-da-server-rt-professional)
  
[Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
  
[Functionality of the WinCC OPC A&amp;E server (RT Professional)](#functionality-of-the-wincc-opc-ae-server-rt-professional)
  
[Principle of operation the WinCC OPC UA Server (RT Professional)](#principle-of-operation-the-wincc-opc-ua-server-rt-professional)
  
[Creating a connection to an OPC server (RT Professional)](#creating-a-connection-to-an-opc-server-rt-professional)

### Configuration (RT Professional)

This section contains information on the following topics:

- [Basic settings for OPC (RT Professional)](#basic-settings-for-opc-rt-professional)

#### Basic settings for OPC (RT Professional)

##### Introduction

For the following WinCC OPC servers, you configure the basic settings on the configuration PC for OPC in the HMI device runtime settings:

- OPC HDA
- OPC A&amp;E
- OPC UA

##### Basic settings for OPC

For HMI devices with Runtime Professional, you define the following in the runtime settings:

- OPC settings

  You configure the following in this category:

  - Exception rules for the validation of writing access to log data
  - Security concept of the WinCC OPC UA server
- Alarms

  In this category you configure the mapping of the WinCC alarm system for the alarm behavior of the following WinCC OPC servers:

  - OPC A&amp;E

---

**See also**

[Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)
  
[Configure WinCC OPC A&amp;E server (RT Professional)](#configure-wincc-opc-ae-server-rt-professional)
  
[Configure WinCC OPC UA Server (RT Professional)](#configure-wincc-opc-ua-server-rt-professional)

### WinCC OPC server (RT Professional)

This section contains information on the following topics:

- [Accessibility of WinCC OPC servers (RT Professional)](#accessibility-of-wincc-opc-servers-rt-professional)
- [WinCC OPC DA Server (RT Professional)](#wincc-opc-da-server-rt-professional)
- [WinCC OPC HDA Server (RT Professional)](#wincc-opc-hda-server-rt-professional)
- [WinCC OPC A&amp;E server (RT Professional)](#wincc-opc-ae-server-rt-professional)
- [WinCC OPC UA Server (RT Professional)](#wincc-opc-ua-server-rt-professional)

#### Accessibility of WinCC OPC servers (RT Professional)

Client-specific OPC clients data from the WinCC data management are available for the WinCC OPC servers, for example, process values or alarms.

In order to access a WinCC OPC server, you must activate the related WinCC project on the HMI device.

#### WinCC OPC DA Server (RT Professional)

This section contains information on the following topics:

- [Functionality of the WinCC OPC DA Server (RT Professional)](#functionality-of-the-wincc-opc-da-server-rt-professional)

##### Functionality of the WinCC OPC DA Server (RT Professional)

###### Principle of operation

The WinCC OPC DA server enables any OPC DA client to access process values from the data management of WinCC.

###### Supported specifications

The WinCC OPC A&amp;E Server supports OPC Data Access 2.05a and 3.0.

###### ProgID of the WinCC OPC DA servers

You access the WinCC OPC DA server via the following ProgID: "OPCServer.WinCC_SCADA".

###### Quality codes

The "Quality Code" delivers information on the status and quality of the process values. For more information, refer to the "OPC Data Access 3.0" specification.

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[Accessibility of WinCC OPC servers (RT Professional)](#accessibility-of-wincc-opc-servers-rt-professional)
  
[Licensing (RT Professional)](#licensing-rt-professional)

#### WinCC OPC HDA Server (RT Professional)

This section contains information on the following topics:

- [Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
- [Supported Write-Accesses (RT Professional)](#supported-write-accesses-rt-professional)
- [Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)](#special-features-of-the-opc-hda-server-in-wincc-for-acyclic-logging-rt-professional)
- [Overview of the supported attributes (RT Professional)](#overview-of-the-supported-attributes-rt-professional)
- [Overview of the supported assemblies (RT Professional)](#overview-of-the-supported-assemblies-rt-professional)
- [Overview of the supported interfaces and functions (RT Professional)](#overview-of-the-supported-interfaces-and-functions-rt-professional)
- [Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)

##### Functionality of the WinCC OPC HDA server (RT Professional)

###### Principle of operation

The WinCC OPC HDA server enables any OPC HDA client to access process values from the data management of the WinCC log system.

###### Supported specifications

The WinCC OPC HDA Server supports the OPC Historical Data Access 1.20 specification.

###### ProgID of the WinCC OPC HDA server

You access the WinCC OPC HDA server via the following ProgID: "OPCServerHDA.WinCC_SCADA".

###### Quality codes

The "Quality Code" delivers information on the status and quality of the raw data. For more information, refer to the "OPC Historical Data Access 1.20" specification.

###### Documentation contents

The WinCC OPC HDA Server documentation contains the following information:

- An overview of the data structure
- An overview of supported attributes, aggregates, and functions

For more information about the OPC HDA Server, refer to the "OPC Historical Data Access 1.20" specification.

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[Accessibility of WinCC OPC servers (RT Professional)](#accessibility-of-wincc-opc-servers-rt-professional)
  
[Overview of the supported attributes (RT Professional)](#overview-of-the-supported-attributes-rt-professional)
  
[Overview of the supported assemblies (RT Professional)](#overview-of-the-supported-assemblies-rt-professional)
  
[Overview of the supported interfaces and functions (RT Professional)](#overview-of-the-supported-interfaces-and-functions-rt-professional)
  
[Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)

##### Supported Write-Accesses (RT Professional)

###### Introduction

By default, any OPC HDA client can change process values in a data log. The tag log validates the data and inserts them to their corresponding time stamp.

If you frequently change a lot of process values, you can use the configuration dialog on the conifguration PC to deactivate the validation of the process values during writing to the data log. You speed up the large writing of process values in this way. The OPC HDA client must sort the data themselves chronologically, otherwise the data is not accepted.

> **Note**
>
> **Deactivate writing access**
>
> You can completely deactivate the writing via the WinCC OPC HDA server from log data via the (user-defined) WinCC setup.

###### Write Accesses

An OPC HDA client does not have generally writing access to the following data logs.

- Compressed logs
- Data logs in main memory
- Swapped logs

The following table shows the supported writing accesses for a process value log on the hard disk of a HMI device:

| Action | Writing in process value log allowed? |
| --- | --- |
| Adding process values later | Yes <sup>1)</sup> |
| Adding process values in Runtime | Yes <sup>2)</sup> |
| Inserting future process values | No |
| Replace process values (Replace) | Yes |
| Deleting process values | Yes <sup>1)</sup> |
| 1: If the time period is contained in the circular log. |  |
| 2: The process value is added in the data buffer currently valid for the process value log. |  |

---

**See also**

[Storing Process Values (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#storing-process-values-rt-professional)
  
[Swapping Out Process Values (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#swapping-out-process-values-rt-professional)
  
[Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)](#special-features-of-the-opc-hda-server-in-wincc-for-acyclic-logging-rt-professional)
  
[Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)

##### Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)

###### Introduction

In WinCC. tags are logged cyclically or acyclically. The WinCC OPC HDA Server works differently depending on the logging method for tags:

- For all cyclically logged values, the OPC HDA Server operates in conformity to the HDA specification of the OPC foundation. The OPC aggregates are linearly interpolated.
- Acyclically logged tags are not included in the HDA specification of the OPC Foundation. The OPC aggregates are interpolated incrementally. If a tag value has not changed for a long period of time, no data are available during this time due to the interpolation.

  To obtain valid data in spite of this, take note of the following particularities:

  > **Note**
  >
  > The OPC HDA Server is not OPC-compliant for acyclically logged tags. The OPC Foundation's HDA specification does not cover acyclically logged tags and therefore does not support log servers for acyclically logged tags. The supported aggregates are calculated in conformity to the OPC HDA specification. No non-explicitly called functions are supported.

###### Configuration of acyclically logged tags

When configuring acyclically logged tags, enable the "Log after segment change" option. This enters the most recent valid value in the the new log when a segment changes.

###### Supported aggregates of the WinCC OPC HDA Server for acyclically logged tags

The OPC HDA Server supports the following aggregates:

- OPCHDA_MINIMUM
- OPCHDA_MAXIMUM
- OPCHDA_AVERAGE
- OPCHDA_END
- OPCHDA_INTERPOLATIVE
- OPCHDA_TIMEAVERAGE
- OPCHDA_TOTAL
- OPCHDA_DURATIONGOOD
- OPCHDA_PERCENTGOOD

###### Supported functions of the WinCC OPC HDA Server for acyclically logged tags

- ReadRaw only with "Boundings". To find the last value actually saved in an area where value changes are not logged, always use "Boundings" when executing "ReadRaw" on a tag.
- ReadProcessed
- DeleteRaw
- DeleteAtTime
- Insert
- InsertReplace
- Replace

###### Calculating the aggregates for acyclically logged tags

The calculation of the aggregates is based on an extended data record of raw data. The extended data record contains not only actually stored values, but also virtual data points for calculation. The WinCC OPC HDA Server prepares the raw data received according to the requirements of "ReadProcessed". The virtual data points needed for the calculation are formed from the bordering real data points. The following significant points are generated for virtual data points:

- Value for "StartTime"
- Value for "EndTime"
- Value for interval limits

###### Example

The values for "00:59:00", "01:02:00" and "01:03:00" are stored for an acyclical logging tag. An OPC HDA Client uses "ReadProcessed" to request an aggregate with the following parameters:

- StartTime = 01:00:00
- EndTime = 01:04:00
- Interval = 00:02:00

  > **Note**
  >
  > When generating virtual values at limits ("EndTime"/"Interval"), the time frame used for the calculation is always 1 µs less than the time stamp at the limit.

For the sake of clarity, a delta of 1 second is used in the following table. The OPC server uses the following raw data to calculate the aggregate:

| Number | Time stamp | Real stored values | Generated virtual values |
| --- | --- | --- | --- |
| 1 | 00:59:00 | 1.00 |  |
| 2 | 01:00:00 |  | 1.00 |
| 3 | 01:01:59 |  | 1.00 |
| 4 | 01:02:00 | 2.00 |  |
| 5 | 01:02:59 |  | 2.00 |
| 6 | 01:03:00 | 3.00 |  |
| 7 | 01:03:59 |  | 3.00 |

The following figure elucidates the example:

![Example](images/22177545739_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ![Example](images/22183595403_DV_resource.Stream@PNG-de-DE.png) | Real values |
| ![Example](images/22183646219_DV_resource.Stream@PNG-de-DE.png) | Virtual values |
| ① | Interval start |
| ② | Interval end |
| ③ | Value change |

---

**See also**

[Supported Write-Accesses (RT Professional)](#supported-write-accesses-rt-professional)
  
[Overview of the supported attributes (RT Professional)](#overview-of-the-supported-attributes-rt-professional)
  
[Overview of the supported assemblies (RT Professional)](#overview-of-the-supported-assemblies-rt-professional)
  
[Overview of the supported interfaces and functions (RT Professional)](#overview-of-the-supported-interfaces-and-functions-rt-professional)

##### Overview of the supported attributes (RT Professional)

The following table contains the attributes supported by the WinCC OPC HDA Server. For more information, refer to the "OPC Historical Data Access 1.20" specification.

###### Attributes

| Attribute | Attribute ID | Description |
| --- | --- | --- |
| ItemID | OPCHDA_ITEMID | Indicates the WinCC logging tag to be accessed. |
| Item Datatype | OPCHDA_DATA_TYPE | Indicates the data type of the WinCC logging tag. |
| Description | OPCHDA_DESCRIPTION | Returns a description of the WinCC logging tag. You define the description in the "HMI Tags" editor. |
| Engineering Units | OPCHDA_ENG_UNITS | Sets the display of measurement units. You define the display in the "HMI Tags" editor. |

---

**See also**

[Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
  
[Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)](#special-features-of-the-opc-hda-server-in-wincc-for-acyclic-logging-rt-professional)

##### Overview of the supported assemblies (RT Professional)

The following table lists the aggregates supported by the WinCC OPC HDA Server. For more information, refer to the "OPC Historical Data Access 1.20" specification.

###### Assemblies

| Assembly | Description |
| --- | --- |
| OPCHDA_COUNT | Detects the raw data count for the specified time interval. |
| OPCHDA_START | Detects the initial value of the raw data at the beginning of the start time interval. |
| OPCHDA_END | Detects the end value of the raw data at the end time interval. |
| OPCHDA_AVERAGE | Detects the raw data mean value for the specified time interval. |
| OPCHDA_TIMEAVERAGE | Detects the time-weighted raw data mean value for the specified time interval. |
| OPCHDA_TOTAL | Returns the sum total value for the specified time interval. |
| OPCHDA_STDEV | Detects the raw data standard deviation for the specified time interval. |
| OPCHDA_MINIMUMACTUALTIME | Returns the minimum value of the raw data time stamp for the specified time interval. |
| OPCHDA_MINIMUM | Detects the raw data minimum value for the specified time interval. |
| OPCHDA_MAXIMUMACTUALTIME | Detects the maximum value and the raw data time stamp for the specified time interval. |
| OPCHDA_MAXIMUM | Detects the raw data maximum value for the specified time interval. |
| OPCHDA_DELTA | Detects the difference between the first and the last value of the raw data for the specified time interval. |
| OPCHDA_REGSLOPE | Detects the slope of the regression line of the raw data for the specified time interval. |
| OPCHDA_REGCONST | Detects the regression line value of the raw data at the starting point. |
| OPCHDA_REGDEV | Detects the slope of the regression line of the raw data for the specified time interval. |
| OPCHDA_VARIANCE | Detects the raw data variance for the specified time interval. |
| OPCHDA_RANGE | Detects the difference between OPCHDA_MAXIMUM and OPCHDA_MINIMUM of the raw data for the specified time interval. |
| OPCHDA_DURATIONGOOD | Detects the period of time in which the quality of the raw data was good. The period is indicated in seconds. |
| OPCHDA_DURATIONBAD | Detects the period of time in which the quality of the raw data was bad. The period is indicated in seconds. |
| OPCHDA_PERCENTGOOD | Detects the percentage of the raw data of good quality. |
| OPCHDA_PERCENTBAD | Detects the percentage of the raw data of bad quality. |
| OPCHDA_WORSTQUALITY | Detects the raw data worst quality for the specified time interval. |

---

**See also**

[Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
  
[Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)](#special-features-of-the-opc-hda-server-in-wincc-for-acyclic-logging-rt-professional)

##### Overview of the supported interfaces and functions (RT Professional)

The WinCC OPC HDA Server supports the following interfaces:

- IOPCHDA_Server
- IOPCHDA_SyncRead (no "ReadModified" method)
- IOPCHDA_SyncUpdate
- IOPCHDA_AsyncRead (no "ReadModified" method)
- IOPCHDA_AsyncUpdate
- IOPCCommon

For more information about the interfaces, refer to the "OPC Historical Data Access 1.20" specification.

---

**See also**

[Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
  
[Special features of the OPC HDA server in WinCC for acyclic logging (RT Professional)](#special-features-of-the-opc-hda-server-in-wincc-for-acyclic-logging-rt-professional)

##### Configure WinCC OPC HDA Server (RT Professional)

###### Introduction

On the configuration PC, define in the configuration settings for the WinCC OPC HDA server whether specific users or OPC HDA clients may change process values in the data logs without validation.

> **Note**
>
> The configuration settings apply for the WinCC OPC HDA server as well as for the OPC UA server.

> **Note**
>
> **Deactivated writing access**
>
> If the writing access of OPC HDA clients was deactivated on the data logs in (user-defined) WinCC setup, these settings are ignored.

###### Procedure

To configure WinCC OPC HDA server, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Define under "OPC settings" which users or OPC clients may change process values in the data logs without validation:

   - To fully disable validation, select "Disable validation of the data during write access for selected OPC clients".
   - To deactivate the validation for single users or OPC clients, double-click "Insert" in the corresponding table. Enter the name of the user or the OPC client.
   - To re-select the validation for a single user or OPC client, clear the option in front of the respective user or OPC client.

---

**See also**

[Functionality of the WinCC OPC HDA server (RT Professional)](#functionality-of-the-wincc-opc-hda-server-rt-professional)
  
[Basic settings for OPC (RT Professional)](#basic-settings-for-opc-rt-professional)

#### WinCC OPC A&E server (RT Professional)

This section contains information on the following topics:

- [Functionality of the WinCC OPC A&amp;E server (RT Professional)](#functionality-of-the-wincc-opc-ae-server-rt-professional)
- [OPC A&amp;E Server mapping rules (RT Professional)](#opc-ae-server-mapping-rules-rt-professional)
- [Configure WinCC OPC A&amp;E server (RT Professional)](#configure-wincc-opc-ae-server-rt-professional)
- [Accessing logged alarms (RT Professional)](#accessing-logged-alarms-rt-professional)

##### Functionality of the WinCC OPC A&E server (RT Professional)

###### Principle of operation

The WinCC OPC A&amp;E server enables the access to alarms of the WinCC alarm system. The OPC A&amp;E Client is kept informed of status changes for WinCC alarms via Subscriptions. To avoid displaying all alarms and attributes on the OPC A&amp;E client, configure in the Subscription filter.

###### Supported specifications

OPC Alarm &amp; Events is a specification for the transmission of alarms and events. The WinCC OPC A&amp;E Server supports the OPC Alarms&amp;Events 1.10 specification.

In addition, the WinCC OPC A&amp;E Server supports access to historical alarms in accordance with the Siemens draft "OPC Historical Alarms and Events v1.10".

###### ProgID of the WinCC OPC A&amp;E server

You access the WinCC OPC A&amp;E server via the following ProgID: "OPCServerAE.WinCC_SCADA".

###### Quality codes

The "Quality Code" delivers information on the status and quality of an alarm. For more information, refer to the "OPC Alarms&amp;Events 1.10" specification.

###### OPC A&amp;E Server mapping rules

To map the WinCC alarm system on OPC Alarms&amp;Events, the WinCC OPC A&amp;E server supports three mapping rules "Mode 1" to "Mode 3".

"Mode 1" and "Mode 2" are supported because of compatibility reasons to WinCC OPC A&amp;E server version 3.52 and earlier. "Mode 1" and "Mode 2" do not have a restricted scope of operation.

"Mode 3" widens the restricted scope of operation of "Mode 1" and "Mode 2".

###### Documentation contents

The WinCC OPC A&amp;E Server documentation contains the following information:

- A mapping of the alarm system on OPC A&amp;E
- An overview of supported attributes

For more information, refer to the "OPC Alarm&amp;Events 1.10" specification.

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[Accessibility of WinCC OPC servers (RT Professional)](#accessibility-of-wincc-opc-servers-rt-professional)
  
[OPC A&amp;E Server mapping rules (RT Professional)](#opc-ae-server-mapping-rules-rt-professional-1)
  
[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)
  
[Restrictions for Mode 1 and Mode 2 (RT Professional)](#restrictions-for-mode-1-and-mode-2-rt-professional)
  
[Access to logged events (RT Professional)](#access-to-logged-events-rt-professional)

##### OPC A&E Server mapping rules (RT Professional)

This section contains information on the following topics:

- [General rules (RT Professional)](#general-rules-rt-professional)
- [Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
- [Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
- [Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)
- [Restrictions for Mode 1 and Mode 2 (RT Professional)](#restrictions-for-mode-1-and-mode-2-rt-professional)
- [Alarm classes and alarm methods (RT Professional)](#alarm-classes-and-alarm-methods-rt-professional)
- [Priorities (RT Professional)](#priorities-rt-professional)

###### General rules (RT Professional)

This section contains information on the following topics:

- [OPC A&amp;E Server mapping rules (RT Professional)](#opc-ae-server-mapping-rules-rt-professional-1)
- [OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)
- [State machine (RT Professional)](#state-machine-rt-professional)
- [Quality Codes for OPC A&amp;E (RT Professional)](#quality-codes-for-opc-ae-rt-professional)
- [Attributes (RT Professional)](#attributes-rt-professional)

###### OPC A&E Server mapping rules (RT Professional)

During the configuration of the WinCC message system, settings are made to determine which process events generate a message. This message is shown as an alarm in OPC A&amp;E.

The following table shows the most important parameters of the alarm and how the WinCC alarm system prepares the information:

| OPC | WinCC message system | Type of event |
| --- | --- | --- |
| Source | Source where the alarm was issued. The source has the format "&lt;server prefix&gt;::@LOCALMACHINE::". | S, C |
| Time | Time of the event. Issues a time stamp in UTC (Universal Time Coordinated). | S, C |
| EventType | Type of event. The WinCC OPC A&amp;E Server supports "Simple Events" and "Condition Related Events". | S, C |
| Severity | Priority of the alarm from WinCC | S, C |
| EventCategory | Category of the alarms. For more information on this topic, refer to "Displaying Message Classes and Types". | S, C |
| Message | Alarm text for the corresponding alarm number. | S, C |
| ConditionName | Specified text that is delivered to the alarm additionally. Which text is returned, depends on the configured display rules:  - "Mode 1" and "Mode 2": Alarm number. - "Mode 3": Alarm method, for example "Analog alarm". | C |
| SubConditionName | Corresponds "ConditionName", because WinCC supports no Multi-State Conditions. | C |
| ChangeMask | Changed status of the alarm. You can find additional information under "State machine". | C |
| NewState | Status of the alarm. You can find additional information under "State machine". | C |
| ConditionQuality | Returns the quality of the message. For more information, refer to "Quality Codes". | C |
| AckRequired | Indicates whether the message requires acknowledgment. | C |
| ActiveTime | Returns the time stamp for received messages. | C |
| EventAttribute | Lists the attributes required for the respective message. For more information, refer to "Attributes of the WinCC Message System". | C |
| Quality | Returns the quality code of the message. | C |
| Cookie | Returns the cookie from the OPC A&amp;E Server. | C |
| ActorID | Returns the logged user. | C |
| S = "Simple Event"  C = "Condition Related Event" |  |  |

---

**See also**

[State machine (RT Professional)](#state-machine-rt-professional)
  
[Quality Codes for OPC A&amp;E (RT Professional)](#quality-codes-for-opc-ae-rt-professional)
  
[Attributes (RT Professional)](#attributes-rt-professional)
  
[Priorities (RT Professional)](#priorities-rt-professional)
  
[Alarm classes and alarm methods (RT Professional)](#alarm-classes-and-alarm-methods-rt-professional)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)

###### OPC A&E types of event  (RT Professional)

###### Introduction

The WinCC OPC A&amp;E Server supports "Condition Related Events" and "Simple Events".

###### Condition Related Events

"Condition Related Events" are alarms triggered by a condition. such as the limit violation of a tag, which is then output as an alarm on the HMI device. A "Condition Related Event"contains additionally the "Alarm" attribute.

By default, each alarm as "Condition Related Event" is sent to the OPC A&amp;A client.

###### Simple Events

As "Simple Events" all other alarms are treated, which cannot be assigned to the "Condition Related Event" type of event.

In order for an alarm to be treated as a "Simple Event", the following prerequisites must be met when the alarm class is configured:

- "Acknowledgment Came In" is not activated.
- "Alarm without outgoing state" is activated.

  > **Note**
  >
  > Note the following while using redundant systems:
  >
  > "Simple Events" that are connected to internal tags are sent twice during tag comparison.
  >
  > The first alarm is triggered by master, the second by the standby server.

---

**See also**

[State machine (RT Professional)](#state-machine-rt-professional)
  
[OPC A&amp;E Server mapping rules (RT Professional)](#opc-ae-server-mapping-rules-rt-professional-1)
  
[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)

###### State machine (RT Professional)

###### Introduction

For WinCC, the state machine is how an alarm is displayed and processed from "incoming" to "outgoing". On the WinCC OPC A&amp;E Server, this alarm status is managed in the "ChangeMask" and "NewState" parameters.

###### ChangeMask

The "ChangeMask" parameter keeps track of where the alarm status changed. Possible parameter values are:

- OPC_CHANGE_ACTIVE_STATE
- OPC_CHANGE_ENABLE_STATE
- OPC_CHANGE_ACK_STATE

###### NewState

The "NewState" parameter indicates the alarm status after a change. Possible parameter values are:

- OPC_CONDITION_ACTIVE
- OPC_CONDITION_ENABLED
- OPC_CONDITION_ACKED

###### Overview

The following table shows how WinCC alarm statuses are mapped to the "NewState" and "ChangeState" OPC parameters:

| WinCC | NewState | ChangeState |
| --- | --- | --- |
| Incoming alarm | OPC_CONDITION_ACTIVE  OPC_CONDITION_ENABLED | OPC_CHANGE_ACTIVE_STATE |
| Outgoing alarm acknowledged | OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACTIVE_STATE |
| Outgoing alarm without acknowledgment | OPC_CONDITION_ENABLED | OPC_CHANGE_ACTIVE_STATE |
| Acknowledged alarms (alarm pending) | OPC_CONDITION_ACTIVE  OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Acknowledged alarms (alarm no longer pending) | OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Locked alarm | - | OPC_CHANGE_ENABLED_STATE |
| Unlocked alarm | OPC_CONDITION_ENABLED | OPC_CHANGE_ENABLED_STATE |
| Incoming, acknowledged alarm | OPC_CONDITION_ACTIVE  OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACTIVE_STATE |
| Incoming, outgoing alarm with acknowledgment | OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Incoming, outgoing alarm without acknowledgment | OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Alarm acknowledged by the system (alarm pending) | OPC_CONDITION_ACTIVE  OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Alarm acknowledged by the system (alarm no longer pending) | OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Emergency-acknowledged alarm (alarm pending) | OPC_CONDITION_ACTIVE  OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |
| Emergency-acknowledged alarm (alarm no longer pending) | OPC_CONDITION_ACKED  OPC_CONDITION_ENABLED | OPC_CHANGE_ACK_STATE |

---

**See also**

[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)

###### Quality Codes for OPC A&E (RT Professional)

The "Quality Code" is required to evaluate the status and quality of an alarm.

###### Quality codes

OPC A&amp;E's quality codes are presented in the following table:

| Code | Quality | Status |
| --- | --- | --- |
| 0xC0 | OPC_GOOD | OK |
| 0x40 | OPC_UNCERTAIN | Discrepancies, resulting from delayed acknowledgment, for example |
| 0x00 | OPC_BAD | Connection to source is interrupted |

###### Attributes (RT Professional)

The following table lists the OPC attributes of the WinCC message system. You can configure the attributes in the "Alarms" editor. Some attributes are intended for internal use in WinCC only and are therefore not relevant to an OPC A&amp;E Client. These attributes are not listed.

| OPC attribute | WinCC message system | Data type |
| --- | --- | --- |
| CLASSNAME | Returns the alarm class name. | VT_BSTR |
| TYPENAME | Returns the alarm method type name. | VT_BSTR |
| FORECOLOR | Returns the text color for received, sent and acknowledged alarms. | VT_I4 |
| BACKCOLOR | Returns the background color for received, sent and acknowledged alarms. | VT_I4 |
| FLASHCOLOR | Returns the flashing color. | VT_I4 |
| FLAGS | Indicates whether the message requires acknowledgment. | VT_I4 |
| TEXT01 | Returns the content of UserTextBlock01. | VT_BSTR |
| TEXT02 | Returns the content of UserTextBlock02. | VT_BSTR |
| TEXT03 | Returns the content of UserTextBlock03. | VT_BSTR |
| TEXT04 | Returns the content of UserTextBlock04. | VT_BSTR |
| TEXT05 | Returns the content of UserTextBlock05. | VT_BSTR |
| TEXT06 | Returns the content of UserTextBlock06. | VT_BSTR |
| TEXT07 | Returns the content of UserTextBlock07. | VT_BSTR |
| TEXT08 | Returns the content of UserTextBlock08 | VT_BSTR |
| TEXT09 | Returns the content of UserTextBlock09 | VT_BSTR |
| TEXT10 | Returns the content of UserTextBlock10 | VT_BSTR |
| PROCESSVALUE01 | Returns the content of ProcessValueBlock01 | VT_VARIANT |
| PROCESSVALUE02 | Returns the content of ProcessValueBlock02 | VT_VARIANT |
| PROCESSVALUE03 | Returns the content of ProcessValueBlock03 | VT_VARIANT |
| PROCESSVALUE04 | Returns the content of ProcessValueBlock04 | VT_VARIANT |
| PROCESSVALUE05 | Returns the content of ProcessValueBlock05 | VT_VARIANT |
| PROCESSVALUE06 | Returns the content of ProcessValueBlock06 | VT_VARIANT |
| PROCESSVALUE07 | Returns the content of ProcessValueBlock07 | VT_VARIANT |
| PROCESSVALUE08 | Returns the content of ProcessValueBlock08 | VT_VARIANT |
| PROCESSVALUE09 | Returns the content of ProcessValueBlock09 | VT_VARIANT |
| PROCESSVALUE10 | Returns the content of ProcessValueBlock10 | VT_VARIANT |
| STATETEXT | Returns the status alarm | VT_BSTR |
| INFOTEXT | Returns the information text for the alarm | VT_BSTR |
| LOOPINALARM | Indicates if loop-in alarm has been configured. | VT_I4 |
| CLASSID | Returns the alarm class ID | VT_I4 |
| TYPEID | Returns the message type ID | VT_I4 |
| MODIFYSTATE | Returns the value of the status tag of the alarm | VT_I4 |
| AGNR | Returns the number of the automation system that generated the alarm | VT_I2 |
| CPUNR | Returns the number of the CPU that generated the alarm | VT_I2 |
| DURATION | Indicates the period of time between alarm received, sent and acknowledged | VT_I4 |
| COUNTER | Returns the number of alarms after the start of Runtime | VT_I4 |
| QUITSTATETEXT | Indicates whether the alarm has been acknowledged | VT_BSTR |
| QUITCOUNT | Returns the number of active, unacknowledged alarms | VT_I4 |
| PARAMETER | Outputs the message parameter. (Image of the message configuration) | VT_BSTR |
| BLOCKINFO | Returns the current content of the alarm block | VT_BSTR |
| ALARMCOUNT | Outputs the number of alarms pending | VT_I4 |
| LOCKCOUNT | Returns the number of locked alarms | VT_I4 |
| PRIORITY | Indicates the configured priority of the alarm | VT_I4 |
| APPLICATION | Returns the application which triggered the alarm | VT_BSTR |
| COMPUTER | Returns the name of the computer which processed the alarm | VT_BSTR |
| USER | Returns the name of the user who processed the alarm | VT_BSTR |
| COMMENT | Returns the alarm comment | VT_BSTR |
| HIDDEN-COUNT* | Number of locked alarms | VT_I4 |
| OS-HIDDEN* | Indicates whether the alarm is locked | VT_BOOL |
| OS_EVENTID* | Indicates the WinCC alarm number | VT_I4 |
| BIG_COUNTER* | Alarm counter | VT_CY |
| UNIQUE EVENT ID* | corresponds to the "BIG_COUNTER" | VT_CY |
| *: Are supported only by "Mode 3". |  |  |

---

**See also**

[Alarm classes and alarm methods (RT Professional)](#alarm-classes-and-alarm-methods-rt-professional)
  
[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)

###### Mapping rule "Mode 1": (RT Professional)

"Mode 1" displays the whole WinCC alarm system under a "OPC Source" with the name "localhost::" The "TEXT01" WinCC attribute is written in the OPC alarm text.

The WinCC alarm number is displayed on the "Condition" of the WinCC OPC A&amp;E server.

"Mode 1" supports the "Simple Events" and "Condition Related Events" types of event. Events can be filtered according to the "Event Type", "Category" and "Severity" criteria.

---

**See also**

[Restrictions for Mode 1 and Mode 2 (RT Professional)](#restrictions-for-mode-1-and-mode-2-rt-professional)
  
[Attributes (RT Professional)](#attributes-rt-professional)
  
[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)
  
[Configure WinCC OPC A&amp;E server (RT Professional)](#configure-wincc-opc-ae-server-rt-professional)
  
[Alarm classes and alarm methods (RT Professional)](#alarm-classes-and-alarm-methods-rt-professional)
  
[Priorities (RT Professional)](#priorities-rt-professional)

###### Mapping rules "Mode 2": (RT Professional)

"Mode 2" is implemented as of version 3.5.2. of the WinCC OPC A&amp;E server. The WinCC alarm number is displayed on the "Condition" of the WinCC OPC A&amp;E server.

The text attribute of the WinCC alarm ("TEXT01" to "TEXT10") you have configured, is written in the OPC alarm text of "OPC Source".

"Mode 2" supports the "Simple Events" and "Condition Related Events" types of event. Events can be filtered according to the "Event Type", "Category" and "Severity" criteria.

---

**See also**

[Restrictions for Mode 1 and Mode 2 (RT Professional)](#restrictions-for-mode-1-and-mode-2-rt-professional)
  
[Attributes (RT Professional)](#attributes-rt-professional)
  
[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)
  
[Configure WinCC OPC A&amp;E server (RT Professional)](#configure-wincc-opc-ae-server-rt-professional)
  
[Alarm classes and alarm methods (RT Professional)](#alarm-classes-and-alarm-methods-rt-professional)
  
[Priorities (RT Professional)](#priorities-rt-professional)

###### Mapping rules "Mode 3": (RT Professional)

"Mode 3" is implemented as of version 3.6 of the WinCC OPC A&amp;E server. "Mode 3" supports the hierarchical mapping of user-defined alarms. The hierarchy of "OPC Areas" is set by the user-defined alarm groups.

With "Mode 3" you query the address space of the WinCC OPC A&amp;E server according to "Areas" and "Sources".

"Mode 3" supports the "Simple Events" and "Condition Related Events" types of event. Events can be additionally filtered according to the "Area" and "Source" criteria. "Mode 3" supports the "System Message" OPC category.

---

**See also**

[Attributes (RT Professional)](#attributes-rt-professional)
  
[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)
  
[Configure WinCC OPC A&amp;E server (RT Professional)](#configure-wincc-opc-ae-server-rt-professional)
  
[Priorities (RT Professional)](#priorities-rt-professional)

###### Restrictions for Mode 1 and Mode 2 (RT Professional)

###### Notes on mapping rules "Mode 1" and "Mode 2":

The mapping rules for "Mode 1" and "Mode 2" contain significant restrictions. The mapping rules for "Mode 1" and "Mode 2" are therefore only because of compatibility reasons supported by the previous version and are not developed further.

> **Note**
>
> In order to ensure compatibility with the previous version, the WinCC OPC A&amp;E server cannot use multiplexer.

The restrictions are solved in the mapping rule "Mode 3".

Some of the restrictions of the mapping rules "Mode 1" and "Mode 2" are listed below:

- The WinCC alarm attributes are passed on via the OPC interface.

  The IDs value range of WinCC alarm attributes is defined by the OPC specification by "Property sets":

  - ID Set 1 contains the "OPC-specific Properties". Range: 1 … 99
  - ID Set 2 contains the "Recommended Properties". Value range 100 to 199
  - IDs 300…399 are especially reserved for OPC A&amp;E
  - IDs 400 to 4999 are reserved by OPC.
  - ID Set 3 contains the "Vendor-specific Properties". Range: 5000 and higher

    The IDs of the WinCC attributes must have values from 5000 and higher.

  Mode 1 and Mode 2 pass on the IDs of the WinCC alarm attributes via the OPC interface. These IDs are in the range of 0 to 61.

  If an OPC client, for example, requires the attribute with the IDs 2 ("Item Value") and 3 ("Item Quality") from the WinCC OPC A&amp;E server, the OPC client receives instead the corresponding WinCC alarm atrocities. In this case the attributes are "ForeColor" and "BackColor".
- Restrictions for transfer of WinCC alarm numbers

  Alarm numbers are only transferred as text in the "Condition" when "Condition Related Events". When "Simple Events", the alarm numbers are completely lost.
- Some WinCC attributes are not supported, for example "UNIQUE_EVENT_ID"

  You can use the "UNIQUE_EVENT_ID" attribute for alarm synchronization of redundant server couples. During switching between redundant servers, the following could happen:

  - Alarms can be double- transferred
  - Alarms can be lost

You can find an overview of all attributes supported by the different modes at "[Attributes](#attributes-rt-professional)".

---

**See also**

[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Attributes (RT Professional)](#attributes-rt-professional)

###### Alarm classes and alarm methods (RT Professional)

###### Introduction

The WinCC message system informs the user of disturbances and operating conditions in the process. A WinCC alarm always belongs to a specific alarm class and alarm method that is related to the "Event Category".

###### Event Category

> **Note**
>
> **"Event Category" depends on the set mapping rules**
>
> The characteristics of the mapping rules "Mode 1" and "Mode 2" are described below:

An "Event Category" is displayed on the WinCC OPC A&amp;E Server for every combination of an alarm class and alarm method.

An "Event Category" is determined by a "CategoryID" and a descriptive "Category Description". The "CategoryID" consists of the WinCC-internal ID of an alarm class and alarm method. The "Category Description" comes from the names of the alarm class and alarm method.

The names of the alarm classes and alarm methods can be ascertained explicitly via the alarm attributes "CLASSNAME" and "TYPENAME".

---

**See also**

[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)

###### Priorities (RT Professional)

###### Introduction

The priority of WinCC alarms is displayed by the WinCC OPC A&amp;E server on the "Severity" attribute.

You can configure up to 17 priority levels in WinCC. The "Severity" OPC attribute has a value range from "1" to "1000":

- 1: Lowest priority
- 1000: Highest priority

Depending on the number of the configured WinCC priority levels, the value in the "Severity" attribute is automatically retrieved by linear scaling.

Exception: For the mapping rules "Mode 1", the priority levels configured in WinCC are displayed directly on the "Severity" attribute.

###### Example

If you do not change the default settings in the configuration settings of the WinCC OPC A&amp;E server, the 17 priority levels are going to be displayed in the WinCC OPC A&amp;E server as follows:

| Priority level in WinCC | Assigned value in the "Severity" attribute |
| --- | --- |
| 0 | 1 |
| 1 | 64 |
| 2 | 127 |
| 3 | 190 |
| ... | ... |
| 15 | 937 |
| 16 | 1000 |

---

**See also**

[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)
  
[Description of the System Blocks (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#description-of-the-system-blocks-rt-professional)

##### Configure WinCC OPC A&E server (RT Professional)

###### Introduction

Define the display of the WinCC alarm system in the configuration settings of the WinCC OPC A&amp;E server.

The following screen shows the configuration settings in the "Runtime settings" of the HMI device:

![Introduction](images/88818845067_DV_resource.Stream@PNG-en-US.png)

###### Requirement

Alarms are configured.

###### Procedure

To configure WinCC OPC A&amp;E server, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Configure the server settings at "Alarms &gt; OPC Alarms &amp; Events":

   - Define the low and high limit for the display of the priority range.
   - To activate the WinCC alarms with the mapping rule "Mode 3" in the WinCC OPC A&amp;E, activate "Activated" and "OPC areas".

     Use primarily this setting.
   - Assign to the "OPC event source" and the "OPC event alarm" respectively an alarm quality, for example, " User text block 3".

###### Result

The WinCC alarms are displayed completely in the WinCC OPC A&amp;E. If you have configured user-defined alarms, areas and sources of the user-defined alarms are displayed in the WinCC OPC A&amp;E server.

###### Alternative procedure

You can display alternatively because of compatibility reasons the WinCC alarm also according to the "Mode 2" and "Mode 1" mapping rules in the WinCC OPC A&amp;E server:

1. To display the WinCC alarms with the mapping rule "Mode 2" in the WinCC OPC A&amp;E server, activate "Activated" and deactivate"OPC areas".
2. To display the WinCC alarms with the mapping rule "Mode 1" in the WinCC OPC A&amp;E server, deactivate "Activated" and "OPC areas".

---

**See also**

[OPC A&amp;E types of event (RT Professional)](#opc-ae-types-of-event-rt-professional)
  
[Priorities (RT Professional)](#priorities-rt-professional)
  
[Basic settings for OPC (RT Professional)](#basic-settings-for-opc-rt-professional)
  
[Mapping rule "Mode 1": (RT Professional)](#mapping-rule-mode-1-rt-professional)
  
[Mapping rules "Mode 2": (RT Professional)](#mapping-rules-mode-2-rt-professional)
  
[Mapping rules "Mode 3": (RT Professional)](#mapping-rules-mode-3-rt-professional)

##### Accessing logged alarms (RT Professional)

This section contains information on the following topics:

- [Access to logged events (RT Professional)](#access-to-logged-events-rt-professional)
- [Syntax for accessing logged alarms using OPC (RT Professional)](#syntax-for-accessing-logged-alarms-using-opc-rt-professional)
- [Read methods for logged alarms (RT Professional)](#read-methods-for-logged-alarms-rt-professional)
- [Identifying logged alarms (RT Professional)](#identifying-logged-alarms-rt-professional)

###### Access to logged events (RT Professional)

###### Introduction

You can access the archived messages via the OPC A&amp;E Server using an OPC client. Two methods are supported for accessing logged alarms:

- Output archived messages from a time period in the past
- Output archived messages from a time period in the past without mentioning end of period. After the output of archived messages, all other newly generated messages are automatically sent to the OPC client.

  > **Note**
  >
  > After reading tagged logs, you are not allowed to use the returned "ActiveTime" of an alarm to acknowledge the alarm or to track any transitions in the alarm. To ensure this does not happen, the OPC A&amp;E Client must check the "EventType" of an alarm for the extra flag "OPC_HAE_HISTORICAL_EVENTFLAG". The "ActiveTime" is not correct on logged alarms. You can find information on the additional flag under "Identifying archived messages".

###### Polling the "Historic alarms and events" functionality

The table below lists the filters offered by the WinCC's extended OPC A&amp;E Server, in addition to the standard filters:

| Filter | Filter Values | Description |
| --- | --- | --- |
| OPC_HAE_FILTER_BY_TIMEFRAME | 0x80000000 | Corresponds to the "ReadRaw" function for OPC Historical Data Access |
| OPC_HAE_FILTER_BY_STARTTIME | 0x40000000 | Corresponds to the "AdviseRaw" function for OPC Historical Data Access |

###### Source filter and historical alarm request

In order for you to be able to request logged alarms, the OPC client must support the "SetFilter" functionality on a Subscription. The OPC server will also send logged alarms if you insert the keyword "OPCHAEServer" into the array of the "Source Filter" in a Subscription. In addition to this keyword, you can use other parameters to define which messages are to be read:

- Method
- Time period
- With or without limits

The lists of sources that are assigned in the filter can include other source names besides the "OPCHAEServer" source. In this a case, the Subscription delivers only the logged events of the given sources. The sequence of the source names is inconsequential.

After configuring the source filter, you can retrieve the selected time period from the client with a "Refresh" call.

---

**See also**

[Identifying logged alarms (RT Professional)](#identifying-logged-alarms-rt-professional)
  
[Syntax for accessing logged alarms using OPC (RT Professional)](#syntax-for-accessing-logged-alarms-using-opc-rt-professional)
  
[Read methods for logged alarms (RT Professional)](#read-methods-for-logged-alarms-rt-professional)

###### Syntax for accessing logged alarms using OPC (RT Professional)

###### Syntax

`OPCHAEServer hMode=(read`|`advise) htStartTime=szTime [hEndTime=szTime] [bBounds=(TRUE`|`FALSE)]`

###### Parameter

**hMode = [read|advise]**

Required Defines how the archived messages and events are to be read.

- Read

  Outputs logged alarms and events of a defined period from the past (comparable to ReadRaw for OPC Historical Data Access).

  The following example shows how a filter is set to read over the past 30 minutes:

  `OPCHAEServer hMode=read htStartTime=NOW-30M bBounds=TRUE`
- Advise

  Outputs archived messages and events from a definite period, When all logged alarms are received, new alarms are sent in the same way as for an active subscription (comparable to AdviseRaw for OPC Historical Data Accesss).

  The following example shows how alarms are read from 30 minutes ago until now (subscription must be active):

  `OPCHAEServer hMode=advise htStartTime=NOW-30M`

  > **Note**
  >
  > The following notation is supported for the parameters "htStartTime" and "htEndTime":
  >
  > - Relative notations such as "NOW"
  > - Symbolic values such as "NOW", "YEAR", "MONTH"
  > - Specification of absolute UTC data/time values according to XML notation: 2006-09-01T10:00:00.000Z
  >
  > The use of symbolic notation corresponds to the syntax of OPC Historical Data Access.

**htStartTime =**

Required Defines the time from when the messages and events are to be read from the archive.

**htEndTime =**

Optional Defines the time up to which the messages and events are to be read from the archive. For "`hMode = read`", the default setting "NOW" is used.

**bBounds = [TRUE|FALSE]**

Optional Defines how messages close to the start and end time are to be handled. The function is identical to OPC historical data access.

- `bBounds=FALSE:`

  - Time stamp of the first transferred alarm &gt;= htStartTime
  - Time stamp of the last transferred alarm &lt; htEndTime
- `bBounds=TRUE:`

  - Time stamp of the first transferred alarm &lt;= htStartTime
  - Time stamp of the last transferred alarm &gt;= htEndTime

The default setting is FALSE.

---

**See also**

[Read methods for logged alarms (RT Professional)](#read-methods-for-logged-alarms-rt-professional)
  
[Identifying logged alarms (RT Professional)](#identifying-logged-alarms-rt-professional)

###### Read methods for logged alarms (RT Professional)

###### Introduction

You can use one of the two read modes to read archived messages:

- read
- advise

###### "read" mode

"read" mode is used to read logged alarms from a defined period in the past. The sequence of read messages is always read from the alarms in chronological sequence in reference to each OS server. By setting the start and end time, you can specify whether the last message is to be read first or last. If the start time is earlier than the end time, the last message is last in the output.

If you want to use "read" mode, run the following functions on the subscription:

1. SetFilter
2. Refresh

A "SetFilter" during the "Refresh" will be rejected. Activating the subscription during "Refresh" does not affect how the Refresh is carried out.

The historic events will continue to be transferred with the Refresh flag.

The newly generated events are transferred according to the standard reaction of an active subscription:

- Taking into account the set filter values with the exception of "historic" source "OPCHAEServer"
- Without the Refresh flag

Enables the client to distinguish between the received events based on the Refresh flag. An event package never contains historic and new events at the same time.

- Event packets with the Refresh flag contain only historic events. These events can also be in queue.
- Event packets without the Refresh flag contain only newly generated events.

###### "advise" mode

"advise" mode is used to read logged alarms starting from a defined period in the past. After reading all archived messages, new messages are sent in the same way as for an active subscription. The archived messages are transferred in chronological sequence in reference to each OS server: The archived messages from a start time onwards are transmitted. Thereafter, the newly archived messages transferred.

Note that you are not permitted to define an end time for "advise".

An active subscription is used for "advise" mode. If you run the "SetFilter" function on an active subscription, the historical alarms are transferred immediately.

If you run the "SetFilter" function on an inactive subscription, the logged alarms are sent only after the subscription is activated. If you want to use "advise" mode with an inactive subscription, follow these steps:

1. SetFilter.
2. Set the subscription to "Active" using "SetState".

The transmission is interrupted if you deactivate the subscription.

The transmission is ended if you set the subscription to "inactive". A "SetFilter" is rejected when the subscription is active.

A "Refresh" on an active "historic" subscription in "advise" mode functions in the same way as it does for a standard subscription:

All queued condition related events are transferred to packages with Refresh flag. The last packet also contains an additional "Last Refresh" flag.

A "Refresh" call has no influence on the reading of historical alarms in "advise" mode.

---

**See also**

[Syntax for accessing logged alarms using OPC (RT Professional)](#syntax-for-accessing-logged-alarms-using-opc-rt-professional)

###### Identifying logged alarms (RT Professional)

###### Principle

Logged alarms are distinguished using an additional flag in EventType. This flag is ORed with the real EventType.

| Name | EventType | EventType (archived message) |
| --- | --- | --- |
| OPC_SIMPLE_EVENT | 0x01 | 0x81 |
| OPC_CONDITION_EVENT | 0x04 | 0x84 |
| OPC_TRACKING_EVENT | 0x02 | 0x82 |
| OPC_HAE_HISTORICAL_EVENTFLAG |  | 0x80 |

###### Example 1

The following source filter is used to output logged alarms and events from the past 30 minutes in "read" mode. The oldest message for each OS server is output as the first one. The low limit value is also sent.

`OPCHAEServer hMode=read htStartTime=NOW-30M bBounds=TRUE`

###### Example 2

The following source filter is used to output events logged on September 1, 2006, from 10:00 a.m. to 12:00 p.m. in "read" mode. The newest message for each OS server is output as the first one. The limits for this time period are also sent.

`OPCHAEServer hMode=read htStartTime=2006-09-01T12:00:00.000Z htEndTime=2006-09-01T10:00:00.000Z bBounds=TRUE`

###### Example 3

The following source filter is used to output logged alarms and events from the past 30 minutes in "advise" mode. After reading the archived messages, newly generated messages are sent in the same way as for an active subscription.

`OPCHAEServer hmode=advise htStartTime=NOW-30M`

---

**See also**

[Access to logged events (RT Professional)](#access-to-logged-events-rt-professional)
  
[Syntax for accessing logged alarms using OPC (RT Professional)](#syntax-for-accessing-logged-alarms-using-opc-rt-professional)

#### WinCC OPC UA Server (RT Professional)

This section contains information on the following topics:

- [Principle of operation the WinCC OPC UA Server (RT Professional)](#principle-of-operation-the-wincc-opc-ua-server-rt-professional)
- [Security concept of OPC UA (RT Professional)](#security-concept-of-opc-ua-rt-professional)
- [OPC UA Services support (RT Professional)](#opc-ua-services-support-rt-professional)
- [Name area of the WinCC OPC UA server (RT Professional)](#name-area-of-the-wincc-opc-ua-server-rt-professional)
- [OPC UA Data Access (RT Professional)](#opc-ua-data-access-rt-professional)
- [OPC UA Log Access (RT Professional)](#opc-ua-log-access-rt-professional)
- [OPC UA Alarms &amp; Conditions (RT Professional)](#opc-ua-alarms-conditions-rt-professional)
- [Attributes of the WinCC message system (RT Professional)](#attributes-of-the-wincc-message-system-rt-professional)
- [Structure of the configuration file (RT Professional)](#structure-of-the-configuration-file-rt-professional)
- [Configure WinCC OPC UA Server (RT Professional)](#configure-wincc-opc-ua-server-rt-professional)

##### Principle of operation the WinCC OPC UA Server  (RT Professional)

###### Principle of operation

The WinCC OPC UA Server provides the following values:

- Process values
- Values from tag logs
- WinCC alarms

The WinCC OPC UA server is installed as Windows service and started automatically. The WinCC OPC UA server supports only the "UA-TCP UA-SC UA Binary" communication profile. The used port number is adjustable.

###### Supported specifications

OPC Unified Architecture is a specification for the transmission of process values and log data, as well as alarms and events. The WinCC OPC UA server supports the transfer of process values, log data and alarms. The WinCC OPC UA server supports the OPC UA specification 1.02. You can find detailed information under "Supported OPC UA Services".

###### URL of the WinCC OPC UA server

You access the WinCC OPC UA server via the following URL: "opc.tcp://[NodeName]:[Port]".

[NodeName]: Placeholder for the computer name. Is set automatically.

[Port]: Port number. The default is "4861".

###### Discovery Server

The "Discovery Server" is available by the OPC foundation. The "Discovery Server" is by default installed on the HMI device as Windows service. On the "Discovery Server" via OPC UA server UA clients information is available that is registered on the "Discovery Server".

The WinCC OPC UA server registers for Runtime-Start, depending on the configuration, on no, one or all available "Discovery Servers" If you end the Runtime, the WinCC OPC UA server is automatically logged off from the "Discovery Server".

###### Supported languages in the WinCC address area

The WinCC OPC A&amp;E Server supports the WinCC address area in the following languages:

- German
- English
- French
- Italian
- Spanish

---

**See also**

[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)
  
[Accessibility of WinCC OPC servers (RT Professional)](#accessibility-of-wincc-opc-servers-rt-professional)
  
[Security concept of OPC UA (RT Professional)](#security-concept-of-opc-ua-rt-professional)
  
[OPC UA Services support (RT Professional)](#opc-ua-services-support-rt-professional)
  
[Name area of the WinCC OPC UA server (RT Professional)](#name-area-of-the-wincc-opc-ua-server-rt-professional)
  
[OPC UA Data Access (RT Professional)](#opc-ua-data-access-rt-professional)
  
[OPC UA Log Access (RT Professional)](#opc-ua-log-access-rt-professional)
  
[Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)

##### Security concept of OPC UA (RT Professional)

###### Introduction

The WinCC OPC UA server uses the TCP/IP protocol for data exchange. For authorization between WinCC OPC UA server and OPC UA client certificates are exchanged. In addition, you can encode the data transfer.

###### Security concept

The WinCC OPC UA server and each OPC UA client authorize themselves mutually by exchanging certificates.

By default, the WinCC OPC UA server creates during installation a self signed instance certificate. You can alternatively replace this instance certificate with a project-specific instance certificate.

> **Note**
>
> **Private key and own certificates**
>
> If you have an own certification center, you can create your own certificates and make them available for all communication partners. In this case, delete the instance certificate created by WinCC OPC UA server.

The instance certificate is stored in the certificate memory. Depending on the configuration of the WinCC OPC UA server, one of the following certificate memories is used:

- Certificate memory of the WinCC OPC UA server
- Certificate memory of the operating system in "UA Applications" folder

In order for the WinCC OPC UA server and an OPC UA client to communicate with each other, the certificates must be known to each other:

- You use the common certificate of the operating system

  Or:
- You copy the certificates in the certificate memory of the participating communication partners:

  - WinCC OPC UA Server
  - OPC UA Client
  - Discovery server (optional)

###### Security settings

The following table lists the security settings supported by the WinCC OPC UA server:

| Security guidelines | Alarm security mode |  |  |
| --- | --- | --- | --- |
| None<sup>1</sup> | None |  |  |
| Basic128Rsa15<sup>2</sup> | None<sup>4</sup> | Signing<sup>5</sup> | Signing and encryption<sup>6</sup> |
| Basic256<sup>3</sup> | None | Signing | Signing and encryption |
| Basic256Sha256<sup> 3</sup> | None | Signing | Signing and encryption |
| 1: The certificate exchange is switched off. Every OPC UA client can log on to the WinCC OPC UA server. |  |  |  |
| 2: Certificate exchange with depth of encryption of 128 bit. |  |  |  |
| 3: Certificate exchange with depth of encryption of 256 bit. |  |  |  |
| 4: The data packages are exchanged after certificate check unsecured between client and server. |  |  |  |
| 5: The data packages are signed with the certificates, but not encoded |  |  |  |
| 6: The data packages are signed with the certificates and encoded |  |  |  |

> **Note**
>
> **Unsecured communication between client and server possible**
>
> Use the "None" setting only for test and diagnostics purposes.
>
> For a secure communication between client and server, use in operating mode at least the following settings:
>
> - Security guideline: Basic128Rsa15
> - Alarm security mode: Signing
>
> You can deactivate the security guideline "None" in the configuration settings of the WinCC OPC UA server.

###### User identification

For user account identification of an OPC UA client, the WinCC OPC UA server supports the methods "Anonymous" and "User name / password". Each user account must be known in the user administration of the operating system of the WinCC OPC UA server.

The user identification is only used for setting up a communication session. Different access rights are not supported.

You can deactivate the support of anonymous users in the configuration settings of the WinCC OPC UA server.

---

**See also**

[Structure of the configuration file (RT Professional)](#structure-of-the-configuration-file-rt-professional)
  
[Configure WinCC OPC UA Server (RT Professional)](#configure-wincc-opc-ua-server-rt-professional)
  
[Principle of operation the WinCC OPC UA Server (RT Professional)](#principle-of-operation-the-wincc-opc-ua-server-rt-professional)
  
[Setting up authentication via certificates. (RT Professional)](#setting-up-authentication-via-certificates-rt-professional)

##### OPC UA Services support (RT Professional)

###### Introduction

The WinCC OPC A&amp;E Server supports the following described functionality.

###### OPC UA Service Sets

The following table shows the supported OPC UA Service Sets:

| OPC UA Service Sets | Services | Comment |
| --- | --- | --- |
| Discovery Service Set | FindServers  GetEndpoints | - |
| Secure Channel Service  Session Service Set | All | - |
| View Service Set | Browse  BrowseNext  RegisterNodes  UnregisterNodes | Detecting the displayed WinCC data: Process values and archived data |
| Attribute Service Set | Read  Write HistoryRead  HistoryUpdate*<sup>)</sup> | only WinCC tags  only WinCC tags  only logging tags  only logging tags |
| Subscription Service Set | CreateSubscription  SetPublishingMode  Publish  RePublish  DeleteSubscription | - |
| MonitoredItem Service Set | CreateMonitoredItems  SetMonitoringMode  DeleteMonitoredItems | only "Value" attribute of WinCC tags  .EventNotifier during access to WinCC alarms |
| Method Service Set | Call | Acknowledge  ConditionRefresh |
| *: With restrictions, see "[Supported Write-Accesses](#supported-write-accesses-rt-professional)" |  |  |

###### OPC UA profile and Conformance Units

> **Note**
>
> The OPC UA profiles for "Historical Access" are not yet released, that is why they are not listed in the following:

The WinCC OPC UA server supports the following OPC UA 1.02 profiles without restrictions:

- 6.5.3 Base Server Behaviour Facet
- 6.5.12 Standard Event Subscription Server Facet
- 6.5.14 A &amp; C Base Condition Server Facet
- 6.5.24  Method Server Facet
- 6.5.30 Historical Raw Data Server Facet
- 6.5.36 Historical Data Update Server Facet
- 6.5.37 Historical Data Insert Server Facet
- 6.5.38 Historical Data Delete Server Facet
- 6.5.107 UA-TCP UA-SC UA Binary
- 6.5.125 SecurityPolicy - Basic256
- 6.5.124 SecurityPolicy - Basic128Rsa15
- 6.5.123 SecurityPolicy - None

The WinCC OPC A&amp;E Server supports the following OPC UA profiles shown in the following table, however with restrictions:

| Profile | "Group" | Not supported "Conformance Unit" |
| --- | --- | --- |
| 6.5.8 Standard DataChange    Subscription Server Facet | Monitored Item Services | DeadBand Filter |
| 6.5.9 Enhanced DataChange Subscription Server Facet | Monitored Item Services |  |
| 6.5.25 Core Server Facet | Attribute Services | Attribute Write Index |
| 6.5.26 Data Access Server Facet | Data Access | Data Access Analog  Data Access Multistate  Data Access PercentDeadBand  Data Access Semantic Changes  Data Access Two State |
| 6.5.35 Standard UA Server | Attribute Services | Attribute Write StatusCode &amp; TimeStamp |
| 6.5.47 Standard UA Server Profile | Attribute Services | Attribute Write StatusCode &amp; Timestamp |

---

**See also**

[Principle of operation the WinCC OPC UA Server (RT Professional)](#principle-of-operation-the-wincc-opc-ua-server-rt-professional)

##### Name area of the WinCC OPC UA server (RT Professional)

###### Introduction

The WinCC OPC UA server provides OPC UA clients with an hierarchical name area to display the following Runtime data:

- Process values (WinCC tags and WinCC tag groups)
- Data log inclusive logging tags
- WinCC alarms

The name area of the WinCC OPC UA server is attached in the "Objects" default folder.

The following screen shows the name area of the WinCC OPC UA server of an active WinCC project on the local PC ("@LOCALMACHINE::"):

![Introduction](images/23146612747_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Start node of the specific name area of WinCC. |
| ② | Display of the WinCC tags; the structure corresponds to the structure of the tags in WinCC. |
| ③ | Display of the data log |

###### Display of the WinCC tags

Tag groups, communication drivers and connections are displayed by OPC UA objects of the "FolderType" type. Each of these folders has references of the "Organizes" type to the subordinate objects and tags.

Internal and external WinCC tags are displayed by OPC UA tags of the "DataItemType" type. If a WinCC tag is additionally logged, the displayed OPC UA tag has additionally a reference of the "HasHistoricalConfiguration" type for a log configuration. The "Historizing" and "AccessLevel" attributes are respectively set.

The following table shows the most important attributes of the OPC UA tags that represent a WinCC tag. You can find the complete list of attributes in the "OPC UA Part 3 - Address Space Model 1.02 Specification" document under "5.6":

| Attribute | Description | Comment |
| --- | --- | --- |
| NodeId | Unique designation of the WinCC tag |  |
| BrowseName | WinCC tag name |  |
| DisplayName | WinCC tag name |  |
| Value | Tag value and status |  |
| DataType | OPC UA data type that corresponds to the WinCC tag type, for example:  - Int32; signed 32 bit value - UInt32; unsigned 32 bit value | - |
| AccessLevel | "CurrentRead" / "CurrentWrite"   "HistoryRead" / "HistoryWrite" | correspondingly to the WinCC tag configuration |
| ValueRank | Always "Scalar" | - |

###### Display of the logging tags

Process values and compressed logs are displayed by OPC UA objects of the "FolderType" type. Each of these folders has references of the "Organizes" type to the related logging tags.

Logging tags from process value or compressed logs are displayed by OPC UA tags of the "BaseDateVariableType" type. A logging tag always has a reference of the "HasHistoricalConfiguration" type for a log configuration.

The following table shows the most important attributes of the OPC UA tags that represent a WinCC logging tag. You can find the complete list of attributes in the "OPC UA Part 3 - Address Space Model 1.02 Specification" document under "§5.6":

| Attribute | Description | Comment |
| --- | --- | --- |
| NodeId | Unique designation of a logging tag |  |
| BrowseName | Name of the logging tag |  |
| DisplayName | Name of the logging tag |  |
| Description | Node description |  |
| Value | Not available | For a logging tag, this attribute cannot be read nor changed. |
| DataType | OPC UA data type that corresponds to the WinCC tag type, for example:  - Double; 64-bit floating point number - UInt32; unsigned 32 bit value | - |
| AccessLevel | "HistoryRead" / "HistoryWrite" | - |
| ValueRank | Always "Scalar" | - |

###### Access to WinCC alarms

The starting node of the WinCC namespace is an Event Notifier with which the OPC UA clients can receive the status changes of WinCC alarms via Subscriptions in Runtime.

##### OPC UA Data Access (RT Professional)

Internal and external WinCC tags are displayed by OPC UA tags of the "DataItemType" type. Other DataAccess tag types as "AnalogItem" or "DiscreteType" are not supported.

The WinCC OPC A&amp;E Server supports the reading access on the OPC UA tag attributes as "DataType" or "AccessLevel". Writing access and subscriptions are only supported for the "Value" attribute.

##### OPC UA Log Access (RT Professional)

###### Introduction

"OPC Historical Access" enables the access to logs and includes the "Historical Data" and "Alarms &amp; Events" services. The WinCC OPC UA server supports only the "Historical Data" service.

The WinCC OPC UA Server offers the OPC clients access to the raw data of tag logs via "Services".

- HistoryRead (READRAW)
- HistoryUpdate (INSERTDATA, REPLACEDATA, UPDATEDATA, DELETE_RAW)

You can read and limitedly write with an OPC UA client the values of logging tags in the tag logs. Depending on the configuration of the tag log, the logging tag can contain either raw or already processed process values.

###### Characteristics of logging tags

According to the OPC "OPC UA Part 11 - Historical Access 1.00 Specification" document, the tags to be logged must have a precise reference to a tag configuration ("HistoricalConfiguration"). A process tag can be contained in WinCC and also in several data logs. In this case the process tag is linked to one of the corresponding logging tags.

###### Properties of log configurations

The following table shows the Properties of an OPC UA tag configuration of the "HistoricalConfigurationType" type: In the "Description" property, the logging tag comment configured in WinCC is displayed. You can find the complete list of properties in the "OPC UA Part 11 - Historical Access 1.02 Specification" document under "§5.2.2":

| Property | Description / Value | Comment |
| --- | --- | --- |
| Definition | WinCC process tag name | For a process value log |
| Stepped | True | - |

The following optional Properties are not supported:

- MaxTimeInterval
- MinTimeInterval
- ExceptionDeviation
- ExceptionDeviationFormat

###### Limitations for Service "HistoryUpdate"

You can use the Service "HistoryUpdate" only on process value logs.

The following table lists the functions supported by the WinCC OPC UA server: Which functions are supported depends on the configuration of the WinCC OPC UA server as well as the process value log configuration. You will find additional information in the "OPC UA Part 11 - Historical Access 1.00 Specification" document under "§5.5":

| Service | Function | Description |
| --- | --- | --- |
| HistoryUpdate | INSERTDATA | Insert new log values |
|  | REPLACEDATA | Replace existing log values |
|  | UPDATEDATA | Replace of insert log values |
|  | DELETE_RAW | Delete log values |

---

**See also**

[OPC UA Services support (RT Professional)](#opc-ua-services-support-rt-professional)
  
[Name area of the WinCC OPC UA server (RT Professional)](#name-area-of-the-wincc-opc-ua-server-rt-professional)
  
[Supported Write-Accesses (RT Professional)](#supported-write-accesses-rt-professional)
  
[Configure WinCC OPC HDA Server (RT Professional)](#configure-wincc-opc-hda-server-rt-professional)

##### OPC UA Alarms & Conditions (RT Professional)

###### Introduction

The OPC UA server allows access to alarms of the WinCC message system.

The OPC UA server relays status changes of messages to OPC UA clients with WinCC-Event-Notifications via Subscriptions and Monitored Event Items , but manages no Condition instance in its namespace. The Event Notifier node to be used is the start node of the WinCC name area. The UA client can filter the messages and define the list of message attributes returned.

The OPC UA server supports the "OPC UA Alarms &amp; Conditions 1.02" specification.

###### Mapping of the message system to OPC UA event types

The messages are mapped to the following OPC UA event types:

****WinCCEventType****

This type is based on "BaseEventType" and maps "simple" WinCC messages with the following acknowledgment theory:

- "Message without status went out" is activated
- "Acknowledgment came in" is not activated

Examples of this type of message are starting and stopping motors**.**

****WinCCAlarmConditionType****

This type is based on "AlarmConditionType" and maps all messages which cannot be mapped on WinCCEventType, for example acknowledgeable messages and messages with the status "came in" and "went out".

With an alarm of the type "WinCCAlarmConditionType", the event is linked to a condition. For example, WinCC generates an alarm as soon as a limit violation of a tag occurs. This message in OPC UA is equivalent to an Alarm Condition.

**WinCC message attributes**

The two Event types add WinCC-specific message attributes to the basic type. The attributes are mapped 1:1 as UA Event Properties and are described in more detail in "Attributes of the WinCC message system".

###### Message class and message type

The message system informs the user of disturbances and operating conditions in the process. A message always belongs to a specific message class and message type, which are specified in the attributes "CLASSID", "TYPEID", "CLASSNAME" and "TYPENAME" of the corresponding UA Events.

###### Priority

When configuring messages in the message system, you can configure a priority of "0" to "16". The OPC UA specification defines a value range of "1" to "1000" for the Severity. "1" stands for the lowest and "1000" for the highest Severity.

The values of the priority must therefore be suitably mapped to the OPC severity. In standard mapping, a priority of "0" is assigned to OPC-Severity "1" and a priority of "16" to OPC-Severity "1000". All other values are interpolated linearly between "0" and "1000".

###### OPC UA mapping rules

During the configuration of the WinCC message system, settings are made to determine which process events generate a message. This message is generally shown as an Event in OPC UA.

The following table shows the most important Properties of an Events and how the WinCC message system provides the information.

| OPC UA property | Mapping in the WinCC message system |
| --- | --- |
| **For all event types:** |  |
| EventID | Unique message designation |
| EventType | Event type: Node ID of the WinCCAlarmConditionType node or WinCCEventType node |
| SourceNode | Irrelevant |
| SourceName | Indicates the source of the message. Mapping is described in more detail below. |
| Message | Message text for the corresponding message number. |
| Time | Time of the event. The time stamp is given in UTC |
| Severity | Priority of the WinCC message |
| **Only with WinCCAlarmConditionType:** |  |
| ConditionName | Set text that is output as well as the message. The text output depends on the mapping rule set:  - "Mode 1" and "Mode 2": Message number - "Mode 3": Message class, for example "Process control message" |
| Quality | Returns the quality of the message |
| ConditionClassId | Node ID of the "ProcessConditionClassType" node |
| ConditionClassName | "ProcessConditionClassType" |
| Retain | "TRUE" for pending alarms |
| NodeId | ConditionId: Designates an UA-Condition uniquely, for example, an alarm. Required for acknowledgment, even if no Condition instances are supported |
| EnabledState | "TRUE" when the alarm has been enabled |
| ActiveState/Id | "TRUE" when the alarm has arrived |
| AckedState/Id | "TRUE" when the alarm has been acknowledged |
| ClientUserId | Indicates the user that is logged on |

> **Note**
>
> The following OPC UA Condition and Alarm Properties are not supported by the OPC UA server:
>
> - BranchId
> - LastSeverity
> - InputNode
> - ConfirmedState
> - SuppressedState
> - ShelvingState
> - SuppressedOrShelved
> - MaxTimeShelved

###### Message statuses / acknowledgment statuses

The following table shows WinCC message status mapping to the corresponding WinCCAlarmConditionType - Properties:

| Message status | EnabledState/Id | ActiveState/Id | AckedState/Id |
| --- | --- | --- | --- |
| Locked message | FALSE | - | - |
| Enabled message | TRUE |  |  |
| Received message | TRUE | TRUE | FALSE |
| Sent message with acknowledgment | TRUE | FALSE | TRUE |
| Sent message without acknowledgment | TRUE | FALSE | FALSE |
| Acknowledged messages (message pending) | TRUE | TRUE | TRUE |
| Acknowledged messages (message no longer pending) | TRUE | FALSE | TRUE |
| Received, acknowledged message | TRUE | TRUE | TRUE |
| Received, sent message with acknowledgment | TRUE | FALSE | TRUE |
| Received, sent message without acknowledgment | TRUE | FALSE | FALSE |
| Message acknowledged by the system (message pending) | TRUE | TRUE | TRUE |
| Message acknowledged by the system (message no longer pending) | TRUE | FALSE | TRUE |
| Emergency-acknowledged message (message pending) | TRUE | TRUE | TRUE |
| Emergency-acknowledged message (message no longer pending) | TRUE | FALSE | TRUE |

###### Settings for mapping the WinCC message system

The configuration of the OPC UA server also applies to the OPC UA server as regards the mapping of the Properties "SourceName" and "Message" of a message.

- With OPC A&amp;E server with hierarchical access:

  | Symbol | Meaning |
  | --- | --- |
  | SourceName | Indicates the source of a message. The Source has the format "&lt;Server prefix&gt;::Area\UserTextBlock 2". The server prefix of the local computer is "@LOCALMACHINE". |
  | Message | Returns the message text of the corresponding message number |
- With OPC A&amp;E server without hierarchical access:

  | Symbol | Meaning |
  | --- | --- |
  | SourceName | Indicates the source of a message. The Source has the format "&lt;Server prefix&gt;::localhost::". The server prefix of the local computer is "@LOCALMACHINE". |
  | Message | Returns the message text of the corresponding message number |

###### Alarm groups

In WinCC, the alarm groups are not displayed in the namespace.

###### Supported event methods

**Acknowledgment**

A WinCC message is acknowledged using the "Acknowledge" method of the "AcknowledgeableConditionType" node in the standard OPC UA info model.

Only messages of the "WinCCAlarmConditionType" type can be acknowledged.

**ConditionRefresh**

Messages still pending are established using the "ConditionRefresh" method of the "ConditionType" node in the standard OPC UA info model.

###### Filters

The OPC UA client can defined a filter for Monitored Event Items .

The following operators are, however, not supported by the OPC UA server:

- FilterOperator_Cast
- FilterOperator_BitwiseAnd
- FilterOperator_BitwiseOr
- FilterOperator_RelatedTo
- FilterOperator_InView

##### Attributes of the WinCC message system (RT Professional)

###### Overview

The following table lists the configurable attributes of the WinCC message system. The attributes are mapped 1:1 as UA Event Properties .

| WinCC message attribute | Meaning | Data type |
| --- | --- | --- |
| CLASSNAME | Name of the message class | String |
| TYPENAME | Name of message type | String |
| FORECOLOR | Foreground color for incoming, outgoing and acknowledged messages. | Int32 |
| BACKCOLOR | Background color for incoming, outgoing and acknowledged messages. | Int32 |
| FLASHCOLOR | Flash color | Int32 |
| FLAGS | Indicates mandatory message acknowledgment | Int32 |
| TEXT01…TEXT10 | Content of user text block #1....#10 | String |
| PROCESSVALUE01…PROCESSVALUE10 | Content of process value block #1....#10 |  |
| STATETEXT | Status message | String |
| INFOTEXT | Information text for the message | String |
| LOOPINALARM | Indicates whether LoopInAlarm was configured | Int32 |
| CLASSID | Message class ID | Int32 |
| TYPEID | Message type ID | Int32 |
| MODIFYSTATE | Value of message status tag | Int32 |
| AGNR | Outputs the number of the automation system that generated the message | Int16 |
| CPUNR | Outputs the number of the CPU that generated the message | Int16 |
| DURATION | Outputs the time period between the incoming state, outgoing state and acknowledgment of a message | Int32 |
| COUNTER | Number of messages after the start of runtime | Int32 |
| QUITSTATETEXT | Indicates whether the message has been acknowledged | String |
| QUITCOUNT | Number of open, unacknowledged messages | Int32 |
| PARAMETER | Configuration parameter of the message | Int32 |
| BLOCKINFO | Current content of the message block | String |
| ALARMCOUNT | Number of pending messages | Int32 |
| LOCKCOUNT | Number of locked messages | Int32 |
| PRIORITY | Priority of the message | Int32 |
| APPLICATION | Outputs the application which triggered the message | String |
| COMPUTER | Outputs the name of the computer which processed the message | String |
| USER | Outputs the name of the user who processed the message | String |
| COMMENT | Comment of the alarm | String |
| HIDDEN-COUNT | Number of hidden messages | Int32 |
| OS-HIDDEN | Indicates that the message is hidden | Boolean |
| OS_EVENTID | WinCC alarm number | Int32 |
| BIG_COUNTER | Message counter | Int64 |

##### Structure of the configuration file (RT Professional)

###### Introduction

You configure the WinCC OPC UA server in the configuration file "OPCUASERVERWINCCPRO.XML".

###### File location

When you create a project in the TIA Portal, the project-specific configuration file "OPCUASERVERWINCCPRO.XML" is stored in the WinCC project folder under:

"&lt;WinCC project folder&gt;\OPC\UASERVER"

###### &lt;`SecuredApplication`&gt; section

In this section the OPC UA application security is set.

| Section | Description |
| --- | --- |
| &lt;Secured Application&gt; |  |
| &lt;BaseAddresses&gt;        &lt;...&gt;&lt;/...&gt;      &lt;/BaseAddresses&gt; | Address and port number  The parameter [`HostName`] is the placeholder for the computer name and is determined during runtime.   Example:   `<BaseAddresses>`    `<ua:String>opc.tcp://`    `[HostName]:5210</ua:String>`    `</BaseAddresses>` |
| &lt;SecurityProfileUris&gt;        &lt;SecurityProfile&gt;          &lt;...&gt;&lt;/...&gt;        &lt;/SecurityProfile&gt;         ...      &lt;/SecurityProfileUris&gt; | Security guidelines  - You enable the setting with "`true`". - You disable the setting with "`false`".   All active OPC clients with this certificate are thus disabled.  Example:   `<SecurityProfile>`    `<ProfileUri>http://opcfoundation.org/`    `UA/SecurityPolicy#Basic128Rsa15</ProfileUri>`    `<Enabled>false</Enabled>`    `</SecurityProfile>` |
| &lt;/Secured Application&gt; |  |

###### &lt;`ServerConfiguration`&gt; section

In this section you set the parameters for data transmission, authentication and optimized WinCC archive write access.

| Symbol | Meaning |
| --- | --- |
| &lt;ServerConfiguration&gt; |  |
| &lt;SecurityPolicies&gt;          &lt;SecurityPolicy&gt;          &lt;...&gt;&lt;/...&gt;          &lt;/SecurityPolicy&gt;          ...      &lt;/SecurityPolicies&gt; | Alarm security mode  To deactivate a security setting, delete the entire entry.  Example:   `<` `SecurityPolicy>`    `<ProfileUri>http://opcfoundation.org/`        `UA/SecurityPolicy#Basic128Rsa15`     `</ProfileUri>`   `<MessageSecurityModes>SignAndEncrypt`    `</MessageSecurityModes>`    `</SecurityPolicy>` |
| &lt;UserTokenPolicies&gt;          &lt;UserTokenPolicy&gt;          &lt;...&gt;&lt;/...&gt;          &lt;/UserTokenPolicy&gt;          ...      &lt;/UserTokenPolicies&gt; | User authentication  To deactivate a setting, delete the entire entry.  Example   `<UserTokenPolicy>`     `<TokenType>`      `<!--[User]-->`   `</TokenType>`    `</UserTokenPolicy>`   Use the "Anonymous" setting only for test and diagnostics purposes. |
| &lt;FastInsert&gt;          &lt;Users&gt;          &lt;...&gt;&lt;/...&gt;          &lt;/Users&gt;          &lt;Clients&gt;          &lt;...&gt;&lt;/...&gt;          &lt;/Clients&gt;      &lt;/FastInsert&gt; | Optimized WinCC archive write access  - You use "`true`" to activate the optimized WinCC archive write access for all OPC UA clients. - You use "`false`" to specify whether specific Windows users or OPC UA clients may use the optimized WinCC archive write access.   You specify the Windows user under `<Users>`.   You specify the OPC UA clients under `<Clients>`. As `ClientName`, use the "Common Name" that is entered in the client certificate.   Example:   `<EnabledByDefault>false</EnabledByDefault>`    `<Users>`    `<User>domain\user1</User>`    `</Users>`    `<Clients>`    `<Client>ClientName1</Client>`    `</Clients>` |
| &lt;/ServerConfiguration&gt; |  |

---

**See also**

[Security concept of OPC UA (RT Professional)](#security-concept-of-opc-ua-rt-professional)
  
[Configure WinCC OPC UA Server (RT Professional)](#configure-wincc-opc-ua-server-rt-professional)
  
[Setting up authentication via certificates. (RT Professional)](#setting-up-authentication-via-certificates-rt-professional)

##### Configure WinCC OPC UA Server (RT Professional)

###### Introduction

You configure the WinCC OPC UA server in the runtime settings and in the configuration file "OPCUASERVERWINCCPRO.XML".

###### Configuring the WinCC OPC UA server in runtime settings

To configure the WinCC OPC UA server in the runtime settings, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. If necessary, configure the write access validation under "OPC settings &gt; Configuration of the OPC Historical Access".
3. Configure the server settings under "OPC settings &gt; Configuration of the OPC Unified Architecture Server":

   - Change the "Port number", if required
   - Activate at least one of the "Security guidelines" and the respective "Alarm security mode".

**Note**

The "Configuration of the OPC Historical Access" applies for the WinCC OPC HDA server as well as for the OPC UA server.

**Note**

**Unsecured communication between client and server possible**

Use the "None" setting only for test and diagnostics purposes.

###### Configuring the WinCC OPC UA server in the configuration file

To configure the WinCC OPC UA server in the configuration file, proceed as follows:

1. Open the Windows Explorer.
2. ​Navigate to the directory​ "&lt;WinCC project folder&gt;\OPC\UASERVER".
3. Open the configuration file ​"OPCUASERVERWINCCPRO.XML".
4. If necessary, change the port number under `<``BaseAddresses``>`.

   Do not use a port number that is already assigned to another application.
5. Configure the OPC UA application security in the section `<SecuredApplication>.`.
6. Configure the data transmission, authentication and optimized WinCC archive write access in the section `<ServerConfiguration>`.

###### Result

The WinCC OPC UA Server is configured. If you activate the project on the HMI device, the WinCC OPC UA server is accessible.

---

**See also**

[Security concept of OPC UA (RT Professional)](#security-concept-of-opc-ua-rt-professional)
  
[Structure of the configuration file (RT Professional)](#structure-of-the-configuration-file-rt-professional)
  
[OPC UA Log Access (RT Professional)](#opc-ua-log-access-rt-professional)
  
[Supported Write-Accesses (RT Professional)](#supported-write-accesses-rt-professional)
  
[Basic settings for OPC (RT Professional)](#basic-settings-for-opc-rt-professional)

### WinCC OPC connection (RT Professional)

This section contains information on the following topics:

- [Creating a connection to an OPC server (RT Professional)](#creating-a-connection-to-an-opc-server-rt-professional)
- [Accessing process values of an OPC server (RT Professional)](#accessing-process-values-of-an-opc-server-rt-professional)

#### Creating a connection to an OPC server (RT Professional)

##### Introduction

If to an OPC DA server an external control is available, you can access its process values from WinCC with the help of the WinCC OPC connection. You configure for this in the engineering system an OPC connection to the desired OPC server. You configure afterwards WinCC tags for the process values of the OPC server.

##### Requirement

- The OPC server to be addressed is ready-to-operate and in the "running" status
- The OPC server and the HMI device with WinCC Runtime Professional are located in a network

##### Procedure

To create a connection to an OPC server, follow these steps:

1. On the HMI device, open the "Connections" editor.
2. Create a new connection and enter a meaningful name.
3. Choose "OPC" as the "Communication driver".
4. In the work area under "Parameters &gt; OPC settings", enter the communication peer.

   - Select the "Type of OPC server".
   - Select the OPC server based on the OPC server type you chose, or enter the IP address or name of the remote computer.

##### Result

The OPC connection is configured. To access data from the OPC server, you create tags.

---

**See also**

[Accessing process values of an OPC server (RT Professional)](#accessing-process-values-of-an-opc-server-rt-professional)
  
[Using OPC in WinCC (RT Professional)](#using-opc-in-wincc-rt-professional)

#### Accessing process values of an OPC server (RT Professional)

##### Requirement

- The OPC server to be addressed is ready-to-operate and in the "running" status
- A connection to the OPC-Server is created

##### Procedure

To access process values of an OPC-Server via the OPC connection, follow these steps:

1. On the configuration PC in the project navigation, open the "HMI tags" editor under the HMI device that you use as an OPC client.
2. Create a tag with the same data type as the tag on the OPC server.
3. Select the OPC connection for "Connection".
4. Enter the "Address", or select the desired tag on the OPC server via the object list.

##### Result

If you launch Runtime on the HMI device, the process value from the OPC server will be written to the tag on the HMI device via the OPC connection.

---

**See also**

[Creating a connection to an OPC server (RT Professional)](#creating-a-connection-to-an-opc-server-rt-professional)

### WinCC OPC UA connection (RT Professional)

This section contains information on the following topics:

- [Creating a connection to an OPC UA server (RT Professional)](#creating-a-connection-to-an-opc-ua-server-rt-professional)
- [Setting up authentication via certificates. (RT Professional)](#setting-up-authentication-via-certificates-rt-professional)
- [Creating OPC UA tags (RT Professional)](#creating-opc-ua-tags-rt-professional)
- [Set read and write protection for OPC-UA tags (RT Professional)](#set-read-and-write-protection-for-opc-ua-tags-rt-professional)
- [Creating array tags for OPC UA connection (RT Professional)](#creating-array-tags-for-opc-ua-connection-rt-professional)
- [Overview of the supported data types (RT Professional)](#overview-of-the-supported-data-types-rt-professional)
- [Diagnostics options of the "OPC UA" channel (RT Professional)](#diagnostics-options-of-the-opc-ua-channel-rt-professional)
- [Supported OPC UA services of the OPC UA client (RT Professional)](#supported-opc-ua-services-of-the-opc-ua-client-rt-professional)
- [Description of Log File Entries (RT Professional)](#description-of-log-file-entries-rt-professional)

#### Creating a connection to an OPC UA server (RT Professional)

##### Introduction

The OPC UA client accesses process values in the hierarchical name space of an OPC UA server. For this access to be carried out, an OPC UA server and the OPC UA client authorize each other through the exchange of certificates. In addition, you can encode the data transfer.

TIA Portal has its own independent certificate store. The certificates from the certificate store are not automatically transferred in Runtime or to the simulation. Therefore, the certificates for any Runtime or simulation PC must be configured manually.

The OPC UA client of the TIA Portal by default classifies each certificate of an OPC UA server as "trustworthy". The certificates must be configured manually for the OPC UA clients in Runtime or simulation. How an OPC UA server responds to a connection request of the OPC UA client depends on the configuration of the OPC UA server.

To establish communication to an OPC UA server, request the following information from the operator of the OPC UA server:

- URL of the OPC UA server
- Security settings
- Required certificates

You can protect the OPC UA connections through authentication. By default, each new OPC UA connection is created as "Anonymous". If you want to protect the connection, enter your user name and password.

##### Requirement

URL and security settings of the OPC UA server are known.

##### Procedure

To create a connection to an OPC UA server, proceed as follows:

1. Open the "Connections" editor on the HMI device.
2. Create a new connection and enter a meaningful name.
3. Select the entry "OPC UA" as the "Communication driver".
4. Configure the "OPC Server" under "Parameters" in the work area:

   - Enter the URL of the OPC UA server in the "UA server discovery URL" text box, or select the OPC UA server from the list.
   - In "Security policy", select one of the supported security policy options.
   - In "Message security mode", select one of the supported security mode options.
5. Enter your user name and password to protect the OPC UA connection.

**Note**

**Migration**

For security reasons, the password is not migrated during migration.

##### Result

The OPC UA connection is configured. You create tags or arrays to access data from the OPC UA server.

##### Additional information on OPC UA connections

- To make a device of the device version V14.0.0.0 available for the OPC UA connection, you need to change the device version to V14.0.1.0 or higher.
- The OPC UA connection is available for a WinCC Runtime Professional device as of version V14.0.1.0. The OPC UA connection protected through authentication is available as of version V15.0.
- In addition, you can protect the assigned password through password protection in runtime (password for transport).

---

**See also**

[Setting up authentication via certificates. (RT Professional)](#setting-up-authentication-via-certificates-rt-professional)
  
[Creating OPC UA tags (RT Professional)](#creating-opc-ua-tags-rt-professional)
  
[Overview of the supported data types (RT Professional)](#overview-of-the-supported-data-types-rt-professional)
  
[Password protection in runtime (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#password-protection-in-runtime-rt-professional)

#### Setting up authentication via certificates. (RT Professional)

##### Server certificates and client certificates

Distinguish between client and server certificates when configuring. Secure communication is only possible when client and server recognize each other's certificates.

Certificates are linked to the respective PC. If the Runtime project is loaded on another PC, the process of mutual exchange of trust certificates must be repeated.

For communication, the OPC UA server must recognize the following client certificates as trustworthy:

- "Siemens OPC UA Client for WinCC"

  Without a valid certificate of the TIA Portal, the tag browser aborts the connection attempt.
- "Siemens OPC UA Client for WinCC Runtime"

  Without a valid Runtime certificate, no current values are displayed in runtime.

Use the WinCC channel diagnostics for the analysis.

You can find additional information under Security Concept of OPC UA.

##### Setting up valid certificates

A self-signed certificate for the tag browser of the TIA Portal ""Siemens OPC UA Client for WinCC" and a certificate for the OPC UA channel of WinCC Runtime "Siemens OPC UA Client for WinCC Runtime" are created during installation. The OPC UA client can only connect to the OPC UA server if the server identifies this client certificate as trustworthy.

When the tag browser opens, the OPC UA server checks the client certificate of the TIA Portal. If the server does not recognize the client certificate as trustworthy, the connection is rejected. The error message "Connection failed" appears. The tag browser automatically accepts the server certificate.

Each WinCC Runtime or simulation has its own certificate and a project-independent certificate store. Certificates are not transferred when downloading the project. This means you must trust the certificate of the OPC UA server on each HMI device. The OPC UA server must trust each HMI device certificate.

For the OPC UA client of Runtime, the certificates are located below the installation path: c:\Program Files (x86)\Siemens\Automation\SCADA-RT_V1x\WinCC\OPC\UAClient\PKI\.

A rejected certificate is stored in the "rejected\certs" folder. To trust a certificate, move it to the "trusted\certs" folder.

---

**See also**

[Creating a connection to an OPC UA server (RT Professional)](#creating-a-connection-to-an-opc-ua-server-rt-professional)
  
[Security concept of OPC UA (RT Professional)](#security-concept-of-opc-ua-rt-professional)
  
[Creating OPC UA tags (RT Professional)](#creating-opc-ua-tags-rt-professional)
  
[Structure of the configuration file (RT Professional)](#structure-of-the-configuration-file-rt-professional)

#### Creating OPC UA tags (RT Professional)

##### Introduction

You create the tags for the OPC UA connection in the "HMI Tags" editor. You can view these tags in the tag browser.

##### Requirements

- The project is open.
- The connection to the OPC UA server has been set up.

##### Procedure

You create OPC UA tags exactly as you would internal HMI tags. You can find additional information under "Creating internal tags".

Make the following deviating settings for the OPC UA tags:

1. In the "Connection" field, select the connection to the OPC UA server that you have set up beforehand.
2. In the "Data type" field, select a permissible data type for OPC UA tags.
3. In the "Address" column, click on the drop-down list and select the address in the tag browser.

   You can also enter the address manually.

   ![Procedure](images/95430903947_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/95430903947_DV_resource.Stream@PNG-en-US.png)
4. If required, make settings under "Area", "Linear scaling", "Start value" and "Substitute value".

##### Result

You have created OPC UA tags that you can use for the OPC UA connection in your project.

---

**See also**

[Creating internal tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-internal-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the supported data types (RT Professional)](#overview-of-the-supported-data-types-rt-professional)
  
[Creating a connection to an OPC UA server (RT Professional)](#creating-a-connection-to-an-opc-ua-server-rt-professional)
  
[Setting up authentication via certificates. (RT Professional)](#setting-up-authentication-via-certificates-rt-professional)

#### Set read and write protection for OPC-UA tags (RT Professional)

##### Introduction

You can protect OPC UA tags against access by clients. For this, you assign read and write protection for individual OPC UA tags. You assign the following settings in the properties of the tags:

| Property | Runtime behavior |
| --- | --- |
| OPC write protection | Clients have read-only access to the tag value. |
| OPC read protection | Clients can neither read nor write the tag value. |

##### Requirement

- The OPC UA tag for which you want to define read and write protection is created.
- The Inspector window with the properties for this tag is open.

##### Procedure

1. In the Inspector window, select "Properties &gt; Properties &gt; Settings".
2. Enable the desired protection under "OPC UA".
3. Download the full project.

**Note**

If you enable the "OPC read protection", the "OPC write protection" option is automatically enabled.

If you disable the OPC read protection the option "OPC write protection" remains enabled.

##### Result

You have configured a write or read protection for an OPC UA tag.

#### Creating array tags for OPC UA connection (RT Professional)

##### Introduction

You create the array tags for the OPC UA connection in the "HMI Tags" editor. You can view these array tags in the tag browser.

You can select the arrays but not the individual array elements in the tag browser.

It is possible to configure one-dimensional arrays for all supported OPC UA data types, with the exception of ByteString.

##### Requirement

- The project is open.
- The connection to the OPC UA server has been set up.

##### Procedure

You create the array tags for OPC UA connections exactly as you would normal array tags. You can find additional information under "Create array tag".

If needed, make the following deviating settings for the created OPC UA connection under "Parameters &gt; OPC Server":

1. To use arrays on older OPC UA servers that do not support writing single array elements, use the "Write array elements without IndexRange" setting.

![Procedure](images/102441376139_DV_resource.Stream@PNG-en-US.png)

If the "Write array elements without IndexRange" setting is selected, the complete array is read and the corresponding elements of the array modified. The entire array is then written back to the server.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of data**  If the "Write array elements without IndexRange" setting is selected, data loss may occur if the arrays are changed between the read and write access on the server. |  |

For additional information on arrays, refer to "Array basics".

---

**See also**

[Creating array tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-array-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on arrays (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-arrays-basic-panels-panels-comfort-panels-rt-advanced)

#### Overview of the supported data types (RT Professional)

##### Introduction

For the data exchange, configure access to the tags of the OPC UA server for the OPC UA client. To do so, import an OPC UA node as HMI tag in the tag management.

##### Supported data types

The OPC UA client supports the following data types:

- Boolean
- Byte (unsigned byte)
- Date Time
- Double
- Float
- Int16
- Int32
- Raw (ByteString)
- SByte
- String
- UInt16
- UInt32
- Int32
- UDT

> **Note**
>
> The elements of the UDT can be interconnected to OPC UA tags.

> **Note**
>
> OPC UA structures are not supported.
>
> If the server supports OPC UA structures, however, you can access elements of an OPC UA structure.

---

**See also**

[Creating OPC UA tags (RT Professional)](#creating-opc-ua-tags-rt-professional)
  
[Creating a connection to an OPC UA server (RT Professional)](#creating-a-connection-to-an-opc-ua-server-rt-professional)

#### Diagnostics options of the "OPC UA" channel (RT Professional)

The following options are available for diagnosing and troubleshooting the "OPC UA" channel and a tag of this channel:

##### Checking the configuration of connection and tags

Possible errors can lie in the configured system parameters and connection parameters. An incorrect addressing of the tag can also be responsible for faulty tag values.

##### Diagnosis of the channel using "Channel Diagnosis"

The status of the channel and the connection can be queried in Runtime using "Channel Diagnosis". Errors that occur are displayed as so-called "Error Codes".

##### Diagnosis of the channel tags

In the tag management, the current value, the current quality code and the last change time of the tags can be queried in Runtime.

#### Supported OPC UA services of the OPC UA client (RT Professional)

##### OPC UA Services support

The OPC UA client supports the following OPC UA services:

- SecurityPolicy - Basic256Sha256
- SecurityPolicy - Basic128Rsa15
- SecurityPolicy - Basic256
- SecurityPolicy - None
- DataAccess ClientFacet

##### Explanation of the security settings

The following table lists the security settings supported by the OPC UA client:

| SecurityPolicy | Message Security Mode |  |  |
| --- | --- | --- | --- |
| None<sup>1</sup> | None |  |  |
| Basic128Rsa15<sup>2</sup> | None<sup>4</sup> | Sign<sup>5</sup> | SignAndEncrypt<sup>6</sup> |
| Basic256<sup>3</sup> | None | Sign | SignAndEncrypt |
| Basic256Sha256<sup>3</sup> | None | Sign | SignAndEncrypt |
| 1: The certificate exchange is disabled. Every OPC UA client can log on to the WinCC OPC UA server. This setting can be disabled on each OPC UA server. |  |  |  |
| 2: Certificate exchange with depth of encryption of 128 bit. |  |  |  |
| 3: Certificate exchange with depth of encryption of 256 bit. |  |  |  |
| 4: The data packages are exchanged after certificate check unsecured between client and server. |  |  |  |
| 5: The data packages are signed with the certificates, but not encoded |  |  |  |
| 6: The data packages are signed with the certificates and encoded |  |  |  |

> **Note**
>
> **Unsecured communication between client and server possible**
>
> Use the "none" setting only for test and diagnostics purposes.
>
> For a secure communication between client and server, use in operating mode at least the following settings:
>
> - SecurityPolicy: Basic128Rsa15
> - Message Security Mode: Sign
>
> The SecurityPolicy - Basic256Sha256 setting is recommended.

#### Description of Log File Entries (RT Professional)

##### Introduction

Important changes of state and errors are entered in the log file through the channel. Only the most important entries are described in the following sections. These entries can be used to further analyze a communication problem.

There are two type of such problems:

- INFO
- ERROR

Logging must be enabled in the channel diagnosis. The file name and flags (trace level) are also configured there.

The log files are stored here: c:\Program Files (x86)\Siemens\Automation\SCADA-RT_V1x\WinCC\diagnose\.

##### Systematic structure of an entry

![Systematic structure of an entry](images/2451632651_DV_resource.Stream@PNG-en-US..png)

##### Example of entries in the logbook

2016-03-24 10:43:18.756 INFO Log starting ...

2016-03-24 10:43:18.756 INFO | LogFileName : C:\Program Files (x86)\Siemens\Automation\SCADA-RT_V1x\WinCC\diagnose

2016-03-24 10:43:18.756 INFO | LogFileCount : 3

2016-03-24 10:43:18.756 INFO | LogFileSize : 1400000

2016-03-24 10:43:18.756 INFO | TraceFlags : fa000007

2016-03-24 10:43:18.756 INFO Process attached at 2016-03-24 09:43:18.746 UTC

2016-03-23 10:46:18.756 INFO Process detached at 2016-03-2410:46:18.746UTC

2016-03-27 13:22:43.390 ERROR ..FOPCData::InitOPC CoCreateInstanceEx- ERROR 800706ba

2016-03-27 13:22:43.390 ERROR - ChannelUnit::SysMessage("[OPC Groups (OPCHN Unit #1)]![OPC_No_Machine]: CoCreateInstance for server "OPCServer.WinCC" on machine OPC_No_Machine failed, Error=800706ba (HRESULT = 800706ba - RPC_S_SERVER_UNAVAILABLE (The RPC Server is unavailable.))")

### Commissioning OPC (RT Professional)

This section contains information on the following topics:

- [Configuring DCOM user permissions in Windows (RT Professional)](#configuring-dcom-user-permissions-in-windows-rt-professional)
- [Adjusting Windows firewall settings (RT Professional)](#adjusting-windows-firewall-settings-rt-professional)

#### Configuring DCOM user permissions in Windows (RT Professional)

##### Introduction

The OPC DA client and OPC DA server are DCOM applications, whose security settings must be set in compliance with the DCOM security mechanisms:

- The OPC DA client needs launch/activation rights and access rights for the OPC DA server.
- The OPC DA server only needs access rights for the OPC DA client.

The following must be known on the PCs of the OPC DA server and the OPC DA client respectively:

- The user account for which the OPC DA client is executed
- The "Simatic HMI" user group

The "Simatic HMI" user group is already created on an HMI device during installation. The security settings of WinCC OPC DA server and the WinCC OPC channel are also preconfigured during installation.

In order to create an additional user for the operation of the OPC DA client, add the user as a member to the "Simatic HMI" user group.

##### Requirement

You have administrator rights.

##### Setting up a user account on PCs with an external OPC DA server or external client

On PCs without a WinCC installation, you configure the access rights manually.

1. Open Windows user administration.
2. Create the "SIMATIC HMI" user group.
3. Under "DCOM &gt; My Computer &gt; COM Security &gt; Access Permissions &gt; Edit Default" enter the permissions "Local Access" and "Remote Access".
4. Assign the user accounts for this user group.

For more information on assigning user rights, see the documentation for Windows XP / 7.

#### Adjusting Windows firewall settings (RT Professional)

##### Introduction

After installation of WinCC, the Windows firewall settings of the WinCC OPC servers are correctly configured.

If OPC clients access OPC servers in different subnets, you must adapt the configuration of the permitted network areas to the OPC servers.

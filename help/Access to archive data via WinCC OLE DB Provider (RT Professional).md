---
title: "Access to archive data via WinCC OLE DB Provider (RT Professional)"
package: OLEDBWCCPenUS
topics: 32
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Access to archive data via WinCC OLE DB Provider (RT Professional)

This section contains information on the following topics:

- [WinCC Archive Connector (RT Professional)](#wincc-archive-connector-rt-professional)
- [Access to archive data via OLE DB Provider (RT Professional)](#access-to-archive-data-via-ole-db-provider-rt-professional)
- [Application cases (RT Professional)](#application-cases-rt-professional)
- [Querying the archive data (RT Professional)](#querying-the-archive-data-rt-professional)
- [Analysis functions for messages and process values (RT Professional)](#analysis-functions-for-messages-and-process-values-rt-professional)
- [Bases of OLE DB (RT Professional)](#bases-of-ole-db-rt-professional)
- [WinCC OLE DB Provider (RT Professional)](#wincc-ole-db-provider-rt-professional)
- [Installation (RT Professional)](#installation-rt-professional)

## WinCC Archive Connector (RT Professional)

This section contains information on the following topics:

- [WinCC Archive Connector (RT Professional)](#wincc-archive-connector-rt-professional-1)
- [The "Configuration" tab (RT Professional)](#the-configuration-tab-rt-professional)
- [The "Connect/Disconnect Archive" tab (RT Professional)](#the-connectdisconnect-archive-tab-rt-professional)

### WinCC Archive Connector (RT Professional)

#### Functionality

The WinCC "Archive Connector" is used for configuring the access to the archive database.

The tool is an integral part of WinCC DataMonitor.

With the Archive Connector, already swapped out WinCC archives can be reconnected to an SQL Server.

The DataMonitor client or WinCC OLE DB Provider can then access the archives once again.

Functions of the WinCC Archive Connector:

- Manual Connection: Local databases may be selected and connected to the local SQL server.
- Manual Disconnection: Connected databases may be selected and disconnected from the SQL server.
- Automatic Connection: Local directories can be selected in which WinCC archives are swapped. All archives which were added to the selected directories from the moment change monitoring was activated are automatically linked to the SQL server.

The Archive Connector may only be operated using a local SQL server and a WinCC DataMonitor license.

Once the configuration has been completed, the Archive Connector may be closed.

> **Note**
>
> WinCC RT archives in the directory "<Project Directory> \ ArchiveManager" and the associated subdirectories must not be connected to or disconnected with the Archive Connector because their connection to the SQL server is managed by the WinCC RT Professional HMI device.
>
> The path for the swapped out WinCC archives is set in WinCC with the Archive Configurator of tag logging, for example, not with the WinCC Archive Connector.
>
> If access is to be made to swapped out archives which are on stored removable media, such as tape or MOD drives, pay attention that the connection to these archives on this medium is disconnected using the Archive Connector before changing the medium in the drive. After changing the medium, the user should check the Archive Connector whether or not the archives on the new medium are connected.
>
> Configuration with the WinCC Archive Connector should be restricted to a limited group of people. This means access to the tool should be protected by using the Windows "Administrators" user right or other Windows protection mechanisms, such as storage in a protected directory.

> **Note**
>
> Use the Archive Connector or DataMonitor to access the connected archives.
>
> The following objects do not give any access to the archives linked with the Archive Connector:
>
> - Alarm view
> - Table view
> - f(t) trend view
> - f(x) trend view

### The "Configuration" tab (RT Professional)

#### The "Configuration" tab

![The "Configuration" tab](images/2548233099_DV_resource.Stream@PNG-en-US..png)

In the "Configuration" tab, archiving folders are displayed and managed that are to be accessed through the web or the WinCC OLE DB-Provider.

Archiving folders can be added or removed by using the buttons. A symbolic, unique name has to be assigned during configuration for each archiving folder.

The DataMonitor client or the WinCC OLE DB-Provider use the symbolic name to access the archive.

The name is also used for managing and connecting swapped out data from several computers or projects.

The symbolic names must only contain characters permitted in the SQL syntax.

By activating the corresponding check box, all archives added to the selected folder at the time of activation will automatically be connected to the SQL server.

If you activate or deactivate monitoring, the changes will not be activated until you close the Archive Connector.

### The "Connect/Disconnect Archive" tab (RT Professional)

#### The "Connect/Disconnect Archive" tab

![The "Connect/Disconnect Archive" tab](images/2548240651_DV_resource.Stream@PNG-en-US..png)

The "Connect/Disconnect Archive" tab lists all archives existing in the archiving directories.

The connection status of each archive is displayed. The connection to the archives can be established or terminated by using the buttons.

The archive type is shown in the "Type" field.

- "A" = Alarm Logging;
- "TF" = Tag Logging (Fast);
- "TS" = Tag Logging (Slow).

The columns "From" and "To" provide information on the local time zone.

> **Note**
>
> The connection of multiple, swapped-out archives to the SQL server may take several seconds.
>
> It is not possible to connect a database file with the same name twice.
>
> The WinCC Archive Connector connects finalized and backed up (swapped-out) archives to the SQL server. Archives not finalized are not supported.
>
> The user interface language of the Archive Connector is based on the settings of the regional and language options in Windows.

## Access to archive data via OLE DB Provider (RT Professional)

This section contains information on the following topics:

- [Options for accessing archive data (RT Professional)](#options-for-accessing-archive-data-rt-professional)
- [Configuring access to archive data (RT Professional)](#configuring-access-to-archive-data-rt-professional)
- [Establishing the Connection to the Archive Database (RT Professional)](#establishing-the-connection-to-the-archive-database-rt-professional)

### Options for accessing archive data (RT Professional)

#### Introduction

Using OLE DB, you have the following options for accessing WinCC archive data and for displaying them using an external interface.

#### Access with WinCC OLE DB Provider

WinCC OLE DB provides access to all WinCC archive data.

Depending on the configuration, process data of WinCC are stored in compressed form. WinCC OLE DB Provider permits transparent access even to these data.

Use the "SQL Server Import / Export Wizard" to take advantage of standard SQL queries. You can save the unzipped files to an intermediate database using the wizard; you access the database with standard SQL queries.

> **Note**
>
> If WinCC closes a full archive and opens a new one, no data from the message and process value archives are read momentarily via the OLE DB Provider.

#### Access with Microsoft OLE DB

Microsoft OLE DB provides access to all WinCC user archives.

> **Note**
>
> Microsoft OLE DB is only tested and released for access to WinCC user archives but not to alarm and process value archives.   
> Use the WinCC OLE DB Provider to access message and process value archives.

### Configuring access to archive data (RT Professional)

#### Configuration options

For access to databases with WinCC OLE DB, you may write your own applications.

For the communication with the WinCC OLE DB-Provider, ADO DB is used in applications created with, for example, Visual Basic, VBScript or VBA.

> **Note**
>
> **Special characters in tag names**
>
> Please not that programming languages, such as Visual Basic, VBScript or VBA, only allow the following characters in the tag names: "A to Z", "a to z", "0 to 9" and "_".
>
> If you use special characters, such as "," or ";", in the tag names in WinCC, the script will be aborted with an error message. In this case use the "Tag ID" to access a tag with special characters in the script name.

#### Requirements

- WinCC RT Professional or WinCC V12 must be installed on the accessing computer for access to archive data.
- For swapped out archives, establish the connection between the SQL database and the swapped out archives with the WinCC Archive Connector.

  > **Note**
  >
  > The WinCC RT archives in the directory "<Project directory> \ ArchiveManager" and the associated subdirectories must not be connected or disconnected with the Archive Connector, because their connection to the SQL server is managed by WinCC RT Professional.

#### Procedure

1. Establish the connection to the database, for example, by using MS Excel or your own application.
2. Define the required selection criteria.
3. Read out the archive data.

   The query result may be displayed in MS Excel, for example, or exported as a CSV file.

### Establishing the Connection to the Archive Database (RT Professional)

#### Introduction

For ActiveX data objects (ADO), the connection between the application and the archive database is established by the connection object. An important parameter here is the ConnectionString. The ConnectionString contains all necessary information for access to the database using OLE DB Provider.

**Structure of the ConnectionString**

`"Provider = Name of the OLE DB Provider; Catalog=Datebase name;Data Source=Server name;"`

| Parameter | Description |
| --- | --- |
| Provider | Name of the OLE DB Provider:  e.g. WinCCOLEDBProvider |
| Catalog | Names of the WinCC database With WinCC RT databases, you will use database names that end in "R." <Datenbankname_R>. The database "CC_ExternalBrowsing" can also be used.  If you have connected swapped out WinCC archives to the SQL Server via the WinCC Archive Connector, use their symbolic name.    **Note**   Enter the WinCC project name for "Catalog" for transparent access; for e.g.: "Catalog=WinCC_Project_Name".   **Note**   If you access message archives or swapped out archives via "CC_ExternalBrowsing", this access may take several minutes. |
| Data Source | Server name Local: ".\WinCC" or "<Computer Name>\WinCC"  Remote: "<Computer name>\WinCC"   **Note**   Enter the transparent access to the Central Archive Server and in case of redundant servers enter the following via the OLE DB-Provider for "Data Source":  <Symbolic Computer Name>::\WinCC.    **Note**   Use the archive tag name to directly access an archive tag on the central archive server CAS. The central archive server CAS returns the CAS-ID and not the archive tag ID as ID:  <SYMBOLIC COMPUTER NAME>\\<Achive_Var_Name> |

**Example Process Value and Message Archive:**

In the following example, a connection object is created with subsequent opening of the connection to the WinCC database (process value and message archive).

`Set conn = CreateObject("ADODB.Connection")`

`conn.open "Provider=WinCCOLEDBProvider.1;Catalog=CC_OpenArch_03_05_27_14_11_46R;Data Source=.\WinCC"`

**Example User Archive:**

In the following example, a connection object is created with subsequent opening of the connection to the WinCC user archive.

`Set conn = CreateObject("ADODB.Connection")`

`conn.open "Provider=SQLOLEDB.1; Integrated Security=SSPI; Persist Security Info=false; Initial Catalog=CC_OpenArch_03_05_27_14_11_46R; Data Source=.\WinCC"`

> **Note**
>
> In order to improve performance during local access, enter "<Computer Name>\WinCC" as the data source instead of ".\WinCC".

## Application cases (RT Professional)

This section contains information on the following topics:

- [Use Case 1: Local Access to WinCC RT Databases (RT Professional)](#use-case-1-local-access-to-wincc-rt-databases-rt-professional)
- [Use Case 2: Remote Access to WinCC RT Databases (RT Professional)](#use-case-2-remote-access-to-wincc-rt-databases-rt-professional)
- [Use Case 3: Local Access to WinCC Archive Databases (RT Professional)](#use-case-3-local-access-to-wincc-archive-databases-rt-professional)
- [Use Case 4: Remote Access to WinCC Archive Databases (RT Professional)](#use-case-4-remote-access-to-wincc-archive-databases-rt-professional)
- [Use Case 5: Local Access to WinCC User Archive (RT Professional)](#use-case-5-local-access-to-wincc-user-archive-rt-professional)
- [Use Case 6: Remote Access to WinCC User Archives (RT Professional)](#use-case-6-remote-access-to-wincc-user-archives-rt-professional)

### Use Case 1: Local Access to WinCC RT Databases (RT Professional)

#### Requirements

The following licenses must be installed on the HMI device:

- WinCC RT Professional

#### Principles

An application uses the WinCC OLE DB-Provider to access the local WinCC Runtime database.

You may locally analyze the archive data and may, for example, calculate the standard deviation of a process value.

![Principles](images/39564871179_DV_resource.Stream@PNG-en-US.png)

### Use Case 2: Remote Access to WinCC RT Databases (RT Professional)

#### Requirements

The following licenses must be installed on the HMI device:

- WinCC RT Professional

The access may take place under various configurations of the Connectivity Pack Client.

- A WinCC software, such as WinCC V12, Web Navigator server or DataMonitor server, is installed on the client computer.   
  The client does not have to be installed explicitly. Licensing is provided through WinCC licenses.

#### Principles

The client accesses the WinCC runtime database of an HMI device with WinCC RT Professional remotely. The client reads the data of the process value archives and alarm logs using the WinCC OLE DB Provider.

Since in this use case, the swapped-out WinCC archive is not accessed, the Archive Connector does not have to connect WinCC archives to an SQL server.

You can display, evaluate or further process the data on the client by exporting it to a CSV file, for example.

![Principles](images/39564976779_DV_resource.Stream@PNG-en-US.png)

### Use Case 3: Local Access to WinCC Archive Databases (RT Professional)

#### Requirements

The HMI device requires the following installations:

- WinCC V12
- WinCC RT Professional

#### Principles

An application accesses the local archive database using WinCC OLE DB Provider. The older archive data are copied from the WinCC RT database to a separate directory on the same computer.

With the Archive Connector, the swapped out WinCC archives are reconnected to an SQL Server. The archives are then available for access using WinCC OLE DB Provider.

Local archive data may be displayed, searched or analyzed, e.g. to search for process errors or to optimize processes.

![Principles](images/39564992779_DV_resource.Stream@PNG-en-US.png)

### Use Case 4: Remote Access to WinCC Archive Databases (RT Professional)

#### Software Requirements

The long-term archive server requires the following to be installed:

- Connectivity Pack Server

Access may take place under various configurations of the client.

- A WinCC software, such as WinCC V12 RT Professional, WinCC V12, Web Navigator server or DataMonitor server, is installed on the client computer.   
  The client does not have to be installed explicitly.

  Licensing is provided through WinCC licenses.

#### Principles

A long-term archive server is used to secure database files of process value and alarm logs, for example, in a monthly backup.

With the Archive Connector, already swapped out WinCC archives can be reconnected to an SQL server. The archives are then available for access using WinCC OLE DB Provider.

The client accesses the archives with the WinCC OLE DB-Provider . Using a VB application, for example, the archives may be analyzed, and process values of a specific day may be displayed.

> **Note**
>
> It may take several minutes if you access alarm logs or swapped out archives with "CC_ExternalBrowsing".

![Principles](images/49596400651_DV_resource.Stream@PNG-en-US.png)

### Use Case 5: Local Access to WinCC User Archive (RT Professional)

#### Requirements

The HMI device requires the following installations:

- WinCC RT Professional

#### Principles

An application accesses the local WinCC user archives with the Microsoft OLE DB Provider.

Using a VB application, for example, you may display, search and write back modified values to local archive data.

![Principles](images/49558251275_DV_resource.Stream@PNG-en-US.png)

### Use Case 6: Remote Access to WinCC User Archives (RT Professional)

#### Requirements

The HMI device requires the following installations:

- WinCC RT Professional

Access may take place under various configurations of the Connectivity Pack Client.

- A WinCC software, such as WinCC RT Professional, Web Navigator server or DataMonitor server, is installed on the client computer.

  The client does not have to be installed explicitly. Licensing is provided through WinCC licenses.

#### Principles

The client accesses the WinCC user archives with the MS OLE DB Provider.

Using a VB application, for example, you may display, search, and write back modified values for archive data.

![Principles](images/39565053579_DV_resource.Stream@PNG-en-US.png)

## Querying the archive data (RT Professional)

This section contains information on the following topics:

- [Displaying Process Value Archives (RT Professional)](#displaying-process-value-archives-rt-professional)
- [Querying Process Value Archives (RT Professional)](#querying-process-value-archives-rt-professional)
- [Querying Alarm Message Archives (RT Professional)](#querying-alarm-message-archives-rt-professional)
- [Displaying Alarm Message Archives (RT Professional)](#displaying-alarm-message-archives-rt-professional)
- [Query for User Archives (RT Professional)](#query-for-user-archives-rt-professional)
- [Configure Access via the Wizard "SQL Server Import/Export" (RT Professional)](#configure-access-via-the-wizard-sql-server-importexport-rt-professional)
- [Meeting prerequisites for using the Reporting Services (RT Professional)](#meeting-prerequisites-for-using-the-reporting-services-rt-professional)
- [Querying the Archive Data (RT Professional)](#querying-the-archive-data-rt-professional-1)
- [Displaying User Archives (RT Professional)](#displaying-user-archives-rt-professional)

### Displaying Process Value Archives (RT Professional)

#### Introduction

The query result is returned as a recordset. The structure of the recordset for process value logs is described in this section.

#### "TAG_EX" extended schematic

To access tags with the following data type, use the extended "TAG_EX" schematic:

- String
- Int64
- UInt64

For compatibility reasons, you can also use "TAG_EX" to access tags that are normally accessed via the "TAG" schematic.

If you use the "TAG" schematic to read String values, the value "0" is returned. As a result, all text tags have the value "0".

#### Recordset structure

"TAG:R" schematic

| Field name | Type | Comment |
| --- | --- | --- |
| ValueID | Integer 4 bytes or  integer 8 bytes | Unique identification of the value.  The length depends on the query type. |
| TimeStamp | DateTime | Time stamp |
| RealValue | Real 8 bytes | Tag value |
| Quality | Integer 4 bytes | QualityCode of the value (e.g. "good" or "bad"). |
| Flags | Integer 4 bytes | Internal control parameter |

"TAG_EX:R" schematic

| Field name | Type | Comment |
| --- | --- | --- |
| ValueID | Integer 4 bytes  or  Integer 8 bytes | Unique identification of the value.  The length depends on the query type. |
| TimeStamp | DateTime | Time stamp |
| TimeStampExt | DateTime | Time stamp of the external device |
| VariantValue | Version 16 bytes | Tag value |
| Bytes | Real 8 bytes | Tag value |
| Quality | Integer 4 bytes | QualityCode of the value (e.g. "good" or "bad"). |
| Flags | Integer 4 bytes | Internal control parameter |

### Querying Process Value Archives (RT Professional)

#### Principle

With the following query, a process value log can be accessed. The data can be selected using filter criteria. The queries are forwarded to the database by the command object.

> **Note**
>
> The length of the ValueID can be different.
>
> - For databases processed on a central archive server (CAS), the ValueID is 8 bytes long and includes a server ID in the HI-DWORD area as well as the ValueID assigned by the respective server in the LO-DWORD area.
> - For all other databases, the ValueID is 4 bytes long and includes only the unique ValueID assigned by the WinCC server.
>
> The 4-byte request via TAG:R is still available for compatibility. The 4-Byte ValueID returned is no longer unique in case of CAS databases.
>
> Queries for process value logs are limited to a maximum of 20 tags, each with a maximum of 128 characters per tag.

#### Syntax

Note that the query may not contain any spaces.

Request of ValueIDs 8 bytes long:

`TAG_LLVID:R,<ValueID or ValueName>,<TimeBegin>,<TimeEnd>[,<SQL_clause>][,<TimeStep>]`

Request of ValueIDs 4 bytes long:

`TAG:R,<ValueID or ValueName>,<TimeBegin>,<TimeEnd>[,<SQL_clause>][,<TimeStep>]`

**"TAG_EX" schematic**

To access process values from the following tag types, use the "TAG_EX:R" schematic:

- Text tag 8-bit character set / 16-bit character set
- Floating-point number 64-bit IEEE 754

Replace "TAG_LLVID:R" with "TAG_LLVID_EX:R".

#### Parameter

| Parameter | Description |  |  |
| --- | --- | --- | --- |
| ValueID | Value ID from the database table   Multiple namings are possible, e.g.,  "TAG:R,(ValueID_1;ValueID_2;ValueID_x),<TimeBegin>,<TimeEnd>" |  |  |
| ValueName | ValueName in format 'ArchiveName\Value_Name'. The <ValueName> parameter must be enclosed in single quotes.   Multiple namings are possible, e.g.,  "TAG:R,('ValueName_1';'ValueName_2';'ValueName_x'), <TimeBegin>,<TimeEnd>"   **Note**   Please not that programming languages such as Visual Basic, VBScript or VBA only allow the following characters in the tag names: "A...Z", "a...z", "0...9" and "_".   In WinCC if you use special characters such as "," or ";" in the tag names then the script will be aborted with an error message. In such a case use the "Tag-ID" to access a tag with special characters in the script name. |  |  |
| TimeBegin | Start time in  'YYYY-MM-DD hh:mm:ss.msc' format  When <TimeStep> is used, <TimeBegin> must be specified as an absolute time. Relative time information or "0000-00-00 00:00:00.000" is not possible. |  |  |
| TimeEnd | End time in  'YYYY-MM-DD hh:mm:ss.msc' format |  |  |
| SQL_Clause | Filter criterion in SQL syntax:  [WHERE search_condition]  [ORDER BY {order_expression [ASC|DESC] } ]   The "ORDER BY" criterion can only be used when the specified sorting order is "{order_expression [ASC|DESC] }".  Example: The following query supplies all values of the "ValueName_1" and "ValueName_2" tags that are less than 50 or greater than 100. "TAG:R,('ValueName_1';'ValueName_2'),<TimeBegin>,<TimeEnd>, 'WHERE RealValue > 100 OR RealValue < 50'" |  |  |
| TimeStep | Values within the specified time interval are collected, beginning with the start time <TimeBegin>   Format: 'TIMESTEP=x,y' x = Interval in seconds  y = Aggregation type, defines the interval result   The following values are possible for aggregation type: |  |  |
| Without interpolation | With interpolation | Meaning |  |
| 1 (FIRST)  2 (LAST)  3 (MIN)  4 (MAX)  5 (AVG)  6 (SUM)  7 (COUNT) | 257 (FIRST_INTERPOLATED)  258 (LAST_INTERPOLATED)  259 (MIN_INTERPOLATED)  260 (MAX_INTERPOLATED)  261 (AVG_INTERPOLATED)  262 (SUM_INTERPOLATED)  263 (COUNT_INTERPOLATED) | First value Last value Minimum value Maximum value Mean value Sum Number of values |  |
| Without interpolation means: If no values are present in the interval, no interval result will be returned.  With interpolation means: If no values are present in the interval, the value will be derived by linear interpolation from the results of the neighboring intervals that are not empty. No extrapolation is done.   Example: When TIMESTEP=60,257, for each interval of 60 seconds, the first value of this interval or - if there are no values in this interval - the linear, interpolated value from the first values of the neighboring intervals are returned.  "TAG:R,1,'2013-07-09 09:03:00.000','0000-00-00 00:10:00.000','TIMESTEP=60,257'" |  |  |  |

> **Note**
>
> <TimeBegin> and <TimeEnd> must not both be "ZERO" = '0000-00-00 00:00:00.000'.
>
> In order to improve performance, use the parameter "ValueID" instead of "ValueName" in the query. You can determine the "ValueID" from the "Archives" table.
>
> Some applications cannot resolve the time of process values into 1 ms increments, which can lead to inaccuracies.   
> An example of resolving the milliseconds from the time stamp of process values can be found in the VB script "SplitDateTimeAndMs" in section "Example: Reading process value log using the WinCC OLE DB provider". The script is also implemented in the demo project "OpConPack".

#### Selection of an Absolute Time Interval

Reads from start time <TimeBegin> to end time <TimeEnd>.

**Example A1:**

Reads the values of the ValueID 1 from start time 9:03 hours to end time 9:10 hours.

`"TAG:R,1,'2013-07-09 09:03:00.000','2013-07-09 09:10:00.000'"`

#### Selection of a Relative Time Interval

Reads from beginning of recording:

`<TimeBegin> = '0000-00-00 00:00:00.000'`

Reads until end of recording:

`<TimeEnd> = '0000-00-00 00:00:00.000'`

<TimeBegin> and <TimeEnd> must not both be "ZERO" = '0000-00-00 00:00:00.000'.

> **Note**
>
> Enter a relative period you want to query in a linked archive database using the following format:
>
> - 0000-00-DD hh:mm:ss.msc
>
> If you indicate the time frame in months, the content can be faulty, because a month can have 28 to 31 days.

**Example B1:**

Reads the absolute time from "TimeBegin" to end of recording, i.e. the last archived value.

`<TimeBegin> = '2013-02-02 12:00:00.000', <TimeEnd> = '0000-00-00 00:00:00.000'`

**Example B2:**

Reads the absolute time from "TimeBegin" for the next 10 seconds.

`<TimeBegin> = '2013-02-02 12:00:00.000', <TimeEnd> = '0000-00-00 00:00:10.000'`

**Example B3:**

Reads 10 seconds backward from the absolute time from "TimeEnd".

`<TimeBegin> = '0000-00-00 00:00:10.000', <TimeEnd> = '2013-02-02 12:00:00.000'`

**Example B4:**

Reads the values of the last hour starting from the time of the last archived value for multiple valueIDs (1;3;5;6).

`"TAG:R,(1;3;5;6),'0000-00-00 01:00:00.000','0000-00-00 00:00:00.000'"`

**Example B5:**

Reads the values of the last five minutes starting from the time of the last archived value for "TAG_2" from the "ArTags" archive.

`"TAG:R,'ArTags\TAG_2','0000-00-00 00:05:00.000','0000-00-00 00:00:00.000'"`

The following diagrams shows a possible result of this example. The query was implemented using the Connectivity Pack Demo Project.

![Selection of a Relative Time Interval](images/2548248203_DV_resource.Stream@PNG-en-US..png)

#### Multiple Return Values to a Query Using a Filter on Tag Value

**Example C1:**

The following query also uses the <SQL_Clause> parameter and returns all tag values that have the ValueID "3" and "6" and are below 50 or above 100.

`"TAG:R,(3;6),<TimeBegin>,<TimeEnd>,'WHERE RealValue > 100 OR RealValue < 50'"`

#### Query with parameter <TimeStep>

**Example C2:**

The following query uses the <TimeStep> parameter and returns all values of ValueID "1" - starting from start time "TimeBegin" till 5 minutes later in intervals of "60" seconds with the aggregation type "5" = "Mean value without interpolation".

`"TAG:R,1,'2004-10-13 17:00:00.000','0000-00-00 00:05:00.000', 'TIMESTEP=60,5'"`

The following diagram shows the query result. The left table displays the archive data which were archived in an archiving cycle of 30 seconds. The right table displays the query result. It determines the average between two archive values at "0" seconds and "30" seconds, displayed with the first time stamp of the averaging interval, i.e. second "0".

![Query with parameter <TimeStep>](images/2548255755_DV_resource.Stream@PNG-en-US..png)

**Example C3:**

The following query uses the <TimeStep> parameter and returns all values of ValueID "1" and "2" - starting from start time "TimeBegin" till 2 minutes later in intervals of "15" seconds with the aggregation type "261" = "Mean value with linear interpolation".

`"TAG:R,(1;2),'2004-10-13 17:00:00.000','0000-00-00 00:02:00.000', 'TIMESTEP=15,261'"`

The following diagram shows the query result. The left table displays the archive data which were archived in an archiving cycle of 30 seconds. The right table displays the query result. The archive values at "0" and "30" seconds are displayed in the query result unchanged with their time stamp. For second "15," the linear, interpolated value is formed of archive values at seconds "0" and "30". For the "45" second, the linear, interpolated value is taken from the archive values of "30" second of the same minute and the "0" second of the next minute.

![Query with parameter <TimeStep>](images/2548263307_DV_resource.Stream@PNG-en-US..png)

### Querying Alarm Message Archives (RT Professional)

#### Introduction

With the following query, an alarm message archive can be accessed. The data can be selected using filter criteria. The queries are forwarded to the database by the command object.

You will find information about status of messages in the WinCC Information System under "Working with WinCC > ANSI-C Function for Creation of Functions and Actions > ANSI-C Function descriptions > Appendix > Structure Definitions > Structure Definition MSG_RTDATA_STRUCT".

When querying message archives, the result is summarized by archive, but without sorting the queried archive segments. The filter condition needs to be extended accordingly if the segments are to be sorted, e.g., for the chronological sorting "ORDER BY DateTime ASC, MS ASC".

#### Syntax

`ALARMVIEW:SELECT * FROM <ViewName>[WHERE <Condition>...., optional]`

#### Parameter

| Parameter | Description |
| --- | --- |
| ViewName | Name of the database table. The table has to be specified in the desired language. The "ViewName" for the five European language is e.g.:  ALGVIEWDEU: German alarm message archive data ALGVIEWENU: English alarm message archive data ALGVIEWESP: Spanish alarm message archive data ALGVIEWFRA: French alarm message archive data ALGVIEWITA: Italian alarm message archive data  The "ViewName" for the Asian language is e.g.:  ALGVIEWCHT: Chinese (simplified) alarm message archive data ALGVIEWCHT: Chinese (traditional) alarm message archive data ALGVIEWJPN: Japanese alarm message archive data ALGVIEWKOR: Korean message archive data  Note  The languages that are installed in the WinCC base system or that are configured in the WinCC Text Library are supported. Information concerning the possible query-languages or the respective "ViewName" can be found in the SQL-Server in the linked alarm archives under "Views". All languages that are supported in the corresponding archive are shown with their IDs e.g. "GENVIEWENU" here. |
| Condition | Filter criterion, e.g.: DateTime>'2003-06-01' AND DateTime<'2003-07-01' DateTime>'2003-06-01 17:30:00' MsgNr = 5 MsgNr in (4, 5) State = 2  With DateTime, only absolute time indications can be used. |

Example 1:   
Reads all entries of message no. 5 that were captured after July 5, 2003.

`"ALARMVIEW:SELECT * FROM ALGVIEWENU WHERE MsgNr = 5 AND DateTime>'2003-07-05'"`

Example 2:   
Reads all messages with the time stamp between July 3, 2003 and July 5, 2003.

`"ALARMVIEW:SELECT * FROM ALGVIEWENU WHERE DateTime>'2003-07-03' AND DateTime<'2003-07-05'"`

The following picture shows a possible result of this example. The query was implemented using the Connectivity Pack Demo Project.

![Parameter](images/2548270859_DV_resource.Stream@PNG-en-US..png)

### Displaying Alarm Message Archives (RT Professional)

#### Introduction

The query result is returned as the Recordset. In this chapter, the structure of the Recordset for alarm log archives is described.

You will find information about status of messages in the WinCC Information System under "Working with WinCC > ANSI-C Function for Creation of Functions and Actions > ANSI-C Function descriptions > Appendix > Structure Definitions > Structure Definition MSG_RTDATA_STRUCT".

#### Recordset Structure

| Location | Field name | Type | Comments |
| --- | --- | --- | --- |
| 1 | MsgNo | Integer 4 Bytes | Message number |
| 2 | State | Small Integer 2 Bytes | Alarm Log Status |
| 3 | DateTime | DateTime 8 Bytes | Time stamp of the message (date/time without milliseconds) |
| 4 | Ms | Small Integer 2 Bytes | Time stamp of the message (milliseconds) |
| 5 | Instance | VarChar (255) | Instance Name of the Alarm Log |
| 6 | Flags1 | Integer 4 Bytes | (only for internal use) |
| 7 | PValueUsed | Integer 4 Bytes | Process Values used |
| 8 to 17 | PValue1 to PValue10 | Real 8 Bytes | Numerical Process Value 1 to 10 |
| 18 to 27 | PText1 to PText10 | VarChar (255) | Process Value Text 1 to 10 |
| 28 | ComputerName | VarChar (255) | Name of computer |
| 29 | Application | VarChar (255) | Application Name |
| 30 | Comment | VarChar (255) | Comments |
| 31 | UserName | VarChar (255) | User name |
| 32 | Counter | Integer 4 Bytes | Running Alarm Message Counter |
| 33 | TimeDiff | Integer 4 Bytes | Time difference to "Came in" status |
| 34 | ClassName | VarChar (255) | Name of the message class |
| 35 | Typename | VarChar (255) | Name of the message type |
| 36 | Class | Small Integer 2 Bytes | Message class ID |
| 37 | Type | Small Integer 2 Bytes | Message type ID |
| 38 to 47 | Text1 to Text10 | VarChar (255) | Message Text 1 to 10 |
| 48 | AG_NR | Small Integer 2 Bytes | Number of the PLC |
| 49 | CPU_NR | Small Integer 2 Bytes | Number of the CPU |
| 50 | CrComeFore | Integer 4 Bytes | Foreground Color for the "Came in" Status |
| 51 | CrComeBack | Integer 4 Bytes | Background Color for the "Came in" Status |
| 52 | CrGoFore | Integer 4 Bytes | Foreground Color for the "Went out" Status |
| 53 | CrGoBack | Integer 4 Bytes | Background Color for the "Went out" Status |
| 54 | CrAckFore | Integer 4 Bytes | Foreground Color for the "Acknowledged" Status |
| 55 | CrAckBack | Integer 4 Bytes | Background Color for the "Acknowledged" Status |
| 56 | LocaIID | Integer 4 Bytes | Location of the Alarm |
| 57 | Priority | Integer 4 Bytes | Priority |
| 58 | AP_type | Integer 4 Bytes | Loop in Alarm |
| 59 | AP_name | VarChar (255) | Loop-in-Alarm Function Name |
| 60 | AP_PAR | VarChar (255) | Loop-in-Alarm Screen |
| 61 | InfoText | VarChar (255) | Infotext |
| 62 | TxtCame | VarChar (255) | Text came in |
| 63 | TxtWent | VarChar (255) | Text went out |
| 64 | TxtCameNWent | VarChar (255) | Text came in and went out |
| 65 | TxtAck | VarChar (255) | Text acknowledged |
| 66 | AlarmTag | Integer 4 Bytes | Message tag |
| 67 | AckType | Small Integer 2 Bytes | Acknowledgment Type |
| 68 | Params | Integer 4 Bytes | Parameter |
| 69 | Servername | VarChar (255) | Servername |

### Query for User Archives (RT Professional)

#### Introduction

With the following query, you may use MS OLE DB Provider to access WinCC user archives. Access may be read or write enabled in order to analyze the saved data and to modify and save same.

The data can be selected using filter criteria. The queries are forwarded to the database by the command object.

> **Note**
>
> Consider the following when accessing WinCC user archives via the MS OLE DB Provider:
>
> - Ensure that the write access is not enabled simultaneously via the MS OLE DB Provider and WinCC. This prevents inconsistencies in the archives.
> - Changes via MS OLE DB Provider will not be displayed in WinCC Runtime until the user archive table controls are selected by a picture change. The current data of the user archives are read again.
> - User archives changed via MS OLE DB Provider are not synchronized in a redundant system.
> - Note that WinCC updates can cause changes in the database scheme. The scheme can also be changed by the installation of hot fixes and service packs. In this case, you must adapt the read and write access accordingly.

#### Syntax

**Reading of Values**

`SELECT * FROM UA#<ArchiveName>[WHERE <Condition>...., optional]`

**Writing of Values**

`UPDATE UA#<ArchiveName> SET UA#<ArchiveName>.<Column_n> = <Value> [WHERE <Condition>...., optional]`

**Inserting a Data Set**

`INSERT INTO UA#<ArchiveName> (ID,<Column_1>,<Column_2>,<Column_n>) VALUES (<ID_Value>, Value_1,Value_2,Value_n)`

**Deleting a Data Set**

`DELETE FROM UA#<ArchiveName> WHERE ID = <ID_Number>`

#### Parameter

| Parameter | Description |
| --- | --- |
| ArchiveName | Name of the user archive. |
| Condition | Filter criterion e.g.: LastAccess>'2004-06-01' AND LastAccess<'2004-07-01' DateTime>'2004-06-01 17:30:00' ID = 5 ID > 3 |

Example 1:   
Reads all data in the user archive "Test".

`SELECT * FROM UA#Test`

Example 2:   
Reads all data in the user archive "Test" that were changed between June 1, 2004 and July 1, 2004.

`SELECT * FROM UA#Test WHERE LastAccess>'2004-06-01' AND LastAccess<'2004-07-01'`

Example 3:   
Enters the value 'New_String' in the field F_STRING of the ID 3.

`UPDATE UA#TEST SET F_STRING = 'New_String' WHERE ID = 3`

Example 4:   
Inserts a data set with the ID 100.

`INSERT INTO UA#Test (ID,F_Integer,F_Float,F_Double,F_String) VALUES (100.10,'10.0','AAAA')`

Example 5:   
Deletes the data set with the ID 100.

`DELETE FROM UA#Test WHERE ID = 100`

### Configure Access via the Wizard "SQL Server Import/Export" (RT Professional)

#### Introduction

WinCC OLE DB Provider may be used to access WinCC databases while employing the Wizard "SQL Server Import/Export. You can save the unzipped files to an intermediate database using the wizard; you access the database with standard SQL queries.

- Using WinCC computers, access to runtime and archive databases may be established locally or remotely.
- In the case of long-term archive servers, local or remote access is only possible to the archive databases since they have no runtime databases.

#### Procedure

1. Start the "SQL Server Management Studio" and select the desired database.
2. In the shortcut menu of the database select "Tasks > Export Date...".

   The SQL Server Import/Export-Wizard opens.
3. Configure the data source.   
   Click "Next". In the field Data source, select the entry WinCC OLE DB-Provider for Archives". Click the button "Properties...". The "Data Link Properties" dialog box opens.
4. Configure the correct Provider settings.  
   In the field "Data Source" enter the following text as data source: ".\WinCC"The entry for "Location" remains empty.   
   Under "Enter the initial catalog to use" either enter the desired Runtime database or the symbolic name, which was configured in "Archive Connector Tool". The correct spelling of the name may be found in "SQL Server Management Studio" in the "Databases" directory. Alternatively you can also enter the database "CC_ExternalBrowsing" for Runtime data and Archive data.  
   Click the "Advanced" tab. For the Property "Connect timeout" select the desired time in seconds. In the property "Access permissions" only select the box "ReadWrite".   
   Close the dialog by activating the "OK" button.
5. Configure the data source.   
   Click "Next". In the field "Destination", select the entry SQL Native Client" for example. The server name can be any SQL Server instance. The database name which you enter in the field "Database", can be any self-created target database.
6. Configure the query conditions.  
   Click "Next". Select "Write a query to specify the data to transfer". Click "Next". Enter the desired query conditions. With the query "Tag:R,1,'0000-00-00 00:10:00.000','0000-00-00 00:00:00.000'' of the ValueID "1", for example, the values of the last ten minutes of the archiving are read. Additional information on the syntax may be found in Chapter "Query for Process Value Archives".
7. End the Wizard and export the data.  
   Click "Next" and on the last page of the Wizard click on "Finish". The Wizard executes the data export to the target database. If the data export was successful, the comprised data in the target database are saved in the newly created table"dbo.Query". You can change the table name. If you do not change the table name, data will be overwritten with a new export. New tables with names "Query1", "Query2" etc. are created by the wizard.

**Note**

In order to improve performance during local access, enter " <Computer Name>\WinCC" in the field "Data Source" instead of ".\WinCC".

**Note**

Leave the "Database" field empty. No target tables are then created.

### Meeting prerequisites for using the Reporting Services (RT Professional)

#### Introduction

With WinCC you can use the Reporting Services of SQL Server. You can therefore make reports with log data created with Microsoft Visual Studio available in the network.

#### Requirements

The use of the Reporting Services with WinCC calls for the following additional software requirements:

- Internet Information Services
- Reporting Services of MS SQL Server

  > **Note**
  >
  > Perform the installation steps in exactly the order specified.

#### Installing the Information Services

1. Select "Settings > Control Panel > Software".
2. Click on the "Add/Remove Windows Components" button on the left.
3. Select the check box "Internet Information Services (IIS)" in the "Windows Components Wizard" dialog.

#### Installing Reporting Services of MS SQL Server

You install the Reporting Services from the WinCC-DVD or its location in the file system.

1. Select "Settings > Control Panel > Programs and Features".
2. Select an older version of "Microsoft SQL Server " (if available) and click on "Uninstall/Change".
3. Select "Add" and select the path "InstData > SQL > SQL..STD > setup" in the WinCC setup.

   The Microsoft SQL Server Installation Wizard is automatically opened. Follow the instructions.
4. Under "Installation Type" select the option "Add features to an existing instance of SQL Server" and the instance "WINCC".

   The management tools and therefore also the SQL Server Data Tools are already installed.
5. Activate "Reporting Services - Native" and follow the instructions.

   The Reporting Services will be installed.
6. Start the Reporting Services Configuration Manager and configure the Reporting Services.

#### Configuring Internet Information Services

1. Open Computer Management.
2. Under "Services and Applications" select the "Internet Information services (IIS) Manager".
3. Open the feature "Authentication" and select the entry "Edit" in the shortcut menu of "Anonymous authentication".
4. Select the option "Specific user" and enter the user name and password.

   The user name has the following format: <domain or computer name>\<user>

> **Note**
>
> We recommend you to restart your computer following installation.

#### Result

The requirements for using the Reporting Services are now created. You can now create reports and make them available on the Internet.

### Querying the Archive Data (RT Professional)

#### Introduction

The queries are forwarded to the database by the command object. An important parameter, aside from "ConnectionString", is CommandText. The CommandText transmits the query. The result is returned as the Recordset.

> **Note**
>
> **Time range for archive inquiries for message and process values**
>
> If the query for message or process value archives specifies a time range for which no messages or other values exist within the archives, no information message or other status display occurs. If this status is to be displayed, error handling must be implemented by the user.
>
> A simple version of this error handling routine is described in the sample script under the topic "Example: Reading message archive data via the WinCC OLE DB Provider".

In the following examples, a command object each is generated and the query transmitted as CommandText.

In the following structure examples, CommandText also includes the ConnectionString whose structure is described under "Establishing Connection to Archive Database".

#### Structure of CommandText

**Process Value Archives:**

`Set oRs = CreateObject("ADODB.Recordset")`

`Set oCom = CreateObject("ADODB.Command")`

`oCom.CommandType = 1`

`Set oCom.ActiveConnection = conn`

`oCom.CommandText = "TAG:R,'PVArchive\Tag1','0000-00-00 00:10:00.000','0000-00-00 00:00:00.000'"`

**Alarm Message Archives:**

`Set oRs = CreateObject("ADODB.Recordset")`

`Set oCom = CreateObject("ADODB.Command")`

`oCom.CommandType = 1`

`Set oCom.ActiveConnection = conn`

`oCom.CommandText = "ALARMVIEW:Select * FROM AlgViewEnu"`

**User archives**

`Set oRs = CreateObject("ADODB.Recordset")`

`Set oCom = CreateObject("ADODB.Command")`

`oCom.CommandType = 1`

`Set oCom.ActiveConnection = conn`

`oCom.CommandText = "SELECT * FROM UA#Test"`

#### Specifying the Recordset location

To specify the location of Recordset for query of the archive data, you need to set the value "3" for the "CursorLocation" property, for example, "conn.CursorLocation = 3". The Recordset is created on the client.

### Displaying User Archives (RT Professional)

#### Introduction

Each user archive consists of data fields with editable properties. Each data field has properties such as name, alias name, type, lengths, value etc. The representation of the data fields and properties in the Editor User Archives is done in lines and columns. Therefore, we are talking of rows instead of data fields and of columns instead of properties.

In the following, the user archive "Test" is described as a structure example. This user archive is included in the Connectivity Pack Demo Project "OPConPack" in directory "\Samples\Connectivity Pack\DemoProject."

#### Structure of User Archive "Test"

| Field Name | Type | Comment |
| --- | --- | --- |
| ID | Integer | Unique identification of Value. |
| F_Integer | Integer | Example for Value |
| F_Float | Float | Example for Value |
| F_Double | Double | Example for Value |
| F_String | String | Sample character sequence |

## Analysis functions for messages and process values (RT Professional)

This section contains information on the following topics:

- [Analysis Functions for Messages and Process Values (RT Professional)](#analysis-functions-for-messages-and-process-values-rt-professional-1)
- [Display of Message Archives for Analysis Queries (RT Professional)](#display-of-message-archives-for-analysis-queries-rt-professional)

### Analysis Functions for Messages and Process Values (RT Professional)

#### Introduction

Different analysis functions are available with WinCC for querying archived messages and process values.

The analysis is triggered by a query with parameters for different aggregate functions. Calculation of the aggregate function is performed on the Connectivity Pack server, and only the result is transferred to the client.

Additional information on CommandText and ConnectionString which are used in the following examples may be found under "Establishing Connection to Archive Database" and "Querying Archive Data".

#### Analysis Functions for Messages

The analysis query for alarm logs archives returns a specific recordset which contains configuration and runtime data for each message as well as results of the aggregate functions.

The returned recordset for analysis queries of alarm logs is not identical to the recordset of normal queries of message archives. Additional information may be found in the section "Display of Alarm Logs for Analysis Queries".

For each message, the following aggregate functions are calculated. The column descriptions of the result list are placed in parenthesis.

- Sum of message frequency ("FreqOfAlarm")
- Cumulative duration from "Message Incoming" until "Message Outgoing" ("CumDurationComeGo")
- Average duration from "Message Incoming" until "Message Outgoing" ("AvDurationComeGo")
- Cumulative duration from "Message Incoming" until initial acknowledgment ("CumDurationComeAckn1")
- Average duration from "Message Incoming" until initial acknowledgment ("AvDurationComeAckn1")
- Cumulative duration from "Message Incoming" until second acknowledgment ("CumDurationComeAckn2")
- Average duration from "Message Incoming" until second acknowledgment ("AvDurationComeAckn2")
- Cumulative duration from "Message Incoming" until "Message Incoming" ("CumDurationComeGo")
- Average duration from "Message Incoming" until "Message Incoming" ("AvDurationComeCome")

> **Note**
>
> **"String" data type is not supported**
>
> If you use these functions for the "String" data type, the analysis function returns the result "0".

**Syntax**

For the calculation of aggregate functions for messages, the following command is issued to WinCC OLE DB Provider.

`"AlarmHitView: SELECT * FROM <ViewName>[WHERE <Condition>]"`

Here:  
<ViewName> = Name of the database table in the desired language, e.g. ALGVIEWMENU for English.   
[WHERE <Condition>] = optional filter criterion as WHERE condition in the SQL syntax.

Additional information on the syntax of parameters may be found in the section "Query for Alarm Logs".

**Example**

The example provides results of the aggregate functions for all messages for the time range between 7/15/2004 12:00 p.m. and 12:15 p.m. from the "ALGVIEWENU" database.

ConnectionString:

`"Provider=WinCCOLEDBProvider.1;Catalog=CC_OpenArch_03_05_27_14_11_46R;Data Source=.\WinCC"`

CommandText:

`"AlarmHitView: SELECT * FROM ALGVIEWENU WHERE DateTime>'2004-07-15 12:00:00' AND DateTime<'2004-07-15 12:15:00'"`

#### Analysis Functions for Process Values

The analysis of process values returns the result of an aggregate function. Only one aggregate function can be calculated in a query.

The following aggregate functions are available for process values.

- MIN (minimum)
- MAX (maximum)
- AVG (average)
- SUM (sum of all values)
- COUNT (count of process values)
- COUNTER (number of entries with value "1", e.g., query of binary tags)
- STDEV (statistical standard deviation)
- VAR (statistical variance)

> **Note**
>
> **Text tags are not supported**
>
> In a query for text tags (8-bit character set / 16-bit character set) via TAG_EX:R, the analysis function returns the result "0".

**Syntax**

For the calculation of aggregate functions for process values, a query is issued to the MS SQL OLE DB Provider and the procedure "cp_TagStatistic" from database "SQL Server Master" is executed.

> **Note**
>
> The analysis functions for process values in transparent access function only with Connectivity Station on a client with own project.

The following parameters are transferred to the "cp_TagStatistic" procedure.

`cp_TagStatistic @P1,@P2,@P3[,@P4]`

Where:  
"@P1" = database name (e.g. WinCC Runtime database or symbolic name of the directory with the swapped out archives). For transparent access, use the WinCC project name instead of the database name.  
"@P2" = WinCC OLE DB-Provider String for process values.   
"@P3" = desired aggregate function.  
"@P4" = <Symbolic computer name>::\WinCC (required only for transparent access).

Additional information on the syntax of parameters "@P1" and "@P2" may be found in the section "Query for Process Value Archives".

> **Note**
>
> **Analysis functions for process values with Asian archive tag names**
>
> If you use archive tag names with Asian character sets to calculate an analysis function, the request for Unicode character sets has to be adapted.
>
> Add the prefix "N'" in front of both parameters.
>
> Example: cp_TagStatistic N'TestDB',N'TAG:R,17,''2004-05-17 12:00:00'',''2004-05-17 13:00:00''','AVG'

**Example**

This query will return the average of process values in the time range between 5/17/2004 12:00 and 13:00 for ValueID "17" from database "TestDB".

ConnectionString:

`"Provider=SQLNCLI11;Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=master ;Data Source=.\WinCC"`

CommandText:

`"cp_TagStatistic 'TestDB','TAG:R,17,''2004-05-17 12:00:00'',''2004-05-17 13:00:00''','AVG'"`

**Example of transparent access**

This query delivers the average process value in the time range between 14.09.2006 10:00 hrs and 11:00 hrs for the ValueID "7" from the "WinCCProj".

ConnectionString:

`"Provider=SQLNCLI11;Integrated Security=SSPI;Persist Security Info=False;Initial Catalog=master ;Data Source=.\WinCC"`

CommandText:

`"cp_TagStatistic 'WinCCProj','TAG:R,7,''2006-09-14 10:00:00'',''2006-09-14 11:00:00''','AVG','Symb_WinCCProj::\WinCC'"`

### Display of Message Archives for Analysis Queries (RT Professional)

#### Introduction

The analysis query for message archives returns a specific recordset which contains configuration and runtime data for each message as well as results of the aggregate functions.   
This Recordset is not identical to the Recordset of normal queries of message archives.

#### Recordset Structure for Analysis of Message Archives

Upon query of message archives using the analysis function "AlarmHitView", the result is returned as recordset with the following structure.

| Location | Field name | Type | Comments |
| --- | --- | --- | --- |
| 1 | MsgNo | Integer 4 Bytes | Message number |
| 2 | State | Small Integer 2 Bytes | Alarm Log Status |
| 3 | DateTime | DateTime 8 Bytes | Time stamp of the message (date/time without milliseconds) |
| 4 | Ms | Small Integer 2 Bytes | Time stamp of the message (milliseconds) |
| 5 | Instance | VarChar (255) | Instance Name of the Alarm Log |
| 6 | Flags1 | Integer 4 Bytes | (only for internal use) |
| 7 | Counter | Integer 4 Bytes | Running Alarm Message Counter |
| 8 | TimeDiff | Integer 4 Bytes | Time difference to "Came in" status |
| 9 | ClassName | VarChar (255) | Name of the message class. |
| 10 | Typename | VarChar (255) | Name of the message type. |
| 11 | Class | Small Integer 2 Bytes | Message class ID |
| 12 | Type | Small Integer 2 Bytes | Message type ID |
| 13 to 22 | Text1 to Text10 | VarChar (255) | Message Text 1 to 10 |
| 23 | AG_NR | Small Integer 2 Bytes | Number of the PLC |
| 24 | CPU_NR | Small Integer 2 Bytes | Number of the CPU |
| 25 | CrComeFore | Integer 4 Bytes | Foreground Color for the "Came in" Status |
| 26 | CrComeBack | Integer 4 Bytes | Background Color for the "Came in" Status |
| 27 | CrGoFore | Integer 4 Bytes | Foreground Color for the "Went out" Status |
| 28 | CrGoBack | Integer 4 Bytes | Background Color for the "Went out" Status |
| 29 | CrAckFore | Integer 4 Bytes | Foreground Color for the "Acknowledged" Status |
| 30 | CrAckBack | Integer 4 Bytes | Background Color for the "Acknowledged" Status |
| 31 | Priority | Integer 4 Bytes | Priority |
| 32 | AP_type | Integer 4 Bytes | Loop in Alarm |
| 33 | AP_name | VarChar (255) | Loop-in-Alarm Function Name |
| 34 | AP_PAR | VarChar (255) | Loop-in-Alarm Screen |
| 35 | InfoText | VarChar (255) | Infotext |
| 36 | TxtCame | VarChar (255) | Text came in |
| 37 | TxtWent | VarChar (255) | Text went out |
| 38 | TxtCameNWent | VarChar (255) | Text came in and went out |
| 39 | TxtAck | VarChar (255) | Text acknowledged |
| 40 | AckType | Small Integer 2 Bytes | Acknowledgment Type |
| 41 | FreqOfAlarm | Integer 4 Bytes | Sum of message frequency |
| 42 | CumDurationComeGo | Integer 4 Bytes | Cumulative duration from "Message Came In" until "Message Went Out" |
| 43 | AvDurationComeGo | Real 8 Bytes | Average duration from "Message Came In" until "Message Went Out" |
| 44 | CumDurationComeAckn1 | Integer 4 Bytes | Cumulative duration from "Message Came In" until initial acknowledgment |
| 45 | AvDurationComeAckn1 | Real 8 Bytes | Average duration from "Message Came In" until initial acknowledgment |
| 46 | CumDurationComeAckn2 | Integer 4 Bytes | Cumulative duration from "Message Came In" until second acknowledgment |
| 47 | AvDurationComeAckn2 | Real 8 Bytes | Average duration from "Message Came In" until second acknowledgment |
| 48 | CumDuration ComeCome | Integer 4 Bytes | Cumulative duration from "Message Came In" until "Message Came In" |
| 49 | AvDurationComeCome | Real 8 Bytes | Average duration from "Message Came In" until "Message Came In" |

## Bases of OLE DB (RT Professional)

### Introduction

Using the OLE DB interface and the associated database provider supplied by WinCC, you have access to process value and message archives.

### OLE DB

OLE DB is an open standard for a fast access to different databases. It is irrelevant whether the database is relational or not.

The connection between the OLE DB level and the database is established through a database provider.

OLE DB interfaces and providers are offered from various manufacturers.

### WinCC OLE DB Provider

Using WinCC OLE DB Provider, you may directly access WinCC archive data stored in the MS SQL server database. Depending on the configuration, process data of WinCC are stored in compressed form. WinCC OLE DB Provider permits transparent access even to these data.

![WinCC OLE DB Provider](images/39564976779_DV_resource.Stream@PNG-en-US.png)

### Microsoft OLE DB

Microsoft OLE DB only provides access to WinCC user archives.

Access to WinCC User Archives using Microsoft OLE DB requires a Connectivity Pack license on the computer where the WinCC user archives will be accessed. A WinCC Client Access License is required for remote access to the MS SQL Server database.

As protection from unauthorized access using MS OLE DB, the administrator of the databases can take appropriate actions. Additional information may be found in Chapter "Security Settings for Access to SQL Databases Using MS OLE DB".

> **Note**
>
> Microsoft OLE DB is only tested and released for access to WinCC user archives but not to alarm and process value archives.   
> Use the WinCC OLE DB Provider to access message and process value archives.

## WinCC OLE DB Provider (RT Professional)

### Introduction

The WinCC OLE DB Provider makes access to the process value and alarm archives possible.

The WinCC OLE DB Provider also provides analysis functions, such as minimum, maximum of archive tags.

### Access to archive data

Access to archive data can take place under different constellations:

### Simultaneous access to archive and Runtime databases

The function "ArchiveMonitor" combines the data of the Runtime and archive databases of the activated WinCC project in an SQL database.

The SQL database is called "CC_ExternalBrowsing" and creates the views "AMT" and "ARCHIVE".

The views provide all necessary information for the WinCC OLE DB Provider.

Because these views provide all the necessary information for the WinCC OLE DB Provider, the "CC_ExternalBrowsing" database can be used as a data source for the provider.

On deactivating WinCC runtime, views additionally created in "CC_ExternalBrowsing" are deleted once again.

Because a long-term archive server does not contain any runtime databases, access to the archive databases using the "CC_ExternalBrowsing" database is not possible.

### WinCC OLE DB Provider as a "Linked Server"

> **Note**
>
> When configuring WinCC OLE DB Provider as a "Linked Server", the "WinCC OLE DB-Provider for Archives" entry must be selected in the "Provider Name" field of the ""Linked Server Properties" dialog.
>
> Activate the "AllowInProcess" check box in the "Provider Options" dialog.   
> Additional information is available here: "SQL Server Books Online" under "Configuring OLE DB Providers for Distributed Queries".

The WinCC OLE DB Provider can be registered in the SQL server in the list of "Linked Servers". Regardless if the database is stored locally or remote .

Example:

WinCC OLE DB Provider as a Linked Server with the server name "WinCC":

select min(realvalue) from openquery(WINCC,'Tag:R,1,''0000-00-00 00:01:00.000'',''0000-00-00 00:00:00.000''')

select * from openquery(WINCC,'Tag:R,1,''0000-00-00 00:01:00.000'',''0000-00-00 00:00:00.000''')

## Installation (RT Professional)

### Installation of WinCC OLE DB-Provider

The WinCC OLE DB-Provider is automatically installed along with WinCC.

The WinCC OLE DB Provider is available for the following systems after installation of WinCC:

- Engineering station with WinCC
- HMI device with WinCC Runtime Professional

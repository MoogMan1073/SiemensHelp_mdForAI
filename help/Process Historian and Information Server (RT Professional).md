---
title: "Process Historian and Information Server (RT Professional)"
package: ProcHistWCCPenUS
topics: 7
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Process Historian and Information Server (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Configuration in TIA Portal (RT Professional)](#configuration-in-tia-portal-rt-professional)

## Basics (RT Professional)

This section contains information on the following topics:

- [Process Historian (RT Professional)](#process-historian-rt-professional)
- [Information Server (RT Professional)](#information-server-rt-professional)

### Process Historian (RT Professional)

#### Introduction

SIMATIC Process Historian is a central logging system for storing process data such as process values and alarms. The Process Historian uses the Microsoft SQL Server 2014 64 Bit and logs historical data originating from a Runtime Professional.

#### Services

Process Historian employs four services for processing, storing and backing up data:

- SIMATIC Process Historian Server

  This service implements all functions the server needs to process and store data.
- Process Historian Maintenance Service

  This service implements all functions that are necessary to maintain the Process Historian database. Process Historian Maintenance Service handles tasks such as starting mirroring, mirror monitoring, restore functions, maintenance of the transaction log, etc.
- Process Historian Redundancy Service

  This service implements functions that are necessary for data exchange between two redundant server systems.
- Process Historian Discovery Service

  This service supports the search for connected Process Historian systems. The Discovery Service is essential for the functionality of the Process Historian.

#### Working with the Process Historian

The Process Historian is not installed with the TIA Portal; it must be purchased separately.

You can find more information on the license and technical data here:

[Process Historian](http://w3.siemens.com/mcms/human-machine-interface/en/visualization-software/scada/wincc-options/simatic-process-historian/Pages/Default.aspx)

### Information Server (RT Professional)

The SIMATIC Information Server can be used to compile, evaluate and graphically visualize the process values, messages and recipe data of a process control system. You can access the web application of the Information Server with Internet Explorer. You also use the web interface to administer the Information Server.

The Information Server may be installed on a separate PC. The Information Server gives you remote access to (archived) data of the Process Historian. A network connection is required for access.

#### Access rights

When you are connected to a Process Historian, you can access the archived data of projects for which you have been granted access rights.

These access rights are linked to the corresponding projects.

The access rights for data used in the Information Server are linked to the folders in which the data is stored. All users may access the "Public" folder. Data stored in the "Private" folder is only available to the user logged on at given time.

#### Reporting

The Information Server can visualize the queried data in various forms. The selected report templates are displayed in user-defined page layouts.

Select a report template to create a report.

You can parameterize a report template, for example, by selecting a tag that contains the start and end time of the necessary monitoring period. The parameters you set define the report content.

The selected report template determines the way the queried information is displayed. The results of the respective query are visualized in the report as tables or charts.

The Information Server provides report templates for the following data:

- Process values
- Messages
- Recipe data

You can output and export reports as Word, Excel, PowerPoint and/or PDF files.

The reports and report templates are created by means of the web application or Office add-ins. Use the same report templates in both applications.

#### Working with the Information Server

The Information Serveris not installed with the TIA Portal; it must be purchased separately.

You can find more information on the license and technical data here:

[Information Server](http://w3.siemens.com/mcms/human-machine-interface/en/visualization-software/scada/wincc-options/simatic-information-server/Pages/Default.aspx)

## Configuration in TIA Portal (RT Professional)

This section contains information on the following topics:

- [Configuring runtime settings for Process Historian (RT Professional)](#configuring-runtime-settings-for-process-historian-rt-professional)
- [Enabling long-term logging (RT Professional)](#enabling-long-term-logging-rt-professional)

### Configuring runtime settings for Process Historian (RT Professional)

#### Introduction

To supply tags for long-term logging, configure Process Historian with "Runtime settings &gt; Process Historian". Enter the server name of the server under "Runtime Settings &gt; Process Historian".

All logging data relevant for Process Historian is stored on the Runtime computer before it is sent to the Process Historian. Under "Store and forward cache", specify a path for caching logging data.

To display the status of Process Historian in Runtime, access the following system tags:

- @PHServer_Principal_State
- @PHServer_Principal_Details
- @PHServer_Mirror_State
- @PHServer_Mirror_Details

> **Note**
>
> **System tag accessibility for Process Historian status display**
>
> The system tags for displaying the status of Process Historian can only be accessed by entering the tag directly as a string. Tags cannot be accessed in the "HMI tags" editor or with object selection in the input field. The tags can be accessed although WinCC marks the input as incorrect.

More information on the use of system tags for the Process Historian status display can be found in the Process Historian server manual "Process Historian - Administration" under "Managing Process Historian".

#### Requirement

- Server for long-term logging is connected to the runtime PC.
- Process Historian is installed on the server for long-term logging.

#### Procedure

1. Select "Runtime settings &gt; Process Historian" in the project tree.

   ![Procedure](images/88810599179_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88810599179_DV_resource.Stream@PNG-en-US.png)
2. Enter the name of the primary Process Historian server in the "Server" field.
3. If you want to use two redundant server systems for data transfer, select the "Configure redundant PH server" checkbox.
4. Enter the name of the redundant Process Historian server in the "Redundant partner" field.
5. Under "Store and forward cache", specify a path for caching data relevant for the Process Historian .

   By default, the data is stored in the "C:\ProgramData\Siemens\SFCache" directory.

   When SIMATIC Process Historian Server is reconnected or restarted, the contents of the cache are transferred to the server and the cache is emptied.

**Note**

Use a maximum of 15 characters for the server name.

If your entries do not correspond to the defined format specifications, an error message will be output.

**Note**

If the path you enter for caching is not correct, an error message is generated during compiling.

#### Process Historian server status display

To display the status of Process Historian in Runtime, access the following system tags:

- @PHServer_Principal_State
- @PHServer_Principal_Details
- @PHServer_Mirror_State
- @PHServer_Mirror_Details

> **Note**
>
> **System tag accessibility for Process Historian status display**
>
> The system tags for displaying the status of Process Historian can only be accessed by entering the tag directly as a string. You cannot access the tags in the "HMI tags" editor or with object selection in the input field. The tags can be accessed although they are marked as an incorrect entry by WinCC.

### Enabling long-term logging (RT Professional)

#### Introduction

To enable long-term logging, assign the relevant logging tags or compressed logging tags the status "Long-term relevant". Only tags with this status are logged in the SIMATIC Process Historian.

#### Requirement

- Server for long-term logging is connected to the runtime PC.
- Process Historian is installed on the server for long-term logging.

#### Procedure

1. Double-click on the "Historical data" entry in the project tree.

   The editor for data logs and compressed logs opens.
2. Select the relevant log under "Data logs".

   The tags in this log appear under "Logging tags".
3. Select one or more logging tags.
4. Select the "Long-term relevant" checkbox in the Inspector window under "Properties &gt; General".

   ![Procedure](images/108444478859_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/108444478859_DV_resource.Stream@PNG-en-US.png)
5. To assign a compressed logging tag the status "long-term relevant", select the compressed tag in a compressed log and select the "Long-term relevant" checkbox.

   ![Procedure](images/108444549899_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/108444549899_DV_resource.Stream@PNG-en-US.png)

#### Result

You have now assigned the tags the status "Long-term relevant". These tags are now logged in the SIMATIC Process Historian.

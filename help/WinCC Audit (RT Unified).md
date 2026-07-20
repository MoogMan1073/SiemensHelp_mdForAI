---
title: "WinCC Audit (RT Unified)"
package: GMPWCCUenUS
topics: 36
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Audit (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring the Audit Trail (RT Unified)](#configuring-the-audit-trail-rt-unified)
- [Configuring audit functions (RT Unified)](#configuring-audit-functions-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [GMP compliance (RT Unified)](#gmp-compliance-rt-unified)
- [GMP-compliant configuration (RT Unified)](#gmp-compliant-configuration-rt-unified)
- [Audit option (RT Unified)](#audit-option-rt-unified)
- [Scope of logging (RT Unified)](#scope-of-logging-rt-unified)
- [Performance features of the GMP-compliant configuration (RT Unified)](#performance-features-of-the-gmp-compliant-configuration-rt-unified)

### GMP compliance (RT Unified)

#### GMP-compliant projects with WinCC

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors, for example

- Pharmaceutical industry
- Companies in the food and beverage industry or in the related mechanical engineering industry

Storage of production data in electronic form offers many advantages compared to paper documents, such as simple acquisition and logging of data.

Events that are relevant for monitoring and ensuring the correctness of the process occur during runtime. Although the data provides information about a specific action, it is complicated for the user to easily identify the relevant data in the data set, such as: Cause of the change in value, actions that led to the change, or additional details about the change itself (e.g. source, location, cause).

However, it is also important to ensure that data cannot be falsified and that it can be read at any time.

Therefore, sector-specific and cross-industry standards have been developed for the electronic documentation of production data.

The most important set of regulations is the FDA Guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration. In addition, different EU regulations apply, for example, EU 178/2002, depending on the industry.

Requirements for production systems in these industries have been developed based on 21 CFR Part 11 and the corresponding interpretation to comply with GMP (Good Manufacturing Practice). However, these requirements are also found in other industries.

The following primary requirements are derived from these directives and rules:

- Creation of an Audit Trail or operating trace in runtime

  Based on this document, it is possible to trace the user who carried out an operator action on the machine at what time.
- Important process steps must also be assignable to a clear responsibility, for example, via an acknowledgment or a comment.

### GMP-compliant configuration (RT Unified)

#### Introduction

"Configuration conforms to GMP" means creating projects in accordance with "Good Manufacturing Practice". The requirements are set out in FDA rules "21 CFR Part 11". The FDA is the U.S. Food and Drug Administration. Eudralex Volume 4, Appendix 1, EMA regulation 178/2002 also applies. EMA is the European Medicines Agency.

GMP-compliant configuration means HMI devices have electronic production data documentation functionalities.

Note that the WinCC Audit option is currently only available for Unified SCADA.

#### GMP-relevant and Audit Trail

WinCC offers the "Audit" option for implementing GMP compliance. Using the Audit option, the "Configuration conforms to GMP" function can be enabled.

Enable the "Configuration conforms to GMP" function directly in the Runtime settings of the HMI device. GMP relevant functionalities are then added to WinCC. These functionalities are:

- Electronic signature
- Option to label tags as "GMP relevant".
- Suggestions for the comment with typical reasons for changes of GMP-relevant tags can be pre-defined by selecting text lists.
- Automatic identification of significant changes in GMP-relevant tags
- Generation and storage of electronic records of the relevant changes - Audit Trail
- System function for recording relevant user actions - electronic recording
- Recording of manipulated log data with checksum
- Audit Trail record for printing logged changes

Execution of or changes to labeled objects are saved in a special log, the "AuditTrail".

#### Licensing

To use the GMP relevant functionalities configured in WinCC in runtime, you need the following license:

- WinCC Audit for RT Unified

You can use the following licenses for the Audit option in WinCC Runtime:

| License | Description |
| --- | --- |
| WinCC Unified Audit Basis | Secured communication  Logging the Audit Trail  Recording of process data changes (automatically, via script or system function)  Confirmation with/without comment  Exporting Audit Trail entries  Audit Trail report and tamper indication  Logging in and logging out Audit Trail entries  Simple electronic signature   Backing up and restoring Audit Trail database segments  Direct display and analysis of the Audit Trail in the Audit Viewer |
| WinCC Unified Audit Enhanced | In addition:   Multiple electronic signature (2 persons) |

### Audit option (RT Unified)

#### Advanced functions

The Audit option adds functions to WinCC to ensure that your project is GMP compliant.

The following functionalities are added:

- Electronic signature

  All Audit-relevant user actions must be protected by authorization in the user administration.

  In runtime, you can make important user actions, such as the following, subject to signature:

  - Value change of recipe data records
  - Value change of GMP-relevant tags
  - Acknowledgment of alarms

  The user will then only be able to run these actions if an electronic signature and, if configured appropriately, a comment have been input.

  The electronic signature and the comment are logged in the Audit Trail.
- Audit Viewer

  - The "Audit Viewer" control enables a transparent and automatic connection with the local Audit Trail.
  - It is not necessary to install WinCC Unified on the target device.
  - Access to online and offline data is possible.
  - Retrieval of electronic records based on specific criteria
  - The "Audit Viewer" control allows defining specific queries and their reuse.
- Audit Trail

  For each HMI device, you can create one Audit Trail .

  Operator actions and system processes that are relevant for the FDA compliance of the process are recorded in an Audit Trail during runtime.

  - Actions by the system, such as starting up runtime or rejecting logon attempts.

#### Audit Trail certificates in Runtime

Audit Trail certificates are required for the HMI device. The certificates are used to check integrity and prevent tampering with the archive. To install the certificate on the HMI device, use the WinCC Unified Certificate Manager. Note that the maximum lifetime of a certificate is 150 months.

![Audit Trail certificates in Runtime](images/149464090763_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Note that an error message appears in the alarm control without the certificate or with an expired certificate.

#### Extension of the WinCC engineering system

For HMI devices that support "Configuration conforms to GMP", the WinCC engineering system is extended to include the following configuration options when GMP is enabled:

- The Audit Trail entry is added to the "Logs" editor
- A "Good Manufacturing Practice Settings" entry is added to the "HMI tags" editor in the Inspector window of a "Properties > Properties" tag
- "InsertElectronicRecord" system function

---

**See also**

[Configuring the "InsertElectronicRecord" system function (RT Unified)](#configuring-the-insertelectronicrecord-system-function-rt-unified)

### Scope of logging (RT Unified)

It is important to ensure that Audit-related processes are always logged in runtime in the Audit Trail in a project with the option "Audit". Logging of the Audit Trail depends on the device used.

You have two options for logging your data in WinCC Unified:

- File-based logging

  File-based logging allows you to log up to 5000 logging tags in an SQL Lite database.

  You do not need a license to log logging tags in WinCC Unified PC.

  You need a WinCC Unified Runtime (RT) license to log logging tags in WinCC Unified PC.
- Database-based logging

  Database-based logging allows you to log all logging tags up to the high limit in an MS SQL database.

  Database-based logging is only available for WinCC Unified PC. You need a WinCC Unified Runtime (RT) license to log logging tags.

  Besides the functionality, database-based logging also includes an MS SQL server. Therefore, you need the "WinCC Unified Database Storage" license.

#### Scope of logging

The following Audit-relevant processes are logged depending on the configuration of the tags of the project:

- Value changes of GMP-relevant tags by the user
- "InsertElectronicRecord" system function

  You use the "InsertElectronicRecord" system function to record user actions that are not automatically recorded by the Audit Trail.

  You can configure this system function to screen calls, for example, or you configure function lists containing system functions that do not require acknowledgment.

### Performance features of the GMP-compliant configuration (RT Unified)

This section contains information on the following topics:

- [Supported HMI devices (RT Unified)](#supported-hmi-devices-rt-unified)
- [Restrictions (RT Unified)](#restrictions-rt-unified)

#### Supported HMI devices (RT Unified)

##### Supported HMI devices

The qualification "GMP relevant configuration" can be configured for the following HMI devices:

- Unified PC
- Unified Comfort Panel

#### Restrictions (RT Unified)

##### Restrictions

The following functions and configurations cannot be used simultaneously with the qualification "GMP relevant configuration":

- PN direct keys
- DP DirectKey
- Events of screen objects

  You can set important user actions as GMP-relevant in runtime, such as changing tag values. In this case, you may not assign any other events to this graphic object.

  When the event of a screen object is assigned actions which open a user dialog, you may not be able to execute these actions at other events.
- Controlling GMP-relevant tags using a slider

  The slider is not suitable for controlling GMP-relevant tags if the property "Process value - write immediately" is activated. Any operation of the slider will continuously change the tag value. If this is a GMP-relevant tag, a flood of entries is generated in the "AuditTrail".

## Configuring the Audit Trail (RT Unified)

This section contains information on the following topics:

- [Enabling GMP compliant configuration (RT Unified)](#enabling-gmp-compliant-configuration-rt-unified)
- [Creating an audit trail (RT Unified)](#creating-an-audit-trail-rt-unified)
- [Audit Trail reports (RT Unified)](#audit-trail-reports-rt-unified)
- [Audit trail logging concept (RT Unified)](#audit-trail-logging-concept-rt-unified)

### Enabling GMP compliant configuration (RT Unified)

#### Introduction

The function is made available to the Audit Trail by labeling it "Configuration conforms to GMP".

#### Requirements

- A project is created.
- A GMP compatible HMI device has been created.

#### Enabling GMP in the HMI device

1. Click on the HMI device in the project tree.
2. Double-click on "Runtime settings".

   ![Enabling GMP in the HMI device](images/170175918731_DV_resource.Stream@PNG-en-US.png)

   ![Enabling GMP in the HMI device](images/170175918731_DV_resource.Stream@PNG-en-US.png)
3. Click on "Good Manufacturing Practice" in the open work area.
4. Click the "Configuration conforms to GMP" button.

   ![Enabling GMP in the HMI device](images/170175971083_DV_resource.Stream@PNG-en-US.png)

   ![Enabling GMP in the HMI device](images/170175971083_DV_resource.Stream@PNG-en-US.png)

"Configuration conforms to GMP" is enabled.

#### Result

The Audit option is now enabled for the HMI device.

The following functions can now be configured:

- Audit Trail log

  - For each HMI device, you can create one Audit Trail
- "InsertElectronicRecord" system function
- GMP-relevant tags
- Reasons for GMP-relevant tags (available text lists with pre-defined comments for acknowledgment in Runtime)

### Creating an audit trail (RT Unified)

#### Requirements

"Configuration conforms to GMP" has been selected on the HMI device. Only one Audit Trail is created per HMI device.

#### Procedure

1. Click on the HMI device in the project tree.
2. Double-click "Logs".

   ![Procedure](images/170176020619_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/170176020619_DV_resource.Stream@PNG-en-US.png)

   The "Logs" work area opens.
3. Change to the "Audit Trail" tab.

   ![Procedure](images/170176095115_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/170176095115_DV_resource.Stream@PNG-en-US.png)

   An Audit Trail is created automatically.
4. Set the parameters of the "AuditTrail" in the Inspector window under "Properties > Properties > General".

   ![Procedure](images/170176033803_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/170176033803_DV_resource.Stream@PNG-en-US.png)

#### Storage medium and storage directory

The following settings are available for the storage medium and the storage directory:

- Default: The storage location that is defined in the WinCC Unified configuration on the runtime machine is selected as storage directory.
- Local: Under storage directory, enter the path to the storage location. Make sure that the user has write permission.

  You can also save the Audit Trail on a USB flash drive or SD card.

- Project folder: As storage directory, you select the runtime folder to which the project data is copied after the download.

#### Log time period

The standard time period is 365 days. You can specify the log time period in the following format: Days.Hours:Minutes:Seconds.

#### Maximum log size

The standard log size is 10 GB. The value is entered in MB. When the maximum log size has been reached, the oldest entries are overwritten.

#### Log segments

The size of the log segments is specified either as a time period or a segment size. You specify the following under "Properties > Properties > Segment":

- Segment time period: The standard time period for logging a single segment is 30 days. You can specify the time period in the following format: Days.Hours:Minutes:Seconds.
- Maximum segment size: The standard segment size is 1 GB. The value is entered in MB.
- Segment start time: Specifies the start time of the log segment.

#### Backup

When the databases exist in the MS SQL format, you can create backups of the database under "Properties > Properties > Backup".

1. Under "Backup mode", select the "Path" setting.
2. Enter a storage location under "Backup path".

### Audit Trail reports (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Add Audit (RT Unified)](#add-audit-rt-unified)
- [Adding or editing configurations for audit (RT Unified)](#adding-or-editing-configurations-for-audit-rt-unified)

#### Basics (RT Unified)

Based on an Audit Trail report, it is possible to trace the operator who carried out operator actions at what time. The configuration engineer uses the WinCC Unified Excel add‑in to configure a report template with parameters of the Audit Trail. The parameters are relevant for quality assurance in the manufacturing process. You can print out the report either as an Excel file, a PDF file or send it via email.

General information on configuring report templates in the Excel add-in is available in [Creating report templates for production protocols](Creating%20production%20reports%20%28RT%20Unified%29.md#creating-report-templates-for-production-reports-rt-unified).

General functions on the configuration of report jobs in runtime are available in [Working with production protocols in runtime](Creating%20production%20reports%20%28RT%20Unified%29.md#working-with-production-reports-in-runtime-rt-unified).

##### Audit Trail parameters

The following table contains an overview of the potential values of the individual report columns:

| Parameter | Description |
| --- | --- |
| Time stamp | Contains the time stamp at which the event occurred. |
| Object name | Contains the name of the object that triggered the change. |
| User | Contains the name of the logged-on user.  When no user is logged on, the field remains empty. |
| Operator Station | Contains either the name of the PC or PLC, or the IP address of the web client. |
| Old value | Contains the tag value before the change. |
| New value | Contains the tag value after the change. |
| Cause | Contains the user comment.  Contains the confirmation of the desired state. |
| Event ID | Contains the internal identifier of the event. |
| Tracking ID | Contains the internal identifier to link the user action to the system response. |
| Provider type of the audit | Contains an identifier for the type of intervention:   2 - Task scheduler  6 - User interface  8 - User management   11 - System diagnostics |
| Audit provider | Contains the name of the provider, for example, Scheduler, User Interface, Event Manager. |
| Type of operation | Contains an identifier for the change:  1 - New value  2 - Updated value  3 - Deleted value |
| Object reference | Contains an identifier of the triggering object. This parameter is reserved for internal purposes. |
| Integrity | Contains an identifier for proof that data was manipulated later. |

---

**See also**

[Add Audit (RT Unified)](Operating%20Unified%20PC%20%28RT%20Unified%29.md#add-audit-rt-unified)
  
[Adding or editing configurations for audit (RT Unified)](Operating%20Unified%20PC%20%28RT%20Unified%29.md#adding-or-editing-configurations-for-audit-rt-unified)

#### Add Audit (RT Unified)

##### Introduction

To output the Runtime device Audit Trail in a report, add an Audit data source item to a report template.

You can find more information about the Audit option in WinCC Unified in the Totally Integrated Automation Portal help.

##### Requirement

- The Audit option was activated in the engineering for the Runtime device.
- The "Audit" option is activated in the connection settings of the Excel add-in.
- The "WinCC Unified" tab is visible in Microsoft Excel.
- A time series segment is available.

##### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded.
2. Select a time series segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Audit" option.
5. Select the Audit Trail.
6. (Optional) To undo your selection, select the Audit Trail under "Selected data source items" and click "Delete".
7. Confirm with "OK".

##### Result

The audit data source item is displayed below the segment.

When an Audit Trail is configured for the data source, the Audit data is added to the report when the Runtime data is read into Microsoft Excel and when it is generated in Runtime:

- In the legend table: Identifier of the overall status of the Audit Trail for the queried time range in the "Audit Status" field

  | Value | Description |
  | --- | --- |
  | Green | No manipulations of the Audit Trail were found in the queried time range. |
  | Red | Manipulations of the Audit Trail were found in the queried time range. Single or multiple entries have been deleted, added or changed. |

  Requirement: The "Audit status" option is activated on the segment under "Header properties".

  > **Note**
  >
  > **Overall status for check mode "None"**
  >
  > If the check mode "None" is set in the configuration of the audit data sources item, the "Audit status" field is always green.
- In the data table of the segment: Identifier of manipulations

  | Type of manipulation | Identifier in the data table |
  | --- | --- |
  | Value of entries changed | Directly at the entries |
  | Entries added |  |
  | Entries deleted | The manipulated time range receives a start and end entry. |

First, the data table shows the contents configured in the standard configuration for Audit. To output other contents, select or create a configuration.

#### Adding or editing configurations for audit (RT Unified)

##### Introduction

**Check mode**

The check mode of the configuration of an audit data source item determines

- Whether an integrity check is performed when the Runtime data is read, and what is checked.

  You can output the overall result of the check in the table header row in the "Audit status" field.
- Which audit data records are provided in the data table.

Possible check modes:

| Symbol | Meaning |
| --- | --- |
| "None" | Provides the data for all audit data records that fall within the requested time range. No integrity check is carried out.  Default setting |
| "Check only" | Checks all audit data records that fall within the requested time range without providing their data.   It is tested whether data records have been manipulated, deleted or added. |
| "Check entries" | Checks the audit data records. Provides the data that falls within the queried time range and that was not deleted from the Audit Trail or added later.   It is checked whether data records have been manipulated. |
| "Check all" | Checks all audit data records. Provides the data that falls within the queried time range.   It is tested whether data records were manipulated, deleted from the audit trail or subsequently added. |

**Filter type**

An audit data record consists of two entries:

- An entry for the user expectation
- An entry for the system response.

User expectation and system response may differ. In addition, there are situations in which only one of the two data records is created.

The filter type controls which data records and which entries are included in the report.

Possible filter types:

| Filter type | User expectation equals system response | User expectation does not equal system response | Data record entry for user expectation or system response is missing |
| --- | --- | --- | --- |
| "Show all data in detail" | Both data record entries are inserted. |  | The existing data record entry is inserted. |
| "Show data and conformity errors" | The data record entry with the user expectation is inserted. | Both data record entries are inserted. |  |
| "Show only data with conformity errors" | No data record entry inserted. |  |  |

##### Requirement

- The "WinCC Unified" tab is visible in Excel.

##### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration > Audit configuration".
4. Enter the name of the configuration under "Name".
5. Select a check mode:
6. Specify a filter type.

   Preset value: "Show data and conformity errors"
7. (Optional) Change the default settings of the optional columns. The optional columns are used to display the audit attributes.

   You can find more information on configuring the optional columns in the WinCC Unified object model > Creating production logs > Configuring optional columns.
8. (Optional) To further filter the inserted content, define a filter query.

   The filter query can consist of up to two conditions. Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an Audit attribute, an operator and enter the value of the attribute.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. You can find more information on setting the display name in the WinCC Unified object model > Creating production logs > Setting the display name for the standard column.

##### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for Audit.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

##### Examples of the configuration of the filter type

The following table contains examples of data records that were generated in Runtime through changes to tags monitored by Audit:

| Data record ID | Tag name | Modified by | Old value | New value | Description |
| --- | --- | --- | --- | --- | --- |
| 1A | Motor1_Speed | User1 | 0 | 10 | An operator changes the speed of a motor in an I/O field of an HMI screen.  User expectation and system response are identical. |
| 1B | Motor1_Speed | System | 0 | 10 |  |
| 2A | ValvePercentile | User1 | 0 | 100 | An operator opens a valve using a slider on an HMI screen.  The valve has a physical blockage and cannot be opened. Therefore, no data record entry for the system response is generated. |
| 3A | ValvePercentile | User1 | 0 | 99 | A physical block has been removed and the operator repeats the entry. The valve reacts, but cannot be fully opened.  User expectation and system response differ. |
| 3B | ValvePercentile | System | 0 | 49 |  |
| 4B | Motor2_Speed | System | 0 | 20 | An operator changed the speed of another motor. The resulting data record was manipulated, and the user expectation entry was deleted.  There is only one entry for the system response. |

The following table shows which data record entries are inserted into the data table depending on the filter type selected when generating the report:

| Data record ID | Tag name | Modified by | Old value | New value |
| --- | --- | --- | --- | --- |
| Filter type "Show all data in detail" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 1B | Motor1_Speed | System | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show data and conformity errors" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show only data with conformity errors" |  |  |  |  |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |

### Audit trail logging concept (RT Unified)

This section contains information on the following topics:

- [Format (RT Unified)](#format-rt-unified)
- [Storage location and medium (RT Unified)](#storage-location-and-medium-rt-unified)
- [Protection mechanisms (RT Unified)](#protection-mechanisms-rt-unified)
- [Upgrading WinCC (RT Unified)](#upgrading-wincc-rt-unified)
- [Audit trail behavior in runtime (RT Unified)](#audit-trail-behavior-in-runtime-rt-unified)

#### Format (RT Unified)

##### Audit Trail format

On an HMI device with "Configuration conforms to GMP", all events that are relevant to the Audit are recorded in runtime in the Audit Trail. You have several format options.

Selection is dependent on the display program and the runtime language used:

- File-based logging  
  File-based logging allows you to log up to 5000 logging tags in an SQL Lite database.
- Database-based logging  
  Database-based logging allows you to log all logging tags up to the high limit in an MS SQL database.

##### Audit Trail with checksum

Audit Trail with checksum is automatically generated in the database that is based on the user certificate. The certificates are created with the WinCC Certificate Manager Tool. You can find more information in the Runtime online help in the Certificate Manager section.

#### Storage location and medium (RT Unified)

##### Storage location and medium

Depending on the hardware configuration of the HMI device, the data may be logged locally (on the hard disk of a PC or on the storage card of a panel) or, if present, on a network drive.

> **Note**
>
> **Logging on network drives**
>
> We do not recommend that you log Audit Trails directly on a network drive. Power supply can be interrupted at any time. This means there is no guarantee for a reliable operation of logs and Audit Trails.
>
> We recommend you save the logs on your local hard drive, or on a storage medium of the HMI device. Use the system function "ArchiveLogFile" to save the logs long-term on a network drive.

"Configuration conforms to GMP" can only be fully operated in runtime as long as Audit-relevant user actions can be saved in the Audit Trail. It is important to ensure that sufficient memory space is available for the Audit Trail and that the connection to the storage location of the Audit Trail is not interrupted.

##### Error-handling with insufficient free storage space

If there is insufficient storage space, your project can be configured so that the administrator has an option of continuing the process without logging in the Audit Trail (forcing).

##### Error-handling if there is no storage medium or the connection to the server is interrupted

If the storage space for the Audit Trail is insufficient, for example, if there is no storage medium, all Audit-relevant user actions are blocked.

The block is canceled as soon as the storage location for the Audit Trail can be reached again. The block can be skipped by "forcing".

##### Error-handling with long-term logging

If the Audit Trail must be moved to a server for long-term logging and the connection to the server is interrupted at this time, the following error-handling is required:

The system closes the Audit Trail and renames it. The system attempts to send the renamed Audit Trail to the server again in the background.

If disruption in the connection to the server persists, you receive a system alarm telling you that the connection is down. Then the system attempts to send the renamed Audit Trail every 300 seconds.

The attempt to transmit the data is repeated until successfully completed. The data is also transmitted after a restart of the HMI device.

#### Protection mechanisms (RT Unified)

##### Protective mechanisms to prevent changes to Audit Trail data

The Audit Trail data are protected against deliberate or accidental changes:

- The directory in which the Audit Trail is saved can only be accessed with special rights.
- The Audit Trail files are write-protected.
- In addition, electronic records that have been removed or added in a certain time segment are identified.
- Each data record contains a checksum that can be used to detect a change of its contents. The checksum is generated based on a certificate. This checksum also ensures that the number of lines has not changed in the Audit Trail file.

Use the "HmiCheckLogIntegrity" tool, included in the Audit option, to check whether an Audit Trail has been changed:

#### Upgrading WinCC (RT Unified)

##### Upgrading WinCC

Before you update WinCC with a Service Pack or a new version, you will have to exit and save the Audit Trail or the logs with checksum. After WinCC is updated, the audit trail or logs with checksum will be continued with new files.

Make sure that the logs are started at a defined state with the new version.

#### Audit trail behavior in runtime (RT Unified)

##### Effects in runtime

The configuration in Audit Trail has the following effects in runtime, depending on the configuration:

- Audit-relevant user actions (such as tag changes) are recorded in an Audit Trail.
- For GMP-relevant tags, the system automatically generates an electronic record as an action requested by the user (requested action) and an electronic record of the system reaction (performed action).
- "Enable logging at runtime start" check box enabled:

  The Audit Trail is started with runtime.
- "Forcing" group, "Allowed if storage space has been exhausted" check box enabled:

  A user with administrator rights can use "forcing" to run operations on the plant even though the Audit Trail can no longer be logged because of storage space limitations. Interrupting the Audit Trail prevents the process from being stopped.

  If the check box "Signing may be bypassed" is enabled, the administrator is not required to input electronic signatures, acknowledgments or comments for operator actions that would normally require signing, acknowledgment or comment.
- Depending on the configuration, the texts can be selected from a pre-defined text list for acknowledgment in Runtime.
- If the storage space available for the Audit Trail is less than the configured "Free storage space limit in MB", the function list configured for the "Low free space" event will be processed.
- If there is insufficient storage space for the Audit Trail because of hardware limits, the function list configured for the "Free space critically low" event will be processed.

## Configuring audit functions (RT Unified)

This section contains information on the following topics:

- [Logging tag value changes (RT Unified)](#logging-tag-value-changes-rt-unified)
- [Logging user actions (RT Unified)](#logging-user-actions-rt-unified)
- [Recording system functions (RT Unified)](#recording-system-functions-rt-unified)
- [Standard entries in the Audit Trail (RT Unified)](#standard-entries-in-the-audit-trail-rt-unified)

### Logging tag value changes (RT Unified)

This section contains information on the following topics:

- [GMP-relevant tags (RT Unified)](#gmp-relevant-tags-rt-unified)
- [Logging tag value changes (RT Unified)](#logging-tag-value-changes-rt-unified-1)
- [Configuring the electronic signature (RT Unified)](#configuring-the-electronic-signature-rt-unified)
- [Audit Viewer (RT Unified)](#audit-viewer-rt-unified)
- [Using Audit Viewer in runtime (RT Unified)](#using-audit-viewer-in-runtime-rt-unified)

#### GMP-relevant tags (RT Unified)

##### GMP-relevant tags

To log changes to the tag value "Good Manufacturing Practice" (GMP), mark a tag as GMP relevant. Special consideration should be given to the following:

- Array tags: When you mark an array variable as GMP relevant, all elements are automatically labeled as GMP relevant. You cannot change the setting of the individual elements.
- User data types: When you mark a user data type as GMP relevant, all elements are automatically labeled as GMP relevant. You cannot change the setting of the individual elements.
- System tags: System tags cannot be marked as GMP relevant.

##### Changes to tag values

When a tag is marked as GMP relevant, changes to the tag value are logged in an Audit Trail.

- Value changes by a user
- Value changes caused by a system function that is configured for an event, if the system function is triggered by a direct user action.

Value changes that are made by the PLC or a system function are not logged in the Audit Trail.

##### Effects in runtime

The configuration has the following effects in runtime depending on the properties of the GMP-relevant tags:

- If the user changes the value of a GMP-relevant tag in runtime, the value change is entered in the Audit Trail.
- Acknowledgment

  If "Acknowledgment" is set as the confirmation type, the user must acknowledge a value change of this tag. Otherwise, the value change is rejected.

  The acknowledgment is logged in the Audit Trail.
- Electronic signature

  If "Electronic signature" is set as confirmation type, the user must log every user-related value change of these tags using an electronic signature. Otherwise, the value change is rejected.

  The name of the user who signed the change is logged in the Audit Trail.
- Comment

  If the "Comment required" setting is selected in addition to the acknowledgment, the user must acknowledge and comment a value change of this tag.

  Otherwise, the value change is rejected. The user can enter the comment via a free text or via the pre-defined text list.

  The acknowledgment and the entered comment are logged in the Audit Trail.

#### Logging tag value changes (RT Unified)

##### Requirement

- "[Configuration conforms to GMP"](#enabling-gmp-compliant-configuration-rt-unified) is activated in the runtime settings.

##### Example procedure

1. Click "HMI tags" in the project tree.
2. Double-click on "Standard tag table".

   ![Example procedure](images/170176160267_DV_resource.Stream@PNG-en-US.png)

   ![Example procedure](images/170176160267_DV_resource.Stream@PNG-en-US.png)
3. In the open work area, select the tag for which you want to make GMP settings.
4. Click "GMP-relevant" under "Properties > Properties > GMP" in the Inspector window.

   ![Example procedure](images/170176130955_DV_resource.Stream@PNG-en-US.png)

   ![Example procedure](images/170176130955_DV_resource.Stream@PNG-en-US.png)

Specify how the user must confirm a value change in the "Confirmation type" selection field.

1. Click on ![Example procedure](images/167171715083_DV_resource.Stream@PNG-de-DE.png) under "Confirmation type".
2. Select the required confirmation type:

   - "None"

     If the value change is to be logged in the Audit Trail without user confirmation.
   - "Acknowledgment"

     If the user needs to acknowledge the value change with "OK".
   - "Electronic signature"

     If the user needs to acknowledge the value change with an electronic signature.

   ![Example procedure](images/170176470411_DV_resource.Stream@PNG-en-US.png)

   ![Example procedure](images/170176470411_DV_resource.Stream@PNG-en-US.png)
3. If you select the electronic signature, you also need to set whether one or two signatures are required.

   If no check box is selected, the Audit Viewer requests one of the two signatures in runtime to acknowledge the value change.

   ![Example procedure](images/170176481931_DV_resource.Stream@PNG-en-US.png)

   ![Example procedure](images/170176481931_DV_resource.Stream@PNG-en-US.png)

   If the user is also required to enter a comment, select the "Comment required" check box.

   This check box is only active if "Acknowledgment" or "Electronic signature" is set as confirmation type.

##### "Electronic signature" confirmation type and corresponding HMI role

If you have selected the "Electronic signature" confirmation type, you need to assign the corresponding HMI role to the user. You can find more information on configuring the HMI role for the electronic signature under "[Configuring the electronic signature](#configuring-the-electronic-signature-rt-unified)".

##### Specifying comments via text lists

To keep the comments uniform, you can use text lists.

You define preset text lists as follows:

1. Click on "Good Manufacturing Practice" in the runtime settings of the HMI device.
2. For "Reasons for GMP-relevant tags", select ![Specifying comments via text lists](images/167366285067_DV_resource.Stream@PNG-de-DE.png).
3. Select the desired text list.
4. Confirm your selection with the green check mark.

   ![Specifying comments via text lists](images/170176511883_DV_resource.Stream@PNG-en-US.png)

   ![Specifying comments via text lists](images/170176511883_DV_resource.Stream@PNG-en-US.png)

You define your own text list as follows:

1. Click on "Good Manufacturing Practice" in the runtime settings of the HMI device.
2. For "Reasons for GMP-relevant tags", select ![Specifying comments via text lists](images/167366285067_DV_resource.Stream@PNG-de-DE.png).
3. Click "Add".

   ![Specifying comments via text lists](images/170176515595_DV_resource.Stream@PNG-en-US.png)

   ![Specifying comments via text lists](images/170176515595_DV_resource.Stream@PNG-en-US.png)
4. Specify the name of the text list.
5. Specify how the connected tag should be interpreted.
6. Add your comment.
7. Click "OK" to confirm the created text list.

   ![Specifying comments via text lists](images/170176519307_DV_resource.Stream@PNG-en-US.png)

   ![Specifying comments via text lists](images/170176519307_DV_resource.Stream@PNG-en-US.png)

#### Configuring the electronic signature (RT Unified)

##### License requirement

You have the "WinCC Unified Audit Basis" license, which includes the "Single electronic signature" functionality. The electronic signature is configured for one person.

You have the "WinCC Unified Audit Enhanced" license, which includes the "Multiple electronic signature" functionality. The electronic signature can be configured for two people.

##### Conditions of configuring the electronic signature

- "Configuration conforms to GMP" is enabled in the runtime settings of the HMI device.
- The desired tag is labeled GMP-relevant.

##### Configuring the "Electronic signature" confirmation type

1. Select "First electronic signature" or "First and second electronic signature". If no check box is selected, the Audit Viewer requests one of the two signatures in runtime to acknowledge the value change.

   ![Configuring the "Electronic signature" confirmation type](images/171482498443_DV_resource.Stream@PNG-en-US.png)

The value change of the tag is associated with the "Electronic signature" confirmation type.

##### Assigning a runtime right for the electronic signature

Assign the corresponding HMI role to the user for the "Electronic signature" confirmation type. Configure the following tasks:

- Create a new user
- Create a new role
- Connect user and role

You create a new user in the following way:

1. Click "Security settings" in the project tree.
2. Double-click on "Users and roles".

   ![Assigning a runtime right for the electronic signature](images/170176617099_DV_resource.Stream@PNG-en-US.png)
3. In the open work area, add a new user.

   - Define the user name and password.

   ![Assigning a runtime right for the electronic signature](images/170176621067_DV_resource.Stream@PNG-en-US.png)

Create a new role

1. Click on the "Roles" tab.
2. Add a new role and name the role.
3. Click on the "Runtime rights" tab.
4. Assign the desired function right to the created role.

   ![Assigning a runtime right for the electronic signature](images/170176637835_DV_resource.Stream@PNG-en-US.png)

Connect user and role

1. Click on the "Users" tab.
2. Assign the appropriate role to the desired user.

   ![Assigning a runtime right for the electronic signature](images/170176641803_DV_resource.Stream@PNG-en-US.png)

In the example, you assigned the "First electronic signature" runtime right to a user.

#### Audit Viewer  (RT Unified)

The "Audit Viewer" object expands the possibilities for visualizing and editing audit-relevant data in runtime:

- Online access to audit data of an Audit Trail
- Offline access to audit data of an exported audit file
- A full installation of WinCC Unified on the runtime device is not necessary
- Automatic and transparent connection to the local Audit Trail
- Query of a range of electronic records that meet specific criteria
- Reuse of defined queries
- Commenting and signing of existing electronic records

##### Audit Viewer

You use the "Audit Viewer" object to evaluate in tabular form all data of the Audit Trail in runtime.

You will find the "Audit Viewer" object under "Toolbox > My controls". You place the object in your screen with a double-click or with drag-and-drop.

![Audit Viewer](images/170176680843_DV_resource.Stream@PNG-en-US.png)

User interface of the "Audit Viewer" object

![Audit Viewer](images/170176677131_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If the filter for manipulated records is set, the affected records are shown with a red background in the Audit Viewer.

##### ① Area navigation

Shows the objects of the Audit Viewer in a worksheet:

- Audit Trail: Shows electronic records saved in an Audit Trail
- Audit File: Retrieves exported electronic records
- User Queries: Allows a user-specific retrieve filter to be defined
- Global Settings: Allows specific control settings to be configured

##### ② Toolbar

| Button | Function |
| --- | --- |
| ![②Toolbar](images/170176684811_DV_resource.Stream@PNG-de-DE.png) | Updates the file. |
| ![②Toolbar](images/170176688779_DV_resource.Stream@PNG-de-DE.png) | Executes the query. |
| ![②Toolbar](images/170176692747_DV_resource.Stream@PNG-de-DE.png) | Enables column selection. |
| ![②Toolbar](images/170176696715_DV_resource.Stream@PNG-de-DE.png) | Sets the filter criteria. |
| ![②Toolbar](images/170176700683_DV_resource.Stream@PNG-de-DE.png) | Exports a CSV file. |

##### ③ Table area

Shows the data records that were selected in the area navigation.

##### ④ Status bar

Shows the following information about the Audit Viewer:

- Scope of IDs of Audit Trail records displayed on the current page.
- Current page number
- Total number of pages
- Total number of trail records

##### Configuring properties

In the Engineering System, you configure the settings for the position, geometry, style and color of the object. You can actively work with the Audit Viewer in runtime. You can adapt the following properties, for example, in the Engineering System:

- "Text": Defines the text for the header of the Audit Viewer.
- "Window settings": Defines the settings for display in runtime.

##### Text

To define a text for the header of the Audit Viewer, follow these steps:

1. Activate the "Show header" option in the Inspector window under "Properties > Appearance > Window settings". The option is activated by default.
2. Click "Properties > Miscellaneous > Label > Font" in the Inspector window.
3. Select a font.
4. Click "Properties > Miscellaneous > Label > Text" in the Inspector window.
5. Enter a text.

##### Adapting size in runtime

To resize the Audit Viewer in runtime, follow these steps:

1. Activate the options "Show border" and "Can be sized" in the Inspector window "Properties > Appearance > Window settings". The options are activated by default.

   The width of the border is not evaluated.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Icon

#### Using Audit Viewer in runtime (RT Unified)

You have created a project in the Engineering System and configured an [Audit Trail](#configuring-the-audit-trail-rt-unified). The project has been loaded into the HMI device and the [Audit Trail system certificate](#audit-option-rt-unified) is installed.

The control shows electronic records that are on the storage medium or based on an active filter in runtime.

##### Showing electronic records

Click on "Audit Trail" in the area navigation for online access to the data of an Audit Trail.

All records are shown in a table.

To keep the status up-to-date, update the Audit Trail after every user action or value change by clicking on ![Showing electronic records](images/170176951947_DV_resource.Stream@PNG-de-DE.png) in the function bar.

##### Exporting an Audit Trail as CSV file

1. To export all data, select the check box in the first column in the table header of the Audit Trail. All displayed actions are automatically selected as well.

   To only export selected data, select each relevant row. Then perform steps 2 and 3.
2. Click the "Export CSV file" button.
3. Save the file. You set the storage location in the area navigation under "Global Settings".

   ![Exporting an Audit Trail as CSV file](images/170176711563_DV_resource.Stream@PNG-en-US.png)

##### Retrieving exported records

To have offline access to the saved data, follow these steps:

1. Click "Audit File" in the area navigation.
2. Click the "Import CSV File" button.

   ![Retrieving exported records](images/169618850955_DV_resource.Stream@PNG-en-US.png)
3. Navigate to the folder where the desired Audit Trail is saved.
4. Select the folder and click "Open" in the bottom area.

   Repeat step 4 until you get to the specific files.
5. You see the imported files in the Audit Viewer under "Audit Trail".

##### Setting and executing a user-specific data query

You set one filter per query. Only one query is ever executed. The user-specific queries can be saved in a central folder.

You can apply queries to currently running or saved Audit Trails.

1. Click "Audit Queries" in the area navigation. A work area for setting the query opens.
2. Click "Add" and add a new query.
3. Name the query in the lower table area.
4. Write a comment, if necessary.
5. Name the author of the query.
6. Click ![Setting and executing a user-specific data query](images/170176955915_DV_resource.Stream@PNG-de-DE.png) under Filter. A work area for filter settings opens.
7. Click ![Setting and executing a user-specific data query](images/169488294795_DV_resource.Stream@PNG-de-DE.png) under "Sorting criteria" and select the desired criterion.

   ![Setting and executing a user-specific data query](images/170176832779_DV_resource.Stream@PNG-en-US.png)
8. Click "Apply".
9. Click ![Setting and executing a user-specific data query](images/169488294795_DV_resource.Stream@PNG-de-DE.png) under "Operator" and select the desired operator.

   ![Setting and executing a user-specific data query](images/170176836747_DV_resource.Stream@PNG-en-US.png)
10. Click "Apply".
11. Set the desired parameters of the specified criterion under "Setting".

    ![Setting and executing a user-specific data query](images/170176861451_DV_resource.Stream@PNG-en-US.png)
12. Click "Apply".
13. Click "Enable" for the query you want to apply.

    ![Setting and executing a user-specific data query](images/171133502603_DV_resource.Stream@PNG-en-US.png)
14. Click the ![Setting and executing a user-specific data query](images/170176951947_DV_resource.Stream@PNG-de-DE.png) button in the function bar of the Audit Viewer to update the Audit Trail.
15. Click the Execute query ![Setting and executing a user-specific data query](images/170177011083_DV_resource.Stream@PNG-de-DE.png) button in the function bar of the Audit Viewer.

##### Setting the display of the columns

To select specific columns in the Audit Trail and display them, follow these steps:

1. Click the ![Setting the display of the columns](images/170177015051_DV_resource.Stream@PNG-de-DE.png) button in the area navigation.
2. All columns are preset to display in the open work area.
3. Disable the columns that you do not require in the Audit Trail.
4. Click "Apply" to apply your settings.
5. You see the desired columns in the "Audit Trail".

##### Defining global settings

With this option, you set global settings that are assigned to the Audit Viewer.

1. Under "List settings", set the number of records to be displayed on a page. The maximum number of records amounts to 50.
2. Under "Audit queries folder", specify the path where the records should be saved.
3. Select a check mode under "Audit verification type settings".
4. Specify a filter type under "Audit filter type settings".
5. Click "Apply".
6. Click the ![Defining global settings](images/170176951947_DV_resource.Stream@PNG-de-DE.png) button in the toolbar of the Audit Viewer to update the global settings.

![Defining global settings](images/170176857483_DV_resource.Stream@PNG-en-US.png)

You can find more information on check modes and filter types in the section [Adding or editing configurations for Audit.](#adding-or-editing-configurations-for-audit-rt-unified)

### Logging user actions (RT Unified)

This section contains information on the following topics:

- [User actions with GMP-compliant configuration (RT Unified)](#user-actions-with-gmp-compliant-configuration-rt-unified)
- [Logging modes (RT Unified)](#logging-modes-rt-unified)
- [Configuring the "InsertElectronicRecord" system function (RT Unified)](#configuring-the-insertelectronicrecord-system-function-rt-unified)
- [GMP-compliant user administration (RT Unified)](#gmp-compliant-user-administration-rt-unified)

#### User actions with GMP-compliant configuration (RT Unified)

##### Introduction

In a GMP-compliant configuration, user actions and system operations in runtime which are relevant for the quality of the process are recorded in an Audit Trail.

For example, a user logon to the system or the change of a tag value are saved in the log.

In runtime, user actions are saved in an Audit Trail under the following conditions:

- "Configuration conforms to GMP" has been enabled
- A user is logged on to the system

#### Logging modes (RT Unified)

##### Configuration-dependent logging

The following processes are logged depending on the configuration of the tags of the project:

- Value changes of GMP-relevant tags by the user

  In addition to logging user actions, you can configure tags to require users to confirm or acknowledge specific actions and enter a comment on the change.

##### Manual logging by means of the "InsertElectronicRecord" system function

This system function is used to log actions in the Audit Trail that are not automatically logged in the Audit Trail.

#### Configuring the "InsertElectronicRecord" system function (RT Unified)

##### Introduction

This system function is used to log user actions that are not entered automatically in the Audit Trail. Moreover, you can use this system and script function to request the user to enter an acknowledgment or a comment for the action.

You can configure this function even if the Unified Scada device is not configured as being GMP-compliant. However, current archiving in runtime takes place only if the device is configured as GMP-compliant.

This function can be configured for screen objects, schedulers, global script. At present, this function is not available for faceplates.

In this example, the system function is assigned to a button. Every time the user operates this button, this action is logged in the Audit Trail.

##### Requirements

- "Configuration conforms to GMP" has been enabled.

##### Procedure

1. Click on a button in a screen.
2. Click on "Events" in the Inspector window.
3. In the function list, configure the "InsertElectronicRecord" system function to the "Click left mouse button" event.

##### System function parameters

| Parameter | Description | Type |
| --- | --- | --- |
| Name | Specifies the name of the object. | String, HMI_tag, Screen object |
| Category | Category or class name of the modified object | String, HMI_tag, Screen object |
| Operation type | Specifies the type of change. | Create: New value  Update: Modified value  Delete: Deleted value |
| Old value | Value before the change | Integer, Double, Bool, String, Color, HMI_tag, Screen object |
| New value | Value after the change | Integer, Double, Bool, String, Color, HMI_tag, Screen object |
| Confirmation type | Specifies whether an acknowledgment is requested. | Specifies how the action must be confirmed.  None = No confirmation required, an entry is created in the Audit Trail.  Confirmation required = Acknowledgment, the user must acknowledge the action; an entry is created in the Audit Trail.  Reason required = Acknowledgment, the user must acknowledge the action and enter a reason; an entry is created in the Audit Trail.  Signature required = electronic signature. A dialog window opens for the user to enter their electronic signature. An entry is created in the Audit Trail.  Signature and comment required = electronic signature. A dialog window opens for the user to enter the electronic signature and a comment. An entry is created in the Audit Trail. |
| Reason (optional) | Specifies the reason for the change. | Text list to select a reason for the change. |
| Required function rights (optional) | Specifies the function right required for the electronic signature. | Specifies the function right required for the electronic signature.  Single electronic signature = A valid electronic signature with first or second signature right is required.  Only first electronic signature = A valid electronic signature with first signature right is required.  Only second electronic signature = A valid electronic signature with second signature right is required.  Multiple audit rights = A double electronic signature with first and second signature rights is required. |

##### Result

When a user operates the screen object in Runtime and triggers the event, the tag value is changed. An entry is created in the Audit Trail at the same time;

depending on the parameters "Confirmation type" and "Reason", the entry is an acknowledgment and a comment.

#### GMP-compliant user administration  (RT Unified)

##### Central user management

Use the central user management to manage users and user groups centrally for multiple applications or HMI devices.

### Recording system functions (RT Unified)

#### Introduction

If system functions are triggered in runtime, this is recorded in the Audit Trail for some system functions. If specific system functions are used on a GMP-relevant object,

the user must confirm the triggering.

Some system functions are not supported when using Audit. If you use these system functions in your project, you are solely responsible for them.

The following table shows which system functions are Audit-relevant and whether the user's signature is required:

#### System functions and Audit

| Function (call in script) | Effect of Audit |
| --- | --- |
| InsertElectronicRecord | Entered in Audit Trail |
| UpdateTag |  |
| SetTagValue |  |
| IncreaseTag |  |
| DecreaseTag |  |
| SetBitInTag |  |
| ResetBitInTag |  |
| InvertBitInTag |  |
| ShiftAndMask |  |

In order for the system function to be entered in the Audit Trail in the event of tag value changes, the tag must be marked as GMP relevant.

### Standard entries in the Audit Trail (RT Unified)

#### General entries in the Audit Trail

Individual operator actions are overwritten during logging. The following table shows examples of such entries:

| Log entry | Description |
| --- | --- |
| Change of the tag value 'HMI_Tag_1' from '0' to'55' | Changing the value of a tag |
| User logged off. | Logging out a user. |
| Shutting down application. | Exiting the program. |
| Runtime start of WinCC Runtime Advanced | Starting WinCC Runtime Advanced |
| 'Project.HMI_1 - 0' Build 2. | Information on the project, the device and the current version number |

#### Version number of the device

The version number is incremented with each compilation of the device. You can find the version number in the Inspector window under "Properties > General > Information".

![Version number of the device](images/142368722315_DV_resource.Stream@PNG-en-US.png)

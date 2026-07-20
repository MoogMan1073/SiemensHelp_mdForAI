---
title: "Logging data (RT Unified)"
package: LogsWCCUenUS
topics: 6
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Logging data (RT Unified)

This section contains information on the following topics:

- [Log basics (RT Unified)](#log-basics-rt-unified)
- [How it works (RT Unified)](#how-it-works-rt-unified)
- [Storage locations of logs (RT Unified)](#storage-locations-of-logs-rt-unified)
- [Creating a data log and an alarm log (RT Unified)](#creating-a-data-log-and-an-alarm-log-rt-unified)
- [Editing log contents with scripts and system functions (RT Unified)](#editing-log-contents-with-scripts-and-system-functions-rt-unified)

## Log basics (RT Unified)

### Introduction

The following types of logs are available for HMI devices:

- Data log

  A data log is used to log process data from an industrial plant. You can find more detailed information about this in section [Logging tags](Configuring%20tags%20%28RT%20Unified%29.md#logging-tags-rt-unified).
- Alarm log

  An alarm log is used to log alarms that occur in the monitored process. You can find more detailed information about this in section [Logging alarms](Configuring%20alarms%20%28RT%20Unified%29.md#logging-alarms-rt-unified).
- Context log

  The context log is used to save user-defined and system-generated contexts of plant objects.

  The context log is only available for Unified PC and is stored according to the settings in the "WinCC Unified Configuration" tool.

  The context log is not segmented and has no limit with regard to size or time period.

### Database types

The following database types are supported by various HMI devices:

| HMI device | Supported database type |
| --- | --- |
| SIMATIC Unified Comfort Panel | SQLite |
| Microsoft SQL |  |
| SIMATIC WinCC Unified PC | SQLite |
| Microsoft SQL |  |

> **Note**
>
> **Microsoft SQL for Unified PC**
>
> Unified PCs use SQLite as the default database type. To use Microsoft SQL, the system provides an installation option with a setup package. Logging with SQLite is not possible after the installation of Microsoft SQL.
>
> Existing SQLite files are retained, but they cannot be accessed in runtime.

### Database for simulation

SQLite is always used for simulations on the Unified PC. Exception: Runtime is installed on the same Unified PC and Microsoft SQL is configured for runtime. The configuration of the storage location is ignored during the simulation. Instead, a relative path is used in the project folder.

### Protection against loss of data

When the database cannot be reached for brief periods, a temporary buffer of 8 MB is available. The buffer is used, for example, during a system overload caused by large amounts of data or when changing the storage medium.

If the power supply is unintentionally interrupted, runtime is suddenly and unexpectedly shut down. In this case, a loss of data may occur for up to 4 seconds. If the system was overloaded by large amounts of data, the loss of data can be even higher.

The data already logged is retained and is available unchanged and completely after the power supply has been restored and the system has been rebooted. Logging can be continued with the same database.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Loss of data due to interrupted power supply and removed storage medium**  Loss of data will occur when the power supply is interrupted and there is no connection to the storage medium at the same time. |  |

### Protection against manipulation

Logs can contain sensitive and confidential content, such as performance parameters or product data, that must be protected from unintentional or unauthorized modification.

In addition to physical protection measures, such as barriers, the Unified PC logs can also be protected using standard tools such as access rights for folders.

On Microsoft SQL servers, you protect the log databases by using the Windows group "Simatic HMI" (read/write) and "Simatic HMI Viewer" (read). Only members of these groups have direct access to the databases.

### Startup behavior

The startup behavior of the logs at runtime start is defined in the "Reset Logs" section of the "Load Preview" dialog box when the project is loaded.

The following options are available:

- "No reset": Existing logged data is retained. This setting adds the data to be logged to an existing log.
- "Reset all": Existing logged data is deleted.

### Restoring log segments

You have the option of restoring log segments of tag and alarm logs in runtime with the Runtime Manager. You can visualize the restored data in a trend control, for example.

You can find more information on this in the help of the Runtime Manager.

---

**See also**

[Specifying runtime settings (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#specifying-runtime-settings-rt-unified)
  
[Specifying runtime settings (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#specifying-runtime-settings-rt-unified-1)

## How it works (RT Unified)

### Introduction

Segmented logs are used for logging.

Each log consists of a configurable number of segments. The segments are filled one after the other.

When the maximum size or the maximum period of a log is reached, the oldest segment is deleted.

When the maximum size or the maximum period of a segment is reached, a new segment is created. The newly created segment is filled further.

### Size of a log

You have the option of defining the size of a log both time-dependent and disk space dependent:

- Log time period: When the maximum period is reached, the oldest segment is deleted.

  If you specify the value "0" for "Log time period", the oldest segment is deleted when the maximum log size in megabytes is reached.

  The limitation of the log by a time period is thus disabled.
- Maximum log size in megabytes: When the maximum log size is reached, the oldest segment is deleted.

  If you specify the value "0" for "Maximum log size (MB)", the oldest segment is deleted when the maximum time period of the log is reached.

  The limitation of the log by log size is thus disabled.

When you define both properties, the oldest segment is deleted as soon as the defined period or the maximum log size has been reached.

> **Note**
>
> **Performance problems with disabled segmentation**
>
> If you specify the value "0" for the time period of the log and the maximum log size, the value for "Single segment time period" and for "Maximum segment size in megabytes" must also be "0". The segmentation is thus disabled. All data is written to one segment. Disabled segmentation results in performance problems when accessing the log. You cannot create a backup when segmentation is disabled. Log contents can only be deleted with the system functions "ClearTagLog" or "ClearAlarmLog".
>
> The database can grow uncontrolled, as the log is not limited in size and time period.
>
> Define at least the log period or the maximum log size in megabytes.

When you define logs, keep the following rules in mind:

- The time period of a segment must not exceed the time period of the log.
- The maximum size of the segment must not exceed the maximum size of the log.

> **Note**
>
> **Recommended log size**
>
> The following limits are recommended for the log size:
>
> - At least 3 individual segments
> - Max. 5000 segments (database type "Microsoft SQL")
> - When the database type "SQLite" is used, the maximum number of segments is only limited by the underlying file system.
>
> Backups and segments that were restored from backups with the Runtime Manager are not taken into account when the system checks the database size.

> **Note**
>
> **Recommended use of database types**
>
> The use of Microsoft SQL for data logs is recommended under the following conditions:
>
> - Number of tag value changes to be logged greater than 500 per second
> - More than 1.3 billion log entries must be available (excluding deleted log segments in the backup)
>
> The use of Microsoft SQL for alarm logs is recommended under the following conditions:
>
> - Number of alarm states to be logged greater than 100 per second
> - More than 26 million log entries must be available (excluding deleted log segments in the backup)

### Size of a segment

According to the log, you can define the size of a segment both time-dependent and disk space dependent:

- Segment time period: When the segment reaches the specified time, the current segment is closed and a new segment is created and filled with data.

  When you specify the value "0" for the "Single segment time period", the single segment is filled until the maximum segment size has been reached. Time-based segmenting is thus disabled.
- Maximum segment size in megabytes: When the segment reaches the specified size, the current segment is closed and a new segment is created and filled with data.

  When you specify the value "0" for the "Maximum segment size (MB)", the single segment is filled until the maximum single segment time period has been reached. Size-based segmentation is thus disabled.

When you define both properties, the current segment is closed and a new segment is created as soon as the defined time or the maximum segment size has been reached.

> **Note**
>
> **Performance problems with disabled segmentation**
>
> When you specify the value "0" for the "Segment time period" and for "Maximum segment size in megabytes", segmentation is disabled. All data is written to one segment. Disabled segmentation results in performance problems when accessing the log. You cannot create a backup when segmentation is disabled. Log contents can only be deleted with the system functions "ClearTagLog" or "ClearAlarmLog".

For SQLite, the segment size of a log is always an integer multiple of 4 MB. This means the actual segment size is 8 MB when you configure a segment size of 7 MB.

For Microsoft SQL, the smallest segment size is 3 MB.

### Segment start time

You define the segment start time. The start time defines the time as of which log segments are written to the log.

### Response to segment change

The individual segments are filled one after the other in runtime. Once a segment is totally full, the next segment is created and filled.

![Response to segment change](images/140796419083_DV_resource.Stream@PNG-de-DE.png)

1. The process values are written continuously to the first segment.
2. When the configured size of the segment is reached or the period is exceeded, a new segment is created and filled.
3. When the maximum log size or the maximum period of a log is reached, the oldest segment is deleted.

To avoid losing process data as a result of deleting, you can configure a backup for the log.

> **Note**
>
> If you change the segmentation settings and load the project in runtime, a new segment is created.

### Example

The following information has been configured:

| Property | Value |
| --- | --- |
| Log time period | 1 week |
| Maximum log size (MB) | 700 MB |
| Segment time period | 1 day |
| Maximum segment size (MB) | 100 MB |
| Segment start time | Friday, 23 May 2020 18:00 |

With the configuration suggested in the table, log segments are written to the log starting on 23 May 2020 at 18:00 hours.

The next time-dependent segment changes take place cyclically after one day as of the configured time. The segment will also change if the configured size of 100 MB is exceeded in the course of one day.

When the maximum log size of 700 MB or the configured time period of one week is reached, the oldest segment is deleted.

### Backup

When you create a log you can configure a backup.

The data is swapped out in segments. A segment is always swapped out during a segment change when a new segment is started.

The larger the segment, the more time a backup requires. When the backup of a segment is complete, you can delete the segment.

> **Note**
>
> **Creating backups**
>
> The backup is created with a delay of approx. 10 minutes.
>
> If data is changed in a segment for which a backup has already been created, a new backup will be created approx. 10 minutes later.

---

**See also**

[Log basics (RT Unified)](#log-basics-rt-unified)
  
[Creating a data log and an alarm log (RT Unified)](#creating-a-data-log-and-an-alarm-log-rt-unified)
  
[Size of a log entry in the data log (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#size-of-a-log-entry-in-the-data-log-rt-unified)
  
[Size of a log entry in the alarm log (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#size-of-a-log-entry-in-the-alarm-log-rt-unified)

## Storage locations of logs (RT Unified)

### Introduction

You adapt the main database storage locations for tag and alarm logging in the runtime settings of the HMI device. Different options are available depending on the HMI device.

For Unified PCs, you have the option of storing the storage location in the "WinCC Unified Configuration" tool under "Archive Settings".

> **Note**
>
> **Default setting for the database storage location**
>
> The storage location "Default" is configured as default setting in the Runtime settings and in the "Logs" editor. If you do not change these options, the database is saved according to the setting in the "WinCC Unified Configuration" tool.

### Storage location of a log

You adjust the storage location of the main database of the tag logs and alarm logs in the runtime settings of the HMI device.

The following options are available depending on the HMI device:

| HMI device | Supported main database storage locations for logging |
| --- | --- |
| Unified Comfort Panel | - SD-X51   Many read and write processes are being executed during logging. Therefore, you should use memory cards rather than USB flash drives. - USB-X61 - USB-X62 - Off: Logging is disabled.  You have the option of specifying a path on the storage medium. |
| Unified PC | - Default: In the "WinCC Unified Configuration" tool, you store the path at which the logs are saved under "Archive Settings". - Local: Select a path on the local file system, on an external storage medium or a network folder.   We do not recommend using network folders, because the power supply can be interrupted at any time. - Project folder: The logs are saved in a subfolder of the Runtime project folder. - Off: Logging is disabled. |

When you define a storage location in the runtime settings of the HMI device, and thus enable logging, you can specify the database storage location for individual tag and alarm logs in the "Logs" editor under "Storage medium".

It must be ensured that the "WCCILScsService" service user under which Runtime is running has read and write rights to the directory in which the logs are stored. You have the following options here:

- Configure the directory for the logs with the "WinCC Unified - Configuration" tool and configure the storage of logs in this directory or its subdirectories in the engineering system.
- In the engineering system, configure the storage of logs in directories for which no restriction of the access rights is configured in the operating system. However, this means that the logs are then not protected from access by third parties.

> **Note**
>
> If you want to access a large number of log values within a short time, it is advisable to set the maximum memory of the SQL server to at least 4 GB in the "WinCC Unified – Configuration" tool.

### Changing the storage location of the main database

> **Note**
>
> **Data loss when changing the location of the main database**
>
> If you have already saved data in a log and then change the location of the main database and reload the project, you can no longer access the already logged data in runtime.
>
> Changing the location of individual logs in the "Logs" editor is possible without data loss as long as the location of the main database remains unchanged.

In the following cases, access to already logged data is lost:

- Unified PC:

  - If you use the storage medium "Standard" as the storage location of the main database in the runtime settings of the Unified PC and change the storage location of the databases in the Werkzeug "WinCC Unified - Configuration" tool
  - If you use the storage medium "Local" as the storage location of the main database in the runtime settings of the Unified PC and change the folder
  - If you change the file path of the log in the file system of the Unified PC, e.g. rename folders with a file explorer
- Unified Comfort Panel:

  - If you change the storage medium or folder of the main database location in the runtime settings of the Unified Comfort Panel
  - If you change the file path of the log on the external storage medium, e.g. rename folders with a file explorer

### Naming conventions

The log names must be unique in an HMI device. Even if different storage locations are selected for different logs, the log name must be unique.

### Syntax examples for storage locations

Location of local file system on the Unified PC:

- <C:\My_File_Folder\My_Archives\Machine_1>: Saves the log on the local hard disk drive "C:" in the subdirectory "My_File_Folder\My_Archives\Machine_1"

Memory card storage location on the Unified Comfort Panel:

- </media/simatic/data-storage /My_Archives/TagLogs>: Saves the log in the subdirectory "My_Archives\TagLogs"

### File name

The segments are stored according to the syntax <Unique name of the runtime project>_<Abbreviation of the logging service>_<System ID>_<Start date of the segment>_<Start time of the segment (UTC)> for example, as follows:

- Microsoft SQL: "HMI_RT_1_TLG200_20201106_135307.mdf" and "HMI_RT_1_TLG200_20201106_135307_log.ldf"
- SQLite: "HMI_RT_1_TLG200_20201106_135307.db3"

The backup files of the segments are stored with the syntax <Unique name of the Runtime project>_<Abbreviation of the logging service>_<System ID>_<Start date of the segment>_<Start time of the segment (UTC)> under the configured path, for example as follows:

- "HMI_RT_1_TLG200_20201106_135307.bak"
- "HMI_RT_1_TLG200_20201106_135307_diff.bak"

  The file with the extension "_diff.bak" is created when the backup was already created and value changes occurred later, for example, by manually adding values.

### External storage medium

You have the option of saving the logs on an external storage medium. To avoid the loss of data, the storage medium must be properly removed.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss due to improper removal of the storage medium**  When the storage medium is not removed correctly, logging is interrupted. As soon as you connect a storage medium and restart runtime, logging can be continued with existing databases.   Data that occur between improper removal of the storage medium and the start of runtime are not logged. |  |

The procedure for ejecting the storage medium differs depending on the HMI device:

- Unified Comfort: You use the system function "EjectStorageMedium".
- Unified PC: Eject the storage medium using the PC operating system.

Next, you remove the storage medium and connect a different storage medium.

Data that occurs during the change process are written to a buffer. Logging is continued in a new segment after the change has been completed.

### Logs on different storage media

> **Note**
>
> **Storage medium for Unified Comfort**
>
> The storage location of the main database of a logging type and the configured storage medium of all associated logs must be identical.

### Tag persistency

In runtime, you have the option of specifying tag persistency for internal tags. A separate database, in which the last values of the persistent tags are stored, is used for tag persistency.

When the databases for data logs or alarm logs and the database for tag persistency are stored on the same storage medium and the medium is changed while runtime is running, tag persistency can be affected.

> **Note**
>
> Use different storage media for tag persistency and logging.

### Parameter set types

With Unified Comfort, you have the option of saving parameter set types on external storage media.

When the databases for data logs or alarm logs and the parameter set types are stored on the same storage medium and the medium is changed while runtime is running, the parameter set types can be affected.

> **Note**
>
> Use different storage media for parameter set types and logging.

---

**See also**

[Storage system (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#storage-system-rt-unified)
  
[Storage system (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#storage-system-rt-unified-1)
  
[Basics of downloading projects (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-of-downloading-projects-rt-unified)
  
[Basics for downloading projects (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#basics-for-downloading-projects-rt-unified)

## Creating a data log and an alarm log (RT Unified)

### Introduction

You create data logs and alarm logs for the HMI device in the "Logs" editor. In addition to the name, storage location and backup, you define the size of the log and its segments.

The size of the log and the segments can be defined both time-dependent and disk space dependent. The size of a log is calculated according to the log type as follows:

- Data log: Number of entries * Size of entries

  In addition to the value of a logging tag, its time stamp and quality code are logged.
- Alarm log: Number of entries times the approximate size of the entries

  The size of an entry depends on the alarm text, whether it contains parameter boxes and in which languages the alarm text is logged.

> **Note**
>
> Make sure that the log size does not exceed the free disk space and the system limits. The system does not validate the selected settings. A high number of linked log segments can lead to prolonged waiting periods in the system when starting and ending runtime.

### Requirement

- An HMI device has been created.
- A database storage location for data logs and alarm logs is stored in the runtime settings.

### Procedure

To create data logs or alarm logs, follow these steps:

1. Double-click the "Logs" entry in the project tree below the HMI device.

   The "Logs" editor opens.
2. Double-click "<Add>" in the "Name" column of the "Data logs" or "Alarm logs" tab.  
   A new log is created.
3. Specify the name of the log.

   You can assign any name to the log. The name must contain at least one letter or one number.

   You can create several logs for each HMI device.

   The name must be unique for the respective HMI device.
4. Select the storage location of the log in the "Storage medium" field:

   - "Local": Enter the storage path for the log under "Storage directory".
   - "Default": Accepts the settings that you have defined in the runtime settings of the HMI device under "Storage system".
5. In the "Log time period" field, define the maximum time period for logging in the format <day>.<hour>:<minute>:<second>[.<millisecond>].
6. Define the maximum size in megabytes in the "Maximum log size (MB)" field.
7. In the "Segment" area, define the time period for a single segment in the format <day>.<hour>:<minute>:<second>[.<millisecond>].
8. Define the maximum segment size.
9. Define the start time.

   The start time defines the time as of which log segments are written to the log.
10. Set whether data is to be backed up and specify the path for the backup under "Backup > Backup mode".

    The backup is created with a delay of approx. 10 minutes.

    If data is changed in a segment for which a backup has already been created, a new backup will be created about 10 minutes later.

    When you subsequently change the primary path, the new backup file is written to the new storage path after loading. The previous backup files remain in the previous storage location.

    ![Procedure](images/136316727563_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/136316727563_DV_resource.Stream@PNG-en-US.png)

**Note**

**Logging on network drives**

Do not save databases directly on a network drive. Power supply can be interrupted at any time. This means there is no guarantee for reliable operation of logs.

Save the logs on the local hard drive or an external storage medium, for example, a USB stick.

In connection with SQLite, loss of data can occur for an external storage medium without journaling file system in case of an unintentional system crash.

**Note**

**Data loss when changing the location of the main database**

If you have already saved data in a log and then change the location of the main database and reload the project, you can no longer access the already logged data in runtime.

Changing the location of individual logs in the "Logs" editor is possible without data loss as long as the location of the main database remains unchanged.

**Note**

We recommend the following number of segments:

- Without backup: 3 segments
- With backup: 4 segments

**Note**

Configure the database type in the runtime settings of the HMI device.

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| Configure the properties of a log directly in the "Logs" editor table. To view hidden columns, activate the column titles using the shortcut menu. |  |

### Result

- The log is created.
- The log database in the configured folder is created after the project is started in runtime.

---

**See also**

[Configuring logging tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-logging-tags-rt-unified)
  
[Basics of alarm logging (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#basics-of-alarm-logging-rt-unified)
  
[How it works (RT Unified)](#how-it-works-rt-unified)

## Editing log contents with scripts and system functions (RT Unified)

### Using snippets

In the shortcut menu of the "Scripts" editor, you will find various snippets for logging. You have the following options, for example:

- Read data logs and alarm logs
- Export data logs and alarm logs
- Correct entries in data logs
- Comment entries in data logs

### Delete log contents

You can delete the contents of an alarm log or data log using the "ClearTagLog" or "ClearAlarmLog" system functions. The log itself is retained, the alarm or logging data stored in it is deleted. This procedure can be useful, for example, after a test phase has been completed when existing logs are to be emptied.

---

**See also**

[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[ClearTagLog (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#cleartaglog-rt-unified)
  
[ClearAlarmLog (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#clearalarmlog-rt-unified)
  
[Input support (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#input-support-rt-unified)
  
[System functions (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified)

---
title: "Working with logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: LogsWCCPenUS
topics: 8
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with logs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with Logs (RT Professional)](#working-with-logs-rt-professional)

## Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Log Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Properties of Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#properties-of-logs-basic-panels-panels-comfort-panels-rt-advanced)
- [Storage locations of logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#storage-locations-of-logs-basic-panels-panels-comfort-panels-rt-advanced)

### Log Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

WinCC provides the following types of log for logging process data for HMI Runtime:

- Data logs
- Alarm logs

A data log is used to log process data from an industrial plant.

An alarm log is used to log alarms that occur in the monitored process.

#### Principle

The two types of log both have roughly the same structure and largely work in the same way. They are very clear and easy to configure. With both types of log you define the same properties for the log. The same logging methods are also available for both types of log.

The following logging methods are available:

- Circular log  
  If a circular log is totally full, the oldest entries are overwritten.
- Segmented circular log  
  In a segmented circular log, multiple single logs of the same size are filled in succession. When all log segments are filled, the oldest log segment is overwritten.
- Log with level-dependent system alarm  
  A system alarm is triggered when a defined level is reached.
- Log with level-dependent triggering of an event  
  The "Overflow" event is triggered when the log is full. The "Overflow" event triggers a system function.

---

**See also**

[Properties of Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#properties-of-logs-basic-panels-panels-comfort-panels-rt-advanced)
  
[Log basics (RT Professional)](#log-basics-rt-professional)

### Properties of Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You define the properties of a data log in the "Data logs" editor.

You define the properties of an alarm log in the "Alarm log" editor.

The properties of the data log and alarm log are configured in the same way. You configure the properties either directly in the table of the respective editor or in the log properties of the Inspector window.

#### General properties

- Name

  You can assign any name to the log. The name must contain at least one letter or one number.
- Storage location

  The storage location specifies where the log is saved. The HMI device determines which storage locations are available.
- Size

  The size of a log depends on the type of log and the selected settings.

  - Size of a data log

    The size of a data log is calculated as follows:

    The number of items * the length of each tag value to be logged.

    In the "Properties" window, the maximum size that the log accepts for retention of the currently selected number of data records is displayed in the input field "Number of data records". The maximum log size is limited by the volume of the storage medium.
  - Size of an alarm log

    The size of an alarm log is calculated from the number of data records and the approximate size of an entry. The size of an entry depends on whether the alarm text and the associated tag values are to be logged as well.
- Restart characteristics

  Under Restart characteristics you can specify that the logging starts when Runtime starts. Check the "Enable logging at runtime start" check box.

  You can also control the behavior when Runtime starts. Enable "Reset log" if you want to overwrite existing logged data with the new data. Select the "Append data to existing log" option if you want to retain the existing logged data. This setting adds the data to be logged to an existing log.

> **Note**
>
> You can use system functions to control the restarting of a log in Runtime.

#### Automatic log entries

In Runtime, the following log entries are created as standard:

| Entry | File format | Log type | Meaning |
| --- | --- | --- | --- |
| $RT_DIS$ | Any | Data log | Indicates that the connection to the log was interrupted at this point in time.   (A bold line is shown in the trend view for this time period.) |
| $RT_OFF$ | Any | Data log | Indicates that Runtime was shut down at this point in time.   (No line is shown in the trend view for this time period.) |
| $RT_ERR$ | Any | Data log  Alarm log  AuditTrail<sup>1</sup> | Indicates in the destination log that a copy operation was not successful or was interrupted.  (The log copy was not fully created.) |
| $RT_COUNT | *.CSV  *. TXT | Data log  Alarm log  AuditTrail<sup>1</sup> | This entry was created at the end of the log and serves to increase the system performance when Runtime starts. |
| <sup>1</sup> The "AuditTrail" logging method is not available for all HMI devices. |  |  |  |

---

**See also**

[Log Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)

### Storage locations of logs (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Storage location of a log

When you configure a log in WinCC, the available storage locations depend on the HMI device you are using.

| HMI devices | Supported logs |  |  | Supported storage locations | Supported storage locations |
| --- | --- | --- | --- | --- | --- |
| Alarms | Tags | Audit Trail |  |  |  |
| Basic Panels<sup>1</sup> | No | No | No | - | - |
| Basic Panels 2<sup>nd</sup> Generation<sup>2</sup> | Yes | Yes | No | a TXT file (Unicode) | USB memory (at USB port) |
| Comfort Panels<sup>3</sup> | Yes | Yes | Yes | a CSV file (ASCII)  RDB file  a TXT file (Unicode) | Storage card (SD)  Storage card (USB)  Network drive |
| Mobile Panels 2<sup>nd</sup> Generation<sup>4</sup> | Yes | Yes | Yes | a CSV file (ASCII)  RDB file  a TXT file (Unicode) | Storage card (SD)  USB memory (at USB port)  Network drive |
| PC systems with Runtime Advanced | Yes | Yes | Yes | a CSV file (ASCII)  Database  RDB file  a TXT file (Unicode) | Local file system  Network drive |
| <sup>1</sup> KP 300, KP 400, KTP 1000, TP 1500   <sup>2</sup> KTP 400, KTP 700, KTP 900, KTP 1200   <sup>3</sup> All HMI devices from the device list   <sup>4</sup> KTP 400F Mobile, KTP 700 Mobile, KTP 900 Mobile - including fail-safe versions |  |  |  |  |  |

> **Note**
>
> **Logging on network drives**
>
> Do not log alarms, tags and Audit Trail directly on a network drive. Power supply can be interrupted at any time. This means there is no guarantee for a reliable operation of logs and audit trails.
>
> Save the logs on your local hard drive or a local storage card. Use the system function "ArchiveLogFile" to save the logs long-term on a network drive. This step ensures reliable operation.

#### Syntax examples for storage locations

Storage card storage location:

- &lt;\Storage Card MMC\My_Archives\TagLogs&gt;: Saves the archive on the MMC storage card to the subdirectory "My_Archives\TagLogs".

Local file system storage location:

- &lt;C:\My_File_Folder\My_Archives\Machine_1&gt;: Saves the log on the local hard disk drive C: in the subdirectory "My_File_Folder\My_Archives\Machine_1"

Network drive storage location:

- &lt;\\ArchiveServer\My_File_Folder\My_Archives\Machine_1&gt;: Saves the archive on the "ArchiveServer" server to the subdirectory "My_File_Folder\My_Archives\Machine_1".

#### Naming conventions

The log names must be unambiguous in a project. The name of a log must always be unique, regardless of whether different storage locations are selected for the log.

> **Note**
>
> The characters which can be used in the name of the data source depend on the storage location.
>
> The \ / * ? : " &lt; &gt; | characters are not allowed at the following locations:
>
> - File - RDB
> - File - CSV (ASCII)
> - File - TXT (Unicode)
>
> If the "Database" storage location is used, the following characters may be used: a-z A-Z 0-9 _ @ # $
>
> The characters _ @ # $ cannot be used as the first character of a name.

> **Note**
>
> **Only applies to Basic Panels 2nd Generation**
>
> Unicode characters are not supported for the log names and the log paths.

#### File - CSV (ASCII)

Data is saved to a CSV file in standard ASCII format.

If you want to read or evaluate logged data without using WinCC Runtime, use the "CSV file" storage location.

> **Note**
>
> Double quotation marks or multiple characters are not permitted as list separators for the "CSV file" storage location. You can find the settings for list separators under "Start &gt; Settings &gt; Control Panel &gt; Regional and Language Options".

> **Note**
>
> **Logging tags of the "BOOL" data type**
>
> Boolean values are logged as digits:
>
> - 0 (False) corresponds to the log entry 0
> - 1 (True) corresponds to the log entry -1

#### File - TXT (Unicode)

Data is stored in Unicode.

This file format supports all characters that can be used in WinCC and WinCC Runtime. For editing, you will need software that can save files in Unicode, such as Notepad.

> **Note**
>
> Use "File - TXT (Unicode)" as the storage location to log Asian languages.

#### File - RDB

Data is saved with quick access in a proprietary database.

If you require maximum read performance in Runtime, use the "RDB file" storage location.

#### Database

Data is saved to a database which is set up for ODBC access by the PC administrator.

#### Log with checksum (Audit Trail)

The following files are generated under special circumstances:

***.keep**

1. If a log is started without checksum and will be continued with a checksum.
2. If you update WinCC with a service pack or a new version and the Audit Trail or the log is continued with the checksum.

The content of the keep file will remain the same when compared with the original csv file or txt file.

***.bak**

If WinCC Runtime has determined a serious, irregular problem in the file.

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Log Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-basics-basic-panels-panels-comfort-panels-rt-advanced)

## Working with Logs (RT Professional)

This section contains information on the following topics:

- [Log basics (RT Professional)](#log-basics-rt-professional)
- [Properties of logs (RT Professional)](#properties-of-logs-rt-professional)

### Log basics (RT Professional)

#### Introduction

WinCC provides the following types of logs for logging process data in Runtime Professional:

- Fast data log
- Slow data log
- Alarm logs

Data logs are used to log process data from an industrial plant.

Alarm logs are used to log alarms that occur in the monitored process.

#### Principle

The different types of logs all have roughly the same structure and largely work in the same way. They are very clear and easy to configure. With all three types of log you define the same properties for the log type.

All three log types can be broken down into individual segments. Segmenting can be made based on size or time.

There are two types of logs available for data logs:

- Fast data log  
  This type of log is used to log process data that change rapidly with a cycle time &lt;= 1 min.
- Slow data logs  
  This type of log is used to log all process data not covered by the "Fast data log" type. In the configuration, you can specify several parameters to define the tag values to be saved in a certain type of log.

The alarm log settings are independent of the data log settings.

---

**See also**

[Properties of logs (RT Professional)](#properties-of-logs-rt-professional)
  
[Log Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-basics-basic-panels-panels-comfort-panels-rt-advanced)

### Properties of logs  (RT Professional)

#### Introduction

You can configure the basic properties of logs in Runtime Professional, such as the segment size, in the "Runtime settings &gt; Logging" dialog. The settings configured in this dialog apply to all the logs in the project.

You configure the special properties for the individual log types either directly in the table of the respective editor or in the log properties of the Inspector window.

You configure the logical organization of data logs and compressed logs in the "Historical Data" editor. See "[Data logging](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-logging-rt-professional-1)" for additional information.

There are no comparable logical structures within the log for alarm logs. This means there is no separate "Alarm log" editor in Runtime Professional. You can only specify whether or not an alarm should be logged. You configure logging of alarms in the "HMI alarms" editor in the "Alarms classes" tab. See "[Basics on alarm logging](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-alarm-logging-rt-professional)" for additional information.

#### Properties

The following properties are available for segmenting:

- Time period of all segments
- Maximum size of all segments
- Time period contained in one single segment
- Maximum size of a single segment
- Time of first segment change

You can also specify how and when backups are to be created.  
Additional properties are available for the "Fast data" log type which you can use to divide the process data between the "Fast" and "Slow" log types.  
See "[Logging Settings](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#logging-settings-rt-professional)" for more details.

---

**See also**

[Data logging (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-logging-rt-professional-1)
  
[Basics on alarm logging (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-alarm-logging-rt-professional)
  
[Logging Settings (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#logging-settings-rt-professional)
  
[Log basics (RT Professional)](#log-basics-rt-professional)
  
[Data logging (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-logging-rt-professional)
  
[Configuring alarm logging (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-alarm-logging-rt-professional)

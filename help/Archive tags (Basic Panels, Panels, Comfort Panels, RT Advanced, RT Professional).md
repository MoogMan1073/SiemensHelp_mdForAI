---
title: "Archive tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: DataLogsWCCPenUS
topics: 58
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Archive tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
- [Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)](#data-logging-basic-panels-panels-comfort-panels-rt-advanced)
- [Data logging (RT Professional)](#data-logging-rt-professional)

## Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)

### Introduction

Data logging is used to collect, process and log process data from an industrial system.

When you analyze the logged process data, you can extract important business and technical information regarding the operational state of the system.

### Application of the data logging

You can use data logging to analyze error statuses and to document the process. By analyzing data logs, you can extract the information necessary to allow you to optimize maintenance cycles, increase product quality and ensure that quality standards are met.

---

**See also**

[Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)](#data-logging-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Data logging (RT Professional)](#data-logging-rt-professional-1)

## Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with data logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-data-logs-basic-panels-panels-comfort-panels-rt-advanced)

### Basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)](#data-logging-basic-panels-panels-comfort-panels-rt-advanced-1)

#### Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Data is information that is collected during the process and saved in the memory of one of the connected automation systems. They represent the status of a plant in the form of temperatures, fill levels or switching states, for example. You define tags for acquiring and editing the process values in WinCC.

External tags are used in WinCC to collect process values and to access a memory address in the connected automation system. Internal tags are not linked to any process and are only available at the associated HMI device.

##### Principle

The values of external and internal tags can be saved in data logs. Create a logging tag for every tag and specify the log in which it is saved.

Data logging is controlled via cycles and events. Logging cycles are used to ensure continuous acquisition and storage of the tag values. You can also trigger data logging in response to events, such as the change in value of a tag. Define these settings independently for each logging tag.

![Principle](images/68176539019_DV_resource.Stream@PNG-en-US.png)

The tag values to be logged are compiled, processed and saved in the data log in Runtime. The HMI device you are using determines where the data log is saved. You can further process the saved data in other programs for analysis purposes, for example.

##### Logging methods

WinCC supports the following logging methods:

- Circular log
- Segmented circular log
- Circular log which sends a system alarm when it is full
- Circular log which executes system functions when it is full.

##### Outputting logged data

In runtime, you can output the logged tag values as trends in the process screens.

---

**See also**

[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

### Working with data logs (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a data log (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-data-log-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing logging behavior when Runtime starts (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-logging-behavior-when-runtime-starts-basic-panels-panels-comfort-panels-rt-advanced)
- [Controlling the Logging in relation to the Fill Level (Basic Panels, Panels, Comfort Panels, RT Advanced)](#controlling-the-logging-in-relation-to-the-fill-level-basic-panels-panels-comfort-panels-rt-advanced)
- [Logging process values (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-process-values-basic-panels-panels-comfort-panels-rt-advanced)
- [Triggering a system function when log is full (Basic Panels, Panels, Comfort Panels, RT Advanced)](#triggering-a-system-function-when-log-is-full-basic-panels-panels-comfort-panels-rt-advanced)
- [System functions for logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#system-functions-for-logs-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-basic-panels-panels-comfort-panels-rt-advanced)
- [Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#evaluating-the-checksum-of-log-data-basic-panels-panels-comfort-panels-rt-advanced)
- [Log response to language switching in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Logging tags in the "Historical Data" editor (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-in-the-historical-data-editor-basic-panels-panels-comfort-panels-rt-advanced)

#### Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In Runtime, you store tag values in logs. You can then analyze the logged data at a later date. You define the following conditions for logging a tag:

- The log tag, through which the values of the connected tag are logged.
- The data log in which the tag is stored.
- The cycle or the event with which the tag is stored.
- The value range within which the tag is stored.

  > **Note**
  >
  > You use data logging mainly to log the values of external tags. You can also log the values of internal tags.

##### Principle

Several steps come together during data logging:

- Creating and configuring the data log

  When you create a data log, you define the following settings:

  - General settings, such as name, size and storage location
  - Runtime start characteristics
  - Behavior when the log is full
- Configuring the logging of tags

  For every log tag, specify a data log in which the values of the connected tags and other information are logged, such as the time of logging.

  When and how often the values of a log tag are logged are also defined. You have the following options:

  - "On demand":

    The tag values are logged by calling the "LogTag" system function.
  - "On change":

    The tag values are logged as soon as the HMI device detects a change in the value of the tag.
  - "Cyclic":

    The tag values are logged at regular intervals. You can supplement the default cycles in WinCC with your own cycles based on the default cycles. The smallest value that can be set is 1 s. All other values are integer multiples of this value.

    You can also restrict the logging of values within or outside a tolerance band. In this way, the logging of values within a relevant range of values is restricted.

  Note the following points if you want to log a tag on demand:

  - Do not log this type of tag in a segmented circular log in which tags are logged in a continuous cycle or in response to changes.

  Background:

  - If logging takes place on demand only rarely, the log segment will be filled by cyclically-logged values, for example, and the next log segment will be created. If you then attempt to access the tag that was logged on demand, it will not be possible to display the tag since it is the current log segment that is accessed in Runtime. To remedy this, you should create a separate data log for tags that are logged only rarely.
- Further processing logged tag values

  You can analyze the logged tag values directly in your project, such as in a trend view, or in another user program, such as Excel.

---

**See also**

[Configuring logging tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating a data log (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-data-log-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing logging behavior when Runtime starts (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-logging-behavior-when-runtime-starts-basic-panels-panels-comfort-panels-rt-advanced)
  
[Controlling the Logging in relation to the Fill Level (Basic Panels, Panels, Comfort Panels, RT Advanced)](#controlling-the-logging-in-relation-to-the-fill-level-basic-panels-panels-comfort-panels-rt-advanced)
  
[Logging process values (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-process-values-basic-panels-panels-comfort-panels-rt-advanced)
  
[Triggering a system function when log is full (Basic Panels, Panels, Comfort Panels, RT Advanced)](#triggering-a-system-function-when-log-is-full-basic-panels-panels-comfort-panels-rt-advanced)
  
[System functions for logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#system-functions-for-logs-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[Data logging (Basic Panels, Panels, Comfort Panels, RT Advanced)](#data-logging-basic-panels-panels-comfort-panels-rt-advanced-1)
  
[Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-basic-panels-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#evaluating-the-checksum-of-log-data-basic-panels-panels-comfort-panels-rt-advanced)
  
[Log response to language switching in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a data log (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Data logs are used to store values from external and internal tags in runtime. When you create a log, you must give it a name and define its size and storage location. In addition you can enter comments for each log.

##### Requirement

- A project is open.
- The Inspector window is open.

##### Procedure

To create a data log, proceed as follows:

1. Double-click on the "Historical Data" entry in the project tree.

   The editor for data logs and alarm logs opens.
2. Open the "Data logs" tab and double-click "Add" in the "Name" column of the "Data logs" editor.

   A new data log is created.
3. In the Inspector window select "Properties &gt; Properties &gt; General."
4. Enter a unique name for the log in the "Name" field.
5. Define the number of data records to be logged in each log in the "Number of data records per log" field.

   The size of a log is calculated as follows: The number of items * the length of each tag value to be logged.

   In the Inspector window, the maximum size that the log can reach if the currently selected number of data records is observed is displayed beneath the "Number of data records" input field.
6. In the "Storage location" field you select where the log entries are saved.
7. Depending on the selected "Storage location", you either select the "Path" or the "Name of the data source".
8. If necessary, enter a descriptive text in the "Comment" category to document your configuration.

Alternatively you can configure log properties directly in the "Data log" editor. To view hidden columns, activate the column titles using the shortcut menu.

##### Result

The data log is created.

You can now configure tags so that their values are stored in this log.

To continue the log configuration, perform the following steps:

- Define the restart characteristics of the log when Runtime is started.
- Define how the log should behave when it is full.
- Configure a function list for the "Overflow" event.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing logging behavior when Runtime starts (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

When you configure a log, you define the restart characteristics of the log when Runtime is started. You define whether the logging should start when Runtime starts in the log properties. You can also define whether an existing log will be continued or overwritten.

You define the restart characteristics separately for each log.

##### Requirement

- You have created a log.
- The "Historical Data" editor is open.
- The Inspector window with the log properties is open.

##### Procedure

To configure the restart characteristics of a data log, proceed as follows:

1. Select the log for which you want to define the restart characteristics in the "Historical Data" editor.
2. In the Inspector window select "Properties &gt; Properties &gt; Restart behavior".
3. If you want logging to start when Runtime starts, enable the "Enable logging at runtime start" option in the "Logging" area.  
   You can also start logging in Runtime using the "StartLogging" system function, for example.
4. Select the restart behavior of the log in the "Log handling at restart" area.

   - The logged values are deleted and logging is started again with the option "Reset log".
   - The option "Append data to existing log" is used to append the values to be logged to the existing log.

Alternatively you can configure the restart characteristics of a log directly in the "Historical Data" editor. To view hidden columns, activate the column titles using the shortcut menu.

##### Result

Logging will start in runtime according to your settings.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### Controlling the Logging in relation to the Fill Level (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The size of a log is determined by the number of entries. You use the logging method to determine how the log responds when it is full.

##### Logging methods

The following logging methods are available:

- ![Logging methods](images/70502244875_DV_resource.Stream@PNG-de-DE.png) Circular log

  When the configured log size has been reached, the oldest entries are deleted. When the configured log size has been reached, approximately 20% of the oldest entries are deleted. It is therefore not possible to display all the configured entries. During configuration, select an appropriate size for the circulation log. Alternatively, configure a segmented circular log.
- ![Logging methods](images/70509190539_DV_resource.Stream@PNG-de-DE.png) Segmented circular log

  In a segmented circular log, multiple log segments of the same size are filled in succession. When all logs are completely full, the oldest log is overwritten.
- ![Logging methods](images/70509198347_DV_resource.Stream@PNG-de-DE.png) Log that sends a system alarm when it is full

  When a defined level is reached, such as 90 %, a system alarm is triggered. When the log is 100% full, new tag values are not logged.
- ![Logging methods](images/70509564555_DV_resource.Stream@PNG-de-DE.png) Log with level-dependent triggering of an event.

  When the log is completely full, the "Overflow" event is triggered. Configure a function list for the event that will be carried out when the "Overflow" event occurs. When the configured size of the log is reached, new tag values are not logged.

  The following system functions are available for further processing of full logs:

##### Requirement

- You have created a log.
- The "Historical Data" editor is open.
- The Inspector window with the log properties is open.

##### Procedure

1. Select the log for which you want to define the logging method in the "Historical Data" editor.
2. Select "Properties &gt; Properties &gt; Logging method" in the Inspector window and select the required logging method.
3. If you have selected the "Segmented circular log" type, enter the number of log segments. The system creates an additional log segment for the main log. This results in the total number of log files created from the number of configured segments as well as the automatically created log.

   If you selected a log with the "Display system alarm on" setting, specify the level as a percentage at which a system alarm is to be triggered.

   If you selected the "Trigger event" setting, configure the function list in the "Events" group.

Alternatively you can configure the logging method directly in the "Historical Data" editor table. To view hidden columns, activate the column titles using the shortcut menu.

The "Overflow" event is not available in the editor table. You must therefore configure the function list in the Inspector window.

##### Result

The selected log responds according to the settings in Runtime.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[System functions for logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](#system-functions-for-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Logging process values (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can save the process values of a tag in a data log in Runtime. You define the following conditions for logging a tag:

- The log tag, through which the values of the connected tag are logged.
- In which log the values are stored
- The conditions under which the values are stored
- If only process values for a certain range of values are stored

To log the tag values, assign a logging tag to an HMI tag. The logging tag is stored in the data log and logs the values of the connected HMI tag. You can configure logging tags directly in the "HMI tags" editor. The " HMI tags" editor contains the "Logging tags" editing table.

![Introduction](images/76062685067_DV_resource.Stream@PNG-en-US.png)

If the view of the "Logging tags" table is minimized, click the arrow button below the tag table.

![The "Logging tags" table is displayed.](images/76062680587_DV_resource.Stream@PNG-en-US.png)

The "Logging tags" table is displayed.

##### Requirement

- The data log has been created.
- The tag for which you wish to configure the logging must already exist.
- The "Tags" editor is open.
- The "Logging tags" table is displayed.
- The Inspector window with the tag properties is open.

##### Procedure

To log process values in a tag, proceed as follows:

1. Select a tag in the tag table.
2. Double-click "Add" in the "Name" field in the "Logging tags" table.  
   A new logging tag is created; it is given the same name as the associated HMI tag.
3. Select the data log in which the values of the tags are to be logged under "Properties &gt; Properties &gt; General" in the Inspector window.
4. Select "Properties &gt; Properties &gt; Logging type" in the Inspector window and select the log type for logging.

   - "Cyclic": The tag values are logged in accordance with the set logging cycle.
   - "On change": The tag values are logged, as soon as the operator device detects a change in value.
   - "On demand": The tag values are logged by calling the "LogTag" system function.
5. If you want to log tag values cyclically, select a cycle time in the "Logging cycle" area. Alternatively, you can define your own cycle using the object list. The smallest value that can be set is 1 s. All other values are integer multiples of this value.
6. If you only want to log tag values outside or inside a defined value range, select "Properties &gt; Properties &gt; Deadband for logging" in the Inspector window. Define the values for the high and low limits.

   If you want to configure a dynamic limit, select "HMI tag" using the selection button. In the second field, select the tag that contains the limit.

   If you want to configure a fixed limit, select "Constant." Enter the limit value in the second field.

   If you want to leave a limit undefined, select "None".
7. Under "Scope", specify whether tag values are to be logged only if they are within the defined limits or only if they are outside the defined limits.

Alternatively, you can configure the logging of a tag directly in the "Logging tags" editor table. To view hidden columns, activate the column titles using the shortcut menu.

You can also fully configure a logging tag in the "Historical Data" editor.

##### Result

The process values of the configured tag are logged in Runtime according to the selected settings.

> **Note**
>
> To have the tag values actually logged in runtime, you must ensure that the data log is started. Logging can be started automatically at start up or by means of a system function. To automatically start the log, use the setting in the log Properties window.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### Triggering a system function when log is full (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can select a logging method that executes a function list as soon as the log is full.

##### Application example

You can use system functions, for example, to swap the data from a full log file out to another log before the full log is overwritten. You can then continue to process the transferred data in another program. Assign the "CopyLog" system function to the "Overflow" event accordingly.

##### Requirement

- A log with the "Trigger event" logging method is created.
- The "Data log" editor is open.
- The Inspector window with the data log properties is open.

##### Procedure

To configure a system function for the "Overflow" event, proceed as follows:

1. Select the required log in the table in the "Data Log" editor.
2. In the Inspector window select "Properties &gt; Events &gt; Overflow."

   The function list will open.
3. Double-click "Add function" and select the desired system function.
4. Configure the required parameters of the selected system function.

##### Result

During runtime, the function list will be executed as soon as the log is full.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### System functions for logs (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### System functions

The following system functions are available for logging:

| Function name | How it works |
| --- | --- |
| ArchiveLogFile | This function moves or copies a log to another storage location for long-term archiving. Use the system function if you want to move the Audit Trail, for example, from a local storage medium to the server.  With Audit Trails, always use the "Move log (hmiMove)" mode, otherwise you will be violating the FDA guideline by duplicating the data stored. |
| LogTag | Saves the value of the given tags in the given data log. Use the system function to log a process values at a specific time. |
| StartLogging | Starts the logging process in the specified log. You can interrupt logging in Runtime by calling the "StopLogging" system function. |
| StopLogging | Stops the logging process in the specified log. To resume logging in Runtime, select the "StartLogging" system function. |
| ClearLog | Deletes all entries in the specified log. |
| StartNextLog | Stops the logging process in the specified log. Logging is continued in the log segment that has been configured for the given log. |
| CloseAllLogs | Closes all logs. The connection between WinCC and the log files or log database is terminated. You can use this system function, for example, to enable hot-swapping of the storage medium on the HMI device without exiting the Runtime software. |
| OpenAllLogs | Opens all logs to resume logging. The connection between WinCC and the log files or log database is restored. |
| CopyLog | Copies the contents of the specified log to another log. |

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In a regulated project, you have the option of assigning a checksum to the log data of an data log or alarm log. This checksum can be used during plant operation to determine if the data of this log has subsequently changed.

> **Note**
>
> **Device dependency**
>
> The "Checksum" option is only available for display and HMI devices which support "Configuration conforms to GMP".

##### Requirements

- GMP compliant configuration is enabled.
- A data log or alarm log has been created.

##### Procedure

Proceed as follows to configure a data log or alarm log for the use of a checksum:

1. Open the data log or alarm log in the corresponding log editor.
2. In the "Storage location" box, select "File - CSV (ASCII)" or "File - TXT (Unicode)".

   ![Procedure](images/70806916747_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70806916747_DV_resource.Stream@PNG-en-US.png)
3. Under "Properties &gt; Properties &gt; Logging method" in the Inspector window, select the option "Display system event at" or "Trigger event".

   ![Procedure](images/70807230603_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70807230603_DV_resource.Stream@PNG-en-US.png)
4. In the editor table, activate the option "Enable checksum".
5. In the editor table, activate the option "Enable logging at runtime start".  
   Columns that are not displayed are activated with the shortcut menu of the column title.

   ![Procedure](images/70807595659_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70807595659_DV_resource.Stream@PNG-en-US.png)
6. Save the project.

##### Result

The log data of the log is assigned a checksum in runtime.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)](#evaluating-the-checksum-of-log-data-basic-panels-panels-comfort-panels-rt-advanced)

#### Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

If you have configured a data log or alarm log with generation of a checksum, you can check if the log data has subsequently changed.

> **Note**
>
> **Device dependency**
>
> The "Checksum" option is only available for display and HMI devices which support "Configuration conforms to GMP".

The DOS program "HmiCheckLogIntegrity" is available for checking the integrity of the log data.

The "HmiCheckLogIntegrity" program supports verification of the following files:

- Log files of alarm logs, data logs, and Audit in CSV format
- Log files of alarm logs, data logs, and Audit in TXT format
- Recipe data records in CSV format
- Recipe data records in TXT format

You can find the "HmiCheckLogIntegrity.exe" program in the installation directory of WinCC under the folder "WinCC Runtime Advanced", for example &lt;C:\Program Files\Siemens\Automation WinCC Runtime Advanced&gt;.

> **Note**
>
> **Audit Trail and Log with Checksum**
>
> Before you update WinCC with a Service Pack or a new version, exit and save the Audit Trail or the logs using checksum. After WinCC is updated, the audit trail or logs will be continued with new files using checksum.
>
> Make sure that the logs are started at a defined state with the new version.

##### Procedure

1. Copy the file to be checked from the HMI device to your configuration computer.
2. Open a command line prompt with "Start &gt; Programs &gt; Accessories &gt; Command Prompt".
3. Enter the path to "HmiCheckLogIntegrity.exe" followed by a space in the command line prompt. After the space, enter the storage location of the file to be checked within quotation marks.
4. Press &lt;Enter&gt;.
5. The check is performed.

   When the checked data are consistent, the "Consistency check succeeded" message appears.

   ![Procedure](images/12695302411_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/12695302411_DV_resource.Stream@PNG-de-DE.png)

   When the checked data are inconsistent, the "Consistency check failed" message appears. Information about the first inconsistent line in the file is also displayed.

   ![Procedure](images/12695310347_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/12695310347_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If there are spaces in the path to the "HmiCheckLogIntegrity.exe" program, you need to specify the path in quotation marks.

You can also check the integrity of the log data with the AuditViewer.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-basic-panels-panels-comfort-panels-rt-advanced)
  
[Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[Evaluating Audit Trails in AuditViewer (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#evaluating-audit-trails-in-auditviewer-panels-comfort-panels-rt-advanced)

#### Log response to language switching in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In the Runtime settings of your HMI device, select the language to be used for writing to logs in runtime.

##### Requirement

- The languages used in your project are activated in the "Project languages" editor, for example, "German (Germany)" and "English (USA)" .

##### Procedure

To determine the startup language, follow these steps:

1. Select "Runtime settings &gt; Language and fonts" in the project navigation.
2. Activate the runtime language, for example, "German (Germany)" and "English (USA)".
3. Set the "Language switch order". Use 0 to determine the startup language, for example:

   - German 0.
   - English 1

     With "0", German is specified as the "Startup language".
4. Select "Runtime settings &gt; General" in the project navigation.
5. Select the "Logs &gt; Logging language &gt; Startup language".

##### Result

The project starts after it is transferred. German is specified as the "Startup language" with "Language switch order". The logs are now written in German. During runtime, the operator switches the runtime language to English. The logs will still to be written in German.

The operator closes runtime. Due to the previously performed language switch, the next time the system starts the "startup language" is English. Since English is the startup language, the logs are now written in English.

The logging language remains English even when the language is switched again in runtime until runtime is closed once again.

If you use another option instead of "Startup language" to select the language, the logs are always written in the same language. This is true regardless of the language selected by the operator in runtime.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

#### Logging tags in the "Historical Data" editor (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring logging tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring logging tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

You can also create and edit logging tags in the "Historical Data" editor in WinCC. You also directly edit the properties of logging tags in the "Historical Data" editor.

> **Note**
>
> If you delete, move or copy in the "Historical Data" editor, the changes also take effect in the tag table.

###### Requirement

- The "Data logs" tab is open in the "Historical Data" editor.
- A data log has been created.

###### Procedure

Proceed as follows to configure a logging tag in the "Historical Data" editor:

1. Select an existing data log in the "Data logs" table of the editor.  
   Alternatively, double-click on "Add..." in the "Name" column to create a new data log.

   ![Procedure](images/111883693195_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111883693195_DV_resource.Stream@PNG-en-US.png)
2. Double-click "Add ..." in the "Name" column of the editor "Logging tags" table.

   ![Procedure](images/76062817163_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062817163_DV_resource.Stream@PNG-en-US.png)
3. Enter a unique name for the logging tag in the "Name" field.
4. In the "Process tag" field, click on the selection button and select the process tag for logging in the object list.

   ![Procedure](images/76062821643_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062821643_DV_resource.Stream@PNG-en-US.png)
5. Select the desired trigger mode in the "Log type" field:

   - "Cyclic": The tag values are logged in accordance with the set logging cycle.
   - "On change": The tag values are logged, as soon as the operator device detects a change in value.
   - "On demand": The tag values are logged by calling the "LogTag" system function.
6. If you want to log tag values cyclically, select the desired cycle time in the "Logging cycle" area. Alternatively, you can define your own cycle using the object list. The smallest value that can be set is 1 s. All other values are integer multiples of this value.
7. Configure additional parameters for logging in the table of the editor or in the Inspector window.

###### Result

The configured logging tag is created in the "Historical Data" editor and is also displayed in the tag table.

---

**See also**

[Logging Tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-tags-basic-panels-panels-comfort-panels-rt-advanced)

## Data logging (RT Professional)

This section contains information on the following topics:

- [Data logging (RT Professional)](#data-logging-rt-professional-1)
- [Basics (RT Professional)](#basics-rt-professional)
- [Working with data logs (RT Professional)](#working-with-data-logs-rt-professional)

### Data logging (RT Professional)

#### Introduction

The logging system is used for data logging in Runtime. The logging system processes the process values cached in the Runtime database and writes them to the logging database.

![Introduction](images/7806407819_DV_resource.Stream@PNG-en-US.png)

The following WinCC subsystems are involved in the data logging:

- Automation system (AS): Saves the process values that are sent to WinCC via communication drivers.
- Data manager (DM): Processes the process values and returns them to the logging system via process tags.
- Log system: Processes the acquired process values (by calculating the average, for example). The method of processing depends on the configuration of the log.
- Runtime database (DB): Saves the process values that are to be logged.

#### Term definitions

The question of whether and when process values are acquired and logged is dependent on a variety of parameters. The parameters to be configured depend on the applied logging method:

- Acquisition cycle: Determines when the value of a process tag is read out in the automation system. You can, for example, configure an acquisition cycle for cyclic data logging.
- Logging cycle: Determines when the processed process value is saved in the log database. You can, for example, configure a logging cycle for cyclic data logging.
- Start/stop tag: Starts data logging when the assigned binary tag has the value "1". Logging stops as soon as the start condition is no longer in effect. You can configure a start/stop tag for cyclic-selective data logging.
- Logging on demand: Process values are logged only upon demand. The request is controlled by a binary tag. Use the "Upon demand" trigger mode for the configuration.
- Data logging on change: Process values are logged only when they have changed. Use the "On change" trigger mode for the configuration.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional-1)
  
[Using Logging Tags (RT Professional)](#using-logging-tags-rt-professional)
  
[Logging Settings (RT Professional)](#logging-settings-rt-professional)
  
[Configuring logging tags (RT Professional)](#configuring-logging-tags-rt-professional)
  
[Function for status check of the log lock (RT Professional)](#function-for-status-check-of-the-log-lock-rt-professional)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)

### Basics (RT Professional)

This section contains information on the following topics:

- [Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
- [Logging tags (RT Professional)](#logging-tags-rt-professional)
- [Telegram Tags (RT Professional)](#telegram-tags-rt-professional)
- [Structure of a Telegram with Raw Data Tags (RT Professional)](#structure-of-a-telegram-with-raw-data-tags-rt-professional)
- [Types of Logging (RT Professional)](#types-of-logging-rt-professional)
- [Storing Process Values (RT Professional)](#storing-process-values-rt-professional)
- [Swapping Out Process Values (RT Professional)](#swapping-out-process-values-rt-professional)
- [Significance of Archive Value Flags (RT Professional)](#significance-of-archive-value-flags-rt-professional)

#### Basic principles for data logging (RT Professional)

##### Introduction

Data logging is used to collect, process and log process data from an industrial system. When you analyze the logged process data, you can extract important business and technical information regarding the operational state of the system.

##### How it works

The process values to be logged are compiled, processed and saved in the log database in Runtime. Current or previously logged process values can be output in Runtime as a table or trend. In addition, it is possible to print out logged process values as a report.

##### Configuration

You configure the logging of process values in the "Historical Data" editor. You create data logs and compressed logs. You define the acquisition cycles, logging cycles, and select the process values to be logged.

You configure trend views and table views for displaying process data in Runtime in the "Screens" editor. These views allow you to output the process data in the form of trends and tables.

You configure the output of logged process data in report format in the "Reports" editor. You output the process data in the report as a table or a trend.

##### Application

You can use data logging for the following tasks:

- Early detection of danger and fault conditions
- Increase of productivity
- Increase of product quality
- Optimization of maintenance cycles
- Documentation of process value trends

---

**See also**

[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional)
  
[Storing Process Values (RT Professional)](#storing-process-values-rt-professional)
  
[Swapping Out Process Values (RT Professional)](#swapping-out-process-values-rt-professional)
  
[Significance of Archive Value Flags (RT Professional)](#significance-of-archive-value-flags-rt-professional)
  
[Trigger mode (RT Professional)](#trigger-mode-rt-professional)
  
[Telegram Tags (RT Professional)](#telegram-tags-rt-professional)
  
[Structure of a Telegram with Raw Data Tags (RT Professional)](#structure-of-a-telegram-with-raw-data-tags-rt-professional)

#### Logging tags (RT Professional)

##### Introduction

The values of external and internal tags are stored in logging tags in a data log.

##### Logging tags

There must be one archive tag created in the data log for every tag whose values are to be logged. There are suitable types of logging tags for the various tag data types. We distinguish between the following types of logging tag:

- A binary tag stores binary process values, such as whether a motor was switched on or off.
- An analog tag stores numerical process values, such as the fill level of a tank.
- A text tag stores, e.g. product IDs or batch names.

Archived process values can be compressed. This compression is achieved through the application of mathematical functions, for example, averaging. Compressed process values of this type are stored in compressed logging tags in a compressed log.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)

#### Telegram Tags (RT Professional)

##### Introduction

Telegram tags are needed to acquire quickly changing process values or to combine several measuring points from one plant.

> **Note**
>
> Telegram tags are of the "raw data type" in WinCC and are therefore also referred to a "raw data tags".

##### Principle

In the automation system the process values are written to a binary file, and are sent as a telegram to WinCC where they are stored in a raw data tag.

##### Archiving of Telegrams

If you want the acquired process values belonging to a raw data tag to be archived, you need to configure a process-controlled tag in the data log. To enable the archive system to process the telegram in the process-controlled tag, select a format DLL. The format DLL is supplied with the automation system that you are using and dismantles the telegram, for example, to ascertain the process values. The process values are then written to the archive database.

A format DLL for the SIMATIC S7 is included as standard in the scope of delivery of WinCC.

If you want to log a raw data tag, you have to activate the "Archive data link" option in the properties of the raw data tag. In the Inspector window, activate the option under "Properties &gt; Properties &gt; Raw data". When the option "Archive data link" is activated, you can select and connect the raw data tag at the logging tag under "Properties &gt; General" in the "Process tag" field.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
  
[Structure of a Telegram with Raw Data Tags (RT Professional)](#structure-of-a-telegram-with-raw-data-tags-rt-professional)

#### Structure of a Telegram with Raw Data Tags (RT Professional)

##### Introduction

A telegram for the transfer of raw data tags consists of two parts: a header and a body.

![Introduction](images/76062826123_DV_resource.Stream@PNG-en-US.png)

##### Telegram header

The header contains general data, i.e. length of the telegram. The high byte of data word 0 is not used by the system and might thus be assigned by the user as required.

![Telegram header](images/76062843403_DV_resource.Stream@PNG-en-US.png)

##### Telegram body

In the block status word, the format of the measurement values and the format of the measurement areas, among other things, are defined. Bit 10 is reserved and will be used in future versions for switching daylight saving and standard times (daylight saving time = 1).

![Telegram body](images/76062847883_DV_resource.Stream@PNG-en-US.png)

Time and date are structured in accordance with the definition of the sequential time indication.

![Telegram body](images/76062852363_DV_resource.Stream@PNG-en-US.png)

If a measurement range is also to be transferred, 8 data words are needed in which the upper and lower limits of the tag and the archive are specified.

![Telegram body](images/76062869643_DV_resource.Stream@PNG-en-US.png)

The following section contains a number of sample telegram types.

**Type 1**

Measured value of a process tag + date and time

![Telegram body](images/76062874123_DV_resource.Stream@PNG-en-US.png)

**Type 2**

n measured values of a process tag + date and time of each measured value

![Telegram body](images/76062878603_DV_resource.Stream@PNG-en-US.png)

**Type 3**

n measured values of a process tag with date and time, and sampling cycle

![Telegram body](images/76062883083_DV_resource.Stream@PNG-en-US.png)

**Type 4**

n measured values of various process tags with time and date

![Telegram body](images/76062887563_DV_resource.Stream@PNG-en-US.png)

**Type 5**

n measured values of various process tags without time and date

![Telegram body](images/76062892043_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
  
[Telegram Tags (RT Professional)](#telegram-tags-rt-professional)

#### Types of Logging (RT Professional)

This section contains information on the following topics:

- [Trigger mode (RT Professional)](#trigger-mode-rt-professional)
- [Cycles and Events (RT Professional)](#cycles-and-events-rt-professional)
- [Cyclic data logging (RT Professional)](#cyclic-data-logging-rt-professional)
- [Cyclic-selective data logging (RT Professional)](#cyclic-selective-data-logging-rt-professional)
- [Data logging on demand (RT Professional)](#data-logging-on-demand-rt-professional)
- [Data logging on change (RT Professional)](#data-logging-on-change-rt-professional)
- [Compressed log (RT Professional)](#compressed-log-rt-professional)

##### Trigger mode (RT Professional)

###### Introduction

You can use different logging methods to log process values. This will allow you to monitor an individual process value at certain times, for example. You make the monitoring dependent on certain events. You can log quickly-changing process values without increasing the system load as a result. You can also compress existing logged process values to reduce the volume of data.

###### Logging methods

The logging method is determined by the selected trigger mode. The following logging methods are available in Runtime:

- Cyclic data logging: Continuous data logging to monitor a process value, for example.
- Cyclic-selective data logging: Event-controlled, continuous data logging to monitor a process value within a specific time period, for example.
- Data logging on demand: Process values are logged only on demand from a trigger tag.
- Data logging on change: Process values are logged only when they have changed.
- Compressed log: Compression of individual logging tags or of entire data logs, such as the hourly averaging of process values that were logged every minute.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
  
[Cycles and Events (RT Professional)](#cycles-and-events-rt-professional)
  
[Cyclic data logging (RT Professional)](#cyclic-data-logging-rt-professional)
  
[Cyclic-selective data logging (RT Professional)](#cyclic-selective-data-logging-rt-professional)
  
[Data logging on demand (RT Professional)](#data-logging-on-demand-rt-professional)
  
[Data logging on change (RT Professional)](#data-logging-on-change-rt-professional)
  
[Compressed log (RT Professional)](#compressed-log-rt-professional)

##### Cycles and Events (RT Professional)

###### Introduction

Data logging is controlled via cycles and events. The acquisition and logging cycles allow you to continuously acquire and store process values. You can also trigger or end data logging by demand or by events. Cycles and events may be combined. For example, a process value can be acquired regularly, but the logging will only be triggered by a binary event.

###### Acquisition cycle

The acquisition cycle determines the interval at which the process value of a process tag is read. The shortest possible value is 500 ms. All other values are integer multiples of this value. The start time of an acquisition cycle is determined by the start time of WinCC Runtime.

> **Note**
>
> A short acquisition cycle may lead to a high system load. Select a acquisition cycle only as low as you actually need it.
>
> If you have configured the acquisition cycle of a PLC tag as "Upon change", the default cycle is 1000 ms.

###### Logging cycle

The logging cycle determines when a process value is saved in the logging database. The logging cycle is always an integer multiple of the acquisition cycle. The start time of the logging cycle depends on either the start time of WinCC Runtime or the selected starting point.

When you set the start time, the values will be logged after a delay, which will share out the logging load. Examples:

- Process values are logged in three cycles: every minute, every two minutes, and every three minutes. This causes a high logging load every six minutes. You should therefore assign a different start time to each of the three cycles.

| Logging cycle | Selected start time |
| --- | --- |
| 1 min | At 15th second Second |
| 2 min | At 30th second Second |
| 3 min | At 45th second Second |

- Many process values must be logged every ten seconds. To distribute the logging load, configure two 10-second cycles with different starting points. Logging is performed at both of the selected starting points.  
  You can configure the starting point for a cycle in the cycle properties in the "Cycles" editor.

The logging load will be distributed by the different starting points.

> **Note**
>
> If the same cycle is used for acquisition and logging, it does not necessarily mean that acquisition and logging are started simultaneously.
>
> There might be a system delay of up to the length of one acquisition cycle between the time of acquisition and the time of logging.

###### Processing method

All process values read from the process tags during the time period between acquisition and logging will be processed by the logging function. There are different processing methods available for binary and analog values.

In a data log, use one of the following processing methods for analog values:

- Current: Saves the last acquired process value.
- Total: Saves the sum of all acquired process values.
- Maximum: Saves the highest of all acquired process values.
- Minimum: Saves the lowest of all acquired process values.
- Average value: Saves the mean of all acquired process values.
- Calculation: The value to be logged is calculated from the most recently acquired process value. The calculation is made using a function created in the "Scripts" editor.

In a data log, use one of the following processing methods for binary values:

- 0 to 1: The logging takes place whenever the value changes from 0 to 1.
- 1 to 0: The logging takes place whenever the value changes from 1 to 0.
- On each change: The logging takes place whenever the value changes from 0 to 1 or from 1 to 0.
- Always: The logging depends on the selected cycle and does not depend on the change in value.

###### Events

Start events and end data logging. Conditions that trigger an event can be linked to a tag. Events are differentiated as follows in WinCC:

- Binary action: Responds to changes in a Boolean tag.

  Example: Switching on a motor starts the data logging.
- Deadband criterion: Defines an absolute or percentage value by which the newly acquired tag value has to deviate from the old tag value so that the newly acquired tag value will be logged. The value change can be absolute or relative.

  Example: Logging is triggered in response to temperature fluctuations greater than 2 %.
- Time-controlled event: Responds at a fixed time or when a defined period of time from the start of data logging has elapsed.

  Example: A log is output after every shift change.

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

##### Cyclic data logging (RT Professional)

###### Introduction

Cyclic data logging begins when Runtime starts. The process values are acquired at fixed cycles and stored in the log database. You can also specify limits. The process value is then only logged if it is within the defined limits. A comparison of the process value with the limit values takes place after acquisition of the process value.

Cyclic data logging ends when Runtime closes.

###### How it works

![How it works](images/23304922379_DV_resource.Stream@PNG-en-US.png)

The external tags in WinCC correspond to a certain process value in the memory of one of the connected PLCs. The acquisition cycle (1) determines when the process value is read from the memory of the connected PLC.

The Runtime component of the logging system processes the process value:

- Whether the process value is logged at all will depend on the way you have configured the system. For example, the process value may have to change by a certain amount or percentage (2).
- The logging function (3) defines how the acquired process values will be processed (by averaging, for example).

The logging cycle (4) determines when the processed process value is written to the log database.

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

##### Cyclic-selective data logging (RT Professional)

###### Introduction

The start of cyclic-selective data logging is controlled by a "Bool" type tag. Logging is started as soon as the tag takes the value "1" and the logging cycle has been triggered in Runtime (by default when you start Runtime). The process values are subsequently acquired at fixed cycles and stored in the log database. You can also specify limits. The process value is then only logged if it is within the defined limits. A comparison of the process value with the limit values takes place after acquisition of the process value.

Cyclic data logging is ended by the following events:

- When the tag for starting the logging has the value "0".
- When you exit Runtime.

When Runtime stops, the most recently acquired process value is also logged.

###### How it works

![How it works](images/23304926091_DV_resource.Stream@PNG-en-US.png)

The external tags in WinCC correspond to a certain process value in the memory of one of the connected PLCs. Data logging starts as soon as the tag for the start of logging has the value "1" in Runtime (2). The acquisition cycle (1) determines when the process value is read from the memory of the connected PLC.

The Runtime component of the logging system processes the process value:

- Whether the process value is logged at all will depend on the way you have configured the system. For example, the process value may have to change by a certain amount or percentage (3).
- The logging function (4) defines how the acquired process values will be processed (by averaging, for example).

When logging stops (6), the logging cycle (5) determines when the processed process value is written to the log database.

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

##### Data logging on demand (RT Professional)

###### Introduction

Data logging on demand saves the current process value to the logging database only on demand in Runtime. The demand is controlled by a trigger tag. The trigger tag is of the data type "Bool". Logging takes place every time the status of the trigger tags changes. You can also specify limits. The process value is then only logged if it is within the defined limits. A comparison of the process value with the limit values takes place after acquisition of the process value.

Data logging on demand ends when Runtime closes.

###### How it works

![How it works](images/23306286603_DV_resource.Stream@PNG-en-US.png)

The external tags in WinCC correspond to a certain process value in the memory of one of the connected PLCs. The process value is read from the PLC (1) when a request from the trigger tag (2) is received. The Runtime component of the logging system processes the process value. The current process value is then written to the logging database (3).

The process value is read anew from the connected PLC (1) with each new request from the trigger tag (2), it is processed and logged (3).

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

##### Data logging on change (RT Professional)

###### Introduction

Data logging on change saves the current process value to the log database in Runtime when the process value changes. You can also specify limits. The process value is then only logged if it is within the defined limits. A comparison of the process value with the limit values takes place after acquisition of the process value.

Data logging on change ends when Runtime closes.

###### How it works

![How it works](images/23306286603_DV_resource.Stream@PNG-en-US.png)

The external tags in WinCC correspond to a certain process value in the memory of one of the connected PLCs. The process value is read cyclically from the memory of the connected PLC (1) and monitored for change. The process value is logged when a change (2) occurs of the external tag.

The Runtime component of the logging system processes the process value.

The current process value is then written to the logging database (3).

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

##### Compressed log (RT Professional)

###### Introduction

To reduce the volume of data in the logging database, the logging tags for a specified period can be compressed. To do this, create a compressed log that will store each logged tag in a compressed log tag. The logging tags are retained, but they can also be copied, moved or deleted. The compressed log is stored in the log database in the same way as the data log.

###### How it works

This compression is achieved through the application of mathematical functions. To achieve this, one of the following functions is applied to the logged process values from a specified period:

- Maximum value: The highest process value is saved in the compressed log tag.
- Minimum value: The lowest process value is saved in the compressed log tag.
- Total: The total of all the process values is saved in the compressed log tag.
- Average value: The average process value is saved in the compressed log tag.
- Average weighted value: The average weighted process value is saved in the compressed log tag. The time period in which a tag value has not changed is included in the calculation. For tags which are acquired "on change", this function returns more meaningful results than the "Average value" function.

What happens to the old, logged process values after compression depends on which method of compression is used:

- Calculate: The process values of the logging tags of the specified period are read out and compressed. The process values of the logging tags are retained.
- Calculate and copy: The process values of the logging tags of the specified period are read out, compressed and copied to the compressed log.
- Calculate and delete: The process values of the logging tags of the specified period are read out, compressed and then deleted.
- Calculate, copy and delete: The process values of the logging tags of the specified period are read out, compressed, copied to the compressed log and then deleted.

###### Example

The following example illustrates the way that the compressed log works:

A process value is archived once every minute and returns 60 values in one hour. The compression takes place over the course of one hour by averaging, for example. Accordingly, every hour, the average of the 60 values is calculated and is stored in the compressed log tag. What happens to the 60 values depends on the compression method described above.

---

**See also**

[Creating a Compressed Log (RT Professional)](#creating-a-compressed-log-rt-professional)
  
[Creating a Compressed Log Tag (RT Professional)](#creating-a-compressed-log-tag-rt-professional)
  
[Trigger mode (RT Professional)](#trigger-mode-rt-professional)

#### Storing Process Values (RT Professional)

##### Introduction

Process values can be stored either in the log database on the hard disk or in the main memory of the Runtime logging system.

##### Storing in Archive Database

The process values to be logged are stored in two separate cyclic archives in the log database.

- Fast data log (A)
- Slow data log (B)

Each circular log consists of a configurable number of segments. You define a size in MB and a period (such as one day) for the segments.

![Storing in Archive Database](images/105036593931_DV_resource.Stream@PNG-de-DE.png)

The process values are written continuously to the first segment (1). When the configured size of the segment is reached or the time span is exceeded, the system switches to the next segment (2). When all the segments are full, the process data in the first segment is overwritten (3). In order that process data is not destroyed by the overwritten process, it can be swapped (exported).

The "Fast data log" stores the process values whose acquisition cycle is less than or equal to one minute. These process values are initially saved and compressed in a binary file. When the binary file has reached a specific size, it is stored in the cyclic archive.

The "Slow data log" stores the process values whose acquisition cycle is longer than one minute. The "Slow data log" also stores the compressed logs. The data is written immediately to the circular log and is not compressed.

> **Note**
>
> When starting Runtime, the system tests whether the configured size of a data buffer has been calculated to a sufficient size. If the configured size is too small, the system automatically adapts to the minimum size.

##### Saving in Main Memory

In contrast to storage in the log database, process values archived in the main memory are only available while Runtime is active. Storing in the main memory has the advantage, however, that the values can be written and read very quickly. The process values stored in the main memory cannot be swapped out.

> **Note**
>
> Compressed logs cannot be saved in the main memory.

##### Optimized configuration

Use the available log types and the different storage methods to match logging to the dynamics of the changing process values.

Select the logging type depending on the frequency of the value changes of a tag and the necessity for logging.

Combing the logging type with the selection of the matching circular log. Use shorter logging types, for example, only for tags whose values change quickly.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)

#### Swapping Out Process Values (RT Professional)

##### Introduction

You can swap out process values from the log database as a backup. All process values contained in a log segment are swapped out. A log segment is always swapped out when it is full and a new segment is started. A log segment is also swapped out when the time set for a segment change is reached and a new segment is started.

##### Principle

You configure the swapping out of process values in the log settings. In the settings, you configure the size of the log and the log segmentsn as well as the time for the segment change. You should also state whether a backup is made in the settings.

![Principle](images/76062909323_DV_resource.Stream@PNG-en-US.png)

In the lines of the backup configuration you define where the backup is created and whether the backup file is signed.

> **Note**
>
> You can change a displayed process value in Runtime using the table view.
>
> If the process value has already been swapped out of the data log, the modified value will not be transferred to the swapped-out log. The change only occurs in the local log segment.
>
> If the log segment has not yet been swapped, the changed value is accepted permanently.

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)
  
[Logging Settings (RT Professional)](#logging-settings-rt-professional)

#### Significance of Archive Value Flags (RT Professional)

The data logging sets flags for every value that is written to the log. The flags indicate the state of the tags.

The flags are represented by a 2-word value. This value is decimal-coded and is shown in the third column of the database log. The flags must be converted to hexadecimal format for analysis purposes.

![Figure](images/7810272523_DV_resource.Stream@PNG-en-US.png)

Structure of the 2-word value:

The High word contains the WinCC status flags or the quality code. The Low word contains the status flags for the data logging and an identifier for the content of the High word.

##### Code for High Word Content:

|  | Meaning |
| --- | --- |
| 0x0 | High word contains WinCC status flags |
| 0x1 | High word contains quality code |

##### Tag logging status flags:

| Name of flag | Value | Meaning |
| --- | --- | --- |
| PDE_RT_DAYLIGHT | 0x001 | Summer time |
| PDE_RT_SUBSTITUTION | 0x002 | Substitute value |
| PDE_RT_TIME_BEVOR_JUMP | 0x004 | Value prior to time jump |
| PDE_RT_TIME_BEHIND_JUMP | 0x008 | Value after time jump |
| PDE_RT_TIME_OVERLAPPED | 0x010 | Values during time overlap |
| PDE_RT_LOAD_SYSTEM | 0x020 | Value that is initially archived when the log is created |
| PDE_RT_RELOAD_SYSTEM | 0x040 | Initial value after archiving of RT |
| PDE_RT_CMPCOPY | 0x080 | Compressed value |
| PDE_RT_TIME_CHANGED | 0x100 | Time change took place |
| PDE_RT_HAND | 0x200 | Manual tag supply |

##### Examples

| Symbol | Meaning |
| --- | --- |
| Value in database | 16842753 |
| Hexadecimal representation | 0101 0001 |
| Coding for high word | 0: High word contains WinCC status flag |
| Data logging status flag | 001: Summer time |
| WinCC status flag | 0101: Link to partner not established; tag initialization value |

| Symbol | Meaning |
| --- | --- |
| Value in database | 266242 |
| Hexadecimal representation | 0004 1002 |
| Coding for high word | 1: High word contains quality code |
| Data logging status flag | 002: Substitute value |
| Quality codes | 0004: Configuration error, value not accepted |

---

**See also**

[Basic principles for data logging (RT Professional)](#basic-principles-for-data-logging-rt-professional)

### Working with data logs (RT Professional)

This section contains information on the following topics:

- [Creating a data log (RT Professional)](#creating-a-data-log-rt-professional)
- [Creating a Logging Tag (RT Professional)](#creating-a-logging-tag-rt-professional)
- [Specifying log settings (RT Professional)](#specifying-log-settings-rt-professional)
- [Logging tags in the "Tags" editor (RT Professional)](#logging-tags-in-the-tags-editor-rt-professional)
- [Functions for data logging (RT Professional)](#functions-for-data-logging-rt-professional)

#### Creating a data log (RT Professional)

This section contains information on the following topics:

- [Logging tags (RT Professional)](#logging-tags-rt-professional-1)
- [Creating a data log (RT Professional)](#creating-a-data-log-rt-professional-1)
- [Creating a Compressed Log (RT Professional)](#creating-a-compressed-log-rt-professional)

##### Logging tags (RT Professional)

###### Principle

For the configuration of logs, the system distinguishes between the following log types:

- The data log stores process values in logging tags. When you configure the data log, select the process tags that are to be logged and the storage location.
- The compressed log compresses logging tags from data logs. The compressed log can further compress other compressed logs. When you configure the compressed log, select a calculation method and the compression time period.

###### Data buffer

For a data log, define whether the data buffer should be created on the hard disk or in the main memory.

In contrast to storage in the log database, process values logged in the main memory are only available while Runtime is active. Storing in the main memory has the advantage, however, that the values can be written and read very quickly. The process values stored in the main memory cannot be swapped out.

> **Note**
>
> Compressed logs can only be saved on the hard disk.

---

**See also**

[Logging Settings (RT Professional)](#logging-settings-rt-professional)
  
[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Creating a data log (RT Professional)](#creating-a-data-log-rt-professional-1)
  
[Creating a Compressed Log (RT Professional)](#creating-a-compressed-log-rt-professional)
  
[Configuring logging tags (RT Professional)](#configuring-logging-tags-rt-professional)

##### Creating a data log (RT Professional)

###### Introduction

The configuration of a data log consists of the following steps:

- Create a data log.
- Configure the data log, for example, by selecting the storage location.
- Select the tags for logging.

###### Requirement

- A project is open.
- The Inspector window is open.

###### Procedure

To create a data log, proceed as follows:

1. Double-click on the "Historical Data" entry in the project tree.

   The editor for data logs and compressed logs opens.
2. Open the "Data logs" tab and double-click "Add" in the "Name" column of the "Data logs" editor.  
   A new data log is created.
3. In the Inspector window select "Properties &gt; Properties &gt; General".
4. Enter a unique name for the log in the "Name" field.
5. In the "Storage location" field, decide whether the process values should be saved in the main memory or in a database.
6. If you select "Memory" as the storage location, set the number of data records to be logged per logging tag in the "Number of data records" field.
7. In the "Status" area, use the "Locked" option to determine whether the logging process is locked at the start of Runtime.  
   If you want to start logging in Runtime, you will need to deactivate the option again.
8. If the status of the logging lock changes, you can be informed of this via a C function or configure subsequent steps. To do this, select an available C function under "Properties &gt; Properties &gt; Events" in the Inspector window. The C function is called in Runtime from the log server when the "Locked" status changes. You must first write the C function in the "Scripts" editor. See "[Function for status check of the log lock](#function-for-status-check-of-the-log-lock-rt-professional)" for additional information. Only one C function can be run by the "Changed lock" event.
9. If necessary, enter a descriptive text under "Comment" to document your project.

Alternatively you can configure log properties directly in the "Data log" editor. To view hidden columns, activate the column titles using the shortcut menu.

###### Result

The data log is created.

The next steps are to configure the higher-level logging parameters.  
See "[Specifying log settings](#specifying-log-settings-rt-professional)" for additional information.

> **Note**
>
> The log name can be up to 32 characters long.
>
> Do not use the following characters: '\\','\'', '.', ',', ';', ':', '!', '?', '"', '´', '`', '^', '~', '-', '+', '=', '/', '*', '#', '%', '&amp;', '§', '°', '(', ')', '[', ']','{', '}', '&lt;', '&gt;', '|', ' ', 'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß'
>
> Capitalization is ignored.
>
> The characters _ @ # $ cannot be used as the first character of a name.
>
> The following terms may not be used when assigning a name: "times", "userarchives", "project", "archives", "defaultarchives", "defaultvariables", "templates", "tabletemplateitems", "curvetemplateitems".
>
> The names of logs must be unique in a project. Log names must also be unique if different storage locations are selected for different logs. You must also assign different names for alarm logs and data logs.

---

**See also**

[Function for status check of the log lock (RT Professional)](#function-for-status-check-of-the-log-lock-rt-professional)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional-1)
  
[Specifying log settings (RT Professional)](#specifying-log-settings-rt-professional)

##### Creating a Compressed Log (RT Professional)

###### Introduction

The configuration of a compressed log consists of the following steps:

- Create the new compressed log.
- Configure the compressed log, for example, by selecting the calculation method and the time period for the compression.
- Select the logging tags that you want to add to the compressed log.

###### Requirement

- A project is open.
- The Inspector window is open.

###### Procedure

To create a compressed log, proceed as follows:

1. Double-click on the "Historical Data" entry in the project tree.

   The editor for data logs and compressed logs opens.
2. Open the "Compressed logs" tab and double-click "Add" in the "Name" column of the "Compressed logs" editor.  
   A new compressed log will be created.
3. In the Inspector window select "Properties &gt; Properties &gt; General".
4. Enter a unique name for the log in the "Name" field.
5. Select the processing method and compression period in the "Compression" area.

   All times created in the "Cycles" editor that are &gt;= 1 minute are available as the compression time period. If the compression cycle you want is unavailable, configure a new cycle time. Then select the new cycle as the compression time period.
6. Use the "Locked" option to determine whether the logging process is locked at the start of Runtime.  
   If you want to start logging in Runtime, you will need to deactivate the option again.
7. If the status of the logging lock changes, you can be informed of this via a C function or configure subsequent steps. To do this, select an available C function under "Properties &gt; Properties &gt; Events" in the Inspector window. The C function is called in Runtime from the log server when the "Locked" status changes. You must first write the C function in the "Scripts" editor. See "[Function for status check of the log lock](#function-for-status-check-of-the-log-lock-rt-professional)" for additional information.
8. If necessary, enter a descriptive text under "Comment" to document your project.

Alternatively you can configure log properties directly in the "Compressed log" editor. To view hidden columns, activate the column titles using the shortcut menu.

###### Result

The compressed log is created.

> **Note**
>
> The log name can be up to 32 characters long.
>
> Do not use the following characters: '\\','\'', '.', ',', ';', ':', '!', '?', '"', '´', '`', '^', '~', '-', '+', '=', '/', '*', '#', '%', '&amp;', '§', '°', '(', ')', '[', ']','{', '}', '&lt;', '&gt;', '|', ' ', 'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß'
>
> Capitalization is ignored.
>
> The characters _ @ # $ cannot be used as the first character of a name.
>
> The following terms may not be used when assigning a name: "times", "userarchives", "project", "archives", "defaultarchives", "defaultvariables", "templates", "tabletemplateitems", "curvetemplateitems".
>
> The names of logs must be unique in a project. You must also assign different names for compressed logs and data logs.

---

**See also**

[Function for status check of the log lock (RT Professional)](#function-for-status-check-of-the-log-lock-rt-professional)
  
[Compressed log (RT Professional)](#compressed-log-rt-professional)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional-1)

#### Creating a Logging Tag (RT Professional)

This section contains information on the following topics:

- [Using Logging Tags (RT Professional)](#using-logging-tags-rt-professional)
- [Creating binary logging tag (RT Professional)](#creating-binary-logging-tag-rt-professional)
- [Creating an analog logging tag (RT Professional)](#creating-an-analog-logging-tag-rt-professional)
- [Creating a Compressed Log Tag (RT Professional)](#creating-a-compressed-log-tag-rt-professional)

##### Using Logging Tags (RT Professional)

###### Principle

Logging tags are used to save the process values to be logged. Use process tags to specify which process data should be logged. The data type is automatically defined by the process tag selected. Use the trigger mode to configure whether a tag is to be logged in relation to the time or specific events.

In a compressed log, each compressed logging tag is stored in a separate compressed logging tag.

###### Basic procedure

For logging tags, specify the trigger mode, e.g. cyclic, as well as the acquisition and logging cycles. Select the parameters to start or end logging according to the trigger mode. Specify the display limits and parameters for processing the process value according to the type of logging tag.

- A binary tag stores binary process values, such as whether a motor was switched on or off.
- An analog tag stores numerical process values, such as the fill level of a tank.
- A text tag stores, e.g. product IDs or batch names.

When configuring a compressed logging tag, select the processing method for forming the logging tags to be compressed, such as the mean value.

> **Note**
>
> If you delete a logging tag, save the project and then create a new tag with the same name as the deleted tag; you can no longer access the previously saved values of the deleted tag for display or logging. Reason: The newly created logging tag is assigned a new ID. The ID of the deleted logging tag is no longer accessible.

---

**See also**

[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Creating binary logging tag (RT Professional)](#creating-binary-logging-tag-rt-professional)
  
[Creating an analog logging tag (RT Professional)](#creating-an-analog-logging-tag-rt-professional)
  
[Creating a Compressed Log Tag (RT Professional)](#creating-a-compressed-log-tag-rt-professional)

##### Creating binary logging tag (RT Professional)

###### Introduction

To configure a binary logging tag, first create a logging tag and then connect it to a binary process tag. The data type of the logging tag will then be set automatically.

Then define the properties for the logging tag.

###### Requirement

- A data log has been created.
- The binary tag for which you want to configure the logging must already exist.
- The "Historical Data" editor is open.
- The Inspector window with the logging tag properties is open.

###### Procedure

To create a binary logging tag, proceed as follows:

1. Select the data log in which you want to create the logging tag from the table in the "Data log" editor.
2. In the "Name" column of the "Logging tags" table, double-click "Add".

   An logging tag is created.
3. Select "Properties &gt; Properties &gt; General" in the Inspector window and enter a unique name for the logging tag in the "Name" field.
4. In the "Process tags" field, select the binary tags to be linked to the logging tag.  
   Use the "Locked" option to define whether logging should be enabled or disabled when Runtime starts. You will have to deactivate the option once again if you want to start the logging in Runtime.
5. To reuse the logged values for other purposes, you can also write the value of the logging tag to an internal tag. The update process is determined by the cycle settings for the logging tag. Select the required tag from the "Copy logged value to tag" field.
6. Select "Properties &gt; Properties &gt; Logging type" in the Inspector window and select the required log type.  
   See "[Trigger mode](#trigger-mode-rt-professional)" for additional information.
7. Select "Properties &gt; Properties &gt; Processing method" in the Inspector window and select the required processing method.  
   You can find more detailed information on this in the section "[Cycles and Events](#cycles-and-events-rt-professional)".
8. If necessary, enter a descriptive text under "Comment" to document your project.

You can configure the properties of a logging tag directly in the "Data log" editor. To view hidden columns, activate the column titles using the shortcut menu.

You can also configure logging tags in the tag table in the "Logging tags" tab.

###### Result

The process values of the configured tag are logged in Runtime according to the selected settings.

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)
  
[Cycles and Events (RT Professional)](#cycles-and-events-rt-professional)
  
[Using Logging Tags (RT Professional)](#using-logging-tags-rt-professional)

##### Creating an analog logging tag (RT Professional)

###### Introduction

To configure an analog logging tag, first create a logging tag and then connect it to an analog process tag. The data type of the logging tag will then be set automatically.

Then define the properties for the logging tag.

###### Requirement

- The data log has been created.
- The analog tag for which you wish to configure the logging must already exist.
- The "Historical Data" editor is open.
- The Inspector window with the logging tag properties is open.

###### Procedure

To create an analog logging tag, proceed as follows:

1. Select the data log in which you want to create the logging tag from the table in the "Data log" editor.
2. In the "Name" column of the "Logging tags" table, double-click "Add".

   An logging tag is created.
3. Select "Properties &gt; Properties &gt; General" in the Inspector window and enter a unique name for the logging tag in the "Name" field.
4. In the "Process tags" field, select the analog tags to be linked to the logging tag.  
   Use the "Locked" option to define whether logging should be enabled or disabled when Runtime starts. You will have to deactivate the option once again if you want to start the logging in Runtime.
5. To reuse the logged values for other purposes, you can also write the value of the logging tag to an internal tag. The update process is determined by the cycle settings for the logging tag. Select the required tag from the "Copy logged value to tag" field.
6. Select "Properties &gt; Properties &gt; Logging type" in the Inspector window and select the required log type.  
   See "[Trigger mode](#trigger-mode-rt-professional)" for additional information.
7. Select "Properties &gt; Properties &gt; Deadband for logging" in the Inspector window and enter the required limits. Open the selection box and select the "Constant" entry to enable the input. Then enter the required limit value. Process values outside the limits will not be logged.
8. Select "Properties &gt; Properties &gt; Processing method" in the Inspector window and select the required processing method.  
   For additional information see "[Cycles and Events](#cycles-and-events-rt-professional)".  
   You can specify a C function for converting tag values if you use the "Calculation" processing method. You must first write the C function in the "Scripts" editor. For additional information see "[Converting values from logging tags](#converting-values-from-logging-tags-rt-professional)".
9. If necessary, enter a descriptive text under "Comment" to document your project.

Alternatively you can configure log properties directly in the "Data log" editor. To view hidden columns, activate the column titles using the shortcut menu.

###### Result

The process values of the configured tag are logged in Runtime according to the selected settings.

---

**See also**

[Trigger mode (RT Professional)](#trigger-mode-rt-professional)
  
[Cycles and Events (RT Professional)](#cycles-and-events-rt-professional)
  
[Converting values from logging tags (RT Professional)](#converting-values-from-logging-tags-rt-professional)
  
[Using Logging Tags (RT Professional)](#using-logging-tags-rt-professional)

##### Creating a Compressed Log Tag (RT Professional)

###### Introduction

You can save the process values of a logging tag or a compressed tag from another compressed log in compressed form in a compressed logging tag. Select the mathematical function with which you want to compress the process values it contains.

The following compression functions are available:

- Weighted mean
- Maximum
- Minimum
- Mean value
- Sum

You create a compressed logging tag in the "Compressed log" editor.

###### Requirement

- You have created a compressed variable.
- You have created the logging tag you want to configure.
- The "Historical Data" editor is open.
- The Inspector window with the logging tag properties is open.

###### Procedure

To create a compressed logging tag, proceed as follows:

1. Click the "Compressed logs" tab in the "Historical Data" editor.  
   The "Compressed logs" editor opens.
2. Select the compressed log in which you want to create the compressed logging tag from the table in the "Compressed log" editor.
3. Click on the vertical "Logging tag" tab on the right side of the window. The "Logging tags" task card opens. The task card shows all objects you can add to the selected compressed log.

   ![Procedure](images/76062913803_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062913803_DV_resource.Stream@PNG-en-US.png)
4. In the task card, select the objects you want to add to the compressed log. You can select the following objects:

   - Single or multiple logging tags
   - A complete data log
   - One or several compressed logging tags
   - A complete compressed log
5. Open the shortcut menu of the selected object and select the menu command "Add." A compressed logging tag is created for each object selected and linked to the respective object. If you have selected a complete data log or a complete compressed log, a compressed logging tag is created for each tag contained in this log.  
   Alternatively, you can drag-and-drop the selected objects into the compressed log selected in step 2.
6. Select one or several compressed logging tags in the table of compressed logging tags. Specify more properties for the selected tags in the Inspector window.  
   Use the "Locked" option to define whether logging should be enabled or disabled when Runtime starts. If you want to start logging in Runtime, you will need to disable the option again.  
   Select the processing method for the compression in the "Compression" field.
7. If necessary, enter a descriptive text under "Comment" to document your project.

You can configure the properties of a compressed logging tag directly in the "Compressed log" editor. To view hidden columns, select these from the shortcut menu for the column titles.

###### Result

The compressed logging tags are connected to the selected logging tags. The values from the logging tag are compressed using the set parameters in Runtime.

If you have selected the compressed logging tags from another compressed log, they will be compressed even further.

---

**See also**

[Compressed log (RT Professional)](#compressed-log-rt-professional)
  
[Using Logging Tags (RT Professional)](#using-logging-tags-rt-professional)

#### Specifying log settings (RT Professional)

This section contains information on the following topics:

- [Logging Settings (RT Professional)](#logging-settings-rt-professional)
- [Defining the Log Size and Segmentation (RT Professional)](#defining-the-log-size-and-segmentation-rt-professional)
- [Configuring the log backup (RT Professional)](#configuring-the-log-backup-rt-professional)
- [Assigning Logging Tags to the Log Types (RT Professional)](#assigning-logging-tags-to-the-log-types-rt-professional)
- [Connecting the log backup (RT Professional)](#connecting-the-log-backup-rt-professional)
- [Disconnecting a log backup (RT Professional)](#disconnecting-a-log-backup-rt-professional)

##### Logging Settings (RT Professional)

###### Introduction

You configure the logical organization of data logs and compressed logs in the "Historical Data" editor. You can configure the basic properties of logs in Runtime Professional, such as the segment size, in the "Runtime settings &gt; Logging" dialog.

You make the settings for data logs separately in the dialog for the "Fast data log" and "Slow data log" types.

The following conditions apply if you are using the default settings:

The Fast data log is used to store all values with a logging cycle &lt;= 1 minute.

The Slow data log is used to store all values with a logging cycle &gt; 1 minute.

You can change the cycle limit for allocation to the log type in the "Cycle" field in the "Runtime settings &gt; Logging" dialog.

###### Overview of procedure

You configure the higher-level log configuration in the "Runtime settings &gt; Logging" dialog. The following instructions contain a description of the configuration procedure:

| Step | Description |
| --- | --- |
| 1 | [Defining the Log Size and Segmentation](#defining-the-log-size-and-segmentation-rt-professional) |
| 2 | [Configuring the log backup](#configuring-the-log-backup-rt-professional) |
| 3 | [Assigning Logging Tags to the Log Types](#assigning-logging-tags-to-the-log-types-rt-professional) |

---

**See also**

[Defining the Log Size and Segmentation (RT Professional)](#defining-the-log-size-and-segmentation-rt-professional)
  
[Configuring the log backup (RT Professional)](#configuring-the-log-backup-rt-professional)
  
[Connecting the log backup (RT Professional)](#connecting-the-log-backup-rt-professional)
  
[Disconnecting a log backup (RT Professional)](#disconnecting-a-log-backup-rt-professional)
  
[Assigning Logging Tags to the Log Types (RT Professional)](#assigning-logging-tags-to-the-log-types-rt-professional)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional-1)
  
[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Swapping Out Process Values (RT Professional)](#swapping-out-process-values-rt-professional)

##### Defining the Log Size and Segmentation (RT Professional)

###### Introduction

In the "Runtime settings &gt; Logging" dialog, you define the sizes of the "Fast data log" and "Slow data log" types in the database. You can also subdivide the two types of log into segments. The size of the individual segments thus also defines the number of individual segments.

The individual segments are filled one after the other in Runtime. Once a segment is totally full, it switches to the next segment. You can also configure the segment change at specific times. If you define a time for the segment change, the next log segment is filled when the time is reached.

> **Note**
>
> Ensure that the log size does not exceed the free memory space available. The system does not validate the selected settings. A high number of linked log segments can lead to longer waiting periods in the system when starting and ending Runtime.

###### Requirement

A project is open.

###### Procedure

To edit the higher-level log settings, proceed as follows:

1. In the project tree, open the folder containing Runtime Professional and double-click the "Runtime Settings" entry.  
   The Runtime settings dialog opens.

   ![Procedure](images/76062918283_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062918283_DV_resource.Stream@PNG-en-US.png)
2. Click the "Logging" entry in the dialog.  
   The "Logging" dialog opens.

   ![Procedure](images/76062909323_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062909323_DV_resource.Stream@PNG-en-US.png)
3. Enter the required values in the "Time period of all segments" and "Maximum size of all segments" fields.

   - When you enter the time period across all the segments and the maximum size, you also define the size of the logging database. If either of these criteria is violated, a new segment is started. When all the segments are filled, the oldest segment is overwritten.
4. Enter the required values in the "Time period contained in a single segment" and "Maximum size of a segment" fields.

   - When you enter the time period for the single segments and the maximum size, you also define the size and number of single segments. If either of these criteria is violated, a new individual segment is started. When the criterion for "Time period of all segments" is exceeded, the oldest individual segment is also deleted.
5. Enter the start date and start time for the first segment change in the "Time of first segment change" field.
6. Continue the configuration from step 2 of the procedural overview and configure the log backup. You can find more detailed information in section "[Configuring the log backup](#configuring-the-log-backup-rt-professional)".

**Note**

If you change the log size or the time period in Runtime, the change will not take effect until the next segment change.

###### Example

The input was configured:

| Property | Value |
| --- | --- |
| Time period of all segments | 1 week |
| Maximum size of all segments | 700 MB |
| Time period contained in one single segment | 1 day |
| Maximum size of a segment | 100 MB |
| Time of first segment change | Friday, 23 November 2010 18:30 |

With the configuration shown in the table, the started segment will be changed for the first time at 18:30 on 23 November 2010. The next time-controlled segment change will take place cyclically, after periods of 1 day since the configured time. The segment will also change if the configured size of 100 MB is exceeded in the course of one day. The oldest single segment will be deleted if the maximum log size of 700 MB is exceeded.

###### Changing the log type

If the user does not change the relevant settings, the logging tags will be logged with a cycle time of &lt;= 1 min in the "Fast data log". Logging tags with a cycle time &gt; 1 min will be logged in the"Slow data log". The cycle time of a logging tag must not be changed in Runtime beyond the above limits. It is not possible to change of a logging tag from "Fast" to "Slow" log type and vice-versa in Runtime.

After a cycle change or reconfiguration, if tags are to be stored in a different log type, these tags will be read from the currently valid log. Previous log values of this tag are not accessible in Runtime.

If you reconfigure the logging tags so that their values are stored in a log other than the previous log type, more memory will be required in the log concerned. You should therefore adjust the log size after making major changes.

> **Note**
>
> Runtime data in the logs will be deleted if you reset the log configuration for data logging. Only previously swapped-out databases remain intact.

###### Resetting the log database

Use the "Extended loading" dialog to reset the log database settings. Select the HMI device in the project tree for this purpose and use the menu command "Online &gt; Extended download to device". Select the interface for your HMI device. Click on "Download". The "Load preview" dialog opens. Make the settings for the reset in the "Load preview" dialog.

![Resetting the log database](images/111884750987_DV_resource.Stream@PNG-en-US.PNG)

The reset will be executed when you start the download process.

---

**See also**

[Configuring the log backup (RT Professional)](#configuring-the-log-backup-rt-professional)
  
[Logging Settings (RT Professional)](#logging-settings-rt-professional)

##### Configuring the log backup (RT Professional)

###### Introduction

Make regular backups of your log data to ensure complete documentation of your process.

> **Note**
>
> The backup normally starts 15 minutes after the first time-related segment change. If the start of backup and start of segment should be synchronous with the start of Runtime, define the start time for the segment change prior to the start of Runtime.
>
> You can change a displayed process value in Runtime using the table view. If the location of the log segment where the process value is stored has already been changed, then the modified value is not accepted in the shifted log. The change only occurs in the local log segment.
>
> If the log segment has not yet been swapped, the changed value is accepted permanently.

###### Requirement

- Step 1 of the procedural overview is complete - [Defining the Log Size and Segmentation](#defining-the-log-size-and-segmentation-rt-professional)
- The "Runtime settings &gt; Logging" dialog is open.

###### Procedure

Proceed as follows to create a log backup:

1. Activate the "Backup" option in the column containing the type of log for which you want to configure the backup, such as the "Fast data log" column.
2. In the same column, enter the storage location for the backup in the "Path" field or navigate to the desired storage location in the file system using the dialog. A network drive is also possible as the storage location.
3. If you want to create a redundant backup, select the "Backup to both paths" option.
4. Enter an alternative storage location for the backup in the "Alternative path" field, or navigate to the desired storage location in the file system using the dialog. A network drive is also possible as the storage location. The alternative storage location is used in the following situations:

   - If the storage space on a backup medium is full.
   - If the original storage location is unavailable due to a network failure, for example.

   After the corresponding system alarms have been configured, the alarms are output, if the specified storage location is not available.
5. If the log backup file should be signed, select the "Enable signing" option. On reconnecting to WinCC, the signature will allow the system to detect whether any changes were made to a log backup file after it was swapped out.
6. Continue the configuration from step 3 of the procedural overview and assign the logging tags to the log types. See the "[Assigning Logging Tags to the Log Types](#assigning-logging-tags-to-the-log-types-rt-professional)" section for more detailed information.

###### Structure of the Log Backup File

A log backup consists of two files with the extensions "*.LDF" and "*.MDF". To transfer a log backup to another computer, for example, copy the corresponding LDF and MDF files. The file name is composed as follows: "&lt;Computer name&gt;_&lt;Project name&gt;_&lt;Type&gt;_&lt;Period_from&gt;_&lt;Period_until&gt;". The type is defined by the log type:

- TLG_F: Data log with a logging cycle of one minute or less.
- TLG_S: Data log with a logging cycle of more than one minute.

The time period is specified in the following format: yyyymmddhhmm, e.g. 201012021118 for December 2, 2010, 11:18. Underscores "_" in the project name are displayed as "#".

Example:

FLEX-LOG2_WINCC#10#11#29#14#37#40_TLG_F_201011291414_201012030502.ldf

FLEX-LOG2_WINCC#10#11#29#14#37#40_TLG_F_201011291414_201012030502.mdf

###### Signing of the log backup files

If signing and backup are enabled, each log backup file is signed when it is swapped out. When the file is connected to WinCC once more, the signature is used to determine whether the file was changed after being swapped out.

If you use log signing, the maximum size of a single segment must not exceed 200 MB.

To verify the data, the "Signing enabled" option must be checked. Connecting "Slow" logs will take longer due to the signing.

The following values apply to the logging of signed data:

| Logging signed data in Runtime | Value/seconds |
| --- | --- |
| Fast data log | 1,000 |
| Slow data log | 500 <sup>1)</sup> |

<sup>1)</sup> With "Slow" type data logs, expect longer screen selection times for a given amount of data as those for "Fast" type data logs.

> **Note**
>
> If you disable signing off to establish a fast connection to the backup files, for example, you should avoid segment changes while it is disabled. After the connection has been established, signing off should be reactivated in order to enable signing off for logged data.

###### Activating and deactivating signing

You activate and deactivate signing in the Runtime settings of the HMI device.

Activate or deactivate signing. If Runtime is running on the engineering station, recompile the project. The change becomes effective after compilation. If Runtime is running on a different PC than WinCC ES, you accept the change with online delta transfer. See [Overview of online delta transfers](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-online-delta-transfers-rt-professional) for additional information.

---

**See also**

[Defining the Log Size and Segmentation (RT Professional)](#defining-the-log-size-and-segmentation-rt-professional)
  
[Assigning Logging Tags to the Log Types (RT Professional)](#assigning-logging-tags-to-the-log-types-rt-professional)
  
[Logging Settings (RT Professional)](#logging-settings-rt-professional)
  
[Overview of online delta transfers (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-online-delta-transfers-rt-professional)
  
[Connecting the log backup (RT Professional)](#connecting-the-log-backup-rt-professional)
  
[Disconnecting a log backup (RT Professional)](#disconnecting-a-log-backup-rt-professional)

##### Assigning Logging Tags to the Log Types (RT Professional)

###### Introduction

Data logging uses two different types of log to store data:

- Fast data log
- Slow data log

The logging tags are automatically allocated to the correct type of log. You can change this allocation in the log settings.

In Runtime, a changed assignment will only be accepted when the project has been deactivated and Runtime is restarted.

###### Requirement

- Step 2 of the procedural overview is complete - [Configuring the log backup](#configuring-the-log-backup-rt-professional)
- The "Runtime settings &gt; Logging" dialog is open.

###### Procedure

To allocate the logging tags to the log types, follow these steps:

1. If you want to log acquired values to the fast data log on demand, activate the "Measured values with acquisition mode "On demand"" option in the "Fast data log" column.

   ![Procedure](images/76062909323_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76062909323_DV_resource.Stream@PNG-en-US.png)
2. Activate the "Cyclically measured values with cycles less or equal" option if you want to log logging tags to the fast data log with the "cyclic" trigger mode.
3. Select a cycle time as the upper limit of the logging cycle in the "Cycle" field. If necessary, select a factor for multiplying the selected cycle time in the "Factor" field.
4. Enable the "Compressed values with shorter or equal cycle" option if you want to log all compressed values with a logging cycle that is less than or equal to the limit allocated to the Fast data log.
5. Select a cycle time as the upper limit of the logging cycle in the "Cycle" field. If necessary, select a factor for multiplying the selected cycle time in the "Factor" field.
6. Save the project.

###### Result

All logging tags to which these settings apply are logged in the Fast data log. All logging tags to which these settings do not apply are logged in the Slow data log.

---

**See also**

[Logging Settings (RT Professional)](#logging-settings-rt-professional)

##### Connecting the log backup (RT Professional)

###### Introduction

In order to access data of a log backup in Runtime, connect the log backup to the project again. You can establish the connection using a VB function or have it established automatically. You can connect all backup segments that were created with each project. A requirement is that you did not change the log or the logging tags.

###### Requirement

- The corresponding LDF and MDF files for the log backup are located in a local folder on the configuration computer, such as the hard disk, MOD or CD.
- You can connect the log files only on the server.

###### Procedure

Proceed as follows to connect a log backup using a VB function:

1. Configure a button in a process screen and label the button "Connect log backup", for example.
2. Write a VB function using the "Restore" method based on this example:

   HMIRuntime.Trace "Ret: " &amp; HMIRuntime.Logging.Restore("D:\Backup","","2010-11-14",-1) &amp; vbNewLine

   You can find more detailed information about this in "[Restore](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#restore-panels-comfort-panels-rt-advanced-rt-professional)".
3. Configure a list of functions for the "Click" event for the configured button.
4. Select the VB function thus created from the list of functions.
5. Save the project.

###### Result

The VB function is executed in Runtime when the button is clicked. The log backup is connected using the parameters defined in the function.

The logged process values from the log backup are sorted in time-stamp order in the configured display.

Connecting "Tag Logging Slow" logs takes longer if signing is enabled.

###### Automatic linking to a log

1. Insert the log backup files into the "CommonArchiving" folder.  
   The "CommonArchiving" folder is located in the project folder of your WinCC project.
2. In Runtime, the data log is automatically connected to the project.

If signing is enabled, signed log backup files that are changed will not be connected automatically. A WinCC system message is generated and an entry is added to the Windows event log in the "Application" section.

---

**See also**

[Logging Settings (RT Professional)](#logging-settings-rt-professional)
  
[Configuring the log backup (RT Professional)](#configuring-the-log-backup-rt-professional)
  
[Disconnecting a log backup (RT Professional)](#disconnecting-a-log-backup-rt-professional)
  
[Restore (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#restore-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example of the start of a script at the server (Logging object) (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-the-start-of-a-script-at-the-server-logging-object-rt-professional)

##### Disconnecting a log backup (RT Professional)

###### Introduction

If you have connected a log backup in Runtime, you can also disconnect the connection once more. You can disconnect the connection using a VB function or manually remove the log backup files from the "CommonArchiving" folder.

###### Requirement

- The corresponding LDF file and MDF file of the log backup are located in the "CommonArchiving" folder in the project folder of the WinCC project.

###### Procedure

Proceed as follows to disconnect a log backup using a VB function:

1. Configure a button in a process screen and label the button "Disconnect log backup", for example.
2. Write a VB function using the "Remove" VBS method based on this example:

   HMIRuntime.Trace "Ret: " &amp; HMIRuntime.Logging.Remove("","2010-11-14",-1) &amp; vbNewLine

   You can find more detailed information about this in "[Remove](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#remove-panels-comfort-panels-rt-advanced-rt-professional)".
3. Configure a list of functions for the "Click" event for the configured button.
4. Select the VB function thus created from the list of functions.
5. Save the project.

###### Result

The VB function is executed in Runtime when the button is clicked. The log backup is disconnected from the log database. You will no longer have access to the data from the backup file in Runtime.

Alternatively, you can manually remove the backup files from the "CommonArchiving" folder. The "CommonArchiving" folder is found in the project folder of your WinCC project.

---

**See also**

[Logging Settings (RT Professional)](#logging-settings-rt-professional)
  
[Configuring the log backup (RT Professional)](#configuring-the-log-backup-rt-professional)
  
[Connecting the log backup (RT Professional)](#connecting-the-log-backup-rt-professional)
  
[Remove (Panels, Comfort Panels, RT Advanced, RT Professional)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#remove-panels-comfort-panels-rt-advanced-rt-professional)

#### Logging tags in the "Tags" editor (RT Professional)

This section contains information on the following topics:

- [Configuring logging tags (RT Professional)](#configuring-logging-tags-rt-professional)

##### Configuring logging tags (RT Professional)

###### Introduction

You can also create and edit logging tags in the "HMI tags" editor in WinCC. You also directly edit the properties of logging tags in the "Tags" editor.

> **Note**
>
> If you delete, move or copy in the "HMI tags" editor, the changes also take effect in the "Logs" editor.

###### Requirement

- The "Logging tags" tab is open in the "HMI tags" editor.
- You have created a tag.

###### Procedure

Proceed as follows to configure a logging tag in the "HMI tags" editor:

1. Select an existing tag in the tag table.  
   Alternatively, double-click "Add" in the "Name" column to create a new tag.
2. Click on "Logging tags" in the lower editor. The editor for logging tags is brought to the foreground.

   ![Procedure](images/129190043915_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/129190043915_DV_resource.Stream@PNG-en-US.png)
3. Double-click "Add ..." in the "Name" column of the editor "Logging tag" table. A new logging tag is created. The logging tag is linked to the tag selected in the first step. The data type of the logging tag is taken automatically from the linked tag.

   ![Procedure](images/136207635979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/136207635979_DV_resource.Stream@PNG-en-US.png)
4. Select the desired logging tag from the "Data log" field. You can also create a new log using the object list.
5. Configure additional parameters for logging in the table of the editor or in the Inspector window.

###### Result

The configured logging tag is created in the "Tags" editor and is displayed in various editors.

---

**See also**

[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Logging tags (RT Professional)](#logging-tags-rt-professional-1)

#### Functions for data logging (RT Professional)

This section contains information on the following topics:

- [Function for status check of the log lock (RT Professional)](#function-for-status-check-of-the-log-lock-rt-professional)
- [Converting values from logging tags (RT Professional)](#converting-values-from-logging-tags-rt-professional)

##### Function for status check of the log lock (RT Professional)

###### Introduction

You can monitor the "Locked" state of a data log using a C function. You need to create the C function in the "Scripts" editor with the correct syntax.

###### Description

This function is called in Runtime from the log server when triggered by a "Locked" status change. You can assign this function to the event "Lock state change" in the "Events" group in the "Data logs" or "Compressed logs" editor. The C function is then only displayed under the "Lock changed" event when the syntax below is correctly written in the function.

###### Syntax

void function name (BOOL fFlag);

###### Parameters

**fFlag**

TRUE - log is locked

FALSE - log is released

###### Example application

You can use this function to receive information about the lock status of a log, for example.

---

**See also**

[Data logging (RT Professional)](#data-logging-rt-professional-1)
  
[Converting values from logging tags (RT Professional)](#converting-values-from-logging-tags-rt-professional)

##### Converting values from logging tags (RT Professional)

###### Description

You can use this C function to convert tag values before logging them. This C function is assigned in the "Logging tags" editor in the properties of the logging tag under "Properties &gt; Processing method". The C function is then only offered for selection in the "Analog processing method" field when the syntax below is correctly written in the function.

###### Syntax

**double function name (double dLastValue,**

**double dCurrentValue,**

**DWORD dwCount,**

**BOOL fArchivingCycle);**

###### Parameters

**dLastValue**: Return value of the function that was triggered in the last acquisition cycle

**dCurrentValue**: currently acquired value

**dwCount**: current acquisition cycle since the most recent log cycle (for example, log cycle is 4 x 1 seconds of acquisition cycle; the count is then 1 to 4, until the count starts again).

**fArchivingCycle**: TRUE = cycle is log cycle (default); FALSE = cycle is acquisition cycle

###### Example application

You can use this function to implement your own mean value calculation. The calculated mean value is used instead of the current tag value.

The following function determines the geometric mean value of the acquired process values:

double CalculateGeometricMean (double dLastValue,double dCurrentValue,DWORD dwCount,BOOL fArchivingCycle)

{

static double dCurrentProduct = 1.0;

double dReturnValue = 0.0;

if (!fArchivingCycle)

{

// 1. continuously calculate the product of all values with every scan cycle

dCurrentProduct *= dCurrentValue;

printf ("current value=%f current product=%f archiving cycle flag=%d\r\n",dCurrentValue,dCurrentProduct ,fArchivingCycle);

dReturnValue = dCurrentProduct ; // optinonally - the return value is actually not of interest in a scan cycle

}

else

{

// 2. if this is the archiving cycle, use the product of all scan values to calculate

// the geometric mean value

dReturnValue = pow (dCurrentProduct ,(double) 1 / dwCount);

printf ("archiving cycle: geometric mean value=%f\r\n",dReturnValue);

printf ("\r\n");

dCurrentProduct = 1.0; // reset current product

// the finally calculated value will be returned - this value will be archived

// since this is the archiving cycle

}

return dReturnValue;

}

---

**See also**

[Function for status check of the log lock (RT Professional)](#function-for-status-check-of-the-log-lock-rt-professional)

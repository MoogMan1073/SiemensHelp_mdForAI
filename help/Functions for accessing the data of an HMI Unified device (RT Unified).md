---
title: "Functions for accessing the data of an HMI Unified device (RT Unified)"
package: OpennessWCCUenUS
topics: 170
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Functions for accessing the data of an HMI Unified device (RT Unified)

This section contains information on the following topics:

- [HMISoftware (RT Unified)](#hmisoftware-rt-unified)
- [Accessing further objects (RT Unified)](#accessing-further-objects-rt-unified)

## HMISoftware (RT Unified)

This section contains information on the following topics:

- [HMISoftware object (RT Unified)](#hmisoftware-object-rt-unified)
- [Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)
- [AlarmClasses (RT Unified)](#alarmclasses-rt-unified)
- [AlarmLogs (RT Unified)](#alarmlogs-rt-unified)
- [AnalogAlarms (RT Unified)](#analogalarms-rt-unified)
- [AuditTrails (RT Unified)](#audittrails-rt-unified)
- [Connections (RT Unified)](#connections-rt-unified)
- [DataLogs (RT Unified)](#datalogs-rt-unified)
- [DiscreteAlarms (RT Unified)](#discretealarms-rt-unified)
- [LoggingTags (RT Unified)](#loggingtags-rt-unified)
- [RuntimeSettings (RT Unified)](#runtimesettings-rt-unified)
- [SystemTags (RT Unified)](#systemtags-rt-unified)
- [Screens (RT Unified)](#screens-rt-unified)
- [ScreenGroups (RT Unified)](#screengroups-rt-unified)
- [Tags (RT Unified)](#tags-rt-unified)
- [TagTables (RT Unified)](#tagtables-rt-unified)
- [TagTableGroups (RT Unified)](#tagtablegroups-rt-unified)

### HMISoftware object  (RT Unified)

![Figure](images/172551373835_DV_resource.Stream@PNG-en-US.png)

### Description HMISoftware (RT Unified)

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal  
  [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Introduction

You can use the HMI Software object to access elements like tags, connections, alarms, and screens.

#### Program code

To access the HMI Software object modify the following program code:

using System;

using System.IO;

using Siemens.Engineering;

using Siemens.Engineering.HmiUnified;

using Siemens.Engineering.HW;

using Siemens.Engineering.HW.Features;

private HmiSoftware GetHmiSoftware()

{

HmiSoftware hmiSoftware = null;

Project project = null;

IList&lt;TiaPortalProcess&gt; tiaProcessList = TiaPortal.GetProcesses();

//If no TIA Application instance is running, then following using statement will start it or

//If TIA application is already running then will attach to it.

TiaPortal tiaApp = tiaProcessList.Count &gt; 0? tiaProcessList[0].Attach(): new TiaPortal(TiaPortalMode.WithUserInterface);

// tiaApp.Projects[X] defines the project which has to be opened

// With order number 0 the first project will be opened if several projects are present in

// given TIA instance.

if (tiaApp.Projects.Count &gt; 0)

project = tiaApp.Projects[0];

else

{

//If there is no device project in given TIA instance, then open the existing project.

FileInfo file = new FileInfo(@"D:\Automation\Project1\Project1.apx");

if (!file.Exists)

throw new FileNotFoundException("Project1.apx not found");

project = tiaApp.Projects?.Open(file);

}

//After getting project, get the object representing UA software HMI device.

var devices = project.Devices;

if (devices != null)

{

//If the device is in the first position of the openness project tree

var device = devices[0];

//If the device is not in the first position of the openness project tree, you have to adapt

// the order number devices[X];

var deviceItems = device.DeviceItems;

if (deviceItems != null)

{

foreach (DeviceItem deviceItem in deviceItems)

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

hmiSoftware = softwareContainer?.Software as HmiSoftware;

}

}

}

return hmiSoftware;

}

clipboard
> **Note**
>
> In the above program code, the extension .apx refers to the installed version of TIA Portal.

### AlarmClasses (RT Unified)

This section contains information on the following topics:

- [Description AlarmClasses (RT Unified)](#description-alarmclasses-rt-unified)
- [AlarmClasses.Create() (RT Unified)](#alarmclassescreate-rt-unified)
- [AlarmClasses.Delete() (RT Unified)](#alarmclassesdelete-rt-unified)
- [Accessing alarm classes properties (RT Unified)](#accessing-alarm-classes-properties-rt-unified)
- [Accessing cross reference service on alarm classes (RT Unified)](#accessing-cross-reference-service-on-alarm-classes-rt-unified)

#### Description AlarmClasses (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on alarm classes you can either use enumerate alarm classes or use Find().

private void BrowseAlarmClasses()

{

//User can navigate all alarm classes of device

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;

foreach (HmiAlarmClass alarmClass in alarmClasses)

{

//Working with alarm classes

}

}

clipboard

To access a single alarm class by name modify the following program code:

private void SearchAlarmClasses()

{

HmiSoftware hmiSoftware = GetHmiSoftware():

// Search for a specific alarm class from list of alarm classes

string alarmClassName = "AlarmClass_1";

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;

HmiAlarmClass alarmClassObj = alarmsClasses.Find(alarmClassName);

}

clipboard

##### Working with alarm classes

You can perform the following tasks with tags while using TIA Portal Openness:

- Creating alarm classes:[AlarmClasses.Create()](#alarmclassescreate-rt-unified)
- Deleting alarm classes [AlarmClasses.Delete()](#alarmclassesdelete-rt-unified)
- Alarm classes properties: [Accessing alarm classes properties](#accessing-alarm-classes-properties-rt-unified)
- Alarm classes cross reference service: [Accessing cross reference service on alarm classes](#accessing-cross-reference-service-on-alarm-classes-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AlarmClasses.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a alarm class with Create() of HmiAlarmClassComposition class modify the following program code:

private void AlarmClassCreate()

{

//Create Alarm Class with name "AlarmClass1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;

HmiAlarmClass alarmClass = alarmClasses.Create("AlarmClass1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AlarmClasses.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a alarm class with Delete() of HmiAlarmClass class modify the following program code :

public void DeleteAlarmClass()

//User wants to delete an alarm class with the alarm name AlarmClass1

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;;

HmiAlarmClass alarmClass = alarmClasses.Find("AlarmClass1");

alarmClass.Delete();

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing alarm classes properties (RT Unified)

##### Property

The following properties are supported in alarm classes:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the name of an alarm class | Depend on type of alarm class provided (system-based alarm or user-based alarm) |
| Priority | Byte | Specifies the priority of an alarm class | R/W |
| IsSystem | Boolean | Specifies if the alarm class is system provided | R |
| StateMachine | HmiAlarmStateMachine | Specifies the state machine of an alarm class | Depend on type of alarm class provided (system-based alarm or user-based alarm) |
| RaisedState | HmiRaisedState | Specifies the state for active alarms | R |
| RaisedState.BackColor | Color | Specifies the back color for active state | R/W |
| RaisedState.TextColor | Color | Specifies the text color for active state | R/W |
| RaisedState.Flashing | Boolean | Specifies the flashing for active state | R/W |
| ClearedState | HmiClearedState | Specifies the state for cleared alarms | R |
| ClearedState.BackColor | Color | Specifies the back color for cleared state | R/W |
| ClearedState.TextColor | Color | Specifies the text color for cleared state | R/W |
| ClearedState.Flashing | Boolean | Specifies the flashing for cleared state | R/W |
| AcknowledgedState | HmiAcknowledgedState | Specifies the state for acknowledged alarms | R |
| AcknowledgedState.BackColor | Color | Specifies the back color for acknowledged state | R/W |
| AcknowledgedState.TextColor | Color | Specifies the text color for acknowledged state | R/W |
| AcknowledgedState.Flashing | Boolean | Specifies the flashing for acknowledged state | R/W |
| AcknowledgedClearedState | HmisAcknowledgedClearedState | Specifies the state for acknowledged and cleared alarms | - |
| AcknowledgedClearedState.BackColor | Color | Specifies the back color for acknowledged and cleared alarms | R/W |
| AcknowledgedClearedState.TextColor | Color | Specifies the text color acknowledged and cleared alarms | R/W |
| AcknowledgedClearedState.Flashing | Boolean | Specifies the flashing for acknowledged and cleared alarms | R/W |
| Id | UInt32 | Specifies the id to identify the alarm class  This id is a unique value for each alarm class. | R |
| Log | System.String | Specifies the log of an alarm class | R/W |
| CommonAlarmClass | System.String | Specifies the common alarm class | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of alarm classes modify the following program code:

private void AlarmClassesPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;

HmiAlarmClass alarmClass = hmiSoftware.AlarmClasses.Find("MostCritical");

int priority = alarmClass.Priority;

alarmClass.Priority = 10;

alarmClass.Acknowledgement = StateMachine.AlarmWithDualModeAcknowledgement;

alarmClass.IncomingOutgoingAcknowledgeStatus.BackColor = Color.Red;

alarmClass.IncomingOutgoingAcknowledgeStatus.TextColor = Color.Black;

alarmClass.IncomingOutgoingAcknowledgeStatus.Flashing = true;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing cross reference service on alarm classes (RT Unified)

##### Requirements

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service with GetService() of HmiAlarmClass class modify the following program code:

private void getCrossReferenceServiceforTag()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;

// Accessing lower

// levels until we reach the HmiAlarmClassComposition

HmiAlarmClassComposition alarmClasses = hmiSoftware.AlarmClasses;

HmiAlarmClass alarmClass = alarmClasses.Find("AlarmClass1");

if (alarmClass != null)

{

try

{

CrossReferenceService crossReferenceService = alarmClass.GetService&lt;CrossReferenceService&gt;();

......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

}

clipboard

---

**See also**

[HMISoftware object (RT Unified)](#hmisoftware-object-rt-unified)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)

### AlarmLogs (RT Unified)

This section contains information on the following topics:

- [Description AlarmLogs (RT Unified)](#description-alarmlogs-rt-unified)
- [AlarmLogs.Create() (RT Unified)](#alarmlogscreate-rt-unified)
- [AlarmLogs.Delete() (RT Unified)](#alarmlogsdelete-rt-unified)
- [Accessing alarm logs properties (RT Unified)](#accessing-alarm-logs-properties-rt-unified)

#### Description AlarmLogs (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on alarm logs you can either use enumerate alarm logs or use Find().

private void AlarmLogBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the alarm logs of given alarm log table

HmiAlarmLogComposition alarmLogs = hmiSoftware.AlarmLogs;

foreach (HmiAlarmLog alarmLog in alarmLogs)

{

//working with alarm log.

}

}

clipboard

To access a single alarm log by name modify the following program code:

private void SearchAlarmlog()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a specific alarm log from list of alarmlogs

String alarmLogName = "AlarmLog_1";

HmiAlarmLogComposition alarmLogs = hmiSoftware.AlarmLogs;

HmiAlarmLog alarmLogObj = alarmLogs.Find(alarmLogName);

}

clipboard

##### Working with alarm logs

You can perform the following tasks with data logs while using TIA Portal Openness:

- Creating alarm logs: [AlarmLogs.Create()](#alarmlogscreate-rt-unified)
- Deleting alarm logs: [AlarmLogs.Delete()](#alarmlogsdelete-rt-unified)
- Alarm logs properties: [Accessing alarm logs properties](#accessing-alarm-logs-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AlarmLogs.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a alarm log with Create() of HmiAlarmLogComposition class modify the following program code:

private void AlarmLogCreate()

{

//Create Alarmlog

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmLogComposition alarmLogs = hmiSoftware.AlarmLogs;

HmiAlarmLog alarmLog = alarmLogs.Create("Alarmlog1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AlarmLogs.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a alarm log with Delete() of HmiAlarmLog class modify the following program code :

private void AlarmLogDelete()

{

//User wants to delete alarm log with name "Alarmlog1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmLogComposition alarmLogs = hmiSoftware.AlarmLogs;

HmiAlarmLog alarmLog = alarmLogs.Find("Alarmlog1");

alarmLog.Delete();

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing alarm logs properties (RT Unified)

##### Property

The following properties are supported in the alarm logs:

| Property Name |  | Data Type | Description | Access |
| --- | --- | --- | --- | --- |
| Name |  | String | Specifies the name of alarm log | R/W |
| Settings |  | LogSettings | Specifies the members in complex properties such as StorageFolder, LogMaxSize, and LogTimePeriod which define the settings related to alarm log | R |
| StoragePath | String | Specifies the path for storage | R/W |  |
| LogMaxSize | Unsigned int | Specifies the maximum size of log on storage medium in units of megabytes | R/W |  |
| LogTimePeriod | LogDuration | Specifies the maximum time period covered by alarm log | R/W |  |
| Segment |  | LogSegment | Specifies the members in complex properties such as SegementMaxSize, StartTime and SegmentTimePeriod which define the settings related to segment | R |
| SegmentMaxSize | Unsigned int | Specifies the maximum size of segment of alarm log in units of megabytes | R/W |  |
| SegmentStartTime | DateTime | Specifies the exact point in time when segment is started | R/W |  |
| SegmentTimePeriod | SegmentDuration | Specifies the maximum time period covered by segment of alarm log | R/W |  |
| Backup |  | LogBackup | Specifies the members of complex properties such as PrimaryPath and BackupMode which define the settings related to log backup | R |
| BackupMode | HmiBackupMode | Specifies the mode for backup | R/W |  |
| PrimaryPath | String | Specifies the path for backup | R/W |  |

The following properties are supported in log duration:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| Days | Unsigned int | Specifies the set and get number of days | R/W |
| Hours | Unsigned int | Specifies the set and get number of hours | R/W |
| Segment | LogSegment | Specifies the members of complex properties such as SegementMaxSize, StartTime and SegmentTimePeriod which define the settings related to Segment | R |
| Backup | LogBackup | Specifies the members of complex properties such as PrimaryPath and BackupMode which define the settings related to log backup | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of alarm logs modify the following program code:

private void AlarmLogPropertiesAccess()

{

//Set and Get alarm log properties.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAlarmLogComposition alarmLogs = hmiSoftware.AlarmLogs;

HmiAlarmLog alarmLog = alarmLogs.Find("Alarmlog_1");

string name = alarmLog.Name;

alarmLog.Settings.StorageFolder = @"C:\Logs\Log";

alarmLog.Settings.LogMaxSize = Int32.MaxValue;

alarmLog.Settings.LogMaxSize = 2000;

LogDuration duration = alarmLog.Settings.LogTimePeriod;

double durationInDouble = duration.GetDoubleLogDuration();

string durationInString = duration.GetStringLogDuration();

duration.Days = 7;

duration.Hours = 23;

duration.Minutes = 50;

duration.Seconds = 0;

duration.Ticks = 1;

//Log duration can be set by using function also.

duration.SetLogDuration(10, 12, 4, 5, 0);

alarmLog.Backup.BackupMode = BackupMode.NoBackup;

alarmLog.Backup.BackupMode = BackupMode.PrimaryPath;

alarmLog.Backup.PrimaryPath = @"C:\Logs\Backup";

alarmLog.Segment.SegmentMaxSize = 500;

alarmLog.Segment.SegmentStartTime = DateTime.Now;

alarmLog.Segment.SegmentStartTime = DateTime.Now.Date;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### AnalogAlarms (RT Unified)

This section contains information on the following topics:

- [Description AnalogAlarms (RT Unified)](#description-analogalarms-rt-unified)
- [AnalogAlarms.Create() (RT Unified)](#analogalarmscreate-rt-unified)
- [AnalogAlarms.Delete() (RT Unified)](#analogalarmsdelete-rt-unified)
- [Accessing analog alarm properties (RT Unified)](#accessing-analog-alarm-properties-rt-unified)
- [Accessing cross reference service on analog alarms (RT Unified)](#accessing-cross-reference-service-on-analog-alarms-rt-unified)

#### Description AnalogAlarms (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on analog alarms you can either use enumerate analog alarms or use Find().

private void AnalogAlarmBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all analog alarms of device

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

foreach (HmiAnalogAlarm analogAlarm in analogAlarms)

{

//Working with analog alarms.

}

}

clipboard

To access a single analog alarm by name modify the following program code:

private void SearchAnalogAlarm()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a specific analog alarm from list of analog alarms

String analogAlarmName = "AnalogAlarm_1";

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

HmiAnalogAlarm analogAlarmObj = analogAlarms.Find(analogAlarmName);

}

clipboard

##### Working with analog alarms

You can perform the following tasks with analog alarms while using TIA Portal Openness:

- Creating tags:[AnalogAlarms.Create()](#analogalarmscreate-rt-unified)
- Deleting tags: [AnalogAlarms.Delete()](#analogalarmsdelete-rt-unified)
- Analog Alarm properties: [Accessing analog alarm properties](#accessing-analog-alarm-properties-rt-unified)
- Analog Alarm cross reference service: [Accessing cross reference service on analog alarms](#accessing-cross-reference-service-on-analog-alarms-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AnalogAlarms.Create() (RT Unified)

##### Requirements

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a analog alarm with Create() of HmiAnalogAlarmComposition class modify the following program code:

private void AnalogAlarmCreate()

{

//Create an Analog Alarm with name "Alarm1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

HmiAnalogAlarm analogAlarm = analogAlarms.Create("Alarm1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### AnalogAlarms.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a analog alarm with Delete() of HmiAnalogAlarm class modify the following program code :

private void AnalogAlarmDelete()

{

//Delete an Analog Alarm

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

HmiAnalogAlarm analogAlarm = analogAlarms.Find("Alarm_1");

if (analogAlarm != null)

{

analogAlarm.Delete();

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing analog alarm properties (RT Unified)

##### Property

The following properties are supported in analog alarm:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| EventText | MultilingualText | Specifies the alarm text of an analog alarm | R/W |
| Id | UInt32 | Specifies the id of an alarm. This id is unique value for each analog alarm. | R/W |
| AlarmClass | String | Specifies the class of an analog alarm. | R/W |
| Name | String | Specifies the name of an analog alarm. | R/W |
| Priority | Byte | Specifies the priority of an analog alarm. | R/W |
| Origin | String | Specifies the origin of an analog alarm | R/W |
| Area | String | Specifies the area of an analog alarm | R/W |
| RaisedStateTag | String | Specifies the tag that triggers the analog alarm | R/W |
| ConditionValue | Object supported type: Double, Int16, UInt16, Int32, UInt32, Int64, UInt64, Byte | Specifies the limit value for analog alarm which can be specified as constant value | R/W |
| Condition | HmiAlarmCondition | Specifies the limit mode for an analog alarm | R/W |
| InfoText | MultilingualText | Specifies the info text of an analog alarm | R/W |
| AlarmParameterTags | Object SupportedType: IList&lt;string&gt; | An array of in maximum 10 elements specifies the alarm parameters in an alarm text. Each element of the array contains a tag name as string. | R/W |
| EventText1 | MultilingualText | Specifies the additional text 1 of an analog alarm | R/W |
| EventText2 | MultilingualText | Specifies the additional text 2 of an analog alarm | R/W |
| EventText3 | MultilingualText | Specifies the additional text 3 of an analog alarm | R/W |
| EventText4 | MultilingualText | Specifies the additional text 4 of an analog alarm | R/W |
| EventText5 | MultilingualText | Specifies the additional text 5 of an analog alarm | R/W |
| EventText6 | MultilingualText | Specifies the additional text 6 of an analog alarm | R/W |
| EventText7 | MultilingualText | Specifies the additional text 7 of an analog alarm | R/W |
| EventText8 | MultilingualText | Specifies the additional text 8 of an analog alarm | R/W |
| EventText9 | MultilingualText | Specifies the additional text 9 of an analog alarm | R/W |
| TriggerAddress | String | Specifies the address of the trigger tag | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of analog alarm modify the following program code:

private void AnalogAlarmPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

HmiAnalogAlarm analogAlarm = analogAlarms.Find("Alarm_1");

uint id = analogAlarm.Id;

analogAlarm.Id = 10;

int priority = analogAlarm.Priority;

analogAlarm.Priority = 7;

string area = analogAlarm.Area;

analogAlarm.Area = "Area_1";

string name = analogAlarm.Name;

analogAlarm.Name = "NewAlarm";

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing cross reference service on analog alarms (RT Unified)

##### Requirements

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service with GetService() of HmiAnalogAlarm class modify the following program code:

private void getCrossReferenceServiceforAnalogAlarm()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;

// Accessing lower levels

// until we reach the HmiAnalogAlarmComposition.

HmiAnalogAlarmComposition analogAlarms = hmiSoftware.AnalogAlarms;

HmiAnalogAlarm analogAlarm = analogAlarms.Find("Alarm1")

if (analogAlarm != null)

{

try

{

CrossReferenceService crossReferenceService = analogAlarm.GetService&lt;CrossReferenceService&gt;();

......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### AuditTrails (RT Unified)

This section contains information on the following topics:

- [Description AuditTrails (RT Unified)](#description-audittrails-rt-unified)
- [Accessing audit trails properties (RT Unified)](#accessing-audit-trails-properties-rt-unified)

#### Description AuditTrails (RT Unified)

##### Requirements

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on audit trails you can either use enumerate alarm trail or use Find().

private void AuditTrailBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the audit trails

HmiAuditTrailComposition auditLogs = hmiSoftware.AuditTrails

foreach (HmiAuditTrail auditLog in auditLogs)

{

//working with audit trails.

}

}

clipboard

To access a single audit trail by name modify the following program code:

private void SearchAuditTrails()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for specific audit trail name

string auditTrailName = "AuditTrail_1";

HmiAuditTrailComposition auditLogs = hmiSoftware.AuditTrails;

HmiAuditTrail auditLogObject = auditLogs [01];

AuditTrail auditTrailObj = auditLogObject.Find(auditTrailName);

}

clipboard

##### Working with audit trails

You can perform the following tasks with audit trails while using TIA Portal Openness:

- Audit trail properties: [Accessing audit trails properties](#accessing-audit-trails-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing audit trails properties (RT Unified)

##### Property

The following properties are supported in the Audit Trails:

| Property Name |  | Data Type | Description | Access |
| --- | --- | --- | --- | --- |
| Name |  | String | Specifies the name of audit trail | R/W |
| Settings |  | LogSettings | Specifies the members of complex properties such as StorageFolder, LogMaxSize, and LogTimePeriod which defines the settings related to the audit trail | R |
| StorageFolder | String | Specifies the folder path for storage | R/W |  |
| LogMaxSize | Unsigned int | Specifies the maximum size of log on storage medium in units of megabytes | R/W |  |
| LogTimePeriod | LogDuration | Specificies the maximum time period covered by log | R/W |  |
| StorageDevice | DeviceNode | Specifies the storage device | R/W |  |
| Segment |  | LogSegment | Specifies the members of complex properties such as SegementMaxSize, StartTime, and SegmentTimePeriod which define the settings related to the segment | R |
| SegmentMaxSize | Unsigned int | Specifies the maximum size of segment in audit trail in units of megabytes | R/W |  |
| SegmentStartTime | DateTime | Specifies the exact point in time when segment is started | R/W |  |
| SegmentTimePeriod | SegmentDuration | Specifies the maximum time period covered by segment of audit trail | R/W |  |
| Backup |  | LogBackup | Specific the members of complex properties such as PrimaryPath, and BackupMode which define the settings related to the audit trail backup | R |
| BackupMode | HmiBackupMode | Specifies the mode for backup | R/W |  |
| PrimaryPath | String | Specifies the primary path for backup | R/W |  |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of audit trails modify the following program code:

private void AuditTrailPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiAuditTrailComposition auditLogs = hmiSoftware.AuditTrails;

HmiAuditTrail auditLogObject = auditLogs [01];

string auditTrailName = auditLogObject.Name;

Console.WriteLine("Name {0}" auditTrailName);

auditLogObject.Name = "Audit Log_100";

auditLogObject.Settings.StorageFolder = @"C:\\Testsl23";

auditLogObject.Settings.LogMaxSize = Int32.MaxValue;

auditLogObject.Settings.LogMaxSize = 2000;

LogDuration duration = auditLogObject.Settings.LogTimePeriod;

double durationlnDouble = duration.GetDoubleLogDuration();

string durationlnString = duration .GetStringLogDuration();

duration.Days = 200;

duration.Hours = 10;

duration.Minutes = 22;

duration.Seconds = 39;

duration.Ticks = 0;

//Log duration can be set by function also

duration.SetLogDuration(10,12,4,5,0);

auditLogObject.Backup.BackupMode = HmiBackupMode.NoBackup;

auditLogObject.Backup.BackupMode = HmiBackupMode.PrimaryPath;

auditLogObject.Backup.PrimaryPath = @"C:\Logs\Backup";

auditLogObject.Segment.SegmentMaxSize = 500;

auditLogObject.Segment.SegmentStartTime = DateTime.Now;

auditLogObject.Segment.SegmentStartTime = DateTime.Now.Date;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Connections (RT Unified)

This section contains information on the following topics:

- [Description Connections (RT Unified)](#description-connections-rt-unified)
- [Connections.Create() (RT Unified)](#connectionscreate-rt-unified)
- [Connections.Delete() (RT Unified)](#connectionsdelete-rt-unified)
- [Accessing connection properties (RT Unified)](#accessing-connection-properties-rt-unified)
- [Accessing cross reference service on connections (RT Unified)](#accessing-cross-reference-service-on-connections-rt-unified)

#### Description Connections (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform task on connection you can either use enumerate connections or use Find( )

private void ConnectionBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all connections of device

HmiConnectionComposition connections = hmiSoftware.Connections;

foreach (HmiConnection connection in connections)

{

//working with connection

}

}

clipboard

To access a single connection by name modify the following program code:

private void ConnectionSearch()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for specific connection name from a list of connections

string connectionName = "Connection_1";

HmiConnectionComposition connections = hmiSoftware.Connections;

HmiConnection connectionObj = connections.Find(connectionName);

}

clipboard

##### Working with connections

You can perform the following tasks with connections while using TIA Portal Openness:

- Creating connections: [Connections.Create()](#connectionscreate-rt-unified)
- Deleting connections: [Connections.Delete()](#connectionsdelete-rt-unified)
- Connection properties: [Accessing connection properties](#accessing-connection-properties-rt-unified)
- Connection cross reference service: [Accessing cross reference service on connections](#accessing-cross-reference-service-on-connections-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Connections.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a connection with Create() of HmiConnectionComposition class modify the following program:

private void ConnectionCreate()

{

//Create a connection with name "Connection_1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiConnectionComposition connections = hmiSoftware.Connections;

HmiConnection connection = connections.Create("Connection_1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Connections.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a connection with Delete() of HmiConnection class modify the following program code:

private void ConnectionDelete()

{

//Delete a connection with name "Connection_1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiConnectionComposition connections = hmiSoftware.Connections;

HmiConnection connection = connections.Find("Connection_1");

connection.Delete();

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing connection properties (RT Unified)

##### Property

The following properties are supported in connection:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the name of connection | R/W |
| DisabledAtStartup | Boolean | Specifies whether the connection is disabled at the start of Runtime | R/W |
| CommunicationDriver | String | Specifies the communication driver | R/W |
| Node | String | Specifies the access point of partner (eg PLC). | R |
| Partner | String | Specifies the name of connected PLC. | R |
| Station | String | Specifies the name of the station to which PLC is located. | R |
| Comment | String | Specifies the additional comments if any | R/W |
| InitialAddress | String | Specifies the parameters of connection like type of interface (DP, TCP/IP), IP address, Rack etc. | R/W |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of connection modify the following program code:

private void ConnectionPropertiesAccess()

{

// Accessing properties of Connection object.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiConnectionComposition connections = hmiSoftware.Connections;

HmiConnection connection = connections.Find("Connection_12");

string name = connection.Name;

connection.Name = "Connection_15";

bool online = connection.DisabledAtStartup;

connection.DisabledAtStartup = true;

string node = connection.Node;

string station = connection.Station;

string partner = connection.Partner;

string communicationDriver = connection.CommunicationDriver;

connection.CommunicationDriver = "SIMATIC S7 300/400";

// Accessing "InitialAddress" property of connection object

// with valid strings

connection.InitialAddress = "CommunicationInterface = Industrial Ethernet;

HostAddress = 127.157.8.1; HostAccessPoint = S7ONLINE; PlcRack = 5; PlcIsCyclicOperation = true";

// Accessing "InitialAddress" property of connection object with invalid value or invalid

// format will return recoverable exception.

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing cross reference service on connections (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service with GetService() of HmiConnection class modify the following program code:

private void getCrossReferenceServiceforConnection()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;  //Accessing lower levels

// until we reach the HmiConnectionComposition.

HmiConnectionComposition connections = hmiSoftware.Connections;

HmiConnection hmiConnection = connections.Find("Connection1");

if (hmiConnection != null)

{

try

{

CrossReferenceService crossReferenceService = hmiConnection.GetService&lt;CrossReferenceService&gt;();

......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### DataLogs (RT Unified)

This section contains information on the following topics:

- [Description Datalogs (RT Unified)](#description-datalogs-rt-unified)
- [Datalogs.Create() (RT Unified)](#datalogscreate-rt-unified)
- [Datalogs.Delete() (RT Unified)](#datalogsdelete-rt-unified)
- [Accessing data logs properties (RT Unified)](#accessing-data-logs-properties-rt-unified)

#### Description Datalogs (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on data logs you can either use enumerate datalog or use Find().

private void DatalogBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all data logs of device

HmiDataLogComposition dataLogs = hmiSoftware.DataLogs;

foreach (HmiDataLog dataLog in dataLogs)

{

// Working with data logs

}

}

clipboard

To access a single data log by name modify the following program code:

private void SearchDatalog()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a specific data log from list of data logs

String datalogName = "DataLog_1";

HmiDataLogComposition dataLogs = hmiSoftware.DataLogs;

HmiDataLog dataLogObj = dataLogs.Find(dataLogName);

}

clipboard

##### Working with data logs

You can perform the following tasks with data logs while using TIA Portal Openness:

- Creating data logs:[Datalogs.Create()](#datalogscreate-rt-unified)
- Deleting data logs: [Datalogs.Delete()](#datalogsdelete-rt-unified)
- Data logs properties: [Accessing data logs properties](#accessing-data-logs-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Datalogs.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a datalog with Create() of HmiDatalogComposition class modify the following program code:

private void DatalogCreate()

{

//Create Datalog

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiDataLogComposition dataLogs = hmiSoftware.DataLogs;

HmiDataLog dataLog = dataLogs.Create("Datalog_1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Datalogs.Delete() (RT Unified)

##### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a data log with Delete() of HmiDataLog class modify the following program code :

private void DatalogDelete()

{

//user wants to delete datalog with name "Datalog1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiDataLogComposition dataLogs = hmiSoftware.DataLogs;

HmiDataLog dataLog = dataLogs.Find("Datalog1");

dataLog.Delete();

}

clipboard

#### Accessing data logs properties (RT Unified)

##### Property

The following properties are supported in the data logs:

| Property Name |  | Data Type | Description | Access |
| --- | --- | --- | --- | --- |
| Name |  | String | Specifies the name of data log | R/W |
| Settings |  | LogSettings | Specifies the members of complex properties such as StorageFolder, LogMaxSize and LogTimePeriod which define the settings related to log | R |
| StorageFolder | String | Specifies the folder path for storage | R/W |  |
| LogMaxSize | Unsigned int | Specifies the maximum size of log on storage medium in units of megabytes | R/W |  |
| LogTimePeriod | LogDuration | Specifies the maximum time period covered by log | R/W |  |
| StorageDevice | DeviceNode | Specifies the storage device to be checked | R/W |  |
| Segment |  | LogSegment | Specifies the members of complex properties such as SegementMaxSize, StartTime and SegmentTimePeriod) which define the settings related to segment | R |
| SegmentMaxSize | Unsigned int | Specifies the maximum size of segment of log in units of megabytes | R/W |  |
| SegmentStartTime | DateTime | Specifies the exact point in time when segment of log is started (to be checked) | R/W |  |
| SegmentTimePeriod | SegmentDuration | Specifies the maximum time period covered by segment of log | R/W |  |
| Backup |  | LogBackup | Specifies the members of complex properties such as PrimaryPath and BackupMode which define the settings related to log backup | R |
| BackupMode | HmiBackupMode | Specifies the mode for back up | R/W |  |
| PrimaryPath | String | Specifies the primary path for back up | R/W |  |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of data logs modify the following program code:

private void DatalogPropertiesAccess()

{

//Set/Get Data Log properties.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiDataLogComposition dataLogs = hmiSoftware.DataLogs;

HmiDataLog dataLog = dataLogs.Find("Datalog_1");

string name = dataLog.Name;

dataLog.Settings.StorageFolder = @"C:\Logs\Log";

dataLog.Settings.LogMaxSize = Int32.MaxValue;

dataLog.Settings.LogMaxSize = 2000;

LogDuration duration = dataLog.Settings.LogTimePeriod;

double durationInDouble = duration.GetDoubleLogDuration();

string durationInString = duration.GetStringLogDuration();

duration.Days = 7;

duration.Hours = 23;

duration.Minutes = 50;

duration.Seconds = 0;

duration.Ticks = 1;

//Method to set log duration.

duration.SetLogDuration(10, 12, 4, 5, 0);

dataLog.Backup.BackupMode = BackupMode.NoBackup;

dataLog.Backup.BackupMode = BackupMode.PrimaryPath;

dataLog.Backup.PrimaryPath = @"C:\Logs\Backup";

dataLog.Segment.SegmentMaxSize = 500;

dataLog.Segment.SegmentStartTime = DateTime.Now;

dataLog.Segment.SegmentStartTime = DateTime.Now.Date;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### DiscreteAlarms (RT Unified)

This section contains information on the following topics:

- [Description DiscreteAlarms (RT Unified)](#description-discretealarms-rt-unified)
- [DiscreteAlarms.Create() (RT Unified)](#discretealarmscreate-rt-unified)
- [DiscreteAlarms.Delete() (RT Unified)](#discretealarmsdelete-rt-unified)
- [Accessing discrete alarm properties (RT Unified)](#accessing-discrete-alarm-properties-rt-unified)
- [Accessing cross reference service on discrete alarms (RT Unified)](#accessing-cross-reference-service-on-discrete-alarms-rt-unified)

#### Description DiscreteAlarms (RT Unified)

##### Requirements

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on discrete alarms you can either use enumerate discrete alarms or use Find().

private void DiscreteAlarmBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all discrete alarms of device

HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;

foreach (HmiDiscreteAlarm discreteAlarm in discreteAlarms)

{

//working with discrete alarms.

}

}

clipboard

To access a single discrete alarm by name modify the following program code:

private void SearchDiscreteAlarm()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a specific discrete alarm from list of discrete alarms

String discreteAlarmName = "DiscreteAlarm_1";

HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;

HmiDiscreteAlarm discreteAlarmObj = discreteAlarms.Find(discreteAlarmName);

}

clipboard

##### Working with discrete alarms

You can perform the following tasks with tags while using TIA Portal Openness:

- Creating discrete alarm:[DiscreteAlarms.Create()](#discretealarmscreate-rt-unified)
- Deleting discrete alarm: [DiscreteAlarms.Delete()](#discretealarmsdelete-rt-unified)
- Discrete Alarm properties: [Accessing discrete alarm properties](#accessing-discrete-alarm-properties-rt-unified)
- Discrete Alarm cross reference service: [Accessing cross reference service on discrete alarms](#accessing-cross-reference-service-on-discrete-alarms-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### DiscreteAlarms.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a discrete alarm with Create() of HmiDiscreteAlarmComposition class modify the following program code:

private void CreateDiscreteAlarm()

{

//Create a discrete alarm with name "Alarm1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;

HmiDiscreteAlarm discreteAlarm = discreteAlarms.Create("Alarm1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### DiscreteAlarms.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a discrete alarm with Delete() of HmiDiscreteAlarm class modify the following program code :

public void DeleteDiscreteAlarm()

//User wants to delete a discrete alarm with the alarm name Alarm_1

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;

HmiDiscreteAlarm discreteAlarm = discreteAlarms.Find("Alarm1");

discreteAlarm.Delete();

}

clipboard

---

**See also**

[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)

#### Accessing discrete alarm properties (RT Unified)

##### Property

The following properties are supported in the Discrete Alarm:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| EventText | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| Id | UInt32 | Specifies the id of alarm   This id is unique value for each discrete alarm. | R/W |
| AlarmClass | String | Specifies the class of discrete alarm | R/W |
| Name | String | Specifies the name of discrete alarm | R/W |
| Priority | Byte | Specifies the priority for discrete alarm | R/W |
| Origin | String | Specifies the origin of discrete alarm | R/W |
| Area | String | Specifies the area of discrete alarm | R/W |
| RaisedStateTag | String | Specifies the tag that triggers the discrete alarm | R/W |
| RaisedStateTagBitNumber | UInt32 | Specifies the trigger bit on trigger tag | R/W |
| TriggerMode | HmiDiscreteAlarmTiggerMode | Specifies the trigger mode for discrete alarm | R/W |
| InfoText | MultilingualText | Specifies the info text of discrete alarm | R/W |
| AlarmParameterTags | Object | If array of 10 parameter tags where each tag specifies alarm parameter. Each alarm parameter takes tag name as string. These parameters can be used in alarm text. | R/W |
| EventText1 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText2 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText3 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText4 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText5 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText6 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText7 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText8 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| EventText9 | MultilingualText | Specifies the event text of HmiDiscreteAlarm | R/W |
| AcknowledgmentStateTag | String | Specifies the acknowledgment tag state for discrete alarm | R/W |
| AcknowledgmentStateTagBitNumber | UInt32 | Specifies the acknowledgment tag bit number for discrete alarm | R/W |
| AcknowledgmentControlTag | String | Specifies the Control Tag for acknowledgment of discrete alarm | R/W |
| AcknowledgmentControlTagBitNumber | UInt32 | Specifies the control tag bit number for acknowledgment of discrete alarm | R/W |
| TriggerBitAddress | String | Specifies the address of the trigger bit | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of discrete alarm modify the following program code:

private void DiscreteAlarmPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;

HmiDiscreteAlarm discreteAlarm = discreteAlarms.Find(Alarm_1);

uint id = discreteAlarm.Id;

discreteAlarm.Id = 10;

int priority = discreteAlarm.Priority;

discreteAlarm.Priority = 7;

discreteAlarm.area = "Area1";

string area = discreteAlarm.Area;

discreteAlarm.Name = "NewAlarm";

string name = discreteAlarm.Name;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing cross reference service on discrete alarms (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service with GetService() of HmiDiscreteAlarm class modify the following program code:

private void getCrossReferenceServiceforDiscreteAlarm()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;  //Accessing lower levels until we reach the HmiTagComposition.

HmiDiscreteAlarmCompositionAlarmComposition discreteAlarms = hmiSoftware.DisceteAlarms;

HmiDiscreteAlarm discreteAlarm = discreteAlarms.Find("Alarm1");

if (discreteAlarm != null)

{

try

{

CrossReferenceService crossReferenceService = discreteAlarm.GetService&lt;CrossReferenceService&gt;();

......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### LoggingTags (RT Unified)

This section contains information on the following topics:

- [Description LoggingTags (RT Unified)](#description-loggingtags-rt-unified)
- [LoggingTags.Create() (RT Unified)](#loggingtagscreate-rt-unified)
- [LoggingTags.Delete() (RT Unified)](#loggingtagsdelete-rt-unified)
- [Accessing logging tags properties (RT Unified)](#accessing-logging-tags-properties-rt-unified)

#### Description LoggingTags (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on logging tag you can either use enumerate logging tags or use Find().

private void LoggingTagBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all logging tags of device

String hmiTagName = "HMI_Tag_1";

HmiTagComposition hmiTags = hmiSoftware.Tags;

HmiTag hmiTag = hmiTags.Find(hmiTagName);

HmiLoggingTagComposition loggingTags = hmiTag.LoggingTags;

foreach (HmiLoggingTag loggingTag in loggingTags)

{

//Working with logging tags

}

}

clipboard

To access a single logging tag by name modify the following program code:

private void SearchLoggingTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for specific logging tag

String hmiTagName = "HMI_Tag_1";

String loggingTagName = "Logging_Tag1";

HmiTagComposition hmiTags = hmiSoftware.Tags;

HmiTag hmiTag = hmiTags.Find(hmiTagName);

HmiLoggingTagComposition loggingTags = hmiTag.LoggingTags";

HmiLoggingTag loggingTagObj = loggingTags.Find(loggingTagName);

}

clipboard

##### Working with logging tags

You can perform the following tasks with data logs while using TIA Portal Openness:

- Creating logging tags: [LoggingTags.Create()](#loggingtagscreate-rt-unified)
- Deleting logging tags: [LoggingTags.Delete()](#loggingtagsdelete-rt-unified)
- Logging tags properties: [Accessing logging tags properties](#accessing-logging-tags-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### LoggingTags.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a logging tag for a tag with Create() of HmiLoggingTagComposition class modify the following program code:

private void LoggingTagCreate()

{

//Create Logging Tag for given tag.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition hmiTags = hmiSoftware.Tags;

//Tag1 exists in TIA project.

HmiTag hmiTag = hmiTags.Find("Tag1");

HmiLoggingTagComposition loggingTags = hmiTag.LoggingTags;

HmiLoggingTag loggingTag = loggingTags.Create("LoggingTag1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### LoggingTags.Delete() (RT Unified)

##### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a logging tag for a tag with Delete() of HmiLoggingTag class modify the following program code :

private void LoggingTagDelete()

{

//To delete a Logging tag with name "LoggingTag_1" for tag "Tag1";

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition hmiTags = hmiSoftware.Tags;

//Tag1 exists in TIA project.

HmiTag hmiTag = hmiTags.Find("Tag1");

HmiLoggingTagComposition loggingTags = hmiTag.LoggingTags;

//LoggingTag1 exists in TIA project.

HmiLoggingTag loggingTag = loggingTags.Find("LoggingTag1");

loggingTag.Delete();

}

clipboard

#### Accessing logging tags properties (RT Unified)

##### Property

The following properties are supported in the Logging Tags:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| AggregationDelay | System.TimeSpan | Specifies the value of aggregation delay | R/W |
| AggregationMode | HmiAggregationMode | Specifies the value of aggregation mode | R/W |
| Cycle | System.String | Specifies the logging cycle of logging tag | R/W |
| CycleFactor | System.UInt32 | Specifies the value of logging cycle factor | R/W |
| DataLog | System.String | Specifies the data log of logging tag | R/W |
| HighLimit | System.Object | Specifies the high limit of logging tag | R/W |
| LimitScope | HmiLimitScope | Specifies the limit scope of logging tag | R/W |
| LoggingMode | HmiLoggingMode | Specifies the logging mode of logging tag | R/W |
| LowLimit | System. Object | Specifies the low limit of logging tag | R/W |
| Name | System.string | Specifies the name of logging tag | R/W |
| SmoothingDeltaValue | System.Double | Specifies the delta value of logging tag | R/W |
| SmoothingMaxTime | System. TimeSpan | Specifies the maximum time of logging tag | R/W |
| SmoothingMinTime | System.TimeSpan | Specifies the minimum time of logging tag | R/W |
| SmoothingMode | HmiSmoothingMode | Specifies the smoothing mode of logging tag | R/W |
| Source | System.string | Specifies the source of logging tag | R/W |
| TriggerMode | HmiTriggerMode | Specifies the trigger mode of logging tag | R/W |
| TriggerTag | System.String | Specifies the value of trigger tag | R/W |
| TriggerTagBitNumber | System.UInt32 | Specifies the value of trigger tag bit number | R/W |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of logging tags modify the following program code:

private void LoggingTagPropertiesAccess()

{

//Set and Get LoggingTag properties.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition hmiTags = hmiSoftware.Tags;

//Tag_1 exists in TIA project.

HmiTag hmiTag = hmiTags.Find("Tag_1");

HmiLoggingTagComposition loggingTags = hmiTag.LoggingTags;

//LoggingTag_1 exists in TIA project.

HmiLoggingTag loggingTag = loggingTags.Find("LoggingTag_1");

string name = loggingTag.Name;

HmiSmoothingMode smoothingMode = loggingTag.SmoothingMode;

loggingTag.SmoothingMode = HmiSmoothingMode.SwingingDoor;

HmiLimitScope limitScope = loggingTag.LimitScope;

loggingTag.LimitScope = HmiLimitScope.WithinLimits;

object lowLimit = loggingTag.LowLimit;

loggingTag.LowLimit = "-32768";

object highLimit = loggingTag.HighLimit;

loggingTag.HighLimit = "-3";

TimeSpan smoothingMinTime = loggingTag.SmoothingMinTime;

TimeSpan tsMin = TimeSpan.Parse("5:00:00");

loggingTag.SmoothingMinTime = tsMin;

TimeSpan smoothingMaxTime = loggingTag.SmoothingMaxTime;

TimeSpan tsMax = TimeSpan.Parse("1000");

loggingTag.SmoothingMaxTime = tsMax;

double smoothingDeltaValue = loggingTag.SmoothingDeltaValue;

loggingTag.SmoothingDeltaValue = 5;

string dataLog = loggingTag.Name;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### RuntimeSettings (RT Unified)

This section contains information on the following topics:

- [Description RuntimeSettings (RT Unified)](#description-runtimesettings-rt-unified)
- [Accessing runtime settings properties (RT Unified)](#accessing-runtime-settings-properties-rt-unified)

#### Description RuntimeSettings (RT Unified)

##### Requirement

- The HMI Software object is accessible.  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform task on runtime settings you can either use enumerate runtime settings or use Find( ):

private void RuntimeSettingsBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all runtime settings of device

HmiRuntimeSetting runtimeSettings = hmiSoftware.RuntimeSettings;

foreach (RuntimeSetting runtimeSetting in runtimeSettings)

{

//Working with runtime setting

}

}

clipboard

##### Working with Runtime settings

You can perform the following tasks with runtime settings while using TIA Portal Openness:

- Runtime setting properties: [Accessing runtime settings properties](#accessing-runtime-settings-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing runtime settings properties (RT Unified)

##### Property

The following properties are supported in Runtime Settings:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| HmiSoftware.RuntimeSettings | HmiRuntimeSetting | Specifies the runtime setting object | R |
| RuntimeSettings.StartScreen | String | Specifies the start screen. | R/W |
| RuntimeSettings.OperateAsOpcServer | Boolean | Specifies that given device should act as OPC server. | R/W |
| RuntimeSettings.LanguageAndFonts | HmiLanguageAndFont Association | Specifies the list of language and fonts | R |
| RuntimeSettings. LanguageAndFonts [index].Enable | Boolean | Specifies the enable / disable runtime language. | R/W |
| RuntimeSettings.LanguageAndFonts [index].EnableForLogging | Boolean | Specifies the language use for logging on runtime | R/W |
| RuntimeSettings. LanguageAndFonts [index].Order | Short | Specifies the order for transferring fonts to device. | R |
| RuntimeSettings. LanguageAndFonts [index].Language | String | Specifies the name of language | R |
| RuntimeSettings. LanguageAndFonts [index].FixedFont1 | String | Specifies the predefined font family available for font configuration | R |
| RuntimeSettings. LanguageAndFonts [index].FixedFont2 | String | Specifies the predefined font family available for font configuration | R |
| RuntimeSettings. LanguageAndFonts [index].FixedFont3 | String | Specifies the predefined font family available for font configuration | R |
| RuntimeSettings.LanguageAndFonts[index].FixedFont4 | String | Specifies the predefined font family available for font configuration | R |
| RuntimeSettings.GMPEnabled | Boolean | Specifies that given device should be enabled for audit logging or not. | R/W |
| RuntimeSettings.OpcUaServerRuntimeSettings | HmiOpcUaServerRuntimeSettings | Specifies the OPCUA settings fo the device. | R/W |
| RuntimeSettings.MaxLoginRuntimeSettings.MaxLoginErrors | UInt32 | Specifies the maximum number of login attempts before user lock | R/W |
| RuntimeSettings.MaxLoginRuntimeSettings.EnableLockAfterNumberOfAttempts | Boolean | Enable lock after login errors | R/W |
| RuntimeSettings.ProcessDiagnosticsRuntimeSettings | HmiProcessDiagnosticsRuntimeSettings | Specifies the Runtime setting of Process diagnostics | R/W |
| RuntimeSettings.HmiReportingSettings | HmiReportingSettings | Specifies the Runtime Settings of Reporting | R/W |
| RuntimeSettings.BitSelectionStrategyForResourceLists | Enum(BitNumberEvaluationType) | Specifies the bit selection strategy for text and graphic lists | R/W |

##### Requirement

- The HMI Software object is accessible.  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

private void RuntimeSettingsPropertiesAcccess()

{

//Accessing properties of RuntimeSettings

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiRuntimeSetting runtimeSettings = hmiSoftware.RuntimeSettings;

hmiSoftware.runtimeSettings.OpcUaServerRuntimeSettings.ActAsOPCServer = true;

hmiSoftware.runtimeSettings.StartScreen = "Screen_1";

hmiSoftware.runtimeSettings.LanguageAndFonts[0].Enable = true;

hmiSoftware.runtimeSettings.LanguageAndFonts[0].EnableForLogging = true;

hmiSoftware.runtimeSettings.GMPEnabled = true;

//Accessing Maximal login Runtime Settings property

var maxLoginRuntimeSettings = hmiSoftware.RuntimeSettings.MaxLoginRuntimeSettings;

maxLoginRuntimeSetttings.EnableLockAfterNumberOfAttempts = true;

var attempts = maxLoginRuntimeSetttings.EnableLockAfterNumberOfAttempts;

maxLoginRuntimeSettings.MaxLoginErrors = 1;

var maxLoginErrors = maxLoginRuntimeSettings.MaxLoginErrors;

//Accessing Process diagnostics Runtime Settings property

HmiProcessDiagnosticsRuntimeSettings hmiProcessDiagnosticsRuntimeSettings =

hmiSoftware.RuntimeSettings.ProcessDiagnosticsRuntimeSettings;

hmiProcessDiagnosticsRuntimeSettings.EnableProcessDiagnostics = true;

var enableProcessDiagnostics = hmiProcessDiagnosticsRuntimeSettings.EnableProcessDiagnostics;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### SystemTags (RT Unified)

This section contains information on the following topics:

- [Description SystemTags (RT Unified)](#description-systemtags-rt-unified)
- [Accessing system tag properties (RT Unified)](#accessing-system-tag-properties-rt-unified)

#### Description SystemTags (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access a single system tag by name modify the following program code:

private void AccessSystemTagName()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for specific system tag name from device

string systemTagName = "@SystemHealthIndex"

HmiSystemTagComposition hmiSystemTags = hmiSoftware.SystemTags;

HmiSystemTag hmiSystemTagObj = hmiSystemTags.Find(systemTagName);

}

clipboard

##### Working with system tags

You can perform the following tasks with system tags while using TIA Portal Openness:

- System tags properties: [Accessing system tag properties](#accessing-system-tag-properties-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing system tag properties (RT Unified)

##### Property

The following properties are supported in system tags:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the name of system tag | R |
| DataType | String | Specifies the data type of system tag | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of system tags modify the following program code:

private void SystemTagPropertiesAccess()

{

//Get the "Name" and "DataType" properties of system tag

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiSystemTagComposition hmiSystemTags = hmiSoftware.SystemTags;

HmiSystemTag hmiSystemTag = hmiSystemTags.Find("@UserName");

string name = hmiSystemTag.Name;

string dataType = hmiSystemTag.DataType;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Screens (RT Unified)

This section contains information on the following topics:

- [Description Screens (RT Unified)](#description-screens-rt-unified)
- [Screens.Create() (RT Unified)](#screenscreate-rt-unified)
- [Screens.Delete() (RT Unified)](#screensdelete-rt-unified)
- [Accessing screens properties (RT Unified)](#accessing-screens-properties-rt-unified)
- [Accessing cross reference service on screens (RT Unified)](#accessing-cross-reference-service-on-screens-rt-unified)
- [EventHandlers (RT Unified)](#eventhandlers-rt-unified)
- [ScreenItems (RT Unified)](#screenitems-rt-unified)

#### Description Screens (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on a screen you can use the enumerate, find, index, and Contains() method.

To access all the screens of the device modify the following program code:

private void ScreenBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the screens of device

HmiScreenComposition objScreens = hmiSoftware.Screens;

foreach (HmiScreen ObjHmiScreen in objScreens)

{

//Working with Screens

}

}

clipboard

To access screen from screens list on the basis of name modify the following program code:

private void ScreenSearch()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can search specific screen from screenlist

string hmiScreenName = "HMI_Screen_1";

HmiScreenComposition objScreens = hmiSoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find(hmiScreenName);

}

clipboard

To access screen from screens list on basis of index modify the following program code:

private void SearchScreenByIndex()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmiSoftware.Screens;

HmiScreen objHmiScreen = objScreens[0];

}

clipboard

To check a particular screen exist in screen item list by using Contains method:

private void IsScreenExist()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmiSoftware.Screens;

HmiScreen screen1 = objScreen.Find("TestScreen1");

bool isExist = objScreens.Contains(screen1);

}

clipboard

##### Working with screens

You can perform the following tasks with screens while using TIA Portal Openness:

- Creating screens:[Screens.Create()](#screenscreate-rt-unified)
- Deleting screens:[Screens.Delete()](#screensdelete-rt-unified)
- Screens properties: [Accessing screens properties](#accessing-screens-properties-rt-unified)
- Screens cross reference service: [Accessing cross reference service on screens](#accessing-cross-reference-service-on-screens-rt-unified)
- Screen event handlers property: [EventHandlers](#eventhandlers-rt-unified)
- Screen screenitems property:[ScreenItems](#screenitems-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description Screenitems (RT Unified)](#description-screenitems-rt-unified)
  
[Description EventHandlers (RT Unified)](#description-eventhandlers-rt-unified)

#### Screens.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a screen by accessing Screens property of HMISoftware object modify the following program code:

private void ScreenCreate()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmiSoftware.Screens;

HmiScreen objHmiScreen = objScreens.Create("TestScreen");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Screens.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a screen by accessing the Screens property of HmiSoftware object modify the following program code:

private void DeleteScreen()

{

//Case 1

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmiSoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find("TestScreen");

if (objHmiScreen != null)

{

objHmiScreen.Delete();

}

}

clipboard

private void ScreenDelete()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmiSoftware.Screens;

objScreens.Find("TestScreen1");

IEngineeringObject alarmClassEnggObj = (IEngineeringObject)objScreens[0];

if (alarmClassEnggObj != null)

{

alarmClassEnggObj.Invoke("Delete", null);

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing screens properties (RT Unified)

##### Property

The following properties are supported in screens:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| BackColor | Color | Specifies the background color of screen | R/W |
| AlternateBackColor | Color | Specifies the screen alternative background color to be used in fill pattern | R/W |
| Name | String | Specifies the name of screen | R/W |
| ScreenNumber | UInt16 | Specifies the configured number of screen | R/W |
| BackFillPattern | HmiFillPattern | Specifies the screen background fill pattern | R/W |
| BackGraphic | String | Specifies graphic to be shown in screen's background. | R/W |
| HorizontalAlignment | HmiHorizontalAlignment | Specifies the current scrollbar position of the parent Hmi (top level) screen window.  If the screen is smaller than its parent window, this alignment is used for positioning | R/W |
| VerticalAlignment | HmiVerticalAlignment | Specifies the current scrollbar position of the parent Hmi (top level) screen window.  If the screen is smaller than its parent window, this alignment is used for positioning | R/W |
| BackgroundFillMode | HmiBackgroundFillMode | Specifies if the background fill just screen or entire window view | R/W |
| BackGraphicStretchMode | HmiGraphicStretchMode | Specifies if the screen background graphic is streched | R/W |
| DisplayName | String | Specifies the screen display name | R/W |
| Width | uint | Specifies the dimensions of the screen in device-independend units (DIU) | r/w |
| Height | uint | Specifies the dimensions of the screen in device-independend units (DIU) |  |
| Enabled (AllowOperatorControl) | Boolean | State whether the screen is operable at all (Enable= “true”) or not | R/W |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamization collection | R |
| Parent | IEngineeringObject | Specifies the parent of this object | R |
| ScreenItems | HmiScreenItem BaseComposition | Specifies the screen items composition  For more information on screenitems, see [ScreenItems](#screenitems-rt-unified) | R/W |
| EventHandlers | HmiScreenEventHandlerComposition | Specifies the event handlers  For more information on EventHandlers, see [EventHandlers](#eventhandlers-rt-unified) | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To set properties of screen modify the following program code:

private void SettingPropertiesScreen()

{

HmiSoftware hmisoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmisoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find("TestScreen");

objHmiScreen.Width = 50;

objHmiScreen.ScreenNumber = 1;

objHmiScreen.BackGraphic = "DownArrow";

objHmiScreen.Enabled = true;

objHmiScreen.Height = 123;

}

clipboard

To get all properties of screen using GetAttributes ( ) modify the following program code:

private void GettingPropertiesScreen()

{

HmiSoftware hmisoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmisoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find("TestScreen");

List&lt;string&gt; getlststring = new List&lt;string&gt;();

getlststring.Add("AlternateBackColor");

getlststring.Add("BackColor");

getlststring.Add("BackFillPattern");

getlststring.Add("BackGraphic");

getlststring.Add("BackGraphicStretchMode");

getlststring.Add("BackgroundFillMode");

getlststring.Add("DisplayName");

//getlststring.Add("Dynamization");

getlststring.Add("Enabled");

//getlststring.Add("EnabledExplicitRelease");

getlststring.Add("Height");

getlststring.Add("HorizontalAlignment");

//getlststring.Add("Layers");

getlststring.Add("Name");

//getlststring.Add("Parent");

//getlststring.Add("ScreenElements");

//getlststring.Add("ScreenItems");

getlststring.Add("ScreenNumber");

getlststring.Add("VerticalAlignment");

getlststring.Add("Width");

var getallpropValue = objHmiScreen.GetAttributes(getlststring);

foreach(var item in getallpropValue)

{

Console.Write(item.ToString());

Console.Write("\n");

}

}

clipboard

To set all properties of screen using SetAttributes( ) modify the following program code:

private void SettingPropertyValueScreen()

{

UInt32 Height=400;

UInt32 Width = 200;

ushort ScreenNumber = 11;

HmiSoftware hmisoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmisoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find("Screen_1");

Dictionary&lt;string, object&gt; setPropertyName = new Dictionary&lt;string, object&gt;();

setPropertyName.Add("AlternateBackColor", Color.Aqua);

setPropertyName.Add("BackColor", Color.Aqua);

setPropertyName.Add("BackFillPattern", HmiFillPattern.GradientHorizontalTricolor);

setPropertyName.Add("BackGraphic", "DownArrow");

setPropertyName.Add("BackGraphicStretchMode", HmiGraphicStretchMode.Fill);

setPropertyName.Add("BackgroundFillMode", HmiBackgroundFillMode.Screen);

//setPropertyName.Add("DisplayName", "AnalogAlarmByDiffMethod");

setPropertyName.Add("Enabled", false);

//setPropertyName.Add("EnabledExplicitRelease", "AnalogAlarmByDiffMethod");

setPropertyName.Add("Height", Height);

setPropertyName.Add("HorizontalAlignment", HmiHorizontalAlignment.Right);

setPropertyName.Add("Name", "Screen_2");

setPropertyName.Add("ScreenNumber", ScreenNumber);

setPropertyName.Add("VerticalAlignment", HmiVerticalAlignment.Center);

setPropertyName.Add("Width", Width);

objHmiScreen.SetAttributes(setPropertyName);

}

clipboard

To get the value from property using IEngineeringObject's GetAttribute modify the following program code:

private void GettingPropertyValueScreen()

{

HmiSoftware hmisoftware = GetHmiSoftware();

HmiScreenComposition objScreens = hmisoftware.Screens;

HmiScreen objHmiScreen = objScreens.Find("Testscreen");

IEngineeringObject obj = objHmiScreen;

Color clraltntvbk = (Color)obj.GetAttribute("AlternateBackColor");

Color clrbk = (Color)obj.GetAttribute("BackColor");

HmiFillPattern filptrns = (HmiFillPattern)obj.GetAttribute("BackFillPattern");

string bkgrphic = (string)obj.GetAttribute("BackGraphic");

HmiGraphicStretchMode strmode = (HmiGraphicStretchMode)obj.GetAttribute("BackGraphicStretchMode");

HmiBackgroundFillMode bkgrndfilmode = (HmiBackgroundFillMode)obj.GetAttribute("BackgroundFillMode");

MultilingualText dsplyName = (MultilingualText)obj.GetAttribute("DisplayName");

//DynamizationBaseComposition dymztns = (DynamizationBaseComposition)obj.GetAttribute("Dynamizations");

bool enable = (bool)obj.GetAttribute("Enabled");

//SumRef objsom = (SomRef)obj.GetAttribute("EnableExplicitRelease");

uint Height = (uint)obj.GetAttribute("Height");

HmiHorizontalAlignment hrzntl = (HmiHorizontalAlignment)obj.GetAttribute("HorizontalAlignment");

HmiVerticalAlignment vrtcle = (HmiVerticalAlignment)obj.GetAttribute("VerticalAlignment");

//HmiLayerPartComposition objlyrs = (HmiLayerPartComposition)Obj.GetAttribute("layers");

string name = (string)obj.GetAttribute("Name");

//IEngineeringObject objparen = (IEngineeringObject)obj.GetAttribute("Parent");

//HmiscreenElementBaseComposition objelemnt = (HmiscreenElementBaseComposition)obj.GetAttribute("ScreenElements");

//HmiScreenItemBaseComposition objitems = (HmiScreenItemBaseComposition)obj.GetAttribute("ScreenItems");

ushort scrnmumber = (ushort)obj.GetAttribute("ScreenNumber");

uint width = (uint)obj.GetAttribute("Width");

}

clipboard

To determine if all properties of screen have valid values modify the following program code:

private void IsValidPropertyValue()

{

HmiSoftware hmiSoftware = GetHmiSoftware ();

HmiScreen objHmiScreen = hmiSoftware.Screens.Create("HmiScreen_1");

IList&lt;IValidator&gt; objectsToValidate = new List&lt;IValidator&gt;();

foreach (var item in hmiSoftware.Screens)

{

objectsToValidate.Add(item);

}

foreach (IValidator validator in objectsToValidate)

{

IList&lt;HmiValidationResult&gt; errors = validator.Validate();

if (errors != null &amp;&amp; errors.Count &gt; 0)

{

foreach (var errornotification in errors)

{

var propName = errornotification.PropertyName;

foreach (var errormasage in errornotification.Errors)

{

Console.WriteLine(errormasage);

}

}

}

}

}

clipboard
> **Note**
>
> If during set of properties the set operation is not able to set the value then a Recoverable exception is thrown

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description Screenitems (RT Unified)](#description-screenitems-rt-unified)

#### Accessing cross reference service on screens (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service with GetService() of screen class modify the following program code:

private void AccessCrossReferenceServiceforScreen()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware; //Accessing lower levels until we reach the ScreenComposition.

ScreenComposition screenComposition = hmiSoftware.Screens;

Screen screen = screenComposition.Find("Screen_1");

if (screen != null)

{

try

{

CrossReferenceService crossReferenceService = screen.GetService&lt;CrossReferenceService&gt;();

// ......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

clipboard

#### EventHandlers (RT Unified)

This section contains information on the following topics:

- [Description EventHandlers (RT Unified)](#description-eventhandlers-rt-unified)
- [EventHandlers.Create() (RT Unified)](#eventhandlerscreate-rt-unified)
- [EventHandlers.Delete() (RT Unified)](#eventhandlersdelete-rt-unified)
- [Accessing EventHandlers properties (RT Unified)](#accessing-eventhandlers-properties-rt-unified)

##### Description EventHandlers (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access event handler for screen items modify the following program code:

private void AccessEvent(HmiSoftware hmiSoftware);

{

var screenComp = ((HmiSoftware)targetSWTag).Screens;

HmiScreen screenOne = screenComp.Create("Screen2");

HmiScreenEventHandler screenHandler = screenOne.EventHandlers.Create(HmiScreenEventType.Unloaded);

HmiScreenEventHandler screenHandlerSearched = screenOne.EventHandlers.Find(HmiScreenEventType.Unloaded);

}

clipboard

###### Working with event for screen items

You can perform the following tasks with event for screen items while using TIA Portal Openness:

- Creating Event Handlers : [EventHandlers.Create()](#eventhandlerscreate-rt-unified)
- Deleting Event Handlers [EventHandlers.Delete()](#eventhandlersdelete-rt-unified)
- Event Handlers properties: [Accessing EventHandlers properties](#accessing-eventhandlers-properties-rt-unified)

##### EventHandlers.Create() (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To create events at the screen item level object using EventHandler navigator modify the following program code:

private void CreateEvents(HmiSoftware hmiSoftware)

{

var screenComp = ((HmiSoftware)targetSWTag).Screens;

HmiScreen screenOne = screenComp.Create(string screenName = "Screen2");

HmiScreenEventHandler screenHandler = screenOne.EventHandlers.Create(HmiScreenEventType.Unloaded);

}

clipboard

##### EventHandlers.Delete() (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To delete events for screen and screen items modify the following program code:

private void DeletePropertyEvent(HmiSoftware hmisoftware)

{

HmiScreen hmiscreen = hmisoftware.Screens.Create(Guid.NewGuid().ToString());

var hmiscreenPropEventDyn = hmiscreen.EventHandlers.Create("Enabled", PropertyEventType.Change);

var enabledevent = hmiscreen.EventHandlers.Find("Enabled", PropertyEventType.Change);

enabledevent.Delete();

}

clipboard

##### Accessing EventHandlers properties (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of events for screen and screen items modify the following program code :

private void AccessEvent(HmiSoftware hmiSoftware)

{

var screenComp = ((HmiSoftware)targetSWTag).Screens;

HmiScreen screenOne = screenComp.Create("Screen2");

HmiScreenEventHandler screenHandler = screenOne.EventHandlers.Create(HmiScreenEventType.Unloaded);

Console.WriteLine(screenOne.Name + ".EventHandler.EventType - {0}", screenHandler.EventType);

Console.WriteLine(screenOne.Name + ".EventHandler.Script.Async - {0}", screenHandler.Script.Async);

Console.WriteLine(screenOne.Name + ".EventHandler.Script.GlobalDefinitionAreaScriptCode - {0}", screenHandler.Script.GlobalDefinitionAreaScriptCode);

Console.WriteLine(screenOne.Name + ".EventHandler.Script.ScriptCode - {0}", screenHandler.Script.ScriptCode);

}

clipboard

#### ScreenItems (RT Unified)

This section contains information on the following topics:

- [Description Screenitems (RT Unified)](#description-screenitems-rt-unified)
- [ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)
- [ScreenItems.Delete() (RT Unified)](#screenitemsdelete-rt-unified)
- [Screenitem objects (RT Unified)](#screenitem-objects-rt-unified)
- [Basic objects (RT Unified)](#basic-objects-rt-unified)
- [Elements (RT Unified)](#elements-rt-unified)
- [Controls (RT Unified)](#controls-rt-unified)
- [My controls (RT Unified)](#my-controls-rt-unified)
- [Dynamic widgets (RT Unified)](#dynamic-widgets-rt-unified)
- [PropertyEventHandlers (RT Unified)](#propertyeventhandlers-rt-unified)
- [Accessing cross reference service on screenitems (RT Unified)](#accessing-cross-reference-service-on-screenitems-rt-unified)

##### Description Screenitems (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To perform a task on screenitems you can use enumerate, find, index commands and the Contains() method.

private void ScreenItemsBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

// User can navigate all screen items of screen

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

foreach (var item in screenitems)

{

//Working with screenitems

}

}

clipboard

To access a screenitem from screenitems list by name modify the following program code :

private void SearchScreenItem()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

string hmiScreenItemName = "Line_1";

HmiScreenItemBase screenitems = hmiScreen.ScreenItems.Find(hmiScreenItemName);

}

clipboard

To access screenitem from screenitems list by index modify the following program code :

private void SearchScreenItemByIndex()

{

HmiScreenItemBase screenitem = hmiScreen.ScreenItems[1];

}

clipboard

To check a particular screenitem exist in screenitem list by using Contains method modify the following program code:

private void IsScreenItemExist()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Create("Screen_21");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiLine hmiLine = screenitems.Create&lt;HmiLine&gt;("ScreenItems_1");

bool isexists = screenitems.Contains(hmiLine);

}

clipboard

###### Working with screen items

You can perform the following tasks with screen items while using TIA Portal Openness:

- Creating screen items: [ScreenItems.Create()](#screenitemscreate-rt-unified)
- Deleting screen items: [ScreenItems.Delete()](#screenitemsdelete-rt-unified)
- Screenitem object list: [Screenitem objects](#screenitem-objects-rt-unified)
- Screenitems cross reference service: [Accessing cross reference service on screenitems](#accessing-cross-reference-service-on-screenitems-rt-unified)
- Screenitems property event handlers: [PropertyEventHandlers](#propertyeventhandlers-rt-unified)

---

**See also**

[Screens.Create() (RT Unified)](#screenscreate-rt-unified)
  
[Screens.Delete() (RT Unified)](#screensdelete-rt-unified)
  
[Accessing line properties (RT Unified)](#accessing-line-properties-rt-unified)
  
[Accessing polyline properties (RT Unified)](#accessing-polyline-properties-rt-unified)
  
[Accessing polygon properties (RT Unified)](#accessing-polygon-properties-rt-unified)
  
[Accessing ellipse properties (RT Unified)](#accessing-ellipse-properties-rt-unified)
  
[Accessing ellipse segment properties (RT Unified)](#accessing-ellipse-segment-properties-rt-unified)
  
[Accessing circle segment properties (RT Unified)](#accessing-circle-segment-properties-rt-unified)
  
[Accessing elliptical arc properties (RT Unified)](#accessing-elliptical-arc-properties-rt-unified)
  
[Accessing circular arc properties (RT Unified)](#accessing-circular-arc-properties-rt-unified)
  
[Accessing circle properties (RT Unified)](#accessing-circle-properties-rt-unified)
  
[Accessing rectangle properties (RT Unified)](#accessing-rectangle-properties-rt-unified)
  
[Accessing graphic view properties (RT Unified)](#accessing-graphic-view-properties-rt-unified)

##### ScreenItems.Create() (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To create a Hmiline screen items with Create() of HmiScreenItemBaseComposition class modify the following program code:

private void ScreenItemCreate()

{

// Creating a Hmiline screenitem

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Create("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens[0].ScreenItems;

HmiLine hmiLine = screenitems.Create&lt;HmiLine&gt;("ScreenItem_1");

}

clipboard

To create a HmiIOField screenitem with Create() of HmiScreenItemBaseComposition class modify the following program code:

private void CreateScreenItem()

{

// Creating a HmiIOField screenitem

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiIOField hmiIOField = screenitems.Create&lt;HmiIOField&gt;("ScreenItem_1");

}

clipboard

To create a HmiAlarmControl screenitem with Create() of HmiScreenItemBaseComposition class modify the following program code:

private void ControlScreenItemCreate()

{

// Creating a HmiAlarmControl screenitem

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiAlarmControl hmiAlarmControl = screenitems.Create&lt;HmiAlarmControl&gt;("ScreenItem_12");

}

clipboard

To create a faceplate container with create() of HmiScreenItemBaseComposition class modify the following program code:

private void createFaceplateContainer(HmiSoftware hmiSoftware, string screenName = "screen_1",

string faceplatecontainerName = "Faceplate container_1")

{

HmiScreen hmiScreen= hmiSoftware.Screens.Find(screenName);

HmiScreenItemBaseComposition screenItems = hmiSoftware.ScreenItems;

HmiFaceplateContainer faceplate = screenItems.Create&lt;HmiFaceplateContainer&gt;(faceplatecontainerName);

}

clipboard

> **Note**
>
> To create other screenitems, you can provide the screenitems type name supported in TIA Portal Openness.

##### ScreenItems.Delete() (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To delete hmiLine screenitems modify the following program code

private void ScreenItemsDelete()

{

//Case 1

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiLine hmiLine = screenitems.Create&lt;HmiLine&gt;("ScreenItem_1");

if (hmiLine != null)

{

hmiLine.Delete();

}

}

clipboard

private void ScreenItemDelete()

{

//Case 2

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiLine hmiLine = (HmiLine)screenitems.Find("ScreenItem_12");

IEngineeringObject ObjhmiLineEnggObj = hmiLine;

if (ObjhmiLineEnggObj != null)

{

ObjhmiLineEnggObj.Invoke("Delete", null);

}

}

clipboard

To delete faceplate container screenitem modify the following program code:

private void DeleteFaceplateInstance(HmiSoftware hmiSoftware, string faceplateContainerName = "Faceplatecontainer_1")

{

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiFaceplateContainer faceplate = (HmiFaceplateContainer)hmiScreen.ScreenItems.Find(faceplateContainerName);

If (faceplate! = null)

{

faceplate.Delete ();

}

}

clipboard

##### Screenitem objects (RT Unified)

###### Introduction

The following screen items are supported in the TIA Portal Openness:

| Namespace (s) | Screen object name | Screen Item name | Type | Property |
| --- | --- | --- | --- | --- |
| Siemens.Engineering.HmiUnified.UI.Shapes  Siemens.Engineering.HmiUnified.UI.Base | Base objects | Circle | HmiCircle | For details on Circle properties, see [Accessing circle properties](#accessing-circle-properties-rt-unified) |
| Circular arc | HmiCircularArc | For details on Circular arc properties, see [Accessing circular arc properties](#accessing-circular-arc-properties-rt-unified) |  |  |
| Circle Segment | HmiCircleSegment | For details on Circle segment properties, see[Accessing circle segment properties](#accessing-circle-segment-properties-rt-unified) |  |  |
| Ellipse | HmiEllipse | For details on ellipse properties, see [Accessing ellipse properties](#accessing-ellipse-properties-rt-unified) |  |  |
| Elliptical arc | HmiEllipticalArc | For details on Elliptical arc properties, see [Accessing elliptical arc properties](#accessing-elliptical-arc-properties-rt-unified) |  |  |
| Ellipse Segment | HmiEllipseSegment | For details on ellipse segment properties, see [Accessing ellipse segment properties](#accessing-ellipse-segment-properties-rt-unified) |  |  |
| Graphic view | HmiGraphicView | For details on Graphic view properties, see [Accessing graphic view properties](#accessing-graphic-view-properties-rt-unified) |  |  |
| Line | HmiLine | For details on line properties, see [Accessing line properties](#accessing-line-properties-rt-unified) |  |  |
| Polyline | HmiPolyline | For details on polyline properties, see [Accessing polyline properties](#accessing-polyline-properties-rt-unified) |  |  |
| Polygon | HmiPolygon | For details on polygon properties, see [Accessing polygon properties](#accessing-polygon-properties-rt-unified) |  |  |
| Rectangle | HmiRectangle | For details on Rectangle properties, see [Accessing rectangle properties](#accessing-rectangle-properties-rt-unified) |  |  |
| Text Box | HmiTextBox | For details on Textbox properties, see [Accessing textbox properties](#accessing-textbox-properties-rt-unified) |  |  |
| Siemens.Engineering.HmiUnified.ModernUI.Widgets Siemens.Engineering.HmiUnified.ModernUI.Base | Elements | Bar | HmiBar | For details on Bar properties, see[Accessing bar properties](#accessing-bar-properties-rt-unified) |
| Button | HmiButton | For details on Button properties, see [Accessing button properties](#accessing-button-properties-rt-unified) |  |  |
| Checkbox | HmiCheckBoxGroup | For details on Checkbox properties, see [Accessing check box properties](#accessing-check-box-properties-rt-unified) |  |  |
| Clock | HmiClock | For details on Clock properties, see [Accessing clock properties](#accessing-clock-properties-rt-unified) |  |  |
| Gauge | HmiGauge | For details on Gauge properties, see [Accessing gauge properties](#accessing-gauge-properties-rt-unified) |  |  |
| IO Field | HmiIOField | For details on IO Field properties, see [Accessing IO Field properties](#accessing-io-field-properties-rt-unified) |  |  |
| Listbox | HmiListBox | For details on Listbox properties, see [Accessing listbox properties](#accessing-listbox-properties-rt-unified) |  |  |
| RadioButton | HmiRadioButtonGroup | For details on RadioButton properties, see [Accessing radio button properties](#accessing-radio-button-properties-rt-unified) |  |  |
| Slider | HmiSlider | For details on Slider properties, see [Accessing slider properties](#accessing-slider-properties-rt-unified) |  |  |
| Switch | HmiToggleSwitch | For details on Switch properties, see [Accessing switch properties](#accessing-switch-properties-rt-unified) |  |  |
| Symbolic IOField | HmisymbolicIOField | For details on Symbolic IO Field properties, see [Accessing symbolic IOField properties](#accessing-symbolic-iofield-properties-rt-unified) |  |  |
| TouchArea | HmiTouchArea | For details on Touch Area properties, see [Accessing touch area properties](#accessing-touch-area-properties-rt-unified) |  |  |
| Siemens.Engineering.HmiUnified.ModernUI.Controls Siemens.Engineering.HmiUnified.ModernUI.Base | Controls | Alarm Control | HmiAlarmControl | For details on Alarm Control properties, see [Accessing alarm control properties](#accessing-alarm-control-properties-rt-unified) |
| Function Trend Control | HmiFunctionTrendControl | For details on Function Trend Control properties, see [Accessing function trend control properties](#accessing-function-trend-control-properties-rt-unified) |  |  |
| Faceplate Container | HmiFaceplateContainer | For details on Faceplate Container properties, see [Faceplate Container](#faceplate-container-rt-unified) |  |  |
| Media Player | HmiMediaControl | For details on Media Player properties, see [Accessing media player properties](#accessing-media-player-properties-rt-unified) |  |  |
| Process Control | HmiProcessControl | For details on Process Control properties, see [Accessing process control properties](#accessing-process-control-properties-rt-unified) |  |  |
| Parameter Set Control | HmiDetailedParameterControl | For details on Parameter Set Control properties, see [Accessing parameter set control properties](#accessing-parameter-set-control-properties-rt-unified) |  |  |
| Screen Window | HmiScreenWindow | For details on Screen Window properties, see [Accessing screen window properties](#accessing-screen-window-properties-rt-unified) |  |  |
| System Diagnosis Control | HmiSystemDiagnosisControl | For details on System Diagnosis Control properties, see [Accessing system diagnosis control properties](#accessing-system-diagnosis-control-properties-rt-unified) |  |  |
| Trend Control | HmiTrendControl | For details on Trend Control properties, see [Accessing trend control properties](#accessing-trend-control-properties-rt-unified) |  |  |
| Trend Companion | HmiTrendCompanion | For details on Trend Companion properties, see [Accessing trend companion properties](#accessing-trend-companion-properties-rt-unified) |  |  |
| Web Control | HmiWebControl | For details on Web Control properties, see [Accessing web control properties](#accessing-web-control-properties-rt-unified) |  |  |
| My controls | Custom Web Control Container | HmiCustomWebControlContainer | For details on Custom Web Control Container properties, see [Accessing custom web control container properties](#accessing-custom-web-control-container-properties-rt-unified) |  |
| Dynamic widgets | Custom Widget Container | HmiCustomWidgetContainer | For details on Custom Widget Container properties, see [Accessing custom widget container properties](#accessing-custom-widget-container-properties-rt-unified) |  |

##### Basic objects (RT Unified)

This section contains information on the following topics:

- [Accessing circle properties (RT Unified)](#accessing-circle-properties-rt-unified)
- [Accessing circular arc properties (RT Unified)](#accessing-circular-arc-properties-rt-unified)
- [Accessing circle segment properties (RT Unified)](#accessing-circle-segment-properties-rt-unified)
- [Accessing ellipse properties (RT Unified)](#accessing-ellipse-properties-rt-unified)
- [Accessing elliptical arc properties (RT Unified)](#accessing-elliptical-arc-properties-rt-unified)
- [Accessing ellipse segment properties (RT Unified)](#accessing-ellipse-segment-properties-rt-unified)
- [Accessing graphic view properties (RT Unified)](#accessing-graphic-view-properties-rt-unified)
- [Accessing line properties (RT Unified)](#accessing-line-properties-rt-unified)
- [Accessing polyline properties (RT Unified)](#accessing-polyline-properties-rt-unified)
- [Accessing polygon properties (RT Unified)](#accessing-polygon-properties-rt-unified)
- [Accessing rectangle properties (RT Unified)](#accessing-rectangle-properties-rt-unified)
- [Accessing textbox properties (RT Unified)](#accessing-textbox-properties-rt-unified)

###### Accessing circle properties (RT Unified)

###### Property

The following properties are supported in circle screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| BorderColor | Color | Specifies the border color of circle | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of circle | R/W |
| BackColor | Color | Specifies the background color of circle | R/W |
| AlternateBackColor | Color | Specifies the alternate background color of circle | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of circle | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of circle | R/W |
| BorderWidth | byte | Specifies the border width of circle | R/W |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of circle | R/W |
| FillLevel | byte | Specifies the fill level of circle | R/W |
| FillDirection | HmiFillDirection | Specifies the fill direction of circle | R/W |
| DashType | HmiDashType | Specifies the line type of circle | R/W |
| ShowFillLevel | bool | Specifies the show fill level of circle | R/W |
| Radius | uint | Specifies the radius of circle | R/W |
| CenterX | int | Specifies the X position of circle | R/W |
| CenterY | int | Specifies the Y position of circle | R/W |
| RotationAngle | short | Specifies the rotation angle of circle | R/W |
| RotationCenterX | float | Specifies the X pivot point of circle | R/W |
| RotationCenterY | float | Specifies the Y pivot point of circle | R/W |
| Opacity | float | Specifies the opacity of circle  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of circle  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies the visiblity of circle | R/W |
| TabIndex | ushort | Specifies the tab index of circle | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of circle | R/W |
| Authorization | string | Specifies the authorization of circle | R/W |
| EventHandlers | HmiCircleEventHandlerComposition | Specifies the event handle of circle | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamization of circle | R |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handle of circle | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of circle screen items modify the following program code:

private void CircleScreenItemsPropertiesAccess

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiCircle circle = screenitems.Create&lt;HmiCircle&gt;("Default Value55647");

//Name

var name = circle.Name;

circle.Name = "Default Value6834e";

//BorderColor

var bordercolor = circle.BorderColor;

circle.BorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = circle.BorderWidth;

circle.BorderWidth = 10;

//ToolTipText

var tooltip = circle.ToolTipText;

var tooltiptext = circle.ToolTipText.Items[0].Text;

circle.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//DashType

var dashtype = circle.DashType;

circle.DashType = HmiDashType.Solid;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing circular arc properties (RT Unified)

###### Property

The following properties are supported in circular arc screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| StartAngle | int | Specifies the start angle of circular arc | R/W |
| AngleRange | int | Specifies the angle range of circular arc | R/W |
| LineColor | Color | Specifies the line color of circular arc | R/W |
| AlternateLineColor | Color | Specifies the alternative border color of circular arc | R/W |
| DashType | HmiDashType | Specifies the line type of circular arc | R/W |
| EndType | HmiLineEndType | Specifies the end line of circular arc | R/W |
| StartType | HmiLineEndType | Specifies the start line of circular arc | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of circular arc | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of circle arc | R/W |
| CapType | HmiCapType | Specifies the cap type of circular arc | R/W |
| LineWidth | byte | Specifies the line width of circular arc | R/W |
| Radius | uint | Specifies the radius of circular arc | R/W |
| CenterX | int | Specifies the X position of circular arc | R/W |
| CenterY | int | Specifies the Y position of circular arc | R/W |
| RotationAngle | short | Specifies the rotation angle of circular arc | R/W |
| RotationCenterX | float | Specifies the X pivot point of circular arc | R/W |
| RotationCenterY | float | Specifies the Y pivot point of circular arc | R/W |
| Opacity | float | Specifies the opacity of circle arc  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of circular arc  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies the visiblity of circular arc | R/W |
| TabIndex | ushort | Specifies the tab index of circular arc | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of circular arc | R/W |
| Authorization | string | Specifies the authorization of circular arc | R/W |
| EventHandlers | HmiCircularArcEventHandlerComposition | Specifies the event handle of circular arc | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of circlular arc screen items modify the following program code:

private void CircularArcScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiCircularArc circulararc = screenitems.Create&lt;HmiCircularArc&gt;("Default Value57");

//Name

var name = circulararc.Name;

circulararc.Name = "Default Value567";

//LineColor

var linecolor = circulararc.LineColor;

circulararc.LineColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//LineWidth

var linewidth = circulararc.LineWidth;

circulararc.LineWidth = 10;

//ToolTipText

var tooltip = circulararc.ToolTipText;

var tooltiptext = circulararc.ToolTipText.Items[0].Text;

circulararc.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//CapType

var captype = circulararc.CapType;

circulararc.CapType = HmiCapType.Round;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing circle segment properties (RT Unified)

###### Property

The following properties are supported in circle segment screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| StartAngle | int | Specifies the start angle of circle segment | R/W |
| AngleRange | int | Specifies the angle range of circle segment | R/W |
| BorderColor | Color | Specifies the border color of circle segment | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of circle segment | R/W |
| BackColor | Color | Specifies the background color of circle segment | R/W |
| AlternateBackColor | Color | Specifies the alternate background color of circle segment | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of circle segment | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of circle segment | R/W |
| BorderWidth | byte | Specifies the border width of circle segment | R/W |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of circle segment | R/W |
| FillLevel | byte | Specifies the fill level of circle segment | R/W |
| FillDirection | HmiFillDirection | Specifies the fill direction of circle segment | R/W |
| DashType | HmiDashType | Specifies the line type of circle segment | R/W |
| ShowFillLevel | bool | Specifies the show level of circle segment | R/W |
| Radius | uint | Specifies the radius of circle segment | R/W |
| CenterX | int | Specifies the X position of circle segment | R/W |
| CenterY | int | Specifies the Y position of circle segment | R/W |
| RotationCenterX | float | Specifies the X pivot point of circle segment | R/W |
| RotationCenterY | float | Specifies the Y pivot point of circle segment | R/W |
| RotationAngle | short | Specifies the rotation angle of circle segment | R/W |
| Opacity | float | Specifies the opacity of circle segment  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of circle segment  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies the visiblity of circle segment | R/W |
| TabIndex | ushort | Specifies the tab index of circle segment | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of circle segment | R/W |
| Authorization | string | Specifies the authorization of circle segment | R/W |
| EventHandlers | HmiCircleSegmentEventHandlerComposition | Specifies the event handle of circle segment | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamization of circle segment | R |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handler of circle segment | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of circle segment screen items modify the following program code:

private void CircleSegmentScreenItemPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiCircleSegment circlesegment = screenitems.Create&lt;HmiCircleSegment&gt;("Default Value5987");

//Name

var name = circlesegment.Name;

circlesegment.Name = "Default Value59876";

//AlternateBorderColor

var bordercolor = circlesegment.AlternateBorderColor;

circlesegment.AlternateBorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = circlesegment.BorderWidth;

circlesegment.BorderWidth = 10;

//ToolTipText

var tooltip = circlesegment.ToolTipText;

var tooltiptext = circlesegment.ToolTipText.Items[0].Text;

circlesegment.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing ellipse properties (RT Unified)

###### Property

The following properties are supported in ellipse screen items :

| Property name | Property type | Description | Access |
| --- | --- | --- | --- |
| BorderColor | Color | Specifies the border color of ellipse | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of ellipse | R/W |
| BackColor | Color | Specifies the background color of ellipse | R/W |
| AlternateBackColor | Color | Specifies the alternative background color of ellipse | R/W |
| BorderWidth | byte | Specifies the border width of ellipse | R/W |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of ellipse | R/W |
| FillLevel | byte | Specifies the fill level of ellipse | R/W |
| FillDirection | HmiFillDirection | Specifies the fill direction of ellipse | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of ellipse | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of ellipse | R/W |
| DashType | HmiDashType | Specifies the line type of ellipse | R/W |
| ShowFillLevel | bool | Specifies the fill level of ellipse | R/W |
| RadiusX | uint | Specifies the X radius of ellipse | R/W |
| RadiusY | uint | Specifies the Y radius of ellipse | R/W |
| CenterX | int | Specifies the X position of ellipse | R/W |
| CenterY | int | Specifies the Y position of ellipse | R/W |
| RotationAngle | short | Specifies the rotation of ellipse | R/W |
| RotationCenterX | float | Specifies the X pivot point of ellipse | R/W |
| RotationCenterY | float | Specifies the Y pivot point of ellipse | R/W |
| Opacity | float | Specifies the opacity of ellipse  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of ellipse  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of ellipse | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of ellipse | R/W |
| Authorization | string | Specifies the authorization of ellipse | R/W |
| EventHandlers | HmiPolylgonEventHandlerComposition | Specifies the event handle of ellipse | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of ellipse screen items modify the following program code :

private void EllipseScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiEllipse ellipse = screenitems.Create&lt;HmiEllipse&gt;("Default Value5");

//Name

var name = ellipse.Name;

ellipse.Name = "Default Value5";

//AlternateBorderColor

var bordercolor = ellipse.AlternateBorderColor;

ellipse.AlternateBorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = ellipse.BorderWidth;

ellipse.BorderWidth = 10;

//ToolTipText

var tooltip = ellipse.ToolTipText;

var tooltiptext = ellipse.ToolTipText.Items[0].Text;

ellipse.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//BackFillPattern

var backfill = ellipse.BackFillPattern;

ellipse.BackFillPattern = HmiFillPattern.GradientBackwardDiagonal;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing elliptical arc properties  (RT Unified)

###### Property

The following properties are supported in elliptical arc screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| StartAngle | int | Specifies the start angle of elliptical arc | R/W |
| AngleRange | int | Specifies the angle range of elliptical arc | R/W |
| LineColor | Color | Specifies the line color of elliptical arc | R/W |
| AlternateLineColor | Color | Specifies the alternative border color of elliptical arc | R/W |
| StartType | HmiLineStartType | Specifies the start line of elliptical arc | R/W |
| EndType | HmiLineEndType | Specifies the end line of elliptical arc | R/W |
| CapType | HmiCapType | Specifies the cap type of elliptical arc | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of elliptical arc | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of elliptical arc | R/W |
| DashType | HmiDashType | Specifies the line type of elliptical arc | R/W |
| LineWidth | byte | Specifies the line width of elliptical arc | R/W |
| RadiusX | uint | Specifies the X radius of elliptical arc | R/W |
| RadiusY | uint | Specifies the Y radius of elliptical arc | R/W |
| CenterX | int | Specifies the X position of elliptical arc | R/W |
| CenterY | int | Specifies the Y position of elliptical arc | R/W |
| RotationAngle | short | Specifies the rotation angle of elliptical arc | R/W |
| RotationCenterX | float | Specifies the X pivot point of elliptical arc | R/W |
| RotationCenterY | float | Specifies the Y pivot point of elliptical arc | R/W |
| Opacity | float | Specifies the opacity of elliptical arc  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of elliptical arc  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies the visiblity of elliptical arc | R/W |
| TabIndex | ushort | Specifies the tab index of elliptical arc | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of elliptical arc | R/W |
| Authorization | string | Specifies the authorization of elliptical arc | R/W |
| EventHandlers | HmiEllipticalArcEventHandlerComposition | Specifies the event handle of elliptical arc | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access basic property of elliptical arc screen items modify the following program code:

private void EllipticalArcScreenItemPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiEllipticalArc ellipticalarc = screenitems.Create&lt;HmiEllipticalArc&gt;("Default Value53987");

//Name

var name = ellipticalarc.Name;

ellipticalarc.Name = "Default Value123124e";

//LineColor

var linecolor = ellipticalarc.LineColor;

ellipticalarc.LineColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//LineWidth

var linewidth = ellipticalarc.LineWidth;

ellipticalarc.LineWidth = 10;

//ToolTipText

var tooltip = ellipticalarc.ToolTipText;

var tooltiptext = ellipticalarc.ToolTipText.Items[0].Text;

ellipticalarc.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//CapType

var captype = ellipticalarc.CapType;

ellipticalarc.CapType = HmiCapType.Round;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing ellipse segment properties (RT Unified)

###### Property

The following properties are supported in ellipse segment segment screen item:

| Property name | Property type | Description | Access |
| --- | --- | --- | --- |
| StartAngle | int | Specifies the start angle of ellipse segment | R/W |
| AngleRange | int | Specifies the angle range of ellipse segment | R/W |
| BorderColor | Color | Specifies the border color of ellipse segment | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of ellipse segment | R/W |
| BackColor | Color | Specifies the background color of ellipse segment | R/W |
| AlternateBackColor | Color | Specifies the alternate background color of ellipse segment | R/W |
| BorderWidth | byte | Specifies the border width of ellipse segment | R/W |
| BackFillPattern | byte | Specifies the background fill pattern of ellipse segment | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of ellipse segment | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of ellipse segment | R/W |
| FillLevel | byte | Specifies the fill level of ellipse segment |  |
| FillDirection | HmiFillDirection | Specifies the fill direction of ellipse segment | R/W |
| DashType | HmiDashType | Specifies the line type of ellipse segment | R/W |
| ShowFillLevel | bool | Specifies the show level of ellipse segment | R/W |
| RadiusX | uint | Specifies the X radius of ellipse segment | R/W |
| RadiusY | uint | Specifies the Y radius of ellipse segment | R/W |
| CenterX | int | Specifies the X position of ellipse segment | R/W |
| CenterY | int | Specifies the Y position of ellipse segment | R/W |
| RotationAngle | short | Specifies the rotation angle of ellipse segment | R/W |
| RotationCenterX | float | Specifies the X pivot point of ellipse segment | R/W |
| RotationCenterY | float | Specifies the Y pivot point of ellipse segment | R/W |
| Opacity | float | Specifies the opacity of ellipse segment  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of ellipse segment  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of ellipse segment | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of ellipse segment | R/W |
| Authorization | string | Specifies the authorization of ellipse segment | R/W |
| EventHandlers | HmiEllipseEventHandlerComposition | Specifies the event handle of ellipse segment | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of ellipse segment screen items modify the following program code:

private void EllipseSegmentScreenItemPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiEllipseSegment ellipsesegment = screenitems.Create&lt;HmiEllipseSegment&gt;("Default Value5");

//Name

var name = ellipse segmentsegment.Name;

ellipse segmentsegment.Name = "Default Value56";

//AlternateBorderColor

var bordercolor = ellipse segmentsegment.AlternateBorderColor;

ellipse segmentsegment.AlternateBorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = ellipse segmentsegment.Height;

ellipse segmentsegment.BorderWidth = 10;

//ToolTipText

var tooltip = ellipse segmentsegment.ToolTipText;

var tooltiptext = ellipse segmentsegment.ToolTipText.Items[0].Text;

ellipse segmentsegment.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//BackFillPattern

var backfill = ellipse segmentsegment.BackFillPattern;

ellipse segmentsegment.BackFillPattern = HmiFillPattern.GradientBackwardDiagonal;

}

clipboard

###### Accessing graphic view properties (RT Unified)

###### Property

The following properties are supported in graphic view screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| GraphicStretchMode | HmiGraphicStretchMode | Specifies the scale background graphic | R/W |
| FillLevel | byte | Specifies the fill level of graphic view | R/W |
| FillDirection | HmiFillDirection | Specifies the fill direction of graphic view | False |
| ShowFillLevel | bool | Specifies the show level of graphic view | False |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of graphic view | R/W |
| AlternateBackColor | Color | Specifies the alternate background color of graphic view | R/W |
| Enabled | Bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of graphic view | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of graphic view | R/W |
| Top | int | Specifies the Y position of graphic view | R/W |
| Left | int | Specifies the X position of graphic view | R/W |
| Width | uint | Specifies the width of graphic view | R/W |
| Height | uint | Specifies the height of graphic view | R/W |
| Padding | HmiPaddingPart | Specifies the spacing of graphic view | R |
| RotationAngle | short | Specifies the rotation angle of graphic view | R/W |
| RotationCenterX | float | Specifies the X pivot point of graphic view | R/W |
| RotationCenterY | float | Specifies the Y pivot point of graphic view | R/W |
| Opacity | float | Specifies the opacity of graphic view  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of graphic view  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies the visiblity of graphic view | R/W |
| Graphic | string | Specifies the graphic of graphic view | R/W |
| TabIndex | ushort | Specifies the tab index of graphic view | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of graphic view | R/W |
| Authorization | string | Specifies the authorization of graphic view | R/W |
| EventHandlers | HmiGraphicViewEventHandlerComposition | Specifies the event handle of graphic view | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of graphic view screenitems modify the following program code:

private void GraphicViewScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiGraphicView graphicview = screenitems.Create&lt;HmiGraphicView&gt;("Default Value35487");

//Name

var name = graphicview.Name;

graphicview.Name = "Default Value765";

//AlternateBackColor

var backcolor = graphicview.AlternateBackColor;

graphicview.AlternateBackColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//Height

var height = graphicview.height;

graphicview.Height = 10;

//ToolTipText

var tooltip = graphicview.ToolTipText;

var tooltiptext = graphicview.ToolTipText.Items[0].Text;

graphicview.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//Padding

var padding = graphicview.Padding;

var bottom = padding.Bottom;

padding.Bottom = 50;

var left = padding.Left;

padding.Left = 60;

var right = padding.Right;

padding.Right = 70;

var top = padding.Top;

padding.Top = 50;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing line properties (RT Unified)

###### Property

The following properties are supported in line screen item:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| X1 | int | Specifies the start point of X - axis | R/W |
| Y1 | int | Specifies the start point of Y - axis | R/W |
| X2 | int | Specifies the end point of X - axis | R/W |
| Y2 | int | Specifies the end point of Y - axis | R/W |
| Enabled | bool | Specifies if the allow operator control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of line | R |
| LineColor | Color | Specifies the color of line | R/W |
| AlternateLineColor | Color | Specifies the alternative color of line | R/W |
| DashType | HmiDashType | Specifies the line type | R/W |
| EndType | HmiLineEndType | Specifies the line end | R/W |
| StartType | HmiLineStartType | Specifies the line start | R/W |
| CapType | HmiCapType | Specifies the cap type | R/W |
| LineWidth | byte | Specifies the width of line | R/W |
| Top | int | Specifies the Y position of line | R/W |
| Left | int | Specifies the X position of line | R/W |
| Width | uint | Specifies the width of line | R/W |
| Height | uint | Specifies the height of line | False |
| RotationAngle | short | Specifies the rotation of line | R/W |
| RotationCenterX | float | Specifies the X pivot of line | R/W |
| RotationCenterY | float | Specifies the Y pivot of line | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of line | R/W |
| Opacity | float | Specifies the opacity of line  The opacity of line should between 0 and 1 | R/W |
| Name | string | Specifies the name of line  The length of name character should between 1 - 128 | R/W |
| Visible | bool | Specifies the visibility of line | R/W |
| TabIndex | ushort | Specifies the tab index of line | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip of line | R/W |
| Authorization | string | Specifies the authorization of line | R/W |
| EventHandlers | HmiLineEventHandlerComposition | Specifies the event handler of line | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of line screen items modify the following code:

private void LineScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiLine hmiline = (HmiLine)screenitems.Find("Line_1");

//Name

var name = hmiline.Name;

hmiline.Name = "Default Value";

//AlternateLineColor

var linecolor = hmiline.AlternateLineColor;

hmiline.AlternateLineColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//Height

var height = hmiline.Height;

hmiline.Height = 100;

//ToolTipText

var tooltip = hmiline.ToolTipText;

var tooltiptext = hmiline.ToolTipText.Items[0].Text;

hmiline.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilinugualProperty&lt;/p&gt;&lt;/body&gt;";

//DashType

var dashtype = hmiline.DashType;

hmiline.DashType = HmiDashType.DashDotDot;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing polyline properties  (RT Unified)

###### Property

The following properties are supported in polyline screen item:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| LineColor | Color | Specifies the line color of polyline | R/W |
| Enabled | bool | Specifies if the allow operator control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of polyline | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of polyline | R/W |
| AlternateLineColor | Color | Specifies the alternate line color of polyline | R |
| DashType | HmiDashType | Specifies the line type of polyline | R |
| EndType | HmiLineEndType | Specifies the end type of polyline | R |
| StartType | HmiLineStartType | Specifies the line start of polyline | R |
| CapType | HmiCapType | Specifies the cap type of polyline | R |
| LineWidth | byte | Specifies the line width of polyline | R |
| JoinType | HmiLineJoinType | Specifies the join type in polyline | R |
| Top | int | Specifies the Y position of polyline | R |
| Left | int | Specifies the X position of polyline | R |
| Width | uint | Specifies the width of polyline | R |
| Height | uint | Specifies the height of polyline | R |
| RotationAngle | short | Specifies the rotation of polyline | R |
| RotationCenterX | float | Specifies the X pivot point of polyline | R |
| RotationCenterY | float | Specifies the Y pivot point of polyline | R |
| Opacity | float | Specifies the opacity of polyline  The value of Opacity should lies between 0 - 1 | R |
| Name | string | Specifies the name of polyline  The length of the name character should lies betweenn 1 - 128 characters | R |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of polyline | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of polyline | R/W |
| Authorization | string | Specifies the authorization of polyline | R/W |
| EventHandlers | HmiPolylineEventHandlerComposition | Specifies the event handle of polyline | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of polyline screen items modify the following program code :

private void PolylineScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiPolyline polyline = (HmiPolyline)screenitems.Find("Default Value123");

//Name

var name = polyline.Name;

polyline.Name = "Default Value123";

//AlternateLineColor

var linecolor = polyline.AlternateLineColor;

polyline.AlternateLineColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//Height

var height = polyline.Height;

polyline.Height = 100;

//ToolTipText

var tooltip = polyline.ToolTipText;

var tooltiptext = polyline.ToolTipText.Items[0].Text;

polyline.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//Joint Type

var dashtype = polyline.JoinType;

polyline.JoinType = HmiLineJoinType.Miter;

//Points

var points = polyline.Points;

var point = points[0];

var x = point.X;

point.X = 10;

var y = point.Y;

point.Y = 10;

var newPoint = points.Create(15, 100);

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing polygon properties (RT Unified)

###### Property

The following properties are supported in polygon screen items:

| Property name | Property type | Description | Access |
| --- | --- | --- | --- |
| BorderColor | Color | Specifies the border color of polygon | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of polygon | R/W |
| BackColor | Color | Specifies the background color of polygon | R/W |
| AlternateBackColor | Color | Specifies the alternative background color of polygon | R/W |
| Points | HmiPointComposition | Specifies the point of polygon | R |
| BorderWidth | byte | Specifies the border width of polygon | R/W |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of polygon | R/W |
| FillLevel | byte | Specifies the fill level of polygon | R/W |
| FillDirection | HmiFillDirection | Specifies the fill direction of polygon | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of polygon | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of polygon | R/W |
| DashType | HmiDashType | Specifies the line type of polygon | R/W |
| ShowFillLevel | bool | Specifies the fill level of polygon | R/W |
| JoinType | HmiLineJoinType | Specifies the join type in polygon | R/W |
| Top | int | Specifies the Y position of polygon | R/W |
| Left | int | Specifies the X position of polygon | R/W |
| Width | uint | Specifies the width of polygon | R/W |
| Height | uint | Specifies the height of polygon | R/W |
| RotationAngle | short | Specifies the rotation of polygon | R/W |
| RotationCenterX | float | Specifies the X pivot point of polygon | R/W |
| RotationCenterY | float | Specifies the Y pivot point of polygon | R/W |
| Opacity | float | Specifies the opacity of polylgon  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of polygon  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of polygon | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of polygon | R/W |
| Authorization | string | Specifies the authorization of polygon | R/W |
| EventHandlers | HmiPolylgonEventHandlerComposition | Specifies the event handle of polygon | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of polygon screen items modify the following program code :

private void PolygonScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiPolygon polygon = (HmiPolygon)screenitems.Find("Default Value563");

//Name

var name = polygon.Name;

polygon.Name = "Default Value563";

//AlternateBorderColor

var linecolor = polygon.AlternateBorderColor;

polygon.AlternateBorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//Height

var height = polygon.Height;

polygon.Height = 100;

//ToolTipText

var tooltip = polygon.ToolTipText;

var tooltiptext = polygon.ToolTipText.Items[0].Text;

polygon.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//BackFillPattern

var backfill = polygon.BackFillPattern;

polygon.BackFillPattern = HmiFillPattern.GradientBackwardDiagnol;

//Points

var points = polygon.Points;

var point = points[0];

var x = point.X;

point.X = 10;

var y = point.Y;

point.Y = 10;

var newPoint = points.Create(15, 100);

}

clipboard

---

**See also**

[Screens.Create() (RT Unified)](#screenscreate-rt-unified)

###### Accessing rectangle properties (RT Unified)

###### Property

The following properties are supported in rectangle screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| BorderColor | Color | Specifies the border color of rectangle | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of rectangle | R/W |
| BackColor | Color | Specifies the background color of rectangle | R/W |
| AlternateBackColor | Color | Specifies the alternative background color of rectangle | R/W |
| BorderWidth | byte | Specifies the border width of rectangle | R/W |
| BackFillPattern | HmiFillPattern | Specifies the background fill pattern of rectangle | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | False |
| CurrentQuality | HmiQuality | Specifies the connection status of rectangle | True |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot point of rectangle | False |
| Corners | HmiCornersPart | Specifies the corner of rectangle | True |
| FillLevel | byte | Specifies the fill level of rectangle | False |
| FillDirection | HmiFillDirection | Specifies the fill direction of rectangle | False |
| DashType | HmiDashType | Specifies the line type of rectangle | False |
| ShowFillLevel | bool | Specifies the show level of rectangle | False |
| Top | int | Specifies the Y position of rectangle | False |
| Left | int | Specifies the X position of rectangle | False |
| Width | uint | Specifies the width of rectangle | False |
| Height | uint | Specifies the height of rectangle | False |
| RotationAngle | short | Specifies the rotation angle of rectangle | False |
| RotationCenterX | float | Specifies the X pivot point of rectangle | False |
| RotationCenterY | float | Specifies the Y pivot point of rectangle | False |
| Opacity | float | Specifies the opacity of rectangle  The value of Opacity should lie between 0 - 1 | False |
| Name | string | Specifies the name of rectangle  The length of the name character should lie betweenn 1 - 128 characters | False |
| Visible | bool | Specifies if the visible is enabled or not | False |
| TabIndex | ushort | Specifies the tab index of rectangle | False |
| ToolTipText | MultilingualText | Specifies the tool tip text of rectangle | False |
| Authorization | string | Specifies the authorization of rectangle | False |
| EventHandlers | HmiRectangleEventHandlerComposition | Specifies the event handle of rectangle | True |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | False |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of rectangle screen items modify the following program code:

private void RectangleSccreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiRectangle rectangle = screenitems.Create&lt;HmiRectangle&gt;("Default Value3587");

//Name

var name = rectangle.Name;

rectangle.Name = "Default Value57";

//BorderColor

var bordercolor = rectangle.BorderColor;

rectangle.BorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = rectangle.BorderWidth;

rectangle.BorderWidth = 10;

//ToolTipText

var tooltip = rectangle.ToolTipText;

var tooltiptext = rectangle.ToolTipText.Items[0].Text;

rectangle.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//Corners

var corner = rectangle.Corners;

var bottomleftradius = corner.BottomLeftRadius;

corner.BottomLeftRadius = 50;

var bottomrightradius = corner.BottomRightRadius;

corner.BottomRightRadius = 30;

var topleftradius = corner.TopLeftRadius;

corner.TopLeftRadius = 50;

var toprightradius = corner.TopRightRadius;

corner.TopRightRadius = 30;

}

clipboard

---

**See also**

[ScreenItems.Create() (RT Unified)](#screenitemscreate-rt-unified)

###### Accessing textbox properties  (RT Unified)

###### Property

The following properties are supported in textbox screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| ReadOnly | bool | Specifies the read only access of textbox | R/W |
| TextWrapping | HmiTextWrapping | Specifies the text wrap of textbox | R/W |
| VerticalTextAlignment | HmiVerticalAlignment | Specifies the vertical text alignment of textbox | R/W |
| HorizontalTextAlignment | HmiHorizontalAlignment | Specifies the horizontal text alignment of textbox | R/W |
| TextTrimming | HmiTextTrimming | Specifies the text trimming of textbox | R/W |
| ForeColor | Color | Specifies the foreground color of textbox | R/W |
| BorderColor | Color | Specifies the border color of textbox | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of textbox | R/W |
| Authorization | string | Specifies the authorization of textbox | R/W |
| BackColor | Color | Specifies the background color of textbox | R/W |
| BorderWidth | byte | Specifies the border width of textbox | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of textbox | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font of textbox | R/W |
| Height | uint | Specifies the height of textbox | R/W |
| Top | int | Specifies the X- position of textbox | R/W |
| Left | int | Specifies the Y- position of textbox | R/W |
| Name | string | Specifies the name of textbox | R/W |
| RotationAngle | short | Specifies the connection status of textbox | R/W |
| VisualizeQuality | bool | Specifies if the allow operation control is enabled or not | R/W |
| AlternateBackColor | Color | Specifies the alternate background color of textbox | R/W |
| RotationCenterX | float | Specifies the X pivot point of textbox | R/W |
| RotationCenterY | float | Specifies the Y pivot point of textbox | R/W |
| Opacity | float | Specifies the opacity of textbox  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the rotation angle of textbox | R/W |
| Visible | bool | Specifies the visibilty of textbox | R/W |
| Width | uint | Specifies the width of textbox | R/W |
| TabIndex | ushort | Specifies the tab index of textbox | R/W |
| ToolTipText | string | Specifies the tool tip text of textbox | R/W |
| EventHandlers | HmiTextBoxEventHandler Composition | Specifies the event handle of textbox | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Text | MultilingualText | Specifies the text of textbox | R/W |
| Padding | HmiPaddingPart | Specifies the padding of textbox | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of textbox modify the following program code:

private void TextboxPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiTextBox textbox = screenitems.Create&lt;HmiTextBox&gt;("Default Value334554");

// To access basic property of textbox

//Name

var name = textbox.Name;

texttbox.Name = "Default Value";

//BorderColor

var bordercolor = textbox.BorderColor;

textbox.BorderColor = Color.FromArgb(0xCC, 0xF0, 0x80, 0x80);

//BorderWidth

var borderwidth = textbox.BorderWidth;

textbox.BorderWidth = 10;

// To access multilingualproperty

//ToolTipText

var tooltip = textbox.ToolTipText;

var tooltiptext = textbox.ToolTipText.Items[0].Text;

textbox.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//To access other typical property of textbox

//Font

var font = textbox.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.FontName;

font.FontName = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var.underline = font.Underline;

font.Underline = false;

font.Bold = true;

}

clipboard

##### Elements (RT Unified)

This section contains information on the following topics:

- [Accessing bar properties (RT Unified)](#accessing-bar-properties-rt-unified)
- [Accessing button properties (RT Unified)](#accessing-button-properties-rt-unified)
- [Accessing check box properties (RT Unified)](#accessing-check-box-properties-rt-unified)
- [Accessing clock properties (RT Unified)](#accessing-clock-properties-rt-unified)
- [Accessing gauge properties (RT Unified)](#accessing-gauge-properties-rt-unified)
- [Accessing IO Field properties (RT Unified)](#accessing-io-field-properties-rt-unified)
- [Accessing listbox properties (RT Unified)](#accessing-listbox-properties-rt-unified)
- [Accessing radio button properties (RT Unified)](#accessing-radio-button-properties-rt-unified)
- [Accessing slider properties (RT Unified)](#accessing-slider-properties-rt-unified)
- [Accessing switch properties (RT Unified)](#accessing-switch-properties-rt-unified)
- [Accessing symbolic IOField properties (RT Unified)](#accessing-symbolic-iofield-properties-rt-unified)
- [Accessing touch area properties (RT Unified)](#accessing-touch-area-properties-rt-unified)

###### Accessing bar properties (RT Unified)

###### Property

The following properties are supported in bar screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| AlternateBackColor | Color | Specifies the alternate background color of bar | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of bar | R/W |
| Authorization | string | Specifies the authorization of bar | R |
| BackgColor | Color | Specifies the background color of bar | R/W |
| BorderColor | Color | Specifies the border color of bar | R/W |
| BarMode | HmiBarMode |  | R/W |
| BorderWidth | byte | Specifies the border width of bar | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of bar | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font type of bar | R/W |
| Label | HmiTextPart | Specifies the label of bar | R/W |
| Height | uint | Specifies the height of bar | R/W |
| StraightScale | HmiStraightScalePart | Specifies the linear scale of bar | R/W |
| Top | int | Specifies the X position of bar | R/W |
| Left | int | Specifies the Y position of bar | R/W |
| Name | string | Specifies the name of bar  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| NormalRangeColor | Color | Specifies the normal range color of bar | R/W |
| OriginValue | double | Specifies the origin value of bar | R/W |
| OutputFormat | string | Specifies the output format of bar  The value of ouput format should lie between 1 - 128 | R/W |
| PeakIndicators | HmiPeakIndicator | Specifies the peak indicator of bar | R/W |
| Process Value | string | Specifies the process value of bar | R/W |
| ProcessValueIndicatorBackColor | Color | Specifies the background color process value indicator of bar | R/W |
| ProcessValueIndicatorForeColor | Color | Specifies the foreground color process value indicator of bar | R/W |
| ProcessValueIndicatorMode | HmiProcessIndicatorMode | Specifies the mode of process value indicator of bar | R/W |
| RelativeToOrigin | bool | Specifies the percentage calculation of orgin value of bar | R/W |
| RotationAngle | short | Specifies the rotation angle of bar | R/W |
| VisualizeQuality | bool | Specifies the connection quality of bar | R/W |
| RotationCenterX | float | Specifies the X pivot point of bar | R/W |
| RotationCenterY | float | Specifies the Y pivot point of bar | R/W |
| Opacity | float | Specifies the opacity of bar  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of bar | R/W |
| ScaleBackColor | uint16 | Specifies the scale background color of bar | R/W |
| ScaleForeColor | Color | Specifies the scale foreground color of bar | R/W |
| ShowTrendIndicator | bool | Specifies the show trend indicator of bar | R/W |
| Visible | bool | Specifies the visiblity of bar | R/W |
| Width | uint | Specifies the width of bar | R/W |
| TabIndex | ushort | Specifies the tab index of bar | R/W |
| TrendIndicateColor | Color | Specifies the trend indicator color of bar | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of bar | R/W |
| EventHandlers | HmiBarEventHandlerComposition | Specifies the event handler of bar | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Title | HmiTextPart | Specifies the title of bar | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of bar screen items modify the following program code:

private void BarScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiBar bar = screenitems.Create&lt;HmiBar&gt;("Default Value334554");

//Name

var name = bar.Name;

bar.Name = "Default Value";

//RotationCenterPlacement

var rotation = bar.RotationCenterPlacement;

bar.RotationCenterPlacement = HmiRotationCenterPlacement.AbsoluteToContainer;

//Width

var width = bar.Width;

bar.Width = 100;

//ToolTipText

var tooltip = bar.ToolTipText;

var tooltiptext = bar.ToolTipText.Items[0].Text;

bar.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//Font

var title = bar.Title;

title.Visible = false;

title.ForeColor = Color.Black;

var font = title.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

}

clipboard

###### Accessing button properties (RT Unified)

###### Property

The following properties are supported in button screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternateBackgroundColor | Color | Specifies the alternate background color of button | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of button | R/W |
| BackgroundColor | Color | Specifies the background color of button | R/W |
| BorderColor | Color | Specifies the border color of button | R/W |
| BorderWidth | byte | Specifies the border width of button | R/W |
| Contents | HmiContentPart | Specifies the content of button | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of button | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font of button | R/W |
| ForegroundColor | Color | Specifies the foreground color of button | R/W |
| Graphic | string | Specifies the graphic of button  The value of graphic should lie between 1 - 128 | R/W |
| Height | uint | Specifies the height of button | R/W |
| Top | int | Specifies the Y position of button | R/W |
| Left | int | Specifies the X position of button | R/W |
| Rotation | short | Specifies the rotation of button | R/W |
| VisualizeQuality | bool | Specifies the visualize quality of button | R/W |
| RotationCenterX | float | Specifies the X pivot point of button | R/W |
| RotationCenterY | float | Specifies the Y pivot point of button | R/W |
| Style Item Appearance | HmiStyleItem Appearance | Specifies the style of button | R/W |
| Opacity | float | Specifies the opacity of button  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of button  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Padding | HmiPaddingPart | Specifies the padding of button | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of button | R/W |
| TabIndex | ushort | Specifies the tab index of button | R/W |
| Text | MultiLingualText | Specifies the text of button | R |
| ToolTipText | MultilingualText | Specifies the tool tip text of button | R |
| Visible | bool | Specifies the visiblity of button | R/W |
| Width | uint | Specifies the width of button | R/W |
| EventHandlers | buttonEventHandlerComposition | Specifies the event handler of button | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| AlternateGraphic | string | Specifies the graphic with pressed button   The value of Alternate Graphic should lie between 1 - 128 | R/W |
| AlternateText | MultiLingualText | Specifiies the text with pressed button | False |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of button screen items modify the following program code:

private void ButtonScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiButton button = screenitems.Create&lt;HmiButton&gt;("Default Value354");

//Name

var name = button.Name;

button.Name = "Default Value";

//AlternateBackColor

var altbackcolor = button.AlternateBackColor;

button.AlternateBackColor = Color.Beige;

//Height

var height = button.Height;

button.Height = 100;

//ToolTipText

string culture = "en-US";

Language lang = Tiaproject.LanguageSettings.Languages.Find(new CultureInfo(culture));

MultilingualText mltprop = button.ToolTipText;

MultilingualTextItemComposition textItemComp = mltprop.Items;

MultilingualTextItem mlttextitem = textItemComp.Find(lang);

mlttextitem.Text = &lt;body&gt;&lt;p&gt;"TestforMultilingualProperty"&lt;/p&gt;&lt;/body&gt;;

//Padding

var padding = button.Padding;

var bottom = padding.Bottom;

padding.Bottom = 50;

padding.Left = 60;

padding.Right = 70;

padding.Top = 50;

}

clipboard

###### Accessing check box properties (RT Unified)

###### Property

The following properties are supported in checkbox screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| AlternateBackgroundColor | Color | Specifies the alternate background color of checkbox | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of checkbox | R/W |
| Authorization | string | Specifies the authorization of checkbox | R/W |
| BackgroundColor | Color | Specifies the background color of checkbox | R/W |
| BorderColor | Color | Specifies the border color of checkbox | R |
| BorderWidth | byte | Specifies the border width of checkbox | R/W |
| Content | HmiContentPart | Specifies the content of checkbox | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of checkbox | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font of checkbox | R |
| ForegroundColor | Color | Specifies the foreground color of checkbox | R/W |
| Height | uint | Specifies the height of checkbox | R/W |
| Top | int | Specifies the Y position of checkbox | R/W |
| Left | int | Specifies the X position of checkbox | R/W |
| Name | string | Specifies the name of checkbox  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Rotation | short | Specifies the rotation of checkbox | R/W |
| VisualizeQuality | bool | Specifies the connection quality of checkbox | R/W |
| RotationCenterX | float | Specifies the X pivot point of checkbox | R/W |
| RotationCenterY | float | Specifies the Y pivot point of checkbox | R/W |
| Opacity | float | Specifies the opacity of checkbox  The value of Opacity should lie between 0 - 1 | R/W |
| Process value | string | Specifies the process value of checkbox | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of checkbox | R/W |
| SelectionItemHeight | uint16 | Specifies the selected height of checkbox | R/W |
| SelectionItems | HmiSelectionItemPartComposition | Specifies the selected items of checkbox | R |
| TabIndex | ushort | Specifies the tab index of checkbox | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of checkbox | R |
| Visible | bool | Specifies the visiblity of checkbox | R/W |
| Width | uint | Specifies the width of checkbox | R/W |
| EventHandlers | HmiCheckBoxGroupEventHandler Composition | Specifies the event handler of checkbox | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Padding | HmiPaddingPart | Specifies the padding of checkbox | R/W |
| SelectionPosition | HmiHorizontalAlignment | Specifies the selection position of checkbox | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of checkbox screen items modify the following program code :

private void CheckboxScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiCheckbox chkbox = screenitems.Create&lt;HmiCheckbox&gt;("Default Value1354");

//Name

var name = chkbox.Name;

chkbox.Name = "DefaultName";

//AlternateBackColor

var altbackcolor = chkbox.AlternateBackColor;

chkbox.AlternateBackColor = Color.Beige;

//Height

var height = chkbox.Height;

chkbox.Height = 100;

//ToolTipText

var tooltip = chkbox.ToolTipText;

var tooltiptext = chkbox.ToolTipText.Items[0].Text;

chkbox.ToolTipText.Items[0].Text = "TestforMultilingualProperty";

//Font

var font = chkbox.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

}

clipboard

###### Accessing clock properties (RT Unified)

###### Property

The following properties are supported in clock screen item:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternativeBackgroundColor | Color | Specifies the alternative background color of clock | R/W |
| AlternativeBorderColor | Color | Specifies the alternative border color of clcok | R/W |
| BorderColor | Color | Specifies the border color of clock | R/W |
| Authorization | string | Specifies the authorization of clock | R |
| BackgroundColor | Color | Specifies the background color of clock | R/W |
| BorderWidth | byte | Specifies the border width of clock | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of clock | True |
| DialBackColor | Color | Specifies the dial background color of clock | False |
| DialLabelColor | Color | Specifies the dial label color of clock | False |
| DialMode | HmiScaleMode | Specifies the dial mode of clock | False |
| DialTickColor | Color | Specifies the dial tick color of clock | False |
| Enabled | bool | Specifies if the allow operation control is enabled or not | False |
| Height | uint | Specifies the height of clock | False |
| Top | int | Specifies the Y- position of clock | False |
| Left | int | Specifies the X-position of clock | False |
| Name | string | Specifies the name of clock | False |
| VisualizeQuality | bool | Specifies the visual quality of clock | False |
| RotationCenterX | float | Specifies the X pivot point of clock | False |
| RotationCenterY | float | Specifies the Y pivot point of clock | False |
| ShowHours | bool | Specifies if the show hours is enabled or not | False |
| ShowMinutes | bool | Specifies if the show minutes is enabled or not | False |
| ShowSeconds | bool | Specifies if the show seconds is enabled or not | False |
| Opacity | float | Specifies the opacity of clock  The value of Opacity should lie between 0 - 1 | False |
| TimeSource | string | Specifies the time source of clock | R/W |
| Rotation | short | Specifies the rotation angle of clock | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of clock | R/W |
| Visiblility | bool | Specifies the visibility of clock | R/W |
| Width | uint | Specifies the width of clock | R/W |
| TabIndex | ushort | Specifies the tab index of clock | R/W |
| Title | HmiTextPart | Specifies the title of clock | R |
| ToolTipText | MultiLingualText | Specifies the tool tip text of clock | R/W |
| EventHandlers | HmiClockEventHandlerComposition | Specifies the event handle of clock | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| DialLabelFont | HmiFontPart | Specifies the dial label font of clock | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of clock modify the following program code :

private void ClockPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiClock clock = screenitems.Create&lt;HmiClock&gt;("Default Value334554");

// To access basic properties of clock

//Name

var name = clock.Name;

clock.Name = "Default Value";

//AlternateBackColor

var altbackcolor = clock.AlternateBackColor;

clock.AlternateBackColor = Color.Beige;

//Height

var height = clock.Height;

clock.Height = 100;

// To access multilingual property of clock

//ToolTipText

var tooltip = clock.ToolTipText;

var tooltiptext = clock.ToolTipText.Items[0].Text;

clock.ToolTipText.Items[0].Text = &lt;body&gt;&lt;p&gt;"TestforMultilingualProperty"&lt;/p&gt;&lt;/body&gt;;

// To access other typical properties

//DialLabelFont

var dialfont = clock.DialLabelFont;

dialfont.Italic = false;

var fontname = dialfont.FontName;

dialfont.FontName = HmiFontName.SimSun;

var size = dialfont.Size;

dialfont.Size = 10.2f;

var stike = dialfont.StrikeOut;

dialfont.StrikeOut = true;

var underline = dialfont.Underline;

dialfont.Underline = false;

dialfont.Bold = true;

//ShowHours

var showhour = clock.ShowHours;

clock.ShowHours = false;

}

clipboard

###### Accessing gauge properties (RT Unified)

###### Property

The following properties are supported in gauge screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternateBackColor | Color | Specifies the alternate background color of gauge | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of gauge | R/W |
| Authorization | string | Specifies the authorization of gauge | R |
| BackgroundColor | Color | Specifies the background color of gauge | R/W |
| BorderColor | Color | Specifies the border color of gauge | R/W |
| BorderWidth | byte | Specifies the border width of gauge | R/W |
| RelativeToOrigin | bool | Specifies if relative origin value of gauge is shown ot not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of gauge | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Title | HmiTextPart | Specifies the title of gauge | R |
| Font | HmiFontPart | Specifies the font type of gauge | R/W |
| Label | HmiTextPart | Specifies the label of gauge | R |
| Height | uint | Specifies the height of gauge | R/W |
| Top | int | Specifies the X position of gauge | R/W |
| Left | int | Specifies the Y position of gauge | R/W |
| Name | string | Specifies the name of gauge  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| NormalRangeColor | Color | Specifies the normal range color of gauge | R/W |
| OriginValue | double | Specifies the origin value of gauge | R/W |
| OutputFormat | string | Specifies the output format of gauge  The value of ouput format should lie between 1 - 128 | R/W |
| PeakIndicators | HmiPeakIndicator | Specifies the peak indicator of gauge | R/W |
| ProcessValue | string | Specifies the process value of gauge | R/W |
| ProcessValueIndicatorBackColor | Color | Specifies the background color of process value indicator | R/W |
| ProcessValueIndicatorForeColor | Color | Specifies the foreground color of process value indicator | R/W |
| ProcessValueIndicatorMode | HmiProcessIndicatorMode | Specifies the mode value of process value indicator | R/W |
| Rotation | short | Specifies the rotation angle of gauge | R/W |
| VisualizeQuality | bool | Specifies the connection quality of gauge | R/W |
| RotationCenterX | float | Specifies the X pivot point of gauge | R/W |
| RotationCenterY | float | Specifies the Y pivot point of gauge | R/W |
| Opacity | float | Specifies the opacity of gauge  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of gauge | R/W |
| ScaleBackgroundColor | Color | Specifies the scale background color of gauge | R/W |
| ScaleForegroundColor | Color | Specifies the scale foreground color of gauge | R/W |
| TrendIndicatorColor | Color | Specifies the show trend indicator of gauge | R/W |
| Visible | bool | Specifies the visiblity of gauge | R/W |
| Width | uint | Specifies the width of gauge | R/W |
| TabIndex | ushort | Specifies the tab index of gauge | R/W |
| ShowTrendIndicator | bool | Specifies if the trend indicator of a gauge will be shown | R/W |
| ToolTipText | string | Specifies the tool tip text of gauge | R/W |
| EventHandlers | HmiGaugeEventHandlerComposition | Specifies the event handler of gauge | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| CurvedScale | HmiCurvedScalePart | Specifies the scale of gauge | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of gauge modify the following program code :

private void GaugeScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiGauge gauge = screenitems.Create&lt;HmiGauge&gt;("Default Value334554");

//Name

var name = gauge.Name;

gauge.Name = "Default Value";

//RotationalCenterPlacement

var rotation = gauge.RotationCenterPlacement;

gauge.RotationCenterPlacement = HmiRotationCenterPlacement.AbsoluteToContainer;

//Width

var width = gauge.Width;

gauge.Width = 100;

//ToolTipText

var tooltip = gauge.ToolTipText;

var tooltiptext = gauge.ToolTipText.Items[0].Text;

gauge.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//Font

var title = gauge.Title;

title.Text.items[0].Text = "&lt;body&gt;&lt;p&gt;teststing&lt;/p&gt;&lt;/body&gt;";

title.Visible = false;

title.ForeColor = Color.Black;

var font = title.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

}

clipboard

###### Accessing IO Field properties (RT Unified)

###### Property

The following properties are supported in IO Field properties screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| AlternateBackColor | Color | Specifies the alternate background color of IO field | R/W |
| Enabled | Bool | Specifies if the allow operation control is enabled or not | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of IO field | R/W |
| Authorization | String | Specifies the authorization of IO field | R |
| BackColor | Color | Specifies the background color of IO field | R/W |
| BorderColor | Color | Specifies the border color of IO field | R/W |
| BorderWidth | byte | Specifies the border width of IO field | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of IO field | R |
| Font | HmiFontPart | Specifies the font of IO field | R/W |
| ForegroundColor | Color | Specifies the foreground color of IO field | R/W |
| Height | uint | Specifies the height of IO field | R/W |
| HorizontalTextAlignment | HmiHorizontalAlignment | Specifies the horizontal alignment of IO Field | R/W |
| IOFieldType | HmiIOFieldType | Specifies the mode of IO field | R/W |
| Top | int | Specifies the Y position of IO field | R/W |
| Left | int | Specifies the X position of IO field | R/W |
| Rotation Angle | short | Specifies the rotation of IO field | R/W |
| VisualizeQuality | bool | Specifies the visualizing quality of IO field | R/W |
| TextTrimming | HmiTextTrimming | Specifies the text to be trimmed of IO field | R/W |
| RotationCenterX | float | Specifies the X pivot point of IO field | R/W |
| RotationCenterY | float | Specifies the Y pivot point of IO field | R/W |
| Opacity | float | Specifies the opacity of IO field  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of IO field  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| OutputFormat | string | Specifies the output format of IO field | R/W |
| Padding | HmiPaddingPart | Specifies the padding of IO field | R |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of IO field | R/W |
| ProcessValue | string | Specifies the process value of IO field | R/W |
| TabIndex | ushort | Specifies the tab index of IO field | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of IO field | R/W |
| VerticalTextAlignment | HmiVerticalAlignment | Specifies the vertical alignment of IO field | R/W |
| Visible | bool | Specifies the visiblity of IO field | R/W |
| Width | uint | Specifies the width of IO field | R/W |
| EventHandlers | HmiIOFieldEventHandle rComposition | Specifies the event handler of IO field | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| InputBehavior | HmiInputBehaviorPart | Specifies the reaction to input of IO field | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of IO Field screen items modify the following program code:

private void IOFieldScreenItemsPropertiesAccess(Project project)

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiIOField iofield = screenitems.Create&lt;HmiIOField&gt;("Default Value354");

//Name

var name = iofield.Name;

iofield.Name = "DefaultName";

//AlternateBackColor

var altbackcolor = iofield.AlternateBackColor;

iofield.AlternateBackColor = Color.Beige;

//Height

var height = iofield.Height;

iofield.Height = 100;

//ToolTipText

string culture = "en-US";

Language lang = project.LanguageSettings.Languages.Find(new CultureInfo(culture));

MultilingualText mltprop = ioField.ToolTipText;

MultilingualTextItemComposition textItemComp = mltprop.Items;

MultilingualTextItem mlttextitem = textItemComp.Find(lang);

mlttextitem.Text = "CommentInEnglish";

//Padding

var padding = iofield.Padding;

var bottom = padding.Bottom;

padding.Bottom = 50;

padding.Left = 60;

padding.Right = 70;

padding.Top = 50;

}

clipboard

###### Accessing listbox properties (RT Unified)

###### Property

The following properties are supported in listbox screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternateBackgroundColor | Color | Specifies the alternative background color of listbox | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of listbox | R/W |
| Authorization | string | Specifies the authorization of listbox | R |
| BackgroundColor | Color | Specifies the background color of listbox | R/W |
| BorderColor | Color | Specifies the border color of listbox | R/W |
| BorderWidth | byte | Specifies the border width of listbox | R/W |
| Content | HmiContentPart | Specifies the content of listbox | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of listbox | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font part of listbox | R/W |
| ForeGroundColor | Color | Specifies the foreground color of listbox | R/W |
| Top | int | Specifies the X position of listbox | R/W |
| Left | int | Specifies the Y position of listbox | R/W |
| Name | string | Specifies the name of listbox  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Process Value | string | Specifies the process value of listbox | R/W |
| Rotation | short | Specifies the rotation angle of listbox | R/W |
| VisualizeQuality | bool | Specifies the connection status of listbox | R/W |
| RotationCenterX | float | Specifies the X pivot point of listbox | R/W |
| RotationCenterY | float | Specifies the Y pivot point of listbox | R/W |
| SelectionItemHeight | uint16 | Specifies the selected item height of listbox | R/W |
| SelectionItems | IList&lt;IHmiSelectionItemPart&gt; | Specifies the selected items of listbox | R |
| SelectionMode | HmiSelectionMode | Specifies the selected mode of listbox | R/W |
| SelectorPosition | HmiHorizontalAlignment | Specifies the selected position of listbox | R/W |
| Opacity | float | Specifies the opacity of listbox  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of listbox | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Width | uint | Specifies the width of listbox | R/W |
| TabIndex | ushort | Specifies the tab index of listbox | R/W |
| ToolTipText | string | Specifies the tool tip text of listbox | R/W |
| EventHandlers | HmiListBoxEventHandler Composition | Specifies the event handle of listbox | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Padding | HmiPaddingPart | Specifies the padding of listbox | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of list box modify the following program code:

private void ListBoxPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiListBox listbox = screenitems.Create&lt;HmiListBox&gt;("Default Value334554");

//Name

var name = listbox.Name;

listbox.Name = "Default Value";

//AlternateBackColor

var altbackcolor = listbox.AlternateBackColor;

listbox.AlternateBackColor = Color.Beige;

//Height

var height = listbox.Height;

listbox.Height = 100;

// To access multilingual property

var tooltip = listbox.ToolTipText;

var tooltiptext = listbox.ToolTipText.Items[0].Text;

// To access other typical property of listbox

//Font

var font = listbox.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

//Selection Items

var selectionItem = listbox.SelectionItems;

var newselectionitem = selectionItem.Create();

var graphic = newselectionitem.Graphic;

newselectionitem.Graphic = "abcd";

newselectionitem.IsSelected = false;

}

clipboard

###### Accessing radio button properties (RT Unified)

###### Property

The following properties are supported in radio button screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternateBackgroundColor | Color | Specifies the alternative background color of radio button | R/W |
| AlternateBorderColor | Color | Specifies the alternative border color of radio button | R/W |
| Authorization | string | Specifies the authorization of radio button | R |
| BackgroundColor | Color | Specifies the background color of radio button | R/W |
| BorderColor | Color | Specifies the border color of radio button | R/W |
| BorderWidth | byte | Specifies the border width of radio button | R/W |
| Content | HmiContentPart | Specifies the content of radio button | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of radio button | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font of radio button | False |
| ForegroundColor | Color | Specifies the foreground color of radio button | R/W |
| Height | uint | Specifies the height of radio button | R/W |
| Top | int | Specifies the X position of radio button | R/W |
| Left | int | Specifies the Y position of radio button | R/W |
| Name | string | Specifies the name of radio button  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Process Value | string | Specifies the process value of radio button | R/W |
| Rotation | short | Specifies the rotation angle of radio button | R/W |
| VisualizeQuality | bool | Specifies the connection status of radio button | R/W |
| RotationCenterX | float | Specifies the X pivot point of radio button | R/W |
| RotationCenterY | float | Specifies the Y pivot point of radio button | R/W |
| SelectionItemHeight | uint16 | Specifies the selection item height of radio button | R/W |
| SelectionItems | IList&lt;IHmiSelectionItemPart&gt; | Specifies the selection items of radio button | R |
| SelectorPosition | HmiHorizontalAlignment | Specifies the selector position of radio button | R |
| Opacity | float | Specifies the opacity of radio button  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of radio button | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Width | uint | Specifies the width of radio button | R/W |
| TabIndex | ushort | Specifies the tab index of radio button | R/W |
| ToolTipText | string | Specifies the tool tip text of radio button | R/W |
| EventHandlers | HmiRadioradio buttonGroup EventHandlerComposition | Specifies the event handle of radio button | R |
| Padding | HmiPaddingPart | Specifies the padding of radio button | R |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of radio button modify the following program code:

private void RadiobuttonPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiRadioButtonGroup radio = screenitems.Create&lt;HmiRadioButtonGroup&gt;("Default Value334554");

// To access basic properties

//Name

var name = radio.Name;

radio.Name = "Default Value";

//AlternateBackColor

var altbackcolor = radio.AlternateBackColor;

radio.AlternateBackColor = Color.Beige;

//Height

var height = radio.Height;

radio.Height = 100;

// To access multilingual property

//ToolTipText

var tooltip = radio.ToolTipText;

var tooltiptext = radio.ToolTipText.Items[0].Text;

//radio.ToolTipText.Items[0].Text = "TestforMultilingualProperty";

// To access other typical properties of radio button

//Font

var font = radio.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

//Selection Items

var selectionItem = radio.SelectionItems;

var newselectionitem = selectionItem.Create();

var graphic = newselectionitem.Graphic;

newselectionitem.Graphic = "abcd";

newselectionitem.IsSelected = false;

}

clipboard

###### Accessing slider properties (RT Unified)

###### Property

The following properties are supported in slider screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| AlternativeBackColor | Color | Specifies the alternative background color of slider | R/W |
| AlternativeBorderColor | Color | Specifies the alternative border color of slider | R/W |
| Authorization | string | Specifies the authorization of slider | R |
| BackgroundColor | Color | Specifies the background color of slider | R/W |
| BorderColor | Color | Specifies the border color of slider | R/W |
| BorderWidth | byte | Specifies the border width of slider | R/W |
| BarMode | HmiBarMode | Specifies the bar mode of slider | R/W |
| RelativeToOrigin | bool | Specifies the relative to origin value of slider | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of slider | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | False |
| Title | HmiTextPart | Specifies the title of slider | R |
| Font | HmiFontPart | Specifies the font type of slider | R/W |
| Label | HmiTextPart | Specifies the label of slider | R |
| Height | uint | Specifies the height of slider | R/W |
| Top | int | Specifies the X position of slider | R/W |
| Left | int | Specifies the Y position of slider | R/W |
| Name | string | Specifies the name of slider  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| NormalRangeColor | Color | Specifies the normal range color of slider | R/W |
| OriginValue | double | Specifies the origin value of slider | R/W |
| OutputFormat | string | Specifies the output format of slider  The value of ouput format should lie between 1 - 128 | R/W |
| PeakIndicators | HmiPeakIndicator | Specifies the peak indicator of slider | R/W |
| Process Value | string | Specifies the process value of slider | R/W |
| ProcessValueIndicatorBackColor | Color | Specifies the background color process value indicator of slider | R/W |
| ProcessValueIndicatorForeColor | Color | Specifies the foreground color process value indicator of slider | R/W |
| ProcessValueIndicatorMode | HmiProcessIndicatorMode | Specifies the mode of process value indicator of slider | R/W |
| Rotation | short | Specifies the rotation angle of slider | R/W |
| VisualizeQuality | bool | Specifies the connection quality of slider | R/W |
| RotationCenterX | float | Specifies the X pivot point of slider | R/W |
| RotationCenterY | float | Specifies the Y pivot point of slider | R/W |
| Opacity | float | Specifies the opacity of slider  The value of Opacity should lie between 0 - 1 | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of slider | R/W |
| ScaleBackgroundColor | Color | Specifies the scale background color of slider | R/W |
| ScaleForegroundColor | Color | Specifies the scale foreground color of slider | R/W |
| TrendIndicatorColor | bool | Specifies the show trend indicator of slider | R/W |
| Visible | bool | Specifies the visiblity of slider | R/W |
| Width | uint | Specifies the width of slider | R/W |
| ValuePosition | HmiSimplePosition | Specifies the value position of slider | R/W |
| WriteDuringChange(Write process value Immediatly) | bool | Specifies if the write process value is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of slider | R/W |
| ShowTrendIndicator | bool | Specifies the trend indicator color of slider | R/W |
| ToolTipText | string | Specifies the tool tip text of slider | R/W |
| ShowValue | bool | Specifies if the value of a slider will be shown | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| EventHandlers | HmiSliderEventHandlerComposition | Specifies the event handler of slider | R |
| ThumbBackColor | color | Specifies the thumb background color of slider | R/W |
| ThumbForeColor | color | Specifies the thumb foreground color of slider | R/W |
| StraightScale | HmiStraightScalePart | Specifies the straight scale of slider | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of slider modify the following program code :

private void SliderPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiSlider slider = screenitems.Create&lt;HmiSlider&gt;("Default Value334554");

// To access basic properties of slider

//Name

var name = slider.Name;

slider.Name = "Default Value";

//RotationalCenterPlacement

var rotation = slider.RotationCenterPlacement;

slider.RotationCenterPlacement = HmiRotationCenterPlacement.AbsoluteToContainer;

//Width

var width = slider.Width;

slider.Width = 100;

// To access multilingual property of slider

//ToolTipText

var tooltip = slider.ToolTipText;

var tooltiptext = slider.ToolTipText.Items[0].Text;

//slider.ToolTipText.Items[0].Text = "TestforMultilingualProperty";

// To access other typical properties of slider

//Font

var title = slider.Title;

//title.Text.Items[0].Text = "teststing";

title.Visible = false;

title.ForeColor = Color.Black;

var font = title.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

}

clipboard

###### Accessing switch properties (RT Unified)

###### Property

The following properties are supported in switch screen items:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| AlternateBackgroundColor | Color | Specifies the alternate background color of switch | R/W |
| AlternateBorderColor | Color | Specifies the alternate border color of switch | R/W |
| IsAlternateState | bool | Specifies the alternate state of switch | R/W |
| Authorization | string | Specifies the authorization of switch | R |
| BackgroundColor | Color | Specifies the background color of switch | R/W |
| BorderColor | Color | Specifies the border color of switch | R/W |
| BorderWidth | byte | Specifies the border width of switch | R/W |
| Contents | HmiContentPart | Specifies the content of switch | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of switch | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| Font | HmiFontPart | Specifies the font of switch | R/W |
| ForegroundColor | Color | Specifies the foreground color of switch | R/W |
| Height | uint | Specifies the height of switch | R/W |
| Top | int | Specifies the Y position of switch | R/W |
| Left | int | Specifies the X position of switch | R/W |
| Rotation | short | Specifies the rotation of switch | R/W |
| Text | MultiLingualText | Specifies the text of switch | R |
| VisualizeQuality | bool | Specifies the visualize quality of switch | R/W |
| RotationCenterX | float | Specifies the X pivot point of switch | R/W |
| RotationCenterY | float | Specifies the Y pivot point of switch | R/W |
| Opacity | float | Specifies the opacity of switch  The value of Opacity should lie between 0 - 1 | R/W |
| Name | string | Specifies the name of switch  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Padding | HmiPaddingPart | Specifies the padding of switch | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of switch | R/W |
| TabIndex | ushort | Specifies the tab index of switch | R/W |
| ToolTipText | MultilingualText | Specifies the tool tip text of switch | R/W |
| Visiblity | bool | Specifies the visiblity of switch | R/W |
| Width | uint | Specifies the width of switch | R/W |
| EventHandlers | HmiToggleswitchEventHandlerComposition | Specifies the event handler of switch | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| Graphic | string | Specifies the graphic of switch  The value of graphic should lie between 1 - 128 | R/W |
| AlternateGraphic | string | Specifies the graphic with pressed switch   The value of Alternate Graphic should lie between 1 - 128 | R/W |
| AlternateText | MultiLingualText | Specifiies the text with pressed switch | R |
| Padding | HmiPaddingPart | Specifiies the padding of switch | R |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of switch screen items modify the following program code:

private void switchScreenItemsPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.ScreenItems;

HmiToggleSwitch toggleswitch = screenitems.Create&lt;HmiToggleSwitch&gt;("Default Value354");

//Name

var name = toggleswitch.Name;

toggleswitch.Name = "Default Value";

//AlternateBackColor

var altbackcolor = toggleswitch.AlternateBackColor;

toggleswitch.AlternateBackColor = Color.Beige;

//Height

var height = toggleswitch.Height;

toggleswitch.Height = 100;

//ToolTipText

var tooltip = toggleswitch.ToolTipText;

var tooltiptext = toggleswitch.ToolTipText.Items[0].Text;

toggleswitch.ToolTipText.Items[0].Text = "TestforMultilingualProperty";

//Font

var font = toggleswitch.Font;

var italic = font.Italic;

font.Italic = false;

var fontname = font.Name;

font.Name = HmiFontName.SimSun;

var size = font.Size;

font.Size = 10.2f;

var stike = font.StrikeOut;

font.StrikeOut = true;

var underline = font.Underline;

font.Underline = false;

font.Weight = HmiFontWeight.Bold;

}

clipboard

###### Accessing symbolic IOField properties (RT Unified)

###### Property

The following properties are supported in HMI Symbolic IO Field:

| Property Name | Property Type | Description | Access |
| --- | --- | --- | --- |
| Authorization | string | Specifies the authorization of symbolic IO field | R/W |
| CurrentQuality | HmiQuality | Specifies the connection quality of symbolic IO field | R |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamizations of symbolic IO field | R |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| EventHandlers | HmiSymbolicIOFieldEventHandlerComposition | Specifies the event handle of symbolic IO field | R |
| Height | uint | Specifies the height of symbolic IO field | R |
| IOFieldType | HmiIOFieldType | Specifies the field type of symbolic IO field | R/W |
| ProcessValue | String | Specifies the process value of symbolic IO field | R/W |
| ResourceList | String | Specifies the textlist and graphic list for symbolic IO field | R/W |
| Selected Index | Int32 | Specifies the selected index of symbolic IO field | R |
| SelectionBackColor | Color | Specifies the selected background color of symbolic IO field | R/W |
| SelectionForeColor | Color | Specifies the selected foreground color of symbolic IO field | R/W |
| Text | MultilingualText | Specifies the text of symbolic IO field | R/W |
| Left | int | Specifies the X-axis position of symbolic IO field | R/W |
| Name | String | Specifies the name of symbolic IO field | R/W |
| Opacity | float | Specifies the opacity value of symbolic IO field | R/W |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handlers of symbolic IO field | R |
| RequireExplicitUnlock | bool | Specifies if the value of explicit unlock is shown or not | R/W |
| RotationAngle | short | Specifies the rotation angle of symbolic IO field | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of symbolic IO field | R/W |
| RotationCenterX | float | Specifies the X pivot point of symbolic IO field | R/W |
| RotationCenterY | float | Specifies the Y pivot point of symbolic IO field | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of checkbox | R/W |
| ToolTipText | MultilingualText | Specifies the text to be mentioned on tool tip | R |
| Top | int | Specifies the Y-position of symbolic IO field | R/W |
| Visible | bool | Specifies the visibility of symbolic IO field | R/W |
| VisualizeQuality | bool | Specifies the visual quality of symbolic IO field | R/W |
| Width | uint | Specifies the width of symbolic IO field | R/W |

###### Requirement

- The HMI Software Object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the basic properties of Symbolic IO Field modify the following program code

private void SymbolicIOFieldPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition screens　=　hmiSoftware.Screens;

HmiScreen hmiScreen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenItems = hmiScreen.ScreenItems

HmiSymbolicIOField objSymbField = screenItems.Create&lt;HmiSymbolicIOField&gt;("Screen_object_1");

//Left

objSymbField.Left = 1;

//ToolTipText

objSymbField.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

}

clipboard

###### Accessing touch area properties (RT Unified)

###### Property

The following properties are supported in HMI Touch Area:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Authorization | string | Specifies the authorization of hmi touch area | R/W |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamization of hmi touch area | R |
| Enabled | bool | Specifies if the allow operator control is enabled or not | R/W |
| EventHandlers | HmiTouchAreaEventHandlerComposition | Specifies the event handler of hmi touch area | R |
| Height | uint | Specifies the height of hmi touch area | R/W |
| BackColor | Color | Specifies the background color of hmi touch area | R/W |
| Left | int | Specifies the X position of hmi touch area | R/W |
| Name | string | Specifies the name of hmi touch area | R/W |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handler of hmi touch area | R |
| RequireExplicitUnlock | bool | Specifies if explicit unlock is required or not | R/W |
| TabIndex | ushort | Specifies the tab index of hmi touch area | R/W |
| Top | int | Specifies the Y position of hmi touch area | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Width | uint | Specifies the width of hmi touch area | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access basic properties of HMI Touch Area modify the following program code:

private void HMITouchAreaPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreenComposition screens = hmiSoftware.Screens;

HmiScreen screen = hmiSoftware.Screens.Find("Screen_1");

HmiScreenItemBaseComposition screenItems = hmiScreen.ScreenItems;

HmiTouchArea objTouchArea = screenItems.Create&lt;HmiTouchArea&gt;("Screen_object_1");

//Left

objTouchArea.Left = 1;

//Backcolor

objTouchArea.Backcolor = Color.Red;

}

clipboard

##### Controls (RT Unified)

This section contains information on the following topics:

- [Accessing alarm control properties (RT Unified)](#accessing-alarm-control-properties-rt-unified)
- [Accessing function trend control properties (RT Unified)](#accessing-function-trend-control-properties-rt-unified)
- [Accessing media player properties (RT Unified)](#accessing-media-player-properties-rt-unified)
- [Accessing process control properties (RT Unified)](#accessing-process-control-properties-rt-unified)
- [Accessing parameter set control properties (RT Unified)](#accessing-parameter-set-control-properties-rt-unified)
- [Accessing screen window properties (RT Unified)](#accessing-screen-window-properties-rt-unified)
- [Accessing system diagnosis control properties (RT Unified)](#accessing-system-diagnosis-control-properties-rt-unified)
- [Accessing trend control properties (RT Unified)](#accessing-trend-control-properties-rt-unified)
- [Accessing trend companion properties (RT Unified)](#accessing-trend-companion-properties-rt-unified)
- [Accessing web control properties (RT Unified)](#accessing-web-control-properties-rt-unified)
- [Faceplate Container (RT Unified)](#faceplate-container-rt-unified)

###### Accessing alarm control properties (RT Unified)

###### roperty

The following properties are supported in alarm control screen items.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| UseAlarmColors | bool | Specifies the user alarm color of alarm control | R/W |
| Filter | string | Specifies the filter of alarm control | R/W |
| AlwaysShowRecent | bool | Specifies the show recent of alram control | R/W |
| AlarmSourceType | HmiAlarmSourceType | Specifies the alarm source of alarm control | R/W |
| Caption | HmiTextPart | Specifies the label to be displayed on alarm control | R |
| WindowFlags | HmiWindowFlag | Specifies the window setting of alarm control | R/W |
| Icon | string | Specifies the icon of alam control | R/W |
| Top | int | Specifies the Y Position of alarm control | R/W |
| Left | int | Specifies the X Position of alarm control | R/W |
| Width | uint | Specifies the width of alarm control | R/W |
| Height | uint | Specifies the height of alarm control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of alarm control | R |
| Name | string | Specifies the name of alarm control | R/W |
| Visible | bool | Specifies the visibility of alarm control | R/W |
| Enabled | bool | Specifies if the allow operator control | R/W |
| TabIndex | ushort | Specifies the tab index of alarm control | R/W |
| ToolBar | HmiToolBarPart | Specifies the toolbar of alarm control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar of alarm control | R |
| EditMode | HmiEditMode | Specifies the editing mode of alarm control | R/W |
| TimeZone | int | Specifies the time zone of alarm control | R/W |
| AlarmDefinitionViewSetup | HmiVisibleAlarms | Specifies the displayed alarms of alarm control | R/W |
| ActiveAlarmsViewSetup | HmiVisibleAlarms | Specifies the current alarms of alarm control | R/W |
| SuppressFlashing | bool | Specifies the suppress flashing of alarm control | R/W |
| AcknowledgmentFlashingRate | HmiFlashingRate | Specifies the flashing rate acknowledgement messages of alarm control | R/W |
| ResetFlashingRate | HmiFlashingRate | Specifies the reset flashing rate of alarm control | R/W |
| DefaultSortDirection | HmiSortDirection | Specifies the default sorting direction | R/W |
| BackColor | Color | Specifies the background color of alarm control | R/W |
| AlarmView | HmiDataGridViewPart | Specifies the alarm view of alarm control | TRUE |
| EventHandlers | HmiAlarmControlEventHandlerComposition | Specifies the event handlers of alarm control | R |
| CaptionColor | Color | Specifies the caption color of alarm control | R/W |
| AlarmStatisticsView | HmiDataGridViewPart | Specifies the alarm statistic view | R |
| ShowFocusVisual | Boolean | Specifies the show focus visual of alarm control | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of alarm control modify the following program code:

private void AccessAlarmControlProperties()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_1");

var hmialarmcontrol= Createdscreen.ScreenItems.Create&lt;HmiAlarmControl&gt;("HmiAlarmControl_1");

// Basic properties Access

// Width

var autoplay = hmialarmcontrol.Width;

hmialarmcontrol.Width = 100;

// BackColor

var backcolor = hmialarmcontrol.BackColor;

hmialarmcontrol.BackColor = Color.Beige;

// Name

var name = hmialarmcontrol.Name;

hmialarmcontrol.Name = "DefaultName";

// MultiLingual Property Access

// Access caption

var caption = hmialarmcontrol.Caption;

IHmiWindowFeature.Caption.Text.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/body&gt;&lt;/p&gt;";

// Access other typical properties

var statusBar = hmialarmcontrol.StatusBar;

var backColor = statusBar. BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar. Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing function trend control properties (RT Unified)

###### Property

The following properties are supported in function function trend control.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| ShowStatisticRulers | bool | Specifies the show statistic rulers of function trend control | R/W |
| AreaSpacing | ushort | Specifies the area space on function trend control | R/W |
| Online | bool | Specifies the online | R |
| ExtendRulerToAxis | bool | Specifies the extend ruler to axis on function trend control | R/W |
| Caption | MultilingualProperty | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon on the control window | R/W |
| Top | Int | Specifies the value of Y- coordinates of function trend control | R/W |
| Left | int | Specifies the value of X- Coordinate of function trend control | R/W |
| Width | uint | Specifies the width value of function trend control | R/W |
| Height | uint | Specifies the height value of function trend control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of function trend control | R |
| Name | string | Specifies the name of function trend control | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of function trend control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar on function trend control | R |
|  | HmiFontPart | Specifies the font type of function trend control | R |
| TimeZone | int | Specifies the time zone | R/W |
| ShowRuler | bool | Specifies the ruler | False |
| ShiftAxes | bool | Specifies the shift axes of function trend control | R/W |
| BackColor | Color | Specifies the background color of function trend control | R/W |
| Legend | HmiLegendPart | Specifies the legend | R |
| EventHandlers | HmiFunctionTrendControlEventHandlerComposition | Specifies the event handlers of function trend control | R |
| FunctionTrendAreas | HmiFunctionTrendAreaPartComposition | Specifes the function trend areas | R |
| CaptionColor | Color | Specifies the caption color of function trend control | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of function function trend control modify the following program code:

private void FunctionTrendControlPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen screen = hmiSoftware.Screens.Create("Screen_164");

HmiFunctionTrendControl hmifunctiontrendcontrol = screen.ScreenItems.Create&lt;HmiFunctionTrendControl&gt;("CTrendControl");

// To access basic properties of function function trend control

//Width

var autoplay = hmifunctiontrendcontrol.Width;

hmifunctiontrendcontrol.Width = 100;

//BackColor

var backcolor = hmifunctiontrendcontrol.BackColor;

hmifunctiontrendcontrol.BackColor = Color.Beige;

//Name

var name = hmifunctiontrendcontrol.Name;

hmifunctiontrendcontrol.Name = "DefaultName";

// To acccess multilingual property

//Caption

var caption = hmifunctiontrendcontrol.Caption.Items[0].Text;

hmifunctiontrendcontrol.Caption.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical properties

//Status bar

var statusBar = hmifunctiontrendcontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Program code: TrendArea in FunctionTrendControl using part

To create a trendarea in a Hmi Function function trend control using part modify the following program code:

private void TrendAreaCreateUsingPart()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_1");

HmiFunctionTrendControl hmifunctiontrendcontrol = hmiSoftware.Screens[0].ScreenItems.Create&lt;HmiFunctionTrendControl&gt;("CTrendControl_1");

HmiFunctionTrendAreaPart part = hmifunctiontrendcontrol.FunctionTrendAreas.Create("part1");

}

clipboard

To search a trendarea in Hmi Function function trend control using part modify the following program code :

private void TrendAreaPartSearch()

{

HmiFunctionTrendAreaPart part = hmifunctiontrendcontrol.FunctionTrendAreas.Find("part1");

}

clipboard

To check a trendarea in Hmi Function function trend control using part modify the following program code :

private void IsTrendAreaExist()

{

bool bPresent = hmifunctiontrendcontrol.FunctionTrendAreas.Contains(part);

}

clipboard

###### Accessing media player properties (RT Unified)

###### Introduction

The following properties are supported in media player screen items.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Url | string | Specifies the url of media player | R/W |
| AutoPlay | bool | Specifies the auto play of media player | R/W |
| VideoOutput | HmiVideoOutput | Specifies the video output of media player | R/W |
| BackColor | Color | Specifies the background color of radio process control | R/W |
| Caption | MultilingualProperty | Specifies the caption of process control | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window flags of process control | R/W |
| Icon | string | Specifies the icon of process control | R/W |
| Top | int | Specifies the X position of process control | R/W |
| Left | int | Specifies the Y position of process control | R/W |
| Width | uint | Specifies the width of process control | R/W |
| Height | uint | Specifies the height of process control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of media player | True |
| Name | string | Specifies the name of process control  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of process control | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of process control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar of process control | R |
| EventHandlers | HmiMediaControlEventHandlerComposition | Specifies the event handle of process control | R |
| CaptionColor | Color | Specifies the caption color of process control | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access basic properties of media player modify the following program code:

private void MediaPlayerPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_156");

var hmimediacontrol = createdscreen.ScreenItems.Create&lt;HmiMediaControl&gt;("HmiMediaControl_1");

// To access basic properties

//Autoplay

var autoplay = hmimediacontrol.AutoPlay;

hmimediacontrol.AutoPlay = true;

//BackColor

var backcolor = hmimediacontrol.BackColor;

hmimediacontrol.BackColor = Color.Beige;

//Name

var name = hmimediacontrol.Name;

hmimediacontrol.Name = "DefaultName";

// To access multilingual properties

//Caption

var caption = hmimediacontrol.Caption.Items[0].Text;

hmimediacontrol.Caption.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical propeties

var statusBar = hmimediacontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing process control properties (RT Unified)

###### Property

The following properties are supported in process control screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Online | bool | Specifies the online connection of process control | R/W |
| TimeStepSmoothingBase | HmiTimeRangeBase | Specifies the time interval for smoothing base | R/W |
| TimeStepSmoothingFactor | int | Specifies the time interval for smoothing factor | R/W |
| BackColor | Color | Specifies the background color of process control | R/W |
| Caption | MultilingualProperty | Specifies the text mentioned on process control | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window flags of process control | R/W |
| Icon | string | Specifies the icon of process control | R/W |
| Top | int | Specifies the X position of process control | R/W |
| Left | int | Specifies the Y position of process control | R/W |
| Width | uint | Specifies the width of process control | R/W |
| Height | uint | Specifies the height of process control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of process control | R |
| Name | string | Specifies the name of process control  The length of the name character should lie betweenn 1 - 128 characters | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if the allow operation control is enabled or not | R/W |
| TabIndex | ushort | Specifies the tab index of process control | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of process control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar of process control | R |
| EditMode | HmiEditMode | Specifies the edit mode of process control | R/W |
| TimeZone | int | Specifies the time zone of process control | R/W |
| ProcessView | HmiDataGridViewPart | Specifies the process view of process control | R |
| EventHandlers | HmiProcessControlEventHandlerComposition | Specifies the event handle of process control | R |
| CaptionColor | Color | Specifies the caption color of process control | R/W |
| ShowFocusVisual | bool | Specifies if the show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of process control modify the following program code :

private void ProcessControlPropertiesAccess()

{

// To access basic properties

//Width

var autoplay = hmiprocesscontrol.Width;

hmiprocesscontrol.Width = 1;

//BackColor

var backcolor = hmiprocesscontrol.BackColor;

hmiprocesscontrol.BackColor = Color.Beige;

//Name

var name = hmiprocesscontrol.Name;

hmiprocesscontrol.Name = "DefaultName";

// To access multilingual property

//Caption

var caption = hmiprocesscontrol.Caption.Items[0].Text;

hmiprocesscontrol.Caption.Items[0].Text= "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical properties

//status bar

var statusBar = hmiprocesscontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing parameter set control properties (RT Unified)

###### Property

The following properties are supported in parameter set control:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| ParameterSetTypeFixed | string |  | False |
| BackColor | Color | Specifies the background color of parameter set control | False |
| Caption | MultilingualProperty | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | False |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | False |
| Icon | string | Specifies the icon on the control window | False |
| Top | int | Specifies the value of Y- coordinates of parameter set control | False |
| Left | int | Specifies the value of X- Coordinate of parameter set control | False |
| Width | uint | Specifies the width value of parameter set control | False |
| Height | uint | Specifies the height value of parameter set control | False |
| CurrentQuality | HmiQuality | Specifies the connection status of parameter set control | True |
| Name | string | Specifies the name of parameter set control | False |
| Visible | bool | Specifies if the visible is enabled or not | False |
| Enabled | bool | Specifies if allow operator control is enabled or not | False |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | False |
| ToolBar | HmiToolBarPart | Specifies the tool bar of parameter set control | True |
| StatusBar | HmiStatusBarPart | Specifies the status bar on parameter set control | True |
| EditMode | HmiEditMode | Specifies the edit mode of parameter set control | False |
| TimeZone | int | Specifies the time zone of parameter set control | False |
| ParameterView | HmiDataGridViewPart | Specifies the parameter view of parameter set control | True |
| ForeColor | Color | Specifies the foreground color of parameter set control | False |
| SelectionBackColor | Color | Specifies the selected background color of parameter set control | False |
| SelectionForeColor | Color | Specifies the selected foreground color of parameter set control | False |
| Font | HmiFontPart | Specifies the font of parameter set control | True |
| EventHandlers | HmiDetailedParameterControlEventHandlerComposition | Specifies the event handler of parameter set control | True |
| CaptionColor | Color | Specifies the caption color of parameter set control | False |
| HideDetails | bool | Specifies if hide details is enabled or not | False |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | False |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of parameter set control modify the following program code :

private void ParameterSetControlPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen screen = hmiSoftware.Screens.Create("TestScreen");

HmiDetailedParameterControl hmidetailedparametercontrol = screen.ScreenItems.Create&lt;HmiDetailedParameterControl&gt;("ParameterControl_1");

// To access basic properties

//Width

var autoplay = hmidetailedparametercontrol.Width;

hmidetailedparametercontrol.Width = 100;

//BackColor

var backcolor = hmidetailedparametercontrol.BackColor;

hmidetailedparametercontrol.BackColor = Color.Beige;

//Name

var name = hmidetailedparametercontrol.Name;

hmidetailedparametercontrol.Name = "Default";

// To access multilingual property

//Caption

var caption = hmidetailedparametercontrol.Caption.Items[0].Text;

hmidetailedparametercontrol.Caption.Items[0].Text= "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical property

//Status bar

var statusBar = hmidetailedparametercontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing screen window properties (RT Unified)

###### Property

The following properties are supported in screen window screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| TabIntoWindow | bool | Specifies the tab into window of screen window | R/W |
| Screen | string | Specifies the screen of screen window | R/W |
| ScreenName | string | Specifies the screen name of screen window | R |
| ScreenNumber | byte | Specifies the screen number of screen window | R |
| System | byte | Specifies the system of screen window | R/W |
| CurrentZoomFactor | double | Specifies the current zoom factor of screen window | R/W |
| VerticalScrollBarVisibility | HmiScrollBarVisibility | Specifies the vertical scroll bar visibility of screen window | R/W |
| VerticalScrollBarPosition | int | Specifies the vertical scroll bar position of screen window | R/W |
| HorizontalScrollBarVisibility | HmiScrollBarVisibility | Specifies the horizontal scroll bar visibility of screen window | R/W |
| HorizontalScrollBarPosition | int | Specifies the horizontal scroll bar position of screen window | R/W |
| Adaption | HmiScreenWindowAdaption | Specifies the adaption of screen window | R/W |
| InteractiveZooming | bool | Specifies the interactive zooming of screen window | R |
| Caption | MultilingualProperty | Specifies the caption of screen window | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon of screen window | R/W |
| Top | int | Specifies the value of the Y coordinates of screen window | R/W |
| Left | int | Specifies the value of the X coordinates of screen window | R/W |
| Width | uintz | Specifies the width of screen window | R/W |
| Height | uint | Specifies the height of screen window | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of screen window | R |
| Name | string | Specifies the name of screen window | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| EventHandlers | HmiScreenWindowEventHandlerComposition | Specifies the event handlers of screen window | R |
| CaptionColor | Color | Specifies the caption color of screen window | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access properties of screen window modify the following program code:

private void ScreenWindowPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_15666");

var hmiscreenwindow = createdscreen.ScreenItems.Create&lt;HmiScreenWindow&gt;("HmiScreenWindow_1")

// To access basis property of screen window

//Width

var autoplay = hmiscreenwindow.Width;

hmiscreenwindow.Width = 100;

//HorizontalScrollBarVisibility

var horizontalscrollbarvisibilityValue = hmiscreenwindow.HorizontalScrollBarVisibility;

hmiscreenwindow.HorizontalScrollBarVisibility = HmiScrollBarVisibility.Visible;

//Name

var name = hmiscreenwindow.Name;

hmiscreenwindow.Name = "DefaultName";

// To access multilingual property

// Caption

hmiscreenwindow.Caption.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

}

clipboard

###### Accessing system diagnosis control properties (RT Unified)

###### Property

The following properties are supported in system diagnosis screen items:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| SystemDiagnosisView | HmiDataGridViewPart | Specifies the system diagnosis view | R |
| Caption | HmiTextPart | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R |
| BackColor | Color | Specifies the  background color of system diagnosis | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon on the system diagnosis | R/W |
| Top | int32 | Specifies the value of Y- coordinates of system diagnosis | R/W |
| Left | int32 | Specifies the value of X- Coordinate of system diagnosis | R/W |
| Width | uint32 | Specifies the width value of system diagnosis | R/W |
| Height | uint32 | Specifies the height value of system diagnosis | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of system diagnosis | R |
| Name | string | Specifies the name of system diagnosis | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of system diagnosis | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar on system diagnosis | R |
| TimeZone | int | Specifies the time zone of system diagnosis | R/W |
| CaptionColor | Color | Specifies the caption color of system diagnosis | R/W |
| ShowFocusVisual | bool | Specifies if show focus visual is enabled or not | R/W |

###### Requirement

- The HMI Software objec is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the properties of system diagnosis modify the following program code:

private void SystemDiagnosisControlPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen screen = hmiSoftware.Screens.Create("Screen_1");

HmiSystemDiagnosisControl syscontrol = screen.ScreenItems.Create&lt;HmiSystemDiagnosisControl&gt;("SysDiag_1");

syscontrol.SystemDiagnosisView.RowHeight = 50;

Debug.Assert(syscontrol.SystemDiagnosisView.RowHeight.Equals(50));

syscontrol.TimeZone = 28;

Debug.Assert(syscontrol.TimeZone.Equals(28));

}

clipboard

###### Accessing trend control properties (RT Unified)

###### Property

The following properties are supported in trend control screen items.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| ShowStatisticRulers | bool | Specifies the show statistic rulers of trend control | R/W |
| AreaSpacing | ushort | Specifies the area space on trend control | R/W |
| ExtendRulerToAxis | bool | Specifies the extend ruler to axis on trend control | R/W |
| Caption | MultilingualProperty | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon on the control window | R/W |
| Top | int | Specifies the value of Y- coordinates of trend control | R/W |
| Left | int | Specifies the value of X- Coordinate of trend control | R/W |
| Width | uint | Specifies the width value of trend control | R/W |
| Height | uint | Specifies the height value of trend control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of trend control | R |
| Name | string | Specifies the name of trend control | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of trend control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar on trend control | R |
| Font | HmiFontPart | Specifies the font type of trend control | R |
| TimeZone | int | Specifies the time zone on trend control | R/W |
| ShowRuler | bool | Specifies the ruler of trend control | R/W |
| ShiftAxes | bool | Specifies the shift axis of trend control | R/W |
| BackColor | Color | Specifies the background color of trend control | R/W |
| Legend | HmiLegendPart | Specifies the legend of trend control | R |
| EventHandlers | HmiTrendControlEventHandlerComposition | Specifies the event handlers of trend control | R |
| CaptionColor | Color | Specifies the caption color of trend control | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |

> **Note**
>
> The LabelFont is a Time Axis property of trend base controls.

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access basic properties of trend control modify the following program code:

private void TrendControlPropertiesAccess()]

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiScreen screen = hmiSoftware.Screens.Create("Screen_164");

HmiFunctionTrendControl hmitrendcontrol = screen.ScreenItems.Create&lt;HmiFunctionTrendControl&gt;("CTrendControl");

// To access basic properties

//Width

var autoplay = hmitrendcontrol.Width;

hmitrendcontrol.Width = 1;

//BackColor

var backcolor = hmitrendcontrol.BackColor;

hmitrendcontrol.BackColor = Color.Beige;

//Name

var name = hmitrendcontrol.Name;

hmitrendcontrol.Name = "DefaultName";

// To access multilingual property

//Caption

var caption = hmitrendcontrol.Caption.Items[0].Text;

hmitrendcontrol.Caption.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

//To access other typical properties

//Status bar

var statusBar = hmitrendcontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing trend companion properties (RT Unified)

###### Property

The following properties are supported in trend companion screen items.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| TrendCompanionMode | HmiTrendCompanionMode | Specifies the companion mode | R/W |
| UseSourceControlTrendColors | bool | Specifies the source control trend color | R/W |
| ShowAlways | bool | Specifies if the show always is enabled or not | R/W |
| UseSourceControlBackColor | bool | Specifies the source control background color | R/W |
| Caption | MultilingualProperty | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon on the control window | R/W |
| Top | int | Specifies the value of Y- coordinates of trend companion | R/W |
| Left | int | Specifies the value of X- Coordinate of trend companion | R/W |
| Width | uint | Specifies the width value of trend companion | R/W |
| Height | uint | Specifies the height value of trend companion | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of trend companion | R |
| Name | string | Specifies the name of trend companion | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of trend companion | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar on trend companion | R |
| SourceTrendControl | string | Specifies the color of trend based on source control | R/W |
| TimeZone | int | Specifies the time zone of trend companion | R/W |
| SnapToSourceControl | bool | Specifies the control that should be snapped to | R/W |
| TrendRulerView | HmiDataGridViewPart | Specifies the trend ruler view | R |
| TrendStatisticAreaView | HmiDataGridViewPart | Specifies the statistic area view | R |
| BackColor | Color | Specifies the background color of trend companion | R/W |
| TrendStatisticResultView | HmiDataGridViewPart | Specifies the statistic result view | R |
| EventHandlers | HmiTrendCompanionEventHandlerComposition | Specifies the event handlers of trend companion | R |
| CaptionColor | Color | Specifies the caption color of trend companion | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Pogram code

Modify the following program code to access basic properties of trend companion:

private void TrendCompanionPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_1566");

var hmitrendcompanion = createdscreen.ScreenItems.Create&lt;HmiTrendCompanion&gt;("HmiTrendCompanion_1");  
// To access basic properties

//Width

var autoplay = hmitrendcompanion.Width;

hmitrendcompanion.Width = 100;

//BackColor

var backcolor = hmitrendcompanion.BackColor;

hmitrendcompanion.BackColor = Color.Beige;

//Name

var name = hmitrendcompanion.Name;

hmitrendcompanion.Name = "DefaultName";

// To access multilingual property

//Caption

var caption = hmitrendcompanion.Caption.Items[0].Text;

hmitrendcompanion.Caption.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical properties

//Status bar

var statusBar = hmitrendcompanion.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Accessing web control properties (RT Unified)

###### Property

The following properties are supported in web control screen items.

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Url | string | Specifies the url of the web control | R/W |
| BackColor | Color | Specifies the background color of web control | R/W |
| Caption | MultilingualProperty | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Icon | string | Specifies the icon on the control window | R/W |
| Top | Int | Specifies the value of Y- coordinates of web control | R/W |
| Left | int | Specifies the value of X- Coordinate of web control | R/W |
| Width | uint | Specifies the width value of web control | R/W |
| Height | uint | Specifies the height value of web control | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of web control | R/W |
| Name | string | Specifies the name of web control | R/W |
| Visible | bool | Specifies if the visible is enabled or not | R/W |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| ToolBar | HmiToolBarPart | Specifies the tool bar of web control | R |
| StatusBar | HmiStatusBarPart | Specifies the status bar on web control | R |
| EventHandlers | HmiWebControlEventHandlerComposition | Specifies the event handler of web control | R |
| CaptionColor | Color | Specifies the caption color of web control | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

Modify the following program code to access basic properties of web control:

private void WebControlPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

var screen = hmiSoftware.Screens;

var createdscreen = screen.Create("TestScreen_1566");

var hmiwebcontrol = createdscreen.ScreenItems.Create&lt;HmiWebControl&gt;("HmiWebControl_1")

// To access basic property

//Width

var autoplay = hmiwebcontrol.width;

hmiwebcontrol.Width = 100;

//BackColor

var backcolor = hmiwebcontrol.BackColor;

hmiwebcontrol.BackColor = Color.Beige;

//Name

var name = hmiwebcontrol.Name;

hmiwebcontrol.Name = "DefaultName";

// To access multilingual property

//Caption

var caption = hmiwebcontrol.Caption.Items[0].Text;

hmiwebcontrol.Caption.Items[0].Text= "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

// To access other typical properties

//Status bar

var statusBar = hmiwebcontrol.StatusBar;

var backColor = statusBar.BackColor;

statusBar.BackColor = Color.Aqua;

var enabled = statusBar.Enabled;

statusBar.Enabled = true;

var visible = statusBar.Visible;

statusBar.Visible = true;

}

clipboard

###### Faceplate Container (RT Unified)

This section contains information on the following topics:

- [Description FaceplateContainer (RT Unified)](#description-faceplatecontainer-rt-unified)
- [FaceplateContainer.Create() (RT Unified)](#faceplatecontainercreate-rt-unified)
- [FaceplateContainer.Delete() (RT Unified)](#faceplatecontainerdelete-rt-unified)
- [Accessing faceplate container properties (RT Unified)](#accessing-faceplate-container-properties-rt-unified)
- [Accessing contained type properties (RT Unified)](#accessing-contained-type-properties-rt-unified)
- [Assigning UDT to faceplate container (RT Unified)](#assigning-udt-to-faceplate-container-rt-unified)

###### Description FaceplateContainer (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To perform a task on a faceplate container screenitems you can use enumerate, find, index commands and the Contains() method.

To access faceplate container from screen items list by using ScreenItems property of the HmiScreen class modify the following program code:

private void FacePlateContainerSearch(HmiSoftware hmiSoftware)

{

HmiScreen hmiScreen = hmiSoftware.Screens.Create("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiScreen.Screens[0].ScreenItems;

foreach (var item in screenitems)

{

//working with screenitems

}

}

clipboard

To access faceplate container from screen items list by name modify the following program code:

private void FacePlateInstanceSearchByName(HmiSoftware hmiSoftware, string FacePlateContainerName = "FaceplateContainer_1")

{

HmiScreenItemBase screenitems = hmiSoftware.Screens[0].ScreenItems.Find(FacePlateContainerName);

}

clipboard

To access faceplate container from screenitems list by index modify the following program code:

private void FaceplateContainerSearchByIndex(HmiSoftware hmiSoftware)

{

HmiScreenItemBase screenitem = hmiSoftware.Screens[0].ScreenItems[0];

}

clipboard

To check a particular faceplate container exist in screen item list by using Contains() modify the following program code:

private void IsFaceplateContainerExist(HmiSoftware hmiSoftware)

{

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens[0].ScreenItems;

HmiFaceplateContainer faceplate = screenitems.Create&lt;HmiFaceplateContainer&gt;("Faceplate_1");

bool isexists = screenitems.Contains(faceplate);

}

clipboard

###### Working with faceplate container

You can perform the following tasks with faceplate container while using TIA Portal Openness:

- Creating faceplate container : [FaceplateContainer.Create()](#faceplatecontainercreate-rt-unified)
- Deleting faceplate container: [FaceplateContainer.Delete()](#faceplatecontainerdelete-rt-unified)
- Faceplate container properties [Accessing faceplate container properties](#accessing-faceplate-container-properties-rt-unified)
- Faceplate container contained type property: [Accessing contained type properties](#accessing-contained-type-properties-rt-unified)
- Faceplate container UDT property: [Assigning UDT to faceplate container](#assigning-udt-to-faceplate-container-rt-unified)

###### FaceplateContainer.Create() (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To create a faceplate container screen item modify the following program code:

private void CreateFaceplateContainer(HmiSoftware hmiSoftware, string FacePlateContainerName = "FaceplateContainer_1")

{

HmiScreen hmiScreen= hmiSoftware.Screens.Create(screenName);

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens[0].ScreenItems;

HmiFaceplateContainer faceplate = hmiScreen.ScreenItems.Create&lt;HmiFaceplateContainer&gt;(FacePlateContainerName);

}

clipboard

###### FaceplateContainer.Delete() (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To delete faceplate container screen item modify the following program code :

private void DeleteFaceplateContainer(HmiSoftware hmiSoftware, string FaceplateContainerName = "FaceplateContainer_1")

{

HmiScreen hmiScreen = hmiSoftware.Screens.Create("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens[0].ScreenItems;

HmiFaceplateContainer faceplate = hmiScreen.ScreenItems.Create&lt;HmiFaceplateContainerName&gt;(FaceplateContainerName);

If (faceplate! = null)

{

faceplate.Delete ();

}

}

clipboard

private void DeleteFaceplateContainer(HmiSoftware hmiSoftware, string FacePlateContainerName = "FaceplateContainer_1")

{

HmiSoftware hmiSoftware = GetHMISoftware();

HmiScreen hmiScreen = hmiSoftware.Screens.Create ("Screen_1");

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens[0].ScreenItems;

HmiFaceplateContainer faceplate = hmiScreen.ScreenItems.Create&lt;HmiFaceplateContainer&gt;(FacePlateContainerName);

IEngineeringObject ObjhmiLineEnggObj = faceplate;

if (ObjhmiLineEnggObj != null)

{

ObjhmiLineEnggObj.Invoke ("Delete", null);

}

}

clipboard

###### Accessing faceplate container properties (RT Unified)

###### Property

The following properties are supported in faceplate container:

| Property Name | Datatype | Description | Accessibility |
| --- | --- | --- | --- |
| Name | System.String | Specifies the name of the faceplate instance | R/W |
| ContainedType | System.String | Specifies the contained faceplate type  For information on contained type, see [Accessing contained type properties](#accessing-contained-type-properties-rt-unified) | R/W |
| Enabled | System.Boolean | Specifies if the allow operator control is enabled or not | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status | R |
| Height | System.UInt32 | Specifies the height of control window | R/W |
| Icon | System.String | Specifies the icon on the control window | R/W |
| Caption | Siemens.Engineering.MultilingualTex | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R |
| TabIndex | System.UInt16 | Specifies the screen items specifying a tab index of 0 are not part of the tab order | R/W |
| Visible | System.Boolean | Specifies the visiblity of screen item | R/W |
| Width | System.UInt32 | Specifies the width of the control window | R/W |
| WindowFlags | Siemens.Engineering  miUnified.UI.Enum  WindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |
| Top | System.Int32 | Specifies the value of Y coordinates of control window | R/W |
| Left | System.Int32 | Specifies the value of X coordinates of control window | R/W |
| Interface | Siemens.Engineering.HmiUnified.UI.Parts.HmiFaceplateInterfaceCompostion | Specifies the  Faceplate interfaces | R |
| EventHandlers | HmiFaceplateContainerEventHandlerComposition | Specifies the event handlers of HmiFaceplateContainer  For more information on event handler, see | R |
| ShowFocusVisual | Boolean | Specifies if the show focus is enabled or not | R/W |
| RotationAngle | Int16 | Specifies the rotation angle of the screen item in degree | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To get the properties usage of faceplate container modify the following program code:

private void FacePlateContainerPropertiesAccess()

{

HmiScreen screen = m_hmiSoftware.Screens[0];

HmiFaceplateContainer faceplate = screens[0].ScreenItems[0] as HmiFaceplateContainer;

//Get_faceplateContainedType

Var containedtype = faceplate.ContainedType;

Console.Writeline("Faceplate Container Type: " + containedtype);

Example Result = "Default Version No.\Faceplate type name";

//Get_CaptionText

string Caption = faceplate.Caption.Items[0].Text;

Console.WriteLine("Faceplate Caption: " + Caption);

//Get_WindowFlags

HmiWindowFlag WindowFlags = faceplate.WindowFlags;

Console.WriteLine("Faceplate WindowFlags: " + WindowFlags);

//Get_Icon

string Icon = faceplate.Icon;

Console.WriteLine("Faceplate Icon: " + Icon);

//Get_Top

int Top = faceplate.Top;

Console.WriteLine("Faceplate Top: " + Top);

//Get_Left

int Left = faceplate.Left;

Console.WriteLine("Faceplate Left: " + Left);

//Get_Width

uint Width = faceplate.Width;

Console.WriteLine("Faceplate Width: " + Width);

//Get_Height

uint Height = faceplate.Height;

Console.WriteLine("Faceplate Height: " + Height);

//Get_CurrentQuality

HmiQuality CurrentQuality = faceplate.CurrentQuality;

Console.WriteLine("Faceplate CurrentQuality: " + CurrentQuality);

//Get_Name

string Name = faceplate.Name;

Console.WriteLine("Faceplate Name : " + Name);

//Get_Visible

bool Visible = faceplate.Visible;

Console.WriteLine("Faceplate Visible: " + Visible);

//Get_Enabled

bool Enabled = faceplate.Enabled;

Console.WriteLine("Faceplate Enabled: " + Enabled);

//Get_TabIndex

ushort TabIndex = faceplate.TabIndex;

Console.WriteLine("Faceplate TabIndex: " + TabIndex);

}

clipboard

To set the properties usage of faceplate container modify the following program code:

private void FacePlateContainerPropertiesAccess()

{

//Set_ContainedType

faceplate.ContainedType = "V0.0.1\Faceplate_1";

//Set_CaptionText:

faceplate.Caption.Items[0].Text = "testCaption";

//Set_WindowFlags

faceplate.WindowFlags = HmiWindowFlag.CanSize;

//Set_Icon

faceplate.Icon = “testCaption”;

//Set_Top

faceplate.Top = 50;

//Set_Left

faceplate.Left = 50;

//Set_Width

faceplate.Width = 50;

//Set_Height

faceplate.Height = 50;

//Set_Name

faceplate.Name = “TestName”;

//Set_Visible

faceplate.Visible = true;

//Set_Enabled

faceplate.Enabled = true;

//Set_TabIndex

faceplate.TabIndex = 10;

}

clipboard

###### Accessing contained type properties (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access the contained type property of faceplate container with new location of faceplate types in project library:

private void AccessUnifiedFaceplateProperties(createFacePlateContainer)

{

HmiFaceplateContainer faceplatecontainer = createFacePlateContainer("FacePlateContainer");

faceplateContainer ContainedType = "Faceplate_1";

var containedType = faceplateContainer.ContainedType;

//Output: "V0.0.2\\Faceplate_1

HmiFaceplateContainer faceplatecontainer = CreateFacePlateContainer("FacePlateContainer");

faceplateContainer ContainedType = "V0.0.1\Faceplate_1";

var containedType = faceplateContainer.ContainedType;

//Output: "V0.0.1\\Faceplate_1"  
}

clipboard

###### Assigning UDT to faceplate container (RT Unified)

###### Requirement

The HMI Software object is accessible  
See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To assign UDT to the Faceplate container modify the following program code:

private void AssignUDTTToFaceplateContainer(HmiSoftware hmiSoftware, Project proj)

{

var hmiSoftware = GetHmiSoftware(proj);

HmiScreenItemBaseComposition screenitems = hmiSoftware.Screens.Find("Screen_1").ScreenItems;

HmiFaceplateContainer faceplateContainer = screenitems.Find("FaceplateContainer_1") as HmiFaceplateContainer;

faceplateContainer.ContainedType = "Faceplate_1";

// where UDT is the instance created in TagTable from the UDT created in library

faceplateContainer.Interface[0].Value = "UDT";

}

clipboard

##### My controls (RT Unified)

This section contains information on the following topics:

- [Accessing custom web control container properties (RT Unified)](#accessing-custom-web-control-container-properties-rt-unified)

###### Accessing custom web control container properties (RT Unified)

###### Property

The following properties are supported in HMI Custom Web Control Container:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Authorization | string | Specifies the authorization of custom web control container | R/W |
| EventHandlers | HmiCustomWebControlContainerEventHandlerComposition | Specifies the event handlers of custom web control container | R |
| Interface | HmiCustomControlInterfaceComposition | Specifies the interface of custom web control container | R |
| RequireExplicitUnlock | bool | Specifies if the explicit unlock required or not | R/W |
| Left | int | Specifies the value of the X coordinates of control window | R/W |
| Caption | HmiTextPart | Specifies the text to be shown in the caption of a screen window or windowed control (Label) | R |
| CaptionColor | Color | Specifies the caption color of custom web control container | R/W |
| ContainedType | string | Specifies the contained faceplate type | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of custom web control container | R |
| Dynamization | DynamizationBaseComposition | Specifies the dynamization of custom web control container | R |
| Enabled | bool | Specifies if allow operator control is enabled or not | R/W |
| Height | uint | Specifies the height of custom web control container | R/W |
| Icon | string | Specifies the icon of custom web control container | R/W |
| Name | string | Specifies the name of custom web control container | R/W |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handlers of custom web control container | R |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| Top | int | Specifies the value of the Y coordinates of custom web control container | R/W |
| Visible | bool | Specifies the visiblity of custom web control container | R/W |
| Width | uint | Specifies the width of the control window | R/W |
| WindowFlags | HmiWindowFlag | Specifies the window configuration like ShowCaption, ShowBorder, AlwaysOnTop. | R/W |

> **Note**
>
> The path to access the HMI Custom Web Control Container available in the following location: C:\Program Files\SiemensAutomation\Portal V*\Data\Hmi\CustomControls
>
> Where V* refers to the installed version of TIA Portal.

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access plant overview control of type Hmi custom web control container modify the following program code:

private void CustomWebControlContainerPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware(MyProject);

HmiScreenComposition screens = hmiSoftware.Screens;

HmiScreen screen = screens.Create("Screen_1");

HmiCustomWebControlContainer plantOverview = screen.ScreenItems.Create&lt;HmiCustomWebControlContainer&gt;("DefaultName", "Siemens.CPM");

HmiCustomWebControlContainer reports = screen.ScreenItems.Create&lt;HmiCustomWebControlContainer&gt;("DefaultName_1", "Siemens.REP");

// Access basic properties of plant overview control of type HmiCustom Web Control Container

//Left

plantOverview.Left = 1;

//CaptionColor

plantOverview.CaptionColor = Color.AliceBlue;

// Access other typical properties of plant overview control of type Hmi Custom Web Control Container

HmiCustomControlInterfaceComposition customControlInterfaceComposition = plantOverview.Interface;

var count = customControlInterfaceComposition.Count;

if (count &gt; 0)

{

foreach (var customControlInterface in customControlInterfaceComposition)

{

string propertyName = customControlInterface.PropertyName;

object propertyValue = customControlInterface.Value;

if (propertyName == "SelectionBackColor")

{

customControlInterface.Value = Color.Blue;

}

}

///*--------------------Alternative　Way-------------------------*/

HmiCustomControlInterface selectionBackColorProperty　= customControlInterfaceComposition.FirstOrDefault(x =&gt; x.PropertyName == "SelectionBackColor");

if (selectionBackColorProperty != null)

{

selectionBackColorProperty.Value = Color.AliceBlue;

}

}

}

clipboard

> **Note**
>
> To create a custom web control, the unique name mentioned in the manifest.json file of the custom web control should be provided as ContainedTypeValue. Using Display name in this case will not create the custom web control object. As in Example above “Siemens.CPM” is used instead of the display name : Plant overview.

##### Dynamic widgets (RT Unified)

This section contains information on the following topics:

- [Accessing custom widget container properties (RT Unified)](#accessing-custom-widget-container-properties-rt-unified)

###### Accessing custom widget container properties (RT Unified)

###### Property

The following properties are supported in HMI Custom Widget Container:

| Property Name | Property Type | Description | Accessibility |
| --- | --- | --- | --- |
| Authorization | string | Specifies the authorization of custom widget container | R/W |
| CurrentQuality | HmiQuality | Specifies the connection status of custom widget container | R |
| Dynamizations | DynamizationBaseComposition | Specifies the dynamization of custom widget container | R |
| Enabled | bool | Specifies if the allow operator control is enabled or not | R/W |
| EventHandlers | HmiCustomWidgetContainerEventHandlerComposition | Specifies the event handler of custom widget container | R |
| Height | uint | Specifies the height of custom widget container | R/W |
| Interface | HmiCustomControlInterfaceComposition | Specifies the interface of custom widget container | R |
| Left | int | Specifies the value of the X coordinates of custom widget container | R/W |
| Name | string | Specifies the name of custom widget container | R/W |
| Opacity | string | Specifies the opacity of custom widget container | R/W |
| PropertyEventHandlers | PropertyEventHandlerComposition | Specifies the property event handler of custom widget container | R |
| RequireExplicitUnlock | bool | Specifies if the explicit unlock is required or not | R/W |
| RotationAngle | short | Specifies the rotational angle of custom widget container | R/W |
| RotationCenterPlacement | HmiRotationCenterPlacement | Specifies the pivot of custom widget container | R/W |
| RotationCenterX | float | Specifies the X pivot of custom widget container | R/W |
| RotationCenterY | float | Specifies th Y pivot of customw widget container | R/W |
| ShowFocusVisual | bool | Specifies if the show focus is enabled or not | R/W |
| TabIndex | ushort | Screen items specifying a tab index of 0 are not part of the tab order | R/W |
| ToolTipText | MultilingualText | Specifies the tooltip text of custom widget container | R |
| Top | int | Specifies the value of the Y coordinates of custom widget container | R/W |
| Visible | bool | Specifies the visiblity of custom widget container | R/W |
| VisualizeQuality | bool | Specifies the visual quality of custom widget container | R/W |
| Width | uint | Specifies the width of the control widget container | R/W |

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access basic properties of "extended.Flame" of type HMI Custom Widget Container modify the following program code:

private void CustomWidgetContainerPropertiesAccess()

{

HmiSoftware hmiSoftware = GetHmiSoftware(MyProject);

HmiScreenComposition screens = hmiSoftware.Screens;

HmiScreen screen = hmiSoftware.Screens.Create("Screen_1");

HmiCustomWidgetContainer flame = screen.ScreenItems.Create&lt;HmiCustomWidgetContainer&gt;("Flame_1", "extended.Flame");

//Left

flame.Left = 1;

//ToolTipText

flame.ToolTipText.Items[0].Text = "&lt;body&gt;&lt;p&gt;TestforMultilingualProperty&lt;/p&gt;&lt;/body&gt;";

}

clipboard
> **Note**
>
> Correct value corresponding to parameter ‘containedTypeValue’ is must, in-order to create custom control.
>
> The keyword "extended.&lt;Widgetname&gt;" should be used for creating any custom widget container using TIA Portal Openness as we use Original name mentioned in the Manifest instead of using a Displayname.

##### PropertyEventHandlers (RT Unified)

This section contains information on the following topics:

- [Description PropertyEventHandlers (RT Unified)](#description-propertyeventhandlers-rt-unified)
- [PropertyEventHandlers.Create() (RT Unified)](#propertyeventhandlerscreate-rt-unified)
- [PropertyEventHandlers.Delete() (RT Unified)](#propertyeventhandlersdelete-rt-unified)
- [Accessing PropertyEventHandlers properties (RT Unified)](#accessing-propertyeventhandlers-properties-rt-unified)

###### Description PropertyEventHandlers (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access property event of screen items modify the following program code:

private void AccessPropertyEvent(HmiSoftware hmiSoftware)

{

HmiScreen screen = ((HmiSoftware)targetSW).Screens.Create("MyScreen");

HmiCircle hmiCircle = screen.ScreenItems.Create&lt;HmiCircle&gt;("MYCircle");

var hmiScreenPropeventDyn = screen.PropertyEventHandlers.Create(“Enabled”, PropertyEventType.Change);

var enabledEvent = screen.PropertyEventHandlers.Find("Enabled", PropertyEventType.Change);

//Property Event Browse

Console.WriteLine("CountofEventActions"+ screen PropertyEventHandlers.Count.ToString());

}

clipboard

###### Working with property event for screen items

You can perform the following tasks with event for screen/screen items while using TIA Portal Openness:

- Creating Property Event Handlers : [PropertyEventHandlers.Create()](#propertyeventhandlerscreate-rt-unified)
- Deleting Property Event Handlers [PropertyEventHandlers.Delete()](#propertyeventhandlersdelete-rt-unified)
- Property Event Handlers properties: [Accessing PropertyEventHandlers properties](#accessing-propertyeventhandlers-properties-rt-unified)

###### PropertyEventHandlers.Create() (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To create property event of screen item level object using PropertyEventHandlers navigator modify the following program code:

private void CreatePropertyEventHandler(HmiSoftware hmiSoftware)

{

HmiScreen screen = ((HmiSoftware)targetSW).Screens.Create("MyScreen");

HmiCircle hmiCircle = screen.ScreenItems.Create&lt;HmiCircle&gt;("MYCircle");

//Event Creation

PropertyEventHandler propertyEvent = hmiCircle.PropertyEventHandlers.Create("ToolTipText", PropertyEventType.Change);

}

clipboard

###### PropertyEventHandlers.Delete() (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To delete property events for screen items modify the following program code:

private void DeletePropertyEventHandler()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

PropertyEventHandler propertyEvent = ((HmiSoftware)targetSW).Screens[0].ScreenItems[0].PropertyEventHandlers.Create("ToolTipText", PropertyEventType.Change);

var changedEvent = screen.PropertyEventHandlers.Find(“ToolTipText”, PropertyEventType.Change);

//Property Event Deletion

changedEvent.Delete();

}

clipboard

###### Accessing PropertyEventHandlers properties (RT Unified)

###### Requirement

- The HMI Unified Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

To access property event properties modify the following program code:

private void AccessPropertyEvent()

{

//Property Event Get

PropertyEventType eventType = propertyEvent.EventType;

string propertyName = propertyEvent.PropertyName;

IHmiScript hmiScript = propertyEvent.Script;

//Script Action in Event Get

bool hmiScriptEventAsync = hmiScript.Async;

string hmiScriptEventGlobal = hmiScript.GlobalDefinitionAreaScriptCode;

string hmiScriptEventCode = hmiScript.ScriptCode;

HmiValidationResult result = hmiScript.SyntaxCheck();

}

clipboard

##### Accessing cross reference service on screenitems (RT Unified)

###### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

###### Program code

private void AccessCrossReferenceService()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;  //Accessing lower levels until we reach the ScreenComposition.

ScreenComposition screenComposition = hmiSoftware.Screens;

Screen screen = screenComposition.Find("Screen_1");

HmiScreenItemBase hmiScreenControl = screen.ScreenItems.Find("Alarm control_1");

if (hmiscreenControl != null)

{

try

{

CrossReferenceService crossReferenceService = hmiScreenControl.GetService&lt;CrossReferenceService&gt;();

// ......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

clipboard

### ScreenGroups (RT Unified)

This section contains information on the following topics:

- [Description ScreenGroups (RT Unified)](#description-screengroups-rt-unified)
- [ScreenGroups.Create() (RT Unified)](#screengroupscreate-rt-unified)
- [ScreenGroups.Delete() (RT Unified)](#screengroupsdelete-rt-unified)
- [Accessing screen groups properties (RT Unified)](#accessing-screen-groups-properties-rt-unified)

#### Description ScreenGroups (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access all screen groups of device modify following program code:

private void ScreenGroupBrowse(HmiSoftware hmiSoftware)

{

screenGroups = hmiSoftware.ScreenGroups;

MessageBox.Show(screenGroups.Count.ToString());

HmiScreenGroupComposition screenGroup2ndLevel = hmiSoftware.ScreenGroups[0].Groups;

MessageBox.Show(screenGroup2ndLevel.Count.ToString());

}

clipboard

##### Working with screen groups

You can perform the following tasks with screen groups while using TIA Portal Openness:

- Creating screen groups:[ScreenGroups.Create()](#screengroupscreate-rt-unified)
- Deleting screen groups: [ScreenGroups.Delete()](#screengroupsdelete-rt-unified)
- Screen groups properties: [Accessing screen groups properties](#accessing-screen-groups-properties-rt-unified)

#### ScreenGroups.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a screen groups (HmiScreenGroup) with Create method of class HmiScreenGroupComposition modify the following progam code:

private void CreateScreenGroupFirstLevel(HmiSoftware hmiSoftware)

{

HmiScreenGroupComposition screenGroups = hmiSoftware.ScreenGroups;

HmiScreenGroup screenGroup1stLevel = hmiSoftware.ScreenGroups.Create("Group_1stLevel");

}

clipboard

#### ScreenGroups.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a specific group with Delete() method of HmiScreenGroup class modify the following program code:

private void ScreenGroupDelete(HmiSoftware hmiSoftware)

{

HmiScreenGroupComposition screenGroups = hmiSoftware.ScreenGroups;

HmiScreenGroup screenGroupFindLevelOne = hmiSoftware.ScreenGroups.Find("Group_2");

screenGroupFindLevelOne.Delete();

}

clipboard

#### Accessing screen groups properties (RT Unified)

##### Property

The following properties are supported in screen groups:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the screen group name | R/W |
| Groups | HmiScreenGroupComposition | Specifies the list of screen groups | R |
| Screens | HmiScreenComposition | Specifies the list of screens | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the Groups property of screen groups modify the following program code:

private void AccessScreenGroupProperties(HmiSoftware hmiSoftware)

{

HmiScreenGroupComposition screenGroups = hmiSoftware.ScreenGroups;

MessageBox.Show(screenGroups.Count.ToString());

HmiScreenGroupComposition screenGroup2ndLevel = hmiSoftware.ScreenGroups[0].Groups;

MessageBox.Show(screenGroup2ndLevel.Count.ToString());

}

clipboard

### Tags (RT Unified)

This section contains information on the following topics:

- [Description Tags (RT Unified)](#description-tags-rt-unified)
- [Tags.Create() (RT Unified)](#tagscreate-rt-unified)
- [Tags.Delete() (RT Unified)](#tagsdelete-rt-unified)
- [Accessing tag properties (RT Unified)](#accessing-tag-properties-rt-unified)
- [Assigning user defined datatype to tag (RT Unified)](#assigning-user-defined-datatype-to-tag-rt-unified)
- [Accessing tag member properties of user defined type (RT Unified)](#accessing-tag-member-properties-of-user-defined-type-rt-unified)
- [Accessing cross reference service on tags (RT Unified)](#accessing-cross-reference-service-on-tags-rt-unified)

#### Description Tags (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on tag you can either use enumerate tag or use Find().

private void TagBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the tags of device

HmiTagComposition hmiTags = hmiSoftware.Tags;

for each (HmiTag hmiTag in hmiTags)

{

//working with tags

}

}

clipboard

private void TagSearch()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the tags of given tag table

string tagTableName = "SpecificTagTable";

HmiTagComposition hmiTags = hmiSoftware.HmiTagTables.Find("tagTableName").Tags;

for each (HmiTag hmiTag in hmiTags)

{

//working with tags

}

}

clipboard

To access a single tag by name modify the following code:

private void AccessTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Search for a specific tag

String hmiTagName = "HMI_Tag_1";

HmiTag hmiTag = hmiSoftware.HmiTags.Find("hmiTagName");

if(hmiTag != null)

{

// working with tags

}

clipboard

To access a tag by table name modify the following code:

private void AccessTagByName()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a tag present in given tag table with name "TagTable1"

HmiTag hmiTag4 = hmiSoftware.HmiTagTables.Find("TagTable1").HmiTags.Find("Tag1");

}

clipboard

##### Working with tags

You can perform the following tasks with tags while using TIA Portal Openness:

- Creating tags:[Tags.Create()](#tagscreate-rt-unified)
- Deleting tags: [Tags.Delete()](#tagsdelete-rt-unified)
- Tag properties: [Accessing tag properties](#accessing-tag-properties-rt-unified)
- Tag cross reference service: [Accessing cross reference service on tags](#accessing-cross-reference-service-on-tags-rt-unified)

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[HMISoftware object (RT Unified)](#hmisoftware-object-rt-unified)

#### Tags.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a HMI tag with Create() of HmiTagComposition class modify the following program code :

private void CreateTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition hmiTagscomp1 = hmiSoftware.HmiTags;

//Create a tag in the default tag table

HmiTag hmiTag1 = hmiTagscomp1.Create("Tag1");

//Create a tag in specific tag table with name "TagTable1"

//TagTable1 has to exist in your project otherwise it results in recoverable exception

HmiTag hmiTag2 = hmiTagscomp1.Create("Tag2", "TagTable1");

}

clipboard

To create a HMI tag by accessing Tags property of TagTable object modify the following program code :

private void CreateTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition hmiTagcomp2 = hmiSoftware.HmiTagTables.Find("Default tag table").HmiTags;

//Create a tag in the default tag table.

HmiTag hmiTag3 = hmiTagcomp2.Create("Tag_3");

//Create a tag in specific tag table with name "TagTableName"

//TagTableName has to exist in your project otherwise it results in recoverable exception

HmiTag hmiTag4 = hmiTagcomp2.Create("Tag_4", "TableTableName");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Tags.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a HMI tag with Delete() of HmiTag class modify the following program code :

private void DeleteTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Delete a tag at HmiSoftware level

HmiTagComposition hmiTagscomp1 = hmiSoftware.HmiTags;

HmiTag hmiTag1 = hmiTagscomp1.Find("Tag1");

hmiTag1.Delete();

}

clipboard

To delete a HMI tag by accessing Tags property of TagTable object modify the following program code:

private void DeleteTag()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Delete a tag with tag name "Tag2" in tag table

HmiTagComposition hmiTags2 = hmiSoftware.HmiTagTables.Find("Default tag table").HmiTags;

HmiTag hmiTag2 = hmiTags2.Find("Tag2");

hmiTag2.Delete();

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing tag properties (RT Unified)

##### Property

The following properties are supported in tag, which are also applicable to tag with UDT (user defined data type) and its members.

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| AccessMode | HmiAccessMode | Specifies the access mode of tag | R/W |
| AcquisitionCycle | String | Speciifies the acquisition cycle attribute of tag | R/W |
| AcquisitionMode | HmiTagAcquisitionMode | Specifies the acquisition mode of tag | R/W |
| Comment | MultilingualText | Specifies the get and set comment on tag | R/W |
| Connection | String | Specifies the connection of tag | R/W |
| DataType | String | Specifies the data type of tag   You can assign different types of datatype for tag for example simple, user defined datatype, and array.  To assign user defined datatype to tag, please refer the instruction mentioned in [Assigning user defined datatype to tag](#assigning-user-defined-datatype-to-tag-rt-unified) | R/W |
| MaxLength | UInt32 | Specifies the length of tag | R/W |
| Address | String | Specifies the address of tag | R/W |
| InitialMinValue | LowerRange | Specifies the start value for the event of tag | R |
| Name | String | Specifies the name of tag | R/W |
| Persistent | Boolean | Specifies the persistence of tag | R/W |
| PlcName | String | Specifies the name of Plc | R |
| PlcTag | String | Specifies the Plc Tag attribute | R/W |
| InitialValue | Object | Specifies the start value of tag | R/W |
| SubstituteValue | HmiSubstituteValue | Specifies the substitute value of tag | R |
| UpdateId | UInt32 | Specifies the updated id of tag | R/W |
| InitialMaxValue | UpperRange | Specifies the upper start limit value of tag | R |
| TagTableName | String | Specifies the tag table name to which tag belongs | R |
| HmiDataType | String | Specifies the Hmi datatype of tag | R/W |
| LinearScaling | Boolean | Specifies the value range on the Hmi tag and the PLC tag to map each other linearly | R/W |
| HmiStartValue | Object | Specifies the start value range on the Hmi tag to map linearly to the start value of the PLC tag | R/W |
| HmiEndValue | Object | Specifies the end value range on the Hmi tag to map linearly to the end value range on the PLC tag | R/W |
| PlcStartValue | Object | Specifies the start value range on the PLC tag to map linearly to the start value range on the Hmi tag | R/W |
| PlcEndValue | Object | Specifies the end value range on the PLC tag to map linearly to the end value range on the Hmi tag | R/W |
| GmpRelevant | Boolean | Specifies the changes to the tag value logged in an audit trail | R/W |
| TagType | Enum-&gt;TagType | Specifies the type of tag for example if tag type is simple, user defined datatype, and array |  |
| Members | HmiTagComposition  (HmiTag which is of UDT data type consists of member which itself are Tags.) | Specifies collection of member tags of user defined data type or element tags of array respectively.   You can access properties of member tags of user defined dataype, please refer the instruction mentioned in [Accessing tag member properties of user defined type](#accessing-tag-member-properties-of-user-defined-type-rt-unified) |  |

The following properties are available in LowerRange/UpperRange:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| Value | Object | Specifies the lower and upper value of tag | R/W |
| ValueType | HmiLimitValueType | Specifies the get and set value type of tag | R/W |

The following properties are available in SubstituteValue:

| Property Name | Data Type | Description | Access |
| --- | --- | --- | --- |
| Value | Object | Specifies the get and set value type | R/W |
| SubstituteValueUsage | Hmi SubstituteValueUsage | Specifies when to use substitute value | R/W |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of tag independent of data type modify the following program code:

private void TagProperties()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Tag_1 has to exist in TIA device project.

HmiTag hmiTag = hmiSoftware.HmiTags.Find("Tag_1");

//Enumeration type properties

AccessMode accessMode = hmiTag.AccessMode;

UpdateScope scope = hmiTag.UpdateScope;

//Assign valid value to properties which are independent from datatype of the tag

hmiTag.Name = "Tag_2";

hmiTag.AcquisitionCycle = "T1s";

hmiTag.DataType = "int";

hmiTag.PlcTag = "PlcTag_1";

}

clipboard

To access the properties of tag dependent of data type modify the following program code:

private void TagProperties()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Tag_1 has to exist in TIA device project.

HmiTag hmiTag = hmiSoftware.HmiTags.Find("Tag_1");

//Enumeration type properties

AccessMode accessMode = hmiTag.AccessMode;

UpdateScope scope = hmiTag.UpdateScope;

//Substitute value depends on data type of tag.

hmiTag.SubstituteValue.Value = "144";

hmiTag.SubstituteValue.OnCommunicationError = false;

//Start value depends on data type of tag.

hmiTag.StartValue = "1";

hmiTag.LowerLimit.ValueType = LimitValueType.Constant;

hmiTag.LowerLimit.Value = "HmiTag_1";

}

clipboard

To assign a string for a multilingual text then add a translation in every language of project modify the following program code:

private void TagProperties()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

//Tag_1 has to exist in TIA device project.

HmiTag hmiTag = hmiSoftware.HmiTags.Find("Tag_1");

//Enumeration type properties

AccessMode accessMode = hmiTag.AccessMode;

UpdateScope scope = hmiTag.UpdateScope;

//Comment property (multilingual text)

string culture = "en-US";

//get the language based on given culture. Culture is standard and it should have correct value.

Language language = GetDeviceProject().LanguageSettings.Languages.Find(new System.Globalization.CultureInfo(culture));

//get comment as multilingual text.

MultilingualText multiLingualComment = hmiTag.Comment;

//get all text items from comment property.

MultilingualTextItemComposition texts = multiLingualComment.Items;

//find text from text list based on language.

MultilingualTextItem textItemEnglish = texts.Find(language);

//get value in selected culture.

string commentEng = textItemEnglish.Text;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Assigning user defined datatype to tag (RT Unified)

##### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To assign user defined datatype as datatype to tag without connection modify the following program code:

private void AssignUdtWithoutConnection()

{

//Assigning three types of UDT to tag by calling DataType property of tag

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition tags = hmiSoftware.HmiTags;

tags[0].DataType = @"\Project library\Types\HmiUdt_Int\V 0.0.1";  
tags[1].DataType = @"\Project library\Types\HmiUdt_byte\V 0.0.1";  
tags[2].DataType = @"\Project library\Types\New folder_2\HmiUdt_string\V 0.0.1";

tags[3].DataType = @"\Project library\Types\New folder_1\HmiUdt_string\V 0.0.1";

tags[4].DataType = @"\Project library\Types\New folder_3\HmiUdt_string\V 0.0.1";

}

clipboard

To assign user defined datatype as datatype to tag with connection modify the following program code:

private void AssignUdtWithConnection()

{

//Assigning user defined datatype to tag by calling DataType property of tag with connection

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition tags = hmiSoftware.HmiTags;

tags[0].Connection = "Connection_1";

tags[0].DataType = @"\Project library\Types\New folder_3\HmiUdt_string\V 0.0.1";

}

clipboard
> **Note**
>
> To assign user defined datatype to tag with connection you should have the correct PLC type connection exist in TIA Portal project; otherwise, a recoverable exception is thrown.

To assign PLC user defined datatype as datatype to tag with connection modify the following program code:

private void AssignPlcUdtWithConnection()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagComposition tags = hmiSoftware.HmiTags;

tags[0].Connection = "HMI_Connection_1";

tags[0].Data Type = "PlcTag_1";

}

clipboard
> **Note**
>
> To assign PLC userdefined datatype as datatype to tag you should have PLC and HMI devices exist in the same TIA Portal project and have integrated connection exist between them.
>
> The PLC device also needs to have a PLC tag with a UDT type.

---

**See also**

[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing tag member properties of  user defined type (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access member properties of user defined datatype for tag modify the following program code:

private static void GetProperties(HmiTagComposition hmiTags)

{

foreach (HmiTag hmiTag in hmiTags)

{

switch(hmiTag.TagType)

{

case HmiTagType.Simple

Console.WriteLine("Name : "+ hmiTag.Name);

GetSimpleTagProperties(HmiTag hmiTag)

break;

case HmiTagType.UDT;

case HmiTagType.Array;

GetProperties(hmiTag.Members); //recursive call to current function.

break;

}

}

}

//The GetSimpleTagProperties()uses hmiTag object as a parameter to access the properties of tag.

private static void GetSimpleTagProperties(HmiTag hmiTag)

{

Console.WriteLine("Name : " +hmiTag.Name);

Console.WriteLine("Date type : " +hmiTag.DataType);

// List the properties of hmi tag

//

//...

}

//The GetProperties()uses hmiTag.Members object as a parameter to access the properties of tag members.

private static void GetProperties(HmiTag hmiTag.Members)

{

Console.Writeline("Name : " +hmiTag.Members.Name);

Console.Writeline("Date type: " +hmiTag.Members.DataType);

// List the properties of hmi tag members

//...

//...

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing cross reference service on tags (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the cross reference service through GetService() on tag object modify the following program code:

private void getCrossReferenceServiceforTag()

{

SoftwareContainer softwareContainer = deviceItem.GetService&lt;SoftwareContainer&gt;();

HmiSoftware hmiSoftware = softwareContainer.Software as HmiSoftware;  //Accessing lower levels until we reach the HmiTagComposition.

HmiTagComposition hmiTagComposition = hmiSoftware.HmiTags;

HmiTag hmiTag = hmiTagComposition.Find("Tag_1");

if (hmiTag != null)

{

try

{

CrossReferenceService crossReferenceService = hmiTag.GetService&lt;CrossReferenceService&gt;();

......

}

catch (Exception e)

{

Console.WriteLine(e.Message);

}

}

}

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[HMISoftware object (RT Unified)](#hmisoftware-object-rt-unified)

### TagTables (RT Unified)

This section contains information on the following topics:

- [Description TagTables (RT Unified)](#description-tagtables-rt-unified)
- [TagTables.Create() (RT Unified)](#tagtablescreate-rt-unified)
- [TagTables.Delete() (RT Unified)](#tagtablesdelete-rt-unified)
- [Accessing tag table properties (RT Unified)](#accessing-tag-table-properties-rt-unified)
- [Exporting and importing tag tables (RT Unified)](#exporting-and-importing-tag-tables-rt-unified)
- [TagTable.Tags.Export() (RT Unified)](#tagtabletagsexport-rt-unified)
- [TagTable.Tags.Import() (RT Unified)](#tagtabletagsimport-rt-unified)

#### Description TagTables (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To perform a task on a tag table you can either use enumerate tag tables or use Find():

private void TagTableBrowse()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// User can navigate all the tag tables of device

HmiTagTableComposition tagTables = hmiSoftware.TagTables;

foreach (HmiTagTable tagTable in tagTables)

{

//Working with tag table

}

}

clipboard

To access a single tag table by name modify the following program code:

private void TagTableSearch()

{

HmiSoftware hmiSoftware = GetHmiSoftware();

// Search for a specific tag table name from a list of tag tables

string tagTableName = "TagTable_1"

HmiTagTableComposition tagTables = hmiSoftware.TagTables;

HmiTagTable tagTableObj = tagTables.Find("tagTableName");

//Working with tag table

}

clipboard

##### Working with tag tables

You can perform the following tasks with tag tables while using TIA Portal Openness:

- Creating tag tables:[TagTables.Create()](#tagtablescreate-rt-unified))
- Deleting tag tables:[TagTables.Delete()](#tagtablesdelete-rt-unified)
- Exporting tags: [TagTable.Tags.Export()](#tagtabletagsexport-rt-unified)
- Importing tags: [TagTable.Tags.Import()](#tagtabletagsimport-rt-unified)
- Tag tables properties: [Accessing tag table properties](#accessing-tag-table-properties-rt-unified)

> **Note**
>
> Querying errors is not supported for tag tables as they don’t have any properties which can be in error state.

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### TagTables.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible

  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a tag table with Create() of HmiTagTableComposition class modify the following program code

private void TagTableCreate()

{

//Create tag table with name "TagTable_1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagTableComposition tagTables = hmiSoftware.TagTables;

HmiTagTable hmiTagTable = tagTables.Create("TagTable_1");

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### TagTables.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a tag table with Delete() of HmiTagTable class modify the following program code:

private void TagTableDelete()

{

//Delete tag table with name "TagTable_1"

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagTableComposition tagTables = hmiSoftware.TagTables;

HmiTagTable tagTable = tagTables.Find("TagTable_1");

tagTable.Delete();

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing tag table properties (RT Unified)

##### Property

The following properties are supported in tag tables:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the name of tag table | R/W |
| Tags | HmiTagComposition | Specifies the list of tags | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the properties of a tag table modify the following program code :

private void TagTableProperties()

{

//Set and Get the "Name" properties of tag table.

HmiSoftware hmiSoftware = GetHmiSoftware();

HmiTagTableComposition tagTables = hmiSoftware.TagTables;

HmiTagTable tagTable = tagTables.Find("TagTable_1");

tagTable.Name = "NewTagTable";

string name = tagTable.Name;

}

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Exporting and importing tag tables (RT Unified)

##### Introduction

You can use TIA Portal Openness to export and import data for a tag table. In case of import new objects are created under unified device if necessary. The export file is a text file using a simplified format: WinCC ML, which is based on YAML format. You can modify the file according to your requirements.

In TIA Portal Openness the export and Import method are implemented at the tag table level.

> **Note**
>
> It is recommended that you should rectify all compilation errors related to tags in tag tables which shall be exported.

##### Export of tags

Using Export functionality, the following types of tags will be exported:

- Tags

  - Internal tags
  - External tags
- Structure tags with their elements

  - HMI user data type (UDT)
  - PLC user defined datatype (UDT)
- Array Tags with their elements

  - Internal array tags
  - External array Tags

> **Note**
>
> When an array of WChar and Char datatype is exported then no tag elements are displayed in the exported WinCCML file and the tags are displayed in the simple tags category. When these tags are imported back, they are added as array tags as expected.

> **Note**
>
> When a structure tag is exported the reference name of the PLC structure tag type will be appended to the PLC name.

##### Contents of Export location

When a tag table is exported to a particular folder location, the following contents will be created:

- Tag table file with the extension ".hmi.yml" and user defined name in the example "Default tag table.hmi.yml".
- A file "NameData.yml" This file does not contain any data required for executing the import and export
- A folder ".ile" This folder does not contain any data required for executing the import and export
- A file with the extension "def.hmi.yml" will be created when a tag table with structure tags is exported. This file will contain the structure types definition

![Contents of Export location](images/158167396235_DV_resource.Stream@PNG-en-US.png)

##### YAML File structure

The structure of the YAML file will be as seen below. It can be opened &amp; edited in any simple text editor like Notepad, Microsoft word, Notepad++, etc. :

The overall configuration will be seen in property name &amp; property value format which makes it easy to read and modify the configuration.

#Version: 2.0

SimpleTags:

Tag_1:

AccessMode: SymbolicAccess

AcquisitionCycle: T1s

Address: 0001:TS:50.73A8C75D.C

Connection: HMI_Connection_2

ControllerDataType: 1006

DataType: Int

InitialMaxValue: 444

InitialMinValue: 44

MaxLength: 2

PlcTag: PLCTag_1

Tag_2:

AccessMode: AbsoluteAccess

AcquisitionCycle: T1s

Address: 0001:CL:%IW0

Connection: HMI_Connection_1

ControllerDataType: 1006

DataType: Int

MaxLength: 2

PlcTag: PLCTag

SymbolicAddress: '%IW0'

Tag_3:

AccessMode: SymbolicAccess

AcquisitionCycle: T1s

Address: $0001:TS:8A0E0001.CDB29A10.A.#{0}

Connection: HMI_Connection_1

ControllerDataType: 1009

DataType: DInt

MaxLength: 4

PlcTag: Data_block_1.Element1[0]

SymbolicAddress: Data_block_1.Element1[Tag_1]

Tag_4

AccessMode: SymbolicAccess

AcquisitionCycle: T1s

Address: 0001:TS:8A0E0001.CDB29A10.A.1

Connection: HMI_Connection_1

ControllerDataType: 1009

DataType: DInt

MaxLength: 4

PlcTag: Data_block_1.Element1[1]

clipboard

##### Property

The below table shows the mapping of properties name in TIA Portal with the properties name being exported in WinCCML file:

| TIA Portal Property Name | WinCCML Property Name | Remark |
| --- | --- | --- |
| Name | Heading of object |  |
| DataType | ControllerDataType | For connections other than Internal, this property will be used during import, to assign datatype to the tag. |
| Connection | Connection |  |
| PLC Name | Derived from PLC Tag property |  |
| PLC Tag | PlcTag |  |
| Address | SymbolicAddress | Property named as 'Address' is ignored by TIA Portal ES during Import |
| Access Mode | AccessMode |  |
| HMI data type | DataType | For Internal connection Tags, this property will be used during import, to assign datatype to the tag. |
| Length | MaxLength |  |
| Acquisition cycle | AcquisitionCycle |  |
| Acquisition mode | AcquisitionMode |  |
| Upper 2 (Tag) | MaxValueTag |  |
| Lower 2 (Tag) | MinValueTag |  |
| Upper 2 (Constant) | InitialMaxValue |  |
| Lower 2 (Constant) | InitialMinValue |  |
| Linear scaling | Derived from PLC/Hmi Start/End Values | This is set as True if PLC/Hmi Start/End Values are present |
| End value PLC | PLCMaxValue |  |
| Start value PLC | PLCMinValue |  |
| End value HMI | HMIMaxValue |  |
| Start value HMI | HMIMinValue |  |
| Start value | InitialValue |  |
| Update ID | ID |  |
| Persistent | Persistent |  |
| Substitute value | SubstituteValue |  |
| Use Substitute Value | SubstituteValueUsage |  |
| GMP relevant | GMPRelevant |  |
| Type of confirmation | ConfirmationType |  |
| Comment required | Derived from ConfirmationType value |  |
| Scope | Scope |  |
| Comment | Comment |  |
|  | Address |  |
|  | Offset |  |
|  | Slope |  |

#### TagTable.Tags.Export() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To export a tag table modify the following program code:

DirectoryInfo directoryInfo = new DirectoryInfo("D:\\Data Exchange");

HmiTagTableComposition tables = GetHmiSoftware(currentProject).TagTables;

HmiTagTable tagTable = tables.Find(tagTableName.Text);

\\Create a file name "ExportedTable" in specific directory by using Export() that includes the details of tag table.

IList&lt;FileInfo&gt; Exportresult = tagTable.Tags.Export(directoryInfo,"ExportedTable").ToList();

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### TagTable.Tags.Import() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To import a tag tables modify the following program code:

DirectoryInfo directoryInfo = new DirectoryInfo("D:\\Data Exchange");

HmiSoftware ImportHMISoftware = GetHmiSoftware(currentProject);

HmiTagTableComposition tables = ImportHMISoftware.TagTables;

HmiTagTable tagTable = tables.Find(importedTagTable.Text);

bool ImportResult = tagTable.Tags.Import(directoryInfo);

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### TagTableGroups (RT Unified)

This section contains information on the following topics:

- [Description TagTableGroups (RT Unified)](#description-tagtablegroups-rt-unified)
- [TagTableGroups.Create() (RT Unified)](#tagtablegroupscreate-rt-unified)
- [TagTableGroups.Delete() (RT Unified)](#tagtablegroupsdelete-rt-unified)
- [Accessing tag table groups properties (RT Unified)](#accessing-tag-table-groups-properties-rt-unified)

#### Description TagTableGroups (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access a tag table group using the Find() method modify the following program code:

privat void SearchTagTableGroups(HmiSoftware hmiSoftware)

{

HmiTagTableGroupComposition tagTableGroups = hmiSoftware.TagTableGroups;

HmiTagTableGroup tagTableGroupFindLevelOne = hmiSoftware.tagTableGroups.Find("Group_2");

MessageBox.Show("Found at 1st level: " + tagTableGroupFindLevelOne.Name);

}

clipboard

##### Working with tag table groups

You can perform the following tasks with tag groups while using TIA Portal Openness:

- Creating tag table groups:[TagTableGroups.Create()](#tagtablegroupscreate-rt-unified)
- Deleting tag table groups: [TagTableGroups.Delete()](#tagtablegroupsdelete-rt-unified)
- Tag table groups properties: [Accessing tag table groups properties](#accessing-tag-table-groups-properties-rt-unified)

#### TagTableGroups.Create() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To create a tag table group (HmiTagTableGroup) with Create() method of class HmiTagTableGroupComposition modify the following program code:

private void CraeteTagTableGroup(HmiSoftware hmiSoftware)

{

HmiTagTableGroupComposition tagTableGroups = hmiSoftware.TagTableGroups;

int count = tagTableGroups.Count;

HmiTagTableGroup tagTableGroup1stLevel = hmiSoftware.TagTableGroups.Create("Group_1stLevel");

}

clipboard

#### TagTableGroups.Delete() (RT Unified)

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To delete a tag table group modify the following program code:

private void DeleteTagTableGroup(HmiSoftware hmiSoftware)

{

HmiTagTableGroupComposition tagTableGroups = hmiSoftware.TagTableGroups;

HmiTagTableGroup tagTableGroupFindLevelOne = hmiSoftware.TagTableGroups.Find("Group_2");

MessageBox.Show("Found at 1st level: " + tagTableGroupFindLevelOne.Name);

tagTableGroupFindLevelOne.Delete();

}

clipboard

#### Accessing tag table groups properties (RT Unified)

##### Property

The following properties are supported in tag table group:

| Property name | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Specifies the tag table group name | R/W |
| Groups | HmiTagTableGroupComposition | Specifies the list of tag table groups | R |
| TagTables | HmiTagTableComposition | Specifies the list of tag tables | R |

##### Requirement

- The HMI Software object is accessible  
  See [Description HMISoftware](#description-hmisoftware-rt-unified)

##### Program code

To access the Groups property of tag table groups of a device modify the following program code:

private void AccessTagTableGroupProperties(HmiSoftware hmiSoftware)

{

HmiTagTableGroupComposition tagTableGroups = hmiSoftware.TagTableGroups;

MessageBox.Show(tagTableGroups.Count.ToString());

HmiTagTableGroupComposition tagTableGroup2ndLevel = hmiSoftware.TagTableGroups[0].Groups;

MessageBox.Show(tagTableGroup2ndLevel.Count.ToString());

}

clipboard

## Accessing further objects (RT Unified)

This section contains information on the following topics:

- [Rename properties and data types (RT Unified)](#rename-properties-and-data-types-rt-unified)
- [Querying errors (RT Unified)](#querying-errors-rt-unified)
- [Accessing simple dynamic (RT Unified)](#accessing-simple-dynamic-rt-unified)
- [Accessing device name of HMI Panel (RT Unified)](#accessing-device-name-of-hmi-panel-rt-unified)
- [Accessing common plant model hierarchies (RT Unified)](#accessing-common-plant-model-hierarchies-rt-unified)
- [Accessing common plant model instance (RT Unified)](#accessing-common-plant-model-instance-rt-unified)
- [Accessing properties for interface/logging tags of plant object instances (RT Unified)](#accessing-properties-for-interfacelogging-tags-of-plant-object-instances-rt-unified)
- [Checking license for access Unified device (RT Unified)](#checking-license-for-access-unified-device-rt-unified)
- [Getting Cross References for WinCC Unified (RT Unified)](#getting-cross-references-for-wincc-unified-rt-unified)
- [Working with dynamization &amp; events for screen/screen items using scripts (RT Unified)](#working-with-dynamization-events-for-screenscreen-items-using-scripts-rt-unified)
- [Working with dynamization for screens/screen items (RT Unified)](#working-with-dynamization-for-screensscreen-items-rt-unified)

### Rename properties and data types (RT Unified)

#### Introduction

In ES TIA Portal Openness, appropriate changes are made in property names and data types, so that it is similar to runtime Openness model.

To achieve it, changes are made in all subsystems for example Alarm, Tag, Connection, and Logging.

To have consistency in naming the property and its data type, it is necessary that prefix Hmi is used for defining their type and name of property should not have this prefix.

#### Change in property name and data type

Following table shows required changes to have consistent name and data type for composition.

| Hmi Object Name | Property Name | Property New Name | Property Data type | Property New Data Type |
| --- | --- | --- | --- | --- |
| Analog Alarm | AnalogAlarms | - | AnalogAlarmComposition | HmiAnalogAlarmComposition |
| Discrete Alarm | DiscreteAlarms | - | DiscreteAlarmComposition | HmiDiscreteAlarmComposition |
| OPC UA Alarm &amp; Condition types | OpcUaAlarmTypes | - | OpcUaAlarmTypeComposition | HmiOpcUaAlarmTypeComposition |
| Alarm Class | AlarmClasses | - | AlarmClassComposition | HmiAlarmClassComposition |
| Tag Table | HmiTagTables | TagTables | HmiTagTableComposition | - |
| Tag | HmiTags | Tags | HmiTagComposition | - |
| System Tag | HmiSystemTags | SystemTags | HmiSystemTagComposition | - |
| Logging Tag | LoggingTags | - | LoggingTagComposition | HmiLoggingTagComposition |
| Connection | HmiConnections | Connections | HmiConnectionComposition | - |
| Data Log | DataLogs | - | DataLogComposition | HmiDataLogComposition |
| Alarm Log | AlarmLogs | - | AlarmLogComposition | HmiAlarmLogComposition |
| Plant Object Interface | PlantObjectTags | - | PlantObjectInterfaceComposition | - |
| Screen | Screens | - | HmiScreenComposition | - |

> **Note**
>
> With dash (-) character in columns 'New Name' and 'New Data Type' in above table shows no change is required.

#### Changes in name of HmiObject classes

Following table shows required changes to have consistent name for classes for Hmi Object.

| Hmi Object Name | Class Name | New Class Name |
| --- | --- | --- |
| Analog Alarm | AnalogAlarm | HmiAnalogAlarm |
| Discrete Alarm | DiscreteAlarm | HmiDiscreteAlarm |
| OPC UA Alarm &amp; Condition types | HmiOpcUaAlarmType | HmiOpcUaAlarmType |
| Alarm Class | AlarmClass | HmiAlarmClass |
| Tag Table | HmiTagTable | - |
| Tag | HmiTag | - |
| Connection | HmiConnection | - |
| RuntimeSettings | RuntimeSetting | HmiRuntimeSetting |
| Data Log | DataLog | HmiDataLog |
| Alarm Log | AlarmLog | HmiAlarmLog |
| Logging Tag | LoggingTag | HmiLoggingTag |
| System Tag | HmiSystemTag | - |
| Screen | HmiScreen | - |
| Plant Object interface | PlantObjectInterface | - |

> **Note**
>
> With dash (-) character in columns 'New Class Name' in above table shows no change is required.

### Querying errors (RT Unified)

#### Introduction

You can use TIA Portal Openness to get error information about properties for the following WinCC objects:

- Analog Alarm
- Discrete Alarm
- Alarm Class
- Data Log
- Alarm Log
- Tag
- Connection
- Logging Tag
- Device runtime settings
- OPC UA Alarms

> **Note**
>
> This feature is not applicable to System Tag and Tag Table as they don’t have any property which can be in error state.

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project).
- Access to HMI Unified Software object  
  See [HMI Unified Software object](#description-hmisoftware-rt-unified)

#### Program code

Modify the following program code to query errors for tag, alarms, runtime setting and screens:

`//For Tag`

`HmiSoftware hmiSoftware = GetHmiSoftware();`

`HmiTagComposition hmiTags = hmiSoftware.HmiTags;`

`HmiTag hmiTag = hmiTags.Find("Tag-l");`

`if(hmiTag != null)`

`{`

`//validate method usage`

`IList<HmiValidationResult> validationResult = hmiTag.Validate();`

`if (validationResult = null && validationResult.Count > 0)`

`{`

`foreach (HmiValidationResult propertyErrors in validationResult)`

`{`

`//browse error for different property`

`string propertyName = propertyErrors. PropertyName;`

`foreach (string propertyError in propertyErrors.Errors)`

`{`

`//work with propertyerrors`

`}`

`}`

`}`

`}`

`//For Discrete Alarm`

`HmiSoftware hmiSoftware = ...;`

`HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;`

`HmiDiscreteAlarm alarm = discreteAlarms.Find("Alarm_1");`

`if (alarm != null)`

`{`

`//Validate Method Usage`

`Ilist<HmiValidationResult> validationResult = alarm.Validate();`

`if (validationResult != null && validationResult.Count > 0)`

`{`

`foreach (HmiValidationResult propertyErrors in validationResult)`

`{`

`//browse error for different property`

`string propertyName = propertyErrors.PropertyName;`

`foreach (string propertyError in propertyErrors.Errors)`

`{`

`//work with property errors`

`}`

`}`

`}`

`}`

`//For Runtime Setting`

`HmiSoftware hmiSoftware = ...;`

`HmiRuntimeSetting runtimeSettings = hmiSoftware.RuntimeSettings;`

`//Validate Method Usage`

`Ilist<HmiValidationResult> validationResult = runtimeSettings.Validate();`

`if (validationResult != null && validationResult.Count > 0)`

`{`

`foreach (HmiValidationResult propertyErrors in validationResult)`

`{`

`//browse error for different property`

`string propertyName = propertyErrors.PropertyName;`

`foreach (string propertyError in propertyErrors.Errors)`

`{`

`//work with property errors`

`}`

`}`

`}`

`// List of Many objects (Tag, Alarm, etc,)`

`HmiSoftware hmiSoftware = ...;`

`IList<IValidator> objectsToValidate = new List<IValidator>();`

`//Put tags in validation list`

`HmiTagComposition hmiTags = hmiSoftware.Tags;`

`foreach (HmiTag hmiTag in hmiTags)`

`{`

`objectsToValidate.Add(hmiTag);`

`}`

`//Put alarms in validation list`

`HmiDiscreteAlarmComposition discreteAlarms = hmiSoftware.DiscreteAlarms;`

`foreach (HmiDiscreteAlarm discreteAlarm in discreteAlarms)`

`{`

`objectsToValidate.Add(discreteAlarm);`

`}`

`//Put RuntimeSettings in validation list`

`objectsToValidate.Add(hmiSoftware.RuntimeSettings);`

`foreach (IValidator validator in objectsToValidate)`

`Ilist<HmiValidationResult> validationResult = validator.Validate();`

`if (validationResult != null && validationResult.Count > 0)`

`{`

`foreach (HmiValidationResult propertyErrors in validationResult)`

`{`

`//browse error for different property`

`string propertyName = propertyErrors.PropertyName;`

`foreach (string propertyError in propertyErrors.Errors)`

`{`

`//work with property errors`

`}`

`}`

`}`

`}`

clipboard

---

**See also**

[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)

### Accessing simple dynamic (RT Unified)

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.   
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Access to HMI Software object  
  See [HMI Unified Software object](#description-hmisoftware-rt-unified)

#### Introduction

You can use the TIA Portal Openness to have complete access to the dynamization by simple dynamics. The Screen &amp; its Screen items can be dynamized using one of the following simple dynamization options :

- Range
- Multiple bits
- Single bit

#### Program code

`var hmiSoftware = GetScadaHmiSoftware();`

`var Screen1 = hmiSoftware.Screens[0];`

`//Range :`

`var screenItem0 = Screen1.ScreenItems.FirstOrDefault(x => x.Name == "Circle_1");`

`string propertyName = "BackColor";`

`var tagDynamization = screenItem0.Dynamizations.Where(x => x.PropertyName == propertyName).FirstOrDefault() as TagDynamization;`

`var mappingTable = tagDynamization.ValueConverter.MappingTable;`

`var entries = mappingTable.Entries;`

`mappingTable.ConditionType = ConditionType.Range;`

`//First Row Entry :`

`var rangeEntry1 = entries.Create<MappingTableEntryRange>(); //Create a new row`

`rangeEntry1.From = 0; // Add a From entry`

`rangeEntry1.To = 50; // Add a To Entry`

`rangeEntry1.Value = Color.Red; // Set the property value`

`rangeEntry1.Flashing = true; // Select the Flashing state`

`rangeEntry1.FlashingRate = FlashingRate.Medium; // Select the Flashing rate`

`rangeEntry1.AlternateValue = Color.Orange; // Select the Flashing color`

`//Second Row Entry :`

`var rangeEntry2 = entries.Create<MappingTableEntryRange>(); //Create a new row`

`rangeEntry2.From = 51; // Add a From entry`

`rangeEntry2.To = 80; // Add a To Entry`

`rangeEntry2.Value = Color.Yellow; // Set the property value`

`rangeEntry2.Flashing = true; // Select the Flashing state`

`rangeEntry2.FlashingRate = FlashingRate.Medium; // Select the Flashing rate`

`rangeEntry2.AlternateValue = Color.YellowGreen; // Select the Flashing color`

`//Third Row Entry :`

`var rangeEntry3 = entries.Create<MappingTableEntryRange>(); //Create a new row`

`rangeEntry3.From = 81; // Add a From entry`

`rangeEntry3.To = 100; // Add a To Entry`

`rangeEntry3.Value = Color.Green; // Set the property value`

`rangeEntry3.Flashing = false; // Select the Flashing state`

`//Fourth Row Entry :`

`var rangeEntry4 = entries.Create<MappingTableEntryRange>(); //Create a new row`

`rangeEntry4.From = 101; // Add a From entry`

`rangeEntry4.To = 101; // Add a To Entry`

`rangeEntry4.Value = Color.Green; // Set the property value`

`rangeEntry4.Flashing = true; // Select the Flashing state`

`rangeEntry4.FlashingRate = FlasingRate.Medium;`

`rangeEntry4.AlternateValue = Color.LightGreen`;

`//Second Row Entry - Bit number 4 :`

`var multibitEntries2 = entries.Create(BitDynamizationType.MultiBit);`

`var multibitEntry2 = multibitEntries2[0];`

`ulong multibitCondition2 = 16; // Condition = 2^(Bit No.) = 2^4 => 16`

`ulong multibitRelevant2 = 20; // Relevant = Decimal equivalent of no. of bits being configured = 0001 0100 => 20`

`multibitEntry2.Update(multibitCondition2, multibitRelevant2);`

`multibitEntry2.Value = Color.Green;`

`multibitEntry2.Flashing = false;// Single Bit`

`var hmiSoftware = GetScadaHmiSoftware();`

`var Screen1 = hmiSoftware.Screens[0];`

`var screenItem0 = Screen1.ScreenItems.FirstOrDefault(x => x.Name == "Process control_1");`

`string propertyName = "Visible";`

`var tagDynamization = screenItem0.Dynamizations.Where(x => x.PropertyName == propertyName).FirstOrDefault() as TagDynamization;`

`var mappingTable = tagDynamization.ValueConverter.MappingTable;`

`var entries = mappingTable.Entries;`

`var singleBitEntries = entries.Create(BitDynamizationType.SingleBit);`

`mappingTable.ConditionType = ConditionType.Singlebit; // Select Condition type`

`//State 0 for Bit 15 :`

`var singleBitEntry1 = singleBitEntries[0]; // Select the 1st Entry - Off State of the bitulong singlebitCondition1 = 0; // Condition value = [Bit State x 2^ Bit number] => (0 x 2^15 = 0)ulong singlebitRelevant1 = 32768; // Relevant = Decimal equivalent of the Single bit being configured = 1000 0000 0000 0000 => 32768`

`singleBitEntry1.Update(singlebitCondition1, singlebitRelevant1);`

`singleBitEntry1.Value = true;//State 1 for Bit 15 :`

`var singleBitEntry2 = singleBitEntries[1]; // Select the 2nd Entry - ON State of the bit`

`ulong singlebitCondition2 = 32768; // Condition value = [Bit State x 2^ Bit number] => (1 x 2^15 = 32768)`

`ulong singlebitRelevant2 = 32768; // Relevant = Decimal equivalent of the Single bit being configured = 1000 0000 0000 0000 => 32768`

`singleBitEntry2.Update(singlebitCondition2, singlebitRelevant2);`

`singleBitEntry2.Value = false;`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)

### Accessing device name of HMI Panel (RT Unified)

#### Introduction

You can use the TIA Portal Openness application to read and write the device names of the unified and non-unified HMI device.

#### Properties

The following attribute can be accessed and edited in HMI device:

| Attribute | Data type | Description | Access |
| --- | --- | --- | --- |
| Name | String | Name of HMI device | R/W |

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.

  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal).
- A project is open.

  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Program code

`Tiaproject = tiaPortal.Projects[0];`

`var deviceUnderTest = Tiaproject.Devices[0];`

`//Set`

`deviceUnderTest.Name = "Test1";`

`//Get`

`var deviceName = deviceUnderTest.Name;`

`foreach (var deviceItem in deviceUnderTest.DeviceItems)`

`{`

`//Set`

`deviceItem.Name = "TestDeviceItem1";`

`//Get`

`var deviceName = deviceItem.Name;`

`}`

clipboard

### Accessing common plant model hierarchies (RT Unified)

This section contains information on the following topics:

- [Working with plant view (RT Unified)](#working-with-plant-view-rt-unified)
- [Working with plant view nodes (RT Unified)](#working-with-plant-view-nodes-rt-unified)
- [Enumerating plant view (RT Unified)](#enumerating-plant-view-rt-unified)
- [Working with plant view to device (RT Unified)](#working-with-plant-view-to-device-rt-unified)

#### Working with plant view (RT Unified)

##### Introduction

You can perform the following tasks related to plant view while using TIA Portal Openness:

- Create plant view
- Delete plant view
- Rename plant view

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to create a plant view:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Create("ABCManufacturingPlant");`

clipboard
> **Note**
>
> You can create only one plant view inside a project.

Modify the following program code to delete or remove a plant view:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`plantView.Delete();`

clipboard

Modify the following program code to rename a plant view by updating the 'Name' property:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView`

`plantView = plantViews.Find("ABCManufacturingPlant");`

`plantView.Name = "New_PlantView_Name";`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Working with plant view nodes (RT Unified)

##### Introduction

You can perform the following tasks related to plant view node while using TIA Portal Openness:

- Create plant view nodes
- Delete plant view nodes
- Rename plant view nodes

##### Properties

The following properties are supported in Plant View Node using TIA Portal Openness:

| Property Name | Data Type | Accessibility |
| --- | --- | --- |
| HierarchyPath | String | R |
| PlantObject | Siemens.Engineering.HmiUnified.Cpm.PlantObject | R |
| Name | String | R/W |
| PlantView | String | R |
| ViewPath | String | R |
| PlantViewNodes | PlantViewNodeComposition | R |

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to create plant view node under a plant view:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNodeComposition`

`viewNodes` 
**=** 
`plantView.PlantViewNodes;`

`PlantViewNode`

`mixingNode = viewNodes.Create("Mixing");`

clipboard

Modify the following program code to create plant view node under another plant view node:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNodeComposition viewNodes = plantView.PlantViewNodes;`

`PlantViewNode mixingNode = viewNodes.Create("Mixing");`

`PlantViewNode motorNode = mixingNode.Create("Motor");`

clipboard
> **Note**
>
> You can create any number of plant view nodes inside a plant view or plant view node itself.

Modify the following program code to remove or delete a plant view node:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Find("Mixing");`

`mixingNode.Delete();`

clipboard

Modify the following program code to rename a plant view node by updating the 'Name' property:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews`
**.**
`Find("ABCManufacturingPlant");`

`PlantViewNodeComposition viewNodes = plantView.PlantViewNodes;`

`PlantViewNode mixingNode = viewNodes.Create("Mixing");`

`mixingNode.Name = "New_PlantViewNode_Name";`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Enumerating plant view (RT Unified)

##### Introduction

You can use the TIA Portal Openness to enumerate plant view present on given project in TIA Portal.

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to enumerate all plant views of the project:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`foreach (var item in plantViews)`

`{`

`// work with plant views (currently only 1 plant view can be created inside a project)`

`}`

clipboard

Modify the following program code to find a plant view from plant view list based on the name:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView`
`plantView = plantViews.`Find`("ABCManufacturingPlant");`

clipboard

Modify the following program code to find a plant view from plant view list based on index:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView`

`plantView = plantViews[0];`

clipboard

Modify the following program code to find plant view node from the plant view list based on the hierarchy path of the required plant view node:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantViewNode plantViewNode = plantViews.FindPlantViewNode("ABCManufacturingPlan\Mixing\Motor");`

clipboard

Modify the following program code to find a plant view node from the plant view node list based on the name of the plant view:

`PlantViewNodeComposition plantViewNodes = m_tiaPortalApp.Projects[0].PlantViews[0].PlantViewNodes;`

`PlantViewNode plantViewNode = plantViewNodes.Find("Mixing");`

clipboard

Modify the following program code to enumerate all plant view nodes list available inside plant view:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantViewNodeComposition`

`nodes = plantView.PlantViewNodes;`

`foreach (var item in nodes)`

`{`

`// work with plant view nodes inside plant view`

`}`

clipboard

Modify the following program code to enumerate all plant view nodes available inside any hierarchial level:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantViewNodeComposition nodes = plantView.PlantViewNodes;`

`PlantViewNodeComposition subNodes = nodes[2].PlantViewNodes;`

`foreach (var item in subNodes)`

`{`

`// work with plant view nodes inside 2nd node within the plant view`

`}`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Working with plant view to device (RT Unified)

##### Introduction

You can perform the following tasks related to accessing plant view hierarchies and plant object while using TIA Portal Openness:

- Assign device to the plant view
- Change device to the plant view
- Remove device to the plant view

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to assign a device to the plant view by setting the AssignedHmiDevice property:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Create("ABCManufacturingPlant");`

`plantView.AssignedHmiDevice = "HMI_RT_1";`

clipboard

Modify the follwing program code to change a device to the plant view by setting a device name to AssignedHmiDevice property.

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Create("ABCManufacturingPlant");`

`plantView.AssignedHmiDevice = "HMI_RT_2";`

clipboard

Modify the following program code to remove device to the plant view by setting a blank device name to AssignedHmiDevice property.

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Create("ABCManufacturingPlant");`

`plantView.AssignedHmiDevice = string.Empty;`

clipboard
> **Note**
>
> To remove the device, use only string.empty. Passing NULL or whitespace (" "), will be treated as a device name and will return device not found error message

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Accessing common plant model instance (RT Unified)

This section contains information on the following topics:

- [Working with CPM object instance (RT Unified)](#working-with-cpm-object-instance-rt-unified)
- [Working with plant view nodes of CPM object instance (RT Unified)](#working-with-plant-view-nodes-of-cpm-object-instance-rt-unified)
- [Enumerating interface tags of CPM object instance (RT Unified)](#enumerating-interface-tags-of-cpm-object-instance-rt-unified)

#### Working with CPM object instance (RT Unified)

##### Introduction

You can perform the following tasks related to access CPM instance based on CPM type while using TIA Portal Openness:

- Create CPM object instances
- Delete CPM object instances
- Rename CPM object instances

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Create a Plant

##### Program code

Modify the following program code to create CPM object instance:

`// Instance inside plant view`

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Create("ABCManufacturingPlant");`

`plantView.AssignedHmiDevice = "HMI_RT_1";`

`PlantViewNodeComposition nodes = plantView.PlantViewNodes;`

`PlantViewNode node = nodes.Create("ObjectLevel1", "Plant_Object_Type_1");`

`//Instance inside plant view node`

`PlantViewNode`

`mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Plant_Object_Type_1");`

clipboard

Modify the following program code to remove or delete a CPM object instance:

`PlantViewNode mixingNode = plantView.PlantViewNodes.Find("Mixing");`

`PlantViewNode`

`mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Find("IngredientMixer");`

`mixerObject.Delete();`

clipboard

Modify the following program code to rename a CPM object instance by updating the 'Name' property:

`PlantViewNode mixingNode = plantView.PlantViewNodes.Find("Mixing");`

`PlantViewNode`

`mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Find("IngredientMixer");`

`mixerObject.Name`

`= "New_PlantViewNode_Name";`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Working with plant view nodes of CPM object instance (RT Unified)

##### Introduction

You can perform the following tasks related to access plant view nodes of CPM object instances while using TIA Portal Openness:

- Create plant view nodes
- Delete plant view nodes
- Rename plant view nodes

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to create a plant view node inside a CPM object instance

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView` 
**=** 
`plantViews.Find("ABCManufacturingPlant");`

`PlantViewNode`

`mixerObject = plantView.PlantViewNodes.Create("ObjectLevel1", "Plant_Object_Type_1");`

`PlantViewNode`

`mixingNode = mixerObject.PlantViewNodes.Create("Mixing");`

clipboard
> **Note**
>
> You can create any number of plant view node inside a CPM object

Modify the following program code to create a CPM object instance inside a plant view node:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = mixingNode.PlantViewNodes.Create("ObjectLevel1", "Plant_Object_Type_1");`

clipboard
> **Note**
>
> You can create any number of CPM object instances inside a plant view node

Modify the following program code to remove or delete a plant view node from a plant view node:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("ObjectLevel1");`

`PlantViewNode mixingNode = mixerObject.PlantViewNodes.Find("Mixing");`

`mixingNode.Delete();`

clipboard

Modify the following program code to rename a plant view node of CPM object instance by updating the 'Name' property:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews.Find("ABCManufacturingPlant");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("ObjectLevel1", "Plant_Object_Type_1");`

`PlantViewNode mixingNode = mixerObject.PlantViewNodes.Find("Mixing");`

`mixingNode.Name = "New_PlantViewNode_Name";`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Enumerating interface tags of CPM object instance  (RT Unified)

##### Introduction

You can use the TIA Portal Openness to enumerate a member of a CPM object instance.

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to enumerate all members of the CPM object instance:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews[0];`

`PlantViewNodeComposition plantViewNodes = plantView.PlantViewNodes;`

`PlantViewNode plantViewNode = plantViewNodes.Find("MixerObject_1");`

`PlantObject plantObject = plantViewNode.PlantObject;`

`PlantObjectInterfaceComposition interfaces = plantObject?. PlantObjectInterfaces;`

clipboard
> **Note**
>
> In the above example, the ?.operator refers to null check

Modify the following program code to find an interface tag from interfaces list based on ‘Name’:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews[0];`

`PlantViewNodeComposition plantNodes = plantView.PlantViewNodes;`

`PlantViewNode plantViewNode = plantNodes.Find("MixerObject_1");`

`PlantObject plantObject = plantViewNode.PlantObject;`

`PlantObjectInterface interface = plantObject. PlantObjectInterfaces.Find("Interface_1");`

clipboard

Modify the following program code to find an interface tag from interface list based on index:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews[0];`

`PlantViewNodeComposition plantViewNodes = plantView.PlantViewNodes;`

`PlantViewNode plantViewNode = plantViewNodes.Find("MixerObject_1");`

`PlantObject plantObject = plantViewNode.PlantObject;`

`PlantObjectInterfaceComposition interfaces = plantObject.PlantObjectInterfaces;`

`PlantObjectInterface interface = interfaces[0];`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Accessing properties for interface/logging tags of plant object instances (RT Unified)

This section contains information on the following topics:

- [Accessing/Updating properties of interface tags of CPM plant object instances (RT Unified)](#accessingupdating-properties-of-interface-tags-of-cpm-plant-object-instances-rt-unified)
- [Accessing/Updating properties of members tags of interface tags (RT Unified)](#accessingupdating-properties-of-members-tags-of-interface-tags-rt-unified)
- [Accessing/Updating properties of logging tags of member tags (RT Unified)](#accessingupdating-properties-of-logging-tags-of-member-tags-rt-unified)

#### Accessing/Updating properties of interface tags of CPM plant object instances (RT Unified)

##### Introduction

You can use the TIA Portal Openness to access and update the properties on interface tags of CPM plant object instance.

The following properties can be accessed on interface tags of CPM plant object instance:

| Property Name | Data type | Description | Accessibility |
| --- | --- | --- | --- |
| Name | System.String | Name of interface tags | R/W |
| PlcTag | System.String | PLC tag associated with interface tags | R/W |
| Connection | System.String | Connection of interface tags | R/W |
| PlcName | System.String | PLC name associated with interface tags | R |
| AccessMode | PlantObjectTagAccessMode | Access mode for interface tags | R |
| DataType | System.String | Object type of the interface tags | R |
| MaxLength | System.Int | Length of interface tags | R |
| HmiDataType | System.Int | HMI data type of interface tags | R |
| AcquisitionMode | PlantObjectTagAcquisitionMode | Acquisition mode of interface tags | R/W |
| AcquisitionCycle | System.Int | Acquisition cycle for interface tags | R/W |
| Persistent | System.Bool | Persistence for internal tags of CPM object instance | R |
| Comment | System.String | Comment | R/W |
| Members | PlantObjectInterfaceMemberComposition | Members of Interface Tag | R |

> **Note**
>
> PLCTag &amp; Connection property can only be configured after assigning Hmi device to the plant view.

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to access all the properties of interface tags:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterface interfaceTag = interfaceTags.FirstOrDefault();`

`string name = interfaceTag.`Name`;`

`MultilingualText comment = interfaceTag.Comment`

clipboard

Modify the following program code to update some properties of an interface tag, such as Comment, PLC Tag, Connection, Acquisition Mode, Acquisition Cycle:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterface interfaceTag = interfaceTags.FirstOrDefault();`

`interfaceTag.Name = "New_InterfaceTag_Name";`

`interfaceTag.Comment.Items[0].Text = "New_InterfaceTag_Comment";`

`interfaceTag.AcquisitionMode = PlantObjectTagAcquisitionMode.CyclicContinuous;`

`interfaceTag.AcquisitionCycle = "T12s";`

`interfaceTag.Connection = "Connection_1";`

`interfaceTag.PlcTag = "PLC_Tag_1";`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing/Updating properties of members tags of interface tags (RT Unified)

##### Introduction

You can use the TIA Portal Openness to access and update properties of member tags of interface tags.

The following properties can be accessed on member tags of interface tags:

| Property Name | Data type | Description | Accessibility |
| --- | --- | --- | --- |
| Name | System.String | Name of member tags | R |
| DataType | System.String | Object type of the member tags | R |
| MaxLength | System.Int | Length of member tags | R |
| HmiDataType | System.String | HMI data type of member tags | R |
| InitialMinValue | PlantObjectTagLowerRange | Lower range value | R/W |
| InitialMaxValue | PlantObjectTagUpperRange | Upper range value | R/W |
| InitialValue | System.Object | Initial value | R/W |
| SubstituteValue | PlantObjectTagSubstituteValue | Substitute value | R |
| Comment | MultilingualText | Comment | R/W |
| Members | PlantObjectInterfaceMemberComposition | Members of Member Tag | R |
| LoggingTags | PlantObjectLoggingTagComposition | LoggingTags of MemberTag | R |

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code:

`PlantViewComposition plantViews = m_tiaPortalApp.Projects[0].PlantViews;`

`PlantView plantView = plantViews[0];`

`PlantViewNodeComposition plantViewNodeComposition = plantView.PlantViewNodes;`

`PlantViewNode plantViewNode = plantViewNodeComposition[0];`

`PlantObjectInterfaceComposition tagComposition = plantViewNode.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterface interfaceTag = tagComposition[0];`

`PlantObjectInterfaceMemberComposition memberTags = interfaceTag.Members;`

`PlantObjectInterfaceMember memberTag = memberTags.FirstOrDefault();`

`//GetAttributes`

`List<string> listOfPropertyNames = new List<string>()`

`{`

`"Name"`

`};`

`var listOfPropertyValues = memberTag.GetAttributes(listOfPropertyNames);`

`//SetAttributes`

`IEnumerable<KeyValuePair<string, object>> propertyNameValuePairList = new List<KeyValuePair<string, object>>()`

`{`

`new KeyValuePair<string, object>("Name", "MemberTag_1");`

`};`

`memberTag.SetAttributes(propertyNameValuePairList);`

clipboard

Modify the following program code to access all the properties of member tags:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterfaceMemberComposition memberTags = interfaceTag.Members;`

`PlantObjectInterfaceMember memberTag = memberTags.FirstOrDefault();`

`string name = memberTag.Name;`

`string comment = memberTag.`Comment`.Items[0].Text;`

clipboard

Modify the following program code to update properties of a member tag of a CPM object instance:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterfaceMember memberTag = memberTags.FirstOrDefault();`

`memberTag.Comment.Items[0].Text = "New_MemberTag_Comment";`

`memberTag.InitialValue = 2;`

`memberTag.InitialMinValue.Value = 2;`

`memberTag.InitialMinValue.ValueType = PlantObjectTagLimitValueType.Constant;`

`memberTag.InitialMaxValue.Value = 2;`

`memberTag.InitialMaxValue.ValueType = PlantObjectTagLimitValueType.Constant;`

clipboard

Modify the following code to access all the logging tags of a member tag of CPM object instance:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaces;`

`PlantObjectInterface interfaceTag = interfaceTags.FirstOrDefault();`

`PlantObjectInterfaceMemberComposition memberTags = interfaceTag.Members;`

`PlantObjectInterfaceMember memberTag = memberTags.FirstOrDefault();`

`PlantObjectLoggingTagComposition loggingTags = memberTag.LoggingTags;`

`PlantObjectLoggingTag loggingTag = loggingTags.FirstOrDefault();`

clipboard

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

#### Accessing/Updating properties of logging tags of member tags (RT Unified)

##### Introduction

You can use the TIA Portal Openness to access logging tags of member tags present inside CPM object instance.

The following properties can be accessed on logging tags of member tags present inside CPM object instance:

| Property name | Data type | Description | Accessibilty |
| --- | --- | --- | --- |
| AggregationDelay | System.TimeSpan | Aggregation delay value | R |
| AggregationMode | PlantObjectLoggingTagAggregationMode | Aggregation Mode value | R |
| Cycle | System.String | Logging Cycle of logging tag | R |
| CycleFactor | System.UInt32 | Logging Cycle Factor vlaue | R |
| DataLog | System.String |  | R |
| Source | System.string | Source Logging Tag | R |
| TriggerMode | PlantObjectLoggingTagTriggerMode | TriggerMode of Logging tag | R |
| TriggerTag | System.String | TriggerTag Value | R |
| TriggerTagBitNumber | System.UInt32 | TriggerTagBitNumber value | R |
| Name | System.string | Name of logging tag | R |
| LogConfiguration | System.String | Data log of logging tag | R |
| LoggingMode | PlantObjectLoggingTagLoggingMode | Logging mode of logging tag | R |
| SmoothingMode | PlantObjectLoggingTagSmoothingMode | Smoothing mode of logging tag | R |
| SmoothingMinTime | System.TimeSpan | Minimum time of logging tag | R |
| SmoothingMaxTime | System.TimeSpan | Maximum time of logging tag | R |
| SmoothingDeltaValue | System.Double | Delta of logging tag | R |
| LimitScope | PlantObjectLoggingTagLimitScope | Limit scope of logging tag | R |
| HighLimit | System.Object | High limit of logging tag | R |
| LowLimit | System. Object | Low limit of logging tag | R |

##### Requirement

- The TIA Portal Openness is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

##### Program code

Modify the following program code to access all the properties of logging tags:

`// Instance inside plant view node`

`PlantViewNode mixingNode = plantView.PlantViewNodes.Create("Mixing");`

`PlantViewNode mixerObject = plantView.PlantViewNodes.Find("Mixing").PlantViewNodes.Create("IngredientMixer", "Mixer");`

`PlantObjectInterfaceMemberComposition interfaceTags = mixerObject.PlantObject.PlantObjectInterfaceMembers;`

`PlantObjectInterfaceMember interfaceTag = interfaceTags.FirstOrDefault();`

`PlantObjectInterfaceMemberComposition memberTags = interfaceTag.Members;`

`PlantObjectInterfaceMember memberTag = memberTags.FirstOrDefault();`

`PlantObjectLoggingTagComposition loggingTags = memberTag.LoggingTags;`

`PlantObjectLoggingTag loggingTag = loggingTags.FirstOrDefault();`

`string name = loggingTag.Name;`

`object lowLimit = loggingTag.LowLimit;`

clipboard
> **Note**
>
> You will not be able to update any property of PlantObjectLoggingTag class, associated to a CPM object instance logging tag.

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Checking license for access Unified device (RT Unified)

#### Introduction

You can use the TIA Openness interface to check any Openness client application for the presence of WinCC Unified license, so that a client application cannot bypass licensing using Openness interfaces.

You are only able to browse to an HMI Unified device and all its underlying objects (e.g. tags, alarms, screen, etc.) when HMI Unified license is not available. Any other operation on device level (e.g. create, find, delete) results in a LicenseNotFoundException being returned from Openness API.

> **Note**
>
> For HMI Unified Software, If license is invalid, then a LicenseNotFound Exception will be returned.

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal   
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open   
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Access to HMI Software object   
  See [HMI Unified Software object](#description-hmisoftware-rt-unified)

#### Program code

Modify the following program code to access the device or device sub systems when license is not available, a LicenseNotFound Exception is returned:

`private static void ListDevices(Project project)`
  
`{`

`foreach (var device in project.Devices)`
  
`{`
  
`ListDeviceItem(device);`
  
`}`
  
`}`
  
  
`private static void ListDeviceItem(Device device)`
  
`{`
  
`try`
  
`{`
  
`Console.Write("HMI device - " + device.Name);`
  
`foreach (var item in device.DeviceItems)`
  
`{`
  
`Console.WriteLine("HMI device type - " + item.TypeIdentifier);`
  
`var softContainer = item.GetService<SoftwareContainer>();`
  
`if (softContainer != null)`
  
`{`
  
`var softTarget = softContainer.Software;`
  
`}`
  
`if (softTarget != null)`
  
`{`
  
`Console.WriteLine("HMI device software - " + softTarget.Name);`

`}`
  
`}`
  
`}`
  
`catch (Exception ex)`
  
`{`
  
`Console.WriteLine(ex.Message);`
  
`}`
  
`}`

clipboard
> **Note**
>
> While accessing the above program code, the softTarget will be null, and accessing sub-systems, such as alarms, tags will not be posssible.

Modify the following program code to access the device or device sub systems when license is available, a null value is returned.

`private static void ListDevices(Project project)`

`{`

`foreach (var device in project.Devices)`

`{`

`ListDeviceItem(device);`

`}`

`}`

`private static void ListDeviceItem(Device device)`

`{`

`Console.Write("HMI device - " + device.Name);`

`foreach (var item in device.DeviceItems)`

`{`

`Console.WriteLine("HMI device type - " + item.TypeIdentifier);`

`var softContainer = item.GetService<SoftwareContainer>();`

`if (softContainer != null)`

`{`

`var softTarget = softContainer.Software;`

`}`

`if (softTarget != null)`

`{`

`Console.WriteLine("HMI device software - " + softTarget.Name);`

`}`

`}`

`}`

`}`

clipboard
> **Note**
>
> While accessing the above program code, the softTarget will have device container, and accessing sub-systems, such as alarms, tags will be possible.

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)

### Getting Cross References for WinCC Unified (RT Unified)

#### Introduction

You can use the TIA Portal Openness to provide cross reference information on applicable WinCC Unified objects. The Openness API returns CrossReferenceResult which provide the textual values of cross reference user interface and actual IEngineeringObject of applicable WinCC Unified objects.

The cross reference will attempt to provide the WinCC Unified object itself on which you can perform additional actions supported by the respective TIA Portal Openness objects.

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal.   
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Acess to the HMI Software object  
  See [HMI Unified Software](#description-hmisoftware-rt-unified)

#### Properties

For information on list of properties supported by WinCC Unified objects, Refer Properties in [Getting CrossReferences for Step7](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#getting-cross-references-for-step7)

#### Program code

Public void GetCrossReferences()

{

CrossReferenceService crossReferenceService = HmiScreen.GetService&lt;CrossReferenceService&gt;();

CrossReferenceResult rootResultObject = crossReferenceService.GetCrossReferences(CrossReferenceFilter.AllObjects);

SourceObjectComposition rootResultSourceObjects = rootResultObject.Sources; //The API returns a single source object but the type is a composition.

foreach (SourceObject sourceObject in rootResultSourceObjects)

{

//Get the source object references

ReferenceObjectComposition referenceObjects = source.References;

PrintReferences(referenceObjects);

}

}

Private void PrintReferences(ReferenceObjectComposition referenceObjects)

{

foreach (ReferenceObject referenceObject in referenceObjects)

{

// Needs similar casting for each type as seen in source object example snippet

if (source.UnderlyingObject != null &amp;&amp; source.UnderlyingObject is HmiScreenItemBase)

{

var hmiScreenItem= source.UnderlyingObject as HmiScreenItem;

//Perform actions on hmiScreenItem.

}

//No other attributes are available from the IEngineeringObject. All the remaining values must be given from crossreference separately via ReferenceObject EOM.

Console.WriteLine(referenceObject.Name);

Console.WriteLine(referenceObject.Address);

Console.WriteLine(referenceObject.TypeName);

Console.WriteLine(referenceObject.Device);

Console.WriteLine(referenceObject.Path);

LocationComposition locations = referenceObject.Locations;

//Looping through ReferenceLocations

{

Console.WriteLine(location.Name);

Console.WriteLine(location.ReferenceLocation);

Console.WriteLine(location.ReferenceType);

Console.WriteLine(location.Access);

if(location.ReferencedAs is Tag)

{

var referencedAsObject = location.ReferencedAs as Tag;

}

// Needs similar casting for each type as seen in source object example snippet

Console.WriteLine(location.ReferncedAsName);

Console.WriteLine(location.Address);

Console.WriteLine(location.TypeName);

}

}

clipboard

---

**See also**

[Getting Cross References for Step7](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#getting-cross-references-for-step7)
  
[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)

### Working with dynamization & events for screen/screen items using scripts (RT Unified)

#### Introduction

You can perform the following tasks with script to configure property dynamization and events for screen/screen items while using TIA Portal Openness:

- Creating script dynamizations
- Enumerating script dynamizations
- Deleting script dynamizations
- Accessing properties of script dynamizations
- Accessing properties of trigger
- Checking syntax

#### Requirement

- The TIA Portal Openness application is connecte to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Access to HMI Uinified Software object  
  See [HMI Unified Software object](#description-hmisoftware-rt-unified)

#### Program code

You can modify and use the following program code examples while working with script dynamization for screen/screen items.

**Creating script dynamizations**

Modify the following program code to create script dynamizations for a property:

`public DynamizationBase Create<DynamizationBase>(string propertyName);`

`HmiScreen screen = m_hmisoftware.Screen[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`ScriptDynamization scriptDynamic = dyns.Create<ScriptDynamization>("BackColor");`

clipboard

**Enumerating script dynamizations**

Modify the following program code to enumerate script dynamization of a property:

`public DynamizationBase Find(string propertyName);`

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`if (dyns is ScriptDynamization)`

`{`

`ScriptDynamization scriptDynamic = (ScriptDynamization)dyns.Find("BackColor");`

`}`

clipboard

**Deleting script dynamizations**

Modify the following program code to delete script dynamization for a property:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`if (dyns is ScriptDynamization)`

`ScriptDynamization scriptDynamic = (ScriptDynamization)dyns.Find("BackColor");`

`scriptDynamic.Delete();`

clipboard

**Accessing properties of script dynamizations**

Modify the following program code to get and set properties of script dynamization:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`foreach (DynamizationBase dynamic in dyns)`

`{`

`if (dynamic.DynamizationType == DynamizationType.Script)`

`{`

`ScriptDynamization scriptDynamization = (ScriptDynamization)dynamic;`

`scriptDynamization.Async = true;`

`scriptDynamization.GlobalDefinitionAreaScriptCode = @"Add(parameter1,parameter2)";`

`scriptDynamization.ScriptCode = @"`

`var value;`

`let tag1 = Tags('Tag_1');`

`let tagValue1 = tag1.Read();`

`HMIRuntime.Trace('value of MyTag1: ' + tagValue1);`

`return value; ";`

`Trigger triggerObj = scriptDynamization.Trigger;`

`}`

`}`

clipboard

**Accessing properties of Trigger**

Modify the following program code to get and set properties of trigger:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`foreach (DynamizationBase dynamic in dyns)`

`{`

`if (dynamic.DynamizationType == DynamizationType.Script)`

`{`

`ScriptDynamization scriptDynamization = (ScriptDynamization)dynamic;`

`// Property write`

`scriptDynamization.Trigger.Type = TriggerType.CustomCycle;`

`scriptDynamization.Trigger.CustomDuration = "T500ms";`

`scriptDynamization.Trigger.Tags = new List<string>() { "Tag_1" };`

`// Property read`

`Console.WriteLine(scriptDynamization.Trigger.Type);`

`Console.WriteLine(scriptDynamization.Trigger.CustomDuration);`

`Console.WriteLine(scriptDynamization.Trigger.Tags);`

`}`

`}`

clipboard

**Syntax Check**

Modify the following program code to check syntax for script code or global script code using SyntaxCheck action (method) of script dynamization:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`foreach (DynamizationBase dynamic in dyns)`

`{`

`if (dynamic.DynamizationType == DynamizationType.Script)`

`{`

`ScriptDynamization scriptDynamization = (ScriptDynamization)dynamic;`

`scriptDynamization.ScriptCode = @"`

`var value;let tag1 = Tags('Tag_1');`

`let tagValue1 = tag1.Read();`

`HMIRuntime.Trace('value of MyTag1: ' + tagValue1);`

`return value; ";`

`HmiValidationResult syntaxCkResult = scriptDynamization.SyntaxCheck();`

`IEnummerable<string> error = syntaxCkResult.Errors;`

`IEnumerable<string> warnings = syntaxCkResult.Warning;`

`}`

`}`

clipboard
> **Note**
>
> Create - Recoverable exception will be thrown in case respective dynamization is not supported for the specified property. If during set of properties the set operation fails consistency checks then a Recoverable exception would be raised.

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)

### Working with dynamization for screens/screen items (RT Unified)

#### Introduction

You can perform the following tasks with dynamization feature of screens/screen items while using TIA Portal Openness:

- Creating dynamization for a property
- Enumerating dynamization for a property
- Deleting dynamization for a property
- Accessing common properties of dynamization
- Accessing properties of tag dynamization
- Accessing properties of flasing dynamization
- Accessing properties of resourcelist dynamization

> **Note**
>
> For accessing dynamization for a properties at part level, you need to access respective part of Control. For part information, see [Accessing properties of trend control](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)

#### Requirement

- The TIA Portal Openness application is connected to the TIA Portal  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A Project is open  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- Access to HMI Software object  
  See [HMI Unified Software object](#description-hmisoftware-rt-unified)

#### Program code

You can modify and use the following program code examples while working with dynamizations for screen/screen items.

**Creating dynamization for a property**

Modify the following program code to create dynamization for a property:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`// Flashing dynamization`

`FlashingDynamization FlashingDyn = dyns.Create<FlashingDynamization>("BackColor");`

`// ResourceList dynamization`

`ResourceListDynamization ResListDyn = dyns.Create<ResourceListDynamization>("DisplayName");`

`// Tag dynamization`

`TagDynamization tagDyn = dyns.Create<TagDynamization>("Width");`

clipboard

**Enumerating dynamization of a property**

Modify the following program code to enumerate dynamization for a property:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`// Flashing dynamization`

`FlashingDynamization FlashDyn = (FlashingDynamization)dyns.Find("BackColor");`

`// ResourceList dynamization`

`ResourceListDynamization resourceDyn = (ResourceListDynamization)dyns.Find("DisplayName");`

`// Tag dynamization`

`TagDynamization tagDyn = (TagDynamization)dyns.Find("Width");`

clipboard

**Deleting dynamization of a property**

Modify the following program code to delete dynamization of a property:

`public void Delete ()`

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`DynamizationBaseComposition dyns = screen.Dynamizations;`

`DynamizationBase dynamization = dyns.Find("BackColor");`

`dynamization.Delete();`

clipboard

**Accessing common properties of dynamization**

Modify the following program code to get common properties of dynamization:

`HmiSoftware m_hmiSoftware = ..;`

`DynamizationBaseComposition screenDynamizations = m_hmiSoftware.Screens[0].Dynamizations;`

`DynamizationBase screenDynamization = screenDynamizations.Find("BackColor");`

`string propertyName = screenDynamization.PropertyName;`

`DynamizationType dynamizationType = screenDynamization.DynamizationType;`

clipboard

**Accessing properties of tag dynamization**

Modify the following program code to get and set properties of tag dynamization:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`TagDynamization tagDynamization = (TagDynamization)screen.Dynamizations.Find("Width");`

`foreach (DynamizationBase dynamization in screen.Dynamizations)`

`{`

`if (dynamization.DynamizationType == DynamizationType.Tag)`

`{`

`TagDynamization TagDynamization = (TagDynamization)dynamization;`

`TagDynamization.Tag = "HmiTagName";`

`TagDynamization.UseIndirectAddressing = true;`

`TagDynamization.ReadOnly = true;`

`}`

`}`

clipboard

**Accessing properties of flashing dynamization**

Modify the following program to get and set properties of flashing dynamization:

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`foreach (DynamizationBase dynamization in screen.Dynamizations)`

`{`

`if (dynamization.DynamizationType == DynamizationType.Flashing)`

`{`

`FlashingDynamization flashingDynamization = (FlashingDynamization)dynamization;`

`flashingDynamization.AlternateColor = Color.Beige;`

`flashingDynamization.Color = Color.FromArgb(12, 22, 152, 200);`

`flashingDynamization.FlashingCondition = FlashingCondition.Always;`

`flashingDynamization.FlashingRate = FlashingRate.Medium;`

`}`

`}`

clipboard

**Accessing properties of resourcelist dynamization**

Modify the following program code to get and set properties of resourcelist dynamization

`HmiScreen screen = m_hmiSoftware.Screens[0];`

`foreach (DynamizationBase dynamization in screen.Dynamizations)`

`{`

`if (dynamization.DynamizationType == DynamizationType.ResourceList)`

`{`

`ResourceListDynamization resourceListDyn = (ResourceListDynamization)dynamization;`

`resourceListDyn.Tag = "Tag name";`

`resourceListDyn.ResourceList = "Resource list name";`

`}`

`}`

clipboard
> **Note**
>
> Create - Recoverable exception will be thrown in case respective dynamization is not  supported for the specified property. If during set of properties the set operation fails consistency checks then a Recoverable exception would be raised.

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
  
[Description HMISoftware (RT Unified)](#description-hmisoftware-rt-unified)
  
Accessing properties of trend control

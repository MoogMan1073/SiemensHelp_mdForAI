---
title: "System functions (Panels, Comfort Panels, RT Advanced)"
package: VBSReferenceWCCAenUS
topics: 95
devices: [Comfort Panels, Panels, RT Advanced]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# System functions (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [AcknowledgeAlarm (Panels, Comfort Panels, RT Advanced)](#acknowledgealarm-panels-comfort-panels-rt-advanced)
- [ActivatePLCCodeViewer (Panels, Comfort Panels, RT Advanced)](#activateplccodeviewer-panels-comfort-panels-rt-advanced)
- [ActivatePreviousScreen (Panels, Comfort Panels, RT Advanced)](#activatepreviousscreen-panels-comfort-panels-rt-advanced)
- [ActivateScreen (Panels, Comfort Panels, RT Advanced)](#activatescreen-panels-comfort-panels-rt-advanced)
- [ActivateScreenByNumber (Panels, Comfort Panels, RT Advanced)](#activatescreenbynumber-panels-comfort-panels-rt-advanced)
- [ActivateSystemDiagnosticsView (Panels, Comfort Panels, RT Advanced)](#activatesystemdiagnosticsview-panels-comfort-panels-rt-advanced)
- [ArchiveLogFile (Panels, Comfort Panels, RT Advanced)](#archivelogfile-panels-comfort-panels-rt-advanced)
- [Back up RAM file system (Panels, Comfort Panels, RT Advanced)](#back-up-ram-file-system-panels-comfort-panels-rt-advanced)
- [CalibrateTouchScreen (Panels, Comfort Panels, RT Advanced)](#calibratetouchscreen-panels-comfort-panels-rt-advanced)
- [ChangeConnection (Panels, Comfort Panels, RT Advanced)](#changeconnection-panels-comfort-panels-rt-advanced)
- [ChangeConnectionEIP (Panels, Comfort Panels, RT Advanced)](#changeconnectioneip-panels-comfort-panels-rt-advanced)
- [ClearAlarmBuffer (Panels, Comfort Panels, RT Advanced)](#clearalarmbuffer-panels-comfort-panels-rt-advanced)
- [ClearAlarmBufferProtool (Panels, Comfort Panels, RT Advanced)](#clearalarmbufferprotool-panels-comfort-panels-rt-advanced)
- [ClearDataRecord (Panels, Comfort Panels, RT Advanced)](#cleardatarecord-panels-comfort-panels-rt-advanced)
- [ClearDataRecordMemory (Panels, Comfort Panels, RT Advanced)](#cleardatarecordmemory-panels-comfort-panels-rt-advanced)
- [ClearLog (Panels, Comfort Panels, RT Advanced)](#clearlog-panels-comfort-panels-rt-advanced)
- [CloseAllLogs (Panels, Comfort Panels, RT Advanced)](#closealllogs-panels-comfort-panels-rt-advanced)
- [ControlSmartServer (Panels, Comfort Panels, RT Advanced)](#controlsmartserver-panels-comfort-panels-rt-advanced)
- [ControlWebServer (Panels, Comfort Panels, RT Advanced)](#controlwebserver-panels-comfort-panels-rt-advanced)
- [CopyLog (Panels, Comfort Panels, RT Advanced)](#copylog-panels-comfort-panels-rt-advanced)
- [DecreaseTag (Panels, Comfort Panels, RT Advanced)](#decreasetag-panels-comfort-panels-rt-advanced)
- [EditAlarm (Panels, Comfort Panels, RT Advanced)](#editalarm-panels-comfort-panels-rt-advanced)
- [Encode (Panels, Comfort Panels, RT Advanced)](#encode-panels-comfort-panels-rt-advanced)
- [EncodeEx (Panels, Comfort Panels, RT Advanced)](#encodeex-panels-comfort-panels-rt-advanced)
- [ExportDataRecords (Panels, Comfort Panels, RT Advanced)](#exportdatarecords-panels-comfort-panels-rt-advanced)
- [ExportDataRecordsWithChecksum (Panels, Comfort Panels, RT Advanced)](#exportdatarecordswithchecksum-panels-comfort-panels-rt-advanced)
- [ExportImportUserAdministration (Panels, Comfort Panels, RT Advanced)](#exportimportuseradministration-panels-comfort-panels-rt-advanced)
- [GetBrightness (Panels, Comfort Panels, RT Advanced)](#getbrightness-panels-comfort-panels-rt-advanced)
- [GetDataRecordFromPLC (Panels, Comfort Panels, RT Advanced)](#getdatarecordfromplc-panels-comfort-panels-rt-advanced)
- [GetDataRecordName (Panels, Comfort Panels, RT Advanced)](#getdatarecordname-panels-comfort-panels-rt-advanced)
- [GetDataRecordTagsFromPLC (Panels, Comfort Panels, RT Advanced)](#getdatarecordtagsfromplc-panels-comfort-panels-rt-advanced)
- [GetGroupNumber (Panels, Comfort Panels, RT Advanced)](#getgroupnumber-panels-comfort-panels-rt-advanced)
- [GetPassword (Panels, Comfort Panels, RT Advanced)](#getpassword-panels-comfort-panels-rt-advanced)
- [GetUserName (Panels, Comfort Panels, RT Advanced)](#getusername-panels-comfort-panels-rt-advanced)
- [GoToEnd (Panels, Comfort Panels, RT Advanced)](#gotoend-panels-comfort-panels-rt-advanced)
- [GoToHome (Panels, Comfort Panels, RT Advanced)](#gotohome-panels-comfort-panels-rt-advanced)
- [ImportDataRecords (Panels, Comfort Panels, RT Advanced)](#importdatarecords-panels-comfort-panels-rt-advanced)
- [ImportDataRecordsWithChecksum (Panels, Comfort Panels, RT Advanced)](#importdatarecordswithchecksum-panels-comfort-panels-rt-advanced)
- [IncreaseTag (Panels, Comfort Panels, RT Advanced)](#increasetag-panels-comfort-panels-rt-advanced)
- [InverseLinearScaling (Panels, Comfort Panels, RT Advanced)](#inverselinearscaling-panels-comfort-panels-rt-advanced)
- [InvertBit (Panels, Comfort Panels, RT Advanced)](#invertbit-panels-comfort-panels-rt-advanced)
- [InvertBitInTag (Panels, Comfort Panels, RT Advanced)](#invertbitintag-panels-comfort-panels-rt-advanced)
- [LinearScaling (Panels, Comfort Panels, RT Advanced)](#linearscaling-panels-comfort-panels-rt-advanced)
- [LoadDataRecord (Panels, Comfort Panels, RT Advanced)](#loaddatarecord-panels-comfort-panels-rt-advanced)
- [LogOff (Panels, Comfort Panels, RT Advanced)](#logoff-panels-comfort-panels-rt-advanced)
- [Logon (Panels, Comfort Panels, RT Advanced)](#logon-panels-comfort-panels-rt-advanced)
- [LookupText (Panels, Comfort Panels, RT Advanced)](#lookuptext-panels-comfort-panels-rt-advanced)
- [NotifyUserAction (Panels, Comfort Panels, RT Advanced)](#notifyuseraction-panels-comfort-panels-rt-advanced)
- [OpenAllLogs (Panels, Comfort Panels, RT Advanced)](#openalllogs-panels-comfort-panels-rt-advanced)
- [OpenCommandPrompt (Panels, Comfort Panels, RT Advanced)](#opencommandprompt-panels-comfort-panels-rt-advanced)
- [OpenControlPanel (Panels, Comfort Panels, RT Advanced)](#opencontrolpanel-panels-comfort-panels-rt-advanced)
- [OpenInternetExplorer (Panels, Comfort Panels, RT Advanced)](#openinternetexplorer-panels-comfort-panels-rt-advanced)
- [OpenScreenKeyboard (Panels, Comfort Panels, RT Advanced)](#openscreenkeyboard-panels-comfort-panels-rt-advanced)
- [OpenTaskManager (Panels, Comfort Panels, RT Advanced)](#opentaskmanager-panels-comfort-panels-rt-advanced)
- [PageDown (Panels, Comfort Panels, RT Advanced)](#pagedown-panels-comfort-panels-rt-advanced)
- [PageUp (Panels, Comfort Panels, RT Advanced)](#pageup-panels-comfort-panels-rt-advanced)
- [PrintReport (Panels, Comfort Panels, RT Advanced)](#printreport-panels-comfort-panels-rt-advanced)
- [PrintScreen (Panels, Comfort Panels, RT Advanced)](#printscreen-panels-comfort-panels-rt-advanced)
- [ResetBit (Panels, Comfort Panels, RT Advanced)](#resetbit-panels-comfort-panels-rt-advanced)
- [ResetBitInTag (Panels, Comfort Panels, RT Advanced)](#resetbitintag-panels-comfort-panels-rt-advanced)
- [SafelyRemoveHardware (Panels, Comfort Panels)](#safelyremovehardware-panels-comfort-panels)
- [SaveDataRecord (Panels, Comfort Panels, RT Advanced)](#savedatarecord-panels-comfort-panels-rt-advanced)
- [SendEMail (Panels, Comfort Panels, RT Advanced)](#sendemail-panels-comfort-panels-rt-advanced)
- [SetAcousticSignal (Panels, Comfort Panels, RT Advanced)](#setacousticsignal-panels-comfort-panels-rt-advanced)
- [SetAlarmReportMode (Panels, Comfort Panels, RT Advanced)](#setalarmreportmode-panels-comfort-panels-rt-advanced)
- [SetBit (Panels, Comfort Panels, RT Advanced)](#setbit-panels-comfort-panels-rt-advanced)
- [SetBitInTag (Panels, Comfort Panels, RT Advanced)](#setbitintag-panels-comfort-panels-rt-advanced)
- [SetBrightness (Panels, Comfort Panels, RT Advanced)](#setbrightness-panels-comfort-panels-rt-advanced)
- [SetConnectionMode (Panels, Comfort Panels, RT Advanced)](#setconnectionmode-panels-comfort-panels-rt-advanced)
- [SetDataRecordTagsToPLC (Panels, Comfort Panels, RT Advanced)](#setdatarecordtagstoplc-panels-comfort-panels-rt-advanced)
- [SetDataRecordToPLC (Panels, Comfort Panels, RT Advanced)](#setdatarecordtoplc-panels-comfort-panels-rt-advanced)
- [SetDaylightSavingTime (Panels, Comfort Panels, RT Advanced)](#setdaylightsavingtime-panels-comfort-panels-rt-advanced)
- [SetDeviceMode (Panels, Comfort Panels, RT Advanced)](#setdevicemode-panels-comfort-panels-rt-advanced)
- [SetDisplayMode (Panels, Comfort Panels, RT Advanced)](#setdisplaymode-panels-comfort-panels-rt-advanced)
- [SetLanguage (Panels, Comfort Panels, RT Advanced)](#setlanguage-panels-comfort-panels-rt-advanced)
- [SetPLCDateTime (Panels, Comfort Panels, RT Advanced)](#setplcdatetime-panels-comfort-panels-rt-advanced)
- [SetRecipeTags (Panels, Comfort Panels, RT Advanced)](#setrecipetags-panels-comfort-panels-rt-advanced)
- [SetScreenKeyboardMode (Panels, Comfort Panels, RT Advanced)](#setscreenkeyboardmode-panels-comfort-panels-rt-advanced)
- [SetTag (Panels, Comfort Panels, RT Advanced)](#settag-panels-comfort-panels-rt-advanced)
- [ShiftAndMask (Panels, Comfort Panels, RT Advanced)](#shiftandmask-panels-comfort-panels-rt-advanced)
- [ShowAlarmWindow (Panels, Comfort Panels, RT Advanced)](#showalarmwindow-panels-comfort-panels-rt-advanced)
- [ShowOperatorNotes (Panels, Comfort Panels, RT Advanced)](#showoperatornotes-panels-comfort-panels-rt-advanced)
- [ShowPopUpScreen (Panels, Comfort Panels, RT Advanced)](#showpopupscreen-panels-comfort-panels-rt-advanced)
- [ShowPopupScreenSizable (Panels, Comfort Panels, RT Advanced)](#showpopupscreensizable-panels-comfort-panels-rt-advanced)
- [ShowSlideInScreen (Panels, Comfort Panels, RT Advanced)](#showslideinscreen-panels-comfort-panels-rt-advanced)
- [ShowSoftwareVersion (Panels, Comfort Panels, RT Advanced)](#showsoftwareversion-panels-comfort-panels-rt-advanced)
- [ShowSystemAlarm (Panels, Comfort Panels, RT Advanced)](#showsystemalarm-panels-comfort-panels-rt-advanced)
- [ShowSystemDiagnosticsWindow (Panels, Comfort Panels)](#showsystemdiagnosticswindow-panels-comfort-panels)
- [StartLogging (Panels, Comfort Panels, RT Advanced)](#startlogging-panels-comfort-panels-rt-advanced)
- [StartNextLog (Panels, Comfort Panels, RT Advanced)](#startnextlog-panels-comfort-panels-rt-advanced)
- [StartProgram (Panels, Comfort Panels, RT Advanced)](#startprogram-panels-comfort-panels-rt-advanced)
- [StopLogging (Panels, Comfort Panels, RT Advanced)](#stoplogging-panels-comfort-panels-rt-advanced)
- [StopRuntime (Panels, Comfort Panels, RT Advanced)](#stopruntime-panels-comfort-panels-rt-advanced)
- [TerminatePROFIsafe (Panels, Comfort Panels, RT Advanced)](#terminateprofisafe-panels-comfort-panels-rt-advanced)

## AcknowledgeAlarm (Panels, Comfort Panels, RT Advanced)

### Description

Acknowledges all selected alarms.

This system function is used when the HMI device does not have an ACK key or when the integrated key of the alarm view should not be used.

This system function can only be used for function keys.

### Use in the function list

AcknowledgeAlarm

### Use in user-defined functions

AcknowledgeAlarm

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## ActivatePLCCodeViewer (Panels, Comfort Panels, RT Advanced)

### Description

Performs a screen change to the given screen with the PLC code view. The PLC code view shows the program code of the relevant network.

You configure the ActivatePLCCodeView system function at the "Click PLC code view button" event of a GRAPH overview or at an event of a button.

**Screen change from the GRAPH overview**

You configure the system function at the "Click PLC code view button" event in a GRAPH overview to display the GRAPH step sequencer in the PLC code view. If no error is pending, the sequence of the GRAPH step sequencer is displayed.

If an error occurs, the faulty step is displayed in the PLC code view after jump of the faulty step. If multiple errors have occurred, the first faulty step of the sequencer is displayed after the jump. If you have corrected the error, the next faulty step is automatically displayed in the view. In the detail view, the transition or the interlock is displayed depending on the type of error.

**Screen change from an alarm**

You configure the system function at an event of a button. When the button is pressed in Runtime, the system function checks whether the alarm selected last in the configured alarm view is a supervision alarm or a GRAPH alarm. If a jump is possible for this alarm, the configured PLC code view is opened with the corresponding program code.

The jump from an alarm in the alarm view to the PLC code view is made possible for the following supervision alarms:

- With global supervisions, only for interlock supervisions (Interlock)
- With local supervisions, for all basic supervisions at input parameters

You can find more information on supervisions in the section "Programming PLC > Supervising machinery and plants with ProDiag".

The jump to the PLC code view is possible for all GRAPH alarms. After the jump, the GRAPH sequencer and the faulty step are displayed in the PLC code view.

If a supervision alarm and an interlock alarm are pending simultaneously for the same step, the interlock network is always displayed first after triggering the system function in the PLC code view regardless of whether the supervision alarm or the interlock alarm was selected.

For the versions < V 18 (Professional) or < V 17 Update 6 (Advanced) the following applies: For the jump from a supervision alarm to the PLC code view, the instance name must conform to the following naming convention when using supported local operands in a function block: <FB-Name>_DB. This restriction does not apply to the current version.

The jump to a function or an organization block is only possible if only global operands are used.

> **Note**
>
> The jump in connection with the alarm buffer or the alarm log is not supported.

### Use in the function list

ActivatePLCCodeView(Screen name, Screen object)

### Use in user-defined functions

ActivatePLCCodeView Screen_name, Object_name

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

> **Note**
>
> The version of the GRAPH block must be at least V3.0 for the jump into the GRAPH sequencer via the "ActivatePLCCodeView" system function.

> **Note**
>
> Use of the system function "ActivatePLCCodeView" in a VB script has no effect at a GRAPH overview.

### Parameters

**Screen name**

Name of the screen that contains the PLC code view.

> **Note**
>
> Screen change to a pop-up screen or a slide-in screen is not supported.

**Screen object**

Object name of the PLC code view.

## ActivatePreviousScreen (Panels, Comfort Panels, RT Advanced)

### Description

Performs a screen change to the screen which was activated before the current screen. The screen change is not performed if no screen was activated beforehand.

The last 10 screens that were called up are saved. A system alarm is output when you change to a screen which is no longer saved.

> **Note**
>
> If you want to use the system function, the screen to which you change has to be used in the navigation structure.

### Use in the function list

ActivatePreviousScreen

### Use in user-defined functions

ActivatePreviousScreen

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## ActivateScreen (Panels, Comfort Panels, RT Advanced)

### Description

Performs a screen change to the given screen.

Use the "ActivateScreenByNumber" system function to change from the root screen to the permanent area or vice versa.

### Use in the function list

ActivateScreen (Screen name, Object number)

### Use in user-defined functions

ActivateScreen Screen_name, Object_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen name**

Name of the screen to which you change.

**Object number**

The operator control element which receives the focus in the given screen after the screen change. The number of the operator control element is to be determined using the tabulator sequence during configuration.

When "0" is specified:

- If the focus is in the permanent area when the system function is called up, the permanent area maintains the focus.
- If the focus is in the root screen when the system function is called up, the first operator control element in the given screen receives the focus.

  > **Note**
  >
  > If the "Reach margin" event is assigned to the "ActivateScreen" system function, only the value "0" is valid for the "Object number" parameter. The active object is not defined by the object number, but rather by the X position it had prior to the screen change.

### Example

The following program code activates "Screen_2" with the ActivateScreen function, for example, when you click a button.

`Sub ActivateScreen_2()`

`'User-defined code`

`'' i. e. when pressing a button`

`ActivateScreen "Screen_2",0`

## ActivateScreenByNumber (Panels, Comfort Panels, RT Advanced)

### Description

Performs a screen change to a screen depending on a tag value.

The screen is identified by its screen number.

### Use in the function list

ActivateScreenByNumber (Screen number, Object number)

### Use in user-defined functions

ActivateScreenByNumber Screen_number, Object_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Screen number**

Tag which contains the screen number of the destination screen.

When a change from the root screen to the permanent area is desired, specify "0" or "-1":

0 = Change from root screen to permanent area.

-1 = Change from permanent area to root screen

**Object number**

The number of the screen object which receives the focus in the given screen after the screen change. The number of the operator control element is to be determined using the tabulator sequence during configuration.

When "0" is specified:

- If the focus is in the permanent area when the system function is called up, the permanent area maintains the focus.
- If the focus is in the root screen when the system function is called up, the first operator control element in the given screen receives the focus.

## ActivateSystemDiagnosticsView (Panels, Comfort Panels, RT Advanced)

### Description

Activates the system diagnostics view. The system diagnostics view shows the detail view of the device concerned.

### Use in the function list

ActivateSystemDiagnosticsView (Screen name, Screen object)

### Use in user-defined functions

ActivateSystemDiagnosticsView Screen_name, Object_name

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen name**

Name of the screen contained in the system diagnostics view.

**Screen object**

Object name of the system diagnostics view.

## ArchiveLogFile (Panels, Comfort Panels, RT Advanced)

### Description

This system function moves or copies a log to another storage location for long-term logging.

Prior to "ArchiveLogFile", always run the "CloseAllLogs" system function.

After this system function has been completed, run the "OpenAllLogs" system function.

In "Copy log" mode, the logs are not reopened until the log has been successfully copied or if a timeout occurs during the copy.

In "Move log" mode, the logs to be moved are renamed and the new logs are opened immediately. To move the renamed logs, a job is submitted which attempts to move them every 300 seconds if the target directory cannot be accessed. The job is also retained after Runtime is restarted until it is executed. Therefore, before you move a log, you should check whether the target directory is accessible.

With Audit Trails, always use the "Move" (hmiMove) mode, otherwise you will be violating the FDA guideline by duplicating the data stored.

### Use in the function list

ArchiveLogFile (Log type, Log, Directory name, Mode)

### Use in user-defined functions

ArchiveLogFile Log_type, Log, Directory_name, Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

2 (hmiAudittrailArchive)= Audit trail log available for GMP compliant projects. Additional information is available under "Activating GMP-compliant configuration".

**Log**

Name of the log being archived.

**Directory name**

Path for saving the log.

**Mode**

0 (hmiCopy) = Copy log

1 (hmiMove) = Move log

### Application example

You want to move a log file from a local storage medium to the server in order to generate a backup copy of this file at cyclic intervals.

**Notes on configuring**

Set up a task in the scheduler which is executed at a specific time on a daily basis. Configure the following function list for the task:

![Application example](images/36154450315_DV_resource.Stream@PNG-en-US.png)

**Procedure on HMI device**

- All log files will be closed.
- The log file you specified is moved to the server.
- All closed log files will be opened again.

## Back up RAM file system (Panels, Comfort Panels, RT Advanced)

### Description

Backs up the RAM file system in the memory medium of the HMI device.

After restarting the HMI device, the data is automatically reloaded in the RAM file system.

Applications such as the Internet Explorer save data (e.g. the last web sites called up) temporarily to the DRAM file system of the HMI device.

### Use in the function list

BackupRAMFileSystem

### Use in user-defined functions

BackupRAMFileSystem

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## CalibrateTouchScreen (Panels, Comfort Panels, RT Advanced)

### Description

Calls a program for calibrating the touch screen.

During the calibration process, there is a prompt to touch five positions on the screen display. Touch the screen display within 30 seconds, to confirm the calibration process. If the calibration is not completed within this time span, the calibration settings are discarded. The user prompt is in English.

Use this system function the first time you start the HMI device.

> **Note**
>
> The direct keys are reset by the system function.

### Use in the function list

CalibrateTouchScreen

### Use in user-defined functions

CalibrateTouchScreen

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

> **Note**
>
> The CalibrateTouchScreen system function cannot be simulated.

## ChangeConnection (Panels, Comfort Panels, RT Advanced)

### Description

Disconnects the connection to the PLC currently in use and establishes a connection to a PLC with another address. The newly connected PLC must belong to the same device class (S7-300, S7-400, etc).

> **Note**
>
> When changing to another address, ensure that the address is not already being used by another HMI device.

The follows address types are supported:

- IP address
- MPI address

The follows PLC types are supported:

- SIMATIC S7 300/400
- SIMATIC S7 200
- SIMATIC S7 1200 (device version up to V11)
- SIMATIC S7 LOGO!
- SIMATIC S7-NC
- SIMOTION

### Use in the function list

ChangeConnection (Connection, Address, Slot, Rack)

### Use in user-defined functions

ChangeConnection Connection, Address, Slot, Rack

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Connection**

Name of the connection that is disconnected. The name is set during configuration, for example, in the "Connections" editor.

**Address**

MPI/PROFIBUS or IP address of the PLC to which the connection will be established.

> **Note**
>
> Set the address by means of a tag. The objects list displays the tags of all data types. Select only tags of the following data types:
>
> - Ethernet connection: "String" data type
> - MPI connection: "Int" data type

**Slot**

Slot of the PLC to which the connection will be established.

**Rack**

Rack of the PLC to which the connection will be established.

### Application example

You want to operate one HMI device on several machines. Configure a controller in the project. When changing the PLC, the connection to the PLC in use is disconnected. Then the connection to the new PLC with other address parameters is reestablished. All tags in this connection are now updated from the new controller.

The PLC which you have indicated when creating the project will be used as default.

1. Enter the name and address of the PLC in the "Connections" editor.
2. Configure a button in the process screen.
3. Configure the "ChangeConnection" system function on the "Press" event.
4. Enter the name of the connection and address of the PLC as parameters.

## ChangeConnectionEIP (Panels, Comfort Panels, RT Advanced)

### Description

Terminates the connection to the Allan Bradley controller currently in use and establishes a connection to another Allan Bradley controller in Runtime. "EIP" stands for "Ethernet/IP".

The newly connected controller must belong to the same device class (Allen Bradley).

For the connection to be established, the CPU type of the controller to be connected must match the CPU type of the controller already connected, for example, both controllers have the CPU type "SLC/Micrologix PLC".

> **Note**
>
> When changing to another address, ensure that the address is not already being used by another HMI device.

The follows address types are supported:

- IP address

### Use in the function list

ChangeConnectionEIP (Connection, Address, Communication path)

### Use in user-defined functions

ChangeConnectionEIP Connection, Address, Communication_path

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Connection**

Name of the connection that is disconnected. The name is set during configuration, for example, in the "Connections" editor.

**Address**

IP address of the controller to which the connection is being established.

> **Note**
>
> Set the address by means of a tag. The objects list displays the tags of all data types. Select only tags of the following data type "String".

> **Note**
>
> The stored IP address must consist of 4 decimal numbers with the value range 0 to 255.

**Communication path**

CIP path from the Ethernet module to the controller to which the connection is being established.

You specify the communication path either with a String tag or an HMI tag of the "String" data type.

### **Application example**

You want to operate one HMI device on several machines. To do so, you configure a PLC in the project. When changing the PLC, the connection to the PLC in use is disconnected. Then the connection to the new PLC with other address parameters is reestablished. All tags of this connection are now updated from the new PLC.

1. Enter the name and address of the PLC in the "Connections" editor.
2. Configure a button in the process screen.
3. Configure the "ChangeConnectionEIP" system function on the "Press" event.
4. Enter the name of the connection and address of the PLC as parameters.

## ClearAlarmBuffer (Panels, Comfort Panels, RT Advanced)

### Description

Deletes alarms from the alarm buffer on the HMI device.

> **Note**
>
> Alarms which have not yet been acknowledged are also deleted.

### Use in the function list

ClearAlarmBuffer (Alarm class number)

### Use in user-defined functions

ClearAlarmBuffer Alarm_class_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Alarm class number**

Determines which alarms are to be deleted from the alarm buffer:

0 (hmiAll) = All alarms

1 (hmiAlarms) = Alarms of alarm class "Error"

2 (hmiEvents) = Alarms of alarm class "Warning"

3 (hmiSystem) = Alarms of alarm class "System event"

4 (hmiS7Diagnosis) = Alarms of alarm class "S7 diagnostic alarm"

> **Note**
>
> **Device dependency**
>
> Alarms of alarm class "Diagnosis Events" are not available on Basic Panels.

## ClearAlarmBufferProtool (Panels, Comfort Panels, RT Advanced)

### Description

The system function exists to ensure compatibility.

It has the same functionality as the "ClearAlarmBuffer" system function, but uses the old ProTool numbering.

### Use in the function list

ClearAlarmBufferProTool (Alarm class number)

### Use in user-defined functions

ClearAlarmBufferProtoolLegacy Alarm_class_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Alarm class number**

Alarm class number whose messages are to be deleted:

-1 (hmiAllProtoolLegacy) = All alarms

0 (hmiAlarmsProtoolLegacy) = Alarms of alarm class "Errors"

1 (hmiEventsProtoolLegacy) = Alarms of alarm class "Warnings"

2 (hmiSystemProtoolLegacy) = Alarms of alarm class "System"

3 (hmiS7DiagnosisProtoolLegacy) = Alarms of alarm class "Diagnosis Events"

> **Note**
>
> **Device dependency**
>
> Alarms of alarm class "Diagnosis Events" are not available on Basic Panels.

## ClearDataRecord (Panels, Comfort Panels, RT Advanced)

### Description

Deletes a recipe data record.

Several data records can be deleted from one or more recipes.

### Use in the function list

ClearDataRecord (Recipe number/name, Data record number/name, Confirmation, Output status message, Processing status)

### Use in user-defined functions

ClearDataRecord

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which recipe data records are deleted. "0" is specified if you want to delete recipe data records from all available recipes.

**Data record number/name**

Number or name of the recipe data record to be deleted. "0" is specified if you want to delete all recipe data records.

**Confirmation**

Determines whether the operator should confirm the deletion:

0 (hmiOff) = Off: Deletion is begun without confirmation.

1 (hmiOn) = On: The starting of the deletion process must be confirmed.

**Output status message**

Determines whether a status message is output after the deletion:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## ClearDataRecordMemory (Panels, Comfort Panels, RT Advanced)

### Description

Deletes all recipes data records from the specified storage medium.

### Use in the function list

ClearDataRecordMemory (Storage location, After confirmation, Output status message, Processing status)

### Use in user-defined functions

ClearDataRecordMemory Storage_location, Confirmation, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Storage location**

Determines the storage location:

0 (hmiFlashMemory) = Flash memory: Internal flash memory of the HMI device

1 (hmiStorageCard) = Storage card

2 (hmiStorageCard2) = Storage card 2

3 (hmiStorageCard3) = Storage card MultiMediaCard

4 (hmiStorageCard4) = Storage card

**With confirmation**

Determines whether the operator should confirm the deletion:

0 (hmiOff) = Off: Deletion is begun without confirmation.

1 (hmiOn) = On: The starting of the deletion process must be confirmed.

**Output status message**

Determines whether a status message is output after the deletion:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## ClearLog (Panels, Comfort Panels, RT Advanced)

### Description

Deletes all data records in the given log.

### Use in the function list

ClearLog (Log type, Log)

### Use in user-defined functions

ClearLog Log_type, Log

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

2 (hmiAudittrailArchive) = Audit trail log. Available for GMP-compliant projects Additional information is available under "Activating GMP-compliant configuration".

**Log**

Name of the log from which all entries are deleted.

## CloseAllLogs (Panels, Comfort Panels, RT Advanced)

### Description

Disconnects the connection between WinCC and all logs.

### Use in the function list

CloseAllLogs

### Use in user-defined functions

CloseAllLogs

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

### Application example

You are in runtime and want to change the data medium on which the process values are logged.

**Notes on configuring**

Configure the "CloseAllLogs" system function on the "Close Archive" button.

Configure the "OpenAllLogs" and "StartLogging" system functions on the "Open Archive" button.

As parameter transfer the respective name of the log that is to be stopped and started.

**Procedure on HMI device**

When you press the "Close Archive" button, the opened logs are closed. The data medium can be changed. The logging continues during the change of the data medium. The process values to be logged are cached. You open all logs with the "Open Archive" button. The logging process will continue in the specified log. The buffered process values are later added to the log.

## ControlSmartServer (Panels, Comfort Panels, RT Advanced)

### Description

Starts or stops the Sm@rtServer.

### Use in the function list

ControlSmartServer (Mode)

### Use in user-defined functions

ControlSmartServer Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Mode**

Specifies whether the Sm@rtServer is started or stopped.

-1 (hmiToggle) = Toggle: Toggles between the two modes

0 (hmiStop) = Stop: Sm@rtServer is stopped

1 (hmiStart) = Start: Sm@rtServer is started

## ControlWebServer (Panels, Comfort Panels, RT Advanced)

### Description

Starts or stops the Web server.

### Use in the function list

ControlWebServer (Mode)

### Use in user-defined functions

ControlWebServer Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Mode**

Specifies whether the Web server is started or stopped.

-1 (hmiToggle) = Toggle: Toggles between the two modes

0 (hmiStop) = Stop: The Web server is stopped.

1 (hmiStart) = Start: The Web server is started.

## CopyLog (Panels, Comfort Panels, RT Advanced)

### Description

Copies the contents of a log to another log. Tag values can only be copied to other data logs and alarms only to other alarm logs, however.

> **Note**
>
> If you copy a log using the "CopyLog" system function, it is possible that external applications will be unable to read certain country-specific special characters in the logged message text of the log copy. This does not apply to WinCC Runtime. WinCC Runtime can read the copied log files without errors.

> **Note**
>
> 80% of the log entries are copied when copying the circular logs. 20% of entries are not copied because the space is reserved for buffer overflow by default.

### Use in the function list

CopyLog (Log type, Destination log, Source log, Mode, Delete source log)

### Use in user-defined functions

CopyLog Log_type, Destination log, Source_log, Mode, Delete_source_log

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

**Destination log**

Name of the log into which the entries are copied (Destination log).

**Source log**

Name of the log from which the entries are copied (Source log).

**Mode**

Determines what is done with copied entries in the destination log:

0 (hmiOverwrite) = Overwrite: Existing entries are overwritten.

2 (hmiAppend) = Append: The entries are inserted at the end of the destination log. When the configured size of the log has been reached, the destination log is treated like a circular log.

**Delete source log**

Determines whether the source log is deleted after copying.

0 (hmiNo) = No: Is not deleted.

1 (hmiYes) = Yes: Is deleted.

## DecreaseTag (Panels, Comfort Panels, RT Advanced)

### Description

Subtracts the given value from the tag value.

X = X - a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, auxiliary tags must be used. The auxiliary tags are assigned to the tag value with the "SetTag" system function.

If you configure the system function on the events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual value of the tags is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

### Use in the function list

DecreaseTag (Tag, Value)

### Use in user-defined functions

DecreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Tag**

The tag from which the given value is subtracted.

**Value**

The value which is subtracted.

## EditAlarm (Panels, Comfort Panels, RT Advanced)

### Description

Triggers the "Edit" event for the selected alarm or for the last selected alarm in case of multiple selection. If the alarms to be edited have not yet been acknowledged, they are acknowledged automatically when this system function is called.

This system function can only be used for function keys.

### Use in the function list

EditAlarm

### Use in user-defined functions

EditAlarm

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

--

## Encode (Panels, Comfort Panels, RT Advanced)

### Description

Adapts the "String" data type of a tag for transfer to the automation system (AS). The tag of WinCC data type "String" is converted into the AS data type "Array of byte". The result is written to a tag.

### Use in the function list

Encode (Byte array, String, Coding)

### Use in user-defined functions

Encode Byte_array, String, Encoding

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Byte array**

The tag that contains the converted value.

> **Note**
>
> The Byte array must be twice the size of the string length + 2. The Byte array must contain 242 array elements if the string has a length of 120 characters.
>
> Characters are either truncated or not converted if the size is insufficient.

**String**

The tag of data type "String" that is converted.

**Encode**

0 (hmiEncodeUTF16LE) - String is encoded in UTF16LE (Unicode 16 Little Endian).

## EncodeEx (Panels, Comfort Panels, RT Advanced)

### Description

Adapts the "String" data type of a tag for transfer to the automation system (AS). The tag of WinCC data type "String" is converted into the AS data type "Array of byte". The result is written to a tag.

By contrast to the Encode system function, you can define the Line break parameter. Using the Line break parameter you can delete line breaks or replace these with predefined characters.

### Use in the function list

EncodeEx (Byte-Array, String, Encoding, Line break)

### Use in user-defined functions

EncodeEx Byte_array, String, Encoding, Line_break

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Byte array**

The tag that contains the converted value.

> **Note**
>
> The byte array must be twice the size of the string length +2. If the string has a length of 120 characters, the byte array must contain 242 array elements.
>
> Characters are either truncated or not converted if the size is insufficient.

**String**

The tag of data type "String" that is converted.

**Encoding**

0 (hmiEncodeUTF16LE) - String is encoded in UTF16LE (Unicode 16 Little Endian).

**Line break**

All line breaks are either deleted or replaced with predefined characters. Do not replace line breaks if set as the default value.

0 (replace with "\r\n' (0x000D, 0x000A)) - the line break is replaced with "\r\n".

1 (replace with "\n' (0x000A)) - the line break is replaced with "\n".

2 (do not replace) - the line break is not replaced.

3 (remove line breaks) - the line breaks are removed.

## ExportDataRecords (Panels, Comfort Panels, RT Advanced)

### Description

Exports one or all data records of a recipe to a CSV file or a TXT file.

One file is created per recipe.

### Use in the function list

ExportDataRecords (Recipe number/name, Data record number/name, File name, Overwrite, Output status message, Processing status)

### Use in user-defined functions

ExportDataRecords Recipe_number/name, Data_record number/name, File_name, Overwrite, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which the data records are exported. Specify "0" if recipe data records are to be exported from all available recipes.

**Data record number/name**

Number or name of the recipe data record to be exported. Specify "0" if all recipe data records are to be exported.

**File name**

Name of the file to which the recipe data records are exported. Enter the name, including the storage location and the file extension (*.csv or *.txt), for example "C:\TEMP\Orange.csv". If a folder does not exist, it is created during the export.

If you do not enter the file name fully, the response depends on the number of configured recipes:

- If multiple recipes are configured and

  you only specify one file name and no path, the file is saved in a system directory, for example, "C:\Documents and Settings\[User]".

  When only a path and no file name is specified, the file name is automatically created from the recipe name. It is a requirement that the folder "D:\Data\", for example, has been created in the specified folder. If the "D:\Data" folder has not been created, the folder name will be used as the prefix for the file name, for example, "Data_Recipe name.csv".
- If only one recipe is configured and only one path and no file name is specified,

  a file with the folder name is created if the folder does not exist. However, this has no file extension.

  the export is aborted with an error message if the folder exists.

If a memory card is used as storage location, specify the storage location as follows: "\StorageCard\<Name>".

For Basic Panel, enter the file name as follows: "\USB_X60.1\<Name>"

**Overwrite**

Determines whether an existing export file with the same name is overwritten:

0 (hmiOverwriteForbidden) = No: Export file will not be overwritten. The export process will not be carried out.

1 (hmiOverwriteAlways) = Yes: Export is overwritten without a prompt for confirmation.

2 (hmiOverwriteWithPrompting) = With confirmation: Export file is not overwritten until confirmed.

**Output status message**

Determines whether a status message is output after the export:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

### Export format of the recipe data records

If ".csv" is chosen as a file extension for the export file, then only valid characters from the ANSI character set will be supported. This also applies to separators in decimal numbers and list elements. The separators used are defined in the country/regional settings of the operating system of the exporting computer.

You may also set "Unicode text" (".txt") format for the export file. This file format supports the WinCC and WinCC Runtime character set. Again, the separators used are specified in the country/regional settings of the operating system of the exporting computer. This file format always uses tab separators in list elements.

The corresponding file import function also supports the ".csv" and ".txt" (Unicode) file formats.

### Application example

You want to export all data records using a key.

**Notes on configuring**

Configure the "ExportDataRecords" system function on the "Press" event for the desired key. Transfer the following parameters:

- Recipe number/name = 1
- Data record number/name = 0
- File name = c:\temp\orange.csv (for Basic Panels "\USB_X60.1\orange.csv")
- Overwrite = 1
- Output status message = 1

Tags can also be specified in place of the constants. Depending on the configuration, the operator can enter the desired values in the I/O field or read from the PLC. In this way, the operator can determine which recipe data records are exported.

**Procedure on HMI device**

As soon as the key is activated, the system function is triggered. The constants or tags are evaluated. All data records of Recipe 1 are exported to the orange.csv file. If the file already exists, it will be overwritten.

After exporting the data records, a system event is output.

## ExportDataRecordsWithChecksum (Panels, Comfort Panels, RT Advanced)

### Description

Exports one or all data records of a recipe to a CSV file and generates a checksum for each line in the file.

One file is created per recipe.

### Use in the function list

ExportDataRecordsWithChecksum (Recipe number/name, Data record number/name, File name, Overwrite, Output status message, Processing status)

### Use in user-defined functions

ExportDataRecordsWithChecksum Recipe_number_or_name, Data_record number_or_name, File_name, Overwrite, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which the data records are exported. Specify "0" if recipe data records are to be exported from all available recipes.

**Data record number/name**

Number or name of the recipe data record to be exported. Specify "0" if all recipe data records are to be exported.

**File name**

Name of the CSV file to which the recipe data records are exported. Enter the path and the file extension e.g. "C:\TEMP\Orange.CSV".

If a storage card is used as storage location, specify the storage location as follows: "\StorageCard\<FileName>".

If you define only a file name without specifying a path, the file is saved to the directory from which Runtime was started. If write access to this directory is not enabled in the Windows 7 operating system, the file is saved to the "VirtualStore" folder of the user directory.

When only one path for the export is specified, the file name is automatically created from the respective recipe name. This requires, for example, that the directory "D:\Temp\" has been created. If the directory "D:\Temp" does not exist, the directory name is used as the prefix for the file name, Temp_Recipe names.csv.

**Overwrite**

Determines whether an existing CSV file with the same name is overwritten:

0 (hmiOverwriteForbidden) = No: CSV file will not be overwritten. The export process will not be carried out.

1 (hmiOverwriteAlways) = Yes: CSV file is overwritten without a prompt for confirmation.

2 (hmiOverwriteWithConfirmation) = With confirmation: CSV file is not overwritten until confirmed.

**Output status message**

Determines whether a status message is output after the export:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

### Export format of the recipe data records

If ".csv" is chosen as a file extension for the export file, then only valid characters from the ANSI character set will be supported. This also applies to separators in decimal numbers and list elements. The separators used are defined in the country/regional settings of the operating system of the exporting computer.

You may also set "Unicode text" (".txt") format for the export file. This file format supports the WinCC and WinCC Runtime character set. Again, the separators used are specified in the country/regional settings of the operating system of the exporting computer. This file format always uses tab separators in list elements.

The corresponding file import function also supports the ".csv" and ".txt" (Unicode) file formats.

### Application example

Using a key, you want to export all data records and assign a checksum.

**Notes on configuring**

Configure the "ExportDataRecordsWithChecksum" system function on the "Press" event for the desired key. Transfer the following parameters:

- Recipe number/name = 1
- Data record number/name = 0
- File name = c:\temp\orange.csv
- Overwrite = 1
- Output status message = 1

Tags can also be specified in place of the constants. Depending on the configuration, the operator can enter the desired values in the I/O field or read from the PLC. In this way, the operator can determine which recipe data records are exported.

**Procedure on HMI device**

As soon as the key is activated, the system function is triggered. The constants or tags are evaluated. All data records of Recipe 1 are exported to the orange.csv file and assigned checksums. If the file already exists, it will be overwritten.

After exporting the data records, a system event is output.

## ExportImportUserAdministration (Panels, Comfort Panels, RT Advanced)

### Description

Exports all users of the user administration of the currently active project to the specified file or imports the users from the specified file to the currently active project.

Users, their passwords and rights are saved in the user administration.

The export/import of the user administration configuration encompasses all the settings. Existing objects (users, groups, logon settings, authorization levels) are overwritten during the import.

The imported users are valid immediately.

### Use in the function list

ExportImportUserAdministration (File name, Direction)

### Use in user-defined functions

ExportImportUserAdministration File_name, Direction

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**File name**

Name of the file which contains the passwords or to which the passwords are written. Enter the file location and the file extension (*.txt), for example, "C:\TEMP\Passwords.txt".

> **Note**
>
> If a storage card is used as file location, specify the file location as follows: "\StorageCard\<FileName".

**Direction**

Specifies whether passwords are exported or imported:

0 (hmiExport) = Export: Passwords are exported.

1 (hmiImport) = Import: Passwords are imported.

## GetBrightness (Panels, Comfort Panels, RT Advanced)

### Description

Reads the value of the brightness.

### Use in the function list

GetBrightness (Brightness)

### Use in user-defined functions

GetBrightness Brightness

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Brightness**

The tag to which the value is written.

## GetDataRecordFromPLC (Panels, Comfort Panels, RT Advanced)

### Description

Transfers the selected recipe data record from PLC to the storage medium of the HMI device.

### Use in the function list

GetDataRecordFromPLC (Recipe number/name, Data record number/name, Overwrite, Output status message, Processing status)

### Use in user-defined functions

GetDataRecordFromPLC Recipe_number_or_name, Data_record_number_or_name, Overwrite, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which recipe data records are transferred.

**Data record number/name**

Number or name of the recipe data record which is transferred from the PLC to the data medium of the HMI device.

**Overwrite**

Determines whether an existing recipe data record with the same name is overwritten:

0 (hmiOverwriteForbidden) = No: Recipe data record is not overwritten. The transfer process will not be carried out.

1 (hmiOverwriteAlways) = Yes: Recipe data record is overwritten without prompting.

2 (hmiOverwriteWithPrompting) = With confirmation: Recipe data record is not overwritten until confirmed.

**Output status message**

Determines whether a status message is output after the transfer:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

### Application example

You want to transfer a data record from the PLC to the data medium of the HMI device using a key.

**Notes on configuring**

Configure the "GetDataRecordFromPLC" system function on the "Press" event for the desired key. Transfer the following parameters:

Recipe number/name = 1

Data record number/name = 1

Overwrite = 1

Output status message = 1

Tags can also be specified in place of the constants. Depending on the configuration, the operator can enter the desired values in the I/O field or read from the PLC. In this way, the operator can determine which recipe data record is transferred from the PLC.

**Procedure on HMI device**

As soon as the key is activated, the system function is triggered. The constants or tags are evaluated and the first data record of Recipe 1 is transferred from the PLC to the data medium of the HMI device. If the recipe data record already exists, it will be overwritten.

A system event is output after the transfer.

## GetDataRecordName (Panels, Comfort Panels, RT Advanced)

### Description

Writes the name of the specified recipe and recipe data record to specified tags.

> **Note**
>
> If the recipe or the recipe data record do not exist, wildcards ("###") are written to the tags.

> **Note**
>
> Only internal tags or external tags are supported as tags.

### Use in the function list

GetDataRecordName (Recipe number, Data record number, Recipe name, Data record name, Processing status)

### Use in user-defined functions

GetDataRecordName Recipe_number, Data_record_number, Recipe_name, Data_record_name, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number**

Number of the recipe whose name is written in the specified tag.

**Data record number**

Number of the recipe data record, whose name is written to the specified tag.

**Recipe name**

The tag to which the recipe name is written. The tag must be of the STRING type.

**Data record name**

The tag to which the name of the recipe data record is written. The tag must be of the STRING type.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

### Application example

You want to output the names of the displayed recipes and the name of the displayed recipe data record on the HMI device.

Configure the following tags:

- "RecNumber" of type INTEGER
- "RecDataNumber" of type INTEGER
- "RecName" of type STRING
- "RecDataName" of type STRING

Configure a recipe view with the tags "RecNumber" for the recipe number and "RecDataNumber" for the data record number.

Configure the "GetDataRecordName" system function on the "Press" event for a button and pass the following parameters:

- Recipe number: RecNumber
- Data record number: RecDataNumber
- Recipe name: RecName
- Data record name: RecDataName

Configure two output fields and connect these to the "RecName" and "RecDataName" tags.

Select a recipe and a data record number from the recipe view. As soon as the button is activated, the system function is triggered and the name of the recipe and the recipe data record are displayed in both output fields.

## GetDataRecordTagsFromPLC (Panels, Comfort Panels, RT Advanced)

### Description

Transfers the values of the recipe data record loaded in the PLC to the corresponding recipe tags.

This system function is used, for example, during teach-in mode on a machine.

### Use in the function list

GetDataRecordTagsFromPLC (Recipe number/name, Processing status)

### Use in user-defined functions

GetDataRecordTagsFromPLC Recipe_number_or_name, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe data record whose values are written from the PLC to the tags.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## GetGroupNumber (Panels, Comfort Panels, RT Advanced)

### Description

Reads the number of the group to which the user logged on to the HMI device belongs, and writes it to the given tag.

### Use in the function list

GetGroupNumber (Tag)

### Use in user-defined functions

GetGroupNumber Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Tag**

The tag to which the number of the group is written.

## GetPassword (Panels, Comfort Panels, RT Advanced)

### Description

Writes the password of the user currently logged on to the HMI device in the given tag.

> **Note**
>
> Make sure that the value of the given tag is not displayed in another place in the project.

> **Note**
>
> The passwords of SIMATIC Logon users cannot be read.

> **Note**
>
> The "ReadPassword" system function is not available for devices as of device version 14.0.0.0.
>
> If this system feature is used in a project older than version V14, it is removed after migration to V14. The event linked to the system function is thereby invalidated. The "ReadPassword" system function appears to be faulty in the configuration. A warning is generated during compiling. The "ReadPassword" system function is no longer included in the compiled Runtime project.

### Use in the function list

ReadPassword (tag)

### Use in user-defined functions

GetPassword Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Tag**

The tag to which the password is written.

## GetUserName (Panels, Comfort Panels, RT Advanced)

### Description

Writes the user name of the user currently logged on to the HMI device in the given tag.

If the given tag has a control connection, the user name is also available in the PLC connection. This system function makes it possible, for example, to implement a user-dependent release of certain functionalities.

### Use in the function list

GetUserName (Tag)

### Use in user-defined functions

GetUserName Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Tag**

The tag to which the user name is written.

## GoToEnd (Panels, Comfort Panels, RT Advanced)

### Description

Executes the key function <End> on the HMI device.

This system function is used when the HMI device does not have this functionality by default.

The system function can only be used for the following function keys.

### Use in the function list

GoToEnd

### Use in user-defined functions

GoToEnd

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## GoToHome (Panels, Comfort Panels, RT Advanced)

### Description

Executes the key function <Home> on the HMI device.

This system function is used when the HMI device does not have this functionality by default.

The system function can only be used for the following function keys.

### Use in the function list

GoToHome

### Use in user-defined functions

GoToHome

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## ImportDataRecords (Panels, Comfort Panels, RT Advanced)

### Description

Imports one or all data records of a recipe from a CSV file or a TXT file.

When a path is specified, all records of the given directory are imported.

> **Note**
>
> **No check of import file for inconsistencies**
>
> The import function doesn't check whether values that were changed in the CSV file between the export and import are still valid, e.g. whether these are still within the defined limits.

### Use in the function list

ImportDataRecords (File name, Data record number/name, Overwrite, Output status message, Processing status)

### Use in user-defined functions

ImportDataRecords File_name, Data_record_number_or_name, Overwrite, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**File name**

Name of the file from which the recipe data records are imported. Also specify the storage location and the file extension (*.csv or *.txt), e.g. "C:\TEMP\Orange.csv".

For a Basic Panel, specify the file name as follows: "\USB_X60.1\<Name>"

For additional devices: If a memory card is used as the storage location, specify the storage location as follows: "\StorageCard\<Name>".

To import all recipe data records, specify only the path to the storage location without a file name: "C:\TEMP\". The system function imports all CSV files from this storage location.

**Data record number/name**

Number or name of the recipe data record to be imported. Specify "0" if all recipe data records are to be imported.

**Overwrite**

Determines whether existing recipe data records are to be overwritten:

0 (hmiOverwriteForbidden) = No: Recipe data records are not overwritten. The import process will not be carried out.

1 (hmiOverwriteAlways) = Yes: Recipe data records are overwritten without prompting.

2 (hmiOverwriteWithPrompting) = With confirmation: Recipe data records are not overwritten until confirmed.

**Output status message**

Determines whether a status message is output after the import:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. Use the return value, for example, to ensure that this system function has been successfully completed before executing other system functions:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

### Configurable objects

| Object | Event |
| --- | --- |
| Tag | Value change  High limit violated  Low limit violated |
| Function key (global) | Release  Press |
| Function key (local) | Release  Press |
| Screen | Loaded  Cleared |
| Screen object | Press  Release  Click  Change (or toggle for switch)  Switch on  Switch off  Enable  Disable |
| Scheduler | Time expired |

## ImportDataRecordsWithChecksum  (Panels, Comfort Panels, RT Advanced)

### Description

Imports one or all data records of a recipe from a CSV file with checksum and verifies the checksum.

### Use in the function list

ImportDataRecordsWithChecksum (File name, Data record number/name, Overwrite, Output status message, Processing status, verify checksum)

### Use in user-defined functions

ImportDataRecordsWithChecksum File_name, Data_record_number_or_name, Overwrite, Output_status_message, Processing_status, Verify_checksum

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**File name**

Name of the CSV file from which the recipe data records are imported. Enter the path and the file extension, for example, "C:\TEMP\Orange.CSV".

If a storage card is used as storage medium, specify the storage location as follows: "\StorageCard\<FileName>".

If you specify a directory instead of an individual CSV file, all files in the specified directory will be imported.

**Data record number/name**

Number or name of the recipe data record to be imported. Specify "0" if all recipe data records are to be imported.

**Overwrite**

Determines whether existing recipe data records are to be overwritten:

0 (hmiOverwriteForbidden) = No: Recipe data records are not overwritten. The import process will not be carried out.

1 (hmiOverwriteAlways) = Yes: Recipe data records are overwritten without prompting.

2 (hmiOverwriteWithConfirmation) = With confirmation: Recipe data records are not overwritten until confirmed.

**Output status message**

Determines whether a status message is output after the import:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. Use the return value, for example, to ensure that this system function has been successfully completed before executing other system functions:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

**Verify checksum**

Determines if the checksum should be verified during import:

0 (hmiFalse) = No: Checksum is not verified.

1 (hmiTrue) = Yes: Checksum is verified.

## IncreaseTag (Panels, Comfort Panels, RT Advanced)

### Description

Adds the given value to the value of the tags.

X = X + a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, help tags must be used. You can use the "SetTag" system function to assign the tag value to the auxiliary tags.

If you configure the system function on the events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual value of the tags is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

### Use in the function list

IncreaseTag (Tag, Value)

### Use in user-defined functions

IncreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Tag**

The tag to which the given value is added.

**Value**

The value that is added.

## InverseLinearScaling (Panels, Comfort Panels, RT Advanced)

### Description

Assigns a value to the tag X, which is calculated from the value of the given tag Y using the linear function X = (Y - b) / a.

The tags X and Y must not be identical. This system function is the inverse of the "LinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

### Use in the function list

InvertLinearScaling (X, Y, b, a)

### Use in user-defined functions

InverseLinearScaling X, Y, b, a

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**X**

The tag which is assigned the value calculated from the linear equation.

**Y**

The tag that contains the value used for calculation.

**b**

The value which is subtracted.

**a**

The value through which is divided.

### Example

The following program code assigns a value to the varX tag by means of the InverseLinearScaling function.

{

BYTE varX;

BYTE Yvalue = 10;

BYTE bvalue = 3;

BYTE avalue = 4;

//Inverse linear scaling

InverseLinearScaling (varX, Yvalue, bvalue, avalue);

printf ("varX = %d\r\n, varX);

...

}

The saved return value can be processed in the following code.

## InvertBit (Panels, Comfort Panels, RT Advanced)

### Description

Inverts the value of the given tag of the "Bool" type:

- If the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

### Use in the function list

InvertBit (Tag)

### Use in user-defined functions

InvertBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag whose bit is set.

### Example

The following program code inverts the value of the Boolean tag bStatus and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Get current value

bValue=myTag.Value

'Save current value

bSaved=bValue

'Invert Bit

InvertBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 0;

BOOL bSaved = bStatus;

//Invert variable

invertBit(bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

  ...

}

## InvertBitInTag (Panels, Comfort Panels, RT Advanced)

### Description

Inverts a bit in the given tag:

- If the bit in the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the bit in the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "InvertBit" system function instead.

### Use in the function list

InvertBitInTag (Tag, Bit)

### Use in user-defined functions

InvertBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which the given bit is set.

**Bit**

The number of the bit that is set.

When this system function is used in a user-defined function, the bits in a tag are counted from right to left. The counting begins with 0.

### Example

The following program code inverts a bit at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Get current value

bValue=myTag.Value

'Save current value

bSaved=bValue

'Invert Bit in position

bitposition=2

InvertBit myTag, bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bStatusWord;

BYTE bsaved = bStatusWord;

BYTE bitposition = 2;

//Invert bit in bitposition

InvertBitInTag (bStatusWord, bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatusWord, bsaved);

  ...

}

## LinearScaling (Panels, Comfort Panels, RT Advanced)

### Description

Assigns a value to the tag Y, which is calculated from the value of the given tag X using the linear function Y= (a *X) + b.

The inverse of this function is the "InvertLinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

### Use in the function list

LinearScaling (Y, a, X, b)

### Use in user-defined functions

LinearScaling Y, a, X, b

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Y**

The tag which is assigned the value calculated from the linear equation.

**a**

The value with which is multiplied.

**X**

The tag that contains the value used for calculation.

**b**

The value that is added.

### Example

The following program code uses the LinearScaling function to assign a value to the Yvar tag.

{

BYTE Yvar;

BYTE Xvalue = 10;

BYTE bvalue = 3;

BYTE avalue = 4;

// linear scaling

LinearScaling ( Yvar, avalue, Xvalue, bvalue);

printf ("Yvar = %d\r\n, Yvar);

...

}

The saved return value can be processed in the following code.

## LoadDataRecord (Panels, Comfort Panels, RT Advanced)

### Description

Loads the given recipe data record from the memory medium of the HMI device in the recipe tags. This system function is used, for example, to display a recipe data record in the recipe screen.

Activate the "Synchronize recipe view and recipe tags" option in the synchronization settings of the recipe. If this option is deactivated, the system function has no effect.

### Use in the function list

LoadDataRecord (Recipe number/name, Data record number/name, Processing status)

### Use in user-defined functions

LoadDataRecord Recipe_number_or_name, Data_record_number_or_name, Confirmation, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which a recipe data record is loaded.

**Data record number/name**

Number or name of the recipe data record which is loaded.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## LogOff (Panels, Comfort Panels, RT Advanced)

### Description

Logs off the current user on the HMI device.

### Use in the function list

Logoff

### Use in user-defined functions

Logoff

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## Logon (Panels, Comfort Panels, RT Advanced)

### Description

Logs on the current user on the HMI device.

### Use in the function list

Logon (Password, User name)

### Use in user-defined functions

Logon Password, User_name

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Password**

The tag from which the password for the user logging on is read. If the user is logged on, the password in the tag is deleted.

**User name**

The tag from which the user name for the user logging on is read.

## LookupText (Panels, Comfort Panels, RT Advanced)

### Description

Identifies an entry from a text list. The result depends on the value and on the selected runtime language. The result is saved to a tag of data type "String".

### Use in the function list

LookupText (Output text, Index, Language, Text list)

### Use in user-defined functions

LookupText Output_text, Index, Language, Text_list

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Output text**

The tag to which the result is written.

**Index**

The tag that defines the value of the list entry.

**Language**

Defines the runtime language in which the list entry is identified.

- Runtime language

  Language code as per VBScript reference, for example, "de-DE" for German (Germany) or "en-US" for English (United States of America). The selection depends on the activated runtime languages.
- Tag

  The tag that contains the language. Enter the runtime language as decimal value of the country ID, for example, 1031 for German - Standard, 1033 for English - USA. Details are available in the VBScript basics, "Locale identifier (LCID) diagram".
- Integer

  The number that corresponds to the order of runtime languages for language switching.   
  The selection depends on the activated runtime languages, for example, "0" for the language that appears when you first start runtime. You can find more information under the topic of "Languages in Runtime".

**Text list**

Defines the text list. The list entry is read from the text list.

## NotifyUserAction (Panels, Comfort Panels, RT Advanced)

### Description

This system function is used to log user actions that are not automatically logged in the Audit Trail. You can also use this system function to require the user to enter an acknowledgment or an electronic signature and a comment for the operator action. A requirement for the use of the system function is that the GMP-compliant configuration is activated under "Runtime settings > GMP".

If you use the "NotifyUserAction" system function in a function, the debugger may open if you cancel your input by clicking "Cancel". To compensate for this reaction, you can use the "On Error Resume Next" statement in a function. With this instruction, the next instruction is executed after a runtime error. If you use the "On Error Resume Next" statement, output of system events is also suppressed.

### Use in the function list

NotifyUserAction (Confirmation type, Mandatory commenting, Category, Object name, Description)

### Use in user-defined functions

NotifyUserAction Confirmation_type, Mandatory_commenting, Category, Object_name, Description

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Confirmation type**

Establishes how the action must be confirmed

0 = (None): No confirmation required, an entry is created in the Audit Trail

1 = (Acknowledgement): Acknowledgment, the user must acknowledge the action; an entry is created in the Audit Trail

2 = (Digital Signature): Electronic signature; a dialog window opens in which the user must enter the electronic signature - an entry is created in the Audit Trail

**Mandatory commenting**

Establishes if the user has to enter a comment. The comment is logged in the Audit Trail.

0 = (True): True; a dialog window opens in which the user must enter a comment

1 = (False): False; no comment required

**Category**

Category or class name of the modified object

**Object name**

Name of the modified object

**Description**

Text which describes the archiving user action.

## OpenAllLogs (Panels, Comfort Panels, RT Advanced)

### Description

Reestablishes the connection between WinCC and the logs. Logging can be continued.

> **Note**
>
> Run the "StartLogging" system function in order to restart logging.

### Use in the function list

OpenAllLogs

### Use in user-defined functions

OpenAllLogs

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

### Application example

You are in runtime and want to change the data medium on which the process values are logged.

**Notes on configuring**

Configure the "StopLogging" and "CloseAllLogs" system functions on the "Close Archive" button.

Configure the "OpenAllLogs" and "StartLogging" system functions on the "Open Archive" button.

As parameter transfer the respective name of the log that is to be stopped and started.

**Procedure on HMI device**

When the button "Close Archive" is pressed, the specified log is stopped and all open logs are closed. The data medium can be changed. You open all logs with the "Open Archive" button. Logging will be continued in the specified log.

## OpenCommandPrompt (Panels, Comfort Panels, RT Advanced)

### Description

Opens a Windows system prompt.

This function is used, e.g., to copy files or to call up another application.

### Use in the function list

OpenCommandPrompt

### Use in user-defined functions

OpenCommandPrompt

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## OpenControlPanel (Panels, Comfort Panels, RT Advanced)

### Description

Opens a dialog that you can use to edit selected Control Panel settings.

This system function lets you set the following on the HMI device:

- Properties and value of the IP address
- User identification on the network
- WinCC Internet settings

> **Note**
>
> **Project security**
>
> The "OpenControlPanelDialog" system function is used to bypass the SecureMode on the HMI device. Take the corresponding precautions to ensure the security of your project.

### Use in the function list

OpenControlPanelDialog (Dialog)

### Use in user-defined functions

-

### Parameters

**Dialog**

Sets the Control Panel dialog to be opened.

- PROFINET_X1: Setting of the IP address and Ethernet parameters
- PROFINET_X3: Setting of the IP address and Ethernet parameters; only for Comfort Panel KP 1500, TP 1500; TP1900, TP2200
- WinCC Internet settings: Setting for Web Server, e-mail notification, provided the HMI device supports these functions
- Network ID: Setting for identification on the network, provided the HMI device supports these functions

## OpenInternetExplorer (Panels, Comfort Panels, RT Advanced)

### Description

Opens the Internet Explorer on the HMI device.

If the Internet Explorer is already open, it will be closed and reopened when you call the system function.

> **Note**
>
> The Internet Explorer saves data temporarily in the DRAM file system of the HMI device, e.g. the last web sites that were be called up.
>
> This data can be saved using the "BackupRAMFileSystem" system function so that it is still available when the HMI device is restarted.

### Use in the function list

OpenInternetExplorer (Start page)

### Use in user-defined functions

OpenInternetExplorer Start_page

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Start page**

The page which is loaded when Internet Explorer is started, e.g. "www.siemens.com".

## OpenScreenKeyboard (Panels, Comfort Panels, RT Advanced)

### Description

Hides or shows the screen keyboard.

The screen keyboard remains open until the screen keyboard is explicitly closed. In this way, the screen keyboard can also be used in other applications.

### Use in the function list

OpenScreenKeyboard (Display mode)

### Use in user-defined functions

OpenScreenKeyboard Display_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Display mode**

Specifies whether the window is opened minimized or maximized with the screen keyboard:

0 (hmiScreenKeyboardMinimized) = Minimized

1 (hmiScreenKeyboardMaximized) = Maximized

## OpenTaskManager (Panels, Comfort Panels, RT Advanced)

### Description

Shows the task manager.

The task manager allows changing to other open applications on the HMI device.

> **Note**
>
> The appearance of the task manager depends on the operating system installed.

### Use in the function list

OpenTaskManager

### Use in user-defined functions

OpenTaskManager

Can be used if the configured device supports user-defined scripts. For additional information, refer to "Device dependency".

### Parameter

--

## PageDown (Panels, Comfort Panels, RT Advanced)

### Description

Executes the key function <Pagedown> on the HMI device.

This system function can only be used for function keys.

### Use in the function list

PageDown

### Use in user-defined functions

PageDown

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

-

## PageUp (Panels, Comfort Panels, RT Advanced)

### Description

Executes the key function <PageUp> on the HMI device.

This system function can only be used for function keys and tasks with a time trigger.

### Use in the function list

PageUp

### Use in user-defined functions

PageUp

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

-

## PrintReport (Panels, Comfort Panels, RT Advanced)

### Description

Prints the given report from the printer which is connected to the HMI device. The report is printed in the language which is set on the HMI device.

> **Note**
>
> If runtime is closed whilst log data are being printed using the system function, the report will cease to be supplied with data as soon as runtime stops.

### Use in the function list

PrintReport (Report)

### Use in user-defined functions

PrintReport Report

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Report**

Name of the report to be printed.

> **Note**
>
> If you have set up via the "Function list" dialog box a new report for the "PrintReport" function, when compiling, the following warning appears: "The report "Report_1" has no printed pages."
>
> In order to remedy the warning, open the "Report_1" via the project view and recompile the project.

## PrintScreen (Panels, Comfort Panels, RT Advanced)

### Description

Prints the screen currently being displayed on the HMI device from the printer which is connected to the HMI device.

Opened windows are also printed.

> **Note**
>
> The printer settings are taken over from the current settings in the Windows operation system.

### Use in the function list

PrintScreen

### Use in user-defined functions

PrintScreen

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

--

## ResetBit (Panels, Comfort Panels, RT Advanced)

### Description

Sets the value of a "Bool" type tag to 0 (FALSE).

### Use in the function list

ResetBit (Tag)

### Use in user-defined functions

ResetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The BOOL type tag which is set to 0 (FALSE).

### Example

The following program code sets the value of the Boolean tag bStatus to 0 by means of the ResetBit function and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Set value

bValue=1

myTag.Value=bValue

'Save current value

bSaved=bValue

'Reset Bit

ResetBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 1;

BOOL bSaved = bStatus;

//Reset bit

ResetBit (bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

...

}

## ResetBitInTag (Panels, Comfort Panels, RT Advanced)

### Description

Sets a bit in the specified tag to 0 (FALSE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "ResetBit" system function instead.

### Use in the function list

ResetBitInTag (Tag, Bit)

### Use in user-defined functions

ResetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which a bit is set to 0 (FALSE).

**Bit**

The number of the bit that is set to 0 (FALSE).

When this system function is used in a user-defined function, the bits in the specified tag will be counted from right to left independent of the PLC used. The counting begins with 0.

### Example

The following program code sets a bit to 0 at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Save current value

bValue=myTag.Value

bSaved=bValue

'Reset Bit

bitposition=2

ResetBitInTag myTag, bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bSaved;

BYTE bitposition = 2;

bSaved = GetTagByte("bStatusWord");

//Reset bit in bitposition

ResetBitInTag ("bStatusWord", bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",GetTagByte("bStatusWord"), bSaved);

  ...

}

## SafelyRemoveHardware (Panels, Comfort Panels)

### Description

Checks whether there is read or write access to the external storage medium. If there is no access, the external storage medium can be removed without data loss.

### Use in the function list

SafelyRemoveHardware(Path, Result)

### Use in user-defined functions

SafelyRemoveHardware Path, Result

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Result**

The tag in which the result is entered.

TRUE: The storage medium can be removed safely. A corresponding system alarm will be output.

FALSE: The storage medium cannot be removed safely. A corresponding system alarm will be output.

**Path**

Path of storage medium, e.g. \Storage Card USB\

## SaveDataRecord (Panels, Comfort Panels, RT Advanced)

### Description

Saves the current values of the recipe tags as data record to the memory medium of the HMI device.

This system function is used, for example, to save a recipe data record in the recipe screen.

Data records are only saved if the "Synchronization" option is activated in the recipe.

- When "Synchronization" is not activated, no data records are saved.

  To save data records, use either the "Save" button in the recipe control or the system function.

  | Synchronization | Button | System function |
  | --- | --- | --- |
  | Activated | Data records are saved. | Data records are saved. |
  | Deactivated | Data records are saved only if list view of the recipe view is displayed. | Data records are not saved.  "12" is returned as the processing status. |
- Alarms related to the operation are not displayed.

### Use in the function list

SaveDataRecord (Recipe number/name, Data record number/name, Overwrite, Output status message, Processing status)

### Use in user-defined functions

SaveDataRecord Recipe_number_or_name, Data_record_number_or_name, Overwrite, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe to which a recipe data record is saved.

**Data record number/name**

Number or name of the recipe data record which is saved. A new data record will be created if no record of this name or number was found in the recipe, independent of the value at the "Overwrite" parameter.

**Overwrite**

Specifies whether an existing data record is overwritten:

0 (hmiOverwriteForbidden) = No: The recipe data record is not overwritten, the data record is not saved.

1 (hmiOverwriteAlways) = Yes: The recipe data record is overwritten without a prompt for confirmation.

2 (hmiOverwriteWithConfirmation) = With confirmation: The recipe data record is overwritten only with confirmation by the user.

**Output status message**

Determines whether a status message is output after saving:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example to delay execution of other system functions, until this system function has been successfully completed.

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## SendEMail (Panels, Comfort Panels, RT Advanced)

### Description

Sends an e-mail from the HMI device to the given addressee.

This system function is used, for example, when, in the case of service, the alarm is to be passed on directly to the service technician.

> **Note**
>
> To send alarms as e-mails, the HMI system must have an e-mail client at its disposal.

### Use in the function list

SendEMail (Address, Subject, Text, Return address)

### Use in user-defined functions

SendEMail Address, Subject, Text, Return_address

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Address**

The e-mail address of the addressee.

**Subject**

The subject line of the e-mail.

**Text**

The text sent in the e-mail.

**Return address**

The e-mail address to which the addressee of this e-mail should send the reply.

## SetAcousticSignal (Panels, Comfort Panels, RT Advanced)

### Description

Configures the acoustic feedback of touch screen operation on the HMI device.

> **Note**
>
> The configuration that was set at Switch off is reestablished when restarting the HMI device.

### Use in the function list

SetAcousticSignal (Volume)

### Use in user-defined functions

SetAcousticSignal Volume

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Volume**

Determines whether and how loud an acoustic signal is emitted:

-1 (hmiToggle) = Toggle: Toggles the emission of the acoustic signal as follows: Muted > Quiet > Loud.

0 (hmiMuted) = Mute: no acoustic signal

1 (hmiQuiet) = Quiet: quiet acoustic signal

2 (hmiLoud) = Loud: loud acoustic signal

## SetAlarmReportMode (Panels, Comfort Panels, RT Advanced)

### Description

Switches the automatic reporting of alarms on the printer on or off.

### Use in the function list

SetAlarmReportMode (Mode)

### Use in user-defined functions

SetAlarmReportMode Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Mode**

Determines whether alarms are reported automatically on the printer:

0 (hmiDisablePrinting) = Reporting off: Alarms are not printed automatically.

1 (hmiEnablePrinting) = Reporting on: Alarms are printed automatically.

-1 (hmiToggle) = Toggle: Toggles between the two modes.

## SetBit (Panels, Comfort Panels, RT Advanced)

### Description

Sets the value of a "Bool" type tag to 1 (TRUE).

### Use in the function list

SetBit (Tag)

### Use in user-defined functions

SetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The BOOL type tag which is set to 1 (TRUE).

### Example

The following program code sets the value of the Boolean tag bStatus to 1 by means of the SetBit function and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Set value

bValue=0

myTag.Value=bValue

'Save current value

bSaved=bValue

'Set Bit

SetBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 0;

BOOL bSaved = bStatus;

//Set bit

SetBit (bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

...

}

## SetBitInTag (Panels, Comfort Panels, RT Advanced)

### Description

Sets a bit in the given tag to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "SetBit" system function instead.

### Use in the function list

SetBitInTag (Tag, Bit)

### Use in user-defined functions

SetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which a bit is set to 1 (TRUE).

**Bit**

The number of the bit that is set to 1 (TRUE).

When this system function is used in a user-defined function, the bits in the specified tag will be counted from right to left independent of the PLC used. The counting begins with 0.

> **Note**
>
> The guaranteed update of the tags used with actual process values is absolutely conditional in terms of reliable functionality. You should therefore configure the tag in an I/O field or assign the system function to a screen object, such as a button.
>
> If you have configured a short event such as the activation of an alarm for the system function you can only access the actual process values by setting the tag for continuous reading.

### Example

The following program code sets a bit to 1 at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Save current value

bValue=myTag.Value

bSaved=bValue

'Set Bit in tag

bitposition=1

SetBitInTag "bStatusWord", bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "& bSaved & "New Value: " & bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bSaved;

BYTE bitposition = 1;

bSaved = GetTagByte("bStatusWord");

//Reset bit in bitposition

SetBitInTag ("bStatusWord", bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",GetTagByte("bStatusWord"), bSaved);

}

## SetBrightness (Panels, Comfort Panels, RT Advanced)

### Description

Determines the brightness of the display.

> **Note**
>
> The configuration that is set in the Control Panel / Start Center will be reestablished when you restart the HMI device.

For Basic Panels 2nd Generation, Mobile Panels and Comfort Panels:

The value for the system function "SetBrightness" can be set between 0% and 100%. The set value is transferred to the HMI device. The brightness settings on the HMI device can be viewed and edited in "Start Center > Settings > Display". The HMI devices support a brightness setting between 10% and 100%.

If the system function "SetBrightness" is assigned a value of 0%, the display of the HMI device is switched off by default in Runtime. If the operator touches the display, the display switches to the previous brightness setting.

If the system function "SetBrightness" is assigned a value between 1% and 10% and the operator opens the display settings in the Start Center, brightness is reset to 10%.

### Use in the function list

SetBrightness (value)

### Use in user-defined functions

SetBrightness Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Value**

New value for the brightness.

## SetConnectionMode (Panels, Comfort Panels, RT Advanced)

### Description

Connects or disconnects the given connection.

> **Note**
>
> A connection to the PLC cannot be established until the "Online" operating mode has been set on the HMI device. Use the "SetDeviceMode" system function for this purpose.
>
> If the connection is loaded in "Offline" mode, the connection is closed again each time the mode switches to "Offline". To re-establish the connection after switching to "Online" mode, set the connection again to "Online" mode.

### Use in the function list

SetConnectionMode (Mode, Connection)

### Use in user-defined functions

SetConnectionMode Mode, Connection

> **Note**
>
> **Good Manufacturing Practice**
>
> The use of the "SetConnectionMode" system function in user-defined functions is not GMP compliant.
>
> When using the "SetConnectionMode" system function in user-defined functions, disable the Good Manufacturing Practice in the runtime settings of the HMI device.

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Mode**

Specifies whether a connection to the PLC is established or disconnected. For devices with Windows CE and for Runtime Advanced, this parameter cannot be supplied via a tag of the data type BOOL.

0 (hmiOnline) = online: Connection is established.

1 (hmiOffline) = offline: Connection is disconnected.

**Connection**

The PLC to which the HMI device is connected. You specify the name of the PLC in the connection editor.

### Multiple use of the system function in a user-defined function

If you use the "SetConnectionMode" system function for different connections, it may be possible that not all system functions are executed correctly. Proceed as follows to prevent this situation:

1. Create a tag with the start value "0".
2. Configure the "SetConnectionMode" system function on the "Value change" event of the HMI tags. If you want to disconnect three connections, for example, you must configure the system function three times.
3. In the user-defined function, apply the "InvertBit" system function to the HMI tag.

### Application example

Two typical application examples for this system function are as follows:

- Test

  As long as no PLC is connected to the HMI device, no error messages will be output during the test on the HMI device. If the HMI device is connected to a PLC, the connection to the PLC can be established by pressing a key.
- Commissioning

  Several PLCs are to be configured for a system. At first, all PLCs except one are configured "Offline". After commissioning of the first PLC, the connection to each of the other PLCs is established by pressing a key. In this way, the other PLCs are started up one after another.

## SetDataRecordTagsToPLC (Panels, Comfort Panels, RT Advanced)

### Description

Transfers the values of the recipe tags to the PLC. The recipe tags contain the values of the data record which is displayed on the HMI device.

### Use in the function list

SetDataRecordTagsToPLC (Recipe number/name, Processing status)

### Use in user-defined functions

SetDataRecordTagsToPLC Recipe_ number_or_name, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which recipe data record is transferred to the PLC.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## SetDataRecordToPLC (Panels, Comfort Panels, RT Advanced)

### Description

Transfers the given recipe data record directly from the data medium of the HMI device to the PLC with which the HMI device is connected.

> **Note**
>
> The values of the recipe data record don't need to be displayed on the HMI device.

### Use in the function list

SetDataRecordToPLC (Recipe number/name, Data record number/name, Output status message, Processing status)

### Use in user-defined functions

SetDataRecordToPLC Recipe_number_or_name, Data_record_number_or_name, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe from which recipe data record is transferred to the PLC.

**Data record number/name**

Number or name of the recipe data record transferred to the PLC.

**Output status message**

Determines whether a status message is output after the transfer:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## SetDaylightSavingTime (Panels, Comfort Panels, RT Advanced)

### Description

The system function "SetDaylightSavingTime" changes the setting of the HMI device from daylight saving to standard time and vice versa.

Time settings will take place immediately following system function.

> **Note**
>
> The "SetDaylightSavingTime" system function does not support time zones without daylight saving time.

> **Note**
>
> **Windows 7**
>
> The system function "SetDaylightSavingTime" is not supported for PC-based HMI devices under Windows 7.

### Use in the function list

SetDaylightSavingTime(DaylightSavingTime)

### Use in user-defined functions

SetDaylightSavingTime Daylight_saving_time

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Daylight Saving Time**

Determines whether Daylight Saving Time is set on the HMI device:

0 = Daylight Saving Time is not activated

1 = Daylight Saving Time is activated

## SetDeviceMode (Panels, Comfort Panels, RT Advanced)

### Description

Toggles the operating mode on the HMI device. The following types of operation are possible: "Online", "Offline" and "Loading".

### Use in the function list

SetDeviceMode (Operating mode)

### Use in user-defined functions

SetDeviceMode Operating_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Operating mode**

Specifies the operating mode of the HMI device. For devices with Windows CE, this parameter cannot be supplied via tag of data type BOOL.

0 (hmiOnline) = online: The connection to the PLC is established. The configured connection status is always set in this process. The states that were last used in Runtime are not considered.

1 (hmiOffline) = offline: The connection to the PLC is disconnected.

2 (hmiTransfer) = Load: A project can be transferred from the configuration computer to the HMI device.

> **Note**
>
> If you use a PC as an HMI device, the runtime software will be exited when you switch operating mode after "Load".

## SetDisplayMode (Panels, Comfort Panels, RT Advanced)

### Description

Changes the settings of the screen in which the runtime software runs.

The runtime software runs in full-screen mode as default. The Windows task switch is disabled.

### Use in the function list

SetDisplayMode (Layout)

### Use in user-defined functions

SetDisplayMode Display_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Display mode**

Determines the settings for the screen in which the runtime software runs.

1 (hmiScreenFull): Full screen: Title bar of the screen is not visible

2 (hmiScreenMaximized): Maximized

3 (hmiScreenRestore): Restore: The last used screen setting is used. This layout can only be used when the window is displayed minimized or maximized.

4 (hmiScreenMinimized): Minimized

5 (hmiScreenAutoAdjust): Automatic: The size of the window is set so that all screen objects in it will be visible.

6 (hmiScreenOnTop): Foreground; either the window appears in the foreground or the program icon associated with the window flashes on the taskbar depending on the Windows setting. The setting can be changed in the Windows configuration and applies to all Windows applications.

## SetLanguage (Panels, Comfort Panels, RT Advanced)

### Description

Toggles the language on the HMI device. All configured text and system events are displayed on the HMI device in the newly set language.

### Use in the function list

SetLanguage (Language)

### Use in user-defined functions

SetLanguage Language

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Language**

Determines which language is set on the HMI device. The following specifications are possible:

- -1 (hmiToggle) = Toggle: Changes to the next language. The sequence is determined during configuration in the "Project languages" editor.
- Number you have defined under "Languages and fonts" in the "Runtime Settings" editor. Changes to the language with the given number.
- Language you have defined under "Languages and fonts" in the "Runtime Settings" editor.
- Language abbreviation in accordance with the VBScript5 reference: This changes to the language corresponding to the specified language code, e.g. "de-DE" for German (Germany) or "en-US" for English (United States).

  An overview of the language abbreviations is available in the basic information of VBScript under the topic "Area diagram-ID (LCID) Diagram".

## SetPLCDateTime (Panels, Comfort Panels, RT Advanced)

### Description

Changes the data and the time of the linked PLC

The system function "SetPLCDateTime" can only be configured for the following PLCs:

- SIMATIC S7-1200
- SIMATIC S7-1500

### Use in the function list

SetPLCDateTime (connection, time)

### Use in user-defined functions

-

### Parameters

****Connection****

Connection of PLC and HMI device.

****Time****

Transfers the date and the time of the HMI device to the PLC. The PLC applies the date and the time of the HMI device.

## SetRecipeTags (Panels, Comfort Panels, RT Advanced)

### Description

Changes the status of the recipe tags from "Online" to "Offline" and vice versa.

This system function is used, for example, when recipe data record values are fine tuned when starting up a machine.

### Use in the function list

SetRecipeTags (Recipe number/name, Status, Output status message, Processing status)

### Use in user-defined functions

SetRecipeTags Recipe_number_or_name, Status, Output_status_message, Processing_status

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Recipe number/name**

Number or name of the recipe in which the recipe data record is saved.

**Status**

Determines the status of the recipe tags:

0 (hmiOnline) = online: Value changes of the recipe tags are transferred immediately to the PLC connected to the HMI device.

1 (hmiOffline) = offline: Value changes to the recipe tags are only transferred to the PLC connected to the HMI device when, for example, the "SetDataRecordTagsToPLC" system function is executed.

**Output status message**

Determines whether a status message is output after saving:

0 (hmiOff) = Off: Status message is not output.

1 (hmiOn) = On: Status message is output.

**Processing status**

Returns the processing status of the system function. You can use the return value, for example, to delay execution of other system functions until this system function has been successfully completed:

2 = System function is being performed.

4 = System function was successfully completed.

12 = System function was not performed because an error has occurred.

You can only use an HMI tag for the parameter.

## SetScreenKeyboardMode (Panels, Comfort Panels, RT Advanced)

### Description

Enables or disables the automatic display of the screen keyboard on the HMI device.

This system function is also used to prevent the display of the screen keyboard, e.g. because an external keyboard is connected to the HMI device.

> **Note**
>
> To enable the "SetScreenKeyboardMode" ("SetScreenKeyboardMode") system function on an HMI other than a Touch Panel device, set the "Use on-screen keyboard" check box in the "Runtime settings" dialog of the device settings.

### Use in the function list

SetScreenKeyboardMode (Mode)

### Use in user-defined functions

SetScreenKeyboardMode Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Mode**

Determines whether the screen keyboard is hidden or shown:

0 (hmiOff) = Off: Screen keyboard is hidden

1 (hmiOn) = On: Screen keyboard is shown

-1 (hmiToggle) = Toggle: Toggles between the two modes.

## SetTag (Panels, Comfort Panels, RT Advanced)

### Description

Assigns a new value to the given tag.

> **Note**
>
> This system function can be used to assign strings and numbers, depending on the type of tag.

### Use in the function list

SetTag (Tag, Value)

### Use in user-defined functions

SetTag Tag, Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag to which the given value is assigned.

**Value**

The value which the given tag is assigned.

> **Note**
>
> The "SetTag" system function is only executed after a connection has been established.

### Example

The following program code uses the SetTag function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag.

{

BOOL ok;

BOOL bvalue;

//Set the tag to true

ok = SetTag("gs_tag_bit", TRUE);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

bvalue = GetTagBit("gs_tag_bit");

printf ("Value of gs_tag_bit: %d\r\n", bvalue);

}

else

{

  // failed

  printf ( "Error - function failed." );

}

...

}

The saved return value can be processed in the following code.

## ShiftAndMask (Panels, Comfort Panels, RT Advanced)

### Description

This system function converts the input bit pattern of the source tags into an output bit pattern of the target tags. This involves bit shifting and masking.

> **Note**
>
> If the source and target tag have a different number of bits, using the system function in the target tag can result in a violation of the value range.

### Use in the function list

ShiftAndMask (Source tag, Target tag, Bits to shift, Bits to mask)

### Use in user-defined functions

ShiftAndMask Source_tag, Target_tag, Bits_to_shift, Bits_to_mask

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Source tag**

The tag includes the input bit pattern. Integer-type tags, e.g. "Byte", "Char", "Int", "UInt", "Long" and "ULong" are permitted.

Example: The actual value 72 is set at the 16-bit integer source tag: 0000000001001000.

**Target tag**

The output bit pattern is saved in the tag. Integer type tags, e.g. "Byte", "Char", "Int", "UInt", "Long" and "ULong" are permitted.

Example: The shifted input bit pattern is multiplied by the bit mask, with bit-by-bit logical AND operation: 0000000000001001. The resultant decimal value "8" is saved to the target tag.

Please note the following:

- The source and target tags have the same number of bits.
- The number of bits to shift is less than the number of bits in the source tag and target tag.
- Bits to mask does not have more bits than the source tag and the target tag.

**Bits to shift**

Number of bits by which the input bit pattern is shifted right. A negative value shifts the input bit pattern to the left.

Example: "Bits to shift" has the value "+3". The input bit pattern is shifted right by three bits when the system function is called: 0000000000001001.  
Bits to the left are padded with "0". Three bits are truncated on the right. The new decimal value is "9".

> **Note**
>
> The left bit is "1" in a source tag of the data type with negative signed integer. This sign bit is padded with "0" when the bits are shifted right. The sign changes to "+".

**Bits to mask**

An integer serves as bit mask. The bit pattern is used to multiply the shifted input bit pattern. Example: Integer "2478" with the bit pattern "0000100110101110".

You can enter the bit mask in three different ways:

- Hexadecimal: First enter the prefix "0h" or "0H", followed by an optional space for better readability. Then group the bit pattern in blocks of four (0000)(1001)(1010)(1110) and set each block in hexadecimal code: (0)(9)(A)(E). Only the characters 0-9, A-F, a-f are allowed: "0h 09AE".
- Binary: First enter the prefix "0b" or "0B", followed by an optional space for better readability. Then group the binary bit pattern into blocks of four 0000 1001 1010 1110 with spaces in between as a check. Only the characters "0" or "1" are allowed: "0b 0000 1001 1010 1110".
- Decimal: Enter the value "2478" directly, without a prefix.

> **Note**
>
> If you change the device version of the target HMI device after configuration (e.g."13.1.0" to "13.0.0" or vice versa), you must check and test the parameters of this system function.
>
> You can use the "Char" and "Word" data types for the "Source tag" and "Target tag" parameters as of device version 13.1.0. In the device versions before 13.1.0, these parameters must be assigned other data types:
>
> - Use "SInt" instead of "Char"
> - Use "Int" instead of "Word"
>
> Otherwise, there may be unwanted effects, for example incorrect or unexpected behavior of the configured system functions.

## ShowAlarmWindow (Panels, Comfort Panels, RT Advanced)

### Description

Hides or shows the alarm window on the HMI device.

### Use in the function list

ShowAlarmWindow (Object name, Display mode)

### Use in user-defined functions

ShowAlarmWindow Object_name, Display_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Object name**

Name of the alarm view which is hidden or shown.

**Display mode**

Determines whether the alarm window is hidden or shown:

0 (hmiOff) = Off: Alarm view is hidden

1 (hmiOn) = On: Alarm view is shown

-1 (hmiToggle) = Toggle: Toggles between the two modes

## ShowOperatorNotes (Panels, Comfort Panels, RT Advanced)

### Application

Displays the tooltip configured for the selected object.

If the system function is configured on a function key, the tooltip for the screen object that currently has the focus is displayed. If a tooltip is configured for the screen itself, you can switch to this text by pressing <Enter> or by double-clicking on the help window.

If the system function is configured on a button, only the tooltip for the current screen is displayed. If a tooltip is configured on the button itself, initially only the tooltip for the button is displayed. You can press <Enter> or double-click on the help window to switch to the tooltip for the current screen.

> **Note**
>
> No other screen object can be used while the help window is open. To use the screen object, close the help window.

### Closing the help window

You can close the help window in the following ways:

Using the keys:

- By pressing the <HELP> key again
- By pressing the <ESC> key

Using the touch screen:

- By pressing the ![Closing the help window](images/36155749259_DV_resource.Stream@PNG-de-DE.png) button

### Use in the function list

ShowOperatorNotes (Layout)

### Use in user-defined functions

ShowOperatorNotes Display_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Display mode**

Determines whether the configured tooltip is hidden or shown:

0 (hmiOff) = Off: Configured tooltip is hidden

1 (hmiOn) = On: Configured tooltip is shown

-1 (hmiToggle) = Toggle: Toggles between the two modes

## ShowPopUpScreen (Panels, Comfort Panels, RT Advanced)

### Description

Opens the pop-up-screen, for example, when a button is pressed.

You can enter a constant value or assign a tag as coordinates.   
If the configured pop-up screen is not visible or only partially visible, the coordinates are set to 0.0.

Regardless of the size of the permanent area, the start position of the coordinates is always 0.0.

### Use in the function list

ShowPopupScreen (Name of the screen, X coordinate, Y coordinate, Display mode, Animation, Animation speed)

### Use in user-defined functions

ShowPopupScreen Screen_name, X_coordinate, Y_coordinate, Display_mode, Animation, Animation_speed

### Parameters

**Name of the screen**

Specifies the name of the pop-up screen that appears in Runtime when a button is pressed.

**X coordinate**

Position of the pop-up screen in the current screen on the X axis

**Y coordinate**

Position of the pop-up screen in the current screen on the X axis

**Display mode**

Specifies the mode for the pop-up screen:

Switching

Off

On

**Animation**

Specifies the direction from which the pop-up screen is shown:

Off

Left

Top

Right

Bottom

**Animation speed**

Specifies the speed at which the pop-up screen is shown:

Slow

Medium

Fast

## ShowPopupScreenSizable (Panels, Comfort Panels, RT Advanced)

### Description

Opens the pop-up screen with a defined size. You can open a pop-up screen in a different size with this system function; the scroll bars are displayed for navigating in the content of the pop-up screen.

You can enter a constant value or assign a tag as coordinates. If the configured pop-up screen is not visible or only partially visible, the coordinates are set to 0.0. Regardless of the size of the permanent area, the start position of the coordinates is always 0.0.

You also define the displayed width and height of the pop-up screen, which can deviate from the sizes of the configured pop-up screen. The scroll bars are displayed in the pop-up screen in this case.

> **Note**
>
> **Operation on HMI devices with keys**
>
> You scroll in pop-up screens using the keyboard shortcut <ALT>+<arrow key>.

### Display only one scroll bar

If you specify only one of the sizes smaller than the size of the configured pop-up screen in the parameters of the system function, the two scroll bars are displayed in the pop-up screen. You have two options to configure only one scroll bar in the pop-up screen:

- Reduce the width/height of the configured pop-up screen by the size of the device-specific scroll bar.
- Specify a value that corresponds to the actual size of the pop-up screen for one of the size parameters and add the device-specific size of the scroll bar. You specify the value for the other size as needed.

  **Example:**

  You want to open a pop-up screen with the configured size of 500 x 420 in the size 500 x 300 with a vertical scroll bar. Specify the value 534 for the width parameter which corresponds to the actual width of the configured pop-up screen plus the size of the scroll bar of 34. Enter the value 300 for the height. The pop-up screen is opened in the size 500 x 300 in Runtime and only the vertical scroll bar is displayed.

  | Device type (version V14) | Width | Height |
  | --- | --- | --- |
  | HMI devices with 4" display Comfort Panels with 19" display  Runtime Advanced | 25 | 25 |
  | HMI devices with 9" display  Comfort Panels with 15" display  Comfort Panels with 22" display | 27 | 27 |
  | HMI devices with 7" display  HMI devices with 12" display | 34 | 34 |

### Use in the function list

ShowPopupScreenSizable (Name of the screen, X coordinate, Y coordinate, Width, Height, Display mode, Animation, Animation speed)

### Use in user-defined functions

ShowPopupScreenSizable Screen_name, X_coordinate, Y_coordinate, Width, Height, Display_mode, Animation, Animation_speed

### Parameters

**Name of the screen**

Specifies the name of the pop-up screen that appears in Runtime when a button is pressed.

**X coordinate**

Position of the pop-up screen in the current screen on the X axis

**Y coordinate**

Position of the pop-up screen in the current screen on the X axis

****Width****

Specifies the width of the pop-up screen. The maximum width must not exceed the screen width of the configured HMI device.

****Height****

Specifies the height of the pop-up screen. The maximum height must not exceed the screen height of the configured HMI device.

**Display mode**

Specifies the mode for the pop-up screen:

Switching

Off

On

**Animation**

Specifies the direction from which the pop-up screen is shown:

Off

Left

Top

Right

Bottom

**Animation speed**

Specifies the speed at which the pop-up screen is shown:

Slow

Medium

Fast

## ShowSlideInScreen (Panels, Comfort Panels, RT Advanced)

### Description

Calls the slide-in screen, for example, when operating a button.

### Use in the function list

ShowSlideinScreen (screen name, mode)

### Use in user-defined functions

ShowSlideInScreen SlideInScreen_name, Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen name**

Specifies the slide-in screen that appears in Runtime when a button is pressed:

Top Slide-in screen

Bottom Slide-in screen

Left Slide-in screen

Right Slide-in screen

**Mode**

Specifies the mode for the slide-in screen:

Switching

Off

On

## ShowSoftwareVersion (Panels, Comfort Panels, RT Advanced)

### Description

Hides or shows the version number of the runtime software.

Use this system function if during servicing, for example, you required the version of the runtime software used.

### Use in the function list

ShowSoftwareVersion (Display mode)

### Use in user-defined functions

ShowSoftwareVersion Display_mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Display mode**

Determines whether the version number is shown:

0 (hmiOff) = Off: Version number is not shown

1 (hmiOn) = On: Version number is shown

-1 (hmiToggle) = Toggle: Toggles between the two modes

## ShowSystemAlarm (Panels, Comfort Panels, RT Advanced)

### Description

Displays the value of the parameter passed as a system event to the HMI device.

### Use in the function list

ShowSystemAlarm (Text/value)

### Use in user-defined functions

ShowSystemAlarm Text_or_value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Text/Value**

The text or the value, which was output as a system alarm.

## ShowSystemDiagnosticsWindow (Panels, Comfort Panels)

### Description

Hides or shows the system diagnostic window on the HMI device. The system diagnostic view is only available in the global screen for Comfort Panels and for WinCC Runtime Advanced.

### Use in the function list

ShowSystemDiagnosticsWindow (Screen object)

### Use in user-defined functions

ShowSystemDiagnosticsWindow Object_name

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen object**

Name of the system diagnostic window which is hidden or shown.

## StartLogging (Panels, Comfort Panels, RT Advanced)

### Description

Starts the logging of data or alarms in the specified log. The function can also be applied to audit trails.

You can interrupt logging at runtime using the "StopLogging" system function.

### Use in the function list

StartLogging (Log type, Log)

### Use in user-defined functions

StartLogging Log_type, Log

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

2 (hmiAudittrailArchive) = Audit trail

**Log**

Name of the log which is started.

## StartNextLog (Panels, Comfort Panels, RT Advanced)

### Description

Stops the logging of data or alarms for the given log.

Logging is continued in the next log of the segmented circular log you configured for the specified log.

If you did not configure a segmented circular log for the specified log, the system function has no effect.

### Use in the function list

StartNextLog (Log type, Log)

### Use in user-defined functions

StartNextLog Log_type, Log

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

**Log**

Name of the log for which the logging is stopped and continued in the next log.

## StartProgram (Panels, Comfort Panels, RT Advanced)

### Description

Starts the specified program on the HMI device.

The runtime software continues running in the background. Alarms continue to be output and data continues to be updated.

When the given application is exited, the screen which was active during the performance of the system function is displayed on the HMI device.

This system function is used, for example, to edit recipe data records in MS Excel on the HMI device.

> **Note**
>
> If Windows CE is installed on the HMI device, during the configuration it must be checked whether the desired application can be started with this system function.
>
> This system function allows all applications to be started which can be started in the "Execute" dialog of Windows CE.
>
> The application to be started must be installed on the HMI device.

> **Note**
>
> If an application is not executed via the "StartProgram" function on a Mobile Panel or Comfort Panel, check the path specification of the system function. On Mobile Panels and Comfort Panels, some applications are located in the folder "\flash\addons".

### Use in the function list

StartProgram (Program name, Program parameters, Display mode, Wait for program to end)

### Use in user-defined functions

StartProgram Program_name, Program_parameters, Display_mode, Wait_for_program_to_end

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Program name**

Name and path of the program which is started. Upper and lower case are taken into account in this parameter.

> **Note**
>
> If the path contains spaces, the program can only be started correctly if the path is specified in inverted commas, e.g. "C:\Program Files\START\start.exe".

**Program parameters**

The parameters you transfer at the start of the program, for example a file that is opened after the start of the program.

The description of the necessary parameters is found in the documentation of the program to be started.

**Display mode**

Determines how the program window is displayed on the HMI device:

0 (hmiShowNormal) = Normal

1 (hmiShowMinimized) = Minimized

2 (hmiShowMaximized) = Maximized

3 (hmiShowMinimizedAndInactive) = Minimized and inactive

**Wait for program to end**

Determines whether there is a change back to the project after the called up program has ended:

0 (hmiNo) = No: No change to project

1 (hmiYes) = Yes: Change to project

> **Note**
>
> The "Wait for program to end" parameter is only available for Runtime Advanced and Panels.

## StopLogging (Panels, Comfort Panels, RT Advanced)

### Description

Stops the logging of process values or alarms in the specified log. The function can also be applied to audit trails.

The "StartLogging" system function is used to resume logging at runtime.

> **Note**
>
> When logging is stopped, a connection between WinCC and the log files or log database still exists. Use the "CloseAllLogs" system function to disconnect this connection.

### Use in the function list

StopLogging (Log type, Log)

### Use in user-defined functions

StopLogging Log_type, Log

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Log type**

Determines the type of log:

0 (hmiTagArchive) = Tag log

1 (hmiAlarmArchive) = Alarm log

2 (hmiAudittrailArchive) = Audit trail

**Log**

Name of the log that is stopped.

### Application example

You are in runtime and want to change the data medium on which the process values are logged.

**Notes on configuring**

Configure the "StopLogging" and "CloseAllLogs" system functions on the "Close Archive" button.

Configure the "OpenAllLogs" and "StartLogging" system functions on the "Open Archive" button.

As parameter transfer the respective name of the log that is to be stopped and started.

**Procedure on HMI device**

When the button "Close Archive" is pressed, the specified log is stopped and all open logs are closed. The data medium can be changed. The "Open Archive" button opens all logs and continues logging in the specified log.

## StopRuntime (Panels, Comfort Panels, RT Advanced)

### Description

Exits the runtime software and thereby the project running on the HMI device.

### Use in the function list

StopRuntime (Mode)

### Use in user-defined functions

StopRuntime Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Mode**

Determines whether the operating system is shut down after exiting runtime.

0 (hmiStopRuntime) = Runtime: Operating system is not shut down

1 (hmiStopRuntimeAndOperatingSystem) = Runtime and operating system: The operating system is shut down (not possible with WinCE)

### Example

The following program code shuts down Runtime and the operating system.

{

//Stop runtime and shutdown

StopRuntime (hmiStopRuntimeAndOperationSystem);

}

The saved return value can be processed in the following code.

## TerminatePROFIsafe (Panels, Comfort Panels, RT Advanced)

### Description

Disconnects the PROFIsafe connection for fail-safe operation between a KTP Mobile Panel and the PLC.

After execution of the system function "TerminatePROFIsafe", the connector of the KTP Mobile Panel can be removed from the PLC without the system signaling an error.

### Use in the function list

TerminatePROFIsafe

### Use in user-defined functions

TerminatePROFIsafe

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

--

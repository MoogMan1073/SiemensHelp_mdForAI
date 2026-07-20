---
title: "Using system functions (RT Unified)"
package: SysFuncWCCUenUS
topics: 93
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using system functions (RT Unified)

This section contains information on the following topics:

- [Working with function lists (RT Unified)](#working-with-function-lists-rt-unified)
- [System functions (RT Unified)](#system-functions-rt-unified)

## Working with function lists (RT Unified)

This section contains information on the following topics:

- [Basics of the function list (RT Unified)](#basics-of-the-function-list-rt-unified)
- [Input support (RT Unified)](#input-support-rt-unified)
- [Configuring a function list (RT Unified)](#configuring-a-function-list-rt-unified)
- [Editing a function list (RT Unified)](#editing-a-function-list-rt-unified)
- [Using a screen item to specify the value of a parameter (RT Unified)](#using-a-screen-item-to-specify-the-value-of-a-parameter-rt-unified)
- [Adapt the function list to changed scripts (RT Unified)](#adapt-the-function-list-to-changed-scripts-rt-unified)

### Basics of the function list (RT Unified)

#### Introduction

A function list performs one or more functions when the configured event occurs.

The following are available:

- System functions
- Functions which you configure in global modules
- Functions which you configure in script modules

#### Principle

The function list is configured for an event of the following objects:

- Screen
- Screen object
- Task

You can configure exactly one function list for each event. Which events are available depends on the selected object. Events occur only when the project is in runtime.

Events include:

- Execution of a task
- Pressing of a button

The function list is opened in the Inspector window under "Properties &gt; Events" as soon as an object has been selected.

#### Layout

![Layout](images/124694740747_DV_resource.Stream@PNG-en-US.png)

The function list is divided into two columns. In the "Name" column you see the names of the functions and the corresponding parameters.

In the Values column you assign values to the parameters. You use different parameter types depending on the parameter.

The following buttons are located above the function list:

| Button | Function |
| --- | --- |
| ![Layout](images/124747113355_DV_resource.Stream@PNG-de-DE.png) | Move function up |
| ![Layout](images/124747122443_DV_resource.Stream@PNG-de-DE.png) | Move function down |
| ![Layout](images/151911027851_DV_resource.Stream@PNG-de-DE.png) | Display parameters |
| ![Layout](images/151911918347_DV_resource.Stream@PNG-de-DE.png) | Hide parameter |
| ![Layout](images/151911935115_DV_resource.Stream@PNG-de-DE.png) | Convert function list to script |
| ![Layout](images/124755600395_DV_resource.Stream@PNG-de-DE.png) | Delete function list |

If the function list cannot be edited, the buttons are locked. This is the case, for example, with reference projects.

---

**See also**

[Editing a function list (RT Unified)](#editing-a-function-list-rt-unified)
  
[System functions (RT Unified)](#system-functions-rt-unified)
  
["Scripts" editor (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified)

### Input support (RT Unified)

The function list supports you in:

- Function input
- Input of parameter values
- Troubleshooting

#### Function input

You have several options for entering a function in the function list:

- Enter the complete or partial name of the function.

  Autocomplete is supported.
- Select the "&lt;Add function&gt;" field and open the selection menu.

  The available functions are sorted by category.
- Select the "&lt;Add function&gt;" field and select the list icon.

  The available functions are displayed in alphabetical order.

The system functions provided in the function list differ depending on the object selected. For example, system functions of the "Screen" category are only available for screens and screen items.

#### Input of parameter values

The parameters required in functions are displayed in the function list and differ depending on the function selected.

You assign a value to each parameter.

The parameter type determines which values the parameter can accept.

The parameter type is either fixed by default or you can choose between several types.

Which parameter types are available depends on the respective parameter.

The following parameter types are implemented in the function list:

- Integer
- UInteger
- Double
- Bool
- String
- Color
- HMI tag: Specify a configured HMI tag. Autocomplete is supported.
- Screen object: Specify a configured screen item in the current screen. Autocomplete is supported.
- Selection: Sets the current screen as value. If this type is selected, the value cannot be edited.
- Text list
- Screen window
- Runtime language

> **Note**
>
> HMI tags and screen items can be renamed without updating the function list. Objects of the WinCC Unified object model are referenced in the function list.

Optional parameters are marked with "(optional)".

Parameters of functions that you have configured in global modules are always optional.

#### Assigning parameters via drag-and-drop operation

For some objects you can assign the objects to parameters of the function list using drag-and-drop operation.

You assign the following objects from the detail view to function list parameters using the drag-and-drop feature:

- HMI tag
- PLC tag

  If you assign a PLC tag by drag-and-drop operation, a connected HMI tag is created automatically. The HMI tag is linked to the parameter.
- Screen

  In addition, you can assign screens from the project tree to parameters in the function list using the drag-and drop features.
- Text list

#### Troubleshooting

The project data is tested in the background during the configuration.

To inform you of errors, missing or incorrect entries in the function list are highlighted in red:

- At least one function is not completely supplied with parameters.
- At least one function is contained which is not supported by the selected HMI device, for example, by changing the device type.

> **Note**
>
> Missing screen items and HMI tags can be created later. Objects of the WinCC Unified object model are referenced in the function list.

Alarms during the compiling and loading of a project are displayed in the Inspector window in the "Info &gt; Compile" tab.

The function list supports you by displaying missing or incorrect entries directly for editing:

- To go directly to the function list, select the green arrow ![Troubleshooting](images/125111278731_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

["Scripts" editor (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified)
  
[System functions (RT Unified)](#system-functions-rt-unified)

### Configuring a function list (RT Unified)

#### Restrictions for events

- "Activated" and "Deactivated" events:

  If the focus is on the affected screen item, scripts are executed at the "activated" and "deactivated" events.
- "Press key" and "Release key" events:

  The events "Press key" and "Release key" can only be queried when a keyboard is connected.

#### Requirement

One of the following objects is configured:

- Screen
- Screen item
- Task

#### Procedure

1. Select the object.
2. Go to "Properties &gt; Events" in the Inspector window.

   The function list opens.
3. Select an event.
4. Select "&lt;Add function&gt;" in the function list.
5. Enter the function.

   If the desired function has parameters, the parameters are displayed.
6. Define the parameter values.
7. To add more functions, repeat steps 4.) to 6.).
8. Save the project.

#### Result

- The function list is configured.
- In addition, to the configured event, the status of the function list is displayed in the Inspector window.
- The function list is executed from top to bottom when the configured event occurs in runtime.

### Editing a function list (RT Unified)

#### Editing function lists

The function list is executed from top to bottom. You have the following options for editing function lists:

| Symbol | Meaning |
| --- | --- |
| ![Editing function lists](images/124747113355_DV_resource.Stream@PNG-de-DE.png) | "Move function up" |
| ![Editing function lists](images/124747122443_DV_resource.Stream@PNG-de-DE.png) | "Move function down" |
| ![Editing function lists](images/124755540619_DV_resource.Stream@PNG-de-DE.png) | "Convert function list to script" |
| ![Editing function lists](images/124755600395_DV_resource.Stream@PNG-de-DE.png) | "Delete function list" |

#### Requirement

- The function list is open.
- At least one function is configured at an event.

#### Changing the order of functions

You move a function within the function list as follows:

1. Select the name of the function or an associated parameter.
2. Select the "Move function up" or "Move function down" button.

   If the function is already at the first or last position in the list, pressing the button has no effect.

#### Replacing a function

1. To replace a function, enter the name of another function in the input field. All parameter settings of the replaced function are deleted.

#### Converting a function list to a local script

1. To convert the function list to a local script, use the "Convert function list to script" button.
2. The "Scripts" editor opens. Adapt the script to your requirements.

The function list can be converted to a local script even if the parameter specifications are incorrect or incomplete. The parameter specifications must be adjusted accordingly in the script.

> **Note**
>
> This action can only be revoked using the ![Converting a function list to a local script](images/124755609355_DV_resource.Stream@PNG-de-DE.png) "Undo" button.

#### Delete function list

1. To delete the entire function list of an event, select the "Delete function list" button.

#### Deleting functions

To delete a single function, follow these steps:

1. Select the name of the function.
2. Press &lt;Del&gt;.

---

**See also**

["Scripts" editor (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified)

### Using a screen item to specify the value of a parameter (RT Unified)

#### Introduction

For some parameters, you can assign "Screen item" as parameter type.

For example, enter the "Value" parameter of the "IncreaseTag" function via the I/O field in runtime.

> **Note**
>
> The assigned screen item must have the property "Process value".
>
> Possible screen items are, for example:
>
> - I/O field
> - Bar
> - Slider
> - Radio button

The value entered in the screen item must correspond to the data type expected by the system function.

If the data types do not match, convert the value using an additional tag.

#### Requirement

- A screen is configured.
- A suitable screen object (e.g. I/O field) is configured.
- A suitable system function (e.g. "IncreaseTag") is created in the function list.

#### Procedure

To assign a parameter to a screen item and convert the value entered in the screen item, proceed as follows:

1. Assign the desired screen item to the parameter.
2. Select the screen item.
3. Go to "Properties &gt; General &gt; Process value" in the Inspector window.
4. Select "Tag" in the "Dynamization" column.

   The tag selection range is displayed.
5. Select the selection button ![Procedure](images/126370774411_DV_resource.Stream@PNG-de-DE.png).
6. Select the "Add" button.
7. Assign a meaningful name.
8. Specify the required tag data type.

   The "Value" parameter, for example, requires a numeric data type.

### Adapt the function list to changed scripts (RT Unified)

You use functions that you have defined for global modules in the function list. These functions and associated parameters are referenced.

If you edit used functions after creating the function list, you must manually transfer some changes to the function list:

- Adding of a parameter
- Deleting of a parameter
- Deleting of a function

> **Note**
>
> If you rename functions or parameters, these changes are automatically transferred to the function list.

#### Requirement

- A function is defined in a global module.
- The function is used in a function list.

#### Procedure

1. Make at least one of the following changes to the function:

   - Add a parameter
   - Delete a parameter
   - Delete a function
2. Go to the relevant function in the function list.
3. Double-click to apply the change marked in red.

---

**See also**

["Scripts" editor (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#scripts-editor-rt-unified)

## System functions (RT Unified)

This section contains information on the following topics:

- [LogOff (RT Unified)](#logoff-rt-unified)
- [UpdateTag (RT Unified)](#updatetag-rt-unified)
- [ActivateCleanScreen (RT Unified)](#activatecleanscreen-rt-unified)
- [InsertElectronicRecord (RT Unified)](#insertelectronicrecord-rt-unified)
- [ExecuteReport (RT Unified)](#executereport-rt-unified)
- [EjectStorageMedium (RT Unified)](#ejectstoragemedium-rt-unified)
- [IncreaseTag (RT Unified)](#increasetag-rt-unified)
- [CreateParameterSet (RT Unified)](#createparameterset-rt-unified)
- [CreateScreenshot (RT Unified)](#createscreenshot-rt-unified)
- [CreateOperatorInputInformation (RT Unified)](#createoperatorinputinformation-rt-unified)
- [CreateSystemInformation (RT Unified)](#createsysteminformation-rt-unified)
- [CreateSystemAlarm (RT Unified)](#createsystemalarm-rt-unified)
- [ExportParameterSets (RT Unified)](#exportparametersets-rt-unified)
- [ExecuteToolbarButton (alarm control) (RT Unified)](#executetoolbarbutton-alarm-control-rt-unified)
- [ExecuteToolbarButton (parameter set control) (RT Unified)](#executetoolbarbutton-parameter-set-control-rt-unified)
- [ExecuteToolbarButton (system diagnostics control) (RT Unified)](#executetoolbarbutton-system-diagnostics-control-rt-unified)
- [GoToPLC (RT Unified)](#gotoplc-rt-unified)
- [ImportParameterSets (RT Unified)](#importparametersets-rt-unified)
- [InvertBitInTag (RT Unified)](#invertbitintag-rt-unified)
- [IsAlarmJumpPossible (RT Unified)](#isalarmjumppossible-rt-unified)
- [LoadParameterSet (RT Unified)](#loadparameterset-rt-unified)
- [LoadAndWriteParameterSet (RT Unified)](#loadandwriteparameterset-rt-unified)
- [GetDHCPState (RT Unified)](#getdhcpstate-rt-unified)
- [GetBrightness (RT Unified)](#getbrightness-rt-unified)
- [GetIPV4Address (RT Unified)](#getipv4address-rt-unified)
- [GetNetworkInterfaceState (RT Unified)](#getnetworkinterfacestate-rt-unified)
- [ReadParameterSet (RT Unified)](#readparameterset-rt-unified)
- [ReadParameterSetName (RT Unified)](#readparametersetname-rt-unified)
- [ReadParameterSetTypeName (RT Unified)](#readparametersettypename-rt-unified)
- [GetSmartServerState (RT Unified)](#getsmartserverstate-rt-unified)
- [ReadAndIncreaseTag (RT Unified)](#readandincreasetag-rt-unified)
- [ReadAndInvertBitInTag (RT Unified)](#readandinvertbitintag-rt-unified)
- [ReadAndResetBitInTag (RT Unified)](#readandresetbitintag-rt-unified)
- [ReadAndSetBitInTag (RT Unified)](#readandsetbitintag-rt-unified)
- [ReadAndSetTagValue (RT Unified)](#readandsettagvalue-rt-unified)
- [ReadAndSaveParameterSet (RT Unified)](#readandsaveparameterset-rt-unified)
- [ReadAndDecreaseTag (RT Unified)](#readanddecreasetag-rt-unified)
- [ClearAlarmLog (RT Unified)](#clearalarmlog-rt-unified)
- [DeleteParameterSet (RT Unified)](#deleteparameterset-rt-unified)
- [ClearTagLog (RT Unified)](#cleartaglog-rt-unified)
- [OpenScreenInPopup (RT Unified)](#openscreeninpopup-rt-unified)
- [OpenScreenInPopupAsync (RT Unified)](#openscreeninpopupasync-rt-unified)
- [OpenScreenWithNumberInPopup (RT Unified)](#openscreenwithnumberinpopup-rt-unified)
- [OpenViewGRAPHByBlock (RT Unified)](#openviewgraphbyblock-rt-unified)
- [OpenGRAPHViewFromOverview (RT Unified)](#opengraphviewfromoverview-rt-unified)
- [OpenPLCCodeViewByAlarm (RT Unified)](#openplccodeviewbyalarm-rt-unified)
- [ResetBitInTag (RT Unified)](#resetbitintag-rt-unified)
- [ShiftAndMask (RT Unified)](#shiftandmask-rt-unified)
- [ClosePopup (RT Unified)](#closepopup-rt-unified)
- [WriteParameterSet (RT Unified)](#writeparameterset-rt-unified)
- [WriteManualValue (RT Unified)](#writemanualvalue-rt-unified)
- [SetBitInTag (RT Unified)](#setbitintag-rt-unified)
- [SetDHCPState (RT Unified)](#setdhcpstate-rt-unified)
- [SetPropertyValue (RT Unified)](#setpropertyvalue-rt-unified)
- [SetBrightness (RT Unified)](#setbrightness-rt-unified)
- [SetIPV4Address (RT Unified)](#setipv4address-rt-unified)
- [SetNetworkInterfaceState (RT Unified)](#setnetworkinterfacestate-rt-unified)
- [SetPLCDateTime](#setplcdatetime)
- [SetLanguage (RT Unified)](#setlanguage-rt-unified)
- [SetSmartServerState (RT Unified)](#setsmartserverstate-rt-unified)
- [SetTagValue (RT Unified)](#settagvalue-rt-unified)
- [SetConnectionMode (RT Unified)](#setconnectionmode-rt-unified)
- [SaveParameterSet (RT Unified)](#saveparameterset-rt-unified)
- [StartProgram (RT Unified)](#startprogram-rt-unified)
- [StopRuntime (RT Unified)](#stopruntime-rt-unified)
- [StopTagLogging (RT Unified)](#stoptaglogging-rt-unified)
- [LookUpText (RT Unified)](#lookuptext-rt-unified)
- [RenameParameterSet (RT Unified)](#renameparameterset-rt-unified)
- [ToggleGRAPHViewerMode (RT Unified)](#togglegraphviewermode-rt-unified)
- [ToggleNetworkDisplay (RT Unified)](#togglenetworkdisplay-rt-unified)
- [ToggleLanguage (RT Unified)](#togglelanguage-rt-unified)
- [ZoomIn (RT Unified)](#zoomin-rt-unified)
- [ZoomOut (RT Unified)](#zoomout-rt-unified)
- [DecreaseTag (RT Unified)](#decreasetag-rt-unified)
- [ChangeScreen (RT Unified)](#changescreen-rt-unified)
- [ChangeScreenAsync (RT Unified)](#changescreenasync-rt-unified)
- [ChangeScreenAsyncWithNumber (RT Unified)](#changescreenasyncwithnumber-rt-unified)
- [ChangeScreenWithNumber (RT Unified)](#changescreenwithnumber-rt-unified)
- [ChangeConnection (RT Unified)](#changeconnection-rt-unified)
- [Next (RT Unified)](#next-rt-unified)
- [ShowLoginDialog (RT Unified)](#showlogindialog-rt-unified)
- [ShowControlPanel (RT Unified)](#showcontrolpanel-rt-unified)
- [ShowSoftwareVersion (RT Unified)](#showsoftwareversion-rt-unified)
- [Previous (RT Unified)](#previous-rt-unified)

### LogOff (RT Unified)

#### Description

Logs off the current user on the HMI device.

#### Use in the function list

Logoff()

The system function "Logoff" has no parameters.

#### Use in scripts

You can find more information on using the "LogOff" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.LogOff() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctlogoff-rt-unified)

### UpdateTag (RT Unified)

#### Description

Reads the current value of the tags with the specified update ID from the PLC. An update ID can be used for several tags.

> **Note**
>
> Tags of the STRUCT data type are not supported.

#### Use in the function list

UpdateTag (Update ID)

The system function "UpdateTag" has the following parameters:

| Parameter | Description |
| --- | --- |
| Update ID | Specifies the Update ID. |

#### Use in scripts

You can find more information on using the "UpdateTag" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.UpdateTag() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctupdatetag-rt-unified)

### ActivateCleanScreen (RT Unified)

#### Description

Opens a cleaning screen as a full-screen popup and deactivates the touch screen of Unified Panels.  
No screen object on the screen lying underneath can be used while the cleaning screen is open. When the time interval has elapsed, the popup closes.

#### Use in the function list

ActivateCleanScreen (Timeout)

The "ActivateCleanScreen" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Timeout | Time period in seconds after which the popup is closed. The maximum value is 300 seconds. |

#### Use in scripts

You can find more information on using the "ActivateCleanScreen" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ActivateCleanScreen() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctactivatecleanscreen-rt-unified)

### InsertElectronicRecord (RT Unified)

#### Description

This system function is used to log user actions in the Audit Trail that are not automatically logged in the Audit Trail. You can also use this system function to require the user to enter an acknowledgment or an electronic signature and a comment for the operator action. A requirement for the use of the system function is that the GMP-compliant configuration is activated under "Runtime settings &gt; GMP".

If you use the "InsertElectronicRecord" system function in a function, the debugger may open if you cancel your input by clicking "Cancel". To compensate for this reaction, you can use the "On Error Resume Next" statement in a function. With this instruction, the next instruction is executed after a runtime error. If you use the "On Error Resume Next" statement, output of system alarms is also suppressed.

#### Use in the function list

InsertElectronicRecord (name, category, operation type, old value, new value, confirmation type, reason, required function rights)

The "InsertElectronicRecord" system function has the following parameters:

> **Note**
>
> The parameter "Required function rights" and the values "Signature required" and "Signature and comment required" of the parameter "Confirmation type" are only supported by HMI devices with an installed Runtime version ≥ V18.0.0.1.

| Parameter | Description |
| --- | --- |
| Name | Name of the modified object |
| Category | Category or class name of the modified object |
| Operation type | Specifies the type of change.  Create = New value.  Update = Changed value.  Delete = Deleted value. |
| Old value | Value before the change |
| New value | Value after the change |
| Confirmation type | Specifies how the action must be confirmed  None = No confirmation required, an entry is created in the Audit Trail.  Confirmation required = Acknowledgment, the user must acknowledge the action; an entry is created in the Audit Trail.  Reason required = Acknowledgment, the user must acknowledge the action and enter a reason; an entry is created in the Audit Trail.  Signature required = electronic signature. A dialog window opens for the user to enter their electronic signature. An entry is created in the Audit Trail.  Signature and comment required = electronic signature. A dialog window opens for the user to enter their electronic signature and a comment. An entry is created in the Audit Trail. |
| Reason (optional) | Text list for selecting a reason for the change. |
| Required function rights (optional) | Specifies the function right required for the electronic signature.  Single electronic signature = A valid electronic signature with first or second signature right is required.  First electronic signature only = A valid electronic signature with first signature right is required.  Second electronic signature only = A valid electronic signature with second signature right is required.  Multiple audit rights = A double electronic signature with first and second signature rights is required. |

#### Use in scripts

You can find more information on using the "InsertElectronicRecord" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.InsertElectronicRecord() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctinsertelectronicrecord-rt-unified)

### ExecuteReport (RT Unified)

#### Description

Executes a report automatically and independently of the general report cycle. The execution can be triggered through a specific event, for example, change of a tag value, occurrence of a specific message or exceeding a tag limiting value.

#### Use in the function list

ExecuteReport (name report order)

The system function "ExecuteReport" has the following parameters:

| Parameter | Description |
| --- | --- |
| Report task name | Specifies the name of the report to be executed. |

#### Use in scripts

You can find more information on using the "ExecuteReport" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ExecuteReport() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexecutereport-rt-unified)

### EjectStorageMedium (RT Unified)

#### Description

Ejects an inserted storage medium. The function checks whether the storage medium is currently being accessed. If no current read or write process is taking place, the storage medium can be removed without data loss.

> **Note**
>
> The "EjectStorageMedium" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.
>
> The system function only works correctly in runtime if you use the storage medium in question for logging.
>
> The system function cannot be used to eject the storage medium of the reporting database.

#### Use in the function list

EjectStorageMedium (storage device)

The system function "EjectStorageMedium" has the following parameters:

| Parameter | Description |
| --- | --- |
| Storage device | System variable name of the storage medium with path specification (e.g. "/USB storage card"). |

#### Use in scripts

You can find more information on using the "EjectStorageMedium" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.EjectStorageMedium() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctejectstoragemedium-rt-unified)

### IncreaseTag (RT Unified)

#### Description

Adds the specified value to the tag value: X = X + a

If you configure the system function for events of an alarm without the tag being used in the current screen, it is not ensured that the actual tag value is being used in the PLC.

For the system function to be executed, the value of the tags must be current and valid, which means the quality code must correspond to Good (cascade).

The following conditions must be met for external tags:

- the connection to the PLC is set up and
- the acquisition mode of the tags is "Cyclic in operation" and
- the tag is used at the "Process value" property of an object.

> **Note**
>
> The system function is executed with the last known process value. Since this process value cannot be kept up to date in all cases, it is prohibited to write it from multiple sources (e.g. from the HMI device via scripts and from the PLC). This ensures that the value that is changed actually corresponds to the process value.

#### Use in the function list

IncreaseTag (Tag, Value)

The system function "IncreaseTag" has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag to which the specified value is added.  The following data types are not supported: Byte, Word, DWord, LWord. |
| Value | Value to be added. |

> **Note**
>
> **Converting a value**
>
> The system function uses the same tag as input and output values. If you are using this system function to convert a value, follow these steps:
>
> 1. Create an auxiliary tag.
> 2. Assign the tag value to the auxiliary tag with the "SetTagValue" system function.

#### Use in scripts

You can find more information on using the "IncreaseTag" system function in JavaScript functions in the WinCC Unified object model.

### CreateParameterSet (RT Unified)

#### Description

Creates a new parameter set. with the default values defined in the Engineering System.

To be able to use the system function, an edit tag must have been created at the associated parameter set type.

#### Use in the function list

CreateParameterSet (parameter set type, Language, ParameterSetTypeName, Processing status)

The system function "CreateParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set ID (optional) | ID of the parameter set that is created. If an ID is not entered, a unique ID is assigned automatically. |
| Parameter set name (optional) | Name of the parameter set that is created. If a name is not entered, a unique name is assigned automatically. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. If the output status is set to "True", alarms are generated and displayed (if configured). |
| Processing status (optional) | Indicates the execution status of a function:  2 = Function is being executed.  4 = Function successfully executed.  12 - Function was canceled. |

#### Using scripts

You can find more information on the "CreateParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.CreateParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcreateparameterset-rt-unified)

### CreateScreenshot (RT Unified)

#### Description

Creates and saves a screenshot. If images already exist in the specified file path, they will be overwritten. If the specified file path cannot be accessed, an error message is displayed.

> **Note**
>
> The system function "CreateScreenshot" is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

CreateScreenshot (path of storage medium)

The system function "CreateScreenshot" has the following parameters:

| Parameter | Description |
| --- | --- |
| Storage media path | Path name of the screenshot, including file name with file format.  Supported file formats: ".jpg", ".jpeg" and ".png"  Example: /media/simatic/X61/Screenshots/image.jpg |

#### Use in scripts

You can find more information on using the "CreateScreenshot" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.CreateScreenshot() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcreatescreenshot-rt-unified)

### CreateOperatorInputInformation (RT Unified)

#### Description

Creates an alarm of the class "OperatorInputInformation".

#### Use in the function list

CreateOperatorInputInformation (alarm text, range, parameter value 1, parameter value 2, parameter value 3, parameter value 4, parameter value 5, parameter value 6, parameter value 7)

The system function "CreateSystemInformation" has the following parameters:

| Parameter | Description |
| --- | --- |
| Alarm text | Specifies the alarm text.  The alarm text can only be defined in one language in the system function. |
| Area (optional) | Specifies the scope of the alarm. |
| Parameter value 1 (optional) | Value of the first alarm parameter |
| Parameter value 2 (optional) | Value of the second alarm parameter |
| Parameter value 3 (optional) | Value of the third alarm parameter |
| Parameter value 4 (optional) | Value of the fourth alarm parameter |
| Parameter value 5 (optional) | Value of the fifth alarm parameter |
| Parameter value 6 (optional) | Value of the sixth alarm parameter |
| Parameter value 7 (optional) | Value of the seventh alarm parameter |

#### Use in scripts

You can find more information on using the "CreateOperatorInputInformation" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.CreateOperatorInputInformation() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcreateoperatorinputinformation-rt-unified)
  
[Creating alarms with multilingual alarm texts (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#creating-alarms-with-multilingual-alarm-texts-rt-unified)

### CreateSystemInformation (RT Unified)

#### Description

Creates an alarm of the class "SystemInformation".

The alarm class "SystemInformation" only has the status "Incoming" and is therefore only displayed under "Logged alarms" in the alarm control and not under "Pending alarms".

#### Use in the function list

CreateSystemInformation (alarm text, range, parameter value 1, parameter value 2, parameter value 3, parameter value 4, parameter value 5, parameter value 6, parameter value 7)

The system function "CreateSystemInformation" has the following parameters:

| Parameter | Description |
| --- | --- |
| Alarm text | Specifies the alarm text.  The alarm text can only be defined in one language in the system function. |
| Area (optional) | Specifies the scope of the alarm. |
| Parameter value 1 (optional) | Value of the first alarm parameter |
| Parameter value 2 (optional) | Value of the second alarm parameter |
| Parameter value 3 (optional) | Value of the third alarm parameter |
| Parameter value 4 (optional) | Value of the fourth alarm parameter |
| Parameter value 5 (optional) | Value of the fifth alarm parameter |
| Parameter value 6 (optional) | Value of the sixth alarm parameter |
| Parameter value 7 (optional) | Value of the seventh alarm parameter |

#### Use in scripts

You can find more information on using the "CreateSystemInformation" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.CreateSystemInformation() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcreatesysteminformation-rt-unified)
  
[Creating alarms with multilingual alarm texts (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#creating-alarms-with-multilingual-alarm-texts-rt-unified)

### CreateSystemAlarm (RT Unified)

#### Description

Creates an alarm of the class "SystemAlarm".

#### Use in the function list

CreateSystemAlarm (alarm text, range, parameter value 1, parameter value 2, parameter value 3, parameter value 4, parameter value 5, parameter value 6, parameter value 7)

The system function "CreateSystemInformation" has the following parameters:

| Parameter | Description |
| --- | --- |
| Alarm text | Specifies the alarm text.  The alarm text can only be defined in one language in the system function. |
| Area (optional) | Specifies the scope of the alarm. |
| Parameter value 1 (optional) | Value of the first alarm parameter |
| Parameter value 2 (optional) | Value of the second alarm parameter |
| Parameter value 3 (optional) | Value of the third alarm parameter |
| Parameter value 4 (optional) | Value of the fourth alarm parameter |
| Parameter value 5 (optional) | Value of the fifth alarm parameter |
| Parameter value 6 (optional) | Value of the sixth alarm parameter |
| Parameter value 7 (optional) | Value of the seventh alarm parameter |

#### Use in scripts

You can find more information on using the "CreateSystemAlarm" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.CreateSystemAlarm() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcreatesystemalarm-rt-unified)
  
[Creating alarms with multilingual alarm texts (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#creating-alarms-with-multilingual-alarm-texts-rt-unified)

### ExportParameterSets (RT Unified)

#### Description

Exports parameter sets from the parameter set memory to a file.

#### Use in the function list

ExportParameterSets (parameter set type ID, parameter set ID, file name, overwrite, output status, processing status (optional), generate checksum)

The system function "ExportParameterSets" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type ID | Specifies the name or the ID of the parameter set type. If the name or ID of the type does not exist, execution is terminated. |
| Parameter set ID | Specifies the name or the ID of the parameter set. The following cases are differentiated:  - If the parameter set ID is set to 0, all parameter sets available in the memory are exported. - If the specified name or the ID does not exist in the imported file, the execution is canceled. - If the specified name or the ID does not exist in the imported file, this specific parameter set is imported.   In the following cases the import is aborted and an alarm appears:  - No parameter set available - Name or ID does not exist in the import file. |
| File name | Specifies the file path of the file to be imported.   In the following cases the execution is canceled and an alarm is generated:  - Invalid file path - Error during file access |
| Overwrite | Specifies whether the existing file is overwritten:   0 = Overwriting is not allowed.   1 = Overwriting is allowed.  An alarm is generated and displayed if an error occurs during file access. This can occur, for example, when the existing file cannot be overwritten even though overwriting is allowed. |
| Output status | Specifies the output status:   True = Alarms are output.  False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function:  2 = Function is being executed.  4 = Function successfully executed.  12 = Function was canceled. |
| Generate checksum | Specifies whether a checksum is generated for the parameter set to be exported:   True = Checksum is generated.   False = Checksum is not generated. |

#### Use in scripts

You can find more information on using the "ExportParameterSets" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ExportParameterSets() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexportparametersets-rt-unified)

### ExecuteToolbarButton (alarm control) (RT Unified)

#### Description

Controls the toolbar buttons of an alarm control.

If the authorization to operate the control or toolbar has been limited or blocked, the buttons can still be operated using the system function.

The authorization must be configured at the object that the system function executes.

Buttons that are not available due to missing functionality in the current display (e.g. Acknowledge button without acknowledgeable alarms) cannot be executed using the system function.

#### Use in the function list

ExecuteToolbarButton (screen object path, alarm control toolbar button)

The "ExecuteToolbarButton" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen object path | Path of the screen object |
| Alarm control toolbar button | Name of the button:  - Single acknowledgment - Group acknowledgment |

#### Use in scripts

You can find more information on using the "ExecuteToolbarButton" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ExecuteToolbarButton() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexecutetoolbarbutton-rt-unified)

### ExecuteToolbarButton (parameter set control) (RT Unified)

#### Description

Controls the toolbar buttons of a parameter set control.

If the authorization to operate the control or toolbar has been limited or blocked, the buttons can still be operated using the system function.

The authorization must be configured at the object that the system function executes.

Buttons that are not available due to missing functionality in the current display (e.g. "Create", if no parameter set type has been configured) cannot be executed using the system function.

#### Use in the function list

ExecuteToolbarButton (screen object path, parameter set control toolbar button)

The "ExecuteToolbarButton" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen object path | Path of the screen object |
| Parameter set control toolbar button | Name of the button:  - Save - Create - Save as - Delete - Rename - Write to PLC - Read from PLC - Export - Import - Cancel |

#### Use in scripts

You can find more information on using the "ExecuteToolbarButton" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ExecuteToolbarButton() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexecutetoolbarbutton-rt-unified-1)

### ExecuteToolbarButton (system diagnostics control) (RT Unified)

#### Description

Controls the toolbar buttons of a system diagnostics control.

If the authorization to operate the control or toolbar has been limited or blocked, the buttons can still be operated using the system function.

The authorization must be configured at the object that the system function executes.

Buttons that are not available due to missing functionality in the current display (e.g. "Next line" if the last line has been selected) cannot be executed using the system function.

#### Use in the function list

ExecuteToolbarButton (screen object path, system diagnostics control toolbar button)

The "ExecuteToolbarButton" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen object path | Path of the screen object |
| System diagnostics control toolbar button | Name of the button:   - Previous - Next - Reload - Home - First line - Previous line - Next line - Last line - Split view - Back - Show diagnostics buffer |

#### Use in scripts

You can find more information on using the "ExecuteToolbarButton" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ExecuteToolbarButton() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctexecutetoolbarbutton-rt-unified-3)

### GoToPLC (RT Unified)

#### Description

Switches from a diagnostics indicator to the system diagnostics control.

#### Use in the function list

GoToPLC (Screen object path)

The system function "GoToPLC" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen object path | Path to the screen object System Diagnostics Control, for example, "./Screen window_1/Diagnostic control_1" |

#### Using scripts

You can find more information on the "GoToPlc" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GoToPlc() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgotoplc-rt-unified)

### ImportParameterSets (RT Unified)

#### Description

Imports parameter sets from a file into the parameter set memory.

#### Use in the function list

ImportParameterSets (file name, parameter set ID, overwrite, output status, processing status (optional), check checksum)

The system function "ImportParameterSets" has the following parameters:

| Parameter | Description |
| --- | --- |
| File name | Specifies the file path of the file to be imported.   In the following cases the execution is canceled and an alarm is generated:  - Invalid file path - Error during file access |
| Parameter set ID | Specifies the name or the ID of the parameter set. The following cases are differentiated:  - If the parameter set ID is set to 0, all parameter sets are imported from the file. - If the name or the ID does not exist in the imported file, the execution is canceled. - If the specified name or the ID does not exist in the imported file, only this specific parameter set is imported.   In the following cases the import is aborted and an alarm appears:  - Invalid file head - No parameter set available - Parameter set name or parameter set ID does not exist in the file. |
| Overwrite | Specifies whether the values in the memory are overwritten with the values from the import file:   0 = Overwriting is not allowed.   1 = Overwriting is allowed.  If the name / ID of the specified parameter set exists, the values in the memory are overwritten with the parameter set values from the import file if overwriting is allowed. If it may not be overwritten, the data in the memory is not renewed. |
| Output status | Specifies the output status:   True = Alarms are output.  False = Alarms are not output.  If the output status is set to "True", alarms are generated and displayed (if configured). |
| Processing status (optional) | Indicates the execution status of a function:  2 = Function is being executed.  4 = Function successfully executed.  12 = Function was canceled. |
| Check checksum | Specifies whether the checksum of the import file is verified:   True = Checksum is verified.   False = Checksum is not verified. |

#### Use in scripts

You can find more information on using the "ImportParameterSets" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[Exporting and importing parameter sets (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#exporting-and-importing-parameter-sets-rt-unified)
  
[SysFct.ImportParameterSets() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctimportparametersets-rt-unified)

### InvertBitInTag (RT Unified)

#### Description

Inverts the bit with the specified number in the tag:

- If the bit in the tag has the value 1 (True), it will be set to 0 (False).
- If the bit in the tag has the value 0 (False), it will be set to 1 (True).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime.

While the function is running, the operator and controller have only read access to the specified tag until it is transferred to the controller again.

For the system function to be executed, the value of the tags must be current and valid, which means the quality code must correspond to Good (cascade).

The following conditions must be met for external tags:

- the connection to the PLC is set up and
- the acquisition mode of the tags is "Cyclic in operation" and
- the tag is used at the "Process value" property of an object.

> **Note**
>
> The system function is executed with the last known process value. Since this process value cannot be kept up to date in all cases, it is prohibited to write it from multiple sources (e.g. from the HMI device via scripts and from the PLC). This ensures that the value that is changed actually corresponds to the process value.

#### Use in the function list

InvertBitInTag (Tag, Value)

The system function "InvertBitInTag" has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which the specified bit is inverted. |
| Bit number | The number of the bit that is inverted.  When this system function is used in a user function, the bits in the given tag will be counted from right to left independent of the controller that is used. Numbering starts with 0. |

#### Use in scripts

You can find more information on using the "InvertBitInTag" system function in JavaScript functions in the WinCC Unified object model.

### IsAlarmJumpPossible (RT Unified)

#### Description

The function checks whether the alarm selected in the alarm control is a process diagnostics alarm. If so, the specified screen object is enabled; otherwise, it is disabled.

#### Use in the function list

IsAlarmJumpPossible (Alarm control, Screen object path)

The "IsAlarmJumpPossible" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Alarm control | Path of the alarm control with selected alarm |
| Screen object path | Path of the screen object |

#### Use in scripts

You can find more information on using the "IsJumpableAlarm" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.IsJumpableAlarm() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctisjumpablealarm-rt-unified)

### LoadParameterSet (RT Unified)

#### Description

Loads parameter sets from the parameter set memory into the edit tag.

To be able to use the system function, an edit tag must have been created at the associated parameter set type.

#### Use in the function list

LoadParameterSet (Parameter set type, Parameter set, Output status, Processing status (optional))

The system function "LoadParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set | Specifies the name or the ID of the parameter set. If the name or ID of the parameter set does not exist, execution is terminated. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 - Function was canceled. |

#### Using scripts

You can find more information on the "LoadParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.LoadParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctloadparameterset-rt-unified)

### LoadAndWriteParameterSet (RT Unified)

#### Description

Loads parameter sets from the parameter set memory and writes them to the PLC.

#### Use in the function list

LoadAndWriteParameterSet (parameter set type ID, parameter set ID, output status, processing status (optional))

The system function "LoadAndWriteParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type ID | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set ID | Specifies the name or the ID of the parameter set. If the name or ID of the parameter set does not exist, execution is terminated. |
| Output status | Specifies the output status:   True = Alarms are output.  False = Alarms are not output.  If the output status is set to "True", alarms are generated and displayed (if configured). |
| Processing status (optional) | Indicates the execution status of a function:  2 = Function is being executed.  4 = Function successfully executed.  12 - Function was canceled. |

#### Use in scripts

You can find more information on using the "LoadAndWriteParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[Transferring parameter sets via scripts (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#transferring-parameter-sets-via-scripts-rt-unified)
  
[Transferring parameter sets (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#transferring-parameter-sets-rt-unified)
  
[SysFct.LoadAndWriteParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctloadandwriteparameterset-rt-unified)

### GetDHCPState (RT Unified)

#### Description

Reads out the DHCP setting of the network adapter.

> **Note**
>
> The "GetDHCPState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

GetDHCPState (Adapter name, Status, IPV6 (optional))

The system function "GetDHCPState" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter.   The following entries are possible:  - X1 = Static network adapter name 1 - X2 = Static network adapter name 2 - Manual input |
| Status | Tag to which the status is written:  0 = DHCP is disabled.  1 = DHCP is enabled. |
| IP V6 (optional) | Tag to which the IPv6 address is written. |

#### Use in scripts

You can find more information on using the "GetDHCPState" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetDHCPState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetdhcpstate-rt-unified)

### GetBrightness (RT Unified)

#### Description

Reads out the brightness value.

> **Note**
>
> The "GetBrightness" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

GetBrightness (Value)

The system function "GetBrightness" has the following parameters:

| Parameter | Description |
| --- | --- |
| Value | The tag to which the brightness value is written. |

#### Use in scripts

You can find more information on using the "GetBrightness" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetBrightness() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetbrightness-rt-unified)

### GetIPV4Address (RT Unified)

#### Description

Reads out the IPv4 settings of the network adapter.

> **Note**
>
> The "GetIPV4Address" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

GetIPV4Address (Adapter name, IP address, Subnet mask, Default gateway (optional), DNS server 1 (optional), DNS server 2 (optional))

The system function "GetIPV4Address" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter.   The following entries are possible:  - X1 = Static network adapter name 1 - X2 = Static network adapter name 2 - Manual input |
| IP address | Tag to which the IP address is written. |
| Subnet mask | Tag to which the subnet mask of the IPv4 address is written. |
| Default gateway (optional) | Tag to which the IP address of the default gateway is written. |
| DNS server 1 (optional) | Tag to which the IP address of DNS server 1 is written. |
| DNS server 2 (optional) | Tag to which the IP address of DNS server 2 is written. |

#### Use in scripts

You can find more information on using the "GetIPV4Address" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetIPV4Address() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetipv4address-rt-unified)

### GetNetworkInterfaceState (RT Unified)

#### Description

Reads out the status of the network adapter.

> **Note**
>
> The "GetNetworkInterfaceState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

GetNetworkInterfaceStatus (Adapter name, Status)

The system function "GetNetworkInterfaceState" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter. The following entries are possible:  - X1 addresses PROFINET (X1) Port 0 - X 1.0 addresses PROFINET (X1) Port 0 - X 1.1 addresses PROFINET (X1) Port 1 - X2 = addresses Ethernet (X2) - Manual input |
| Status | Tag to which the state of the network adapter is written:  0 = Network adapter is disabled.  1 = Network adapter is enabled. |

#### Use in scripts

You can find more information on using the "GetNetworkInterfaceState" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetNetworkInterfaceState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetnetworkinterfacestate-rt-unified)

### ReadParameterSet (RT Unified)

#### Description

Transfers the values of the recipe data record loaded in the PLC to the associated edit tags.

To be able to use the system function, an edit tag must have been created at the associated parameter set type.

#### Use in the function list

ReadParameterSet (Parameter set type, Output status, Processing status (optional))

The system function "ReadParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Using scripts

You can find more information on the "ReadParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ReadParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctreadparameterset-rt-unified)

### ReadParameterSetName  (RT Unified)

#### Description

Reads the name of the specified parameter set.

#### Use in the function list

ReadParameterSetName (Parameter set type ID, Parameter set ID, Language, ParameterSetName, Processing status)

The system function "ReadParameterSetName" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type ID | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set ID | Specifies the name or the ID of the parameter set. |
| Language | Specifies the language of the ID that is to be read. |
| Parameter set name | The tag to which the name of the parameter set is written. |
| Processing status | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Use in scripts

You can find more information on using the "GetParameterSetName" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetParameterSetName() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetparametersetname-rt-unified)

### ReadParameterSetTypeName (RT Unified)

#### Description

Reads the name of the specified parameter set type.

#### Use in the function list

ReadParameterSetTypeName (Parameter set type ID, Language, ParameterSetTypeName, Processing status)

The system function "ReadParameterSetTypeName" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type ID | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Language | Specifies the language of the ID that is to be read. |
| Parameter set type name | The tag to which the name of the parameter set type is written. |
| Processing status | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Using scripts

You can find more information on the "GetParameterSetTypeName" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetParameterSetTypeName() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetparametersettypename-rt-unified)

### GetSmartServerState (RT Unified)

#### Description

Returns the activation state of the Smart server.

> **Note**
>
> The "GetSmartServerState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

GetSmartServerState (Status)

The system function "GetSmartServerState" has the following parameters:

| Parameter | Description |
| --- | --- |
| Status | Tag to which the activation status of the Smart Server is written:   True = Smart Server is enabled.   False = Smart Server is disabled. |

#### Use in scripts

You can find more information on using the "GetSmartServerState" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.GetSmartServerState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctgetsmartserverstate-rt-unified)

### ReadAndIncreaseTag (RT Unified)

#### Description

Adds the specified value to the current tag value during inching: X = X + a

The function reads the current value of the tag, performs the arithmetic operation with the current value and returns the output value to the tag.

The following conditions must be met for external tags:

- There is a connection to the PLC.
- The tag is used at the "Process value" property of an object.

#### Use in the function list

ReadAndIncreaseTag (Tag, Value)

The "ReadAndIncreaseTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag to which the specified value is added.  The following data types are not supported: Byte, Word, DWord, LWord. |
| Value | The value that is added. |

#### Use in scripts

You can find more information on using the "ReadAndIncreaseTag" system function in JavaScript functions in the WinCC Unified object model.

### ReadAndInvertBitInTag (RT Unified)

#### Description

Inverts the bit with the specified number in the tag during inching:

- If the bit in the tag has the value 1 (True), it is set to 0 (False).
- If the bit in the tag has the value 0 (False), it is set to 1 (True).

The function reads the current value of the bit, sets the inverted value and returns the output value to the bit of the tag.

The following conditions must be met for external tags:

- There is a connection to the PLC.
- The tag is used at the "Process value" property of an object.

#### Use in the function list

ReadAndInvertBitInTag (Tag, Value)

The "ReadAndInvertBitInTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which the specified bit is inverted. |
| Bit number | The number of the bit that is inverted.  When you use this system function in a user function, the bits in the specified tag are numbered from right to left regardless of which PLC is used. The numbering starts with 0. |

#### Use in scripts

You can find more information on using the "ReadAndInvertBitInTag" system function in JavaScript functions in the WinCC Unified object model.

### ReadAndResetBitInTag (RT Unified)

#### Description

Sets the bit with the specified number in the tag to 0 (False) during inching:

The function reads the current value of the bit, sets the value to 0 and returns the output value to the bit of the tag.

The following conditions must be met for external tags:

- There is a connection to the PLC.
- The tag is used at the "Process value" property of an object.

#### Use in the function list

ReadAndResetBitInTag (Tag, Value)

The "ReadAndResetBitInTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which a bit is set to 0 (False). |
| Bit number | The number of the bit that is set to 0 (False).  When you use this system function in a user function, the bits in the specified tag are numbered from right to left regardless of which PLC is used. The numbering starts with 0. |

#### Use in scripts

You can find more information on using the "ReadAndResetBitInTag" system function in JavaScript functions in the WinCC Unified object model.

### ReadAndSetBitInTag (RT Unified)

#### Description

Sets the bit with the specified number in the tag to 1 (True) during inching:

The function reads the current value of the bit, sets the value to 1 and returns the output value to the bit of the tag.

The following conditions must be met for external tags:

- There is a connection to the PLC.
- The tag is used at the "Process value" property of an object.

#### Data types not supported

The following data types are not supported by the function:

- UINT

#### Use in the function list

ReadAndSetBitInTag (Tag, Value)

The "ReadAndSetBitInTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which a bit is set to 1 (True). |
| Bit number | The number of the bit that is set to 1 (True).  When you use this system function in a user function, the bits in the specified tag are numbered from right to left regardless of which PLC is used. The numbering starts with 0. |

#### Use in scripts

You can find more information on using the "ReadAndSetBitInTag" system function in JavaScript functions in the WinCC Unified object model.

### ReadAndSetTagValue (RT Unified)

#### Description

Assigns a new value to the specified tag during inching:

Depending on the tag type, you assign strings and numbers with this system function.

> **Note**
>
> The "SetTagValue" system function is only executed after a connection has been established.

#### Use in the function list

ReadAndSetTagValue (Tag, Value)

The "ReadAndSetTagValue" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag to which the specified value is assigned. |
| Value | The value that is assigned to the specified tag. |

#### Use in scripts

You can find more information on using the "ReadAndSetTagValue" system function in JavaScript functions in the WinCC Unified object model.

### ReadAndSaveParameterSet (RT Unified)

#### Description

Reads a parameter set from the PLC and writes the parameter set to the parameter set memory.

#### Use in the function list

ReadAndWriteParameterSet (parameter set type ID, parameter set ID, overwrite, output status, processing status (optional))

The system function "ReadAndWriteParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type ID | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set ID | Specifies the name or the ID of the parameter set. If the name or ID of the parameter set does not exist, a new parameter set is created.  If the name or the ID of the specified parameter set exists, the values in the PLC are overwritten with the parameter set values in the memory if hmiOverwrite.Enabled is set. If hmiOverwrite.Disabled is set, the data in the memory is not replaced. |
| Overwrite | Specifies whether the values in the memory are overwritten with the values from the import file:  0 = Overwriting is not allowed.   1 = Overwriting is allowed.  The following cases are differentiated:  - If the name / ID of the specified parameter set exists, the values in the PLC are overwritten with the parameter set values in the memory if overwriting is allowed. - If overwriting is not allowed, the data in the memory is not replaced. The process tag is updated to the status of the system function, if configured accordingly. |
| Output status | Specifies the output status:   True = Alarms are output.  False = Alarms are not output.  If the output status is set to "True", alarms are generated and displayed (if configured). |
| Processing status (optional) | Indicates the execution status of a function:  2 = Function is being executed.  4 = Function successfully executed.  12 = Function cancelled. |

#### Use in scripts

You can find more information on using the "ReadAndSaveParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[Transferring parameter sets via scripts (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#transferring-parameter-sets-via-scripts-rt-unified)
  
[Transferring parameter sets (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#transferring-parameter-sets-rt-unified)
  
[SysFct.ReadAndSaveParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctreadandsaveparameterset-rt-unified)

### ReadAndDecreaseTag (RT Unified)

#### Description

Subtracts the specified value from the value of the tag during inching: X = X - a

The function reads the current value of the tag, performs the arithmetic operation with the current value and returns the output value to the tag.

The following conditions must be met for external tags:

- There is a connection to the PLC.
- The tag is used at the "Process value" property of an object.

#### Use in the function list

ReadAndDecreaseTag (Tag, Value)

The "ReadAndDecreaseTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag from which the specified value is subtracted.  The following data types are not supported: Byte, Word, DWord, LWord. |
| Value | That value that is subtracted. |

#### Use in scripts

You can find more information on using the "ReadAndDecreaseTag" system function in JavaScript functions in the WinCC Unified object model.

### ClearAlarmLog (RT Unified)

#### Description

Deletes all recordings from the specified alarm log.

> **Note**
>
> **No backup**
>
> Note that no automatic backup is performed before the execution of the function.

#### Use in the function list

ClearAlarmLog (Log name)

The system function "ClearAlarmLog" has the following parameters:

| Parameter | Description |
| --- | --- |
| Log name | Name of the alarm log from which the entries are deleted. |

#### Use in scripts

You can find more information on using the "ClearAlarmLog" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ClearAlarmLog() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctclearalarmlog-rt-unified)

### DeleteParameterSet (RT Unified)

#### Description

Deletes a parameter set.

#### Use in the function list

DeleteParameterSet (Parameter set type, Parameter set, Output status, Processing status (optional))

The system function "DeleteParameterSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the type of parameter set from which the parameter set will be deleted. |
| Parameter set | Specifies the name or the ID of the parameter set that is being deleted. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Use in scripts

You can find more information on using the "DeleteParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.DeleteParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctdeleteparameterset-rt-unified)

### ClearTagLog (RT Unified)

#### Description

Deletes all data records in the specified data log.

> **Note**
>
> **No backup!**
>
> Note that no automatic backup is performed before execution of the function!

#### Use in the function list

ClearTagLog (Log name)

The system function "ClearTagLog" has the following parameters:

| Parameter | Description |
| --- | --- |
| Log name | Name of the data log from which all entries are deleted. |

#### Use in scripts

You can find more information on using the "ClearTagLog" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ClearTagLog() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctcleartaglog-rt-unified)

### OpenScreenInPopup (RT Unified)

#### Description

Opens a screen in a popup window.

#### Use in the function list

OpenScreenInPopup (Popup window name, Screen name, Close when open, Header, Left, Top, Hide close button, Parent screen path)

The system function "OpenScreenInPopup" has the following parameters:

| Parameter | Description |
| --- | --- |
| Popup window name | Name of the popup window. The name must be unique within the parent screen and is required to close the pop-up window. |
| Screen name | Name of the screen that is to be opened in the pop-up window. |
| Close when opened | True = If the pop-up window is open when the function is called, it is closed.  False = If the popup window is open when the function is called, it remains open. |
| Header | Specifies the window title of the popup window. |
| Left | Defines the window position as offset from the left margin. |
| Top | Defines the window position as offset from the top margin. |
| Hide close button | True = The "Close" button is not displayed.  False = The "Close" button is displayed. |
| Parent screen path (optional) | Path of the parent screen. With this parameter, you specify whether the pop-up window is closed in case of a screen change or in case of a screen change in a screen window.   If this value is not defined, the pop-up window is global. The pop-up window remains open until it is closed manually, by means of a function call or by exiting runtime. |

#### Use in scripts

You can find more information on using the "OpenScreenInPopup" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenScreenInPopup() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenscreeninpopup-rt-unified)
  
[Opening and closing a screen in a pop-up window (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#opening-and-closing-a-screen-in-a-pop-up-window-rt-unified)

### OpenScreenInPopupAsync (RT Unified)

#### Description

Opens a screen asynchronously in a popup window. The popup window opens once it has fully loaded.

#### Use in the function list

OpenScreenInPopupAsync (Popup window name, Screen name, Close if opened, Header, Left, Top, Hide close button, Parent screen path)

The "OpenScreenInPopupAsync" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Popup window name | Name of the popup window. The name must be unique within the parent screen and is required to close the popup window. |
| Screen name | Name of the screen that is loaded into the popup window. |
| Close if opened | True = If the window is open, it is closed.  False = If the window is open, it remains open. |
| Header | Defines the window title of the popup window. |
| Left | Defines the window position as offset from the left margin. |
| Top | Defines the window position as offset from the top margin. |
| Hide close button | True = The "Close" button is not displayed.  False = The "Close" button is displayed. |
| Parent screen path (optional) | Path of the parent screen. With this parameter, you specify whether the popup window closes following the screen change or following the screen change within a screen window.   If this value is not defined, the popup window is global. The popup window remains open until it is closed manually due to a function call or by exiting runtime. |

#### Using scripts

You can find more information on the "OpenScreenInPopupAsync" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenScreenInPopupAsync() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenscreeninpopupasync-rt-unified)
  
[Opening and closing a screen in a pop-up window (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#opening-and-closing-a-screen-in-a-pop-up-window-rt-unified)

### OpenScreenWithNumberInPopup (RT Unified)

#### Description

Opens a screen in a popup window.

#### Use in the function list

OpenScreenWithNumberInPopup (Popup window name, Screen number, Close when open, Header, Left, Top, Hide close button, Parent screen path)

The system function "OpenScreenWithNumberInPopup" has the following parameters:

| Parameter | Description |
| --- | --- |
| Popup window name | Name of the popup window. The name must be unique within the parent screen and is required to close the pop-up window. |
| Screen number | Unique number (&gt; 0) of the screen that will be loaded into the popup window. |
| Close when opened | True = If the pop-up window is open when the function is called, it is closed.  False = If the popup window is open when the function is called, it remains open. |
| Header | Specifies the window title of the popup window. |
| Left | Defines the window position as offset from the left margin. |
| Top | Defines the window position as offset from the top margin. |
| Hide close button | True = The "Close" button is not displayed.  False = The "Close" button is displayed. |
| Parent screen path (optional) | Path of the parent screen. With this parameter, you specify whether the pop-up window is closed in case of a screen change or in case of a screen change in a screen window.   If this value is not defined, the pop-up window is global. The pop-up window remains open until it is closed manually, by means of a function call or by exiting runtime. |

#### Use in scripts

You can find more information on using the "OpenScreenByNumberInPopup" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenScreenByNumberInPopup() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenscreenbynumberinpopup-rt-unified)

### OpenViewGRAPHByBlock (RT Unified)

#### Description

Switches from any screen object to the PLC code view.

#### Use in the function list

OpenViewGRAPHByBlock (PLC name, GRAPH instance name, step number, screen object path)

The "OpenGRAPHViewerGraphByBlock" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| PLC name | Indicates the name of the PLC. |
| GRAPH instance name | Instance name of the GRAPH block to be displayed. |
| Step number | Number of the step to be displayed. |
| Screen object path | Path of the screen object PLC code view, e.g. "./Screen window_1/ PlcCodeViewer control_1". |

#### Using scripts

You can find more information on the "OpenViewerGraphByBlock" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenViewerGraphByBlock() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenviewergraphbyblock-rt-unified)

### OpenGRAPHViewFromOverview (RT Unified)

#### Description

Opens the PLC code view from the GRAPH overview.

Gets the required parameters from the screen object "GRAPH overview" and passes them to the PLC code view using the "OpenGRAPHDetails" method.

#### Use in the function list

OpenGRAPHViewFromOverview (Object path to GRAPH overview, Object path to PLC code view)

The system function "OpenGRAPHViewFromOverview" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to GRAPH overview | Path to the screen object GRAPH overview, from which switching is to take place. |
| Object path to PLC code display | Path to the screen object PLC code view. |

#### Using scripts

You can find more information on the "OpenViewerGraphFromOverview" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenViewerGraphFromOverview() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenviewergraphfromoverview-rt-unified)

### OpenPLCCodeViewByAlarm (RT Unified)

#### Description

Opens the corresponding block in the PLC code view according to the selected alarm in the alarm control.

#### Use in the function list

OpenPLCCodeViewByAlarm (Alarm control, PLC code view)

The "OpenPLCCodeViewByAlarm" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Alarm control | Path of the alarm control |
| PLC code view | Path to the PLC code view |

#### Use in scripts

You can find more information on the "OpenPlcCodeViewFromAlarm" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.OpenPlcCodeViewFromAlarm() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctopenplccodeviewfromalarm-rt-unified)

### ResetBitInTag (RT Unified)

#### Description

Sets the bit with the specified number to 0 in the tag (False).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

For the system function to be executed, the value of the tags must be current and valid, which means the quality code must correspond to Good (cascade).

The following conditions must be met for external tags:

- the connection to the PLC is set up and
- the acquisition mode of the tags is "Cyclic in operation" and
- the tag is used at the "Process value" property of an object.

> **Note**
>
> The system function is executed with the last known process value. Since this process value cannot be kept up to date in all cases, it is prohibited to write it from multiple sources (e.g. from the HMI device via scripts and from the PLC). This ensures that the value that is changed actually corresponds to the process value.

#### Use in the function list

ResetBitInTag (Tag, Value)

The system function "ResetBitInTag" has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which a bit is set to 0 (False). |
| Bit number | The number of the bit that is set to 0 (False).  When this system function is used in a user function, the bits in the given tag will be counted from right to left independent of the controller that is used. Numbering starts with 0. |

#### Use in scripts

You can find more information on using the "ResetBitInTag" system function in JavaScript functions in the WinCC Unified object model.

### ShiftAndMask (RT Unified)

#### Description

The system function converts the input bit pattern of the source into an output bit pattern of the target. This involves bit shifting and masking. An integer number serves as bit mask, with whose bit pattern the shifted input bit pattern is multiplied. The shifted input bit pattern is multiplied by the bit mask, with bit-by-bit logical AND operation. The result has a decimal value and is stored in the target.

The following conditions must be met for external tags:

- the connection to the PLC is set up and
- the acquisition mode of the tags is "Cyclic in operation" and
- the tag is used by an object, e.g. an I/O field.

You can enter the bit mask in three different ways:

- Hexadecimal: First, enter "0h" or "0H" as prefix, followed by an optional space for better readability. Then group the bit pattern in blocks of four, for example (0000)(1001)(1010)(1110), and set each block in hexadecimal code: (0)(9)(A)(E). Only the characters 0-9, A-F, a-f are permitted for the input: "0h 09AE".
- Binary: First, enter "0b" or "0B" as prefix, followed by an optional space for better readability. Then group the binary bit pattern into blocks of four, for example 0000 1001 1010 1110 with spaces in between as a check. Only the characters "0" or "1" are permitted for the input: "0b 0000 1001 1010 1110".
- Decimal: Enter the value directly without prefix, for example "2478".

#### Use in the function list

ShiftAndMask (Source, Target, Bits to shift, Bit pattern)

The system function "ShiftAndMask" has the following parameters:

| Parameter | Description |
| --- | --- |
| Source | The Source parameter includes the input bit pattern. Integer-type tags, e.g. "Byte", "Char", "Int", "UInt", "Long" and "ULong", are permitted.   Example: The source of the 16-bit integer type has the current value 72: 0000000001001000. |
| Target | The output-bit pattern is stored in the Target. Integer type tags, e.g. "Byte", "Char", "Int", "UInt", "Long" and "ULong" are permitted. |
| Bits to shift | Number of bits by which the input bit pattern is shifted right. A negative value shifts the input bit pattern to the left.  Example: "Bits to shift" has the value "+3". The input bit pattern is shifted right by three bits when the system function is called: 0000000000001001. Bits to the left are padded with "0". Three bits are truncated on the right. The new decimal value is "9". |
| Bit pattern | An integer serves as bit mask. The bit pattern is used to multiply the shifted input bit pattern. |

> **Note**
>
> Note the following:
>
> - Source and target have the same number of bits. When the source and target have a different number of bits, using the system function in the target can result in a violation of the value range.
> - The number of the bits to shift is smaller than the number of bits of source and target.
> - Bit pattern has no more bits than source and target.
> - The left bit is "1" if the source has a signed Integer data type with the sign "-". This sign bit is padded with "0" when the bits are shifted right. The sign changes to "+".

#### Use in scripts

You can find more information on using the "ShiftAndMask" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ShiftAndMask()](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctshiftandmask)

### ClosePopup (RT Unified)

#### Description

Closes a pop-up window dynamically during runtime.

#### Use in the function list

ClosePopup (popup window path)

The system function "ClosePopup" has the following parameters:

| Parameter | Description |
| --- | --- |
| Popup window path | Specifies the path to the popup window to be closed. |

#### Use in scripts

You can find more information on using the "ClosePopup" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ClosePopup() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctclosepopup-rt-unified)
  
[Opening and closing a screen in a pop-up window (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#opening-and-closing-a-screen-in-a-pop-up-window-rt-unified)

### WriteParameterSet (RT Unified)

#### Description

Writes the values of the edit tag to the PLC.

To be able to use the system function, an edit tag must have been created at the associated parameter set type.

#### Use in the function list

WriteParameterSet (Parameter set type, Output status, Processing status (optional))

The system function "WriteParametersSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Using scripts

You can find more information on the "WriteParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.WriteParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctwriteparameterset-rt-unified)

### WriteManualValue (RT Unified)

#### Description

Assigns a new value to the specified logging tag. The associated time stamp is transferred in this process.

#### Use in the function list

WriteManualValue (Logging tag name, Value, Time stamp)

The system function "WriteManualValue" has the following parameters:

| Parameter | Description |
| --- | --- |
| Logging tag name | Logging tag to which the specified value is assigned. |
| Value | The value assigned to the specified logging tag. |
| Time stamp | The time stamp assigned to the specified value. |

#### Use in scripts

You can find more information on using the "WriteManualValue" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.WriteManualValue() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctwritemanualvalue-rt-unified)

### SetBitInTag (RT Unified)

#### Description

Sets the bit with the specified number to 1 in the tag (True).

After the specified bit is changed, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. HMI device and PLC only have read access to the specified tag until it is transferred back to the PLC.

For the system function to be executed, the value of the tags must be current and valid, and the quality code must correspond to Good (cascade).

The following conditions must be met for external tags:

- The connection to the PLC is set up.
- The acquisition mode of the tags is "Cyclic in operation".
- The tag is used at the "Process value" property of an object.

> **Note**
>
> The system function is executed with the last known process value. Since this process value cannot be kept up to date in all cases, it is prohibited to write it from multiple sources (e.g. from the HMI device via scripts and from the PLC). This ensures that the value that is changed actually corresponds to the process value.

#### Data types not supported

The following data types are not supported by the function:

- UINT

#### Use in the function list

SetBitInTag (Tag, Value)

The "SetBitInTag" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | The tag in which a bit is set to 1 (True). |
| Bit number | The number of the bit that is set to 1 (True).  When this system function is used in a user function, the bits in the given tag will be counted from right to left independent of the controller that is used. Numbering starts with 0. |

#### Use in scripts

You can find more information on using the "SetBitInTag" system function in JavaScript functions in the WinCC Unified object model.

#### Use of "SetBitInTag" in structure tags

If "SetBitInTag" is used at a structure tag, the result is that after setting and resetting individual bits, all previously changed bits are overwritten when they are set again. This occurs, for example, as a result of an event of a button.

To prevent this, follow these steps:

1. Convert the function at the event to JavaScript.

   ![Use of "SetBitInTag" in structure tags](images/153936918155_DV_resource.Stream@PNG-en-US.png)
2. Replace the "SetBitInTag" system function with the "SetBit()" method of the "Tags" object.

### SetDHCPState (RT Unified)

#### Description

Changes the DHCP setting of the network adapter.

> **Note**
>
> The "SetDHCPState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

SetDHCPState (Adapter name, Enabled, IP V6 (optional))

The system function "SetDHCPState" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter.   The following entries are possible:  - X1 = Static network adapter name 1 - X2 = Static network adapter name 2 - Manual input |
| Enabled | Defines the DHCP setting of the network adapter:  0 = DHCP is disabled.  1 = DHCP is enabled. |
| IP V6 (optional) | Tag to which the IPv6 address is written. |

#### Use in scripts

You can find more information on using the "SetDHCPState" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetDHCPState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetdhcpstate-rt-unified)

### SetPropertyValue (RT Unified)

#### Description

Assigns a new value to the specified property of the screen item.

> **Note**
>
> Depending on the type of the object property, you can use this system function to assign strings and numbers.

#### Use in the function list

SetPropertyValue (Screen item path, Screen item property name, Value)

The system function "SetPropertyValue" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen object path | Path of the screen item whose property is changed. |
| Screen object property name | Name of the property that will be changed.  The property name can be copied with selected screen item to the Inspector window under "Properties &gt; Properties":  1. Right-click the name of the property. 2. Select "Copy property name". |
| Value | The value assigned to the property. |

#### Use in scripts

You can find more information on using the "SetPropertyValue" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetPropertyValue() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetpropertyvalue-rt-unified)

### SetBrightness (RT Unified)

#### Description

Assigns a new value to the brightness of the display.

The value for the "SetBrightness" system function can be set between 0 and 100. The HMI devices support a brightness setting between 10% and 100%. The brightness settings on the HMI device can be viewed and edited in the Control Panel under "Settings &gt; Display". The configuration set in the Control Panel is restored when the HMI device is restarted.

- If the system function has been assigned a value of 0, the display of the HMI device is switched off in runtime. If the operator touches the display, the display switches to the previous brightness setting.
- If the system function has been assigned a value between 1 and 10, the brightness is set to 10% on the HMI device.
- If the system function has been assigned a value between 10 and 100, the brightness is set to this value.

> **Note**
>
> The "SetBrightness" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

SetBrightness (value)

The system function "SetBrightness" has the following parameters:

| Parameter | Description |
| --- | --- |
| Value | Value for the brightness of the display |

#### Use in scripts

You can find more information on using the "SetBrightness" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetBrightness() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetbrightness-rt-unified)

### SetIPV4Address (RT Unified)

#### Description

Changes the IPv4 settings of the network adapter.

> **Note**
>
> The "SetIPV4Address" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

SetIPV4Address (Name adapter, IP address, Subnet mask, Standard gateway (optional), DNS Server 1 (optional), DNS Server 2 (optional))

The system function "SetIPV4Address" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter.  The following entries are possible:  - X1 = Static network adapter name 1 - X2 = Static network adapter name 2 - Manual input |
| IP address | Specifies the IP address. |
| Subnet mask | Subnet mask of the IPv4 network. |
| Default gateway (optional) | IP address of the default gateway. |
| DNS server 1 (optional) | IP address of DNS server 1. |
| DNS server 2 (optional) | IP address of DNS server 2. |

#### Use in scripts

You can find more information on using the "SetIPV4Address" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetIPV4Address() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetipv4address-rt-unified)

### SetNetworkInterfaceState (RT Unified)

#### Description

Changes the state of the network adapter.

> **Note**
>
> The "SetNetworkInterfaceState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

SetNetworkInterfaceState (Adapter name, Enabled)

The system function "SetNetworkInterfaceState" has the following parameters:

| Parameter | Description |
| --- | --- |
| Adapter name | Specifies the name of the network adapter. The following entries are possible:  - X1 = addresses PROFINET (X1) Port 0. - X1.0 = addresses PROFINET (X1) Port 0. - X1.1 = addresses PROFINET (X1) Port 1. - X2 = addresses Ethernet (X2). - Manual input |
| Enabled | Specifies the state of the network adapter:  0 = Network adapter is disabled.  1 = Network adapter is enabled. |

> **Note**
>
> The Panel must be restarted after a change in the status of X1.0 or X1.1.

#### Use in scripts

You can find more information on using the "SetNetworkInterfaceState" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetNetworkInterfaceState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetnetworkinterfacestate-rt-unified)

### SetPLCDateTime

#### Description

Sets the date and time of the HMI device in the connected PLC.

> **Note**
>
> The "SetPLCDateTime" system function can only be configured for the following PLCs:
>
> - SIMATIC S7-1200
> - SIMATIC S7-1500

#### Use in the function list

SetPLCDateTime (Connection name)

The "SetPLCDateTime" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Connection name | Name of the connection of PLC and HMI device (optional)  If no parameter is passed, all S7+ connections are taken into consideration. |

#### Use in scripts

You can find more information on the "SetPLCDateTime" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetPLCDateTime() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetplcdatetime-rt-unified)

### SetLanguage (RT Unified)

#### Description

Toggles the language on the HMI device. All configured texts and system events are displayed on the HMI device in the newly set language.

#### Use in the function list

SetLanguage (LCID)

The system function "SetLanguage" has the following parameters:

| Parameter | Description |
| --- | --- |
| LCID | LCID of the language set on the HMI device. Specify the language ID, e.g. 1031 for German - Standard, 1033 for English - USA.  You can find an overview of all languages under: "https://docs.microsoft.com/de-de/deployoffice/office2016/language-identifiers-and-optionstate-id-values-in-office-2016". |

#### Use in scripts

You can find more information on using the "SetLanguage" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetLanguage() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetlanguage-rt-unified)

### SetSmartServerState (RT Unified)

#### Description

Allows you to enable or disable the smart server.

> **Note**
>
> The "SetSmartServerState" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

SetSmartServerState (Status)

The "SetSmartServerState" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Status | Status to which the Smart Server is to be set:  True = Smart Server is enabled.   False = Smart Server is disabled. |

#### Use in scripts

You can find more information on using the "SetSmartServerStart" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetSmartServerState() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetsmartserverstate-rt-unified)

### SetTagValue (RT Unified)

#### Description

Assigns the specified tag a new value.

Depending on the tag type, you use this system function to assign strings and numbers.

> **Note**
>
> The "SetTagValue" system function is only executed after a connection has been established.

#### Use in the function list

SetTagValue (Tag, Value)

The system function "SetTagValue" has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag to which the specified value is assigned. |
| Value | The value that is assigned to the specified variable. |

#### Use in scripts

You can find more information on using the "SetTagValue" system function in JavaScript functions in the WinCC Unified object model.

### SetConnectionMode (RT Unified)

#### Description

The specified connection is established or disconnected.

#### Use in the function list

SetConnectionMode (Connection name, Activated)

The "SetConnectionMode" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Connection name | The PLC whose connection to the HMI device is established or disconnected. You specify the name of the PLC in the connection editor. |
| Enabled | 0 = Offline: Connection is terminated.  1 = Online: Connection is established. |

#### Use in scripts

You can find more information on using the "SetConnectionMode" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SetConnectionMode() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsetconnectionmode-rt-unified)

### SaveParameterSet (RT Unified)

#### Description

Saves the current values of the edit tag of a parameter set to the memory of the HMI device.

To be able to use the system function, an edit tag must have been created at the associated parameter set type.

#### Use in the function list

SaveParameterSet (Parameter set type, Parameter set, Output status, Overwrite, Processing status (optional))

The system function "SaveParametersSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set | Specifies the name or the ID of the parameter set. If the name or ID of the parameter set does not exist, a new parameter set is created. |
| Overwrite | Specifies whether an existing parameter set is overwritten:  0 = Overwriting is not allowed.  1 = Overwriting is allowed.  The following cases are differentiated:  - If the name / ID of the specified parameter set exists, the values in the PLC are overwritten with the parameter set values in the memory if overwriting is allowed. - If overwriting is not allowed, the data in the memory is not replaced. The process tag is updated to the status of the system function, if configured accordingly. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Using scripts

You can find more information on the "SaveParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.SaveParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctsaveparameterset-rt-unified)

### StartProgram (RT Unified)

#### Description

Starts the specified program on the HMI device.

The runtime software continues running in the background.

Alarms continue to be output and process values continue to be updated.

When the given application is exited, the screen which was active during the performance of the system function is displayed on the HMI device.

This system function is used, for example, to edit recipe data records in MS Excel on the HMI device.

The function is supported by both the Windows and Linux systems.

> **Note**
>
> On a SIMATIC Unified PC, this system function can only be used to start applications that do not have a user interface.

#### Use in the function list

StartProgram (Program name, Program parameters, Display mode, Wait for end of program, Result (optional))

The system function "StartProgram" has the following parameters:

| Parameter | Description |
| --- | --- |
| Program name | Name and path of the program which is started. Upper and lower case are taken into account in this parameter. |
| Program parameters | The parameters you transfer at the start of the program, for example a file that is opened after the start of the program.   You can find additional information on the necessary parameters in the documentation of the program to be started. |
| Display mode | Determines how the program window is displayed on the HMI device. This function has no effect on Linux systems. |
| Waiting for program to end | Determines whether there is a change back to the project after the called up program has ended:  0 = No change to project.  1 = Change to project. |
| Result (optional) | Contains data that can be written to the standard output from an external application. |

> **Note**
>
> If the path for the program name contains spaces, the program can only be started correctly if the path is specified in quotation marks, e.g. "C:\Program Files\START\start.exe".

#### Use in scripts

You can find more information on using the "StartProgram" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.StartProgram() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctstartprogram-rt-unified)
  
[Win32 Microsoft](https://docs.microsoft.com/en-us/locale/?target=https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow)

### StopRuntime (RT Unified)

#### Description

Ends the runtime software and the project running on the HMI device.

The system function can be used with or without parameters. If no parameters are specified, the system function remains undefined and stops the running project. In this case, the HMI device is not restarted.

> **Note**
>
> All functions after "StopRuntime" are not executed.

#### Use in the function list

StopRuntime (StopRuntime, stop runtime and restart operating system)

The "StopRuntime" system function can be used with or without the following parameter:

| Parameter | Description |
| --- | --- |
| Mode (optional) | Sets the type of termination: 0 = Ends runtime.  1 = Ends runtime and restarts the device. |

#### Use in scripts

You can find more information on using the "StopRuntime" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.StopRuntime() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctstopruntime-rt-unified)

### StopTagLogging (RT Unified)

#### Description

Stops the logging of one or all configured data logs.

After logging is stopped:

- A system alarm is output. The system alarm disappears as soon as logging is restarted.
- Existing log entries remain readable.
- An entry is made in the Audit Trail unless the logging of Audit Trails has been stopped.

#### Use in the function list

StopTagLogging (Log name)

The "StopTagLogging" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Log name | Name of the data log whose logging is to be stopped.  If no log name is specified, the logging of all configured data logs is stopped. |

#### Use in scripts

You can find more information on using the "StopTagLogging" system function in JavaScript functions in the WinCC Unified object model.

### LookUpText (RT Unified)

#### Description

Identifies a list entry from a text list. The result depends on the value of the list entry and the selected runtime language. The result is saved to a tag of data type "String".

#### Use in the function list

CallText (output text, index, LCID, text list name)

The system function "LookUpText" has the following parameters:

| Parameter | Description |
| --- | --- |
| Output text | The tag to which the result is written. |
| Index | The tag that defines the value of the list entry. |
| LCID | LCID of the language set on the HMI device. Specify the language ID, e.g. 0x0409 for English - USA, 0x0007 for German - Standard.  You can find an overview of all languages under: "https://msdn.microsoft.com/en-us/library/cc233982.aspx". |
| Text list name | Defines the text list. The list entry is read from the text list. |

#### Use in scripts

You can find more information on using the "LookUpText" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.LookUpText() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctlookuptext-rt-unified)

### RenameParameterSet (RT Unified)

#### Description

Changes the name of a parameter set.

#### Use in the function list

RenameParameterSet (Parameter set type, Parameter set, NewParameterSetName, Output status, Processing status (optional))

The system function "RenameParametersSet" has the following parameters:

| Parameter | Description |
| --- | --- |
| Parameter set type | Specifies the name or the ID of the parameter set type. If the name or ID of the parameter set type does not exist, execution is terminated. |
| Parameter set | Specifies the name or the ID of the parameter set. If the name or ID of the parameter set does not exist, execution is terminated. |
| New parameter set name | Specifies the new name of the parameter set in the current Runtime language. |
| Output status | Defines the output status: True = Alarms are output. False = Alarms are not output. |
| Processing status (optional) | Indicates the execution status of a function: 2 = Function is being executed. 4 = Function successfully executed. 12 = Function was canceled. |

#### Using scripts

You can find more information on the "RenameParameterSet" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.RenameParameterSet() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctrenameparameterset-rt-unified)

### ToggleGRAPHViewerMode (RT Unified)

#### Description

Switches to the GRAPH-Viewer Mode of the PLC code view.

#### Use in the function list

ToggleGRAPHViewerMode (object path to PLC code view)

The system function "ToggleGRAPHViewerMode" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "ToggleGRAPHViewerMode" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ToggleGRAPHViewerMode() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfcttogglegraphviewermode-rt-unified)

### ToggleNetworkDisplay (RT Unified)

#### Description

Switches to the network display of the PLC code view.

#### Use in the function list

ToggleNetworkDisplay (Object path to PLC code view)

The system function "ToggleNetworkDisplay" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "ToggleNetworkDisplay" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ToggleNetworkDisplay() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfcttogglenetworkdisplay-rt-unified)

### ToggleLanguage (RT Unified)

#### Description

This function allows you to change the runtime language in order to display language-dependent texts correctly on the user interface. The conversion takes place according to the runtime language configuration.

#### Use in the function list

ToggleLanguage()

The system function "ToggleLanguage" has no parameters.

#### Use in scripts

You can find more information on using the "ToggleLanguage" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ToggleLanguage() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfcttogglelanguage-rt-unified)

### ZoomIn (RT Unified)

#### Description

Zooms in the view of the network in the network area of a PLC Code View.

#### Use in the function list

Zoom in (Object path to PLC code view)

The system function "ZoomIn" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "ZoomIn" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ZoomIn() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctzoomin-rt-unified)

### ZoomOut (RT Unified)

#### Description

Zooms out of the view of the network in the network area of a PLC code view.

#### Use in the function list

ZoomOut (Object path to PLC code view)

The system function "ZoomOut" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "ZoomOut" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ZoomOut() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctzoomout-rt-unified)

### DecreaseTag (RT Unified)

#### Description

Subtracts the given value from the tag value: X = X - a

If you configure the system function for events of an alarm without the tag being used in the current screen, it is not ensured that the actual tag value is being used in the PLC.

For the system function to be executed, the value of the tags must be current and valid, which means the quality code must correspond to Good (cascade).

The following conditions must be met for external tags:

- the connection to the PLC is set up and
- the acquisition mode of the tags is "Cyclic in operation" and
- the tag is used at the "Process value" property of an object.

> **Note**
>
> The system function is executed with the last known process value. Since this process value cannot be kept up to date in all cases, it is prohibited to write it from multiple sources (e.g. from the HMI device via scripts and from the PLC). This ensures that the value that is changed actually corresponds to the process value.

#### Use in the function list

DecreaseTag (Tag, Value)

The system function "DecreaseTag" has the following parameters:

| Parameter | Description |
| --- | --- |
| Tag | Tag from which the specified value is subtracted.  The following data types are not supported: Byte, Word, DWord, LWord. |
| Value | Value to be subtracted. |

> **Note**
>
> **Converting a value**
>
> The system function uses the same tag as input and output values. If you are using this system function to convert a value, follow these steps:
>
> 1. Create an auxiliary tag.
> 2. Assign the tag value to the auxiliary tag with the "SetTagValue" system function.

#### Use in scripts

You can find more information on using the "DecreaseTag" system function in JavaScript functions in the WinCC Unified object model.

### ChangeScreen (RT Unified)

#### Description

Loads a new screen into a screen window.

> **Note**
>
> The function list is updated when the screen changes. The functions after "ChangeScreen" are therefore not executed.
>
> Always execute "ChangeScreen" as the last function.

#### Use in the function list

ChangeScreen (Screen name, Screen window path)

The system function "ChangeScreen" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen name | Name of the screen to which you change. |
| Screen window path | Path of the screen window or base screen that is displayed after the change has been completed.   You can find additional information at "Addressing screen windows". |

#### Use in scripts

You can find more information on using the "ChangeScreen" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ChangeScreen() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctchangescreen-rt-unified)

### ChangeScreenAsync (RT Unified)

#### Description

Switches the screen in a screen window. Switching only takes place after the current screen has been fully loaded.

#### Principle

ChangeScreenAsync (Screen name, Screen window path)

The system function "ChangeScreenAsync" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen name | Specifies the name of the new screen. |
| Screen window path | Specifies the path of the screen window in which the screen is to be changed, e.g. "Screen_window_1" |

#### Using scripts

You can find more information on the "ChangeScreenAsync" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ChangeScreenAsync() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctchangescreenasync-rt-unified)

### ChangeScreenAsyncWithNumber (RT Unified)

#### Description

Switches the screen asynchronously in a screen window. Switching only takes place after the current screen has been fully loaded.

#### Principle

ChangeScreenAsyncWithNumber (screen number, screen window path)

The system function "ChangeScreenAsyncWithNumber" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen number | Unique number (&gt; 0) of the new screen to which you change. |
| Screen window path | Path of the top-level screen window or screen in which the screen is to be switched, for example, "Screen_window_1" |

#### Using scripts

You can find more information on the "ChangeScreenAsyncByNumber" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ChangeScreenAsyncByNumber() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctchangescreenasyncbynumber-rt-unified)

### ChangeScreenWithNumber (RT Unified)

#### Description

Performs a screen change to the specified screen window.

> **Note**
>
> The function list is updated when the screen changes. The functions after "ChangeScreenWithNumber" are therefore not executed.
>
> Always execute "ChangeScreenWithNumber" as the last function.

#### Use in the function list

ChangeScreenWithNumber (screen number, screen window path)

The system function "ChangeScreenWithNumber" has the following parameters:

| Parameter | Description |
| --- | --- |
| Screen number | Unique number (&gt; 0) of the new screen to which you change. |
| Screen window path | Path of the top-level screen window or screen in which the screen is to be switched, for example, "Screen_window_1" |

#### Use in scripts

You can find more information on using the "ChangeScreenByNumber" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ChangeScreenByNumber() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctchangescreenbynumber-rt-unified)

### ChangeConnection (RT Unified)

#### Description

Changes the connection parameters of an HMI connection. The following parameters can be changed: The IP address, the slot number and the rack number. Because the function is executed synchronously, the return value returns an error code that provides immediate information about the cause of the error. The error code can only be read if the function is called via a script.

> **Note**
>
> **Change of function parameters after a function call**
>
> With the execution of the function you change the function parameters. The new connection may not be active yet at this point.

> **Note**
>
> **Usage on devices of the S7 Plus PLC family**
>
> For devices of the S7 Plus PLC family (PLCs 15xx and 12xx) it is not possible to change the slot or the rack. The system function cannot be executed if parameters for slot or rack are set.

#### Use in the function list

ChangeConnection (Connection name, IP V4 address, Slot (optional), Rack (optional))

The "ChangeConnection" system function has the following parameters:

| Parameter | Description |
| --- | --- |
| Connection name | Indicates the name of the connection. |
| IP V4 address | Specifies the IPv4 address, e.g. 192.169.153.45. |
| Slot (optional) | Specifies the slot number. Permitted values from 1 to 32. |
| Rack (optional) | Specifies the rack number. Permitted values from 0 to 7. |

#### Use in scripts

You can find more information on using the "ChangeConnection" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ChangeConnection() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctchangeconnection-rt-unified)

### Next (RT Unified)

#### Description

Goes to the next network in a PLC code view.

#### Use in the function list

Next (Object path to PLC code view)

The system function "Next" has the following parameters:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "Next" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.Next() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctnext-rt-unified)

### ShowLoginDialog (RT Unified)

#### Description

Opens a login dialog for entering user name and password without leaving the currently displayed screen.

#### Use in the function list

ShowLoginDialog ()

The "ShowLoginDialog" system function has no parameters.

#### Use in scripts

You can find more information on using the "ShowLoginDialog" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ShowLoginDialog() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctshowlogindialog-rt-unified)

### ShowControlPanel (RT Unified)

#### Description

- Hides or shows the Control Panel.
- Opens an applet in runtime.

> **Note**
>
> The "ShowControlPanel" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

ShowControlPanel (Home)

The "ShowControlPanel" system function has the following parameter:

| Parameter | Description |
| --- | --- |
| Home page | Specifies the applet to be displayed: "AppletName" |

#### Use in scripts

You can find more information on using the "ShowControlPanel" system function in JavaScript functions in the WinCC Unified object model.

#### List of available applets

List of applet names that are available to the system function:

| Display page | Applet name |
| --- | --- |
| Panel information | SystemProperties.PanelInformation |
| Display | SystemProperties.Display |
| Screensaver | SystemProperties.Screensaver |
| Reboot | SystemProperties.Reboot |
| Network settings | NetworkandInternet.NetworkSettings |
| Date And Time | LanguageRegionAndFormats.DateAndTime |
| User Management | Security.UserManagement |

---

**See also**

[SysFct.ShowControlPanel() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctshowcontrolpanel-rt-unified)

### ShowSoftwareVersion (RT Unified)

#### Description

Hides or shows the version number of the Runtime software.

Use this system function if during servicing, for example, you required the version of the runtime software used.

> **Note**
>
> The "ShowSoftwareVersion" system function is only available for WinCC Unified Comfort Panel. The system outputs a compiler warning if the function is used through manual input or through a device replacement in SIMATIC WinCC Unified PC.

#### Use in the function list

ShowSoftwareVersion ()

The system function "ShowSoftwareVersion" has no parameters.

#### Use in scripts

You can find more information on using the "ShowSoftwareVersion" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.ShowSoftwareVersion() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctshowsoftwareversion-rt-unified)

### Previous (RT Unified)

#### Description

Navigates to the previous network in a PLC code view.

#### Use in the function list

Previous (Object path to PLC code view)

The "Back" system function has the following parameter:

| Parameter | Description |
| --- | --- |
| Object path to PLC code display | Path of the PLC code view |

#### Using scripts

You can find more information on the "Previous" system function in JavaScript functions in the WinCC Unified object model.

---

**See also**

[SysFct.Previous() (RT Unified)](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#sysfctprevious-rt-unified)

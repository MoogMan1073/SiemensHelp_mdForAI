---
title: "What's new in TIA Portal"
package: PENewsenUS
topics: 82
source: Siemens TIA Portal Information System (offline help, en-US)
---


# What's new in TIA Portal

This section contains information on the following topics:

- [What's new in TIA Portal V19](#whats-new-in-tia-portal-v19)
- [What's new in TIA Portal V18](#whats-new-in-tia-portal-v18)
- [What's new in TIA Portal V17](#whats-new-in-tia-portal-v17)
- [What's new in TIA Portal V16](#whats-new-in-tia-portal-v16)
- [What's new in TIA Portal V15.1](#whats-new-in-tia-portal-v151)
- [What's new in TIA Portal V15](#whats-new-in-tia-portal-v15)
- [What's new in TIA Portal V14 SP1](#whats-new-in-tia-portal-v14-sp1)
- [What's new in TIA Portal V14](#whats-new-in-tia-portal-v14)

## What's new in TIA Portal V19

This section contains information on the following topics:

- [TIA Portal](#tia-portal)
- [SIMATIC STEP 7](#simatic-step-7)
- [SIMATIC WinCC](#simatic-wincc)
- [Hardware configuration](#hardware-configuration)
- [SIMATIC Visualization Architect](#simatic-visualization-architect)
- [SINAMICS Startdrive](#sinamics-startdrive)
- [SINUMERIK](#sinumerik)
- [SIMOTION](#simotion)
- [System functions](#system-functions)
- [Engineering options](#engineering-options)
- [Runtime options](#runtime-options)
- [TIA Portal Openness](#tia-portal-openness)

### TIA Portal

#### Discover the highlights of V19

TIA Portal V19 provides several new functions. You can find an overview of and detailed information about the new functions in this contribution:

[https://support.industry.siemens.com/cs/ww/en/view/109821307](https://support.industry.siemens.com/cs/ww/en/view/109821307)

### SIMATIC STEP 7

All important new features of STEP 7 are summarized here. You can find more details on the various topics in the product documentation sections.

#### Named value data types according to IEC 61131-3 (S7-1500)

As of V19, you can declare named value data types (NVT) and use them in your program. Named value data types contain a set of values that are assigned a unique set of names. The names can be easily referenced throughout the program and make it easier to read and maintain the program.

Named value data types have a base data type that applies to all elements within the named value data type.

Tags based on Named value data types can assume all values within the value range of the base data type, thus including values not explicitly specified in the declaration.

See also: [Basics of named value data types](Data%20types.md#basics-of-named-value-data-types-s7-1500)

#### Symbolic access during runtime (S7-1500)

The "Symbolic access during runtime" function gives external applications access to the tags in the PLC program during runtime. External applications can be, for example, HMI applications, OPC UA functions or other communication functions.

With V19, the "Symbolic access during runtime" function offers the following new features:

- You can also access the following types of data through symbolic names at runtime:

  - Structured data types, e.g., ARRAY or STRUCT.
  - STRING and WSTRING
  - DTL
- The list of tag names that you specify at the parameter "nameList" of the system function block "ResolveSymbols" can also be in a non-optimized memory area.
- As of FW version 3.0, the system data type "ResolvedSymbol" can be declared as an element of a PLC data type.

See also: [Symbolic access during runtime](SCL%20%28S7-1200%2C%20S7-1500%29.md#symbolic-access-during-runtime-s7-1500)

#### Filtering PLC tag tables

You can now filter PLC tag tables. A new filter view is available for this purpose. Filters especially assist you in targeted searching and replacing of entries.

See also: [Filtering entries in the PLC tag table](Declaring%20PLC%20tags.md#filtering-entries-in-the-plc-tag-table)

#### Virtual CPUs for Edge-based automation applications

You can insert and configure virtual CPUs into a project, e.g. a CPU S7-1587V. Functionally these CPUs are not different from standard CPUs. Virtual CPUs have the advantage, however, that since they are not hardware-dependent, they can be easily integrated in an Industrial Edge Computing platform.

See also: [Principle of operation of virtual CPUs](Configuring%20automation%20systems.md#principle-of-operation-of-virtual-cpus)

#### Fully-qualified names for program elements in software units

The length restriction for fully qualified names of program elements in software units has been made more flexible. The fully qualified name is composed of the namespace and the name. The name and namespace of a program element may now be 125 characters long in total. This also applies to nested namespaces. Dots used as separators are counted as well.

See also: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

#### Trace

- Long-term trace

  You can display and analyze the values directly in the chart during the recording.

  You can use superimposed measurements for the long-term trace. You can synchronize the time bases.

  R/H CPUs support the long-term trace via a connection to the primary CPU. In the event of a system-related switch to the backup CPU, the data in the backup CPU continues to be recorded. You can only save this data when the primary CPU is active again and you have restarted the long-term trace.
- Long-term project trace

  With the long-term project trace, you can record signals from different CPUs S7-1500 at the same time. The CPUs must be configured in a network. The recording is stored on a drive that you have configured.
- Improved operation

  Additional functions from the toolbar are now also available via a shortcut menu.

  You can zoom in and out of the signal characteristics using the right mouse button.

#### S7-1500 and S7-1500T Motion Control

You can find an overview of the new features in technology version V8.0 in the S7-1500/S7-1500T Motion Control Overview, in section [New features V8.0](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#new-features-v80-s7-1500-s7-1500t).

#### PID Control

- **Instruction"**
  **Filter_Universal**"

  The new auxiliary "Filter_Universal" function for SIMATIC S7-1500 controllers is a configurable digital filter of order 1 to 10.

  The instruction is used to manipulate a signal in such a way that specific frequency components of this signal are either allowed passed or attenuated.

  The filter parameters including frequency, bandwidth, type, characteristic, and order can be set by the user to achieve the desired behavior.
- **PID_Compact**
   **V3.0 with adjustable deadband**

  The new version V3.0 of the PID_Compact closed-loop controller for SIMATIC S7-1500 controllers allows the deadband to be set to reduce output signal fluctuations with noisy input value.

  If a process value is influenced by noise, the noise can also have a significant impact on the output value, especially when the closed-loop controller's gain is high. The adjustable deadband can help reduce such fluctuations.

#### Instructions as of firmware version V3.1

Note that for S7-1500R/H CPUs, the associated firmware will be supplied together with an HSP following start of delivery of TIA Portal V19.

- The new "Random" instruction is used to generate a 32-bit random number for an S7-1500 CPU or S7-1500R/H CPU.

  See also: [Random: Generate random number](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#random-generate-random-number-s7-1500)
- The new "SHA2" instruction calculates a SHA2 hash value from a specified data area for an S7-1500 CPU.

  See also: [SHA2: Form hash value using SHA2](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#sha2-form-hash-value-using-sha2-s7-1500)
- The existing "RT_INFO" instruction is extended as follows:

  - You can reset all OB statistics.
  - You can reset the longest cycle time.
  - You can reset the shortest cycle time.
  - You can reset the longest and the shortest cycle time with a call of "RT_INFO".

  See also: [RT_INFO: Read out runtime statistics](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rt_info-read-out-runtime-statistics-s7-1500)
- You use the new "GetSymbolForReference" instruction to determine the name of an indirectly addressed object for an S7-1500 CPU.

  See also: [GetSymbolForReference: Determine name of an indirectly addressed object](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#getsymbolforreference-determine-name-of-an-indirectly-addressed-object-s7-1500)
- The existing "RH_CTRL" instruction for S7-1500R/H CPUs is extended as follows:

  - You can request that one of the two R/H-CPUs goes into the "STOP" mode and takes on the role of the backup CPU.
  - You can specify that the "SYNCUP" system state be run through without the intended MRP check when there is at least one MRP ring present.

  See also: [RH_CTRL: Influencing sequences in R/H systems](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rh_ctrl-influencing-sequences-in-rh-systems-s7-1500)
- The S7-1500R/H redundant system supports the data logging instructions. With data logging, you save process values from the user program in a file, the data log. The data logs are saved on the SIMATIC Memory Card in csv format and stored in the "DataLogs" directory.

  See also: [Data logging](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#data-logging-s7-1200-s7-1500)
- The S7-1500R/H redundant system supports the instructions for editing user files.

  See also: [File handling](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#file-handling-s7-1200-s7-1500)
- The new instruction version V1.1 is supported for the existing instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost".

  You can find the related details here: [Product information on documentation S7-1500/ET 200MP, S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/68052815)

### SIMATIC WinCC

This section contains information on the following topics:

- [Efficient configuration](#efficient-configuration)
- [Configuring screens](#configuring-screens)
- [System functions and scripting](#system-functions-and-scripting)
- [Diagnostics](#diagnostics)
- [User administration](#user-administration)
- [Connectivity](#connectivity)
- [Options](#options)
- [Unified PC Runtime](#unified-pc-runtime)

#### Efficient configuration

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### One Edition - Installation set

The installation of the engineering system for WinCC Unified Runtime, WinCC Runtime Professional und WinCC Runtime Advanced takes place from a shared data storage medium. To use the simulation, you must install Runtime systems. If no license is found for Runtime, start the simulation in demo mode.

Parallel installation with WinCC V7.x or WinCC V8.x is possible with V19.

> **Note**
>
> If TIA Portal V19 is installed with WinCC Unified and/or WinCC Professional, take into account that only such older WinCC components &lt; V19 which are released according to the compatibility tool are installed subsequently.  
> https://support.industry.siemens.com/cs/ww/de/view/64847781

##### Multiuser support for configuration of screens

Engineering times can be greatly reduced through the parallel configuration of screens for Unified devices. With Multiuser Engineering, several configurators in the team can work concurrently on different screens.   
See also [Overview of the mode of operation with Multiuser Engineering](Using%20Multiuser%20Engineering.md#overview-of-the-mode-of-operation-with-multiuser-engineering).

##### New devices

SIPLUS HMI Unified Comfort Panels are optimized for outstanding visualization under extreme ambient conditions. All the devices have the same number of hardware interfaces and the same functionality. Every Unified Comfort Panel is available in the standard design with Siemens- and SIMATIC HMI branding as well as a silver-colored aluminum frame.

SIPLUS HMI Unified Comfort Panels with display unit sizes 7”, 10” and 12” can be configured with V19.

##### Efficient configuration

The simulation can be started with a click on an icon in the toolbar.

In a project, you can swap one device for another with a different display size. The configured screen size is adapted to the size of the new target device using the command in the context menu.

See also [Changing the screen resolution](Configuring%20screens%20%28RT%20Unified%29.md#changing-the-screen-resolution-rt-unified).

Text lists can be created as types in libraries. The configured text list types can be maintained and versioned centrally and reused across all projects.

See also Creating text lists as type.

The resources monitor of an HMI device provides an overview of the current number of screens, the HMI tags used, logging tags, connections and the project size.

See also [Resources Monitor](WinCC%20Unified%20%28RT%20Unified%29.md#resources-monitor-rt-unified).

##### Logging

Segment-based backup for SQLite is supported for all log types of the HMI devices Unified PC and Unified Comfort Panel.

The "SQLite" database type must be enabled so that the HMI device can use SQLite.

See also [Log basics](Logging%20data%20%28RT%20Unified%29.md#log-basics-rt-unified)

##### Information system

A graphical access to the relevant information for the topics "User administration" and "Certificates" has been implemented in the information system. Important topics in the information system, in the SIEMENS Industry Online Support or in the SIMATIC WinCC Unified Tutorial Center can be reached with just a few clicks.

See also [Configuring users and roles](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#configuring-users-and-roles-rt-unified-1).

See also [Certificates in WinCC Unified](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#certificates-in-wincc-unified-rt-unified).

##### WinCC Unified Corporate Designer

SIMATIC WinCC Unified Corporate Designer is a stand-alone application that is geared towards TIA Portal. You can design your user interface in TIA Portal projects using an individual style. The Corporate Designer provides a style library with a selection of objects and controls in typical, frequently-in-demand designs (for example angular corners), and different fonts and colors.​

The user can create the user-defined styles based on the style library, import them into their TIA Portal project, assign them to the configured WinCC Unified device and reuse them.​

The WinCC Unified Corporate Designer runs independently of the TIA Portal installation.

See also [SIMATIC WinCC Unified Corporate Designer](https://support.industry.siemens.com/cs/ww/en/view/109824234).

#### Configuring screens

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### Background color of the screen

A specific background color can be configured for the screens in the project. A common layout is achieved as a result.

In a newly created device, the selected color is used in all screens. In an existing device, the configured color is used in all newly added screens.

See also [Using the toolbar in the screen editor](Configuring%20screens%20%28RT%20Unified%29.md#using-the-toolbar-in-the-screen-editor-rt-unified).

##### Persistence of the property columns

For image objects that contain a collection of similar elements under the properties, for example, curves or columns, the properties are efficiently administered in the Inspector window in a table. The user can:

- Show or hide the individual columns
- Show all columns.
- Optimize the column width.
- Move the columns with drag-and-drop.

The changed sort order and modified visibility of the columns is saved across projects.

See also [Displaying the properties of a collection](Configuring%20screens%20%28RT%20Unified%29.md#displaying-the-properties-of-a-collection-rt-unified).

##### Toolbar in the screen editor

The toolbar in the screen editor allows you to position the objects in the screen and to configure frequently used properties efficiently. Additional buttons in the toolbar make it possible to determine

- The font and its properties
- The horizontal text alignment
- The border and line thickness
- The line type

See also [Using the toolbar in the screen editor](Configuring%20screens%20%28RT%20Unified%29.md#using-the-toolbar-in-the-screen-editor-rt-unified).

##### "Hide change events" function

The "Hide change events" function !["Hide change events" function](images/167561903115_DV_resource.Stream@PNG-de-DE.png) is provided so as to be able to work efficiently with the Properties in the Inspector window. If the function is activated, the arrow in front of the name of a property is displayed only for properties that contain further properties.

See also [Managing properties](Configuring%20screens%20%28RT%20Unified%29.md#managing-properties-rt-unified).

##### Moving objects in the Inspector window to other layers

Objects can also be moved in the Inspector window to another layer with "Properties &gt; Miscellaneous &gt; Layer".

See also [Moving objects between layers](Configuring%20screens%20%28RT%20Unified%29.md#moving-objects-between-layers-rt-unified).

##### Removing or deleting objects from the group

Objects can be removed from a group from the context menu. The objects that are removed are placed outside the group on the screen.

Objects can be deleted from a group or a layer via the context menu. The deleted objects are removed from the screen.

See also [Removing an object from the group](Configuring%20screens%20%28RT%20Unified%29.md#removing-an-object-from-the-group-rt-unified) and [Deleting an object from the group](Configuring%20screens%20%28RT%20Unified%29.md#deleting-an-object-from-the-group-rt-unified).

##### Event "Input finished" at the IO field.

The "Input finished" event can be configured at the "IO field". The "Input finished" event is triggered when you press the &lt;Return&gt; key after inputting the value, or click another object. For example, you can script this event to check whether the value you entered is within the defined limits.

See also [Triggering the "Input finished" event](Configuring%20screens%20%28RT%20Unified%29.md#triggering-the-input-finished-event-rt-unified).

##### Highlighting and resetting properties

In the Runtime settings of the device, you can set one of the pre-defined styles. You can change some properties of screens and screen objects in the Inspector window, for example the background color, irrespective of the style values.

In the Inspector window, you can highlight those properties whose value is different from the specification in the style, and reset it to the default value.

See also [Highlighting and resetting properties](Configuring%20screens%20%28RT%20Unified%29.md#highlighting-and-resetting-properties-rt-unified).

##### Zooming in Runtime without the Control key

Zooming in Runtime without using the &lt;Ctrl&gt; key can be configured in the Runtime settings of the device by activating the option "Zooming without pressing the Control key".

See also [Configuring zooming in runtime without Control key](Configuring%20screens%20%28RT%20Unified%29.md#configuring-zooming-in-runtime-without-control-key-rt-unified).

##### Configuring screen management

You can configure a main screen window in screen management. A screen is assigned to the main screen window. The main screen window allows you to focus on areas of the assigned screen in Runtime by zooming and scrolling.

See also [Configuring screen management](Configuring%20screens%20%28RT%20Unified%29.md#configuring-screen-management-rt-unified).

##### Faceplates

The global search takes into consideration types in the libraries and interface properties of faceplate instances.

See also Searching, replacing and rewiring

You have the option in local scripts, for example in screens, faceplates or script modules, to search and replace.

See also Searching, replacing and rewiring

Tag parameters at interface tags of faceplate instances allow dynamic data exchange without scripting. The use of tag parameters allows for a more flexible or complex standardization of faceplates.

You can define a tag name consisting of static and dynamic parts as a tag parameter. The dynamic parts are tag references that are replaced at Runtime with the current tag values. The resulting tag name is thus dependent on the values of the tag references.

See also [Dynamizing an object property using a tag parameter](Configuring%20screens%20%28RT%20Unified%29.md#dynamizing-an-object-property-using-a-tag-parameter-rt-unified)

The screen size of a faceplate type can be automatically adjusted to match the content under consideration of the desired outside margin, in the context menu by using the function "Match screen size to content".

See also [Editing the visualization of a faceplate type](Configuring%20screens%20%28RT%20Unified%29.md#editing-the-visualization-of-a-faceplate-type-rt-unified)

The "Interruptible" property of faceplate types allows the interruption of script executions of the faceplates that are not visible in the current display in Runtime. When the faceplates are made visible again, pending script executions are resumed. The use of the "Interruptible" property can be used to improve performance in projects with many faceplates in a screen.

See also [Performance improvement when using a large number of faceplates](Configuring%20screens%20%28RT%20Unified%29.md#performance-improvement-when-using-a-large-number-of-faceplates-rt-unified)

The lowest device version of a faceplate type is defined on the version level. If you upgrade a faceplate type in the project library, a new version with the desired lowest device version is created. The previous version retains the lowest device version.

See also [Lowest device version of a faceplate type](Configuring%20screens%20%28RT%20Unified%29.md#lowest-device-version-of-a-faceplate-type-rt-unified)

##### Clock - display in analog or digital form

You can configure an analog or a digital display for the Clock object.

See also [Clock](Configuring%20screens%20%28RT%20Unified%29.md#clock-rt-unified).

#### System functions and scripting

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### System functions

The "ActivateCleanScreen" system function opens a screen as a popup window in full-screen mode and disables the touch screen of the Unified Panels. While the clean screen is open, no screen object of the underlying screen can be used. When the configured time interval has elapsed, the popup window is closed.

See also [ActivateCleanScreen](Using%20system%20functions%20%28RT%20Unified%29.md#activatecleanscreen-rt-unified)

The system function "SetPLCDateTime" enables time synchronization between PLCs and an HMI device. The system function has been enabled for the PLCs SIMATIC S7-1200 and S7-1500.

See also [SetPLCDateTime](Using%20system%20functions%20%28RT%20Unified%29.md#setplcdatetime)

The following system functions are available for the jog mode:

- [ReadAndIncreaseTag](Using%20system%20functions%20%28RT%20Unified%29.md#readandincreasetag-rt-unified)
- [ReadAndInvertBitInTag](Using%20system%20functions%20%28RT%20Unified%29.md#readandinvertbitintag-rt-unified)
- [ReadAndResetBitInTag](Using%20system%20functions%20%28RT%20Unified%29.md#readandresetbitintag-rt-unified)
- [ReadAndSetBitInTag](Using%20system%20functions%20%28RT%20Unified%29.md#readandsetbitintag-rt-unified)
- [ReadAndSetTagValue](Using%20system%20functions%20%28RT%20Unified%29.md#readandsettagvalue-rt-unified)
- [ReadAndDecreaseTag](Using%20system%20functions%20%28RT%20Unified%29.md#readanddecreasetag-rt-unified)

The functions differ from the system functions "DecreaseTag", "IncreaseTag", "InvertBitInTag", "SetBitInTag", "ResetBitInTag" and "SetTagValue" in the following way:

- The HMI device updates the value of the HMI tag with the value from the PLC before the write operation occurs.
- After the write operation, the value of the HMI tag is updated immediately, e.g. in an IO field.

The new functions are slower due to the updating of the tag at the beginning and end of jog mode. It is recommended that you use the features only when they have to perform time-critical tasks.

The system function "ExecuteToolbarButton" executes a button of the toolbars of the alarm control, parameter set control or system diagnostics.

The following buttons are available for the screen object:

- [Alarm control](Using%20system%20functions%20%28RT%20Unified%29.md#executetoolbarbutton-alarm-control-rt-unified)

  - Single acknowledgment
  - Group acknowledgment
- [Parameter set control](Using%20system%20functions%20%28RT%20Unified%29.md#executetoolbarbutton-parameter-set-control-rt-unified)

  - Save
  - Create
  - Delete
  - Rename
  - Write to PLC
  - Read from PLC
  - Export
  - Import
  - Cancel
- [System diagnostics control](Using%20system%20functions%20%28RT%20Unified%29.md#executetoolbarbutton-system-diagnostics-control-rt-unified)

  - Previous
  - Continue
  - Reload
  - Home
  - First line
  - Previous line
  - Next line
  - Last line
  - Share view
  - Back
  - Show diagnostic buffer

##### Scripting

The compilation of changes in the case of scripts, especially global scripts, has been improved.

The lowest device version of a script mode type is defined on the version level. If you upgrade a script module type in the project library, a new version with the desired lowest device version is created. The previous version retains the lowest device version.

See also [Lowest device version of a script module type](Runtime%20scripting%20%28RT%20Unified%29.md#lowest-device-version-of-a-script-module-type-rt-unified)

Importing and exporting JavaScript functions and JavaScript types is possible.

The Openness API can be used to swap JavaScript functions and JavaScript types with external version management systems.

#### Diagnostics

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### System diagnostics

The system diagnostics provide an intelligent and simple monitoring of the entire plant and display the system components in a clear and well-arranged manner.

The functionality is available on WinCC Unified PC and Unified Panels.

The object "System diagnostics display" is available in three view types:

- Matrix view
- Diagnostic view
- Distributed I/O view

The "Distributed I/O view" view type shows the distributed devices of the PROFINET IO system. The requirement is that only one PLC is configured with a PROFINET IO system. Otherwise, Runtime switches back to the matrix view.

See also "[System diagnostics display](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#system-diagnostics-display-rt-unified)".

##### Process diagnosis

In addition to the established system diagnostics, there is an integrated machine and plant diagnostics available for WinCC Unified, with a criteria analysis for GRAPH overview and ProDiag overview. The criteria analysis serves to identify and flag the first recognized faulty operand within a CPU cycle.

The functionality is available on WinCC Unified PC and Unified Comfort Panels.

Thus, with minimal engineering effort and without hampering the user program, faults and errors in the production sequence can now also be visualized automatically with WinCC Unified, and quickly localized accurately.

All the known objects and functions for the process diagnosis are available in WinCC Unified:

- GRAPH overview including the first faulty operand (symbol name)
- ProDiag overview
- PLC code display including the marking of the first operand with error
- Criteria analysis control
- Output of the 1st faulty operand in the alarm, the following information can be appended to the operand: Symbol name, absolute address, value and comment
- Output of all the faulty operands, also parameterizable according to: Symbol name, absolute address, value and comment

**Simple configuring**

The error messages are automatically derived from the information stored in the project, for example, station name (CPU), function type such as valve (block name) and instance, like Valve 993 (instance name).

The user can vary their choice and sequence freely. This is generally needed only once. Subsequently, the system then adopts the created alarm structure for all the subsequent monitoring actions Since the information under question is available in the configured foreign language, no additional effort is required for a multilingual diagnostics.

Configuration of the diagnostic objects takes place on the HMI side. This is limited to simple drag&amp;drop of the desired object with a mouse from the toolbox view in TIA Portal into the screen, and adaptation of its size.

**Synchronization of all HMI devices**

One aspect that is very important for test runs and commissioning is that the diagnostic-related changes or extensions in ProDiag do not hinder operation. The HMI devices are synchronized by the controller automatically and can thus remain in Runtime mode, so that there is no unnecessary wait time for repeated loading procedures.

**High flexibility**

WinCC Unified has the option of querying all the ProDiag information via scripting, for example, to organize an automatic operator guidance in the event of a fault.

**System functions**

Automated operation procedures such as, for example, jumping from the GRAPH overview to the PLC code display are now available in WinCC Unified to the full extent.

**ProDiag overview**

The object "ProDiag overview" provides a summary of all the monitoring of a ProDiag monitoring module. It can serve as a proxy of a technological component of a plant.

See also "[Process diagnostics](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#process-diagnostics-rt-unified)".

#### User administration

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### System function "ShowLogonDialog"

A pop-up window with the logon dialog "User Login" is displayed in Runtime via the "ShowLoginDialog" system function. A new user can register with Runtime.

See also [Configuring the display of the login dialog](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#configuring-the-display-of-the-login-dialog-rt-unified).

##### Deactivation after failed login attempts

In the Runtime settings, you can specify whether and after how many failed login attempts a user account is blocked.

See also [Specifying local or central user management](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#specifying-local-or-central-user-management-rt-unified).

##### Login via RFID

If local user administration is used, WinCC Unified supports login with RFID. Note that login via RFID always only affects the device on which the card is read.

- Unified PC**:**

  The prerequisite is that PM-LOGON is installed on the Runtime PC and the teach-in of the RFID cards with PM-LOGON has been completed. You can find additional information on licensing, the installation of PM-LOGON and teach-in for the RFID cards in the [Link to PM-LOGON user help](https://support.industry.siemens.com/cs/de/en/view/109810587).
- Unified Comfort Panel**:**

  The prerequisite is that the teach-in of the RFID cards in the Control Panel has been completed. Additional information on using RFID on Unified Control Panels is available in the operating instructions [Unified Control Panels](https://support.industry.siemens.com/cs/ww/en/view/109810754) TIA V18 or higher.

See also [Local user management](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#local-user-management-rt-unified).

#### Connectivity

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### OPC UA

The importing of XML files with OPC UA server alarm instances enables the offline check of alarms and events. Node ID and condition type ID can be added and edited manually.

See also [Integrating OPC UA server alarm instances into a Unified client](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#integrating-opc-ua-server-alarm-instances-into-a-unified-client-rt-unified)

HMI tags with an OPC UA connection support addresses with a length of up to 256 characters.

##### S7 plus PLC

System tags for reading or setting the operational state of S7plus PLCs can be used for dynamization in screens or in scripts.

- `@ConnectionName_PLC_OpState` reads the state of the PLC.
- `@ConnectionName_PLC_OpStateCtrl` sets the state of the PLC.

The tags are available from version 18.0.0.2 onwards. If the version of a device is changed to an older version, the tags are no longer available.

If the connection is removed or the connection type is changed, the tags are removed.

The functionality replaces the system functions "SetPlcMode" and "GetPlcMode".

See also [Reading and setting the operating state of an S7-1200/1500](Communication%20with%20SIMATIC%20PLCs%20%28RT%20Unified%29.md#reading-and-setting-the-operating-state-of-an-s7-12001500-rt-unified)

The system function "SetPLCDateTime" facilitates time synchronization of one or all S7plus-PLCs with the connected HMI device.

See also [SetPLCDateTime](Using%20system%20functions%20%28RT%20Unified%29.md#setplcdatetime)

New system functions for the jog mode enable the synchronization of the tag values between HMI and PLC before and after a write operation.

#### Options

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### Audit

The Audit option has new functions to help you better ensure that your project conforms to GMP.

- Electronic signature: All audit-relevant user actions can be confirmed by the electronic signatures of up to two users.  
  See also [Configuring the electronic signature](WinCC%20Audit%20%28RT%20Unified%29.md#configuring-the-electronic-signature-rt-unified)
- Audit Viewer: The "Audit Viewer" object expands the possibilities for visualizing and editing audit-relevant data in runtime.   
  See also [Audit Viewer](WinCC%20Audit%20%28RT%20Unified%29.md#audit-viewer-rt-unified)

| License | Description |
| --- | --- |
| WinCC Unified Audit Basis | Secured communication  Logging the Audit Trail  Recording of process data changes (automatically, via script or system function)  Confirmation with/without comment  Exporting Audit Trail entries  Audit Trail report and tamper indication  Logging in and logging out Audit Trail entries  Simple electronic signature   Backing up and restoring Audit Trail database segments  Direct display and analysis of the Audit Trail in the Audit Viewer |
| WinCC Unified Audit Enhanced | In addition to the functionalities contained in WinCC Unified Audit Basis:   Multiple electronic signature (2 persons) |

##### Parameter set control

Using the system function "ExecuteToolbarButton" makes it possible to access the buttons of the toolbar from outside the parameter set control. That in turn makes it possible to create a user-defined control for the functions of the parameter set control.

See also [ExecuteToolbarButton (parameter set control)](Using%20system%20functions%20%28RT%20Unified%29.md#executetoolbarbutton-parameter-set-control-rt-unified)

Flexible limit values can be configured by linking a tag with the property "Minimum value" or "Maximum value" of a parameter set type element.

See also ["Parameter set types" editor](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#parameter-set-types-editor-rt-unified)

A text list or a graphics list can be transferred to a parameter set type element as a resource list for counting. An element can be selected and saved for the parameter set from the transferred list.

See also Assign a resource list to a parameter set item

##### PI options

**Improvements for PFI and Calendar**

- Improved operation and depiction of the "Performance Gantt chart" control
- Improved operation and depiction of the "Dashboard Element" control
- Support of layer plans in PFI Controls
- Improved function in case of shifting of schedules
- The top 10 and top 5 downtimes for machine states, cause groups and causes can be output in the Excel report.
- Changes to PFI coefficients and actions in Calendar Control are logged in the Audit Trail and displayed in the Audit Viewer.

**Improvements for LCS &amp; SES**

- Existing recipes can be duplicated to configure new recipes faster.
- By creating LCS data logs, production data can be stored.
- Expansion of the "SES - Sequence Execution System" library by two function blocks for equipment modules and units with extended quantity structure:

  - EquipmentModuleXLarge
  - UnitXLarge

#### Unified PC Runtime

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

##### Kiosk mode

You have the option to run clients of a Unified PC in Kiosk mode. Clients running in Kiosk mode are restricted in their operations. The following applies to these clients:

- Runtime can only be displayed in Kiosk mode.
- Runtime only has access to configured folders.

  Depending on the Kiosk settings, these folders may be located on an external drive.
- In addition, depending on the Kiosk settings, the following restrictions may apply:

  - The use of Windows key combinations is not possible in Runtime.

    Runtime can only be quit by restarting the device.

    Or  
    The use of Windows key combinations is not possible in Runtime, except Alt+F4 for quitting Runtime.
  - Quitting Runtime must be authorized by inputting a PIN.

To configure which client devices run in Kiosk mode and which Kiosk settings they have, use the My WinCC Unified application. Operation of My WinCC Unified is tied to function rights. Configuration takes place at Runtime. My WinCC Unified is available:

- On the Kiosk clients and the Unified PC: As a stand-alone application
- In the Web clients of the Unified PC: As a Web application

Kiosk devices must be Windows PCs with SIMATIC WinCC Unified Install Center installation. The Unified PC must also have a SIMATIC WinCC Unified Install Center installation.

See also section Settings for kiosk.

##### Client-specific start screens

You have the option to define client-specific start screens for the client devices of a Unified PC at runtime. If a client-specific start screen has been defined, all the users who log in to the client device during Runtime of the Unified PC see the same start screen.

You can configure for each client device which start screen is displayed and whether the entire screen or a section of the screen is displayed. For configuring, use the My WinCC Unified application. Operation of My WinCC Unified is tied to function rights. Configuration takes place at Runtime. My WinCC Unified is available:

- In the Web clients of the Unified PC: As a Web application
- On a Windows PC with SIMATIC WinCC Unified Install Center installation: As a stand-alone application

See also section Start screen settings.

##### Automatic login to Runtime

You have the option to activate the automatic login to Runtime client devices of a Unified PC at Runtime.

If automatic login has been activated for a client device and the client connects to the Runtime of the Unified PC, the client logs in to Runtime automatically as a default user. Entry of the user name and password is not required. The default user does not have any function rights. If you switch to another user and then log out for that user, the default user is logged in again.

Use My WinCC Unified to configure the automatic login. Operation of My WinCC Unified is tied to function rights. Configuration takes place at Runtime. My WinCC Unified is available:

- In the Web clients of the Unified PC: As a Web application
- On a Windows PC with SIMATIC WinCC Unified Install Center installation: As a component of SIMATIC WinCC Unified Control Center, via the Windows tray

See also section Settings for kiosk.

##### Automatic logout

Unified PCs support automatic logout from Runtime. When configured accordingly, a user who has been inactive in Runtime for too long is automatically logged off from Runtime. The login page is displayed.

In the following cases, the default user is automatically logged in to Runtime after the logout.

- Local client: Automatic login or login via RFID is enabled.
- Web client: If the "Show start screen without login" option was activated for the client device in My WinCC Unified.

The default user does not have any function rights.

If using a local user administration, for each user, configure whether automatic logout is active for the user as well as the length of time the user may be inactive before he or she is automatically logged out.

If using a central user administration, configure for each user the length of time the user may be inactive before they are automatically logged out. It is not possible to disable the automatic logout only for selected users.

In SIMATIC Runtime Manager, you have the option to completely disable or re-enable the automatic logout in Runtime. By default, automatic logout is disabled.

Behavior for Panels

- Web clients that access a Unified Panel do not support automatic logout.
- When Runtime is displayed on the Panel, Runtime supports automatic logout. You can disable automatic logout in the user settings.

  This behavior has not changed.

See also section [Configuring security settings](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#configuring-security-settings-rt-unified).

##### GraphQL

**New operations**

The GraphQL API was expanded with the following operation:

| Operation | Description |
| --- | --- |
| loggedAlarms | Name of the logged alarms. |
| acknowledgeAlarms | Acknowledges active alarms. |
| resetAlarms | Resets alarms. |
| enableAlarms | Enables alarms. |
| disableAlarms | Disables alarms. |
| shelveAlarms | Resets alarms. |
| unshelveAlarms | Cancels the resetting of alarms. |
| reduState | Subscribes to the redundancy status of the host connected with the GraphQL client in a redundant system. |

**Access control**

The access of GraphQL clients to Runtime can be restricted as follows:

- Linking access to function rights

  An operation of the GraphQL client is only executed if the user who is logged on at the client has the required rights.

  Reading rights are required for querying and subscriptions, and writing rights for mutations.
- Controlling access at the object level

  Read access and write access of the user logged on at the GraphQL client is defined per object:

  - Read access to an object without authorization: The object is removed from the server response.
  - Write access to an object without authorization: The operation is aborted.

**Subscription of tags during the delta download**

If a GraphQL client subscribes to two tags and their tag names are renamed in a delta download such that the tags swap their names, the subscription is now executed further.

See also section [Introduction](WinCC%20Unified%20GraphQL%20%28RT%20Unified%29.md#introduction-rt-unified).

##### Trend control

You can add new trends to the trend view in Runtime by drag&amp;drop. To do so, drag an IO field that is connected to a tag through a numeric data type, from the screen to a trend area of the trend view.

The trend is visible up to the next screen change or till the screen is re-loaded.

See also section [Add new trend](Operating%20Unified%20PC%20%28RT%20Unified%29.md#add-new-trend-rt-unified).

### Hardware configuration

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### Uniform user and rights management for S7-1500 CPUs

With TIA Portal V19, the new CPU FW versions have a uniform and improved way of managing [users and their roles](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#settings-for-users-and-roles-s7-1500) and CPU function rights. The new function rights relate to the PG/HMI communication (engineering accesses), web server and OPC UA. The existing local user configuration for the web server and OPC UA server is integrated into the new user management.

#### PLC Security Logging for S7-1500 CPUs

The newly integrated [Syslog functionality](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#syslog-s7-1500) in the CPUs enables better tracking and monitoring of critical CPU changes and operations. In the event of security-relevant events, such as user logins, configuration changes or operating state changes, messages are generated in a separate message memory of the PCU. The configurable forwarding to external Syslog / SIEM systems enables integration into existing security monitoring systems.

#### Support of PROFINET Security Class 1 functions

As of STEP 7 (TIA Portal) version V18, you have already been able to activate/deactivate SNMP in the hardware configuration and define the community names. The SNMP is disabled by default.

As of V19, IO devices and I-devices also support these SNMP settings and the basic setting (SNMP disabled). To determine whether an IO device supports this configuration option, refer to the respective Equipment Manuals. In addition, you can configure DCP write protection and read-only access for SNMP for the current CPUs as IO controllers as well as for IO devices and I-devices.

It is also possible to benefit from the improved integration protection for GSD files by importing GSDX files (containers for GSD files), e.g. in the commissioning phase.

#### Configuring shared IO devices and I-devices in a common project

As of STEP 7 (TIA Portal) version V18, you have already been able to configure IO devices as shared IO devices in a common project. The restriction to GSD-based IO devices will no longer apply as of V19: You can insert and configure the devices directly from the hardware catalog. Furthermore, you can configure I-devices together with assigned IO controllers in a common project.

**Advantages**:

- Reduction in the possible error sources: The complete consistency is examined by STEP 7 in a project.
- Less configuration effort: A common STEP 7 project contains all devices.
- Improved diagnostics: Complete diagnostics in one project.

#### SIMATIC S7-1500R/H-CPUs

New functions as of firmware version V3.1 (note that the associated firmware version will be supplied together with an HSP following start of delivery of TIA Portal V19.):

- Support of OPC UA server

  The redundant system S7-1500R/H supports data exchange as an OPC UA server according to the redundancy concept of the OPC UA specification.

  You can find an overview of the OPC UA server in the Communication Function Manual.
- OPC UA server instructions

  The S7-1500R/H redundant system supports the instructions "OPC_UA_ServerMethodPre" and "OPC_UA_ServerMethodPost" as of instruction version V1.1.

  You can find the related details here: [Product information on documentation S7-1500/ET 200MP, S7-1500R/H](https://support.industry.siemens.com/cs/ww/en/view/68052815)
- Support for central CP modules and system power supplies

  To expand Ethernet communications interfaces, the communications processor CP 1543-1 can now also be used in the redundant S7-1500R/H system. The redundant design of the CPs (per R/H CPU) increases the availability of the redundant system for communication tasks. Use of the active backplane bus for S7-1500H enables the CP 1543-1 to be removed and inserted in "RUN-Redundant" system state without causing any reaction.

  The option to use system power supplies (PS) in the redundant S7-1500R/H system is also added.
- Support of IE/PB LINK HA

  The IE/PB LINK HA connects PROFINET IO and PROFIBUS DP as a gateway. This way, the IE/PB-LINK HA enables access to all DP devices connected to the underlying PROFIBUS network. In the redundant S7-1500R/H system, the IE/PB-LINK HA is integrated into the PROFINET ring as an S2 device, allowing seamless connection of PROFIBUS nodes in case of switchover.
- Access using Web API

  The redundant system S7-1500R/H supports the Web Server API. The CPU offers you a web-based API (Web API) as an interface for reading and writing CPU data. You can find an overview of the mechanisms and methods that support the R/H CPUs in the Web server Function Manual.
- Extension of OB83 start events

  The OB 83 (pull/plug OB) is available in the redundant S7-1500R/H system with additional start events.

Support of additional system functions as of firmware version V3.1 (note that the associated firmware version will be supplied together with an HSP following start of delivery of TIA Portal V19.):

- Data logging

  The S7-1500R/H redundant system supports the data logging instructions. With data logging, you save process values from the user program in a file, the data log. The data logs are saved on the SIMATIC Memory Card in csv format and stored in the "DataLogs" directory.
- "Random" instruction

  The "Random" instruction is supported. With the instruction, you generate a 32-bit random number.
- Editing user files

  The S7-1500R/H redundant system supports the instructions for editing user files: FileReadC, FileWriteC, FileDelete
- Extension of the existing "RH_CTRL" instruction.

  The "RH_CTRL" instruction is extended to include two modes for controlling the operating state and for running through the "SYNCUP" system state.
- Support of Long Term Trace

  The "Long Term Trace" function for long-term recording of signal trends is also available for the redundant S7-1500R/H CPUs.
- Secure Open User Communication

  Open User Communication (OUC) can also be performed in a secure form (Secure OUC) in the S7-1500R/H redundant system.

### SIMATIC Visualization Architect

The SIMATIC Visualization Architect (SiVArc) enables easy, fast and flexible automated creation of HMI content based on the STEP 7 user program.

#### What's new in V19

The following functions are newly available with SIMATIC Visualization Architect V19:

**Rule editor: "Advanced Tag Rule Editor"**

- The new rule editor offers full control for the generation of HMI tags, e.g. generation of multiplex tags.

**Support of additional screen objects for WinCC Unified**

- PLC code view
- Graph overview
- Screen windows

**Improvement of SiVArc expressions**

- The expression "FolderPath" now provides better results when using S7 units.
- The expression Block.Parameters("Name") can now also read the value of PLC user constants.
- The "Split" function now also works with strings in addition to individual characters.
- Evaluations based on the key words True and False are no longer case-sensitive. The comparison value is interpreted, e.g.  
   when "false", "False", or 0 = False, the result would be correct

**Other properties that can be changed by SiVArc:**

- "Mode" property for the symbolic IO field.
- Logging tags are supported for the trend control.

**Improvement of the Property configurator:**

- The resource type can be selected for the symbolic IO field.
- Improved handling of alarms.

**Improvement of the generation of multilingual texts:**

- SiVArc now generates the languages based on the project languages. As a result, regeneration is no longer necessary after adding another Runtime language to a device.

**Improvement of usability**

- Cut &amp; Paste is supported in the rule editors.
- The SiVArc expression at the interface or event of a Unified faceplate is retained even after the interface or event is renamed.
- Entries for the rules in a rule group can be specified in the row of the rule group. This reduces maintenance effort.
- Deleted objects are listed by name in the log file.

### SINAMICS Startdrive

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### SINAMICS Startdrive Basic

- Integration of the new drives SINAMICS S200, S210 (as of FW V6.1) and G220.

  - Security functions, such as UMAC.
  - User-defined lists
  - Online firmware update
  - Backup and Restore function
  - Basic positioner (EPOS) with physical units (for SINAMICS S200)
- Project-integrated Shared Device functionality for SINAMICS S120, S210, and G220.
- Extensions for SINAMICS CU3x0-2-based drives.

  - New display format in the device view with multiple lines.
  - Support for distributed SINAMICS S120M modules.
  - Support for additional Z options for specific motor series.
- Extensions for Openness

  - Configuring encoders for SINAMICS CU3x0-2-based drives.
  - Support of the new drives SINAMICS S200, S210 (as of FW V6.1) and G220.

  Support for high-resolution screen settings.

#### SINAMICS Startdrive Advanced

- Long-term trace for CU3x0-2-based drives
- Extension of Safety Integrated acceptance test

  - Support of SINAMICS S200, S210 (as of FW V6.1) and G220
- Measuring functions

  - Support of SINAMICS S200, S210 (as of FW V6.1) and G220

#### SINAMICS Drive Control Chart (DCC)

- Uploading charts that were loaded into the drive using STARTER (including complex charts).
- Support for high-resolution screen settings.
- Statistics overview of charts
- Jump of DCC parameters in the parameter list to the reference location in the chart.
- Publishing pins in the subchart
- Extensions for Openness

  - Improved functionality in the chart layout of the block
  - Additional block information available

### SINUMERIK

All important new features of SINUMERIK can be found in the section "What's new in V19" under "Configuring and programming SINUMERIK".

The availability of the SINUMERIK STEP 7 Toolbox V19 is scheduled for 02/2024.

### SIMOTION

#### SIMOTION SCOUT TIA

- Communication

  - Optimizations in OPC - environment
- Simulation

  - Support of the TControl technology package in SIMOSIM

### System functions

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### Information system in the browser

The information system of the TIA Portal can now optionally also be displayed in your default Windows browser.

In V19, we offer a first look at a browser-based information system with a modern design and improved navigation options. To manage favorites or display information in different tabs, for example, you can use the familiar functions of your default browser.

In subsequent versions of TIA Portal, we will continue to improve the browser-based information system.

Information on calling the information system in the browser and on current limitations can be found here: [Introduction to the information system in the web browser](Introduction%20to%20the%20TIA%20Portal.md#introduction-to-the-information-system-in-the-web-browser)

#### User Management &amp; Access Control (UMAC)

- New function right "View users and roles" for the "Users and roles" editor:

  In addition to the existing function right for managing users and roles, there is a new function right for explicit displaying of users and roles. This enables the configuration of user roles as follows:

  - The editor is not opened.
  - Editor is opened write-protected.
  - The editor can be edited.
- Safety-relevant function rights are marked.
- Login dialog remembers the user type:

  When logging in or switching users, the last used user type (e.g. Global user) is preselected.

#### SIMATIC TIA CAx

With V19, TIA Portal supports the exchange of AutomationML files according to version 1.4 of the Application Recommendation Automation Project Configuration (AR APC).

For communications objects (interfaces, ports, nodes and subnets), it is now possible to exchange available Openness attributes via the so-called custom attributes in AutomationML.

The exchangeable attributes can be determined for modules that are described using MDD or GSDML and made available for partner systems such as ECAD systems. The CAx Publication Tools allow you to easily determine the exchangeable Openness attributes and save them in various file formats for further processing by partner tools.

#### SIMATIC TIA Portal Add-Ins

V19 provides the following improvements in the area of Add-Ins:

- An additional authorization for Add-Ins (Full Trust) has been introduced, which allows an Add-In to be run with all rights of the user. This enables use, for example, of interop assemblies through an Add-In that has this authorization.
- The provided TIA Portal Add-In Development Tools for Microsoft Visual Studio 2019 and 2022 and Visual Studio Code allows the Full Trust authorization to be set for a new Add-In and a justification for why this authorization is needed to be entered for the user.
- A company administrator can now declare Add-Ins as trustworthy so that they can be used without additional activation by the users of them.

  See also: [Basics of Add-Ins](Introduction%20to%20the%20TIA%20Portal.md#basics-of-add-ins)

#### TIA Portal Version Control Interface

The functionality of the Version Control Interface of the TIA Portal has been extended in V19 to include the following:

- A project can be connected to an existing workspace in one step. This reduces the number of manual steps that were previously necessary.
- Languages that are used in a SimaticML file but not defined as project languages can be automatically activated as additional project languages during import. This functionality is available on both the UI and the Openness interface.
- The Openness interface now provides a more efficient method for initial calculation of the comparison status between an object in the project and the associated file in the workspace.
- The order of import in V19 is independent of dependencies between objects. This eliminates the need to import files in multiple steps in some cases.

  See also: [TIA Portal Version Control Interface basics](Using%20TIA%20Portal%20Version%20Control%20Interface.md#tia-portal-version-control-interface-basics)

### Engineering options

#### TIA Portal Test Suite Advanced

General:

- You can now use the Test Suite in the context of Multiuser Engineering. Changes to style guide, application test or system test objects are now marked in the local multiuser session in the project tree. They are transferred to the project server at the next check-in.

Application test:

- In addition to PLCSIM Advanced V6.0, the S7-1500 Software Controller family as well as the Open Controller family from FW V30.0 are now supported.
- Significantly shortened test execution due to the new "ExternallyManagedPLCSIMInstance" user mode. In this mode, the instance of PLCSIM Advanced is not set up by Test Suite. Instead, the user sets up the instance once himself. The application test connects to the prepared instance and runs the selected tests. This means that a separate instance of PLCSIM does not have to be set up and prepared for each individual test case.
- Assert commands can optionally be extended with comments and accompanying values.

System test:

- In addition to the standard SIMATIC and the user-defined OPC UA interface that you set up in TIA Portal, the system test now also supports companion specifications created with SiOME.
- The duration of the test has been significantly reduced, especially due to the extensive OPC UA Server interface.
- System test cases can now also be saved as a copy template in a library.

#### SIMATIC Target™ for Simulink®

The following functions are newly available with SIMATIC Target V6.0 SP1:

- Restrictions on the use of software units:

  - Support of namespaces: The generated blocks automatically use the namespace specification of the target software unit.
  - Retention of the "Published" property: The "Published" block property in the TIA Portal is retained even when regenerating the program blocks.
- Improvements in automatic downloading to the controller
- Improved stability of External Mode communication
- Support of SIMATIC ODK 1500S V2.5 SP4 (including Windows 11 support)

The Service Pack 1 for SIMATIC Target V6.0 is provided free of charge.

#### TIA Portal Cloud Connector

The TIA Portal Cloud Connector enables remote access to the TIA Portal engineering environment (e.g. TIA Portal Cloud, private cloud, or RDP), to the local PG/PC interfaces and the connected SIMATIC hardware.

- What's new as of TIA Portal Cloud Connector V1.2 SP3

  - Multi-device registration: A user device can be registered for multiple remote devices simultaneously. This allows multiple TIA Portal Cloud users to access SIMATIC hardware through the same Cloud Connector.
- What's new as of TIA Portal Cloud Connector V1.2 SP4

  - The default settings of the protocols have been changed to enhance security.

#### TIA Portal Teamcenter Gateway

With "TIA Portal Teamcenter Gateway", you can store and manage TIA Portal projects, global libraries, program blocks, and PLC data types (UDTs) in Teamcenter. The operation is integrated into the TIA Portal.

- What's new as of TIA Portal Teamcenter Gateway V19

  - Support of Active Workspace Client (AWC) V6.2.

    With the Active Workspace Client (AWC), you can access (mainly read-only) Teamcenter data. This client runs in a web browser and does not require installation of the Teamcenter Rich Application Client (RAC).

    The Active Workspace Client (AWC) can also be configured and extended without installation.
- The Active Workspace Client (AWC) V6.2 supports the following functions:

  - Display of TIA Portal projects and global libraries along with their associated properties.
  - Link between TIA Portal objects and Teamcenter artifacts. For example, motor artifacts can be linked with a motor program block.
  - Opening a TIA Portal Automation Engineering project/library from the Active Workspace client.
  - Quickly and easily track, navigate, and adapt machine control programs in the TIA Portal from Active Workspace Client (AWC).
- Compatibility

  - Teamcenter versions 13.2/13.3/14.1/14.2/V14.3(*) are supported.

    (*) – Support for TC V14.3 in TIA Portal is in progress for V19.

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic / Advanced V19 is the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V19.

- Project Integrated shared devices and I-devices for the F-CPU:

  With TIA Portal V19, you can configure Project Integrated shared devices and I-devices for the F-CPU in a single project. This allows you to configure stations and PN interfaces in a centralized location.
- Unique identification of the F-CPU through a serial number.

  Enables the unique identification of an F-CPU through its serial number to ensure that the correct safety program is loaded onto the right F-CPU.
- Openness enhancements

  The available Openness functionalities have also been extended with STEP 7 Safety V19:

  - The following modules have been expanded for attribute access with Openness:

    **ET 200pro:**

    6ES7148-4FA00-0AB0

    6ES7148-4FS00-0AB0

    6ES7148-4FC00-0AB0

    **ET 200eco** PN:

    6ES7146-6FF00-0AB0

    6ES7148-3FA00-0XB0

    **ET 200MP:**

    6ES7526-1BH00-0AB0

    6ES7526-2BF00-0AB0
  - F-Download via Openness on SD card

#### Central user management via UMC

The configuration limits for operating UMC in larger infrastructures have been expanded. UMC can now synchronize in a network with up to 300 runtime servers per ring server.

The expansion of the configuration limits provides the advantage of greater flexibility in designing the UMC infrastructure, such as operating a UMC server per production cell.

#### TIA Portal Multiuser Engineering &amp; TIA Project Server

The following functions are newly available with Multiuser Engineering V19.

- Newly supported object types in a local session:

  - TIA Portal Test Suite:

    Rules
  - WinCC Unified:

    WinCC Unified screens, HMI alarms and HMI tags
- New "Exclusive Multiuser mode":

  - The new Exclusive Multiuser mode allows quick changes to objects that cannot be edited in a local session, such as device configuration changes.
  - The Exclusive Multiuser mode is started from the local session without closing the local session.

    All changes in the local session are retained and available in the exclusive local session.
  - A quick switch to the exclusive local session requires that the local session is based on the current project state.
- Significant reduction in the runtime for transferring changes from an exclusive local session to the TIA Project Server.

#### S7-PLCSIM and S7-PLCSIM Advanced

S7-PLCSIM Standard TIA Portal V19:

- New design of the user interface for S7-PLCSIM Standard, which also allows the use of S7-PLCSIM Advanced functions. (A license for S7-PLCSIM Advanced is required.)
- Improved workspace concept
- Graphical support of the TCP/IP multiadapter mode of the S7-PLCSIM Advanced
- Simulation of STEP 7 programs is now also possible for Software Controllers as of version V30.0.
- Support of the latest firmware versions in S7-1200 and S7-1500
- All new PLC order numbers for TIA Portal V19/FW V3.1 are supported, including RAIL and SIPLUS variants

New in S7-PLCSIM Advanced V6.0:

- Simulation of Software/Open Controllers (SWCs)

  - Possible as of SWC V30.0 with TIA Portal V18
  - Includes SWC V30.1 in TIA Portal V19
  - Includes existing ODK functionality from V3.0
- All new PLC order numbers for TIA Portal V19/FW V3.1 are supported, including RAIL and SIPLUS variants
- In S7-PLCSIM Advanced, TIA Portal projects from versions V14 to V19 as well as CPU firmware versions V1.8–V3.1 are now supported
- Improved applicability of the network configuration at the API

### Runtime options

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### OPC UA

The data types "[GUID](Configuring%20automation%20systems.md#using-additional-opc-ua-data-types-for-companion-specifications-s7-1500-s7-1500t)" and "DynamicArrays" (see Readme file) used primarily in Companion Specifications are additionally supported by the OPC UA server of S7-1500 and ET 200 CPUs.

### TIA Portal Openness

#### TIA Portal Openness

The following new functions and innovations are available in TIA Portal Openness V19. For more details on the various topics, refer to the corresponding sections of the product documentation.

**General**

- Import of every supported SimaticML version, regardless of the API version used.
- More flexible SimaticML import with options to handle project languages.

**Projects**

- Configuring the use of S7-1500 blocks in virtual PLCs.

**Hardware configuration**

- Creating, reading, modifying and deleting transfer areas for direct PLC-PLC data exchange.
- Managing the "PLC System Logging" configuration.
- Managing the new PLC access level configuration for CPU firmware 3.1 (UMAC and protection levels).
- Changing the standard language for OPC UA alarms &amp; events in PLC multilingualism.
- Mass change of the hardware parameters in the correct sequence in all overloaded "SetAttributes" methods.

**Hardware modules**

- New supported modules for parameter access: ET200pro Safety, ET200eco PN Safety, ET200MP Safety.
- Expanded parameter access for SCALANCE XC-200 (as of V4.3), XP-200 (as of V4.3), SC-600 (as of V2.3).

**CAx data exchange**

- Import/export of CAx data via AutomationML and return of the results via API instead of a log file.
- Support of additional attributes for the exchange of hardware configuration.

**Online scenarios**

- Reading out the accessible online devices for download or upload.
- Downloading a PLC including Safety to a SIMATIC memory card folder.
- Handling the UMAC user management data for the download.
- Providing the UMAC access data for the authentication of online access to a PLC.

**PLC user programs**

- Read and write access to additional columns in data blocks.
- Informative attribute on blocks to support virtual PLCs.
- Extension of the SimaticML schema to support the usage of Named Value Types.
- Named Value constants are supported during block import/export.

**WinCC Unified**

- Access to additional object properties and runtime settings.
- Import and export of JavaScript functions and JavaScript types

**Interrupts and ProDiag**

- Managing system diagnostics in the PLC configuration.

**Safety Engineering**

- Configuring the serial numbers for unique identification of an F-PLC in the "Safety Administration Editor".

**UMAC**

- Configuring the alias name for project users.

**Technology objects**

- Support of groups for technology objects.
- File import and export for Interpreter programs.

**Startdrive**

- Connecting a technology object with a Startdrive telegram.
- Reading the hardware ID of a Startdrive telegram.
- Support of new Startdrive devices.
- Parameter assignment of external encoders.

**Test Suite Advanced**

- Configuring OPC UA settings for system tests.
- Configuring the mode for application tests.
- Support of master copies.

**Version Control Interface (VCI)**

- VCI setting to handle non-active project languages during SimaticML import.
- Initializing the VCI object status to the mapped file.

**Web server**

- Managing data access for the web server in the CPU firmware 3.1.

## What's new in TIA Portal V18

This section contains information on the following topics:

- [TIA Portal](#tia-portal-1)
- [SIMATIC STEP 7](#simatic-step-7-1)
- [SIMATIC WinCC](#simatic-wincc-1)
- [Hardware configuration](#hardware-configuration-1)
- [SINAMICS Startdrive](#sinamics-startdrive-1)
- [SINUMERIK](#sinumerik-1)
- [SIMOTION](#simotion-1)
- [System functions](#system-functions-1)
- [Engineering options](#engineering-options-1)
- [Runtime options](#runtime-options-1)

### TIA Portal

#### Discover the highlights of V18

TIA Portal V18 provides several new functions. You can find an overview of and detailed information about the new functions in this contribution:

[https://support.industry.siemens.com/cs/ww/en/view/109807106](https://support.industry.siemens.com/cs/ww/en/view/109807106)

### SIMATIC STEP 7

All important new features of STEP 7 are summarized here. You can find more details on the various topics in the product documentation sections.

#### Namespaces

Within software units you have the option of using namespaces to structure the program.

Namespaces offer the following advantages, for example:

- Program elements can have the same name if they are located in different namespaces.
- Clear representation of elements in the project tree
- Clear representation of operands in the program code

See also: [Categorizing program elements in namespaces](Using%20software%20units%20%28S7-1500%29.md#categorizing-program-elements-in-namespaces-s7-1500)

#### Safety programs in software units

You can create Safety programs in software units and process or load them independently of other program sections. You can also use namespaces in Safety programs.

#### Symbolic access during runtime (S7-1500)

The "Symbolic access during runtime" function gives external applications access to the tags in the PLC program during runtime. External applications can be, for example, HMI applications, OPC UA functions or other communication functions. The tags can be read or written.

Read or write access is not programmed statically when the program is being created. In fact, access takes place dynamically during runtime. Users enter the symbolic tag names they wish to access manually or program-controlled during runtime.

See also: [Symbolic access during runtime](LAD%20%28S7-1200%2C%20S7-1500%29.md#symbolic-access-during-runtime-s7-1500)

#### Icon for in/out parameters (LAD, FBD, GRAPH)

For easier visual distinction between input parameters (IN) and in/out parameters (InOut), the in/out parameters are identified with their own symbol in the program code:

![Icon for in/out parameters (LAD, FBD, GRAPH)](images/154277850379_DV_resource.Stream@PNG-de-DE.png)

#### Checksum "Program code" (LAD, FBD, STL, SCL)

The new checksum "Program code" is available for comparing project data. It determines whether the source code of two blocks is identical. Spaces, line breaks, tabs and comments of all types are not included in the comparison.

> **Note**
>
> **Online/offline differences after upgrading to V18**
>
> After upgrading a project to V18, the checksum "Program code" shows an online/offline difference as long as the program has not been loaded to the device with V18.

See also: [Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)

#### References to technology objects

You can declare references to technology objects of the "Motion" and "SIMATIC Ident" categories and use them in value assignments. It is also possible to assign DB_ANY to the reference of one of these technology objects.

This will simplify the handling of technology objects in PLC programs. Thus, for example, you can process different axis types iteratively in program loops.

See also: [Example: Editing different axis types iteratively in a program loop](References%20%28S7-1500%29.md#example-editing-different-axis-types-iteratively-in-a-program-loop-s7-1500)

#### Find and replace

The "Find and replace" function was extended:

- Hidden block parameters can be searched and replaced in LADs and FBDs.
- The "Replace All" function and its relevant options are supported in PLC tag tables and PLC constant tables.

#### Watch table

The menu command "Modify selection now" simplifies controlling several selected tags.

See also: [Introduction to modifying tags](Testing%20with%20the%20watch%20table.md#introduction-to-modifying-tags)

#### Importing libraries from SIMATIC AX

With AX Code, SIMATIC AX provides a development environment for developing, compiling and testing PLC programs in a text-based and object-oriented manner. AX Code is based on Visual Studio Code and offers all the advantages of modern IT programming. Structured Text (ST) is available as a programming language.

Libraries created with SIMATIC AX can be integrated in STEP 7.

See also: [Overview of SIMATIC AX](Import%20SIMATIC%20AX%20libraries%20into%20TIA%20Portal.md#overview-of-simatic-ax)

#### Trace

- Traces

  The number of signals to be recorded in the respective trace is increased from 16 to 64.

  This results in significantly expanded options when comparing the signals of a single record.
- Long-term trace

  Now it is possible for all S7-1500 CPUs to record a trace, in addition to the already available trace and project trace, that is not recorded in the device but on the hard disk of the computer on which the TIA Portal project is open. This results in significantly better diagnostic possibilities when analyzing the course of signals over a long period of time, which in principle is only limited by the storage capacity of the hard disk.
- Fast-Fourier-Transform (FFT)

  In addition to the possibilities of the Bode diagram, the user now also has an FFT analysis available.

#### S7-1500 and S7-1500T Motion Control

You can find an overview of the new features in technology version V7.0 in the S7-1500/S7-1500T Motion Control Overview, in section [New features V7.0](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#new-features-v70-s7-1500-s7-1500t).

#### PID

The PID auxiliary functions have been extended by the RampSoak instruction with which you can realize a time-dependent profile.

#### Instructions

- The existing "GetStationInfo" instruction has been extended as follows: You can now also read out address information of an R1 device.
- The existing "RH_CTRL" instruction has been extended as follows: You can now also query whether the "SYNCUP" system state is currently locked.
- The existing "OPC_UA_ReadList" instruction has been extended as follows: You can now also access the OPC UA address space of the local CPU. This enables you, for example, to read out diagnostic information via the local OPC UA server and react to this in the user program.
- The existing "OPC_UA_WriteList" instruction has been extended as follows: In addition to the DataValue, you can now also set the "SourceTimestamp" and the StatusCode of the OPC UA nodes of your user-defined server interface. It is now possible to transmit the time of the last value change via OPC UA.

#### Online and Diagnostics view

The connection diagnostics in the Online and Diagnostics view has been extended as follows: You can now also display the connection properties of the interface modules of an IO device in the S7-1500H system.

### SIMATIC WinCC

Here you will find a summary of the important innovations in WinCC. You can find more details on the various topics in the product documentation sections. The innovations are divided into the following topics:

- WinCC Unified: Simulation
- WinCC Unified: Efficient configuration of screens
- WinCC Unified: System diagnostics control
- WinCC Unified: Faceplates
- WinCC Unified: Tags
- WinCC Unified: Alarms
- WinCC Unified: Parameter sets
- WinCC Unified: System functions
- WinCC Unified: Scripting
- WinCC Unified: Library
- WinCC Unified: OPC UA
- WinCC Unified: GraphQL
- WinCC Unified: Logon via RFID
- WinCC Unified Collaboration
- WinCC Unified: Reporting
- WinCC Unified: Audit
- WinCC Unified: Process diagnostics
- WinCC Unified: Unified Comfort Panel
- WinCC Unified: Performance Insight
- WinCC Unified: Calendar
- WinCC Unified: Line coordination
- WinCC Unified: Sequence
- WinCC Unified: SIMATIC Energy Suite
- WinCC Unified: TIA Portal Openness
- WinCC Professional
- SiVArc

#### Simulation of runtime

To use the simulation, you must install WinCC Unified Runtime. If no license is found for runtime, start the simulation in demo mode.

#### Efficient configuration of screens

**Harmonization of the names of object properties**

The names of the object properties have been harmonized. Related properties are also displayed one below the other in all languages when sorted alphabetically in the TIA Portal.

Example:

- Line - Width
- Line - Color
- Line - Type

**Favorites for object properties**

You can define your own favorite properties for each screen object. Some properties are defined as favorites by the system.

You can find the overview of the system-defined and user-defined favorites under "Options &gt; Settings &gt; Visualization &gt; Favorites screens (WinCC Unified)" in the "Favorites properties" table.

You can locate the individual properties of an object by using the "Filter" function in the Inspector window.

See also ["Favorites" function](Configuring%20screens%20%28RT%20Unified%29.md#favorites-function-rt-unified).

**Central color management**

You can centrally change the colors used in a project in the "Change object color" dialog.

The "Change object color" dialog box contains a hierarchical overview of all color-relevant object properties. In the display, you can navigate within the display and operating objects that are shown. You will receive an overview of all colors in use. You specify a color selection and replace it with other colors.

See also [Central color management](Configuring%20screens%20%28RT%20Unified%29.md#central-color-management-rt-unified).

**Automatic scrolling**

When you drag and drop the object to one of the corners of the screen, automatic scrolling is triggered. You can place the object in other areas of the screen.

See also [Moving objects in the screen](Configuring%20screens%20%28RT%20Unified%29.md#moving-objects-in-the-screen-rt-unified)

**Grouped objects**

When you join two or more objects with the "Group" function, the objects form a group. You can manage a group in the engineering system and in runtime like a single object, e.g. change the color of all grouped objects with one step.

Grouping is available on the Unified PC and on the Unified Control Panel as of version V18.

See also [Using groups](Configuring%20screens%20%28RT%20Unified%29.md#using-groups-rt-unified).

**Direct text input**

You can change the label of the "Text box" and "Button" objects directly via the keyboard.

See also [Enter text directly into the object](Configuring%20screens%20%28RT%20Unified%29.md#enter-text-directly-into-the-object-rt-unified).

**Select multiple objects**

To edit several objects at once, select all the objects in question. This procedure is called "multiple selection". The Inspector window shows all the properties of the selected objects.

See also [Select multiple objects](Configuring%20screens%20%28RT%20Unified%29.md#select-multiple-objects-rt-unified).

**Overlapping ranges during dynamization with tags**

When dynamizing an object property with tags of "Range" type, the values in the individual ranges may overlap. Cells where range overlaps occur are highlighted in color. The overlaps are reported as a warning when compiling the project. Downloading to the device is possible. The first highlighted value is always used in runtime.

See also [Dynamizing an object property with "Range" evaluation type](Configuring%20screens%20%28RT%20Unified%29.md#dynamizing-an-object-property-with-range-evaluation-type-rt-unified) .

**Renaming layers**

When you create a screen, the 32 layers are numbered consecutively by default. To improve clarity, you can rename the layers to suit your requirements. You change the name of a layer under runtime settings of the device.

See also [Renaming a layer](Configuring%20screens%20%28RT%20Unified%29.md#renaming-a-layer-rt-unified).

**Changing the screen resolution**

The default size of the screen is adjusted to the resolution of the device. You change the screen resolution in the runtime settings of the device.

See also [Changing the screen resolution](Configuring%20screens%20%28RT%20Unified%29.md#changing-the-screen-resolution-rt-unified).

#### System diagnostics control

The system diagnostics control supports the matrix view and the diagnostic buffer view.

With the matrix view you have the possibility to check the status of your PLCs and their lower-level hardware components. All hardware components are displayed as tiles. You can configure the display as well as the content of the tiles.

Using the diagnostic buffer view, you can display diagnostic events of the currently selected PLC.

#### Screen window - Extension of the multitouch function

The multitouch function in screen windows has been extended. You have the possibility to scale a screen window and move the contents.

To scale the content, drag two fingers apart or slide them together.

Drag vertically or horizontally with a finger to move the contents.

#### Faceplates

**Support for additional screen objects**

You can use the "alarm control" and "trend control" objects in faceplates. You insert the controls via the "Tools" task card.

**Using faceplate in faceplate**

You can use faceplate types in other faceplate types. In this way, you have the possibility to put several faceplate types together and thus increase the reusability. When using nested user data types at the faceplate interface, data are automatically passed to the underlying faceplates.

**Dynamic SVGs available in faceplates**

Dynamic SVGs created in the project library can be used in faceplates via drag-and-drop.

**"Events" interface**

Interface events allow you to define events and associated parameters in a faceplate type. System functions of the function list and scripts to the events configured at the instances. Various data types are available for the parameters associated with an interface event.

**Extension of the "Properties" interface**

The following changes were made to the property interface:

- "Graphic" interface property You can associate properties that correspond to a graphic with the "Graphic" data type. You link graphics in the "Visualization" tab, for example, with the "Graphic view" and "Switch" screen objects. In the faceplate instance, you can assign graphics from the project's collection of graphics or released type versions of the "Graphic" type from the project library.
- "Multilingual text" interface property You define different texts in different faceplate instances. In the instance, you assign static texts, resource lists, tags or scripts for this purpose.

**Extension of the "Tags" interface**

The following changes were made to the tag interface:

- "ARRAY" data type: You can define interface tags of the "Array" data type in faceplates. The arrays can consist of elementary data type as well as user data types.
- "HMIUDT" data type: You can define interface tags of data type "HMIUDT" in faceplates and link them to HMI user data types in this way.
- "PLCUDT" data type: To link PLC user data types at the tags interface, use the "PLCUDT" data type.
- You can nest user data types on multiple levels in interface tags of faceplates.
- Time and date: You can connect interface tags for date and time specification with PLC user data types and HMI tags.

**Local tags**

Local tags are used to pass or buffer information within a faceplate type. In this way, you can, for example, dynamize elements of a faceplate depending on the current properties of another element. Besides elementary data types you have the possibility to define arrays.

#### Tags

The scope of an internal tag can be changed to "Local session". In a multi-user environment, session-related data is processed independently in each local session.

The use of local session tags in Unified Collaboration and in the web client is supported.

The values of the local session tags are not saved at the end of a session and are lost.

#### Alarms - system events

System events now have fixed IDs. The IDs are thus no longer dependent on the sequence of the configuration.

#### Parameter sets

You can work with parameter sets in screens independently of the parameter set control. To do this, you use, for example, IO fields that you link to local session tags. In parameter set types you assign the local session tags to the edit tags.

You use system functions to trigger the following actions with screen objects:

- Enable parameter sets for productions:

  - Save a parameter set of the PLC into a local edit tag.
  - Write a parameter set from a local edit tag to the PLC.
- Managing parameter sets:

  - Create a new parameter set with user-defined default values.
  - Saving a current parameter set.
  - Load a saved parameter set.

#### System functions - Assign parameters to the function list via drag-and-drop operation

You assign the following objects from the detail view to a parameter in the function list using drag-and-drop operation:

- HMI tag
- PLC tag
- Screen
- Text list

#### Scripting

**Visibility of layers in runtime**

Unified Runtime supports switching the visibility of layers using JavaScript functions.

1. In the engineering system, place the objects of a screen in the "Layout" task card on different layers.
2. Program a JavaScript function to change the visibility of, for example, "Layer_1" in the current screen.  
   `Screen.Layers ("Layer_0").Visible = false;`
3. Configure this function, e.g. on an event of a button.

If the event occurs in runtime, all objects placed on this layer become invisible.

To make a layer visible in the current screen, use: `Screen.Layers("Layer_0").Visible = true;`

**Changing the style in runtime**

You can query and change the style with JavaScript functions in runtime.

1. To change the style in runtime, create a JavaScript function with the following content:  
   `HMIRuntime.UI.Style = "FlatStyle_Dark";`  
   `HMIRuntime.Trace("Switched style to: " + HMIRuntime.UI.Style);`
2. Configure this function, e.g. on an event of a button.

When the event occurs in runtime, all objects are changed to the dark style. The name of the style is output via the debug output of the runtime.

**Documentation of the object model**

The documentation of the object model has been completely revised. Among other things, clickable screens enable navigation in the object model.

**New system functions and JavaScript functions**

The following functions are introduced on Unified PC and Unified Comfort Panel:

- .FileSystem.Browse
- .FileSystem.GetSpecialFolder
- .FileSystem.IsDirectory
- .ParameterSetTypes.Sysfct.CreateParameterSet
- .ParameterSetTypes.Sysfct.DeleteParameterSet
- .ParameterSetTypes.Sysfct.LoadParameterSet
- .ParameterSetTypes.Sysfct.ReadParameterSet
- .ParameterSetTypes.Sysfct.RenameParameterSet
- .ParameterSetTypes.Sysfct.SaveParameterSet
- .ParameterSetTypes.Sysfct.WriteParameterSet
- .Tags.CreateTagSubscription
- .UI.ProDiag.SysFct.OpenViewerGraphByBlock
- .UI.ProDiag.SysFct.OpenViewerGraphFromOverview
- .UI.ProDiag.SysFct.Next
- .UI.ProDiag.SysFct.Previous
- .UI.ProDiag.SysFct.ToggleGRAPHViewerMode
- .UI.ProDiag.SysFct.ToggleNetworkDisplay
- .UI.ProDiag.SysFct.ZoomIn
- .UI.ProDiag.SysFct.ZoomOut
- .UI.ProDiag.SysFct.IsJumpableAlarm
- .UI.ProDiag.OpenTIAPortalProject
- .UI.ProDiag.OpenTIAPortalGRAPHDetails
- .UI.ProDiag.OpenTIAPortalProDiagDetailsByCall
- .UI.ProDiag.OpenTIAPortalProDiagDetailsByAssignment
- .UI.ProDiag.OpenTIAPortalFromAlarm
- .UI.SysDiag.SysFct.GoToPlc
- .UI.SysFct.ChangeScreenAsync
- .UI.SysFct.ChangeScreenAsyncByNumber
- .UI.SysFct.ChangeScreenByNumber
- .UI.SysFct.OpenScreenByNumberInPopup
- .UserManagement.GetRolesFromUser
- .UserManagement.HasUserRole

#### Library

**Extension for script module types**

Script module types can be managed in the library. For example, you have the possibility to create new script module types and version them.

If you have created and enabled a script module type, you have the following options to use the script module type:

- In the "Screens" editor at events and properties of screen objects
- In the scheduler at events
- In global modules

To use a version of a script module type, the version in question must be referenced in an "Import" statement in the global definition.

Example: `import * as MyCalc from "SMT_1_V_0_0_1"`

In the example, "SMT_1" is the name of the script module type and the version number is V 0.0.1.

You also reference versions of script module types in faceplate types and other versions of script module types. Here, the lowest device version must be compatible. A type version of a script module referenced in another type must have the same or lower required device version.

**Extension of dynamic SVG graphics**

You can manage dynamic SVG graphics as types in libraries. In the "Add new type" dialog, under "Graphic", select the "Dynamic SVG graphics" option.

#### OPC UA

**Configuration of Unified OPC UA servers in TIA Portal**

For Unified PCs and Unified Comfort Panels working as OPC UA servers, TIA Portal now provides OPC UA server configuration options in the runtime settings of the HMI device.

OPC UA server configuration via the configuration file is no longer supported for Unified PCs.

#### WinCC Unified GraphQL

The WinCC Unified Openness interface, GraphQL, is a web API for read and write runtime access. A user of the GraphQL API must authenticate via UMC and requires special Unified user rights for authorization.

Functional scope:

- Read, write and subscribe to process tags
- Read and subscribe to active alarms

#### Logon via RFID

If local user management is used, WinCC Unified supports logon with RFID. Note that logon via RFID always only effects the device on which the card is read and has no influence on connected remote devices.

**Unified PC**

Requirements are that the PM-LOGON must be installed on the runtime computer and the teach-in of the RFID cards with PM-LOGON must be completed.

You can find additional information on licensing, installation of PM-LOGON and teach-in for the RFID cards in the [PM-LOGON Operating Manual](https://support.industry.siemens.com/cs/de/en/view/109810587).

**Unified Comfort Panel**

A requirement is that the teach-in of the RFID cards in the Control Panel must be completed.

You can find information on using RFID on Unified Control Panels in the operating instructions [Dynamizing an object property with "Range" evaluation type](Configuring%20screens%20%28RT%20Unified%29.md#dynamizing-an-object-property-with-range-evaluation-type-rt-unified)  TIA V18 or higher.

See also [Central user management](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#central-user-management-rt-unified).

#### Unified Collaboration

The "Parameter set control" and "Reports" screen objects can be used in screens that are displayed via Unified Collaboration in another runtime.

#### Reporting

**Settings for reporting**

Reporting can be enabled or disabled in the runtime settings of the HMI device.

When reporting is enabled, you define the storage locations for the reporting database and the main local storage location for the reports. To do this, you have the following options in each case:

Unified PC:

- "Standard": The folder selected during installation or later in WinCC Unified Configuration in the "Reporting" step is used as the storage location.
- "Project folder": The project folder of the runtime project is used as the storage location.
- "Local": The device folder entered under "Folder" is used as the storage location.

Unified Comfort Panel:

- Select the storage medium and enter the path to an existing folder on this medium under "Folder". The folder is used as storage location.

  Default folder of the reporting database: The project folder

  Default folder of the local main storage location for reports: "media/simatic/&lt;storage medium&gt;/Reports​"

**Support for text lists and graphic lists**

If standard columns and optional columns of data source items output numerical values, you can assign text lists and graphic lists to these columns. When the Runtime data is read in, the cell values of these columns are replaced by texts or graphics from the assigned lists.

**Improved alarms**

When a report job is discarded because the queue is full, an alarm is issued containing the name of the discarded job.

When a report job cannot be completely executed, an alarm is issued containing the name of this job.

#### Audit

**Configuration conforms to GMP**

"Configuration conforms to GMP" means creating projects in accordance with "Good Manufacturing Practice". The requirements are set out in FDA rules "21 CFR Part 11". The FDA is the U.S. Food and Drug Administration. Eudralex Volume 4, Appendix 1, EMA regulation 178/2002 also applies. EMA is the European Medicines Agency.

The Audit option has new functions to help you better ensure that your project conforms to GMP.

**Protection against manipulation**

The Audit Trail is protected from tampering in such a way that the tampering is detected.

**Audit Viewer**

With the configurable screen object Audit Viewer you can display the acquired data in runtime in tabular form.

- Online from an Audit Trail
- Offline from an exported audit file

**Recording user changes**

Audit now also records and documents the logon or logoff of a user.

#### Process diagnostics

The TIA Portal functionality, ProDiag (Process Diagnostics), is used to monitor and determine errors that occur in your plant or machine. You can use ProDiag to show the type of error, the cause of the error and the location of the error on the HMI device.

The following objects are available for displaying the current status of error monitoring and diagnostics in the program code:

**GRAPH overview**

The "GRAPH overview" object is used to display the current program status for executed steps of the GRAPH sequencer.

**PLC code display**

The "PLC code display" object is used to display the current program status of user programs that have been programmed in the GRAPH programming language.

#### Unified Comfort Panel

**Images for Unified Comfort Panel**

- Images can be downloaded from the [SIOS image downloads](https://support.industry.siemens.com/cs/ww/en/view/109746530).
- Images are released independent of WinCC (TIA Portal).
- Use ProSave to import an image version that does not correspond to the configured device version onto a panel.
- If a new image only contains improvements for the runtime of the device, this version is not shown in the engineering system. In this case, use the most recent device version displayed in the engineering system.

**Scaling screens and screen windows**

Unified Comfort Panels support scaling in screen and screen windows with a two-finger gesture. Scaling a screen does not affect an open popup window. Enlarged sections can be moved with a one-finger gesture.

When zooming in on a section, the detail is reduced by hiding objects or displaying them as icons.

**Alarm control**

The order of column sorting has been improved.

- If the "Priority" column is defined in the alarm view, sorting is based on alarm priority. As a result, in a single-line alarm view, only the top-priority alarm appears in the alarm window. A lower-priority alarm will not be displayed, even if it is more recent. The alarms are displayed in chronological order.
- If one of the following columns in the alarm view is configured, sorting on a Unified Comfort Panel is according to the specified order.  
  1. Priority  
  2. Modification time  
  3. Raise time  
  4. Alarm state

**Alarm statistics**

Unified Comfort Panels support the following statistical calculations on archived alarms:

- Frequency of an alarm
- Total display time of an alarm in seconds
- Average display time of an alarm in seconds

**Trend control**

In a trend control with multiple trends, a trend can be selected via the legend.

You can also use a trend control to configure the "Min Max" compression mode for Unified Comfort Panel.

**Trend companion**

Unified Comfort Panel support the trend companion object.

**Communication**

Communication via interfaces X1 and X2 can occur simultaneously.

Unified Comfort Panel can now also communicate via Modbus RTU.

**Network drive**

The "Network and Internet" function is available in the Control Panel under "Network drive". You can use this function to exchange data between the HMI device and an enabled network drive on a server PC.

You can find more information in the Control Panel help and in the operating instructions.

**Print**

For the objects "Trend control", "Function trend control", "Value table", Unified Comfort Panel supports printing via the button in the toolbar. The data to be printed is sent to the specified default printer. The last ten print jobs are saved as graphics in the directory on the Panel.

**Improved support for printers**

- Selection of the default printer from the printer list
- "CUSTOM Plus 2" has been added to the list of supported printers.

#### Performance Insight

**WinCC Unified Collaboration**
  
With WinCC Unified Collaboration, you access the Performance Controls from another HMI device. This allows operators, plant management, and maintenance personnel to access and evaluate the KPIs of other stations in the plant from their own screens.  
They can also search for WinCC Unified Collaboration partners that use PFI objects and display these KPIs.

**Cause/downtime analysis** 
  
Identify the ten most important causes of machine downtime and display the cause graphically. Configure causes and cause groups for this purpose.

**Predefined styles**
  
The performance controls support the use of predefined light and dark styles.

![Performance Insight](images/157411662731_DV_resource.Stream@PNG-de-DE.png)

**Long-term KPI evaluation and recalculation** 
  
For long-term KPI calculation, the maximum 32-day restriction on KPI calculation or recalculation has been removed. The calculation is now only limited by the available resources and data (log time period of the PFI data log). For example, the KPI calculation can go over ten years if the server has sufficient hardware support and the maximum log size is large enough.

**Storing the runtime configuration**
  
Permanent storage of control configuration in runtime.

**Dashboard control** 
  
New performance control for a simplified graphic view of KPIs in runtime.

#### Calendar

**WinCC Unified Collaboration**
  
Using WinCC Unified Collaboration, you can access the calendar control from another HMI device. This allows operators, plant management, and maintenance personnel to access and edit the shift schedules of other stations in the plant from their own screens.

**Reuse shift schedule of a scheduled week**
  
To save configuration work, the shift schedule of a scheduled week can be copied and pasted into another week.

**Info panel** 
  
The info panel is a quick view in the calendar that displays user alarms and events at a glance.

**Predefined styles**
  
The calendar control supports the use of predefined light and dark styles.

**Global calendar configuration** 
  
In the Engineering System, a global configurator for calendar settings is provided under "Common data". This enables the simultaneous configuration of all calendars within the plant view. Individual adjustments of single calendars are additionally possible at the plant object within the plant view.

**Restoring modified day instances in the template**With the restore function, it is possible to reset the customized day instances to the day template that was used to create the instance. These day instances are again automatically updated when changes are made to the day template.

#### Line coordination

**New controls - Unit status and unit control**
  
The unit status shows you the current ISA-88 status of a unit in color. An additional symbol shows whether the unit is allocated or not. The unit control shows you more detailed information of the unit. You also have the option to control the individual recipe operations and recipe unit procedures within the control.

**New status "Withdrawn from system"**
  
If a change affects the procedure or recipe, this procedure or recipe is set to the new status "Withdrawn from system". You have the option of using a button in the recipe control to set all recipes or procedures in the "Withdrawn from system" status to the "Available" status by means of a validation.

**Improved handling during recipe creation**Recipes and procedures can be filtered in the recipe control. The insertion of technical operations has been improved.

**Manage materials and use as material parameters in operation**
  
Material parameters can be created in the engineering system, used and configured in the technical operation (LCS) or in the step (SES). A target value for the material and the quantity is defined in the operation parameter and linked to the defined material in the material overview (LCS).

**Local Reporting - Automatically triggered reports**After a job has been completed, canceled, or stopped, a report is generated automatically. This configuration is done via a check box in the job history.

**Integration in Audit**Provision of evidence of the operator's activities in support of regulations and quality requirements**.** Tracking of relevant operator actions during job execution. All actions performed within the job control are logged within the WinCC Unified Audit Trail (e.g. deletion process, start/pause process, setpoint change...).

**Information box**The information box, within the LCS control, provides a quick and detailed overview of contextualized system events. The alarms are categorized into error messages, warning messages and info messages, which can also be filtered. Contextualized messages are displayed with details of the technical setup and corresponding object name.

Note the information provided in [Industry Online Support](https://support.industry.siemens.com/cs/ww/de/view/109807125).

#### Sequence

**Improved handling when creating and loading operations**The status for steps has been removed. Only operation parameters affect the status of operations. Loading operations into the PLC is now independent of the status. Loading can be done in manual mode as well as in automatic mode. If an operation is already being performed, a loading is also possible.

**Managing materials and using them as material parameters in the operation**
  
Material parameters can be created in the engineering system, used in the step (SES) and configured. A target value for the material and the quantity is defined in the operation parameter and linked to the defined material in the material overview (LCS).

**Assignment as step condition**Conditional assignment as an additional step condition based on feedback from another parameter. A parameter or control module can be assigned to another parameter or control module. Only when the condition of the assigned object is met, is the parameter or control module continued.

**Easy navigation to the active SES operation**In the job control (LCS), you have the option of double-clicking on the active recipe operation to display the SES operation in the SES Control.   
Also in the unit control (LCS), you have the option to display the active SES operation via a button in the SES Control.

**Integration in Audit**Provision of evidence of the operator's activities in support of regulations and quality requirements**.** Tracking of relevant operator actions during the execution of an SES operation. All actions performed within the SES controller are logged within the WinCC Unified Audit Trail (e.g. deletion process, start/pause process, setpoint change,...).

**Information box**The information box, within SES control, provides a quick and detailed overview of contextualized system events. The alarms are categorized into error messages, warning messages and info messages, which can also be filtered. Contextualized messages are displayed with details of the technical setup and corresponding object name.

**Storing the runtime configuration**
  
Permanent storage of control configuration in runtime.

Note the information provided in [Industry Online Support](https://support.industry.siemens.com/cs/ww/de/view/109807125).

#### SIMATIC Energy Suite

The SIMATIC Energy Suite supports with V18 WinCC Unified. The following features are supported:

- Complete visualization  
  Faceplates and screens are supplied for visualization of energy data acquisition, peak load management and base load management in WinCC Unified.
- Simplified handling  
  To reduce the configuration effort, the complete visualization for WinCC Unified can be generated with SiVArc. Using SiVArc exclusively within the SIMATIC Energy Suite requires installation, but does not require an additional license.
- Data buffering between PLC and WinCC Unified  
  If the connection between PLC and WinCC Unified is temporarily interrupted, the data on the PLC are temporarily stored in a ring buffer. As soon as communication is restored, the buffer is emptied and the data is transferred to WinCC Unified.
- No duplicate licensing  
  Tags of the Energy Suite are license-neutral in WinCC, which means they are not considered for the tag license. The tags of the Energy Suite are nevertheless still relevant for the system limits of WinCC Unified (e.g. for the Unified Comfort Panel).

In addition, the following features have been added with V18:

- Base load management  
  Continuous monitoring of a power value that should be between a low and high limit. If it is outside this range, actuators (consumers, generators, storage) are switched based on their defined priorities to bring the value back between the limits.
- Storage actuators  
  Energy storage is supported for peak and base load management.
- Software/Open Controller  
  The Energy Suite supports the software and Open Controller.
- Simplified project migration  
   The visualization of a previous version of the Energy Suite can be upgraded to the current status with little effort.

#### TIA Portal Openness

TIA Portal Openness supports the creation of all screen objects including Custom Web Controls and dynamic SVG graphics, as well as the dynamization of their properties.

TIA Portal Openness supports the dynamization of screens and screen objects via conditions for tags.

#### WinCC Professional: WinCC Channel Diagnosis

"WinCC Channel Diagnosis" is integrated into the new tool "WinCC System Diagnosis" as a new CCAx control.

Two modes are available in "WinCC System Diagnosis":

- System Diagnostics Mode (SDM)
- Channel Diagnostics Mode (CDM)

The SDM can be integrated into the standalone controller container, i.e. the system diagnostics information is available in the standalone desktop app.

Filtering and sorting mechanism allow overview. A new column visualizes the operating status of the PLC.

#### WinCC Professional: Certificate Manager

A Certificate Manager is available to centrally manage all certificates, e.g. for HTTPS connections from web clients, OPC UA and other connections.

#### WinCC Professional: Web control

Microsoft Internet Explorer is no longer supported.

The existing functionality is made available for Chrome and Edge browsers.

Supported browsers can download WebNavigator client application, updates, plugins and required installers from WebNavigator Server V18.

The new "homepage.html" with the following options is displayed:

- Download Hub WebNavigator client applications, updates, plugins and required installers can be downloaded from WebNavigator Server V18.
- Language selection If one of the supported languages is selected in the language selection, the content of "homepage.html" is displayed in the selected language.
- "homepage.html" is accessible via both HTTP and HTTPS connection.

During the basic installation of the WebNavigator client application and the installation of the Datamonitor client setup, a shortcut of WinCCViewerRT is created on the desktop.

If Microsoft Internet Explorer is used to connect to WebNavigator Server, the existing ASP web pages will be displayed.

- When starting the runtime with "CCWinCCStart.exe", the option "Disable operating system access on startup" is available.

  After installing the runtime, you can find the tool under the following path:

  %PROGRAMFILES(x86)%\Siemens\Automation\SCADA-RT_V11\WinCC\bin

#### WinCC Professional: Restricted access when starting the runtime

When starting the runtime with "CCWinCCStart.exe", the option "Disable operating system access at startup" is available.

After installing the runtime, you can find the tool under the following path:

%PROGRAMFILES(x86)%\Siemens\Automation\SCADA-RT_V11\WinCC\bin

#### WinCC Professional: WebUX

The range of functions for WebUX has been extended as follows:

- C scripts are supported.
- Local session tags are supported.
- Faceplates are supported.
- The alarm filter in the alarm control is supported.

#### SiVArc

**Improved support of Unified devices**

- Generation of screen objects trend control and function trend control
- Generation of positioning fields
- Generation of alarms
- Assignment of graphics lists or text lists to symbolic IO fields via SiVArc properties
- Copy rules support scripts

**Improved support of faceplates for Unified devices**

- Additional properties for the faceplates generated by SiVArc
- The following data types can be used in addition in the properties interface: Multilingual text, authorizations, graphics
- Support of PLC and HMI user data types in the tag interfaces
- Generation of interface events

**Rule tables**

Rule tables are used to create rules for SiVArc-supported objects. Rule tables are stored in the library in structured groups and are versionable. The rule tables include a read-only default rule table that is created from projects that were configured with previous versions and upgraded to the latest version. The names of rule tables can be used as a keyword for the "Global search".

**Improvements to the Expression Resolver**

- In the Expression Resolver, you receive the result of the expressions for all instances of the block for an S7 block.
- Autocomplete lists all parameters of an FC/FB for the expression Block.Parameters(…).

**Exporting the generation overview**

You can export the generation overview and open it in Microsoft Excel, for example.

**Additional expressions**

The "Block.DB.DisplayName" expression returns the name of the instance in quotation marks.

**Generation via TIA Portal Openness**

You can define the mode and the rule set of tag generation for the SiVArc generations triggered via TIA.

---

**See also**

[Unified Comfort Panels](https://support.industry.siemens.com/cs/ww/en/view/109810754)

### Hardware configuration

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### General

Support of password complexity rules for PLC passwords for web server and OPC UA (S7-1200/S7-1500)

**Hardware comparison**

The I/O modules are now directly included when comparing two controllers; the user can easily navigate to the parameters of the I/O modules.

**Station upload**

Station upload from a controller is now also supported for this setup of device configurations:

- SENTRON measuring devices are operated as PROFINET IO devices on a controller of the S7-1500.
- F-Panel or F-SINAMICS drives are operated as PROFINET I/O devices on an F-controller of the S7-1500.

**Who is online?**

Loading onto a controller is always assigned exclusively to one user.

If several users commissioned a controller together, the individual user could not see who was currently accessing the controller online. This may have prevented other users from loading the controller.

As of V18, information about all users is displayed in the "Load preview" dialog, making it easier to contact and coordinate.

**View of Things**

View of Things (VoT) allows the user to create HMI screens under the CPU. Once loaded onto the CPU, they are accessible as a web application via the PLC web server.

With V18, it is now possible to load the "View of Things" application to the memory card via the Card Reader Download.

#### SIMATIC S7-1500 and ET 200 CPUs

New functions with firmware V3.0 for all S7-1500 and ET 200 CPUs:

- A simple configuration option is now available for the SNMP service, see [Activating and deactivating SNMP](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#activating-and-deactivating-snmp-s7-1500). For new configurations, this is disabled by default in terms of "Security-by-Default". With automatic topology detection, there may be some functional restrictions if both nodes have SNMP disabled.
- LongTermTrace: Cycle-granular recording of up to 64 different tags in a .csv file over a long period (hours, days, etc.)

New functions with firmware V3.0 for S7-1500 and ET 200 CPUs (without R/H CPUs):

- OPC UA Server – Reading the diagnostics status of the own address space, see [Running diagnostics for OPC UA servers in the program](Configuring%20automation%20systems.md#running-diagnostics-for-opc-ua-servers-in-the-program-s7-1200-s7-1500-s7-1500t).

  The own namespace of the OPC UA server can be accessed by using the OPC UA instruction for reading ("OPC_UA_ReadList"). This makes it possible to read out the status of the own OPC UA server as well as the connections of OPC UA clients, the session as well as the subscriptions and to react to them in the user program. This way, e.g. connection problems can be quickly detected and the plant availability can be increased.
- OPC UA server – Time stamping of the source time of nodes, see [Client accesses and local accesses to the OPC UA server](Configuring%20automation%20systems.md#client-accesses-and-local-accesses-to-the-opc-ua-server-s7-1500-s7-1500t).

  By using the OPC UA instruction for writing ("OPC_UA_WriteList"), it is possible to change both the "SourceTimestamp" and the status code of an OPC UA tag (node). This makes it possible to distinguish between the "Source" and "Server" time as of V18.
- OPC UA server - Increased configuration limits

  The possible number of nodes in the server interface has been increased to 15,000 for small PLCs and to 30,000 for medium PLCs. The maximum possible number of subscriptions per session has also been increased to 50. And the recommendation for monitored values for subscription was increased to max. 4,000 (at a 1s sampling and transmission rate).
- The web server certificate for HTTPS communication can now also be managed via the OPC UA GDS mechanism without separate download of the hardware configuration, see [Certificate management via Global Discovery Server (GDS)](Configuring%20automation%20systems.md#certificate-management-via-global-discovery-server-gds-s7-1500-s7-1500t).
- New functions for general file handling and especially log file handling via WEB API (as support for workflow automation)

  - Backup and restore (Backup &amp; Restore, including Failsafe)
  - Files on the memory card (user files, recipes, data logs)
- Web API read time of day (read system time, read time settings)
- Improved verification of HMI accesses (see Verified external access).

New functions with firmware V3.0 for all fail-safe CPUs:

- F-consistent Fast Commissioning Download (as of FW 3.0)

  - Together with TIA Portal V18, Consistent Commissioning Download (Consistent Compile) is now available to the user in addition to the "Fast Commissioning Download" (Fast Compile) introduced with V17.
  - This enables the user with activated Fast Commissioning to perform a consistent compile and download of the fail-safe user program to the F-CPU in RUN.
  - In addition, the Consistent Compile in TIA Portal extends the possible customizations of the user program (e.g. adding timer blocks etc.) in Fast Commissioning Mode.
  - This offers greater flexibility during commissioning or when adapting the safety program, while at the same time reducing commissioning time.
  - Finally, the F-CPU is transferred to activated safety mode by a Stop-RUN transition.

New functions with firmware V3.0 for S7-1500R/H CPUs:

- Support of PROFINET system redundancy R1 (connection of redundant interface modules) for S7-1500H
- Various network topologies (line, open ring, ring, etc.) are supported on S7-1500H
- New H-Sync module for distances up to 40 km between H-CPUs
- Support of functions for block handling CREATE_DB/DELETE_DB and READ_DBL/WRIT_DBL

New hardware and configuration limits

- Innovated S7-1500 / ET 200SP CPUs

  - 8 standard and fail-safe S7-1500 CPUs 1511(F)-1 PN, 1513(F)-1 PN, 1515(F)-2 PN and 1516(F)-3 PN/DP
  - 4 technology S7-1500 CPUs 1511T(F)-1 PN and 1515T(F)
  - 2 redundant S7-1500 CPUs 1513R-1 PN and 1515R-2 PN
  - 4 standard and fail-safe ET 200SP CPUs 1510SP(F)-1 PN and 1512SP(F)-1 PN
  - 100% more program memory and up to 100% more data memory
  - Performance increase up to factor 5 depending on CPU and STEP 7 project
  - Two performance classes

    Low: CPU 1510SP(F)-1 PN to CPU 1513(F)-1 PN

    Middle: CPU 1514SP(F)-2 PN to CPU 1516(F)-3 PN/DP
  - Higher communication performance (2nd Core)
  - The display is integrated in the R-CPUs
  - Completely revised display implementation =&gt; no separate FW necessary
- 4 new ET 200SP CPUs 1514SP-2 PN, 1514SP F-2 PN, 1514SP T-2 PN and 1514SP TF-2 PN

  - Memory concept, performance, configuration limits and features of a SIMATIC S7-1500 CPU 1515 (F) - 2 PN CPU
  - 2 PROFINET IO interfaces
- Harmonization of the technical specifications within the performance classes

#### SIMATIC S7-1200

New functions with firmware V4.6:

- Increased work memory for S7-1200 Compact CPUs:

  - CPU 1211C is now 75 KB in size.
  - CPU 1212C is now 100 KB in size.
  - CPU 1214C is now 150 KB in size.
  - CPU 1215C is now 200 KB in size.
  - CPU 1217C is now 250 KB in size.
- Increased work memory for S7-1200 Fail Safe Compact CPUs:

  - CPU 1212FC is now 150 KB in size.
  - CPU 1214FC is now 200 KB in size.
  - CPU 1215FC is now 250 KB in size.
- SNMP is disabled by default, see [Activating and deactivating SNMP](Functional%20description%20of%20S7-1200%20CPUs%20%28S7-1200%29.md#activating-and-deactivating-snmp-s7-1200).

#### PROFINET System Redundancy R1 for S7-1500H and ET 200SP

With the introduction of firmware version V3.0 for CPU 1517H-3 PN and CPU 1518HF-4 PN, it is now possible to operate redundant PROFINET interface modules (PROFINET system redundancy R1). This allows the use of redundant PROFINET networks on the fieldbus level at the same time.

Both options result in higher availability, since the failure of an interface module or the malfunction of a network no longer results in the loss of process data.

With the introduction of the IM155-6PN R1, the ET 200SP I/O family now also supports redundant interface modules that can be operated on an S7-1500H controller.

In the course of this, the ET 200SP system rail is also introduced to the market. This has been developed for the IM155-6PN R1 to significantly improve the mechanical and EMC boundary conditions.

The new LC-LD BusAdapters for single-mode fiber-optic cables up to max. 20 km complete the portfolio of BusAdapters.

### SINAMICS Startdrive

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### SINAMICS Startdrive Basic

- Extensions for CU3x0-2 based drives

  - Linear motor support
  - Fast Fourier Transform (FFT) for displaying measurements in the frequency domain
- Support of linear axes in BasicPosControl
- Extensions for SINAMICS TEC

  - Pre-installation for selected SINAMICS TEC packages  
    VIBX  
    SERVCOUP
  - Parameter help and interrupt help for SINAMICS TEC in Startdrive online help
- Extensions for Openness

  - Create and specify third-party motors (rotary) for CU3x0-2-based drive devices
  - Support of SINAMICS TEC  
    Install, activate, deactivate, delete  
    Read version via Openness
- Extensions for UMAC

  - Changed function right: Edit drive applications

    A user with this function right can edit the configuration of drives with Startdrive. All safety settings are excluded.
  - New function right: Edit Safety Integrated application of the drive

    A user with this function right can edit the safety configuration of drives and carry out safety acceptance tests.
  - New function right: Control the drive in manual mode

    A user with this function right may activate master control over the drive through the project, and then carry out targeted drive optimizations.

#### SINAMICS Startdrive Advanced

Extension of safety acceptance test

- Support of SINAMICS G130, G150, S150
- Improvement of usability during safety acceptance test
- Multiuser support for safety acceptance testing

#### SINAMICS DCC

- Upload of DCC plans loaded into the drive with STARTER (simple DCC plans)
- Extensions for Openness

  - Plan creation via Openness
  - Adding, deleting and interconnecting blocks
  - Publishing block I/Os

### SINUMERIK

All important new features of SINUMERIK can be found in the section "What's new in V18" under "Configuring and programming SINUMERIK".

The availability of the SINUMERIK STEP 7 Toolbox V18 is scheduled for 02/2023.

### SIMOTION

#### SIMOTION SCOUT TIA

- Security

  - Firmware integrity check during startup
- Download

  - Optimizations regarding download in RUN after changes
- Communication

  - Support for daylight saving time with OPC UA
- Diagnostics

  - Recording of global tags from libraries in Trace

- Simulation

  - Support of the TControl technology package in SIMOSIM

- Web server

  - Creation of a user-defined password policy

- Usability

  - Post-installation of technology packages
  - Optimization for the online consistency display
  - Direct copying of programs between SCOUT TIA and SCOUT Classic
  - Handling of Version Control improved
  - Selective closing of windows

### System functions

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### User Management &amp; Access Control (UMAC)

V18 contains the following improvements for TIA Portal user management:

- TIA Portal projects can be used more easily in different UM domains.

  If a TIA Portal project is transferred from one UM domain to another, the configured users and user groups can be synchronized to the new UM domain. Users and user groups from the old UM domain are transferred to the new UM domain. Users and user groups that do not exist in the new UM domain are disabled in the TIA Portal project.
- TIA Portal user name

  The logged-on user can now also be alternatively used for a protected project at the locations where the user name can be freely selected from the TIA Portal settings.

See also: [Basics of global users and user groups](Managing%20users%20and%20roles.md#basics-of-global-users-and-user-groups)

#### SIMATIC TIA CAx

With V18, TIA Portal supports the exchange of AutomationML files according to version 1.3 of the Application Recommendation Automation Project Configuration (AR APC).

This enables the import and export of IO-Link devices in TIA Portal in conjunction with the Port Configuration Tool.

For channels and modules, the exchange of available Openness attributes is now possible via AutomationML using the so-called custom attributes in AutomationML. The exchangeable attributes can be determined for modules that are described using MDD or GSDML and made available for partner systems such as ECAD systems.

#### SIMATIC TIA Portal Add-Ins

V18 provides the following improvements in the area of Add-Ins:

- In V18, additional types of workflow Add-Ins are offered, which allow specific functionalities of TIA Portal to be extended with user-specific operations.
- Simplified creation and debugging of Add-Ins is possible using the provided TIA Portal Add-In Development Tools for Microsoft Visual Studio 2019 and 2022 and Visual Studio Code. In doing so, the Add-In programmer is offered templates for the existing Add-In types.

  The current versions of the add-Ins for Microsoft Visual Studio 2019/2022 and Visual Studio Code are also available from Siemens Industry Online Support.
- Additional options are available to Add-In programmers to display messages of their Add-Ins directly in TIA Portal.
- A mass rollout mechanism can be used for distributing Add-Ins in the company. For this, a service is used that allows administrators to centrally administer the Add-Ins on the computers under their management.

See also: [Basics of Add-Ins](Introduction%20to%20the%20TIA%20Portal.md#basics-of-add-ins)

#### TIA Portal Version Control Interface

The functionality of the Version Control Interface of the TIA Portal has been extended in V18 by the following points:

- The structure of the workspace can be automatically derived from the structure of the project. For this, the interface for connecting the Add-Ins to a version management program has been extended to automatically track the structure of the workspace in the version management program.
- New files are listed in the workspace in a separate view of the unassigned files and can be transferred to the project in a single step.
- The sources of STL blocks can now also be exported and imported in text format.
- Export and import of technology objects is supported.
- Metadata such as timestamps are removed when exporting in SimaticML format. In addition, metadata, if any, is ignored when calculating the comparison status in the Version Control Interface.
- The language for the object names in the workspace can be set separately and is now independent of the TIA Portal user interface language used.

See also: [TIA Portal Version Control Interface basics](Using%20TIA%20Portal%20Version%20Control%20Interface.md#tia-portal-version-control-interface-basics)

#### TIA Portal Openness

The following new functions and innovations are available in TIA Portal Openness V18. For more details on the various topics, refer to the corresponding sections of the product documentation.

- General

  - Configurable error handling for "SetAttributes" for HWCN objects. The following classes are supported: Device, DeviceItem, HardwareObject, PlcAccessLevelProvider, Address, Channel, StructuredData, NetworkInterface, IoConnector, IoSystem, IoController, Node, Subnet, MrpDomain, SyncDomain, TransferArea, NetworkPort.
  - Provision of the supported data types at the "EngineeringAttributeInfo" class
  - License checks in Openness workflows with "LicenseNotFoundException"
- Security

  - Access to the automated certificate management configuration of the S7-1500 CPU
  - Configuring password policies:
- PLC user programs

  - Expansion of PLC block fingerprints with "ProgramCode" (code without comments)
  - Support of "NamespacePreset" for software units and "Namespace" for PLC blocks
  - Updating the PLC program to the latest instruction versions
  - Reading the cross-reference information of objects (XREF)
  - Configuration of the SimaticML export scope regarding "DocumentInfo" for PLC blocks, PLC tags, PLC user constants, PLC tag tables, PLC data types and technology objects, force table and watch tables
- Safety Engineering

  - Creating, configuring and deleting Safety Runtime Groups (RTG)
  - Management TIA Portal settings "Generate default fail-safe program" and "Manage fail-safe in Software Units environment"
  - Read access to the Safety property of PLC tags
  - Managing the Safety Software Unit
  - Generating the global F-IO status block
- Libraries

  - Detailed comparison of libraries or even individual copy templates, types and versions
  - Setting the update property on individual types in a global library
- CAx data export and import

  - Importing/exporting IO-Link data configured via PCT
  - Importing/exporting Siemens hardware parameters and channel properties
- Hardware configuration

  - Read access to the TIA Portal hardware catalog
  - Device replacement
  - Setting hardware parameters without prior type conversion of values as "String"
  - Mass change of the hardware parameters in the correct sequence via "SetAttributes"
  - New supported modules for parameter access (without Safety and communication modules): ET200pro, ET200MP, ET200eco PN, Push Buttons, HMI Extension Units
  - New service "SimpleWebserverUserManagement" for managing web server users and their rights for ET200SP SIWAREX modules
  - Read access to the transfer areas for cross-PLC synchronous operation
- Station Upload

  - Station upload of a S7-1200/1500 CPU via CM/CP with IP routing or DNAT routing possible (only via TIA Portal Openness)
- Version Control Interface (VCI)

  - Configuration of workspace language is possible
  - Synchronization status for child objects
- UMAC / UMC

  - Check that the UMAC copy of the UMC data is consistent with the UMC server data
  - Synchronizing the UMAC copy of the UMC data with the UMC server
- Teamcenter Gateway

  - Data record lock of the Teamcenter Gateway
  - Connecting and disconnecting with Teamcenter
  - Searching and downloading projects and libraries from Teamcenter
  - Saving a project / library in Teamcenter
- SiVArc

  - Support of the new folders and tables for the generation rules
  - New generation options for all rules, Energy Suite and user-created rules
- Interrupts and ProDiag

  - Support of PLC alarm text lists
- WinCC Unified

  - Importing and exporting tag tables
  - Support for all screen objects, including custom web controls and dynamic SVGs
  - Creating and editing groups in the project tree for screens and tag tables
- Test Suite Advanced

  - Importing and performing system tests
- Startdrive

  - Creating and specifying third-party motors (rotary) for CU3x0-2-based drive devices
  - Support of SINAMICS Technology Extensions (SINAMICS TEC): Installing, activating, deactivating, deleting, reading version
- Sinamics DCC

  - Plan creation
  - Adding, deleting and interconnecting blocks
  - Publishing block I/Os
- Continuous Function Chart (CFC)

  - XML export of the plans (all or selective)
  - XML import of plans

#### Libraries

- Library management as editor

  As of version V18 of TIA Portal, it is possible to use the library management as a stand-alone editor.

  The improved usability allows users to use the library management in parallel with the project editors. There is no need to switch between library view and project view.
- Comparison of global libraries

  With V18 of TIA Portal, the user has the option of comparing global libraries with each other or with the project library.

  Library types and master copies are considered for the comparison. The user also has the option to perform synchronization between the libraries.
- Multiuser engineering and global libraries

  As of version V18 of the TIA Portal, it is possible to store global libraries on the project server and to edit them together in a team.

  The same multiuser workflows are available for working with global libraries as for projects.

#### Security logging

It is possible to have log messages written to the Windows EventLog for security-relevant events. Events include, for example, user logons to the TIA Portal, changes to the user management in the project or critical PLC changes up to the point of download.

#### Software and licensing management

The functions for license management and the connection to Online Software Delivery (OSD) that were previously integrated in the TIA Administrator are no longer available. However, these can still be used via the Automation License Manager.

### Engineering options

#### Multiuser Engineering &amp; project server

- Grouped storage structures for projects

  As of TIA Portal V18, it is possible to store projects in groups on the project server. To do this, the project server offers the possibility to create groups.

  TIA Portal projects can be assigned to these groups. Group names, for example, can reflect projects, plants, jobs.
- Extended access authorizations

  Extended project access protection is available with TIA Portal V18. This makes it possible to configure access to projects and project groups for individual users or groups.

  Users of TIA Portal version V17 and earlier also benefit from the extended project protection. Access protection in this case is limited to the top-level project repository.

  As of V18, the project server is available for download via the SIOS entry "[Download project server](https://support.industry.siemens.com/cs/ww/en/view/109810588)". New project server functions are made available independently of the TIA Portal release.
- Global libraries

  As of version V18 of the TIA Portal, it is possible to store global libraries on the project server and to edit them together in a team.  
  The same multi-user workflows are available for working with global libraries as for projects.

#### Central user management via UMC

- Microsoft Active Directory connection

  Multiple "trusted" AD domains can now be connected.
- Extended configuration with the TIA Administrator

  - Secure communication incl. certificate export can now also be configured for the use of the SIMATIC Logon protocol.
  - Remote authentication for Unified devices can now be configured.

#### TIA Portal Cloud Connector

The TIA Portal Cloud Connector makes it possible to access the local PG/PC interface and the SIMATIC hardware connected to it from a TIA Portal Engineering in a cloud environment.

- What's new in TIA Portal Cloud Connector V1.2 SP1?

  - New protocol: "TIA Portal Cloud Endpoint" to access SIMATIC hardware with TIA Portal Cloud.
- What's new in TIA Portal Cloud Connector V1.2 SP2?

  - Increased performance for downloading to a PLC.

#### SIMATIC Energy Suite

The SIMATIC Energy Suite supports the following features with V18 WinCC Unified:

- Complete visualization

  Faceplates and screens are supplied for the visualization of energy data acquisition, peak load management and base load management in WinCC Unified.
- Simplified handling

  To save configuration effort, the complete visualization for WinCC Unified can be generated with SiVArc. Using SiVArc exclusively within the SIMATIC Energy Suite requires installation, but does not require an additional license.
- Data buffering between PLC and WinCC Unified

  If the connection between PLC and WinCC Unified is temporarily interrupted, the data on the PLC is temporarily stored in a ring buffer. As soon as communication is restored, the buffer is emptied and the data is transferred to WinCC Unified.
- No double licensing

  Tags of the Energy Suite are license-neutral in WinCC, which means they are not considered for the tag license. The tags of the Energy Suite are nevertheless still relevant for the system limits of WinCC Unified (e.g. for the Unified Comfort Panel).

In addition, the following features have been added with V18:

- Base load management

  Continuous monitoring of a power value that should be between a low and high limit. If it is outside this range, actuators (consumers, generators, storage) are switched based on their defined priorities to bring the value back between the limits.
- Storage actuators

  Energy storage is supported for peak and base load management.
- Software/Open Controller

  The Energy Suite supports the software and Open Controller.
- Simplified project migration

  The visualization of a previous version of the Energy Suite can be upgraded to the current status with little effort.

#### PLCSIM and S7 PLCSIM Advanced

PLCSIM TIA Portal V18:

- Introduction of a new user interface for PLCSIM, which also allows the use of PLCSIM Advanced functions.
- Support of the latest firmware versions in S7-1200 and S7-1500

New in S7 PLCSIM Advanced V5.0:

- In PLCSIM Advanced, TIA Portal projects from versions V14 to V18 as well as CPU firmware versions V1.8 - V3.0 are now supported.
- The API now also supports reading and writing of the STRING data type.
- All interfaces of a CPU can now optionally be made visible on the network, via API or Control Panel. This allows communication to be established between PLC instances / TIA Portal in cloud application scenarios.
- The new S7-1514 SP /T/TF CPUs are now supported.
- The new S7-1514 SP /T/TF CPUs are now supported.
- The new S7-1514 SP /T/TF CPUs are now supported.
- The R1/S2 configuration of the IO devices of an S7-1500 R/H is now supported.
- The R1/S2 configuration of the IO devices of an S7-1500 R/H is now supported.
- NTP time synchronization is now supported.
- Testing of the backup and restore functions possible via the S7-1500 Web server.
- Data logs and recipes can be read and written.

#### TIA Portal Test Suite Advanced

Style guide:

- An additional property with a specific condition can now be added for a style guide rule. The rule is then only evaluated if the additional condition is met. The following conditions are available:

  - Tag type
  - Data type
  - Block type

  With the help of these conditions, the application of a style guide rule can be restricted, for example, to a specific data type (Boolean, Integer, etc.) or tag type (Multi-instance, Array, Struct, etc.).
- In the object selector, the application of style guide rules can now also be restricted to organization blocks, functions or function blocks.
- The "Prefix/Suffix" and "Name contains" rule types can now optionally be made case-sensitive.

Application test:

- Tags of WChar, String and WString data type can now also be used in the application test.
- Application test - RUN with condition:  
  The RUN command can be used with an optional parameter for conditional execution of the test case. Once the optional parameter reaches the value specified by the user or the maximum number of cycles is reached, the execution is terminated.  
  Syntax: RUN( Cycles := &lt;value&gt;, &lt;optional_parameter&gt; = &lt;value&gt;);

System test:

This type of test is newly available as of Test Suite V18. The system test allows the user to define and execute test cases for a PLC program using OPC UA server interfaces. The system test enables the execution of the following tests:

- Hardware-in-the-loop tests with S7-1200 and S7-1500
- Software-in-the-loop tests with PLCSIM Advanced.

#### TIA Portal Teamcenter Gateway

- Support for Teamcenter Gateway operation in Exclusive Engineering

  Teamcenter Gateway supports operations such as connect, save, open, search etc. in the TIA Portal Exclusive Engineering environment.  
  With Exclusive Engineering, you can conveniently work on your project as a "single user" on the project server.   
  Functionality for Exclusive Engineering on the project server to work with Teamcenter Gateway.
- Openness API for Teamcenter Gateway workflows

  As of V18, there is an interface for Openness API of Teamcenter Gateway Workflows for integrating TIA Portal into your development environment and the automation of your tasks in the engineering workflow. Write your own applications with external development environments, for example to push &amp; pull your engineering projects from TIA Portal into Teamcenter to manage projects and libraries in TIA Portal as a whole in Teamcenter - for consistent versions and consistent release workflows. Refer to the TIA Portal Openness Manual for details.
- Updating modified linked TIA proxy objects in Teamcenter

  As of V18, TIA Portal objects (FBs, FCs and PLC data types) can be exported as

  proxy objects to Teamcenter and linked to Teamcenter artifacts. As of V19, it is possible to update changed linked TIA Portal objects (FBs, FCs and PLC data types) in existing stored relevant artifacts in Teamcenter.
- Compatibility

  Teamcenter versions V13.1/13.2/13.3/14(*) are supported.

  (*) – Support for TC V14 in TIA Portal is in progress for V18.

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic / Advanced V18, the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V18.

- Consistent Fast Commissioning Download (as of FW 3.0)

  With TIA Portal V18, Consistent Commissioning Download (Consistent Compile) is now available to the user in addition to the Fast Commissioning Download (Fast Compile) introduced with V17.

  This enables the user with activated Fast Commissioning to perform a consistent compile and download of the fail-safe user program to the F-CPU in RUN.

  In addition, the Consistent Compile extends the possible modifications to the fail-safe user program (e.g. adding timer blocks) in Fast Commissioning mode.

  This provides greater flexibility during commissioning or when modifying the safety program and reduces commissioning time.

  Finally, the F-CPU is transferred to activated safety mode by a Stop-RUN transition.
- Openness enhancements

  The available Openness functionalities have also been extended with STEP 7 Safety V18:

  - Configuration of F-runtime group in the Safety Administration Editor (SAE)

    Creation and deletion of F-runtime groups  
    Modification of the F-runtime group iDB  
    Modification of the pre-processing and post-processing of the F-runtime group
  - Generation of the global F-I/O status block
  - Download of the project data (including safety-related project data) into a PG/PC
- Fail-safe unit

  In future, users can decide whether the safety program is to be created in the familiar sequence structure or in a fail-safe unit.

### Runtime options

All important new features are summarized here. You can find more details on the various topics in the product documentation sections.

#### OPC UA

You can find new functions in the OPC UA context under "New functions with firmware V3.0 for all S7-1500 and ET 200 CPUs (without R/H CPUs)" in section [Hardware configuration](#hardware-configuration-1).

## What's new in TIA Portal V17

This section contains information on the following topics:

- [SIMATIC STEP 7](#simatic-step-7-2)
- [SIMATIC WinCC](#simatic-wincc-2)
- [Hardware configuration](#hardware-configuration-2)
- [SINAMICS Startdrive](#sinamics-startdrive-2)
- [System functions](#system-functions-2)
- [Engineering options](#engineering-options-2)
- [Runtime options](#runtime-options-2)
- [Installing language packs](#installing-language-packs)

### SIMATIC STEP 7

All important new features of STEP 7 are summarized here. You can find more details on the various topics in the product documentation chapters.

#### CEM programming language (S7-1200/S7-1500)

CEM (Cause-Effect-Matrix) offers you a new, easily understandable programming language with which you can program cause-effect relationships quickly and easily.

> **Note**
>
> **Video tutorial on CEM**
>
> [Automate efficient engineering with Cause Effect Matrix (CEM) in less than 10 minutes](https://youtu.be/FaR9rVXUkJo)

#### Downloading groups and group structures (S7-1200/S7-1500)

Existing groups and group structures are downloaded to the CPU during "Download to device".

The groups and group structures can be downloaded from the following system folders in the project tree. The same applies to the system folders listed below software units.

- Program blocks
- PLC data types
- PLC tags (only CPU S7-1500 firmware version &gt;= V2.5 and higher)

This means the group structure is restored when downloading the CPU as a new station or when uploading from a device.

See also: [Introduction to downloading blocks](Compiling%20and%20downloading%20PLC%20programs.md#introduction-to-downloading-blocks-s7-1200-s7-1500)

#### Editors for programming languages

- A cross-reference list in the Inspector window now allows for freezing the current cross-reference view as well as showing higher-level access for structure tags (STRUCT, PLC data type).
- The display of overlapping input or output addresses in the cross-reference editor has been improved.
- The "Open block" (F7) dialog now also allows for the partial search of names. This means you no longer have to enter the initial letters to search for blocks and PLC data types (UDT).
- For blocks, PLC data types (UDT) and PLC tag tables within software units, the "Published" property is now displayed directly in the project tree.
- For local Find &amp; Replace, the total number of replacements is displayed.
- In many STEP 7 editors, the selected text can be copied directly to the search box of the local search with &lt;Ctrl + F&gt;. A second &lt;Ctrl + F&gt; copies the search text to the global search.
- To make the code easier to read, there will be an automatic line break for tag names in LAD, FBD, GRAPH and CEM blocks using the camelCase syntax.
- Keyboard operation to insert frequently used instructions has been simplified:

  | LAD instruction | Old keyboard operation | New keyboard operation |
  | --- | --- | --- |
  | Empty box | &lt;Shift+F5&gt; | &lt;F8&gt; |
  | Normally open contact | &lt;Shift+F2&gt; | &lt;F9&gt; |
  | Normally closed contact | &lt;Shift+F3&gt; | &lt;F10&gt; |

  | FBD instruction | Old keyboard operation | New keyboard operation |
  | --- | --- | --- |
  | Empty box | &lt;Shift+F5&gt; | &lt;F8&gt; |
  | AND logic operation | &lt;Shift+F2&gt; | &lt;F9&gt; |
  | OR logic operation | &lt;Shift+F3&gt; | &lt;F10&gt; |

#### Loading and monitoring changed data blocks (S7-1200/S7-1500)

The following rule has been in effect when loading blocks:

If the block in the offline project had a newer interface time stamp than in the online project, the block always had to be reloaded. As a result, the tag values were always reinitialized. Inconsistencies in the running plant operation could result.

Starting with V17, the time stamps are no longer compared, the structure of the online and offline blocks is compared instead. Data blocks are only reinitialized when downloaded if their structure has actually changed. Another advantage is that in these cases the program status can be continuously monitored, even if differences are displayed in the online-offline program.

Note:

Changes to the program code in the blocks of the GRAPH, CEM or CFC languages can result in a change of internal interface data. These changes require a reinitialization even if no structural changes are visible at the block interface.

**Examples**:

You can download a data block without reinitialization in the following cases:

- You generate a data block with the same structure multiple times from an external source, via the Openness function or via the Version Control Interface.

  Note: When you use the described functions to generate a GRAPH block or a block whose memory reserve is activated, the block must be reloaded and reinitialized.
- You add a parameter to the interface and then delete it again.

#### Configuring alarms

When creating alarm classes, each alarm class is assigned an ID which must be unique in the project. Note that when changing projects that were created with an older version, online/offline differences may be displayed even though the online and offline programs are completely identical. These differences are attributable to the fact that the calculation of checksums in alarms has been optimized. However, the blocks are still compatible in most cases.

In some rare cases, however, you might have to recompile and download the project again due to the changes in the checksum calculation before you can monitor and test the project online.

#### Edit non-fail-safe parts of a program via Openness API

As of V17, it is possible to edit the components that are not part of the fail-safe program via the Openness API.

The following functions can be executed via Openness:

- Load non-fail-safe programs into an F-CPU S7-1200/S7-1500
- Compile non-fail-safe hardware and software

#### Instructions

- The existing "D_ACT_DP" instruction has been extended as follows: If you have configured your S7-1500 or ET-200 CPU as I-device, you can switch the I-device functionality off or on in the program of this CPU with the "D_ACT_DP" instruction.
- You use the new "Get_AlarmResources" instruction to determine the number of alarms in an S7-1500 CPU for which your CPU currently has sufficient memory.
- The existing "RH_CTRL" instruction has been extended as follows:

  - You can request the "SYNCUP" system state.
  - You can request that the backup CPU becomes the primary CPU and thus takes control of the process.
  - You can request that the backup CPU goes into "STOP" mode.
- The existing instruction "Get_SMC_Info" is now also supported by S7-1200 CPUs.
- The existing instructions "FileWriteC" and "FileReadC" are now also supported by S7-1200 CPUs.
- The existing instructions "ServerMethodPre" and "ServerMethodPost" are now also supported by S7-1200 CPUs.
- The new instructions "OPC_UA_ReadList_C", "OPC_UA_WriteList_C" and "OPC_UA_MethodCall_C" makes for easier handling of S7-1500 and ET-200 CPUs as OPC UA client. Each of these compact instructions is characterized by the fact that only this one instruction must be parameterized and executed to fulfill its task as an OPC UA client.
- The existing "MB_CLIENT" (MODBUS TCP) instruction has been extended as follows: It now supports the Modbus function 23 that can be used to write job data to the Modbus server and read data from the Modbus server.
- With the new instruction "TCONSettings", you request a connection ID for a new OUC connection in an S7-1200 or an S7-1500 CPU, read a property of a prepared or existing OUC connection, or specify a property for a prepared or existing OUC connection.

  You can read or specify the following connection properties:

  - How a TCP connection is terminated:

    The connection and the associated resources are either released immediately via TCP reset (current behavior) or the connection is terminated via TCP finish. This means that the resources are only released after a timer has expired so that the communication partner can send an acknowledgment.
  - Changing the TTL value for UDP multicast (only for S7-1500 CPUs):

    Until now, a UDP multicast telegram could not be sent across router limits. Now you can specify how many routers in a row can forward a UDP multicast telegram.
- The new "CommConfig" instruction allows you to read and change the following communication parameters of an S7-1500 CPU:

  - DNS host name
  - DNS domain name
  - DHCP ClientId
  - DNS server addresses
  - IP suite (IP address, subnet mask, default gateway or default router)
  - NTP server addresses (You cannot read this communication parameter, only change it.)
- With the new instruction "DQ4_CAM" (S7-1500) you can use the cam control functions of the output module DQ 4x24VDC/2A HS.

### SIMATIC WinCC

#### WinCC Unified (for PC and Unified Comfort Panel)

To avoid error messages due to inconsistencies in the linking of data types, you need to include the user data types used in the PLC in the library before upgrading a project from V16 to V17. To do this, drag the PLC user data type to the library under "Project Library &gt; Types".

WinCC Unified as new generation of HMI development

- Improvements in the operation of the screen editor

  - Improvements in handling screen objects

    (SnapLine To Object, properties for multiple selection, search filter for properties etc.)
- Use of customer-specific fonts
- Two additional pre-defined styles for the WinCC Unified HMI (e.g. day and night mode)
- Faceplates and graphics versioned in library
- Faceplate – functional extensions (e.g. rotating faceplates, additional dynamic &amp; static properties, etc.)
- Additional system functions, e.g. UpdateTag
- Two-hand operation
- Customer-specific fonts
- Centralized user administration
- Enhancement of communication:

  - Indirect addressing of 1200/1500 (absolute multiplexing)
  - Support of S7-1500 Software Controller
  - OPC UA DA (server and client)
  - OPC UA A&amp;C (server)
  - Modbus TCP/IP
  - Omron
  - Ethernet/IP
  - Mitsubishi TCP/IP MELSEC iQR, iQF, FX3 and Q
- The following options are offered for system diagnostics:

  - Diagnostics indicator
  - Device diagnostic buffer as new control
- New features in the parameter control option

  - Complex structures (PLC data type in PLC data type)
- Openness RT

  - Extended with browsing for Openpipe

#### WinCC Unified PC

Version 17 also offers the following functional enhancements:

- Operator control and monitoring of production from any terminal device with an HTML5-capable web browser.

  - Introduction of a new Monitor Client License to enable a user to monitor one process only.
  - In the Runtime Manager, you can define a project as an autostart project, which will be started automatically after a restart of the RT station.
  - In the Runtime Manager, you can set an auto-scaling in the web browser to enable automatic adaptation of the engineered screens to the size of the web browser.
- Audit function:

  - Definition of audit-relevant process values
  - Electronic storage (who, when, old value, new value, comment) and
  - Report generation (including manipulation detection)

#### SIMATIC HMI Unified Comfort Panels

The SIMATIC HMI Unified Comfort Panels are the latest generation of high-end HMI devices from 7" to 22". Glass front with multitouch technology, option to extend functionality with apps and visualization powered by WinCC Unified are only a few of the highlights of this new generation of devices.

Version 17 also offers the following functional enhancements:

- Web Client: Flexible, web-based remote monitoring and operation
- Unified Collaboration: Flexible configuration scenarios by sharing screens between Unified systems
- PDF support in Web Control
- Function Trend Control (f(x))
- Extended RT interface for Edge apps

  - Browsing for Openpipe
- Configurable task bar in the control panel

  - Disable
  - Position selection

#### WinCC Advanced

Screen objects:

- Template screens are possible as library objects
- Pop-up screens are possible as library objects
- Increase to the maximum size of pop-up screens

Tags/communication:

- The operation of S7-1500, Modbus and SIMOTION communications is possible in parallel.

#### WinCC Professional

Logging:

- New SQL server version

  A new version SQL Server 2017 was introduced with WinCC RT Professional V17.

Tags/communication:

- Raw data communication for S7-1500

In addition:

- Runtime stop via command line

  This function enables an automated, controlled shutdown of the RT station in WinCC RT Professional V17.

### Hardware configuration

All important new features of the CPU families are summarized here. You can find additional details on the various topics in the product documentation.

#### S7-1200 CPU

- New Web server

  The PLC web server offers a web-compliant, modern JSON-based data format for reading and writing as well as browsing to CPU process tags (tag values and metadata of the tags) for easy connection of the PLC to web data consumers, such as MES systems and SCADA systems. Even basic system control commands, such as setting the operating state (STOP / RUN), are possible. Each action is secured by a corresponding authorization that must be configured in the TIA Portal.
- OPC UA

  - Improved diagnostics: The OPC UA user receives the following information on the status of the OPC UA server:

    - via the diagnostics buffer

    - via an OPC UA area in the Online &amp; Diagnostics area in the TIA Portal

    - via an improved connection resources display
  - Methods can be provided via the user program of an S7-1200 CPU (instructions "ServerMethodPre" and "ServerMethodPost"). These methods use OPC UA clients in order, for example, to process a manufacturing order via the method call by the S7-1200 CPU.
- Compact Read/Write ASCII Files

  You can use the "FileReadC" and "FileWriteC" instructions to read data from an ASCII file on the SIMATIC memory card on S7-1200 CPUs or write data to an ASCII file on the SIMATIC memory card.
- GetSMCInfo

  Using the "GetSMCInfo" instruction you can read out information about the inserted SIMATIC memory card - such as the memory size, the amount of storage space used or the percentage of service life used up so far (depending on the number of already completed write/delete actions).
- TCONSettings

  With the new instruction "TCONSettings", you request a connection ID for a new OUC connection, read a property of an OUC connection, or specify a property for an OUC connection. You can read or specify the following connection property: Behavior when terminating a TCP connection.

  Behavior when terminating a TCP connection: The connection and the associated resources are either released immediately via TCP reset (current behavior) or the connection is terminated via TCP finish. This means that the resources are only released after a timer has expired so that the communication partner can send an acknowledgment.
- Configured OUC connections
- Time format for data logs selectable - Europe/US

#### SIMATIC S7-1500 and ET 200 CPUs

- New hardware and configuration limits:

  - CPU 1518HF-4 PN (6ES7518-4JP00-0AB0), the new innovative SIMATIC S7-1500H CPU with integrated fail-safe functionality – predestined for applications with high demands on availability and fail-safety.
  - CPU 1518T(F)-4 PN/DP, the high-end S7-1500 technology CPU for sophisticated motion control applications with very high requirements on program scope, networking and processing speed. The CPU with a quantity structure of up to 192 axes is available with and without integrated fail-safety. The current configuration limit of the respective CPU is documented in the technical specifications.
  - CPU 1518 with an extended memory capacity: The work memory of the CPUs 1518 (including T, F, TF, HF) is significantly extended. The current configuration limit of the respective CPU is documented in the technical specifications.
  - The number of UDP multicast circuits has been extended for CPUs 1517 and 1518. The current configuration limits of the respective controller is documented in the technical specifications of the CPU.
  - For the CPUs 1510SP to 1513 (including CPU 1513R) and CPU 1515 (including CPU 1515R), the configuration limit has been increased regarding the number of blocks (and UDTs). The current configuration limits are documented in the technical specifications of the respective CPU.
  - TM MFP (Technology module Multifunctional Platform), this module is predestined for IT applications in the automation technology, that is, for applications that directly evaluate and process data and information from the CPU but that are not integrated directly into the actual control job.
- New functions with firmware V2.9 for all S7-1500 and ET 200 CPUs:

  - Support of MRP (Media Redundancy Protocol) Interconnection. This function is integrated into the firmware and allows for the coupling of multiple MRP rings (up to 11 rings) and thus opens up the possibility to operate more participants in total in MRP rings.
- New functions with firmware V2.9 for S7-1500 and ET 200 CPUs (without R/H CPUs):

  - OPC UA Alarms &amp; Conditions:

    The OPC UA Alarms &amp; Conditions function allows you to transmit messages including their associated values to OPC UA clients. Alarms requiring acknowledgment can be acknowledged by the OPC UA client. This function is activated in TIA Portal via the settings in the CPU properties.
  - OPC UA server interface

    When modeling the OPC UA server interfaces for S7-1500 and ET 200 CPUs, objects and folders can now be created or added as OPC UA elements via drag-and-drop.
  - Compact instructions for OPC UA

    Handling of the CPU as OPC UA client is made easier with the introduction of compact instructions for reading ("OPC_UA_ReadList_C"), writing ("OPC_UA_WriteList_C") and for the method call ("OPC_UA_MethodCall_C").   
    With TIA Portal V17, this means only three instructions are required instead of 12.
  - GDS for certificate update

    The S7-1500 and ET 200 CPUs support the handling of OPC UA certificates via GDS (Global Discovery Service).   
    Either the TIA Portal or a separate GDS server can now be used for certificate updates. You can update certificates during runtime via GDS. Commissioning for GDS can be performed without the need for a certificate to be on the CPU.
  - Completion of the DNS (Domain Name System) functionality for OPC UA / OUC and in the web server:

    - The OPC UA server of the CPU simplifies the handling of connections via NAT router by using name-based address parameters.

    - The NTP client of the CPU can now respond via DNS to its relevant NTP servers. This allows addressing a pool of NTP servers, for example.

    - The web server can be consistently reached via DNS addressing.

    - DNS is taken into account during certificate handling.
  - Support of DHCP (Dynamic Host Configuration Protocol)

    The CPU can use the DHCP communication protocol to assign the network configuration via a DHCP server. The CPU uses a client ID for identification on the DHCP server. The following parameters can be obtained:

    - IP address, subnet mask, default router

    - DNS Server

    - NTP Server

    - Host and domain names

    The CPU can also signal a configured or programmed host and domain name to a DHCP server that is coupled directly to a DNS server. (Dynamic DNS).
  - DHCP and NTP servers:

    With the introduction of DHCP, NTP servers can also be obtained via DHCP. Configuration has changed compared to the previous versions in this instance. Where the NTP server(s) get their configuration must be defined in the configuration:
  - - Via the configuration in the HW properties of the CPU

    - Via DHCP

    - Via the T_CONFIG block*   
     * In contrast to previous firmware versions, when changing the hardware to firmware V2.9, you must now select, in addition to using the T_CONFIG block, that the NTP servers should obtain their configuration via this block.
  - Disabling / enabling the I-device in the user program:

    It is possible to disable or enable the I-device configuration with the instruction "D_ACT_DP" in the user program of the I-device CPU. In so doing, the operation of an I-device without a higher-level IO Controller becomes the "normal operating mode" for which no error is displayed any longer.
  - In the instruction "MB_CLIENT" (MODBUS TCP), the newly supported Modbus function 23 allows for the writing and reading of data within a job.
  - For programmed connections, the new instruction "TCONSettings" can be used to request a connection ID for a new OUC connection, read a property of an OUC connection, or specify a property for an OUC connection. You can read or specify the following connection properties: Behavior when terminating a TCP connection, changing the TTL value for UDP multicast.

    Behavior when terminating a TCP connection: The connection and the associated resources are either released immediately via TCP reset (current behavior) or the connection is terminated via TCP finish. This means that the resources are only released after a timer has expired so that the communication partner can send an acknowledgment.

    Changing the TTL (Time to Live) value for UDP multicast: Until now, a UDP multicast telegram could not be sent across router limits. Now you can specify how many routers can forward a UDP multicast telegram.
  - The new "CommConfig" instruction allows you to read and change the following communication parameters:

    - DNS host name

    - DNS domain name

    - DHCP ClientId

    - DNS server addresses

    - IP suite (IP address, subnet mask, default gateway or default router)

    - NTP server addresses (you cannot read this parameter, only change it.)
  - Assignment of PROFINET device names ("Initialization"):

    Topology-based assignment of device names has been extended to allow PROFINET devices to be renamed, even if they already have a device name. This is used primarily for mobile devices such as automated guided vehicles (AGVs).
  - The display in the CPU web server is extended by information on the "Program resources consumption" so that the user program can be changed accordingly when the available memory is not sufficient.
  - User-defined web pages for the SIMATIC S7-1500 and ET 200 CPUs can be created via WinCC Unified. No special know-how related to producing HTML pages is required for this, but the web pages can be created as screens in the editor of WinCC Unified and then loaded onto the controller.
  - User-defined web pages created using any HTML editing tool can be loaded as HTML files directly into the S7-1500 or ET 200 CPU via the new WEB API without having to use the TIA Portal. The pages are displayed via an HTTPS endpoint in the CPU.
  - You use the new "Get_AlarmResources" instruction to determine the number of alarms for which your CPU currently has sufficient memory.
- New functions with firmware V2.9 for S7-1500R/H CPUs:

  - Expanding the options with the "RH_CTRL" instruction: It is possible to swap the roles of primary CPU and backup CPU, trigger a new SYNCUP and set the backup CPU to "STOP".
  - The changeover times for non-redundant PROFINET devices (switched S1 operation) were significantly reduced.
  - The recipe functions (RecipeImport, RecipeExport) can now also be used for S7-1500R/H CPUs.
  - A redundancy loss of the sync cable is not signaled via an OB72 call for S7-1500H.
- New functions with firmware V2.9 for S7-1500T(F) CPUs:

  - Motion Control extensions

    - Correction profiles coupled to leading values on the following axis

    - Down synchronization of synchronous operation and camming specific to position

    - New cam type (10,000 points) and extended cam diagnostics

    - Backlash compensation

    - Trace: Bode diagram
  - Handling

    - Control of kinematics with up to 4 interpolating axes including synchronization to moving belts

    - Path length output

    - Path control panel with dynamic adaptation
- New functions with firmware V2.9 for S7-1500 and SIMATIC S7-1500T Motion Control

  You can find an overview of the innovations in technology version V6.0 in the S7-1500/S7-1500T Motion Control overview.

  See also: [Innovations V6.0](S7-1500-S7-1500T%20Motion%20Control%20Overview%20%28S7-1500%2C%20S7-1500T%29.md#innovations-v60-s7-1500-s7-1500t)
- New features Safe Kinematics V2.0 (Release 08/2020 with TIA Portal V16 Update 1):

  - System integrated and certified fail-safe solution according to

    - SIL3 (IEC 61508 and IEC 62061)

    - PLe (ISO 13849-1)
  - Released for the following hardware:

    - CPU 1517TF‑3 PN/DP as of FW 2.8

    - CPU 1515SP PC2 TF with CPU 1505SP TF as of FW 20.8

    - CPU 1517F‑3 PN/DP as of FW 2.8

    - CPU 1518F‑4 PN/DP as of FW 2.8
  - Pre-defined kinematics systems

    Monitoring the movement of pre-defined kinematics with up to four axes and free transformations in Cartesian space with up to 12 interpolating axes
  - Safe zone monitoring

    Freely programmable zones for limiting the kinematic movement space and for programming area-dependent Safety functions
  - Safe velocity monitoring

    Monitoring of the Cartesian velocity at freely configurable monitoring points
  - Safe orientation monitoring

    Supervision of the orientation of the flange in user-defined kinematics

#### Web server (S7-1500)

New Web API methods:

- Plc.ReadOperatingMode
- Plc.RequestChangeOperatingMode
- Customer benefits:

  Reading and changing the CPU operating state via Web API

Ticket mechanism and ticket methods for handling the tickets:

- Api.GetTickets
- Api.GetTicketStatus
- Api.CloseTicket
- Customer benefits:

  With the Web server as of firmware version V2.9, you can use the ticket mechanism of the Web API. You can use the ticket mechanism to transfer large amounts of data outside of the JSON RPC protocol.

  The ticket mechanism is the basis for all new, file-based methods, such as file upload/download of resources.

Web applications of the Web API that can be loaded by the user:

- Web applications that can be loaded by the user provide you with an additional set of methods to manage web applications via Web API.
- You can use all available Web API methods within the web applications.
- Customer benefits:

  Web applications that can be loaded by the user offer you the following major advantages as of firmware version V2.9 compared to the older method that provided the user-defined pages via the system function SFC 99 in STEP 7:

  Only the TIA Portal project in the SIMATIC.S7S directory on the SIMATIC memory card changes. Your TIA Portal project is extended by the option of saving resources (e.g. HTML, CSS, JavaScript, etc.) in the project but outside of the data blocks of the user program.

  The resources are saved in the associated web application. Via the Web API, you can download the resources to your PC, edit them and upload them back to the CPU. This procedure results in significantly reduced development times of user-defined pages.

  You can access resources independent of the CPU operating mode (e.g. RUN, STOP) and update these.

  Web applications are also available in the STOP operating mode of the CPU.

Creating user-defined pages with TIA Portal WinCC Unified as of Version V17:

- Compared to creating user-defined pages with a random HTML editor, creating and loading user pages with WinCC Unified for SIMATIC S7-1500 CPUs offers the following advantages:

  - No HTML code expertise required
  - You can make changes to the user-defined pages while the CPU is in the RUN operating state.

#### Comparing the hardware configuration

- Global offline/online comparison of the hardware configuration

  With the help of an icon in the project overview, you can quickly recognize and easily show whether the offline project in the TIA Portal matches the loaded project of the module.
- Offline/offline comparison at parameter level for the hardware configuration

  It is possible to compare the hardware configuration of two identical modules down to the parameter level.

  With a PLC, the configurations of the connected PROFINET and PROFIBUS participants are also taken into account.

The combination of these two functions together with station upload also enables offline/online comparison of the hardware configuration on the parameter level.

### SINAMICS Startdrive

#### SINAMICS Startdrive Basic

- Extension for UMAC

  - Additional function right for changes of drive parameters including DCC
- Extension of the SINAMICS S210 family

  - Support of SINAMICS firmware V5.2 SP3
- Extension by CU320-2 DP (for S120 booksize and chassis devices)
- Extensions for CU320-2 PN and CU310-2 PN based drive units

  - Support of SINAMICS firmware V5.2 SP3
  - User-definable parameter list
  - Data set changeover (drive, motor, encoder and command data sets)
  - Improved optimization options in the drive

    - Bode diagram
  - Extensions for SINAMICS Integrated in the SIMATIC Drive Controller

    - EPOS (basic positioner)

    - DCC (Drive Control Chart)
  - Improvement in the interaction between drives and SIMATIC technology objects
- Extension of the SINAMICS G120 family

  - Support of the distributed drive G115D
- Extension of the SINAMICS MV family

  - Support for SINAMICS firmware V5.2 SP2
- Extension of TO_BasicPos with physical units and the mechanics input

#### SINAMICS Startdrive Advanced

- Extension Safety Acceptance Test

  - Safety Activation Test
  - Support of the distributed drive G115D
- Extensions for CU320-2 PN and CU310-2 PN based drive units

  - Improved optimization options in the drive

    Advanced measurement functions

#### SINAMICS DCC (Drive Control Chart)

- Know-how protection for charts
- Online engineering of the charts
- Support for the CU320-2 DP
- Support of SINAMICS firmware V5.2 SP3
- Support of SINAMICS Integrated in the SIMATIC Drive Controller

### System functions

#### Libraries

- Execution of logic/comment changes do not require version adaptation of dependent types.
- User-defined default version for use in library functions
- Status information on library types
- Roll back to older versions.
- Force update of library types independent of the version number
- Create distributed global libraries by configuring the types relevant for the update
- New filters and search functions for project library and global libraries
- New TIA Portal Openness APIs for library functions

#### SIMATIC TIA Portal Openness

The following new functions and innovations are available in TIA Portal Openness V17. For more details on the various topics, refer to the corresponding sections of the product documentation.

- Extensions for project generation of PLC programs:

  - Creation of instance DBs for FBs in the following additional languages: LAD, FBD, STL, SCL, Graph, Cause Effect Matrix (CEM)
  - Write access to the "PriorityNumber" OB attribute
  - Modules or data types from "ExternalSourceGroup" can be generated directly into a subgroup.
  - Direct read access to DB tags and write access to their "StartValue" property
- Extension for devices with IP address not configured in the project when downloading to the PLC
- Extensions for Safety engineering:

  - Write access for most attributes of the Safety Administration Editor (SAE)
  - Configuration of the Safety engineering password (set, reset, lock, unlock)
  - Compiling the Safety hardware and Safety software
  - Loading of changes in the standard software or standard hardware configuration to an F-PLC with unchanged Safety program / Safety hardware configuration
  - Documentation generation (Safety printout)
- Extended support for library processes:

  - Structure applied when updating the library
  - Clean up library
  - Harmonize project
  - Force update
  - Reading and setting the default version of a type
  - Reading the status information of library types
- Extension of CAx export and import:

  - Support of the AML specification AR APC v1.2
  - Support of Safety Base Units for ET200SP modules
  - Exchange of manufacturer-specific hardware parameters for GSD/GSDML-based devices
  - Option to export normalized order numbers (MLFB)
  - Tolerant import of order numbers (MLFB)
- Support for protected projects (UMAC):

  - Activation of project protection
  - Method extension for opening a protected project
  - Configuration of users and roles in the project
  - Openness function right to prevent changes to a protected project via the Openness API
- Support of the Openness API in a multiuser session
- Support of multi-user processes

  - Create, modify and delete server connections
  - Read out the available projects, sessions on a project server
  - Add projects to the project server
  - Create, open, save and close multi-user sessions
  - Information about changed objects
  - Apply or discard changes (exclusive sessions / server project view)
- Extended export/import support for alarms and ProDiag

  - Export/import of alarm classes
  - Export/import of system diagnostics settings
  - Export/import of ProDiag supervisions and supervision settings
  - Export/import of global supervisions of a ProDiag FB
  - Exporting/importing UDT supervisions
- Support of TIA Portal Test Suite Advanced

  - Export/import of rule sets and test cases
  - Execution of rule sets and test cases
  - Provision of test results from application tests or style guide checks as .NET objects
- Enhancements for Startdrive

  - Write access to MRP communication attributes for all drive devices that support this function
  - Support for G115D
- Openness API enhancement

  Load software changes into all CPU families

#### User Management &amp; Access Control (UMAC)

- Project lock

  When temporarily leaving the engineering station, the project lock prevents editing without closing the project.
- Change user

  The "Change user" function allows you to continue working at the same position in the project after a user change.
- Deactivate users

  Configured users and user groups can be deactivated/activated in the project.
- Anonymous user

  A protected project can be opened by activating the anonymous user without entering a password with the assigned authorizations.
- Selection of the standard logon procedure

  A protected project can be opened without explicit user authentication with the logon procedures "Use anonymous user" or "Use single sign-on session".
- New engineering function rights

  With the new functional rights, the user roles can now be adapted even more specifically to the responsibilities. This makes it possible to protect numerous actions and editors from unauthorized users, e.g. changing the Safety program.
- Openness API support

  - Activation of project protection
  - Configuration of users and roles in the project

See also: [Basics of user administration property in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)

#### Checking for updates

Updates can be installed via TIA Administrator as of V17. The following functions in TIA Portal open the TIA Administrator:

- "Check for updates" function under "Help &gt; Installed software"
- "Check for updates now" function under "Options &gt; Settings &gt; General &gt; Software updates"
- "Check for updates" function in the navigation area of the Information System

#### Secure PG/HMI communication

The PG/HMI communication between TIA Portal or HMIs and the S7-1200 / S7-1500 CPUs contains various security upgrades. Protection is now based on the Internet standard TLS (Transport Layer Security) and thus supports unique identification of the PLCs via certificates as well as encrypted communication. Confidential PLC configuration data can be secured via their own, separate key.

See also: [Secure PG/HMI communication](Configuring%20devices%20and%20networks.md#secure-pghmi-communication-s7-1200-s7-1500-s7-1500t)

### Engineering options

#### TIA Portal Test Suite Advanced

- Styleguide

  - For rule sets, the properties "Author", "Version" and "Comment" can be stored.
  - Manual XML import / export of rule sets using the project tree
- Application test

  - Manual ASCII import / export of application tests using the project tree
- Openness support for Styleguide &amp; Application test

  - Import and export of rule sets (XML file) / test cases (ASCII file) via Openness APIs
  - Import and export of rule sets / test cases from libraries (master copies) via Openness APIs
  - Execution of rule sets / test cases via Openness APIs
  - Test results from application tests or Styleguide checks are made available as .NET objects for the Openness application. They can be used to create user-defined export formats for test results.

#### SIMATIC Target™ for Simulink® V5.0

- Code generation for LiveTwin on Siemens Industrial Edge (this is also why the option from SIMATIC Target 1500S for Simulink was renamed to SIMATIC Target for Simulink)
- Support of the Simulink Embedded Coder
- Integrated S-functions for PLCSIM Advanced coupling for S7-1500 Runtime

#### Central user management via UMC

- Single sign-on

  Single sign-on enables seamless authentication between a protected TIA Portal project and HMI Runtime on the same operator station. Once authenticated, the application can take over the existing single sign-on session.
- SIMATIC Logon client support

  The integration of the SIMATIC Logon protocol enables the use of an existing HMI runtime system within a UMC domain.
- Extended license model

  - Smaller license scale with 100 user accounts
  - No license required for up to 10 user accounts
- Extended configuration with the TIA Administrator

See also: [Basics of user administration property in the TIA Portal](Managing%20users%20and%20roles.md#basics-of-user-management-in-the-tia-portal)

#### Multiuser

- Existing Openness functions can be used in a multiuser session.
- New TIA Portal Openness APIs for the integration of multiuser workflows in own automation processes.
- The asynchronous commissioning mode now supports loading of controllers with activated access protection.

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic / Advanced V17, the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V17.

- Fast Commissioning

  As of TIA Portal V17, it is possible to make commissioning with STEP 7 Safety more efficient. In the future, program adaptations can be made in the F-program in disabled Safety mode and then loaded into the controller during operation. The combination of disabled Safety mode and fast commissioning enables more efficient work due to reduced compile times, since only the program created by the user is compiled and loaded into the controller.

  After finishing the adaptations, the complete F-program can be generated, consistently loaded into the controller and activated by a final re-initialization through a STOP – START transition. The commissioning can then be completed with the acceptance of the Safety program.
- Nested PLC data types

  To optimally structure data in the Safety program, you can create F-compliant data types up to a nesting depth of 8. All data types permitted in the Safety program can be used as F-PLC data types.
- Group signature

  If the Safety program is stored in several groups, changes can be localized faster using the new group signature. For this, the Safety program to be approved can be compared with the already approved Safety program and the approval can be performed more efficiently.
- Support of UMAC (User Management and Access Control)

  In the future, access protection for the F program can also be realized user/role-specific via a Safety engineering function right.
- Openness enhancements

  The available openness functionalities have also been extended with STEP 7 Safety V17:

  - Write access for most attributes of the Safety Administration Editor (SAE)
  - Configuration of the Safety engineering password (set, reset, lock, unlock)
  - Compiling the Safety program and the Safety hardware configuration
  - Safety documentation generation possible (Safety printout)
  - Downloading changes in the standard software or standard hardware configuration to an F-PLC with unchanged Safety program / Safety hardware configuration

  The Openness enhancements now enable the full range of functions for the standard application while using a Safety program.

#### SIMATIC Energy Suite

Flexible energy data connection through integrated interface modules:

- Individual interconnection of advanced and user-defined energy data enables manual connection:

  - Of third party devices or devices not supported by EnSL (Energy Support Library)
  - Via alternative communication channels (e.g. OPC UA, Modbus, cyclic process image)

Automatic load management:

- Overview:

  - Avoidance of expensive load peaks and optimization of the energy supply, through priority-based switching on/off of loads and generators
  - PLC-based load management – offers significantly higher flexibility and availability than a purely PC-based solution
  - Intuitive and simplified engineering of the actuators (consumers and generators) with automatic generation of the S7 program
  - Screens included (for WinCC Professional)
- Enhancements in V17:

  - Support and display of the regenerative operation at the infeed (= negative energy consumption)

#### SIMATIC Visualization Architect (SiVArc)

- Support of Unified
- Use of typed screens instead of master copies
- Global expressions
- Extension of the functions of the copy rule editor.
- Text lists / tag plug-in for FBs / FCs can be written via Openness
- New expressions
- Accesses to STEP 7 OBs
- Access to the resolution of the HMI device
- Improvement in usability

#### TIA Portal Teamcenter Gateway

- "Single sign-on" and smart card (PKI) support

  Teamcenter Gateway supports secure connection between TIA Portal and Teamcenter via "Single-sign-on" (SSO). This only requires a one-time authentication via SSO. No further input of your access data from other Teamcenter clients (with SSO support) is necessary.

  In addition, Teamcenter Gateway V17 and higher supports authentication via customer specific smart card (PKI).
- Link between Teamcenter and TIA Portal objects

  As of V17, TIA Portal objects (FBs, FCs and PLC data type) can be exported to Teamcenter as proxy objects and linked to Teamcenter artifacts. This allows individual Teamcenter objects (e.g. a motor) to be put directly into context with the respective TIA object (FB, FC, PLC data type). If changes are required, you can navigate directly from Teamcenter to the respective TIA Portal object and make changes if necessary. By saving as "new revision", the adapted TIA object is exported as a TIA proxy object to the Teamcenter and stored there as a new revision.
- Export of OPC UA server interfaces

  OPC UA server interfaces can be exported and managed in Teamcenter as of V17.
- Compatibility

  Teamcenter versions V11.2/11.3/11.4/11.5/11.6.0.5/12.2/12.3/12.4/13 are supported.
- Usability improvements

  TIA Portal projects can now be opened directly from Teamcenter.

#### PLCSIM

New for S7-PLCSIM Advanced V4.0:

- The controller code for the following SIMATIC PLCs can now be loaded directly and simulated with S7-PLCSIM Advanced:

  - SIMATIC Drive Controller S7-1504 D TF and S7-1507 D TF
  - SIMATIC S7-1500 H/R CPUs
  - SIMATIC S7-1518 T/TF
  - SIMATIC S7-SIPLUS CPUs (equivalent of the supported standard CPU types)
- PLCSIM Advanced now supports TIA Portal projects from versions V14 to V17 as well as the CPU firmware versions V1.8 – V2.9.
- Extension of the UDP multicast connections:

  - Support of up to 128 UDP multicast connections analogous to the hardware CPU with firmware version V2.9
- TCP/IP communication with NpCap
- The WinPcab TCP/IP driver was replaced with the latest NpCap version that is now installed automatically during the setup.

PLCSIM TIA Portal V17:

- As of V17, you will find the device configuration only in the TIA Portal which results in significant performance enhancements.

### Runtime options

#### SIMATIC ProDiag

There are new supervision symbols to see at a glance what kind of supervision is involved. The round symbols show instantiated supervisions. The square symbols show supervision definitions:

- ![SIMATIC ProDiag](images/133597523083_DV_resource.Stream@PNG-de-DE.png): This symbol shows you a global supervision instance that was created directly in a tag table or in a Global DB.
- ![SIMATIC ProDiag](images/85248238347_DV_resource.Stream@PNG-de-DE.png): This symbol shows you instantiated type supervisions of PLC data types or function blocks.
- ![SIMATIC ProDiag](images/133901181067_DV_resource.Stream@PNG-de-DE.png) : This symbol shows you that a type definition for a supervision was created directly in the block interface of a function block or in a PLC data type.
- ![SIMATIC ProDiag](images/133902783243_DV_resource.Stream@PNG-de-DE.png) : This symbol indicates inherited supervisions of PLC data types and function blocks (multi-instances).

**Supervisions within PLC data types**

- As of TIA Portal version 17, it is possible to define supervisions within PLC data types at Boolean operands.
- It is possible to use hierarchical data structures (another PLC data type is used in the PLC data type by which the supervisions are defined).
- Instances of PLC data types do not necessarily have to be assigned to a ProDiag function block (then no diagnostic function is available).
- Additional supervisions at the point of use of the PLC data type are possible, so that additional diagnostics are available for instance-specific requirements.

Customer benefits:

- Central management of supervisions is possible, e.g. in the library.
- Fewer sources of error due to the elimination of manual definition of supervisions at the points of use.

Important notes:

- Compatibility with old projects: It is possible to reuse previously defined supervisions.
- Criteria analysis for supervisions within PLC data types is not supported.

See also: [Creating supervisions at PLC data types](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#creating-supervisions-at-plc-data-types-s7-1500)

**Convenient configuration of associated values in the specific text field**

- Simple configuration of the associated values using guided operating steps from a drop-down list including syntax check.
- Export/import file has been extended by a new input form, so that external editing is possible.

Customer benefits:

- Intuitive usage of the @ syntax through context-sensitive input support.
- Immediate implementation of the required configuration without previous knowledge through simple usability.

Important notes:

- Compatibility to previous versions is ensured: The @ syntax can still be used if needed. Previous entries remain unchanged.

See also: [Creating accompanying values using the shortcut menu](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#creating-accompanying-values-using-the-shortcut-menu-s7-1500)

**Text list addressable in the user program**

- Text lists can now be addressed in the user program via an associated value using a number.
- The fixed reference via the text list name can be omitted: The text lists can be used flexibly for messages depending on the process status in the user program.

Customer benefits:

- Library blocks can now be used even more flexibly.
- Text lists are multilingual and therefore have an advantage over fixed strings in the user program for message associated values.

Requirements:

- CPU of the S7-1500 series with FW version 2.9 or higher is required (CPU properties: Central alarm management in the CPU must be enabled).

See also: [Creating accompanying values using the shortcut menu](Supervision%20of%20machinery%20and%20plants%20with%20ProDiag%20%28S7-1500%29.md#creating-accompanying-values-using-the-shortcut-menu-s7-1500)

**Usability: Filter views**

- Filter views are available in the ProDiag overviews, as of TIA Portal V17. These provide you with an overview of certain types of supervisions more quickly.
- The following filters are available for global supervision:

  - All global supervisions
  - Global supervisions at PLC data type instances:
- The following filters are available for supervision definitions by type:

  - All supervision definitions
  - Supervision definitions in FBs
  - Supervision definitions in PLC data types
  - Supervision definitions in FBs at elements of PLC data types

    This filter view enables the user to quickly transfer corresponding supervisions definitions directly to the PLC data type (deleting the definitions that are directly available in the FB)
- The following filters are available for instantiated supervisions:

  - All supervision instances
  - FB supervision instances
  - Supervision instances defined in PLC data types

Customer benefits:

- Easy migration from previous projects and thus use of the new possibilities with the definition of supervisions directly in the PLC data type.

Important notes:

- All existing supervisions of old projects remain unaffected by the migration. No automatic adjustments are made.

**Usability: New symbols for better orientation**

- With the introduction of supervisions within PLC data types, new symbols are also provided for better orientation:

  - Symbol for global supervisions (PLC tag table, Global DB)
  - Symbol for type supervisions (FB, PLC data type)
  - Symbol for lower-level supervisions (PLC data type, used in a FB or another PLC data type)
  - Symbol for instantiated supervisions (PLC tag table, Global-DB, Instance-DB)

Customer benefits:

- Improved overview of usage locations of ProDiag supervisions compared to previous version
- The supervisions are now also marked with symbols in the instances. The properties of the supervisions themselves are displayed in the "Properties" Inspector window.

Important notes:

The symbols for global supervisions (color) are automatically changed after migrating the previous project. The symbol form (magnifying glass) remains the same.

**ProDiag in connection with Multiuser Engineering**

Blocks supervised with ProDiag, such as FBs or global DBs, Software Units, PLC data types or tags, are consistently supported by Multiuser Engineering.

#### OPC UA

An S7-1500 CPU with firmware V2.9 or higher supports certificate management services that can be used, for example, by a Global Discovery Server (GDS). Via GDS push management functions, the OPC UA server certificate, trust lists and certificate revocation lists (CRLs) of an S7-1500 CPU can be updated automatically.

OPC UA server of the S7-1500 CPU: Alarms &amp; Conditions with OPC UA runtime license:

- After activation in the server: Program messages including associated values are taken over by the OPC UA server
- Acknowledgment in OPC UA client possible (can be disabled)
- Supported SIMATIC signaling concepts:

  - ProDiag messages (supervision alarms)
  - System alarms
  - Program alarms
  - GRAPH alarms
- Activation requires a PLC license on SIMATIC memory card
- Supported alarms can be received on an OPC UA client via subscriptions
- Node "General SIMATIC alarms/events" or selection of the 3 alarm types

### Installing language packs

#### Description

As of TIA Portal Version 17, you can quickly and easily install additional interface languages using TIA Administrator and the TIA Updater Corporate Configuration Tool. This offers you many advantages:

- Quick availability of additional interface languages
- Reduced data volume for the installation of the TIA Portal setup
- The TIA administrator provides information about newly available language packs and provides support during the installation.
- When changing the version of the TIA Portal, you can freely decide whether you want to add further interface languages or delete the existing ones.

#### Installing the language packs via the TIA Administrator

- As of TIA Portal version 17, the interface languages French (FR), Italian (IT), Spanish (SP), Russian (RU), Japanese (JA) and Korean (KO) can be individually installed via the TIA Administrator.
- The online help in version 17 is available in English only for Russian, Japanese and Korean.

You can find a detailed description of the installation of language packs here.

- Help on the TIA Administrator &gt; Help on software management &gt; Installing language packs
- Help on the TIA Updater Corporate Configuration Tool &gt; Basic information on working with TIA Updater Corporate Configuration Tool

#### Customer benefits

- As of TIA Portal version 17, the interface languages Russian, Japanese and Korean are centrally available in addition to the 6 languages available to date.
- OEMs can also install Russian, Japanese, Korean for their project without having to go through the region.
- Language support is independent of TIA Portal updates
- Faster download times are ensured due to the smaller SETUP size of the TIA Portal
- Notification of new language packs by the TIA Administrator

#### Important notes

- The languages German (DE), English (EN) and Chinese (CH) are still provided with the SETUP of the TIA Portal and can be installed as before. They are therefore not offered by the TIA Administrator.
- All 9 interface languages are thus available for the following components:

  - TIA Portal
  - TIA administrator
  - PLCSIM
- The six interface languages German, English, Chinese, Italian, French and Spanish are available for the following components:

  - License Manager (+ Japanese)
  - SIMATIC Energy Suite
  - SiVArc
  - SINAMICS DCC
  - SINAMICS Startdrive (G120 + S120)
  - SIMOTION SCOUT TIA
  - SIMOCODE ES
  - SINUMERIK STEP 7 Toolbox
  - SINUMERIK Integrate MyHMI
  - SIRIUS ES Plus Platform
  - SIRIUS Soft Starter
  - PCS neo (+ Russian and Japanese)
  - CFC
  - DIGSI 5 (+ RU)

- As before, two languages (German and English) are available for the following packages:

  - SIMATIC STEP 7 Safety (Basic, Advanced)
  - TIA Portal Test Suite Advanced (+ Chinese)
  - SIRIUS Safety ES
  - SICAM
  - SystemOneABT

## What's new in TIA Portal V16

This section contains information on the following topics:

- [SIMATIC STEP 7](#simatic-step-7-3)
- [SIMATIC WinCC](#simatic-wincc-3)
- [SINAMICS Startdrive](#sinamics-startdrive-3)
- [SIMOCODE ES](#simocode-es)
- [System functions](#system-functions-3)
- [Engineering options](#engineering-options-3)
- [Runtime options](#runtime-options-3)
- [Installing language packs](#installing-language-packs-1)

### SIMATIC STEP 7

All important new features of STEP 7 are summarized here. You can find additional details on the various topics in the sections of the product documentation.

#### Software units

- PLC tag tables in software units can be published. It is then possible to access PLC tags and global constants that were declared in another software unit.
- The automated configuration of programs in software units is supported by two new functions:

  - Software units and all their existing program elements are available via the Openness interface.
  - The import and export of external SCL sources in software units is supported.

#### Instructions

- With the new instruction "File Delete" you can delete existing files on the memory card of S7-1500 CPUs.
- The existing "TMAIL_C" instruction has been extended as follows for S7-1500 CPUs / S7-1200 CPUs:

  - You can now send data logs, recipes and user files located on the SIMATIC memory card as email attachments via an integrated interface of your CPU.
  - The value zero is now also allowed for the parameter "WatchDogTime". This means that there is no time monitoring takes place for the execution of "TMAIL_C".
  - Additional error information is available.
- The existing "TMAIL_C" instruction for S7-1200 CPUs has also been extended so that it now has the same range of functions as for S7-1500 CPUs, e.g. email encryption.
- Improved performance of the instructions "Serialize: Serialize", "Deserialize: Deserialize", and "CMP" (comparator) with S7-1500.

  To use the instructions with optimal performance, follow these steps:

  Use a specific data type instead of a VARIANT at the parameters that define the source and target of the instructions.

#### New PID instructions

Three new PID auxiliary functions are available. They reduce the programming effort for tasks in control technology:

- "Filter_PT1"

  The instruction "Filter_PT1" is a proportional transmission component with a delay of the first order, also referred to as PT1 component.

  "Filter_PT1" can be used as

  - Low-pass filter to attenuate high-frequency portions of a signal, such as noise
  - Delay element for smoothing signal jumps, for example, from the setpoint or output value of a controller
  - Process simulation block to realize a closed control loop within the CPU to test, for example, controllers prior to commissioning.

  The following filter parameters can be defined:

  - Proportional gain
  - Delay time constant (lag)
- "Filter_PT2"

  The instruction "Filter_PT2" is a proportional transmission component with a delay of the second order, also referred to as PT2 component.

  "Filter_PT2" can be used as

  - Low-pass filter to attenuate high-frequency portions of a signal, such as noise
  - Delay element for smoothing signal jumps, for example, from the setpoint or output value of a controller
  - Process simulation block to realize a closed control loop within the CPU to test, for example, controllers prior to commissioning.

  The following filter parameters can be defined:

  - Proportional gain
  - Timer constant
  - Damping
- "Filter_DT1"

  The instruction "Filter_DT1" is a differentiator with a delay of the first order, also referred to as DT1 element.

  "Filter_DT1" can be used as

  - High-pass filter to attenuate low-frequency portions of a signal
  - Differentiator to calculate the derivative of a signal, such as the velocity from position values.
  - Feedforward control to mitigate the effect of measurable interferences on the process

  The following filter parameters can be defined:

  - Differentiation time (Td)
  - Delay time constant (lag)

#### Editors for programming languages

- Multilingual comments in SCL

  The new syntax (/* ... */) allows for the input of multilingual comments and regions in SCL blocks. This means code implementations can have comments in different languages.
- Detailed comparison with blocks from the project and global library

  Blocks from the project can be compared with templates and specific type versions from the project or global library using the compare editor.
- CASE statements in SCL blocks support bit sequences

  In addition to integers, Case instructions now also permit bit strings, such as Byte or Word in the expression.
- FOR loops in SCL blocks support unsigned data types

  FOR loops now also allow the unsigned data types UINT, USINT, UDINT and ULINT as run variables.
- Go to Definition

  Navigation via "Go to definition" is now also offered in the tag table (tag of the data type UDT) as well as in the watch table and force table.
- Parameters instance with DB_ANY

  When calling a function block, the parameter instance can now also be transferred by a tag of the data type DB_ANY.
- Display of operand representation and tag information for SCL blocks

  The display of the operand representation and tag information in SCL can now be adjusted independently of the other programming languages via the global settings.

#### Hardware configuration

- S7-1500R/H-CPUs support GRAPH blocks, ProDiag blocks and the "Program_Alarm" instruction.

- The following new CPUs of the ET 200pro family complete the portfolio:

  - CPU 1513pro (F)-2 PN

#### Trace

The new function "Project trace" is used to record traces across devices.  To do so, traces can be created for multiple devices at a central location in the project tree and downloaded to the CPUs involved. The trigger event of one CPU is transferred to all devices and the recordings are synchronized. Once recordings are complete, the project trace displays them in a shared diagram.

The function is available for CPUs of the S7-1500, ET200 SP, Drive Controller and Open Controller series as of firmware version V2.8.

### SIMATIC WinCC

#### WinCC Unified

WinCC Unified as new generation of HMI development:

- Configuration of WinCC Unified in the familiar TIA Portal for a Panel-based (Comfort Unified Panel) and for a PC-based system.
- Seamless scalability of the WinCC Unified project:

  - Easy switch from a Panel-based to a PC-based WinCC Unified project in TIA Portal without loss of configuration information
  - Identical functionality for Panel-based and PC-based systems: Controls with identical appearance and functionality, identical dynamization options using JavaScript as new scripting language
  - Extension of functionalities by adding options (e.g. FileBased Logging, ParameterControl)
- New innovative controls based on HTML5/SVG technology.
- Option to extend the user interface through customer-specific dynamic SVG or CustomWebControls (on HTML5/SVG basis)

#### WinCC Unified PC

- Operator control and monitoring of production from any terminal device with an HTML5-capable web browser.
- Simultaneous, independent access of multiple clients to one server from machine-level PC system all the way to the SCADA system.
- Openness functionality:

  - Automatic creation of WinCC Unified projects using the new HMI ES Openness functionality.
  - Read and write access to process values and alarms during runtime using the HMI RT Openness functionality.
  - Piping mechanism provides access to real-time data of Runtime.
- Plant hierarchy in the TIA Portal enables object-oriented HMI configuration.

#### SIMATIC HMI Unified Comfort Panels

The SIMATIC HMI Unified Comfort Panels are the latest generation of high-end HMI devices from 7" to 22". Glass front with multitouch technology, option to extend functionality with apps and visualization powered by WinCC Unified are only a few of the highlights of this new generation of devices.

An overview of the innovations of the device generation:

- Capacitive multitouch technology as well as saturated colors and exceptional readability of the display
- Identical functionality for all devices from 7" to 22"
- Implementation of larger applications through significantly increased performance and system limits
- Extension of standard functionality through apps possible
- Everything is integrated - from access control, through encrypted communication, all the way to security patches
- Complete commissioning with the TIA Portal. No IT management required
- Visualization powered by WinCC Unified

#### Comfort Panel / Mobile Panel

OnScreenKeyboard:

- Selection of international keyboard layouts for input on the Panel
- Hidden input with connection over Sm@rtServer for devices with full-screen keyboard
- Choice between full screen or small keyboard for 7" and 9"

Printout of barcodes

- The readability of barcode fonts on a printout can be improved with a ProSave add-on

Update of the PDF control and of the PDF printer

- Use of the latest PDF versions

#### HMI Option Plus V3

New functions available:

- Extension of available RFID card readers
- Date display for last project download

#### WinCC Advanced

WinCC Runtime Advanced

- ProDiag

  - "ShowBlockInTIAPortal" system function, the "TIA Portal project path" parameter can be supplied with a dynamic value from a tag

#### WinCC Professional

Archiving

- Archiving of string tags

Tags/communication

- Improvements during autostart between server &lt;&gt; client communication
- Remote communication via Simatic Shell can be switched off
- New tag simulator

ProDiag

- Hierarchical comments are displayed in the PLC Code Viewer
- Operand values are displayed during slice access
- Connection status server &lt;&gt; client is displayed in controls

In addition

- WebBrowser IE 11 compatible
- Connection status of PLC can be displayed and edited via system tag.

---

**See also**

[https://support.industry.siemens.com/cs/ww/en/view/109758056](https://support.industry.siemens.com/cs/ww/en/view/109758056)

### SINAMICS Startdrive

#### SINAMICS Startdrive Basic

- Extension of the S120 family by the Blocksize format

  - Support of CU310-2 PN
  - Support of CU adapters CUA31 and CUA32
  - Support of the PM240-2 power module
  - Support of know-how protection and write protection
- Extensions for CU320-2 PN-based drive units

  - Support of SIMATIC Drive Controller

    With CU320-2 Integrated for up to 6 drives

    Can be expanded with additional CU320-2 PN or S210

    Connection of technology object measuring input with telegram 39x

    See also sales release SIMATIC Drive Controller
  - Support of device know-how protection and write protection
  - Support of the DRIVE-CLiQ hub

    DMC 20

    DME 20
  - Support of UMAC (User Management and Access Control)
  - Support of SINAMICS TEC functionality

    For CU320-2

    For CU310-2
- Extension of the SINAMICS G120 family

  - Support of SINAMICS firmware V4.7 SP13
  - Support of the distributed drive G120Log M and D
  - Support of UMAC (User Management and Access Control)
- Extension of the SINAMICS MV family

  - Support of SINAMICS firmware V5.2 SP1

#### SINAMICS Startdrive Advanced

- Introduction of extended license types for Startdrive Advanced

  - SUS (Software Update Service)
  - UCL (Unlock Copy License)
  - EPL (Enterprise License)
- Extension of the Safety acceptance test for

  - G120Log M and D
  - S120 Blocksize

#### SINAMICS DCC

- Support of Openness Support for DCC

  - Creation of charts
  - Export/import of charts
  - Import of DCB Extension libraries
- Consistency display when charts go online
- Own parameter group for DCC parameters
- Support of the S120 family for the Blocksize format with the CU310-2 PN
- Support of device know-how protection and write protection
- Introduction of extended license types for SINAMICS DCC

  - SUS (Software Update Service)

### SIMOCODE ES

#### Description

The following new features and innovations are available at SIMOCODE ES in the TIA Portal:

- Direct support of new SIMOCODE hardware:

  - Basic unit SIMOCODE pro V PB V4.1
  - Basic unit SIMOCODE pro V EIP V1.1
- Reduction of versions for SIMOCODE ES

  - SIMOCODE ES Standard and SIMOCODE ES Premium become SIMOCODE ES Professional.
- Improved performance in online/offline scenarios
- Trail license query can be disabled if only Basic is to be used.
- Improvement of the expert list:

  - Flat view with uniform name is set as default.
  - Parameters can be marked as favorites for more effective parameter assignment.
- Improvements for bulk change:

  - New toolbar functions
  - Sorting of individual columns is supported
  - New tooltips for better function information
- Improvement of the function diagrams:

  - New banner as information for online/offline differences
  - Online/offline differences are now directly visible at the connection via an icon
  - New search bar for the function blocks
  - Connections can be dragged with a double-click
  - Automatic centering on added function blocks
  - Cursor-oriented zooming in the function diagram editor
  - Easy changing of name and comment of a block I/O
  - Shorten connection names for better display
- Firmware version can be loaded to devices and read online.
- General improvement of tooltips and labeling.
- The safety mode of the DMF-PROFIsafe module can now be disabled.
- Update of the module description is available in the Openness interface.

### System functions

#### TIA Portal Version Control Interface

The Version Control Interface of the TIA Portal allows you to connect an external version control program to the TIA Portal. This allows you to easily store your project data in your preferred versioning program, version it and import it back into the TIA Portal.

#### SIMATIC TIA Portal add-ins

You will receive support for add-ins when you install "TIA Portal Openness". Add-ins enable you to extend TIA Portal to include your own functions. You can integrate these functions into the user interface of TIA Portal via shortcut menus.

You create the program for this with C# and the TIA Portal Openness API. Add-ins must be available as .addin files and be saved in the installation directory of TIA Portal.

You manage your add-ins and activate them in the new "Add-ins" task card.

You can find additional information in the section "Extending TIA Portal functions with add-ins" of the information system.

#### TIA Portal Support Gateway

With the TIA Portal Support Gateway, you can directly access selected online content from Siemens Industry Online Support (SIOS). You can search in the forum and view additional information, such as FAQs or manuals, about the products used in the TIA Portal project.

In addition, the TIA Portal Support Gateway helps you to create support requests: It enables you to export relevant system and project data so that this data is available later when you create a support request.

#### SIMATIC TIA Portal Openness

Compatibility and long-term stability

- Siemens.Engineering.dll files

  The Siemens.Engineering.dll files of V14 SP1, V15, V15.1 and V16 are included in the scope of delivery. This means that applications based on TIA Portal V15, for example, can also run with TIA Portal V16 without modification. To use the new functions of V16, you have to include the Siemens.Engineering.dll file of V16 and recompile the application.

  The Siemens.Engineering.dll files of the compatible versions are located in the installation directory under "PublicAPI\[version]\". For example, the Siemens.Engineering.dll file for V15 can be found under "C:\Program Files\Siemens\Automation\Portal V*\PublicAPI\V15\Siemens.Engineering.dll".
- Export of SimaticML files

  The Siemens.Engineering.dll files V14 SP1, V15, V15.1 and V16 create SimaticML files of the TIA Portal version V16 during export.
- Import of SimaticML files

  Each Siemens.Engineering.dll file can be used to import SimaticML files of its own version and past versions. For example, a SimaticML file of the V15 can be imported with the Siemens.Engineering.dll V16. A SimaticML file of the V16 cannot be imported with the Siemens.Engineering.dll V15.

New functionality

The following new functions and innovations are available in TIA Portal Openness V16. For more details on the various topics, refer to the corresponding sections of the product documentation.

- User-specific marking for devices and modules for unique identification
- Querying of online checksums of PLCs for hardware and software
- Support for software units
- Support for export/import of technology objects
- Support for OPC UA server configuration and interface configuration
- Support for Version Control Interface (VCI)
- Extension of the CAx export and import, such as:

  - AR APC V1.1 support
  - Using objects from the library
  - Support of Base Units for ET200SP modules
- Extension of the support of the hardware configuration of assemblies and modules, such as:

  - OPC UA server configuration and user management
  - Certificate management
  - Web server configuration and user management
  - Watch tables for web server and display
- Support for the configuring of WinCC Unified
- Support for SiVArc:

  - Creation and modification of the SiVArc rules
- Support for safety engineering with set password for the safety program

Export and import of technology objects:

The following technology objects can be exported and imported as XML file:

| CPU | FW | Technology object | Version of the technology object |
| --- | --- | --- | --- |
| S7-1200 | ≥ V4.4 | TO_PositioningAxis | ≥ V7.0 |
| TO_CommandTable |  |  |  |
| ≥ V4.2 | PID_Compact | V2.3 |  |
| PID_3Step |  |  |  |
| PID_Temp | V1.1 |  |  |
| S7-1500 | &lt; V2.0 | High_Speed_Counter | ≥ V4.1 |
| SSI_Absolute_Encoder | ≥ V3.1 |  |  |
| ≥ V2.0 | TO_SpeedAxis | ≥ V5.0 |  |
| TO_PositioningAxis |  |  |  |
| TO_ExternalEncoder |  |  |  |
| TO_SynchronousAxis |  |  |  |
| TO_OutputCam |  |  |  |
| TO_CamTrack |  |  |  |
| TO_MeasuringInput |  |  |  |
| TO_Cam (S7-1500T) |  |  |  |
| TO_Kinematics (S7-1500T) |  |  |  |
| TO_LeadingAxisProxy (S7-1500T) |  |  |  |
| High_Speed_Counter | ≥ V4.1 |  |  |
| SSI_Absolute_Encoder | ≥ V3.1 |  |  |
| PID_Compact | ≥ V2.3 |  |  |
| PID_3Step | V2.3 |  |  |
| PID_Temp | V1.1 |  |  |
| CONT_C |  |  |  |
| CONT_S |  |  |  |
| TCONT_CP |  |  |  |
| SCONT_S |  |  |  |
| S7-300/400 | All | CONT_C | V1.1 |
| CONT_S |  |  |  |
| TCONT_CP |  |  |  |
| TCONT_S |  |  |  |
| TUN_EC |  |  |  |
| TUN_ES |  |  |  |
| PID_CP | V2.0 |  |  |
| PID_ES |  |  |  |
| AXIS_REF |  |  |  |

### Engineering options

#### TIA Portal Engineering

The following improvements have been made in engineering:

- When starting the TIA Portal, you can optionally specify that the last used project is automatically reloaded and the last opened editors are automatically restored.
- TIA Portal project archives can be deactivated and opened using the "Open project" dialog. The "Restore from archive" menu item has been removed.
- TIA Portal project archives can also be used as reference projects without retrieving from archive.
- Locally stored multi-user sessions and exclusive sessions can also be used as reference projects.

#### TIA Portal project server

The server previously known as "Multiuser server" has been renamed "TIA Portal project server".

The "Exclusive Engineering" functionality has been added to the project server.

The TIA Portal project server can be used together with Exclusive Engineering for exclusive local processing of projects.

This has the advantage that all functions of the project server, such as restore preceding versions, use project history and user administration, are also available in the standard engineering environment of the TIA Portal.

#### TIA Portal Multiuser Commissioning

Working with Multiuser Commissioning has been extended by an "asynchronous mode". In asynchronous commissioning mode, the download to device is executed automatically in the background by a second TIA Portal instance. This enables a high-performance downloading to the device and the respective local session is available again faster for renewed changes.

#### PLCSIM

PLCSIM Advanced V3.0

- ODK support for Shared Object and synchronous DLL

  - S7-1518MFP can be simulated with the ODK Part – no changes in the STEP 7 program code. The hardware configuration is necessary to simulate the functionality of an S7-1518MFP.
- PLCSIM Advanced now supports TIA Portal projects from versions V14 to V16 as well as the CPU firmware versions V1.8 – V2.8.
- Improvements of the PLCSIM Advanced API

  - The API has been enhanced by the option to browse for runtimes in the network. This further improved the application in complex scenarios.
  - The API now also supports the deletion of virtual memory cards (local and remote) to release memory in automatic test scenarios, for example.
- Improvements of the diagnostic entries in case of an OB overflow.

PLCSIM TIA Portal V16

- Importing SIM tables from the TIA Portal

  - TIA Portal tag tables / watch tables can be copied and used in PLCSIM.
- Event simulation using the relevant error OB such as OB 40, OB8x
- Scan control allows for program debugging per OB1 cycle

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic / Advanced V16, the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V16.

- A shared installation

  As of TIA Portal V16, STEP 7 Safety is delivered with STEP 7 Professional and WinCC Advanced in a shared installation and together with STEP 7. This means products can be installed more easily and faster, and STEP 7 Safety is available for immediate use providing the corresponding license is available. Delivery includes SIMATIC STEP 7 V16.

  The desired licenses for STEP 7 Safety must still be purchased separately under the corresponding article numbers.
- Openness enhancements

  The range of available Openness functionalities is continuously being extended, which is also the case with STEP 7 Safety V16.

  - Version Control Interface (VCI) – Support

    The new Version Control Interface (VCI) is now also available for fail-safe blocks. It enables the connection of external versioning tools, such as SUBVERSION or GIT. A graphical user interface offers easy operation, integrated block comparison via UI or by connecting third-party tools.
  - Reading out of PLC online fingerprint for Safety program

    For quick detection of differences between online CPU program and offline TIA Portal projects. For users, this functionality means a significant increase in efficiency compared to a conventional station upload and subsequent comparison with a reference project.
  - Openness with set F-password

    So far, Openness could be used until the F-Engineering password (offline password) was set. As of this moment, the Openness functionalities were locked for the safety-related hardware and software components, and the Openness functionalities could only be released again by deleting the F-Engineering password.

    As of Safety V16, users can authenticate themselves with the F-Engineering password and thus use the Openness functionality once again.
- F-SCALE – Scaling in the DINT output area

  The new F-SCALE block allows for fail-safe scaling of encoder values between 0 … 27648 to an output value range in the DINT area.

  The large value range enables, for example, scaling for large distances and weights. The new block prevents time-consuming application solutions that take a long time to compile and require a lot of runtime.

#### SIMATIC Energy Suite

Automatic load management:

- Intuitive and simple engineering of load management systems with a flexible number of consumers and generators
- Automatic generation of the S7 program for all energy objects (for energy measurement and load management)
- Screens for load management included in the scope of delivery (for WinCC Professional)

Generating screens with SiVArc:

- Significant reduction in engineering thanks to automatic generation of screens for all energy objects (energy measurement and load management)
- To generate the Energy Suite screen, only the "Energy Suite Engineering" license is required (SiVArc must be installed, but a SiVArc license is not necessary)

Performance and usability improvements:

- Reduced PLC cycle times thanks to optimized PLC code (approx. 40% faster compared to previous versions)
- Faster and more intuitive engineering thanks to minor usability improvements

#### SIMATIC Visualization Architect (SiVArc)

Support of SIMATIC Energy Suite:

- SIMATIC Energy Suite creates and deletes its own system rules; these are read-only
- The customer only needs the valid "Energy Suite Engineering" license to generate the SIMATIC Energy Suite rules
- The customer can select which rule set is used during generation.

  The following are available for selection: User-created rules / Rules for Energy Suite / All rules. The corresponding licenses must be available for the selected setting.

Support of Openness (optimizations):

- Creating rules
- Modifying rules

Generating based on HWCN:

- Generating screens, tags and alarms based on the configured PN devices.

Merge of properties:

- The customer can select individual parameters for "Merging" in the faceplates.
- This means customers can change these values manually without SiVArc overwriting the value during generating processes.

Optimizations / Improvements:

- Template screens and pop-up screens can now also be used in the Generation Matrix.
- Screen events are now also supported by SiVArc
- Alarm rule editor: Multiple selection for alarm objects

### Runtime options

#### OPC UA

For S7-1500 CPUs as of firmware V2.8 and TIA Portal version 16, with a corresponding Runtime license you can benefit from the following expansions of the integrated OPC UA server:

Improved diagnostics: The OPC UA user receives information on the status of the OPC UA server via messages in the diagnostic buffer, an OPC UA category in the Online &amp; Diagnostics area of TIA Portal as well as an improved connection resources display.

Download behavior: In RUN mode, the OPC UA server only performs a restart during download from the TIA Portal when the newly downloaded data has an effect on the data management of the OPC UA server.

Server interface modeling: Server interfaces can now also be modeled in the TIA Portal or OPC UA Companion Specifications can be imported and mapped to the PLC data management.

The S7-1200 CPUs support the OPC UA server functionality as of firmware V4.4.

This includes reading and writing of tags, the subscription functionality as well as the option to integrate Companion Specifications.

### Installing language packs

#### Description

As of TIA Portal Version 16 you can quickly and easily install additional interface languages using TIA Administrator and the TIA Updater Corporate Configuration Tool. This offers you many advantages:

- Quick availability of additional interface languages
- Reduced data volume for the installation of the TIA Portal setup
- The TIA administrator provides information about newly available language packs and provides support during the installation.
- When changing the version of the TIA Portal, you can freely decide whether you want to add further interface languages or delete the existing ones.

#### Language selection

The following interface languages can be installed as language packs via the TIA Administrator:

- Japanese
- Korean
- Russian

#### Product selection

The additional language packs are available for the following products:

- WinCC Professional + STEP 7
- WinCC Unified + STEP 7
- PLCSim

#### Installing language packs

You can find a detailed description of the installation of language packs here.

Help on the TIA Administrator &gt; Help on software management &gt; Installing language packs

Help on the TIA Updater Corporate Configuration Tool &gt; Basic information on working with TIA Updater Corporate Configuration Tool

## What's new in TIA Portal V15.1

This section contains information on the following topics:

- [SIMATIC STEP 7](#simatic-step-7-4)
- [SIMATIC WinCC](#simatic-wincc-4)
- [SINAMICS Startdrive](#sinamics-startdrive-4)
- [SIMOCODE ES](#simocode-es-1)
- [Engineering options](#engineering-options-4)
- [Runtime options](#runtime-options-4)

### SIMATIC STEP 7

All important new features of STEP 7 are summarized here. You can find additional details on the various topics in the sections of the product documentation.

#### Software units

Software units allow for breaking down the user program into separately loadable units. This means you can load changes to different software units independently of one another to the controller, especially when these changes were made by different users.

The modular processing of the PLC program by multiple users is made a lot easier by this approach.

#### System functions

Keyboard shortcuts are defined in the system for many functions of TIA Portal. As of V15.1 you can also use your own keyboard shortcuts as an alternative to the system-defined keyboard shortcuts. You can find an overview of all keyboard shortcuts and the option of assigning user-defined keyboard shortcuts in the settings for TIA Portal.

#### Editors for programming languages

- Textual block interface in SCL

  When creating new SCL blocks, you can have the block interface displayed as table or text. With text display, you have once again access to the familiar programming environment of STEP 7 V5.x. You can enjoy the benefits of creating comment sections in the block interface, for example, or using basic copying actions with other text editors.

- Actual parameters in SCL

  For better readability of programs in SCL blocks, you can left align the actual parameters for block calls.

- Setpoints in PLC data types (UDTs)

  You can select or deselect the setpoints predefined in a user-defined PLC data type (UDT) in the instance used.

- Snapshot of the current values

  A snapshot of current values is now also retained even in case of structural changes of the data block.

- Monitoring tags

  The keyboard shortcut "Ctrl+T" for enabling/disabling the monitoring of tags is now available in all STEP 7 editors (DB editor, watch table, tag table, etc.).

- Monitoring of PLC data types (UDTs)

  You can mark an input or output parameter of a UDT data type in the program during monitoring and show the associated current values in the inspector window.

- Monitoring of block calls

  Current values for non-interconnected outputs are now also displayed when monitoring block calls.

#### Hardware configuration

- S7-1500 CPUs for the configuration of redundant automation systems

  The following S7-1500 CPUs are available for configuration of redundant and high availability automation systems:

  - CPU 1513R-1 PN
  - CPU 1515R-2 PN
  - CPU 1517H-3 PN

- Isochronous mode on the backplane bus

  Modules which are plugged centrally in an S7-1500 station can be operated in isochronous mode. Isochronous coupling of centrally plugged modules with distributed plugged modules is also possible.

- MRP domain configuration across project boundaries

  Redundancy managers and redundancy clients of an MRP domain can be located in different projects.

- Quickly change firmware version for multiple modules

  You can change the configured firmware version of modules in an IO device by multiple selection of a group of modules in one step.

- Fast switching between I/O tag in the program editor and affected input/output in the device view

  The shortcut menu "Go to &gt; Device view" enables fast navigation from the programmed I/O address from the program editors to the configured input or output in the device view.

- Simplified configuration of series machine projects

  For the configuration of optional IO devices in a series machine project, the necessity of port interconnection (topology configuration) is eliminated.

#### S7-1500 Motion Control

Technology version V4.0 contains the following new features:

- Exchange of torque data with the drive in the technological units of the technology object:

  - Additive setpoint torque
  - Current actual torque
  - Permissible torque range

- Time requirements for the technology object "Measurement jobs" via "MC_MeasuringInput"

- Extension of the data structure of the positioning axis and synchronous axis for using the kinematic technology object

- Use of optimized data blocks (drive/encoder connection)

Technology version V4.0 for the technology CPUs (S7-1500T) contains the following additional new features:

- Kinematic technology object (S7-1500T)

- Motion specification via "MotionIn" instructions (S7-1500T)

- Direct synchronous setting with MC_CamIn V4.0 (S7-1500T)

Technology version V4.0 contains the following new or extended Motion Control instructions for these functions.

#### Trace

Easier handling of chart configurations:

- Settings relevant for the display can already be made during configuration. This includes signal grouping, color selection, display format and creating formulas.

- Changes made online can be applied with "Transfer of trace configuration from the device". The settings in the "Chart" tab are retained even if you make changes during the configuration and add signals, for example, or change the number of measuring points.

### SIMATIC WinCC

#### WinCC RT Professional

- OPC UA server

  - Support of OPC UA server alarm and condition
  - WinCC alarms can be transferred to a third-party application via OPC UA servers.

- ProDiag Control

  - Display of the entire Call Interface block

- Additional functional extensions

  - Setting the WebUX / WebNavigator user rights in runtime
  - Automatic login for operator role
  - HMI Compiler provides additional information for users (e.g. number of compiled HMI objects)
  - Software controller with WinCC Professional on a shared computer

#### Mobile Panel

- KTP Mobile V15 images and SmartServer option for F-devices

  [https://support.industry.siemens.com/cs/ww/en/view/109758056](https://support.industry.siemens.com/cs/ww/en/view/109758056)

- Option+ V2 for Comfort and Mobile Panel

  - Support of the Mobile Panel 2nd Generation
  - Code is written directly into a tag with QR reader MV320/325
  - Display of the Panel CPU load directly in runtime
  - Optimization of the certificate handling of SIMATIC Logon
  - Hiding of individual desktop icons
  - Expansion of service file for technical support
  - Switch of communication between Option+ and Panel Runtime from SOAP to OPC UA

- Mobile Panel 2nd Gen., Comfort Panel and Basic Panel 2nd Gen.

  Configuration of the alarm buffer

### SINAMICS Startdrive

#### All drive families (G120, S120, S210)

- Extensions of the Openness interface:

  - Functional interfaces for important applications (e.g. input of motor data)
  - For G120 and S210: Generation of the TIA Portal project based on an AML-based import of EPLAN
- Startdrive Advanced V15.1: Safety Integrated acceptance test also for S210 and S120

  - Guided acceptance test wizard for all drive-based Safety Integrated Functions (Basic, Extended and Advanced)
  - Automatic and Safety Integrated function-specific creation of traces for analysis of the machine behavior
  - Generation of an acceptance report as an Excel file (xlsx format, can also be used with OpenOffice)

#### SINAMICS G120

- User-definable parameter lists
- Data synchronization between G120 and S7-1500 technology objects also possible offline (in the project)
- Usability improvements:

  - Overview screen form for G120 configuration
  - Simplified device identification via LED flashing in the "Connect online" dialog

#### Integration of SINAMICS S210 and 1FK2

- Integration of the S210 drives with 200 V and 400 V as of SINAMICS firmware V5.2
- Support of 1FK2 motors
- Usability: Easier configuration procedure compared to S120
- Data synchronization between S210 and S7-1500 technology objects online and offline (in the project)
- Trace (including recommendation of typical parameters)
- Firmware update via TIA Portal
- Auto Servo Tuning via One Button Tuning
- Safety Integrated configuration

#### SINAMICS S120 (CU320-based drives)

- Support of the SINAMICS firmware V5.1 SP1
- Support of 1FK2 motors
- Operation on S7-1500 Open/Software controllers
- Data synchronization between S120 and S7-1500 technology objects also offline (in the project)
- Connection to S7-1500 technology object type "Probe"
- Support of the technology data block telegram 750
- Support of Isochronous Safe Position (for support of the PLC function "Cartesian Safety")
- Parameter list with functional structure (parameter groups)
- Auto Servo Tuning via One Button Tuning

### SIMOCODE ES

#### Description

The following new features and innovations are available at SIMOCODE ES in the TIA Portal:

- Direct support of new SIMOCODE hardware:

  - Basic unit SIMOCODE pro V PN V2.1 with ATEX dry-running protection
  - Basic unit SIMOCODE pro V PN GP V2.1 as "General Performance" PROFINET device
  - Current/voltage acquisition module with ATEX dry-running protection
- Access to all device-specific parameters via the TIA Openness interface:

  - Creation and configuration of SIMOCODE pro devices via the Openness interface
  - Offline definition of all SIMOCODE pro parameters
  - Networking devices
  - Support for exporting and importing CAx data
  - Support for exporting and importing one or more devices into / out of an AML file
- SIMOCODE pro V PN offers the possibility of implementing dry-running protection for centrifugal pumps (non-electrical devices) using active power monitoring and motor shutdown. This applies to centrifugal pumps with progressive performance curve, which are also suitable for handling flammable media and can also be installed in hazardous areas. Detailed information can be found in the online help for SIMOCODE ES V15.1 topics "Dry-running protection of centrifugal pumps based on active power monitoring" and "Dry-running protection wizard".
- The following labeling parameters can now be changed online during operation:

  - Plant designation
  - Location identifier
  - Installation date
  - Description
- The parameter wizard now allows changes to be made which result in a modified hardware configuration.
- Expert list

  - Marking and filtering of changed parameters
- Improvements for bulk changes:

  - Changed parameters can be copied to other devices/groups.
  - Device can be added to multiple groups.
- Migration of SIMOCODE ES 2007 template files (*.sdt) is now possible:

  - Parameters marked as SIMOCODE ES 2007 "Template" are designated as "Favorites" in the expert list after migration.
- Clearer grouping of analog values in the block catalog.

### Engineering options

#### TIA Portal Multiuser Engineering

- Improved performance at low network bandwidths

  New network profiles have been added for improved connectivity between the engineering station and the multiuser server.

- Functional extensions for multiuser power tools (command line tools)

  Export and import functions are now available for Multiuser server projects and local sessions.

#### TIA Portal Multiuser Commissioning

Multiuser engineering supports users during commissioning with a guided commissioning workflow. Download to the device is automatically synchronized in commissioning mode. This enables a consistent version between the device and the multiuser server project and the associated local sessions.

#### PLCSIM Advanced

- Control Panel extensions

  - Double-click the Control Panel to open it as a floating window. It can be moved freely and can always be shown in the foreground, if necessary.
  - Instances that were created in the past can be created in the floating Control Panel by selecting the virtual memory card in the Explorer and moving the instances from the Explorer to the Control Panel with drag and drop.

- API extensions

  The maximum cycle time of the virtual controller can be freely defined over the API without having to change the maximum cycle time in the TIA Portal project.

#### SIMATIC TIA Portal Openness

- Openness DLLs of V14 SP1, V15 and V15.1 in the scope of delivery

  Because the Openness DLLs of V14 SP1, V15 and V15.1 are included in the scope of delivery, applications based on V14S P1 or V15 also run in V15.1 without any changes. To make use of the functions of V15.1, you must integrate the DLL of V15.1 and recompile the application.

- Accessing projects

  - Multiple projects in a TIA Portal instance can be opened via Openness.
  - Projects can be archived and restored via Openness.
  - For UMAC-protected projects Openness enables read access to objects. The same restrictions apply to this type of access as for a user with the "Read only" authorization.

- Save as

  Projects and global libraries can be saved via Openness under a different name.

- Online/offline comparison

  The online and offline comparison of data is possible via Openness.

- Accessing protection levels

  A protection level can be set or removed for blocks.

- Accessing fingerprints

  The fingerprint can be queried for blocks and PLC data types (UDTs).

- Accessing names

  The name can be set for blocks, data blocks and UDTs.

- Fault-tolerant import

  In addition to the strict import that can still be used, a fault-tolerant import is now available. The import is still possible even if linked user data types or called blocks do not match, for example.

- Export and import

  - Watch tables as well as force tables can be exported and imported.
  - Snapshots of the current values can be exported as XML from an offline DB. This means different snapshots can be compared with the help of the XML files.

- ET200SP

  Read and write access is possible for most attributes of the ET200SP modules.

- R/H systems

  Download to the primary PLC and the backup PLC is possible for R/H systems.

- Fail-safe PLC

  - The upload is now also possible indirectly via NAT router.
  - Recipes, archives, user files and the passwords of the protection levels are also taken into account during the upload.

#### SIMATIC STEP 7 Safety

- New fail-safe CPU-CPU communication "Flexible F-Link"

  A new fail-safe CPU-CPU communication, "Flexible F-Link", is available with STEP 7 Safety V15.1 for the fail-safe S7-1200 and S7-1500 CPUs. This means fail-safe data can be easily exchanged as fail-safe ARRAY between two fail-safe CPUs by means of standard communication mechanisms.

- Fail-safe transfer of large amounts of fail-safe data over standard communication blocks

  Flexible F-Link supports the fail-safe transfer of large amounts of fail-safe data by means of standard communication blocks even across network limits (Layer 3 communication). Requirement is the consistent and deterministic transfer of data.

  The data to be transferred is bundled into user-defined F-compliant PLC data types (UDTs). Any fail-safe data types (Bool, Word, INT, DINT, TIME) can be used. Up to 100 bytes per UDT are supported.

- Easy parameter assignment and automatic generation of fail-safe communication DBs

  The parameters of the communication connection are assigned in the Safety Administration Editor (SAE) whereby each communication connection is created with name, UDT, monitoring time, send or receive direction, and a communication DB is automatically generated by the system. This communication DB provides the data to be transferred in form of a coded F-ARRAY which can then be easily transferred over standard communication blocks such as TSEND or USEND.

- Fail-safe runtime group communication

  Flexible F-Link also enables easy implementation of fail-safe runtime group communication. To do so, the fail-safe data can, for example, be transferred between the F-runtime groups with the "UMOVE_BLK" instruction.

- Unique communication ID (UUID) throughout the network

  The Flexible F-Link also provides a solution when it comes to ensuring the unique identification of communication partners across network limits. A unique communication ID (Universally Unique Identifier UUID) can be generated with STEP 7 Safety which ensures that the ID is unique.

- Communication signature

  A separate communication signature that is independent of the hardware and software signature makes it easy to clearly distinguish between changes to the UUID and changes to the program or hardware.

- Pre-processing and post-processing

  For easier configuration and an easily verifiable time behavior, especially in the context of fail-safe communication, STEP 7 Safety in version V15.1 offers the possibility of placing standard blocks for pre-processing and post-processing of process values around the F-runtime groups.

- Variable communication ID (DP_DP_ID)

  As of version V15.1, STEP 7 Safety offers the possibility of assigning tags instead of constants to the communication IDs (DP_DP_IDs) required for the SENDDP and RCVDP blocks. This enables users in plants with a large number of identical iDevices (high-bay warehouses, AGVs, suspended monorails, etc.), for example, to use safety programs with the same F-collective signature. The variable communication ID thus enables easier commissioning, maintenance and project management.

  **Notice:** If variable communication IDs (DP_DP_ID) are used, the user must ensure that from an application viewpoint the communication IDs are unique throughout the network at any time.

- Openness

  Additional functions are provided with STEP 7 Safety V15.1 over the Openness interface

  - Reading and configuring i-parameters of the ET200SP F-IOs
  - Station Upload
  - Hardware and software comparison (offline/offline)
  - Import and export of consistent (unchanged) F-blocks

#### TIA Portal Teamcenter Gateway

- Multiuser Engineering

  Multiple persons can now work on a TIA Portal project simultaneously with the help of "TIA Portal Teamcenter Gateway" and "Multiuser Engineering" options.

- Opening reference projects from Teamcenter

  You can open projects from Teamcenter directly as reference projects, for example, to compare and merge different revisions.

- Saving projects under existing Teamcenter elements

  You can save TIA Portal projects and libraries from within the TIA Portal under already existing Teamcenter elements.

- Compatibility

  Teamcenter versions V11.2/11.3/11.4/11.5 are supported.

#### SIMATIC Energy Suite

- Energy Screens

  Now part of the scope of delivery of Energy Suite V15.1

- Reports

  New: Cost center report including rates

- SINAMICS

  The configuration of SINAMICS devices with MDD is supported (until now only GSDML has been supported)

- Usability improvements

  Various smaller usability improvements

#### **SIMATIC Visualization Architect**

- Access protection to the SiVArc rule editors by means of UMAC

- X/Y properties can be set using SiVArc expressions.

- Support of STEP 7 blocks written in SCL

- Generation on template screens

- SiVArc – Openness:

  - Copying individual rules or entire rule groups from the library
  - Starting SiVArc generation

### Runtime options

#### SIMATIC ProDiag

- Text export/import for translations

  All texts relevant for ProDiag or S7-GRAPH can be exported for translation, for example, with one action.

  The following alarm texts can be exported:

  - User-defined text lists for supervisions
  - Display names for steps and transitions in GRAPH
  - Comments of all supervised tags
  - Comments of all supervised parameters of a block
  - Instance name and instance comment of multi-instances

  The following texts can be exported for the HMI display:

  - Tag comments in Transition and Interlock
  - Titles and comments of supervised networks or tags

- Display of the entire block (LAD, FBD) in the HMI PLC Code Viewer

  The PLC Code Viewer can be used even if static parameters of a block are being monitored (user blocks with own monitoring logic).

- Edit block supervisions in the ProDiag overview editor

  Existing supervisions in the "FB supervision definitions" tab can be edited or deleted.

- Jump into TIA Portal from WinCC Advanced

  - System-supported jump into TIA Portal in the context of a GRAPH or ProDiag alarm
  - Relevant block is opened automatically
  - Read mode or write/read mode is possible
  - Automatic status display

- Consideration of hierarchical comments in ProDiag alarms

  - Easy mapping of the technological view on the machine / plant using hierarchical comments whereby the path is generated automatically.

- Subcategories in GRAPH

  - Identical alarm structure can be configured as in ProDiag.
  - Especially relevant for control systems in which a follow-up action is derived from additional information in the alarm text.

#### OPC UA

For S7-1500 CPUs as of firmware V2.6 you can benefit from the following extension with a corresponding OPC UA Runtime license:

In addition to the OPC UA server, an OPC UA client is integrated in the CPU which offers the following functions over corresponding OPC UA communication instructions:

- Method calls
- Reading and writing of data

The client opens up the following application areas, for example:

- Vertical communication to MES systems or cloud services
- Controller-Controller communication

## What's new in TIA Portal V15

This section contains information on the following topics:

- [Introduction](#introduction)
- [SIMATIC STEP 7](#simatic-step-7-5)
- [SIMATIC WinCC](#simatic-wincc-5)
- [SINAMICS Startdrive](#sinamics-startdrive-5)
- [SIMOCODE ES](#simocode-es-2)
- [Engineering options](#engineering-options-5)
- [Runtime options](#runtime-options-5)

### Introduction

#### Description

All important new features compared to existing versions are summarized here. You can find additional details on the various topics in the individual sections of the product documentation.

### SIMATIC STEP 7

#### Description

All important new features of STEP 7 are shown grouped together based on the engineering workflow.

#### Hardware configuration

- The following new CPUs of the S7-1500 family complete the portfolio:

  - CPU 1518(F)-4 PN/DP MFP (multifunctional platform)
  - CPU 1516T(F)
- Hardware recognition of real existing PROFINET IO devices  
  The online function "hardware recognition" detects IO devices on the connected PROFINET subnet. You can transfer a detected device to your project: STEP 7 inserts the IO device with all the modules and submodules, thus saving the manual insertion of IO devices and modules from the hardware catalog.
- The "Go to device view" function enables fast navigation from the PLC tag table to the configured input or output in the device view.
- Extended alarm display with new filter functions.

#### Editors for programming languages

- Multilingual project texts, such as block and network titles or comments, can be displayed and edited directly in the programming editors in all available languages. You can also export and import the texts for external translation. The following editors support local display of project texts: PLC tag table, programming editor (LAD, FBD, SCL, STL, GRAPH), data blocks and PLC data types.
- The status bar has been extended in SCL. The current cursor position is now displayed. By double-clicking on the line number, you can call the "Go to line number" function to navigate to additional lines. The editing mode (insert/overwrite) is also shown in the status bar. You can switch the editing mode by double-clicking on the display field.

#### New instructions

- You can use the "FileReadC" and "FileWriteC" instructions to read data from an ASCII file on the SIMATIC memory card on S7-1500 CPUs or write data to an ASCII file on the SIMATIC memory card.
- You can use the "GetClockStatus" instruction to read the following information from the CPU-internal clock on S7-1500 CPUs:

  - Information about time synchronization via an NTP Server
  - Information about whether automatic switching of daylight saving to standard time is activated
- With the help of the "EQ_TypeOfDB" instruction (SCL: "TypeofDB"), the data type of a data block which is addressed via a DB_ANY tag can be determined.
- The existing "SCATTER" and "GATHER" instructions have been extended and now also support an anonymous STRUCT data type and PLC data types with Boolean elements only.
- There are two new PID auxiliary functions available: They reduce the programming effort for tasks in control technology.

  - "SplitRange"

    Is used for distribution of the controller output to several actuators. Dependent on the controller output, this enables different actuators to be controlled
  - "RampFunction"

    This limits the sweep rate and the maximum values of signals. The slew rate can be individually limited in four operating areas: For positive or negative signals, for rising or falling signals.

#### Language innovations

- "References" provides a new type of pointer. References are typed pointers that refer to a specific data type. When you use references, you define the data type during the creating of the program. Because the data type does not have to be determined at runtime, the program will perform better and be more clearly structured. "Dereferencing" gives can direct write or read access to the referenced tag without having to copy the tag beforehand or integrate additional instructions in your program.

  A CPU of the S7-1500 series as of version V2.5 is required to use referencing.
- Constants of the BOOL type can be used at inputs of instructions in LAD/FBD. This facilitates the testing or "bridging" of current paths.

  An S7-1200 CPU as of FW V4.0 or an S7-1500 as of FW V1.8 is required for this function.

#### System functions

- The information system offers the possibility to display hardware manuals integrated. This has the advantage that you can search, filter or use the content as a favorite. Some hardware manuals are already included in the installation of the TIA Portal V15. If necessary, you can download additional hardware manuals available as support packages. To do this, select the function "Check for updates" in the toolbar of the table of contents.
- Local user and rights management

  - Managing project users
  - Open new function rights as read only / open project as read only + write / create users and roles
  - Managing project roles
  - Assignment of users to project roles
  - A block for industrial security with TIA Portal
  - Efficient user administration for products in a TIA Portal project

#### Libraries

- Global libraries can be exported as read-only libraries. The contained library types have permanent write protection and are therefore protected against changes. Write protection of the library types is retained even when they are used as a type instance. Write protection of protected global libraries cannot be revoked. Read-only libraries are available for PLC and HMI types.

#### New functionality for controlling operands

- Boolean operands can be controlled by double-clicking on the monitor value. The actual values can be toggled easily and quickly.
- Non-Boolean operands can also be controlled easily and quickly via the stored dialog.
- Both global tags and instance tags are supported in the DB.

#### Cross-references for instructions used

- User-defined "Instruction" type filters enable you to display all the instructions used in a CPU in the cross-references with the respective instruction versions.

#### Loading PLC tag tables

- PLC tag tables can be uploaded to and downloaded from the device in the specified structure and enable improved team engineering on the CPU.
- The PLC tag tables on the CPU are also displayed with "Accessible devices" and on the memory card.
- The online/offline comparison gives you a detailed overview of the tags available online and offline in the individual PLC tag tables.

#### Breakpoints for S7-1500 as of firmware V2.5

- Testing with breakpoints is also possible in mixed LAD/FBD blocks for SCL and STL programs.
- When a breakpoint is reached, the CPU goes to the "HOLD" operating state. Tags can also be monitored and controlled when the breakpoint is reached.
- This allows the STL and SCL program code to be tested step-by-step using breakpoints in order to find and correct logical errors during program creation. This enables easy and fast analysis of complex programs before the actual commissioning.

#### PLCSIM

- Know-how protected blocks of an S7-1500 CPU can be simulated with PLCSIM V15 (S7-1200 CPUs are currently not supported).
- Using a slider for analog values and pushbuttons for Boolean values, you can very easily make changes to values within the SIM table for quick testing of the STEP 7 user program.
- PLCSIM V15 and PLCSIM Advanced V2.0 can be installed on the same PC. Simultaneous use of both simulation tools is excluded, however.

#### Trace

- Generation of virtual signals based on mathematical functions from the recorded signals. The following functions are supported:

  - Basic arithmetic
  - Absolute value, square root, square, 1/x, modulo operation
  - Integral, differentiation
  - Filter function
- Calculation of the mean, RMS and integral of the selected signal in the range of the measurement cursors
- Time tags of type TIME, LTIME, TOD, LTOD, DATE and LDT can be recorded as a signal and used to specify trigger conditions
- Import and export of superimposed measurements
- Moving the measurement cursors using the arrow keys

### SIMATIC WinCC

#### HMI devices

The following HMI devices can also be configured in the TIA Portal:

- TP1200 Comfort PRO
- TP1500 Comfort PRO
- TP1900 Comfort PRO
- TP2200 Comfort PRO

#### HMI device versions

To optimize the size of the standard installation, older versions of the HMI device images are swapped out to an additional DVD. The device versions affected are:

- V13
- V13 SP1
- V13 SP2
- V14

#### SVG graphics

In WinCC, the format SVG is also supported for graphics.

#### Extension of the ProDiag functionality

The criteria analysis display can be configured for improved process diagnostics. This makes it possible to display the operands with error that have triggered a selected ProDiag or GRAPH alarm in the user program.

#### OPC UA Client in WinCC RT Professional

Communication via OPC UA has been extended.

- Arrays and array variables are supported.
- Communication via an OPC UA connection can be protected with a password.

#### Number of connections with WinCC RT Professional

The number of possible integrated connections for S7-1200 and S7-1500 was increased to 128.

### SINAMICS Startdrive

#### **SINAMICS Startdrive Basic (formerly SINAMICS Startdrive)**

- Enhancements for CU320-2 PN-based drive devices:

  - Support of G130, G150, S150 and Sinamics MV (up to 85.00 kW)
  - Support of Chassis and Cabinet Modules (not Blocksize Modules)
  - Support of SIMOTICS asynchronous motors and third-party motors
  - Vector control
  - Parameter comparison (online/offline, comparison to factory setting)
- Enhancements for SINAMICS G120 product family:

  - Support of SINAMICS Firmware Version V4.7 SP9
  - Further optimization and expansion of the commissioning wizard:

    - Configuration of motor holding brake

    - Cancel online

    - CU250D-2: SSI encoder as motor encoder
  - PROFINET name assignment without restart of G120 Control Unit also in the list of accessible devices
  - Support of CU240D-2/CU250D-2 with polymer optical fiber (POF)
- Openness for drive devices:

  - Creating drive devices and components (including frame configuration)
  - Setting of selected drive parameters (offline and online, reading and writing)
  - Download to the device (no upload)

#### SINAMICS Startdrive Advanced

- Introduction of Startdrive Advanced license for use of additional engineering functions with high added value
- Only license key is needed, no additional installation
- Free trial license without license key (21 days)
- Functions in V15: Safety acceptance test for G120 family

  - Guided acceptance test wizard for all Safety Integrated functions (Basic and Extended Safety)
  - Automatic and safety function-specific creation of traces
  - Generation of an acceptance report as an Excel file

### SIMOCODE ES

#### Description

The following new features and innovations are available at SIMOCODE ES in the TIA Portal:

- User-configurable display of device parameters

  - A new view of the device parameters, the "Expert list", is available in the parameter editor.
  - Groups of parameters as well as individual parameters can be marked as favorites.
  - A filtered parameter view is possible based on these favorites.
  - Export and import this selection of favorites (without values)
- Bulk engineering

  - High-performance function for bulk engineering of devices within a project (also for different SIMOCODE for each device)
  - Selected and appropriately set parameters can be transferred to a group of devices in a single step.
- Parameter wizard

  - Step-by-step configuration of all important device parameters
  - Settings for the fieldbus interface, device configuration, motor protection and monitoring functions can be queried and stored
  - User can call up the wizard directly from the Parameter Editor at any time.
- Automatic generation of PLC tags

  - If STEP 7 is additionally installed and one SIMOCODE per device is connected to a PLC, PLC tags are automatically generated for all inputs and outputs that are exchanged with a PLC via PROFIBUS or PROFINET.
  - Thanks to this function, the user can directly access these data in the user program using symbolic addressing.
- Automatic layout of graphical blocks

  - Placement of the blocks in fixed columns similar to the IPO principle (IPO = input, processing, output)
- All parameters can now be edited in the graphics editor, not just the connections.

  - Values can be entered directly at the function block using the keyboard.

### Engineering options

#### PLCSIM Advanced

- Synchronization of PLCSIM Advanced with co-simulations tools on process image partitions of cyclic OBs (e.g. cyclic interrupt OBs)
- Support of acyclic services (RDREC/WRREC) and interrupts (e.g. hardware interrupts)
- Hardware interrupts configured in the TIA Portal can be read out via the API
- Simple backup and reloading of the software and hardware configuration of PLCSIM Advanced instances
- The storage path of the virtual SIMATIC memory card is freely selectable.
- GUI expansions:

  - Autocomplete
  - Buttons for RUN / STOP and Memory Reset integrated in the GUI of PLCSIM Advanced
- Computer-to-computer transfer of SIMATIC memory cards via the API
- Improved performance for symbolic access
- Parallel installation of PLCSIM and PLCSIM Advanced on a PC

#### **User Management Component**

- Central. cross-project user management in the system
- Managing user groups
- Import of Windows users and user groups is possible
- Efficient administration of users / user groups in a system
- Fault tolerance through redundant design of a UMC domain
- Load distribution of login request surges by means of several UMC stations in a UMC domain
- Licensing via the number of users

#### Multiuser Engineering

- Multiuser objects are now automatically selected when editing. Manual selection is still possible. Automatic selection increases the reliability when working together with Multiuser Engineering.
- Working with Multiuser Engineering is now also possible offline and without a direct server connection.
- Comment functions for documentation of the type and scope of the changes made have been added to the multiuser editors.
- When checking in, a filter is available for viewing objects with "conflicts".
- The multiuser server provides extended project history with a restore function. This enables traceability of the project process on the multiuser server. The milestones of a project can be commented and saved. The project history can be exported for extended evaluation.
- Multiuser Server V14 and V15 can be used side-by-side. Multiuser Server V15 also supports TIA Portal projects from V14 with the corresponding scope of functions.
- The external multiuser tools for the configuration and administration of the multiuser server are now available in all languages of the TIA Portal.

#### **SIMATIC Visualization Architect**

- Generation of alarms, alarms classes and alarm groups
- Support of the HMI objects "trend view", "f(x) trend view" and "f(t) trend view"
- Support of screen templates

#### **SIMATIC Energy Suite**

- Visualization of energy data in energy objects does not require additional PowerTags in WinCC RT Professional.
- S7 energy efficiency monitor for machines (new S7 instruction in STEP 7: "EnS_EEm_Calc" and "EnS_EEm_Report"):

  - For production-related and standardized determination of energy consumptions in machines (according to VDMA 34179)
  - Easy integration in machine controller (S7-1200/1500) and local visualization of the efficiency status
  - Automatic long-term measurements (e.g. batch, shift)
  - Efficiency report (.csv) for data evaluation and documentation
- Support of Sentron PAC 3200/4200 configured using the Hardware Catalog (MDD) – previously only GSDML was supported.

#### SIMATIC TIA Portal Openness

- Openness DLLs of V14SP1 and V15 in scope of delivery  
  Because the Openness DLLs of V14SP1 and V15 are included in the scope of delivery, applications based on V14SP1 also run in V15 without modification. To make use of the functions of V15, you must integrate the DLL of V15 and recompile the application
- Export and import of SCL blocks  
  Both SCL blocks as well as LAD and FBD blocks with SCL networks can be exported and imported as XML.
- PLC download  
  The download of standard S7-1500 PLCs can be automated. A stop and start of the PLC is implicitly performed for this. Protection level passwords and binding passwords can be transferred from the application.
- Reading a checksum  
  The checksum of the standard PLC program can be read from an offline PLC.
- ProDiag  
  FBs, instances and assignments for ProDIAG can be created.
- System folder for UDTs  
  System UDTs can be accessed in the system group within the user data types.
- Block numbering  
  The automatic block numbering can be switched on and off. In addition, block numbers can be changed.
- Technology objects  
  Openness includes enhancements for downloading and saving data of the TO Plotter and for new TO features.
- Startdrive  
  DriveObjects and frames can be created for the SINAMICS G120 and SINAMICS S120 drives. Selected drive parameters can be set online and offline. Downloading to the device is possible.
- SINAMICS in AutomationML  
  V90 slaves and SINAMICS G120 Profinet head modules can be exported and imported using AutomationML.

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic/Advanced V15, the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V15.

- Fail-safe arrays (read) for data types INT and DINT

  Safety V15 provides new instructions for reading fail-safe integer and double integer values from fail-safe arrays.  The arrays can be created in global fail-safe data blocks (F-global DBs) and may contain up to 10,000 elements of the data type INT or DINT.

  The array elements are accessed with the instructions RD_ARRAY_I or RD_ARRAY_DI. The instructions are available for the fail-safe S7-1500 CPUs.
- Hardware and software signatures

  The F-collective signature uniquely identifies a particular status of the safety program and the safety-relevant parameters of the F-CPU and F-I/O.

  In addition to the F-collective signature, with Safety V15 you receive additional information regarding the fail-safe software and hardware signatures for the fail-safe S7-1200 and S7-1500 CPUs. These additional signatures enable a better differentiation between hardware- and software-relevant changes, thus simplifying the acceptance of changes.

  The F-signatures are displayed in the Safety Administration Editor (SAE) and are part of the Safety printout.
- Overflow handling

  When converters or mathematical functions such as additions, multiplications etc. are used, there is the possibility of a range overflow, which is detected by fail-safe processing and results in a STOP of the CPU.  
  This STOP can be prevented by reliable overflow handling.  
  Fail-safe S7-300 / S7-400 CPUs require the placing of a corresponding overflow instruction "Query status bit OV" in the following network.  
  Overflow handling can be programmed considerably easier and by analogy with the STEP 7 Standard for the fail-safe S7-1200 / S7-1500 CPUs.  
  Overflow handling is programmed and a STOP of the CPU in the event of an overflow can be prevented just by wiring the enable output ENO. If the result of the instruction is outside the range permitted for the data type, then the enable output ENO returns the signal state "0". The result of the instruction then behaves like the corresponding instruction in a standard block.

  Overflow handling is supported for the following instructions:

  - ADD: Add
  - SUB: Subtract
  - MUL: Multiply
  - DIV: Divide
  - NEG: Create two's complement
  - ABS: Form absolute value (S7-1200, S7-1500)
  - CONVERT: Convert value
- Isochronous fail-safe OB

  The isochronous F-OBs of Safety V15 enable the connection of isochronous PROFIsafe devices such as SINAMICS S120 (as of FW V5.1) for minimum response times and jitter.

  Requirement: F-CPUs S7-1500 firmware version 2.0 and higher that support IRT.
- Usability improvements

  With V15, Safety Basic / Advanced offers a number of usability improvements which simplify the creation of fail-safe user programs:

  - Readback of fail-safe F-FB Out tags also on S7-1200 and S7-1500 CPUs
  - Writing of F-FB input tags analogous to the STEP 7 standard
  - Start values of instance DBs can be changed
- Other innovations

  - The monitoring of system-integrated F-IO-DBs and F-runtime group information DBs using ProDiag is supported.
  - DINT -&gt; INT converter (S7-1200, S7-1500)
  - ABS: Form absolute value (S7-1200, S7-1500)

---

**See also**

[SIMOCODE ES](#simocode-es-2)

### Runtime options

#### Description

The following new options are only offered as a runtime option with the TIA Portal. ProDiag is already integrated into the existing STEP 7 and WinCC products and only needs to be licensed when used on the real hardware. Unlike the engineering options, the runtime options are not version-dependent.

#### SIMATIC ProDiag

- S7 GRAPH blocks as of version 5.0 allow GRAPH step and GRAPH transition names to be compiled, as well as the initial values of interlocks and transitions to be reset.
- Improvements for multiple selection in global data blocks, function blocks and tag tables

  - New monitoring functions added, even when the multiple selection contains non-Boolean elements
  - Deletion includes all monitoring functions, even if an element contains more than one monitoring function
  - All the properties of the monitoring function are included in copying when a monitoring function is copied. During insertion, new monitoring functions are created with the copied properties and existing monitoring functions are overwritten. If an element contains several monitoring functions, these are deleted and one or more new monitoring functions with the copied properties are created.
  - During automatic filling of the cells, new monitoring functions are created in the marked cells of a global data block or of a function block and the properties of the selected monitoring function(s) are applied.
- Within the tag table, the FB block interface or global data blocks the "Monitoring" column displays how many monitoring functions the absolute address contains.
- The global search now also finds the ProDiag texts of the created monitoring functions from the Inspector window, from the ProDiag function blocks and from the ProDiag monitoring functions.

#### OPC UA

For S7-1500 CPUs firmware V2.5 and higher, with a corresponding Runtime license you can benefit from the following expansions of the integrated OPC UA server:

- Methods can be provided via the user program of an S7-1500 CPU. These methods use OPC UA clients in order, for example, to process a manufacturing order via the method call by the S7-1500 CPU.
- Import of standardized OPC UA information models (companion specifications). For this, you use the uniform interfaces for a large selection of devices or machines - e.g. for modeling of RFID readers or injection molding machines. Examples of this are the companion specifications AutoID and Euromap 77.

## What's new in TIA Portal V14 SP1

This section contains information on the following topics:

- [Introduction](#introduction-1)
- [SIMATIC STEP 7](#simatic-step-7-6)
- [SIMATIC WinCC](#simatic-wincc-6)
- [SINAMICS Startdrive](#sinamics-startdrive-6)
- [Engineering options](#engineering-options-6)
- [Runtime options](#runtime-options-6)

### Introduction

#### Description

All important new features compared to the present version V14 are summarized here. You can find additional details on the various topics in the individual sections of the product documentation.

### SIMATIC STEP 7

#### Description

All important new features of STEP 7 are shown grouped together based on the engineering workflow.

#### Hardware configuration

- New PS 60W 24/48/60VDC HF system power supply for the S7-1500 provides an energy buffer for data backup of up to 20 MB in the CPU.
- Tabular configuration of the I/O channels for modules of the ET 200MP DI HF and ET 200MP DO HF including copy-and-paste and auto-complete function
- Editing of devices names in the graphic views
- Enhanced zooming and optimized (multiple) selection in the graphic network and topology view
- Overview of I/O tags of an entire device (such as an ET 200SP station)
- Easy removal of unused GSD files in the project
- Wizard enhancement for UDP Multicast for Open User Communication (OUC) with S7-1500

#### Editors for programming languages

- In SCL program code structured tags and ARRAY elements can be replaced by other tags using drag-and-drop operation.
- In the SCL editor, it is possible to switch between insert and overwrite mode.
- In SCL, selected program code segments can be simply enclosed with specific structure elements, such as "IF..Then".
- The detailed comparison of individual blocks can be started directly from the project tree (offline/offline, but also online/offline).
- In LAD/FBD, the tag comment can be shown directly at the point of use.
- The F7 functions ("Open block/PLC data type…") can also be started with focus inside editors.
- Generating external source file from blocks: The export of objects as external source file takes into consideration the PLC data types (UDTs), multi-instances and all called blocks defined in the block interface.
- All the PLC instructions used can be updated to the latest version release in the "Instructions" task card.

#### New instructions

- The values can be moved between tags of the data type BYTE, WORD, DWORD, LWORD and tag ARRAYs of the data type BOOL using the new instructions "SCATTER" and "GATHER" for the S7-1200/1500. As a result, control and status words can, for example, be simply broken down into single bit signals and reassembled.
- Information about the inserted SIMATIC memory card - such as the memory size, the amount of storage space used or the number of already completed write/delete actions (as percentage) – can be read out using the "GetSMCInfo" instruction.
- The "Polyline" instruction maps the input value to the output value using a characteristic curve. The characteristic curve is defined as a polyline (with up to 50 interpolation points).

#### Language innovations

- PLC data types (UDT) and ARRAY comments can be modified instance-specific.
- The assignment of various PLC data types (UDTs) with the same structure but different symbolic names is supported.
- S7-GRAPH blocks as of version 4.0 enable the initial value acquisition of the disturbed operands. The actual values of the signal states of Boolean operands and the results of comparator operations in interlocks and transitions are recorded continuously from the time of activation of the initial value acquisition, even if no error occurs. The signal states are stored for each cycle in the GRAPH instance data block. A maximum of 32 signal states are recorded per interlock or per transition of a GRAPH step.

#### Libraries

- Project libraries and global libraries can now be separately translated into additional foreign languages.
- Simplified upgrading of types (blocks, PLC data types) in an existing project library.
- The user-defined help can be now also be started in the context of the project language. Until V14, this was only possible in the context of the TIA Portal language.

#### Messages/diagnostics

- The display of the alarm display in the Inspector window has been optimized and functionally enhanced with new functions such as "Receive alarms" and "Freeze alarms".

#### Migration

- The local constants for ARRAY limits that are used in the SCL sources are retained during the migration from STEP 7 V5.x to TIA Portal.

#### Trace

- Switching the display format (for example: A WORD can be shown in hexadecimal format, as signed or unsigned INT)
- The scroll bar of the X axis has a small preview window ("Time range display"), with which you can recognize which are has just been zoomed.

#### System functions

- CAx data based on XML, for exchange of ECAD system for example, can be exported and re-imported.
- Filters are supported for cross-references that are freely definable by the user, for example, in order to find multiple accesses to tags.
- The TIA Portal can be connected to an external password manager via a password provider. This offers the advantage that passwords do not have to be released. This increases the security of the program code.

#### SIMATIC Ident

The technology object (TO) for SIMATIC Ident connects the hardware configuration of communication modules and readers to the programming of an S7-1200 and S7-1500 controller. The TO hereby prevents incorrect settings and detects errors in the parameter assignment.

Hardware configuration:

- The plant builder assigns a "unique name" to each communication module / reader with which it can be identified by both commissioning engineers and programmers.
- The parameter assignment of each communication module, reader or reading point is set via the TO.
- The Ident devices can be configured with a single click for operation with the TO using the "Auto Configuration" button.

New instructions:

- All instructions for SIMATIC Ident have been revised for the collaboration with the TO. You can find the instructions in the TIA Portal under "Optional packages" &gt; "SIMATIC Ident".
- The hardware addressing of a reader to the instructions has been changed so that the reader is selected through the "unique name" which was defined in the TO. There is no need, therefore, for the previous searching, noting and transferred of the HW identifier and logical address.
- Optional inputs at the instructions are hidden. The user thus recognizes immediately the important parameters that are required for a function.
- The programmer no longer has to assign parameters to the hardware. Only the RESET_READER instruction, which has no other input parameters, is needed for the PLC startup, regardless of the reader connected. The instruction acquires the required parameters from a data area which was configured with the TO.

Diagnostics:

- The last messages which were reported by the instructions to the application can be displayed with the TO.
- A time stamp and the exact error text help to achieve fast analysis of the error.

### SIMATIC WinCC

#### Function enhancement - Openness

- Support of HMI faceplates
- Support of HMI slide-in screens
- Support of HMI pop-up screens

#### Enhancements for SIMATIC HMI panels

- SIMATIC HMI BASIC Panels:

  - Unicode CSV export of recipes for Basic Panels
  - Changing of IP addresses of controllers and additional SIMATIC components (such as CPs) via the HMI device.
  - Support for Chinese, Japanese, Korean, Russian and Arabic fonts in the browser.
- Updating of tested network cameras (AXIS M1013, AXIS M1011, D-Link DCS-942L, D-LINK 4701E, Siemens CCMS2025).
- Installation/deinstallation of Word, Excel, Win Mediaplayer, IE via ProSave.
- Unlimited number of usable scripts for Comfort.
- Configuration for Startup (additional value "60s" for RT start time and system function for Restart Panel).
- Additional system functions in the "Zones" editor for Mobile Panels.

#### Enhancement for SIMATIC Runtime Advanced

- Camera displays for showing live video streams from network cameras
- Enhancements of the PDF display (search and copy)
- License-free use of the Sm@rtServer on Runtime Advanced (similar to Comfort Panels)

#### Integration of SINUMERIK Operate (GUI and data) in Runtime Advanced

- Access to SINUMERIK Operate user interface via new NC operator display in screens of RT Advanced (also multitouch operation)
- Access to SINUMERIK NCU data via separate SINUMERIK channel

#### Enhancements for SIMATIC Runtime Professional

- Support for OPC UA DA client
- New VBS methods for screen windows. This provides you with the option of temporarily switching off the operability of the screen window.
- Customization of the recipe view. This provides you with the option of adapting the properties of the controls (buttons or table elements).

### SINAMICS Startdrive

#### Startdrive for G120

- Optimized and enhanced commissioning wizard:

  - The two former wizards for the standard commissioning and the operation under a SIMATIC Motion Control axis are combined in a single wizard
  - Integration of the selection of message frame, brake resistor, motor-side filter, temperature sensor, and selection of the motor, also via the motor code number
- Online/offline parameter comparison
- Support for Windows 10

#### Startdrive option for S120

- Automatic hardware configuration
- Support for drive-based extended safety with graphic parameterization masks
- Support for torque motors (1FW3, 1FW6)
- Networking with ET200 SP CPU
- Support for Windows 10

### Engineering options

#### SIMATIC STEP 7 Safety

SIMATIC STEP 7 Safety Basic/Advanced V14 SP1, the high-performance option package for programming fail-safe S7 controllers for the Totally Integrated Automation Portal V14 SP1.

- Station upload

  The consistent hardware and software upload enables a loading of project data (including safety-related project data) from a fail-safe S7-1500 CPU*) to a programming device / PC. The project data are loaded without an additional generation step and are consistently available in the TIA Portal for immediate continued work.

  *) As of firmware version V2.1
- Configuration control

  With Safety V14 SP1, the configuration control (option handling) for SIMATIC fail-safe I/O devices is supported in the following configurations:

  - Distributed in an F-CPU S7-300/400/1200/1500
  - Centrally in an F-CPU S7-1500 (including fail-safe ET200SP CPUs)
- Cross-project IO controller I-device communication

  Safety V14 SP1 enables cross-project communication of fail-safe S7-1200/1500/1500 software controllers with S7-300/400/1200/1500 I-devices. The I-device project can be easily created with STEP 7 Safety V13 (or higher) or also S7 Distributed Safety V5.4, exported as GSD file, and imported into the IO controller project.
- Global F-IO Status block

  Fail-safe F I/O devices provide a wide range of status information about the status of the channel and module using the QBAD tags and the value status bits.

  In the Safety Administration editor, you can create a default FB for each F-runtime group in order to record and further process any channel, communication or fail-safe I/O errors, even in automation systems with very large volumes of project data. The value status bits and the QBAD tags of the fail-safe I/O used in the corresponding F-runtime group are evaluated and the result of the evaluation is made available at the "QSTATUS" output.

  You can use the default FB in the standard program.
- Openness

  You can use the Openness command set in STEP 7 Safety, as in the standard version. This requires that no password is set for the safety-relevant project data. The use of Openness in production operation is not permitted.

  Supported functions include the following:

  - Working with libraries (deleting, copying, instancing and upgrading elements etc.)
  - Importing tags, tag tables, PLC data types (UDTs), etc.
  - Compiling of SW, blocks, PLC data types (UDTs).
  - Plugging/deleting F-CPUs and fail-safe I/O
  - Copying/deleting F-CPUs and fail-safe I/O from master copies
  - Configuring networks
  - Compiling software (including the safety program)
  - Reading/configuring F-parameters of the F-CPU
  - Reading/configuring F-parameters of the fail-safe I/O
  - Reading, declaring or deleting fail-safe tags in the PLC tag table
  - Updating the project to the latest type versions of F-blocks

#### SINUMERIK STEP 7 Toolbox

The SINUMERIK STEP 7 Toolbox V14 SP1 is an option package for SIMATIC STEP 7 Professional V14 SP1 (TIA Portal) with additional setup.

The SINUMERIK STEP 7 Toolbox V14 SP1 enables the configuration of the SINUMERIK hardware in the TIA Portal through the following functionalities and tools:

- Addition of the following modules of SINUMERIK 840D sl to the hardware catalog (as of firmware V4.5 SP2):

  - NCU 710.3B
  - NCU 720.3B
  - NCU 730.3B
  - NX10.3
  - NX15.3
- Addition of the ADI4 module to the hardware catalog
- Basic SINUMERIK PLC program for the versions

  - V4.5.x.x
  - V4.7.x.x
  - V4.8.x.x

    The basic PLC program is installed in the form of the "SINUMERIK 840D sl PLC Basic Program" system library using the SINUMERIK STEP 7 Toolbox V14 SP1.

- Support for hardware migration
- Creation of SINUMERIK PLC commissioning logs, PLC hardware upgrade logs and reload logs
- Export of PLC symbols for SINUMERIK Operate
- Import of SINUMERIK user alarm texts
- Creation of SINUMERIK PLC logs
- Support of PROFINET IO IRT for NCK
- Support of SINUMERIK Safety Integrated and Safety Integrated plus
- NC-VAR-Selector (external tool)

### Runtime options

#### Description

The following new options are only offered as a runtime option with TIA Portal V14 SP1. The ProDiag product is are already integrated into the existing STEP 7 and WinCC products and only needs to be licensed when used on the real hardware. In comparison with the Engineering options, the runtime options are not version-dependent.

#### SIMATIC ProDiag

- S7-GRAPH blocks as of version 4.0 enable the initial value acquisition of the disturbed operands.
- The initial values can be displayed on the HMI device using the "PLC code view" object and the faulty operands can be detected immediately in the case of error (criteria analysis). The initial values remain stored until they are overwritten by a new error.
- For the initial value acquisition, all instructions are supported which are supported in an S7-GRAPH function block for transitions and interlocks. For bit logic operations, the status of the operand is stored. For comparator operations, the result of the comparison is stored.

#### SIMATIC Energy Suite S7-1500

SIMATIC Energy Suite as an integrated option for the TIA Portal for the first time efficiently combines energy management with automation, bringing energy transparency to production. In addition, the configuration work is significantly reduced due to the simplified configuration of components for energy recording.

Functions:

- Integrated and intuitive configuration of energy management
- Automatic generation of the PLC energy program for S7-1500 for basic energy data (energy and power)
- Archiving to WinCC Runtime Professional or to a PLC-internal SIMATIC memory card
- Seamless connection to SIMATIC Energy Manager PRO

New in V14 SP1:

- Enhancement of the automatic PLC program generation with additional energy data (currents, voltages, frequency)
- In addition to the manual energy data export, the automatic export is now also offered (for example, start of the export of the energy data of the last week, each Monday at 00:15 hrs)
- Program generator: Detailed representation of the generation progress and configuration error messages.

## What's new in TIA Portal V14

This section contains information on the following topics:

- [Introduction](#introduction-2)
- [SIMATIC STEP 7](#simatic-step-7-7)
- [SIMATIC WinCC](#simatic-wincc-7)
- [SINAMICS Startdrive](#sinamics-startdrive-7)
- [SIMOTION SCOUT TIA](#simotion-scout-tia)
- [SIMOCODE ES V14](#simocode-es-v14)
- [Engineering options](#engineering-options-7)
- [Runtime options](#runtime-options-7)

### Introduction

#### Description

All important new features compared to the present version V13 SP1 are summarized here. You can find additional details on the various topics in the individual sections of the product documentation.

### SIMATIC STEP 7

#### Description

All important new features of STEP 7 are shown grouped together based on the engineering workflow.

#### Hardware configuration

- Support of the S7-1500 T-CPU family, with the Motion Control functions "constant velocity" and "cam disks".
- Support of the new CPU 1518(F)-4 PN/DP ODK (Open Development Kit), which enables C/C++ functions created via the SIMATIC ODK 1500S to be integrated into the user program
- Support of the CPU 1516pro (F)-2 PN
- Support of the new S7-1500 failsafe software controller
- IO devices can be grouped in the project tree to quickly find and technologically merge devices.
- The arrangement of the devices in the topological view can be synchronized with the network view.
- Own profiles can be defined in the hardware catalog for easy and quick access to frequently used modules.

#### Editors for programming languages

- Separate editors are available for the new technology objects Output Cam, Cam Track and Measuring Input. There is also a convenient cam disk editor for the S7-1500T controllers.
- SCL networks can be inserted into a LAD/FBD block.
- "Regions" can be used in SCL program code to improve structuring and navigation.
- You can hide the block parameters when calling the block in LAD or FBD.
- The comparison of PLC programs has been thoroughly revised and enables the quick and convenient comparison of source code with many filter options.
- Networks in the programming editors for LAD / FBD / STL are automatically displayed as they were when you last exited the block.

#### Language innovations

- ARRAYs of variable length can be passed with ARRAY[*].
- Multiple instances can be declared in ARRAYs in the block interface and called in loops. This helps to significantly reduce the program code and provides better readability and more efficient programming when processing the same program objects.
- The data type DB_ANY can also be used for technology objects. This allows technology objects to be handled more flexibly in the program. An "ARRAY of DB_ANY" may be a list of positioning axes, for example.
- Instances can be passed as a parameter in the "InOut" section of the block interface so that only one dedicated instance needs to be selected in the call.
- Message texts and comments for up to 3 languages can be loaded into the PLC S7-1500 and changed online.

#### Messages/diagnostics

- Using the new "Get_Alarm" instruction, messages can be directly read from the message server of the S7-1500 CPU and, sent and to a higher-level reporting system (e.g. process control system), for example.
- With the instruction "GET_DIAG" in Mode 1, the diagnostic data are output in the DIS structure. Bit 15 of the parameter IOState of this structure outputs the signal status "1" when a network / hardware fault has occurred.

#### Trace

- The Trace function enables different measurements to be displayed in a shared diagram ("overlaid measurements").
- In addition, with the Trace function, after completion, messages can be stored on the memory card independently of the power supply, and if required, can be automatically restarted.

#### Online functions

- Restructuring of the toolbar in the DB editor with the possibility to reinitialize complete data blocks with the defined start values.
- Structures in the block can be observed directly in the Inspector window including the call environment.

#### System functions

- The new global search enables cross-project searching for PLC and HMI objects. In addition, the search results can be restricted by filter. A "GoTo" function is also available.
- TIA Portal settings can be exported or imported and stored on a central server. If the server path is available, for example, the stored settings are used automatically as "default" every time you restart the TIA Portal.
- Innovative help/information system with tab technology, improved search function and the possibility to filter information by device families.
- The new cross-reference list provides a quick overview of the use of objects and devices within the project.

  - Support of overlapping accesses (PLC tags)
  - Support of know-how-protected blocks
  - Access to Individual elements of an ARRAY
  - Representation of objects which occur both in HMI and PLC devices
  - Free entry of objects to be searched for in the cross-reference list possible
  - Various filter options
  - Convenient and central provision of updates in company networks.
  - A company server can be configured with the TIA Automation Corporate Configuration Tool. The available updates / support packages are stored on the server and are thus available to users.

#### S7-PLCSIM

- Quick start of S7-PLCSIM in compact mode and without a simulation project.
- Devices can be exchanged in the simulation project so that existing TIM tables and sequence entries can continue to be used without any problems.
- Sequences can be automatically started on the basis of a trigger condition.
- Sequences can be temporarily deactivate.
- Decentralized I/O devices can be simulated in the device view.

#### Motion Control applications

- Pre-configured and integrated connection and configuration of the SINAMICS V90 PN drive message to a Motion Control technology object of SIMATIC S7-1500.
- Automatic data synchronization between the controller and the drive.

---

**See also**

[Engineering options](#engineering-options-7)
  
[Runtime options](#runtime-options-7)

### SIMATIC WinCC

#### Configuring screens

- New view on distributed I/Os of the system diagnostic controls.
- Improvements of controls:

  - New scroll bar with configurable colors.
  - Dynamic number of commands in the drop-down menu for recipe control.
  - Expansion of the slider, bar, gauge controls with up to four limits.
- New "Siemens TIA Portal Icons" fonts.
- Graphics library includes new graphics and completely revised structure.

#### Working with tags

- Symbolic address multiplexing of PlcUDT instances within a ARRAY variable of a data block.
- Hierarchical IntelliSense for connecting PLC data to HMI tags.

#### SIMATIC Panels and SIMATIC WinCC Runtime Advanced

- Transfer of configuration via USB stick / SD card for Basic Panels 2ndGeneration, Comfort Panels, Outdoor Panels, Mobile Panels and WinCC Runtime Advanced.
- Sm@rt Server Option for Basic Panel 2nd Generation.
- The safety of the following features has been enhanced:

  - The following components are signed:

    Comfort and Mobile Panel: Runtime, ProSave options and Runtime add-ons.

    Basic Panels 2nd Generation: Image of the panel
  - Security of passwords used in Runtime
  - Web browser connection to a Sm@rtServer via HTTPS protocol possible and secure connection from a Web SmartClient to the Sm@rtServer possible.
- The maximum number of power tags in WinCC Runtime Advanced was increased to 16K.

#### WinCC Runtime Professional

- WebUX option

  Platform and browser-independent operation and monitoring via the Web.

- Process diagnostics option

  When a process fault occurs, process diagnostics provide information about the cause and location of the error and supports troubleshooting.

- Extension: Quantity structure for 1200/1500 PLCs

  There can now be 64 connections to S7-1200/1500.

- Extension: Multitouch for certain controls

  Gestures can now be used to move the display area of controls (trend-based controls, grid-based controls, axis controls).

- Harmonization: Licenses for WEBNAVIGATOR, DATAMONITOR and WebUX

  The license type of Web options can be counted consistently. These SCADA options as of V7.4 or V14 in the future will have uniform MLFBs and therefore there will no longer be separate MLFBs for Runtime Professional.

---

**See also**

[Engineering options](#engineering-options-7)
  
[Runtime options](#runtime-options-7)

### SINAMICS Startdrive

#### Simplified commissioning and simplified (remote) servicing

Extended routing functionality for communication between Startdrive and drive:

- Routing across various PROFINET systems
- Routing from PROFIBUS to PROFINET

#### Simple modification of a project to the machine

Upgrade G120 firmware version in the Startdrive project (beginning with firmware version 4.4)

#### Reuse of the parameter assignment across various performance ranges.

Also for G120C

#### Faster access to Smartdrive download package in SIOS

- No waiting time for export control
- Starting with the Startdrive V13 SP1, export restriction no longer applies (export identifier AL=N, ECCN=N)

#### More efficient configuration

Optimized compilation time of the S7-CPU for networked drives configured with Startdrive

#### Modification of the supplied S7 data blocks for drive control

Drive library now without know-how protection

#### Simplified commissioning

Assignment of PROFINET device names is now easy to do in the project navigation and in the HWCN network view via the shortcut menu of the drive.

#### Simplified update process

Automatic installation of Startdrive HSPs and updates via the TIA Portal Updater

#### Support for new hardware

New 1FP1 synchronous Reluktanz motors are supported.

#### No manual update required

HSPs for Sinamics Firmware V4.7.3 and V4.7.6 are integrated.

### SIMOTION SCOUT TIA

#### Description

The SIMOTION P platform (PC-based) is now available in the TIA Portal. (Planned for approx. 3 months after release of STEP 7)

- You can now upload the hardware configuration for SIMOTION devices.
- Additional PROFINET functions for SIMOTION devices:

  - Shared I-device
  - Shared device
  - Seamless Media Redundancy (MRPD)
  - "Check of VendorID/DeviceID" and "Overwriting of the NameOfStation" (automatic configuration of the topology)
  - Address tailoring (modular machines)

### SIMOCODE ES V14

#### Routing via Ethernet - PROFINET

SIMOCODE ES V14 supports routing to SIMOCODE pro devices with PROFINET. Devices can now also be reached from an engineering station with SIMOCODE ES V14 Premium via Ethernet, if they are not directly connected to the PROFINET network to which the SIMOCODE pro devices are connected. This improves the capabilities of the software in systems in which SIMOCODE pro devices are used with PROFINET.

#### Migration of SIMOCODE ES 2007 group files

Configurations created with SIMOCODE ES 2007 in which the parameter files for SIMOCODE pro devices have been assembled into "group files", can now be migrated directly to one and the same TIA Portal V14 project without additional configuration steps. This function improves the handling of the software when migrating from SIMOCODE ES 2007 to SIMOCODE ES V14 TIA Portal.

#### Improved editor functions for charts with SIMOCODE pro interconnections

With SIMOCODE ES V14 Standard and Premium, CFC-based charts can be copied in whole or part, saved as library elements and reused. This feature simplifies the handling of recurrent configurations for typical configurations.

#### Clear presentation of all the important parameter settings in the parameter editor

All important parameter settings for fast commissioning of a motor feeder can be displayed and edited in a new overview in SIMOCODE ES V14, which significantly helps to improve clarity.

#### Uniform presentation of recorded trends for measured values

Measured values and data recorded online and offline with SIMOCODE ES "Live Trend" and "Analog Value Recording" functions are displayed using the TIA Portal "Trace" function. The operation of this function has been significantly improved thanks to the TIA Portal-wide standardization.

### Engineering options

#### TIA Portal Multiuser

TIA Portal Multiuser Engineering enables several users to simultaneously work together on a project. This reduces configuration times considerably and enables quicker commissioning of projects.

The basic principle:

- An independent server application carries out project management. The server application can be installed independent of a TIA Portal.

  or

  project management is located on a server. The server can be installed independent of a TIA Portal.
- Different users work in local sessions, based on the projects managed by the server.
- Users work independently from each other in local sessions; changes made by other editors are displayed and can be applied.
- The changes from the local sessions are transferred to the server project on check-in.

#### TIA Portal Teamcenter Gateway

The TIA Portal Teamcenter Gateway allows you to store and manage TIA Portal projects and global libraries in the Teamcenter. The operation is performed in the TIA Portal.

#### TIA Portal Cloud Connector

The TIA Portal Cloud Connector lets you access local PG/PC interfaces and the SIMATIC hardware connected to them in the TIA Portal engineering even though the engineering itself is operated in a private cloud using Remote Desktop.

#### SIMATIC Energy Suite

SIMATIC Energy Suite as an integrated option for the TIA Portal for the first time efficiently combines energy management with automation, bringing energy transparency to production. In addition, the configuration work is significantly reduced due to the simplified configuration of components for energy recording.

- Integrated and intuitive configuration of energy management
- Automatic creation of PLC energy program for S7-1500
- Archiving to WinCC Runtime Professional or to a PLC-internal SIMATIC memory card
- Seamless connection to SIMATIC Energy Manager PRO

#### SIMATIC S7-PLCSIM Advanced

S7-PLCSIM Advanced is suitable for the simulation of an S7-1500 PLC. Compared to standard S7-PLCSIM, S7-PLCSIM Advanced provides the following additional features:

- API for interfacing with co-simulations
- Multiple, distributed instances possible
- Adjustable, virtual time
- Web server and OPC UA access

#### SIMATIC ODK 1500S

The SIMATIC ODK 1500S enables the development of function libraries with the high-level languages C/C++ for ODK-capable SIMATIC S7-1500 PLCs. These function libraries can be directly loaded and run directly from the user program. ODK-capable S7-1500 PLCs:

- S7-1500 Software Controller (CPU 1507S (F))
- ET 200SP Open Controller (CPU 1515SP PC (F))
- S7-1500 Advanced Controller (CPU 1518(F)-4 PN/DP ODK)

#### SIMATIC Target 1500S<sup>TM</sup> for Simulink®

SIMATIC Target 1500S<sup>TM</sup> for Simulink® is an add-on for Simulink from MathWorks. It enables the integration of Simulink models directly in the program cycle of an ODK-capable S7-1500 PLC.

- Enables model-based development with MATLAB® and Simulink for SIMATIC controllers
- Seamless integration in Simulink as a so-called target file
- No C/C++ or ODK know-how required
- Support of the Simulink external mode for direct monitoring and control of model parameters in the controller from Simulink
- The generated program code can be executed on the CPUs 1507S(F) V2.0, CPU 1515SP PC (F) V2.0 and CPU 1518(F)-4 PN/DP ODK.

#### SIMATIC Visualization Architect

The SIMATIC Visualization Architect (SiVArc) enables easy, fast and flexible automated production of HMI content based on the STEP 7 user program.

- Supported HMI devices:

  Comfort Panel, Mobile Panel 2nd Generation, WinCC RT Professional, WinCC RT Advanced
- Supported HMI objects:

  Screens, text lists, power tags, captions, buttons, I/O fields, symbolic I/O fields, graphic I/O fields, switches, round buttons
- Configuration via control editor
- Templates are managed through libraries

### Runtime options

#### Description

The following new options are only offered as a runtime option with TIA Portal V14. The products ProDiag and OPC UA S7-1500 are already integrated into the existing products STEP 7 and WinCC and only need to be licensed when used on the real hardware. In comparison with the Engineering options, the runtime options are not version-dependent.

#### SIMATIC ProDiag

SIMATIC ProDiag enables precise and fast machine and plant diagnostics for SIMATIC S7-1500 and SIMATIC HMI:

- Central cycle-precise time stamp of error messages
- Automatic generation of monitoring logic and message calls
- Automatic update of the SIMATIC HMI when changes are made to message configuration for 3 languages
- HMI systems do not have to leave runtime mode in the event of changes
- Is directly available in the language editors LAD, FBD, SCL and STL.
- Monitoring can be parameterized later on F blocks and know-how protected blocks
- Central project definition of message structure
- Alarm texts are automatically derived from existing information in the project
- Simple visualization of the HMI through prepared controls

#### SIMATIC OPC UA S7-1500

The OPC UA S7-1500 option allows easily connection of any third-party devices to the S7-1500 via the OPC UA server integrated in the S7-1500 CPU:

- OPC UA server directly in S7-1500
- OPC UA data access, read/write, subscription to value changes
- Security
- XML export for offline configuration of OPC UA clients

#### SIMATIC Energy Suite S7-1500

10 energy objects are supplied with the SIMATIC Energy Suite Engineering. Additional energy objects can be extended by the Runtime packages.

#### WinCC / WebUX

WinCC / WebUX allows us to monitor plant processes over the Internet or Intranet using mobile devices and if required, to also control them. The software offers a visualization solution which is suitable for HTML5 and SVG-capable browsers, independent of the operating system – and which does not require engineering work.

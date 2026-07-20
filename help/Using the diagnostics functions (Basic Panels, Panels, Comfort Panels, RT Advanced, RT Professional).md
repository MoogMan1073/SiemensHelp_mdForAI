---
title: "Using the diagnostics functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: DiagnosticsWCCPenUS
topics: 51
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the diagnostics functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-system-diagnostics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Monitoring functions for SIMATIC IPCs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#monitoring-functions-for-simatic-ipcs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](#supervising-machinery-and-plants-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)

## Monitoring functions for SIMATIC IPCs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Monitoring functions for SIMATIC IPCs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#monitoring-functions-for-simatic-ipcs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### Monitoring functions for SIMATIC IPCs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Hardware monitoring for SIMATIC IPCs

All SIMATIC IPCs support monitoring functions. Some of the monitoring functions can be displayed in the TIA Portal if you connect to the IPC online. The diagnostics editor provides information on operating states of the following groups:

- Fans
- Temperatures
- Voltages
- Drives/Storage media

The following figure shows an overview of all groups in the diagnostics editor.

![Hardware monitoring for SIMATIC IPCs](images/79207762187_DV_resource.Stream@PNG-en-US.png)

You can choose between the complete view and the single view in the diagnostics editor.

#### "Temperatures" group

The "Temperatures" group displays the temperatures of different components.

#### "Fans" group

The "Fans" group indicates the status of available fans (depending on the device). The speeds are given in revolutions per minute (rpm).

#### "Voltages" group

The "Voltages" group indicates the status of the available voltage sensors (depending on the device). The voltage of the CMOS battery is monitored. This sensor provides information about whether the voltage is OK, critical or faulty.

#### "Drives" group

The "Drives" group indicates the status of the available drives/storage media (depending on the device). The following storage media are supported here:

- ATA hard disks
- CompactFlash cards
- SCSI hard disks
- USB hard disks or USB sticks
- Hard disks of an INTEL RAID adapter

Information about whether each drive has S.M.A.R.T. capability and/or is a RAID drive is specified in the properties. Status information is displayed in this case.

#### Limits

High and low limits are defined for the two groups, Fans and Temperatures. The limits depend on the IPC and cannot be changed.

#### Color code

The icons next to each display object change color depending on the state of the object. The following applies to all groups:

- Green = OK
- Red = High or low limit violation or status of the object is critical.

#### Reaction to deviations

If there is a high or low limit violation or one of the groups has reached a critical state, an entry is triggered in the diagnostic buffer. At the same time, the icon color changes to red.

You can find additional information on the diagnostics functions of the IPCs in [SIOS Portal](https://support.industry.siemens.com/cs/de/en/view/39129913).

## Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics of supervision with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-supervision-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
- [Basics of supervising operands (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-supervising-operands-panels-comfort-panels-rt-advanced-rt-professional)
- [Requirements and licensing (Panels, Comfort Panels, RT Advanced, RT Professional)](#requirements-and-licensing-panels-comfort-panels-rt-advanced-rt-professional)
- [Visualizing supervisions (Panels, Comfort Panels, RT Advanced, RT Professional)](#visualizing-supervisions-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Visualization of the ProDiag functionality (Panels, Comfort Panels, RT Advanced, RT Professional)](#example-visualization-of-the-prodiag-functionality-panels-comfort-panels-rt-advanced-rt-professional)
- [Initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](#initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)

### Basics of supervision with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The TIA Portal ProDiag functionality is used for monitoring and identification of errors that occur in your plant or machine. You can use ProDiag to show the type of error, the cause of the error and the location of the error on the HMI device.

#### Use

You can use ProDiag functions to monitor your plant and to visualize it on an HMI device. The main objective of ProDiag is the reduction of downtime and loss of production after an error occurs, and the avoidance of errors using timely warnings. Diagnostic and display objects provide specific information for the user for troubleshooting and show the processes on an HMI device on site.

#### Principle

In STEP 7, you create operand supervisions and configure the settings according to your requirements. When an error occurs, a supervision alarm is generated based on the criteria you have configured. The configured supervision instances are stored in the preset ProDiag function block. You can use the automatically generated ProDiag FBs or create and configure your own ProDiag FBs.

You can use WinCC to visualize the ProDiag functions for display on an HMI device. You configure the screen objects which provide an overview of the current status of the plant and display the affected code or the step sequence when an error occurs.

### Basics of supervising operands (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Supervising operands

You can use a supervision to view the status of a Boolean tag. If an event occurs in your plant or machine, it triggers the configured supervision and the status of the operand is written to a ProDiag block in an error bit. The following types of supervision are available:

- Operand supervision
- Interlock supervision
- Action supervision
- Reaction supervision
- Position supervision
- Text message
- Error message

#### Categories and subcategories

You can define categories and subcategories for each supervision instance. You can use eight categories to classify occurring events according to their urgency. Subcategories are used to further subdivide information. You can combine categories and subcategories in a supervision instance.

You can find categories, subcategories and alarm texts for the supervision in the project tree under "Common data > Supervision settings". You can find more information about supervisions and categories in the chapter "Programming PLC > Supervising machinery and plants with ProDiag".

#### Tracking a supervision in HMI

Track the status of the configured supervisions in WinCC using the "ProDiag overview" object.

When an event occurs in your plant, the corresponding symbols of the supervision category and the type of supervision light up in the ProDiag overview. You jump directly to the error message or to the display if the affected network in the PLC code view via the configured buttons.

You display the status of the GRAPH sequencer of a GRAPH data block in the object "GRAPH overview". If a GRAPH supervision error occurs in one of the steps, the error symbol in the GRAPH overview lights up and the faulty step is highlighted visually.

With the object "PLC code view", you show the user program in the LAD, FBD and GRAPH programming languages on your HMI device.

The initial value acquisition and criteria analysis functions enable you to record the values at the time of the error and to quickly identify the operands with error with the "Criteria analysis view" object.

#### Advantages

ProDiag enables you to configure supervisions and monitor your plant without changing the user program code.

You carry out plant diagnostics on your HMI device. The data is automatically synchronized in order to keep the display on your HMI device always up-to-date.

You can find additional information on the integrated diagnostics of your machines and plants with SIMATIC ProDiag on the Siemens YouTube channel:

[Increased availability of your machines and plants with SIMATIC ProDiag](https://youtu.be/pri8m08g4Ak)

An application example for machine and plant diagnostics with ProDiag can be found in the Siemens Industry Online Support with Entry ID 109740151:

[Machine and plant diagnostics with ProDiag](https://support.industry.siemens.com/cs/ww/en/view/109740151)

---

**See also**

[Machine and plant diagnostics with ProDiag](https://support.industry.siemens.com/cs/ww/en/view/109740151)

### Requirements and licensing (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You configure the ProDiag supervisions in the TIA Portal using STEP 7 Professional and create the screen objects for the supervision and diagnostics using WinCC. You need a license to use the ProDiag functionality and the corresponding screen objects.

#### Software requirements

To configure ProDiag supervisions, you need the following products:

- TIA Portal STEP 7 Professional
- TIA Portal WinCC

  - Comfort/Advanced V14 or higher or
  - Professional V14 or higher

#### Hardware requirements

ProDiag functionality is available for CPUs of the S7-1500 series with firmware version 2.0 or higher.

The objects for the supervision and diagnostics of plants are available for the following HMI devices:

- Comfort Panels and KTP Mobile Panels*
- RT Advanced
- RT Professional

* The "PLC code view" object is available on Comfort Panels and KTP Mobile Panels from display size 7"

> **Note**
>
> Objects for supervision and diagnostics of plants can be used under the "Full access" and "Read access" protection levels configured in the CPU.
>
> ProDiag objects under the "HMI access" and "No access" protection levels cannot be used.

#### Licensing of ProDiag supervisions

The number of ProDiag supervisions that you configure using STEP 7 Professional is licensed. You do not need a license for the first 25 supervisions, licenses must be used for additional supervisions.

| Number of supervisions | <= 25 | <= 250 | <= 500 | <= 750 | <= 1000 | > 1000 |
| --- | --- | --- | --- | --- | --- | --- |
| Number of licenses | None | 1 | 2 | 3 | 4 | 5 |

#### Licensing of ProjDiag objects

To use the objects for the diagnostics and supervision in conjunction with the ProDiag supervision in your program, you need a ProDiag license.

### Visualizing supervisions (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Objects for the supervision and diagnostics of plants (Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-for-the-supervision-and-diagnostics-of-plants-panels-comfort-panels-rt-advanced-rt-professional)
- [Interaction of the objects for the supervision and diagnostics (Panels, Comfort Panels, RT Advanced)](#interaction-of-the-objects-for-the-supervision-and-diagnostics-panels-comfort-panels-rt-advanced)
- [Interaction of the objects for the supervision and diagnostics (RT Professional)](#interaction-of-the-objects-for-the-supervision-and-diagnostics-rt-professional)
- [Configuring the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-prodiag-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graph-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced)
- [Configuring the PLC code view (RT Professional)](#configuring-the-plc-code-view-rt-professional)
- [Correcting display problems in the PLC code view (Panels, Comfort Panels, RT Advanced, RT Professional)](#correcting-display-problems-in-the-plc-code-view-panels-comfort-panels-rt-advanced-rt-professional)

#### Objects for the supervision and diagnostics of plants (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC offers the following objects for displaying the current monitoring status and for fault diagnostics in the program code:

- ProDiag overview
- GRAPH overview
- PLC code view
- Criteria analysis view

##### ProDiag overview

The "ProDiag overview" object provides an overview of the current status of the configured supervisions.   
The ProDiag overview is available on Comfort Panels, KTP Mobile Panels, RT Advanced and RT Professional.

##### GRAPH overview

The "GRAPH overview" object is used to display the current program status for executed steps of the GRAPH sequencer.   
The GRAPH overview is available on Comfort Panels, KTP Mobile Panels, RT Advanced and RT Professional.

Keep in mind that you need a ProDiag license to use the "GRAPH Overview" object.

##### PLC code view

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH programming languages.

The PLC code view is available on Comfort Panels, KTP Mobile Panels (display size 7" or larger), RT Advanced and RT Professional.

##### Criteria analysis view

The "Criteria analysis view" object is used to display incorrect operands in the user program that were identified for a selected alarm by the criteria analysis.  
The criteria analysis view is available on Comfort Panels, KTP Mobile Panels, RT Advanced and RT Professional.

#### Interaction of the objects for the supervision and diagnostics (Panels, Comfort Panels, RT Advanced)

##### Introduction

With the objects for the supervision and diagnostics of plants, you have the following options:

- On a HMI device, you show the status of the supervisions configured in the user program
- Evaluate the current alarms and display the network that causes the alarms,
- Display the program code on the HMI device

Depending on the network, you display the following information on the HMI device:

- With the object "ProDiag overview" you display the current status of the ProDiag supervisions.
- With the object "GRAPH overview" you display the current status of the GRAPH sequencer.
- With the "Criteria analysis view" object, you display the incorrect operands for a selected GRPAH or ProDiag alarm.

##### Interaction of ProDiag objects

The figure below shows the interaction of objects for visualizing the ProDiag supervisions:

![Interaction of ProDiag objects](images/100835721867_DV_resource.Stream@PNG-en-US.png)

The visualization of the ProDiag functionality on the HMI device is comprised of the following actions:

1. Display program status

   - Display status of the supervisions with the ProDiag overview

     On the HMI device the connection is established to the PLC and the connected ProDiag FB and the current status of the supervisions is displayed. The corresponding symbol in the ProDiag overview lights up as soon as an event occurs.

     The "Alarm view" button allows you to jump to the alarm view or alarm window showing details on the event that occurred. To find the supervision-relevant alarms more easily in the alarm view/alarm window, it is recommended to use a filter to restrict the alarm shown.
   - Show sequence of the GRAPH sequencer using the GRAPH overview

     As soon as the connection is established to the PLC, the currently executed step of the GRAPH sequencer is shown in Runtime. Navigate to the next step or to the initial step of the sequencer using the operator buttons.

     The "Alarm view" button allows you to jump to the alarm view or alarm window showing details on the event that occurred.

     The "PLC code view" allows you to jump to the PLC code view, for example, to display an error in the execution of the GRAPH sequencer.
2. Display current alarms in the alarm view or in the alarm window

   Alarms that occur in Runtime are display in the alarm view or in the alarm window.

   > **Note**
   >
   > **Display of alarms of "Acknowledgement" and "No Acknowledgement" alarm classes**
   >
   > To display the supervision alarms of the system alarm classes or self-defined alarm classes in your alarm view or in your alarm window, enable the display of the these alarm classes in the Inspector window under "Properties > Properties > General".
   >
   > In the alarm view/alarm window the alarm classes of the supervision alarms can only be enabled after the supervisions have been configured and the PLC compiled.

   The system function "ActivatePLCCodeView" allows you to jump from the last active or a selected alarm to the PLC code view with the affected program code.

   In addition, the initial value acquisition and criteria analysis functions allow you to acquire the values at the time of the error and to output the incorrect operands in the program in the "Criteria analysis view" object.
3. Display program code in the PLC code view

   As soon as the connection has been established to the PLC, the PLC code view displays the current status of the network depending on the configuration:

   - In Runtime, the LAD/FBD network and the program code is displayed. The symbol names, absolute addresses of the symbols and corresponding comments are show in the symbol table.
   - In Runtime, the GRAPH sequencer is shown. In the detail view, the transitions of the steps are displayed.

   You have the option of configuring a button that changes its appearance in case of an error and allows you to jump to the configured PLC code view. To do so, specify a button and configure the system function "ActivatePLCCodeView" to it. Dynamize the appearance (e.g. background color) of the button using the control tag for PLC code view that you previously connected with the alarm view, so that the button changes its color, for example, in the event of an incoming ProDiag alarm.

##### Transfer of languages from CPU to HMI device

In the TIA Portal, the texts for the ProDiag functionality, for example, symbol names and comments in a PLC code view as well as the texts of the supervision alarms, are automatically loaded from the user program of the controller to the HMI device. In multi-lingual projects, make sure that the languages that are available in the PLC match the Runtime languages of the HMI device. The alarm texts on the HMI device can only be displayed in the desired languages if the languages match.

For more information on multilingual projects, refer to "Configuring devices and networks > Additional information on configurations > Functional description of S7-1500 CPUs > Setting the operating behavior > CPU properties > Multilingual capability".

#### Interaction of the objects for the supervision and diagnostics (RT Professional)

##### Introduction

With the objects for the supervision and diagnostics of plants, you have the following options:

- On a HMI device, you show the status of the supervisions configured in the user program
- Evaluate the current alarms and display the network that causes the alarms,
- Display the program code on the HMI device

Depending on the network, you display the following information on the HMI device:

- With the object "ProDiag overview" you display the current status of the ProDiag supervisions.
- With the object "GRAPH overview" you display the current status of the GRAPH sequencer.
- With the "Criteria analysis view" object, you display the incorrect operands for a selected GRPAH or ProDiag alarm.

##### Interaction of ProDiag objects

The figure below shows the interaction of objects for visualizing the ProDiag supervisions:

![Interaction of ProDiag objects](images/100835721867_DV_resource.Stream@PNG-en-US.png)

The visualization of the ProDiag functionality on the HMI device is comprised of the following actions:

1. Display program status

   - Display status of the supervisions with the ProDiag overview

     On the HMI device the connection is established to the PLC and the connected ProDiag FB and the current status of the supervisions is displayed. The corresponding symbol in the ProDiag overview lights up as soon as an event occurs.

     The "Alarm view" button allows you to jump to the alarm view or alarm window showing details on the event that occurred. To find the supervision-relevant alarms more easily in the alarm view/alarm window, it is recommended to use a filter to restrict the alarm shown.
   - Show sequence of the GRAPH sequencer using the GRAPH overview

     As soon as the connection is established to the PLC, the currently executed step of the GRAPH sequencer is shown in Runtime. Navigate to the next step or to the initial step of the sequencer using the operator buttons.

     The "Alarm view" button allows you to jump to the alarm view or alarm window showing details on the event that occurred.

     The "PLC code view" allows you to jump to the PLC code view, for example, to display an error in the execution of the GRAPH sequencer.
2. Display current alarms in the alarm view or in the alarm window

   Alarms that occur in Runtime are display in the alarm view or in the alarm window.

   > **Note**
   >
   > **Display of alarms of "Acknowledgement" and "No Acknowledgement" alarm classes**
   >
   > To display the supervision alarms of the system alarm classes or self-defined alarm classes in your alarm view or in your alarm window, enable the display of the these alarm classes in the Inspector window under "Properties > Properties > General".
   >
   > In the alarm view/alarm window the alarm classes of the supervision alarms can only be enabled after the supervisions have been configured and the PLC compiled.

   The system function "ShowPLCCodeViewFromAlarm" allows you to jump from the last active alarm or a selected alarm to the PLC code view with the affected program code.

   In addition, the initial value acquisition and criteria analysis functions allow you to acquire the values at the time of the error and to output the incorrect operands in the program in the "Criteria analysis view" object.
3. Display program code in the PLC code view

   As soon as the connection has been established to the PLC, the PLC code view displays the current status of the network depending on the configuration:

   - In Runtime, the LAD/FBD network and the program code is displayed. The symbol names, absolute addresses of the symbols and corresponding comments are show in the symbol table.
   - In Runtime, the GRAPH sequencer is shown. In the detail view, the transitions of the steps are displayed.

   You have the option of configuring a button that allows you to jump to the configured PLC code view in the case of an error. To do so, specify a button and configure the system function "ShowPLCCodeViewFromAlarm" to it.

##### Transfer of languages from CPU to HMI device

In TIA Portal V14, the texts for the ProDiag functionality, such as symbol names and comments in a PLC code view and supervision alarm texts, are automatically loaded from the PLC's user program to the HMI device. In multi-lingual projects, make sure that the languages that are available in the PLC match the Runtime languages of the HMI device. The alarm texts on the HMI device can only be displayed in the desired languages if the languages match.

For more information on multilingual projects, refer to "Configuring devices and networks > Additional information on configurations > Functional description of S7-1500 CPUs > Setting the operating behavior > CPU properties > Multilingual capability".

#### Configuring the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of the supervision configuration (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-the-supervision-configuration-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-prodiag-overview-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Configuring jump to the alarm view (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-jump-to-the-alarm-view-panels-comfort-panels-rt-advanced-rt-professional)

##### Overview of the supervision configuration (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In TIA Portal, configure ProDiag supervision functions in your user program in STEP 7 and configure the visualization for the HMI devices in WinCC.

###### Requirements

- An S7-1500 controller has been created.
- There is at least one Boolean tag, either in a data block, tag table or in a block interface.
- An HMI device has been created
- A screen has been created

###### Steps for configuring the supervisions with ProDiag

You configure the ProDiag functionality in the TIA Portal in the following steps:

**In STEP 7**

1. Create ProDiag function block for supervision.
2. Define settings at the ProDiag function block.
3. Defining the ProDiag supervision settings

   - Specify the type of supervision
   - Set the delay time
   - You select the conditions by which a supervision signal is triggered
   - Define the categories and subcategories
4. Add supervision for a Boolean tag.

   You create either global or a local supervision for a Boolean tag.
5. Call the ProDiag function block.
6. Compile and download the project

**In WinCC**

1. Insert the "ProDiag overview" object in the HMI screen.
2. Select a status tag.
3. Configure the display and the representation of the object in the settings.
4. Configuring the jump to the alarm view.

In addition, you can have the program execution in the "GRAPH overview" object displayed, as well as the current program status in the "PLC code view" object.

###### Assignment of symbols in the ProDiag overview

![Assignment of symbols in the ProDiag overview](images/164377566859_DV_resource.Stream@PNG-en-US.png)

The status tag "State" from the PLC data type "SV_FB_State" of the ProDiag function block contains the group error bits for the supervision types and categories that you visualize with the help of the ProDiag overview.

You can visualize two types of group error bit in the "ProDiag overview" object:

- Group error bit for supervisions (All, O, I, R, A, P, Merr, Mtxt)
- Group error bit for categories (C1 to C6)

The table below shows the assignment of the group error bits of the status tag "State" to the symbols in the ProDiag overview.

| ProDiag overview | Elements in ProDiag FB | Description |
| --- | --- | --- |
| **Symbols** |  |  |
| ![Assignment of symbols in the ProDiag overview](images/79044085515_DV_resource.Stream@PNG-de-DE.png) | All | Group error bit for all supervision types, excluding message text  If value of All = TRUE, at least one supervision was triggered and the symbol is visually highlighted in the ProDiag overview. |
| ![Assignment of symbols in the ProDiag overview](images/79043014283_DV_resource.Stream@PNG-de-DE.png) | SV_Types | Byte for all group error bits of the supervision types |
| Mtxt (message text) | Group error bit for all alarms |  |
| ![Assignment of symbols in the ProDiag overview](images/79043005195_DV_resource.Stream@PNG-de-DE.png) | - | Tooltip with information on this ProDiag overview |
| **Categories** |  |  |
| E (Error) | C1 (Category) | Error |
| W (Warning) | C2 (Category) | Warning |
| Categories | Group error byte for all categories. |  |
| I (Info) | C3 (Category) | Information |
| C4 to C6 | C4 to C6 (Category) | Additional categories |
| **Supervision types** |  |  |
| O | O (Operand) | Group error bit for operand supervisions |
| I | I (Interlock) | Group error bit for interlock supervisions |
| A | A (Action) | Group error bit for action supervisions |
| R | R (Reaction) | Group error bit for reaction supervisions |
| P | P (Position) | Group error bit for position supervisions |
| M | Merr (Message error) | Group error bit for error texts |

##### Configuring the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

ProDiag overview is used to monitor your machine or system at runtime and determination of diagnostics information in the event of a fault occurring.

Once you have set the status tag in the object and the connection to a ProDiag FB has been established, the status of the "State" status tag of the corresponding PLC data type is queried. In Runtime, the states of the monitored operands are represented as symbols in the ProDiag overview, similar to a traffic light colors.

In WinCC, you configure the display and the representation of categories and supervision types that are displayed in the "ProDiag overview" object independent of the supervision settings in STEP7.

###### Requirements

- At least one S7-1500 controller has been created.
- At least one supervision instance has been configured.
- A ProDiag FB and ProDiag DB are available.
- A PC station or an HMI device that supports the ProDiag functionality has been created.
- An HMI connection has been established between the controller and HMI device.
- An screen is created and the Inspector window is open.

###### Procedure

1. In the Inspector window, select "Properties > Properties > General".
2. Open the selection button under the "Tag" property.
3. Select the status tag of ProDiag FB.

   Alternatively, you can add the corresponding status tags from the detail view using drag-and-drop.

   ![Procedure](images/111975499659_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111975499659_DV_resource.Stream@PNG-en-US.png)
4. Under "Output > Categories", define the names and colors for the supervision categories.
5. Under "Output > Monitoring types", define the names and colors for the supervision categories.
6. Under "Layout", specify which icons and buttons are to be displayed in the object.
7. Select an authorization for operation under "Properties > Properties > Security".
8. You can configure a system function to the event "Alarm view button click" under "Properties > Events" to jump from the ProDiag overview to the alarm view in Runtime.

###### Result

The ProDiag overview is inserted in the screen. The current states for supervised events are displayed in Runtime.

##### Configuring jump to the alarm view (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

After an error has occurred, you have the option of jumping directly from the ProDiag overview to an alarm window or a screen with an alarm view.

###### Requirement

- You have created a screen.
- An alarm view or an alarm window has been created.
- The "ProDiag overview" object has been created.
- The Inspector window is open.

###### Configuring the jump to the alarm view

1. Click "Properties > Events" in the Inspector window.
2. Click on the event "Click alarm view button".
3. Select the "ShowAlarmWindow" system function under "<Add function".
4. Specify the object name of the alarm window.
5. Alternatively, open the screen with the configured alarm view using the "ActivateScreen" function.

   Specify the screen name of the screen that contains the configured alarm view.

###### Result

When you press the "Alarm view" button in the configured ProDiag overview, the screen with the corresponding alarm view or an alarm window opens automatically.

#### Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying the status of the GRAPH sequencer (Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-the-status-of-the-graph-sequencer-panels-comfort-panels-rt-advanced-rt-professional)
- [Show step history (Panels, Comfort Panels, RT Advanced, RT Professional)](#show-step-history-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graph-overview-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Configuring the operating mode (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-operating-mode-panels-comfort-panels-rt-advanced-rt-professional)

##### Displaying the status of the GRAPH sequencer (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

With the help of the "GRAPH Overview" object, you visualize the status of the GRAPH sequencer.

![Introduction](images/83654609931_DV_resource.Stream@PNG-de-DE.png)

① Error symbol

② Name of the GRAPH data block

③ Name of the currently executed step

④ Active step of the sequencer

- If an error occurs in a step, the step number is highlighted in red.

⑤ Operating mode

⑥"Step" button

- If the sequencer is in the last step, the "Initial step" button is displayed.

⑦ "Alarm view" button

⑧ Initial step symbol

⑨ "PLC code view" button

⑩ Simultaneous step symbol

###### Displaying the status of the GRAPH sequencer

You connect the GRAPH overview to the PLC via the GRAPH DB tag. After the connection has been established to the PLC, the object shows the step numbers of the steps of the GRAPH sequencer. The name of the currently executed step is shown below the sequencer. If there are additional simultaneous steps besides the currently executed step, the simultaneous step symbol lights up in the GRAPH overview.

Depending on the application, you can switch between the four operating modes for executing the GRAPH sequencer. The currently selected mode is displayed in the GRAPH overview.

If an error occurs during the execution of a step, the faulty step and the error symbol are highlighted visually.

In the case of error you have the option of jumping to the alarm in the configured alarm view or of viewing the affected program in the PLC code view.

###### Single-line mode

You have the option of displaying the GRAPH overview in the standard view or in single line mode. You can, for example, configure multiple GRAPH overviews in a screen. This provides you with the overview of the current status of multiple production areas, whose supervisions are summarized in the corresponding GRAPH FBs.

###### Display of steps and criteria analysis

In extended mode you activate the additional lines for display of previous and next steps as well as the first operand of the criteria analysis with errors.

![Display of steps and criteria analysis](images/165903532299_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#graph-overview-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graph-overview-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Configuring the operating mode (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-operating-mode-panels-comfort-panels-rt-advanced-rt-professional)
  
[Interaction of the objects for the supervision and diagnostics (Panels, Comfort Panels, RT Advanced)](#interaction-of-the-objects-for-the-supervision-and-diagnostics-panels-comfort-panels-rt-advanced)
  
[Initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](#initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)

##### Show step history (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You have the option of displaying the previous and next steps of the GRAPH sequence in addition to the current step in the GRAPH overview. For this, the active steps are internally recorded after a screen with a GRAPH overview is called. If an error occurs in a step, you see the actions that were executed before and after the step with an error.

You specify the multilingual step names displayed in the GRAPH overview in a multilingual text list in the user program beforehand.

![Introduction](images/165903532299_DV_resource.Stream@PNG-en-US.png)

###### Marking of the steps

The GRAPH sequencer is evaluated from left to right. The step numbers in the GRAPH overview are additionally marked to indicate whether a simultaneous or alternative branch is present directly before or after this step. This allows you to see the following information on the program flow at a glance:

- Plus sign

  - Previous step: a simultaneous branch is present before the active step. Multiple steps were active simultaneously.
  - Next step: a simultaneous branch is present after the active step. More than one step will be activated.
- Question mark

  - Previous step: A different step than the first (left) step of the sequence could have been active before the active step.
  - Next step: an alternative branch is present after the active step. As a result, a different step than the first (left) step of the sequence may also become activated.
- No character: the previous step or next step is uniquely determined.

> **Note**
>
> **Limitations affecting step determination**
>
> At the first call of the GRAPH overview, the previous and next steps are determined from the GRAPH block in the order of the programmed sequence.
>
> At the first call of the GRAPH overview and after a screen change, no recording of the active steps exists, and a unique determination of the previous steps is thus not possible.
>
> GRAPH overview updates the display at regular intervals. If the sequence is run through quickly or you manually switch between the steps frequently, a different step of the sequence than the step that was active may be determined.

###### Displaying previous and next steps

To display the previous and next steps in the GRAPH overview, select the "Previous and next step" option under "Properties > Appearance > Options".

###### Displaying the result of the criteria analysis

You have the option of displaying the result of the criteria analysis in the GRAPH overview when an error is present. The symbol name, the absolute address, the value of the first operand with error and the comment are displayed.

To display the first operand with error of the criteria analysis, select the "Criteria analysis" option under "Properties > Appearance > Options".

> **Note**
>
> No information will be output for the criteria analysis in the GRAPH overview in the following cases:
>
> - The version of the GRAPH block is older than V4.0.
> - The initial value acquisition was not activated in the block properties or the initial values were not acquired.
> - There is no error in the current step.

##### Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can use the GRAPH overview to view the current program status for the executed steps of a GRAPH sequencer.

###### Requirement

- A PLC including a GRAPH instance data block has been created.
- GRAPH instance data block contains at least one tag which is visible in HMI and accessible from HMI.

  > **Note**
  >
  > The process tag you are using for the GRAPH overview must be visible in HMI and accessible from HMI.
  >
  > To identify the tags of the GRAPH data block as visible and accessible for HMI, open the GRAPH function block, select the block in the work area, and select "Edit > Internal parameters visible/accessible from HMI" in the menu bar. Then compile the program blocks.
- An HMI device has been created.
- You have created a screen.
- The Inspector window is open.

###### Procedure

1. Drag the GRAPH overview from the toolbox view into the configured screen.
2. In the Inspector window, select "Properties > Properties > General".
3. Open the selection button under "Process > Tag".

   The "Add new object" dialog opens.
4. Select the corresponding PLC in the "Program blocks" folder.
5. Select the corresponding PLC tag of the GRAPH instance data block.
6. Under "Properties > Properties > Layout > Options", specify the symbols that are displayed in the GRAPH overview .

   To represent the GRAPH overview in compatibility mode without toolbar buttons and operating mode display, enable the "Single-line mode" property.

   ![Procedure](images/102982480779_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/102982480779_DV_resource.Stream@PNG-en-US.png)
7. Under "Properties > Properties > Toolbar > General", specify the buttons that will be displayed in the object.
8. You can dynamize the properties in the "GRAPH overview" object using tags and color-code the states.

   You can find a detailed description of dynamizing a property in the section [Dynamizing screens](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
9. Under "Properties > Events", you can assign system functions to the buttons in the GRAPH overview to jump to the alarm view and the PLC code view in Runtime.

**Note**

If no connection was configured between the HMI device and the selected PLC, a connection is set up automatically.

In addition, an HMI tag is created which is connected to the PLC tag.

###### Result

The GRAPH overview is inserted in the screen. The current status of the GRAPH step sequence is displayed in Runtime.

---

**See also**

[Displaying the status of the GRAPH sequencer (Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-the-status-of-the-graph-sequencer-panels-comfort-panels-rt-advanced-rt-professional)
  
[Dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring the operating mode (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

Four different operating modes are available for executing the GRAPH block:

- Auto (default setting)  
  Automatically switches to the next step when the transition is fulfilled.
- TAP  
  Automatically switches to the next step when the transition is fulfilled and there is an edge change from "0" to "1" at the T_PUSH parameter.
- TOP  
  Automatically switches to the next step when the transition is fulfilled or there is an edge change from "0" to "1" at the T_PUSH parameter.
- Manual  
  The next step is not automatically enabled when the transition is fulfilled. The steps can be selected and deselected manually.

> **Note**
>
> You set the operating mode by modifying the interface parameters of the GRAPH block in your control program.

> **Note**
>
> The name of the operating mode is language dependent and can be translated for the required Runtime languages.

In WinCC Runtime Professional you have the option of renaming the operating mode that is displayed in th GRAPH overview.

###### Configuring labels for the operating modes

A screen with the configured GRAPH overview is open.

1. In the Inspector window, select "Properties > Properties > Output".
2. Configure the labels for the four operating modes under "Output > Labeling".

#### Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced-1)
- [Views in the PLC code view (Panels, Comfort Panels, RT Advanced)](#views-in-the-plc-code-view-panels-comfort-panels-rt-advanced)
- [Configuring a view in the PLC code view (Panels, Comfort Panels, RT Advanced)](#configuring-a-view-in-the-plc-code-view-panels-comfort-panels-rt-advanced)
- [Supported instructions (Panels, Comfort Panels, RT Advanced)](#supported-instructions-panels-comfort-panels-rt-advanced)
- [Supported data types (Panels, Comfort Panels, RT Advanced)](#supported-data-types-panels-comfort-panels-rt-advanced)
- [Restrictions for the PLC code view (Panels, Comfort Panels, RT Advanced)](#restrictions-for-the-plc-code-view-panels-comfort-panels-rt-advanced)

##### Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)

###### Introduction

To display the PLC program networks in the LAD, FBD and GRAPH programming languages in Runtime, insert a PLC code view into your project.

###### Requirement

- At least one PLC has been created.
- An HMI device has been created.
- An HMI connection has been established between the controller and HMI device.
- "System diagnostics" has been enabled for the connection on all devices under "Runtime settings > Alarms".

  ![Requirement](images/159374355467_DV_resource.Stream@PNG-en-US.png)
- You have created a screen.

###### Procedure

1. Drag-and-drop the PLC code view from the toolbox view.
2. Click "Properties > Properties > Toolbar" in the Inspector window.
3. Select the buttons that you require in Runtime, for example: Next network, Previous network, Step mode.

   ![Procedure](images/111976014731_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111976014731_DV_resource.Stream@PNG-en-US.png)
4. If required, configure the button display, e.g. background color and fill pattern.
5. In the Inspector window, select "Properties > Properties > Columns".
6. Adapt the column headers or change the order if necessary.
7. Select an authorization for operation in "Properties > Properties > Security".

###### Result

The PLC code view is inserted in the screen. In Runtime, PLC user programs that are programmed in the LAD, FBD or GRAPH programming languages can be displayed.

##### Views in the PLC code view (Panels, Comfort Panels, RT Advanced)

###### Introduction

In the PLC code view you display various items of information about the user program:

- Information area
- Symbol table
- Detail view
- "Transition/Interlock view"
- Initial value/actual value view

###### Information area

The information area displays the LAD/FBD program code of your user program, and/or the GRAPH sequencer of a GRAPH function block. After the connection to the PLC has been established, the network status is displayed in the information area highlighted via the program code.

![Information area](images/96277646219_DV_resource.Stream@PNG-de-DE.png)

###### Symbol table

The symbol table displays the symbols that are used in the displayed network. The three columns of the symbol table display the symbol names of the tags, the absolute address and the comments. As the comments are loaded from the user program, these are displayed in the language that is stored in the PLC.

You can dynamically change the height and width of the symbol table in Runtime.

###### Detail view

The detail view is also available for displaying your GRAPH sequencer.

The detail view gives detailed information about the selected network and the pending errors. In the detail view you see, for example, the transition of the first active step of the GRAPH sequencer. Open the detail view in Runtime using the "Detail view" button.

![Detail view](images/96279941131_DV_resource.Stream@PNG-de-DE.png)

###### "Transition/Interlock view"

You have the option of switching between the transition and interlock views in the display of your user program. The transition/interlock view is available when the detail view is displayed.

To switch between the transition/interlock views in Runtime, use the "Transition/Interlock" button. When the button is enabled the interlock network is displayed, when disabled the transition network.

!["Transition/Interlock view"](images/96279944843_DV_resource.Stream@PNG-de-DE.png)

###### Initial value/actual value view

If you have activated actual value acquisition for the corresponding function block in the user program, you can switch between the initial value view and actual value view in the PLC code PLC code view. The actual value view uses the current values from the PLC and displays the current program status. The initial value view uses the values that were recorded at the time of the error and displays the operands with error and criteria. The operands with error are visually highlighted in the initial value view.

To switch between the actual values and initial values, use the "Initial values or actual values" button. When initial value acquisition is activated, the initial value view is displayed by default in the PLC code view after the jump.

In the initial value view, the operands with error are visually highlighted in Runtime in case of an error.

![Initial value/actual value view](images/102966340491_DV_resource.Stream@PNG-de-DE.png)

###### Buttons on the toolbar

The table below shows the buttons on the toolbar and their meaning.

| Operator control | Designation | Function |
| --- | --- | --- |
| ![Buttons on the toolbar](images/81241269643_DV_resource.Stream@PNG-de-DE.png) | "Symbol area" | Shows the symbol area. |
| ![Buttons on the toolbar](images/81241914123_DV_resource.Stream@PNG-de-DE.png) | "Previous network" | Navigates to the previous network |
| ![Buttons on the toolbar](images/81241278475_DV_resource.Stream@PNG-de-DE.png) | "Next network" | Navigates to the next network |
| ![Buttons on the toolbar](images/81241922571_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Enlarges the information area. |
| ![Buttons on the toolbar](images/81241931019_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Reduces the information area. |
| ![Buttons on the toolbar](images/81242387467_DV_resource.Stream@PNG-de-DE.png) | "Detail" | Shows the detail view. |
| ![Buttons on the toolbar](images/81242408715_DV_resource.Stream@PNG-de-DE.png) | "Step mode" | Switches between manual and automatic step selection for the active step. |
| ![Buttons on the toolbar](images/84248476683_DV_resource.Stream@PNG-de-DE.png) | "Transition or Interlock" | Switches between the transition and interlock network views. |
| ![Buttons on the toolbar](images/94991861387_DV_resource.Stream@PNG-de-DE.png) | "Actual values or initial values" | Switches between actual value view and initial value view. |

##### Configuring a view in the PLC code view (Panels, Comfort Panels, RT Advanced)

###### Introduction

The PLC code view also provides a split view of the display to show the GRAPH sequencer. You have the option of viewing the program and the associated details at a glance. Press "Detail view" to open the detail view in Runtime.

In WinCC, you can define the size ratio between the information area and the detail view.

###### Requirement

- You have created a screen.
- A PLC code view has been created in the screen.
- The Inspector window is open.

###### Define width of detail view

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Specify the width of the detail view in relation to the information area using the option "GRAPH detail view width (%)".

###### Result

The PLC code view is divided in two areas to represent the GRAPH sequencer in Runtime. The left-hand area shows the GRAPH sequencer and the right-hand area shows the detail view with the transition of the active step.

##### Supported instructions (Panels, Comfort Panels, RT Advanced)

###### Introduction

The "PLC code view" object supports instructions in the FBD and LAD programming languages.

###### Instructions

The following instructions are supported in the PLC code view:

- Bit logic operations
- Comparator operations
- Timers
- Counters

###### Bit logic operations

| Instruction | LAD | FBD |
| --- | --- | --- |
| Normally closed contact | ![Bit logic operations](images/84679344267_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84832530699_DV_resource.Stream@PNG-de-DE.png) |
| Normally open contact | ![Bit logic operations](images/84678899339_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84669425035_DV_resource.Stream@PNG-de-DE.png) |
| Set output | ![Bit logic operations](images/84677616779_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675946891_DV_resource.Stream@PNG-de-DE.png) |
| Reset output | ![Bit logic operations](images/84678069899_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675626635_DV_resource.Stream@PNG-de-DE.png) |
| Assignment | ![Bit logic operations](images/84678415755_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675280523_DV_resource.Stream@PNG-de-DE.png) |
| NOT: Invert RLO | ![Bit logic operations](images/84669420683_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84673684363_DV_resource.Stream@PNG-de-DE.png) |
| Negated contact | ![Bit logic operations](images/84678595467_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675562379_DV_resource.Stream@PNG-de-DE.png) |
| SR: Set/reset flip-flop | ![Bit logic operations](images/84677138315_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84676536203_DV_resource.Stream@PNG-de-DE.png) |
| RS: Reset/set flip-flop | ![Bit logic operations](images/84676856459_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84676164747_DV_resource.Stream@PNG-de-DE.png) |
| AND | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84672689291_DV_resource.Stream@PNG-de-DE.png) |
| OR | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84673159051_DV_resource.Stream@PNG-de-DE.png) |
| EXCLUSIVE OR | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84673274507_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

###### Comparator operations

| Instruction | LAD | FBD |
| --- | --- | --- |
| CMP ==: Equal | ![Comparator operations](images/84696480779_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698221835_DV_resource.Stream@PNG-de-DE.png) |
| CMP <>: Not equal | ![Comparator operations](images/84698273291_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698388747_DV_resource.Stream@PNG-de-DE.png) |
| CMP >=: Greater or equal | ![Comparator operations](images/84698414603_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698478859_DV_resource.Stream@PNG-de-DE.png) |
| CMP <=: Less or equal | ![Comparator operations](images/84698517515_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698556171_DV_resource.Stream@PNG-de-DE.png) |
| CMP >: Greater than | ![Comparator operations](images/84698594827_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698659083_DV_resource.Stream@PNG-de-DE.png) |
| CMP <: Less than | ![Comparator operations](images/84698684939_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698710795_DV_resource.Stream@PNG-de-DE.png) |

> **Note**
>
> PLC code view supports the following data types for displaying the comparator: Binary numbers, integers, floating-point numbers and timers with exception of S5TIME.

You can find additional information on this in the section "Programming PLC > Instructions".

###### Timers

| Instruction | LAD | FBD |
| --- | --- | --- |
| TP: Generate pulse | ![Timers](images/84701922315_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84698750475_DV_resource.Stream@PNG-de-DE.png) |
| TON: Generate on-delay | ![Timers](images/84704124171_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699045387_DV_resource.Stream@PNG-de-DE.png) |
| TOF: Generate off-delay | ![Timers](images/84704226827_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699199243_DV_resource.Stream@PNG-de-DE.png) |
| TONR: Time accumulator | ![Timers](images/84704252683_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699263755_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

###### Counters*

* Counters support the integer data types

| Instruction | LAD | FBD |
| --- | --- | --- |
| CTU: Count up | ![Counters*](images/84699290635_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84699559691_DV_resource.Stream@PNG-de-DE.png) |
| CTD: Count down | ![Counters*](images/84699777803_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84700085259_DV_resource.Stream@PNG-de-DE.png) |
| CTUD: Count up and down | ![Counters*](images/84700251915_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84700316171_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

##### Supported data types (Panels, Comfort Panels, RT Advanced)

###### Supported data types

The following table shows data types supported in the "PLC code view" object and their display formats:

| Data type | Length | Format |
| --- | --- | --- |
| **Binary numbers** |  |  |
| BOOL | 1 bit | Bool |
| BYTE | 8-bit | Hex |
| WORD | 16-bit | Hex |
| DWORD | 32-bit | Hex |
| LWORD | 64-bit | Hex |
| **Integers** |  |  |
| SINT | 8-bit | Dec |
| USINT | 8-bit | Dec |
| INT | 16-bit | Dec |
| UINT | 16-bit | Dec |
| DINT | 32-bit | Dec |
| UDINT | 32-bit | Dec |
| LINT | 64-bit | Dec |
| ULINT | 64-bit | Dec |
| **Floating-point numbers** |  |  |
| REAL | 32-bit | Floating point number |
| LREAL | 64-bit | Floating point number |
| **Timers** |  |  |
| TIME | 32-bit | Time |
| LTIME | 64-bit | LTime |
| **Date and time** |  |  |
| DTL** | 12 bytes | Date and Time |
| * Only with Boolean operands  ** Complete DTL structures are not supported. Only single elements of DTL structures are supported. |  |  |

> **Note**
>
> You can find more information on the data types under "PLC Programming > Data Types".

> **Note**
>
> The 64-bit PLC data types LINT, ULINT and LWORD are mapped to the HMI data type LREAL in the HMI channel. A loss of accuracy can be expected when the value exceeds the size 2^50.

##### Restrictions for the PLC code view (Panels, Comfort Panels, RT Advanced)

###### SCL

If you access a program network created with SCL the error code 4100 is displayed.

###### Operands and UDTs

Operands that are declared in the "#Temp" or "#InOut" area are generally not supported by the PLC code view. This applies both to elementary data types and to data types that are contained in UDTs. Data types of a UDT can be declared in the "#In" and "#Out" area and displayed in the PLC code view. The same limitations as for elementary data types apply to the data types of the UDT.

###### Restrictions to data types

The use of the data types STRING, WSTRING, CHAR, WCHAR, S5TIME results in the network not being able to be displayed in the PLC code view.

###### Use of 64-bit data types

The use of 64-bit data types may result in a slight loss of accuracy as these data types are mapped in the HMI channel to the data type Double. It is therefore possible that integer data types are displayed with decimal places.

###### Addressing of tags

Please note the following restrictions when addressing tags:

- The "PLC code view" object only supports symbolic addressing of tags. If the operand is not addressed symbolically, the network with the operand cannot be displayed and an error message is generated.
- The use of array elements with a tag as index is not supported, e.g. #myArray[MyTag]. Please use numerical values when addressing array elements, for example #myArray[6].
- Slice access enables you to address specific areas within declared variables. With Slice access, PLC code view only supports the access width "Bit" to Boolean tags.

###### Jump to the PLC code view

For the jump from a supervision alarm to the PLC code view, the instance name must conform to the following naming convention when using supported local operands in a function block: <FB-Name>_DB.

The jump to a function or an organization block is only possible if only global operands are used.

#### Configuring the PLC code view (RT Professional)

This section contains information on the following topics:

- [Configuring the PLC code view (RT Professional)](#configuring-the-plc-code-view-rt-professional-1)
- [Views in the PLC code view (RT Professional)](#views-in-the-plc-code-view-rt-professional)
- [Supported instructions (RT Professional)](#supported-instructions-rt-professional)
- [Supported data types (RT Professional)](#supported-data-types-rt-professional)
- [Restrictions for the PLC code view (RT Professional)](#restrictions-for-the-plc-code-view-rt-professional)
- [Configuring a jump from the alarm (RT Professional)](#configuring-a-jump-from-the-alarm-rt-professional)

##### Configuring the PLC code view (RT Professional)

###### Introduction

To display the PLC program networks in the LAD, FBD and GRAPH programming languages in runtime, insert a PLC code view in your project.

###### Requirement

- At least one PLC has been created.
- A PC station has been created.
- An HMI connection has been established between the controller and HMI device.
- "System diagnostics" has been enabled for the connection under "Runtime settings > Alarms".

  ![Requirement](images/159374355467_DV_resource.Stream@PNG-en-US.png)
- You have created a screen.
- The Inspector window is open.

###### Procedure

1. Drag-and-drop the PLC code view from the toolbox view.
2. Click "Properties > Properties > Layout" in the Inspector window.
3. Under "Layout > Symbol table lines", you adjust the number of lines that are displayed in the symbol table.
4. Click "Properties > Properties > Toolbar" in the Inspector window.
5. Assign a hotkey to the buttons that you need in runtime, e.g. Step mode.

   ![Procedure](images/110880907147_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/110880907147_DV_resource.Stream@PNG-en-US.png)
6. To display or handle errors when configuring the display of a network in runtime, configure a corresponding script under "Properties > Events > Errors".

###### Result

The PLC code view is inserted in the screen. In Runtime, PLC user programs that are programmed in the LAD, FBD or GRAPH programming languages can be displayed.

##### Views in the PLC code view (RT Professional)

###### Introduction

In the PLC code view you display various items of information about the user program:

- Information area
- Symbol table
- Detail view
- "Transition/Interlock view"
- Initial value/actual value view

###### Information area

The information area displays the LAD/FBD program code of your user program, and/or the GRAPH sequencer of a GRAPH data block. After the connection to the PLC has been established, the network status is displayed in the information area highlighted via the program code.

![Information area](images/111976683915_DV_resource.Stream@PNG-de-DE.png)

###### Symbol table

The symbol table shows the symbols that are used in the displayed network. The three columns of the symbol table display the symbol names of the tags, the absolute address and the comments. As the comments are loaded from the user program, these are displayed in the language that is stored in the PLC.

You can dynamically change the height and width of the symbol table in Runtime.

###### Detail view

The detail view gives detailed information about the selected network and the pending errors. In the detail view you see, for example, the transition of the first active step of the GRAPH sequencer. Open the detail view in Runtime using the "Detail view" button.

![Detail view](images/96280348939_DV_resource.Stream@PNG-de-DE.PNG)

###### "Transition/Interlock view"

You have the option of switching between the transition and interlock views in the display of your LAD/FBD user program. The transition/interlock view is available when the detail view is displayed.

To switch between the transition/interlock views in Runtime, use the "Transition/Interlock" button. When the button is enabled the interlock network is displayed, when disabled the transition network.

!["Transition/Interlock view"](images/111976742795_DV_resource.Stream@PNG-de-DE.png)

###### Initial value/actual value view

If you have activated actual value acquisition for the corresponding function block in the user program, you can switch between the initial value view and actual value view in the PLC code PLC code view. The actual value view uses the current values from the PLC and displays the current program status. The initial value view uses the values that were recorded at the time of the error and displays the operands with error and criteria. The operands with error are visually highlighted in the initial value view.

To switch between the actual values and initial values, use the "Initial values or actual values" button. When initial value acquisition is activated, the initial value view is displayed by default in the PLC code view after the jump.

![Initial value/actual value view](images/96277636619_DV_resource.Stream@PNG-de-DE.png)

###### Buttons on the toolbar

The table below shows the buttons on the toolbar and their meaning.

| Operator control | Designation | Function |
| --- | --- | --- |
| ![Buttons on the toolbar](images/83180944907_DV_resource.Stream@PNG-de-DE.png) | "Symbol area" | Shows the symbol area. |
| ![Buttons on the toolbar](images/83205324939_DV_resource.Stream@PNG-de-DE.png) | "Previous network" | Navigates to the previous network |
| ![Buttons on the toolbar](images/83205333771_DV_resource.Stream@PNG-de-DE.png) | "Next network" | Navigates to the next network |
| ![Buttons on the toolbar](images/83205457803_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Enlarges the information area. |
| ![Buttons on the toolbar](images/83205543435_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Reduces the information area. |
| ![Buttons on the toolbar](images/83205727499_DV_resource.Stream@PNG-de-DE.png) | "Detail" | Shows the detail view. |
| ![Buttons on the toolbar](images/83205552267_DV_resource.Stream@PNG-de-DE.png) | "Step mode" | Switches between manual and automatic step selection for the active step. |
| ![Buttons on the toolbar](images/83205800331_DV_resource.Stream@PNG-de-DE.png) | "Transition or Interlock" | Switches between transition view and interlock view. |
| ![Buttons on the toolbar](images/94991852555_DV_resource.Stream@PNG-de-DE.PNG) | "Actual values or initial values" | Switches between actual value view and initial value view. |

##### Supported instructions (RT Professional)

###### Introduction

The "PLC code view" object supports instructions in the FBD and LAD programming languages.

###### Instructions

The following instructions are supported in the PLC code view:

- Bit logic operations
- Comparator operations
- Timers
- Counters

###### Bit logic operations

| Instruction | LAD | FBD |
| --- | --- | --- |
| Normally closed contact | ![Bit logic operations](images/84679344267_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84832530699_DV_resource.Stream@PNG-de-DE.png) |
| Normally open contact | ![Bit logic operations](images/84678899339_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84669425035_DV_resource.Stream@PNG-de-DE.png) |
| Set output | ![Bit logic operations](images/84677616779_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675946891_DV_resource.Stream@PNG-de-DE.png) |
| Reset output | ![Bit logic operations](images/84678069899_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675626635_DV_resource.Stream@PNG-de-DE.png) |
| Assignment | ![Bit logic operations](images/84678415755_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675280523_DV_resource.Stream@PNG-de-DE.png) |
| NOT: Invert RLO | ![Bit logic operations](images/84669420683_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84673684363_DV_resource.Stream@PNG-de-DE.png) |
| Negated contact | ![Bit logic operations](images/84678595467_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84675562379_DV_resource.Stream@PNG-de-DE.png) |
| SR: Set/reset flip-flop | ![Bit logic operations](images/84677138315_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84676536203_DV_resource.Stream@PNG-de-DE.png) |
| RS: Reset/set flip-flop | ![Bit logic operations](images/84676856459_DV_resource.Stream@PNG-de-DE.png) | ![Bit logic operations](images/84676164747_DV_resource.Stream@PNG-de-DE.png) |
| AND | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84672689291_DV_resource.Stream@PNG-de-DE.png) |
| OR | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84673159051_DV_resource.Stream@PNG-de-DE.png) |
| EXCLUSIVE OR | Is implemented by the corresponding interconnection of normally closed contacts or normally open contacts. | ![Bit logic operations](images/84673274507_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

###### Comparator operations

| Instruction | LAD | FBD |
| --- | --- | --- |
| CMP ==: Equal | ![Comparator operations](images/84696480779_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698221835_DV_resource.Stream@PNG-de-DE.png) |
| CMP <>: Not equal | ![Comparator operations](images/84698273291_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698388747_DV_resource.Stream@PNG-de-DE.png) |
| CMP >=: Greater or equal | ![Comparator operations](images/84698414603_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698478859_DV_resource.Stream@PNG-de-DE.png) |
| CMP <=: Less or equal | ![Comparator operations](images/84698517515_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698556171_DV_resource.Stream@PNG-de-DE.png) |
| CMP >: Greater than | ![Comparator operations](images/84698594827_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698659083_DV_resource.Stream@PNG-de-DE.png) |
| CMP <: Less than | ![Comparator operations](images/84698684939_DV_resource.Stream@PNG-de-DE.png) | ![Comparator operations](images/84698710795_DV_resource.Stream@PNG-de-DE.png) |

> **Note**
>
> PLC code view supports the following data types for displaying the comparator: Binary numbers, integers, floating-point numbers and timers with exception of S5TIME.

You can find additional information on this in the section "Programming PLC > Instructions".

###### Timers

| Instruction | LAD | FBD |
| --- | --- | --- |
| TP: Generate pulse | ![Timers](images/84701922315_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84698750475_DV_resource.Stream@PNG-de-DE.png) |
| TON: Generate on-delay | ![Timers](images/84704124171_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699045387_DV_resource.Stream@PNG-de-DE.png) |
| TOF: Generate off-delay | ![Timers](images/84704226827_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699199243_DV_resource.Stream@PNG-de-DE.png) |
| TONR: Time accumulator | ![Timers](images/84704252683_DV_resource.Stream@PNG-de-DE.png) | ![Timers](images/84699263755_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

###### Counters*

* Counters support the integer data types

| Instruction | LAD | FBD |
| --- | --- | --- |
| CTU: Count up | ![Counters*](images/84699290635_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84699559691_DV_resource.Stream@PNG-de-DE.png) |
| CTD: Count down | ![Counters*](images/84699777803_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84700085259_DV_resource.Stream@PNG-de-DE.png) |
| CTUD: Count up and down | ![Counters*](images/84700251915_DV_resource.Stream@PNG-de-DE.png) | ![Counters*](images/84700316171_DV_resource.Stream@PNG-de-DE.png) |

You can find additional information on this in the section "Programming PLC > Instructions".

##### Supported data types (RT Professional)

###### Supported data types

The following table shows data types supported in the "PLC Code View" object and their display formats:

| Data type | Length | Format |
| --- | --- | --- |
| **Binary numbers** |  |  |
| BOOL* | 1 bit | Bool |
| BYTE | 8-bit | Hex |
| WORD | 16-bit | Hex |
| DWORD | 32-bit | Hex |
| LWORD | 64-bit | Hex |
| **Integers** |  |  |
| SINT | 8-bit | Dec |
| USINT | 8-bit | Dec |
| INT | 16-bit | Dec |
| UINT | 16-bit | Dec |
| DINT | 32-bit | Dec |
| UDINT | 32-bit | Dec |
| LINT | 64-bit | Dec |
| ULINT | 64-bit | Dec |
| **Floating-point numbers** |  |  |
| REAL | 32-bit | Floating point number |
| LREAL | 64-bit | Floating point number |
| **Timers** |  |  |
| S5TIME | 16-bit | SIMATIC_Timer |
| TIME | 32-bit | Time |
| LTIME | 64-bit | LTime |
| **Date and time** |  |  |
| DTL** | 12 bytes | Date and Time |
| * Only with Boolean operands  ** Complete DTL structures are not supported. Only single elements of DTL structures are supported. |  |  |

> **Note**
>
> You can find more information on the data types under "PLC Programming > Data Types".

> **Note**
>
> **Operands and UDTs**
>
> Operands that are declared in the "#Temp" or "#InOut" area are generally not supported by the PLC code view. This applies both to elementary data types and to data types that are contained in UDTs. Data types of a UDT can be declared in the "#In" and "#Out" area and displayed in the PLC code view. The same limitations as for elementary data types apply to the data types of the UDT.

> **Note**
>
> The upstream network must not contain any tags from the Temp or InOut section of an FB.
>
> The following data types may not be used for tags: STRING, WSTRING, CHAR, WCHAR, S5TIME

> **Note**
>
> The 64-bit PLC data types LINT, ULINT and LWORD are mapped to the HMI data type LREAL in the HMI channel. A loss of accuracy can be expected when the value exceeds the size 2^50.

---

**See also**

[Data types for SIMATIC S7-1500 (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-for-simatic-s7-1500-rt-professional)

##### Restrictions for the PLC code view (RT Professional)

###### SCL

If you access a program network created with SCL the error code 4100 is displayed.

###### Operands and UDTs

Operands that are declared in the "#Temp" or "#InOut" area are generally not supported by the PLC code view. This applies both to elementary data types and to data types that are contained in UDTs. Data types of a UDT can be declared in the "#In" and "#Out" area and displayed in the PLC code view. The same limitations as for elementary data types apply to the data types of the UDT.

###### Restrictions to data types

The use of the data types STRING, WSTRING, CHAR, WCHAR, S5TIME results in the network not being able to be displayed in the PLC code view.

###### Use of 64-bit data types

The use of 64-bit data types may result in a slight loss of accuracy as these data types are mapped in the HMI channel to the data type Double. It is therefore possible that integer data types are displayed with decimal places.

###### Addressing of tags

Please note the following restrictions when addressing tags:

- The "PLC code view" object only supports symbolic addressing of tags. If the operand is not addressed symbolically, the network with the operand cannot be displayed and an error message is generated.
- The use of array elements with a tag as index is not supported, e.g. #myArray[MyTag]. Please use numerical values when addressing array elements, for example #myArray[6].
- Slice access enables you to address specific areas within declared variables. With Slice access, PLC code view only supports the access width "Bit" to Boolean tags.

###### Jump to the PLC code view

For the jump from a supervision alarm to the PLC code view, the instance name must conform to the following naming convention when using supported local operands in a function block: <FB-Name>_DB.

The jump to a function or an organization block is only possible if only global operands are used.

##### Configuring a jump from the alarm (RT Professional)

###### Introduction

You have the option of configuring a jump from the alarm view to the PLC code view or to the project in TIA Portal from runtime. Two functions are available to you:

- Jump to the PLC code view using the system function "[ShowPLCCodeViewFromAlarm](System%20functions%20%28RT%20Professional%29.md#showplccodeviewfromalarm-rt-professional)".
- Jump from runtime to the configuration in TIA Portal using the system function "[ShowBlockInTIAPortalFromAlarm](System%20functions%20%28RT%20Professional%29.md#showblockintiaportalfromalarm-rt-professional)" .

In this example you configure the jump to the PLC code view from the corresponding alarm in the alarm view.

###### Requirement

- The "Alarm" screen is opened.
- The alarm view "ProDiag_Alarm" has been created.
- The PLC code view "PLC code view" is created in the "Program code" screen.

###### Configuring the button for the jump

1. Drag-and-drop a button from the "Tools" task card into the open "Alarm" screen.
2. Assign a name, for example, "Jump to PLC Code" under "Miscellaneous > Object > Name".
3. Switch to "Events > Click".
4. Click "Add function".
5. Select the function "ShowPLCCodeViewFromAlarm" from the selection list.
6. Specify the name of the screen in which the alarm view is configured under "Alarm screen name", "Alarm".
7. Specify the name of the alarm view under "Alarm view", "ProDiag_Alarm".
8. Enter "Program code" under "Screen name of the PLC code view".
9. Enter "PLC code view" under "Name of the PLC code view".

###### Checking the jump option

1. Select the alarm view "ProDiag Alarm".
2. Switch to the "Events" tab.
3. Click on the "Selection changed" event.
4. Create a user-defined C script at this event:

   `#include "GlobalDefinitions.h"`

   `void OnSelectedIdChanged(char* screenName, char* objectName, long id) {`

   `#pragma code("KOPAPI.dll")`

   `#include "kopapi.h"`

   `#pragma code()`

   `CMN_ERROR errorStruct;`

   `BOOL bResult;`

   `bResult = IsJumpableProDiagAlarm (screenName, objectName, id, &errorStruct);`

   `SetPropBOOL (screenName, "Jump to PLC Code", "Enabled", bResult);`

###### Result

You have configured a button for jumping to the PLC code view. The button which enables the jump is only displayed if a ProDiag- relevant alarm appears in the alarm view.

---

**See also**

[IsJumpableProDiagAlarm (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#isjumpableprodiagalarm-rt-professional)
  
[Jumping to the configuration (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#jumping-to-the-configuration-rt-professional)

#### Correcting display problems in the PLC code view (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If an error occurs in visualizing the program code, an error message with the associated error number is output in the PLC code view. To correct the display error, first work through the recommended first measures.

If the error persists, contact Customer Support.

> **Note**
>
> **Representation depends on the PLC program**
>
> The structure of the PLC program generated with S7-Graph, especially the number of contained jumps, influences the representation in the PLC code display.

##### First measures for error correction

Observe the following general information about troubleshooting:

1. Make sure that the current configuration was loaded onto the HMI device.
2. If you display program code in the PLC code view using a Runtime API function, check the notation and the sequence of the parameters of the call.
3. Restart Runtime on your HMI device.

##### Notes on error messages

The table below shows the error messages and the notes for correcting some specific errors in displaying the program code (if any):

| Error number | Error message | Instructions |
| --- | --- | --- |
| 3101, 3107, 3109, 3113, 3402, 3501, 3502, 3601, 3602,   4000 - 4107,   4110 - 4113, 4115 - 4121  4200 - 4203, 4300 - 4604 | A general error occurred in determining the display data. |  |
| 3102  4114, 4122, 4123 | The parameters of the call are not correct. | Check whether all parameters of the call were entered in the specified order. Make sure that the information is complete and correct. |
| 3103 | The PLC was not found or the name of the PLC is incorrect. | Check the specified PLC name. |
| 3104 | The address of the code block could not be determined. |  |
| 3105 | The address of the instance data block could not be determined. | Make sure that the name of the instance data black and not the name of the function block was specified in the parameter. |
| 3106 | The block is know-how protected. |  |
| 3108 | The version of the Engineering System is not compatible. | Make sure that the user program and the visualization were configured with the corresponding version of the TIA Portal. The PLC code view with WinCC V14 only supports the configuration with the Engineering System of the TIA Portal V14. |
| 3112 | The network contains an operand that is not supported. |  |
| 3117 | The network language is not supported. |  |
| 3201 | The operand was not found. |  |
| 3301 | The called block was not found. |  |
| 3302 | No block was found in which this UDT is used. |  |
| 3303 | No matching entries were found, or the entries contain data types that are not supported. |  |
| 3401 | An error occurred in determining the data of a GRAPH block. | Make sure that the specified block is a GRAPH block. |
| 3114, 3110, 3111  4103 | The network contains an element that is not supported. |  |
| 4106 | An error occurred during the calculation of the online status. | Disconnect the HMI device by unplugging the network cable. Wait a moment and then re-connect the network cable. |
| 4108 | The PLC name was not specified. |  |
| 4109 | The DB name was not specified. |  |
| 4202 | The ProDiag UDT was not specified. |  |

### Example: Visualization of the ProDiag functionality (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Procedures overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#procedures-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Requirements (Panels, Comfort Panels, RT Advanced, RT Professional)](#requirements-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-screens-panels-comfort-panels-rt-advanced-rt-professional)
- [Inserting diagnostic objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-diagnostic-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring diagnostic objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-diagnostic-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the alarm view for ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-alarm-view-for-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the jump from the GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-jump-from-the-graph-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the jump from the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-jump-from-the-prodiag-overview-panels-comfort-panels-rt-advanced-rt-professional)

#### Procedures overview (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

ProDiag enables you to supervise faults in your plant and display information on the supervisions on your HMI device.

The following example shows you how to use objects for the supervision and diagnostics of plants in WinCC.

##### Example

In this example you configure the visualization for supervision of a conveyor belt operation.

You track the movement of the production units on the conveyor belt with a ProDiag supervision that you created beforehand.

You create your user program in STEP 7 and set up ProDiag supervisions for the operands. In WinCC you then configure the screens and objects required to display the program, the current program status and the output of error messages.

![Example](images/87207154571_DV_resource.Stream@PNG-de-DE.png)

##### Configuration steps

The example is divided into several steps:

- Creating screens

  - Overview screen with the ProDiag screen objects
  - Screen for the alarm view
  - Screen for the PLC code view
- Inserting objects in the screens

  - ProDiag overview for display of the ProDiag supervisions
  - GRAPH overview for display of the GRAPH sequencer
  - Alarm view for display of the ProDiag alarms
  - PLC code view for display of the program code in the languages LAD, FBD and GRAPH

- Configuring objects

  Interconnecting the objects to enable targeted navigation to the cause of the error in runtime.

#### Requirements (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirements

- An S7-1500 controller with firmware version 2.0 or higher has been created.
- A user program for controlling the conveyor belt has been created.
- The user program contains a GRAPH function block with the motion sequence of the conveyor belt.
- The user program contains a ProDiag function block with the configured operand monitoring.

  You can find more information about creating ProDiag supervisions in the section "Programming PLC > Supervising machinery and plants with ProDiag".
- The HMI device TP1200 Comfort has been created.
- A connection has been established between the controller and your HMI device.

##### Control program

A program for the sequence of the conveyor belt and a ProDiag function block with operand monitoring was previously created in STEP 7. The following table shows the blocks and tags which are used in this example of visualization with WinCC:

| Name | Designation/type | Explanation |
| --- | --- | --- |
| **Conv_Seq [FB]** | GRAPH function block | Contains the program sequence for moving the conveyor belt. |
| Conv_Seq_DB | GRAPH data block | Associated GRAPH instance data block. |
| OFF_SQ | Tag of the type Bool from the GRAPH data block | PLC tag which is used as the process tag for displaying the status of the GRAPH sequencer. |
| **Conveyor [FB]** | ProDiag function block | ProDiag function block contains the configured ProDiag monitoring for the operands which control the operation of the conveyor. |
| Conveyor_DB | ProDiag data block | Associated ProDiag instance data block. |
| State | Tag of the type SV_FB_State from the ProDiag data block | The status tag of the "SV_FB_State" PLC data type contains the group error bits of all the supervisions that are assigned to the ProDiag function data block. |

#### Creating screens (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You will create three screens for displaying various objects to visualize the ProDiag supervisions in your plant.

##### Procedure

1. Open the project tree.
2. Click "Add new screen" in the Screens folder.
3. Open the shortcut menu of the screen and assign the name "Overview".
4. Create two additional screens named "Alarm" and "Program code".

##### Result

You have created an overview screen and two additional screens for visualization of the supervisions in Runtime.

#### Inserting diagnostic objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To visualize the program code and the program status on your HMI device in runtime, insert the diagnostic objects into the created screens.

In the GRAPH overview, you can see the currently executed steps of the GRAPH sequencer that you have configured in Runtime.

ProDiag overview shows you whether a fault has occurred and a ProDiag supervision was triggered.

##### Requirements

- The screens "Program code", "Overview" and "Alarm" have been created.
- The "Tools" task card is open.

##### Procedure

1. Open the screen "Program code".
2. Drag-and-drop a "PLC code view" from the "Tools" task card into the screen.
3. Enter the object name "PLC code view" under "Properties > Properties > Miscellaneous > Name" in the Inspector window.
4. Open the screen "Overview".
5. Drag-and-drop the "ProDiag overview" object from the "Tools" task card into the screen.

   If you want to supervise multiple ProDiag blocks from your program, create a ProDiag overview for each block.
6. Enter a meaningful object name, such as "Overview_Conveyor", under "Properties > Properties > Miscellaneous > Name" in the Inspector window.
7. Drag-and-drop a "GRAPH overview" from the "Tools" task card into the screen.
8. Enter the name "GRAPH_Sequence" under "Properties > Properties > Miscellaneous > Name" in the Inspector window.
9. Open the screen "Alarm".
10. Drag-and-drop an alarm view from the "Tools" task card into the screen.
11. Enter the name "ProDiag_Alarm" under "Properties > Properties > Miscellaneous > Name" in the Inspector window.

##### Result

You have created objects for supervision and diagnostics in the respective screens.

- Objects for display of the current program status in the screen "Overview".
- PLC code view for display of program code in the languages LAD, FBD and GRAPH in the screen "Program code".
- Alarm view for display of ProDiag alarms in the screen "Alarm".

#### Configuring diagnostic objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example, you connect the objects for visualization of program code and supervisions to your control program. You have previously created a program in STEP 7 for transportation of the production units on the conveyor belt. You have also created a ProDiag function block in which you set up the supervisions for the operands.

##### Requirements

- The "Overview" screen has been created.
- A GRAPH overview and a ProDiag overview have been created in the screen.
- A ProDiag function block was created in the control program.
- A GRAPH instance data block "Conv_Seq_DB" was created in the control program.
- GRAPH instance data block "Conv_Seq_DB" contains the "OFF_SQ" tag which is visible in HMI and accessible from HMI.

##### Procedure

1. Select the GRAPH overview.
2. Click on the selection button under "Properties> General> Process > Tag" in the Inspector window.

   A dialog opens.
3. Click on the GRAPH instance data block "Conv_Seq_DB" in the "Program blocks" folder.
4. Select the PLC tag "OFF_SQ" of the GRAPH instance data block and confirm your selection.

   ![Procedure](images/111977041291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111977041291_DV_resource.Stream@PNG-en-US.png)

   The GRAPH instance data block and the "GRAPH overview" object are connected.
5. Select the ProDiag overview "Overview_Conveyor".
6. Click on the selection button under "Properties> General> Process > Tag" in the Inspector window.

   A dialog opens.
7. Click on the data block "Coveyor_DB" in the "Program blocks" folder.
8. Select the status tag "State" of the "Conveyor_DB" data block.

   ![Procedure](images/111977432459_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111977432459_DV_resource.Stream@PNG-en-US.png)

   The ProDiag data block and the "ProDiag overview" object are connected.

**Note**

The process tag you are using for the GRAPH overview must be visible in HMI and accessible from HMI.

To identify the tags of the GRAPH data block as visible and accessible for HMI, open the GRAPH function block, select the block in the work area, and select "Edit > Internal parameters visible/accessible from HMI" in the menu bar. Then compile the program blocks.

##### Result

GRAPH overview and ProDiag overview are connected to the data blocks of the control program. In Runtime, the objects show the incoming monitoring errors and the current status of the GRAPH sequencer.

#### Configuring the alarm view for ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example you configure the alarm view for display of the monitoring alarms and jump to the PLC code view with the program code.

##### Requirements

- The "Alarm" screen has been created.
- The alarm view "ProDiag_Alarm" has been created.
- The PLC code view "PLC code view" is created in the "Program code" screen.

##### Procedure

1. Open the "Alarm" screen and select the alarm view.
2. In the Inspector window, select "Properties > General".
3. Select the alarm classes of alarms that are displayed in the alarm view, for example, the system-internal alarm classes "Acknowledgement" and "No Acknowledgement".

   You have the option to also display alarms of alarm classes that you have defined previously in STEP 7.

   ![Procedure](images/111978467595_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111978467595_DV_resource.Stream@PNG-en-US.png)
4. Specify a Boolean tag under "Properties > Display > Control tag for PLC code view" that will control the jump from the last active ProDiag alarm to the PLC code view.

   This tag is used to evaluate whether the jump from the selected alarm to the PLC code view is possible.

   ![Procedure](images/111978472075_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111978472075_DV_resource.Stream@PNG-en-US.png)
5. Drag-and-drop a button from the "Tools" task card into the "Alarm" screen.

   Enter the name "Program code" under "Properties > Properties > Miscellaneous > Name" in the Inspector window.
6. Select "Events > Click" in the Inspector window.
7. Select the "ActivatePLCCodeView" system function under "Add function".
8. Enter the screen name "Program code" and the object name "PLC code view" as parameters.
9. Under "Properties > Animations > Visibility > Tag", select the previously specified Boolean control tag for PLC code view.

   ![Procedure](images/87491816203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/87491816203_DV_resource.Stream@PNG-en-US.png)

   If the jump from the incoming ProDiag alarm to the PLC code view is possible, the "Program code" button is visible.

##### Result

You have activated the display of alarms of the defined alarm classes in the alarm view. In Runtime, the alarms of the corresponding alarm classes are displayed in the alarm view.

Using the configured button, you jump to Runtime in the PLC code view with the program instance that has triggered the ProDiag alarm.

#### Configuring the jump from the GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this step you configure the basic navigation between the GRAPH overview, the alarm view and the PLC code view.

##### Configuring the jump from the GRAPH overview

1. Select the GRAPH overview "GRAPH_Sequence".
2. Select "Events > Alarm view button click" in the Inspector window.
3. Select the "ActivateScreen" system function under "Add function".
4. Specify the name of the "Alarm" screen that contains the alarm view.
5. Select "Events > PLC code view button click" in the Inspector window.
6. Select the "ActivatePLCCodeView" system function under "Add function".
7. Enter the name of the "Program code" screen and of the PLC code view "PLC code view".

   ![Configuring the jump from the GRAPH overview](images/87395628427_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the jump from the GRAPH overview](images/87395628427_DV_resource.Stream@PNG-en-US.png)

You have connected the GRAPH overview to the PLC code view. By clicking the "PLC code view" button, the screen with the display of the GRAPH sequencer is shown in Runtime.

##### Result

You monitor the current status of the sequencer using the GRAPH overview in Runtime. You have the option of viewing the GRAPH sequencer at any time in the PLC code view.

![Result](images/96377719819_DV_resource.Stream@PNG-de-DE.png)

In case of a fault, you use the configured buttons to jump to the corresponding alarm in the alarm view or directly to the PLC code view with display of the step sequencer.

![Result](images/96378206219_DV_resource.Stream@PNG-de-DE.png)

#### Configuring the jump from the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this step you configure the basic navigation between the ProDiag overview, the alarm view and the PLC code view.

##### Configuring the jump from the ProDiag overview

1. Select the ProDiag overview "Overview_Conveyor".
2. Select "Events > Alarm view button click" in the Inspector window.
3. Select the "ActivateScreen" system function under "Add function".
4. Specify the name of the "Alarm" screen that contains the alarm view.

##### Result

You have connected the diagnostic objects to each other.

You monitor the status of the ProDiag supervisions using the ProDiag overview in Runtime. In case of an error, the corresponding supervision icon is visually highlighted.

By clicking the "Alarm view" button, the screen with the alarm view and the currently pending alarms is displayed. Using the configured buttons, you jump, for example, from a ProDiag alarm to the display of the network in the PLC code view.

![Result](images/96378217739_DV_resource.Stream@PNG-de-DE.png)

### Initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)
- [Supported instructions (Panels, Comfort Panels, RT Advanced, RT Professional)](#supported-instructions-panels-comfort-panels-rt-advanced-rt-professional)
- [Example of order of the criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](#example-of-order-of-the-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the criteria analysis view (Panels, Comfort Panels, RT Advanced)](#configuring-the-criteria-analysis-view-panels-comfort-panels-rt-advanced)
- [Configuring the criteria analysis view (RT Professional)](#configuring-the-criteria-analysis-view-rt-professional)
- [Outputting alarms with criteria (Panels, Comfort Panels, RT Advanced, RT Professional)](#outputting-alarms-with-criteria-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the TIA Portal you have the option of testing the execution of your user program on the HMI device. The data and values on the HMI device are continuously synchronized with the PLC and updated. You therefore see the current program status with the actual values of the signal states on the HMI device.

If an error occurs in your plant, you have the option of jumping to the program code from the corresponding error message and displaying the error location in the network in the “PLC code view". In the "Criteria analysis view" object, you see the operands with error for a selected GRAPH or ProDiag alarm at a glance.

The initial value acquisition and criteria analysis functions enable you to record the values at the time of the error and to quickly identify the operands with error in the program.

The actual value acquisition and criteria analysis functions are available for GRAPH function blocks, ProDiag function blocks and safety programs (F-blocks).

##### Requirement

- Initial value acquisition is available in TIA Portal for the following blocks:

  - Version V14 SP1 or higher for GRAPH function blocks Version 4.0 or higher.
  - Version V15 or higher for ProDiag function blocks Version 2.0 or higher.
- Maximum of 32 statuses can be recorded. The initial values for a network that contains more than 32 elements are not recorded.

##### Initial value acquisition

With the help of initial value acquisition you can acquire the values at the time of the error in the PLC, display them in the PLC code view and compare them with the actual values. With initial value acquisition you continuously record the signal states of Boolean operands and results of comparators in transitions and interlocks.

The signal states are recorded in a defined order from top left to bottom right:

![Initial value acquisition](images/95190347147_DV_resource.Stream@PNG-de-DE.png)

You activate initial value acquisition individually for each GRAPH block in the user program. A maximum of 32 signal states of Boolean operands can be recorded per interlock or per transition of a GRAPH step. Each individual signal state occupies one bit. The values are saved in a DWORD.

In the following example you can see the principle and order in which the initial values are recorded in the interlock:

![Initial value acquisition](images/95015296267_DV_resource.Stream@PNG-de-DE.png)

##### Criteria analysis

Initial value acquisition in the PLC enables the analysis of criteria and operands with error in the program. You see the evaluation of the criteria analysis on your HMI in the PLC code view. In addition, you can use the criteria analysis to have the operands with error displayed for a selected GRAPH or ProDiag alarm.

For the blocks for which you have activated initial value acquisition, after the jump the initial value view is displayed by default in the PLC code view. In addition, the operands with error and criteria are highlighted visually in the initial value view.

The names, absolute address and comments of the operands with error can be seen in the symbol table. You can switch between the view of the actual values and initial values.

In the event of an error in a comparator, both operands are marked as having errors. Only the recorded values are shown in the initial value view. To see the actual values of the tags, change to the actual value view.

> **Note**
>
> **Observe the evaluation order during programming**
>
> As the operands are listed in the symbol table in accordance with the rule of initial value acquisition, in the event of an error the top left operand is output first in the symbol table in the criteria analysis. Observe this evaluation order when programming the network in order to see the most important operands first in the PLC code view.

Further information on the order of the listing can be found in the [Example of order of the criteria](#example-of-order-of-the-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional).

---

**See also**

[Example of order of the criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](#example-of-order-of-the-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)

#### Supported instructions (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You see the initial values and the results of the criteria analysis in the "PLC code view" object.

For global supervisions, the initial values of all Boolean operands in the network are recorded. If the network contains multiple individual power rails that are not connected to each other, only the initial values of the respective power rail are recorded.

For local supervisions, only the initial values that are specified as conditions for the supervised parameter for the block call are recorded.

##### Supported instructions

The following instructions are supported in LAD and FBD for initial value acquisition:

| Instructions | Display on the HMI device |
| --- | --- |
| **Bit logic operations** |  |
| Normally open contact | Initial values and criteria analysis |
| Normally closed contact |  |
| Invert RLO | The instruction is supported but it is not relevant for initial values or the criteria analysis. |
| Assignment |  |
| Negate assignment |  |
| Reset output | Initial values |
| Set output |  |
| Set/reset flip-flop | Initial values and criteria analysis up to and including the instruction box |
| Reset/set flip-flop |  |
| **Comparator operations** |  |
| Equal | Initial values and criteria analysis |
| Not equal |  |
| Greater or equal |  |
| Less or equal |  |
| Greater than |  |
| Less than |  |
| **Timers** |  |
| TP | Initial values and criteria analysis up to and including the instruction box |
| TON | Initial values and criteria analysis |
| TOF | Initial values and criteria analysis up to and including the instruction box |
| TONR |  |
| **Counters** |  |
| CTU | Initial values and criteria analysis up to and including the instruction box |
| CTD |  |
| CTUD |  |

For bit logic operations, the status of the operand is recorded. For comparators, the result of the comparison is recorded.

For flip-flops, both inputs (R and S) are recorded if they are interconnected.

For timers and counters, the status of the operand at the output, and the inputs if they are interconnected, are recorded. (For example, for CTUD: CU, CD, R, LD)

The FBD instructions AND and OR are also supported for initial value acquisition and criteria analysis. The FBD instruction EXCLUSIVE OR is not supported by the initial value acquisition and criteria analysis.

---

**See also**

[Supported data types (RT Professional)](#supported-data-types-rt-professional)
  
[Supported data types (Panels, Comfort Panels, RT Advanced)](#supported-data-types-panels-comfort-panels-rt-advanced)

#### Example of order of the criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The evaluation of the criteria analysis in the PLC code view is performed in a defined order. In this example you see how initial value acquisition and the criteria analysis work on an HMI device.

##### Initial value acquisition

You record the signal state of an interlock in automatic and manual mode in the user program and have configured the following operands:

| Name of symbol | Comment | Meaning |
| --- | --- | --- |
| Tag_1 | Auto mode | Automatic mode |
| Tag_2 | Interlock_1 | First interlock |
| Tag_3 | Motor On | Switch on the motor |
| Tag_4 | Interlock_2 | Second interlock |
| Tag_5 | Hand mode | Manual mode |
| Tag_6 | Hand switch | Manual button |

The signal states of the operands are recorded in the following order and written to the DWORD:

![Initial value acquisition](images/95228488459_DV_resource.Stream@PNG-de-DE.png)

##### Criteria analysis in the event of an error

If an error occurs in the interlock, use the configured button to jump to the PLC code view from the error message and see the error location in the program. As you have already activated initial value acquisition, the initial value view is automatically shown with the criteria analysis in the PLC code view.

The operands triggering the error are highlighted in color. You only see the names, absolute addresses and comments of the operands with error in the symbol table of the PLC code view in accordance with the order of the initial value acquisition.

![Criteria analysis in the event of an error](images/111979777163_DV_resource.Stream@PNG-de-DE.png)

You have the option of switching to manual mode and enabling criteria analysis. This allows you to see the error-triggering network in the detail view even if the error situation has been corrected in the meantime.

##### Optimized programming of the interlock

So that you quickly see at a glance that the light barrier is responsible for the error, in this example it is beneficial to first program the operand Tag_4. The information about the open light barrier is then shown in the first line of the symbol table.

The following example shows the programming for the optimum view in the "PLC code view" object:

![Optimized programming of the interlock](images/111980015243_DV_resource.Stream@PNG-de-DE.png)

#### Configuring the criteria analysis view (Panels, Comfort Panels, RT Advanced)

##### Use

The "Criteria analysis view" object shows you the operands with error in the user program that have triggered a selected ProDiag or GRAPH alarm. To establish the connection to the corresponding alarms, you configure control tags at both objects.

If you select the incoming ProDiag or GRAPH alarm in the alarm view in Runtime, you see the operands that were determined in the criteria analysis in the criteria analysis view. You see the alarms and operands at a glance in Runtime if you configure the criteria analysis view and its linked alarm view in the same screen.

You have the option of connecting multiple alarm views to a criteria analysis view, and vice versa. You can configure the criteria analysis view in a pop-up screen or in a slide-in screen on KTP Mobile Panels, Comfort Panels and RT Advanced. As a result, you can connect multiple alarm views configured in various screens to one criteria analysis view, which you display as needed in a slide-in screen.

> **Note**
>
> The "Criteria analysis view" object is not available in the global screen.

##### Requirement

- The HMI device is connected to the controller
- A ProDiag program Version 2.0 or higher or a GRAPH program Version 4.0 or higher is installed on the controller
- Initial value acquisition is activated for the function blocks
- An alarm view is configured

##### Procedure

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Select "Properties > Properties > General" in the Inspector window.
3. Open the selection button under the "Tag" property.
4. Select the status tag of the corresponding alarm view under "Process > Tag".
5. Click on the alarm view.
6. Select "Properties > Properties > View" in the Inspector window.
7. Select the status tag of the criteria analysis view under "Control tag for criteria analysis".

**Note**

**Data type and length of the status tags**

The status tag must be of the WString data type and have a length of 50.

##### Result

The criteria analysis view is configured in the screen and connected to the alarm view. For a selected alarm you can see detailed information in Runtime about that operands that triggered this alarm.

#### Configuring the criteria analysis view (RT Professional)

##### Use

The "Criteria analysis view" object shows you the operands with error in the user program that have triggered a selected ProDiag or GRAPH alarm. To establish the connection to the corresponding alarms, you configure control tags at both objects.

If you select the incoming ProDiag or GRAPH alarm in the alarm view in Runtime, you see the operands that were determined by the criteria analysis in the criteria analysis view.

You configure the criteria analysis view and its linked alarm view in the same screen.

##### Requirement

- The HMI device is connected to the controller
- A ProDiag program Version 2.0 or higher or a GRAPH program Version 4.0 or higher is installed on the controller
- Initial value acquisition is activated for the function blocks
- An alarm view is configured

##### Procedure

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Select "Properties > Properties > General" in the Inspector window.
3. Open the selection button under the "Data source" property.
4. Select the configured alarm view.

##### Result

The criteria analysis view is configured in the screen and connected to the alarm view. For a selected alarm you can see detailed information in Runtime about that operands that triggered this alarm.

#### Outputting alarms with criteria (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When initial value acquisition is activated, the values of the operand with error are recorded at the time of the error and missing criteria are analyzed and determined.

You have the option of adding additional information about the operands with error to the GRAPH and ProDiag alarms and outputting them on your HMI device. If an error occurs in the program flow in runtime, the error message also indicates the first operand with error in the faulty network. You see detailed information on all operands with error of the error message in the "Criteria analysis view" object.

![Introduction](images/110359669003_DV_resource.Stream@PNG-en-US.png)

The following information can be added for an alarm:

- Symbol name: The symbolic name of the first operand that triggered the selected error message
- Absolute address: The address of the first operand with error
- Value of the operand: The value of the first operand with error at the time of the error
- Comment: Multilingual comments that were configured in the user program

The additional information is displayed in the message after the alarm text, separated by a semicolon and a space in each case.

Alternatively, you can specify that the additional information is displayed in the Info text.

In WinCC Runtime Professional you also have the option of expanding the additional alarm texts of the supervision alarms. For this, select the appropriate additional alarm text under "Runtime settings > Alarms > Criteria analysis > Expand text".

> **Note**
>
> The order of the additional information that is added to the alarm is predefined and cannot be changed.

> **Note**
>
> To completely display the alarms from the controller on the HMI device, the "Automatic update" option must be selected under "Runtime Settings > Alarms > Controller alarms" for the relevant connection. You can find additional information on complete alarms under "[Sending a complete alarm from the controller to the HMI device](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

##### Criteria analysis in the alarm system

You visualize the alarms for the criteria analysis in the following steps:

- You activate initial value acquisition in the properties of the ProDiag or GRAPH function block of the user program
- You activate the options for expanding the alarm texts in the runtime settings of the HMI device
- You configure an alarm view and a criteria analysis view and interconnect the two objects

##### Expanding alarms

1. Open the "Runtime settings" editor of the HMI device.
2. Select "Runtime settings > Alarms > Criteria analysis".
3. Select which alarms you want to expand under "Criteria analysis > Expand text".
4. Select the additional information to be added to the alarm text in the alarm, e.g. symbol name and address of the first operand with error.

##### Result

If an error occurs, you see not only the alarm text in the alarm view but also the operands that triggered the error message. You select the relevant alarm and see the operands with error determined by the criteria analysis in the criteria analysis view.

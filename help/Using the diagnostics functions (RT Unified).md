---
title: "Using the diagnostics functions (RT Unified)"
package: DiagnosticsWCCUenUS
topics: 25
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the diagnostics functions (RT Unified)

This section contains information on the following topics:

- [Configuring system diagnostics objects (RT Unified)](#configuring-system-diagnostics-objects-rt-unified)
- [Example: System diagnostics with all objects (RT Unified)](#example-system-diagnostics-with-all-objects-rt-unified)
- [Process diagnostics (RT Unified)](#process-diagnostics-rt-unified)

## Configuring system diagnostics objects (RT Unified)

This section contains information on the following topics:

- [Activating system diagnostics (S7-1200/1500) (RT Unified)](#activating-system-diagnostics-s7-12001500-rt-unified)
- [Configuring diagnostics indicators (S7-1200/1500) (RT Unified)](#configuring-diagnostics-indicators-s7-12001500-rt-unified)
- [Configuring system diagnostics of the controller (S7-1200/1500) (RT Unified)](#configuring-system-diagnostics-of-the-controller-s7-12001500-rt-unified)
- [System diagnostics display (RT Unified)](#system-diagnostics-display-rt-unified)

### Activating system diagnostics (S7-1200/1500) (RT Unified)

#### Introduction

An integrated HMI connection must exist between the controller and the HMI device so that the controller can send alarms to the system diagnostics view. In addition, the system diagnostics must be enabled both in the PLC and on the HMI device.

With an HMI connection to a SIMATIC S7-1200/1500 controller, the system diagnostics on the HMI device can be activated and deactivated by default.

The following describes how to activate system diagnostics in a controller and on an HMI device, if necessary.

> **Note**
>
> System diagnostics works only for integrated connections.

#### Requirement

- There is an integrated HMI connection between the S7-1200/1500 controller and the HMI device (WinCC Unified PC or WinCC Unified Panel).
- The S7-1200 PLC is supported as of firmware version 4.0.
- PLC S7-1500 is supported as of firmware version 2.0.

#### Activating system diagnostics in the controller

To activate the system diagnostics in a controller, proceed as follows:

1. Open the "Device configuration" of the controller in the project tree.
2. In the "Device view" tab, select the CPU on the rack.
3. Select "Properties &gt; General &gt; System diagnostics" in the Inspector window.
4. Activate the option "Activate system diagnostics for this device".

   ![Activating system diagnostics in the controller](images/160590470027_DV_resource.Stream@PNG-en-US.png)

   ![Activating system diagnostics in the controller](images/160590470027_DV_resource.Stream@PNG-en-US.png)
5. Right-click the controller in the project tree and select "Compile &gt; Hardware (rebuild all)" in the shortcut menu.

#### Activating system diagnostics on the HMI device

To activate the system diagnostics on an HMI device, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Activate the option "System diagnostics" under "Alarms &gt; Controller alarms and diagnostics".

   ![Activating system diagnostics on the HMI device](images/160592090507_DV_resource.Stream@PNG-en-US.png)

   ![Activating system diagnostics on the HMI device](images/160592090507_DV_resource.Stream@PNG-en-US.png)

   The display of system diagnostic alarms is enabled in Runtime.

> **Note**
>
> **When an upload is performed from the PLC to the TIA Portal, the uploaded PLC must be compiled to HMI RT before it is compiled and downloaded.**
>
> This is system behavior, because the Runtime data file is created during compiling.

### Configuring diagnostics indicators (S7-1200/1500) (RT Unified)

#### Showing the overall status of HMI connections via traffic light SVGs

The diagnostic status is represented by a system tag named "@DiagnosticsIndicatorTag". The "System" is notified of the diagnostic status of the configured PLCs.

The diagnostic status represents the overall status of all supported/connected PLCs. The merged state always corresponds to the worst state of all relevant PLCs.

#### Requirements

- Integrated HMI connection with PLC S7-1200/1500.
- PLC setting "Central alarm management in the PLC" is enabled.
- "Automatic update" and "System diagnostics" are enabled for the controller alarms of the HMI connection.

#### Using dynamic SVGs

System diagnostics for RT Unified provides 3 pre-programmed dynamic SVGs for S7-1200/1500 PLCs as tools for dynamic widgets:

- Diagnostics indicator ①
- Signal lamp ②
- Signal tower ③

![Using dynamic SVGs](images/138997011467_DV_resource.Stream@PNG-en-US.png)

To create a diagnostics indicator, proceed as follows:

1. Open the "Toolbox" and find "IndustryGraphicLibrary &gt; Dynamic widgets &gt; SIMATIC &gt; SystemDiagnostic" ④.
2. Select one of the 3 pre-programmed SVGs:

   - "SysDiag_DiagnosticsIndicator"
   - "SysDiag_SignalLamp"
   - "SysDiag_SignalTower"
3. Double-click or drag-and-drop the selected SVG over to the screen. The object is added to the screen.
4. Open the properties of the object in the Inspector window. Assign the "Tag" dynamization to the interface element "State" ⑥.
5. Dynamize the State property with the tag "@DiagnosticsIndicatorTag" ⑤.

The color of the dynamized SVG changes according to the defined tag values in Runtime.

Possible diagnostic values

| Status | Diagnostic value | Color |
| --- | --- | --- |
| Uncertain | 0 | Gray |
| Good | 1 | Green |
| Maintenance | 2 | Yellow |
| Error | 3 | Red |

#### Global libraries

In the "Global libraries" task card, the system diagnostics contains screen objects to reduce the configuration effort as far as possible.

![Global libraries](images/161468390027_DV_resource.Stream@PNG-en-US.png)

Under "Global libraries &gt; Buttons-and-Switches &gt; Master copies &gt; DiagnosticsButtons &gt; RT Unified", three pre-programmed dynamic SVGs are available which you can drag-and-drop into an open screen:

- "DiagnosticIndicator"
- "SignalLamp"
- "Signal Tower"

With "SystemDiagnostics", a pre-programmed screen already containing the system diagnostics control is available to you.

The indicators serve to display the general diagnostic status of the PLCs and to switch to the matrix view with a click on a button.

- To display the correct status, the "@DiagnosticsIndicatorTag" tag is assigned to the state property.

  ![Global libraries](images/161486768523_DV_resource.Stream@PNG-en-US.png)
- To switch from a diagnostics indicator to the system diagnostics control, the relevant function list is pre-programmed.

  ![Global libraries](images/161486778891_DV_resource.Stream@PNG-en-US.png)

You can use the pre-programmed function list for the following configuration:

- Screen_1 contains the indicator button and an empty screen window "Screen window_1".
- Another screen "SystemDiagnostics" is created which contains the system diagnostics control named "System diagnostics control_1". You create this screen by dragging the screen from the global libraries into the Screens folder in the project tree, or you can drag it directly into an existing screen. In this case, it is shown as a button with which you can switch from the existing screen to the "SystemDiagnostics" screen.

**Result**

In Runtime, a screen window is displayed, the system diagnostics control is loaded with the matrix view and a switch to the hardware module with error takes place.

> **Note**
>
> **Switching from the diagnostics indicator to the matrix view works in the following way:**
>
> - No error or multiple errors present: Switches to the diagnostic overview of the matrix view.
> - Exactly one error present: Switches to the hardware module with error in the matrix view.

### Configuring system diagnostics of the controller (S7-1200/1500) (RT Unified)

The system diagnostics control shows the diagnostic events of the configured PLCs in your HMI device. When loading the screen, the control displays the diagnostic buffer of the PLC with the most serious status.

#### Requirements

- At least one S7-1200/1500 PLC is configured.
- The S7-1200 PLC is supported as of firmware version 4.0.
- The S7-1500 PLC is supported as of firmware version 2.0.
- PLC setting "Central alarm management in the PLC" is enabled.
- An HMI device has been configured.
- An integrated HMI connection has been established between the S7-1200/1500 PLC and the HMI device.
- "Automatic update" and "System diagnostics" are enabled for the controller alarms of the HMI connection.
- System diagnostics is enabled in every controller and on the HMI device.
- A screen has been created.
- The Inspector window is open.

> **Note**
>
> If you configure the HMI connections to more than 50 PLCs for the object, this can lead to an overload in runtime. As a result, HMI connections can no longer be established.

#### Procedure

Double-click the icon of the "System diagnostics control" object ![Procedure](images/160523808651_DV_resource.Stream@PNG-de-DE.png)in the "Controls" section of the "Toolbox" task card, or drag it into the screen using drag-and-drop. The object is added to the screen.

![Procedure](images/160597560075_DV_resource.Stream@PNG-en-US.png)

You can change the setting for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- "View type": Switches between diagnostic view, matrix view, and Distributed I/O view.
- "Information bar": Specifies the representation of the information bar.
- "Toolbar": Specifies the buttons of the system diagnostics control.

#### Setting pre-defined styles

You can assign pre-defined styles to the object in Runtime: "Dark Style", "Extended Style" or "Bright Style". You can use pre-defined styles to change the background color of the object.

To assign a style, follow these steps:

1. Open the Runtime settings of the HMI device.

   ![Setting pre-defined styles](images/161482966923_DV_resource.Stream@PNG-en-US.png)
2. In the "General &gt; Screen &gt; Selected style" tab, select one of the following options:

   "Bright style", "Extended style" or "Dark style" to use the style.

#### Result

The "System diagnostics control" has been added to the screen. The system diagnostics can access the data of the integrated HMI connections to S7-1200/1500 PLCs. In Runtime, the diagnostic alarms of the selected PLC are displayed in the "System diagnostics control". Once Runtime has started, the events of the PLC with the most serious error are displayed.

**Diagnostic buffer**

If the diagnostic view was selected during the configuration, the diagnostic buffer is displayed in Runtime. The diagnostic buffer displays the diagnostics events of a PLC in a grid view. The grid view shows the last 200 diagnostics events of the PLC.

![Result](images/161500054923_DV_resource.Stream@PNG-en-US.png)

The first column shows the number of the entry.

The symbols in the second column indicate the event type of the PLC:

| Symbol | Meaning |
| --- | --- |
| ![Result](images/138997784843_DV_resource.Stream@PNG-de-DE.png) | Device in operation |
| ![Result](images/138997847179_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Result](images/138997881355_DV_resource.Stream@PNG-de-DE.png) | Maintenance necessary |
| ![Result](images/138997889931_DV_resource.Stream@PNG-de-DE.png) | Error in the device |

You can see the symbols of the incoming or outgoing status in the third column:

| Symbol | Meaning |
| --- | --- |
| ![Result](images/138997898507_DV_resource.Stream@PNG-de-DE.png) | Incoming event |
| ![Result](images/138997907083_DV_resource.Stream@PNG-de-DE.png) | Outgoing event |
| ![Result](images/138997915659_DV_resource.Stream@PNG-de-DE.png) | Incoming event for which there is no independent outgoing event |
| ![Result](images/138997949835_DV_resource.Stream@PNG-de-DE.png) | User-defined diagnostics event |

The fourth column shows the date and time of the event. You can see the event information in the last column.

Below the grid view, the detail view of the selected row from the grid view is displayed. You can enable or disable the detail view.

For performance reasons, no automatic update is performed. You need to perform the update manually.

At the bottom of the window, a status box is displayed with the diagnostic status and the name of the station/PLC.

> **Note**
>
> **Rearranging columns**
>
> You have the option of changing the column order configured in the Engineering System. You can find more detailed information in section "[Rearranging columns at runtime](Operating%20Unified%20PC%20%28RT%20Unified%29.md#rearranging-columns-at-runtime-rt-unified)".

**Matrix view**

If the matrix view was selected during the configuration, the status of your PLC and its lower-level hardware components are displayed as tiles in Runtime.

![Result](images/161500065291_DV_resource.Stream@PNG-en-US.png)

- Status path (1)

  - The status path shows the navigation path.
  - The background color of the status path shows the higher-level state of the plant, independent of the navigation level.
- Tile area (2)

  - The tile area adapts to the width of the control.
  - You can configure the minimum tile width and the maximum tile width.
  - You can move the tile width vertically with a scroll bar if the view area is not large enough.
- Tile (3)

  The following details are shown in the tile:

  - The state of the tile is displayed primarily by the fill color and an additional symbol. The red color means an error, i.e. when there is at least one error in the PLC or in the lower-level hardware component. The gray color is displayed if there is no error in the PLC or in the lower-level hardware component.
  - The difference, i.e. the state of the lower-level nodes, is shown by the border color of the tile. The red color means an error and the gray color stands for "State OK".
  - Name of the device.
  - Type of the device.
  - PLC operating state.
  - IP address.
  - Navigation view (4) - if further navigation is possible.
- Tooltip (8)

  When you move the mouse pointer over the tile, a tooltip appears.

  The tooltip shows the details of the device such as name, type, IP address, etc.
- Toolbar

  These buttons are available:

  - Home page: Switches to the diagnostic overview.
  - Split view (5): Opens the detail view to show the hardware details of a higher-level device.
  - Previous (6): Navigates to the previous PLC.
  - Show diagnostic buffer (7): Shows the buffer event of the currently navigated PLC.

**Hardware detail view**

![Result](images/161587837323_DV_resource.Stream@PNG-en-US.png)

In addition to the details shown on the tile, there are additional attributes for a device that can give the user further details on the device. These details are displayed as a table in the hardware detail view.

The hardware details of a device can be displayed when you navigate within the device and click the button (4) in the toolbar.

#### Languages in Runtime

The alarms are displayed in the RT language selected by the user in the screen logon dialog. The Runtime language and the PLC language should be identical.

The PLC supports only three languages, which can be configured by the user in the engineering. If the PLC language and the Runtime language are different, the event text is displayed as follows according to the fallback mechanism:

- English US
- English UK
- the standard text "## text is missing ##"

---

**See also**

[System diagnostics display (RT Unified)](#system-diagnostics-display-rt-unified)

### System diagnostics display (RT Unified)

#### Use

You can use the "System diagnostics control" object to display the diagnostic status of several PLCs using traffic light SVGs. The diagnostic status contains the overall status of all relevant PLCs. The merged state is always the worst state of all PLCs.

#### Defining the properties of the system diagnostics control

You define the properties of the system diagnostics control in the Inspector window under "Properties &gt; Properties".

![Defining the properties of the system diagnostics control](images/160544793227_DV_resource.Stream@PNG-en-US.png)

#### Selecting the view type

You select the view type in the following way:

1. Click "Properties &gt; Properties &gt; General &gt; View type" in the Inspector window.
2. Select between the "Matrix view", "Diagnostic view" and the "Distributed I/O view".

Selection of the matrix view as start view is recommended. From the matrix view, you can switch to the diagnostic view using the corresponding button in the toolbar.

**Matrix view**

With the matrix view, you have the possibility to check the status of your PLCs and their lower-level hardware components.

All hardware components are displayed as tiles. You can configure the display as well as the content of the tiles:

Make the settings for hardware details and tiles under "Properties &gt; Properties &gt; General &gt; Matrix view".

![Selecting the view type](images/160598299403_DV_resource.Stream@PNG-en-US.png)

**Diagnostic view**

The diagnostic view shows the diagnostic buffer of the PLC with the diagnostic events of the currently selected PLC.

It is not possible to switch between different PLCs in Runtime. Navigating to the diagnostic view via the selected PLC in the matrix view is recommended.

Under "Properties &gt; Properties &gt; General &gt; Diagnostic view", you make the settings for the rows, header, grid lines, scroll bar, cells and columns.

![Selecting the view type](images/160598250123_DV_resource.Stream@PNG-en-US.png)

**Distributed I/O view**

The distributed I/O view shows the distributed devices of the Profinet IO system.

The requirement is that only one PLC is configured with a Profinet IO system. Otherwise, Runtime changes back to the matrix view.

Using the "Start page" button, you can switch from the distributed I/O view to the diagnostic overview. From the distributed I/O view, you can also jump to the diagnostic buffer.

If the Profinet IO system is not accessible, the diagnostic overview is displayed.

If you change the device version from 18.00.01.01 to 18.00.01.00, the matrix view is displayed and the distributed I/O view is not visible in the selection field.

#### Setting up column sorting

To set up the column sorting in the diagnostic view, follow these steps:

1. In the Inspector window, click "Properties &gt; Properties &gt; General &gt; Diagnostic view &gt; Columns &gt; [0] Column".
2. Select the sorting direction and sorting order for the individual columns.

#### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

#### Access protection in Runtime

Configure access protection with the property "Operator control - allow" in the Inspector window under "Properties &gt; Properties &gt; Security". A logged-in user having the required authorization can acknowledge and edit the system diagnostics control using the buttons in the system diagnostics control.

#### Configuring the information bar

The information bar of the system diagnostics control shows the connection status and path.

The connection status is not displayed while the PLC is starting.

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties &gt; Properties &gt; Miscellaneous &gt; Information bar".
2. Configure the display of the information bar elements under "Properties &gt; Properties &gt; Miscellaneous &gt; Information bar &gt; Elements".

#### Toolbar

You can define the buttons of the system diagnostics control in Runtime and their operator authorizations in the Inspector window under "Properties &gt; Properties &gt; Miscellaneous &gt; Toolbar &gt; Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the system diagnostics control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/155631893131_DV_resource.Stream@PNG-de-DE.png) | Home | Shows the home page. |
| ![Toolbar](images/143094621963_DV_resource.Stream@PNG-de-DE.png) | Reload | Updates the view of the diagnostic event. |
| ![Toolbar](images/132458615563_DV_resource.Stream@PNG-de-DE.png) | First line | Selects the first of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/132458689035_DV_resource.Stream@PNG-de-DE.png) | Previous line | Selects the previous diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458681611_DV_resource.Stream@PNG-de-DE.png) | Next line | Selects the next diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458622987_DV_resource.Stream@PNG-de-DE.png) | Last line | Selects the last of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/143097143051_DV_resource.Stream@PNG-de-DE.png) | Share view | Enables/disables the detail view. |
| ![Toolbar](images/156264938379_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous PLC. |
| ![Toolbar](images/155631901707_DV_resource.Stream@PNG-de-DE.png) | Show diagnostic buffer | Changes from the matrix view to the diagnostic view. The diagnostic view shows the diagnostics buffer of the PLC.   This button is only enabled if a PLC or one of its lower-level modules is shown in the matrix view. |

#### Setting the time zone

Under Properties &gt; Properties &gt; Miscellaneous &gt; Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

> **Note**
>
> **In Runtime, you also have the option of setting the time zone via a selection list.**

---

**See also**

[Activating system diagnostics (S7-1200/1500) (RT Unified)](#activating-system-diagnostics-s7-12001500-rt-unified)
  
[Configuring diagnostics indicators (S7-1200/1500) (RT Unified)](#configuring-diagnostics-indicators-s7-12001500-rt-unified)
  
[Configuring system diagnostics of the controller (S7-1200/1500) (RT Unified)](#configuring-system-diagnostics-of-the-controller-s7-12001500-rt-unified)

## Example: System diagnostics with all objects (RT Unified)

This section contains information on the following topics:

- [Example: Procedures overview (RT Unified)](#example-procedures-overview-rt-unified)

### Example: Procedures overview (RT Unified)

#### Introduction

- A controller and an HMI device have been created.
- An HMI connection has been established between the controller and HMI device.
- System diagnostics is activated in the controller and on the HMI device.

#### Configuration steps

To get a quick view of errors, create an overview screen with the various objects for displaying diagnostic alarms.

The following example shows how to efficiently use the objects of the "Tools" or "Libraries" task cards in your project.

The example is divided into several steps:

- Creating screens

  The project engineer creates multiple screens for system diagnostics:

  - Overview screen with all objects for system diagnostics
  - Screen for the alarm view
  - Screen for the system diagnostics view
- Inserting objects in the screens

  The project engineer inserts various objects in the screens:

  - Alarm view in the "Alarm" screen
  - Screen window for displaying the alarm view and system diagnostics view
- Configuring objects

  The project engineer connects objects to enable targeted navigation to the cause of the error in runtime.

  - System diagnostics indicator with screen window of the system diagnostics view
  - Goto button with the screen window of the alarm view and the system diagnostics view.

## Process diagnostics (RT Unified)

This section contains information on the following topics:

- [Basics of supervision with ProDiag (RT Unified)](#basics-of-supervision-with-prodiag-rt-unified)
- [Requirements and licensing (RT Unified)](#requirements-and-licensing-rt-unified)
- [Objects for the supervision and diagnostics of plants](#objects-for-the-supervision-and-diagnostics-of-plants)
- [GRAPH overview](#graph-overview)
- [Configuring a GRAPH overview (RT Unified)](#configuring-a-graph-overview-rt-unified)
- [PLC code view (RT Unified)](#plc-code-view-rt-unified)
- [Configuring the PLC code view](#configuring-the-plc-code-view)
- [ProDiag overview](#prodiag-overview)
- [Configuring the ProDiag overview](#configuring-the-prodiag-overview)
- [Initial value acquisition and criteria analysis (RT Unified)](#initial-value-acquisition-and-criteria-analysis-rt-unified)

### Basics of supervision with ProDiag (RT Unified)

#### Introduction

The TIA Portal functionality, ProDiag (Process Diagnostics), is used to monitor and determine errors that occur in your plant or machine. You can use ProDiag to show the type of error, the cause of the error and the location of the error on the HMI device.

#### Use

You can use ProDiag functions to monitor your plant and to visualize it on an HMI device. The main objective of ProDiag is the reduction of downtime and loss of production after an error occurs, and the avoidance of errors using timely warnings. Diagnostic and display objects provide specific information for the operator for troubleshooting and show the processes on an HMI device on site.

#### Principle

In STEP 7, you create operand supervisions and configure the settings according to your requirements. When an error occurs, a supervision alarm is generated based on the criteria you have configured. The configured supervision instances are stored in the preset ProDiag function block. You can use the automatically generated ProDiag FBs or create and configure your own ProDiag FBs according to technological aspects.

#### Advantages

ProDiag enables you to configure supervisions and monitor your plant without changing the user program code.

You perform plant diagnostics on your HMI device. The data is automatically synchronized in order to keep the display on your HMI device always up-to-date.

### Requirements and licensing (RT Unified)

#### Introduction

You configure the ProDiag supervisions in TIA Portal with STEP 7 and create the screen objects for monitoring and diagnostics with WinCC. You need a license to use the ProDiag functionality and the corresponding screen objects.

#### Software requirements

You need the following products to configure ProDiag supervisions and visualization on the HMI device:

- TIA Portal STEP 7 Professional
- WinCC Unified

#### Hardware requirements

ProDiag functionality is available for CPUs of the S7-1500 series with firmware version 2.0 or higher.

The objects for the supervision and diagnostics of plants are available for the following HMI devices:

- WinCC Unified

> **Note**
>
> Objects for supervision and diagnostics of plants can be used under the "Full access" and "Read access" protection levels configured in the CPU.
>
> ProDiag objects under the "HMI access" and "No access" protection levels cannot be used.

#### Licensing of ProDiag supervisions

The number of ProDiag monitors that you configure with STEP 7 is licensed. You do not need a license for the first 25 supervisions, licenses must be used for additional supervisions.

| Number of supervisions | &lt;= 25 | &lt;= 250 | &lt;= 500 | &lt;= 750 | &lt;= 1000 | &gt; 1000 *) |
| --- | --- | --- | --- | --- | --- | --- |
| Number of licenses | None | 1 | 2 | 3 | 4 | 5 |
| *) If it is clear from the beginning that &gt; 1000 supervisions are required in the project, a license to use supervisions can be ordered without limitation. |  |  |  |  |  |  |

#### Licensing of ProjDiag objects

To use the objects for the diagnostics and supervision in conjunction with the ProDiag supervision in your program, you need a WinCC Unified ProDiag license.

#### Enable process diagnostics

To activate process diagnostics on an HMI device, follow these steps:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Under Process diagnostics, select the "Enable process diagnostics" option.

The display of process diagnostic alarms is enabled in runtime.

![Enable process diagnostics](images/164261333771_DV_resource.Stream@PNG-en-US.png)

### Objects for the supervision and diagnostics of plants

#### Introduction

WinCC offers the following objects for displaying the current monitoring status and for fault diagnostics in the program code:

- GRAPH overview
- PLC code view
- ProDiag overview
- Criteria analysis control

#### GRAPH overview

The "GRAPH overview" object is used to display the current program status for executed steps of the GRAPH sequencer.

#### PLC code view

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH graphic programming languages.

#### ProDiag overview

The "ProDiag overview" object provides an overview of the current status of the supervisions in the context of a ProDiag Overview supervision block.

#### Criteria analysis control

The "Criteria analysis control" object is used to display the faulty operands in the user program that were determined for a selected alarm by criteria analysis.

### GRAPH overview

#### Use

The "GRAPH Overview" object is used to display the current program status for executed steps of the GRAPH sequencer. Errors during execution of a program are displayed directly at the corresponding step.

The following information is displayed in the "GRAPH Overview" object:

- Name and status of the function block
- Status of initial and simultaneous steps
- Number and name of the first step currently executed step
- Operating mode for running the GRAPH sequencer

WinCC supports the display of step names for the GRAPH blocks in multiple languages starting from Version 6.0. The step names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available, the names are displayed in the default language (English).

![Use](images/164599456139_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> To view the program status of an GRAPH instance data block in the "GRAPH overview" object, set the block's instance-specific properties to "Visible in HMI" and "Accessible from HMI".

#### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Process &gt; Tag": Assign the tag.
- "Function bar": Specifies the buttons of the GRAPH overview.

#### Operating mode

There are four modes of operation available to you for running the GRAPH sequence:

- AUTO (default setting) - Automatically switches to the next step when the transition is fulfilled.
- TAP - Automatically switches to the next step when the transition is fulfilled and there is an edge change from "0" to "1" at the T_PUSH parameter.
- TOP - Automatically switches to the next step when the transition is fulfilled or there is an edge change from "0" to "1" at the T_PUSH parameter.
- MAN - The next step is not automatically enabled when the transition is fulfilled. You can select and deselect the steps manually.

> **Note**
>
> You set the operating mode by modifying the interface parameters of the GRAPH block in your control program.

In WinCC Unified Runtime, you can customize the name for the operating mode that is displayed in the GRAPH overview.

#### Configuring a compact view

You can also configure a compact GRAPH overview without function bar buttons and operating mode display.

To display a compact GRAPH overview in single-line compatibility mode, drag the control to the desired size.

#### Symbols

The symbols displayed in the GRAPH overview are pre-defined:

| Symbol |  | Function |
| --- | --- | --- |
| ![Symbols](images/81523267723_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred during the execution of a step. |
| ![Symbols](images/81524872587_DV_resource.Stream@PNG-de-DE.png) | Initial step | Indicates that the currently executing step is the first step in the GRAPH step sequence. |
| ![Symbols](images/81523276555_DV_resource.Stream@PNG-de-DE.png) | Simultaneous step | Shows that there are other simultaneous steps in the GRAPH step sequence in addition to the current one. |

#### Function bar

You can define the buttons of the GRAPH overview in runtime along with their operator authorizations in the Inspector window under "Properties &gt; Properties &gt; Miscellaneous &gt; Function bar &gt; Elements". By default, only the "Next Step" button is available. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the GRAPH overview:

| Button |  | Function |
| --- | --- | --- |
| ![Function bar](images/162811779467_DV_resource.Stream@PNG-de-DE.png) | Next Step | Jumps to the next step in parallel step. When you get to the last step, you can jump back to the first step. |
| ![Function bar](images/162811783435_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message in WinCC Unified.  The button is intended to be populated with appropriate system functions/scripts. |
| ![Function bar](images/162821541003_DV_resource.Stream@PNG-de-DE.png) | Jump To PLC code view | Opens the configured PLC code view.  The button is intended to be populated with appropriate system functions/scripts.  Ideally, use the "OpenGRAPHViewerFromOverview" system function. |
| ![Function bar](images/162821544971_DV_resource.Stream@PNG-de-DE.png) | Jump to TIA Portal | Several script functions are available for opening the TIA Portal. |

### Configuring a GRAPH overview (RT Unified)

#### Introduction

You can use the GRAPH overview to view the current program status for the executed steps of a GRAPH sequencer.

#### Requirement

- A PLC including a GRAPH instance data block has been created.
- GRAPH instance data block contains at least one tag which is visible in HMI and accessible from HMI.

  > **Note**
  >
  > The process tag you are using for the GRAPH overview must be visible in HMI and accessible from HMI.
  >
  > To identify the tags of the GRAPH data block as visible and accessible for HMI, open the GRAPH function block, select the block in the work area, and select "Edit &gt; Internal parameters visible/accessible from HMI" in the menu bar. Then compile the program blocks.
- An HMI device has been created.
- You have created a screen.
- The Inspector window is open.

#### Procedure

1. Drag-and-drop the GRAPH overview from the toolbox view into the configured screen.
2. In the Inspector window, click "Properties &gt; Properties &gt; Miscellaneous".
3. Open the selection button under "PLC Source &gt; Tag".

   The "Add new object" dialog opens.
4. Select the corresponding PLC in the "Program blocks" folder.
5. Select the corresponding PLC tag of the GRAPH instance data block.
6. To display the GRAPH overview in compatibility mode without function bar buttons and operating mode display, drag the object to the desired size, whereby multiple basic views are possible.
7. Under "Properties &gt; Properties &gt; Miscellaneous &gt; Function bar &gt; Elements", specify the buttons to be displayed in the object.

   ![Procedure](images/159222117899_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159222117899_DV_resource.Stream@PNG-en-US.png)
8. Under "Properties &gt; Events", you can assign system functions or scripts to the buttons in the GRAPH overview in order, for example, to jump to the alarm control or the PLC code view in Runtime and to open the TIA Portal.

**Note**

If no connection was configured between the HMI device and the selected PLC, a connection is set up automatically.

In addition, an HMI tag is created which is connected to the PLC tag.

#### Result

The GRAPH overview is inserted in the screen. The current status of the GRAPH step sequence is displayed in Runtime.

### PLC code view (RT Unified)

#### Use

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH graphic programming languages.

A variety of information about the user program is displayed in the PLC code view:

- Information area
- Symbol line
- Detail view
- Transition/Interlock view

![Use](images/162821795211_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Function bar": Specifies the buttons of the PLC code view control.
- "Symbol line": Shows information about the first or the selected icon.

#### Information area

In the information area of the PLC code view, you are shown:

- In the left area, the GRAPH sequence.
- In the right area, the details, e.g. for the step or for the transition. In the ProDiag view, the networks to the supervised operands are displayed in this area.

#### Buttons of the function bar

You can define the buttons of the PLC code view control in runtime along with their operator authorizations in the Inspector window under "Properties &gt; Properties &gt; Miscellaneous &gt; Function bar &gt; Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the PLC code view:

| Button |  | Function |
| --- | --- | --- |
| ![Buttons of the function bar](images/162823707019_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous sequence / previous network. |
| ![Buttons of the function bar](images/162823710987_DV_resource.Stream@PNG-de-DE.png) | Continue | Navigates to the next sequence / next network. |
| ![Buttons of the function bar](images/162823714955_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the information area. |
| ![Buttons of the function bar](images/162823757323_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the information area. |
| ![Buttons of the function bar](images/162823761291_DV_resource.Stream@PNG-de-DE.png) | Toggle GRAPH mode | Switches between manual and automatic step selection for the active step. |
| ![Buttons of the function bar](images/162823765259_DV_resource.Stream@PNG-de-DE.png) | Toggle detail view | 1. GRAPH view: Switches between the transition and interlock networks.  2. ProDiag view: Switches between network and the whole block. |
| ![Buttons of the function bar](images/162825361163_DV_resource.Stream@PNG-de-DE.png) | Toggle criteria analysis | Switches between the network view including criteria analysis and the standard network display without criteria analysis. |

### Configuring the PLC code view

#### Introduction

To display the PLC program networks in the graphic programming languages LAD, FBD and GRAPH in Runtime, insert a PLC code viewer control into your project.

#### Requirement

- At least one PLC has been created.
- An HMI device has been created.
- An HMI connection has been established between the controller and HMI device.
- The process diagnosis is activated on the HMI device.
- You have created a screen.

#### Procedure

1. Drag-and-drop the PLC code view control from the toolbox view.
2. In the Inspector window, click "Properties &gt; Properties &gt; Function bar".
3. Select the buttons that you require in Runtime, for example: Back, Next, Zoom in.

   ![Procedure](images/164407799563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164407799563_DV_resource.Stream@PNG-en-US.png)

#### Result

The PLC code view is inserted in the screen. In Runtime, PLC user programs can be displayed that are programmed in the graphic programming languages LAD and FBD as well as GRAPH.

You can populate the PLC code viewer using system functions, e.g. jump from the GRAPH overview or from the alarm, or you can select the corresponding parameters directly.

### ProDiag overview

#### Use

The "ProDiag overview" object provides an overview of the current status of the configured monitoring in Runtime. When an error occurs, the type of error and the error category are determined in the ProDiag overview. You can navigate directly to the alarm control to find the error and you can jump from the corresponding alarm to the PLC code viewer control. You can display the affected program code in the PLC code viewer control.

![Use](images/164456222219_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Device dependency of the "ProDiag overview" object**
>
> The "ProDiag overview" object is available for WinCC Unified.

#### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Displayed buttons
- Names and colors for categories
- Names and colors for monitoring types

#### Monitoring types and categories

You can display a maximum of 8 categories and 6 monitoring types in the "ProDiag overview" object. The following pre-defined categories and monitoring types are available:

| Designation | Categories |
| --- | --- |
| E (Error) | Error |
| W (Warning) | Warning |
| I (Info) | Information |
| C4 ... C8 | Additional categories |

Rename the categories C4 to C8, which are created by default, according to your requirements.

| Designation | Monitoring type |
| --- | --- |
| O (Operand) | Operand error |
| I (Interlock) | Interlock error |
| R (Reaction) | Reaction error |
| A (Action) | Action error |
| P (Position) | Position error |
| M (Message error) | Alarm |

You can change display symbols of the supervision types and categories at any time in the Inspector window under "Miscellaneous".

#### Symbols

The icons displayed in the ProDiag overview are fixed.

| Icon | Name | Function |
| --- | --- | --- |
| ![Symbols](images/80801398795_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred. |

#### "Jump to Alarm Control" button

The "Jump to Alarm Control" button in the ProDiag overview is activated by default.

| Button | Name | Function |
| --- | --- | --- |
| !["Jump to Alarm Control" button](images/164643614091_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message after system functions or scripts have been assigned to the button. |

#### Deactivated display

If there is a faulty connection to the controller during runtime, the object "ProDiag overview" is displayed grayed-out (unavailable). This deactivated display can be due to the following:

- The controller is deactivated
- The configured ProDiag program block was removed from the control program
- The controller is in Stop mode

As soon as the cause of the error is removed and the connection reestablished, the ProDiag overview shows the current online status of the monitoring during runtime.

### Configuring the ProDiag overview

#### Introduction

The ProDiag overview is used to monitor your machine or system at runtime and determination of diagnostic information in the event of a fault occurring.

Once you have set the status tag in the object and the connection to a ProDiag FB has been established, the status of the "State" status tag of the corresponding PLC data type is queried. In Runtime, the states of the monitored operands are represented as symbols in the ProDiag overview, similar to a traffic light colors.

In WinCC, you configure the display and the representation of categories and supervision types that are displayed in the "ProDiag overview" object independent of the supervision settings in STEP 7.

#### Requirements

- At least one S7-1500 controller has been created.
- At least one supervision instance has been configured.
- A ProDiag FB and ProDiag DB are available.
- A PC station or an HMI device that supports the ProDiag functionality has been created.
- An HMI connection has been established between the controller and HMI device.
- An screen is created and the Inspector window is open.

#### Procedure

1. Drag-and-drop the ProDiag overview from the toolbox view.
2. In the Inspector window, select "Properties &gt; Properties &gt; General".
3. Open the selection button under the "Tag" property.
4. Select the status tag of ProDiag FB.

   Alternatively, you can add the corresponding status tags from the detail view using drag-and-drop.

   ![Procedure](images/164610422411_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164610422411_DV_resource.Stream@PNG-en-US.png)
5. Under "Properties &gt; Properties &gt; Miscellaneous &gt; P Diag Categories", define the names and colors for the supervision categories.
6. Under "Properties &gt; Properties &gt; Miscellaneous &gt; P Diag Supervision types", define the names and colors for the supervision types.
7. Under "Properties &gt; Events", you can configure a system function for the "Alarm view - Button tapped" event to jump from the ProDiag overview to the alarm view in Runtime.

#### Result

The ProDiag overview is inserted in the screen. The current states of the supervised events are displayed in Runtime.

### Initial value acquisition and criteria analysis (RT Unified)

This section contains information on the following topics:

- [Overview of initial value acquisition and criteria analysis (RT Unified)](#overview-of-initial-value-acquisition-and-criteria-analysis-rt-unified)
- [Supported instructions (RT Unified)](#supported-instructions-rt-unified)
- [Criteria analysis view](#criteria-analysis-view)
- [Configuring the criteria analysis view](#configuring-the-criteria-analysis-view)
- [Outputting alarms with criteria (RT Unified)](#outputting-alarms-with-criteria-rt-unified)
- [Criteria analysis in the "GRAPH overview" object](#criteria-analysis-in-the-graph-overview-object)

#### Overview of initial value acquisition and criteria analysis (RT Unified)

##### Introduction

In the TIA Portal you have the option of testing the execution of your user program on the HMI device. The data and values on the HMI device are continuously synchronized with the PLC and updated. You therefore see the current program status with the actual values of the signal states on the HMI device.

If an error occurs in your plant, you have the option of jumping to the program code from the corresponding error message and displaying the error location in the network in the “PLC code view". In the "Criteria analysis view" object, you see the faulty operands for a selected GRAPH alarm or ProDiag alarm at a glance.

The initial value acquisition and criteria analysis functions enable you to record the values at the time of the error and to quickly identify the faulty operands in the program.

The actual value acquisition and criteria analysis functions are available for GRAPH function blocks, ProDiag function blocks and safety programs (F-blocks).

##### Requirement

- The initial value acquisition is available in WinCC Unified Runtime for the following blocks:

  - For the GRAPH function blocks as of version 6.0.
  - For the ProDiag function blocks as of version 2.0.
- Maximum of 32 statuses can be recorded. The initial values for a network that contains more than 32 elements are not recorded.

##### Initial value acquisition

With the help of initial value acquisition you can acquire the values at the time of the error in the PLC, display them in the PLC code view and compare them with the actual values. With initial value acquisition you continuously record the signal states of Boolean operands and results of comparators in transitions and interlocks.

The signal states are recorded in a defined order from top left to bottom right:

![Initial value acquisition](images/95190347147_DV_resource.Stream@PNG-de-DE.png)

You activate initial value acquisition individually for each GRAPH block in the user program. A maximum of 32 signal states of Boolean operands can be recorded per interlock or per transition of a GRAPH step. Each individual signal state occupies one bit. The values are saved in a DWORD.

In the following example you can see the principle and order in which the initial values are recorded in the interlock:

![Initial value acquisition](images/95015296267_DV_resource.Stream@PNG-de-DE.png)

##### Criteria analysis

Initial value acquisition in the PLC enables the analysis of criteria and operands with error in the program. You see the evaluation of the criteria analysis on your HMI in the PLC code view. In addition, in the "Criteria analysis view" object, you can use the criteria analysis to have the faulty operands displayed for a selected GRAPH alarm or ProDiag alarm.

> **Note**
>
> If the upstream network has been changed, the alarm is not be triggered again. This leads to inconsistencies between the network and faulty operands. As a result, the criteria analysis view cannot correctly display the faulty operands. If the alarm is triggered again, the faulty operands are displayed correctly again in the criteria analysis view.

For the blocks for which you have activated initial value acquisition, after the jump the initial value view is displayed by default in the PLC code view. In addition, the operands with error and criteria are highlighted visually in the initial value view.

All information about the selected operand can be seen in one line of the PLC code view.

In the event of an error in a comparator, both operands are marked as having errors. Only the recorded values are shown in the initial value view. To see the actual values of the tags, change to the actual value view.

#### Supported instructions (RT Unified)

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

#### Criteria analysis view

##### Use

The "Criteria analysis view" object shows you the faulty operands in the user program that have triggered a selected ProDiag alarm or GRAPH alarm. As a result, you have the option of seeing the list of faulty operands in addition to the alarm in the same screen.

To see the evaluation of the criteria analysis in the "Criteria analysis view" object in Runtime, select the initial value acquisition in the settings of the function blocks in the user program. The initial value acquisition is available for GRAPH function blocks as of version 6.0 and ProDiag function blocks as of version 2.0.

To enable the link to the corresponding error message, configure a reference to a previously configured alarm control. If you select a GRAPH alarm or a ProDiag alarm in the alarm control in Runtime, then the name, address, comment and value of the operand that caused this error is displayed in the criteria analysis view.

![Use](images/172315208331_DV_resource.Stream@PNG-de-DE.png)

You see the incoming alarms and the faulty operands at a glance in Runtime if you configure the criteria analysis view and its linked alarm control in the same screen.

> **Note**
>
> Criteria analysis is only available for the user programs for which initial value acquisition has been activated.
>
> Activate initial value acquisition in the properties of the following blocks:
>
> - ProDiag function blocks with version greater than or equal to V2.0
> - GRAPH function blocks with version greater than or equal to 6.0

##### Layout

You change the settings for the position, style, colors, and fonts of the object in the Inspector window.

##### Columns

The following columns are displayed in the criteria analysis view in Runtime.

| Column | Description |
| --- | --- |
| Symbol name | Symbolic name of the operand in the user program. |
| Address | Absolute address of the operand. |
| Value | The value of the operand at the time of the error. |
| Comment | Additional comments from the user program in the language that is loaded into the controller. |

---

**See also**

[Configuring the criteria analysis view](#configuring-the-criteria-analysis-view)

#### Configuring the criteria analysis view

##### "Criteria analysis view" object

The "Criteria analysis view" object shows you the faulty operands in the user program that have triggered a selected ProDiag alarm or GRAPH alarm. It is used to list the initial values in a separate view in order to obtain an overview of the fault status of the plant.

If you select the incoming ProDiag alarm or GRAPH alarm in the alarm control in Runtime, you see the operands that were determined in the criteria analysis view.

You configure the criteria analysis view and its linked alarm control in the same screen.

##### Requirement

- The HMI device is connected to the controller.
- A ProDiag program version 2.0 or a GRAPH program Version 6.0 or higher is installed on the controller.
- Process diagnostics is enabled in the "Runtime settings &gt; Process diagnostics &gt; General" of the Unified Runtime device.
- Initial value acquisition is enabled for the function blocks.
- An alarm control has been configured.

##### Procedure

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Click on "Properties &gt; Properties" in the Inspector window.
3. Open the selection button under the "Data source" property.
4. Select the configured alarm control.

   ![Procedure](images/169740338059_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/169740338059_DV_resource.Stream@PNG-en-US.png)

##### Result

The criteria analysis view is configured in the screen and connected to the alarm control. For a selected alarm you can see detailed information in Runtime about that operands that triggered this alarm.

#### Outputting alarms with criteria (RT Unified)

##### Introduction

When initial value acquisition is activated, the values of the faulty operands are recorded at the time of the error and missing criteria are analyzed and determined.

You have the option to add additional information about faulty operands to the GRAPH and ProDiag alarms and output them on your HMI device. If an error occurs in the program flow in runtime, the error message also indicates the faulty operands in the faulty network. You see detailed information on all operands with error of the error message in the "Criteria analysis view" object.

![Introduction](images/110359669003_DV_resource.Stream@PNG-en-US.png)

In WinCC Unified Runtime, you have the option to add additional information to the alarms. For this, select the appropriate text that you want to extend under "Runtime settings &gt; Process diagnostics &gt; Criteria analysis &gt; Extend text", i.e. alarm text, info text or additional text 1 - 9. You can extend the texts with the first faulty operand or with all faulty operands.

The following information can be added to the operands:

- Symbol: The symbolic name of the first or all faulty operands.
- Absolute address: The address of the first or all faulty operands.
- Value: The value of the first or all faulty operands at the time of the fault.
- Comment: Multilingual comments that were configured in the user program.

The additional information is separated in the alarm by semicolons and spaces.

> **Note**
>
> The order of the additional information that is added to the alarm is predefined and cannot be changed.

> **Note**
>
> To completely display the alarms from the controller on the HMI device, the "Automatic update" option must be selected under "Runtime settings &gt; Alarms &gt; Controller alarms" for the relevant connection. You can find additional information on complete alarms under "[Sending a complete alarm from the controller to the HMI device](Configuring%20alarms%20%28RT%20Unified%29.md#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)".

##### Criteria analysis in the alarm system

You visualize the alarms for the criteria analysis in the following steps:

- You enable the initial value acquisition in the properties of the ProDiag function block or GRAPH function block of the user program
- You enable the options to extend the alarm texts or info texts in the runtime settings of the HMI device

##### Extend alarms

1. Open the "Runtime settings" editor of the HMI device.
2. Click "Process diagnostics &gt; Criteria analysis".
3. Under "Criteria analysis &gt; Extend text", select which texts you want to extend.
4. Select the additional information to be added to the alarm text in the alarm, such as symbol name, address and value of the first faulty operand and comment.

   ![Extend alarms](images/169740348171_DV_resource.Stream@PNG-en-US.png)

   ![Extend alarms](images/169740348171_DV_resource.Stream@PNG-en-US.png)

##### Result

If an error occurs, you see not only the alarm text in the alarm control but also the operands that triggered the error message.

---

**See also**

[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)

#### Criteria analysis in the "GRAPH overview" object

##### Extension of the "GRAPH overview" object with the criteria analysis

To display the criteria analysis in the "GRAPH overview" object, the criteria analysis must be enabled in the Inspector window under "Properties &gt; Properties &gt; Information bar &gt; Elements".

![Extension of the "GRAPH overview" object with the criteria analysis](images/171168840459_DV_resource.Stream@PNG-en-US.png)

##### Result

In runtime, the information bar of the "GRAPH overview" object displays the symbolic name of the 1st faulty operand.

![Result](images/172315199499_DV_resource.Stream@PNG-de-DE.png)

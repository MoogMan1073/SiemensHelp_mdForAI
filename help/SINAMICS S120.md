---
title: "SINAMICS S120"
package: TFTraceS120enUS
topics: 27
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS S120

This section contains information on the following topics:

- [Recordable signals](#recordable-signals)
- [Quantity structure](#quantity-structure)
- [Persistence of the installed trace configuration and recorded signals](#persistence-of-the-installed-trace-configuration-and-recorded-signals)
- [Software user interface of the configuration](#software-user-interface-of-the-configuration)
- [Configuration](#configuration)
- [Using the measuring function](#using-the-measuring-function)

## Recordable signals

### Drive parameters

You can record the signal characteristic directly in the device with the trace function. The selection is limited to those parameters that can be recorded with the trace. The drop-down lists for the signal selection and selection of the trigger parameters show the restricted view of these parameters. For further information, see also [User interface - Signals](#user-interface---signals), [User interface - Recording conditions](#user-interface---recording-conditions) and [Configuring the recording conditions](#configuring-the-recording-conditions).

### Structure of the drive parameters

The drive parameters can be divided into the following categories:

- "Normal" parameters; these parameters have a value
- Enumeration parameters; these parameters have several values which can be used, for example, as an event query for the trace trigger ("="; "<>").
- Index parameters; these parameters contain an index which can be used to display several properties.

  Example: r37[0] "Control Unit Temperature [current measurement value]" and r37[1] "Control Unit Temperature [maximum measurement value]"

  These parameters have one entry per index value in the drop-down lists for the signal selection in the trace.
- Bit-coded parameters; these parameters contain a bit array which can be used to display settings with "0/1" or "True/False".

  Example "IF1 PROFIdrive diagnostics PZD send word" r2053.0...24

  These parameters are displayed as a bit array in the "Trigger parameters" field.

## Quantity structure

The following table shows the maximum quantity structure for SINAMICS S120 that can be recorded with the trace and logic analyzer function:

| Device | Maximum number of installed traces | Maximum number of signals per trace |
| --- | --- | --- |
| **SINAMICS S120** | 2 | 8 1...4 signals; 0.0625 ms minimum recording cycle 5...8 signals; 4.0 ms minimum recording cycle |

## Persistence of the installed trace configuration and recorded signals

Trace configurations in the device are stored persistently in the load memory and retained during POWER OFF. After a POWER OFF and POWER ON, the trace configurations are in the initial state as before the POWER OFF.

Recorded values are lost during POWER-OFF.

## Software user interface of the configuration

This section contains information on the following topics:

- [User interface - Signals](#user-interface---signals)
- [Recording conditions](#recording-conditions)

### User interface - Signals

The "Signals" area shows a table in which the signals to be recorded are configured for the selected trace configuration.

#### Setting options and displays in "Signals"

The following table shows the settings and displays:

| Column | Icon | Description |
| --- | --- | --- |
| "Name" | - | Input field for the name or address of the signal.  The input field supports autocomplete.  The parameters of the current drive object which include the entered search term in their name are offered for selection. To see the selection of parameters from all drive objects of the drive unit, put an asterisk and a period - "*." - in front of the search term.  "?" and "*" are permissible wildcard characters, with "?" representing any single character and "*" any group of characters.   **Example: Signal probes of the current drive object**   Inputting "probe" will result in a list of the probe parameters of the current drive object being shown.   **Example: Signal probes of all drive objects**   Inputting "*.probe" will result in a list of the probe parameters of all drive objects in the drive unit being shown.   **Example: Parameter r63**   Inputting "*.r63" will result in a list of the parameters from all drive objects in the drive unit which have addresses beginning with r63 being shown. |
| - | ![Setting options and displays in "Signals"](images/42119533579_DV_resource.Stream@PNG-de-DE.png) | Button to open the signal selection table  The button is displayed when the table line is selected.  Clicking the icon opens a table which offers possible signals for selection. The selected signal is displayed in the input field. |
| "Address" | - | Text field with the parameter number |
| "Data type" | - | Text field with display of the data type for the signal. |
| "Color" | - | Text field for display and selection of the color  Click the signal color to open the color selection dialog. |
| "Comment" | - | Entry field for a comment.  After inserting the signal, the name of the signal is shown first. If required, overwrite this name with your own comment. |

---

**See also**

[Selecting signals](#selecting-signals)
  
[Recordable signals](#recordable-signals)

### Recording conditions

This section contains information on the following topics:

- [User interface - Recording conditions](#user-interface---recording-conditions)
- [Trigger event](#trigger-event)

#### User interface - Recording conditions

The "Recording conditions" area shows the trigger condition for the selected trace configuration and in which cycle and how long the recording is made. Configuration is only possible when the trace configuration is displayed in offline mode or online mode with deactivated viewing.

##### Setting options and displays in "Recording conditions"

The following figure shows an example of the display in the TIA Portal:

![Setting options and displays in "Recording conditions"](images/91578514571_DV_resource.Stream@PNG-en-US.png)

| Setting/display |  |  | Description |
| --- | --- | --- | --- |
| "Trigger mode" |  |  | Selection of the trigger mode. |
|  | Drop-down list |  | The following settings are possible:  - "Start recording immediately"   The recording is made immediately after the device is activated. - "Trigger on tag"   The recording is made as soon as the installed trace is activated and the configured trigger condition is fulfilled. - "Trigger on fault"   The recording is started as soon as a fault is output on the drive. - "Trigger on alarm"   The recording is started as soon as an alarm is output on the drive. - "Monitor without trigger condition"   The recording is made immediately after the device is activated. |
| "Trigger tag" |  |  | The "Trigger tag" specifies a signal that is used to trigger the recording. |
|  | Input field |  | Input field for the name or the address of the trigger tag.  The input field supports autocomplete.  The parameters of the current drive object which include the entered search term in their name are offered for selection. To see the selection of parameters from all drive objects of the drive unit, put an asterisk and a period - "*." - in front of the search term.  "?" and "*" are permissible wildcard characters, with "?" representing any single character and "*" any group of characters.   **Example: Signal probes of the current drive object**   Inputting "probe" will result in a list of the probe parameters of the current drive object being shown.   **Example: Signal probes of all drive objects**   Inputting "*.probe" will result in a list of the probe parameters of all drive objects in the drive unit being shown.   **Example: Parameter r63**   Inputting "*.r63" will result in a list of the parameters from all drive objects in the drive unit which have addresses beginning with r63 being shown. |
|  |  | ![Setting options and displays in "Recording conditions"](images/42119295115_DV_resource.Stream@PNG-de-DE.png) | Opens the signal selection table.  Clicking the icon opens a table which offers possible signals for selection as trigger tag. The selected signal is displayed in the input field. |
|  | Text field |  | Display of the trigger tag parameter number. |
| "Event" |  |  | The events that can be used on this trigger tag are offered for selection according to the data type of the trigger tag.  The event can only be configured when a valid signal has been entered as trigger tag. |
|  | Drop-down list |  | Event selection for which the trigger tag is checked.  The entries in the drop-down list are described in Section [Trigger event](#trigger-event). |
| "Value" |  |  | Configuration of the selected event.  The configuration options differ depending on the format of the trigger tag and the selected event.   See [Trigger event](#trigger-event). |
| "Cycle" |  |  | Cycle time with which the trace recording is to be made / has been made.  The possible cycle time depends on the number of signals to be recorded:  - Up to four signals: 0.125 ms minimum recording duration - As of five signals: 4.0 ms minimum recording duration |
| "Recording duration (a)" |  |  | Input of the duration in relation to the selection in the drop-down list. The possible total duration of the trace is shown to the right of the entry field.  Select the "Use max. recording duration" option to record the maximum possible duration. The "Recording duration (a)" input field is then deactivated. The pre-trigger is part of the recording duration. If you record for 10 seconds (recording duration) and select 9 seconds as pre-trigger, then the recording is 10 seconds long, with 9 seconds before the trigger event and 1 second after.  Note: The maximum recording duration depends on the set recording cycle and on the signals selected for recording. |
| "Use max. recording duration" |  |  | Set the recording duration to the maximum value.  When the checkbox is activated, the recording duration is set to the maximum possible recording duration.  The recording duration is also adapted when additional signals are added. |
| "Pre-trigger (b)" |  |  | "Pre-trigger" defines the time interval during which the signals are already recorded before the actual trigger condition is fulfilled.  The recording duration is not extended by the "pre-trigger". |

#### Trigger event

The selectable trigger events depend on the selected trigger signal.

The individual events are described below.

##### "Rising signal"

The recording is started when the rising value of the trigger reaches or exceeds the value configured for this event.  
After activation of the installed trace, at least two cycles are required to identify the edge.

##### "Falling signal"

The recording is started when the falling value of the trigger reaches or falls below the value configured for this event.  
After activation of the installed trace, at least two cycles are required to identify the edge.

##### "Within tolerance band"

The recording starts as soon as the value of the trigger is in the value range configured for this event.

##### "Outside tolerance band"

The recording starts as soon as the value of the trigger is outside the value range configured for this event.

##### "= TRUE"

The recording starts when the state of the trigger is TRUE.

##### "= FALSE"

The recording starts when the state of the trigger is FALSE.

##### "Bit pattern"

The recording starts when the value of the trigger matches the bit pattern configured for this event. The assignment of the individual bits is displayed in the tooltip so that the relevant bits can be identified more easily.

The following figure shows the setting options for a "bit pattern":

!["Bit pattern"](images/91598704779_DV_resource.Stream@PNG-en-US.png)

It is possible to switch between the icons by clicking the respective button.

The following table shows the icons:

| Icon | Description |
| --- | --- |
| !["Bit pattern"](images/42119233035_DV_resource.Stream@PNG-de-DE.png) | Bit is not evaluated |
| !["Bit pattern"](images/42119241355_DV_resource.Stream@PNG-de-DE.png) | Bit is checked for FALSE |
| !["Bit pattern"](images/42119249675_DV_resource.Stream@PNG-de-DE.png) | Bit is checked for TRUE |

---

**See also**

[User interface - Recording conditions](#user-interface---recording-conditions)

## Configuration

This section contains information on the following topics:

- [Trace configuration - overview](#trace-configuration---overview)
- [Long-term trace configuration – overview S120](#long-term-trace-configuration-overview-s120)
- [Selecting signals](#selecting-signals)
- [Configuring the recording conditions](#configuring-the-recording-conditions)

### Trace configuration - overview

The configuration of the recording conditions and the signals to be recorded is device-specific.

#### Requirement

A trace configuration has been created and selected by double-clicking in the project tree.

#### Procedure

The following table shows the procedure for configuring.

| Step | Description |
| --- | --- |
| 1 | Documentation of the configuration (optional)  Enter a comment and an author for the configuration. |
| 2 | [Selecting signals](#selecting-signals)   Select the signals to be recorded in the "Signals" area. |
| 3 | [Configuring the recording conditions](#configuring-the-recording-conditions)   In the "Recording conditions" area, select whether the recording is to be performed immediately or depending on a trigger condition.  Also select a cycle and the recording duration. |

### Long-term trace configuration – overview S120

The configuration of the recording conditions and the signals to be recorded is device-specific.

Detailed information on the long-term trace can be found in the TIA Portal information system under the keyword "Long-term trace" in the chapter "Using online and diagnostic functions" in the section "Using the trace and logic analyzer function".

#### Requirements

- A long-term trace configuration has been created and selected by double-clicking in the project tree.
- The "Startdrive Advanced" license is available.
- The "LONGTRC" Technology Extension is installed and activated.
- To record a long-term trace you need at least 4 GB free space on your hard disk.

#### Procedure

The following table shows the procedure for configuring.

| Step | Description |
| --- | --- |
| 1 | [Selecting signals](#selecting-signals)   Select the signals to be recorded in the "Signals" area. |
| 2 | [Configuring the recording conditions](#configuring-the-recording-conditions)   In the "Recording Conditions" area, select a cycle and the target path for storing the long-term trace recording on the operating unit. |

### Selecting signals

#### Requirement

- A trace configuration has been created and selected by double-clicking in the project tree.
- The "Signals" area is open in the "Configuration" tab.

#### Procedure

To configure the signals to be recorded, proceed as follows:

1. Click in the first empty line of the table.
2. Click in the first empty cell of the "Name" column
3. Select a signal. The following options are available:

   - In the "Name" column, click the ![Procedure](images/42119533579_DV_resource.Stream@PNG-de-DE.png) button and select a parameter.
   - In the "Name" column, enter the name or the parameter or part of the name in the cell. The field displays the possible parameters in the drop-down list.
   - The "Address" column displays the number of the parameter.
4. Click in the "Comment" column and enter a comment for the signal. After inserting the parameter, the parameter name is displayed first. This can be changed.
5. Repeat the procedure from step 1 until all the signals to be recorded have been entered in the table.

**Note**

**No bit selection in "Monitor without trigger condition" trigger mode**

If you select the "Monitor without trigger condition" trigger mode when configuring the recording conditions, it is not possible to address parameter bits directly when selecting the signal. You can then only carry out bit selection in the settings of the signal table in the diagram view.

---

**See also**

[Long-term trace configuration – overview S120](#long-term-trace-configuration-overview-s120)
  
["Time diagram" tab: Signal table](#time-diagram-tab-signal-table)

### Configuring the recording conditions

#### Requirements

- A trace configuration has been created and selected by double-clicking in the project tree.
- The "Recording conditions" area is open in the "Configuration" tab.
- With active user administration (UMAC):  
  There is an active user account in the project, which is assigned role "Engineering-Administrator" or "Engineering-Standard" (see Engineering rights).

  - Or -

  The user account of the active user is assigned rights "Create and edit traces" and "Open and edit the project" via a role.

#### "Start recording immediately" trigger condition

To start the recording immediately, proceed as follows:

1. Select the "Start recording immediately" entry in the drop-down list for "Trigger mode".

   The input fields for the trigger parameter are hidden.
2. Enter the recording duration. The possible total duration is on the right.
3. Enter a recording cycle at "Cycle". The possible cycle settings depends on the number of signals.
4. Transfer the trace configuration to the device with the !["Start recording immediately" trigger condition](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.

#### "Trigger on tag" trigger condition

To start the recording depending on a condition, proceed as follows:

1. Select the "Trigger on tag" entry in the drop-down list for "Trigger mode".
2. Select a trigger parameter. The following options are available:

   - Click the !["Trigger on tag" trigger condition](images/42119533579_DV_resource.Stream@PNG-de-DE.png) button for the trigger parameter and select a parameter.
   - Enter the name or the parameter number directly in the input field for the trigger parameter.

   A drop-down list with events is displayed. The display depends on the data type of the parameter (see also [Recordable signals](#recordable-signals)).
3. Configure the event.
4. In order to record a period before the trigger event, enter a value greater than 0 in the input field for the pre-trigger.
5. Enter the recording duration. The possible total duration is on the right.
6. Enter a recording cycle at "Cycle". The possible cycle settings depends on the number of signals.
7. Transfer the trace configuration to the device with the !["Trigger on tag" trigger condition](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.

#### "Trigger on fault” trigger condition

To start the recording when a fault occurs, proceed as follows:

1. Select the "Trigger on fault" entry in the drop-down list for "Trigger mode".
2. Select a trigger parameter. The following options are available:

   - Click the !["Trigger on fault” trigger condition](images/42119533579_DV_resource.Stream@PNG-de-DE.png) button for the trigger parameter and select a parameter.
   - Enter the name or the parameter number directly in the input field for the trigger parameter.
3. Enter the pre-trigger, recording duration and cycle (see above).
4. Transfer the trace configuration to the device with the !["Trigger on fault” trigger condition](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.

#### "Trigger on alarm" trigger condition

To start the recording when an alarm occurs, proceed as follows:

1. Select the "Trigger on alarm" entry in the drop-down list for "Trigger mode".
2. Select a trigger parameter. The following options are available:

   - Click the !["Trigger on alarm" trigger condition](images/42119533579_DV_resource.Stream@PNG-de-DE.png) button for the trigger parameter and select a parameter.
   - Enter the name or the parameter number directly in the input field for the trigger parameter.
3. Enter the pre-trigger, recording duration and cycle (see above).
4. Transfer the trace configuration to the device with the !["Trigger on alarm" trigger condition](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.

#### "Monitor without trigger condition" trigger condition

**Requirements**

- The "Startdrive Advanced" license is available.
- The "LONGTRC" Technology Extension is installed and activated.
- The PG/PC is connected to the X150 interface of the drive via PROFINET (physically ONLINE).  
  Following the offline settings, an online connection must be created subsequently.

**Procedure**

To start a permanent recording without depending on a condition, proceed as follows:

1. Select the "Monitor without trigger condition" entry in the drop-down list for "Trigger mode".

   The input fields for the trigger parameters are hidden.
2. Enter a recording cycle at "Cycle". The possible cycle settings depends on the number of signals.  
   You can enter a cycle of 2 ms or 4 ms for up to four signals. For more than four signals, only a cycle of 4 ms is possible.
3. Enter the recording duration. The possible total duration is shown on the right.  
   Optional: To set the recording duration to the maximum possible, select the "Use max. recording duration" option. The maximum possible recording duration when using the "Monitor without trigger condition" trigger mode is ten minutes, or 600,000 ms.  
   The recording duration can be adjusted in steps of 1000 x recording cycle. The maximum recording duration is 10 minutes.
4. Transfer the trace configuration to the device with the !["Monitor without trigger condition" trigger condition](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.  
   The recording is made continuously in data blocks of 1000 x duration of recording cycle. If the set recording duration is reached, the oldest data block is discarded and the recording continues.

---

**See also**

[Long-term trace configuration – overview S120](#long-term-trace-configuration-overview-s120)

## Using the measuring function

This section contains information on the following topics:

- [Description](#description)
- [Measuring function software user interface](#measuring-function-software-user-interface)
- [Operating the measuring function](#operating-the-measuring-function)

### Description

The measuring function is used for controller optimization. With the measuring function, you can directly inhibit the influence of higher-level control loops by means of simple parameterization, and analyze the dynamic response of individual drives. In principle, the measuring function uses predefined trace configurations for which you can still make fine adjustments.

You can use different types of measuring functions for controller optimization.

- Speed controller setpoint frequency response (after current setpoint filter)
- Speed-controlled system (excitation after current setpoint filter)
- Speed controller disturbance variable frequency response (disturbance after current setpoint filter)
- Speed controller setpoint frequency response (before speed setpoint filter)
- Speed controller setpoint step (after current setpoint filter)
- Speed controller disturbance variable step (fault after current setpoint filter)
- Current controller setpoint frequency response (after current setpoint filter)
- Current controller setpoint step (after current setpoint filter)

When configuring the measuring function, only those measuring function types can be selected that are compatible to the device configuration of your drive.

Depending on the type selected, different parameters of the created signal are specified.

**Displaying the measurement results**

The recorded measured values of the signals are displayed as curves via a time diagram or a Bode diagram. The curves can be scaled, hidden, and moved along the y-axis, the measuring cursor and auxiliary lines can be displayed, and the diagram properties (e.g. color settings, line type for printing) can be specified.

In addition, the Bode diagram can be used for mathematically processed curves. Here, the recorded signals are postprocessed by user-defined formulas.

The time diagram and Bode diagram each has its own separate tab so that you can quickly switch back and forth between the two displays of the measurement results.

#### Requirements

- The operating unit is connected to the drive via LAN (physically ONLINE).  
  Following the offline settings, an online connection must be created subsequently.
- The "Startdrive Advanced" license is available.
- Do not use precontrol if the frequency responses are to be used to set the controllers. Precontrol would overlay the control response.

  - In this case, deactivate acceleration precontrol. Make a note of the value originally entered and re-enter it when the measurement has been completed.

### Measuring function software user interface

This section contains information on the following topics:

- ["Configuration" tab](#configuration-tab)
- ["Time diagram" and "Bode diagram" tabs](#time-diagram-and-bode-diagram-tabs)
- ["Time diagram" tab: Signal table](#time-diagram-tab-signal-table)
- ["Time diagram" tab: Formula editor](#time-diagram-tab-formula-editor)

#### "Configuration" tab

![Structure of the measuring function](images/144063996171_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Secondary navigation |
| ② | Toolbar |
| ③ | Working area with the subareas "Master control", "Measuring function settings" and "Signals" of the measuring function |
| ④ | Configuration tab |
| ⑤ | Time diagram tab |
| ⑥ | Bode diagram tab |

Structure of the measuring function

##### Icons on the toolbar

| Icon | Description |
| --- | --- |
| ![Icons on the toolbar](images/131804013579_DV_resource.Stream@PNG-de-DE.png) | Transfers the selected measuring function to the device. |
| ![Icons on the toolbar](images/131804021771_DV_resource.Stream@PNG-de-DE.png) | Transfers the selected measuring function from the device to the current project. |
| ![Icons on the toolbar](images/131804439563_DV_resource.Stream@PNG-de-DE.png) | Toggles the display between online and offline. |
| ![Icons on the toolbar](images/131804481547_DV_resource.Stream@PNG-de-DE.png) | Activates the measuring function on the selected drive.   During a recording, previously recorded values are lost. |
| ![Icons on the toolbar](images/131804502539_DV_resource.Stream@PNG-de-DE.png) | Deactivates the measuring function in the drive. |
| ![Icons on the toolbar](images/131804570123_DV_resource.Stream@PNG-de-DE.png) | Deletes the parameterization in the device. |
| ![Icons on the toolbar](images/131804607499_DV_resource.Stream@PNG-de-DE.png) | Repeats the measuring function automatically. |
| ![Icons on the toolbar](images/131804510731_DV_resource.Stream@PNG-de-DE.png) | Saves the selected measuring function to the "Measurements" folder. |
| ![Icons on the toolbar](images/131804591115_DV_resource.Stream@PNG-de-DE.png) | Exports the configuration of the measuring function to a file. |
| ![Icons on the toolbar](images/131804599307_DV_resource.Stream@PNG-de-DE.png) | Exports the measurement with the settings of the current view. |

#### "Time diagram" and "Bode diagram" tabs

With the time diagram and the Bode diagram, the recorded measured values of the signals are displayed as curves. The curves can be scaled, hidden, and moved along the y-axis, the measuring cursor and auxiliary lines can be displayed, and the diagram properties (e.g. color settings, line type for printing) can be specified.

##### Setting options and displays in the diagram

The following figure shows an example of the display:

![Time diagram example](images/167489064971_DV_resource.Stream@PNG-en-US.png)

Time diagram example

The scale in the diagram applies to the selected (highlighted in gray) signal in the legend. The legend can be moved and its size can be adjusted with the mouse.

The ![Setting options and displays in the diagram](images/167489079691_DV_resource.Stream@PNG-de-DE.png) icon displays the trigger point together with the trigger time of the device with a vertical line.

A drop-down list for selecting the unit is available below the curve for the "Time (relative)" setting for the time axis. The "Automatic" setting automatically adjusts the unit based on the displayed time range.

> **Note**
>
> **Non-interpretable data types**
>
> Some data types require a defined format, e.g. the S7 data type `LTime_of_Day`. If this format is not available, the data type is interpreted as INT.

##### Toolbar of the time diagram and Bode diagram

The following table shows the functions of the icons for the adaptation of the display:

| Icon | Function | Description |
| --- | --- | --- |
| ![Toolbar of the time diagram and Bode diagram](images/167489109899_DV_resource.Stream@PNG-de-DE.png) | Undo zoom | Undoes the most recently executed zoom function.  If several zoom functions have been executed, they can be undone step-by-step. |
| ![Toolbar of the time diagram and Bode diagram](images/167489118219_DV_resource.Stream@PNG-de-DE.png) | Redo zoom | Redoes the last undone zoom function.  If several zoom functions have been undone, they can be redone step-by-step. |
| ![Toolbar of the time diagram and Bode diagram](images/167489126539_DV_resource.Stream@PNG-de-DE.png) | Standard view | Defines the current view as standard for this recording. If the trace recording is displayed again at a later time, then the standard view is restored. |
| ![Toolbar of the time diagram and Bode diagram](images/167489136011_DV_resource.Stream@PNG-de-DE.png) | Move view | Moves the display with the mouse button pressed. |
| ![Toolbar of the time diagram and Bode diagram](images/167489144331_DV_resource.Stream@PNG-de-DE.png) | Zoom selection | Selects an arbitrary range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the time diagram and Bode diagram](images/167489152651_DV_resource.Stream@PNG-de-DE.png) | Vertical zoom selection | Selects a vertical range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the time diagram and Bode diagram](images/167489160971_DV_resource.Stream@PNG-de-DE.png) | Horizontal zoom selection | Selects a horizontal range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the time diagram and Bode diagram](images/167489169291_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |
| ![Toolbar of the time diagram and Bode diagram](images/167489177995_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |
| ![Toolbar of the time diagram and Bode diagram](images/167489186699_DV_resource.Stream@PNG-de-DE.png) | Display all | Scales the display of the available data so that the entire time range and all values are displayed. |
| ![Toolbar of the time diagram and Bode diagram](images/167489288843_DV_resource.Stream@PNG-de-DE.png) | Automatic scaling of the value axis | Scales the display so that all values are displayed for the currently displayed time range.  The relative scaling ratio between the signals may change.    **Note**   The automatic scaling of the value axis is stopped when the zoom function is activated for the value axis. This button reactivates the automatic adjustments to the minimum/maximum values. |
| ![Toolbar of the time diagram and Bode diagram](images/167489101195_DV_resource.Stream@PNG-de-DE.png) | Show the overall time range | Scales the display so that the values in the value range currently displayed are displayed for the overall time range.  The value range displayed only then changes if "Display all values" ![Toolbar of the time diagram and Bode diagram](images/167489288843_DV_resource.Stream@PNG-de-DE.png) is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |
| ![Toolbar of the time diagram and Bode diagram](images/167489195019_DV_resource.Stream@PNG-de-DE.png) | Arrange in tracks | Activates/Deactivates the track arrangement.  When the trace arrangement is activated the signals are arranged among themselves with the relevant value axes.  Scaling groups are displayed in the same trace.  This setting does not affect the display for the bit tracks. |
| ![Toolbar of the time diagram and Bode diagram](images/167489203339_DV_resource.Stream@PNG-de-DE.png) | Unit changeover of the time axis | Changes the unit of the time axis. The following are possible:  - Measuring points - Time (relative)   Relative time related to the trigger time - Time stamp of the measuring points |
| ![Toolbar of the time diagram and Bode diagram](images/167489212043_DV_resource.Stream@PNG-de-DE.png) | Display measuring points | Displays the measuring points as small circles on the curves. |
| ![Toolbar of the time diagram and Bode diagram](images/167489220363_DV_resource.Stream@PNG-de-DE.png) | Interpolated representation | Displays the linear interpolation between two consecutive measuring points for floating point numbers.  If linear interpolation is not enabled (default), the connection between the measuring points is drawn in steps. |
| ![Toolbar of the time diagram and Bode diagram](images/167489229067_DV_resource.Stream@PNG-de-DE.png) | Display vertical measurement cursors | Shows the vertical measurement cursor. The vertical position of the two measurement cursors can be moved using the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the "Measurement cursor" pane in the Trace task card in order to display further information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |
| ![Toolbar of the time diagram and Bode diagram](images/167489237387_DV_resource.Stream@PNG-de-DE.png) | Display horizontal measurement cursors | Shows the horizontal measurement cursor.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the "Measurement cursor" pane in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |
| ![Toolbar of the time diagram and Bode diagram](images/167489245707_DV_resource.Stream@PNG-de-DE.png) | Time range display | Shows or hides the time range display below the curve diagram.  The time range display shows the area in the curve in yellow based on a selected signal.  The yellow area can be moved with the mouse and the borders can be changed horizontally.    ![Toolbar of the time diagram and Bode diagram](images/167489297547_DV_resource.Stream@PNG-de-DE.png) |
| ![Toolbar of the time diagram and Bode diagram](images/167489254411_DV_resource.Stream@PNG-de-DE.png) | Display chart legend | Shows or hides the legend in the curve diagram and the bit track labels. |
| ![Toolbar of the time diagram and Bode diagram](images/167489263115_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the left | Shows the legend and the bit track labels on the left side of the curve diagram. |
| ![Toolbar of the time diagram and Bode diagram](images/167489271819_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the right | Shows the legend and the bit track labels on the right side of the curve diagram. |
| ![Toolbar of the time diagram and Bode diagram](images/167489280523_DV_resource.Stream@PNG-de-DE.png) | Change background color | Toggles between several predefined background colors. |

#### "Time diagram" tab: Signal table

The signal table lists the signals of the selected measurement and provides setting options for some properties.

In the online mode, you can change the settings of the measuring function in the device. The changes of the display options can be applied to the project using the ![Figure](images/167488924683_DV_resource.Stream@PNG-de-DE.png) icon. Otherwise the changes are discarded during the switch to offline mode.

When the measuring function is added to the measurements in the device, the current settings of the signal table are saved in the measurement.

The signals can be sorted using drag-and-drop. The bits of a signal can be resorted within a signal.

##### Setting options and displays in the signal table

The following figure shows an example of the display:

![Setting options and displays in the signal table](images/167489330827_DV_resource.Stream@PNG-en-US.png)

To select the signals to be recorded, follow the instructions under [Selecting signals](#selecting-signals).

The following table shows the settings and displays of the recorded signals:

| Column |  | Description |
| --- | --- | --- |
| Status |  | Status display |
|  | ![Setting options and displays in the signal table](images/167489493387_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists offline |
| ![Setting options and displays in the signal table](images/167489345547_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |  |
| ![Setting options and displays in the signal table](images/167489502091_DV_resource.Stream@PNG-de-DE.png) | No access right |  |
| ![Setting options and displays in the signal table](images/167489367051_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |  |
| Signal (error) |  |  |
|  | ![Setting options and displays in the signal table](images/167489510795_DV_resource.Stream@PNG-de-DE.png) | Signal |
| ![Setting options and displays in the signal table](images/167489393931_DV_resource.Stream@PNG-de-DE.png) | Failsafe signal |  |
| ![Setting options and displays in the signal table](images/167489402635_DV_resource.Stream@PNG-de-DE.png) | Signal from a data block |  |
| ![Setting options and displays in the signal table](images/167489411339_DV_resource.Stream@PNG-de-DE.png) | Signal from a failsafe data block |  |
| ![Setting options and displays in the signal table](images/167489420043_DV_resource.Stream@PNG-de-DE.png) | Calculated signal (formula) |  |
| ![Setting options and displays in the signal table](images/167489428747_DV_resource.Stream@PNG-de-DE.png) | Error in the formula of the calculated signal |  |
| ![Setting options and displays in the signal table](images/167489446155_DV_resource.Stream@PNG-de-DE.png)     ![Setting options and displays in the signal table](images/167489454475_DV_resource.Stream@PNG-de-DE.png) |  | Enables the selection of up to 16 signals for the display in the curve diagram.   The dot in the icon indicates that, for the signal in the bit selection, at least one bit has been selected for display as a bit track. |
| Signal reference (only trace) |  | Displays the automatically generated number of the signal.  The signal are accessed via the signal reference in the formulas. |
| Name |  | Displays the signal name.  A click on the name of a displayed signal updates the scale in the curve diagram.  You can enter a name for a calculated signal in the last line without a signal symbol. The calculated signal is entered with its name. |
| Measurement |  | Shows the name of the measurement to which the signal belongs.  (only with overlay measurements) |
|  | ![Setting options and displays in the signal table](images/167489463179_DV_resource.Stream@PNG-de-DE.png) | Opens the bit selection.  Individual bits can also be selected for the following data types for display as a bit track in the lower curve diagram:  - Byte, Word, DWord, LWord - SInt, USInt, Int, UInt, DInt, UDInt, LInt, ULInt   Example of an opened bit selection for the DWORD data type:    ![Setting options and displays in the signal table](images/167489471883_DV_resource.Stream@PNG-de-DE.png)   Select or deselect the relevant bit for display by clicking the ![Setting options and displays in the signal table](images/167489446155_DV_resource.Stream@PNG-de-DE.png) icon. |
| Data type |  | Shows the data type of the signal. |
| Display format |  | Shows the display format of the signal.  The display formats supported for the signal are offered for selection.  A display format suitable for the data type is set with "Default". |
| Address |  | Displays the address of the signal.  The field remains empty with optimized / type correct tags. |
| Formula |  | Displays the current formula. This formula can be changed via the formula editor.   A formula can contain mathematical functions with numbers and signals. Use the formula editor to conveniently create formulas. |
|  | ![Setting options and displays in the signal table](images/167489519115_DV_resource.Stream@PNG-de-DE.png) | Calls the [formula editor](#time-diagram-tab-formula-editor) for calculated signals. |
| Color |  | Shows the set color of the signal. This color can be changed. |
| Signal group |  | Shows the name of a signal group. This name can be changed.   The Y-scales are scaled identically for all signals of one signal group.  - Enter an identical signal group name for those signals that are to be scaled identically. - Remove signals from the signal group by deleting the signal group name.   The signal groups are saved via the function "Use current view as standard" (![Setting options and displays in the signal table](images/167489437451_DV_resource.Stream@PNG-de-DE.png) icon).   **Notes**   You cannot group binary signal events.  In hex display format, group only the signals with a format compatible to the sign for the display. |
|  | Gray field for chain icon | Move the cursor over the gray field or the chain icon (![Setting options and displays in the signal table](images/167489375755_DV_resource.Stream@PNG-de-DE.png) or ![Setting options and displays in the signal table](images/167489384459_DV_resource.Stream@PNG-de-DE.png)) to add the signal to a signal group or delete the signal from the signal group.  - ![Setting options and displays in the signal table](images/167489375755_DV_resource.Stream@PNG-de-DE.png) : Adds the signal to a signal group or creates a new signal group. - ![Setting options and displays in the signal table](images/167489384459_DV_resource.Stream@PNG-de-DE.png) : Removes the signal from the signal group.   For a selected signal with signal group, the ![Setting options and displays in the signal table](images/167489384459_DV_resource.Stream@PNG-de-DE.png) chain icon displays all signals of the same signal group. |
| Input field | Displays the signal group name.  As an alternative to the chain icon, you can assign or delete a group name via text input in this field. |  |
| Min. Y-scale |  | Displays the minimum value for scaling the signal. This value can be changed. |
| Max. Y-scale |  | Displays the maximum value for scaling the signal. This value can be changed. |
| Y(t1) |  | Displays the value at the position of the first measurement cursor. |
| Y(t2) |  | Displays the value at the position of the second measurement cursor. |
| ΔY |  | Displays the value difference between the first and the second measurement cursor. |
| ![Setting options and displays in the signal table](images/167489288843_DV_resource.Stream@PNG-de-DE.png) |  | Activates the automatic scaling of the value axis for the signal.  When this option is activated, the minimum and maximum values for scaling the signal are adjusted so that all values are displayed for the currently displayed time range. |
| Unit |  | Shows the unit.  For example for unit-based values from technology objects. |
| Comment |  | Shows a comment for the respective signal. The comment can be changed. |

#### "Time diagram" tab: Formula editor

The formula editor provides various mathematical functions for analyzing signals. You can open the editor in the signal table by clicking the ![Figure](images/134895241099_DV_resource.Stream@PNG-de-DE.png) button.

##### Configuration options and displays in the formula editor

![Formula dialog box](images/134888135307_DV_resource.Stream@PNG-en-US.PNG)

Formula dialog box

The following table shows the configuration options and displays of the formula editor:

| Field/Button |  | Description |
| --- | --- | --- |
| Name |  | Displays the name for the created formula. This can be changed.   The name must be unique and only contain characters that are allowed in Windows file names. |
| Data type |  | Shows the data type of the formula.  The data type is pre-assigned with a floating-point number of LREAL type and cannot be changed. |
| Unit |  | Shows a user-defined unit. This can be freely specified. |
| Drop-down list with signals |  | Allows selection of the signals.  The drop-down list contains the signals from the signal table and inserts a selected signal into the formula. |
| Formula entry |  | Displays the current formula. This formula can be created or changed by making entries in this text field or by means of buttons for the mathematical functions.  Signals can be referenced in the text box using the signal reference with a prefixed $ character or the name in double quotes in the formula. Mixed input is possible.  Bits from a bit selection (e.g. below the INT data type) are not allowed in the formula. |
| Mathematical functions |  |  |
|  | + | Addition |
| - | Subtraction |  |
| * | Multiplication |  |
| / | Division |  |
| () | Brackets  Grouping expressions |  |
| SQR | Square |  |
| SQRT | Square root |  |
| ABS | Absolute value  Calculates the size of a number.   **Examples**    `ABS(5)` → 5   `ABS(-3)` → 3   `ABS(-3.14)` → 3.14 |  |
| MOD | Modulo  Calculates the residual value of a division   **Examples**    `MOD(5,3)` → 2   `MOD(3.14,3)` → 0.14 |  |
| REC | Reciprocal value (1/x) |  |
| DIFF<sup> 1)</sup> | Numerical differentiation   **Examples**   Formula: `DIFF($0,SAMPLETIME)` |  |
| INT <sup>1)</sup> | Numerical integration   **Examples**   Formula: `INT($0,SAMPLETIME)` |  |
| RMS<sup> 1)</sup> | Quadratic mean  The quadratic mean is given by first adding the squares of all the measured values and dividing them by the number of measured values. The quadratic mean is the square root of this value.   **Examples**   Formula: `RMS($0,SAMPLETIME)` |  |
| AV | Mean value filter from 1st to 5th order  If the specification of an order is missing, the mean filter of the 1st order is used.   **Examples**    `AV($0,1)` → Mean filter 1st order   `AV($0,5)` → Mean filter 5th order |  |
| π | Mathematical constant Pi |  |
| AM | Arithmetic mean  The arithmetic mean is a moving average over five measuring points. |  |
| DIF | Simple subtraction with mean filter from 1st to 5th order  If the specification of an order is missing, simple subtraction is performed with a 1st order filter.   **Examples**    `DIF($0,1)` → Single subtraction with 1st order filter   `DIF($0,5)` → Single subtraction with 5th order filter   `DIF($0)` → Single subtraction with 1st order filter   **Example: Calculate an acceleration curve from a velocity signal**     `$0`: Velocity signal in meters per second Cycle time of the constant cycle velocity recording: 1 ms  Formula: `DIF($0,1)/0.001`  Unit: `m/s`<sup>2</sup> |  |
| DIF2 | Double subtraction with mean filter from 1st to 5th order  If the specification of an order is missing, then double subtraction is executed with a 1st order filter.   **Examples**    `DIF2($0,1)` → Double subtraction with 1st order filter   `DIF2($0,5)` → Double subtraction with 5th order filter   `DIF2($0)` → Double subtraction with 1st order filter   **Example: Calculate an acceleration curve from a position sequence**     `$0`: Position sequence in meters Cycle time of the constant cycle position recording: 1 ms  Formula: `DIF2($0,1)/SQR(0.001)` Unit: `m/s`<sup>2</sup> |  |
|  | Bode | Bode diagram with amplitude and phase  Calculated signals as parameter or calculations for the parameters are not permitted.   Additional calculations with the Bode function are not permitted.   **Mandatory parameters**   Analog signals must be specified for the parameters of the input and output signal.   Permitted data types for the parameters:  SINT, INT, DINT, LINT, USINT, UINT, UDINT, ULINT, REAL, LREAL, BYTE, WORD, DWORD, LWORD   **Optional parameters**   The following parameters can be optionally specified  - RangeStart   Index of the first measuring point to be displayed.   The index of the measuring points is displayed on the X axis in the Bode diagram.   If the parameter is not set, the first measuring point of the measurement is assumed to be the default. - RangeEnd (RangeStart required)   Index of the last measuring point to be displayed.   The index of the measuring points is displayed on the X axis in the Bode diagram.   If the parameter is not set, the last measuring point of the measurement is assumed to be the default.    **Valid examples**   $0=input signal, $1=output signal   `BODE($0,$1)`    `BODE($0,$1,0,1000)`    **Invalid examples**    `BODE($0,20)`    `BODE($0,$1,0)`    `BODE($0,$1,1000)`    `BODE($0+1,0)`    `BODE($0,$1)+10`    `BODE($0,$1)+SQRT($5)` |
| Show signal name |  | Activates the signal name display.  If the check box is selected, the signal names in the formula are displayed instead of the signal references. |
| Validate |  | Checks the validity of the formula. |
| Result of validation |  | Displays the result of the validation.  Displays the result of the validation and indicates errors and error locations. |
| <sup>1) </sup>The constant `SAMPLETIME` is only available for equidistant recording cycles. Time unit for `SAMPLETIME` is always μs. |  |  |

> **Note**
>
> The functions DIF, DIF2, DIFF, AM, RMS, AV and INT can only process one recorded signal as argument. Not all invalid formulas are marked as errors.

### Operating the measuring function

This section contains information on the following topics:

- [Overview](#overview)
- [Create or call measuring function](#create-or-call-measuring-function)
- [Configure measuring function](#configure-measuring-function)
- [Performing measurement(s)](#performing-measurements)
- [Managing a measuring function](#managing-a-measuring-function)

#### Overview

##### Requirement

- A drive is configured in Startdrive that supports the trace and logic analyzer function and to which an online connection has been established.
- The "Startdrive Advanced" license is available.

##### Procedure

The following table shows a procedural overview with typical steps when working with the measuring function.

| Step | Description |
| --- | --- |
| 1 | Create or call measuring function |
| 2 | [Configure measuring function](#configure-measuring-function) |
| 3 | [Perform measurements](#performing-measurements) |
| 4 | [Manage measuring function](#managing-a-measuring-function) |

#### Create or call measuring function

Measuring functions can be created for the trace in the project tree. Saved measuring functions can be called and modified.

The following describes how you create a measuring function under the system folder ![Figure](images/82025997579_DV_resource.Stream@PNG-de-DE.png) "Trace" and how you display a measuring function that has been saved.

##### Requirements

- The configured drive supports the trace function.
- The SINAMICS S210 drive has a firmware version from SINAMICS FW V6.1.
- The operating unit is connected to the drive via LAN (physically ONLINE).

##### Creating a new measuring function

1. To create a new measuring function in the project, double-click on the entry "Add new measuring function" in the "Traces" folder.

   A new measuring function is then created in the working area on the right. Using the "Measuring conditions" function view, you can make settings for the active measuring function.

##### Displaying saved settings of a selected measuring function

1. In the project tree, double-click on the corresponding icon (![Displaying saved settings of a selected measuring function](images/82026044427_DV_resource.Stream@PNG-de-DE.png) offline / ![Displaying saved settings of a selected measuring function](images/82026074123_DV_resource.Stream@PNG-de-DE.png) online) of a created measuring function.

   In the working area, the "Measuring conditions" screen form opens with the saved settings.
2. Correct the settings of the measuring function where necessary and save the changes.

#### Configure measuring function

> **Note**
>
> **Backup of the measuring function data**
>
> The trace configuration, and therefore the measuring function configuration as well, are saved retentively. This data is retained even after the system is switched off or on.
>
> In contrast, recordings are not automatically saved, and are therefore lost when the system is switched off. As a consequence, recordings must be manually saved in the project or exported to a file structure.

##### Requirements

- At least one measuring function has been set up in the project.
- The measuring function to be parameterized is displayed in the working area.

##### Possible settings

Depending on the device configuration, certain parameters and options are either not displayed or displayed in gray. Incorrectly parameterized input fields are displayed in red to simplify input checking.

| Field |  | Meaning/Instruction |
| --- | --- | --- |
| **Drive selection** |  | Here you select the drive axis on which the measuring function is to act. |
|  | Amplitude | The value of the signal amplitude to be applied.  For the current controller, the specification is a relative value in percent. The value refers to the reference current (p2002). For the speed controller, the amplitude specification is always in physical units. |
|  | Offset | DC component which is superimposed on the test signal.  The value is normalized in the same way as the amplitude specification. Please note that the offset is subtracted again when saving the measured values in runtime. |
| **Measuring function selection** |  | Select the measuring function for the controller optimization here. Depending on the selected measuring function, you can also set various parameters of the applied signal. The recorded parameters are shown in the table. You can freely select other parameters for the free signals to be recorded. |
|  | Speed controller setpoint frequency response (after current setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the reference frequency response on the speed controller, the speed setpoint is activated by a PRBS signal. The evaluation of the signals is performed in the frequency range. |
| Speed-controlled system (excitation after current setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the measurement of the speed-controlled system on the speed controller, the speed setpoint is activated by a PRBS signal. The evaluation of the signals is performed in the frequency range. |  |
| Speed controller disturbance variable frequency response (disturbance after current setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the disturbance variable frequency response on the speed controller, the speed setpoint is activated by the PRBS signal. The evaluation of the signals is performed in the frequency range. |  |
| Speed controller setpoint frequency response (before speed setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the setpoint frequency response on the speed controller, the speed setpoint is activated by the PRBS signal. The evaluation of the signals is performed in the frequency range. |  |
| Speed controller setpoint step (after speed setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the setpoint step on the speed controller, the speed setpoint is activated by a step function. The evaluation of the signals is performed in the time range. |  |
| Speed controller disturbance step (fault after current setpoint filter) | The speed control loop is closed, all of the higher-level control loops are open. For the disturbance variable step on the speed controller, the disturbance torque is activated by a step function. The evaluation of the signals is performed in the time range. |  |
| Current controller setpoint frequency response (after current setpoint filter) | For the setpoint frequency response on the current controller, the current setpoint is activated by the PRBS signal. The evaluation of the signals is performed in the frequency range. |  |
| Current controller setpoint step (after current setpoint filter) | Speed and position controller are switched off and current setpoints applied in the current controller cycle. For the setpoint step on the current controller, the current setpoint is activated by a step function. The evaluation is performed in the time range. |  |
| **Curve parameters** |  | Dynamic curve parameters depending on the selected measuring function. |
|  | Measuring periods | Maximum number of measuring periods for a PRBS signal. |
| Settling periods | For a PRBS signal, waits this number of periods before the recording is started. |  |
| Measuring time | Measurement duration  For activation by means of a PRBS signal, the duration is defined by the bandwidth and the number of measuring periods of a PRBS period. |  |
| Settling time | For a step function, waits this time until the recording is started. |  |
| Amplitude | The value of the signal amplitude to be applied.  For the current controller, the specification is a relative value in percent. The value refers to the reference current (p2002). For the speed controller, the amplitude specification is always in physical units. |  |
| Offset | DC component which is superimposed on the test signal.  The value is normalized in the same way as the amplitude specification. Please note that the offset is subtracted again when saving the measured values in runtime. |  |
| Bandwidth | Bandwidth of the measurement for activation by a PRBS signal.  Definition: Bandwidth = 1 / (2 * duration of the shortest pulse). As only integer multiples of the controller sampling time are possible as pulse, the bandwidths that can be implemented are also quantized. |  |
|  |  |  |
| Ramp-up time | Time until the first increase of the test signal. |  |
| Max. measuring time | This parameter is active only when activated by a step function. The time depends on the memory on RT. |  |
| Values in % | Switches the display of the input fields to curve parameters in % of the preset default values. |  |
| Offset in rpm | Switches the display of the offset from % to rpm. |  |
| **Signals** |  |  |
|  | ![Possible settings](images/134896569355_DV_resource.Stream@PNG-de-DE.png) | Static display of the signal icon |
| Name | Display of the signal name. |  |
| Address | Display of the address (not for symbolic tags) |  |
| Data type | Display of the data type |  |
| Comment | Display a comment on the signal |  |

##### Configure measuring function

1. Select the required measuring function (see table above) in the "Measuring function setting" subarea.
2. Parameterize the specific curve parameters of the selected measuring function (see table above).
3. Select the drive axis or drive axes to which the measuring function is to be applied.

##### Configuring signals

> **Note**
>
> **Maximum number of signals**
>
> You can configure a maximum of 8 signals per measuring function.

To configure the signals to be recorded, proceed as follows:

1. Click in the first empty cell of the "Name" column.
2. Select a signal. The following options are available:

   - In the "Name" column, click on the ![Configuring signals](images/134899574923_DV_resource.Stream@PNG-de-DE.png) icon and select a parameter.
   - Enter the parameter name in the "Name" column or part of the name in the cell. The field shows the possible parameters in the drop-down list.
   - The "Address" column displays the number of the parameter. A signal color is recommended in the "Color" column.
   - For selecting parameters from all drive objects of the drive unit, put an asterisk and a period - "*." - in front of the search term, e.g. "*.r0063".
3. If you wish to assign another color to the signal, then select a new color from the drop-down list in the "Color" column.
4. Click in the "Comment" column and enter a comment for the signal.
5. Repeat the procedure from step 1 until all of the signals to be recorded have been entered in the table.

---

**See also**

[Overview](#overview)

#### Performing measurement(s)

##### Requirements

- The project includes at least one measuring function in the "Traces" system folder ![Requirements](images/82026099467_DV_resource.Stream@PNG-de-DE.png).
- The created measuring function is parameterized.
- PG/PC is connected to the drive unit via LAN (physically ONLINE).

##### Measurement procedure

1. Transfer a completely configured measuring function to the drive.
2. Activate the master control for this drive.
3. If you use an infeed, switch it on.
4. Set a drive enable.
5. Start the measurement and then stop it again.

   - Or -

   Perform overlay measurements.
6. Finally, deactivate the master control of the drive again.

##### Transferring the measuring function to the drive

Proceed as follows to transfer (upload) a selected measuring function to the drive:

1. Open a valid measuring function in the project tree.

   The settings of the measuring function are displayed in the working area.
2. To establish an online connection to the drive, click the "Go online" button in the toolbar.

   The "Go online" dialog box then appears.

   Make the settings for the online connection here and click on "Connect".
3. Click the ![Transferring the measuring function to the drive](images/131804013579_DV_resource.Stream@PNG-de-DE.png) icon to transfer the measuring function to the drive unit.

**Result:**

The measuring function is transferred to the drive.

##### Activating the master control

You can use the master control to traverse the drive and thus test the measuring function settings that have been made. The control panel can always only be activated for one drive.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot apply the project lock if project protection is activated.
>
> In addition, as a result of inactivity, the automatic project lock is not activated as long as the control panel is active.

When you activate the control panel, you assume master control of the drive. The master control can only be activated for one drive.

| Symbol | Meaning |
| --- | --- |
| 1. Click on the opened measuring function on the "Master control" entry in the secondary navigation.    The "Master control" screen form is now displayed in the working area. 2. Click the "Activate" button under "Master control".    The "Activate master control" message window opens. 3. Read the warning carefully. Check the monitoring time and if required, correct it.    The monitoring time specifies the time during which the connection from the operating unit to the drive is cyclically monitored. The minimum value is 1000 ms. 4. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.       | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury.  - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.       This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 5. To close the message window and confirm your inputs, click the "OK" button.     The message window closes. The master control is then active. |  |

##### Setting the drive enable

To set the required drive enable, proceed as follows:

1. Click on the opened measuring function on the "Master control" entry in the secondary navigation.

   The "Master control" screen form is now displayed in the working area.
2. Click the "Set" button under "Drive enables".
3. Click the "Acknowledge faults" button to acknowledge the currently pending faults.
4. If you no longer require the enables, click the "Reset" button under "Drive enables".

##### Starting/stopping the measuring function

If you want to start or stop a measurement with a measuring function, proceed as follows:

1. To start the measuring function, click either the ![Starting/stopping the measuring function](images/144056090123_DV_resource.Stream@PNG-de-DE.png) icon on the “Master control” screen or, alternatively, the ![Starting/stopping the measuring function](images/131804481547_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar.

   The selected measuring function is started. It measures the dynamic response of the selected drive.
2. To stop the measuring function, click either the ![Starting/stopping the measuring function](images/144054106507_DV_resource.Stream@PNG-de-DE.png) icon on the “Master control” screen or, alternatively, the ![Starting/stopping the measuring function](images/131804502539_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar.

   The selected measuring function is stopped.

##### Superimposing measuring functions

If you want to superimpose several measuring functions, proceed as follows:

1. To superimose measuring functions, click on the ![Superimposing measuring functions](images/131804510731_DV_resource.Stream@PNG-de-DE.png) icon (Add to measuring functions) before starting the measuring function.
2. To start the measuring function, click either the ![Superimposing measuring functions](images/144056090123_DV_resource.Stream@PNG-de-DE.png) icon on the "Master control" screen form in the "Control" area or, alternatively, the ![Superimposing measuring functions](images/131804481547_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar.

   The selected measuring function is started. It measures the dynamic response of the selected drive.
3. To stop the measuring function, click either the ![Superimposing measuring functions](images/144054106507_DV_resource.Stream@PNG-de-DE.png) icon on the "Master control" screen form in the "Control" area or, alternatively, the ![Superimposing measuring functions](images/131804502539_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar.

   The selected measuring function is stopped.
4. Drag & drop the measurements to the system folder ![Superimposing measuring functions](images/84072764427_DV_resource.Stream@PNG-de-DE.png) (overlaid measurements).

##### Deactivating the master control

How to return the master control:

1. Click the "Deactivate" button under "Master control".  
   The grayed-out user interface of the screen form indicates that the master control is deactivated.

---

**See also**

[Overview](#overview)

#### Managing a measuring function

##### Requirement

- The project includes at least one measuring function in the "Traces" system folder ![Requirement](images/82026099467_DV_resource.Stream@PNG-de-DE.png).
- The created measuring function is parameterized.

##### Loading the measuring function from the drive into the project

To transfer (download) the measuring function of the drive into the project, proceed as follows:

1. Check whether an online connection to the drive exists and establish an online connection if necessary.
2. Open a measuring function in the drive.
3. Click on the icon ![Loading the measuring function from the drive into the project](images/131804021771_DV_resource.Stream@PNG-de-DE.png)"Add trace configuration from device to trace configuration" to transfer the measuring function from the drive into the project.

The measuring function is transferred to the ![Loading the measuring function from the drive into the project](images/82025997579_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder.

At the same time, a measuring function of the same name is overwritten in the system folder.

##### Switchover of the configuration display (online/offline)

The configuration of the measuring function can only be configured offline. Once the configuration has been uploaded to the drive, the parameterization no longer can be changed online. You can quickly toggle between online and offline via the ![Switchover of the configuration display (online/offline)](images/131804439563_DV_resource.Stream@PNG-de-DE.png) icon.

1. To switch over between online and offline mode, click the ![Switchover of the configuration display (online/offline)](images/131804439563_DV_resource.Stream@PNG-de-DE.png) icon.

##### Deleting the parameterization in the drive

To delete the parameterization of the drive, proceed as follows:

1. Check whether an online connection to the drive exists and establish an online connection if necessary.
2. Ensure that the measuring function is not active. Stop the measuring function, if necessary.
3. To delete the parameterization in the drive, click on the icon ![Deleting the parameterization in the drive](images/131804570123_DV_resource.Stream@PNG-de-DE.png)"Delete trace from the device".

##### Exporting the measuring function

To export a measuring function to your file system, proceed as follows:

1. Display the measuring function in the working area.
2. Click on the icon ![Exporting the measuring function](images/82025984523_DV_resource.Stream@PNG-de-DE.png)"Export trace configuration" to export the selected measuring function.

   - OR -

   Select the ![Exporting the measuring function](images/82026099467_DV_resource.Stream@PNG-de-DE.png)"Traces" system folder and select "Export measurement" from the shortcut menu.

   The "Save As..." dialog box opens.
3. Select a folder, file name and possibly a file type to save the measuring function.
4. Click the "Save" button.

   The selected measuring function is saved in the specified folder.

##### Importing the measuring function

To import a measuring function from your file system, proceed as follows:

1. Mark the ![Importing the measuring function](images/82026099467_DV_resource.Stream@PNG-de-DE.png)"Traces" system folder and select "Import measuring function" from the shortcut menu.

   The "Open" dialog opens.
2. Select the file of file type "*.ttcfgx" to be imported with the measuring function.
3. Click the "Open" button.

   The selected measuring function is imported into the project.

---

**See also**

[Overview](#overview)

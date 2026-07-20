---
title: "SINAMICS G120"
package: TFTraceG120enUS
topics: 13
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SINAMICS G120

This section contains information on the following topics:

- [Recordable signals](#recordable-signals)
- [Quantity structure](#quantity-structure)
- [Persistence of the installed trace configuration and recorded signals](#persistence-of-the-installed-trace-configuration-and-recorded-signals)
- [Software user interface of the configuration](#software-user-interface-of-the-configuration)
- [Configuration](#configuration)

## Recordable signals

### Drive parameters

You can record the signal characteristic directly in the device with the trace function. The selection is limited to those parameters that can be recorded with the trace. The drop-down lists for the signal selection and selection of the trigger parameters show the restricted view of these parameters. For further information, see also [User interface - Signals](#user-interface---signals), [User interface - Recording conditions](#user-interface---recording-conditions) and [Configuring the recording conditions](#configuring-the-recording-conditions).

### Structure of the drive parameters

The drive parameters can be divided into the following categories:

- "Normal" parameters; these parameters have a value
- Enumeration parameters; these parameters have several values which can be used, for example, as an event query for the trace trigger ("="; "&lt;&gt;").
- Index parameters; these parameters contain an index which can be used to display several properties.

  Example: r39[0] "Energy balance (sum)" and r39[1] "Energy drawn"

  These parameters have one entry per index value in the drop-down lists for the signal selection in the trace.
- Bit-coded parameters; these parameters contain a bit array which can be used to display settings with "0/1" or "True/False".

  Example: "Missing enables" r46.0...31

  These parameters are displayed as a bit array.

## Quantity structure

The following table shows the maximum quantity structure for SINAMICS G120 that can be recorded with the trace and logic analyzer function:

| Device | Maximum number of installed traces | Maximum number of signals per trace |
| --- | --- | --- |
| **SINAMICS G120** | 2 | 8 1...4 signals; 0.5 ms minimum recording cycle 5...8 signals; 4.0 ms minimum recording cycle |

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
| "Name" | - | Input field for the name or parameter number of the signal.   **Examples:**   - Missing enables r46 - Status word 1 r52 |
| - | ![Setting options and displays in "Signals"](images/42119533579_DV_resource.Stream@PNG-de-DE.png) | Button to open the signal selection table.  The button is displayed when the table line is selected.  Clicking the icon opens a table which offers possible signals for selection. The selected signal is displayed in the input field. |
| "Address" | - | Input field for the parameter numbers. |
| "Data type" | - | Text field with display of the data type for the signal. |
| "Color" | - | Text field for display and selection of the color.  Click the signal color to open the color selection dialog. |
| "Comment" |  | Input field for a comment.  After inserting the signal, the name of the signal is shown first. If required, overwrite this name with your own comment. |

---

**See also**

[Selecting signals](#selecting-signals)
  
[Recordable signals](#recordable-signals)

### Recording conditions

This section contains information on the following topics:

- [User interface - Recording conditions](#user-interface---recording-conditions)
- [Trigger event](#trigger-event)

#### User interface - Recording conditions

The "Recording conditions" area shows the trigger condition for the selected trace configuration and in which cycle and how long the recording is made. Configuration is only possible when the trace configuration is displayed in offline mode or online mode with deactivated viewing .

##### Setting options and displays in "Recording conditions"

The following figure shows an example of the display in the TIA Portal:

![Setting options and displays in "Recording conditions"](images/91578514571_DV_resource.Stream@PNG-en-US.png)

| Setting/display |  |  | Description |
| --- | --- | --- | --- |
| "Trigger mode" |  |  | Selection of the trigger mode. |
|  | Drop-down list |  | The following settings are possible:  - "Start recording immediately"   The recording is made immediately after the device is activated. - "Trigger on tag"   The recording is made as soon as the installed trace is activated and the configured trigger condition is fulfilled. - "Trigger on fault"   The recording is started as soon as a fault is output on the drive. - "Trigger on alarm"   The recording is started as soon as an alarm is output on the drive. |
| "Trigger tag" |  |  | The "Trigger tag" specifies a signal that triggers the recording. |
|  | Input field |  | Enter a signal.   **Examples:**   - Missing enables r46 - Status word 1 r52 |
|  |  | ![Setting options and displays in "Recording conditions"](images/42119295115_DV_resource.Stream@PNG-de-DE.png) | Opens the signal selection table.  Clicking the icon opens a table which offers possible signals for selection as trigger tag. The selected signal is displayed in the input field. |
|  | Text field |  | Display of the trigger tag parameter number. |
| "Event" |  |  | The events that can be used on this trigger tag are offered for selection according to the data type of the trigger tag.  The event can only be configured when a valid signal has been entered as trigger tag. |
|  | Drop-down list |  | Event selection for which the trigger tag is checked.  The entries in the drop-down list are described in Section [Trigger event](#trigger-event). |
| Value |  |  | Configuration of the selected event.  The configuration options differ depending on the format of the trigger tag and the selected event.   See [Trigger event](#trigger-event). |
| "Cycle" |  |  | Cycle time with which the trace recording is to be made / has been made.  The possible cycle time depends on the number of signals to be recorded:  - Up to four signals: 0.5 ms minimum recording duration - As of five signals: 4.0 ms minimum recording duration |
| "Recording duration (a)" |  |  | Input of the recording duration in relation to the selection in the drop-down list. The possible total duration of the trace is shown to the right of the input field.  Activate the "Use max. recording duration" checkbox to record the maximum possible duration. The "Recording duration (a)" input field is then deactivated. The pre-trigger is part of the recording duration. If you record for 10 seconds (duration) and select 9 seconds as pre-trigger, then the recording is 10 seconds long, whereby 9 seconds are before the trigger event and 1 second after.  Note: The maximum recording duration depends on the set recording cycle and on the signals selected for recording. |
| "Use max. recording duration" |  |  | Set the recording duration to the maximum value.  When the checkbox is activated, the recording duration is set to the maximum possible recording duration.  The recording duration is also adapted when additional signals are added. |
| "Pre-trigger (b)" |  |  | "Pre-trigger" defines the time during which the signals are already recorded before the actual trigger condition is fulfilled.  The recording duration is not extended by the "pre-trigger". |

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

##### Bit pattern

The recording starts when the value of the trigger matches the bit pattern configured for this event. The assignment of the individual bits is displayed in the tooltip so that the relevant bits can be identified more easily.

The following figure shows the setting options for a "bit pattern":

![Bit pattern](images/91598704779_DV_resource.Stream@PNG-en-US.png)

It is possible to switch between the icons by clicking the respective button.

The following table shows the icons:

| Icon | Description |
| --- | --- |
| ![Bit pattern](images/42119233035_DV_resource.Stream@PNG-de-DE.png) | Bit is not evaluated |
| ![Bit pattern](images/42119241355_DV_resource.Stream@PNG-de-DE.png) | Bit is checked for FALSE |
| ![Bit pattern](images/42119249675_DV_resource.Stream@PNG-de-DE.png) | Bit is checked for TRUE |

---

**See also**

[User interface - Recording conditions](#user-interface---recording-conditions)

## Configuration

This section contains information on the following topics:

- [Trace configuration - overview](#trace-configuration---overview)
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
| 1 | Documentation of the configuration (optional)  Enter a comment and an author for the configuration in the Inspector window. |
| 2 | [Selecting signals](#selecting-signals)   Select the signals to be recorded in the "Signals" area. |
| 3 | [Configuring the recording conditions](#configuring-the-recording-conditions)   In the "Recording conditions" area, select whether the recording is to be performed immediately or depending on a trigger condition.  Also select a cycle and the recording duration. |

> **Note**
>
> **Importing of a trace configuration from a measurement**
>
> If you import a measurement exported with Startdrive V13 to a higher version (≥V14), the imported measurement contains the data recorded but no trace configuration.
>
> Measurements exported as of V14 also contain the trace configuration when importing to version V14 or higher.

### Selecting signals

#### Requirement

- A trace configuration has been created and selected by double-clicking in the project tree.
- The "Signals" area is open in the "Configuration" tab.

#### Procedure

To configure the signals to be recorded, proceed as follows:

1. Click in the first empty line of the table.
2. Click in the first empty cell of the "Name" column.
3. Select a signal. The following options are available:

   - In the "Name" column, click the ![Procedure](images/42119533579_DV_resource.Stream@PNG-de-DE.png) button and select a parameter.
   - In the "Name" column, enter the name or the parameter or part of the name in the cell. The field displays the possible parameters in the drop-down list.
   - The "Address" column displays the number of the parameter.
4. Click in the "Comment" column and enter a comment for the signal. After inserting the parameter, the parameter name is displayed first. This can be changed.
5. Repeat the procedure from step 1 until all the signals to be recorded have been entered in the table.

### Configuring the recording conditions

#### Requirement

- A trace configuration has been created and selected by double-clicking in the project tree.
- The "Recording conditions" area is open in the "Configuration" tab.

#### "Start recording immediately" trigger condition

To start the recording immediately, proceed as follows:

1. Select the "Start recording immediately" entry in the drop-down list for "Trigger mode".

   The input fields for the trigger parameter are hidden.
2. Enter the recording duration. The possible total duration is on the right.
3. Enter a recording cycle at "Cycle". The possible cycle settings depends on the number of signals.

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

#### "Trigger on fault"

To start the recording when a fault occurs, proceed as follows:

1. Select the "Trigger on fault" entry in the drop-down list for "Trigger mode".

   The input fields for the trigger parameters are hidden.
2. Enter the pre-trigger, recording duration and cycle (see above).

#### "Trigger on alarm" trigger condition

To start the recording when an alarm occurs, proceed as follows:

1. Select the "Trigger on alarm" entry in the drop-down list for "Trigger mode".

   The input fields for the trigger parameters are hidden.
2. Enter the pre-trigger, recording duration and cycle (see above).

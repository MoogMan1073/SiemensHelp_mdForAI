---
title: "S7-1500/S7-1500T Motion Control alarms and error IDs (S7-1500, S7-1500T)"
package: Alarm1500MCenUS
topics: 131
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# S7-1500/S7-1500T Motion Control alarms and error IDs (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Diagnostics concept (S7-1500, S7-1500T)](#diagnostics-concept-s7-1500-s7-1500t)
- [Technology alarms (S7-1500, S7-1500T)](#technology-alarms-s7-1500-s7-1500t)
- [Error IDs in Motion Control instructions (S7-1500, S7-1500T)](#error-ids-in-motion-control-instructions-s7-1500-s7-1500t)

## Diagnostics concept (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Diagnostics concept (S7-1500, S7-1500T)](#diagnostics-concept-s7-1500-s7-1500t-1)

### Diagnostics concept (S7-1500, S7-1500T)

The diagnostics concept encompasses alarms and associated messages, as well as error messages in the Motion Control instructions. The TIA Portal also supports you with consistency checks during configuration of the technology objects, and during the creation of your user program.

All alarms in runtime (from the CPU, technology, hardware etc.) are displayed in the Inspector window of the TIA Portal. Diagnostic information that relates to technology objects (technology alarms, status information) are additionally displayed in the Diagnostics window of the respective technology object.

During motion control, if an error occurs at a technology object (e.g. approaching a hardware limit switch), then a [technology alarm](#technology-alarms-s7-1500-s7-1500t) is triggered, and a corresponding message is displayed in the TIA Portal as well as on HMI devices.

In your user program, technology alarms are generally signaled via error bits in the technology data block. The number of the technology alarm with the highest priority is also displayed. In order to simplify error evaluation, the "Error" and "ErrorID" parameters of the Motion Control instructions also indicate that a technology alarm is pending.

[Program errors](#error-ids-in-motion-control-instructions-s7-1500-s7-1500t) can occur during parameter assignment or during the processing sequence of the Motion Control instructions (e.g. invalid parameter specification when calling the instruction, initiation of a job without enable via "MC_Power"). With active jobs, errors in Motion Control instructions are indicated by the "Error" and "ErrorID" parameters.

## Technology alarms (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of technology alarms (S7-1500, S7-1500T)](#short-description-of-technology-alarms-s7-1500-s7-1500t)
- [Overview of the technology alarms (S7-1500, S7-1500T)](#overview-of-the-technology-alarms-s7-1500-s7-1500t)
- [Technology alarms 101 - 114 (S7-1500, S7-1500T)](#technology-alarms-101---114-s7-1500-s7-1500t)
- [Technology alarms 201 - 204 (S7-1500, S7-1500T)](#technology-alarms-201---204-s7-1500-s7-1500t)
- [Technology alarms 304 - 343 (S7-1500, S7-1500T)](#technology-alarms-304---343-s7-1500-s7-1500t)
- [Technology alarms 401 - 431 (S7-1500, S7-1500T)](#technology-alarms-401---431-s7-1500-s7-1500t)
- [Technology alarms 501 - 563 (S7-1500, S7-1500T)](#technology-alarms-501---563-s7-1500-s7-1500t)
- [Technology alarms 601 - 612 (S7-1500, S7-1500T)](#technology-alarms-601---612-s7-1500-s7-1500t)
- [Technology alarms 700 - 758 (S7-1500, S7-1500T)](#technology-alarms-700---758-s7-1500-s7-1500t)
- [Technology alarms 801 - 820 (S7-1500T)](#technology-alarms-801---820-s7-1500t)
- [Technology alarms 900 - 903 (S7-1500T)](#technology-alarms-900---903-s7-1500t)
- [Technology alarms 1001 - 1012 (S7-1500T)](#technology-alarms-1001---1012-s7-1500t)

### Short description of technology alarms (S7-1500, S7-1500T)

If an error occurs at a technology object (e.g. approaching a hardware limit switch), a technology alarm is triggered and indicated. The impact of a technology alarm on the technology object is specified by the alarm response.

#### Alarm classes

Technology alarms are divided into three classes:

- **Acknowledgeable warning**

  The processing of Motion Control job is continued. The current motion of the axis can be influenced, e.g. by limiting the current dynamic values to the configured limit values.
- **Alarm requiring acknowledgment**

  Motion jobs are aborted in accordance with the alarm response. You must acknowledge the alarms in order to continue execution of new jobs after eliminating the cause of the error.
- **Fatal error**

  Motion jobs are aborted in accordance with the alarm response.

  To be able to use the technology object again after eliminating the cause of the error, you must restart the technology object.

#### Display of technology alarms

A technology alarm is displayed in the following locations:

- **TIA Portal**

  - **"Technology object &gt; Diagnostics &gt; Status and error bits"**

    Display of pending technology alarms for each technology object
  - **"Technology object &gt; Commissioning &gt; Axis control panel"**

    Display of the last pending technology alarm for each technology object
  - **"Inspector window &gt; Diagnostics &gt; Message display"**

    Select the "Receive messages" check box under "Online &amp; Diagnostics &gt; Online Access" in order to display technology alarms via the message display.

    With an online connection to the CPU, the pending technology alarms for all technology objects are displayed. Additionally, the archive view is available to you.

    The message display can also be activated and displayed on a connected HMI.
  - **"CPU &gt; Online &amp; diagnostics"**

    Display of the technology alarms that have been entered in the diagnostic buffer
- **User program**

  - **Tags "**
    **&lt;TO&gt;.ErrorDetail.Number**
    **" and "**
    **&lt;TO&gt;.ErrorDetail.Reaction**
    **"**

    Indication of the number and the reaction of the technology alarm with the highest priority
  - **Tag "**
    **&lt;TO&gt;.StatusWord**
    **"**

    A pending technology alarm is indicated with bit 1 ("Error").
  - **Tag "**
    **&lt;TO&gt;.ErrorWord**
    **"**

    Indication of alarms and fatal errors
  - **Tag "**
    **&lt;TO&gt;.WarningWord**
    **"**

    Indication of warnings
  - **Parameter "**
    **Error**
    **" and "**
    **ErrorID**
    **"**

    In a Motion Control instruction, the parameters "Error" = TRUE and "ErrorID" = 16#8001 indicate that a technology alarm is pending.
- **Display of the CPU**

  In order to show technology alarms on the CPU display, make the following setting when loading to the CPU:  
  In the "Load preview" dialog, select the action "Consistent download" for the "Text libraries" entry.
- **Web server**

  - **"Motion Control diagnostics &gt; Diagnostics"**

    Display of pending technology alarms for each technology object
  - **"Motion Control diagnostics &gt; Service overview"**

    Status display of technology objects

#### Alarm response

A technology-alarm always leads to an alarm response, which describes the effect on the technology object. The alarm response is specified by the system.

The following table shows possible alarm response:

| Alarm response | Validity |  | Description |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| No reaction (warnings only)  &lt;TO&gt;.ErrorDetail.Reaction = 0 | ✓ | ✓ | The processing of Motion Control job is continued. The current motion of the axis can be influenced, e.g. by limiting the current dynamic values to the configured limit values. |
| Stop with current dynamic values  &lt;TO&gt;.ErrorDetail.Reaction = 1 | ✓ | - | Active motion commands are aborted. The axis is braked with the dynamic values that present in the Motion Control instruction and brought to a standstill. |
| Stop with maximum dynamic values  &lt;TO&gt;.ErrorDetail.Reaction = 2 | ✓ | - | Active motion commands are aborted. The axis is braked with the dynamic values configured under "Technology object &gt; Extended parameters &gt; Dynamic limits", and brought to a standstill. The configured maximum jerk is hereby taken into account. |
| Stop with emergency stop ramp  &lt;TO&gt;.ErrorDetail.Reaction = 3 | ✓ | - | Active motion commands are aborted. The axis is braked with the emergency stop deceleration configured under "Technology object &gt; Extended parameters &gt; Emergency stop ramp", without any jerk limit, and brought to a standstill. |
| Remove enable  &lt;TO&gt;.ErrorDetail.Reaction = 4 | ✓ | - | Active motion commands are aborted. The setpoint zero is output and the enable is removed. The axis is braked to a standstill according to the configuration in the drive. |
| Track setpoints  &lt;TO&gt;.ErrorDetail.Reaction = 5 | ✓ | - | Active motion commands are aborted. The setpoint zero is output. The actual values supplied by the drive are automatically tracked as setpoints. |
| Terminate processing of the technology object:  - Output cam   &lt;TO&gt;.ErrorDetail.Reaction = 6 - Cam track   &lt;TO&gt;.ErrorDetail.Reaction = 7 - Measuring input   &lt;TO&gt;.ErrorDetail.Reaction = 8 - Cam   &lt;TO&gt;.ErrorDetail.Reaction = 9 - External encoder   &lt;TO&gt;.ErrorDetail.Reaction = 10 - Leading axis proxy   &lt;TO&gt;.ErrorDetail.Reaction = 13 | ✓ | - | Processing of the technology object is terminated. All running Motion Control jobs are aborted. |
| Stop without leaving the path  &lt;TO&gt;.ErrorDetail.Reaction = 11 | - | ✓ | The kinematics are decelerated and brought to a standstill. The current path is not exited when the kinematics is stopped. Linear and circular motion jobs are braked without jerk limit. |
| Stop with maximum dynamic values of the axes  &lt;TO&gt;.ErrorDetail.Reaction = 12 | - | ✓ | Active and queued motion jobs are canceled. The axes are decelerated with the maximum dynamic values configured under "Technology object &gt; Configuration &gt; Extended parameters &gt; Limits &gt; Dynamic limits", and brought to a standstill. The configured maximum jerk is hereby taken into account. |
| Stop Interpreter program with diagnostics option  &lt;TO&gt;.ErrorDetail.Reaction = 14 | ✓ | - | Execution of the Interpreter program is stopped. One diagnostic option is to read out the last values, for example. |
| Stop and recompile Interpreter program  &lt;TO&gt;.ErrorDetail.Reaction = 15 | ✓ | - | Execution of the Interpreter program is stopped. The Interpreter program is prepared for another execution. The preparation of the Interpreter program starts. All parameters are reinitialized. The Interpreter program can be executed again. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Acknowledging technology alarms

You can acknowledge technology alarms as follows:

- **TIA Portal**

  - **"Technology object &gt; Commissioning &gt; Axis control panel"**

    Click "Confirm" to acknowledge all alarms and warnings pending for the selected technology object.
  - **"Inspector window &gt; Diagnostics &gt; Message display"**

    You can acknowledge the alarms and warnings for all technology objects either individually, or all at once.
- **HMI**

  At an HMI with enabled message display, you can acknowledge the alarms and warnings for all technology objects either individually, or all at once.
- **User program**

  Acknowledge pending technology alarms for a technology object with the Motion Control instruction "MC_Reset".
- **CPU display**

  Acknowledge pending technology alarms via the display of the CPU.
- **Web server**

  Acknowledge pending technology alarms under "Alarms".

### Overview of the technology alarms (S7-1500, S7-1500T)

The following table shows an overview of the technology alarms and the corresponding alarm responses. When a technology alarm occurs, evaluate the entire indicated alarm text, in order to find the precise cause.

#### Legend

| Table column |  | Description |
| --- | --- | --- |
| No. |  | Number of the technology alarm  (corresponds to "&lt;TO&gt;.ErrorDetail.Number") |
| Validity |  | Validity of the descriptions for the technology objects |
|  | TO | Applies to all technology objects with the exception of the Kinematics technology object. |
| Kin | Applies only to the Kinematics technology object. |  |
| Reaction |  | Effective alarm response  (corresponds to "&lt;TO&gt;.ErrorDetail.Reaction") |
| F |  | Error bit  Bit that is set in "&lt;TO&gt;.ErrorWord" when the technology alarm occurs  A description of the bits can be found in the tags of the corresponding technology object. |
| W |  | Warning bit  Bit that is set in "&lt;TO&gt;.WarningWord" when the technology alarm occurs  A description of the bits can be found in the tags of the corresponding technology object. |
| R |  | Restart  To acknowledge the technology alarm, the technology object must be reinitialized (Restart). |
| D |  | Diagnostic buffer  The alarm is entered in the diagnostic buffer. |
| Alarm text |  | Displayed alarm text |

#### List of the technology alarms

| No. | Validity |  | Reaction | F | W | R | D | Alarm text |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TO | Kin |  |  |  |  |  |  |  |
| [101](#technology-alarm-101-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | ✓ | ✓ | Configuration error. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| ✓ | - | Interpreter technology object:  Stop Interpreter program with diagnostics option | X1 | - | -<sup>1)</sup> | ✓ |  |  |
| [102](#technology-alarm-102-s7-1500-s7-1500t) | ✓ | - | Remove enable | X15 | - | ✓ | ✓ | Error in drive configuration adaptation. |
| [103](#technology-alarm-103-s7-1500-s7-1500t) | ✓ | - | Remove enable | X15 | - | ✓ | ✓ | Encoder configuration adaptation error. |
| [104](#technology-alarm-104-s7-1500-s7-1500t) | ✓ | - | Stop with maximum dynamic values | X1 | - | - | - | SW limit switch specification error. |
| [105](#technology-alarm-105-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | ✓ | ✓ | Drive configuration error. |
| [106](#technology-alarm-106-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | - | ✓ | Drive connection configuration error. |
| [107](#technology-alarm-107-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | ✓ | ✓ | Encoder configuration error. |
| [108](#technology-alarm-108-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | - | ✓ | Encoder connection configuration error. |
| [109](#technology-alarm-109-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | ✓ | - | Configuration error. |
| [110](#technology-alarm-110-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X1 | - | - | Configuration is adjusted internally. |
| [111](#technology-alarm-111-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X15 | - | ✓ | TO and drive configuration inconsistent. |
| [112](#technology-alarm-112-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X15 | - | ✓ | TO and encoder configuration inconsistent. |
| [113](#technology-alarm-113-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | ✓ | - | Isochronous mode not possible. |
| [114](#technology-alarm-114-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | ✓ | ✓ | Cross-PLC synchronous operation configuration error. |
| [201](#technology-alarm-201-s7-1500-s7-1500t) | ✓ | - | Remove enable | X0 | - | ✓ | ✓ | Internal error. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| ✓ | - | Interpreter technology object:  Stop Interpreter program with diagnostics option | X0 | - | -<sup>2)</sup> | ✓ |  |  |
| [202](#technology-alarm-202-s7-1500-s7-1500t) | ✓ | - | No reaction | X0 | - | ✓ | - | Internal configuration error. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| ✓ | - | Interpreter technology object:  Stop Interpreter program with diagnostics option | X0 | - | -<sup>2)</sup> | - |  |  |
| [203](#technology-alarm-203-s7-1500-s7-1500t) | ✓ | - | Remove enable | X0 | - | ✓ | - | Internal error. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| [204](#technology-alarm-204-s7-1500-s7-1500t) | ✓ | - | Remove enable | X0 | - | - | - | Commissioning error. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| ✓ | - | Interpreter technology object:  No reaction | X0 | - | -<sup>2)</sup> | - |  |  |
| [304](#technology-alarm-304-s7-1500-s7-1500t) | ✓ | - | Stop with emergency stop ramp | X2 | - | - | - | Velocity limit is zero. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| [305](#technology-alarm-305-s7-1500-s7-1500t) | ✓ | - | Stop with emergency stop ramp | X2 | - | - | - | - Limit value of the acceleration is zero. - Limit value of the deceleration is zero. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| [306](#technology-alarm-306-s7-1500-s7-1500t) | ✓ | - | Stop with emergency stop ramp | X2 | - | - | - | Jerk limit is zero. |
| - | ✓ | Stop with maximum dynamic values of the axes |  |  |  |  |  |  |
| [307](#technology-alarm-307-s7-1500-s7-1500t) | ✓ | - | Stop with maximum dynamic values | X2 | - | - | ✓ | - Negative numerical value range of the position reached. - Positive numerical value range of the position reached. |
| [308](#technology-alarm-308-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | ✓ | - Negative numerical value range of the position exceeded. - Positive numerical value range of the position exceeded. |
| [321](#technology-alarm-321-s7-1500-s7-1500t) | ✓ | - | Stop with emergency stop ramp | X3 | - | - | - | Axis is not homed. |
| [322](#technology-alarm-322-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X3 | - | - | Restart not executed. |
| ✓ | - | Interpreter technology object:  No reaction | X0 | X3 | -<sup>2)</sup> | - |  |  |
| [323](#technology-alarm-323-s7-1500-s7-1500t) | ✓ | - | Remove enable | X3 | - | - | - | Homing could not be performed. |
| [341](#technology-alarm-341-s7-1500-s7-1500t) | ✓ | - | Stop with maximum dynamic values | X10 | - | - | - | Homing data faulty. |
| [342](#technology-alarm-342-s7-1500-s7-1500t) | ✓ | - | Stop with emergency stop ramp | X10 | - | - | - | Reference cam/encoder zero mark not found. |
| [343](#technology-alarm-343-s7-1500-s7-1500t) | ✓ | - | Remove enable | X1 | - | - | - | Homing function not supported by device. |
| [401](#technology-alarm-401-s7-1500-s7-1500t) | ✓ | - | Remove enable | X13 | - | - | ✓ | Error accessing logical address. |
| [411](#technology-alarm-411-s7-1500-s7-1500t) | ✓ | - | Remove enable | X5 | - | - | ✓ | Encoder at the logical address disrupted. |
| [412](#technology-alarm-412-s7-1500-s7-1500t) | ✓ | - | Remove enable | X5 | - | - | - | Permitted actual value range exceeded. |
| [421](#technology-alarm-421-s7-1500-s7-1500t) | ✓ | - | Remove enable | X4 | - | - | ✓ | Drive disrupted at the logical address. |
| [431](#technology-alarm-431-s7-1500-s7-1500t) | ✓ | - | Remove enable | X7 | - | - | ✓ | Communication to the device under logical address is disturbed. |
| [501](#technology-alarm-501-s7-1500-s7-1500t) | ✓ | ✓ | No reaction | - | X6 | - | - | Programmed velocity is limited. |
| [502](#technology-alarm-502-s7-1500-s7-1500t) | ✓ | ✓ | No reaction | - | X6 | - | - | - Programmed acceleration is being limited. - Programmed deceleration is being limited. |
| [503](#technology-alarm-503-s7-1500-s7-1500t) | ✓ | ✓ | No reaction | - | X6 | - | - | Programmed jerk is limited. |
| [504](#technology-alarm-504-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X6 | - | - | Speed setpoint monitoring active. |
| [511](#technology-alarm-511-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X6 | - | - | Dynamic limit is violated by the kinematics motion. |
| [521](#technology-alarm-521-s7-1500-s7-1500t) | ✓ | - | Remove enable | X11 | - | - | - | Following error. |
| [522](#technology-alarm-522-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X11 | - | - | Warning following error tolerance. |
| [531](#technology-alarm-531-s7-1500-s7-1500t) | ✓ | - | Remove enable | X9 | - | - | - | - Positive HW limit switch approached. - Negative HW limit switch approached. - Invalid retraction direction, HW limit switch active. |
| ✓ | - | - HW limit switch polarity reversed, retraction not possible. - Both HW limit switches active, retraction not possible. - Encoder error with triggered HW limit switch, no retraction possible. |  |  |  |  |  |  |
| [533](#technology-alarm-533-s7-1500-s7-1500t) | ✓ | - | The alarm response depends on the configured response and the type of axis motion.  - Stop with maximum dynamic values   When "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 0 and an interconnected axis.   - Axis motion as following axis in synchronous operation   - Kinematics axis in kinematics motion - Stop with current dynamic values   When "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 1 and interconnected axis | X8 | - | - | - | - Negative SW limit switch is approached. - Positive SW limit switch is approached. |
| [534](#technology-alarm-534-s7-1500-s7-1500t) | ✓ | - | You can configure the alarm response.  - Remove enable   Setting: "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 0 - Stop with emergency stop ramp    Setting: "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 1 | X8 | - | - | - | - Negative SW limit switch was overtraveled. - Positive SW limit switch was overtraveled. |
| [541](#technology-alarm-541-s7-1500-s7-1500t) | ✓ | - | Remove enable | X12 | - | - | - | Positioning monitoring error. |
| [542](#technology-alarm-542-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Clamping monitoring error: Axis leaving clamping tolerance window. |
| [550](#technology-alarm-550-s7-1500-s7-1500t) | ✓ | - | Track setpoints | X13 | - | - | - | Drive-autonomous motion is being executed. |
| [551](#technology-alarm-551-s7-1500-s7-1500t) | ✓ | - | No reaction | - | X6 | - | - | Maximum velocity cannot be reached with drive/axis parameters. |
| [552](#technology-alarm-552-s7-1500-s7-1500t) | ✓ | - | Remove enable | X15 | - | - | - | Encoder adaptation error during ramp-up. |
| [561](#technology-alarm-561-s7-1500t) | - | ✓ | No reaction | - | X6 | - | - | Programmed velocity of the orientation motion is limited. |
| [562](#technology-alarm-562-s7-1500t) | - | ✓ | No reaction | - | X6 | - | - | - Programmed acceleration of the orientation motion is limited. - Programmed deceleration of the orientation motion is limited. |
| [563](#technology-alarm-563-s7-1500t) | - | ✓ | No reaction | - | X6 | - | - | Programmed jerk of the orientation motion is limited. |
| [601](#technology-alarm-601-s7-1500-s7-1500t) | ✓ | - | Stop with maximum dynamic values | X14 | - | - | - | Leading axis is not assigned or defective. |
| [603](#technology-alarm-603-s7-1500-s7-1500t) | ✓ | - | Remove enable | X14 | - | - | - | Leading axis is not in position-controlled mode. |
| [608](#technology-alarm-608-s7-1500-s7-1500t) | ✓ | - | Stop with maximum dynamic values | X14 | - | - | - | Error during synchronization/desynchronization. |
| [612](#technology-alarm-612-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Specified cyclic cam has not been interpolated. |
| [700](#technology-alarm-700-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Error when calculating the switching position. |
| [701](#technology-alarm-701-s7-1500-s7-1500t) | ✓ | - | Remove enable | X13 | - | - | - | I/O output error. |
| [702](#technology-alarm-702-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Position value invalid. |
| [703](#technology-alarm-703-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Cam track data faulty. |
| [704](#technology-alarm-704-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Output cam data faulty. |
| [750](#technology-alarm-750-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Measuring job not possible during homing of assigned axis. |
| [752](#technology-alarm-752-s7-1500-s7-1500t) | ✓ | - | No reaction | X2 | - | - | - | Validity range of measuring job not recognized. |
| [753](#technology-alarm-753-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Only one measuring input can access an encoder at a time. |
| [754](#technology-alarm-754-s7-1500-s7-1500t) | ✓ | - | Remove enable | X2 | - | - | - | Measuring input configuration in external device is not correct. |
| [755](#technology-alarm-755-s7-1500-s7-1500t) | ✓ | - | Remove enable | X13 | - | - | - | Measuring job not possible. |
| [758](#technology-alarm-758-s7-1500-s7-1500t) | ✓ | - | No reaction | X2 | - | - | - | A measuring edge was not evaluated. |
| [801](#technology-alarm-801-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X2 | - | - | - | Kinematics axis not ready. |
| [802](#technology-alarm-802-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X3 | - | - | - | Cannot calculate the geometry element. |
| [803](#technology-alarm-803-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X4 | - | - | - | Error in the calculation of the transformation. |
| [804](#technology-alarm-804-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X2 | - | - | - | Kinematics motion cannot be stopped at the end. |
| [805](#technology-alarm-805-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X2 | - | - | - | Limitation of path dynamics by axis dynamics incorrect. |
| [806](#technology-alarm-806-s7-1500t) | - | ✓ | Stop without leaving the path | X2 | - | - | - | Zone violation of work or blocked zones. |
| [807](#technology-alarm-807-s7-1500t) | - | ✓ | No reaction | - | X2 | - | - | Zone violation of signal zones. |
| [808](#technology-alarm-808-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X2 | - | - | - | Ambiguity due to multiple active work zones. |
| [809](#technology-alarm-809-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X2 | - | - | - | Path dynamic limit through dynamic response of the orientation motion faulty. |
| [810](#technology-alarm-810-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X7 | - | - | - | Conveyor belt not assigned or faulty (OCS &lt;number&gt;). |
| [811](#technology-alarm-811-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X7 | - | - | - | Error when approaching the TCP to an object coordinate system (OCS &lt;number&gt;). |
| [812](#technology-alarm-812-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X4 | - | - | - | Error in the treatment of singularities.  - The kinematics has reached the singularity. - Too many singularities occur in the path command. |
| [820](#technology-alarm-820-s7-1500t) | - | ✓ | Stop with maximum dynamic values of the axes | X8 | - | - | - | - Upper limit of joint traversing range joint &lt;No.&gt; overtraveled. - Lower limit of joint traversing range joint &lt;No.&gt; overtraveled. |
| [900](#technology-alarm-900-s7-1500t) | ✓ | - | Set leading value invalid | X2 | - | - | ✓ | Leading values invalid. |
| [901](#technology-alarm-901-s7-1500t) | ✓ | - | Set leading value invalid | X2 | - | - | ✓ | Data transmission error. |
| [902](#technology-alarm-902-s7-1500t) | ✓ | - | No reaction | - | X2 | - | - | Leading value accuracy limited. |
| [903](#technology-alarm-903-s7-1500t) | ✓ | - | Set leading value invalid | X2 | - | ✓ | ✓ | Modulo settings of the leading axis changed in cyclic mode. |
| [1001](#technology-alarm-1001-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Configuration error Interpreter or max. Interpreter program configuration limits reached. |
| [1002](#technology-alarm-1002-s7-1500t) | ✓ | - | Stop Interpreter program with diagnostics option | X5 | - | - | ✓ | Configuration error Interpreter or max. Interpreter mapping configuration limits reached. |
| [1003](#technology-alarm-1003-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Syntax error Interpreter program. |
| [1004](#technology-alarm-1004-s7-1500t) | ✓ | - | Stop Interpreter program with diagnostics option | X5 | - | - | ✓ | Syntax error Interpreter mapping. |
| [1005](#technology-alarm-1005-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Semantic error Interpreter program. |
| [1006](#technology-alarm-1006-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X5 | - | - | ✓ | Semantic error Interpreter mapping. |
| [1007](#technology-alarm-1007-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Parameter error Interpreter instruction. |
| [1008](#technology-alarm-1008-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Processing error Interpreter instruction. |
| [1009](#technology-alarm-1009-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | ✓ | Processing error synchronous action. |
| [1010](#technology-alarm-1010-s7-1500t) | ✓ | - | Stop and recompile Interpreter program | X4 | - | - | - | Processing error synchronous start. |
| [1011](#technology-alarm-1011-s7-1500t) | ✓ | - | Stop Interpreter program with diagnostics option | X5 | - | - | ✓ | Error when mapping technology objects. |
| [1012](#technology-alarm-1012-s7-1500t) | ✓ | - | No reaction | - | X4 | - | - | Critical programming |
| <sup>1)</sup> To acknowledge the technology alarm, the Interpreter technology object must be enabled.   <sup>2)</sup> To acknowledge the technology alarm, the execution of the Interpreter program must be restarted. |  |  |  |  |  |  |  |  |

### Technology alarms 101 - 114 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 101 (S7-1500, S7-1500T)](#technology-alarm-101-s7-1500-s7-1500t)
- [Technology alarm 102 (S7-1500, S7-1500T)](#technology-alarm-102-s7-1500-s7-1500t)
- [Technology alarm 103 (S7-1500, S7-1500T)](#technology-alarm-103-s7-1500-s7-1500t)
- [Technology alarm 104 (S7-1500, S7-1500T)](#technology-alarm-104-s7-1500-s7-1500t)
- [Technology alarm 105 (S7-1500, S7-1500T)](#technology-alarm-105-s7-1500-s7-1500t)
- [Technology alarm 106 (S7-1500, S7-1500T)](#technology-alarm-106-s7-1500-s7-1500t)
- [Technology alarm 107 (S7-1500, S7-1500T)](#technology-alarm-107-s7-1500-s7-1500t)
- [Technology alarm 108 (S7-1500, S7-1500T)](#technology-alarm-108-s7-1500-s7-1500t)
- [Technology alarm 109 (S7-1500, S7-1500T)](#technology-alarm-109-s7-1500-s7-1500t)
- [Technology alarm 110 (S7-1500, S7-1500T)](#technology-alarm-110-s7-1500-s7-1500t)
- [Technology alarm 111 (S7-1500, S7-1500T)](#technology-alarm-111-s7-1500-s7-1500t)
- [Technology alarm 112 (S7-1500, S7-1500T)](#technology-alarm-112-s7-1500-s7-1500t)
- [Technology alarm 113 (S7-1500, S7-1500T)](#technology-alarm-113-s7-1500-s7-1500t)
- [Technology alarm 114 (S7-1500, S7-1500T)](#technology-alarm-114-s7-1500-s7-1500t)

#### Technology alarm 101 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Configuration error.** |  | ✓ | ✓ |  |
|  | Value in &lt;tag&gt; not allowed. | ✓ | ✓ | Adjust the specified value. |
| Value in Kinematics.TypeOfKinematics not permissible. |  |  | - Select a valid kinematics type. - If you are using a kinematics type with more than 4 interpolating axes, ensure that the "S7-1500T Motion Control KinPlus" motion control package is supported by the CPU and is loaded into the CPU and activated. |  |
| Faulty load gear factors. | ✓ | - | Adjust the load gear factors in the "&lt;TO&gt;.LoadGear.Numerator" and/or "&lt;TO&gt;.LoadGear.Denominator" parameters. |  |
| At least one encoder required. Sensor[].existent | ✓ | - | Configure at least one encoder. |  |
| Sensor[1] must be configured for DSC. | ✓ | - | Configure Sensor[1]. |  |
| Values in Sensor[1..4].Parameter.FineResolutionXist1 and p979 are not equal. | ✓ | - | Set the identical fine resolution on the technology as on the drive. |  |
| Encoder position cannot be displayed due to the encoder configuration/mechanics. | ✓ | - | Check the configuration of the encoder and mechanics. |  |
| Linear encoder in not permitted on rotary drive system (Sensor.System). | ✓ | - |  |  |
| Backlash compensation not permitted with encoder on load side. | ✓ | - |  |  |
| Controller parameter incorrect. | ✓ | - | Adjust the value of the "&lt;TO&gt;.PositionController.Kv" parameter. |  |
| PROFIBUS parameter assignment inconsistent. Sum of Ti and To greater than send clock. | ✓ | - | Adjust the send clock in the hardware configuration. |  |
| Drive or drive telegram type or encoder not suitable for DSC. | ✓ | - | Check whether the drive can be operated with DSC and adjust the drive telegram if required. |  |
| Technology data block is only possible with digital drive coupling. | ✓ | - | Check the drive coupling. |  |
| The VREF of the analog output or the bit drivers are assigned multiple times. | ✓ | - | Make sure that different addresses are assigned for all technology objects in the project. |  |
| TimeOut parameter outside of limits. | ✓ | - | Set the monitoring time of the axis control panel to a valid value. |  |
| Telegram in Actor.Interface.AddressIn and AddressOut not equal. | ✓ | - | Set the identical drive telegram type for sending and receiving direction. |  |
| Illegal combination for homing data with incremental encoder. encoder. | ✓ | - | Check the active and passive homing settings. |  |
| Telegram in Sensor[1..4].Interface.AddressIn and AddressOut not equal. | ✓ | - | Set the identical encoder telegram type for sending and receiving direction. |  |
| Kinematics axis A&lt;No.&gt; not connected | - | ✓ | Interconnect the axis. |  |
| Delta picker 2D: No formation of a closed parallel structure. | - | ✓ | Adjust the geometry data of the mechanics. |  |
| Delta picker 3D: No formation of a closed parallel structure. | - | ✓ |  |  |
| Delta picker 3D: Angular offset does not permit a third arm. | - | ✓ |  |  |
| Invalid arm distances. | - | ✓ |  |  |
| Tripod: Angular offset does not permit a third arm. | - | ✓ |  |  |
| Multiple versions of the same kinematics axis specified as AxisCoupling.N[].CausingAxis. | - | ✓ | Adjust the configuration for the mechanical axis coupling. |  |
| Kinematics axes coupled in a circle under AxisCoupling.N[]. | - | ✓ |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 102 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |  |
| **Drive configuration adaptation error.** |  |  | ✓ | - |  |
|  | Drive is not assigned to a SINAMICS device. |  | ✓ | - | The drive adaptation is only available for SINAMICS drives. |
| Parameter does not exist, value unreadable or invalid. |  | ✓ | - | Check whether your device supports acyclic data communication according to PROFIdrive. |  |
|  | Maximum speed. | ✓ | - |  |  |
| Maximum torque (p1520). | ✓ | - |  |  |  |
| Maximum torque (p1521) | ✓ | - |  |  |  |
| Fine resolution torque. | ✓ | - |  |  |  |
| Rated speed. | ✓ | - |  |  |  |
| Rated torque. | ✓ | - |  |  |  |
| Motor type. | ✓ | - |  |  |  |
| Unspecified. | ✓ | - |  |  |  |
| Adaptation canceled due to insufficient resources. |  | ✓ | - |  |  |
| Drive is not interconnected directly to I/O area. |  | ✓ | - | In the configuration of the axis, the logical addresses were placed, for example, in a data block. The adaptation is only possible when the encoder has been directly interconnected to an I/O area. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |  |

#### Technology alarm 103 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |  |
| **Encoder configuration adaptation error.** |  |  | ✓ | - |  |
|  | Encoder is not assigned to a SINAMICS device. |  | ✓ | - | The encoder adaptation is only available for SINAMICS devices and external Siemens encoders. |
| Parameter does not exist, value unreadable or invalid. |  | ✓ | - | Check whether your device supports acyclic data communication according to PROFIdrive. |  |
|  | Encoder system | ✓ | - |  |  |
| Encoder resolution | ✓ | - |  |  |  |
| Encoder fine resolution Gx_XIST1 | ✓ | - |  |  |  |
| Encoder fine resolution Gx_XIST2 | ✓ | - |  |  |  |
| Encoder revolutions | ✓ | - |  |  |  |
| Unspecified | ✓ | - |  |  |  |
| Adaptation canceled due to insufficient resources. |  | ✓ | - |  |  |
| Encoder is not interconnected directly to I/O area. |  | ✓ | - | In the configuration of the axis, the logical addresses were placed, for example, in a data block. The adaptation is only possible when the encoder has been directly interconnected to an I/O area. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |  |

#### Technology alarm 104 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with maximum dynamic values

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **SW limit switch specification error.** |  | ✓ | - |  |
|  | Neg. SW limit switch greater than pos. SW limit switch. | ✓ | - | Change the position of the software limit switches. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 105 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Drive configuration error.** |  | ✓ | - |  |
|  | HW Configuration. | ✓ | - | - Connect a suitable device. - Check the device (I/Os). - Check the topology of the project. - Compare the device configuration and the configuration of the technology object. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| The TO needs a smaller servo cycle clock. | ✓ | - |  |  |
| Error in internal communication. | ✓ | - | - Check the project for consistency and reload the project into the controller. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |  |
| Address for drive data does not exist in project. | ✓ | - | Check the project for consistency and reload the project into the controller. |  |
| Error during the parameter assignment of the frame for the torque data. | ✓ | - | Check the interconnection of the SIEMENS additional telegram 750 (torque data). |  |
| Address overlap during drive interconnection. | ✓ | - | Make sure that different addresses are assigned for all technology objects in the project. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 106 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Drive connection configuration error.** |  | ✓ | - |  |
|  | System has no communication with drive. | ✓ | - | Internal system error.  - Check the project for consistency and reload the project into the controller. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| Drive not initialized during ramp-up. | ✓ | - | - Ensure that the communication between the controller and drive is established. To do this, evaluate the "&lt;TO&gt;.StatusDrive.CommunicationOK" parameter before enabling the axis. - To enable a technology object, the drive initialization must be complete. Trigger the job again later. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 107 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Encoder configuration error.** |  | ✓ | - |  |
|  | HW Configuration. | ✓ | - | - Connect a suitable device. - Check the device (I/Os). - Check the topology of the project. - Compare the device configuration and the configuration of the technology object. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| The TO needs a smaller servo cycle clock. | ✓ | - |  |  |
| Error in internal communication. | ✓ | - | - Check the project for consistency and reload the project into the controller. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |  |
| Address overlap during encoder interconnection. | ✓ | - | Make sure that different addresses are assigned for all technology objects in the project. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 108 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Encoder connection configuration error.** |  | ✓ | - |  |
|  | System without communication to encoder. | ✓ | - | Internal system error.  - Check the project for consistency and reload the project into the controller. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| Encoder not initialized during ramp-up. | ✓ | - | - Ensure that the communication between the controller and encoder is established. To do this, evaluate the "&lt;TO&gt;.StatusSensor[1..4].CommunicationOK" parameter before enabling the axis and also check if the status of the encoder actual value is "&lt;TO&gt;.StatusSensor[1..4].State" = VALID (2). - To enable a technology object, the encoder initialization must be complete. Trigger the job again later. |  |
| Encoder data address missing in project. | ✓ | - | Check the project for consistency and reload the project into the controller. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 109 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Configuration error.** |  | ✓ | - |  |
|  | Neg. HW limit switch. | ✓ | - | - Connect a suitable device. - Check the device (I/Os). - Check the topology of the project. - Compare the device configuration and the configuration of the technology object. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| Pos. HW limit switch | ✓ | - |  |  |
| Reference cam "Active homing". | ✓ | - |  |  |
| Reference cam "Passive homing". | ✓ | - |  |  |
| Enable bit for the analog drive interface. | ✓ | - |  |  |
| DriveReady bit of the analog drive interface. | ✓ | - |  |  |
| Input for measuring input faulty. | ✓ | - |  |  |
| Output cam output faulty. | ✓ | - |  |  |
| Data exchange with the drive. | ✓ | - | - Check whether telegram 750 has been created. - Check the configuration of the logical address. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 110 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Configuration is adjusted internally.** |  | ✓ | - |  |
|  | Actor.DriveParameter.MaxSpeed is limited. | ✓ | - | - Correct the reference speed in the drive and in the technology object "&lt;TO&gt;.Actor.DriveParameter.ReferenceSpeed". The reference speed (parameter p2000) must be at least half the maximum speed (parameter p1082) "&lt;TO&gt;.Actor.DriveParameter.ReferenceSpeed" ≥ 0.5 "&lt;TO&gt;.Actor.DriveParameter.MaxSpeed". - During the automatic transfer of the drive parameters to the technology object during runtime (online), slight accuracy deviations may occur from the reference speed and maximum speed configured in the drive. - With analog drive connection, correct the reference value in the drive and in the configuration of the technology object to "&lt;TO&gt;.Actor.MaxSpeed" / 1.17. |
| PositioningMonitoring.ToleranceTime is limited. | ✓ | - | Change the configuration data. |  |
| DynamicDefaults.EmergencyDeceleration is limited. | ✓ | - |  |  |
| DriveParameter.ReferenceTorque too low. | ✓ | - |  |  |
| Sensor[].Backlash.Size is limited. | ✓ | - |  |  |
| Sensor[].Backlash.Velocity is limited. | ✓ | - |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 111 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **TO and drive configuration inconsistent.** |  | ✓ | - |  |
|  | Different telegram. | ✓ | - | Match the telegram configuration for the technology object with the telegram configuration in the drive (p922 in the drive). |
| Incompatible torque resolution. | ✓ | - | Adjust the high torque resolution for the drive. |  |
| Application cycle of the drive and servo cycle are different. | ✓ | - | Adjust the application cycle of the drive in the device configuration for the PROFIBUS drive. |  |
| Application cycle of the drive and processing cycle of the TO are different. | ✓ | - |  |  |
| Linear motor configured. | ✓ | - | Set round-frame motor (P300) in the drive. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 112 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **TO and encoder configuration inconsistent.** |  | ✓ | - |  |
|  | Different telegram type. | ✓ | - | Match the telegram configuration for the technology object with the telegram configuration in the encoder. |
| Encoder is not an absolute encoder. | ✓ | - | Configure the encoder for the technology object as absolute encoder. |  |
| Application cycle of the encoder and servo cycle are different. | ✓ | - | Adjust the application cycle of the encoder in the device configuration for the PROFIBUS encoder. |  |
| Application cycle of the encoder and processing cycle of the TO are different. | ✓ | - |  |  |
| Encoder is not an incremental encoder. | ✓ | - | Configure the encoder for the technology object as an incremental encoder. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 113 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Isochronous mode not possible.** | ✓ | - | - The configured output for the technology object output cam or cam track or input for the technology object measuring input cannot be used in isochronous mode.   Configure the I/O in the device configuration as isochronous I/O. - The maximum permissible application cycle T<sub>Servo</sub> has been exceeded.   When using SINAMICS sensors, the maximum application cycle may be up to 8 ms. - Make sure that the organization block MC_Servo is called synchronously with the bus system. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 114 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Cross-PLC synchronous operation configuration error.** |  | ✓ | - |  |
|  | Configuration error. | ✓ | - | Check the configuration of the interconnected leading and following axes. Make sure that all relevant tags are correctly configured for cross-PLC synchronous operation. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Technology alarms 201 - 204 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 201 (S7-1500, S7-1500T)](#technology-alarm-201-s7-1500-s7-1500t)
- [Technology alarm 202 (S7-1500, S7-1500T)](#technology-alarm-202-s7-1500-s7-1500t)
- [Technology alarm 203 (S7-1500, S7-1500T)](#technology-alarm-203-s7-1500-s7-1500t)
- [Technology alarm 204 (S7-1500, S7-1500T)](#technology-alarm-204-s7-1500-s7-1500t)

#### Technology alarm 201 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Internal error.** | ✓ | ✓ | Open a Support request.  The following data is required for the error analysis:  - The service data of the CPU directly after the occurrence of the error   (Online &amp; diagnostics &gt; Functions &gt; Save service data) - The diagnostic buffer of the CPU as text file   (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer) - The software installed on the PG as an export file   (Help &gt; Service &amp; Support in TIA Portal &gt; Support request) - The project in the state that led to this alarm - The password for the project - Steps for reproduction |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

#### Technology alarm 202 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Internal configuration error.** | ✓ | ✓ | Open a Support request.  The following data is required for the error analysis:  - The service data of the CPU directly after the occurrence of the error   (Online &amp; diagnostics &gt; Functions &gt; Save service data) - The diagnostic buffer of the CPU as text file   (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer) - The software installed on the PG as an export file   (Help &gt; Service &amp; Support in TIA Portal &gt; Support request) - The project in the state that led to this alarm - The password for the project - Steps for reproduction |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

#### Technology alarm 203 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Internal error.** | ✓ | ✓ | Open a Support request.  The following data is required for the error analysis:  - The service data of the CPU directly after the occurrence of the error   (Online &amp; diagnostics &gt; Functions &gt; Save service data) - The diagnostic buffer of the CPU as text file   (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer) - The software installed on the PG as an export file   (Help &gt; Service &amp; Support in TIA Portal &gt; Support request) - The project in the state that led to this alarm - The password for the project - Steps for reproduction |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

#### Technology alarm 204 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Alarm response interpreter: No reaction

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Commissioning error.** |  | ✓ | ✓ |  |
|  | Connection to the TIA Portal interrupted. | ✓ | ✓ | Check the connection properties. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Technology alarms 304 - 343 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 304 (S7-1500, S7-1500T)](#technology-alarm-304-s7-1500-s7-1500t)
- [Technology alarm 305 (S7-1500, S7-1500T)](#technology-alarm-305-s7-1500-s7-1500t)
- [Technology alarm 306 (S7-1500, S7-1500T)](#technology-alarm-306-s7-1500-s7-1500t)
- [Technology alarm 307 (S7-1500, S7-1500T)](#technology-alarm-307-s7-1500-s7-1500t)
- [Technology alarm 308 (S7-1500, S7-1500T)](#technology-alarm-308-s7-1500-s7-1500t)
- [Technology alarm 321 (S7-1500, S7-1500T)](#technology-alarm-321-s7-1500-s7-1500t)
- [Technology alarm 322 (S7-1500, S7-1500T)](#technology-alarm-322-s7-1500-s7-1500t)
- [Technology alarm 323 (S7-1500, S7-1500T)](#technology-alarm-323-s7-1500-s7-1500t)
- [Technology alarm 341 (S7-1500, S7-1500T)](#technology-alarm-341-s7-1500-s7-1500t)
- [Technology alarm 342 (S7-1500, S7-1500T)](#technology-alarm-342-s7-1500-s7-1500t)
- [Technology alarm 343 (S7-1500, S7-1500T)](#technology-alarm-343-s7-1500-s7-1500t)

#### Technology alarm 304 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with emergency stop ramp

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Velocity limit is zero.** | ✓ | - | Enter a non-zero value for the maximum velocity (DynamicLimits.MaxVelocity) in the dynamic limits. |
| - | ✓ | Enter a value for the velocity (DynamicLimits.Path.Velocity) that does not equal zero in the dynamic limits. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 305 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with emergency stop ramp

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Acceleration/deceleration limit is zero.** |  | ✓ | ✓ |  |
|  | Acceleration | ✓ | - | Enter a non-zero value for the maximum acceleration (DynamicLimits.MaxAcceleration) in the dynamic limits. |
| - | ✓ | Enter a value for the acceleration (DynamicLimits.Path.Acceleration) that does not equal zero in the dynamic limits. |  |  |
| Deceleration | ✓ | - | Enter a non-zero value for the maximum deceleration (DynamicLimits.MaxDeceleration) in the dynamic limits. |  |
| - | ✓ | Enter a value for the deceleration (DynamicLimits.Path.Deceleration) that does not equal zero in the dynamic limits. |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 306 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with emergency stop ramp

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Jerk limit is zero.** | ✓ | - | Enter a non-zero value for the maximum jerk (DynamicLimits.MaxJerk) in the dynamic limits. |
| - | ✓ | Enter a value for the JERK (DynamicLimits.Path.Jerk) that does not equal zero in the dynamic limits. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 307 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with maximum dynamic values

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Negative/positive numerical value range of the position reached.** |  | ✓ | - |  |
|  | Negative | ✓ | - | Enable the "Modulo" setting for the technology object. |
| Positive | ✓ | - |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 308 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Negative/positive numerical value range of the position exceeded.** |  | ✓ | - |  |
|  | Negative | ✓ | - | Enable the "Modulo" setting for the technology object. |
| Positive | ✓ | - |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 321 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with emergency stop ramp

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Axis is not homed.** | ✓ | - | To perform an absolute positioning motion, you must home the technology object. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 322 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: No reaction

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Restart not executed.** |  | ✓ | - |  |
|  | TO is not ready for restart. | ✓ | - | Download the project again. |
| Condition for TO restart not satisfied. | ✓ | - | Disable the technology object. |  |
| Cam technology object:  Make sure that the cam is not in use. |  |  |  |  |
| Interpreter technology object  Ensure that the Interpreter technology object is not in operation. Stop the execution of the Interpreter program. |  |  |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 323 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Homing could not be performed.** | ✓ | - | - Enable the "Modulo" setting for the technology object. - Adjust the position value for homing. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 341 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with maximum dynamic values

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Homing data faulty.** |  | ✓ | - |  |
|  | Approach velocity is zero. | ✓ | - | Check the configuration for homing (Homing.ApproachVelocity). |
| Homing velocity is zero. | ✓ | - | Check the configuration for homing (Homing.ReferencingVelocity). |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 342 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with emergency stop ramp

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Reference cam/encoder zero mark not found.** | ✓ | - | The reference cam configured for homing was not found in the traversing range of the axis. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 343 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Homing function not supported by device.** | ✓ | - | Configure a reference switch input for the pulse generator output used in the properties of the C-CPU.  ("Pulse generators (PTO/PWM) &gt; PTO[n]/PWN[n] &gt; Hardware inputs/outputs")  When homing across a zero mark, the CPU transfers the reference switch input as zero mark. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

### Technology alarms 401 - 431 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 401 (S7-1500, S7-1500T)](#technology-alarm-401-s7-1500-s7-1500t)
- [Technology alarm 411 (S7-1500, S7-1500T)](#technology-alarm-411-s7-1500-s7-1500t)
- [Technology alarm 412 (S7-1500, S7-1500T)](#technology-alarm-412-s7-1500-s7-1500t)
- [Technology alarm 421 (S7-1500, S7-1500T)](#technology-alarm-421-s7-1500-s7-1500t)
- [Technology alarm 431 (S7-1500, S7-1500T)](#technology-alarm-431-s7-1500-s7-1500t)

#### Technology alarm 401 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Error accessing logical address.** |  | ✓ | - |  |
|  | Address is invalid. | ✓ | - | - Connect a suitable device. - Check the device (I/Os). - Check the topology of the project. - Compare the device configuration and the configuration of the technology object. - Configure the valid hardware limit switch. - Open a Support request.   The following data is required for the error analysis:   - The service data of the CPU directly after the occurrence of the error     (Online &amp; diagnostics &gt; Functions &gt; Save service data)   - The diagnostic buffer of the CPU as text file     (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer)   - The software installed on the PG as an export file     (Help &gt; Service &amp; Support in TIA Portal &gt; Support request)   - The project in the state that led to this alarm   - The password for the project   - Steps for reproduction |
| Input address is invalid. | ✓ | - |  |  |
| Output address is invalid. | ✓ | - |  |  |
| Error during parameter assignment of the address area. | ✓ | - | Make sure that different addresses are assigned for all technology objects in the project. |  |
| Address overlap during drive interconnection. | ✓ | - |  |  |
| Address overlap during encoder interconnection. | ✓ | - |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 411 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Encoder at the logical address disrupted.** |  | ✓ | - |  |
|  | Alarm message from encoder. | ✓ | - | Check the function, connections and I/Os of the encoder. |
| HW error encoder. | ✓ | - |  |  |
| Encoder dirty. | ✓ | - |  |  |
| Read error encoder absolute value. | ✓ | - | Compare the encoder type in the drive or encoder parameter P979 with the configuration data of the technology object. |  |
| Zero mark monitoring encoder. | ✓ | - | Encoder signals error in zero mark monitoring (fault code 0x0002 in Gx_XIST2, see PROFIdrive profile). |  |
| Encoder in Parking state. | ✓ | - | - Search for the cause of the error in the connected drive or encoder. - Check whether the alarm was possibly triggered by a commissioning action involving the drive or encoder. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 412 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Permitted actual value range exceeded.** |  | ✓ | - |  |
|  | Positive. | ✓ | - | - Home the axis/encoder in a valid actual value range. - When using an absolute encoder, check the transfer of the incremental actual value "Gx_XIST1" in PROFIdrive Telegram. If the incremental actual value is transmitted at less than 32 bit, configure the evaluation of "Gx_XIST1" in "&lt;TO&gt;.Sensor[1..4].Parameter.BehaviorGx_XIST1" to the value "0" in the data block of the technology object.   For more detailed information on the evaluation of the incremental actual value "Gx_XIST1", refer to the section "[Drive and encoder connection](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#drive-and-encoder-connection-s7-1500-s7-1500t)" in the "S7-1500/S7-1500T Axis functions" documentation. |
| Negative. | ✓ | - |  |  |
| Modulo length. | ✓ | - | Note the maximum permissible velocity for modulo axes:  - The modulo axis is not configured as a possible leading value for a synchronous axis technology object:   The maximum permissible velocity is limited to the Modulo length/cycle time of MC_Servo. - The modulo axis is configured as a possible leading value for a synchronous axis technology object:   The maximum permissible velocity is limited to half the Modulo length/cycle time of MC_Servo.   Reduce the cycle time of MC_Servo.  Configure the maximum velocity "&lt;TO&gt;.DynamicLimits.MaxVelocity" to the maximum permissible velocity of the modulo axis. This limits the velocity of the axis to the maximum permissible velocity. The axis remains enabled.  Increase the modulo length or disable the "Modulo" setting if that is possible for your application.   **Notice**   You must adapt the user program after changing the modulo configuration.  Modify the following points in the user program:  - Calculation of the target positions and the motion direction for positioning instructions - Parameter assignment of synchronous operation instructions and cams - Display of positions in the HMI and other user interfaces   Additional modifications may be necessary depending on your application. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 421 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Drive disrupted at the logical address.** |  | ✓ | - |  |
|  | Alarm message from drive. | ✓ | - | - Check the function and the connections of the drive. - Enable the safety function in the drive.   You can find more detailed information in the section "[Safety functions in the drive](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#brief-description-of-the-safety-functions-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Axis functions" documentation. - In the case of analog connected axes, check if the "&lt;TO&gt;.StatusDrive.InOperation" tag = TRUE. - Wait to enable the drive until the axis has reached a standstill (&lt;TO&gt;.StatusWord.X7 (Standstill)). You can configure the standstill detection in the configuration of the axis technology object under "Extended parameters &gt; Position monitoring &gt; Standstill signal". |
| No drive control required. | ✓ | - |  |  |
| Drive has shut down. | ✓ | - |  |  |
| Drive enable not possible. | ✓ | - |  |  |
| Error controlling the PROFIdrive State Machine. | ✓ | - | Wait until the axis has reached a standstill (&lt;TO&gt;.StatusWord.X7 (Standstill)). You can configure the standstill detection in the configuration of the axis technology object under "Extended parameters &gt; Position monitoring &gt; Standstill signal".  Disable the technology object. Acknowledge the alarm. Enable the technology object again. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 431 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Communication to the device under logical address is disturbed.** |  | ✓ | - |  |
|  | Drive failed. | ✓ | - | Check the function, connections and I/Os of the drive. |
| Signs of life of drive faulty. | ✓ | - | - Check the function, connections and I/Os of the drive. - Compare the cycle times in the device configuration (PROFINET sync master, PROFINET sync device or PROFIBUS DP master system, PROFIBUS device) and in the MC_Servo. The cycle of the master application and the application cycle of the MC_Servo must be parameterized with the same cycle time.   (An incorrect parameter assignment is indicated with 0x0080.) - If you call the application cycle of the MC_Servo reduced to the send clock of a PROFINET IO system and the technology alarm 431 (Signs of life of drive faulty) is repeatedly shown, increase the update time of the send clock. |  |
| Encoder failed. | ✓ | - | Check the function, connections and I/Os of the encoder. |  |
| Signs of life of encoder faulty. | ✓ | - | - Check the function, connections and I/Os of the encoder. - Compare the cycle times in the device configuration (PROFINET sync master, PROFINET sync device or PROFIBUS DP master system, PROFIBUS device) and in the MC_Servo. The cycle of the master application and the application cycle of the MC_Servo must be parameterized with the same cycle time. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Technology alarms 501 - 563 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 501 (S7-1500, S7-1500T)](#technology-alarm-501-s7-1500-s7-1500t)
- [Technology alarm 502 (S7-1500, S7-1500T)](#technology-alarm-502-s7-1500-s7-1500t)
- [Technology alarm 503 (S7-1500, S7-1500T)](#technology-alarm-503-s7-1500-s7-1500t)
- [Technology alarm 504 (S7-1500, S7-1500T)](#technology-alarm-504-s7-1500-s7-1500t)
- [Technology alarm 511 (S7-1500, S7-1500T)](#technology-alarm-511-s7-1500-s7-1500t)
- [Technology alarm 521 (S7-1500, S7-1500T)](#technology-alarm-521-s7-1500-s7-1500t)
- [Technology alarm 522 (S7-1500, S7-1500T)](#technology-alarm-522-s7-1500-s7-1500t)
- [Technology alarm 531 (S7-1500, S7-1500T)](#technology-alarm-531-s7-1500-s7-1500t)
- [Technology alarm 533 (S7-1500, S7-1500T)](#technology-alarm-533-s7-1500-s7-1500t)
- [Technology alarm 534 (S7-1500, S7-1500T)](#technology-alarm-534-s7-1500-s7-1500t)
- [Technology alarm 541 (S7-1500, S7-1500T)](#technology-alarm-541-s7-1500-s7-1500t)
- [Technology alarm 542 (S7-1500, S7-1500T)](#technology-alarm-542-s7-1500-s7-1500t)
- [Technology alarm 550 (S7-1500, S7-1500T)](#technology-alarm-550-s7-1500-s7-1500t)
- [Technology alarm 551 (S7-1500, S7-1500T)](#technology-alarm-551-s7-1500-s7-1500t)
- [Technology alarm 552 (S7-1500, S7-1500T)](#technology-alarm-552-s7-1500-s7-1500t)
- [Technology alarm 561 (S7-1500T)](#technology-alarm-561-s7-1500t)
- [Technology alarm 562 (S7-1500T)](#technology-alarm-562-s7-1500t)
- [Technology alarm 563 (S7-1500T)](#technology-alarm-563-s7-1500t)

#### Technology alarm 501 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Programmed velocity is limited.** | ✓ | ✓ | - Check the value for the velocity at the instruction. - Check the configuration of the dynamic limits. - Check the value of the "&lt;TO&gt;.Static.DynamicLimits.Velocity" tag. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 502 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Programmed acceleration/deceleration is being limited.** |  | ✓ | ✓ |  |
|  | Acceleration | ✓ | ✓ | - Check the value for the acceleration at the instruction. - Check the configuration of the dynamic limits. |
| Deceleration | ✓ | ✓ | - Check the value for the delay at the instruction. - Check the configuration of the dynamic limits. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 503 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Programmed jerk is limited.** | ✓ | ✓ | - Check the value for the jerk at the instruction. - Check the configuration of the dynamic limits. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 504 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Speed setpoint monitoring active.** | ✓ | - | - Check the mechanical configuration. - Check the encoder connection. - Check the configuration of the speed setpoint interface. - Check the configuration of the control loop. - Check the value for the maximum velocity (&lt;TO&gt;.DynamicLimits.MaxVelocity). - When using an absolute encoder, check the transfer of the incremental actual value "Gx_XIST1" in PROFIdrive Telegram. If the incremental actual value is transmitted at less than 32 bit, configure the evaluation of "Gx_XIST1" in "&lt;TO&gt;.Sensor[1..4].Parameter.BehaviorGx_XIST1" to the value "0" in the data block of the technology object.   For more detailed information on the evaluation of the incremental actual value "Gx_XIST1", refer to the section "[Drive and encoder connection](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#drive-and-encoder-connection-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T" documentation. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 511 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Dynamic limit is violated by kinematics motion.** |  | ✓ | - |  |
|  | Velocity. | ✓ | - | Reduce the velocity of the kinematics motion. |
| Acceleration. | ✓ | - | Reduce the acceleration of the kinematics motion. |  |
| Deceleration. | ✓ | - | Reduce the deceleration of the kinematics motion. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 521 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Following error.** | ✓ | - | - Check the configuration of the control loop. - Check the direction signal of the encoder. - Check the configuration of the following error monitoring. - When using an absolute encoder, check the transfer of the incremental actual value "Gx_XIST1" in PROFIdrive Telegram. If the incremental actual value is transmitted at less than 32 bit, configure the evaluation of "Gx_XIST1" in "&lt;TO&gt;.Sensor[1..4].Parameter.BehaviorGx_XIST1" to the value 0 in the data block of the technology object.   For more detailed information on the evaluation of the incremental actual value "Gx_XIST1", refer to the section "[Drive and encoder connection](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#drive-and-encoder-connection-s7-1500-s7-1500t)" in the "S7-1500/S7-1500T Axis functions" documentation. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 522 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Warning following error tolerance.** | ✓ | - | - Check the configuration of the control loop. - Check the direction signal of the encoder. - Check the configuration of the following error monitoring. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 531 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Positive HW limit switch approached.** | ✓ | - | Acknowledge the alarm.  After the acknowledgment, motions in the negative direction are allowed. |
| **Negative HW limit switch approached.** | ✓ | - | Acknowledge the alarm.  After the acknowledgment, motions in the positive direction are allowed. |
| **Invalid retraction direction, HW limit switch active.** | ✓ | - | The programmed direction of movement is disabled due to the active HW limit switch.  Retract the axis in the opposite direction. |

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Encoder error with triggered HW limit switch, no retraction possible.** | ✓ | - | Correct the fault in the encoder.  Acknowledge the alarm by switching the controller off and on or by restarting the technology object. |

Restart: See Remedy

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **HW limit switch polarity reversed, retraction not possible.** | ✓ | - | - Check the mechanical configuration of the HW limit switch. - Check the limit switches. - Make sure that only one of the two tags is "TRUE":   - &lt;TO&gt;.StatusWord.X17 (HWLimitMinActive)   - &lt;TO&gt;.StatusWord.X18 (HWLimitMaxActive) - To enable retraction, you can temporarily disable the HW limit switches.  Technology version ≥ V7.0:  Only required for traversable HW limit switches: Acknowledge the alarm by switching the controller off and on or by restarting the technology object.  Technology version &lt; V7.0:  Acknowledge the alarm by switching the controller off and on or by restarting the technology object. |
| **Both HW limit switches active, retraction not possible.** | ✓ | - |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 533 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: The alarm response depends on the configured response and the type of axis motion.

- Stop with maximum dynamic values

  When "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 0 and an interconnected axis.

  - Axis motion as following axis in synchronous operation
  - Kinematics axis in kinematics motion
- Stop with current dynamic values

  When "&lt;TO&gt;.PositionLimits_SW.LimitReachedBehavior" = 1 and interconnected axis

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Software limit switch is approached.** |  | ✓ | - |  |
|  | Negative | ✓ | - | With the current dynamic values, the axis will approach the negative software limit switch.  For positioning axes, check the position setpoint.  For following axes, check whether the current dynamics violates the configured dynamic limits.  Move the axis in positive direction away from the negative software limit switch. |
| Positive | ✓ | - | With the current dynamic values, the axis will approach the positive software limit switch.  For positioning axes, check the position setpoint.  For following axes, check whether the current dynamics violates the configured dynamic limits.  Move the axis in negative direction away from the positive software limit switch |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

---

**See also**

[Behavior when reaching the SW limit switch (S7-1500, S7-1500T)](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#behavior-when-reaching-the-sw-limit-switch-s7-1500-s7-1500t)

#### Technology alarm 534 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: You can configure the alarm response.

- Remove enable

  Setting: "&lt;TO&gt;.PositionLimits_SW.LimitExceededBehavior" = 0
- Stop with emergency stop ramp

  Setting: "&lt;TO&gt;.PositionLimits_SW.LimitExceededBehavior" = 1

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **SW limit switch was overtraveled.** |  | ✓ | - |  |
|  | Negative | ✓ | - | The software limit switch was overtraveled.  Acknowledge the alarm.  After the acknowledgment, motions in the positive direction are allowed. |
| Positive | ✓ | - | The software limit switch was overtraveled.  Acknowledge the alarm.  After the acknowledgment, motions in the negative direction are allowed. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 541 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Position monitoring error.** |  | ✓ | - |  |
|  | Target range not reached. | ✓ | - | The target range was not reached within the tolerance time.  - Check the configuration of the position monitoring. - Check the configuration of the control loop. |
| Exit target range again. | ✓ | - | The target range was exited within the minimum dwell time.  - Check the configuration of the position monitoring. - Check the configuration of the control loop. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 542 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Clamping monitoring error: Axis leaving clamping tolerance window.** | ✓ | - | The axis has executed a motion greater than the permissible tolerance at the fixed stop.  Check whether the fixed stop has broken away. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 550 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Track setpoints

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Drive-autonomous motion is being executed.** | ✓ | - | - The drive is performing a motion that was not specified by the technology object. - Check if a safety function is active in the drive.   You can find more detailed information in the section "[Safety functions in the drive](Using%20S7-1500-S7-1500T%20Axis%20functions%20%28S7-1500%2C%20S7-1500T%29.md#brief-description-of-the-safety-functions-s7-1500-s7-1500t)" of the "S7-1500/S7-1500T Axis functions" documentation. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 551 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Maximum velocity cannot be reached with drive/axis parameters.** | ✓ | - | The configured maximum velocity cannot be reached with the configured mechanics of the axis.  Check the configuration of the mechanics and the set reference speed.  Check the adapted reference speed "&lt;TO&gt;.Actor.DriveParameter.ReferenceSpeed" during automatic transfer of the drive parameters during runtime (online). During the automatic transfer of the drive parameters in runtime (online), slight accuracy deviations may occur from the reference speed configured in the drive. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 552 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |  |
| **Encoder adaptation error during ramp-up.** |  |  | ✓ | - |  |
|  | Encoder is not assigned to a SINAMICS device. |  | ✓ | - | - The operationally active encoder could not be adapted. Other encoders that can be used are configured. Use the encoder switch. - The encoder set as the operationally active encoder could not be adapted. - Specify a different sensor for the initialization of the technology object. |
|  | Encoder system. | ✓ | - |  |  |
| Encoder resolution. | ✓ | - |  |  |  |
| Encoder fine resolution. | ✓ | - |  |  |  |
| Encoder revolutions. | ✓ | - |  |  |  |
| Unspecified. | ✓ | - |  |  |  |
| Reference value NACT. | ✓ | - |  |  |  |
| Parameter does not exist, value unreadable or invalid. |  | ✓ | - | Check whether your device supports acyclic data communication according to PROFIdrive. |  |
|  | Encoder system. | ✓ | - |  |  |
| Encoder resolution. | ✓ | - |  |  |  |
| Encoder fine resolution. | ✓ | - |  |  |  |
| Encoder revolutions. | ✓ | - |  |  |  |
| Unspecified. | ✓ | - |  |  |  |
| Reference value NACT. | ✓ | - |  |  |  |
| Adaptation canceled due to insufficient resources. |  | ✓ | - |  |  |
|  | Encoder system. | ✓ | - |  |  |
| Encoder resolution. | ✓ | - |  |  |  |
| Encoder fine resolution. | ✓ | - |  |  |  |
| Encoder revolutions. | ✓ | - |  |  |  |
| Unspecified. | ✓ | - |  |  |  |
| Reference value NACT. | ✓ | - |  |  |  |
| Encoder is not interconnected directly to I/O area. |  | ✓ | - | During the configuration of the axis, the logical addresses were set to a data block or bit memory address area, for example. The adaptation is only possible when the encoder has been directly interconnected to an I/O area. |  |
|  | Encoder system. | ✓ | - |  |  |
| Encoder resolution. | ✓ | - |  |  |  |
| Encoder fine resolution. | ✓ | - |  |  |  |
| Encoder revolutions. | ✓ | - |  |  |  |
| Unspecified. | ✓ | - |  |  |  |
| Reference value NACT. | ✓ | - |  |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |  |

#### Technology alarm 561 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Programmed velocity of the orientation motion is limited.** | - | ✓ | Check the configuration of the velocity of the orientation motion. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 562 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Programmed acceleration/deceleration of the orientation motion is limited.** |  | - | ✓ |  |
|  | Acceleration | - | ✓ | Check the configuration of the acceleration of the orientation motion. |
| Deceleration | - | ✓ | Check the configuration of the deceleration of the orientation motion. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 563 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Programmed jerk of the orientation motion is limited.** | - | ✓ | Check the configuration of the jerk of the orientation motion. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

### Technology alarms 601 - 612 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 601 (S7-1500, S7-1500T)](#technology-alarm-601-s7-1500-s7-1500t)
- [Technology alarm 603 (S7-1500, S7-1500T)](#technology-alarm-603-s7-1500-s7-1500t)
- [Technology alarm 608 (S7-1500, S7-1500T)](#technology-alarm-608-s7-1500-s7-1500t)
- [Technology alarm 612 (S7-1500T)](#technology-alarm-612-s7-1500t)

#### Technology alarm 601 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with maximum dynamic values

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Leading axis is not assigned or defective.** | ✓ | - | Configure the possible leading value axes for the following axis under "Configuration &gt; Leading value interconnections".  For cross-PLC synchronous operation, make sure that the option "Synchronous to the bus" is selected for the MC_Servo OBs of all connected CPUs under "Properties &gt; General &gt; Cycle time". |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 603 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Leading axis is not in position-controlled mode.** | ✓ | - | During synchronization/desynchronization, the leading axis must be operated in position-controlled mode. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 608 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Stop with maximum dynamic values

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Error during synchronization/desynchronization.** | ✓ | - | - Prevent a reverse leading value motion during the synchronization/desynchronization. - If necessary, use a higher [hysteresis value](Using%20S7-1500-S7-1500T%20Synchronous%20operation%20functions%20%28S7-1500%2C%20S7-1500T%29.md#actual-value-coupling-and-actual-value-extrapolation-s7-1500t) (&lt;TO&gt;.Extrapolation.Hysteresis.Value) for actual value coupling.   You can find more information at Siemens Industry Online Support in the FAQ entry [109798578](https://support.industry.siemens.com/cs/ww/en/view/109798578). - Check the direction specification for the synchronization or desynchronization at the instruction. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 612 (S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Specified cam has not been interpolated.** | ✓ | - | Interpolate the cam used for camming. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

### Technology alarms 700 - 758 (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Technology alarm 700 (S7-1500, S7-1500T)](#technology-alarm-700-s7-1500-s7-1500t)
- [Technology alarm 701 (S7-1500, S7-1500T)](#technology-alarm-701-s7-1500-s7-1500t)
- [Technology alarm 702 (S7-1500, S7-1500T)](#technology-alarm-702-s7-1500-s7-1500t)
- [Technology alarm 703 (S7-1500, S7-1500T)](#technology-alarm-703-s7-1500-s7-1500t)
- [Technology alarm 704 (S7-1500, S7-1500T)](#technology-alarm-704-s7-1500-s7-1500t)
- [Technology alarm 750 (S7-1500, S7-1500T)](#technology-alarm-750-s7-1500-s7-1500t)
- [Technology alarm 752 (S7-1500, S7-1500T)](#technology-alarm-752-s7-1500-s7-1500t)
- [Technology alarm 753 (S7-1500, S7-1500T)](#technology-alarm-753-s7-1500-s7-1500t)
- [Technology alarm 754 (S7-1500, S7-1500T)](#technology-alarm-754-s7-1500-s7-1500t)
- [Technology alarm 755 (S7-1500, S7-1500T)](#technology-alarm-755-s7-1500-s7-1500t)
- [Technology alarm 758 (S7-1500, S7-1500T)](#technology-alarm-758-s7-1500-s7-1500t)

#### Technology alarm 700 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Error when calculating the switching position.** |  | ✓ | - |  |
|  | Cam position: OnPosition | ✓ | - | The position for the "OnPosition" parameter could not be calculated.  Invalid positions (e.g. "OnPosition" &gt; "OffPosition") were calculated due to lead times.  The output cam cannot be switched due to the axis dynamics and compensation times. |
| Cam position: OffPosition | ✓ | - | The position for the "OffPosition" parameter could not be calculated.  Invalid positions (e.g. "OffPosition" &gt; "OnPosition") were calculated due to lead times.  The output cam cannot be switched due to the axis dynamics and compensation times. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 701 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **I/O output error.** | ✓ | - | The digital output for the output cam or cam track technology object cannot be addressed.  Download the device configuration again. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 702 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Position value invalid.** | ✓ | - | - A restart of the technology object is performed. Wait until the technology object restart is complete. - The encoder values are invalid due to an encoder error. Check the encoder and adjust the configuration if necessary. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 703 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Output cam data faulty.** |  | ✓ | - |  |
|  | Output cam: Output cam number | ✓ | - | Check the configuration of the relevant output cam in the cam track and adjust the values if necessary.  Examples of a correct configuration:  - "&lt;TO&gt;.Parameter.Cam[1..32].OnPosition" &lt; "&lt;TO&gt;.Parameter.Cam[1..32].OffPosition" - "&lt;TO&gt;.Parameter.Cam[1..32].Duration" &gt; "&lt;TO&gt;.Parameter.OffCompensation" - "&lt;TO&gt;.Parameter.OnCompensation" |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 704 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Output cam data faulty.** | ✓ | - | Check the configuration of the output cam and adjust the values if necessary.  Examples of a correct configuration:  - "MC_OutputCam.OnPosition" &lt; "MC_OutputCam.OffPosition" - "MC_OutputCam.Duration" &gt; "&lt;TO&gt;.Parameter.OffCompensation" - "&lt;TO&gt;.Parameter.OnCompensation" |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 750 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Measuring job not possible during homing of assigned axis.** | ✓ | - | Do not use a measuring job and a homing job simultaneously. Wait until homing of the axis is complete. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 752 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Validity range of measuring job not recognized.** | ✓ | - | The pre-defined measuring range was not recognized. Adjust the measuring range. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 753 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Only one measuring input can access an encoder at a time.** | ✓ | - | Use only one measuring job for an encoder. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 754 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Measuring input configuration in external device is not correct.** | ✓ | - | Check the configuration of the measuring inputs on the external device. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 755 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: Remove enable

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Measuring job not possible.** |  | ✓ | - |  |
|  | Device has reported an error. | ✓ | - | The measurement was aborted with error.  Check the measuring input functionality in the utilized device. |
| Cyclic measuring is not possible with telegram 39x. | ✓ | - | - Use a job to start a one-time measurement. - Cyclic measuring is only possible when measuring using TM Timer DIDQ. Change the configuration of the measuring input type to "TM Timer DIDQ". |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 758 (S7-1500, S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **A measuring edge was not evaluated.** | ✓ | - | An edge was already detected at the input of the measuring input even though the module was not yet ready.  The measured value is provided at the next edge. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

### Technology alarms 801 - 820 (S7-1500T)

This section contains information on the following topics:

- [Technology alarm 801 (S7-1500T)](#technology-alarm-801-s7-1500t)
- [Technology alarm 802 (S7-1500T)](#technology-alarm-802-s7-1500t)
- [Technology alarm 803 (S7-1500T)](#technology-alarm-803-s7-1500t)
- [Technology alarm 804 (S7-1500T)](#technology-alarm-804-s7-1500t)
- [Technology alarm 805 (S7-1500T)](#technology-alarm-805-s7-1500t)
- [Technology alarm 806 (S7-1500T)](#technology-alarm-806-s7-1500t)
- [Technology alarm 807 (S7-1500T)](#technology-alarm-807-s7-1500t)
- [Technology alarm 808 (S7-1500T)](#technology-alarm-808-s7-1500t)
- [Technology alarm 809 (S7-1500T)](#technology-alarm-809-s7-1500t)
- [Technology alarm 810 (S7-1500T)](#technology-alarm-810-s7-1500t)
- [Technology alarm 811 (S7-1500T)](#technology-alarm-811-s7-1500t)
- [Technology alarm 812 (S7-1500T)](#technology-alarm-812-s7-1500t)
- [Technology alarm 820 (S7-1500T)](#technology-alarm-820-s7-1500t)

#### Technology alarm 801 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Kinematics axis &lt;no.&gt; not ready.** |  | - | ✓ |  |
|  | Axis not released. | - | ✓ | Enable the technology object. |
| Axis job programmed. | - | ✓ | To be able to transmit another kinematics job, set the specified axis to a standstill. |  |
| Axis alarm. | - | ✓ | Check and acknowledge the technology alarms of the specified kinematics axis. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 802 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Cannot calculate the geometry element.** |  | - | ✓ |  |
|  | Radius less than half the path distance. | - | ✓ | Adjust the radius. |
| Starting, intermediate, or end point identical | - | ✓ | Specify different values for starting point, intermediate point and end point. |  |
| Intermediate point cannot be accessed. | - | ✓ | Adjust the intermediate point. |  |
| Starting and end points identical. | - | ✓ | Define different start and end points. |  |
| Unable to execute dynamic adaptation. | - | ✓ | Switch off the dynamic adaptation. |  |
| Movement is outside the transformation area. | - | ✓ | Define the motions within the transformation area |  |
| Transformation only works with sPTP motions. | - | ✓ | Use one job for an absolute or relative sPTP motion. |  |
| Not possible to approach tracked OCS. | - | ✓ | - Use an absolute linear or circular motion. - For an absolute circular motion, define the circular path via intermediate point and target position. - Switch off the dynamic adaptation. - Use a route &gt; 0 for the linear or circular motion. An orientation motion without kinematics motion is not possible. |  |
| Kinematics motion in the coupled OCS cannot be terminated by job configuration. | - | ✓ |  |  |
| Change of the coordinate system is not possible with coupled OCS. | - | ✓ | It is not possible to directly change from one coupled OCS into another coupled OCS with a motion command. First transmit an instruction in the WCS or a non-tracked OCS to complete the process of the kinematics with the tracked OCS. |  |
| sPTP motion not possible with coupled OCS. | - | ✓ | An sPTP motion cannot be used in a moved OCS. To move the kinematics in a coupled OCS, use one of the following motions:  - Absolute or relative linear motion - Absolute or relative circular motion |  |
| Active coordinate system cannot be changed with coupled OCS. | - | ✓ | The following instructions can only be performed in the status "TrackingState" = 0 or 1:  - Redefine tool - Change active tool - Start conveyor tracking   The following instruction can only be performed in the status "TrackingState" = 0:  - Redefine object coordinate systems   First transmit an instruction in the WCS or a non-tracked OCS to complete the process of the kinematics with the tracked OCS. |  |
| Dynamic values of the user transformation not correctly specified. | - | ✓ | Check the calculation of the velocities and accelerations in the user transformation in the MC_Transformation. |  |
| The target joint position is outside the valid joint travel range. | - | ✓ | Check the set limits of the joint travel range. Specify a valid target joint position. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 803 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  |  |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |  |  |
| **Error in the calculation of the transformation.** |  |  |  | - | ✓ |  |
|  | Error during transformation of the axis coordinates into Cartesian coordinates. |  |  | - | ✓ | - Correct your specified motion with regard to the joint positioning space and the transformation areas: - Position the kinematics axes with single-axis motions in a permitted transformation area. - For user transformation:   Check the calculation in the MC_Transformation. |
| Error during transformation of the Cartesian coordinates into axis coordinates. |  |  | - | ✓ |  |  |
| Additional info: |  |  | - | ✓ |  |  |
|  | With predefined kinematics systems: |  |  |  |  |  |
| 0 | Cartesian position cannot be reached |  |  |  |  |  |
| 1 | Singularity |  |  |  |  |  |
| With user-defined kinematics systems:  "FunctionResult" of MC_Transformation |  |  |  |  |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |  |  |

#### Technology alarm 804 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Kinematics motion cannot be stopped at end.** | - | ✓ | Ensure that the path is sufficiently long. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 805 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Limitation of path dynamics by axis dynamics incorrect.** |  | - | ✓ |  |
|  | Path velocity is limited to zero. | - | ✓ | Configure a higher "Maximum velocity" on the kinematics axes. |
| Acceleration/deceleration is limited to zero. | - | ✓ | Configure a larger "Maximum acceleration" or "Maximum deceleration" on the kinematics axes. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 806 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop without leaving the path

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Zone violation of work or blocked zones.** | - | ✓ | Move the kinematics into the work zone or out of the blocked zone. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

#### Technology alarm 807 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: No reaction

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Zone violation of signal zones.** | - | ✓ | - |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

#### Technology alarm 808 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Ambiguity due to multiple active work zones.** |  | - | ✓ |  |
|  | &lt;Number of current active work zones&gt; | - | ✓ | Activate only one work zone. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 809 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Path dynamic limit through dynamic of the orientation motion faulty.** |  | - | ✓ |  |
|  | Velocity is limited to zero. | - | ✓ | Configure a higher maximum velocity for the axes involved in the orientation motion. |
| Acceleration/deceleration is limited to zero. | - | ✓ | Configure a higher maximum acceleration or deceleration for the axes involved in the orientation motion. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 810 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Conveyor belt not assigned or faulty (OCS &lt;number&gt;).** | - | ✓ | - Check the parameter inputs for initiating conveyor tracking. - Check the configuration of the leading-value-capable technology object which represents the conveyor belt. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 811 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Error when approaching the TCP to an object coordinate system (OCS &lt;number&gt;).** | - | ✓ | - You have used an impermissible motion job for approaching the TCP on the object coordinate system. Use an absolute linear or circular motion. - The kinematics motion was stopped or interrupted, and the tracking of the OCS in the state "TrackingState" = "2" and "4" was terminated. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 812 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Error in the treatment of singularities.** |  | - | ✓ |  |
|  | The kinematics has reached the singularity. | - | ✓ | Correct the given path motion with respect to the singularities. |
| Too many singularities occur in the path command. | - | ✓ |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

#### Technology alarm 820 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: Stop with maximum dynamic values of the axes

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| Upper limit of joint traversing range joint &lt;No.&gt; overtraveled. | - | ✓ | Move the joint back into the joint traversing range via a single-axis job. |
| Lower limit of joint traversing range joint &lt;No.&gt; overtraveled. | - | ✓ |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

### Technology alarms 900 - 903 (S7-1500T)

This section contains information on the following topics:

- [Technology alarm 900 (S7-1500T)](#technology-alarm-900-s7-1500t)
- [Technology alarm 901 (S7-1500T)](#technology-alarm-901-s7-1500t)
- [Technology alarm 902 (S7-1500T)](#technology-alarm-902-s7-1500t)
- [Technology alarm 903 (S7-1500T)](#technology-alarm-903-s7-1500t)

#### Technology alarm 900 (S7-1500T)

Alarm response TO<sup>1)</sup>: Set leading value invalid

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Leading values invalid.** | ✓ | - | Set a higher tolerance time (&lt;TO&gt;.Parameter.ToleranceTimeExternalLeadingValueInvalid).  Check the connection of the interconnected components. Make sure that there is no communication interference.  Make sure that the CPUs involved are in RUN operating state. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 901 (S7-1500T)

Alarm response TO<sup>1)</sup>: Set leading value invalid

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Data transmission error.** |  | ✓ | - |  |
|  | Reason: Invalid version | ✓ | - | Check the communication. |
| Reason: Invalid modulo start value | ✓ | - |  |  |
| Reason: Invalid modulo length | ✓ | - |  |  |
| Reason: Sign-of-life error | ✓ | - |  |  |
| Reason: Invalid position | ✓ | - | Check the leading value of the leading axis on the other CPU. |  |
| Reason: Invalid velocity | ✓ | - |  |  |
| Reason: Invalid acceleration | ✓ | - |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 902 (S7-1500T)

Alarm response TO<sup>1)</sup>: No reaction

Alarm response Kin<sup>2)</sup>: -

Restart: Not required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Leading value accuracy limited.** | ✓ | - | Decrease the configured delay time. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |

#### Technology alarm 903 (S7-1500T)

Alarm response TO<sup>1)</sup>: Set leading value invalid

Alarm response Kin<sup>2)</sup>: -

Restart: Required

| Alarm text | Validity |  | Remedy |
| --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |
| **Modulo settings of the leading axis changed in cyclic operation.** | ✓ | - | The changed modulo settings of the leading axis are only adopted by the leading axis proxy after a restart and a change in the operating state of the CPU.  Acknowledge the alarm by switching the controller off and on and perform a restart of the technology object. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |

### Technology alarms 1001 - 1012 (S7-1500T)

This section contains information on the following topics:

- [Technology alarm 1001 (S7-1500T)](#technology-alarm-1001-s7-1500t)
- [Technology alarm 1002 (S7-1500T)](#technology-alarm-1002-s7-1500t)
- [Technology alarm 1003 (S7-1500T)](#technology-alarm-1003-s7-1500t)
- [Technology alarm 1004 (S7-1500T)](#technology-alarm-1004-s7-1500t)
- [Technology alarm 1005 (S7-1500T)](#technology-alarm-1005-s7-1500t)
- [Technology alarm 1006 (S7-1500T)](#technology-alarm-1006-s7-1500t)
- [Technology alarm 1007 (S7-1500T)](#technology-alarm-1007-s7-1500t)
- [Technology alarm 1008 (S7-1500T)](#technology-alarm-1008-s7-1500t)
- [Technology alarm 1009 (S7-1500T)](#technology-alarm-1009-s7-1500t)
- [Technology alarm 1010 (S7-1500T)](#technology-alarm-1010-s7-1500t)
- [Technology alarm 1011 (S7-1500T)](#technology-alarm-1011-s7-1500t)
- [Technology alarm 1012 (S7-1500T)](#technology-alarm-1012-s7-1500t)

#### Technology alarm 1001 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Max. Interpreter program configuration limits reached.** |  | ✓ | - |  |
|  | General error | ✓ | - | Check whether the Interpreter program adheres to the configuration limits. |
| Max. number of global Interpreter variables reached | ✓ | - | Reduce the number of global interpreter variables. |  |
| Max. number of local variables and parameters in function reached | ✓ | - | Reduce the number of local tags and parameters in the function. |  |
| Max. number of synchronous actions reached | ✓ | - | Reduce the number of synchronized actions. |  |
| Max. number of symbols reached, e.g. operators, identifiers, literals, data types, etc. | ✓ | - | Reduce the number of symbols, e.g. operators, identifiers, literals, data types etc. |  |
| Max. number of mapped technology objects reached | ✓ | - | Reduce the number of mapped technology objects. |  |
| Max. number of mapped PLC tags reached | ✓ | - | Reduce the number of mapped technology PLC tags. |  |
| Max. character length of identifier reached | ✓ | - | Reduce the character length of the identifier. |  |
| Max. number of functions reached | ✓ | - | Reduce the number of functions. |  |
| Max. calls of the stack depth of functions reached | ✓ | - | Reduce the function calls. |  |
| Max. nesting depth of control instructions reached | ✓ | - | Reduce the nesting depth of control instructions. |  |
| Max. number of user-defined data types reached | ✓ | - | Reduce the number of user-defined data types. |  |
| Max. nesting depth of user-defined data types reached | ✓ | - | Reduce the nesting depth of the user-defined data types. |  |
| Max. number of jump labels reached | ✓ | - | Reduce the number of jump labels. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

##### More information

You can find more information on the configuration limits of the Interpreter program in the [documentation "S7-1500T Interpreter functions"](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#configuration-limits-s7-1500t), section "Configuration limits".

#### Technology alarm 1002 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Max. Interpreter mapping configuration limits reached.** |  | ✓ | - |  |
|  | General error | ✓ | - | Check whether the Interpreter mapping adheres to the configuration limits. |
| Max. number of global Interpreter variables reached | ✓ | - | Reduce the number of global interpreter variables. |  |
| Max. number of local variables and parameters in function reached | ✓ | - | Reduce the number of local tags and parameters in the function. |  |
| Max. number of synchronous actions reached | ✓ | - | Reduce the number of synchronized actions. |  |
| Max. number of symbols reached, e.g. operators, identifiers, literals, data types, etc. | ✓ | - | Reduce the number of symbols, e.g. operators, identifiers, literals, data types etc. |  |
| Max. number of mapped technology objects reached | ✓ | - | Reduce the number of mapped technology objects. |  |
| Max. number of mapped PLC tags reached | ✓ | - | Reduce the number of mapped technology PLC tags. |  |
| Max. character length of identifier reached | ✓ | - | Reduce the character length of the identifier. |  |
| Max. number of functions reached | ✓ | - | Reduce the number of functions. |  |
| Max. calls of the stack depth of functions reached | ✓ | - | Reduce the function calls. |  |
| Max. nesting depth of control instructions reached | ✓ | - | Reduce the nesting depth of control instructions. |  |
| Max. number of user-defined data types reached | ✓ | - | Reduce the number of user-defined data types. |  |
| Max. nesting depth of user-defined data types reached | ✓ | - | Reduce the nesting depth of the user-defined data types. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

##### More information

You can find more information on the configuration limits of the Interpreter mapping in the [documentation "S7-1500T Interpreter functions"](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#configuration-limits-s7-1500t), section "Configuration limits".

#### Technology alarm 1003 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Syntax error Interpreter program.** |  | ✓ | - |  |
|  | General syntax error | ✓ | - | Correct the expression. |
| Invalid expression | ✓ | - | Use a different expression. |  |
| Declaration invalid | ✓ | - | Move the declaration to the declaration area. |  |
| Invalid characters | ✓ | - | Correct the characters. |  |
| Invalid value | ✓ | - | Correct the value. |  |
| Object invalid or typo | ✓ | - | Use a different object or correct the typos. |  |
| Characters in string invalid | ✓ | - | Use only valid characters. |  |
| Keyword or identifier reserved | ✓ | - | Use a different identifier. |  |
| Identifier already declared in the current context | ✓ | - | Use a different identifier. |  |
| Keywords of the control structure incorrect | ✓ | - | Correct the keywords. |  |
| PROGRAM not declared, entry point for Interpreter missing | ✓ | - | Complete the "PROGRAM" structure. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1004 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Syntax error Interpreter mapping.** |  | ✓ | - |  |
|  | General syntax error | ✓ | - | Correct the expression. |
| Invalid expression | ✓ | - | Use a different expression. |  |
| Declaration invalid | ✓ | - | Move the declaration to the declaration area. |  |
| Invalid characters | ✓ | - | Correct the characters. |  |
| Invalid value | ✓ | - | Correct the value. |  |
| Object invalid or typo | ✓ | - | Use a different object or correct the typos. |  |
| Characters in string invalid | ✓ | - | Use only valid characters. |  |
| Keyword or identifier reserved | ✓ | - | Use a different identifier. |  |
| Identifier already declared in the current context | ✓ | - | Use a different identifier. |  |
| PROGRAM not declared, entry point for Interpreter missing | ✓ | - | Complete the "PROGRAM" structure. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1005 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Semantic error Interpreter program.** |  | ✓ | - |  |
|  | Variable access failed | ✓ | - | Check the access rights of the tag. |
| Index limit exceeded | ✓ | - | Check the array size. |  |
| Step size of the FOR loop is zero | ✓ | - | The step size of a FOR loop must be not equal to zero. Correct or supplement the step size of the FOR loop.   `FOR i :=`  `<Start value>`  `TO`  `<Target value>`  `BY`  `<Step size>`  `DO`    `...`    `END_FOR;` |  |
| Return value missing | ✓ | - | Add a return value. |  |
| Data type conflict | ✓ | - | Use a tag with the suitable data type. |  |
| Implicit conversion not possible | ✓ | - | Check the data types used. |  |
| Invalid expression | ✓ | - | Use a valid expression. |  |
| Reference invalid | ✓ | - | Use a valid reference. |  |
| Declaration not found | ✓ | - | Complete the declaration. |  |
| Multiple declaration | ✓ | - | Declare an object only once. Delete all additional declarations of the object. |  |
| Assignment not possible | ✓ | - | - Check the access rights of the tag. Use a writable tag. - Check the data types. |  |
| Invalid result (NaN) | ✓ | - | Correct the calculation or correct the data type of the return value. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1006 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Semantic error Interpreter mapping.** |  | ✓ | - |  |
|  | Variable access failed | ✓ | - | Check the access rights of the tag. |
| Index limit exceeded | ✓ | - | Check the array size. |  |
| Step size of the FOR loop is zero | ✓ | - | The step size of a FOR loop must be not equal to zero. Correct or supplement the step size of the FOR loop.   `FOR i :=`  `<Start value>`  `TO`  `<Target value>`  `BY`  `<Step size>`  `DO`    `...`    `END_FOR;` |  |
| Return value missing | ✓ | - | Add a return value. |  |
| Data type conflict | ✓ | - | Use a tag with the suitable data type. |  |
| Implicit conversion not possible | ✓ | - | Check the data types used. |  |
| Invalid expression | ✓ | - | Use a valid expression. |  |
| Reference invalid | ✓ | - | Use a valid reference. |  |
| Declaration not found | ✓ | - | Complete the declaration. |  |
| Multiple declaration | ✓ | - | Declare an object only once. Delete all additional declarations of the object. |  |
| Assignment not possible | ✓ | - | - Check the access rights of the tag. Use a writable tag. - Check the data types. |  |
| Invalid result (NaN) | ✓ | - | Correct the calculation or correct the data type of the return value. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1007 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Parameter error Interpreter instruction.** |  | ✓ | - |  |
|  | Parameter value invalid | ✓ | - | Correct the parameter value. |
| Parameter unknown | ✓ | - | Correct the parameter specification. |  |
| Parameter missing | ✓ | - | Complete the obligatory parameters. |  |
| Multiple parameter | ✓ | - | Delete redundantly specified parameters. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1008 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Processing error Interpreter instruction.** |  | ✓ | - |  |
|  | Access to connected or mapped object not possible | ✓ | - | Check the links and mappings |
| No kinematics connected | ✓ | - | Connect a kinematics technology object. |  |
| Error reaction of a technology object controlled by the Interpreter | ✓ | - | Check and acknowledge the technology alarms of the technology object controlled by the Interpreter |  |
| Kinematics job cannot be run, job active at least one axis | ✓ | - | Terminate the active jobs of the kinematics axes. |  |
| Job cannot be executed, axis or kinematics control panel active | ✓ | - | Relinquish master control of the active axis or kinematics control panel. |  |
| Other job active at an axis controlled by the Interpreter | ✓ | - | Terminate the active jobs of the axis. |  |
| setControlledByInterpreter() cannot be executed, job is running in the technology object | ✓ | - | Terminate the active job at the technology object. |  |
| Technology error | ✓ | - | Check the error ID named in this alarm. |  |
| Execution not possible, missing enable(s) | ✓ | - | Enable the technology object controlled by the interpreter using the Motion Control instruction "[MC_Power](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_power-enable-disable-technology-object-v8-s7-1500-s7-1500t)" or the MCL instruction "[powerOn()](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#poweron-enable-axis-s7-1500t)". |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1009 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Processing error synchronous action.** |  | ✓ | - |  |
|  | General error | ✓ | - | Open a Support request.  The following data is required for the error analysis:  - The service data of the CPU directly after the occurrence of the error   (Online &amp; diagnostics &gt; Functions &gt; Save service data) - The diagnostic buffer of the CPU as text file   (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer) - The software installed on the PG as an export file   (Help &gt; Service &amp; Support in TIA Portal &gt; Support request) - The project in the state that led to this alarm - The password for the project - Steps for reproduction |
| Invalid expression | ✓ | - | Use only valid expressions. |  |
| Programming cannot be realized | ✓ | - | Correct the programming of the synchronized action. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1010 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop and recompile Interpreter program

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Processing error synchronous start.** |  | ✓ | - |  |
|  | Programming invalid | ✓ | - | Correct the programming of the synchronized action. |
| Invalid expression | ✓ | - | Correct the expression. |  |
| Complete preparation not possible | ✓ | - | All MCL instructions of the synchronous action between SYNC and END_SYNC must be completely prepared.  - Check the MCL instructions of the synchronous action. MCL instructions that interrupt the preparation are not permitted, e.g. "preHalt()". - Check the number of MCL instructions of the synchronous action and reduce this if necessary. - Check the maximum number of jobs to be prepared in the Interpreter job sequence and increase this if necessary (&lt;TO_Interpreter&gt;.Parameter.MaxNumberOfCommands). |  |
| Mutual dependency of instructions/instruction sequence. | ✓ | - | The MCL instructions of the synchronous action are contradictory. Contradictory MCL instructions cannot be applied to the same technology object simultaneously.  Check whether the same technology object is accessed simultaneously with the synchronous action. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1011 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: Stop Interpreter program with diagnostics option

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Error when mapping technology objects.** |  | ✓ | - |  |
|  | General error | ✓ | - | Open a Support request.  The following data is required for the error analysis:  - The service data of the CPU directly after the occurrence of the error   (Online &amp; diagnostics &gt; Functions &gt; Save service data) - The diagnostic buffer of the CPU as text file   (Online &amp; diagnostics &gt; Diagnostics &gt; Diagnostics buffer) - The software installed on the PG as an export file   (Help &gt; Service &amp; Support in TIA Portal &gt; Support request) - The project in the state that led to this alarm - The password for the project - Steps for reproduction |
| Type of the mapped technology object is not supported | ✓ | - | Correct the mapping. |  |
| Mapped technology object cannot be found | ✓ | - | Check the mapped technology object |  |
| Technology object to be mapped already connected | ✓ | - | Check the mapping. |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

#### Technology alarm 1012 (S7-1500T)

Alarm response TO<sup>1)</sup>: -

Alarm response Kin<sup>2)</sup>: -

Alarm response interpreter: No reaction

Restart: Not required

| Alarm text |  | Validity |  | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| **Critical programming** |  | ✓ | - |  |
|  | System function overridden by a function with the same identifier. | ✓ | - | Correct the programming of the function |
| Job is ignored due to a "MC_Power" job in the user program | ✓ | - | To enable or disable a technology object to be controlled by the Interpreter, use the MCL instructions "powerOn()" and "powerOff()" or the Motion Control instruction "MC_Power". |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

## Error IDs in Motion Control instructions (S7-1500, S7-1500T)

This section contains information on the following topics:

- [Short description of error IDs in Motion Control instructions (S7-1500, S7-1500T)](#short-description-of-error-ids-in-motion-control-instructions-s7-1500-s7-1500t)
- [Error IDs 16#0000 - 16#800F (S7-1500, S7-1500T)](#error-ids-160000---16800f-s7-1500-s7-1500t)
- [Error IDs 16#8010 - 16#801F (S7-1500, S7-1500T)](#error-ids-168010---16801f-s7-1500-s7-1500t)
- [Error IDs 16#8020 - 16#802F (S7-1500, S7-1500T)](#error-ids-168020---16802f-s7-1500-s7-1500t)
- [Error IDs 16#8030 - 16#803F (S7-1500, S7-1500T)](#error-ids-168030---16803f-s7-1500-s7-1500t)
- [Error IDs 16#8040 - 16#804F (S7-1500, S7-1500T)](#error-ids-168040---16804f-s7-1500-s7-1500t)
- [Error IDs 16#8050 - 16#805F (S7-1500, S7-1500T)](#error-ids-168050---16805f-s7-1500-s7-1500t)
- [Error IDs 16#8060 - 16#806F (S7-1500, S7-1500T)](#error-ids-168060---16806f-s7-1500-s7-1500t)
- [Error IDs 16#8070 - 16#807F (S7-1500, S7-1500T)](#error-ids-168070---16807f-s7-1500-s7-1500t)
- [Error IDs 16#8080 - 16#808F (S7-1500, S7-1500T)](#error-ids-168080---16808f-s7-1500-s7-1500t)
- [Error IDs 16#80A0 - 16#80AF (S7-1500, S7-1500T)](#error-ids-1680a0---1680af-s7-1500-s7-1500t)
- [Error IDs 16#80B0 - 16#80BF (S7-1500T)](#error-ids-1680b0---1680bf-s7-1500t)
- [Error IDs 16#80C0 - 16#80CF (S7-1500T)](#error-ids-1680c0---1680cf-s7-1500t)
- [Error IDs 16#80D0 - 16#80DF (S7-1500T)](#error-ids-1680d0---1680df-s7-1500t)
- [Error IDs 16#80E0 - 16#80EF (S7-1500T)](#error-ids-1680e0---1680ef-s7-1500t)
- [Error IDs 16#80F0 - 16#80FE (S7-1500T)](#error-ids-1680f0---1680fe-s7-1500t)
- [Error IDs 16#8110 - 16#8111 (S7-1500, S7-1500T)](#error-ids-168110---168111-s7-1500-s7-1500t)
- [Error IDs 16#8FF0 - 16#8FFF (S7-1500, S7-1500T)](#error-ids-168ff0---168fff-s7-1500-s7-1500t)

### Short description of error IDs in Motion Control instructions (S7-1500, S7-1500T)

Errors in Motion Control instructions are indicated by the "Error" and "ErrorID" output parameters.

Under the following conditions, "Error" = TRUE and "ErrorID" = 16#8xxx are indicated for the Motion Control instruction:

- Illegal status of the technology object, which prevents the execution of the job.
- Invalid parameter assignment of the Motion Control instruction, which prevents the execution of the job.
- As a result of the alarm response for a technology object error.

#### Error display

If there is a Motion Control instruction error, the "Error" parameter shows the value "TRUE". The cause of the error is given in the "ErrorID" parameter.

Jobs to the technology object are rejected when "Error" = TRUE. Running jobs are not influenced by rejected jobs.

If "Error" = TRUE and "ErrorID" = 16#8001 is indicated during job execution, a technology alarm has occurred. In this case, evaluate the indication of the technology alarm.

If "Error" = TRUE is displayed during execution of a "MC_MoveJog" job, the axis is braked and brought to a standstill. In this case, the deceleration configured for the "MC_MoveJog" instruction takes effect.

#### Acknowledge error

Acknowledging errors in Motion Control instructions is not required.

Restart a job after resolving the error.

### Error IDs 16#0000 - 16#800F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#0000 | ✓ | ✓ | No error | - |
| 16#8001 | ✓ | ✓ | A technology alarm (technology object error) occurred while processing the Motion Control instruction. | In the technology data block, an error message is output at the "ErrorDetail.Number" tag.  You can find a list of the technology alarms and alarm responses in the section "[Overview of the technology alarms](#overview-of-the-technology-alarms-s7-1500-s7-1500t)". |
| 16#8002 | ✓ | - | Invalid specification of the technology object | - Check the specification of the technology object for the "Axis", "Master", "Slave", "OutputCam", "CamTrack", "MeasuringInput" or "Cam"or "Interpreter" parameter. - With "MC_MeasuringInputCyclic": Specify a valid measuring input type for parameter "MeasuringInputType". |
| - | ✓ | Check the specification of the technology object for the "Axis" or "AxesGroup" parameter.  You can use a kinematics technology object only for the "AxesGroup" parameter. |  |  |
| 16#8003 | ✓ | ✓ | Invalid velocity specification | Specify a permissible value for the velocity for parameter "Velocity". |
| - | ✓ | Invalid velocity factor | Specify a permissible value for the velocity factor for the "VelocityFactor" parameter. |  |
| 16#8004 | ✓ | ✓ | Invalid acceleration specification | Specify a permissible value for the acceleration for the "Acceleration" parameter. |
| - | ✓ | Invalid acceleration factor | Specify a permissible value for the acceleration factor for the "AccelerationFactor" parameter. |  |
| 16#8005 | ✓ | ✓ | Invalid deceleration specification | Specify a permissible value for the deceleration for the "Deceleration" parameter. |
| - | ✓ | Invalid deceleration factor | Specify a permissible value for the deceleration factor for the "DecelerationFactor" parameter. |  |
| 16#8006 | ✓ | ✓ | Invalid jerk specification | Specify a permissible value for the jerk for parameter "Jerk". |
| - | ✓ | Invalid jerk factor | Specify a permissible value for the jerk factor for the "JerkFactor" parameter. |  |
| 16#8007 | ✓ | - | Invalid entry  Both the "JogForward" and "JogBackward" parameters are set to TRUE at the same time. The axis is braked at the last valid deceleration. | Reset both the "JogForward" parameter and the "JogBackward" parameter. |
| ✓ | - | Invalid direction specification | Specify a permissible value for the direction at the parameter "Direction" or "SyncDirection". |  |
| - | ✓ | Specify a permissible value for the motion direction for the "DirectionA" parameter. |  |  |
| 16#8008 | ✓ | - | Invalid distance specification | Set a permissible distance value for the "Distance" parameter. |
| - | ✓ | Invalid specification of the relative target coordinate | Specify permissible values for the relative target coordinate for the "Distance" parameter. |  |
| 16#8009 | ✓ | - | Invalid position specification | Set a permissible position value for the "Position" parameter. |
| - | ✓ | Invalid specification of the absolute target coordinate | Specify a permissible value for the absolute target coordinate in the "Position" parameter. |  |
| 16#800A | ✓ | - | Invalid operating mode | Specify a permissible operating mode for parameter "Mode". |
| ✓ | ✓ | Invalid mode specification | Specify a permissible value for the mode for the "Mode" parameter. |  |
| 16#800B | ✓ | - | Invalid stop mode specifications | Specify a permissible value for the stop mode at the "StopMode" parameter. |
| 16#800C | ✓ | - | Only one instance of the instruction per technology object is allowed. | - The instruction is called at multiple points in the user program with identical value for parameter "Axis", "Master", "Slave" or "Cam".   Ensure that only one instruction with the value for parameter "Axis", "Master", "Slave" or "Cam" is called. - The error message can occur through the DB editor functions "Load snapshot as actual values" or "Load start values as actual values".   Correct the error of the affected data block technology object by switching the CPU to STOP, re-compiling the affected data block, and loading it into the device. |
| 16#800D | ✓ | ✓ | The job is not permitted in the current state. Technology objects are initialized. | When the operating state changes from STOP to RUN, the technology objects are initialized one after the other (STARTUP operating state). Depending on the number of technology objects used, this may take several application cycles.  Wait until the initialization of the technology objects is complete. Alternatively, extend the application cycle. |
| ✓ | - | The job is not permitted in the current state. "Restart" is executed. | While a "Restart" is being performed, the technology object cannot perform any jobs. Active jobs on the cam, output cam, cam track or measuring input technology objects were canceled.  Wait until the "Restart" of the technology object is complete. |  |
| - | ✓ | While a restart is being performed, the technology object cannot perform any jobs. Active jobs were canceled.  Restarting the kinematics technology object can take up to one second.  Wait until the technology object restart is complete. |  |  |
| 16#800E | ✓ | - | If the technology object is enabled, a "Restart" is not possible. | Before a "Restart", deactivate the technology object with "MC_Power.Enable" = FALSE. |
| 16#800F | ✓ | ✓ | The job cannot be executed because the technology object is locked. | - Enable the technology object with "MC_Power.Enable" = TRUE. Restart the job. - A "MC_Stop" job is active with "Execute" = TRUE. Reset the job with the parameter "Execute" = FALSE. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8010 - 16#801F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8010 | ✓ | - | Invalid homing mode for incremental encoder | Absolute encoder adjustment is not possible with an incremental encoder ("Mode" = 6, 7).  Technology version ≥ V7.0:  Start a homing process for an incremental encoder using parameter "Mode" = 0, 1, 2, 3, 5, 8, 10, 11, 12, 13.  Technology version &lt; V7.0:  Start a homing process for an incremental encoder using parameter "Mode" = 0, 1, 2, 3, 5, 8, 10, 11, 12. |
| 16#8011 | ✓ | - | Invalid homing mode for absolute encoder | Technology version ≥ V7.0:  Start a homing process for an absolute encoder using parameter "Mode" = 0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12.  Technology version &lt; V7.0:  Start a homing process for an absolute encoder using parameter "Mode" = 0, 1, 6, 7, 11, 12. |
| 16#8012 | ✓ | - | The job cannot be executed because the axis control panel is active. | Return master control to your user program. Restart the job. |
| Interpreter technology object  The job cannot be executed because the commissioning or test interface is active. |  |  |  |  |
| - | ✓ | The job cannot be executed because the kinematics control panel is active. |  |  |
| 16#8013 | ✓ | - | The online connection between the CPU and the TIA Portal is down. | Check the online connection to the CPU. |
| 16#8014 | ✓ | ✓ | No internal job memory available. | The maximum possible number of motion control job has been reached.   Reduce the number of jobs to be executed (parameter "Execute" = FALSE). |
| 16#8015 | ✓ | ✓ | Error acknowledgment with "MC_Reset" is not possible. Error in the configuration of the technology object. | Check the configuration of the technology object. |
| 16#8016 | ✓ | - | The actual values are not valid. | To execute a "MC_Home" or positioning job, the actual values must be valid.  Check the status of the actual values. The "&lt;TO&gt;.StatusSensor[1..4].State" tag of the technology object must show the value 2 (valid). |
| 16#8017 | ✓ | - | Illegal value for gear ratio numerator | Specify a permissible value for the gear ratio numerator for parameter "RatioNumerator".  Permitted integer values:  -2147483648 to 2147483647  (value 0 not permitted) |
| 16#8018 | ✓ | - | Illegal value for gear ratio denominator | Specify a permissible value for the gear ratio denominator for parameter "RatioDenominator".  Permitted integer values:   1 to 2147483647 |
| 16#8019 | ✓ | - | Job cannot be executed. The specified following axis is the original leading value for the synchronous operation chain. | Recursive interconnections are not possible. A leading axis cannot be interconnected as a following axis to its own leading value. Specify a permissible following axis for parameter "Slave". |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8020 - 16#802F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8021 | ✓ | - | Illegal value for shift of the leading value range | Specify a permissible value for the shift of the leading value range for parameter "MasterOffset". |
| 16#8022 | ✓ | - | Illegal value for shift of the following value range | Specify a permissible value for the shift of the leading value range for parameter "SlaveOffset". |
| 16#8023 | ✓ | - | Illegal value for scaling of the leading value range | Specify a permissible value for the scaling of the leading value range for parameter "MasterScaling". |
| 16#8024 | ✓ | - | Illegal value for scaling of the following value range | Specify a permissible value for the scaling of the following value range for parameter "SlaveScaling". |
| 16#8026 | ✓ | - | Illegal value for leading value distance | Specify a permissible value for the leading value distance at parameter "MasterStartDistance" or "MasterStopDistance". |
| 16#8027 | ✓ | - | Illegal value for use of cam | Specify a permissible value for cyclic/acyclic use of the cam for parameter "ApplicationMode". |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8030 - 16#803F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8034 | ✓ | - | Illegal value for synchronous position of the leading axis | Specify a permissible value for the synchronous position of the leading axis for parameter "MasterSyncPosition". |
| 16#8035 | ✓ | - | Illegal value for synchronous position of the following axis | Specify a permissible value for the synchronous position of the following axis for parameter "SlaveSyncPosition". |
| 16#8036 | ✓ | - | Invalid value for type of synchronization/desynchronization | Specify a permissible value for the type of synchronization/desynchronization for the "SyncProfileReference" parameter. |
| 16#8037 | ✓ | - | Invalid value for stop position of the following axis | Specify a permissible value for the stop position of the following axis for the "SlavePosition" parameter. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8040 - 16#804F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8040 | ✓ | - | Illegal value for start position of output cam | Specify a permissible value for the start position of the output cam for parameter "OnPosition". |
| 16#8041 | ✓ | - | Illegal value for end position of distance output cam | Specify a permissible value for the end position of the distance output cam for parameter "OffPosition". |
| 16#8042 | ✓ | - | Illegal value for switch-on duration of time-based output cam | Specify a permissible value for the switch-on duration of the time-based output cam for parameter "Duration". |
| 16#8043 | ✓ | - | Illegal value for force/torque limiting | Specify a value within the permissible range at the "Limit" parameter.  Permitted integer values:   -2147483648 to 2147483648 |
| 16#8044 | ✓ | - | The axis is not configured for torque reduction. | Select drive telegram 102, 103, 105 or 106 |
| 16#8045 | ✓ | - | The job cannot be executed because a job for traveling to fixed stop is active. | Switchover to non-position-controlled mode is not possible during active travel to fixed stop. |
| 16#8046 | ✓ | - | The "MC_TorqueLimiting" job cannot be deactivated in the "InClamping" state. | Retract the axis and deactivate "MC_TorqueLimiting". |
| 16#8047 | ✓ | - | The motion results in a fixed stop. | Only motions away from the fixed stop are permitted. |
| 16#804A | ✓ | - | Illegal value for additive torque setpoint | Specify a permissible value for the additive torque setpoint at the "Value" parameter. |
| 16#804B | ✓ | - | Illegal value for torque high limit | Specify a permissible value for the high limit of the torque at the "UpperLimit" parameter. |
| 16#804C | ✓ | - | Illegal value for torque low limit | Specify a permissible value for the low limit of the torque at the "LowerLimit" parameter. |
| 16#804D | ✓ | - | The value of the high limit of the torque is less than or equal to the value of the low limit of the torque. | Adapt the values of the "UpperLimit" and "LowerLimit" parameters so that the high limit of the torque is greater than the value of the low limit of the torque. |
| 16#804E | ✓ | - | The job cannot be executed because a "MC_TorqueLimiting" job is active. | Exit the setting of the high and low torque limits. Restart the "MC_TorqueLimiting" job. |
| The job cannot be executed because a "MC_TorqueRange" job is active. | Stop the force/torque limit or fixed stop detection. Restart the "MC_TorqueRange" job. |  |  |  |
| 16#804F | ✓ | - | The axis is not configured for additional torque values. | Use supplemental telegram 750. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8050 - 16#805F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8050 | ✓ | - | Illegal encoder number | Technology version &lt; V7.0:  MC_SetSensor: At the "Sensor" parameter, enter a permissible number for the encoder.  Technology version ≥ V7.0:  MC_SetSensor: At the "Sensor" parameter, enter a permissible number (1, 2, 3, 4) for the encoder.  MC_Home: At the "Sensor" parameter, enter a permissible number (0, 1, 2, 3, 4) used for an encoder. |
| 16#8051 | ✓ | - | Illegal number of the reference encoder | Specify a permissible number of the reference encoder for parameter "MC_SetSensor.ReferenceSensor".  If you call the instruction "MC_SetSensor" with parameter "Mode" = 0, enter a different number for the parameter "ReferenceSensor" than for the parameter "Sensor". |
| 16#8055 | ✓ | - | Bit masking not permitted at "MC_SetAxisSTW" | Non-controllable bits are selected in the "STW1 BitMask" and "STW2 BitMask" bit masks.  Only control [permissible bits](S7-1500%20Motion%20Control%20%28S7-1500%2C%20S7-1500T%29.md#mc_setaxisstw-control-bits-of-control-word-1-and-2-v8-s7-1500-s7-1500t). |
| 16#805A | ✓ | - | Illegal value of the parameter to be changed | At parameter "ParameterNumber", enter a permissible value for the index of the parameter to be changed. |
| 16#805B | ✓ | - | Error in the configuration of the hardware limit switch. | Specify a valid tag at the input of the positive/negative HW limit switch. |
| 16#805C | ✓ | - | Illegal data type of the value to be written. | Specify a valid data type at the parameter "Value". |
| 16#805D | ✓ | - | - Direct PROFIdrive data connection from axis or external encoder. - Axis is in simulation. - Axis is configured as virtual axis. | Configure the T<sub>i</sub>, T<sub>o</sub>, T<sub>DC</sub> communication times only if the PROFIdrive data connection via data block is configured. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8060 - 16#806F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8062 | ✓ | - | Invalid approach value | Specify a permissible approach value for the searched for leading value for parameter "ApproachLeadingValue". |
| 16#8063 | ✓ | - | A valid mapping to the definition range (leading values) does not exist for the specified following value. | - Specify a permissible following value for parameter "FollowingValue". - Ensure that the cam is interpolated ("MC_InterpolateCam.Done" = TRUE, "&lt;TO&gt;.StatusWord.X5 (Interpolated)" = TRUE). |
| 16#8064 | ✓ | - | A valid mapping to the range of the function (following values) does not exist for the specified leading value. | - Specify a permissible leading value for parameter "LeadingValue". - Ensure that the cam is interpolated ("MC_InterpolateCam.Done" = TRUE, "&lt;TO&gt;.StatusWord.X5 (Interpolated)" = TRUE). |
| 16#8065 | ✓ | - | Invalid approach direction | Specify a permissible value for the approach direction for the searched for leading value for the "ApproachDirection" parameter. |
| 16#8066 | ✓ | - | The end of the cam has been reached in the specified approach direction. No suitable leading value could be found. | - Specify the opposite approach direction at the "ApproachDirection" parameter. - Specify a different approach value for the searched for leading value for parameter "ApproachLeadingValue". - Specify a permissible following value for parameter "FollowingValue". |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8070 - 16#807F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8070 | ✓ | - | Illegal value for leading value shift | Specify a permissible value for the leading value shift for parameter "PhaseShift". |
| 16#8071 | ✓ | - | The job cannot be executed because the axis is not in position-controlled mode. | Activate position-controlled mode. |
| 16#8074 | ✓ | - | The job cannot be executed because a "MC_Home" job is active. | During active or passive homing, an encoder switchover is rejected.  Wait until the "MC_Home" job is complete. Restart the job. |
| 16#8075 | ✓ | - | The job cannot be executed because no synchronization operation is active on the axis. | Switch on the synchronous operation function. Restart the job. |
| 16#8076 | ✓ | - | The job cannot be executed because synchronization is being simulated at the specified axis. | End the simulation of the synchronous operation. Restart the job. |
| 16#8077 | ✓ | - | The job cannot be executed because no "MC_GearInPos" or "MC_GearIn" job is waiting or active. | Switch on the synchronous operation function. Restart the job.  To desynchronize a camming, use the Motion Control instruction "MC_CamOut". |
| 16#8078 | ✓ | - | The job cannot be executed because no "MC_CamIn" job is waiting or active. | Switch on the camming function. Restart the job.  To desynchronize gearing, use the Motion Control instruction "MC_GearOut". |
| 16#8079 | ✓ | - | The job cannot be executed because a velocity gearing with "MC_GearInVelocity" is active. | A job to offset the leading or following value is only applicable during an active gearing or camming. |
| Following axis is in non-position-controlled operation.  Stop velocity gearing and restart "MC_GearInPos" job or "MC_CamIn" job. |  |  |  |  |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#8080 - 16#808F (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8080 | ✓ | - | Invalid value for the following value offset | Specify a permissible value for the following value offset for the "Offset" parameter. |
| 16#8081 | ✓ | - | Invalid value for leading value distance | Specify a permissible value for the following value offset for the "OffsetDistance" parameter. |
| 16#8082 | ✓ | - | Invalid value for leading value distance | Specify a permissible value for the leading value offfset for parameter "PhasingDistance". |
| 16#8083 | ✓ | - | Invalid value for the type of traversing of the leading/following value offset | Specify a permissible value for the leading value/following value offset shift for parameter "ProfileReference". |
| 16#8084 | ✓ | - | Invalid value for start position | Specify a permissible value for the leading value/following value offset shift for parameter "StartPosition". |
| 16#808A | ✓ | - | The job for the leading value offset cannot be executed because a following value offset is active on the axis. | Exit the active following value offset via "MC_OffsetAbsolute" or "MC_OffsetRelative". Restart the job. |
| The job for the following value offset cannot be executed because a leading value offset is active on the axis. | Exit the active leading value offset via "MC_PhasingAbsolute" or "MC_PhasingRelative". Restart the job. |  |  |  |
| 16#808B | ✓ | - | The job cannot be executed because no camming is active on the axis. | A "MC_CamIn" job with "SyncProfileReference" = 5 can only be used if the camming is already active. |
| 16#808C | ✓ | - | Reversing the leading value is not permitted during an active leading value offset or following value offset. | Start the job again after reversing the leading value. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#80A0 - 16#80AF (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80A1 | ✓ | - | The order cannot be executed because a synchronous operation job is active. | A "MC_Home" job on a following axis is not executed when a "MC_CamIn" or "MC_GearInPos" job is active.  Exit the synchronous operation job. Restart the job. |
| 16#80A2 | ✓ | - | - For one-time measuring with measuring range, the measuring range was run without a measuring edge being detected. - The measuring range is invalid with the configured modulo axis settings. | Check and adjust the measuring input and adjust the measuring range positions, if necessary. |
| 16#80A3 | ✓ | - | The measuring input job via PROFIdrive telegram could not be started because a homing job is active. | Simultaneous execution of a homing job and a measuring input job via PROFIdrive telegram is not possible.  Wait until the homing job has ended. Restart the measuring job via PROFIdrive telegram. |
| 16#80A5 | ✓ | - | Illegal value for start position of measuring range | Specify a permissible value for the start position of the measuring range for parameter "MC_MeasuringInput.StartPosition" or "MC_MeasuringInputCyclic.StartPosition". |
| 16#80A6 | ✓ | - | Illegal value for end position of measuring range | Specify a permissible value for the end position of the measuring range for parameter "MC_MeasuringInput.EndPosition" or "MC_MeasuringInputCyclic.EndPosition". |
| 16#80A7 | ✓ | - | A measurement is performed when measuring with the measuring range, but the calculated position is outside the specified measuring range. The measured value is discarded. | Check and adjust the measuring input and adjust the measuring range positions, if necessary. |
| 16#80A8 | ✓ | - | The job cannot be executed because camming is active on the axis. | An "MC_PhasingRelative" or "MC_PhasingAbsolute" job with "ProfileReference" = 0 can only be used on an active gearing with "MC_GearIn" or "MC_GearInPos" in the "synchronous" status ("MC_GearIn.InGear" = TRUE or "MC_GearInPos.InSync" = TRUE). |
| 16#80A9 | ✓ | - | The job cannot be executed because no synchronous gearing or camming is active on the axis. | A job for leading/following value offset is only applicable to up an active gearing or camming in "synchronous" status ("MC_GearIn.InGear" = TRUE, "MC_GearInPos.InSync" = TRUE or  "MC_CamIn.InSync" = TRUE). |
| 16#80AA | ✓ | - | The cam contains no points or segments and cannot be interpolated. | Fill the cam with points/segments. Restart the job. |
| 16#80AB | ✓ | - | The cam is currently being used and cannot be interpolated. | End the current use of the cam. Restart the job. |
| 16#80AC | ✓ | - | The cam contains incorrect points or segments and cannot be interpolated.   (for example, the cam contains only one point.) | Fill the cam with permissible points/segments. Restart the job. |
| 16#80AD | ✓ | - | The specified synchronous position is outside the definition range of the cam. | When "SyncProfileReference" = 0, 1, 2, 3, 5, 6:  Specify a permissible synchronous position for parameter "MasterSyncPosition". Restart the job.  When "SyncProfileReference" = 4:  With the "MasterOffset" parameter, you offset the leading values of the cam or move the leading axis into the definition range of the cam. Restart the job. |
| 16#80AE | ✓ | - | The job cannot be executed because a kinematic motion is active. | End the current kinematic motion. Restart the job. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#80B0 - 16#80BF (S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80B1 | - | ✓ | Illegal specification of the coordinate system | Specify a permissible value for the coordinate system for the "CoordSystem" parameter. |
| 16#80B2 | - | ✓ | Illegal specification of the motion transition | Specify a permissible value for the motion transition for the "BufferMode" parameter. |
| 16#80B3 | - | ✓ | Illegal specification of the rounding clearance | Specify a permissible value for the rounding clearance for the "TransitionParameter" parameter. |
| 16#80B4 | - | ✓ | Illegal specification for the joint position range | Specify a permissible value for the joint target position range at the "TurnJoint" parameter. |
| 16#80B5 | - | ✓ | Illegal specification of the dynamic adaptation | Specify a permissible value for the dynamic adaptation for the "DynamicAdaption" parameter. |
| 16#80B6 | - | ✓ | Illegal specification for the definition of the circular path | Specify a permissible value for the definition of the circular path for the "CircMode" parameter. |
| 16#80B7 | - | ✓ | Illegal specification for the circular path auxiliary point | Specify a permissible value for the circular path auxiliary point for the "AuxPoint" parameter. |
| 16#80B8 | - | ✓ | Illegal specification of the target position | Specify a permissible value for the target position for the "EndPoint" parameter. |
| 16#80B9 | - | ✓ | Illegal specification of the orientation of the circular path | Specify a permissible value for the orientation of the circular path for the "PathChoice" parameter. |
| 16#80BA | - | ✓ | Illegal specification for the main plane of the circular path | Specify a permissible value for the main plane of the circular path for the "CirclePlane" parameter. |
| 16#80BB | - | ✓ | Illegal radius specification | Specify a permissible value for the radius of the circular path for the "Radius" parameter. |
| 16#80BC | - | ✓ | Illegal angle specification | Specify a permissible value for the angle of the circular path for the "Arc" parameter. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#80C0 - 16#80CF (S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80C1 | - | ✓ | Illegal specification of the zone type | Specify a permissible value for the zone type for the "ZoneType" parameter. |
| 16#80C2 | - | ✓ | Illegal specification of the zone position | Specify a permissible value for the zone number for the "ZoneNumber" parameter. |
| 16#80C3 | - | ✓ | Illegal specification of the reference system | Specify a permissible value for the reference system for the "ReferenceSystem" parameter. |
| 16#80C4 | - | ✓ | Illegal coordinate specification | Specify permissible values for the coordinates for the "Frame" parameter. |
| 16#80C5 | - | ✓ | Illegal specification of the zone geometry | Specify a permissible value for the zone geometry for the "GeometryType" parameter. |
| 16#80C6 | - | ✓ | Illegal specification of the geometric parameters | Specify permissible values for the geometric parameters for the "GeometryParameter" parameter. |
| 16#80C7 | - | ✓ | The zone is not defined. | Define a workspace zone using the "MC_DefineWorkspaceZone" job or a kinematics zone using the "MC_DefineKinematicsZone" job. |
| 16#80C8 | - | ✓ | A tool cannot be redefined during a motion. | Exit the active motion. Restart the "MC_DefineTool" job. |
| - | ✓ | An active tool cannot be changed during a motion. | Exit the active motion. Restart the "MC_SetTool" job. |  |
| 16#80CA | - | ✓ | Illegal specification of the tool number | Specify a permissible value for the tool number for the "ToolNumber" parameter. |
| 16#80CB | - | ✓ | Illegal specification of the object coordinate system | Specify a permissible value for the object coordinate system for the "OcsNumber" parameter. |
| 16#80CC | - | ✓ | The job cannot be executed because a single-axis motion is active at a kinematics axis or a kinematics axis is controlled by an Interpreter. | Exit the current single-axis motion or the running Interpreter program. Restart the job. |
| 16#80CD | - | ✓ | The job cannot be executed because a "MC_GroupStop" job is active. | Set the "MC_GroupStop.Execute" parameter to "FALSE". Restart the job. |
| 16#80CE | - | ✓ | The job sequence is used to capacity. | The maximum possible Motion Control jobs have been transmitted. |
| ✓ | - | Interpreter technology object:  The job sequence contains the maximum number of possible MLC jobs. |  |  |
| 16#80CF | - | ✓ | The kinematics motion cannot be executed. | Configure the kinematics motion within the working range of the kinematics axes. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

### Error IDs 16#80D0 - 16#80DF (S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80D1 | - | ✓ | Invalid value for the use of the parameter "Position" | At the "PositionMode"parameter, specify a valid value for the use of the "Position" parameter. |
| 16#80D2 | - | ✓ | Illegal value for the target arm positioning space | Enter a permissible value for the target arm positioning space in the "LinkConstellation" parameter. |
| 16#80D3 | - | ✓ | Illegal value for the positions of the kinematics axes | Enter a permissible value for the positions of the kinematics axes at the parameter "AxesPosition". |
| 16#80D4 | - | ✓ | Illegal value for the velocity of the kinematics axes | Specify a permissible value for the velocity of the kinematics axes for the "AxesVelocity" parameter. |
| 16#80D5 | - | ✓ | Illegal value for the acceleration of the kinematics axes | Specify a permissible value for the acceleration of the kinematics axes for the "AxesAcceleration" parameter. |
| 16#80D6 | - | ✓ | An error occurred during the transformation. | Specify permissible values for the transformation. |
| 16#80D7 | - | ✓ | The job on the kinematics transformation cannot be executed. | A "MC_KinematicsTransformation" or "MC_InverseKinematicsTransformation" instruction cannot perform a calculation, when the kinematics moves a tracked OCS or the moving of a tracked OCS is completed. Wait until the current job for the conveyor tracking has been completed and restart the job for the kinematics transformation. |
| 16#80D8 | - | ✓ | Invalid value for the reference coordinate system | Specify a permissible value for the reference coordinate system for the "AxesCoordSystem" parameter. |
| 16#80DA | - | ✓ | Invalid value parameter "InitialObjectPosition" | Enter permissible values for the frame at the parameter "InitialObjectPosition". |
| 16#80DB | - | ✓ | Simulation mode of kinematics cannot be ended | Ensure that when you end the simulation, the setpoints of the axis positions on the kinematics technology object match the setpoints of the axis positions on the assigned axes.  If you use a modulo axis, make sure that the axis is in the same modulo cycle as at the start time of the simulation. |
| 16#80DC | - | ✓ | The job cannot be executed, because only one job of this type can be active at the technology object. | Wait until the active job is finished or finish the active job. Restart the job. |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

### Error IDs 16#80E0 - 16#80EF (S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80E0 | - | ✓ | The kinematics motion cannot be executed. | Configure the kinematics motion within the workspace zone of the kinematics. |
| 16#80E1 | ✓ | - | Invalid value for the index of the starting point in the cam | At the "StartPointCam" parameter, specify a valid value for the index of the starting point in the cam. |
| 16#80E2 | ✓ | - | Invalid value for the index of the starting segment in the cam | At the "StartSegmentCam" parameter, specify a valid value for the index of the starting segment in the cam. |
| 16#80E3 | ✓ | - | Invalid value for the index of the starting point in the "ArrayOfPoints". | At the "StartPointArray" parameter, specify a valid value for the index of the starting point in the "ArrayOfPoints". |
| 16#80E4 | ✓ | - | Invalid value for the index of the starting segment in the "ArrayOfSegments". | At the "StartSegmentArray" parameter, specify a valid value for the index of the starting segment in the "ArrayOfSegments". |
| 16#80E5 | ✓ | - | Invalid value for the number of points to be copied | At the "NumberOfPoints" parameter, specify a valid value for the number of points to be copied. |
| 16#80E6 | ✓ | - | Invalid value for the number of segments to be copied | At the "NumberOfSegments"parameter, specify a valid value for the number of segments to be copied. |
| 16#80E7 | ✓ | - | The job cannot be executed because a copy operation is active. | Wait until the active copy operation is completed via "MC_CopyCamData". Restart the job. |
| 16#80E8 | ✓ | - | The job cannot be executed because the cam is being interpolated. | Wait until the interpolation of the cam is completed via "MC_InterpolateCam". Restart the job. |
| 16#80E9 | ✓ | - | Invalid array of points to be copied | At the "ArrayOfPoints" parameter, specify an array of the data type "ARRAY[*] OF TO_Cam­_Struct­_Point­Data". Do not use a variable declared as temporary.  Ensure that the "Optimized block access" option is selected under "General &gt; Attributes" in the properties of the data block that contains the array. |
| 16#80EA | ✓ | - | Invalid array of segments to be copied | At the "ArrayOfSegments" parameter, specify an array of the data type "ARRAY[*] OF TO_Cam­_Struct­_Segment­Data". Do not use a variable declared as temporary.  Ensure that the "Optimized block access" option is selected under "General &gt; Attributes" in the properties of the data block that contains the array. |
| 16#80EB | ✓ | - | SIMATIC Memory Card has insufficient storage space for the backup file. | Ensure there is sufficient storage space available on the SIMATIC Memory Card used. |
| 16#80EC | ✓ | - | An error occurred when writing the backup file. | - |
| 16#80ED | ✓ | - | More than two instances of the "MC_SaveAbsoluteEncoderData" instruction are used in the user program. | Use a maximum of two instances of the "MC_SaveAbsoluteEncoderData" instruction in your user program. |
| 16#80EE | ✓ | - | Job cannot be executed. | Wait until the current "MC_SaveAbsoluteEncoderData" job has finished with "Done" = TRUE and restart the job. |
| 16#80EF | ✓ | - | The SIMATIC Memory Card is write-protected. | Deactivate the write protection on your SIMATIC Memory Card. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

### Error IDs 16#80F0 - 16#80FE (S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#80F0 | ✓ | - | The name of the Interpreter program technology object has been incorrectly defined or contains invalid characters | Specify a valid name for the Interpreter program technology object at the "Program" parameter. |
| 16#80F1 | ✓ | - | Source of the Interpreter program contains Illegal characters or does not exist | At the "ProgramSource" parameter, specify a valid source for the Interpreter program. |
| 16#80F2 | ✓ | - | The name of the Interpreter mapping technology object has been incorrectly defined or contains invalid characters | Specify a valid name for the Interpreter Mapping technology object at the parameter "Mapping". |
| 16#80F3 | ✓ | - | Source of the Interpreter mapping contains Illegal characters or does not exist | At the "MappingSource" parameter, specify a valid source for the Interpreter Mapping technology object defined at the "Mapping" parameter. |
| 16#80F4 | ✓ | - | User program cannot be opened / does not exist | Check whether the specified Interpreter program exists. |
| 16#80F5 | ✓ | - | Mapping cannot be opened / does not exist | Check whether the specified Interpreter mapping exists. |
| 16#80F6 | ✓ | - | User programs cannot be read during loading | Check whether the specified Interpreter program exists. |
| 16#80F7 | ✓ | - | Mapping cannot be read during loading | Check whether the specified Interpreter mapping exists. |
| 16#80F8 | ✓ | - | Maximum program memory reached. | Check whether the Interpreter program adheres to the configuration limits.  You can find more information on the configuration limits of the Interpreter program in the [documentation "S7-1500T Interpreter functions"](Using%20S7-1500T%20Interpreter%20functions%20%28S7-1500T%29.md#configuration-limits-s7-1500t), section "Configuration limits". |
| 16#80F9 | ✓ | - | Error during discharge of the Interpreter program. | Check whether the Interpreter program is still active. Stop the Interpreter program or wait until the Interpreter program has finished. Restart the job. |
| 16#80FA | ✓ | - | The job cannot be executed because a "MC_StopProgram" job is active. | Reset the "Execute" parameter of the "MC_StopProgram" job to "FALSE". Restart the job. |
| 16#80FB | ✓ | - | The job cannot be executed because a Motion Control job is active on the Interpreter technology object. | - An "MC_LoadProgram" job is not executed while a Motion Control job is active at the Interpreter technology object. - An "MC_RunProgram" job is not executed as long as another "MC_RunProgram" job is active at the Interpreter technology object.  End the active Motion Control jobs on the Interpreter technology object. Restart the job. |
| 16#80FC | ✓ | - | The job cannot be executed because the Interpreter program is not loaded in the Interpreter technology object or is being loaded. | An "MC_RunProgram" job is not executed as long as an Interpreter program has not been loaded into the Interpreter technology object or is in the process of being loaded.  Load the Interpreter program to the Interpreter technology object or wait until the loading is completed. Restart the job. |
| 16#80FD | ✓ | - | The job cannot be executed because the loaded Interpreter program was stopped. | Correct the error that is preventing preparation of the Interpreter program. Restart the job. |
| 16#80FE | ✓ | - | The job is not executed as a further job with the same or higher-priority dynamic mode is active at the Interpreter technology object. | An "MC_StopProgram" job is not executed while a further "MC_StopProgram" job with the same or higher-priority dynamic mode is active at the Interpreter technology object.  Wait until the current "MC_StopProgram" job has ended. Restart the job. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

### Error IDs 16#8110 - 16#8111 (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8110 | ✓ | ✓ | Value for override is impermissible | Specify a permissible value for the override in the axis or kinematics control panel. |
| 16#8111 | ✓ | ✓ | Commissioning mode is impermissible | Correct the settings in the axis or kinematics control panel. |
| <sup>1)</sup> Applies to all technology objects with the exception of the kinematics technology object.   <sup>2)</sup> Applies to the kinematics technology object only. |  |  |  |  |

### Error IDs 16#8FF0 - 16#8FFF (S7-1500, S7-1500T)

| ErrorID | Validity |  | Description | Remedy |
| --- | --- | --- | --- | --- |
| TO<sup>1)</sup> | Kin<sup>2)</sup> |  |  |  |
| 16#8FFF | ✓ | ✓ | Unspecified error | Contact your local Siemens representative or support center.  You will find your contact information for digital industries at:   [https://www.siemens.com/automation/partner](https://www.siemens.com/automation/partner) |
| <sup>1)</sup> Applies to all technology objects with the exception of the Kinematics technology object.   <sup>2)</sup> Applies to the Kinematics technology object only. |  |  |  |  |

---
title: "Using ET 200S 1PosU (S7-300, S7-400)"
package: TFHWC1PosUenUS
topics: 106
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using ET 200S 1PosU (S7-300, S7-400)

This section contains information on the following topics:

- [Terminal Assignment of the 1PosU (S7-300, S7-400)](#terminal-assignment-of-the-1posu-s7-300-s7-400)
- [Basics of controlled positioning by means of rapid/creep feed (S7-300, S7-400)](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400)
- [Functions of 1PosU (S7-300, S7-400)](#functions-of-1posu-s7-300-s7-400)
- [Configuring and assigning parameters to 1PosU (S7-300, S7-400)](#configuring-and-assigning-parameters-to-1posu-s7-300-s7-400)
- [Diagnostics of 1PosU (S7-300, S7-400)](#diagnostics-of-1posu-s7-300-s7-400)

## Terminal Assignment of the 1PosU (S7-300, S7-400)

### Wiring rules

If a position encoder with 5 V differential signals is used, the wires to the terminals 9 and 13, the terminals 12 and 16, as well as at incremental encoders the wires to the terminals 11 and 15 have to be in twisted pairs and shielded.

If an incremental encoder with 24 V signals is used, the wires to the terminals 9, 11 and 12 have to be shielded.

The shield must be supported at both ends. To do this, use the shield contact (see the appendix of the [ET 200S Distributed I/O System](http://support.automation.siemens.com/WW/view/en/1144348) operating instructions).

### Terminal assignment

The following table shows the terminal assignment of 1PosU.

| View | Terminal assignment | Remarks |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ![Terminal assignment](images/23268859659_DV_resource.Stream@PNG-de-DE.png) |  | **Connection of the Switches and the Drive: Terminals 1 to 8** |  | **Connection of the position encoder with 5 V differential signals or 24 V signals: Terminals 9 to 16** |  |
| 1: IN0 | Limit switch minus | 9: A / D | Track A / Data from the SSI encoder |  |  |
| 5: IN1 | Limit switch plus | 13: /A / /D |  |  |  |
| 2: IN2 | Reducing cam; latch signal | 10: 24 V DC | Power supply for the position encoder |  |  |
| 6: 24 V DC | Supply for the switches | 14: M |  |  |  |
| 3: OUT0 | Travel minus or rapid feed | 11: B | Track B |  |  |
| 7: 2L+ | Load voltage infeed for OUT0, OUT1 and OUT2 | 15: /B |  |  |  |
| 4: OUT1 | Travel plus or creep feed | 12: N / C | Track N / SSI clock (clock line) |  |  |
| 8: OUT2 | Rapid/creep feed and travel plus/minus | 16: /N / /C |  |  |  |

### Connection of Relays and Contactors to the Digital Outputs

> **Note**
>
> Direct connection of inductivities (such as relays and contactors) is possible without external circuiting. If SIMATIC output circuits can be deactivated by additionally installed contacts (for example relay contacts), you have to provide additional overvoltage protection devices at inductivities (see the following example for overvoltage protection).

### Overvoltage Protection Example

The following figure shows an output circuit that requires additional overvoltage protection devices. Direct-current coils are wired with diodes or Zener diodes.

![Overvoltage Protection Example](images/23268647307_DV_resource.Stream@PNG-en-US.png)

## Basics of controlled positioning by means of rapid/creep feed (S7-300, S7-400)

### Positioning process

From the start position, the target is approached at high velocity (rapid traverse). At a preset distance from the target (changeover point), there is a change to a lower velocity (creep speed). Shortly before the axis reaches the target, again at a preset distance from the target, the drive is switched off (switch-off point).

The drive is controlled via digital outputs for rapid traverse or creep speed and the appropriate direction.

The following figure shows the switch points and switch differences. To facilitate understanding, the change in velocity is illustrated over the path traversed.

![Positioning process](images/22265431563_DV_resource.Stream@PNG-en-US.png)

### Definitions

The following tables contains the basic terms for controlled positioning using rapid traverse / creep speed.

| Term | Description |
| --- | --- |
| Working range | defines the range which you set for a particular job by means of the hardware limit switches.  At an SSI encoder, the operating range is also limited by the range covered by the SSI encoder.  You enter the encoder range in the parameters for:  - Pulses per encoder revolution and - revolutions.   Encoder range = pulses per encoder revolution × revolutions   Maximum operating range:  - Linear axis max. 0 to (encoder range – 1) - Rotary axis from 0 to (encoder range - 1)     At an incremental encoder the operating range is limited to:  - Max. 0 to 16,777,215 increments at a linear axis - 0 to the programmed end of the rotary axis |
| Changeover difference | defines the distance from the destination at which the drive is switched over from rapid traverse to creep speed. |
| Changeover point | defines the position at which the drive is switched over from rapid traverse to creep speed. |
| Switch-off difference | defines the distance from the destination at which the drive is switched off.  If the switch-off difference ≥ the changeover difference, there is no changeover point. There is no change from rapid traverse to creep speed. |
| Switch-off point | defines the position at which the drive is switched off.   The 1PosU reports the end of the traverse at this point. |
| Start position | defines the position of the drive within the operating range from which the run is started.  If the start position is within the switch-off difference, the drive is not triggered. The 1PosU reports the end of the traverse at this point.  If the start position is within the changeover difference, the traverse is only executed at creep speed. |
| Target | defines the absolute or relative position of the axis approached during positioning.  The target is the position to be reached on an axis during a traverse.  In the case of an absolute traverse, you specify the target directly by means of your control program.  In the case of a relative traverse, the destination is calculated from the start position and the distance specified in the control program.  If you want to find out how accurately you have reached the destination, you have to compare the actual value with the position specified. |
| Linear axis | defines the axis type with a limited operating range.  It is limited by the following:  - the encoder range - the displayable numeric range (0 to 16 777 215 increments) - hardware limit switches |
| Rotary axis | defines the axis type with an infinite operating range.  This includes resetting the axis position to 0 after one rotation (assigned parameter end of a rotary axis at an incremental encoder or parameterized encoder range at an SSI encoder). |
| Minus direction | If the drive moves in the minus direction, the actual value displayed is decreased. |
| Plus direction | If the drive moves in the plus direction, the actual value displayed is increased. |

## Functions of 1PosU (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of the Functions (S7-300, S7-400)](#overview-of-the-functions-s7-300-s7-400)
- [Starting motion types (MODEs) (S7-300, S7-400)](#starting-motion-types-modes-s7-300-s7-400)
- [Activating further functions JOBs) (S7-300, S7-400)](#activating-further-functions-jobs-s7-300-s7-400)
- [Axis, Drive and Encoder (S7-300, S7-400)](#axis-drive-and-encoder-s7-300-s7-400)
- [Effect of the Directional Enables (S7-300, S7-400)](#effect-of-the-directional-enables-s7-300-s7-400)
- [Stop (MODE 0) (S7-300, S7-400)](#stop-mode-0-s7-300-s7-400)
- [Inching (MODE 1) (S7-300, S7-400)](#inching-mode-1-s7-300-s7-400)
- [Reference point approach (MODE 3) (S7-300, S7-400)](#reference-point-approach-mode-3-s7-300-s7-400)
- [Relative positioning (MODE 4) (S7-300, S7-400)](#relative-positioning-mode-4-s7-300-s7-400)
- [Absolute positioning (MODE 5) (S7-300, S7-400)](#absolute-positioning-mode-5-s7-300-s7-400)
- [Canceling JOB Processing (JOB 0) (S7-300, S7-400)](#canceling-job-processing-job-0-s7-300-s7-400)
- [Setting the Actual Value (JOB 1) (S7-300, S7-400)](#setting-the-actual-value-job-1-s7-300-s7-400)
- [Shifting the encoder range (JOB 2) (S7-300, S7-400)](#shifting-the-encoder-range-job-2-s7-300-s7-400)
- [Changing the switch-off difference (JOB 3) (S7-300, S7-400)](#changing-the-switch-off-difference-job-3-s7-300-s7-400)
- [Changing the changeover difference (JOB 4) (S7-300, S7-400)](#changing-the-changeover-difference-job-4-s7-300-s7-400)
- [Evaluating the reference signal (JOB 9) (S7-300, S7-400)](#evaluating-the-reference-signal-job-9-s7-300-s7-400)
- [Latch Function (JOB 10) (S7-300, S7-400)](#latch-function-job-10-s7-300-s7-400)
- [Defining the settings for monitoring the direction of rotation (JOB 11) (S7-300, S7-400)](#defining-the-settings-for-monitoring-the-direction-of-rotation-job-11-s7-300-s7-400)
- [Displaying current values (JOB 15) (S7-300, S7-400)](#displaying-current-values-job-15-s7-300-s7-400)
- [Error detection / diagnostics (S7-300, S7-400)](#error-detection-diagnostics-s7-300-s7-400)
- [CPU/Master STOP and RESET state (S7-300, S7-400)](#cpumaster-stop-and-reset-state-s7-300-s7-400)

### Overview of the Functions (S7-300, S7-400)

#### Overview

The 1PosU offers you the following functions for moving your axis:

- [Stop](#stop-mode-0-s7-300-s7-400)
- [Inching](#inching-mode-1-s7-300-s7-400)
- [Referance point approach](#reference-point-approach-mode-3-s7-300-s7-400)
- [Relative Positioning](#relative-positioning-mode-4-s7-300-s7-400)
- [Absolute Positioning](#absolute-positioning-mode-5-s7-300-s7-400)

In addition to the different types of motion, the 1PosU also offers functions for:

- [Cancelling JOB processing](#canceling-job-processing-job-0-s7-300-s7-400)
- [Setting of Actual Value](#setting-the-actual-value-job-1-s7-300-s7-400)
- [Move Encoder Range](#shifting-the-encoder-range-job-2-s7-300-s7-400)
- [Change Switch-Off Difference](#changing-the-switch-off-difference-job-3-s7-300-s7-400)
- [Change Changeover Difference](#changing-the-changeover-difference-job-4-s7-300-s7-400)
- [Reference Signal Evaluation](#evaluating-the-reference-signal-job-9-s7-300-s7-400)
- [Latch Function](#latch-function-job-10-s7-300-s7-400)
- [Setting the Monitoring of the Direction of Rotation](#defining-the-settings-for-monitoring-the-direction-of-rotation-job-11-s7-300-s7-400)
- [Display Current Values](#displaying-current-values-job-15-s7-300-s7-400)
- [Error detection / diagnostics](#error-detection-diagnostics-s7-300-s7-400)
- [Behavior in CPU/Master-STOP](#cpumaster-stop-and-reset-state-s7-300-s7-400)

#### Parameters

Define the variables that depend on the drive, axis, and encoder uniquely in the parameters.

#### Dosing mode

With incremental encoders, you can use the 1PosU for dosing. You set the dosing mode in the parameters. In dosing mode the 1PosU only evaluates the encoder signal A (/A). The actual value is incremented at each positive edge.

In dosing mode, only the "Inching" and "Relative positioning" functions are available for controlling the digital outputs.

The dosing function itself is triggered using the "Relative positioning" function. The dosing quantity is specified during starting by means of the control interface (distance).

At every start the actual value is set to 0 and the digital outputs are controlled as a function of the changeover and switch-off difference.

#### How the 1PosU works

The following figure shows how the 1PosU works.

![How the 1PosU works](images/22209478795_DV_resource.Stream@PNG-en-US.png)

#### Interfaces to the Control Program and the Axis

To execute the function, the 1PosU has digital inputs as an interface to the axis, encoder signals for the connection to an encoder and digital outputs to control the drive.

### Starting motion types (MODEs) (S7-300, S7-400)

You can control and monitor the types of motion (MODEs) with your control program using control signals and checkback signals.

#### Starting MODEs

The following table shows how you start MODEs and how the 1PosU reacts to them.

| What You Do | 1PosU reactions |
| --- | --- |
| Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the data required depending on the MODE.  Check whether the [feedback bit](#1posu-feedback-interface-s7-300-s7-400) is POS_ACK = 0. |  |
| Switch the START control bit from 0 to 1. | The 1PosU sets the POS_ACK = 1 and POS_DONE = 0 feedback bit.  You can tell by this that the start has been detected by 1PosU and when POS_ERR = 0, the MODE is executed.  When POS_ERR = 1, the MODE is not executed. |
| Switch the START control bit from 1 to 0. | The 1PosU sets the POS_ACK = 0 feedback bit. |
|  | In the case of stopping, the reference point traverse and absolute and relative positioning, the 1PosU sets the POS_DONE = 1 feedback bit when the MODE is terminated without errors.  When POS_ERR = 1, the MODE is terminated with errors. |
| You can start a new MODE only if POS_ACK = 0.  If you start when a MODE is running, the 1PosU takes on the new motion and executes a change of direction, if necessary. |  |

The following figure shows the interaction of the control signals and checkback signals when starting the MODEs.

![Starting MODEs](images/22218514443_DV_resource.Stream@PNG-de-DE.png)

### Activating further functions JOBs) (S7-300, S7-400)

You can control and monitor further functions (JOBs) with your control program using control signals and checkback signals.

#### Activating JOBs

The following table shows how you start JOBs and how the 1PosU reacts to them.

| What You Do | 1PosU reactions |
| --- | --- |
| Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the data required depending on the JOB.  Check whether the [feedback bit](#1posu-feedback-interface-s7-300-s7-400) is JOB_ACK = 0. |  |
| Switch the JOB_REQ control bit from 0 to 1. | The 1PosU sets the JOB_ACK = 1 feedback bit.  You can tell by this that the start has been detected by 1PosU and when JOB_ERR = 0, the JOB is executed.  - With "Evaluate reference signal", the 1PosU sets the SYNC = 0 feedback bit simultaneously. - In the case of the latch function, the 1PosU sets the LATCH_DONE = 0 feedback bit simultaneously. - All the other JOBs are then executed.   When JOB_ERR = 1, the JOB is not executed. |
| Switch the JOB_REQ control bit from 1 to 0. | The 1PosU sets the JOB_ACK = 0 feedback bit. |
|  | When a reference signal is evaluated, the 1PosU sets the SYNC = 1 feedback bit when the function has been executed.  With "Latch", the 1PosU sets the LATCH_DONE = 1 feedback bit when the function has been executed. |
| You can only activate a new JOB if JOB_ACK = 0. |  |

The following figure shows the interaction of the control signals and checkback signals when starting the JOBs.

![Activating JOBs](images/28155072907_DV_resource.Stream@PNG-en-US.png)

### Axis, Drive and Encoder (S7-300, S7-400)

#### Evaluation of the Encoder Signals

The 1PosU evaluates the signals supplied by the encoder differently depending on the encoder type:

- SSI encoder:

  The 1PosU evaluates the encoder value supplied by the SSI encoder directly in increments and forms the actual value in increments (actual value = encoder value).

  The actual value lies in the encoder range from 0 ... (number of rotations * number of increments) – 1. The 1PosU generates an high limit violated / low limit violated of the actual value at the limits of the encoder operating range.
- Incremental encoder:

  The 1PosU evaluates the pulses supplied by the position encoder four times and adds them up direction-specifically to form the actual value. You must take the quadruple evaluation into account when you make settings for paths in the parameters and in the control and feedback interfaces:

  1 pulse of the incremental encoder corresponds to 4 increments of the 1PosU.

  The actual value lies in the operating range of 0 - 16 777 215 increments. The 1PosU generates an high limit violated or low limit violated of the actual value at the limits of the operating range.
- Incremental encoder in dosing mode:

  The 1PosU only evaluates the positive edges of the encoder A signal and adds them up to form the actual value.

  The actual value lies in the operating range of 0 - 16 777 215 increments. The 1PosU creates an high limit violated of the actual value at the high limit of the operating range.

#### Controlling the Drive

The drive is controlled using the 3 digital outputs of the 1PosU.

You can select the velocity with the SPEED control bit (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse). You can also change the speed during the run.

You can bring about a [change in direction](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400) with the "T<sub>min</sub> direction change" parameter.

You can read the status of the respective output from the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) (DO 0, DO 1 and DO 2).

The function of the digital outputs depends on the control mode:

The following figure shows the states of the digital outputs with **control mode 0**.

![Controlling the Drive](images/22219212683_DV_resource.Stream@PNG-en-US.png)

The following figure shows the states of the digital outputs with **control mode 1**.

![Controlling the Drive](images/22219589131_DV_resource.Stream@PNG-en-US.png)

### Effect of the Directional Enables (S7-300, S7-400)

#### Description

You enable the digital outputs directionally using the DIR_M and DIR_P control bits.

- With DIR_M = 1, you can traverse in a minus direction.
- With DIR_P = 1, you can traverse in a plus direction.

#### Interrupting and Continuing the Run

If you reset the relevant directional enable during a run, the motion of the axis is halted, all 3 digital outputs are set to 0, and the run is interrupted.

If you set the relevant directional enable again, the run is continued.

### Stop (MODE 0) (S7-300, S7-400)

#### Stop

If you start MODE 0, then the 1PosU stops the current traverse, all 3 digital outputs are set to "0" and the traverse is terminated (POS_ERR = 0, POS_DONE = 1).

A traverse terminated with MODE 0 cannot be continued. To put the axis into motion again, you start a new MODE.

#### Control signals

The following table shows the data in the control interface which is relevant for "Stop".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bit 0.7 … 0.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | MODE 0 = Stop |  |
| 0 | 0 | 0 | 0 |  |  |  |
| Bit 0: START |  |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [control interface](#1posu-feedback-interface-s7-300-s7-400) relevant for "Stop".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |

---

**See also**

[1PosU control interface (S7-300, S7-400)](#1posu-control-interface-s7-300-s7-400)

### Inching (MODE 1) (S7-300, S7-400)

#### Inching

You use "Inching" to control the drive directly in a particular direction using the DIR_M or DIR_P[control bits](#effect-of-the-directional-enables-s7-300-s7-400).

If you start MODE 1 then the 1PosU moves the drive with the specified velocity (SPEED[control bit](#1posu-control-interface-s7-300-s7-400)) in the specified direction (DIR_M or DIR_P[control bits](#1posu-control-interface-s7-300-s7-400)).

You stop the drive by setting the DIR_M = 0 and DIR_P = 0 control bits.

A [change of direction](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400) is executed after the time T<sub>min</sub> elapses.

You can also activate jogging on an unsynchronized axis (feedback bit SYNC = 0) or when there is a pending encoder error (feedback bit ERR_ENCODER = 1) or without an encoder connected.

The figure below shows the sequence of the "Inching" motion type.

![Inching](images/22219858699_DV_resource.Stream@PNG-en-US.png)

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Inching".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bit 0.7 … 0.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | MODE 1 = Inching |  |
| 0 | 0 | 0 | 1 |  |  |  |
| Bit 3: SPEED (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse)  Bit 2: DIR_M  Bit 1: DIR_P  Bit 0: START |  |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [control interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Inching".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |
| Bytes 1 to 3 | Actual value:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |

#### Causes of the POS_ERR error

You must find out the causes of errors with JOB 15 ([Display current values](#displaying-current-values-job-15-s7-300-s7-400)).

The following table shows the error numbers relevant for "Inching" with the causes of the errors and possible remedies.

| Error Number | Cause | Remedy |
| --- | --- | --- |
| 2 | ERR_2L+ is displayed | Check the load voltage (2L+) at terminal 7. |
| 5 | The limit switch that lies in the direction in which the drive is moved is active | Check your switches and the wiring as well as the "[DI0 limit switch minus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" and "[DI1 limit switch plus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" parameters. |
| 7 | Inching: DIR_P = 1 and DIR_M = 1 |  |
| 13 | Direction of rotation of the drive and the encoder varies | Check the wiring of the drive and the encoder as well as the "[Reversal of the direction of rotation](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)" parameter. |
| 15 | In dosing mode: DIR_M = 1 |  |

### Reference point approach (MODE 3) (S7-300, S7-400)

This section contains information on the following topics:

- [Reference point approach (MODE 3) (S7-300, S7-400)](#reference-point-approach-mode-3-s7-300-s7-400-1)
- [Profile of a reference point approach (S7-300, S7-400)](#profile-of-a-reference-point-approach-s7-300-s7-400)

#### Reference point approach (MODE 3) (S7-300, S7-400)

##### Reference point approach

A reference point run can only be started at incremental encoders and non-activated dosing mode.

With reference point approach, you synchronies the axis by using external referencing signals. You can use either the [3 digital inputs or the zero mark](#profile-of-a-reference-point-approach-s7-300-s7-400) as a reference signal.

You can assign parameters to the digital inputs DI0 (minus limit switch), DI1 (plus limit switch) and DI2 (reducing cam) as NC or NO contacts.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the reference point coordinates and start MODE 3. The 1PosU sets the SYNC = 0 checkback signal, moves the drive at the set velocity (SPEED control bit) in the programmed start direction and searches for the reference signal. The 1PosU automatically executes the required change of direction at the limit switches or the reducing cam.

Set the necessary [directional enables](#effect-of-the-directional-enables-s7-300-s7-400) (DIR_M, DIR_P) to ensure that the drive is controlled.

When the 1PosU detects the assigned parameter reference signal, it then controls the drive at creep speed in the referencing direction. This is controlled by the "Reference signal" and "Reference switch" parameters.

|  | Reference switch: Reduction cam towards minus | Reference switch: Reduction cam towards plus | Reference switch: Limit switch minus | Reference switch: Limit switch plus |
| --- | --- | --- | --- | --- |
| **Reference signal: Reference switch and zero mark** | Minus referencing direction | Plus referencing direction | Plus referencing direction | Minus referencing direction |
| **Reference signal: Reference switch** |  |  |  |  |
| **Reference signal: Zero mark** | The referencing direction is not defined. The axis is synchronized at the next zero mark. |  |  |  |

After the reference signal has been traversed, the axis is synchronized. The 1PosU sets the checkback signal SYNC = 1 and assigns the reference point coordinates to the actual value.

The following figure shows the sequence of the "Inching" motion type.

![Reference point approach](images/28155200651_DV_resource.Stream@PNG-en-US.png)

##### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Reference point approach".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bit 0.7 … 0.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | MODE 3 = Reference point approach |  |
| 0 | 0 | 1 | 1 |  |  |  |
| Bit 3: SPEED (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse)  Bit 2: DIR_M  Bit 1: DIR_P  Bit 0: START |  |  |  |  |  |  |
| Bytes 1 to 3 | Reference point coordinates:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … end of the rotary axis – 1 |  |  |  |  |  |

##### Checkback signals

The following table shows the data in the [control interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Reference point approach".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 3: SYNC  Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |
| Bytes 1 to 3 | Actual value:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … end of the rotary axis – 1 |

##### Causes of the POS_ERR error

You must find out the causes of errors with JOB 15 ([Display current values](#displaying-current-values-job-15-s7-300-s7-400)).

The following table shows the error numbers relevant for "Reference point approach" with the causes of the errors and possible remedies.

| Error number | Cause | Remedy |
| --- | --- | --- |
| 1 | Impermissible MODE in dosing operation |  |
| 2 | ERR_2L+ is displayed | Check the load voltage (2L+) at terminal 7. |
| 3 | ERR_ENCODER is displayed | Check the encoder wiring |
| 10 | Reference point approach: Reference point coordinate ≥ end of the rotary axis |  |
| 11 | No reference signal found up to the limit switch or between the limit switches | Check your switches, the encoder and the wiring |
| 13 | Direction of rotation of the drive and the encoder varies | Check the wiring of the drive and the encoder as well as the "[Reversal of the direction of rotation](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)" parameter. |

#### Profile of a reference point approach (S7-300, S7-400)

##### Execution of a Reference Point Run Depending on Parameterization and Start Position

The profile of a reference point approach depends on the assigned parameters and the start position.

Therefore, for a reference point approach, there are different scenarios which are dependent on

- The start position of the drive at the start of the reference point run
- The assigned parameter start direction
- The assigned parameter reference signal
- The assigned parameter reference switch.

##### Example 1: Reference point approach with reduction cam and zero mark

Start position and parameters assigned:

- Start position: between the minus limit switch and the reducing cam
- Start direction: Plus
- Reference signal: Reference switch and zero mark
- Reference switch: Reduction cam towards plus

The following figure shows a reference point approach with reducing cams and zero mark.

![Example 1: Reference point approach with reduction cam and zero mark](images/22229949451_DV_resource.Stream@PNG-en-US.png)

You can also carry out synchronization using the reducing cam without a zero mark.

If the start position is on the reducing cam, the 1PosU controls the drive directly at creep speed in the referencing direction.

##### Example 2: Reference Point Run with Minus Limit Switch

Start position and parameters assigned:

- Start position: between the minus limit switch and the plus limit switch
- Start direction: Minus
- Reference signal: Reference switch
- Reference switch: Limit switch minus

The following figure shows a reference point approach with minus limit switch.

![Example 2: Reference Point Run with Minus Limit Switch](images/22229991947_DV_resource.Stream@PNG-en-US.png)

You can also carry out synchronization at the limit switch with the following zero mark.

If the start position is on the limit switch, the 1PosU controls the drive directly at creep speed in the referencing direction.

##### Example 3: Reference Point Run with Reversal of Direction at the Plus Limit Switch

Start position and parameters assigned:

- Start position: between the minus limit switch and the reducing cam
- Start direction: Plus
- Reference signal: Reference switch and zero mark
- Reference switch: Reduction cam towards plus

The following figure shows a reference point approach with a direction reversal at the plus limit switch.

![Example 3: Reference Point Run with Reversal of Direction at the Plus Limit Switch](images/22230021643_DV_resource.Stream@PNG-en-US.png)

If the start position is at the plus limit switch, the 1PosU controls the drive directly at rapid traverse in the opposite direction to the assigned parameter start direction.

##### Example 4: Reference Point Run Only with Zero Mark

Start position and parameters assigned:

- Start position: between the minus limit switch and the plus limit switch
- Start direction: Minus
- Reference signal: Zero mark
- Reference switch: irrelevant

The following figure shows a reference point approach just with zero mark.

![Example 4: Reference Point Run Only with Zero Mark](images/22230067595_DV_resource.Stream@PNG-en-US.png)

### Relative positioning (MODE 4) (S7-300, S7-400)

#### Relative Positioning

In relative positioning the 1PosU moves the drive from the start position in a specified direction for a certain preset distance.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the distance, and start MODE 4, specifying the direction (DIR_M and DIR_P). The 1PosU moves the drive at the preset velocity (SPEED control bit) for that distance. At the switch-over point the 1PosU switches from rapid traverse to creep speed, and at the switch-off point the 1PosU terminates the traverse.

If you start during an active traverse, the 1PosU executes the necessary [change in direction](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400) after the time T <sub>min</sub> has elapsed.

The preset distance is not checked by the 1PosU. This means that more than one revolution may be involved with rotary axes.

In [dosing mode](#overview-of-the-functions-s7-300-s7-400), "Relative positioning" is only possible in the plus direction. The actual value is set to 0 at every start.

The figure below shows the sequence of the "Relative positioning" motion type.

![Relative Positioning](images/28155278731_DV_resource.Stream@PNG-en-US.png)

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Relative positioning".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bit 0.7 … 0.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | MODE 4 = Relative positioning |  |
| 0 | 1 | 0 | 0 |  |  |  |
| Bit 3: SPEED (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse)  Bit 2: DIR_M  Bit 1: DIR_P  Bit 0: START |  |  |  |  |  |  |
| Bytes 1 to 3 | distance:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … 16 777 215 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Relative positioning".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 3: SYNC  Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |
| Bytes 1 to 3 | Actual value:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |

#### Causes of the POS_ERR error

You must find out the causes of errors with dem JOB 15 ([Display current values](#displaying-current-values-job-15-s7-300-s7-400)).

The following table shows the error numbers relevant for "Relative positioning" with the causes of the errors and possible remedies.

| Error number | Cause | Remedy |
| --- | --- | --- |
| 2 | ERR_2L+ is displayed | Check the load voltage (2L+) at terminal 7. |
| 3 | ERR_ENCODER is displayed | Check the encoder wiring |
| 5 | The limit switch that lies in the direction in which the drive is moved is active | Check your switches and the wiring as well as the "[DI0 limit switch minus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" and "[DI1 limit switch plus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" parameters. |
| 7 | Relative positioning: Start withDIR_P = 0 and DIR_M = 0 or DIR_P = 1 and DIR_M = 1 |  |
| 13 | Direction of rotation of the drive and the encoder varies | Check the wiring of the drive and the encoder as well as the "[Reversal of the direction of rotation](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)" parameter. |
| 15 | In dosing mode: DIR_M = 1 |  |

### Absolute positioning (MODE 5) (S7-300, S7-400)

#### Absolute Positioning

With absolute positioning, the 1PosU moves the drive toward absolute targets. To do this, the axis must be synchronized.

"Absolute positioning" is not possible in activated dosing mode.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the target, and start MODE 5 with the necessary [directional enable](#effect-of-the-directional-enables-s7-300-s7-400) (DIR_M, DIR_P). The 1PosU moves the drive at the preset velocity (control bit SPEED) toward the target. At the switch-over point the 1PosU switches from rapid traverse to creep speed, and at the switch-off point the 1PosU terminates the traverse.

If you start during an active traverse, the 1PosU executes the necessary [change in direction](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400) after the time T <sub>min</sub> has elapsed.

#### Linear axis

The 1PosU determines the direction the destination is to be approached from. You must set the necessary directional enable (DIR_M, DIR_P) to start. You can also set both enables.

#### Rotary axis

You determine the direction in which the target is approached by selecting the directional enable (DIR_M, DIR_P):

| DIR_P and DIR_M control bits | Direction |
| --- | --- |
| DIR_P = 1  DIR_M = 0 | The destination is approached in the plus direction. |
| DIR_P = 0  DIR_M = 1 | The destination is approached in the minus direction. |
| DIR_P = 1  DIR_M = 1 | The destination is approached by the shortest route.  The 1PosU determines the direction the destination is to be approached from. If the resulting distance to be traversed is smaller than the switch-off difference, no traverse is started (POS_DONE = 1). |

The figure below shows the sequence of the "Absolute positioning" motion type.

![Rotary axis](images/28155345163_DV_resource.Stream@PNG-en-US.png)

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Absolute positioning".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bit 0.7 … 0.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | MODE 5 = Absolute positioning |  |
| 0 | 1 | 0 | 1 |  |  |  |
| Bit 3: SPEED (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse)  Bit 2: DIR_M  Bit 1: DIR_P  Bit 0: START |  |  |  |  |  |  |
| Bytes 1 to 3 | Target:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Absolute positioning".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 3: SYNC  Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |
| Bytes 1 to 3 | Actual value:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |

#### Causes of the POS_ERR error

You must find out the causes of errors with JOB 15 ([Display current values](#displaying-current-values-job-15-s7-300-s7-400)).

The following table shows the error numbers relevant for "Absolute positioning" with the causes of the errors and possible remedies.

| Error number | Cause | Remedy |
| --- | --- | --- |
| 1 | Impermissible MODE in dosing operation |  |
| 2 | ERR_2L+ is displayed | Check the load voltage (2L+) at terminal 7. |
| 3 | ERR_ENCODER is displayed | Check the encoder wiring |
| 4 | Axis is not synchronized (SYNC = 0) | You can synchronize the axis with:   - Reference point run - Reference Signal Evaluation - Setting Actual Value |
| 5 | The limit switch in the direction of which the drive is controlled is active | Check your switches and the wiring as well as the "[DI0 limit switch minus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" and "[DI1 limit switch plus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" parameters. |
| 7 | Start with DIR_P = 0 and DIR_M = 0 or relevant DIR_P = 0 or DIR_M = 0 control bit |  |
| 8 | Target ≥ end of rotary axis (at incremental encoders) or   target ≥ encoder range (at SSI encoders) |  |
| 9 | Absolute positioning was terminated because JOB 9 was initiated (only at incremental encoders) |  |
| 13 | Direction of rotation of the drive and the encoder varies | Check the wiring of the drive and the encoder as well as the "[Reversal of the direction of rotation](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)" parameter. |

### Canceling JOB Processing (JOB 0) (S7-300, S7-400)

#### Cancelling JOB processing

When you activate JOB 0, then the 1PosU reacts as follows:

- it cancels the current JOB 9 "Evaluate referencing signal",
- it cancels the current JOB 10 "Latch function",
- it sets a pending JOB_ERR = 0.

You can activate JOB 0 whatever the state of the axis.

#### Effect on the MODEs

MODEs are not affected by the JOB 0.

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Cancel JOB processing".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 0 = JOB-Cancel processing |  |
| 0 | 0 | 0 | 0 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Cancel JOB processing".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |

### Setting the Actual Value (JOB 1)  (S7-300, S7-400)

#### Setting actual value

"Set actual value" assigns new coordinates to the actual value displayed. This moves the operating range to another part of the axis.

The axis is synchronized at incremental encoders and non-activated dosing mode.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the new actual value coordinates and activate JOB 1.

The 1PosU sets the preset actual value coordinates to the actual value displayed in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) and sets the feedback bit SYNC = 1.

#### Effect on the MODEs

The following table shows the effects of JOB 1 on the various MODEs.

| MODE | What happens? |
| --- | --- |
| Reference point approach | At incremental encoders and in non-activated dosing mode, ensure that, when the reference point run is evaluated, the SYNC = 1 feedback bit is set immediately.  The reference point run still continues to run. |
| Inching | - |
| Absolute positioning | The following reactions are possible:  - Distance to the target ≤ switch-off difference  The switch-off point is reached or overshot; positioning is switched off immediately, and the run is terminated with POS_DONE = 1. In this case, the destination is sometimes overshot. - Distance to the destination ≤ the changeover difference  The changeover point is reached or overshot; there is an immediate reduction from rapid feed to creep feed. In this case, the distance covered at creep speed is less than (switch-over difference - switch-off difference). - Distance to the destination > the changeover difference  The drive is moved using rapid traverse, even if it was switched over to creep speed beforehand. |
| Relative Positioning | The preset distance continues to be traversed. |

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Set actual value".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 1 = Setting actual value |  |
| 0 | 0 | 0 | 1 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | Actual value coordinates:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Set actual value".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 3: SYNC |
| Bytes 1 to 3 | Actual value:  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Set actual value" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 23 | ERR_ENCODER is displayed | Check the encoder wiring |
| 34 | Actual value coordinates ≥ end of rotary axis (at incremental encoders) or actual value coordinate ≥ encoder range (at SSI encoders) |  |

### Shifting the encoder range (JOB 2)  (S7-300, S7-400)

#### Move Encoder Range

The "Shift encoder range" function can only be executed at SSI encoders.

"Shift encoder range" adjusts the encoder value so that the actual value displayed corresponds to the real actual value. Before this can be done, any active run must be terminated.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the offset and activate JOB 2.

You calculate the offset as follows:

- Offset = displayed actual value – real actual value

If the offset is negative, proceed as follows:

- Offset = displayed actual value - real actual value +  
   (number of rotations × number of increments)

The 1PosU accepts the preset offset and displays the real actual value coordinates at the [feedback interface](#1posu-feedback-interface-s7-300-s7-400).

#### Effect on the MODEs

MODEs are not affected by the JOB 2.

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Shift encoder range"

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 2 = Shift encoder range |  |
| 0 | 0 | 1 | 0 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | Offset (0 to encoder range) |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Shift encoder range".

| Address | Assignment |
| --- | --- |
| Bytes 1 to 3 | Actual value:  - 0 … encoder range – 1 |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Shift encoder range" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 21 | Impermissible JOB at the incremental encoder: |  |
| 23 | ERR_ENCODER is displayed | Check the encoder wiring |
| 26 | JOB 2 "Shift encoder range" cannot be initiated because there is an active traverse |  |
| 33 | with JOB 2: Offset not in encoder range |  |

### Changing the switch-off difference (JOB 3)  (S7-300, S7-400)

#### Change Switch-Off Difference

"Change switch-off difference" allows you to adjust the drive control to adapt to any changes in the load and mechanical conditions.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the new switch-off difference and activate JOB 3.

The 1PosU accepts the specified switch-off difference.

The switch-off difference remains valid until the [parameter assignment](#cpumaster-stop-and-reset-state-s7-300-s7-400) of the 1PosU is changed.

#### Effect on the MODEs

The following table shows the effects of JOB 3 on the various MODEs.

| MODE | What happens? |
| --- | --- |
| Reference point approach | - |
| Inching |  |
| Absolute positioning | Distance to the target ≤ switch-off difference  The switch-off point is reached or overshot; positioning is switched off immediately, and the run is terminated with POS_DONE = 1. In this case, the destination is sometimes overshot. |
| Relative Positioning |  |

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Change switch-off difference".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 3 = Change switch-off difference |  |
| 0 | 0 | 1 | 1 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | Switch-off difference  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … 16 777 215 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Change switch-off difference".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 0: JOB_ACK |

### Changing the changeover difference (JOB 4)  (S7-300, S7-400)

#### Change Changeover Difference

"Change switch-over difference" allows you to adjust the drive control to adapt to any changes in the load and mechanical conditions.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the new switch-over difference and activate JOB 4.

The 1PosU accepts the specified switch-over difference.

The switch-over difference remains valid until the [parameter assignment](#cpumaster-stop-and-reset-state-s7-300-s7-400) of the 1PosU is changed.

#### Effect on the MODEs

The following table shows the effects of JOB 4 on the various MODEs.

| MODE | What happens? |
| --- | --- |
| Reference point approach | - |
| Inching |  |
| Absolute positioning | The following reactions are possible:  - Distance to the destination ≤ the changeover difference.  The changeover point is reached or overshot; there is an immediate reduction from rapid feed to creep feed. In this case, the distance covered at creep speed is less than (switch-over difference - switch-off difference). - Distance to the destination > the changeover difference  The drive is moved using rapid feed, even if it was switched over to creep feed beforehand. |
| Relative Positioning |  |

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Change switch-over difference".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 4 = Change switch-over difference |  |
| 0 | 1 | 0 | 0 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | Switch-over difference:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … 16 777 215 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Change changeover difference".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 0: JOB_ACK |

### Evaluating the reference signal (JOB 9)  (S7-300, S7-400)

#### Evaluating the reference signal

The "Evaluate reference signal" function is only available at incremental encoders and in non-active dosing mode.

"With "Evaluate reference signal" you can synchronize the axis using an external reference signal during a current traverse in "Jogging" and "Relative positioning" MODEs. You can use either the [3 digital inputs or the zero mark](#profile-of-a-reference-point-approach-s7-300-s7-400) as a reference signal.

You can assign parameters to the digital inputs DI0 (minus limit switch), DI1 (plus limit switch) and DI2 (reducing cam) as NC or NO contacts.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the reference point coordinates and activate JOB 9. The 1PosU sets the SYNC = 0 checkback signal.

If the 1PosU detects the passing of the assigned parameter reference signal in the reference direction, the axis is synchronized. The 1PosU sets the checkback signal SYNC = 1 and assigns the reference point coordinates to the actual value.

The reference direction is controlled by the "Reference signal" and "Reference switch" parameters.

|  | Reference switch: Reduction cam towards minus | Reference switch: Reduction cam towards plus | Reference switch: Limit switch minus | Reference switch: Limit switch plus |
| --- | --- | --- | --- | --- |
| **Reference signal: Reference switch and zero mark** | Minus referencing direction | Plus referencing direction | Plus referencing direction | Minus referencing direction |
| **Reference signal: Reference switch** |  |  |  |  |
| **Reference signal: Zero mark** | The referencing direction is not defined. The axis is synchronized at the next zero mark. |  |  |  |

#### Effect on the MODEs

The following table shows the effects of JOB 9 on the various MODEs.

| MODE | What happens? |
| --- | --- |
| Reference point approach | The reference coordinates transferred with JOB 9 are valid. |
| Inching | - |
| Absolute positioning | Traverse is cancelled with POS_ERR = 1, as SYNC us deleted |
| Relative positioning | - |

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Evaluate reference signal".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 9 = Evaluating the reference signal |  |
| 1 | 0 | 0 | 1 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | Reference point coordinates:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … end of the rotary axis – 1 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [control interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Evaluate reference signal".

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 3: SYNC |
| Bytes 1 to 3 | Actual value:  - Linear axis: 0 … 16 777 215 - Rotary axis: 0 … end of the rotary axis – 1 |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Evaluate the reference signal" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 21 | Impermissible JOB at SSI encoders or in dosing operation |  |
| 23 | ERR_ENCODER is displayed | Check the encoder wiring |
| 30 | Reference point coordinate ≥ end of the rotary axis |  |

### Latch Function (JOB 10) (S7-300, S7-400)

#### Latch Function

The "Latch function" allows you to store the actual value once at an edge at the DI2 digital input. You can use this function, for example, to detect edges or measure lengths.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the desired edge and activate JOB 10.

If the 1PosU detects the preset edge at the DI2 digital input, it stores the associated actual value, displays it as a [feedback value](#1posu-feedback-interface-s7-300-s7-400) and sets the LATCH_DONE = 1 feedback bit.

You can then activate the "Latch function" again.

#### Latch function and reference point approach or "Evaluate the reference signal"

If the 1PosU synchronizes at the same edge, it stores the actual value before it assigns the reference point coordinates.

#### Effect on the MODEs

MODEs are not affected by the JOB 10.

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Latch function".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 10 = Latch function |  |
| 1 | 0 | 1 | 0 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Byte 5 | Bit 1: Latch at negative edge at DI2  Bit 0: Latch at positive edge at DI2 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Latch function".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 2: LATCH_DONE  Bit 1: JOB_ERR  Bit 0: JOB_ACK |
| Bytes 5 to 7 | Feedback value: Actual value at the edge at the DI2  - at the incremental encoder:   - Linear axis: 0 … 16 777 215   - Rotary axis: 0 … end of the rotary axis – 1 - at the SSI encoder:   - 0 … encoder range – 1 |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Latch function" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 23 | ERR_ENCODER is displayed | Check the encoder wiring |
| 36 | Edge selection unknown |  |

### Defining the settings for monitoring the direction of rotation (JOB 11)  (S7-300, S7-400)

#### Setting the Monitoring of the Direction of Rotation

The "Define the settings for monitoring the direction of rotation" function is not available in dosing mode.

With "Define the settings for monitoring the direction of rotation" you can adjust the monitoring of the 1PosU's direction of rotation to suit your load and mechanical conditions.

Monitoring of the direction of rotation is always active. The 1PosU detects whether the direction of rotation of the drive and the encoder is the same. Direction of rotation monitoring will tolerate different directions for the drive and the encoder up to the preset path difference. If the specified distance is exceeded then the 1PosU reports POS_ERR = 1.

Unless you have activated JOB 11, double the switch-off difference is used from the parameters as the path difference. JOB 3 "Change switch-off difference" does not affect the distance difference for the purpose of monitoring the direction of rotation.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the new distance difference and activate JOB 11.

The 1PosU accepts the preset distance difference for the monitoring of the direction of rotation.

The distance difference for the monitoring of the direction of rotation remains valid until the [parameter assignment](#cpumaster-stop-and-reset-state-s7-300-s7-400) of the 1PosU is changed.

#### Disabling the Monitoring of the Direction of Rotation

Monitoring of the direction of rotation is disabled when the path difference is 0.

#### Effect on the MODEs

MODEs are not affected by the JOB 11.

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Define the settings for monitoring the direction of rotation".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 11 = Define the settings for monitoring the direction of rotation |  |
| 1 | 0 | 1 | 1 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Byte 5 | 0 |  |  |  |  |  |
| Bytes 6, 7 | Distance difference for monitoring the direction of rotation  - 0 … 65 535 |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Define the settings for monitoring the direction of rotation".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Define the settings for monitoring the direction of rotation" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 21 | Impermissible JOB in dosing mode |  |
| 38 | Monitoring of the direction of rotation path difference > 65 535 |  |

### Displaying current values (JOB 15)  (S7-300, S7-400)

#### Display Current Values

You can display the following values in the feedback interface as feedback values:

- Residual distance
- Actual speed
- Causes of errors POS_ERR and JOB_ERR

The residual distance is set by the 1PosU as the default for the feedback value.

The 1PosU continuously displays the actual value in the feedback interface irrespective of the selected feedback value.

Provide the [control interface](#1posu-control-interface-s7-300-s7-400) with the desired feedback value and activate JOB 15.

The selected feedback value remains valid until the [parameter assignment](#cpumaster-stop-and-reset-state-s7-300-s7-400) of the 1PosU is changed.

#### "Display current values and latch function

If you activate the latch function, the 1PosU sets a feedback value of 0 and displays the actual value at the edge at the DI2 digital input.

You can only activate JOB 15 again after the latch function has terminated.

#### Residual distance

The 1PosU calculates the distance to the target as the residual distance in the "Absolute positioning" and "Relative positioning" MODEs. As long as the actual value is before the destination, the residual distance remains positive. It becomes negative when the destination is overshot. The residual distance is 0 in the other MODEs.

The 1PosU displays the residual distance with a sign between -8 388 608 and 8 388 607 increments. Negative values are displayed in twos complement. If the actual residual distance is beyond these limits, the limit value is displayed.

#### Actual speed

The 1PosU calculates the actual velocity as an encoder value change in increments per 10 ms. It displays these between 0 and 16 777 215.

#### Causes of errors POS_ERR and JOB_ERR

The 1PosU displays the causes of errors for POS_ERR and JOB_ERR as well as the MODE and JOB entered in the [control interface](#1posu-control-interface-s7-300-s7-400).

#### Effect on the MODEs

MODEs are not affected by the JOB 15.

#### Control signals

The following table shows the data in the [control interface](#1posu-control-interface-s7-300-s7-400) which is relevant for "Display current values".

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 4 | Bit 4.7 … 4.4: |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 | JOB 15 = Display current values |  |
| 1 | 1 | 1 | 1 |  |  |  |
| Bit 0: JOB_REQ |  |  |  |  |  |  |
| Byte 5 | 0: Residual distance  1: Actual speed  2: Causes of errors POS_ERR and JOB_ERR |  |  |  |  |  |

#### Checkback signals

The following table shows the data in the [feedback interface](#1posu-feedback-interface-s7-300-s7-400) which is relevant for "Display current values".

| Address | Assignment |
| --- | --- |
| Byte 4 | Bit 1: JOB_ERR  Bit 0: JOB_ACK |
| Bytes 5 to 7 | In accordance with the selected feedback value:  - With a residual distance of: –8 388 608 … 8 388 607 - With an actual speed of: 0 … 16 777 215 - with causes of POS_ERR and JOB_ERR errors:   - Byte 5: [Causes of](#causes-of-pos_err-error-s7-300-s7-400) POS_ERR error   - Byte 6: [Causes of](#causes-of-job_err-error-s7-300-s7-400) JOB_ERR error   - Bit 7.3 … 7.0: MODE (= bits 0.7 to 0.4 from the control signals)   - Bit 7.7 … 7.4: JOB (= bits 4.7 to 4.4 from the control signals) |

#### Causes of the JOB_ERR error

The following table shows the error numbers relevant for "Display current values" with the causes of the errors and possible remedies.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 35 | Display current values: Selection unknown |  |
| 37 | Display current values: JOB 15 cannot be activated with the latch function running. |  |

### Error detection / diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [Overview of errors with 1PosU (S7-300, S7-400)](#overview-of-errors-with-1posu-s7-300-s7-400)
- [Parameter assignment error (S7-300, S7-400)](#parameter-assignment-error-s7-300-s7-400)
- [External errors (S7-300, S7-400)](#external-errors-s7-300-s7-400)
- [Errors in the control of MODEs and JOBs (S7-300, S7-400)](#errors-in-the-control-of-modes-and-jobs-s7-300-s7-400)
- [Error acknowledgment EXTF_ACK (S7-300, S7-400)](#error-acknowledgment-extf_ack-s7-300-s7-400)
- [Causes of POS_ERR error (S7-300, S7-400)](#causes-of-pos_err-error-s7-300-s7-400)
- [Causes of JOB_ERR error (S7-300, S7-400)](#causes-of-job_err-error-s7-300-s7-400)

#### Overview of errors with 1PosU (S7-300, S7-400)

Various errors can occur when working with the 1PosU. The following types of error are differentiated between:

- [Parameter assignment error](#parameter-assignment-error-s7-300-s7-400)
- [External Errors](#external-errors-s7-300-s7-400)
- [Errors in the Control of MODEs and JOBs](#errors-in-the-control-of-modes-and-jobs-s7-300-s7-400)

You must [acknowledge](#error-acknowledgment-extf_ack-s7-300-s7-400) the "Load voltage missing", "Short circuit of the encoder supply" and "Wire break/short circuit of the encoder signals" errors.

If errors occur when starting MODEs or activating JOBs, you can find more information here:

- [Causes of POS_ERR error](#causes-of-pos_err-error-s7-300-s7-400)
- [Causes of JOB_ERR error](#causes-of-job_err-error-s7-300-s7-400)

#### Parameter assignment error (S7-300, S7-400)

##### Parameter assignment error

The following table shows 1PosU parameter assignment errors.

| Parameter assignment error | 1PosU reactions |
| --- | --- |
| Causes:  - The 1PosU cannot identify existing parameters as its own. - The 1PosU slot you have configured does not match the structure.     Only at SSI encoder:  - Impermissible value for "Pulses per encoder revolution" parameter. - Impermissible value for "Revolutions" parameter. - Pulses per encoder revolution × revolutions is greater than 4096 × 4096.     Only for dosing operation:  - Activated "Encoder signal diagnostics" - Activated "Reversal of the direction of rotation"     What to Do:  - Check the configuration and structure. | - The 1PosU is not configured and cannot execute its functions. - Generating channel-specific diagnostics |

#### External errors (S7-300, S7-400)

##### External errors

The following table shows 1PosU external errors.

| Symbol | Meaning |
| --- | --- |
| **Load Voltage 2L+ Missing** | **Reactions of the**  **1PosU** |
| Causes:  - Load voltage 2L+ not present or too low at terminal 7   Remedy:  - Check the wiring. Eliminate a possible short-circuit. - [Acknowledge](#error-acknowledgment-extf_ack-s7-300-s7-400) the error with the EXTF_ACK control bit. | - The current traverse is halted; it is not possible to start a new traverse.   - All 3 digital outputs are set to 0.   - POS_ERR = 1 feedback bit   - POS_DONE = 0 feedback bit - ERR_2L+ = 1 feedback bit - generate channel-specific diagnostics - waits for EXTF_ACK error acknowledgment |
| **Short circuit of the encoder supply** | **Reactions of the**  **1PosU** |
| Causes:  - Short circuit of the encoder supply made available at terminals 6 and 10   Remedy:  - Check the wiring and correct the short circuit. - [Acknowledge](#error-acknowledgment-extf_ack-s7-300-s7-400) the error with the EXTF_ACK control bit. | - The current "Reference point approach", "Relative positioning" and "Absolute positioning" MODEs are stopped; it is not possible to start a new traverse in these MODEs.   - All 3 digital outputs are set to 0.   - POS_ERR = 1 feedback bit   - POS_DONE = 0 feedback bit - ERR_ENCODER = 1 feedback bit - SYNC = 0 feedback bit - generate channel-specific diagnostics - waits for EXTF_ACK error acknowledgment - Jogging MODE is not affected by this error. - The current "Evaluate referencing signal" JOB is cancelled. |
| **Wire break/short circuit of the encoder signals** | **Reactions of the**  **1PosU** |
| **If an SSI encoder is used:**   Requirements:  - To detect errors at the encoder signals, you must enable the "Encoder signal diagnostics" parameter.   Causes:  - Wire break or short circuit of the encoder signals at terminals 9 and 13 or 12 and 16. - The parameters for the SSI encoder do not correspond to the encoder connected.   Remedy:  - Check the wiring and correct the short circuit. - Compare the configuration with the technical specifications of the encoder. - [Acknowledge](#error-acknowledgment-extf_ack-s7-300-s7-400) the error with the EXTF_ACK control bit.      **The following applies when using an incremental encoder:**   Requirement:  - You must enable the "Encoder signal diagnostics" parameter for error detection at the A, /A and B, /B signals with 5V differential signal or at the A* and B* with 24V differential signal. - The "Zero marker diagnostics" parameter must be enabled in order to allow error recognition at the N, /N signals with 5V differential signal. If you use an encoder without a zero mark, switch off error detection. If dosing mode is activated, "Zero marker signal diagnostics" is not possible.   Causes:  - For 5V differential signal: Wire break or short circuit of the encoder signals at terminals 9 and 13 or 11 and 15 or 12 and 16. - Edge error of the encoder signals recognized so that 1PosU cannot carry out clear direction recognition.   Remedy:  - Check the wiring and correct the short circuit. - [Acknowledge](#error-acknowledgment-extf_ack-s7-300-s7-400) the error with the EXTF_ACK control bit. | - The current "Reference point approach", "Relative positioning" and "Absolute positioning" MODEs are stopped; it is not possible to start a new traverse in these MODEs.   - All 3 digital outputs are set to 0.   - POS_ERR = 1 feedback bit   - POS_DONE = 0 feedback bit - ERR_ENCODER = 1 feedback bit - SYNC = 0 feedback bit - generate channel-specific diagnostics - waits for EXTF_ACK error acknowledgment - Jogging MODE is not affected by this error. - The current "Evaluate referencing signal" JOB is cancelled. |

#### Errors in the control of MODEs and JOBs (S7-300, S7-400)

##### Errors in the control of MODEs and JOBs

The following tables shows errors in the control of MODEs and JOBs with the 1PosU.

| Symbol | Meaning |
| --- | --- |
| **POS_ERR** | **Reactions of the**  **1PosU** |
| Causes:  - Certain requirements or conditions have not been met at the start of a MODEs | - The MODE started is not executed. - The current traverse is stopped.   - All 3 digital outputs are set to 0.   - POS_ERR = 1 feedback bit   - POS_DONE = 0 feedback bit |
| **JOB_ERR** | **Reactions of the**  **1PosU** |
| Causes:  - Certain requirements or conditions have not been met at the start of a JOBs | - The activated JOB is not executed.   - JOB_ERR = 1 feedback bit |

#### Error acknowledgment EXTF_ACK (S7-300, S7-400)

##### EXTF_ACK error acknowledgment

You must [acknowledge](#external-errors-s7-300-s7-400) the "Load voltage missing", "Short circuit of the encoder supply" and "Wire break/short circuit of the encoder signals" corrected external errors. The following table shows the sequence necessary for this.

| What You Do | 1PosU reactions |
| --- | --- |
|  | - ERR_2L+ = 1 feedback bit  and/or  - ERR_ENCODER = 1 feedback bit |
| Your control program detects the set ERR_2L+ or ERR_ENCODER feedback bit.  Execute your application-specific error response.  Eliminate the cause of the error. |  |
| Switch the EXTF_ACK[control bit](#1posu-control-interface-s7-300-s7-400) from 0 to 1 | The 1PosU sets the ERR_2L+ = 0 and ERR_ENCODER = 0[feedback bits](#1posu-feedback-interface-s7-300-s7-400).  This tells you that the cause has been eliminated and acknowledged.  If ERR_2L+ = 1 and/or ERR_ENCODER = 1, the cause of the error has not yet been eliminated. |
| Switch the EXTF_ACK[control bit](#1posu-control-interface-s7-300-s7-400) from 1 to 0. |  |
| In the case of constant error acknowledgment (EXTF_ACK = 1) or at CPU/Master Stop, the 1PosU reports the errors as soon as they are detected and deletes them as soon as they have been eliminated. |  |

#### Causes of POS_ERR error (S7-300, S7-400)

##### Causes of the POS_ERR error

The following table shows the causes and possible remedies for the POS_ERR error.

| Error number | Cause | Remedy |
| --- | --- | --- |
| 1 | MODE unknown or impermissible | Permissible MODEs are:  - MODE 0 - MODE 1 - MODE 3 (not possible at SSI encoders or in dosing mode) - MODE 4 - MODE 5 (not possible in dosing mode) |
| 2 | ERR_2L+ is displayed | Check the load voltage (2L+) at terminal 7. |
| 3 | ERR_ENCODER is displayed | Check the encoder wiring |
| 4 | Axis is not synchronized (SYNC = 0) | SSI encoder:  - Eliminate the encoder error.     The axis can be synchronized at incremental encoders and non-activated dosing mode with:  - Reference point approach - Evaluating the reference signal - Set actual value |
| 5 | The limit switch in the direction of which the drive is controlled is active | Check your switches and the wiring as well as the "[DI0 limit switch minus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" and "[DI1 limit switch plus](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)" parameters. |
| 7 | Inching: DIR_P = 1 and DIR_M = 1  Absolute positioning: Start with DIR_P = 0 and DIR_M = 0 or relevant DIR_P = 0 or DIR_M = 0 control bit  Relative positioning: Start withDIR_P = 0 and DIR_M = 0 or DIR_P = 1 and DIR_M = 1 |  |
| 8 | Absolute positioning : Target ≥ end of rotary axis at incremental encoders or target ≥ encoder range at SSI encoders |  |
| 9 | Absolute positioning was terminated because JOB 9 was initiated |  |
| 10 | Reference point approach: Reference point coordinate ≥ end of the rotary axis |  |
| 11 | Reference point approach:  No reference signal found up to the limit switch or between the limit switches | Check your switches, the encoder and the wiring |
| 13 | Direction of rotation of the drive and the encoder varies | Check the wiring of the drive and the encoder as well as the "[Reversal of the direction of rotation](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)" parameter. |
| 15 | Jogging, relative positioning: In dosing mode DIR_M = 1 |  |

#### Causes of JOB_ERR error (S7-300, S7-400)

##### Causes of the JOB_ERR error

The following table shows the causes and possible remedies for the POS_ERR error.

| Error number | Meaning | Remedy |
| --- | --- | --- |
| 21 | JOB unknown or impermissible | Permissible JOBs are:  - JOB 0 - JOB 1 - JOB 2 (only possible at SSI encoders) - JOB 3 - JOB 4 - JOB 9 (not possible at SSI encoders or in [dosing mode](#overview-of-the-functions-s7-300-s7-400)) - JOB 10 - JOB 11 (not possible in dosing mode) - JOB 15 |
| 23 | ERR_ENCODER is displayed | Check the encoder wiring |
| 26 | JOB 2 "Shift encoder range" cannot be initiated because there is an active traverse |  |
| 29 | Evaluating the Reference Signal: Reference point coordinate ≥ end of the rotary axis |  |
| 34 | Setting an Actual Value: Actual value coordinates ≥ encoder range |  |
| 35 | Display current values: Selection unknown |  |
| 36 | Latch Function: Edge selection unknown |  |
| 37 | Display current values: JOB 15 cannot be activated with the latch function running. |  |
| 38 | Monitoring of the direction of rotation  path difference > 65 535 |  |

### CPU/Master STOP and RESET state (S7-300, S7-400)

#### Behavior in CPU/Master-STOP

The following table shows the behavior of 1PosU in CPU/Master-STOP.

| Behavior in CPU/Master-STOP | 1PosU reactions |
| --- | --- |
| - due to POWER-OFF of the CPU / bus master  or  - due to POWER-OFF of the IM 151 / IM 151 FO   or  - due to failure of bus transmission   or  - Due to change from RUN to STOP | - The current traverse is stopped. - All 3 digital outputs are set to 0. - POS_ERR = 0[feedback bit](#1posu-feedback-interface-s7-300-s7-400) - POS_DONE = 1[feedback bit](#1posu-feedback-interface-s7-300-s7-400) |

#### Exiting the CPU/Master STOP status

The following table shows the behavior of 1PosU after exiting the CPU/Master-STOP status.

| Exiting the CPU/Master STOP status | 1PosU reactions |
| --- | --- |
| - with POWER-ON of the CPU / bus master  or  - with POWER-OFF of the IM 151 / IM 151 FO   or  - after failure of the bus transmission   or  - After a change from STOP to RUN | - The [feedback interface](#1posu-feedback-interface-s7-300-s7-400) of the 1PosU remains current. - The axis remains synchronized, and the actual value is current. - The moved encoder range remains valid. - The changed switch-off and changeover differences and the path difference for the monitoring of the direction of rotation remain valid. - An initiated "[Evaluate referencing signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)" JOB 9 and "[Latch function](#latch-function-job-10-s7-300-s7-400)" JOB 10 remain active. - The [feedback value](#displaying-current-values-job-15-s7-300-s7-400) selected with JOB 15is current. |

#### RESET state of the 1PosU

The following table shows the behavior of the 1PosU in RESET state.

| RESET state of the 1PosU and changing the 1PosU parameters | 1PosU reactions |
| --- | --- |
| - due to changing the parameters of the 1PosU and downloading the parameter assignment or configuration of the ET 200S station to the CPU / bus master  or  - due to POWER-ON at the power module of the 1PosU   or  - inserting the 1PosU in an energized state | - The axis is synchronized, and the actual value corresponds to the current encoder value. - The encoder range has not been moved. - The switch-off and changeover difference is accepted from the parameters. - The path difference for the monitoring of the direction of rotation is set at double the switch-off difference. - "[Evaluate referencing signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)" JOB 9 and "[Latch function](#latch-function-job-10-s7-300-s7-400)" JOB 10 are not active. - The residual distance is displayed as a [feedback value](#displaying-current-values-job-15-s7-300-s7-400). |

## Configuring and assigning parameters to 1PosU (S7-300, S7-400)

This section contains information on the following topics:

- [Operation (S7-300, S7-400)](#operation-s7-300-s7-400)
- [Parameters for incremental encoders with 5V differential signal (S7-300, S7-400)](#parameters-for-incremental-encoders-with-5v-differential-signal-s7-300-s7-400)
- [Parameters for incremental encoders with 24V signals (S7-300, S7-400)](#parameters-for-incremental-encoders-with-24v-signals-s7-300-s7-400)
- [Parameters for SSI encoders (S7-300, S7-400)](#parameters-for-ssi-encoders-s7-300-s7-400)
- [1PosU control and feedback interface (S7-300, S7-400)](#1posu-control-and-feedback-interface-s7-300-s7-400)

### Operation (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting the encoder interface (S7-300, S7-400)](#selecting-the-encoder-interface-s7-300-s7-400)

#### Selecting the encoder interface (S7-300, S7-400)

##### Encoder interface

You define the 1PosU signal type you want to use by setting the encoder interface.

| Encoder interface | Description |
| --- | --- |
| [5V differential signal](#parameters-for-incremental-encoders-with-5v-differential-signal-s7-300-s7-400) | The 1PosU receives the signals from the incremental encoders with 5V differential signal. |
| [24 V differential signal](#parameters-for-incremental-encoders-with-24v-signals-s7-300-s7-400) | The 1PosU receives the signals from the incremental encoders with 24V signals. |
| [SSI absolute](#parameters-for-ssi-encoders-s7-300-s7-400) | The 1PosU receives the signals from the absolute encoders (SSI). |

### Parameters for incremental encoders with 5V differential signal (S7-300, S7-400)

This section contains information on the following topics:

- [Enables (S7-300, S7-400)](#enables-s7-300-s7-400)
- [Encoder and axes (S7-300, S7-400)](#encoder-and-axes-s7-300-s7-400)
- [Digital inputs (S7-300, S7-400)](#digital-inputs-s7-300-s7-400)
- [Reference point approach and evaluation of the reference signal (S7-300, S7-400)](#reference-point-approach-and-evaluation-of-the-reference-signal-s7-300-s7-400)
- [Drive (S7-300, S7-400)](#drive-s7-300-s7-400)

#### Enables (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400)
- [Enabling encoder signal diagnostics (S7-300, S7-400)](#enabling-encoder-signal-diagnostics-s7-300-s7-400)
- [Enable zero mark signal diagnostics (S7-300, S7-400)](#enable-zero-mark-signal-diagnostics-s7-300-s7-400)

##### Enabling group diagnostics (S7-300, S7-400)

###### Group diagnostics

You enable group diagnostics by ticking the corresponding options box.

When group diagnostics is enabled, an encoder error (ERR_ENCODER), no load voltage (ERR_2L+) or a parameter assignment error will result in a channel-specific diagnostics.

##### Enabling encoder signal diagnostics (S7-300, S7-400)

###### Encoder signal diagnostics

You enable encoder signal diagnostics by ticking the corresponding options box.

With "Encoder signal diagnostics" enabled, encoder signals A, /A and B, /B are monitored for short circuit and wire break. With non-enabled dosing mode, the signal sequence is also monitored. A simultaneous edge change at signals A and B causes an error.

##### Enable zero mark signal diagnostics (S7-300, S7-400)

###### Zero mark signal diagnostics

You enable zero mark signal diagnostics by ticking the corresponding options box.

With "Zero mark signal diagnostics" enabled, zero mark signals N, /N are monitored for short circuit and wire break.

#### Encoder and axes (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling dosing mode (S7-300, S7-400)](#enabling-dosing-mode-s7-300-s7-400)
- [Enabling reversal of direction of rotation (S7-300, S7-400)](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400)
- [Selecting axis type (S7-300, S7-400)](#selecting-axis-type-s7-300-s7-400)
- [Specifying end of rotary axis (S7-300, S7-400)](#specifying-end-of-rotary-axis-s7-300-s7-400)

##### Enabling dosing mode (S7-300, S7-400)

###### Dosing mode

You enable dosing mode by ticking the corresponding options box.

In [dosing mode](#overview-of-the-functions-s7-300-s7-400), 1PosU only evaluates encoder signals A and /A. As a result, the distance can only be changed in the positive direction. The actual value is incremented at each positive edge.

##### Enabling reversal of direction of rotation (S7-300, S7-400)

###### Reversal of direction of rotation

You enable reversal of direction of rotation by ticking the corresponding options box.

You can use the "Reversal of direction of rotation" parameter to adapt the direction of rotation of the encoder to that of the drive and the axis.

In [dosing mode](#overview-of-the-functions-s7-300-s7-400), reversal of the direction of rotation is not possible.

##### Selecting axis type (S7-300, S7-400)

###### Axis types

The 1PosU positioning module can control the following axis types:

- Linear axis

  A linear axis is an axis which has a limited physical traversing range.

  ![Axis types](images/24575900299_DV_resource.Stream@PNG-en-US.png)
- Rotary axis

  The rotary axis is an axis whose traversing range is not restricted by mechanical stops.

  ![Axis types](images/24575948427_DV_resource.Stream@PNG-en-US.png)

##### Specifying end of rotary axis (S7-300, S7-400)

###### End of rotary axis

This parameter is only relevant for the "Rotary axis" axis type.

The value "end of rotary axis" is the theoretical maximum value that the actual value can reach. The theoretically highest value is however never displayed, because it physically identifies the same position as the start of the rotary axis (0).

The displayed value jumps at

- high limit violated of (end of rotary axis – 1) to 0
- low limit violated of 0 to (end of rotary axis – 1)

Permitted value range for the end of the rotary axis: 1 … 16 777 215  
Specifying "0" causes a configuration error.

#### Digital inputs (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting minus limit switch and plus limit switch (S7-300, S7-400)](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400)
- [Selecting reduction cam (S7-300, S7-400)](#selecting-reduction-cam-s7-300-s7-400)

##### Selecting minus limit switch and plus limit switch (S7-300, S7-400)

###### Function of the hardware limit switches

The two digital inputs (DI0 and DI1) are evaluated by the 1PosU as limit switches:

- DI0 is the minus limit switch and limits the operating range in the minus direction.
- DI1 is the plus limit switch and limits the operating range in the plus direction.

You can assign parameters to the hardware limit switches **separately as NC or NO contacts**.

The hardware limit switches are evaluated with linear axes and rotary axes.

Only the hardware limit switch that lies in the direction in which the drive is being moved is evaluated.

This enables you to move away from a hardware limit switch without additional error acknowledgment by moving in the other direction if you reach or overrun a hardware limit switch.

The current signal level of the digital inputs is displayed in the feedback interface, delayed by the update rate.

The following table shows how the hardware limit switches work in the individual MODEs.

| MODE | Function of the hardware limit switches |
| --- | --- |
| Reference point approach | The 1PosU executes an automatic direction reversal at the hardware limit switch. |
| Inching | The motion of the axis is halted on the hardware limit switch, all 3 digital outputs are set to 0, and the POS_ERR feedback bit is reported. |
| Absolute Positioning |  |
| Relative Positioning |  |

###### Starting on the hardware limit switch

The following table shows the reaction of the 1PosU when starting MODEs on the hardware limit switch.

| Direction | 1PosU reactions |
| --- | --- |
| Starting into the operating range | The 1PosU starts the specified MODE. |
| Starting away from the operating range | The POS_ERR = 1 feedback bit is set. |

##### Selecting reduction cam (S7-300, S7-400)

###### Function of the reduction cam

The digital input DI2 is evaluated as a reduction cam or latch input by 1PosU:

- as a reduction cam with MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)" and with JOB 9 "[Evaluate referencing signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)"
- as a latch input with JOB 10 "[Latch function](#latch-function-job-10-s7-300-s7-400)"

You can assign parameters to the hardware limit switches separately as **NC or NO contacts**.

#### Reference point approach and evaluation of the reference signal (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting reference signal (S7-300, S7-400)](#selecting-reference-signal-s7-300-s7-400)
- [Selecting reference switch (S7-300, S7-400)](#selecting-reference-switch-s7-300-s7-400)
- [Selecting start direction (S7-300, S7-400)](#selecting-start-direction-s7-300-s7-400)

##### Selecting reference signal (S7-300, S7-400)

###### Reference signal

The "Reference signal" parameter defines the relevant switch or combination of switches and zero marks for MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)" and JOB 9 "[Evaluate reference signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)". The following are selectable:

- Reference switch and zero mark
- Reference switch
- Zero mark

You select the type of reference switch with the "[Reference switch](#selecting-reference-switch-s7-300-s7-400)" parameter.

##### Selecting reference switch (S7-300, S7-400)

###### Reference switch

The "Reference switch" parameter defines the relevant switch and the reference direction in which the switch must be overrun. The following are selectable:

- Reduction cam towards minus
- Reduction cam towards plus
- Limit switch minus
- Limit switch plus

These parameters are only relevant if you have selected it with "[reference signal](#selecting-reference-signal-s7-300-s7-400)"

- Reference switch and zero mark

  or
- Reference switch

##### Selecting start direction (S7-300, S7-400)

###### Start direction

The "Start direction" parameter defines the start direction for the MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)". The following are selectable:

- Plus
- Minus

#### Drive (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting control mode (S7-300, S7-400)](#selecting-control-mode-s7-300-s7-400)
- [Entering the switch-off difference (S7-300, S7-400)](#entering-the-switch-off-difference-s7-300-s7-400)
- [Entering the changeover difference (S7-300, S7-400)](#entering-the-changeover-difference-s7-300-s7-400)
- [Entering the delay time for the direction change (S7-300, S7-400)](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400)

##### Selecting control mode (S7-300, S7-400)

###### Control mode

The"Control mode" parameter defines the function of the digital outputs for the [control of the drive](#axis-drive-and-encoder-s7-300-s7-400). The following are selectable:

- Control mode 0:

  - DO0 travel minus
  - DO1 travel plus
  - DO2 rapid/creep feed
- Control mode 1:

  - DO0 rapid feed
  - DO1 creep feed (rapid feed is 0)
  - DO2 traverse plus (1 )/ traverse minus (0)

##### Entering the switch-off difference (S7-300, S7-400)

###### Switch-off difference

[Switch-off difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from creep speed to 0.

If the switch-off difference ≥ the changeover difference, there is no changeover point. There is no deceleration from rapid traverse to creep speed; the response is executed directly at the switch-off point.

Valid value range:

- 0 to 65,535

You can use [JOB 3](#changing-the-switch-off-difference-job-3-s7-300-s7-400) to change the switch-off difference.

##### Entering the changeover difference (S7-300, S7-400)

###### Changeover difference

[Changeover difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from rapid traverse to creep speed.

Valid value range:

- 0 to 65,535

You can use [JOB 4](#changing-the-changeover-difference-job-4-s7-300-s7-400) to change the changeover difference.

##### Entering the delay time for the direction change (S7-300, S7-400)

###### T<sub>min</sub> direction change

The "T<sub>min</sub> direction change" parameter defines the delay time for the direction change. The digital outputs are switched off, and a change of direction by T<sub>min</sub> is executed with a delay. T<sub>min</sub> is effective at each change of direction during a run.

T<sub>min</sub> does not work when starting after POS_DONE = 1 or POS_ERR = 1.

Valid value range:

- 0 to 255

Your input value is multiplied by 10. You thus specify T<sub>min</sub> in increments of 10 ms (for example, 0 ms, 10 ms or 2550 ms).

### Parameters for incremental encoders with 24V signals (S7-300, S7-400)

This section contains information on the following topics:

- [Enables (S7-300, S7-400)](#enables-s7-300-s7-400-1)
- [Encoder and axes (S7-300, S7-400)](#encoder-and-axes-s7-300-s7-400-1)
- [Digital inputs (S7-300, S7-400)](#digital-inputs-s7-300-s7-400-1)
- [Reference point approach and evaluation of the reference signal (S7-300, S7-400)](#reference-point-approach-and-evaluation-of-the-reference-signal-s7-300-s7-400-1)
- [Drive (S7-300, S7-400)](#drive-s7-300-s7-400-1)

#### Enables (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400-1)
- [Enabling encoder signal diagnostics (S7-300, S7-400)](#enabling-encoder-signal-diagnostics-s7-300-s7-400-1)

##### Enabling group diagnostics (S7-300, S7-400)

###### Group diagnostics

You enable group diagnostics by ticking the corresponding options box.

When group diagnostics is enabled, an encoder error (ERR_ENCODER), no load voltage (ERR_2L+) or a parameter assignment error will result in a channel-specific diagnostics.

##### Enabling encoder signal diagnostics (S7-300, S7-400)

###### Encoder signal diagnostics

You enable encoder signal diagnostics by ticking the corresponding options box.

A simultaneous edge change of the signals A* and B* with "Encoder signal diagnostics" enabled leads to an error.

#### Encoder and axes (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling dosing mode (S7-300, S7-400)](#enabling-dosing-mode-s7-300-s7-400-1)
- [Selecting encoder inputs (S7-300, S7-400)](#selecting-encoder-inputs-s7-300-s7-400)
- [Enabling reversal of direction of rotation (S7-300, S7-400)](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400-1)
- [Selecting axis type (S7-300, S7-400)](#selecting-axis-type-s7-300-s7-400-1)
- [Specifying end of rotary axis (S7-300, S7-400)](#specifying-end-of-rotary-axis-s7-300-s7-400-1)

##### Enabling dosing mode (S7-300, S7-400)

###### Dosing mode

You enable dosing mode by ticking the corresponding options box.

In [dosing mode](#overview-of-the-functions-s7-300-s7-400) the 1PosU only evaluates the encoder signal A*. As a result, the distance can only be changed in the positive direction. The actual value is incremented at each positive edge.

##### Selecting encoder inputs (S7-300, S7-400)

###### Encoder inputs

Different sensors can be connected to the encoder inputs:

- Sourcing output/push pull
- Sinking output

  > **Note**
  >
  > If you have selected the "Sinking output" setting with for the "Encoder inputs" parameter, you must use the M-switching sensors.

Select the output circuit of the encoder in use for the signals A*, B* and N* from the drop-down list box.

##### Enabling reversal of direction of rotation (S7-300, S7-400)

###### Reversal of direction of rotation

You enable reversal of direction of rotation by ticking the corresponding options box.

You can use the "Reversal of direction of rotation" parameter to adapt the direction of rotation of the encoder to that of the drive and the axis.

In [dosing mode](#overview-of-the-functions-s7-300-s7-400), reversal of the direction of rotation is not possible.

##### Selecting axis type (S7-300, S7-400)

###### Axis types

The 1PosU positioning module can control the following axis types:

- Linear axis

  A linear axis is an axis which has a limited physical traversing range.

  ![Axis types](images/24575900299_DV_resource.Stream@PNG-en-US.png)
- Rotary axis

  The rotary axis is an axis whose traversing range is not restricted by mechanical stops.

  ![Axis types](images/24575948427_DV_resource.Stream@PNG-en-US.png)

##### Specifying end of rotary axis (S7-300, S7-400)

###### End of rotary axis

This parameter is only relevant for the "Rotary axis" axis type.

The value "end of rotary axis" is the theoretical maximum value that the actual value can reach. The theoretically highest value is however never displayed, because it physically identifies the same position as the start of the rotary axis (0).

The displayed value jumps at

- high limit violated of (end of rotary axis – 1) to 0
- low limit violated of 0 to (end of rotary axis – 1)

Permitted value range for the end of the rotary axis: 1 … 16 777 215  
Specifying "0" causes a configuration error.

#### Digital inputs (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting minus limit switch and plus limit switch (S7-300, S7-400)](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400-1)
- [Selecting reduction cam (S7-300, S7-400)](#selecting-reduction-cam-s7-300-s7-400-1)

##### Selecting minus limit switch and plus limit switch (S7-300, S7-400)

###### Function of the hardware limit switches

The two digital inputs (DI0 and DI1) are evaluated by the 1PosU as limit switches:

- DI0 is the minus limit switch and limits the operating range in the minus direction.
- DI1 is the plus limit switch and limits the operating range in the plus direction.

You can assign parameters to the hardware limit switches **separately as NC or NO contacts**.

The hardware limit switches are evaluated with linear axes and rotary axes.

Only the hardware limit switch that lies in the direction in which the drive is being moved is evaluated.

This enables you to move away from a hardware limit switch without additional error acknowledgment by moving in the other direction if you reach or overrun a hardware limit switch.

The current signal level of the digital inputs is displayed in the feedback interface, delayed by the update rate.

The following table shows how the hardware limit switches work in the individual MODEs.

| MODE | Function of the hardware limit switches |
| --- | --- |
| Reference point approach | The 1PosU executes an automatic direction reversal at the hardware limit switch. |
| Inching | The motion of the axis is halted on the hardware limit switch, all 3 digital outputs are set to 0, and the POS_ERR feedback bit is reported. |
| Absolute Positioning |  |
| Relative Positioning |  |

###### Starting on the hardware limit switch

The following table shows the reaction of the 1PosU when starting MODEs on the hardware limit switch.

| Direction | 1PosU reactions |
| --- | --- |
| Starting into the operating range | The 1PosU starts the specified MODE. |
| Starting away from the operating range | The POS_ERR = 1 feedback bit is set. |

##### Selecting reduction cam (S7-300, S7-400)

###### Function of the reduction cam

The digital input DI2 is evaluated as a reduction cam or latch input by 1PosU:

- as a reduction cam with MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)" and with JOB 9 "[Evaluate referencing signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)"
- as a latch input with JOB 10 "[Latch function](#latch-function-job-10-s7-300-s7-400)"

You can assign parameters to the hardware limit switches separately as **NC or NO contacts**.

#### Reference point approach and evaluation of the reference signal (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting reference signal (S7-300, S7-400)](#selecting-reference-signal-s7-300-s7-400-1)
- [Selecting reference switch (S7-300, S7-400)](#selecting-reference-switch-s7-300-s7-400-1)
- [Selecting start direction (S7-300, S7-400)](#selecting-start-direction-s7-300-s7-400-1)

##### Selecting reference signal (S7-300, S7-400)

###### Reference signal

The "Reference signal" parameter defines the relevant switch or combination of switches and zero marks for MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)" and JOB 9 "[Evaluate reference signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)". The following are selectable:

- Reference switch and zero mark
- Reference switch
- Zero mark

You select the type of reference switch with the "[Reference switch](#selecting-reference-switch-s7-300-s7-400-1)" parameter.

##### Selecting reference switch (S7-300, S7-400)

###### Reference switch

The "Reference switch" parameter defines the relevant switch and the reference direction in which the switch must be overrun. The following are selectable:

- Reduction cam towards minus
- Reduction cam towards plus
- Limit switch minus
- Limit switch plus

These parameters are only relevant if you have selected it with "[reference signal](#selecting-reference-signal-s7-300-s7-400-1)"

- Reference switch and zero mark

  or
- Reference switch

##### Selecting start direction (S7-300, S7-400)

###### Start direction

The "Start direction" parameter defines the start direction for the MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)". The following are selectable:

- Plus
- Minus

#### Drive (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting control mode (S7-300, S7-400)](#selecting-control-mode-s7-300-s7-400-1)
- [Entering the switch-off difference (S7-300, S7-400)](#entering-the-switch-off-difference-s7-300-s7-400-1)
- [Entering the changeover difference (S7-300, S7-400)](#entering-the-changeover-difference-s7-300-s7-400-1)
- [Entering the delay time for the direction change (S7-300, S7-400)](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400-1)

##### Selecting control mode (S7-300, S7-400)

###### Control mode

The"Control mode" parameter defines the function of the digital outputs for the [control of the drive](#axis-drive-and-encoder-s7-300-s7-400). The following are selectable:

- Control mode 0:

  - DO0 travel minus
  - DO1 travel plus
  - DO2 rapid/creep feed
- Control mode 1:

  - DO0 rapid feed
  - DO1 creep feed (rapid feed is 0)
  - DO2 traverse plus (1 )/ traverse minus (0)

##### Entering the switch-off difference (S7-300, S7-400)

###### Switch-off difference

[Switch-off difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from creep speed to 0.

If the switch-off difference ≥ the changeover difference, there is no changeover point. There is no deceleration from rapid traverse to creep speed; the response is executed directly at the switch-off point.

Valid value range:

- 0 to 65,535

You can use [JOB 3](#changing-the-switch-off-difference-job-3-s7-300-s7-400) to change the switch-off difference.

##### Entering the changeover difference (S7-300, S7-400)

###### Changeover difference

[Changeover difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from rapid traverse to creep speed.

Valid value range:

- 0 to 65,535

You can use [JOB 4](#changing-the-changeover-difference-job-4-s7-300-s7-400) to change the changeover difference.

##### Entering the delay time for the direction change (S7-300, S7-400)

###### T<sub>min</sub> direction change

The "T<sub>min</sub> direction change" parameter defines the delay time for the direction change. The digital outputs are switched off, and a change of direction by T<sub>min</sub> is executed with a delay. T<sub>min</sub> is effective at each change of direction during a run.

T<sub>min</sub> does not work when starting after POS_DONE = 1 or POS_ERR = 1.

Valid value range:

- 0 to 255

Your input value is multiplied by 10. You thus specify T<sub>min</sub> in increments of 10 ms (for example, 0 ms, 10 ms or 2550 ms).

### Parameters for SSI encoders (S7-300, S7-400)

This section contains information on the following topics:

- [Enables (S7-300, S7-400)](#enables-s7-300-s7-400-2)
- [Encoder and axes (S7-300, S7-400)](#encoder-and-axes-s7-300-s7-400-2)
- [Digital inputs (S7-300, S7-400)](#digital-inputs-s7-300-s7-400-2)
- [Drive (S7-300, S7-400)](#drive-s7-300-s7-400-2)

#### Enables (S7-300, S7-400)

This section contains information on the following topics:

- [Enabling group diagnostics (S7-300, S7-400)](#enabling-group-diagnostics-s7-300-s7-400-2)
- [Enabling encoder signal diagnostics (S7-300, S7-400)](#enabling-encoder-signal-diagnostics-s7-300-s7-400-2)

##### Enabling group diagnostics (S7-300, S7-400)

###### Group diagnostics

You enable group diagnostics by ticking the corresponding options box.

When group diagnostics is enabled, an encoder error (ERR_ENCODER), no load voltage (ERR_2L+) or a parameter assignment error will result in a channel-specific diagnostics.

##### Enabling encoder signal diagnostics (S7-300, S7-400)

###### Encoder signal diagnostics

You enable encoder signal diagnostics by ticking the corresponding options box.

With "Encoder signal diagnostics" enabled, encoder signals D, /D are monitored for short circuit and wire break. Monitoring of the frame is carried out additionally (start bit and stop bit).

#### Encoder and axes (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting encoder type (S7-300, S7-400)](#selecting-encoder-type-s7-300-s7-400)
- [Selecting the transmission rate (S7-300, S7-400)](#selecting-the-transmission-rate-s7-300-s7-400)
- [Selecting increments per encoder revolution (S7-300, S7-400)](#selecting-increments-per-encoder-revolution-s7-300-s7-400)
- [Selecting the number of encoder revolutions (S7-300, S7-400)](#selecting-the-number-of-encoder-revolutions-s7-300-s7-400)
- [Enabling reversal of direction of rotation (S7-300, S7-400)](#enabling-reversal-of-direction-of-rotation-s7-300-s7-400-2)
- [Selecting axis type (S7-300, S7-400)](#selecting-axis-type-s7-300-s7-400-2)

##### Selecting encoder type (S7-300, S7-400)

###### Encoder type

Select the encoder in use from the drop-down list:

- Single-turn encoder (SSI 13 bit)
- Multi-turn encoder (SSI 25 bit)

##### Selecting the transmission rate (S7-300, S7-400)

###### Transmission rate

With the "transmission rate" parameter, you define the data transmission rate between the SSI encoder and the positioning module.

The maximum transmission rate is dependent on the cable length:

- 320 m → 125 kHz
- 160 m → 250 kHz
- 60 m → 500 kHz
- 20 m → 1 MHz

##### Selecting increments per encoder revolution (S7-300, S7-400)

###### Increments per encoder revolution

The "Increments per encoder revolution" parameter defines the number of increments an absolute encoder returns per revolution.

For the limits you have to differentiate between the individual encoder models. Only values to the power of 2 are selectable.

- Single-turn encoder (number of revolutions = 1) with 13-bit frame length:

  - minimum value = 4
  - maximum value = 8192
- Multiturn encoder (number of revolutions > 1) with 25-bit message frame length:

  - Minimum value = 4
  - Maximum value = 8192

##### Selecting the number of encoder revolutions (S7-300, S7-400)

###### Number of encoder revolutions

This parameter is used to define the maximum number of revolutions of this encoder.

The entry is only relevant for multi-turn encoders. For single-turn encoders, the 1PosU sets the number of revolutions to 1.

Valid value range:

- 2 to 4096 in powers of 2

##### Enabling reversal of direction of rotation (S7-300, S7-400)

###### Reversal of direction of rotation

You enable reversal of direction of rotation by ticking the corresponding options box.

You can use the "Reversal of direction of rotation" parameter to adapt the direction of rotation of the encoder to that of the drive and the axis.

##### Selecting axis type (S7-300, S7-400)

###### Axis types

The 1PosU positioning module can control the following axis types:

- Linear axis

  A linear axis is an axis which has a limited physical traversing range.

  ![Axis types](images/24575900299_DV_resource.Stream@PNG-en-US.png)
- Rotary axis

  The rotary axis is an axis whose traversing range is not restricted by mechanical stops.

  ![Axis types](images/24575948427_DV_resource.Stream@PNG-en-US.png)

#### Digital inputs (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting minus limit switch and plus limit switch (S7-300, S7-400)](#selecting-minus-limit-switch-and-plus-limit-switch-s7-300-s7-400-2)
- [Selecting reduction cam (S7-300, S7-400)](#selecting-reduction-cam-s7-300-s7-400-2)

##### Selecting minus limit switch and plus limit switch (S7-300, S7-400)

###### Function of the hardware limit switches

The two digital inputs (DI0 and DI1) are evaluated by the 1PosU as limit switches:

- DI0 is the minus limit switch and limits the operating range in the minus direction.
- DI1 is the plus limit switch and limits the operating range in the plus direction.

You can assign parameters to the hardware limit switches **separately as NC or NO contacts**.

The hardware limit switches are evaluated with linear axes and rotary axes.

Only the hardware limit switch that lies in the direction in which the drive is being moved is evaluated.

This enables you to move away from a hardware limit switch without additional error acknowledgment by moving in the other direction if you reach or overrun a hardware limit switch.

The current signal level of the digital inputs is displayed in the feedback interface, delayed by the update rate.

The following table shows how the hardware limit switches work in the individual MODEs.

| MODE | Function of the hardware limit switches |
| --- | --- |
| Reference point approach | The 1PosU executes an automatic direction reversal at the hardware limit switch. |
| Inching | The motion of the axis is halted on the hardware limit switch, all 3 digital outputs are set to 0, and the POS_ERR feedback bit is reported. |
| Absolute Positioning |  |
| Relative Positioning |  |

###### Starting on the hardware limit switch

The following table shows the reaction of the 1PosU when starting MODEs on the hardware limit switch.

| Direction | 1PosU reactions |
| --- | --- |
| Starting into the operating range | The 1PosU starts the specified MODE. |
| Starting away from the operating range | The POS_ERR = 1 feedback bit is set. |

##### Selecting reduction cam (S7-300, S7-400)

###### Function of the reduction cam

The digital input DI2 is evaluated as a reduction cam or latch input by 1PosU:

- as a reduction cam with MODE 3 "[Reference point approach](#reference-point-approach-mode-3-s7-300-s7-400-1)" and with JOB 9 "[Evaluate referencing signal](#evaluating-the-reference-signal-job-9-s7-300-s7-400)"
- as a latch input with JOB 10 "[Latch function](#latch-function-job-10-s7-300-s7-400)"

You can assign parameters to the hardware limit switches separately as **NC or NO contacts**.

#### Drive (S7-300, S7-400)

This section contains information on the following topics:

- [Selecting control mode (S7-300, S7-400)](#selecting-control-mode-s7-300-s7-400-2)
- [Entering the switch-off difference (S7-300, S7-400)](#entering-the-switch-off-difference-s7-300-s7-400-2)
- [Entering the changeover difference (S7-300, S7-400)](#entering-the-changeover-difference-s7-300-s7-400-2)
- [Entering the delay time for the direction change (S7-300, S7-400)](#entering-the-delay-time-for-the-direction-change-s7-300-s7-400-2)

##### Selecting control mode (S7-300, S7-400)

###### Control mode

The"Control mode" parameter defines the function of the digital outputs for the [control of the drive](#axis-drive-and-encoder-s7-300-s7-400). The following are selectable:

- Control mode 0:

  - DO0 travel minus
  - DO1 travel plus
  - DO2 rapid/creep feed
- Control mode 1:

  - DO0 rapid feed
  - DO1 creep feed (rapid feed is 0)
  - DO2 traverse plus (1 )/ traverse minus (0)

##### Entering the switch-off difference (S7-300, S7-400)

###### Switch-off difference

[Switch-off difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from creep speed to 0.

If the switch-off difference ≥ the changeover difference, there is no changeover point. There is no deceleration from rapid traverse to creep speed; the response is executed directly at the switch-off point.

Valid value range:

- 0 to 65,535

You can use [JOB 3](#changing-the-switch-off-difference-job-3-s7-300-s7-400) to change the switch-off difference.

##### Entering the changeover difference (S7-300, S7-400)

###### Changeover difference

[Changeover difference](#basics-of-controlled-positioning-by-means-of-rapidcreep-feed-s7-300-s7-400) defines the distance from the target at which the drive is slowed down from rapid traverse to creep speed.

Valid value range:

- 0 to 65,535

You can use [JOB 4](#changing-the-changeover-difference-job-4-s7-300-s7-400) to change the changeover difference.

##### Entering the delay time for the direction change (S7-300, S7-400)

###### T<sub>min</sub> direction change

The "T<sub>min</sub> direction change" parameter defines the delay time for the direction change. The digital outputs are switched off, and a change of direction by T<sub>min</sub> is executed with a delay. T<sub>min</sub> is effective at each change of direction during a run.

T<sub>min</sub> does not work when starting after POS_DONE = 1 or POS_ERR = 1.

Valid value range:

- 0 to 255

Your input value is multiplied by 10. You thus specify T<sub>min</sub> in increments of 10 ms (for example, 0 ms, 10 ms or 2550 ms).

### 1PosU control and feedback interface  (S7-300, S7-400)

This section contains information on the following topics:

- [1PosU control interface (S7-300, S7-400)](#1posu-control-interface-s7-300-s7-400)
- [1PosU feedback interface (S7-300, S7-400)](#1posu-feedback-interface-s7-300-s7-400)

#### 1PosU control interface (S7-300, S7-400)

##### Assignment of the Control Interface

The table below shows the assignment of the 1PosU control interface (outputs).

| Address | Assignment |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | Bits 0.7 to 0.4 stand for the MODEs |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 |  |  |
| 0 | 0 | 0 | 0 | MODE 0 = Stop |  |  |
| 0 | 0 | 0 | 1 | MODE 1 = Inching |  |  |
| 0 | 0 | 1 | 1 | MODE 3 = Reference point approach |  |  |
| 0 | 1 | 0 | 0 | MODE 4 = Relative positioning |  |  |
| 0 | 1 | 0 | 1 | MODE 5 = Absolute positioning |  |  |
| Bit 3: SPEED (SPEED = 0 is creep speed; SPEED = 1 is rapid traverse)  Bit 2: DIR_M  Bit 1: DIR_P  Bit 0: START |  |  |  |  |  |  |
| Bytes 1 to 3 | with MODE 3 = Reference point approach: reference point coordinates |  |  |  |  |  |
| with MODE 4 = Relative positioning: distance |  |  |  |  |  |  |
| with MODE 5 = Absolute positioning: target |  |  |  |  |  |  |
| Byte 4 | Bits 4.7 to 4.4 stand for the JOBs |  |  |  |  |  |
| Bit | 7 | 6 | 5 | 4 |  |  |
| 0 | 0 | 0 | 0 | JOB 0 = Cancel JOB processing |  |  |
| 0 | 0 | 0 | 1 | JOB 1 = Set actual value |  |  |
| 0 | 0 | 1 | 0 | JOB 2 = Shift encoder range (only at SSI encoders) |  |  |
| 0 | 0 | 1 | 1 | JOB 3 = Change switch-off difference |  |  |
| 0 | 1 | 0 | 0 | JOB 4 = Change changeover difference |  |  |
| 1 | 0 | 0 | 1 | JOB 9 = Evaluate the reference signal |  |  |
| 1 | 0 | 1 | 0 | JOB 10 = Latch function |  |  |
| 1 | 0 | 1 | 1 | JOB 11 = Define the settings for monitoring the direction of rotation |  |  |
| 1 | 1 | 1 | 1 | JOB 15 = Display current values |  |  |
| Bit 3: EXTF_ACK  Bit 2: Reserved = 0  Bit 1: Reserved = 0  Bit 0: JOB_REQ |  |  |  |  |  |  |
| Bytes 5 to 7 | In accordance with the selected JOBs:  - with JOB 1 = Actual value coordinates: - with JOB 2 = Offset: - with JOB 3 = Switch-off difference - with JOB 4 = Changeover difference - withJOB 9 = Reference point coordinates - with JOB 10   - Byte 5: Bit 0 = latch at positive edge at DI2   - Byte 5: Bit 1 = latch at negative edge at DI2 - with JOB 11 = Distance difference for monitoring of the direction of rotation - with JOB 15   - Byte 5: 0 = Residual distance   - Byte 5: 1 = Actual speed   - Byte 5: 2 = Error information |  |  |  |  |  |

#### 1PosU feedback interface (S7-300, S7-400)

##### Assignment of the Feedback Interface

The following table shows the assignment of the 1PosU feedback interface (inputs).

| Address | Assignment |
| --- | --- |
| Byte 0 | Bit 7: ERR_ENCODER  Bit 6: STATUS DO 2  Bit 5: STATUS DO 1  Bit 4: STATUS DO 0  Bit 3: SYNC  Bit 2: POS_DONE  Bit 1: POS_ERR  Bit 0: POS_ACK |
| Bytes 1 to 3 | Actual value |
| Byte 4 | Bit 7: ERR_2L+  Bit 6: STATUS DI 2 Reduction cam  Bit 5: STATUS DI 1 Limit switch plus  Bit 4: STATUS DI 0 Limit switch minus  Bit 3: Reserved = 0  Bit 2: LATCH_DONE  Bit 1: JOB_ERR  Bit 0: JOB_ACK |
| Bytes 5 to 7 | Feedback value |

## Diagnostics of 1PosU (S7-300, S7-400)

This section contains information on the following topics:

- [Diagnostics using the LED display (S7-300, S7-400)](#diagnostics-using-the-led-display-s7-300-s7-400)
- [Error types (S7-300, S7-400)](#error-types-s7-300-s7-400)

### Diagnostics using the LED display (S7-300, S7-400)

#### LED display on the 1PosU

![LED display on the 1PosU](images/23270263819_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Group error (red) |
| ② | Status display for a change in an actual value (green) |
| ③ | Positioning underway (green) |
| ④ | Status displays for digital inputs (green) |

#### Status and error displays by means of LEDs on the 1PosU

The table below shows the status and error displays on the 1PosU.

| Event (LED) |  |  |  |  |  |  | Cause | Remedy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF | 1 | 5 | 2 | UP | DN | POS |  |  |
| On |  |  |  |  |  |  | No parameter assignment. Diagnostic message. | Check the parameter settings. Analyze the diagnostic data. |
|  | On |  |  |  |  |  | DI 0 is activated. |  |
|  |  | On |  |  |  |  | DI 1 is activated. |  |
|  |  |  | On |  |  |  | DI 2 is activated. |  |
|  |  |  |  | On |  |  | In the case of actual value change from lower to higher values |  |
|  |  |  |  |  | On |  | In the case of actual value change from higher to lower values |  |
|  |  |  |  |  |  | On | Positioning is running and one of the 3 digital outputs is set. |  |

### Error types (S7-300, S7-400)

For information on the structure of the channel-related diagnostics, refer to the manual on the interface module used in your ET 200S station.

#### 1PosU error types

The following table shows the error types on the 1PosU.

| Error type |  | Meaning | Remedy |
| --- | --- | --- | --- |
| 1<sub>D</sub> | 00001:  Short circuit | Short circuit of the sensor supply. | Check the wiring to the sensor. Correct the process wiring. |
| 16<sub>D</sub> | 10000:  Parameter assignment error | Parameters have not been assigned to the module. | Correct the parameter assignment. |
| 17<sub>D</sub> | 10001:  Load voltage 2L + missing | Power supply voltage not present or too low. | Correct the process wiring. Check the supply voltage. |
| 26<sub>D</sub> | 11010:  External error | Wire break/short circuit of the sensor signals.  Wire break in the sensor cable, or sensor cable is not connected.   Sensor is defective or there are faults.  Sensor type, transmission rate, and monoflop time do not correspond to the sensor connected; programmable sensors do not correspond to the settings on the module. | Correct the process wiring.  Correct the parameter assignment.  Replace the sensor. |
